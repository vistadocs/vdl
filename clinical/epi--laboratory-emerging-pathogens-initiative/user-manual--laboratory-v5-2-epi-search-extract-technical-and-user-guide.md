---
title: Laboratory Version 5.2 EPI Search/Extract Technical and User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: EPI Search/Extract Technical and
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
menu_options: 0
description: "The VISTA Laboratory Search/Extract Patch LR\5.2\175 is an enhancement to the VISTA Laboratory Emerging Pathogens Initiative Patch LR\5.2\132 software application. The Laboratory Search/Extract enhancement software supports the following two national initiatives:"
audience: 
keywords: 
  - blockquote
  - search
  - extract
  - table
  - class
  - mail
  - contents
  - laboratory
  - message
  - report
page_count: 0
word_count: 33815
section_count: 46
table_count: 9
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: September 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Emerging_Pathogens_Initiative/lab_epi_searchextract_tm_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Emerging_Pathogens_Initiative/lab_epi_searchextract_tm_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=118"
---

---
title: |
  <span id="_Toc385323587" class="anchor"></span>Laboratory

  Version 5.2

  <span id="_Toc385323589" class="anchor"></span>Search/Extract Technical and User Guide
---

![](laboratory-version-5-2-epi-search-extract-technical-and-user-guide/001.png)

September 2015

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Product Development (PD)

Revision History

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 22%" />
<col style="width: 38%" />
<col style="width: 24%" />
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
<td><p>Updates for LR*5.2*442, ICD-10 PTF Modifications:</p>
<p>Updated title page and footers, updated Preface (p.iv), added new DBIA #6130 (p.15), reformatted and updated Routine List (p.16), updated patches required (p.17), updated Installation Instructions (p.33), updated Post Installation Instructions (p.38).</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/2014</td>
<td><p>LR*5.2*421</p>
<p>p. <a href="#preface"><span>v</span></a></p>
<p>pp.<a href="#p421_14">14</a>, <a href="#p421_20">20</a>, <a href="#p421_53">53</a>, <a href="#p421_58">58</a>, <a href="#p421_87ICD">87</a>, <a href="#p421_109">109</a>, <a href="#ICD9toICDchange10">125</a>,</p>
<p>p. <a href="#Routine"><u>16</u></a></p>
<p>p. <a href="#HelpText69"><u>27</u></a></p>
<p>p. <a href="#p421_32">32</a></p>
<p>pp. <a href="#p421_17"><u>17</u></a>, <a href="#p39">33</a>, <a href="#p43"><u>37</u></a></p>
<p>p. <a href="#p421_44"><u>44</u></a></p>
<p>pp. <a href="#p421_45"><u>45</u></a>, <a href="#p421_46"><u>46</u></a>, <a href="#p421_115"><u>115</u></a>, <a href="#p421_134"><u>134</u></a>, <a href="#PII_000_SSN_4"><u>135</u></a>, <a href="#p421_138"><u>138</u></a></p>
<p>pp. <a href="#Primary_Menu_Candida"><u>61</u></a>, <a href="#Primary_Menu_Clostr"><u>65</u></a>, <a href="#Primary_Menu_Creut"><u>68</u></a>-<a href="#p75"><u>69</u></a>, <a href="#Primary_Menu_Cryp"><u>71</u></a>-<a href="#CodeSysUpdate2"><u>72</u></a>, <a href="#Primary_Menu_Dengue"><u>74</u></a>-<a href="#ICDCodeAdd2"><u>75</u></a>, <a href="#Primary_Menu_E_Coli"><u>78</u></a>-<a href="#ICDCodeAdd3"><u>79</u></a>, <a href="#Primary_Menu_Hep"><u>81</u></a>-<a href="#ICDCodeAdd4"><u>82</u></a>, <a href="#Primary_Menu_Legion"><u>84</u></a>-<a href="#ICDCodeAdd5"><u>85</u></a>, <a href="#Primary_Menu_Leis"><u>87</u></a>-<a href="#ICD9toICDchange6"><u>88</u></a>, <a href="#Primary_Menu_Malaria"><u>90</u></a>-<a href="#ICDCodeAdd6"><u>91</u></a>, <a href="#Primary_Menu_PEN"><u>93</u></a>-<a href="#ICDCodeAdd7"><u>94</u></a>, <a href="#Primary_Menu_Strep"><u>96</u></a>-<a href="#ICDCodeAdd8"><u>97</u></a>, <a href="#Primary_Menu_Tuber"><u>99</u></a>-<a href="#ICDCodeAdd9"><u>100</u></a>, <a href="#Primary_Menu_VAN"><u>103</u></a>, <a href="#Primary_Menu_NCH"><u>128</u></a>-<a href="#ICDCodeAdd11"><u>129</u></a>, <a href="#Primary_Menu_NCH_PAP"><u>131</u></a>-<a href="#ICDCodeAdd12"><u>132</u></a>, <a href="#p150"><u>144</u></a></p>
<p>Multiple pages</p>
<p>Multiple pages</p></td>
<td><p>Updated for ICD-10 Remediation:</p>
<p>Added Revision History.</p>
<p>Updated TOC.</p>
<p>Updated information in Preface.</p>
<p>General Changes from ICD-9 to ICD</p>
<p>Updated Routine List and updated Software Requirements</p>
<p>Updated File (#69.5) file fields for Help.</p>
<p>Added fields to Data Dictionary.</p>
<p>Added notes that refer users to the LR*5.2*421 Release Notes for Required Patches, Installation and Post Installation instructions.</p>
<p>Updated DG1 Segment of HL7 message to utilize ~ rather than ^.</p>
<p>Removed Personally Identifiable Information (PII).</p>
<p>Updated Primary Menu and examples for addition of Code System prompt.</p>
<p>Changed ICDM-9 to ICD-10.</p>
<p>Austin Automation Center (AAC) changed to Austin Information Technology Center (AITC)</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/2008</td>
<td>LR*5.2*175</td>
<td>Initial release.</td>
<td>VA OI&amp;T</td>
</tr>
</tbody>
</table>

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [VISTA Laboratory Search/Extract Patch LR\5.2\175 Technical and User Guide Sections:](#vista-laboratory-searchextract-patch-lr52175-technical-and-user-guide-sections)
- [Overview](#overview)
  - [Mandate](#mandate)
  - [Functionality](#functionality)
    - [Mail Messages](#mail-messages)
  - [Enhancements](#enhancements)
    - [Cytology Search](#cytology-search)
    - [New Option](#new-option)
    - [Input Screens](#input-screens)
    - [Mail Groups](#mail-groups)
    - [LRNCH Protocol](#lrnch-protocol)
    - [### New mail messages](#new-mail-messages)
    - [Files](#files)
  - [Modifications](#modifications)
    - [Files Renamed](#files-renamed)
    - [Menu Renamed](#menu-renamed)
    - [Options Renamed](#options-renamed)
    - [Option Replaced](#option-replaced)
  - [Orientation](#orientation)
    - [Screen Displays](#screen-displays)
    - [Computer Dialogue](#computer-dialogue)
    - [User Response](#user-response)
    - [Return Symbol](#return-symbol)
    - [Tab Symbol](#tab-symbol)
    - [Technical and User Guide Distributions](#technical-and-user-guide-distributions)
    - [Hard Copy](#hard-copy)
    - [Electronic Distributions](#electronic-distributions)
    - [ANONYMOUS.SOFTWARE Accounts](#anonymoussoftware-accounts)
    - [References](#references)
- [Pre-Installation Information](#pre-installation-information)
  - [Hardware and Operating System Requirements](#hardware-and-operating-system-requirements)
    - [Digital Equipment Corporation (DEC) Alpha Series](#digital-equipment-corporation-dec-alpha-series)
    - [Personal Computer (PC) System](#personal-computer-pc-system)
  - [System Performance Capacity](#system-performance-capacity)
  - [Installation Time](#installation-time)
  - [Users on the System](#users-on-the-system)
  - [Staffing Requirements](#staffing-requirements)
    - [IRM Staff](#irm-staff)
    - [Laboratory Staff](#laboratory-staff)
  - [Periodic Reviews](#periodic-reviews)
  - [Backup Routines](#backup-routines)
  - [Test Sites](#test-sites)
  - [Kernel Installation and Distribution System (KIDS)](#kernel-installation-and-distribution-system-kids)
  - [Database Integration Agreements (DBIA)](#database-integration-agreements-dbia)
  - [DBIA \#418 DBIA \#1372 DBIA \#1888 DBIA \#2488](#dbia-418-dbia-1372-dbia-1888-dbia-2488)
  - [Namespace](#namespace)
  - [Routine List](#routine-list)
  - [VISTA Software Requirements](#vista-software-requirements)
  - [Patches Required](#patches-required)
  - [Health Level Seven (HL7)](#health-level-seven-hl7)
  - [Domain](#domain)
  - [Protocols](#protocols)
  - [Mail Groups](#mail-groups-1)
  - [Laboratory Search/Extract Menu and Options](#laboratory-searchextract-menu-and-options)
  - [Laboratory Search/Extract Parameters Input Screen](#laboratory-searchextract-parameters-input-screen)
  - [Prompts Definitions](#prompts-definitions)
  - [VISTA Lab Search/Extract Files Data Dictionaries](#vista-lab-searchextract-files-data-dictionaries)
    - [LABORATORY SEARCH/EXTRACT PROTOCOL file (#69.4)](#laboratory-searchextract-protocol-file-694)
    - [LAB SEARCH/EXTRACT file (#69.5)](#lab-searchextract-file-695)
- [Installation Instructions](#installation-instructions)
- [Post Installation Instructions](#post-installation-instructions)
    - [DSM/Alpha and Open M Sites](#dsmalpha-and-open-m-sites)
  - [Trouble Shooting](#trouble-shooting)
  - [# Health Level Seven (HL7) Protocol](#health-level-seven-hl7-protocol)
- [EPI User Guide](#epi-user-guide)
  - [Purpose](#purpose)
  - [EPI Objective:](#epi-objective)
  - [EPI Data Transmission](#epi-data-transmission)
    - [EPI HL7 formatted Mail Messages](#epi-hl7-formatted-mail-messages)
    - [EPI Verification Report Mail Messages](#epi-verification-report-mail-messages)
    - [EPI Confirmation Mail Messages](#epi-confirmation-mail-messages)
    - [EPI Processing Report Mail Message](#epi-processing-report-mail-message)
  - [Austin Automation Center Database Processing](#austin-automation-center-database-processing)
    - [Numerator file:](#numerator-file)
    - [Denominator file:](#denominator-file)
  - [Lab Search/Extract Protocol Edit \[LREPI PROTOCOL EDIT\] option](#lab-searchextract-protocol-edit-lrepi-protocol-edit-option)
  - [EPI Descriptions and Input Examples](#epi-descriptions-and-input-examples)
  - [Laboratory Search/Extract Parameters Input Screen](#laboratory-searchextract-parameters-input-screen-1)
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
  - [EPI Helpful Hints:](#epi-helpful-hints)
    - [Clostridium difficile](#clostridium-difficile)
    - [Validating EPI Data Capture](#validating-epi-data-capture)
    - [Emerging Pathogens Verification Report Message](#emerging-pathogens-verification-report-message)
    - [Protocols](#protocols-1)
    - [Domain](#domain-1)
    - [EPI Mail Groups](#epi-mail-groups)
    - [Office of the Director (00)](#office-of-the-director-00)
    - [EPI Mail Groups](#epi-mail-groups-1)
    - [Adding Mail Groups](#adding-mail-groups)
    - [Starting the Lower Level Protocol of the HL7 V. 1.6 Background Job](#starting-the-lower-level-protocol-of-the-hl7-v-16-background-job)
    - [EPI HL7 Format Mail Message](#epi-hl7-format-mail-message)
    - [EPI Confirmation Message](#epi-confirmation-message)
    - [EPI Processing Report](#epi-processing-report)
    - [EPI Table of Reject and Warning Codes](#epi-table-of-reject-and-warning-codes)
- [NCH User Guide](#nch-user-guide)
  - [Overview](#overview-1)
    - [Mandate](#mandate-1)
    - [NCH Database Access](#nch-database-access)
    - [Impact](#impact)
    - [National Roll-Up](#national-roll-up)
    - [NCH Search and Extract Criteria](#nch-search-and-extract-criteria)
    - [Recommended Users](#recommended-users)
    - [Periodic Reviews](#periodic-reviews-1)
    - [NCH Data Transmission](#nch-data-transmission)
    - [Cholesterol Screening](#cholesterol-screening)
    - [Papanicolaou (Pap) Screening](#papanicolaou-pap-screening)
  - [NCH Mail Messages](#nch-mail-messages)
    - [NCH Verification Report mail message](#nch-verification-report-mail-message)
    - [NCH HL7 Mail Message Status List](#nch-hl7-mail-message-status-list)
    - [NCH HL7 Formatted (Acknowledgment) mail message](#nch-hl7-formatted-acknowledgment-mail-message)
    - [NCH Acknowledgment mail message](#nch-acknowledgment-mail-message)
  - [NCH VA Alert](#nch-va-alert)
- [Editing Files/Screens, Linking Data, Request Form](#editing-filesscreens-linking-data-request-form)
  - [Editing TOPOGRAPHY file (#61)](#editing-topography-file-61)
  - [How to Link Antimicrobial Entries to Workload Codes Entries](#how-to-link-antimicrobial-entries-to-workload-codes-entries)
    - [Using the Antimicrobial Link Update \[LREPILK\] options](#using-the-antimicrobial-link-update-lrepilk-options)
    - [How to Delete an Entry from the Laboratory Search/Extract Parameters Input Screen](#how-to-delete-an-entry-from-the-laboratory-searchextract-parameters-input-screen)
    - [How to add an entry using the Laboratory Search/Extract Parameters Input Screen](#how-to-add-an-entry-using-the-laboratory-searchextract-parameters-input-screen)
    - [Additional Workload and Suffixes Codes Request Form](#additional-workload-and-suffixes-codes-request-form)
The Veterans Health Information Systems and Architecture (*VISTA*) Laboratory Search/Extract Patch LR\*5.2\*175 Technical and User Guide provides assistance for installing, implementing, and maintaining the *VISTA* Laboratory Search/Extract Patch LR\*5.2\*175 software application.
<span id="Preface" class="anchor"></span>The International Classification of Diseases, Tenth Revision (ICD-10) Remediation patch LR\* 5.2\*421 makes the following changes to the Emerging Pathogens Initiative (EPI) application:
- The following fields and screens have been updated to refer to “ICD” rather than “ICD9”:
  - Laboratory Search/Extract Parameters Input screens
  - Enter/Edit Local Pathogens screens
  - Detailed Verification Report
  - Help text
- Within the Enter/Edit Local Pathogens and Laboratory Search/Extract Parameters Input screens, users are prompted to specify a code set on which to search prior to entering an ICD code. Based on this input, the system will only allow ICD-9 entry or ICD-10 entry.
- The Pathogen Inquiry option has been modified to list both ICD-9 and ICD-10 codes.
- The Generate Local Report/Spreadsheet option has been modified to include both the Diagnosis Code Set Designation and the Diagnosis Code.
- Health Level 7 (HL7) Reports that are sent to Austin Information Technology Center (AITC) have been modified to include ICD-10 Codes and Descriptions, which are included in the DG1 HL7 Segments.
The ICD-10 PTF Modifications patch LR\*5.2\*442 made changes to accommodate the expanded number of ICD-10 codes that can now be entered in a patient record.Recommended Users:
Department of Veterans Affairs Medical Center (DVAMC) Information Resource Management (IRM) staff
Laboratory Information Manager (LIM)
Representative from the Microbiology section for the Emerging Pathogens Initiative (i.e., director, supervisor, or technologist)
Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) staff (or person at the facility with similar function)

## VISTA Laboratory Search/Extract Patch LR\*5.2\*175 Technical and User Guide Sections:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre-Installation Information: This section contains pre-installation information.

Installation Instructions: This section of the guide provides an example of the V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 installation process.

Post Installation Instructions: This section provides all the necessary information required for the IRM and LIM staff to implement the software application.

Appendix A - EPI User Guide: The EPI User Guide provides the necessary information for implementing and maintaining the EPI search/extract criteria.

Appendix B - NCH User Guide: The NCH User Guide provides the necessary information for implementing and maintaining the NCH search/extract criteria.

Appendix C - Editing Files, Input Screens, Linking Data, and Request Form: This section provides instructions for editing files, input screens, linking data, and a Workload and Suffixes Codes Request Form.

Table of Contents

VISTA Laboratory Search/Extract Patch LR\*5.2\*175 Technical and User Guide Sections: [vi](#vista-laboratory-searchextract-patch-lr5.2175-technical-and-user-guide-sections)

Overview [1](#_Toc428460942)

Mandate [1](#mandate)

Functionality [2](#functionality)

Mail Messages [2](#mail-messages)

EPI Mail Messages: [3](#epi-mail-messages)

EPI HL7 formatted Mail Messages [3](#epi-hl7-formatted-mail-messages)

EPI Verification Report Mail Messages [3](#epi-verification-report-mail-messages)

EPI Confirmation Mail Messages [3](#epi-confirmation-mail-messages)

EPI Processing Report Mail Message [3](#epi-processing-report-mail-message)

NCH Mail Messages: [4](#nch-mail-messages)

NCH HL7 Formatted Mail Messages [4](#nch-hl7-formatted-mail-messages)

NCH Verification Report mail messages [4](#nch-verification-report-mail-messages)

HL7 Message Status List [4](#hl7-message-status-list)

NCH HL7 formatted Acknowledgment mail message [4](#nch-hl7-formatted-acknowledgment-mail-message)

NCH Acknowledgment mail message [5](#nch-acknowledgment-mail-message)

NCH VA Alert mail message [5](#nch-va-alert-mail-message)

Enhancements [6](#enhancements)

Cytology Search [6](#cytology-search)

New Option [6](#new-option)

Input Screens [6](#input-screens)

Mail Groups [6](#mail-groups)

LRNCH Protocol [7](#lrnch-protocol)

New mail messages [7](#new-mail-messages)

Files [7](#files)

LAB SEARCH/EXTRACT PROTOCOL file (#69.4) New Fields [7](#lab-searchextract-protocol-file-69.4-new-fields)

LAB SEARCH/EXTRACT file (#69.5) New Fields [7](#lab-searchextract-file-69.5-new-fields)

Modifications [9](#modifications)

Files Renamed [9](#files-renamed)

Menu Renamed [9](#menu-renamed)

Options Renamed [9](#options-renamed)

Option Replaced [9](#option-replaced)

Orientation [11](#orientation)

Screen Displays [11](#screen-displays)

Computer Dialogue [11](#computer-dialogue)

User Response [11](#user-response)

Return Symbol [11](#return-symbol)

Tab Symbol [11](#tab-symbol)

Technical and User Guide Distributions [12](#technical-and-user-guide-distributions)

Hard Copy [12](#hard-copy)

Electronic Distributions [12](#electronic-distributions)

ANONYMOUS.SOFTWARE Accounts [12](#anonymous.software-accounts)

References [12](#references)

Pre-Installation Information [13](#pre-installation-information)

Hardware and Operating System Requirements [13](#hardware-and-operating-system-requirements)

Digital Equipment Corporation (DEC) Alpha Series [13](#digital-equipment-corporation-dec-alpha-series)

Personal Computer (PC) System [13](#personal-computer-pc-system)

System Performance Capacity [13](#system-performance-capacity)

Installation Time [13](#installation-time)

Users on the System [14](#users-on-the-system)

Staffing Requirements [14](#staffing-requirements)

IRM Staff [14](#irm-staff)

Laboratory Staff [14](#laboratory-staff)

Periodic Reviews [14](#periodic-reviews)

Backup Routines [15](#backup-routines)

Test Sites [15](#_Toc428460996)

Kernel Installation and Distribution System (KIDS) [15](#kernel-installation-and-distribution-system-kids)

Database Integration Agreements (DBIA) [15](#database-integration-agreements-dbia)

Namespace [16](#namespace)

Routine List [16](#_Toc428461000)

V*IST*A Software Requirements [17](#vista-software-requirements)

Patches Required [17](#patches-required)

Health Level Seven (HL7) [17](#health-level-seven-hl7)

Domain [17](#domain)

Protocols [18](#protocols)

Mail Groups [18](#mail-groups-1)

Laboratory Search/Extract Menu and Options [19](#laboratory-searchextract-menu-and-options)

Laboratory Search/Extract Parameters Input Screen [20](#laboratory-searchextract-parameters-input-screen)

Prompts Definitions [20](#prompts-definitions)

V*IST*A Lab Search/Extract Files Data Dictionaries [22](#vista-lab-searchextract-files-data-dictionaries)

LABORATORY SEARCH/EXTRACT PROTOCOL file (#69.4) [22](#laboratory-searchextract-protocol-file-69.4)

LAB SEARCH/EXTRACT file (#69.5) [25](#lab-searchextract-file-69.5)

Installation Instructions [33](#installation-instructions)

Post Installation Instructions [38](#post-installation-instructions)

DSM/Alpha and Open M Sites [38](#dsmalpha-and-open-m-sites)

Trouble Shooting [42](#trouble-shooting)

Health Level Seven (HL7) Protocol [44](#health-level-seven-hl7-protocol)

APPENDIX - A [52](#appendix---a)

EPI User Guide [54](#epi-user-guide)

Purpose [54](#purpose)

EPI Objective: [54](#epi-objective)

EPI Data Transmission [55](#epi-data-transmission)

EPI HL7 formatted Mail Messages [55](#epi-hl7-formatted-mail-messages-1)

EPI Verification Report Mail Messages [55](#epi-verification-report-mail-messages-1)

EPI Confirmation Mail Messages [55](#epi-confirmation-mail-messages-1)

EPI Processing Report Mail Message [55](#epi-processing-report-mail-message-1)

Austin Automation Center Database Processing [56](#austin-automation-center-database-processing)

Numerator file: [56](#numerator-file)

Denominator file: [57](#denominator-file)

Lab Search/Extract Protocol Edit \[LREPI PROTOCOL EDIT\] option [58](#lab-searchextract-protocol-edit-lrepi-protocol-edit-option)

EPI Descriptions and Input Examples [59](#epi-descriptions-and-input-examples)

Laboratory Search/Extract Parameters Input Screen [60](#laboratory-searchextract-parameters-input-screen-1)

Candida (Reference \#8) [61](#candida-reference-8)

Clostridium difficile (Reference \#4) [65](#clostridium-difficile-reference-4)

Creutzfeldt-Jakob Disease (CJD) (Reference \#13) [69](#creutzfeldt-jakob-disease-cjd-reference-13)

Cryptosporidium (Reference \#9) [72](#cryptosporidium-reference-9)

Dengue (Reference \#12) [75](#dengue-reference-12)

E. coli O157:H7 (Reference \#10) [78](#e.-coli-o157h7-reference-10)

Hepatitis C Antibody Positive (Reference \#2) [81](#hepatitis-c-antibody-positive-reference-2)

Legionella (Reference \#7) [84](#legionella-reference-7)

Leishmaniasis (Reference \#14) [88](#leishmaniasis-reference-14)

Malaria (Reference \#11) [91](#malaria-reference-11)

Penicillin- Resistant Pneumococcus (Reference \#3) [94](#penicillin--resistant-pneumococcus-reference-3)

Streptococcus-Group A (Reference \#6 [97](#streptococcus-group-a-reference-6)

Tuberculosis (Reference \#5) [100](#tuberculosis-reference-5)

Vancomycin-Resistant Enterococcus (VRE) (Reference \#1) [103](#vancomycin-resistant-enterococcus-vre-reference-1)

Conclusion [107](#conclusion)

EPI Helpful Hints: [108](#epi-helpful-hints)

Clostridium difficile [108](#clostridium-difficile)

Validating EPI Data Capture [110](#validating-epi-data-capture)

Emerging Pathogens Verification Report Message [111](#emerging-pathogens-verification-report-message)

Protocols [113](#protocols-1)

Domain [113](#domain-1)

EPI Mail Groups [113](#epi-mail-groups)

Office of the Director (00) [113](#office-of-the-director-00)

EPI Mail Groups [114](#epi-mail-groups-1)

Adding Mail Groups [115](#adding-mail-groups)

Starting the Lower Level Protocol of the HL7 V. 1.6 Background Job [115](#starting-the-lower-level-protocol-of-the-hl7-v.-1.6-background-job)

EPI HL7 Format Mail Message [116](#epi-hl7-format-mail-message)

EPI Confirmation Message [116](#epi-confirmation-message)

EPI Processing Report [117](#epi-processing-report)

EPI Table of Reject and Warning Codes [118](#epi-table-of-reject-and-warning-codes)

NCH User Guide [124](#nch-user-guide)

Overview [124](#overview-1)

Mandate [125](#mandate-1)

NCH Database Access [125](#nch-database-access)

Impact [125](#impact)

National Roll-Up [125](#national-roll-up)

NCH Search and Extract Criteria [126](#nch-search-and-extract-criteria)

Recommended Users [126](#recommended-users)

Periodic Reviews [126](#periodic-reviews-1)

NCH Data Transmission [127](#nch-data-transmission)

NCH HL7 formatted mail messages [127](#nch-hl7-formatted-mail-messages-1)

NCH Verification Report mail message [127](#nch-verification-report-mail-message)

NCH Acknowledgment mail message [127](#nch-acknowledgment-mail-message-1)

NCH VA View Alert mail message [127](#nch-va-view-alert-mail-message)

Cholesterol Screening [128](#cholesterol-screening)

Cholesterol Screening for Hyperlipidemia [128](#cholesterol-screening-for-hyperlipidemia)

Papanicolaou (Pap) Screening [132](#papanicolaou-pap-screening)

Pap Smear for Cervical Cancer [132](#pap-smear-for-cervical-cancer)

NCH Mail Messages [135](#nch-mail-messages-1)

NCH HL7 Formatted Mail Message [135](#nch-hl7-formatted-mail-message)

NCH Verification Report mail message [136](#nch-verification-report-mail-message-1)

NCH HL7 Mail Message Status List [137](#nch-hl7-mail-message-status-list)

NCH HL7 Formatted (Acknowledgment) mail message [138](#nch-hl7-formatted-acknowledgment-mail-message-1)

NCH Acknowledgment mail message [139](#nch-acknowledgment-mail-message-2)

NCH VA Alert [140](#nch-va-alert)

Editing Files/Screens, Linking Data, Request Form [144](#editing-filesscreens-linking-data-request-form)

Editing TOPOGRAPHY file (#61) [144](#editing-topography-file-61)

How to Link Antimicrobial Entries to Workload Codes Entries [145](#how-to-link-antimicrobial-entries-to-workload-codes-entries)

Using the Antimicrobial Link Update \[LREPILK\] options [145](#using-the-antimicrobial-link-update-lrepilk-options)

How to link entries using the AUTO option [145](#how-to-link-entries-using-the-auto-option)

How to add and delete entries to a file using the MANUAL option [145](#how-to-add-and-delete-entries-to-a-file-using-the-manual-option)

How to add entries using the SEMI-AUTO option. [146](#how-to-add-entries-using-the-semi-auto-option.)

How to Delete an Entry from the Laboratory Search/Extract Parameters Input Screen [147](#how-to-delete-an-entry-from-the-laboratory-searchextract-parameters-input-screen)

How to add an entry using the Laboratory Search/Extract Parameters Input Screen [148](#how-to-add-an-entry-using-the-laboratory-searchextract-parameters-input-screen)

Additional Workload and Suffixes Codes Request Form [149](#additional-workload-and-suffixes-codes-request-form)

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 is an enhancement to the V*IST*A Laboratory Emerging Pathogens Initiative Patch LR\*5.2\*132 software application. The Laboratory Search/Extract enhancement software supports the following two national initiatives:

1.  Emerging Pathogens Initiative (EPI): The Department of Veterans Affairs (DVA) Headquarters Infectious Disease Program Office assists with identifying new antibiotic-resistant, otherwise problematic pathogens within the DVA. Using this objective information, plans may be formulated on a national level for intervention strategies and resource needs. Results from the aggregate data may also be shared with the appropriate public health authorities for planning on the national level (i.e., private health care sectors).
2.  National Center for Health PromotionCholesterol and Pap Screening (NCH): Pursuant to the Congressional mandates stipulated in its enabling legislation (PL. 102-585, U.S.C. 17, 1704), the Department of Veterans Affairs (DVA) National Center for Health Promotion (NCHP) is tasked with monitoring and improving the prevalence of health promotion screening activities provided to veterans VA-wide. The purpose of the NCH Cholesterol and Pap Screening database is to monitor cholesterol and Pap screening activities at a national level, with the ultimate goal for improving detection and treatment of hyperlipidemia and cervical cancer. The NCH Cholesterol and Pap Screening database will also provide a valuable resource for clinical and health services researchers on screening activities and health outcomes, particularly for high-risk and special emphasis group such as veterans with hyperlipidemia, older veterans, and female veterans.

## Mandate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of the V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 software should be completed in accordance with PL. 102-585, U.S.C. 17, 1704. It is recommended that all VAMCs installed and implemented the software as soon as possible to help facilitate these important initiatives.

## Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 enhancement software application tracks the EPI and NCH ongoing initiatives within the VAMCs without the necessity of any additional data entry. The software will automatically search and extract data from several V*IST*A Software databases (e.g., Laboratory, PIMS, and Social Work). The LAB DATA file (#63) (i.e., contains verified lab data results), PTF file (#45), and the PATIENT file (#2) data are used for the defined search/extract criteria.

The V*IST*A Laboratory Search/Extract software application automatically generates the data as defined by the EPI and NCH criteria’s. The EPI search/extract data is processed on the 15<sup>th</sup> of each month. The NCH search/extract data is processed daily.

### Mail Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 enhancement software application automatically processes the EPI and NCH data producing HL7 formatted mail messages. A Verification Report mail message is then produced for each HL7 formatted mail message. The HL7 formatted mail messages are used for sending the EPI and NCH data to the Austin Information Technology Center (AITC) database.

The Verification Report mail message is a copy of the HL7 formatted mail messages in a human readable format. The Verification Report allows the users to review the EPI and NCH data and make corrections (e.g., complete social security numbers, valid Date of Births, and Period of Services, etc.) as deemed necessary.

The new Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option enables the user to generate a Verification Report mail message (i.e., human readable format) as often as needed for reviewing the EPI and NCH data. This option will automatically send the NCH data to the AITC database each time the option is manually run.

#### EPI Mail Messages:

> **NOTE:** See Appendix A for examples of the EPI mail messages.

#### EPI HL7 formatted Mail Messages

The V*IST*A Laboratory Search/Extract software automatically processes the EPI data on the 15<sup>th</sup> of each month producing HL7 formatted mail messages. A Verification Report mail message is then produced (i.e., in a human readable format) for each HL7 mail message. The EPI HL7 formatted mail messages must be manually forwarded on the 15<sup>th</sup> of each month to the AITC database via the Q-EPI.XXX.XX.XXX domain. Use the VA MailMan software to manually forward the EPI data to XXX@ Q-EPI.XXX.XX.XXX domain.

#### EPI Verification Report Mail Messages

The EPI Verification Report mail messages are sent to the EPI-REPORT mail group on the 15<sup>th</sup> of each month. The members of the EPI-REPORT mail group should review the EPI Verification Report and make data corrections (e.g., social security number, date of birth, period of service, etc.) as deemed necessary. The software automatically processes the EPI data corrections on the 15<sup>th</sup> of each month. Note: The EPI Verification Report may be generated as often as needed using the new Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option.

#### EPI Confirmation Mail Messages

EPI Confirmation mail messages are sent to the sending facility EPI-REPORT mail group after the EPI HL7 mail messages has been received by the AITC database.

#### EPI Processing Report Mail Message

EPI Processing Report mail messages are sent to the sending facility EPI-REPORT mail group at the end of the AITC processing cycle (i.e., the 25<sup>th</sup> of each month). The EPI Processing Report mail messages confirms that the EPI data has been processed and lists any errors and/or warning codes requiring corrections.

#### NCH Mail Messages:

> **NOTE:** See Appendix B for examples of the NCH mail messages.

#### NCH HL7 Formatted Mail Messages

The V*IST*A Laboratory Search/Extract software automatically processes the NCH data daily producing HL7 formatted mail messages. A Verification Report mail message is then produced (i.e., in a human readable forma) for each HL7 formatted mail message. The software automatically transmits the NCH HL7 formatted mail messages daily to the AITC database.

#### NCH Verification Report mail messages

The NCH Verification Report mail messages are generated daily and sent to the LR NCH-Report mail group. The members of the LR NCH-Report mail group may use the Verification Report to review the NCH data and make corrections (e.g., social security number, date of birth, period of service, etc.) as deemed necessary. The new Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option enables the users to generate the NCH Verification Report and to transmit the NCH data corrections to the AITC database as often as needed.

#### HL7 Message Status List

The HL7 Message Status List contains the status of each transmission sent by the site to the AITC database.

#### NCH HL7 formatted Acknowledgment mail message

The NCH HL7 formatted Acknowledgment mail message is sent by the AITC to the sending site. This message is translated in a human readable format and sent to the LR NCH Report mail group.

#### NCH Acknowledgment mail message

The NCH Acknowledgment mail message displays the status of the NCH HL7 formatted mail message transmission to the AITC. The NCH Acknowledgment mail message is sent to the LR NCH-Report mail group.

#### NCH VA Alert mail message

A NCH VA Alert mail message is sent to the LABORATORY SEARCH/EXTRACT PROTOCOL file (#69.4), Report Mail Group field (#1), after the NCH data has been processed by the AITC.

## Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 software consists of the following enhancements:

### Cytology Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cytology Search/Extract searches the LAB DATA file (#63) based on the criteria defined by the NCH Cholesterol and NCH Pap search criteria in the LAB SEARCH/EXTRACT file (#69.5).

### New Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option: This option is used to run the EPI or NCH extracts manually.

Lab Search/Extract Protocol Edit \[LREPI PROTOCOL EDIT\] option: Use this option to edit the LAB SEARCH/EXTRACT PROTOCOL file (#69.4).

### Input Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Emerging Pathogens Parameters Input Screen is renamed Laboratory Search/Extract Parameters Input Screen. The Laboratory Search/Extract Parameters Input Screens were enhanced by adding a fifth screen to accommodate the following four new prompts (i.e., Lag Days, Sex, Before Date of Birth, and After Date of Birth).

### Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch LR\*5.2\*175 automatically installs the LR NCH and LR NCH-Report mail groups during the installation process. The LR NCH and LR NCH-Report mail groups Coordinator(s) may be entered doing the installation process. Other mail groups members must be added to the mail groups after the installation process.

### LRNCH Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LRNCH protocol is added to the LAB SEARCH/EXTRACT file (69.5), Protocol field (#12) during patch installation process.

### ### New mail messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- NCH HL7 formatted mail messages
- NCH Verification Report mail messages
- NCH HL7 formatted Status List
- NCH HL7 formatted (Acknowledgment) mail messages
- NCH Acknowledgment messages
- NCH VA Alert messages

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### LAB SEARCH/EXTRACT PROTOCOL file (#69.4) New Fields

Send Alert field (#3): Enter 1 for YES to receive an alert when a search is run automatically.

Receive Alert field (#5): Select the user (s) or group responsible for receiving alerts when the search has been executed automatically.

Title field (#4): This field will over-ride the default title for the Verification Report. If this field is left, blank the default title <u>Verification Report</u> will be used.

#### LAB SEARCH/EXTRACT file (#69.5) New Fields

Lag Days field (#5): This is the number of days that the search should wait after the test was ordered to ensure that the results have been entered in the system. Enter the number of lag days desired. The amounts allowed will vary depending on the type.

Sex field (#16):FOR FUTURE USE ONLYBefore Date of Birth field (#17): Patients born after the date entered will not be included in the report. Enter a date to screen out patients born after the date entered.

After Date of Birth field (#18): Persons born before the entered will not be included in the report.

SNOMED Codes field (#8): This is a list of SNOMED codes to be included in the search.

PTF field (#14): This field is used to follow the inpatient PTF information.

## Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Listed below are the modifications made to the V*IST*A Laboratory Emerging Pathogens Initiative (EPI) Patch LR\*5.2\*132 software application files, menu, and options. These modifications were made to accomplish the enhancements for the V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 software application.

### Files Renamed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EMERGING PATHOGENS PROTOCOL file (#69.4) is renamed the LAB SEARCH/EXTRACT PROTOCOL file (#69.4).

The EMERGING PATHOGENS file (#69.5) is renamed the LAB SEARCH/EXTRACT file (#69.5).

### Menu Renamed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Emerging Pathogens Primary Menu \[LREPI EMERGING PATHOGENS MENU\] is renamed the Lab Search/Extract Primary Menu \[LREPI SEARCH EXTRACT MENU\].

### Options Renamed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Emerging Pathogens Parameter Setup \[LREPI PARAMETER UPDATE\] option is renamed the Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option.

The Emerging Pathogens Nightly Task \[LREPI NIGHTLY TASK\] is renamed the Lab Search/Extract Nightly Task \[LREPI NIGHTLY TASK\].

### Option Replaced

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Emerging Pathogens Manual Run \[LREPI (EPI) MANUAL RUN\] option is replaced with the new Lab Search/Extract Manual Run (Enhanced) \[LREPI ENCHANCE MANUAL RUN\] option.

![](laboratory-version-5-2-epi-search-extract-technical-and-user-guide/002.png)

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section addresses the Laboratory Search/Extract Patch LR\*5.2\*175 Technical and User Guide computer screen dialogue, symbols, reference manuals, and the electronic and hard copy distributions.

### Screen Displays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Search/Extract Primary \[LREPI SEARCH EXTRACT MENU\] Menu options are using VA FileMan/ScreenMan forms for editing and displaying data. For detailed instructions using ScreenMan forms please refer to the VA FileMan V. 21.0 User Manual, Section 6 - ScreenMan.

### Computer Dialogue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The computer dialogue appears in Courier font, no larger than 10 points.

Example: Courier font 10 points

### User Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User entry response appears in boldface type Courier font, no larger than 10 points.

Example: Boldface type

### Return Symbol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User response to computer dialogue is followed by the \<RET\> symbol which appears in Courier font, no larger than 10 points, and bolded.

Example: \<RET\>

### Tab Symbol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User response to computer dialogue is followed by the \<Tab\> symbol that appears in Courier font, no larger than 10 points, and bolded.

Example: \<Tab\>

### Technical and User Guide Distributions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following information states how to obtain the Laboratory Search/Extract Patch LR\*5.2\*175 Technical and User Guide electronic and hard copy distributions.

### Hard Copy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory Search/Extract Patch LR\*5.2\*175 Technical and User Guide hard copies are distributed by National Center for Documentation (NCD) to all Veteran Affairs Medical Centers (VAMCs).

### Electronic Distributions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory Search/Extract Patch LR\*5.2\*175 Technical and User Guide is available on the Intranet in Hyper Text Markup Language (HTML) and Portable Document Format (PDF) at the following Intranet address: http://152.127.1.95/softserv/clin_nar.row/lab/

### ANONYMOUS.SOFTWARE Accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory Search/Extract Patch LR\*5.2\*175 Technical and User Guide is also available on the ANONYMOUS SOFTWARE accounts at the Albany, Hines, and Salt Lake City Chief Information Officer Field Offices (CIOFOs) in PDF (i.e., P175TUG.PDF) at the following FTP addresses:

CIOFOs FTP Address

<span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

<span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

<span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel V. 8.0 Systems Manual
HL7 V. 1.6 Manuals
PIMS V. 5.3 Manuals
VA FileMan V. 21.0 User Manual, Section 6 - ScreenMan
MailMan V. 7.1 Manuals

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Hardware and Operating System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

V*IST*A software operates on two hardware platforms. The hardware platforms are listed in the mini-computer category, which provides <u>multi-tasking</u> and <u>multi-user</u> capabilities. The hardware platforms systems used are:

### Digital Equipment Corporation (DEC) Alpha Series

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Digital Equipment Corporation (DEC) Alpha series is using the DEC Open Virtual Memory System (VMS), Version 6.1 or greater, operating system. This platform uses the DEC System Mumps (DSM), Version 6.3 or greater, of American National Standards Institutes (ANSI) of Massachusetts General Hospital Utility Multi-Programming System (MUMPS) also known as ‘M’ language. MUMPS is a Federal Information Processing Standard (FIPS) language.

### Personal Computer (PC) System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Personal Computer (PC) System with 486 or Pentium computer processor chip is using the Microsoft Disk Operating System (MS-DOS). The platform uses Open-M, of the American National Standards Institutes (ANSI) of Massachusetts General Hospital Utility Multi-Programming System (MUMPS) also known as 'M' language. MUMPS is a Federal Information Processing Standard (FIPS) language.

## System Performance Capacity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no changes in the performance of the system once Patch LR\*5.2\*175 is installed.

## Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation time is less than 2 minutes during off peak hours and less than 5 minutes during peak hours.

## Users on the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users may remain on system and no options need to be placed out of service.

## Staffing Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following staff is required to successfully install and implement Patch LR\*5.2\*175 software:

### IRM Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An IRM staff is required for installing Patch LR\*5.2\*175, setting up the domains, mail groups, and menu assignments.

### Laboratory Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that the following person (s) <u>jointly</u> participate in reviewing the parameter descriptions:

Laboratory Information Manager (LIM)

Representative from the Microbiology section for the Emerging Pathogens Initiative (i.e., director, supervisor, or technologist)

Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) staff (or person at the facility with similar function)

## Periodic Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Search/Extract parameter descriptions require an ongoing review process (as directed by (VAHQ) Infectious Disease Program and NHCP Offices). The person(s) participating in the ongoing review process is responsible for ensuring the following requirements are kept current:

> Periodic reviews of the <span id="p421_14" class="anchor"></span>ICD codes

> Periodic reviews of the Lab Search/Extract Parameter Setup

> Annual review of the NCHP parameter descriptions

## Backup Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is <u>highly</u> recommended that a backup of the transport global be performed before installing Patch LR\*5.2\*175.

## Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 software application was tested by the following sites:

|                                    |                 |              |
|------------------------------------|-----------------|--------------|
| Test Sites                     | Test Phases | Platform |
| <span class="mark">REDACTED</span> | Alpha           | DEC/Alpha    |
|                                    |                 |              |
| <span class="mark">REDACTED</span> | Alpha           | DEC/Alpha    |
|                                    |                 |              |
| <span class="mark">REDACTED</span> | Beta            | DEC/Alpha    |
|                                    |                 |              |
| <span class="mark">REDACTED</span> | Beta            | DEC/Alpha    |
|                                    |                 |              |
| <span class="mark">REDACTED</span> | Beta            | DEC/Alpha    |
|                                    |                 |              |
| <span class="mark">REDACTED</span> | Beta            | Open M       |

## Kernel Installation and Distribution System (KIDS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Laboratory Search/Extract Patch LR\*5.2\*175 distribution is using KIDS. For further instructions on using KIDS, please refer to the Kernel Version 8.0 Systems Manual.

## Database Integration Agreements (DBIA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new DBIA was approved for VistA Laboratory ICD-10 PTF Modifications patch LR\*5.2\*442:

- DBIA#6130

The following DBIA were approved for V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175:

## DBIA \#418 DBIA \#1372 DBIA \#1888 DBIA \#2488

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 namespace is Laboratory’s LR.

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

## V*IST*A Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Packages Versions (or Greater)

VA FileMan 21 (with patches installed)

Kernel 8.0 (with patches installed)

Laboratory 5.2 (with patches installed)

PIMS 5.3 (with patches installed)

Health Level 7 1.6 (with patches installed)

Social Work 3.0 (with patches installed)

MailMan 7.1 (with patches installed)

## Patches Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** For a list of patches required to install patch LR\*5.2\*442, please refer to the ICD-10 PTF Modifications Installation Guide: <http://www.va.gov/vdl/application.asp?appid=118>

<span id="p421_17" class="anchor"></span>NOTE: For a list of patches required to install patch LR\*5.2\*421, please refer to the ICD-10 Release Notes.

Prior to the installation of Patch LR\*5.2\*175, the following patches MUST be installed:

Packages Patches

MailMan V.7.1 XM\*DBA\*116 (NCH-Lab Domain)

Health Level Seven V. 1.6 HL\*1.6\*34

Laboratory V. 5.2 LR\*5.2\*132

LR\*5.2\*157

## Health Level Seven (HL7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 software uses the V*IST*A HL7 software to transmit data to the AITC database. The data resides in the AITC database. The data is use for assisting public health surveillance activities with new health care initiatives.

## Domain

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 software application Domain name is XXX@Q-NCH. Sites must install Patch XM\*DBA\*116. See VA MailMan V. 7.1 Manual for instruction on how to set up the domain after the patch has been installed.

## Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LRNCH is the Event Driver protocol used for sending the NCH HL7 messages to the Austin Automation Center.

LRNCH SEND CLIENT is the Client server used for sending NCH HL7 mail messages to the Austin Automation Center.

LRNCHAITC is the Subscriber server used for processing the NCH Acknowledgment mail messages received from the Austin Automation Center.

## Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Office of the Director (00) at each facility should determine responsible individual(s)/function(s) for the mail groups. The Laboratory Search/Extract Patch LR\*5.2\*175 creates the following two mail groups during the installation process.

LRNCH: This mail group is used to transmit the NCH HL7 messages derived from the parameters defined in the LAB SEARCH/EXTRACT file (#69.5) to the AITC database.

LRNCH-REPORT: This mail group delivers the Verification Report mail message and Acknowledgment mail messages (i.e., human readable format) to the recipients assigned to this mail group.

## Laboratory Search/Extract Menu and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lab Search/Extract Primary Menu \[LREPI SEARCH EXTRACT MENU\] is the only menu included with the V*IST*A Laboratory Search/Extract software. The menu contains four options. The Lab Search/Extract Nightly Task \[LREPI NIGHTLY TASK\] is a stand-alone option that is included with the software. There are no locks or security keys associated with the menu or options.

> **NOTE:** The Lab Search/Extract Primary Menu \[LREPI SEARCH EXTRACT MENU\] options are using VA FileMan screen displays, referred to as ScreenMan.

For detailed instructions on how to use the screens please review the VA FileMan V. 21.0 User Manual, Section 6 ScreenMan.

Lab Search/Extract Primary Menu \[LREPI SEARCH EXTRACT MENU\]: This is the primary menu that contains the Lab Search/Extract options.

Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCE MANUAL RUN\] option: This option is used to run the EPI and NCH extracts manually.

Antimicrobial Link Update \[LREPILK\] option: This option allows the user to link the ANTIMICROBIAL SUSCEPIBILTY file (#62.06) with the WKLD CODE file (#64).

> **NOTE:** Please see the Appendix C section of this guide for instructions on “How to Link Antimicrobial Entries to Workload Code Entries” using the Antimicrobial Link Update \[LREPILK\] option.

Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\]option: This option allows the users to setup the EPI and NCH parameter search/extract criteria.

Lab Search/Extract Protocol Edit \[LREPI PROTOCOL EDIT\] option: Use this option to edit the LAB SEARCH/EXTRACT PROTOCOL file (#69.4).

Lab Search/Extract Nightly Task \[LREPI NIGHTLY TASK\] option: The Lab Search/Extract Nightly Task \[LREPI NIGHTLY TASK\] option must be scheduled to run each night by TaskMan. This option will build a HL7 Message and send it to the defined locations specified by the EPI and NCH protocols.

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
<td><p><strong>Laboratory Search/Extract</strong></p>
<p><strong>Parameters Input Screen</strong></p>
<p><strong>Prompt Definitions</strong></p></td>
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
<p><span id="p421_20" class="anchor"></span>ICD-9</p>
</blockquote></td>
<td><blockquote>
<p>ICD-9 standardized code used nationwide in federal and non-federal/private health care facilities. Select from the ICD-9 DIAGNOSIS file (#80).</p>
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
<p>Title of ICDM diagnosis</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Selected Etiology</p>
</blockquote></td>
<td><blockquote>
<p>Consider synonymous with organism, final microbial diagnosis/isolate. Select from the ETIOLOGY FIELD file (#61.2).</p>
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
<td><p><strong>Laboratory Search/Extract</strong></p>
<p><strong>Parameters Input Screen</strong></p>
<p><strong>Prompt Definitions</strong></p></td>
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
<p>Enter the numbers of lag days desired. The number allowed will vary depending on the cycle type.</p>
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

## V*IST*A Lab Search/Extract Files Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are examples of the LABORATORY SEARCH/EXTRACT files standard Data Dictionaries:

### LABORATORY SEARCH/EXTRACT PROTOCOL file (#69.4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

STANDARD DATA DICTIONARY \#69.4 -- LAB SEARCH/EXTRACT PROTOCOL FILE 06/11/98 PAGE 1

STORED IN ^LAB(69.4, (2 ENTRIES) SITE: BROCKTON/W.ROXBURY UCI: VAH,ROU

(VERSION 5.2)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

------------------------------------------------------------------------------

This file contains additional search and extract parameters to be used by the

Laboratory Search/Extract software. These parameters are not specific to

entries in LAB SEARCH/EXTRACT file (#69.5), but are specific to the Protocol

(refer to Protocol file \#101) being used.

POINTED TO BY: PROTOCOL field (#12) of the LAB SEARCH/EXTRACT File (#69.5)

CROSS

REFERENCED BY: PROTOCOL(B)

69.4,.01 PROTOCOL 0;1 POINTER TO PROTOCOL FILE (#101)

(Required)

INPUT TRANSFORM: S DINUM=X

LAST EDITED: NOV 08, 1996

HELP-PROMPT: Select the Protocol that will be used to build

the message.

DESCRIPTION: This is the entry in the Protocol file (#101)

that will be used to build the HL7 Message.

This allows additional parameters to be

associated with the protocol.

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

CROSS-REFERENCE: 69.4^B

1)= S ^LAB(69.4,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.4,"B",\$E(X,1,30),DA)

69.4,1 Report Mail Group 0;2 POINTER TO MAIL GROUP FILE (#3.8)

LAST EDITED: NOV 08, 1996

HELP-PROMPT: Select which mail group will receive the

verification report.

DESCRIPTION: This is the mail group that will receive the

verification report.

69.4,2 Message Size 0;3 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>999999)!(X\<100)!(X?.E1"."1N.N) X

LAST EDITED: DEC 04, 1996

HELP-PROMPT: Enter the maximum number of lines a message

may contain (100 to 999999) before it breaks

into another message.

DESCRIPTION: This determines how big the HL7 message will

be before it breaks into another message.

69.4,3 Send Alert 0;4 SET

'1' FOR YES;

LAST EDITED: JUL 31, 1997

HELP-PROMPT: Enter '1' or 'YES' to send an alert when a

search is run automatically. Leave this field

blank if no alert is desired.

DESCRIPTION: When this field is set to '1' or 'YES' an

alert is transmitted to the recipients listed

in the RECEIVE ALERTS field when a search is

run automatically for this protocol.

69.4,4 Title 0;5 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>40!(\$L(X)\<2) X

LAST EDITED: AUG 01, 1997

HELP-PROMPT: Enter a new title (2 to 40 characters) for the

Verification report. If this field is left

blank the default title "Verification Report"

will be used.

DESCRIPTION: This field will over-ride the default title

for the Verification Report.

69.4,5 Receive Alerts 1;0 VARIABLE POINTER Multiple \#69.45

DESCRIPTION: This is the User(s) or Group that will receive

alerts stating the extract has been run.

automatically.

69.45,.01 Receive Alerts 0;1 VARIABLE POINTER

(Multiply asked)

FILE ORDER PREFIX LAYGO MESSAGE

200 1 U n Responsible User

3.8 2 G n Responsible Group

LAST EDITED: AUG 05, 1997

HELP-PROMPT: Select the User(s) or Group responsible for

receiving alerts that the search has been

run automatically.

DESCRIPTION: This is the user(s) or Group that will

receive alerts that the search has been run

automatically.

CROSS-REFERENCE: 69.45^B

1)= S

^LAB(69.4,DA(1),1,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.4,DA(1),1,"B",\$E(X,1,30),DA)

3)= Required Index for Variable Pointer

FILES POINTED TO FIELDS

MAIL GROUP (#3.8) Report Mail Group (#1)

PROTOCOL (#101) PROTOCOL (#.01)

INPUT TEMPLATE(S):

PRINT TEMPLATE(S):

CAPTIONED USER \#0

SORT TEMPLATE(S):

FORM(S)/BLOCK(S):

LREPIPROT SEP 05, 1997@13:34 USER \#0

LRPROTHEAD DD \#69.4

LRPROT1 DD \#69.4

LRPROT2 DD \#69.45

### LAB SEARCH/EXTRACT file (#69.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

STANDARD DATA DICTIONARY \#69.5 -- LAB SEARCH/EXTRACT FILE 06/11/98 PAGE 1

STORED IN ^LAB(69.5, (17 ENTRIES) SITE: BROCKTON/W.ROXBURY UCI: VAH,ROU

(VERSION 5.2)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

------------------------------------------------------------------------------

This file contains search criteria used by the Laboratory Search/Extract software. This file should only be edited using Lab Search/Extract Parameter Setup option \[LREPI PARAMETER SETUP\] provided with this software.

CROSS

REFERENCED BY: NAME(B), REFERENCE NUMBER(C)

69.5,.01 NAME 0;1 FREE TEXT (Required)

INPUT TRANSFORM: K:\$L(X)\>50!(\$L(X)\<3)!'(X'?1P.E)!(X'?.ANP) X

LAST EDITED: DEC 17, 1996

HELP-PROMPT: Enter a Name (3 to 50 characters) for the

Search/Extract parameter you are defining.

DESCRIPTION: This is the name of the Search/Extract

parameter you are defining.

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

CROSS-REFERENCE: 69.5^B

1)= S ^LAB(69.5,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,"B",\$E(X,1,30),DA)

69.5,.05 REFERENCE NUMBER 0;9 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>999)!(X\<1)!(X?.E1"."1N.N)!(X'\>99)!\$D

(^LAB(69.5,"C",X)) X

LAST EDITED: NOV 29, 1996

HELP-PROMPT: Type a unique number between 100 and 999 to

identify this entry. Numbers from 1 to 99 are

reserved for future use.

DESCRIPTION: This is a unique number used to identify this

entry.

UNEDITABLE

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

CROSS-REFERENCE: 69.5^C

1)= S ^LAB(69.5,"C",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,"C",\$E(X,1,30),DA)

69.5,1 ACTIVE 0;2 SET

'1' FOR YES;

'0' FOR NO;

LAST EDITED: JUN 09, 1998

HELP-PROMPT: '1' or 'YES' indicates that this is an active

entry.

DESCRIPTION: This defines if this entry is active or not.

69.5,2 LAB TEST 1;0 POINTER Multiple \#69.52

DESCRIPTION: This is the test that is to be searched for

and retrieved.

69.52,.01 LAB TEST 0;1 POINTER TO LABORATORY TEST FILE (#60)

(Multiply asked)

INPUT TRANSFORM: S DIC("S")="I

\$P(\$G(^(0)),U,4)=""CH""!(\$P(\$G(

^(0)),U,4)=""CY"")" D ^DIC K DIC S

DIC=DIE,X= +Y K:Y\<0 X

LAST EDITED: FEB 04, 1998

HELP-PROMPT: Enter the lab test that is to be searched

for and retrieved. Consider this synonymous

with chemistry, serology, hematology

“blood/serum” or Cytology tests.

DESCRIPTION: This is the lab test that is to be searched

for and retrieved.

SCREEN: S DIC("S")="I

\$P(\$G(^(0)),U,4)=""CH""!(\$P(\$G(

^(0)),U,4)=""CY"")"

EXPLANATION: Only CH subscripts are selectable.

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

CROSS-REFERENCE: 69.52^B

1)= S

^LAB(69.5,DA(1),1,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),1,"B",\$E(X,1,30),DA)

69.52,1 INDICATOR 0;2 SET

'1' FOR Use Reference Ranges;

'2' FOR Contains;

'3' FOR Greater Than;

'4' FOR Less Than;

'5' FOR Equal To;

LAST EDITED: FEB 05, 1997

HELP-PROMPT: Select the code that will determine how to

match lab results.

DESCRIPTION: This indicates if the search for the lab

testis conditional.

69.52,2 INDICATED VALUE 0;3 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>30!(\$L(X)\<1) X

LAST EDITED: FEB 05, 1998

HELP-PROMPT: Enter the data to be compared using the

INDICATOR field.

DESCRIPTION: If the search is conditional this defines

the criteria.

69.5,3 ETIOLOGY 2;0 POINTER Multiple \#69.53

DESCRIPTION: This defines the Etiology to search for.

69.53,.01 ETIOLOGY 0;1 POINTER TO ETIOLOGY FIELD FILE (#61.2)

(Multiply asked)

LAST EDITED: AUG 29, 1996

HELP-PROMPT: Select the Etiology to search for.

DESCRIPTION: This defines the Etiology to search for.

Select the appropriate Etiology.

CROSS-REFERENCE: 69.53^B

1)= S

^LAB(69.5,DA(1),2,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),2,"B",\$E(X,1,30),DA)

<span id="HelpText69" class="anchor"></span>69.5,4        ICD DIAGNOSIS          3;0 POINTER Multiple \#69.54

              LAST EDITED:      JUN 12, 2012

              DESCRIPTION:      This defines the ICD to search for. 

69.54,.01     ICD DIAGNOSIS          0;1 POINTER TO ICD DIAGNOSIS FILE (#80)

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

69.54,1       CODING SYSTEM     0;2 POINTER TO ICD CODING SYSTEMS FILE (#80.4)

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

DESCRIPTION: This determines that if any of the

selected are to be resistant to

Antimicrobials. Select the appropriate

Antimicrobials to screen out the Etiologies.

CROSS-REFERENCE: 69.55^B 1)= S

^LAB(69.5,DA(1),4,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),4,"B",\$E(X,1,30),DA)

69.5,6 INCLUDED SITES 5;0 POINTER Multiple \#69.56

LAST EDITED: OCT 04, 1996

DESCRIPTION: This determines what Topography to screen for.

69.56,.01 TOPOGRAPHY 0;1 POINTER TO TOPOGRAPHY FIELD FILE (#61)

(Multiply asked)

LAST EDITED: OCT 04, 1996

HELP-PROMPT: Selection of a Topography screens all others

out except the ones selected. For "ALL"

leave blank. Not to be used in conjunction

with the exclude Topography selection.

DESCRIPTION: This determines what Topography to screen

for. Select the appropriate Topography to

include in the extract.

CROSS-REFERENCE: 69.56^B

1)= S

^LAB(69.5,DA(1),5,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),5,"B",\$E(X,1,30),DA)

69.5,7 EXCLUDED SITES 6;0 POINTER Multiple \#69.57

DESCRIPTION: This determines what Topography to screen

out.

69.57,.01 TOPOGRAPHY 0;1 POINTER TO TOPOGRAPHY FIELD FILE (#61)

(Multiply asked)

LAST EDITED: OCT 04, 1996

HELP-PROMPT: Select the Topography to screen out. Not to

be used in conjunction with the Include

Topography selection.

DESCRIPTION: This determines what Topography to screen

out. Select the appropriate Topography to be

excluded from the extract.

CROSS-REFERENCE: 69.57^B

1)= S ^LAB(69.5,DA(1),6,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),6,"B",\$E(X,1,30),DA)

69.5,8 SNOMED CODES 9;0 Multiple \#69.58

DESCRIPTION: This is a list of SNOMED codes to be included

in the search.

69.58,.01 SNOMED CODES 0;1 FREE TEXT (Multiply asked)

INPUT TRANSFORM: K:\$L(X)\>15!(\$L(X)\<1) X

LAST EDITED: AUG 20, 1997

HELP-PROMPT: Enter any SNOMED codes to be included in the

search. Enter one code per line.

DESCRIPTION: This is a list of SNOMED code to be included

in the search.

CROSS-REFERENCE: 69.58^B

1)= S

^LAB(69.5,DA(1),9,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),9,"B",\$E(X,1,30),DA)

69.5,9 RUN DATE 0;4 DATE

INPUT TRANSFORM: S %DT="ESTX" D ^%DT S X=Y K:Y\<1 X

LAST EDITED: FEB 06, 1997

HELP-PROMPT: Enter the date that the last Auto

Search/Extract processed.

DESCRIPTION: The date that the last Auto Search/Extract

processed

69.5,10 CYCLE 0;5 SET

'M' FOR MONTHLY;

'D' FOR DAILY;

LAST EDITED: DEC 03, 1997

HELP-PROMPT: Select whether this parameter is to be used

'D'aily or 'M'onthly

DESCRIPTION: This field defines how often the this entry is

acted upon by the nightly task.

CROSS-REFERENCE: ^^TRIGGER^69.5^10.5

1)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S

Y(1)=\$S(\$D(

^LAB(69.5,D0,0)):^(0),1:"") S

X=\$P(Y(1),U,3),X=X S DIU=X K Y S X=""

X ^DD(69.5,10,1,1,1.4) 1.4)= S

DIH=\$S(\$D(^LAB(69.5,DIV(0),0)):^(0),1:"

"),DIV=X S \$P(^(0),U,3)=DIV,DIH=69.5,DIG=10.5

D^DICR:\$O(^DD(DIH,DIG,1,0))\>0

2)= K DIV S DIV=X,D0=DA,DIV(0)=D0 S

Y(1)=\$S(\$D(^LAB(69.5,D0,0)):^(0),1:"")

S X=\$P(Y(1),U,3),X=X S DIU=X K Y S X=""

X ^DD(69.5,10,1,1,2.4)

2.4)= S

DIH=\$S(\$D(^LAB(69.5,DIV(0),0)):^(0),1:

" "),DIV=X S

\$P(^(0),U,3)=DIV,DIH=69.5,DIG=10.5 D

^DICR:\$O(^DD(DIH,DIG,1,0))\>0

CREATE VALUE)= ""

DELETE VALUE)= ""

FIELD)= LAG DAY

69.5,10.5 LAG DAYS 0;3 NUMBER

INPUT TRANSFORM: S CYC=\$P(^LAB(69.5,DA,0),U,5),MAX=\$S(CYC="D":99

,CYC="M":26,1:0) K:+X'=X!(X\>MAX)!(X\<1)!(X?.E1".

"1N.N) X K MAX,CYC

LAST EDITED: SEP 04, 1997

HELP-PROMPT: Enter the numbers of lag days desired. The

amount allowed will vary depending on the

cycle type.

DESCRIPTION: This is the number of days that the search

should wait after the test was ordered to

ensure that the results have been entered in

the system.

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

TRIGGERED by the CYCLE field of the LAB

SEARCH/EXTRACT File

69.5,11 FIRST ENCOUNTER 0;6 SET

'1' FOR YES;

'0' FOR NO;

LAST EDITED: DEC 30, 1996

HELP-PROMPT: Enter '1' to limit the output to the first

encounter for the patient. '0' will list all

encounters.

DESCRIPTION: This determines if after the first encounter

is found and extracted should sequential

encounters be extracted.

69.5,12 PROTOCOL 0;7 POINTER TO LAB SEARCH/EXTRACT PROTOCOL

FILE (#69.4)

LAST EDITED: NOV 08, 1996

HELP-PROMPT: Select the Protocol to be used to define the

output messages.

DESCRIPTION: This defines what protocol is associated with

the parameters.

69.5,13 FOLLOW PTF 0;8 SET

'1' FOR YES;

'0' FOR NO;

LAST EDITED: OCT 17, 1996

HELP-PROMPT: 'YES' or '1' indicates that the PTF record

will be followed until a discharge has been

entered.

DESCRIPTION: This determines whether the discharge

information should be updated upon discharge

if an inpatient encounter does not have an

existing discharge.

69.5,14 PTF 7;0 POINTER Multiple \#69.514

(Add New Entry without Asking)

DESCRIPTION: This is the PTF file entry to be followed.

69.514,.01 PTF 0;1 POINTER TO PTF FILE (#45)

LAST EDITED: OCT 17, 1996

HELP-PROMPT: Enter the PTF file entry to be followed.

DESCRIPTION: This is the PTF file entry to be followed.

CROSS-REFERENCE: 69.514^B

1)= S

^LAB(69.5,DA(1),7,"B",\$E(X,1,30),DA)=""

2)= K ^LAB(69.5,DA(1),7,"B",\$E(X,1,30),DA)

69.514,1 DATE 0;2 DATE

INPUT TRANSFORM: S %DT="E" D ^%DT S X=Y K:Y\<1 X

LAST EDITED: DEC 31, 1996

HELP-PROMPT: Enter the date that the Inpatient discharge

information was included in the report as an

update.

DESCRIPTION: This is the date that the Inpatient

discharge information was included in the

report as a update.

69.5,15 Description 8;0 WORD-PROCESSING \#69.515

DESCRIPTION: This is the general description for the

entry.

69.5,16 SEX 0;10 SET

'M' FOR MALE;

'F' FOR FEMALE;

'O' FOR OTHER;

LAST EDITED: NOV 17, 1997

HELP-PROMPT: Enter the sex code to be included in the

search. Leave blank if all types are to be

included.

DESCRIPTION: This is the sex code to be included in the

search. All types will be included if this

field is left blank.

69.5,17 BEFORE DATE OF BIRTH 0;11 DATE

INPUT TRANSFORM: S %DT="EX" D ^%DT S X=Y K:Y\<1 X

LAST EDITED: NOV 17, 1997

HELP-PROMPT: Enter a date to screen out patients born after

the date entered.

DESCRIPTION: Patients born after the date entered will not

be included in the report.

69.5,18 AFTER DATE OF BIRTH 0;12 DATE

INPUT TRANSFORM: S %DT="EX" D ^%DT S X=Y K:Y\<1 X

LAST EDITED: NOV 17, 1997

HELP-PROMPT: A birthrate to screen patients. i.e. patients

DOB after 1/1/1950.

before the date entered.

DESCRIPTION: Persons born before the entered will not be

included in the report.

FILES POINTED TO FIELDS

ANTIMICROBIAL SUSCEPTIBILITY (#62.06) ANTIMICROBIAL SUSCEPTIBILITY:ANTIMICROBIAL SUSCEPTIBILITY (#.01)

<span id="p421_32" class="anchor"></span>ETIOLOGY FIELD (#61.2)            ETIOLOGY:ETIOLOGY (#.01)

ICD CODING SYSTEMS (#80.4)        ICD DIAGNOSIS:CODING SYSTEM (#1)

ICD DIAGNOSIS (#80)               ICD DIAGNOSIS:ICD DIAGNOSIS (#.01)

LAB SEARCH/EXTRACT PROTOCOL(#69.4)PROTOCOL (#12)

LABORATORY TEST (#60) LAB TEST:LAB TEST (#.01)

PTF (#45) PTF:PTF (#.01)

TOPOGRAPHY FIELD (#61) INCLUDED SITES:TOPOGRAPHY (#.01)

EXCLUDED SITES:TOPOGRAPHY (#.01)

INPUT TEMPLATE(S):

PRINT TEMPLATE(S):

CAPTIONED USER \#0

SORT TEMPLATE(S):

FORM(S)/BLOCK(S):

LREPI OCT 07, 1996@10:13 USER \#0

LREPIHEAD DD \#69.5

LREPI2 DD \#69.52

LREPI3 DD \#69.54

LREPI1 DD \#69.5

LREPI11 DD \#69.5

LREPI4 DD \#69.53

LREPI5 DD \#69.55

LREPI6 DD \#69.5

LREPI12 DD \#69.58

LREPI7 DD \#69.5

LREPI8 DD \#69.56

LREPI9 DD \#69.57

LREPI13 DD \#69.5

LREPI10 DD \#69.5

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** For patch LR\*5.2\*442 installation instructions, please refer to the ICD-10 PTF Modifications Installation Guide: <http://www.va.gov/vdl/application.asp?appid=118>

<span id="p39" class="anchor"></span>

> **NOTE:** For Patch LR\*5.2\*421 installation instructions, please refer to the ICD-10 Release Notes.

The V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 is using the Kernel Installation and Distribution System (KIDS).

> **NOTE:** For further instructions on using KIDS, please refer to the Kernel V. 8.0 Systems Manual, Chapter 26, pages 393-409.

1.  Use the 'INSTALL/CHECK MESSAGE' option on the PackMan menu. This option will load the KIDS package in this message onto your system.
2.  Review your mapped set. If the routines are mapped, they should be removed from the mapped set at this time.
3.  The patch has now been loaded into a Transport global on your system. You now need to use KIDS to install the Transport global. On the KIDS menu, under the Installation menu, use the following options:

> Print Transport Global

> Compare Transport Global to Current System

> Verify Checksums in Transport Global

> Backup a Transport Global

4.  Users may remain on system and no options need to be placed out of service.
5.  Installation time is less than 2 minutes during off peak hours and less than 5 minutes during peak hours.
6.  Installation of this patch requires no additional memory space.
7.  From the Installation Menu of the KIDS menu, run the option Install Package(s)

> Select the package LR\*5.2\*175 and proceed with the install.

8.  If any routines were unmapped as part of step 2, they should be returned to the mapped set once the installation has run to completion.
9.  Delete routine LR175 and LR175P.
10. Remove the Emerging Pathogens Manual Run \[LREPI (EPI) MANUAL RUN\] option.

Example: Terminal screen dialogue seen during the KIDS install (dates shown in the example will not be the same as those in the released version).

Select Programmer Options Option: KID Kernel Installation & Distribution System\<RET\>

Select Kernel Installation & Distribution System Option: INstallation\<RET\>

Select Installation Option: MAILMan Menu\<RET\>

VA MailMan 7.1 service for DOE.DAVID_R@JDV.ISC-DALLAS.VA.GOV

You last used MailMan: 01 Jun 98 14:12

You have 1 new message.

Select MailMan Menu Option: NEW messages and responses\<RET\>

Subj: LR\*5.2\*175 \[#15320\] 9 Jun 1998 16:50 EST 6046 Lines

From: \<"NPM \[#27200849\]"@FORUM.VA.GOV\> in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

\$TXT Created by DOE DAVID R at BROCKTON.VA.GOV (KIDS) on TUESDAY, 06/09/98 at 16:15

=============================================================================

Run Date: JUN 09, 1998 Designation: LR\*5.2\*175

Package : LR - LAB SERVICE Priority: Mandatory

Version : 5.2 Status: Under Development

=============================================================================

Subject: HEALTH PROMOTIONS ENHANCE TO EPI

Category:

\- Routine

\- Enhancement (Mandatory)

\- Other

Select MESSAGE Action: IGNORE (in IN basket)//X\<RET\>

Select PackMan function: 6 INSTALL/CHECK MESSAGE\<RET\>

Line 3 Message \#13928486 Unloading KIDS Distribution LR\*5.2\*175

LR\*5.2\*175

Want to Continue with Load? YES//\<RET\>

Loading Distribution.

LR\*5.2\*175

Will first run the Environment Check Routine, LR175

Select PackMan function:\<RET\>

Select MESSAGE Action: IGNORE (in IN basket)// ^ \<RET\>

Ignored

Select MailMan Menu Option:\<RET\>

Select Installation Option: INstall Package(s)\<RET\>

Select INSTALL NAME: LR\*5.2\*175 Loaded from Distribution 7/10/98@14:31:58

=\> LR\*5.2\*175

This Distribution was loaded on Jul 10, 1998@14:31:58 with header of

LR\*5.2\*175

It consisted of the following Install(s):

LR\*5.2\*175

LR\*5.2\*175

Will first run the Environment Check Routine, LR175

Environment Check is Ok ---

Install Questions for LR\*5.2\*175

Incoming Files:

69.4 LAB SEARCH/EXTRACT PROTOCOL

\*BUT YOU ALREADY HAVE ‘EMERGING PATH’ PROTOCOL' AS File \#69.4!

Shall I write over your EMERGING PATH’ PROTOCOL File? YES//\<RET\>

69.5 LAB SEARCH/EXTRACT

\*BUT YOU ALREADY HAVE ‘EMERGING PATHOGENSS’AS File \#69.5!

Shall I write over your EMERGING PATHOGENSS File? YES//\<RET\>

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'LR NCH': DOE BLOW BD

Enter the Coordinator for Mail Group 'LR NCH-REPORT': DOE BLOW BD

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//NO\<RET\>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \[Enter your site printer’s name\]\<RET\>

Adding Protocol 'LRNCH' to the LAB SEARCH/EXTRACT File (69.5)

Updating Routine file

Updating KIDS files

LR\*5.2\*175 Installed.

Jul 10, 1998@14:33:47.

Install Message sent \#13928998

------------------------------------------------------------------------------

100% 25 50 75

Complete

Install Completed

# Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="p43" class="anchor"></span>NOTE: There are no post installation instructions for LR\*5.2\*442.NOTE: For Patch LR\*5.2\*421 post installation instructions, please refer to the ICD-10 Release Notes for LR\*5.2\*421.

It is highly recommended that the Laboratory Search/Extract Patch LR\*5.2\*175 post installation instructions are done in the following order:

### DSM/Alpha and Open M Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have disabled journaling, you may now re-enable journaling. If using a mapped system, rebuild the map set now.

IRM - Step \#1: Ensure that XXX@Q-NCH domain is defined as instructed by VA MailMan V.7.1, Patch XM\*DBA\*116.

IRM – Step \#2: Add designated members to the LR NCH and LR NCH-Report mail groups.

> **NOTE:** The Office of the Director should designate the recipients of these mail groups.

Example: LR NCH mail group setup

NAME: LRNCH TYPE: public

ALLOW SELF ENROLLMENT?: NO REFERENCE COUNT: 56

LAST REFERENCED: MAY 01, 1998 RESTRICTIONS: UNRESTRICTED

COORDINATOR: DOE BLOW

MEMBER: \[Enter Member’s Name\]

MEMBER: \[Enter Member’s Name\]

DESCRIPTION: LRNCH Mail group

REMOTE MEMBERS:XXX@Q-NCH

Example: LR NCH-Report mail group setup

NAME: LRNCH-REPORT TYPE: public

ALLOW SELF ENROLLMENT?: NO REFERENCE COUNT: 56

LAST REFERENCED: MAY 01, 1998 RESTRICTIONS: UNRESTRICTED

COORDINATOR: DOE BLOW

MEMBER: \[Enter Member’s Name\]

MEMBER: \[Enter Member’s Name\]

DESCRIPTION: LR NCH-REPORT Mail group

IRM - Step \#3: Assign the Lab Search/Extract Primary \[LREPI SEARCH EXTRACT MENU\] menu to the designated user(s).

> **NOTE:** It is highly recommended that a LIM, TQI/QA/QI, and a representative from the Microbiology section for EPI (e.g., director, supervisor, or technologist) be assigned the Lab Search/Extract Primary \[LREPI SEARCH EXTRACT MENU\] menu. These individuals should be responsible for initially setting up the NCH parameters and performing periodic reviews to ensure that the parameters remain current.

LIM - Step \#4: Use the Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] option to set up the NCH Cholesterol and Pap smear parameters (e.g., in Appendix B). Lab test names for Cholesterol and Pap smears may differ at each site.

> **NOTE:** The user assigned the Lab Search/Extract Primary Menu \[LREPI SEARCH EXTRACT MENU\] should be designated to set up the parameters.

To verify that the fields in the LAB SEARCH/EXTRACT file (#69.5) are correctly defined, do a VA FileMan inquiry of the file. The fields should be defined in File (#69.5) as shown in the example below.

Example: NCH Cholesterol setup

NAME: NCH CHOLESTEROL ACTIVE: NO\<RET\>

LAG DAYS: 10\<RET\> RUN DATE: JUN 22, 1998

CYCLE: DAILY\<RET\> PROTOCOL: LRNCH\<RET\>

FOLLOW PTF: YES\<RET\> REFERENCE NUMBER: 50

LAB TEST: CHOLESTEROL\<RET\>

LAB TEST: HDL CHOLESTEROL\<RET\>

LAB TEST: TRIGLYCERIDE\<RET\>

LAB TEST: LDL CHOLESTEROL\<RET\>

LAB TEST: HEALTH FAIR-CHOLESTEK PANEL\<RET\>Example: NCH Pap Smear setup

NAME: NCH PAP SMEAR ACTIVE: NO

LAG DAYS: 10 RUN DATE: JUN 22, 1998

CYCLE: DAILY PROTOCOL: LRNCH

FOLLOW PTF: YES REFERENCE NUMBER: 51

SEX: FEMALE

LAB TEST: PAP SMEAR

TOPOGRAPHY: VAGINAL CYTOLOGIC MATERIAL

TOPOGRAPHY: CERVICAL CYTOLOGIC MATERIAL

IRM - Step \#5: Set up the EPI and LRNCH protocols using the Lab Search/Extract Protocol Edit \[LREPI PROTOCOL EDIT\] option.

Example: EPI Protocol Setup

Protocol Parameters Setup Definition

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PROTOCOL: LREPI

Title: Emerging Pathogens Initiative (EPI) Message Size: 32000

Report Mail Group: EPI-REPORT

Send Alert: YES

Send Alert To

DOE,JaneExample: LRNCH Protocol Setup

Protocol Parameters Setup Definition

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PROTOCOL: LRNCH

Title: National Center for Health Promotion Message Size: 32000

Report Mail Group: LR NCH-REPORT

Send Alert: YES

Send Alert To

DOE,JaneIRM - Step \#6: Start the Lower Level Protocol of the HL7 V. 1.6 background job.

Example:

Select Systems Manager Menu Option:HL7 Main\<RET\>Menu

1 V1.5 OPTIONS

2 V1.6 OPTIONS ...

3 Activate/Inactivate Application

4 Print/Display Menu ...

5 Purge Message Text File Entries

Select HL7 Main Menu Option: 2\<RET\>V1.6 OPTIONS

1 Communications Server

2 Interface Workbench

3 Message Requeuer

Select V1.6 OPTIONS Option: 1\<RET\> Communications Server

1 Edit Communication Server parameters

2 Manage incoming & outgoing filers ...

3 Monitor incoming & outgoing filers

4 Start LLP

5 Stop LLP

6 Systems Link Monitor

7 Logical Link Queue Management ...

8 Report

Select Communications Server Option: 4\<RET\> Start LLP

This option is used to launch the lower level protocol for the appropriate device. Please select the node with which you want to communicate.

Select HL LOGICAL LINK NODE: LRNCH\<RET\>

The LLP was last shutdown on JAN 30, 1997 12:06:19.

Select one of the following:

F FOREGROUND

B BACKGROUND

Q QUIT

Method for running the receiver: B//\<RET\> ACKGROUND

Job was queued as 131225.

IRM - Step \#7: Schedule the Lab Search/Extract Nightly Task \[LREPI NIGHTLY TASK\] option to run nightly.

Example: Select OPTION to schedule or reschedule: LREPI NIGHTLY TASK\<RET\>

Lab Search/Extract Nightly Task

...OK? Yes//\<RET\> (Yes)

\(R\)

Edit Option Schedule

Option Name: LREPI NIGHTLY TASK

Menu Text: Lab Search/Extract Nightly Task TASK ID: 2298854

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: APR 29,1998@01:45\<RET\>

DEVICE FOR QUEUED JOB OUTPUT:\<RET\>

QUEUED TO RUN ON VOLUME SET: ROU\<RET\>

RESCHEDULING FREQUENCY: 1D\<RET\>

TASK PARAMETERS:\<RET\>

SPECIAL QUEUEING:\<RET\>

## Trouble Shooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. If a NCH HL7 mail message is sent to the AITC but a NCH Verification Report mail message was not sent to the users please check the following:

- Check the LR NCH and LR NCH-Report mail group memberships.
- Check the member’s name in the MAIL GROUP file (#3.8), Remote field (#12) in the LR NCH mail group for incorrect member names.
- Ensure that the LABORATORY SEARCH/EXTRACT PROTOCOL file (#69.4), Report Mail Group field (#1) entry contains LR NCH-Report.

> 2\. If no VA Alert mail messages are sent, please check for the following:

- Ensure that the LABORATORY SEARCH/EXTRACT PROTOCOL file (#69.4), Send Alert field (#3) is set to “YES”.
3.  If the Lab Search/Extract Nightly Task \[LREPI NIGHTLY TASK\] option job does not generate a NCH HL7 mail message and Verification Report mail message but the new Lab Search/Extract Manual Run (Enhanced) \[LREPI (EPI) ENHANCED MANUAL RUN\] option does, please check the following:
- Ensure that the LABORATORY SEARCH/EXTRACT file (#69.5), Active field (#1) entry for the NCH Cholesterol and NCH Pap smear Search/Extract is set to “NO”.

## # Health Level Seven (HL7) Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 software application uses the V*IST*A Laboratory, PIMS, and Social Work databases for the EPI and NCH search/extract criteria. The V*IST*A HL7 software is used to transmit the data to the AITC database.

3. General Specifications

3.1 Communication Protocol

The electronic V*IST*A MailMan software application is used as the communications protocol for sending the EPI and NCH HL7 mail messages between V*IST*A database and AITC database.

3.2 Application Processing Rules

The HL7 protocol itself describes the basic rules for application processing by the sending and receiving systems. The HL7 Version 2.2 protocol is used. The ORU message is sent using the HL7 batch protocol.

3.3 Message

The following HL7 mail message is used to support the exchange of data.

ORU Observational Results Unsolicited

3.4 Segments

The following HL7 segments are used to support the exchange of data.

DG1 Diagnosis OBX Observation Results

MSH Message Header PID Patient Identification

NTE Notes and Comments PV1 Patient Visit

OBR Observation Request

3.5 Fields

The HL7 fields on the following page are used to support the exchange of data for each of the segments listed in the 3.4 Segments.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 14%" />
<col style="width: 61%" />
<col style="width: 13%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td>FIELD</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>SEGMENT</td>
<td>SEQUENCE</td>
<td>FIELD ELEMENT NAME</td>
<td>USER/HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>NUMBER</td>
<td></td>
<td>DEFINED</td>
</tr>
<tr class="even">
<td><strong>DG1</strong></td>
<td>1</td>
<td>Set ID-Diagnosis (Sequence #)</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>Diagnosis Code (Code(id) <span id="p421_44" class="anchor"></span>~Text (St.) ~ Name of coding system (st)</td>
<td>HL7</td>
</tr>
<tr class="even">
<td><strong>MSH</strong></td>
<td>1</td>
<td>Field Separator</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Encoding Characters</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Sending Application</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>Sending Facility</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>5</td>
<td>Receiving Application</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>6</td>
<td>Receiving Facility</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>Date/Time of Message</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td>Security</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>9</td>
<td>Message Type</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>10</td>
<td>Message Control ID</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>11</td>
<td>Processing ID</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>12</td>
<td>Version ID</td>
<td>HL7</td>
</tr>
<tr class="even">
<td><strong>OBR</strong></td>
<td>1</td>
<td>Set ID-Observation Request (Seq #)</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>4</td>
<td>Universal Service ID (identifier^ text ^ name of coding system ^ alt id ^ alt text ^ alt coding system)</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>Observation Date/Time</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>15</td>
<td>Specimen Source (Specimen source code (CE) ^^ text (TX) )</td>
<td>HL7 (Table 0070)</td>
</tr>
<tr class="even">
<td></td>
<td>26</td>
<td>Parent Results (OBX observation id of parent ^OBX sub ID</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td><strong>NTE</strong></td>
<td>1</td>
<td>Set ID Notes and Comments (Seq #)</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Comment</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td><strong>OBX</strong></td>
<td>1</td>
<td>Set Id-Observational Simple (seq. #)</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>2</td>
<td>Value Type</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>3</td>
<td>Observation Identifier (identifier ^ text ^ name of coding system ^ alt id ^ alt text ^ alt coding system)</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>4</td>
<td>Sub Id</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>Observation Value (Result)</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>6</td>
<td>Units (Units)</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td>Abnormal Flags</td>
<td>HL7 (Table 0078)</td>
</tr>
<tr class="even">
<td></td>
<td>15</td>
<td>Date/Time of the Observation (Verified Date/Time)</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td><strong>PID</strong></td>
<td>2</td>
<td>Patient ID (External ID)</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>3</td>
<td>Patient ID (Internal ID)</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>5</td>
<td>Patient Name</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>7</td>
<td>Date of Birth</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>8</td>
<td>Sex</td>
<td>HL7 (Table 0001)</td>
</tr>
<tr class="even">
<td></td>
<td>10</td>
<td>Race</td>
<td>HL7 (Table VA07)</td>
</tr>
<tr class="odd">
<td></td>
<td>11</td>
<td>Address (Homeless)</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>19</td>
<td>SSN</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>27</td>
<td><p>Veteran’s Military Status</p>
<p>Period Of Service</p></td>
<td>HL7 (Table Va011)</td>
</tr>
<tr class="even">
<td><strong>PV1</strong></td>
<td>1</td>
<td>Set ID - Patient Visit</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>2</td>
<td>Patient Class</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>36</td>
<td>Discharge Disposition</td>
<td>HL7</td>
</tr>
<tr class="odd">
<td></td>
<td>44</td>
<td>Admit Date/Time (Event Date/Time)</td>
<td>HL7</td>
</tr>
<tr class="even">
<td></td>
<td>45</td>
<td>Discharge Date/Time</td>
<td>HL7</td>
</tr>
</tbody>
</table>

4.0 Transaction Specifications

4.1 General

The V*IST*A software sends an ORU observation result type HL7 message whenever one or more of the defined initiatives are identified.

4.2 Specific Transaction

*A. Identified Encounter*

When EPI and NCHP-CPSdb data are identified an ORU message is sent to the AITC. These ORU messages consist of the following segments:

Example: EPI ORU Message

ORU OBSERVATIONAL RESULT UNSOLICITED

MSH Message Header

NTE Notes and Comments

PID Patient Identification

PV1 Patient Visit

NTE Notes and Comments

DG1 Diagnosis

OBR Observation Report

OBX Results

MSH\|~\|\\\|EPI-XXX\|170\|EPI-XXX\|170\|19961018113521\|\|ORU~R01\|107\|P\|2.2\|\|\|\|\|USA

NTE\|\|REPORTING DATE FROM 19850101 TO 19961018

PID\|1\|<span id="p421_45" class="anchor"></span>000-16-7946~0~M10\|5~5~M10\|\|EPI~PATONE\|\|19220912\|M\|\|7\|\|\|\|\|\|\|\|\|000167946

PV1\|1\|O\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|19950315151907

NTE\|1\|Vanc-Res Enterococcus

DG1\|1\|\|451.19^DEEP PHLEBITIS-LEG NEC^I9

DG1\|2\| \|511.9~PLEURAL EFFUSION NOS~I9

DG1\|3\| \|670.02~MAJOR PUERP INF-DEL P/P~I9

DG1\|4\| \|331.0~ALZHEIMER'S DISEASE~I9

DG1\|5\| \|500.~COAL WORKERS' PNEUMOCON~I9

OBR\|1\|\|\|^CHEMISTRY TEST^VANLT\|\|\|19950315151907\|\|\|\|\|\|\|\|SER^^SERUM

OBX\|1\|ST\|84330.0000^Glucose Quant^VANLT^175^GLUCOSE1^VA60\|\|25\|mg/dL\|70-125\|L\*

NTE\|2\|2^Hepatitis C antibody

OBR\|2\|\|\|^CHEMISTRY TEST^VANLT\|\|\|19950315151907\|\|\|\|\|\|\|\|SER^^SERUM

OBX\|1\|ST\|84330.0000^Glucose Quant^VANLT^175^GLUCOSE1^VA60\|\|25\|mg/dL\|70-125\|L\*

PID\|2\|000-45-6666~8~M10\|7~7~M10\|\|EPI~PATTWO\|\|19591229\|F\|\|7\|\|\|\|\|\|\|\|\|000456666

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

Example: NCH ORU Mail Message

MSH^~\|\\^NCH-LAB^525^NCH-LAB^525^19980416021403^^ORU~R01^1741793^P^2.2^^^NE^AL^USA\|

NTE^^~REPORTING DATE FROM 19980415 TO 19980415~2

PID^50^<span id="p421_46" class="anchor"></span>666-16-1010~4~M10^69836~2~M10^^TESTONE, PATIENT^^19230609^M^^6^~02132^^^^ ^^^^666161010^^^^^^^^2

PV1^1^O^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^19980414075625

NTE^1^50~NCH CHOLESTEROL

OBR^1^^^81121.0000~CHEMISTRY TEST~VANLT^^^19980414075625^^^^^^^^SER\~~SERUM^^^R/

CH 0414 333

OBX^1^ST^82466.0000~Cholesterol Total~VANLT~183~CHOLESTEROL~VA60^^227^mg/dl^" S

EE TEST DESC"-^^^^^^^19980414100054

OBX^2^ST^83013.0000~Cholesterol HDL~VANLT~244~HDL CHOLESTEROL~VA60^^pending^mg/

dl^30-65^^^^^^^19980414100054

OBX^3^ST^82350.0000~Calculation~VANLT~901~LDL CHOLESTEROL~VA60^^pending^mg/dl^"

SEE TEST DESC"-^^^^^^^19980414100054

OBX^4^ST^84480.0000~Triglycerides w o extract~VANLT~205~TRIGLYCERIDE~VA60^^230^

mg/dl^35-200^H^^^^^^19980414100054

PID^51^000-54-0927~4~M10^73453~2~M10^^EPI~PATTHREE~E.^^19620728^F^^7^~02332

^^^^^^^^000540927^^^^^^^^X

PV1^1^O^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^19980414101934

NTE^1^50~NCH CHOLESTEROL

OBR^1^^^81121.0000~CHEMISTRY TEST~VANLT^^^19980414101934^^^^^^^^SER\~~SERUM^^^R/

CH 0414 439

OBX^1^ST^82466.0000~Cholesterol Total~VANLT~183~CHOLESTEROL~VA60^^169^mg/dl^

SEE TEST DESC -^^^^^^^19980414115804

OBX^2^ST^83013.0000~Cholesterol HDL~VANLT~244~HDL CHOLESTEROL~VA60^^pending^mg/

dl^30-65^^^^^^^19980414115804

OBX^3^ST^82350.0000~Calculation~VANLT~901~LDL CHOLESTEROL~VA60^^pending^mg/dl^"

SEE TEST DESC"-^^^^^^^19980414115804

OBX^4^ST^84480.0000~Triglycerides w o extract~VANLT~205~TRIGLYCERIDE~VA60^^72^m

g/dl^35-200^^^^^^^19980414115804

PID^52^000-30-6640~4~M10^74913~4~M10^^EPI~PATSEVEN.^^19400125^M^^7^~02021^^^^^

^^^000306640^^^^^^^^5

PV1^1^O^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^19980414112550

NTE^1^50~NCH CHOLESTEROL

OBR^1^^^81121.0000~CHEMISTRY TEST~VANLT^^^19980414112550^^^^^^^^SER\~~SERUM^^^R/

CH 0414 530

OBX^1^ST^82466.0000~Cholesterol Total~VANLT~183~CHOLESTEROL~VA60^^257^mg/dl^" S

EE TEST DESC"-^^^^^^^19980414141943

PID^53^000-42-9046~8~M10^75677~2~M10^^EPI JR.~PATFOUR.^^19490720^M^^6^~145

85^^^^^^^^000429046^^^^^^^^7

PV1^1^I^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^19980413164159

NTE^1^50~NCH CHOLESTEROL

OBR^1^^^81121.0000~CHEMISTRY TEST~VANLT^^^19980414060010^^^^^^^^SER\~~SERUM^^^R/

CH 0414 306

OBX^1^ST^82466.0000~Cholesterol Total~VANLT~183~CHOLESTEROL~VA60^^169^mg/dl^

SEE TEST DESC-^^^^^^^19980414094610

OBX^2^ST^83013.0000~Cholesterol HDL~VANLT~244~HDL CHOLESTEROL~VA60^^pending^mg/

dl^30-65^^^^^^^19980414094610

OBX^3^ST^82350.0000~Calculation~VANLT~901~LDL CHOLESTEROL~VA60^^pending^mg/dl^"

SEE TEST DESC"-^^^^^^^19980414094610

OBX^4^ST^84480.0000~Triglycerides w o extract~VANLT~205~TRIGLYCERIDE~VA60^^184^

mg/dl^35-200^^^^^^^19980414094610

Table VA011 - Period of Service

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Value</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>0</td>
<td><blockquote>
<p>KOREAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>WORLD WAR I</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>WORLD WAR II</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>SPANISH AMERICAN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>PRE-KOREAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>POST-KOREAN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>OPERATION DESERT SHIELD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>VIETNAM ERA</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>POST-VIETNAM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>OTHER OR NONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>A</td>
<td><blockquote>
<p>ARMY--ACTIVE DUTY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>B</td>
<td><blockquote>
<p>NAVY, MARINE--ACTIVE DUTY</p>
</blockquote></td>
</tr>
<tr class="even">
<td>C</td>
<td><blockquote>
<p>AIR FORCE--ACTIVE DUTY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>D</td>
<td><blockquote>
<p>COAST GUARD--ACTIVE DUTY</p>
</blockquote></td>
</tr>
<tr class="even">
<td>E</td>
<td><blockquote>
<p>RETIRED, UNIFORMED FORCES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>F</td>
<td><blockquote>
<p>MEDICAL REMEDIAL ENLIST</p>
</blockquote></td>
</tr>
<tr class="even">
<td>G</td>
<td><blockquote>
<p>MERCHANT SEAMEN--USPHS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>H</td>
<td><blockquote>
<p>OTHER USPHS BENEFICIARIES</p>
</blockquote></td>
</tr>
<tr class="even">
<td>I</td>
<td><blockquote>
<p>OBSERVATION/EXAMINATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>J</td>
<td><blockquote>
<p>OFFICE OF WORKERS COMP.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>K</td>
<td><blockquote>
<p>JOB CORPS/PEACE CORPS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>L</td>
<td><blockquote>
<p>RAILROAD RETIREMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>M</td>
<td><blockquote>
<p>BENEFICIARIES-FOREIGN GOV</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>N</td>
<td><blockquote>
<p>HUMANITARIAN (NON-VET)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>O</td>
<td><blockquote>
<p>CHAMPUS RESTORE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>P</td>
<td><blockquote>
<p>OTHER REIMBURS. (NON-VET)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Q</td>
<td><blockquote>
<p>OTHER FEDERAL - DEPENDENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>R</td>
<td><blockquote>
<p>DONORS (NON-VET)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>S</td>
<td><blockquote>
<p>SPECIAL STUDIES (NON-VET)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>T</td>
<td><blockquote>
<p>OTHER NON-VETERANS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>U</td>
<td><blockquote>
<p>CHAMPVA--SPOUSE, CHILD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>V</td>
<td><blockquote>
<p>CHAMPUS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>W</td>
<td><blockquote>
<p>CZECHOSLOVAKIA/POLAND SVC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>X</td>
<td><blockquote>
<p>PERSIAN GULF WAR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Y</td>
<td><blockquote>
<p>CAV/NPS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Z</td>
<td><blockquote>
<p>MERCHANT MARINE</p>
</blockquote></td>
</tr>
</tbody>
</table>

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

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Value</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td><blockquote>
<p>HISPANIC, WHITE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>HISPANIC, BLACK</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>AMERICAN INDIAN OR ALASKA NATIVE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4</td>
<td><blockquote>
<p>BLACK, NOT OF HISPANIC ORIGIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>ASIAN OR PACIFIC ISLANDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>6</td>
<td><blockquote>
<p>WHITE NOT OF HISPANIC ORIGIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>7</td>
<td><blockquote>
<p>UNKNOWN</p>
</blockquote></td>
</tr>
</tbody>
</table>

Table 0001 - Sex

|           |                 |
|-----------|-----------------|
| Value | Description |
| F         | FEMALE          |
| M         | MALE            |
| O         | OTHER           |

Table 0078 - Abnormal flags

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Value</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>L</td>
<td><blockquote>
<p>Below low normal</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>H</td>
<td><blockquote>
<p>Above high normal</p>
</blockquote></td>
</tr>
<tr class="even">
<td>LL</td>
<td><blockquote>
<p>Below lower panic limits</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HH</td>
<td><blockquote>
<p>Above upper panic limits</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>For microbiology sensitivities only</strong></td>
<td></td>
</tr>
<tr class="odd">
<td>S</td>
<td><blockquote>
<p>Sensitive</p>
</blockquote></td>
</tr>
<tr class="even">
<td>R</td>
<td><blockquote>
<p>Resistant</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>I</td>
<td><blockquote>
<p>Intermediate</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MS</td>
<td><blockquote>
<p>Moderately sensitive</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VS</td>
<td><blockquote>
<p>Very sensitive</p>
</blockquote></td>
</tr>
</tbody>
</table>

######### APPENDIX - A

EPI USER GUIDE

# EPI User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPI User Guide provides all the necessary information, instructions, illustrations, and examples required for the EPI coordinators, Laboratory personnel, and other users to implement and maintain the Laboratory Search/Extract software. This information must be adhered to as recommended to assure a successful implementation and utilization of the software.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VAHQ Infectious Disease Program Office Emerging Pathogens Initiative is to identify new antibiotic-resistant, otherwise problematic pathogens. Using this objective information, plans may be formulated on a national level for intervention strategies and resource needs. Results of aggregate data may also be shared with appropriate public health authorities for planning on the national level for the non-VA and private health care sectors. The V*IST*A Laboratory Search/Extract software tracks Emerging Pathogens for DVA and the national level without the necessity for additional site data entry.

## EPI Objective:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Emerging Pathogens (as defined by VAHQ) act as triggers for data acquisition for the V*IST*A Laboratory Search/Extract software. The software then retrieves relevant, predetermined, and patient-specific data for transmission to the AITC database repository. Once at that location, the data are analyzed using a SAS based statistical software. VAHQ Reports may then be generated for appropriate use and distribution at the national level.

- Identify Emerging Pathogens
- Extract specific data associated with the Emerging Pathogen
- Transmit data to AITC
- Create national Statistical Analysis System (SAS) data sets for Infectious Diseases Program Office access
- Intermittent periodic review must be done as determined by the sites. The Verification Report is not used to determine Laboratory or <span id="p421_53" class="anchor"></span>ICD collected data totals or validation (i.e., X numbers of cases of positive tests for Hepatitis C or X positive culture results for Streptococcus, Group A).

## EPI Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EPI HL7 formatted Mail Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A Laboratory Search/Extract software automatically processes the EPI data on the 15<sup>th</sup> of each month producing HL7 formatted mail messages. A Verification Report mail message is then produced (i.e., in a human readable format) for each HL7 mail message. The EPI HL7 formatted mail messages must be manually forwarded on the 15<sup>th</sup> of each month to the AITC database via the Q-EPI.XXX.XX.XXX domain. Use the VA MailMan software to manually forward the EPI data to XXX@ Q-EPI.XXX.XX.XXX domain.

### EPI Verification Report Mail Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPI Verification Report mail messages are sent to the EPI-REPORT mail group on the 15<sup>th</sup> of each month. The members of the EPI-REPORT mail group should review the EPI Verification Report and make data corrections (e.g., social security number, date of birth, period of service, etc.) as deemed necessary. The software automatically processes the EPI data corrections on the 15<sup>th</sup> of each month. Note: The EPI Verification Report may be generated as often as needed using the new Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option.

### EPI Confirmation Mail Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPI Confirmation mail messages are sent to the sending facility EPI-REPORT mail group after the EPI HL7 mail messages has been received by the AITC database.

### EPI Processing Report Mail Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPI Processing Report mail messages are sent to the sending facility EPI-REPORT mail group at the end of the AITC processing cycle (i.e., the 25<sup>th</sup> of each month). The EPI Processing Report mail messages confirms that the EPI data has been processed and lists any errors and/or warning codes requiring corrections.

## Austin Automation Center Database Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Austin Information Technology Center (AITC) created two file structures, both in Statistical Analysis System (SAS) file format. These two file structures are used primarily as a source of data for the Infectious Diseases Program Office. The data is available to the Infectious Diseases Program Office to be manipulated and used for analysis and reporting.

The two file structures are referred to as the “Numerators” and “Denominators” because of their planned utilization.

### Numerator file:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Numerator file contains an accumulation of data sent by all DVA medical centers. It contains twelve individual months’ worth of data and is updated monthly. Each month the oldest month data is removed from the Numerator file and the latest month’s data is added.

Upon receipt of the DVA medical centers monthly input, AITC transmits an acknowledgment message back to the sending DVA medical centers. The acknowledgment message identifies any “problem transmissions”. The “problem transmissions” records any discrepancies in the field format or the actual field value. AITC identifies the data as invalid records or just warning the DVA medical center that the record has some discrepancies. However, the data is not being rejected. Both the “problem transmissions” and the “accepted records” are documented on a Processing Report that is transmitted from the AITC to the DVA medical centers. The “Processing Report” itemizes all transmissions received by AITC, document the records status as either being accepted or rejected (with the reason code identified), and a warning stating that something is unusual about the value of one or more fields (with the warning reason code identified). An example of the “Tables of Reject and Warning codes” are located in the Appendix - B section of this guide.

The Numerator file information is specific to unique patients with a VAHQ designated Emerging Pathogen. The Emerging Pathogens are flagged through the V*IST*A software process. The Numerator file data are collected and transmitted to AITC monthly by the DVA facilities medical centers.

### Denominator file:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Denominator file provides the Infectious Diseases Program Office, data elements for each DVA medical center. The source of these data elements is the corporate medical database residing in AITC. The individual files that these data elements are extracted from are the National Patient Care (NPC), Inpatient Treatment File (PTF),

Automated Management Information System (AMIS), and Cost Distribution Report (CDR) systems.

The data elements are:

- Unique SSN served (inpatient and outpatient together)
- Total \# of discharges
- Total unique SSN discharges
- Inpatient hospital days
- Inpatient ICU days
- Unique SSN encounters for both inpatient and outpatient

A “running 12 month” accumulation is required (i.e., there will always be one year’s worth of monthly counts) with the oldest month dropped off each cycle and a new one added.

> **NOTE:** The need to track individual station data and to consolidate by parent station has not been specified. At this time we are only gathering by individual station number.

## Lab Search/Extract Protocol Edit \[LREPI PROTOCOL EDIT\] option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Lab Search/Extract Protocol Edit \[LREPI PROTOCOL EDIT\] option is located on the Lab Search/Extract Primary Menu \[LREPI SEARCH EXTRACT MENU\]. This new option is used for editing the EPI protocol.

Example: EPI Protocol Parameters Setup Definition

Protocol Parameters Setup Definition

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PROTOCOL: LREPI

Title: Emerging Pathogens Initiative (EPI) Message Size: 32000

Report Mail Group: EPI-REPORT

Send Alert: YES

Send Alert To

DOE,Jane

## EPI Descriptions and Input Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the 14 Emerging Pathogens descriptions and input examples that the V*IST*A Laboratory Search/Extract software is tracking. The following EPI descriptions must be reviewed for compliance (as specified by the VAHQ Infectious Disease Program Office) <u>before</u> defining the Lab Search/Extract Parameters Setup.

*CandidaLegionellaClostridiumdifficile* Leishmanaisis

Creutzfeldt-Jakob Disease Malaria

*Cryptosporidium* Pen- Res Pneumococcus

Dengue *Streptococcus-*Group A

*E. coli* O157:H7 Tuberculosis

*Hepatitis C Antibody Pos Vanc-Res Enterococcus*NOTE: It is highly recommended that the following person(s) <u>jointly</u> participate in the review process for the 14 EPI descriptions:

Laboratory Information Manager (LIM)

Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) staff (or person at the site with similar function)

Representative from the Microbiology section for the Emerging Pathogens Initiative (i.e., director, supervisor, or technologist)

The 14 Emerging Pathogens parameter descriptions will require an ongoing review process (as specified by the VAHQ Infectious Disease Program Office). The person(s) participating in the ongoing review process is responsible for ensuring the following requirements are kept current:

Periodic reviews of the <span id="p421_58" class="anchor"></span>ICD codes

Periodic reviews of the Lab Search/Extract Parameter Setup \[LREPI PARAMETER SETUP\] for the EPI

Annual review of the 14 Emerging Pathogens descriptions (as specified by the VAHQ Infectious Disease Program Office)

## Laboratory Search/Extract Parameters Input Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following examples displays how to use the Laboratory Search/Extract Parameters Input Screen for defining the emerging pathogens parameters. Some of the Input Screen examples show <u>partially</u> pre-populated fields. The ETIOLOGY FIELD file (#61.2) site specific data is used to <u>partially</u> pre-populate the fields in the LAB SEARCH/EXTRACT file (#69.5). However, further data entries are required for site specific data. Additional data entries can be added or deleted to meet your site-specific needs.

> **NOTE:** The Lab Search/Extract Primary \[LREPI SEARCH EXTRACT MENU\] Menu options are using VA FileMan screens displays, referred to as ScreenMan. For detailed instructions on how to use the screens please review the VA FileMan V. 21.0 User Manual, Section 6 ScreenMan.

> **NOTE:** There are a number of different ways that sites have chosen to enter results into the V*IST*A database. As long as the results are in a retrievable format (straight from the V*IST*A database without additional manual input needed), how it is entered is not of significance to the Emerging Pathogen Initiative. However, two preferred methods make it easy to capture the data. Please reference the Helpful Hints section of this guide for the two methods.

> **NOTE:** Please be consistent with site specific data spelling or alternate spelling to assure accurate data capture.

### Candida (Reference \#8)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Fungal infections are rising in significance especially in severely ill patients. The same is true for bloodstream infections acquired in the hospital, especially those associated with intravenous lines. Fungal bloodstream infections are increasing in prevalence.

As a marker of bloodstream infections, the fungus *Candida* (and *Torulopsis*) has been chosen as an initial indicator organism. This organism may not be a prevalent or significant entity at your site, however, its presence is more likely to be indicative of serious or true infection than other organisms. The fungus *Candida* (and *Torulopsis)* may commonly be isolated from the blood in association with IV lines. Additionally, this yeast is more likely to be associated with nosocomial acquisition than other organisms (i.e., *Staphylococcus aureus* and coagulase negative *Staphylococcus)*, which can cause a number of community acquired syndromes not at all related to IV lines.

All episodes of *Candida* (*Torulopsis,* yeast) isolation from blood or a blood source (central line, IV catheter tip, etc.) are being tracked. The V*IST*A Laboratory Search/Extract software has provided a partial pre-populated list of (etiologies/organisms) that fit the description for *Candida* (*Torulopsis,* yeast) to choose. These (etiologies/organisms) should be used, in addition to any site specific (etiologies/organisms) which may also fit the description.

  
Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_Candida" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: Candida \<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: Candida ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

\<RET\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: CANDIDA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes

Examples:CANDIDA

CANDIDA GUILLIERMONDII

CANDIDA KRUSEI

CANDIDA PARAPSILOSIS

CANDIDA PSEUDOTROPICALIS

CANDIDA SKIN TEST ANTIGEN

CANDIDA STELLATOIDEA

CANDIDA TROPICALIS

CANDIDA, NOS

\<RET\>Note: During the post Init, the ETIOLOGY FIELD file (#61.2) was searched to pre-populate the Etiology field (#3) in the EMERGING PATHOGENS file (#69.5). Listed above are examples of etiology entries which may have been populated from your site’s file. Additional etiologies may be added or deleted at the <u>Selected Etiology</u> prompt to meet your site specific needs.

> **NOTE:** If spelling differences occur within your ETIOLOGY FIELD file (#61.2), be consistent with your local file and spell the results here, as it is spelled in your file (even if it is spelled differently in the example). We are concerned more importantly with data <u>recovery</u>.

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: Candida ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

Blood\<RET\>\<RET\>Bloodstream\<RET\>Catheter Tip\<RET\>Note: These are only suggestions. Please add accordingly to your site definition.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: Candida ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FIRST ENCOUNTER:\<RET\> Follow PTF:YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Select SEX:\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME:Candida ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

### Clostridium difficile (Reference \#4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Disease associated with the presence of *Clostridium difficile* enterotoxin A can cause significant morbidity, as well as mortality. It is of importance, as its predominant acquisition seems to occur nosocomially. Presence of Clostridial toxin (either enterotoxin A or cytotoxin L) by assay (whether it be EIA, latex agglutination, cytotoxicity of cell culture <u>+</u> neutralization, or culture of organism with subsequent colony testing) is the best indicator that an inflammatory diarrheal disease is due to presence of *Clostridium difficile*.

Laboratory Services are quite varied as to how they identify the presence of *Clostridium difficile*. Some labs are set up to identify *C. difficile* as the final microbiological (bacterial) etiology of a culture, even if a culture method was not used. Other labs use a final etiology of “see comment” and then enter the results in a free text format. Still others enter the text under a hematology or chemistry format where a reference range and “positive” and “negative” result values can be entered. Wherever the facility lab places the results which are used to demonstrate the presence of toxin-producing *C. difficile*, we need to be able to track them (that means it must occur as a retrievable “positive” or “negative” result, or as a “bacterial etiology”). Results in a “Comments” or “Free-text” section are not acceptable.

There are a number of different ways that sites have chosen to enter *Clostridium difficile* toxin assay results into the V*IST*A database. As long as the toxin assay results are in a retrievable format (straight from the V*IST*A database without additional manual input needed), how it is entered is not of significance to the Emerging Pathogen Initiative. However, there are two preferred methods that make it easy to capture the data. Please reference the Appendix - B section of this guide for the two methods.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_Clostr" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: CLOSTRIDIUM DIFFICILE \<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

Clostridium\<RET\> difficile toxin Contains\<RET\>Pos\<RET\>Note: This example is only a suggestion. Please add accordingly to your site definition.

ICD Coding System \[ICD-9 or ICD-10\]? (9/10): 9

ICD Code Cd Set ICD Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes

Clostridium difficile toxin positive\<RET\>Note: This is only a suggestion. Please add accordingly to your site definition.

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include \<RET\> Exclude \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter:\<RET\> Follow PTF: YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Selected SEX:\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: CLOSTRIDIUM DIFFICILE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

### Creutzfeldt-Jakob Disease (CJD) (Reference \#13)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Creutzfeldt-Jakob Disease* (CJD*)* disease is a rare illness associated with prions. The DVA has chosen to follow this entity because of historic problems with certain blood products used in the private and public health care sectors. The data will be one of a number of ways used to identify changes in trends of incidence of this illness. This task is remarkably complex because of the long incubation period of CJD. There are no specific tests for diagnosis other than central nervous system histology combined with clinical presentation. As such, this entity is followed through ICD coding.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_Creut" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: CREUTZFELDT-JAKOB DISEASE \<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME:CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

\<RET\>

<span id="p75" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

046.1 ICD-9 JAKOB-CREUTZFELDT DIS

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes\<RET\>

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<RET\> \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter: \<RET\> Follow PTF: YES\<RET\>

BEFORE DATE OF BIRTH: \<RET\> AFTER DATE OF BIRTH: \<RET\>

Select SEX: \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: CREUTZFELDT-JAKOB DISEASE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

### Cryptosporidium (Reference \#9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The parasite *Cryptosporidium parvum* is a cause of water-borne diarrheal disease. It has gained recent prominence after evaluation of the outbreak in the greater Milwaukee area in 1993 which is estimated to have affected \<400,000 persons. In addition to affecting HIV-infected persons and young children, information exists which demonstrates that the chronically ill, elderly are also a higher risk group than the general population. Microbiology laboratory data (parasitology for most laboratories) as well as ICD coding is used to track this disease, both are narrowly defined parameters.

> **NOTE:** Microsporidiosis is a similar disease, however, the EPI do not currently wish to follow this disease process. Microsporidian etiologies should not be entered.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_Cryp" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: CRYPTOSPORIDIUM \<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: CRYPTOSPORIDIUM ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

\<RET\>

<span id="CodeSysUpdate2" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

007.8 ICD-9 PROTOZOAL INTEST DIS N

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: CRYPTOSPORIDIUM ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes

Cryptosporidium\<RET\>Note: If Cryptosporidium is reported under parasitology, add Cryptosporidium species at the Etiology prompt.

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: CRYPTOSPORIDIUM ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<RET\> \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: CRYPTOSPORIDIUM ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter:\<RET\> Follow PTF: YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Select SEX:\<RET\>

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: CRYPTOSPORIDIUM ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date: Protocol: LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

### Dengue (Reference \#12)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The mosquito-borne disease of Dengue Hemorrhagic Fever is a rare but re-emerging infection, especially in the Caribbean. The VA has seen cases of Dengue Hemorrhagic Fever over the last several years. Most of these cases have been in Dengue endemic areas served by the VA. However, as our society becomes more mobile, and the area of Dengue endemnity expands, more cases are likely to occur. Because microbiologic culture is not routinely done and serology can be difficult to track, initially ICD coded diagnoses is used to track this entity.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_Dengue" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: DENGUE \<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: DENGUE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

\<RET\>

<span id="ICDCodeAdd2" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

061\. ICD-9 DENGUE

065.4 ICD-9 MOSQUITO-BORNE HEM FEVER

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: DENGUE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Etiology Selected Snomed Codes

\<RET\>

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: DENGUE ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<RET\> \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: DENGUE ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter: \<RET\> Follow PTF: YES \<RET

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Select SEX:\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: DENGUE ACTIVE YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

### E. coli O157:H7 (Reference \#10)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Escherichia coli* serotype O157 (*E. coli* O157) has gained prominence as a food-borne illness with potentially life threatening complications coming from the associated Hemolytic Uremic Syndrome. Not all sites routinely culture for the presence of *E. coli* O157 in stool specimens submitted for culture. In addition, *E. coli* O157 is not a microbiologic (bacterial) etiology pre-existing in the most recent - national microbiology lab package. In order to nationally track cultures positive for this organism, each site will need to make an etiology specific for *E-coli* O157 (e.g. *Escherichia coli* O157, *E. coli* O157, *E. coli* serotype O157, etc.). Some sites have already done this and will not need to generate a new entry.

> **NOTE:** Entering *Escherichia coli* or *E. coli* from the bacterial etiology and then entering “serotype O157” or “O157”, under the “Comments” or “Free Text” section is not acceptable, as it will not allow the data to be retrieved nationally.

All subsequent positive cultures for this organism must then be entered under the new etiology.

Other serotypes of *E. coli* will also cause disease, but we will not currently track these as O157 causes by far, the majority of cases of interest for the national database.

The EPI criteria is dependent on your site. If your site already has an etiology that will select positive cultures for *E. coli* O157, then enter that etiology. However, if your site had to enter a new etiology to accommodate the EPI criteria, be sure to enter this new etiology here.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_E_Coli" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: E. COLI 0157:H7 \<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: E. COLI 0157:H7 ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

\<RET\>

<span id="ICDCodeAdd3" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: E. COLI 0157:H7 ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

Example: Escherichia coli O157\<RET\>Note: Entering *Escherichia coli* or *E. coli* from the bacterial etiology and then entering “serotype O157” or “O157”, under the Comments section or in

free text is not acceptable as it will not allow the data to be retrieved nationally).

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: E. COLI 0157:H7 ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<RET\> \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: E. COLI 0157:H7 ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter:\<RET\> Follow PTF:YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Select SEX:\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: E. COLI 0157:H7 ACTIVE YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

### Hepatitis C Antibody Positive (Reference \#2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hepatitis C is much more prevalent than originally thought at least in certain key patient sub-populations. As new and more sensitive assays come into use, we seem to find more evidence of this pathogen. We are looking for evidence of exposure to Hepatitis C in patients as demonstrated by Hepatitis C antibody positivity. The need for confirmatory testing or demonstration of active disease is not currently necessary in gathering data for this program. Different facilities may use different assays for this test. What we are looking for is evidence of presence of antibody to Hepatitis C, whether it be recorded as “weakly positive”, “strongly positive”, “positive”, or “present”. If other phrases are used to describe a test result, one should be able to differentiate the results upon entry into the program. As an example, the words, “present” “and “not present” would not allow retrieval of only positive cases as both phrases contain the word, “present”.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_Hep" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: HEPATITIS C ANTIBODY POS \<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: HEPATITIS C ANTIBODY POS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

HEPATITIS C ANTIBODY\<RET\> Contains\<RET\>Pos\<RET\>Note: Enter the appropriate test for your site, and how the results are reported.

<span id="ICDCodeAdd4" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: HEPATITIS C ANTIBODY POS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes

\<RET\>

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: HEPATITIS C ANTIBODY POS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<RET\> \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: HEPATITIS C ANTIBODY POS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter:\<RET\> Follow PTF:YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Select SEX:\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: HEPATITIS C ANTIBODY POS ACTIVE YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

Save changes before leaving form (Y/N)?Y\<RET\>

### Legionella (Reference \#7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since the American Legion Convention in Philadelphia in the 1970’s, Legionnaires’ Disease has been an illness of keen interest to the DVA. Because diagnosis is complex, we have chosen to review for presence of *Legionella* in culture and in ICD DIAGNOSIS file (#80). We will not look at *Legionella* direct fluorescent antibody positivity because of the potential high false positivity of this test. Likewise, serology is not easy to interpret or easily extracted from V*IST*A for our purposes and will not be included as a marker in this first iteration of the EPI program. Because it is not yet approved, the newer test of *Legionella* urinary antigen will not be used either. The Selected Etiology screen display has been partially pre-populated.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_Legion" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: LEGIONELLA\<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: LEGIONELLA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

\<RET\>

<span id="ICDCodeAdd5" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

482.80 ICD-9 LEGIONNARIE’S DISEASE

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

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

\<RET\>Note: During the post Init, the ETIOLOGY FIELD file (#61.2) was searched to pre-populate the Etiology field (#3) in the EMERGING PATHOGENS file (#69.5). Listed above are examples of etiology entries which may have been populated from your site’s file. Additional etiologies may be added or deleted at the <u>Selected Etiology</u> prompt to meet your site-specific needs.

> **NOTE:** If spelling differences occur within your ETIOLOGY FIELD file (#61.2) be consistent with your local file and spell the results here, as it is spelled in your file (even if it is spelled differently in the example). We are concerned more importantly with data <u>recovery</u>.

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: LEGIONELLA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<RET\>\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: LEGIONELLA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter:\<RET\> Follow PTF: YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Select SEX:\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: E. LEGIONELLA ACTIVE YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

### Leishmaniasis (Reference \#14)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Leishmaniasis is a significant tropical disease that can cause serious complications. It is of interest to the Department of Veterans Affairs as Leishmania has caused illness among military personnel for many years. In addition, the Persian Gulf War occurred in an area of the world where the parasite is endemic. Because no simple, straightforward serology exists and no standard culture techniques exist, we have chosen to follow this entity through <span id="p421_87ICD" class="anchor"></span>ICD diagnosis codes.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_Leis" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: LEISHMANIASIS \<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: LEISHMANIASIS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

\<RET\>

<span id="ICD9toICDchange6" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):9\<RET\>

ICD Code Cd Set ICD Description

085.0 ICD-9 VISCERAL LEISHMANIASIS

085.1 ICD-9 CUTAN LEISHMANIAS URBAN

085.2 ICD-9 CUTAN LEISHMANIAS ASIAN

085.3 ICD-9 CUTAN LEISHMANIAS ETHIOP

085.4 ICD-9 CUTAN LEISHMANIAS AMER

085.5 ICD-9 MUCOCUTAN LEISHMANIASIS

085.9 ICD-9 LEISHMANIASIS NOS

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: LEISHMANIASIS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes

\<RET\>

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: LEISHMANIASIS ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<RET\> \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: LEISHMANIASIS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter:\<RET\> FOLLOW PTF:YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Select SEX:\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: E. LEISHMANIASIS ACTIVE YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

### Malaria (Reference \#11)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The plasmodial parasite is responsible for the blood-borne disease of malaria. Malaria can cause acute as well as chronic, relapsing disease. Occasionally, U.S. troops are deployed in malaria endemic areas. This placement could potentially put troops at risk for acquiring this disease. For the Emerging Pathogens Initiative program, we are interested in tracking patients with malaria, either acute or chronic, relapsing, and in either inpatient or outpatient status. No standardized serologic test allows for easy identification. Since not all sites consistently code and record malarial parasites seen histologically or on blood smears (not all of these interpretations are done through the Pathology and Laboratory Service), we have currently decided to track malaria based on ICD coding.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_Malaria" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: MALARIA \<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: MALARIA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

\<RET\>

<span id="ICDCodeAdd6" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

084.0 ICD-9 FALCIPARUM MALARIA

084.1 ICD-9 VIVAX MALARIA

084.2 ICD-9 QUARTAN MALARIA

084.3 ICD-9 OVALE MALARIA

084.4 ICD-9 MALARIA NEC

084.5 ICD-9 MIXED MALARIA

084.6 ICD-9 MALARIA NOS

084.7 ICD-9 INDUCED MALARIA

084.8 ICD-9 BLACKWATER FEVER

084.9 ICD-9 MALARIA COMPLICATED NEC

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: MALARIA ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes

\<RET\>

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: MALARIA ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<RET\> \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: MALARIA ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter:\<RET\> FOLLOW PTF:YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Selected SEX:\<RET\>

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: MALARIA ACTIVE YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

Save changes before leaving form (Y/N)?Y\<RET\>

### Penicillin- Resistant Pneumococcus (Reference \#3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The emergence of antibiotic resistance in microbial agents is of great interest and concern for health care. Penicillin (PCN) was once the mainstay of therapy for *Streptococcuspneumoniae* infections but resistance to this agent is becoming more prominent. Different therapeutic strategies need to be developed once the prevalence of PCN-resistant *S. pneumoniae* reaches a critical threshold in a community. In order to monitor this, we are looking for the presence of any resistance in the pneumococci (either “moderate/intermediate” or “frank/high” level resistance). As such, any *S. pneumoniae* which is not fully susceptible to PCN on PCN susceptibility testing should be recorded.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_PEN" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: PEN-RES PNEUMOCOCCUS \<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: PEN-RES PNEUMOCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

\<RET\>

<span id="ICDCodeAdd7" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: \<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: PEN-RES PNEUMOCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes

> **NOTE:** You may enter a new ETIOLOGY, if you wish.

STREPTOCOCCUSPNEUMONIAE 12

Are you adding 'STREPTOCOCCUS PNEUMONIAE' as

a new ETIOLOGY (the 1ST for this EMERGING PATHOGENS)?Y\<RET\>

Antimicrobial Susceptibility NLT Code NLT Description

Penicillin\<RET\>

Are you adding ' Penicillin ' as

a new Antimicrobial Susceptibility (the 1ST for this EMERGING PATHOGENS)?Y \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: \<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: PEN-RES PNEUMOCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<RET\> \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: PEN-RES PNEUMOCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter:\<RET\> FOLLOW PTF:YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Selected SEX:\<RET\>

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: PEN-RES PNEUMOCOCCUS ACTIVE YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

### Streptococcus-Group A (Reference \#6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Streptococcus-*Group A can be associated with or cause significant disease such as severe fasciitis and streptococcal toxic shock syndrome. We are especially interested to find out how much severe/deep seated disease the VA is experiencing, but other disease entities are of interest also. To this end, we are looking for all episodes of culture positivity for *Streptococcus-*Group A, regardless of site and regardless of inpatient or outpatient status of the person from whom the specimen is obtained. We are aware that some sites may use rapid screenings for *Streptococcus-*Group A, especially from pharyngeal sources. These rapid screens may be difficult to capture, so we are not asking for them on this first iteration of the EPI program.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_Strep" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: STREPTOCOCCUS-GROUP A \<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: STREPTOCOCCUS-GROUP A ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

\<RET\>

<span id="ICDCodeAdd8" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: STREPTOCOCCUS-GROUP A ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes

STREPTOCOCCUS-GROUP A\<RET\>

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: STREPTOCOCCUS-GROUP A ACTIVE: YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<RET\>\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: STREPTOCOCCUS-GROUP A ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter:\<RET\> FOLLOW PTF:YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Select SEX:\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: STREPTOCOCCUS-GROUP A ACTIVE YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

### Tuberculosis (Reference \#5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Mycobacterium tuberculosis* infection is an important public health concern. Recent increases in incidence of disease, and occurrence of multiply-drug resistant strains in outbreak situations along with the increased susceptibility of HIV-infected persons for this disease has generated renewed interest in this entity. Since the national data show that 80-85% of all reported active tuberculosis cases are culture positive (with acid fast bacilli smear-only positive cases increasing the reporting by 2-5% more) we have decided to use culture positivity for *Mycobacterium tuberculosis* to track tuberculosis infections in the current iteration of the EPI software package. Information regarding susceptibility will be tracked as well. For the national EPI program, there will be no need to enter specific antimycobacterial agents to be tracked; it will be done automatically. ICD coding is complex and confusing for many cases of tuberculosis and therefore will not be used.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_Tuber" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: TUBERCULOSIS\<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: TUBERCULOSIS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

\<RET\>

<span id="ICDCodeAdd9" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME:TUBERCULOSIS ACTIVE:YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes

Mycobacterium tuberculosis\<RET\>

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: TUBERCULOSIS ACTIVE:YES \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<RET\> \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: TUBERCULOSIS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter:\<RET\> FOLLOW PTF:YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Select SEX:\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: TUBERCULOSIS ACTIVE YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

### Vancomycin-Resistant Enterococcus (VRE) (Reference \#1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vancomycin-Resistant Enterococcus (VRE) is a pathogen of increasing importance. Not only can it cause significant disease, but also it can be spread within facilities. It is important to capture all positive cultures for VRE (not just disease). As such, all positive cultures for VRE will be reported.

> **NOTE:** This includes cultures positive for prevalence and surveillance review, including specimens of stool and rectal swabs.

Vancomycin-resistant *Enterococcus faecalis* and *E. faecium* are most common, but we wish to look at all vancomycin resistant enterococci whether speciated or not. Therefore, it is important to be sure to list all the places in the Micro Lab package where *Enterococcus* are found, either as *Enterococcus*, *E. (sp.),* Group D-*Streptococcus*, *E. faecalis*, *E. faecium*, *E. durans*, *E. gallinarum*, *E. casseliflavus*, etc.

> **NOTE:** Only a partial pre-populated Etiology list is shown in the screen display example at the <u>Selected Etiology</u> prompt. Please be sure to review the entire Etiology list. If you have other etiology results at your site, they can be added to this Etiology list. Again, if alternate spellings are present in your site’s ETIOLOGY FIELD file (#61.2), be certain those spellings assure capture of all data points possible.

Example:

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_VAN" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: VANC-RES ENTEROCOCCUS \<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: VANC-RES ENTEROCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

\<RET\>

ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: VANC-RES ENTEROCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes

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

\<RET\>Note: During the post Init, the ETIOLOGY FIELD file (#61.2) was searched to pre-populate the Etiology field (#3) in the EMERGING PATHOGENS file (#69.5). Listed above are examples of etiology entries which may have been populated from your site’s file. Additional etiologies may be added or deleted at the <u>Selected Etiology</u> prompt to meet your site specific needs.

> **NOTE:** If spelling differences occur within your ETIOLOGY FIELD file (#61.2) be consistent with your local file and spell the results here, as it is spelled in your file (even if it is spelled differently in the example). We are concerned more importantly with data <u>recovery</u>.

Antimicrobial Susceptibility NLT Code NLT Description

VANCOMYCIN\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: VANC-RES ENTEROCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\<RET\> \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: VANC-RES ENTEROCOCCUS ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

First Encounter:\<RET\> FOLLOW PTF:YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Select SEX:\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: VANC-RES ENTEROCOCCUS ACTIVE YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LREPI\<RET\>

Run Cycle:MONTHLY\<RET\> Lag Days:15\<RET\>

General Description:\<TAB\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

## Conclusion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have finished entering the information as directed by the national Infectious Diseases Program Office, these fields should not again be changed except for the following conditions:

1\. As requested nationally via the Veterans Affairs Headquarters (VAHQ) Infectious Disease Program Office to update, modify, add, or delete data from the existing files used by the Laboratory Search/Extract software or an addition of a new entity to be tracked.

2\. The yearly review must ensure that the entry is acceptable and to update the EPI files with any changes in etiology, lab tests or results parameters that may have occurred locally at the site during the previous year.

Annually the EPI national program materials should be reviewed by the VAMCs and updated. It is suggested that this review occur in February of each year. If no changes have occurred in lab practices, etiologies, sites, or results parameters leave the information as is until the next review period. If changes <u>did</u> occur, then enter them as appropriate in order to capture the data requested for each EPI national entity (disease/organism) to be tracked.

As entities (diseases/organisms) are no longer to be tracked nationally (“dropped from the list”), or a new entity is to be tracked (“added to the list”), revision will be forwarded to the sites to assist in updating your site files.

## EPI Helpful Hints:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Clostridium difficile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two preferred methods that will make it easy to capture data for Clostridium difficile criteria (i.e., as well as several other methods which sites may already employ). Note: As long as the designated parameter results being tracked are in a retrievable field (i.e., not a “Free Text” or “Comment” field) the method the site chooses is an individual decision.

Preferred Method: The first preferred method is to have the site define an etiology of “Clostridium difficile toxin positive”. This allows a topography specimen of accession area “feces/stool” to be accessioned through the Microbiology accession area. Then, if the stool specimen were indeed positive for *Clostridium difficile* toxin, by any of the known methods of testing, the etiology would be “Clostridium difficile toxin positive.” To accomplish this method would require sites to enter three new local etiologies:

- Clostridium difficile toxin positive
- Clostridium difficile toxin negative
- Clostridium difficile toxin indeterminant

These would be different from a culture isolate being positive for *Clostridium difficile,* in that they actually are etiologies/results based on toxin testing. This leaves the etiology of *Clostridium difficile* for actual culture positive specimens for the organism *Clostridium difficile*. The Lab Search/Extract Parameter Setup, the site parameter by which the software will capture a patient diagnosed with proven *Clostridium difficile*-associated colitis, will be by placing “Clostridium difficile toxin positive” etiology into the selected etiology entry screen. This has the advantage of being more consistent with other data entry practices in the Microbiology sections of most laboratories.

Preferred Method: The second preferred method is having the data in retrievable form would be to enter/accession the specimen for *Clostridium difficile* toxin assay under the chemistry/serology format (regardless of where the test is physically done) with the results being a choice of “positive”, “negative”, or “indeterminate”. This would allow one to enter *“Clostridium difficile* toxin” assay as the test for the EPI software to search in the chemistry/serology format. The result would be retrievable for EPI under a chemistry/serology lab test of “*Clostridium difficile* toxin” with the indicator “contains” and the value of “pos”, as noted in the sample page. If your site does not routinely do *Clostridium difficile* toxin assay testing this way, a different method of accessioning the specimen to get it in chemistry/serology format would be needed.

However, the Chemistry/Serology format would give additional flexibility in placing interpretational guidelines for the test results in the “Comments” field. For the EPI, “positive” or “negative” results cannot be located in a “Free Text” or “Comments” field as these are not retrievable.

Some VAMCs accession the stool specimen for the *Clostridium difficile* toxin assay under the Microbiology format. An etiology is not given under the final culture result, but written into free text or comments section stating the *Clostridium difficile* toxin assay test result. This is not in a retrievable format and therefore not acceptable for the EPI creteria.

Some VAMCs still use cytotoxin assays of cell culture, which are again entered in a “Free Text” or “Comment” field. This again is not acceptable unless it is accessioned and recorded under the chemistry/serology format as a straightforward lab test result of “positive” or “negative” or “indeterminate”.

Some VAMCs choose to report *Clostridium difficile* toxin assay positivity under the Microbiology application. As an etiology/culture result of *Clostridium difficile* (even though culture, was not actually done) this is not a true measure of what is actually being tested (as most sites do not culture the organism but just run the toxin assay test). However, if your site uses this means to represent *Clostridium difficile* toxin assay positivity and there are no exceptions (such as the site reporting an actual positive culture of (*Clostridium difficile* which is toxin assay negative), then this would be acceptable though less desirable for EPI purposes.

### Validating EPI Data Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the Lab Search/Extract Parameter is setup, the Laboratory Search/Extract software automatically generates an Verification Report message around the 15<sup>th</sup> of each month. The Emerging Pathogen Verification Report should be used to compare the EPI data capture to site-specific data capture. This comparison also helps determine if the Lab Search/Extract Parameter for the EPI criteria is accurately defined. It is recommended that the Lab Search/Extract Manual Run \[LREPI (EPI) MANUAL RUN\] option be run to evaluate 1-3 months of data (i.e., as determined by the sites).

The Microbiology Laboratory staff, Laboratory Manager, TQI/QI/QA, or other person (i.e., as determined by the sites) may already have data of isolated “organisms of interest”. Several of the nationally defined emerging pathogens may well corresponds with the existing data. Therefore, a quick comparison can be done using the Emerging Pathogens Verification Report message. This comparison also ensures that the Laboratory Search/Extract software is appropriately capturing the EPI cases and numbers

For tests such as Hepatitis C, most Laboratory Managers should be able to generate reports (with patient names) that includes “positive” tests results to use for comparison. Additionally, the Health Information Management Section at each site should be able to generate a report of <span id="p421_109" class="anchor"></span>ICD-9 and ICD-10 Diagnoses by date. This ICD Diagnoses by date Report helps determine if the 14 VAHQ defined Emerging Pathogens data captures concurs with the EPI criterion (i.e., Cryptosporidium-007.8, Legionnaire’s disease--482.80, malaria--084, 084.0, 084.1, 084.2, 084.3, 084.4, 084.5, 084.6, 085.7, 084.8, 084.9, dengue-061, 065.4, Creutzfeldt-Jakob--046.1, and Leishmaniasis--085, 085.0, 085.1, 085.2, 085.3, 085.4, 085.5, 085.9).

Be aware that a number of these emerging pathogens do not occur at a high frequency. Sites with previously known cases of emerging pathogens, such as TB, should run the Lab Search/Extract Manual Run \[LREPI (EPI) MANUAL RUN\] option for the entire month to verify that the TB culture was isolated and to see if it is captured. Additionally, “test patients” known to have these lab results can also be run.

The purpose of this validation is not to require extra paperwork for QI monitors and long term document files. The validation should be done at the initial implementation of the Laboratory Search/Extract software to ensure accurate data capture. Thereafter, a review should be done once every 4-6 months to ensure that Lab Search/Extract Parameter Setup \[LREPI (EPI) PARAMETER UPDATE\] option entries for the EPI criteria remains accurate. Parameter updates may be required if a new lab test/result is to be implemented for one of the Emerging Pathogens Initiative.

### Emerging Pathogens Verification Report Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of the Emerging Pathogens Verification Report mail message. The EPI software automatically transmits the EPI data to the AITC on the 15<sup>th</sup> of each month. The AITC processes the on the 25<sup>th</sup> of each month

Example:

Emerging Pathogens Verification Report \[#60004\] Page 1

----------------------------------------------------------------------------

REPORTING DATE FROM 12-01-1996 TO 12-31-1996 Message Seq \# 1 Auto

JOHN DOEDOE XXX-XX-XXXX 07-07-1913 M WORLD WAR II 45205

Outpatient Accession Date 12-11-1996@1025

\*\*\*\*\*\*\*\*\* STREPTOCOCCUS GROUP A \*\*\*\*\*\*\*\*\*

12-11-1996@1025 BACT 96 10383 MICRO CULTURE LEG

1 12-13-1996 STREPTOCOCCUS BETA HEMOLYTIC, GROUP A

2 12-13-1996 STAPHYLOCOCCUS (COAGULASE NEGATIVE)

ORG \# 1 12-11-1996@1025 ANTIBIOTIC MIC LEG

ORG \# 2 12-11-1996@1025 ANTIBIOTIC MIC LEG

JOHN DOEDOE XXX-XX-XXXX 01-08-1923 M WORLD WAR II 45239

Inpatient Admission Date 12-19-1996@1125

\*\*\*\*\*\*\*\*\*4 CLOSTRIDIUM DIFFICILE \*\*\*\*\*\*\*\*\*

Can be verified using standard result reviews for “CH” subscripted tests (e.g., LRRSP, LRRP3, LRSORD, LRSORA, LRGEN)

12-25-1996@1415 MSER 96 418 CHEMISTRY TEST FECES

Clostridium Difficile Toxin 12-27-1996@1403 POSITIVE

JOHN DOE \###-##-#### 11-05-1910 M WORLD WAR II 45255

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

JOHN DOE \###-##-#### 02-23-1920 M PRE-KOREAN 45150

Inpatient Admission Date 11-18-1996@2213

\*\*\*\*\*\*\*\*\*8 CANDIDA \*\*\*\*\*\*\*\*\*

12-11-1996@0100 BLD 96 3914 MICRO CULTURE BLOOD

1 12-15-1996 CANDIDA ALBICANS

ORG \# 1 12-11-1996@0100 ANTIBIOTIC MIC BLOOD

JOHN DOE \###-##-#### 12-23-1949 M VIETNAM ERA 45206

Outpatient Accession Date 12-20-1996@1309

\*\*\*\*\*\*\*\*\*2 HEPATITIS C ANTIBODY POS \*\*\*\*\*\*\*\*\*

12-20-1996@1309 RIA 1220 68 CHEMISTRY TEST SERUM

Hepatitis C Ab 01-03-1997@1347 STRONG POSITIVE -

JOHN DOE \###-##-#### 07-06-1919 M WORLD WAR II 41074

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

### Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LREPI: This event driver protocol defines the associated parameters needed to build the HL7 Message used to send data to the AITC.

LREPI CLIENT: This subscriber protocol defines the parameter required by the HL7 application that determines where to send the HL7 formatted message containing the EPI data.

### Domain

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPI software Domain name is Q-EPI-MED.GOV. Sites must install Patch XM\*DBA\*103. See VA MailMan V. 7.1 manual for instruction on how to set up the domain after the patch has been installed.

### EPI Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPI software application has two mail groups. These mail groups are use too electronically transmit data (i.e., HL7 format messages) to the AITC and to receive messages from the AITC. Listed below are recommendations for membership and suggestions for managing the EPI mail groups.

### Office of the Director (00)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that the Office of the Director (00) at each VAMC initially designate the member(s) responsible for overseeing the two EPI mail groups.

The EPI mail group member(s) is responsible for transmitting the EPI data to the AITC.

The EPI-Report mail group member(s) will receive the Emerging Pathogens Verification Report Messages, Confirmation Messages and the Processing Report transmitted by the AITC. This individual(s) will also assist in the EPI data validation, data corrections, and re-transmitting the EPI data to the AITC.

#### <span class="smallcaps">  
</span>NOTE: It is highly recommended that a TQI/QI/QA staff, Laboratory Information Manager (LIM), Microbiology director or supervisor, Infection Control Practitioners, or Hospital Epidemiologist), or individual(s) with similar functions be a member(s) of the mail groups. This member(s) is responsible for making EPI data corrections due to the numerous files from which the data is obtained (e.g., PTF, PIMS, Health Information Management, Laboratory, etc.). Once the corrections are made, it is the responsibility of the EPI mail group member(s) to re-transmit the EPI data to the AITC. These members may also be of assistance with the verification and periodic validation processes.

### EPI Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following information explains the functionality of each mail group.

EPI:

This mail group is used for the transmission of EPI HL7 messages derived from the parameters defined in the LAB SEARCH/EXTRACT file (#69.5) to the AITC.

- Transmit EPI data from the VAMCs (i.e., in HL7 format as defined by the Laboratory Search/Extract software) to the AITC.

EPI-Report:

This mail group is used to deliver the Verification Report message (i.e., created in human readable formatted) which is used to review the data sent to the AITC.

Receives the EPI Verification Report that is generated at each VAMC around the 15<sup>th</sup> of each month The EPI Verification Report is automatically generated monthly from the HL7 formatted mail message (i.e., in a human readable format). The EPI Verification Report can be generated manually using the Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option and re-run whenever deemed necessary.

Receive the Confirmation Messages

Receive Processing Report from AITC. This report displays any errors that occurred and if a message is unacceptable for receiving by the AITC.

### Adding Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add the EPI mail groups to the HL7 APPLICATION PARAMETER file (#771) using VA FileMan V. 21.0:

Example:

Select OPTION: ENTER OR EDIT FILE ENTRIES \<RET\>

INPUT TO WHAT FILE: HL7 APPLICATION PARAMETER file (#771)\<RET\>

(7 entries)

EDIT WHICH FIELD: ALL// \[Enter Facility Name field\]\<RET\>

THEN EDIT FIELD:\<RET\>

Select HL7 APPLICATION PARAMETER NAME: EPI \<RET\> ACTIVE

FACILITY NAME: \[Enter your facility name or facility number\] \<RET\>

Select HL7 APPLICATION PARAMETER NAME: EPI-Report\<RET\> ACTIVE

FACILITY NAME: \[Enter your facility name or facility number\] \<RET\>

### Starting the Lower Level Protocol of the HL7 V. 1.6 Background Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example:

Select Systems Manager Menu Option:HL7 Main\<RET\> Menu

1 V1.5 OPTIONS ...

2 V1.6 OPTIONS ...

3 Activate/Inactivate Application

4 Print/Display Menu ...

5 Purge Message Text File Entries

Select HL7 Main Menu Option: 2\<RET\> V1.6 OPTIONS

1 Communications Server ...

2 Interface Workbench

3 Message Requeuer

Select V1.6 OPTIONS Option: 1\<RET\> Communications Server

1 Edit Communication Server parameters

2 Manage incoming & outgoing filers ...

3 Monitor incoming & outgoing filers

4 Start LLP

5 Stop LLP

6 Systems Link Monitor

7 Logical Link Queue Management

8.  Report

Select Communications Server Option: 4\<RET\> Start LLP

This option is used to launch the lower level protocol for the

Appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: EPI\<RET\>

The LLP was last shutdown on JAN 30, 1997 12:06:19.

Select one of the following:

F FOREGROUND

B BACKGROUND

Q QUIT

Method for running the receiver: B//\<RET\> ACKGROUND

Job was queued as 131225.

### EPI HL7 Format Mail Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPI data is transmitted via an HL7 format mail message to the AITC. The HL7 format mail message should to be transmitted to the AITC by the 15<sup>th</sup> of each month. Forward the HL7 format mail message to the <XXX@Q-EPI> domain.

Example:

Subj: HL7 Message FEB 10,1997@15:56:29 from Station XXX STATION XXX \[#63430\]

10 Feb 97 15:56 262 Lines

From: POSTMASTER (Sender: ANYBODY) in 'IN' basket. Page 1

----------------------------------------------------------------------------

MSH\|~^\\\|EPI-LAB\|\|EPI-LAB\|\|19970210155618\|\|ORU~R01\|483\|P\|2.2\|\|\|NE\|NE\|USA

NTE\|\|R~REPORTING DATE FROM 19960101 TO 19970131~1

PID\|1\|<span id="p421_115" class="anchor"></span>000-54-3435~4~M10\|17~8~M10\|\|DUCK~DONALD\|\|19840426\|M\|\|7\|~\|\|\|\|\|\|\|\|000543435

PV1\|1\|O\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|19960312123902

NTE\|1\|1~VANC-RES ENTEROCOCCUS

OBR\|1\|\|\|81121.0000~CHEMISTRY TEST~VANLT\|\|\|19960312123902\|\|\|\|\|\|\|\|SER\~~SERUM\|\|\|CH

0312 14

OBX\|1\|ST\|\~\~~183~CHOLESTEROL~VA60\|\|190\|mg/dL\|\$S(AGE\<50:135,1:120)-288\|\|\|\|\|\|\|1996

0328145221

Select MESSAGE Action: IGNORE (IN basket)// FORWARD\<RET\>

Send mail to: XXX@Q-EPI \<RET\>.XXX.XX.XXX via FOC-AUSTIN.VA.GOV

### EPI Confirmation Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An EPI Confirmation mail message is sent to the sending site EPI-Report mail group after the EPI HL7 formatted mail message has been received by the AITC database.

### EPI Processing Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Processing Report mail message is sent to the sending facility EPI-Report mail group at the end of the AITC processing cycle (i.e., the 25<sup>th</sup> of each month). The EPI Processing Report mail message confirms that the EPI data has been processed and lists any errors and/or warning codes requiring corrections.

Example: EPI Processing Report

Subj: EPI/LRK \#970451447950300 \[#1425971\] 14 Feb 97 14:55 CST 50 Lines

From: \<POSTMASTER@FOC-AUSTIN.VA.GOV\> in 'IN' basket. Page 1 \*\*NEW\*\*

---------------------------------------------------------------------------

2EPI0001 LRK.

STATION XXX EPI PROCESSING REPORT REPORT DATE 1997/02/11 PAGE 01

PROCESS DATE SSN ENCOUNTER DATE MESSAGE ERROR CODES

19970131 000000190 19970131132151 001 NO ERRORS

19970131 003466370 19961002160512 001 500

19970131 012225556 19970121121609 001 NO ERRORS

19970131 026368799 19961229043131 001 NO ERRORS

19970131 061187860 19960917165748 001 NO ERRORS

19970131 062267678 19970131125821 001 NO ERRORS

19970131 062385860 19961230185116 001 NO ERRORS

19970131 062385860 19970107162010 001 NO ERRORS

19970131 075684002 19970109103417 001 NO ERRORS

19970131 084501279 19970128090146 001 NO ERRORS

19970131 097549144 19970108132918 001 NO ERRORS

19970131 099302298 19970108082142 001 NO ERRORS

19970131 099345601 19970113114752 001 NO ERRORS

19970131 103166277 19970122095702 001 NO ERRORS

19970131 110541525 19970106225241 001 NO ERRORS

19970131 113328446 19970114143128 001 NO ERRORS

19970131 133425965 19970131105820 001 NO ERRORS

19970131 135205512 19960607174229 001 NO ERRORS

19970131 138384641 19970114082310 001 NO ERRORS

19970131 186185119 19960220155121 001 NO ERRORS

19970131 193609042 19970129172826 001 NO ERRORS

19970131 202364130 199701141902 001 NO ERRORS

19970131 218565414 19961011133221 001 500

19970131 229749494 19970123203635 001 NO ERRORS

19970131 250461267 19970121115616 001 NO ERRORS

19970131 253769911 19970115085841 001 NO ERRORS

19970131 254783854 19970118162650 001 NO ERRORS

19970131 259387083 19961028154210 001 NO ERRORS

### EPI Table of Reject and Warning Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example:

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
<p><em>000 Series</em></p>
<p><em>Miscellaneous</em></p>
</blockquote></td>
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
<p>Invalid Batch Sending Facility.</p>
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
<p>PID Segment missing. Do</p>
<p>not edit for the existence</p>
<p>of PID when NTE segments are present.</p>
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
<p>PV1 Segment missing. Do</p>
<p>not edit for the existence</p>
<p>of PV1 when NTE segments are present.</p>
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
<p><em>100 Series</em></p>
<p><em>NTE Totals Segment</em></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
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
<tr class="even">
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
<tr class="odd">
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
<p>Negative Input Ind was</p>
<p>not 'N'.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>200 Series</em></p>
<p><em>PID Segment</em></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
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
<tr class="even">
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
<p>(Also see W03, W04,</p>
<p>and W05)</p>
</blockquote></td>
</tr>
<tr class="odd">
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
<tr class="even">
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
<tr class="odd">
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
</tbody>
</table>

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
<tr class="odd">
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
<tr class="even">
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
<tr class="odd">
<td><blockquote>
<p>240</p>
</blockquote></td>
<td><blockquote>
<p>Period of Military Service</p>
</blockquote></td>
<td><blockquote>
<p>Must be a valid code.</p>
<p>(Refer to table VA011)</p>
</blockquote></td>
<td><blockquote>
<p>Period of Service was invalid.</p>
<p>(Refer to table VA011).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>300 Series</em></p>
<p><em>OBR Segment</em></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>300</p>
</blockquote></td>
<td><blockquote>
<p>Universal Service ID</p>
</blockquote></td>
<td><blockquote>
<p>Must be a valid code.</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Universal Service ID</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>305</p>
</blockquote></td>
<td><blockquote>
<p>Observation Date</p>
</blockquote></td>
<td><blockquote>
<p>Must be numeric date.</p>
<p>Must be a valid date.</p>
<p>Must be less than processing</p>
<p>date.</p>
</blockquote></td>
<td><blockquote>
<p>Observation Date is invalid</p>
<p>date or after the date of</p>
<p>transmission</p>
</blockquote></td>
</tr>
<tr class="odd">
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
<tr class="even">
<td><blockquote>
<p>310</p>
</blockquote></td>
<td><blockquote>
<p>Specimen Source Code</p>
</blockquote></td>
<td><blockquote>
<p>Not required. If not blank,</p>
<p>must be a valid code.</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Specimen Source</p>
<p>Code (also see W07)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>315</p>
</blockquote></td>
<td><blockquote>
<p>Parent Observation ID</p>
</blockquote></td>
<td><blockquote>
<p>Not required. Must be</p>
<p>blank or a valid code.</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Parent Observation ID.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p><em><strong>400 Series</strong></em></p>
<p><em><strong>PV1 Segment</strong></em></p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>400</td>
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
<td>410</td>
<td><blockquote>
<p>Discharge Date</p>
</blockquote></td>
<td><blockquote>
<p>Not required.</p>
<p>Must be blank or a valid</p>
<p>date. Must be less than or</p>
<p>equal to processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Discharge Date is invalid or</p>
<p>after date of transmission.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>411</td>
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
<td>420</td>
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
<td>421</td>
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
</tbody>
</table>

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
<td><p><em><strong>500 Series</strong></em></p>
<p><em><strong>DG1 Segment</strong></em></p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>500</td>
<td><blockquote>
<p>Diagnosis Code</p>
</blockquote></td>
<td><blockquote>
<p>Required. Must be a valid</p>
<p>code.</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Diagnosis Code.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p><em><strong>600 Series</strong></em></p>
<p><em><strong>OBX Segment</strong></em></p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>600</td>
<td><blockquote>
<p>Observation Nat Lab Num.</p>
</blockquote></td>
<td><blockquote>
<p>If not blank, must be</p>
<p>a valid code.</p>
</blockquote></td>
<td><blockquote>
<p>Invalid Observation</p>
<p>Nat Lab Num. (Also see W09)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>605</td>
<td><blockquote>
<p>Final Result Date</p>
</blockquote></td>
<td><blockquote>
<p>Must be blank or a valid date. Must be numeric</p>
<p>date. Must be a less than or equal to the processing date.</p>
</blockquote></td>
<td><blockquote>
<p>Final Result.</p>
<p>Date is invalid or after</p>
<p>the date of transmission.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p><em>W00 Series</em></p>
<p><em>Warnings</em></p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>W03</td>
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
<td>W04</td>
<td><blockquote>
<p>Patient Date of Birth</p>
</blockquote></td>
<td><blockquote>
<p>Year must not be all zeros.</p>
</blockquote></td>
<td><blockquote>
<p>Patient Date of Birth Year is</p>
<p>all zeros. (see also 205)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>W05</td>
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
<td>W07</td>
<td><blockquote>
<p>Specimen Source Code</p>
</blockquote></td>
<td><blockquote>
<p>Blanks in code.</p>
</blockquote></td>
<td><blockquote>
<p>Specimen Source code is</p>
<p>blank. (see also 310)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>W09</td>
<td><blockquote>
<p>Observation</p>
<p>Nat Lab Num.</p>
</blockquote></td>
<td><blockquote>
<p>Blanks in code.</p>
</blockquote></td>
<td><blockquote>
<p>Observation Nat Lab Num is</p>
<p>blank. (Also see 600)</p>
</blockquote></td>
</tr>
</tbody>
</table>

APPENDIX B

NCH USER GUIDE

# NCH User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NCH User Guide provides all the necessary information, instructions, illustrations, and examples required to implement and maintain the V*IST*A Laboratory Search/Extract software application.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

National Center for Health PromotionCholesterol and Pap Screening (NCH): Pursuant to the Congressional mandates stipulated in its enabling legislation (PL. 102-585, U.S.C. 17, 1704), the Department of Veterans Affairs (DVA) National Center for Health Promotion (NCHP) is tasked with monitoring and improving the prevalence of health promotion screening activities provided to veterans VA-wide. The purpose of the NCH Cholesterol and Pap Screening database is to monitor cholesterol and Pap screening activities at a national level, with the ultimate goal for improving detection and treatment of hyperlipidemia and cervical cancer. The NCH Cholesterol and Pap Screening database will also provide a valuable resource for clinical and health services researchers on screening activities and health outcomes, particularly for high-risk and special emphasis group such as veterans with hyperlipidemia, older veterans, and female veterans.

The NCH database is an ongoing initiative. When completed, the NCH database shall consist of a serial (i.e., annual) patient-level database of Cholesterol and Pap Screening procedures conducted in DVA facilities nationally.

At minimum, the NCH database records the following characteristics of the screening procedures:

1\. Records the DVA facility where the procedure was conducted.

2\. Records the Social Security Number (SSN) of the patient.

3\. Records the date the screening procedure was conducted or the date the specimen taken.

4\. Records the type of test provided.

5\. Records the result of the screening procedure.

### Mandate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of the V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 software should be completed in accordance with PL. 102-585, U.S.C. 17, 1704. It is recommended that all VAMCs installed and implemented the software as soon as possible to help facilitate these important initiatives.

### NCH Database Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to the NCH database is currently restricted to the NCHP staff. Upon completion of the NCH Cholesterol and Pap Screening initiative the NCHP office will initiate a data-sharing protocol that ensures adherence to the Privacy Act

(5 U.S.C.552a).

### Impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinicians and clerks in the Laboratory Service are the primarily users of the software. Front-line managers, VISN directors, clinical managers, and health researchers may also have the need to use the software. Telecommunications issues are paramount. The V*IST*A Laboratory Search/Extract software automatically generates and transmits the NCH data to the AITC database daily.

### National Roll-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NCH database is stored at the AITC. The database is compiled in SAS format (i.e., serialized by year). Some NCH database routine reports are generated by the AITC. The NCHP may also generate routine and specialized reports as deemed necessary and appropriate. Data elements included in the national roll-up are proportion of unique patients screened by age, type of test and by date range.

The Denominator file criteria is developed by the NCHP for prevalence ratios for screening activities by the DVA facilities and VISNs. The volume of data expected is very large. It is estimated that the number of records in the NCH database may approach 500,000 annually. Funding is provided by the NCHP to the AITC for NCH database storage and report generation.

### NCH Search and Extract Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 software extracts the NCH data directly from the V*IST*A database. The patient social security number, accession date, and time are used as the unique identifier for the search/extract criteria. The V*IST*A Laboratory Search/Extract software does not add any additional data to the patient medical record. However, because the unique identifier is appended to the record. The NCH data can be linked to the patient record if deemed appropriate. All NCH data extracted by the V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175 are already routinely collected. No new equipment or staffing is necessary to use the V*IST*A Laboratory Search/Extract software.

### Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that the following person(s) <u>jointly</u> participate in reviewing the parameter descriptions:

> Laboratory Information Manager (LIM)

> Total Quality Improvement/Quality Improvement/Quality Assurance (TQI/QI/QA) staff (or person at the site with similar function)

> Representative from the Microbiology section for the Emerging Pathogens Initiative (i.e., director, supervisor, or technologist)

### Periodic Reviews

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NCH parameter descriptions require an ongoing review process (as specified by the NHCP). The person (s) participating in the ongoing review process is responsible for ensuring the following requirements are current:

> Periodic reviews of the <span id="ICD9toICDchange10" class="anchor"></span>ICD codes

> Periodic reviews of the Lab Search/Extract Parameter Setup

> Annual review of the NCHP parameter descriptions

### NCH Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### NCH HL7 formatted mail messages

The V*IST*A Laboratory Search/Extract software automatically processes the NCH data daily producing HL7 formatted mail messages. A Verification Report mail message is then produced for each HL7 mail message. The Verification Report is a copy of the HL7 formatted mail messages in a human readable format.

The NCH HL7 formatted mail messages are daily transmitted automatically by the V*IST*A Laboratory Search/Extract software to the AITC database.

#### NCH Verification Report mail message

The NCH Verification Report is sent to the LR NCH-Report mail group. The members of the LR NCH-Report mail group may use this Verification Report to review the NCH data and make correction as deemed necessary (e.g., social security number, valid date of births, period of service, etc.).

The new Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option can be used to generate the NCH Verification Report and to transmit NCH data corrections to the AITC database.

> **NOTE:** See Appendix B for an example of the NCH Verification Report mail message.

#### NCH Acknowledgment mail message

The NCH Acknowledgment mail message displays the status of the NCH HL7 formatted mail message transmission to the AITC. The NCH Acknowledgment mail message is sent to the sending facility LR NCH-Report mail group.

#### NCH VA View Alert mail message

A NCH VA Alert mail message is sent to the LABORATORY SEARCH/EXTRACT PROTOCOL file (#69.4), Report Mail Group field (#1), after the NCH data has been processed by the AITC.

### Cholesterol Screening

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cholesterol Screening is a critical mechanism in the detection and treatment of hyperlipidemia and coronary artery disease, particularly in high-risk patients. Hyperlipidemia is defined as an undesirable level of plasma lipids. The major lipids are cholesterol and triglycerides. Evidence suggests that elevated total cholesterol, elevated low-density lipoprotein cholesterol, and reduced high-density lipoprotein cholesterol contribute to the development of coronary artery disease. Treatment of hyperlipidemia involves primary and secondary prevention along with pharmacological intervention.

The NCH database is use to assists VA clinicians, Planners, and Researchers in the prevention and treatment of hyperlipidemia by providing estimates of screening rate, age- and sex-adjusted hyperlipidemia prevalence, and actual values for total low-density and high-density lipoprotein cholesterol. The VHA Health Promotion and Disease Prevention Handbook (VHA Handbook 1101.8) recommends that males ages 35 to 65 and females ages 45 to 65 be screened for hyperlipidemia every five years.

Laboratory Services have tended to identify cholesterol screening using the following test names:

Cholesterol HDL CholesterolTriglyceride LDL Cholesterol

#### Cholesterol Screening for Hyperlipidemia

Hyperlipidemia is a major risk factor for cardiovascular disease. Cholesterol Screening detects abnormal blood lipid levels; and subsequent interventions to normalize these levels are effective strategies in the prevention of coronary artery disease. Abnormal blood lipids that are associated with cardiovascular disease are elevated total cholesterol, triglycerides and low density lipoprotein (LDL) levels, and reduced high density lipoprotein (HDL) levels.

Example: Lab Search/Extract Parameter Setup for NCH Cholesterol

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_NCH" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: NCH CHOLESTEROL\<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: NCH Cholesterol ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

CHOLESTEROL

TRIGLYCERIDE

HDL CHOLESTEROL

LDL CHOLESTEROL

\<RET\>

<span id="ICDCodeAdd11" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: NCH Cholesterol ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: NCH Cholesterol ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: NCH Cholesterol ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FIRST ENCOUNTER:\<RET\> Follow PTF:YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Select SEX:\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: NCH Cholesterol ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LRNCH\<RET\>

Run Cycle:DAILY\<RET\> Lag Days:10\<RET\>(Site Specific)

General Description:\<Tab\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

### Papanicolaou (Pap) Screening

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pap Screening is intended to detect cervical dysplasia and cancer at the earliest time possible. Cervical cancer is a disease associated with considerable morbidity and mortality. Approximately 16,000 new cases of cervical cancer are detected in the United States each year with nearly 5,000 deaths.

#### Pap Smear for Cervical Cancer

Currently, the U. S. Preventive Service Task Force and the VHA Health Promotion and Disease Prevention Handbook (VHA Handbook 1101.8) recommend that Pap testing ensure with the onset of sexual activity. Pap testing should be repeated every three years with a possible top age limit for testing at 65, although evidence for this age limit is equivocal.

Example: Lab Search/Extract Parameter Setup for NCH Pap smear

Lab Search/Extract Primary Menu

ENH Lab Search/Extract Manual Run (Enhanced)

<span id="Primary_Menu_NCH_PAP" class="anchor"></span> VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary menu Option: UP\<RET\> Lab Search/Extract Parameter Setup

Select LAB SEARCH/EXTRACT NAME: ?\<RET\>

Answer with LAB SEARCH/EXTRACT NAME, or REFERENCE NUMBER

Do you want the entire 16-Entry LAB SEARCH/EXTRACT List? Y (Yes)\<RET\>

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

NCH CHOLESTEROL

NCH PAP SMEAR

PEN-RES PNEUMOCOCCUS

STREPTOCOCCUS GROUP A

TUBERCULOSIS

VANC-RES ENTEROCOCCUS

Select LAB SEARCH/EXTRACT NAME: NCH PAP SMEAR\<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 1 of 5

NAME: NCH PAP SMEAR ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Laboratory Test(s) Indicator Value

PAP SMEAR

\<RET\>

<span id="ICDCodeAdd12" class="anchor"></span>ICD Coding System \[ICD-9 or ICD-10\]? (9/10):\<RET\>

ICD Code Cd Set ICD Description

\<RET\> \<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: NCH PAP SMEAR ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology Selected Snomed Codes

Antimicrobial Susceptibility NLT Code NLT Description

\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 3 of 5

NAME: NCH PAP SMEAR ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Topography Selection

Include Exclude

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: N\<RET\> Press \<PF1\>H for help Insert

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 4 of 5

NAME: NCH PAP SMEAR ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

FIRST ENCOUNTER:NO\<RET\> Follow PTF:YES\<RET\>

BEFORE DATE OF BIRTH:\<RET\> AFTER DATE OF BIRTH:\<RET\>

Select SEX:\<RET\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 5 of 5

NAME: NCH PAP SMEAR ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Run Date:\<RET\> Protocol:LRNCH\<RET\>

Run Cycle:DAILY\<RET\> Lag Days:10\<RET\>(Site Specific)

General Description:\<Tab\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

COMMAND: E\<RET\> Press \<PF1\>H for help Insert

Save changes before leaving form (Y/N)?Y\<RET\>

## NCH Mail Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are examples of mail messages and reports that are produced by the V*IST*A Laboratory Search/Extract Patch LR\*5.2\*175.

#### NCH HL7 Formatted Mail Message

The V*IST*A Laboratory Search/Extract software automatically transmits the NCH HL7 formatted mail messages daily to the AITC, formerly AITC, database.

Example: NCH HL7 formatted mail messages transmission to the AITC database

MSH\|~^\\\|NCH-LAB\|525\|NCH-AITC\|200\|19980505160420\|\|ORU~R01\|1810579\|6\|2.2\|\|\|NE\|AL\|USA

NTE\|\|R~REPORTING DATE FROM 19980422 TO 19980422~1

PID\|1\|<span id="p421_134" class="anchor"></span>000-10-5466~9~M10\|69604~5~M10\|\|EPI~PATFOUR\|\|00041027\|M\|\|6\|~01603\|\|\|\|\|\|

\|\|034105466\|\|\|\|\|\|\|\|2

PV1\|1\|O\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|19980422080566

NTE\|1\|50~NCH CHOLESTEROL

OBR\|1\|\|\|81121.0000~CHEMISTRY TEST~VANLT\|\|\|19980422080566\|\|\|\|\|\|\|\|SER\~~SERUM\|\|\|R/

CH 0422 340

OBX\|1\|ST\|82466.0000~Cholesterol Total~VANLT~183~CHOLESTEROL~VA60\|\|165\|mg/dl\|"

SEE TEST DESC"-\|\|\|\|\|\|\|19980423140447OBX\|2\|ST\|83013.0000~Cholesterol HDL~VANLT~244~HDL CHOLESTEROL~VA60\|\|30\|mg/dl\|30-65\|\|\|\|\|\|\|19980423140447

OBX\|3\|ST\|82350.0000~Calculation~VANLT~901~LDL CHOLESTEROL~VA60\|\|109c\|mg/dl\|"

### NCH Verification Report mail message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NCH Verification Report mail message may be sent to the LR NCH Report mail group. Members of the LR NCH Report mail may choose to review the NCH data and make corrections (e.g., social security number, valid date of births, period of service, etc.) as deemed appropriate. The new Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option automatically transmits the NCH data corrections to the AITC database.

Example: NCH Verification Report mail message.

MailMan message for DOE,DAVID R LAB PROGRAMMER

Printed at BROCKTON.VA.GOV 05 May 98 16:06

Subj: National Center for Health Promotion \[#13326619\] 05 May 98 16:04

21 Lines

From: POSTMASTER in 'IN' basket. Page 1

------------------------------------------------------------------------------

REPORTING DATE FROM 04-22-1998 TO 04-22-1998 Message Seq \# 1 manual

EPI PATFIVE <span id="PII_000_SSN_4" class="anchor"></span>000-07-5914 10-27-1925 M WORLD WAR II 01603

Outpatient Accession Date 04-22-1998@0805

\*\*\*\*\*\*\*\*\* 50 NCH CHOLESTEROL \*\*\*\*\*\*\*\*\*

04-22-1998@0805 R/CH 0422 340 CHEMISTRY TEST SERUM

CHOLESTEROL 04-23-1998@1404 165 mg/dl " SEE TEST DESC"-

HDL CHOLESTEROL 04-23-1998@1404 30 mg/dl 30-65

LDL CHOLESTEROL 04-23-1998@1404 109c mg/dl " SEE TEST DESC"-

TRIGLYCERIDE 04-23-1998@1404 160 mg/dl 35-200

TOTAL 82466.0000 CHOLESTEROL 1

TOTAL 82466.0000 PATIENTS WITH CHOLESTEROL 1

TOTAL TRIGLYCERIDE 1

TOTAL PATIENTS WITH TRIGLYCERIDE 1

TOTAL 83013.0000 HDL CHOLESTEROL 1

TOTAL 83013.0000 PATIENTS WITH HDL CHOLESTEROL 1

TOTAL 82350.0000 LDL CHOLESTEROL 1

TOTAL 82350.0000 PATIENTS WITH LDL CHOLESTEROL 1

### NCH HL7 Mail Message Status List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 Message Status List contains the status of each transmission sent by the site to the AITC database.

Example: HL7 Message Status List

HL7 MESSAGE STATUS LIST JUL 8,1998 14:02 PAGE 1

-----------------------------------------------------------------

NAME: APPLICATION LEVEL ERROR CODE: ALE

DESCRIPTION: An error occurred while the application was processing the message. The Error Message field of the Message Text file provides a description of the error.

NAME: AWAITING ACKNOWLEDGEMENT CODE: AA

DESCRIPTION: The message has been sent, but has not yet been acknowledged as having been processed by the receiving application.

NAME: AWAITING PROCESSING CODE: AP

DESCRIPTION: The message is awaiting processing by the receiving application.

NAME: BEING GENERATED CODE: BG

DESCRIPTION: The message is in the process of being generated and stored in

the Message Text file by the Messaging System.

NAME: ERROR DURING GENERATION CODE: EDG

DESCRIPTION: An error occurred during the generation of the message.

NAME: ERROR DURING PROCESSING CODE: EDP

DESCRIPTION: An error occurred during the processing of the message.

NAME: ERROR DURING TRANSMISSION CODE: EDT

DESCRIPTION: An error occurred during the transmission of the message.

NAME: PENDING TRANSMISSION CODE: PT

DESCRIPTION: The message is waiting to be transmitted.

NAME: SUCCESSFULLY COMPLETED CODE: SC

DESCRIPTION: One of the following actions was accomplished for the message:

The message was successfully generated. The message was successfully sent and no acknowledgment is required. The message was successfully sent and acknowledged.

### NCH HL7 Formatted (Acknowledgment) mail message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of the NCH HL7 formatted Acknowledgment mail message received from the AITC.

Example: NCH HL7 formatted Acknowledgment mail message.

> DATE/TIME ENTERED: MAY 18, 1998@22:13:27

> SERVER APPLICATION: NCH-AITC TRANSMISSION TYPE: *INCOMING*

> MESSAGE ID: 1855276 PARENT MESSAGE: MAY 17, 1998@02:08:05

> PRIORITY: IMMEDIATE RELATED EVENT PROTOCOL: LRNCH

> MESSAGE TEXT:

> MSH^~\|\\^NCH-AITC^200^NCH-LAB^525^19980518210822^^ACK~^1855276^P^2.2^^^NE^AL\|

> MSA^AA^1855276

> DSP^0001^999999999::000

> DSP^0001^006309421:19980512125558:000 3

> DSP^0001^009381088:19980514103659:000

### NCH Acknowledgment mail message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NCH Acknowledgment mail message displays the status of the NCH HL7 formatted Acknowledgment mail message in a human readable format. The NCH Acknowledgment mail message is sent to the LR NCH-Report mail group. If the NCH Acknowledgment mail message displays an error, make corrections (e.g., social security number, valid date of births, period of service, etc.) as deemed necessary. Use the new Lab Search/Extract Manual Run (Enhanced) \[LREPI ENHANCED MANUAL RUN\] option to automatically transmit the NCH data corrections to the AITC database.

Example: NCH Acknowledgment mail messages in a human readable format.

Subj: Acknowledgment message from NCH. \[#13202750\] 22 Apr 98 16:36 3 Lines

From: DOE,DAVID K in 'IN' basket. Page 1

-----------------------------------------------------------------

Flash... This is an acknowledgment message from NCH

Message \#: 1 From the status file 771.6 message is categorized as:

Message: 1746675 AWAITING PROCESSING @ Apr 22, 1998@16:32:48

Subj: Acknowledgement message from Austin. \[#13224503\] 24 Apr 98 11:32 3 Lines

From: POSTMASTER - POSTMASTER (Sender: DOE,DAVID R - LAB PROGRAMMER) in 'LAB SEARCH' basket. Page 1

------------------------------------------------------------------------------

Flash... This is an acknowledgement message from NHC

Message \#: 1 From the status file 771.6 message is categorized as:

Message: 1733492 ERROR DURING TRANSMISSION @ Apr 14, 1998@09:15:44

Subj: Acknowledgement message from NHC. \[#13128237\] 14 Apr 98 19:31 3 Lines

From: DOE,<span id="p421_138" class="anchor"></span>EPI R - LAB PROGRAMMER in 'LAB SEARCH' basket. Page 1

------------------------------------------------------------------------------

Flash... This is an acknowledgement message from NHC

Message \#: 1 From the status file 771.6 message is categorized as:

Message: 1711986 SUCCESSFULLY COMPLETED @ Apr 08,

## NCH VA Alert

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A NCH VA Alert mail message is sent to the LABORATORY SEARCH/EXTRACT PROTOCOL file (#69.4), Report Mail Group field (#1) after NCH transmissions has been processed by the AITC.

Example: NCH VA Alert mail message from the AITC

1.I National Center for Health Promotion Was processed at JUN 30, 1998@03:

2.I National Center for Health Promotion Was processed at JUN 29, 1998@03:

3.I National Center for Health Promotion Was processed at JUN 28, 1998@02:

4.I National Center for Health Promotion Was processed at JUN 27, 1998@02:

5.I National Center for Health Promotion Was processed at JUN 26, 1998@03:

Select from 1 to 5 or enter ?, A I, F, P, M, R, or ^ to exit: A

Processed Alert Number 1

National Center for Health Promotion Was processed at JUN 30, 1998@03:08:20

Processed Alert Number 2

National Center for Health Promotion Was processed at JUN 29, 1998@03:11:13

Processed Alert Number 3

National Center for Health Promotion Was processed at JUN 28, 1998@02:33:00

Processed Alert Number 4

National Center for Health Promotion Was processed at JUN 27, 1998@02:25:11

Processed Alert Number 5

National Center for Health Promotion Was processed at JUN 26, 1998@03:19:22

APPENDIX-C

EDITING FILES, LINKING DATA, EDITING SCREENS, REQUEST FORM

# Editing Files/Screens, Linking Data, Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains instructions for, editing files, linking data, and a Workload and Suffix Code Request Form (that can be reproduced).

## Editing TOPOGRAPHY file (#61)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific HL7 codes must be added to the TOPOGRAPHY file (#61). The HL7 Code field (#08) in this file is used to add the entries. Specific HL7 codes that must be added to File \#61 is located in the HL7 section of this guide, Table 0070 (Specimen Source Codes). The following is an example of how to add the specific HL7 codes to the TOPOGRAPHY file (#61) using VA FileMan - Enter Or Edit File Entries \[ \] option.

Example: How to add specific HL7 codes to TOPOGRAPHY file (#61)

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: TOPOGRAPHY FIELD// \<RET\>

EDIT WHICH FIELD: ALL// .08 HL7 CODE

THEN EDIT FIELD: \<RET\>

Select TOPOGRAPHY FIELD NAME: ? \<RET\>

Answer with TOPOGRAPHY FIELD NAME, or SNOMED CODE, or ABBREVIATION, or

SYNONYM

Do you want the entire 8575-Entry TOPOGRAPHY FIELD List? NO\<RET\>

You may enter a new TOPOGRAPHY FIELD, if you wish

ANSWER MUST BE 2-80 CHARACTERS IN LENGTH

Select TOPOGRAPHY FIELD NAME: AMNIOTIC FLUID 8Y300

HL7 CODE: ? \<RET\>

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

HL7 CODE: AMN\<RET\>

## How to Link Antimicrobial Entries to Workload Codes Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post INIT links as many of the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) entries to the WKLD CODE file (#64) entries that are identified in your site files. However, the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) entries that were not linked (i.e. no match found) to the WKLD CODE file (#64) will require linking. The Antimicrobial Link Update \[LREPILK\] option contains the following three options that are used to <u>identify</u> and <u>link</u> the entries that were not linked by the post INIT.

### Using the Antimicrobial Link Update \[LREPILK\] options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example:

Select Lab Search/Extract Primary Menu\<RET\>

<span id="p150" class="anchor"></span> ENH Lab Search/Extract Manual Run (Enhanced)

VR Print Detailed Verification Report

LO Local Pathogen Menu ...

PI Pathogen Inquiry

UP Lab EPI Parameter Setup

Lab EPI Protocol Edit

LK Antimicrobial Link Update

Select Lab Search/Extract Primary Menu Option: LK \<RET\> Antimicrobial Link Update

This option will allow you to link file '62.06 ANTIMICROBIAL

SUSCEPTIBILITY' file with file '64 WKLD CODE.

Select one of the following:

A AUTO

M MANUAL

S SEMI-AUTO

#### How to link entries using the AUTO option

The AUTO option identifies and attempts to link entries that are not currently linked. This option also displays linked and non linked entries.

Example:

Enter response: A\<RET\>UTO

AMIKACN \<----Linked----\> Amikacin

AMPICLN \<----Linked----\> Ampicillin

CLINDAM \<----Linked----\> Clindamycin

POLYMYXIN B \<----Not Linked----\>No Match Found

RIFAMPIN \<----Linked----\> Rifampin

#### How to add and delete entries to a file using the MANUAL option

The MANUAL option will create or edit the links. Selections are from entries in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06).

Example:

Enter response: M\<RET\>ANUAL

Select ANTIMICROBIAL SUSCEPTIBILITY NAME: PENICLIN\<RET\> PENICILLIN

NATIONAL VA LAB CODE: Substance P// PEN\<RET\>

1 PENFIELD AND CONE STAIN 88010.0000

2 PENICILLIN Penicillin 81852.0000

3 PENTAZOCINE Pentazocine 81854.0000

4 PENTOBARBITAL Pentobarbital 81856.0000

CHOOSE 1-4: 2 Penicillin\<RET\>

Select ANTIMICROBIAL SUSCEPTIBILITY NAME: VANCMCN\<RET\> VANCOMYCIN

NATIONAL VA LAB CODE: Shell Vial Technique// VANCOMYCIN\<RET\> Vancomycin

81485.0000\<RET\>

Select ANTIMICROBIAL SUSCEPTIBILITY NAME: Ampicillin/sulbactam\<RET\> Ampicillin/subalctam

NATIONAL VA LAB CODE: Ampicillin// @\<RET\>

SURE YOU WANT TO DELETE? Y (Yes)\<RET\>

Select ANTIMICROBIAL SUSCEPTIBILITY NAME:

#### How to add entries using the SEMI-AUTO option.

The SEMI-AUTO option looks for entries that are not currently linked and prompts the user to select the corresponding entry in the WKLD CODE file (#64).

Example:

Enter response: S\<RET\>EMI-AUTO

AMIKACN AMIKACIN

NATIONAL VA LAB CODE: AMIK\<RET\>ACIN Amikacin 81098.0000

Continue YES/\<RET\>

AMPICLN AMPICILLIN

NATIONAL VA LAB CODE: AMP\<RET\>

1 AMP CYCLIC 81029.0000

2 AMPHETAMINE Amphetamine 81528.0000

3 AMPHOTERICIN B Amphotericin B 81530.0000

4 AMPICILLIN Ampicillin 81532.0000

CHOOSE 1-4: 4 Ampicillin

Continue YES// \<RET\>

CLINDAM CLINDAMYCIN

NATIONAL VA LAB CODE: CLINDAMYCIN Clindamycin 81676.0000

Continue YES// \<RET\>

CARBCLN CARBENICILLIN

NATIONAL VA LAB CODE:

Continue YES// NO \<RET\>

### How to Delete an Entry from the Laboratory Search/Extract Parameters Input Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the tab key to move the cursor. Highlight the entry that is to be deleted, select the “@” symbol, then press enter/return. You will then receive a deletion warning asking if you are sure.

Example: Deleting an Entry

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: CANDIDA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

CANDIDA PARAPSILOSIS \<Tab\>

CANDIDA PSEUDOTROPICALIS \<Tab\>CANDIDA SKIN TEST ANTIGEN @ \<Ret\>

CANDIDA STELLATOIDEA

Antimicrobial Susceptibility NLT Code NLT Description

\<Tab\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

COMMAND: Press \<PF1\>H for help

> **WARNING:** DELETIONS ARE DONE IMMEDIATELY!

(EXITING WITHOUT SAVING WILL NOT RESTORE DELETED RECORDS.)

Are you sure you want to delete this entire Subrecord (Y/N)? y \<Ret\>

### How to add an entry using the Laboratory Search/Extract Parameters Input Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the tab key to move the cursor. Highlight a blank line where the entry is to be added.

Example:

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: CANDIDA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

CANDIDA

CANDIDA GUILLIERMONDII

CAN \<Ret\>

Antimicrobial Susceptibility NLT Code NLT Description

\<Tab\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

1 CAN CANDIDA ALBICANS 4081

2 CANARYPOX VIRUS 3604

3 CANDICIDIN 7328

4 CANDIDA, NOS 4080

5 CANDIDA GUILLIERMONDII 4082

Choose 1-5 or '^' to quit: 1\<Ret\>

LABORATORY SEARCH/EXTRACT PARAMETERS INPUT SCREEN Page 2 of 5

NAME: CANDIDA ACTIVE: YES

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Selected Etiology

CANDIDA GUILLIERMONDII

CANDIDA KRUSEI

CANDIDA ALBICANS \<- The entry will appear after answering yes

to the adding a new ETIOLOGY prompt.

Antimicrobial Susceptibility NLT Code NLT Description

\<Tab\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

CAN CANDIDA ALBICANS

Are you adding 'CANDIDA ALBICANS' as a new ETIOLOGY? Y \<Ret\>

### Additional Workload and Suffixes Codes Request Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Request Form may be reproduced and used for requesting additional Workload and Suffixes codes. Please submit the Request Form to the address located at bottom of form.

Additional Workload and Suffixes Codes Request Form

Site Name:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Site Number:\_\_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_\_\_

Contact Person:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Commercial PH#\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ EXT\_\_\_\_\_

FTS PH#:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ EXT\_\_\_\_\_\_

Procedure Name \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Abbreviations: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Procedure Name \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Abbreviations: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Procedure Name \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Abbreviation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Method: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Abbreviation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Method: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Abbreviation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Method: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Lab Section \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Abbreviation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Instrument Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Manufacturer’s Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Submit Request Forms to: *Frank Stalling, P&LMS Informatics Manager*

> *1901 North Highway 360, Suite 351*

> *Grand Prairie, Texas 75050*