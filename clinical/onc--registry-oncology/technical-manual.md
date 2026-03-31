---
title: Oncology Version 2.2 Technical Manual and Package Security Guide (Updated ONC*2.2*22)
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: and Package Security Guide (Updated ONC*2.2*22)
app_code: ONC
app_name: "Registry: Oncology"
section: CLI
app_status: active
pkg_ns: ONC
patch_ver: 2.2
patch_id: ONC*2.2
group_key: "ONC:ONC:2.2"
file_numbers: 
  - 164
security_keys: []
menu_options: 3
description: ![](oncology-version-2-2-technical-manual-and-package-security-guide-updated-onc-2-2/001.png)
audience: 
keywords: 
  - onco
  - oncology
  - table
  - contents
  - class
  - site
  - contains
  - codes
  - routines
  - over
page_count: 0
word_count: 6109
section_count: 14
table_count: 5
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: JUNE 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Oncology/onc_2_2_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Oncology/onc_2_2_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=81"
---

ONCOLOGY (ONC)TECHNICAL MANUALANDPACKAGE SECURITY GUIDE

![](oncology-version-2-2-technical-manual-and-package-security-guide-updated-onc-2-2/001.png)

JUNE 2014

(Revised September 2025)

Office of Information and Technology (OI&T)

Enterprise Program Management Office

  
Revision History

When updates occur, the Title Page lists the new revised date, and this page describes the changes. Bookmarks link the described content changes to its place within manual. There are no bookmarks for format updates. Page numbers change with each update; therefore, they are not included as a reference in the Revision History.

<table>
<caption>Revision History TableRevision History Table</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 35%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Patch</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>September 2025</td>
<td>ONC*2.2*22</td>
<td><u>Routines</u></td>
</tr>
<tr class="even">
<td>March 2025</td>
<td>ONC*2.2*21</td>
<td><p><u>Routines</u></p>
<p><u>Files</u></p>
<p><u>Templates</u></p></td>
</tr>
<tr class="odd">
<td>September 2024</td>
<td>ONC*2.2*20</td>
<td><u>Routines</u></td>
</tr>
<tr class="even">
<td>June 2024</td>
<td>ONC*2.2*19</td>
<td><p><u>Routines</u></p>
<p>Table of Contents</p>
<p><u>Files</u></p>
<p><u>Exported Options</u></p>
<p><u>Technical Routines</u></p>
<p><u>Templates</u></p></td>
</tr>
<tr class="odd">
<td>November 2023</td>
<td>ONC*2.2*18</td>
<td><p><u>Routines</u></p>
<p>Table of Contents</p></td>
</tr>
<tr class="even">
<td>June 2023</td>
<td>ONC*2.2*17</td>
<td><p><u>Routines,</u></p>
<p><a href="#exported-options">Exported Options</a><u>,</u></p>
<p>Table of Contents</p></td>
</tr>
<tr class="odd">
<td>April 2023</td>
<td>ONC*2.2*16</td>
<td><p><u>Routines</u></p>
<p>Table of Contents</p></td>
</tr>
<tr class="even">
<td>October 2022</td>
<td>ONC*2.2*15</td>
<td><p><u>Routines</u></p>
<p>Table of Contents</p></td>
</tr>
<tr class="odd">
<td>March 2022</td>
<td>ONC*2.2*14</td>
<td><p>New pre and post installation routines for Patch ONC*2.2*14</p>
<p><u>Routines,</u></p>
<p><a href="#security-features">Technical References</a></p>
<p>Table of Contents</p></td>
</tr>
<tr class="even">
<td>December 2021</td>
<td>ONC*2.2*13</td>
<td><p>New routines and files for changes related to NAACCR Standards Vol II Version 2021 Metafile 21B <u>Files, File Descriptions, Routines</u></p>
<p>Table of Contents</p></td>
</tr>
<tr class="odd">
<td>October 2020</td>
<td>ONC*2.2*12</td>
<td><p>New routines for changes related to NAACCR Standards Vol II Version 2018 Metafile 18D <a href="#routines-1">Routines</a></p>
<p>Templates, Table of Contents</p></td>
</tr>
<tr class="even">
<td>April 2020</td>
<td>ONC*2.2*10</td>
<td><p><u>Files, File Descriptions, Routines</u></p>
<p>New fields, files and routines for changes related to NAACCR Standards Vol II Version 2018 and AJCC 8<sup>TH</sup> Edition Staging</p></td>
</tr>
<tr class="odd">
<td>September 2017</td>
<td>ONC*2.2*6</td>
<td><p><u>Files, File Descriptions, Routines</u></p>
<p>ONCOLOGY STAGED BY CODES (#165.7) added to Files Section, Package Default Definition, and File Security.  Added information about upgrading NAACCR Versions in Appendix A.</p>
<p>ROUTINES updated to include current ONC ROUTINES.</p></td>
</tr>
</tbody>
</table>

Revision History TableRevision History Table

# # # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# # Introduction](#introduction)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Implementation](#implementation)
    - [Oncology Namespace](#oncology-namespace)
    - [File Numbering](#file-numbering)
    - [Global](#global)
    - [Routines](#routines)
    - [Security Keys](#security-keys)
    - [Option Delegation](#option-delegation)
    - [Site Parameters](#site-parameters)
  - [Maintenance](#maintenance)
    - [Oncology Site Manager Menu](#oncology-site-manager-menu)
- [Files](#files)
  - [File Descriptions](#file-descriptions)
  - [Package Default Definition](#package-default-definition)
- [Routines](#routines-1)
- [Templates](#templates)
  - [INPUT TEMPLATES](#input-templates)
  - [PRINT TEMPLATES](#print-templates)
  - [SORT TEMPLATES](#sort-templates)
- [Exported Options](#exported-options)
  - [Site Manager Menu](#site-manager-menu)
- [Archiving and Purging](#archiving-and-purging)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
  - [DBIA Subscriber Package Agreements](#dbia-subscriber-package-agreements)
  - [DBIA Custodial Package Agreements](#dbia-custodial-package-agreements)
- [Internal Relations](#internal-relations)
- [Package-Wide Variables](#package-wide-variables)
- [Software Product Security](#software-product-security)
  - [Security Management](#security-management)
  - [Privacy Act Statement](#privacy-act-statement)
  - [Security Features](#security-features)
- [Appendix A – Upgrading NAACCR Versions](#appendix-a-upgrading-naaccr-versions)
- [Glossary](#glossary)
The VA Automated Tumor Registry for Oncology is written in standard M and VA FileMan. This package has four unique files: the Site-Group for Oncology file, the AJCC Staging Groups file, and the ICDO Topography, and ICDO Morphology files. These files are tied together to create site-specific topography, morphology, and extent of disease coding as defined in the Surveillance, Epidemiology, and End Results Reporting (SEER) Program, the American College of Surgeons (ACOS) cancer-directed codes, and the conventions of the AJCC TNM coding schemes. Once a general site group is selected, all related relevant codes are available as on-line help to the user, reducing the possibility of coding errors.
Additional features include automatic case finding that identifies patients diagnosed with malignancies and the ability to document follow-up (required annually by the ACOS) and track delinquent follow-up cases.
Users may generate several reports for running the registry by using the Registry Lists, Annual Reports, and Statistical Reports modules.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Oncology Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace ONC is assigned to all menus and options of Tumor Registry. All Oncology routines and globals start with these characters.

All Oncology compiled template routines begin with the ONCO namespace, followed by the X\*, Y\*, and W\* characters.

### File Numbering

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Oncology is assigned Files \#160 through \#160.99 and files \#164 through \#169.99.

### Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Oncology uses the ^ONCO global to store all files. Journaling is recommended on this global.

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routine mapping is not necessary for any Oncology routines.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no security keys used in the Oncology package.

### Option Delegation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Give the Oncology Site Manager Menu \[ONCO \#SITE MANAGER MENU\] to the IRM staff or package ADPAC.

Give the DHCP Tumor Registry menu \[ONCO \* TUMOR REGISTRY MENU\] to Tumor Registry users.

### Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Define Tumor Registry Parameters \[ONCO UTIL-SITE PARAMETERS\] option is located under the user's Utility Options \[ONCO UTIL MENU\] within the DHCP Tumor Registry menu \[ONCO \*TUMOR REGISTRY MENU\]. The option can be populated by the Tumor Registrars. (See the user manual for details.)

## Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Oncology Site Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Oncology Site Manager Menu option should be assigned to the IRM specialist responsible for Oncology. Below is a description of each of the menu's functions:

#### DHCP Tumor Registry \[ONCO\*TUMOR REGISTRY MENU\]

> This is the main menu of the Oncology Tumor Registry module. At present it has seven menu items consisting of the functions of the Tumor Registry. These are Suspense, Abstracting, Lists, Follow‑up, Annual Reporting, Statistics, and Utilities.

#### Correct Next Follow‑Up for Expired Patients \[ONCO \#SITE-FIX EXP PAT F/U\]

> This option searches all FOLLOW‑UP multiples (#400) on the Oncology Patient file (#160) looking for expired patients. It then makes sure that the NEXT FOLLOW‑UP METHOD sub‑field (#6) is set to "9" (not followed).

#### Recompute AJCC TNM Staging \[ONCO \#SITE-RESTAGE PRIMARY\]

> This option is no longer available.

#### Purge Patient Records with No Suspense/Primaries \[ONCO \#SITE-PURGE SUSPENSE\]

> This option drives through the Oncology Patient file (#160) looking for records that have no suspense date and no associated primaries. Upon confirmation from the user, it deletes these records from the file.

#### Create a report to preview ACOS output \[ONCO \#SITE-CREATE ACOS REPORT\]

This is a report which allows the tumor registrar to preview the contents of the specified accessions intended for output to the ACOS disk. This option is independent of the disk capture function but uses the precise database selection criteria. This option is also found under the Utility Options.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three (3) Oncology files which contain data relevant to the cancer patient: the Oncology Patient file (#160), the Oncology Primary file (#165.5), and the Oncology Contact file (#165). These are used extensively in the Annual and Statistical Reports menus.

> The Oncology Patient file is a variable pointer file, which points to both the VISTA Patient file (#2) and the Referral Patient file (#67) (for deceased patients). It contains data relative to the patient's demographics. The data does not change with each cancer. Fields that have ACOS specific codes, such as race, ethnicity, and place of birth, are converted and stored in this file. Patient history relevant to cancer (e.g., alcohol and tobacco, occupation, and family cancer history), as well as follow-up history, reside in this file.

> The Oncology Primary file, or "cancer-case" file, contains all the cancer cases in the registry. There is a backwards pointer to the Oncology Patient file with a many-to-one relationship between cancers and patient. Data elements in this file uniquely define the tumor, the extent of disease, first course of treatment accorded, and all recurrence information. Pointers to the Oncology coding data files containing all codes pertinent to the definition of the tumor are widely used.

> The Oncology Contact file holds all patient contact information and is used in conjunction with the Follow-up Form Letter file and the Oncology Site Parameters file to produce professional quality letters on either a dot matrix or laser printer.

## File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>FILE DESCRIPTIONFILE DESCRIPTION</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 12%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Number</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ONCOLOGY PATIENT</td>
<td>160</td>
<td>Demographic and follow-up data concerning Oncology patients is stored in this file. (Tumor-related data is stored in the Primary file). Data is NOT exported with this file. The file is populated on site.</td>
</tr>
<tr class="even">
<td>ONCOLOGY SITE PARAMETERS</td>
<td>160.1</td>
<td>This file contains fields unique to the facility. They are used in follow-up and enable ACOS reporting. Data is input at the facility by the user and should be the first file that is populated before any other data is collected.</td>
</tr>
<tr class="odd">
<td>TYPE OF RECURRENCE</td>
<td>160.12</td>
<td>This file contains types of recurrence. The term "recurrence" defines the return or reappearance of the cancer after a disease-free intermission or remission.</td>
</tr>
<tr class="even">
<td>NON CANCER-DIRECTED SURGERY</td>
<td>160.14</td>
<td>This file contains surgical procedures that are performed to diagnose/stage disease (exploratory) or relieve symptoms (palliative).</td>
</tr>
<tr class="odd">
<td>ACOS STATE AT DIAGNOSIS</td>
<td>160.15</td>
<td>This file contains the states and Canadian provinces used for the patient's usual residence when the tumor was diagnosed and treated.</td>
</tr>
<tr class="even">
<td>ONCOLOGY DATA EXTRACT FORMAT</td>
<td>160.16</td>
<td>This file contains the Oncology Data Extract Formats.</td>
</tr>
<tr class="odd">
<td>ONCOLOGY PCE EXTRACT FORMAT</td>
<td>160.17</td>
<td>This file contains the Oncology PCE Extract Formats.</td>
</tr>
<tr class="even">
<td>FACILITY</td>
<td>160.19</td>
<td>This file contains 5000+ medical locations (American College of Surgeons identification number) nationwide.</td>
</tr>
<tr class="odd">
<td>FORMS/INSTRUCTIONS</td>
<td>160.2</td>
<td>This file contains forms used by the Tumor Registry as well as on-line instructions for procedures that must be followed such as making a disk for ACOS.</td>
</tr>
<tr class="even">
<td>PRIMARY PAYER AT DIAGNOSIS</td>
<td>160.3</td>
<td>This file contains the patients' primary payor/insurance carriers at the time of initial diagnosis and/or treatment. The file is populated at the site.</td>
</tr>
<tr class="odd">
<td>RECONSTRUCTIVE SURGERY</td>
<td>160.4</td>
<td>This file contains types of reconstructive surgery. Reconstructive surgery reconstructs, restores, or improves the shape and appearance or function of body structures that are missing, defective, damaged, or misshapen by cancer or cancer-directed therapies. Reconstruction may be a part of the first course of therapy or may be done after the first course is completed.</td>
</tr>
<tr class="even">
<td>SURGICAL APPROACH</td>
<td>160.6</td>
<td>This file contains surgical approaches. The data is used to record information on the increasing use of less invasive procedures. The data will make possible a comparative analysis of traditional and laparoscopic approaches.</td>
</tr>
<tr class="odd">
<td>ICDO TOPOGRAPHY</td>
<td>164</td>
<td>This file contains the Complete ICDO-2 Topography, with site specific coding for Extent of Disease and AJCC Staging. This file comes with data, which overwrite the site’s data. It is not recommended that sites modify this file.</td>
</tr>
<tr class="even">
<td>ICDO-SITES</td>
<td>164.08</td>
<td>This file contains the parent ICDO-2 Groups for the ICDO-2 Topography codes. It is pointed to by File #164, providing a simple list of code groups.</td>
</tr>
<tr class="odd">
<td>ICD-O-2 MORPHOLOGY</td>
<td>164.1</td>
<td>This file contains the World Health Organization's International Classification of Diseases-Oncology codes including /2's. This file comes with data, which overwrite the site’s data. It is not recommended that sites modify this file.</td>
</tr>
<tr class="even">
<td>ICDO SITE GROUPS FOR REPORTING</td>
<td>164.14</td>
<td>This file, pointed to by the ICDO-SITES file (#164.08), facilitates the production of the Annual Registry Summary Report. This file comes with data, which overwrite the site's data. It is not recommended that sites modify this file.</td>
</tr>
<tr class="odd">
<td>TUMOR MARKERS</td>
<td>164.15</td>
<td>This file contains the set of codes used by the <em>ACOS Commission on Cancer Data Acquisition Manual</em> to record the use of tumor markers in tracking neoplasms of the breast. This file comes with data, which overwrite the site's data. It is not recommended that sites modify this file.</td>
</tr>
<tr class="even">
<td><p>KARNOFSKY’S RATING</p>
<p>CHEMOTHERAPEUTIC DRUGS</p>
<p>SITE-GROUP FOR ONCOLOGY</p></td>
<td><p>164.17</p>
<p>164.18</p>
<p>164.2</p></td>
<td><p>This file lists the physical conditions of patients prior to the beginning of</p>
<p>initial treatment using Karnofsky's Rating.</p>
<p>Chemotherapeutic drugs as listed in SEER SELF-INSTRUCTIONAL MANUAL FOR TUMOR</p>
<p>REGISTRARS Book 8 - ANTINEOPLASTIC DRUGS Third Edition</p>
<p>This file contains major site-groups for the Oncology package. It contains all the ACOS Site-Specific Surgery Codes. In addition, it also contains the SEER Extension and Lymph node coding - sharing that function with File #164. The "F" cross-reference of the TOPOGRAPHY field (#.01) of the TOPOGRAPHY multiple (#10) sets an index under ^ONCO(164.2,"F"). An index under ^ONCO(164.2,"G") is set by both the "G" cross-reference of the ICDO-1 TOPOGRAPHY field (#.02) of the TOPOGRAPHY multiple (#10), and by the "AC" cross-reference of the TOPOGRAPHY field (#.01) of the TOPOGRAPHY multiple (#10) of the ICDO-1 Site For Oncology file (#169.2).</p></td>
</tr>
<tr class="odd">
<td>OTHER STAGING FOR ONCOLOGY</td>
<td>164.3</td>
<td>This file contains other methods of staging for particular sites. Data comes with the file and will overwrite data in field.</td>
</tr>
<tr class="even">
<td>AJCC STAGING GROUPS</td>
<td>164.33</td>
<td>This file contains the AJCC Staging Groups and the TNM coding schema. This file should not be modified.</td>
</tr>
<tr class="odd">
<td>COMMON CANCERS</td>
<td>164.4</td>
<td>This file contains a list of common cancers (data file).</td>
</tr>
<tr class="even">
<td>PRIMARY CANCER STATUS CODE</td>
<td>164.42</td>
<td>This file contains a superset of the DAM Cancer Status Codes for use in identifying tumor status at follow-up on the Oncology Primary file (#165.5).The extended codes (4-7) help the registrar to record more completely the overall cancer status of an expired patient. This file comes with data, which overwrite the site's data. It is not recommended that sites modify this file. This file is referenced directly by routine ONCOCOFA.</td>
</tr>
<tr class="odd">
<td>GRADE</td>
<td>164.43</td>
<td>This file contains codes used to record the grade of tumor in the GRADE field (#24) of the Oncology Primary file (#165.5). This file comes with data, which overwrite the site's data. It is not recommended that sites modify this file.</td>
</tr>
<tr class="even">
<td><p>ONCOLOGY GRADE TABLES</p>
<p>AJCC STAGE GROUP</p></td>
<td><p>164.44</p>
<p>164.45</p></td>
<td><p>This file contains the Grade Codes for the Grade Clinical, Grade Pathologic, Grade Post-Therapy (yc) and Grade Post Therapy (yp) fields.</p>
<p>This file contains transforms for converting AJCC stage data from internal to external format and vice versa. This file comes with data, which overwrite the site's data. It is not recommended that sites modify this file. This file is referenced directly by routine ONCOTNS.</p></td>
</tr>
<tr class="odd">
<td>RACE CODE FOR ONCOLOGY</td>
<td>164.46</td>
<td>This file contains codes used to record the patient's race in the RACE field (#8) of the Oncology Patient file (#160). The codes are derived from the ACOS Data Acquisition Manual. This file comes with data, which overwrite the site's data. It is not recommended that sites modify this file.</td>
</tr>
<tr class="even">
<td>ONCOLOGY SCHEMA DISCRIMINATOR CODES</td>
<td>164.47</td>
<td>This file contains the Schema Discriminator 1, 2 and 3 codes used by NAACCR.</td>
</tr>
<tr class="odd">
<td>SEER CODE SET</td>
<td>164.5</td>
<td>This file contains extension, lymph node, and surgery codes from the SEER Extent of Disease Codes and Coding Instructions. Each set of codes can be linked to code sets from future editions. This file is referenced directly by routines ONCODEL (for extension and lymph node codes) and ONCODSR (for surgery codes). This file comes with data, which overwrite the site's data. It is not advised that sites modify this file.</td>
</tr>
<tr class="even">
<td><p>ONC CS SITE-SPECIFIC FACTORS</p>
<p>TYPE OF STAGING SYSTEM (PEDIATRIC)</p></td>
<td><p>164.52</p>
<p>164.6</p></td>
<td><p>Identifies additional information needed to generate stage, or prognostic</p>
<p>factors that have an effect on stage or survival.</p>
<p>The Commission requires staging of pediatric patients using AJCC or the staging criteria of the pediatric intergroup studies and the pediatric cooperative groups.</p></td>
</tr>
<tr class="odd">
<td>RADIATION TREATMENT VOLUME</td>
<td>164.7</td>
<td>This file contains the radiation treatment volume codes.</td>
</tr>
<tr class="even">
<td>RADIATION COMPLETION STATUS</td>
<td>164.8</td>
<td>This file contains radiation completion statuses.</td>
</tr>
<tr class="odd">
<td><p>ONCO RADIATION EXTERNAL BEAM</p>
<p>ONCO RADIATION TREATMENT VOLUME</p>
<p>ONCO RADIATION TO DRAINING LN</p>
<p>ONCO RADIATION TREATMENT MODALITY</p>
<p>WHO HISTOLOGICAL CLASSIFICATION</p>
<p>ONCOLOGY CONTACT</p></td>
<td><p>164.81</p>
<p>164.82</p>
<p>164.83</p>
<p>164.84</p>
<p>164.9</p>
<p>165</p></td>
<td><p>This file contains the codes and descriptions used for the NAACCR Phase I, II and III Radiation External Beam Planning fields.</p>
<p>This file contains the codes and descriptions used for the NAACCR Phase I, II and III Radiation Treatment Volume fields.</p>
<p>This file contains the codes and descriptions used for the NAACCR Phase I, II and III Radiation to Draining Lymph Node fields.</p>
<p>This file contains the codes and descriptions used for the NAACCR Phase I, II and III Radiation Treatment Modality fields.</p>
<p>This file contains the WHO histological classification of tumor codes for</p>
<p>tumors of the brain and central nervous system.</p>
<p>This file contains Oncology contacts. It is populated by the user and, in some part, automatically by the Follow-up options. It is used only for patient follow-up.</p></td>
</tr>
<tr class="even">
<td>FOLLOW-UP FORM LETTER</td>
<td>165.1</td>
<td>This file contains the form letters used for Oncology/Tumor Registry follow-up. These are linked by type to the Contact file.</td>
</tr>
<tr class="odd">
<td>GEOCODES</td>
<td>165.2</td>
<td>This file contains codes for states of the United States and foreign countries.</td>
</tr>
<tr class="even">
<td><p>CLASS OF CASE</p>
<p>ONCOLOGY PRIMARY</p></td>
<td><p>165.3</p>
<p>165.5</p></td>
<td><p>For a hospital registry, Class of Case divides cases into two groups.</p>
<p>Analytic cases (codes 00-22) are those that are required by CoC (Commission on</p>
<p>Cancer) to be abstracted because of the program's primary responsibility in</p>
<p>managing the cancer. Analytic cases are grouped according to the location of</p>
<p>diagnosis and treatment. Treatment and outcome reports may be limited to</p>
<p>analytic cases.</p>
<p>Nonanalytic cases (codes 30-49 and 99) may be abstracted by the facility to</p>
<p>meet central registry requirements or because of a request by the facility's</p>
<p>cancer program.</p>
<p>Tumor-related data for Oncology patients is stored in this file. (Demographic and follow-up data is in the Oncology Patient file). This file is populated in the field by using the abstracting options.</p></td>
</tr>
<tr class="odd">
<td><p>CONVERSION FLAGS</p>
<p>COMPUTED PRIMARY</p></td>
<td><p>165.55</p>
<p>165.59</p></td>
<td><p>Identifies the regional lymph nodes involved with cancer at the time of</p>
<p>diagnosis.</p>
<p>This file is tied to the Oncology Primary file (DINUMed to .01 field) and contains computed fields only. This can be used by IRM to add computed fields to the file for use in the statistical options for cross-tabulation routines.</p></td>
</tr>
<tr class="even">
<td>ONCOLOGY STAGED BY CODES</td>
<td>165.7</td>
<td>For a hospital registry, Primary Abstract cases need to record the person or group who assigned the clinical and pathologic staging items. This file contains the applicable numeric codes to use for recording the value for each case and the label (description) for each code.</td>
</tr>
<tr class="odd">
<td><p>ONCO AJCC STAGING CHAPTERS</p>
<p>ONCOLOGY EOD SCHEMAS</p>
<p>CASEFINDING SOURCE</p>
<p>BLADDER PHYSICIAN SPECIALTY</p>
<p>REGIONAL TREATMENT MODALITY</p>
<p>ONCOLOGY SUBSITE</p></td>
<td><p>165.8</p>
<p>165.9</p>
<p>166</p>
<p>166.12</p>
<p>166.13</p>
<p>166.3</p></td>
<td><p>This file contains the T, N and M codes as well as the T and N suffixes and AJCC Chapter and Name for the AJCC Cancer Staging Manual 8<sup>th</sup> Edition and beyond.</p>
<p>This file contains the site-specific codes and descriptions for the SEER EOD (Extent of Disease) data items.</p>
<p>This file is intended to assist the registrar in coding the source that first identified the tumor.</p>
<p>This file contains a list of managing physician specialties. The file is used</p>
<p>for the Patient Care Evaluation Study of Cancers of the Urinary Bladder form.</p>
<p>REGIONAL TREATMENT MODALITY is intended to identify the dominant modality of</p>
<p>therapy delivered to the primary volume of interest.</p>
<p>This file supports the 1996 Patient Care Evaluation of Soft Tissue Sarcoma.</p></td>
</tr>
<tr class="even">
<td><p>HEMATOLOGIC TRANSPLANT/ENDOCRINE PROCEDURES</p>
<p>ONCO BRAIN MOLECULAR MARKERS</p>
<p>GLEASON PATTERNS</p>
<p>ONCO LN STATUS</p>
<p>ONCO PERIPHERAL BLOOD INVOLVEMENT</p>
<p>ONCO RESIDUAL TUMOR VOLUME</p>
<p>ONCO NEOADJUVANT THERAPY TREATMENT EFFECT</p>
<p>ONCO HPV STATUS</p>
<p>TYPE OF REPORTING SOURCE</p>
<p>TYPE OF MULTIPLE TUMORS</p></td>
<td><p>167</p>
<p>167.1</p>
<p>167.2</p>
<p>167.3</p>
<p>167.4</p>
<p>167.5</p>
<p>167.6</p>
<p>167.7</p>
<p>168</p>
<p>169</p></td>
<td><p>Identifies systemic therapeutic procedures administered as part of the first</p>
<p>course of treatment at this and all other facilities. If none of these procedures were administered, then this item records the reason they were not</p>
<p>performed. These include bone marrow transplants, stem cell harvests, surgical</p>
<p>and/or radiation endocrine therapy.</p>
<p>For further information see FORDS pages 182-183.</p>
<p>This file contains the codes and descriptions for the NAACCR Brain Molecular Marker field.</p>
<p>This file contains the codes and descriptions for the NAACCR Gleason Patterns Clinical and Gleason Patterns Pathological fields.</p>
<p>This file contains the codes and descriptions for the NAACCR Lymph Node Status Fem-Ing, Par-Aor, PLVfield.</p>
<p>This file contains the codes and descriptions for the NAACCR Peripheral Blood Involvement field.</p>
<p>This file contains the codes and descriptions for the NAACCR Residual Tumor Volume field.</p>
<p>This file contains the codes and descriptions for the NAACCR Neoadjuvant Therapy – Treatment Effect field.</p>
<p>This file contains the HPV STATUS codes and descriptions for use with the SEER Site Specific Fact 1 NAACCR Data element.</p>
<p>This file is intended to assist the registrar in coding the source of documents used to abstract the cancer being reported.</p>
<p>This file is used to identify the type of multiple tumors that are abstracted</p>
<p>as a single primary.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>ICD-O-3 MORPHOLOGY</p>
<p>ONCOLOGY PACKAGE STATUS</p></td>
<td><p>169.3</p>
<p>169.99</p></td>
<td><p>This file contains the International Classification of Diseases for Oncology,</p>
<p>Third Edition (ICD-O-3) morphology codes and code descriptions.</p>
<p>This file allows the storage of the status of the package under control of the programmer: version installed, beginning, and ending of the installation, with the generation of a mail-message to the installer, and supporting ISC the installation information.</p></td>
</tr>
</tbody>
</table>

FILE DESCRIPTIONFILE DESCRIPTION

## Package Default Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# NAME DD CODE W/FILE DATA PTS RIDE

160 ONCOLOGY PATIENT YES YES NO

160.1 ONCOLOGY SITE PARAMETERS YES YES NO

160.12 TYPE OF RECURRENCE YES YES YES OVER YES NO

160.14 NON CANCER-DIRECTED SURGERY YES YES YES OVER YES NO

160.15 ACOS STATE AT DIAGNOSIS YES YES YES OVER YES NO

160.16 ONCOLOGY DATA EXTRACT FORMAT YES YES YES OVER YES NO

160.17 ONCOLOGY PCE EXTRACT FORMAT YES YES YES OVER YES NO

160.19 FACILITY YES YES YES OVER YES NO

160.2 FORMS/INSTRUCTIONS YES YES YES OVER YES NO

160.3 PRIMARY PAYER AT DIAGNOSIS YES YES YES OVER YES NO

160.4 RECONSTRUCTIVE SURGERY YES YES YES OVER YES NO

160.6 SURGICAL APPROACH YES YES YES OVER YES NO

164 ICDO TOPOGRAPHY YES YES YES OVER YES NO

164.08 ICDO-SITES YES YES YES OVER YES NO

164.1 ICD-O-2 MORPHOLOGY YES YES YES OVER YES NO

164.14 ICDO SITE GROUPS FOR REPORTING YES YES YES OVER YES NO

164.15 TUMOR MARKERS YES YES YES OVER YES NO

164.17 KARNOFSKY’S RATING

164.18 CHEMOTHERAPEUTIC DRUGS

164.2 SITE-GROUP FOR ONCOLOGY YES YES YES OVER YES NO

164.3 OTHER STAGING FOR ONCOLOGY YES YES YES OVER YES NO

164.33 AJCC STAGING GROUPS YES YES YES OVER YES NO

164.4 COMMON CANCERS YES YES YES OVER YES NO

164.42 PRIMARY CANCER STATUS CODE YES YES YES OVER YES NO

164.43 GRADE YES YES YES OVER YES NO

164.45 AJCC STAGE GROUP YES YES YES OVER YES NO

164.46 RACE CODE FOR ONCOLOGY YES YES YES OVER YES NO

164.5 SEER CODE SET YES YES YES OVER YES NO

164.52 ONC CS SITE-SPECIFIC FACTORS

164.6 TYPE OF STAGING SYSTEM YES YES YES OVER YES NO

(PEDIATRIC)

164.7 RADIATION TREATMENT VOLUME YES YES YES OVER YES NO

164.8 RADIATION COMPLETION STATUS YES YES YES OVER YES NO

164.81 ONCO RADIATION EXTERNAL BEAM

164.82 ONCO RADIATION TREATMENT VOLUME

164.83 ONCO RADIATION TO DRAINING LN

164.84 ONCO RADIATION TREATMENT MODALITY

164.9 WHO HISTOLOGICAL CLASSIFICATION

165 ONCOLOGY CONTACT YES YES NO

165.1 FOLLOW-UP FORM LETTER YES YES YES OVER YES NO

165.2 GEOCODES YES YES YES OVER YES NO

165.3 CLASS OF CASE

165.5 ONCOLOGY PRIMARY YES YES NO

165.55 CONVERSION FLAGS

165.59 COMPUTED PRIMARY YES YES NO

165.7 ONCOLOGY STAGED BY CODES YES YES YES REPL NO NO

165.8 ONCO AJCC STAGING CHAPTERS

165.9 ONCOLOGY EOD SCHEMAS

166 CASEFINDING SOURCE

166.12 ONCOLOGY SUBSITE

166.13 REGIONAL TREATMENT MODALITY YES YES YES OVER YES NO

166.3 ONCOLOGY SUBSITE YES YES YES OVER YES NO

167 HEMATOLOGIC TRANSPLANT/

ENDOCRINE PROCEDURES

167.1 ONCO BRAIN MOLECULAR MARKERS

167.2 GLEASON PATTERNS

167.3 ONCO LN STATUS

167.4 ONCO PERIPHERAL BLOOD INVOLVEMENT

167.5 ONCO RESIDUAL TUMOR VOLUME

167.6 ONCO NEOADJUVANT TX EFFECT

167.7 ONCO HPV STATUS

168 TYPE OF REPORTING SOURCE

169 TYPE OF MULTIPLE TUMORSYES YES YES OVER YES NO

169.3 ICD-O-3 MORPHOLOGY

169.99 ONCOLOGY PACKAGE STATUS YES YES NO

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can get a listing of the routines by using the First Line Routine Print option located in the Routine Tools menu.

ONC2CNV ONC2PR12 ONC2PR13 ONC2PR14 ONC2PR15 ONC2PR16 ONC2PR17 ONC2PR18 ONC2PS01 ONC2PS04 ONC2PS05 ONC2PS06 ONC2PS09 ONC2PS10 ONC2PS12 ONC2PS13 ONC2PS14 ONC2PS15 ONC2PS16 ONC2PS17 ONC2PS18 ONC2PR19 ONC2PR20 ONC2PR21 ONC2PR22 ONC2PS22 ONC2PS1A ONC2PS21 ONC2PS4A ONC2PSTN

\*ONC2PR\*,\*ONC2PS\* routines may have been optionally deleted

ONCACD0 ONCACD1 ONCACDU1 ONCACDU2 ONCASCI ONCATF ONCATF1 ONCATF2 ONCBPC0 ONCBPC1 ONCBPC2 ONCBPC3 ONCBPC4 ONCBPC4A ONCBPC5 ONCBPC6 ONCBPC8 ONCBPC8A ONCBRP0 ONCBRP1 ONCBRP2 ONCBRP3 ONCBRP4 ONCBRP5 ONCBRP5A ONCBRP6 ONCBRP7 ONCBRP9 ONCBRP9A ONCBRP9B ONCCPC0 ONCCPC1 ONCCPC2 ONCCPC3 ONCCPC4 ONCCPC4A ONCCPC5 ONCCPC6 ONCCPC7 ONCCPC9 ONCCPC9A ONCCPC9B ONCCS ONCCS2 ONCCS3 ONCCSOT ONCCSRS ONCCSRS1 ONCCSSTF ONCCSV2 ONCCSV2A ONCDTUTL ONCDTX ONCDTX1 ONCEDIT ONCEDIT2 ONCEECA ONCFUNC ONCGENED ONCGPC0 ONCGPC1 ONCGPC2 ONCGPC3 ONCGPC4 ONCGPC5 ONCGPC7 ONCGPC7A ONCGPC7B ONCHPC0 ONCHPC1 ONCHPC2 ONCHPC2A ONCHPC3 ONCHPC4 ONCHPC4A ONCHPC5 ONCHPC6 ONCHPC8 ONCHPC8A ONCHTWT ONCIPC0 ONCIPC1 ONCIPC2 ONCIPC2A ONCIPC3 ONCIPC3A ONCIPC3B ONCIPC3C ONCIPC4 ONCIPC5 ONCIPC6 ONCIPC8 ONCIPC8A ONCIPC8B ONCIPC8C ONCLNG ONCLNG1 ONCLPC0 ONCLPC1 ONCLPC2 ONCLPC3 ONCLPC4 ONCLPC5 ONCLPC6 ONCLPC7 ONCLPC9 ONCLPC9A ONCLPC9B ONCMPC0 ONCMPC1 ONCMPC2 ONCMPC3 ONCMPC4 ONCMPC4A ONCMPC5 ONCMPC6 ONCMPC7 ONCMPC9 ONCMPC9A ONCMPC9B ONCMPH ONCNPC0 ONCNPC1 ONCNPC2 ONCNPC3 ONCNPC4 ONCNPC4A ONCNPC5 ONCNPC6 ONCNPC8 ONCNPC8A ONCNPC8B ONCNPI ONCNTX ONCNTX1 ONCOAI ONCOAIC ONCOAID ONCOAIF ONCOAIM ONCOAIM2 ONCOAIP ONCOAIP1 ONCOAIP2 ONCOAIQ ONCOAIS ONCOAIT ONCOANC0 ONCOANC1 ONCOANC2 ONCOANC3 ONCOANC4 ONCOANC5 ONCOANC9 ONCOANCF ONCOANCQ ONCOAS ONCOCC ONCOCFL ONCOCFL1 ONCOCFL2 ONCOCFP ONCOCFP1 ONCOCFR ONCOCKI ONCOCOC ONCOCOF ONCOCOFA ONCOCOM ONCOCOML ONCOCON ONCOCOP ONCOCOS ONCOCRA ONCOCRC ONCOCRF ONCOCRFA ONCODEL ONCODIS ONCODGR ONCODIS ONCODLF ONCODSP ONCODSP1 ONCODSR ONCODXD ONCOEDC ONCOEDC1 ONCOEDC2 ONCOENA ONCOENV ONCOEOD1 ONCOES ONCOFDP ONCOFLF ONCOFTS ONCOFUL ONCOFUM ONCOFUP ONCOGEN ONCOHELP ONCOHICD ONCOIT ONCOLRU ONCOMNI ONCOOT ONCOPA1 ONCOPA1A ONCOPA2 ONCOPA2A ONCOPA3 ONCOPA3A ONCOPA4 ONCOPAR

ONCOPCE ONCOPFX ONCOPMA ONCOPMB ONCOPMP ONCOPRT ONCOPRT1 ONCORF

ONCOSA ONCOSA1 ONCOSC ONCOSC1 ONCOSCF ONCOSCG ONCOSCOM ONCOSCT

ONCOSCT0 ONCOSCT1 ONCOSCT2 ONCOSCT3 ONCOSINP ONCOSO ONCOSSA ONCOSSA1 ONCOSSA2 ONCOSSA3 ONCOSSA4 ONCOSSAT ONCOST ONCOST1 ONCOSUR ONCOSUR1 ONCOSUR2 ONCOSUR3 ONCOTM ONCOTN ONCOTN0 ONCOTNE ONCOTNM ONCOTNM2 ONCOTNMA ONCOTNMB ONCOTNMC ONCOTNMX ONCOTNO ONCOTNS ONCOU ONCOU0 ONCOU55 ONCOU55A ONCOU55B ONCOUK ONCOUTC ONCP2P0 ONCP2P1 ONCP2P2 ONCP2P3 ONCP2P4 ONCP2P4A ONCP2P5 ONCP2P6 ONCP2P8 ONCP2P8A ONCP2P8B ONCPAT ONCPAT1 ONCPCDX ONCPCI ONCPCS ONCPDI ONCPHC ONCPL ONCPM ONCPMB ONCPMC ONCPML ONCPMP ONCPPC0 ONCPPC1 ONCPPC2 ONCPPC3 ONCPPC4 ONCPPC5 ONCPPC6 ONCPPC7 ONCPPC9 ONCPPC9A ONCPPC9B ONCPSD ONCPTX ONCRESTG ONCRFNR ONCRPC ONCRR ONCSAPI ONCSAPI1 ONCSAPI3 ONCSAPID ONCSAPIE ONCSAPIR ONCSAPIS ONCSAPIT ONCSAPIU ONCSAPIV ONCSAPIX ONCSCHMA ONCSCHMB ONCSCHMC ONCSCHMD ONCSCHME ONCSCHMG ONCSCHMH ONCSCHMM ONCSHMN ONCSCHMP ONCSCHMS ONCSCHMT ONCSCHMU ONCSCHMX ONCSCHMY ONCSCHMZ ONCSCHM0 ONCSCHM1 ONCSCHM2 ONCSCHM3 ONCSED01 ONCSED02 ONCSED03 ONCSED04 ONCSEDEM ONCSG0 ONCSG0A ONCSG1 ONCSG1A ONCSG2 ONCSG3 ONCSG4 ONCSG4A ONCSG5 ONCSG5A ONCSGA8A ONCSGA8B ONCSGA8C ONCSGA8H ONCSGA8U ONCSGA8X ONCSNACR ONCSPC0 ONCSPC1 ONCSPC2 ONCSPC3 ONCSPC4 ONCSPC4A ONCSPC5 ONCSPC6 ONCSPC8 ONCSPC8A ONCSRV ONCSRV01 ONCSRVRP ONCSRVTM ONCSSF1 ONCSSF2 ONCSSF25 ONCSSF3 ONCSSF4 ONCSSF5 ONCSSF6 ONCSTX ONCSUBS ONCSYMP ONCTEXT ONCTIME ONCTNMC ONCTPC0 ONCTPC1 ONCTPC2 ONCTPC3 ONCTPC4 ONCTPC5 ONCTPC6 ONCTPC8 ONCTPC8A ONCTXSM ONCUTX ONCUTX1 ONCWEB1 ONCWEB2 ONCWEBCS ONCWEBP1 ONCWEBP2 ONCX ONCX10 ONCX10A ONCXDEM ONCXERR ONCXURL ONCCS4 ONCCSWEB ONCOSUR3 ONCSCHMV ONCSCHMW

# Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## INPUT TEMPLATES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ONCO ABSTRACT-I              | File \#165.5  |
|------------------------------|---------------|
| ONCO DEATH                   | File \#160    |
| ONCO FOLL ADD/EDIT LETTER    | File \#165.1  |
| ONCO FOLL ATTEMPT            | File \#160    |
| ONCO FOLL-ADD CONTACT        | File \#160    |
| ONCO FOLLOWUP                | File \#160    |
| ONCO RECURRENCE FOLLOWUP     | File \#165.5  |
| ONCO UPDATE CONTACT          | File \#165    |
| ONCO UTL CORRECT DATA        | File \#165.5  |

Input TemplatesInput Templates

## PRINT TEMPLATES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ONC EXTRACT  File \#160.16                    |
|-----------------------------------------------|
| ONC EXTRACT REPORT      File \#165.5          |
| ONCO ABSTRACT NOT-COMPLETE File \#165.5       |
| ONCO ACCREG-ACOS80      File \#165.5          |
| ONCO ACCREG-EOVA132      File \#165.5         |
| ONCO ACCREG-SITE/GP80      File \#165.5       |
| ONCO ACOS DOCUMENTATION      File \#160.2     |
| ONCO AJCC SUMMARY STAGE GPS File \#165.5      |
| ONCO ANNUAL ACCREG80      File \#165.5        |
| ONCO ANNUAL ACCREG80-HDR      File \#165.5    |
| ONCO ANNUAL CLASS/PATIENT      File \#165.5   |
| ONCO ANNUAL CLASS/PATIENT-HDR File \#165.5    |
| ONCO ANNUAL HIST/SITE/ICDO      File \#165.5  |
| ONCO ANNUAL ICDO/STAGE/TX      File \#165.5   |
| ONCO ANNUAL PATIENT INDX      File \#165.5    |
| ONCO ANNUAL PATIENT INDX-HDR    File \#165.5  |
| ONCO ANNUAL PATIENT INFO      File \#165.5    |
| ONCO ANNUAL PATIENT INFO-HDR    File \#165.5  |
| ONCO ANNUAL SITE/GP      File \#165.5         |
| ONCO ANNUAL SITE/GP-HDR      File \#165.5     |
| ONCO ANNUAL SITE/ICDT/ICDM      File \#165.5  |
| ONCO ANNUAL SITE/STAGE/TX  File \#165.5       |
| ONCO ANNUAL SITE/STAGE/TX-HDR  File \#165.5   |
| ONCO ANNUAL SITE/STG/TX      File \#165.5     |
| ONCO ANNUAL TREATMENT      File \#165.5       |
| ONCO CASEFINDING REPORT      File \#160       |
| ONCO CASEFINDING-HDR      File \#160          |
| ONCO CONTACT LIST-A      File \#165           |
| ONCO CONTACT LIST-T      File \#165           |
| ONCO DELINQUENT(LTF) LIST      File \#160     |
| ONCO DELINQUENT(LTF) LIST HDR   File \#160    |
| ONCO DELINQUENT(LTF) LIST2      File \#160    |
| ONCO DELINQUENT(LTF) LIST2 HDR  File \#160    |
| ONCO DUE FOLLOWUP      File \#160             |
| ONCO DUE FOLLOWUP-HDR      File \#160         |
| ONCO DUE FOLLOWUP2      File \#160            |
| ONCO DUE FOLLOWUP2-HDR     File \#160         |
| ONCO F/U HISTORY (NEW)      File \#160        |
| ONCO FOLLOW-UP STATUS LIST      File \#160    |
| ONCO FOLLOWUP HISTORY   File \#160            |
| ONCO FOLLOWUP HISTORY-HDR      File \#160     |
| ONCO FOLLOWUP PATIENT RPT      File \#160     |
| ONCO FOLLOWUP PATIENT RPT-HDR File \#160      |
| ONCO FOLLOWUP STATUS RPT      File \#160      |
| ONCO ICDO PATIENT LIST      File \#165.5      |
| ONCO ICDO-SITE132      File \#165.5           |
| ONCO ICDO-SITE132-HDR      File \#165.5       |
| ONCO ICDO-SITE80      File \#165.5            |
| ONCO ICDO-SITE80-HDR      File \#165.5        |
| ONCO LAB-CASEFINDING REPORT     File \#160    |
| ONCO LAB-CASEFINDING-HDR      File \#160      |
| ONCO NEG-REPORT         File \#160.1          |
| ONCO PATIENT INDX-ACOS      File \#160        |
|                                               |
| ONCO PATIENT INDX-ACOS-HDR      File \#160    |
| ONCO PATIENT INDX-EOVA132      File \#160     |
| ONCO PATIENT INDX80      File \#160           |
| ONCO PATIENT ONLY      File \#160             |
| ONCO PATIENT ONLY-HDR      File \#160         |
| ONCO PRIMARY EXTENT CODE AUDIT  File \#165.5  |
| ONCO PRIMARY INFORMATION132     File \#165.5  |
| ONCO PRIMARY SURGERY AUDIT      File \#165.5  |
| ONCO PTF-CASEFINDING RPT      File \#160      |
| ONCO PTF-CASEFINDING-HDR      File \#160      |
| ONCO RAD-CASEFINDING RPT      File \#160      |
| ONCO RAD-CASEFINDING-HDR       File \#160     |
| ONCO SITE HEADING      File \#160.1           |
| ONCO SITE-QA REPORT      File \#160.1         |
| ONCO SITE/GP80       File \#165.5             |
| ONCO SITE/GP80-HDR      File \#165.5          |
| ONCO SITE80          File \#165.5             |
| ONCO SITE80-HEADER      File \#165.5          |
| ONCO SUSPENSE        File \#160               |
| ONCO SUSPENSE-HDR      File \#160             |
| ONCO TOPOG BY SITEGRP      File \#164         |
| ONCO TOPOG SITES      File \#164.2            |
| ONCO TOPOGRAPHY BY CODE      File \#164       |
| ONCO TREATMENT       File \#165.5             |
| ONCO WORKSHEET       File \#160.2             |
| ONCO XABSTRACT RECORD      File \#165.5       |
| ONCO XADMISSION      File \#165.5             |
| ONCO XCONTACT LIST      File \#160            |
| ONCO XDEATH INFO      File \#160              |
| ONCO XINCIDENCE RPRT      File \#165.5        |
| ONCO XPATIENT CONTACTS      File \#160        |
| ONCO XPATIENT DATA      File \#160            |
| ONCO XPATIENT INFO      File \#160            |
| ONCO XPATIENT STATUS      File \#160          |
| ONCOLOGY INPUT TEMPLATE LIST File \#.402      |
| ONCOLOGY OPTION LIST      File \#19           |
| ONCOLOGY PRINT TEMPLATE LIST     File \#.4    |
| ONCOLOGY ROUTINE LIST       File \#9.8        |
| ONCOLOGY SORT TEMPLATE LIST     File \#.401   |
| ONCOW1               File \#165.5             |
| ONCOX1               File \#165.5             |
| ONCOX10              File \#165.5             |
| ONCOX11              File \#165.5             |
| ONCOX2               File \#165.5             |
| ONCOX3              File \#165.5              |
| ONCOX4             File \#165.5               |
| ONCOX5            File \#165.5                |
| ONCOX6             File \#165.5               |
| ONCOX7           File \#165.5                 |
| ONCOX8            File \#165.5                |
| ONCOX9          File \#165.5                  |
| ONCOX99          File \#165.5                 |
| ONCOXA1        File \#165.5                   |
| ONCOXA2      File \#165.5                     |
| ONCOXA3             File \#165.5              |
| ONCOXA4              File \#165.5             |
| ONCOY49           File \#165.5                |
| ONCOY50            File \#165.5               |
| ONCOY51                File \#165.5           |
| ONCOY52          File \#165.5                 |
| ONCOY53          File \#165.5                 |
| ONCOY54         File \#165.5                  |
| ONCOY55         File \#165.5                  |
| ONCOY56           File \#165.5                |
| ONCOY57         File \#165.5                  |
| ONCOY58          File \#165.5                 |
| ONCQA           File \#165.5                  |
| ONCQA1            File \#165.5                |
| ONCQA2               File \#165.5             |
| ONCQA3            File \#165.5                |
| ONC DISEASE INDEX File \#9000010.07           |

Print TemplatesPrint Templates

## SORT TEMPLATES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ONCO ABSTINCOM-TERMDIG          | File \#165.5     |
|---------------------------------|------------------|
| ONCO ABSTRACT DATE/COMPLETE     | File \#165.5     |
| ONCO ABSTRACT NOT-COMPLETE      | File \#165.5     |
| ONCO ABSTRACT NOT-COMPLETE 1    | File \#165.5     |
| ONCO ABSTRACT RECORD            | File \#165.5     |
| ONCO ACCREG-ACOS80              | File \#165.5     |
| ONCO ACCREG-EOVA132             | File \#165.5     |
| ONCO ACCREG-SITE/GP80           | File \#165.5     |
| ONCO ACOS DOCUMENTATION         | File \#160.2     |
| ONCO ANN/ANAL/STA/SITE/DX AGE   | File \#165.5     |
| ONCO ANNUAL ACCREG80            | File \#165.5     |
| ONCO ANNUAL ACOSACCREG80        | File \#165.5     |
| ONCO ANNUAL ANALYTIC            | File \#165.5     |
| ONCO ANNUAL CLASS/PATIENT       | File \#165.5     |
| ONCO ANNUAL CLASS/SITE          | File \#165.5     |
| ONCO ANNUAL HIST/SITE/ICDO      | File \#165.5     |
| ONCO ANNUAL ICDO/STAGE/TX       | File \#165.5     |
| ONCO ANNUAL PATIENT INDX        | File \#165.5     |
| ONCO ANNUAL SITE/GP             | File \#165.5     |
| ONCO ANNUAL SITE/ICDT/ICDM      | File \#165.5     |
| ONCO ANNUAL SITE/STAGE/TX       | File \#165.5     |
| ONCO CASEFINDING REPORT         | File \#160       |
| ONCO CONTACT LIST-A             | File \#165       |
| ONCO CONTACT LIST-T             | File \#165       |
| ONCO DELINQUENT(LTF) LIST       | File \#160       |
| ONCO DISEASE INDEX              | File \#9000010.7 |
| ONCO DISEASE INDEX CASEFINDING  | File \#9000010.7 |
| ONCO DUE FOLLOWUP               | File \#160       |
| ONCO FOLLOWUP HISTORY           | File \#160       |
| ONCO FOLLOWUP PATIENT RPT       | File \#160       |
| ONCO FOLLOWUP STATUS RPT        | File \#160       |
| ONCO ICDO-SITE                  | File \#165.5     |
| ONCO ICDO-SITE132               | File \#165.5     |
| ONCO ICDO-SITE80                | File \#165.5     |
| ONCO LAB-CASEFINDING REPORT     | File \#160       |
| ONCO LOSTTOFOLLOWUP             | File \#160       |
| ONCO NEG-REPORT                 | File \#160.1     |
| ONCO PATIENT ONLY               | File \#160       |
| ONCO PCE ANNUAL REPORT          | File \#165.5     |
| ONCO PTF-CASEFINDING RPT        | File \#160       |
| ONCO RAD-CASEFINDING RPT        | File \#160       |
| ONCO SITE/GP80                  | File \#165.5     |
| ONCO STAGE/SITE                 | File \#165.5     |
| ONCO TOPOG BY SITEGRP           | File \#164       |
| ONCO TOPOG SITES                | File \#164.2     |
| ONCO TOPOGRAPHY BY CODE         | File \#164       |
| ONCOLOGY INPUT TEMPLATE LIST    | File \#.402      |
| ONCOLOGY OPTION LIST            | File \#19        |
| ONCOLOGY PRINT TEMPLATE LIST    | File \#.4        |
| ONCOLOGY ROUTINE LIST           | File \#9.8       |
| ONCOLOGY SITE/GROUP-TOPOGRAPHY  | File \#164.2     |
| ONCOLOGY SORT TEMPLATE LIST     | File \#.401      |
| ONCOS ANAL/STAGE 0              | File \#165.5     |
| ONCOS ANAL/STAGE I              | File \#165.5     |
| ONCOS ANAL/STAGE II             | File \#165.5     |
| ONCOS ANAL/STAGE III            | File \#165.5     |
| ONCOS ANAL/STAGE IV             | File \#165.5     |
| ONCOS ANAL/STAGE NA             | File \#165.5     |
| ONCOS ANAL/STAGE U              | File \#165.5     |
| ONCOS ANALYTIC                  | File \#165.5     |
| ONCOS ANALYTIC-140              | File \#165.5     |
| ONCOS ANALYTIC-153              | File \#165.5     |
| ONCOS ANALYTIC-154              | File \#165.5     |
| ONCOS ANALYTIC-160              | File \#165.5     |
| ONCOS ANALYTIC-161              | File \#165.5     |
| ONCOS ANALYTIC-162              | File \#165.5     |
| ONCOS ANALYTIC-193              | File \#165.5     |
| ONCOS ANALYTIC-196              | File \#165.5     |
| ONCOS ANALYTIC_NON              | File \#165.5     |
| ONCOS ANNUAL ANAL/STAGE 0       | File \#165.5     |
| ONCOS ANNUAL ANAL/STAGE I       | File \#165.5     |
| ONCOS ANNUAL ANAL/STAGE II      | File \#165.5     |
| ONCOS ANNUAL ANAL/STAGE III     | File \#165.5     |
| ONCOS ANNUAL ANAL/STAGE IV      | File \#165.5     |
| ONCOS ANNUAL ANAL/STAGE NA      | File \#165.5     |
| ONCOS ANNUAL ANAL/STAGE U       | File \#165.5     |
| ONCOS ANNUAL-ALLCASES           | File \#165.5     |
| ONCOS ANNUAL-ANALYTIC           | File \#165.5     |
| ONCOS ANNUAL-NON ANAL           | File \#165.5     |
| ONCOS ANNUAL/ANAL-90            | File \#165.5     |
| ONCOS BLACK-FEMALES             | File \#160       |
| ONCOS BLACK-MALES               | File \#160       |
| ONCOS KAPOSI                    | File \#165.5     |
| ONCOS LARYNX/AN/90              | File \#165.5     |
| ONCOS LUNG/NON-SMALL CELL       | File \#165.5     |
| ONCOS MEMPHIS LUNG              | File \#165.5     |
| ONCOS NON-ANALYTIC              | File \#165.5     |
| ONCOS RACE=BLACK                | File \#160       |
| ONCOS RACE=WHITE                | File \#160       |
| ONCOS RANGE-ALLCASES            | File \#165.5     |
| ONCOS RANGE-ANALYTIC            | File \#165.5     |
| ONCOS RANGE-NON ANAL            | File \#165.5     |
| ONCOS SEX=FEMALE                | File \#160       |
| ONCOS SEX=MALE                  | File \#160       |
| ONCOS SITE=BLADDER              | File \#165.5     |
| ONCOS SITE=BRAIN                | File \#165.5     |
| ONCOS SITE=BREAST               | File \#165.5     |
| ONCOS SITE=COLON                | File \#165.5     |
| ONCOS SITE=ESOHAGUS             | File \#165.5     |
| ONCOS SITE=HODGKIN'S            | File \#165.5     |
| ONCOS SITE=HODGKINS             | File \#165.5     |
| ONCOS SITE=LARYNX               | File \#165.5     |
| ONCOS SITE=LIP                  | File \#165.5     |
| ONCOS SITE=LIVER                | File \#165.5     |
| ONCOS SITE=LUNG                 | File \#165.5     |
| ONCOS SITE=LYMPH NODES          | File \#165.5     |
| ONCOS SITE=NON-HODGKINS         | File \#165.5     |
| ONCOS SITE=NON-HODGKINS'S       | File \#165.5     |
| ONCOS SITE=PHARYNX              | File \#165.5     |
| ONCOS SITE=PROSTATE             | File \#165.5     |
| ONCOS SITE=TESTIS               | File \#165.5     |
| ONCOS TOTAL-ANAL                | File \#165.5     |
| ONCOS TOTAL-NON                 | File \#165.5     |
| ONCOS TX-CHEMO                  | File \#165.5     |
| ONCOS TX-HORMONE                | File \#165.5     |
| ONCOS TX-RADIATION              | File \#165.5     |
| ONCOS TX-SURGERY                | File \#165.5     |
| ONCOS WHITE-FEMALES             | File \#160       |
| ONCOS WHITE-MALES               | File \#160       |
| ONCOZ LUNG SURVIVAL             | File \#165.5     |
| ONC DISEASE INDEX               | 9000010.07       |
| ONC DISEASE CASEFINDING         | 9000010.07       |

Sort TemplatesSort Templates

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Site Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DHCP Tumor Registry

Casefinding/Suspense

Abstracting/Printing

Follow-up Functions

Registry Lists

Annual Reports

Statistical Reports

Utility Options

Registry Summary Reports

Delete Oncology Patient

THIS OPTION IS OUT OF ORDER: Marked for deletion

Delete Primary Site/GP Record

Find Duplicate Acc/Seq Numbers

Edit Site/AccSeq# Data

List Topographic Site Groups

List Topography Codes by Site Group

Create a report to preview ACOS output

Create ACOS Data Download

Create a report to preview State/VACCR output

Create State Data Download

Define Tumor Registry Parameters

Enter/Edit Facility file

Print Condensed DD--Oncology Patient file

Print Condensed DD--Oncology Primary file

Purge Suspense Records

Purge Patient Records with No Suspense/Primaries

Restage CS cases using latest version

Compute percentage of TNM forms completed

Timeliness Report

Enter/Edit Chemotherapeutic Drugs file

Create RCRS extract

Create RQRS extract

Find non-standard characters in TEXT

Update Oncology Physician Contacts

Check Validity of TNM Field Values

Correct Next Follow-Up for Expired Patients

Recompute AJCC TNM Staging

Purge Patient Records with No Suspense/Primaries

Create a report to preview ACOS output

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Oncology/Cancer data should be retained on-line, to enable long term survival studies. Therefore, there are no provisions for purging this data. However, there is purging of Contact file entries for a deceased patient available to sites, to be used at their discretion.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable routines for this package.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Oncology requires VA FileMan V. 21 (or later) and VA Kernel V. 8.0 (or later) and points to the following files:

> Patient \#2

> Institution \#4

> County (#5.1)

> ZIP Code (#5.11)

> Referral Patient \#67

> Topography Field \#61

> Morphology Field \#61.1

> Occupation Field \#61.6

> Rad/Nuc Med Procedures \#71

> ICD Diagnosis \#80

> New Person (#200)

## DBIA Subscriber Package Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Obtain a list of agreements using the Print ACTIVE by Subscribing Package option on FORUM.

## DBIA Custodial Package Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Obtain a list of agreements using the Print ACTIVE by Custodial Package option on FORUM.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no options that cannot function independently.

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables.

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are legal issues concerning the dispensing of data regarding veterans to the State and other requesting organizations. It is important for each site to be aware of the privacy laws.

No additional licenses are necessary to run the software.

## Privacy Act Statement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In accordance with Office of Personnel Management and VA policies, this information is to be furnished for use only as authorized. It will not be reproduced or used for any other purpose. Any output must be secured in a storage system adequate to insure against disclosure to unauthorized parties. Disposal will be by burning, shredding, or other treatment to destroy their legibility.

## Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> a\. Mail groups and alerts.

> There are no mail groups or alerts used in this package.

> b\. Remote systems.

> The application transmits some encrypted patient data to a central database on a cloud server.

> c\. Archiving/Purging.

> Oncology/Cancer data should be retained on-line, to enable long term survival studies. Therefore, there are no provisions for purging this data. However, there is purging of Contact file entries for a deceased patient available to sites, to be used at their discretion.

> d\. Contingency Planning.

> It is the responsibility of the using service to develop a local contingency plan to be used in the event of application problems.

> e\. Interfacing.

> No specialized (non-VA) interfaces are used or required by the application.

> f\. Electronic signatures.

> Electronic signatures are not used by the application.

> g\. Menus.

> There are no options of special note for the Information Security Officers (ISO's) to view.

> h\. Security Keys.

> There are no Security Keys in this application.

> i\. File Security.

DD RD WR DEL LAY AUD

NUMBER NAME GLOBAL NAME ACC ACC ACC ACC ACC ACC

------------------------------------------------------------------------------

160 ONCOLOGY PATIENT ^ONCO(160,

160.1 ONCOLOGY SITE PARAMETERS ^ONCO(160.1,

160.12 TYPE OF RECURRENCE ^ONCO(160.12, @ @ @ @ @ @

160.14 NON CANCER-DIRECTED ^ONCO(160.14, @ @ @ @ @ @

SURGERY

160.15 ACOS STATE AT DIAGNOSIS ^ONCO(160.15, @ @ @ @ @ @

160.16 ONCOLOGY DATA EXTRACT ^ONCO(160.16, @ @ @ @ @ @

FORMAT

160.17 ONCOLOGY PCE EXTRACT ^ONCO(160.17, @ @ @ @ @ @

FORMAT

160.19 FACILITY ^ONCO(160.19, @ @

160.2 FORMS/INSTRUCTIONS ^ONCO(160.2,

160.3 PRIMARY PAYER AT ^ONCO(160.3, @ @ @ @ @ @

DIAGNOSIS

160.4 RECONSTRUCTIVE SURGERY ^ONCO(160.4, @ @ @ @ @ @

160.6 SURGICAL APPROACH ^ONCO(160.6, @ @ @ @ @ @

164 ICDO TOPOGRAPHY ^ONCO(164,

164.08 ICDO-SITES ^ONCO(164.08,

164.1 ICD-O-2 MORPHOLOGY ^ONCO(164.1,

164.14 ICDO SITE GROUPS FOR ^ONCO(164.14, @ @ @ @ @ @

REPORTING

164.15 TUMOR MARKERS ^ONCO(164.15, @ @ @ @ @ @

164.17 KARNOFSKY’S RATING ^ONCO(164.17, @ @ @ @ @ @

164.18 CHEMOTHERAPEUTIC DRUGS ^ONCO(164.18, @ @ @ @ @ @

164.2 SITE-GROUP FOR ONCOLOGY ^ONCO(164.2,

164.3 OTHER STAGING FOR ^ONCO(164.3,

ONCOLOGY

164.33 AJCC STAGING GROUPS ^ONCO(164.33,

164.4 COMMON CANCERS ^ONCO(164.4,

164.42 PRIMARY CANCER STATUS ^ONCO(164.42, @

CODE

164.43 GRADE ^ONCO(164.43, @ @ @ @ @ @

164.44 ONCOLOGY GRADE TABLES ^ONCO(164.44, @ @ @ @ @ @

164.45 AJCC STAGE GROUP ^ONCO(164.45, @ @ @ @ @ @

164.46 RACE CODE FOR ONCOLOGY ^ONCO(164.46, @ @ @ @ @ @

164.47 ONCOLOGY SCHEMA DISC CODES ^ONCO(164.47, @ @ @ @ @ @

164.48 PATIENT CANCER STATUS ^ONCO(164.48, @ @ @ @ @ @

CODE

164.5 SEER CODE SET ^ONCO(164.5, @ @ @ @ @ @

164.52 ONC CS SITE-SPECIFIC ^ONCO(164.52, @ @ @ @ @ @

FACTORS

164.6 TYPE OF STAGING SYSTEM ^ONCO(164.6, @ @ @ @ @ @

(PEDIATRIC)

164.7 RADIATION TREATMENT ^ONCO(164.7,

VOLUME

164.8 RADIATION COMPLETION STATUS ^ONCO(164.8,

164.81 ONCO RADIATION EXTERNAL ^ONCO(164.81, @ @ @ @ @ @

BEAM

164.82 ONCO RADIATION TREATMENT ^ONCO(164.82, @ @ @ @ @ @

VOLUME

164.83 ONCO RADIATION TO ^ONCO(164.83, @ @ @ @ @ @

DRAINING LN

164.84 ONCO RADIATION TREATMENT ^ONCO(164.84, @ @ @ @ @ @

MODALITY

164.9 WHO HISTOLOGICAL ^ONCO(164.9, @ @ @ @ @ @

CLASSIFICATION

165 ONCOLOGY CONTACT ^ONCO(165,

165.1 FOLLOW-UP FORM LETTER ^ONCO(165.1,

165.2 GEOCODES ^ONCO(165.2,

165.3 CLASS OF CASE ^ONCO(165.3, @ @ @ @ @ @

165.5 ONCOLOGY PRIMARY ^ONCO(165.5,

165.55 CONVERSION FLAGS ^ONCO(165.55, @ @ @ @ @ @

165.59 COMPUTED PRIMARY ^ONCO(165.59,

165.7 ONCOLOGY STAGED BY CODES ^ONCO(165.7, @ @ @ @ @ @

165.8 AJCC STAGING CHAPTERS ^ONCO(165.8, @ @ @ @ @ @

165.9 ONCOLOGY EOD SCHEMAS ^ONCO(165.9, @ @ @ @ @ @

166 CASEFINDING SOURCE ^ONCO(166, @ @ @ @ @ @

166.12 BLADDER PHYSICIAN SPECIALTY^ONCO(166.12, @

166.13 REGIONAL TREATMENT ^ONCO(166.13, @ @ @ @ @ @

MODALITY

166.3 ONCOLOGY SUBSITE ^ONCO(166.3, @ @ @ @ @ @

167 HEMATOLOGIC TRANSPLANT/ ^ONCO(167, @ @@ @ @ @

ENDOCRINE PROCEDURES

167.1 ONCO BRAIN MOLECULAR MARK ^ONCO(167.1, @ @ @ @ @ @

167.2 GLEASON PATTERNS ^ONCO(167.2, @ @ @ @ @ @

167.3 ONCO LN STATUS ^ONCO(167.3, @ @ @ @ @ @

167.4 ONCO PERIPHERAL BLOOD ^ONCO(167.4, @ @ @ @ @ @

INVOLVEMENT

167.5 ONCO RESIDUAL TUMOR VOLUME ^ONCO(167.5, @ @ @ @ @ @

167.6 ONCO NEOADJUVANT ^ONCO(167.6, @ @ @ @ @ @

THERAPY TREATMENT EFFECT

167.7 ONCO HPV STATUS ^ONCO(167.7, @ @ @ @ @ @

168 TYPE OF REPORTING SOURCE ^ONCO(168, @ @ @ @ @ @

169 TYPE OF MULTIPLE TUMORS ^ONCO(169, @ @ @ @ @ @

169.3 ICD-O-3 MORPHOLOGY ^ONCO(169.3, @ @ @ @ @ @

169.99 ONCOLOGY PACKAGE STATUS ^ONCO(169.99, @ @ @ @ @ @

> j\. Technical References.

> There are several reference materials used for this package:

> 1\. Registry Operations and Data Standards (ROADS) Manual

> 2\. AJCC Cancer Staging Manual

> 3\. SEER Extent of Disease Codes and Coding Instructions

> 4\. International Classification of Diseases for Oncology

> 5\. Standards for Oncology Registry Entry (STORE) Manual

> k\. Official Policies.

> There are no special official policies for this package.

# Appendix A – Upgrading NAACCR Versions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Whenever a new NAACCR Version is implemented, the following steps need to be taken:

1)  Obtain an updated library file generated by the “Veterans Administration” user
2)  Log into VHAWASCCAonc.v05.med.va.gov with administrator rights
3)  Make a zip file of the full web server working folder and store in a safe location:
    1.  (TEST): D:\RockyMountain\wwwroot\OncoTrax_TEST\\
    2.  (PROD): D:\RockyMountain\wwwroot\OncoTrax_PROD\\
4)  Install the new version definition file
    1.  Delete the existing metafile.rmf file in the cgi-bin folder  
        (D:\RockyMountain\wwwroot\OncoTrax\_\<ENV\>\cgi_bin\\ )
    2.  Copy the new .rmf file into the folder above
    3.  Make a copy of this file and rename to “metafile.rmf”
5)  Restart the website

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Abstract                | A summary of pertinent information about the patient, the cancer, the treatment, and outcome. To compile the essential data on a case.                                                                            |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Accession Register      | An annual, sequential listing of all cases entered the registry.                                                                                                                                                  |
| Accession number        | A number unique to the patient which identifies the patient by the year diagnosed and, in the order, he was identified by the registry.                                                                           |
| Accession Year          | The year in which the patient was first seen at the reporting institution for the primary.                                                                                                                        |
| ACoS                    | American College of Surgeons.                                                                                                                                                                                     |
| ACoS number             | A number assigned to facilities by the American College of Surgeons.                                                                                                                                              |
| ADPAC                   | Designated individual responsible for user-level management and maintenance of an application package such as Oncology.                                                                                           |
| AJCC                    | American Joint Commission on Cancer.                                                                                                                                                                              |
| Analytic case           | A case which was diagnosed at your facility or cases in which all or part of the first course of therapy was given at your facility after your reference date.                                                    |
| Automatic case finding  | The electronic capture of cases meeting the defined criteria.                                                                                                                                                     |
| BRM                     | Biological Response Modifier. This is a generic term given to all chemical or biological agents which alter the immune system or the defense mechanism.                                                           |
| Case finding            | A systematic method of locating all eligible cases.                                                                                                                                                               |
| Central Registry Number | The registry number assigned by the state central registry where applicable.                                                                                                                                      |
| Device                  | As used in this document, a printer or computer screen to which a display/report is sent.                                                                                                                         |
| DINUM                   | This input variable identifies the subscript at which the data is to be stored. This means DINUM must be a canonic number and that no data exists in the global at that subscript location.                       |
| ERA                     | Estrogen Receptor Assay is a tumor marker for breast cancer.                                                                                                                                                      |
| Gleason's Grade         | A system for assigning differentiation scores to prostate tissue specimens. The higher the pattern score, the worse the prognosis.                                                                                |
| ICD-O                   | International Classification of Diseases for Oncology.                                                                                                                                                            |
| ICD-9 CM                | International Classification of Diseases, Clinical Modification, 9<sup>th</sup> Revision. Used to code death information.                                                                                         |
| Institution ID Number   | The registry number assigned by the American College of Surgeons. It is used to define the registry in the ACoS Call for Data.                                                                                    |
| LTF                     | Lost to Follow-up. This condition occurs when no contact has been made in over 15 months.                                                                                                                         |
| Non-Analytic case       | A case involving a patient who was diagnosed elsewhere and treated elsewhere or was diagnosed and treated prior to the reference date at your facility. These patients are excluded from the survival statistics. |
| PRA                     | Progesterone Receptor Assay is a tumor marker for breast cancer.                                                                                                                                                  |
| Primary                 | Refers to a specific anatomical site with malignancy.                                                                                                                                                             |
| PTF                     | Patient Treatment File.                                                                                                                                                                                           |
| Reference date          | Starting date after which all cases are entered into the registry. It is established as January 1 of a given year.                                                                                                |
| SEER                    | Surveillance, Epidemiology and End Results Program.                                                                                                                                                               |
| Sequence number         | A number which relates to the independent primary malignancies that occur in the same individual.                                                                                                                 |
| State Hospital Number   | The number assigned by the state to your medical center.                                                                                                                                                          |
| Template                | A computerized filter created to screen information and later print the information in a specific format.                                                                                                         |
| Tumor marker            | Medical laboratory examinations of material that may be indicative of presence of malignancy.                                                                                                                     |
| VA FileMan              | The VA file management program used to maintain, access, and manipulate data in a file.                                                                                                                           |
| Suspense, being in      | Having a date in the Suspense Date field in the Oncology Patient file \#160. Cases remain in suspense until they are accessioned for abstracting or manually deleted.                                             |
GlossaryGlossary
