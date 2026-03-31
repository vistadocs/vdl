---
title: PSS*1*129 Release Notes - Pharmacy Reengineering (PRE) V.0.5 Pre-Release
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Pharmacy Reengineering (PRE) V.0.5 Pre-Release
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 1
patch_id: PSS*1*129
group_key: "PSS:PSS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - medication
  - management
  - route
  - pharmacy
  - local
  - report
  - routes
  - edit
  - dosages
  - standard
page_count: 0
word_count: 2459
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: February 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p129_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p129_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

![](pss-1-129-release-notes-pharmacy-reengineering-pre-v-0-5-pre-release/001.png)

PHARMACY REENGINEERING (PRE) Version 0.5Pre-Release

####### RELEASE NOTES 

PSS\*1\*129

February 2009

Office of Enterprise Development

Table of Contents

*(This page included for two-sided copying)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Enhancements](#enhancements)
  - [Menu Changes](#menu-changes)
  - [New Options](#new-options)
  - [Changed Options](#changed-options)
  - [New Files](#new-files)
  - [New Fields](#new-fields)
  - [Changed Fields](#changed-fields)
- [Other Functionality](#other-functionality)
- [Impacts to Other Packages](#impacts-to-other-packages)
The goal of the Pharmacy Reengineering (PRE) project is to replace the current M-based suite of pharmacy applications with a system that will better meet the current and expected business needs for the Department of Veterans Affairs (VA) and address the ever-changing patient safety issues. The first phase, PRE V. 0.5, will implement enhanced order checking functionality utilizing HealtheVet (HeV) compatible architecture and First DataBank (FDB) Drug Information Framework (DIF) Application Program Interfaces (APIs) and database.
It has been determined that local facilities must perform certain file mapping, setup and review tasks to prepare for the new dosing checks to be implemented in PRE V. 0.5. Patch PSS\*1.0\*129, known as the PRE V.0.5 Pre-Release patch, will provide the means for sites to accomplish these tasks.
This release notes document provides a brief description of the new features and functions of the PRE V.0.5 Pre-Release patch PSS\*1\*129. More detailed information on the steps sites need to follow to prepare for PRE V.0.5 is provided in the *Pharmacy Reengineering (PRE) Version 0.5 Pre-Release Implementation Guide*. Additional information is available in the *Pharmacy Data Management V.1.0 User Manual* and *Pharmacy Data Management V.1.0 Technical Manual*.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software will provide the following enhancements:

- Improved PDM menu structure to group related options
- A new menu containing all the options needed to perform PRE V.0.5 Pre-Release tasks
- New fields, files, reports and options to assist in the population and maintenance of data necessary to
  - Map Local Medication Routes to a Standard Medication Route
  - Breakdown a free text Local Possible Dosage to a Numeric Dose and Dose Unit
  - Review Administration Schedules and Medication Instruction file entries to ensure a frequency has been defined if appropriate
  - Identify IV Solutions that are considered PreMixes

## Menu Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new *Enhanced Order Checks Setup Menu* has been created under the main *Pharmacy Data Management* menu. The existing *Pharmacy Data Management* menu has been restructured to add some of the same new reports and options on the *Enhanced Order Checks Setup Menu*. The *Enhanced Order Checks Setup Menu* will be deleted once PRE V. 0.5 is released. Details on the new and modified options can also be found in the *Pharmacy Reengineering (PRE) V.0.5 Pre-Release Implementation Guide*, *Pharmacy Data Management (PDM) V.1.0 User Manual* and *Pharmacy Data Management (PDM) V.1.0 Technical Manual*.

Restructured Pharmacy Data Management menu (new sub-menus are bolded)

Select Pharmacy Data Management Option: <u>??</u>

CMOP Mark/Unmark (Single drug) \[PSSXX MARK\]

\*\*\> Locked with PSXCMOPMGR

Dosages ... \[PSS DOSAGES MANAGEMENT\]

Drug Enter/Edit \[PSS DRUG ENTER/EDIT\]

Drug Interaction Management ... \[PSS DRG INTER MANAGEMENT\]

Electrolyte File (IV) \[PSSJI ELECTROLYTE FILE\]

Lookup into Dispense Drug File \[PSS LOOK\]

Medication Instruction Management ... \[PSS MED INSTRUCTION MANAGEMENT\]Medication Routes Management ... \[PSS MEDICATION ROUTES MGMT\]

Orderable Item Management ... \[PSS ORDERABLE ITEM MANAGEMENT\]

Formulary Information Report \[PSSNFI\]

Drug Text Management ... \[PSS DRUG TEXT MANAGEMENT\]

Pharmacy System Parameters Edit \[PSS SYS EDIT\]

Standard Schedule Management ... \[PSS SCHEDULE MANAGEMENT\]

Synonym Enter/Edit \[PSS SYNONYM EDIT\]

Controlled Substances/PKI Reports ... \[PSS CS/PKI REPORTS\]

Send Entire Drug File to External Interface \[PSS MASTER FILE ALL\]

Enhanced Order Checks Setup Menu ... \[PSS ENHANCED ORDER CHECKS\]

IV Solution Report \[PSS IV SOLUTION REPORT\]

Warning Builder \[PSS WARNING BUILDER\]

Warning Mapping \[PSS WARNING MAPPING\]

New Enhanced Order Checks Setup Menu (options duplicated on other menus are bolded)

Select Enhanced Order Checks Setup Menu Option: <u>??</u>

Find Unmapped Local Medication Routes \[PSS MED ROUTES INITIAL MAPPING\]

Map Local Medication Route to Standard \[PSS MAP ONE MED ROUTE\]

Medication Route Mapping Report \[PSS MED ROUTE MAPPING REPORT\]Medication Route File Enter/Edit \[PSS MEDICATION ROUTES EDIT\]Medication Route Mapping History Report \[PSS MED ROUTE MAPPING CHANGES\]Request Change to Standard Medication Route \[PSS MEDICATION ROUTE REQUEST\]

Find Unmapped Local Possible Dosages \[PSS LOCAL DOSAGES EDIT ALL\]

Map Local Possible Dosages \[PSS LOCAL DOSAGES EDIT\]

Local Possible Dosages Report \[PSS LOCAL POSSIBLE DOSAGES\]

Strength Mismatch Report \[PSS STRENGTH MISMATCH\]

Enter/Edit Dosages \[PSS EDIT DOSAGES\]Request Change to Dose Unit \[PSS DOSE UNIT REQUEST\]

Mark PreMix Solutions \[PSS MARK PREMIX SOLUTIONS\]

IV Solution Report \[PSS IV SOLUTION REPORT\]Administration Schedule File Report \[PSS SCHEDULE REPORT\]Medication Instruction File Report \[PSS MED INSTRUCTION REPORT\]

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: These options do not affect the current functionality of the Inpatient Medications, Outpatient Pharmacy, or CPRS applications.

Unless otherwise noted, the options listed below can be found under the *Enhanced Order Checks Setup Menu* on the main *Pharmacy Data Management* menu. Some options have also been added to other menus as noted.

*Administration Schedule File Report* \[PSS SCHEDULE REPORT\] option prints out entries from the ADMINISTRATION SCHEDULE file in order to check whether a frequency is defined, if appropriate, for all standard schedules marked for pharmacy use. The option is also found under the *Standard Schedule Management* menu.

*Drug Text Management* \[PSS DRUG TEXT MANAGEMENT\] menu option is located on the main *Pharmacy Data Management* menu and contains the *Drug Text Enter/Edit* and *Drug Text File Report* options moved from the main *Pharmacy Data Management* menu.

*Find Unmapped Local Medication Routes* \[PSS MED ROUTES INITIAL MAPPING\] option loops through all Medication Route entries, finds any marked for 'ALL PACKAGES' that are not mapped to a Standard Medication Route, and prompts for the mapping.

*Find Unmapped Local Possible Dosages* \[PSS LOCAL DOSAGES EDIT ALL\] option loops through all Local Possible Dosages, identifies entries eligible for dosage checks that do not have data in the new Dose Unit and Numeric Dose fields, and prompts for data entry into these fields.

*IV Solution Report* \[PSS IV SOLUTION REPORT\] option displays all IV Solutions or just those entries marked as PreMixes. This option is also found under the main *Pharmacy Data Management Menu*.

*Local Possible Dosages Report* \[PSS LOCAL POSSIBLE DOSAGES\] option displays any Local Possible Dosages with missing values for Dose Unit or Numeric Dose, or displays all Local Possible Dosages and their Dose Unit and Numeric Dose values. This option is also found under the *Dosages* menu.

*Map Local Medication Route to Standard* \[PSS MAP ONE MED ROUTE ROUTES\] option provides the ability to select an entry from the Medication Routes file and map/remap it to an entry in the Standard Medication Routes file.

*Map Local Possible Dosages* \[PSS LOCAL DOSAGES EDIT\] option allows edits to the new Dose Unit and Numeric Dose fields. This data needs to be populated for Dosage checks to be performed when that Local Possible Dosage is selected for an order.

*Mark Premix Solutions* \[PSS MARK PREMIX SOLUTIONS\] option can be used to mark an IV Solution as a PreMix so that it can be included in order checks when PRE V.0.5 is installed.

*Medication Instruction File Report* \[PSS MED INSTRUCTION REPORT\] prints out entries from the Medication Instruction file to check whether a frequency is defined, if appropriate. This option is also located under the *Medication Instruction Management* menu*.Medication Instruction Management* \[PSS MED INSTRUCTION MANAGEMENT\] menu is located on the main *Pharmacy Data Management* menu and contains the *Medication Instruction File Add/Edit* and the new *Medication Instruction File Report* options.

*Medication Routes Management* \[PSS MEDICATION ROUTES MGMT\] menu option is located on the main *Pharmacy Data Management* menu and contains *Medication Route File Enter/Edit*, *Medication Route Mapping Report*, *Medication Route Mapping History Report*, and *Request Change to Standard Medication Route* options.

*Medication Route Mapping History Report* \[PSS MED ROUTE MAPPING CHANGES\] option shows all the mapping changes between a single entry or all entries from the Medication Routes file to entries in the Standard Medication Routes file over a specified timeframe. This option is also located under the *Medication Routes Management* menu.

*Medication Route Mapping Report* \[PSS MED ROUTE MAPPING REPORT\] shows the status of the current mapping from the Medication Routes file to the Standard Medication Routes file. This option is also located under the *Medication Routes Management* menu.

*Request Change to Dose Uni*t \[PSS DOSE UNIT REQUEST\] option enables a request to be made to have a new entry added, or a current entry changed in the new Dose Units file. Requests are submitted via a mail message to a review committee including representatives from Pharmacy Benefits Management (PBM), Pharmacy Subject Matter Experts (SME) and the Pharmacy Reengineering (PRE) team. This option is also found under the *Dosages* menu.

*RequestChange to Standard Medication Route* \[PSS MEDICATION ROUTE REQUEST\] option provides a means to request changes and additions to the Standard Medication Routes. Requests are submitted via a mail message to a review committee including representatives from Standards and Terminology Services (STS), Pharmacy Benefits Management (PBM), Pharmacy Subject Matter Experts (SME) and the Pharmacy Reengineering (PRE) team. This option is also located under the *Medication Routes Management* menu.

*Standard Schedule Management* \[PSS SCHEDULE MANAGEMENT\] menu option is located on the main *Pharmacy Data Management* menu and contains *Standard Schedule Edit* and *Administration Schedule File Report* options.

*Strength Mismatch Report* \[PSS STRENGTH MISMATCH\] option shows any strength mismatches between local Drug file entries and a VA Product to which they are matched. This report can only identify local Drug file entries that qualify for Possible Dosages and have a Strength defined in the Drug file. This report is temporary and will be removed from the package when the PRE V.0.5 functionality is installed.

## Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Dosage Form File Enter/Edit* \[PSS DOSAGE FORM EDIT\] option has been changed to no longer allow the creation of a new Local Medication Route.

*Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option has been modified to facilitate population of the new Local Possible Dosage fields and the marking of an IV Solution as a PreMix.

*Enter/Edit Dosages* \[PSS EDIT DOSAGES\] option has been modified to facilitate population of the new Local Possible Dosage fields*.* It remains under the Dosages menu and has been added to the new the *Enhanced Order Checks Setup Menu*.

*Medication Route File Enter/Edit* \[PSS MEDICATION ROUTES EDIT\] option has been changed to allow for mapping/remapping of a Local Medication Route to a Standard Medication Route. This option has been moved from the main *Pharmacy Data Management* menu to under the *Enhanced Order Checks Setup Menu* and under the *Medication Routes Management* menu.

*Primary Solution File (IV)* \[PSSJI SOLN\] has been modified to facilitate the marking of an IV Solution as a PreMix.

*Review Dosages Report* \[PSS DOSAGE REVIEW REPORT\] option has been modified to display data from the two new Local Possible Dosage fields.

## New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new STANDARD MEDICATION ROUTES file (#51.23) was created to map Local Medication Routes in VistA to a Standard Medication Route in order to perform dosage checks in PRE V.0.5. This file has been standardized by Standards and Terminology Service (STS) and mapped to a First DataBank (FDB) Route. It cannot be edited locally.

A list of all Standard Medication Routes and corresponding FDB Route mapping initially released with the PRE V.0.5 Pre-Release patch can be found in Appendix A of the *Pharmacy Reengineering (PRE) Version 0.5 Pre-Release Implementation Guide*.

Any additions or changes to the Standard Medication Route file will be pushed out by the New Term Rapid Turnaround (NTRT) process. For a complete listing, use FileMan to print the NAME field (#.01) and FIRST DATABANK MED ROUTE field (#1) from the STANDARD MEDICATION ROUTE file (#51.23).

A new DOSE UNITS file (#51.24) was created. All entries in this file have been mapped to an FDB Dose Unit. Although this file has not yet been standardized by STS, no local editing will be allowed. When populating the Dose Unit field for a Local Possible Dosage, selection will be from this new file. The initial list of Dose Unit values and corresponding FDB Dose Unit mapping is provided in Appendix B of the *Pharmacy Reengineering (PRE) Version 0.5 Pre-Release Implementation Guide*.

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMERIC DOSE field (#5) and DOSE UNIT field (#4) have been created in the LOCAL POSSIBLE DOSAGE multiple (#50.0904) of the DRUG file (#50).

EXCLUDE FROM DOSAGE CHECKS field (#11), has been created in the DOSAGE FORM file (#50.606). This field contains an indicator of whether or not this Dosage Form will be excluded from Dosage checks. Initially populated during the PSS\*1\*129 post-init, subsequent updates to this field will be sent out via the regular NDF data update patches.

The initial list of Dosage Forms to be excluded is provided in Appendix C of the *Pharmacy Reengineering (PRE) Version 0.5 Pre-Release Implementation Guide*.

The following fields have been added to the MEDICATION ROUTES file (#51.2): STANDARD MEDICATION ROUTE field (#10); STANDARD MED ROUTE CHANGE LOG sub-file field (#7). This sub-file contains the ACTIVITY DATE AND TIME  field (#.01), PERSON MAKING CHANGE field (#1),  OLD VALUE field (#2) and NEW VALUE field (#3).

PREMIX field (#18) has been added to the IV SOLUTIONS file (#52.7).

> **NOTE:** National Drug File patch PSN\*4\*169, released in conjunction with PSS\*1\*129, adds the OVERRIDE DF DOSE CHK EXCLUSION field (#31) to the VA PRODUCT file (#50.68) to override dosage form exclusions for a VA Product as described above. For example, if the dosage form is set to be excluded from dosage checks and the override field in the VA PRODUCT file is set to ‘Yes’, a dosage check will be performed on a dispense drug that is matched to this VA Product. An initial list of VA Products that have the new OVERRIDE DF DOSE CHK EXCLUSION field (#31) set to ‘Yes’ is provided in Appendix D of the *Pharmacy Reengineering (PRE) Version 0.5 Pre-Release Implementation Guide*.

## Changed Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MED ROUTE FOR DOSAGE FORM field (#.01) of the MED ROUTE FOR DOSAGE FORM multiple (#50.6061) in the DOSAGE FORM file (#50.606) was changed by removing LAYGO to prevent creation of a new Medication Route through the *Dosage Form File Enter/Edit* option.

# Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The POST-INIT routine PSSPO129 will perform the following tasks:

> 1\) Set the Read Access of the STANDARD MEDICATION ROUTES file (#51.23) to “Pp.”

> 2\) Set the Read Access of the DOSE UNITS file (#51.24) to "Pp."

> 3\) Initiate the VHA Unique Identifier (VUID) population for the STANDARD MEDICATION ROUTES file (#51.23). Any updates (i.e. new additions) to the file since the initial creation of the patch will also occur.

> 4\) Rebuild the Pharmacy Data Management menu structure.

> 5\) Populate the EXCLUDE FROM DOSAGE CHECKS field (#11) of the DOSAGE FORM file (#50.606), using the XPDGREF variable that was set in the PRE-TRANSPORT routine.

> 6\) Auto-map entries from the MEDICATION ROUTES file (#51.2) to entries in the STANDARD MEDICATION ROUTES file (#51.23).

> 7\) Auto-populate the new DOSE UNIT field (#4) and NUMERIC DOSE field (#5) in the LOCAL POSSIBLE DOSAGE sub-file (#50.0904) of the DRUG file (#50).

> 8\) Generate the mail message indicating the POST-INIT routine has run to completion.

As a follow-up to the PRE-INSTALLATION instructions, if you had any locally added menu options under the Pharmacy Data Management \[PSS MGR\] menu option or any of its sub-menus, please check to see if they need to be re-attached once the POST-INSTALL is complete and the VistA mail message indicating this has been received.

<u>Note if for some reason this patch is installed multiple times</u>: On all subsequent installs, attempts will be made to auto-populate the Standard Medication Route field for a Medication Routes File entry only if the field is not already populated and to populate the Numeric Dose and Dose Unit fields for a Local Possible Dosage in the Drug File only if both fields are empty.

# Impacts to Other Packages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These options do not affect the current functionality of the Inpatient Medications, Outpatient Pharmacy, or CPRS applications.