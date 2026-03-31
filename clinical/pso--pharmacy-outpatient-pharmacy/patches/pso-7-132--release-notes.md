---
title: PSO*7*132 Herbal/OTC/Non-VA Meds Documentation Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Herbal/OTC/Non-VA Meds Documentation
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*132
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: "Non-VA Meds functionality affects Pharmacy Data Management in the following ways:"
audience: 
keywords: 
  - meds
  - drug
  - table
  - contents
  - pharmacy
  - report
  - patient
  - other
  - entries
  - medications
page_count: 0
word_count: 2981
section_count: 15
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p132_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p132_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

> ![](pso-7-132-herbal-otc-non-va-meds-documentation-release-notes/001.png)

Herbal/OTC/Non-VA Meds Documentation  

####### RELEASE NOTES 

May 2004

PSS\*1\*68

PSS\*1\*69

OR\*3\*176

PSO\*7\*132

PSJ\*5\*107

OR\*3\*190

GMTS\*2.7\*65

V*IST*A Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [Pharmacy Data Management](#pharmacy-data-management)
  - [Overview](#overview)
  - [Features, Functions and Enhancements](#features-functions-and-enhancements)
  - [Files and Fields](#files-and-fields)
  - [Other Functionality](#other-functionality)
- [Outpatient Pharmacy](#outpatient-pharmacy)
  - [Overview](#overview-1)
  - [Features, Functions, and Enhancements](#features-functions-and-enhancements-1)
  - [Files and Fields](#files-and-fields-1)
  - [Other Functionality](#other-functionality-1)
- [Inpatient Medications](#inpatient-medications)
  - [Overview](#overview-2)
  - [Features, Functions and Enhancements](#features-functions-and-enhancements-2)
  - [Files and Fields](#files-and-fields-2)
  - [Other Functionality](#other-functionality-2)
- [Helpful Information](#helpful-information)
  - [Communicating New Non-VA Meds Entries to the Pharmacist](#communicating-new-non-va-meds-entries-to-the-pharmacist)
    - [Manual Processes](#manual-processes)
    - [Create a new Drug Entry called “Other”](#create-a-new-drug-entry-called-other)
    - [CPRS Tools Menu Option](#cprs-tools-menu-option)
  - [Test Sites’ Herbals Entries](#test-sites-herbals-entries)
The purpose of these release notes is to briefly describe the features and functions of the Pharmacy portion of Herbal/OTC/Non-VA Meds Documentation software, also known as Non-VA Meds software. Pharmacy Data Management, Inpatient Medications, and Outpatient Pharmacy information is included in this manual for the Pharmacy side of the project. This document is intended for the Information Resources Management Service (IRMS) staff and the Pharmacy Automated Data Processing Application Coordinator (ADPAC).
Through both Pharmacy and Computer Patient Record System (CPRS), Non-VA Meds provides accessible information about a patient’s use of the following medications:
- Over The Counter (OTC) medications
- Herbal supplements
- Medications prescribed by providers outside the VA
- Medications prescribed by the VA, but purchased by the patient at an outside pharmacy.
Non-VA Meds software allows the pharmacist to use this data to screen for Drug-Herbal and Drug-Drug interactions with prescribed medications in Veterans Health Information Systems and Technology Architecture (V*IST*A). It meets the Joint Commission for Accreditation of Healthcare Organizations (JCAHO) requirement that all health care facilities document a patient’s use of over the counter (OTC) medications and herbal supplements.
Non-VA Meds orders cannot be placed or updated in Pharmacy. The user can input information about a patient’s use of Non-VA Meds only through CPRS. However, the user can use either CPRS or Pharmacy menu options to view Non-VA Meds data in a patient’s medical records.
|                                                                                                     |                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pso-7-132-herbal-otc-non-va-meds-documentation-release-notes/002.png) | This document will refer to OTC medications, herbal supplements, medications prescribed by providers outside the VA, and medications prescribed by the VA, but purchased by the patient at an outside pharmacy, as Non-VA Meds. |
Non-VA Meds software is not part of a master build. The Non-VA Meds project includes patches PSS\*1\*68, PSS\*1\*69, OR\*3\*176, PSO\*7\*132, PSJ\*5\*107, GMTS\*2.7\*65, and OR\*3\*190, which are installed separately. The software listed below must be installed before one can load all the patches that make Non-VA Meds functional.
| Package              | Minimum Version Needed |
|--------------------------|----------------------------|
| VA FileMan               | 22.0                       |
| Kernel                   | 8.0                        |
| MailMan                  | 7.1                        |
| Outpatient Pharmacy      | 7.0                        |
| Inpatient Medications    | 5.0                        |
| PIMS                     | 5.0                        |
| Pharmacy Data Management | 1.0                        |
| National Drug File       | 4.0                        |
| OE/RR                    | 3.0                        |

# Pharmacy Data Management 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists changed features, functions, and enhancements of the Non-VA Meds software for the Pharmacy Data Management package.

![](pso-7-132-herbal-otc-non-va-meds-documentation-release-notes/003.png)Patches PSS\*1\*68 and PSS\*1\*69 were released in June and September 2003 respectively.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Non-VA Meds functionality affects Pharmacy Data Management in the following ways:

- It adds a new Application Package Use value, Non-VA Med, and allows entries in the DRUG file (#50) to be marked as such.
- It allows the user to enter and view Non-VA Meds into the DRUG file (#50).
- It allows the user to indicate whether a Drug is marked as a Non-VA Med in DRUG file (#50).

## Features, Functions and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains information about changed Pharmacy Data Management menu options for the Non-VA Meds software. No menu options or actions have been added or deleted.

#### Changed Menu Options

############################### 

The following menu options have been changed to support Non-VA Meds:

- *Enter/Edit Dosages* \[PSS EDIT DOSAGES\] option displays “Non-VA Med” if the drug is marked as a Non-VA Med.
- *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option allows the user to enter herbal and other OTC medications into the DRUG file (#50), and to mark a Drug as a Non-VA Med. To mark a drug as a Non-VA Med, the user must hold the ‘PSORPH’ security key.
- *Lookup into Dispense Drug File* \[PSS LOOK\] option displays “Non-VA Med” if the drug is marked as a Non-VA Med.
- *Edit Orderable Items* \[PSS EDIT ORDERABLE ITEMS\] lists whether a drug (Orderable Item) in the PHARMACY ORDERABLE ITEM file (#50.7) is marked for Non-VA Meds.

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains information about modified files and fields. No new files have been added to Pharmacy Data Management application for the Non-VA Meds software; however, a new sub-file NON-VA MEDS (#55.05) has been added to PHARMACY PATIENT file (#55), which will be used to store the Non-VA Med orders.

#### #### New Sub-File

############################### 

############################### PHARMACY PATIENT file (#55), NON-VA MEDS sub-file (#55.05):

This sub-file will store the Non-VA Med orders and contain the following fields:

- Orderable Item (only field that is required by CPRS)
- Dispense Drug
- Dosage
- Medication Route
- Schedule
- Pointer to CPRS Orders File (#100)
- Status
- Disclaimer (Word Processing Field)
- Start Date
- Documented By
- Documented Date
- Order Checks (multiple)
  - Order Check Narrative
  - Override Reason
  - Override Provider
- Clinic
- Discontinued Date
- Comments

#### New Fields

############################### 

############################### NON-VA MED field (#8)

############################### 

############################### This field in the PHARMACY ORDERABLE ITEM file (#50.7) identifies whether the Pharmacy Orderable Item is selectable as a Non-VA Med. This field is not editable.

############################### 

#### Changed Fields

############################### 

############################### APPLICATION USAGE PKG field (#63) in the DRUG file (#50)

############################### 

A new application use indicator of “X” is added to this field to indicate a Dispense drug can be used as a Non-VA Med. All Dispense drugs must be marked with an “X” to be selectable as Non-VA Meds.

############################### 

############################### 

## Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Installation of patches PSS\*1\*68 and PSS\*1\*69, all active DRUG file (#50) entries that are flagged for Outpatient ordering are auto-populated with the “X” to indicate the drug can be ordered through the CPRS Non-VA Meds ordering dialog. These patches were released in 2003.

An Orderable Item is marked as a Non-VA Med only if one or more Dispense drugs that are matched to the Orderable Item are active and marked for use as a Non-VA Med. Marking Orderable Items for Non-VA Med use does not limit its use for Outpatient Pharmacy or Inpatient Medications meds.

When a provider selects an Orderable Item in CPRS that is identified for use as a Non-VA Med, Pharmacy Data Management will provide a list of all possible dosages based on the Dispense drugs associated to the Orderable Item and those, which are marked for Non-VA Med use. The provider can then select a specific dosage from the list for the Non-VA Med or leave it blank.

<span class="mark">  
</span>*(This page included for two-sided copying.)*

# Outpatient Pharmacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists new and changed features, functions, and enhancements of the Non-VA Meds software for the Outpatient Pharmacy package.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Non-VA Meds functionality affects Outpatient Pharmacy in the following ways:

- Non-VA Meds will be displayed on all screen displays or printouts where medications for a patient are listed/shown or displayed.
- A new *Non-VA Meds Usage Report* \[PSO NON-VA MEDS USAGE REPORT\] menu option is added under the *Output Reports* \[PSO OUTPUTS\] option.
- Non-VA Meds are included as part of the drug-drug interaction, drug-allergy interaction, and duplicate order checks when entering new prescriptions.
- Non-VA Meds will be included in the Rx Health Summary report.

|                                                                                                     |                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pso-7-132-herbal-otc-non-va-meds-documentation-release-notes/004.png) | The user cannot place or update Non-VA Meds in the Outpatient Pharmacy package. The user can only use Outpatient Pharmacy options to view Non-VA Meds data in a patient’s medical records. |

## Features, Functions, and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains information about new Outpatient Pharmacy menu options and actions, and changed reports for the Non-VA Meds software. No menu options, reports, or actions have been deleted.

#### New Menu Option

The following new report menu option has been added to support Non-VA Meds:

############################### 

- *Non-VA Meds Usage Report* \[PSO NON-VA MEDS USAGE REPORT\] option retrieves the Non-VA Med orders entered by CPRS and stored in the PHARMACY PATIENT file (#55). This 80-column report is part of the *Output Reports* \[PSO OUTPUTS\] option. It provides the following prompts in order to generate the report:
- Flexibility of selecting a Date Range (Documented Date).
- The option of choosing various SORT criteria, such as “Date Documented,” “Patient Name,” “Orderable Item,” “Status,” or “Order Checks.”
- Output device to print the report (screen or to a device).
- The new report contains the following fields:

Patient Name Clinic

> Last 4 SSN Start Date

> Patient Phone Number Dispense Drug

> Orderable Item Dosage

> Status Medication Route

> Discontinued Date Schedule

> Order Number Order Checks (multiple)

> Documented By Override Reason

> Documented Date Override Provider

Statement/Explanation

#### New Action

The following new hidden action has been added to the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option to support Non-VA Meds:

############################### 

- The hidden action, Non-VA Meds Report \[NV\], will print the *Non-VA Meds Usage Report* \[PSO NON-VA MEDS USAGE REPORT\] option for the current patient selected on the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option. This new action, NV, exists under the hidden *Other OP Actions* \[OTH\] option, within the Medication Profile screen. While the hidden action provides the same information as *Non-VA Meds Usage Report* \[PSO NON-VA MEDS USAGE REPORT\] option, this report is patient specific and the user is able to select a date range and a device.

#### Changed Menu Options

All menu options that display medications for a patient on the screen or in a printout will contain the patient’s Non-VA Meds.

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new files or fields have been added to the Outpatient Pharmacy package for the Non-VA Meds software.

## Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current Interface, used to provide order checks to the CPRS and the Inpatient Medications packages has been updated to include Non-VA Meds.

The Interface that passes Pharmacy orders to the CPRS Meds Tab includes Non-VA Meds.

The Health Summary Interface and the Clinical Reminders Interface also include Non-VA Meds.

Non-VA Meds are included in order checking during backdoor Prescription Order Entry for duplicate drugs, duplicate drug class and drug interactions. These order checking results are displayed to the user in the same way that pending orders and outpatient prescriptions is currently displayed. Any item in the DRUG file (#50) that is identified with the VA drug class of HA000 for Herbals will not display duplicate drug warnings or duplicate drug class checks against another drug with the same VA drug class of HA000. This is due to ALL Herbals being identified by the VA drug class of HA000.

Non-VA Meds are automatically discontinued, the same as Prescriptions and Outpatient Pharmacy pending orders, when a Date of Death has been entered for a patient. In the event a Date of Death is entered in error and subsequently deleted, the Non-VA Meds will be automatically reinstated to an active status if they were active before they were discontinued.

*(This page included for two-sided copying.)*

# Inpatient Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists new and changed features, functions, and enhancements of the Non-VA Meds software for the Inpatient Medications package.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Non-VA Meds functionality affects Inpatient Medications in the following way:

- It includes Non-VA Meds in the drug-drug interaction, drug-allergy interaction, and duplicate drug order checking.

## Features, Functions and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No menu options or actions have been added or deleted.

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new files or fields have been added to Inpatient Medications for the Non-VA Meds software.

## Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no other functionality added to the Inpatient Medications package for the Non-VA Meds software.

*(This page included for two-sided copying.)*

# Helpful Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Communicating New Non-VA Meds Entries to the Pharmacist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Test Sites for the Non-VA Meds project suggested several different communication methods to the Pharmacy Staff to use when a Non-VA Med is not found and will need to be added to the system. These are only suggestions and are listed below.

### Manual Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When one of your staff encounters a Non-VA Med that has not been documented, instruct them to telephone or e-mail the Pharmacy person responsible for adding the Non-VA Meds. The Pharmacy person can add the new Herbal, OTC Med or prescription medication and make it available for use within the Non-VA Meds software.

### Create a new Drug Entry called “Other”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a new drug entry called “Other” and mark it for use with Non-VA Meds only. Then instruct the staff responsible at your facility for documenting Non-VA Meds usage to select “Other” when the item they need is unavailable. Have the documenter enter the actual drug name they need in the COMMENTS field.

The Pharmacy persons can run the new report *Non-VA Meds Usage Report* option to review the active listings of the drug “Other” for any patient. Instruct your Pharmacy persons who can add new Non-VA Meds entries to review the Non-VA Meds Usage Report often. By regularly reviewing this report, they will know when to add requested items for selection and can update the patient's Non-VA Meds entries to reflect any new requested item.

The *Non-VA Meds Usage Report* \[PSO NON-VA MED USAGE\] option is located under the *Output Reports* \[PSO OUTPUTS\] option on the *Outpatient Pharmacy Manager* menu option. The Pharmacy persons will enter a date for the “FROM DATE DOCUMENTED” and “TO DATE DOCUMENTED,” prompts. To show all of the active listings of the drug “Other”, sort by Orderable Item. Please emphasize that this report must be run and reviewed regularly to ensure the requested Non-VA Meds are known and can be added to the system.

### CPRS Tools Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One facility developed a local solution that is placed on the Tools menu within CPRS. This solution simply opens a New Message in Outlook with the 'To:' address already filled in to deliver the message to your Pharmacy persons who can then add a new Non-VA Meds entry. The staff responsible at your facility for documenting Non-VA Meds usage can use the messaging tool to request a new Non-VA Med be made available for documentation.

To setup this CPRS Tools Menu option:

Select General Parameter Tools Option:  Edit Parameter Values  
                         --- Edit Parameter Values ---

 

Select PARAMETER DEFINITION NAME:    ORWT TOOLS MENU   CPRS GUI Tools Menu

 

ORWT TOOLS MENU may be set for the following:

 

     1   User          USR    \[choose from NEW PERSON\]  
     2   Location      LOC    \[choose from HOSPITAL LOCATION\]  
     2.5 Service       SRV    \[choose from SERVICE/SECTION\]  
     3   Division      DIV    \[ISC REGION 3\]  
     4   System        SYS    \[OPAVAA.FO-BIRM.MED.VA.GOV\]

 

\*\* NOTE: Select the parameter level you wish to modify. If you currently have no parameters set up, your users will see the default tools menu items. If you wish to retain those choices for your users, you must enter each of those choices as Sequences for the parameter level you are editing and add this new sequence for creating an e-mail message.

 

Enter selection: 1  User   NEW PERSON  
Select NEW PERSON NAME:    OPPROVIDER,ONE     TUSC     ALABAMA     DEWC     IRM 

 

--------------- Setting ORWT TOOLS MENU  for User: OPPROVIDER,ONE------  
Select Sequence: 2

 

Sequence: 2// \<Enter\>   2

\*\*NOTE: Substitute the person or mailgroup name you wish to receive this message. For mailgroups, you must view the mailgroup in the Outlook Global Address Listing. Look at the e-mail addresses tab to get the mailgroup name you will use. This will likely be different from the group name you normally type into the GAL, as the actual group name will have no spaces and must be unique.

Name=Command: &Send=MAILTO:one.opprovider@med.va.gov?subject=Add_new_Non-VA_Med_as_Selectable  
  Replace  
Select Sequence:

## Test Sites’ Herbals Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Veterans Health Administration (VHA) currently has no authoritative source of herbals to distribute via the National Drug File (NDF). However, a few herbals do have sufficient documentation to allow the NDF Manager to distribute them via National Drug File patches and those herbal entries have already been released to the field. More herbal entries may be added in the future.

The Test Sites’ Herbals Entries document has been prepared to serve as an example of Herbal entries that other sites found necessary to run the Non-VA Meds software at their facility. Your facility may choose to start with these examples or to build your own set of herbal entries.

The herbal entries provided in the *Test Sites’ Herbals Entries* document are listed by the submitting site’s name and include the drug name, VA Class, NDF drug, any applicable synonyms, dosages, and ingredients. These entries can provide a starting point for the enhancement of the DRUG file (#50) entries to be marked for Non-VA Meds use.

The *Test Sites’ Herbals Entries* document can be found on the Technical Services Project Repository (TSPR) on the Herbal/OTC/Non-VA Meds Documentation project notebook page under the *Training Materials* heading:

<span class="mark">REDACTED</span>

*(This page included for two-sided copying.)*