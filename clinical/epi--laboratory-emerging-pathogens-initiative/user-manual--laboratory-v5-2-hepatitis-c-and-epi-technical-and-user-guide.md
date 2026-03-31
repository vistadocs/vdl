---
title: Laboratory Version 5.2 Hepatitis C and EPI Technical and User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Hepatitis C and EPI Technical and
app_code: EPI
app_name: "Laboratory: Emerging Pathogens Initiative"
section: CLI
app_status: active
pkg_ns: EPI
patch_ver: 5.2
patch_id: EPI*5.2
group_key: "EPI:EPI:5.2"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - blockquote
  - class
  - table
  - strong
  - contents
  - even
  - date
  - style
  - width
  - alphanumeric
page_count: 0
word_count: 16211
section_count: 67
table_count: 8
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Emerging_Pathogens_Initiative/lab_epi_hepc_tech_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Emerging_Pathogens_Initiative/lab_epi_hepc_tech_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=118"
---

LaboratoryEmerging Pathogens Initiative (EPI)Version 5.2Hepatitis C Extract and EPI Technical and User Guide

![](laboratory-version-5-2-hepatitis-c-and-epi-technical-and-user-guide/001.png)

September 2015Department of Veterans Affairs (VA)Office of Information and Technology (OI&T)Product Development (PD)Revision History

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 19%" />
<col style="width: 40%" />
<col style="width: 23%" />
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
<td><p>LR*5.2*442, ICD-10 Patient Treatment File (PTF) Modifications:</p>
<p>Reformatted title page and footers. Added text to Preface (p.iv), added DBIA #6130 (p.11), added text to Required Patches (p.13), reformatted and updated Routine List (p.14), updated Post Installation (p.18), and updated Installation Instructions (p.23).</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/2014</td>
<td><p>LR*5.2*421</p>
<p>i-ii</p>
<p>p. <a href="#p421_v">iii</a></p>
<p>vii-x</p>
<p>p. <a href="#_Toc425208766"><u>13</u></a></p>
<p>p. <a href="#lab-searchextract-file-69.5">14</a></p>
<p>p. <a href="#p421_25">24</a></p>
<p>p. <a href="#p421_26">25</a></p>
<p>p. <a href="#p41">41</a></p>
<p>p. <a href="#p421_43">42</a></p>
<p>pp.<a href="#p421_48">47</a>, <a href="#p421_49">48</a>, <a href="#p421_53">52</a>, <a href="#p421_55">54</a>, <a href="#p421_56">55</a>, <a href="#p421_58">57</a>, <a href="#p421_59">58</a><u>,</u> <a href="#p421_60">59</a><u>,</u> <a href="#ICDM9toICD4">61</a><u>,</u> <a href="#p421_63">62</a><u>,</u> <a href="#p421_66">65</a><u>,</u> <a href="#p421_67">66</a><u>,</u> <a href="#p421_70">69</a><u>,</u> <a href="#p421_71">70</a><u>,</u> <a href="#p421_74">73</a><u>,</u> <a href="#p421_75">74</a><u>,</u> <a href="#p421_78">77</a><u>,</u> <a href="#p421_79">78</a><u>,</u> <a href="#p421_82">81</a><u>,</u> <a href="#ICD_Hep_C_POS_2">82</a><u>,</u> <a href="#p421_85">84</a><u>,</u> <a href="#p421_86">85</a><u>,</u> <a href="#p421_88">87</a><u>,</u> <a href="#p421_89">88</a><u>,</u> <a href="#p421_91">90</a><u>,</u> <a href="#p421_92">91</a><u>,</u> <a href="#p421_94">93</a><u>,</u> <a href="#ICD_Pneu_2">94</a><u>,</u> <a href="#p421_97">96</a><u>,</u> <a href="#ICD_Strep_2">97</a><u>,</u> <a href="#p421_100">99</a><u>,</u> <a href="#p421_101">100</a><u>,</u> <a href="#p421_104">103</a><u>,</u> <a href="#p421_111">110</a><u>,</u> <a href="#p421_113">112</a><u>,</u> <a href="#p421_123">121</a></p>
<p>multiple pages</p></td>
<td><p>Updated for ICD-10 Remediation:</p>
<p>Added Revision History</p>
<p>Updated Preface for LR*5.2*421</p>
<p>Updated Table of Contents</p>
<p>Added required patches for installation of LR*5.2*421</p>
<p>Added new routines for LR*5.2*421</p>
<p>Added note for installation instructions</p>
<p>Added information on HL7 message segment for ICD-10</p>
<p>Added note to explain new prompts for ICD-9 or ICD-10 codes</p>
<p>Revised ICD description information in Laboratory Search/Extract Parameters Input Screen and updated references to ICD in the Prompts Definitions table</p>
<p>Added new prompt and headings for ICD codes and changed multiple instances of ICD-9 to ICD</p>
<p>Changed AAC to Austin Information Technology Center (AITC) throughout manual</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>08/2000</td>
<td>LR*5.2*260</td>
<td>Initial release</td>
<td>VA OI&amp;T</td>
</tr>
</tbody>
</table>

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Recommended Users](#recommended-users)
  - [Technical and User Guide Distributions](#technical-and-user-guide-distributions)
  - [Technical and User Guide Orientation](#technical-and-user-guide-orientation)
  - [Screen Dialogue](#screen-dialogue)
  - [Related Manuals](#related-manuals)
- [Overview](#overview)
  - [Emerging Pathogens Initiative (EPI)](#emerging-pathogens-initiative-epi)
  - [Hepatitis C Assessment for Risk](#hepatitis-c-assessment-for-risk)
  - [Associated VISTA Software Applications](#associated-vista-software-applications)
    - [VISTA BLOOD BANK SOFTWARE](#vista-blood-bank-software)
  - [Austin Information Technology Center Database Processing](#austin-information-technology-center-database-processing)
  - [EPI Data Transmission](#epi-data-transmission)
  - [AITC Transmission Reports](#aitc-transmission-reports)
  - [# Enhancements](#enhancements)
- [Pre-Installation Information](#pre-installation-information)
  - [IRM Staff](#irm-staff)
  - [Laboratory Staff](#laboratory-staff)
  - [Hardware and Operating System Requirements](#hardware-and-operating-system-requirements)
    - [Digital Equipment Corporation (DEC) Alpha Series](#digital-equipment-corporation-dec-alpha-series)
    - [Personal Computer (PC) System](#personal-computer-pc-system)
  - [System Performance Capacity](#system-performance-capacity)
  - [Installation Time](#installation-time)
  - [Users on the System](#users-on-the-system)
  - [Namespace](#namespace)
  - [Database Integration Agreements (DBIAs)](#database-integration-agreements-dbias)
  - [VISTA Software Requirements](#vista-software-requirements)
  - [Required Patches](#required-patches)
  - [Health Level Seven (HL7)](#health-level-seven-hl7)
  - [Protocols](#protocols)
  - [## Domain](#domain)
  - [Mail Groups](#mail-groups)
  - [Backup Routines](#backup-routines)
  - [Routine List](#routine-list)
  - [LAB SEARCH/EXTRACT file (#69.5)](#lab-searchextract-file-695)
  - [## New LREPI REMINDER LINK file (#69.51)](#new-lrepi-reminder-link-file-6951)
  - [Routine Summary](#routine-summary)
  - [Installation Process](#installation-process)
- [Post Installation Instructions](#post-installation-instructions)
  - [IRM Staff](#irm-staff-1)
  - [LIM Staff](#lim-staff)
  - [NOTE: For patch LR\5.2\442 installation instructions, please refer to the ICD-10 PTF Modifications Installation Guide: <http://www.va.gov/vdl/application.asp?appid=118>](#note-for-patch-lr52442-installation-instructions-please-refer-to-the-icd-10-ptf-modifications-installation-guide-httpwwwvagovvdlapplicationaspappid118)
- [Health Level Seven (HL7) Protocol](#health-level-seven-hl7-protocol)
  - [General Specifications](#general-specifications)
  - [Definitions from Austin](#definitions-from-austin)
    - [Transaction Specifications](#transaction-specifications)
- [Laboratory Hepatitis C Extract and EPI User Guide](#laboratory-hepatitis-c-extract-and-epi-user-guide)
  - [Lab Search/Extract Primary \[LREPI SEARCH EXTRACT MENU\] Menu](#lab-searchextract-primary-lrepi-search-extract-menu-menu)
  - [> <span id="p41" class="anchor"></span>NOTE: Patch LR\5.2\421 adds prompts to the Enter/Edit Local Pathogens and Laboratory Search/Extract Parameters Input screens for users to specify a code set on which to search prior to entering an ICD code. Based on this input, the system only allows either ICD-9 entry or ICD-10 entry.](#span-idp41-classanchorspannote-patch-lr52421-adds-prompts-to-the-enteredit-local-pathogens-and-laboratory-searchextract-parameters-input-screens-for-users-to-specify-a-code-set-on-which-to-search-prior-to-entering-an-icd-code-based-on-this-input-the-system-only-allows-either-icd-9-entry-or-icd-10-entry)
  - [Laboratory Search/Extract Parameters Input Screen](#laboratory-searchextract-parameters-input-screen)
  - [Prompts Definitions](#prompts-definitions)
  - [Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option](#lab-searchextract-parameter-setup-lrepi-parameter-setup-option)
    - [Candida (Reference \#8)](#candida-reference-8)
    - [Clostridium difficile (Reference \#4)](#clostridium-difficile-reference-4)
    - [Creutzfeldt-Jakob Disease (CJD) (Reference \#13](#creutzfeldt-jakob-disease-cjd-reference-13)
    - [Cryptosporidium (Reference \#9)](#cryptosporidium-reference-9)
    - [Dengue (Reference \#12)](#dengue-reference-12)
    - [E. coli O157:H7 (Reference \#10)](#e-coli-o157h7-reference-10)
    - [Hepatitis A Antibody Positive (Reference \#16)](#hepatitis-a-antibody-positive-reference-16)
    - [Hepatitis B Positive (Reference \#17)](#hepatitis-b-positive-reference-17)
    - [Not Positive for Hepatitis C Antibody OR Hepatitis C Antibody Neg (Reference \#15)](#not-positive-for-hepatitis-c-antibody-or-hepatitis-c-antibody-neg-reference-15)
    - [Hepatitis C Antibody Positive (Reference \#2)](#hepatitis-c-antibody-positive-reference-2)
    - [Legionella (Reference \#7)](#legionella-reference-7)
    - [Leishmaniasis (Reference \#14)](#leishmaniasis-reference-14)
    - [Malaria (Reference \#11)](#malaria-reference-11)
    - [Penicillin- Resistant Pneumococcus (Reference \#3)](#penicillin-resistant-pneumococcus-reference-3)
    - [Streptococcus-Group A (Reference \#6)](#streptococcus-group-a-reference-6)
    - [Tuberculosis (Reference \#5)](#tuberculosis-reference-5)
    - [Vancomycin-Resistant Enterococcus (VRE) (Reference \#1)](#vancomycin-resistant-enterococcus-vre-reference-1)
  - [Conclusion](#conclusion)
- [Editing/Printing Files, Screens, Linking Data, Request Form](#editingprinting-files-screens-linking-data-request-form)
  - [Editing TOPOGRAPHY file (#61)](#editing-topography-file-61)
  - [Printing LAB SEARCH/EXTRACT file (#69.5) Definitions](#printing-lab-searchextract-file-695-definitions)
  - [How to Link Antimicrobial Entries to Workload Codes Entries](#how-to-link-antimicrobial-entries-to-workload-codes-entries)
    - [Antimicrobial Link Update \[LREPILK\] options](#antimicrobial-link-update-lrepilk-options)
  - [Delete Entry from Laboratory Search/Extract](#delete-entry-from-laboratory-searchextract)
  - [Parameters Input Screen](#parameters-input-screen)
  - [How to add an entry to the Laboratory Search/Extract Parameters Input Screen](#how-to-add-an-entry-to-the-laboratory-searchextract-parameters-input-screen)
  - [Additional Workload and Suffixes Codes Request Form](#additional-workload-and-suffixes-codes-request-form)
  - [# Helpful Hints](#helpful-hints)
  - [Preferred Methods for Clostridium difficile Data Capture](#preferred-methods-for-clostridium-difficile-data-capture)
    - [Preferred Method \#1:](#preferred-method-1)
    - [Preferred Method \#2:](#preferred-method-2)
  - [Validating EPI Data Capture](#validating-epi-data-capture)
  - [Lab Search/Extract Protocol Edit \[LREPI PROTOCOL EDIT\] option](#lab-searchextract-protocol-edit-lrepi-protocol-edit-option)
  - [EPI Mail Groups](#epi-mail-groups)
    - [EPI mail group](#epi-mail-group)
    - [EPI-Report mail group](#epi-report-mail-group)
    - [Adding EPI Mail Groups](#adding-epi-mail-groups)
  - [Starting Lower Level Protocol for HL7 V. 1.6 Background Job](#starting-lower-level-protocol-for-hl7-v-16-background-job)
  - [EPI Data Cycle Process](#epi-data-cycle-process)
  - [EPI Data Transmission](#epi-data-transmission-1)
  - [HL7 Format Mailman Message](#hl7-format-mailman-message)
  - [EPI Confirmation Mailman Message](#epi-confirmation-mailman-message)
  - [Emerging Pathogens Verification Report Mailman Message](#emerging-pathogens-verification-report-mailman-message)
  - [Lab Search/Extract Manual Run (Enhanced)](#lab-searchextract-manual-run-enhanced)
  - [\[LREPI ENHANCED MANUAL RUN\] option](#lrepi-enhanced-manual-run-option)
  - [EPI Processing Report Mailman Message](#epi-processing-report-mailman-message)
  - [Table of Reject and Errors and/or Warning Codes](#table-of-reject-and-errors-andor-warning-codes)
- [VHA Directive 2000-019](#vha-directive-2000-019)
- [# Under Secretary For Health’s Information Letter](#under-secretary-for-healths-information-letter)
  - [IL 10-98-013](#il-10-98-013)
> The Veterans Health Information Systems and Architecture (VISTA) Laboratory Hepatitis C Extract and Emerging Pathogens Initiative (EPI) Technical and User Guide for patch LR\*5.2\*260 provides assistance for installing, implementing, and maintaining the patch LR\*5.2\*260.
> <span id="p421_v" class="anchor"></span>The ICD-10 Remediation patch LR\* 5.2\*421 makes the following changes to the Emerging Pathogens Initiative (EPI) application:
- The following fields and screens have been updated to refer to “ICD” rather than “ICD9”:
  - Laboratory Search/Extract Parameters Input screens
  - Enter/Edit Local Pathogens screens
  - Detailed Verification Report
  - Help text
- Within the Enter/Edit Local Pathogens and Laboratory Search/Extract Parameters Input screens, users are prompted to specify a code set on which to search prior to entering an ICD code. Based on this input, the system will only allow ICD-9 entry or ICD-10 entry.
- The Pathogen Inquiry option has been modified to list both ICD-9 and ICD-10 codes.
- The Generate Local Report/Spreadsheet option has been modified to include both the Diagnosis Code Set Designation and the Diagnosis Code.
- HL7 Reports that are sent to Austin Information Technology Center (AITC, formerly AAC) have been modified to include ICD-10 Codes and Descriptions, which are included in the DG1 HL7 Segments.
The ICD-10 PTF Modifications patch LR\*5.2\*442 made changes to accommodate the expanded number of ICD-10 codes that can now contained in a patient record. Routines LRAPQAT1, LREPI3, and LREPI5 were modified.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Veterans Health Administration (VHA) facility Information Resource Management (IRM) staff
- Laboratory Information Manager (LIM), Lab ADPACs, or experts in lab tests used by the Laboratory package
- Representative from the Microbiology section in support of the Emerging Pathogens Initiative (EPI) and the three new Hepatitis pathogens (i.e., director, supervisor, or technologist)
- Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) staff or person at the VHA facility with similar function

## Technical and User Guide Distributions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *VISTA* Laboratory Hepatitis C Extract and EPI Technical and User Guide for patch LR\*5.2\*260 is available in Portable Document Format (PDF) (i.e., LR_260TUG.PDF) at the following locations:

> Anonymous Software Accounts

- <span class="mark">REDACTED</span> <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>
- <span class="mark">REDACTED</span> <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>
- <span class="mark">REDACTED</span> <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

> V*IST*A Laboratory Home Page

> <span class="mark">REDACTED</span>

## Technical and User Guide Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Pre-Installation Information -* This section contains information that should be recognized prior to installation Patch LR\*5.2\*260 Hepatitis C Extract.

> *Installation Instructions -* This section provides information regarding the installation process for Patch LR\*5.2\*260 Hepatitis C Extract.

> *Post Installation Instruction -* This section provides all the necessary information required for the IRM and LIM personnel to implement the Laboratory Search/Extract software application.

> *EPI and Hepatitis Pathogens User Guide* - This user guide provides the necessary information for implementing and maintaining the EPI and Hepatitis pathogens search/extract criteria.

> *Appendix A -* This section provides instructions for editing/printing files, using input screens, linking data, and a Workload and Suffixes Codes Request Form.

> *Appendix B -* This section provides helpful hints and examples regarding for EPI and Hepatitis pathogens preferred methods, transmissions, and data validation suggestions.

> *Appendix C -* This section contain a copy of VHA DIRECTIVE 2000-019 for the Installation of Clinical Reminders 1.5 Software and Laboratory LR\*5.2\*260 Hepatitis C Extract patch.

## Screen Dialogue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Screen Captures -* The computer dialogue appears in courier font, no larger than 10 points. Example: Courier font 10 points

> *User Response -* User entry response appears in boldface type Courier font, no larger than 10 points. Example:Boldface type

> *Return Symbol -* User response to computer dialogue is followed by the \<RET\> symbol that appears in Courier font, no larger than 10 points, and bolded. Example: \<RET\>

> *Tab Symbol -* User response to computer dialogue is followed by the symbol that appears in Courier font, no larger than 10 points, and bolded. Example: \<Tab\>

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Review the following guides and manuals prior to installing and implementing the Laboratory Hepatitis C Extract patch LR\*5.2\*260.

- V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 Technical and User Guide
- Hepatitis C Extract Installation and Setup Guide for PXRM\*1.5\*1, LR\*5.2\*260, PSJ\*7\*5\*48, PSO\*7\*45
- Clinical Reminders V. 1.5 Installation Guide
- Clinical Reminders V. 1.5 Manager Manual
- Kernel V. 8.0 Systems Manual

Table of Contents

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Emerging Pathogens Initiative (EPI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Veterans Health Administration (VHA) Headquarters Infectious Disease Program Office Emerging Pathogens Initiative is to identify with new antibiotic-resistant and otherwise problematic pathogens within the Veterans Health Administration (VHA) facilities. Using this objective information, plans may be formulated on a national level for intervention strategies and resource needs. Results of aggregate data may also be shared with appropriate public health authorities for planning on the national level for the non-VA and private health care sectors.

> The VHA Headquarters Infectious Disease Program Office previously assisted with identifying the following 14 emerging pathogens for patient seeking care in a VHA facility and to report the data to the AITC database. This was accomplished by the V*IST*A Laboratory Emerging Pathogens Initiative (EPI) Patch LR\*5.2.132 and Laboratory Search/Extract patch LR\*5.2\*175 software:

> *CandidaLegionella*

> *Clostridiumdifficile* Leishmanaisis

> Creutzfeldt-Jakob Disease Malaria

> *Cryptosporidium* Pen- Res Pneumococcus

> Dengue *Streptococcus-*Group A

> *E. coli* O157:H7 Tuberculosis

> *Hepatitis C Antibody Pos Vanc-Res Enterococcus*

> The Under Secretary for Health (USH) published an information letter on standards for evaluation and testing for Hepatitis C Virus in June 1998 (IL-10-98-013-- Hepatitis C: Standard for Provider Evaluation and Testing at http://vaww.va.gov/publ/direc/health/infolet/109813.doc). The VHA policy outlines HCV background, infection, its growth as a national problem, transmission, and antibody development. The USH information letter directed that “all patients will be evaluated with respect to risk factors” for HCV. Clinicians are required to record this assessment in the patients’ medical records. Based on risk factors, antibody testing should be used according to an algorithm included in the policy letter. According to the VHA Chief Consultant for its Acute Care Strategic Health Care Group, the USH intends that each patient seeking care in a VHA facility will be screened for HCV risk factors. VISN officials were advised of this.

## Hepatitis C Assessment for Risk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The DVA Headquarters Infectious Disease Program Office is to support the tracking of assessment of risk for hepatitis C infection for patients seeking care in VHA facilities. This will be accomplished through the EPI. Further, 3 new emerging pathogen entities (Hepatitis A Antibody POS, Hepatitis B POS, Hepatitis C Antibody NEG), along with the already existing Hepatitis C Antibody POS will be added to EPI Lab Search/Extract activities to give a more comprehensive estimate of hepatitis overall in the VHA.

## Associated V*IST*A Software Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The V*IST*A Laboratory LR\*5.2\*260 Hepatitis C Extract, PXRM\*1.5\*1 Hepatitis C Extract, PSJ\*7\*48 Hepatitis C Extract, and PSO\*7\*45 Hepatitis C Extract patches were developed in a combined effort to support the tracking of assessment of risk for hepatitis C infection. This data, along with the three new Hepatitis pathogens data will automatically be provided without any additional individual data entry at the VHA facility level. Patch LR\*5.2\*260 searches, extracts, and processes the three new Hepatitis pathogens and the existing Hepatitis C Antibody POS defined data criteria from several V*IST*A databases. Laboratory Patch LR\*5.2\*260 automatically transmits the data to AITC for processing and coupling with denominator data related workload. The VAHQ Infectious Disease Program Office data retrieval and analysis can then be accomplished.

### V*IST*A BLOOD BANK SOFTWARE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The V*IST*A Laboratory LR\*5.2\*260 Hepatitis C Extract patch does not contain any changes to the V*IST*A Blood Bank Software as defined by VHA DIRECTIVE 99-053 titled V*IST*A BLOOD BANK SOFTWARE.

## Austin Information Technology Center Database Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Austin Information Technology Center (AITC) creates two file structures, both in Statistical Analysis System (SAS) file format. These two file structures are used as a source of data for the VHA Headquarters Infectious Disease Program Office. The data is available to the VHAQ Infectious Diseases Program Office to be used for analysis and reporting. The two file structures are referred to as the “Numerator Files” and “Denominator File” because of their planned utilization.

> Numerator Files:

> The Numerator files contain accumulation of data sent by all VHA facilities. The Numerator file information is specific to unique patients with a VHA Headquarters Infectious Diseases Program Office designated emerging pathogen. Emerging pathogen data entries are flagged through the V*IST*A Laboratory Search/Extract software process. Numerator files data are collected and transmitted to AITC monthly by VHA facilities.

> Denominator File:

> The Denominator file provides the VHA Headquarters Infectious Diseases Program Office total and unique counts of patients each VHA facility. The individual files that these data elements are extracted from are the National Patient Care (NPC), Inpatient Treatment File (PTF), VHA Work Measurement (VWM), and Cost Distribution Report (CDR) systems.

> The data elements are:

> \* Unique SSN served (inpatient and outpatient together)

> \* Total \# of discharges

> \* Total unique SSN discharges

> \* Inpatient hospital days

> \* Inpatient ICU days

> \* Unique SSN encounters for both inpatient and outpatient

> Unique and total counts are available for the individual months, current month, and previous eleven months for a year's set of totals, current month, and previous three month periods for a quarter's set of totals.

## EPI Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Emerging Pathogens (as defined by VAHQ) act as triggers for data acquisition for the LR\*5.2\*260 patch. The software then retrieves relevant, predetermined, and patient-specific data for transmission to the AITC database repository. Once at that location, the data are analyzed using Statistical Analysis System (SAS)-based statistical software. VAHQ Reports may then be generated for appropriate use and distribution at the national level.

> With the installation of the new LR\*5.2\*260 patch, automated data transmissions will occur. Receipt of this transmission at the AITC queue will trigger a confirmation message back to the originating site to “confirm” that data has been sent. Then at the next processing cycle (25<sup>th</sup> of the month), a processing/error report will also be generated and sent back to the originating site. This processing/error report will serve as the ultimate “confirmation” that data has been accepted. If there is a fatal error in any segment of the message, the entire message will be rejected and must be resent manually. Warning codes/errors are accepted into the data set, but serve to remind the originating site that a correction of the process generating the error may be needed.

> NOTE: The daily NCH data transmissions are no longer necessary and the NCHP program office has requested that we terminate the transmissions. This will be done during the post-init phase and does not require any user intervention.

## AITC Transmission Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EPI Confirmation Mailman Message

> An EPI Confirmation mailman message is sent from the AITC, upon receipt of the VHA facilities EPI monthly transmission via the EPI-REPORT mail group. The EPI-REPORT mail group members are notified that the original EPI and Hepatitis pathogens HL7 format mailman message data transmission has been received by AITC for processing.

> NOTE: This EPI Confirmation mailman message ONLY means that the sending VHA facility data transmission has been received by the AITC for processing.

> EPI Processing Report Mailman Message

> The EPI Processing Report mailman message itemizes all transmissions received by AITC, document the records status as either being accepted or rejected (with the reason code identified). Examples of the “Tables of Rejects and Errors and/or Warning Codes” are located in the Appendix - B section of this guide.

## # Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The V*IST*A Laboratory Hepatitis C Extract patch LR\*5.2\*260 is an enhancement to the Laboratory Emerging Pathogens Initiative (EPI) patch LR\*5.2\*132 and Laboratory Search/Extract Patch LR\*5.2\*175 software application. The enhancements support the tracking of assessment for risk for Hepatitis C infection and three new Hepatitis pathogens entities (i.e., Hepatitis A Antibody POS, Hepatitis B POS, Hepatitis C Antibody NEG).

> NOTE: The daily NCH data transmissions are no longer necessary. The National Center for Health Promotion (NCHP) program office has requested that we terminate the transmissions. The NCH CHOLESTEROL and NCH PAP SMEAR entries will be inactivated in the LAB SEARCH/EXTRACT file (#69.5). This is done during the post-init phase and does not require any user intervention.

> 1\. Patch LR\*5.2\*260 automatically extracts information about the three new emerging pathogens entities (Hepatitis A Antibody POS, Hepatitis B POS, Hepatitis C Antibody NEG). This is done <u>without</u> the necessity of any manual data entry once the Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option parameter descriptions has been set up for the three new Hepatitis pathogens.

> 2\. Patch LR\*5.2\*260 automatically searches, extracts, and processes EPI and the three new Hepatitis pathogens data along with information about assessment of risk for infection with Hepatitis C, pharmacy-based information and other laboratory-based information, from the following V*IST*A software applications, files, and routines:

|                                   |                                                                       |
|-----------------------------------|-----------------------------------------------------------------------|
| V*IST*A Software Applications | V*IST*A Files and Routines                                        |
| Laboratory Version 5.2            | LAB DATA file (#63) (i.e., containing verified lab test data results) |
| PIMS Version 5.3                  | PATIENT file (#2) and PTF file (#45)                                  |
| Social Work Version 3.0           | Routine - \$\$ HOMELESS^SOWKHIRM                                      |
| Clinical Reminders Version 1.5    | Routine - D PATS^PXRMXX                                               |

> 3\. Patch LR\*5.2\*260 exports the new LREPI REMINDER LINK file (#69.51). This new file points to the Clinical Reminders V. 1.5 software application, REMINDER DEFINITION file (#811.9), NAME field (#.01) data entries (i.e., VA-NATIONAL EPI LAB EXTRACT, VA-NATIONAL EPI RX EXTRACT, VA-HEP C RISK ASSESSMENT) used by the three new Hepatitis A Antibody POS, Hepatitis B POS, Hepatitis C Antibody NEG and the existing Hepatitis C Antibody POS pathogens. Entries in the new LREPI REMINDER LINK file (#69.51) are used to determine which Clinical Reminders data.

|                                                                                           |                   |                                                              |
|-------------------------------------------------------------------------------------------|-------------------|--------------------------------------------------------------|
| New LREPI REMINDER LINK file (#69.51) points to the following file and field entries: |                   |                                                              |
| REMINDER DEFINITION file (#811.9)                                                         | NAME field (#.01) | Clinical Reminders data entries used for Hepatitis pathogens |
|                                                                                           |                   | VA-NATIONAL EPI LAB EXTRACT                                  |
|                                                                                           |                   | VA-NATIONAL EPI RX EXTRACT                                   |
|                                                                                           |                   | VA-HEP C RISK ASSESSMENT                                     |

> 4\. Patch LR\*5.2\*260 automatically exports data entries to seven fields of the LAB SEARCH/EXTRACT file (#69.5), for the three new Hepatitis A Antibody POS, Hepatitis B POS, and Hepatitis C Antibody NEG pathogens ONLY. The following chart list the seven fields and data entries that are automatically exported by this patch:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>LAB SEARCH/EXTRACT file (#69.5), fields automatically being exported with data:</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Data Entries</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NAME field (#.01)</p>
</blockquote></td>
<td><blockquote>
<p>Hepatitis A Antibody POS, Hepatitis B POS, and Hepatitis C Antibody NEG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>REFERENCE NUMBER field</p>
<p>(#69.5, .05)</p>
</blockquote></td>
<td><blockquote>
<p>Hepatitis A Antibody POS-<strong>Ref #16</strong>, Hepatitis B POS-<strong>Ref #17</strong>, and Hepatitis C Antibody NEG-<strong>Ref #15</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ACTIVE field (#69.5, 1)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CYCLE field (69.5, 10)</p>
</blockquote></td>
<td><blockquote>
<p>Monthly</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LAG DAYS field (#69.5, 10.5)</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PROTOCOL field (#69.5, 12)</p>
</blockquote></td>
<td><blockquote>
<p>LREPI</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Follow PTF field (#69.5, 13)</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 5\. Patch LR\*5.2\*260 automatically exports the three new Hepatitis pathogen entries in LAB SEARCH/EXTRACT file (#69.5), LAB TEST field (#2).

> The table below lists the three new Hepatitis pathogens the and existing Hepatitis C Antibody POS emerging pathogen and the Lab Search/Extract parameter setup entries. The LAB SEARCH/EXTRACT parameter (second column) is an example as other sites may have different names for tests. Also the second column does not use the indicator mechanism of whether the result CONTAINS the POS or is EQUAL TO the POS, etc)

> Example:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>LAB SEARCH/EXTRACT file (#69.5) Hepatitis pathogens entries</td>
<td>LAB SEARCH/EXTRACT parameter setup required lab tests for each Hepatitis pathogens</td>
</tr>
<tr class="even">
<td>Hepatitis A Antibody NEG</td>
<td><p>HEP A ANTIBODY-TOTAL REACTIVE</p>
<p>HEP A ANTIBODY(IgM) POS</p>
<p>HEPATITIS A AB(IGG)D/C(2/99) POS</p>
<p>HEPATITIS A AB(IGG)D/C(2/99) Pos</p>
<p>HEPATITIS A AB(IGG)D/C(2/99) P</p>
<p>HEPATITIS A AB(IGG)D/C(2/99) p</p>
<p>HEP A ANTIBODY-TOTAL R</p></td>
</tr>
<tr class="odd">
<td>Hepatitis B Antibody NEG</td>
<td><p>HEP B SURFACE Ag POS</p>
<p>HEP B SURFACE AB POS</p>
<p>HEP B CORE AB(IgM) POS</p>
<p>HEP Be ANTIGEN POS</p>
<p>HEP Be ANTIGEN Pos</p>
<p>HEP Be ANTIGEN p</p>
<p>HEP Be ANTIGEN P</p></td>
</tr>
<tr class="even">
<td>Hepatitis C Antibody NEG</td>
<td><p>HEP C ANTIBODY NEG</p>
<p>HEP C ANTIBODY SEE COMMENTS</p>
<p>HEP C ANTIBODY <strong>*</strong></p>
<p>HEP C ANTIBODY <strong>#</strong></p></td>
</tr>
<tr class="odd">
<td>Hepatitis C Antibody POS</td>
<td>Hepatitis C Antibody POS</td>
</tr>
</tbody>
</table>

> NOTE: LAB SEARCH/EXTRACT file (#69.5) contains the previous EPI pathogens and the three new Hepatitis pathogens defined search and extract criteria. This file should ONLY be edited using the Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option.

> 6\. Patch LR\*5.2\*260 automatically searches, extracts, and processes all previous and newly EPI-defined data within the VHA facility on the 15<sup>th</sup> of each month.

> 7\. The new Patch LR\*5.2\*260 has been enhanced to automatically transmit EPI-related data to the AITC via HL7 format mailman messages each time the option is run. This will occur from either automated runs of data or manual runs of the data {Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\]}.

> NOTES:

> Transmissions to AITC after 6:00 pm are processed the next day.

> Please DO NOT run the Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option to transmit EPI and Hepatitis pathogens data on Wednesdays of PAY ROLL weeks. These transmissions may cause a delay in processing the PAY ROLL data.

> 8\. Patch LR\*5.2\*260 automatically adds two new segments to the HL7 transmissions. The new segments are:

> ABBREVIATED NAME: ZXE - FULL NAME: Pharmacy Prescription Order.

> This segment will report Pharmacy data consisting of the Drug Name, NDC, and Days Supply.

> ABBREVIATED NAME: DSP - FULL NAME: Display Data

> This segment will report Clinical Reminders Hepatitis C Risk Assessment Data, along with associated laboratory tests and results of SGOT, SGPT and bilirubin.

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## IRM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An IRM staff is required for reviewing mail groups and menu assignments.

## Laboratory Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is highly recommended that the following person (s) <u>jointly</u> participate in reviewing the parameter descriptions:

- Laboratory Information Manager (LIM)
- Representative from the Microbiology section for the Emerging Pathogens Initiative (i.e., director, supervisor, or technologist)
- Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) staff (or person at the facility with similar function)

## Hardware and Operating System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> V*IST*A software operates on two hardware platforms. The hardware platforms are listed in the mini-computer category, which provides <u>multi-tasking</u> and <u>multi-user</u> capabilities. The hardware platforms systems used are:

### Digital Equipment Corporation (DEC) Alpha Series

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Digital Equipment Corporation (DEC) Alpha series is using the DEC Open Virtual Memory System (VMS), Version 6.1 or greater, operating system. This platform uses the DEC System Mumps (DSM), Version 6.3 or greater, of American National Standards Institutes (ANSI) of Massachusetts General Hospital Utility Multi-Programming System (MUMPS) also known as ‘M’ language. MUMPS is a Federal Information Processing Standard (FIPS) language.

### Personal Computer (PC) System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Personal Computer (PC) System with 486 or Pentium computer processor chip is using the Microsoft Disk Operating System (MS-DOS). The platform uses Open-M, of the American National Standards Institutes (ANSI) of Massachusetts General Hospital Utility Multi-Programming System (MUMPS) also known as 'M' language. MUMPS is a Federal Information Processing Standard (FIPS) language.

## System Performance Capacity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> LR\*5.2\*260 is an informational patch. There are no changes in the performance of the system.

## Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installation time is less than 2 minutes during off peak hours and less than 5 minutes during peak hours.

## Users on the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users may remain on system and no options need to be placed out of service.

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Laboratory LR\*5.2\*260 Hepatitis C Extract patch namespace is Laboratory’s LR.

## Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new DBIA was approved for VistA Laboratory ICD-10 PTF Modifications patch LR\*5.2\*442:

- DBIA \#6130

> The following DBIAs were approved for Laboratory LR\*5.2\*260 Hepatitis C Extract patch:

> Reference to ^PSDRUG supported by IA \#221-A

> Reference to ^DGPT supported by IA \#418

> Reference to ^ORD supported by IA \#872

> Reference to ^DD supported by IA \#999

> Reference to ^ICD9 supported by IA \#10082

> Reference to ^XLFSTR supported by IA \#10104

> Reference to ^PXD(811.9 supported by IA \#1256

> Reference to ^FIDATA^PXRM supported by IA \#3134

> Reference to ^PATS^PXRMXX supported by IA \#3134

> Reference to ^DIC(21 supported by IA \#2504

## V*IST*A Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following software applications are must be installed prior to the installation of Laboratory Hepatitis C Extract patch LR\*5.2\*260:

> Software Applications Versions (or Greater)

> VA FileMan 21 (with patches installed)

> Kernel 8.0 (with patches installed)

> Laboratory 5.2 (with patches installed)

> PIMS 5.3 (with patches installed)

> HL7 1.6 (with patches installed)

> Social Work 3.0 (with patches installed)

> MailMan 7.1 (with patches installed)

> Clinical Reminders 1.5 (with patches installed)

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Prior to the installation of Laboratory Hepatitis C Extract patch LR\*5.2\*260, the following patches MUST be installed:

> Software Applications Patches

> Laboratory V. 5.2 LR\*5.2\*175

> LR\*5.2\*242

> Clinical Reminders V. 1.5 (u) PXRM\*1.5\*1

<span id="_Toc425208766" class="anchor"></span>

> In addition, prior to installation of patch LR\*5.2\*421, the following patches must be installed:

> Software Applications Patches

> Laboratory V. 5.2 LR\*5.2\*315

> LR\*5.2\*422

> LR\*5.2\*429

> Lexicon Utility LEX\*2\*80

> Global Coding System ICD\*18\*57

> **NOTE:** For patches required for LR\*5.2\*442, please refer to the ICD-10 PTF Modifications Installation Guide: <http://www.va.gov/vdl/application.asp?appid=118>

## Health Level Seven (HL7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Laboratory Hepatitis C Extract patch LR\*5.2\*260 uses the V*IST*A HL7 V. 1.6 software application to transmit EPI data to the AITC, formerly AAC.

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> LREPI: This event driver protocol defines the associated parameters required for building HL7 messages that are used to transmit EPI data to the AITC, formerly AAC.

> LREPI CLIENT: This subscriber protocol defines the parameter required by the HL7 application that determines where to send the HL7 formatted message containing the emerging pathogens data.

## ## Domain

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Q-EPI-MED.GOV domain is used for transmitting EPI data to AITC.

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EPImail group - is used by the VHA facilities to transmit EPI HL7 format mailman messages to AITC and for AITC to transmit EPI Confirmation mailman messages back to the sending VHA facilities once the EPI HL7 format mailman messages data transmission has been received by AITC.

> EPI-Reportmail group – is used to receive the Emerging Pathogens Verification Report and the EPI Processing Report mailman messages sent from AITC. The members of this mail group will assist in the EPI data validation and corrections process.

## Backup Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is <u>highly</u> recommended that a backup of the transport global be performed before installing Patch LR\*5.2\*260.

## Routine List

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

## LAB SEARCH/EXTRACT file (#69.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The LAB SEARCH/EXTRACT file (#69.5), LAB TEST field (#2) was edited to add the three new, “Hepatitis A Antibody POS”, “Hepatitis B POS”, and “Hepatitis C Antibody NEG”) pathogens. This file contains search criteria used by the

Laboratory Search/Exact software. This file should ONLY be edited using the Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option.

## ## New LREPI REMINDER LINK file (#69.51)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The new LREPI REMINDER LINK file (#69.51) points to the Clinical Reminders V. 1.5 software application, REMINDER DEFINITION file (#811.9), NAME field (#.01) data entries (i.e., VA-NATIONAL EPI LAB EXTRACT, VA-NATIONAL EPI RX EXTRACT, and VA-HEP C RISK ASSESSMENT) used by the three new Hepatitis A Antibody POS, Hepatitis B POS, Hepatitis C Antibody NEG, and the existing Hepatitis C Antibody POS pathogens. Entries in the new LREPI REMINDER LINK file (#69.51) is used to determine which Clinical Reminders data entries are used to generate data for the Hepatitis emerging pathogens.

> Example:

> STANDARD DATA DICTIONARY \#69.51 -- LREPI REMINDER LINK FILE 07/20/00 PAGE 1

> STORED IN ^LAB(69.51, (3 ENTRIES) SITE: Dallas ISC - Development Account UCI: VAH,DEV

> DATA NAME GLOBAL DATA

> ELEMENT TITLE LOCATION TYPE

> -----------------------------------------------------------------------------

> This file holds a pointer to the REMINDER DEFINITION (#811.9) file for use by the Emerging Pathogens Initiative (EPI). The entries in this file are used to determine which Clinical Reminders will be used to generate data for the Hepatitis C registry.

> DD ACCESS: @

> RD ACCESS:

> WR ACCESS: \#

> DEL ACCESS: \#

> LAYGO ACCESS: \#

> AUDIT ACCESS:

> CROSS

> REFERENCED BY: REMINDER(B)

> CREATED ON: JUN 2,2000 by LABUSER, ONE

> 69.51,.01 REMINDER 0;1 POINTER TO REMINDER DEFINITION FILE

> (# 811.9) (Required)

> POINTER TO CLINICAL REMINDER

> LAST EDITED: JUN 02, 2000

> HELP-PROMPT: Select an entry from the REMINDER DEFINITION

> (#811.9) file.

> DESCRIPTION: This field holds a pointer to the REMINDER

> DEFINITION (#811.9) file. These entries will

> be used to determine which Clinical Reminders

> will be used to generate data for the

> Hepatitis C registry.

> CROSS-REFERENCE: 69.51^B

> 1)= S ^LAB(69.51,"B",\$E(X,1,30),DA)=""

> 2)= K ^LAB(69.51,"B",\$E(X,1,30),DA)

> FILES POINTED TO FIELDS

> REMINDER DEFINITION (#811.9) REMINDER (#.01)

> INPUT TEMPLATE(S):

> PRINT TEMPLATE(S):

> SORT TEMPLATE(S):

> FORM(S)/BLOCK(S):

## Routine Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example:

> ROUTINE SUMMARY

> ===============

The following routines are distributed and installed with Clinical

Reminders patch PXRM\*1.5\*1.

The second line of each routine now looks like:

\<tab\>;;5.2;LAB SERVICE;\*\*\[patch list\]\*\*;;Sep 27, 1994

CHECK^XTSUMBLD Results

Routine Name Before Patch After Patch Patch List

------------ ------------ ----------- ----------

LR260 NEW 10238627 260

LREPI 11741568 14217525 132,175,260

LREPI1 10215540 10654552 132,157,175,260

LREPI1A 5536163 5834647 175,260

LREPI2 5729687 7199135 132,157,175,242,260

LREPI3 3617464 5462995 132,175,260

LREPI4 1715994 1903453 132,175,260

LREPIAK 2866307 3640656 175,260

LREPIPH NEW 5818757 260

LREPIRP 6008472 5973015 132,157,175,260

LREPISRV NEW 12552990 260

## Installation Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Laboratory Hepatitis C Extract patch LR\*5.2\*260 is an informational patch only. The routines referenced in this patch are distributed and installed with Clinical Reminders V. 1.5 patch PXRM\*1.5\*1.

> NOTE: See the Hepatitis C Extract Installation and Setup Guide the for an example of the combined installation process for PXRM\*1.5\*1 Hepatitis C Extract, LR\*5.2\*260 Hepatitis C Extract, PSO\*7\*45 Hepatitis C Extract, PSJ\*7\*5\*48 patches.

> NOTE: The daily NCH data transmissions are no longer necessary. The National Center for Health Promotion (NCHP) program office has requested that we terminate the transmissions. The NCH CHOLESTEROL and NCH PAP SMEAR entries will be inactivated in the LAB SEARCH/EXTRACT file (#69.5). This is done during the post-init phase and does not require any user intervention.

# Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: There are no post installation instructions for LR\*5.2\*442.

> The post installation instructions should be followed as recommended. This will ensure a successful implementation of the software.

## IRM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Step 1. DSM/Alpha and Open M Sites may now re-enable journaling. If using a mapped system, rebuild the map set now.

> Step 2. Verify that the Lower Level Protocol of the HL7 V. 1.6 background job for EPI is running.

> Select Systems Manager Menu Option: HL7 Main\<RET\> Menu

> 1 V1.5 OPTIONS ...

> 2 V1.6 OPTIONS ...

> 3 Activate/Inactivate Application

> 4 Print/Display Menu ...

> 5 Purge Message Text File Entries

> Select HL7 Main Menu Option: 2\<RET\> V1.6 OPTIONS

> 1 Communications Server ...

> 2 Interface Workbench

> 3 Message Requeuer

> Select V1.6 OPTIONS Option: 1\<RET\> Communications Server

> 1 Edit Communication Server parameters

> 2 Manage incoming & outgoing filers ...

> 3 Monitor incoming & outgoing filers

> 4 Start LLP

> 5 Stop LLP

> 6 Systems Link Monitor

> 7 Logical Link Queue Management ...

> 8 Report

> Select Communications Server Option: 4\<RET\> Start LLP

> This option is used to launch the lower level protocol for the appropriate device. Please select the node with which you want to communicate

> Select HL LOGICAL LINK NODE: EPI-LAB\<RET\>

> The LLP was last shutdown on JAN 30, 1997 12:06:19.

> Select one of the following:

> F FOREGROUND

> B BACKGROUND

> Q QUIT

> Method for running the receiver: B//\<RET\> ACKGROUND

> Job was queued as 131225.

> Step 3. Verify that the Lab Search/Extract Primary Menu \[LREPI SEARCH EXTRACT MENU\] is assigned to designate users.

> NOTE: It is highly recommended that the Laboratory Information Manager (LIM), a representative from the Microbiology section (director, supervisor, or technologist) and a Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) staff (or person at the facility with similar function) be assigned the Lab Search/Extract Primary Menu \[LREPI SEARCH EXTRACT MENU\]. These will be the individual(s) responsible for initially setting the Lab Search/Extract parameters descriptions and doing periodic reviews of the parameters descriptions to assure they are current.

> NOTE: Any change in the EPI Lab Search/Extract parameter set-up for the four hepatitis pathogens (Hepatitis A Antibody POS, Hepatitis B POS, Hepatitis C Antibody NEG, or Hepatitis C Antibody POS) must have a corresponding change in the Clinical Reminders VA-National EPI Lab Extract Reminders logic.

> Step 4. Verify that the Lab Search/Extract Nightly Task \[LREPI NIGHTLY TASK\] option is schedule to run each night. This option will build HL7 messages and send them to the defined locations specified by the LREPI protocol.

> Step 5. PLEASE DO NOT PERFORM THIS STEP UNTIL SPECIFICALLY REQUESTED TO DO SO BY THE VHA CIO HEP-C IMPLEMENTATION TEAM. After the Hepatitis Extract Reminder definitions and Lab Search/Extract parameter description setups for the three new Hepatitis pathogens have been completed by the LIM staff or designate user. EPI and Hepatitis pathogens data for your VHA facility will be REVIEWED by the VHA CIO HEP-C IMPLEMENTATION TEAM. At this time you will be asked to add XXX@Q-EPI.MED.VA.GOV to the MEMBERS – REMOTE field (#12) of the MAIL GROUP file (#3.8) for the EPI mail group.

> Example:

Select VA FileMan 22.0

Select OPTION: 1\<RET\>ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: MAIL GROUP//\<RET\>

EDIT WHICH FIELD: ALL// MEMBERS - REMOTE (multiple)

EDIT WHICH MEMBERS - REMOTE SUB-FIELD: ALL//\<RET\>

THEN EDIT FIELD:\<RET\>

Select MAIL GROUP NAME: EPI\<RET\>

1 EPI

2 EPI-REPORT

CHOOSE 1-2: 1 EPI\<RET\>

Select REMOTE MEMBER: S.HL V16 SERVER@DEV// XXX@Q-EPI.MED.VA.GOV\<RET\>

Are you adding 'XXX@Q-EPI.MED.VA.GOV' as a new REMOTE MEMBER (the

2ND for this MAIL GROUP)? No// Y\<RET\>(Yes)

## LIM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: It is highly recommended that the Laboratory Information Manager (LIM), a representative from the Microbiology section (director, supervisor, or technologist) and a Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) staff (or person at the facility with similar function) be assigned the Lab Search/Extract Primary Menu \[LREPI SEARCH EXTRACT MENU\]. These will be the individual(s) responsible for initially setting the Lab Search/Extract parameters descriptions and doing periodic reviews of the parameters descriptions to assure they are current.

> Step 1. Review the three new Hepatitis A Antibody POS, Hepatitis B POS, and Hepatitis C Antibody NEG pathogens descriptions and input screens examples prior to setting up the Lab Search/Extract parameters. *(Descriptions and input screens examples are contained in the EPI and Hepatitis Pathogens User Guide section of this guide).*

> Step 2. Use the Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option to setup the three new Hepatitis A Antibody POS, Hepatitis B POS, and Hepatitis C Antibody NEG pathogens parameter descriptions (i.e., as specified by the VAHQ Infectious Disease Program Office). *(See the EPI and Hepatitis Pathogens User Guide section in this guide for examples on setting up the parameters).*

> NOTE: Take this opportunity to review the already existing Hepatitis C POS parameter set-up to assure that it is up-to-date and correct. Again, if there is any changes in any of the four hepatitis pathogens in the Lab Search/Extract parameter set up a concomitant change in the findings must occur in the Clinical Reminders.

> NOTE: LAG DAYS must be set at 15 for all EPI-defined pathogens, including three new Hepatitis pathogens.

> Step 3. Upon receipt of the VHA facilities EPI and Hepatitis pathogens HL7 format mailman message monthly transmission to AITC, individual EPI Confirmation mailman messages are sent by AITC to the sending VHA facilities EPI mail group. Members of this mail group are being notified that EPI and Hepatitis pathogens HL7 format mailman message data transmission has been received by AITC for processing. *(See the EPI and Hepatitis Pathogens User Guide Appendix-B section of this guide for examples of the EPI Confirmation mailman messages).*

> NOTE: EPI Confirmation mailman messages ONLY means that the sending VHA facility data transmission has been received by AITC for processing.

> Step 4. EPI-REPORT mail group members will receive an Emerging Pathogens Verification Report mailman message (i.e., in a human readable format) on the 15<sup>th</sup> of each month. The report should assist in validating the accuracy of the EPI data transmission to AITC. *(See the EPI and Hepatitis Pathogens User Guide Appendix-B section of this guide for examples of the Verification Reportmailman messages).*

> Step 5. After validating the Emerging Pathogens Verification Report mailman message for accuracy, make data corrections as deemed necessary to the associated V*IST*A software applications data fields entries (e.g., complete social security numbers, valid Date of Births, Period of Services, etc.).

> Step 6. Use the Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option to generate and automatically transmit EPI corrections to the AITC via HL7 format mailman messages. This option may be manually initiated as often as necessary. EPI and the three new Hepatitis pathogens data transmissions to AITC will occur each time the option is run. *(See the EPI and Hepatitis Pathogens User Guide Appendix-B section of this guide for an example on how to run the option).*

> NOTE:EPI and EPI-REPORT mail members should be advised to expect a significant increase in the amount of data acquired with the new version of EPI Laboratory Search/Extract coming across in the HL7 mailman messages and Verification Report.

> NOTE: Please DO NOT transmits EPI and Hepatitis pathogens data on Wednesdays of PAY ROLL weeks. These transmissions may cause a delay in processing PAY ROLL data.

> Step 7. EPI-REPORT mail group members will receive an EPI Processing Report mailman message at the end of AITC processing cycle (i.e., the 25<sup>th</sup> of each month). The EPI Processing Report mailman message confirms that EPI and Hepatitis emerging pathogens data has been processed and lists any errors and/or warning codes requiring corrections. The EPI Processing Report mailman message will ultimately determine whether EPI and Hepatitis pathogens data has been accepted by the AITC to be processed and placed into the EPI Statistical Analysis System (SAS) files. *(See the EPI and Hepatitis Pathogens User Guide Appendix-B section of this guide for the EPI Processing Report mailman message example).*

> Step 8. Review the Table of Reject of Errors and/or Warning Codes definitions and make corrections as needed. (*See the EPI and Hepatitis Pathogens User Guide Appendix-B section of this guidefor examples)*.

> NOTE: Use the Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option to manually transmit the EPI and Hepatitis pathogens data corrections to the AITC. (*See the EPI and Hepatitis Pathogens User Guide Appendix-B section of this guidefor examples)*.

> <span id="p421_25" class="anchor"></span>NOTE: For patch LR\*5.2\*421 installation instructions, please refer to the ICD-10 Release Notes for LR\*5.2\*421.

## NOTE: For patch LR\*5.2\*442 installation instructions, please refer to the ICD-10 PTF Modifications Installation Guide: <http://www.va.gov/vdl/application.asp?appid=118>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Health Level Seven (HL7) Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The V*IST*A Laboratory Hepatitis C Extract patch LR\*5.2\*260 uses Laboratory, PIMS, Pharmacy, Clinical Reminders, and Social Work databases for the EPI and Hepatitis C search/extract criteria. The V*IST*A HL7 software is used to transmit the EPI and Hepatitis C data to the AITC database.

## General Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *3.1 Communication Protocol*

> The electronic V*IST*A MailMan software application is used as the communications protocol for sending the EPI HL7 mailman messages between V*IST*A database and AITC database.

> *3.2 Application Processing Rules*

> The HL7 protocol itself describes the basic rules for application processing by the sending and receiving systems. The HL7 Version 2.2 protocol is used. The Observational Results Unsolicited (ORU) message is sent using the HL7 batch protocol.

> *3.3 Message*

> The following HL7 mail message is used to support the exchange of data:

> ORU Observational Results Unsolicited

> *3.4 Segments*

> The following HL7 segments are used to support the exchange of data:

> DG1 Diagnosis OBX Observation Results

> DSP Display Data PID Patient Identification

> MSH Message Header PV1 Patient Visit

> NTE Notes and Comments ZXE Pharmacy Prescription Order

> OBR Observation Request

> <span id="p421_26" class="anchor"></span>Patch LR\*5.2\*421 updates the DG1 segment of HL7 messages to the AITC to include an ICD-9 or ICD-10 code set indicator.

> Example:

> DG1\|1\|\|A90.~DENGUE FEVER \[CLASSICAL DENGUE\]~I10\|20121023183419-0400\|\|PR

> DG1\|2\|\|A91.~DENGUE HEMORRHAGIC FEVER~I10\|20121023183419-0400\|\|

> DG1\|3\|\|A93.8~OTHER SPECIFIED ARTHROPOD-BORNE VIRAL FEVERS~I10\|20121023183419-0400\|\|

> *3.5 Fields*

> The following HL7 fields are used to support the exchange of data for each of the segments listed in the 3.4 Segments:

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 37%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td><strong>FIELD</strong></td>
<td><strong>Data</strong></td>
<td></td>
<td></td>
<td><strong>Used</strong></td>
</tr>
<tr class="even">
<td><strong>SEGMENT</strong></td>
<td><strong>SEQUENCE</strong></td>
<td><p><strong>Type/</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>FIELD ELEMENT NAME</strong></td>
<td><strong>USER/HL7</strong></td>
<td><strong>By</strong></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>NUMBER</strong></td>
<td><strong>HL/7</strong></td>
<td></td>
<td><strong>DEFINED</strong></td>
<td><strong>See Note #1</strong></td>
</tr>
<tr class="even">
<td><strong>DG1</strong></td>
<td>1</td>
<td>4/SI</td>
<td>Set ID-Diagnosis (Sequence #)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>60/CE</td>
<td>Diagnosis Code (Code(id) ^Text (St.) ^ Name of coding system (st)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>19/TS</td>
<td>Admission Date</td>
<td>HL7</td>
<td>EPI</td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td>2/IS</td>
<td>Diagnosis Type (PR=DXLS)</td>
<td>HL7</td>
<td>EPI</td>
</tr>
<tr class="even">
<td><strong>MSH</strong></td>
<td>1</td>
<td>1/ST</td>
<td>Field Separator</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>4/ST</td>
<td>Encoding Characters</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>180/HD</td>
<td>Sending Application</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>180/HD</td>
<td>Sending Facility</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>180/HD</td>
<td>Receiving Application</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td>180/HD</td>
<td>Receiving Facility</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>19/TS</td>
<td>Date/Time of Message</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td>40/SY</td>
<td>Security</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>7/CM</td>
<td>Message Type</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>20/ST</td>
<td>Message Control ID</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>11</td>
<td>3/PT</td>
<td>Processing ID</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td>8/ID</td>
<td>Version ID</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td><strong>OBR</strong></td>
<td>1</td>
<td>4/SI</td>
<td>Set ID-Observation Request (Seq #)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>200/CE</td>
<td>Universal Service ID (identifier ~ text ~ name of coding system ~ alt id ~ alt text ~ alt coding system)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>19/TS</td>
<td>Observation Date/Time</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>15</td>
<td>300/CM</td>
<td>Specimen Source (Specimen source code (CE) ~~ text (TX) )</td>
<td>HL7 (Table 0070)</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>26</td>
<td>400/CM</td>
<td>Parent Results (OBX observation id of parent ^OBX sub ID</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td><strong>NTE</strong></td>
<td>1</td>
<td>4/SI</td>
<td>Set ID (seq. #)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>64K/FT</td>
<td>Comment (Four formats exist for this segment, see Note #2)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td><strong>OBX</strong></td>
<td>1</td>
<td>4/SI</td>
<td>Set Id-Observational Simple (seq. #)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>2/ID</td>
<td>Value Type</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>80/CE</td>
<td>Observation Identifier (identifier ~ text ~ name of coding system ~ alt id ~ alt text ^ alt coding system)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 37%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td><strong>FIELD</strong></td>
<td><strong>Data</strong></td>
<td></td>
<td></td>
<td><strong>Used</strong></td>
</tr>
<tr class="even">
<td><strong>SEGMENT</strong></td>
<td><strong>SEQUENCE</strong></td>
<td><p><strong>Type/</strong></p>
<p><strong>Length</strong></p></td>
<td><strong>FIELD ELEMENT NAME</strong></td>
<td><strong>USER/HL7</strong></td>
<td><strong>By</strong></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>NUMBER</strong></td>
<td><strong>HL/7</strong></td>
<td></td>
<td><strong>DEFINED</strong></td>
<td><strong>See Note #1</strong></td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>20/ST</td>
<td>Sub Id</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td></td>
<td>Observation Value (Result)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>6</td>
<td>60/CE</td>
<td>Units (Units)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td>10/ID</td>
<td>Abnormal Flags</td>
<td>HL7 (Table 0078)</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>14</td>
<td>60/CE</td>
<td><p>Date/Time of the Observation</p>
<p>(Verified Date/Time)</p></td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td>PID</td>
<td>1</td>
<td>4/SI</td>
<td>Set ID – Patient ID</td>
<td>Hl7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>16/CK</td>
<td>Patient ID (External ID)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>20/CM</td>
<td>Patient ID (Internal ID)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>48/PN</td>
<td>Patient Name</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td>19/TS</td>
<td>Date of Birth</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>8</td>
<td>1/ID</td>
<td>Sex</td>
<td>HL7 (Table 0001)</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>1/ID</td>
<td>Race</td>
<td>HL7 (Table VA07)</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>11</td>
<td>106/AD</td>
<td><p>Address (Homeless{where</p>
<p>applicable}~Zip Code)</p></td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>19</td>
<td>16/ST</td>
<td>SSN</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>27</td>
<td>60/CE</td>
<td>Veteran’s Military Status</td>
<td>HL7 (Table Va011)</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td><strong>PV1</strong></td>
<td>1</td>
<td>4/SI</td>
<td>Set ID - Patient Visit</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>1/ID</td>
<td>Patient Class (I=Inpatient,O=Outpatient)</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>36</td>
<td>3/ID</td>
<td><p>Discharge Disposition (Type</p>
<p>of Disposition {Code}~Type</p>
<p>of Disposition {Text}~Source</p>
<p>ID {VA45=VA File 45})</p></td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td></td>
<td>44</td>
<td>19/TS</td>
<td><p>Admit Date/Time (Event</p>
<p>Date/Time)</p></td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="odd">
<td></td>
<td>45</td>
<td>19/TS</td>
<td>Discharge Date/Time</td>
<td>HL7</td>
<td>EPI/NCH</td>
</tr>
<tr class="even">
<td>DSP</td>
<td>1</td>
<td>2/ID</td>
<td>Set ID</td>
<td>HL7</td>
<td>EPI</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>80/FT</td>
<td><p>Date~Text Term~Resolved</p>
<p>Term~Result~Sourceid</p></td>
<td>USER</td>
<td>EPI</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>2/ID</td>
<td><p>Result ID (linking DSP and</p>
<p>ZXE)</p></td>
<td>HL7</td>
<td>EPI</td>
</tr>
<tr class="odd">
<td>ZXE</td>
<td>1</td>
<td>20/FT</td>
<td>NDC</td>
<td>USER</td>
<td>EPI</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>75/FT</td>
<td>Drug Name~Coding System</td>
<td>USER</td>
<td>EPI</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>4/NM</td>
<td>Days Supply</td>
<td>USER</td>
<td>EPI</td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>19/TS</td>
<td>Release Date/Time</td>
<td>USER</td>
<td>EPI</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>19/TS</td>
<td>Fill Date/Time</td>
<td>USER</td>
<td>EPI</td>
</tr>
<tr class="even">
<td></td>
<td>6</td>
<td>19/TS</td>
<td>Stop Date/Time</td>
<td>USER</td>
<td>EPI</td>
</tr>
<tr class="odd">
<td></td>
<td>7</td>
<td>2/ID</td>
<td><p>Result ID (linking DSP</p>
<p>and ZXE)</p></td>
<td>USER</td>
<td>EPI</td>
</tr>
</tbody>
</table>

> Note \#1 – This software extracts data for two databases, EPI (Emerging Pathogens Initiative) and NCH (National Center for Health). Items not marked with NCH will not be transmitted during that run.

> Note \#2 – The NTE segment is present in four forms. EPI only items tagged with (epi).

> a\. NTE\|\|manual/automatic indicator (Null for automatic, R for Manual)~REPORTING DATE FROM from date TO to date~message number\~~software version number (blank for original system/V2 for new system(epi)~Negative Input Indicator (null if input is present, N if negative)

> b\. NTE\|sequence number\|reference number from field .05 (reference number) in file 69.5 (LAB SEARCH/EXTRACT)

> c\. NTE\|\|Totals indicator (T if NTE describes totals for run)~National Lab Test Code~Test Name from files 60 (Lab Test) or file 61.2 (Etiology Field)~Total number of tests performed

> d\. NTE\|\|Totals indicator (T if NTE describes totals for run)~National Lab Test Code~”PATIENTS WITH “\_Test Name from files 60 (Lab Test) or file 61.2 (Etiology Field)~Number of unique patients receiving this test

## Definitions from Austin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 38%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Start</strong></td>
<td><strong>End</strong></td>
<td><strong>Length</strong></td>
<td><strong>Properties</strong></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>DG1 SEGMENT</strong></td>
<td><h1 id="section-4"></h1></td>
<td><h1 id="section-5"></h1></td>
<td><h1 id="section-6"></h1></td>
<td><h1 id="section-7"></h1></td>
<td><h1 id="section-8"></h1></td>
</tr>
<tr class="even">
<td>SET-ID</td>
<td>94</td>
<td>97</td>
<td>4</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>DIAG-CODING-METHOD</td>
<td>98</td>
<td>99</td>
<td>2</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>DIAG-CODE</td>
<td>100</td>
<td>106</td>
<td>7</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>DIAG-TEXT</td>
<td>107</td>
<td>146</td>
<td>40</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>DIAG-CODING-SYT</td>
<td>147</td>
<td>156</td>
<td>10</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>FILLER</td>
<td>157</td>
<td>467</td>
<td>311</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>NTE-SEGMENT</td>
<td><h1 id="section-9"></h1></td>
<td><h1 id="section-10"></h1></td>
<td><h1 id="section-11"></h1></td>
<td><h1 id="section-12"></h1></td>
<td><h1 id="section-13"></h1></td>
</tr>
<tr class="even">
<td>SET-ID</td>
<td>94</td>
<td>97</td>
<td>4</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>ACTION-IND</td>
<td>98</td>
<td>99</td>
<td>2</td>
<td>alphanumeric</td>
<td>valid total indicator T</td>
</tr>
<tr class="even">
<td><p>NATIONAL-</p>
<p>LAB-TEST-NUM</p></td>
<td>100</td>
<td>109</td>
<td>10</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>BACTERIA</td>
<td>110</td>
<td>144</td>
<td>35</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>TOTAL-COUNT</td>
<td>145</td>
<td>149</td>
<td>5</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>FILLER</td>
<td>150</td>
<td>467</td>
<td>318</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>NTE-SEGMENT</strong> (alternate type)</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>SET-ID</td>
<td>94</td>
<td>97</td>
<td>4</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>ACTION-IND</td>
<td>98</td>
<td>99</td>
<td>2</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>FILLER</td>
<td>100</td>
<td>119</td>
<td>20</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>FROM-DATE</td>
<td>120</td>
<td>127</td>
<td>8</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>FILLER</td>
<td>128</td>
<td>131</td>
<td>4</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>TO-DATE</td>
<td>132</td>
<td>139</td>
<td>8</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>MSG-SEQ-NUM</td>
<td>140</td>
<td>142</td>
<td>3</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>NEGATIVE-INPUT-IND</td>
<td>143</td>
<td>143</td>
<td>1</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>FILLER</td>
<td>144</td>
<td>467</td>
<td>324</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OBR-SEGMENT</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><h1 id="section-14"></h1></td>
</tr>
<tr class="odd">
<td>SET-ID</td>
<td>94</td>
<td>97</td>
<td>4</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>PATHOGEN-NAME</td>
<td>98</td>
<td>132</td>
<td>35</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>UNIV-SERVICE-ID</td>
<td>133</td>
<td>142</td>
<td>10</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>UNIV-SERVICE-TEXT</td>
<td>143</td>
<td>172</td>
<td>30</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>UNIV-SERVICE-CODE</td>
<td>173</td>
<td>187</td>
<td>15</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>ALT-UNIV-SERVICE-ID</td>
<td>188</td>
<td>202</td>
<td>15</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>ALT-UNIV-SERVICE-TEXT</td>
<td>203</td>
<td>232</td>
<td>30</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>ALT-UNIV-SERVICE-CODE</td>
<td>233</td>
<td>247</td>
<td>15</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>OBSER-DATE</td>
<td>248</td>
<td>255</td>
<td>8</td>
<td>yyyymmdd</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 38%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Start</strong></td>
<td><strong>End</strong></td>
<td><strong>Length</strong></td>
<td><strong>Properties</strong></td>
<td></td>
</tr>
<tr class="even">
<td>OBSER-TIME</td>
<td>256</td>
<td>261</td>
<td>6</td>
<td>hhmmss</td>
<td></td>
</tr>
<tr class="odd">
<td>OBSER-DATE-A</td>
<td>262</td>
<td>269</td>
<td>8</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>SPECIMEN-CODE</td>
<td>270</td>
<td>273</td>
<td>4</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>FILLER</td>
<td>274</td>
<td>274</td>
<td>1</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>SPECIMEN-CODE-TEXT</td>
<td>275</td>
<td>304</td>
<td>30</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>ACCESSION-NUM</td>
<td>305</td>
<td>324</td>
<td>20</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>PARENT-OBSER-ID</td>
<td>335</td>
<td>334</td>
<td>10</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>PARENT-OBSER-SUB-ID</td>
<td>355</td>
<td>340</td>
<td>6</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>PARENT-TEST-SYS</td>
<td>361</td>
<td>350</td>
<td>10</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>PARENT-LAB-NUM</td>
<td>371</td>
<td>360</td>
<td>10</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>FILLER</td>
<td>381</td>
<td>458</td>
<td>98</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td><strong>OBX-SEGMENT</strong></td>
<td><h1 id="section-15"></h1></td>
<td><h1 id="section-16"></h1></td>
<td><h1 id="section-17"></h1></td>
<td><h1 id="section-18"></h1></td>
<td><h1 id="section-19"></h1></td>
</tr>
<tr class="even">
<td>OBR-SET-ID</td>
<td>94</td>
<td>97</td>
<td>4</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>OBX-SET-ID</td>
<td>98</td>
<td>101</td>
<td>4</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>VALUE-TYPE</td>
<td>102</td>
<td>103</td>
<td>2</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>OBSERVATION-ID</td>
<td>104</td>
<td>113</td>
<td>10</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>OBSERVATION-TEXT</td>
<td>114</td>
<td>143</td>
<td>30</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>OBSERVATION-CODE</td>
<td>144</td>
<td>158</td>
<td>15</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>OBSERVATION-ID-ALT</td>
<td>159</td>
<td>168</td>
<td>10</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>OBSERVATION-TEXT-ALT</td>
<td>169</td>
<td>198</td>
<td>30</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>OBSERVATION-CODE-ALT</td>
<td>199</td>
<td>213</td>
<td>15</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>OBSERVATION-SUB-ID</td>
<td>214</td>
<td>219</td>
<td>6</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>OBSERVATION-NAT-LAB</td>
<td>220</td>
<td>229</td>
<td>10</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>OBSERVATION-VALUE</td>
<td>230</td>
<td>274</td>
<td>45</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>OBSERVATION-UNITS</td>
<td>275</td>
<td>289</td>
<td>15</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>OBSERVATION-REF-RANGE</td>
<td>290</td>
<td>304</td>
<td>15</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>ABNORMAL-FLAGS</td>
<td>305</td>
<td>314</td>
<td>10</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>FINAL-RESULT-DATE</td>
<td>315</td>
<td>322</td>
<td>8</td>
<td>yyyymmdd</td>
<td></td>
</tr>
<tr class="even">
<td>FILLER</td>
<td>323</td>
<td>450</td>
<td>128</td>
<td>alphanumeric</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 38%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Field Name</strong></td>
<td><strong>Start</strong></td>
<td><strong>End</strong></td>
<td><strong>Length</strong></td>
<td><strong>Properties</strong></td>
<td></td>
</tr>
<tr class="even">
<td>PID-SEGMENT</td>
<td><h1 id="section-20"></h1></td>
<td><h1 id="section-21"></h1></td>
<td><h1 id="section-22"></h1></td>
<td><h1 id="section-23"></h1></td>
<td><h1 id="section-24"></h1></td>
</tr>
<tr class="odd">
<td>SET-ID</td>
<td>94</td>
<td>97</td>
<td>4</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>PATIENT-EXTERNAL-ID</td>
<td>98</td>
<td>114</td>
<td>17</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>PATIENT-INTERNAL-ID</td>
<td>115</td>
<td>135</td>
<td>21</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>PATIENT-NAME</td>
<td>136</td>
<td>220</td>
<td>85</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>PATIENT-BIRTH-DATE</td>
<td>221</td>
<td>228</td>
<td>8</td>
<td>yyyymmdd</td>
<td></td>
</tr>
<tr class="even">
<td>PATIENT-SEX</td>
<td>229</td>
<td>229</td>
<td>1</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>PATIENT-RACE</td>
<td>230</td>
<td>230</td>
<td>1</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>PATIENT-ADDRESS</td>
<td>231</td>
<td>231</td>
<td>1</td>
<td>alphanumeric</td>
<td>valid patient address H</td>
</tr>
<tr class="odd">
<td>ZIP</td>
<td>232</td>
<td>240</td>
<td>9</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>FILLER</td>
<td>241</td>
<td>241</td>
<td>1</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td>PATIENT-SSN</td>
<td>242</td>
<td>250</td>
<td>9</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>PATIENT-PSEUDO</td>
<td>251</td>
<td>251</td>
<td>1</td>
<td>alphanumeric</td>
<td>valid pseudo space or P</td>
</tr>
<tr class="odd">
<td>PATIENT-VETERAN-STATUS</td>
<td>252</td>
<td>253</td>
<td>2</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>FILLER</td>
<td>254</td>
<td>450</td>
<td>197</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>PV1-SEGMENT</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>SET-ID</td>
<td>94</td>
<td>97</td>
<td>4</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>PATIENT-CLASS</td>
<td>98</td>
<td>98</td>
<td>1</td>
<td>alphanumeric</td>
<td>valid patient class I or O or U</td>
</tr>
<tr class="odd">
<td>DISCHARGE-DISPOSITION</td>
<td>99</td>
<td>133</td>
<td>35</td>
<td>alphanumeric</td>
<td></td>
</tr>
<tr class="even">
<td>ADMIT-DATE</td>
<td>134</td>
<td>141</td>
<td>8</td>
<td>yyyymmdd</td>
<td></td>
</tr>
<tr class="odd">
<td>ADMIT-TIME</td>
<td>142</td>
<td>147</td>
<td>6</td>
<td>hhmmss</td>
<td></td>
</tr>
<tr class="even">
<td>DISCHARGE-DATE</td>
<td>148</td>
<td>155</td>
<td>8</td>
<td>yyyymmdd</td>
<td></td>
</tr>
<tr class="odd">
<td>DISCHARGE-TIME</td>
<td>156</td>
<td>161</td>
<td>6</td>
<td>hhmmss</td>
<td></td>
</tr>
<tr class="even">
<td>FILLER</td>
<td>162</td>
<td>450</td>
<td>289</td>
<td>alphanumeric</td>
<td></td>
</tr>
</tbody>
</table>

### Transaction Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *4.1 General*

> The V*IST*A software sends an Observational Result Unsolicited (ORU) result type HL7 message whenever one or more of the defined emerging pathogen initiatives are identified.

> *4.2 Specific Transaction*

> A. Identified Encounter

> When EPI data are identified an EPI Observational Result Unsolicited (ORU) message is sent to the AITC. The EPI ORU message consist of the following segments:

> Example: EPI ORU Message

> ORU OBSERVATIONAL RESULT UNSOLICITED

> MSH Message Header

> NTE Notes and Comments

> PID Patient Identification

> PV1 Patient Visit

> NTE Notes and Comments

> DG1 Diagnosis

> DSP Display Data

> ZXE Pharmacy Prescription

> OBR Observation Report

> OBX Results

> MSH\|~\|\\\|EPI-XXX\|170\|EPI-XXX\|170\|19961018113521\|\|ORU~R01\|107\|P\|2.2\|\|\|\|\|USA

> NTE\|\|REPORTING DATE FROM 19850101 TO 19961018

> PID\|1\|000-00-0008~0~M10\|5~5~M10\|\|LABPATIENT~EIGHT\|\|19220912\|M\|\|7\|\|\|\|\|\|\|\|\|052167946

> PV1\|1\|O\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|19950315151907

> NTE\|1\|Vanc-Res Enterococcus

> DG1\|1\|I9\|451.19^DEEP PHLEBITIS-LEG NEC^I9

> DG1\|2\|I9\|511.9^PLEURAL EFFUSION NOS^I9

> DG1\|3\|I9\|670.02^MAJOR PUERP INF-DEL P/P^I9

> DG1\|4\|I9\|331.0^ALZHEIMER'S DISEASE^I9

> DG1\|5\|I9\|500.^COAL WORKERS' PNEUMOCON^I9

> OBR\|1\|\|\|^CHEMISTRY TEST^VANLT\|\|\|19950315151907\|\|\|\|\|\|\|\|SER^^SERUM

> OBX\|1\|ST\|84330.0000^Glucose Quant^VANLT^260^GLUCOSE1^VA60\|\|25\|mg/dL\|70-125\|L\*

> NTE\|2\|2^Hepatitis C antibody

> OBR\|2\|\|\|^CHEMISTRY TEST^VANLT\|\|\|19950315151907\|\|\|\|\|\|\|\|SER^^SERUM

> OBX\|1\|ST\|84330.0000^Glucose Quant^VANLT^260^GLUCOSE1^VA60\|\|25\|mg/dL\|70-125\|L\*

> PID\|2\|000-00-0009~8~M10\|7~7~M10\|\|LABPATIENT~NINE\|\|19591229\|F\|\|7\|\|\|\|\|\|\|\|\|023456666

> PV1\|1\|O\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|19950315152721

> NTE\|1\|1^Vanc-Res Enterococcus

> OBR\|1\|\|\|87999.0000^MICRO CULTURE^VANLT\|\|\|198612100835\|\|\|\|\|\|\|\|^^BLOOD

> OBX\|1\|CE\|87993.0000^BACTERIOLOGY CULTURE^VANLT\|1\|^ESCHERICHIA COLI

> OBR\|2\|\|^ANTIBIOTIC MIC^VANLT\|\|\|\|198612100835\|\|\|\|\|\|\|\|^^BLOOD\|\|\|\|\|\|\|\|\|\|\|87993.0000^1

> OBX\|1\|ST\|81812.0000^Neomycin^VANLT^18^NEOMYCN^VA62.06\|\|\|\|\|R

> OBX\|2\|ST\|^^^35^BACTRCN^VA62.06\|\|\|\|\|R

> OBX\|3\|ST\|81852.0000^Penicillin^VANLT^23^PENICLN^VA62.06\|\|\|\|\|R

> OBX\|4\|ST\|81676.0000^Clindamycin^VANLT^3^CLINDAM^VA62.06\|\|\|\|\|S

#### Table VA011 - Period of Service

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Value</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>KOREAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>WORLD WAR I</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>WORLD WAR II</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>SPANISH AMERICAN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>PRE-KOREAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>POST-KOREAN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>OPERATION DESERT SHIELD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>VIETNAM ERA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>POST-VIETNAM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>OTHER OR NONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p>ARMY--ACTIVE DUTY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p>NAVY, MARINE--ACTIVE DUTY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p>AIR FORCE--ACTIVE DUTY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p>COAST GUARD--ACTIVE DUTY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>E</p>
</blockquote></td>
<td><blockquote>
<p>RETIRED, UNIFORMED FORCES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>F</p>
</blockquote></td>
<td><blockquote>
<p>MEDICAL REMEDIAL ENLIST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>G</p>
</blockquote></td>
<td><blockquote>
<p>MERCHANT SEAMEN--USPHS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>H</p>
</blockquote></td>
<td><blockquote>
<p>OTHER USPHS BENEFICIARIES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>I</p>
</blockquote></td>
<td><blockquote>
<p>OBSERVATION/EXAMINATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>J</p>
</blockquote></td>
<td><blockquote>
<p>OFFICE OF WORKERS COMP.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>K</p>
</blockquote></td>
<td><blockquote>
<p>JOB CORPS/PEACE CORPS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p>RAILROAD RETIREMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>BENEFICIARIES-FOREIGN GOV</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p>HUMANITARIAN (NON-VET)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>CHAMPUS RESTORE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>P</p>
</blockquote></td>
<td><blockquote>
<p>OTHER REIMBURS. (NON-VET)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Q</p>
</blockquote></td>
<td><blockquote>
<p>OTHER FEDERAL - DEPENDENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>DONORS (NON-VET)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>SPECIAL STUDIES (NON-VET)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>T</p>
</blockquote></td>
<td><blockquote>
<p>OTHER NON-VETERANS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p>CHAMPVA--SPOUSE, CHILD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>V</p>
</blockquote></td>
<td><blockquote>
<p>CHAMPUS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>W</p>
</blockquote></td>
<td><blockquote>
<p>CZECHOSLOVAKIA/POLAND SVC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>PERSIAN GULF WAR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Y</p>
</blockquote></td>
<td><blockquote>
<p>CAV/NPS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Z</p>
</blockquote></td>
<td><blockquote>
<p>MERCHANT MARINE</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Table 0070 - Specimen Source Codes

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
<td><blockquote>
<p>Abbreviations</p>
</blockquote></td>
<td><blockquote>
<p>Descriptions</p>
</blockquote></td>
<td><blockquote>
<p>Abbreviations</p>
</blockquote></td>
<td><blockquote>
<p>Descriptions</p>
</blockquote></td>
<td><blockquote>
<p>Abbreviations</p>
</blockquote></td>
<td><blockquote>
<p>Descriptions</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ABS</p>
</blockquote></td>
<td><blockquote>
<p>Abscess</p>
</blockquote></td>
<td><blockquote>
<p>FLU</p>
</blockquote></td>
<td><blockquote>
<p>Body fluid, unsp</p>
</blockquote></td>
<td><blockquote>
<p>SER</p>
</blockquote></td>
<td><blockquote>
<p>Serum</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AMN</p>
</blockquote></td>
<td><blockquote>
<p>Amniotic fluid</p>
</blockquote></td>
<td><blockquote>
<p>GAS</p>
</blockquote></td>
<td><blockquote>
<p>Gas</p>
</blockquote></td>
<td><blockquote>
<p>SKN</p>
</blockquote></td>
<td><blockquote>
<p>Skin</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ASP</p>
</blockquote></td>
<td><blockquote>
<p>Aspirate</p>
</blockquote></td>
<td><blockquote>
<p>GAST</p>
</blockquote></td>
<td><blockquote>
<p>Gastric fluid/contents</p>
</blockquote></td>
<td><blockquote>
<p>SKM</p>
</blockquote></td>
<td><blockquote>
<p>Skeletal muscle</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BPH</p>
</blockquote></td>
<td><blockquote>
<p>Basophils</p>
</blockquote></td>
<td><blockquote>
<p>GEN</p>
</blockquote></td>
<td><blockquote>
<p>Genital</p>
</blockquote></td>
<td><blockquote>
<p>SPRM</p>
</blockquote></td>
<td><blockquote>
<p>Spermatozoa</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BIFL</p>
</blockquote></td>
<td><blockquote>
<p>Bile fluid</p>
</blockquote></td>
<td><blockquote>
<p>GENC</p>
</blockquote></td>
<td><blockquote>
<p>Genital cervix</p>
</blockquote></td>
<td><blockquote>
<p>SPT</p>
</blockquote></td>
<td><blockquote>
<p>Sputum</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BBL</p>
</blockquote></td>
<td><blockquote>
<p>Blood bag</p>
</blockquote></td>
<td><blockquote>
<p>GENV</p>
</blockquote></td>
<td><blockquote>
<p>Genital vaginal</p>
</blockquote></td>
<td><blockquote>
<p>SPTT</p>
</blockquote></td>
<td><blockquote>
<p>Sputum tracheal</p>
<p>aspirate</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BLDC</p>
</blockquote></td>
<td><blockquote>
<p>Blood capillary</p>
</blockquote></td>
<td><blockquote>
<p>HAR</p>
</blockquote></td>
<td><blockquote>
<p>Hair</p>
</blockquote></td>
<td><blockquote>
<p>STON</p>
</blockquote></td>
<td><blockquote>
<p>Stone (use CALC)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BPU</p>
</blockquote></td>
<td><blockquote>
<p>Blood product unit</p>
</blockquote></td>
<td><blockquote>
<p>IHG</p>
</blockquote></td>
<td><blockquote>
<p>Inhaled Gas</p>
</blockquote></td>
<td><blockquote>
<p>STL</p>
</blockquote></td>
<td><blockquote>
<p>Stool = Fecal</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BLDV</p>
</blockquote></td>
<td><blockquote>
<p>Blood venous</p>
</blockquote></td>
<td><blockquote>
<p>IT</p>
</blockquote></td>
<td><blockquote>
<p>Intubation tube</p>
</blockquote></td>
<td><blockquote>
<p>SWT</p>
</blockquote></td>
<td><blockquote>
<p>Sweat</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BON</p>
</blockquote></td>
<td><blockquote>
<p>Bone</p>
</blockquote></td>
<td><blockquote>
<p>ISLT</p>
</blockquote></td>
<td><blockquote>
<p>Isolate</p>
</blockquote></td>
<td><blockquote>
<p>SNV</p>
</blockquote></td>
<td><blockquote>
<p>Synovial fluid</p>
<p>(Joint fluid)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BRTH</p>
</blockquote></td>
<td><blockquote>
<p>Breath</p>
<p>(use EXHLD)</p>
</blockquote></td>
<td><blockquote>
<p>LAM</p>
</blockquote></td>
<td><blockquote>
<p>Lamella</p>
</blockquote></td>
<td><blockquote>
<p>TEAR</p>
</blockquote></td>
<td><blockquote>
<p>Tears</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>BRO</p>
</blockquote></td>
<td><blockquote>
<p>Bronchial</p>
</blockquote></td>
<td><blockquote>
<p>WBC</p>
</blockquote></td>
<td><blockquote>
<p>Leukocytes</p>
</blockquote></td>
<td><blockquote>
<p>THRT</p>
</blockquote></td>
<td><blockquote>
<p>Throat</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BRN</p>
</blockquote></td>
<td><blockquote>
<p>Burn</p>
</blockquote></td>
<td><blockquote>
<p>LN</p>
</blockquote></td>
<td><blockquote>
<p>Line</p>
</blockquote></td>
<td><blockquote>
<p>THRB</p>
</blockquote></td>
<td><blockquote>
<p>Thrombocyte</p>
<p>(platelet)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CALC</p>
</blockquote></td>
<td><blockquote>
<p>Calculus (=Stone)</p>
</blockquote></td>
<td><blockquote>
<p>LNA</p>
</blockquote></td>
<td><blockquote>
<p>Line arterial</p>
</blockquote></td>
<td><blockquote>
<p>TISS</p>
</blockquote></td>
<td><blockquote>
<p>Tissue</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CDM</p>
</blockquote></td>
<td><blockquote>
<p>Cardiac muscle</p>
</blockquote></td>
<td><blockquote>
<p>LNV</p>
</blockquote></td>
<td><blockquote>
<p>Line venous</p>
</blockquote></td>
<td><blockquote>
<p>TISG</p>
</blockquote></td>
<td><blockquote>
<p>Tissue gall bladder</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CNL</p>
</blockquote></td>
<td><blockquote>
<p>Cannula</p>
</blockquote></td>
<td><blockquote>
<p>LIQ</p>
</blockquote></td>
<td><blockquote>
<p>Liquid NOS</p>
</blockquote></td>
<td><blockquote>
<p>TLGI</p>
</blockquote></td>
<td><blockquote>
<p>Tissue large</p>
<p>intestine</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CTP</p>
</blockquote></td>
<td><blockquote>
<p>Catheter tip</p>
</blockquote></td>
<td><blockquote>
<p>LYM</p>
</blockquote></td>
<td><blockquote>
<p>Lymphocytes</p>
</blockquote></td>
<td><blockquote>
<p>TLNG</p>
</blockquote></td>
<td><blockquote>
<p>Tissue lung</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CSF</p>
</blockquote></td>
<td><blockquote>
<p>Cerebral spinal fluid</p>
</blockquote></td>
<td><blockquote>
<p>MAC</p>
</blockquote></td>
<td><blockquote>
<p>Macrophages</p>
</blockquote></td>
<td><blockquote>
<p>TISPL</p>
</blockquote></td>
<td><blockquote>
<p>Tissue placenta</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CVM</p>
</blockquote></td>
<td><blockquote>
<p>Cervical mucus</p>
</blockquote></td>
<td><blockquote>
<p>MAR</p>
</blockquote></td>
<td><blockquote>
<p>Marrow</p>
</blockquote></td>
<td><blockquote>
<p>TSMI</p>
</blockquote></td>
<td><blockquote>
<p>Tissue small</p>
<p>intestine</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CVX</p>
</blockquote></td>
<td><blockquote>
<p>Cervix</p>
</blockquote></td>
<td><blockquote>
<p>MEC</p>
</blockquote></td>
<td><blockquote>
<p>Meconium</p>
</blockquote></td>
<td><blockquote>
<p>TISU</p>
</blockquote></td>
<td><blockquote>
<p>Tissue ulcer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>COL</p>
</blockquote></td>
<td><blockquote>
<p>Colostrum</p>
</blockquote></td>
<td><blockquote>
<p>MBLD</p>
</blockquote></td>
<td><blockquote>
<p>Menstrual blood</p>
</blockquote></td>
<td><blockquote>
<p>TUB</p>
</blockquote></td>
<td><blockquote>
<p>Tube NOS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CBLD</p>
</blockquote></td>
<td><blockquote>
<p>Cord blood</p>
</blockquote></td>
<td><blockquote>
<p>MLK</p>
</blockquote></td>
<td><blockquote>
<p>Milk</p>
</blockquote></td>
<td><blockquote>
<p>ULC</p>
</blockquote></td>
<td><blockquote>
<p>Ulcer</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CNJT</p>
</blockquote></td>
<td><blockquote>
<p>Conjunctiva</p>
</blockquote></td>
<td><blockquote>
<p>MILK</p>
</blockquote></td>
<td><blockquote>
<p>Breast milk</p>
</blockquote></td>
<td><blockquote>
<p>UMB</p>
</blockquote></td>
<td><blockquote>
<p>Umbilical blood</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CUR</p>
</blockquote></td>
<td><blockquote>
<p>Curettage</p>
</blockquote></td>
<td><blockquote>
<p>NAIL</p>
</blockquote></td>
<td><blockquote>
<p>Nail</p>
</blockquote></td>
<td><blockquote>
<p>UMED</p>
</blockquote></td>
<td><blockquote>
<p>Unknown medicine</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CYST</p>
</blockquote></td>
<td><blockquote>
<p>Cyst</p>
</blockquote></td>
<td><blockquote>
<p>NOS</p>
</blockquote></td>
<td><blockquote>
<p>Nose (nasal passage)</p>
</blockquote></td>
<td><blockquote>
<p>URTH</p>
</blockquote></td>
<td><blockquote>
<p>Urethra</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DIAF</p>
</blockquote></td>
<td><blockquote>
<p>Dialysis fluid</p>
</blockquote></td>
<td><blockquote>
<p>ORH</p>
</blockquote></td>
<td><blockquote>
<p>Other</p>
</blockquote></td>
<td><blockquote>
<p>UR</p>
</blockquote></td>
<td><blockquote>
<p>Urine</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DOSE</p>
</blockquote></td>
<td><blockquote>
<p>Dose med or</p>
<p>substance</p>
</blockquote></td>
<td><blockquote>
<p>PAFL</p>
</blockquote></td>
<td><blockquote>
<p>Pancreatic fluid</p>
</blockquote></td>
<td><blockquote>
<p>URC</p>
</blockquote></td>
<td><blockquote>
<p>Urine clean catch</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DRN</p>
</blockquote></td>
<td><blockquote>
<p>Drain</p>
</blockquote></td>
<td><blockquote>
<p>PAT</p>
</blockquote></td>
<td><blockquote>
<p>Patient</p>
</blockquote></td>
<td><blockquote>
<p>URT</p>
</blockquote></td>
<td><blockquote>
<p>Urine catheter</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DUFL</p>
</blockquote></td>
<td><blockquote>
<p>Duodenal fluid</p>
</blockquote></td>
<td><blockquote>
<p>PRT</p>
</blockquote></td>
<td><blockquote>
<p>Peritoneal fluid ascites</p>
</blockquote></td>
<td><blockquote>
<p>URNS</p>
</blockquote></td>
<td><blockquote>
<p>Urine sediment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EAR</p>
</blockquote></td>
<td><blockquote>
<p>Ear</p>
</blockquote></td>
<td><blockquote>
<p>PLC</p>
</blockquote></td>
<td><blockquote>
<p>Placenta</p>
</blockquote></td>
<td><blockquote>
<p>USUB</p>
</blockquote></td>
<td><blockquote>
<p>Unknown</p>
<p>substance</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EARW</p>
</blockquote></td>
<td><blockquote>
<p>Ear wax (cerumen)</p>
</blockquote></td>
<td><blockquote>
<p>PLAS</p>
</blockquote></td>
<td><blockquote>
<p>Plasma</p>
</blockquote></td>
<td><blockquote>
<p>VOM</p>
</blockquote></td>
<td><blockquote>
<p>Vomitus</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ELT</p>
</blockquote></td>
<td><blockquote>
<p>Electrode</p>
</blockquote></td>
<td><blockquote>
<p>PLB</p>
</blockquote></td>
<td><blockquote>
<p>Plasma bag</p>
</blockquote></td>
<td><blockquote>
<p>BLD</p>
</blockquote></td>
<td><blockquote>
<p>Whole blood</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ENDC</p>
</blockquote></td>
<td><blockquote>
<p>Endocardium</p>
</blockquote></td>
<td><blockquote>
<p>PLR</p>
</blockquote></td>
<td><blockquote>
<p>Pleural fluid</p>
<p>(thoracentesis fld)</p>
</blockquote></td>
<td><blockquote>
<p>BDY</p>
</blockquote></td>
<td><blockquote>
<p>Whole body</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ENDM</p>
</blockquote></td>
<td><blockquote>
<p>Endometrium</p>
</blockquote></td>
<td><blockquote>
<p>PMN</p>
</blockquote></td>
<td><blockquote>
<p>Polymorphonuclear</p>
<p>neutrophils</p>
</blockquote></td>
<td><blockquote>
<p>WAT</p>
</blockquote></td>
<td><blockquote>
<p>Water</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EOS</p>
</blockquote></td>
<td><blockquote>
<p>Eosinophils</p>
</blockquote></td>
<td><blockquote>
<p>PPP</p>
</blockquote></td>
<td><blockquote>
<p>Platelet poor plasma</p>
</blockquote></td>
<td><blockquote>
<p>WICK</p>
</blockquote></td>
<td><blockquote>
<p>Wick</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RBC</p>
</blockquote></td>
<td><blockquote>
<p>Erythrocytes</p>
</blockquote></td>
<td><blockquote>
<p>PRP</p>
</blockquote></td>
<td><blockquote>
<p>Platelet rich plasma</p>
</blockquote></td>
<td><blockquote>
<p>WND</p>
</blockquote></td>
<td><blockquote>
<p>Wound</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EYE</p>
</blockquote></td>
<td><blockquote>
<p>Eye</p>
</blockquote></td>
<td><blockquote>
<p>PUS</p>
</blockquote></td>
<td><blockquote>
<p>Pus</p>
</blockquote></td>
<td><blockquote>
<p>WNDA</p>
</blockquote></td>
<td><blockquote>
<p>Wound abscess</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EXHLD</p>
</blockquote></td>
<td><blockquote>
<p>Exhaled gas (breath)</p>
</blockquote></td>
<td><blockquote>
<p>RT</p>
</blockquote></td>
<td><blockquote>
<p>Route of medicine</p>
</blockquote></td>
<td><blockquote>
<p>WNDE</p>
</blockquote></td>
<td><blockquote>
<p>Wound exudate</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FIB</p>
</blockquote></td>
<td><blockquote>
<p>Fibroblasts</p>
</blockquote></td>
<td><blockquote>
<p>SAL</p>
</blockquote></td>
<td><blockquote>
<p>Saliva</p>
</blockquote></td>
<td><blockquote>
<p>WNDD</p>
</blockquote></td>
<td><blockquote>
<p>Wound drainage</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FLT</p>
</blockquote></td>
<td><blockquote>
<p>Filter</p>
</blockquote></td>
<td><blockquote>
<p>SEM</p>
</blockquote></td>
<td><blockquote>
<p>Seminal fluid</p>
</blockquote></td>
<td><blockquote>
<p>XXX</p>
</blockquote></td>
<td><blockquote>
<p>To be specified in</p>
<p>another part of the</p>
<p>message</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FIST</p>
</blockquote></td>
<td><blockquote>
<p>Fistula</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

#### Table VA07 - Race

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Value</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>HISPANIC, WHITE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>HISPANIC, BLACK</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>AMERICAN INDIAN OR ALASKA NATIVE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>BLACK, NOT OF HISPANIC ORIGIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>ASIAN OR PACIFIC ISLANDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>WHITE NOT OF HISPANIC ORIGIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>UNKNOWN</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Table 0001 - Sex

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Value</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>F</p>
</blockquote></td>
<td><blockquote>
<p>FEMALE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p>MALE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p>OTHER</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Table 0078 - Abnormal flags

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Value</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p>Below low normal</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>H</p>
</blockquote></td>
<td><blockquote>
<p>Above high normal</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LL</p>
</blockquote></td>
<td><blockquote>
<p>Below lower panic limits</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HH</p>
</blockquote></td>
<td><blockquote>
<p>Above upper panic limits</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>For microbiology sensitivities only</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>Sensitive</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p>Resistant</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>I</p>
</blockquote></td>
<td><blockquote>
<p>Intermediate</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MS</p>
</blockquote></td>
<td><blockquote>
<p>Moderately sensitive</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VS</p>
</blockquote></td>
<td><blockquote>
<p>Very sensitive</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Table Specimen Source ID Code

|              |                 |
|--------------|-----------------|
| Value    | Description |
| Problem List | 1               |
| Encounter Dx | 2               |
| Discharge DX | 3               |

#### Table Hepatitis Risk Assessment Resolutions

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Value</strong></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>Declined Hep C Risk Assessment</td>
<td>1</td>
</tr>
<tr class="odd">
<td>No Risk Factors for Hep C</td>
<td>2</td>
</tr>
<tr class="even">
<td>Prev Positive Test for Hep C</td>
<td>3</td>
</tr>
<tr class="odd">
<td>Risk Factor for Hepatitis C</td>
<td>4</td>
</tr>
<tr class="even">
<td>Hep C Virus Antibody Positive</td>
<td>5</td>
</tr>
<tr class="odd">
<td>Hep C Virus Antibody Negative</td>
<td>6</td>
</tr>
<tr class="even">
<td>Hepatitis C Infection</td>
<td>7</td>
</tr>
</tbody>
</table>

> **NOTE:** Term other than Hepatitis C National Risk Assessment Clinical Reminders resolution term 00

LABORATORY HEPATITIS C EXTRACT AND EPI USER GUIDE

*(This page included for two-sided copying.)*

# Laboratory Hepatitis C Extract and EPI User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Laboratory Hepatitis C Extract and EPI User Guide provides all the necessary information, instructions, illustrations, and examples required for the EPI coordinators, Laboratory personnel, and other users to implement and maintain the following 17 EPI parameter descriptions.

> *CandidaHepatitis C Antibody POS*

> *ClostridiumdifficileLegionella*

> Creutzfeldt-Jakob Disease Leishmanaisis

> *Cryptosporidium* Malaria

> Dengue Pen- Res Pneumococcus

> *E. coli* O157:H7 *Streptococcus-*Group A

> *Hepatitis A Antibody POS* Tuberculosis

> *Hepatitis B POS Vanc-Res Enterococcus*

> *Hepatitis C Antibody NEG*

> NOTE: It is highly recommended that the following person(s) <u>jointly</u> participate in the review and parameter descriptions setup process for the 17 EPI descriptions:

> Laboratory Information Manager (LIM)

> Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) staff (e.g., or person at the facility with similar function)

> Representative from the Microbiology (i.e., director, supervisor, or technologist)

> The 17 emerging pathogens will require an ongoing review process (i.e., as specified by the VAHQ Infectious Disease Program Office). The person(s) participating in the ongoing review process is responsible for ensuring the following requirements are kept current.

- Periodic reviews of the ICD codes.
- Periodic reviews of the Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option for the defined EPI parameter description setups. Remember that if the parameter set up needs to be changed for any of the four hepatitis entities, that a concomitant change needs to be made in the corresponding Reminders logic.
- Annual review of the 17 Emerging Pathogens descriptions (as specified by the VAHQ Infectious Disease Program Office).

## Lab Search/Extract Primary \[LREPI SEARCH EXTRACT MENU\] Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: The Lab Search/Extract Primary \[LREPI SEARCH EXTRACT MENU\] Menu options are using VA FileMan screens displays, referred to as ScreenMan. For detailed instructions on how to use the screens please review the VA FileMan V. 21.0 User Manual, Section 6 ScreenMan.

> Lab Search/Extract Primary Menu \[LREPI SEARCH EXTRACT MENU\]: This is the primary menu containing five options. There are no locks or security keys associated with the menu or options.

> Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCE MANUAL RUN\] option: This option will automatically transmit EPI and the three new Hepatitis pathogens data corrections to the AITC, via HL7 format mailman messages each time the option is run.

> NOTES:

> Lab Search/Extract transmissions to AITC after 6:00 pm are processed the next day.

> Please DO NOT use the Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option to transmit EPI and Hepatitis pathogens data on Wednesdays of PAY ROLL weeks. These transmissions may cause a delay in processing the PAY ROLL data.

- Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option: This option allows the users to setup the EPI and Hepatitis pathogens parameter descriptions search/extract criteria. Periodic reviews of the Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option for the defined EPI parameter description setups. Note: Remember that if the parameter set up needs to be changed for any of the four hepatitis entities, that a concomitant change needs to be made in the corresponding Reminders logic.

> Antimicrobial Link Update \[LREPILK\] option: This option allows the user to link the ANTIMICROBIAL SUSCEPIBILTY file (#62.06) data entries with the WKLD CODE file (#64) data entries.

> NOTE: Please see Appendix B section of this guide for instructions on “How to Link Antimicrobial Entries to Workload Code Entries” using the Antimicrobial Link Update \[LREPILK\] option.

> Lab Search/Extract Protocol Edit \[LREPI PROTOCOL EDIT\] option: Use this option to edit the LAB SEARCH/EXTRACT PROTOCOL file (#69.4).

> Lab Search/Extract Nightly Task \[LREPI NIGHTLY TASK\] option: This option must be scheduled to run each night by TaskMan. This option will build a HL7 message and send it to the defined locations specified by the EPI and Hepatitis emerging pathogens protocols. This is a stand-alone option.

## > <span id="p41" class="anchor"></span>NOTE: Patch LR\*5.2\*421 adds prompts to the Enter/Edit Local Pathogens and Laboratory Search/Extract Parameters Input screens for users to specify a code set on which to search prior to entering an ICD code. Based on this input, the system only allows either ICD-9 entry or ICD-10 entry.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Laboratory Search/Extract Parameters Input Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Prompts Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Laboratory Search/Extract Parameters Input Screen Prompts</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Laboratory Search/Extract</strong></p>
<p><strong>Parameters Input Screen</strong></p>
<p><strong>Prompt Definitions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Laboratory Test (s)</p>
</blockquote></td>
<td><blockquote>
<p>Consider these synonymous with, chemistry, serology, hematology, and “blood/serum” tests. Results anticipated to be found here would have had a test done under the chemistry/hematology accession areas, even if physically performed in microbiology and other areas. Select tests from the LABORATORY TEST file (#60).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Indicator</p>
</blockquote></td>
<td><blockquote>
<p>Select the code that will determine how to match lab results.</p>
<p>‘1’ FOR Use Reference Ranges</p>
<p>‘2’ FOR Contains</p>
<p>‘3’ FOR Greater Than</p>
<p>‘4’ FOR Less Than</p>
<p>‘5’ FOR Equal To</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Value</p>
</blockquote></td>
<td><blockquote>
<p>Positive, etc. Answer must be 1-15 characters in length. This is a Free Text field.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><span id="p421_43" class="anchor"></span>ICD-9</p>
</blockquote></td>
<td><blockquote>
<p>ICD-9 standardized code used nationwide in federal and non-federal/private health care facilities. Select from the ICD DIAGNOSIS file (#80).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICD-10</p>
</blockquote></td>
<td><blockquote>
<p>ICD-10 standardized code used nationwide in federal and non-federal/private health care facilities. Select from the ICD DIAGNOSIS file (#80).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ICD Description</p>
</blockquote></td>
<td><blockquote>
<p>Title of ICD diagnosis</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Selected Etiology</p>
</blockquote></td>
<td><blockquote>
<p>Consider synonymous with organism, final microbial diagnosis/isolate. Select from the ETIOLOGY FIELD</p>
<p>file (#61.2).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Selected SNOMED codes</p>
</blockquote></td>
<td><blockquote>
<p>Answer with SNOMED CODES</p>
<p>You may enter a new SNOMED CODE, if you wish. Answer</p>
<p>must be 1-15 characters in length.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Antimicrobial Susceptibility</p>
</blockquote></td>
<td><blockquote>
<p>Enter the Antimicrobial that will be used in screening out sensitive Etiologies (e.g., “Vancomycin” for Vancomycin Resistant Enterococcus). Select from the ANTIMICROBIAL SUSCEPTIBILITY file (#62.6).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NLT Code</p>
</blockquote></td>
<td><blockquote>
<p>Displays the associated NLT code if linked. If no NLT Code is displayed use the Antimicrobial Link Update option.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NLT Description</p>
</blockquote></td>
<td><blockquote>
<p>Displays the Description of the linked NLT code.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Topography Selection</p>
</blockquote></td>
<td><blockquote>
<p>Enter a date to screen out patients born before the date entered. Examples of Valid Dates:</p>
<p>JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057</p>
<p>T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.</p>
<p>T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Include</p>
</blockquote></td>
<td><blockquote>
<p>Selection of Topography screens all others out except the ones selected. For “ALL” leave blank. Not to be used in conjunction with the exclude Topography selection. Select from the TOPOGRAPHY file (#61).</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Laboratory Search/Extract Parameters Input Screen Prompts</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Laboratory Search/Extract</strong></p>
<p><strong>Parameters Input Screen</strong></p>
<p><strong>Prompt Definitions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Exclude</p>
</blockquote></td>
<td><blockquote>
<p>Select the Topography to screen out. Not to be used in conjunction with the Include Topography selection.</p>
<p>Select from the TOPOGRAPHY file (#61).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>First Encounter:</p>
</blockquote></td>
<td><blockquote>
<p>Limits the output to the first encounter for the patient. Otherwise list all encounters.</p>
<p>Choose: ‘1’ FOR YES</p>
<p>‘0’ FOR NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Follow PTF:</p>
</blockquote></td>
<td><blockquote>
<p>Indicates if the PTF record will be followed until a discharge has been entered.</p>
<p>Choose: ‘1’ FOR YES</p>
<p>‘0’ FOR NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Before Date Of Birth:</p>
</blockquote></td>
<td><blockquote>
<p>Enter a date to screen out patients born before the date entered. Examples of Valid Dates:</p>
<p>JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057</p>
<p>T (for TODAY), T+1 (for TOMORROW), T+2, T+7, etc.</p>
<p>T-1 (for YESTERDAY), T-3W (for 3 WEEKS AGO), etc.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>After Date Of Birth:</p>
</blockquote></td>
<td><blockquote>
<p>A birthrate to screen patients</p>
<p>(i.e., patients DOB after 1/1/1950).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Select SEX:</p>
</blockquote></td>
<td><blockquote>
<p><strong>FOR FUTURE USE ONLY.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Run Date:</p>
</blockquote></td>
<td><blockquote>
<p>Date that the last Auto Search/Extract processed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Protocol:</p>
</blockquote></td>
<td><blockquote>
<p>Defines the protocol used to define the output messages. Select from the LAB SEARCH/EXTRACT PROTOCOL file (#69.4).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Run Cycle:</p>
</blockquote></td>
<td><blockquote>
<p>Enter the date that the last Auto Search/Extract processed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Lag Days:</p>
</blockquote></td>
<td><blockquote>
<p>Defines the Lag Days parameter as 15 for all 17 emerging pathogens.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>General Description:</p>
</blockquote></td>
<td><blockquote>
<p>To review or edit the General Description prompt use the <strong>&lt;Tab&gt;</strong> key.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following information must be adhered to as recommended to ensure a successful implementation and utilization of the software.

> NOTE: It is highly recommended that the Laboratory Information Manager (LIM), a representative from the Microbiology section (director, supervisor, or technologist) and a Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) staff (or person at the facility with similar function) be assigned the Lab Search/Extract Primary Menu \[LREPI SEARCH EXTRACT MENU\]. These will be the individual(s) responsible for initially setting the Lab Search/Extract parameters descriptions and doing periodic reviews of the parameters descriptions to assure they are current.

> The Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option is used to setup local parameters for the 17 emerging pathogens. Each emerging pathogens descriptions must be reviewed prior to setting up the Lab Search/Extract parameters.

> NOTES:

> There are a number of different ways that sites have chosen to enter results into the V*IST*A database. As long as the results are in a retrievable format (straight from the V*IST*A database without additional manual input needed), how it is entered is not of significance to the Emerging Pathogen Initiative. However, two preferred methods make it easy to capture the data. Please reference the Helpful Hints section of this guide for the two preferred methods.

> Site-specific spelling or alternate spelling for data entries must be consistent to guarantee accurate data capture.

> The Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option, Lag Day parameter MUST be defined as 15 for ALL 17 emerging pathogen.

> NOTES: If a lab test needs to be entered in the parameter set up for a particular lab search/extract pathogen name (e.g. because there is more than one test result that may meet the definition), the second and subsequent tests must be placed in quotes (“ ”). Even though the “ ” marks are used to enter the data, they don't appear in the final product. This process can be done unlimited times for one set-up.

> The Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option input screen examples displays how to setup EPI parameters (i.e., including the three new Hepatitis A Antibody POS, Hepatitis B POS, and Hepatitis C Antibody NEG) pathogens. Several of the Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option input screen examples display <u>partially</u> pre-populated entries. The ETIOLOGY FIELD file (#61.2) site-specific data entries are used to <u>partially</u> pre-populate the fields in the LAB SEARCH/EXTRACT file (#69.5). However, further data entries are required for site-specific data. Additional data entries can be added or deleted to meet your site-specific needs.

> The table below lists the three new Hepatitis pathogens the and existing Hepatitis C Antibody POS emerging pathogen and the Lab Search/Extract parameter setup entries. The LAB SEARCH/EXTRACT parameter (second column) is an example as other sites may have different names for tests. Also the second column does not use the indicator mechanism of whether the result CONTAINS the POS or is EQUAL TO the POS, etc)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>LAB SEARCH/EXTRACT file (#69.5) Hepatitis emerging pathogens entries</td>
<td>LAB SEARCH/EXTRACT parameter setup entries for each Hepatitis emerging pathogens</td>
</tr>
<tr class="even">
<td>Hepatitis A Antibody NEG</td>
<td><p>HEP A ANTIBODY-TOTAL REACTIVE</p>
<p>HEP A ANTIBODY(IgM) POS</p>
<p>HEPATITIS A AB(IGG)D/C(2/99) POS</p>
<p>HEPATITIS A AB(IGG)D/C(2/99) Pos</p>
<p>HEPATITIS A AB(IGG)D/C(2/99) P</p>
<p>HEPATITIS A AB(IGG)D/C(2/99) p</p>
<p>HEP A ANTIBODY-TOTAL R</p></td>
</tr>
<tr class="odd">
<td>Hepatitis B Antibody NEG</td>
<td><p>HEP B SURFACE Ag POS</p>
<p>HEP B SURFACE AB POS</p>
<p>HEP B CORE AB(IgM) POS</p>
<p>HEP Be ANTIGEN POS</p>
<p>HEP Be ANTIGEN Pos</p>
<p>HEP Be ANTIGEN p</p>
<p>HEP Be ANTIGEN P</p></td>
</tr>
<tr class="even">
<td>Hepatitis C Antibody NEG</td>
<td><p>HEP C ANTIBODY NEG</p>
<p>HEP C ANTIBODY SEE COMMENTS</p>
<p>HEP C ANTIBODY <strong>*</strong></p>
<p>HEP C ANTIBODY <strong>#</strong></p></td>
</tr>
<tr class="odd">
<td>Hepatitis C Antibody POS</td>
<td>Hepatitis C Antibody POS</td>
</tr>
</tbody>
</table>

### Candida (Reference \#8)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Fungal infections are rising in significance especially in severely ill patients. The same is true for bloodstream infections acquired in the hospital, especially those associated with intravenous lines. Fungal bloodstream infections are increasing in prevalence.

> As a marker of bloodstream infections, the fungus *Candida* (and *Torulopsis*) has been chosen as an initial indicator organism. This organism may not be a prevalent or significant entity at your site; however, its presence is more likely to be indicative of serious or true infection than other organisms. The fungus *Candida* (and *Torulopsis)* may commonly be isolated from the blood in association with IV lines. Additionally, this yeast is more likely to be associated with nosocomial acquisition than other organisms (i.e., *Staphylococcus aureus* and coagulase negative *Staphylococcus)*, which can cause a number of community acquired syndromes not at all related to IV lines.

> All episodes of *Candida* (*Torulopsis,* yeast) isolation from blood or a blood source (central line, IV catheter tip, etc.) are being tracked. The V*IST*A Laboratory Search/Extract software has provided a partial pre-populated list of (etiologies/organisms) that fit the description for *Candida* (*Torulopsis,* yeast) to choose. These (etiologies/organisms) should be used, in addition to any site specific (etiologies/organisms) that may also fit the description.

> Example: Lab Search/Extract Parameter Setup for CANDIDA emerging pathogen

> Lab Search/Extract Primary Menu

> <span id="p421_48" class="anchor"></span>ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: Candida\<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: Candida ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> \<RET\>

> <span id="p421_49" class="anchor"></span>Department ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

> ICD Code Cd Set ICD Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: CANDIDA ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> Examples:CANDIDA

> CANDIDA GUILLIERMONDII

> CANDIDA KRUSEI

> CANDIDA PARAPSILOSIS

> CANDIDA PSEUDOTROPICALIS

> CANDIDA STELLATOIDEA

> CANDIDA TROPICALIS

> CANDIDA, NOS

> \<RET\>

> Note: During the post Init, the ETIOLOGY FIELD file (#61.2) was searched to pre-populate the Etiology field (#3) in the EMERGING PATHOGENS file (#69.5). Listed above are examples of etiology entries which may have been populated from your site’s file. Additional etiologies may be added or deleted at the <u>Selected Etiology</u> prompt to meet your site specific needs.

> Note: If spelling differences occur within your ETIOLOGY FIELD file (#61.2), be consistent with your local file and spell the results here, as it is spelled in your file (even if it is spelled differently in the example). We are concerned more importantly with data <u>recovery</u>.

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: Candida ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> Blood\<RET\>\<RET\>

> Bloodstream\<RET\>

> Catheter Tip\<RET\>

> Note: These are only suggestions. Please add accordingly to your site definition.

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: Candida ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> FIRST ENCOUNTER:\<RET\> Follow PTF:YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME:Candida ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

### Clostridium difficile (Reference \#4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Save changes before leaving form (Y/N)?Y\<RET\>

> Disease associated with the presence of *Clostridium difficile* enterotoxin A can cause significant morbidity, as well as mortality. It is of importance, as its predominant acquisition seems to occur nosocomially. Presence of Clostridial toxin (either enterotoxin A or cytotoxin L) by assay (whether it be EIA, latex agglutination, cytotoxicity of cell culture <u>+</u> neutralization, or culture of organism with subsequent colony testing) is the best indicator that an inflammatory diarrheal disease is due to presence of *Clostridium difficile*.

> Laboratory Services are quite varied as to how they identify the presence of *Clostridium difficile*. Some labs are set up to identify *C. difficile* as the final microbiological (bacterial) etiology of a culture, even if a culture method was not used. Other labs use a final etiology of “see comment” and then enter the results in a free text format. Still others enter the text under a hematology or chemistry format where a reference range and “positive” and “negative” result values can be entered. Wherever the facility lab places the results which are used to demonstrate the presence of toxin-producing *C. difficile*, we need to be able to track them (that means it must occur as a retrievable “positive” or “negative” result, or as a “bacterial etiology”). Results in a “Comments” or “Free-text” section are not acceptable.

> There are a number of different ways that sites have chosen to enter *Clostridium difficile* toxin assay results into the V*IST*A database. As long as the toxin assay results are in a retrievable format (straight from the V*IST*A database without additional manual input needed), how it is entered is not of significance to the Emerging Pathogen Initiative. However, there are two preferred methods that make it easy to capture the data. Please reference the Appendix-B section of this guide for the two methods.

> Example: Lab Search/Extract Parameter Setup for CLOSTRIDIUM DIFFICILE emerging pathogen

> Lab Search/Extract Primary Menu

> ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: CLOSTRIDIUM DIFFICILE \<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> Clostridium\<RET\> difficile toxin Contains\<RET\>Pos\<RET\>

> Note: This example is only a suggestion. Please add accordingly to your site definition.

> <span id="p421_53" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

> ICD Code Cd Set ICD Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> Clostridium difficile toxin positive\<RET\>

> Note: This is only a suggestion. Please add accordingly to your site definition.

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refres

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include \<RET\> Exclude \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> Follow PTF: YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Selected SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

### Creutzfeldt-Jakob Disease (CJD) (Reference \#13

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Creutzfeldt-Jakob Disease* (CJD*)* disease is a rare illness associated with prions. The DVA has chosen to follow this entity because of historic problems with certain blood products used in the private and public health care sectors. The data will be one of a number of ways used to identify changes in trends of incidence of this illness. This task is remarkably complex because of the long incubation period of CJD. There are no specific tests for diagnosis other than central nervous system histology combined with clinical presentation. As such, this entity is followed through ICD coding.

> Example: Lab Search/Extract Parameter Setup for CREUTZFELDT-JAKOB DISEASE emerging pathogen

> Lab Search/Extract Primary Menu

> <span id="p421_55" class="anchor"></span>ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: CREUTZFELDT-JAKOB DISEASE \<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME:CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> \<RET\>

> <span id="p421_56" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):9\<RET\>

> ICD Code Cd Set ICD Description

> 046.1 ICD-9 JAKOB-CREUTZFELDT DIS

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes\<RET\>

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter: \<RET\> Follow PTF: YES\<RET\>

> BEFORE DATE OF BIRTH: \<RET\> AFTER DATE OF BIRTH: \<RET\>

> Select SEX: \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

### Cryptosporidium (Reference \#9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The parasite *Cryptosporidium parvum* is a cause of water-borne diarrheal disease. It has gained recent prominence after evaluation of the outbreak in the greater Milwaukee area in 1993 which is estimated to have affected \<400,000 persons. In addition to affecting HIV-infected persons and young children, information exists which demonstrates that the chronically ill, elderly are also a higher risk group than the general population. Microbiology laboratory data (parasitology for most laboratories) as well as <span id="p421_58" class="anchor"></span>ICD coding is used to track this disease, both are narrowly defined parameters.

> NOTE: Microsporidiosis is a similar disease, however, the EPI does not currently wish to follow this disease process. Microsporidian etiologies should not be entered.

> NOTE: If a lab test needs to be entered in the parameter set up for a particular lab search/extract pathogen name (e.g. because there is more than one test result that may meet the definition), the second and subsequent tests must be placed in quotes (“ ”). Even though the “ ” marks are used to enter the data, they don't appear in the final product. This process can be done unlimited times for one set-up.

> Example: Lab Search/Extract Parameter Setup for CRYPTOSPORIDIUM emerging pathogen

> Lab Search/Extract Primary Menu

> <span id="p421_59" class="anchor"></span>ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: CRYPTOSPORIDIUM \<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: CRYPTOSPORIDIUM ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> \<RET\>

> <span id="p421_60" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):9\<RET\>

> ICD Code Cd Set ICD Description

> 007.8 ICD-9 PROTOZOAL INTEST DIS N

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: CRYPTOSPORIDIUM ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> Cryptosporidium\<RET\>

> Note: If Cryptosporidium is reported under parasitology, add Cryptosporidium species at the Etiology prompt.

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: CRYPTOSPORIDIUM ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: CRYPTOSPORIDIUM ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> Follow PTF: YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: CRYPTOSPORIDIUM ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date: Protocol: LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

### Dengue (Reference \#12)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The mosquito-borne disease of Dengue Hemorrhagic Fever is a rare but re-emerging infection, especially in the Caribbean. The VA has seen cases of Dengue Hemorrhagic Fever over the last several years. Most of these cases have been in Dengue endemic areas served by the VA. However, as our society becomes more mobile, and the area of Dengue endemncity expands, more cases are likely to occur. Because microbiologic culture is not routinely done and serology can be difficult to track, initially <span id="ICDM9toICD4" class="anchor"></span>ICD coded diagnoses are used to track this entity.

> Example: Lab Search/Extract Parameter Setup for DENGUE emerging pathogen

> Lab Search/Extract Primary Menu

> ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: DENGUE \<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: DENGUE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> \<RET\>

> <span id="p421_63" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):9\<RET\>

> ICD Code Cd Set ICD Description

> 061\. ICD-9 DENGUE

> 065.4 ICD-9 MOSQUITO-BORNE HEM FEVER

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: DENGUE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Etiology Selected Snomed Codes

> \<RET\>

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: DENGUE ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: DENGUE ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter: \<RET\> Follow PTF: YES \<RET

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: DENGUE ACTIVE YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

### E. coli O157:H7 (Reference \#10)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Escherichia coli* serotype O157 (*E. coli* O157) has gained prominence as a food-borne illness with potentially life threatening complications coming from the associated Hemolytic Uremic Syndrome. Not all sites routinely culture for the presence of *E. coli* O157 in stool specimens submitted for culture. In addition, *E. coli* O157 is not a microbiologic (bacterial) etiology pre-existing in the most recent - national microbiology lab package. In order to nationally track cultures positive for this organism, each site will need to make an etiology specific for *E-coli* O157 (e.g. *Escherichia coli* O157, *E. coli* O157, *E. coli* serotype O157, etc.). Some sites have already done this and will not need to generate a new entry.

> NOTE: Entering *Escherichia coli* or *E. coli* from the bacterial etiology and then entering “serotype O157” or “O157”, under the “Comments” or “Free Text” section is not acceptable, as it will not allow the data to be retrieved nationally.

> All subsequent positive cultures for this organism must then be entered under the new etiology.

> Other serotypes of *E. coli* will also cause disease, but we will not currently track these as O157 causes by far, the majority of cases of interest for the national database.

> The EPI criteria is dependent on your site. If your site already has an etiology that will select positive cultures for *E. coli* O157, then enter that etiology. However, if your site had to enter a new etiology to accommodate the EPI criteria, be sure to enter this new etiology here.

> NOTE: If a lab test needs to be entered in the parameter set up for a particular lab search/extract pathogen name (e.g. because there is more than one test result that may meet the definition), the second and subsequent tests must be placed in quotes (“ ”). Even though the “ ” marks are used to enter the data, they don't appear in the final product. This process can be done unlimited times for one set-up.

> Example: Lab Search/Extract Parameter Setup for E. COLI 0157:H7

> Lab Search/Extract Primary Menu

> <span id="p421_66" class="anchor"></span>

> ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: E. COLI 0157:H7 \<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: E. COLI 0157:H7 ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> \<RET\>

> <span id="p421_67" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):9\<RET\>

> ICD Code Cd Set ICD Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: E. COLI 0157:H7 ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology

> Example: Escherichia coli O157\<RET\>

> Note: Entering *Escherichia coli* or *E. coli* from the bacterial etiology and then entering “serotype O157” or “O157”, under the Comments section or in

> free text is not acceptable as it will not allow the data to be retrieved nationally).

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: E. COLI 0157:H7 ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: E. COLI 0157:H7 ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> Follow PTF:YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: E. COLI 0157:H7 ACTIVE YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

### Hepatitis A Antibody Positive (Reference \#16)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> One of the goals of the Healthy People 2000 and 2010 initiatives of the Department of Health and Human Services is to decrease certain infectious diseases, especially those that are vaccine preventable. Acute infection with Hepatitis A is one such disease that has specific objectives present in the Healthy People objectives.

> The purpose of surveillance for this disease is to record all cases as diagnosed by the laboratory. A positive laboratory test for the presence of Hepatitis A virus is needed. Usually this criterion is met by presence of antibodies to the Hepatitis A virus. In particular, the IgM antibody against hepatitis A is the test most commonly used for determining acute hepatitis A infection. There are other antibody tests available for Hepatitis A. These tests usually indicate past infection with hepatitis A (or in some circumstances may indicate evidence of previous vaccination); usually the IgG antibody against Hepatitis A, OR the Total antibody against Hepatitis A (a test that does not discriminate between IgM or IgG, but can show evidence of exposure) are the tests done for this purpose.

> What we are looking for is evidence of presence of any antibody to Hepatitis A, whether it is recorded as “weakly positive,” “strongly positive,” “positive,” or “present.” If other phrases are used to describe a test result, one should be able to differentiate responses upon entry into the program. As an example, the words “present” and “not present” might be used to designate “positive” vs. “negative”, however, they would not allow retrieval of only the positive cases as both phrases contain the word, “present.” Also, numerical values of results (e.g. at titer value) are not readily useable. Therefore, parameters for this are to be laboratory based and should include all tests for antibodies against hepatitis A (see examples above).

> Also, some institutions will use ICD-9 coding and problem lists as a means to abstract data on this disease. DO NOT use these methods for this particular program. We are only abstracting laboratory confirmed cases of antibodies against Hepatitis A.

> NOTE: If a lab test needs to be entered in the parameter set up for a particular lab search/extract pathogen name (e.g. because there is more than one test result that may meet the definition), the second and subsequent tests must be placed in quotes (“ ”). Even though the “ ” marks are used to enter the data, they don't appear in the final product. This process can be done unlimited times for one set-up.

> Example: Lab Search/Extract Parameter Setup HEPATITIS A ANTIBODY POS pathogen

> Lab Search/Extract Primary Menu

> <span id="p421_70" class="anchor"></span>ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: HEPATITIS A ANTIBODY POS \<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: HEPATITIS A ANTIBODY POS ACTIVE: NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> HEP A ANTIBODY-TOTAL\<RET\> Equal To\<RET\> REACTIVE\<RET\>

> HEP A ANTIBODY(IgM)\<RET\> Contains\<RET\> POS\<RET\>

> HEPATITIS A AB(IGG)D/C(2/99)\<RET\> Contains\<RET\> POS\<RET\>

> “HEPATITIS A AB(IGG)D/C(2/99)”\<RET\> Contains\<RET\> Pos\<RET\>

> “HEPATITIS A AB(IGG)D/C(2/99)”\<RET\> Contains\<RET\> P\<RET\>

> “HEPATITIS A AB(IGG)D/C(2/99)”\<RET\> Contains\<RET\> p\<RET\>

> “HEP A ANTIBODY-TOTAL”\<RET\> Equal To\<RET\> R\<RET\>

> Note: Enter the appropriate test for your site, and how the results are reported.

> <span id="p421_71" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

> ICD Code Cd Set ICD Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: HEPATITIS A ANTIBODY POS ACTIVE: NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> \<RET\>

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: HEPATITIS A ANTIBODY POS ACTIVE: NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: HEPATITIS A ANTIBODY POS ACTIVE: NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> Follow PTF:YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: HEPATITIS A ANTIBODY POS ACTIVE NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> Save changes before leaving form (Y/N)?Y\<RET\>

### Hepatitis B Positive (Reference \#17)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> One of the goals of the Healthy People 2000 and 2010 initiatives of the Department of Health and Human Services is to decrease certain infectious diseases, especially those that are vaccine preventable. Acute and chronic infection with Hepatitis B is one such disease that has specific objectives present in the Healthy People objectives.

> Both acute and chronic diseases have significant morbidity and can contribute to mortality. Further, infection with hepatitis B can complicate the medical course of persons with other liver ailments. As such, surveillance for both acute and chronic disease is important. In order for the VHA to do surveillance for these diseases, we are looking for laboratory evidence of infection with hepatitis B. This laboratory evidence of infection includes the following standard serological markers:

1.  Presence of the Hepatitis B surface antigen
2.  Presence of antibodies against the Hepatitis B core antigen (in particular, the IgM antibody)
3.  Presence of antibodies against the Hepatitis B surface antigen

> 4\. Presence of the hepatitis B e antigen.

> These are not all of the tests that can be done for hepatitis B, but they are the ones likely to pick up acute cases (new) or those chronic cases that are likely to be infectious to other persons. Please list only those tests at your facility that are in keeping with what we are looking for—acute cases, or those cases likely to be infectious to others.

> NOTE: There are advanced PCR based tests that can measure amount of virus in the bloodstream; these are not done at all sites and have not yet been FDA approved. As such, these PCR tests should not be used for case determination.

> NOTE: If a lab test needs to be entered in the parameter set up for a particular lab search/extract pathogen name (e.g. because there is more than one test result that may meet the definition), the second and subsequent tests must be placed in quotes (“ ”). Even though the “ ” marks are used to enter the data, they don't appear in the final product. This process can be done unlimited times for one set-up.

> Example: Lab Search/Extract Parameter Setup for HEPATITIS B POS pathogen

> Lab Search/Extract Primary Menu

> <span id="p421_74" class="anchor"></span>ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: HEPATITIS B POS\<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: HEPATITIS B POS ACTIVE: NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> HEP B SURFACE Ag\<RET\> Contains\<RET\> POS\<RET\>

> HEP B SURFACE AB\<RET\> Contains\<RET\> POS\<RET\>

> HEP B CORE AB(IgM)\<RET\> Contains\<RET\> POS\<RET\>

> HEP Be ANTIGEN\<RET\> Contains\<RET\> POS\<RET\>

> “HEP Be ANTIGEN”\<RET\> Contains\<RET\> Pos\<RET\>

> “HEP Be ANTIGEN”\<RET\> Contains\<RET\> p\<RET\>

> “HEP Be ANTIGEN”\<RET\> Contains\<RET\> P\<RET\>

> Note: Enter the appropriate test for your site, and how the results are reported.

> <span id="p421_75" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

> ICD Code Cd Set ICD Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: HEPATITIS B POS ACTIVE: NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> \<RET\>

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: HEPATITIS B POS ACTIVE: NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: HEPATITIS B POS ACTIVE: NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> Follow PTF:YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: HEPATITIS B POS ACTIVE NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> Save changes before leaving form (Y/N)?Y\<RET\>

### Not Positive for Hepatitis C Antibody OR Hepatitis C Antibody Neg (Reference \#15)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The first version of the EPI gathered data on persons who were positive for antibody against Hepatitis C. This version will continue to gather such data. However, there are many cases, and it is important to try to find out what differences there are in those persons who are positive for Hepatitis C antibody as opposed to those who do not have Hepatitis C antibody present. Therefore, please review those results that you have designated to be place into the Hepatitis C Antibody Positive portion of the EPI. Be sure that they truly meet the definition, as noted in Lab Search/Extract Patch LR\*5.2\*175 Technical and User Guide (distributed August 1998).

> All the results of Hepatitis C antibody testing that are not considered “positive” should be reported in this area. Therefore, all of the hepatitis C results that your facility reports should be mapped to either the hepatitis C Antibody Positive file or the Not Positive for Hepatitis C Antibody File. Not positive terms may include “negative,” “indeterminant,” “indeterminate,” “undetectable.” As with the Hepatitis C Antibody Positive component, be sure that phrases that truly differentiate results are used (e.g. the results of “present” and “not present” are not truly differentiated by computer retrieval as both contain the word “present”).

> NOTE: There are PCR based tests utilized for Hepatitis C. These tests are not used at all facilities and are not yet FDA approved for identification of hepatitis C disease. As such, they should not be used for reporting purposes with this iteration of EPI.

> NOTE: If a lab test needs to be entered in the parameter set up for a particular lab search/extract pathogen name (e.g. because there is more than one test result that may meet the definition), the second and subsequent tests must be placed in quotes (“ ”). Even though the “ ” marks are used to enter the data, they don't appear in the final product. This process can be done unlimited times for one set-up.

> Example: Lab Search/Extract Parameter Setup for HEPATITIS C ANTIBODY NEG pathogen

> Lab Search/Extract Primary Menu

> <span id="p421_78" class="anchor"></span>ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: HEPATITIS C ANTIBODY NEG\<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: HEPATITIS C ANTIBODY NEG ACTIVE: NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> HEP C ANTIBODY\<RET\> Contains\<RET\> NEG\<RET\>

> “HEP C ANTIBODY”\<RET\> Contains\<RET\> SEE COMMENTS\<RET\>

> “HEP C ANTIBODY”\<RET\> Contains\<RET\> \*\<RET\>

> “HEP C ANTIBODY”\<RET\> Contains\<RET\> \#\<RET\>

> Note: Enter the appropriate test for your site, and how the results are reported.

> <span id="p421_79" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

> ICD Code Cd Set ICD Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: HEPATITIS C ANTIBODY NEG ACTIVE: NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> \<RET\>

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: HEPATITIS C ANTIBODY Neg ACTIVE: NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: HEPATITIS C ANTIBODY NEG ACTIVE: NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> Follow PTF:YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: HEPATITIS C ANTIBODY NEG ACTIVE NO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> Save changes before leaving form (Y/N)?Y\<RET\>

### Hepatitis C Antibody Positive (Reference \#2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Hepatitis C is much more prevalent than originally thought at least in certain key patient sub-populations. As new and more sensitive assays come into use, we seem to find more evidence of this pathogen. We are looking for evidence of exposure to Hepatitis C in patients as demonstrated by Hepatitis C antibody positivity. The need for confirmatory testing or demonstration of active disease is not currently necessary in gathering data for this program. Different facilities may use different assays for this test. What we are looking for is evidence of presence of antibody to Hepatitis C, whether it be recorded as “weakly positive”, “strongly positive”, “positive”, or “present”. If other phrases are used to describe a test result, one should be able to differentiate the results upon entry into the program. As an example, the words, “present” “and “not present” would not allow retrieval of only positive cases as both phrases contain the word, “present”.

> NOTE: There are PCR based tests utilized for Hepatitis C. These tests are not used at all facilities and are not yet FDA approved for identification of hepatitis C disease. As such, they should not be used for reporting purposes with this iteration of EPI.

> Example: Lab Search/Extract Parameter Setup for Hepatitis C Antibody POS pathogen.

> Lab Search/Extract Primary Menu

> <span id="p421_82" class="anchor"></span>ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: HEPATITIS C ANTIBODY POS \<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: HEPATITIS C ANTIBODY POS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> HEPATITIS C ANTIBODY\<RET\> Contains\<RET\>POS\<RET\>

> Note: Enter the appropriate test for your site, and how the results are reported.

> <span id="ICD_Hep_C_POS_2" class="anchor"></span>

> ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

> ICD Code Cd Set ICD Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: HEPATITIS C ANTIBODY POS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> \<RET\>

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: HEPATITIS C ANTIBODY POS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: HEPATITIS C ANTIBODY POS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> Follow PTF:YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: HEPATITIS C ANTIBODY POS ACTIVE YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> Save changes before leaving form (Y/N)?Y\<RET\>

### Legionella (Reference \#7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Since the American Legion Convention in Philadelphia in the 1970’s, Legionnaires’ Disease has been an illness of keen interest to the DVA. Because diagnosis is complex, we have chosen to review for presence of *Legionella* in culture and in ICD DIAGNOSIS file (#80). We will not look at *Legionella* direct fluorescent antibody positivity because of the potential high false positivity of this test. Likewise, serology is not easy to interpret or easily extracted from the V*IST*A database for our purposes and will not be included as a marker in this first iteration of the EPI program. Because it is not yet approved, the newer test of *Legionella* urinary antigen will not be used either. The Selected Etiology screen display has been partially pre-populated.

> Lab Search/Extract Primary Menu

> <span id="p421_85" class="anchor"></span>ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: LEGIONELLA\<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: LEGIONELLA ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> \<RET\>

> <span id="p421_86" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):9\<RET\>

> ICD Code Cd Set ICD Description

> 482.80 ICD-9 LEGIONNARIE’S DISEASE

> 482.84 ICD-9 LEGIONNARIE’S DISEASE

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: LEGIONELLA ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology

> Examples:LEGIONELLA BOZEMANII

> LEGIONELLA DUMOFFII

> LEGIONELLA GORMANII

> LEGIONELLA JORDANIS

> LEGIONELLA LONGBEACHAE

> LEGIONELLA MICDADEI

> LEGIONELLA OAKRIDGENSIS

> LEGIONELLA PNEUMOPHILIA

> LEGIONELLA SP

> LEGIONELLA WADSWORTHII

> \<RET\>

> Note: During the post Init, the ETIOLOGY FIELD file (#61.2) was searched to pre-populate the Etiology field (#3) in the EMERGING PATHOGENS file (#69.5). Listed above are examples of etiology entries which may have been populated from your site’s file. Additional etiologies may be added or deleted at the <u>Selected Etiology</u> prompt to meet your site-specific needs.

> Note: If spelling differences occur within your ETIOLOGY FIELD file (#61.2) be consistent with your local file and spell the results here, as it is spelled in your file (even if it is spelled differently in the example). We are concerned more importantly with data <u>recovery</u>.

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: LEGIONELLA ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\>\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: LEGIONELLA ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> Follow PTF: YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: E. LEGIONELLA ACTIVE YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

### Leishmaniasis (Reference \#14)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Leishmaniasis is a significant tropical disease that can cause serious complications. It is of interest to the Department of Veterans Affairs as Leishmania has caused illness among military personnel for many years. In addition, the Persian Gulf War occurred in an area of the world where the parasite is endemic. Because no simple, straightforward serology exists and no standard culture techniques exist, we have chosen to follow this entity through <span id="p421_88" class="anchor"></span>ICD diagnosis codes.

> Example:

> Lab Search/Extract Primary Menu

> ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: LEISHMANIASIS \<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: LEISHMANIASIS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> \<RET\>

> <span id="p421_89" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):9\<RET\>

> ICD Code Cd Set ICD Description

> 085.0 ICD-9 VISCERAL LEISHMANIASIS

> 085.1 ICD-9 CUTAN LEISHMANIAS URBAN

> 085.2 ICD-9 CUTAN LEISHMANIAS ASIAN

> 085.3 ICD-9 CUTAN LEISHMANIAS ETHIOP

> 085.4 ICD-9 CUTAN LEISHMANIAS AMER

> 085.5 ICD-9 MUCOCUTAN LEISHMANIASIS

> 085.9 ICD-9 LEISHMANIASIS NOS

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: LEISHMANIASIS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> \<RET\>

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: LEISHMANIASIS ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: LEISHMANIASIS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> FOLLOW PTF:YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: E. LEISHMANIASIS ACTIVE YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

### Malaria (Reference \#11)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The plasmodial parasite is responsible for the blood-borne disease of malaria. Malaria can cause acute as well as chronic, relapsing disease. Occasionally, U.S. troops are deployed in malaria endemic areas. This placement could potentially put troops at risk for acquiring this disease. For the Emerging Pathogens Initiative program, we are interested in tracking patients with malaria, either acute or chronic, relapsing, and in either inpatient or outpatient status. No standardized serologic test allows for easy identification. Since not all sites consistently code and record malarial parasites seen histologically or on blood smears (not all of these interpretations are done through the Pathology and Laboratory Service), we have currently decided to track malaria based on <span id="p421_91" class="anchor"></span>ICD coding.

> Example:

> Lab Search/Extract Primary Menu

> ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: MALARIA\<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: MALARIA ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> \<RET\>

> <span id="p421_92" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):9\<RET\>

> ICD Code Cd Set ICD Description

> 084.0 ICD-9 FALCIPARUM MALARIA

> 084.1 ICD-9 VIVAX MALARIA

> 084.2 ICD-9 QUARTAN MALARIA

> 084.3 ICD-9 OVALE MALARIA

> 084.4 ICD-9 MALARIA NEC

> 084.5 ICD-9 MIXED MALARIA

> 084.6 ICD-9 MALARIA NOS

> 084.7 ICD-9 INDUCED MALARIA

> 084.8 ICD-9 BLACKWATER FEVER

> 084.9 ICD-9 MALARIA COMPLICATED NEC

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: MALARIA ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> \<RET\>

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: MALARIA ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: MALARIA ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> FOLLOW PTF:YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Selected SEX:\<RET\>

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: MALARIA ACTIVE YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> Save changes before leaving form (Y/N)?Y\<RET\>

### Penicillin- Resistant Pneumococcus (Reference \#3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The emergence of antibiotic resistance in microbial agents is of great interest and concern for health care. Penicillin (PCN) was once the mainstay of therapy for *Streptococcuspneumoniae* infections but resistance to this agent is becoming more prominent. Different therapeutic strategies need to be developed once the prevalence of PCN-resistant *S. pneumoniae* reaches a critical threshold in a community. In order to monitor this, we are looking for the presence of any resistance in the pneumococci (either “moderate/intermediate” or “frank/high” level resistance). As such, any *S. pneumoniae* which is not fully susceptible to PCN on PCN susceptibility testing should be recorded.

> Example:

> Lab Search/Extract Primary Menu

> <span id="p421_94" class="anchor"></span>ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: PEN-RES PNEUMOCOCCUS \<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: PEN-RES PNEUMOCOCCUS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> \<RET\>

> <span id="ICD_Pneu_2" class="anchor"></span>

> ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

> ICD Code Cd Set ICD Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: \<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: PEN-RES PNEUMOCOCCUS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> NOTE: You may enter a new ETIOLOGY, if you wish.

> STREPTOCOCCUSPNEUMONIAE 12

> Are you adding 'STREPTOCOCCUS PNEUMONIAE' as

> a new ETIOLOGY (the 1ST for this EMERGING PATHOGENS)?Y\<RET\>

> Antimicrobial Susceptibility NLT Code NLT Description

> Penicillin\<RET\>

> Are you adding ' Penicillin ' as

> a new Antimicrobial Susceptibility (the 1ST for this EMERGING PATHOGENS)?Y \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: \<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: PEN-RES PNEUMOCOCCUS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: PEN-RES PNEUMOCOCCUS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> FOLLOW PTF:YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Selected SEX:\<RET\>

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: PEN-RES PNEUMOCOCCUS ACTIVE YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

### Streptococcus-Group A (Reference \#6)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Streptococcus-*Group A can be associated with or cause significant disease such as severe fasciitis and streptococcal toxic shock syndrome. We are especially interested to find out how much severe/deep seated disease the VA is experiencing, but other disease entities are of interest also. To this end, we are looking for all episodes of culture positivity for *Streptococcus-*Group A, regardless of site and regardless of inpatient or outpatient status of the person from whom the specimen is obtained. We are aware that some sites may use rapid screenings for *Streptococcus-*Group A, especially from pharyngeal sources. These rapid screens may be difficult to capture, so we are not asking for them on this first iteration of the EPI program.

> Example:

> Lab Search/Extract Primary Menu

> <span id="p421_97" class="anchor"></span>ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: STREPTOCOCCUS-GROUP A \<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: STREPTOCOCCUS-GROUP A ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> \<RET\>

> <span id="ICD_Strep_2" class="anchor"></span>

> ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

> ICD Code Cd Set ICD Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: STREPTOCOCCUS-GROUP A ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> STREPTOCOCCUS-GROUP A\<RET\>

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: STREPTOCOCCUS-GROUP A ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\>\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: STREPTOCOCCUS-GROUP A ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> FOLLOW PTF:YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: STREPTOCOCCUS-GROUP A ACTIVE YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

### Tuberculosis (Reference \#5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Mycobacterium tuberculosis* infection is an important public health concern. Recent increases in incidence of disease, and occurrence of multiply-drug resistant strains in outbreak situations along with the increased susceptibility of HIV-infected persons for this disease has generated renewed interest in this entity. Since the national data show that 80-85% of all reported active tuberculosis cases are culture positive (with acid fast bacilli smear-only positive cases increasing the reporting by 2-5% more) we have decided to use culture positivity for *Mycobacterium tuberculosis* to track tuberculosis infections in the current iteration of the EPI software application. Information regarding susceptibility will be tracked as well. For the national EPI program, there will be no need to enter specific antimycobacterial agents to be tracked; it will be done automatically. <span id="p421_100" class="anchor"></span>ICD coding is complex and confusing for many cases of tuberculosis and therefore will not be used.

> Lab Search/Extract Primary Menu

> ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: TUBERCULOSIS\<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: TUBERCULOSIS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> \<RET\>

> <span id="p421_101" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

> ICD Code Cd Set ICD Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME:TUBERCULOSIS ACTIVE:YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> Mycobacterium tuberculosis\<RET\>

> Antimicrobial Susceptibility NLT Code NLT Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: TUBERCULOSIS ACTIVE:YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: TUBERCULOSIS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> FOLLOW PTF:YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: TUBERCULOSIS ACTIVE YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

### Vancomycin-Resistant Enterococcus (VRE) (Reference \#1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Vancomycin-Resistant Enterococcus (VRE) is a pathogen of increasing importance. Not only can it cause significant disease, but also it can be spread within facilities. It is important to capture all positive cultures for VRE (not just disease). As such, all positive cultures for VRE will be reported.

> Note: This includes cultures positive for prevalence and surveillance review, including specimens of stool and rectal swabs.

> Vancomycin-resistant *Enterococcus faecalis* and *E. faecium* are most common, but we wish to look at all vancomycin resistant enterococci whether speciated or not. Therefore, it is important to be sure to list all the places in the Micro Lab package where *Enterococcus* are found, either as *Enterococcus*, *E. (sp.),* Group D-*Streptococcus*, *E. faecalis*, *E. faecium*, *E. durans*, *E. gallinarum*, *E. casseliflavus*, etc.

> NOTE: Only a partial pre-populated Etiology list is shown in the screen display example at the <u>Selected Etiology</u> prompt. Please be sure to review the entire Etiology list. If you have other etiology results at your site, they can be added to this Etiology list. Again, if alternate spellings are present in your site’s ETIOLOGY FIELD file (#61.2), be certain those spellings assure capture of all data points possible.

> Example:

> Lab Search/Extract Primary Menu

> <span id="p421_104" class="anchor"></span>ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

> Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

> Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

> Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

> Choose from:

> CANDIDA

> CLOSTRIDIUM DIFFICILE

> CREUTZFELDT-JAKOB DISEASE

> CRYPTOSPORIDIUM

> DENGUE

> E. COLI 0157:H7

> HEPATITIS A ANTIBODY POS

> HEPATITIS B POS

> HEPATITIS C ANTIBODY NEG

> HEPATITIS C ANTIBODY POS

> LEGIONELLA

> LEISHMANIASIS

> MALARIA

> NCH CHOLESTEROL

> NCH PAP SMEAR

> PEN-RES PNEUMOCOCCUS

> STREPTOCOCCUS GROUP A

> TUBERCULOSIS

> VANC-RES ENTEROCOCCUS

> Select LAB SEARCH/EXTRACT NAME: VANC-RES ENTEROCOCCUS \<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

> NAME: VANC-RES ENTEROCOCCUS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Laboratory Test(s) Indicator Value

> \<RET\>

> ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

> ICD Code Cd Set ICD Description

> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: VANC-RES ENTEROCOCCUS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology Selected Snomed Codes

> Examples:Enterococcus

> Enterococcus (Strept. faecalis-Group D)

> Streptococcus faecalis Enterococcus durans

> Streptococcus faecium Streptococcus sp. Group D

> Enterococcus avium

> Enterococcus avium - (Group D)

> Enterococcus casseliflavus

> Enterococcus faecalis

> Enterococcus gallinarum

> Enterococcus malodoratus Enterococcus

> Enterococcus hirae solitarius

> Enterococcus mundtii Enterococcus

> Enterococcus raffinosus pseudoavium

> Enterococcus sp. Enterococcus faecium

> Enterococcus species Enterococcus durans

> \<RET\>

> Note: During the post Init, the ETIOLOGY FIELD file (#61.2) was searched to pre-populate the Etiology field (#3) in the EMERGING PATHOGENS file (#69.5). Listed above are examples of etiology entries which may have been populated from your site’s file. Additional etiologies may be added or deleted at the <u>Selected Etiology</u> prompt to meet your site specific needs.

> Note: If spelling differences occur within your ETIOLOGY FIELD file (#61.2) be consistent with your local file and spell the results here, as it is spelled in your file (even if it is spelled differently in the example). We are concerned more importantly with data <u>recovery</u>.

> Antimicrobial Susceptibility NLT Code NLT Description

> VANCOMYCIN\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

> NAME: VANC-RES ENTEROCOCCUS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Topography Selection

> Include Exclude

> \<RET\> \<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: N\<RET\> Press \<PF1\>H for help Insert

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

> NAME: VANC-RES ENTEROCOCCUS ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> First Encounter:\<RET\> FOLLOW PTF:YES\<RET\>

> BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

> Select SEX:\<RET\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

> NAME: VANC-RES ENTEROCOCCUS ACTIVE YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Run Date:\<RET\> Protocol:LREPI\<RET\>

> Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

> General Description:\<TAB\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> COMMAND: E\<RET\> Press \<PF1\>H for help Insert

> Save changes before leaving form (Y/N)?Y\<RET\>

## Conclusion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once you have finished entering the information as directed by the National Infectious Diseases Program Office, these fields should not be changed again except for the following conditions:

> 1\. As requested nationally via the Veterans Affairs Headquarters (VAHQ) Infectious Disease Program Office to update, modify, add, or delete data from the existing files used by the Laboratory Search/Extract software or an addition of a new entity to be tracked.

> 2\. The yearly review must ensure that the entry is acceptable and to update the EPI files with any changes in etiology, lab tests or results parameters that may have occurred locally at the site during the previous year.

> Annually the EPI national program materials should be reviewed by the VAMCs and updated. It is suggested that this review occur in February of each year. If no changes have occurred in lab practices, etiologies, sites, or results parameters leave the information as is until the next review period. If changes <u>did</u> occur, then enter them as appropriate in order to capture the data requested for each EPI national entity (disease/organism) to be tracked.

> As entities (diseases/organisms) are no longer to be tracked nationally (“dropped from the list”), or a new entity is to be tracked (“added to the list”), revision will be forwarded to the sites to assist in updating your site files.

> NOTE: Remember that if the parameter set up needs to be changed for any of the four hepatitis entities, that a concomitant change needs to be made in the corresponding Reminders logic.

APPENDIX-A

EDITING FILES, LINKING DATA, EDITING SCREENS, WORKLOAD AND SUFFIXES CODES REQUEST FORM

*(This page included for two-sided copying.)*

# Editing/Printing Files, Screens, Linking Data, Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section contains instructions for editing files, printing, linking data, and a Workload and Suffix Code Request Form used for requesting additional Workload and Suffix Codes.

## Editing TOPOGRAPHY file (#61)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Specific HL7 codes must be added to the TOPOGRAPHY file (#61). The HL7 Code field (#08) in this file is used to add the entries. Specific HL7 codes that must be added to TOPOGRAPHY file (#61) is located in the HL7 section of this guide, Table 0070 (Specimen Source Codes). The following is an example of how to add the specific HL7 codes to the TOPOGRAPHY file (#61) using VA FileMan - Enter Or Edit File Entries option.

Example: How to add specific HL7 codes to TOPOGRAPHY file (#61)

> Select OPTION: ENTER OR EDIT FILE ENTRIES\<RET\>

> INPUT TO WHAT FILE: TOPOGRAPHY FIELD//\<RET\>

> EDIT WHICH FIELD: ALL// .08 HL7 CODE\<RET\>

> THEN EDIT FIELD:\<RET\>

> Select TOPOGRAPHY FIELD NAME: ? \<RET\>

> Answer with TOPOGRAPHY FIELD NAME, or SNOMED CODE, or ABBREVIATION, or

> SYNONYM

> Do you want the entire 8575-Entry TOPOGRAPHY FIELD List? NO\<RET\>

> You may enter a new TOPOGRAPHY FIELD, if you wish

> ANSWER MUST BE 2-80 CHARACTERS IN LENGTH

> Select TOPOGRAPHY FIELD NAME: AMNIOTIC FLUID 8Y300

> HL7 CODE: ? \<RET\>

> Answer must be 2-4 characters in length.

> Enter the two to four character code from the left column:

> ABS ABCs

> AMN Amniotic fluid

> ASP Aspirate

> BPH Basophils

> ABLD Blood arterial

> BBL Blood bag

> BON Bone

> BRTH Breath

> BRO Bronchial

> BRN Burn

> HL7 CODE: AMN\<RET\>

## Printing LAB SEARCH/EXTRACT file (#69.5) Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please use the following VA FileMan print examples to capture your local sites definitions from the LAB SEARCH/EXTRACT file (#69.5).

Example:

> VA FileMan 22.0

> Select OPTION: 2 PRINT FILE ENTRIES\<RET\>

> OUTPUT FROM WHAT FILE: REMINDER TERM// LAB SEARCH\<RET\>

> 1 LAB SEARCH/EXTRACT (19 entries)

> 2 LAB SEARCH/EXTRACT PROTOCOL (2 entries)

> CHOOSE 1-2: 1\<RET\> LAB SEARCH/EXTRACT (19 entries)

> SORT BY: NAME//\<RET\>

> START WITH NAME: FIRST// HEPATITIS\<RET\>

> GO TO NAME: LAST// HEPATITIS Z\<RET\>

> WITHIN NAME, SORT BY:

> FIRST PRINT FIELD: ? \<RET\>

> Answer with FIELD NUMBER, or LABEL

> Do you want the entire 21-Entry FIELD List? Y\<RET\> (Yes)

> Choose from:

> .01 NAME

> .05 REFERENCE NUMBER

> 1 ACTIVE

> 2 LAB TEST (multiple)

> 3 ETIOLOGY (multiple)

> <span id="p421_111" class="anchor"></span>4 ICD DIAGNOSIS (multiple)

> 5 ANTIMICROBIAL SUSCEPTIBILITY (multiple)

> 6 INCLUDED SITES (multiple)

> 7 EXCLUDED SITES (multiple)

> 8 SNOMED CODES (multiple)

> 9 RUN DATE

> 10 CYCLE

> 10.5 LAG DAYS

> 11 FIRST ENCOUNTER

> 12 PROTOCOL

> 13 FOLLOW PTF

> 14 PTF (multiple)

> 15 Description (word-processing)

> 16 SEX

> 17 BEFORE DATE OF BIRTH

> 18 AFTER DATE OF BIRTH

> ^

> TYPE '&' IN FRONT OF FIELD NAME TO GET TOTAL FOR THAT FIELD,

> '!' TO GET COUNT, '+' TO GET TOTAL & COUNT, '#' TO GET MAX & MIN,

> '\]' TO FORCE SAVING PRINT TEMPLATE

> TYPE '\[TEMPLATE NAME\]' IN BRACKETS TO USE AN EXISTING PRINT TEMPLATE

> YOU CAN FOLLOW FIELD NAME WITH ';' AND FORMAT SPECIFICATION(S)

> FIRST PRINT FIELD: .01;C1;L30 NAME\<RET\>

> THEN PRINT FIELD: ACTIVE;C35;L5\<RET\>

> THEN PRINT FIELD: LAG DAYS;C45;L5\<RET\>

> THEN PRINT FIELD: LAB TEST (multiple)\<RET\>

> THEN PRINT LAB TEST SUB-FIELD: .01;C5;L30 LAB TEST\<RET\>

> THEN PRINT LAB TEST SUB-FIELD: INDICATOR;C38;L15\<RET\>

> THEN PRINT LAB TEST SUB-FIELD: INDICATED VALUE;C55;L23\<RET\>

> THEN PRINT LAB TEST SUB-FIELD: \<RET\>

> THEN PRINT FIELD: \<RET\>

> Heading (S/C): LAB SEARCH/EXTRACT LIST Replace L With site name_L

> Replace site name_LAB SEARCH/EXTRACT LIST

> STORE PRINT LOGIC IN TEMPLATE:

> START AT PAGE: 1//

> DEVICE: ;;999999 WAN Right Margin: 80//\<RET\>

> site name_LAB SEARCH/EXTRACT LIST AUG 18,2000 12:21 PAGE 1

> LAG

> NAME ACTIVE DAYS

> LAB TEST INDICATOR INDICATED VALUE

> ----------------------------------------------------------------------------

> HEPATITIS A ANTIBODY POS NO 15

> HEP A ANTIBODY-TOTAL Equal To Reactive

> HEP A ANTIBODY(IgM)

> HEP A ANTIBODY(IgM) Contains POS

> HEPATITIS A AB(IGG)D/C(2/99) Contains POS

> HEPATITIS A AB(IGG)D/C(2/99) Contains Pos

> HEPATITIS A AB(IGG)D/C(2/99) Contains p

> HEPATITIS A AB(IGG)D/C(2/99) Equal To Reactive

> HEPATITIS A AB(IGG)D/C(2/99) Contains p

> HEPATITIS A AB(IGG)D/C(2/99) Equal To Pos

> HEPATITIS B POS NO 15

> HEP B SURFACE Ag Contains POS

> HEP B SURFACE AB Contains POS

> HEP B CORE AB(IgM) Contains POS

> HEP Be ANTIGEN Contains POS

> HEP Be ANTIGEN Contains Pos

> HEP Be ANTIGEN Contains p

> HEP Be ANTIGEN Contains P

> HEPATITIS C ANTIBODY NEG NO 15

> HEP C ANTIBODY Contains NEG

> HEP C ANTIBODY Contains SEE COMMENT

> HEPATITIS C ANTIBODY POS NO 15

> HEP C ANTIBODY Contains POS

> NOTE: The VHA CIO HEP-C Implementation team will be comparing the HEPATITIS A, B, and C LAB SEARCH/EXTRACT setup to the hepatitis laboratory terms in the REMINDER TERM file (#811.5). They will also be reviewing the Hepatitis C Risk Assessment mappings.

## How to Link Antimicrobial Entries to Workload Codes Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Laboratory Search/Extract software automatically links as many of the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) data entries to the WKLD CODE file (#64) data entries that are identified in your site files. However, the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) data entries that were not linked (i.e. no match found) to the WKLD CODE file (#64) will require linking. The Antimicrobial Link Update \[LREPILK\] option contains three options that can be used to <u>identify</u> and <u>link</u> data entries that were not linked by the post INIT.

### Antimicrobial Link Update \[LREPILK\] options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Examples:

> Select Lab Search/Extract Primary Menu\<RET\>

> <span id="p421_113" class="anchor"></span>ENH Lab EPI Manual Run (Enhanced)

> VR Print Detailed Verification Report

> LO Local Pathogen Menu ...

> PI Pathogen Inquiry

> UP Lab EPI Parameter Setup

> Lab EPI Protocol Edit

> LK Antimicrobial Link Update

> Select Lab Search/Extract Primary Menu Option: LK \<RET\> Antimicrobial Link Update

> This option will allow you to link file '62.06 ANTIMICROBIAL

> SUSCEPTIBILITY' file with file '64 WKLD CODE.

> Select one of the following:

> A AUTO

> M MANUAL

> S SEMI-AUTO

#### AUTO option

> The AUTO option identifies and attempts to link data entries that are not currently linked. This option also displays linked and non-linked data entries.

> Example:

> Enter response: A\<RET\>UTO

> AMIKACN \<----Linked----\> Amikacin

> AMPICLN \<----Linked----\> Ampicillin

> CLINDAM \<----Linked----\> Clindamycin

> POLYMYXIN B \<----Not Linked----\>No Match Found

> RIFAMPIN \<----Linked----\> Rifampin

#### MANUAL option

> The MANUAL option will add or delete linked entries. Examples are from entries in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06).

> Example: Deleting an Entry

> Enter response: MANUAL\<RET\>

> Select ANTIMICROBIAL SUSCEPTIBILITY NAME: PENICLIN\<RET\> PENICILLIN

> NATIONAL VA LAB CODE: Substance P// PEN\<RET\>

> 1 PENFIELD AND CONE STAIN 88010.0000

> 2 PENICILLIN Penicillin 81852.0000

> 3 PENTAZOCINE Pentazocine 81854.0000

> 4 PENTOBARBITAL Pentobarbital 81856.0000

> CHOOSE 1-4: 2 Penicillin\<RET\>

> Select ANTIMICROBIAL SUSCEPTIBILITY NAME: VANCMCN\<RET\> VANCOMYCIN

> NATIONAL VA LAB CODE: Shell Vial Technique// VANCOMYCIN\<RET\> Vancomycin 81485.0000\<RET\>

> Select ANTIMICROBIAL SUSCEPTIBILITY NAME: Ampicillin/sulbactam\<RET\> Ampicillin/subalctam

> NATIONAL VA LAB CODE: Ampicillin// @\<RET\>

> SURE YOU WANT TO DELETE? Y (Yes)\<RET\>

> Select ANTIMICROBIAL SUSCEPTIBILITY NAME:

#### SEMI-AUTO option

> The SEMI-AUTO option looks for entries that are not currently linked and prompts the user to select the corresponding entry in the WKLD CODE file (#64).

> Example:

> Enter response: SEMI-AUTO\<RET\>

> AMIKACN AMIKACIN

> NATIONAL VA LAB CODE: AMIK\<RET\>ACIN Amikacin 81098.0000

> Continue YES/\<RET\>

> AMPICLN AMPICILLIN

> NATIONAL VA LAB CODE: AMP\<RET\>

> 1 AMP CYCLIC 81029.0000

> 2 AMPHETAMINE Amphetamine 81528.0000

> 3 AMPHOTERICIN B Amphotericin B 81530.0000

> 4 AMPICILLIN Ampicillin 81532.0000

> CHOOSE 1-4: 4 Ampicillin

> Continue YES// \<RET\>

> CLINDAM CLINDAMYCIN

> NATIONAL VA LAB CODE: CLINDAMYCIN Clindamycin 81676.0000

> Continue YES// \<RET\>

> CARBCLN CARBENICILLIN

> NATIONAL VA LAB CODE:

> Continue YES// NO\<RET\>

## Delete Entry from Laboratory Search/Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Parameters Input Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the tab key to move the cursor. Highlight the entry that is to be deleted, select the “@” symbol, then press enter/return. You will then receive a deletion warning asking if you are sure.

> Example: Deleting an Entry

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: CANDIDA ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology

> CANDIDA PARAPSILOSIS \<Tab\>

> CANDIDA PSEUDOTROPICALIS \<Tab\>

> CANDIDA SKIN TEST ANTIGEN @ \<Ret\>

> CANDIDA STELLATOIDEA

> Antimicrobial Susceptibility NLT Code NLT Description

> \<Tab\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Next Page Refresh

> COMMAND: Press \<PF1\>H for help

> WARNING: DELETIONS ARE DONE IMMEDIATELY!

> (EXITING WITHOUT SAVING WILL NOT RESTORE DELETED RECORDS.)

> Are you sure you want to delete this entire Subrecord (Y/N)? y \<Ret\>

## How to add an entry to the Laboratory Search/Extract Parameters Input Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the tab key to move the cursor. Highlight a blank line where the entry is to be added.

> Example:

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: CANDIDA ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology

> CANDIDA

> CANDIDA GUILLIERMONDII

> CAN \<Ret\>

> Antimicrobial Susceptibility NLT Code NLT Description

> \<Tab\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 1 CAN CANDIDA ALBICANS 4081

> 2 CANARYPOX VIRUS 3604

> 3 CANDICIDIN 7328

> 4 CANDIDA, NOS 4080

> 5 CANDIDA GUILLIERMONDII 4082

> Choose 1-5 or '^' to quit: 1\<Ret\>

> LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

> NAME: CANDIDA ACTIVE: YES

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Selected Etiology

> CANDIDA GUILLIERMONDII

> CANDIDA KRUSEI

> CANDIDA ALBICANS \<- The entry will appear after answering yes

> to the adding a new ETIOLOGY prompt.

> Antimicrobial Susceptibility NLT Code NLT Description

> \<Tab\>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> CAN CANDIDA ALBICANS

> Are you adding 'CANDIDA ALBICANS' as a new ETIOLOGY? Y \<Ret\>

## Additional Workload and Suffixes Codes Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this form to request additional Workload and Suffixes codes.

> Additional Workload and Suffixes Codes Request Form

> Site Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Site Number: \_\_\_\_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_\_

> Contact Person: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Commercial PH# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ EXT\_\_\_\_\_

> FTS Ph \#: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ EXT \_\_\_\_\_\_\_\_

> Procedure Name \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Abbreviations: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Procedure Name \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Abbreviations: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Procedure Name \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Abbreviation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Method: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Abbreviation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Method: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Abbreviation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Method: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Abbreviation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Submit Additional Workload and Suffixes Codes Request Form to:

> *Frank Stalling, P&LMS Informatics Manager*

> *1901 North Highway 360, Suite 351*

> *Grand Prairie, Texas 75050*

> *FAX: 817-649-7110*

APPENDIX-B

HELPFUL HINTS

## # Helpful Hints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides helpful hints and examples for maintaining and validating EPI and the three new Hepatitis pathogens.

## Preferred Methods for Clostridium difficile Data Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are two preferred methods that will make it easy to capture data for Clostridium difficile criteria (i.e., as well as several other methods which sites may already employ).

> NOTE: As long as the designated parameter results being tracked are in a retrievable field (i.e., not a “Free Text” or “Comment” field) the method the site chooses is an individual decision.

### Preferred Method \#1:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The first preferred method is to have the site define an etiology of “Clostridium difficile toxin positive”. This allows a topography specimen of accession area “feces/stool” to be accessioned through the Microbiology accession area. Then, if the stool specimen were indeed positive for *Clostridium difficile* toxin, by any of the known methods of testing, the etiology would be “Clostridium difficile toxin positive.” To accomplish this method would require sites to enter three new local etiologies:

- Clostridium difficile toxin positive
- Clostridium difficile toxin negative
- Clostridium difficile toxin in determinant

> These would be different from a culture isolate being positive for *Clostridium difficile,* in that they actually are etiologies/results based on toxin testing. This leaves the etiology of *Clostridium difficile* for actual culture positive specimens for the organism *Clostridium difficile*. The Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option, the site parameter by which the software will capture a patient diagnosed with proven *Clostridium difficile*-associated colitis, will be by placing “Clostridium difficile toxin positive” etiology into the selected etiology entry screen. This has the advantage of being more consistent with other data entry practices in the Microbiology sections of most laboratories.

### Preferred Method \#2:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The second preferred method is having the data in retrievable form would be to enter/accession the specimen for *Clostridium difficile* toxin assay under the chemistry/serology format (regardless of where the test is physically done) with the results being a choice of “positive”, “negative”, or “indeterminate”. This would allow one to enter *“Clostridium difficile* toxin” assay as the test for the EPI software to search in the chemistry/serology format. The result would be retrievable for EPI under a chemistry/serology lab test of “*Clostridium difficile* toxin” with the indicator “contains” and the value of “pos”, as noted in the sample page. If your site does not routinely do *Clostridium difficile* toxin assay testing this way, a different method of accessioning the specimen to get it in chemistry/serology format would be needed.

> However, the Chemistry/Serology format would give additional flexibility in placing interpretational guidelines for the test results in the “Comments” field. For the EPI, “positive” or “negative” results cannot be located in a “Free Text” or “Comments” field as these are not retrievable.

> Some VAMCs accession the stool specimen for the *Clostridium difficile* toxin assay under the Microbiology format. An etiology is not given under the final culture result, but written into free text or comments section stating the *Clostridium difficile* toxin assay test result. This is not in a retrievable format and therefore not acceptable for the EPI criteria.

> Some VAMCs still use cytotoxin assays of cell culture, which are again entered in a “Free Text” or “Comment” field. This again is not acceptable unless it is accessioned and recorded under the chemistry/serology format as a straightforward lab test result of “positive” or “negative” or “indeterminate”.

> Some VAMCs choose to report *Clostridium difficile* toxin assay positivity under the Microbiology application. As an etiology/culture result of *Clostridium difficile* (even though culture, was not actually done) this is not a true measure of what is actually being tested (as most sites do not culture the organism but just run the toxin assay test). However, if your site uses this means to represent *Clostridium difficile* toxin assay positivity and there are no exceptions (such as the site reporting an actual positive culture of (*Clostridium difficile* which is toxin assay negative), then this would be acceptable though less desirable for EPI purposes.

## Validating EPI Data Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once the Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option parameter descriptions are defined, EPI HL7 format mailman messages (i.e., containing EPI and Hepatitis C EPI data) are transmitted on the 15<sup>th</sup> of each month to AITC, formerly AAC. The AITC will send an Emerging Pathogens Confirmation mailman message to the sending VHA facility via the EPI mail group on the 15<sup>th</sup> of each month.

> An Emerging Pathogens Verification Report mailman message will also be generated locally; it is a summary of the transmitted EPI HL7 format mailman message (i.e., in a human readable format). This report is sent to the EPI-REPORT mail group on the 15<sup>th</sup> of each month.

> The Emerging Pathogens Verification Report mailman message allows the EPI-REPORT mail group members to review EPI and the three new Hepatitis pathogens data transmissions to AITC, formerly AAC and make corrections (e.g., complete social security numbers, valid Date of Births, and Period of Services, etc.) as deemed necessary. The Emerging Pathogen Verification Report mailman messages should be used to compare EPI and the three new Hepatitis pathogens data capture to site-specific data capture. It is recommended that the Lab Search/Extract Manual Run \[LREPI (EPI) MANUAL RUN\] option be run to evaluate 1-3 months of data (i.e., as determined by the sites) at initial implementation of the software.

> The Microbiology Laboratory personnel, Laboratory Manager, TQI/QI/QA, or other personnel (i.e., as determined by the sites) may already have data of isolated “organisms of interest”. Several of the nationally defined emerging pathogens may well corresponds. Therefore, a quick comparison can be done using the Emerging Pathogens Verification Report mailman message. This comparison also ensures that the Laboratory Search/Extract software is appropriately capturing the EPI and the three new Hepatitis pathogens cases and numbers.

> For tests such as Hepatitis C and the three new Hepatitis pathogens, most LIMs should be able to generate reports (with patient names) that include “positive” tests results to use for comparison. Additionally, the Health Information Management Section at each site should be able to generate a report of <span id="p421_123" class="anchor"></span>ICD-9 or ICD-10 Diagnoses by date. This ICD Diagnoses by-date-report helps determine if the VHAQ Infectious Disease Program Office EPI and the three new Hepatitis pathogens data captures concurs with the defined EPI criterion (i.e., Cryptosporidium-007.8, Legionnaire’s disease--482.80, malaria--084, 084.0, 084.1, 084.2, 084.3, 084.4, 084.5, 084.6, 085.7, 084.8, 084.9, dengue-061, 065.4, Creutzfeldt-Jakob--046.1, and Leishmaniasis--085, 085.0, 085.1, 085.2, 085.3, 085.4, 085.5, 085.9).

> Be aware that a number of these pathogens DO NOT occur at a high frequency. Sites with previously known cases of emerging pathogens, such as TB, should run the Lab Search/Extract Manual Run \[LREPI (EPI) MANUAL RUN\] option for the entire month to verify that the TB culture was isolated and to see if it is captured. Additionally, “test patients” known to have these lab results can also be run.

> The purpose of this validation is not to require extra paperwork for QI monitors and long-term document files. The validation should be done at the initial implementation of the Laboratory Search/Extract software to ensure accurate data capture. Thereafter, a review should be done once every 4-6 months to ensure that Lab Search/Extract Parameter Setup \[LREPI (EPI) PARAMETER UPDATE\] option entries for the EPI criteria remain accurate. Parameter updates may be required if a new lab test/result is to be implemented for one of the Emerging Pathogens Initiative.

## Lab Search/Extract Protocol Edit \[LREPI PROTOCOL EDIT\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Lab Search/Extract Protocol Edit \[LREPI PROTOCOL EDIT\] option is used for editing the LREPI protocol. The option is located on the Lab Search/Extract Primary Menu \[LREPI SEARCH EXTRACT MENU\].

> Example:

> Protocol Parameters Setup Definition

> PROTOCOL: LREPI\<RET\>

> Title: Emerging Pathogens Initiative (EPI) Message Size: 32000

> Report Mail Group: EPI-REPORT

> Send Alert: YES

> Send Alert To

> LABUSER, TWO

## EPI Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: It is highly recommended that the “Office of the Director (00)” at each VHA facility initially designate the member(s) responsible for overseeing the EPI mail group and EPI-Report mail group.

> NOTE: It is highly recommended that a TQI/QI/QA staff, Laboratory Information Manager (LIM), Microbiology director or supervisor, Infection Control Practitioners, or Hospital Epidemiologist), or individual(s) with similar functions be a member(s) of the mail groups. This member(s) is responsible for making EPI data corrections due to the numerous files from which the data is obtained (e.g., PTF, PIMS, Health Information Management, Laboratory, etc.). Once the corrections are made, it is the responsibility of the EPI mail group member(s) to re-transmit the EPI data to the AITC. These members may also be of assistance with the verification and periodic validation processes.

### EPI mail group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The EPI mail group is used by the VHA facilities to transmit EPI HL7 format mailman messages to AITC and for AITC to transmit EPI Confirmation mailman messages back to the sending VHA facilities once the EPI HL7 format mailman messages data transmission has been received by AITC.

> Example: EPI mail group setup

> NAME: EPI TYPE: public

> ALLOW SELF ENROLLMENT?: NO REFERENCE COUNT: 1220

> LAST REFERENCED: AUG 15, 2000 RESTRICTIONS: UNRESTRICTED

> MEMBER: Add the local staff who will play a role in validating the HL7 messages.

> DESCRIPTION: This mail group is used for the transmission of HL7 messages

> derived from the parameters defined in the EMERGING PATHOGEN file (#69.5) to

> the Austin Automation Center.

> REMOTE MEMBER: S.HL V16 SERVER@ (add your site name here)

> REMOTE MEMBER: XXX@Q-EPI.MED.VA.GOV

> REMOTE MEMBER: <span class="mark">REDACTED</span>

> REMOTE MEMBER: <span class="mark">REDACTED</span>

### EPI-Report mail group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The EPI-Report receives the Emerging Pathogens Verification Report and the EPI Processing Report mailman messages sent from AITC. The members of this mail group will assist in EPI and the three new Hepatitis pathogens data validation and correction process.

> Example: EPI Report mail group setup

> OUTPUT FROM WHAT FILE: LAB SEARCH/EXTRACT// MAIL GROUP\<RET\>

> (1441 entries)

> Select MAIL GROUP NAME: EPI-REPORT\<RET\>

> ANOTHER ONE:\<RET\>

> STANDARD CAPTIONED OUTPUT? Yes//\<RET\>(Yes)

> Include COMPUTED fields: (N/Y/R/B): NO//\<RET\> - No record number (IEN), no Computed Fields

> NAME: EPI-REPORT TYPE: public

> ALLOW SELF ENROLLMENT?: NO REFERENCE COUNT: 8499

> LAST REFERENCED: AUG 15, 2000 RESTRICTIONS: UNRESTRICTED

> MEMBER: EPI,USER

> DESCRIPTION: This mail group is used to deliver a formatted report taken from the HL7 message that is created to assist in the verification of data.

### Adding EPI Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Add the EPI mail groups to the HL7 APPLICATION PARAMETER file (#771) using VA FileMan V. 21.0:

> Example:

> Select OPTION: ENTER OR EDIT FILE ENTRIES \<RET\>

> INPUT TO WHAT FILE: HL7 APPLICATION PARAMETER file (#771)\<RET\>

> (7 entries)

> EDIT WHICH FIELD: ALL// \[Enter Facility Name field\]\<RET\>

> THEN EDIT FIELD:\<RET\>

> Select HL7 APPLICATION PARAMETER NAME: EPI \<RET\> ACTIVE

> FACILITY NAME: \[Enter your facility name or facility number\] \<RET\>

> Select HL7 APPLICATION PARAMETER NAME: EPI-Report\<RET\> ACTIVE

> FACILITY NAME: \[Enter your facility name or facility number\] \<RET\>

## Starting Lower Level Protocol for HL7 V. 1.6 Background Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example:

> Select Systems Manager Menu Option:HL7 Main\<RET\> Menu

> 1 V1.5 OPTIONS ...

> 2 V1.6 OPTIONS ...

> 3 Activate/Inactivate Application

> 4 Print/Display Menu ...

> 5 Purge Message Text File Entries

> Select HL7 Main Menu Option: 2\<RET\> V1.6 OPTIONS

> 1 Communications Server ...

> 2 Interface Workbench

> 3 Message Requeuer

> Select V1.6 OPTIONS Option: 1\<RET\> Communications Server

> 1 Edit Communication Server parameters

> 2 Manage incoming & outgoing filers ...

> 3 Monitor incoming & outgoing filers

> 4 Start LLP

> 5 Stop LLP

> 6 Systems Link Monitor

> 7 Logical Link Queue Management

> 8 Report

> Select Communications Server Option: 4\<RET\> Start LLP

> This option is used to launch the lower level protocol for the

> Appropriate device. Please select the node with which you want

> to communicate

> Select HL LOGICAL LINK NODE: EPI\<RET\>

> The LLP was last shutdown on JAN 30, 1997 12:06:19.

> Select one of the following:

> F FOREGROUND

> B BACKGROUND

> Q QUIT

> Method for running the receiver: B//\<RET\> ACKGROUND

> Job was queued as 131225.

## EPI Data Cycle Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Patch builds global message or HL7 message transmission monthly (i.e., 15<sup>th</sup> of the month)
- Local global build used to generate Verification Report about abstracted data in HL7 messages
- HL7 messages sent to Austin Automation Center EPI queue
- Upon receipt of HL7 message, AITC returns a confirmation message (confirming that data has reached queue, but not necessarily accepted for processing)
- Processing of data at Austin Automation Center (i.e., 25<sup>th</sup> of the month) AITC returns a processing message to site with contains information about errors and processing of data (this is the message that data has been processed at the AITC with Fatal Error codes constituting rejection of the entire data set, and presence of no fatal errors on processing report indicating acceptance of data set)

## EPI Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Emerging Pathogens (as defined by VAHQ) act as triggers for data acquisition for the Laboratory Search/Extract software. The software then retrieves relevant, predetermined, and patient-specific data for transmission to the AITC database repository. Once at that location, the data are analyzed using a Statistical Analysis System (SAS)-based statistical software. VAHQ Reports may then be generated for appropriate use and distribution at the national level.

> With the installation of the new LR\*5.2\*260, automated data transmissions will occur. Receipt of this transmission at the AITC queue will trigger a confirmation mailman message back to the originating site to “confirm” that data has been sent. Then at the next processing cycle (25<sup>th</sup> of the month), a processing/error report will also be generated and sent back to the originating site. This processing/error report will serve as the ultimate “confirmation” that data has been accepted. If there is a fatal error in any segment of the message, the entire message will be rejected and must be resent manually. Warning codes/errors are accepted into the data set, but serve to remind the originating site that a correction of the process generating the error may be needed.

> Note: The daily NCH data transmissions are no longer necessary and the NCHP program office has requested that we terminate the transmissions. This will be done during the post-init phase and does not require any user intervention.

## HL7 Format Mailman Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The V*IST*A Laboratory Search/Extract software automatically processes and transmits EPI and the three new Hepatitis pathogens data using an HL7 format mailman message on the 15<sup>th</sup> of each month via the Q-EPI.MED.VA.GOV domain to the AITC for processing.

> Example: HL7 Format Mailman Message

> Subj: HL7 Message JUL 28,2000@15:56:29 from Station XXX STATION XXX \[#63430\]

> 10 Feb 97 15:56 262 Lines

> From: POSTMASTER (Sender: ANYBODY) in 'IN' basket. Page 1

> ----------------------------------------------------------------------------

> PID\|1\|000-00-1910~1~M10\|36402~8~M10\|\|LABPATIENT19~TEN\|\|19310912\|M\|\|6\|~33496\|\|\|\|\|\|\|\|000001910\|\|\|\|\|\|\|\|0

> PV1\|1\|I\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|1~REGULAR~VA45\|\|\|\|\|\|\|\|20000515124929\|20000516174217

> DG1\|1\|\|244.9~HYPOTHYROIDISM NOS~I9\|20000515124929\|\|

> DG1\|2\|\|280.9~IRON DEFIC ANEMIA NOS~I9\|20000515124929\|\|PR

> DG1\|3\|\|456.1~ESOPH VARICES W/O BLEED~I9\|20000515124929\|\|

> DG1\|4\|\|456.8~VARICES OF OTHER SITES~I9\|20000515124929\|\|

> DG1\|5\|\|530.2~ULCER OF ESOPHAGUS~I9\|20000515124929\|\|

> DG1\|6\|\|553.3~DIAPHRAGMATIC HERNIA~I9\|20000515124929\|\|

> DG1\|7\|\|571.5~CIRRHOSIS OF LIVER NOS~I9\|20000515124929\|\|

> DG1\|8\|\|572.3~PORTAL HYPERTENSION~I9\|20000515124929\|\|

> DG1\|9\|\|579.8~INTEST MALABSORPTION NEC~I9\|20000515124929\|\|

> DG1\|10\|\|530.19~OTHER ESOPHAGITIS~I9\|20000515124929\|\|

> ZXE\|\|INTERFERON BETA-1A 30MCG/VL \*R~NDC\|30\|20000504\|20000504\|\|1

> DSP\|1\|\|20000504~INTERFERON BETA-1A~00\~~\|\|1

> ZXE\|\|INTERFERON BETA-1A 30MCG/VL \*R~NDC\|30\|20000511\|20000511\|\|2

> DSP\|2\|\|20000511~INTERFERON BETA-1A~00\~~\|\|2

> DSP\|1\|\|20000501140060~HEP C VIRUS ANTIBODY POSITIVE~5~REACTIVE~\|\|0

> DSP\|3\|\|20000501140020~TRANSFERASE (AST) (SGOT)~00~52~\|\|0

> DSP\|4\|\|20000501140020~ALANINE AMINO (ALT) (SGPT)~00~93~\|\|0

> DSP\|5\|\|20000501140020~BILIRUBIN~00~0.2~\|\|0

> NTE\|1\|17~HEPATITIS B ANTIBODY POS

> OBR\|1\|\|\|81121.0000~CHEMISTRY

> TEST~VANLT\|\|\|20000503070530\|\|\|\|\|\|\|\|SER\~~SERUM\|\|\|VIR 0503 10

> OBX\|1\|ST\|89067.0000~HEPATITIS B SURFACE

> AB~VANLT~507~HBSAB~VA60\|\|REACTIVE\|\|"NEG"-\|\|\|\|\|\|\|20000511143048

> PV1\|2\|O\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|200005050650

> NTE\|1\|16~HEPATITIS A ANTIBODY POS

> OBR\|1\|\|\|81121.0000~CHEMISTRY TEST~VANLT\|\|\|200005050650\|\|\|\|\|\|\|\|SER\~~SERUM\|\|\|IMM 0505 37

> OBX\|1\|ST\|87428.0000~HEPATITIS A~VANLT~505~HEPATITIS A ANTIBODY TOTAL~VA60\|\|POS\|\|"NEG"-\|\|\|\|\|\|\|20000509044823

> OBX\|2\|ST\|89083.0000~HEPATITIS A IGM AB~VANLT~1336~HEPATITIS A ANTIBODY IGM~VA60\|\|INDETERMINATE\|\|"NEG"-\|\|\|\|\|\|\|20000509044823

> PV1\|3\|O\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|200005081035

> NTE\|1\|15~HEPATITIS C ANTIBODY NEG

> OBR\|1\|\|\|81121.0000~CHEMISTRY TEST~VANLT\|\|\|200005081035\|\|\|\|\|\|\|\|SER\~~SERUM\|\|\|VIR 0508 71

> OBX\|1\|ST\|89070.0000~HEPATITIS C AB~VANLT~1354~HEP C AB~VA60\|\|NEG\|\|"NEG"-\|\|\|\|\|\|\|20000509140045

> PV1\|4\|I\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|1~REGULAR~VA45\|\|\|\|\|\|\|\|20000509141603\|20000510162649

> DG1\|1\|\|250.01~DIABETES MELLI W/0 COMP TYP I~I9\|20000509141603\|\|

> DG1\|2\|\|585.~CHRONIC RENAL FAILURE~I9\|20000509141603\|\|

> DG1\|3\|\|V45.1~RENAL DIALYSIS STATUS~I9\|20000509141603\|\|

> DG1\|4\|\|787.02~NAUSEA ALONE~I9\|20000509141603\|\|

> DG1\|5\|\|789.00~ABDOM PAIN, UNSP SITE~I9\|20000509141603\|\|PR

> DG1\|6\|\|787.91~DIARRHEA~I9\|20000509141603\|\|

> NTE\|1\|16~HEPATITIS A ANTIBODY POS

> OBR\|1\|\|\|81121.0000~CHEMISTRY TEST~VANLT\|\|\|200005091830\|\|\|\|\|\|\|\|SER\~~SERUM\|\|\|IMM 0509 355

> OBX\|1\|ST\|87428.0000~HEPATITIS A~VANLT~505~HEPATITIS A ANTIBODY TOTAL~VA60\|\|POS\|\|"NEG"-\|\|\|\|\|\|\|20000512020040

> OBX\|2\|ST\|89083.0000~HEPATITIS A IGM AB~VANLT~1336~HEPATITIS A ANTIBODY IGM~VA60\|\|INDETERMINATE\|\|"NEG"-\|\|\|\|\|\|\|20000512020040

> PV1\|5\|O\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|20000530122010

> NTE\|1\|16~HEPATITIS A ANTIBODY POS

> OBR\|1\|\|\|81121.0000~CHEMISTRY

> TEST~VANLT\|\|\|20000530122010\|\|\|\|\|\|\|\|SER\~~SERUM\|\|\|IMM 0530 164

> OBX\|1\|ST\|87428.0000~HEPATITIS A~VANLT~505~HEPATITIS A ANTIBODY

> TOTAL~VA60\|\|POS\|\|"NEG"-\|\|\|\|\|\|\|20000603040054

> OBX\|2\|ST\|89083.0000~HEPATITIS A IGM AB~VANLT~1336~HEPATITIS A ANTIBODY

> IGM~VA60\|\|INDETERMINATE\|\|"NEG"-\|\|\|\|\|\|\|20000603040054

## EPI Confirmation Mailman Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Upon receipt of the VHA facilities EPI and Hepatitis pathogens HL7 format mailman message monthly transmission to AITC, individual EPI Confirmation mailman messages are sent by AITC to the originating VHA facilities via the EPI mail group. Members of this mail group are being notified that EPI and Hepatitis pathogens HL7 format mailman message data transmission has been received by AITC for processing.

> NOTE: EPI Confirmation mailman messages ONLY means that the originating VHA facility data transmission has been received by the AITC for processing.

> Examples: EPI Confirmation Mailman Messages

> Subj: DRM6491 EPI Confirmation \[#1724877\] 03 Aug 00 19:48 CST 2 lines

> From: <span class="mark">REDACTED</span> In 'IN' basket. Page 1 \*New\*

> -----------------------------------------------------------------------

> Ref: Your EPI message \#20756491 with Austin ID \#124368839,

> is assigned confirmation number 002161938706725.

> Enter message action (in IN basket): Ignore//

> Subj: DRM6500 EPI Confirmation \[#1724889\] 03 Aug 00 19:48 CST 2 lines

> From: <span class="mark">REDACTED</span> In 'IN' basket. Page 1 \*New\*

> ------------------------------------------------------------------------

> Ref: Your EPI message \#20756500 with Austin ID \#124368871,

> is assigned confirmation number 002161938706735.

> Enter message action (in IN basket): Ignore//

## Emerging Pathogens Verification Report Mailman Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An Emerging Pathogens Verification Report mailman message is generated locally and sent to the EPI-REPORT mail group once the transmitted HL7 format mailman message has been built locally (i.e., on the 15<sup>th</sup> of each month). The Emerging Pathogens Verification Report mailman message is a copy of the transmitted EPI HL7 format mailman messages (i.e., in a human readable format). This report allows the EPI-REPORT mail group members to review EPI and the three new Hepatitis pathogens data transmissions to AITC and make corrections (e.g., complete social security numbers, valid Date of Births, and Period of Services, etc.) as deemed necessary.

> NOTES:

> The Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCE MANUAL RUN\] option can be generated manually to transmit EPI and Hepatitis pathogens corrections to the AITC whenever needed. This option can be manually generated as often as necessary. (*See the EPI and Hepatitis Pathogens User Guide Appendix-B section of this guidefor examples)*.

> Lab Search/Extract Transmissions to AITC after 6:00 pm are processed the next day.

> Please DO NOT use the Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option to transmit EPI and Hepatitis pathogens data on Wednesdays of PAY ROLL weeks. These transmissions may cause a delay in processing the PAY ROLL data.

> Example: Emerging Pathogens Verification Report Mailman Message

> Emerging Pathogens Verification Report \[#60004\] Page 1

> ----------------------------------------------------------------------------

> REPORTING DATE FROM 12-01-1996 TO 12-31-1996 Message Seq \# 1 Auto

> LABPAIENT, ONE 000-00-0001 07-07-1913 M WORLD WAR II 45205

> Outpatient Accession Date 12-11-1996@1025

> \*\*\*\*\*\*\*\*\* STREPTOCOCCUS GROUP A \*\*\*\*\*\*\*\*\*

> 12-11-1996@1025 BACT 96 10383 MICRO CULTURE LEG

> 1 12-13-1996 STREPTOCOCCUS BETA HEMOLYTIC, GROUP A

> 2 12-13-1996 STAPHYLOCOCCUS (COAGULASE NEGATIVE)

> ORG \# 1 12-11-1996@1025 ANTIBIOTIC MIC LEG

> ORG \# 2 12-11-1996@1025 ANTIBIOTIC MIC LEG

> LABPATIENT, TWO 000-00-0002 01-08-1923 M WORLD WAR II 45239

> Inpatient Admission Date 12-19-1996@1125

> \*\*\*\*\*\*\*\*\*4 CLOSTRIDIUM DIFFICILE \*\*\*\*\*\*\*\*\*

> Can be verified using standard result reviews for “CH” subscripted tests (e.g., LRRSP, LRRP3, LRSORD, LRSORA, LRGEN)

> 12-25-1996@1415 MSER 96 418 CHEMISTRY TEST FECES

> Clostridium Difficile Toxin 12-27-1996@1403 POSITIVE

> LABPATIENT, THREE 000-00-0003 11-05-1910 M WORLD WAR II 45255

> Inpatient Admission Date 12-03-1996@1908

> Discharge Date 12-09-1996@1151 Discharge Disposition REGULAR

> 250.01 DIABETES MELLI W/0 COMP TYP I

> PTF data can be verified using several different PTF options:

> DG PTF ICD DIAGNOSIS SEARCH

> DG PTF SUMMARY DIAG/OP OUTPUT

> DG PTF COMPREHENSIVE INQUIRY

> (most require DGPTFSUP key)

> 276.8 HYPOPOTASSEMIA

> 427.31 ATRIAL FIBRILLATION

> 428.0 CONGESTIVE HEART FAILURE

> 482.30 PNEUM. UNSPEC. STREPTOCOCCUS

> \*\*\*\*\*\*\*\*\*6 STREPTOCOCCUS GROUP A \*\*\*\*\*\*\*\*\*

> 12-04-1996 BACT 96 10187 MICRO CULTURE SPUTUM

> 1 12-06-1996 STREPTOCOCCUS BETA HEMOLYTIC, GROUP A

> 2 12-06-1996 STAPHYLOCOCCUS AUREUS

> ORG \# 1 12-04-1996 ANTIBIOTIC MIC SPUTUM

> ORG \# 2 12-04-1996 ANTIBIOTIC MIC SPUTUM

> Microbiology subscripted organisms and susceptibilities can be reviewed using LRMIPSZ, LRMIPC, LRMIPLOG, LRGEN, LRRSP, and LRRP3.

> Penicillin R

> Clindamycin S

> Vancomycin S

> TETRCLN S

> TRMSULF S

> Erythromycin S

> Oxacillin S

> Cephalothin S

> Ciprofloxacin S

> AMPICILLIN-SULBACTAM S

> LABPATIENT, FOUR 000-00-0004 02-23-1920 M PRE-KOREAN 45150

> Inpatient Admission Date 11-18-1996@2213

> \*\*\*\*\*\*\*\*\*8 CANDIDA \*\*\*\*\*\*\*\*\*

> 12-11-1996@0100 BLD 96 3914 MICRO CULTURE BLOOD

> 1 12-15-1996 CANDIDA ALBICANS

> ORG \# 1 12-11-1996@0100 ANTIBIOTIC MIC BLOOD

> LABPATIENT, FIVE 000-00-0005 12-23-1949 M VIETNAM ERA 45206

> Outpatient Accession Date 12-20-1996@1309

> \*\*\*\*\*\*\*\*\*2 HEPATITIS C ANTIBODY POS \*\*\*\*\*\*\*\*\*

> 12-20-1996@1309 RIA 1220 68 CHEMISTRY TEST SERUM

> Hepatitis C Ab 01-03-1997@1347 STRONG POSITIVE -

> LABPATIENT, SIX 000-00-0006 07-06-1919 M WORLD WAR II 41074

> Outpatient Accession Date 12-19-1996@1007

> \*\*\*\*\*\*\*\*\*1 VANC-RES ENTEROCOCCUS \*\*\*\*\*\*\*\*\*

> 12-19-1996@1007 BACT 96 10618 MICRO CULTURE URINE

> 1 12-23-1996 PSEUDOMONAS AERUGINOSA

> 2 12-23-1996 ENTEROCOCCUS FAECIUM

> ORG \# 1 12-19-1996@1007 ANTIBIOTIC MIC URINE

> Gentamicin S

> Cefazolin R

> Ampicillin R

> Tobramycin S

> TRMSULF R

> Amikacin S

> Cefoxitin R

> Cefotaxime I

> Nitrofurantoin R

> Cefoperazone S

> Mezlocillin S

## Lab Search/Extract Manual Run (Enhanced)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## \[LREPI ENHANCED MANUAL RUN\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCE MANUAL RUN\] option automatically transmit EPI and the three new Hepatitis pathogens data corrections to the AITC via HL7 format mailman messages each time the option is run.

> NOTES:

> Lab Search/Extract Transmissions to AITC after 6:00 p.m. are processed the next day.

> Please DO NOT use the Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option to transmit EPI and Hepatitis pathogens data on Wednesdays of PAY ROLL weeks. These transmissions may cause a delay in processing the PAY ROLL data.

> Example: Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option

> Laboratory Search rerun option

> Select Protocol: ?

> Answer with LAB SEARCH/EXTRACT PROTOCOL, or NUMBER

> Choose from:

> 4024 LREPI Emerging Pathogens Initiative (EPI)

> 4990 LRNCH National Center for Health Promotion

> Select Protocol: 4024 LREPI Emerging Pathogens Initiative (EPI)

> ...OK? Yes// (Yes)

> Override Any Inactive indicators: ? NO//\<RET\>

> Include All Search Parameters? YES//\<RET\>

> Select Search Date: 06012000

> Requested Start Time: NOW// \<RET\> (AUG 09, 2000@16:22:35)

## EPI Processing Report Mailman Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An EPI Processing Report mailman message is sent by AITC to the sending facility EPI-REPORT mail group members at the end of the AITC processing cycle (i.e., the 25<sup>th</sup> of each month). The EPI Processing Report mailman message itemizes all transmissions received by AITC, document the records status as either being accepted or rejected (with the reason code identified). The EPI Processing Report mailman message will ultimately determine whether EPI and Hepatitis pathogens data has been accepted by the AITC to be processed and placed into the EPI Statistical Analysis System (SAS) files. An example of the “Tables of Rejects and Errors and/or Warning Codes” follows the EPI Processing Report Mailman Message example.

> Example: EPI Processing Report Mailman Message sent by AITC

> Subj: EPI/LRK \#970451447950300 \[#1425971\] 11 Aug 00 14:55 CST 50 Lines

> From: \<POSTMASTER@FOC-AUSTIN.VA.GOV\> in 'IN' basket. Page 1 \*\*NEW\*\*

> ---------------------------------------------------------------------------

> 2EPI0001 LRK.

> 437 RLEH1 STATION 437 V2 EPI PROCESSING REPORT REPORT DATE 2000/08 437 RLEH2 PAGE 01..\$

> 437 RLEH3 PROCESS DATE SSN ENCOUNTER DATE MESSAGE ERROR CODES..\$

> 437 RLED1 20000630 000001014 200006071300 005 NO ERRORS..

> 437 RLED1 20000630 000001014 200006071300 008 NO ERRORS..

> 437 RLED1 20000630 000001015 200006230830 003 W23 ..\$

> 437 RLED1 20000630 000001016 20000609145448 001 W23 W23 W23 W2

> 437 RLED1 20000630 000001017 200006141330 004 NO ERRORS..

> 437 RLED1 20000630 000001017 200006141330 007 NO ERRORS..

> 437 RLED1 20000630 000001018 200006121230 001 NO ERRORS..

> 437 RLED1 20000630 000001018 200006121230 001 NO ERRORS..

> 437 RLED1 20000630 000001019 20000605 004 W23 ..\$

> 437 RLED1 20000630 000001019 20000605 006 W23 ..\$

> 437 RLED1 20000630 000001020 20000616123364 001 W23 W23 W23 W2

> 437 RLED1 20000630 000001021 200006121030 004 NO ERRORS..

> 437 RLED1 20000630 000001021 200006121030 006 NO ERRORS..

> 437 RLED1 20000630 000001022 20000530190455 005 W23 W23 W23 W2

> 437 RLED1 20000630 000001023 200006051300 005 NO ERRORS..

> 437 RLED1 20000630 000001023 20000607124866 008 W23 W23 W23..

## Table of Reject and Errors and/or Warning Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following are Tables of Rejects and Errors and/or Warning Codes definitions used by AITC, for the EPI Processing Report Mailman Message.

> Examples:

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>ERROR NUMBER</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>EDIT DESCRIPTION</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ERROR MESSAGE</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>000 Series</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>Miscellaneous</em></p>
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
<p>001</p>
</blockquote></td>
<td><blockquote>
<p>Message Control ID</p>
</blockquote></td>
<td><blockquote>
<p>Must not be blank</p>
</blockquote></td>
<td><blockquote>
<p>Message control ID was blank</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>002</p>
</blockquote></td>
<td><blockquote>
<p>Batch Sending Facility</p>
</blockquote></td>
<td><blockquote>
<p>Sending Station not valid.</p>
<p>(Refer to table AA001)</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Batch Sending</p>
<p>Facility.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>003</p>
</blockquote></td>
<td><blockquote>
<p>Segment Name</p>
</blockquote></td>
<td><blockquote>
<p>PID Segment missing. Do not edit for the existence of PID when NTE segments are present.</p>
</blockquote></td>
<td><blockquote>
<p>PID Segment missing.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>004</p>
</blockquote></td>
<td><blockquote>
<p>Segment Name</p>
</blockquote></td>
<td><blockquote>
<p>PV1 Segment missing. Do not edit for the existence of PV1 when NTE segments are present.</p>
</blockquote></td>
<td><blockquote>
<p>PV1 Segment missing.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>005</p>
</blockquote></td>
<td><blockquote>
<p>Segment Name</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Segment name.</p>
</blockquote></td>
<td><blockquote>
<p>Invalid HL7 Segment name.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>006</p>
</blockquote></td>
<td><blockquote>
<p>Message Creation Date</p>
</blockquote></td>
<td><blockquote>
<p>Must a valid date.</p>
</blockquote></td>
<td><blockquote>
<p>Message Creation Date is invalid.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>007</p>
</blockquote></td>
<td><blockquote>
<p>Message Creation Time</p>
</blockquote></td>
<td><blockquote>
<p>Must a valid time.</p>
</blockquote></td>
<td><blockquote>
<p>Message Creation Time is invalid.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>008</p>
</blockquote></td>
<td><blockquote>
<p>Processing Period</p>
</blockquote></td>
<td><blockquote>
<p>Must a valid time.</p>
</blockquote></td>
<td><blockquote>
<p>Processing period in the NTE segment is invalid.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>009</p>
</blockquote></td>
<td><blockquote>
<p>Processing Period</p>
</blockquote></td>
<td><blockquote>
<p>Historical processing for V2 of EPI (commonly known as HEP C) must be received in Austin sequentially from 1998 forward.</p>
</blockquote></td>
<td><blockquote>
<p>For V2 only - Processing into AITC must be sequential from 10/98 forward.</p>
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
<p><strong>100 Series</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>NTE Totals Segment</em></p>
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
<p>100</p>
</blockquote></td>
<td><blockquote>
<p>Action Ind</p>
</blockquote></td>
<td><blockquote>
<p>Currently not being used.</p>
</blockquote></td>
<td><blockquote>
<p>Currently not being used.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>105</p>
</blockquote></td>
<td><blockquote>
<p>Totals Total Count</p>
</blockquote></td>
<td><blockquote>
<p>Must be numeric, if Action Ind is 'T '.</p>
</blockquote></td>
<td><blockquote>
<p>NTE Totals Total Count was not numeric.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>110</p>
</blockquote></td>
<td><blockquote>
<p>Negative Input Ind</p>
</blockquote></td>
<td><blockquote>
<p>Must be 'N', if Action Ind is not 'T '.</p>
</blockquote></td>
<td><blockquote>
<p>Negative Input Ind was not 'N'.</p>
</blockquote></td>
</tr>
</tbody>
</table>

*Continued*

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>ERROR NUMBER</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>EDIT DESCRIPTION</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ERROR MESSAGE</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>200 Series</strong></p>
<p><em>PID Segment</em></p>
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
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>Patient Name</p>
</blockquote></td>
<td><blockquote>
<p>Required. Must be alpha</p>
<p>numeric. Must not be all</p>
<p>numeric. Must not be all</p>
<p>blanks.</p>
</blockquote></td>
<td><blockquote>
<p>Patient Name is missing, or not alphanumeric, or all numeric, or all blanks.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>205</p>
</blockquote></td>
<td><blockquote>
<p>Patient Date of Birth</p>
</blockquote></td>
<td><blockquote>
<p>Not required. Must be less</p>
<p>than the processing year.</p>
</blockquote></td>
<td><blockquote>
<p>Date of Birth is after the</p>
<p>Date of transmission.</p>
<p>(Also see W03, W04, and W05)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>210</p>
</blockquote></td>
<td><blockquote>
<p>Patient Sex</p>
</blockquote></td>
<td><blockquote>
<p>Not required. Must be</p>
<p>blank or match table.</p>
<p>(Refer to table 0001)</p>
</blockquote></td>
<td><blockquote>
<p>Sex code is not blank or a</p>
<p>valid code.</p>
<p>(Refer to table 0001)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>215</p>
</blockquote></td>
<td><blockquote>
<p>Patient Race</p>
</blockquote></td>
<td><blockquote>
<p>Not required. Must be blank</p>
<p>or a valid code.</p>
<p>(Refer to table VA07)</p>
</blockquote></td>
<td><blockquote>
<p>Race code is not blank or a</p>
<p>valid code.</p>
<p>(Refer to table VA07)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>220</p>
</blockquote></td>
<td><blockquote>
<p>Patient Address</p>
</blockquote></td>
<td><blockquote>
<p>Must be blank or 'H'.</p>
</blockquote></td>
<td><blockquote>
<p>Patient Address is not blank</p>
<p>or 'H'.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>224</p>
</blockquote></td>
<td><blockquote>
<p>Patient Zip Code</p>
</blockquote></td>
<td><blockquote>
<p>Not required. Must be</p>
<p>Blank or numeric.</p>
<p>If numeric, first five digits</p>
<p>must not be all zeros.</p>
<p>If last four digits exist,</p>
<p>then must be numeric.</p>
</blockquote></td>
<td><blockquote>
<p>Address Zip Code is missing</p>
<p>or not numeric.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>235</p>
</blockquote></td>
<td><blockquote>
<p>Social Security Number</p>
</blockquote></td>
<td><blockquote>
<p>Required.</p>
<p>Last byte must be 'P' or</p>
<p>blank.</p>
</blockquote></td>
<td><blockquote>
<p>Pseudo SSN is not 'P' or</p>
<p>blank.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>236</p>
</blockquote></td>
<td><blockquote>
<p>Social Security Number</p>
</blockquote></td>
<td><blockquote>
<p>Required. Must be numeric.</p>
<p>Must be greater than zeros.</p>
</blockquote></td>
<td><blockquote>
<p>Social Security Number is</p>
<p>missing, or not numeric, or</p>
<p>is equal to zeros.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>240</p>
</blockquote></td>
<td><blockquote>
<p>Patient Veteran Status</p>
</blockquote></td>
<td><blockquote>
<p>Must be a valid code.</p>
<p>(Refer to table VA11)</p>
</blockquote></td>
<td><blockquote>
<p>Period of Service was invalid.</p>
<p>(Refer to table VA11).</p>
</blockquote></td>
</tr>
</tbody>
</table>

*Continued*

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>ERROR NUMBER</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>EDIT DESCRIPTION</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ERROR MESSAGE</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>300 Series</strong></p>
<p><em>OBR Segment</em></p>
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
<p>300</p>
</blockquote></td>
<td><blockquote>
<p>Universal Service ID</p>
</blockquote></td>
<td><blockquote>
<p>Must be a valid code.</p>
<p>(Refer to table NLT)</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Universal Service ID</p>
<p>(Refer to table NLT)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>305</p>
</blockquote></td>
<td><blockquote>
<p>Observation Date</p>
</blockquote></td>
<td><blockquote>
<p>Must be numeric date.</p>
<p>Must be a valid date.</p>
<p>Must be less than</p>
<p>Processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Observation Date is invalid</p>
<p>date or after the date of</p>
<p>transmissio.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>307</p>
</blockquote></td>
<td><blockquote>
<p>Observation Time</p>
</blockquote></td>
<td><blockquote>
<p>Not required</p>
<p>Must be blank or numeric.</p>
<p>If numeric, must be a valid</p>
<p>time.</p>
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
<td><blockquote>
<p>Not required. If not blank,</p>
<p>must be a valid code.</p>
<p>(Refer to table SPC)</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Specimen Source</p>
<p>(Refer to table SPC)</p>
<p>Code. (also see W07)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>315</p>
</blockquote></td>
<td><blockquote>
<p>Parent Observation ID</p>
</blockquote></td>
<td><blockquote>
<p>Not required. Must be</p>
<p>blank or a valid code.</p>
<p>(Refer to table NLT)</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Parent Observation ID</p>
<p>(Refer to table NLT).</p>
</blockquote></td>
</tr>
</tbody>
</table>

*Continued*

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>ERROR NUMBER</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>EDIT DESCRIPTION</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ERROR MESSAGE</strong></p>
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
<p><strong>400 Series</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>PV1 Segment</strong></em></p>
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
<p>Required.</p>
<p>Must be 'I', 'O', or 'U'.</p>
</blockquote></td>
<td><blockquote>
<p>Patient Class is not 'I', 'O',</p>
<p>or 'U'.</p>
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
<p>Not required. Must be</p>
<p>blank or a valid date.</p>
<p>Must be less than or</p>
<p>equal to processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Discharge Date is invalid or</p>
<p>after date of transmission.</p>
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
<p>Not required. Time must</p>
<p>be blank or a valid time.</p>
</blockquote></td>
<td><blockquote>
<p>Discharge Time is invalid</p>
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
<p>Required. Must be numeric. Must be a valid</p>
<p>date. Must be less than or</p>
<p>equal to processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Admit Date is invalid or</p>
<p>after date of transmission.</p>
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
<p>Required. Time must be</p>
<p>numeric. Must be a valid</p>
<p>time.</p>
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
<p><strong>500 Series</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>DG1 Segment</strong></em></p>
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
<p>Required. Must be a valid</p>
<p>code.</p>
<p>(Refer to table AA010)</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Diagnosis Code.</p>
<p>(Refer to table 0051)</p>
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
<p><strong>600 Series</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em><strong>OBX Segment</strong></em></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>600</p>
</blockquote></td>
<td><blockquote>
<p>Observation ID.</p>
</blockquote></td>
<td><blockquote>
<p>If not blank, must be a valid code.</p>
<p>(Refer to table NLT)</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Observation Nat Lab</p>
<p>Num. (Refer to table NLT).</p>
<p>(Also see W09)</p>
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
<p>Must be blank or a valid date. Must be numeric.</p>
<p>Must be a less than or equal to the processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Final Result Date is invalid</p>
<p>or after the date of</p>
<p>transmission.</p>
</blockquote></td>
</tr>
</tbody>
</table>

*Continued*

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 23%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>ERROR NUMBER</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>FIELD NAME</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>EDIT DESCRIPTION</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>ERROR MESSAGE</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>W00 Series</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>Warnings</em></p>
</blockquote></td>
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
<p>Patient Date of Birth is all</p>
<p>spaces. (Also see 205)</p>
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
<p>Year must not be all zeros</p>
</blockquote></td>
<td><blockquote>
<p>Patient Date of Birth Year is</p>
<p>all zeros. (See also 205)</p>
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
<p>Patient Date of Birth is not</p>
<p>in a valid date format.</p>
<p>(Also see 205)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W07</p>
</blockquote></td>
<td><blockquote>
<p>Specimen Source Code</p>
</blockquote></td>
<td><blockquote>
<p>Blanks in code.</p>
</blockquote></td>
<td><blockquote>
<p>Specimen Source code is</p>
<p>blank. (See also 310)</p>
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
<p>Observation Nat Lab Num is</p>
<p>blank. (Also see 600)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W010</p>
</blockquote></td>
<td><blockquote>
<p>Date of Prescription</p>
</blockquote></td>
<td><blockquote>
<p>Must not be all spaces.</p>
</blockquote></td>
<td><blockquote>
<p>Date of Prescription is all</p>
<p>Spaces.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>W011</p>
</blockquote></td>
<td><blockquote>
<p>Date of Prescription</p>
</blockquote></td>
<td><blockquote>
<p>Year must not be all</p>
<p>zeros.</p>
</blockquote></td>
<td><blockquote>
<p>Date of Prescription is all</p>
<p>Zeros.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W012</p>
</blockquote></td>
<td><blockquote>
<p>Date of Prescription</p>
</blockquote></td>
<td><blockquote>
<p>Must be a valid date.</p>
</blockquote></td>
<td><blockquote>
<p>Date of Prescription is not in</p>
<p>a valid date format.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>W014</p>
</blockquote></td>
<td><blockquote>
<p>Resolve Term</p>
</blockquote></td>
<td><blockquote>
<p>Must be numeric.</p>
</blockquote></td>
<td><blockquote>
<p>Resolve Term must be</p>
<p>numeric.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W015</p>
</blockquote></td>
<td><blockquote>
<p>Days Supply</p>
</blockquote></td>
<td><blockquote>
<p>Must be numeric or blank.</p>
</blockquote></td>
<td><blockquote>
<p>Days Supply not numeric</p>
<p>or blank.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>W016</p>
</blockquote></td>
<td><blockquote>
<p>Release Date</p>
</blockquote></td>
<td><blockquote>
<p>Must be numeric date. Must be a valid date.</p>
<p>Must be less than processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Release Date is invalid date</p>
<p>or after the date of</p>
<p>transmission.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W017</p>
</blockquote></td>
<td><blockquote>
<p>Fill Date</p>
</blockquote></td>
<td><blockquote>
<p>Must be numeric date. Must be a valid date. Must be less than processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Fill Date is invalid date</p>
<p>or after the date of</p>
<p>transmission.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>W018</p>
</blockquote></td>
<td><blockquote>
<p>Stop Date</p>
</blockquote></td>
<td><blockquote>
<p>Must be numeric date. Must be a valid date.</p>
<p>Must be less than processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Stop Date is invalid date</p>
<p>or after the date of</p>
<p>transmission.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W019</p>
</blockquote></td>
<td><blockquote>
<p>Primary Indicator</p>
</blockquote></td>
<td><blockquote>
<p>One DG1 diagnostic code must be designated as the primary code-valid starting with version 2 of the software.</p>
</blockquote></td>
<td><blockquote>
<p>No diagnostic code designated</p>
<p>as primary.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>W020</p>
</blockquote></td>
<td><blockquote>
<p>Release Date/Fill Date</p>
</blockquote></td>
<td><blockquote>
<p>At least one of the two</p>
<p>release date or fill date must be present.</p>
</blockquote></td>
<td><p>Release Date and Fill Date are</p>
<p>both blank.</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W021</p>
</blockquote></td>
<td><blockquote>
<p>DSP Nomenclature</p>
</blockquote></td>
<td><blockquote>
<p>Must not be all spaces.</p>
</blockquote></td>
<td>DSP Nomenclature is all spaces.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>W022</p>
</blockquote></td>
<td><blockquote>
<p>Resolve Term</p>
</blockquote></td>
<td><blockquote>
<p>Must be 1, 2, 3, 4, 5, 6, 7, or 0.</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Resolve Term</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>W023</p>
</blockquote></td>
<td><blockquote>
<p>Lab Result</p>
</blockquote></td>
<td><blockquote>
<p>Must be spaces if Resolve Term is 1, 2, 3, 4,, or 7.</p>
</blockquote></td>
<td><blockquote>
<p>Lab Result is not in sync with</p>
<p>Resolve Term.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> APPENDIX-C

> VHA DIRECTIVE 2000-019

> UNDER SECRETARY FOR HEALTH’S INFORMATION LETTER

*(This page included for two-sided copying.)*

# VHA Directive 2000-019

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                    |                            |
|------------------------------------|----------------------------|
| Department of Veterans Affairs     | VHA DIRECTIVE 2000-019 |
| Veterans Health Administration |                            |
| Washington, DC 20420           | July 19, 2000          |

> INSTALLATION OF CLINICAL REMINDERS 1.5 SOFTWARE

> 1. PURPOSE: The purpose of this Veterans Health Administration (VHA) Directive mandates the immediate installation and use of the Veterans Health Information Systems and Technology Architecture (V*IST*A) Clinical Reminders 1.5 software.

> 2\. BACKGROUND

> a\. Information Letter 10-98-013 established VA standards for evaluation and testing of veterans for Hepatitis C Virus (HCV). Software developed within the Department of Veterans Affairs (VA) assists in clinical management of veterans and provides data regarding progress toward meeting established standards.

> b\. Clinical Reminders 1.5 software is a V*IST*A product that was released to the field on June 21, 2000. This package builds on the functionality originally contained in the Patient Care Encounter package and streamlines the clinical reminders process in conjunction with guidance received from the National Advisory Council for Clinical Practice Guidelines.

> c\. Clinical Reminders 1.5 software provides the framework for the functionality of two patches that will be released soon, i.e., Laboratory software v5.2 patch (LR\* 5.2\*260) and Clinical Reminders software v1.5 (PXRM\*1.5\*1). Clinical Reminders 1.5 software does not require the Computerized Patient Record System (CPRS) Graphical User Interface (GUI); however, the CPRS GUI v14 provides additional functionality to streamline the clinical reminder process for clinicians at the point of care.

> 3. POLICY: It is VHA policy that the Clinical Reminders V*IST*A package be used to extract Hepatitis C information to augment the Emerging Pathogen Initiative (EPI) database.

> *NOTE: Patches that support the Hepatitis C reporting process depend on the presence of Clinical Reminders 1.5 software.*

> 4. ACTION: By July 30, 2000, each facility will:

> a\. Install Clinical Reminders 1.5 software. Roll-out of the patches that support the Hepatitis C reporting process will begin in August. At that time further instructions will be provided related to a phased seeding of Hepatitis C data into the national EPI database.

2.  Follow instructions in the Clinical Reminders 1.5 Installation Guide for mapping Hepatitis C risk assessment terms.

> c\. Ensure the encounter process (Automated Information Collection System (AICS), Patient Care Encounter (PCE) and CPRS GUI) utilized at each facility is set up to collect Hepatitis C risk assessment data.

> THIS VHA DIRECTIVE EXPIRES JULY 31, 2005

> d\. Set CPRS parameters to include the risk assessment reminder on the cover sheet.

> 5. REFERENCES: None.

> 6. FOLLOW-UP RESPONSIBILITY: The Office of Information (192) is responsible for the contents of this directive.

> 7. RESCISSIONS: None. This VHA Directive expires July 31, 2005.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 11%" />
<col style="width: 21%" />
<col style="width: 43%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="3"></td>
<td colspan="2"><blockquote>
<p>S/ Melinda Murphy for</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"></td>
<td colspan="2"><blockquote>
<p>Thomas L. Garthwaite, M.D.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"></td>
<td colspan="2"><blockquote>
<p>Acting Under Secretary for Health</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>DISTRIBUTION:</strong></p>
</blockquote></td>
<td><blockquote>
<p>CO:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>E-mailed 7/20/00</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>FLD:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>VISN, MA, DO, OC, OCRO, and 200 - FAX 7/20/00</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>EX:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Boxes 104, 88, 63, 60, 54, 52, 47, and 44 - FAX 7/20/00</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

# # Under Secretary For Health’s Information Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Available at: http://vawww.va.gov/publ/direc/health/infolet/109813.doc</u>

## IL 10-98-013

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In Reply Refer To: 11

> June 11, 1998

> UNDER SECRETARY FOR HEALTH’S INFORMATION LETTER

> HEPATITIS C: STANDARDS FOR PROVIDER EVALUATION AND TESTING

> 1\. Background: Hepatitis C virus (HCV) infection was first recognized in the 1970’s, when the majority of transfusion-associated infections were found to be unrelated to hepatitis A and B, the two hepatitis viruses recognized at the time. This transmissible disease was then simply called “non-

> A, non-B” hepatitis. Sequencing of the HCV genome was accomplished in 1989, and the term hepatitis C was subsequently applied to infection with this single strand ribonucleic acid (RNA) virus. The genome of HCV is highly heterogeneous and, thus, the virus has the capacity to escape the immune surveillance of the host; this circumstance leads to a high rate of chronic infection and lack of immunity to reinfection. Reliable and accurate (second generation) tests to detect antibody to HCV were not available until 1992, at which time an effective screening of donated blood for HCV antibody was initiated.

> 2\. HCV infection is now recognized as a serious national problem. Nearly 4 million Americans are believed to be infected, and approximately 30,000 new infections occur annually. Only about 25 to 30 percent of these infections will be diagnosed. HCV is now known to be responsible for 8,000 to 10,000 deaths annually, and this number is expected to triple in the next 10 to 20 years.

> 3\. Hepatitis C has particular import for the Department of Veterans Affairs (VA) because of its prevalence in VA’s service population. For example, a 6-week inpatient survey at the VA Medical Center, Washington, DC, revealed a prevalence of 20 percent antibody positivity. A similar investigation at the VA Medical Center San Francisco, CA, found 10 percent of inpatients to be antibody positive. Veterans Health Administration (VHA) Transplant Program data reveal that 52 percent of all VA liver transplant patients have hepatitis C. An electronic survey of 125 VA medical centers conducted by the Infectious Disease Program Office from February through December of 1997, identified 14,958 VA patients who tested positive for hepatitis C antibody. Clearly, HCV infection is becoming a leading cause of cirrhosis, liver failure, and hepatocellular carcinoma. The incidence and prevalence rates are higher among nonwhite racial and ethnic groups.

> 4\. HCV is transmitted primarily by the parenteral route. Sources of infection include transfusion of blood or blood products prior to 1992, injection drug use, nasal cocaine, needlestick accidents, and, possibly, tattooing. Sexual transmission is possible, and while the risk is low in a mutually monogamous relationship, persons having multiple sexual partners are at higher risk of infection.

> 5\. After infection, 90 percent of HCV infected patients will develop viral antibodies within 3 months. The disease becomes chronic in 85 percent of those infected, although one-third will have normal aminotransferase levels. The rate of progression is variable, and chronic HCV infection leads to cirrhosis in at least 20 percent of infected persons within 20 years; 1 to 5 percent of those infected will develop hepatocellular carcinoma.

> 6\. At present, treatment for HCV infection is limited, consisting primarily of administration of interferon alpha, with or without the addition of ribavirin. The treatment benefits some patients and appears to alter the natural progression of the disease, although evidence is lacking that it will translate into improvements in quality of life or reduction in the risk of hepatic failure. Current regimens include the use of 6 or 12-month courses of interferon alpha, with or without ribavirin. The recent National Institutes of Health Consensus Statement on Hepatitis C concluded that liver biopsy should be performed prior to initiating treatment. If little liver damage is apparent, therapy need not be initiated; treatment is probably appropriate for those with significant histologic abnormalities. However, data presented at this Consensus Conference indicated that significant uncertainty remains regarding indications for treatment. Treatment options and a listing of VA protocols will be the subject of a separate Information Letter.

> 7\. A number of serologic tests are available for diagnosis and evaluation of HCV infection. Enzyme immunoassays (EIA) are “first line” tests, and are relatively inexpensive. They contain HCV antigens and detect the presence of antibodies to those antigens. Recombinant immunoblot assays (RIBA) contain antigens in an immunoblot format, and are used as supplemental or confirmatory tests. Viral RNA can be detected by reverse-transcription polymerase chain reaction (PCR) testing. Quantitative HCV RNA testing uses target amplification PCR or signal amplification (branched deoxyribonucleic acid (DNA)) techniques.

> 8\. The EIA tests have sensitivities in the range of 92 to 95 percent. Specificities depend on the risk stratification pre-testing. That is, in blood donors with no risk factors, 25 to 60 percent of positive EIA are also positive by PCR for viral RNA. About 75 percent of low risk donors with positive EIA and RIBA will be positive by PCR. Positive EIA tests should be confirmed by RIBA. If that is also positive the patient has, or has had, HCV infection. In high-risk patients who are EIA positive, particularly if there is evidence of liver disease, supplemental testing with RIBA or HCV RNA analysis is probably unnecessary. Quantitative RNA tests may be useful in the selection and monitoring of patients undergoing treatment.

> 9\. All patients will be evaluated with respect to risk factors for hepatitis C, and this assessment documented in the patient’s chart. Based upon those risk factors, antibody testing should be utilized as elaborated on in the algorithm found in Attachment A.

> S/Kenneth W. Kizer, M.D., M.P.H.

> Under Secretary for Health

> Attachment

> DISTRIBUTION: CO: E-mailed 6/11/98

> FLD: VISN, MA, DO, OC, OCRO, and 200 – FAX 6/11/98

> EX: Boxes 104,88,63,60,54,52,47,and 44 – FAX 6/11/98