---
title: Pharmacy Ordering Enhancements (POE) Phase 2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: plain
doc_subject: Pharmacy Ordering Enhancements (POE) Phase 2
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: - [# Introduction](#introduction) - [Outpatient Pharmacy](#outpatient-pharmacy) - [Options and Actions](#options-and-actions) - [Reports and Profiles](#reports-and-profiles) - [Files and Fields](#files-and-fields) - [Other Functionality](#other-functionality) - [Obsolete Functionality](#obsolete-fun
audience: 
keywords: 
  - order
  - pharmacy
  - orderable
  - drug
  - orders
  - patient
  - dose
  - cprs
  - table
  - contents
page_count: 0
word_count: 10745
section_count: 25
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2001
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/cprs_poe_1_0_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/cprs_poe_1_0_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

> ![](pharmacy-ordering-enhancements-poe-phase-2-release-notes/001.png)

PHARMACY ORDERING ENHANCEMENTS (POE)Phase 2

####### RELEASE NOTES 

PSO\*7\*46

OR\*3\*94

PSS\*1\*38

PSJ\*5\*50

September 2001

V*IST*A System Design & Development

Table of Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [Outpatient Pharmacy](#outpatient-pharmacy)
  - [Options and Actions](#options-and-actions)
  - [Reports and Profiles](#reports-and-profiles)
  - [Files and Fields](#files-and-fields)
  - [Other Functionality](#other-functionality)
  - [Obsolete Functionality](#obsolete-functionality)
  - [Impacts to Other Packages](#impacts-to-other-packages)
- [Pharmacy Data Management](#pharmacy-data-management)
  - [Options and Actions](#options-and-actions-1)
  - [Reports and Profiles](#reports-and-profiles-1)
  - [Files and Fields](#files-and-fields-1)
  - [Other Functionality](#other-functionality-1)
  - [Obsolete Functionality](#obsolete-functionality-1)
  - [Impacts to Other Packages](#impacts-to-other-packages-1)
- [\<This page is intentionally left blank.\>](#this-page-is-intentionally-left-blank)
- [Inpatient Medications](#inpatient-medications)
  - [Options and Actions](#options-and-actions-2)
  - [Reports and Profiles](#reports-and-profiles-2)
  - [Files and Fields](#files-and-fields-2)
  - [Other Functionality](#other-functionality-2)
  - [Obsolete Functionality](#obsolete-functionality-2)
  - [Impacts to Other Packages](#impacts-to-other-packages-2)
- [Computerized Patient Record System](#computerized-patient-record-system)
  - [Options and Actions](#options-and-actions-3)
  - [Reports and Profiles](#reports-and-profiles-3)
  - [Files and Fields](#files-and-fields-3)
  - [Other Functionality](#other-functionality-3)
  - [Obsolete Functionality](#obsolete-functionality-3)
  - [Impacts to Other Packages](#impacts-to-other-packages-3)
The Pharmacy Ordering Enhancements (POE) project is a collection of upgrades to the Inpatient Medications (IM), Outpatient Pharmacy (OP), Pharmacy Data Management (PDM), and Computerized Patient Record System (CPRS) software packages. The goal of the POE project is to optimize functionality utilized by clinicians to enter and transfer medication orders. This goal is accomplished by providing changes to the pharmacy medication ordering dialogues to eliminate the redundant entry of drug information during medication order entry and improve the process of medication order transfer between Inpatient Medications and Outpatient Pharmacy packages. Additionally, order checks will be provided for medication orders for which a dispense drug has not been selected during the CPRS order entry process. It will provide the display of documented drug formulary statuses and corresponding restriction/guidelines to the provider and pharmacist at the time of order entry in a timelier manner.
The release notes provide a brief description of the new features and functions of the POE project which is provided as a Master Build including Patches PSO\*7\*46, OR\*3\*94, PSS\*1\*38, and PSJ\*5\*50.
This Master Build can only be run with a standard M operating system. It also requires the following Department of Veterans Affairs (VA) software packages:
|                                              |                            |
|----------------------------------------------|----------------------------|
| Package                                  | Minimum Version Needed |
|                                              |                            |
| Pharmacy Data Management (PDM)               | 1.0                        |
| VA FileMan                                   | 22.0                       |
| Kernel                                       | 8.0                        |
| Patient Information Management System (PIMS) | 5.3                        |
| National Drug File (NDF)                     | 4.0                        |
| Integrated Billing                           | 2.0                        |
| Fee Basis                                    | 3.5                        |
| Adverse Reaction Tracking (ART)              | 4.0                        |
| Inpatient Medications (IM)                   | 5.0                        |
| IFCAP                                        | 5.0                        |
| Laboratory                                   | 5.2                        |
| Order Entry/Results Reporting (OERR)         | 3.0                        |
| Outpatient Pharmacy (OP)                     | 7.0                        |
| Decision Support System                      | 3.0                        |
|                                              |                            |
The above software is not included in this Master Build and must be installed before this build is completely functional.
\<This page is intentionally left blank.\>

# Outpatient Pharmacy 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new features, functions, and enhancements of the POE project for Outpatient Pharmacy are grouped and discussed below.

## Options and Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed menu options and new or changed actions including hidden actions.

#### Menu Options

There are no additions or changes to any of the menu options in the Outpatient Pharmacy package.

#### New Actions

With the POE software changes, the backdoor outpatient order entry dialog process is revised. The user is no longer able to enter or edit the SIG as a single field. The SIG is broken down into separate and distinct dosing, patient instruction, and provider comment fields. Fields that define the dosing sequence are DOSAGE ORDERED, VERB, DISPENSE UNITS PER DOSE, NOUN, ROUTE, SCHEDULE, DURATION, and CONJUNCTION. These fields are listed in Section 2.3 below.

After installation of patch PSO\*7\*46, the software will attempt to determine default values for as many of the new fields as possible, when renewing or finishing pending orders entered <u>through CPRS</u> prior to this patch. The defaults will be based on data in the original CPRS-entered order.

![](pharmacy-ordering-enhancements-poe-phase-2-release-notes/002.png)Note: This functionality will not be seen for orders originally entered through the Outpatient Pharmacy package via the Patient Prescription Processing option.

If defaults cannot be determined, the user will be prompted to fill in any blanks after the order is accepted. The order will not be assigned an active status until all required missing information is entered. Editing the SIG or order in such a way as to create a new order will also require that all dosing fields be filled in. An asterisk ‘\*’ is displayed next to the fields that create a new order when edited.

A new List Manager hidden action, DIN, is added to display available drug restriction/guideline information for the Dispense Drug and Orderable Item associated with the selected medication order.

#### Changed Actions

The synonym for the Print List (PL) action is changed to PT.

## Reports and Profiles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed reports and/or profiles.

#### Reports

There are no additions or changes to any of the reports in the Outpatient Pharmacy package.

#### New Profiles

There are no additions to any of the profiles in the Outpatient Pharmacy package.

#### Changed Profiles

All Order Views display a drug text indicator, \<DIN\>, if active drug text entries exist for either the Orderable Item or Dispense Drug associated with the selected outpatient medication order. If either the Orderable Item or Dispense Drug is locally non-formulary, this status is also displayed to the user.

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed files and fields.

#### New Files

There are no new files added to the Outpatient Pharmacy package.

#### Changed Files

The addition of new fields and modification of existing fields in the PRESCRIPTION file and the Pending Outpatient Orders file is described in detail below under the New Fields and Changed Fields sub-headings.

#### New Fields

############################### PRESCRIPTION file (#52)

The PATIENT INSTRUCTIONS field can display information associated with the Orderable Item that is entered through PDM or it can contain free text entered by the user for an individual order. The Patient Instructions entry is automatically added to the end of the SIG in backdoor pharmacy. When Provider Comments are copied from a CPRS order, the Provider Comments will be appended to the end of the SIG following the Patient Instructions.

Several of the new fields within the PRESCRIPTION file are not displayed to the user but are used by the software. The POE RX field, that is set whenever a new/renew prescription is entered after the POE software has been installed, is one of these hidden fields. Another new hidden field, the OTHER COMMENTS multiple of the ACTIVITY sub-file, is used to store original front door medication instructions for Pre-POE prescriptions. The EXPANDED PATIENT INSTRUCTIONS multiple of the PRESCRIPTION file will store the expanded patient instructions that are stored in the PATIENT INSTRUCTION field or the expanded patient instructions that were entered from CPRS. The ORIGINAL QTY field, used to hold the quantity for the original fill of the prescription, is created for use in a future enhancement.

The MEDICATION INSTRUCTIONS sub-file is added to the PRESCRIPTION file and contains the values for DISPENSE UNITS PER DOSAGE ORDERED, DOSAGE ORDERED, UNITS, NOUN, VERB, SCHEDULE, DURATION, and CONJUNCTION for an order. These fields are used to build the SIG.

The DOSAGE ORDERED field is a single dose of medication the patient receives for this prescription order. The user is displayed a default selection list of Possible Dosages or Local Possible Dosages based on the Dispense Drug from which to choose or the user can elect to enter a free text dosage.

The DISPENSE UNITS PER DOSE field is the number of units of the Dispense Drug the patient receives for a single dose of the medication. Default DISPENSE UNITS PER DOSE values are derived from the Possible Dosages associated with the Dispense Drug. The user has the option to enter a different value.

The UNITS field is the unit of measure associated with the DOSAGE ORDERED. The displayed default value is supplied from the DRUG UNITS file.

The NOUN field contains the nouns associated with the DOSAGE FORM. It is used to build a SIG for pending orders entered through CPRS.

The DURATION field (In Days, Hours, Minutes, Weeks, and Months) is used only when a medication should be taken for a limited period of time. Days are assumed for numeric entries. The user should follow the number with an “H” to specify hours, an “M” to specify minutes, a “W” to specify weeks, or an “L” to specify months.

![](pharmacy-ordering-enhancements-poe-phase-2-release-notes/003.png)Note: Do not use the DURATION field for DAYS SUPPLY.

The CONJUNCTION field is used to join dosing sequences for a complex order. The entries are limited to “AND,” “THEN,” or “EXCEPT.” “AND” is used for concurrent doses in a complex order, such as “Take 1 tablet every morning AND take 2 tablets at bedtime.” “THEN” is used for consecutive doses in a complex order, for example “Take 2 tablets daily for one week THEN take 1 tablet daily for five days.” “EXCEPT” can be used in a complex order to describe any dosing order that is not routine, as in “Take 1 tablet every day EXCEPT take no tablets Wednesday.”

The ROUTE field describes the route by which a medication is to be taken, applied, or used. The default value displayed is supplied from the pharmacy Orderable Item file. If no default value is entered, the default display will be “PO.”

The SCHEDULE field describes how often a medication is to be taken. The default SCHEDULE displayed is supplied from the pharmacy Orderable Item file entry for the selected Orderable Item. The user can accept the displayed default or enter free text. If a free text entry is typed in, the software looks at the entire SCHEDULE field and tries to find a match in the ADMINISTRATION SCHEDULE file that has an Outpatient Expansion. If nothing is found there, then it looks in the MEDICATION INSTRUCTION file for an expansion. If nothing is there, and there are spaces in the SCHEDULE field, it performs the same process on each word.

![](pharmacy-ordering-enhancements-poe-phase-2-release-notes/004.png)Note: Entries to the SCHEDULE field cannot have more than two spaces or be more than 20 characters long (including spaces).

The VERB field describes how the medication is taken or used. Default values come from the DOSAGE FORM file entry for the selected Orderable Item. The VERB field is used by both the Outpatient Pharmacy package and CPRS. CPRS uses it as the first word when building the order text of an Outpatient order entered through CPRS. Outpatient Pharmacy uses the VERB field as the first word when building the SIG for orders entered through CPRS and through the Outpatient Pharmacy package.

###############################  PENDING OUTPATIENT ORDERS file (#52.41)

The PATIENT INSTRUCTIONS field contains information associated with the Orderable Item selected or free text instructions entered for the individual order. Each word entered in this field will be checked against entries in the Medication Instruction file to see if an expansion exists. The expansion will replace the word in the PATIENT INSTRUCTIONS field.

The DAYS SUPPLY field displays a default value based on Rx patient status. This field is used to calculate the default value displayed in the QTY field. If the DAYS SUPPLY field is edited, the QTY field is recalculated. If the QTY field is edited, the DAYS SUPPLY field value does not change but a message is displayed warning the user of the change and recommending that the value be checked.

The provider will use the PATIENT INSTRUCTIONS FLAG field to indicate if the PATIENT INSTRUCTIONS associated with the Orderable Item should be included in the SIG.

Several of the fields within the Pending Outpatient Orders file are not displayed to the user but are used by the software. The EXPANDED PATIENT INSTRUCTIONS multiple stores the expanded patient instructions that are stored in the PATIENT INSTRUCTION field or the expanded patient instructions that were entered from CPRS. The PRE_POE ORDER field, used to identify pending orders entered before installation of the POE patch, is one of these hidden fields. The FLAG field, used to identify orders flagged for follow-up with a provider, is added to support a future enhancement.

The following fields have been added to store data from pending orders entered through CPRS and may be used to build the SIG. These fields are located in the QUANTITY TIMING sub-file of the Pending Outpatient Orders file.

The DOSAGE ORDERED field contains a single dose of medication the patient receives for this prescription order.

The DISPENSE UNITS PER DOSE field is the number of units of the Dispense Drug the patient receives for a single dose of the medication.

The MED ROUTE field describes the route by which a medication is to be taken, applied, or used.

The UNITS field is the unit of measure associated with the DOSAGE ORDERED. The displayed default value is supplied from the DRUG UNITS file.

The NOUN field contains the noun associated with the dosing sequence for a pending order.

The VERB field describes the manner in which the medication is taken or used.

#### Changed fields

############################### PRESCRIPTION file (#52)

The SCHEDULE field in the MEDICATION INSTRUCTIONS sub-file is modified to allow a maximum of twenty characters, only two of which can be spaces.

The maximum value for entries is increased to 9999 in the UNIT PRICE OF DRUG field, CURRENT UNIT PRICE OF DRUG field of the PRESCRIPTION REFILL sub-file, and the CURRENT UNIT PRICE OF DRUG field of the PRESCRIPTION PARTIAL DATE sub-file.

############################### 

############################### PENDING OUTPATIENT ORDERS file (#52.41)

The SCHEDULE field in the QUANTITY TIMING sub-file is modified to allow a maximum of twenty characters, only two of which can be spaces.

## Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains any new or changed functionality to the Outpatient Pharmacy package that cannot be placed in the above categories.

![](pharmacy-ordering-enhancements-poe-phase-2-release-notes/005.png)Note: A Drug Enforcement Agency (DEA) number or VA number is required for a name to be entered as the provider on a controlled substance medication order. This is not a new or changed functionality for the OP package; however, it is a new functionality for the CPRS package. Please review the CPRS section of this document for an explanation of the related changes.

The New Order Entry action provides the display of the drug formulary status, when the drug is locally non-formulary. It also displays corresponding drug restriction/guideline information to the pharmacists when entering new orders for a patient.

When finishing orders entered through CPRS, PROVIDER COMMENTS may be added to the SIG by copying them first to the Patient Instructions field. The content of the entire PATIENT INSTRUCTIONS field is then appended to the end of the SIG.

Entries to the Days Supply field produce a calculated default value for the QTY field if the Schedule field has a frequency and a numeric Possible Dosage is selected as the Dosage Ordered. If the order is a complex order, all DURATIONs must be available or assumable by the software in order to provide a QTY default to the user.

The software attempts to find a common Dispense Drug that can be used to calculate dosages for all the dosing sequences in a complex order entered through CPRS. When the same Dispense Drug cannot accommodate all the dosages for the order, then no Dispense Drug is assigned to the order and the dosages appear in the SIG as entered. The user will have to create separate orders for each Dispense Drug required or otherwise edit the order.

Users are provided with the ability to change the DAYS SUPPLY, \# of REFILLS and QTY when renewing prescriptions.

The View Prescription option is modified to incorporate the new order dialog fields.

The RENEWING RX’S ALLOWED field under the *Site parameters Enter/Edit* option is restored. Setting this parameter to NO will disable individual and speed prescription renewals through backdoor pharmacy only.

## Obsolete Functionality 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains any functionality that has been deleted in this Outpatient Pharmacy portion of the Master Build.

The SIG field can no longer be entered as a single field or edited directly.

## Impacts to Other Packages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section shows any impacts the Outpatient Pharmacy portion of the Master Build release has to other software packages.

#### Inpatient Medications

The Pharmacy Ordering Enhancements project improves the transfer of Outpatient Pharmacy orders to Inpatient Medications within CPRS and vice versa. It improves future order checking by utilizing dosages associated with a Dispense Drug in CPRS. It also provides order checks for orders that do not contain a designated Dispense Drug by checking against all Dispense Drugs tied to the Orderable Item in the order.

\<This page is intentionally left blank.\>

# Pharmacy Data Management 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new features, functions, and enhancements of the POE project for Pharmacy Data Management are grouped and discussed below.

## Options and Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed menu options and new or changed actions including hidden actions.

#### New Options

The *Medication Route File Enter/Edit* option provides the ability to edit data in the MEDICATION ROUTES file.

The *Dosage Form File Enter/Edit* option provides the ability to edit data in the DOSAGE FORM file.

#### Changed Options

The *Drug Enter/Edit* option includes the ability to enter or edit Possible Dosage and Local Possible Dosage information for drug entries. Some other new fields are added to the option for editing purposes.

The *Lookup into Dispense Drug File* option is enhanced to display Dosage information for the selected drug.

The *Standard Schedule Edit* option allows the Schedules to be entered or edited with two (2) spaces, instead of the one (1) space that the option previously allowed.

The *Auto Create Dosages* option is modified to only allow the merging of new Dosages if the option is rerun. Previously, the choice was given to either merge Dosages or delete all Dosages and create new Dosages.

Since IV Pharmacy Orderable Items are all inactivated with Phase 2 of POE, all IV Additives and IV Solutions are re-matched to non-IV flagged Pharmacy Orderable Items. The *Edit Orderable Items* option now reflects those new matches.

The *Noun/Dosage Form Report* displays the DOSAGE FORMS, along with their associated NOUNS and PACKAGE USE fields. It also displays the Local Possible Dosage based on the Nouns and Instructions. This option was originally named the *Dosage Form/Noun Report* in the Pharmacy Ordering Enhancements Pharmacy Data Management Pre-Release (Phase 1) of the POE project.

The *Medication Instruction File Add/Edit* option is modified to allow editing of the FREQUENCY field.

The *Edit Orderable Item* and *Dispense Drug/Orderable Item Maintenance* options are enhanced to display all IV Additives and IV Solutions associated with the Pharmacy Orderable Item and to allow editing of the PATIENT INSTRUCTION field.

#### Actions

There are no additions or changes to any of the actions in the Pharmacy Data Management package.

## Reports and Profiles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed reports and/or profiles.

#### New Reports

There are no new reports added to the Pharmacy Data Management package.

#### #### #### Changed Reports

The *Orderable Item Report* option is enhanced to consolidate three separate reports, one for IV Additives, IV Solutions, and Dispensed Drugs into one single report.

#### Profiles

There are no additions or changes to any of the profiles in the Pharmacy Data Management package.

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed files and fields.

#### New Files

There are no additions to any of the files in the Pharmacy Data Management package.

#### Changed Files

The DRUG file is modified to include a BCMA UNITS PER DOSE field.

The field descriptions of the VERB and PREPOSITION fields of the DOSAGE FORM file are enhanced to make them more descriptive and helpful.

Within the PHARMACY ORDERABLE ITEM file, the cross-references are re-worked to provide a method to maintain Pharmacy Orderable Item links and their existing relationships.

The SCHEDULE field in the MEDICATION INSTRUCTION file is no longer in use by the Pharmacy software after installing Phase 2 of the Pharmacy Ordering Enhancements software.

The ADMINISTRATION SCHEDULE file is modified to allow a Schedule to be entered that contains two (2) spaces, where previously only one (1) space was allowed.

Within the IV ADDITIVES file, the cross-references are re-worked to provide a method to maintain Pharmacy Orderable Item links and their existing relationships. Additionally, the file is modified to automatically update the Pharmacy Orderable Item of the Additive based on its Dispense Drug match.

Within the IV SOLUTIONS file, the cross-references are re-worked to provide a method to maintain Pharmacy Orderable Item links and their existing relationships. Additionally, the file is modified to automatically update the Pharmacy Orderable Item of the Solution based on its Dispense Drug match.

The PHARMACY PATIENT file is modified to include the DOSE and UNIT fields. The data available from POE changes are stored in these new fields for future dosage checks. The LAST RENEW sub-nodes are added to both IV and Unit Dose sub-files for a future-renewing enhancement. A NATURE OF ORDER field is added to both IV and Unit Dose sub-files.

The PHARMACY SYSTEM file is modified to include the CALC UNITS NEEDED PRN ORDERS field. The sites can set this field to allow for the calculation of Units Needed on the Inpatient Medications V. 5.0 Pick List for orders with PRN in the schedule.

#### New Fields

DRUG file (#50)

A new field, BCMA UNITS PER DOSE, is added to the POSSIBLE DOSAGES sub-file of the DRUG file. This field represents the BCMA UNITS PER DOSE, which is associated with the DOSAGE for Inpatient Medication orders. This field is used to populate the UNITS PER DOSE field within the DISPENSE DRUG multiple of the UNIT DOSE sub-file of the PHARMACY PATIENT file. The UNITS PER DOSE field designates the number of times a Dispense Drug unit must be scanned to document delivery of a needed dosage through the Bar Code Medication Administration (BCMA) package.

A new field is added to the LOCAL POSSIBLE DOSAGES sub-file of the DRUG file. The field is BCMA UNITS PER DOSE. This field represents the BCMA UNITS PER DOSE, which is associated with the DOSAGE for Inpatient Medication orders. This field is used to populate the UNITS PER DOSE field within the DISPENSE DRUG multiple of the UNIT DOSE sub-file of the PHARMACY PATIENT file. The UNITS PER DOSE field designates the number of times a Dispense Drug unit must be scanned to document delivery of a needed dosage through the BCMA package.

PHARMACY PATIENT file (#55)

A NATURE OF ORDER field of the IV sub-file of the PHARMACY PATIENT file is added. This field represents the method that the provider used to communicate the order to the person taking any action on the order.

A DOSE field of the UNIT DOSE sub-file of the PHARMACY PATIENT file is added. This field represents the numeric DOSAGE for the order. It is combined with the UNIT field of the UNIT DOSE sub-file to show the DOSAGE ORDERED.

A UNIT field of the UNIT DOSE sub-file of the PHARMACY PATIENT file is added and represents the unit for the numeric DOSAGE.

A NATURE OF ORDER field of the UNIT DOSE sub-file of the PHARMACY PATIENT file is added. This field represents the method that the provider used to communicate the order to the person taking any action on the order.

A LAST RENEW field of the LAST RENEW sub-file of the IV sub-file of the PHARMACY PATIENT file is added. This field represents the date/time that the order was renewed.

A RENEWED BY field of the LAST RENEW sub-file of the IV sub-file of the PHARMACY PATIENT file is added and represents the person who renewed the order.

A PREVIOUS PROVIDER field of the LAST RENEW sub-file of the IV sub-file of the PHARMACY PATIENT file is added. This field represents the provider responsible for the prior order.

A PREVIOUS STOP DATE/TIME field of the LAST RENEW sub-file of the IV sub-file of the PHARMACY PATIENT file is added. This field represents the stop date/time the prior order.

A LAST RENEW field of the LAST RENEW sub-file of the UNIT DOSE sub-file of the PHARMACY PATIENT file is added. This field represents the date/time that the order was renewed.

A RENEWED BY field of the LAST RENEW sub-file of the UNIT DOSE sub-file of the PHARMACY PATIENT file is added. This field represents the person who renewed the order.

A PREVIOUS PROVIDER field of the LAST RENEW sub-file of the UNIT DOSE sub-file of the PHARMACY PATIENT file is added. This field represents the provider responsible for the prior order.

A PREVIOUS STOP DATE/TIME field of the LAST RENEW sub-file of the UNIT DOSE sub-file of the PHARMACY PATIENT file is added and represents the stop date/time of the prior order.

PHARMACY SYSTEM File (#59.7)

A CALC UNITS NEEDED PRN ORDERS field of the PHARMACY SYSTEM file is added. This field controls whether or not UNITS NEEDED will be calculated for Inpatient orders with PRN in the SCHEDULE field. This information will show on the Pick List if this field is set to 1.

#### Changed Fields

DRUG File (#50)

The “AK” cross-reference is added to the GENERIC NAME field of the DRUG file. This cross-reference is only a placeholder. It describes cross-references set from fields in other files into the ^PSDRUG global of the DRUG file.

The “AC” cross-reference of the VA CLASSIFICATION field of the DRUG file is changed. This change prevents an error from occurring on occasion.

The “AE” cross-reference is added to the PHARMACY ORDERABLE ITEM field of the DRUG file. This cross-reference is used to update the Pharmacy Orderable Item pointers in the IV ADDITIVES file and the IV SOLUTIONS file for IV Additives and IV Solutions that are matched to this Drug. This cross- reference is also used to keep the Pharmacy Orderable Item up to date with current information, based on all active Drugs, IV Additives, and IV Solutions that are matched to the Pharmacy Orderable Item. This information is also sent to CPRS to update the corresponding Orderable Item entry in the ORDERABLE ITEMS file.

The “AF” cross-reference is added to the DEA, SPECIAL HDLG field of the DRUG file. This cross-reference is used to keep the Pharmacy Orderable Item up to date with current information, based on all active Drugs, IV Additives, and IV Solutions that are matched to the Pharmacy Orderable Item. This information is also sent to CPRS to update the corresponding Orderable Item entry in the ORDERABLE ITEMS file.

The “AJ” cross-reference has been added to the LOCAL NON-FORMULARY field of the DRUG file. This cross-reference is used to keep the Pharmacy Orderable Item up to date with current information, based on all active Drugs, IV Additives, and IV Solutions that are matched to the Pharmacy Orderable Item. This information is also sent to CPRS to update the corresponding Orderable Item entry in the ORDERABLE ITEMS file.

The “AD” cross-reference is added to the INACTIVE DATE field of the DRUG file. This cross-reference is used to keep the Pharmacy Orderable Item up to date with current information, based on all active Drugs, IV Additives, and IV Solutions that are matched to the Pharmacy Orderable Item. This information is also sent to CPRS to update the corresponding Orderable Item entry in the ORDERABLE ITEMS file.

The field description of the DISPENSE UNITS PER DOSE field of the POSSIBLE DOSAGES SUB-FIELD sub-file of the DRUG file is enhanced to make it more descriptive and helpful.

DOSAGE FORM File (#50.606)

The field description of the VERB field of the DOSAGE FORM file is enhanced to make it more descriptive and helpful.

The field description of the PREPOSITION field of the DOSAGE FORM file is enhanced to make it more descriptive and helpful.

PHARMACY ORDERABLE ITEM File (#50.7)

The “A50” cross-reference is added to the NAME field of the PHARMACY ORDERABLE ITEM file. This cross-reference is only a placeholder. It describes cross-references set from fields in other files into the ^PS(50.7 global of the PHARMACY ORDERABLE ITEM file.

The “AC” cross-reference is added to the INACTIVE DATE field of the PHARMACY ORDERABLE ITEM file. This cross-reference is used to keep the Pharmacy Orderable Item up to date with current information, based on all active Drugs, IV Additives, and IV Solutions that are matched to the Pharmacy Orderable Item. This information is also sent to CPRS to update the corresponding Orderable Item entry in the ORDERABLE ITEMS file.

The Input Transform of the SCHEDULE field of the PHARMACY ORDERABLE ITEM file is changed to echo back separate Inpatient and Outpatient information when a schedule is entered or edited.

The FORMULARY STATUS field of the PHARMACY ORDERABLE ITEM file is not editable through FileMan. The formulary status is controlled automatically, based on the formulary status of the drugs that are matched to the Orderable Item.

The field description of the OI-DRUG TEXT ENTRY multiple of the PHARMACY ORDERABLE ITEM file is enhanced to make it more descriptive and helpful.

############################### MEDICATION INSTRUCTION File (#51)

A change is made to the SCHEDULE field of the MEDICATION INSTRUCTION file. Prior to the Pharmacy Ordering Enhancements project, this field was used to associate schedules with Outpatient prescriptions, by running each word of the SIG through the MEDICATION INSTRUCTION file to look for an associated SCHEDULE. The field is currently not being used by the Pharmacy software.

ADMINISTRATION SCHEDULE File (#51.1)

A change is made to the NAME field of the ADMINISTRATION SCHEDULE file. This change allows a SCHEDULE to be entered that contains two (2) spaces, where previously only one (1) space was allowed.

IV ADDITIVES File (#52.6)

The “AD” cross-reference is added to the GENERIC DRUG field of the IV ADDITIVES file. This cross-reference is used to update the PHARMACY ORDERABLE ITEM field of the IV ADDITIVES file. This cross-reference is also used to keep the Pharmacy Orderable Item up to date with current information, based on all active Drugs, IV Additives, and IV Solutions that are matched to the Pharmacy Orderable Item. This information is sent to CPRS to update the corresponding Orderable Item entry in the ORDERABLE ITEMS file.

The “AE” cross-reference is added to the INACTIVATION DATE field of the IV ADDITIVES file. This cross-reference is used to keep the Pharmacy Orderable Item up to date with current information, based on all active Drugs, IV Additives, and IV Solutions that are matched to the Pharmacy Orderable Item. This information is also sent to CPRS to update the corresponding Orderable Item entry in the ORDERABLE ITEMS file.

The “AD” cross-reference of the PHARMACY ORDERABLE ITEM field of the IV ADDITIVES file is removed. The field is not editable through FileMan. These changes are made because the software automatically updates this field based on the Pharmacy Orderable Item that is matched to the Dispense Drug to which the IV Additive is matched

The “AF” cross-reference is added to the USED IN IV FLUID ORDER ENTRY field of the IV ADDITIVES file. This cross-reference is used to keep the Pharmacy Orderable Item up to date with current information, based on all active Drugs, IV Additives, and IV Solutions that are matched to the Pharmacy Orderable Item. This information is also sent to CPRS to update the corresponding Orderable Item entry in the ORDERABLE ITEMS file.

IV SOLUTIONS File (#52.7)

The “AD” cross-reference is added to the GENERIC DRUG field of the IV SOLUTIONS file. This cross-reference is used to update the PHARMACY ORDERABLE ITEM field of the IV SOLUTIONS file. This cross-reference is also used to keep the Pharmacy Orderable Item up to date with current information, based on all active Drugs, IV Additives, and IV Solutions that are matched to the Pharmacy Orderable Item. This information is sent to CPRS to update the corresponding Orderable Item entry in the ORDERABLE ITEMS file.

The “AE” cross-reference is added to the INACTIVATION DATE field of the IV SOLUTIONS file. This cross-reference is used to keep the Pharmacy Orderable Item up to date with current information, based on all active Drugs, IV Additives, and IV Solutions that are matched to the Pharmacy Orderable Item. This information is also sent to CPRS to update the corresponding Orderable Item entry in the ORDERABLE ITEMS file.

The “AD” cross-reference of the PHARMACY ORDERABLE ITEM field of the IV SOLUTIONS file is removed. The field is not editable through FileMan. These changes are made because the software will now automatically update this field based on the Pharmacy Orderable Item that is matched to the Dispense Drug to which the IV Solution is matched.

The “AF” cross-reference is added to the USED IN IV FLUID ORDER ENTRY field of the IV SOLUTIONS file. This cross-reference is used to keep the Pharmacy Orderable Item up to date with current information, based on all active Drugs, IV Additives, and IV Solutions that are matched to the Pharmacy Orderable Item. This information is also sent to CPRS to update the corresponding Orderable Item entry in the ORDERABLE ITEMS file.

  
PHARMACY PATIENT File (#55)

The SCHEDULE field of the IV sub-file of the PHARMACY PATIENT file is changed to allow two (2) spaces in the schedule, where previously only one (1) space was allowed.

The DOSAGE ORDERED field of the IV sub-file of the PHARMACY PATIENT file is changed to allow up to 60 characters.

The SCHEDULE field of the UNIT DOSE sub-file of the PHARMACY PATIENT file is changed to allow two (2) spaces in the schedule, where previously only one (1) space was allowed.

The DOSAGE ORDERED field of the UNIT DOSE sub-file of the PHARMACY PATIENT file is changed to allow up to 60 characters.

## Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains any new or changed functionality to the Pharmacy Data Management package that cannot be placed in the above categories.

A change is made to the relationship between Pharmacy Orderable Items, IV Additives, and IV Solutions. Prior to Phase 2 of the POE project, IV Additives and IV Solutions were matched to Pharmacy Orderable Items that were flagged for IV use. All Dispense Drugs were matched to Pharmacy Orderable Items that were not flagged for IV use. Upon installation of Phase 2 of the POE project, all IV flagged Pharmacy Orderable Items are inactivated. All IV Additives and IV Solutions are re-matched to Pharmacy Orderable Items not flagged for IV use. This new match is made based on the Pharmacy Orderable Item match of the Dispense Drug to which the IV Additive or IV Solution is matched.

For example, if there is an IV Additive named Ampicillin, that IV Additive also has a Generic Drug (Dispense Drug) link and this Dispense Drug is matched to a non-IV flagged Orderable Item. Upon installation of Phase 2 of POE, the software finds the Pharmacy Orderable Item to which the Dispense Drug is matched and automatically matches that IV Additive to that same Pharmacy Orderable Item. The software maintains those Pharmacy Orderable Links automatically. If, at a later time, that Dispense Drug is re-matched to a new Pharmacy Orderable Item, then the Ampicillin IV Additive that is matched to that drug will automatically be matched to that same, new Pharmacy Orderable Item.

## Obsolete Functionality 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains any functionality that is deleted in this Pharmacy Data Management portion of the Master Build.

The IV IDENTIFIER and CHANGE TYPE ORDER FROM OERR field prompts are removed from the *Pharmacy System Parameters Edit* option.

The CORRESPONDING IV ITEM, CORRESPONDING UD ITEM, and FORMULARY STATUS fields are removed from both *Edit Orderable Item* and *Dispense Drug/Orderable ItemMaintenance* options.

Many of the options necessary for the Pharmacy Ordering Enhancements Pharmacy Data Management Pre-Release (Phase 1) of the POE project are now obsolete. All options that are eliminated with Phase 2 of the POE project are listed below.

*Ordering Enhancements Pre-Release*

> This option contained the sub-options necessary for set up of the POE PDM Pre-Release patch.

*Auto Rematch IV Additives/Solutions Report*

> This option provided a report, which showed how the Additive and Solutions were re-matched to new Orderable Items based on their Dispense Drug link.

*Corresponding Drug*

> This option provided the sub-options for review of the Corresponding Inpatient Drug and Corresponding Outpatient Drug functionality.

*Enter/Edit Corresponding Drug *

> This option provided the ability to mark Corresponding Inpatient Drugs and Corresponding Outpatient Drugs.

*Mark Corresponding Drugs*

> This option provided the ability to mark all Corresponding Inpatient Drugs and Corresponding Outpatient Drugs based on the potential matches that were displayed in the *Report of Corresponding Drugs*.

*  
Report of Corresponding Drugs*

> This option provided a report that showed which drugs were currently marked as Corresponding Inpatient Drugs and Corresponding Outpatient Drugs in the DRUG file. It also showed potential matches that could be achieved by using the *Mark Corresponding Drugs* option.

*Dosages*

> This option provided the sub-options used to create, view, enter, and edit dosages.

*Conversion Tracker*

> This option provided the ability to track when the last dosage conversion was run.

*Dosages Enter/Edit*

> This option allowed the POSSIBLE DOSAGES fields and LOCAL POSSIBLE DOSAGE fields for a selected Dispense Drug to be edited. This option was renamed *Enter/Edit Dosages* and included in Phase 2 of the POE project.

*Instructions/Nouns*

> This option provided the sub-options to populate and control the NOUN fields in the DOSAGE FORM file.

> *Convert Instructions to Nouns   
> *

> This option allowed the conversion of all non-numeric instructions to NOUNS in the DOSAGE FORM file.

> *Dosage Form/Noun Report*  

> This option provided a report that displayed the DOSAGE FORMS, along with their associated NOUN and PACKAGE fields. It also displayed the Local Possible Dosage based on the NOUN. This option was renamed *Noun/Dosage Form Report* and included in Phase 2 of the POE project.

> *Instructions to Noun Conversion Report  
> *

> This option provided a report that displayed the instructions associated with each dosage form. The non-numeric instructions could be converted to the NOUN field by using the *Convert Instructions to Nouns* option.

> *  
> Nouns Enter/Edit*  

> This option allowed the entering and editing of Nouns and their associated NOUN fields in the DOSAGE FORM file.

> *Med Instruction/Frequency*  

> This option provided the sub-options for editing and displaying the data in the MEDICATION INSTRUCTION file.

> *Edit Medication Instruction Frequency  
> *

> This option provided the ability to edit data in the FREQUENCY (IN MINUTES) field in the MEDICATION INSTRUCTION file. This data was used for calculating default QUANTITY and DAYS SUPPLY values for Outpatient Pharmacy orders.

> *Medication Instruction Frequency Report  
> *

> This report displayed information from the MEDICATION INSTRUCTION file. It could be used to help determine which instructions can have a valid frequency.

*Medication Routes/IV Flag  
*

> This option provided sub-options that involved the new IV Flag indicator in the MEDICATION ROUTES file.

Edit Medication Route IV Flag

> This option allowed the editing of the IV Flag in the MEDICATION ROUTES file.

> *Flag Medication Routes as IV  
> *

> This option was used to automatically populate the IV FLAG field in the MEDICATION ROUTES file for all routes that were associated with an IV Flagged Orderable Item or contained in Quick Codes in the IV ADDITIVES file.

> *Medication Routes flagged for IV Report*

> This option provided a report that showed the Medication Routes, their abbreviations, the package use, and the IV Flag status of the Medication Route. The IV Flag helped determine how Inpatient Medication Orders entered through CPRS were finished in the Inpatient Medications package.

> *  
> Patient Instructions Enter/Edit*

> This option provided the ability to edit the PATIENT INSTRUCTIONS field in the PHARMACY ORDERABLE ITEM file.

## Impacts to Other Packages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section shows any impacts the Pharmacy Data Management portion of the Master Build release has to other software packages.

#### BCMA

The DRUG file is modified to include a BCMA UNITS PER DOSE field.

#### CPRS

The CPRS screens and options are updated to reflect the changes in medication order entry resulting from the enhancements to the PDM package.

If Pharmacy wishes for the drug message not to display to the CPRS users, then the CPRS parameter can be set appropriately.

# \<This page is intentionally left blank.\>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Inpatient Medications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new features, functions, and enhancements of the POE project for Inpatient Medications are grouped and discussed below.

## Options and Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed menu options and new or changed actions including hidden actions.

#### Menu Options

There are no additions or changes to any of the menu options in the Inpatient Medications package.

#### New Actions

A new List Manager hidden action, DIN, is added to display drug restriction/guideline information for the Dispense Drug and/or Orderable Item associated with the selected order.

#### Changed Actions

The synonym for the Print List (PL) action is changed to PT.

## Reports and Profiles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed reports and/or profiles.

#### New Reports

There are no new reports added to the Inpatient Medications package.

#### Changed Reports

The Activity Log is modified to store the Requested Start and Stop Date/Time values when a Unit Dose and/or IV Pending order is finished and the status is active. It also logs the date/time and user that finishes a Unit Dose order if auto verification is <u>not</u> turned on.

#### Profiles

There are no additions or changes to any of the profiles in the Inpatient Medications package.

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed files and fields.

#### New Files

There are no new files added to the Inpatient Medications package.

#### Changed Files

The ACTIVITY LOG REASON file is changed by the addition of three new entries. These entries include Verified, Finished by Pharmacist, and Finished by Nurse. The verified entry contains the date and time the order is verified. The finished entries log the date/time and user that finishes the order if auto verification is not turned on.

#### New Fields

All of the new fields added in this project are added to the NON-VERIFIED ORDERS file.

The REQUESTED START DATE/TIME and REQUESTED STOP DATE/TIME fields are added and contain the date and time the provider is requesting that the order starts and stops. These dates and times display on the Pending Order Views. A DURATION field is added to indicate the length of time in days the provider requests that an order last and is used to calculate the REQUESTED STOP DATE/TIME.

A UD/IV PROMPT field is added for use during the finishing process to prompt the user whether to finish the order as an IV or Unit Dose order. This prompt occurs only during certain circumstances. These circumstances depend upon the setting of the IV FLAG field in the MEDICATION ROUTES file in conjunction with the setting of the APPLICATION PACKAGES’ USE field in the DRUG file. These two settings determine whether the user is prompted to finish as an IV or Unit Dose order and/or is presented with the Unit Dose Order View or the IV Order View.

A DOSE field and UNIT field are added. The DOSE field is the numeric dosage for the order. It is combined with the UNIT field to show the DOSAGE ORDERED. The UNIT field contains the unit of measurement for the numeric dosage. For example, a dosage of 325 MG, the DOSE field contains 325 and the UNIT field contains MG.

Two new multiple fields are added. The first multiple field named LAST RENEW contains many sub-fields that relate to the renewal of an order. These sub-fields are LAST RENEW, RENEWED BY, PREVIOUS PROVIDER, and PREVIOUS STOP DATE/TIME. This multiple field is added to support a future enhancement.

The second multiple field is ACTIVITY LOG. This multiple field is a record of the actions that have taken place on the order. Some of the actions include edit, renewal, cancellation, and/or finish. Along with the action name, the date and time the action took place, and the user who took the action are recorded. When the action is an edit, the data in the field edited prior to the edit are also stored. These sub-fields are DATE, USER, ACTION, FIELD, and OLD DATA.

#### Changed Fields

Three fields in the NON-VERIFIED ORDERS file are modified.

The SCHEDULE field is modified to allow the user to enter up to two (2) spaces in this field. This field is the frequency (ONLY) with which the doses are to be administered. For example, TID PC PRN can be used in the SCHEDULE field.

The NATURE OF ORDER field is the method the provider used to communicate the order to the user taking any action on the order. The new codes are Electronically Entered, Policy, Service Correction, and Duplicate. These codes are in addition to Written, Telephoned, and Verbal. The Provider Entered code is removed.

The DOSAGE ORDERED field is changed to allow up to 60 characters.

## Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains any new or changed functionality to the Inpatient Medications package that cannot be placed in the above categories.

The Order View displays a drug text indicator if active drug text entries exist for either the Orderable Item or Dispense Drug associated with the selected Unit Dose order. When the IV order has Additives and Solutions associated with a Dispense Drug that contains drug text information, the \<DIN\> indicator is displayed.

The New Order Entry action provides for the display of the drug formulary status, when the drug is locally non-formulary. It also displays corresponding drug restriction/guideline information to pharmacists when entering new orders for a patient.

The Pending Order Views (Unit Dose and IV) are modified. The Requested Start Date/Time displays on the line below the start date/time of the order. The Requested Stop Date/Time displays on the line below the stop date/time of the order. This Requested Stop Date/Time flashes on the screen if it differs from the default stop date/time calculated from the pharmacy parameters. The flashing is used to alert the pharmacist finishing the order.

The Order Processing Logic now includes the use of the IV FLAG field in the MEDICATON ROUTES file in conjunction with the setting of the APPLICATION PACKAGES’ USE field in the DRUG file to determine how an order shall be processed through the *Inpatient Order Entry* or *Non-Verified/Pending Orders* options. This determination establishes whether the user is prompted to finish the order as an IV or Unit Dose order and/or is displayed as the Unit Dose Order View or the IV Order View.

The IV Order Entry Finishing Process includes presenting the user with a list of selectable Additives/Solutions to choose from, for the order, when more than one IV Additive/Solution is tied to the same Orderable Item.

The functionality of the “DOSAGE ORDERED:” prompt and the “UNITS PER DOSE:” prompt is changed in the *Inpatient Order Entry* option and the *Order Entry* option. At the “DOSAGE ORDERED:” prompt, the default/selection list displayed is based on the Possible Dosages and the Local Possible Dosages for the Dispense Drug chosen. When both dosages exist for the Dispense Drug, the Possible Dosages list is displayed. These dosages are specific to the application package for which they are marked. When the user enters an incorrect value at the “UNITS PER DOSE:” prompt for the dosage ordered, a warning message is displayed.

The “UNITS PER DOSE:” prompt is not displayed when the user selects a dosage from the dosage selection list of Possible Dosages or Local Possible Dosages with a BCMA UNITS PER DOSE default at the “DOSAGE ORDERED:” prompt. The default value for the UNITS PER DOSE field is the value defined in the DISPENSE UNITS PER DOSE field or the BCMA UNITS PER DOSE field in the DRUG file. When the BCMA UNITS PER DOSE field is populated, it always overrides the DISPENSE UNITS PER DOSE field. If the user enters free text or no value at the “DOSAGE ORDERED:” prompt, then the “UNITS PER DOSE:” prompt is displayed so that data can be entered.

A new parameter, CALC UNITS NEEDED PRN ORDERS, is added to the PHARMACY SYSTEMS file. This parameter allows for the calculation of UNITS NEEDED on the Inpatient Medications V. 5.0 Pick List for orders with PRN in the schedule. Previously, orders with PRN in the schedule were shown on the Pick List with a UNITS NEEDED of zero (0).

The Pick List is rounding up the UNITS PER DOSE to the next whole number when it is not a whole number. This rounded number is used to calculate the number of doses needed for an order.

## Obsolete Functionality 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains any functionality that is deleted in this Inpatient Medications portion of the Master Build.

The *Inpatient Order Entry* option and *Non-Verified/Pending Orders* option are no longer checking several fields during the order entry processing. These fields include the CORRESPONDING UD ITEM field from the PHARMACY ORDERABLE ITEM file, the CORRESPONDING IV ITEM field from the PHARMACY ORDERABLE ITEM file, and the CHANGE TYPE OF ORDER FROM OERR field from the PHARMACY SYSTEMS file.

In the *Systems Parameters Edit* option, the IV IDENTIFIER field prompt and the ALLOW THE CHANGE OF ORDER TYPES ON ORDERS FROM OERR field prompt are removed.

## Impacts to Other Packages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section shows any impacts the Inpatient Medications portion of the Master Build release has to other software packages.

#### Bar Code Medication Administration (BCMA) 

The BCMA UNITS PER DOSE field in the DRUG file is created to address the number of times Nursing scans a medication to indicate the dosage administered. This field is associated with the Possible Dosages and Local Possible Dosages and is used when the DISPENSE UNITS PER DOSE field does not produce the appropriate dispensing units for Pharmacy and Nursing.

#### CPRS

Inpatient Medications has the ability to accept complex orders from CPRS. CPRS splits the complex orders and then releases the individual orders to Inpatient Medications. This includes orders entered through CPRS with the indication to be given ‘NOW’. Two orders are released to Inpatient Medications; one for the ‘NOW’ dose and the second for the continuous order.

Inpatient Medications passes a default to the CPRS package for the “Requested Start Date” prompt in the CPRS Inpatient Meds dialog. The default passed is based on the Inpatient Ward Parameter DEFAULT START DATE CALCULATION. Inpatient Medications also passes a default for the Duration prompt. The default passed is based on the same criteria that Inpatient Medications uses to determine the stop date/time for an order. Inpatient Medications also passes the next administration date/time for the order based on the administration times defined in the ADMINISTRATION SCHEDULE file for the selected schedule. When no administration times exist, renewal orders return the next administration date/time for the order based on the last administration date/time for the medication as returned to Inpatient Medications by BCMA.

# Computerized Patient Record System 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new features, functions and enhancements of the POE project for Computerized Patient Record System are grouped and discussed below.

## Options and Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed menu options and new or changed actions including hidden actions.

#### Menu Options

There are no additions or changes to any of the menu options in the Computerized Patient Record System package.

#### Actions

There are no additions or changes to any of the actions in the Computerized Patient Record System package.

## Reports and Profiles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed reports and/or profiles.

#### Reports

There are no additions or changes to any of the reports in the Computerized Patient Record System package.

#### Profiles

There are no additions or changes to any of the profiles in the Computerized Patient Record System package.

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains new or changed files and fields.

In patch OR\*3\*94, two fields in the ORDERABLE ITEMS file are updated. One field has a new cross-reference that can be triggered and the other is a new field.

#### New Field

The NON-FORMULARY field tracks if an Orderable Item is non-formulary. An Orderable Item will only be marked as non-formulary if there are no active Dispense Drugs matched to the Orderable Item that are on the local formulary.

#### Changed Field

The INPATIENT MED field triggers a new cross-reference when its value is 2 (Yes-Inpatient IV): ^ORD(101.43,"S.IVM RX",name,ien). This cross-reference is used internally for more efficient look up and ordering of Inpatient IV Medications.

## Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains any new or changed functionality to the Computerized Patient Record System package that cannot be placed in the above categories.

Patch OR\*3\*94 introduces changes to improve medications ordering by simplifying the prompts in the ordering dialog and ensuring that the medication ordering dialogs are more similar. The major changes in this patch are to data in the ORDER DIALOG file that control how a medication order is prompted for in CPRS.

This patch also includes a new order dialog called PS MEDS. The PS MEDS dialog is another MEDICATIONS order dialog that can be placed on a menu and used in addition to the existing dialogs for INPATIENT MEDS, OUTPATIENT MEDS, and IV FLUIDS. The only difference between this new dialog and the Inpatient and Outpatient dialogs is that PS MEDS will automatically assign the ordering context (Inpatient vs. Outpatient) based on the selected patient's current admission/visit status. The PS MEDS dialog provides a single dialog for medication orders instead of forcing the provider to pick among the INPATIENT MEDS, OUTPATIENT MEDS, and IV FLUIDS order dialogs. With this new dialog, the provider will not be able to write a prescription if the patient is currently admitted or order an inpatient IV medication for a patient in an outpatient clinic (i.e. the provider will not be able to write an order for the opposite context.) Therefore, the old INPATIENT MEDS, OUTPATIENT MEDS, and IV FLUIDS dialogs should still be available for the provider to select from.

To add the PS MEDS dialog to an order menu for CPRS, the user will select the *CPRS Configuration (Clin Coord)* option \[OR PARAM COORDINATOR MENU\], then select the *Order Menu Management* option \[ORCM MGMT\], and then select the *Enter/edit order menus* option \[ORCM MENU\] (such as the Add New Orders as shown in the example below).

Example: Adding the PS MEDS dialog

AU Auto-DC Parameters

AL Allocate OE/RR Security Keys

KK Check for Multiple Keys

DC Edit DC Reasons

GP GUI Parameters ...

MI Miscellaneous Parameters

NO Notification Mgmt Menu ...

OC Order Checking Mgmt Menu ...

MM Order Menu Management ...

LI Patient List Mgmt Menu ...

FP Print Formats

PR Print/Report Parameters ...

RE Release/Cancel Delayed Orders

US Unsigned orders search

EX Set Unsigned Orders View on Exit

NA Search orders by NATURE or STATUS

Select CPRS Configuration (Clin Coord) Option: MM Order Menu Management

OI Enter/edit orderable items

PM Enter/edit prompts

GO Enter/edit generic orders

QO Enter/edit quick orders

ST Enter/edit order sets

AC Enter/edit actions

MN Enter/edit order menus

AO Assign Primary Order Menu

CP Convert protocols

SR Search/replace components

LM List Primary Order Menus

DS Disable/Enable order dialogs

Select Order Menu Management Option: MN Enter/edit order menus

Select ORDER MENU: ORZ ADD MENU CLINICIAN

Menu Editor May 07, 2001 12:55:44 Page: 1 of 3

Menu: ORZ ADD MENU CLINICIAN Column Width: 26

<u>1 2 3 4</u>

\|0 ORDER SETS... 30 PATIENT CARE... 70 LABORATORY...

\|1 Patient Movement 31 Condom Catheter 71 Chem 7

\|2 Diagnosis 32 Guaiac Stools 72 T&S

\|3 Condition 33 Incentive Spirometer 73 Glucose

+4 Allergies 34 Dressing Change 74 CBC w/Diff

\| 75 PT

\|10 PARAMETERS... 40 DIETETICS... 76 PTT

\|11 TPR B/P 41 Regular Diet 77 CPK

\|12 Weight 42 Tubefeeding 78 CPK

113 I & O 43 NPO at Midnight 79 LDH

\|14 Call HO on 80 Urinalysis

\| 50 IV FLUIDS... 81 Culture & Suscept

\|20 ACTIVITY... 51 OUTPATIENT MEDS...

\|21 Ad Lib 55 INPATIENT MEDS... 90 OTHER ORDERS...

+23 Bed Rest / BRP 91 EKG: Portable

\|24 Ambulate TID 60 IMAGING ...

\|25 Up in Chair TID 61 Chest 2 views PA&LAT 99 Text Only Order

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

Add ... Edit ... Assign to User(s) Select New Menu

Remove ... Toggle Display Order Dialogs ... Quit

Select Action: Next Screen// AD Add ...

-----------------------------------------report continues----------------------------------------

Example: Adding the PS MEDS dialog (continued)

Menu Items Text or Header Row

Add: M Menu Items

ITEM: PS MEDS

ROW: 15

COLUMN: 2

DISPLAY TEXT: MEDICATIONS...

MNEMONIC: 56

ITEM:

Rebuilding menu display ...

Menu Editor May 07, 2001 12:56:11 Page: 1 of 3

Menu: ORZ ADD MENU CLINICIAN Column Width: 26

<u>1 2 3 4</u>

\|0 ORDER SETS... 30 PATIENT CARE... 70 LABORATORY...

\|1 Patient Movement 31 Condom Catheter 71 Chem 7

\|2 Diagnosis 32 Guaiac Stools 72 T&S

\|3 Condition 33 Incentive Spirometer 73 Glucose

+4 Allergies 34 Dressing Change 74 CBC w/Diff

\| 75 PT

\|10 PARAMETERS... 40 DIETETICS... 76 PTT

\|11 TPR B/P 41 Regular Diet 77 CPK

\|12 Weight 42 Tubefeeding 78 CPK

113 I & O 43 NPO at Midnight 79 LDH

\|14 Call HO on 80 Urinalysis

\| 50 IV FLUIDS... 81 Culture & Suscept

\|20 ACTIVITY... 51 OUTPATIENT MEDS...

\|21 Ad Lib 55 INPATIENT MEDS... 90 OTHER ORDERS...

+23 Bed Rest / BRP 56 MEDICATIONS... 91 EKG: Portable

\|24 Ambulate TID 60 IMAGING ...

\|25 Up in Chair TID 61 Chest 2 views PA&LAT 99 Text Only Order

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

Add ... Edit ... Assign to User(s) Select New Menu

Remove ... Toggle Display Order Dialogs ... Quit

Select Action: Next Screen// Q Quit

There are 2 parameters that can be used to define what goes into the write orders list box on the left side of the main orders window, ORWDX WRITE ORDERS LIST or ORWOR WRITE ORDERS LIST.

If the default add order menu is defined in the ORWDX WRITE ORDERS LIST (GUI) under the *General Parameter Tools* option, \[XPAR MENU TOOLS\] or the OR ADD ORDERS MENU (LM) parameter located under the *Order Menu Management Option \[ORCM MGMT\]* of the *CPRS Configuration (Clin Coord)* menu \[OR PARAM COORDINATOR MENU\], adding the PS MEDS dialog to an add order menu that exists in these 2 parameters will automatically make the PS MEDS dialog available to the users.

If the site has defined the ORWOR WRITE ORDERS LIST parameter, the user may want to add the PS MEDS dialog as an item to the system level of this parameter. Select the CPRS Configuration (IRM) option \[OR PARAM IRM MENU\], then select the General Parameter Tools option \[XPAR MENU TOOLS\], then select the Edit Parameter Values option \[XPAR EDIT PARAMETER\], (such as the ORWOR WRITE ORDERS LIST in the example).

  
Example: Adding the PS MEDS dialog

CL Clinician Menu ...

NM Nurse Menu ...

WC Ward Clerk Menu ...

PE CPRS Configuration (Clin Coord) ...

IR CPRS Configuration (IRM) ...

Select \<SMA\> CPRS Manager Menu Option: IR CPRS Configuration (IRM)

OC Order Check Expert System Main Menu ...

TI ORMTIME Main Menu ...

UT CPRS Clean-up Utilities ...

XX General Parameter Tools ...

Select \<SMA\> CPRS Configuration (IRM) Option: XX General Parameter Tools

LV List Values for a Selected Parameter

LE List Values for a Selected Entity

LP List Values for a Selected Package

LT List Values for a Selected Template

EP Edit Parameter Values

ET Edit Parameter Values with Template

Select \<SMA\> General Parameter Tools Option: EP Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: ORWOR WRITE ORDERS LIST Write Orders (Inpatient)

ORWOR WRITE ORDERS LIST may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.3 Service SRV \[choose from SERVICE/SECTION\]

2.7 Division DIV \[choose from INSTITUTION\]

3 System SYS \[SMA.ISC-XXXXX.VA.GOV\]

4 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 3 System SMA.ISC-XXXXX.VA.GOV

----- Setting ORWOR WRITE ORDERS LIST for System: SMA.ISC-XXXXX.VA.GOV ----

Select Sequence: ?

Sequence Value

-------- -----

20 GMRAOR ALLERGY ENTER/EDIT

30 FHW1

40 PSJ OR PAT OE

50 PSO OERR

60 PSJI OR PAT FLUID OE

65 LR OTHER LAB TESTS

70 RA OERR EXAM

85 GMRCOR REQUEST

90 GMRVOR

99 OR GXTEXT WORD PROCESSING ORDER

Select Sequence: 55

Are you adding 55 as a new Sequence? Yes// \<Enter\> YES

Sequence: 55// \<Enter\> 55

Order Dialog: PS MEDS

The “DISPENSE DRUG” prompt has been removed in the Inpatient Medications and Outpatient Pharmacy medications dialog. The “Dose” prompt, which was previously a free text entry that facilitated inaccurate entries that had to be corrected, now provides a list of common doses for a medication. CPRS uses an API provided by Pharmacy to get this list of common doses as set up by the pharmacy. The listed doses are tied internally to a Dispense Drug to allow for order checks and other defaults within the ordering dialog. Also, the “Dose” prompts, for Inpatient Medications and Outpatient Pharmacy, will now look the same. If needed, the strength from the associated Dispense Drug is included in the order text with the Orderable Item or, in some cases, the Dispense Drug name itself may be used if strength is not available. The cost of the associated medication dosage is displayed to the right of the dosage.

The “Dose” prompts, for Inpatient Medications and Outpatient Pharmacy, will now look the same. Prior to this patch, the “Dose” prompt in the OUTPATIENT MEDS order dialog attempted to mimic the building of a SIG, which many users found confusing. The prompt has been changed, but the order text for Outpatient Pharmacy orders will continue to include a SIG, converting the dosage data to an amount, as needed, so that patients can better understand the SIG.

This patch will take advantage of the changes in the Outpatient Pharmacy package to make the Transfer option work more consistently and efficiently. Prior to the POE patches, the Outpatient Pharmacy package did not store the SIG data in individual fields. When orders originated or new orders were created through the finishing process in the Outpatient Pharmacy package, CPRS could not copy the data into the individual fields required by the Inpatient Medications package. Outpatient Pharmacy now stores the SIG data, which should improve the operation of the Transfer option.

For complex orders, a prompt has been added to allow the ordering clinician to place AND or THEN in the dosing information of inpatient orders and place AND, THEN, or EXCEPT in the dosing information of outpatient orders. This enables concurrent dosing; formerly, only sequential dosing was supported. In addition, complex orders can now be entered for Inpatient Medications through CPRS. A separate order for each dose is created when the order is signed, for release to the Inpatient Medications package. Previously complex orders could only be entered for Outpatient Medication orders. Once a complex order is begun from the Complex dose tab, the provider must remain in the complex tab until the complex order is completely entered. Any attempts to start from or switch back to the Dosage tab will erase all complex dosages and the provider will be forced to start again.

On medications orders, CPRS presents the user with a prompt "First Dose NOW?”. If the user answers YES and the order is an Inpatient Medications order, CPRS automatically generates a second order and sends it to Inpatient Medications for a NOW order in addition to an order for the schedule entered. When ordering a complex order, the provider receives a message box indicating the first dose now is being ordered. The provider needs to ensure that the Now order and the schedule entered by the provider do not overmedicate the patient.

Previously, users could not renew a medication order through CPRS if the Orderable Item was inactive. The Inpatient Medications and Outpatient Pharmacy packages now provide CPRS with APIs that determine if an order can be renewed, regardless of whether it is active or inactive. If possible, the Outpatient Pharmacy API will also supply a replacement active Orderable Item.

Patch OR\*3\*94 corrects a situation where the IV identifier was being saved as part of the Name in the ORDERABLE ITEMS file. A post installation updates all IV medications in this file.

Patch OR\*3\*86 allowed users to specify a schedule for IV piggyback orders in CPRS; however, the schedule information was not being passed to the Inpatient Medications package. Patch OR\*3\*94 passes the information to the Inpatient Medications package.

Outpatient Pharmacy orders prompt for DAYS SUPPLY, with a default provided in the QUANTITY field based on the DAYS SUPPLY. This is an auto calculation based on the DAYS SUPPLY x SCHEDULE = QUANTITY.

A DEA number or VA number is required for ordering Schedule II drugs (i.e. narcotics), and a message displays to the provider indicating that the pharmacy will also require a wet signature on paper (in List Manager only). The DEA and VA number is set up in the Outpatient Pharmacy package and is stored in the NEW PERSON file.

In addition, to ensure that controlled substances are not accidentally ordered, CPRS now uses an API to check if the selected drug will require the signature of a provider who has a DEA number or a VA number. Prior to entering an order for a controlled substance, the provider for the selected encounter must have a DEA number or VA number assigned in the system. Before a nurse or physician’s assistant, for example, enters an order for a controlled substance, the nurse or physician’s assistant will have to change the ordering provider to someone who has a DEA number or VA number and can sign the order. In order to change the provider, the user will need to close their current ordering dialog, change the provider, and then open the appropriate ordering dialog.

The provider will receive a message when a wet signature is required for a medication order in List Manager only. This is determined by the DEA SPECIAL HANDLING field of the medication stored in the DRUG file.

Changes made to Outpatient Pharmacy orders by the pharmacist are reflected on the Orders tab; previously, updates were only shown on the Orders tab if a new order was generated by the pharmacy, though the changes did show up on the Meds tab.

A CPRS parameter, ORWDPS SUPPRESS DISPENSE MSG, is set to show drug messages to the CPRS users when this parameter is delivered during the installation of this project. If the drug message is not to be seen by the CPRS users, this parameter should be set appropriately.

## Obsolete Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains any functionality that has been deleted in this Computerized Patient Record System portion of the Master Build.

There is no removal of any current functionality in the Computerized Patient Record System package.

## Impacts to Other Packages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section shows any impacts the Computerized Patient Record System portion of the Master Build release has to other software packages.

#### Inpatient Medications

With the release of this build, CPRS can now accept complex medication orders for inpatients. These orders are split into separate orders and then released to the Inpatient Medications package.

\<This page is intentionally left blank.\>