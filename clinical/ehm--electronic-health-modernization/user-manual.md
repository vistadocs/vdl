---
title: Electronic Health Modernization User Manual
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: Electronic Health Modernization
app_code: EHM
app_name: Electronic Health Modernization
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - date
  - table
  - contents
  - report
  - appointment
  - span
  - clinic
  - consult
  - status
  - converted
page_count: 0
word_count: 16019
section_count: 14
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2026
revision_count: 15
revision_newest: 06/03/2025
revision_oldest: 01/11/2023
docx_url: "https://www.va.gov/vdl/documents/Clinical/Electronic_Health_Modernization_(EHM)/ehm_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Electronic_Health_Modernization_(EHM)/ehm_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=439"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Electronic Health Modernization (EHM)

  User Guide
---

![](electronic-health-modernization-user-manual/001.png)

March 2026

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date       | Revision | Description                          | Author  |
|------------|----------|--------------------------------------|---------|
| 06/03/2025 | 15       | Tweaks for EHM\*1\*13                | EHRM-IO |
| 01/23/2025 | 14       | Tweaks for EHM\*1\*13                | EHRM-IO |
| 12/10/2024 | 13       | Tweaks for EHM\*1\*13                | EHRM-IO |
| 10/17/2024 | 12       | Updated for EHM\*1\*15               | EHRM-IO |
| 08/21/2024 | 11       | Updated for EHM\*1\*13               | EHRM-IO |
| 07/30/2024 | 10       | Added EHM\*1\*15                     | EHRM-IO |
| 07/03/2024 | 9        | Updated for GMRC\*3\*192             | EHRM-IO |
| 07/01/2024 | 8        | Updated for EHM\*1\*13               | EHRM-IO |
| 06/05/2024 | 7        | Updated for EHM\*1\*13               | EHRM-IO |
| 4/25/24    | 6        | Updated for EHM\*1\*8                | EHRM-IO |
| 04/23/2024 | 5        | Updated for EHM\*1\*13               | EHRM-IO |
| 01/25/2024 | 4        | Updated for EHM\*1\*9 and EHM\*1\*14 | EHRM-IO |
| 08/03/2023 | 3        | Updated for EHM\*1\*4v5              | EHRM-IO |
| 07/25/2023 | 2        | EHM\*1\*10 added                     | EHRM-IO |
| 01/11/2023 | 1        | Initial user guide                   | EHRM-IO |

<span id="_Ref123892259" class="anchor"></span>Table 1: EHM Patches

Artifact Rationale

Per the Veteran-focused Integrated Process (VIP) Guide, the User’s Guide is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A User Guide is a technical communication document intended to give assistance to people using a particular system, such as VistA end users. It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most user guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The User Guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required if applicable to your product.

Table of Contents

Table of Figures

[Figure 1: Automated VistA Patching - Process Flow [13](#_Ref141871412)](#_Ref141871412)

Table of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [System Overview](#system-overview)
  - [Document Orientation](#document-orientation)
    - [Organization of the Manual](#organization-of-the-manual)
    - [Assumptions](#assumptions)
    - [Coordination](#coordination)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [Patches](#patches)
  - [EHM\1\2 – Image Migration](#ehm12-image-migration)
    - [System Configuration](#system-configuration)
    - [Data Flows](#data-flows)
    - [User Access Levels](#user-access-levels)
    - [Continuity of Operation](#continuity-of-operation)
    - [Using the Software](#using-the-software)
  - [EHM\1\4 – Automated VistA Patching Tool](#ehm14-automated-vista-patching-tool)
    - [System Configuration](#system-configuration-1)
    - [Data Flows](#data-flows-1)
    - [User Access Levels](#user-access-levels-1)
    - [Continuity of Operation](#continuity-of-operation-1)
    - [Using the Software](#using-the-software-1)
  - [EHM\1\8 – EHRM-IO Clinical Cutover Tools](#ehm18-ehrm-io-clinical-cutover-tools)
    - [System Configuration](#system-configuration-2)
    - [Data Flows](#data-flows-2)
    - [User Access Levels](#user-access-levels-2)
    - [Continuity of Operation](#continuity-of-operation-2)
    - [Using the Software / Options](#using-the-software-options)
  - [EHM\1\9 – EHRM-IO Kernel Cutover Tools](#ehm19-ehrm-io-kernel-cutover-tools)
    - [System Configuration](#system-configuration-3)
    - [Data Flows](#data-flows-3)
    - [User Access Levels](#user-access-levels-3)
    - [Continuity of Operation](#continuity-of-operation-3)
    - [Using the Software / Options](#using-the-software-options-1)
  - [EHM\1\10 – IFC and PRF HL7 Message Storage](#ehm110-ifc-and-prf-hl7-message-storage)
    - [System Configuration](#system-configuration-4)
    - [Data Flows](#data-flows-4)
    - [User Access Levels](#user-access-levels-4)
    - [Continuity of Operation](#continuity-of-operation-4)
    - [Using the Software / Options](#using-the-software-options-2)
  - [EHM\1\14 – HITT Menu](#ehm114-hitt-menu)
    - [System Configuration](#system-configuration-5)
    - [Data Flows](#data-flows-5)
    - [User Access Levels](#user-access-levels-5)
    - [Continuity of Operation](#continuity-of-operation-5)
    - [Using the Software / Options](#using-the-software-options-3)
  - [GMRC\3\192 – EHRM-IO Cutover Tools](#gmrc3192-ehrm-io-cutover-tools)
    - [System Configuration](#system-configuration-6)
    - [Data Flows](#data-flows-6)
    - [User Access Levels](#user-access-levels-6)
    - [Continuity of Operation](#continuity-of-operation-6)
    - [Using the Software / Options](#using-the-software-options-4)
  - [EHM\1\13 – CONVERTED APPOINTMENT MAINTENANCE](#ehm113-converted-appointment-maintenance)
    - [User Functionality](#user-functionality)
    - [System Configuration](#system-configuration-7)
    - [Data Flows](#data-flows-7)
    - [User Access Levels](#user-access-levels-7)
    - [Continuity of Operation](#continuity-of-operation-7)
    - [Using the Software / Options](#using-the-software-options-5)
  - [EHM\1\15 – Automated Patient Discharge Tool](#ehm115-automated-patient-discharge-tool)
    - [System Configuration](#system-configuration-8)
    - [Data Flows](#data-flows-8)
    - [User Access Levels](#user-access-levels-8)
    - [Continuity of Operation](#continuity-of-operation-8)
    - [Using the Software / Options](#using-the-software-options-6)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
Electronic Health Modernization (EHM) Veterans Health Information Systems and Technology Architecture (VistA) patches support the Electronic Health Record Modernization Integration Office (EHRM-IO) during conversion from VistA to Cerner Millennium.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This User Guide provides information about the functionality of EHM Package software for users.

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHM patches have no single system orientation. Patches (see Table 1) support the conversion process rather than any single system.

| Patch    | Description                   |
|--------------|-----------------------------------|
| EHM\*1\*2    | Image Migration                   |
| EHM\*1\*4    | Automated VistA Patching          |
| EHM\*1\*8    | EHRM-IO Clinical Cutover Tools    |
| EHM\*1\*9    | EHRM-IO Kernel Cutover Tools      |
| EHM\*1\*10   | IFC and PRF HL7 Message Storage   |
| GMRC\*3\*192 | Consult Update using Grouper      |
| EHM\*1\*14   | HITT Menu                         |
| EHM\*1\*13   | Converted Appointment Maintenance |
| EHM\*1\*15   | Automated Patient Discharge Tool  |

<span id="_Toc170907094" class="anchor"></span>Table 4: EHM\*1\*8 Menus and Security Keys

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audience for this document are end users of EHM patches.

### Organization of the Manual 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the following assumed experience/skills of the audience:

- User has basic knowledge of the operating system (such as the use of commands, menu options, and navigation tools).
- User has been provided the appropriate active roles, menus, and security keys required for the EHM package.
- User has completed any prerequisite training.

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees or contractors of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified*.*

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the VA of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA*.*

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses several methods to highlight different aspects of the material.

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

> <span id="_Toc199858071" class="anchor"></span>Table 2. Documentation Symbols and Descriptions

| Symbol                                                                                                                                                                                                                                 | Description                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](electronic-health-modernization-user-manual/002.png)                                                        | NOTE: Used to inform the reader of general information including references to additional reading material |
| ![](electronic-health-modernization-user-manual/003.png) | CAUTION: Used to caution the reader to take special notice of critical information                     |

<span id="_Ref119997050" class="anchor"></span>Table 5: EHM Menus and Security Keys

- Descriptive text is presented in a proportional font (as represented by this font).
- “Snapshots” of computer online displays (i.e., character-based screen captures/dialogs) and computer source code are shown in a non-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogs or forms).
- Use the pre-defined styles exported with the template for all formatting (e.g., paragraph text, bullets, enumeration, etc.).
- User's responses to online prompts (e.g., manual entry, taps, clicks, etc.) will be boldface type.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security key (e.g., the XUPROGMODE key).
- Conventions for displaying TEST data in this manual are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either “000” or “666”.
- Patient and user names are formatted as follows:

> \<Application Name\>”PATIENT”,\<fictitious given name\>\<NUMBER\> and \<Application Name\>”USER”,\<fictitious given name\>\<NUMBER\>, respectively.

> The “Fictitious given name” represents a fabricated given name for the patient or user based on the application being released or the product name. For example, Master Veteran Index (MVI) software test patient and user names would be documented as follows: MVIPATIENT,ONE; MVIPATIENT,TWO; MVIPATIENT,THREE; etc. and MVIUSER,ONE; MVIUSER,TWO; etc.

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation associated with the EHM package can be found on the VA Software Documentation Library (VDL). The associated documents are:

| EHM User Manual      | ehm_ug.pdf |
|----------------------|------------|
| EHM Technical Manual | ehm_tm.pdf |

<span id="_Ref157070060" class="anchor"></span>Table 6: EHM Menus and Security Keys

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref390770787" class="anchor"></span>Table 3. Tier Support Contact Information”

<table>
<caption>Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Name</strong></th>
<th><strong>Role</strong></th>
<th><strong>Org</strong></th>
<th><strong>Contact Info</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OIT National Service Desk</td>
<td>Tier 1 Support</td>
<td>OIT</td>
<td><p><a href="mailto:Nationalservicedeskanr@va.gov">Nationalservicedeskanr@va.gov</a> </p>
<p>1-855-673-4357</p></td>
</tr>
<tr class="even">
<td>EHRM-IO/Release &amp; Interface Mgmt/VistA Patch</td>
<td>Tier 2 &amp; 3 Application Support</td>
<td>EHRM-IO</td>
<td><p><a href="mailto:ehrm-iovistamodernizationteam@va.gov">ehrm-iovistamodernizationteam@va.gov</a></p>
<p>ServiceNow Assignment Group: EHRM-IO TM PM</p></td>
</tr>
</tbody>
</table>

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

# Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EHM\*1\*2 – Image Migration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Image Migration patch creates and maintains a record of image associated entities – consults and Radiology reports – together with the attributes needed by Cerner to link images to them. Although installed at individual VistA sites, the image migration database uniquely identifies each such entity across the VA enterprise.

The EHM\*1\*2 patch is installed at a VistA site six (6) to twelve (12) months prior to its conversion to Cerner. After installation, a baseline of the image migration database is created by scanning the four (4) VistA files that house image associated entities:

1)  REQUEST/CONSULTATION (#123)
2)  RAD/NUC MED REPORTS (#74)
3)  DICOM GMRC TEMP LIST (#2006.5839)
4)  IMAGE STUDY (#2005.62)

Data is extracted from each of these files and loaded into the Image Migration file (#1606).

Images created after the baseline load are added to the Image Migration file when consults or Radiology procedures are resulted through subscribers to the relevant protocols.

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Image Migration software runs on a standard VistA system. It requires no additional software or hardware.

### Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All data flows supported by the Image Migration software are internal to VistA. The host file produced by the <u>Record Extraction</u> process requires use of Secure File Transfer Protocol (SFTP) to transmit as it contains Personal Identifiable Information (PII).

### User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Image Migration software needs users to use options to: 1) run baseline loads, 2) produce analyzer reports, 3) produce report extracts and 4) produce exception reports. External to the software, Image Migration requires users who can correct data conditions (e.g., missing Electronic Data Interchange Personal Identifier (EDIPI)) identified in the exception report.

### Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Image Migration software does not impact routine VistA operations.

### Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The main Image Migration menu is EHM IMAGE MENU. Image Migration options to run the baseline loads, the analyzers, the extraction reports and the exception reports are all available from this menu. Real-time maintenance is executed automatically by VistA whenever a result is posted against a Radiology or Consult procedure.

#### Baseline Loads

There are four(4) separate load options for Image Migration that correspond to the different data sources for image-associated entities and their corresponding images.

The user interaction for these options is as follows:

OK TO PROCEED? YES//

QUEUE PROCESS? YES//

Answer NO to the first question to terminate the option. Press ENTER or answer YES to continue.

Answer NO to the second question to runs the option on screen. Press ENTER or answer YES to the second questions and be prompted for the date/time when the queued task is to run.

IMPORTANT NOTE: Once a baseline load option has been run to completion, the option should be marked out of service so that it is not inadvertently executed twice.

#### Load Consults into Image Migration file (EHM_LOAD1ALL)

This option scans the REQUEST/CONSULTATION file (#123) and identifies consults that have images associated with them through TIU notes (file \#8925). If the image sets (stored in the IMAGE file (#2005)) are for DICOM images (file extensions .DCM and .TGA) then a record is added to the Image Migration file (#1606) for each of these consults.

When a record is added to the Image Migration file, an accession number is generated in the following format:

\<SITE NUMBER\> \_C \<Consult IEN right-justified, zero filled to 11 digits\>

For example, 541_C00001234567.

The time that EHM_LOAD1ALL takes to run will vary according to the site’s size and system load. The load took less than 10 minutes to run for a site with 1.77 million consults in file \#123.

#### Load Radiology Reports into Image Migration file (EHM_LOAD2ALL)

This option scans the RAD/NUC MED REPORTS file (#74) and identifies reports that have images associated with them. If the image sets (stored in the IMAGE file (#2005)) are for DICOM images (file extensions .DCM and .TGA) then a record is added to the Image Migration file (#1606) for each of these Radiology reports.

When a record is added to the Image Migration file, an accession number is generated in the following format:

\<SITE NUMBER\> \_R \<Radiology Report IEN right-justified, zero filled to 11 digits\>

For example, 541_R00007654321.

The time that EHM_LOAD2ALL takes to run will vary according to the site’s size and system load. The load took less than 80 minutes to run for a site with 850,000 reports in file \#74.

#### Load file \#206.5839 in Image Migration file (EHM_LOAD5839)

This option scans the DICOM GMRC TEMP LIST file (#2006.5839) and extracts the consult identifiers associated with the image sets stored here. If the image sets (stored in the IMAGE file (#2005)) are for Digital Imaging and Communications in Medicine (DICOM) images (file extensions .DCM and .TGA) then a record is added to the Image Migration file (#1606) for each of these consults.

The format of the accession number generated by this option is the same as for other consults described above.

> **NOTE:** Because of the nature of file \#2006.5839, running this option will likely not be done at the same time as the other baseline loads. Images stored in the DICOM GMRC TEMP LIST file were intended to be there temporarily. VistA options exist to move images in and out of the file. The load option, therefore, will not be run until just prior to conversion.

The time that EHM_LOAD5839 takes to run will vary according to the site’s size and system load. Experience so far has been 5-15 minutes for small and mid-size sites.

#### Load Image Studies into Image Migration file (EHM_LODSTUDY)

This option scans the IMAGE SERIES file (#2005.63) and identifies image studies that have DICOM images associated with them. Data is extracted from the IMAGE STUDY file (#2005.62) that determines whether the image study is a Radiology or Consult study. A record is added to or updated in the Image Migration file (#1606). The accession number generated is a Consult type or Radiology type as apppropriate.

> **NOTE:** All images stored in the new Service Object Pair (SOP) file (#2005.62 and 2005.63) are DICOM.

The time that EHM_LODSTUDY takes to run will vary according to the site’s size and system load. Experience so far has been 10-20 minutes for small and mid-size sites.

#### Image v. Image Migration Analysis

#### Analyze Old SOP Images v. Image Migration file (EHM_EHMANLZR-OLDSOP)

This option does the opposite of what the Consult and Radiology baseline loads do. The baseline loads start in the REQUEST/CONSULTATION file (#123) and in the RAD/NUC MED REPORTS file (#74) and trace through to the IMAGE file (#2005). The analyzer starts in the Image file and traces back to Consult or Radiology Report file. In so doing, it identifies images not linked to the Image Migration file (#1606). It then determines why the images are unlinked and accounts for the differences.

The user interaction for these options is as follows:

OK TO PROCEED? YES//

QUEUE PROCESS? YES//

Answer NO to the first question to terminate the option. Press ENTER or answer YES to continue.

Answer NO to the second question to runs the option on screen. Press ENTER or answer YES to the second questions and be prompted for the date/time when the queued task is to run.

The time that EHM_EHMANLZR-OLDSOP takes to run will vary according to the site’s size and system load. Experience so far has been less than 60 minutes to run to completion for small and mid-size sites.

The output of the analyzer is a MailMan message is shown below.

Output of Image v. Image Migration File analyzer

EHMUTIL: Image v. Image Migration File

Date/Time: Apr 25, 2022@12:22:56

==========================================================================

TOTAL IMAGES SCANNED: 151,674,373

NUMBER OF PARENTS: 5,993,748

NUMBER WITH DICOM IMAGES: 1,919,370

NUMBER LINKED TO RADIOLOGY: 1,700,112

NUMBER LINKED TO CONSULTS: 219,129

NUMBER OF CONSULT STUDIES WITH NO TIU NOTES: 27,553

PARENT IMAGES NOT LINKED: 129

NUMBER OF UNLINKED RADIOLOGY STUDIES NOT IN FILE \#74: 79

NUMBER OF UNLINKED RADIOLOGY STUDIES BY STATUS:

PD: 10 - WITH ZERO IMAGES:

V: 7 - WITH ZERO IMAGES: 6

...CONSULT PROCEDURE (CON/PROC): 9 - WITH ZERO IMAGES: 0

...CONSULT PROCEDURE (TELEDERMATOLOGY (PUGET SOUND)): 5 - WITH ZERO IMAGES: 1

...CONSULT PROCEDURE (TELEDERMATOLOGY IFC (PUGET SOUND)): 19 - WITH ZERO IMAGES: 9

==========================================================================

SUMMARY

\- UNLINKED IMAGE SETS: 129

\* RADIOLOGY

\- NOT IN FILE \#74: 79

\- DELETED OR PROBLEM DRAFT: 10

\- ZERO IMAGE REPORTS: 6

\* CONSULTS

\- ZERO IMAGE CONSULTS: 10

\* REMAINDER: 24

#### Analyze New SOP Images v. Image Migration file (EHM_EHMANLZR-NEWSOP)

This analyzer option identifies images in the IMAGE STUDY (#2005.62) and IMAGE SERIES (#2005.63) files that are not linked to the Image Migration file (#1606). It then determines why the images are unlinked and accounts for the differences.

The user interaction for these options is the same as for the other analyzer option.

The time that EHM_EHMANLZR-NEWSOP takes to run will vary according to the site’s size and system load. Experience so far has been less than 10 minutes to run to completion for small and mid-size sites.

The output of this analyzer is akin to that shown previously.

#### Analyze Image Migration Records by Site and Date (EHM_EHMANLZR-STATS)

This option scans the Image Migration files and extracts ordering site and examination date. It produces a report (see below). There is no user interaction to perform the analysis and to produce the report.

Analysis by Site and Date

Image Migration Record Statistics

---------------------------------

Total records: 1,693,039

Type Count

--------- ------------

CONSULT 193,008

RADIOLOGY 1,500,031

--------- ------------

Total 1,693,039

Site Type Count

---------------------------------------- --------- ------------

AMERICAN LAKE (VAMC) (663A4) CONSULT 50,164

RADIOLOGY 400,039

BOISE VA MEDICAL CENTER (531) CONSULT 11

RADIOLOGY 0

JONATHAN M. WAINWRIGHT VAMC (687) CONSULT 5

RADIOLOGY 0

MANN-GRANDSTAFF VAMC (668) CONSULT 8

RADIOLOGY 0

PORTLAND VA MEDICAL CENTER (648) CONSULT 1

RADIOLOGY 0

SAN FRANCISCO VAMC (662) CONSULT 1

RADIOLOGY 0

SEATTLE VA MEDICAL CENTER (663) CONSULT 142,818

RADIOLOGY 1,099,992

---------------------------------------- --------- ------------

Total 1,693,039

Year Type Count

---------- --------- ------------

2014 CONSULT 15,410 Note: This portion of the

RADIOLOGY 88,884 report was truncated

2015 CONSULT 17,875 for display purposes.

RADIOLOGY 88,854 The total shown at the

2016 CONSULT 22,178 bottom is not correct

RADIOLOGY 86,097 for the portion of the

2017 CONSULT 22,671 report shown here.

RADIOLOGY 85,335

2018 CONSULT 23,896

RADIOLOGY 85,045

2019 CONSULT 24,066

RADIOLOGY 80,720

2020 CONSULT 7,369

RADIOLOGY 17,213

---------- --------- ------------

Total 1,693,039

#### Real-time Maintenance

Real-time maintenance kicks in once the baseline loads are complete. Its purpose is to update the Image Migration file (#1606) with new or updated Radiology reports or Consults. No user interaction is required for real-time maintenance. When a result is posted for a Radiology exam or for a Consult exam, Image Migration software embedded in protocols is executed automatically.

#### Record Extraction

#### Generate Image Migration Extract File (EHM_EHMIMGRP)

This option is used to produce a file of Image Migration records that can be transmitted to Cerner. Each record produced contains the following data:

1.  Last Name
2.  First Name
3.  Middle Name
4.  EDIPI
5.  Date of Birth
6.  Gender
7.  Accession Number
8.  Exam Date
9.  Exam Time
10. Modality Type List – comma-separated list of the modalities employed in the study
11. Image Set UID – For images that are sourced in the IMAGE file (#2005), this is the PACS UID (field \#60) of the parent image. For images that are sourced in the IMAGE STUDY file (#2005.62), this is the STUDY INSTANCE UID (field \#.01).
12. Image Count – this is the number of images associated with the image set
13. Record Type – “RAD” for Radiology images sets, “TIU” for Consult images sets that are linked to TIU notes, “CON” for Consult image sets that are not linked to TIU notes.
14. Report IEN List – For record type “TIU”, this is a comma-separated list of TIU notes associated with the image set. For record type “RAD”, this is the IEN of the Radiology Report.
15. Consult Procedure – For record type “CON”, this is the consult procedure.
16. Other Case List – For record type “RAD”, this is the list of other case numbers.

The user interaction for this option is as follows:

Include Radiology Exams? NO//

Include Consults? NO//

Select examination date range? NO//

Start Date of Range:

End Date of Range:

Only consults without TIU Notes? NO//

Include previously extracted records? NO//

Answer YES to include records for Radiology reports. NO excludes Radiology reports from the extract. Answer YES to the second question include records for consults. NO excludes Consults from the extract. If NO is entered for both of the first two questions, the option exits as nothing was selected to be extracted.

Answer YES to the third question to extract records only for a range of examination dates. Answer NO to extract records for all examination dates. If YES is entered for the date range question, the user is then prompted for the start and end dates of the range. If NO is entered, the start and end date questions are not asked.

If YES is entered for the “include consults” question, the user is prompted to include only consults without TIU notes. A YES response to this question extracts only consult records that are not associated with a TIU note. A NO response extracts all consult records.

The final question determines whether previously extracted records are to be included in the current extract. Answer YES to include records that have appeared on a previous record extraction. Answer NO to include only records that have not previously been extracted.

The user is then prompted for an output device. At this point, the extraction process can be queued.

#### Exception Recording and Reporting

#### Exception Recording

Exception recording occurs during record extraction when a candidate record is checked and one or more data items fails validation. Exceptions are stored in the Image Migration Exception file (#1606.5).

At present, there are two (2) reasons a record can be failed to be extracted. They are:

1.  EDIPI missing
2.  EDIPI multiple

#### Generate Image Migration Exception Report (EHM_EHMEXCP)

This option is used to display the exceptions recorded during record extraction. The output appears as follows:

1.  Exception Date – this is the date when the extract was run
2.  Accession Number – this is the accession number of the rejected Image Migration record
3.  Patient – this is the patient’s name
4.  Reason – this is the exception reason

After each record, a message will appear if the exception reason has been corrected. For example, if the exception reason was “EDIPI Missing” and an EDIPI was then assigned to the patient, a message reading EDIPI CHANGED FROM ‘MISSING’ TO ‘1234567890’ will be displayed.

The user interaction for this option is as follows:

Start Date of Range:

End Date of Range:

Exclude test patients (name begins with ZZ) NO//

The user is then prompted for an output device. At this point, the extraction process can also be queued. If the report is run interactively, the user is prompted Continue? YES// as the screen fills.

## EHM\*1\*4 – Automated VistA Patching Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the Automated VistA Patching Tool is to automate, to the extent possible, the process of loading and installing patches in VistA test environments maintained by Independent Verification and Validation (IV&V) system administrators.

<span id="_Ref141871412" class="anchor"></span>Figure 1: Automated VistA Patching - Process Flow

![](electronic-health-modernization-user-manual/004.png)

As shown in Figure 1, the Automated VistA Patching Tool receives VistA patches from Forum and analyzes them for suitability for automatic loading and installation. If a patch can be automatically loaded, the Tool loads and backs it up. The backup patch is sent to the local instance installation team as a MailMan message[^1].

The Tool then determines if the patch can be automatically installed, and, if so, installs it. If the patch is not eligible for automatic loading and installing, its parent mail message is forwarded to the local instance installation team for manual processing.

If the patch is loaded but not installed by the Tool, a new mail message is created with the patch description that is sent to the local installation team for manual processing (see below).

The Tool builds and maintains a database of patches it has processed including those not automatically loaded and/or installed. It also provides tools to list the contents of the patch database.

Loaded not Installed MailMan message

Subj: MAG\*3.0\*293 SEQ#228 loaded. Needs to be installed. \[#72976587\]

09/22/22@12:17 600 lines

From: CHAVE,WARREN T In 'WASTE' basket. Page 1

--------------------------------------------------------------------------

========================================================================

Run Date: SEP 20, 2022 Designation: MAG\*3\*293

Package : MAG - IMAGING Priority: Mandatory

Version : 3 SEQ \#228 Status: Released

Compliance Date: OCT 21, 2022

========================================================================

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Automated VistA Patching tool runs on a standard VistA system. It requires no additional software or hardware.

### Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All data flows supported by the Automated VistA Patching tool are internal to VistA.

### User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Automated VistA Patching Tool needs users to employ options to produce the four (4) different reports: 1) count by status, 2) detail patch, 3) patch install and 4) summary patch.

### Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Automated VistA Patching tool does not impact routine VistA operations.

### Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Automated VistA Patching tool comes in two (2) parts: 1) automatic loader/installer and 2) reports. The automatic loader/installer is invoked whenever a patch message is received by the test system’s designated MailMan group and the EHM AUTOMATED PATCH LOAD server option is executed. The operation of the automatic loader/installer is described above in section 2.2.

The reports can be found on the tool’s main menu – option EHM AUTOMATED PATCHING MENU.

EHM AUTOMATED PATCHING MENU

Select Automated Patching Options \<TEST ACCOUNT\> Option: ?

COUNT - Print Count by Status Report

DETL - Print Detail Report

INSTALL - Print Install Report

SUMRY - Print Summary Report

#### Count by Status Report

Printing a count report of patches is done by selecting “COUNT - Print Count by Status Report” (option EHM_PATCH STATUS COUNT). The user is prompted to select a date range and whether to include or exclude informational patches from the report. Sample report output is also shown below.

Count by Status Report User Interaction

Select Automated Patching Options \<TEST ACCOUNT\> Option: COUNT - Print Count by Status Report

Start Date of Range: (SEP 10, 2021-AUG 02, 2023): T-7 (JUL 26, 2023)

End Date of Range: (JUL 26, 2023-AUG 02, 2023): T (AUG 02, 2023)

Include informational patches? YES//

Count by Status Report (Informational Patches included)

AUTOMATED PATCH INSTALLATION SYSTEM

Counts by Status (Feb 14, 2022-Mar 16, 2022)

Status Count Percentage

----------------------------------- -------- ----------

CANNOT BE AUTO-LOADED/INSTALLED 31 56%

FAILED AUTO-LOAD 1 2%

INSTALLED 11 20%

LOADED, CANNOT BE AUTO-INSTALLED 12 22%

----------------------------------- --------

TOTAL 55

Count by Status Report (Informational Patches excluded)

AUTOMATED PATCH INSTALLATION SYSTEM

Counts by Status (Feb 14, 2022-Mar 16, 2022)

Informational patches excluded

Status Count Percentage

----------------------------------- -------- ----------

CANNOT BE AUTO-LOADED/INSTALLED 10 29%

FAILED AUTO-LOAD 1 3%

INSTALLED 11 32%

LOADED, CANNOT BE AUTO-INSTALLED 12 35%

----------------------------------- --------

TOTAL 34

#### Detail Report

The user selects “DETL - Print Detail Report” (option EHM_PATCH DETAIL REPORT). The user is prompted to enter a date range and then to select status and package filters. The filters allow the user to select specific patch installation status values and/or VistA software packages to include in the report. To include all status values, enter “A” or press RETURN. To include only specific status values, enter “S”. The list of status values is shown below.

0 PENDING LOAD

1 LOADED

2 INSTALLED

3 CANNOT BE AUTO-LOADED/INSTALLED

4 FAILED AUTO-LOAD

5 FAILED AUTO-INSTALL

6 LOADED, CANNOT BE AUTO-INSTALLED

Select one or more of these values to include in the report. If a value is selected that, in retrospect, should not be included in the report, enter it again and it will be de-selected. Selecting packages to include in the report works the same as for status values. Examples of packages are “LR” for Lab, “RA” for Radiology and “MAG” for Imaging. The complete list of packages is too long to include in this user guide.

The user may also include details of the actions taken by the tool. The detail report option then prompts the user to include or exclude informational patches.

Detail Report Interaction

Select Automated Patching Options \<TEST ACCOUNT\> Option: DETL - Print Detail Report

Start Date of Range: (SEP 10, 2021-AUG 02, 2023): T-7 (JUL 26, 2023)

End Date of Range: (JUL 26, 2023-AUG 02, 2023): T (AUG 02, 2023)

Select one of the following:

A All

S Selected

Status: All//

Select one of the following:

A All

S Selected

Package(s): All//

Include action details? NO//

Include informational patches? YES//

Sample report output is shown below.

AUTOMATED PATCH INSTALLATION SYSTEM

Patch Detail (Sep 01, 2022-Sep 26, 2022)

Patch: MAG\*3.0\*320

Load Type: HOST FILE

Host File: MAG3_0P320.KID

Package Type: SINGLE PACKAGE

Patch Type: RELEASED

Patch Version: 227

Status: LOADED, CANNOT BE AUTO-INSTALLED

Install Completed

Date Processed: SEP 06, 2022@14:43:37

Reason not loaded: Patch has post-install routine.

Loaded: SEP 06, 2022@14:43:37

Install Error:

Action Date/Time Performed by

------ --------- ------------

Added to EHM Patch file 9/6/22@14:43:37 CHAVE,W

Loaded 9/6/22@14:43:37 CHAVE,W

Backed up 9/6/22@14:43:37 CHAVE,W

Ineligible for install. Forwarded. 9/6/22@14:43:37 CHAVE,W

--------------------------------------------------------------------------

Continue? YES//

#### Install Report

The user selects “INSTALL - Print Install Report” (option EHM_PATCH INSTALL REPORT). The user is prompted to enter a date range, a sort order (by date or patch number) and then an output format (formatted or comma-delimited output) as shown here.

Select Automated Patching Options \<TEST ACCOUNT\> Option: install - Print Install Report

Start Date of Range: (SEP 10, 2021-AUG 03, 2023): t-7 (JUL 27, 2023)

End Date of Range: (JUL 27, 2023-AUG 03, 2023): t (AUG 03, 2023)

Select one of the following:

D Date Processed

P Patch Number

Sort Order: Date Processed//

Select one of the following:

F Formatted Report

C Comma-Delimited

Output Format: Formatted Report//

A sample of the formatted report is shown below.

AUTOMATED PATCH INSTALLATION SYSTEM

Patch Install Report (Jul 27, 2023-Jul 31, 2023)

Date Installed Patch Seq \# Type Installation Method

-------------- ------ ----- ------------- -------------------

7/27/23 MMRS\*1.0\*10 10 PACKMAN AUTOMATED TOOL

7/27/23 GMRC\*3.0\*185 3 PACKMAN MANUALLY

7/27/23 SD\*5.3\*846 703 PACKMAN MANUALLY

7/27/23 MAG\*3.0\*360 244 INFORMATIONAL AUTOMATED TOOL

7/27/23 WEBP\*1.0\*30 30 INFORMATIONAL AUTOMATED TOOL

7/31/23 JLV\*3.0\*22 22 INFORMATIONAL AUTOMATED TOOL

7/31/23 MAG\*3.0\*319 243 HOST FILE MANUALLY

MAG3_0P319.KID

7/31/23 MAG\*3.0\*319 243 HOST FILE MANUALLY

MAG3_0P319.KID

Comma-delimited output is shown here.

"7/27/23","MMRS\*1.0\*10","10","PACKMAN","AUTOMATED TOOL"

"7/27/23","GMRC\*3.0\*185","3","PACKMAN","MANUALLY"

"7/27/23","SD\*5.3\*846","703","PACKMAN","MANUALLY"

"7/27/23","MAG\*3.0\*360","244","INFORMATIONAL","AUTOMATED TOOL"

"7/27/23","WEBP\*1.0\*30","30","INFORMATIONAL","AUTOMATED TOOL"

"7/31/23","JLV\*3.0\*22","22","INFORMATIONAL","AUTOMATED TOOL"

"7/31/23","MAG\*3.0\*319","243","MAG3_0P319.KID","MANUALLY"

"7/31/23","MAG\*3.0\*319","243","MAG3_0P319.KID","MANUALLY"

"7/31/23","MAG\*3.0\*319","243","MAG3_0P319.KID","MANUALLY"

"7/31/23","IB\*2.0\*747","696","PACKMAN","AUTOMATED TOOL"

"7/31/23","PSO\*7.0\*677","599","PACKMAN","AUTOMATED TOOL"

"7/31/23","DG\*5.3\*1101","962","PACKMAN","AUTOMATED TOOL"

#### Summary Report

The user selects “DETL - Print Detail Report” (option EHM_PATCH DETAIL REPORT). The user is prompted to enter a date range and then to select status and package filters. The user may also include details of the actions taken by the tool. The detail report option then prompts the user to include or exclude informational patches. The interaction is the same as for the detail report.

Select Automated Patching Options \<TEST ACCOUNT\> Option: SUMRY - Print Summary Report

Start Date of Range: (SEP 10, 2021-SEP 26, 2022): 9/1 (SEP 01, 2022)

End Date of Range: (SEP 01, 2022-SEP 26, 2022): 9/26 (SEP 26, 2022)

Select one of the following:

D Date Processed

P Patch Number

Sort Order: Date Processed//

Select one of the following:

A All

S Selected

Status: All//

Select one of the following:

A All

S Selected

Package(s): All//

DEVICE: HOME// HOME(CRT)

AUTOMATED PATCH INSTALLATION SYSTEM

Patch Summary (Sep 01, 2022-Sep 26, 2022)

Patch Version Status Processed Load Type

----------- ------ ------------------------------- --------- -----------

MAG\*3.0\*320 227 LOADED, CANNOT BE AUTO-INSTALLED 9/6/22 HOST FILE

Install Completed

LR\*5.2\*559 458 LOADED, CANNOT BE AUTO-INSTALLED 9/6/22 PACKMAN

Install Completed

IB\*2.0\*718 669 LOADED, CANNOT BE AUTO-INSTALLED 9/9/22 PACKMAN

Install Completed

RA\*5.0\*192 173 INSTALLED 9/9/22 PACKMAN

MHV\*1.0\*79 71 CANNOT BE AUTO-LOADED/INSTALLED 9/12/22 INFORMATIONAL

DG\*5.3\*1081 943 CANNOT BE AUTO-LOADED/INSTALLED 9/12/22 PACKMAN

Install Completed

IVM\*2.0\*207 173 CANNOT BE AUTO-LOADED/INSTALLED 9/12/22 INFORMATIONAL

SD\*5.3\*823 674 LOADED, CANNOT BE AUTO-INSTALLED 9/12/22 PACKMAN

Install Completed

PRC\*5.1\*227 199 INSTALLED 9/14/22 PACKMAN

LEX\*2.0\*141 132 CANNOT BE AUTO-LOADED/INSTALLED 9/15/22 PACKMAN

Install Completed

ICPT\*6.0\*107 105 CANNOT BE AUTO-LOADED/INSTALLED 9/15/22 INFORMATIONAL

#### EHM Automatic Patching Tool Parameter (#1608)

File \#1608 stores control data used by the tool. A record is created in the file by a post-install routine when the patch is installed. If later changes are required to the record, they can be made using FileMan.

Version 5 of the Tool added a feature that moves backup patches out of the IN mailbox and into the BACKUP mailbox of the installation team member. To enable this feature, use FileMan and edit the entry in file \#1608 (there is only one). Set the BACKUP PATCH MESSAGE ACTION field to be MOVE TO 'BACKUP'. Only team members who have a BACKUP mailbox will be affected.

#### Mail Groups

#### EHM AUTOMATED PATCHING

The EHM AUTOMATED PATCHING mail group contains the list of recipients of patches that cannot be automatically loaded and installed by the tool as well as all backup patch mail messages generated by the tool. These recipients must be able to manually load and install VistA patches. Members of this mail group should be added post-install of the patch.

#### EHMPATCHING

The EHMPATCHING mail group has a single member, the server option (EHM AUTOMATED PATCH LOAD) that executes the Automated VistA Patching Tool. This mail group should not be edited.

## EHM\*1\*8 – EHRM-IO Clinical Cutover Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch EHM\*1\*8 loads tools that are used during cutover form VistA to Cerner. The patch is a component of the EHM Package.

A representative of the Electronics Health Record Modernization (EHRM) team for outpatient pharmacy prescription (RX) data prepares a spreadsheet containing a table of prescription internal entry numbers (RX IEN's) that have been successfully migrated to Millennium. These RX IEN's are then copy/pasted into a new option - Discontinue RX for EHRM Data Migration \[EHM CANCEL RX\]. This option performs the automatic discontinue/cancel action for each prescription and files a standardized comment text. This ensures that only one active instance of a prescription exists in the two systems.

New print and sort templates have been created and added to new menu options to perform the needed reports to verify all prescriptions have been discontinued.

A new security key named Outpatient Pharmacy RX Cancel \[EHM RX CANCEL\] has been created to access the Pharmacy Discontinue RX \[EHM PHARMACY DISCONTINUE RX\] main menu option. All the new options will be under the \[EHM PHARMCY DISCONTINUE RX\] menu option. The EHM PHARMACY DISCONTINUE RX menu option can be found under the EHM MAIN MENU \[EHM MAIN MENU\] option, locked by the EHM MGR security key.

The following tools are provided by EHM\*1\*9 to assist during cutover. They are available from the EHM MAIN MENU that is created by EHM\*1\*14.

Select OPTION NAME: EHM MAIN MENU EHM Main Menu

HITT EHM TRANSITION MENU ...

RX Pharmacy Discontinue RX ...

Sub-menus created by this patch are secured by keys as listed in Table 5.

| Menu                      | Key       |
|-------------------------------|---------------|
| Outpatient Pharmacy RX Cancel | EHM RX CANCEL |

The Pharmacy Discontinue menu and its options are show below.

Select Pharmacy Discontinue RX \<TEST ACCOUNT\> Option: ?

DIS Discontinue RX for EHRM Data Migration

ACT QA check for Auto-D/C - Active

SUS QA check for Auto-D/C - Suspended

HOLD QA check for Auto-D/C - Hold

CMOP CMOP Temporary Address

IV1 IV Future Clinic Orders

IV2 IV Future Clinic Orders Filtered

UD1 Unit Dose Future Clinic Orders

UD2 Unit Dose Future Clinic Orders Filtered

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHRM-IO CLINICAL CUTOVER TOOLS patch is loaded via EHM\*1\*8 and run through the EHM MAIN MENU system.

### Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All data flows supported by the EHRM-IO CLINICAL CUTOVER TOOLS patch are internal to VistA.

### User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users who need to access the EHM MAIN MENU option will need to be assigned the EHM MGR security key.

Users who need to access the Outpatient Pharmacy RX Cancel \[EHM RX CANCEL\] menu will need to be assigned the EHM RX CANCEL security key. This key will allow the user to enter prescription internal entry numbers to be discontinued from the menu option.

### Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHRM-IO CLINICAL CUTOVER TOOLS software does not impact routine VistA operations.

### Using the Software / Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Patch EHM\*1\*8 creates tools needed at cutover from VistA to Cerner. This patch will NOT be released nationally. It is only run at cutover VAMC sites being converted to Cerner.

#### Pharmacy Discontinue RX \[EHM CANCEL RX\]

Select EHM Main Menu \<TEST ACCOUNT\> Option: RX Pharmacy Discontinue RX Menu

> DIS Discontinue RX for EHRM Data Migration

> ACT QA check for Auto-D/C - Active

> SUS QA check for Auto-D/C - Suspended

> HOLD QA check for Auto-D/C - Hold

> CMOP CMOP Temporary Address

> IV1 IV Future Clinic Orders

> IV2 IV Future Clinic Orders Filtered

> UD1 Unit Dose Future Clinic Orders

> UD2 Unit Dose Future Clinic Orders Filtered

Pharmacy Discontinue RX is part of the cutover process. The menu and its options are shown in Figure 18. It is locked by the EHM CANCEL RX security key.

1.  Discontinue RX for EHRM Data Migration allows a user to paste in a series of prescription internal entry numbers (RX IEN’s) to call an application programming interface (API) developed for the purpose of discontinuing the prescriptions (RX’s) on the legacy VistA system after successful migration to EHRM/Cerner Millenium. The routine called from this option is CAN^EHMPSRXDC.
2.  QA check for Auto-D/C – Active is used to perform a quality assurance check for lingering prescriptions with a status of Active after Cerner data migration. This option contains a print template called EHM QA CHECK.
3.  QA check for Auto-D/C – Suspended is used to perform a quality assurance check for lingering prescriptions with a status of Suspended after Cerner data migration. This option contains a print template called EHM QA CHECK.
4.  QA check for Auto-D/C – Hold is used to perform a quality assurance check for lingering prescriptions with a status of Hold after Cerner data migration. This option contains a print template called EHM QA CHECK.
5.  CMOP Temporary Address tracks the temporary addresses of CMOP patient. This will be run pre go-live and repeatedly until go-live to see the numbers track downward towards zero.
6.  IV Future Clinic Orders includes both recurring orders that started before go-live date and orders with future start dates.

> Used at T-30 (maybe T-60) pre-go-live. Needs patient accounts to exist in Cerner and then the first place in which this one is used is to log prior Auth adjudication approvals before providers do their part of order back-entry into EHRM.

> This option contains a print templated named EHM IV FUTURE CLINIC ORDERS and a sort template named EHM IV FUTURE ACTIVE CLINIC.

7.  IV Future Clinic Orders Filtered includes both recurring orders that started before go-live date and orders with future start dates.

> Used at T-30 (maybe T-60) pre-go-live. Needs patient accounts to exist in Cerner and then the first place in which this one is used is to log prior Auth adjudication approvals before providers do their part of order back-entry into EHRM.

> This option contains a print templated named EHM IV FUTURE CLINIC FILTERED and a sort templated named EHM IV FUTURE ACTIVE FILTERED.

8.  Unit Dose Future Clinic Orders includes both recurring orders that started before go-live date and orders with future start dates.

> Used at T-30 (maybe T-60) pre-go-live. Needs patient accounts to exist in Cerner and then the first place in which this one is used is to log prior Auth adjudication approvals before providers do their part of order back-entry into EHRM.

> This option contains a print templated named EHM UD FUTURE ACTIVE CLINICS and a sort templated named EHM UD FUTURE ACTIVE CLINIC.

9.  Unit Dose Future Clinic Orders Filtered includes both recurring orders that started before go-live date and orders with future start dates.

> Used at T-30 (maybe T-60) pre-go-live. Needs patient accounts to exist in Cerner and then the first place in which this one is used is to log prior Auth adjudication approvals before providers do their part of order back-entry into EHRM.

> This option contains a print templated named EHM UD FUTURE ACTIVE FILTERED and a sort templated named EHM UD FUTURE ACTIVE FILTERED.

## EHM\*1\*9 – EHRM-IO Kernel Cutover Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch EHM\*1\*9 loads tools that are used during cutover from VistA to Cerner. The patch is a component of the EHM Package.

Version 1 of the patch includes options used to manage user access and security keys. The user access options allow the transition team to restrict user access to VistA at cutover. They are used in conjunction with WebVRAM. The delete key option removes a key from all entries in the New Person file (#200).

The following tools are provided by EHM\*1\*9 to assist during cutover. They are available from the EHM MAIN MENU.

Select OPTION NAME: EHM MAIN MENU EHM Main Menu

HITT EHM TRANSITION MENU ...

KEY Key Deletion Menu ...

USER User Access Menu ...

Menus created by this patch are secured by keys as listed in Table 5.

| Menu                                  | Key         |
|-------------------------------------------|-----------------|
| Key Deletion Menu \[EHM KEY MENU\]        | EHM KEY DELETE  |
| User Access Menu \[EHM USER ACCESS MENU\] | EHM USER ACCESS |

The user access menu has five (5) options:

1.  List users to be terminated \[EHM USER TERMINATION LIST\]
2.  Remove single user from termination list\[EHM REMOVE SINGLE USER\]
3.  Revert single user's termination \[EHM REVERT SINGLE USER\]
4.  Set user termination date \[EHM SET USER TERMINATION DATE\]

On the night of cutover, user access to VistA is terminated for existing users using the EHM SET USER TERMINATION DATE option. The users affected are those that have been flagged previously using Web VRAM.

Prior to terminating user access, a single user can be removed from the termination list using the EHM REMOVE SINGLE USER option. After access has been terminated, a single user’s termination can be reversed using the EHM REVERT SINGLE USER option.

The list option exists to prepare for go-live. The list shows the users that will be terminated by the set user termination date option.

The key management menu consists of two options: 1) delete key and 2) restore key. With the first option, the user selects a key to be deleted from all entries in the New Person file (#200). The code that deletes the key builds a list of the records edited so that the restore option can be used to reverse the deletion.

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHRM-IO CUTOVER TOOLS patch is loaded via EHM\*1\*9 and run through the EHM MAIN MENU system.

### Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All data flows supported by the EHRM-IO CUTOVER TOOLS patch are internal to VistA.

### User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users who need to access the EHM MAIN MENU option will need to be assigned the EHM MGR security key.

Users who need to access the Key Deletion menu \[EHM KEY MENU\] will need to be assigned the EHM KEY DELETE security key.

Users who need to access the User Access menu \[EHM USER ACCESS MENU\] will need to be assigned the EHM USER ACCESS security key.

### Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHRM-IO TOOLS software does not impact routine VistA operations.

### Using the Software / Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Patch EHM\*1\*9 creates tools needed at cutover from VistA to Cerner. This patch will NOT be released nationally. It is only run at cutover VAMC sites being converted to Cerner.

#### Key Deletion Menu \[EHM KEY MENU\]

Security access key deletion from system users is part of the cutover process. It is locked by the EHM KEY DELETE security key.

Select EHM Main Menu \<TEST ACCOUNT\> Option: KEY Key Deletion Menu

Delete Security Key from All Users

Restore Security Key to Users

10. Delete Security Key from All Users is used to delete a key from all entries in the New Person file (#200).

As shown below, the user selects the security key to be deleted and confirms the action. Dots represent the entries in the New Person file (#200) from which the key has been deleted.

Select Key Deletion Menu \<TEST ACCOUNT\> Option: DElete Security Key from All Users

Delete a key from all users.

Select SECURITY KEY NAME: EHM-TEST

Delete the "EHM-TEST"security key from all users?? NO// YES..

11. Restore Security Key to Users is used to restore a deleted key to entries in the New Person file (#200)

> As shown below, the user selects the key to be restored and confirms the action. Dots represent the entries in the New Person file (#200) to which the key has been restored.

Select Key Deletion Menu \<TEST ACCOUNT\> Option: restore Security Key to Users Restore deleted key.

Select SECURITY KEY NAME: EHM-TEST

Restore the "EHM-TEST"security key from all users?? NO// YES..

Restore complete

#### User Access Menu \[EHM USER ACCESS MENU\]

User access to VistA for local and remote users is terminated as part of the cutover process.

Select User Access Menu \<TEST ACCOUNT\> Option: USER User Access Menu

List users to be terminated

Remove user from termination list

Revert single user's termination

Set user termination date

Web VRAM is employed to identify the group of users in the New Person file (#200) on the target system whose access is to be terminated. The menu and its options are show in Error! Reference source not found.. It is locked by the EHM USER ACCESS security key.

1.  List user to be terminated produces a report of users who will be terminated on a specific future date. It can be used to confirm the membership of the group to be terminated at cutover.

\*\*\* Cerner Go Live - users to be terminated list. \*\*\*

Expected termination date: (JUN 06, 2022-DEC 31, 2699): 8/31/22 (AUG 31, 2022)

Users identified: 1

DEVICE: HOME// HOME (CRT)

User termination list for expected termination date: Aug 31, 2022

USER LAST EDIT DATE

------------------------------ --------------

EHMPERSON,JOHN A JUN 02, 2022

2.  Remove user from termination list sets an individual user’s termination date 90 days in the future so the New Person file record will not be affected by the group set or revert options.

The user is prompted to select an entry in the New Person file and then to confirm that the person selected should be removed. The person’s termination date is set 90 days in the future and, if present in the group identified by Web VRAM, removed from that list.

Select User Access Menu \<TEST ACCOUNT\> Option: REMove user from termination list

Select NEW PERSON NAME: EHMP,KATH

1 EHMPERSON1,KATHLEEN S KSE 192 OI&T STAFF

2 EHMPERSON9,GREGG W GWE

CHOOSE 1-2: 1 EHMPERSON1,KATHLEEN S KSE 192 OI&T STAFF

Verify? NO// YES... removed from termination list.

3.  Revert single user’s termination removes a single person from the group and sets a user-entered termination date in the New Person file.

> The user is prompted for an entry in the New Person file. The person must exist in the group whose termination dates were set using the Set User Termination Date option. Once the person is identified, the user is prompted for a date in the future to record as the new termination date.

Select User Access Menu \<TEST ACCOUNT\> Option: Revert single user's termination

Select NEW PERSON NAME: EHMP,KATH EHMPERSON1,KATHLEEN S KSE 192 OI&T STAFF

Termination date: (JUN 07, 2022-DEC 31, 2699): T+10 (JUN 17, 2022)... reverted

4.  Set user termination date is used to set the termination date for the group to tomorrow.

There is no user interaction for this option. When selected, it outputs a header that says:

Cerner Go Live - setting termination dates for select users.

Upon completion, it displays the number of records that were processed:

Records processed: 0

## EHM\*1\*10 – IFC and PRF HL7 Message Storage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inter-Facility Consult (IFC) and Patient Record Flag (PRF) Health Level Seven (HL7) Message Storage functionality was created to facilitate research into issues resulting from communication between non-converted VistA sites and converted Cerner sites. The VistA HL7 system lacks capacity to store HL7 messages for longer than a few days because of the large number of messages exchanged between systems. EHM\*1\*10 addresses this restriction by separately saving a select group of HL7 messages and retaining them for a longer period of time. The only HL7 messages saved are IFC and PRF messages that are sent by Cerner to a non-converted VistA or vice versa, a very small subset of the total volume of HL7 messages.

EHM\*1\*10 is the second of four patches contained in the IFC Proxy Add/Order Resubmission 1.0 multi-build. The patch creates a VistA database (EHRM HL7 Message file (#1609)) to store IFC and PRF HL7 messages sent to or received from Cerner. It also includes options to inquire into the database of HL7 messages and to purge them.

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHM\*1\*10 is the second of four (4) patches in the IFC Proxy Add/Order Resubmission 1.0 build. The patch list is:

- DG\*5.3\*1096
- EHM\*1\*10
- GMRC\*3\*189
- DG\*5.3\*1091

### Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All data flows are internal to VistA.

### User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch does not impact routine VistA operations.

### Using the Software / Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Records are added automatically to the IFC and PRF HL7 Message Storage database every time that a non-converted VistA site receives an IFC or PRF HL7 message from Cerner and every time that a non-converted site sends an IFC or PRF HL7 message to Cerner. The messages are then available for inquiry using the option described below.

Retention of records in the database is controlled by the purge option described below. This option can be run from the EHMHL7 Menu or it can be scheduled in TaskMan to run daily during non-peak hours.

#### EHMHL7 Menu \[EHMHL7 MENU\]

Users of the IFC and PRF HL7 Message Storage system must be given access to the EHMHL7 Menu option.

Select EHRM HL7 Message Menu \<TEST ACCOUNT\> Option: ?

Message Inquiry

Purge messages

Use the Message Inquiry option to access HL7 messages in the IFC and PRF HL7 Message Storage database. FileMan inquiry, print and search are also available to access the HL7 data repository. Six (6) different data elements can be used to identify messages although all are not available for both message types. An IFC HL7 message can be found using the following date elements:

1)  Message ID
2)  VistA Consult Number
3)  Cerner Order Number
4)  Patient’s Name
5)  Date

A PRF HL7 message can be found using the following data elements:

1)  Message ID
2)  Patient’s Name
3)  ICN
4)  Date

Examples of user interaction for the inquiry modes are shown in the figures below. Note that inquiry by patient name does not support partial last/partial first name lookup.

Message Inquiry

Select EHRM HL7 Message Menu \<TEST ACCOUNT\> Option: Message Inquiry

Select one of the following:

M Message ID

V VistA Consult Number

C Cerner Order Number

P Patent's Name

I ICN

D Date

Inquire by:

Message Inquiry by Message ID

Select EHRM HL7 Message Menu \<TEST ACCOUNT\> Option: Message Inquiry

Select one of the following:

M Message ID

V VistA Consult Number

C Cerner Order Number

P Patent's Name

I ICN

D Date

Inquire by: Message ID

Message ID: Q974257807T1137452535 JAN 11, 2023@13:01:39

----------------------------------------------------------------------

DATE/TIME POSTED: JAN 11, 2023@13:01:39

TYPE: Inter-Facility Consult MESSAGE ID: Q974257807T1137452535

VISTA CONSULT NUMBER: 6916466 CERNER ORDER NUMBER: 2726926829

PATIENT'S NAME: PROSTEST,EHR SENDER: CERNER

RECEIVER: 663

HL7 MESSAGE:

MSH\|^~\\\|GMRC IF CONSULT\|^vac10apphsh905.va.gov^DNS\|GMRC IF CONSULT\|663^^DNS\|20220624194132+0000\|CRNR\|ORM^O01^ORM_O01\|Q974257807T1137452535\|T\|2.3\|\|\|AA

PID\|1\|1013570973V041977\|1013570973V041977^^^ICN^VETID~2110106796^^^EDIPI^EDIPI\|\|PROSTEST^EHR\|\|19760902\|M\|\|\|\|\|\|\|\|\|\|18100359\|678235672

ORC\|DC\|2726926829^663^GMRCIFR\|6916466^663^GMRCIFR\|\|DC\|\|^^^20220624123900-0700^^R\|\|20220624124119-0700\|^^^\|\|^^^\|\|\|20220624124132-0700\|\|663

OBR\|1\|2726926829^663^GMRCIFR\|6916466^663^GMRCIFR\|663^PROSTHETICS IFC^663VA1235\|\|202206241939\|\|\|\|\|\|\|\|\|\|z12363^PCP9^VA-Physician

NTE\|1\|L\|Order has been Discontinued in Cerner.

NTE\|2\|L\|PN_6.24_Issued in Clinic

OBX\|5\|CE\|^TIME ZONE^VA4.4\|1\|PDT

Message Inquiry by ICN

Select EHRM HL7 Message Menu \<TEST ACCOUNT\> Option: Message Inquiry

Select one of the following:

M Message ID

V VistA Consult Number

C Cerner Order Number

P Patent's Name

I ICN

D Date

Inquire by: ICN

ICN: 1013717804V969486

1 1013717804V969486 DEC 15, 2022@16:13:47

2 1013717804V969486 JAN 11, 2023@13:05:11

CHOOSE 1-2: 2 JAN 11, 2023@13:05:11

------------------------------------------------------------------------

DATE/TIME POSTED: JAN 11, 2023@13:05:11

TYPE: Patient Record Flag

MESSAGE ID: Q975084458T1138387680X1522-BH

PATIENT'S NAME: EAGLES,PHILLY ICN: 1013717804V969486

SENDER: 200CRNR RECEIVER: 668

HL7 MESSAGE:

MSH^~\|\\^PRF-SEND^200CRNR^PRF-RECV^668^20220923074232-0700^^ORU~R01^Q975084458T1138387680X1522-BH^T^2.3^^^NE^AL^USA

PID^1^558222207^1013717804V969486~V733194\~~USVHA&&L~NI\|2113798494\~\~~USDOD&&L~NI^^EAGLES~PHILLY^^19710101^M^^^^^^^^^^^558222207^

OBR^2^^^1~HIGH RISK FOR SUICIDE~VA085^^^20220923074232-0700^^^^^^^^^^^^^668^668

OBX^1^ST^S~Status~L^^NEW ASSIGNMENT^^^^^^F^^^20220923074232-0700

OBX^2^TX^N~Narrative~L^1^Testing with John 9-23-2022.^^^^^^F^^^20220923074232-0700

#### Purge Messages \[EHMHL7 PURGE\]

The Purge Messages option deletes records from the EHRM HL7 Messages file (#1609) when their DATE/TIME POSTED field (#.01) is older than the retention period in the EHRM HL7 Message Retention file (#1609.1) for the record’s type. There is no user interaction for this option. It is intended to be set up and run in TaskMan.

## EHM\*1\*14 – HITT Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch EHM\*1\*14 loads tools that are used during cutover from VistA to Cerner. The patch is a component of the EHM Package.

Version 1 of the patch includes an extensive set of menus and options for the Health Informatics Transition Team (HITT). These menus and options are composed of national standard options instead of locally modified versions of the same options.

Menu generation code clones entries in the Option file (#19) to create a set of menus and options (HITT Transition Menu). Option cloning is executed against a copy of the gold standard PATVEE environment to ensure that no local modifications to options are included.

EHM\*1\*14 creates the EHM Main Menu \[EHM MAIN MENU\] and assigns EHM TRANSITION MENU \[EHM-00001\] to it. EHM MAIN MENU is secured by the EHM MGR security key.

Select OPTION NAME: EHM MAIN MENU EHM Main Menu

HITT EHM TRANSITION MENU ...

Subordinate menus are secured by other keys as listed in Table 6.

| Menu                          | Key       |
|-----------------------------------|---------------|
| EHM MAIN MENU                     | EHM MGR       |
| EHM Transition Menu \[EHM-00001\] | EHM HITT MENU |

The HITT Transition menu contains all the menu options and their submenus needed by the VistA transition team to perform their duties for upcoming converted sites. This can be run 180 days pre-cutover, thus the national gold-menu options will be cloned as EHM Menu options and attached to the HITT Transition Menu. This will ensure no locally modified menus will be overlayed.

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHM HITT MENU patch is loaded via EHM\*1\*14 and run through the EHM MAIN MENU system.

### Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All data flows supported by the EHM HITT MENU patch are internal to VistA.

### User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users who need to access the EHM MAIN MENU option will need to be assigned the EHM MGR security key.

Users who need to access the EHM Transition menu \[EHM-00001\] will need to be assigned the EHM HITT MENU security key.

### Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHM HITT MENU software does not impact routine VistA operations.

### Using the Software / Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Patch EHM\*1\*14 creates tools needed for conversion from VistA to Millennium. This patch will be released nationally.

Select EHM Main Menu \<TEST ACCOUNT\> Option: HITT EHM TRANSITION MENU

ALERTS ...

CONSULTS ...

CPRS ...

CUTOVER ...

FILEMAN ...

GROUP ...

MENU ...

PACKAGES ...

REMIND ...

TIU ...

USER ...

#### EHM Transition Menu \[EHM-00001\]

The EHM Transition Menu is comprised of cloned versions of standard VistA menu options. Each option is renamed to be part of the EHM namespace during the cloning process but retains its original functionality. Names are assigned sequentially and prefixed with “EHM-“, e.g., EHM-00001, EHM-00002. Security keys associated with the original option are removed during cloning. The menu is locked by the EHM HITT MENU security key.

letion, it displays the number of records that were processed:

## GMRC\*3\*192 – EHRM-IO Cutover Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch GMRC\*3\*192 loads tools that are used during cutover from VistA to Cerner. The patch is a component of the Consult/Request Tracking (GMRC) Package.

Version 1 of the patch consists of an option to update consult status in bulk using grouper services as well as options to report on the status changes. It also includes options to list services by grouper and unresolved consults. The consults updated by this patch are those that have been migrated to Cerner and need to be marked “discontinued” in VistA to prevent confusion and duplication post go-live.

> **NOTE:** The bulk consult status change process has been modified to suppress HL7 message generation from a converted site so that production databases (Inter-Facility Consult (IFC) sites and third-party community care sites) do not improperly receive discontinue notifications. The affected consults in the VistA database have already been converted to the Cerner database.

The following tools are provided by GMRC\*3\*192 to assist after cutover. They are available from the Consult status update \[GMRCSTSM\] menu shown below.

Select OPTION NAME: GMRCSTSM Consult status update - Converted sites only

Group update of consults

Consult update report

Consult update file output

Service list

Unresolved Consults

The Group update of consults \[GMRCSTSC\] option changes the status of Active, Pending and Scheduled consults to Discontinued in VistA for consults that were already migrated to Cerner.

The Consult update report \[GMRCSTSR\] option produces a report of consults updated by the GMRCSTSC option.

The Consult update file output \[GMRCSTSR1\] option produces a set of comma-delimited records for the consults updated by the GMRCSTSC option.

The Service list \[GMRCSTSR2\] option produces a report showing the services that have consults in Active, Pending or Scheduled status. The report is sorted alphabetically by grouper. Output is available as a formatted list or as a comma-delimited list.

The Unresolved Consults \[GMRCSTSQ\] option produces a report of consults that are NOT discontinued, complete, expired or lapsed for four (4) groupings: 1) Clinical Procedure, 2) Community Care, 3) IFC and 4) Prosthetics consults. The report is sorted in consult number order within the four groupings. Output is available as a formatted list or as a comma-delimited list.

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHRM-IO CONSULT CUTOVER TOOLS patch is loaded via GMRC\*3\*192 and run through the GMRCSTSM menu.

### Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All data flows supported by the EHRM-IO CUTOVER TOOLS patch are internal to VistA.

### User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users who need to access the GMRCSTSM menu will need to have it assigned to their secondary options.

### Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHRM-IO CONSULT CUTOVER TOOLS software does not impact routine VistA operations.

### Using the Software / Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The patch consists of an option to update consult status in bulk using grouper services, options to report on the status changes, a list of services that have consults eligible for bulk update and a report of unresolved consults. The consults updated by this patch are those that have been migrated to Cerner and need to be marked “discontinued” in VistA to prevent confusion and duplication post go-live.

This patch will NOT be released nationally. It is run only after cutover at VAMC sites converted to Cerner.

#### Options

#### Consult Status Update \[GMRCSTSM\]

This option is the main menu used to access the Consult Status Update options.

#### Group Update of Consults \[GMRCSTSC\]

#### This option changes consult status from Active, Pending or Scheduled to Discontinued for all consults in scope of a grouper service. User interaction is shown below.

Select Consult status update - Converted sites only \<TEST ACCOUNT\> Option: Group update of consults - converted sites only

Select REQUEST SERVICES SERVICE NAME: ALL

1 ALL SERVICES GROUPER ONLY

2 ALLERGY GROUPER GROUPER ONLY

CHOOSE 1-2: 1 ALL SERVICES GROUPER ONLY

The first order in Consults has an entry date of DEC 14,2004

Update Status Start Date: DEC 14,2004// (DEC 14, 2004)

Update Status Stop Date: T (NOV 22, 2022)

Records will be updated for:

------------------------------------------------------------------------------

Service: ALL SERVICES

Beginning: Dec 14, 2004

Ending: Nov 22, 2022

Update: Active, Pending, and Scheduled Consults

To: DISCONTINUED

Update Comment:

Consult administratively discontinued to update EHR post Cerner go live.

Verified this consult order migrated to Cerner. Review patient record in

Cerner for clinically relevant information pertaining to this consult.

------------------------------------------------------------------------------

Consult/request discontinuation report display will not be available using

this option. That information runs in the background. You must use Consult

update report or Consult update file output report options to generate a

report in either List format or comma-delimited format.

Is this correct? NO//YES

#### Consult update report \[GMRCSTSR\]

This option produces a report of consults whose status was changed by the GMRCSTSC option. User interaction and sample report are shown below.

Select OPTION NAME: GMRCSTSM Consult status update - Converted sites only

Group update of consults - converted sites only

Consult update report - converted sites only

Consult update file output - converted sites only

Service list - converted sites only

Select Consult status update - Converted sites only \<TEST ACCOUNT\> Option: C

1 Consult update file output - converted sites only

2 Consult update report - converted sites only

CHOOSE 1-2: 2 Consult update report - converted sites only

The first order in Consults has an entry date of AUG 21,1996

Report Start Date: AUG 21,1996// 4/1/2019 (APR 01, 2019)

Report Stop Date: 4/13/2019 (APR 13, 2019)

Select REQUEST SERVICES SERVICE NAME: WTC TEST GROUPER ONLY

DEVICE: HOME// HOME (CRT)

CONSULT STATUS CHANGE REPORT

SERVICE: ENDO COLONOSCOPY OUTPT

Apr 01, 2019 - Apr 13, 2019

Consult Request

Number Date/Time Patient/SSN Status Change

---------- ---------------- ------------------------------ -------------

1301901 4/1/2019@14:57 XXXXX,JACKSON JAMES a to dc

\<SSN\> 9/21/2022@10:00

1302682 4/3/2019@08:55 XXXXXXXX,STACEY B a to dc

\<SSN\> 9/21/2022@10:00

Continue? YES//YES

CONSULT STATUS CHANGE REPORT

SERVICE: ORTHOPEDIC OUTPT CONSULT

Apr 01, 2019 - Apr 13, 2019

Consult Request

Number Date/Time Patient/SSN Status Change

---------- ---------------- ------------------------------ -------------

1303928 4/5/2019@12:57 XXXXXX,ELTON G JR s to dc

\<SSN\> 9/21/2022@10:00

#### Consult update file output \[GMRCSTSR1\]

This option produces a set of comma-delimited records for the consults whose status was changed by the GMRCSTSC option. User interaction and sample output are shown below.

Select OPTION NAME: GMRCSTSM Consult status update - Converted sites only

Group update of consults - converted sites only

Consult update report - converted sites only

Consult update file output - converted sites only

Service list - converted sites only

Select Consult status update - Converted sites only \<TEST ACCOUNT\> Option: C

1 Consult update file output - converted sites only

2 Consult update report - converted sites only

CHOOSE 1-2: 1 Consult update file output - converted sites only

The first order in Consults has an entry date of AUG 21,1996

Report Start Date: AUG 21,1996// 4/1/2019 (APR 01, 2019)

Report Stop Date: 4/3/2019 (APR 03, 2019)

Select REQUEST SERVICES SERVICE NAME: WTC TEST GROUPER ONLY

DEVICE: HOME// 0;132;99999 HOME (CRT)

"Service Name","Consult Number","Request Date","Request Time","Patient's Name","SSN","Status Change","Last Activity Date","Last Activity Time"

"ENDO COLONOSCOPY OUTPT","1301901","4/1/2019","14:57","XXXXXX,JACKSON JAMES","\<SSN\>","a to dc","9/21/2022","10:00"

"ENDO COLONOSCOPY OUTPT","1302682","4/3/2019","08:55","XXXXXXX,STACEY B","\<SSN\>","a to dc","9/21/2022","10:00"

#### Service List \[GMRCSTSR2\]

This option lists services that have active, pending, or scheduled consults. It is sorted by grouper. User interaction and sample report are shown below.

Select OPTION NAME: GMRCSTSM Consult status update - Converted sites only

Group update of consults

Consult update report

Consult update file output

Service list

Unresolved consults

Select Consult status update - Converted sites only \<TEST ACCOUNT\> Option: Service list - converted sites only

List of services with active, pending, or scheduled consults.

Select one of the following:

L List

F File (comma-delimited list)

Output Format: List// List

DEVICE: HOME// HOME (CRT) Right Margin: 80//

Compiling list

99% of 1,397,439

GROUPER: ADDICTION/VARC GROUPER

SERVICE COUNT

--------------------------------------------------------------- --------

A ADDICTION PROGRAM OUTPT 1

PRM VARC ADDICTIONS TREATMENT OUTPT 1

W VARC ADDICTIONS TREATMENT INPT 4

W VARC ADDICTIONS TREATMENT OUTPT 12

W VARC OBOT INDUCTION OUTPT 1

W VARC OPIOID TREATMENT OUTPT 11

Y ADDICTION PROGRAM OUTPT 1

--------------------------------------------------------------- --------

TOTAL 31

#### Unresolved Consults \[GMRCSTSQ\]

This option lists consults that are NOT discontinued, complete, expired or lapsed. It reports consults that: 1) have clinical procedures, 2) involved community care, 3) are IFCs or 4) are for Prosthetics. User interaction and sample report are shown below.

Select OPTION NAME: GMRCSTSM Consult status update - Converted sites only

Group update of consults

Consult update report

Consult update file output

Service list

Unresolved consults

Select Consult status update - Converted sites only \<TEST ACCOUNT\> Option: Unresolved Consults

List of unresolved consults that are IFCs, Community Care or Clinical Procedures.

Select one of the following:

L List

F File (comma-delimited list)

Output Format: List// List

DEVICE: HOME// ;132 HOME (CRT)

Compiling list

99% of 1,397,439

UNRESOLVED CONSULTS

CLINICAL PROCEDURE

CONSULT/ LAST ACTION/ GROUPER/

REQUEST DT PATIENT NAME/SSN STATUS SERVICE

---------- ------------------------- ----------------------- ---------------------------------------------------------------

7826686 XXXXX,E (1234) ADDED COMMENT CP GI PROCEDURES FUTURE CARE

Feb 04, 2019 ACTIVE WADE PARK SERVICES

7921753 XXXXXX,E (6789) PRINTED TO CP GI PROCEDURES FUTURE CARE

Mar 28, 2019 PENDING WADE PARK SERVICES

User interaction for comma-delimited output and a sample of it are shown below.

Select OPTION NAME: GMRCSTSM Consult status update - Converted sites only

Group update of consults

Consult update report

Consult update file output

Service list

Unresolved consults

Select Consult status update - Converted sites only \<TEST ACCOUNT\> Option: Unresolved Consults

List of unresolved consults that are IFCs, Community Care or Clinical Procedures.

Select one of the following:

L List

F File (comma-delimited list)

Output Format: List// File

DEVICE: HOME// ;200 HOME (CRT)

Compiling list

99% of 1,397,439

"Type","Consult","Service Name","Status","Request Date","Patient Name","Grouper Name","Last Action"

"CLINICAL PROCEDURE","7826686","CP GI PROCEDURES FUTURE CARE","ACTIVE","Feb 04, 2019","XXXXX,E (1234)","WADE PARK SERVICES","ADDED COMMENT"

"CLINICAL PROCEDURE","7921753","CP GI PROCEDURES FUTURE CARE","PENDING","Mar 28, 2019","XXXXXX,E (9876)","WADE PARK SERVICES","PRINTED TO"

## EHM\*1\*13 – CONVERTED APPOINTMENT MAINTENANCE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch EHM\*1\*13 loads tools that are used to clean up appointments in converted systems. Appointments and encounters at VistA sites post-conversion to Cerner should not be left

in an active state. This patch provides tools to manage several different classes of appointments, appointment requests and clinics. They are:

1.  Appointments converted to Cerner at go-live
2.  Appointments added to a converted VistA after go-live.
3.  Active appointments post-conversion
4.  All appointments
5.  Appointment requests
6.  Appointments with ACTION REQUIRED encounters
7.  Clinics eligible for inactivation

In addition to the report options, the patch also provides tools to:

1\) Mark converted appointments with a "converted" status

2\) Cancel post-conversion appointments with a reason of

"Duplicate - Cerner"

3\) Inactivate all eligible clinics at a converted site.

The tools to mark converted appointments and to cancel post-conversion appointments are in 2 parts: 1) in bulk, i.e., based on the algorithms defined below and 2) individually, i.e., based on user interaction. Appointments that have encounters associated with them can be cleaned up (marked converted or cancelled) so long as the encounter's status is not ACTION REQUIRED. The exception to this rule is if the ACTION REQUIRED encounter is "empty." An encounter is "empty" if its associated visit has none of the following linked to it:

1\) Provider

2\) Diagnosis

3\) Service/Procedure

4\) Immunization

5\) Health Factor

6\) TIU Document

An encounter that has TIU Document(s) associated with it is considered "empty" if all of the TIU Documents have a status of RETRACTED.

The tool to inactivate clinics determines eligibility by the presence or absence of future scheduled appointments.

### User Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main cleanup menu (\[EHM_APPOINTMENT CLEANUP\]) is shown below. It is locked with the EHM_DATA CLEANUP security key.

CONV Converted Appointments ...

POST Post-Conversion Appointments ...

ACTA Active Appointments ...

ALL All Appointments ...

REQ Appointment Requests ...

ACO Appointment Cleanup Options ...

CC Clinic Cleanup Options ...

> **NOTE:** Some options can only be employed on converted sites to prevent inappropriate database changes. The error message – \*\*\* CAN BE RUN ON CONVERTED SITES ONLY \*\*\* – is returned if any of these options is selected on a non-converted VistA. Once the site is marked converted, the options are available to be executed without code changes or additional patch installation.

The specific options are:

Appointment Cleanup Options:

- Converted Appointment Cleanup
- Mark Appointment Converted
- Post-Conversion Appointment Cleanup
- Mark Appointment Cancelled

> Clinic Cleanup Options:

- Inactivate Clinics
  - Inactivate Converted Clinics

Most of the summaries and lists produced prompt the user for the actual or expected date of conversion. Future dates are permitted so that the tools provided can be used prospectively as well as retrospectively. Many of the options also can be run for all clinics, for all except selected clinics or for selected clinics. They also allow the user to include or exclude NON-COUNT clinics.

List options can be sorted three (3) different ways:

1)  Appointment date/time, patient, clinic
2)  Clinic, appointment date/time, patient
3)  Patient, appointment date/time, clinic

List options can be produced in two (2) formats:

1)  Formatted report
2)  Comma-delimited

Formatted reports are suitable for display on screen or to be printed. Comma-delimited output is suitable for uploading to Excel or to a relational database management system (RDBMS).

#### CONVERTED APPOINMENTS

Converted Appointments Algorithm: Converted appointments are those that have an appointment date that is on or after the conversion date and that were made before the conversion date. They must be active appointments and not entered more than two (2) years before the conversion date.

EHM\*1\*13 provides tools to summarize, list and close converted appointments with a status of "CONVERTED TO CERNER." Associated downstream records associated with the appointments (e.g., encounters) are all cancelled.

The <u>Converted Appointments</u> sub-menu is shown below.

SUMM Converted Appointment Summary

LIST Converted Appointment List

CSUM Converted Appts Summary with ACT REQ Encounters

CLST Converted Appts List with ACT REQ Encounters

The <u>Converted Appointment Summary</u> requires the actual or expected date of conversion. It can filter the clinics included in the report.

> Conversion Date: 1/1/21 (JAN 01, 2021)

> Select one of the following:

> I Include

> E Exclude

> Non-count Clinics: I// <span class="mark">Include</span>

> Select one of the following:

> A All

> X Excluding selected clinics

> S Selected clinics

> Clinics: All// <span class="mark">\<ret\></span>

> DEVICE: HOME// <span class="mark">\<ret\></span>

The summary outputs total number of appointments: 1) by month and year and 2) by clinic. Appointment counts are accompanied by the number of appointments: 1) with no encounters, 2) with ACTION REQUIRED encounters, 3) with empty ACTION REQUIRED encounters, and 4) with encounters with other status values.

> CONVERTED APPOINTMENT SUMMARY

> CONVERSION DATE: Jan 01, 2021

> DATE COUNT NO ENC ACT REQ EMPTY OTHER

> ---------- -------- -------- -------- -------- --------

> 01/2021 4802 4454 1 347

> 02/2021 3782 3538 244

> 03/2021 2370 2213 1 156

> 04/2021 933 847 1 85

> 05/2021 392 371 21

> 06/2021 17 17

> --------- -------- -------- -------- -------- --------

> TOTAL 12296 11440 3 0 853

CONVERTED APPOINTMENT SUMMARY

CONVERSION DATE: Jan 01, 2021

CLINIC COUNT NO ENC ACT REQ EMPTY OTHER

------------------------------ -------- -------- -------- -------- -----

AKR CARDIO MADAN MOHAN 1 1

AKR CARDIO NP CLAPHAM 23 23

AKR CARDIO NP CLAPHAM TELE 1 1

AKR CARDIO PROC ECHO 1 3 3

AKR DERM CSOLTKO 2 2

AKR DERM TARRILLION 9 9

AKR GI GREER 1 1

AKR HEM/ONC ATTD 2 10 10

AKR LAB 127 2 125

AKR MH SHERER 1 1

AKR NURSE VACCINE 1 1

AKR NUTR 3 3

AKR OPTOMETRY 1 158 158

AKR OPTOMETRY 2 85 85

AKR OPTOMETRY 3 142 142

AKR OPTOMETRY 4 17 17

AKR PACT 1 5 5

The <u>Converted Appointment List</u> shows appointment date/time, patient’s name and last 4 digits of Social Security Number, clinic name, appointment status, associated encounter status and the encounter’s unique ID. The user is prompted as shown below:

> Conversion Date: 1/1/21 (JAN 01, 2021)

> Select one of the following:

> 1 Appointment Date/Time, Patient, Clinic

> 2 Clinic, Appointment Date/Time, Patient

> 3 Patient, Appointment Date/Time, Clinic

> Sort Order: 1// <span class="mark">\<ret\></span> Appointment Date/Time, Patient, Clinic

> Select one of the following:

> I Include

> E Exclude

> Non-count Clinics: I// <span class="mark">I</span>nclude

> Select one of the following:

> A All

> X Excluding selected clinics

> S Selected clinics

> Clinics: All// <span class="mark">\<ret\></span>

> Select one of the following:

> 1 All

> 2 With Encounters

> 3 Without Encounters

> 4 Without ACTION REQUIRED Encounters

> Appointment Filter: ALL// <span class="mark">\<ret\></span> All

> Select one of the following:

> F Formatted Report

> C Comma-Delimited

> Output Format: Formatted Report//

> DEVICE: HOME// <span class="mark">;132</span> HOME(CRT)

Output of the formatted report is shown below. Output of the comma-delimited list includes all of the fields shown below but patient name and SSN are returned as separate fields. The full names of the patient and clinic are also output.

Converted Appointment List (All Appointments) p.1

Conversion Date: Jan 01, 2021

Appointment Appt \[-------------Encounter------------\]

Date/Time Patient Clinic Status Status Unique ID

-------------- ------------------------------ ------------------------------ ------ --------------------- -------------

01/04/21@08:40 AAAAAGER,C (0001) NPH PACT 4 NT ACTION REQUIRED 6CWJ8D-CLE

01/05/21@11:00 BBBBB,E (0002) MAN OPTOMETRY 2 blank EMPTY 6CVGW8-CLE

01/05/21@11:00 CCCCCX,A (0003) PRM PACT 9 blank EMPTY 6D0N3H-CLE

01/05/21@11:00 DDDDDRO,S (0004) AKR HEM/ONC ATTD 2 blank EMPTY 6CVG2M-CLE

01/05/21@11:00 EEEEEO,A (0005) MAN MH PHARM blank none

01/05/21@11:00 FFFFFNCY,M (0006) LOR OPTOMETRY 2 blank EMPTY 6CXTND-CLE

01/05/21@11:00 GGGGGN,C (0007) CLE NEPH MALIK blank EMPTY 6CPJHK-CLE

01/05/21@11:00 HHHHH,R (0008) WAR PACT 2 blank EMPTY 6D06T0-CLE

01/05/21@11:00 IIIII,L (0009) SAN PACT 2 NEW blank EMPTY 6JDPBT-CLE

01/05/21@11:20 JJJJJEFF,S (0010) LAK PODIATRY blank EMPTY 6CX85C-CLE

01/05/21@11:30 KKKKK,E (0011) CLE SLEEP FAREEHA I EMPTY 6CXCKN-CLE

The <u>Converted Appts Summary with ACT REQ Encounters</u> option produces a summary report of converted appointments that have encounters with non-empty ACTION REQUIRED status. As shown below, the user enters the conversion date and clinic filter information.

> Conversion Date: <span class="mark">1/1/21</span> (JAN 01, 2021)

> Select one of the following:

> I Include

> E Exclude

> Non-count Clinics: I// <span class="mark">Include</span>

> Select one of the following:

> A All

> X Excluding selected clinics

> S Selected clinics

> Clinics: All// <span class="mark">All</span>

> DEVICE: HOME// <span class="mark">\<ret\></span>

The resulting report shows counts by date and by clinic.

SUMMARY OF CONVERTED APPOINTMENTS WITH ACTION REQUIRED ENCOUNTERS

CONVERSION DATE: Jan 01, 2021

DATE COUNT

---------- --------

01/2021 1

03/2021 1

04/2021 1

--------- --------

TOTAL 3

SUMMARY OF CONVERTED APPOINTMENTS WITH ACTION REQUIRED ENCOUNTERS

CONVERSION DATE: Jan 01, 2021

CLINIC COUNT

------------------------------ --------

NPH PACT 4 2

YOU PACT 5 1

------------------------------ --------

TOTAL

The <u>Converted Appts List with ACT REQ Encounters</u> option produces a detailed report of converted appointments that have encounters with non-empty ACTION REQUIRED status. As shown below, the user enters the conversion date and clinic filter information.

> Conversion Date: <span class="mark">1/1/21</span> (JAN 01, 2021)

> Select one of the following:

> A All

> S Single

> Clinics: All// <span class="mark">\<ret\></span>

> Select one of the following:

> F Formatted Report

> C Comma-Delimited

> Output Format: Formatted Report// <span class="mark">\<ret\></span>

> DEVICE: HOME// <span class="mark">\<;132\></span> HOME(CRT)

The resulting report shows the appointment date/time, status, patient, clinic and the reason or reasons why the encounter is not empty.

ACTION REQUIRED Encounters for Converted Appointments

Conversion Date: Jan 01, 2021

Appt Date/Time Status Patient Clinic Associated Content

-------------- ------ ------------------------------ ------------------------------ -----------------------

01/04/21@08:40 NT AAAAAGER,C (0001) NPH PACT 4 TIU document

03/08/21@09:00 BBBBBA,S (0002) NPH PACT 4 TIU document

04/12/21@09:40 CCCCC,E (0003) YOU PACT 5 TIU document

#### POST-CONVERSION APPOINTMENTS

Post-Conversion Appointment Algorithm: Appointments added to a converted VistA after go-live are active appointments with an appointment date after the conversion date that were made after the conversion date.

EHM\*1\*13 provides tools to list these appointments and to cancel them with a cancellation reason of "duplicate of Cerner appointment." Associated downstream records associated with

the appointments (e.g., encounters) are all cancelled.

The <u>Post-Conversion Appointments</u> sub-menu is shown below.

SUMM Post Conversion Appointment Summary

LIST Post Conversion Appointment List

PSUM Post-Conv Appts Summary with ACT REQ Encounters

PLST Post-Conv Appts List with ACT REQ Encounters

The <u>Post Conversion Appointment Summary</u> requires the actual or expected date of conversion. It can filter the clinics included in the report.

> Conversion Date: 1/1/21 (JAN 01, 2021)

> Select one of the following:

> I Include

> E Exclude

> Non-count Clinics: I// <span class="mark">I</span>nclude

> Select one of the following:

> A All

> X Excluding selected clinics

> S Selected clinics

> Clinics: All// <span class="mark">\<ret\></span>

> DEVICE: HOME// <span class="mark">\<ret\></span>

The summary outputs total number of appointments: 1) by month and year and 2) by clinic. Appointment counts are accompanied by the number of appointments: 1) with no encounters, 2) with ACTION REQUIRED encounters, 3) with empty ACTION REQUIRED encounters, and 4) with encounters with other status values.

> POST-CONVERSION APPOINTMENT SUMMARY

> CONVERSION DATE: Jan 01, 2021

> DATE COUNT NO ENC ACT REQ EMPTY OTHER

> ---------- -------- -------- -------- -------- --------

> 03/2021 1 1

> 03/2024 1 1

> 03/2025 1 1

> --------- -------- -------- -------- -------- --------

> TOTAL 3 3 0 0 0

POST-CONVERSION APPOINTMENT SUMMARY

CONVERSION DATE: Jan 01, 2021

CLINIC COUNT NO ENC ACT REQ EMPTY OTHER

------------------------------ -------- -------- -------- -------- -----

AKR AUDIO CONSULT 2 2

CLE AUDIO CI 1 1

------------------------------ -------- -------- -------- -------- -----

TOTAL 3 3 0 0 0

The <u>Post Conversion Appointment List</u> shows appointment date/time, patient’s name and last 4 digits of Social Security Number, clinic name, appointment status, associated encounter status and the encounter’s unique ID. The user is prompted as shown below:

> Conversion Date: 1/1/21 (JAN 01, 2021)

> Select one of the following:

> 1 Appointment Date/Time, Patient, Clinic

> 2 Clinic, Appointment Date/Time, Patient

> 3 Patient, Appointment Date/Time, Clinic

> Sort Order: 1// <span class="mark">\<ret\></span> Appointment Date/Time, Patient, Clinic

> Select one of the following:

> I Include

> E Exclude

> Non-count Clinics: I// <span class="mark">I</span>nclude

> Select one of the following:

> A All

> X Excluding selected clinics

> S Selected clinics

> Clinics: All// <span class="mark">\<ret\></span>

> Select one of the following:

> 1 All

> 2 With Encounters

> 3 Without Encounters

> 4 Without ACTION REQUIRED Encounters

> Appointment Filter: ALL// <span class="mark">\<ret\></span> All

> Select one of the following:

> F Formatted Report

> C Comma-Delimited

> Output Format: Formatted Report// <span class="mark">\<ret\></span>

> DEVICE: HOME// <span class="mark">;132</span> HOME(CRT)

Output of the formatted report is shown below. Output of the comma-delimited list includes all of the fields shown below but patient name and SSN are returned as separate fields. The full names of the patient and clinic are output.

Post Go-Live Appointment List (All Appointments) p. 1

Conversion Date: Jan 01, 2021

Appointment Appt \[-------------Encounter------------\] Appointment

Date/Time Patient Clinic Status Status Unique ID/IEN Made/Made By

-------------- ------------------------------ ------------------------------ ------ --------------------- ------------- --------------------

03/11/21@13:00 AAAAALL,M (0001) CLE AUDIO CI blank none 3/9/21

ZZZZZMAN,P

03/15/24@10:00 BBBBBAND,A (0002) AKR AUDIO CONSULT blank none 3/13/24

YYYYY,W

03/12/25@10:00 BBBBBND,A (0002) AKR AUDIO CONSULT blank none 3/13/24

YYYYY,W

TOTAL RECORDS = 3

The <u>Post-Conv Appts Summary with ACT REQ Encounters</u> option produces a summary report of post-conversion appointments that have encounters with non-empty ACTION REQUIRED status. As shown below, the user enters the conversion date and clinic filter information.

> Conversion Date: <span class="mark">1/1/21</span> (JAN 01, 2021)

> Select one of the following:

> I Include

> E Exclude

> Non-count Clinics: I// <span class="mark">Include</span>

> Select one of the following:

> A All

> X Excluding selected clinics

> S Selected clinics

> Clinics: All// <span class="mark">All</span>

> DEVICE: HOME// <span class="mark">\<ret\></span>

The resulting report shows counts by date and by clinic.

SUMMARY OF POST-CONVERSION APPOINTMENTS WITH ACTION REQUIRED ENCOUNTERS

CONVERSION DATE: May 01, 2020

DATE COUNT

---------- --------

05/2020 291

06/2020 19

07/2020 1

08/2020 1

11/2020 1

--------- --------

TOTAL 313

SUMMARY OF POST-CONVERSION APPOINTMENTS WITH ACTION REQUIRED ENCOUNTERS

CONVERSION DATE: May 01, 2020

CLINIC COUNT

------------------------------ --------

AKR CARDIO NP CLAPHAM TELE 1

AKR COVID SCREENING 5

AKR MH BERG TELE 3

AKR MH DESMARAIS VH 1

AKR MH KEIPER TELE 1

AKR PACT 12 TELE 1

AKR PACT 3 TELE 1

AKR PHARM TELE A 1

AKR PHARM TELE B 3

AKR PMRS 2

AKR SPECIALTY NURSE 2

CAN COVID SCREENING 2

------------------------------ --------

TOTAL 23

The <u>Post-Conv Appts List with ACT REQ Encounters</u> option produces a detailed report of post-conversion appointments that have encounters with non-empty ACTION REQUIRED status. As shown below, the user enters the conversion date and clinic filter information.

> Conversion Date: <span class="mark">5/1/20</span> (MAY 01, 2020)

> Select one of the following:

> A All

> S Single

> Clinics: All// <span class="mark">\<ret\></span>

> Select one of the following:

> F Formatted Report

> C Comma-Delimited

> Output Format: Formatted Report// <span class="mark">\<ret\></span>

> DEVICE: HOME// <span class="mark">\<;132\></span> HOME(CRT)

The resulting report shows the appointment date/time, status, patient, clinic and the reason or reasons why the encounter is not empty.

ACTION REQUIRED Encounters for Post-Conversion Appointments

Conversion Date: May 01, 2020

Appt Date/Time Status Patient Clinic Associated Content

-------------- ------ ------------------------------ ------------------------------ -----------------------

05/13/20@10:00 NT VVVVVR,W (0001) CLE POLYTRAUMA BEH MED VH TIU document

05/13/20@10:30 NT WWWWWAM,B (0002) CLE SCI CVT VIDEO HOME TIU document

05/13/20@11:30 XXXXX,S (0003) ELP PHARM TELE Provider

TIU document

05/14/20@10:00 NT YYYYR,C (0004) CLE HEM/ONC FELLOW D Health factor

TIU document

#### ACTIVE APPOINTMENTS

The tools for managing active appointments are useful pre-conversion to list upcoming appointments and to manage them especially when non-VistA applications (e.g., Dental) are involved.

The <u>Active Appointments</u> sub-menu is shown below.

SUMM Active Appointment Summary

LIST Active Appointment List

The <u>Active Appointment Summary</u> requires the actual or expected date of conversion. It can be run for all clinics, for a single clinic or for all clinics that share a single stop code.

> Conversion Date: <span class="mark">1/1/21</span> (JAN 01, 2021)

> Select one of the following:

> A All Clinics

> S Single Clinic

> C Single Stop Code

> Filter: All// <span class="mark">\<ret\></span> Clinics

> DEVICE: HOME// <span class="mark">\<ret\></span> HOME(CRT)

The summary outputs total number of appointments: 1) by month and year and 2) by clinic. Appointment counts are accompanied by the number of appointments: 1) with no encounters, 2) with ACTION REQUIRED encounters, 3) with “empty” ACTION REQUIRED encounters, and 4) with encounters with other status values.

ACTIVE APPOINTMENT SUMMARY

CONVERSION DATE: Jan 01, 2021

DATE COUNT NO ENC ACT REQ EMPTY OTHER

---------- -------- -------- -------- -------- --------

01/2021 4523 4180 1 342

02/2021 3620 3378 242

03/2021 2240 2083 1 156

04/2021 843 757 1 85

05/2021 387 366 21

06/2021 17 17

05/2022 1 1

03/2024 1 1

03/2025 1 1

--------- -------- -------- -------- -------- --------

TOTAL 11633 10784 3 0 846

ACTIVE APPOINTMENT SUMMARY

CONVERSION DATE: Jan 01, 2021

CLINIC COUNT NO ENC ACT REQ EMPTY OTHER

------------------------------ -------- -------- -------- -------- -----

AKR AUDIO CONSULT 2 2

AKR CARDIO MADAN MOHAN 1 1

AKR CARDIO NP CLAPHAM 23 23

AKR CARDIO NP CLAPHAM TELE 1 1

AKR CARDIO PROC ECHO 1 3 3

AKR DERM CSOLTKO 2 2

AKR DERM TARRILLION 9 9

AKR GI GREER 1 1

AKR HEM/ONC ATTD 2 10 10

AKR LAB 127 2 125

AKR MH SHERER 1 1

AKR NURSE VACCINE 1 1

AKR NUTR 3 3

AKR OPTOMETRY 1 158 158

AKR OPTOMETRY 2 85 85

AKR OPTOMETRY 3 142 142

AKR OPTOMETRY 4 17 17

The <u>Active Appointment List</u> option shows appointment date/time, patient’s name, date of birth, EDIPI, clinic name, and, optionally, dental classification. The user is prompted for: 1) the actual or expected date of conversion, 2) report sort order, 3) include all or a single clinic or all clinics for a stop code, 4) whether to display dental classification, and 5) output format.

> Conversion Date: <span class="mark">1/1/21</span> (JAN 01, 2021)

> Select one of the following:

> 1 Appointment Date/Time, Patient, Clinic

> 2 Clinic, Appointment Date/Time, Patient

> 3 Patient, Appointment Date/Time, Clinic

> Sort Order: 1// <span class="mark">\<ret\></span> Appointment Date/Time, Patient, Clinic

> Select one of the following:

> A All Clinics

> S Single Clinic

> C Single Stop Code

> Filter: All// <span class="mark">\<ret\></span> Clinics

> Display dental classification? NO// <span class="mark">\<ret\></span>

> Select one of the following:

> F Formatted Report

> C Comma-Delimited

> Output Format: Formatted Report// <span class="mark">\<ret\></span>

> DEVICE: HOME// <span class="mark">\<ret\></span> HOME(CRT)

Output of the formatted report displays appointment date/time, patient name, and date of birth, EDIPI and clinic name.

Active Appointment List - Station 541

Conversion Date: Jan 01, 2021

Appt Date/Time Patient DOB EDIPI Clinic

-------------- --------------- ----------- ---------- ----------------

01/02/21@08:00 AAAET,GONZO SEP 6,1953 \<redacted\> W RAD CAT SCAN

01/02/21@10:30 BBBLETH,GRADY NOV 6,1956 \<redacted\> W RAD CAT SCAN

01/03/21@11:04 CCCTIGO,CHUCK L JUN 22,1951 \<redacted\> CLE CARDIO ECG

01/04/21@07:30 DDDLSETH,STEVE DEC 8,1956 \<redacted\> W RAD CAT SCAN

#### ALL APPOINTMENTS

The tools for managing all appointments are intended for use after converted and post-conversion appointments are cleaned up. At that point, these tools will show what's left in VistA. They can then be used to determine what to do with them.

The <u>All Appointments</u> sub-menu is shown below.

SUMM All Appointment Summary

LIST All Appointment List

ASUM All Appts Summary with ACT REQ Encounters

ALST All Appts List with ACT REQ Encounters

The <u>All Appointment Summary</u> option prompts the user to filter clinics as shown below.

> Select one of the following:

> I Include

> E Exclude

> Non-count Clinics: I// <span class="mark">Include</span>

> Select one of the following:

> A All

> X Excluding selected clinics

> S Selected clinics

> Clinics: All// <span class="mark">All</span>

> DEVICE: HOME// <span class="mark">\<ret\></span>

The summary outputs total number of appointments: 1) by month and year and 2) by clinic. Appointment counts are accompanied by the number of appointments: 1) with no encounters, 2) with ACTION REQUIRED encounters, 3) with “empty” ACTION REQUIRED encounters, and 4) with encounters with other status values.

ALL APPOINTMENT SUMMARY

DATE COUNT NO ENC ACT REQ EMPTY OTHER

---------- -------- -------- -------- -------- --------

02/2020 5339 239 5100

03/2020 4817 232 5 4580

04/2020 3050 238 26 2786

05/2020 22979 18391 547 4041

06/2020 45444 42759 165 2520

07/2020 34556 32305 37 2214

08/2020 25969 24135 40 1794

09/2020 17609 16008 22 1579

10/2020 13422 12175 14 1233

11/2020 8446 7640 5 801

12/2020 3770 3495 3 272

01/2021 4505 4168 1 336

02/2021 3610 3370 240

03/2021 2235 2079 1 155

04/2021 840 757 1 82

05/2021 386 365 21

ALL APPOINTMENT SUMMARY

CLINIC COUNT NO ENC ACT REQ EMPTY OTHER

------------------------------ -------- -------- -------- -------- -----

AKR ADMIN PROCESSING 18487 7 18480

AKR AUDIO CONSULT 159 157 2

AKR AUDIO HAE 43 43

AKR AUDIO REPAIR 12 12

AKR CARDIO MADAN MOHAN 8 8

AKR CARDIO MADAN MOHAN TELE 28 28

AKR CARDIO NP CLAPHAM 489 487 2

AKR CARDIO NP CLAPHAM TELE 378 364 12 2

AKR CARDIO PROC ECHO 1 137 135 2

AKR CARDIO SPRINT 586 586

AKR COVID SCREENING 19 16 3

AKR DERM CSOLTKO 166 166

AKR DERM TARRILLION 331 331

AKR DERM TELEDERM 1 1

AKR DM 1 GRP 2 2

AKR DM SMA GRP 6 6

AKR GI DOLNEY 34 34

The <u>All Appointment List</u> option shows appointment date/time, patient’s name and last 4 digits of Social Security Number, clinic name, appointment, and associated encounter status. The user is prompted for: 1) report sort order, 2) include all or a single clinic, and 3) output format.

Select one of the following:

I Include

E Exclude

Non-count Clinics: I// <span class="mark">Include</span>

Select one of the following:

A All

X Excluding selected clinics

S Selected clinics

Clinics: All// <span class="mark">Selected clinics</span>

Clinic to include: <span class="mark">AKR CARDIO NP CLAPHAM TELE</span> LATTRELL,WILLA

Clinic to include:

Select one of the following:

F Formatted Report

C Comma-Delimited

Output Format: Formatted Report// <span class="mark">\<ret\></span>

DEVICE: HOME// <span class="mark">;132</span> HOME(CRT)

Output of the formatted report is shown below.

All Appointments List - AKR CARDIO NP CLAPHAM TELE

Appt Date/Time Patient Clinic Status Encounter

-------------- ------------------------------ ------------------------------ ------ ---------------------

05/19/20@10:30 NNNES,G (0000) AKR CARDIO NP CLAPHAM TELE blank ACTION REQUIRED

05/19/20@13:30 CCCALLI,O (0001) AKR CARDIO NP CLAPHAM TELE blank ACTION REQUIRED

05/19/20@15:00 KKKYMAN,W (0002) AKR CARDIO NP CLAPHAM TELE blank ACTION REQUIRED

05/20/20@08:30 PPPPIN,M (0003) AKR CARDIO NP CLAPHAM TELE blank blank

05/20/20@09:00 NNNNEN,N (0004) AKR CARDIO NP CLAPHAM TELE blank blank

05/20/20@09:30 AAAZOLA,T (0005) AKR CARDIO NP CLAPHAM TELE blank blank

05/20/20@10:00 GGGESS,O (0006) AKR CARDIO NP CLAPHAM TELE blank blank

The <u>All Appts Summary with ACT REQ Encounters</u> option produces a summary report of appointments that have encounters with non-empty ACTION REQUIRED status. As shown below, the user enters clinic filter information.

> Select one of the following:

> I Include

> E Exclude

> Non-count Clinics: I// <span class="mark">Include</span>

> Select one of the following:

> A All

> X Excluding selected clinics

> S Selected clinics

> Clinics: All// <span class="mark">All</span>

> DEVICE: HOME// <span class="mark">\<ret\></span>

The resulting report shows counts by date and by clinic.

SUMMARY OF ALL APPOINTMENTS WITH ACTION REQUIRED ENCOUNTERS

CONVERSION DATE: May 01, 2020

DATE COUNT

---------- --------

05/2020 291

06/2020 19

07/2020 1

08/2020 1

11/2020 1

--------- --------

TOTAL 313

SUMMARY OF ALL APPOINTMENTS WITH ACTION REQUIRED ENCOUNTERS

CONVERSION DATE: May 01, 2020

CLINIC COUNT

------------------------------ --------

AKR CARDIO NP CLAPHAM TELE 1

AKR COVID SCREENING 5

AKR MH BERG TELE 3

AKR MH DESMARAIS VH 1

AKR MH KEIPER TELE 1

AKR PACT 12 TELE 1

AKR PACT 3 TELE 1

AKR PHARM TELE A 1

AKR PHARM TELE B 3

AKR PMRS 2

AKR SPECIALTY NURSE 2

CAN COVID SCREENING 2

------------------------------ --------

TOTAL 23

The <u>All Appts List with ACT REQ Encounters</u> option produces a detailed report of appointments that have encounters with non-empty ACTION REQUIRED status. As shown below, the user enters clinic filter information.

> Select one of the following:

> I Include

> E Exclude

> Non-count Clinics: I// <span class="mark">Include</span>

> Select one of the following:

> A All

> X Excluding selected clinics

> S Selected clinics

> Clinics: All// <span class="mark">Selected clinics</span>

> Clinic to include: <span class="mark">AKR COVID SCREENING</span> FOLLMAN,BRIDGETTE M

> Clinic to include: <span class="mark">AKR PHARM TELE B</span> GIGUERE,CARMELA C

> Clinic to include:

> Select one of the following:

> F Formatted Report

> C Comma-Delimited

> Output Format: Formatted Report// <span class="mark">\<ret\></span>

> DEVICE: HOME// <span class="mark">;132</span> HOME(CRT)

The resulting report shows the appointment date/time, status, patient, clinic and the reason or reasons why the encounter is not empty.

ACTION REQUIRED Encounters for All Appointments

Appt Date/Time Status Patient Clinic Associated Content

-------------- ------ ------------------------------ ------------------------------ -----------------------

05/15/20@10:00 NT AAAAAER,V (0001) AKR COVID SCREENING TIU document

05/18/20@13:30 NT BBBBBBO,M (0002) AKR COVID SCREENING TIU document

05/19/20@08:30 CCCCCC,T (0003 AKR PHARM TELE B Provider

Diagnosis

Service/procedure

Health factor

TIU document

05/19/20@11:00 DDDDDON,S (0004) AKR PHARM TELE B Health factor

TIU document

#### APPOINTMENT REQUESTS

This patch also includes limited tools for managing active appointment requests. Both options report active appointment requests from: 1) SDEC APPT REQUEST file (#409.85), 2) SD WAIT LIST file (#409.3) and 3) RECALL REMINDERS file (#403.5).

The <u>Appointment Requests</u> sub-menu is shown below.

SUMM Appointment Request Summary

LIST Appointment Request List

The <u>Appointment Request Summary</u> option outputs counts of active appointment requests summarized by source file, by date (month and year) and by clinic.

> **NOTE:** Appointment requests that come from the SDEC APPT REQUEST file (#409.85) are sub-divided by type of request (field \#4). Appointment (APPT) and return to clinic (RTC) are reported separately. All other request types (e.g., VETERAN, MOBILE) are reported under OTHER.

To produce the summary report, the user selects the appointment request source as shown below.

> Select one of the following:

> ALL All Sources

> REQ Appointment Requests

> WAIT Wait List

> RECALL Recall Reminders

> Source: ALL Sources// <span class="mark">\<ret\></span> All Sources

> DEVICE: HOME// <span class="mark">\<ret\></span>

The output of the summary is in three parts: 1) summary by source, 2) summary by date, and 3) summary by requested clinic.

Appointment Request Summary

SOURCE COUNT

------------------ --------

APPT REQ-APPT 64081

APPT REQ-RTC 58994

APPT REQ-OTHER 0

RECALL 45956

WAIT LIST 48

--------------- --------

TOTAL 169079

Appointment Request Summary

DATE COUNT

---------- --------

01/2021 2206

02/2021 1958

03/2021 1592

04/2021 1093

Appointment Request Summary

CLINIC COUNT

------------------------------ --------

AKR ADMIN PROCESSING 42

AKR AMPUTEE VIDEO PATIENT 2

AKR AUDIO CONSULT 399

AKR AUDIO CONSULT MMU 8

AKR AUDIO HAE 77

AKR AUDIO HAE VIDEO PATIENT 1

AKR AUDIO REPAIR 10

AKR AUDIO WALK-IN 165

The <u>Appointment Request List</u> option outputs the requested date for the appointment, patient’s name, clinic name and the source file where the request resides. The user is prompted for the source of requests, sort order and output format.

Select one of the following:

ALL All Sources

REQ Appointment Requests

WAIT Wait List

RECALL Recall Reminders

Source: ALL Sources// <span class="mark">\<ret\></span> All Sources

Select one of the following:

1 Requested Date of Appointment, Patient, Requested Clinic

2 Requested Clinic, Requested Date of Appointment, Patient

3 Patient, Requested Date of Appointment, Requested Clinic

Sort Order: 1// <span class="mark">\<ret\></span> Requested Date of Appointment, Patient, Requested Clinic

Select one of the following:

F Formatted Report

C Comma-Delimited

Output Format: Formatted Report// <span class="mark">\<ret\></span>

DEVICE: HOME// <span class="mark">;132</span>

Output of the formatted report is shown below.

Open Appointment Request List - Station 541

Requested Date Patient Clinic Source Req IEN PID

-------------- ------------------------------ ------------------------------ --------------- --------- --------------

May 21, 2020 LXXXXX,R (0001) RAV PODIATRY APPT REQ-APPT 7111620 May 21, 2020

May 21, 2020 LYYYYY,E (0002) AKR PACT 8 RECALL

May 21, 2020 LZZZZZ,Q (0003) CLE SPINE NEUROSURGERY PHONE APPT REQ-RTC 7116991 May 21, 2020

May 21, 2020 LAAAAA,O (0004) CLE RO/RE-EVAL 1 APPT REQ-APPT 7093993 May 21, 2020

May 21, 2020 LBBBBB,O (0005) W RO/SIMULATION APPT REQ-APPT 6839980 May 21, 2020

#### APPOINTMENT CLEANUP OPTIONS

The Appointment Cleanup Options sub-menu of EHM\*1\*13 is used to mark converted appointments CONVERTED and post-conversion appointments CANCELLED.

The <u>Appointment Cleanup Options</u> sub-menu is shown below.

CAP Converted Appointment Cleanup

MACO Mark Appointment Converted

PAC Post-Conversion Appointment Cleanup

MAC Mark Appointment Cancelled

The <u>Converted Appointment Cleanup</u> option first identifies appointments that have been converted to Cerner using the “appointment date after date of conversion that was entered before date of conversion” algorithm described above. It then changes each appointment’s status in the Patient file (#2) and in the SDEC Appointment file (#409.84) to “CNV – Converted to Cerner”. Downstream files (e.g., Outpatient Encounter (#409.68)) are then updated as if the appointment had been cancelled. The user is asked for the date of conversion and for any clinic filter.

Output from this option is the appointment date/time, patient’s name, clinic name and cleanup result. As shown below, if the appointment is successfully marked converted, “OK” is returned. If the process is unsuccessful, an error message is returned.

> 01/04/21@08:40 HHHINGER,RONALD N TIN...OK

> 03/08/21@09:00 IIILLA,ALBERT N TIN cannot be automatically converted. Appointment has ACTION REQUIRED encounter.

> 04/12/21@09:40 JJJEZ,CHRISTOPHER YNEM...OK

The <u>Mark Appointment Converted</u> option can be used to mark individual appointments converted. The user is prompted for clinic, patient, and admission date. A list of eligible appointments is displayed which the user can select from. “Eligible” appointments must be active and cannot be linked to a non-empty ACTION REQUIRED encounter. Note that the option does not enforce compliance with the converted appointments algorithm employed with bulk cleanup. Any eligible appointment can be marked converted.

Mark appointment converted

Select HOSPITAL LOCATION NAME: <span class="mark">AKR NCT</span> AKR CARDIO NP CLAPHAM TELE LATTRELL,

WILLA

Select PATIENT NAME: <span class="mark">XXXPIN,M</span>

1 XXXPIN,MARCEL JOSEPH 1-1-99 \<SSN redacted\> NO NSC VETERAN

2 XXXPIN,MICHAEL GREGORY 2-2-98 \<SSN redacted\> NO NSC VETERAN

CHOOSE 1-2: <span class="mark">2</span> XXXPIN,MARCEL JOSEPH 1-1-99 \<SSN redacted\> NO NSC VETERAN

Enrollment Priority: GROUP 5 Category: ENROLLED End Date:

Appointment Date: <span class="mark">5/20/20</span> (MAY 20, 2020)

Appointment Date/Time Encounter Status

--------------------- ------------------------------

1\. May 20, 2020@08:30

Select Appointment: (1-1): <span class="mark">1</span>

MARKED CONVERTED

The <u>Post-Conversion Appointment Cleanup</u> option first identifies appointments that have been entered post-conversion using the “appointment date after date of conversion that was entered after date of conversion” algorithm described above. It then cancels each appointment with the cancellation reason “DUPLICATE – CERNER.” Downstream files (e.g., Outpatient Encounter (#409.68)) are also cancelled. The user is asked for the date of conversion and for any clinic filter.

Output from this option is the appointment date/time, patient’s name, clinic name and cleanup result. As shown below, if the appointment is successfully marked cancelled, “OK” is returned. If the process is unsuccessful, an error message is returned.

> 01/04/21@08:40 HHHINGER,RONALD N TIN...OK

> 03/08/21@09:00 IIILLA,ALBERT N TIN cannot be automatically cancelled. Appointment has ACTION REQUIRED encounter.

> 04/12/21@09:40 JJJEZ,CHRISTOPHER YNEM...OK

The <u>Mark Appointment Cancelled</u> option can be used to mark individual appointments cancelled. The user is prompted for clinic, patient, and admission date. A list of eligible appointments is displayed which the user can select from. “Eligible” appointments must be active and cannot be linked to a non-empty ACTION REQUIRED encounter. Note that the option does not enforce compliance with the post-conversion appointments algorithm employed with bulk cleanup. Any eligible appointment can be cancelled.

Mark appointment cancelled

Select HOSPITAL LOCATION NAME: <span class="mark">AKR NCT</span> AKR CARDIO NP CLAPHAM TELE LATTRELL,

WILLA

Select PATIENT NAME: <span class="mark">XXXPIN,M</span>

1 XXXPIN,MARCEL JOSEPH 1-1-99 \<SSN redacted\> NO NSC VETERAN

2 XXXPIN,MICHAEL GREGORY 2-2-98 \<SSN redacted\> NO NSC VETERAN

CHOOSE 1-2: <span class="mark">2</span> XXXPIN,MARCEL JOSEPH 1-1-99 \<SSN redacted\> NO NSC VETERAN

Enrollment Priority: GROUP 5 Category: ENROLLED End Date:

Appointment Date: <span class="mark">5/20/20</span> (MAY 20, 2020)

Appointment Date/Time Encounter Status

--------------------- ------------------------------

1\. May 20, 2020@08:30

Select Appointment: (1-1): <span class="mark">1</span>

MARKED CANCELLED

#### CLINIC CLEANUP OPTIONS

Clinic Cleanup Options sub-menu is used to maintain the list of active clinics post-conversion and to inactivate clinics that are not active post-conversion.

The Clinic Cleanup Options sub-menu is shown below.

ACTC Active Clinics ...

INAC Inactivate Clinics ...

#### ACTIVE CLINICS

The Active Clinics sub-menu of EHM\*1\*13 is used to identify those clinics, if any, that are active in VistA post conversion to Millennium. Post-conversion appointments in these clinics will not be automatically cancelled, and the clinics will not be inactivated.

The ACTIVE CLINICS sub-menu is shown below.

EDIT Active Clinic Add/Edit

LIST Active Clinic List

The <u>Active Clinic Add/Edit</u> option prompts the user to add or delete clinics in the EHRM ACTIVE CLINIC file (#1610). Adding or deleting clinics can be done by name (single clinic) or by stop code (set of clinics). Sample interaction is shown below.

Select ACTIVE CLINICS \<TEST ACCOUNT\> Option: <span class="mark">EDIT</span> Active Clinic Add/Edit

Select one of the following:

NAME Clinic Name

STOP Stop Code

Select by: NAME// <span class="mark">\<RET\></span> Clinic Name

Select CLINIC to add or delete from the EHRM ACTIVE CLINIC file.

Select HOSPITAL LOCATION NAME: <span class="mark">CLE</span>

1 CLE ACCORD DIABETES RESEARCH HENSEN,ISSAC

2 CLE ADMIN PROCESSING

3 CLE ADMISSION

4 CLE ADVICE NURSE TELE

5 CLE ALCOHOL DETOX ECONS OUTPT

Press \<Enter\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <span class="mark">3</span> CLE ADMISSION

Add clinic to EHRM ACTIVE CLINIC file?? YES// <span class="mark">\<RET\></span>...Added

Select HOSPITAL LOCATION NAME: <span class="mark">\<space bar\></span> CLE ADMISSION

Delete clinic from EHRM ACTIVE CLINIC file?? NO// <span class="mark">YES</span>...Deleted

Select HOSPITAL LOCATION NAME: <span class="mark">\<RET\></span>

EDIT Active Clinic Add/Edit

LIST Active Clinic List

Select ACTIVE CLINICS \<TEST ACCOUNT\> Option: <span class="mark">ED</span> Active Clinic Add/Edit

Select one of the following:

NAME Clinic Name

STOP Stop Code

Select by: NAME// <span class="mark">S</span>top Code

Select STOP CODE of clinics to add or delete from the EHRM ACTIVE CLINIC file.

Select CLINIC STOP NAME: <span class="mark">OPH</span>

1 OPHTHALMOLOGY 58 10-01-1987

2 OPHTHALMOLOGY 407

CHOOSE 1-2: <span class="mark">2</span> OPHTHALMOLOGY 407

Select one of the following:

A Add

D Delete

Clinics matching stop code: <span class="mark">A</span>// dd

ZZB EYE/GALAINENA...Inactive. Skipped.

ZZ W OPHTH/FU...Inactive. Skipped.

CLE OPHTH CORNEA...Added.

CLE OPHTH GENERAL...Added.

CLE RESEARCH EYE MOVE 09080H50...Added.

CLE CODING IP OPHTH-X...Added.

ZZCLE OPHTH RETINA FRI...Inactive. Skipped.

CLE OPHTH GLAUCOMA...Already in EHRM ACTIVE CLINIC file.

EDIT Active Clinic Add/Edit

LIST Active Clinic List

Select ACTIVE CLINICS \<TEST ACCOUNT\> Option: <span class="mark">ED</span> Active Clinic Add/Edit

Select one of the following:

NAME Clinic Name

STOP Stop Code

Select by: NAME// <span class="mark">S</span>top Code

Select STOP CODE of clinics to add or delete from the EHRM ACTIVE CLINIC file.

Select CLINIC STOP NAME: <span class="mark">OPH</span> OPHTHALMOLOGY 407

Select one of the following:

A Add

D Delete

Clinics matching stop code: A// <span class="mark">D</span>elete

ZZB EYE/GALAINENA...Not in file.

ZZ W OPHTH/FU...Not in file.

CLE OPHTH CORNEA...Deleted

CLE OPHTH GENERAL...Deleted

CLE RESEARCH EYE MOVE 09080H50...Deleted

CLE CODING IP OPHTH-X...Deleted.

ZZCLE OPHTH RETINA FRI...Not in file.

CLE OPHTH GLAUCOMA...Deleted

The <u>Active Clinic List</u> option employs standard FileMan interaction on the EHRM ACTIVE CLINIC file (#1610). Sample output is shown below.

Select ACTIVE CLINICS \<TEST ACCOUNT\> Option: <span class="mark">LIST</span> Active Clinic List

Start with CLINIC: FIRST// <span class="mark">\<RET\></span>

DEVICE: HOME(CRT) <span class="mark">\<RET\></span> Right Margin: 80// <span class="mark">\<RET\></span>

ACTIVE CLINIC LIST JUL 01, 2024@15:15 PAGE 1

CLINIC

-----------------------------------------------------------------------------

CLE ACCORD DIABETES RESEARCH

CLE ALLERGY ECONSULT

#### INACTIVATE CLINICS

EHM\*1\*13 also provides a tool to automatically inactivate clinics at a converted site. The tool skips clinics that are identified as active in VistA after conversion. The tool also skips clinics that have active appointments post-conversion.

The <u>Inactivate Clinics</u> sub-menu is shown below.

LIST Inactivate Clinics List

INAC Inactivate Converted Clinics

The <u>Inactivate Clinics List</u> option can be used as a precursor to actual clinic activation. The report lists clinics and their inactivation status – eligible for inactivation, active post go-live, inactive, Cannot be inactivated. The user is prompted to filter the report as shown below.

> Select one of the following:

> 1 All Clinics

> 2 All except Inactive Clinics

> 3 Clinics Eligible for Inactivation

> 4 Clinics with Future Appointments

> Report Filter: 1// All Clinics

> DEVICE: HOME//

Sample output is shown below.

Clinic Inactivation List: All Clinics

CLINIC STATUS

------------------------------ ---------------------------------------------

1003 INACTIVE

06182109 INACTIVE

ADM (BLOOD) ELIGIBLE FOR INACTIVATION

ADMIT-SCREEN-PRINCIPAL CLINIC ELIGIBLE FOR INACTIVATION

ADULT DAYCARE/PRINCIPAL CLINIC ELIGIBLE FOR INACTIVATION

ADVANCED MRIMAGING INACTIVE

ADVANCED MRIMAGING ELIGIBLE FOR INACTIVATION

AKR ADMIN PROCESSING ACTIVE POST GO-LIVE

AKR AMPUTEE VIDEO PATIENT ELIGIBLE FOR INACTIVATION

AKR AUDIO CONSULT CANNOT BE INACTIVATED. 1 APPOINTMENT PRESENT.

AKR AUDIO CONSULT MMU ELIGIBLE FOR INACTIVATION

AKR AUDIO HAE ELIGIBLE FOR INACTIVATION

The <u>Inactivate Converted Clinics</u> option performs clinic inactivation. User interaction is as follows:

DATE OF CONVERSION: <span class="mark">1/1/22</span>

\*\*\* This option INACTIVATES all eligible clinics. \*\*\*

Are you sure?? NO// <span class="mark">YES</span>

Inactivating clinics.....................

YOU PACT 8 INACTIVATED

YOU PACT 8 EH INACTIVATED

YOU PACT 8 NEW INACTIVATED

YOU PACT 8 NURSE INACTIVATED

YOU PACT 8 NURSE TELE INACTIVATED

YOU PACT 8 NURSE VH INACTIVATED

YOU PACT 8 RN INACTIVATED

YOU PACT 8 TELE INACTIVATED

YOU PACT 8 TELE NEW INACTIVATED

YOU PACT 8 VH INACTIVATED

YOU PACT 8 VH NEW INACTIVATED

YOU PACT 8 WH INACTIVATED

CLINICS INACTIVATED: 7877

INACTIVATION FAILED: 0

Future appointments: 0

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All data flows supported by EHM\*1\*13 patch are internal to VistA.

### User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users who need to access the EHM_APPOINTMENT CLEANUP option will need to be assigned the EHM_DATA CLEANUP security key.

### Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHM\*1\*13 and EHM_APPOINTMENT CLEANUP are deployed only to VistA sites that have been converted or that are in the process of being converted.

### Using the Software / Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Patch EHM\*1\*13 creates tools needed for data cleanup on sites converted from VistA to Millennium. The patch will not be released nationally.

## EHM\*1\*15 – Automated Patient Discharge Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the night of cutover to Cerner, all inpatients are discharged out of VistA. EHM\*1\*15 supplies the Automated Patient Discharge Tool to identify and automatically discharge those patients. The patch is a component of the EHM Package. It is not nationally released.

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Automated Patient Discharge Tool is loaded via EHM\*1\*15. Its primary menu is EHM_DISCHARGE MENU.

### Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All data flows supported by the Automated Patient Discharge Tool are internal to VistA.

### User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No security keys are included in this patch.

### Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Automated Patient Discharge Tool does not impact routine VistA operations.

### Using the Software / Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Patch EHM\*1\*15 creates the Automated Patient Discharge Tool to discharge automatically all eligible patients in VistA. Its options are needed on the night of cutover from VistA to Cerner Millennium.

The Patient Discharge Tool’s primary menu is EHM_DISCHARGE MENU. It is shown below.

> Select Patient Discharge Menu Option: ?

AUTO Discharge Patients

LIST Patient Discharge List

POST Discharged Patients List

SUMM Patient Discharge Summary

#### Discharge Patients \[EHM_DISCHARGE PATIENTS\]

This option builds a list of patients eligible for discharge and then loops through the list and discharges them one at a time. Shown below is one patient being discharged. There is no user interaction.

INSTITUTION (STA): CLEVELAND PRRTP (541PA)

BCWT/TR1 BBBBB,CCCCCNEY L 10/10/19 22:53

BA205-1

Primary Care Team: CLE PC 4B

PC Provider: BOGUS,PAT Position: NURSE PRACTITIONER

Pager: Phone: (444) 444-4444

Status : ACTIVE INPATIENT-on WARD

Admitted : OCT 10,2019@22:53:19 Transferred : MAR 29,2020@22:00

Ward : BCWT/TR1 Room-Bed : BA205-1

Provider : IIIII,STEFAN Specialty : GEN CWT/TR

Attending : IIIII,STEFAN

Admission LOS: 1743 Absence days: 0 Pass Days: 12 ASIH days: 0ONTINUE

DISCHARGE DATE: NOW// (JUL 18,2024@08:32:46)

Patient Discharged

Updating appointment status...completed.

Executing HL7 ADT Messaging

Executing HL7 ADT Messaging

Executing HL7 ADT Messaging (RAI/MDS)

Updating incomplete records...

Means Test Signed?:

Means Test Not Required

Primary Means Test Last Applied 'NOV 16,2016' (NO LONGER REQUIRED: JAN 24,2020)

Updating claims tracking ... completed.

Updating Transfer Pricing has been...completed.

...Inpatient Medications check...

...discontinuing Inpatient Medication orders....done...

Updating automated team lists...completed.

Updating visit status...completed.

...updating Pyxis data base...done

#### Patient Discharge List \[EHM_DISCHARGE LIST\]

The Patient Discharge List produces a report of patients eligible to be discharged. The report is output separately for each affected institution. As shown below, the user can filter the report for a single institution or include all of them and then can sort the report either by ward or by patient. The patient’s transfer history can optionally be included as well.

Select Patient Discharge Menu \<TEST ACCOUNT\> Option: <span class="mark">LIST</span> Patient Discharge List

Select one of the following:

A All

S Selected

Institutions: All// <span class="mark">ALL</span>

Select one of the following:

WARD Ward

PATIENT Patient

Sort by: <span class="mark">WARD</span>

Include transfer history? NO// <span class="mark">YES</span>

Report is 160 columns wide

DEVICE: HOME// <span class="mark">;160</span> HOME(CRT)

Sorting patients within ward...............

Sample output of both sorts is shown below. First, sorted by ward including transfer history:

Patient Discharge List - CLEVELAND VAMC (541) 7/30/24

WARD PATIENT ADMIT DATE/TIME ROOM/BED DIAGNOSIS ATTENDING PROVIDER

------------------------------ ------------------------------ --------------- -------- ------------------------------ ------------------------------

W4A BBBBOUR,CCCCOLL 05/17/20 18:51 4A144-1 Pancytopenia HHHHELL,EEEEN

ADMISSION 05/17/20 18:51 W4A Pancytopenia

BBBBA,OOOO LOU 05/14/20 16:54 4A155-1 CELLULITIS LLLLZ,RRRRE

ADMISSION 05/14/20 16:54 W4A CELLULITIS

BBBB,CCCCOLL C 05/18/20 16:29 4A127-1 ALCOHOL WITHDRAWAL LLLLZ,RRRRE

ADMISSION 05/18/20 16:29 W4A ALCOHOL WITHDRAWAL

BBBBS,GGGGAVO DONALD 05/08/20 15:12 4A153-2 FOURNIERS GANGRENE HHHHHERLY,GGGGAVO M

ADMISSION 05/08/20 15:12 WSIC FOURNIERS GANGRENE

TRANSFER 05/18/20 14:55 W4A FOURNIERS GANGRENE

Next, sorted by patient without transfer history:

Patient Discharge List - CLEVELAND VAMC (541) 7/30/24

PATIENT WARD ADMIT DATE/TIME ROOM/BED DIAGNOSIS ATTENDING PROVIDER

------------------------------ ------------------------------ --------------- -------- ------------------------------ ------------------------------

AAAAWER,CCCCK J WSCIR 04/28/20 15:24 6B100-1 CERVICAL MYELOPATHY BBBBON,AAAAINE

AAALONI,BBBBNT MICHAEL WCT6 05/15/20 00:22 6F139-1 SUICIDAL IDEATION WWWWCH,TTTTOR P

BBBBOUR,CCCCOLL W4A 05/17/20 18:51 4A144-1 Pancytopenia HHHHELL,EEEEN

#### Discharged Patients List \[EHM_DISCHARGE POST-LIST\]

The Discharged Patients List produces a report of the patients automatically discharged by the Tool. User interaction, such as it is, is shown below.

Select Patient Discharge Menu \<TEST ACCOUNT\> Option: <span class="mark">POST</span> Discharged Patients List

Report is 80 columns wide

DEVICE: HOME// <span class="mark">\<RET\></span> HOME(CRT)

Sample report output is shown below.

Patients Discharged at Conversion 10/17/24

Patient Name Date/Time Discharged

------------------------------ --------------------

AAAAAAA,SSSS 07/17/24 10:32

AAAAAA,TTTTTT R 07/17/24 10:29

AAAA,RRRRRR 07/17/24 10:32

#### Patient Discharge Summary \[EHM_DISCHARGE SUMMARY\]

The Patient Discharge Summary produces counts of patients eligible to be discharged by affected institution and then ward. User interaction, such as it is, is shown below.

Select Patient Discharge Menu \<TEST ACCOUNT\> Option: <span class="mark">SUMM</span> Patient Discharge Summary

DEVICE: HOME// <span class="mark">\<RET\></span> HOME(CRT)

Sorting patients within ward......................

Sample report output is shown below.

Patient Discharge Summary 7/12/24

INSTITUTION WARD COUNT

---------------------------------------- ------------------------------ ------

CLEVELAND COMM LIVING CENTER (5419AA) WCT3 22

WCT4 23

WCT5 23

WPHOSP 7

------------------------------ ------

TOTAL 75

CLEVELAND DOMICILIARY (541BU) DOM21 10

DOM31 6

------------------------------ ------

TOTAL 16

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| TERM | MEANING                                                      |
|----------|------------------------------------------------------------------|
| API      | Application Programming Interface                                |
| CD2      | Critical Decision Point \#2                                      |
| DICOM    | Digital Imaging and Communications in Medicine                   |
| EDIPI    | Electronic Data Interchange Personal Identifier                  |
| EHM      | Electronic Health Modernization                                  |
| EHRM-IO  | Electronic Health Record Modernization Integration Office        |
| ESD      | Enterprise Service Desk                                          |
| HITT     | Health Informatics Transition Team                               |
| HL7      | Health Level Seven                                               |
| IFC      | Inter-Facility Consult                                           |
| IV&V     | Independent Validation and Verification                          |
| OIT      | Office of Information and Technology                             |
| PII      | Personal Identifiable Information                                |
| PRF      | Patient Record Flag                                              |
| SFTP     | Secure File Transfer Protocol                                    |
| SOP      | Service Object Pair                                              |
| VA       | Department of Veterans Affairs                                   |
| VAMC     | VA Medical Center                                                |
| VDL      | VA Software Documentation Library                                |
| VIP      | Veteran-focused Integrated Process                               |
| VistA    | Veterans Health Information Systems and Technology Architecture. |

[^1]: A feature in version 5 of the patch, if enabled, will automatically forward these messages to a team member’s BACKUP mailbox if he/she has one set up. See Section 2.2.5.2 to enable this feature.