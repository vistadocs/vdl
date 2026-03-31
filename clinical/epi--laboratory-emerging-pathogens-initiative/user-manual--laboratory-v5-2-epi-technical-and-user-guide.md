---
title: Laboratory Version 5.2 EPI Technical and User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: EPI Technical and
app_code: EPI
app_name: "Laboratory: Emerging Pathogens Initiative"
section: CLI
app_status: active
pkg_ns: EPI
patch_ver: 5.2
patch_id: EPI*5.2
group_key: "EPI:EPI:5.2"
file_numbers: 
  - 69
security_keys: []
menu_options: 0
description: Under the auspices of the Program Office for Infectious Diseases VAHQ the Laboratory Emerging Pathogens Initiative (EPI) software package is to allow the Department of Veterans Affairs (DVA) to track Emerging Pathogens on the national level without the necessity for additional local data entry. Usin
audience: 
keywords: 
  - emerging
  - table
  - blockquote
  - class
  - pathogens
  - contents
  - pathogen
  - site
  - reference
  - description
page_count: 0
word_count: 23538
section_count: 39
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Emerging_Pathogens_Initiative/lab_epi_tech_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Emerging_Pathogens_Initiative/lab_epi_tech_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=118"
---

LaboratoryEmerging Pathogens Initiative (EPI)Version 5.2Technical and User Guide

![](laboratory-version-5-2-epi-technical-and-user-guide/001.png)

September 2015Department of Veterans Affairs (VA)Office of Information and Technology (OI&T)Product Development (PD)Revision History

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 21%" />
<col style="width: 41%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>9/2015</td>
<td>LR*5.2*442</td>
<td><p>Updates for LR*5.2*442, ICD-10 Patient Treatment File (PTF) Modifications:</p>
<p>Updated title page and footers, updated Preface (p.vi), updated Pre-installation Instructions (p.9), added DBIA #6130 (p.11), reformatted and updated Routine List (p.11), updated Patches Required (p.14), updated Installation Instructions (p.23), updated Post Installation Instructions (p.30).</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/2014</td>
<td><p>LR*5.2*421</p>
<p>pp. v-vi</p>
<p>p. <a href="#p421_vii">vii</a></p>
<p>p. <a href="#p421_8">8</a></p>
<p>p. <a href="#pre-installation-instructions"><u>9</u></a></p>
<p>p. <a href="#epi-routines"><u>11</u></a></p>
<p>pp. <a href="#File695">18-19</a></p>
<p>p. <a href="#p421_21"><u>21</u></a></p>
<p>p. <a href="#PIIFix2">23</a></p>
<p>p. <a href="#p421_31">31</a></p>
<p>pp. <a href="#DG1_table"><u>36</u></a>, <a href="#p421_38"><u>38</u></a></p>
<p>p. <a href="#p421_47">47</a></p>
<p>pp. <a href="#EP_Prim_Menu"><u>49</u></a>, <a href="#ICDCodingSystemUpdate2"><u>53</u></a>, <a href="#p421_55">55-56</a>, <a href="#p421_58">58-59</a>, <a href="#p421_61">61-62</a>, <a href="#Primary_Menu_E_Coli"><u>65</u></a>, <a href="#p421_68">68-69</a>, <a href="#p421_71">71-72</a>, <a href="#p421_74">74-75,</a> <a href="#p421_77">77-78</a>, <a href="#p421_80">80-81</a>, <a href="#p421_83">83-84</a>, <a href="#p421_86">86-87</a>, <a href="#Primary_Menu_Vanc"><u>90</u></a></p>
<p>pp. <a href="#p421_38"><u>38</u></a>, <a href="#p421_114"><u>114</u></a></p>
<p>Multiple pages</p>
<p>Multiple pages</p></td>
<td><p>Added Revision History.</p>
<p>Added summary of features for patch LR*5.2*421</p>
<p>Updated TOC.</p>
<p>Updated VDL URL.</p>
<p>Added note on pre-installation.</p>
<p>Added routines for patch LR*5.2*421.</p>
<p>Updated File #69.5 fields for Help Text and generic change from ICDM-9 to ICD.</p>
<p>Added Data Dictionary changes.</p>
<p>Added note on installation.</p>
<p>Added note on post installation.</p>
<p>Updated DG1 Segment of HL7 message to utilize ~ rather than ^.</p>
<p>Added ICD-10 to definitions table.</p>
<p>Updated Primary Menu and examples for addition of Code System prompt.</p>
<p>Removed Personally Identifiable Information (PII).</p>
<p>Updated all references from ICDM-9 to ICD.</p>
<p>Changed AAC to Austin Information Technology Center (AITC) throughout manual</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>02/1997</td>
<td>LR*5.2*132</td>
<td>Initial release.</td>
<td>VA OI&amp;T</td>
</tr>
</tbody>
</table>

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Introduction](#introduction)
  - [Major functions:](#major-functions)
    - [Objectives:](#objectives)
  - [VISTA Process](#vista-process)
  - [Austin Automation Center:](#austin-automation-center)
  - [EPI Technical and User Guide Notations](#epi-technical-and-user-guide-notations)
    - [Screen Displays](#screen-displays)
    - [Computer Dialogue](#computer-dialogue)
    - [User Response](#user-response)
    - [Return Symbol \<Enter\>](#return-symbol-enter)
    - [Tab Symbol \<Tab\>](#tab-symbol-tab)
    - [References](#references)
    - [### EPI Technical and User Guide Distributions](#epi-technical-and-user-guide-distributions)
- [Pre-installation Instructions](#pre-installation-instructions)
  - [Hardware and Operating System Requirements](#hardware-and-operating-system-requirements)
  - [Performance/Capacity Impact](#performancecapacity-impact)
  - [Backup Routines](#backup-routines)
  - [It is <u>highly</u> recommended that a backup of the transport global is performed.](#it-is-uhighlyu-recommended-that-a-backup-of-the-transport-global-is-performed)
  - [EPI Test Sites](#epi-test-sites)
  - [Test Account](#test-account)
  - [It is <u>highly</u> recommended that the EPI Patch LR\5.2\132 is installed into a test account before installing into a live Production Account. The Test and Production Accounts must include all required software versions and patches to assure a successful installation of this patch.](#it-is-uhighlyu-recommended-that-the-epi-patch-lr52132-is-installed-into-a-test-account-before-installing-into-a-live-production-account-the-test-and-production-accounts-must-include-all-required-software-versions-and-patches-to-assure-a-successful-installation-of-this-patch)
  - [Installation Time](#installation-time)
  - [Kernel Installation and Distribution System (KIDS)](#kernel-installation-and-distribution-system-kids)
  - [Health Level Seven (HL7)](#health-level-seven-hl7)
  - [Database Integration Agreements (DBIA)](#database-integration-agreements-dbia)
  - [EPI Routines](#epi-routines)
  - [Staffing Requirement](#staffing-requirement)
    - [IRM Staff](#irm-staff)
    - [Laboratory Staff](#laboratory-staff)
    - [Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) Staff](#total-quality-improvementquality-improvementquality-assurance-tqiqiqa-staff)
  - [VISTA\DHCP Software Requirements](#vistadhcp-software-requirements)
  - [Patches Required](#patches-required)
  - [## EPI Files](#epi-files)
  - [EPI Namespace](#epi-namespace)
  - [EPI Menu and Options](#epi-menu-and-options)
  - [Emerging Pathogens Nightly Task Option](#emerging-pathogens-nightly-task-option)
  - [New <span class="mark">REDACTED</span> Domain](#new-span-classmarkredactedspan-domain)
  - [Protocols](#protocols)
  - [## EPI-Mail Groups](#epi-mail-groups)
  - [Data Dictionaries](#data-dictionaries)
- [Installation Instructions](#installation-instructions)
  - [Installation Time](#installation-time-1)
  - [Installation Process](#installation-process)
- [# Post Installation Instructions](#post-installation-instructions)
    - [DSM/Alpha Sites](#dsmalpha-sites)
    - [MSM Sites](#msm-sites)
    - [IRM Staff](#irm-staff-1)
  - [# Health Level Seven (HL7) Protocol](#health-level-seven-hl7-protocol)
- [Laboratory EPI Patch LR\5.2\132 User Guide](#laboratory-epi-patch-lr52132-user-guide)
  - [Emerging Pathogens](#emerging-pathogens)
  - [Emerging Pathogen Primary Menu](#emerging-pathogen-primary-menu)
  - [Emerging Pathogens Descriptions and Screen Displays](#emerging-pathogens-descriptions-and-screen-displays)
    - [Candida (Reference \#8)](#candida-reference-8)
    - [Clostridium difficile (Reference \#4)](#clostridium-difficile-reference-4)
    - [Creutzfeldt-Jakob Disease (CJD) (Reference \#13)](#creutzfeldt-jakob-disease-cjd-reference-13)
    - [Cryptosporidium (Reference \#9)](#cryptosporidium-reference-9)
    - [Dengue (Reference \#12)](#dengue-reference-12)
    - [E. coli O157:H7 (Reference \#10)](#e-coli-o157h7-reference-10)
    - [Hepatitis C Antibody Positive (Reference \#2)](#hepatitis-c-antibody-positive-reference-2)
    - [Legionella (Reference \#7)](#legionella-reference-7)
    - [Leishmaniasis (Reference \#14)](#leishmaniasis-reference-14)
    - [Malaria (Reference \#11)](#malaria-reference-11)
    - [Penicillin- Resistant Pneumococcus (Reference \#3)](#penicillin-resistant-pneumococcus-reference-3)
    - [Streptococcus-Group A (Reference \#6](#streptococcus-group-a-reference-6)
    - [Tuberculosis (Reference \#5)](#tuberculosis-reference-5)
    - [Vancomycin-Resistant Enterococcus (VRE) (Reference \#1)](#vancomycin-resistant-enterococcus-vre-reference-1)
  - [Conclusion](#conclusion)
- [Appendix](#appendix)
  - [Validation Of Data Capture](#validation-of-data-capture)
    - [Emerging Pathogens Verification Report](#emerging-pathogens-verification-report)
    - [Table of Reject and Warning Codes](#table-of-reject-and-warning-codes)
  - [Editing TOPOGRAPHY file (#61)](#editing-topography-file-61)
  - [How to Link Antimicrobial Entries to Workload Codes Entries](#how-to-link-antimicrobial-entries-to-workload-codes-entries)
    - [### ### Request Form](#request-form)
  - [Helpful Hints:](#helpful-hints)
    - [Screens Enter/Edits](#screens-enteredits)
    - [Clostridium difficile](#clostridium-difficile)
    - [EPI Mail Groups Assignments](#epi-mail-groups-assignments)
    - [Transmitting a Message to Austin](#transmitting-a-message-to-austin)
    - [EPI Processing Report](#epi-processing-report)
The Veterans Health Information Systems and Architecture (*VISTA*) formerly Decentralized Hospital Computer Program (DHCP) Laboratory Emerging Pathogens Initiative (EPI) Patch LR\*5.2\*132 Technical and User Guide provides the Department of Veterans Affairs Medical Center (DVAMC) Information Resource Management (IRM) and other medical center users with a straightforward means for installing and implementing the EPI software package.
> **NOTE:** It is <u>highly</u> <u>recommended</u> that the Laboratory Information Manager (LIM), and a representative from the Microbiology section (director, supervisor, or technologist) <u>jointly</u> participate in reviewing the 14 Emerging Pathogen parameters descriptions and entering of data for the EPI software package. The individual(s) will be responsible for initially defining the EPI parameters and a yearly review of the 14 Emerging Pathogens.
It is also suggested that a Total Quality Improvement/Quality Improvement/ Quality Assurance (TQI/QI/QA) staff (or person at the site with similar function) be involved in the EPI process. The individual(s) will assist in initially defining the EPI parameters, a yearly review of the 14 Emerging Pathogens, and a periodic review of the ICD codes to assure they are current. Also, this function will help coordinate the overall implementation at each site.
The International Classification of Diseases, Tenth Revision (ICD-10) Remediation patch LR\* 5.2\*421 makes the following changes to the EPI application:
- The following fields and screens have been updated to refer to “ICD” rather than “ICD9”:
  - Laboratory Search/Extract Parameters Input screens
  - Enter/Edit Local Pathogens screens
  - Detailed Verification Report
  - Help text
- Within the Enter/Edit Local Pathogens and Laboratory Search/Extract Parameters Input screens, users are prompted to specify a code set on which to search prior to entering an ICD code. Based on this input, the system will only allow ICD-9 entry or ICD-10 entry.
- The Pathogen Inquiry option has been modified to list both ICD-9 and ICD-10 codes.
- The Generate Local Report/Spreadsheet option has been modified to include both the Diagnosis Code Set Designation and the Diagnosis Code.
- Health Level 7 (HL7) Reports that are sent to Austin Information Technical Center (AITC) have been modified to include ICD-10 Codes and Descriptions, which are included in the DG1 HL7 Segments.
The ICD-10 PTF Modifications patch LR\*5.2\*442 made changes to accommodate the expanded number of ICD-10 codes that can now be entered in a patient record.
EPI Technical and User Guide focuses on easy-to-follow, step-by-step instructions. This guide includes the following four sections:
Pre-Installation: This section covers the requirements that must be performed prior to installing the software.
Installation Instructions: This section includes a detailed example of the actual EPI Patch LR\*5.2\*132 installation process.
Post Installation Instructions: This section provides all the necessary information required for the IRM personnel to implement the EPI software package after the installation process is completed.
User Guide: This section provides all necessary information required for the user to implement and maintain the EPI software.
Table of Contents
Preface [iv](#preface)
Introduction [1](#introduction)
Major functions: [1](#major-functions)
Objectives: [1](#objectives)
How The Software Accomplishes The Objective: [1](#how-the-software-accomplishes-the-objective)
*VISTA* Process [2](#vista-process)
Local Reports [2](#local-reports)
Austin Automation Center: [3](#austin-automation-center)
EPI Technical and User Guide Notations [7](#epi-technical-and-user-guide-notations)
Screen Displays [7](#screen-displays)
Computer Dialogue [7](#computer-dialogue)
User Response [7](#user-response)
Return Symbol \<Enter\> [7](#return-symbol-enter)
Tab Symbol \<Tab\> [7](#tab-symbol-tab)
References [8](#references)
EPI Technical and User Guide Distributions [8](#epi-technical-and-user-guide-distributions)
Electronic Distributions [8](#electronic-distributions)
Hyper Text Markup Language (HTML) [8](#hyper-text-markup-language-html)
Portable Document Format (PDF) [8](#portable-document-format-pdf)
Hard Copy [8](#hard-copy)
Pre-installation Instructions [9](#pre-installation-instructions)
Hardware and Operating System Requirements [9](#hardware-and-operating-system-requirements)
Performance/Capacity Impact [9](#performancecapacity-impact)
Backup Routines [9](#backup-routines)
EPI Test Sites [10](#epi-test-sites)
Test Account [10](#test-account)
Installation Time [10](#installation-time)
Kernel Installation and Distribution System (KIDS) [11](#kernel-installation-and-distribution-system-kids)
Health Level Seven (HL7) [11](#health-level-seven-hl7)
Database Integration Agreements (DBIA) [11](#database-integration-agreements-dbia)
EPI Routines [11](#epi-routines)
Staffing Requirement [13](#staffing-requirement)
IRM Staff [13](#irm-staff)
Laboratory Staff [13](#laboratory-staff)
Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) Staff [13](#total-quality-improvementquality-improvementquality-assurance-tqiqiqa-staff)
*VISTA*\DHCP Software Requirements [14](#vistadhcp-software-requirements)
Patches Required [14](#patches-required)
EPI Files [14](#epi-files)
EPI Namespace [14](#epi-namespace)
EPI Menu and Options [15](#epi-menu-and-options)
Emerging Pathogens Nightly Task Option [15](#emerging-pathogens-nightly-task-option)
New Q-EPI.MED.VA.GOV Domain [16](#new-redacted-domain)
Protocols [16](#protocols)
EPI-Mail Groups [16](#epi-mail-groups)
Data Dictionaries [17](#data-dictionaries)
Installation Instructions [23](#installation-instructions)
Installation Time [23](#installation-time-1)
Installation Process [24](#installation-process)
Post Installation Instructions [30](#post-installation-instructions)
DSM/Alpha Sites [30](#dsmalpha-sites)
MSM Sites [30](#msm-sites)
IRM Staff [30](#irm-staff-1)
Health Level Seven (HL7) Protocol [34](#health-level-seven-hl7-protocol)
Laboratory EPI Patch LR\*5.2\*132 User Guide [44](#laboratory-epi-patch-lr5.2132-user-guide)
Emerging Pathogens [44](#emerging-pathogens)
Emerging Pathogen Primary Menu [45](#emerging-pathogen-primary-menu)
Emerging Pathogens Descriptions and Screen Displays [47](#emerging-pathogens-descriptions-and-screen-displays)
Candida (Reference \#8) [47](#candida-reference-8)
Clostridium difficile (Reference \#4) [51](#clostridium-difficile-reference-4)
Creutzfeldt-Jakob Disease (CJD) (Reference \#13) [54](#creutzfeldt-jakob-disease-cjd-reference-13)
Cryptosporidium (Reference \#9) [57](#cryptosporidium-reference-9)
Dengue (Reference \#12) [60](#dengue-reference-12)
E. coli O157:H7 (Reference \#10) [63](#e.-coli-o157h7-reference-10)
Hepatitis C Antibody Positive (Reference \#2) [67](#hepatitis-c-antibody-positive-reference-2)
Legionella (Reference \#7) [70](#legionella-reference-7)
Leishmaniasis (Reference \#14) [73](#leishmaniasis-reference-14)
Malaria (Reference \#11) [76](#malaria-reference-11)
Penicillin- Resistant Pneumococcus (Reference \#3) [79](#penicillin--resistant-pneumococcus-reference-3)
Streptococcus-Group A (Reference \#6 [82](#streptococcus-group-a-reference-6)
Tuberculosis (Reference \#5) [85](#tuberculosis-reference-5)
Vancomycin-Resistant Enterococcus (VRE) (Reference \#1) [88](#vancomycin-resistant-enterococcus-vre-reference-1)
Conclusion [92](#conclusion)
Appendix [96](#appendix)
Validation Of Data Capture [96](#validation-of-data-capture)
Emerging Pathogens Verification Report [98](#emerging-pathogens-verification-report)
Table of Reject and Warning Codes [100](#table-of-reject-and-warning-codes)
Editing TOPOGRAPHY file (#61) [103](#editing-topography-file-61)
How to Link Antimicrobial Entries to Workload Codes Entries [104](#how-to-link-antimicrobial-entries-to-workload-codes-entries)
Request Form [105](#request-form)
Helpful Hints: [107](#helpful-hints)
Screens Enter/Edits [107](#screens-enteredits)
How to delete a entry. [107](#how-to-delete-a-entry.)
How to add a entry [108](#how-to-add-a-entry)
Clostridium difficile [109](#clostridium-difficile)
EPI Mail Groups Assignments [111](#epi-mail-groups-assignments)
Office of the Director (00) [111](#office-of-the-director-00)
Transmitting a Message to Austin [113](#transmitting-a-message-to-austin)
EPI Processing Report [114](#epi-processing-report)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Under the auspices of the Program Office for Infectious Diseases VAHQ the Laboratory Emerging Pathogens Initiative (EPI) software package is to allow the Department of Veterans Affairs (DVA) to track Emerging Pathogens on the national level without the necessity for additional local data entry. Using this objective information, plans can be formulated on the national level for intervention strategies and resource needs. Results of aggregate data can also be shared with appropriate public health authorities for planning on the national level for the non-VA and private health care sectors.

## Major functions: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory EPI program is designed to automatically provide data on emerging pathogens to Veterans Affairs Headquarters (VAHQ) without additional individual data entry at the site level. The data will be sent to Austin Information Technology Center (AITC) for initial processing and coupling with denominator data related to workload. VAHQ data retrieval and analysis can then be accomplished.

### Objectives:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Identify Emerging Pathogens.
- Extract specific data associated with the Emerging Pathogen.
- Transmit data to AITC.
- Create national Statistical Analysis System (SAS) data sets for Infectious Diseases Program Office access.

#### How The Software Accomplishes The Objective:

Emerging Pathogens (as defined by VAHQ) act as triggers for data acquisition for the automated program. The system then retrieves relevant, predetermined, patient-specific information for transmission to the central data repository. Once at that location, the data will be analyzed using a SAS based statistical package. VAHQ Reports can then be generated for appropriate use and distribution.

## *VISTA* Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Department of Veterans Affairs provides a unique opportunity to assist public health surveillance activities for new, antibiotic-resistant, or otherwise problematic pathogens. The Laboratory EPI software interface will obtain data from the V*ist*A database and report the data to a registry that will assist the Emerging Pathogens Initiative of the VAHQ Infectious Disease Program Office to produce predictive trends in health care events.

The EPI software consists of two new files, 10 new routines, two mail groups, one menu consisting of three options, and one Emerging Pathogens Nightly Task option. After installation minimal file setup will be required. Two mail groups are created and will require populating with the appropriate members. Some of the Emerging Pathogens data will have to be added using the Emerging Pathogens Parameter update option if the installation process cannot make the match. IRM personnel will assign the Emerging Pathogens Primary Menu to a specified user (TQI/QI/QA staff, Laboratory Information Manager (LIM), and Microbiology personnel are highly recommended).

The Search/Extract process runs once a month. This process uses the criteria defined in the EMERGING PATHOGEN file (#69.5) to search the verified Lab results in the LAB DATA file (#63) and PTF file (#45) for any of the defined Emerging Pathogens. If an Emerging Pathogen is identified the Search/Extract process builds an entry into the ^TMP global along with the appropriate inpatient or outpatient information. An inpatient associated PTF number is placed into the EMERGING PATHOGEN file (#69.5) for the appropriate Emerging Pathogen until the inpatient is discharged. During the sequential months the inpatient associated PTF record is monitored until discharged. The additional discharge information is sent to Austin as a “patient update.”

#### Local Reports 

On a monthly basis the EPI data is transmitted to the AITC. Before the EPI data is transmitted, an Emerging Pathogens Verification Report is available for the sites to review, verify, and make corrections if needed. After the EPI data is transmitted to AITC, it is then added to the National Database.

The purpose of the Emerging Pathogen Verification Report is to determine that the information being sent to ACC is accurate (i.e. complete social security numbers, valid Date of Births, and the Period of Services are present). The purpose of verification is not to determine that the total reported for actual laboratory or ICD collected data are valid (i.e. that there were X numbers of cases of positive tests for Hepatitis C or that there were X positive culture results for Streptococcus, Group A). The validation of laboratory and ICD capture should be done with the initial setup of the patch and at intermittent periodic review as determined by site (e.g. see Appendix section).

## Austin Automation Center:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Austin Automation Center creates two file structures, both in Statistical Analysis System (SAS) file format, which are used primarily as a source of data for the Infectious Diseases Program Office. The data will be available to the Infectious Diseases Program Office to be manipulated and used for analysis and reporting.

The two file structures are referred to as the “Numerators” and the “Denominators” because of their planned utilization.

<u>Numerator:</u>

This file is an accumulation of the EPI data sent from all medical centers. It will contain twelve individual months’ worth of data and will be updated monthly. Each month the oldest month will be dropped from the file and the latest month’s data will be added. Upon receipt of the monthly input, the AITC will return acknowledgments to the facility, and will identify any “problem” transmissions. These “problem” transmissions are records that, because of field format or the actual field value, either Austin is rejecting as invalid records or is just warning the facility that the record has some discrepancy, but it is not being rejected. Both the “problem” transmissions and the accepted records are documented on a Processing Report that will be transmitted from Austin to the facility. This Processing Report will itemize all of the transmissions received by Austin and will document the records status as either being accepted or rejected (with the reason code identified) but with a warning that there is something unusual about the value of one or more fields (warning reason code identified). An example of the “Tables of Reject and Warning codes” are located in the Appendix section of this guide. The Numerator information will be specific to unique patients with a VAHQ designated Emerging Pathogen which has been flagged through the V*ist*A process. Numerator data will be collected and transmitted to Austin monthly.

<u>Denominator:</u>

This file will provide to the Infectious Diseases Program Office, data elements for each facility. The source of these data elements will be the corporate medical data base residing in Austin. The individual files that these data elements will be extracted from are the National Patient Care (NPC), Inpatient Treatment File (PTF), Automated Management Information System (AMIS) and Cost Distribution Report (CDR) systems.

The data elements are:

Unique SSN served (inpatient and outpatient together)

Total \# of discharges

Total unique SSN discharges

Inpatient hospital days

Inpatient ICU days

Unique SSN encounters for both inpatient and outpatient

A “running 12 month” accumulation is required (i.e., there will always be one year’s worth of monthly counts) with the oldest month dropped off each cycle and a new one added.

> **NOTE:** The need to track individual station data and to consolidate by parent station has not been specified. At this time we are only gathering by individual station number.

![](laboratory-version-5-2-epi-technical-and-user-guide/002.png)

![](laboratory-version-5-2-epi-technical-and-user-guide/003.png)

## EPI Technical and User Guide Notations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section addresses the symbols and computer dialogue that are displayed in this guide.

### Screen Displays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPI Primary menu options are using VA FileMan-ScreenMan forms for editing and displaying data. For detailed instructions using ScreenMan forms please refer to the VA FileMan V. 21.0 User Manual, Section 6 - ScreenMan.

### Computer Dialogue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The computer dialogue appears in Courier font, no larger than 10 points.

Example: Courier font 10 points

### User Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User entry response appears in boldface type Courier font, no larger than 10 points.

Example: Boldface type

### Return Symbol \<Enter\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User response to computer dialogue is followed by the \<Enter\> symbol which appears in Courier font, no larger than 10 points, and bolded.

Example: \<Enter\>

### Tab Symbol \<Tab\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User response to computer dialogue is followed by the \<Tab\> symbol which appears in Courier font, no larger than 10 points, and bolded.

Example: \<Tab\>

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel V. 8.0 Systems Manual
HL7 V. 1.6 Manuals
PIMS V. 5.3 Manuals
VA FileMan V. 21.0 User Manual, Section 6 - ScreenMan.

### ### EPI Technical and User Guide Distributions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPI Technical and User Guide is distributed in hard copy and electronic formats. Listed below are the ways the EPI guide may be obtained.

#### Electronic Distributions

#### Hyper Text Markup Language (HTML)

The EPI Technical and User Guide is available on the Intranet at the following address <span id="p421_8" class="anchor"></span>[http://www.va.gov/vdl/application.asp?appid=118](http://www.va.gov/vdl/application.asp?appid=118)

#### Portable Document Format (PDF)

The EPI Technical and User Guide is available on the ANONYMOUS.SOFTWARE accounts at the Albany, Hines, and Salt Lake City Information Resources Management Field Offices (IRMFOs) in the Portable Document Format (PDF).

IRMFO FTP Address

<span class="mark">REDACTED</span>

<span class="mark">REDACTED</span>

<span class="mark">REDACTED</span>

> **NOTE:** This guide is also available in PDF on the Intranet at the following address [http://www.va.gov/vdl/application.asp?appid=118](http://www.va.gov/vdl/application.asp?appid=118)

#### Hard Copy

The EPI Technical and User Guide hard copies are distributed to all VA Medical Centers by the National Center for Documentation (NCD).

# Pre-installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** For patch LR\*5.2\*442 pre-installation instructions, please refer to the ICD-10 PTF Modifications Installation Guide: <http://www.va.gov/vdl/application.asp?appid=118>NOTE: For patch LR\*5.2\*421 pre-installation instructions, please refer to the ICD-10 Release Notes for LR\*5.2\*421.

This Pre-Installation Instructions section provides the necessary information and requirements for installing EPI Patch LR\*5.2\*132.

## Hardware and Operating System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*VISTA *software operates on two hardware platforms. The hardware platforms are mini-computer category, providing <u>multi-tasking</u> and <u>multi-user</u> capabilities.

The hardware systems are:

 Digital Equipment Corporation (DEC) Alpha series using DEC Open Virtual Memory System (VMS), Version 6.1 or greater, operating system. This platform uses DEC System Mumps (DSM), version 6.3 or greater, of American National Standards Institutes (ANSI) of Massachusetts General Hospital Utility Multi-Programming System (MUMPS) also known as ‘M’ language. MUMPS is a Federal Information Processing Standard (FIPS) language.

- Personal Computer (PC) System with 486 or Pentium computer processor chip using Microsoft Disk Operating System (MS-DOS). This platform uses Micronetics Standard Mumps (MSM), Version 3.0.14 or greater, of American National Standards Institutes (ANSI) of Massachusetts General Hospital Utility Multi-Programming System (MUMPS) also known as 'M' language. MUMPS is a Federal Information Processing Standard (FIPS) language.

## Performance/Capacity Impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no changes in the performance of the system once the installation process is complete.

## Backup Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## It is <u>highly</u> recommended that a backup of the transport global is performed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## EPI Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chart displays the sites that assisted in testing the EPI Patch LR\*5.2\*132 prior to the release date.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 28%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Test Site</strong></td>
<td><strong>Type of Test Site</strong></td>
<td><strong>Date Installed</strong></td>
<td><p><strong>Hardware Platform</strong></p>
<p><strong>/Operating System</strong></p></td>
</tr>
<tr class="even">
<td>Cincinnati VAMC</td>
<td>Alpha</td>
<td>11/4/96 test and production accounts</td>
<td>DEC Alpha/DSM</td>
</tr>
<tr class="odd">
<td>Miami VAMC</td>
<td>Beta</td>
<td>1/9/97 test and production accounts</td>
<td>DEC Alpha/DSM</td>
</tr>
<tr class="even">
<td>Muskogee VAMC</td>
<td>Beta</td>
<td>1/27/97 test and production accounts</td>
<td>MSM</td>
</tr>
<tr class="odd">
<td>North Hampton VAMC</td>
<td>Beta</td>
<td>1/28/97 test and production accounts</td>
<td>MSM</td>
</tr>
</tbody>
</table>

## Test Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## It is <u>highly</u> recommended that the EPI Patch LR\*5.2\*132 is installed into a test account before installing into a live Production Account. The Test and Production Accounts must include all required software versions and patches to assure a successful installation of this patch.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The actual installation time for this patch should take no more than 10 minutes. Although users may remain on the system, it is recommended that you install this patch during non-peak hours.

## Kernel Installation and Distribution System (KIDS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel Installation and Distribution System(KIDS) is a new method of installing DHCP software and a new module in Kernel Version 8.0. The Emerging Pathogens Initiative LR\*5.2\*132 patch is distributed using KIDS. For further instructions on using KIDS please refer to the Kernel Version 8.0 Systems Manual.

## Health Level Seven (HL7) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Emerging Pathogen Initiative Patch LR\*5.2\*132 is using the DHCP HL7 software to transport the EPI health care data onto the AITC, formerly AAC system. These health care data are extracted from the Laboratory, PIMS, Social Work, and EPI data bases. The health care data are used to assist public health surveillance activities for new antibiotic - resistant or otherwise problematic pathogens. The EPI health care data reside on the AITC system.

## Database Integration Agreements (DBIA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new DBIA was approved for VistA Laboratory ICD-10 PTF Modifications patch LR\*5.2\*442:

- DBIA#6130

There are three DBIAs (#418, \#1372, and \#1881) that were approved for the EPI Patch LR\*5.2\*132.

## EPI Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The below routine list includes three routines (LRAPQAT1, LREPI3 and LREPI5) that have been modified for patch LR\*5.2\*442.NOTE: The below routine list includes three routines (LR421P, LREPICD, and LRESPIXDG) that have been added for Patch LR\*5.2\*421.

- LR132
- LR132P
- LR175
- LR175P
- LR421P
- LRAPQAT1
- LREPI
- LREPI1A
- LREPI2
- LREPI3
- LREPI4
- LREPI5
- LREPIAK
- LREPICD
- LREPICY
- LREPILK
- LREPIPH
- LREPIPI
- LREPIRM
- LREPIRN
- LREPIRP
- LREPIRP3
- LREPIRP5
- LREPIRP7
- LREPIRS1
- LREPIRS3
- LRESPIXDG

## Staffing Requirement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IRM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM staff is required for installing EPI Patch LR\*5.2\*132, setting up the EPI-Domain, EPI-Lab mail groups and menu assignments.

### Laboratory Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is <u>highly</u> <u>recommended</u> that the Laboratory Information Manager (LIM), and a representative from the Microbiology section (director, supervisor, or technologist) <u>jointly</u> participate in reviewing the 14 Emerging Pathogen descriptions and entering of data for the EPI software package. The individual(s) will assist in the initially setting of the EPI parameters and doing periodic reviews of the parameters to assure they are current.

### Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that a Total Quality Improvement/Quality Improvement/ Quality Assurance (TQI/QI/QA) staff (or persons at site with similar function) be involved in the EPI process due to the multi-disciplinary nature of the information to be retrieved by the EPI program (both patient-specific for pathogens and site-specific for denominators). This will facilitate coordination of subsequent site interactions once the actual patch has been installed (i.e. to be responsible for reviewing verification reports, transmitting data once it is determined to be correct, review the data error messages and make corrections as needed, periodic validation of verification reports, to assist with coordinating the yearly update of parameters, and the intermittent specific update of parameters requests from Veterans Affairs Headquarters).

## *VISTA*\DHCP Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Packages Versions (or Greater)

VA FileMan 21 (with patches installed)

Kernel 8.0 (with patches installed)

Laboratory 5.2 (with patches installed)

MAS/PIMS 5.3 (with patches installed)

HL7 1.6 (with patches installed)

Social Work 3.0 (with patches installed)

MailMan 7.1 (with patches installed)

## Patches Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** For patches required for LR\*5.2\*442, please refer to the ICD-10 PTF Modifications Installation Guide: <http://www.va.gov/vdl/application.asp?appid=118>

Prior to the installation of LR\*5.2\*132, the following patches MUST be installed:

Packages Patches

Kernel V. 8.0 XU\*8\*44

MailMan V.7.1 XM\*DBA\*103 (EPI-Lab Domain)

Health Level Seven V. 1.6 HL\*1.6\*17

Laboratory V. 5.2 LR\*5.2\*128

Social Work V. 3.0 SOW\*3\*42 (install after LR\*5.2\*128)

## ## EPI Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EMERGING PATH PROTOCOL file (#69.4): This file contains additional parameters that are not specific to entries in EMERGING PATHOGENS file (#69.5), but are specific to the protocol used.

EMERGING PATHOGENS file (#69.5): This file contains search criteria along with additional information associated with the Emerging Pathogen Initiative (EPI) software. This file should only be edited using the ScreenMan ‘Emerging Pathogens Parameter update’ option which is provided by the EPI Software.

## EPI Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPI Patch LR\*5.2\*132 is using Laboratory’s LR namespace.

## EPI Menu and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory EPI software has one stand-alone menu. There are no locks or security keys created for this menu. The Emerging Pathogen Primary Menu consists of the following three options:

Antimicrobial Link Update: This option will allows the user to link the ANTIMICROBIAL SUSCEPIBILTY' file (#62.06) with WKLD CODE file (#64).

> **NOTE:** Please see the Appendix section of this guide on “How to Link Antimicrobial Entries to Workload Codes Entries” using this option.

Emerging Pathogen Manual Run: This option allows the user to select any month to run the Search/Extract process manually. The first and last day of the month will be determined automatically.

Emerging Pathogens Parameter update: This option is used to define the search criteria along with additional information associated with the Emerging Pathogen Initiative.

> **NOTE:** The Emerging Pathogen Primary Menu options are using VA FileMan screens displays, referred to as ScreenMan. For detailed instructions on how to use the screens displays please review the VA FileMan V. 21.0 User Manual, Section 6 ScreenMan.

## Emerging Pathogens Nightly Task Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Emerging Pathogens Nightly Task option must be scheduled to run each night by TaskMan. This option will build the Emerging Pathogen HL7 Message for Austin. The HL7 message is built after the 15<sup>th</sup> day of each month for the previous month search data.

## New <span class="mark">REDACTED</span> Domain

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new <span class="mark">REDACTED</span> domain implementation instructions are released by MailMan XM\*DBA\*103 informational patch.

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LREP: This event driver protocol defines the associated parameters needed to build the HL7 Message used to send the EPI data to Austin.

LREPI CLIENT: This subscriber protocol defines the parameter needed by the HL7 package to determine where to send the HL7 formatted message containing the EPI information.

## ## EPI-Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPI Patch LR\*5.2\*132 creates two mail groups during the installation process.

EPI: This mail group is used for the transmission of HL7 messages derived from the parameters defined in the EMERGING PATHOGEN file (#69.5) to the Austin Automation Center. This mail group will also receive Confirmation and Processing Report Messages from Austin.

EPI-REPORT: This mail group is used to deliver a formatted report taken from the HL7 message that is created to assist in the verification of data.

> **NOTE:** The Office of the Director (00) will be the initial individual/function to whom the EPI mail and EPI-Report mail groups will be directed. The Office of the Director at each site will then determine responsible individual(s)/function(s) for the mail groups. For further information regarding the EPI mail groups please see the Appendix section page 122.

> **NOTE:** To transmit a mail message please reference the example in the Appendix section of this guide.

## Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EMERGING PATH PROTOCOL file (#69.4)

STANDARD DATA DICTIONARY \#69.4 -- EMERGING PATH PROTOCOL FILE 01/30/97 PAGE 1

STORED IN ^LAB(69.4, (1 ENTRY) SITE: DALLAS ISC-DEVELOPMENT

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

This file contains additional parameters that are not specific to entries in file (#69.5), but are specific to the protocol used.

POINTED TO BY: PROTOCOL field (#12) of the EMERGING PATHOGENS File (#69.5)

CROSS REFERENCED BY: PROTOCOL(B)

CREATED ON: NOV 8,1996

69.4,.01 PROTOCOL 0;1 POINTER TO PROTOCOL FILE (#101)

(Required)

INPUT TRANSFORM: S DINUM=X

LAST EDITED: NOV 08, 1996

> DESCRIPTION: Select the protocol from the Protocol file

(#101) that will be used to build the HL7

Message. This allows additional parameters to

be associated with the protocol.

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

CROSS-REFERENCE: 69.4^B

1)= S ^LAB(69.4,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.4,"B",\$E(X,1,30),DA)

69.4,1 Report Mail Group 0;2 POINTER TO MAIL GROUP FILE (#3.8)

LAST EDITED: NOV 08, 1996

HELP-PROMPT: Select what mail group to send the verification

report.

DESCRIPTION: This defines what mail group to send the

verification report.

69.4,2 Message Size 0;3 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>999999)!(X\<100)!(X?.E1"."1N.N) X

LAST EDITED: DEC 04, 1996

HELP-PROMPT: Type a Number between 100 and 999999, 0 Decimal

Digits.

DESCRIPTION: This determines how big the HL7 message will be

before it breaks into another message.

FILES POINTED TO FIELDS

MAIL GROUP (#3.8) Report Mail Group (#1)

PROTOCOL (#101) PROTOCOL (#.01)

INPUT TEMPLATE(S):

PRINT TEMPLATE(S):

SORT TEMPLATE(S):

FORM(S)/BLOCK(S):

EMERGING PATHOGENS file (#69.5)

STANDARD DATA DICTIONARY \#69.5 -- EMERGING PATHOGENS FILE 01/30/97 PAGE 1

STORED IN ^LAB(69.5, (14 ENTRIES) SITE: DALLAS ISC-DEVELOPMENT ACCOUNT

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

------------------------------------------------------------------------------

This file contains search criteria along with additional information associated

with the Emerging Pathogen Initiative (EPI) software. This file should only be edited using the ScreenMan 'Emerging Pathogens Parameter update' option that is provided by the EPI software.

CROSS REFERENCED BY: NAME(B), REFERENCE NUMBER(C)

CREATED ON: AUG 29,1996

69.5,.01 NAME 0;1 FREE TEXT (Required)

INPUT TRANSFORM: K:\$L(X)\>50!(\$L(X)\<3)!'(X'?1P.E)!(X'?.ANP) X

LAST EDITED: DEC 17, 1996

HELP-PROMPT: Answer must be 3-50 characters in length.

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

DESCRIPTION: This is the name of the Search/Extract

parameters you are defining.

CROSS-REFERENCE: 69.5^B

1)= S ^LAB(69.5,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,"B",\$E(X,1,30),DA)

69.5,.05 REFERENCE NUMBER 0;9 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>999)!(X\<1)!(X?.E1"."1N.N)!(X'\>99)!

(^LAB(69.5,"C",X)) X

LAST EDITED: NOV 29, 1996

HELP-PROMPT: Type a Number between 100 and 999. Numbers from

1 to 99 are reserved for future use.

UNEDITABLE

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

DESCRIPTION: This is a unique number used to identify this

entry.

CROSS-REFERENCE: 69.5^C

1)= S ^LAB(69.5,"C",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,"C",\$E(X,1,30),DA)

69.5,1 ACTIVE 0;2 SET

'0' FOR YES;

'1' FOR NO;

LAST EDITED: AUG 29, 1996

HELP-PROMPT: Indicates if the entry is active or inactive.

DESCRIPTION: This defines if this entry is active or not.

69.5,2 LAB TEST 1;0 POINTER Multiple \#69.52

DESCRIPTION: This is the test that is searched for.

69.52,.01 LAB TEST 0;1 POINTER TO LABORATORY TEST FILE (#60)

(Multiply asked)

INPUT TRANSFORM: I \$P(\$G(^(0)),U,4)="CH" D ^DIC K DIC S DIC=DIE

,X=+Y K:Y\<0 X

LAST EDITED: OCT 07, 1996

HELP-PROMPT: Consider this synonymous with chemistry, serology,

hematology “blood/serum” test.  
STANDARD DATA DICTIONARY \#69.5 -- EMERGING PATHOGENS FILE 01/30/97 PAGE 2

STORED IN ^LAB(69.5, (14 ENTRIES) SITE: DALLAS ISC-DEVELOPMENT ACCOUNT

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

------------------------------------------------------------------------------

DESCRIPTION: This is the lab test that is searched for and

retrieved.

SCREEN: I \$P(\$G(^(0)),U,4)="CH"

EXPLANATION: Only CH subscripts are selectable.

CROSS-REFERENCE: 69.52^B

1)= S ^LAB(69.5,DA(1),1,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),1,"B",\$E(X,1,30),DA)

69.52,1 INDICATOR 0;2 SET

'1' FOR Use Reference Ranges;

'2' FOR Contains;

'3' FOR Greater Than;

'4' FOR Less Than;

'5' FOR Equal to;

LAST EDITED: SEP 18, 1996

HELP-PROMPT: Select the Code that will determine how to match

lab results

DESCRIPTION: This indicates if the search for the lab test

is conditional.

69.52,2 INDICATED VALUE 0;3 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>15!(\$L(X)\<1) X

LAST EDITED: SEP 17, 1996

HELP-PROMPT: Answer must be 1-15 characters in length.

DESCRIPTION: If the search is conditional this defines the

criteria.

69.5,3 ETIOLOGY 2;0 POINTER Multiple \#69.53

DESCRIPTION: This defines the Etiology to search for.

69.53,.01 ETIOLOGY 0;1 POINTER TO ETIOLOGY FIELD FILE (#61.2)

(Multiply asked)

LAST EDITED: AUG 29, 1996

HELP-PROMPT: Select the Etiology to search for.

DESCRIPTION: This defines the Etiology to search for.

Select the appropriate Etiology.

CROSS-REFERENCE: 69.53^B

1)= S ^LAB(69.5,DA(1),2,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),2,"B",\$E(X,1,30),DA)

<span id="File695" class="anchor"></span>69.5,4         ICD DIAGNOSIS          3;0 POINTER Multiple \#69.54

               LAST EDITED:      JUN 12, 2012

               DESCRIPTION:      This defines the ICD to search for. 

69.54,.01       ICD DIAGNOSIS          0;1 POINTER TO ICD DIAGNOSIS FILE (#80)

                                    (Multiply asked)

                LAST EDITED:      SEP 17, 2012

                HELP-PROMPT:      Select the ICD standardized code, used

                                 nationwide in federal and non-federal private

                                  health care facilities, to be included in the search.

                DESCRIPTION:      This defines an ICD for use in emerging

                                  pathogens data search/extract. 

                CROSS-REFERENCE:  69.54^B                                  

> 1)= S LAB(69.5,DA(1),3,"B",\$E(X,1,30),DA)=""

                                  2)= K ^LAB(69.5,DA(1),3,"B",\$E(X,1,30),DA)

69.54,1         CODING SYSTEM     0;2 POINTER TO ICD CODING SYSTEMS FILE (#80.4)

                LAST EDITED:      AUG 10, 2012

                HELP-PROMPT:      Enter the applicable ICD coding system for

                                  this ICD.

69.5,5 ANTIMICROBIAL SUSCEPTIBILITY 4;0 POINTER Multiple \#69.55

LAST EDITED: JAN 22, 1997

DESCRIPTION: This determines that if any of the Etiologies

selected are to be resistant to any

Antimicrobials.

69.55,.01 ANTIMICROBIAL SUSCEPTIBILITY 0;1 POINTER TO ANTIMICROBIAL

SUSCEPTIBILITY FILE (#62.06) (Multiply asked)

LAST EDITED: JAN 22, 1997

HELP-PROMPT: Enter the Antimicrobial that will be used in

screening out sensitive Etiologies.

DESCRIPTION: This determines that if any of the Etiologies

selected are to be resistant to any

Antimicrobials. Select the appropriate

Antimicrobials to screen out the Etiologies.

CROSS-REFERENCE: 69.55^B

1)= S ^LAB(69.5,DA(1),4,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),4,"B",\$E(X,1,30),DA)

69.5,6 INCLUDED SITES 5;0 POINTER Multiple \#69.56

LAST EDITED: OCT 04, 1996

DESCRIPTION: This determines what Topography to screen for.

69.56,.01 TOPOGRAPHY 0;1 POINTER TO TOPOGRAPHY FIELD FILE (#61)

(Multiply asked)

LAST EDITED: OCT 04, 1996

HELP-PROMPT: selection of a Topography screens all others out

except the ones selected. For “ALL” leave blank.

Not to be used in conjunction with the exclude

Topography

DESCRIPTION: This determines what Topography to screen

for. Select the appropriate Topography to

include in the extract.

CROSS-REFERENCE: 69.56^B

1)= S ^LAB(69.5,DA(1),5,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),5,"B",\$E(X,1,30),DA)

69.5,7 EXCLUDED SITES 6;0 POINTER Multiple \#69.57

DESCRIPTION: This determines what Topography to screen out.

69.57,.01 TOPOGRAPHY 0;1 POINTER TO TOPOGRAPHY FIELD FILE (#61)

(Multiply asked)

LAST EDITED: OCT 04, 1996

HELP-PROMPT: Select the Topography to out. Not to be used in

conjunction with the Include Topography selection.

DESCRIPTION: This determines what Topography to screen

out. Select the appropriate Topography to be

excluded from the extract.

STANDARD DATA DICTIONARY \#69.5 -- EMERGING PATHOGENS FILE 01/30/97 PAGE 4

STORED IN ^LAB(69.5, (14 ENTRIES) SITE: DALLAS ISC-DEVELOPMENT ACCOUNT

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

CROSS-REFERENCE: 69.57^B

1)= S ^LAB(69.5,DA(1),6,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),6,"B",\$E(X,1,30),DA)

69.5,9 RUN DATE 0;4 DATE

INPUT TRANSFORM: S %DT="ESTX" D ^%DT S X=Y K:Y\<1 X

LAST EDITED: OCT 09, 1996

HELP-PROMPT: Date that the last Auto Search/Extract processed.

DESCRIPTION: The date that the last Auto Search/Extract

processed

69.5,10 CYCLE 0;5 SET

'Y' FOR YEARLY;

'M' FOR MONTHLY;

'W' FOR WEEKLY;

'D' FOR DAILY;

LAST EDITED: OCT 09, 1996

HELP-PROMPT: This field is currently not used. For future use.

DESCRIPTION: This field is not currently used.

69.5,11 FIRST ENCOUNTER 0;6 SET

'1' FOR YES;

'0' FOR NO;

LAST EDITED: DEC 30, 1996

HELP-PROMPT: Limits the output to the first encounter for the

DESCRIPTION: This determines if after the first encounter is

found and extracted should sequential

encounters be extracted. patient. Otherwise list all

encounters.

69.5,12 PROTOCOL 0;7 POINTER TO EMERGING PATH PROTOCAL FILE (#69.4)

LAST EDITED: NOV 08, 1996

HELP-PROMPT: Defines the protocol used to define the output

message.

DESCRIPTION: This defines what protocol is associated with

the parameters.

69.5,13 FOLLOW PTF 0;8 SET

'1' FOR YES;

'0' FOR NO;

LAST EDITED: OCT 17, 1996

HELP-PROMPT: Indicates if the PTF record will be followed until

a discharge has been entered.

DESCRIPTION: This determines that if a inpatient encounter

does not have a discharge should the discharge

information be updated upon discharge.

69.5,14 PTF 7;0 POINTER Multiple \#69.514

(Add New Entry without Asking)

DESCRIPTION: This is the Inpatient information to follow.

STANDARD DATA DICTIONARY \#69.5 -- EMERGING PATHOGENS FILE 01/30/97 PAGE 5

STORED IN ^LAB(69.5, (14 ENTRIES) SITE: DALLAS ISC-DEVELOPMENT ACCOUNT UCI:

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

69.514,.01 PTF 0;1 POINTER TO PTF FILE (#45)

LAST EDITED: OCT 17, 1996

DESCRIPTION: This is the Inpatient information to follow.

CROSS-REFERENCE: 69.514^B

1)= S ^LAB(69.5,DA(1),7,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),7,"B",\$E(X,1,30),DA)

69.514,1 DATE 0;2 DATE

INPUT TRANSFORM: S %DT="E" D ^%DT S X=Y K:Y\<1 X

LAST EDITED: DEC 31, 1996

DESCRIPTION: This is the date that the Inpatient discharge

information was included in the report as a

update.

69.5,15 Description 8;0 WORD-PROCESSING \#69.515

DESCRIPTION: This is the general description for the entry.

FILES POINTED TO FIELDS

ANTIMICROBIAL SUSCEPTIBILITY ANTIMICROBIAL SUSCEPTIBILITY:ANTIMICROBIAL

(#62.06) SUSCEPTIBILITY (#.01)

EMERGING PATH PROTOCAL (#69.4) PROTOCOL (#12)

ETIOLOGY FIELD (#61.2) ETIOLOGY:ETIOLOGY (#.01)

<span id="p421_21" class="anchor"></span>ICD CODING SYSTEMS (#80.4) ICD DIAGNOSIS:CODING SYSTEM (#1)

ICD DIAGNOSIS (#80) ICD DIAGNOSIS:ICD DIAGNOSIS (#.01)

LABORATORY TEST (#60) LAB TEST:LAB TEST (#.01)

PTF (#45) PTF:PTF (#.01)

TOPOGRAPHY FIELD (#61) INCLUDED SITES:TOPOGRAPHY (#.01)

EXCLUDED SITES:TOPOGRAPHY (#.01)

INPUT TEMPLATE(S):

PRINT TEMPLATE(S):

CAPTIONED USER \#0

SORT TEMPLATE(S):

FORM(S)/BLOCK(S):

LREPI OCT 07, 1996@10:13 USER \#6459

LREPIHEAD DD \#69.5

LREPI2 DD \#69.52

LREPI3 DD \#69.54

LREPI1 DD \#69.5

LREPI11 DD \#69.5

LREPI4 DD \#69.53

LREPI5 DD \#69.55

LREPI6 DD \#69.5

LREPI7 DD \#69.5

LREPI8 DD \#69.56

LREPI9 DD \#69.57

LREPI10 DD \#69.5

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="PIIFix2" class="anchor"></span>NOTE: For patch LR\*5.2\*442 installation instructions, please refer to the ICD-10 PTF Modifications Installation Guide: <http://www.va.gov/vdl/application.asp?appid=118>

> **NOTE:** For patch LR\*5.2\*421 installation instructions, please refer to the ICD-10 Release Notes.

For Patch LR\*5.2\*132:

The Kernel Installation and Distribution System (KIDS) is a new method of installing VISTA software and the replacement for DIFROM. The EPI patch LR\*5.2\*132 is using the KIDS standard distribution. The KIDS standard distributions are done in three phases:

Phase 1: Loading transport globals from a PackMan message.

Phase 2: Answering installation questions for transport globals in a distribution.

Phase 3: KIDS installation of the patch.

> **NOTE:** For further instructions on using KIDS, please refer to the Kernel V. 8.0 Systems Manual, Chapter 26, pages 393-409.

## Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The actual installation time for this patch should take no more than 10 minutes. Although users may remain on the system, it is recommended that you install this patch during off-peak hours.

> **NOTE:** Kernel Patch XU\*8\*44 MUST be installed prior to installing EPI Patch LR\*5.2\*132 or this installation of will abort.

## Installation Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of the terminal screen dialogue seen during the KIDS install. However, the dates shown will not be the same as those on the released version.

Phase 1: Loading transport globals from a PackMan message.

KIDS Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: \<Enter\>Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 2\<Enter\> Verify Checksums in Transport Global

Select INSTALL NAME: LR\*5.2\*132\<Enter\> Loaded from Distribution 1/23/97@07:36:06

=\> LR\*5.2\*132

DEVICE: HOME//\<Enter\>

PACKAGE: LR\*5.2\*132 Jan 23, 1997 7:57 am PAGE 1

----------------------------------------------------------------------------

10 Routine checked, 0 failed.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 5\<Enter\> Backup a Transport Global

Select INSTALL NAME: LR\*5.2\*132\<Enter\> Loaded from Distribution 1/23/97@07:36:06

=\> LR\*5.2\*132

This Distribution was loaded on Jan 23, 1997@07:36:06 with header of

LR\*5.2\*132

It consisted of the following Install(s):

LR\*5.2\*132

Subject: BACKUP 132

Loading Routines for LR\*5.2\*132.

Routine LR132P is not on the disk.......

Routine LREPILK is not on the disk...

Routine LREPIRP is not on the disk..

Send mail to: LABMAIL,ONE\<Enter\> Last used MailMan: 23 Jan 97 07:54

Select basket to send to: IN//\<Enter\>

And send to: \<Enter\>Phase 2: Answering installation questions for transport globals in a distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 6\<Enter\> Install Package(s)

Select INSTALL NAME: LR\*5.2\*132\<Enter\> Loaded from Distribution 1/23/97@07:36:06

=\> LR\*5.2\*132

This Distribution was loaded on Jan 23, 1997@07:36:06 with header of

LR\*5.2\*132

It consisted of the following Install(s):

LR\*5.2\*132

LR\*5.2\*132

Will first run the Environment Check Routine, LR132

Environment Check is Ok ---

Install Questions for LR\*5.2\*132

62.06 ANTIMICROBIAL SUSCEPTIBILITY (Partial Definition)

> **NOTE:** You already have the 'ANTIMICROBIAL SUSCEPTIBILITY' File.

69.4 EMERGING PATH PROTOCOL

69.5 EMERGING PATHOGENS (including data)

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO\<Enter\>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//\<Enter\>Phase 3: KIDS installation of the patch.

Install Started for LR\*5.2\*132 :

Jan 23, 1997@07:59:07

Installing Routines:

Jan 23, 1997@07:59:08

Installing Data Dictionaries:

Jan 23, 1997@07:59:12

Installing Data:

Jan 23, 1997@07:59:13

Installing PACKAGE COMPONENTS:

Installing HELP FRAME

Installing FORM

Installing MAIL GROUP

Installing HL LOWER LEVEL PROTOCOL PARAMETER

Installing HL LOGICAL LINK

Installing HL7 APPLICATION PARAMETER

Installing PROTOCOL

Installing OPTION

Jan 23, 1997@07:59:24

Running Post-Install Routine: ^LR132P

Adding Protocol 'LREPI' to the Emerging Pathogen File (69.5)

\*\*\*\*\*\*\*\*

\*\*Updating Emerging Pathogen File (69.5) with ICD9 Codes\*\*

Adding 085.0 VISCERAL LEISHMANIASIS into LEISHMANAISIS

Adding 085.1 CUTAN LEISHMANIAS URBAN into LEISHMANAISIS

Adding 085.2 CUTAN LEISHMANIAS ASIAN into LEISHMANAISIS

Adding 085.3 CUTAN LEISHMANIAS ETHIOP into LEISHMANAISIS

Adding 085.4 CUTAN LEISHMANIAS AMER into LEISHMANAISIS

Adding 085.5 MUCOCUTAN LEISHMANIASIS into LEISHMANAISIS

Adding 085.9 LEISHMANIASIS NOS into LEISHMANAISIS

Adding 084.0 FALCIPARUM MALARIA into MALARIA

Adding 084.1 VIVAX MALARIA into MALARIA

Adding 084.2 QUARTAN MALARIA into MALARIA

Adding 084.3 OVALE MALARIA into MALARIA

Adding 084.4 MALARIA NEC into MALARIA

Adding 084.5 MIXED MALARIA into MALARIA

Adding 084.6 MALARIA NOS into MALARIA

Adding 084.7 INDUCED MALARIA into MALARIA

Adding 084.8 BLACKWATER FEVER into MALARIA

Adding 084.9 MALARIA COMPLICATED NEC into MALARIA

Adding 007.8 PROTOZOAL INTEST DIS NEC into CRYPTOSPORIDIUM

Adding 046.1 JAKOB-CREUTZFELDT DIS into CREUTZFELDT-JAKOB DISEASE

Adding 061. DENGUE into DENGUE

Adding 065.4 MOSQUITO-BORNE HEM FEVER into DENGUE

Adding 482.80 LEGIONNAIRE'S DISEASE into LEGIONELLA

\*\*\*\*\*\*\*\*

\*\*Updating Emerging Pathogen File (69.5) with Etiology\*\*

Adding CANDIDA ALBICANS into CANDIDA

Adding CANDIDA GUILLIERMONDII into CANDIDA

Adding CANDIDA KRUSEI into CANDIDA

Adding CANDIDA PARAPSILOSIS into CANDIDA

Adding CANDIDA PSEUDOTROPICALIS into CANDIDA

Adding CANDIDA SKIN TEST ANTIGEN into CANDIDA

Adding CANDIDA STELLATOIDEA into CANDIDA

Adding CANDIDA TROPICALIS into CANDIDA

Adding CANDIDA, NOS into CANDIDA

Adding ENTEROCOCCUS (STREPT. FAECALI into VANC-RES ENTEROCOCCUS

Adding LEGIONELLA BOZEMANII into LEGIONELLA

Adding LEGIONELLA DUMOFFII into LEGIONELLA

Adding LEGIONELLA MICDADEI into LEGIONELLA

Adding LEGIONELLA PNEUMOPHILIA into LEGIONELLA

Adding LEGIONELLA SP into LEGIONELLA

I will auto link file '62.06 ANTIMICROBIAL SUSCEPTIBILITY' to file '64 WKLD CODE.

AMIKACN \<----Linked----\> Amikacin

AMPICLN \<----Linked----\> Ampicillin

CLINDAM \<----Linked----\> Clindamycin

CARBCLN \<----Linked----\> Carbenicillin

CEFMAND \<----Linked----\> Cefamandole

CEFOPERAZONE \<----Linked----\> Cefoperazone

CEFOTAXIME \<----Linked----\> Cefotaxime

CEFOXITIN \<----Linked----\> Cefoxitin

CEFAZOLIN \<----Linked----\> Cefazolin

CHLORAM \<----Linked----\> Chloramphenicol

ERYTHROMYCIN \<----Linked----\> Erythromycin

KANAMCN \<----Linked----\> Kanamycin

METHCLN \<----Linked----\> Methicillin

MEZLOCILLIN \<----Linked----\> Mezlocillin

NEOMYCN \<----Linked----\> Neomycin

NETILMICIN \<----Linked----\> Netilmicin

NITROFURANTOIN \<----Linked----\> Nitrofurantoin

NOVOBIOCIN \<----Linked----\> Novobiocin

OXACILLIN \<----Linked----\> Oxacillin

PENICLN \<----Linked----\> Penicillin

PIPERACILLIN \<----Linked----\> Piperacillin

POLYMYXIN B \<----Not Linked----\> No Match Found

RIFAMPIN \<----Linked----\> Rifampin

TETRCLN \<----Not Linked----\> No Match Found

TOBRMCN \<----Linked----\> Tobramycin

TRMSULF \<----Not Linked----\> No Match Found

VANCMCN \<----Linked----\> Vancomycin

MOXALACTAM \<----Linked----\> Moxalactam

GENTMCN \<----Linked----\> Gentamicin

SULFISOXAZOLE \<----Not Linked----\> No Match Found

BACTRCN \<----Linked----\> Bacitracin

NAFCILLIN \<----Linked----\> Nafcillin

NALIDIXIC ACID \<----Linked----\> Nalidixic Acid

COLISTIN \<----Linked----\> Colistin

CEPHALOTHIN \<----Linked----\> Cephalothin

METRONIDAZOLE \<----Linked----\> Metronidazole

Updating Routine file

Updating KIDS files

LR\*5.2\*132 Installed.

Jan 23, 1997@07:59:35.

Install Message sent \#13957

Install Completed

# # Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="p421_31" class="anchor"></span>NOTE: There are no post installation instructions for LR\*5.2\*442.NOTE: For patch LR\*5.2\*421 post installation instructions, please refer to the ICD-10 Release Notes for LR\*5.2\*421.

The post installation instructions for the EPI Patch LR\*5.2\*132 should be followed as recommended. This will assure a successful implementation of the EPI software.

### DSM/Alpha Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have disabled journaling, you may now re-enable it.

### MSM Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that MSM sites move the routines to the other servers. Using a mapped system, rebuild your map set.

### IRM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Assure that the Q-EPI-MED.GOV Domain is set-up as instructed by MailMan Patch XM\*DBA\*103.

2\. Set-up the EPI-Lab and EPI-Report Lab mail groups. Recipients of these mail groups are designated by the EPI coordinator.

3\. Using VA FileMan V. 21.0 edit the facility name field in the HL7 APPLICATION PARAMETER file (#771) for the EPI-LAB entry.

Example:

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: HL7 APPLICATION PARAMETER\<Enter\>

(7 entries)

EDIT WHICH FIELD: ALL// FACILITY NAME\<Enter\>

THEN EDIT FIELD: \<Enter\>

Select HL7 APPLICATION PARAMETER NAME: EPI-LAB\<Enter\> ACTIVE

FACILITY NAME: 170\<Enter\> <u>Enter your facility number</u>

Select HL7 APPLICATION PARAMETER NAME: \<Enter\>

4\. Start the Lower Level Protocol of the HL7 V. 1.6 background job for EPI.

Select Systems Manager Menu Option: HL7 Main\<Enter\> Menu

1 V1.5 OPTIONS ...

2 V1.6 OPTIONS ...

3 Activate/Inactivate Application

4 Print/Display Menu ...

5 Purge Message Text File Entries

Select HL7 Main Menu Option: 2\<Enter\> V1.6 OPTIONS

1 Communications Server ...

2 Interface Workbench

3 Message Requeuer

Select V1.6 OPTIONS Option: 1\<Enter\> Communications Server

1 Edit Communication Server parameters

2 Manage incoming & outgoing filers ...

3 Monitor incoming & outgoing filers

4 Start LLP

5 Stop LLP

6 Systems Link Monitor

7 Logical Link Queue Management ...

8 Report

Select Communications Server Option: 4\<Enter\> Start LLP

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: EPI-LAB\<Enter\>

The LLP was last shutdown on JAN 30, 1997 12:06:19.

Select one of the following:

F FOREGROUND

B BACKGROUND

Q QUIT

Method for running the receiver: B//\<Enter\> ACKGROUND

Job was queued as 131225.

5\. Assign the Emerging Pathogen Primary Menu to specified users.

> **NOTE:** It is highly recommended that the Laboratory Information Manager (LIM), TQI/QA/QI, and a representative from the Microbiology section (director, supervisor, or technologist) are assigned the Emerging Pathogen Primary Menu. This will be the individual(s) responsible for initially setting the parameters and doing periodic reviews of parameters to assure they are current.

6\. Schedule the Emerging Pathogen Nightly Task option to run each night.

## # Health Level Seven (HL7) Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Emerging Pathogen Initiative Patch LR\*5.2\*132 is using the V*IST*A HL7 software to transport the EPI health care data onto the ACC system. This health care data is extracted from the Laboratory, PIMS, and EPI data bases. The health care data is used to assist public health surveillance activities for new antibiotic - resistant or otherwise problematic pathogens. The EPI health care data is transmitted to ACC system monthly where it will be processed.

3. General Specifications

3.1 Communication Protocol

The V*IST*A MailMan electronic mail system will be used as the communications protocol for sending HL7 messages between D V*IST*A and EPI.

3.2 Application Processing Rules

The HL7 protocol itself describes the basic rules for application processing by the sending and receiving systems. The HL7 Version 2.2 protocol will be used. The ORU message will be sent using the HL7 batch protocol.

3.3 Messages

The following HL7 messages will be used to support the exchange of EPI data.

ORU Observational Results Unsolicited

3.4 Segments

The following HL7 segments will be used to support the exchange of EPI data.

DG1 Diagnosis OBR Observation Request

MSH Message Header PID Patient Identification

NTE Notes and Comments PV1 Patient Visit

3.5 Fields: The following HL7 fields will be used to support the exchange of EPI data for each of the segments listed in the 3.4 Segments.

|         |          |                                                                                                              |                   |
|---------|----------|--------------------------------------------------------------------------------------------------------------|-------------------|
|         | FIELD    |                                                                                                              |                   |
|         | SEQUENCE |                                                                                                              | USER/HL7          |
| SEGMENT | NUMBER   | FIELD ELEMENT NAME                                                                                           | DEFINED           |
| DG1 | 1        | Set ID-Diagnosis (Sequence \#)                                                                               | HL7               |
|         | 3        | Diagnosis Code (Code(id<span id="DG1_table" class="anchor"></span>) ~Text (St.) ~ Name of coding system (st) | HL7               |
| MSH | 1        | Field Separator                                                                                              | HL7               |
|         | 2        | Encoding Characters                                                                                          | HL7               |
|         | 3        | Sending Application                                                                                          | HL7               |
|         | 4        | Sending Facility                                                                                             | HL7               |
|         | 5        | Receiving Application                                                                                        | HL7               |
|         | 6        | Receiving Facility                                                                                           | HL7               |
|         | 7        | Date/Time of Message                                                                                         | HL7               |
|         | 8        | Security                                                                                                     | HL7               |
|         | 9        | Message Type                                                                                                 | HL7               |
|         | 10       | Message Control ID                                                                                           | HL7               |
|         | 11       | Processing ID                                                                                                | HL7               |
|         | 12       | Version ID                                                                                                   | HL7               |
| OBR | 1        | Set ID-Observation Request (Seq \#)                                                                          | HL7               |
|         | 4        | Universal Service ID (identifier^ text ^ name of coding system ^ alt id ^ alt text ^ alt coding system)      | HL7               |
|         | 7        | Observation Date/Time                                                                                        | HL7               |
|         | 15       | Specimen Source (Specimen source code (CE) ^^ text (TX) )                                                    | HL7 (Table 0070)  |
|         | 26       | Parent Results (OBX observation id of parent ^OBX sub ID                                                     | HL7               |
| NTE | 1        | Set ID Notes and Comments (Seq \#)                                                                           | HL7               |
|         | 3        | Comment                                                                                                      | HL7               |
| OBX | 1        | Set Id-Observational Simple (seq. \#)                                                                        | HL7               |
|         | 2        | Value Type                                                                                                   | HL7               |
|         | 3        | Observation Identifier (identifier ^ text ^ name of coding system ^ alt id ^ alt text ^ alt coding system)   | HL7               |
|         | 4        | Sub Id                                                                                                       | HL7               |
|         | 5        | Observation Value (Result)                                                                                   | HL7               |
|         | 6        | Units (Units)                                                                                                | HL7               |
|         | 8        | Abnormal Flags                                                                                               | HL7 (Table 0078)  |
|         | 15       | Date/Time of the Observation (Verified Date/Time)                                                            | HL7               |
| PID | 2        | Patient ID (External ID)                                                                                     | HL7               |
|         | 3        | Patient ID (Internal ID)                                                                                     | HL7               |
|         | 5        | Patient Name                                                                                                 | HL7               |
|         | 7        | Date of Birth                                                                                                | HL7               |
|         | 8        | Sex                                                                                                          | HL7 (Table 0001)  |
|         | 10       | Race                                                                                                         | HL7 (Table VA07)  |
|         | 11       | Address (Homeless)                                                                                           | HL7               |
|         | 19       | SSN                                                                                                          | HL7               |
|         | 27       | Veteran’s Military Status                                                                                    | HL7 (Table Va011) |
| PV1 | 1        | Set ID - Patient Visit                                                                                       | HL7               |
|         | 2        | Patient Class                                                                                                | HL7               |
|         | 36       | Discharge Disposition                                                                                        | HL7               |
|         | 44       | Admit Date/Time (Event Date/Time)                                                                            | HL7               |
|         | 45       | Discharge Date/Time                                                                                          | HL7               |

4.0 Transaction Specifications

4.1 General

The V*ist*A system will send the ORU observation result type HL7 message whenever one or more of the defined pathogens have been identified.

4.2 Specific Transaction

> A. Identified Encounter

> When the Emerging Pathogens have been identified an ORU message is sent from the V*ist*A system to the EPI database. These ORU messages will consist of the following segments.

Example:

ORU OBSERVATIONAL RESULT UNSOLICITED

MSH Message Header

NTE Notes and Comments

PID Patient Identification

PV1 Patient Visit

NTE Notes and Comments

DG1 Diagnosis

OBR Observation Report

OBX Results

Example: Message

MSH\|~\|\\\|EPI-LAB\|170\|EPI-LAB\|170\|19961018113521\|\|ORU~R01\|107\|P\|2.2\|\|\|\|\|USA

NTE\|\|REPORTING DATE FROM 19850101 TO 19961018

PID\|1\|<span id="p421_38" class="anchor"></span>000-16-7946~0~M10\|5~5~M10\|\|LABPATIENT, EIGHT\|\|000000008\|M\|\|7\|\|\|\|\|\|\|\|\|000167946

PV1\|1\|O\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|19950315151907

NTE\|1\|1^Vanc-Res Enterococcus

DG1\|1\| \|451.19~DEEP PHLEBITIS-LEG NEC~I9

DG1\|2\| \|511.9~PLEURAL EFFUSION NOS!I9

DG1\|3\| \|670.02~MAJOR PUERP INF-DEL P/P~I9

DG1\|4\| \|331.0~ALZHEIMER'S DISEASE~I9

DG1\|5\| \|500.~COAL WORKERS' PNEUMOCON~I9

OBR\|1\|\|\|^CHEMISTRY TEST^VANLT\|\|\|19950315151907\|\|\|\|\|\|\|\|SER^^SERUM

OBX\|1\|ST\|84330.0000^Glucose Quant^VANLT^175^GLUCOSE1^VA60\|\|25\|mg/dL\|70-125\|L\*

NTE\|2\|2^Hepatitis C antibody

OBR\|2\|\|\|^CHEMISTRY TEST^VANLT\|\|\|19950315151907\|\|\|\|\|\|\|\|SER^^SERUM

OBX\|1\|ST\|84330.0000^Glucose Quant^VANLT^175^GLUCOSE1^VA60\|\|25\|mg/dL\|70-125\|L\*

PID\|2\|000-45-6666~8~M10\|7~7~M10\|\|LABPATIENT, NINE\|\|000000009\|F\|\|7\|\|\|\|\|\|\|\|\|000456666

PV1\|1\|O\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|19950315152721

NTE\|1\|1^Vanc-Res Enterococcus

OBR\|1\|\|\|87999.0000^MICRO CULTURE^VANLT\|\|\|198612100835\|\|\|\|\|\|\|\|^^BLOOD

OBX\|1\|CE\|87993.0000^BACTERIOLOGY CULTURE^VANLT\|1\|^ESCHERICHIA COLI

OBR\|2\|\|^ANTIBIOTIC MIC^VANLT\|\|\|\|198612100835\|\|\|\|\|\|\|\|^^BLOOD\|\|\|\|\|\|\|\|\|\|\|87993.0000^1

OBX\|1\|ST\|81812.0000^Neomycin^VANLT^18^NEOMYCN^VA62.06\|\|\|\|\|R

OBX\|2\|ST\|^^^35^BACTRCN^VA62.06\|\|\|\|\|R

OBX\|3\|ST\|81852.0000^Penicillin^VANLT^23^PENICLN^VA62.06\|\|\|\|\|R

OBX\|4\|ST\|81676.0000^Clindamycin^VANLT^3^CLINDAM^VA62.06\|\|\|\|\|S

OBX\|5\|ST\|81307.0000^Gentamicin^VANLT^33^GENTMCN^VA62.06\|\|\|\|\|R

OBX\|6\|ST\|81656.0000^Chloramphenicol^VANLT^10^CHLORAM^VA62.06\|\|\|\|\|R

OBX\|7\|ST\|81946.0000^Tetracycline NOS^VANLT^27^TETRCLN^VA62.06\|\|\|\|\|R

OBX\|8\|ST\|81532.0000^Ampicillin^VANLT^2^AMPICLN^VA62.06\|\|\|\|\|R

OBX\|9\|ST\|81475.0000^Tobramycin^VANLT^28^TOBRMCN^VA62.06\|\|\|\|\|R

OBX\|10\|ST\|^^^29^TRMSULF^VA62.06\|\|\|\|\|R

OBX\|11\|ST\|81098.0000^Amikacin^VANLT^1^AMIKACN^VA62.06\|\|\|\|\|R

OBX\|12\|ST\|81604.0000^Cefamandole^VANLT^5^CEFMAND^VA62.06\|\|\|\|\|R

OBX\|13\|ST\|81886.0000^Piperacillin^VANLT^24^PIPERACILLIN^VA62.06\|\|\|\|\|R

OBX\|14\|ST\|81616.0000^Cefoperazone^VANLT^6^CEFOPERAZONE^VA62.06\|\|\|\|\|R

OBX\|15\|ST\|81794.0000^Mezlocillin^VANLT^16^MEZLOCILLIN^VA62.06\|\|\|\|\|R

Table VA011 - Period of Service

|           |                           |
|-----------|---------------------------|
| Value | Description           |
| 0         | KOREAN                    |
| 1         | WORLD WAR I               |
| 2         | WORLD WAR II              |
| 3         | SPANISH AMERICAN          |
| 4         | PRE-KOREAN                |
| 5         | POST-KOREAN               |
| 6         | OPERATION DESERT SHIELD   |
| 7         | VIETNAM ERA               |
| 8         | POST-VIETNAM              |
| 9         | OTHER OR NONE             |
| A         | ARMY--ACTIVE DUTY         |
| B         | NAVY, MARINE--ACTIVE DUTY |
| C         | AIR FORCE--ACTIVE DUTY    |
| D         | COAST GUARD--ACTIVE DUTY  |
| E         | RETIRED, UNIFORMED FORCES |
| F         | MEDICAL REMEDIAL ENLIST   |
| G         | MERCHANT SEAMEN--USPHS    |
| H         | OTHER USPHS BENEFICIARIES |
| I         | OBSERVATION/EXAMINATION   |
| J         | OFFICE OF WORKERS COMP.   |
| K         | JOB CORPS/PEACE CORPS     |
| L         | RAILROAD RETIREMENT       |
| M         | BENEFICIARIES-FOREIGN GOV |
| N         | HUMANITARIAN (NON-VET)    |
| O         | CHAMPUS RESTORE           |
| P         | OTHER REIMBURS. (NON-VET) |
| Q         | OTHER FEDERAL - DEPENDENT |
| R         | DONORS (NON-VET)          |
| S         | SPECIAL STUDIES (NON-VET) |
| T         | OTHER NON-VETERANS        |
| U         | CHAMPVA--SPOUSE, CHILD    |
| V         | CHAMPUS                   |
| W         | CZECHOSLOVAKIA/POLAND SVC |
| X         | PERSIAN GULF WAR          |
| Y         | CAV/NPS                   |
| Z         | MERCHANT MARINE           |

Table 0070 - Specimen Source Codes

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Abbreviations</strong></td>
<td><strong>Descriptions</strong></td>
<td><strong>Abbreviations</strong></td>
<td><strong>Descriptions</strong></td>
<td><strong>Abbreviations</strong></td>
<td><strong>Descriptions</strong></td>
</tr>
<tr class="even">
<td>ABS</td>
<td>Abscess</td>
<td>FLU</td>
<td>Body fluid, unsp</td>
<td>SER</td>
<td>Serum</td>
</tr>
<tr class="odd">
<td>AMN</td>
<td>Amniotic fluid</td>
<td>GAS</td>
<td>Gas</td>
<td>SKN</td>
<td>Skin</td>
</tr>
<tr class="even">
<td>ASP</td>
<td>Aspirate</td>
<td>GAST</td>
<td>Gastric fluid/contents</td>
<td>SKM</td>
<td>Skeletal muscle</td>
</tr>
<tr class="odd">
<td>BPH</td>
<td>Basophils</td>
<td>GEN</td>
<td>Genital</td>
<td>SPRM</td>
<td>Spermatozoa</td>
</tr>
<tr class="even">
<td>BIFL</td>
<td>Bile fluid</td>
<td>GENC</td>
<td>Genital cervix</td>
<td>SPT</td>
<td>Sputum</td>
</tr>
<tr class="odd">
<td>BBL</td>
<td>Blood bag</td>
<td>GENV</td>
<td>Genital vaginal</td>
<td>SPTT</td>
<td><p>Sputum tracheal</p>
<p>aspirate</p></td>
</tr>
<tr class="even">
<td>BLDC</td>
<td>Blood capillary</td>
<td>HAR</td>
<td>Hair</td>
<td>STON</td>
<td>Stone (use CALC)</td>
</tr>
<tr class="odd">
<td>BPU</td>
<td>Blood product unit</td>
<td>IHG</td>
<td>Inhaled Gas</td>
<td>STL</td>
<td>Stool = Fecal</td>
</tr>
<tr class="even">
<td>BLDV</td>
<td>Blood venous</td>
<td>IT</td>
<td>Intubation tube</td>
<td>SWT</td>
<td>Sweat</td>
</tr>
<tr class="odd">
<td>BON</td>
<td>Bone</td>
<td>ISLT</td>
<td>Isolate</td>
<td>SNV</td>
<td><p>Synovial fluid</p>
<p>(Joint fluid)</p></td>
</tr>
<tr class="even">
<td>BRTH</td>
<td><p>Breath</p>
<p>(use EXHLD)</p></td>
<td>LAM</td>
<td>Lamella</td>
<td>TEAR</td>
<td>Tears</td>
</tr>
<tr class="odd">
<td>BRO</td>
<td>Bronchial</td>
<td>WBC</td>
<td>Leukocytes</td>
<td>THRT</td>
<td>Throat</td>
</tr>
<tr class="even">
<td>BRN</td>
<td>Burn</td>
<td>LN</td>
<td>Line</td>
<td>THRB</td>
<td><p>Thrombocyte</p>
<p>(platelet)</p></td>
</tr>
<tr class="odd">
<td>CALC</td>
<td>Calculus (=Stone)</td>
<td>LNA</td>
<td>Line arterial</td>
<td>TISS</td>
<td>Tissue</td>
</tr>
<tr class="even">
<td>CDM</td>
<td>Cardiac muscle</td>
<td>LNV</td>
<td>Line venous</td>
<td>TISG</td>
<td>Tissue gall bladder</td>
</tr>
<tr class="odd">
<td>CNL</td>
<td>Cannula</td>
<td>LIQ</td>
<td>Liquid NOS</td>
<td>TLGI</td>
<td><p>Tissue large</p>
<p>intestine</p></td>
</tr>
<tr class="even">
<td>CTP</td>
<td>Catheter tip</td>
<td>LYM</td>
<td>Lymphocytes</td>
<td>TLNG</td>
<td>Tissue lung</td>
</tr>
<tr class="odd">
<td>CSF</td>
<td>Cerebral spinal fluid</td>
<td>MAC</td>
<td>Macrophages</td>
<td>TISPL</td>
<td>Tissue placenta</td>
</tr>
<tr class="even">
<td>CVM</td>
<td>Cervical mucus</td>
<td>MAR</td>
<td>Marrow</td>
<td>TSMI</td>
<td><p>Tissue small</p>
<p>intestine</p></td>
</tr>
<tr class="odd">
<td>CVX</td>
<td>Cervix</td>
<td>MEC</td>
<td>Meconium</td>
<td>TISU</td>
<td>Tissue ulcer</td>
</tr>
<tr class="even">
<td>COL</td>
<td>Colostrum</td>
<td>MBLD</td>
<td>Menstrual blood</td>
<td>TUB</td>
<td>Tube NOS</td>
</tr>
<tr class="odd">
<td>CBLD</td>
<td>Cord blood</td>
<td>MLK</td>
<td>Milk</td>
<td>ULC</td>
<td>Ulcer</td>
</tr>
<tr class="even">
<td>CNJT</td>
<td>Conjunctiva</td>
<td>MILK</td>
<td>Breast milk</td>
<td>UMB</td>
<td>Umbilical blood</td>
</tr>
<tr class="odd">
<td>CUR</td>
<td>Curettage</td>
<td>NAIL</td>
<td>Nail</td>
<td>UMED</td>
<td>Unknown medicine</td>
</tr>
<tr class="even">
<td>CYST</td>
<td>Cyst</td>
<td>NOS</td>
<td>Nose (nasal passage)</td>
<td>URTH</td>
<td>Urethra</td>
</tr>
<tr class="odd">
<td>DIAF</td>
<td>Dialysis fluid</td>
<td>ORH</td>
<td>Other</td>
<td>UR</td>
<td>Urine</td>
</tr>
<tr class="even">
<td>DOSE</td>
<td><p>Dose med or</p>
<p>substance</p></td>
<td>PAFL</td>
<td>Pancreatic fluid</td>
<td>URC</td>
<td>Urine clean catch</td>
</tr>
<tr class="odd">
<td>DRN</td>
<td>Drain</td>
<td>PAT</td>
<td>Patient</td>
<td>URT</td>
<td>Urine catheter</td>
</tr>
<tr class="even">
<td>DUFL</td>
<td>Duodenal fluid</td>
<td>PRT</td>
<td>Peritoneal fluid ascites</td>
<td>URNS</td>
<td>Urine sediment</td>
</tr>
<tr class="odd">
<td>EAR</td>
<td>Ear</td>
<td>PLC</td>
<td>Placenta</td>
<td>USUB</td>
<td><p>Unknown</p>
<p>substance</p></td>
</tr>
<tr class="even">
<td>EARW</td>
<td>Ear wax (cerumen)</td>
<td>PLAS</td>
<td>Plasma</td>
<td>VOM</td>
<td>Vomitus</td>
</tr>
<tr class="odd">
<td>ELT</td>
<td>Electrode</td>
<td>PLB</td>
<td>Plasma bag</td>
<td>BLD</td>
<td>Whole blood</td>
</tr>
<tr class="even">
<td>ENDC</td>
<td>Endocardium</td>
<td>PLR</td>
<td><p>Pleural fluid</p>
<p>(thoracentesis fld)</p></td>
<td>BDY</td>
<td>Whole body</td>
</tr>
<tr class="odd">
<td>ENDM</td>
<td>Endometrium</td>
<td>PMN</td>
<td><p>Polymorphonuclear</p>
<p>neutrophils</p></td>
<td>WAT</td>
<td>Water</td>
</tr>
<tr class="even">
<td>EOS</td>
<td>Eosinophils</td>
<td>PPP</td>
<td>Platelet poor plasma</td>
<td>WICK</td>
<td>Wick</td>
</tr>
<tr class="odd">
<td>RBC</td>
<td>Erythrocytes</td>
<td>PRP</td>
<td>Platelet rich plasma</td>
<td>WND</td>
<td>Wound</td>
</tr>
<tr class="even">
<td>EYE</td>
<td>Eye</td>
<td>PUS</td>
<td>Pus</td>
<td>WNDA</td>
<td>Wound abscess</td>
</tr>
<tr class="odd">
<td>EXHLD</td>
<td>Exhaled gas (breath)</td>
<td>RT</td>
<td>Route of medicine</td>
<td>WNDE</td>
<td>Wound exudate</td>
</tr>
<tr class="even">
<td>FIB</td>
<td>Fibroblasts</td>
<td>SAL</td>
<td>Saliva</td>
<td>WNDD</td>
<td>Wound drainage</td>
</tr>
<tr class="odd">
<td>FLT</td>
<td>Filter</td>
<td>SEM</td>
<td>Seminal fluid</td>
<td>XXX</td>
<td><p>To be specified in</p>
<p>another part of the</p>
<p>message</p></td>
</tr>
<tr class="even">
<td>FIST</td>
<td>Fistula</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table VA07 - Race

|           |                                  |
|-----------|----------------------------------|
| Value | Description                  |
| 1         | HISPANIC, WHITE                  |
| 2         | HISPANIC, BLACK                  |
| 3         | AMERICAN INDIAN OR ALASKA NATIVE |
| 4         | BLACK, NOT OF HISPANIC ORIGIN    |
| 5         | ASIAN OR PACIFIC ISLANDER        |
| 6         | WHITE NOT OF HISPANIC ORIGIN     |
| 7         | UNKNOWN                          |

Table 0001 - Sex

|           |                 |
|-----------|-----------------|
| Value | Description |
| F     | FEMALE      |
| M     | MALE        |
| O     | OTHER       |
| U     | UNKNOWN     |

Table 0078 - Abnormal flags

|                                         |                          |
|-----------------------------------------|--------------------------|
| Value                               | Description          |
| L                                       | Below low normal         |
| H                                       | Above high normal        |
| LL                                      | Below lower panic limits |
| HH                                      | Above upper panic limits |
| For microbiology sensitivities only |                          |
| S                                       | Sensitive                |
| R                                       | Resistant                |
| I                                       | Intermediate             |
| MS                                      | Moderately sensitive     |
| VS                                      | Very sensitive           |

LABORATORY EPI PATCH LR\*5.2\*132 USER GUIDE

# Laboratory EPI Patch LR\*5.2\*132 User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory EPI Patch LR\*5.2\*132 User Guide section provides all the necessary information, instructions, illustrations, and examples required for the EPI coordinators, Laboratory personnel, and other users to implement and maintain the EPI software package. This information should be adhered to as recommended to assure a successful implementation of the EPI software.

> **NOTE:** It is <u>highly</u> <u>recommended</u> that the Laboratory Information Manager (LIM), TQI/QA/QI, and a representative from the Microbiology section (director, supervisor, or technologist) <u>jointly</u> participate in reviewing the 14 Emerging Pathogen descriptions and entering of data for the EPI software package. The individual(s) will be responsible for initially setting the EPI parameters, doing periodic reviews of ICD codes and parameters to assure they are current.

## Emerging Pathogens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Listed below are the 14 Emerging Pathogens that the EPI software package has been defined to track:

*CandidaLegionellaClostridiumdifficile* Leishmanaisis

Creutzfeldt-Jakob Disease Malaria

*Cryptosporidium* Pen- Res Pneumococcus

Dengue *Streptococcus-*Group A

*E. coli* O157:H7 Tuberculosis

Hepatitis C Antibody Pos Vanc-Res *Enterococcus*NOTE: Descriptions for each of the 14 Emerging Pathogens are located in the “Emerging Pathogens Descriptions and Screen Displays” section of this User Guide.

## Emerging Pathogen Primary Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory EPI software has one stand-alone menu. There are no locks or security keys created for this menu. The Emerging Pathogen Primary Menu consists of the following three options:

Antimicrobial Link Update: This option will allows the user to link the ANTIMICROBIAL SUSCEPIBILTY' file (#62.06) with WKLD CODE file (#64).

> **NOTE:** Please see the Appendix section of this guide on “How to Link Antimicrobial Entries to Workload Codes Entries” using this option.

Emerging Pathogen Manual Run: This option allows the user to select any month to run the Search/Extract process manually. The first and last day of the month will be determined automatically.

Emerging Pathogens Parameter update: This option is used to define the search criteria along with additional information associated with the Emerging Pathogen Initiative.

> **NOTE:** The Emerging Pathogen Primary Menu options are using VA FileMan screens displays, referred to as ScreenMan. For detailed instructions on how to use the screens displays please review the VA FileMan V. 21.0 User Manual, Section 6 ScreenMan.

Emerging Pathogens Parameter update option screen and help prompts definitions:

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Emerging Pathogen update option Parameters Screens Prompts</strong></td>
<td><p><strong>Emerging Pathogen Parameter update option</strong></p>
<p><strong>Screens Help Prompts</strong></p></td>
</tr>
<tr class="even">
<td>Serology Lab Test (s)</td>
<td>Consider this synonymous with, chemistry, serology, hematology “blood/serum” tests. Results anticipated to be found here will have had a test done, under chemistry/hematology accession areas, even if physically performed in microbiology other areas. Select from the LABORATORY TEST file (#60)</td>
</tr>
<tr class="odd">
<td>Indicator</td>
<td><p>Select the code that will determine how to match lab results.</p>
<p>‘1’ FOR Use Reference Ranges</p>
<p>‘2’ FOR Contains</p>
<p>‘3’ FOR Greater Than</p>
<p>‘4’ FOR Less Than</p>
<p>‘5’ FOR Equal To</p></td>
</tr>
<tr class="even">
<td>Value</td>
<td>Positive, etc. Answer must be 1-15 characters in length. This is a Free Text field.</td>
</tr>
<tr class="odd">
<td><span id="p421_47" class="anchor"></span>ICD-9</td>
<td>ICD-9 standardized code used nationwide in federal and non-federal/private health care facilities. Select from the ICDM-9 DIAGNOSIS file (#80).</td>
</tr>
<tr class="even">
<td>ICD Description</td>
<td>Title of ICD diagnosis</td>
</tr>
<tr class="odd">
<td>ICD-10</td>
<td>ICD-10 standardized code used nationwide in federal and non-federal/private health care facilities. Select from the ICD DIAGNOSIS file (#80).</td>
</tr>
<tr class="even">
<td>Selected Etiology</td>
<td>Consider synonymous with organism, final microbial diagnosis/isolate. Select from the ETIOLOGY FIELD file (61.2).</td>
</tr>
<tr class="odd">
<td>Antimicrobial Susceptibility</td>
<td>Enter the Antimicrobial that will be used in screening out sensitive Etiologies (e.g., “Vancomycin” for Vancomycin Resistant Enterococcus). Select from the ANTIMICROBIAL SUSCEPTIBILITY file (#62.6).</td>
</tr>
<tr class="even">
<td>NLT Code:</td>
<td>Displays the associated NLT code if linked. If no NLT Code is displayed use the Antimicrobial Link Update option.</td>
</tr>
<tr class="odd">
<td>NLT Description</td>
<td>Displays the Description of the linked NLT code.</td>
</tr>
<tr class="even">
<td>Topography Selection</td>
<td></td>
</tr>
<tr class="odd">
<td>Include</td>
<td>Selection of a Topography screens all others out except the ones selected. For "ALL" leave blank. Not to be used in conjunction with the exclude Topography selection. Select from the TOPOGRAPHY file (#61).</td>
</tr>
<tr class="even">
<td>Exclude</td>
<td>Select the Topography to screen out. Not to be used in conjunction with the Include Topography selection. Select from the TOPOGRAPHY file (#61).</td>
</tr>
<tr class="odd">
<td>Follow PTF:</td>
<td><p>Indicates if the PTF record will be followed until a discharge has been entered.</p>
<p>Choose: ‘1’ FOR YES</p>
<blockquote>
<p>‘0’ FOR NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Run Date:</td>
<td>Date that the last Auto Search/Extract processed.</td>
</tr>
<tr class="odd">
<td>Run Cycle:</td>
<td>This field is currently not used. For future use.</td>
</tr>
<tr class="even">
<td>First Encounter:</td>
<td><p>Limits the output to the first encounter for the patient. Otherwise list all encounters.</p>
<p>Choose: ‘1’ FOR YES</p>
<p>‘0’ FOR NO</p></td>
</tr>
<tr class="odd">
<td>Protocol:</td>
<td>Defines the protocol used to define the output messages. Select from the EMERGING PATH PROTOCOL file (#69.4).</td>
</tr>
<tr class="even">
<td>General Description:</td>
<td>To review or edit the General Description use the <strong>&lt;Enter&gt;</strong> key instead of the<strong>&lt;Tab&gt;</strong> key.</td>
</tr>
</tbody>
</table>

## Emerging Pathogens Descriptions and Screen Displays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section includes the 14 Emerging Pathogens descriptions and screen displays. The screen displays contains examples of the pre-populated fields. The ETIOLOGY FIELD file (#61.2) site specific data is used to <u>partially</u> pre-populate the fields in the EMERGING PATHOGENS file (#69.5). However, further entries will be required for site specific data. Additional entries may be added or deleted to meet your site specific needs. These examples will assist in the initial Emerging Pathogens parameter updates.

### Candida (Reference \#8)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fungal infections are rising in significance especially in severely ill patients. The same is true for bloodstream infections acquired in the hospital, especially those associated with intravenous lines. Fungal bloodstream infections are increasing in prevalence.

As a marker of bloodstream infections we have chosen the fungus *Candida* (and *Torulopsis*) as an initial indicator organism. This may not be a prevalent or significant entity at your site, but its presence is more likely to be indicative of serious or true infection than other organisms which may commonly be isolated from the blood in association with IV lines. Additionally this yeast is more likely to be associated with nosocomial acquisition than other organisms such as *Staphylococcus aureus* and coagulase negative *Staphylococcus*, which can cause a number of community acquired syndromes not at all related to IV lines.

We wish to capture all episodes of *Candida* (*Torulopsis,* yeast) isolation from blood or a blood source (central line, IV catheter tip, etc.). For *Candida* a partial pre-populated list of (etiologies/organisms) to choose from has been included. These should be entered, in addition to any site specific (etiologies organisms) which also fit the description.

> **NOTE:** The Emerging Pathogen Primary Menu options are using VA FileMan screens displays, referred to as ScreenMan. For detailed instructions on how to use the screens displays please review the VA FileMan V. 21.0 User Manual, Section 6 ScreenMan.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="EP_Prim_Menu" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ?\<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS-GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME:CAN\<Enter\>DIDA

> **NOTE:** Please be consistent with site specific data spelling or alternate spelling to assure accurate EPI data capture.

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: Candida ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

\<Enter\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: CANDIDA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

Examples:CANDIDA

CANDIDA GUILLIERMONDII

CANDIDA KRUSEI

CANDIDA PARAPSILOSIS

CANDIDA PSEUDOTROPICALIS

CANDIDA SKIN TEST ANTIGEN

CANDIDA STELLATOIDEA

CANDIDA TROPICALIS

CANDIDA, NOS

\<Enter\>Note: During the post Init, the ETIOLOGY FIELD file (#61.2) was searched to pre-populate the Etiology field (#3) in the EMERGING PATHOGENS file (#69.5). Listed above are examples of etiology entries which may have been populated from your site’s file. Additional etiologies may be added or deleted at the <u>Selected Etiology</u> prompt to meet your site specific needs.

> **NOTE:** If spelling differences occur within your ETIOLOGY FIELD file (#61.2), be consistent with your local file and spell the results here, as it is spelled in your file (even if it is spelled differently in the example). We are concerned more importantly with data <u>recovery</u>.

Antimicrobial Susceptibility NLT Code NLT Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: Candida ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

Blood\<Enter\>\<Enter\>Bloodstream\<Enter\>Catheter Tip\<Enter\>Note: These are only suggestions. Please add accordingly to your site definition.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: Candida ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter:\<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<Enter\>

### Clostridium difficile (Reference \#4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Disease associated with the presence of *Clostridium difficile* enterotoxin A can cause significant morbidity, as well as mortality. It is of importance as its predominant acquisition seems to occur nosocomially. Presence of Clostridial toxin (either enterotoxin A or cytotoxin L) by assay (whether it be EIA, latex agglutination, cytotoxicity of cell culture <u>+</u> neutralization, or culture of organism with subsequent colony testing) is the best indicator that an inflammatory diarrheal disease is due to presence of *Clostridium difficile*. Laboratory services are quite varied as to how they identify the presence of *Clostridium difficile*. Some labs are set up to identify *C. difficile* as the final microbiological (bacterial) etiology of a culture, even if a culture method was not used. Other labs use a final etiology of “see comment” and then enter the results in a free text format. Still others enter the text under a hematology or chemistry format where a reference range and “positive” and “negative” result values can be entered. Wherever the facility lab places the results which are used to demonstrate the presence of toxin-producing *C. difficile*, we need to be able to track them (that means it must occur as a retrievable “positive” or “negative” result, or as a “bacterial etiology”). Any results contained in a “Comments” or “Free-text” sections are not acceptable.

There are a number of different ways that sites have chosen to enter *Clostridium difficile* toxin assay results into the V*ist*A system. As long as the toxin assay results are in a retrievable format (straight from the V*ist*A system without additional manual input needed), how it is entered is not of significance to the EPI package.

> **NOTE:** However, there are two preferred methods that makes it easy to capture the EPI data. Please reference the Appendix section of this guide for the two methods.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ?\<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: CLO\<Enter\>STRIDIUM DIFFICILE

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

Clostridium\<Enter\> difficile toxin Contains\<Enter\>Pos\<Enter\>Note: This is only a suggestion. Please add accordingly to your site definition.

<span id="ICDCodingSystemUpdate2" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

Clostridium difficile toxin positive\<Enter\>Note: This is only a suggestion. Please add accordingly to your site definition.

Antimicrobial Susceptibility NLT Code NLT Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\> \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter:\<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help

### Creutzfeldt-Jakob Disease (CJD) (Reference \#13)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Creutzfeldt-Jakob Disease* (CJD*)* disease is a rare illness associated with prions. The VA has chosen to follow this entity because of historic problems with certain blood products in use in both the private and public health care sectors. The EPI data will be one of a number of ways used to identify changes in trends of incidence of this illness. This task is remarkably complex because of the long incubation period of CJD. There are no specific tests for diagnosis other than central nervous system histology combined with clinical presentation. As such, we will follow this entity through <span id="p421_55" class="anchor"></span>ICD coding.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ?\<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: CRE\<Enter\>UTZFELDT-JAKOB DISEASE

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

\<Enter\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

046.1 ICD-9 JAKOB-CREUTZFELDT DIS

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

\<Enter\>

Antimicrobial Susceptibility NLT Code NLT Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\> \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter: \<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help Insert

### Cryptosporidium (Reference \#9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The parasite *Cryptosporidium parvum* is a cause of water-borne diarrheal disease. It has gained recent prominence after evaluation of the outbreak in the greater Milwaukee area in 1993 which is estimated to have affected \<400,000 persons. In addition to affecting HIV-infected persons and young children, information exists which demonstrates that the chronically-ill, elderly are also a higher risk group than the general population. We will utilize both microbiology laboratory data (parasitology for most laboratories), as well as <span id="p421_58" class="anchor"></span>ICD coding to track this disease as both are narrowly defined parameters.

> **NOTE:** Microsporidiosis is a similar disease, but we do not currently wish to follow this disease process and Microsporidian etiologies should not be entered.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ? \<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: CRY\<Enter\>PTOSPORIDIUM

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: CRYPTOSPORIDIUM ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

\<Enter\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

007.8 ICD-9 PROTOZOAL INTEST DIS N

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: CRYPTOSPORIDIUM ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

Cryptosporidium\<Enter\>Note: If Cryptosporidium is reported under parasitology, add Cryptosporidium species at the Etiology prompt.

Antimicrobial Susceptibility NLT Code NLT Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: CRYPTOSPORIDIUM ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\> \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: CRYPTOSPORIDIUM ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter: \<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

Edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help

### Dengue (Reference \#12)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The mosquito-borne disease of Dengue Hemorrhagic Fever is a rare but re-emerging infection, especially in the Caribbean. The VA has seen cases of Dengue Hemorrhagic Fever over the last several years. Most of these cases have been in Dengue endemic areas served by the VA. However, as our society becomes more mobile, and the area of Dengue endemnity expands, more cases are likely to occur. Because microbiologic culture is not routinely done and serology can be difficult to track, we will initially use <span id="p421_61" class="anchor"></span>ICD coded diagnoses to track this entity.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ?\<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: DEN\<Enter\>GUE

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: DENGUE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

\<Enter\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

061\. ICD-9 DENGUE

065.4 ICD-9 MOSQUITO-BORNE HEM FEVER

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: DENGUE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

\<Enter\>

Antimicrobial Susceptibility NLT Code NLT Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: DENGUE ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\> \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

COMMAND: Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: DENGUE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES \<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY \<Enter\> First Encounter: \<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help

### E. coli O157:H7 (Reference \#10)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Escherichia coli* serotype O157 (*E. coli* O157) has gained prominence as a food-borne illness with potentially life threatening complications coming from the associated Hemolytic Uremic Syndrome. Not all sites routinely culture for the presence of *E. coli* O157 in stool specimens submitted for culture. Also, *E. coli* O157 is not a microbiologic (bacterial) etiology pre-existing in the most recent - national microbiology lab package. In order to nationally track cultures positive for this organism, each site will need to make an etiology specific for *E-coli* O157 (e.g. *Escherichia coli* O157, *E. coli* O157, *E. coli* serotype O157, etc.). Some sites have already done this and will not need to generate a new entry.

> **NOTE:** Entering *Escherichia coli* or *E. coli* from the bacterial etiology and then entering “serotype O157” or “O157”, under the “Comments section” or in “Free Text” is not acceptable as it will not allow the data to be retrieved nationally).

All subsequent positive cultures for this organism must then be entered under the new etiology.

Other serotypes of *E. coli* will also cause disease, but we will not currently track these as O157 causes, by far, the majority of cases of interest for the national database.

For the EPI package, this will be dependent on your site. If your site already has an etiology which will select positive cultures for *E. coli* O157, then enter that etiology. However, if your site had to enter a new etiology to accommodate this EPI package, be sure to enter this new etiology here.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_E_Coli" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ?\<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: E.\<Enter\> COLI 0157:H7

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: E. COLI 0157:H7 ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

\<Enter\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: E. COLI 0157:H7 ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

Example: Escherichia coli O157\<Enter\>Note: Entering *Escherichia coli* or *E. coli* from the bacterial etiology and then entering “serotype O157” or “O157”, under the Comments section or in

free text is not acceptable as it will not allow the data to be retrieved nationally).

Antimicrobial Susceptibility NLT Code NLT Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: E. COLI 0157:H7 ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\> \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: E. COLI 0157:H7 ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter: \<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help

### Hepatitis C Antibody Positive (Reference \#2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hepatitis C is much more prevalent than originally thought at least in certain key patient sub-populations. As new and more sensitive assays come into use, we seem to find more evidence of this pathogen. We are looking for evidence of exposure to Hepatitis C in patients as demonstrated by Hepatitis C antibody positivity. The need for confirmatory testing or demonstration of active disease is not currently necessary in gathering data for this program. Different facilities may use different assays for this test. What we are looking for are evidence of presence of antibody to Hepatitis C, whether it be recorded as “weakly positive”, “strongly positive”, “positive”, or “present”. If other phrases are used to describe a test result, one should be able to differentiate the results upon entry into the program. As an example, the words, “present” and “not present” would not allow retrieval of only positive cases as both phrases contain the word, “present”.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="p421_68" class="anchor"></span>VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ? \<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: HEP\<Enter\>ATITIS C ANTIBODY POS

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: HEPATITIS C ANTIBODY POS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

HEPATITIS C ANTIBODY\<Enter\> Contains\<Enter\>Pos\<Enter\>Note: Enter the appropriate test for your site, and how the results are reported.

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: HEPATITIS C ANTIBODY POS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

\<Enter\>

Antimicrobial Susceptibility NLT Code NLT Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: HEPATITIS C ANTIBODY POS ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\> \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: HEPATITIS C ANTIBODY POS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter: \<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help

### Legionella (Reference \#7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since the American Legion Convention in Philadelphia in the 1970’s, Legionnaires’ Disease has been an illness of keen interest to the DVA. Because diagnosis is complex, we have chosen to review for presence of *Legionella* in culture and in <span id="p421_71" class="anchor"></span>ICD DIAGNOSIS file (#80). We will not look at *Legionella* direct fluorescent antibody positivity because of the potential high false positivity of this test. Likewise, serology is not easy to interpret or easily extracted from V*IST*A for our purposes and will not be included as a marker in this first iteration of the EPI program. Because it is not yet approved, the newer test of *Legionella* urinary antigen will not be used either. The Selected Etiology screen display has been partially pre-populated.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ? \<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: LEG\<Enter\>IONELLA

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: LEGIONELLA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

\<Enter\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

482.80 ICD-9 LEGIONNARIE’S DISEASE

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: LEGIONELLA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

Examples:LEGIONELLA BOZEMANII

LEGIONELLA DUMOFFII

LEGIONELLA GORMANII

LEGIONELLA JORDANIS

LEGIONELLA LONGBEACHAE

LEGIONELLA MICDADEI

LEGIONELLA OAKRIDGENSIS

LEGIONELLA PNEUMOPHILIA

LEGIONELLA SP

LEGIONELLA WADSWORTHII

\<Enter\>Note: During the post Init, the ETIOLOGY FIELD file (#61.2) was searched to pre-populate the Etiology field (#3) in the EMERGING PATHOGENS file (#69.5). Listed above are examples of etiology entries which may have been populated from your site’s file. Additional etiologies may be added or deleted at the <u>Selected Etiology</u> prompt to meet your site specific needs.

> **NOTE:** If spelling differences occur within your ETIOLOGY FIELD file (#61.2) be consistent with your local file and spell the results here, as it is spelled in your file (even if it is spelled differently in the example). We are concerned more importantly with data <u>recovery</u>.

Antimicrobial Susceptibility NLT Code NLT Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: LEGIONELLA ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\>\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: LEGIONELLA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter: \<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help

### Leishmaniasis (Reference \#14)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Leishmaniasis is a significant tropical disease which can cause serious complications. It is of interest to the Department of Veterans Affairs as Leishmania has caused illness among military personnel for many years. In addition, the Persian Gulf War occurred in an area of the world where the parasite is endemic. Because no simple, straight-forward serology exists and no standard culture techniques exist, we have chosen to follow this entity through <span id="p421_74" class="anchor"></span>ICD diagnosis codes.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ? \<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: LEI\<Enter\>SHMANIASIS

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: LEISHMANIASIS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

\<Enter\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

085.0 ICD-9 VISCERAL LEISHMANIASIS

085.1 ICD-9 CUTAN LEISHMANIAS URBAN

085.2 ICD-9 CUTAN LEISHMANIAS ASIAN

085.3 ICD-9 CUTAN LEISHMANIAS ETHIOP 085.4 ICD-9 CUTAN LEISHMANIAS AMER

085.5 ICD-9 MUCOCUTAN LEISHMANIASIS

085.9 ICD-9 LEISHMANIASIS NOS

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: LEISHMANIASIS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

\<Enter\>

Antimicrobial Susceptibility NLT Code NLT Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: LEISHMANIASIS ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\> \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

COMMAND: Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: LEISHMANIASIS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter: \<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help

### Malaria (Reference \#11)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The plasmodial parasite is responsible for the blood-borne disease of malaria. Malaria can cause acute as well as chronic, relapsing disease. Occasionally, U.S. troops are deployed in malaria endemic areas. This placement could potentially put troops at risk for acquiring this disease. For the Emerging Pathogens Initiative program, we are interested in tracking patients with malaria, either acute or chronic, relapsing, and in either inpatient or outpatient status. No standardized serologic test allows for easy identification. Since not all sites consistently code and record malarial parasites seen histologically or on blood smears (not all of these interpretations are done through the Pathology and Laboratory Service), we have currently decided to track malaria based on <span id="p421_77" class="anchor"></span>ICD coding.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ? \<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: MAL\<Enter\>ARIA

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: MALARIA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

\<Enter\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

084.0 ICD-9 FALCIPARUM MALARIA

084.1 ICD-9 VIVAX MALARIA

084.2 ICD-9 QUARTAN MALARIA

084.3 ICD-9 OVALE MALARIA

084.4 ICD-9 MALARIA NEC

084.5 ICD-9 MIXED MALARIA

084.6 ICD-9 MALARIA NOS

7.  ICD-9 INDUCED MALARIA

084.8 ICD-9 BLACKWATER FEVER

084.9 ICD-9 MALARIA COMPLICATED NEC

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: MALARIA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

\<Enter\>

Antimicrobial Susceptibility NLT Code NLT Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: MALARIA ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\> \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: MALARIA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter: \<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help

### Penicillin- Resistant Pneumococcus (Reference \#3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The emergence of antibiotic resistance in microbial agents is of great interest and concern for health care. Penicillin (PCN) was once the mainstay of therapy for *Streptococcuspneumoniae* infections but resistance to this agent is becoming more prominent. Different therapeutic strategies need to be developed once the prevalence of PCN-resistant *S. pneumoniae* reaches a critical threshold in a community. In order to monitor this, we are looking for the presence of any resistance in the pneumococci (either “moderate/intermediate” or “frank/high” level resistance). As such, any *S. pneumoniae* which is not fully susceptible to PCN on PCN susceptibility testing should be recorded.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="p421_80" class="anchor"></span>VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ? \<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: PEN\<Enter\>-RES PNEUMOCOCCUS

NAME: PEN-RES PNEUMOCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

\<Enter\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: \<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: PEN-RES PNEUMOCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

> **NOTE:** You may enter a new ETIOLOGY, if you wish.

STREPTOCOCCUSPNEUMONIAE 12

Are you adding 'STREPTOCOCCUS PNEUMONIAE' as

a new ETIOLOGY (the 1ST for this EMERGING PATHOGENS)?Y\<Enter\>

Antimicrobial Susceptibility NLT Code NLT Description

Penicillin\<Enter\>

Are you adding ' Penicillin ' as

a new Antimicrobial Susceptibility (the 1ST for this EMERGING PATHOGENS)?Y \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: \<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: PEN-RES PNEUMOCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\> \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: PEN-RES PNEUMOCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter: \<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<Enter\>

### Streptococcus-Group A (Reference \#6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Streptococcus-*Group A can be associated with or cause significant disease such as severe fasciitis and streptococcal toxic shock syndrome. We are especially interested to find out how much severe/deep seated disease the VA is experiencing, but other disease entities are of interest also. To this end, we are looking for all episodes of culture positivity for *Streptococcus-* Group A, regardless of site and regardless of inpatient or outpatient status of the person from whom the specimen is obtained. We are aware that some sites may use rapid screenings for *Streptococcus-*Group A, especially from pharyngeal sources. These rapid screens may be difficult to capture, so we are not asking for them on this first iteration of the EPI program.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="p421_83" class="anchor"></span>VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ? \<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS-GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: STR\<Enter\>EPTOCOCCUS-GROUP A

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: STREPTOCOCCUS-GROUP A ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

\<Enter\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: STREPTOCOCCUS-GROUP A ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

STREPTOCOCCUS-GROUP A\<Enter\>

Antimicrobial Susceptibility NLT Code NLT Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: STREPTOCOCCUS-GROUP A ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\>\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: STREPTOCOCCUS-GROUP A ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter: \<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help

### Tuberculosis (Reference \#5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Mycobacterium tuberculosis* infection is an important public health concern. Recent increases in incidence of disease, and occurrence of multiply-drug resistant strains in outbreak situations along with the increased susceptibility of HIV-infected persons for this disease has generated renewed interest in this entity. Since the national data show that 80-85% of all reported active tuberculosis cases are culture positive (with acid fast bacilli smear-only positive cases increasing the reporting by 2-5% more) we have decided to use culture positivity for *Mycobacterium tuberculosis* to track tuberculosis infections in the current iteration of the EPI software package. Information regarding susceptibility will be tracked as well. For the national EPI program, there will be no need to enter specific antimycobacterial agents to be tracked; it will be done automatically. <span id="p421_86" class="anchor"></span>ICD coding is complex and confusing for many cases of tuberculosis and therefore will not be used.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ? \<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS-GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: TUB\<Enter\>ERCULOSIS

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: TUBERCULOSIS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

\<Enter\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: TUBERCULOSIS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

Mycobacterium tuberculosis\<Enter\>

Antimicrobial Susceptibility NLT Code NLT Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: TUBERCULOSIS ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\> \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: TUBERCULOSIS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter: \<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help

### Vancomycin-Resistant Enterococcus (VRE) (Reference \#1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vancomycin-Resistant Enterococcus (VRE) is a pathogen of increasing importance. Not only can it cause significant disease, but also it can be spread within facilities. It is important to capture all positive cultures for VRE (not just disease). As such, all positive cultures for VRE will be reported.

> **NOTE:** This includes cultures positive for prevalence and surveillance review, including specimens of stool and rectal swabs.

Vancomycin-resistant *Enterococcus faecalis* and *E. faecium* are most common, but we wish to look at all vancomycin resistant enterococci whether speciated or not. Therefore, it is important to be sure to list all the places in the Micro Lab package where *Enterococcus* are found, either as *Enterococcus*, *E. (sp.),* Group D-*Streptococcus*, *E. faecalis*, *E. faecium*, *E. durans*, *E. gallinarum*, *E. casseliflavus*, etc.

> **NOTE:** Only a partial pre-populated Etiology list is shown in the screen display example at the <u>Selected Etiology</u> prompt. Please be sure to review the entire Etiology list. If you have other etiology results at your site, they can be added to this Etiology list. Again, if alternate spellings are present in your site’s ETIOLOGY FIELD file (#61.2), be certain those spellings assure capture of all data points possible.

Emerging Pathogen Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_Vanc" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Emerging Pathogens (EPI) Primary menu Option: UP\<Enter\> Emerging Pathogens Parameter update

Select EMERGING PATHOGENS NAME: ? \<Enter\>

Answer with EMERGING PATHOGENS NAME, or REFERENCE NUMBER

Do you want the entire 14-Entry EMERGING PATHOGENS List? Y\<Enter\> (Yes)

Choose from:

CANDIDA

CLOSTRIDIUM DIFFICILE

CREUTZFELDT-JAKOB DISEASE

CRYPTOSPORIDIUM

DENGUE

E. COLI 0157:H7

HEPATITIS C ANTIBODY POS

LEGIONELLA

LEISHMANIASIS

MALARIA

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS-GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select EMERGING PATHOGENS NAME: VANC\<Enter\>-RES ENTEROCOCCUS

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 1 of 4

NAME: VANC-RES ENTEROCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Serology Lab Test(s) Indicator Value

\<Enter\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: VANC-RES ENTEROCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

Examples:Enterococcus

Enterococcus (Strept. faecalis-Group D)

Streptococcus faecalis Enterococcus durans

Streptococcus faecium Streptococcus sp. Group D

Enterococcus avium

Enterococcus avium - (Group D)

Enterococcus casseliflavus

Enterococcus faecalis

Enterococcus gallinarum

Enterococcus malodoratus Enterococcus

Enterococcus hirae solitarius

Enterococcus mundtii Enterococcus

Enterococcus raffinosus pseudoavium

Enterococcus sp. Enterococcus faecium

Enterococcus species Enterococcus durans

\<Enter\>Note: During the post Init, the ETIOLOGY FIELD file (#61.2) was searched to pre-populate the Etiology field (#3) in the EMERGING PATHOGENS file (#69.5). Listed above are examples of etiology entries which may have been populated from your site’s file. Additional etiologies may be added or deleted at the <u>Selected Etiology</u> prompt to meet your site specific needs.

> **NOTE:** If spelling differences occur within your ETIOLOGY FIELD file (#61.2) be consistent with your local file and spell the results here, as it is spelled in your file (even if it is spelled differently in the example). We are concerned more importantly with data <u>recovery</u>.

Antimicrobial Susceptibility NLT Code NLT Description

VANCOMYCIN\<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 3 of 4

NAME: VANC-RES ENTEROCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<Enter\> \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<Enter\> Press \<PF1\>H for help Insert

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 4 of 4

NAME: VANC-RES ENTEROCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Follow PTF: YES\<\<Enter\> Run Date: \<Enter\>

Run Cycle: MONTHLY\<Enter\> First Encounter: \<Enter\>

Protocol: LREPI\<Enter\> General Description: \<Tab\>Note: To review or

edit the General

Description use the

\<Enter\> key instead of

the \<Tab\> key.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<Enter\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<Enter\>

## Conclusion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have finished entering the information as directed by the national Infectious Diseases Program Office, these fields should not again be changed except for the following conditions:

1\. As requested by the national EPI program office to either update, modify, add, or delete data from the existing files used by the EPI software or an addition of a new entity to be tracked.

2\. At the yearly review to assure that the entry is acceptable and to update the EPI package with any changes in etiology, lab tests or results parameters which may have occurred locally at the site during the previous year.

Annually the EPI national package materials should be reviewed by the sites and updated. It is suggested that this review occur in February. If no changes have occurred in lab practices, etiologies, sites, or results parameters have occurred, leave the information as is until the next review period. If changes <u>did</u> occur, then enter them as appropriate in order to capture the data requested for each EPI national entity (disease/organism) to be tracked.

As entities (diseases/organisms) are no longer to be tracked nationally (“dropped from the list”), or a new entity is to be tracked (“added to the list”), revision will be forwarded to the sites to assist in updating your site files.

APPENDIX

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains instructions for validating data captures, defining files, linking of data, examples of verification reports, tables, request forms and a Helpful Hint section.

## Validation Of Data Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites will evaluate the EPI software program once it is implemented to assure that the software is accurately capturing VAHQ defined Emerging Pathogens.

Once the initial parameters update is completed, it is recommended that the Emerging Pathogen Manual Run option is run to evaluate 1-3 months of data (as determined by the sites). The Emerging Pathogens Verification Report is automatically generated, and should be compared with site specific records to assure optimal data capture of the Laboratory EPI program. This comparison will also help determine that site parameters for the EPI software has been accurately defined.

The Microbiology Laboratory staff, Laboratory Manager, TQI/QI/QA, or other person (as determined by the sites) may already have records of isolated “organisms of interest”. Several of nationally defined EPI pathogens may well correspond to those lists, and can thus be quickly compared to the Emerging Pathogens Verification Report to ensure that cases and numbers are being appropriately captured by the EPI program (this helps to determine that the site parameters for the EPI software has been installed optimally.)

For tests such as Hepatitis C, most Laboratory Managers should be able to generate reports (with patient names) that includes “positive” tests results to use for comparison.

Additionally, the Health Information Management Section at each site should be able to generate a report of ICD-9 and ICD-10 Diagnoses by date. This ICD Diagnoses by date Report will help determine if the 14 VAHQ defined Emerging Pathogens data captures will concur with the EPI criterion (i.e., Cryptosporidium-007.8, Legionnaire’s disease--482.80, malaria--084, 084.0, 084.1, 084.2, 084.3, 084.4, 084.5, 084.6, 085.7, 084.8, 084.9, dengue-061, 065.4, Creutzfeldt-Jakob--046.1, and Leishmaniasis--085, 085.0, 085.1, 085.2, 085.3, 085.4, 085.5, 085.9).

Be aware that a number of these Emerging Pathogens do not occur at a high frequency. Sites with previously known cases of Emerging Pathogens, such as TB, should run the Emerging Pathogen Manual Update option for the month that the TB culture was isolated to see if it is captured. Additionally, “test patients” known to have these lab results can also be run.

The purpose of this validation is not to require extra paperwork of QI monitors and long term document files. The validation is to be done at initial setup and reviewed once every 4-6 months to assure that parameters remain entered appropriately, or to achieve parameter changes if a new lab test or result format is implemented for one of the EPI.

### Emerging Pathogens Verification Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example:

Subj: Emerging Pathogens Verification Report \[#60004\] Page 1

----------------------------------------------------------------------------

REPORTING DATE FROM 12-01-1996 TO 12-31-1996 Message Seq \# 1 Auto

LABPATIENT, ONE 000-00-0001 07-07-1913 M WORLD WAR II 45205

Outpatient Accession Date 12-11-1996@1025

\*\*\*\*\*\*\*\*\* STREPTOCOCCUS GROUP A \*\*\*\*\*\*\*\*\*

12-11-1996@1025 BACT 96 10383 MICRO CULTURE LEG

1 12-13-1996 STREPTOCOCCUS BETA HEMOLYTIC, GROUP A

2 12-13-1996 STAPHYLOCOCCUS (COAGULASE NEGATIVE)

ORG \# 1 12-11-1996@1025 ANTIBIOTIC MIC LEG

ORG \# 2 12-11-1996@1025 ANTIBIOTIC MIC LEG

LABPATIENT, TWO 000-00-0002 01-08-1923 M WORLD WAR II 45239

Inpatient Admission Date 12-19-1996@1125

\*\*\*\*\*\*\*\*\*4 CLOSTRIDIUM DIFFICILE \*\*\*\*\*\*\*\*\*

Can be verified using standard result reviews for “CH” subscripted tests (e.g., LRRSP, LRRP3, LRSORD, LRSORA, LRGEN)

12-25-1996@1415 MSER 96 418 CHEMISTRY TEST FECES

Clostridium Difficile Toxin 12-27-1996@1403 POSITIVE

LABPATIENT, THREE 000-00-0003 11-05-1910 M WORLD WAR II 45255

Inpatient Admission Date 12-03-1996@1908

Discharge Date 12-09-1996@1151 Discharge Disposition REGULAR

250.01 DIABETES MELLI W/0 COMP TYP I

PTF data can be verified using several different PTF options:

DG PTF ICD DIAGNOSIS SEARCH

DG PTF SUMMARY DIAG/OP OUTPUT

DG PTF COMPREHENSIVE INQUIRY

(most require DGPTFSUP key)

276.8 HYPOPOTASSEMIA

427.31 ATRIAL FIBRILLATION

428.0 CONGESTIVE HEART FAILURE

482.30 PNEUM. UNSPEC. STREPTOCOCCUS

\*\*\*\*\*\*\*\*\*6 STREPTOCOCCUS GROUP A \*\*\*\*\*\*\*\*\*

12-04-1996 BACT 96 10187 MICRO CULTURE SPUTUM

1 12-06-1996 STREPTOCOCCUS BETA HEMOLYTIC, GROUP A

2 12-06-1996 STAPHYLOCOCCUS AUREUS

ORG \# 1 12-04-1996 ANTIBIOTIC MIC SPUTUM

ORG \# 2 12-04-1996 ANTIBIOTIC MIC SPUTUM

Microbiology subscripted organisms and susceptibilities can be reviewed using LRMIPSZ, LRMIPC, LRMIPLOG, LRGEN, LRRSP, and LRRP3.

Penicillin R

Clindamycin S

Vancomycin S

TETRCLN S

TRMSULF S

Erythromycin S

Oxacillin S

Cephalothin S

Ciprofloxacin S

AMPICILLIN-SULBACTAM S

LABPATIENT, FOUR 000-00-0004 02-23-1920 M PRE-KOREAN 45150

Inpatient Admission Date 11-18-1996@2213

\*\*\*\*\*\*\*\*\*8 CANDIDA \*\*\*\*\*\*\*\*\*

12-11-1996@0100 BLD 96 3914 MICRO CULTURE BLOOD

1 12-15-1996 CANDIDA ALBICANS

ORG \# 1 12-11-1996@0100 ANTIBIOTIC MIC BLOOD

LABPATIENT, FIVE 000-00-0005 12-23-1949 M VIETNAM ERA 45206

Outpatient Accession Date 12-20-1996@1309

\*\*\*\*\*\*\*\*\*2 HEPATITIS C ANTIBODY POS \*\*\*\*\*\*\*\*\*

12-20-1996@1309 RIA 1220 68 CHEMISTRY TEST SERUM

Hepatitis C Ab 01-03-1997@1347 STRONG POSITIVE -

LABPATIENT, SIX 000-00-0006 07-06-1919 M WORLD WAR II 41074

Outpatient Accession Date 12-19-1996@1007

\*\*\*\*\*\*\*\*\*1 VANC-RES ENTEROCOCCUS \*\*\*\*\*\*\*\*\*

12-19-1996@1007 BACT 96 10618 MICRO CULTURE URINE

1 12-23-1996 PSEUDOMONAS AERUGINOSA

2 12-23-1996 ENTEROCOCCUS FAECIUM

ORG \# 1 12-19-1996@1007 ANTIBIOTIC MIC URINE

Gentamicin S

Cefazolin R

Ampicillin R

Tobramycin S

TRMSULF R

Amikacin S

Cefoxitin R

Cefotaxime I

Nitrofurantoin R

Cefoperazone S

Mezlocillin S

### Table of Reject and Warning Codes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example:

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 24%" />
<col style="width: 0%" />
<col style="width: 29%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ERROR NUMBER</strong></td>
<td><strong>FIELD NAME</strong></td>
<td colspan="2"><strong>EDIT DESCRIPTION</strong></td>
<td><strong>ERROR MESSAGE</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td><em><strong>000 Series</strong></em></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><em>Miscellaneous</em></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>001</td>
<td>Message Control ID</td>
<td colspan="2">Must not be blank</td>
<td>Message control ID was blank</td>
</tr>
<tr class="odd">
<td>002</td>
<td colspan="2">Batch Sending Facility</td>
<td><p>Sending Station not valid.</p>
<p>(Refer to table AA001)</p></td>
<td>Invalid Batch Sending Facility.</td>
</tr>
<tr class="even">
<td>003</td>
<td colspan="2">Segment Name</td>
<td>PID Segment missing. Do not edit for the existence of PID when NTE segments are present.</td>
<td>PID Segment missing.</td>
</tr>
<tr class="odd">
<td>004</td>
<td colspan="2">Segment Name</td>
<td>PV1 Segment missing. Do not edit for the existence of PV1 when NTE segments are present.</td>
<td>PV1 Segment missing.</td>
</tr>
<tr class="even">
<td>005</td>
<td colspan="2">Segment Name</td>
<td>Invalid Segment name.</td>
<td>Invalid HL7 Segment name.</td>
</tr>
<tr class="odd">
<td>006</td>
<td colspan="2">Message Creation Date</td>
<td>Must a valid date.</td>
<td>Message Creation Date is invalid.</td>
</tr>
<tr class="even">
<td>007</td>
<td colspan="2">Message Creation Time</td>
<td>Must a valid time.</td>
<td>Message Creation Time is invalid.</td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><em><strong>100 Series</strong></em></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><em>NTE Totals Segment</em></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>100</td>
<td colspan="2">Action Ind</td>
<td>Currently not being used.</td>
<td>Currently not being used.</td>
</tr>
<tr class="even">
<td>105</td>
<td colspan="2">Totals Total Count</td>
<td>Must be numeric, if Action Ind is 'T '.</td>
<td>NTE Totals Total Count was not numeric.</td>
</tr>
<tr class="odd">
<td>110</td>
<td colspan="2">Negative Input Ind</td>
<td>Must be 'N', if Action Ind is not 'T '.</td>
<td>Negative Input Ind was not 'N'.</td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>200 Series</strong></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><em>PID Segment</em></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>200</td>
<td colspan="2">Patient Name</td>
<td>Required. Must be alphanumeric. Must not be all numeric. Must not be all blanks.</td>
<td>Patient Name is missing, or not alphanumeric, or all numeric, or all blanks.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 24%" />
<col style="width: 0%" />
<col style="width: 29%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ERROR NUMBER</strong></td>
<td><strong>FIELD NAME</strong></td>
<td colspan="2"><strong>EDIT DESCRIPTION</strong></td>
<td><strong>ERROR MESSAGE</strong></td>
</tr>
<tr class="even">
<td>205</td>
<td colspan="2">Patient Date of Birth</td>
<td>Not required. Must be less than the processing year.</td>
<td>Date of Birth is after the date of transmission. (see also W03, W04, and W05)</td>
</tr>
<tr class="odd">
<td>210</td>
<td colspan="2">Patient Sex</td>
<td>Not required. Must be blank or match table. (Refer to table T0001)</td>
<td>Sex code is not blank or a valid code. (Refer to table 0001).</td>
</tr>
<tr class="even">
<td>215</td>
<td colspan="2">Patient Race</td>
<td>Not required. Must be blank or a valid code. (Refer to table VA07)</td>
<td>Race code is not blank or a valid code. (Refer to table VA07).</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>220</p>
</blockquote></td>
<td><blockquote>
<p>Patient Address</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Must be blank or 'H'.</p>
</blockquote></td>
<td><blockquote>
<p>Patient Address is not blank or 'H'.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>224</p>
</blockquote></td>
<td><blockquote>
<p>Patient Zip Code</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Not required. Must be blank or numeric. If numeric, first five digits must not be all zeros. If last four digits exist, then must be numeric.</p>
</blockquote></td>
<td><blockquote>
<p>Address - Zip Code is missing or not numeric.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>235</p>
</blockquote></td>
<td><blockquote>
<p>Social Security Number</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Required. Last byte must be 'P' or blank.</p>
</blockquote></td>
<td><blockquote>
<p>Pseudo SSN is not 'P' or blank.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>236</p>
</blockquote></td>
<td><blockquote>
<p>Social Security Number</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Required. Must be numeric. Must be greater than zeros.</p>
</blockquote></td>
<td><blockquote>
<p>Social Security Number is missing, or not numeric, or is equal to zeros.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>240</td>
<td><blockquote>
<p>Patient Veteran Status</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Must be a valid code. (Refer to table VA11)</p>
</blockquote></td>
<td><blockquote>
<p>Period of Service was invalid. (Refer to table VA11).</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>300 Series</strong></em></p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>OBR Segment</em></p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>300</p>
</blockquote></td>
<td><blockquote>
<p>Universal Service ID</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Must be a valid code. (Refer to table NLT)</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Universal Service ID (Refer to table NLT).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>305</p>
</blockquote></td>
<td><blockquote>
<p>Observation Date</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Must be numeric date. Must be a valid date. Must be less than processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Observation Date is invalid date or after the date of transmission.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>307</p>
</blockquote></td>
<td><blockquote>
<p>Observation Time</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Not required. Must be blank or numeric. If numeric, must be a valid time.</p>
</blockquote></td>
<td><blockquote>
<p>Observation Time is invalid.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>310</p>
</blockquote></td>
<td><blockquote>
<p>Specimen Source Code</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Not required. If not blank, must be a valid code. (Refer to table SPC)</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Specimen Source Code (Refer to table (SPC). (see also W07)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>315</p>
</blockquote></td>
<td><blockquote>
<p>Parent Observation ID</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Not required. Must be blank or a valid code. (Refer to table NLT)</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Parent Observation ID (Refer to table NLT).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 24%" />
<col style="width: 29%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>ERROR NUMBER</strong></td>
<td><strong>FIELD NAME</strong></td>
<td><strong>EDIT DESCRIPTION</strong></td>
<td><strong>ERROR MESSAGE</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>400 Series</strong></em></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>PV1 Segment</em></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>400</p>
</blockquote></td>
<td><blockquote>
<p>Patient Class</p>
</blockquote></td>
<td><blockquote>
<p>Required. Must be 'I', 'O', or 'U'.</p>
</blockquote></td>
<td><blockquote>
<p>Patient Class is not 'I', 'O', or 'U'.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410</p>
</blockquote></td>
<td><blockquote>
<p>Discharge Date</p>
</blockquote></td>
<td><blockquote>
<p>Not required. Must be blank or a valid date. Must be less than or equal to processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Discharge Date is invalid or after date of transmission.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>411</p>
</blockquote></td>
<td><blockquote>
<p>Discharge Time</p>
</blockquote></td>
<td><blockquote>
<p>Not required. Time must be blank or a valid time.</p>
</blockquote></td>
<td><blockquote>
<p>Discharge Time is invalid.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>420</p>
</blockquote></td>
<td><blockquote>
<p>Admit Date/Time</p>
</blockquote></td>
<td><blockquote>
<p>Required. Must be numeric. Must be a valid date. Must be less than or equal to processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Admit Date is invalid or after date of transmission.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>421</p>
</blockquote></td>
<td><blockquote>
<p>Admit Date/Time</p>
</blockquote></td>
<td><blockquote>
<p>Required. Time must be numeric. Must be a valid time.</p>
</blockquote></td>
<td><blockquote>
<p>Admit Time is invalid.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>500 Series</strong></em></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>DG1 Segment</em></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>500</p>
</blockquote></td>
<td><blockquote>
<p>Diagnosis Code</p>
</blockquote></td>
<td><blockquote>
<p>Required. Must be a valid code. (Refer to table AA010)</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Diagnosis Code (Refer to table 0051).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>600 Series</strong></em></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>OBX Segment</em></p>
</blockquote></td>
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
<td><blockquote>
<p>600</p>
</blockquote></td>
<td><blockquote>
<p>Observation Nat Lab Num</p>
</blockquote></td>
<td><blockquote>
<p>If not blank, must be a valid code. (Refer to table NLT)</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Observation Nat Lab Num (Refer to table NLT). (see also W09)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>605</p>
</blockquote></td>
<td><blockquote>
<p>Final Result Date</p>
</blockquote></td>
<td><blockquote>
<p>Must be blank or a valid date. Must be numeric. Must be a less that or equal to processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Final Result Date is invalid or after the date of transmission.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em><strong>W00 Series</strong></em></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>Warnings</em></p>
</blockquote></td>
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
<td><blockquote>
<p>W03</p>
</blockquote></td>
<td><blockquote>
<p>Patient Date of Birth</p>
</blockquote></td>
<td><blockquote>
<p>Must not be all spaces.</p>
</blockquote></td>
<td><blockquote>
<p>Patient Date of Birth is all spaces. (see also 205)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W04</p>
</blockquote></td>
<td><blockquote>
<p>Patient Date of Birth</p>
</blockquote></td>
<td><blockquote>
<p>Year must not be all zeros.</p>
</blockquote></td>
<td><blockquote>
<p>Patient Date of Birth Year is all zeros. (see also 205)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>W05</p>
</blockquote></td>
<td><blockquote>
<p>Patient Date of Birth</p>
</blockquote></td>
<td><blockquote>
<p>Must be a valid date.</p>
</blockquote></td>
<td><blockquote>
<p>Patient Date of Birth is not in a valid date format. (see also 205)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W07</p>
</blockquote></td>
<td><blockquote>
<p>Speciman Source Code</p>
</blockquote></td>
<td><blockquote>
<p>Blanks in code.</p>
</blockquote></td>
<td><blockquote>
<p>Speciman Source code is blank. (see also 310)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>W09</p>
</blockquote></td>
<td><blockquote>
<p>Observation Nat Lab Num</p>
</blockquote></td>
<td><blockquote>
<p>Blanks in code.</p>
</blockquote></td>
<td><blockquote>
<p>Observation Nat Lab Num is blank. (see also 600)</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Editing TOPOGRAPHY file (#61)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific HL7 codes must be added to the TOPOGRAPHY file (#61). The HL7 Code field (#.08) in this file is used to add the entries. The specific HL7 codes that must be added to File (#61) is located in the HL7 section of this guide, Table 0070 (Specimen Source Codes). The following is an example of how to add the specific HL7 codes to the TOPOGRAPHY file (#61) using VA FileMan - Enter Or Edit File Entries option.

Example: How to Populate TOPOGRAPHY file (#61) with HL7 codes.

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: TOPOGRAPHY FIELD// \<Enter\>

EDIT WHICH FIELD: ALL// .08 HL7 CODE

THEN EDIT FIELD: \<Enter\>

Select TOPOGRAPHY FIELD NAME: ? \<Enter\>

Answer with TOPOGRAPHY FIELD NAME, or SNOMED CODE, or ABBREVIATION, or

SYNONYM

Do you want the entire 8575-Entry TOPOGRAPHY FIELD List? NO\<Enter\>

You may enter a new TOPOGRAPHY FIELD, if you wish

ANSWER MUST BE 2-80 CHARACTERS IN LENGTH

Select TOPOGRAPHY FIELD NAME: AMNIOTIC FLUID 8Y300

HL7 CODE: ? \<Enter\>

Answer must be 2-4 characters in length.

Enter the two to four character code from the left column:

ABS ABCs

AMN Amniotic fluid

ASP Aspirate

BPH Basophils

ABLD Blood arterial

BBL Blood bag

BON Bone

BRTH Breath

BRO Bronchial

BRN Burn

Enter RETURN to continue or '^' to exit: ^

HL7 CODE: AMN\<Enter\>

## How to Link Antimicrobial Entries to Workload Codes Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post INIT links as many of the ANTIMICROBIAL SUSCEPTIBILITY' file (#62.06) entries to the WKLD CODE file (#64) entries that are identified in your site files. However, the ANTIMICROBIAL SUSCEPTIBILITY' file (#62.06) entries that were not linked (i.e. no match found) to the WKLD CODE file (#64) entries by the post INIT will require linking. The Antimicrobial Link Update option contains the following three options that are used to <u>identify</u> and <u>link</u> the entries that were not linked by the post INIT.

AUTO: This option will identify and attempt to link any entries that are not currently linked.

Manual: This option can create or edit the links. Selection is by entry in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06).

Semi-Auto: This option looks for entries that are not currently linked and prompts the user to select the corresponding entry in the WKLD CODE file (#64).

Examples: Using the Antimicrobial Link Update option.

Select Emerging Pathogen Primary Menu\<Enter\>

MAN Emerging Pathogen Manual Run

LK Antimicrobial Link Update

UP Emerging Pathogens Parameter update

Select Emerging Pathogens (EPI) Primary menu Option: LK \<Enter\> Antimicrobial Link Update

This option will allow you to link file '62.06 ANTIMICROBIAL

SUSCEPTIBILITY' file with file '64 WKLD CODE.

Select one of the following:

A AUTO

M MANUAL

S SEMI-AUTO

Example: How to add links using the AUTO option. This option will also display linked and non linked entries.

Enter response: A\<Enter\>UTO

AMIKACN \<----Linked----\> Amikacin

AMPICLN \<----Linked----\> Ampicillin

CLINDAM \<----Linked----\> Clindamycin

POLYMYXIN B \<----Not Linked----\>No Match Found

RIFAMPIN \<----Linked----\> Rifampin

Example: How to add and delete entries using the MANUAL option.

Enter response: M\<Enter\>ANUAL

Select ANTIMICROBIAL SUSCEPTIBILITY NAME: PENICLIN\<Enter\> PENICILLIN

NATIONAL VA LAB CODE: Substance P// PEN\<Enter\>

1 PENFIELD AND CONE STAIN 88010.0000

2 PENICILLIN Penicillin 81852.0000

3 PENTAZOCINE Pentazocine 81854.0000

4 PENTOBARBITAL Pentobarbital 81856.0000

CHOOSE 1-4: 2 Penicillin\<Enter\>

Select ANTIMICROBIAL SUSCEPTIBILITY NAME: VANCMCN\<Enter\> VANCOMYCIN

NATIONAL VA LAB CODE: Shell Vial Technique// VANCOMYCIN\<Enter\> Vancomycin

81485.0000\<Enter\>

Select ANTIMICROBIAL SUSCEPTIBILITY NAME: Ampicillin/sulbactam\<Enter\> Ampicillin/subalctam

NATIONAL VA LAB CODE: Ampicillin// @\<Enter\>

SURE YOU WANT TO DELETE? Y (Yes)\<Enter\>

Select ANTIMICROBIAL SUSCEPTIBILITY NAME:

Example: How to add entries using the SEMI-AUTO option

Enter response: S\<Enter\>EMI-AUTO

AMIKACN AMIKACIN

NATIONAL VA LAB CODE: AMIK\<Enter\>ACIN Amikacin 81098.0000

Continue YES/\<Enter\>

AMPICLN AMPICILLIN

NATIONAL VA LAB CODE: AMP\<Enter\>

1 AMP CYCLIC 81029.0000

2 AMPHETAMINE Amphetamine 81528.0000

3 AMPHOTERICIN B Amphotericin B 81530.0000

4 AMPICILLIN Ampicillin 81532.0000

CHOOSE 1-4: 4 Ampicillin

Continue YES// \<Enter\>

CLINDAM CLINDAMYCIN

NATIONAL VA LAB CODE: CLINDAMYCIN Clindamycin 81676.0000

Continue YES// \<Enter\>

CARBCLN CARBENICILLIN

NATIONAL VA LAB CODE:

Continue YES// NO \<Enter\>

### ### ### Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following page contains a Request Form that may be reproduced and used for requesting additional Workload and Suffixes codes as needed by your site. Please submit the Request Form to the address located at bottom of form.

Additional Workload Codes and Workload Codes SuffixesRequest Form

Site Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Site Number: \_\_\_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_\_\_

Contact Person: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Commercial Ph#: \_\_\_\_\_\_\_\_\_\_\_\_\_\_ Ext. \_\_\_\_

FTS Phone: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Ext. \_\_\_\_

Procedure Name \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_

Abbreviations: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Procedure Name \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_

Abbreviations: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Procedure Name \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_

Abbreviations: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Procedure Name \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_

Abbreviation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Method: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_

Abbreviation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Method: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_

Abbreviation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Method: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_

Abbreviation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Submit Request Forms to:

Frank Stalling, P&LMS Informatics Manager

1901 North Highway 360, Suite 351

> Grand Prairie, Texas 75050

## Helpful Hints:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Screens Enter/Edits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Emerging Pathogen Primary Menu options are using VA FileMan screens displays, referred to as ScreenMan. For <u>detailed</u> instructions on how to use the screens displays please review the VA FileMan V. 21.0 User Manual, Section 6 ScreenMan.

#### How to delete a entry.

Use the Return key to move the cursor. When the entry that is to be deleted is highlighted enter a “@” then press enter/return. You will then receive a deletion warning and asked if you are sure.

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: CANDIDA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

CANDIDA PARAPSILOSIS \<Tab\>

CANDIDA PSEUDOTROPICALIS \<Tab\>CANDIDA SKIN TEST ANTIGEN @ \<Enter\>

CANDIDA STELLATOIDEA

Antimicrobial Susceptibility NLT Code NLT Description

\<Tab\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: Press \<PF1\>H for help

> **WARNING:** DELETIONS ARE DONE IMMEDIATELY!

(EXITING WITHOUT SAVING WILL NOT RESTORE DELETED RECORDS.)

Are you sure you want to delete this entire Subrecord (Y/N)? y \<Enter\>

#### How to add a entry

Use the tab key to move the cursor and highlight a blank line were the entry is to be added.

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: CANDIDA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

CANDIDA

CANDIDA GUILLIERMONDII

CAN \<Enter\>

Antimicrobial Susceptibility NLT Code NLT Description

\<Tab\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1 CAN CANDIDA ALBICANS 4081

2 CANARYPOX VIRUS 3604

3 CANDICIDIN 7328

4 CANDIDA, NOS 4080

5 CANDIDA GUILLIERMONDII 4082

Choose 1-5 or '^' to quit: 1\<Enter\>

EMERGING PATHOGEN SITE PARAMETERS INPUT SCREEN Page 2 of 4

NAME: CANDIDA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

CANDIDA GUILLIERMONDII

CANDIDA KRUSEI

CANDIDA ALBICANS \<- The entry will appear after answering yes

to the adding a new ETIOLOGY prompt.

Antimicrobial Susceptibility NLT Code NLT Description

\<Tab\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CAN CANDIDA ALBICANS

Are you adding 'CANDIDA ALBICANS' as a new ETIOLOGY? Y \<Enter\>

### Clostridium difficile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two preferred methods for the Laboratory EPI patch that may make it easy to capture for the EPI data, as well as several other methods which site may already employ. As long as the designated parameter result to be obtained is in a. retrievable field and not a free text or comment field, the method the site chooses is an individual decision.

One of two preferred methods, would be to have a site etiology of “Clostridium difficile toxin positive”. This would allow a topography specimen of accession area “feces/stool” to be accessioned through the Microbiology accession area. Then, if the stool specimen was indeed positive for *Clostridium difficile* toxin, by any of the known methods of testing, the etiology would be “Clostridium difficile toxin positive.” To accomplish this would require sites to enter three new local etiologies:

1\) Clostridium difficile toxin positive

> 2\) Clostridium difficile toxin negative

3\) Clostridium difficile toxin indeterminant

These would be different from a culture isolate being positive for *Clostridium difficile,* in that they actually are etiologies/results based on toxin testing. This then leaves the etiology of *Clostridium difficile* for actual culture positive specimens for the organism *Clostridium difficile*. Then at the EPI parameter update, the site parameter by which the EPI program will capture a patient diagnosed with proven *Clostridium difficile*-associated colitis, will be by placing “Clostridium difficile toxin positive” etiology into the selected etiology entry screen. This has the advantage of being more consistent with other data entry practices in the Microbiology sections of most laboratories.

A second preferred method of having the data in retrievable form would be to enter/accession the specimen for *Clostridium difficile* toxin assay under the chemistry/serology format (regardless of where the test is physically done) with the results being a choice of “positive”, “negative”, or “indeterminate”. This would allow one to enter *“Clostridium difficile* toxin” assay as the test for the EPI program to search in the chemistry/serology format. The result would be retrievable for the EPI package under a chemistry/serology lab test of “*Clostridium difficile* toxin” with the indicator “contains” and the value of “pos”, as noted in the sample page. If your site does not routinely do *Clostridium difficile* toxin assay testing this way, a different method of accessioning the specimen (to get it in chemistry/serology format would be needed.

However, the Chemistry/Serology format would give additional flexibility in placing interpretational guidelines for the test results in the “Comments” field. For the EPI package, “positive” or “negative” results cannot be located in a free text or comments section as these are not retrievable.

Some VAs accession the stool specimen for the *Clostridium difficile* toxin assay under Microbiology format. An etiology is not given under the final culture result, but written into free text or comments section stating the *Clostridium difficile* toxin assay test result. This is not in a retrievable format and therefore not acceptable for the EPI package.

Some VAs still use cytotoxin assays of cell culture which are again entered as free text or under the comments section. This again is not acceptable unless it is accessioned and recorded under the chemistry/serology format as a straightforward lab test result of “positive” or “negative” or “indeterminate”.

Some VAs choose to report *Clostridium difficile* toxin assay positivity under the Microbiology package, as an etiology/culture result of *Clostridium difficile* (even though culture, was not actually done) this is not a true measure of what is actually being tested (as most sites do not culture the organism but just run the toxin assay test). However, if your site uses this means to represent *Clostridium difficile* toxin assay positivity and there are no exceptions (such as the site reporting an actual positive culture of (*Clostridium difficile* which is toxin assay negative), then this would be acceptable though less desirable for EPI purposes.

### EPI Mail Groups Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two mail groups have been determined for the Emerging Pathogens Initiative program. The EPI mail group and the EPI-Report mail group. The EPI mail group is a national mail group and will serve as the communication for the EPI patch between the local site and the and the Austin Automation Center. The EPI Report mail group is a local site mail group to receive verification reports and other information as directed. Additionally, one individual/function at site should be responsible for the EPI mail group, but the EPI-Report mail group may contain one or several individual/function, of which the EPI mail group individual(s) function(s) will most likely be a member.

#### Office of the Director (00)

The Office of the Director (00) will be the initial individual/function to whom the EPI mail and EPI-Report mail groups will be directed. The Office of the Director at each site will then determine responsible individual(s)/function(s) for the mail groups. The following are explanations of the functions of each of these two mail groups, with suggestions as to which site individual(s)/function(s) may be appropriate to consider for membership of these groups. Other individual(s)/ function(s) may desire access to this at site for assuring that the EPI information is collected and transmitted properly.

EPI mail group

The function of the EPI mail group is to transmit the site message (in HL7 format as defined by the EPI patch) to the Austin Automation Center. Additionally, this mail group will receive confirmation messages from Austin Automation Center that the report has been received and a receipt verification number which should be kept for future reference. Further, if the message has an error or is unacceptable to be received at the Austin Automation Center, an error message or messages will be sent to the EPI mail group individual/function at the site to attend or to corrections before re-transmittal of the message. Once the corrections are made, it will be the responsibility of the EPI mail group individual(s)/function(s) at site to retransmit the data to the Austin Automation Center. Because the information being collected and transmitted is being obtained from numerous different areas/functions/services (Patient Treatment Files, Medical Administration Service, Health Information Management Section, Laboratory, IRM, etc.) it is recommended that a TQI/QI/QA staff (or person with similar function at site) be the responsible party for this function.

EPI-Report mail group

The function of the EPI-Report mail group is to receive the site message (formatted from the HL7 message into a more readable format.) The EPI-Report mail group is composed of those who will receive this local site Emerging Pathogens Verification Report from the automatic monthly runs and from manual runs (and reruns if necessary). Again, this report is the Emerging Pathogens Verification Report, and is used to assist in verification as previously described (see the Appendix section of this guide). Obviously, the individual(s)/function(s) designated to be responsible for the transmission of the data to the Austin Automation Center (i.e. EPI mail group) should be contained within this mail group because of the more easily readable format in which the report is generated. However, others on site, may also be appropriate to receive this data, such as Laboratory Information Manager, Microbiology director or supervisor, Infection Control Practitioners, or Hospital Epidemiologist. These individuals should all be considered to be included in this mail group as they may derive benefit from the local report, but further, they may be of assistance with verification or with the periodic validation (see the Appendix section for example of the verification report), as deemed appropriate by site. Be aware that validation and verification are two different processes.

### Transmitting a Message to Austin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On or about the 15<sup>th</sup> of the month the EPI package will produce two mail messages. Both messages are comprised of the same data , the only difference being the format of the data. In the verification report portions of the data has been extracted from the HL7 message. Use the verification message to insure the accuracy of the data that will be sent to Austin. If the extracted data is incorrect make the corrections and rerun the Search/Extract using the “Emerging Pathogen Manual Run” option to build the messages again. When satisfied with the report transmit the HL7 Message to Austin Information Technology Center (AITC). Do not transmit the verification report. The HL7 messages need to be sent to Austin by the 25<sup>th</sup> of the month. Once the message has been received by Austin a confirmation message will be returned indicating that they have received the message. At the end of the cycle Austin will process the messages and transmit a processing report back confirming the data and/or listing any error/warning codes.

To transmit the HL7 message forward the message to XXX@Q-EPI.

Example:

Subj: HL7 Message FEB 10,1997@15:56:29 from Station XXX STATION XXX \[#63430\]

10 Feb 97 15:56 262 Lines

From: POSTMASTER (Sender: ANYBODY) in 'IN' basket. Page 1

----------------------------------------------------------------------------

MSH\|~^\\\|EPI-LAB\|\|EPI-LAB\|\|19970210155618\|\|ORU~R01\|483\|P\|2.2\|\|\|NE\|NE\|USA

NTE\|\|R~REPORTING DATE FROM 19960101 TO 19970131~1

PID\|1\|000-00-0007~4~M10\|17~8~M10\|\|LABPATIENT, SEVEN\|\|19840426\|M\|\|7\|~\|\|\|\|\|\|\|\|<span id="p421_114" class="anchor"></span>000543435

PV1\|1\|O\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|19960312123902

NTE\|1\|1~VANC-RES ENTEROCOCCUS

OBR\|1\|\|\|81121.0000~CHEMISTRY TEST~VANLT\|\|\|19960312123902\|\|\|\|\|\|\|\|SER\~~SERUM\|\|\|CH

0312 14

OBX\|1\|ST\|\~\~~183~CHOLESTEROL~VA60\|\|190\|mg/dL\|\$S(AGE\<50:135,1:120)-288\|\|\|\|\|\|\|1996

0328145221

Enter RETURN to continue or '^' to exit: ^\<Enter\>

Select MESSAGE Action: IGNORE (IN basket)// FORWARD\<Enter\>

Send mail to: XXX@Q-EPI \<Enter\>.MED.VA.GOV via FOC-AUSTIN.VA.GOV

And send to: \<Enter\>.

Mail forwarded

### EPI Processing Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: EPI/LRK \#970451447950300 \[#1425971\] 14 Feb 97 14:55 CST 50 Lines

From: \<<span class="mark">REDACTED</span>\> in 'IN' basket. Page 1 \*\*NEW\*\*

---------------------------------------------------------------------------

2EPI0001 LRK.

STATION XXX EPI PROCESSING REPORT REPORT DATE 1997/02/11 PAGE 01

PROCESS DATE SSN ENCOUNTER DATE MESSAGE ERROR CODES

19970131 000000190 19970131132151 001 NO ERRORS

19970131 000466370 19961002160512 001 500

19970131 000225556 19970121121609 001 NO ERRORS

19970131 000368799 19961229043131 001 NO ERRORS

19970131 000187860 19960917165748 001 NO ERRORS

19970131 000267678 19970131125821 001 NO ERRORS

19970131 000385860 19961230185116 001 NO ERRORS

19970131 000385860 19970107162010 001 NO ERRORS

19970131 000684002 19970109103417 001 NO ERRORS

19970131 000501279 19970128090146 001 NO ERRORS

19970131 000549144 19970108132918 001 NO ERRORS

19970131 000302298 19970108082142 001 NO ERRORS

19970131 000345601 19970113114752 001 NO ERRORS

19970131 000166277 19970122095702 001 NO ERRORS

19970131 000541525 19970106225241 001 NO ERRORS

19970131 000328446 19970114143128 001 NO ERRORS

19970131 000425965 19970131105820 001 NO ERRORS

19970131 000205512 19960607174229 001 NO ERRORS

19970131 000384641 19970114082310 001 NO ERRORS

19970131 000185119 19960220155121 001 NO ERRORS

19970131 000609042 19970129172826 001 NO ERRORS

19970131 000364130 199701141902 001 NO ERRORS

19970131 000565414 19961011133221 001 500

19970131 000749494 19970123203635 001 NO ERRORS

19970131 000461267 19970121115616 001 NO ERRORS

19970131 000769911 19970115085841 001 NO ERRORS

19970131 000783854 19970118162650 001 NO ERRORS

19970131 000387083 19961028154210 001 NO ERRORS

19970131 000061089 19961115111612 001 NO ERRORS

19970131 000376819 19970126001019 001 NO ERRORS

19970131 000376819 19970126003234 001 NO ERRORS

19970131 000701169 19970121162629 001 NO ERRORS