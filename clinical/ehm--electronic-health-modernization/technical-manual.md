---
title: Electronic Health Modernization Technical Manual
doc_type: TM
doc_label: Technical Manual
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
file_numbers: 
  - 1606
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - patch
  - report
  - options
  - security
  - appointments
  - date
  - patient
  - subroutine
page_count: 0
word_count: 16959
section_count: 22
table_count: 37
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2026
revision_count: 16
revision_newest: 06/04/2025
revision_oldest: 01/11/2023
docx_url: "https://www.va.gov/vdl/documents/Clinical/Electronic_Health_Modernization_(EHM)/ehm_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Electronic_Health_Modernization_(EHM)/ehm_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=439"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Electronic Health Modernization (EHM)

  Technical Manual
---

![](electronic-health-modernization-technical-manual/001.png)

March 2026

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date       | Revision | Description                                                    | Author  |
|------------|----------|----------------------------------------------------------------|---------|
| 06/04/2025 | 16       | Tweaks for EHM\*1\*13                                          | EHRM-IO |
| 01/23/2025 | 15       | Tweaks for EHM\*1\*13                                          | EHRM-IO |
| 12/10/2024 | 14       | Tweaks for EHM\*1\*13                                          | EHRM-IO |
| 07/30/2024 | 13       | Added EHM\*1\*15                                               | EHRM-IO |
| 07/03/2024 | 12       | Revisions for GMRC\*3\*192                                     | EHRM-IO |
| 05/31/2024 | 11       | Revisions for EHM\*1\*13                                       | EHRM-IO |
| 4/25/24    | 10       | Updated for EHM\*1\*8                                          | EHRM-IO |
| 04/22/2024 | 9        | Updated for EHM\*1\*13.                                        | EHRM-IO |
| 04/08/2024 | 8        | Updated for changes made in EHM\*1\*14v2.                      | EHRM-IO |
| 01/26/2024 | 7        | Added more tools documentation.                                | EHRM-IO |
| 01/25/2024 | 6        | Updated EHM\*1\*9v1. Added EHM\*1\*14v1.                       | EHRM-IO |
| 08/03/2023 | 5        | Updated for EHM\*1\*4v5                                        | EHRM-IO |
| 06/28/2023 | 4        | Updated for routine, file and file and field comparison tools. | EHRM-IO |
| 06/14/2023 | 3        | Updated for patch EHM\*1\*10                                   | EHRM-IO |
| 02/02/2023 | 2        | Added tools documentation                                      | EHRM-IO |
| 01/11/2023 | 1        | Initial technical manual                                       | EHRM-IO |

<span id="_Ref123892259" class="anchor"></span>Table 1: EHM Patches

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [System Overview](#system-overview)
  - [Document Orientation](#document-orientation)
    - [Disclaimers](#disclaimers)
  - [Implementation and Maintenance](#implementation-and-maintenance)
    - [System Requirements](#system-requirements)
- [# Patches](#patches)
  - [EHM\1\2 – Image Migration](#ehm12-image-migration)
    - [Files](#files)
    - [Routines](#routines)
    - [Options](#options)
    - [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
    - [Public Interfaces](#public-interfaces)
    - [Software-wide Variables](#software-wide-variables)
    - [Security](#security)
  - [EHM\1\4 – Automated VistA Patching Tool](#ehm14-automated-vista-patching-tool)
    - [Files](#files-1)
    - [Routines](#routines-1)
    - [Options](#options-1)
    - [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins-1)
    - [Public Interfaces](#public-interfaces-1)
    - [Software-wide Variables](#software-wide-variables-1)
    - [Security](#security-1)
  - [EHM\1\8 – EHRM-IO Clinical Cutover Tools](#ehm18-ehrm-io-clinical-cutover-tools)
    - [Files](#files-2)
    - [Routines](#routines-2)
    - [Options](#options-2)
    - [Templates](#templates)
    - [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins-2)
    - [Public Interfaces](#public-interfaces-2)
    - [Software-wide Variables](#software-wide-variables-2)
    - [Security](#security-2)
  - [EHM\1\9 – EHRM-IO Kernel Cutover Tools](#ehm19-ehrm-io-kernel-cutover-tools)
    - [Files](#files-3)
    - [Routines](#routines-3)
    - [Options](#options-3)
    - [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins-3)
    - [Public Interfaces](#public-interfaces-3)
    - [Software-wide Variables](#software-wide-variables-3)
    - [Security](#security-3)
  - [EHM\1\10 – IFC and PRF HL7 Message Storage](#ehm110-ifc-and-prf-hl7-message-storage)
    - [Files](#files-4)
    - [Routines](#routines-4)
    - [Options](#options-4)
    - [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins-4)
    - [Public Interfaces](#public-interfaces-4)
    - [Standards and Conventions Exemptions](#standards-and-conventions-exemptions)
    - [Security](#security-4)
  - [EHM\1\13 – Converted Appointment Maintenance](#ehm113-converted-appointment-maintenance)
    - [Files](#files-5)
    - [Routines](#routines-5)
    - [Options](#options-5)
    - [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins-5)
    - [Public Interfaces](#public-interfaces-5)
    - [Software-wide Variables](#software-wide-variables-4)
    - [Security](#security-5)
  - [EHM\1\14 – HITT Menu](#ehm114-hitt-menu)
    - [Files](#files-6)
    - [Routines](#routines-6)
    - [Options](#options-6)
    - [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins-6)
    - [Public Interfaces](#public-interfaces-6)
    - [Software-wide Variables](#software-wide-variables-5)
    - [Security](#security-6)
  - [GMRC\3\192 – EHRM-IO CONSULT CUTOVER TOOLS](#gmrc3192-ehrm-io-consult-cutover-tools)
    - [Files](#files-7)
    - [Routines](#routines-7)
    - [Options](#options-7)
    - [### Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins-7)
    - [Public Interfaces](#public-interfaces-7)
    - [Software-wide Variables](#software-wide-variables-6)
    - [Security](#security-7)
  - [EHM\1\15 – Automated Patient Discharge Tool](#ehm115-automated-patient-discharge-tool)
    - [Files](#files-8)
    - [Routines](#routines-8)
    - [Options](#options-8)
    - [Templates](#templates-1)
    - [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins-8)
    - [Public Interfaces](#public-interfaces-8)
    - [Software-wide Variables](#software-wide-variables-7)
    - [Security](#security-8)
- [Tools](#tools)
  - [Routine Comparison](#routine-comparison)
  - [FileMan File Comparison](#fileman-file-comparison)
  - [FileMan File and Field Comparison](#fileman-file-and-field-comparison)
  - [Routine Print](#routine-print)
  - [File Entry Print](#file-entry-print)
  - [^DD Lister](#dd-lister)
  - [Global Search](#global-search)
  - [Released Patch Comparison](#released-patch-comparison)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
Electronic Health Modernization (EHM) VistA patches and software tools support the Electronic Health Record Modernization Integration Office (EHRM-IO) during conversion from Veterans Health Information Systems and Technology Architecture (VISTA) to Cerner Millennium.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Technical Manual provides information about EHM Package software for developers and technical personnel.

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHM patches and software tools have no single system orientation. Patches (see Table 1)and tools (see Table 2) support the conversion process rather than any single system.

| Patch    | Description                        |
|--------------|----------------------------------------|
| EHM\*1\*2    | Image Migration                        |
| EHM\*1\*4    | Automated VistA Patching               |
| EHM\*1\*8    | EHRM IO CUTOVER TOOLS                  |
| EHM\*1\*9    | EHRM-IO Kernel Cutover Tools           |
| EHM\*1\*10   | IFC and PRF HL7 Message Storage        |
| EHM\*1\*13   | EHRM–Converted Appointment Maintenance |
| EHM\*1\*14   | HITT Menu                              |
| GMRC\*3\*192 | EHRM-IO Consult Cutover Tools          |
| EHM\*1\*15   | Automated Patient Discharge Tool       |

<span id="_Ref123892280" class="anchor"></span>Table 2: EHM Software Tools

| Tool           | Description                                                   |
|--------------------|-------------------------------------------------------------------|
| CHECKSUMS^EHMUTILS | List routines with checksums                                      |
| FILELIST^EHMUTILS  | List FileMan files                                                |
| FILES^EHMUTILS     | List FileMan files and fields                                     |
| ROUTINE^EHMUTILS   | Routine print for text files                                      |
| FILENTRY^EHMUTILS  | File entry print for text files                                   |
| DDLIST^EHMUTILS    | List ^DD for a file                                               |
| GSEARCH^EHMUTILS   | Global search                                                     |
| PATCHES2^EHMUTILS  | Compare list of released patches from CATS to INSTALL file (#9.7) |
|                    |                                                                   |

<span id="_Ref120778356" class="anchor"></span>Table 19: EHM\*1\*9 Security Keys

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audience for this document is developers and technical personnel who support EHM patches or use EHM tools.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections detail Department of Veterans Affairs (VA) software and document disclaimers.

#### Software Disclaimer

This software was developed at the VA by employees of the Federal Government in the course of their official duties. Pursuant to Title 17 Section 105 of the United States Code, this software is not subject to copyright protection and is in the public domain. The VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. The VA would appreciate acknowledgement if the software were used. This software can be redistributed and/or modified freely, provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the VA of this website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

## Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections provide details regarding the implementation and maintenance of EHM patches.

### System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Hardware Requirements

Standard VistA environment.

#### Software Requirements

Standard VistA environment.

#### Database Requirements

Standard VistA environment.

# # Patches

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

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 3 lists the file names and numbers used by Image Migration software.

<span id="_Ref123898365" class="anchor"></span>Table 3: EHM\*1\*2 File Names and Numbers

<table>
<caption><p><span id="_Ref164667535" class="anchor"></span>Table 24: EHM*1*13 Files</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 20%" />
<col style="width: 16%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th>FILE NUMBER</th>
<th>FILE NAME</th>
<th>GLOBAL</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1606</td>
<td>Image Migration</td>
<td>^EHMACCN</td>
<td><p>File #1606 is the repository for all image associated VistA entities. Its purpose is to ensure that all Digital Imaging and Communications in Medicine (DICOM) images are migrated from VistA to Cerner. It does so by creating a unique accession number for all Radiology reports (#74) and consults (#123) and by storing attributes of the image sets (parent</p>
<p>images or studies) associated with each of these.</p></td>
</tr>
<tr class="even">
<td>1606.5</td>
<td>Image Migration Exception</td>
<td>^EHMEXCP</td>
<td>This file stores a record of all Image Migration file (#1606) entries that failed validation during the extraction report process.</td>
</tr>
</tbody>
</table>

<span id="_Ref164667535" class="anchor"></span>Table 24: EHM\*1\*13 Files

#### Image Migration (#1606)

The Image Migration file is the central repository linking image associating entities (Consults and Radiology Reports) with image sets (parent images for old Service Object Pair (SOP) images and studies for new SOP images). Consults and Radiology Reports are the unifying entities for the file because they are ultimately where images and results/reports are displayed to providers. Each record is “for” either a Consult or a Radiology Report. If the former, the CONSULT field (#2) is populated and the RADIOLOGY REPORT field (#5) is not. If the latter, field \#5 is populated and \#2 is not. The SITE field (#.5) exists because the Image Migration solution is enterprise-wide when images and reports are migrated to Cerner Millennium. SITE is populated using the ORDERING FACILITY (#.05) field of the REQUEST/CONSULTATION file (#123) or the HOSPITAL DIVISION (#3) field of the REGISTERED EXAMS (#2) multiple of the RAD/NUC MED PATIENT (#70) file. In either case, the extracted site is converted to the VistA site if the extracted site is not a VAMC. The latter determination is made by examining the FACILITY TYPE (#13) field of the INSTITUTION (#4) file. The MIGRATED field (#6) is used by the extraction process to prevent duplicate records from being produced.

The RADIOLOGY OTHER CASE NUMBER multiple (field \#5.2) is populated so that other case numbers can be reported on the extract report. The other case numbers are needed by the image migration process because image UIDs on the DICOM servers are constructed using the other case numbers. These image Unique Identifiers (UIDs) are different from the identifiers stored in the Image file (#2005) for the same images.

The Picture Archiving and Communication Systems (PACS) UID multiple implements the one-to-many relationship between Consults/Radiology Reports and their image sets. For old SOP images, this one-to-many relationship manifests in the IMAGE multiple (field \#2005) in the RAD/NUC MED REPORTS file (#74) and in the combination of the TIU RESULT NARRATIVE (field \#16) and the ASSOCIATED RESULTS multiple (field \#50) in the REQUEST/CONSULTATION file (#123). For new SOP images, the one-to-many relationship results because image studies refer back to Consults and Radiology Reports through a combination of the PROCEDURE TYPE field (#.03) in the IMAGE PROCEDURE REFERENCE file (#2005.61) and the ACCESSION NUMBER field (#.02) of the IMAGE STUDY file (#2005.62). The SOURCE field (#1) characterizes the image set as old or new SOP.

The MODALITY field (#2) can be a comma-delimited list because some image sets employ more than one modality. The NUMBER OF IMAGES (field \#3) is the sum of all images in the image sets that share the same PACS UID. The DICOM GMRC TEMP LIST field (#6) is populated if at least one of the old SOP images sets for the PACS UID was found in file \#2006.5839. IMAGE STUDY (field \#7) identifies the PACS UID as a new SOP study instance UID.

The TIU NOTE multiple (field \#10) within the PACS UID multiple implements the one-to-many relationship that may exist for old SOP image sets tied to a PACS UID for a Consult. The one-to-many relationship manifests when two (or more) image sets share a single PACS UID and when each image set points to a separate TIU Note (file \#8925). Such can occur if a Consult has a primary TIU note (from the TIU RESULT NARRATIVE field (#16)) with images and associated results with TIU notes and images.

The IMAGE multiple (field \#20) within the PACS UID multiple implements the one-to-many relationship that may exist for old SOP image sets tied to a PACS UID for either a Consult or a Radiology Report. This manifests when two or more parent images share the same PACS UID.

The ACTION multiple (field \#10) records a history of changes made to an Image Migration record.

CONDENSED DATA DICTIONARY---Image Migration FILE (#1606)UCI: CLE623,ROU

STORED IN: ^EHMACCN( AUG 20,2021 PAGE 1

---------------------------------------------------------------------------

CROSS REFERENCED BY:

EXAM DATE/TIME(AEXAMDTTM) CONSULT(CONSULT) RADIOLOGY REPORT(RADRPT)

FILE \#1606

INDEXED BY: ACCESSION NUMBER (B), PACS UID (STUDYUID)

SUBFILE \#1606.07

INDEXED BY: PACS UID (B)

FILE STRUCTURE

FIELD FIELD

NUMBER NAME

.01 ACCESSION NUMBER (RFJ16), \[0;1\]

.5 SITE (P4'), \[0;6\]

1 CREATED (D), \[0;2\]

2 CONSULT (P123'), \[0;3\]

2.01 CONSULT SERVICE (CJ), \[ ; \]

2.02 CONSULT PROCEDURE (CJ), \[ ; \]

2.03 CONSULT CLINICAL PROCEDURE (CJ), \[ ; \]

2.04 CONSULT PATIENT (CJ30), \[ ; \]

2.05 CONSULT REQUEST DATE (CD), \[ ; \]

5 RADIOLOGY REPORT (P74'), \[0;7\]

5.01 RADIOLOGY PATIENT (CJ30), \[ ; \]

5.02 RADIOLOGY PROCEDURE (CJ30), \[ ; \]

5.03 RADIOLOGY SERVICE (CJ), \[ ; \]

5.04 RADIOLOGY EXAM DATE (CD), \[ ; \]

5.05 RADIOLOGY CASE NUMBER (CJ30), \[ ; \]

5.06 RADIOLOGY STATUS (CJ30), \[ ; \]

5.1 RADIOLOGY REPORT HAS IMAGES (S), \[0;11\]

5.2 RADIOLOGY OTHER CASE NUMBER (Multiple-1606.02), \[3;0\]

.01 RADIOLOGY OTHER CASE NUMBER (FJ20), \[0;1\]

6 MIGRATED (D), \[0;8\]

7 PACS UID (Multiple-1606.07), \[2;0\]

.01 PACS UID (FJ70), \[0;1\]

1 SOURCE (S), \[0;2\]

2 MODALITY (FJ100), \[0;3\]

3 NUMBER OF IMAGES (NJ9,0), \[0;4\]

4 EXAM DATE/TIME (D), \[0;5\]

6 DICOM GMRC TEMP LIST (P2006.5839'), \[0;7\]

7 IMAGE STUDY (P2005.62'), \[0;8\]

10 TIU NOTE (Multiple-1606.08), \[1;0\]

.01 TIU NOTE (P8925'), \[0;1\]

20 IMAGE (Multiple-1606.09), \[2;0\]

.01 IMAGE (P2005'), \[0;1\]

10 ACTION (Multiple-1606.01), \[1;0\]

.01 ACTION DATE/TIME (D), \[0;1\]

1 ACTION (S), \[0;2\]

2 PERFORMED BY (P200'), \[0;3\]

#### Image Migration Exception (#1606.5)

The Image Migration Exception file is a repository for records that failed data validation during the extraction process. The three fields store the date/time when the exception occurred, a pointer to the offending Image Migration file record and the reason for the exception.

CONDENSED DATA DICTIONARY---Image Migration Exception FILE (#1606.5)UCI: CLE623,ROU

STORED IN: ^EHMEXCP( MAY 24,2021 PAGE 1

---------------------------------------------------------------------------

CROSS REFERENCED BY:

EXCEPTION DATE/TIME(B)

FILE STRUCTURE

FIELD FIELD

NUMBER NAME

.01 EXCEPTION DATE/TIME (RD), \[0;1\]

1 IMAGE MIGRATION (P1606'), \[0;2\]

2 EXCEPTION REASON (S), \[0;3\]

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 4 lists the routines associated with Image Migration software and their descriptions.

<span id="_Ref123898346" class="anchor"></span>Table 4: EHM\*1\*2 Routines

| ROUTINE NAME | ROUTINE DESCRIPTION                                                                                                                                                                                                                                        |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EHMACCN      | Code to populate the Image Migration database. Code to build the Consult baseline. Functions to create consult and Radiology records.                                                                                                                      |
| EHMACCN1     | Code to populate the Image Migration database. Code to build the Radiology Report baseline as well as to load data from file \#2006.5839 and the new SOP files.                                                                                            |
| EHMANLZ1     | New SOP Image v. Image Migration file analyzer code.                                                                                                                                                                                                       |
| EHMANLZR     | Old SOP Image v. Image Migration file analyzer code.                                                                                                                                                                                                       |
| EHMEXCP      | Code to display extraction exceptions.                                                                                                                                                                                                                     |
| EHMIMGRP     | Code to produce the extraction reports.                                                                                                                                                                                                                    |
| EHMRSLT      | Real-time maintenance code that is executed by the protocols associated with Radiology and Consult resulting.                                                                                                                                              |
| EHMUTIL      | External APIs to return accession numbers for Consults and Radiology Reports. Functions to set or reset the migrated date and to return the Electronic Data Interchange Personal Identifier (EDIPI) for a patient. Function to translate an ordering site. |

<span id="_Ref164848638" class="anchor"></span>Table 27: EHM\*1\*13 Security Keys

#### EHMACCN

ACTION – function to add an action to a record in file \#1606.

ADDIMAGE – function to add an image to a record in file \#1606.

ADDPACS – function to add or edit a PACS or Study Instance UID to a record in file \#1606.

ADDTNOTE – function to add a TIU note to a record in file \#1606.

CONSULT – function to add or edit a Consult record in file \#1606.

INTERVAL – function to calculate the number of record interval for progress reporting.

LOAD1A – subroutine to add all images associated with a Consult.

LOAD1ALL – entry point to run the baseline load for Consults.

PROGRESS – subroutine to output percent complete to the screen.

RADIOLOG – function to add or edit a Radiology report record in file \#1606.

> **NOTE:** LOAD1ALL scans the REQUEST/CONSULTATION file (#123) in reverse order to reduce the chance of overlap with the real-time maintenance code (EHMRSLT) should results be posted while the baseline load is in process. LOAD2ALL scans the RAD/NUC MED REPPORTS file (#74) file in reverse order under the same rationale.

#### EHMACCN1

LOAD5839 – entry point to run the baseline load for the DICOM GMRC TEMP file (#2006.5839).

LODSTUDY – entry point to run the baseline load for new SOP image files.

LOAD2A – subroutine to add all images associated with a Radiology Report.

LOAD2ALL – entry point to run the baseline load for Radiology Reports.

#### EHMANLZ1

NEWSOP – entry point to run the image v. image migration analyzer for new SOP images.

#### EHMANLZR

OLDSOP – entry point to run the image v. image migration analyzer for old SOP images.

#### EHMEXCP

DATES – subroutine to display available dates in the Image Migration Exception file (#1606.5).

REPORT – entry point to output the exception report.

#### EHMIMGRP

CONSULTS – subroutine to generate an extraction report for Consults without a date range.

EXAMDATE – subroutine to generate an extraction report for a date range.

RADRPT – subroutine to generate an extraction report for Radiology Reports without a date range.

RECOUT – function to generate extraction record or records for an Image Migration file entry.

SELECT – entry point to generate an extraction report.

#### EHMRSLT

CONSULT – entry point for processing an HL7 result message for a Consult.

RADRPT – entry point for processing an HL7 result message for a Radiology Report.

> **NOTE:** Code was added in v15 to RADRPT and RADRPT1 to handle the situation where an earlier protocol kills the HL array. “Earlier” means a protocol in the RARPT 2.3 event driver list that is executed before the EHM RADRPT protocol.

#### EHMUTIL

CONSACCN – function to return an accession number for a Consult in the Image Migration file.

EDIPI – function that outputs a Veteran’s EDIPI or EDIPIs.

MIGRATED – function to set or reset the migration date/time for a record in file \#1606.

PARENT – function that transforms an ordering site to the appropriate division of its parent VistA site.

RADACCN – function to return an accession number for a Radiology Report in the Image Migration file.

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 5 lists Image Migration options and their descriptions.

<span id="_Ref123898324" class="anchor"></span>Table 5: EHM\*1\*2 Options

| OPTION NAME     | DESCRIPTION                                  |
|---------------------|--------------------------------------------------|
| EHM IMAGING MENU    | Image Migration Options menu                     |
| EHM_EHMANLZR-STATS  | Analyze Image Migration records by site and date |
| EHM_EHMANLZR-NEWSOP | Analyze New SOP Images v. Image Migration file   |
| EHM_EHMANLZR-OLDSOP | Analyze Old SOP Images v. Image Migration file   |
| EHM_EHMEXCP         | Generate Image Migration Exception Report        |
| EHM_EHMIMGRP        | Generate image migration extract file            |
| EHM_LOAD1ALL        | Load consults into Image Migration file          |
| EHM_LOAD2ALL        | Load Radiology Reports into Image Migration file |
| EHM_LOAD5839        | Load file \#2006.5839 in Image Migration file    |
| EHM_LODSTUDY        | Load Image Studies into Image Migration file     |

<span id="_Ref157068420" class="anchor"></span>Table 30: EHM\*1\*14 Security Keys

### Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 6 describes the mail groups and their descriptions.

<span id="_Ref123898308" class="anchor"></span>Table 6: EHM\*1\*2 Mail Group and Descriptions

| MAIL GROUP   | DESCRIPTION                                                |
|--------------|------------------------------------------------------------|
| EHM_ANALYZER | Mail group where results of the analyzer options are sent. |

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

### Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integration Control Registrations (ICR)

N/A

#### Application Programming Interfaces

N/A

#### Remote Procedure Calls

N/A

#### HL7 Messaging

N/A

#### Web Services

N/A

### Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VistA users are required to observe VA rules of behavior regarding patient privacy and the security of patient information, VA computers, and VA networks.

#### Security Menus and Options

N/A

#### Security Keys and Roles

N/A

#### File Security

Table 7 details file security.

<span id="_Ref124152066" class="anchor"></span>Table 7: EHM\*1\*2 File Security

|                 |            |          |           |           |                     |            |
|-----------------|------------|----------|-----------|-----------|---------------------|------------|
| FILE NUMBER | GLOBAL | READ | WRITE | LAYGO | DATA DICTIONARY | DELETE |
| 1606            | ^EHMACCN   | @        | @         | @         | @                   | @          |
| 1606.5          | ^EHMEXCP   | @        | @         | @         | @                   | @          |

## EHM\*1\*4 – Automated VistA Patching Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the Automated VistA Patching Tool is to automate, to the extent possible, the process of loading and installing patches in VistA test environments maintained by Independent Verification and Validation (IV&V) system administrators.

As shown in Error! Reference source not found. below, the Automated VistA Patching Tool receives VistA patches from Forum and analyzes them for suitability for auto-load and auto-install. If a patch can be automatically loaded, the Tool loads and backs it up. The Tool then determines if the patch can be automatically installed, and, if so, installs it. If the patch is not eligible for automatic loading and installing, its parent mail message is forwarded to the local instance installation team for manual processing. If the patch is eligible for automatic loading but not automatic installation, a new mail message is created with the patch description that is sent to the local installation team for manual processing. The Tool builds and maintains a database of patches it has processed including those not automatically loaded and/or installed. It also provides tools to list the contents of the patch database.

<span id="_Ref181693899" class="anchor"></span>Figure 1: Automated VistA Patching - Process Flow

![](electronic-health-modernization-technical-manual/002.png)

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 8 lists the file names and numbers used by the Automated VistA Patching Tool.

<span id="_Ref124154232" class="anchor"></span>Table 8: EHM\*1\*4 File Names and Numbers

| FILE NUMBER | FILE NAME                             | GLOBAL    | DESCRIPTION                                                                                                                                                                                                                             |
|-------------|---------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1607        | EHM Patch                             | ^EHMPATCH | File \#1607 is the repository for all VistA patches received by the Automated VistA Patching Tool. Its purpose is to record information about patches including when they were automatically loaded and installed or why they were not. |
| 1608        | EHM Automatic Patching Tool Parameter | ^EHMTOOL  | File \#1608 stores control data used by the Tool.                                                                                                                                                                                       |

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

#### EHM Patch (#1607)

The EHM Patch file is the central repository of patches received and processed by the Automated VistA Patching Tool. A record in the file stores data about the patch and its installation status.

CONDENSED DATA DICTIONARY---EHM Patch FILE (#1607)UCI: CLE623,ROU VERSION: 1.0

STORED IN: ^EHMPATCH( FEB 25,2022 PAGE 1

---------------------------------------------------------------------------

CROSS REFERENCED BY:

PATCH(B) DATE PROCESSED(C) LOADED(LOADED)

FILE STRUCTURE

FIELD FIELD

NUMBER NAME

.01 PATCH (RFJ30), \[0;1\]

1 LOAD TYPE (S), \[0;2\]

1.01 PACKAGE TYPE (S), \[0;8\]

1.02 STATUS (S), \[0;7\]

1.03 DATE PROCESSED (D), \[0;9\]

1.04 PATCH TYPE (S), \[0;10\]

1.05 MAILMAN MESSAGE (P3.9'), \[0;6\]

1.06 PATCH VERSION (FJ30), \[0;11\]

1.1 HOST FILE NAME (FJ250), \[1;1\]

1.2 PARENT PATCH (FJ20), \[0;5\]

1.21 PATCH LIST (FJ250), \[4;E1,250\]

1.3 AUTO-LOAD FAILURE REASON (Multiple-1607.01), \[5;0\]

.01 AUTO-LOAD FAILURE REASON (Wx), \[0;1\]

2 LOADED (D), \[0;3\]

3 INSTALLED (D), \[0;4\]

4 LOAD ERROR (FJ250), \[2;1\]

5 INSTALL ERROR (FJ250), \[3;1\]

10 PRE-INSTALLATION INSTRUCTIONS (Multiple-1607.1), \[10;0\]

.01 PRE-INSTALLATION INSTRUCTIONS (Wx), \[0;1\]

20 POST-INSTALLATION INSTRUCTIONS (Multiple-1607.2), \[20;0\]

.01 POST-INSTALLATION INSTRUCTIONS (Wx), \[0;1\]

30 ACTION (Multiple-1607.02), \[21;0\]

.01 ACTION (FJ50), \[0;1\]

1 DATE/TIME (D), \[0;2\]

2 PERFORMED BY (P200'), \[0;3\]

#### EHM Automatic Patching Tool Parameter (#1608)

The EHM Automatic Patching Tool Parameter file stores control data used by the Tool’s routines.

CONDENSED DATA DICTIONARY---EHM Automatic Patching Tool Parameter FILE (#1608)UCI: CLE623,ROU VERSION: 1.0

STORED IN: ^EHMTOOL( AUG 3,2023 PAGE 1

---------------------------------------------------------------------------

FILE SECURITY

DD SECURITY : @ DELETE SECURITY: @

READ SECURITY : @ LAYGO SECURITY : @

WRITE SECURITY : @

CROSS REFERENCED BY:

DOMAIN(B)

FILE STRUCTURE

FIELD FIELD

NUMBER NAME

.01 DOMAIN (RP4.2'), \[0;1\]

1 HOST FILE PATH NOMINAL (FJ250), \[1;1\]

2 HOST FILE PATCH ACTUAL (FJ250), \[2;1\]

3 VOCCB RESTRICTED (S), \[0;2\]

4 OWNER (P200'), \[0;3\]

5 BACKUP PATCH MESSAGE ACTION (S), \[0;4\]

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 9 lists the routines associated with the Automated VistA Patching Tool and their descriptions. The majority of the routines that make up the Automated VistA Patching Tool are clones of existing VistA routines that perform patch loading, backup, and installation. Where necessary, user interaction was suppressed so the routines can be run in the background. The new routines that were created manage automated loading and installation, analyze patch messages, and report the status of patches processed through the Tool.

<span id="_Ref124157756" class="anchor"></span>Table 9: EHM\*1\*4 Routines

| ROUTINE NAME | ROUTINE DESCRIPTION                                                                                                                                         |
|--------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EHM004P      | Post-install routine for EHM\*1\*4.                                                                                                                         |
| EHMDI        | Clone of XPDI. Install process. User interaction suppressed.                                                                                                |
| EHMDI1       | Clone of XPDI1. Install process. User interaction suppressed.                                                                                               |
| EHMDIB       | Clone of XPDIB. Backup installed package. User interaction suppressed.                                                                                      |
| EHMDIGP      | Clone of XPDIGP. Load global distribution. User interaction suppressed.                                                                                     |
| EHMDIJ1      | Clone of XPDIJ1. Install job. User interaction suppressed.                                                                                                  |
| EHMDIL       | Clone of XPDIL. Load distribution global. User interaction suppressed.                                                                                      |
| EHMDIL1      | Clone of XPDIL1. Load distribution global. User interaction suppressed.                                                                                     |
| EHMDIQ       | Clone of XPDIQ. Install questions. User interaction suppressed.                                                                                             |
| EHMDIST      | Clone of XPDIST. Site tracking. User interaction suppressed.                                                                                                |
| EHMDTP       | Clone of XPDTP. Send backup message. User interaction suppressed.                                                                                           |
| EHMDUTL      | Clone of XPDUTL. KIDS utilities. User interaction suppressed.                                                                                               |
| EHMP2        | Clone of XMP2. Load patch. User interaction suppressed.                                                                                                     |
| EHMP2A       | Clone of XMP2A. Load patch. User interaction suppressed.                                                                                                    |
| EHMP3        | Clone of XMP3. Build backup. User interaction suppressed.                                                                                                   |
| EHMPATCH     | Generate summary and detail reports of patches plus count by status report.                                                                                 |
| EHMPC        | Clone of XMPC. PackMan compare. User interaction suppressed.                                                                                                |
| EHMPDIK      | Clone of XPDIK. Install Kernel and FM files. User interaction suppressed.                                                                                   |
| EHMPDIP      | Clone of XPDIP. Install package and routines. User interaction suppressed.                                                                                  |
| EHMPDIPM     | Clone of XPDIPM. Load PackMan message. User interaction suppressed.                                                                                         |
| EHMPSEC      | Clone of XMPSEC. PackMan security. User interaction suppressed.                                                                                             |
| EHMPTCH1     | Second half of EHMPTCHZ. Processes host file patches.                                                                                                       |
| EHMPTCHX     | Patch processor. Analyzes, creates record in \#1607, loads, backs up and installs patches. Forwards ineligible patches for manual loading and installation. |
| EHMPTCHZ     | Patch analyzer. Decomposes mail message and extracts patch attributes.                                                                                      |

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

#### EHM004P

EHMOO4P is the post-install routine for EHM\*1\*4. It performs two (2) duties: 1) add or update the parameter file (#1608) entry, and 2) add the server option EHM AUTOMATED PATCH LOAD to the EHMPATCHING mail group.

#### EHMDI

EHMDI is a clone of XPDI with the user interaction suppressed. Errors in the load and/or install process return the variable EHMERROR instead of displaying the reason to the screen.

#### EHMDI1

EHMDI1 is a clone of XPDI1 with the user interaction suppressed.

#### EHMDIB

EHMDIB is a clone of XPDIB with the user interaction suppressed.

In version 5 of EHM\*1\*4, the PM subroutine was enhanced so that backup patches are sent to the installation team’s BACKUP mailbox. PM checks to see if the backup message switch in file \#1608 is enabled and, if so, calls BKUPMSGS.

The BKUPMSGS subroutine scans the members of the EHM AUTOMATED PATCHING mail group and calls MOVEMSG^XMXAPI to move the message from the user’s IN mailbox to his/her BACKUP mailbox. If the user does not have a BACKUP mailbox, the message is left in the IN mailbox.

#### EHMDIGP

EHMDIGP is a clone of XPDIGP with the user interaction suppressed.

#### EHMDIJ1

EHMDIJ1 is a clone of XPDIJ1 with the user interaction suppressed.

#### EHMDIL

EHMDIL is a clone of XPDIL with the user interaction suppressed.

#### EHMDIL1

EHMDIL1 is a clone of XPDIL1 with the user interaction suppressed.

#### EHMDIQ

EHMDIQ is a clone of XPDIQ with the user interaction suppressed.

#### EHMDIST

EHMDIST is a clone of XPDIST with the user interaction suppressed.

#### EHMDTP

EHMDTP is a clone of XPDTP with the user interaction suppressed.

#### EHMDUTL

EHMDUTL is a clone of XPDUTL with the user interaction suppressed.

#### EHMP2

EHMP2 is a clone of XMP2 with the user interaction suppressed.

#### EHMP2A

EHMP2A is a clone of XMP2A with the user interaction suppressed.

#### EHMP3

EHMP3 is a clone of XMP3 with the user interaction suppressed.

#### EHMPATCH

EHMPATCH produces detail and summary reports of patches. Reports cover a user-selected date range and can be filtered by patch status and/or package.

In Version 5, the option to exclude informational patches from the SUMMARY and DETAIL reports was added. That functionality was previously only available in the COUNT report.

In Version 3, the following changes were made:

1.  Summary report was modified so that it can be sorted by patch number or by date processed.
2.  Patch version number was added to the summary and detail report display.
3.  Action details were added to the detail report.

Entry points and functions are:

- SUMMARY – Entry point for EHM_PATCH SUMMARY REPORT option.
- SUMMARY1 – Entry point for summary report produced from TaskMan.
- SUMRYHDR – Summary report header
- DETAIL – Entry point for EHM_PATCH DETAIL REPORT option.
- DETAIL1 – Entry point for detail report produced from TaskMan.
- DETLHDR – Detail report header
- COUNT – Entry point for EHM_PATCH STATUS COUNT option.
- COUNT1 – Entry point for count by status report produced from TaskMan.
- COUNTHDR – Count by status report header
- INSTALL – Entry point for EHM_PATCH INSTALL REPORT option.
- INSTALL1 – Entry point for install report produced from TaskMan.
- INSTLHDR – Install report header.
- LIST – Prepares comma-separated list of values and outputs it.
- DATES – User interaction to select beginning and end dates for a report.
- STATUS – User interaction to select all or selected status values for a report.
- PACKAGES – User interaction to select all or selected packages for a report.
- CENTER – Function that returns a centered text string.
- CONTINUE – User interaction to continue or stop output.
- INSTLSTS – Function that returns patch installation status from the INSTALL file (#9.7).

#### EHMPC

EHMPC is a clone of XMPC with the user interaction suppressed.

#### EHMPDIK

EHMPDIK is a clone of XPDIK with the user interaction suppressed.

#### EHMPDIP

EHMPDIP is a clone of XPDIP with the user interaction suppressed.

#### EHMPDIPM

EHMPDIPM is a clone of XPDIPM with the user interaction suppressed.

#### EHMPSEC

EHMSEC is a clone of XMPSEC with the user interaction suppressed.

#### EHMPTCH1

In version 3 of the patch, due to its size, EHMPTCHZ was split into EHMPTCHZ and EHMPTCH1. Code that processes patches in host files was moved into EHMPTCH1. In addition, host files are required to end in .KID or .KIDS (upper or lower case).

- HOSTFILE – Function reads the patch message from a host file and processes it.

#### EHMPTCHX

EHMPTCHX is the main driver for automatic loading and installation of VistA patches. SERVER^EHMPTCHX is invoked by the EHM AUTOMATED PATCH LOAD server option when a patch is received from Forum by the EHMPATCHING mail group on the test server. The variable XMZ contains a pointer to the patch in the MESSAGE file (#3.9).

The main driver requires that the user under which it runs have programmer access allowing creation of entries in the BUILD (#9.6) and INSTALL (#9.7) files. The post-install routine (EHM004P) stores the DUZ of the user who installs the EHM\*1\*4 patch in the OWNER (#4) field of the parameter file (#1608). Since all installers are required to have programmer access, the Tool can run with that user’s identity and file access codes. Before continuing, the main driver extracts the user’s identity and sets up the DUZ() array via call to DUZ^XUP.

The first step after identity initialization is to call the patch analyzer (ANALYZE^EHMPTCHZ). Based on the analyzer’s output, EHMPTCHX then creates a record in the EHM Patch file (#1607) with a status of PENDING LOAD. Patches that fail analysis are forwarded for manual processing.

The next step is to determine if the patch is eligible for automatic processing.

> **NOTE:** In version 1 of the Tool, the instructions are saved to the EHM Patch file (#1607) in EHMPTCHX but not otherwise processed.

> **NOTE:** In version 1 of the Tool, only patches that are loaded from Packman and which have no environment check routine, no pre-install routine and no post-install routine are eligible. Host file-based patches are ineligible in version 1.

> **NOTE:** In version 2 of the Tool, all patches are auto loaded, whether presented in PackMan or host file format except those that have an environment check routine or which are multi-builds. The restrictions on auto-installing patches that existed in version 1 (e.g., presence of a post-install routine) remain. Informational patches are not auto loaded as they are not VistA patches. Patches auto-loaded but not installed are given a status of LOADED, CANNOT BE AUTO-INSTALLED. A MailMan message is sent to the EHM AUTOMATED PATCHING mail group indicating that the patch has been loaded but needs to be installed. The patch description is included in the body of the MailMan message.

An eligible patch will become ineligible if any required builds are missing or if routine checksums do not match. Secure patches are also ineligible.

The Tool allows multiple versions of a patch to be loaded and installed with the following restrictions:

- A test version cannot over-write a released version.
- An older version (e.g., v.1 or SEQ 123) cannot over-write a newer one (e.g., v.2 or SEQ 124).
- The same patch – type (test or released) and version/sequence – cannot be installed twice.

If the patch has already been installed – same type (test or released) and same version/sequence – its host message is not forwarded to the EHM AUTOMATED PATCHING mail group because no further action is required.

If a patch is determined to be ineligible, EHMPTCHX updates the status of the patch in the EHM Patch file to CANNOT BE AUTO-LOADED/INSTALLED and the ineligibility reason is stored. The patch is then forwarded to the EHM AUTOMATED PATCHING mail group so that it can be manually loaded and installed. Finally, it is removed from the EHMPATCHING mail group’s queue.

If a patch is determined to be eligible, EHMPTCHX loads the patch by calling XI^EHMP2. If an error occurs during loading, the variable EHMERROR is returned. EHMPTCHX changes the status of the patch in file \#1607 to FAILED AUTO-LOAD, the error reason is stored, the patch message is forwarded for manual processing and de-queued.

If the load is successful, the status of the patch in file \#1607 is changed to LOADED. The patch is then backed up by calling EN^EHMDIB. The backup message is sent to the EHM AUTOMATED PATCHING mail group.

In version 2 of the Tool, after the message is backed up, the patch is evaluated to determine if it can be auto installed. The presence of a pre- or post-install routine prevents auto-installation.

The patch is then installed by calling EN^EHMDI. If an error occurs during the installation process, EHMPTCHX changes the status of the patch in file \#1607 to FAILED AUTO-INSTALL, the error reason is stored, the patch message is forwarded for manual processing and de-queued.

If the installation succeeds, the status of the patch in file \#1607 is changed to INSTALLED and the patch message is de-queued.

In Version 3, the following changes were made:

1.  Patch version was added to the “loaded not installed” MailMan message.
2.  Host files must end in “KID” or “KIDS” (upper or lowercase) to be processed.

Entry points and functions are:

- SERVER – main entry point for the EHM AUTOMATED PATCH LOAD server option.
- SAVEPTCH – adds a record to the EHM Patch file (#1607).
- ADDACTN – adds action to the ACTION multiple in file \#1607.
- FORWARD – forwards the patch mail message to the EHM AUTOMATED PATCHING mail group.
- DEQUEUE – removes the patch mail message from the EHM AUTOMATED PATCH LOAD server option’s queue.
- UPDSTS – updates the patch status in file \#1607.
- UPDFIELD – updates a single field in file \#1607.
- FILPATH1 – returns the host file path used in patch descriptions from file \#1608.
- FILPATH2 – returns the host file path where patches are accessible to test systems from file \#1608.
- STRIP – removes quotation marks (“) from a string.
- BLANKS – removes leading blanks from a string.
- FMPATCH – formats a patch.
- SENDMSG – sends a patch loaded but not installed message to the EHM AUTOMATED PATCHING mail group.

#### EHMPTCHZ

EHMPTCHZ hosts the patch analyzer. It scans the mail message in the MESSAGE file (#3.9), decomposes the structured patch and looks for patch characteristics. After validating that the message is for a patch, the analyzer extracts and stores the patch description. For PackMan messages, the analyzer then identifies and extracts data for each of the patch’s sections, e.g., “BLD” or “RTN”.

The analyzer scans the patch description to determine if the patch is informational or is sourced in a host file as well as to extract the pre-installation and post-installation instructions. If the patch’s attributes are stored in a host file, the analyzer opens the host file and reads the patch from it. The analyzer then identifies and extracts data for each of the patch’s sections, e.g., “BLD” or “RTN”.

In version 3 of the patch, due to its size, EHMPTCHZ was split into EHMPTCHZ and EHMPTCH1. Host file processing was removed from EHMPTCHZ and moved to EHMPTCH1. In addition, code was changed to recognize MailMan messages with test patches.

Entry points and functions are:

- ANALYZE – Main entry point for the analyzer.
- DESCRPTN – Extracts and stores the patch description.
- BLD – Extracts and stores the different attributes (e.g., environment check routine, pre-install routine, post-install routine) stored in the “BLD” section. Determines if a patch’s required builds have been installed by checking each build in the INSTALL file (#9.7) on the target system.
- DATA – Extracts attributes from the “DATA” section of the patch.
- FIA – Extracts attributes from the “FIA” section of the patch.
- KRN – Calls PROCESS to extract attributes from the “KRN” section of the patch.
- MBREQ – Calls PROCESS to extract attributes from the “MBREQ” section of the patch.
- ORD – Calls PROCESS to extract attributes from the “ORD” section of the patch.
- PKG – Calls PROCESS to extract attributes from the “PKG” section of the patch.
- QUES – Extracts attributes from the “QUES” section of the patch.
- RTN – Extracts attributes from the “RTN” section of the patch. Calculates the checksum of each routine on the target system and compares it to the expected value stored in the patch message.
- SEC – Calls PROCESS to extract attributes from the “SEC” section of the patch.
- VER – Extracts attributes from the “VER” section of the patch. Compares the Kernel and FileMan versions in the patch with those running on the target system.
- DD – Calls PROCESS to extract attributes from the “^DD” section of the patch.
- DIC – Calls PROCESS to extract attributes from the “^DIC” section of the patch.
- SECTION – Extracts the section name from a line of the patch message.
- PROCESS – Extracts attributes for a section.

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 10 lists Image Migration options and their descriptions.

<span id="_Ref124160472" class="anchor"></span>Table 10: EHM\*1\*4 Options

| OPTION NAME             | DESCRIPTION                                        |
|-----------------------------|--------------------------------------------------------|
| EHM AUTOMATED PATCH LOAD    | Server option that processes a mail message from Forum |
| EHM AUTOMATED PATCHING MENU | Automated Patching Tool menu                           |
| EHM_PATCH DETAIL REPORT     | Print patch detail report                              |
| EHM_PATCH INSTALL REPORT    | Print install report                                   |
| EHM_PATCH STATUS COUNT      | Print count by status report                           |
| EHM_PATCH SUMMARY REPORT    | Print patch summary report                             |

### Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 11 describes the mail groups and their descriptions.

<span id="_Ref124160507" class="anchor"></span>Table 11: EHM\*1\*4 Mail Group and Descriptions

| MAIL GROUP             | DESCRIPTION                                                                                                        |
|------------------------|--------------------------------------------------------------------------------------------------------------------|
| EHM AUTOMATED PATCHING | Mail group with the names of the installers at a site.                                                             |
| EHMPATCHING            | Mail group that receives patch messages from Forum. Its only member is the EHM AUTOMATED PATCH LOAD server option. |

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

### Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integration Control Registrations (ICR)

N/A

#### Application Programming Interfaces

N/A

#### Remote Procedure Calls

N/A

#### HL7 Messaging

N/A

#### Web Services

N/A

### Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EHMERROR is a global variable that is used to pass back to the main driver (EHMPTCHX) error conditions that prevent automatic loading and/or installation of patches. Use of a global variable in this case obviated the need for a major rewrite of the cloned load/install code as functions returning a success/failure flag and error reason.

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VistA users are required to observe VA rules of behavior regarding patient privacy and the security of patient information, VA computers, and VA networks.

#### Security Menus and Options

N/A

#### Security Keys and Roles

N/A

#### File Security

Table 12 details file security for patch EHM\*1\*4.

<span id="_Ref124162159" class="anchor"></span>Table 12: EHM\*1\*4 File Security

|                 |            |          |           |           |                     |            |
|-----------------|------------|----------|-----------|-----------|---------------------|------------|
| FILE NUMBER | GLOBAL | READ | WRITE | LAYGO | DATA DICTIONARY | DELETE |
| 1607            | ^EHMPATCH  | @        | @         | @         | @                   | @          |
| 1608            | ^EHMTOOL   | @        | @         | @         | @                   | @          |

## EHM\*1\*8 – EHRM-IO Clinical Cutover Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch EHM\*1\*8 loads Clinical tools that are used during cutover from VistA to Millennium. The patch is a component of the EHM Package. It is not nationally released.

A representative of the Vista Transition Team (VTT) for outpatient pharmacy prescription data prepares a spreadsheet containing a table of prescription internal entry numbers (RX IEN's)

that have been successfully migrated to Millennium. These RX IEN's are then copy/pasted into a new option - Discontinue RX for EHRM Data Migration \[EHM CANCEL RX\]. This option performs the automatic discontinue/cancel action for each prescription and files a standardized comment text. This ensures that only one active instance of a prescription exists in the

two systems.

New print and sort templates have been created and added to new menu options to create the needed reports and verify all prescriptions have been discontinued.

A new security key named Outpatient Pharmacy RX Cancel \[EHM RX CANCEL\] has been created to access the Pharmacy Discontinue RX \[EHM PHARMACY DISCONTINUE RX\] main menu option. All new options will be under the \[EHM PHARMCY DISCONTINUE RX\] menu option. The EHM PHARMACY DISCONTINUE RX menu option can be found under the EHM MAIN MENU \[EHM MAIN MENU\] option, locked by the EHM MGR security key.

Example of new menus:

Select OPTION NAME: EHM PHARMACY DISCONTINUE RX Pharmacy

Discontinue RX

DIS Discontinue RX for EHRM Data Migration

ACT QA check for Auto-D/C - Active

SUS QA check for Auto-D/C - Suspended

HOLD QA check for Auto-D/C - Hold

CMOP CMOP Temporary Address

IV1 IV Future Clinic Orders

IV2 IV Future Clinic Orders Filtered

UD1 Unit Dose Future Clinic Orders

UD2 Unit Dose Future Clinic Orders Filtered

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 17 lists the routines associated with EHRM-IO TOOLS software and their descriptions.

<span id="_Toc199923295" class="anchor"></span>Table 13: EHM\*1\*8 Routines

| ROUTINE NAME | ROUTINE DESCRIPTION                                                                                           |
|--------------|---------------------------------------------------------------------------------------------------------------|
| EHMPSRXDC    | Code to have user input prescription internal entry numbers (IENS) so they can be automatically discontinued. |

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

#### EHMKEYS

This routine was cloned from PSOCAN3 and modified as an API for EHRM Data Migration. This was created from class II software R1PSCAN3 (Rob Silverman wrote) and converted to class I software. Only subroutine line CAN is the part that was changed in this cloned routine. No other parts were altered as to not break any functions.

CAN is using ‘discontinued prescriptions (RX) due to death’ as API to discontinue RX’s for EHRM. This routine will delete the RX from the RX VERIFY file (#52.4) and the RX SUSPENSE file (#52.5). It will also update the activity record in the PRESCRIPTION file (#52).

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 18 lists EHRM-IO Clinical Cutover Tools options and their descriptions.

<span id="_Toc199923296" class="anchor"></span>Table 14: EHM\*1\*8 Options

| OPTION NAME               | DESCRIPTION                                                                                                            |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| EHM CANCEL RX                 | Discontinue RX for EHM Data Migration                                                                                      |
| EHM PHARMACY DISCONTINUE RX   | Main Menu for all Pharmacy options to discontinue an RX                                                                    |
| EHM QA CHECK - ACTIVE         | Perform a quality assurance check for lingering prescriptions with a status of ACTIVE after Cerner data migration.         |
| EHM QA CHECK – HOLD           | Perform a quality assurance check for lingering prescriptions with a status of HOLD after Cerner data migration.           |
| EHM QA CHECK – SUSPENDED      | Perform a quality assurance check for lingering prescriptions with a status of SUSPENDED after Cerner data migration.      |
| EHM CMOP TEMPORARY ADDRESS    | Tracks the temporary addresses of CMOP patients.                                                                           |
| EHM IV FUTURE CLINIC FILTERED | Report to include both recurring orders that started before go-live date and orders with future start dates for IV.        |
| EHM IV FUTURE CLINIC ORDERS   | Report to include both recurring orders that started before go-live date and orders with future start dates for IV.        |
| EHM UD FUTURE CLINIC FILTERED | Report to include both recurring orders that started before go-live date and orders with future start dates for Unit Dose. |
| EHM UD FUTURE CLINIC ORDERS   | Report to include both recurring orders that started before go-live date and orders with future start dates for Unit Dose. |

### Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 15 lists EHRM-IO Clinical Cutover Tools templates and their descriptions.

<span id="_Toc199923297" class="anchor"></span>Table 15: EHM\*1\*8 Templates

| TEMPLATE NAME             | TYPE | FILE NAME (NUMBER) |
|-------------------------------|----------|------------------------|
| EHM IV FUTURE ACTIVE CLINIC   | SORT     | PHARMACY PATIENT (#55) |
| EHM IV FUTURE ACTIVE FILTERED | SORT     | PHARMACY PATIENT (#55) |
| EHM UD FUTURE ACTIVE CLINIC   | SORT     | PHARMACY PATIENT (#55) |
| EHM UD FUTURE ACTIVE FILTERED | SORT     | PHARMACY PATIENT (#55) |
| EHM IV FUTURE CLINIC ORDERS   | PRNT     | PHARMACY PATIENT (#55) |
| EHM IV FUTURE CLINIC FILTERED | PRINT    | PHARMACY PATIENT (#55) |
| EHM UD FUTURE ACTIVE CLINIC   | PRINT    | PHARMACY PATIENT (#55) |
| EHM UD FUTURE ACTIVE FILTERED | PRINT    | PHARMACY PATIENT (#55) |
| EHM QA CHECK                  | PRINT    | PRESCRIPTION (#52)     |

### Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integration Control Registrations (ICR)

N/A

#### Application Programming Interfaces

N/A

#### Remote Procedure Calls

N/A

#### HL7 Messaging

N/A

#### Web Services

N/A

### Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VistA users are required to observe VA rules of behavior regarding patient privacy and the security of patient information, VA computers, and VA networks.

#### Security Menus and Options

N/A

#### Security Keys and Roles

Table 16 lists security keys.

<span id="_Toc199923298" class="anchor"></span>Table 16: EHM\*1\*8 Security Key

| SECURITY KEY NAME | DESCRIPTION                                                                             |
|-----------------------|---------------------------------------------------------------------------------------------|
| EHM RX CANCEL         | Used to access the Pharmacy Discontinue RX (EHM PHARMACY DISCONTINUE RX\] main menu option. |

#### File Security

#### N/A

## EHM\*1\*9 – EHRM-IO Kernel Cutover Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch EHM\*1\*9 loads Kernel tools that are used during cutover from VistA to Millennium. The patch is a component of the EHM Package. It is not to be nationally released.

Version 1 of the patch includes options used to manage user access and security keys by the Health Informatics Transition Team (HITT).

The user access options allow the transition team to restrict user access to VistA at cutover. They are used in conjunction with WebVRAM. The delete key option removes a key from all entries in the New Person file (#200).

The user access menu has five (5) options:

1.  List users to be terminated \[EHM USER TERMINATION LIST\]
2.  Remove single user from termination list\[EHM REMOVE SINGLE USER\]
3.  Revert single user's termination \[EHM REVERT SINGLE USER\]
4.  Set user termination date \[EHM SET USER TERMINATION DATE\]

On the night of cutover, user access to VistA is terminated for existing users using the EHM SET USER TERMINATION DATE option. The users affected are those that have been flagged previously using Web VRAM.

Prior to terminating user access, a single user can be removed from the termination list using the EHM REMOVE SINGLE USER option. After access has been terminated, a single user’s termination can be reversed using the EHM REVERT SINGLE USER option.

The list option exists to prepare for go-live. The list shows the users that will be terminated by the set user termination date option.

The key management menu consists of two options: 1) delete key and 2) restore key. With the first option, the user selects a key to be deleted from all entries in the New Person file (#200). The code that deletes the key builds a list of the records edited so that the restore option can be used to reverse the deletion.

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 17 lists the routines associated with EHRM-IO TOOLS software and their descriptions.

<span id="_Ref124162942" class="anchor"></span>Table 17: EHM\*1\*9 Routines

| ROUTINE NAME | ROUTINE DESCRIPTION                      |
|--------------|------------------------------------------|
| EHMKEYS      | Code to support key delete/restore.      |
| EHMTERM      | Code to support user access termination. |

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

#### EHMKEYS

This routine is in two parts – one to delete key and one to restore the deleted key.

KEY is used to delete a key from all entries in the New Person file (#200). As each record is updated, an entry is made in ^XTMP so that the deleted key can be restored. Note that the ^XTMP list is key specific so that more than one key can be deleted by repeated executions of the routine or its associated option.

RESTRKEY is used to re-load a deleted key to the entries in file \#200.

#### EHMTERM

The following subroutines and functions exist in EHMTERM.

ENTRY – Scans the New Person file (#200), selects records that have been flagged by VRAM and sets the user’s termination date to tomorrow.

REPORT – Produces report of users to be terminated.

HEADER – Header subroutine used by REPORT.

USERLIST – Function that scans the New Person file (#200), identifies records eligible for termination on a specific date. Returns number of entries found.

COMPARE – Compares the list produced by USERLIST with externally-produced lists of local and remote users to be terminated.

COMPRHDR – Header subroutine used by COMPARE.

LOADLIST – Function that loads a list of usernames in either of two methods: 1) typed in or cut-and-paste or 2) from a text file. Returns number of names loaded.

CENTER – Function that returns a centered string.

CONTINUE – Function that prompts the user to continue or stop screen display. Returns user response.

RESTORE – Subroutine that scans the list of terminated users created when ENTRY is run and resets the termination date to be what it was before ENTRY was executed.

RESTRUSR – Subroutine that resets the termination date for a single user.

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 18 lists EHRM-IO Kernel Cutover Tools options and their descriptions.

<span id="_Ref124163187" class="anchor"></span>Table 18: EHM\*1\*9 Options

| OPTION NAME                 | DESCRIPTION                                                                                        |
|---------------------------------|--------------------------------------------------------------------------------------------------------|
| EHM KEY DELETE                  | Runs the KEY subroutine in EHMKEYS to delete a key from entries in the New Person file (#200).         |
| EHM KEY MENU                    | Top level menu for options to delete and restore keys in mass.                                         |
| EHM KEY RESTORE                 | Runs the RESTRKEY subroutine in EHMKEYS to restore a key to entries in the New Person file (#200).     |
| EHM MAIN MENU                   | Top level menu for options needed for the EHM application.                                             |
| EHM REVERT SINGLE USER          | Runs the RESTRUSR subroutine in EHMTERM to revert a single user’s termination date.                    |
| EHM SET USER TERMINATION DATE   | Runs the ENTRY subroutine in EHMTERM to set user termination dates.                                    |
| EHM-00001 (EHM TRANSITION MENU) | All the options needed for the HITT/CAC Transition Menu                                                |
| EHM USER ACCESS MENU            | Top level menu for options to terminate VistA access to users and, if necessary, restore their access. |
| EHM USER TERMINATION LIST       | Runs the REPORT subroutine in EHMTERM to list users to be terminated on a specific date.               |

### Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integration Control Registrations (ICR)

N/A

#### Application Programming Interfaces

N/A

#### Remote Procedure Calls

N/A

#### HL7 Messaging

N/A

#### Web Services

N/A

### Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VistA users are required to observe VA rules of behavior regarding patient privacy and the security of patient information, VA computers, and VA networks.

#### Security Menus and Options

N/A

#### Security Keys and Roles

Table 19 lists security keys.

| SECURITY KEY NAME | DESCRIPTION                                                                              |
|-----------------------|----------------------------------------------------------------------------------------------|
| EHM USER ACCESS       | Used to restrict access to the user access options provided with the EHRM-IO Toolkit.        |
| EHM KEY DELETE        | Used to restrict access to the key delete/restore options provided with the EHRM-IO Toolkit. |

#### File Security

#### N/A

## EHM\*1\*10 – IFC and PRF HL7 Message Storage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inter-Facility Consult (IFC) and Patient Record Flag (PRF) HL7 Message Storage functionality was created to facilitate research into issues resulting from communication between non-converted VistA sites and converted Cerner sites. The VistA HL7 system lacks capacity to store HL7 messages for longer than a few days because of the large number of messages exchanged between systems. EHM\*1\*10 addresses this restriction by separately saving a select group of HL7 messages and retaining them for a longer period of time. The only HL7 messages saved are IFC and PRF messages that are sent by Cerner to a non-converted VistA or vice versa, a very small subset of the total volume of HL7 messages.

EHM\*1\*10 is one of four patches contained in the <u>IFC PROXY ADD/ORDER RESUBMISSION 1.0</u> mutli-build. The patch creates a VistA database to store Inter-Facility Consult (IFC) and Patient Record Flag (PRF) Health Level Seven (HL7) messages sent by or received from Cerner. It also provides application programming interfaces (API) that can be called to add records to the database as well as routines and options to inquire into it and to purge its contents.

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 20 lists the file names and numbers created by EHM\*1\*10 software.

<span id="_Ref124323127" class="anchor"></span>Table 20: EHM\*1\*10 File Names and Numbers

| FILE NUMBER | FILE NAME                  | GLOBAL          | DESCRIPTION                                                                            |
|-------------|----------------------------|-----------------|----------------------------------------------------------------------------------------|
| 1609        | EHRM HL7 Message           | ^EHMHL7(1609,   | File \#1609 is the repository for HL7 messages.                                        |
| 1609.1      | EHRM HL7 Message Retention | ^EHMHL7(1609.1, | This file specifies the number of days to retain entries in the EHRM HL7 Message file. |

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

#### EHRM HL7 Message (#1609)

The EHRM HL7 Message file stores HL7 messages sent to Cerner by VistA or sent by Cerner to VistA so they can be used to research issues or data discrepancies involving the two systems. Records are added to the file by calls to EHM\*1\*10 APIs. Records are deleted by the EHMHL7 PURGE option.

The file is a chronological record of HL7 messages received by or sent from a VistA instance. The TYPE field (#1) differentiates between Inter-Facility Consult (IFC) and Patient Record Flag (PRF) messages. MESSAGE ID (#2) is extracted from MSH-10, VISTA CONSULT NUMBER (#3) is extracted from ORC-4. CERNER ORDER NUMBER (#4) is extracted from ORC-3. PATIENT’S NAME (#5) is extracted from PID-6. ICN (#6) is extracted from PID-4. SENDER (#7) is extracted from MSH-4. RECEIVER (#8) is extracted from MSH-6.

CONDENSED DATA DICTIONARY---EHRM HL7 Message FILE (#1609)UCI: CLE623,ROU

STORED IN: ^EHMHL7(1609, DEC 19,2022 PAGE 1

---------------------------------------------------------------------------

CROSS REFERENCED BY:

DATE/TIME POSTED(B) CERNER ORDER NUMBER(CERNER)

VISTA CONSULT NUMBER(CONSULT) ICN(ICN) MESSAGE ID(MSGID)

PATIENT'S NAME(PATIENT)

FILE STRUCTURE

FIELD FIELD

NUMBER NAME

.01 DATE/TIME POSTED (RD), \[0;1\]

1 TYPE (S), \[0;2\]

2 MESSAGE ID (FJ50), \[0;3\]

3 VISTA CONSULT NUMBER (FJ30), \[0;4\]

4 CERNER ORDER NUMBER (FJ30), \[0;5\]

5 PATIENT'S NAME (FJ50), \[0;6\]

6 ICN (FJ30), \[0;7\]

7 SENDER (FJ30), \[0;8\]

8 RECEIVER (FJ30), \[0;9\]

10 HL7 MESSAGE (Multiple-1609.01), \[1;0\]

.01 HL7 MESSAGE (Wx), \[0;1\]

#### EHRM HL7 Message Retention (#1609.1)

The EHRM HL7 Message Retention file defines the number of days to retain records in the EHRM HL7 Message file. TYPE (#.01) is either IFC or PRF. RETENTION (#1) is the number of days before a record is purged from file \#1609 by the EHMHL7 PURGE option.

CONDENSED DATA DICTIONARY---EHRM HL7 Message Retention FILE (#1609.1)UCI: CLE623,ROU

STORED IN: ^EHMHL7(1609.1, DEC 16,2022 PAGE 1

---------------------------------------------------------------------------

CROSS REFERENCED BY:

TYPE(B)

FILE STRUCTURE

FIELD FIELD

NUMBER NAME

.01 TYPE (RS), \[0;1\]

1 RETENTION (NJ3,0), \[0;2\]

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 21 lists the routine created by EHM\*1\*10 software.

<span id="_Ref124253657" class="anchor"></span>Table 21: EHM\*1\*10 Routines

| ROUTINE NAME | ROUTINE DESCRIPTION                                                                                             |
|--------------|-----------------------------------------------------------------------------------------------------------------|
| EHMHL7       | APIs to create a record in the EHRM HL7 Message file (#1609). Code for EHMHL7 INQUIRE and EHMHL7 PURGE options. |

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

#### EHMHL7

This routine contains the APIs used to add an HL7 message to file \#1609 as well as to inquire into or purge records from the database.

SAVEHL7 – function to add an HL7 message to file \#1609. TYPE must be defined as either IFC or PRF depending on the type of HL7 message to be recorded. The contents of the HL7 message are generated by the function from the VistA HL7 system.

SAVEHL7X – function to add an HL7 message to file \#1609. TYPE must be defined as either IFC or PRF depending on the type of HL7 message to be recorded. The contents of the HL7 message are passed in ^TMP(NODE,\$J).

GETHL7 – subroutine that loads an HL7 message from the VistA HL7 system and returns it in the HL7MSG array.

FILE – function to post an HL7 message to file \#1609. The HL7 message is passed in the HL7MSG array. The type of message (IFC or PRF) is passed in the TYPE parameter. In addition to adding the HL7 message to file \#1609, FILE extracts key data fields from the message and files them in separate fields.

PARSE – function that returns a field from an HL7 segment. PARSE scans the message (HL7MSG array) for the requested segment (SEGID) then extracts and returns the requested field (FIELDNO). PARSE also extracts and returns the HL7 field separator (FS), component separator (CS) and repetition separator (RS) so that the returned field can be further parsed by the calling code.

PURGE – subroutine that scans file \#1609 and deletes record older than the retention period for the record’s type specified in file \#1609.1. Invoked by the EHMHL7 PURGE option.

INQUIRE – subroutine that inquires into file \#1609 by Message ID, VistA Consult Number, Cerner Order Number, Patient’s Name, ICN or Posting Date. Invoked by the EHMHL7 INQUIRE option.

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 22 lists the routine created by EHM\*1\*10 software.

<span id="_Ref124321336" class="anchor"></span>Table 22: EHM\*1\*10 Options

| OPTION NAME    | OPTION DESCRIPTION                                                |
|----------------|-------------------------------------------------------------------|
| EHMHL7 INQUIRE | Inquire into EHRM HL7 Message file (#1609). Runs INQUIRE^EHMHL7.  |
| EHMHL7 MENU    | EHRM HL7 Message menu.                                            |
| EHMHL7 PURGE   | Purge EHRM HL7 Message file (#1609.1) entries. Runs PURGE^EHMHL7. |

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

### Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integration Control Registrations (ICR)

Subscriber ICR 7424 created to use APIs to add records to EHRM HL7 Message file (#1609).

#### Application Programming Interfaces

#### SAVEHL7^EHMHL7

External packages that need to add records to the EHRM HL7 Message file (#1609) may call this API. The type of message – IFC or PRF – is passed in as a parameter. The HL7 message is obtained by the API from the VistA HL7 system.

#### SAVEHL7X^EHMHL7

External packages that need to add records to the EHRM HL7 Message file (#1609) may call this API. The type of message – IFC or PRF – is passed in as a parameter. The HL7 message is stored in ^TMP(NODE,\$J), and NODE is passed to the API as a parameter.

#### Remote Procedure Calls

N/A

#### HL7 Messaging

N/A

#### Web Services

N/A

### Standards and Conventions Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

#### Internal Relationships

N/A

#### Software-wide Variables

N/A

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VistA users are required to observe VA rules of behavior regarding patient privacy and the security of patient information, VA computers, and VA networks.

#### Security Menus and Options

N/A

#### Security Keys and Roles

N/A

#### File Security

Table 23 details file security.

<span id="_Ref124322687" class="anchor"></span>Table 23: EHM\*1\*10 File Security

|                 |                 |          |           |           |                     |            |
|-----------------|-----------------|----------|-----------|-----------|---------------------|------------|
| FILE NUMBER | GLOBAL      | READ | WRITE | LAYGO | DATA DICTIONARY | DELETE |
| 1609            | ^EHMHL7(1609,   | @        | @         | @         | @                   | @          |
| 1609.1          | ^EHMHL7(1609.1, | @        | @         | @         | @                   | @          |

## EHM\*1\*13 – Converted Appointment Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch EHM\*1\*13 loads tools that are used during and after cutover from VistA to Cerner. The patch is a component of the EHM Package.

At the time of cutover, appointments made for dates that post-date conversion are loaded into Cerner. Those appointments should not be left active in VistA. EHM\*1\*13 provides tools for identifying those appointments and marking them as converted. Appointments entered VistA post-conversion that duplicate appointments in Cerner should also not be left active in VistA. EHM\*1\*13 provides tools for identifying these appointments and cancelling them.

After conversion, appointments should not be entered for most, if not all, clinics in VistA. EHM\*1\*13 provides tools to automatically inactivate clinics. It also creates a mechanism to identify any clinics that use VistA post-conversion and prevent them from being inactivated.

EHM\*1\*13 also provides tools to summarize and list:

1)  Active appointments
2)  All appointments
3)  Appointment requests
4)  Appointments with action required encounters

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 24 lists the files created by EHM\*1\*13.

| Table Name                 | Table Description                                                                                                                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EHRM ACTIVE CLINIC (#1610) | This file stores the VistA clinics that are active on a site after it is converted to Millennium. The file is used by the automated clinic inactivation tool (included with EHM\*1\*10), so the clinics are left active. |

EHM\*1\*13 also adds a value (CNV – Converted to Cerner) to the status fields in the appointment multiple in the PATIENT (#2) file and to the SDEC APPOINTMENT file (#409.84). EHM\*1\*13 adds CNV to each field’s set of codes.

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 25 lists the routines associated with the Converted Appointment Maintenance tools and their descriptions.

<span id="_Ref164667765" class="anchor"></span>Table 25: EHM\*1\*13 Routines

| ROUTINE NAME | ROUTINE DESCRIPTION                                                                                                                                                                                                    |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EHM013P      | Post-install routine that adds "CONVERTED TO CERNER" and "DUPLICATE - CERNER" to the CANCELLATION REASONS file (#409.2).                                                                                               |
| EHM13UTIL    | Contains common functions and subroutines.                                                                                                                                                                             |
| EHMAPPT      | Contains code to generate converted appointment reports. Also contains common subroutines used to output formatted and comma-delimited lists.                                                                          |
| EHMAPPT0     | Contains code to generate post-conversion and all appointment reports.                                                                                                                                                 |
| EHMAPPT1     | Contains code to change the status of converted appointments to “converted” and to cancel post-conversion appointments. Produces lists of clinics for inactivation. Contains code to automatically inactivate clinics. |
| EHMAPPT2     | Contains code to output summary reports. Contains code to produce reports of action required encounters for converted, post-conversion and all appointments.                                                           |
| EHMAPPT3     | Contains code to produce summaries of converted or post-conversion appointments with action required encounters and to add/edit clinics to the EHRM ACTIVE CLINIC file (#1610).                                        |
| EHMAPPTR     | Contains code to generate active appointment reports.                                                                                                                                                                  |
| EHMAPPTZ     | Clone of EHMAPPT used to produce converted appointment list with IENs displayed for UAT (option EHM_CONVERTED APPT LIST (UAT)).                                                                                        |
| EHMAPPTZ0    | Clone of EHMAPPT0 used to produce post-conversion appointment list with IENs displayed for UAT (option EHM_POST CONV APPT LIST (UAT)).                                                                                 |
| EHMAPTRQ     | Contains code to generate appointment request reports.                                                                                                                                                                 |
| EHMSDC8A     | Contains code to mark appointments converted or to cancel post-conversion appointments. Code was cloned from SDEC08A then modified.                                                                                    |
| EHMSDEC8     | Contains code to mark appointments converted or to cancel post-conversion appointments. Code was cloned from SDEC08 then modified.                                                                                     |

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

#### EHM013P

This is the post-install routine for EHM\*1\*13. It adds two (2) new entries to the CANCELLATION REASONS file (#409.2).

RUN – Entry point for post-install execution. Code adds two (2) new entries to the CANCELLATION REASONS file if they do not already exist.

#### EHM13UTIL

This routine contains several common functions and subroutines.

ENCTRSTS – Function that returns the status of an encounter. If the candidate encounter is not a parent encounter, the function looks to its parent.

MPTYNCTR – Function that determines if an encounter is “empty” or not. The code extracts the visit associated with the encounter and then checks to see if the visit has a provider, diagnosis, service/procedure, immunization, health factor or TIU note associated with it. If none are present, the encounter is considered empty. If only TIU notes are associated with the visit and all of the notes have been retracted, the encounter is also considered empty.

ADDAPPT – Function that adds an entry in the SDEC APPOINTMENT file (#409.84) so that the appointment can be cancelled in all files. This function was required because some code operating in VistA post-conversion created appointments only in the PATIENT (#2) and HOSPITAL LOCATION (#44) files.

LASTFI – Function that returns the last name and first initial for a patient or full name.

FMTDDTM – Function that returns a FileMan date/time in “MM/DD/YY@HHMM” format.

PROGRESS – Subroutine that outputs the progress of a compilation.

COMMAOUT – Function that returns a set of values as a comma-delimited record.

CENTER – Function that returns a centered text string.

DASHES – Function that returns a string of dashes for underlining.

CONTINUE – Function that prompts the user to continue and returns the result.

STRIP – Function the returns a string without leading spaces.

COMMAOUT2 – Function that returns a set of values as a comma-delimited record.

CONVDATE – Function to prompt the user for the conversion date.

SORTORDR – Function to prompt the user for the list report sort order.

FILTER – Function to prompt the user for the encounter filter.

CLINICS – Function to prompt the user for the clinic filter and selected clinics.

NONCOUNT – Function to prompt the user to include or exclude non-count clinics.

RPTFMT – Function to prompt the user for the list report format.

#### EHMAPPT

This routine produces converted appointment datasets and reports. It also contains callable subroutines to output formatted or comma-delimited lists of records.

CNVSELCT – Subroutine that prompts for and collects the attributes of a converted appointments dataset. The user is prompted for conversion date, sort order, all or single clinic, encounter filter and whether to include or exclude non-count clinics.

CNVTDAPT – Subroutine that identifies converted appointments that satisfy the desired attributes and returns the dataset in ^TMP(\$J).

CNVTDLST – Entry point to produce a converted appointments list.

CNVTDLS1 – TaskMan start point for a converted appointments list.

HEADER – Subroutine that outputs a header for a formatted report.

APPTLSTF – Subroutine that outputs an appointments list from a dataset in report format. It is used for converted appointment reports (CNVTDLST^EHMAPPT), post-conversion appointment reports (POSTLIST^EHMAPPT0) and all appointment reports (APPTLIST^EHMAPPT0).

APPTLSTC - Subroutine that outputs an appointments list from a dataset in comma-delimited format. It is used by CNVTDLST^EHMAPPT and by POSTLIST^EHMAPPT0.

#### EHMAPPT0

This routine produces post-conversion appointments datasets and reports and all appointment datasets and reports.

POSTSLCT – Subroutine that prompts for and collects the attributes of a post-conversion appointments dataset. The user is prompted for conversion date, sort order, all or single clinic, encounter filter and whether to include or exclude non-count clinics.

POSTLIVE – Subroutine that identifies post-conversion appointments that satisfy the desired attributes and returns the dataset in ^TMP(\$J).

POSTLIST – Entry point to produce a post-conversion appointments list.

POSTLST1 – TaskMan start point for a post-conversion appointments list.

SUMMARY – Entry point to produce a summary of post-conversion appointments.

SUMMARY1 – TaskMan start point for a post-conversion appointments summary.

ALLSLCT – Subroutine that prompts for and collects the attributes of an dataset. The user is prompted for sort order and all or single clinic.

ALLAPPTS – Subroutine that identifies all appointments that satisfy the desired attributes and returns the dataset in ^TMP(\$J).

APPTLIST – Entry point to produce an list.

APPTLST1 – TaskMan start point for an list.

APPTSMRY – Entry point to produce a summary of all appointments.

APTSMRY1 – TaskMan start point for an summary.

#### EHMAPPT1

CNVTDCLN – Subroutine that marks all eligible conversion appointments CONVERTED. Eligible appointments are those created before the conversion date but with an appointment date on or after the conversion date. Appointments may not have a non-empty action required encounter associated with them.

SELCTAPPT – Subroutine to interactively identify an appointment for a patient that can be marked CONVERTED or CANCELLED.

MARKCNVTD – Subroutine that marks an individual appointment CONVERTED.

MARKCANC – Subroutine that marks an individual appointment CANCELLED.

CANCAPPT – Subroutine that marks all eligible post-conversion appointments CANCELLED. Eligible appointments are those created after the conversion date with an appointment date on or after the conversion date. Appointments may not have a non-empty action required encounter associated with them.

INACTLIST – Subroutine that lists clinics and their eligibility to be inactivated. Output can be: 1) all clinics, 2) all except inactive clinics, 3) clinics eligible to be inactivated or 4) clinics with future appointments.

INACTLS1 – TaskMan entry point for the clinic list.

APPTCNT – Function that returns the number of active and future appointments for a clinic.

INACTHDR – Subroutine that outputs the header for the clinic list.

INACTVAT – Subroutine that inactivates eligible clinics. Clinics must be active and not have future appointments for them to be automatically inactivated.

SDNACT – Function that inactivates a clinic. The code in this label and those that follow were cloned from the SDNACT routine and modified to remove user interaction.

#### EHMAPPT2

This routine outputs summaries from appointment datasets and produces reports about ACTION REQUIRED encounters for converted, post-conversion and all appointment datasets.

SUMMARY – Entry point to produce a summary report for converted appointments.

SUMMARY1 – TaskMan start point for a converted appointment summary report.

SUMOUT – Subroutine that outputs a summary report for an appointment dataset. It is called by EHMAPPT and EHMAPPT0 for converted, post-conversion and all appointment datasets.

SUMHDR – Subroutine that outputs header for a summary report.

CNVTD – Entry point to produce a report of ACTION REQUIRED encounters for converted appointments.

CNVTD1 – TaskMan start point for report of ACTION REQUIRED encounters for converted appointments.

POSTLIVE – Entry point to produce a report of ACTION REQUIRED encounters for post-conversion appointments.

POSTLIV1 – TaskMan start point for report of ACTION REQUIRED encounters for post-conversion appointments.

ALLAPPT – Entry point to produce a report of ACTION REQUIRED encounters for all appointments.

ALLAPPT1 – TaskMan start point for report of ACTION REQUIRED encounters for all appointments.

ACTREQ – Subroutine to output an ACTION REQUIRED encounters report.

ACTREQF – Subroutine to output an ACTION REQUIRED encounter formatted report.

ACTREQC - Subroutine to output an ACTION REQUIRED encounter comma-delimited report.

ACTREQHD – Subroutine to output a header for an ACTION REQUIRED encounter formatted report.

#### EHMAPPT3

This routine produces summaries of appointments with action required encounters.

CNTVD – Entry point to generate a summary report of converted appointments with action required encounters.

CNVTD1 – TaskMan start point for summary report of converted appointments with action required encounters.

POSTLIVE – Entry point to generate a summary report of post-conversion appointments with action required encounters.

POSTLIV1 – TaskMan start point for summary report of post-conversion appointments with action required encounters.

ALLAPPT – Entry point to generate a summary report of all appointments with action required encounters.

ALLAPPT1 – TaskMan start point for summary report of all appointments with action required encounters.

EDIT1610 – Entry point for the EHM_ACTIVE CLINIC ADD/EDIT option. Allows the user to add or delete clinics from the EHRM ACTIVE CLINIC file (#1610) by name or stop code.

#### EHMAPPTR

This routine produces active appointment summaries and reports.

ACTVSLCT – Subroutine that prompts for and collects the attributes of an active appointment’s dataset. The user is prompted for conversion date; sort order; all, single clinic and single stop code and whether to include dental classification.

ACTVAPPT – Subroutine that identifies active appointments that satisfy the desired attributes and returns the dataset in ^TMP(\$J).

ACTVLIST – Entry point to produce an active appointments list.

ACTVLST1 – TaskMan start point for an active appointments list.

SUMMARY – Entry point to produce a summary of active appointments.

SUMMARY1 – TaskMan start point for an active appointment’s summary.

APPTLSTF – Subroutine that outputs an active appointments list in report format.

APPTLSTC – Subroutine that outputs an active appointments list in comma-delimited format.

HEADER – Subroutine that outputs a header for a formatted report.

EDIPI – Function that returns the EDIPI for a patient from the treating facility list.

#### EHMAPPTZ

This routine produces the same reports as EHMAPPT except that it also displays IENs from the OUTPATIENT ENCOUNTER file (#409.68) for use during user acceptance testing (UAT).

See section 2.6.2.3 for description of the subroutines.

#### EHMAPPTZ0

This routine produces the same reports as EHMAPPT0 except that it also displays IENs from the OUTPATIENT ENCOUNTER file (#409.68) for use during user acceptance testing (UAT).

See section 2.6.2.4 for description of the subroutines.

#### EHMAPTRQ

This routine produces appointment request summaries and reports. Data about appointment requests are extracted from the SDEC APPT REQUEST file (#409.85), the SD WAIT LIST file (#409.2) and the RECALL REMINDERS file (#403.5).

OPENRQST – Subroutine that compiles a dataset of appointment requests and stores it in ^TMP(\$J).

RQSTLIST – Entry point to produce an appointment request list.

RQSTLST1 – TaskMan start point for an appointment request list.

HEADER – Subroutine that outputs a header for a formatted report.

APPTLSTF – Subroutine that outputs an appointment request list in report format.

APPTLSTC – Subroutine that outputs an appointment request list in comma-delimited format.

SUMMARY – Entry point to produce a summary of appointment requests.

SUMMARY1 – TaskMan start point for an appointment requests summary.

SUMHDR – Subroutine that outputs header for a summary report.

#### EHMSDC8A

This routine is used to change the status of converted appointments and to cancel post-conversion appointments. SDEC08A was cloned and modified.

#### EHMSDEC8

This routine is used to change the status of converted appointments and to cancel post-conversion appointments. SDEC08 was cloned and modified.

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 26 lists Converted Appointment Maintenance options and their descriptions.

<span id="_Ref164689540" class="anchor"></span>Table 26: EHM\*1\*13 Options

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>OPTION NAME</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EHM_ACT REQ-ALL</td>
<td>This report lists ACTION REQUIRED encounters for all appointments and the reason(s) that the encounters are not empty.</td>
</tr>
<tr class="even">
<td>EHM_ACT REQ-CONVERTED</td>
<td>This report lists ACTION REQUIRED encounters for converted appointments and the reason(s) that the encounters are not empty.</td>
</tr>
<tr class="odd">
<td>EHM_ACT REQ-POST-CONVERSION</td>
<td>This report lists ACTION REQUIRED encounters for post-conversion appointments and the reason(s) that the encounters are not empty.</td>
</tr>
<tr class="even">
<td>EHM_ACTIVE APPOINTMENT LIST</td>
<td>This option produces a list of active appointments at a site prior to conversion.</td>
</tr>
<tr class="odd">
<td>EHM_ACTIVE APPOINTMENT SUMMARY</td>
<td>This option produces a summary of the active appointments at a site prior to conversion. The user is prompted for the prospective conversion date. The summary can be run for a single clinic, a single stop code or all clinics.</td>
</tr>
<tr class="even">
<td>EHM_ACTIVE APPOINTMENTS</td>
<td>Menu for active appointment options.</td>
</tr>
<tr class="odd">
<td>EHM_ACTIVE CLINIC ADD/EDIT</td>
<td>This option populates the EHRM ACTIVE CLINIC file (#1610). The clinics in this file are those that are active in VistA post conversion to Cerner. Appointments made to these clinics will not be automatically cancelled nor will the clinics be automatically inactivated.</td>
</tr>
<tr class="even">
<td>EHM_ACTIVE CLINIC LIST</td>
<td>This option lists the EHRM ACTIVE CLINIC file (#1610). The clinics in this file are those that are active in VistA post conversion to Cerner. Appointments made to these clinics will not be automatically cancelled nor will the clinics be automatically inactivated.</td>
</tr>
<tr class="odd">
<td>EHM_ACTIVE CLINICS</td>
<td>Sub-menu for active clinic options</td>
</tr>
<tr class="even">
<td>EHM_ALL ACT REQ SUMMARY</td>
<td>This option produces a summary report of all appointments with action required encounters.</td>
</tr>
<tr class="odd">
<td>EHM_ALL APPOINTMENT LIST</td>
<td>This option lists all appointments that are not cancelled, no-shows, checked in or checked out.</td>
</tr>
<tr class="even">
<td>EHM_ALL APPOINTMENT SUMMARY</td>
<td>This option summarizes all appointments that are not cancelled, no-shows, checked in or checked out.</td>
</tr>
<tr class="odd">
<td>EHM_ALL APPOINTMENTS</td>
<td>Sub-menu for all appointments options.</td>
</tr>
<tr class="even">
<td>EHM_APPOINTMENT CLEANUP</td>
<td>Menu for all sub-menus.</td>
</tr>
<tr class="odd">
<td>EHM_APPOINTMENT REQUESTS</td>
<td>Sub-menu for all appointment request options.</td>
</tr>
<tr class="even">
<td>EHM_APPT REQUEST LIST</td>
<td>This option lists open appointment requests from the SDEC APPOINTMENT REQUEST (#409.85), the SD WAIT LIST (#409.3) and the RECALL REMINDERS (#403.5) files.</td>
</tr>
<tr class="odd">
<td>EHM_APPT REQUEST SUMMARY</td>
<td>This option summarizes open appointment requests from the SDEC APPOINTMENT REQUEST (#409.85), the SD WAIT LIST (#409.3) and the RECALL REMINDERS (#403.5) files.</td>
</tr>
<tr class="even">
<td>EHM_CLINIC CLEANUP OPTIONS</td>
<td>Sub-menu for menus that manage active clinics and the inactivation of clinics.</td>
</tr>
<tr class="odd">
<td>EHM_CNVTD ACT REQ SUMMARY</td>
<td>This option produces a summary report of converted appointments with action required encounters.</td>
</tr>
<tr class="even">
<td>EHM_CONVERTED APPOINTMENT LIST</td>
<td>This option lists appointments converted to Cerner. These are the active (not cancelled) appointments that have an appointment date after the date of conversion that were entered before the date of conversion but no more than two years ago.</td>
</tr>
<tr class="odd">
<td>EHM_CONVERTED APPOINTMENTS</td>
<td>Sub-menu for all converted appointments options.</td>
</tr>
<tr class="even">
<td>EHM_CONVERTED APPT CLEANUP</td>
<td>This option identifies all appointments created before the conversion date with appointment dates on or after the conversion date and marks them "converted."</td>
</tr>
<tr class="odd">
<td>EHM_CONVERTED APPT SUMMARY</td>
<td>This option summarizes appointments converted to Cerner. These are the active (not cancelled) appointments that have an appointment date after the date of conversion that were entered before the date of conversion but no more than two years ago.</td>
</tr>
<tr class="even">
<td>EHM_INACTIVATE CLINICS</td>
<td>Sub-menu for inactivate clinics options.</td>
</tr>
<tr class="odd">
<td>EHM_INACTIVATE CLINICS LIST</td>
<td><p>This option lists clinics prior to inactivation. The list can be produced for the following:</p>
<p>1. All Clinics</p>
<p>2. All Clinics except Inactive Clinics</p>
<p>3. Clinics Eligible for Inactivation</p>
<p>4. Clinics with Future Appointments</p></td>
</tr>
<tr class="even">
<td>EHM_INACTIVATE_CLINICS</td>
<td><p>This option inactivates clinics in converted environments. The user enters the date of conversion. The HOSPITAL LOCATION (#44) file is scanned for active clinics. If they have no future appointments - or only appointments marked "converted" - then they are inactivated.</p>
<p>A summary of the number of clinics inactivated as well as those that could not be inactivated is produced.</p></td>
</tr>
<tr class="odd">
<td>EHM_MARK APPOINTMENT CANCELLED</td>
<td><p>This option to cancels a selected appointment with a cancellation reason indicating that it is a duplicate of one in</p>
<p>Cerner.</p></td>
</tr>
<tr class="even">
<td>EHM_MARK APPOINTMENT CONVERTED</td>
<td>This option marks a selected appointment converted.</td>
</tr>
<tr class="odd">
<td>EHM_POST ACT REQ SUMMARY</td>
<td>This option produces a summary report of post-conversion appointments with action required encounters.</td>
</tr>
<tr class="even">
<td>EHM_POST CONV APPT SUMMARY</td>
<td>This option summarizes active (not cancelled) appointments in a converted system that have an appointment date after the date of conversion that were entered after the date of conversion.</td>
</tr>
<tr class="odd">
<td>EHM_POST CONVERSION APPT LIST</td>
<td>This option lists active (not cancelled) appointments in a converted system that have an appointment date after the date of conversion that were entered after the date of conversion.</td>
</tr>
<tr class="even">
<td>EHM_POST CONVERSION CLEANUP</td>
<td>This option identifies all appointments with appointment dates after conversion that were entered after conversion and cancels them with a reason that they are duplicates of Cerner appointments.</td>
</tr>
<tr class="odd">
<td>EHM_POST-CONVERSION APPTS</td>
<td>Sub-menu for post-conversion appointment options.</td>
</tr>
</tbody>
</table>

### Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integration Control Registrations (ICR)

N/A

#### Application Programming Interfaces

N/A

#### Remote Procedure Calls

N/A

#### HL7 Messaging

N/A

#### Web Services

N/A

### Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VistA users are required to observe VA rules of behavior regarding patient privacy and the security of patient information, VA computers, and VA networks.

#### Security Menus and Options

N/A

#### Security Keys and Roles

Table 27 lists the patch’s security keys.

| SECURITY KEY NAME | DESCRIPTION                                  |
|-----------------------|--------------------------------------------------|
| EHM_DATA CLEANUP      | Used to access the EHM_APPOINTMENT CLEANUP menu. |

#### File Security

#### N/A

## EHM\*1\*14 – HITT Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch EHM\*1\*14 loads tools that are used during cutover from VistA to Cerner. The patch is a component of the EHM Package.

Version 1 of the patch includes an extensive set of menus and options for the Health Informatics Transition Team (HITT). Except for the top-level and group menus, the menus and options are all clones of national standard options instead of locally modified versions of the same options. The HITT Transition menu contains all the menu options and their submenus needed by the VistA transition team to perform their duties for upcoming converted sites.

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 28 lists the routines associated with EHM HITT MENU software and their descriptions.

<span id="_Ref157003683" class="anchor"></span>Table 28: EHM\*1\*14 Routines

<table>
<caption>3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES</caption>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>ROUTINE NAME</th>
<th>ROUTINE DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>EHM014</td>
<td><p>Code that clones options to build the EHM Transition Menu.</p>
<p><strong>Note:</strong> This routine is not part of the EHM*1*14 patch. It is a developer tool used to generate all of the components of the patch in the OPTION file (#19) and to load them in the BUILD file (#9.6).</p></td>
</tr>
</tbody>
</table>

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

#### EHM014

This routine is used by a developer to generate all of the components of the patch into the Build file. It automatically clones the menus, their sub-menus and options that make up the HITT Transition Menu.

ENTRY – This is the entry point for generating the build. It creates the keys, menus, and options then loads them as file components in the Build file.

VALIDATE – This function checks to see that the menus and options exist for cloning. It also checks to see that the EHM package and the EHM\*1\*14 build exist. The latter two are necessary for automatically loading options into the Build file.

LIST – This subroutine lists the menus and options for each group.

BUILDALL – This subroutine creates a top-level menu, the next level group menus and then clones all of the menus and options that are included in each group. BUILDALL depends on data stored in three different places in EHM014 – 1) TOP, 2) GROUPS and 3) ITEMS – to generate the transition menu. BUILDALL first creates the top menu using the option name and menu text listed in TOP+1. BUILDALL next creates the group menus and assigns them as items to the just created top menu. GROUPS+1, GROUPS+2, etc. specify the option name, menu text and display order for each group. Finally, BUILDALL clones existing options and links them to group menus. ITEMS+1, ITEMS+2, etc. specify the name of the option to clone, then group menu to assign it to and the display order. When EHM014 clones a lower-level menu, it links the newly created items to the cloned menu while linking the cloned menu to the next higher level cloned menu.

CREATKEY – This subroutine creates the security keys used by the patch. See KEYS below to add or remove keys in the patch.

CREATMNU – This function creates a menu in the Option file (#19) and, optionally, makes it an item on a higher-level menu. There are six (6) parameters: 1) NAME,2) TEXT,3) ORDER,4) TOP, 5) DESCRPTN, 6) KEY. The first two (2) are required. The third, fourth, fifth and sixth are optional. NAME is the option name, the .01 field of the Option file. TEXT is the MENU TEXT, field 1 of the Option file. TOP is specified if the new menu is to be assigned to a higher-level menu. TOP must be a pointer to the Option file. If TOP is present, ORDER may also be specified. It is stored in the DISPLAY ORDER field (#3) in the MENU multiple (#10) in the Option file. DESCRPTN is the option description and is stored in the DESCRIPTION field (#3.5). KEY is the security key associated with the option and is stored in the LOCK field (#3).

CLONOPTN – This function clones an option and assigns it to a menu. The OPTION parameter is a pointer to the Option file (#19) and is the option to be cloned. MENU is also a pointer to the Option file and is the menu the newly created option is assigned as an item. SYNONYM and ORDER, if present, are, respectively, the synonym and display order for the newly-created item in MENU. The NAME field (#.01) of the new option is sequentially created in the EHM-00001, EHM-00002… sequence. It is created by looking at the last option in the sequence and adding one to the number. The CLONOPTN function strips out the source option’s security keys before creating the new option.

OPTION – This function clones a single option unless the option is a menu in which case it also clones all of the items for the menu. OPTION uses the following parameters:

- OPTION – The option to be cloned (pointer to \#19)
- MENU – The menu to assign the new option to as an item (pointer to \#19)
- SYNONYM – The menu synonym of the new option in its menu.
- ORDER – The display order of the new option in its menu.

> Note: If the parameters are not specified, the OPTION function prompts the user for each of them.

MENU – This function clones the items of a menu and assigns them to a second menu. MENU1, a pointer to the Option file (#19), specifies the menu to be cloned. MENU, also a pointer to the Option file, specifies the menu where the new items are to be assigned. Prior to calling MENU, the second menu must be created using the CREATMNU function.

This function is at the heart of EHM014. If any of the items associated with the menu to be cloned is a menu, the function recursively calls MENU to clone its items. In this way, a single call to MENU will clone all options associated with the menu and any of its sub-menus however far down they go.

LOOP – This subroutine provides an interactive mechanism for cloning and creating menus and options. It was used prior to the existence of BUILDALL which automated the creation of EHM\*1\*14.

BUILD – The purpose of this subroutine is to automate generation of the EHM\*1\*14 patch and , in particular, to prevent the developer from having to enter thousands of options into the build interactively.

EHM\*1\*14 must exist in the BUILD file (#9.6) before this subroutine can be run. The build should include EHM MAIN MENU as well as the EHM MGR and EHM HITT MENU keys.

BUILD loads the cloned menus and options into the BUILD file entry.

RZJF – This function pads a number with leading zeroes to a desired length.

TOP – This section of the code contains the name and menu text of the Transition menu. It is used by BUILDALL to generate the menu.

GROUPS – This section of the code contains the data required to generate the menus to which all cloned options are assigned. Each line in GROUP has the option name, menu text and display order. It is used by BUILDALL to generate the menus.

New groups can be added to this list as needed.

ITEMS – This section of the code contains the menus and options to clone. Each line in ITEMS has the name of the menu/option to be cloned, the menu to assign it to and the display order. Sub-menus for the listed menus do not have to be included in ITEMS as EHM014 automatically clones all menus and options linked to a listed item.

New items can be added to this list as needed.

KEYS – This section of the code contains the security keys to be generated. Each line contains the key name, descriptive name, and description.

New keys can be added to this list as needed.

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 29Table 23 lists HITT Menu options and their descriptions.

<span id="_Ref157065808" class="anchor"></span>Table 29: EHM\*1\*14 Options

| OPTION NAME                 | DESCRIPTION                                            |
|---------------------------------|------------------------------------------------------------|
| EHM MAIN MENU                   | Top level menu for options needed for the EHM application. |
| EHM-00001 (EHM TRANSITION MENU) | All the options needed for the HITT/CAC Transition Menu    |
| EHM-00002 (ALERTS)              | Alerts-related menus and options group menu.               |
| EHM-00003 (CONSULTS)            | Consults-related menus and options group menu.             |
| EHM-00004 (CPRS)                | CPRS-related menus and options group menu.                 |
| EHM-00005 (CUTOVER)             | Cutover-related menus and options group menu.              |
| EHM-00006 (FILEMAN)             | FileMan-related menus and options group menu.              |
| EHM-00007 (GROUP)               | Group-related menus and options group menu.                |
| EHM-00008 (MENU)                | Menu-related menus and options group menu.                 |
| EHM-00009 (PACKAGES)            | Packages-related menus and options group menu.             |
| EHM-00010 (REMIND)              | Reminder-related menus and options group menu.             |
| EHM-00011 (TIU)                 | TIU-related menus and options group menu.                  |
| EHM-00012 (USER)                | User-related menus and options group menu.                 |

In addition to the listed options, the cloned VistA menus and options are created and assigned names starting with EHM-00013.

### Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integration Control Registrations (ICR)

N/A

#### Application Programming Interfaces

N/A

#### Remote Procedure Calls

N/A

#### HL7 Messaging

N/A

#### Web Services

N/A

### Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VistA users are required to observe VA rules of behavior regarding patient privacy and the security of patient information, VA computers, and VA networks.

#### Security Menus and Options

N/A

#### Security Keys and Roles

Table 30 lists security keys.

| SECURITY KEY NAME | DESCRIPTION                                                             |
|-----------------------|-----------------------------------------------------------------------------|
| EHM MGR               | Used to access the EHM MAIN MENU option for tools used at cutover           |
| EHM HITT MENU         | Used to restrict access to the HITT menu provided with the EHRM-IO Toolkit. |

#### File Security

#### N/A

## GMRC\*3\*192 – EHRM-IO CONSULT CUTOVER TOOLS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch GMRC\*3\*192 loads tools that are used during cutover from VistA to Cerner. The patch is a component of the GMRC Package.

This patch provides tools to update the status of consults by grouper. The existing "Group update of consult/procedure requests" \[GMRCSTSU\] option that bulk updates consult status was cloned and modified as follows:

1)  Functions for grouper request services only.
2)  Expands allowable end of request date range from T-30 to today.
3)  Processes pending, scheduled and active consults without concurrent reporting or user interaction.
4)  Changes status to discontinued automatically.
5)  Files a standard comment with each consult modified.
6)  Records the date the consult was changed to discontinued and the consult's previous status for reporting.
7)  Suppresses generation of HL7 messages for all consults (e.g., IFCs, Community Care, Clinical Procedures) to prevent undesired effects on production environments.

A new option - "Group update of consults" \[GMRCSTSC\] - was created to call routine GMRCSTSC to perform the bulk update.

Two new options were created to list consults changed to discontinued status by the GMRCSTSC option. Output of the list is provided on the screen by the "Consult update report" \[GMRCSTSR\] option or as a comma-delimited list that can be sent to a file by the "Consult update file output" \[GMRCSTSR1\]. The lists are sorted by service (see REQUEST SERVICES - file \#123.5) and then by consult request date (FILE ENTRY DATE (field \#.01) of the REQUEST/CONSULTATION file (#123)).

A third report option - "Service list" \[GMRCSTSR2\] - was created to list the services that have consults in active, pending or scheduled status. The list is sorted by grouper then service and shows the number of active, pending or scheduled consults in each service. The report can be produced for display/printing or as a comma-delimited list that can be uploaded into Excel.

A fourth report option - "Unresolved Consults" \[GMRCSTSQ\] - was created to list unresolved consults (status not discontinued, complete, cancelled or lapsed) for four (4) categories of consults: 1) IFCs, 2) Community Care, 3) Clinical Procedures, 4) Prosthetics. The report can be produced for display/printing or as a comma-delimited list that can be uploaded into Excel.

> **NOTE:** Determining if a VistA site has been converted to Cerner is done by calling the CRNRSITE^VAFCCRNR API. It looks for the value YES in the CERNER ENABLED field (#.02) in the EHRM MIGRATED FACILITIES INSTITUTION file (#391.919).

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new files were added with this patch. Two (2) fields were added to the REQUEST/CONSULTATION file (#123). They are:

1)  DISCONTINUED AT CONVERSION (#509)
2)  STATUS BEFORE DISCONTINUED (#510)

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 31 lists the routines associated with EHRM-IO CONSULT CUTOVER TOOLS software and their descriptions.

<span id="_Ref170740260" class="anchor"></span>Table 31: GMRC\*3\*192 Routines

| ROUTINE NAME | ROUTINE DESCRIPTION                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GMRCASVX     | Clone of GMRCASV (part of the consult status update process) which has been modified to suppress authorization checking for consults by service.                                                                                                                                                                                                                                                                                         |
| GMRCSTSC     | Routine that creates the variables and lists used by GMRCSTS1 to change consult status. GMRCSTSC is used to select grouper service and date range as well as to default values for current status (active, pending, scheduled), update status (discontinued), update method (update only, no report) and update comment. GMRCSTSC then calls GMRCSTS1 to update the consult’s status, generate an activity and store data for reporting. |
| GMRCSTSQ     | Routine that generates the unresolved consults report.                                                                                                                                                                                                                                                                                                                                                                                   |
| GMRCSTSR     | Routine that generates reports and comma-delimited lists of consults updated by GMRCSTSC as well as the service list.                                                                                                                                                                                                                                                                                                                    |
| GMRCSTSX     | Clone of GMRCSTS1 (part of the consult status update process) which has been modified to suppress generation of HL7 messages.                                                                                                                                                                                                                                                                                                            |

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

#### GMRCASVX

This routine was cloned from GMRCASV and modified to suppress authorization checking for consults by service (see PROC). SERV1 is called by GETSRV^GMRCSTSC.

#### GMRCSTSC

This routine is the front-end that automates bulk updates of consults post conversion to Cerner. It parallels the functionality in the existing GMRCSTS routine.

ENTRY – Entry point for the GMRCSTSC option. It first checks to see that it is being run on a converted system. It exits with a message if not. ENTRY then asks the user to select a grouper service and a date range for bulk update of consult status following conversion to Cerner. It then defaults values used by existing code (GMRCSTS1) to actually perform the status update.

Unlike code in GMRCSTS, ENTRY loops through all of the services subordinate to the grouper or its children when identifying the consults to be updated (done by repeated calls to GENTENTS^GMRCSTS1).

GETDTR – Asks user to select a date range of consults to be processed. Unlike GETDTR in GMRCSTS, this subroutine allows the user to select an end date of TODAY.

GETSRV – Asks user to select a grouper service from the REQUEST SERVICES file (#123.5). Once selected, GETSRV calls SERV1^GMRCASVX to build arrays of services.

METHOD – This function returns 4 indicating that consults in active, pending, or scheduled status are to be included in the conversion process.

PROCESS – This subroutine calls the subroutines in GMRCSTS1 and its clone, GMRCSTSX, that actually update the consult, generate an activity, and produce audit records. It was cloned from PROCESS in GMRCSTS1 and then modified to save the consult status before updating, to call AUDIT^GMRCSTSX instead of AUDIT^GMRCSTS1 and to store the update date and the previous status (see SETDATA).

SETDATA – This subroutine stores the date the update was made in field \#509 and the previous status in field \#510 in file \#123. Posting a date in field \#509 also creates the “ACERNER” cross-reference.

UPD1 – This function returns “1^DC” indicating that consult status is to be changed to “Discontinued” not “Complete.”

UPDCMT – This subroutine sets the standard text of the comment posted with the activity in the consult file.

VERIFY – This subroutine prompts the user to proceed with updating consults.

WHATTODO – This function returns “2” indicating that the consults are to be updated not just listed.

#### GMRCSTSQ

This routine produces the unresolved consults report. Output is available in two formats: 1) report style for screen or printer and 2) comma-delimited records that can be uploaded to Excel.

REPORT – This is the entry point for the report. After verifying that the site has been converted, REPORT prompts the user for output style and device.

REPORT2 – This is the entry point when the report is queued and is where the bulk of report processing is performed. REPORT2 scans the REQUEST/CONSULTATION file (#123) searching for unresolved consults that fit into four (4) categories: 1) clinical procedures, 2) community care, 3) IFCs, 4) prosthetics. After the file scan is complete, REPORT2 produces the report in the requested style.

HEADER – This subroutine outputs the header for the human-readable list style of the report.

GROUPER – This function returns the grouper associated with a service.

LASTACTN – This function returns the last action taken on the consult.

#### GMRCSTSR

This routine reports about consults that were discontinued by the GMRCSTSC option. Output is available in two formats: 1) report style for screen or printer and 2) comma-delimited records that can be uploaded to Excel.

REPORT – This is the entry point for report style output. After verifying that the site has been converted, REPORT calls REPORT1 specifying that the output is a list.

FILE – This is the entry point for file output. After verifying that the site has been converted, REPORT calls REPORT1 specifying that the output is a file.

REPORT1 – This subroutine prompts the user for the range of consult request dates and the grouper service to be used when generating the output. If queueing is requested, REPORT1 sets up and calls TaskMan.

REPORT2 – This subroutine generates the requested output. It is also the entry point when the queueing is employed. It first obtains a list of the services directly or indirectly subordinate to the grouper. Next, it scans the “ACERNER” cross-reference in file \#123 to produce the consults to be included in the report. This cross-reference identifies all consults updated by the GMRCSTSC option. The candidate consults are sorted by service name and consult request date.

REPORT2 then outputs either a formatted report or a set of comma-delimited records.

HEADER – This subroutine generates the page header for the formatted report.

FILEHDR – This section of the code has the names of the columns for the comma-delimited records. Column header names follow a pair of semi-colons. A line with a blank column header indicates the end of the list.

START – This subroutine prompts the user for the start date of the range of consult request dates.

STOP – This subroutine prompts the user for the end date of the range of consult request dates.

CENTER – Function that returns a centered string.

GROUPS – This is a subroutine that generates a list of the services subordinate to the grouper service. It is called recursively to process sub-groupers.

NOSECNDS – Function that returns time without seconds.

CONTINUE – Function that prompts the user to continue or stop screen display. Returns user response.

COMMAOUT – Function that returns a string of comma-delimited values from an array.

SERVLIST – This subroutine generates the service list, either as a formatted list or as a comma-delimited list.

#### GMRCSTSX

This routine is a clone of GMRCSTS1 except that HL7 message generation has been suppressed in the AUDIT subroutine. It is called by PROCESS^GMRCSTSC.

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 32Table 23 lists HITT Menu options and their descriptions.

<span id="_Ref170740668" class="anchor"></span>Table 32: GMRC\*3\*192 Options

| OPTION NAME | DESCRIPTION                                     |
|-----------------|-----------------------------------------------------|
| GMRCSTSC        | Group update of consults                            |
| GMRCSTSM        | Consult status update - Converted sites only – menu |
| GMRCSTSQ        | Unresolved consults                                 |
| GMRCSTSR        | Consult update report                               |
| GMRCSTSR1       | Consult update file output                          |
| GMRCSTSR2       | Service list                                        |

#### Group Update of Consults \[GMRCSTSC\]

This option performs bulk updates to status for consults whose service belongs to a grouper service. The option is based on the Group update of consult/procedure requests \[GMRCSTSU\] option. Unlike GMRCSTSU, the GMRCSTSC option only works with grouper services. In addition, the user does not select the consult status to change from – Active, Pending and Scheduled – nor what to change the status to – Discontinued. GMRCSTSC also over-rides authorization requirements present in GMRCSTSU. GMRCSTSC updates the status of identified consults automatically without producing a report. It also posts a standard comment in the activity generated by the status change.

GMRCSTSC records the date that the consult update was made and the status of the consult before the update was made. These fields are used by the reporting options.

#### Consult Update Report \[GMRCSTSR\]

This option produces reports of consults that were updated by the GMRCSTSC option. The user selects a grouper service and a date range when consults were created. The option identifies those consults whose status was changed to discontinued by GMRCSTSC and sorts them by requesting service and request date. The report outputs the following fields:

- Consult number
- Request Date/Time
- Patient’s Name and SSN
- Status Change (From/To)

> A sample report is shown below.

SERVICE: DIABETIC RETINOPATHY SURVEILLANCE TESTING

Aug 21, 1996 - Sep 14, 2022

Consult Request

Number Date/Time Patient/SSN Status Change

---------- ---------------- ------------------------------ -------------

1234567 2/6/2019@09:12 XXXXXXXX,DIEGO LOGAN s to dc

\<SSN\> 9/14/2022@14:16

#### #### Consult Update File Output \[GMRCSTSR1\]

This option produces a list of consults that were updated by the GMRCSTSC option in comma-delimited format that can be uploaded to Excel. The user selects a grouper service and a date range when consults were created. The option identifies those consults whose status was changed to discontinued by GMRCSTSC and sorts them by requesting service and request date.

The report outputs the following fields:

- Service Name
- Consult Number
- Request Date
- Request Time
- Patient’s Name
- SSN
- Status Change (From/To)
- Last Activity Date
- Last Activity Time

A sample of the output is shown below:

“Service Name","Consult Number","Request Date","Request Time","Patient's Name","SSN","Status Change","Last Activity Date","Last Activity Time"

"CAC CP TESTING","1234567","3/24/2017","10:42","XXXXXXX,LAMONT","\<SSN\>","a to dc","9/14/2022","11:05"

"CP RENAL DIALYSIS","7654321","8/27/2018","14:45","XXXXXXXXX,DESIREE","\<SSN\>","a to dc","9/14/2022","11:13"

#### #### Service List \[GMRCSTSR2\]

This option produces a list of services and the number of consults in each service that is in Active, Pending or Scheduled status. The user selects only the output type – formatted list or comma-delimited list. The code scans the REQUEST/CONSULTATION file (#123) for entries that are in active, pending, or scheduled status. It extracts the service from field \#1 TO SERVICE then finds the grouper or groupers that the service belongs to. The resulting output is sorted by grouper and service name.

A sample formatted list is shown below.

GROUPER: ALL SERVICES

SERVICE COUNT

--------------------------------------------------------------- --------

CARE COORDINATION HOME TELEHEALTH SCREENING 1

CAREGIVER SUPPORT PROGRAM OUTPT 2

CHAPLAIN SUICIDE PREVENTION 5

CHY HEMATOLOGY ONCOLOGY AND EXPRESS OUTPATIENT CLINIC CONSULT 9

CLC CONSULT 12

CP STRESS - CV - CARDIOLITE - OUTPAT 8

CP STRESS-CV-PERSANTINE (NON-AMBULATORY)-OUTPAT 17

DENTAL IMAGING 4

DENTAL OUTPATIENT 11

A sample of the comma-delimited output is shown below.

"GROUPER","SERVICE","COUNT"

"ALL SERVICES","CARE COORDINATION HOME TELEHEALTH SCREENING","1"

"ALL SERVICES","CAREGIVER SUPPORT PROGRAM OUTPT","2"

"ALL SERVICES","CHAPLAIN SUICIDE PREVENTION","5"

"ALL SERVICES","CHY HEMATOLOGY ONCOLOGY AND EXPRESS OUTPATIENT CLINIC CONSULT","9"

"ALL SERVICES","CLC CONSULT","12"

"ALL SERVICES","CP STRESS - CV - CARDIOLITE - OUTPAT","8"

"ALL SERVICES","CP STRESS-CV-PERSANTINE (NON-AMBULATORY)-OUTPAT","17"

"ALL SERVICES","DENTAL IMAGING","4"

"ALL SERVICES","DENTAL OUTPATIENT","11"

#### Unresolved Consults \[GMRCSTSQ\]

This option lists all consults that are unresolved (NOT discontinued, complete, expired or lapsed) for four (4) categories: 1) Clinical Procedures, 2) Community Care, 3) IFCs, 4) Prosthetics.

A sample formatted list is shown below.

UNRESOLVED CONSULTS

UNRESOLVED CONSULTS

CLINICAL PROCEDURE

CONSULT/ LAST ACTION/ GROUPER/

REQUEST DT PATIENT NAME/SSN STATUS SERVICE

---------- ------------------------- ----------------------- -------------------------------

7826686 XXXXX,E (1234) ADDED COMMENT CP GI PROCEDURES FUTURE CARE

Feb 04, 2019 ACTIVE WADE PARK SERVICES

7921753 XXXXXX,E (6789) PRINTED TO CP GI PROCEDURES FUTURE CARE

Mar 28, 2019 PENDING WADE PARK SERVICES

A sample of the comma-delimited output is shown below.

"Type","Consult","Service Name","Status","Request Date","Patient Name","Grouper Name","Last Action"

"CLINICAL PROCEDURE","7826686","CP GI PROCEDURES FUTURE CARE","ACTIVE","Feb 04, 2019","XXXXX,E (1234)","WADE PARK SERVICES","ADDED COMMENT"

"CLINICAL PROCEDURE","7921753","CP GI PROCEDURES FUTURE CARE","PENDING","Mar 28, 2019","XXXXXX,E (9876)","WADE PARK SERVICES","PRINTED TO"

### ### Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integration Control Registrations (ICR)

N/A

#### Application Programming Interfaces

N/A

#### Remote Procedure Calls

N/A

#### HL7 Messaging

N/A

#### Web Services

N/A

### Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VistA users are required to observe VA rules of behavior regarding patient privacy and the security of patient information, VA computers, and VA networks.

#### Security Menus and Options

N/A

#### Security Keys and Roles

N/A

#### File Security

#### N/A

## EHM\*1\*15 – Automated Patient Discharge Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the night of cutover to Cerner, all inpatients are discharged out of VistA. EHM\*1\*15 supplies the Automated Patient Discharge Tool to identify and automatically discharge those patients. The patch is a component of the EHM Package. It is not nationally released.

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 33Table 17 lists the routines associated with the Automated Patient Discharge Tool software and their descriptions.

<span id="_Ref173224199" class="anchor"></span>Table 33: EHM\*1\*15 Routines

| ROUTINE NAME | ROUTINE DESCRIPTION                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EHMDISCH     | Code in this routine produces lists and summaries of patients eligible for discharge, controls automatic discharge of eligible patients and produces lists of patients automatically discharged.                                                             |
| EHMDGPMV     | This is a clone of DGPMV modified for automatic discharge. User interaction and code not relevant to the discharge process has been suppressed. A subroutine – DSC2CRNR – was added to the end to record that the patient has been automatically discharged. |
| EHMDGPMV1    | This is a clone of DGPMV1 modified for automatic discharge. User interaction and code not relevant to the discharge process has been suppressed.                                                                                                             |
| EHMDGPMV2    | This is a clone of DGPMV2 modified for automatic discharge. User interaction and code not relevant to the discharge process has been suppressed.                                                                                                             |
| EHMDGPMV3    | This is a clone of DGPMV3 modified for automatic discharge. User interaction and code not relevant to the discharge process has been suppressed.                                                                                                             |

3.1. PCE PATIENT CARE ENCOUNTER FILESPCE PATIENT CARE ENCOUNTER FILES

#### EHMDISCH

This routine contains code to generate a list of the patients eligible for discharge as well as produces a list or summary of those patients.

LIST – Subroutine to list patients eligible for discharge. The list is separated by institution and then sorted either by ward or patient name. Single institutions can be listed or all institutions with eligible patients can be included in the report. Transfer history is also displayed if requested.

LIST1 – TaskMan entry point for the list when queueing is selected.

HEADER – Subroutine to produce a header for lists.

SUMMARY – Subroutine to produce a summary report of patients eligible for discharge. The report is sorted by institution and then ward. Totals for the institution and for the station are produced as well.

SUMMARY1 – TaskMan entry point for the summary when queueing is selected.

DISCHARGE – Subroutine that controls the automatic discharging of eligible patients.

BLDLIST – Subroutine to generate a dataset of patients eligible for discharge in ^TMP(\$J). The code supports filtering for a single institution and sorting by ward or patient name. Transfer history is included in the dataset if the user requests it.

POSTLIST – Subroutine to produce alphabetic list of patients automatically discharged.

POSTLIST1 – TaskMan entry point for the discharged patient list when queueing is selected.

POSTHDR – Subroutine to produce a header for the discharged patient list.

PAGINATE – Subroutine to prompt the user when reports are printed to the screen.

CENTER – Function that returns centered text.

DASHES – Function that returns a string of dashes.

CONTINUE – Function that prompts to user to continue or not.

DATETIME – Function that formats a date/time in HH/MM/YY HH:MM format, zero-filled as required.

#### EHMDGPMV

This routine was cloned from DGPMV then modified to automatically discharge a patient by pre-setting required variables and by suppressing user interaction. The labels listed below were added to the routine after cloning.

ENTRY – This label was added at the top of the routine so the patient’s DFN could be passed in and to pre-set variables needed for automatic discharge processing.

DSC2CRNR – This subroutine stores the date/time automatic discharge processing completed in the Patient file (#2) in the DISCHARGED TO CERNER field (#9000).

#### EHMDGPMV1

This routine was cloned from DGPMV1 then modified to automatically discharge a patient by pre-setting required variables and by suppressing user interaction.

#### EHMDGPMV2

This routine was cloned from DGPMV2 then modified to automatically discharge a patient by pre-setting required variables and by suppressing user interaction.

#### EHMDGPMV3

This routine was cloned from DGPMV3 then modified to automatically discharge a patient by pre-setting required variables and by suppressing user interaction.

### Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 34 lists Automated Patient Discharge Tool options and their descriptions.

<span id="_Ref173224200" class="anchor"></span>Table 34: EHM\*1\*15 Options

| OPTION NAME         | DESCRIPTION                                            |
|-------------------------|------------------------------------------------------------|
| EHM_DISCHARGE MENU      | Main menu for the Patient Discharge Tool.                  |
| EHM_DISCHARGE LIST      | List patients eligible for discharge.                      |
| EHM_DISCHARGE PATIENTS  | Discharge eligible patients.                               |
| EHM_DISCHARGE POST-LIST | List patients automatically discharged.                    |
| EHM_DISCHARGE SUMMARY   | Produce summary report of patients eligible for discharge. |

### Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EHM DGPM DISCHARGE input template for the PATIENT MOVEMENT file (#405) was cloned from the DGPM DISCHARGE template. User interaction was suppressed and the discharge type set to REGULAR.

### Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integration Control Registrations (ICR)

N/A

#### Application Programming Interfaces

N/A

#### Remote Procedure Calls

N/A

#### HL7 Messaging

N/A

#### Web Services

N/A

### Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VistA users are required to observe VA rules of behavior regarding patient privacy and the security of patient information, VA computers, and VA networks.

#### Security Menus and Options

N/A

#### Security Keys and Roles

N/A

#### File Security

#### N/A

# Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routine Comparison

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routine comparison tool – CHECKSUMS^EHMUTILS – is used to identify which routines differ between two (2) systems. It also can identify routines that are present in one system and missing in the second. The tool is run separately in each system and then the output from them is loaded into a text comparison app such as Beyond Compare. The tool calculates the checksum for each selected routine and outputs it along with the date the routine was last modified (from line 1 of the routine) and the patch modification history (from line 2 of the routine). Differences in checksum values indicate if the routines are not the same. Last modified date and patch history are listed to assist with determining why the routines differ although a complete routine comparison may also be required. An example of the output of the routine comparison tool is shown below.

The routine comparison tool is contained in the CHECKSUMS subroutine in the EHMUTILS routine. Output of the tool is 132 characters wide. Note that it may be necessary to parcel the routine directory (e.g., by first letter or by package) into multiple runs as comparison apps are ineffective when the discrepancies are large. This occurs when, for example, one of the two systems has a large number of routines that the other does not.

Routine Comparison tool output

ROUTINE CHECKSUM LAST MODIFIED PATCH HISTORY

GMRCIAC1 B95622228 Mar 20, 2014 \*\*22,66,73,154\*\*

GMRCIAC2 B66788923 Feb 03, 2022 \*\*22,28,35,66,154,184\*\*

GMRCIAIT B9668267 Dec 18, 2002 \*\*30\*\*

GMRCIBKG B51788367 May 05, 2022 \*\*22,28,30,35,58,92,154,189\*\*

GMRCIBKM B13637196 Feb 14, 2002 \*\*22\*\*

GMRCIEHM B26831908 Dec 19, 2022 \*\*189\*\*

## FileMan File Comparison

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan File comparison tool – FILELIST^EHMUTILS – is used to identify which files differ between two (2) systems. It also can identify files that are present in one system and missing in the second. The tool is run separately in each system and then the output from them is loaded into a text comparison app such as Beyond Compare. The tool lists FileMan files in numerical order showing the file number, name and global where it is stored. An example of the output of the routine comparison tool is shown below.

FileMan File Comparison tool output

FILE NAME GLOBAL

------------ ------------------------------ ------------

.11 INDEX DD("IX",

.2 DESTINATION DIC(.2,

.31 KEY DD("KEY",

.4 PRINT TEMPLATE DIPT(

.401 SORT TEMPLATE DIBT(

.402 INPUT TEMPLATE DIE(

The routine comparison tool is contained in the FILELIST subroutine in the EHMUTILS routine.

## FileMan File and Field Comparison

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan File and Field comparison tool – FILES^EHMUTILS – is used to identify which files and fields differ between two (2) systems. It also can identify files and fields that are present in one system and missing in the second. The tool is run separately in each system and then the output from them is loaded into a text comparison app such as Beyond Compare. The tool lists FileMan files in numerical order showing the file number, name and global where it is stored. An example of the output of the routine comparison tool is shown below.

FileMan File Comparison tool output

FILE NAME GLOBAL FIELD NAME TYPE NODE;PIECE

------------ ------------------------------ ------------ -------- ------------------------------ -------- ----------

.11 INDEX DD("IX", .01 FILE RNJ20,7 0;1

.02 NAME RF 0;2

.1 DESCRIPTION .1101 .1;0

.01 DESCRIPTION W 0;1

.11 SHORT DESCRIPTION RF 0;3

.2 TYPE RS 0;4

.4 EXECUTION RS 0;6

.41 ACTIVITY FX 0;7

.42 USE S 0;14

The routine comparison tool is contained in the FILEFLDS subroutine in the EHMUTILS routine.

## Routine Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This tool – ROUTINE^EHMUTILS – generates text files for routines that can be uploaded to GitHub. Each routine is written to a file named \<ROUTINE NAME\>.m (e.g., EHMUTILS.m). The tool requires a file path where the text files are to be written. It can be invoked with the file path included, e.g.,

D ROUTINE^EHMUTILS(“/home/cle623”)

or without, i.e., D ROUTINE^EHMUTILS, and the user will be prompted for the file path.

## File Entry Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This tool – FILENTRY^EHMUTILS – generates text files for FileMan file entries that can be uploaded to GitHub. Each file entry is written to a file named \< FILEMAN FILE \>\_\<FILE ENTRY NAME\>.txt (e.g., 19_EHM MAIN MENU.txt). \<FILEMAN FILE\> is the number of the FileMan file. \<FILE ENTRY NAME\> is the .01 field of the entry in the FileMan file. The tool requires a FileMan file number and a file path where the text files are to be written. It can be invoked with the file number and path included, e.g.,

D FILENTRY^EHMUTILS(19,“/home/cle623”)

or without, i.e., D FILENTRY^EHMUTILS, and the user will be prompted for the file and the file path.

## ^DD Lister

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This tool – DDLIST^EHMUTILS – produces a data dictionary list of a FileMan file in the format required by GitHub. When prompted for “Global”, enter the “DD(“ followed by the file number, e.g., “DD(1609”. Do not include the leading up-arrow (“^”) nor the ending right parenthesis (“)”). Sample output is shown below.

^DD Lister Sample Output

CLE623\>D DDLIST^EHMUTILS

Global: DD(1609.1

DEVICE: HOME// HOME(CRT) Right Margin: 80//

^DD(1609.1,0)="FIELD^^1^2"

^DD(1609.1,0,"DT")="3230727"

^DD(1609.1,0,"IX","B",1609.1,.01)=""

^DD(1609.1,0,"NM","EHRM HL7 Message Retention")=""

^DD(1609.1,0,"VR")="1.0"

^DD(1609.1,0,"VRPK")="EHM"

^DD(1609.1,.01,0)="TYPE^RS^IFC:Inter-Facility Consult;PRF:Patient Record Flag;^0

;1^Q"

^DD(1609.1,.01,1,0)="^.1"

^DD(1609.1,.01,1,1,0)="1609.1^B"

^DD(1609.1,.01,1,1,1)="S ^EHMHL7(1609.1,"B",\$E(X,1,30),DA)="""

^DD(1609.1,.01,1,1,2)="K ^EHMHL7(1609.1,"B",\$E(X,1,30),DA)"

^DD(1609.1,.01,3)="Enter IFC or PRF."

^DD(1609.1,.01,21,0)="^^1^1^3221216^"

^DD(1609.1,.01,21,1,0)="This field stores the type of HL7 message - IFC or PRF."

^DD(1609.1,.01,"DT")="3230503"

^DD(1609.1,1,0)="RETENTION^NJ3,0^^0;2^K:+X'=X!(X\>999)!(X\<1)!(X?.E1"."1.N) X"

^DD(1609.1,1,3)="Enter number of days to retain messages, 1-999."

^DD(1609.1,1,21,0)="^^1^1^3221216^"

^DD(1609.1,1,21,1,0)="This field stores the number of days to retain HL7 message

s for each type."

^DD(1609.1,1,"DT")="3230503"

^DD(1609.1,"B","RETENTION",1)=""

^DD(1609.1,"B","TYPE",.01)=""

^DD(1609.1,"GL",0,1,.01)=""

^DD(1609.1,"GL",0,2,1)=""

^DD(1609.1,"IX",.01)=""

^DD(1609.1,"RQ",.01)=""

## Global Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This tool – GSEARCH^EHMUTILS – searches a global for a string of text. The subroutine is invoked with three (3) parameters:

> 1\. Global to be searched (e.g., ^DIC or ^DIC(19))

1.  String to be searched for (e.g., EHM MAIN MENU)
2.  1 if string to be searched for must match case, 0 if not (default=0)

The global name may be either at the root (e.g., ^DIC) or at the node level (e.g., ^DIC(19)). If a global is specified at the node level, the closing right parenthesis is required.

## Released Patch Comparison

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch comparison tool – PATCHES2^EHMUTILS – compares a list of released patches from the Compliance and Tracking Systems (CATS) web site against the site’s INSTALL file (#9.7). To use the tool, navigate to the CATS tool web site and list the released patches (Individual Patch Compliance Report All Regions). See Error! Reference source not found..

CATS Web Page

![](electronic-health-modernization-technical-manual/003.png)

Grab the patch data starting at the line below the headers and paste it into a text editor (see sample below). Save the file where the tool can access it.

9411 MAG\*3\*353 VISTA IMAGING MUMPS FIX 2024-01-24 2024-02-27 Yes

9407 RA\*5\*206 DIAGNOSTIC CODE UPDATES TO BI-RADS 2024-01-23 2024-02-26 Yes

9408 PXRM\*2\*85 SUPPORT FOR DIAGNOSTIC CODE UPDATES TO BI-RADS 2024-01-23 2024-02-26 Yes

9409 WV\*1\*32 SUPPORT FOR DIAGNOSTIC CODE UPDATES TO BI-RADS 2024-01-23 2024-02-26 Yes

9414 PSB\*3\*144 BCBU FUTURE TERMINATION DATE ISSUE 2024-01-25 2024-02-25 Yes

9415 WEBP\*1\*35 PCMM WEB DEFECT REMEDIATION AND LATENCY ADAPTIVE M 2024-01-25 2024-02-25 No

Invoke the tool, e.g., D PATCHES2^EHMUTILES(“/home/cle623”,”patches.txt”). Sample output is shown below.

Output of Patch Comparison Tool

PATCH DATE CATS SITE

HDS\*1.0\*75 2023-12-20 YES NO

EDP\*2.0\*29 2023-12-13 YES NO

KPAS\*1.0\*46 2023-12-06 YES NO

JLV\*3.0\*27 2023-12-05 YES NO

MHV\*1.0\*95 2023-12-15 YES NO

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc116559657" class="anchor"></span>Table 35: Glossary

| TERM | MEANING                                                      |
|----------|------------------------------------------------------------------|
| API      | Application Programming Interface                                |
| DICOM    | Digital Imaging and Communications in Medicine                   |
| EDIPI    | Electronic Data Interchange Personal Identifier                  |
| EHM      | Electronic Health Modernization                                  |
| EHRM     | Electronic Health Record Modernization                           |
| EHRM-IO  | Electronic Health Record Modernization Integration Office        |
| ESD      | Enterprise Service Desk                                          |
| HITT     | Health Informatics Transition Team                               |
| HL7      | Health Level Seven                                               |
| ICR      | Integration Control Registration                                 |
| IFC      | Inter-Facility Consult                                           |
| IOC      | Initial Operating Capability                                     |
| IV&V     | Independent Validation and Verification                          |
| OIT      | Office of Information Technology                                 |
| PACS     | Picture Archiving and Communication System                       |
| PRF      | Patient Record Flag                                              |
| SOP      | Service Object Pair                                              |
| UID      | Unique Identifier                                                |
| VA       | Department of Veterans Affairs                                   |
| VistA    | Veterans Health Information Systems and Technology Architecture. |