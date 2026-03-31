---
title: Oncology Version 2.2 User Manual (Updated ONC*2.2*22)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: (Updated ONC*2.2*22)
app_code: ONC
app_name: "Registry: Oncology"
section: CLI
app_status: active
pkg_ns: ONC
patch_ver: 2.2
patch_id: ONC*2.2
group_key: "ONC:ONC:2.2"
file_numbers: 
  - 165
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - patient
  - table
  - contents
  - date
  - follow
  - site
  - primary
  - abstract
  - strong
  - print
page_count: 0
word_count: 18307
section_count: 80
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: JUNE 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Oncology/onc_2_2_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Oncology/onc_2_2_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=81"
---

ONCOLOGY (ONC)USER MANUAL

![](oncology-version-2-2-user-manual-updated-onc-2-2-22/001.png)

JUNE 2014(Revised September 2025)Office of Information and Technology (OI&T)Enterprise Program Management Office  
Revision History

When updates occur, the Title Page lists the new revised date, and this page describes the changes. Bookmarks link the described content changes to its place within manual. There are no bookmarks for format updates. Page numbers change with each update; therefore, they are not included as a reference in the Revision History.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 61%" />
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
<td>Implement the NAACCR 2025 field updates and the v25 EDITs metafile. These changes are based on the NAACCR 2025 Implementation Guide.</td>
</tr>
<tr class="even">
<td>March 2025</td>
<td>ONC*2.2*21</td>
<td><p>Implement the remainder of the NAACCR 2024 field updates and the v24 EDITs metafile. These changes are based on the NAACCR 2024</p>
<p>Implementation Guide.</p>
<p>SSDi (Site Specific Data Item) updates (section 3.1 of the Implementation Guide), AJCC (American Joint Commission On Cancer) Version 9 protocols (section 5.6) as well as Histology updates (section 5.7), and EOD (Extent of Disease) updates (section 5.8).</p>
<p>Update the State, RCRS (Rapid Cancer Reporting System) and NCDB (National Cancer Database) reports to the latest NAACCR layout.</p>
<p>Reset any completed 2024 Abstracts to Partial status and not allow users to complete any 2025 cases because the 2025 metafile is not implemented yet. The next patch will allow users to complete 2025 cases.</p>
<p>A post-initialization routine will display any users in the Oncology Package that do not have the INITIAL (#1) field in the New</p>
<p>Person (#200) file set.</p>
<p>The display of the histology reverts to the original value for cases accessioned from suspense. This patch will fix the issue in the display.</p>
<p>Restrict the values in the Casefinding Source (#21) field of the Oncology Primary (#165.5) file to only the values specified in the</p>
<p>VACRS manual.</p>
<p>Change the default values of two fields. The Reporting Facility (#.03) field of the Oncology Primary (#165.5) file will default to the facility in the Registry Parameters and the Type of Reporting Source (#1.2) field of the Oncology Primary (#165.5) file will default to a value of 1.</p>
<p>Change the name of field #49 of the Oncology</p>
<p>Primary (#165.5) file to DATE 1ST CRS RX COC and change the name of field #49.9 of the Oncology Primary (#165.5) file to DATE INITIAL RX SEER. These 2 fields will now display in the First Course of Treatment section and the Extended Abstract</p>
<p>Display.</p></td>
</tr>
<tr class="odd">
<td>September 2024</td>
<td>ONC*2.2*20</td>
<td><p>Implement NAACCR (North American Association of Central Cancer Registries) 2023 updates and Edits.</p>
<p>Provide updates including calculation changes for AJCC (American Joint Commission on Cancer) Version 9 protocols to the Anus, Appendix, Brain, CNS Other and Intracranial Gland schemas, as well as a new schema called Medullablastoma.</p>
<p>Update State, RCRS (Rapid Cancer Reporting System) and NCDB (National Cancer DataBase) extracts to v23.</p>
<p>Reset any completed 2023 and 2024 cases to Partial status.</p>
<p>Automatically jump to the Text-Remarks (File #165.5, #13) field if a case is set to "Pending Delete" to allow users to enter a reason.</p>
<p>Update the Casefinding Source (File #165.5, #21) field and the description for Code 20 in the Casefinding Source field.</p>
<p>Display Treatment fields when a Date of No Treatment (File #165.5, #124) is entered.</p>
<p>Allow users to edit the treatment fields when a Date of No Treatment value is entered, instead of stuffing and skipping over those fields.</p>
<p>Update the six Exposure fields: AGENT ORANGE</p>
<p>EXPOSURE (#160, #48), IONIZING RADIATION EXPOSURE (#160, #50), CHEMICAL EXPOSURE (#160, #52), ASBESTOS EXPOSURE (#160, #61), BURN PIT EXPOSURE (#160, #72) and OTHER TOXIC EXPOSURE ((#160, #73).</p>
<p>Add HISTOLOGY (#165.5, #20) as an optional field value brought in when a new case is accessioned.</p>
<p>Add the Gender Identity and Sexual Orientation demographic data fields from the PATIENT file into the case ascertainment section.</p>
<p>Make the FEE BASIS field (#165.5 ,#237) a required field. If set to "YES" then the FEE BASIS LOCATION (#165.5, #237.1) will also be required.</p>
<p>Fix the Restage CS Cases Using Latest Version [ONCO UTILCS RESTAGING] option which was not working correctly after the cloud migration in Patch ONC*2.2*19.</p></td>
</tr>
<tr class="even">
<td>June 2024</td>
<td>ONC*2.2*19</td>
<td><p>NAACCR Edits and Collaborative Staging moved to a cloud server.</p>
<p>Correct an issue with 'Pending Delete' Abstract Status.</p>
<p>Correct the "NA" (Not Applicable) code</p>
<p>for Race fields.</p>
<p>Correct several typographical errors in text and code descriptions.</p></td>
</tr>
<tr class="odd">
<td>November 2023</td>
<td>ONC*2.2*18</td>
<td><p><a href="#pt-automatic-case-finding---ptf-search">PT Automatic Case Finding - PTF Search</a></p>
<p>ICD codes to be searched updated</p>
<p><a href="#dp-delete-oncology-patient">DP Delete OncoTrax Patient</a></p>
<p><a href="#ds-delete-primary-sitegp-record">DS Delete Primary Site/Gp Record</a></p>
<p>The functionality in these options will be removed</p></td>
</tr>
<tr class="even">
<td>June 2023</td>
<td>ONC*2.2*17</td>
<td><p><a href="#utl-utility-options-module">UTL Utility Options Module</a></p>
<p>Added UPC Update Oncology Physician Contacts</p>
<p><a href="#rs-registry-summary-reports">RS Registry Summary Reports</a></p>
<p>The Follow-up report offers two options that meet the ACoS requirements</p>
<p><a href="#upc-update-oncology-physician-contacts">UPC Update Oncology Physician Contacts</a> description added</p>
<p>Available Record Layouts added</p></td>
</tr>
<tr class="odd">
<td>April 2023</td>
<td>ONC*2.2*16</td>
<td><a href="\l">Appendix A: Edits API</a></td>
</tr>
<tr class="even">
<td>October 2022</td>
<td>ONC*2.2*15</td>
<td><p><a href="#entering-a-first-primary-for-a-patient">Remove obsolete warnings when completing cases</a></p>
<p><a href="#edits-within-oncotrax">Require more data fields to be entered before accessioning a case</a></p>
<p>Update Site-Specific Data Item (SSDi) fields</p>
<p>Add new codes to Extent Of Disease (EOD) and</p>
<p>Site Specific Data Item (SSDi) fields</p>
<p>Correct TNM Edition number issues</p>
<p>Correct Schema ID calculation</p>
<p>Correct issues in the Oncology Casefinding reports</p>
<p>Update XML Extract reports</p>
<p>Update RCRS Report dates to include cases back to 2006</p></td>
</tr>
<tr class="odd">
<td>March 2022</td>
<td>ONC*2.2*14</td>
<td><p><a href="#rcrs-create-rcrs-extract">Update the ONCO RCRS Extract Report to XML format</a></p>
<p><a href="#pt-automatic-case-finding---ptf-search">Update the NAACCR and SEER Extract Reports to XML format</a></p>
<p>Update the Extract Report options to include Cervix cases</p>
<p>Include the Date Initial RX SEER (NAACCR item #1260) in extracts</p>
<p>Correct a typo in the 8077/2 Histology description.</p>
<p>Add the missing 750 value to the Extent of Disease (EOD) Primary Tumor Code for Schema 00795</p>
<p>Add new field called SCHEMA ID DESCRIPTION (#165.5, #3800.1) to the Abstract</p></td>
</tr>
<tr class="even">
<td>December 2021</td>
<td>ONC*2.2*13</td>
<td><p>Revised to reflect current record layout (NAACCR Standards Vol II version 2021) and AJCC 9<sup>th</sup> Edition Staging and related changes <a href="#upc-update-oncology-physician-contacts">Create State/VACCR Data Download</a> and will update the <a href="#cf-automatic-case-finding---lab-search">Automatic Casefinding – Lab Search</a>, <a href="#qa-print-abstract-qa-80c">Print Abstract QA</a>, <a href="#ex-print-abstract-extended-80c">Print Abstract-Extended</a>, <a href="#pa-print-complete-abstract-132c">Print Complete Abstract</a> and <a href="#ma-print-qamultiple-abstracts">Print QA/Multiple Abstracts</a> reports</p>
<p>Update Site-Specific Data Item (SSDi) fields</p>
<p>Resolved the American Joint Commission on Cancer (AJCC) ID issue for Oropharynx cases</p>
<p>Remove SYMENC^MXMLUTL Kernel call from ONC code</p>
<p>Update Histology code lists and surgery codes</p>
<p>Address Extent of Disease (EOD) 2.0 Updates</p>
<p>Add 4 new COVID fields and new AJCC 9th Edition Staging fields</p>
<blockquote>
<p>NCDB-SARSCOV2-TEST (#165.5, 3943)</p>
<p>NCDB-SARSCOV2-POSITIVE (#165.5, 3944)</p>
<p>NCDB-SARSCOV2-POSITIVE DATE (#165.5, 3945)</p>
<p>NCDB-SARSCOV2-COVID-19-TX-IMPACT (#165.5, 3946)</p>
</blockquote>
<p>Update the Lab-Casefinding list for 2021 codes</p>
<p>Address Collaborative Stage and Bad Gateway Errors</p></td>
</tr>
<tr class="odd">
<td>October 2020</td>
<td>ONC*2.2*12</td>
<td>Revised to reflect changes for version 18D Metafile including updates to <a href="#upc-update-oncology-physician-contacts">Create State/VACCR Data Download</a> options (Richard Knoepfle)</td>
</tr>
<tr class="even">
<td>May 2020</td>
<td>ONC*2.2*10</td>
<td><p>PF Post/Edit Follow-up</p>
<p>Revised to reflect current record layout (NAACCR Standards Vol II version 2018) and AJCC 8<sup>th</sup> Edition Staging and related changes (Richard Knoepfle)</p>
<p>Updated title page, footers, revision history, and table of contents. Updated Facility Oncology Registry Data Standards (FORDS) website Recommended Websites</p>
<p>Updated National Cancer Database website Downloading and Installing Genedits</p>
<p>Updated NAACCR Standards website Edits within Genedits</p>
<p>Removed ONC*2.11*47 Patch installation instructions</p>
<p>(Kimberly Meneguzzo)</p></td>
</tr>
<tr class="odd">
<td>August 2017</td>
<td>ONC*2.2*6</td>
<td>Revised to reflect current record layout (NAACCR v16) and associated utilities (Richard Knoepfle)</td>
</tr>
<tr class="even">
<td>June 2015</td>
<td>ONC*2.2*4</td>
<td>Revised to reflect current record layout (NAACCR v15) (Kathleen Waller)</td>
</tr>
<tr class="odd">
<td>May 2007</td>
<td>ONC*2.11*47</td>
<td>Initial Publication of OncoTraX: Cancer Registry User Manual (Christine Beynon)</td>
</tr>
</tbody>
</table>

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Recommended Users](#recommended-users)
  - [Related Manuals](#related-manuals)
  - [Recommended Websites](#recommended-websites)
  - [OncoTrax Conventions](#oncotrax-conventions)
  - [OncoTrax Menu](#oncotrax-menu)
  - [Getting Started](#getting-started)
  - [Define Tumor Registry Parameters](#define-tumor-registry-parameters)
- [SUS Case Finding and Suspense Module](#sus-case-finding-and-suspense-module)
  - [CF Automatic Case Finding - Lab Search](#cf-automatic-case-finding-lab-search)
  - [LR Print Case Finding - Lab Report](#lr-print-case-finding-lab-report)
  - [RA Automatic Case Finding - Radiology Search](#ra-automatic-case-finding-radiology-search)
  - [PT Automatic Case Finding - PTF Search](#pt-automatic-case-finding-ptf-search)
  - [SE Add/Edit/Delete from Suspense](#se-addeditdelete-from-suspense)
    - [Adding a VA Patient to Suspense](#adding-a-va-patient-to-suspense)
    - [Editing a VA Patient in Suspense](#editing-a-va-patient-in-suspense)
    - [Deleting a VA Patient from Suspense](#deleting-a-va-patient-from-suspense)
  - [SP Print Suspense List by Suspense Date (132c)](#sp-print-suspense-list-by-suspense-date-132c)
  - [NP Patients in Suspense with No Primaries](#np-patients-in-suspense-with-no-primaries)
- [DI Disease Index](#di-disease-index)
  - [AI Complete Abstract](#ai-complete-abstract)
    - [Abstracting a Case](#abstracting-a-case)
    - [Completing an Abstract](#completing-an-abstract)
  - [EE Abstract Edit Primary](#ee-abstract-edit-primary)
  - [NC Print Abstract NOT Complete List](#nc-print-abstract-not-complete-list)
  - [IR Patient Summary](#ir-patient-summary)
  - [QA Print Abstract QA (80c)](#qa-print-abstract-qa-80c)
  - [EX Print Abstract-Extended (80c)](#ex-print-abstract-extended-80c)
  - [PA Print Complete Abstract (132c)](#pa-print-complete-abstract-132c)
  - [MA Print QA/Multiple Abstracts](#ma-print-qamultiple-abstracts)
  - [AS Abstract Screens Menu (80c)](#as-abstract-screens-menu-80c)
- [FOL Follow-up Module](#fol-follow-up-module)
  - [PF Post/Edit Follow-up](#pf-postedit-follow-up)
  - [RF Recurrence/Sub Tx Follow-up](#rf-recurrencesub-tx-follow-up)
  - [FH Patient Follow-up History](#fh-patient-follow-up-history)
  - [DF Print Due Follow-up List by Month Due](#df-print-due-follow-up-list-by-month-due)
  - [LF Print Delinquent (LTF) List](#lf-print-delinquent-ltf-list)
  - [FP Follow-up Procedures Menu](#fp-follow-up-procedures-menu)
  - [Follow-up Letter](#follow-up-letter)
  - [AA Accession Register-ACoS (80c)](#aa-accession-register-acos-80c)
  - [AS Accession Register-Site (80c)](#as-accession-register-site-80c)
  - [AE Accession Register-EOVA (132c)](#ae-accession-register-eova-132c)
  - [PA Patient Index-ACoS (132c)](#pa-patient-index-acos-132c)
  - [PS Patient Index-Site (80c)](#ps-patient-index-site-80c)
  - [PE Patient Index-EOVA (132c)](#pe-patient-index-eova-132c)
  - [IN Primary ICDO Listing (80c)](#in-primary-icdo-listing-80c)
  - [SG Primary Site/GP Listing (80c)](#sg-primary-sitegp-listing-80c)
  - [IW Primary ICDO Listing (132c)](#iw-primary-icdo-listing-132c)
- [ANN Annual Reporting Module](#ann-annual-reporting-module)
  - [AAR Annual ACoS Accession Register (80c)](#aar-annual-acos-accession-register-80c)
  - [API Annual ACoS Patient Index (132c)](#api-annual-acos-patient-index-132c)
  - [ASL Annual Primary Site/GP Listing (132c)](#asl-annual-primary-sitegp-listing-132c)
  - [ACL Annual Patient List by Class of Case (80c)](#acl-annual-patient-list-by-class-of-case-80c)
  - [SST Annual Primary Site/Stage/Tx (132c)](#sst-annual-primary-sitestagetx-132c)
  - [TST Annual ICDO Topography/Stage/Tx (132c)](#tst-annual-icdo-topographystagetx-132c)
  - [SDX Annual Status/Site/Dx-Age (132c)](#sdx-annual-statussitedx-age-132c)
  - [HIS Annual Histology/Site/Topography (80c)](#his-annual-histologysitetopography-80c)
  - [ACT Annual Cross Tabs (80c)](#act-annual-cross-tabs-80c)
  - [CPR PRINT Custom Reports](#cpr-print-custom-reports)
- [STA Statistical Reporting Module](#sta-statistical-reporting-module)
  - [DS Define Search Criteria](#ds-define-search-criteria)
    - [SP Survival by Site](#sp-survival-by-site)
    - [SS Survival by Stage](#ss-survival-by-stage)
    - [TX Survival by Treatment](#tx-survival-by-treatment)
  - [TS Treatment by Stage - Cross Tabs](#ts-treatment-by-stage-cross-tabs)
- [UTL Utility Options Module](#utl-utility-options-module)
  - [RS Registry Summary Reports](#rs-registry-summary-reports)
  - [DP Delete Oncology Patient](#dp-delete-oncology-patient)
  - [DS Delete Primary Site/Gp Record](#ds-delete-primary-sitegp-record)
  - [SQ Find Duplicate Acc/Seq Numbers](#sq-find-duplicate-accseq-numbers)
  - [EA Edit Site/AccSeq# Data](#ea-edit-siteaccseq-data)
  - [AR Create a Report to Preview ACoS Output](#ar-create-a-report-to-preview-acos-output)
  - [CT Create ACoS Data Download](#ct-create-acos-data-download)
  - [SR Create a Report to Preview State/VACCR Output](#sr-create-a-report-to-preview-statevaccr-output)
  - [CC Create State Data Download](#cc-create-state-data-download)
  - [TR Define Tumor Registry Parameters](#tr-define-tumor-registry-parameters)
  - [AC Enter/Edit Facility File](#ac-enteredit-facility-file)
  - [CDD1 Print Condensed DD--Oncology Patient file](#cdd1-print-condensed-dd-oncology-patient-file)
  - [CDD2 Print Condensed DD-Oncology Primary file](#cdd2-print-condensed-dd-oncology-primary-file)
  - [PSR Purge Suspense Records](#psr-purge-suspense-records)
  - [SP Purge Patient Records with No Suspense/Primaries](#sp-purge-patient-records-with-no-suspenseprimaries)
  - [CS Restage CS Cases](#cs-restage-cs-cases)
  - [TNM Compute Percentage of TNM Forms Completed](#tnm-compute-percentage-of-tnm-forms-completed)
  - [TIME Timeliness Report](#time-timeliness-report)
  - [CHEM Enter/Edit chemotherapeutic Drug File](#chem-enteredit-chemotherapeutic-drug-file)
  - [RCRS Create RCRS Extract](#rcrs-create-rcrs-extract)
  - [TEXT Find Non-Standard characters in TEXT](#text-find-non-standard-characters-in-text)
  - [UPC Update Oncology Physician Contacts](#upc-update-oncology-physician-contacts)
  - [VL Check Validity of TNM Fields](#vl-check-validity-of-tnm-fields)
- [Utility Tools](#utility-tools)
  - [PC Capture Program](#pc-capture-program)
  - [Downloading and Installing Genedits](#downloading-and-installing-genedits)
  - [Line Editor](#line-editor)
  - [Screen Editor](#screen-editor)
  - [Menu Options](#menu-options)
- [Edits within OncoTrax](#edits-within-oncotrax)
- [Edits within Genedits](#edits-within-genedits)
- [Glossary](#glossary)
- [Appendix A: Edits API](#appendix-a-edits-api)
OncoTrax: Cancer Registry is an integrated collection of computer programs and routines, which work together in assisting the Cancer Registrars to create and maintain a cancer patient database. The software creates case listings and registry reports for Cancer Boards (Cancer Conferences), special studies, and the Annual Report recommended by the American College of Surgeons (ACoS).
The software allows the Cancer Registrars to:
1.  Perform case finding.
2.  Identify potential cases to include in your registry, enter the pertinent data directly into the computer system, and maintain patient follow-up information on an annual basis.
3.  Enter abstracts.
4.  Download and transmit data electronically to the VA Central Cancer Registry, state central registries, the National Cancer Database for the ACoS Call for Data.
5.  Produce several reports by using an option in the Utility menu.
> **NOTE:** Several reports within the software provide basic information; however, for more specific reports, you need to know basic FileMan functions. Any and all data collected within an abstract can be pulled back into reports.
6.  Print out by year the number of cases by site, including sex, race, and stages.
7.  Generate follow-up reports as required by the ACoS
> **NOTE:** OncoTrax is in complete compliance with all ACoS required data elements and is updated as changes occur.
OncoTrax is used by cancer registrars and meets all requirements set forth by the American College of Surgeons for approved cancer programs.
> **NOTE:** OncoTrax makes extensive use of Help screens, but it does not replace the use of your reference manuals.
This manual deals with the three most used areas of the software. These are the main functions of registry work used to maintain the cancer registry.
1.  Case Finding/Suspense Module allows you to perform an automated case finding search of relevant hospital databases (pathology, radiology, and patient treatment files) for cases meeting specific criteria for inclusion in the registry.
8.  Abstracting/Printing allows you to enter coded data into the database directly or by utilizing auto-coding techniques. The software is site-specific prompt driven; the only data elements presented are those pertinent to the site you are abstracting.
9.  Follow-Up in OncoTrax assists you in following your patients. The database automatically reminds you when it is time to do a follow-up on a patient. You can update each patient’s record with new follow-up information. The software comes with a variety of follow-up letters, which may be customized to fit the needs of individual facilities.
When using the electronic version of the manual to search for information, click Edit on the menu bar and select Find (binoculars icon). Enter the word or words for which you are looking, and Microsoft Word searches the document.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual is intended for VA registrars using the OncoTrax: Cancer Registry software.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Every cancer registry office should have the following reference material.

> **NOTE:** Use the older editions of the reference materials when entering old cases.

- *Standards For Oncology Registry Entry* (STORE), 2018 and after
- Facility Oncology Registry Data Standards (FORDS), 2016 and after
- *Facility Oncology Registry Data Standards* (FORDS), 2011 and after
- *Registry Operations and Data Standards* (ROADS), prior to 2003 cases
- *Facility Oncology Registry Data Standards* (FORDS), 2003 and after
- *Collaborative Staging Manual and Coding Instructions  
  *Collaborative Staging was added to OncoTrax in July 2004. Use the *Collaborative Staging ManualandCoding Instructions* for all cases diagnosed in 2004 and after.
- *AJCC Cancer Staging Manual, 9<sup>th</sup> Edition* on <u>cervix uteri</u> cancer cases diagnosed beginning January 1, 2021
- *AJCC Cancer Staging Manual, 8<sup>th</sup> Edition* on cancer cases diagnosed beginning January 1, 2018
- *AJCC Cancer Staging Manual, 7<sup>th</sup> Edition* on cancer cases diagnosed beginning January 1, 2010
- *AJCC Cancer Staging Manual*, 6th *Edition* on cancer cases diagnosed beginning January 1, 2003
- *AJCC Cancer Staging Manual*, 5th edition, for entering older cases
- *SEER Summary Staging Manual*, 2000
- *Summary Staging Guide*, 1977
- *SEER Extent of Disease*, 1988; *Codes and Coding Instructions*, 2nd edition, 1994
- *SEER Extent of Disease*, 1998; *Codes and Coding Instructions*, 3rd edition, 1998
- *SEER Program Coding and Staging Manuals* – use current or applicable year
- *SEER\*Rx - Interactive Antineoplastic Drugs Database*  
  The interactive antineoplastic drugs database (helpful when abstracting) is available from SEER on the following website: <http://www.seer.cancer.gov/tools/seerrx/>
- *SEER Self Instructional Manuals for Tumor Registrars*  
  SEER Self-Instructional manuals are available for download on the following website: <http://www.seer.cancer.gov/training/manuals/>
- *ICD-O-3*, International Classification of Diseases for Oncology (ICD-O), 3rd edition
- *ICD-O-2*, International Classification of Diseases for Oncology (ICD-O), 2nd edition
- *Cancer Registry Management Principles and Practice*, 3rd edition

## Recommended Websites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <https://www.cancer.gov/>
- Website for the National Cancer Institute
- <http://www.facs.org/cancer/index.html>
- Home page for the Commission on Cancer, American College of Surgeons, Cancer Programs
- [<u>https://www.facs.org/</u>](https://www.facs.org/)
- Highlights for the month from the Commission on Cancer, American College of Surgeons, Cancer Programs
- <http://web.facs.org>/
- American College of Surgeons, Commission on Cancer: Inquiry and Response System (I & R) Available to all cancer care professionals. It is a repository of thousands of questions and answers related to the Approvals and Accreditation Program, the National Cancer Data Base (NCDB), the American Joint Committee on Cancer (AJCC), and the Facility Oncology Registry Data Standards (FORDS).
- <http://www.ncra-usa.org/>
- Website for the National Cancer Registrars Association
- <https://www.facs.org/quality-programs/cancer-programs/american-joint-committee-on-cancer/cancer-staging-systems/>
- Website for the American Joint Committee on Cancer (AJCC)
- <http://www.naaccr.org/>
- Website for the North American Association of Central Cancer Registries (NAACCR)
- <http://cancerstaging.org/>
- Website for Collaborative Staging
- <http://vaww.medicalsurgical.va.gov/cancer/index.asp>
- All links for the Veterans Health Administration Cancer Program
- [http://www.training.seer.cancer.gov](http://www.training.seer.cancer.gov/)
- SEER’s Training Web Site provides web-based training modules for cancer registration and surveillance. When the site is complete, it will comprise about 30 training modules, each covering a particular cancer registration training subject.
- <http://www.seer.cancer.gov/tools/seerrx/>
- <http://www.cancerstaging.org/>
- Collaborative Staging Manual and Coding Instructions Part I
- http://cancerstaging.org/
- Collaborative Staging Manual and Coding Instructions Part II
- <http://seer.cancer.gov/>
- The SEER Program Code Manual, Third Edition, 1998
- http://seer.cancer.gov/
- SEER Extent of Disease - 1988, Codes and Coding Instructions, Third Edition, January 1998
- <https://www.facs.org/media/whmfnppx/2020_coc_standards.pdf>
- American College of Surgeons Optimal Resources for Cancer Care 2020 Standards
- Facility Oncology Registry Data Standards (FORDS): Revised for 2016

  [<u>https://www.facs.org/quality-programs/cancer/ncdb/call-for-data/fordsmanual</u>](https://www.facs.org/quality-programs/cancer/ncdb/call-for-data/fordsmanual)

## OncoTrax Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must have a working knowledge of VistA conventions, to maneuver easily in OncoTrax. The table contains frequently used characters and their descriptions with examples.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Character</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&lt;ret&gt;</td>
<td><p><strong>&lt;ret&gt;</strong> is the symbol for the Return or Enter key.<br />
Type <strong>&lt;ret&gt;</strong> after every response, or to bypass a prompt or accept a default.</p>
<p><strong>Note:</strong> Do not press it more than necessary; you do not want to bypass an opportunity to enter valuable information.</p></td>
</tr>
<tr class="even">
<td>?</td>
<td><strong>?</strong> (one question mark)<br />
Type <strong>?</strong> at any prompt to view a message explaining the requested information or how to enter it.</td>
</tr>
<tr class="odd">
<td>??</td>
<td><strong>??</strong> (two question marks)<br />
Type <strong>??</strong> at any prompt to view detailed instructions and/or a list of choices.</td>
</tr>
<tr class="even">
<td>//</td>
<td><p><strong>//</strong> (two slash marks)<br />
Type <strong>//</strong> after text for the default response.</p>
<ul>
<li><p>If you accept the default answer, press <strong>&lt;ret&gt;</strong> to continue to the next prompt.</p></li>
<li><p>For a different choice, type the choice and press <strong>&lt;ret&gt;</strong>.</p></li>
<li><p>Press <strong>Enter</strong> at <strong>//</strong> and the word before the slashes becomes the default response.</p></li>
<li><p>Type <strong>?</strong> at // and a list of choices displays.<br />
<strong>Example</strong></p></li>
</ul>
<p>PREVIOUS HISTORY OF CANCER: No// ?</p>
<p>Choose from:</p>
<p>0 No</p>
<p>1 Yes</p>
<p>9 Unknown</p></td>
</tr>
<tr class="odd">
<td>^</td>
<td><p><strong>^</strong> (caret) is Shift + 6 on the keyboard and is also called the up-caret symbol.</p>
<ul>
<li><p>Type ^ to exit an option and return to the menu;</p></li>
<li><p>Type ^ to jump to another field.<br />
<strong>Example<br />
</strong>Type <strong>^ DATE DX</strong> at the field prompt to jump to the <strong>DATE DX</strong> field.</p></li>
</ul>
<p>DATE DX: 04/05/2005//</p>
<p>DX FACILITY: BUFFALO VA MEDICAL CENTER//</p>
<p>PRIMARY SITE: PROSTATE//</p>
<p>TEXT-PRIMARY SITE TITLE: PROSTATE//</p>
<p>LATERALITY: Not a paired site//</p>
<p>HISTOLOGY (ICD-O-3): ADENOCARCINOMA, NOS//</p>
<p>HISTOLOGY CODE: 8140/3</p>
<p>TEXT-HISTOLOGY TITLE: ADENOCARCINOMA, NOS// <strong>^DATE DX</strong></p>
<p>DATE DX: 04/05/2005//</p>
<p>Type a new date after <strong>DATE DX:</strong></p>
<p><strong>In the Abstract</strong></p>
<ul>
<li><p>Go from one field to another in most areas of an abstract<br />
<strong>type ^&lt;field name&gt;</strong></p></li>
<li><p>Go completely out of the abstract<br />
<strong>type ^ without a field name</strong></p></li>
<li><p>Edit a field already completed<br />
<strong>type ^&lt;field name&gt;</strong> to return to the field and then edit.</p></li>
</ul>
<blockquote>
<p><strong>Example</strong></p>
</blockquote>
<p>CLASS OF CASE: 1 Dx here, 1st tx here</p>
<p>FACILITY REFERRED FROM: NONE/ ^CLASS OF CASE</p>
<p>CLASS OF CASE: Dx here, 1st tx here//</p></td>
</tr>
<tr class="even">
<td>@</td>
<td><strong>@</strong> (at symbol) is Shift + 2 on the keyboard.<br />
Type <strong>@</strong> to delete data values stored in fields.</td>
</tr>
<tr class="odd">
<td>…</td>
<td><p><strong>…</strong> (three dots)<br />
Type <strong>…</strong> to <em>replace</em> all data in a field.</p>
<blockquote>
<p><strong>Example</strong></p>
</blockquote>
<p>TX Primary Cancer cannot be assessed Replace … With</p>
<blockquote>
<p>At the <strong>Replace</strong> prompt, type <strong>…</strong> and press <strong>Enter</strong>. When <strong>With</strong> displays, type new data.</p>
<p><strong>Example</strong></p>
</blockquote>
<p>CLINICAL T: T3 Chest wall/diaphragm/mediastinal pleura etc.</p>
<p>Replace ... With</p>
<p>There is a submenu when <strong>...</strong> displays after a menu option.</p>
<blockquote>
<p><strong>Example<br />
</strong>ANN *Annual Reports ...</p>
<p>Select <strong>ANN</strong> and the following displays.</p>
</blockquote>
<p>AAR Annual ACoS Accession Register (80c)</p>
<p>API Annual ACoS Patient Index (132c)</p>
<p>ASL Annual Primary Site/GP Listing (132c)</p>
<p>ACL Annual Patient List by Class of Case (80c)</p>
<p>SST Annual Primary Site/Stage/Tx (132c)</p>
<p>TST Annual ICDO Topography/Stage/Tx (132c)</p>
<p>SDX Annual Status/Site/Dx-Age (132c)</p>
<p>HIS Annual Histology/Site/Topography (80c)</p>
<p>ACT Annual Cross Tabs (80c)</p>
<p>CPR Print Custom Reports</p></td>
</tr>
<tr class="even">
<td>Dates</td>
<td><p>Several date formats are acceptable.<br />
<strong>Examples<br />
</strong>010102, 1-1-02, 1/1/02, 01/01/2002, January 1, 2002</p>
<p>If the year is omitted, the computer uses <strong>Current Year</strong>.</p></td>
</tr>
<tr class="odd">
<td>Device prompt</td>
<td><p>To send a report to a printer, type the name of the printer at the <strong>Device</strong> prompt.</p>
<ul>
<li><p>If the printer is shared, queue your report by entering <strong>Q</strong> at the <strong>Device</strong> prompt and then the name of the printer at the next prompt.</p></li>
<li><p>To view a report on your computer screen, press the <strong>&lt;ret&gt;</strong> key at the <strong>Device</strong> prompt.</p></li>
</ul>
<p>When <em>capturing a file</em>, type 0;269;9999999 at the <strong>Device</strong> prompt.</p>
<p><strong>Note:</strong> When you learn to <em>capture files</em> from the software, you can also learn many ways to display data.</p></td>
</tr>
<tr class="even">
<td>Space bar return</td>
<td><p>Press the <strong>space bar</strong> to re-enter the last selection made at a particular level. (This feature may be limited for some options.)</p>
<p><strong>Example</strong></p>
<ul>
<li><p>At a submenu, the space bar enters the last submenu option accessed.</p></li>
<li><p>At a field, the space bar re-enters whatever was last entered, to any other field within the same option.</p></li>
</ul>
<p><strong>Note:</strong> Press the space bar, and then press the Return key, not both at the same time.</p></td>
</tr>
<tr class="odd">
<td>Report options</td>
<td><p>Report options with <strong>80c</strong> in the name; require an 80-character line printer. Report options with 80c in the name; look correct when viewed on your monitor.</p>
<p>Report options with <strong>132c</strong> in the name; require a 132-character line printer. Reports with 132c in the name do not look correct when viewed on your monitor–the text wraps.</p>
<p><strong>Note:</strong> A printer that can print both <strong>80c</strong> and <strong>132c</strong> is recommended.</p></td>
</tr>
</tbody>
</table>

## OncoTrax Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main OncoTrax menu is the first screen that displays when you sign on to the program. The OncoTrax menu displays the version number of the OncoTrax: Cancer Registry software running on your system.

Example

VVVV VVAA

VVVV VVAAAA

VVVV VVAAAAAA

VVVV VVAA AAAA

VVVV VVAA AAAA

VVVV VVAA AAAA

VVVVVVAA AAAA

VVVVAA AAAAAAAAAAA

VVAA AAAAAAAAAAA

OncoTraX V2.2 Patch 22.v6

SUS \*..Casefinding/Suspense ...

ABS \*..Abstracting/Printing ...

FOL \*..Follow-up Functions ...

LIS \*..Registry Lists ...

ANN \*..Annual Reports ...

STA \*..Statistical Reports ...

UTL \*..Utility Options ...

Select DHCP Tumor Registry \<TEST ACCOUNT\> Option:

- The Select OncoTrax Option: prompt is the starting point for all the modules within the software.
- At the prompt, type in an option/module three-letter abbreviation. The group of related submenu options displays.

> Example

Select OncoTrax Option: SUS \*..Case Finding/Suspense

\*\*\*\*\*\*\*\*\*\*\* Suspense Cases \*\*\*\*\*\*\*\*\*\*\*

CF Automatic Case Finding-Lab Search

LR Print Case Finding-Lab Report

RA Automatic Case Finding-Radiology Search

PT Automatic Case Finding-PTF Search

SE Add/Edit/Delete 'Suspense' Case

SP Print Suspense List by Suspense Date (132c)

NP Patients in Suspense with no primaries

DI Disease Index

## Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before using OncoTrax for the first time, you must define your registry’s parameters.

If OncoTrax is already being used by the registry and you are a new registrar, review the registry’s parameters because you may need to update them.

To access the registry’s parameters:

1.  From the main OncoTrax menu, select UTL \*..Utility Options…
10. From the Utility Options, select TR Define Tumor Registry Parameters

> Example

SUS \*..Case Finding/Suspense ...

ABS \*..Abstracting/Printing ...

FOL \*..Follow-up Functions ...

LIS \*..Registry Lists ...

ANN \*..Annual Reports ...

STA \*..Statistical Reports ...

UTL \*..Utility Options ...

Select OncoTrax Option:

UTL \*..Utility Options…

\*\*\*\*\*\*\*\*\*\*\*\*\*UTILITY OPTIONS\*\*\*\*\*\*\*\*\*\*\*\*\*

RS Registry Summary Reports

DP Delete Oncology Patient

DS Delete Primary Site/GP Record

SQ Find Duplicate Acc/Seq Numbers

EA Edit Site/AccSeq# Data

LG List Topographic Site Groups

LT List Topography Codes by Site Group

AR Create a report to preview ACoS output

CT Create ACoS Data Download

SR Create a report to preview State/VACCR output

CC Create State Data Download

TR Define Tumor Registry Parameters

AC Enter/Edit Facility file

CDD1 Print Condensed DD--Oncology Patient file

CDD2 Print Condensed DD--Oncology Primary file

PSR Purge Suspense Records

SP Purge Patient Records with No Suspense/Primaries

CS Restage CS cases using latest version

TNM Compute percentage of TNM forms completed

TIME Timeliness Report

CHEM Enter/Edit Chemotherapeutic Drugs file

RCRS Create RCRS extract RQRS Create RQRS extract

TEXT Find non-standard characters in TEXT

UPC Update Oncology Physician Contacts

VL Check Validity of TNM Field Values

## Define Tumor Registry Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use Define Tumor Registry Parameters to update/change parameters, such as the name of the Tumor Registrar.

You are required to put in information for the following fields.

Select ONCOLOGY SITE PARAMETERS HOSPITAL NAME:

HOSPITAL NAME: Type the name of your medical center as you want it to display.

STREET ADDRESS: Type the street address of your medical center.

ZIP CODE: Type the zip code for your medical center.

REFERENCE DATE: Type the year: f*irst* day of the *first* month of the year the registry *first* starts capturing data. Reference date cannot be later than 1/1/2009.

COC ACCREDITATION DATE: Enter the date of COC accreditation, otherwise leave blank.

TUMOR REGISTRAR: Type the name of the cancer registrar (3 - 30 characters in length) as you want it to display on letters and reports.

PHONE NUMBER: Type the phone number of the cancer registrar's office.

STATE HOSPITAL \#: Type the number assigned by the state to your medical center.

FACILITY ID \#: Type the registry number assigned by the American College of Surgeons. Use the ID to define the registry in the ACoS Call for Data.

CENTRAL REGISTRY \#: Type the registry number assigned by the state central registry, where applicable.

> **NOTE:** This field may be left blank.

VISN: Type the Veterans Integrated Service Network number.

CS URL: Type the URL address for the Collaborative Staging computer algorithms: <http://10.41.100.27:86/cgi_bin/oncsrv.exe>

> **NOTE:** Copy and paste the address, so as not to make a mistake when typing.

DIVISION: Type in your division or site number. It is a required field, even for a single division site.

> **NOTE:** Case finding does not work when Division is blank; type in the name of the hospital or the division.

COC ACCREDITATION: Type 00 (Not accredited) or 01 (Coc Accredited)

COC ACCREDITATION TEXT.: Enter any information regarding history of accreditation (example: when lost accreditation and/or regained accreditation).

Select AFFILIATED DIVISION: Type the name of the division that is associated with the primary division for purposes of the tumor registry.

- If you are not an integrated site, bypass the Define Tumor Registry Parameters prompt by pressing \<RET\>.
- If you are an integrated site and each site/division manages its own tumor registry, bypass the Define Tumor Registry Parameters prompt by pressing \<RET\>.
- If you are an integrated site and one or more sites/divisions do not have a tumor registry and you are responsible for tracking patients from one or more of those sites in your tumor registry, type the name of each in Select AFFILIATED DIVISION.

Select QA USER: Type the name of the tumor registrar.

> Example

> REFERENCE DATE: ??

1.  Record the reference date for the registry. This date is listed as the first day of the first month of the year the registry first starts keeping data.
2.  Enter the date in format: 010106.

# SUS Case Finding and Suspense Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SUS Case Finding and Suspense module provides a way to automatically find eligible cases or manually add the patients to Suspense.

Case finding is a systematic method of locating all eligible cases to enter (accession for abstracting) into your database. One of the unique features of the OncoTrax software is Automatic Case Finding. Enter a range, start date, and end date, and the computer searches pathology (CF), radiology (RA) and the Patient Treatment File (PT) for eligible cases in that date range. Each search is run separately according to your input. Cases meeting the defined criteria are captured electronically and added to Suspense.

The Suspense Date field, the cases are held in Suspense until they are accessioned for abstracting or manually deleted.

- After reviewing the Suspense cases, you may find some that are not required in the registry. You can manually delete them; refer to [Deleting a VA Patient from Suspense](#deleting-a-va-patient-from-suspense), page [16](#deleting-a-va-patient-from-suspense).
- You may find some cases that are recurrences of an already documented primary. Recurrences of analytic cases require a follow up. The recurrences must be updated using [RF Recurrence/Sub Tx Follow-up](#rf-recurrencesub-tx-follow-up), page [29](#rf-recurrencesub-tx-follow-up) in the Follow-up Module. Update the follow-up using [PF Post/Edit Follow-up](#pf-postedit-follow-up), page [28](#pf-postedit-follow-up).
- Cases that are accessioned are automatically deleted from Suspense.

Case Finding/Suspense Menu

CF Automatic Case Finding-Lab Search

LR Print Case Finding-Lab Report

RA Automatic Case Finding-Radiology Search

PT Automatic Case Finding-PTF Search

SE Add/Edit/Delete from Suspense

SP Print Suspense List by Suspense Date (132c)

NP Patients in Suspense with no primaries

DI Disease Index

> **NOTE:** For your date range, run CF, RA, and PT only once. If you repeat the search for your date range, cases already reviewed end up in your Suspense file.

## CF Automatic Case Finding - Lab Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to search the Lab files to build a Suspense list of cases. When the search is complete, you can print the Suspense list on a selected device/printer.

Start with Date: .

Go to Date: Type the end date of the search, such as 1/31/04  
If the year is omitted, the computer uses Current Year.

Device: Type the name of your printer.

\*\*\*\*\*\*\*\*\*\*\*\* LAB CASE FINDING \*\*\*\*\*\*\*\*\*\*\*\*

This option will search the LAB DATA file  
for cases to add to the Suspense List.

Start Date: Type the begin date of the search.  
If this option was used previously, the previous end date is the begin date, such as JUL 1, 2005

End Date: JUL 31, 2005

Dates OK? Y//  
Press Enter.

> **NOTE:** The option searches for ICD-O morphology codes 800-998, excluding Behavior Code /0 (Benign) codes.

Exceptions to the search criteria:

> Benign Cancers of the central nervous system will be included.

> Squamous cell neoplasms (805-808) of the skin will be excluded.

> Basal cell neoplasms (809) will be excluded.

DEVICE: HOME//

Your report shows the total number of patients identified.

Example

CASE FINDING LIST your hospital VAMC 03/10/2004

Patient Name PtID# Lab Test Organ/Tissue Morph/Disease-SNOMED

SUSPENSE DATE: 7-5-2005

ONCOPATIENT1 O9999 07/15/2005-SP LUNG, UPPER 80703-SQUAMOUS CELL

## LR Print Case Finding - Lab Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to generate a list of patients from Suspense, identified in Pathology with reportable malignancies in the CF Automatic Case Finding - Lab Search. You can print all lab cases in Suspense by entering \<ret\> at the start date prompt or print only those cases within a specified date range.

Start with Suspense Date: First//: Type the begin date for the search or press Enter to print all cases.

Go to Suspense Date Last: Type the end date for the search or press the \<ret\> key to accept the last date available.

Device: Type the name of your printer.

  
Example

Select \*..Case finding/Suspense Option: lr Print Case finding-Lab Report

START WITH SUSPENSE DATE: FIRST//

DEVICE: UCX REMOTE TCPIP

---------------------------------------------------------------------------  
CASE FINDING LIST WASHINGTON DC VAMC 03/10/2004

Patient Name PtID# Lab Test Organ/Tissue CODE-Morphology

---------------------------------------------------------------------------SOURCE: CYTOPATHOLOGY

ONCOPATIENT1 L9999 07/08/2005-CY BRONCHIAL WAS 69760-USPICIOUS

SOURCE: SURGICAL PATHOLOGY

ONCOPATIENT2 N9999 07/10/2005-SP SKIN OF UPPER 87203-MELANOMA,NOS

Last Contact: 04/03/1998

Acc/Sequence Primary Site Last Cancer Status Date DX Status

------------ ---------------- ------------------- -------- -----

1998-00139/00 SKIN, FACE NOS Unknown 04/03/1998 Complete

> **NOTE:** Patient N999 has a primary from 1998; so that information also displays. When the patient has a history of malignancy, you must verify whether this new finding is a recurrence or a new primary.

## RA Automatic Case Finding - Radiology Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to search the Rad/Nuc Med (Radiology/Nuclear Medicine) Patient file for suspicious malignancies and add the cases to your Suspense list in the Oncology Patient file.

Select Start Date: Type the begin date for the search or use the default date.

Select Ending Date: Type the end date for the search.

Device: Type the name of your printer.

-----------------------------------------------------------------------

-----------------------------------------------------------------------RADIOLOGY CASE FINDING LIST WASHINGTON DC VAMC 07/18/2005

Patient Name PtID# Exam Date Procedure

-----------------------------------------------------------------------ONCOPATIENT1 B1111 07/18/2005 CT THORAX W/O CONTRAST

ONCOPATIENT2 D9999 07/18/2005 ULTRASOUND ABDOMEN LTD

> **NOTE:** This option only yields results if Radiology is entering internal Code 8 or Code 9, not an ICD-9 Code for Radiology. Many patients identified through these options may not actually have cancer., page [16](#deleting-a-va-patient-from-suspense).

## PT Automatic Case Finding - PTF Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to search the PTF (Patient Treatment File) and add the cases to your Suspense list in the Oncology Patient file. After you enter the dates for your search, the program lists the codes to capture during this search.

> **NOTE:** Suspense date = Admission day +1.

Select Start Date: Type the begin date for the search or use the default date.

Select Ending Date: Type the end date for the search.

Device: Type the name of your printer.

Example

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* PTF CASEFINDING \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This option will search the PRINCIPLE DIAGNOSIS and

SECONDARY DIAGNOSIS fields of the PTF file for ICD

codes which identify cases to be added to the Suspense

list.

Start Date: 02-02-2022// 1/1/2022 JAN 01, 2022

End Date: T FEB 02, 2022

Dates OK? Y// ES

The following ICD codes will be searched for:

140-239 NEOPLASMS

(excluding benign neoplasms 210-229 unless listed below)

042.2 HIV WITH SPECIFIED MALIGNANT NEOPLASMS

225.0-225.9 BENIGN NEOPLASMS OF BRAIN AND OTHER PARTS OF NERVOUS SYSTEM

227.3 BENIGN NEOPLASM OF PITUITARY GLAND AND CRANIOPHARYNGEAL DUCT

227.4 BENIGN NEOPLASM OF PINEAL GLAND

228.02 HEMANGIOMA INTRACRANIAL

259.2 CARCINOID SYNDROME

273.1-273.9 DISORDERS OF PLASMA PROTEIN METABOLISM

284.9 ANAPLASTIC ANEMIA, UNSPECIFIED

285.0 SIDEROBLASTIC ANEMIA

288.3 EOSINOPHILIA

288.4 HEMOPHAGOCYTIC SYNDROMES

289.6 FAMILIAL POLYCYTHEMIA

289.8 OTHER SPECIFIED DISEASES OF BLOOD AND BLOOD-FORMING ORGANS

289.83 MYELOFIBROSIS

795.06 PAPANICOLAOU SMEAR OF CERVIX WITH CYTOLOGIC EVIDENCE OF

MALIGNANCY

795.16 PAP SMR VAG-CYTOL MALIG

796.76 PAP SMR ANUS-CYTOL MALIG

V07.3 NEED FOR OTHER PROPHYLACTIC CHEMOTHERAPY

V07.8 NEED FOR OTHER SPECIFIED PROPHYLACTIC MEASURE

V10.00-V10.09 GASTROINTESINAL TRACT

V12.41 PERS HX BENIGN NEOPL OF BRAIN

V58.0 ENCOUNTER FOR RADIOTHERAPY

V58.1 ENCOUNTER FOR CHEMOTHERAPY

V58.11 ANTINEOPLASTIC CHEMO ENC

V58.12 IMMUNOTHERAPY ENCOUNTER

V66.1-V66.2 CONVALESCENCE FOLLOWING RADIOTHERAPY/CHEMOTHERAPY

V67.1-V67.2 FOLLOW-UP EXAMINATION FOLLOWING RADIOTHERAPY/CHEMOTHERAPY

V71.1 OBSV-SUSPCT MAL NEOPLASM

V76.0-V76.9 SPECIAL SCREENING FOR MALIGNANT NEOPLASMS

\*\*\* COMPREHENSIVE ICD-10-CM Casefinding Code List for Reportable Tumors \*\*\*

(C00.\_ to C43.\_),C4A.\_,(C45.\_ to C48.\_),C49.\_ to C96.\_)

Malignant neoplasms (excluding category C44), stated or presumed

to be primary (of specified site) and certain specified histologies

C44.00\_, C44.09 Unspecified/other malignant neoplasm of skin of lip

C44.10\_, C44.19\_ Unspecified/other malignant neoplasm of skin of eyelid

C44.13\_ Sebaceous cell carcinoma of skin of eyelid, including canthus

C44.20\_, C44.29\_ Unspecified/other malignant neoplasm skin of ear and

external auricular canal

C44.30\_, C44.39\_ Unspecified/other malignant neoplasm of skin of

other/unspecified parts of face

C44.40\_, C44.49 Unspecified/other malignant neoplasm of skin of

scalp & neck

C44.50\_, C44.59\_ Unspecified/other malignant neoplasm of skin of trunk

C44.60\_, C44.69\_ Unspecified/other malignant neoplasm of skin of upper

limb, incl. shoulder

C44.70\_, C44.79\_ Unspecified/other malignant neoplasm of skin of lower

limb, including hip

C44.80\_, C44.89 Unspecified/other malignant neoplasm of skin of

overlapping sites of skin

C44.90\_, C44.99 Unspecified/other malignant neoplasm of skin of

unspecified sites of skin

C49.A\_ Gastrointestinal stromal tumors...

(D00.\_ to D05.\_), (D07.\_ to D09.\_) In-situ neoplasms (Note: Carcinoma in situ of the cervix

(C/N III-8077/2) and Prostatic Intraepithelial Carcinoma

(PIN III-8148/2) are not reportable).

D18.02 Hemangioma of intracranial structures and any site

D32.\_ Benign neoplasm of meninges (cerebral, spinal and unspecified)

D33.\_ Benign neoplasm of brain and other parts of central nervous

system

(D35.2 to D35.4) Benign neoplasm of pituitary gland, craniopharyngeal

duct and pineal gland

D42.\_, D43.\_ Neoplasm of uncertain or unknown behavior of meninges, brain, CNS

(D44.3 to D44.5) Neoplasm of uncertain or unknown behavior of pituitary

gland, craniopharyngeal duct and pineal gland

D45 Polycythemia vera (9950/3)

D46.\_ Myelodysplastic syndromes (9980, 9982, 9983, 9985, 9986, 9989, 9991, 9992)

D47.02 Systemic mastocytosis

D47.1 Chronic myeloproliferative disease (9963/3)

D47.3 Essential (hemorrhagic) thrombocythemia (9962/3)

D47.4 Osteomyelofibrosis (9961/3)

Includes: Chronic idiopathic myelofibrosis

Myelofibrosis (idiopathic) (with myeloid metaplasia)

Myesclerosis (megakaryocytic) with myeloid metaplasia)

Secondary myelofibrosis in myeloproliferative disease)

D47.9 Neoplasms of uncertain behavior of lymphoid, hematopoitec and related tissue, unspecified (9970/1,9931/3)

D47.Z\_ Neoplasm of uncertain behavior of lymphoid, hematopoietic

and related tissue, unspecified (9960/3,9970/1,9971/3, 9931/3)

D49.6, D49.7 Neoplasm of unspecified behavior of brain, endocrine glands and other CNS

D72.11\_ Hypereosonophilic syndrome (HES\] (9964/3)

K31.A22 Gastric intestinal metaplasia with high grade dysplasia

N85.02 Endometrial intaepithelial neoplasia (EIN)

R85.614 Cytologic evidence of malignacy on smear of anus

R87.614 Cytologic evidence of malignacy on smear of cervix

R86.624 Cytologic evidence of malignacy on smear of vagina

R90.0 Intracranial space-occupying lesion found on diagnostic imaging of central nervous system

DEVICE: HOME//Note: These are the codes searched for and added to your Suspense file.

(Eliminating BENIGN 209.0-229.9)

---------------------------------------------------------------------------PTF-CASE FINDING LIST WASHINGTON DC VAMC 03/10/2004

Patient Name PtID# Admit – Disch Level/ICD9-Description

---------------------------------------------------------------------------

ONCOPATIENT1 A9999 02/03/2004-02/04/2004 ICD-6/0-HX-PROSTATIC MALIGNA

ONCOPATIENT2 G9999 02/06/2004-02/06/2004 ICD-8/0-HX OF BLADDER MALIGN

PTF CASE FINDING RESULTS

38 Cases found

2 New Patients added

2 New cases added

> **NOTE:** Although there were 38 cases found during this time period, only 2 of the 38 were not already in Suspense.

## SE Add/Edit/Delete from Suspense 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to manually add patients to the Suspense file, to modify patient information in the file, or to manually delete patients from Suspense.

### Adding a VA Patient to Suspense

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enter a patient in the Suspense file:

1.  Type the patient PID#; refer to the *Glossary* on page [66](#glossary).
11. The program asks: do you want to add the patient as a New OncoTrax Patient?  
    Response is YES.
12. At the Suspense Date: prompt, type the provisional date of the diagnosis. You can edit the date when the abstract is complete.

> **NOTE:** You must enter a date

### Editing a VA Patient in Suspense

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To modify patient information in the Suspense file:

1.  Type the patient PID#; refer to the *Glossary* on page [66](#glossary).
13. At the Suspense Date: prompt, change the date.

### Deleting a VA Patient from Suspense

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove a patient from the Suspense file:

1.  Type the patient PID#; refer to the *Glossary* on page [66](#glossary).
2.  Press @ (shift + 2) to delete the patient.

Example

Select ONCOTRAX PATIENT NAME: 19999

Searching for a VA Patient, (pointed-to by NAME)

ONCOPATIENT1 12-21-99 999999999 NO NSC VETERAN

Enrollment Priority: GROUP 8c Category: ENROLLED End Date:

...OK? Yes// (Yes)

Patient Name: ONCOPATIENT

Date of Last Contact or Death:

Vital Status:

Follow-Up Status:

SUSPENSE DATE: FEB 10,2004// @

SURE YOU WANT TO DELETE THE ENTIRE SUSPENSE DATE? y (Yes)

This patient is not on suspense and has no primaries.  
This patient's record has been deleted.

## SP Print Suspense List by Suspense Date (132c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to print a list of patients currently in Suspense by the suspense date. The printout lists patients according to how they are identified; first by the source (through Surgical Pathology, Cytopathology, Electron Microscopy, Autopsy, PTF, Radiology, or manual entry) and then in the order of the suspense date. The printout lists the patient's name, the patient's SSN or identifier, Organ/Tissue, Lab Morphology, and Suspense, Admission and Discharge Dates.

> **NOTE:** 132c (132 columns) does not present an easy-to-read display on the computer screen because the text wraps; select a device that can print 132 columns.

Start with Suspense Date: FIRST//: Press the \<ret\> key to accept FIRST. All the cases with suspense dates display.  
or type a date for a Go to Suspense Date prompt.

Go to Suspense Date: Type the end date of the range for the printout.

Example

START WITH SUSPENSE DATE: FIRST//

Patient Name SSN Organ/Tissue Lab Morphology Suspense Dt Admission Discharge

SOURCE: SURGICAL PATHOLOGY

ONCOPATIENT1 999-99-9999 LOBE OF LUNG LIGNANT MELANOMA JAN 6,2006 JAN 6,2006 JAN 10,2006

ONCOPATIENT2 999-99-9999 SIGMOID COLON ENOCARCINOMA,MODERATEL JAN 6,2006 JAN 6,2006 JAN 10,2006

## NP Patients in Suspense with No Primaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints a list of OncoTrax patients that are in Suspense, but do not have a primary.

Example

ONCOTRAX PATIENT ONLY

Patient Name SSN Suspense Last Admit Last Disch

--------------------------------------------------------------------ONCOPATIENT1 999-99-9999 FEB 3, 2004 03/07/2004 03/09/2004

ONCOPATIENT2 999-99-9999 FEB 2, 2004 01/30/2004 02/04/2004

# DI Disease Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to START WITH/GO TO a VISIT range and START WITH/GO TO a POV range. The output is sorted by PATIENT NAME.

Select DISEASE INDEX report: ??

Select 'Casefinding' if you want to find and add to SUSPENSE

cases with reportable tumors for the selected date range.

Select 'Customized search' if you want to search for an

individual ICD-CM code or range of codes.

Select one of the following:

1 Casefinding

2 Customized search

Select DISEASE INDEX report: 1 Casefinding

\* Previous selection: VISIT from 2020 to 2022@24:00

Start with VISIT: 2020// (2020)

Go to VISIT: 2022// (2022)

DEVICE:  
ABS Abstract Entry and Printing Module

The Abstract Entry and Printing module is used for abstracting cases. An abstract is a summary of pertinent information about the patient, the cancer, the treatment, and the outcome. Components include patient demographic information, cancer identification, extent of disease, stage at diagnosis, first course of treatment, recurrence, and subsequent therapies or progression and follow-up.

- An abstract must be completed for all cases that meet the criteria for inclusion in the registry.  
  (The standards are set forth by the American College of Surgeons and VACRS reportable lists.)
- If a patient has multiple primary malignancies, an abstract must be prepared for each additional primary.
- An abstract must be completed within six months from the date of first contact.

Abstract Entry/Print Menu

\*\*\*\*\*\*\*\*\*\*\*\*\*\* ABSTRACT ENTRY/PRINT \*\*\*\*\*\*\*\*\*\*\*\*\*\*

AI Complete Abstract

EE Abstract Edit Primary

NC Print Abstract NOT Complete List

IR Patient Summary

QA Print Abstract QA (80c)

EX Print Abstract-Extended (80c)

PA Print Complete Abstract (132c)

MA Print QA/Multiple Abstracts

AS Abstract Screens Menu (80c) ...

## AI Complete Abstract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** To complete an abstract, you need the appropriate COC manual based on diagnosis year. For 2018+ cases, use the Standards for Oncology Registry Entry (STORE) manual.

The Complete Abstract option is the main entry point for abstracting new cases or editing existing abstracted cases.

OncoTrax is prompt driven. Once a specific Topography Code is selected, all successive prompts displayed are specific. Some of the data captured in the case finding and suspense process, as well as demographic data, are automatically transferred and inserted into the appropriate fields within the abstract; however, you can edit the data if necessary.

> **NOTE:** The OncoTrax Conventions on page 4 are helpful in maneuvering around an abstract.

### Abstracting a Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You begin an abstract by searching for the patient to determine if the patient is new to the VA.

If you do not enter data in all required fields, you cannot change the status of the abstract to Complete (3).

#### Adding a New Patient

1.  At the prompt, type the patient PID#; refer to the *Glossary* on page [66](#glossary).
2.  Respond YES to the prompt: Are you adding 'LAST,FIRST' as a new ONCOTRAX PATIENT (the 24673RD)? No//

Example:

Enter patient name: h9999

     Searching for a VA Patient, (pointed-to by NAME)

     Searching for a Non-VA or Ambiguous Patient, (pointed-to by NAME)

     Searching for a VA Patient

   1 H9999 LAST,FIRST \*SENSITIVE\* \*SENSITIVE\* NO EMPLOYEE       

   2 H9999 LAST,FIRST1 7-1-15 999999999 NO COLLATERAL SY/ 

   3 H0000 LAST,FIRST2 11-1-58 000000000 NO NON-VET(OTHER) SY/ 

   4 H9999 LAST,FIRST3 10-1-48 999009999 YES SC VETERAN  

   5 H0000 LAST,FIRST4 6-1-22 000990000 NO NSC VETERAN    

  

ENTER '^' TO STOP, OR

CHOOSE 1-5: 1  LAST,FIRST \*SENSITIVE\* \*SENSITIVE\* NO  EMPLOYEE       

        ...OK? Yes//   (Yes)

  Are you adding 'LAST,FIRST' as

    a new ONCOTRAX PATIENT (the 24673RD)? No// y  (Yes)

      The following information is contained in the Patient file

            NOT editable - See your MAS department IF in error

                    Name: LAST,FIRST

DOB:  DEC 1, 1953             Address: 1111 THIRD AVENUE

SSN:  999-00-9999                       Washington DC 20422

SEX:  Female

POB:  Not Stated                        888-8888, EXT. 1111

                         NOK:

          \*\*\*\*\*\*\*\*\*\*\*\*\* OncoTrax Patient file DATA \*\*\*\*\*\*\*\*\*\*\*\*\*\*

    Place of birth.............: UNKNOWN

    Race 1.....................:

    Race 2.....................:

    Race 3.....................:

    Race 4.....................:

    Race 5.....................:

    Spanish origin.............:

    Sex........................: FEMALE

    Agent Orange exposure......:

    Ionizing radiation exposure:

    Chemical exposure..........:

    Asbestos exposure..........:

Vietnam service............:

Lebanon service............:

Grenada service............:

Panama service.............:

Persian Gulf service.......:

Somalia service............:

Yugoslavia service.........:

Afghanistan (OEF) service..:

Iraq (OIF) service.........:

Edit patient data? YES//

    Continue with Patient History? Yes// n  NO

    Register a Primary for this patient? Yes//   YES

#### Editing an Existing Patient

1.  Respond NO to the prompt: Are you adding 'LAST,FIRST' as a new ONCOTRAX PATIENT (the 24673RD)? No//
2.  At the prompt: Edit patient data? YES// y  YES
3.  Type in the patient’s remaining demographic information.  
    Some information is automatically imported from the patient’s electronic record; and some information is taken from the patient’s chart

> Example

Edit patient data? YES// y YES

> **NOTE:** Answer No to Edit patient data?, if you are not going to complete this section now; such as when accessioning a patient to remove from Suspense.

PLACE OF BIRTH: New York//

RACE 1: White//

RACE 2: NA//

RACE 3: NA

RACE 4: NA

RACE 5: NA

SPANISH ORIGIN: Non-Spanish, non-Hispanic

SEX: Male//

> **NOTE:** These fields are automatically brought into the abstract from information in the patient’s electronic record. Enter 99 for Unknown.

AGENT ORANGE EXPOSURE : No//

IONIZING RADIATION EXPOSURE: No//

CHEMICAL EXPOSURE:

ASBESTOS EXPOSURE:

> **NOTE:** These two fields are not automatically populated. This information is found in the patient’s chart. Leave no blanks.

PERSIAN GULF SERVICE: No//

MIDDLE EAST SERVICE: No//

SOMALIA SERVICE: No//

Would you like to see a PROBLEM LIST for this patient to assist

you in entering the COMORBIDITY/COMPLICATION \#1-6 prompts? Yes// YES

> **NOTE:** All problems from the cover sheet display. Select ICD-9 codes as required by ACoS.

DATE OF ONSET ICD DIAGNOSIS

------------- --------- --------------------------------------------

2003 266.2 B-COMPLEX DEFIC NEC

2003 110.4 DERMATOPHYTOSIS OF FOOT

2001 401.9 HYPERTENSION NOS

UNKNOWN 780.79 OTHER MALAISE AND FATIGUE

UNKNOWN 110.1 DERMATOPHYTOSIS OF NAIL

UNKNOWN 414.9 CHR ISCHEMIC HRT DIS NOS

SOURCE COMORBIDITY: Facility face sheet//

COMORBIDITY/COMPLICATION \#1:

//

COMORBIDITY/COMPLICATION \#2:

COMORBIDITY/COMPLICATION \#3:

COMORBIDITY/COMPLICATION \#4:

COMORBIDITY/COMPLICATION \#5:

COMORBIDITY/COMPLICATION \#6:

COMORBIDITY/COMPLICATION \#7:

COMORBIDITY/COMPLICATION \#8:

COMORBIDITY/COMPLICATION \#9:

COMORBIDITY/COMPLICATION \#10:

Enter RETURN to continue or '^' to exit: ??

Patient name:

Secondary Diagnosis \#1.:

Secondary Diagnosis \#2.:

Secondary Diagnosis \#3.:

Secondary Diagnosis \#4.:

Secondary Diagnosis \#5.:

Secondary Diagnosis \#6.:

Secondary Diagnosis \#7.:

Secondary Diagnosis \#8.:

Secondary Diagnosis \#9.:

Secondary Diagnosis \#10.:

Would you like to edit the SECONDARY DIAGNOSIS \#1-10 prompts? No//

\*SECONDARY DIAGNOSIS \#1-10 refers to future ICD-10 diagnostic coding. Record as required by ACoS. LEAVE blank prior to ICD-10 implementation

14. A registrar often finds that a patient’s occupation is not in the list. When ?? (two question marks) display after the occupation, it means the occupation is not in the list. You can add an occupation.

> Continue with Patient History? Yes// YES

> Select USUAL OCCUPATION: DOG TRAINER ??

1.  Type an existing occupation.
2.  When it is echoed back, type in the new occupation.
3.  At the prompt: Are you adding DOG TRAINER as a new ……., type YES with the suggested SNOMED code.

Example:

> Select USUAL OCCUPATION: TEACHER IN EDUCATION (THIRD LEVEL)

> USUAL OCCUPATION...........: TEACHER IN AGRICULTURAL SCIENCE (THIRD LEVEL) // DOG TRAINER

#### Entering a First Primary for a Patient

1.  Press Enter at the prompt default.

Register a Primary for this patient? Yes//

Select (first) Primary 'SITE/GP':

15. At the prompt, Primary 'SITE/GP': type the site group name or the ICDO Topography code (C code).  
    The case is assigned to the appropriate group and all subsequent fields display only the information relating to the selected site.

\*\*\*\*\*\*\*\* CREATE FIRST PRIMARY RECORD FOR THIS PATIENT\*\*\*\*\*\*\*

     PATIENT: LAST,FIRST

     Select first Primary SITE/GP: BREAST 

     Ok to ADD:? Yes//   YES

     Creating a new Primary record for LAST,FIRST

     ACCESSION YEAR:  2007//

    

ACCESSION NUMBER: 200700224//

SEQUENCE NUMBER: 00//

CLASS OF CASE: 12 Dx by staff physician AND all tx at reporting facility

DATE OF FIRST CONTACT: T (AUG 31, 2022)

DATE DX: T (AUG 31, 2022)

PRIMARY SITE: KIDNEY NOS C64.9

CASEFINDING SOURCE: 10 Reporting Hospital, NOS

 LAST,FIRST                                                       BREAST

 999-00-9999                                                                   

--------------------------------------------------------------------------

                         Primary Menu Options

--------------------------------------------------------------------------

                      1. Patient Identification
                      2. Cancer Identification
                      3. Stage of Disease at Diagnosis

                         Collaborative Staging (2004+ cases)
                      4. First Course of Treatment
                     5. Performance Measures

6\. Over-ride Flags

7\. Case Administration

8\. EDIT Modifiers

9\. User-Defined Fields

                      A  All - Complete Abstract

                         Enter option: All//

--------------------------------------------------------------------------

 LAST,FIRST          Patient Identification BREAST 999-00-9999       

--------------------------------------------------------------------------

 Reporting Hospital...........:

 Marital status at Dx.........: MARRIED/COMMON LAW

 Patient address at Dx........: 1111 FIRST AVENUE

16. A new primary record is created for this patient and you are prompted for:

> Accession Year: Type the year the case was added to the registry.

> **NOTE:** The current year is the default, but you can type in any year.

> Accession No.: Press Enter to accept the accession number.

> **NOTE:** The next available accession number for the accession year displays.

> Sequence No.: If this is the first primary for the patient, press Enter to accept the sequence number 00.

If this is not the first primary for the patient, all the primaries for the patient are listed, and you can edit any of the primaries or add another.  
If the sequence number is not correct, such as when a patient had a previous cancer diagnosis and was treated elsewhere, type 02.

#### Editing a New or an Existing Primary

1.  Type a new primary SITE/GP.  
    The program takes you to the body of the abstract.

E EDIT existing Primary

A ADD another Primary

F Follow-Up

Q Quit Patient

EDIT/ADD primary for this patient: Edit//

17. Select A to edit all the information or select the portion of the abstract you want to edit.

--------------------------------------------------------------------------Primary Sub-menu Options

--------------------------------------------------------------------------

1\. Patient Identification

2\. Cancer Identification

3\. Stage of Disease at Diagnosis

4\. First Course of Treatment

5\. Patient Care Evaluation

A All - Complete Abstract

> **NOTE:** If you only want to edit one section of the abstract, select that number.

#### Adding a Second Primary

1.  Select AI, the Abstract/Printing option.

Select \*..Abstracting/Printing Option: AI Complete Abstract

Enter patient name: LAST, FIRST

Place of birth.............: NEW YORK

Race 1.....................: WHITE

Race 2.....................: NA

Race 3.....................: NA

Race 4.....................: NA

Race 5.....................: NA

Spanish origin.............: NON-SPANISH, NON-HISPANIC

Sex........................: MALE

Agent Orange exposure......: NO

Ionizing radiation exposure: NO

Chemical exposure..........: UNKNOWN

Asbestos exposure..........: UNKNOWN

Persian Gulf service.......: NO

Middle East service........: NO

Somalia service............: NO

Comorbidity/Complication \#1: 401.9 HYPERTENSION NOS

Comorbidity/Complication \#2: 724.2 LUMBAGO

Comorbidity/Complication \#3:

Comorbidity/complication \#4:

Comorbidity/Complication \#5:

Comorbidity/Complication \#6:

> **NOTE:** The personal information entered for the first primary displays and you can edit it or accept it as it is.

Edit patient data? YES// NO

Continue with Patient History? Yes// NO

Acc/Sequence Primary Site Last Cancer Status Date DX Status

------------- ------------- ------------------ --------- ---------

2004-00898/00 BONE MARROW Evidence this CA 06/23/2004 Complete

Select one of the following:

E EDIT existing Primary

A ADD another Primary

F Follow-Up

Q Quit Patient

18. To add another primary for the patient select ADD another Primary.

EDIT/ADD primary for this patient: Edit// ADD another Primary

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* ADD PRIMARY \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

LAST, FIRST

ACCESSION NUMBER: 2004-00898

SEQUENCE NUMBER: 02//

> **NOTE:** The sequence number is updated. The first sequence number is changed from 00 to 01 and the additional one is 02.

19. Type the site or topography code and press Enter.

Select another Primary 'SITE/GP': LUNG NOS

20. Continue following the prompts.

### Completing an Abstract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you finish an abstract, you must change the abstract status to Complete (3).

OncoTrax reviews all mandatory fields and if any are not filled in, you are unable to code the abstract status as Complete. When an abstract is not complete and you have a large amount of data, you can change the status to partial or minimal.

An incomplete abstract generates a list of empty required fields. Go back into the abstract and fill in the empty required fields–leave no blanks.

In Abstract Status, you decide when to call an *incomplete* abstract. To change the status, type the number, the first letter, or the entire word.

> **NOTE:** You cannot set the abstract to Complete, if any of the required fields are left blank.

Example

ABSTRACT STATUS

ABSTRACT STATUS: Incomplete// ?

Choose from:

0 Incomplete

1 Minimal data

2 Partial

3 Complete

ABSTRACT STATUS: Incomplete// c Complete??

Abstract Status may not be set to COMPLETE unless

ALL REQUIRED DATA FIELDS HAVE BEEN ENTERED.

The following REQUIRED fields have not been entered for this primary:

ALCOHOL HISTORY

DATE OF SURGICAL DISCHARGE

DATE RADIATION STARTED

DIAGNOSTIC CONFIRMATION

EXTENSION

> **NOTE:** Alcohol History, Tobacco History, Family History, and Occupation Information are considered patient demographic fields.  
You *cannot*^ from these fields back to the patient . You must exit out of the abstract and go back into AI.  
You *can*^ to any primary field, such as Date of Surgical Discharge, Date Radiation Started, Diagnostic Confirmation, and Extension , and so on. Example: ^Date of Surgical Discharge.

ABSTRACT STATUS = Complete will also perform a checksum of the values and an API call-up to the current EDITS metafile. An EDITS report will generate containing any inter-field edit check errors or warnings. Abstract status will reset to INCOMPLETE. Correct these edits and reset ABSTRACT STATUS to Complete to re-run the current EDITS metafile.

## EE Abstract Edit Primary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Abstract Edit Primary option allows you to edit only information related to the cancer and not to a patient’s demographics. Only the primary fields of the abstract are brought up. This option allows you to pull up a patient using only the Accession/Sequence Number.

> **NOTE:** The Accession/Sequence Number must be typed exactly as in the example.

Select \*..Abstracting/Printing Option: EE Abstract Edit Primary

Select primary or patient name: 2000-00163/00

PROSTATE Last, First

> **NOTE:** The site and patient’s name are echoed back to you.

## NC Print Abstract NOT Complete List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Abstract NOT Complete List option allows you to print a list of records with an Abstract Status of Incomplete, Minimal, and Partial. The report shows the accession/sequence number, patient name, SSN, ICDO topography, and the date of diagnosis. Records are sorted according to the Status and Patient Name.

Example

ACC/SEQ

NAME SSN NUMBER PRIMARY SITE COC DATE DX

ABSTRACT STATUS: Incomplete

ONCOPatient1 999-99-9999 2005-00537/00 UNKNOWN PRIMAR 1 07/29/2005

ABSTRACT STATUS: Minimal data

ONCOPatient2 999-99-9999 1995-00136/01 SKIN, TRUNK 1 03/02/1995

ABSTRACT STATUS: Partial

ONCOPatient3 999-99-9999 2005-00752/01 RECTOSIGMOID J 1 10/18/2005

ONCOPatient4 999-99-9999 2005-00763/00 ESOPHAGUS, LOW 1 10/27/2005

> **NOTE:** Only AI and EE allow you to enter data into an abstract.

## *IR* Patient Summary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Summary option allows you to produce a brief summary of the data found in a patient’s abstract.

## *QA* Print Abstract QA (80c) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Abstract QA option allows you to print a user-friendly abstract, which physicians can use when doing the ACoS required QA portion of registry abstracts.

> **NOTE:** 80c (80 columns) presents an easy-to-read display on the computer screen.

## *EX* Print Abstract-Extended (80c) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Abstract Extended option allows you to print a condensed version of a complete abstract.

> **NOTE:** 80c (80 columns) presents an easy-to-read display on the computer screen.

## *PA* Print Complete Abstract (132c) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Complete Abstract option allows you to print a complete abstract, which includes capturing the extended data set or to print without personal identifiers (sensitive information), specifically name and SSN.

> **NOTE:** 132c (132 columns) does not present an easy-to-read display on the computer screen because the text wraps; select a device that can print 132 columns.

## *MA* Print QA/Multiple Abstracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print QA/Multiple Abstracts option allows you to print quality assurance/multiple abstracts.

## *AS Abstract Screens Menu (80c)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Abstract Screens Menu option allows you to print or view on your screen, various portions of a patient’s abstract.

> **NOTE:** 80c (80 columns) presents an easy-to-read display on the computer screen.

# FOL Follow-up Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Follow-up module provides follow up information based on the date of last contact. A patient is considered delinquent or lost to follow-up when no contact is made within 15 months after the date of last contact. Lost cases remain delinquent in follow-up until further information is obtained.

\*\*\*\*\*\*\*\*\*\*\*\* FOLLOW-UP FUNCTIONS \*\*\*\*\*\*\*\*\*\*

PF Post/Edit Follow-up

RF Recurrence/Sub Tx Follow-up

FH Patient Follow-up History

DF Print Due Follow-up List by Month Due

LF Print Delinquent (LTF) List

FP Follow-up Procedures Menu ...

> **NOTE:** The first screen contains the information from the last posted follow-up note. The system prompts you to enter new follow-up information, beginning with Date of Last Contact or Death.

## PF Post/Edit Follow-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Post Follow-up option allows you to post and edit follow-up information.

PF Post/Edit Follow-up: Type the patient's PID#; refer to the *Glossary* on page [66](#glossary).

Date of Last Contact or Death: Date of last contact with the patient and not the date you are entering the patient information.  
To edit the date of contact, select the date and press Enter. To add new follow-up information, type a new date.

DATE ENTERED, REGISTRAR: The system automatically enters the date you are entering the follow-up and the registrar’s name.

VITAL STATUS: Type A for Alive or D for Dead.

FOLLOW-SOURCE: From the STOREmanual, select allowable fields.

COMMENTS: Type information from the patient’s last contact.  
Example

> Patient seen in Oncology clinic, no evidence of disease recurrence.  
> or  
> Patient seen in urology clinic, PSA \<0.05.

CANCER STATUS: Choose from the following:

1 No evidence of this tumor

2 Evidence of this tumor

9 Unknown/not stated if this tumor present

DATE OF LAST CANCER STATUS: Enter the date of last cancer (tumor status) of the patient’s malignant or non-malignant tumor. This data item is required for COC-accredited facilities for cases diagnosed 1/1/2018 and later.

DATE OF LAST CANCER STATUS FLG: If applicable enter the appropriate code. This flag explains why there is no appropriate value in the corresponding date field.

> **NOTE:** Every Complete abstract must have follow-up and TYPE OF FIRST RECURRENCE posted.

## RF Recurrence/Sub Tx Follow-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Recurrence/Sub Tx Follow-up option allows you to document the first recurrence and/or subsequent treatment. Date of first recurrence is the date a medical practitioner diagnoses a recurrence of a cancer after a disease-free period. Recurrence means the return or reappearance of the cancer after a disease-free period.

Select Initiation Date:

Recurrence/Sub Tx Follow-up: Type the patient's or PID#; refer to the *Glossary* on page [66](#glossary).

Type of First Recurrence: Enter the appropriate code for the first recurrence for this primary.

> **NOTE:** To bring up a list of selections, type ?? at the prompt.

Select Subsequent Course of Treatment If the patient did not receive subsequent treatment, press Enter.  
If the patient did receive subsequent treatment, type the date treatment began.

Treatment fields display:

SURGERY OF PRIMARY SITE:

SCOPE OF LYMPH NODE SURGERY:

SCOPE OF LN SURGERY DATE:

SURGICAL PROC/OTHER SITE:

SURGICAL PROC/OTHER SITE DATE:

METS SITE RESECTED:

METS SITE RESECTED DATE:

RADIATION:

RADIATION DATE:

CHEMOTHERAPY:

CHEMOTHERAPY DATE:

HORMONE THERAPY:

HORMONE THERAPY DATE:

IMMUNOTHERAPY:

IMMUNOTHERAPY DATE:

HEMA TRANS/ENDOCRINE PROC:

HEMA TRANS/ENDOCRINE PROC DATE:

OTHER TREATMENT:

OTHER TREATMENT START DATE:

PALLIATIVE CARE:

PLACE:

SUBSEQUENT THERAPY COMMENTS:

No existing text

Edit? NO//  
To enter a comment, type Y.

Initiation Date: For each recurrence for this primary, type the date the course of treatment began.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* POST/EDIT FOLLOW-UP \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Update the follow-up now.

> **NOTE:** The subsequent course of treatment may consist of multiple treatments. If a patient did not receive a particular treatment, be sure to code it 00 for *no treatment*. Do not leave any treatment fields blank.

## FH Patient Follow-up History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Follow-up History allows you to print the patient's follow-up history, including when the next follow-up is due. Type the patient's name and a device, or print to your screen.

## DF Print Due Follow-up List by Month Due

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Due Follow-up List by Month Due option allows you to print a list of follow-ups that are due for a selected date range. They display by month due, along with the SSN, primary site, last date of contact, and date of diagnosis.

Your previous date range selection displays automatically. You want to be current by doing a patient due for follow-up in the month that the follow-up is scheduled; however, with other duties to perform, you may not be able to do this. In this case, work on the Lost To Follow-up list.

Example

START WITH DUE FOLLOW-UP: // 12-2005 (DEC 2005)

GO TO DUE FOLLOW-UP: LAST// 12-31-05 (DEC 31 2005)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

TUMOR REGISTRY - DUE FOLLOW-UP Washington DC VAMC DEC 21, 2005 PAGE: 1

Patient Name Med Rec# Contact Primary Site/Gp Date Dx

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

DUE FOLLOW-UP: DEC 2005

ONCOPATIENT1 999-99-9999 12/1/2004 TESTIS 03/13/1986 TESTIS 07/27/1999

ONCOPATIENT2 999-99-9999 12/31/2004 MELANOMA 11/05/2004

ONCOPATIENT3 999-99-9999 12/14/2004 SOFT TISSUE 04/19/2002

-------------------------------------------

COUNT 3

## LF Print Delinquent (LTF) List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Delinquent (LTF) List option allows you to print a list of all patients whose Due Follow-up date is over 3 months (are not seen/contacted for over 15 months). These patients are considered lost to follow-up. The report is sorted by the month and year the follow-up was due and prints the SSN, date of last contact, Site/Gp, and date of diagnosis.

> **NOTE:** You may want to use this option frequently; if you are in a crunch, run only this list and work to reduce these numbers.

Example

ONCOLOGY DELINQUENT (LTF) LIST

DATE

LAST

NAME SSN CONTACT SITE/GP DATE DX

------------------------------------------------------------------------------------------------ DUE FOLLOW-UP: MAY 1997

ONCOPATIENT1 999-99-9999 5/03/1996 BLADDER 10/25/1993

DUE FOLLOW-UP: JUN 2005

ONCOPATIENT2 999-99-9999 06/07/2004 PROSTATE 05/14/1998

DUE FOLLOW-UP: AUG 2005

ONCOPATIENT3 999-99-9999 08/19/2004 PROSTATE 02/06/1985

DUE FOLLOW-UP: SEP 2005

ONCOPATIENT4 999-99-9999 09/01/2004 ENDOCRINE, OTHER 06/24/1996

ONCOPATIENT5 999-99-9999 09/13/2004 BREAST 03/22/2000

COUNT 5

## *FP Follow-up Procedures Menu*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Follow-up Procedures Menu option allows you to manage follow-up by providing a list of contacts for the patient, follow-up letters, and a summary report of the patient follow-up.

PI Patient Follow-up Inquiry

AC Add Patient Contact

AF Attempt a Follow-up

PL Print Follow-up Letter

EL Add/Edit Follow-up Letter

FR Individual Follow-up Report

\*\*\> Out of order: Marked for deletion

UP Update Contact File

Type a patient name at the prompt.

- PI Patient Follow-up Inquiry – view the last time a patient had follow-up and the status of the cancer at that time.
- AC Add Patient Contact – view contacts for a specific patient and add other contacts. Additional contacts may be useful when doing follow-up on a patient.
- AF Attempt a Follow-up – document the date for which you want a patient follow-up and the method you used.
- PL Print Follow-up Letter – print a follow-up form letter to send to obtain follow-up.
- EL Add/Edit Follow-up Letter – edit or create other follow-up letters specific to your facility.

## Follow-up Letter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To send a letter to a patient, use the AC, AF, and PL options, in this sequence.

#### To generate a follow up letter:

Select OncoTrax Cancer Registry Option: fol \*..Follow-up Functions

\*\*\*\*\*\*\*\*\*\*\*\* FOLLOW-UP FUNCTIONS \*\*\*\*\*\*\*\*\*\*

PF Post/Edit Follow-up

RF Recurrence/Sub Tx Follow-up

FH Patient Follow-up History

DF Print Due Follow-up List by Month Due

LF Print Delinquent (LTF) List

SR Follow-up Status Report by Patient (132c)

FP Follow-up Procedures Menu ...

Select \*..Follow-up Functions Option: FP

Follow-up Procedures Menu

PI Patient Follow-up Inquiry

AC Add Patient Contact

AF Attempt a Follow-up

PL Print Follow-up Letter

EL Add/Edit Follow-up Letter

FR Individual Follow-up Report

UP Update Contact File

Select Follow-up Procedures Menu Option: AC Add Patient Contact

\*\*\*\*\*\*\*\*\* DISPLAY CONTACTS \*\*\*\*\*\*\*\*\*\*

Select Patient: T9999 (Type the PID# to bring up patient or patient’s name)

Searching for a VA Patient, (pointed-to by NAME)

LAST,FIRST 10-23-26 000129999

All of the contacts for this patient are displayed

AVAILABLE CONTACTS

==================

Patient LAST,FIRST

000 999-0000

1269 STREETNAME ST

City, ST 00000

Next of Kin LAST,FIRST1, NEXT OF KIN

000 999-0000

0000 STREETNAME ST

City,ST 00000

\*\*\*\*\*\*\*\*\*\* ADD/EDIT CONTACTS \*\*\*\*\*\*\*\*\*\*

for: Last,First

#### To send a letter to a patient:

Select TYPE OF FOLLOW-UP CONTACT: Guardian// PT Type PT.

TYPE OF FOLLOW-UP CONTACT: Patient//

CONTACT NAME: LAST,FIRST1//

Go to the Contact File to edit the contact's name and address.

CONTACT: LAST,FIRST1//

STREET ADDRESS 1: 0000 STREETNAME ST//

STREET ADDRESS 2:

STREET ADDRESS 3:

ZIP CODE: City,ST 00000

> **NOTE:** Always check the Zip Code field. The first town alphabetically with the zip code is selected. Compare it with the address in CPRS and select the correct town.

PHONE: 000 999-0000//

TITLE: Mr// Type a title without a period (Mr Mrs Ms and so on)

COMMENTS:

Select one of the following:

1 Display Contacts

2 Edit Contact

3 Attempt a Follow-up Select 3 Attempt a Follow-up.

4 Another Patient

5 Exit Option

Select Action: 3// Attempt a Follow-up

\*\*\*\*\*\*\*\*\*\* ATTEMPT A FOLLOW-UP \*\*\*\*\*\*\*\*\*\*

for Last,First

Select FOLLOW-UP ATTEMPT DATE: JUL 5,2005//

FOLLOW-UP ATTEMPT DATE: JUL 5,2005//

TYPE: ?

How will you be obtaining follow-up information?

Choose from:

1 Chart Review

2 Phone Contact

3 Letter Contact Select 3 Letter Contact

8 Other

THE CONTACT: LAST,First1,// Type the patient’s last name.

RESULT: Pending//

REMARKS:

Generate Letter...!!

Specify TYPE Contact letter: ?? ?? (two question marks)  
brings up a list from which to select a type.

Choose from:

1 PATIENT \*Washington LETTER\*

2 PATIENT \*Washington 2\* DOT MATRIX

3 PATIENT \*Washington 3 LETTER\*

4 PATIENT \*Washington NEW\*

5 PATIENT TESTING LETTER

CHOOSE 1-5: 1 PATIENT \*Washington LETTER\*

DEVICE: (ENTER YOUR PRINTER)

#### To edit the follow-up letter:

Follow-up Procedures Menu

PI Patient Follow-up Inquiry

AC Add Patient Contact

AF Attempt a Follow-up

PL Print Follow-up Letter

EL Add/Edit Follow-up Letter Select EL Add/Edit Follow-up Letter.

FR Individual Follow-up Report

UP Update Contact File

EL Add/Edit Follow-up Letter

Select letter to Add/Edit: PAT Type PAT.

1 PATIENT \*Washington LETTER\*

2 PATIENT \*Washington DOT MATRIX

3 PATIENT \*Washington 2 LETTER\*

4 PATIENT \*Washington NEW\*

5 PATIENT TESTING LETTER

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5:

1 PATIENT \*Washington LETTER\*

NAME: PATIENT \*Washington LETTER\* Replace To change the name, type … and press Enter. Type the name change for the letter.

FORM TYPE: PATIENT// ?

DESCRIPTION:

No existing text

Edit? NO//

MAIN FORM BODY:. . .

Our hospital has a clinical program engaged in following the progress of our former patients. We are interested in knowing how you are doing.

Edit? NO// YES Respond YES to edit the letter.

This takes you into the text editor (like VistA E-MAIL), where you can make changes to the wording of the letter. *Do not change anything that is between the upright characters*.

Example\|PATIENT NAME\|

This information is automatically pulled from other parts in VistA. If you delete an *upright* or alter the text in the *upright*, the information is not placed into your letter.

Edit? NO// YES

Example of the editing screen

DO NOT CHANGE ANYTHING WITHIN THE UPRIGHTS OR DELETE THEM

\|INDENT(10)\| DEPARTMENT OF VETERANS AFFAIRS

\|HOSPITAL NAME\|

\|HOSPITAL STREET ADDRESS\|

\|HOSPITAL CITY,ST ZIP\|

\|LAST(FOLLOW-UP ATTEMPTS:FOLLOW-UP ATTEMPT DATE)\|

\|SSN\|

528/111H

\|LOWERCASE(ONCOFIRSTNAME LASTNAME(LAST FOLLOW-UP CONTACT))\|\|TAB\|

\|LAST FOLLOW-UP CONTACT:STREET ADDRESS 1\|

\|WRAP\|

\|LAST FOLLOW-UP CONTACT:STREET ADDRESS 2\|

\|LAST FOLLOW-UP CONTACT:STREET ADDRESS 3\|

\|NOWRAP\|

\|LAST FOLLOW-UP CONTACT:ZIP CODE\|

Dear \|LAST FOLLOW-UP CONTACT:TITLE\|. \|LOWERCASE(LAST NAME)\|,

Text below this line may be changed.

#### Example of a follow-up letter to a patient

Our hospital has a clinical program engaged in following

the progress of our former patients. We are interested in

knowing how you are doing.

Would you be kind enough to answer the questions

listed below? Your assistance will add to the

success of this program and help us achieve better

patient care in our hospital. A self-addressed

stamped envelope is enclosed for your convenience.

Thank you for your participation.

Sincerely,

\|Cancer Registrar\|

Cancer Registrar

Today's date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

What is your present status?

\_\_\_\_\_ Free of cancer \_\_\_\_\_ Not free of cancer

Are you able to work or carry on normal activity? \_\_\_\_ YES, Normal

\_\_\_\_\_ Limited \_\_\_\_\_ Capable, but limited \_\_\_\_\_ Incapable \_\_\_\_\_ Bedridden

Have you seen a doctor outside of the VA Medical Center?

\_\_\_\_\_ Yes \_\_\_\_\_ No If "Yes", who and where:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

IF THE PATIENT IS DECEASED, Please give date and place of death:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

What was the cause of death? \_\_\_\_\_\_\_Cancer \_\_\_\_\_\_\_\_Not Cancer

\_\_\_\_\_ Other causes (specify) \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Please list any other symptoms relating to your condition not covered in the above items on the back of this sheet.

LIS Registry Lists Module

The Registry Lists module is a menu of registry listings containing various accession registers, and patient and site reports.

Any 132c report requires a printer that prints 132 columns. Any 80c report requires a printer that prints 80 columns. The majority of the reports produce information that includes the entire database. If you have 20 years of data in your registry, the report contains all 20 years of data. For data from a specific year, use the options in the

ANN \*..Annual Reports ...module.

\*\*\*\*\*\*\*\*\*\*\*\*Cancer Registry Lists\*\*\*\*\*\*\*\*\*\*\*\*

AA Accession Register-ACoS (80c)

AS Accession Register-Site (80c)

AE Accession Register-EOVA (132c)

PA Patient Index-ACoS (132c)

PS Patient Index-Site (80c)

PE Patient Index-EOVA (132c)

IN Primary ICDO Listing (80c)

SG Primary Site/GP Listing (80c)

IW Primary ICDO Listing (132c)

## AA Accession Register-ACoS (80c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Accession Register-ACoS list allows you to print all records. This contains the ACoS required *Accession Register* data items.

> **NOTE:** 80c (80 columns) presents an easy-to-read display on the computer screen.

Press Enter at the START WITH prompt.

For a complete register:

START WITH ACC/SEQ NUMBER: FIRST// \<Enter\>

To get all records beginning with the same year:

For a single accession year (e.g. 2003):

START WITH ACC/SEQ NUMBER: FIRST// 2003-00000

GO TO ACC/SEQ NUMBER: LAST// 2003-99999

To get a Specific range of records:

START WITH ACC/SEQ NUMBER: 2004-00400 -00//

GO TO ACC/SEQ NUMBER: 2004-00500

ACC/SEQ# PATIENT NAME ICDO TOPOGRAPHY DATE DX YEAR

2004-00400/00 ONCOPATIENT1 C42.0 BLOOD 06/03/2004 2004

2004-00408/00 ONCOPATIENT2 C02.9 TONGUE NOS 06/24/2004 2004

2004-00409/00 ONCOPATIENT3 C18.7 COLON, SIGMOID 06/24/2004 2004

## *AS Accession Register-Site (80c)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Accession Register Site list allows you to select a range of accession years or a range of accession numbers.

> **NOTE:** 80c (80 columns) presents an easy-to-read display on the computer screen.

You are provided with the following data:

ACC/SEQ \# PATIENT NAME SSN PRIMARY SITE/GP DATE DX YEAR

## *AE Accession Register-EOVA (132c)* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Accession Register-EOVA list is similar to AA Accession Register-ACoS, but displays more fields.

> **NOTE:** 132c (132 columns) does not present an easy-to-read display on the computer screen because the text wraps; select a device that can print 132 columns.

## PA Patient Index-ACoS (132c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Index-ACoS allows you to print the Patient Index, which contains all elements required by the ACoS Cancer Program, for all the patients in the registry. The list is very long.

> **NOTE:** 132c (132 columns) does not present an easy-to-read display on the computer screen because the text wraps; select a device that can print 132 columns.

Example

PATIENT NAME MED RECORD# S DT-BIRTH DT-DEATH ACC/SEQ-NO DATE DX ICD–TOPOGRAPHY L ICDO–MORPHOLOGY

----------------------------------------------------------------------------

ONCOPATIENT1 000-00-0000 M 07/01/1940 07/25/2000 2000-00371/00 09/25/1992 C18.5–COLON, SPLENIC

## *PS Patient Index-Site (80c)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Index Site list provides an alphabetical list of the entire registry.

> **NOTE:** 80c (80 columns) presents an easy-to-read display on the computer screen.

PATIENT NAME SSN SX ACC/SEQ \# PRIMARY SITE/GP DATE DX

## *PE Patient Index-EOVA (132c)* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Index-EOVA is similar to PA Patient Index Site, but provides slightly different information.

> **NOTE:** 132c (132 columns) does not present an easy-to-read display on the computer screen because the text wraps; select a device that can print 132 columns.

## *IN Primary ICDO Listing (80c)* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Primary ICDO Listing provides a list of all cases in the entire registry by the ICDO codes. The list begins with ICDO-SITE: C00-LIP. The list is very long.

> **NOTE:** 80c (80 columns) presents an easy-to-read display on the computer screen.

PATIENT NAME SSN YEAR ACC/SEQ \# TOPOGRAPHY DATE DX

## SG Primary Site/GP Listing (80c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Primary Site/GP Listing provides a list of all cases in the entire registry by requested site/gp. The previous selection displays as the default.

> **NOTE:** 80c (80 columns) presents an easy-to-read display on the computer screen.

\* Previous selection: SITE/GP equals LUNG

START WITH SITE/GP: LUNG// PANCREAS Type PANCREAS.

GO TO SITE/GP: LAST// PANCREAS

Previous selection: ICDO TOPOGRAPHY-CODE from C34.0 to C34.9

START WITH PRIMARY SITE CODE: C34.0// C25 For a specific primary site use only that code

GO TO PRIMARY SITE CODE: C34.9// C25.9

Example

List for an ICDO Code, sorted alphabetically.

PATIENT NAME SSN YEAR ACC/SEQ \# TOPOGRAPHY DATE DX

---------------------------------------------------------------------------

ICDO CODE: C25.0

LAST,FIRST A 000-00-0000 2002 2002-00072/00 PANCREAS HEAD 02/20/2002

ICDO CODE: C25.1

LAST,FIRST B 000-00-0000 1978 1978-00089/00 PANCREAS BODY 05/01/1978

LAST,FIRST C 000-00-0000 2005 2005-00143/02 PANCREAS BODY 03/23/2005

ICDO CODE: C25.2

LAST,FIRST D 000-00-0000 2006 2006-00001/00 PANCREAS TAIL 01/01/2006

LAST,FIRST E 000-00-0000 1985 1985-00347/03 PANCREAS TAIL 07/17/1985

ICDO CODE: C25.9

LAST,FIRST F 000-00-0000 2005 2005-00089/00 PANCREAS NOS 05/01/2005

LAST,FIRST G 000-00-0000 1998 1998-00019/00 PANCREAS NOS 02/01/1998

## IW Primary ICDO Listing (132c) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Primary ICDO Listing provides a list of all patients by all primary site codes in the entire registry.

PRIMARY SITE: C00.0-LIP, EXTERNAL UPPER

PATIENT NAME SSN DOB DOD YEAR ACC/SEQ# DATE DX TOPOGRAPHY MORPHOLOGY

> **NOTE:** If you have time, experiment with this listing to see all that it can provide.

# ANN Annual Reporting Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Annual Reporting module is a menu of annual reports.

Annual Reports

AAR Annual ACoS Accession Register (80c)

API Annual ACoS Patient Index (132c)

ASL Annual Primary Site/GP Listing (132c)

ACL Annual Patient List by Class of Case (80c)

SST Annual Primary Site/Stage/Tx (132c)

TST Annual ICDO Topography/Stage/Tx (132c)

SDX Annual Status/Site/Dx-Age (132c)

HIS Annual Histology/Site/Topography (80c)

ACT Annual Cross Tabs (80c)

CPR Print Custom Reports

- The Annual ACoS Accession Register and Annual ACoS Patient Index are required for ACoS approval.
- Print Custom Reports allows you to retrieve data requested by your staff from your database. It requires knowledge of basic FileMan functions.

## AAR Annual ACoS Accession Register (80c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ACoS Annual Accession Register is an annual report required by ACoS. The report is sorted by accession /sequence number within a specific accession year and a count of the records prints at the end.

> **NOTE:** 80c (80 columns) presents an easy-to-read display on the computer screen.

Select year: 2005 Type specific year.

Example of the report

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

ACC/SEQ-No Patient Name ICDO – Topography Date Dx C L

1975-00334/04 ONCOPATIENT1 C44.1 SKIN, EYELID 01/19/2005 1 1

1987-00118/03 ONCOPATIENT2 C80.9 UNKNOWN PRIMARY 05/10/2005 1 0

2005-00055/00 ONCOPATIENT3 C61.9 PROSTATE 02/08/2005 1 0

## API Annual ACoS Patient Index (132c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Annual ACoS Patient Index is an annual report of the required ACoS items for an accession year. A count of the records prints at the end.

> **NOTE:** 132c (132 columns) does not present an easy-to-read display on the computer screen because the text wraps; select a device that can print 132 columns.

Select year: Type specific year.

Example – fields in this report

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PATIENT NAME MED RECORD# DT-BIRTH DT-DEATH ACC/SEQ-NO ICDO – TOPOGRAPHY MORPHOLOGY L

## ASL Annual Primary Site/GP Listing (132c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** 132c (132 columns) does not present an easy-to-read display on the computer screen because the text wraps; select a device that can print 132 columns.

The Annual Primary Site/GP Listing is an annual report sorted first by accession year and then by the primary site/group.

Example

START WITH ACCESSION YEAR: FIRST// 2003

GO TO ACCESSION YEAR: LAST// 2003

START WITH SITE/GP: FIRST// BLADDER

> **NOTE:** Type the SITE/GP in capital letters.

GO TO SITE/GP: LAST// BLADDER

Example – fields in this report

A list of all patients from the year 2003 with a primary Bladder cancer displays.

PATIENT NAME MED RECORD# S DT-BIRTH DT-DEATH ACC/SEQ DATE DX ICDO TOPOGRAPHY ICDO MORPHOLOGY

## ACL Annual Patient List by Class of Case (80c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Annual Patient List by Class of Case is an annual report listing all patients alphabetically, for a specific year for each class of case.

> **NOTE:** 80c (80 columns) presents an easy-to-read display on the computer screen.

Example – fields in this report

Patient Name Med Rec# Sx Acc/Seq# Site/Group Date Dx

## SST Annual Primary Site/Stage/Tx (132c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Annual Primary Site/Stage/Tx is an annual report listing patients for a specific year and specific site and stage.

> **NOTE:** 132c (132 columns) does not present an easy-to-read display on the computer screen because the text wraps; select a device that can print 132 columns.

START WITH ACCESSION YEAR: 2005//

GO TO ACCESSION YEAR: LAST// 2005

\* Previous selection: SITE/GP equals PHARYNX

START WITH SITE/GP: PHARYNX//

GO TO SITE/GP: PHARYNX//

Example – fields in this report

PT ID TX TREATMENT SURG DATE SURGERY RAD DATE RADIATION CHEMO DT CHEMOTHERAPY HT DATE HORMONE TPY

## TST Annual ICDO Topography/Stage/Tx (132c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Annual ICDO Topography/Stage/Tx is an annual report listing cases by stage and site for a selected accession year and selected ICDO-topography.

> **NOTE:** 132c (132 columns) does not present an easy-to-read display on the computer screen because the text wraps; select a device that can print 132 columns.

START WITH ACCESSION YEAR: 2006// 2005 Define the year.

GO TO ACCESSION YEAR: 2006// 2005

\* Previous selection: ICDO-SITE CODE from C00 to C90

START WITH PRIMARY SITE CODE PREFIX: C00// Define the ICDO-SITE CODE (S).

GO TO PRIMARY SITE CODE PREFIX: C90// C02

Example

--------------------------------------------------------------------------

ICDO-SITE CODE: C32

STAGE GROUPING-AJCC: I

W5555 C32.0 NONE

-------

SUBCOUNT 1

R3333 C32.0 XRT 00/00/0000 06/13/2005 Beam radiation 00/00/0000 None 00/00/0000 None

-------

SUBCOUNT 1

-------

SUBCOUNT 2

STAGE GROUPING-AJCC: II

B4444 C32.0 XRT 00/00/0000 03/03/2005 Beam radiation 00/00/0000 None 00/00/0000 None

-------

SUBCOUNT 1

-------

SUBCOUNT 1

STAGE GROUPING-AJCC: IV

B6666 C32.0 NONE

-------

SUBCOUNT 1

P7777 C32.1 SUR 09/02/2005

-------

SUBCOUNT

H7777 C32.1 XRT/CMX 00/00/0000 07/13/2005 Beam radiation 07/18/2005 Multiagent00/00/0000 None

-------

SUBCOUNT 1

-------

SUBCOUNT 3

-------

COUNT 6

## SDX Annual Status/Site/Dx-Age (132c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Annual Status/Site/Dx-Age is an annual report listing patients for a specific accession year.

> **NOTE:** 132c (132 columns) does not present an easy-to-read display on the computer screen because the text wraps; select a device that can print 132 columns.

Annual report - sorted first by Accession year

Then by Class Category (Non-analytic/Analytic)

Then by Status, Site/GP, and Diagnosis Age Gp.

Enter four digit ACCESSION YEAR,

For Class category: either 'A'

for Analytic, or first to last.

Example

START WITH ACCESSION YEAR: 2005

GO TO ACCESSION YEAR: LAST// 2005 .

\* Previous selection: CLASS CATEGORY equals 1 (ANALYTIC)

START WITH CLASS CATEGORY: 1// ANALYTIC

GO TO CLASS CATEGORY: 1// ANALYTIC

DEVICE:

PRIMARY LIST

DX AGE-GP: 60-69

ONCOPATIENT1 999-99-9999 2005-00054/00 02/02/2005 ANUS NOS SQUAM CELL CARC T1 N0 M0 I SUR

ONCOPATIENT2 999-99-9999 2005-00272/00 03/22/2005 ANUS NOS SQUAM CELL CARC TX NX MX Unkno UR/CMX

## HIS Annual Histology/Site/Topography (80c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Annual Histology/Stage/Topography is an annual report listing.

> **NOTE:** 80c (80 columns) presents an easy-to-read display on the computer screen.

START WITH ACCESSION YEAR: 2005//

GO TO ACCESSION YEAR: LAST// 2005

START WITH SITE/GP: PHARYNX//

GO TO SITE/GP: PHARYNX//

Example

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

2005 - ANALYTIC Washington DC VAMc DEC 21,2005 PAGE: 1

Patient Name Med Rec# Sx Acc/Seq# ICDO-Topography Date Dx

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

ICDO HISTOLOGY-CODE: 8070/3

SITE/GP: PHARYNX

ICDO-SITE CODE: C01

PATIENT NAME: ONCOPATIENT1

ONCOPATIENT1 999-99-9999 M 2005-00096/00 TONGUE BASE 03/14/2005

ICDO-SITE CODE: C09

PATIENT NAME: ONCOPATIENT2

ONCOPATIENT2 999-99-9999 M 2005-00494/00 TONSILLAR FOSSA 07/12/2005

ICDO-SITE CODE: C10

PATIENT NAME: ONCOPATIENT3

ONCOPATIENT3 999-99-9999 M 2005-00029/00 OROPHARYNX NOS 01/27/2005

COUNT 4 -------------

SUBCOUNT 3

## ACT Annual Cross Tabs (80c)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Annual Cross Tabs is an annual report that is very long. Queue this report after hours.

> **NOTE:** 80c (80 columns) presents an easy-to-read display on the computer screen.

## CPR PRINT Custom Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRINT Custom Reports option allows you to create custom reports using VA FileMan.

> **NOTE:** It is very helpful to have some FileMan training from the computer department at your facility. Also, with knowledge of capturing files and opening them in Microsoft Excel, you can create a very usable and professional document.

You can retrieve any data that you enter into an abstract. Create a report by specifying:

- file from which the information is coming, ONCOLOGY Primary (#165.5), ONCOLOGY Patient (#160), or ONCOLOGY Contact (#165);
- fields that contain the data;
- how to separate/sort the data; and
- information to be printed.

# STA Statistical Reporting Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Statistical Reporting module allows you to obtain 5-year survival information on your data. You can search for user-defined criteria.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*STATISTICAL REPORTS\*\*\*\*\*\*\*\*\*\*\*\*\*\*

TS Treatment by Stage - Cross tabs

SP Survival by Site

SS Survival by Stage

TX Survival by Treatment

SU Survival Routines

DS Define Search Criteria

## DS Define Search Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Define Search Criteria option allows you to define criteria to obtain 5-year survival information from:

SP Survival by Site

SS Survival by Stage

TX Survival by Treatment

In order to use SP, SS, TX, or SU (Survival Routines), you must first create a template using DS Define Search Criteria.

Use DS to create search templates for Survival Analysis.

> **NOTE:** Name templates beginning with ONCOZ for user-defined templates rather than software-distributed names, ONCOS.

Select one of the following:

1 ONCOTRAX PRIMARY

2 ONCOTRAX PATIENT

3 ONCOTRAX CONTACT

Select File: 1 ONCOTRAX PRIMARY

We will search entries in ONCOTRAX PRIMARY file...

-A- SEARCH FOR ONCOTRAX PRIMARY FIELD: SITE/GP

-A- CONDITION: ? Type ? to view choices.

Answer with CONDITION NUMBER, or NAME Type a condition.

Choose from

1 NULL

2 CONTAINS

3 MATCHES

4 LESS THAN

5 EQUALS

6 GREATER THAN

YOU CAN NEGATE ANY OF THESE CONDITIONS BY PRECEDING THEM WITH “’” OR "-"

SO THAT "'NULL'" MEANS "NOT NULL"

-A- CONDITION: CONTAINS

-A- CONTAINS: LUNG NOS

-B- SEARCH FOR ONCOTRAX PRIMARY FIELD: ACCESSION YEAR

-B- CONDITION: GREATER THAN

-B- GREATER THAN: 1995

-C- SEARCH FOR ONCOTRAX PRIMARY FIELD: ACCESSION YEAR

-C- CONDITION: LESS THAN

-C- LESS THAN: 2001

-D- SEARCH FOR ONCOTRAX PRIMARY FIELD: CLASS CATEGORY

-D- CONDITION: EQUALS

-D- EQUALS: ANALYTIC Use only analytic cases for survival data.

-E- SEARCH FOR ONCOTRAX PRIMARY FIELD:

> **NOTE:** If you want to include more data, continue with E. If not, press Enter and at IF, type the letters of your search criteria. The screen echoes back your selections.

IF: ABCD SITE/GP CONTAINS (case-insensitive) "LUNG NOS"

and ACCESSION YEAR GREATER THAN 1995

and ACCESSION YEAR LESS THAN 2001

and CLASS CATEGORY EQUALS "1" (ANALYTIC)

or

STORE RESULTS OF SEARCH IN TEMPLATE: ONCOZ LUNG NOS SURVIVAL

> Name the template beginning with ONCOZ. Press Enter to start the sort.

> **NOTE:** You do a sort make sure that data is available. You can sort and print any data you want to view.

SORT BY: NUMBER// AJCC STAGE

START WITH AJCC STAGE: FIRST//

WITHIN AJCC STAGE, SORT BY:

FIRST PRINT FIELD: !PID#

THEN PRINT FIELD: DATE DX

THEN PRINT FIELD: TREATMENT PLAN

THEN PRINT FIELD:

Heading (S/C): ONCOTRAX PRIMARY STATISTICS Replace

Running Survival Options.

SP Survival by Site

SS Survival by Stage

TX Survival by Treatment

### SP Survival by Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Survival by Site produces a 5-year survival by site, from the criteria you set in the DS Define Search Criteria.

### SS Survival by Stage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Survival by stage produces a 5-year survival by AJCC Stage, from the criteria you set in the DS Define Search Criteria.

### TX Survival by Treatment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Survival by Treatment produces a 5-year survival by the treatment, from the criteria you set in the DS Define Search Criteria.

Each of the three options also generates a list of patients who are dropped from the search and why.

Example including reason

Cases dropped: 4

PATIENT REASON FOR BEING DROPPED

---------------------- --------------------------------

L9999 ONCOPATIENT1 SURVIVAL MONTHS 0

Y1111 ONCOPATIENT2 SURVIVAL MONTHS 0

Example of the survival information for the template

ONCOTRAX PRIMARY Template ONCOZ LUNG NOS SURVIVAL 96-99

Life Table

Yrs % Alive \# Left Deaths Losses

-----------------------------------------------------------------------

0 100.0 416 259 0

1 37.7 157 73 0

2 20.2 84 17 0

3 16.1 67 18 0

4 11.8 49 6 10

5 10.2 33 3 5

## TS Treatment by Stage - Cross Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Treatment by Stage – Cross tabs option allows you to print cross-tabs for all analytic cases for treatment by stage groups (I, II, III, IV). It is a large report and not user-friendly to view.

# UTL Utility Options Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Utility Options module allows you to manage the information in your OncoTrax database. You can correct errors, delete records, and create data disks to send to national and state databases.

RS Registry Summary Reports

DP Delete Oncology Patient

DS Delete Primary Site/GP Record

SQ Find Duplicate Acc/Seq Numbers

EA Edit Site/AccSeq# Data

LG List Topographic Site Groups

LT List Topography Codes by Site Group

AR Create a report to preview ACoS output

CT Create ACoS Data Download

SR Create a report to preview State/VACCR output

CC Create State Data Download

TR Define Tumor Registry Parameters

AC Enter/Edit Facility file

CDD1 Print Condensed DD--Oncology Patient file

CDD2 Print Condensed DD--Oncology Primary file

PSR Purge Suspense Records

SP Purge Patient Records with No Suspense/Primaries

CS Restage CS cases using latest version

TNM Compute percentage of TNM forms completed

TIME Timeliness Report

CHEM Enter/Edit Chemotherapeutic Drugs file

RCRS Create RCRS extract

RQRS Create RQRS extract

TEXT Find non-standard characters in TEXT

UPC Update Oncology Physician Contacts

VL Check Validity of TNM Field Values

## RS Registry Summary Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Registry Summary Reports provide a quick count for:

- T–Today
- A–Annual (132c)
- F–Follow-up

The *Today* report gives you an overview of the entire registry on the day and time you run the report.

Analytical: 10144

Non-Analytical: 1515

Total: 11659

WORKLOAD STATISTICS

Suspense: 4 Incomplete: 68 Minimal: 4 Partial: 35 Complete: 1311

The *Annual* report gives you the number of cases for the selected year by site, race, sex, and the AJCC Stage. There are two options to choose from after you select the year.

Select year for summary: (1952-2006): 2005//

Analytic cases only? YES// m

Answer 'YES' if you want only analytic cases (CLASS OF CASE 0-2) displayed.

Answer 'NO' if you want all cases (analytic and non-analytic) displayed.

The *Follow-up* report offers two options that meet the ACoS requirements. This report has changed in 2023 to a 15- or 5-year rolling window report based on reference date or COC Accreditation date.

Follow-up rate calculation parameters (select 1 or 2):

1\) 15 Year Rolling Follow-Up Rate for All Patients: For all eligible

analytic cases (Class of Case 10-14 and 20-22) from the most

current year of completed cases through 15 years prior or the

program's first accreditation date (or reference date if no

accreditation date), whichever is shorter.

2\) 5 Year Rolling Follow-Up Rate for Recent Patients: For all eligible

analytic cases (Class of Case 10-14 and 20-22) diagnosed from

the most current year of completed cases through five years

preceding or the program's first accredited date (or reference

date if no accreditation date), whichever is shorter.

Select follow-up rate calculation parameter:

Example of selection 1

JUN 8,2023@10:23:09

15 Year Rolling Follow-Up Rate for All Patients

COC ACCREDITATION DATE: JAN 1,2010

REFERENCE DATE: JAN 1,2002

Total patients from accredited OR reference date - 15 years: 7

Less foreign residents: 1

Less patients over 100 years of age: 2

NUMBER PERCENT

A. Subtotal (after subtractions): - 4 100%
B. Less number expired: - 1 25%
C. Subtotal (number living): - 3 75%
D. Number living with current f/u

info (within 15 months): - 2 50%

E. Patients lost to follow-up: - 1 25%
F. Percent of successful follow up\*

(should be at least 80%): - 3 75%

> **NOTE:** Percent should be 80% or greater.

## DP Delete Oncology Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** With Patch ONC\*2.2\*18 the functionality in this option will be removed. It was deemed to be problematic for a patient record to be permanently deleted from the Oncology Patient (#160) File.

*The Delete Oncology Patient option allows you to delete an Oncology patient from the Oncology Patient file. You can also delete any associated records in the Oncology Primary file.Note: Once you delete an abstract, you cannot undelete it. If you delete a patient by mistake, you have to manually re-enter the patient’s abstract.*

## DS Delete Primary Site/Gp Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** With Patch ONC\*2.2\*18 the functionality in this option will be removed. It was deemed to be problematic for a patient primary record to be permanently deleted from the Oncology Primary (#165.5) File.

*The Delete Primary Site/Gp Record option allows you to delete a selected primary record for a specific OncoTrax patient.*

## SQ Find Duplicate Acc/Seq Numbers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Find Duplicate Ac/Seq Numbers option will check for any existing duplicates in the system.

## EA Edit Site/AccSeq# Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit Site/AccSeq# Data option allows you to edit/correct accession numbers, sequence numbers, diagnosis dates, and so on.

## AR Create a Report to Preview ACoS Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Create a Report to Preview ACoS Output option allows the cancer registrar to preview the contents of the specified accessions intended as output for the ACoS.

## CT Create ACoS Data Download

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Create ACoS Data Download option allows you to create the file for submission to the American College of Surgeons (ACoS), in response to the annual call for data.

## SR Create a Report to Preview State/VACCR Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Create a Report to Preview State/VACCR Output option allows you to print the state extract data in a report format.

## CC Create State Data Download

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Create State Data Download option allows you to create a file for the transmission of cancer registry information, excluding confidential patient identity data to the State collecting agencies. This extraction routine includes/downloads only patients from your state based on ZIPCODE and COUNTY AT DIAGNOSIS. It also blanks out communicable diseases and substance abuse, which are protected by federal law.

## TR Define Tumor Registry Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Define Tumor Registry Parameters option allows you to set up the Oncology: Tumor Registry software. You must use this option first, in order to make several of the follow-up options work. For more information, refer to software implementation in the *Oncology Technical Manual and Software Security Guide* at <https://www.va.gov/vdl/application.asp?appid=81>

## AC Enter/Edit Facility File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter/Edit Facility File option allows you to enter new facilities in the Facility file or change the data for a facility.

## CDD1 Print Condensed DD--Oncology Patient file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Condensed DD-Oncology Patient file option allows you to view the data dictionary, which lists all patient information files in the abstract. Use this option when doing custom reports.

## CDD2 Print Condensed DD-Oncology Primary file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Condensed DD-Oncology Primary file option allows you to view the data dictionary, which lists all primary information files in the abstract. Use this option when doing custom reports.

## PSR Purge Suspense Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge Suspense Records option allows you to enter multiple dates in the suspense file when deleting.

## SP Purge Patient Records with No Suspense/Primaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Purge Patient Records with No Suspense/Primaries option allows you to purge Oncology Patient records with no suspense records and no primaries

## CS Restage CS Cases 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Restage CS Cases option allows you to correct a problem in Collaborative Staging; use the most current version of collaborative staging. Run it only once.

## TNM Compute Percentage of TNM Forms Completed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Compute Percentage of TNM Forms Completed option allows you to compute the percentage of Primary Tumor, Regional Lymph Nodes, and Distant Metastasis forms completed.

## TIME Timeliness Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Timeliness Report computes the percentage of cases within the selected date range, which have an ELAPSED DAYS TO COMPLETION value less than 180 days.

## CHEM Enter/Edit chemotherapeutic Drug File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Chem module allows user to enter chemotherapeutic drugs for use in CHEMOTHERAPY \#1-10 fields. Enter generic chemotherapeutic drug name with its NSC number

## RCRS Create RCRS Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to create a RCRS (Rapid Cancer Reporting System) extract file for submission to the ACoS-NCDB (American College of Surgeons – National Cancer Database). This option replaces the Create RQRS Extract option (see below).

*RQRS Create RQRS Extract*

This option created an RQRS (Rapid Quality Response System) extract. The RQRS option has been obsolete since it was replaced by RCRS in 2020.

## TEXT Find Non-Standard characters in TEXT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will show users non-standard characters which occur in any TEXT field. The user can select a Patient Name or specific Primary Record and the option will search text fields and display any fields with non-standard characters.

## UPC Update Oncology Physician Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will allow the user to add, edit or delete Oncology physician type contacts. Previously the user could add physician contacts in the Abstract Edit Primary option when entering the Managing Physician, Following Physician and Primary Surgeon fields. This is no longer allowed and physician contacts must be added in this option.

## VL Check Validity of TNM Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will display a list of patients with invalid data in the Clinical and

Pathologic TNM fields. This is for use after the data conversion with the implementation of NAACCR Vol II v16. This will allow users to see any problematic data in the TNM fields.

<span id="_Toc168391332" class="anchor"></span>Reporting to VA Central Cancer Registry

End users no longer manually report to VACCR; this process is now automated.

# Utility Tools 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PC Capture Program

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions to Upload XML files to your State, RCRS, NCDB

*(Using a state file upload as example)*Vista Oncology Reflections: you will need to have the correct Reflections version of VISTA in order to export and save this report. To check if you have the correct version, look at the top menu when you log into Vista/ Oncotrax. The top menu should look like this:

Specifically, look to see if you have the icons that look like a camera and a stop sign on the far right (circled in red above). Be sure to check this each time you are preparing to create an xml file – *sometimes facilities will do Vista updates that may remove this version of Reflections, so always look for the icons*. If you do not have these, you will not be able to export files from Oncotrax and will need to re-install Reflections. If you do not have these, you will need to re-install Reflections.

Instructions to set up are here: Reflections Set Up

In order to submit a file to your state, you need to execute these steps:

1. Create the file in Oncotrax using v22 (or higher/current) menu option, using the Capture buttons to save it2. Remove the extra line/ character at the end of the file3. Convert the file to xml format

For state (and other) uploads, you should be tracking each upload and which field that you used to select records. Use the same field, otherwise your reports will not be consistent. Most states do not want records to be re-submitted because this requires more labor on their side to determine if there are differences in subsequent record submission and if those changes are relevant for them (most states focus on incidence and do not track follow up information). If your state does want records to be re-submitted with follow up updates, you will also need to track those (and use the Date Case Last Changed option to re-submit cases that have updates – see below).

1. Create the file in Oncotrax using v22 (or higher/current) menu option, and use the Capture buttons to save it

In Oncotrax, from the UTL menu, choose CC, or use ^

^CC Create State Data Download

You will be prompted to select a date field for Start/End range:

Select date field to be used for Start/End range: ??

Select the date field you wish to use for this download's Start/End

range prompts.

Select one of the following:

1 Date Case Completed (recommended)

2 Date Case Last Changed

3 Accession Number

Recommend \#1, unless you know that your state wants updates (then you may opt for \#2) or you have been using Accession Number.

Enter the date range or accession number range *and record this information so that you know how to determine the range next time*.

When prompted for Analytic Cases Only, choose NO unless you know that your state wants analytic cases only. (most state registries are interested in incidence, so they will want your non-analytic cases as well).

Your setting will be displayed, then:

Are these settings correct? YES//

--------------------------------------------------------------

\|Please activate your PC capture program. The data will be \|

\|sent in 2 minutes or when you press the return key. \|

--------------------------------------------------------------

At the menu at top, click on the camera icon to start the Capture, choose your folder and name the file, then hit return key.

The file will run and you will know it is done when you see the upside-down question mark on the last line:

\<Item naaccrId="rxSummSurgPrimSite"\>98\</Item\>

\</Tumor\>

\</Patient\>

\</NaaccrData\>



Click on the Stop Capture button (stop sign icon) to finish the capture.

Oncotrax will now generate a list of patients in the file – you can start and stop a separate capture if you want to capture this list (or you can copy/paste from Oncotrax and save it).

2. Remove the extra line/ character at the end of the file

In File Explorer, find the file, right click on the file, choose Open With, and use NotePad to open the file.

Scroll to the very bottom of the file, place your cursor after the last character (in Oncotrax this appears as an upside-down question mark, but in Notepad it looks like a long rectangle) and backspace twice to remove this character and the hard return, so that your cursor is right behind \</NaaccrData\>.

Save the file and close it.3. Convert the file to xml format

From File Explorer, re-name the file and add the .xml extension: right click on the file, choose Rename, and add .xml to the end of the file name.

Example: if file name is Jan2021state, rename the file to Jan2021state.xml

There may be other possibilities to prepare your file to send to the state (or RCRS, NCDB) – some registrars have tried Wordpad or altered these steps in other ways. If you are able to submit cases to your state or NCDB, then that is the final test, but if you have any problems, please follow above steps.

## Downloading and Installing Genedits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to American College of Surgeon’s NCDB website for instructions on software needed and submission instructions for current year’s Call for data:

[<u>https://www.facs.org/quality-programs/cancer/ncdb</u>](https://www.facs.org/quality-programs/cancer/ncdb)

*VistA Setup*

VistA can be set up in different ways. 

## Line Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are set up with Line Editor in VistA, your screen for entering text can look like the example, TEXT-DX PROC-PE:. The number lines make editing a little difficult.

#### Example of the Line Editor Screen 

![](oncology-version-2-2-user-manual-updated-onc-2-2-22/002.png)

## Screen Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change to a more user-friendly word processing screen. Using the Screen Editor, you are able to move around easily, format your text, and do many things that are impossible with the line editor.

1.  To change to the Screen Editor, type ^EDIT USER CHARACTERISTICS..
21. Tab or arrow down to PREFERRED EDITOR: LINE EDITOR – VA FILEMAN.

![](oncology-version-2-2-user-manual-updated-onc-2-2-22/003.png)

22. Change LINE to SCREEN.

#### Example of the Screen Editor Screen

![](oncology-version-2-2-user-manual-updated-onc-2-2-22/004.png)

You can type in this screen, just like in Microsoft Word or Word Perfect. You are able to change margins, format text, join lines together, cut and paste text, easily delete text, and so on.

Type F1H (H for help) to access word processing Help commands for the Screen Editor.

There are four Help screens to which you can navigate. Use the Arrow keys (to the left of the number pad) to move around the Help screens. Help Screen 3 of 4 is the most useful of the Help screens.

Example of Help Screen 3 of 4

![](oncology-version-2-2-user-manual-updated-onc-2-2-22/005.png)

Example of Help Screen 2 of 4

![](oncology-version-2-2-user-manual-updated-onc-2-2-22/006.png)

## Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you sign on to VistA, your screen may be set up not to display menus. You may want to change your set up options, so that you can see your menu choices.

![](oncology-version-2-2-user-manual-updated-onc-2-2-22/007.png)

1.  At Select OncoTrax: Cancer Registry Option, type ^EDIT USER CHARACTERISTICS.
23. Arrow down to AUTO MENU: and type ? Your options display.

![](oncology-version-2-2-user-manual-updated-onc-2-2-22/008.png)

24. Select 1 YES, MENUS GENERATED.  
    Your menu choices display when you access VistA.

![](oncology-version-2-2-user-manual-updated-onc-2-2-22/009.png)

| Before                                                                                                                                                                                                                      | After                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](oncology-version-2-2-user-manual-updated-onc-2-2-22/010.png) | ![](oncology-version-2-2-user-manual-updated-onc-2-2-22/011.png) |

# Edits within OncoTrax

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If there are inter-field problems, warning messages display when you attempt to change the ABSTRACT STATUS (165.5,91) to Complete  These warning messages are the VistA inter-field edit checks. Some of these warning messages are dependent on the Date DX and might only appear for certain date ranges. You can override these warnings.

| 1   | WARNING: REPORTING HOSPITAL = REFERRING FACILITY                                                                                                                                          |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2   | WARNING: REPORTING HOSPITAL = TRANSFER FACILITY                                                                                                                                           |
| 3   | WARNING: CLASS OF CASE = 2 (Dx ew, 1st rx here) -REFERRING FACILITY may not be blank                                                                                                      |
| 4   | WARNING: CLASS OF CASE = 3 (Dx ew, 1st rx ew) REFERRING FACILITY may not be blank                                                                                                         |
| 5   | WARNING: CLASS OF CASE = 0 (Dx here, 1st rx ew)-DATE OF FIRST CONTACT..: later than SURGERY OF PRIMARY SITE DATE.:                                                                        |
| 6   | WARNING: CLASS OF CASE = 0 (Dx here, 1st rx ew) DATE OF FIRST CONTACT. later than RADIATION DATE...............:                                                                          |
| 7   | WARNING: CLASS OF CASE = 0 (Dx here, 1st rx ew) DATE OF FIRST CONTACT..: later than RADIATION THERAPY TO CNS DATE:                                                                        |
| 8   | WARNING: CLASS OF CASE = 0 (Dx here, 1st rx ew) DATE OF FIRST CONTACT..: later than CHEMOTHERAPY DATE............:                                                                        |
| 9   | WARNING: CLASS OF CASE = 0 (Dx here, 1st rx ew) DATE OF FIRST CONTACT..:                                                                                                                  |
| 10  | WARNING: CLASS OF CASE = 0 (Dx here,  1st rx ew) DATE OF FIRST CONTACT..: later than IMMUNOTHERAPY DATE...........:                                                                       |
| 11  | WARNING: CLASS OF CASE = 0 (Dx here,  1st rx ew) DATE OF FIRST CONTACT..: later than OTHER TREATMENT DATE.........:                                                                       |
| 12  | WARNING: CLASS OF CASE = 2 (Dx ew, 1st rx here) DATE OF FIRST CONTACT..: earlier than DATE DX......................:                                                                      |
| 13  | WARNING: TYPE OF REPORTING SOURCE = 6 (Autopsy only) CLASS OF CASE must be 5 (Dx at autopsy)                                                                                              |
| 14  | WARNING: CLASS OF CASE = 5 (Dx at autopsy) TYPE OF REPORTING SOURCE must be 6 (Autopsy only)                                                                                              |
| 15  | WARNING: TYPE OF REPORTING SOURCE = 6 (Autopsy only) DIAGNOSTIC CONFIRMATION must be 1 (Pos histology) or 6 (Direct visualization)                                                        |
| 16  | WARNING: TYPE OF REPORTING SOURCE = 7 (Death certificate only) DIAGNOSTIC CONFIRMATION must be 9 (Unk if microscopically confirmed)                                                       |
| 17  | WARNING: XXX is a paired site LATERALITY may not be 0 (Not a paired site) \*(this warning excluded for C44.4 melanoma cases)                                                              |
| 18  | WARNING: XXX is an unpaired site LATERALITY must be 0 (Not a paired site) \*(this warning excluded for C44.4 melanoma cases)                                                              |
| 19  | WARNING: BONES, PELVIS, SACRUM, COCCYX is a paired site                                                                                                                                   |
| 20  | WARNING: BEHAVIOR CODE = 2 (In situ) SUMMARY STAGE must be 0 (In situ)                                                                                                                    |
| 21  | WARNING: BEHAVIOR CODE = 3 (Malignant) SUMMARY STAGE may not be  0 (In situ)                                                                                                              |
| 22  | WARNING: HISTOLOGY =  8331 FOLLICULAR ADENOCA, WELL DIFF GRADE/DIFFERENTIATION must be 1 (Grade I)                                                                                        |
| 23  | WARNING: HISTOLOGY =   8851 LIPOSARCOMA, WELL DIFFGRADE/DIFFERENTIATION must be 1 (Grade I)                                                                                               |
| 24  | WARNING: HISTOLOGY = 9511 RETINOBLASTOMA, DIFFERENTIATED GRADE/DIFFERENTIATION must be 1 (Grade I)                                                                                        |
| 25  | WARNING: HISTOLOGY =   9083 TERATOMA, INTERMEDIATE GRADE/DIFFERENTIATION must be 2 (Grade II)                                                                                             |
| 26  | WARNING: HISTOLOGY =   8020 CARCINOMA, UNDIFFERENTIATED GRADE/ DIFFERENTIATION must be 4 (Grade IV)                                                                                       |
| 27  | WARNING: HISTOLOGY =   8021 CARCINOMA, ANAPLASTIC NOS GRADE/DIFFERENTIATION must be 4 (Grade IV)                                                                                          |
| 28  | WARNING: HISTOLOGY =   9062 SEMINOMA, ANAPLASTIC TYPE GRADE/DIFFERENTIATION must be 4 (Grade IV)                                                                                          |
| 29  | WARNING: HISTOLOGY =   9082 TERATOMA, ANAPLASTIC GRADE/DIFFERENTIATION must be 4 (Grade IV)                                                                                               |
| 30  | WARNING: HISTOLOGY =   9390 CHOROID PLEXUS PAPILLOMA GRADE/DIFFERENTIATION must be 4 (Grade IV)                                                                                           |
| 31  | WARNING: HISTOLOGY =   9401 ASTROCYTOMA, ANAPLASTIC GRADE/DIFFERENTIATION must be 4 (Grade IV)                                                                                            |
| 32  | WARNING: HISTOLOGY =   9451 OLIGODENDROGLIOMA, ANAPLASTIC GRADE/DIFFERENTIATION must be 4 (Grade IV)                                                                                      |
| 33  | WARNING: HISTOLOGY =   9512 RETINOBLASTOMA, UNDIFFGRADE/DIFFERENTIATION must be 4 (Grade IV)                                                                                              |
| 34  | WARNING: HISTOLOGY =   9696 LYMPHOMA, LYMPH. POOR DIFF. NOD GRADE/DIFFERENTIATION must be: 3 (Grade III) or 5 (T-cell) or 6 (B-cell)  or 7 (Null cell)                                    |
| 35  | WARNING: HISTOLOGY =   9694 LYMPHOMA, LYMPH. INT. DIFF. NOD GRADE/DIFFERENTIATION must be: -2 (Grade II) or 5 (T-cell) or 6 (B-cell) or7 (Null cell) or 9 (Unknown)                       |
| 36  | WARNING: HISTOLOGY =   9683 LYMPHOMA CENTROBLASTIC DIFFGRADE/DIFFERENTIATION must be: 4 (Grade IV) or5 (T-cell) or 6 (B-cell) or7 (Null cell)                                             |
| 37  | WARNING: GRADE/DIFFERENTIATION = 5 (T-cell) HISTOLOGY must be leukemia or lymphoma (9590-9941)                                                                                            |
| 38  | WARNING: GRADE/DIFFERENTIATION = 6 (B-cell) HISTOLOGY must be leukemia or lymphoma (9590-9941)                                                                                            |
| 39  | WARNING: GRADE/DIFFERENTIATION = 7 (Null cell) HISTOLOGY must be leukemia or lymphoma (9590-9941)                                                                                         |
| 40  | WARNING: GRADE/DIFFERENTIATION = 8 (Natural killer cell) HISTOLOGY must be leukemia or lymphoma (9590-9941)                                                                               |
| 41  | WARNING: No TNM classification is available for LYMPHOMA SUMMARY STAGE cannot be blank                                                                                                    |
| 41  | WARNING: No TNM classification is available for KAPOSI'S SARCOMA SUMMARY STAGE cannot be blank                                                                                            |
| 43  | WARNING: BEHAVIOR CODE = 3 (Malignant) EXTENSION may not be 00 (In situ)                                                                                                                  |
| 44  | WARNING: ICDO-TOPOGRAPHY = XXX PATHOLOGIC EXTENSION = XXX                                                                                                                                 |
| 45  | PATHOLOGIC EXTENSION may only be coded for PROSTATE (C61.9) cases                                                                                                                         |
| 46  | WARNING: NODES POSITIVE (REGIONAL) = 01-97 LYMPH NODES may not be 0 (No lymph nodes)                                                                                                      |
| 47  | WARNING: ICDO-TOPOGRAPHY = XXX HORMONE THERAPY = 2 (Endocrine surgery and/or radiation) Only BREAST and PROSTATE cases may be coded as receiving endocrine surgery or endocrine radiation |
| 48  | WARNING: STATUS = Dead PLACE OF DEATH may not be blank                                                                                                                                    |
| 49  | WARNING: STATUS = Dead CAUSE OF DEATH and STATE DEATH CERT may not both be blank                                                                                                          |
| 50  | WARNING: For race combinations RACE 1 may not be 'White'                                                                                                                                  |
| 51  | WARNING: A specific race code may not occur more than once                                                                                                                                |
| 52  | If REGIONAL NODES EXAMINED is 99 (Unknown if nodes examined, NA), REGIONAL NODES POSITIVE must be 99 (Unk if nodes  + or  -, NA)                                                          |

The following edit sets are used to create the 2022 metafile.

Eod EDITS FOR 2018

Hosp: Vs22 COC Required – All + CS

# Edits within Genedits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Messages display for the Veterans Administration Edits Metafile (Current version of NAACR –Hospital All metafile).

Refer to the NAACCR website for a detail report of these Edit messages:

[<u>https://www.naaccr.org/standard-data-edits/</u>](https://www.naaccr.org/standard-data-edits/)

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th>ACoS</th>
<th>American College of Surgeons</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AJCC</td>
<td>American Joint Committee on Cancer</td>
</tr>
<tr class="even">
<td>API</td>
<td>Application Program Interface</td>
</tr>
<tr class="odd">
<td>COC</td>
<td>Commission on Cancer</td>
</tr>
<tr class="even">
<td>CS</td>
<td>Collaborative Staging</td>
</tr>
<tr class="odd">
<td>DOB</td>
<td>Date of Birth</td>
</tr>
<tr class="even">
<td>DOD</td>
<td>Date of Death</td>
</tr>
<tr class="odd">
<td>EOD</td>
<td>Extent of Disease</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ICD-O</td>
<td>International Classification of Diseases for Oncology</td>
</tr>
<tr class="odd">
<td>NAACCR</td>
<td>North American Association of Central Cancer Registries</td>
</tr>
<tr class="even">
<td>NCDB</td>
<td>National Cancer Data Base</td>
</tr>
<tr class="odd">
<td>NCI</td>
<td>National Cancer Institute</td>
</tr>
<tr class="even">
<td>NCRA</td>
<td>National Cancer Registrars Association</td>
</tr>
<tr class="odd">
<td>NPCR</td>
<td>National Program of Cancer Registries</td>
</tr>
<tr class="even">
<td>PID#</td>
<td>Patient Identification Number<br />
First initial of the last name plus the last four digits of the SSN: W9999</td>
</tr>
<tr class="odd">
<td>PTF</td>
<td>Patient Treatment File</td>
</tr>
<tr class="even">
<td>Report 80C</td>
<td>Report contains 80 columns and requires a printer that prints 80 columns</td>
</tr>
<tr class="odd">
<td>Report 132C</td>
<td>Report contains 132 columns and requires a printer that prints 132 columns; on screen the text wraps.</td>
</tr>
<tr class="even">
<td>SEER</td>
<td>Surveillance, Epidemiology and End Results</td>
</tr>
<tr class="odd">
<td>SNOMED</td>
<td>Systematized Nomenclature of Medicine</td>
</tr>
<tr class="even">
<td>SSN</td>
<td>Social Security Number</td>
</tr>
<tr class="odd">
<td>TNM</td>
<td>Primary <u>T</u>umor, Regional Lymph <u>N</u>odes, Distant <u>M</u>etastasis</td>
</tr>
<tr class="even">
<td>VACCR</td>
<td>VA Central Cancer Registry</td>
</tr>
<tr class="odd">
<td>VISN</td>
<td>Veterans Integrated Service Network</td>
</tr>
</tbody>
</table>

# Appendix A: Edits API 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instituted May 2007 with OncoTrax: Cancer Registry V.2.11 - Patch ONC\*2.11\*47 Released May 17, 2007

#### Description:

This patch will implement the EDITS API.

When the registrar attempts to set the ABSTRACT STATUS (#165.5,91) to 3 (Complete), three things will occur:

1.  The program will first check to make sure that all of the "required" data items have been filled in. This is currently being done.
25. Once all of the "required" data items have been filled in, the program will pass the abstract through a series of local inter-field edit checks. This is also currently being done.
26. Once all of the local inter-field edit checks have been resolved (or overridden), the program will invoke the EDITS API and pass the abstract through the EDITS application. This feature is new with this patch.
27. NOTE: With patch ONC\*2.2\*16, VistA Oncology will utilize the VistA HealtheVet Web Services Client (HWSC) to allow Hypertext Transfer Protocol Secure (https) encrypted connections to the EDITS API application.

#### Example:

ABSTRACT STATUS: Incomplete// Complete

All required data fields have been entered.

Beginning inter-field edit checks...

No inter-field edit check warnings.

Calling EDITS API... \<--new with this patch

If the EDITS API encounters errors the error messages will be displayed followed by the following message:

EDITS errors were encountered. ABSTRACT STATUS is unchanged.

#### Example:

Calling EDITS API...

Date of Last Contact, Date of Diag. (NAACCR IF19)

E:Date of Diagnosis and Date of Last Contact conflict

Date of Diagnosis (283) = 12092004

Date of Last Contact (1294) = 09052003

RETURN to continue, '^' to exit, or Edit# for help:

Edit Set Errors Warnings

--------------------------------------------------------------------

Veterans Administration 1 0

EDITS errors were encountered. ABSTRACT STATUS is unchanged.

--------------------------------------------------------------------

> **NOTE:** Each error will be numbered sequentially. If the registrar wishes to see additional information about a specific error, he/she may enter the sequential error number after the "RETURN to continue, '^' to exit, or Edit# for help:" prompt for additional error information.

If EDITS errors are encountered, the registrar should then review the error messages and resolve any data conflicts.

If the EDITS API does not encounter any errors the program will do the following:

- ABSTRACT STATUS will be set to 3 (Complete).
- A unique checksum value will be computed for the abstract.
- DATE CASE COMPLETED will be set to the current date.
- ABSTRACTED BY will be set to the registrar who 'completed' the abstract.

The following messages will be displayed:

No EDITS errors or warnings.

ABSTRACT STATUS.......: Complete

DATE CASE COMPLETED...: 03/21/2007

ABSTRACTED BY.........: REGISTAR,TEST

DATE CASE LAST CHANGED:

CASE LAST CHANGED BY..:

Computing checksum value for this abstract...

Once an abstract has successfully passed through the EDITS API and its ABSTRACT STATUS set to 3 (Complete), if the registrar makes a change which will affect the abstract's NAACCR record, he/she will see the following message:

You have made a change to a 'Completed' abstract.

This abstract needs to be re-run through the EDITS API.

Calling EDITS API...

If no EDITS errors are encountered the registrar will see the following message:

No EDITS errors or warnings. ABSTRACT STATUS = 3 (Complete).

If EDITS errors are encountered the registrar will see the following message:

EDITS errors were encountered.

The ABSTRACT STATUS has been changed to 0 (Incomplete).

Each time a 'complete' abstract is changed the abstract will be date-stamped with the date of the most recent change and the name of registrar making the change.

Index

A

AA 36

AAR 39

ABS 18

Abstract

Add a second primary 24

Add new patient 19

Complete 18

Edit a primary 26

Edit an existing primary 23

Edit existing patient 20

Enter a new primary 23

Enter a primary 22

Enter first primary 22

Occupations not included 22

Patient summary 27

Print complete 27

Print extended 27

Print not complete list 26

Print QA 27

Print QA/multiple 27

Screens menu 27

Start 19

Status 25

ACL 40

ACT 43

AE 37

AI 18

ANN 39

Annual reporting

ACoS Accession Register 39

ACoS patient index 39

Cross tabs 43

Histology/site/topography 42

ICDO topography/stage/tx 40

Patient list by class of case 40

Primary site/GP listing 40

Primary site/stage/tx 40

Print custom reports 43

Status/site/dx-age 42

API 39

AR 49

AS 27, 37

ASL 40

C

Case Finding

Radiology search 12

Case Finding

Lab search 10

Print lab report 11

Case Finding

PTF search 12

CC 49

CF 10

Character

// 4

? 4

?? 4

^ 4

\<ret\> 4

CPR 43

CT 49

D

Define cancer registry parameters 8

Define parameters 7

Delete Oncology Patient 49

DF 30

Downloading

Genedits 54

DP 49

DS 44, 49

E

EA 49

Edit user characteristics 56

Edits

Genedits 65

Interfield problems 62

OncoTraX 62

Warning messages 62

EE 26

EX 27

F

FH 30

FOL 28

Follow-up

Edit letter 33

Generate letter 31

History 30

Letter 31

Letter edit screen 34

Letter example 35

Post/edit 28

Print delinquent list 30

Print list by month due 30

Procedures menu 31

Recurrence/sub tx 29

Send letter 32

FP 31

G

Genedits

Downloading 54

H

Help screens 58

HIS 42

I

IN 38

Installing

Genedits 54

IR 27

IW 38

L

LF 30

Line editor example 55

LIS 36

LR 11

M

MA 27

Menu options 60

Module

Abstract entry and printing 18

Annual reporting 39

Case finding and suspense 10

Follow-up 28

Registry lists 36

Statistical reporting 44

N

NC 26

NP 17

O

Oncology menu 6

OncoTraX conventions 4

OncoTraX menu 6

P

PA 27, 37

PE 37

PF 28

PS 37

PT 12

Q

QA 27

R

RA 12

Recommended websites 3

Registry

Accession Register-ACoS 36

Accession Register-EOVA 37

Accession Register-Site 37

Patient index-ACoS 37

Patient index-EOVA 37

Patient index-site 37

Primary ICDO listing 38

Primary site/GP listing 38

Related manuals 2

RF 29

RS 47

S

Screen editor example 57

SDX 42

SE 15

Search criteria

SP 45

SS 46

Survival by site 45

Survival by stage 46

Survival by treatment 46

TX 46

SG 38

SP 16

SR 49

SST 40

STA 44

Statistical reporting

Define search criteria 44

Treatment by stage-cross tabs 46

SUS 10

Suspense

Add a VA patient 15

Delete a VA patient 16

Edit a VA patient 16

Patients with no primaries 17

Print list by suspense date 16

Suspense date 10

T

TIME 51

TNM 50

TR 50

TS 46

TST 40

U

Utility options

Compute percentage of TNM forms completed 50

Create a report to preview ACoS output 49

Create a report to preview state/VACCR output 49

Create ACoS data download 49

Create state VACCR data download 49

Define cancer registry parameters 50

Delete patient 49

Delete primary site/Gp record 49

Edit site/AccSeq# data 49

Registry summary reports 47

Timeliness report 51

V

VistA conventions 4

*VistA setup* 54

Line editor 54

Screen editor 56