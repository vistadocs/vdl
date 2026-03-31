---
title: LR*5.2*257 Laboratory Multidivisional Antimicrobial Trend Report  User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: Laboratory Multidivisional Antimicrobial Trend Report
app_code: LR
app_name: Laboratory (LA and LR)
section: CLI
app_status: active
pkg_ns: LR
patch_ver: 5.2
patch_id: LR*5.2*257
group_key: "LR:LR:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - report
  - table
  - trend
  - contents
  - strong
  - microbiology
  - class
  - laboratory
  - antimicrobial
  - division
page_count: 0
word_count: 3617
section_count: 10
table_count: 18
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/lab_52_257_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Laboratory/lab_52_257_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=71"
---

![](lr-5-2-257-laboratory-multidivisional-antimicrobial-trend-report-user-guide/001.png)

LABORATORYMULTIDIVISONAL ANTIMICROBIAL TREND REPORTUSER GUIDEPATCH LR\*5.2\*257Version 5.2

June 2005

Department of Veterans AffairsVistA Health Systems Design & Development

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Staffing Requirements:](#staffing-requirements)
    - [IRM Staff](#irm-staff)
    - [Laboratory Information Manager (LIM)](#laboratory-information-manager-lim)
    - [Intended Users](#intended-users)
  - [Blood Bank Clearance](#blood-bank-clearance)
    - [VISTA BLOOD BANK SOFTWARE V5.2 DEVICE PRODUCT LABELING STATEMENT](#vista-blood-bank-software-v52-device-product-labeling-statement)
  - [# Orientation](#orientation)
    - [Screen Captures](#screen-captures)
    - [User Response](#user-response)
    - [Return Symbol](#return-symbol)
    - [Tab Symbol](#tab-symbol)
  - [Software and Documentation Retrieval Information](#software-and-documentation-retrieval-information)
    - [Software Retrieval](#software-retrieval)
    - [Documentation Retrieval](#documentation-retrieval)
    - [Documentation Retrieval Formats](#documentation-retrieval-formats)
  - [VistA Website Locations:](#vista-website-locations)
    - [Laboratory Version 5.2 Home Page](#laboratory-version-52-home-page)
    - [VistA Documentation Library (VDL)](#vista-documentation-library-vdl)
- [Introduction](#introduction)
  - [Overview](#overview)
    - [Scope and Requirements](#scope-and-requirements)
  - [Test Sites](#test-sites)
- [Enhancements and Modifications](#enhancements-and-modifications)
  - [Enhancements:](#enhancements)
    - [LAB DATA file (#63)](#lab-data-file-63)
    - [Microbiology Trend Report \[LRMITS\] option](#microbiology-trend-report-lrmits-option)
    - [## Modification](#modification)
    - [Typographical Errors Corrected:](#typographical-errors-corrected)
- [Use of the Software](#use-of-the-software)
  - [Microbiology Trend Report \[LRMITS\] option](#microbiology-trend-report-lrmits-option-1)
- [Glossary](#glossary)
The Veterans Health Information Systems and Architecture (Vist*A*) Laboratory Multidivisional Antimicrobial Trend Report Patch LR\*5.2\*257 User Guide Version 5.2 provides the Department of Veterans Affairs Medical Center (DVAMC) Information Resource Management (IRM) staff, Laboratory Information Manager (LIM), and other DVAMC users with a straightforward means for using the software application.

## Staffing Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IRM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM personnel is required for installing and supporting the VistA Laboratory patch LR\*5.2\*257 software.

### Laboratory Information Manager (LIM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of VistA Laboratory Multidivisional Antimicrobial Trend Report Patch LR\*5.2\*257 requires interactive input not <u>only</u> from IRMS, but also from an LIM well versed in the Laboratory Microbiology software application.

### Intended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended user of this software enhancement is VA Medical Center’s laboratory personnel.

## Blood Bank Clearance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VISTA BLOOD BANK SOFTWARE V5.2 DEVICE PRODUCT LABELING STATEMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LR\*5.2\*257 does not contain any changes to the VISTA BLOOD BANK Software as defined by VHA DIRECTIVE 99-053 titled VISTA BLOOD BANK SOFTWARE VERSION 5.2.

EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: Patch LR\*5.2\*257 does not alter or modify any software design safeguards or safety critical elements functions.

RISK ANALYSIS: Changes made by patch LR\*5.2\*257 have no effect on Blood Bank software functionality, therefore RISK is none.

VALIDATION REQUIREMENTS BY OPTION: Because of the nature of the changes made, no specific validation requirements exist as a result of installation of this patch.

## # Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section addresses package-or audience-specific notations or directions (e.g., symbols used to indicate terminal dialogues or user responses) and software/documentation retrieval information.

### Screen Captures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The computer dialogue appears in Courier font, no larger than 10 points.

Example: Courier font 10 points

### User Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User entry response appears in boldface type Courier font, no larger than 10 points.

Example:Boldface type

### Return Symbol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User response to computer dialogue is followed by the \<RET\> symbol that appears in Courier font, no larger than 10 points, and bolded.

Example: \<RET\>

### Tab Symbol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User response to computer dialogue is followed by the symbol that appears in Courier font, no larger than 10 points, and bolded.

Example: \<Tab\>

## Software and Documentation Retrieval Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Multidivisional Antimicrobial Trend Report LR\*5.2\*257 software and User Guide distributions are as follows:

> **NOTE:** All sites are encouraged to use the File Transfer Protocol (FTP) capability. Use the FTP address “download.vista.med.va.gov” (without the quotes) to connect to the first available FTP server where the files are located.

### Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Multidivisional Antimicrobial Trend Report Patch LR\*5.2\*257 software is distributed by Packman.

### Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Multidivisional Antimicrobial Trend Report Patch LR\*5.2\*257 User Guide is available at the following Office of Information Field Offices (OIFOs) ANONYMOUS.SOFTWARE directories:

| OI FIELD OFFICE                    | FTP ADDRESS                    | DIRECTORY                      |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|                                    |                                    |                                    |
|                                    |                                    |                                    |

### Documentation Retrieval Formats

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Multi-divisional Antimicrobial Trend Report Patch LR\*5.2\*257 User Guide files are exported in the following retrieval formats:

| File Names        | Contents                                                                            | Retrieval Formats |
|-------------------|-------------------------------------------------------------------------------------|-------------------|
|                   |                                                                                     |                   |
| LAB_52_257_UG.doc | Laboratory Multidivisional Antimicrobial Trend Report Patch LR\*5.2\*257 User Guide | BINARY            |
|                   |                                                                                     |                   |
| LAB_52_257_UG.pdf | Laboratory Multidivisional Antimicrobial Trend Report Patch LR\*5.2\*257 User Guide | BINARY            |

## VistA Website Locations:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Laboratory Multidivisional Antimicrobial Trend Report LR\*5.2\*257 User Guide is accessible in MS Word (.doc) and Portable Document Format (.pdf) at the following VistA locations:

### Laboratory Version 5.2 Home Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<http://vista.med.va.gov/ClinicalSpecialties/lab/>

### VistA Documentation Library (VDL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[www.va.gov/vdl/](http://www.va.gov/vdl/)
# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Laboratory Multidivisional Antimicrobial Trend Report Patch LR\*5.2\*257 enhancements for the ‘Antimicrobial Trend Reports’ involve antibiograms. Antibiograms are reports that are generated by microbiology laboratories to show clinicians/providers antibiotic activity of the organisms being cultured at a particular facility. Consecutive antibiograms allow the clinicians to evaluate trends in antibiotic sensitivity and resistance. Antibiotic sensitivity means antibiotics that microorganisms respond favorably to and the patient can be cured. Antibiotic resistance is the extent to which microorganism resist or do not respond to antibiotic treatment. Antibiotic resistance is often localized to specific geographic areas and may differ even among health care facilities or nursing homes in a particular geographic region. Therefore, it is crucial that clinicians have access to antimicrobial trend reports involving organisms that have been identified at their facilities. One of the unintended consequences of consolidating VA facilities and merging lab data bases is that it has become increasing difficult for multi-divisional facilities to generate separate antibiograms for each of their divisions. An example of multidivisional facilities experiencing this problem are the VA New York Harbor Health Care System divisions which consists of two acute care facilities (one in Manhattan with a neurosurgery and cardiac surgery program and one Brooklyn), and a nursing home facility in Queens. All the cultures from the three divisions are merged into a single antibiogram, therefore, clinicians at each facility cannot adequately evaluate antibiotic activity trends for their individual divisions. Consequently, these clinicians do not have the technology to adequately evaluate trends to expedite diagnosis, enhance the choice of treatment and promote optimal health care.

### Scope and Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. VistA Laboratory Multidivisional Antimicrobial Trend Report Patch LR\*5.2\*257 enhancements involves the ability of individual facilities within a multidivisional setup to obtain ‘Antimicrobial Trend Reports’ specific to their facilities. This patch provides the functionality for obtaining and printing an ‘Antimicrobial Trend Report’ by DIVISION.

2\. Patch LR\*5.2\*257 also corrects two typographical errors. The query portion of the Microbiology Trend Entry routine has two typographical errors. The word misspelled as susceptibility should be susceptibility. Also, the misspelled word proceed should be proceed.

## Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Laboratory Multi-divisional Antimicrobial Trend Report Patch LR\*5.2\*257 software was tested by the following Veteran Affairs Medical Centers (VAMCs):

<table style="width:100%;">
<colgroup>
<col style="width: 34%" />
<col style="width: 32%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Test Sites</strong></p>
<p><strong>(At least One Integrated Site)</strong></p></th>
<th><strong>Operating System Platform</strong></th>
<th><strong>Test Site Size</strong></th>
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
<td>Cache-VMS</td>
<td>Large</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p><mark>REDACTED</mark></p>
<p><strong>(Integrated Site)</strong></p></td>
<td>Cache-VMS</td>
<td>Large</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p><mark>REDACTED</mark></p>
<p><strong>(Integrated Site)</strong></p></td>
<td>Cache-VMS</td>
<td>Large</td>
</tr>
</tbody>
</table>

# Enhancements and Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Laboratory Multidivisional Antimicrobial Trend Report Patch LR\*5.2\*257 contains the following enhancements and modification:

## Enhancements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### LAB DATA file (#63)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Multidivisional Antimicrobial Trend Report Patch LR\*5.2\*257 enhancement provides the ability to print an Antimicrobial Trend Report by DIVISION using the Microbiology Trend Report \[LRMITS\] option. LAB DATA file (#63), CHEM, HEM, TOX, RIA, SER, etc. subfile (#63.04) and MICROBIOLOGY subfile (#63.05) contain the following one modified field and three new fields:

#### CHEM, HEM, TOX, RIA, SER, etc. subfile (#63.04):

- REQUESTING LOC/DIV field (#63.04,.111): This field was modified to remove the screen on INSTITUTION file (#4). VA facilities need to be able to point to entries in the INSTITUTION file (#4) that are not VA facilities such as DoD and commercial/civilian facilities.
- ACCESSIONING INSTITUTION field (#63.05,.112): This new field contains the pointer to the institution where the specimen was accessioned. This field can be blank if LEDI or POC specimen is accessioned. The field will be set if an actual user accepts the specimen. (For "CH" subscript)

#### MICROBIOLOGY subfile (#63.05): 

- REQUESTING LOC/DIV (#63.05,.111): This new field is used to enter the hospital location or institution ordering the test. (For "MI" subscript)
- ACCESSIONING INSTITUTION field (#63.05,.112): This new field contains the pointer to the institution where the specimen was accessioned. This field can be blank if LEDI or POC specimen is accessioned. The field will be set if an actual user accepts the specimen. (For "MI" subscript)

### Microbiology Trend Report \[LRMITS\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Microbiology Trend Report \[LRMITS\] option is enhanced to sort and print ‘Antimicrobial Trend Report’ by DIVISION. This report is used to compare counts of organisms and patterns of antibiotic susceptibility. Different types of reports can be generated. The types of reports are categorized by; organism, specimen, collection sample, patient, physician, and location. Specific criteria can be applied to all report types. Criteria include; specific types of organisms, isolates collected after a specified time from admission, merge criteria, antibiotic patterns, and detailed reports. These reports can be printed by division or for selected divisions.

### ## Modification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Typographical Errors Corrected:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Laboratory Multidivisional Antimicrobial Trend Report Patch LR\*5.2\*257 software release corrected two typographical errors. The query portion of the Microbiology Trend Entry routine had two typographical errors. Routine LRMITSE contained errors on lines QUERY+3 and QUERY+6. The word <u>susceptibility</u> is corrected as “susceptibility”. The word <u>proceed</u> is corrected “proceed.”

# Use of the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section of the VistA Laboratory Multi-divisional Antimicrobial Trend Report User Guide contains information that allows the END USERS to completely operate the software product. Task-oriented approaches with step-by-step instructions with examples.

## Microbiology Trend Report \[LRMITS\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Microbiology Trend Report \[LRMITS\] option is enhanced to sort the ‘Antimicrobial Trend Report’ by DIVISION. This report is used to compare counts of organisms and patterns of antibiotic susceptibility. Different types of ‘Antimicrobial Trend Report’ by division can be generated. The Microbiology Trend Report \[LRMITS\] option is located on the Laboratory DHCP Menu \[LRMENU\] (locked with LRLAB security key), Microbiology menu \[LRMI\] (locked with LRMICRO security key), Microbiology print menu \[LRMIP\] option.

The ‘Antimicrobial Trend Report’ can be generated by DIVISION using the Microbiology Trend Report \[LRMITS\] option by the following categories:

- Organism
- Specimen
- Collection sample
- Patient
- Physician
- Location

The ‘Antimicrobial Trend Report’ can be generated by DIVISION using the Microbiology Trend Report \[LRMITS\] option by specified criteria:

- Types of organisms
- Isolates collected after a specified time from admission
- Merge criteria
- Antibiotic patterns
- Detailed reports

The ‘Antimicrobial Trend Report’ can be printed by the following DIVISIONS:

- (A)ll Divisions
- (S)elected Divisions
- (N)o Division Report? No

> **NOTE:** Defaults for the ‘Antimicrobial Trend Report’ types can be defined in the LABORATORY SITE file (#69.9). Reports can be restricted to specific types of values (i.e., specific patients, specific specimens, etc.). The reports can be restricted to criteria that affect all types of reports.

The user selects the comprehensive criteria and types of ‘Antimicrobial Trend Reports.’ The time range is forced to months. The report is forced to be queued, preferably to be run during off-hours. The Antimicrobial Trend Reports extracts data from LAB DATA file (#63) and temporarily stores the data in a ^TMP global. The format of the ^TMP global is indexed similar to the outputs of the requested reports. Once the data has been collected, it is reprocessed; counted, and merged using the specified criteria selected. Data merges can be done so that isolates from the same patient and same organism and non-conflicting antibiotic patterns will only be counted once depending on being isolated from the same specimen, collection sample or any sample. A detailed ‘Antimicrobial Trend Report’ showing each isolate values can be used to confirm the counts reported. The data is reported by simply displaying the values of the ^TMP global.

Example: *Microbiology Trend Report \[LRMITS\] option by ALL DIVISION*

Select Laboratory DHCP Menu Option: microbiology menu\<ENTER\>

Select Microbiology menu Option: microbiology print menu\<ENTER\>

Select Microbiology print menu \[LRMIP\] Option: micro \<ENTER\>

    1    Microbiology Audit Reports       

    2    Microbiology Trend Report        

CHOOSE 1-2: 2\<ENTER\> Microbiology Trend Report

Select Microbiology print menu Option: Microbiology Trend Report\<ENTER\>

                              MICROBIOLOGY TREND REPORT

Report by: DIVISION

(A)ll Divisions, (S)elected Divisions, or (N)o Division Report? No//ALL\<ENTER\>

Sort the Antibiotic output by: A// \<ENTER\>lphabetically  
Use default reports HERE? YES//\<ENTER\>

Start Date: t\<ENTER\> (OCT 14, 2004)

End Date: t\<ENTER\> (OCT 14, 2004)

QUEUE TO PRINT ON

DEVICE: Printer\<ENTER\> DALLAS OIFO PRINTER

TIME TO RUN: <T+1@1AM//>\<ENTER\>

REQUEST QUEUED

                      ANTIBIOTIC TREND REPORT BY DIVISION

                          Oct 14, 2004 - Oct 14, 2004

Data reported on: Bacteria

Isolates are merged when same patient, same organism, and same specimen exists.

Merged isolates are those not having conflicting antibiotic patterns.

Example: *Microbiology Trend Report \[LRMITS\] option by ALL DIVISION (continued)*

Antibiotics:

AM+=Ampicillin(+), AMI=Amikacin, AMP=Ampicillin, AUG=Augmentin, AZL=Azlocillin,

AZT=Aztreonam, CEF=Cefamandole, CFP=Cefoperazone, CFR=Cefuroxime,

CFT=Ceftizoxime, CFX=Cefoxitin, CHL=Chloramphenicol, CIP=Ciprofloxacin,

CLI=Clindamycin, CPI=Cefpirome, CPM=Cefepime, CPS=Cephalosporin,

CTA=Ceftriaxone, CTX=Cefotaxime, CTZ=Ceftazidime, CZC=Ceftaz/clavul,

ERY=Erythromycin, GAT=Gatifloxacin, GEN=Gentamicin, IMI=Imipenem,

LEV=Levofloxacin, LIN=Linezolid, MZL=Mezlocillin, NOR=Norfloxacin,

OFL=Ofloxacin, OXC=Oxacillin, PEN=Penicillin, PIP=Piperacillin, PTZ=Piper/taz,

RIF=Rifampin, STR=Streptomycin, TET=Tetracycline, TIM=Timentin, TOB=Tobramycin,

TRM=Trimethaprim/sulfamethoxazole, TRV=Trovafloxacin, UNA=Unasyn,

VAN=Vancomycin

Oct 15, 2004@1:00 ANTIBIOTIC TREND REPORT (from Oct 14, 2004 to: Oct 14, 2004 2 patients)           BY DIVISION Page 1

\|AM+\|AMI\|AMP\|AUG\|AZL\|AZT\|CEF\|CFP\|CFR\|CFT\|CFX\|CHL\|CIP\|CLI\|CPI\|CPM\|CPS\|CTA\|CT

X\|CTZ\|CZC\|ERY\|GAT\|GEN\|IMI\|LEV\|LIN\|MZL\|NOR\|OFL\|OXC\|PEN\|PIP\|PTZ\|RIF\|STR\|TET\|TIM\|TO

B\|TRM\|TRV\|UNA\|VAN\|

     \|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---

Oct 15, 2004@1:00  ANTIBIOTIC TREND REPORT  (from Oct 14, 2004 to: Oct 14, 2004

   2 patients)           BY DIVISION    Page 2

\|AM+\|AMI\|AMP\|AUG\|AZL\|AZT\|CEF\|CFP\|CFR\|CFT\|CFX\|CHL\|CIP\|CLI\|CPI\|CPM\|CPS\|CTA\|CT  
X\|CTZ\|CZC\|ERY\|GAT\|GEN\|IMI\|LEV\|LIN\|MZL\|NOR\|OFL\|OXC\|PEN\|PIP\|PTZ\|RIF\|STR\|TET\|TIM\|TO  
B\|TRM\|TRV\|UNA\|VAN\|  
     \|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---  
DURHAM VAMC (1 isolates)  
---------------

Example: *Microbiology Trend Report \[LRMITS\] option by ALL DIVISION (continued)*

ESCHERICHIA COLI  
(1 counted, 0 merged, 0 not tested)  
% sus\|   \|   \|100\|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   
 \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|100\|100\|   \|   \|   \|100\|   
 \|   \|   \|   \|   \|  
% ctd\|   \|   \|  1\|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   
 \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|   \|  1\|  1\|   \|   \|   \|  1\|   
 \|   \|   \|   \|   \|  
RALEIGH CBOC (1 isolates)

---------------

KLEBSIELLA SP

(1 counted, 0 merged, 0 not tested)  
% sus\|   \|100\|100\|100\|   \|   \|   \|   \|   \|   \|   \|   \|  0\|   \|   \|   \|100\|  0\|   
 \|100\|   \|   \|   \|100\|   \|  0\|   \|   \|   \|   \|   \|   \|100\|100\|   \|   \|   \|100\|10  
0\|  0\|   \|   \|   \|

Oct 15, 2004@1:00 ANTIBIOTIC TREND REPORT (from Oct 14, 2004 to: Oct 14, 2004  
2 patients)           BY DIVISION Page 3

\|AM+\|AMI\|AMP\|AUG\|AZL\|AZT\|CEF\|CFP\|CFR\|CFT\|CFX\|CHL\|CIP\|CLI\|CPI\|CPM\|CPS\|CTA\|CT  
X\|CTZ\|CZC\|ERY\|GAT\|GEN\|IMI\|LEV\|LIN\|MZL\|NOR\|OFL\|OXC\|PEN\|PIP\|PTZ\|RIF\|STR\|TET\|TIM\|TO  
B\|TRM\|TRV\|UNA\|VAN\|  
     \|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---  
% ctd\|   \|  1\|  1\|  1\|   \|   \|   \|   \|   \|   \|   \|   \|  1\|   \|   \|   \|  1\|  1\|   
 \|  1\|   \|   \|   \|  1\|   \|  1\|   \|   \|   \|   \|   \|   \|  1\|  1\|   \|   \|   \|  1\|   
1\|  1\|   \|   \|   \|

Example: *Microbiology Trend Report \[LRMITS\] option by SELECTED DIVISIONS*

Select Microbiology print menu Option: Microbiology Trend Report\<ENTER\>

                              MICROBIOLOGY TREND REPORT

Report by: DIVISION

(A)ll Divisions, (S)elected Divisions, or (N)o Division Report? No// s\<ENTER\> Selected

Select Division: RALEIGH CBOC\<ENTER\>

Select Division: \<ENTER\>

Sort the Antibiotic output by: A//\<ENTER\>lphabetically  
Use default reports HERE? YES//\<ENTER\>

Start Date: t\<ENTER\> (OCT 14, 2004)

End Date: t\<ENTER\> (OCT 14, 2004)

QUEUE TO PRINT ON

DEVICE: Printer\<ENTER\> DALLAS OIFO PRINTER

TIME TO RUN: <T+1@1AM//>\<ENTER\>

REQUEST QUEUED

                      ANTIBIOTIC TREND REPORT BY DIVISION  
                          Oct 14, 2004 - Oct 14, 2004  
This report is restricted to the following divisions:

RALEIGH CBOC

Data reported on: Bacteria  
Isolates are merged when same patient, same organism and same specimen exists.

Merged isolates are those not having conflicting antibiotic patterns.

Antibiotics:  
AM+=Ampicillin(+), AMI=Amikacin, AMP=Ampicillin, AUG=Augmentin, AZL=Azlocillin,  
AZT=Aztreonam, CEF=Cefamandole, CFP=Cefoperazone, CFR=Cefuroxime,  
CFT=Ceftizoxime, CFX=Cefoxitin, CHL=Chloramphenicol, CIP=Ciprofloxacin,  
CLI=Clindamycin, CPI=Cefpirome, CPM=Cefepime, CPS=Cephalosporin,  
CTA=Ceftriaxone, CTX=Cefotaxime, CTZ=Ceftazidime, CZC=Ceftaz/clavul,  
ERY=Erythromycin, GAT=Gatifloxacin, GEN=Gentamicin, IMI=Imipenem,  
LEV=Levofloxacin, LIN=Linezolid, MZL=Mezlocillin, NOR=Norfloxacin,  
OFL=Ofloxacin, OXC=Oxacillin, PEN=Penicillin, PIP=Piperacillin, PTZ=Piper/taz,  
RIF=Rifampin, STR=Streptomycin, TET=Tetracycline, TIM=Timentin, TOB=Tobramycin,  
TRM=Trimethaprim/sulfamethoxazole, TRV=Trovafloxacin, UNA=Unasyn,  
VAN=Vancomycin

Example: *Microbiology Trend Report \[LRMITS\] option by SELECTED DIVISIONS (continued)*

Oct 15, 2004@1:00 ANTIBIOTIC TREND REPORT (from Oct 14, 2004 to: Oct 14, 2004

1 patients) BY DIVISION Page 1

\|AM+\|AMI\|AMP\|AUG\|AZL\|AZT\|CEF\|CFP\|CFR\|CFT\|CFX\|CHL\|CIP\|CLI\|CPI\|CPM\|CPS\|CTA\|CT  
X\|CTZ\|CZC\|ERY\|GAT\|GEN\|IMI\|LEV\|LIN\|MZL\|NOR\|OFL\|OXC\|PEN\|PIP\|PTZ\|RIF\|STR\|TET\|TIM\|TO  
B\|TRM\|TRV\|UNA\|VAN\|  
     \|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---

Oct 15, 2004@1:00 ANTIBIOTIC TREND REPORT (from Oct 14, 2004 to: Oct 14, 2004 1 patients) BY DIVISION Page 2

\|AM+\|AMI\|AMP\|AUG\|AZL\|AZT\|CEF\|CFP\|CFR\|CFT\|CFX\|CHL\|CIP\|CLI\|CPI\|CPM\|CPS\|CTA\|CT  
X\|CTZ\|CZC\|ERY\|GAT\|GEN\|IMI\|LEV\|LIN\|MZL\|NOR\|OFL\|OXC\|PEN\|PIP\|PTZ\|RIF\|STR\|TET\|TIM\|TO  
B\|TRM\|TRV\|UNA\|VAN\|  
     \|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---  
RALEIGH CBOC (1 isolates)---------------  
KLEBSIELLA SP  
(1 counted, 0 merged, 0 not tested)  
% sus\|   \|100\|100\|100\|   \|   \|   \|   \|   \|   \|   \|   \|  0\|   \|   \|   \|100\|  0\|   
 \|100\|   \|   \|   \|100\|   \|  0\|   \|   \|   \|   \|   \|   \|100\|100\|   \|   \|   \|100\|10  
0\|  0\|   \|   \|   \|  
% ctd\|   \|  1\|  1\|  1\|   \|   \|   \|   \|   \|   \|   \|   \|  1\|   \|   \|   \|  1\|  1\|   
 \|  1\|   \|   \|   \|  1\|   \|  1\|   \|   \|   \|   \|   \|   \|  1\|  1\|   \|   \|   \|  1\|   
1\|  1\|   \|   \|   \|

Example: *Microbiology Trend Report \[LRMITS\] option by NO DIVISION REPORT*

MICROBIOLOGY TREND REPORT

Report by: DIVISION

(A)ll Divisions, (S)elected Divisions, or (N)o Division Report? No//\<ENTER\>

Sort the Antibiotic output by: A//\<ENTER\>lphabetically

Use default reports HERE? YES//\<ENTER\>

Start Date: T\<ENTER\> (MAY 12, 2005)

End Date: \<ENTER\> (MAY 12, 2005)

QUEUE TO PRINT ON

DEVICE: Printer\<ENTER\> DALLAS OIFO PRINTER

TIME TO RUN: <T+1@1AM//>\<ENTER\>

REQUEST QUEUED

                      ANTIBIOTIC TREND REPORT BY ORGANISM

                          May 12, 2005 - May 12, 2005

Data reported on: Bacteria

Isolates are merged when same patient, same organism, and same specimen exists.

Merged isolates are those not having conflicting antibiotic patterns.

Antibiotics:

AMI=Amikacin, AMP=Ampicillin, AZT=atreonam, CAR=Carbenicillin, CEF=Cefamandole,

CEP=Cefazolin, CFT=Cefotetan, CFX=Cefoxitin, CHL=Chloramphenicol,

CLI=Clindamycin, CTX=Cefotaxime, ERY=Erythromycin, FUR=Cefuroxime,

GEN=Gentamicin, MET=Methicillin, PEN=Penicillin, PIP=Piperacillin,

TET=Tetracycline, TOB=Tobramycin, TRM=Trimethaprim/sulfamethoxazole,

VAN=Vancomycin

May 13, 2005@1:00 ANTIBIOTIC TREND REPORT (from May 12, 2005 to: May 12, 2005

1 patients) BY ORGANISM Page 1

\|AMI\|AMP\|AZT\|CAR\|CEF\|CEP\|CFT\|CFX\|CHL\|CLI\|CTX\|ERY\|FUR\|GEN\|MET\|PEN\|PIP\|TET\|TO

B\|TRM\|VAN\|

     \|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---\|---

KLEBSIELLA SP  
(1 counted, 0 merged, 0 not tested)  
% sus\|   \|100\|100\|100\|   \|   \|   \|   \|   \|   \|   \|   \|  0\|   \|   \|   \|100\|  0\|   
 \|100\|   \|   \|   \|100\|   \|  0\|   \|   \|   \|   \|   \|   \|100\|100\|   \|   \|   \|100\|10  
0\|  0\|   \|   \|   \|  
% ctd\|   \|  1\|  1\|  1\|   \|   \|   \|   \|   \|   \|   \|   \|  1\|   \|   \|   \|  1\|  1\|   
 \|  1\|   \|   \|   \|  1\|   \|  1\|   \|   \|   \|   \|   \|   \|  1\|  1\|   \|   \|   \|  1\|   
1\|  1\|   \|   \|   \|

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Glossary contains terms and their definitions, acronyms, and phrases that are used throughout the VistA Laboratory environments:
<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Glossary of Terms</strong></th>
<th><strong>Definitions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>AAC:</strong></td>
<td>Austin Automation Center</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>ADPAC:</strong></td>
<td>Automated Data Processing Application Coordinator</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>API:</strong></td>
<td>Application Program Interface</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>E3R:</strong></td>
<td>Electronic Error and Enhancement Report</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>EEI:</strong></td>
<td>Equipment Entity Identifier</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>HCS:</strong></td>
<td>Health Care Systems</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>HL7:</strong></td>
<td>Health Level Seven</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>IDCU:</strong></td>
<td>Integrated Data Communications Utility</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>KIDS:</strong></td>
<td>Kernel Installation &amp; Distribution System</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>LAN:</strong></td>
<td>Local Area Network</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>LEDI:</strong></td>
<td>Laboratory Electronic Data Interchange</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>MUMPS:</strong></td>
<td><p>Massachusetts General Hospital Utility Multi-</p>
<p>Programming System</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>OI:</strong></td>
<td>Office of Information</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>NLFT:</strong></td>
<td>VA National Laboratory Test File</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>NOIS:</strong></td>
<td>National Online Information System</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
</tbody>
</table>
| Glossary of Terms | Definitions                                      |
|-----------------------|------------------------------------------------------|
| PIMS:             | Patient Information Management System                |
|                       |                                                      |
| PLMS:             | Pathology and Laboratory Medicine Service            |
|                       |                                                      |
| POC:              | Point of Care                                        |
|                       |                                                      |
| PTF:              | Patient Treatment File                               |
|                       |                                                      |
| RPC Broker:       | Remote Procedure Call Broker                         |
|                       |                                                      |
| TCP/IP:           | Transmission Control Protocol/Internet Protocol      |
|                       |                                                      |
| UI:               | Universal Interface                                  |
|                       |                                                      |
| VA:               | Department of Veterans Affairs (never use DVA)       |
|                       |                                                      |
| VAMC:             | Department of Veterans Affairs Medical Centers       |
|                       |                                                      |
| VAO:              | VA Office                                            |
|                       |                                                      |
| VISN:             | Veterans Integrated Service Network                  |
|                       |                                                      |
| VistA:            | Veterans Health Information Systems and Architecture |
