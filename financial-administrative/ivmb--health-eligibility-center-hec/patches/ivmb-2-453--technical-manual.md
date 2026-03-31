---
title: IVMB*2*453 Priority Letters Phase 1 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Priority Letters Phase 1
app_code: IVMB
app_name: Health Eligibility Center (HEC)
section: FIN
app_status: active
pkg_ns: IVMB
patch_ver: 2
patch_id: IVMB*2*453
group_key: "IVMB:IVMB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - priority
  - enrollment
  - care
  - veterans
  - health
  - letter
  - letters
  - group
page_count: 0
word_count: 5465
section_count: 24
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2000
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/pl_pivmb_2_453_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Health_Elig_Center_(HEC)/pl_pivmb_2_453_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=143"
---

![](ivmb-2-453-priority-letters-phase-1-technical-manual/001.png)

Priority Letters Phase I

Technical Manual

Health Eligibility Center (HEC)  
Module

Patch IVMB\*2\*453

October 2000

*VISTA* Technical Services

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Background](#background)
  - [Functionality](#functionality)
  - [Related Manuals](#related-manuals)
- [Integration](#integration)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Site Parameters](#site-parameters)
- [Routines](#routines)
  - [Routine Descriptions](#routine-descriptions)
    - [MAIN^IVMB453A](#mainivmb453a)
    - [STRATIFY^AYCBPRI2](#stratifyaycbpri2)
    - [MAIN^AYCBPRIO](#mainaycbprio)
    - [PRI^DGENELA4](#pridgenela4)
    - [GETEGT^AYCBEGT](#getegtaycbegt)
    - [CVTPRIO1^AYCBEGT4](#cvtprio1aycbegt4)
    - [CVTPRIO2^AYCBEGT4](#cvtprio2aycbegt4)
    - [CHKEGT^AYCBENA1](#chkegtaycbena1)
    - [ZEN^AYCBCDT2](#zenaycbcdt2)
    - [ENRPRICR^AYCBCEN](#enrpricraycbcen)
    - [FIELD^AYCBCEN](#fieldaycbcen)
    - [^AYCBLTRI](#aycbltri)
    - [POST^IVMB453](#postivmb453)
    - [^AYCBLTRA](#aycbltra)
    - [^AYCBLTRA](#aycbltra-1)
    - [GETENR^AYCBLTR2](#getenraycbltr2)
    - [LTRS^AYCBLTR1](#ltrsaycbltr1)
    - [CHKRSND^AYCBLTRV](#chkrsndaycbltrv)
    - [CHKPRV^AYCBLTRW](#chkprvaycbltrw)
    - [OKTO027^AYCBLTR8](#okto027aycbltr8)
    - [RULES^AYCBLTR9](#rulesaycbltr9)
    - [GENLTR^AYCBLTR1](#genltraycbltr1)
    - [HIS^DGENL2](#hisdgenl2)
    - [^AYCBCENR](#aycbcenr)
    - [^DGENRPT1](#dgenrpt1)
    - [^DGENRPT2](#dgenrpt2)
    - [^DGENRPT3](#dgenrpt3)
    - [^DGENRPT4](#dgenrpt4)
    - [^DGENA3](#dgena3)
    - [^AYCBLT1](#aycblt1)
  - [Routines by Function](#routines-by-function)
- [Files](#files)
  - [Globals to Journal](#globals-to-journal)
  - [File List](#file-list)
  - [File Flow (Relationships between files)](#file-flow-relationships-between-files)
- [Exported Options](#exported-options)
- [Archiving and Purging](#archiving-and-purging)
- [Package-Wide Variables](#package-wide-variables)
  - [SACC Exemptions/Non-Standard Code](#sacc-exemptionsnon-standard-code)
- [External/Internal Relations](#externalinternal-relations)
  - [Callable Entry Points and APIs](#callable-entry-points-and-apis)
  - [DBIA Agreements](#dbia-agreements)
  - [Internal Relations](#internal-relations)
  - [External Relations](#external-relations)
- [Security](#security)
  - [General Security](#general-security)
  - [Security Keys](#security-keys)
    - [IVME Supervisor](#ivme-supervisor)
    - [DCD Supervisor](#dcd-supervisor)
- [Glossary](#glossary)
  - [Acronyms](#acronyms)
  - [Definitions](#definitions)
- [Appendices](#appendices)
  - [Sample 600C - Enrollment Welcome Letter](#sample-600c-enrollment-welcome-letter)
  - [Sample 600B - One-Time Priority Grouping Notification](#sample-600b-one-time-priority-grouping-notification)
  - [Sample Enrollment Frequently Asked Questions](#sample-enrollment-frequently-asked-questions)
  - [Enrollment Priority Group Fact Sheet](#enrollment-priority-group-fact-sheet)
  - [<table>](#table)

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On November 23, 1999, the Eastern Paralyzed Veterans Association, Inc. (EPVA) petitioned the court claiming that the enrollment regulations promulgated by the Department of Veterans Affairs (VA) violated the Veterans' Health Care Eligibility Reform Act of 1996 (P.L. 104-262) and violated the due process clause of the Fifth Amendment of the United States Constitution.

One issue in the EPVA's complaint is that VA does not advise veterans of their priority group assignment and thereby denies a meaningful right to appeal. Therefore, the Secretary has directed that VHA provide this information to both existing enrollees as well as new enrollees.

The VHA currently sends enrollment letters to veterans notifying them of their enrollment in the VHA Health Care system. However, the notification letter does not contain the veteran’s enrollment priority grouping. There is no other notification from VHA that provides veterans with this information. The ‘Priority Letters Project’ was developed by the VHA with the goal of modifying its current enrollment notification process by including information on the enrollees assigned enrollment priority grouping and if applicable sub-priority.

## Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Priority Letters: Phase I provides the functionality required to advise current and newly enrolled veterans of their priority group assignment and to monitor the progress of Phase I letter mailings.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>User Interactive Functions</strong></td>
<td><strong>Non-interactive Functions</strong></td>
</tr>
<tr class="even">
<td><ul>
<li><blockquote>
<p>Mail ongoing letters to newly enrolled veterans informing them of their priority group assignment</p>
</blockquote></li>
<li><blockquote>
<p>Display sub-priority on existing screens</p>
</blockquote></li>
<li><blockquote>
<p>Display sub-priority on existing reports</p>
</blockquote></li>
<li><blockquote>
<p>Include sub-priority on existing bulletins</p>
</blockquote></li>
<li><blockquote>
<p>Report on the progress of Phase I letter mailings</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Determine sub-priority for Priority 7 veterans</p>
</blockquote></li>
<li><blockquote>
<p>Mail new one-time letter to currently enrolled veterans informing them of their priority group assignment</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Priority Letters Phase I User Manual
- Priority Letters Phase I Installation Guide

# Integration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no integration requirements external to Enrollment application.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no site parameters included with Priority Letters Phase I.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines were created or modified for the priority letters project. The second line of each of these routines will look like:

> \<tab\>;;2.0;INCOME VERIFICATION;\*\*\[Patch list\]\*\*;May 25, 1994

|              |            |           |                                                            |           |
|--------------|------------|-----------|------------------------------------------------------------|-----------|
| Routine  | Before | After | Patch List                                             | Bytes |
| AYCBCDT1 | 2118123    | 2118123   | 277, 392, 453                                              | 7228      |
| AYCBCDT2 | 3407702    | 3442251   | 277, 392, 453                                              | 6131      |
| AYCBCEN  | 6783460    | 7166248   | 277, 392, 399, 453                                         | 7214      |
| AYCBCENR | 8058554    | 8204061   | 359, 392, 453                                              | 6582      |
| AYCBEGT  | 1393766    | 1394335   | 392, 453                                                   | 3260      |
| AYCBEGT4 | 4245021    | 4688966   | 392, 453                                                   | 5448      |
| AYCBENA1 | 9564849    | 9700833   | 190, 257, 290, 315, 392, 453                               | 7922      |
| AYCBLP   | 8907828    | 12044153  | 392, 405, 411, 453                                         | 7641      |
| AYCBLT   | 6322762    | 6320274   | 392, 405, 425, 411, 453                                    | 5048      |
| AYCBLTR  | 9125922    | 9423563   | 405, 411, 453                                              | 5977      |
| AYCBLTR1 | 5328272    | 4069131   | 178, 189, 394, 392, 398, 400, 405, 416, 420, 425, 411, 453 | 5213      |
| AYCBLTR2 | 4723174    | 4625122   | 178, 189, 198, 248, 394, 392, 405, 430, 411, 453           | 3943      |
| AYCBLTR5 | 7715587    | 7511973   | 248, 394, 392, 405, 430, 411, 453                          | 4632      |
| AYCBLTR9 | 9643587    | 8101943   | 420, 453                                                   | 7107      |
| AYCBLTRA | N/A        | 11990926  | 453                                                        | 8662      |
| AYCBLTRI | 6211468    | 6768999   | 392, 398, 400, 420, 453                                    | 6310      |
| AYCBLTRU | 6323228    | 6505452   | 189, 198, 248, 392, 398, 405, 420, 453                     | 9747      |
| AYCBLTRV | 6516787    | 7276324   | 198, 248, 392, 411, 453                                    | 8164      |
| AYCBLTRX | 2762881    | 2856818   | 420, 453                                                   | 2916      |
| AYCBPRI2 | 1515050    | 454990    | 392, 453                                                   | 1048      |
| AYCBPRIO | 8464282    | 7747060   | 94, 120, 132, 141, 142, 188, 235, 241, 392, 453            | 8068      |
| AYCBRLT1 | N/A        | 5449277   | 453                                                        | 3193      |
| AYCBRLT2 | N/A        | 6889823   | 453                                                        | 3512      |
| IVMB453  | N/A        | 7035088   | 453                                                        | 4178      |
| IVMB453A | N/A        | 6337540   | 453                                                        | 4741      |

## Routine Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MAIN^IVMB453A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new routine will scan the ENROLLMENT file (#300.132) for all currently enrolled veterans with an enrollment priority of 7. The sub-priority is calculated by function \$\$STRATIFY^AYCBPRI2. The routine updates the enrollment record with the sub-priority in the ENROLLMENT PRIORITY SUB-GROUP field (#6.5). An entry is made in the ‘AZ11’ cross-reference on the VIVA file (#300.11), causing a Z11 HL7 message to be sent back to the local VAMC systems. The Z11 message contains the new sub-priority and updates the ENROLLMENT SUBGROUP field (#.12) of the PATIENT ENROLLMENT file (#27.11) on the local VAMC systems.

This routine is run as part of the post install process for patch IVMB\*2\*453 called from main post install routine POST^IVMB453. Sub-priorities processing is tasked to run as soon as the patch install completes. The tasked job can be stopped and restarted.

> **NOTE:** This routine must be run and the process of updating all the sub-priorities must be completed before the processing of the new letters can begin.

### STRATIFY^AYCBPRI2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function calculates and returns the sub-priority for priority 7 enrollees.

The sub-priority logic was changed to result in a value of 1 or 3, based on the priority algorithm specified in Priority Letters Phase I SRS section 5.2.8. References to variable ENRDATE were removed.

### MAIN^AYCBPRIO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function calculates the enrollment priority.

In previous versions, the S ENSUBCAT=”” Q bypassed the call to the sub-priority calculation function \$\$STRATIFY^AYCBPRI2.

The line S ENSUBCAT=”” Q was removed so the sub-priority can be calculated and returned by function \$\$STRATIFY^AYCBPRI2. ENRDATE7, the code that determined the enrollment date and set variables was also removed. Enrollment date is no longer needed to calculate the sub-priority.

### PRI^DGENELA4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function returns the priority group and sub-priority group based on a single eligibility code.

This routine was modified to eliminate the check for DGEGT(“EFFDATE”) and perform sub-priority calculations should be done for all priority 7’s. The sub-priority logic was changed to result in a value of 1 or 3, based on the priority algorithm specified in Priority Letters Phase I SRS section 5.2.8.

### GETEGT^AYCBEGT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function returns the EGT that is in effect for a specified date.

The routine was modified to reflect the new sub-priority values so that the variables would be set to 7c and 7.03.

### CVTPRIO1^AYCBEGT4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function converts the EGT from an alpha to numeric value.

In previous versions, the function assumed that alpha values of the sub-priority were A, B, C or D. The code has been modified to calculate the numeric value based on the internal value of the sub-priority field and not assume that it is alpha (A, B, C, or D).

### CVTPRIO2^AYCBEGT4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function converts the EGT from a numeric to an alpha value.

In previous versions, the function assumed that alpha values of the sub-priority were A, B, C or D. The code has been modified to calculate the numeric value based on the internal value of the sub-priority field and not assume that it is alpha (A, B, C, or D).

### CHKEGT^AYCBENA1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function checks the veteran’s priority against the current EGT and if action needs to be taken returns a new enrollment status.

The routine previously converted the sub-priority to a numeric value with a calculation assuming the sub-priority is A, B, C, or D. It has been modified to reflect the new sub-priority values of ‘a’ or ‘c’.

### ZEN^AYCBCDT2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This sub-routine sets up an array of variables that will be used to populate the ZEN segment of the Z11 HL7 message.

The code was modified to add a variable to the ENR array for the sub-priority (\$P(ENRL(0), U,14).

### ENRPRICR^AYCBCEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function performs a consistency check on the current enrollment priority comparing it to the priority calculated using VIVA data. If inconsistent, a flag is set and the calculated priority is returned to be printed in an error message bulletin. In previous versions, the code calculated and compared just the priority. The code has been modified to include the sub-priority in the calculation and comparison.

### FIELD^AYCBCEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function returns file \# and field \# for fields in the ENROLLMENT file (#300.132).

In previous versions, this function included just the PRIORITY field (#6). The code has been modified to add the SUB-PRIORITY field (#6.5).

### ^AYCBLTRI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine can be tasked to produce letters for all veterans requiring letters.

Previously, the enrollment sub-priority threshold was set to ‘D’ at tag EN+1. The code has been modified to reflect the new sub-priority code ‘c’.

### POST^IVMB453

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

POST^IVMB453 runs as part of the patch post install process. It creates a new record in the DCD LETTERS file (#301.11) for the new one-time enrollment letter. POST^IVMB453 calls FileMan APIs to create the new record.

### ^AYCBLTRA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

^AYCBLTRA identifies veterans requiring the new one-time letter and will update their enrollment correspondence record with either ‘0’ for SEND TO AAC or ‘2’ for REJECTED BY THE HEC. The veterans will be identified according to the business rules specified in the Priority Letters Phase I SRS sections 4.2.1.1 and 4.10.1. This routine will call the following existing APIs:

|                       |                                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| API               | Function                                                                    |
| LTRST^AYCBLTR1    | Ensure that the new letter has been activated                                   |
| QUE^AYCBUTL4      | Queue the process to run in the background if the user so chooses               |
| STOPIT^AYCBUTL4   | Check if user requested task to stop                                            |
| FINDCUR^AYCBENA   | Get the current enrollment record                                               |
| GENR^AYCBLTRI     | Get the current enrollment data                                                 |
| DUP^AYCBLTRV      | Check for duplicates                                                            |
| CHK062^IVMBDUP    | Check for duplicates                                                            |
| SSNDUP1^IVMBDUP   | Check for duplicates                                                            |
| UPDTTRCK^AYCBLTRU | Create record and update record in the ENROLLMENT CORRESPONDENCE file (#742027) |

### ^AYCBLTRA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new routine generates VMS files that contain the list of veterans requiring the new one-time enrollment letter. The files will be used by the AAC mail center to generate the letters. This routine will call the following existing APIs:

|                       |                                                           |
|-----------------------|-----------------------------------------------------------|
| API               | Function                                              |
| GFILE^AYCBLTR1    | Get appropriate file name and open the VMS file           |
| GETENR^AYCBLTR2   | Get data needed for letters and file it into the VMS file |
| FILESTAT^AYCBLTR1 | Add totals to the file                                    |
| CLOSE^AYCBLTRU    | Close the file when finished adding data                  |

### GETENR^AYCBLTR2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function gets the enrollment data needed for the letters, formats the data, and updates the file for the AAC.

Previous versions of the routine contained formatting commands that put parentheses around the sub-priority, e.g. 7(a). The code has modified to eliminate the parentheses, e.g. 7a.

### LTRS^AYCBLTR1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function contains the logic to determine which letters need to be mailed. The code has been modified to add validation logic for the new one-time letter according to the business rules specified in Priority Letters Phase I SRS section 4.2.4.1.

### CHKRSND^AYCBLTRV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function contains logic to check to see if a letter can be re-mailed. The code has been modified to add the validation logic for the new one-time letter according to the business rules specified in Priority Letters Phase I SRS section 4.2.4.1.

### CHKPRV^AYCBLTRW

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function checks to see if a letter was sent previously. The code has been modified to include the new one-time letter.

### OKTO027^AYCBLTR8 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function checks to see if a letter should be entered into the ENROLLMENT CORRESPONDENCE file (#742027). It has been modified to include the new welcome and one-time letters.

### RULES^AYCBLTR9 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function contains the logic to determine if the various letters should be sent. The code has been modified to add the logic for the new one-time letter according to the business rules specified in Priority Letters Phase I SRS section 4.2.4.1.

### GENLTR^AYCBLTR1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine generates the correspondence queue entry if it is determined that the veteran should receive a letter for the current enrollment period. A new API has been added to this routine with logic to filter out all priority 7 veterans with AGREE TO DEDUCTIBLE=NO. No letters will be sent to these veterans. The logic to screen out these veterans will be according to the business rules specified in Priority Letters Phase I SRS section 4.10.1.

### HIS^DGENL2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function produces an enrollment history display including the priority and sub-priority.

In previous versions, the code to print the sub-priority was based on \$E(“ABCD”,sub-priority). For Priority Letters Phase I, the code has been modified to display the external value from the data dictionary of the ENROLLMENT SUBGROUP field (#.12) of the PATIENT ENROLLMENT file (#27.11) and not assume what the values are.

### ^AYCBCENR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is the front end for entry/editing of enrollment status information at the HEC. An additional line of code has been added to the DISPENR subroutine to display the appropriate Enrollment Sub-Priority (‘a’ or ‘c’) along with the Enrollment Priority.

### ^DGENRPT1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is used to generate the ‘EGT Preliminary Summary Impact Report’.

The \$S statement of both the PSHEAD and EGTP subroutines have been modified to account for the two Enrollment Priority Sub-priorities of ‘a’ and ‘c’.

### ^DGENRPT2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is used to create the ‘EGT Preliminary Detailed Impact Report’.

The \$S statements in the PRESORT, EGTP and EP subroutines currently have modified to account for the two Enrollment Priority Sub-priorities of ‘a’ and ‘c’.

### ^DGENRPT3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is used to create the ‘EGT Actual Summary Impact Report’.

The \$S statements in the EGTP and PSHEAD subroutines have been modified to account for the ‘a’ and ‘c’ Enrollment Priority Sub-priorities.

### ^DGENRPT4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This routine is used to create the ‘EGT Actual Detailed Impact Report’.

The PRESRT1, EGTP and EP subroutines currently have \$S statements that will need modification to account for the two Enrollment Priority Sub-priorities of ‘a’ and ‘c’.

### ^DGENA3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

^DGENA3 is an Enrollment API used to execute a consistency checks on enrollment information contained in the DGENR array.

The \$E statements in CHECK subroutine have been modified in order to account for the 'a' and 'c' Enrollment Sub-priorities.

### ^AYCBLT1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

^AYCBLT1 generates a report to track the status of HEC enrollment letter mailings for phase I. The report enables the user to generate the report for a selected date/date range. The primary sort for this report is by letter type, within letter type by action date. The user may select a secondary sort of priority code and sub-priority code.

## Routines by Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Determine sub-priority for currently enrolled priority 7 veterans

- MAIN^IVMB453A
- STRATIFY^AYCBPRI2
- MAIN^AYCBPRIO

Determine ‘preliminary’ sub-priority of new priority 7 applicants

- PRI^DGENELA4
- GETEGT^AYCBEGT
- CVTPRIO1^AYCBEGT4
- CVTPRIO2^AYCBEGT4

Determine ‘verified’ sub-priority of new priority 7 applicants/enrollees

- STRATIFY^AYCBPRI2
- CHKEGT^AYCBENA1
- ZEN^AYCBCDT2
- ENRPRICR^AYCBCEN
- FIELD^AYCBCEN
- ^AYCBLTRI

Identify currently enrolled veterans requiring the new one-time letter (600B)

- POST^IVMB453
- ^AYCBLTRA
- Notify the AAC mail center of veterans requiring the new one-time letter
- ^AYCBLTRA
- GETENR^AYCBLTR2

Modify Mail/Remail Enrollment Letter Option to include one-time letter

- LTRS^AYCBLTR1
- CHKRSND^AYCBLTRV
- CHKPRV^AYCBLTRW
- OKTO027^AYCBLTR8
- RULES^AYCBLTR9

Identify newly enrolled veterans requiring a welcome letter (600C)

- POST^IVMB453
- GENLTR^AYCBLTR1
- LTRS^AYCBLTR1
- CHKPRV^AYCBLTRW
- OKTO027^AYCBLTR8
- RULES^AYCBLTR9

Modify Mail/Remail Enrollment Letter Option to include new welcome letter

- LTRS^AYCBLTR1

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Globals to Journal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Priority Letters Phase I project does not require that any globals be journaled.

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|          |                                                    |                 |        |
|----------|----------------------------------------------------|-----------------|--------|
| Number   | Name                                               | Global Location | System |
| 27.16    | Enrollment Group Threshold File                    | ^DGEN(27,16,    | VAMC   |
| 27.11    | Patient Enrollment File                            | ^DGEN(27,11     | VAMC   |
| 2        | Patient File                                       | ^DPT(           | VAMC   |
| 300.132  | Enrollment File                                    | IVMG(300.132    | HEC    |
| 300.13   | IVM Client Income File                             | ^IVMB(300.13    | HEC    |
| 300.12   | IVM Master Client File                             | ^IVM(300.12     | HEC    |
| \#300.11 | Veterans Identification & Verification Access File | ^IVMD (301.11   | HEC    |
| 742027   | Enrollment Correspondence File                     | ^AYCB(742027,   | HEC    |
| 742031   | AAC Printing Transmission Control                  | ^AYCB(742031    | HEC    |
| 742027.1 | Letter Error Codes                                 | ^AYCB(742027.1  | HEC    |
| 742060   | Enrollment Group Threshold File                    | ^IVMGA(742060,  | HEC    |
| 301.11   | DCD Letters File                                   | ^IVMD(301.11    | HEC    |

## File Flow (Relationships between files) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  VA FileMan Menu
2.  Data Dictionary Utilities Menu
3.  List File Attributes Option
4.  Enter File \# or range of File \#s
5.  Select Listing Format: Standard
6.  You will see what files point to the selected file. To see what files the selected file points to, look for fields that say “POINTER TO”.

# Exported Options 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AYCBLTRA ENROLLMENT 600B LTR

^AYCBLT1 Report on Progress by the HEC

# Archiving and Purging 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no archiving and purging capabilities contained in this software product.

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables associated with Priority Letters Phase I.

## SACC Exemptions/Non-Standard Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no SACC Exemptions associated with Priority Letters Phase I.

# External/Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Callable Entry Points and APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no callable entry points or APIs included in this software product.

## DBIA Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no database integration agreements (DBIA) were required for this software product.

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All Priority Letters Phase I package options were designed to stand alone.

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following V<span class="smallcaps">ist</span>A package versions (or higher) MUST be installed PRIOR to loading this version of Priority Letters Phase I:.

Package Version

Kernel V. 7.1

VA FileMan V. 20.0

PIMS V. 5.3

Integrated Billing V. 2.0

OERR V. 2.5

HL7 V. 1.5

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional security implementation is needed.

## General Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IVME Supervisor 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Notify Enrollee Of Priority (600B) Letter \[AYCBLTRA ENROLLMENT 600B LTR\] option is used to task the 600B letter to currently enrolled veterans in order to notify them of their priority. This Option is locked by the IVME SUPERVISOR key.

### DCD Supervisor 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only users holding the DCD Supervisor key can only update Canceled/Declined status enrollments.

# Glossary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                                                                         |
|---------|--------------------------------------------------------------------------------------------------------------------|
| AAC     | Austin Automation Center                                                                                           |
| DCD     | Data Collection Division                                                                                           |
| DHCP    | Decentralized Hospital Computer Program                                                                            |
| EGT     | Enrollment Group Threshold                                                                                         |
| EPVA    | Eastern Paralyzed Veterans Association                                                                             |
| HEC     | Health Eligibility Center                                                                                          |
| HL7     | Health Level Seven                                                                                                 |
| IVM     | Income Verification Match                                                                                          |
| MVR     | Master Veteran Record                                                                                              |
| OPP     | Office of Policy and Planning                                                                                      |
| SLA     | Service Level Agreement (between HEC & AAC mail center)                                                            |
| SRS     | Software Requirement Specification                                                                                 |
| VA      | Veterans Affairs                                                                                                   |
| VHA     | Veterans Health Administration                                                                                     |
| VAMC    | Veterans Affairs Medical Center                                                                                    |
| VISN    | Veteran Integrated Service Networks                                                                                |
| V*IST*A | Veterans Health Information System and Technology Architecture. Both the HEC and VAMC systems are a part of VISTA. |
| VIVA    | Veterans Information and Verification Access program                                                               |

## Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Terminology                                  | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |     |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Austin Automation Center (AAC)               | This organization works in coordination with HEC to support national enrollment mailings, data requests, and data storage.                                                                                                                                                                                                                                                                                                                                                                                                                                           |     |
| Disenrollment                                | Process by which veterans who were previously enrolled are no longer enrolled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |     |
| Enrollment                                   | A process to identify veterans who are eligible for VA benefits, where they are likely to seek this care, and identifying attributes that may suggest the level of care they may need (i.e.; home health, long term care, etc.). This process will enable VA to better plan for and therefore deliver services to its customers. The National Enrollment process is a mandate from congress and outlined in the Eligibility Reform Act of 1996, Public Law 104-262. It is a critical component in managing the delivery of high quality, cost effective health care. |     |
| Enrollment Group Threshold (EGT)             | The Secretary of the VA has the responsibility for determining how many veterans shall be eligible for enrollment into the VA Healthcare System. If it is determined that the VHA does not have sufficient funds to enroll all eligible veterans, enrollment shall be based on the priority groupings established under the regulations of Public Law 104-262, the Veterans Healthcare Eligibility Reform Act of 1996.                                                                                                                                               |     |
| Enrollment History                           | A log of enrollment records for a specific patient that lists the effective date, enrollment status, enrollment priority, and date/time enrollment entered. This history lists the most recent enrollment record first, according to its effective date.                                                                                                                                                                                                                                                                                                             |     |
| Health Level Seven (HL7)                     | ANSI standard for electronic data exchange in healthcare environments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |     |
| Health Eligibility Center (HEC)              | This organization, based in Atlanta, is chartered to provide national customer support for enrollment and manage an interim national database for enrollment.                                                                                                                                                                                                                                                                                                                                                                                                        |     |
| Income Verification Match (IVM), Version 2.0 | VA software that provides the functionality to verify income information for veterans whose eligibility for medical care at VA facilities is based on income. The income verification process for VHA is centralized and performed at the HEC.                                                                                                                                                                                                                                                                                                                       |     |
| Message                                      | The atomic unit of HL7 data transferred between systems. It is comprised of a group of segments in a defined sequence.                                                                                                                                                                                                                                                                                                                                                                                                                                               |     |
| Reenrollment                                 | Process by which veterans whose enrollment cycle has ended are enrolled again.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |     |
| Segment                                      | The logical grouping of HL7 data fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |     |
| Threshold (above/below)                      | Enrollment Priority 1 is the highest and 7 the lowest (in ranking). If the Threshold is 6 and the Enrollment Priority is 5, the enrollment priority is considered to be above the threshold. If the threshold is 5 and the enrollment priority is 6, the enrollment priority is considered to be below the threshold. Above threshold is enrolled, below threshold is not enrolled. If the EGT Threshold and the Enrollment Priority are the same (both 6) then veterans with an Enrollment Priority of 6 would continue to be enrolled.                             |     |
| Trigger Event                                | The event that initiates the exchange of HL7 messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |     |

# Appendices 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sample 600C - Enrollment Welcome Letter [21](#sample-600c---enrollment-welcome-letter)

Sample 600B - One-Time Priority Grouping Notification [22](#sample-600b---one-time-priority-grouping-notification)

Sample Enrollment Frequently Asked Questions [23](#sample-enrollment-frequently-asked-questions)

Enrollment Priority Group Fact Sheet [25](#enrollment-priority-group-fact-sheet)

## Sample 600C - Enrollment Welcome Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[DATE\]

\[NAME\]

\[ADDRESS\]

\[CITY, ST ZIP\]

Dear \[Mr./Ms.\]\[name\]:

I am pleased to confirm your enrollment with the Department of Veterans Affairs (VA) health care system. Enrollment, which occurs on a year-to-year basis, gives you access to a broad range of VA health care services anywhere in the country. Preventive care, primary care, and inpatient and outpatient services are available through VA. You can use these services even if you have Medicare, Medicaid, Department of Defense, or private health insurance coverage.

You are currently enrolled in priority group (stuffing routine to fill in priority group value). If you feel you have been enrolled in the wrong priority group and wish to appeal your classification, you may call the VA Health Benefits Service Center for assistance at 1-877-222-VETS (toll free service).

If your current enrollment Priority Group is 4, 5, 6, or 7 and you received a Purple Heart, you are eligible to be reassigned to Priority Group 3. . VA is in the process of upgrading its computer system to accommodate the Purple Heart enrollment status. If you received a Purple Heart Award, please refer to the Attachment for details on informing VA of your award. Assignment to this new status will be made as soon as the required computer upgrades are completed. You will receive a separate notification when that occurs.

Should you choose to cancel your enrollment for any reason, please notify VA in writing at the following address: VA Health Eligibility Center, REDACTED, Atlanta, Georgia 30329.

Information about enrollment priority groups, your appeal rights and some frequently asked questions and answers are enclosed. Should you have any questions, please contact us at the toll-free number, 1-877-222-VETS (1-877-222-8387).

Thank you for enrolling with the Department of Veterans Affairs health care system. We will do our best to provide you health care that is second to none.

Sincerely,

REDACTED

Chief Network Officer

Enclosure

## Sample 600B - One-Time Priority Grouping Notification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[DATE\]

\[NAME\]

\[ADDRESS\]

\[CITY, ST ZIP\]

Dear \[Mr./Ms.\]\[name\]:

In a previous mailing, you were notified of your enrollment in the Department of Veterans Affairs (VA) health care system. You are currently enrolled in priority group (stuffing routine to fill in priority group value). If you feel you have been enrolled in the wrong priority group and wish to appeal your classification, you may call the VA Health Benefits Service Center for assistance at 1-877-222-VETS (toll free service).

If your current enrollment Priority Group is 4, 5, 6, or 7 and you received a Purple Heart, you are eligible to be reassigned to Priority Group 3. VA is in the process of upgrading its computer system to accommodate the Purple Heart enrollment status. If you received a Purple Heart Award, please see the Attachment for details on informing VA of your award. Assignment to this new status will be made as soon as the required computer upgrades are completed. You will receive a separate notification when that occurs.

Should you choose to cancel your enrollment for any reason, please notify VA in writing at the following address: VA Health Eligibility Center, REDACTED, Atlanta, Georgia 30329.

Information about enrollment priority groups, your appeal rights and some frequently asked questions and answers are enclosed. Should you have any questions, please contact us at the toll-free number, 1-877-222-VETS (1-877-222-8387).

Thank you for enrolling with the Department of Veterans Affairs health care system. We will do our best to provide you health care that is second to none.

Sincerely,

REDACTED

Chief Network Officer

Enclosure

## Sample Enrollment Frequently Asked Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ivmb-2-453-priority-letters-phase-1-technical-manual/002.png)</td>
<td><p>Enclosure</p>
<p><strong>VA HEALTH CARE AND ENROLLMENT</strong></p></td>
</tr>
</tbody>
</table>

Congress has required that after October 1, 1998, most veterans must be enrolled to receive VA hospital and outpatient care. Congress has also expanded the range of medical services that enrolled veterans may receive. Veterans may apply for enrollment at any time. Here are some common questions about enrollment and benefits:

I previously received an Enrollment Welcome letter, why am I receiving a second letter? You received this letter to inform you that your enrollment in the VA health care system has been continued for another enrollment year. The letter also provides information regarding your enrollment priority group status, which was not included in the previous mailing.

If I am enrolled with VA, what benefits will I receive? Veterans in the VA health care system will be eligible to receive necessary hospital and outpatient services, including preventive and primary care. These services include: diagnostic and treatment services; rehabilitation; mental health and substance abuse treatment; home health, respite and hospice care; and drugs in conjunction with VA treatment.

If I am enrolled, what cost will there be for me? There is not a monthly premium required to use VA care. However, you may have to agree to pay some co-payments. If you have insurance, it may cover the cost of the co-payments. For hospital care, the co-payment is the same as the Medicare inpatient deductible for the first 90-day period of care (\$776 in calendar year 2000) and \$10 for each day of care. For outpatient care, the per visit co-payment is 20% of the average cost of a VA outpatient visit (\$50.80 calendar year 2000). There is also a \$2 co-payment for each 30-day supply of prescription drugs.

Is this an insurance policy or an HMO? It is neither. VA health benefits are established by Federal law and regulations and funded through appropriations. They are not the same as an insurance contract. Also, veterans do not pay monthly premiums to receive VA health care. In addition, you are not required to use VA as your exclusive health care provider. If you have health insurance, or eligibility for other programs such as Medicare, Medicaid, or CHAMPUS, you may continue to use services under those programs. We recommend that, if you have other insurance or HMO coverage, you should keep that coverage to provide you with options and flexibility in the future.

Are there any restrictions on getting care in private facilities at VA expense? Yes. Care in private facilities at VA expense is provided only under certain circumstances. To determine if you are eligible for private care at VA expense, you will need to contact the nearest VA health care facility.

  
Will VA pay for care in private facilities? Usually not. VA provides care in private facilities at VA expense when VA has a contract arrangement for certain services or, under very limited circumstances, when VA approves the care in advance.

What is the coverage for emergency services? VA provides urgent and limited emergency care in VA facilities. However, VA’s ability to pay for emergency care in non-VA facilities is very limited. The Veterans Millennium Health Care and Benefits Act has authorized VA to expand emergency care coverage. Refer to the last paragraph for additional details.

What If I get sick while on travel? You may receive health care at any VA health care facility in the country. To minimize any “out-of-pocket” expenses while traveling, you should familiarize yourself with the location of any VA health care facilities in the area. VA’s authority to reimburse you for care in non-VA facilities is very limited.

If enrolled, can I get dental care? In general, dental benefits are limited to service-connected dental conditions or to veterans who are permanently and totally disabled from service-connected causes. For specifics, contact the VA health-benefits advisor at your local VA health care facility.

Will VA take care of my nursing home needs? Nursing home care in VA or private nursing homes may be provided to certain veterans as space and resources permit. The Veterans Millennium Health Care and Benefits Act has authorized VA to expand long-term care services. Refer to the last paragraph for additional details. To determine if you are eligible for VA nursing home care, you will need to contact the nearest VA health care facility.

What Priority Group are veterans assigned to if they were awarded the Purple Heart? Veterans who were awarded the Purple Heart are assigned to Priority Group 3. However, verification of proof is required. Proof of documentation must be submitted to the VA health care facility responsible for your medical care. After VA verifies the document(s) you submitted, appropriated changes will be made to your Priority Group classification. VA is in the process of upgrading its computer system to accommodate the Purple Heart enrollment status. Assignment to this new status will be made as soon as the required upgrades are completed. Affected veterans will receive a separate notification when that occurs.

Will VA provide hearing aids and eyeglasses? Yes, if you are receiving VA care and are service-disabled with a disability rating of 10% or greater or are a former POW. Otherwise, hearing aids and eyeglasses will only be provided in special circumstances, and not for generally occurring hearing or vision loss.

What kinds of maternity services are available? VA provides maternity care, but cannot provide care to a newborn child, even in the immediate aftermath of the birth. The veteran mother must make other arrangements for payment for the care of the child.

Are there any limits on days of hospital care or outpatient visits VA will provide? No, your treating physician will determine what is considered appropriate and necessary hospital care or outpatient services and will provide such care consistent with current medical care practices.

Are there any plans to further expand VA's health care benefits? On November 30, 1999, the President signed Public Law 106-117, the Veterans Millennium Health Care and Benefits Act. This legislation authorizes VA to expand long-term care services and to reimburse for the emergency treatment of certain enrolled veterans. The law also requires VA enroll veterans awarded the Purple Heart into Priority Group Three. VA is currently in the process of drafting regulations required to implement these new authorities. For specifics, contact the Health Benefits Service Center at 877-222-VETS(8387).

## Enrollment Priority Group Fact Sheet 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## <table>
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ivmb-2-453-priority-letters-phase-1-technical-manual/003.png)</td>
<td><strong>Enrollment Priority Groups Health Care Fact Sheet<br />
</strong></td>
</tr>
</tbody>
</table>

![](ivmb-2-453-priority-letters-phase-1-technical-manual/004.png)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Priority Group 1</strong></p>
<ul>
<li><p>Veterans with service-connected disabilities rated 50% or more disabling</p></li>
</ul>
<p><strong>Priority Group 2</strong></p>
<ul>
<li><p>Veterans with service-connected disabilities rated 30% or 40% disabling</p></li>
</ul>
<p><strong>Priority Group 3</strong></p>
<ul>
<li><p>Veterans who are former POWs</p></li>
<li><p>Veterans awarded the Purple Heart</p></li>
</ul>
<ul>
<li><p>Veterans whose discharge was for a disability that was incurred or aggravated in the line of duty</p></li>
</ul>
<ul>
<li><p>Veterans with service-connected disabilities rated 10% or 20% disabling</p></li>
</ul>
<ul>
<li><p>Veterans awarded special eligibility classification under Title 38, U.S.C., Section 1151, "benefits for individuals disabled by treatment or vocational rehabilitation"</p></li>
</ul>
<p><strong>Priority Group 4</strong></p>
<ul>
<li><p>Veterans who are receiving aid and attendance or housebound benefits</p></li>
</ul>
<ul>
<li><p>Veterans who have been determined by VA to be catastrophically disabled</p></li>
</ul></td>
<td><p><strong>Priority Group 5</strong></p>
<ul>
<li><p>Nonservice-connected veterans and service-connected veterans rated 0% disabled whose annual income and net worth are below the established dollar threshold</p></li>
</ul>
<p><strong>Priority Group 6</strong></p>
<ul>
<li><p>All other eligible veterans who are not required to make co-payments for their care, including:</p></li>
</ul>
<ul>
<li><p>World War I and Mexican Border War veterans</p></li>
</ul>
<ul>
<li><p>Veterans receiving care solely for disabilities resulting from exposure to toxic substances, radiation or for disorders associated with service in the Gulf War; or for any illness associated with service in combat in a war after the Gulf War or during a period of hostility after November 11, 1998</p></li>
</ul>
<ul>
<li><p>Compensable 0% service-connected veterans</p></li>
</ul>
<p><strong>Priority Group 7</strong></p>
<ul>
<li><p>(a) <u>noncompensable</u> 0% service-connected veterans and</p></li>
<li><p>(c) all other priority category 7 veterans with income and net worth above the statutory threshold who agree to pay specified <u>co-payment</u></p></li>
</ul></td>
</tr>
</tbody>
</table>