---
title: MOCHA Version 2.1a Release Notes (PSS*1*201)
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: a  (PSS*1*201)
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 2.1
patch_id: PSS*2.1*201
group_key: "PSS:PSS:2.1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - dose
  - table
  - contents
  - schedule
  - instruction
  - medication
  - check
  - dosing
  - frequency
  - order
page_count: 0
word_count: 1880
section_count: 9
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: May 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_201_rn_r0517.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_201_rn_r0517.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

![](mocha-version-2-1a-release-notes-pss-1-201/001.png)

Medication order check healthcare application (mocha) v2.1a

Release Notes

PSS\*1\*201

May 2017

Product Development

*(This page included for two-sided copying.)*Table of Contents

*  
(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Enhancements](#enhancements)
- [Menu Changes](#menu-changes)
  - [New Options](#new-options)
  - [Changed Options](#changed-options)
  - [Deleted Options](#deleted-options)
  - [New Files](#new-files)
  - [Modified Fields](#modified-fields)
  - [New Fields](#new-fields)
  - [Security Key](#security-key)
  - [Modified Templates](#modified-templates)
- [Other Functionality](#other-functionality)
- [Impacts to Other Packages](#impacts-to-other-packages)
- [Known Anomalies](#known-anomalies)
The goal of the Pharmacy Reengineering (PRE) project is to replace the current M-based suite of Pharmacy applications with a system that will better meet the current and expected business needs for the Department of Veterans Affairs (VA) and address the ever-changing patient safety issues. The first phase, Medication Order Check Healthcare Application (MOCHA) v1.0, implemented enhanced order checking functionality utilizing Health*e*Vet (H*e*V) compatible architecture and First Databank (FDB) MedKnowledge Framework (formerly DIF) Application Program Interfaces (APIs), and database for Drug Interaction and Duplicate Therapy order checks. MOCHA v2.0 implemented the Maximum Single Dose Order Check for simple and complex medication orders. MOCHA v2.1a releases new fields, updated options, and one new file that are essential to the implementation of the Max Daily Dose Order Check for simple medication orders in the future MOCHA v2.1b release.
This release notes document provides a brief description of the new fields, new file, and updated options for the MOCHA v2.1a application via the PSS\*1\*201 patch. More detailed information on the functionality can be found in the application user and technical manuals found on the Virtual Documentation Library (VDL).

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA v2.1a will provide the following enhancements:

- Add new fields to both the ADMINISTRATION SCHEDULE file (#51.1) and the MEDICATON INSTRUCTION file (#51) to define a frequency for a schedule or medication instruction used within a medication order for specific dispense drug(s) or for all drugs in order to perform a Max Daily Dose Order Check.
- Add new fields to both the ADMINISTRATION SCHEDULE file (#51.1) and the MEDICATION INSTRUCTION file (#51) to be able to derive a frequency value to perform a Max Daily Dose Order Check when the name of a schedule or medication instruction has been changed.
- Modify *Standard Schedule Edit* \[PSS SCHEDULE EDIT\] option to allow editing of the new frequency fields.
- Modify *Administration Schedule File Report* \[PSS SCHEDULE REPORT\] option to display data entered in the frequency fields.
- Modify *Medication Instruction File Add/Edit* \[PSSJU MI\] option to allow editing of the new frequency fields.
- Modify *Medication Instruction File Report* \[PSS MED INSTRUCTION REPORT\] option to display data entered in the new frequency fields.
- Modify entries to the DOSE UNITS file (#51.24), see section 4 for details.
- Create a new file called DOSE UNIT CONVERSION (#51.25) to convert one dose unit to another using a conversion factor so that a comparison can be made between two dose units when they are not equivalent.
- Add new entries to the APSP INTERVENTION TYPE file (#9009032.3), MAX DAILY DOSE and MAX SINGLE DOSE & MAX DAILY DOSE.
- Enhance the free text dosage logic for dosing ranges for medication orders entered through Pharmacy and Computerized Patient Record System (CPRS).
- Enhance the free text dosage logic for multi-ingredient product medication orders entered through CPRS.
- Enhance free text logic to handle information data placed in parenthesis which is found in the dosage ordered field for an order.
- Modify the VistA XML parsing code for the DOSING_INFO and DRUG_INFO Web Services to properly interpret all attributes returned with future versions of Mocha Server.

# Menu Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No menu changes have been made.

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new options have been created.

## Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options have been changed:

- The *Standard Schedule Edit* \[PSS SCHEDULE EDIT\] option has been modified to allow editing of the DOSING CHECK FREQUENCY field (#11), DRUG(S) FOR DOSING CHK FREQ (#11.1), and OLD SCHEDULE NAME(S) field (#13) for a schedule.
- The *Administration Schedule File Report* \[PSS SCHEDULE REPORT\] option has been modified to allow display of the DOSING CHECK FREQUENCY field (#11), DRUG(S) FOR DOSING CHK FREQ (#11.1), and OLD SCHEDULE NAME(S) field (#13) from the ADMINISTRATION SCHEDULE file (#51.1) for a schedule.
- The *Medication Instruction File Add/Edit* \[PSSJU MI\] option has been modified to allow editing of the DOSING CHECK FREQUENCY field (#32), DRUG(S) FOR DOSING CHK FREQ field (#32.1), and OLD MED INSTRUCTION NAME(S) field (#33) for a medication instruction.
- The *Medication Instruction File Report* \[PSS MED INSTRUCTION REPORT\] option has been modified to allow display of the DOSING CHECK FREQUENCY field (#32), DRUG(S) FOR DOSING CHK FREQ (#32.1), and OLD MED INSTRUCTION NAME(S) field (#33) from the MEDICATION INSTRUCTION file (#51) for a medication instruction.

## Deleted Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No options have been deleted.

## New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following file has been added:

A new DOSE UNIT CONVERSION file (#51.25) was created. Although this file has not yet been standardized by Standards & Terminology Service (STS), no local editing will be allowed. The Read Access of the DOSE UNIT CONVERSION file (#51.25) has been set to "Pp." The DOSE UNIT CONVERSION file will be used to convert one dose unit to another using a conversion factor so that a comparison can be made between two dose units when they are not equivalent. The dose unit used for the Dosing Order Check may not be the same dose unit First Databank (FDB) returns with the Dosing Order Check results. The initial list of Dose Unit Conversion entries is provided in Appendix D of the Dosing Order Check User Manual.

## Modified Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields have been modified:

- The Input Transform and Executable Help have been updated in the NAME field (#.01) of the MEDICATION INSTRUCTION file (#51) to enforce uniqueness among the NAME, SYNONYM and OLD MED INSTRUCTION NAMES fields, and to enhance the help text.
- The Input Transform and Executable Help have been updated in the SYNONYM field (#.5) of the MEDICATION INSTRUCTION file (#51) to enforce uniqueness among the NAME, SYNONYM and OLD MED INSTRUCTION NAMES fields, and to enhance the help text.

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields have been added:

- The DOSING CHECK FREQUENCY field (#11) has been created in the ADMINISTRATION SCHEDULE file (#51.1). This field allows a user to enter a specific format pattern to represent the frequency such as ‘X#D’, where ‘#’ represents a 1-2 character numeric value. The DOSING CHECK FREQUENCY field takes priority over all other fields/values when determining frequency for the Max Daily Dose Order Check.
- The DRUG(S) FOR DOSING CHK FREQ field (#11.1) has been created in the ADMNISTRATION SCHEDULE file (#51.1). This multiple field allows for dispense drugs from the DRUG file (#50) to be associated with the DOSING CHECK FREQUENCY field (#11) value within the ADMINISTRATION SCHEDULE file (#51.1).
- The OLD SCHEDULE NAME(S) field (#13) has been created in the ADMINISTRATION SCHEDULE file (#51.1). This multiple field stores the old values of the schedule when the NAME field (#.01) is edited. Values can also be added to this field directly.
- The DOSING CHECK FREQUENCY field (#32) has been created in the MEDICATION INSTRUCTION file (#51). This field allows a user to enter a specific format pattern to represent the frequency such as ‘X#D’, where ‘#’ represents a 1-2 character numeric value. The DOSING CHECK FREQUENCY field takes priority over all other fields/values in this file when determining frequency for the Max Daily Dose Order Check.
- The DRUG(S) FOR DOSING CHK FREQ field (#32.1) has been created in the MEDICATION INSTRUCTION file (#51). This multiple field allows for dispense drugs from the DRUG file (#50) to be associated with the DOSING CHECK FREQUENCY field (#32) value within the MEDICATION INSTRUCTION file (#51).
- The OLD MED INSTRUCTION NAME(S) field (#33) has been created in the MEDICATION INSTRUCTION file (#51). This multiple field stores the old values of the medication instruction when the NAME field (#.01) is edited. Values can also be added to this field directly.

## Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new security keys have been created.

## Modified Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PSSJ SCHEDULE EDIT Input template has been modified to allow editing of DOSING CHECK FREQUENCY field (#11), DRUG(S) FOR DOSING CHK FREQ (#11.1), and OLD SCHEDULE NAME(S) field (#13) in the ADMINISTRATION SCHEDULE file (#51.1).

# Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*201 provides the following additional functionality:

- The POST-INIT routine POST^PSS1P201 will add two new entries to the APSP INTERVENTION TYPE file (#9009032.3). They are MAX DAILY DOSE and MAX SINGLE DOSE & MAX DAILY DOSE.
- The POST-INIT routine POST^PSS1P201 will change the NAME field value of the 'SUPPOSITOR(IES)' to 'SUPPOSITORY(IES)' in the DOSE UNITS file (#51.24).
- The term ‘APPLIC’ has been added as a synonym to the entry ‘APPLICATION(S) in the DOSE UNITS file (#51.24).
- Modifications have been made to the VistA XML parsing code for the DOSING_INFO and DRUG_INFO Web Services to properly interpret all attributes returned with future versions of Mocha Server. These changes are transparent to the end user.

# Impacts to Other Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Maximum Single Dose Order Check performed in Inpatient Medications, Outpatient Pharmacy, and CPRS applications will be impacted by the free text enhancements released in patch PSS\*1\*201.

A wider array of free text dosage ranges will be interpreted, resulting in successful Maximum Single Dose Order Checks being performed. Numbers within the dosages no longer have to be sequential. There are no upper limits to the numeric values.

Many times when a dosage is ordered for a medication, clarifying information is placed in parenthesis next to the actual dose. The software will now handle free text dosages that contain parenthesis with additional information.

Combination Insulin Products have active ingredients that are assigned the same dose units as the combination product when the product is ordered. MOCHA v2.0 does not perform a Maximum Single Dose Check on a combination product for which a free text dosage was ordered if no dispense drug was assigned to the order and multiple dispense drugs were associated with the Orderable Item. The software will now allow the Maximum Single Dose Order Check to occur if the dose unit assigned to the combination product matches the drug units assigned to the active ingredients.

# Known Anomalies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Notification messages have been enhanced when entering duplicative data in the NAME field (#.01), SYNONYM field (#.5), and OLD MED INSTRUCTION NAME(S) field (#33) multiple of the MEDICATION INSTRUCTION file (#51), and when entering duplicative data in the NAME field (#.01) and OLD SCHEDULE NAME(S) field (#13) multiple of the ADMINISTRATION SCHEDULE file (#51.1). Due to a defect in FileMan patch DI\*22.2\*2 these messages may be suppressed, and will not be displayed to the user. The defect causing the issue will be fixed in FileMan patch DI\*22.2\*5.