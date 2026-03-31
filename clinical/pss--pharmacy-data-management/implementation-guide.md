---
title: Pharmacy Ordering Enhancements (POE) Pre-Release Implementation Guide
doc_type: IG-IMP
doc_label: Implementation Guide
doc_layer: plain
doc_subject: Pharmacy Ordering Enhancements (POE) Pre-Release
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this POE PDM Pre-Release patch is to prepare sites for the upcoming release of the Pharmacy Ordering Enhancements patches. The new PDM options provide sites the necessary functionality to manipulate data in the Pharmacy files in preparation for the subsequent POE release. The packages
audience: 
keywords: 
  - drug
  - dosages
  - dosage
  - possible
  - inpatient
  - dextrose
  - pharmacy
  - dispense
  - dose
  - diagram
page_count: 0
word_count: 18436
section_count: 3
table_count: 17
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pdm1p34_impg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pdm1p34_impg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

# ![](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/001.png)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [![](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/001.png)](#pharmacy-ordering-enhancements-poe-pre-release-implementation-guide001png)
- [# Pharmacy Ordering Enhancements (POE)](#pharmacy-ordering-enhancements-poe)
- [Pharmacy Data Management (PDM V. 1.0) Pre-Release](#pharmacy-data-management-pdm-v-10-pre-release)
- [Implementation Guide](#implementation-guide)
- [# # # Scope](#scope)
- [Release Notes](#release-notes)
- [Medication Routes/IV Flag \[PSS MEDICATION ROUTES SUB-MENU\]](#medication-routesiv-flag-pss-medication-routes-sub-menu)
- [Edit Medication Route IV Flag \[PSS EDIT MED ROUTE IV FLAG\]](#edit-medication-route-iv-flag-pss-edit-med-route-iv-flag)
- [Menu](#menu)
  - [Overview](#overview)
  - [Options](#options)
- [Diagram B](#diagram-b)
- [Diagram C](#diagram-c)
- [Diagram D](#diagram-d)
- [Diagram E](#diagram-e)
- [Diagram G](#diagram-g)
- [Diagram H](#diagram-h)
    - [Example: Local Possible Dosages for Topical Products](#example-local-possible-dosages-for-topical-products)
- [Diagram J](#diagram-j)
- [# ![](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/011.png)](#pharmacy-ordering-enhancements-poe-pre-release-implementation-guide011png)
- [# Diagram J](#diagram-j-1)
- [Diagram K](#diagram-k)
- [Diagram K2](#diagram-k2)
- [Multi-Ingredient Drugs](#multi-ingredient-drugs)
- [Diagram M](#diagram-m)
- [![Diagram M](#diagram-m-1)
- [Diagram Q](#diagram-q)
- [![Diagram Q](#diagram-q-1)
- [Medication Routes IV Flag Setup](#medication-routes-iv-flag-setup)
- [# New Options with Examples](#new-options-with-examples)
    - [Example 1: Initial Creation of Dosages](#example-1-initial-creation-of-dosages)
    - [Example 2: Dosage Conversion Queued to Run](#example-2-dosage-conversion-queued-to-run)
    - [Example 3: Dosage Conversion Currently Running](#example-3-dosage-conversion-currently-running)
    - [### Example 4: Dosage Conversion Complete](#example-4-dosage-conversion-complete)
    - [Example: Most Common Dosages Report](#example-most-common-dosages-report)
- [Medication Routes/IV Flag \[PSS MEDICATION ROUTES SUB-MENU\]](#medication-routesiv-flag-pss-medication-routes-sub-menu-1)
- [Edit Medication Route IV Flag \[PSS EDIT MED ROUTE IV FLAG\]](#edit-medication-route-iv-flag-pss-edit-med-route-iv-flag-1)
    - [### Example: Medication Routes flagged for IV Report](#example-medication-routes-flagged-for-iv-report)
- [DIGOXIN 0.125MG TAB](#digoxin-0125mg-tab)

# # Pharmacy Ordering Enhancements (POE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Pharmacy Data Management (PDM V. 1.0) Pre-Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Implementation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

October 2000

V*IST*A Technical Services

# # # # Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System (CPRS) Clinical Workgroup (the Workgroup) requested changes in the pharmacy medication ordering dialogues in order to eliminate the need for redundant entry of drug information during medication order entry and to improve the process for transferring orders between Inpatient and Outpatient medicine applications. Additional enhancement requests from the Workgroup were to provide order checks for all medication orders entered through CPRS and to provide drug specific information during medication order entry.

Currently, the CPRS/Pharmacy order dialogues require the selection of a medication (orderable item), then the selection of a Dispense Drug that contains a strength associated with the selected medication, and then the entry of a dosage of the medication to be given to the patient. The Workgroup requested that these duplicate entries be consolidated to eliminate redundancy. A standard ordering dialogue for the entry of medication orders into either the Inpatient Medications or Outpatient Pharmacy applications was also requested in order to improve the process for the transfer of medication orders between the two applications.

In CPRS, order checks are currently based on the Dispense Drug that is selected as part of the order. Therefore, for both Inpatient and Outpatient orders entered through CPRS, order checks do not occur if a Dispense Drug is not selected during the CPRS ordering process. Though a Dispense Drug will no longer be selected during this ordering process, a dosage will be selected. Although not visible to the CPRS user, each dosage is associated with a Dispense Drug, and order checks are based on the Dispense Drug associated with the selected dosage. If a dosage is not selected from the available dosage list, and instead a dosage is typed in as a free text entry, the order checks will be based on all of the Dispense Drugs matched to the selected orderable item. Therefore, order checks will now be performed on all Inpatient and Outpatient orders that are entered through CPRS.

Currently, there are no dosage values associated with Outpatient prescriptions that can be used for dosage range checks. By adding dosage information to Outpatient prescriptions, dosage range checks can be available in the near future for the medication order entry and finishing processes.

# Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options have been added to the Pharmacy Data Management package. These options enable the Pharmacy staff to set up the local Pharmacy files in preparation of the upcoming Pharmacy Ordering Enhancements release. A brief description is provided here; more detailed examples are provided in the New Options with Examples section of this document.

> *Ordering Enhancements Pre-Release*  
> \[PSS DOSAGE PRE-RELEASE\]

> This menu contains the options necessary for set up of the POE PDM Pre-Release patch.

> *Auto Rematch IV Additives/Solutions Report*  
> \[PSS ADDITIVE/SOLUTION REPORT\]

> This report shows how the Additive and Solutions will be rematched to new orderable items, based on their Dispense Drug link.

*Corresponding Drug  
*\[PSS CORRESPONDING DRUG MENU\]

> This menu provides the options for review of the Corresponding Inpatient Drug and Corresponding Outpatient Drug functionality.

*Enter/Edit Corresponding Drug  
*\[PSS CORRESPONDING DRUG EDIT\]

> This option provides the ability to mark Corresponding Inpatient Drugs and Corresponding Outpatient Drugs.

*Mark Corresponding Drugs  
*\[PSS CORRESPONDING DRUG MARK\]

> This option provides the ability to mark all Corresponding Inpatient Drugs and Corresponding Outpatient Drugs based on the potential matches that are displayed in the *Report of Corresponding Drugs* \[PSS CORRESPONDING DRUG REPORT\].

> *Report of Corresponding Drugs*  
> \[PSS CORRESPONDING DRUG REPORT\]

> This report shows which drugs are currently marked as Corresponding Inpatient Drugs and Corresponding Outpatient Drugs in the DRUG file (#50). It also shows potential matches that can be achieved by using the *Mark Corresponding Drugs* \[PSS CORRESPONDING DRUG MARK\] option.

> *Dosages*  
> \[PSS DOSAGES SUB-MENU\]

> These are the options used to create, view, enter and edit dosages.

> *Auto Create Dosages  
> *\[PSS DOSAGE CONVERSION\]

This option is used to populate the POSSIBLE DOSAGES fields and LOCAL POSSIBLE DOSAGE fields in the DRUG file (#50).

> *Conversion Tracker*  
> \[PSS DOSAGE CONVERSION TRACKER\]

This option provides the ability to track when the last dosage conversion was run.

> *Dosages Enter/Edit*  
> \[PSS EDIT DOSAGES\]

This option allows the POSSIBLE DOSAGES fields and LOCAL POSSIBLE DOSAGE fields for a selected Dispense Drug to be edited.

> *Most Common Dosages Report*  
> \[PSS COMMON DOSAGES\]

> This report displays the most common dosages ordered over a specified time period for Unit Dose orders.

> *Review Dosages Report*  
> \[PSS DOSAGE REVIEW REPORT\]

> This report shows the Possible Dosages and Local Possible Dosages for selected Dispense Drugs.

*Instructions/Nouns*  
\[PSS INSTRUCTIONS/NOUNS\]

These options provide the functionality to populate and control the NOUN fields in the DOSAGE FORM file (#50.606).

> *Convert Instructions to Nouns  
> *\[PSS CONVERT INSTRUCTIONS\]

> This option allows the conversion of all non-numeric instructions to NOUNS in the DOSAGE FORM file (#50.606).

> *Dosage Form/Noun Report*  
> \[PSS DOSE FORM/NOUN REPORT\]

> This report displays the DOSAGE FORMS, along with their associated NOUN and PACKAGE fields. It also displays the Local Possible Dosage based on the NOUN.

> *Instructions to Noun Conversion Report  
> *\[PSS INSTRUCTIONS REPORT\]

> This report displays the instructions associated with each dosage form. The non-numeric instructions can be converted to the NOUN field by using the *Convert Instructions to Nouns* \[PSS CONVERT INSTRUCTIONS\] option.

> *Nouns Enter/Edit*  
> \[PSS ENTER/EDIT NOUNS\]

> This option allows the entering and editing of Nouns and their associated NOUN fields in the DOSAGE FORM file (#50.606).

> *Med Instruction/Frequency*  
> \[PSS MED INSTRUCTION FREQUENCY\]

> This menu provides the *Med Instruction/Frequency* \[PSS MED INSTRUCTION FREQUENCY\] menu options.

> *Edit Medication Instruction Frequency  
> *\[PSS EDIT INSTRUCTION FREQUENCY\]

> This option provides the ability to edit data in the FREQUENCY (IN MINUTES) field in the MEDICATION INSTRUCTION file (#51). This data will be used for calculating default QUANTITY and DAYS SUPPLY values for Outpatient Pharmacy orders.

> *Medication Instruction Frequency Report  
> *\[PSS FREQUENCY REPORT\]

> This report displays information from the MEDICATION INSTRUCTION file (#51). It can be used to help determine which instructions can have a valid frequency.

# *Medication Routes/IV Flag *\[PSS MEDICATION ROUTES SUB-MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> These options affect the new IV Flag indicator in the MEDICATION ROUTES file (#51.2).

# *Edit Medication Route IV Flag *\[PSS EDIT MED ROUTE IV FLAG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the editing of the IV Flag in the MEDICATION ROUTES file (#51.2).

> *Flag Medication Routes as IV  
> *\[PSS FLAG MED ROUTES AS IV\]*  

> *This option is used to automatically populate the IV FLAG field in the MEDICATION ROUTES file (#51.2) for all routes that are associated with an IV Flagged Orderable Item or contained in Quick Codes in the IV ADDITIVES file (#52.6).

> *Medication Routes flagged for IV Report*  
> \[PSS MEDICATION ROUTES REPORT\]

> This report shows the Medication Routes, their abbreviations, the package use, and the IV Flag status of the Medication Route. The IV Flag helps determine how Inpatient Medication Orders entered through CPRS are finished in the Inpatient Medications package.

> *Patient Instructions Enter/Edit*

> \[PSS PATIENT INSTRUCTIONS\]

> This option provides the ability to edit the PATIENT INSTRUCTIONS field in the PHARMACY ORDERABLE ITEM file (#50.7).

# Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this POE PDM Pre-Release patch is to prepare sites for the upcoming release of the Pharmacy Ordering Enhancements patches. The new PDM options provide sites the necessary functionality to manipulate data in the Pharmacy files in preparation for the subsequent POE release. The packages that will be involved in the POE changes are CPRS, Inpatient Medications, Outpatient Pharmacy, and Pharmacy Data Management. The only package that requires Pre-Release functionality, however, is Pharmacy Data Management V. 1.0.

All of the options released in this patch will reside under the *Ordering Enhancements Pre-Release* \[PSS DOSAGE PRE-RELEASE\] option, which is located under the *Pharmacy Data Management* \[PSS MGR\] menu.

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ordering Enhancements Pre-Release…

Auto Rematch IV Additives/Solutions Report

Corresponding Drug…

> Enter/Edit Corresponding Drug

> Mark Corresponding Drugs

Report of Corresponding Drugs

Dosages…

Auto Create Dosages

Conversion Tracker

Dosages Enter/Edit

Most Common Dosages Report

Review Dosages Report

Instructions/Nouns…

Convert Instructions to Nouns

Dosage Form/Noun Report

Instructions to Noun Conversion Report

Nouns Enter/Edit

Med Instruction/Frequency…

Edit Medication Instruction Frequency

Medication Instruction Frequency Report

Medication Routes/IV Flag…

Edit Medication Route IV Flag

Flag Medication Routes as IV

Medication Routes flagged for IV Report

Patient Instructions Enter/Edit

These options do not affect the current functionality of the Inpatient Medications, Outpatient Pharmacy, or CPRS applications. Instead, they provide functionality to enter data into new fields that will be required for the subsequent POE patches. After this initial POE PDM Pre-Release patch is released and the Pharmacy files have been appropriately updated, another Pharmacy Data Management patch will be released which will delete the options that are no longer needed. Any new options that are still needed will be incorporated into the current *Pharmacy Data Management* \[PSS MGR\] menu.

Steps<span id="_Toc495917830" class="anchor"></span>

The following is a recommendation concerning the implementation steps for the POE PDM Pre-Release patch (PSS\*1\*34) to ensure a successful transition to the Pharmacy Ordering Enhancements changes that will be available in the near future.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| It is recommended that this patch be installed into the test account initially in order to test the installation process and to do some preliminary familiarization with the functionality. The extensive work required for this setup can be accomplished in the production account since these changes will not affect the current functionality of any associated applications until the Outpatient Pharmacy, Inpatient Medications, and CPRS patches are installed. Therefore, it is recommended that the POE PDM Pre-Release patch first be installed into the test account for minimal testing. Next, install the patch into the production account and complete the setup work. Finally, a mirror of the production account can be made into the test account prior to the installation of the subsequent Pharmacy Ordering Enhancements patches. |

Step 1: Read the functionality section of this document carefully. It is important to have a clear understanding of the Pharmacy Ordering Enhancements project and a solid understanding of the work that is necessary to prepare for the release of the POE project before beginning installation.

Step 2: Using the *Dosage Form/Noun Report*\[PSS DOSE FORM/NOUN REPORT\] option, print the report. It will provide a “before changes” look at the NOUNS that are currently associated with each dosage form. At this point, it will also show DISPENSE UNITS PER DOSE and any Local Possible Dosages that will potentially be created based solely on the <u>current</u> data in the DOSAGE FORM file (#50.606).

Step 3: Using the *Instructions to Noun Conversion Report* \[PSS INSTRUCTIONS REPORT\] option, print the report. It will display all current instructions that are associated with dosage forms. The far right column will contain a “Y” if the instruction is non-numeric. Through another option, *Convert Instructions to Nouns* \[PSS CONVERT INSTRUCTIONS\], the opportunity to automatically move the non-numeric instruction entries to the NOUN field for the individual dosage forms will be provided.

Step 4: If, after evaluation of the content of the *Instructions to Noun Conversion Report* \[PSS INSTRUCTIONS REPORT\], it is determined that less editing will be required to convert the non-numeric instructions entries to the NOUN field for the individual dosage forms, this conversion can be accomplished by running the *Convert Instructions to Nouns* \[PSS CONVERT INSTRUCTIONS\] option. If the decision is made not to run this report, continue on to Step 5.

Step 5: At this point begin using the *Nouns Enter/Edit* \[PSS ENTER/EDIT NOUNS\] option to enter all of the appropriate data into the DOSAGE FORM file (#50.606). While entering this data, a review of the data can be performed by periodically printing the report from the *Dosage Form/Noun Report* \[PSS DOSE FORM/NOUN REPORT\] option. Continue this process until completely satisfied with the data in the DOSAGE FORM file (#50.606). This is one of the most important steps in the entire process.

Step 6: Under the *Dosages*\[PSS DOSAGES SUB-MENU\] option, run the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option. This option will populate the DRUG file (#50) with Possible Dosages and Local Possible Dosages. Do not continue with the next step until the Auto Create Dosages job is complete. To check the status of this job, run the *Conversion Tracker* \[PSS DOSAGE CONVERSION TRACKER\] option. This option will provide information on the status of the job, such as whether the job is still running or if the job has completed. When the *Auto Create Dosages* job is complete, move on to the next step.

Step 7: Review the dosages that have been created by using the *Review Dosages Report* \[PSS DOSAGE REVIEW REPORT\] option. This report will show all of the Possible Dosages and Local Possible Dosages for the drugs in the local DRUG file (#50). The report can be very long, so it is recommended that it be run one letter at a time, (for example all drugs beginning with A, then B., etc.), or run it for a few letters at a time. As the reports are reviewed, use the *Dosages Enter/Edit* \[PSS EDIT DOSAGES\] option to add, delete, and edit the Possible Dosages and Local Possible Dosages as needed. Continue this process until the dosages in the DRUG file (#50) are satisfactory.

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Note \*\*\*The *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option can be run multiple times. If the *AutoCreate Dosages* \[PSS DOSAGE CONVERSION\] option has already been run once, the prompts, “Are you sure you want to run the Dosage conversion again?”, “Do you want to delete the Dosages you already created and start over?”, and “Are you sure you want to delete all DRUG file (#50) dosages and start over?” will appear. The user can opt to have the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option run the setup of the dosages from scratch or have it build upon the previously created dosages. If the decision is made to build upon the previous dosages, the program will not delete any dosages already created, nor will it change the PACKAGE field back to the original value, if that value has been edited after the initial *Auto Create Dosages* has been run. The main benefit of building upon the previously created dosages is that any edits that were made to the DRUG file (#50) will be preserved. Alternatively, if major edits to the DRUG file (#50) are required due to errors or invalid NOUNS, for example, it may be more beneficial to run the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option from scratch to save time. \*\*\* |

Using the *Most Common Dosages Report* \[PSS COMMON DOSAGES\] option, print the report. Enter a Start Date and Frequency. For a Unit Dose order to be counted on this report, the patient must have been admitted after the Start Date entered, and the Stop Date of the order must be after the Start Date entered. The Frequency is the minimum number of times a dosage has been ordered for a drug to appear on the report. Using this report and the *Dosages Enter/Edit* \[PSS EDIT DOSAGES\] option, enter any frequently ordered dosages for these Dispense Drugs if they have not already been created. Please note that the *Most Common Dosages Report* \[PSS COMMON DOSAGES\] only displays information for Unit Dose orders.

Step 8: Under the *Medication Routes/IV Flag* \[PSS MEDICATION ROUTES SUB-MENU\] menu option, print the *Medication Routes flagged for IVReport* \[PSS MEDICATION ROUTES REPORT\]. After reviewing the Med Routes listed, run the *Flag Medication Routes as IV* \[PSS FLAG MED ROUTES AS IV\] option. For the Med Routes listed in this option, a decision can be made as to whether or not to automatically flag the listed Med Routes for IV Use. The *Medication Routes flagged for IV Report* \[PSS MEDICATION ROUTES REPORT\] option can be run again, and using the *Edit Medication Route IV Flag* \[PSS EDIT MED ROUTE IV FLAG\] option, individual Med Routes can be flagged or unflagged for IV use.

Step 9: Print the *Auto Rematch IV Additives/SolutionsReport* \[PSS ADDITIVE/SOLUTION REPORT\]. After reviewing this report, edits can be made to an IV Additive or IV Solution by utilizing the *Drug Enter/Edit* option. Any edits made to the IV Additives or IV Solutions will affect the current functionality of CPRS or Inpatient Medications.

Step 10: Print the *Report of Corresponding Drugs* \[PSS CORRESPONDING DRUG REPORT\] using the *Report of Corresponding Drugs* \[PSS CORRESPONDING DRUG REPORT\] option. If there are any potential drug matches displayed in the second part of this report, review these potential matches. If these matches should be made, run the *MarkCorresponding Drugs* \[PSS CORRESPONDING DRUG MARK\] option to automatically mark these drugs.

Step 11: Use the *Enter/Edit Corresponding Drug* \[PSS CORRESPONDING DRUG EDIT\] option to enter, edit, or delete as many Corresponding Inpatient and Outpatient drugs as possible. At any time during this process, step 11 can be repeated. The more drugs that are marked as Corresponding Inpatient or Corresponding Outpatient drugs, the more drugs will display as potential matches on the *Report of Corresponding Drugs* \[PSS CORRESPONDING DRUG REPORT\]. At any time the *Mark Corresponding Drugs* \[PSS CORRESPONDING DRUG MARK\] option can be run to automatically mark these potential drugs.

Step 12: Defaults can be provided for the new “PATIENT INSTRUCTIONS” prompt and can be entered through the *Patient Instructions Enter/Edit* \[PSS PATIENT INSTRUCTIONS\] option for all drugs tied to a specific Pharmacy Orderable Item. In an effort to enhance the directions to the patient, this field is designed to provide instructions to print on the Outpatient prescription label. Such instructions include, but are not limited to, “TAKE WITH FOOD”, “AVOID SUN EXPOSURE”, etc.

Step 13: Print the report generated by the *Medication Instruction Frequency Report* \[PSS FREQUENCY REPORT\] option. Use this report to determine which entries in this file are or contain a schedule and have valid frequencies. Then use the *Edit Medication Instruction Frequency* \[PSS EDIT INSTRUCTION FREQUENCY\] option to enter the appropriate frequencies.

Functionality<span id="_Toc489428376" class="anchor"></span>

|                                                                               |
|-------------------------------------------------------------------------------|
| Functionality of the POE PDM Pre-Release patch can be divided into six areas: |

1.  Dosage Setup
2.  Medication Routes IV Flag Setup
3.  Corresponding Drug Setup
4.  Additive/Solution Review
5.  Patient Instructions Setup
6.  Med Instruction/Frequency Setup

Of these six, the area that requires the closest attention is step one, Dosage Setup. Proper dosage setup is imperative for the Pharmacy Ordering Enhancements changes to be successful.  

Each of the six affected areas is discussed in detail below.

1. Dosage Setup<span id="_Toc483734611" class="anchor"></span>

Under the current Pharmacy Data Management setup, the first selection made by the provider during CPRS medication order entry is the medication (orderable item). After selecting the orderable item, a list of all Dispense Drugs tied to that orderable item is displayed to the provider so that a selection can be made. For example, if the provider selects as the orderable item PROPRANOLOL TAB, the selection list of Dispense Drugs could display as follows:

PROPRANOLOL HCL 20MG TAB

PROPRANOLOL HCL 40MG TAB

One of the primary goals of the Pharmacy Ordering Enhancements project is to provide a simple dosage selection after the orderable item is selected, such as:

PROPRANOLOL TAB

10MG

20MG

40MG

60MG

Unfortunately, this cannot be accomplished with the current file structure. To provide these dosages it is necessary to associate Possible Dosages and/or Local Possible Dosages with every Dispense Drug.

The dosage information needed for Pharmacy Ordering Enhancements will reside as new fields in the DRUG file (#50). Data will be gathered from other files and this data will be used to populate the DRUG file (#50). Two types of dosages will now be stored in the DRUG file (#50); Possible Dosages and Local Possible Dosages.

Possible Dosages<span id="_Toc489428378" class="anchor"></span>

The PROPRANOLOL TAB example is an example of a drug that can have Possible Dosages. Possible Dosages can be broken down into three individual fields; DISPENSE UNITS PER DOSE, DOSE, and PACKAGE. For a drug to have Possible Dosages it must meet the following criteria:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><p><strong>The drug must be matched to National Drug File.</strong></p></li>
<li><p><strong>The match in National Drug File must be a single-ingredient product.</strong></p></li>
<li><p><strong>The strength of the product must be numeric.</strong></p></li>
<li><p><strong>The dosage form/unit combination of the product must be marked as convertible in the DOSAGE FORM file (#50.606). See Appendix A for a list of dosage form/unit combinations that will automatically be identified by the software.</strong></p></li>
</ol></td>
</tr>
</tbody>
</table>

Possible Dosages are initially populated automatically through the use of the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option. This option will identify drugs that meet the four criteria mentioned above, and by utilizing fields in the VA PRODUCT file (#50.68) and the DOSAGE FORM file (#50.606), it will populate the DRUG file (#50) entry with Possible Dosage information.

Diagram A is an example of how the PROPRANOLOL HCL 20MG TAB Drug entry would exist under the current file setup.

######### Diagram A 

![Diagram A

The VA Product match for this drug is PROPRANOLOL HCL 20MG TAB. It is a single ingredient product with a numeric strength (20). It has a dosage form of TAB and UNITS of MG in the VA PRODUCT file (#50.68). Additionally, a new multiple field called UNITS has been added to the DOSAGE FORM file (#50.606). This field is not editable. It indicates which combination of DOSAGE FORM and UNITS can be converted to Possible Dosages, assuming that the product is a single ingredient drug with a numeric strength. It also indicates the package (Inpatient Medications, Outpatient Pharmacy, or Both) for which Possible Dosages can be created. So, in the first PROPRANOLOL example, the dosage form/unit combination of TAB/MG is convertible for both Inpatient Medications and Outpatient Pharmacy. The DISPENSE UNITS PER DOSE multiple of the DOSAGE FORM file (#50.606) is also a new non-editable field. In the first PROPRANOLOL example the entries for DISPENSE UNITS PER DOSE are 1 and 2, marked for both Inpatient Medications and Outpatient Pharmacy package use. 1 or 1 and 2 were chosen for all dosage forms because it was felt that they were the most common entries and would require the least amount of editing in the DRUG file (#50). In Diagram B, using this information, the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option created the following information in the DRUG file (#50) for PROPRANOLOL HCL 20MG TAB. (See Diagram B.)](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/002.png)

*Diagram A

The VA Product match for this drug is PROPRANOLOL HCL 20MG TAB. It is a single ingredient product with a numeric strength (20). It has a dosage form of TAB and UNITS of MG in the VA PRODUCT file (#50.68). Additionally, a new multiple field called UNITS has been added to the DOSAGE FORM file (#50.606). This field is not editable. It indicates which combination of DOSAGE FORM and UNITS can be converted to Possible Dosages, assuming that the product is a single ingredient drug with a numeric strength. It also indicates the package (Inpatient Medications, Outpatient Pharmacy, or Both) for which Possible Dosages can be created. So, in the first PROPRANOLOL example, the dosage form/unit combination of TAB/MG is convertible for both Inpatient Medications and Outpatient Pharmacy. The DISPENSE UNITS PER DOSE multiple of the DOSAGE FORM file (#50.606) is also a new non-editable field. In the first PROPRANOLOL example the entries for DISPENSE UNITS PER DOSE are 1 and 2, marked for both Inpatient Medications and Outpatient Pharmacy package use. 1 or 1 and 2 were chosen for all dosage forms because it was felt that they were the most common entries and would require the least amount of editing in the DRUG file (#50). In Diagram B, using this information, the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option created the following information in the DRUG file (#50) for PROPRANOLOL HCL 20MG TAB. (See Diagram B.)*

# Diagram B 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![Diagram B

Diagram B shows the drug entry with the new data. Two new fields, STRENGTH and UNIT, have been added to the DRUG file (#50). These two fields are populated with data based on the data contained in the STRENGTH and UNITS fields of the VA PRODUCT file (#50.68). The DOSE field of the POSSIBLE DOSAGE subfile of DRUG file (#50) is populated by multiplying the entry in the DISPENSE UNITS PER DOSE field of the POSSIBLE DOSAGE subfile of DRUG file (#50) by the numeric value of the STRENGTH field in the DRUG file (#50).](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/003.png)

*Diagram B

Diagram B shows the drug entry with the new data. Two new fields, STRENGTH and UNIT, have been added to the DRUG file (#50). These two fields are populated with data based on the data contained in the STRENGTH and UNITS fields of the VA PRODUCT file (#50.68). The DOSE field of the POSSIBLE DOSAGE subfile of DRUG file (#50) is populated by multiplying the entry in the DISPENSE UNITS PER DOSE field of the POSSIBLE DOSAGE subfile of DRUG file (#50) by the numeric value of the STRENGTH field in the DRUG file (#50).*

(DOSE=DISPENSE UNITS PER DOSE x STRENGTH)

Diagram C shows what the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option could create as dosage selections for a PROPRANOLOL TAB orderable item when one or more drugs are matched to that orderable item. (See Diagram C.)

# Diagram C 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![Diagram C

In Diagram C, the PROPRANOLOL drug entries are matched to VA products that have numeric strengths, 20 and 40, and the VA products both have the dosage form/unit combination of TAB/MG. Since TAB/MG is marked as “convertible” in the DOSAGE FORM file (#50.606) for both Inpatient and Outpatient, the new STRENGTH and UNIT fields in the DRUG file (#50) for these drugs can be populated by the software. The STRENGTH and UNITS fields of DRUG file (#50) are populated from the VA PRODUCT file (#50.68) into the DRUG file (#50).](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/004.png)

*Diagram C

In Diagram C, the PROPRANOLOL drug entries are matched to VA products that have numeric strengths, 20 and 40, and the VA products both have the dosage form/unit combination of TAB/MG. Since TAB/MG is marked as “convertible” in the DOSAGE FORM file (#50.606) for both Inpatient and Outpatient, the new STRENGTH and UNIT fields in the DRUG file (#50) for these drugs can be populated by the software. The STRENGTH and UNITS fields of DRUG file (#50) are populated from the VA PRODUCT file (#50.68) into the DRUG file (#50).*

The new fields in the DRUG file (#50), DISPENSE UNITS PER DOSE, DOSE, and PACKAGE, are now populated with data. The DISPENSE UNITS PER DOSE of “1” and “2” came from the new DISPENSE UNITS PER DOSE field in the DOSAGE FORM file (#50.606). When this data is carried over to the DRUG file (#50), the dose is computed by multiplying the DISPENSE UNITS PER DOSE from DRUG file (#50) by the STRENGTH from DRUG file (#50) of each drug. The PACKAGE field values of the DOSAGE FORM file (#50.606), “I” for Inpatient Medications and “O” for Outpatient Pharmacy, are also copied to the PACKAGE field of DRUG file (#50). Some of the Possible Dosages will be converted for both packages, such as the combination of TAB/MG, since this type of dosage can be ordered for Inpatient Medications and also can be converted to a patient readable Outpatient Sig. Other dosage form/unit combinations, such as SYRUP/MG/5ML, can only be converted for Inpatient Medications, since they cannot be easily changed to an Outpatient readable Sig.

In this example, if PROPRANOLOL TAB were selected as the orderable item in CPRS, the Dose selection would be:

20MG

40MG

80MG

Notice that there is only one 40MG selection for the provider, yet both the PROPRANOLOL HCL 20MG TAB drug and the PROPRANOLOL HCL 40MG TAB drug entries have doses of 40MG. In this case, the 40MG dose is associated with the PROPRANOLOL HCL 40MG TAB drug, because it has a lower DISPENSE UNITS PER DOSE (1), than the DISPENSE UNITS PER DOSE (2) associated with the 40MG dose for the PROPRANOLOL HCL 20MG TAB.For Possible Dosages, when the software encounters two doses that are the same, the lowest DISPENSE UNITS PER DOSE will be used to determine the Dispense Drug.

Additionally, another screen that is used for duplicate doses is the non-formulary screen.

If there are two of the same doses, and one is formulary and the other is non-formulary, the formulary entry is the one that is used, regardless of which dose has the lowest DISPENSE UNITS PER DOSE value.

The non-formulary drug filter is executed prior to the lowest DISPENSE UNITS PER DOSE filter. So in this example, if the PROPRANOLOL HCL 40MG TAB is marked as non-formulary, and the PROPRANOLOL HCL 20MG TAB is formulary, the 40MG dosage selection would be associated with the PROPRANOLOL HCL 20MG TAB, even though it has a higher DISPENSE UNITS PER DOSE (2) than the 40MG entry for PROPRANOLOL HCL 40MG TAB (1 DISPENSE UNITS PER DOSE).

Once the Possible Dosages have been created by the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option, doses can be deleted or added by editing the DISPENSE UNITS PER DOSE field using the *Dosages Enter/Edit* \[PSS EDIT DOSAGES\] option. The DOSE field is automatically calculated by multiplying the DISPENSE UNITS PER DOSE field times the STRENGTH. For example, if the PROPRANOLOL TABLET is commonly given in a 10MG dose, and there is not a Dispense Drug entry in DRUG file (#50) of PROPRANOLOL HCL 10MG TAB, a DISPENSE UNITS PER DOSE of .5 can be added for the PROPRANOLOL HCL 20MG TAB, and a dose of 10MG will be created. If a dose of 60MG is sometimes given for PROPRANOLOL TAB, entering a DISPENSE UNITS PER DOSE of 3 for the PROPRANOLOL HCL 20MG TAB drug will provide a 60MG dose. Similarly, if the 80MG dose is rarely given, the DISPENSE UNITS PER DOSE of 2 can be deleted for the PROPRANOLOL HCL 40MG TAB drug, and the 80MG dose will be deleted.

The PACKAGE field can also be edited, but this is a “controlled” type of edit. If the dosage form/unit combination is not marked as convertible in the DOSAGE FORM file (#50.606) for the package, then that package cannot be added as a package for that Possible Dosage. Strength can also be edited in the DRUG file (#50). If the strength is edited, then all of the doses are automatically re-calculated based on the DISPENSE UNITS PER DOSE and new STRENGTH entry. It is recommended that the strength only be edited in the rare case that the Dispense Drug must be matched to a VA Product with an inappropriate strength. (This scenario is discussed in further detail later in this document.) In summary, by adding new DISPENSE UNITS PER DOSE of .5 and 3 to the PROPRANOLOL HCL 20MG TAB entry, and by deleting the DISPENSE UNITS PER DOSE of 2 for the PROPRANOLOL HCL 40MG TAB entry, the following Possible Dosages now exist for PROPRANOLOL TAB orderable item. (See Diagram D.)

# Diagram D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![Diagram D

Though the list of dosages is all that the provider will see for selection, each of the dosages is associated with a Dispense Drug. For example, if the 60MG is selected, the DISPENSE UNITS PER DOSE is 3, and the drug is PROPRANOLOL HCL 20MG TAB. For Outpatient Pharmacy orders the Sig will be built in the same manner as it is today. If the 60MG is chosen, the Sig will begin with “TAKE 3 TABLETS…” and the assigned Dispense Drug is PROPRANOLOL HCL 20MG TAB.](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/005.png)

*Diagram D

Though the list of dosages is all that the provider will see for selection, each of the dosages is associated with a Dispense Drug. For example, if the 60MG is selected, the DISPENSE UNITS PER DOSE is 3, and the drug is PROPRANOLOL HCL 20MG TAB. For Outpatient Pharmacy orders the Sig will be built in the same manner as it is today. If the 60MG is chosen, the Sig will begin with “TAKE 3 TABLETS…” and the assigned Dispense Drug is PROPRANOLOL HCL 20MG TAB.*

As demonstrated in the PROPRANOLOL example, the key to populating the Possible Dosages in the DRUG file (#50) is the information that is contained in the VA PRODUCT file (#50.68) entry to which that drug is matched. Earlier diagrams also show that dosages can be added, deleted, etc., for a drug by editing the DISPENSE UNITS PER DOSE field for that drug.

In addition to creating Possible Dosages for a drug by editing the DISPENSE UNITS PER DOSE field, appropriate Possible Dosages can be created by editing the STRENGTH field for a drug. When Possible Dosages are created for a drug, the strength information from the VA Product match is moved to the drug entry and stored in the STRENGTH field. The only time this data would not be accurate would be if a VA PRODUCT file (#50.68) entry with the correct strength did not exist, and so a different strength of the drug had to be selected for the drug’s VA product match; however, these instances should be rare. If the desired strength does not exist for a particular drug, the functionality exists to edit the STRENGTH field in the DRUG file (#50) for that drug. Once the strength edit is completed, new Possible Dosages are created for every DISPENSE UNITS PER DOSE for that drug.

For example, Diagram E shows an entry in the DRUG file (#50) of METOPROLOL TARTRATE 25MG TAB. No entries with a strength of 25 exist in the VA PRODUCT file (#50.68) for that drug, so it has been matched instead to a VA Product entry with a strength of 50. (See Diagram E.)

# Diagram E

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![Diagram E

In Diagram E, the Possible Dosages created are 50 MG (1 tablet) and 100MG (2 tablets), but the drug is actually METOPROLOL TARTRATE 25MG TAB. These Possible Dosages were created because the STRENGTH of the VA PRODUCT file (#50.68) entry is 50. As displayed in Diagram F, the STRENGTH in the DRUG file (#50) can simply be edited from 50 to 25, and when that STRENGTH is edited, the Possible Dosages for all DISPENSE UNITS PER DOSE, in this case 1 and 2, will be recalculated. (See Diagram F.)](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/006.png)

*Diagram E

In Diagram E, the Possible Dosages created are 50 MG (1 tablet) and 100MG (2 tablets), but the drug is actually METOPROLOL TARTRATE 25MG TAB. These Possible Dosages were created because the STRENGTH of the VA PRODUCT file (#50.68) entry is 50. As displayed in Diagram F, the STRENGTH in the DRUG file (#50) can simply be edited from 50 to 25, and when that STRENGTH is edited, the Possible Dosages for all DISPENSE UNITS PER DOSE, in this case 1 and 2, will be recalculated. (See Diagram F.)*

######### Diagram F

![](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/007.png)

#########  Local Possible Dosages

Diagram G

In the earlier example in Diagram C using PROPRANOLOL TAB, Inpatient and Outpatient Possible Dosages were able to be created for the Dispense Drugs matched to PROPRANOLOL TAB because they met all of the following four criteria:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>1) The drug must be matched to the National Drug File.</strong></p>
<p><strong>2) The match in the National Drug File must be a single-ingredient product.</strong></p>
<p>3) The strength of the product must be numeric.</p>
<p><strong>4) The dosage form/unit combination of the product must be marked as convertible in the DOSAGE FORM file (#50.606).</strong></p></td>
</tr>
</tbody>
</table>

In the following example in Diagram G, the orderable item requested is TIMOLOL SOLN, OPH, which has two Dispense Drugs matched to it. Neither of these Dispense Drugs meets the four criteria for creating Possible Dosages. The two Dispense Drugs are matched to entries in the VA PRODUCT file (#50.68) as follows. (See Diagram G.)

# Diagram G

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![Diagram G (continued)](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/008.png)

*Diagram G (continued)*

These two drugs meet the first three of the Possible Dosages criteria, but do not meet criteria number four. The dosage form/unit combination of SOLN,OPH / % is not marked as convertible in the DOSAGE FORM file (#50.606) for Inpatient or for Outpatient. Since Possible Dosages cannot be created for these drugs, Local Possible Dosages must be created. To create Local Possible Dosages the NOUN field in the DOSAGE FORM file (#50.606) will be utilized. By default, all Local Possible Dosages will be marked for Inpatient Medications and/or Outpatient Pharmacy use based on the PACKAGE identification of the NOUN.

The NOUN field already exists in the DOSAGE FORM file (#50.606) and is used currently by the software. It is a multiple field, meaning that more than one NOUN can be associated with each dosage form. Currently, this field is used by the Outpatient Pharmacy and CPRS packages. For example, the dosage form, TAB, may have one NOUN associated with it, which most likely would be TABLET(S). The NOUN is used in CPRS for display when entering Outpatient Orders and is also used when building the Sig in Outpatient Pharmacy for orders entered through CPRS. Some dosage forms may have multiple NOUNS. The dosage form CREAM may have the following entries in the NOUN field:

LIBERALLY

SMALL AMOUNT

SPARINGLY

THIN FILM

During order entry a selection may be made in CPRS from this list of NOUNS, and Outpatient Pharmacy uses the CPRS selection to build the Sig.

Returning to the TIMOLOL example, a review of the DOSAGE FORM entry for SOLN,OPH, shows that DISPENSE UNITS PER DOSE of 1 and 2 are designated, but no NOUNS are specified. If the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option is run with the current setup, no Possible Dosages for the two TIMOLOL drugs will be created because the drugs do not meet all four Possible Dosages criteria. No Local Possible Dosages will be created either, because there are no NOUNS associated with the dosage form SOLN, OPH.

It is extremely important to review and add/edit the NOUNS prior to running the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option because the NOUNS are the key to creating Local Possible Dosages.

Four options are provided, under the *Instructions/Nouns* \[PSS INSTRUCTIONS/NOUNS\] menu option to assist with the NOUNS review and add/edit process.

*Convert Instructions to Nouns* \[PSS CONVERT INSTRUCTIONS\]

*Dosage Form/Noun Report* \[PSS DOSE FORM/NOUN REPORT\]

*Instructions to Noun Conversion Report* \[PSS INSTRUCTIONS REPORT\]

*Nouns Enter/Edit* \[PSS ENTER/EDIT NOUNS\]

Noun Setup<span id="_Toc489428380" class="anchor"></span>

The first step in setting up the NOUNS is to run the *Dosage Form/Noun Report* \[PSS DOSE FORM/NOUN REPORT\]. This report shows the current NOUN setup of each dosage form. The report displays the dosage form, all of the associated NOUNS, the DISPENSE UNITS PER DOSE, and any Local Possible Dosages. Although the Local Possible Dosages have not yet actually been created in the DRUG file (#50), the NOUNS and the DISPENSE UNITS PER DOSE that will be used to create the Local Possible Dosages will display.

The next step is to run the *Instructions to Noun Conversion Report *\[PSS INSTRUCTIONS REPORT\]. This report shows all of the instructions associated with each dosage form. Most of the instructions will be numeric, and depending on the site setup of the DOSAGE FORM file (#50.606), it is possible that all instructions are numeric. This report and the *Convert Instructions to Nouns* \[PSS CONVERT INSTRUCTIONS\] option are provided for sites that used the INSTRUCTIONS field for text entries. The *Convert Instructions to Nouns* \[PSS CONVERT INSTRUCTIONS\] option will automatically move any non-numeric instructions to the NOUN field for that particular dosage form. The last column on the *Instructions to Noun Conversion Report* \[PSS INSTRUCTIONS REPORT\] indicates which instructions will be converted to NOUNS if the instructions conversion is run. At this point, if the instructions text entries are to be converted to NOUNS, proceed with the *Convert Instructions to Nouns* \[PSS CONVERT INSTRUCTIONS\] option. If the non-numeric instructions were converted to the NOUN field, it is recommended that the *Dosage Form/Noun Report*\[PSS DOSE FORM/NOUN REPORT\] be run and reviewed again.

The *Nouns Enter/Edit* \[PSS ENTER/EDIT NOUNS\] option provides the ability to enter and edit NOUNS and also the ability to enter and edit three new fields:

PACKAGE

PRE-ORDERING ENHANCEMENT

CONJUNCTION

The PACKAGE field is associated with each NOUN, and can be marked “I” for Inpatient Medications, “O” for Outpatient Pharmacy, or “I O” for both Inpatient Medications and Outpatient Pharmacy. This field determines whether or not the Local Possible Dosage will be built for Inpatient Medications, Outpatient Pharmacy, or both, and what will be returned as Local Possible Dosages to CPRS. All current NOUNS will automatically be marked for both Inpatient Medications and Outpatient Pharmacy upon installation of this patch.

The PRE-ORDERING ENHANCEMENT field indicates that any newly entered NOUN is to be used in the current software after this patch is installed, but before the supporting software is installed. All current NOUNS will be marked as PRE-ORDERING ENHANCEMENT NOUNS upon installation, but any NOUNS added after this patch should not be marked as PRE-ORDERING ENHANCEMENT, unless the new NOUNS are to be used immediately.

The CONJUNCTION field is a field that is not associated with each NOUN but is associated with each dosage form. This field will be used exclusively by CPRS for display to the provider in the selection list of Local Possible Dosages. For example, a Local Possible Dosage of

1 DROP 0.25%

can be modified to

1 DROP OF 0.25%

by adding the word OF as the conjunction for the dosage form.

The CONJUNCTION field is not used to build Local Possible Dosages. Instead, the CONJUNCTION field is returned to CPRS as a separate field when Local Possible Dosages are returned for a drug with that dosage form, in order to clarify the display of dosages.

Use the *Nouns Enter/Edit* \[PSS ENTER/EDIT NOUNS\] option to enter the needed data in the NOUN field of the DOSAGE FORM file (#50.606). This data can be reviewed at any time with the *Dosage Form/Noun Report*\[PSS DOSE FORM/NOUN REPORT\].

Examples of possible NOUN entries are:

<u>DOSAGE FORM</u> <u>NOUNS</u> <u>PACKAGE</u>

OINT, OPHTH ¼ INCH RIBBON IO

SMALL AMOUNT IO

THIN FILM IO

SUSPENSION,ORAL TEASPOONFUL(S) IO

TABLESPOONFUL(S) IO

ML(S) I

SYRUP TEASPOONFUL(S) IO

TABLESPOONFUL(S) IO

ML(S) I

Most sites have at least some NOUNS that end in “(S)”, such as CAPSULE(S), DROP(S), and TABLET(S). In the current software, when Sigs are built for orders entered through CPRS for the Outpatient Pharmacy finish process, these Sigs will appear in Pharmacy as:

TAKE 1 TABLET(S) BY MOUTH…

TAKE 2 TABLET(S) BY MOUTH…

TAKE 1 CAPSULE(S) BY MOUTH….

TAKE 2 CAPSULE(S) BY MOUTH….

The “(S)” currently appears at the end of the NOUN regardless of how many DISPENSE UNITS PER DOSE are indicated, 1, 2, 3, etc. As part of the Pharmacy Ordering Enhancements project, the software will drop the (S) from the NOUN if the DISPENSE UNITS PER DOSE is 1 or less. When DISPENSE UNITS PER DOSE are greater than 1, the parenthesis will be dropped from the “(S)”. For example, these Sigs will appear as:

TAKE 1 TABLET BY MOUTH…

TAKE 2 TABLETS BY MOUTH…

TAKE 1 CAPSULE BY MOUTH….

TAKE 2 CAPSULES BY MOUTH….

If a NOUN ends in “(S)” or “(s)”, such as TABLET(S) or capsule(s), the “(S)” or “(s)” will be completely dropped from the NOUN when building the Sigs, as long as the DISPENSE UNITS PER DOSE is 1 or less. If the DISPENSE UNITS PER DOSE is greater than 1, the parenthesis around the “(S)” will be eliminated, creating a plural NOUN, such as “TABLETS”. For this to happen, the NOUN must precisely end in the three characters “(S)”. It is important that the NOUNS are built this way prior to running the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option, particularly as it relates to the building of the Local Possible Dosages. Local Possible Dosages are created and stored in the DRUG file (#50) as text entries. The process of removing the parenthesis will be performed during the *Auto Create Dosages* process. Therefore, it is important that NOUNS that may be plural be entered into the NOUN field with the parenthesis prior to running the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option.Only when completely satisfied with the NOUN set up should the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option be run.

Keep in mind that if an orderable item is selected in CPRS, and there are Possible Dosages for any of the Dispense Drugs tied to that orderable item, only the Possible Dosages will be returned, and any Local Possible Dosages will be ignored. Local Possible Dosages will only be used when no Possible Dosages can be found for Drugs tied to the selected orderable item and identified for use by the selected application (Inpatient Medications or Outpatient Pharmacy). The *AutoCreate Dosages* \[PSS DOSAGE CONVERSION\] option will automatically create the Local Possible Dosages with the appropriate “s” ending for any NOUNS ending with the “(s)” or “(S)” character sequence entered in the DOSAGE FORM file (#50.606).

Diagram H

In the TIMOLOL example in Diagram H, the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option still has not been run, but DROP(S) has been entered as a NOUN and the drug has a dosage form of SOLN,OPH. This entry produces the following results. (See Diagram H.)

# Diagram H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![Diagram I

In Diagram I, the “OF” has been entered into the CONJUNCTION field to appear in the CPRS display of dosages. After running the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option, the following Dosages will be created. (See Diagram I.)](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/009.png)

*Diagram I

In Diagram I, the “OF” has been entered into the CONJUNCTION field to appear in the CPRS display of dosages. After running the *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option, the following Dosages will be created. (See Diagram I.)*

######### Diagram I

![](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/010.png)

IMPORTANT INFORMATION:

All current NOUNS will be marked as PRE-ORDERING ENHANCEMENT NOUNS upon installation, but any NOUNS added after this patch should not be marked as PRE-ORDERING ENHANCEMENT, unless newly added NOUNS are to be used immediately.

If there is a NOUN, and NO DISPENSE UNITS PER DOSE, the Local Possible Dosages are created with just the NOUN. (If an orderable item has drugs with Possible Dosages and Local Possible Dosages, Locals are ignored.)

Example: Noun with no Dispense Units Per Dose

<u>DOSAGE FORM</u> <u>DISPENSE UNITS</u> <u>NOUNS</u> <u>PACKAGE</u>

<u>PER DOSE</u>

####### CREAM,TOP none OVER ENTIRE AREA IO

SMALL AMOUNT IO

THIN FILM IO

ADAPTER none ADAPTER O

### Example: Local Possible Dosages for Topical Products

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\(2159\) FLUOCINOLONE .025% OINT (15GM) \*N/F\* Inactive Date:

ORDER BY GM (15GM = 1 TUBE)

Strength: Units: Application Package: UO

Possible Dosages: (None)

Local Possible Dosages:

SMALL AMOUNT Package: IO

MODERATE AMOUNT Package: IO

LIBERAL AMOUNT Package: IO

\(1129\) FLUOCINOLONE 0.01% CREAM \*N/F\* Inactive Date:

ORDER BY GM IN INCREMENTS OF 15, 30, 45 OR 60 GM

Strength: Units: Application Package: UO

Possible Dosages: (None)

Local Possible Dosages:

SMALL AMOUNT Package: IO

THIN LAYER Package: IO

LIBERALLY Package: IO

\(1130\) FLUOCINOLONE 0.025% CREAM (15GM) \*N/F\* Inactive Date:

ORDER BY GM (15 GM = 1 TUBE)

Strength: Units: Application Package: UO

Possible Dosages: (None)

Local Possible Dosages:

SMALL AMOUNT Package: IO

THIN LAYER Package: IO

LIBERALLY Package: IO

\(2627\) FLUOCINOLONE 0.025% OINT 425GM JAR \*N/F\* Inactive Date:

Strength: Units: Application Package: U

Possible Dosages: (None)

Local Possible Dosages:

SMALL AMOUNT Package: IO

MODERATE AMOUNT Package: IO

INCH(S) Package: IO

LIBERAL AMOUNT Package: IO

\(1131\) FLUOCINOLONE ACETONIDE 0.01% SOLN (60ML) Inactive Date:

ORDER BY ML (60 ML = 1 BOTTLE)

Strength: Units: Application Package: OU

Possible Dosages: (None)

Local Possible Dosages:

SMALL AMOUNT Package: IO

LIBERALLY Package: IO

\(3572\) FLUOCINOLONE ACETONIDE 0.025% OINT Inactive Date:

ORDER BY GM (60 GM = 1 TUBE)

Strength: Units: Application Package: O

Possible Dosages: (None)

Local Possible Dosages:

SMALL AMOUNT Package: IO

MODERATE AMOUNT Package: IO

INCH(S) Package: IO

LIBERAL AMOUNT Package: IO

\(1132\) FLUOCINONIDE 0.05% CREAM,TOP (30GM) Inactive Date:

RESTRICTED NAT.FORMULARY-JUSTIFY USE\*\*\*ORDER BY GM (15,30 or 60 GM)

Strength: Units: Application Package: UO

Possible Dosages: (None)

Local Possible Dosages:

SMALL AMOUNT Package: IO

THIN LAYER Package: IO

LIBERALLY Package: IO

\(1133\) FLUOCINONIDE 0.05% GEL 60GM \*N/F\* Inactive Date:

ORDER BY THE GM(60GM/TU)

\(1134\) FLUOCINONIDE 0.05% OINT,TOP 30GM Inactive Date:

RESTRICTED NATIONAL FORMULARY\*\*\*ORDER BY GRAM

Strength: Units: Application Package: UO

Possible Dosages: (None)

Local Possible Dosages:

SMALL AMOUNT Package: IO

MODERATE AMOUNT Package: IO

LIBERAL AMOUNT Package: IO

\(794\) FLUORESCEIN NA 0.6MG STRIP 300/BX Inactive Date:

ORDER BY EACH STRIP(300/BX)

Strength: Units: Application Package: UO

Possible Dosages: (None)

Local Possible Dosages:

#######  1 STRIP Package: IO 

####### Possible Dosages and Local Possible Dosages

The following dosage example is of a Dispense Drug that has Possible Dosages for Inpatient Medications, and Local Possible Dosages for Outpatient Pharmacy. The Dispense Drug in Diagram J is PROMETHAZINE HCL 25MG/5ML SYRUP. (See Diagram J.)

# Diagram J 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # ![](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/011.png)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Diagram J

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As demonstrated in Diagram J, the PROMETHAZINE HCL 25MG/5ML is matched to the VA PRODUCT file (#50.68) entry of PROMETHAZINE HCL 25MG/5ML SYRUP, with a STRENGTH of 25, a UNIT of MG/5ML, and a DOSAGE FORM of SYRUP. In the DOSAGE FORM file (#50.606) the entry for SYRUP that has a UNITS of MG/5ML is only marked for Inpatient Medications. As part of the setup, the NOUNS, ML(S), TEASPOONFUL(S), and TABLESPOONFUL(S), have been added.

The reason that the combination of SYRUP and MG/5ML was only marked for Inpatient Medications use is that it is difficult to convert this type of dosage to an outpatient readable Sig. The entire VA PRODUCT file (#50.68) was reviewed for all combinations of dosage form/units and a determination was made on each combination. For the DOSAGE FORM of SYRUP, there were no UNITS that were marked for Outpatient Pharmacy use. The UNITS that have been marked for Inpatient Medications use for the SYRUP DOSAGE FORM are:

GM/15ML

GM/5ML

MEQ/5ML

MG/15ML

MG/5ML

MG/ML

The *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option would create Possible Dosages and Local Possible Dosages based on the DOSAGE FORM setup of SYRUP. (See Diagram K.)

# Diagram K

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![Diagram K

Possible Dosages have been created for Inpatient Medications, and Local Possible Dosages have been created for Outpatient Pharmacy. Again, the reason Possible Dosages were created only for Inpatient Medications is because the UNITS of MG/5ML for the SYRUP dosage form was only marked convertible for Inpatient Medications. The Possible Dosages returned to CPRS for an Inpatient Medications order are displayed in the top left section of the diagram as follows:](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/012.png)

*Diagram K

Possible Dosages have been created for Inpatient Medications, and Local Possible Dosages have been created for Outpatient Pharmacy. Again, the reason Possible Dosages were created only for Inpatient Medications is because the UNITS of MG/5ML for the SYRUP dosage form was only marked convertible for Inpatient Medications. The Possible Dosages returned to CPRS for an Inpatient Medications order are displayed in the top left section of the diagram as follows:*

25MG/5ML

50MG/10ML

Possible Dosages are not stored as a DOSE and UNIT combination. The DOSE is stored as a numeric value and the UNIT, a pointer to the DRUG UNITS file (#50.607), is retrieved from the DRUG UNITS file (#50.607) at the time the user selects the drug through the Pharmacy applications or CPRS. Therefore, within the Pharmacy packages and the CPRS package, the expanded version of the dosage is viewable, although it is stored in the numeric form in the DOSE field of the Possible Dosages.

> **NOTE:** Local Possible Dosages will only be used when no Possible Dosages can be found for Drugs tied to the selected orderable item and identified for use by the selected application (Inpatient Medications or Outpatient Pharmacy).

Diagram K2

Diagram K2 illustrates an edit of the STRENGTH field in DRUG file (#50) for a product with volume related UNITS. In the background, the software will evaluate the UNIT field in the DRUG file (#50) to determine if an adjustment in the UNIT is necessary. The software will search for the existence of a “/” in the UNIT field. If the UNIT field contains a “/”, when the strength is edited, calculations will be performed to make appropriate adjustments in the value of the UNIT. For example, the DRUG file (#50) entry may have a STRENGTH of 25 and a UNIT of MG/5ML. If the STRENGTH is edited to 12.5, the UNIT will be adjusted by the software to MG/2.5ML.

When the UNIT value is adjusted it will not display in the DRUG file (#50); however, throughout all Pharmacy and CPRS displays, the correct, adjusted UNIT value of the dosage will be displayed. (See Diagram K2.)

# Diagram K2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/013.png)

# Multi-Ingredient Drugs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are examples of Multi-Ingredient Drugs. Since Multi-Ingredient Drugs do not meet the criteria for creation of a Possible Dosage, Local Possible Dosages will be created based on the NOUN entries in the DOSAGE FORM file (#50.606).

The first example is GUAIFENESIN SYRUP WITH CODEINE 4oz. The dosage form of SYRUP has three NOUNS, all marked for Inpatient Medications and Outpatient Pharmacy use. These NOUNS are TABLESPOONFUL(S), TEASPOONFUL(S), and ML(S). The APPLICATION PACKAGE USE field of the Dispense Drug is marked for Outpatient use only. The *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option will create the following Local Possible Dosages for the drug. (See Diagram L.)

######### Diagram L

![Diagram L

In this case, the Local Possible Dosages of 1ML and 2MLS may be deemed inappropriate for an Outpatient order. An inappropriate dosage selection may be removed so that it is not selectable through CPRS or Pharmacy backdoor in either of two ways. The first way is to simply delete the Local Possible Dosage entries of 1ML and 2MLS from the drug. The second way is to remove the “O”s from the PACKAGE fields that are associated with the Local Possible Dosages of 1ML and 2MLS. Both of these processes can be accomplished through the *Dosages Enter/Edit* \[PSS EDIT DOSAGES\] option. If the “O” is removed from the PACKAGE fields, the following dosages appear through CPRS. (See Diagram M.)](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/014.png)

*Diagram L

In this case, the Local Possible Dosages of 1ML and 2MLS may be deemed inappropriate for an Outpatient order. An inappropriate dosage selection may be removed so that it is not selectable through CPRS or Pharmacy backdoor in either of two ways. The first way is to simply delete the Local Possible Dosage entries of 1ML and 2MLS from the drug. The second way is to remove the “O”s from the PACKAGE fields that are associated with the Local Possible Dosages of 1ML and 2MLS. Both of these processes can be accomplished through the *Dosages Enter/Edit* \[PSS EDIT DOSAGES\] option. If the “O” is removed from the PACKAGE fields, the following dosages appear through CPRS. (See Diagram M.)*

# Diagram M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ![Diagram M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The drug in Diagram M was indicated for Outpatient Pharmacy use only. Drugs designated for Inpatient Medications use only, however, may require different dosages. For example, in the case of a Drug file (#50) entry of Guaifenesin/Codeine 10ml UD, Local Possible Dosages would be created based on the SYRUP DOSAGE FORM NOUN field entries. The dosage form of SYRUP has three NOUNS, all marked for Inpatient Medications and Outpatient Pharmacy use. These NOUNS are TABLESPOONFUL(S), TEASPOONFUL(S), and ML(S). The *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option would create the following Local Possible Dosages for the drug. (See Diagram N.)](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/015.png)

*Diagram M

The drug in Diagram M was indicated for Outpatient Pharmacy use only. Drugs designated for Inpatient Medications use only, however, may require different dosages. For example, in the case of a Drug file (#50) entry of Guaifenesin/Codeine 10ml UD, Local Possible Dosages would be created based on the SYRUP DOSAGE FORM NOUN field entries. The dosage form of SYRUP has three NOUNS, all marked for Inpatient Medications and Outpatient Pharmacy use. These NOUNS are TABLESPOONFUL(S), TEASPOONFUL(S), and ML(S). The *Auto Create Dosages* \[PSS DOSAGE CONVERSION\] option would create the following Local Possible Dosages for the drug. (See Diagram N.)*

####### Diagram N

![Diagram N

In this case, the Local Possible Dosages of 1ML, TEASPOONFUL(S) and TABLESPOONFUL(S) may be deemed inappropriate for an Inpatient order. The 2MLS entry can be edited to display the desired 10 MLS Local Possible Dosage, and the “O” can be removed from the PACKAGE field of Local Possible Dosages, so that the entry is available for Inpatient use only. Using the *Dosages Enter/Edit* \[PSS EDIT DOSAGES\] option, the remaining Local Possible Dosages, 1ML, TEASPOONFUL(S) and TABLESPOONFUL(S), can be deleted. By making these deletions and edits to the LOCAL POSSIBLE DOSAGE fields, the following dosages will be available. (See Diagram O.)](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/016.png)

*Diagram N

In this case, the Local Possible Dosages of 1ML, TEASPOONFUL(S) and TABLESPOONFUL(S) may be deemed inappropriate for an Inpatient order. The 2MLS entry can be edited to display the desired 10 MLS Local Possible Dosage, and the “O” can be removed from the PACKAGE field of Local Possible Dosages, so that the entry is available for Inpatient use only. Using the *Dosages Enter/Edit* \[PSS EDIT DOSAGES\] option, the remaining Local Possible Dosages, 1ML, TEASPOONFUL(S) and TABLESPOONFUL(S), can be deleted. By making these deletions and edits to the LOCAL POSSIBLE DOSAGE fields, the following dosages will be available. (See Diagram O.)*

Notes:

######### Diagram O

![Diagram O

After the edits and deletions mentioned previously, 10 MLS is now the only selectable dosage for this Inpatient Drug. In this way, edits and deletions can be used to control the Possible Dosages and Local Possible Dosages in DRUG file (#50).](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/017.png)

*Diagram O

After the edits and deletions mentioned previously, 10 MLS is now the only selectable dosage for this Inpatient Drug. In this way, edits and deletions can be used to control the Possible Dosages and Local Possible Dosages in DRUG file (#50).*

Diagram P presents another example where appropriate numeric dosages could not be calculated and Local Possible Dosages were created based upon the NOUN in the DOSAGE FORM file (#50.606). (See Diagram P.)

######### Diagram P

![Diagram P

In this example, the NOUNS for this dosage form of CREAM, TOP were THIN FILM and SPARINGLY. When displayed through the CPRS ordering dialog, the dosages of THIN FILM OF 1% and 0.5 % and SPARINGLY OF 1% and 0.5% are created. It is extremely important to review these Local Possible Dosages created and edit those that are inappropriate.](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/018.png)

*Diagram P

In this example, the NOUNS for this dosage form of CREAM, TOP were THIN FILM and SPARINGLY. When displayed through the CPRS ordering dialog, the dosages of THIN FILM OF 1% and 0.5 % and SPARINGLY OF 1% and 0.5% are created. It is extremely important to review these Local Possible Dosages created and edit those that are inappropriate.*

Diagram Q provides an example of how a supply would be entered. (See Diagram Q.)

# Diagram Q

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ![Diagram Q

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Remember, the Local Possible Dosage is concatenated with the NOUN from the DOSAGE FORM file (#50.606). In this example of a supply item, there is no DISPENSE UNITS PER DOSE, therefore the NOUN displays as a Local Possible Dosage. As you can see in Diagram Q, the Local Possible Dosage of GAUZE would look inappropriate in the CPRS ordering dialog and should be deleted as a Local Possible Dosage, leaving PAD as the choice.](pharmacy-ordering-enhancements-poe-pre-release-implementation-guide/019.png)

*Diagram Q

Remember, the Local Possible Dosage is concatenated with the NOUN from the DOSAGE FORM file (#50.606). In this example of a supply item, there is no DISPENSE UNITS PER DOSE, therefore the NOUN displays as a Local Possible Dosage. As you can see in Diagram Q, the Local Possible Dosage of GAUZE would look inappropriate in the CPRS ordering dialog and should be deleted as a Local Possible Dosage, leaving PAD as the choice.*

# Medication Routes IV Flag Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Pharmacy Data Management, Inpatient Medications, Outpatient Pharmacy, and CPRS patches are released, Pharmacy Orderable Items marked with the IV Flag will be inactivated. All IV Additives and IV Solutions that are matched to these IV Flagged Pharmacy Orderable Items will be re-matched to Non IV-Flagged Pharmacy Orderable Items. This change has necessitated that a new field, named IV FLAG, be added to the MEDICATION ROUTES file (#51.2). This field will be instrumental in determining how Inpatient Medication orders entered through CPRS are finished in the Pharmacy software.

When an Inpatient order is entered through CPRS, the Possible Dosage selection will automatically assign a Dispense Drug, and possibly an IV Additive and/or IV Solution. The Medication Route entered for the order will be the key as to how the order is presented for finishing in Pharmacy. This is detailed in the following table:

> I=IV IV=IV FINISH SCREEN  
> U=UNIT DOSE UD=UD FINISH SCREEN

MED DISPENSE DRUG ORDER VIEW SCREEN SPECIAL PROCESSING

ROUTE APPLICATION

USE

IV I IV NONE

IV U UD Prompt User to Finish IV or UD?

IV IU IV Prompt User to Finish IV or UD?

NON IV I UD Prompt User to Finish IV or UD?

NON IV U UD NONE

NON IV IU UD Prompt User to Finish IV or UD?

If no Dispense Drug is passed from CPRS, all Dispense Drugs assigned to the Pharmacy Orderable Item will be accessed for application use and the processing logic described above will be used to determine how the order is presented for finishing in Pharmacy.

This pre-release patch includes three options that provide tools to be used to mark the appropriate Medication Routes with the IV Flag. Remember that marking Medication Routes with the IV Flag will have no effect on the current Pharmacy/CPRS software.

*Medication Routes flagged for IV Report* \[PSS MEDICATION ROUTES REPORT\]

*Flag Medication Routes as IV* \[PSS FLAG MED ROUTES AS IV\]

*Edit Medication Route IV Flag* \[PSS EDIT MED ROUTE IV FLAG\]

The first option*, Medication Routes flagged for IV Report* \[PSS MEDICATION ROUTES REPORT\], displays the Medication Routes, along with the abbreviation, the package use (all packages or National Drug File only), and whether or not the route is flagged for IV use.

The *Flag Medication Routes as IV* \[PSS FLAG MED ROUTES AS IV\] option allows the automatic population of the IV FLAG field in the MEDICATION ROUTES file (#51.2) for all routes associated with IV Flagged Orderable Items, and all routes contained in Quick Codes in the IV ADDITIVES file (#52.6). These routes will be the ones that will most likely be flagged for IV use. The option will show the routes, then prompt if these routes are to be marked with the IV Flag.

The *Edit Medication Route IV Flag* \[PSS EDIT MED ROUTE IV FLAG\]

is a simple edit option that allows single Medication Routes to be marked with the IV flag.

3. Corresponding Drug Setup<span id="_Toc483734613" class="anchor"></span>

The current PDM functionality provides a CORRESPONDING OUTPATIENT DRUG field in the DRUG file (#50) that is used by CPRS when transferring orders from Inpatient to Outpatient. This patch introduces a new field to the DRUG (#50) file called CORRESPONDING INPATIENT DRUG. With the Pharmacy Ordering Enhancements changes, the functionality of transferring orders between Pharmacy packages in CPRS will be greatly enhanced, primarily due to the addition of the CORRESPONDING INPATIENT DRUG field in the DRUG file (#50). The software, in most cases, will be able to automatically assign a drug and a dose to the new order created during the transfer process. More information, such as Dose, Med Route and Schedule, will also be transferable between the packages.

The option named *Report of Corresponding Drugs* \[PSS CORRESPONDING DRUG REPORT\] is included in this patch. This option provides a report that shows what is currently marked as Corresponding Inpatient Drugs and Corresponding Outpatient Drugs for Dispense Drug entries in the DRUG (#50) file. The report is divided into two sections. The first section of the report lists any existing entries in the CORRESPONDING OUTPATIENT DRUG and CORRESPONDING INPATIENT DRUG fields for a Dispense Drug. The second part of the report lists any potential entries for CORRESPONDING OUTPATIENT DRUG and CORRESPONDING INPATIENT DRUG fields that will be populated if the *Mark Corresponding Drugs* \[PSS CORRESPONDING DRUG MARK\] option is run.

The *Mark Corresponding Drugs* \[PSS CORRESPONDING DRUG MARK\] option provides the ability to automatically populate CORRESPONDING INPATIENT DRUG and CORRESPONDING OUTPATIENT DRUG fields for those Dispense Drugs identified as potential matches in the second part of the *Report of Corresponding Drugs* \[PSS CORRESPONDING DRUG REPORT\]. A mail message will be sent to the user who executed the option when the job has been completed.

The option named *Enter/Edit Corresponding Drug* \[PSS CORRESPONDING DRUG EDIT\] is provided in order to edit the CORRESPONDING OUTPATIENT DRUG AND CORRESPONDING INPATIENT DRUG fields in the DRUG file (#50). After selection of the Drug, the packages for which the drug is marked are displayed. If the drug is marked for the Outpatient Pharmacy package, the “CORRESPONDING INPATIENT DRUG” prompt displays for entry or edit. If the drug is marked for Unit Dose or IV package use, the “CORRESPONDING OUTPATIENT DRUG” prompt displays for entry or edit. If the drug is marked for Outpatient Pharmacy and Unit Dose or IV packages use, neither field displays for entry or edit, as the drug is usable in both packages.

4. Additive/Solution Review

<span id="_Toc483734614" class="anchor"></span>

There have always been two types of Pharmacy Orderable Items; ones that are marked with the IV Flag, and ones that are not. The ones that are marked with the IV Flag can only be matched to IV Additives and/or IV Solutions. The ones that are not marked with the IV Flag can only be matched to Dispense Drugs. This was done to control the finishing process of IV and Unit Dose orders entered through CPRS.

One of the changes the Pharmacy Ordering Enhancements project will make is that all of the Pharmacy Orderable Items that are flagged for IV use will be inactivated. Additionally, all IV Additives and IV Solutions that were matched to these IV Flagged Pharmacy Orderable Items will be rematched to Non-IV Flagged Pharmacy Orderable Items. The matching of the Additives and Solutions to the Non-IV Flagged Pharmacy Orderable Item will be based on the Dispense Drug to which the Additive or Solution is linked. This means that a Pharmacy Orderable Item can now have Dispense Drugs, IV Additives and/or IV Solutions matched to it. Below is an example of the current file structure.

CURRENT IV ADDITIVE LINKS:( IV Additive) ( Dispense Drug)

AMPICILLIN AMPICILLIN SOD. 1GM INJ

AMPICILLIN INJ IV AMPICILLIN INJ

(Pharmacy Orderable Item) (Pharmacy Orderable Item)

CURRENT IV SOLUTION LINKS:

|                           |            |     |                           |
|---------------------------|------------|-----|---------------------------|
| IV Solutions              | Volume |     | Dispense Drugs            |
|                           |            |     |                           |
| DEXTROSE 5%               | 50ML       |     | DEXTROSE 5% 50ML INJ.     |
| DEXTROSE 5%               | 100ML      |     | DEXTROSE 5% 100ML BAG     |
| DEXTROSE 5%               | 1000ML     |     | DEXTROSE 5% 1000ML LVP    |
|                           |            |     |                           |
|                           |            |     |                           |
| DEXTROSE 5% INJ,SOLN IV   |            |     | DEXTROSE 5% INJ,SOLN      |
| (Pharmacy Orderable Item) |            |     | (Pharmacy Orderable Item) |
|                           |            |     |                           |

Upon installation of the Pharmacy Ordering Enhancement patches, this re-matching process will automatically be done. Below is an example of the new file structure.

NEW IV ADDITIVE LINKS:( IV Additive) ( Dispense Drug)

AMPICILLIN AMPICILLIN SOD. 1GM INJ

*(Now Inactive)*

AMPICILLIN INJ IV AMPICILLIN INJ

(Pharmacy Orderable Item) (Pharmacy Orderable Item)

NEW IV SOLUTION LINKS:

|                           |            |     |                           |
|---------------------------|------------|-----|---------------------------|
| IV Solutions              | Volume |     | Dispense Drugs            |
|                           |            |     |                           |
| DEXTROSE 5%               | 50ML       |     | DEXTROSE 5% 50ML INJ.     |
| DEXTROSE 5%               | 100ML      |     | DEXTROSE 5% 100ML BAG     |
| DEXTROSE 5%               | 1000ML     |     | DEXTROSE 5% 1000ML LVP    |
|                           |            |     |                           |
| *(Now Inactive)*          |            |     |                           |
| DEXTROSE 5% INJ,SOLN IV   |            |     | DEXTROSE 5% INJ,SOLN      |
| (Pharmacy Orderable Item) |            |     | (Pharmacy Orderable Item) |
|                           |            |     |                           |

The primary reason for removal of the IV Flagged Pharmacy Orderable Items is to reduce the number of new orders created due to Pharmacy’s editing during the finishing of Inpatient Medication orders. For example, an order is entered through CPRS, and the orderable item is HEPARIN INJ (Non-IV Flagged Orderable Item). When the order is finished, Pharmacy determines it is more appropriate to finish the order through the IV package instead of the Unit Dose package, which necessitates changing the orderable item from HEPARIN INJ to HEPARIN INJ IV. Because it is a new Pharmacy Orderable Item, a new order is created.

With the new structure, a new order will not be created, because both the Dispense Drug and the IV Additive of HEPARIN will now be matched to the same Pharmacy Orderable Item.

The option named *Auto-Rematch IV Additive/Solutions Report* \[PSS ADDITIVE/SOLUTION REPORT\] is included in this patch. This option provides a report that shows IV Solutions and IV Additives, along with the current orderable item match. It also shows what the new orderable item match will be after the installation of the Pharmacy Ordering Enhancement patches. There are no edit options exported in this patch that deal with this particular subject. The report simply provides a method to review what the new structure will be, based on the current file setup. One thing to look for is the possibility of multiple active Additives with the same name in the IV ADDITIVES file (#52.6). If multiples exist, the Pharmacy Orderable Items must have been edited in such a way as to distinguish between the Additives with the same name, because the current functionality does not allow more than one IV Pharmacy Orderable Item with the same name and dosage form. After the re-matching, there is a good possibility that these IV Additives will now be matched to the same Pharmacy Orderable Item. This means that there could potentially be a situation where the IV Additives with the same name could be shown for selection during the IV order finishing process. In the current file structure, an IV order would only have one IV Additive matched to the IV Flagged Pharmacy Orderable Item. With the new file structure, there can be more than one IV Additive matched to the same Pharmacy Orderable Item; therefore, when displayed for selection, confusion may result if multiple IV Additives with the same names display. If IV Additives with the same name exist in the IV ADDITIVES file (#52.6), unique names should be created for each Additive. Please remember that if IV Additive names are edited prior to the release of the Pharmacy Ordering Enhancement patches, the current software WILL be affected by these NAME changes.

Example: Multiple Additive with Similar Names

ADDITIVE SUMMARY

OI =\> AMPICILLIN INJ

\(1\) AMPICILLIN (Additive)

\(7\) AMPICILLIN (Additive)

Dispense Drugs matched to OI:

AMPICILLIN SOD. 1GM INJ

AMPICILLIN 10GM INJ. M.D.V.

5. Patient Instructions Setup<span id="_Toc483734615" class="anchor"></span>

As a result of the Pharmacy Ordering Enhancements changes, when orders are entered through the Outpatient Pharmacy package, the dialogue will be changing. Among these changes is a prompt for “PATIENT INSTRUCTIONS”.

Here is an example of the new dialogue:

-----------------------------------------------------------------------------------

> DRUG: Acetaminophen 325mg Tab

> Dosage Ordered(in mg):

> 1\. 325

> 2\. 650

> DOSAGE ORDERED: <u>2</u> 650 (MG)

> DISPENSE UNITS PER DOSE (TABLET(S)): 2// <u>2</u>

> ROUTE: PO// <u>PO</u> (BY MOUTH)

> SCHEDULE: QAM// <u>QAM</u> (EVERY MORNING)

> DURATION (IN DAYS, MINUTES OR HOURS):

> THEN or AND:

> PATIENT INSTRUCTIONS:<u>NOT TO EXCEED 12 TABLETS PER DAY</u>

> rest of order…

> Based on the information entered above, the software will now build the Sig. In this case, the Sig would read:

> TAKE 2 TABLETS BY MOUTH EVERY MORNING NOT TO EXCEED 12 TABLETS PER DAY

-------------------------------------------------------------------------------------------------------------

The text “NOT TO EXCEED 12 TABLETS PER DAY” that was entered at the “PATIENT INSTRUCTIONS” prompt was automatically added to the end of the Sig.

With the release of this patch, a PATIENT INSTRUCTIONS field has been added to the PHARMACY ORDERABLE ITEM file (#50.7). The option *Patient Instructions Enter/Edit* \[PSS PATIENT INSTRUCTIONS\] has been added for entry of data into this field for Pharmacy Orderable Items. This data will be used as a default for the “PATIENT INSTRUCTIONS” prompt in the new Outpatient Pharmacy dialogue for orders entered through the Outpatient Pharmacy package.

When a CPRS entered order is displayed for finishing in Outpatient Pharmacy, if there is data in the PATIENT INSTRUCTIONS field for the Pharmacy Orderable Item, that data will be displayed in the PATIENT INSTRUCTIONS field of the order and added to the end of the Sig. If the default instructions are not appropriate for the prescription, they can be deleted from the order by using the “@” symbol. Deletion of this data will not create a new order since it is not physician-entered data. This PATIENT INSTRUCTIONS data will not be presented to the CPRS user at any time during the CPRS order entry process. It will only be viewable through the Backdoor Outpatient Pharmacy user. It becomes a part of the order after Pharmacy accepts the order during the finishing process and will therefore display as a part of the active order on the CPRS.

6. Medication Instruction/Frequency<span id="_Toc483734616" class="anchor"></span>

As part of the new Outpatient Pharmacy Order dialogues in CPRS and in Outpatient Pharmacy, the software, when possible, will provide default values for the QUANTITY field and DAYS SUPPLY field. These calculations will be based on other information entered for the order, specifically the SCHEDULE, DISPENSE UNITS PER DOSE, and either QUANTITY or DAYS SUPPLY. A new field has been added to the MEDICATION INSTRUCTION file (#51), called FREQUENCY (IN MINUTES) to help in these calculations. This new field will serve the same function as the FREQUENCY (IN MINUTES) field in the ADMINISTRATION SCHEDULE file (#51.1). The reason this new field was added to the MEDICATION INSTRUCTION file (#51) was to provide an additional place to check for this data, in case the data could not be found in the ADMINISTRATION SCHEDULE file (#51.1). The software will use the schedule entry of the order to find an associated frequency in these files, for both CPRS and Outpatient Pharmacy.

Some examples of data to enter would be:

MEDICATION INSTRUCTION FREQUENCY (IN MINUTES)

Q2H 120

Q4H 240

Q6H 360

Q8H 480

# # New Options with Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Ordering Enhancements Pre-Release*  
> \[PSS DOSAGE PRE-RELEASE\]

> This menu contains the options necessary for set up of the POE PDM Pre-Release patch.

> *Auto Rematch IV Additives/Solutions Report*  
> \[PSS ADDITIVE/SOLUTION REPORT\]

> This report shows how the Additive and Solutions will be re-matched to new orderable items, based on their Dispense Drug link.

Example 1: Report for IV Additives Only (Part One of the Additives Report)<span id="_Toc495917845" class="anchor"></span>

Select Ordering Enhancements Pre-Release Option: <u>AUTO</u> Rematch IV Additives/Solutions Report

The current Orderable Item structure keeps Additives and Solutions matched to

Orderable Items flagged for IV use. All Dispense Drugs are currently matched to

Orderable Items that are not flagged for IV Use. This was done to control

the finishing process of IV and Unit Dose orders entered through CPRS.

The new Orderable Item structure will inactivate all IV flagged Orderable

Items. All Additives and Solutions will be re-matched to non-IV flagged

Orderable Items, based on their Dispense Drug links.

Enter RETURN to continue or '^' to exit: <u>\<RET\></u>

Select one of the following:

A ADDITIVES

S SOLUTIONS

B BOTH

Print report for Additives, Solutions, or Both: B// <u>A</u>DDITIVES

\*\*\* THIS REPORT IS DESIGNED FOR 132 COLUMNS \*\*\*

DEVICE: HOME// <u>\<RET\></u> VIRTUAL Right Margin: 80// <u>\<RET\></u>

ADDITIVE REPORT (Additive Internal number in parenthesis) PAGE: 1

Current Additive/Orderable Item match:

\(3\) 10% DEXTROSE (01/11/94)==================\> 10% DEXTROSE INJ,SOLN IV

New Orderable Item===========================\> DEXTROSE INJ,SOLN

Dispense Drugs matched to Orderable Item:

DEXTROSE 10% IN WATER (Additive link)

DEXTROSE 5% IN 0.2%NS 1000ML

DEXTROSE 5% IN 0.45% NS

DEXTROSE 5% 50ML INJ.

DEXTROSE 5% 100ML INJ

DEXTROSE 5% 500ML INJ

DEXTROSE 5% 1000ML INJ

DEXTROSE 5%/WATER

DEXTROSE 50% 50ML SYRINGE

DEXTROSE 50% IN WAT

DEXTROSE 20% IN WATER 500ML

DEXTROSE 5% 250ML BAG

DEXTROSE 50% INJ 50ML VIAL

DEXTROSE 5% 250ML (GLASS)

DEXTROSE 5% WATER 100ML BAG

DEXTROSE 20% 500ML IN 1000ML BAG

DEXTROSE 25GM/50ML VIAL

DEXTROSE 5% 150ML BAG

DEXTROSE 5% 500ML BAG

DEXTROSE 50% 1000ML BOTTLE

Current Additive/Orderable Item match:

\(15\) 10% DEXTROSE (01/11/94)==================\> 10% D5W INJ,SOLN (01/11/94) IV

New Orderable Item============================\> DEXTROSE INJ,SOLN

Dispense Drugs matched to Orderable Item:

DEXTROSE 10% IN WATER (Additive link)

DEXTROSE 5% IN 0.2%NS 1000ML

DEXTROSE 5% IN 0.45% NS

DEXTROSE 5% 50ML INJ.

DEXTROSE 5% 100ML INJ

DEXTROSE 5% 500ML INJ

DEXTROSE 5% 1000ML INJ

DEXTROSE 5%/WATER

DEXTROSE 50% 50ML SYRINGE

DEXTROSE 50% IN WAT

DEXTROSE 20% IN WATER 500ML

DEXTROSE 5% 250ML BAG

DEXTROSE 50% INJ 50ML VIAL

DEXTROSE 5% 250ML (GLASS)

DEXTROSE 5% WATER 100ML BAG

DEXTROSE 20% 500ML IN 1000ML BAG

DEXTROSE 25GM/50ML VIAL

DEXTROSE 5% 150ML BAG

DEXTROSE 5% 500ML BAG

DEXTROSE 50% 1000ML BOTTLE

Current Additive/Orderable Item match:

\(4\) 5% DEXTROSE==============================\> 5% DEXTROSE INJ,SOLN IV

New Orderable Item===========================\> DEXTROSE INJ,SOLN

Dispense Drugs matched to Orderable Item:

DEXTROSE 10% IN WATER

DEXTROSE 5% IN 0.2%NS 1000ML

DEXTROSE 5% IN 0.45% NS

DEXTROSE 5% 50ML INJ. (Additive link)

DEXTROSE 5% 100ML INJ

DEXTROSE 5% 500ML INJ

DEXTROSE 5% 1000ML INJ

DEXTROSE 5%/WATER

DEXTROSE 50% 50ML SYRINGE

DEXTROSE 50% IN WAT

DEXTROSE 20% IN WATER 500ML

DEXTROSE 5% 250ML BAG

DEXTROSE 50% INJ 50ML VIAL

DEXTROSE 5% 250ML (GLASS)

DEXTROSE 5% WATER 100ML BAG

DEXTROSE 20% 500ML IN 1000ML BAG

DEXTROSE 25GM/50ML VIAL

DEXTROSE 5% 150ML BAG

DEXTROSE 5% 500ML BAG

DEXTROSE 50% 1000ML BOTTLE

Current Additive/Orderable Item match:

\(20\) 5-FLUOURACIL=============================\> 5-FLUOURACIL INJ,SOLN IV

New Orderable Item============================\> FLUOROURACIL INJ,SOLN

Dispense Drugs matched to Orderable Item:

FLUOROURACIL 500MG/10ML INJ (Additive link)

Current Additive/Orderable Item match:

\(14\) 50% DEXTROSE=============================\> 50% DEXTROSE INJ,SOLN IV

New Orderable Item============================\> DEXTROSE INJ,SOLN

Dispense Drugs matched to Orderable Item:

DEXTROSE 10% IN WATER

DEXTROSE 5% IN 0.2%NS 1000ML

DEXTROSE 5% IN 0.45% NS

DEXTROSE 5% 50ML INJ.

DEXTROSE 5% 100ML INJ

DEXTROSE 5% 500ML INJ

DEXTROSE 5% 1000ML INJ

DEXTROSE 5%/WATER

DEXTROSE 50% 50ML SYRINGE (Additive link)

DEXTROSE 50% IN WAT

DEXTROSE 20% IN WATER 500ML

DEXTROSE 5% 250ML BAG

DEXTROSE 50% INJ 50ML VIAL

DEXTROSE 5% 250ML (GLASS)

DEXTROSE 5% WATER 100ML BAG

DEXTROSE 20% 500ML IN 1000ML BAG

DEXTROSE 25GM/50ML VIAL

DEXTROSE 5% 150ML BAG

DEXTROSE 5% 500ML BAG

DEXTROSE 50% 1000ML BOTTLE

Current Additive/Orderable Item match:

\(1\) AMPICILLIN (03/07/00)====================\> AMPICILLIN INJ (03/07/00) IV

New Orderable Item===========================\> AMPICILLIN INJ (03/07/00)

Dispense Drugs matched to Orderable Item:

AMPICILLIN SOD. 1GM INJ (03/07/00) (Additive link)

AMPICILLIN 10GM INJ. M.D.V. (03/07/00)

Report for IV Additives Only (Part Two Summary of the Additives Report)<span id="_Toc495917846" class="anchor"></span>

ADDITIVE SUMMARY PAGE: 1

OI =\> AMPICILLIN INJ

\(1\) AMPICILLIN (Additive)

\(7\) AMPICILLIN (Additive)

Dispense Drugs matched to OI:

AMPICILLIN SOD. 1GM INJ

AMPICILLIN 10GM INJ. M.D.V.

OI =\> CEFAMANDOLE INJ

\(21\) CEFAMANDOLE (Additive)

Dispense Drugs matched to OI:

CEFAMANDOLE 1GM INJ

CEFAMANDOLE 1GM FOR PROTOCOL 15

OI =\> CEFAZOLIN INJ

\(5\) CEFAZOLIN (Additive)

Dispense Drugs matched to OI:

CEFAZOLIN SOD 1GM INJ

CEFAZOLIN SOD 10GM M/D INJ

Press Return to continue, '^' to exit:

Example 2: IV Solutions (Part One of the Solutions Report)<span id="_Toc495917847" class="anchor"></span>

SOLUTION REPORT (Solution Internal number in parenthesis) PAGE: 1

Current Solution/Orderable Item match:

\(5\) 0.9% SODIUM CHLORIDE (100 ML)======================\> 0.9% SODIUM CHLORIDE

INJ IV

New Orderable Item======================================\> SODIUM CHLORIDE INJ

Dispense Drugs matched to Orderable Item:

SODIUM CHLORIDE 0.9% LVP 1000

SODIUM CHLORIDE 0.9% LVP 500

SODIUM CHLORIDE 0.9% LVP 250

SODIUM CHLORIDE USP INJ 10ML

SODIUM CHLORIDE 0.9% 50ML

SODIUM CHLORIDE 0.9% 100ML (Solution link)

Current Solution/Orderable Item match:

\(6\) 0.9% SODIUM CHLORIDE (50 ML)=======================\> 0.9% SODIUM CHLORIDE

INJ IV

New Orderable Item======================================\> SODIUM CHLORIDE INJ

Dispense Drugs matched to Orderable Item:

SODIUM CHLORIDE 0.9% LVP 1000

SODIUM CHLORIDE 0.9% LVP 500

SODIUM CHLORIDE 0.9% LVP 250

SODIUM CHLORIDE USP INJ 10ML

SODIUM CHLORIDE 0.9% 50ML (Solution link)

SODIUM CHLORIDE 0.9% 100ML

Current Solution/Orderable Item match:

\(2\) 20% DEXTROSE (500 ML) (01/11/94)===================\> 20% DEXTROSE INJ,SOLN

(01/11/94) IV

New Orderable Item======================================\> DEXTROSE INJ,SOLN

Dispense Drugs matched to Orderable Item:

DEXTROSE 10% IN WATER

DEXTROSE 5% IN 0.2%NS 1000ML

DEXTROSE 5% IN 0.45% NS

DEXTROSE 5% 50ML INJ.

DEXTROSE 5% 100ML INJ

DEXTROSE 5% 500ML INJ

DEXTROSE 5% 1000ML INJ

DEXTROSE 5%/WATER

DEXTROSE 50% 50ML SYRINGE

DEXTROSE 50% IN WAT

DEXTROSE 20% IN WATER 500ML (Solution link)

DEXTROSE 5% 250ML BAG

DEXTROSE 50% INJ 50ML VIAL

DEXTROSE 5% 250ML (GLASS)

DEXTROSE 5% WATER 100ML BAG

DEXTROSE 20% 500ML IN 1000ML BAG

DEXTROSE 25GM/50ML VIAL

DEXTROSE 5% 150ML BAG

DEXTROSE 5% 500ML BAG

DEXTROSE 50% 1000ML BOTTLE

Current Solution/Orderable Item match:

\(11\) 20% DEXTROSE (500 ML) (01/11/94)===================\> 20% DEXTROSE INJ,SOL

N (01/11/94) IV

New Orderable Item=======================================\> DEXTROSE INJ,SOLN

Dispense Drugs matched to Orderable Item:

DEXTROSE 10% IN WATER

DEXTROSE 5% IN 0.2%NS 1000ML

DEXTROSE 5% IN 0.45% NS

DEXTROSE 5% 50ML INJ.

DEXTROSE 5% 100ML INJ

DEXTROSE 5% 500ML INJ

DEXTROSE 5% 1000ML INJ

DEXTROSE 5%/WATER

DEXTROSE 50% 50ML SYRINGE

DEXTROSE 50% IN WAT

DEXTROSE 20% IN WATER 500ML (Solution link)

DEXTROSE 5% 250ML BAG

DEXTROSE 50% INJ 50ML VIAL

DEXTROSE 5% 250ML (GLASS)

DEXTROSE 5% WATER 100ML BAG

DEXTROSE 20% 500ML IN 1000ML BAG

DEXTROSE 25GM/50ML VIAL

DEXTROSE 5% 150ML BAG

DEXTROSE 5% 500ML BAG

DEXTROSE 50% 1000ML BOTTLE

Example 2: IV Solutions (Part Two Summary of the IV Solutions Report)<span id="_Toc495917848" class="anchor"></span>

SOLUTION SUMMARY PAGE: 1

OI =\> AMINO ACIDS INJ,SOLN

\(8\) AMINO ACID SOLUTION 8.5% (500 ML) (Solution)

Dispense Drugs matched to OI:

AMINO ACID W/ELECT 8.5% 500ML

AMINO ACID W/O ELECT 8.5% 500ML

OI =\> DEXTROSE INJ,SOLN

\(1\) 5% DEXTROSE (1000 ML) (Solution)

\(2\) 20% DEXTROSE (500 ML) (01/11/94) (Solution)

\(3\) 5% DEXTROSE (50 ML) (Solution)

\(4\) 5% DEXTROSE (150 ML) (Solution)

\(7\) DEXTROSE 10% (1000 ML) (Solution)

\(9\) 50% DEXTROSE (500 ML) (Solution)

\(10\) DEXTROSE 5% 1/2 NS (1000 ML) (Solution)

\(11\) 20% DEXTROSE (500 ML) (01/11/94) (Solution)

\(15\) DEXTROSE 10% (1000 ML) (Solution)

\(16\) 5% DEXTROSE (100 ML) (Solution)

Dispense Drugs matched to OI:

DEXTROSE 10% IN WATER

DEXTROSE 5% IN 0.2%NS 1000ML

DEXTROSE 5% IN 0.45% NS

DEXTROSE 5% 50ML INJ.

DEXTROSE 5% 100ML INJ

DEXTROSE 5% 500ML INJ

DEXTROSE 5% 1000ML INJ

DEXTROSE 5%/WATER

DEXTROSE 50% 50ML SYRINGE

DEXTROSE 50% IN WAT

DEXTROSE 20% IN WATER 500ML

DEXTROSE 5% 250ML BAG

DEXTROSE 50% INJ 50ML VIAL

DEXTROSE 5% 250ML (GLASS)

DEXTROSE 5% WATER 100ML BAG

DEXTROSE 20% 500ML IN 1000ML BAG

DEXTROSE 25GM/50ML VIAL

DEXTROSE 5% 150ML BAG

DEXTROSE 5% 500ML BAG

DEXTROSE 50% 1000ML BOTTLE

OI =\> SODIUM CHLORIDE INJ

\(5\) 0.9% SODIUM CHLORIDE (100 ML) (Solution)

\(6\) 0.9% SODIUM CHLORIDE (50 ML) (Solution)

Dispense Drugs matched to OI:

SODIUM CHLORIDE 0.9% LVP 1000

SODIUM CHLORIDE 0.9% LVP 500

SODIUM CHLORIDE 0.9% LVP 250

SODIUM CHLORIDE USP INJ 10ML

SODIUM CHLORIDE 0.9% 50ML

SODIUM CHLORIDE 0.9% 100ML

*Corresponding Drug  
*\[PSS CORRESPONDING DRUG MENU\]

> This menu provides the options for review of the Corresponding Inpatient Drug and Corresponding Outpatient Drug functionality.

*Enter/Edit Corresponding Drug  
*\[PSS CORRESPONDING DRUG EDIT\]

> This option provides the ability to mark Corresponding Inpatient Drugs and Corresponding Outpatient Drugs.

######## Example 1: Corresponding Outpatient Drug

#### Select Corresponding Drug Option: <u>ENT</u>er/Edit Corresponding Drug

Select Drug: <u>TYLENOL</u>

1 TYLENOL W/CODEINE NO. 1 TAB N/F

2 TYLENOL \#3 U/D ACETAMINOPHEN W/CODEINE 30MG U/D TAB CN101 INPATIENT USE ONLY

3 TYLENOL \#4 ACETAMINOPHEN W/CODEINE 60MG TAB CN101 N/F

4 TYLENOL 325MG TAB ACETAMINOPHEN 325MG TAB CN103

5 TYLENOL 325MG TAB ACETAMINOPHEN 325MG TAB U/D CN103

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <u>2</u> ACETAMINOPHEN W/CODEINE 30MG U/D TAB CN101 INPATIENT USE ONLY

This entry is marked for the following PHARMACY packages:

Unit Dose

Controlled Substances

CORRESPONDING OUTPATIENT DRUG: <u>TYLENOL</u>

1 TYLENOL W/CODEINE NO. 1 TAB N/F

2 TYLENOL \#4 ACETAMINOPHEN W/CODEINE 60MG TAB CN101 N/F

3 TYLENOL 325MG TAB ACETAMINOPHEN 325MG TAB CN103 NOU

4 TYLENOL DROPS 100MG/ML SOLN ACETAMINOPHEN 125MG/5ML ELIXIR N/F

5 TYLENOL ELIXIR 325MG/10.15ML ACETAMINOPHEN 325MG/10.15ML U/D CN103

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5:<u>\<RET\></u>

6 TYLENOL ELIXIR 650MG/20.3ML ACETAMINOPHEN 650MG/20.3ML U/D CN103

7 TYLENOL ELIXIR W/CODEINE A28 CN101

8 TYLENOL SUPP 650MG ACETAMINOPHEN 650MG RECT SUPP 12'S CN103

9 TYLENOL W/ CODEINE \#2 ACETAMINOPHEN W/CODEINE 15MG TAB CN101

10 TYLENOL W/ CODEINE \#3 ACETAMINOPHEN W/CODEINE 30MG TAB CN101

CHOOSE 1-10: <u>10</u> ACETAMINOPHEN W/CODEINE 30MG TAB CN101

Example 2: Corresponding Inpatient Drug<span id="_Toc495917850" class="anchor"></span>

Select Drug: <u>TYLENOL</u>

1 TYLENOL W/CODEINE NO. 1 TAB N/F

2 TYLENOL \#3 U/D ACETAMINOPHEN W/CODEINE 30MG U/D TAB CN101 INPATIENT USE ONLY

3 TYLENOL \#4 ACETAMINOPHEN W/CODEINE 60MG TAB CN101 N/F

4 TYLENOL 325MG TAB ACETAMINOPHEN 325MG TAB CN103 NOU

5 TYLENOL 325MG TAB ACETAMINOPHEN 325MG TAB U/D CN103

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <u>\<RET\></u>

6 TYLENOL DROPS 100MG/ML SOLN ACETAMINOPHEN 125MG/5ML ELIXIR N/F

7 TYLENOL ELIXIR 325MG/10.15ML ACETAMINOPHEN 325MG/10.15ML U/D CN103

8 TYLENOL ELIXIR 650MG/20.3ML ACETAMINOPHEN 650MG/20.3ML U/D CN103

9 TYLENOL ELIXIR W/CODEINE A28 CN101

10 TYLENOL SUPP 650MG ACETAMINOPHEN 650MG RECT SUPP 12'S CN103

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-10: <u>\<RET\></u>

11 TYLENOL SUPP 650MG ACETAMINOPHEN 650MG RECT SUPP U/D CN103

12 TYLENOL W/ CODEINE \#2 ACETAMINOPHEN W/CODEINE 15MG TAB CN101

13 TYLENOL W/ CODEINE \#3 ACETAMINOPHEN W/CODEINE 30MG TAB CN101

CHOOSE 1-13: <u>13</u> ACETAMINOPHEN W/CODEINE 30MG TAB CN101

This entry is marked for the following PHARMACY packages:

Outpatient

Controlled Substances

#### #### Example 3: Corresponding Inpatient and Outpatient Drug

Select Drug: <u>DACARBAZINE</u> 200MG INJ AN900

This entry is marked for the following PHARMACY packages:

Outpatient

Unit Dose

Press Return to continue: <u>\<RET\></u>

Select Drug:

*Mark Corresponding Drugs  
*\[PSS CORRESPONDING DRUG MARK\]

> This option provides the ability to mark all Corresponding Inpatient drugs and Corresponding Outpatient drugs based on the potential matches that are displayed in the *Report of Corresponding Drugs* \[PSS CORRESPONDING DRUG REPORT\].

Example: Mark Corresponding Drugs Option:<span id="_Toc495917852" class="anchor"></span>

Select Corresponding Drug Option: <u>MARK</u> Corresponding Drugs

This option will automatically mark all corresponding Inpatient and Outpatient

drugs that are listed in the 'Potential Corresponding Inpatient/Outpatient Drug

Matches' section of the 'Report of Corresponding Drugs'.

Before using this option, please make sure you print a current 'Report of

Corresponding Drugs' for review.

Mark potential corresponding drugs? Y// <u>??</u>

Enter 'Yes' to mark corresponding inpatient and outpatient drugs as displayed

in the 'Potential Corresponding Inpatient/Outpatient Drug Matches' section of

the 'Report of Corresponding Drugs'.

Mark potential corresponding drugs? Y// <u>\<RET\></u>ES

This job must be queued. You will receive a mail message upon completion.

Requested Start Time: NOW// (JUL 25, <2000@09:39:47>)

Example: Mail Message<span id="_Toc495917853" class="anchor"></span>

Subj: PDM CORRESPONDING DRUGS \[#14112\] 25 Jul 00 09:40 2 Lines

From: PHARMACY DATA MANAGEMENT in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

The PDM job that automatically marks corresponding inpatient and

outpatient drugs is complete.

Select MESSAGE Action: IGNORE (in IN basket)// <u>\<RET\></u>

> *Report of Corresponding Drugs*  
> \[PSS CORRESPONDING DRUG REPORT\]

> This report shows which drugs are currently marked as Corresponding Inpatient Drugs and Corresponding Outpatient Drugs in the DRUG file (#50). It also shows potential matches that can be achieved by using the *Mark Corresponding Drugs* \[PSS CORRESPONDING DRUG MARK\] option.

Example: Report of Corresponding Drugs<span id="_Toc495917854" class="anchor"></span>

Select Corresponding Drug Option: <u>REP</u>ort of Corresponding Drugs

Since this report must check every drug in the DRUG (#50) File, we recommend

that you queued this report to a printer.

DEVICE: HOME// <u>\<RET\></u> VIRTUAL Right Margin: 80// <u>\<RET\></u>

Current Corresponding Inpatient/Outpatient Drug Matches PAGE: 1

-----------------------------------------------------------------------------

ACETAMINOPHEN 325MG C.T.

Corresponding Outpatient drug: ACETAMINOPHEN 325MG C.T.

Corresponding Inpatient drug: ACETAMINOPHEN 325MG C.T.

ACETAMINOPHEN 325MG TABLET

Corresponding Outpatient drug: ACETAMINOPHEN 325MG TABLET

Corresponding Inpatient drug: ACETAMINOPHEN 325MG TABLET

ACETAMINOPHEN 650MG SUPPOS.

Corresponding Outpatient drug: ACETAMINOPHEN 650MG SUPPOS.

Corresponding Inpatient drug: ACETAMINOPHEN 650MG SUPPOS.

ALBUTEROL INHALER

Corresponding Outpatient drug: ALBUTEROL INHALER

Corresponding Inpatient drug: ALBUTEROL INHALER

ALLOPURINOL 300MG S.T.

Corresponding Outpatient drug: ALLOPURINOL 300MG S.T.

Corresponding Inpatient drug: ALLOPURINOL 300MG S.T.

AMPICILLIN 250MG

Corresponding Outpatient drug: AMPICILLIN 250MG

Corresponding Inpatient drug: AMPICILLIN 250MG

AMPICILLIN SOD. 1GM INJ

Corresponding Outpatient drug: AMPICILLIN SOD. 1GM INJ

CARBAMAZEPINE 200MG S.T.

Corresponding Outpatient drug: CARBAMAZEPINE 200MG S.T.

Corresponding Inpatient drug: CARBAMAZEPINE 200MG S.T.

CEFAMANDOLE 1GM INJ

Corresponding Inpatient drug: CEFAZOLIN SOD 1GM INJ

CEFAZOLIN SOD 1GM INJ

Corresponding Outpatient drug: CEFAMANDOLE 1GM INJ

CIMETIDINE 200MG TAB

Corresponding Outpatient drug: CIMETIDINE 200MG TAB

Corresponding Inpatient drug: CIMETIDINE 200MG TAB

CIMETIDINE 300MG TAB

Corresponding Outpatient drug: CIMETIDINE 300MG TAB

Corresponding Inpatient drug: CIMETIDINE 300MG TAB

CISAPRIDE 10MG

Corresponding Outpatient drug: CISAPRIDE 10MG

Corresponding Inpatient drug: CISAPRIDE 10MG

CLOZAPINE 25MG TAB

Corresponding Outpatient drug: CLOZAPINE 25MG TAB

Corresponding Inpatient drug: CLOZAPINE 25MG TAB

HEXAVITAMINS

Corresponding Outpatient drug: HEXAVITAMINS

Corresponding Inpatient drug: HEXAVITAMINS

HYDRALAZINE 50MG TAB

Corresponding Outpatient drug: HYDRALAZINE 50MG TAB

Corresponding Inpatient drug: HYDRALAZINE 50MG TAB

SODIUM CHLORIDE 0.9% 100ML

Corresponding Outpatient drug: SODIUM CHLORIDE 0.9% LVP 1000

SODIUM CHLORIDE 0.9% LVP 1000

Corresponding Inpatient drug: SODIUM CHLORIDE 0.9% 100ML

TEST DRUG III

Corresponding Outpatient drug: TEST DRUG III

Corresponding Inpatient drug: TEST DRUG III

TESTOSTERONE ENTH. 200MG/ML 5ML

Corresponding Outpatient drug: TESTOSTERONE ENTH. 200MG/ML 5ML

Corresponding Inpatient drug: TESTOSTERONE ENTH. 200MG/ML 5ML

\*\*\* Potential Corresponding Inpatient/Outpatient Drug Matches PAGE: 6

-----------------------------------------------------------------------------

There are no potential matches!

End of Report.

> *Dosages*  
> \[PSS DOSAGES SUB-MENU\]

> These are the options used to create, view, enter and edit Dosages.

> *Auto Create Dosages  
> *\[PSS DOSAGE CONVERSION\]

This option is used to populate the POSSIBLE DOSAGES fields and LOCAL POSSIBLE DOSAGE fields in the DRUG file (#50).

### Example 1: Initial Creation of Dosages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Dosages Option: <u>AUT</u>o Create Dosages

This option will queue the conversion that populates the Possible Dosages

and Local Possible Dosages in the Drug file.

Requested Start Time: NOW// (MAR 30, 2000@15:00:45)

#### Dosage Conversion queued!

####### Example 2: Rerun Auto Create Dosages 

Select Dosages Option: <u>AUTO</u> Create Dosages

This option will queue the conversion that populates the Possible Dosages

and Local Possible Dosages in the Drug file.

The dosage conversion was last run by PDMPharmacist, One

It started on MAY 02, 2000@07:56:21 and ended on MAY 02, 2000@07:56:34

Are you sure you want to run the Dosage conversion again? N// <u>Y</u> <u>\<RET\></u> ES

Requested Start Time: NOW// <u>\<RET\></u> (MAY 30, 2000@17:07:35)

Dosage Conversion queued!

> *Conversion Tracker*  
> \[PSS DOSAGE CONVERSION TRACKER\]

This option provides the ability to track when the last dosage conversion was run.

Example 1: Dosage Conversion Never Been Run<span id="_Toc495917857" class="anchor"></span>

Select Dosages Option: <u>CO</u>nversion Tracker

Dosage Conversion Tracker Status

=============================================================================

The Dosage conversion has never been run!

Press Return to continue:<u>\<RET\></u>

### Example 2: Dosage Conversion Queued to Run 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Dosages Option: <u>CO</u>nversion Tracker

Dosage Conversion Tracker Status

=============================================================================

The Dosage conversion is queued to run at MAR 30, 2000@15:09:26

It was queued by PDMPharmacist, Two

Press Return to continue: <u>\<RET\></u>

### Example 3: Dosage Conversion Currently Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Dosages Option: <u>CO</u>nversion Tracker

Dosage Conversion Tracker Status

=============================================================================

The Dosage conversion is currently running.

It started at MAR 30, 2000@15:09:43

Press Return to continue: <u>\<RET\></u>

### ### Example 4: Dosage Conversion Complete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Dosages Option: <u>CO</u>nversion Tracker

Dosage Conversion Tracker Status

=============================================================================

The Dosage conversion was last run by PDMPharmacist, One

It started on MAR 30, 2000@15:09:43 and ended on MAR 30, 2000@15:09:46

Press Return to continue: <u>\<RET\></u>

> *Dosages Enter/Edit*  
> \[PSS EDIT DOSAGES\]

This option allows the POSSIBLE DOSAGES fields and LOCAL POSSIBLE DOSAGE fields for a selected Dispense Drug to be edited.

Example 1: Adding a Possible Dosage<span id="_Toc495917861" class="anchor"></span>

Select Dosages Option: <u>DOS</u>ages Enter/Edit

Select Drug: <u>ATIVAN</u>

1 ATIVAN LORAZEPAM 1MG TAB CN302 NATL RESTRICTED; "HALF-TABLET"

2 ATIVAN LORAZEPAM 4MG/ML 1ML INJ (ML) CN302 NATL RESTRICTED(IEN)

3 ATIVAN LORAZEPAM 1MG TAB U.D. CN302 NATL RESTRICTED (NDC)

4 ATIVAN LORAZEPAM 2MG/ML 10ML INJ CN302 NATL RESTRICTED (IEN)

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-4: <u>3</u> LORAZEPAM 1MG TAB U.D. CN302 NATL RESTRICTED (NDC)

This entry is marked for the following PHARMACY packages:

Unit Dose

Controlled Substances

LORAZEPAM 1MG TAB U.D. Inactive Date:

Strength from National Drug File match =\> 1 MG

Strength currently in the Drug File =\> 1 MG

Edit Strength? N// <u>\<RET\></u> O

Strength =\> 1 Unit =\> MG

Select DISPENSE UNITS PER DOSE: <u>?</u>

Answer with POSSIBLE DOSAGES DISPENSE UNITS PER DOSE

Choose from:

1 1 IO

2 2 IO

You may enter a new POSSIBLE DOSAGES, if you wish

Type a Number between 0 and 99999999, 4 Decimal Digits

Select DISPENSE UNITS PER DOSE: <u>.5</u>

Are you adding '.5' as a new POSSIBLE DOSAGES (the 3RD for this DRUG)? No// <u>Y</u> <u>\<RET\></u> (Yes)

Dosage = 0.5MG

POSSIBLE DOSAGES DOSE: .5// <u>\<RET\></u> (No Editing)

DISPENSE UNITS PER DOSE: .5// <u>\<RET\></u>

PACKAGE: <u>I</u>

Strength =\> 1 Unit =\> MG

Select DISPENSE UNITS PER DOSE: <u>?</u>

Answer with POSSIBLE DOSAGES DISPENSE UNITS PER DOSE

Choose from:

.5 0.5 I

1 1 IO

2 2 IO

You may enter a new POSSIBLE DOSAGES, if you wish

Type a Number between 0 and 99999999, 4 Decimal Digits

Select DISPENSE UNITS PER DOSE:<u>\<RET\></u>Example 2: Editing Strength Field & Deletion of Local Possible Dosage<span id="_Toc495917862" class="anchor"></span>

Select Drug: <u>METOPROLOL</u> TARTRATE 25MG TAB U.D. CV100 NATL FORM (NDC)

This entry is marked for the following PHARMACY packages:

Unit Dose

METOPROLOL TARTRATE 25MG TAB U.D. Inactive Date:

Strength from National Drug File match =\> 50 MG

Strength currently in the Drug File =\> 50 MG

Edit Strength? N// <u>YES</u>

STRENGTH: 50// <u>25</u>

Resetting possible dosages:

Possible Dosage = 25MG

Possible Dosage = 50MG

Strength =\> 25 Unit =\> MG

Select DISPENSE UNITS PER DOSE: <u>?</u>

Answer with POSSIBLE DOSAGES DISPENSE UNITS PER DOSE

Choose from:

1 25 IO

2 50 IO

You may enter a new POSSIBLE DOSAGES, if you wish

Type a Number between 0 and 99999999, 4 Decimal Digits

Select DISPENSE UNITS PER DOSE: <u>2</u> 50 IO

DISPENSE UNITS PER DOSE: 2// <u>@</u>

SURE YOU WANT TO DELETE THE ENTIRE '2' DISPENSE UNITS PER DOSE? <u>Y</u> (Yes)

Strength =\> 25 Unit =\> MG

Select DISPENSE UNITS PER DOSE: <u>?</u>

Answer with POSSIBLE DOSAGES DISPENSE UNITS PER DOSE:

1 25 IO

You may enter a new POSSIBLE DOSAGES, if you wish

Type a Number between 0 and 99999999, 4 Decimal Digits

Select DISPENSE UNITS PER DOSE: <u>\<RET\></u>

Enter/Edit Local Possible Dosages? N// <u>\<RET\></u> O

Example 3: Multi-Ingredient Product with Local Possible Dosages<span id="_Toc495917863" class="anchor"></span>

Select Drug: <u>Guaifen</u>

1 GUAIFENESIN 100MG/5ML SYRUP RE302 NATL FORM; 120 ML/BT (NDC)

2 GUAIFENESIN 20MG/ML 10ML U.D. RE302 NATL FORM (NDC)

3 GUAIFENESIN 600MG + DM 30MG TAB RE302 N/F NATL N/F (IEN)

4 GUAIFENESIN 600MG SA TAB RE302 NATL FORM (IEN)

5 GUAIFENESIN 100MG/COD 10MG/5ML (ML) RE301 NATL RESTRICTED; RESTRICTED TO ONE FILL

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <u>5</u> GUAIFENESIN 100MG/COD 10MG/5ML (ML) RE301 NATL RESTRICTED; RESTRICTED TO ONE FILL

This entry is marked for the following PHARMACY packages:

Outpatient

Unit Dose

Controlled Substances

GUAIFENESIN 100MG/COD 10MG/5ML (ML) Inactive Date:

Select LOCAL POSSIBLE DOSAGE: <u>?</u>

Answer with LOCAL POSSIBLE DOSAGE

Choose from:

1 TABLESPOONFUL O

1 TEASPOONFUL O

2 TEASPOONFULS O

You may enter a new LOCAL POSSIBLE DOSAGE, if you wish

Answer must be 1-60 characters in length.

Select LOCAL POSSIBLE DOSAGE: <u>10 ML</u>

Are you adding '10 ML' as a new LOCAL POSSIBLE DOSAGE (the 4TH for this DRUG)?

No// <u>Y</u> (Yes)

LOCAL POSSIBLE DOSAGE: 10 ML//<u>\<RET\></u>

PACKAGE: I Inpatient

Select LOCAL POSSIBLE DOSAGE:<u>\<RET\></u>

> *Most Common Dosages Report*  
> \[PSS COMMON DOSAGES\]

> This report displays the most common dosages ordered over a specified time period for Unit Dose orders.

### Example: Most Common Dosages Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report displays common dosages of Dispense Drugs for Unit Dose orders

based on the time frame entered. Unit Dose orders without a Dosage Ordered

are not included on this report.

If there are multiple Dispense Drugs associated with an order, only the first

Dispense Drug of the order will print with the Dosage Ordered.

Press Return to continue, '^' to exit: <u>\<RET\></u>

Enter start date for gathering Dosages: <u>T-3000</u> (MAR 29, 1992)

Do not print Dosage if frequency is less than: (1-100): 1// <u>2</u>

COMMON DOSAGES REPORT STARTING FROM 03/29/92 PAGE: 1

DRUG DOSAGE FREQUENCY

------------------------------------------------------------------------------

ACETAMINOPHEN 325MG C.T. 100MG 2

500mg 2

ACETAMINOPHEN 325MG TABLET 650MG 2

ACETAMINOPHEN AND CODEINE 30MG 35ML 2

ACYCLOVIR 5% OINT 20MG 2

ALLOPURINOL 300MG S.T. 25MG 2

AMITRIPTYLINE 100MG 100MG 3

AMPICILLIN 250MG 250MG 9

> *Review Dosages Report*  
> \[PSS DOSAGE REVIEW REPORT\]

> This report shows the Possible Dosages and Local Possible Dosages for selected Dispense Drugs.

> Example: Review Dosages Report<span id="_Toc495917865" class="anchor"></span>

Select Dosages Option: <u>REV</u>iew Dosages Report

Select one of the following:

A ALL

S SELECT A RANGE

Print Report for (A)ll or (S)elect a Range: S// <u>\<RET\></u> ELECT A RANGE

To see drugs beginning with the letter 'A', enter 'A', or whichever letter you

wish to see. To see drugs in a range, for example drugs starting with the

letters 'G', 'H', 'I' and 'J', enter in the format 'G-J'.

Select a Range: <u>A</u>

Report will be for drugs starting with the letter A,

and ending with drugs starting with the letter A.

Is this correct? Y// <u>\<RET\></u> ES

This report is designed for 132 column format!

DEVICE: HOME// <u>;C-VT132</u> TELNET TERMINAL

Dosage report for drugs from A through A

Outpatient Expansion

PAGE: 1

--------------------------------------------------------------------------------

\(2361\) ABCIXIMAB 2MG/ML 5ML INJ Inactive

Date:

NATL RESTRICTED - PROCURE FROM UMC ON PRN BASIS (P&T 10/99) (IEN)

Strength: 2 Units: Application Package: UI

Possible Dosages:

Dispense Units Per Dose: 1 Dose: 2MG/1ML Package: I

Dispense Units Per Dose: 2 Dose: 4MG/2ML Package: I

Dispense Units Per Dose: 3 Dose: 6MG/3ML Package: I

Dispense Units Per Dose: 4 Dose: 8MG/4ML Package: I

Dispense Units Per Dose: 5 Dose: 10MG/5ML Package: I

Local Possible Dosages:

2MG Package: O

4MG Package: O

6MG Package: O

8MG Package: O

10MG Package: O

\(2903\) ABSORBASE CREAM 120GM Inactive Date:

CONVERT ALL ORDERS TO "ABSORBASE TOP OINT"

Strength: Units: Application Package:

Possible Dosages: (None)

Local Possible Dosages:

SMALL AMOUNT Package: IO

THIN FILM Package: IO

\(3684\) ABSORBASE TOP OINT Inactive Date:

NATL FORM; 480 GM/JAR (NDC)

Strength: Units: Application Package: UO

Possible Dosages: (None)

Local Possible Dosages:

SMALL AMOUNT Package: IO

THIN FILM Package: IO

\(3779\) ACARBOSE 50MG TAB Inactive Date:

NATL RESTRICTED; "HALF-TABLET"; Requires P&T form (IEN)

Strength: 50 Units: MG Application Package: OU

Possible Dosages:

Dispense Units Per Dose: 1 Dose: 50MG Package: IO

1 TABLET

Dispense Units Per Dose: 2 Dose: 100MG Package: IO

2 TABLETS

Dispense Units Per Dose: .5 Dose: 25MG Package: IO .5 TABLET

Local Possible Dosages: (None)

\(3250\) ACARBOSE 50MG TAB U.D. Inactive Date:

NATL RESTRICTED- NO LONGER STOCKED

Strength: 50 Units: MG Application Package:

Possible Dosages:

Dispense Units Per Dose: 1 Dose: 50MG Package: IO

1 TABLET

Dispense Units Per Dose: 2 Dose: 100MG Package: IO

2 TABLETS

Local Possible Dosages: (None)

\(2063\) ACEBUTOLOL HCL 200MG CAP \*N/F\* Inactive

Date:

NATL N/F (IEN)

Strength: 200 Units: MG Application Package: UO

Possible Dosages:

*Instructions/Nouns*  
\[PSS INSTRUCTIONS/NOUNS\]

These options provide the functionality to populate and control the NOUN fields in the DOSAGE FORM file (#50.606).

> *Convert Instructions to Nouns  
> *\[PSS CONVERT INSTRUCTIONS\]

> This option allows the conversion of all non-numeric instructions to NOUNS in the DOSAGE FORM file (#50.606).

Example: Convert Instructions to Nouns<span id="_Toc495917866" class="anchor"></span>

Select Instructions/Nouns Option: <u>CON</u>vert Instructions to Nouns

This option will move all non-numeric Instructions to the Noun field in the

Dosage Form file. If you do this, you will then need to review the Nouns and

decide to mark them for Inpatient, Outpatient or both.

Convert all non-numeric Instructions to Nouns? Y//

Converting....

Finished converting Instructions to Nouns!

> *Dosage Form/Noun Report*  
> \[PSS DOSE FORM/NOUN REPORT\]

> This report displays the DOSAGE FORMS, along with their associated NOUN and PACKAGE fields. It also displays the Local Possible Dosage based on the NOUN.

Example: Dosage Form/Noun Report<span id="_Toc495917867" class="anchor"></span>

Select Instructions/Nouns Option: <u>DOS</u>age Form/Noun Report

This report shows the Dosage Forms and Nouns, along with the package use for

each Noun and the resulting Local Possible Dosage.

DEVICE: HOME// <u>\<RET\></u> TELNET TERMINAL

Dosage Form Dispense Units per Dose PAGE: 1

Noun(s) Package--\>Local Possible Dosage

-----------------------------------------------------------------------------

ADAPTER (1)

(No Nouns)

AEROSOL (1)

(No Nouns)

AEROSOL,ORAL (1,2)

PUFF(S) IO--\> 1 PUFF

IO--\> 2 PUFFS

AEROSOL,RTL (1,2)

APPLICATORFUL(S) IO--\> 1 APPLICATORFUL

IO--\> 2 APPLICATORFULS

AEROSOL,TOP (1,2)

SPRAY(S) IO--\> 1 SPRAY

IO--\> 2 SPRAYS

AEROSOL,VAG (1,2)

SPRAY(S) IO--\> 1 SPRAY

IO--\> 2 SPRAYS

APPLICATOR (1,2)

(No Nouns)

BAG

(No Nouns)

BANDAGE

(No Nouns)

BAR,CHEWABLE (1)

BAR(S) IO--\> 1 BAR

BAR,TOP

(No Nouns)

BARRIER

(No Nouns)

BEADS,TOP

(No Nouns)

BELT

(No Nouns)

BLOCK

(No Nouns)

CAP,EC (1,2)

CAPSULE(S) IO--\> 1 CAPSULE

IO--\> 2 CAPSULES

CAP,INHL (1,2)

CAPSULE(S) IO--\> 1 CAPSULE

IO--\> 2 CAPSULES

CAP,ORAL (1,2)

CAPSULE(S) IO--\> 1 CAPSULE

IO--\> 2 CAPSULES

CAP,SA (1,2)

CAPSULE(S) IO--\> 1 CAPSULE

IO--\> 2 CAPSULES

CAP,SPRINKLE (1,2)

CAPSULE(S) IO--\> 1 CAPSULE

IO--\> 2 CAPSULES

CAP,SPRINKLE,SA (1,2)

CAPSULE(S) IO--\> 1 CAPSULE

IO--\> 2 CAPSULES

CAP/INJ (1,2)

(No Nouns)

CATHETER

(No Nouns)

CHAMBER

(No Nouns)

CLAMP

(No Nouns)

COLLAR

(No Nouns)

CONE

(No Nouns)

CONTAINER

(No Nouns)

CONVEX INSERT

(No Nouns)

CREAM

SMALL AMOUNT IO--\> SMALL AMOUNT

MODERATE AMOUNT IO--\> MODERATE AMOUNT

THIN FILM IO--\> THIN FILM

CREAM,ORAL

SMALL AMOUNT IO--\> SMALL AMOUNT

MODERATE AMOUNT IO--\> MODERATE AMOUNT

CREAM,OTIC

SMALL AMOUNT IO--\> SMALL AMOUNT

MODERATE AMOUNT IO--\> MODERATE AMOUNT

CREAM,RTL

APPLICATORFUL(S) IO--\> APPLICATORFUL(S)

CREAM,TOP

SMALL AMOUNT IO--\> SMALL AMOUNT

MODERATE AMOUNT IO--\> MODERATE AMOUNT

LIBERALLY IO--\> LIBERALLY

CREAM,VAG

APPLICATORFUL(S) IO--\> APPLICATORFUL(S)

CREAM/TAB,VAG

(No Nouns)

CRYSTAL (1,2)

TABLESPOONFUL(S) IO--\> 1 TABLESPOONFUL

IO--\> 2 TABLESPOONFULS

DENTAL CONE (1)

(No Nouns)

DEVICE

(No Nouns)

DIAPHRAGM

(No Nouns)

DISK

(No Nouns)

DOUCHE (1,2)

CONTENTS IO--\> 1 CONTENTS

IO--\> 2 CONTENTS

DRAIN

(No Nouns)

DRESSING

DRESSING(S) IO--\> DRESSING(S)

DRESSING,TOP

DRESSING(S) IO--\> DRESSING(S)

DROPS,ORAL (1,2)

DROP(S) IO--\> 1 DROP

IO--\> 2 DROPS

ELIXER (1,2)

TEASPOONFUL(S) IO--\> 1 TEASPOONFUL

IO--\> 2 TEASPOONFULS

TABLESPOONFUL(S) IO--\> 1 TABLESPOONFUL

IO--\> 2 TABLESPOONFULS

ELIXIR (1,2)

TEASPOONFUL(S) IO--\> 1 TEASPOONFUL

IO--\> 2 TEASPOONFULS

TABLESPOONFUL(S) IO--\> 1 TABLESPOONFUL

IO--\> 2 TABLESPOONFULS

EMULSION (1,2)

(No Nouns)

EMULSION,TOP

(No Nouns)

ENEMA (1,2)

CONTENTS IO--\> 1 CONTENTS

IO--\> 2 CONTENTS

ENEMA,RTL (1,2)

CONTENTS IO--\> 1 CONTENTS

IO--\> 2 CONTENTS

EXTRACT (1,2)

(No Nouns)

FACEPLATE

(No Nouns)

FILM

(No Nouns)

FILM,CONT REL

(No Nouns)

FLANGE CAP

(No Nouns)

FLUFF

(No Nouns)

FLUID EXTRACT (1,2)

(No Nouns)

GAS

(No Nouns)

GAUZE

1 4X4 IO--\> 1 4X4

GEL (1,2)

SMALL AMOUNT IO--\> 1 SMALL AMOUNT

IO--\> 2 SMALL AMOUNT

MODERATE AMOUNT IO--\> 1 MODERATE AMOUNT

IO--\> 2 MODERATE AMOUNT

GEL,DENT (1,2)

SMALL AMOUNT IO--\> 1 SMALL AMOUNT

IO--\> 2 SMALL AMOUNT

LIBERAL AMOUNT IO--\> 1 LIBERAL AMOUNT

IO--\> 2 LIBERAL AMOUNT

GEL,NASAL (1,2)

(No Nouns)

GEL,OPH (1,2)

SMALL AMOUNT IO--\> 1 SMALL AMOUNT

IO--\> 2 SMALL AMOUNT

THIN FILM IO--\> 1 THIN FILM

IO--\> 2 THIN FILM

GEL,TOP

SMALL AMOUNT IO--\> SMALL AMOUNT

LIBERAL AMOUNT IO--\> LIBERAL AMOUNT

GLOVE

(No Nouns)

GLVOE

(No Nouns)

GRAFT,TOP

(No Nouns)

GRANULES (1,2)

(No Nouns)

GRNL,EFFERVSC (1,2)

PACKET(S) IO--\> 1 PACKET

IO--\> 2 PACKETS

GRNL,RCNST-ORAL (1,2)

(No Nouns)

GUM,CHEWABLE (1,2)

PIECE(S) IO--\> 1 PIECE

IO--\> 2 PIECES

IMPLANT (1,2)

(No Nouns)

INHALANT (1,2)

PUFF(S) IO--\> 1 PUFF

IO--\> 2 PUFFS

INHALATIONS (1,2)

(No Nouns)

INHALER (1,2)

PUFF(S) IO--\> 1 PUFF

IO--\> 2 PUFFS

INHL,NASAL (1,2)

PUFF(S) IO--\> 1 PUFF

IO--\> 2 PUFFS

INHL,ORAL (1,2)

PUFF(S) IO--\> 1 PUFF

IO--\> 2 PUFFS

INJ (1,2)

(No Nouns)

INJ (IN OIL) (1,2)

(No Nouns)

INJ,CONC (1,2)

(No Nouns)

INJ,CONC, W/BUF (1,2)

(No Nouns)

INJ,CONC-SOLN (1,2)

(No Nouns)

INJ,FROZEN (1,2)

(No Nouns)

INJ,LYPHL (1,2)

(No Nouns)

INJ,PWDR (1,2)

(No Nouns)

INJ,REPOSITORY (1,2)

(No Nouns)

INJ,SOLN (1,2)

> *Instructions to Noun Conversion Report  
> *\[PSS INSTRUCTIONS REPORT\]

> This report displays the instructions associated with each Dosage Form. The non-numeric instructions can be converted to the NOUN field by using the *Convert Instructions to Nouns* \[PSS CONVERT INSTRUCTIONS\] option.

Example: Instructions to Noun Conversion Report<span id="_Toc495917868" class="anchor"></span>

Select Instructions/Nouns Option: <u>INST</u>ructions to Noun Conversion Report

This report shows the Instructions associated with each Dosage Form. Use the

Convert Instructions to Nouns option to move all non-numeric Instructions into

the Noun field of the Dosage Form file.

DEVICE: HOME// <u>\<RET\></u> TELNET TERMINAL

Instructions Report PAGE: 1

Y in convert column indicates non-numeric (can convert to Noun field)

Dosage Form Instruction Convert

------------------------------------------------------------------------------

ADAPTER

AEROSOL

AEROSOL,ORAL 1

2

AEROSOL,RTL 1

AEROSOL,TOP

AEROSOL,VAG

APPLICATOR 1

BAG

BANDAGE

BAR,CHEWABLE 1

BAR,TOP

BARRIER

BEADS,TOP

BELT

BLOCK

CAP,EC 1

2

CAP,INHL 1

CAP,ORAL 1

2

CAP,SA 1

2

CAP,SPRINKLE 1

2

CAP,SPRINKLE,SA 1

2

CAP/INJ

CATHETER

CHAMBER

CLAMP

COLLAR

CONE

CONTAINER

CONVEX INSERT

CREAM

CREAM,ORAL SPARINGLY Y

LIBERALLY Y

THIN FILM

> *Nouns Enter/Edit*  
> \[PSS ENTER/EDIT NOUNS\]

This option allows the entering and editing of NOUNS and their associated NOUN fields in the DOSAGE FORM file (#50.606). The PACKAGE field will allow a NOUN to be marked for Inpatient Medications and/or Outpatient Pharmacy package use. The PRE-ORDERING ENHANCEMENTS field will designate whether or not the current Outpatient software will recognize a value in the NOUN field. If this field is designated as “YES”, the NOUN field entry will become part of the current functionality. If data is entered into the CONJUNCTION field, it will become part of the Dosage selection display in CPRS for Local Possible Dosages, for Dispense Drugs matched to a Pharmacy Orderable Item with this Dosage Form. It will connect the Local Possible Dosage with the STRENGTH and UNITS for CPRS display.

Example: Nouns Enter/Edit<span id="_Toc495917869" class="anchor"></span>

Select Instructions/Nouns Option: <u>NOU</u>ns Enter/Edit

Select DOSAGE FORM NAME: <u>AEROSOL</u>

1 AEROSOL

2 AEROSOL,ORAL

3 AEROSOL,RTL

4 AEROSOL,TOP

5 AEROSOL,VAG

CHOOSE 1-5: <u>1</u> AEROSOL

Dosage Form =\> AEROSOL

Select NOUN: <u>?</u>

You may enter a new NOUN, if you wish

Answer must be 1-30 characters in length.

Select NOUN: <u>PUFF(S)</u>

Are you adding 'PUFF(S)' as a new NOUN (the 1ST for this DOSAGE FORM)? No// <u>Y</u> (Yes)

NOUN: PUFF(S)//<u>\<RET\></u>

PACKAGE: <u>IO</u> Both

PRE-ORDERING ENHANCEMENT: <u>N</u> NO

Dosage Form =\> AEROSOL

Select NOUN: <u>\<RET\></u>

CONJUNCTION: <u>OF</u>

Select DOSAGE FORM NAME: <u>\<RET\></u>

> *Med Instruction/Frequency*  
> \[PSS MED INSTRUCTION FREQUENCY\]

> This menu provides the *Med Instruction/Frequency* \[PSS MED INSTRUCTION FREQUENCY\] menu options.

> *Edit Medication Instruction Frequency  
> *\[PSS EDIT INSTRUCTION FREQUENCY\]

> This option provides the ability to edit data in the FREQUENCY (IN MINUTES) field in the MEDICATION INSTRUCTION file (#51). This data will be used for calculating default QUANTITY and DAYS SUPPLY values for Outpatient Pharmacy orders.

Example: Edit Med Instruction/Frequency<span id="_Toc495917870" class="anchor"></span>

Select Ordering Enhancements Pre-Release Option: <u>med</u>

1 Med Instruction/Frequency

2 Medication Routes/IV Flag

CHOOSE 1-2: <u>1</u> Med Instruction/Frequency

Select Medication Instruction: <u>?</u>

Answer with MEDICATION INSTRUCTION NAME

Do you want the entire 119-Entry MEDICATION INSTRUCTION List? <u>N</u> (No)

Select Medication Instruction: <u>Q6H</u> EVERY SIX HOURS

FREQUENCY (IN MINUTES): <u>?</u>

Type a Number between 0 and 129600, 0 Decimal Digits

FREQUENCY (IN MINUTES): <u>360</u>

Select Medication Instruction: <u>BID</u>

1 BID TWICE A DAY

2 BIDAP TWICE A DAY IN MORNING AND EVENING

CHOOSE 1-2: <u>1</u> BID TWICE A DAY

FREQUENCY (IN MINUTES): <u>720</u>

> *Medication Instruction Frequency Report  
> *\[PSS FREQUENCY REPORT\]

> This report displays information from the MEDICATION INSTRUCTION file (#51). It can be used to help determine which instructions can have a valid frequency.

Example: Medication Instruction/Frequency Report<span id="_Toc495917871" class="anchor"></span>

This report shows the MEDICATION INSTRUCTION file entries, along with the

Synonym, Frequency and Expansion. Use the Edit Medication Instruction

Frequency option to enter appropriate frequencies.

DEVICE: HOME// <u>\<RET\></u>

MEDICATION INSTRUCTION FREQUENCY REPORT PAGE: 1

NAME SYNONYM FREQUENCY EXPANSION

------------------------------------------------------------------------------

Q34 Q34H EVERY 3-4 HOURS

Q3H Q3 180 EVERY THREE HOURS

Q46 Q46H EVERY 4-6 HOURS

Q4H Q4 240 EVERY FOUR HOURS

Q68 Q68H EVERY 6-8 HOURS

Q6H Q6 360 EVERY SIX HOURS

Q8H Q8 EVERY EIGHT HOURS

QAM EVERY MORNING

# * Medication Routes/IV Flag *\[PSS MEDICATION ROUTES SUB-MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> These options affect the new IV Flag indicator in the MEDICATION ROUTES file (#51.2).

# *Edit Medication Route IV Flag *\[PSS EDIT MED ROUTE IV FLAG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the editing of the IV Flag in the MEDICATION ROUTES file (#51.2).

Example: Edit Medication Route IV Flag<span id="_Toc495917872" class="anchor"></span>

Select Medication Routes/IV Flag Option: <u>ED</u>it Medication Route IV Flag

Select MEDICATION ROUTES NAME: <u>IV</u>

1 IV PIGGYBACK IVPB

2 IV INTRAVENOUS IV

3 IV IA INTRAVENOUS INTRA-ARTICULAR IV IA

4 IV IAER INTRAVENOUS INTRA-ARTERIAL IV IAER

5 IV IAERIA INTRAVENOUS INTRA-ARTERIAL INTRA-ARTICULAR IV IAERIA

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <u>2</u> INTRAVENOUS IV

IV FLAG: YES// <u>?</u>

Enter a '1' for Yes.

Choose from:

0 NO

1 YES

IV FLAG: YES// <u>1</u> YES

Select MEDICATION ROUTES NAME: <u>\<RET\></u>

> *Flag Medication Routes as IV  
> *\[PSS FLAG MED ROUTES AS IV\]*  

> *This option is used to automatically populate the IV FLAG field in the MEDICATION ROUTES file (#51.2) for all routes that are associated with an IV Flagged Orderable Item or contained in Quick Codes in the IV ADDITIVES file (#52.6).

Example: Flag Medication Routes as IV<span id="_Toc495917873" class="anchor"></span>

Select Option: <u>Flag</u> Medication Routes as IV

Flag Medication Routes as IV

This option allows you to automatically populate the IV Flag field in the

Medication Routes file for all Routes associated with IV flagged Orderable

Items, and all Routes contained in Quick Codes in the IV Additive File.

Press Return to continue, '^' to exit: <u>\<RET\></u>

Gathering data.....

Medication Routes to be flagged for IV use:

-----------------------------------------------------------------------------

IM INTRAVENOUS INTRA-ARTERIAL INTRATHECAL

INTRAVENOUS

IV PIGGYBACK

Mark these Medication Routes for IV Use? Yes// <u>\<RET\></u> YES

Flagging Med Routes.....

Finished!

> *Medication Routes flagged for IV Report*  
> \[PSS MEDICATION ROUTES REPORT\]

> This report shows the Medication Routes, their abbreviations, the package use, and the IV Flag status of the Medication Route. The IV Flag helps determine how Inpatient Medication Orders entered through CPRS are finished in the Inpatient Medications package.

### ### Example: Medication Routes flagged for IV Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Option: <u>Med</u>ication Routes flagged for IV Report

Medication Routes flagged for IV Report

This report displays the Medication Routes, along with the abbreviation, the

package use (all packages or National Drug File only), and if the route is

flagged for IV Use or not, which helps determine how Inpatient Med orders

entered through CPRS will be finished in the Pharmacy package.

Med Routes are screened out during CPRS and Pharmacy ordering processes if they

are marked as NDF ONLY, or if they are null.

DEVICE: HOME// <u>\<RET\></u> VIRTUAL Right Margin: 80// <u>\<RET\></u>

MEDICATION ROUTES LIST PAGE: 1

NAME ABBREVIATION USAGE IV

------------------------------------------------------------------------------

BLOOD TEST

BOTH EARS AU ALL

BOTH EYES OU ALL

BUCCAL BUCC ALL

BUCCAL DENTAL INFILTRATION BUCCDENTIF

BUCCAL ORAL BUCCORAL ALL

BUCCAL SUBLINGUAL BUCCSL ALL

BY MOUTH

CATHETER ALL

CAUDAL BLOCK CAUD ALL

CAUDAL EPIDURAL CAUDED ALL

CAUDAL EPIDURAL MISCELLANEOUS CAUDED MISC

CAUDAL SUBCUTANEOUS INFILTRATION CAUDSC IF

DEEP IM

DENTAL DENT ALL

DENTAL INFILTRATION DENTIF ALL

DENTAL INTRAMUSCULAR DENTALIM ALL

DENTAL ORAL DENTORAL ALL

DENTAL ORAL TOPICAL DENTORALTOP ALL

DENTAL SUBCUTANEOUS DENTSC

DENTAL SUBCUTANEOUS INFILTRATION DENTSC IF

DENTAL TOPICAL DENTTOP ALL

DENTAL TOPICAL BUCCAL DENTTOP BUCC

EPIDURAL ED ALL Y

EPIDURAL CAUDAL SUBCUTANEOUS ED CAUDSC ALL

EPIDURAL INFILTRATION CAUDAL ED IF CAUD ALL

EPIDURAL INFILTRATION INTRAVENOUS ED IF IV

EPIDURAL INTRASPINAL INFILTRATION ED IS IF

EPIDURAL INTRATHECAL ED INTH

EPIDURAL RETROBULBAR ED RBUL

EPIDURAL SUBCUTANEOUS INFILTRATION ED SC IF

G TUBE ALL

GARGLE GLUG ALL

IM INTRA-ARTICULAR INTRASYNOVIAL INTRADERMAL IM IA ISY ID

IM INTRAVENOUS INTRA-ARTERIAL INTRATHECAL IM IV IAER INTH ALL

IMPLANT IMP ALL

IN VITRO ALL

INFILTRATION IF ALL

INFILTRATION CAUDAL IF CAUD

INFILTRATION DENTAL IF DEN ALL

INFILTRATION EPIDURAL IF ED

INFILTRATION EPIDURAL CAUDAL IF ED CAUD ALL

INFILTRATION EPIDURAL INTRAMUSCULAR IF ED IM

INFILTRATION INTRAMUSCULAR IF IM

INFILTRATION INTRAVENOUS IF IV Y

End of Report.

*Patient Instructions Enter/Edit*

\[PSS PATIENT INSTRUCTIONS\]

This option provides the ability to edit the PATIENT INSTRUCTIONS field in the PHARMACY ORDERABLE ITEM file (#50.7).

Example: Patient Instructions Enter/Edit<span id="_Toc495917875" class="anchor"></span>

Select Ordering Enhancements Pre-Release Option: <u>PAT</u>ient Instructions Enter/Edit

Select Pharmacy Orderable Item: <u>WARFARIN</u>

1 WARFARIN INJ,CONC, W/BUF

2 WARFARIN TAB

CHOOSE 1-2: <u>2</u> WARFARIN TAB

PATIENT INSTRUCTIONS: <u>??</u>

The text in this field shall be presented as a default for the Patient Instructions prompt in the Outpatient Pharmacy package when entering orders, if the Dispense Drug selected is matched to this Pharmacy Orderable Item.

PATIENT INSTRUCTIONS: <u>TO THIN BLOOD</u>

Select Pharmacy Orderable Item: <u>\<RET\></u>

> *Drug Enter/Edit*

> \[PSS DRUG ENTER/EDIT\]

> This option allows the user to edit fields for ALL pharmacy packages if they possess the proper package key. It also will allow the user to match to NDF and an orderable item. While this is not a new option, new information regarding dosage deletion and creation displays when NDF matching/rematching occurs. The new information is bolded in the screen print below.

Example: Drug Enter/Edit<span id="_Toc495917876" class="anchor"></span>

Select Pharmacy Data Management Option: <u>Drug Ent</u>er/Edit

Select DRUG GENERIC NAME: <u>DIGOXIN 0.125MG</u> TAB CV050

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This entry is marked for the following PHARMACY packages:

Outpatient

Unit Dose

Ward Stock

GENERIC NAME: DIGOXIN 0.125MG TAB// <u>\<RET\></u>

VA CLASSIFICATION: CV050//<u>\<RET\></u>

DEA, SPECIAL HDLG: 6//<u>\<RET\></u>

NATIONAL FORMULARY INDICATOR: YES <u>\<RET\></u>

LOCAL NON-FORMULARY: <u>\<RET\></u>

VISN NON-FORMULARY: <u>\<RET\></u>

Select DRUG TEXT ENTRY: <u>\<RET\></u>

Select FORMULARY ALTERNATIVE: <u>\<RET\></u>

Select SYNONYM: 000081024230// <u>\<RET\></u>

SYNONYM: 000081024230// <u>\<RET\></u>

INTENDED USE: DRUG ACCOUNTABILITY// <u>\<RET\></u>

NDC CODE: 000081-0242-30//<u>\<RET\></u>

Select SYNONYM: <u>\<RET\></u>

MESSAGE: <u>\<RET\></u>

RESTRICTION: <u>\<RET\></u>

FSN: <u>\<RET\></u>

NDC: 0081-0242-30// <u>\<RET\></u>

INACTIVE DATE: <u>\<RET\></u>

WARNING LABEL: <u>\<RET\></u>

ORDER UNIT: BT// <u>\<RET\></u>

PRICE PER ORDER UNIT: 2.86// <u>\<RET\></u>

DISPENSE UNIT: TAB// <u>\<RET\></u>

DISPENSE UNITS PER ORDER UNIT: 30// <u>\<RET\></u>

PRICE PER DISPENSE UNIT: 0.095

points to DIGOXIN 0.125MG TAB in the National Drug file.

This drug has already been matched and classified with the National Drug

file. In addition, if the dosage form changes as a result of rematching,

you will have to match/rematch to Orderable Item.

Do you wish to match/rematch to NATIONAL DRUG file? ? No// <u>YES</u> (Yes)

Deleting Possible Dosages...

Match local drug DIGOXIN 0.125MG TAB

ORDER UNIT: BT

DISPENSE UNITS/ORDER UNITS: 30

DISPENSE UNIT: TAB

I will try to match NDC: 0081-0242-30 to NDF.

Local drug DIGOXIN 0.125MG TAB

matches DIGOXIN 0.125MG TAB

PACKAGE SIZE: 30

PACKAGE TYPE: UNIT DOSE

Is this a match ?

Enter Yes or No: YES// <u>YES</u>

LOCAL DRUG NAME: DIGOXIN 0.125MG TAB

ORDER UNIT: BT

DISPENSE UNITS/ORDER UNITS: 30

DISPENSE UNIT: TAB

VA PRODUCT NAME: DIGOXIN 0.125MG TAB

VA PRINT NAME: DIGOXIN (LANOXIN) 0.125MG TAB CMOP ID: D0080

VA DISPENSE UNIT: TAB MARKABLE FOR CMOP: YES

PACKAGE SIZE: 30

PACKAGE TYPE: UNIT DOSE

VA CLASS: CV050 DIGITALIS GLYCOSIDES

INGREDIENTS:

NATIONAL FORMULARY INDICATOR: YES

NATIONAL FORMULARY RESTRICTION:

\< Enter "Y" for yes, "N" for no \>

Is this a match ? <u>YES</u>

You have just VERIFIED this match and MERGED the entry.

Resetting Possible Dosages...Use the 'Dosages Enter/Edit' option to review newly created dosages for

# DIGOXIN 0.125MG TAB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Press Return to continue: <u>\<RET\></u>

Just a reminder...you are editing DIGOXIN 0.125MG TAB.

Appendix A<span id="_Toc495917877" class="anchor"></span>

The dosage form/unit combinations that have been designated as convertible for the creation of Possible Dosages are displayed in the following table.

<u>Dosage Form</u><u>Unit</u><u>Package</u>

CAP,EC MG Both

CAP,INHL MCG Both

MG Both

CAP,ORAL GM Both

MCG Both

MG Both

MG/PKG Both

MIC Both

MIL Both

MIN Both

ML Both

UNT Both

CAP,SA MEQ Both

MG Both

UNT Both

CAP,SPRINKLE MG Both

CAP,SPRINKLE,SA MG Both

DENTAL CONE MG Both

DROPS,ORAL MG/0.6ML Inpatient

MG/ML Inpatient

UNT/ML Inpatient

ELIXIR MEQ/15ML Inpatient

MEQ/5ML Inpatient

> MG/10.15ML Inpatient

> MG/15ML Inpatient

> MG/5ML Inpatient

> MG/ML Inpatient

EMULSION GM/15ML Inpatient

UNT Inpatient

ENEMA MG/60ML Inpatient

ENEMA,RTL MG/5ML Inpatient

FLUID EXTRACT GM/ML Inpatient

GEL MCG/0.1ML Inpatient

> MG/2.5ML Inpatient

> MG/3GM Inpatient

> MG/5ML Inpatient

> MG/UNT Inpatient

GRANULES GM Inpatient

> GM/PKT Inpatient

> MG Inpatient

> MG/5ML Inpatient

GRNL,EFFERVSC MEQ/PKG Inpatient

GRNL,RCNST-ORAL GM/PKG Inpatient

> MG/2.5ML Inpatient

> MG/5ML Inpatient

> MG/ML Inpatient

> MG/PKT Inpatient

GUM,CHEWABLE MG Inpatient

IMPLANT MG Inpatient

INJ GM Inpatient

> GM/100ML Inpatient

> GM/3ML Inpatient

> GM/50ML Inpatient

> GM/BAG Inpatient

> GM/BTL Inpatient

> GM/ML Inpatient

> GM/VIAL Inpatient

> MBq/ML Inpatient

> MBq/VIL Inpatient

> MCG/0.5ML Inpatient

> MCG/ML Inpatient

> MCG/VIL Inpatient

> MEQ/L Inpatient

> MEQ/ML Inpatient

> MG Inpatient

> MG/0.2ML Inpatient

> MG/0.3ML Inpatient

> MG/0.4ML Inpatient

> MG/0.5ML Inpatient

> MG/0.5ML Inpatient

> MG/0.625ML Inpatient

> MG/0.6ML Inpatient

> MG/0.8ML Inpatient

> MG/10ML Inpatient

> MG/2ML Inpatient

> MG/5ML Inpatient

> MG/AMP Inpatient

> MG/BAG Inpatient

> MG/ML Inpatient

> MG/VIAL Inpatient

> MIC/VIL Inpatient

> MIL/ML Inpatient

> MIL/VIL Inpatient

> MILLION UNT/VIL Inpatient

> ML Inpatient

> PNU Inpatient

> PNU/ML Inpatient

> UNT Inpatient

> UNT/0.1ML Inpatient

> UNT/0.2ML Inpatient

> UNT/0.5ML Inpatient

> UNT/AMP Inpatient

> UNT/ML Inpatient

> UNT/TEST Inpatient

> UNT/VIL Inpatient

> mgI/ml Inpatient

> nKatU/ML Inpatient

INJ (IN OIL) MG/ML Inpatient

INJ,CONC MG/50ML Inpatient

> MG/5ML Inpatient

> MG/VIAL Inpatient

> MG/ML Inpatient

INJ,CONC, W/BUF MG/ML Inpatient

MG/VIAL Inpatient

INJ,CONC-SOLN MEQ/ML Inpatient

MG/10ML Inpatient

MG/ML Inpatient

INJ,FROZEN MG/ML Inpatient

INJ,LYPHL GM/VIAL Inpatient

> MCG/VIL Inpatient

> MG/AMP Inpatient

> MG/VIAL Inpatient

> UNT/AMP Inpatient

> UNT/VIL Inpatient

INJ,PWDR GM/BTL Inpatient

> GM/VIAL Inpatient

> MG Inpatient

> MG/VIAL Inpatient

> UNT/VIL Inpatient

INJ,REPOSITORY MG/ML Inpatient

UNT/ML Inpatient

INJ,SOLN GM Inpatient

> GM/100ML Inpatient

> GM/20ML Inpatient

> GM/50ML Inpatient

> GM/AMP Inpatient

> GM/BAG Inpatient

> GM/BTL Inpatient

> GM/KIT Inpatient

> GM/ML Inpatient

> GM/VIAL Inpatient

> MCG/0.3ML Inpatient

> MCG/0.5ML Inpatient

> MCG/ML Inpatient

> MEQ/100ML Inpatient

> MEQ/50ML Inpatient

> MEQ/ML Inpatient

> MG Inpatient

> MG/0.3ML Inpatient

> MG/0.5ML Inpatient

> MG/0.5ML Inpatient

> MG/0.7ML Inpatient

> MG/2ML Inpatient

> MG/AMP Inpatient

> MG/INJ Inpatient

> MG/ML Inpatient

> MG/SYRINGE Inpatient

> MG/UNT Inpatient

> MG/VIAL Inpatient

> MIC/0.6ML Inpatient

> MIC/1.5ML Inpatient

> MIC/VIL Inpatient

> MIL Inpatient

> MIL/ML Inpatient

> MILLION UNT/SYR Inpatient

> MILLION UNT/VIL Inpatient

> PNU/ML Inpatient

> UNT Inpatient

> UNT/0.1ML Inpatient

> UNT/0.2ML Inpatient

> UNT/0.5ML Inpatient

> UNT/0.6ML Inpatient

> UNT/AMP Inpatient

> UNT/ML Inpatient

> UNT/TEST Inpatient

> UNT/VIL Inpatient

> VIL Inpatient

> mgI/ml Inpatient

INJ,SOLN,SA MG/ML Inpatient

INJ,SUSP GM/VIAL Inpatient

> MCG/ML Inpatient

> MG/ML Inpatient

> MIL/ML Inpatient

> MILLION UNT/VIL Inpatient

> UNT/0.5ML Inpatient

> UNT/1.2ML Inpatient

> UNT/ML Inpatient

INJ,SUSP,SA MG Inpatient

MG/ML Inpatient

INJ,SUSP-DRY,SA MG Inpatient

MG/VIAL Inpatient

INJ/IMPLANT MG Inpatient

INSERT,CONT REL MG Inpatient

MG/CAP Inpatient

INSERT,CONT REL,OPH MG/UNT Inpatient

INSERT,VAG MG Inpatient

LIQUID GM Inpatient

> MEQ/15ML Inpatient

> MG Inpatient

> MG/15ML Inpatient

> MG/5ML Inpatient

> MG/GTT Inpatient

> MG/ML Inpatient

LIQUID,ORAL GM Inpatient

> GM/10ML Inpatient

> GM/UNT Inpatient

> MEQ/15ML Inpatient

> MG Inpatient

> MG/0.6ML Inpatient

> MG/15ML Inpatient

> MG/2.5ML Inpatient

> MG/4ML Inpatient

> MG/5ML Inpatient

> MG/MIN Inpatient

> MG/ML Inpatient

> UNT/0.1ML Inpatient

> UNT/ML Inpatient

LOZENGE MCG Inpatient

> MG Inpatient

> UNT Inpatient

OPHTHALMIC,CRC MG/UNT Inpatient

PELLET MG Inpatient

POWDER GM Inpatient

> GM/1.7GM Inpatient

> GM/5GM Inpatient

> GM/9GM Inpatient

> GM/BAG Inpatient

> GM/BTL Inpatient

> GM/CUP Inpatient

> GM/PKT Inpatient

> MG Inpatient

UNT/VIL Inpatient

POWDER,ORAL GM Inpatient

> GM/5GM Inpatient

> GM/CUP Inpatient

> GM/PKG Inpatient

> MG/GM Inpatient

POWDER,TOP GM Inpatient

UNT/GM Inpatient

PWDR,EFFERVSC MEQ/PKT Inpatient

PWDR,RENST-ORAL CAL/ML Inpatient

> GM Inpatient

> GM/5GM Inpatient

> GM/BTL Inpatient

> GM/PKG Inpatient

> GM/PKT Inpatient

> GM/UNT Inpatient

> MEQ/PKT Inpatient

> MG/5ML Inpatient

> MG/ML Inpatient

> MG/PKG Inpatient

> MG/PKT Inpatient

> UNT/5ML Inpatient

RING,VAG MG Inpatient

SOLN MG/5ML Inpatient

> MG/ML Inpatient

> MIL Inpatient

> MIL/ML Inpatient

> UNT/ML Inpatient

SOLN,CONC MG/5ML Inpatient

MG/ML Inpatient

SOLN,INHL MG/5ML Inpatient

MG/ML Inpatient

SOLN,IRRG MG/ML Inpatient

SOLN,NASAL MCG/SPRAY Inpatient

MG/ML Inpatient

UNT/SPRAY Inpatient

SOLN,ORAL GM/ML Inpatient

> MEQ/15ML Inpatient

> MEQ/5ML Inpatient

> MG Inpatient

> MG/0.5ML Inpatient

> MG/0.5ML Inpatient

> MG/18.75ML Inpatient

> MG/20ML Inpatient

> MG/5ML Inpatient

> MG/7.5ML Inpatient

> MG/ML Inpatient

> MIL/ML Inpatient

> UNT/ML Inpatient

SOLN,RTL MG/ML Inpatient

SOLN,SPRAY,NASAL MCG/SPRAY Inpatient

MG/SPRAY Inpatient

UNT/ML Inpatient

SUPP,RTL MG Inpatient

SUPP,VAG GM Inpatient

MG Inpatient

SUPPOSITORY MCG Inpatient

SUSP GM/5ML Inpatient

> GM/60ML Inpatient

> MG/15ML Inpatient

> MG/5ML Inpatient

> MG/ML Inpatient

> UNT/ML Inpatient

SUSP,INTRATHECAL MG/ML Inpatient

SUSP,ORAL MCG/ML Inpatient

> MG/15ML Inpatient

> MG/5ML Inpatient

> MG/ML Inpatient

> UNT/ML Inpatient

SUSP,RTL GM/60ML Inpatient

SYRINGE UNT Inpatient

SYRUP GM/15ML Inpatient

> GM/5ML Inpatient

> MEQ/5ML Inpatient

> MG/15ML Inpatient

> MG/5ML Inpatient

> MG/ML Inpatient

SYRUP,ORAL MG/5ML Inpatient

TAB GM Both

> GR Both

> MCG Both

> MEQ Both

> MG Both

> MG/5ML Inpatient

> MG/DAY Inpatient

> UNT Both

TAB,BUCC,SA MG Both

TAB,BUCCAL MG Both

TAB,CHEWABLE GM Both

MG Both

TAB,EC GM Both

> GR Both

> MEQ Both

> MG Both

> UNT Both

TAB,EFFERVSC MEQ Both

MG Both

TAB,ORAL MCG Both

MG Both

UNT Both

TAB,ORAL DISINTEGRATING MG Both

TAB,RAPID DISINTEGRATE MG Both

TAB,SA GM Both

MEQ Both

MG Both

TAB,SOLUBLE MG Both

TAB,SUBLINGUAL MG Both

TAB,VAG MG Both

UNT Both

TAMPON MG Inpatient

TAPE MCG/SQCM Inpatient

TINCTURE MG/5ML Inpatient

MG/ML Inpatient

TROCHE MG Inpatient

WAFER GM Inpatient

MG Inpatient