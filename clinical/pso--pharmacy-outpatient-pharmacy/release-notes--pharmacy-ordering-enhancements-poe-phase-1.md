---
title: Pharmacy Ordering Enhancements (POE) Phase 1 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: plain
doc_subject: Pharmacy Ordering Enhancements (POE) Phase 1
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
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
  - table
  - contents
  - mark
  - blockquote
  - installation
  - install
  - patch
  - redacted
  - report
  - medication
page_count: 0
word_count: 833
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2000
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pdm1p34_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pdm1p34_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

> ![](pharmacy-ordering-enhancements-poe-phase-1-release-notes/001.png)

> Pharmacy Ordering Enhancements (POE) Pharmacy Data Management (PDM) Pre-Release PSS\*1\*34

> Release Notes and Installation Guide

> October 2000

## Department of Veterans Affairs 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> V*IST*A Technical Services

# Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Department of Veterans Affairs](#department-of-veterans-affairs)
- [Purpose](#purpose)
    - [Before these associated patches can be installed at the facilities, the work required by the POE PDM Pre-Release patch PSS\1\34 must be completed.](#before-these-associated-patches-can-be-installed-at-the-facilities-the-work-required-by-the-poe-pdm-pre-release-patch-pss134-must-be-completed)
- [Scope](#scope)
- [Release Notes](#release-notes)
- [Pre-Installation](#pre-installation)
    - [Patch Requirements](#patch-requirements)
- [Installation](#installation)
    - [Example of PSS\1\34 Installation:](#example-of-pss134-installation)
- [Post-Installation](#post-installation)
> The purpose of this document is to provide installation instructions for the Pharmacy Ordering Enhancements (POE) Pharmacy Data Management (PDM) Pre-Release patch PSS\*1\*34. This POE PDM Pre-Release patch for the Pharmacy Data Management V. 1.0 package creates new fields and provides reports and options to assist in the population and maintenance of data necessary for the installation of associated Inpatient Medications V. 5.0, Outpatient Pharmacy V.
> 7.0 and Computerized Patient Record System (CPRS) patches.

### Before these associated patches can be installed at the facilities, the work required by the POE PDM Pre-Release patch PSS\*1\*34 must be completed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Computerized Patient Record System (CPRS) Clinical Workgroup (the Workgroup) requested changes in the pharmacy medication ordering dialogues in order to eliminate the need for redundant entry of drug information during medication order entry and to improve the process for transferring orders between Inpatient and Outpatient medicine applications.

> Additional enhancement requests from the Workgroup were to provide order checks for all medication orders entered through CPRS and to provide drug specific information during medication order entry.

> Currently, the CPRS/Pharmacy order dialogues require the selection of a medication (orderable item), then the selection of a Dispense Drug that contains a strength associated with the selected medication, and then the entry of a dosage of the medication to be given to the patient. The Workgroup requested that these duplicate entries be consolidated to eliminate redundancy. A standard ordering dialogue for the entry of medication orders into either the Inpatient Medications or Outpatient Pharmacy applications was also requested in order to improve the process for the transfer of medication orders between the two applications.

> In CPRS, order checks are currently based on the Dispense Drug that is selected as part of the order. Therefore, for both Inpatient and Outpatient orders entered through CPRS, order checks do not occur if a Dispense Drug is not selected during the CPRS ordering process. Though a Dispense Drug will no longer be selected during this ordering process, a dosage will be selected. Although not visible to the CPRS user, each dosage is associated with a Dispense Drug, and order checks are based on the Dispense Drug associated with the selected dosage. If a dosage is not selected from the available dosage list, and instead a dosage is typed in as a free text entry, the order checks will be based on all of the Dispense Drugs matched to the selected orderable item. Therefore, order checks will now be performed on all Inpatient and Outpatient orders that are entered through CPRS.

> Currently, there are no dosage values associated with Outpatient prescriptions that can be used for dosage range checks. By adding dosage information to Outpatient prescriptions, dosage range checks can be available in the near future for the medication order entry and finishing processes.

> The POE PDM Pre-Release patch creates new fields, reports and options to assist in the population and maintenance of data necessary for the future Inpatient Medications, Outpatient Pharmacy and CPRS patches that comprise the upcoming Pharmacy Ordering Enhancements project. All of the options released in this patch will reside under the *Ordering Enhancements Pre-Release* \[PSS DOSAGE PRE-RELEASE\] menu option, which is located under the *Pharmacy Data Management* \[PSS MGR\] menu.

# Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following options have been added to the Pharmacy Data Management package. These options enable the Pharmacy staff to set up their Pharmacy files in preparation of the upcoming Pharmacy Ordering Enhancements release. A brief description is provided here; more detailed examples are provided in the POE PDM Pre-Release Implementation Guide. Instructions concerning where to locate the POE PDM Pre-Release Implementation Guide are located in the Post-Installation section of this document.

#### Ordering Enhancements Pre-Release

> \[PSS DOSAGE PRE-RELEASE\]

> This menu contains the options necessary for set up of the POE PDM Pre-Release patch.

#### Auto Rematch IV Additives/Solutions Report

> \[PSS ADDITIVE/SOLUTION REPORT\]

> This report shows how the Additive and Solutions will be rematched to new orderable items, based on their Dispense Drug link.

#### Corresponding Drug

> \[PSS CORRESPONDING DRUG MENU\]

> This menu provides the options for review of the Corresponding Inpatient Drug and Corresponding Outpatient Drug functionality.

#### Enter/Edit Corresponding Drug

> \[PSS CORRESPONDING DRUG EDIT\]

> This option provides the ability to mark Corresponding Inpatient Drugs and Corresponding Outpatient Drugs.

#### Mark Corresponding Drugs

> \[PSS CORRESPONDING DRUG MARK\]

> This option provides the ability to mark all Corresponding Inpatient Drugs and Corresponding Outpatient Drugs based on the potential matches that are displayed in the *Report of Corresponding Drugs* \[PSS CORRESPONDING DRUG REPORT\].

October 2000 Pharmacy Ordering Enhancements 3

> Pharmacy Data Management Pre-Release PSS\*1\*34

> Release Notes and Installation Guide

#### Report of Corresponding Drugs

> \[PSS CORRESPONDING DRUG REPORT\]

> This report shows which drugs are currently marked as Corresponding Inpatient Drugs and Corresponding Outpatient Drugs in the DRUG file (#50). It also shows potential matches that can be achieved by using the *Mark Corresponding Drugs* \[PSS CORRESPONDING DRUG MARK\] option.

#### Dosages

> \[PSS DOSAGES SUB-MENU\]

> These are the options used to create, view, enter and edit dosages.

#### Auto Create Dosages

> \[PSS DOSAGE CONVERSION\]

> This option is used to populate the POSSIBLE DOSAGES fields and LOCAL POSSIBLE DOSAGE fields in the DRUG file (#50).

#### Conversion Tracker

> \[PSS DOSAGE CONVERSION TRACKER\]

> This option provides the ability to track when the last dosage conversion was run.

#### Dosages Enter/Edit

> \[PSS EDIT DOSAGES\]

> This option allows the POSSIBLE DOSAGES fields and LOCAL POSSIBLE DOSAGE fields for a selected Dispense Drug to be edited.

#### Most Common Dosages Report

> \[PSS COMMON DOSAGES\]

> This report displays the most common dosages ordered over a specified time period for Unit Dose orders.

#### Review Dosages Report

> \[PSS DOSAGE REVIEW REPORT\]

> This report shows the Possible Dosages and Local Possible Dosages for selected Dispense Drugs.

#### Instructions/Nouns

> \[PSS INSTRUCTIONS/NOUNS\]

> These options provide the functionality to populate and control the NOUN fields in the DOSAGE FORM file (#50.606).

#### Convert Instructions to Nouns

> \[PSS CONVERT INSTRUCTIONS\]

> This option allows the conversion of all non-numeric instructions to NOUNS in the DOSAGE FORM file (#50.606).

#### Dosage Form/Noun Report

> \[PSS DOSE FORM/NOUN REPORT\]

> This report displays the DOSAGE FORMS, along with their associated NOUN and PACKAGE fields. It also displays the Local Possible Dosage based on the NOUN.

#### Instructions to Noun Conversion Report

> \[PSS INSTRUCTIONS REPORT\]

> This report displays the instructions associated with each dosage form. The non-numeric instructions can be converted to the NOUN field by using the *Convert Instructions to Nouns* \[PSS CONVERT INSTRUCTIONS\] option.

#### Nouns Enter/Edit

> \[PSS ENTER/EDIT NOUNS\]

> This option allows the entering and editing of Nouns and their associated NOUN fields in the DOSAGE FORM file (#50.606).

#### Med Instruction/Frequency

> \[PSS MED INSTRUCTION FREQUENCY\]

> This menu provides the *Med Instruction/Frequency* \[PSS MED INSTRUCTION FREQUENCY\] menu options.

#### Edit Medication Instruction Frequency

> \[PSS EDIT INSTRUCTION FREQUENCY\]

> This option provides the ability to edit data in the FREQUENCY (IN MINUTES) field in the MEDICATION INSTRUCTION file (#51). This data will be used for calculating default QUANTITY and DAYS SUPPLY values for Outpatient Pharmacy orders.

#### Medication Instruction Frequency Report

> \[PSS FREQUENCY REPORT\]

> This report displays information from the MEDICATION INSTRUCTION file (#51). It can be used to help determine which instructions can have a valid frequency.

#### Medication Routes/IV Flag

> \[PSS MEDICATION ROUTES SUB-MENU\]

> These options affect the new IV Flag indicator in the MEDICATION ROUTES file (#51.2).

#### Edit Medication Route IV Flag

> \[PSS EDIT MED ROUTE IV FLAG\]

> This option allows the editing of the IV Flag in the MEDICATION ROUTES file (#51.2).

#### Flag Medication Routes as IV

> \[PSS FLAG MED ROUTES AS IV\]

> This option is used to automatically populate the IV FLAG field in the MEDICATION ROUTES file (#51.2) for all routes that are associated with an IV Flagged Orderable Item or contained in Quick Codes in the IV ADDITIVES file (#52.6).

#### Medication Routes flagged for IV Report

> \[PSS MEDICATION ROUTES REPORT\]

> This report shows the Medication Routes, their abbreviations, the package use, and the IV Flag status of the Medication Route. The IV Flag helps determine how Inpatient Medication Orders entered through CPRS are finished in the Inpatient Medications package.

#### Patient Instructions Enter/Edit

> \[PSS PATIENT INSTRUCTIONS\]

> This option provides the ability to edit the PATIENT INSTRUCTIONS field in the PHARMACY ORDERABLE ITEM file (#50.7).

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Patch Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before installing the POE PDM Pre-Release patch PSS\*1\*34, the following patches must be installed:

> PSS\*1\*13 PSS\*1\*28 PSS\*1\*32 PSN\*4\*33 PSO\*7\*41

> If these patches have not been installed, contact your Information Resources Management Staff (IRM) for assistance.

> It is recommended that this patch be installed into the test account initially in order to test the installation process and to do some preliminary familiarization with the functionality. The extensive work required for this setup can be accomplished in the production account since these changes will not affect the current functionality of any associated applications until the Outpatient Pharmacy, Inpatient Medications, and CPRS patches are installed. Therefore, it is recommended that after the installation of the POE PDM Pre-Release patch PSS\*1\*34 into the test account, the setup be performed in the production account and a mirror of the production account be made in the test account prior to the installation of the subsequent Pharmacy Ordering Enhancements patches.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before installing this patch, use the TaskMan option List Tasks \[XUTM INQ\] to list currently running tasks. Do not install this patch while Pharmacy Data Management users are using the software. Installation will take no longer than 5 minutes. There are no scheduling restrictions or recommendations.

1.  Use the *INSTALL/CHECK MESSAGE* option on the PackMan menu.
2.  Review your mapped set. If the routines are mapped, they should be removed from the mapped set at this time.
3.  From the *Kernel Installation & Distribution System* menu, select the *Installation* menu.
4.  From this menu, you may select to use the following options: (when prompted for INSTALL NAME, enter PSS\*1.0\*34)
    1.  *Backup a Transport Global* - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.
    2.  *Compare Transport Global to Current System* - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
    3.  *Verify Checksums in Transport Global* - this option will ensure the integrity of the routines that are in the transport global.
5.  Use the *Install Package(s)* option and select the package PSS\*1.0\*34.
6.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//” respond NO.
7.  When Prompted “Want KIDS to INHIBIT LOGONs during the install? YES//” respond

> NO.

8.  When Prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//” respond NO.

> (Example of install is displayed on the following page.)

### Example of PSS\*1\*34 Installation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Kernel Installation & Distribution System Option: <u>Ins</u>tallation

> Select Installation Option: <u>Ins</u>tall Package(s)

> Select INSTALL NAME: <u>PSS\*1.0\*34</u> Loaded from Distribution 4/27/00@12:49:40

> =\> PSS\*1\*34

> This Distribution was loaded on Apr 27, 2000@12:49:40 with header of PSS\*1\*34

> It consisted of the following Install(s): PSS\*1.0\*34

> Checking Install for Package PSS\*1.0\*34

> Install Questions for PSS\*1.0\*34

> Incoming Files:

50. DRUG (Partial Definition) Note: You already have the 'DRUG' File.

> 50.606 DOSAGE FORM (Partial Definition) Note: You already have the 'DOSAGE FORM' File.

> 50.7 PHARMACY ORDERABLE ITEM (Partial Definition) Note: You already have the 'PHARMACY ORDERABLE ITEM' File.

51. MEDICATION INSTRUCTION (Partial Definition) Note: You already have the 'MEDICATION INSTRUCTION' File.

> 51.2 MEDICATION ROUTES (Partial Definition) Note: You already have the 'MEDICATION ROUTES' File.

> 59.7 PHARMACY SYSTEM (Partial Definition) Note: You already have the 'PHARMACY SYSTEM' File.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// <u>NO</u>

> Want KIDS to INHIBIT LOGONs during the install? YES// <u>NO</u>

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <u>NO</u>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enter the Device you want to print the Install messages.</p>
<p>You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.</p>
<p>DEVICE: HOME// <strong><u>&lt;RET&gt;</u></strong> DECSERVER</p>
<blockquote>
<p>Install Started for PSS*1.0*34 :</p>
<p>Apr 27, 2000@12:51:40</p>
</blockquote>
<p>Build Distribution Date: Apr 27, 2000 Installing Routines:</p>
<blockquote>
<p>Apr 27, 2000@12:51:43</p>
<p>Installing Data Dictionaries:</p>
<p>Apr 27, 2000@12:51:46</p>
<p>Installing PACKAGE COMPONENTS: Installing OPTION</p>
<p>Apr 27, 2000@12:51:50</p>
<p>PSS*1.0*34</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>---</p>
<p>Running Post-Install Routine: ^PSSPOST1 Updating Dosage Form file with data...</p>
<p>Initializing new data fields... Updating current Dosage Form fields...</p>
<blockquote>
<p>Updating Routine file... Updating KIDS files...</p>
<p>PSS*1.0*34 Installed.</p>
<p>Apr 27, 2000@12:51:51</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>+------------------------------------------------------------+ 100% | 25 50 75 | Complete +------------------------------------------------------------+</p>
<p>Install Completed</p></td>
</tr>
</tbody>
</table>

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch does not affect the current functionality of the Outpatient Pharmacy V. 7.0, Inpatient Medications V. 5.0, or Computerized Patient Record System V. 1.0, but instead provides the necessary functionality for later Pharmacy Ordering Enhancements patches. After this initial POE PDM Pre-Release patch is released and the Pharmacy files have been appropriately updated, another Pharmacy Data Management patch will be released which will delete the options that are no longer needed. Any new options that are still needed will be incorporated into the current Pharmacy Data Management menu.

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 33%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>OI FIELD OFFICE</p>
</blockquote></th>
<th><blockquote>
<p>FTP ADDRESS</p>
</blockquote></th>
<th><blockquote>
<p>DIRECTORY</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>===============</p>
</blockquote></td>
<td><blockquote>
<p>===========</p>
</blockquote></td>
<td><blockquote>
<p>=========</p>
</blockquote></td>
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

October 2000 Pharmacy Ordering Enhancements 11

> Pharmacy Data Management Pre-Release PSS\*1\*34

> Release Notes and Installation Guide