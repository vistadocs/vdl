---
title: PSS*1*129/147 Implementation Guide - Pharmacy Reengineering (PRE) V.0.5 Pre-Release
doc_type: IG-IMP
doc_label: Implementation Guide
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
  - dose
  - unit
  - package
  - local
  - numeric
  - possible
  - drug
  - dosages
  - medication
  - strength
page_count: 0
word_count: 24858
section_count: 31
table_count: 8
figure_count: 0
appendix_count: 6
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p129_p147_r0210_img.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p129_p147_r0210_img.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/001.png)

# PHARMACY REENGINEERING (PRE) Version 0.5Pre-Release


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [PHARMACY REENGINEERING (PRE) Version 0.5Pre-Release](#pharmacy-reengineering-pre-version-05pre-release)
- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Project Description](#project-description)
  - [Scope](#scope)
  - [Menu Changes](#menu-changes)
    - [Pharmacy Data Management menu (Restructured)](#pharmacy-data-management-menu-restructured)
    - [Enhanced Order Checks Setup Menu (New)](#enhanced-order-checks-setup-menu-new)
    - [IV Additive/Solution Reports (New)](#iv-additivesolution-reports-new)
- [Functionality](#functionality)
  - [Steps](#steps)
    - [Local Medication Route Mapping](#local-medication-route-mapping)
    - [### Local Possible Dosage Setup](#local-possible-dosage-setup)
    - [Frequency Review](#frequency-review)
    - [Identify IV Solution PreMixes](#identify-iv-solution-premixes)
    - [Enter/Edit Additive Frequency for IV Additives](#enteredit-additive-frequency-for-iv-additives)
  - [Medication Route Mapping Report](#medication-route-mapping-report)
  - [Find Unmapped Local Medication Routes](#find-unmapped-local-medication-routes)
  - [Request Change to Standard Medication Route](#request-change-to-standard-medication-route)
  - [Map Local Medication Route to Standard](#map-local-medication-route-to-standard)
  - [Medication Route File Enter/Edit](#medication-route-file-enteredit)
  - [Medication Route Mapping History Report](#medication-route-mapping-history-report)
- [Chapter 2 – Local Possible Dosage Setup](#chapter-2-local-possible-dosage-setup)
  - [Local Possible Dosages Report](#local-possible-dosages-report)
  - [Find Unmapped Local Possible Dosages](#find-unmapped-local-possible-dosages)
  - [Request Change to Dose Unit](#request-change-to-dose-unit)
  - [Map Local Possible Dosages](#map-local-possible-dosages)
  - [Enter/Edit Dosages](#enteredit-dosages)
  - [Drug Enter/Edit](#drug-enteredit)
  - [Strength Mismatch Report](#strength-mismatch-report)
  - [Review Dosages Report](#review-dosages-report)
  - [# Chapter 3 – Frequency Review](#chapter-3-frequency-review)
  - [Administration Schedule File Report](#administration-schedule-file-report)
  - [Medication Instruction File Report](#medication-instruction-file-report)
- [Chapter 4 – Identify IV Solution PreMixes](#chapter-4-identify-iv-solution-premixes)
  - [IV Solution Report](#iv-solution-report)
  - [Mark PreMix Solutions](#mark-premix-solutions)
  - [Drug Enter/Edit](#drug-enteredit-1)
  - [Primary Solution File (IV)](#primary-solution-file-iv)
- [Chapter 5 – Enter/Edit Additive Frequency for IV Additives](#chapter-5-enteredit-additive-frequency-for-iv-additives)
  - [IV Additive Report](#iv-additive-report)
  - [Drug Enter/Edit](#drug-enteredit-2)
- [Appendix A: Standard Medication Routes File](#appendix-a-standard-medication-routes-file)
- [Appendix B: New DOSE UNITS File with FDB mapping](#appendix-b-new-dose-units-file-with-fdb-mapping)
- [# Appendix C: List of Dosage Forms to Exclude from Dosage Checks](#appendix-c-list-of-dosage-forms-to-exclude-from-dosage-checks)
- [# Appendix D: VA Products with OVERRIDE DF DOSE CHK EXCLUSION field set to ‘Yes’](#appendix-d-va-products-with-override-df-dose-chk-exclusion-field-set-to-yes)
  - [# # Appendix E: Examples of Local Medication Route Mappings to Standard](#appendix-e-examples-of-local-medication-route-mappings-to-standard)
  - [# Appendix F: Local Possible Dosages Report](#appendix-f-local-possible-dosages-report)

####### Implementation Guide 

PSS\*1\*129 & PSS\*1\*147
February 2010
Office of Enterprise Development
Revision History
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 62%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Revised Pages</td>
<td>Patch Number</td>
<td>Description</td>
</tr>
<tr class="even">
<td>02/2010</td>
<td>All</td>
<td>PSS*1*147</td>
<td><p>Added Revision History page.</p>
<p>Updated patch references to include PSS*1*147.</p>
<p>Described files, fields, options and routines added/modified as part of this patch. Added Chapter 5, Additive Frequency for IV Additives, to describe the steps needed to ensure correct data is in the new IV Additive <mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>01/2009</td>
<td>All</td>
<td>PSS*1*129</td>
<td><p>Original version</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>
*(This page included for two-sided copying.)*
Table of Contents

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Implementation Guide provides information needed to implement the Pharmacy Reengineering (PRE) Version 0.5 Pre-Release patch PSS\*1\*129 and Pre-Release Enhancements patch PSS\*1\*147. The intended audience for this document is the Pharmacy staff responsible for maintaining Pharmacy files.

In order to be able to implement a portion of the enhanced order checking functionality, specifically the new dosing checks, the work required by this Pre-Release patch PSS\*1\*129 and Pre-Release Enhancements patch PSS\*1\*147 must be completed.

## Project Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PRE V. 0.5 project will deliver enhanced order checking functionality utilizing Health*e*Vet (H*e*V) compatible architecture to the field and address some Patient Safety Issues (PSI) regarding order checks. PRE V. 0.5 will implement the enhanced order checking accomplished in 2006 with the development of the Proof -Of-Concept (POC). Services provided by First DataBank (FDB), our current drug database vendor, will be utilized. A Pre-Release will be delivered to allow for file mapping, setup, and review in preparation of the new dosing checks to be implemented in PRE V. 0.5. A Graphical User Interface (GUI) application will be developed to allow for customization of FDB standard reference tables used in the enhanced order checking. The GUI application will be utilized by the National Drug File (NDF) Manager or designee to update the FDB custom tables. In the future, access will be given to local users to request custom changes. A process via File Transfer Protocol (FTP) to update local/regional instances of FDB standard and custom tables from a national database will also be provided.

Enhanced Order Checking Features for PRE V. 0.5:

- Enhanced drug-drug interaction order check to provide the clinician with more information by displaying a short description of the clinical effects of the drug interaction and providing an optional view of a detailed professional drug interaction monograph
- The *Enter/Edit Local Drug Interaction* \[PSS INTERACTION LOCAL ADD\] option will be deleted
- Create a new option called *Request Changes to Enhanced Order Check Database* to allow custom requests by pharmacy users
- The *Edit Drug Interaction Severity* \[PSS INTERACTION SEVERITY\] stand alone option will be deleted
- Enhanced duplicate therapy order check to utilize FDB’s Enhanced Therapeutic Classification System which allows for multiple classes per drug
- New Maximum Single Dosage order check
- New Daily Dosage Range order check
- Provide general dosing information for a drug when dosage checks cannot be performed
- Incorporate new dosage checks within Outpatient Pharmacy verification options
- Redesign drug interaction and duplicate therapy order check display warnings and action prompts for Inpatient Medications (IV and Unit Dose) application to minimize user confusion (PSI-07-080)
- Add new intervention types to accommodate interventions added for dosage checks
- Order check display sequence changes for efficiency and consistency between Outpatient Pharmacy and Inpatient Medications applications (PSI-07-080)
- Order check information display changes for consistency between Remote Data Interoperability (RDI) and local medication order information and for improved readability and processing
- Provide error messages at the system, drug or order level when order checks cannot be performed
- Send a priority notification message to a mail group when FDB link is down
- Ability to perform drug-drug interaction, duplicate therapy and dosing order checks on PreMix solutions (PSI-06-01)
- Provide a quick and timely notification display of recently discontinued/expired outpatient and inpatient medication orders
- Provide quick identification of the action on the medication profile by which an outpatient or inpatient order was discontinued or held
- Provide display changes to Duplicate Drug Order Check for outpatient pharmacy to be consistent with the enhanced Drug Interaction and Duplicate Therapy Order Checks
- Remove Duplicate Drug Order Check from Inpatient Medications application; all duplicate drug orders will be presented as duplicate therapy warnings
- Provide Intervention Menu hidden action on additional ListMan order screens for both Outpatient Pharmacy and Inpatient Medications applications
- Addition of three new Computerized Patient Record System (CPRS) (OE./RR) V. 3.0 Order Checks (Aminoglycoside Ordered, Glucophage Lab Results, and Dangerous Meds for Patient \>64) to Pharmacy backdoor order checks
- Provide an option to allow a user to check to see if the link to the FDB database is up or down
- Provide consistency between Allergy/ADR order check displays in Outpatient Pharmacy and Inpatient Medications
- Allow the user to take action after an Allergy/ADR order check is displayed for Inpatient Medications application
- Provide user notifications of updates/additions within Standard Medication Routes file
- Create/Modify Application Programmers Interfaces (APIs) (i.e. CPRS, etc) in M environment to support order check enhancements
- Provide an option to allow a user to disable/enable the connection to the vendor database
- Provide an option to ensure that the connection to the vendor database is operational and that the enhanced order checks can be executed successfully
- Provide option to keep track of when and for how long the vendor database connection is unavailable

H*e*V Construction includes:

- Component(s) to utilize services provided by a commercial drug database to support Legacy VistA order check changes

The enhancements to drug-drug interactions, duplicate therapy, duplicate drug order checks and introduction of new dosing order checks will also be incorporated within the CPRS application.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this PRE V.0.5 Pre-Release patch is to have sites perform some preparation work for the upcoming release of the Pharmacy Reengineering (PRE) Version 0.5 order check enhancements. Enhancing current Drug-Drug interaction and Duplicate Class order checks, as well as introducing new dosing order checks will be accomplished by utilizing a First DataBank (FDB) Drug Information Framework (DIF) database and APIs. Interfacing to FDB’s database and utilizing their APIs requires some mapping to be performed between VistA files and FDB tables. Local Medication Routes will have to be mapped to a Standard Medication Route which is mapped to an FDB table entry. In order to be able to perform dosing checks on a Local Possible Dosage, which is free text, sites will be asked to break down each Local Possible Dosage into a Numeric Dose and Dose Unit. The FREQUENCY (IN MINUTES) field (#2) of ADMINISTRATION SCHEDULE file (#51.1) and the FREQUENCY (IN MINUTES) field (#31) of the MEDICATION INSTRUCTION file (#51) will require review to ensure they have been populated, if appropriate. The frequency is necessary when executing a daily dose range check on a prescribed drug within an order. Sites will be asked to identify IV Solutions that are considered as PreMixes so that they can be included in order checks.

Patch PSS\*1\*147 – Pre-Release Enhancements creates a new ADDITIVE FREQUENCY field (#18) in the IV ADDITIVES file (#52.6). During the post-init the patch will auto populate the field with data. A new IV Additive Report \[PSS ADDITIVE REPORT\] is provided for users to review the data for accuracy and edit if necessary. This new field will be used to provide a default value for the ADDITIVE FREQUENCY field in CPRS for the IV Fluid dialog when continuous IV orders with additives are entered.

Pharmacy Data Management V.1.0 package, PSS\*1\*129 and PSS\*1\*147 patches, create new fields and files and provide reports and options to assist in the population and maintenance of data necessary for the future installation of the Enhanced Order Checks PRE V. 0.5 project patches for Pharmacy Data Management V. 1.0, Inpatient Medications V. 5.0, Outpatient Pharmacy V. 7.0 and CPRS.

## Menu Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new *Enhanced Order Checks Setup Menu* has been created under the main *Pharmacy Data Management* menu. The existing *Pharmacy Data Management* menu has been restructured to add some of the same new reports and options on the *Enhanced Order Checks Setup Menu*. The *Enhanced Order Checks Setup Menu* will be deleted once PRE V. 0.5 is released. Details on the new and modified options can also be found in the *Pharmacy Reengineering (PRE) V.0.5 Pre-Release Release Notes*, *Pharmacy Data Management (PDM) V.1.0 User Manual* and *Pharmacy Data Management (PDM) V.1.0 Technical Manual*.

### Pharmacy Data Management menu (Restructured)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS MGR\]

Select Pharmacy Data Management Option: ??

CMOP Mark/Unmark (Single drug) \[PSSXX MARK\]

\*\*\> Locked with PSXCMOPMGR

Dosages ... \[PSS DOSAGES MANAGEMENT\]

Drug Enter/Edit \[PSS DRUG ENTER/EDIT\]

Drug Interaction Management ... \[PSS DRG INTER MANAGEMENT\]

Electrolyte File (IV) \[PSSJI ELECTROLYTE FILE\]

Lookup into Dispense Drug File \[PSS LOOK\]

Medication Instruction Management ... \[PSS MED INSTRUCTION MANAGEMENT\]

Medication Routes Management ... \[PSS MEDICATION ROUTES MGMT\]

Orderable Item Management ... \[PSS ORDERABLE ITEM MANAGEMENT\]

Formulary Information Report \[PSSNFI\]

Drug Text Management ... \[PSS DRUG TEXT MANAGEMENT\]

Pharmacy System Parameters Edit \[PSS SYS EDIT\]

Standard Schedule Management ... \[PSS SCHEDULE MANAGEMENT\]

Synonym Enter/Edit \[PSS SYNONYM EDIT\]

Controlled Substances/PKI Reports ... \[PSS CS/PKI REPORTS\]

Send Entire Drug File to External Interface \[PSS MASTER FILE ALL\]

Enhanced Order Checks Setup Menu ... \[PSS ENHANCED ORDER CHECKS\]IV Additive/Solution Reports ... \[PSS ADDITIVE/SOLUTION REPORTS\]

Warning Builder \[PSS WARNING BUILDER\]

Warning Mapping \[PSS WARNING MAPPING\]

### Enhanced Order Checks Setup Menu (New)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS ENHANCED ORDER CHECKS\]

Select Pharmacy Data Management Option: ENHANCed Order Checks Setup Menu

Find Unmapped Local Medication Routes \[PSS MED ROUTES INITIAL MAPPING\]

Map Local Medication Route to Standard \[PSS MAP ONE MED ROUTE\]

Medication Route Mapping Report \[PSS MED ROUTE MAPPING REPORT\]

Medication Route File Enter/Edit \[PSS MEDICATION ROUTES EDIT\]

Medication Route Mapping History Report \[PSS MED ROUTE MAPPING CHANGES\]

Request Change to Standard Medication Route \[PSS MEDICATION ROUTE REQUEST\]

Find Unmapped Local Possible Dosages \[PSS LOCAL DOSAGES EDIT ALL\]

Map Local Possible Dosages \[PSS LOCAL DOSAGES EDIT\]

Local Possible Dosages Report \[PSS LOCAL POSSIBLE DOSAGES\]

Strength Mismatch Report \[PSS STRENGTH MISMATCH\]

Enter/Edit Dosages \[PSS EDIT DOSAGES\]

Request Change to Dose Unit \[PSS DOSE UNIT REQUEST\]

Mark PreMix Solutions \[PSS MARK PREMIX SOLUTIONS\]

IV Solution Report \[PSS IV SOLUTION REPORT\]

Administration Schedule File Report \[PSS SCHEDULE REPORT\]

Medication Instruction File Report \[PSS MED INSTRUCTION REPORT\]

### IV Additive/Solution Reports (New)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS ADDITIVE/SOLUTION REPORTS\]

> Select Pharmacy Data Management Option: IV Additive/Solution Reports

> IV Additive Report (New)

> IV Solution Report

> NOTE: These options do not affect the current functionality of the Inpatient Medications, Outpatient Pharmacy, or CPRS applications.

# Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Functionality of the PRE V. 0.5 Pre-Release (PSS\*1\*129) and Pre-Release enhancements (PSS\*1\*147) patches can be divided into five areas:

1.  Local Medication Route Mapping
2.  Local Possible Dosage Setup
3.  Frequency Review
4.  Identify IV Solution PreMixes
5.  Enter/Edit Additive Frequency for IV Additives

> Of these five, the area that will command the most time is the Local Possible Dosage Setup. In order to accurately perform dosage checks, it is very important that each Local Possible Dosage be broken down to an appropriate Dose Unit and corresponding Numeric Dose.

> Each of the five affected areas is discussed in detail below.

1.  Local Medication Route Mapping

> In order to perform a dosage check, the medication route by which a medication is given must be taken into account. Since the First DataBank (FDB) database is utilized to perform the dosage checks, we need to map our Local Medication Routes in VistA to an FDB Route. A new STANDARD MEDICATION ROUTES file (#51.23) was created in VistA to accomplish this. This file has been standardized by Standards and Terminology Service (STS) and mapped to an FDB Route. Options have been provided for sites to map each Local Medication Route that is marked for ‘All Packages’ to an active Standard Medication Route. Reports have also been provided to review the mappings. When dosage checks are performed, the software will use this mapping to pass the equivalent FDB Route for the Local Medication Route that was specified in the medication order for the drug to the interface. If the Local Medication Route is not mapped, dosage checks will not be performed. The user entering the order will be informed that the dosage check was not performed and the reason why. In this case, general dosing information cannot be provided to the user either. If a Local Medication Route cannot be mapped because a corresponding Standard Medication Route is not available, an option to request a new Standard Medication Route or change an existing one is provided.

> Appendix E provides examples of Local Medication Route Mappings to a Standard.  When mapping, if it is not clear as to which Standard Medication Route one should map their Local Medication Route to, use the following guidelines:

1)  The first thing you should look at is the drugs being ordered with that Local Medication Route. By what route are they normally administered?   For example, a Local Medication Route of ‘Affected Area’ is usually used with topical drugs. The most appropriate Standard Route to map the Local Medication Route of ‘Affected Area’ would be ‘Topical’.
2)  If you have Local Medication Routes defined that are used when ordering supplies, map to the Standard Medication Route of ‘NOT APPLICABLE’.
3)  Local Medication Routes that are combinations, i.e. Intramuscularly or By Mouth should be mapped to the Standard Medication Route of ‘NOT APPLICABLE’.
4)  In some cases, you may not find the exact Local Medication Route term in the Standard Medication Route file to map to. However, there may be a Standard Medication Route that is comparable to map to that is named differently. For example, the Local Medication Route of ‘Percutaneous’ can be mapped to the Standard Medication Route of ‘Transdermal’ and a Local Medication Route of ‘Intra-Abdominal’ can be mapped to ‘Intraperitoneal’.
5)  In some cases, there will just be no appropriate Standard Medication Route to map to. In those cases, leave the Local Medication Route unmapped.  For example, it would be appropriate to leave a Local Medication Route of ‘Intrathoracic’ or ‘Intrafollicular’ unmapped. If any drugs are being ordered using that particular Local Medication Route, and you feel that it should be added to the Standard Medication Route file, please submit your request at the following website: <span class="mark">REDACTED</span>.

> Some auto population will be performed during the post-init of the Pre-Release patch installation. The software will attempt to map a Local Medication Route that is marked for ‘All Packages’ to a Standard Medication Route based on developed business rules. Sites need to review this auto mapping for accuracy.

> Appendix A provides a list of all Standard Medication Routes and corresponding FDB Route mapping initially released with the Pre-Release patch. Since then there have been additions pushed out by the New Term Rapid Turnaround (NTRT) process. For a complete listing use FileMan to print the NAME field (#.01) and FIRST DATABANK MED ROUTE field (#1) from the STANDARD MEDICATION ROUTES file (#51.23).

> Example:

> ![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/002.png)

> The software will look at the Local Medication Route that is in the medication order and find the Standard Medication Route that it is mapped to. It will then look in the STANDARD MEDICATION ROUTES file (#51.23) to locate the equivalent FDB Route to send to the interface.

> If no mapping to a Standard Medication Route is found, no dosage checks will be performed, the user will see a message informing them and a reason why.

> ![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/003.png) There is no current functionality to allow the inactivation of a Local Medication Route. If you do not want a Local Medication Route to be selectable for order entry, mark the PACKAGE USE field for ’National Drug File Only’. No further action is needed. This will also make it ineligible for mapping. You do NOT need to delete the Local Medication Route if associated with a dosage form from the DOSAGE FORM file (#50.606).          

2.  Local Possible Dosage Setup

> In order to perform a dosage check, a Dose Unit and Numeric Dose are required. The software can take a Possible Dosage and break it down to a Numeric Dose and Dose Unit; however it cannot do the same for a Local Possible Dosage because it is a free text entry. Two new fields, NUMERIC DOSE (#5) and DOSE UNIT (#4) have been created in the LOCAL POSSIBLE DOSAGE multiple (#50.0904) of the DRUG file (#50). Sites will have to review all their Local Possible Dosages and populate the Dose Unit and corresponding Numeric Dose fields.

> A new DOSE UNITS file (#51.24) was created in VistA to accomplish the mapping to FDB. All entries in this file have been mapped to an FDB Dose Unit. Although this file has not yet been standardized by STS, no local editing will be allowed. When populating the Dose Unit field for a Local Possible Dosage, selection will be from this new file.

> A new field, EXCLUDE FROM DOSAGE CHECKS (#11), was created in the DOSAGE FORM file (#50.606) to allow a dosage form to be excluded from dosage checks. Dosage checks will not be performed on a drug that is associated with a dosage form excluded from dosage checks. A list of Dosage Forms to be excluded has been determined and a listing is provided in Appendix C. In some cases all VA products associated with a dosage form did not belong to the ‘exclude’ or ‘not exclude’ category. In order to deal with these exceptions, the National Drug File patch (PSN\*4\*169) which is required for the Pre-Release patch will create a new field, OVERRIDE DF DOSE CHK EXCLUSION (#31), in the VA PRODUCT file (#50.68) to allow overriding of this dosage form exclusion for a VA Product. For example, if the dosage form is set to be excluded from dosage checks and the override field in the VA PRODUCT file is set to ‘Yes’, a dosage check will be performed on a dispense drug that is matched to this VA Product. If data is missing in either the EXCLUDE FROM DOSAGE CHECKS field in the DOSAGE FORM file or the OVERRIDE DF DOSE CHK EXCLUSION field in the VA PRODUCT file, dosage checks will be performed. An initial list of VA Products that have the new OVERRIDE DF DOSE CHK EXCLUSION field (#31) set to ‘Yes’ is provided in Appendix D.

> Below is a table to describe how the values of the two new fields determine whether dosage checks will be performed on a drug.

> The null values represent fields with missing data.

| Dosage Form Field – Exclude from Dosage Checks | VA Product Field – OVERRIDE DF DOSE CHK EXCLUSION | Dosage Check Performed? (Y/N) |
|----------------------------------------------------|-------------------------------------------------------|-----------------------------------|
| Yes                                                | No                                                    | No                                |
| Yes                                                | Yes                                                   | Yes                               |
| No                                                 | No                                                    | Yes                               |
| No                                                 | Yes                                                   | No                                |
| Null                                               | No                                                    | Yes                               |
| Null                                               | Yes                                                   | Yes                               |
| Yes                                                | Null                                                  | Yes                               |
| No                                                 | Null                                                  | Yes                               |
| Null                                               | Null                                                  | Yes                               |

> Some auto population will be performed during the post-init of the Pre-Release patch installation. The software will attempt to populate the Numeric Dose and Dose Unit fields for Local Possible Dosages that are defined for drugs eligible for dosing checks based on developed business rules. Sites need to review this auto population for accuracy. Drugs that are NOT eligible for dosing checks are:

1)  Inactive
2)  Not Matched to NDF
3)  Associated with a dosage form that is excluded from dosage checks and matched to a VA Product that has the OVERRIDE DF DOSE CHK EXCLUSION field (#31) set to ‘No’.
4)  Marked as a supply item ( ‘S’ in DEA, SPECIAL HDLG field or assigned a VA Drug Class starting with an ‘XA’)
5)  Associated with a dosage form that is NOT excluded from dosage checks, but is matched to a VA Product that has the OVERRIDE DF DOSE CHK EXCLUSION field set to ‘Yes’.

Appendix B provides a list of all Dose Units and corresponding FDB Dose Unit mapping. If a Dose Unit is not available for selection, an option to request a new Dose Unit or change an existing one is provided. VistA VA Products have been mapped to FDB drugs using the GCNSEQNO. The GCNSEQNO is an FDB drug identifier. It represents a generic formulation. It is specific to the generic ingredient(s), route of administration, dosage form, and strength. The Formulation ID (GCN), in some cases, may have the same value for different dosage forms, strengths, or non-active ingredient list differences and therefore may be linked to more than one GCNSEQNO. But a GCNSEQNO is unique in its association with each combination of factors. The GCNSEQNO is found for most Products in the VA PRODUCT file (#50.68) and is currently used to map a Product to a Patient Medication Instruction Sheet (PMIS) that is obtained from First DataBank (FDB).

  
Example 1:

![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/004.png)

In this example, we identify the drug Timolol Maleate 0.5% Oph Soln to the FDB database by passing in the GCNSEQNO found for the VA product that the drug Timolol Maleate 0.5% Oph Soln is matched to. For the Local Possible Dosage of ‘2 DROPS’ we have selected DROP(S) from the DOSE UNITS file as the Dose Unit and entered a ‘2’ for the corresponding Numeric Dose which will be sent to the interface. The corresponding FDB Dose Unit ‘DROP(S)’ will be sent to the interface.

Example 2:

![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/005.png)

In this second example, for a combination product, Amlodipine Besylate 10mg/Benazapril 40mg cap the GCNSEQNO that is sent to the interface identifies the drug and strength. So when we send ‘2’ for the Numeric Dose and CAPSULE(S) for the Dose Unit to the interface, it is understood what ‘2 CAPSULE(S)’ represents.

  
Example 3:

![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/006.png)

An example of how a dosage check will be done on a Possible Dosage is given here. If a Possible Dosage of ‘81MG’ is ordered, the software will use the unit identified in the DRUG file and do a look up in the DOSE UNITS File on the name and synonym fields. Once a match is found, we will take the corresponding FDB Dose Unit and send that to the interface. The Numeric Dose sent to the interface will be calculated by multiplying the Dispense Units per Dose by the Strength specified in the Drug File. The drug will be identified by the GCNSEQNO of the VA Product that it is matched to.

  
Example 4:

![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/007.png)

In some cases, more than one Dose Unit can be specified for a Local Possible Dosage. Let’s look at the first Local Possible Dosage defined, ‘ONE TEASPOONFUL’. In this case we could select a ‘TEASPOONFUL(S)’ or ‘MILLIGRAM(S)’ as a Dose Unit. Either would be acceptable, as long as the Numeric Dose is entered correctly for that Dose Unit. In the example above we chose ‘MILLIGRAM(S)’ for the Dose Unit with a corresponding Numeric Dose of ‘160’. For the second Local Possible Dosage defined, ‘ONE TABLESPOONFUL’, we could select ‘TABLESPOONFUL(S)’ or ‘MILLIGRAM(S)’. In this case, we selected ‘TABLESPOONFUL(S)’ for the Dose Unit and assigned ‘1’ as the Numeric Dose. For the second Local Possible Dosage, since ‘TABLESPOONFUL(S)’ was selected, the GCNSEQNO will identify the drug and strength within the FDB database, in order to be able to evaluate the dosage prescribed. For the first Local Possible Dosage, since ‘MILLIGRAM(S)’ was selected, the GCNSEQNO is needed to identify the drug, but not the strength.

Whatever Dose Unit is selected, should a message be returned indicating a problem with the dosage after the dosing check is performed; the message will contain the Dose Unit sent into the interface. For example, if there was a problem with the dosages above, see the messages that would have been returned and displayed to the clinician:

For 160 MILLIGRAMS:

Single dose amount of XX MILLIGRAMS exceeds the maximum single dose amount of

XXX MILLIGRAMS.

Total dose amount of XX MILLIGRAMS/DAY exceeds the dosing range of

XXX MILLIGRAMS/DAY to XXX MILLIGRAMS/DAY.

For 1 TABLESPOONFULS:

Single dose form amount of XX TABLESPOONFULS exceeds the maximum single dose

form amount of XXX TABLESPOONFULS.

Total dose form amount of XX TABLESPOONFULS/DAY exceeds the dosing range of

XXX TABLESPOONFULS/DAY to XXX TABLESPOONFULS/DAY.

The messages using the MILLIGRAMS Dose Unit may be more meaningful to the clinician vs. the TABLESPOONFULS Dose Unit.

  
Example 5:

![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/008.png)

In the final example above, if a strength mismatch exists between the strength in the DRUG file (#50) and the strength of the VA Product the drug is matched to; you need to be very careful when populating the Dose Unit and Numeric Dose fields. The Numeric Dose should reflect the strength that is defined for the drug in the DRUG file. Although for the Local Possible Dosage of ‘TWO TEASPOONFULS’ you can assign a Dose Unit of ‘TEASPOONFUL(S)’ or ‘MILLIGRAM(S)’, it is recommended that ‘MILLIGRAM(S)’ be selected with ‘240’ entered as the Numeric Dose in order to have the dosage check evaluated correctly. The reason for this is that the GCNSEQNO that is passed in for the VA Product that the dispense drug is matched to reflects a different strength. If we had assigned ‘TEASPOONFUL(S)’ as the Dose Unit with a corresponding Numeric Dose of ‘2’, the GCNSEQNO passed into the interface would identify the drug and strength as ACETAMINOPHEN 160MG/5ML ELIXIR and evaluate ‘2 TEASPOONFULS’ as ‘320MG’ instead of ‘240MG’.

3. Frequency Review

> In order to perform a daily dose range check on a prescribed medication, the software needs to determine how many times per day the single dosage is taken. The FREQUENCY (IN MINUTES) field in the Administration Schedule and Medication Instruction File will be used to determine a frequency. If a schedule entered for a medication order is not found in either the Administration Schedule (marked with prefix of ‘PSJ’) or Medication Instruction files, or is found in one of those two files but a frequency (in minutes) does not exist, a daily dose range check will not be performed. The user will be informed of this and a reason given as to why. A maximum single dose check will still be performed and general dosing information for the drug will be provided.

> If the TYPE OF SCHEDULE for an Administration Schedule within an order is designated as ONE-TIME or ON CALL; or if the Schedule Type for a Unit Dose order is ONE-TIME or ON CALL only a maximum single dose check will be performed on the order and a frequency is not needed.

> If the TYPE OF SCHEDULE for an Administration Schedule within an order is designated as DAY OF THE WEEK, the number of administration times will be used to determine the frequency in order to perform a daily dose range check. If none are defined, a frequency of ‘1’ will be assumed.

Example 1:

![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/009.png)

In the example above, the medication order specified the schedule of ‘BID’. The software will first look at the Administration Schedule file to see if the entry is there. In this case BID was found. The software will then check to see if there is a value in the frequency (in minutes) field. In this case a value of ‘720’ is present. The software will take the value ‘720’ and divide it into ‘1440’ which is the number of minutes for 24 hours to get the number of administrations per day. The result of ‘1440/720’ is ‘2’. ‘2’ will be sent to the interface for frequency.

Example 2:

![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/010.png)

In example 2, a schedule of ‘NOW’ was selected for an order. The TYPE OF SCHEDULE for this Administration Schedule has been designated as a ONE-TIME. In this case, it does not matter if there is a frequency defined. The software will not look at this field at all. If an order contains a schedule that is designated as a ONE-TIME or ON CALL in the type of schedule field or if a Unit Dose order has a ONE-TIME or ON CALL for the schedule type, the software will not be looking for a frequency. In these cases, the software will only perform a maximum single dose order check. A daily dose range check will not be performed. The frequency is needed for the daily dose range order check only.

Example 3:

![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/011.png)

In example 3, a schedule of ‘MO-WE-FR@09-17’ was selected for an order. The TYPE OF SCHEDULE for this Administration Schedule has been designated as a DAY OF THE WEEK. The software will determine the number of administration times defined for this schedule and that number will represent the frequency. In this example, two administration times of 09 and 17 have been defined for this DAY OF THE WEEK schedule. The frequency that will be sent to the interface is ‘2’.

4. Identify IV Solution PreMixes

A PreMix solution is an IV Solution that comes prepared from the manufacturer with additives. Some examples would be Heparin 25,000 units in 5% Dextrose 250ml or 5% Dextrose 0.45% Sodium Chloride with 20 MeQ Potassium Chloride 1000ml. Currently if such a drug is entered as an IV Solution for an IV order, it does not participate in order checks (i.e. drug-drug interactions, duplicate class, etc). If entered as an IV Additive it does. You can now enter these types of premixed drugs as IV Solutions and mark them as PreMixes and they will participate in order checks. Order checks will be performed on the dispense drug associated with the IV Solution.

If you have your PreMix solutions set up as IV Additives or set up as an IV Additive and IV Solution in order to participate in order checks, you do NOT have to make any changes if you do not wish to. They will continue to participate in order checks when PRE V. 0.5 is released.

However, if you want to enter your PreMixes as IV Solutions and mark them as PreMixes you have two options:

1)  Make your file changes AFTER PRE V. 0.5 is installed.
2)  Make your file changes NOW, but keep them inactivated. Once PRE V. 0.5 is installed, you can delete the inactivation date and inactivate the IV additives or IV Additive and IV solution entries that you are replacing.

Remember, these changes will only be recognized by PRE V. 0.5 software.5. Enter/Edit Additive Frequency for IV Additives

To facilitate accurate daily dose checking for a continuous IV Solution with IV Additives, the software must calculate the amount of an IV Additive that is administered to a patient over a 24 hour period of time. In order to capture that information at the time the provider enters the IV order through the CPRS Continuous IV Dialog, software changes were required. PSS\*1.0\*147 creates a new ADDITIVE FREQUENCY (#18) field in the IV ADDITIVES (#52.6) file to provide a default value for a new additive frequency field in CPRS when continuous IV orders with additives are entered. The provider will have three choices for selection; ‘1 Bag/day’, ‘All bags’, and ‘See Comments’. If the provider selects ‘See Comments’, the software will check to make sure instructions are entered in the Provider comments field.

When the pharmacist finishes the order, the value entered in the additive frequency for an IV Additive will be transferred to the IV Additive bottle field. A ‘1 Bag/day’ value will be represented as ‘1’; ‘All bags’ value will be represented as ‘All’ and ‘See Comments’ will be represented as ‘All’ with the understanding that the pharmacist will have to edit the bottle \# field based on the provider instructions entered in the Provider comments.

These defaults will not start to appear in CPRS until Pharmacy Re-Engineering (PRE) V. 0.5 software is installed. Data for the IV Additive file will be auto-populated by a Post-Install routine for patch PSS\*1\*147 based on defined business rules. The selection values for the additive frequency in the IV Additive file will be ‘1 Bag/day’, ‘All Bags’ or it can be left blank. The business rules for the auto population logic are as follows:

1.  If the dispense drug associated with the IV Additive has a VA Drug Class assigned and the VA Drug Class code contains a ‘VT’, the additive frequency will be set to ‘1 Bag/day’.
2.  If the dispense drug associated with the IV Additive has a VA Drug Class assigned and the VA Drug Class code does not contain a ‘VT’, the additive frequency will be set to ‘All bags’.
3.  If the dispense drug associated with the IV Additive does not a VA Drug Class assigned, the additive frequency will be left blank.

A new IV Additive Report \[PSS IV ADDITIVE REPORT\] option has also been added to allow review of the Additive Frequency data. Some guidance when reviewing the auto populated additive frequency:

1.  If an IV Additive (i.e. MVI Inj) is always administered once per day, a value of ‘1 Bag/day’ should be entered for the additive frequency.
2.  If an IV Additive (i.e. Antibiotic; or Drug administered continuously such as Dopamine, Dobutamine) will always be placed in all IV Bags for an IV order, a value of ‘All Bags’ should be entered for the additive frequency.
3.  If an IV Additive (i.e. Potassium Chloride) can be placed in all bags or sometimes in 1 or 2 bags for an IV order, leave the additive frequency blank.

This new field can be edited using the *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option or the *Additives File* \[PSSJI DRUG\] option.

Remember, changes to the CPRS software to display the Additive Frequency field with defaults from Pharmacy in the IV Dialog will only occur when the PRE V. 0.5 software is installed.

## Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When installation of PSS\*1\*129 is complete a Mailman message is sent to the patch installer and anyone else who has been added to receive the message during patch installation. Do not start manual mapping until confirmation has been received that the post-init is complete and this Mailman message has been received.

Subj: PSS\*1\*129 Installation Complete \[#43593\] 07/25/08@07:53 1 line

From: PSS\*1\*129 INSTALL In 'IN' basket. Page 1

-----------------------------------------------------------------------------

The Installation of patch PSS\*1.0\*129 is complete.

Enter message action (in IN basket): Ignore//

If you did not receive this Mailman message, contact your local IRM office. Possible causes for not receiving the message could be that the install is still running, you were not included as a recipient of the message or there is a problem and further investigation is required.

What follows is a summary of the steps that need to be completed within each functional area for the PRE V. 0.5 Pre-Release patch (PSS\*1\*129) and Pre-Release Enhancements patch (PSS\*1\*147). There is no specific order in which the functional areas need to be completed. The work must be completed in order for the new dosing checks implemented in PRE V.0.5 enhanced order check functionality to work. More detailed information on each option/report mentioned in each step is included later in the document.

### Local Medication Route Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 1: Using the *Medication Route Mapping Report* \[PSS MED ROUTE MAPPING REPORT\] option, print the report selecting “All Medication Routes.” It will provide a look at the auto mapping that was performed during the post-init when the Pre-Release patch was installed. Review your Local Medication Routes that were mapped to a Standard Medication Route for accuracy. It will also display Local Medication Routes marked for “All Packages’ that still require mapping to be performed. See Appendix A for a list of Standard Medication Routes that were released with the Pre-Release patch. Since then there have been additions pushed out by the New Term Rapid Turnaround (NTRT) process. For a complete listing, use FileMan to print the NAME field (#.01) and FIRST DATABANK MED ROUTE field (#1) from the STANDARD MEDICATION ROUTES file (#51.23).

See Appendix E for sample medication route mappings from test sites.

Step 2: After reviewing the report, you can begin mapping the rest of your unmapped Local Medication Routes. The *Find Unmapped Local Medication Routes* \[PSS MED ROUTES INITIAL MAPPING\] option will identify all Local Medication Routes that require mapping and present them one by one for mapping.

Step 3: If while mapping you discover that a Standard Medication Route is not available for use, request it to be added to the Standard Medication Route list at the following website: <span class="mark">REDACTED</span>. The request will be reviewed and acted upon. The requestor will be informed of the outcome.

Step 4: Upon completion of the mapping or any time you need to review your Local Medication Route mappings for accuracy and completeness, rerun the report in Step 1. You can print all medication routes marked for ‘All Packages’ that are mapped or unmapped or just those that remain unmapped.

Step 5: After reviewing, if changes need to be made the following options can also be used:

> *Map Local Medication Route to Standard* \[PSS MAP ONE MED ROUTE\] option – Allows the user to select a single medication route for quick mapping or remapping to a Standard Medication Route. No other medication route fields can be edited using this option.

> *Medication Route File Enter/Edit* \[PSS MEDICATION ROUTES EDIT\] option –Allows the user to select a single medication route for editing of all fields pertaining to that route, including the mapping/remapping to a Standard Medication Route. This is the only option from which you can delete the mapping to a Standard Medication Route.

Step 6: If it is necessary to track mapping changes, the *Medication Route Mapping History Report* \[PSS MED ROUTE MAPPING CHANGES\] option is available. This report can provide all mapping changes for all medication routes or for a single route over a specified timeframe.

> ![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/012.png) There  is no current functionality to allow the inactivation of a Local Medication Route. If you do not want a Local Medication Route to be selectable for order entry, mark the PACKAGE USE field for ’National Drug File Only’. No further action is needed. This will also make it ineligible for mapping. You do NOT need to delete the Local Medication Route if associated with a dosage form from the DOSAGE FORM file (#50.606).          

### ### Local Possible Dosage Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 1: Using the *Local Possible Dosages Report* \[PSS LOCAL POSSIBLE DOSAGES\] option, print the report selecting “All Local Possible Dosages’. It will provide a look at the auto population of the Numeric Dose and Dose Unit fields that was performed during the post-init when the Pre-Release patch was installed. Review your Local Possible Dosages that were populated for accuracy. It will also display Local Possible Dosages that still require population. See Appendix B for a list of Dose Units that you will be able to select from. An example of a Local Possible Dosage Report is provided in Appendix F.

Step 2: After reviewing the report, you can begin populating the Numeric Dose and Dose Unit fields for the rest of your eligible Local Possible Dosages. The *Find Unmapped Local Possible Dosages* \[PSS LOCAL DOSAGES EDIT ALL\] option will identify all Local Possible Dosages eligible for dosage checks that require population and present them one by one for processing.

Step 3: While populating the Numeric Dose and Dose Unit fields, if it is discovered that a Dose Unit needs to be changed or added to the DOSE UNITS file, use the *Request Change to Dose Unit* \[PSS DOSE UNIT REQUEST\] option to request it to be added to the DOSE UNITS file (#51.24). The request will be directed to the Outlook mail group <span class="mark">REDACTED</span>. The request will be reviewed and acted upon. The requestor will be informed of the outcome.

Step 4: Upon completion of the Local Possible Dosage population or at any time if you need to review your Local Possible Dosage population of the Numeric Dose and Dose Unit fields for accuracy and completeness, rerun the report in Step (1). You can print all Local Possible Dosages or those just missing data.

Step 5: After reviewing, if changes need to be made the following options can also be used;

> *Map Local Possible Dosages* \[PSS LOCAL DOSAGES EDIT\] option – Allows the user to select a single drug and add/edit values for the Numeric Dose and Dose Unit fields for its Local Possible Dosages. No other data can be modified using this option.

> *Enter/Edit Dosages* \[PSS EDIT DOSAGES\] option – Allows the user to edit all dosage related fields for a single drug. The Numeric Dose and Dose Unit fields have been added.

> *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option – Allows user to add/edit all drug related fields for a single drug. This option was modified to allow editing of the Numeric Dose and Dose Unit fields.

In addition to drugs that are eligible for Dosage Checks, all three options above will allow a user to enter values in the Numeric Dose and Dose Unit fields for a Local Possible Dosage defined for an inactive drug or one that has not been matched to NDF.

Step 6: Two other reports that are available:

> *Strength Mismatch Report* \[PSS STRENGTH MISMATCH\] option – This report will print Dosage information for all entries in the DRUG file (#50) that have a different Strength than what is in the VA Product file (#50.68) match. This report can only identify strength mismatches if the drug qualifies for Possible Dosages, and a strength has been defined in the DRUG file (#50).

> *Review Dosages Report* \[PSS DOSAGE REVIEW REPORT\] option – The Numeric Dose and Dose Unit fields were added to display on this existing report.

### Frequency Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 1: Use the *Administration Schedule File Report* \[PSS SCHEDULE REPORT\] option to review that all appropriate administration schedules have the FREQUENCY (IN MINUTES) field defined. This report allows you to print all administration schedules or just those without a frequency defined.

Step 2: Use the *Standard Schedule Edit* \[PSS SCHEDULE EDIT\] option to add/modify data in the FREQUENCY (IN MINUTES) field.

Step 3: The *Administration Schedule File Report* \[PSS SCHEDULE REPORT\] option can be rerun as many times as needed.

Step 4: Use the *Medication Instruction File Report* \[PSS MED INSTRUCTION REPORT\] option to review that all appropriate medication instructions have the FREQUENCY (IN MINUTES) field defined. This report allows you to print all medication instructions or just those without a frequency defined.

Step 5: Use the *Medication Instruction File Add/Edit* \[PSSJU MI\] option to add/modify data in the FREQUENCY (IN MINUTES) field.

Step 6: The *Medication Instruction File Report* \[PSS MED INSTRUCTION REPORT\] option can be rerun as many times as needed.

### Identify IV Solution PreMixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 1: Use the *IV Solution Report* \[PSS IV SOLUTION REPORT\] option to review all your IV Solutions and identify the ones that are PreMixes. Initially when printing this report select to print “All IV Solutions’. This report allows one to also just print those IV Solutions marked as PreMixes.

Step 2: Use the *Mark PreMix Solutions* \[PSS MARK PREMIX SOLUTIONS\] option to mark an IV Solution as a PreMix. Other fields may also be edited using this option.

Step 3: The *IV Solution Report* \[PSS IV SOLUTION REPORT\] option can be rerun as many times as needed.

Step4: The following options have been modified to allow a user to mark an IV Solution as a PreMix:

> Drug Enter/ Edit \[PSS DRUG ENTER/EDIT\] option – Allows user to add/edit all drug related fields for a single drug.

> *Primary Solution File (IV)* \[PSSJI SOLN\] Stand alone option – Allows user to add/edit all IV Solution related fields.

### Enter/Edit Additive Frequency for IV Additives

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 1: Using the *IV Additive Report \[PSS IV ADDITIVE REPORT\]* option, print the report selecting “Print all IV Additives.” It will provide a look at the auto mapping that was performed during the post-init when the PSS\*1.0\*147 patch was installed. Review the Additive Frequency data for accuracy. This report allows one to also just print those IV Additives that have no value in the Additive Frequency field or those IV Additives that have a value of '1 BAG/DAY' in the Additive Frequency field.

Step 2: The following options have been modified to allow a user to edit the Additive Frequency field:

> Drug Enter/ Edit \[PSS DRUG ENTER/EDIT\] option – Allows user to add/edit all drug related fields for a single drug.

> Additives File \[PSSJI DRUG\] Stand alone option – Allows user to add/edit all IV Additive related fields.

Step 3: The *IV Additive Report* \[PSS IV ADDITIVE REPORT\] option can be rerun as many times as needed.

  
<span id="_Toc213747215" class="anchor"></span>Chapter 1 – Local Medication Route Mapping

In order to perform a dosage check, the medication route by which a medication is given must be taken into account. Since the First DataBank (FDB) database is utilized to perform the dosage checks, we need to map our Local Medication Routes in VistA to an FDB Route. A new STANDARD MEDICATION ROUTES file (#51.23) was created in VistA to accomplish this. This file has been standardized by Standards and Terminology Service (STS) and mapped to an FDB Route. Options have been provided for sites to map each Local Medication Route that is marked for ‘All Packages’ to an active Standard Medication Route. Reports have also been provided to review the mappings. When dosage checks are performed, the software will use this mapping to pass the equivalent FDB Route for the Local Medication Route that was specified in the medication order for the drug to the interface. If the Local Medication Route is not mapped, dosage checks will not be performed. The user entering the order will be informed that the dosage check was not performed and the reason why. In this case, general dosing information cannot be provided to the user either. If a Local Medication Route cannot be mapped because a corresponding Standard Medication Route is not available, an option to request a new Standard Medication Route or change an existing one is provided.

Appendix E provides examples of Local Medication Route Mappings to a Standard.  When mapping, if it is not clear as to which Standard Medication Route one should map their Local Medication Route to, use the following guidelines:

1)  The first thing you should look at is the drugs being ordered with that Local Medication Route. By what route are they normally administered?   For example, a Local Medication Route of ‘Affected Area’ is usually used with topical drugs. The most appropriate Standard Route to map the Local Medication Route of ‘Affected Area’ would be ‘Topical’.
2)  If you have Local Medication Routes defined that are used when ordering supplies, map to the Standard Medication Route of ‘NOT APPLICABLE’.
3)  Local Medication Routes that are combinations, i.e. Intramuscularly or By Mouth should be mapped to the Standard Medication Route of ‘NOT APPLICABLE’.
4)  In some cases, you may not find the exact Local Medication Route term in the Standard Medication Route file to map to. However, there may be a Standard Medication Route that is comparable to map to that is named differently. For example, the Local Medication Route of ‘Percutaneous’ can be mapped to the Standard Medication Route of ‘Transdermal’ and a Local Medication Route of ‘Intra-Abdominal’ can be mapped to ‘Intraperitoneal’.
5)  In some cases, there will just be no appropriate Standard Medication Route to map to. In those cases, leave the Local Medication Route unmapped.  For example, it would be appropriate to leave a Local Medication Route of ‘Intrathoracic’ or ‘Intrafollicular’ unmapped. If any drugs are being ordered using that particular Local Medication Route, and you feel that it should be added to the Standard Medication Route file, please submit your request at the following website: <span class="mark">REDACTED</span>.

Some auto population will be performed during the post-init of the Pre-Release patch installation. The software will attempt to map a Local Medication Route that is marked for ‘All Packages’ to a Standard Medication Route based on developed business rules. Sites need to review this auto mapping for accuracy.

Appendix A provides a list of all Standard Medication Routes and corresponding FDB Route mapping initially released with the Pre-Release patch. Since then there have been additions pushed out by the New Term Rapid Turnaround (NTRT) process. For a complete listing use FileMan to print the NAME field (#.01) and FIRST DATABANK MED ROUTE field (#1) from the STANDARD MEDICATION ROUTES file (#51.23).

The bolded options below are created specifically for the Local Medication Route Mapping tasks.

Enhanced Order Checks Setup Menu:

Find Unmapped Local Medication RoutesMap Local Medication Route to StandardMedication Route Mapping ReportMedication Route File Enter/EditMedication Route Mapping History ReportRequest Change to Standard Medication Route

Find Unmapped Local Possible Dosages

Map Local Possible Dosages

Local Possible Dosages Report

Strength Mismatch Report

Enter/Edit Dosages

Request Change to Dose Unit

Mark PreMix Solutions

IV Solution Report

Administration Schedule File Report

Medication Instruction File Report

The detailed descriptions of the options that follow are presented in the logical sequence to accomplish the file setup, not the order in which they are displayed on the menu.

## Medication Route Mapping Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS MED ROUTE MAPPING REPORT\]

The *Medication Route Mapping Report* \[PSS MED ROUTE MAPPING REPORT\] option displays the mapping between the Local Medication Route, the Standard Medication Route and the FDB Route.

You can choose to display all Local Medication Routes that are marked for ‘All Packages’ (that are mapped or unmapped) or unmapped Local Medication Routes (that are marked for ‘All Packages’). The report will list alphabetically only those Local Medication Routes that are marked for ‘All packages’.

- Report formatted for 132 column width
- Displays the Local Medication Route, the Standard Medication Route, the FDB Route and the outpatient expansion associated with the Local Medication Route
- Displays totals at the end of the report for the number of all Local Medication Routes (marked for ‘All Packages’) and the number of unmapped Local Medication Routes if the user chooses to display all Local Medication Routes. If only unmapped Local Medication Routes are chosen, only the total for the number of unmapped entries will be displayed
- Output can be sent to a printer or screen

User selects all Local Medication Routes

> Medication Route Mapping Report

> This report will print Medication Route mapping information for Medication

> Routes marked for All Packages in the PACKAGE USE (#3) Field of the MEDICATION

> ROUTES (#51.2) File.

> Select one of the following:

> A ALL MEDICATION ROUTES

> O ONLY UNMAPPED MEDICATION ROUTES

> Enter 'A' for All Routes, 'O' for Only Unmapped Routes: O// ALL MEDICATION ROUTES

> This report is designed for 132 column format!

> DEVICE: HOME// \<ENTER\>

> MEDICATION ROUTES MAPPING REPORT Page: 1

> MEDICATION ROUTES (File 51.2) STANDARD ROUTE FDB ROUTE

> OUTPATIENT EXPANSION

> --------------------------------------------------------------------------------------

> BY MOUTH ORAL ORAL

> DENTAL DENTAL DENTAL

> EPIDURAL EPIDURAL EPIDURAL

> INTRA-URETHRAL URETHRAL INTRA-URETHRAL

> ORAL

> BY MOUTH

> MEDICATION ROUTES MAPPING REPORT Page: 2

> MEDICATION ROUTES (File 51.2) STANDARD ROUTE FDB ROUTE

> OUTPATIENT EXPANSION

> --------------------------------------------------------------------------------------

> TOTAL LOCAL MEDICATION ROUTES = 5

> TOTAL UNMAPPED LOCAL MEDICATION ROUTES = 1

> End of Report.

  
User selects only unmapped Local Medication Routes

> Medication Route Mapping Report

> This report will print Medication Route mapping information for Medication

> Routes marked for All Packages in the PACKAGE USE (#3) Field of the MEDICATION

> ROUTES (#51.2) File.

> Select one of the following:

> A ALL MEDICATION ROUTES

> O ONLY UNMAPPED MEDICATION ROUTES

> Enter 'A' for All Routes, 'O' for Only Unmapped Routes: O// \<ENTER\> NLY UNMAPPED MEDICAT

> ION ROUTES

> This report is designed for 132 column format!

> DEVICE: HOME// \<ENTER\>

> MEDICATION ROUTES

> MAPPING EXCEPTION REPORT Page: 1

> MEDICATION ROUTES (File 51.2)

> OUTPATIENT EXPANSION

> --------------------------------------------------------------------------------------

> BOTH EYES

> THIS IS A TEST

> G TUBE

> ORAL (BY MOUTH)

> BY MOUTH

> SUBCUTANEOUS

> MEDICATION ROUTES MAPPING EXCEPTION REPORT Page: 2

> MEDICATION ROUTES (File 51.2)

> OUTPATIENT EXPANSION

> --------------------------------------------------------------------------------------

> TOTAL UNMAPPED MEDICATION ROUTES = 4

> End of Report.

## Find Unmapped Local Medication Routes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS MED ROUTES INITIAL MAPPING\]

The *Find Unmapped Local Medication Routes* \[PSS MED ROUTES INITIAL MAPPING\] option identifies all medication routes in the MEDICATION ROUTES file (#51.2) that are marked for ‘All Packages’ but are not mapped to an active Standard Medication Route.

Every time an unmapped Local Medication Route is identified, it will be displayed and the user asked to select a Standard Medication Route to map it to.

Once a Standard Medication Route is selected, the First DataBank (FDB) route that the Standard Medication Route is mapped to will display.

If no selection for mapping is made, the next unmapped Local Medication Route will be displayed.

If the user enters an up-arrow (^) at the ‘Select STANDARD MEDICATION ROUTES NAME’ prompt, the system will ask if they want to continue. If the response is ‘Yes’, the system will display the next unmapped Local Medication Route. If the response is ‘No’, the system will check whether all Local Medication Routes have been mapped. If some are still unmapped, a message to that effect will display and the user referred to the *Medication Route Mapping Report* for details. If all Local Medication Routes have been mapped, a message to that effect will display.

Up-Arrow (^) exit with Remaining Unmapped Local Med Routes

> Select Enhanced Order Checks Setup Menu Option: Find Unmapped Local Medication Routes

> This option will find local Medication Routes marked for 'All Packages' not

> mapped to a Standard Medication Route, and prompt you to map the local route.

> This mapping is necessary to perform Dosage checks.

> Searching for unmapped Med Routes...

> Mapping local Med Route of 'INTRATHORACIC'

> Select STANDARD MEDICATION ROUTES NAME: \<ENTER\>

> Mapping local Med Route of 'ORAL SUBLINGUAL'

> Select STANDARD MEDICATION ROUTES NAME: ^

> Do you want to continue mapping Med Routes? Y// \<ENTER\> ES

> Mapping local Med Route of 'RETROBULBAR'

> Select STANDARD MEDICATION ROUTES NAME: ^

> Do you want to continue mapping Med Routes? Y// NO

> Checking for any remaining unmapped Local Med Routes...

> There are still local Med Routes marked for 'All Packages' not yet mapped,

> see the 'Medication Route Mapping Report' option for more details.

> Press Return to continue:

  
All Local Med Routes Mapped

> Select Enhanced Order Checks Setup Menu Option: Find Unmapped Local Medication Routes

> This option will find local Medication Routes marked for 'All Packages' not

> mapped to a Standard Medication Route, and prompt you to map the local route.

> This mapping is necessary to perform Dosage checks.

> Searching for unmapped Med Routes...

> Mapping local Med Route of 'G TUBE'

> Select STANDARD MEDICATION ROUTES NAME: ENTERAL FDB Route: ORAL

> Local Route: 'G TUBE' has been mapped to

> Stnd Route: 'ENTERAL' FDB Route: 'ORAL'

> Mapping local Med Route of 'SUBCUTANEOUS'

> Select STANDARD MEDICATION ROUTES NAME: SUBCUTANEOUS FDB Route: SUBCUTANEOUS

> Local Route: 'SUBCUTANEOUS' has been mapped to

> Stnd Route: 'SUBCUTANEOUS' FDB Route: 'SUBCUTANEOUS'

> Checking for any remaining unmapped Local Med Routes...

> All Local Med Routes are mapped!

## Request Change to Standard Medication Route

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS MEDICATION ROUTE REQUEST\]

The *Request Change to Standard Medication Route* \[PSS MEDICATION ROUTE REQUEST\] option is provided to direct users to a website to request additions or changes to the Standard Medication Routes file. The website is: <span class="mark">REDACTED</span>.

> Select Enhanced Order Checks Setup Menu Option: Request Change To Standard Medication Route

> Standard Medication Route requests must now be made at the following website:

> <span class="mark">REDACTED</span>

> Press Return to continue:

## Map Local Medication Route to Standard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS MAP ONE MED ROUTE\]

The *Map Local Medication Route to Standard* \[PSS MAP ONE MED ROUTE\] option allows quick mapping or remapping of a Local Medication Route to a Standard Medication Route. No other medication route fields can be edited using this option.

The user will only be able to select for mapping, Local Medication Routes that are marked for ‘All packages’ in the PACKAGE USE field (#3) in the MEDICATION ROUTES file (#51.2).

Upon selection of a Standard Medication Route, the system will display the FDB Route that the Standard Medication Route is mapped to. If the Local Medication Route selected has already been mapped, the mapping (Standard Medication Route and FDB Route) will be displayed and the user will be asked if they want to remap. If the response is ‘No’, the user will be asked to select another medication route. If the response is ‘Yes’, the user will be asked to select a new Standard Medication Route and the remapped entry will be redisplayed.

If a Standard Medication Route is not entered to map a Local Medication Route to, a warning message will be displayed which states that dosage checks will not be performed for medication orders containing this Local Medication Route.

If the user up-arrows out (^) at any point before completing the mapping, a warning message will display that dosage checks will not be performed for medication orders containing this Local Medication Route.

Mapping

> Select Enhanced Order Checks Setup Menu Option: Map Local Medication Route to Standard

> Select MEDICATION ROUTES NAME: OS LEFT EYE OS

> LEFT EYE

> Select STANDARD MEDICATION ROUTES NAME: ORAL FDB Route: ORAL

> Local Route: 'LEFT EYE' has been mapped to

> Stnd Route: 'ORAL' FDB Route: 'ORAL'

> Select MEDICATION ROUTES NAME:

Remapping

> Select Enhanced Order Checks Setup Menu Option: MAP LOCAL MEDication Route to

> Standard

> Select MEDICATION ROUTES NAME: LEFT EYE OS

> LEFT EYE

> Already mapped to:

> Stnd Route: 'ORAL' FDB Route: 'ORAL'

> Do you want to remap to a different Standard Med Route? N// YES

> Select STANDARD MEDICATION ROUTES NAME: OPHTHALMIC FDB Route: OPHTHALMIC

> Local Route: 'LEFT EYE' has been remapped to

> Stnd Route: 'OPHTHALMIC' FDB Route: 'OPHTHALMIC'

> Select MEDICATION ROUTES NAME:

No Mapping performed

> Map Local Medication Route to Standard

> Select MEDICATION ROUTES NAME: BY MOUTH

> BY MOUTH

> Select STANDARD MEDICATION ROUTES NAME: \<ENTER\>

> Nothing mapped - No dosing checks will be performed on orders containing this

> local medication route until it is mapped to a Standard Medication Route.

> Select MEDICATION ROUTES NAME: BY MOUTH

> BY MOUTH

> Select STANDARD MEDICATION ROUTES NAME: ^

> Nothing mapped - No dosing checks will be performed on orders containing this

> local medication route until it is mapped to a Standard Medication Route.

## Medication Route File Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS MEDICATION ROUTES EDIT\]

The *Medication Route File Enter/Edit* \[PSS MEDICATION ROUTES EDIT\] option has been modified to allow the user to map their Local Medication Route to an active Standard Medication Route. This is the only option that allows a Standard Medication Route mapping to be deleted.

The system will display the Standard Medication Routes name prompt for only those Local Medication Routes selected that are marked for ‘All Packages’ in the PACKAGE USE field (#3) in the MEDICATION ROUTES file (#51.2). If a Local Medication Route is selected that is marked for ‘National Drug File Only’, the user will not be asked to map to a Standard Medication Route.

Once a Standard Medication Route is selected, the FDB Route that the Standard Medication Route is mapped to will be displayed.

If the user selects a Local Medication Route that has already been mapped, the system will display the mapping (Standard Medication Route and FDB Route). The user will be given the opportunity to change the mapping. If the user chooses to remap, the new Standard Medication Route and corresponding FDB Route will be redisplayed.

If the user does not enter a Standard Medication Route to map their Local Medication Route to upon exiting the option, a warning message will be displayed that dosage checks will not be performed for medication orders containing this Local Medication Route.

If the user up-arrows out (^) at any point before completing the mapping, a warning message will display that dosage checks will not be performed for medication orders containing this Local Medication Route.

Mapping of Local Medication Route

> Select MEDICATION ROUTES NAME: DEEP IM

> NAME: DEEP IM// \<ENTER\>

> ABBREVIATION: \<ENTER\>

> PACKAGE USE: All Packages

> OUTPATIENT EXPANSION: THIS IS A TEST// \<ENTER\>

> OTHER LANGUAGE EXPANSION: \<ENTER\>

> IV FLAG: \<ENTER\>

> PROMPT FOR INJ. SITE IN BCMA: \<ENTER\>

> DSPLY ON IVP/IVPB TAB IN BCMA?: \<ENTER\>

> STANDARD MEDICATION ROUTE: INTRAMUSCULARINTRAMUSCULARLocal Medication Route marked for ‘National Drug File Only’

> Select MEDICATION ROUTES NAME: IMPLANT IMP

> NAME: IMPLANT// \<ENTER\>

> ABBREVIATION: IMP// \<ENTER\>

> PACKAGE USE: NATIONAL DRUG FILE ONLY// \<ENTER\>

> OUTPATIENT EXPANSION: \<ENTER\>

> OTHER LANGUAGE EXPANSION: \<ENTER\>

> IV FLAG: \<ENTER\>

> PROMPT FOR INJ. SITE IN BCMA: \<ENTER\>

> DSPLY ON IVP/IVPB TAB IN BCMA?: \<ENTER\>

> Select MEDICATION ROUTES NAME:

Local Medication Route already mapped

> Select MEDICATION ROUTES NAME: BOTH EYES

> 1 BOTH EYES OU

> 2 BOTH EYES

> CHOOSE 1-2: 1 BOTH EYES OU

> NAME: BOTH EYES// \<ENTER\>

> ABBREVIATION: OU// \<ENTER\>

> PACKAGE USE: All Packages// \<ENTER\>

> OUTPATIENT EXPANSION: THIS IS A TEST// \<ENTER\>

> OTHER LANGUAGE EXPANSION: \<ENTER\>

> IV FLAG: \<ENTER\>

> PROMPT FOR INJ. SITE IN BCMA: \<ENTER\>

> DSPLY ON IVP/IVPB TAB IN BCMA?: \<ENTER\>

> Already mapped to:

> Stnd Route: 'ORAL' FDB Route: 'ORAL'

> Do you want to remap to a different Standard Med Route? N//

  
Local Medication Route remapped

> Select MEDICATION ROUTES NAME: BOTH EYES

> 1 BOTH EYES OU

> 2 BOTH EYES

> CHOOSE 1-2: 1 BOTH EYES OU

> NAME: BOTH EYES// \<ENTER\>

> ABBREVIATION: OU// \<ENTER\>

> PACKAGE USE: All Packages//\<ENTER\>

> OUTPATIENT EXPANSION: THIS IS A TEST// \<ENTER\>

> OTHER LANGUAGE EXPANSION: \<ENTER\>

> IV FLAG: \<ENTER\>

> PROMPT FOR INJ. SITE IN BCMA: \<ENTER\>

> DSPLY ON IVP/IVPB TAB IN BCMA?: \<ENTER\>

> Already mapped to:

> Stnd Route: 'ORAL' FDB Route: 'ORAL'

> Do you want to remap to a different Standard Med Route? N// YES

> STANDARD MEDICATION ROUTE: ORAL// OPHTHALMIC OPHTHALMIC

> Local Route: 'BOTH EYES' has been remapped to

> Stnd Route: 'OPHTHALMIC' FDB Route: 'OPHTHALMIC'

> Press Return to continue, '^' to exit:

Exiting Option without Mapping

> Select MEDICATION ROUTES NAME: DENTAL SUBCUTAN

> 1 DENTAL SUBCUTANEOUS DENTSC

> 2 DENTAL SUBCUTANEOUS INFILTRATION DENTSC IF

> CHOOSE 1-2: 1 DENTAL SUBCUTANEOUS DENTSC

> NAME: DENTAL SUBCUTANEOUS// \<ENTER\>

> ABBREVIATION: DENTSC// \<ENTER\>

> PACKAGE USE: ALL All Packages

> OUTPATIENT EXPANSION: \<ENTER\>

> OTHER LANGUAGE EXPANSION: \<ENTER\>

> IV FLAG: ^

> \*\*\* No dosing checks will be performed on orders containing this local

> medication route until it is mapped to a Standard Medication Route.\*\*\*

> Press Return to continue, '^' to exit: \<ENTER\>

> Select MEDICATION ROUTES NAME: DENTAL SUBCUTANEOUS DENTSC

> NAME: DENTAL SUBCUTANEOUS// \<ENTER\>

> ABBREVIATION: DENTSC// \<ENTER\>

> PACKAGE USE: All Packages// \<ENTER\>

> OUTPATIENT EXPANSION: \<ENTER\>

> OTHER LANGUAGE EXPANSION: \<ENTER\>

> IV FLAG: \<ENTER\>

> PROMPT FOR INJ. SITE IN BCMA: \<ENTER\>

> DSPLY ON IVP/IVPB TAB IN BCMA?: \<ENTER\>

> STANDARD MEDICATION ROUTE: \<ENTER\>

> \*\*\* No dosing checks will be performed on orders containing this local

> medication route until it is mapped to a Standard Medication Route.\*\*\*

> Press Return to continue, '^' to exit:

## Medication Route Mapping History Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS MED ROUTE MAPPING CHANGES\]

The *Medication Route Mapping History Report* \[PSS MAP MED ROUTE MAPPING CHANGES\] option tracks all mapping changes between Local Medication Routes and Standard Medication Routes. The report can be run for a single medication route or for all medication routes over a specified time frame. If ’A All Med Routes’ is selected, the report will display only those Local Medication Routes with mapping changes.

User selects single medication route

> Select Enhanced Order Checks Setup Menu Option: Medication Route Mapping History Report

> This report displays changes made to the mapping of Medication Routes in the MEDICATION ROUTES (#51.2) File to Medication Routes in the STANDARD MEDICATION ROUTES (#51.23) File.

> Select one of the following:

> S Single Med Route

> A All Med Routes

> Print report for a Single Med Route, or All Med Routes: S// \<ENTER\> ingle Med Route

> Select Med Route: BOTH EYES

> 1 BOTH EYES OU

> 2 BOTH EYES

> CHOOSE 1-2: 1 BOTH EYES OU

> Beginning Date: T-30 (APR 28, 2008)

> Ending Date: T (MAY 28, 2008)

> DEVICE: HOME// \<ENTER\>

> Medication Route mapping changes for BOTH EYES

> made between APR 28, 2008 and MAY 28, 2008 PAGE: 1

> -----------------------------------------------------------------------------

> Medication Route: BOTH EYES

> Date/Time: MAY 28, 2008@09:57:58

> Edited By: PHARMACIST,ONE

> Old Value: ORAL

> New Value: OPHTHALMIC

> Medication Route: BOTH EYES

> Date/Time: MAY 28, 2008@12:12:59

> Edited By: PHARMACIST,ONE

> Old Value: OPHTHALMIC

> New Value: \<no new value\>

> End of Report.

  
User selects all medication routes

> Select Enhanced Order Checks Setup Menu Option: Medication Route Mapping History Report

> This report displays changes made to the mapping of Medication Routes in the

> MEDICATION ROUTES (#51.2) File to Medication Routes in the STANDARD MEDICATION ROUTES (#51.23) File.

> Select one of the following:

> S Single Med Route

> A All Med Routes

> Print report for a Single Med Route, or All Med Routes: S// All Med Routes

> Beginning Date: T-365 (JAN 10,2007)

> Ending Date: T (JAN 10,2008)

> DEVICE: HOME// \<ENTER\>

> Medication Route mapping changes for ALL Medication Routes Page: 1

> made between JAN 10,2007 and JAN 10,2008

> -----------------------------------------------------------------------

> Medication Route: BOTH EARS

> Date/time: JAN 9,2008@15:18

> Edited by: PHARMACIST,ONE

> Old Value: BUCCAL

> New Value: OTIC

> Medication Route: BOTH EYES

> Date/time: NOV 30,2007@13:01:20

> Edited by: PHARMACIST,TWO

> Old Value: DENTAL

> New Value: OPHTHALMIC

> Medication Route: INTRADERMAL

> Date/time: DEC 19,2007@14:43:49

> Edited by: AUTOMAPPED

> Old Value: \<no previous value\>

> New Value: INTRADERMAL

> Medication Route: INTRAMUSCULAR

> Date/time: JAN 9,2008@15:23:20

> Edited by: PHARMACIST,ONE

> Old Value: EPIDURAL

> New Value: \<no new value\>

> End Of Report

  
No mapping changes for selection of single medication route.

> This report displays changes made to the mapping of Medication Routes in the

> MEDICATION ROUTES (#51.2) File to Medication Routes in the STANDARD MEDICATION ROUTES (#51.23) File.

> Select one of the following:

> S Single Med Route

> A All Med Routes

> Print report for a Single Med Route, or All Med Routes: S// \<ENTER\> ingle Med Route

> Select Med Route: BOTH EYES

> 1 BOTH EYES OU

> 2 BOTH EYES

> CHOOSE 1-2: 1 BOTH EYES OU

> Beginning Date: T-30 (APR 28, 2008)

> Ending Date: T (MAY 28, 2008)

> DEVICE: HOME// \<ENTER\>

> Medication Route mapping changes for BOTH EYES

> made between APR 28, 2008 and MAY 28, 2008 PAGE: 1

> -----------------------------------------------------------------------------

> No mapping changes to report.

> No mapping changes for selection of all medication routes

> This report displays changes made to the mapping of Medication Routes in the

> MEDICATION ROUTES (#51.2) File to Medication Routes in the STANDARD MEDICATION ROUTES (#51.23) File.

> Select one of the following:

> S Single Med Route

> A All Med Routes

> Print report for a Single Med Route, or All Med Routes: S// All Med Routes

> Beginning Date: T-365 (JAN 10,2007)

> Ending Date: T (JAN 10,2008)

> DEVICE: HOME// \<ENTER\>

> Medication Route mapping changes for ALL Medication Routes Page: 1

> made between JAN 10,2007 and JAN 10,2008

> -----------------------------------------------------------------------------

> No mapping changes to report.

# Chapter 2 – Local Possible Dosage Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to perform a dosage check in PRE V. 0.5, a Numeric Dose and Dose Unit are required. The software can take a Possible Dosage and break it down to a Numeric Dose and Dose Unit; however it cannot do the same for a Local Possible Dosage because it is a free text entry. Two new fields, NUMERIC DOSE (#5) and DOSE UNIT (#4), have been created in the LOCAL POSSIBLE DOSAGES multiple of the DRUG File (#50). Sites will have to review all their Local Possible Dosages and populate the Dose Unit and corresponding Numeric Dose.

A new DOSE UNITS file was created to accomplish the mapping to FDB. All entries in this file have been mapped to an FDB Dose Unit. Appendix B provides a list of all Dose Units and corresponding FDB Dose Unit mapping. When populating the Dose Unit field for a Local Possible Dosage, selection will be from the new DOSE UNITS file. A Numeric Dose will have to be entered that corresponds to the Dose Unit selected.

A new field was created in the Dosage Form file to allow a dosage form to be excluded from dosage checks. Dosage checks will not be performed on a drug that is associated with a dosage form excluded from dosage checks. A list of Dosage forms to be excluded has been determined and a listing is provided in Appendix C. In some cases all VA products associated with a dosage form did not belong to the ‘exclude’ or ‘not exclude’ category. In order to deal with these exceptions, the National Drug File patch (PSN\*4\*169) which is required for the Pre-Release patch will create a new field in the VA PRODUCT file to allow overriding of this dosage form exclusion for a VA Product. For example, if the dosage form is set to be excluded from dosage checks and the override field in the VA Product file is set to ‘Yes’, a dosage check will be performed on a drug that is matched to this VA Product. If data is missing in either the EXCLUDE FROM DOSAGE CHECKS field in the DOSAGE FORM file or the OVERRIDE DF DOSE CHK EXCLUSION field in the VA PRODUCT file, dosage checks will be performed. An initial list of VA Products that have the new OVERRIDE DF DOSE CHK EXCLUSION field set to ‘Yes’ is provided in Appendix D.

Below is a table to describe how the values of the two new fields determine whether dosage checks will be performed on a drug. The null values represent fields with missing data.

| Dosage Form Field – Exclude from Dosage Checks | VA Product Field – OVERRIDE DF DOSE CHK EXCLUSION | Dosage Check Performed? (Y/N) |
|----------------------------------------------------|-------------------------------------------------------|-----------------------------------|
| Yes                                                | No                                                    | No                                |
| Yes                                                | Yes                                                   | Yes                               |
| No                                                 | No                                                    | Yes                               |
| No                                                 | Yes                                                   | No                                |
| Null                                               | No                                                    | Yes                               |
| Null                                               | Yes                                                   | Yes                               |
| Yes                                                | Null                                                  | Yes                               |
| No                                                 | Null                                                  | Yes                               |
| Null                                               | Null                                                  | Yes                               |

Some auto population was performed during the post init of the PDM Pre-Release patch installation. The software attempted to populate the Numeric Dose and Dose Unit fields for Local Possible Dosages that were defined for drugs eligible for dosage checks based on developed business rules. It is recommended that auto populated data be reviewed for accuracy. Drugs that are NOT eligible for dosage checks are:

1)  Inactive
2)  Not Matched to NDF
3)  Associated with a dosage form that is excluded from dosage checks and matched to a VA Product that has the OVERRIDE DF DOSE CHK EXCLUSION field set to ‘No’
4)  Marked as a supply item (‘S’ in DEA,SPECIAL HDLG field or assigned a VA Drug Class starting with an ‘XA’)
5)  Associated with a dosage form that is NOT excluded from dosage checks, but is matched to a VA Product that has the OVERRIDE DF DOSE CHK EXCLUSION field set to ‘Yes’

The highlighted options below are created specifically for population of the Dose Unit and Numeric Dose fields for a Local Possible Dosage.

> Enhanced Order Checks Setup Menu:

> Find Unmapped Local Medication Routes

> Map Local Medication Route to Standard

> Medication Route Mapping Report

> Medication Route File Enter/Edit

> Medication Route Mapping History Report

> Request Change to Standard Medication Route

> Find Unmapped Local Possible Dosages

> Map Local Possible Dosages

> Local Possible Dosages Report

> Strength Mismatch Report

> Enter/Edit Dosages

> Request Change to Dose Unit

> Mark PreMix Solutions

> IV Solution Report

> Administration Schedule File Report

> Medication Instruction File Report

These additional options may also be used for review and when populating the Dose Unit and Numeric Dose fields for a Local Possible Dosage:

> Review Dosages Report (under *Dosages* option \[PSS DOSAGES MANAGEMENT\])

> Drug Enter/Edit (under *Pharmacy Data Management Option* menu \[PSS MGR\])

The detailed descriptions of the options that follow are presented in the logical sequence to accomplish the file setup, not the order in which they are displayed on the menu.

## Local Possible Dosages Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS LOCAL POSSIBLE DOSAGES\]

The new *Local Possible Dosages Report* \[PSS LOCAL POSSIBLE DOSAGES\] option identifies drugs with Local Possible Dosages that have missing data in the Numeric Dose and Dose Unit fields. These two fields are needed for dosage checks.

This report can be printed for all drugs in the local drug file that have Local Possible Dosages defined or only the drugs that have Local Possible Dosages defined with missing data in either of the Numeric Dose and Dose Unit fields.

> **NOTE:** This report is written for a 132 column format.

Drugs that meet the following criteria will be screened out from this report.

- Inactive
- Not Matched to NDF
- Associated with dosage form that is excluded from dosage checks and matched to a VA Product that has the OVERRIDE DF DOSE CHK EXCLUSION field set to ‘No’
- Associated with dosage form that is NOT excluded from dosage checks, but is matched to a VA Product that has the OVERRIDE DF DOSE CHK EXCLUSION field set to ‘Yes’
- Drug is marked as a supply item (‘S’ in DEA, SPECIAL HDLG field or assigned a VA Drug Class starting with an ‘XA’)
- Drug does not have any Local Possible Dosages defined

The report displays the following data elements:

- Internal Entry Number (IEN) of drug in DRUG file (#50)
- Drug Name
- Strength
- Units
- Application Package Use
- Local Possible Dosage(s)
  - Local possible dosage
  - Numeric Dose
  - Units
  - Package
- Strength of NDF VA product match (if mismatch)
- VA Product matched to

If no missing data is found the report will display ‘No Local Possible Dosage missing data found.’

  
User selects Only Local Possible Dosage with Missing Data

> Select Enhanced Order Checks Setup Menu Option: LOCAL POssible Dosages Report

> This report will print Local Possible Dosage information only for Drugs for

> which Dosage Checks can be performed. Drugs that are inactive, marked and/or

> classed as supply items, not matched to NDF or excluded from dosage checks (due

> to dosage form or VA Product override) will not be included in this report.

> Users will be able to print Local Possible Dosage information for all eligible

> drugs or only for drugs with missing data in the Numeric Dose and Dose Unit

> fields. These two fields must be populated to perform Dosage Checks for a Local

> Possible Dosage selected when placing a Pharmacy order.

> Select one of the following:

> A ALL LOCAL POSSIBLE DOSAGES

> O ONLY LOCAL POSSIBLE DOSAGE WITH MISSING DATA

> Enter 'A' for All, 'O' for Only: O// \<ENTER\> NLY LOCAL POSSIBLE DOSAGE WITH MISSING DATA

> This report is designed for 132 column format!

> DEVICE: HOME// \<ENTER\>

> Local Possible Dosages Report (Missing Data Only) PAGE: 1

> ----------------------------------------------------------------------------------------- (811) GELUSIL TABLETS

> Strength: Units: Application Package: UOX

> Local Possible Dosages:

> 1 TABLET

> Numeric Dose: Dose Unit: Package: O

> 2 TABLET(S)

> Numeric Dose: Dose Unit: Package: O

> VA PRODUCT MATCH: AL OH 200MG/MG OH 200MG/SIMETHICONE 25MG TAB,CHEWABLE

> \(156\) GUAIFENESIN 50MG/5ML SYRUP

> Strength: 50 Units: MG/5ML Application Package: OUX

> Local Possible Dosages:

> 1 TEASPOONFUL

> Numeric Dose: Dose Unit: MILLIGRAM(S) Package: IO

> 2 TEASPOONFUL(S)

> Numeric Dose: Dose Unit: Package: IO

> Note: Strength 50 does not match NDF strength of 100.

> VA PRODUCT MATCH: GUAIFENESIN 100MG/5ML SYRUP

  
No Missing Data

> Select Enhanced Order Checks Setup Menu Option: LOCAL POssible Dosages Report

> This report will print Local Possible Dosage information only for Drugs for

> which Dosage Checks can be performed. Drugs that are inactive, marked and/or

> classed as supply items, not matched to NDF or excluded from dosage checks (due

> to dosage form or VA Product override) will not be included in this report.

> Users will be able to print Local Possible Dosage information for all eligible

> drugs or only for drugs with missing data in the Numeric Dose and Dose Unit

> fields. These two fields must be populated to perform Dosage Checks for a Local

> Possible Dosage selected when placing a Pharmacy order.

> Select one of the following:

> A ALL LOCAL POSSIBLE DOSAGES

> O ONLY LOCAL POSSIBLE DOSAGE WITH MISSING DATA

> Enter 'A' for All, 'O' for Only: O// \<ENTER\> NLY LOCAL POSSIBLE DOSAGE WITH MISSING DATA

> This report is designed for 132 column format!

> DEVICE: HOME// \<ENTER\>

> Local Possible Dosages Report (Missing Data Only) PAGE: 1

> -----------------------------------------------------------------------------------------

> No Local Possible Dosage missing data found.

User selects All Local Possible Dosages

> Select Enhanced Order Checks Setup Menu Option: LOCAL POssible Dosages Report

> This report will print Local Possible Dosage information only for Drugs for

> which Dosage Checks can be performed. Drugs that are inactive, marked and/or

> classed as supply items, not matched to NDF or excluded from dosage checks (due

> to dosage form or VA Product override) will not be included in this report.

> Users will be able to print Local Possible Dosage information for all eligible

> drugs or only for drugs with missing data in the Numeric Dose and Dose Unit

> fields. These two fields must be populated to perform Dosage Checks for a Local

> Possible Dosage selected when placing a Pharmacy order.

> Select one of the following:

> A ALL LOCAL POSSIBLE DOSAGES

> O ONLY LOCAL POSSIBLE DOSAGE WITH MISSING DATA

> Enter 'A' for All, 'O' for Only: O// ALL LOCAL POSSIBLE DOSAGES

> This report is designed for 132 column format!

> DEVICE: HOME// \<ENTER\>

> Local Possible Dosages Report (All) PAGE: 1

> -----------------------------------------------------------------------------------------

> \(811\) GELUSIL TABLETS

> Strength: Units: Application Package: UOX

> Local Possible Dosages:

> 1 TABLET

> Numeric Dose: Dose Unit: Package: O

> 2 TABLET(S)

> Numeric Dose: Dose Unit: Package: O

> VA PRODUCT MATCH: AL OH 200MG/MG OH 200MG/SIMETHICONE 25MG TAB,CHEWABLE

> \(156\) GUAIFENESIN 50MG/5ML SYRUP

> Strength: 50 Units: MG/5ML Application Package: OUX

> Local Possible Dosages:

> 1 TEASPOONFUL

> Numeric Dose: 50 Dose Unit: MILLIGRAM(S) Package: IO

> 2 TEASPOONFUL(S)

> Numeric Dose: Dose Unit: Package: IO

> Note: Strength 50 does not match NDF strength of 100.

> VA PRODUCT MATCH: GUAIFENESIN 100MG/5ML SYRUP

> \(2280\) IBUPROFEN 300MG TAB \*N/F\*

> Strength: 300 Units: MG Application Package: OX

> Local Possible Dosages:

> 3 TABLETS

> Numeric Dose: 900 Dose Unit: MILLIGRAM(S) Package: IO

> 4 TABLETS

> Numeric Dose: 1200 Dose Unit: MILLIGRAM(S) Package: IO

> \(1676\) TIMOLOL 0.25% OPTH SOL 10ML

> Strength: Units: Application Package: UOX

> Local Possible Dosages:

> 1 DROP

> Numeric Dose: Dose Unit: Package: IO

> 2 DROP(S)

> Numeric Dose: Dose Unit: Package: O

> 2 DROPS

> Numeric Dose: Dose Unit: Package: O

> VA PRODUCT MATCH: TIMOLOL MALEATE 0.25% SOLN,OPH

## Find Unmapped Local Possible Dosages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS LOCAL DOSAGES EDIT ALL\]

A new option called *Find Unmapped Local Possible Dosages* \[PSS LOCAL DOSAGES EDIT ALL\] is provided to identify all Local Possible Dosages that are eligible for dosage checks and do not have either the Numeric Dose or Dose Unit populated.

Drugs with the following criteria will be screened out from this option.

- Inactive
- Not Matched to NDF
- Associated with dosage form that is excluded from dosage checks and matched to a VA Product that has the OVERRIDE DF DOSE CHK EXCLUSION field set to ‘No’
- Associated with dosage form that is NOT excluded from dosage checks, but is matched to a VA Product that has the OVERRIDE DF DOSE CHK EXCLUSION field set to ‘Yes’
- Drug is marked as a supply item (‘S’ in DEA, SPECIAL HDLG field or assigned a VA Drug Class starting with an ‘XA’)
- Drug does not have any Local Possible Dosages defined

All identified drugs, along with their Local Possible Dosages will be presented to the user one by one for editing. If data exists in the strength and unit fields for the drug, it will be displayed following the drug name. The user will be notified if the strength defined for the drug does not match the strength of the VA Product that it is matched to. The strength and unit of the VA Product the drug is matched to will be displayed along with the strength in the DRUG file (#50).

Next, the first Local Possible Dosage defined for the selected drug will be displayed. The user will be prompted to enter a Dose Unit, followed by the Numeric Dose. The Dose Unit will be selectable from the new DOSE UNITS file (#51.24).

Any data entered will be redisplayed to the user (Local Possible Dosage, Dose Unit and Numeric Dose) before presenting the next Local Possible Dosage for editing, if one exists for the drug. All Local Possible Dosages defined for the drug with missing data in the Numeric Dose and Dose Unit fields will be presented for editing.

See example on next page.

Select Enhanced Order Checks Setup Menu Option: Find Unmapped Local Possible Dosages

This option will find all Local Possible Dosages that are eligible for Dosage

Checks that do not have either the Numeric Dosage or Dose Unit entered for the

Local Possible Dosage. This mapping is necessary to perform Dosage checks.

Searching for local Possible Dosages...

> Drug: ACETAMINOPHEN ELIX. 120MG/5ML 4OZ

> Strength from National Drug File match =\> 160 MG/5ML

> Strength currently in the Drug File =\> 120

> Please Note: Strength of drug does not match strength of VA Product it is

> matched to.

> TWO TEASPOONFULS

> Numeric Dose: Dose Unit: MILLIGRAM(S)

> DOSE UNIT: MILLIGRAM(S)// \<ENTER\>

> NUMERIC DOSE: 240

> TWO TEASPOONFULS

> Numeric Dose: 240 Dose Unit: MILLIGRAM(S)

> Drug: ACETAMINOPHEN 120MG/COD 12MG PER 5ML EL

> TWO TEASPOONFULS

> DOSE UNIT: TEASPOONFUL(S)

> NUMERIC DOSE: 2

> TWO TEASPOONFULS

> Numeric Dose: 2 Dose Unit: TEASPOONFUL(S)

> ONE TABLESPOONFUL

> DOSE UNIT: TABLESPOONFUL(S)

> NUMERIC DOSE: 1

> ONE TABLESPOONFUL

> Numeric Dose: 1 Dose Unit: TABLESPOONFUL(S)

> Drug: ALBUMIN 25% INJ BL500

> Strength: 25 Unit: %

> 50 ML

> DOSE UNIT: GRAM(S)

> NUMERIC DOSE: 12.5

> 50 ML

> Numeric Dose: 12.5 Dose Unit: GRAM(S)

> 100 ML

> DOSE UNIT: GRAM(S)

> NUMERIC DOSE: 25

> 100 ML

> Numeric Dose: 25 Dose Unit: GRAM(S)

> Drug: ALBUTEROL SO4 0.083% INHL 3ML RE102

> Strength: 0.083 Unit: %

> 1 AMPULE

> DOSE UNIT: MILLILITER(S)

> NUMERIC DOSE: 3

> 1 AMPULE

> Numeric Dose: 3 Dose Unit: MILLILITER(S)

> Drug: ALBUTEROL 90/IPRATROP 18MCG 200D PO INHL

> TWO PUFFS

> DOSE UNIT: INHALATION(S)

> NUMERIC DOSE: 2

> TWO PUFFS

> Numeric Dose: 2 Dose Unit: INHALATION(S)

> Drug: AMLODIPINE 10MG/VALSARTAN 320MG TAB

> 1 TABLET (10MG/320MG)

> DOSE UNIT: TABLET(S)

> NUMERIC DOSE: 1

> 1 TABLET (10MG/320MG)

> Numeric Dose: 1 Dose Unit: TABLET(S)

> Drug: CHLORAL HYD. SYR. 500MG/5ML (OZ)

> Strength: 500 Unit: MG/5ML

> 1 TEASPOONFUL

> DOSE UNIT: MILLIGRAM(S)

> NUMERIC DOSE: 500

> 1 TEASPOONFUL

> Numeric Dose: 500 Dose Unit: MILLIGRAM(S)

If a user presses the \<ENTER\> key at the ‘DOSE UNIT:’ prompt, they will be prompted to enter a Numeric Dose. If the user presses the \<ENTER\> key at the ‘NUMERIC DOSE:’ prompt, the next available Local Possible Dosage for that drug if one exists with missing data will be displayed. If no more Local Possible Dosages exist for the drug that require data population, the next drug and its Local Possible Dosages will be presented for editing.

If the user up-arrows (^) at the ‘DOSE UNIT:’ prompt, they will be asked if they want to continue. If the response is ‘Yes’, the next Local Possible Dosage with missing data for that drug will be displayed, if any exist. If no more Local Possible Dosages exist for the drug, the next drug will display. If the user responds ‘No’, the a check will be made to see if any Local Possible Dosages still require data to be entered and inform the user.

The user will be informed when all required data has been entered.

Select Enhanced Order Checks Setup Menu Option: Find Unmapped Local Possible Dosages

This option will find all Local Possible Dosages that are eligible for Dosage

Checks that do not have either the Numeric Dosage or Dose Unit entered for the

Local Possible Dosage. This mapping is necessary to perform Dosage checks.

Searching for local Possible Dosages...

> Drug: CHLORAMPHENICOL 0.5% OPTH SOL

> Strength: 0.5 Unit: %

> 1 DROP

> DOSE UNIT: \<ENTER\>

> NUMERIC DOSE: \<ENTER\>

> 2 DROP(S)

> DOSE UNIT: \<ENTER\>

> NUMERIC DOSE: \<ENTER\>

> Drug: CLOTRIMAZOLE ORAL TROCHES

> Strength: 10 Unit: MG

> 1 TROCHE

> DOSE UNIT: ^

> Do you want to continue mapping Local Possible Dosages? Y// \<ENTER\> ES

> 2 TROCHE(S)

> DOSE UNIT: ^

> Do you want to continue mapping Local Possible Dosages? Y// NO

> Checking for any remaining unmapped Local Possible Dosages...

> There are still Local Possible Dosages not yet mapped,

> see the 'Local Possible Dosages Report' option for more details.

> Press Return to Continue:

> OR

> All Local Possible Dosages are mapped!

## Request Change to Dose Unit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS DOSE UNIT REQUEST\]

The new *Request Change to Dose Unit* \[PSS DOSE UNIT REQUEST\] option is provided for users to request additions or changes to the DOSE UNITS file (#51.24). The request is directed to an Outlook mail group <span class="mark">REDACTED</span> that will review and act on the requests. A copy of the request is also sent to the user’s VistA email account. The following information about the request will be needed:

- Dose Unit to be added or modified (required)
- References or Reason for Request (required)

If the user is not ready to send the request, answering ‘No’ at the transmit prompt will send the request just to the user’s VistA email account. Once ready to send the request, if no changes are needed, the VistA email message can be retrieved and forwarded to the Outlook mail group <span class="mark">REDACTED</span> . If the VistA email message is no longer available for retrieval, the request must be reentered and transmitted.

> **NOTE:** The option will use whatever editor (line or screen) the user has defined for his or her “Preferred editor” in the NEW PERSON file (#200).

> Select Enhanced Order Checks Setup Menu Option: REQUEST CHANGE TO DOSE UNIT

> Select one of the following:

> N New Dose Unit

> C Change to Existing Dose Unit

> Request New Dose Unit or Change existing Dose Unit: N// \<ENTER\> ew Dose Unit

> Enter Dose Unit name: GRAIN(S)

> You must now enter a reason or references for this request.

> Press Return to continue, '^' to exit: \<ENTER\>

> ==\[ WRAP \]==\[ INSERT \]====\< References/Reason for Request \>==\[ \<PF1\>H=Help \]====

> Valid Dose Unit missing from file.

> \<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

> Do you want to save changes? y

> Transmit Dose Unit Request? Y// \<ENTER\> ES

> Mail message transmitted for review.

> Press Return to continue:

> Subj: Dose Unit Request \[#89442\] 05/28/08@12:51 4 lines

> From: PHARMACIST, ONE In 'IN' basket. Page 1

> -------------------------------------------------------------------------------

> Request New Dose Unit:

> GRAIN(S)

> Valid Dose Unit missing from file.

> Enter message action (in IN basket): Ignore// QD Query Detailed

> Subj: Dose Unit Request \[#89442\] 05/28/08@12:51 4 lines

> From: PHARMACIST, ONE In 'IN' basket.

> Local Message-ID: 89442@PEPCACHE.FO-BIRM.MED.VA.GOV (2 recipients)

> PHARMACIST, ONE Last read: 05/28/08@12:52 \[First read: 05/28/08@12:51\]

> <span class="mark">REDACTED</span> Sent: 05/28/08@12:51 Time: 1 second

> Message ID: 48343526<span class="mark">REDACTED</span>

> Enter message action (in IN basket): Ignore//

## Map Local Possible Dosages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS LOCAL DOSAGES EDIT\]

A new option called *Map Local Possible Dosages* \[PSS LOCAL DOSAGES EDIT\] is created to allow for entry of the Dose Unit and Numeric Dose fields for Local Possible Dosages defined for a drug.

The user will be asked to select a drug upon entering the option.

If a drug with no Local Possible Dosages is selected, the message ‘No local possible dosages exist for this drug’ will be displayed.

Select Enhanced Order Checks Setup Menu Option: Map Local Possible Dosages

Select Drug: VERAPAMIL 80MG TABS CV200

No local possible dosages exist for this drug.

Select Drug:

If the drug selected is associated with a dosage form that is excluded from dosage checks, and the VA Product that it is matched to has the OVERRIDE DF DOSE CHK EXCLUSION field set to ‘No’, the following message will be displayed. ‘The dosage form ‘XXX’ associated with this drug has been excluded from dosage checks. Population of the numeric dose and dose unit for this drug’s local possible dosages is not required.’

Select Enhanced Order Checks Setup Menu Option: Map Local Possible Dosages

Select Drug: HYDROCORTISONE 1% CREAM DE200

The dosage form 'CREAM,TOP' associated with the drug has been excluded from dosage checks. Population of the numeric dose and dose unit for this drug's local possible dosages is not required

Select Drug:

If the drug selected is associated with a dosage form that is NOT excluded from dosage checks and the VA Product that the drug is matched to has the OVERRIDE DF DOSE CHK EXCLUSION field set to ‘Yes’, the following message will be displayed. ‘The VA Product that this drug is matched to has been excluded from dosage checks. Population of the numeric dose and dose unit for this drug’s local possible dosages is not required..’

Select Enhanced Order Checks Setup Menu Option: Map Local Possible Dosages

Select Drug: THICK-IT POWDER TN200

The VA product that this drug is matched to has been excluded from dosage

checks. Population of the numeric dose and dose unit for this drug's local

possible dosages is not required.

Select Drug:

The following message is displayed if a supply item is selected: ‘This drug is marked as a supply and therefore excluded from dosing checks. Population of the numeric dose and dose unit for this drug’s local possible dosages is not required.’

Select Enhanced Order Checks Setup Menu Option: Map Local Possible Dosages

Select Drug: ABDOMINAL PAD 5 X 7

This drug is marked as a supply and therefore excluded from dosing checks.

Population of the numeric dose and dose unit for this drug's local possible

dosages is not required.

Select Drug:

If a drug is not matched to NDF a message will display indicating this.

If a drug is inactive, the inactivation date will be displayed upon drug selection. In either case, the user will be allowed to enter values in the Dose Unit and Numeric Dose fields, if they wish.

  
Not matched to NDF

Select Enhanced Order Checks Setup Menu Option: Map Local Possible Dosages

Select Drug: PROCHLORPERAZINE 25MG SUPPOS. GA605

This drug is not matched to NDF and therefore will be excluded from dosing

checks.

1 SUPPOSITORY(IES)

DOSE UNIT: SUPPOSITOR(IES)

NUMERIC DOSE: 1

1 SUPPOSITORY(IES)

Numeric Dose: 1 Dose Unit: SUPPOSITOR(IES)

Select Drug:

Inactive Drug

Select Drug: ACETAMINOPHEN 650MG SUPPOS. CN103 05-08-08

Strength: 650 Unit: MG

1 SUPPOSITORY(IES)

DOSE UNIT: SUPPOSITOR(IES)

NUMERIC DOSE: 1

1 SUPPOSITORY(IES)

Numeric Dose: 1 Dose Unit: SUPPOSITOR(IES)

2 SUPPOSITORY(IES)

DOSE UNIT: SUPPOSITOR(IES)

NUMERIC DOSE: 2

2 SUPPOSITORY(IES)

Numeric Dose: 2 Dose Unit: SUPPOSITOR(IES)

Select Drug:

Strength and unit values will display if defined for the drug. If the strength defined for the drug does not match the strength of the VA Product that it is matched to, the strength mismatch will be displayed to the user.

Next, the first Local Possible Dosage defined for the selected drug will display along with a prompt to enter a Dose Unit, followed by the Numeric Dose. Only active Dose Units will be available for selection.

Any data entered will be redisplayed (Local Possible Dosage, Dose Unit and Numeric Dose) followed by the next Local Possible Dosage, if one exists for the drug.

  
Strength Mismatch

Select Enhanced Order Checks Setup Menu Option: Map Local Possible Dosages

Select Drug: ACETAMINOPHEN ELIX. 120MG/5ML 4OZ CN103

Strength from National Drug File match =\> 160 MG/5ML

Strength currently in the Drug File =\> 120

Please Note: Strength of drug does not match strength of VA Product it is

matched to.

ONE TEASPOONFUL

DOSE UNIT: MILLIGRAM(S)

NUMERIC DOSE: 120

ONE TEASPOONFUL

Numeric Dose: 120 Dose Unit: MILLIGRAM(S)

ONE TABLESPOONFUL

DOSE UNIT: MILLIGRAM(S)

NUMERIC DOSE: 360

ONE TABLESPOONFUL

Numeric Dose: 360 Dose Unit: MILLIGRAM(S)

Select Drug:

Select Enhanced Order Checks Setup Menu Option: Map Local Possible Dosages

Select Drug: PILOCARPINE 3% OPTH SOL 15ML OP102

Strength: 3 Unit: %

1 DROP

DOSE UNIT: DROP(S)

NUMERIC DOSE: 1

1 DROP

Numeric Dose: 1 Dose Unit: DROP(S)

2 DROP(S)

DOSE UNIT: DROP(S)

NUMERIC DOSE: 2

2 DROP(S)

Numeric Dose: 2 Dose Unit: DROP(S)

Select Drug: LORAZEPAM 1MG TAB CN302

Strength: 1 Unit: MG

1-2 TABLETS

DOSE UNIT: MILLIGRAM(S)

NUMERIC DOSE: 2

1-2 TABLETS

Numeric Dose: 2 Dose Unit: MILLIGRAM(S)

Select Drug:

Any data already entered for a Local Possible Dosage will be displayed and each field presented for editing.

If any existing Local Possible Dosage data is modified, the Local Possible Dosage, Dose Unit and Numeric Dose will be redisplayed.

All Local Possible Dosages defined for a selected drug will be presented for editing.

No changes made

Select Drug: PILOCARPINE 3% OPTH SOL 15ML OP102

Strength: 3 Unit: %

1 DROP

Numeric Dose: 1 Dose Unit: DROP(S)

DOSE UNIT: DROP(S)// \<ENTER\>

NUMERIC DOSE: 1// \<ENTER\>

2 DROP(S)

Numeric Dose: 2 Dose Unit: DROP(S)

DOSE UNIT: DROP(S)// \<ENTER\>

NUMERIC DOSE: 2// \<ENTER\>

Select Drug:

Edit made

Select Enhanced Order Checks Setup Menu Option: Map Local Possible Dosages

Select Drug: TIMOLOL 0.25% OPTH SOL 10ML OP101

Strength: 0.25 Unit: %

1 DROP

Numeric Dose: 4 Dose Unit: MICROGRAM(S)

DOSE UNIT: MICROGRAM(S)// DROPS DROP(S)

NUMERIC DOSE: 4// 1

1 DROP

Numeric Dose: 1 Dose Unit: DROP(S)

2 DROP(S)

Numeric Dose: 2 Dose Unit: CENTIMETER(S)

DOSE UNIT: CENTIMETER(S)// DROPS DROP(S)

NUMERIC DOSE: 2// \<ENTER\>

2 DROP(S)

Numeric Dose: 2 Dose Unit: DROP(S)

Select Drug:

If the user presses the \<ENTER\> key at the ‘DOSE UNIT:’ prompt, they will be prompted to enter a Numeric Dose. If the user presses the \<ENTER\> key at the ‘NUMERIC DOSE:’ prompt, the next available Local Possible Dosage for that drug will display, if one exists. If no more Local Possible Dosages exist for the drug, the user will be prompted to select another drug.

If a user up-arrows (^) at the ‘DOSE UNIT:’ prompt, they will be asked if they want to exit the option. If the user takes the default of ‘Yes’, they will be exited out of the option. If the user responds ‘No’, the next Local Possible Dosage for that drug will display, if any exist. If no more Local Possible Dosages exist for the drug, the user will be asked to select another drug.

\<ENTER\> at DOSE UNIT prompt

Select Enhanced Order Checks Setup Menu Option: Map Local Possible Dosages

Select Drug: TIMOLOL 0.25% OPTH SOL 10ML OP101

Strength: 0.25 Unit: %

1 DROP

DOSE UNIT: \<ENTER\>

NUMERIC DOSE: \<ENTER\>

2 DROP(S)

DOSE UNIT: \<ENTER\>

NUMERIC DOSE: \<ENTER\>

2 DROPS

DOSE UNIT: \<ENTER\>

NUMERIC DOSE: \<ENTER\>

Select Drug:

Up-arrow (^) at DOSE UNIT prompt and ‘Yes’ at Exit Option prompt

Select Enhanced Order Checks Setup Menu Option: Map Local Possible Dosages

Select Drug: TIMOLOL 0.25% OPTH SOL 10ML OP101

Strength: 0.25 Unit: %

1 DROP

DOSE UNIT: ^

Do you want to exit this option? Y// y YES

Up-arrow (^)at DOSE UNIT prompt and ‘NO’ at Exit Option prompt

Select Drug: TIMOLOL 0.25% OPTH SOL 10ML OP101

Strength: 0.25 Unit: %

1 DROP

DOSE UNIT:

NUMERIC DOSE: ^

Do you want to exit this option? Y// n NO

2 DROP(S)

DOSE UNIT: ^

Do you want to exit this option? Y// n NO

2 DROPS

DOSE UNIT: ^

Do you want to exit this option? Y// n NO

Select Drug:

## Enter/Edit Dosages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS EDIT DOSAGES\]

The *Enter/Edit Dosages* \[PSS EDIT DOSAGES\] option is modified to allow entry/editing of the new Numeric Dose and Dose Unit fields defined for Local Possible Dosages.

If any of the following conditions can be determined at the time of entry, the Numeric Dose and Dose Unit fields for any defined Local Possible Dosage will not be presented for data entry.

- Drug associated with a dosage form that is excluded from dosage checks and the VA Product that the drug is matched to has the OVERRIDE DF DOSE CHK EXCLUSION field set to ‘No’
- Drug associated with a dosage form that is NOT excluded from dosage checks, but the VA Product that it is matched to has the OVERRIDE DF DOSE CHK EXCLUSION field set to ‘Yes’
- Drug is marked as a supply item (‘S’ in DEA, SPECIAL HDLG field or assigned a VA Drug Class starting with an ‘XA’).

A warning will be displayed if the DRUG file strength does not match the VA Product strength to which it is matched.

![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/013.png)Auto population of the Numeric Dose and Dose Unit fields for Local Possible Dosages of eligible drugs ONLY occurs during the post init of the Pre-Release patch installation.

Changes are shown in boxes

Drug Unmatched to NDF

Select Dosages Option: ENTER/Edit Dosages

Select Drug: PILOCARPINE

1 PILOCARPINE 0.25% OPTH SOL 15ML

2 PILOCARPINE 1% OPTH SOL 15ML OP102

3 PILOCARPINE 2% 2ML OP102

4 PILOCARPINE 2% OPTH SOL 15ML OP102

5 PILOCARPINE 3% OPTH SOL 15ML OP102

Press \<ENTER\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 PILOCARPINE 0.25% OPTH SOL 15ML

This entry is marked for the following PHARMACY packages:

Outpatient

Unit Dose

PILOCARPINE 0.25% OPTH SOL 15ML Inactive Date:

This drug has the following Local Possible Dosages:

ONE DROP(S) PACKAGE: IO

TWO DROP(S) PACKAGE:

Do you want to merge new Local Possible Dosages? Y// NO

Strength: Unit:

Select LOCAL POSSIBLE DOSAGE: ONE DROP(S) IO

LOCAL POSSIBLE DOSAGE: ONE DROP(S)// \<ENTER\>

OTHER LANGUAGE DOSAGE NAME: \<ENTER\>

PACKAGE: Both// \<ENTER\>

BCMA UNITS PER DOSE: \<ENTER\>

DOSE UNIT: DROP(S)

NUMERIC DOSE: 1

Strength: Unit:

Select LOCAL POSSIBLE DOSAGE:

Strength Mismatch

Select Dosages Option: Enter/Edit Dosages

Select Drug: ACETAMINO

1 ACETAMINOPHEN 1000MG TABLET CN100

2 ACETAMINOPHEN 325MG C.T. CN103 \*\* OK 90 DAY SUPPLY \*\*

3 ACETAMINOPHEN 325MG TABLET CN103 INFECTIOUS DISEASE

RESTRICTED TO

4 ACETAMINOPHEN 650MG SUPPOS. CN103

5 ACETAMINOPHEN AND CODEINE 30MG CN101

Press \<ENTER\> to see more, '^' to exit this list, OR

CHOOSE 1-5: \<ENTER\>

6 ACETAMINOPHEN ELIX. 120MG/5ML 4OZ CN103

7 ACETAMINOPHEN, CODEINE ELIXIR (OZ) CN101

8 ACETAMINOPHEN 325MG TAB ACETAMINPHEN 325MG CT CN103

CHOOSE 1-8: 6 ACETAMINOPHEN ELIX. 120MG/5ML 4OZ CN103

This entry is marked for the following PHARMACY packages:

Outpatient

Unit Dose

Non-VA Med

ACETAMINOPHEN ELIX. 120MG/5ML 4OZ Inactive Date:

Strength from National Drug File match =\> 160 MG/5ML

Strength currently in the Drug File =\> 120

Please Note: Strength of drug does not match strength of VA Product it is matched to.

> Press Return to Continue: \<ENTER\>

Edit Strength? N// \<ENTER\> O

Strength =\> 120 Unit =\>

Select DISPENSE UNITS PER DOSE: \<ENTER\>

Strength: 120 Unit: MG/5ML

Select LOCAL POSSIBLE DOSAGE: ?

You may enter a new LOCAL POSSIBLE DOSAGE, if you wish

Answer must be 1-60 characters in length.

Select LOCAL POSSIBLE DOSAGE: ONE TEASPOONFUL

Are you adding 'ONE TEASPOONFUL' as

a new LOCAL POSSIBLE DOSAGE (the 1ST for this DRUG)? No// Y (Yes)

LOCAL POSSIBLE DOSAGE: ONE TEASPOONFUL// \<ENTER\>

OTHER LANGUAGE DOSAGE NAME: \<ENTER\>

PACKAGE: O Outpatient

DOSE UNIT: MILLIGRAM(S)

NUMERIC DOSE: 120

Strength: 120 Unit: MG/5ML

Select LOCAL POSSIBLE DOSAGE: \<ENTER\>

Select Drug:

## Drug Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS DRUG ENTER/EDIT\]

The *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option is modified to allow editing of the two new Local Possible Dosage fields, Numeric Dose and Dose Unit, when matching/rematching to NDF or when entering a new drug without matching to the National Drug File (NDF).

If any of the following conditions can be determined at the time of entry, the Numeric Dose and Dose Unit fields for any defined Local Possible Dosage will not be presented for data entry.

- Drugs associated with a dosage form that is excluded from dosage checks and the VA Product it is matched to will have the OVERRIDE DF DOSE CHK EXCLUSION field (#31) ) in the VA PRODUCT file (#50.68) set to ‘No’
- Drug associated with a dosage form that is NOT excluded from dosage checks, but the VA Product that it is matched to will have the OVERRIDE DF DOSE CHK EXCLUSION field set to ‘Yes’
- Drug is marked as a supply item Drug is marked as a supply item (‘S’ in DEA, SPECIAL HDLG field or assigned a VA Drug Class starting with an ‘XA’).

A warning will be provided if the DRUG file strength does not match the VA Product strength to which it is matched.

![](pss-1-129-147-implementation-guide-pharmacy-reengineering-pre-v-0-5-pre-release/014.png) Auto population of the Numeric Dose and Dose Unit fields for Local Possible Dosages of eligible drugs ONLY occurs during the post init of the Pre-Release patch installation. If you choose to delete your Local Possible Dosages when remapping to NDF, then when redefining your Local Possible Dosages you will have to repopulate the Numeric Dose and Dose Unit fields along with all other Local Possible Dosage fields.

Changes are shown in boxes.

Rematching drug to NDF (no deletion of Local Possible Dosages)

Select Pharmacy Data Management Option: Drug Enter/Edit

Select DRUG GENERIC NAME: TIMOPTIC

Lookup: SYNONYM

1 TIMOPTIC 0.25% TIMOLOL 0.25% OPTH SOL 10ML OP101

2 TIMOPTIC 0.5% TIMOLOL 0.5% OPTH SOL 10ML OP101

CHOOSE 1-2: 2 TIMOLOL 0.5% OPTH SOL 10ML OP101

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This entry is marked for the following PHARMACY packages:

Outpatient

Unit Dose

Non-VA Med

GENERIC NAME: TIMOLOL 0.5% OPTH SOL 10ML Replace \<ENTER\>

VA CLASSIFICATION: OP101// \<ENTER\>

DEA, SPECIAL HDLG: 6P// \<ENTER\>

DAW CODE: \<ENTER\>

NATIONAL FORMULARY INDICATOR: YES

LOCAL NON-FORMULARY: \<ENTER\>

VISN NON-FORMULARY: \<ENTER\>

Select DRUG TEXT ENTRY: \<ENTER\>

Select FORMULARY ALTERNATIVE: \<ENTER\>

Select SYNONYM: 000006336710// \<ENTER\>

SYNONYM: 000006336710// \<ENTER\>

INTENDED USE: DRUG ACCOUNTABILITY// \<ENTER\>

NDC CODE: 000006-3367-10// \<ENTER\>

Select SYNONYM: \<ENTER\>

MESSAGE: \<ENTER\>

RESTRICTION: \<ENTER\>

FSN: \<ENTER\>

NDC: 6-3367-10// \<ENTER\>

INACTIVE DATE: \<ENTER\>

WARNING LABEL SOURCE is not 'NEW'.

WARNING LABEL will be used until the WARNING LABEL SOURCE is set to 'NEW'.

WARNING LABEL: \<ENTER\>

Current Warning labels for TIMOLOL 0.5% OPTH SOL 10ML

Labels will print in the order in which they appear for local and CMOP fills:

22N For the eye.

Pharmacy fill card display: DRUG WARNING 22N

> **NOTE:** Because the NEW WARNING LABEL LIST field is empty, the warnings above

are the warnings that our national data source distributes for this drug.

Would you like to edit this list of warnings? N// \<ENTER\> O

ORDER UNIT: BT// \<ENTER\>

PRICE PER ORDER UNIT: 6.06// \<ENTER\>

DISPENSE UNIT: \<ENTER\>

DISPENSE UNITS PER ORDER UNIT: 1// \<ENTER\>

NCPDP DISPENSE UNIT: EACH//

NCPDP QUANTITY MULTIPLIER: 1//

PRICE PER DISPENSE UNIT: 6.060

points to TIMOLOL MALEATE 0.5% SOLN,OPH in the National Drug file.

This drug has already been matched and classified with the National Drug

file. In addition, if the dosage form changes as a result of rematching,

you will have to match/rematch to Orderable Item.

Do you wish to match/rematch to NATIONAL DRUG file? No// Y \<ENTER\> (Yes)

Deleting Possible Dosages...

LOCAL POSSIBLE DOSAGES:

1 DROP (Package -\> O)

2 DROP(S) (Package -\> O)

Delete these Local Possible Dosages? Y// NO

Local Possible Dosages not deleted.

Match local drug TIMOLOL 0.5% OPTH SOL 10ML

ORDER UNIT: BT

DISPENSE UNITS/ORDER UNITS: 1

DISPENSE UNIT:

I will try to match NDC: 6-3367-10 to NDF.

Local drug TIMOLOL 0.5% OPTH SOL 10ML

matches TIMOLOL MALEATE 0.5% SOLN,OPH

PACKAGE SIZE: 10 ML

PACKAGE TYPE: BOTTLE

Is this a match ?

Enter Yes or No: YES// \<ENTER\>

LOCAL DRUG NAME: TIMOLOL 0.5% OPTH SOL 10ML

ORDER UNIT: BT

DISPENSE UNITS/ORDER UNITS: 1

DISPENSE UNIT:

VA PRODUCT NAME: TIMOLOL MALEATE 0.5% SOLN,OPH

VA PRINT NAME: TIMOLOL MALEATE 0.5% OPH SOLN CMOP ID: T0056

VA DISPENSE UNIT: ML MARKABLE FOR CMOP: YES

PACKAGE SIZE: 10 ML

PACKAGE TYPE: BOTTLE

VA CLASS: OP101 BETA-BLOCKERS,TOPICAL OPHTHALMIC

CS FEDERAL SCHEDULE:

INGREDIENTS:

TIMOLOL MALEATE 0.5 %

NATIONAL FORMULARY INDICATOR: YES

NATIONAL FORMULARY RESTRICTION:

\< Enter "Y" for yes, "N" for no \>

Is this a match ? Y

You have just VERIFIED this match and MERGED the entry.

Resetting Possible Dosages..

Press Return to continue: \<ENTER\>

This drug has the following Local Possible Dosages:

1 DROP PACKAGE: IO

BCMA UNITS PER DOSE:

NUMERIC DOSE: DOSE UNIT:

2 DROP(S) PACKAGE: IO

BCMA UNITS PER DOSE:

NUMERIC DOSE: DOSE UNIT:

Do you want to merge new Local Possible Dosages? Y// ??

If you answer 'YES', any new Local Possible Dosages found based on the nouns

associated with the SOLN,OPH Dosage Form

will be added to your current Local Possible Dosages.

Do you want to merge new Local Possible Dosages? Y// NO

Just a reminder...you are editing TIMOLOL 0.5% OPTH SOL 10ML.

LOCAL POSSIBLE DOSAGES:

1 DROP PACKAGE: IO

BCMA UNITS PER DOSE:

NUMERIC DOSE: DOSE UNIT:

2 DROP(S) PACKAGE: IO

BCMA UNITS PER DOSE:

NUMERIC DOSE: DOSE UNIT:

Do you want to edit Local Possible Dosages? N// YES

This drug has the following Local Possible Dosages:

1 DROP PACKAGE: IO

BCMA UNITS PER DOSE:

NUMERIC DOSE: DOSE UNIT:

2 DROP(S) PACKAGE: IO

BCMA UNITS PER DOSE:

NUMERIC DOSE: DOSE UNIT:

Do you want to merge new Local Possible Dosages? Y// NO

Strength: 0.5 Unit: %

Select LOCAL POSSIBLE DOSAGE: 1 DROP IO

LOCAL POSSIBLE DOSAGE: 1 DROP// \<ENTER\>

OTHER LANGUAGE DOSAGE NAME: \<ENTER\>

PACKAGE: Both// \<ENTER\>

DOSE UNIT: DROP(S)// \<ENTER\>

NUMERIC DOSE: 1//\<ENTER\>

Strength: 0.5 Unit: %

Select LOCAL POSSIBLE DOSAGE: 2 DROP(S) IO

LOCAL POSSIBLE DOSAGE: 2 DROP(S)// \<ENTER\>

OTHER LANGUAGE DOSAGE NAME: \<ENTER\>

PACKAGE: Both// \<ENTER\>

DOSE UNIT: DROP(S)// \<ENTER\>

NUMERIC DOSE: 2// \<ENTER\>

Strength: 0.5 Unit: %

Select LOCAL POSSIBLE DOSAGE:

.

.

.

Entering new drug without matching to NDF

Select Pharmacy Data Management Option: Drug Enter/Edit

Select DRUG GENERIC NAME: PILOCARPINE 0.25% OPTH SOL 15ML

Are you adding 'PILOCARPINE 0.25% OPTH SOL 15ML' as

a new DRUG (the 1734TH)? No// Y (Yes)

DRUG NUMBER: 95// \<ENTER\>

DRUG VA CLASSIFICATION: \<ENTER\>

DRUG FSN: \<ENTER\>

DRUG NATIONAL DRUG CLASS: \<ENTER\>

DRUG LOCAL NON-FORMULARY: \<ENTER\>

DRUG INACTIVE DATE: \<ENTER\>

DRUG MESSAGE: \<ENTER\>

DRUG RESTRICTION: \<ENTER\>

GENERIC NAME: PILOCARPINE 0.25% OPTH SOL 15ML Replace \<ENTER\>

VA CLASSIFICATION: \<ENTER\>

DEA, SPECIAL HDLG: \<ENTER\>

DAW CODE: \<ENTER\>

NATIONAL FORMULARY INDICATOR: Not Matched To NDF

LOCAL NON-FORMULARY: \<ENTER\>

VISN NON-FORMULARY: \<ENTER\>

Select DRUG TEXT ENTRY: \<ENTER\>

Select FORMULARY ALTERNATIVE: \<ENTER\>

Select SYNONYM: \<ENTER\>

MESSAGE: \<ENTER\>

RESTRICTION: \<ENTER\>

FSN: \<ENTER\>

NDC: \<ENTER\>

INACTIVE DATE: \<ENTER\>

If you are planning to match to a NDF entry later or have no plan of using

the external billing function, you may skip the Service Code entry.

SERVICE CODE:

WARNING LABEL SOURCE is not 'NEW'.

WARNING LABEL will be used until the WARNING LABEL SOURCE is set to 'NEW'.

WARNING LABEL: \<ENTER\>

Current Warning labels for PILOCARPINE 0.25% OPTH SOL 15ML

No warnings from the new data source exist for this drug.

Verify that the drug is matched to the National Drug File.

Would you like to edit this list of warnings? N//\<ENTER\> O

ORDER UNIT: BT BOTTLE

PRICE PER ORDER UNIT: 10

DISPENSE UNIT: ML

DISPENSE UNITS PER ORDER UNIT: 15

> **NOTE:** Defaulting the NCPDP DISPENSE UNIT to EACH and the

NCPDP QUANTITY MULTIPLIER to 1 (one).

NCPDP DISPENSE UNIT: EACH//

NCPDP QUANTITY MULTIPLIER: 1//

PRICE PER DISPENSE UNIT: 0.6667

Do you wish to match/rematch to NATIONAL DRUG file? Yes// N \<ENTER\> (No)

Just a reminder...you are editing PILOCARPINE 0.25% OPTH SOL 15ML.

LOCAL POSSIBLE DOSAGES: \<ENTER\>

Do you want to edit Local Possible Dosages? N// YES

Strength: Unit:

Select LOCAL POSSIBLE DOSAGE: ONE DROP(S)

Are you adding 'ONE DROP(S)' as

a new LOCAL POSSIBLE DOSAGE (the 1ST for this DRUG)? No// Y (Yes)

LOCAL POSSIBLE DOSAGE: ONE DROP(S)// \<ENTER\>

OTHER LANGUAGE DOSAGE NAME: \<ENTER\>

PACKAGE: IO Both

BCMA UNITS PER DOSE: \<ENTER\>

DOSE UNIT: DROP(S)

NUMERIC DOSE: 1

Strength: \<ENTER\> Unit: \<ENTER\>

Select LOCAL POSSIBLE DOSAGE: TWO DROP(S)

Are you adding 'TWO DROP(S)' as

a new LOCAL POSSIBLE DOSAGE (the 2ND for this DRUG)? No// Y (Yes)

LOCAL POSSIBLE DOSAGE: TWO DROP(S)// \<ENTER\>

OTHER LANGUAGE DOSAGE NAME: \<ENTER\>

PACKAGE: Both

BCMA UNITS PER DOSE: \<ENTER\>

DOSE UNIT: DROP(S)

NUMERIC DOSE: 2

Strength: \<ENTER\> Unit: \<ENTER\>

Select LOCAL POSSIBLE DOSAGE:

.

.

.

Strength Mismatch

Select Pharmacy Data Management Option: DRUG

1 Drug Enter/Edit

2 Drug Interaction Management

3 Drug Text Management

CHOOSE 1-3: 1 Drug Enter/Edit

Select DRUG GENERIC NAME: ACETAMINOPHEN ELIX. 120MG/5ML 4OZ CN103

...OK? Yes// \<ENTER\> (Yes)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This entry is marked for the following PHARMACY packages:

Outpatient

Unit Dose

Non-VA Med

GENERIC NAME: ACETAMINOPHEN ELIX. 120MG/5ML 4OZ Replace \<ENTER\>

VA CLASSIFICATION: CN103// \<ENTER\>

DEA, SPECIAL HDLG: 6// \<ENTER\>

DAW CODE: \<ENTER\>

NATIONAL FORMULARY INDICATOR: YES

LOCAL NON-FORMULARY: \<ENTER\>

VISN NON-FORMULARY: \<ENTER\>

Select DRUG TEXT ENTRY: \<ENTER\>

Select FORMULARY ALTERNATIVE: \<ENTER\>

Select SYNONYM: 000054301050// \<ENTER\>

SYNONYM: 000054301050// \<ENTER\>

INTENDED USE: DRUG ACCOUNTABILITY// \<ENTER\>

NDC CODE: 000054-3010-50// \<ENTER\>

Select SYNONYM: \<ENTER\>

MESSAGE: \<ENTER\>

RESTRICTION: \<ENTER\>

FSN: \<ENTER\>

NDC: 54-3010-50// \<ENTER\>

INACTIVE DATE: \<ENTER\>

WARNING LABEL SOURCE is not 'NEW'.

WARNING LABEL will be used until the WARNING LABEL SOURCE is set to 'NEW'.

WARNING LABEL: 8// \<ENTER\>

Current Warning labels for ACETAMINOPHEN ELIX. 120MG/5ML 4OZ

Labels will print in the order in which they appear for local and CMOP fills:

8N Do not drink alcoholic beverages when taking this medication.

66N This medicine contains ACETAMINOPHEN. Taking more ACETAMINOPHEN than

recommended may cause serious liver problems.

70N Do not take other ACETAMINOPHEN containing products at the same time

without first checking with your doctor. Check all medicine labels carefully.

Pharmacy fill card display: DRUG WARNING 8N,66N,70N

> **NOTE:** Because the NEW WARNING LABEL LIST field is empty, the warnings above

are the warnings that our national data source distributes for this drug.

Would you like to edit this list of warnings? N// \<ENTER\> O

ORDER UNIT: \<ENTER\>

PRICE PER ORDER UNIT: \<ENTER\>

DISPENSE UNIT: \<ENTER\>

DISPENSE UNITS PER ORDER UNIT: 1// \<ENTER\>

PRICE PER DISPENSE UNIT: 0.000

points to ACETAMINOPHEN 160MG/5ML ELIXIR in the National Drug file.

This drug has already been matched and classified with the National Drug

file. In addition, if the dosage form changes as a result of rematching,

you will have to match/rematch to Orderable Item.

Do you wish to match/rematch to NATIONAL DRUG file? No// \<ENTER\> (No)

Just a reminder...you are editing ACETAMINOPHEN ELIX. 120MG/5ML 4OZ.

Strength from National Drug File match =\> 160 MG/5ML

Strength currently in the Drug File =\> 120

Please Note: Strength of drug does not match strength of VA Product it is matched to.

Press Return to Continue: \<ENTER\>

Strength =\> 120 Unit =\>

POSSIBLE DOSAGES:

DISPENSE UNITS PER DOSE: 2 DOSE: 240 MG/5 ML PACKAGE: I

LOCAL POSSIBLE DOSAGES:

LOCAL POSSIBLE DOSAGE: ONE TEASPOONFUL PACKAGE: O

BCMA UNITS PER DOSE:

NUMERIC DOSE: 120 DOSE UNIT: MILLIGRAM(S)

Do you want to edit the dosages? N// YES

Changing the strength will update all possible dosages for this Drug.

This drug has the following Local Possible Dosages:

Press Return to continue,'^' to exit the list:

ONE TEASPOONFUL PACKAGE: O

BCMA UNITS PER DOSE:

NUMERIC DOSE: 120 DOSE UNIT: MILLIGRAM(S)

Do you want to merge new Local Possible Dosages? Y// NO

Strength: 120 Unit: MG/5MLSelect LOCAL POSSIBLE DOSAGE: ?

Answer with LOCAL POSSIBLE DOSAGE:

ONE TEASPOONFUL O

You may enter a new LOCAL POSSIBLE DOSAGE, if you wish

Answer must be 1-60 characters in length.

Select LOCAL POSSIBLE DOSAGE: ONE TEASPOONFUL O

LOCAL POSSIBLE DOSAGE: ONE TEASPOONFUL// \<ENTER\>

OTHER LANGUAGE DOSAGE NAME: \<ENTER\>

PACKAGE: Outpatient// \<ENTER\>

DOSE UNIT: MILLIGRAM(S)// \<ENTER\>

NUMERIC DOSE:120//\<ENTER\>

Strength: 120 Unit: MG/5ML

Select LOCAL POSSIBLE DOSAGE:

## Strength Mismatch Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS STRENGTH MISMATCH\]

A new *Strength Mismatch Report* \[PSS STRENGTH MISMATCH\] option will list all DRUG file (#50) entries that have a strength defined that does not match the strength of the VA product that it is matched to. If these drugs have Local Possible Dosages, you need to be careful when populating the new Dose Unit and Numeric Dose fields to be used for Dosage checks, because the Dosage check will be based on the VA Product. This report can only identify strength mismatches if the drug qualifies for Possible Dosages, and a Strength has been defined in the DRUG file (#50).

The report will display:

- Internal Entry Number (IEN) of the Drug
- Drug Name
- Inactivation Date
- Strength
- Units
- Application Package Use
- Possible Dosages
  - Dispense Units Per Dose
  - Dose
  - Package
  - Outpatient Expansion
- Local Possible Dosages
  - Local Possible Dosage
  - Numeric Dose
  - Dose Unit
  - Package
- Strength mismatch message noting the drug strength and VA Product strength, along with the VA Product Name the drug is matched to

Select Enhanced Order Checks Setup Menu Option: STREngth Mismatch Report

This report will print Dosage information for all entries in the DRUG (#50)

File that have a different Strength than what is in the VA PRODUCT (#50.68)

File match. If these drugs have Local Possible Dosages, you need to be careful

when populating the new Dose Unit and Numeric Dose fields to be used for Dosage

checks, because the Dosage check will be based on the VA Product. This report

can only identify Strength mismatches if the Drug qualifies for Possible

Dosages, and a Strength has been defined in the DRUG (#50) File.

This report is designed for 132 column format!

DEVICE: HOME//\<ENTER\>

Mismatched Strength Report PAGE: 1

--------------------------------------------------------------------------------------

\(65\) CAPTOPRIL 6.25MG TAB Inactive Date:

Strength: 6.25 Units: MG Application Package:

Possible Dosages:

Dispense Units Per Dose: 1 Dose: 6.25MG Package: IO ONE TABLET

Dispense Units Per Dose: 2 Dose: 12.5MG Package: IO TWO TABLETS

Local Possible Dosages: (None)

> **NOTE:** Strength 6.25 does not match NDF strength of 12.5.

VA PRODUCT MATCH: CAPTOPRIL 12.5MG TAB

\(156\) GUAIFENESIN 50MG/5ML SYRUP Inactive Date:

Strength: 50 Units: Application Package: OX

Possible Dosages:

Dispense Units Per Dose: 1 Dose: 50MG/2.5ML Package: I

Dispense Units Per Dose: 2 Dose: 100MG/5ML Package: I

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 50 Dose Unit: MILLIGRAM(S) Package: O

2 TEASPOONSUL(S)

Numeric Dose: 100 Dose Unit: MILLIGRAM(S) Package: O

> **NOTE:** Strength 50 does not match NDF strength of 100.

VA PRODUCT MATCH: GUAIFENESIN 100MG/5ML SYRUP.

## Review Dosages Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS DOSAGE REVIEW REPORT\]

The *Review Dosages Report* \[PSS DOSAGE REVIEW REPORT\] option now displays the new Numeric Dose and Dose Unit fields defined for Local Possible Dosages.

If the strength of the drug does not match the strength of the VA Product to which it is matched to, it will be noted on the report. The VA Product Name will also be displayed.

Dosage report for all drugs

Select Dosages Option: REVIEW Dosages Report

Select one of the following:

A ALL

S SELECT A RANGE

Print Report for (A)ll or (S)elect a Range: S// ALL

This report will be for all drugs.

Is this correct? Y// \<ENTER\> ES

This report is designed for 132 column format!

DEVICE: HOME// \<ENTER\>

Dosage report for all drugs Outpatient Expansion PAGE: 1

-------------------------------------------------------------------------------------------------

\(699\) GUAIFENESIN 50MG/5ML SYRUP Inactive Date:

Strength: 50 Units: Application Package: OX

Possible Dosages:

Dispense Units Per Dose: 1 Dose: 50MG/2.5ML Package: I

Dispense Units Per Dose: 2 Dose: 100MG/5ML Package: I

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 50 Dose Unit: MILLIGRAM(S) Package: O

2 TEASPOONSUL(S)

Numeric Dose: 100 Dose Unit: MILLIGRAM(S) Package: O

> **NOTE:** Strength of 50 does not match NDF strength of 100.

VA PRODUCT MATCH: GUAIFENESIN 100MG/5ML SYRUP

\(2280\) IBUPROFEN 300MG TAB \*N/F\* Inactive Date:

Strength: 300 Units: MG Application Package: OX

Possible Dosages: (None)

Local Possible Dosages:

3 TABLETS

Numeric Dose: 900 Dose Unit: MILLIGRAM(S) Package: IO

4 TABLETS

Numeric Dose: 1200 Dose Unit: MILLIGRAM(S) Package: IO

\(5249\) IBUPROFEN 400MG (120'S) \*N/F\* Inactive Date:

Strength: 400 Units: MG Application Package: OX

Possible Dosages:

Dispense Units Per Dose: 1 Dose: 400MG Package: IO 1 TABLET

Dispense Units Per Dose: 2 Dose: 800MG Package: IO 2 TABLETS

Local Possible Dosages: (None)

\(1676\) TIMOLOL 0.25% OPTH SOLN (10ML) Inactive Date:

Strength: Units: Application Package: OXU

Possible Dosages: (None)

Local Possible Dosages:

2 DROPS

Numeric Dose: 2 Dose Unit: DROP(S) Package: IO

## # Chapter 3 – Frequency Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to perform a daily dose range check on a prescribed medication, the software needs to determine how many times per day the single dosage is taken. The schedule from an order will be used to obtain that information. The FREQUENCY (IN MINUTES) field (#2) in the ADMINISTRATION SCHEDULE file (#51.1) or the FREQUENCY (IN MINUTES) field (#31) in the MEDICATION INSTRUCTION file (#51) will be used to calculate a frequency.

If a schedule entered for a medication order is not found in either the ADMINISTRATION SCHEDULE (marked with prefix of ‘PSJ’) or MEDICATION INSTRUCTION files or is found in one of those two files, but a frequency (in minutes) does not exist, a daily dose range check will not be performed. The user will be informed of this and a reason given as to why. A maximum single dose check will still be performed and general dosing information for the drug will be provided.

If the type of schedule for an administration schedule used for an order is designated as ONE-TIME or ON CALL or if the Schedule Type for a Unit Dose order is ONE-TIME or ON CALL only a maximum single dosage check will be performed on the order and a frequency is not needed.

If the TYPE OF SCHEDULE for an Administration Schedule within an order is designated as DAY OF THE WEEK, the number of administration times will be used to determine the frequency in order to perform a daily dose range check. If none are defined, a frequency of ‘1’ will be assumed.

Enhanced Order Checks Setup Menu:

Find Unmapped Local Medication Routes

Map Local Medication Route to Standard

Medication Route Mapping Report

Medication Route File Enter/Edit

Medication Route Mapping History Report

Request Change to Standard Medication Route

Find Unmapped Local Possible Dosages

Map Local Possible Dosages

Local Possible Dosages Report

Strength Mismatch Report

Enter/Edit Dosages

Request Change to Dose Unit

Mark PreMix Solutions

IV Solution Report

Administration Schedule File ReportMedication Instruction File Report

## Administration Schedule File Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS SCHEDULE REPORT\]

The new *Administration Schedule File Report* \[PSS SCHEDULE REPORT\] option prints out entries from the Administration Schedule file in order to check to see if a frequency is defined. A report can be run for all administration schedules or only the administration schedules without a frequency.

Only administration schedules with a PACKAGE PREFIX (field \#4) set to ‘PSJ’ will be included in the report.

The report can be set to print in either an 80 or 132 column format.

The report will include

- Schedule Name
- Standard Administration Times
- Outpatient Expansion
- Other Language Expansion
- Ward(s)
  - Ward
  - Ward Administration Times
- Type of Schedule
- Frequency in Minutes

  
User selects all administration schedules

> Select Enhanced Order Checks Setup Menu Option: Administration Schedule File

> Report

> This report displays entries from the ADMINISTRATION SCHEDULE (#51.1) File.

> It can be run for all Schedules, or only Schedules without a FREQUENCY

> (IN MINUTES). Only schedules with a PSJ Package Prefix will be displayed, since

> they are the only schedules the software will look at when deriving a FREQUENCY

> (IN MINUTES) for the daily dosage checks. If a FREQUENCY (IN MINUTES) cannot

> be determined for an order, the daily dosage check cannot occur for that order.

> Select one of the following:

> A All Schedules

> O Only Schedules with a missing frequency

> Print All Schedules, or Only Schedules without a frequency: A//\<ENTER\> ll Schedules

> Select one of the following:

> 80 80 Column

> 132 132 Column

> Print report in 80 or 132 column format: 80// \<ENTER\> Column

> DEVICE: HOME// \<ENTER\>

> ADMINISTRATION SCHEDULE FILE REPORT (All) PAGE: 1

> -----------------------------------------------------------------------------

> BID

> STANDARD ADMINISTRATION TIMES: 09-17

> OUTPATIENT EXPANSION: TWICE A DAY

> OTHER LANGUAGE EXPANSION:

> WARD: GEN MED

> WARD ADMINISTRATION TIMES: 08-16

> WARD: 7A GEN MED

> WARD ADMINISTRATION TIMES: 10-18

> SCHEDULE TYPE: CONTINUOUS

> FREQUENCY (IN MINUTES): 720

> Q1H

> STANDARD ADMINISTRATION TIMES: 0100-0200-0300-0400-0500-0600-0700-0800-

> 0900-1000-1100-1200-1300-1400-1500-1600-

> 1700-1800-1900-2000-2100-2200-2300-2400

> OUTPATIENT EXPANSION: EVERY HOUR

> OTHER LANGUAGE EXPANSION:

> SCHEDULE TYPE: CONTINUOUS

> FREQUENCY (IN MINUTES): 60

> Q6H

> STANDARD ADMINISTRATION TIMES: 06-12-18-24

> OUTPATIENT EXPANSION: EVERY 6 HOURS

> OTHER LANGUAGE EXPANSION:

> SCHEDULE TYPE: CONTINUOUS

> FREQUENCY (IN MINUTES): 360

> QHS

> STANDARD ADMINISTRATION TIMES: 21

> OUTPATIENT EXPANSION: AT BEDTIME

> OTHER LANGUAGE EXPANSION:

> SCHEDULE TYPE: CONTINUOUS

> FREQUENCY (IN MINUTES): 1440

> TID

> STANDARD ADMINISTRATION TIMES: 09-13-17

> OUTPATIENT EXPANSION: THREE TIMES A DAY

> OTHER LANGUAGE EXPANSION:

> SCHEDULE TYPE: CONTINUOUS

> FREQUENCY (IN MINUTES): 480

End of Report

User selects administration schedules without a frequency defined.

> Select Enhanced Order Checks Setup Menu Option: ADMINistration Schedule File

> Report

> This report displays entries from the ADMINISTRATION SCHEDULE (#51.1) File.

> It can be run for all Schedules, or only Schedules without a FREQUENCY

> (IN MINUTES). Only schedules with a PSJ Package Prefix will be displayed, since

> they are the only schedules the software will look at when deriving a FREQUENCY

> (IN MINUTES) for the daily dosage checks. If a FREQUENCY (IN MINUTES) cannot

> be determined for an order, the daily dosage check cannot occur for that order.

> Select one of the following:

> A All Schedules

> O Only Schedules with a missing frequency

> Print All Schedules, or Only Schedules without a frequency: A// Only Schedules with a missing frequency

> Select one of the following:

> 80 80 Column

> 132 132 Column

> Print report in 80 or 132 column format: 80// \<ENTER\> Column

> DEVICE: HOME// \<ENTER\>

> ADMINISTRATION SCHEDULE WITHOUT FREQUENCY REPORT PAGE: 1

> -----------------------------------------------------------------------------

> BID-W/MEAL

> STANDARD ADMINISTRATION TIMES: 11

> OUTPATIENT EXPANSION:

> OTHER LANGUAGE EXPANSION:

> SCHEDULE TYPE:

> FREQUENCY (IN MINUTES):

> Q12H

> STANDARD ADMINISTRATION TIMES: 0900-2100

> OUTPATIENT EXPANSION: EVERY 12 HOURS

> OTHER LANGUAGE EXPANSION:

> SCHEDULE TYPE:

> FREQUENCY (IN MINUTES):

> End of Report.

## Medication Instruction File Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSS MED INSTRUCTION REPORT

The new *Medication Instruction File Report* option prints out entries from the MEDICATION INSTRUCTION file (#51) in order to check to see if a frequency is defined.

The report can be run for all medication instructions or just the medication instructions without a frequency.

The report can be set to print in either an 80 or 132 column format.

The report will include:

- Medication Instruction Name
- Synonym
- Expansion
- Other Language Expansion
- Plural
- Intended Use
- Frequency in Minutes

If the report is run for only those medication instructions with a missing frequency and all medication instructions have a frequency, the report will note that.

User selects all medication instructions

> Select Enhanced Order Checks Setup Menu Option: Medication Instruction File Report

> This report displays entries from the MEDICATION INSTRUCTION (#51) File. It

> can be run for all Medication Instructions or only Medication Instructions

> without a FREQUENCY (IN MINUTES). If a FREQUENCY (IN MINUTES) cannot be

> determined for an order, the daily dosage check cannot occur for that order.

> Select one of the following:

> A All Medication Instructions

> O Only Medication Instructions with a missing frequency

> Print All Medication Instructions, or Only Medication Instructions

> without a frequency: A// All Medication Instructions

> Select one of the following:

> 80 80 Column

> 132 132 Column

> Print report in 80 or 132 column format: 80// \<ENTER\> Column

> DEVICE: HOME// \<ENTER\>

> MEDICATION INSTRUCTION FILE REPORT (All) PAGE: 1

> -----------------------------------------------------------------------------

> AD

> SYNONYM:

> EXPANSION: RIGHT EAR

> OTHER LANGUAGE EXPANSION:

> PLURAL:

> INTENDED USE: OUTPATIENT ONLY

> FREQUENCY (IN MINUTES):

> BID

> SYNONYM:

> EXPANSION: TWICE A DAY

> OTHER LANGUAGE EXPANSION:

> PLURAL:

> INTENDED USE: IN & OUTPATIENT

> FREQUENCY (IN MINUTES): 720

> FCP

> SYNONYM:

> EXPANSION: FOR CHEST PAIN

> OTHER LANGUAGE EXPANSION:

> PLURAL:

> INTENDED USE: IN & OUTPATIENT

> FREQUENCY (IN MINUTES):

> Q12H

> SYNONYM: Q12

> EXPANSION: EVERY TWELVE HOURS

> OTHER LANGUAGE EXPANSION:

> PLURAL:

> INTENDED USE: IN & OUTPATIENT

> FREQUENCY (IN MINUTES): 720

> Q46

> SYNONYM: Q46H

> EXPANSION: EVERY 4-6 HOURS

> OTHER LANGUAGE EXPANSION:

> PLURAL:

> INTENDED USE: IN & OUTPATIENT

> FREQUENCY (IN MINUTES): 240

> QIDAC

> SYNONYM: QIDACHS

> EXPANSION: FOUR TIMES A DAY BEFORE MEALS & AT BEDTIME

> OTHER LANGUAGE EXPANSION:

> PLURAL:

> INTENDED USE: IN & OUTPATIENT

> FREQUENCY (IN MINUTES): 288

> WM

> SYNONYM:

> EXPANSION: WITH MEALS

> OTHER LANGUAGE EXPANSION:

> PLURAL:

> INTENDED USE: IN & OUTPATIENT

> FREQUENCY (IN MINUTES):

End of Report

  
User selects medication instruction without a frequency defined

Select Enhanced Order Checks Setup Menu Option: Medication Instruction File Report

This report displays entries from the MEDICATION INSTRUCTION (#51) File. It

can be run for all Medication Instructions or only Medication Instructions

without a FREQUENCY (IN MINUTES). If a FREQUENCY (IN MINUTES) cannot be

determined for an order, the daily dosage check cannot occur for that order.

Select one of the following:

A All Medication Instructions

O Only Medication Instructions with a missing frequency

Print All Medication Instructions, or Only Medication Instructions

without a frequency: A// Only Medication Instructions with a missing frequency

Select one of the following:

80 80 Column

132 132 Column

Print report in 80 or 132 column format: 80// \<ENTER\> Column

DEVICE: HOME// \<ENTER\>

MEDICATION INSTRUCTIONS WITHOUT FREQUENCY REPORT PAGE: 1

-----------------------------------------------------------------------------

> AC

> SYNONYM:

> EXPANSION: BEFORE MEALS

> OTHER LANGUAGE EXPANSION:

> PLURAL:

> INTENDED USE: IN & OUTPATIENT

> FREQUENCY (IN MINUTES):

> AD

> SYNONYM:

> EXPANSION: RIGHT EAR

> OTHER LANGUAGE EXPANSION:

> PLURAL:

> INTENDED USE: OUTPATIENT ONLY

> FREQUENCY (IN MINUTES):

> FCP

> SYNONYM:

> EXPANSION: FOR CHEST PAIN

> OTHER LANGUAGE EXPANSION:

> PLURAL:

> INTENDED USE: IN & OUTPATIENT

> FREQUENCY (IN MINUTES):

> PC

> SYNONYM:

> EXPANSION: AFTER MEALS

> OTHER LANGUAGE EXPANSION:

> PLURAL:

> INTENDED USE: IN & OUTPATIENT

> FREQUENCY (IN MINUTES):

> WM

> SYNONYM:

> EXPANSION: WITH MEALS

> OTHER LANGUAGE EXPANSION:

> PLURAL:

> INTENDED USE: IN & OUTPATIENT

> FREQUENCY (IN MINUTES):

End of Report.

All medication instructions have a frequency defined

This report displays entries from the MEDICATION INSTRUCTION (#51) File. It

can be run for all Medication Instructions or only Medication Instructions

without a FREQUENCY (IN MINUTES). If a FREQUENCY (IN MINUTES) cannot be

determined for an order, the daily dosage check cannot occur for that order.

Select one of the following:

A All Medication Instructions

O Only Medication Instructions with a missing frequency

Print All Medication Instructions, or Only Medication Instructions

without a frequency: A// Only Medication Instructions with a missing frequency

Select one of the following:

80 80 Column

132 132 Column

Print report in 80 or 132 column format: 80// \<ENTER\> Column

DEVICE: HOME// \<ENTER\>

MEDICATION INSTRUCTIONS WITHOUT FREQUENCY REPORT PAGE: 1

-----------------------------------------------------------------------------

No Medication Instructions found without frequencies

# Chapter 4 – Identify IV Solution PreMixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A PreMix solution is an IV Solution that comes prepared from the manufacturer with additives. An example would be Heparin 25,000 units in 5% Dextrose 250ml or 5% Dextrose 0.45% Sodium Chloride with 20 MeQ Potassium Chloride 1000ml. Currently if such a drug is entered as an IV Solution for an IV order, it does not participate in order checks (i.e. drug-drug interactions, duplicate class, etc). If entered as an IV Additive it does.

You can now enter these types of premixed drugs as IV Solutions and mark them as PreMixes and they will participate in order checks. Order checks will be performed on the drug associated with the IV solution. If you have your PreMix solutions set up as IV additives or set up as an IV additive and IV solution in order to participate in order checks, you do NOT have to make any changes if you do not wish to. They will continue to participate in order checks when PRE V. 0.5 is released.

However, if you want to enter your PreMixes as IV Solutions and mark them as PreMixes you have two options:

1\) Make your file changes AFTER PRE V. 0.5 is installed.

2\) Make your file changes NOW, but keep them inactivated.

Once PRE V. 0.5 is installed, you can delete the inactivation date and inactivate the IV additives or IV Additive and IV Solution entries that you are replacing.

Remember, these changes will only be recognized by PRE V. 0.5 software.

The following bolded options are to be used to identify and mark PreMixes.

Enhanced Order Checks Setup Menu:

Find Unmapped Local Medication Routes

Map Local Medication Route to Standard

Medication Route Mapping Report

Medication Route File Enter/Edit

Medication Route Mapping History Report

Request Change to Standard Medication Route

Find Unmapped Local Possible Dosages

Map Local Possible Dosages

Local Possible Dosages Report

Strength Mismatch Report

Enter/Edit Dosages

Request Change to Dose Unit

Mark PreMix SolutionsIV Solution Report

Administration Schedule File Report

Medication Instruction File Report

These additional options may also be used to mark an IV Solution as a PreMix:

> Drug Enter/Edit (under Pharmacy Data Management option)

> Primary Solution File (IV) (stand alone option)

The detailed descriptions of the options that follow are presented in the logical sequence to accomplish the file setup, not the order in which they are displayed on the menu.

## IV Solution Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS IV SOLUTION REPORT\]

The new *IV Solution Report* \[PSS IV SOLUTION REPORT\] option displays only IV solutions marked as PreMixes or all IV solutions.

The report will print the following data elements:

- Print Name
- Print Name {2}
- Volume
- Synonyms
- Generic Drug
- Pharmacy Orderable Item
- Inactivation Date
- Used in IV Fluid Order Entry
- PreMix

If the user chooses to print only the IV solutions marked as PreMixes and none are found the report will display ‘No IV Solutions marked as PreMixes found.’

  
User selects only solutions marked as PreMix

Select Enhanced Order Checks Setup Menu Option: IV SOLUTION Report

This report displays only those solutions in the IV Solutions (#52.7) File

that are marked as PreMix IV Solutions, or it displays all Solutions.

Select one of the following:

P Print only IV Solutions marked as PreMix

A Print All IV Solutions

Print report for PreMix (P), or All IV Solutions (A): (P/A): Premix: P// \<ENTER\> rint only IV Solutions marked as PreMix

This report is designed for 80 column format!

DEVICE: HOME// \<ENTER\>

Solution PreMix report for IV Solutions marked as PreMix Page: 1

---------------------------------------------------------------------------

Print Name: DOPAMINE 400MG IN DEXTROSE 5% Volume: 500 ML

Print Name {2}:

> Synonyms: INTROPIN

> DOPAMINE D5

> Generic Drug: DOPAMINE 400MG IN 5% DEXTROSE 500ML

> Pharmacy Orderable Item: DOPAMINE IN DEXTROSE 5% INJ,SOL

> Inactivation Date:

> Used in IV Fluid Order Entry: YES

> PreMix: YES

Print Name: METRONIDAZOLE 500MG IN NACL Volume: 100 ML

Print Name {2}:

Synonyms:

Generic Drug: METRONIDAZOLE 500MG/100ML NACL

Pharmacy Orderable Item: METRONIDAZOLE/SODIUM CHLORIDE INJ,SOLN

Inactivation Date:

Used in IV Fluid Order Entry: YES

PreMix: YES

End of Report

No IV solutions marked as PreMixes

Select Enhanced Order Checks Setup Menu Option: IV SOLUTION Report

This report displays only those solutions in the IV Solutions (#52.7) File

that are marked as PreMix IV Solutions, or it displays all Solutions.

Select one of the following:

P Print only IV Solutions marked as PreMix

A Print All IV Solutions

Print report for PreMix (P), or All IV Solutions (A): (P/A): Premix: P// \<ENTER\> rint only IV Solutions marked as PreMix

This report is designed for 80 column format!

DEVICE: HOME// \<ENTER\>

Solution PreMix report for IV Solutions marked as PreMix Page: 1

---------------------------------------------------------------------------

No IV Solutions marked as PreMixes found.

User Selects all IV Solutions

Select Enhanced Order Checks Setup Menu Option: IV Solution Report

This report displays only those solutions in the IV Solutions (#52.7) File

that are marked as PreMix IV Solutions, or it displays all Solutions.

Select one of the following:

P Print only IV Solutions marked as PreMix

A Print All IV Solutions

Print report for PreMix (P), or All IV Solutions (A): (P/A): Premix: P// a Print All IV Solutions

This report is designed for 80 column format!

DEVICE: HOME// \<ENTER\>

Solution PreMix report for all IV Solutions Page: 1

------------------------------------------------------------------------------

Print Name: 0.9% SODIUM CHLORIDE Volume: 100 ML

Print Name {2}:

Synonyms: 2673

Generic Drug: SODIUM CHLORIDE 0.9% 100ML

Pharmacy Orderable Item: SODIUM CHLORIDE INJ

Inactivation Date:

Used in IV Fluid Order Entry: YES

PreMix:

Print Name: 0.9% SODIUM CHLORIDE Volume: 50 ML

Print Name {2}:

Synonyms: 2672

Generic Drug: SODIUM CHLORIDE 0.9% 50ML

Pharmacy Orderable Item: SODIUM CHLORIDE INJ

Inactivation Date:

Used in IV Fluid Order Entry: YES

PreMix:

Print Name: 20% DEXTROSE Volume: 500 ML

Print Name {2}:

Synonyms:

Generic Drug: DEXTROSE 20% IN WATER 500ML

Pharmacy Orderable Item: DEXTROSE INJ,SOLN

Inactivation Date:

Used in IV Fluid Order Entry: YES

PreMix:

Print Name: METRONIDAZOLE 500MG IN NACL Volume: 100 ML

Print Name {2}:

Synonyms:

Generic Drug: METRONIDAZOLE 500MG/100ML NACL

Pharmacy Orderable Item: METRONIDAZOLE/SODIUM CHLORIDE INJ,SOLN

Inactivation Date:

Used in IV Fluid Order Entry: YES

PreMix: YES

End of Report.

## Mark PreMix Solutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS MARK PREMIX SOLUTIONS\]

The new *Mark PreMix Solutions* \[PSS MARK PREMIX SOLUTIONS\] option allows a user to quickly mark an IV Solution as a PreMix.

The following data fields can be edited:

- Print Name
- Print Name {2}
- Generic Drug
- Volume
- Inactivation Date
- Used in IV Fluid Order Entry
- PreMix

After successful edit of an entry, the user will be prompted to enter another IV Solution to edit. If the user presses \<ENTER\>, they will be exited out of the option.

Select Enhanced Order Checks Setup Menu Option: MARK PreMix Solutions

Select IV SOLUTIONS PRINT NAME: HEP

1 HEPARIN 1,000U/0.9% NS-2U/ML 500 ML

2 HEPARIN 25,000U/D5W (50U/ML) 500 ML

3 HEPARIN 25000 UNITS/0.45% NACL 250 ML

CHOOSE 1-3: 3 HEPARIN 25000 UNITS/0.45% NACL 250 ML

PRINT NAME: HEPARIN 25000 UNITS/0.45% NACL Replace \<ENTER\>

PRINT NAME {2}: \<ENTER\>

GENERIC DRUG: HEPARIN 25,000 UNITS IN 0.45% NACL 250ML

// \<ENTER\>

VOLUME: 250 ML// \<ENTER\>

INACTIVATION DATE:

USED IN IV FLUID ORDER ENTRY: YES// \<ENTER\>

PREMIX: YES// \<ENTER\>

Select IV SOLUTIONS PRINT NAME:

## Drug Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS DRUG ENTER/EDIT\]

The *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option allows a user to mark an IV Solution as a PreMix.

Select Pharmacy Data Management Option: Drug Enter/Edit

Select DRUG GENERIC NAME: METRONIDAZOLE 500MG/100ML NACL AM900

...OK? Yes// \<ENTER\> (Yes)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This entry is marked for the following PHARMACY packages:

IV

GENERIC NAME: METRONIDAZOLE 500MG/100ML NACL Replace \<ENTER\>

VA CLASSIFICATION: AM900// \<ENTER\>

DEA, SPECIAL HDLG: \<ENTER\>

DAW CODE: \<ENTER\>

.

.

.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This entry is marked for the following PHARMACY packages:

IV

MARK THIS DRUG AND EDIT IT FOR:

O - Outpatient

U - Unit Dose

I - IV

W - Ward Stock

D - Drug Accountability

C - Controlled Substances

X - Non-VA Med

A - ALL

Enter your choice(s) separated by commas : I

I - IV

\*\* You are NOW editing IV fields. \*\*

AN IV ITEM? Yes// \<ENTER\> (Yes)

Edit Additives or Solutions:

Select one of the following:

A ADDITIVES

S SOLUTIONS

Enter response: SOLUTIONS

Select IV SOLUTIONS PRINT NAME: METRONIDAZOLE 500MG IN NACL 100 ML

PRINT NAME: METRONIDAZOLE 500MG IN NACL Replace \<ENTER\>

PRINT NAME {2}: \<ENTER\>

GENERIC DRUG: METRONIDAZOLE 500MG/100ML NACL// \<ENTER\>

VOLUME: 100 ML// \<ENTER\>

Select ELECTROLYTES: \<ENTER\>

Select SYNONYM: \<ENTER\>

DRUG INFORMATION: \<ENTER\>

No existing text

Edit? NO// \<ENTER\>

AVERAGE DRUG COST: \<ENTER\>

INACTIVATION DATE: \<ENTER\>

USED IN IV FLUID ORDER ENTRY: YES// \<ENTER\>

PREMIX: YES

Edit Additives or Solutions: \<ENTER\>

Select one of the following:

A ADDITIVES

S SOLUTIONS

Enter response:

## Primary Solution File (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSSJI SOLN\]

The *Primary Solution File (IV)* \[PSSJI SOLN\] stand alone option is modified to allow a user to mark an IV Solution as a premix.

Select OPTION NAME: PRIMARY SOLUTION FILE (IV) PSSJI SOLN PRimary Solution

File (IV)

PRimary Solution File (IV)

Select IV ROOM NAME: ALBANY IV ROOM

You are signed on under the ALBANY IV ROOM IV ROOM

Current IV LABEL device is: TELNET - IN

Current IV REPORT device is: TELNET - IN

Select IV SOLUTIONS PRINT NAME: METRONIDAZOLE 500MG IN NACL 100 ML

PRINT NAME: METRONIDAZOLE 500MG IN NACL Replace \<ENTER\>

PRINT NAME {2}: \<ENTER\>

GENERIC DRUG: METRONIDAZOLE 500MG/100ML NACL// \<ENTER\>

VOLUME: 100 ML// \<ENTER\>

Select ELECTROLYTES: \<ENTER\>

Select SYNONYM: \<ENTER\>

DRUG INFORMATION: \<ENTER\>

No existing text

Edit? NO// \<ENTER\>

AVERAGE DRUG COST: \<ENTER\>

INACTIVATION DATE: \<ENTER\>

USED IN IV FLUID ORDER ENTRY: YES// \<ENTER\>

PREMIX: YES//

  
*(This page included for two-sided copying.)*

# Chapter 5 – Enter/Edit Additive Frequency for IV Additives

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To facilitate accurate daily dose checking for a continuous IV Solution with IV Additives, the software must calculate the amount of an IV Additive that is administered to a patient over a 24 hour period of time. In order to capture that information at the time the provider enters the IV order through the CPRS Continuous IV Dialog software changes were required. PSS\*1.0\*147 creates a new ADDITIVE FREQUENCY (#18) field in the IV ADDITIVES (#52.6) file to provide a default value for a new Additive Frequency field in Computerized Patient Record System (CPRS) when an IV Additive for a continuous IV order is entered. These defaults will not start to appear in CPRS

until Pharmacy Re-Engineering (PRE) V. 0.5 software is installed.

Data will be auto-populated by a Post-Install routine for patch PSS\*1\*147 based on the following business rules:

- If the dispense drug assigned to the IV Additive has a VA Drug Class code that contains a ‘VT’, the additive frequency for the IV Additive will be set to ‘1 BAG/DAY’.

> (I.e. Multivitamins IV are administered as a single dose)

- If the dispense drug assigned to the IV Additive has a VA Drug Class code that does not contain a ‘VT’, the additive frequency for the IV Additive will be set to ‘All Bags’.
- If the dispense drug assigned to the IV Additive has no VA Drug Class code defined (not match to NDF or not manually classed) the field will be left blank.

A new IV Additive Report \[PSS IV ADDITIVE REPORT\] option has also been added to allow review of the Additive Frequency data. Users should use this report to review the auto populated Additive Frequency data for accuracy/appropriateness. When reviewing the Additive Frequency data use the following as a guideline:

1.  If an IV Additive (i.e. IV Multivitamins) is always administered as a single dose within a 24 hour period, assign ‘1 BAG/DAY’.
2.  If an IV Additive (i.e. Dopamine) is always administered as a continuous infusion and will be placed in all bags for an IV order, assign ‘ALL BAGS’.
3.  If an IV Additive (i.e. Potassium Chloride) may sometimes be administered in all bags or sometimes in only one or two bags of an IV order, leave it blank.

This new field can be edited using the Drug Enter/Edit \[PSS DRUG ENTER/EDIT\] option or the Additives File \[PSSJI DRUG\] stand alone option.

The following bolded options are to be used to review and enter/edit the Additive Frequency for IV Additives.

Select Pharmacy Data Management Option:

CMOP Mark/Unmark (Single drug)

Dosages ...

Drug Enter/Edit

Drug Interaction Management ...

Electrolyte File (IV)

Lookup into Dispense Drug File

Medication Instruction Management ...

Medication Routes Management ...

Orderable Item Management ...

Formulary Information Report

Drug Text Management ...

Pharmacy System Parameters Edit

Standard Schedule Management ...

Synonym Enter/Edit

Controlled Substances/PKI Reports ...

Send Entire Drug File to External Interface

Enhanced Order Checks Setup Menu ...

IV Additive/Solution Reports ...

IV Additive Report

IV Solution Report

Warning Builder

Warning Mapping

This additional option may also be used to enter/edit an Additive Frequency for an IV Additive:

> ADditives File (stand alone option)

The detailed descriptions of the options that follow are presented in the logical sequence to accomplish the file setup, not the order in which they are displayed on the menu.

## IV Additive Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS IV ADDITIVE REPORT\]

The new *IV Additive Report* \[PSS IV ADDITIVE REPORT\] option displays entries in the IV ADDITIVES (#52.6) File. You can select to display only entries marked with '1 BAG/DAY' in the ADDITIVE FREQUENCY (#18) field, or only those entries with nothing entered in the ADDITIVE FREQUENCY (#18) field, or all entries can be displayed. The report will print the following data elements:

- Print Name
- Generic Drug
- Drug Unit
- Synonyms
- Pharmacy Orderable Item
- Inactivation Date
- Used in IV Fluid Order Entry
- Additive Frequency

If the user chooses to print only the IV Additives marked with ‘1 BAG/DAY’ in the Additive Frequency or those entries with nothing entered in the Additive Frequency and none are found, the report will display ‘No IV Additives marked as '1 BAG/DAY' or ‘No IV Additives marked as null’ respectively.

  
User selects only IV Additives marked with ‘1 BAG/DAY’ in the Additive Frequency

Select IV Additive/Solution Reports Option: IV ADditive Report

This report displays entries in the IV ADDITIVES (#52.6) File. You can select

to display only entries marked with '1 BAG/DAY' in the ADDITIVE FREQUENCY (#18)

Field, or only those entries with nothing entered in the ADDITIVE FREQUENCY

(#18) Field, or all entries can be displayed.

Select one of the following:

1 Print entries marked as '1 BAG/DAY' for ADDITIVE FREQUENCY

N Print entries marked as Null for ADDITIVE FREQUENCY

A Print all IV Additives

Print which IV Additives: A// <u>1</u> Print entries marked as '1 BAG/DAY' for ADDITIVE FREQUENCY

This report is designed for 80 column format!

DEVICE: HOME// \<ENTER\>

IV Additives marked as '1 BAG/DAY' for ADDITIVE FREQUENCY Page: 1

------------------------------------------------------------------------------

Print Name: MVI

Drug Unit: ML

Synonyms:

Generic Drug: MULTIVITAMIN 5ML INJ

Pharmacy Orderable Item: MULTIVITAMINS INJ,SOLN

Inactivation Date:

Used in IV Fluid Order Entry: YES

Additive Frequency: 1 BAG/DAY

Print Name: THIAMINE

Drug Unit: MG

Synonyms:

Generic Drug: THIAMINE 100MG/ML INJ 10(ML)

Pharmacy Orderable Item: THIAMINE INJ,SOLN

Inactivation Date:

Used in IV Fluid Order Entry: YES

Additive Frequency: 1 BAG/DAY

End of Report.

User selects only IV Additives marked with no value in the Additive Frequency

Select IV Additive/Solution Reports Option: IV ADditive Report

This report displays entries in the IV ADDITIVES (#52.6) File. You can select

to display only entries marked with '1 BAG/DAY' in the ADDITIVE FREQUENCY (#18)

Field, or only those entries with nothing entered in the ADDITIVE FREQUENCY

(#18) Field, or all entries can be displayed.

Select one of the following:

1 Print entries marked as '1 BAG/DAY' for ADDITIVE FREQUENCY

N Print entries marked as Null for ADDITIVE FREQUENCY

A Print all IV Additives

Print which IV Additives: A// <u>N</u> Print entries marked as Null for ADDITIVE FREQUENCY

This report is designed for 80 column format!

DEVICE: HOME// \<ENTER\>

IV Additives marked as null for ADDITIVE FREQUENCY Page: 1

------------------------------------------------------------------------------

Print Name: CALCIUM GLUCONATE

Drug Unit: MEQ

Synonyms: CAGLUC

Generic Drug: CALCIUM GLUCONATE 1GM

Pharmacy Orderable Item: CALCIUM GLUCONATE INJ,SOLN

Inactivation Date:

Used in IV Fluid Order Entry: YES

Additive Frequency:

Print Name: POTASSIUM CHLORIDE

Drug Unit: MEQ

Synonyms: KCL

Generic Drug: POTASSIUM CL 2MEQ/ML (10ML) INJ

Pharmacy Orderable Item: POTASSIUM CHLORIDE INJ,SOLN

Inactivation Date:

Used in IV Fluid Order Entry: YES

Additive Frequency:

End of Report.

No IV Additives marked with ‘1 BAG/DAY’ in the Additive Frequency

Select IV Additive/Solution Reports Option: IV ADDitive Report

This report displays entries in the IV ADDITIVES (#52.6) File. You can select

to display only entries marked with '1 BAG/DAY' in the ADDITIVE FREQUENCY (#18)

Field, or only those entries with nothing entered in the ADDITIVE FREQUENCY (#18) Field, or all entries can be displayed.

Select one of the following:

1 Print entries marked as '1 BAG/DAY' for ADDITIVE FREQUENCY

N Print entries marked as Null for ADDITIVE FREQUENCY

A Print all IV Additives

Print which IV Additives: A// <u>1</u> Print entries marked as '1 BAG/DAY' for ADDITIVE FREQUENCY

This report is designed for 80 column format!

DEVICE: HOME// \<ENTER\>

IV Additives marked as '1 BAG/DAY' for ADDITIVE FREQUENCY Page: 1

------------------------------------------------------------------------------

No IV Additives marked as '1 BAG/DAY'.

End of Report.

No IV Additives with nothing in the Additive Frequency

Select IV Additive/Solution Reports Option: IV ADditive Report

This report displays entries in the IV ADDITIVES (#52.6) File. You can select

to display only entries marked with '1 BAG/DAY' in the ADDITIVE FREQUENCY (#18)

Field, or only those entries with nothing entered in the ADDITIVE FREQUENCY (#18) Field,

or all entries can be displayed.

Select one of the following:

1 Print entries marked as '1 BAG/DAY' for ADDITIVE FREQUENCY

N Print entries marked as Null for ADDITIVE FREQUENCY

A Print all IV Additives

Print which IV Additives: A// <u>N</u> Print entries marked as Null for ADDITIVE FREQUENCY

This report is designed for 80 column format!

DEVICE: HOME// \<ENTER\>

IV Additives marked as null for ADDITIVE FREQUENCY Page: 1

------------------------------------------------------------------------------

No IV Additives marked as null.

End of Report.

User Selects all IV Additives

Select IV Additive/Solution Reports Option: IV Additive Report

This report displays entries in the IV ADDITIVES (#52.6) File. You can select

to display only entries marked with '1 BAG/DAY' in the ADDITIVE FREQUENCY (#18)

Field, or only those entries with nothing entered in the ADDITIVE FREQUENCY(#18)

Field, or all entries can be displayed.

Select one of the following:

1 Print entries marked as '1 BAG/DAY' for ADDITIVE FREQUENCY

N Print entries marked as Null for ADDITIVE FREQUENCY

A Print all IV Additives

Print which IV Additives: A// \<ENTER\> Print all IV Additives

This report is designed for 80 column format!

DEVICE: HOME// \<ENTER\>

All IV Additives Page: 1

------------------------------------------------------------------------------

Print Name: AMINOPHYLLINE

Drug Unit: MG

Synonyms:

Generic Drug: AMINOPHYLLINE 25MG/ML 20ML INJ

Pharmacy Orderable Item: AMINOPHYLLINE INJ,SOLN

Inactivation Date:

Used in IV Fluid Order Entry: YES

Additive Frequency: ALL BAGS

Print Name: CALCIUM GLUCONATE

Drug Unit: MEQ

Synonyms: CAGLUC

Generic Drug: CALCIUM GLUCONATE 1GM

Pharmacy Orderable Item: CALCIUM GLUCONATE INJ,SOLN

Inactivation Date:

Used in IV Fluid Order Entry: YES

Additive Frequency:

Print Name: HEPARIN

Drug Unit: UNITS

Synonyms:

Generic Drug: HEPARIN 10,000 UNITS 4ML

Pharmacy Orderable Item: HEPARIN INJ,SOLN

Inactivation Date:

Used in IV Fluid Order Entry: YES

Additive Frequency: ALL BAGS

Print Name: TRACE ELEMENTS

Drug Unit: ML

Synonyms:

Generic Drug: TRACE ELEMENTS 5ML INJ

Pharmacy Orderable Item: TRACE ELEMENTS INJ,CONC-SOLN

Inactivation Date:

Used in IV Fluid Order Entry: YES

Additive Frequency: 1 BAG/DAY

End of Report.

## Drug Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS DRUG ENTER/EDIT\]

The *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option allows a user to enter/edit an Additive Frequency for an IV Additive.

Select Pharmacy Data Management Option: Drug Enter/Edit

Select DRUG GENERIC NAME: CIMETIDINE 150MG/ML MDV INJ (8ML) GA301

...OK? Yes// \<ENTER\> (Yes)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This entry is marked for the following PHARMACY packages:

IV

Ward Stock

GENERIC NAME: CIMETIDINE 150MG/ML MDV INJ (8ML) Replace \<ENTER\>

VA CLASSIFICATION: GA301// \<ENTER\>

DEA, SPECIAL HDLG: \<ENTER\>

DAW CODE: \<ENTER\>

.

.

.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This entry is marked for the following PHARMACY packages:

IV

Ward Stock

MARK THIS DRUG AND EDIT IT FOR:

O - Outpatient

U - Unit Dose

I - IV

W - Ward Stock

D - Drug Accountability

C - Controlled Substances

X - Non-VA Med

A - ALL

Enter your choice(s) separated by commas : I

I - IV

\*\* You are NOW editing IV fields. \*\*

AN IV ITEM? Yes// \<ENTER\> (Yes)

Edit Additives or Solutions:

Select one of the following:

A ADDITIVES

S SOLUTIONS

Enter response: ADDITIVES

Select IV SOLUTIONS PRINT NAME: CIMETIDINE

PRINT NAME: CIMETIDINE// \<ENTER\>

GENERIC DRUG: CIMETIDINE 150MG/ML MDV INJ (8ML)// \<ENTER\>

USED IN IV FLUID ORDER ENTRY: YES// \<ENTER\>

DRUG UNIT: MG// \<ENTER\>

NUMBER OF DAYS FOR IV ORDER: \<ENTER\>

USUAL IV SCHEDULE: \<ENTER\>

ADMINISTRATION TIMES: \<ENTER\>

Select QUICK CODE: \<ENTER\>

AVERAGE DRUG COST PER UNIT: \<ENTER\>

Select ELECTROLYTE: \<ENTER\>

Select SYNONYM: \<ENTER\>

DRUG INFORMATION: \<ENTER\>

1\>

INACTIVATION DATE: \<ENTER\>

CONCENTRATION: \<ENTER\>

MESSAGE: \<ENTER\>

ADDITIVE FREQUENCY: ALL BAGS// \<ENTER\>

Edit Additives or Solutions: \<ENTER\>

Select one of the following:

A ADDITIVES

S SOLUTIONS

Enter response:

Additives File \[PSSJI DRUG\]

The *Additives File* \[PSSJI DRUG\] stand alone option is modified to allow a user to enter/edit an Additive Frequency for an IV Additive.

Select OPTION NAME: ADDITIVES FILE PSSJI DRUG ADditives File

ADditives File

You are signed on under the GLRISC IV ROOM

Current IV LABEL device is: TELNET

Current IV REPORT device is: TELNET

Select IV ADDITIVES PRINT NAME: CEFAZOLIN

PRINT NAME: CEFAZOLIN//

GENERIC DRUG: CEFAZOLIN SOD 1GM INJ// \<ENTER\>

USED IN IV FLUID ORDER ENTRY: YES// \<ENTER\>

DRUG UNIT: GM// \<ENTER\>

NUMBER OF DAYS FOR IV ORDER: 10// \<ENTER\>

USUAL IV SCHEDULE: Q8H// \<ENTER\>

ADMINISTRATION TIMES: \<ENTER\>

Select QUICK CODE: CEF2Q6H// \<ENTER\>

QUICK CODE: CEF2Q6H// \<ENTER\>

STRENGTH: 2 GM// \<ENTER\>

USUAL INFUSION RATE: OVER 30 MINUTES// \<ENTER\>

OTHER PRINT INFO: REFRIGERATE// \<ENTER\>

USUAL IV SCHEDULE: Q8H// \<ENTER\>

ADMINISTRATION TIMES: 06-14-22// \<ENTER\>

USUAL IV SOLUTION: 0.9% SODIUM CHLORIDE 100 ML// \<ENTER\>

MED ROUTE: IV PIGGYBACK// \<ENTER\>

Select QUICK CODE: \<ENTER\>

AVERAGE DRUG COST PER UNIT: 2.31// \<ENTER\>

Select ELECTROLYTE: \<ENTER\>

Select SYNONYM: ANCEF// \<ENTER\>

DRUG INFORMATION: \<ENTER\>

1\>

INACTIVATION DATE: \<ENTER\>

CONCENTRATION: \<ENTER\>

MESSAGE: \<ENTER\>

ADDITIVE FREQUENCY: ALL BAGS// \<ENTER\>*Page included for two-sided copying*

# Appendix A: Standard Medication Routes File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The file on your system will have more entries than are listed here. There have been additions pushed out by the New Term Rapid Turnaround (NTRT) process since the release of this patch. To get a complete listing, do a FileMan print for the NAME (#.01) and FIRST DATABANK MED ROUTE (#1) fields in the STANDARD MEDICATION ROUTES file (#51.23).

|                                        |                     |
|----------------------------------------|---------------------|
| Standard VA Medication Routes Name | FDB Route       |
| BUCCAL                                 | BUCCAL              |
| DENTAL                                 | DENTAL              |
| EPIDURAL                               | EPIDURAL            |
| INHALATION                             | INHALATION          |
| INTRA-ARTERIAL                         | INTRA-ARTERIAL      |
| INTRA-ARTICULAR                        | INTRA-ARTICULAR     |
| INTRACARDIAC                           | INTRACARDIAC        |
| INTRACAVERNOSAL                        | INTRA-CAVERNOSAL    |
| INTRADERMAL                            | INTRADERMAL         |
| INTRALESIONAL                          | INTRALESIONAL       |
| INTRAMUSCULAR                          | INTRAMUSCULAR       |
| INTRAOCULAR                            | INTRAOCULAR         |
| INTRAPERITONEAL                        | INTRAPERITONEAL     |
| INTRAPLEURAL                           | INTRAPLEURAL        |
| INTRATHECAL                            | INTRATHECAL         |
| INTRATRACHEAL                          | INTRATRACHEAL       |
| INTRAVENOUS                            | INTRAVENOUS         |
| INTRAVESICAL                           | INTRAVESICAL        |
| IRRIGATION                             | IRRIGATION          |
| NASAL                                  | INTRANASAL          |
| NEBULIZATION                           | NEBULIZATION-UNSPEC |
| OPHTHALMIC                             | OPHTHALMIC          |
| ORAL                                   | ORAL                |
| OTIC                                   | OTIC                |
| RECTAL                                 | RECTAL              |
| SUBCUTANEOUS                           | SUBCUTANEOUS        |
| SUBLINGUAL                             | SUBLINGUAL          |
| TOPICAL                                | TOPICAL             |
| TRANSDERMAL                            | TRANSDERMAL         |
| URETHRAL                               | INTRA-URETHRAL      |
| VAGINAL                                | VAGINAL             |

*Page included for two-sided copying*

# Appendix B: New DOSE UNITS File with FDB mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The file on your system may have more entries than are listed here. To get a complete listing, do a FileMan print for the NAME (#.01), FIRST DATABANK DOSE UNIT (#1),

DOSE FORM INDICATOR (#3) and SYNONYM (#2) fields in the DOSE UNITS file (#51.24)

| DOSE UNIT NAME | SYNONYM      | MAP TO FDB DOSE UNIT | DOSE FORM INDICATOR |
|--------------------|------------------|--------------------------|-------------------------|
| anti-Xa unit       | aXa IU           | AXA IU                   | N                       |
|                    | aXa unit         |                          |                         |
|                    | AXA IU           |                          |                         |
|                    | antiXA unit      |                          |                         |
|                    | ANTI-XA UNIT     |                          |                         |
|                    | AXA UNIT         |                          |                         |
|                    | ANTIXA UNIT      |                          |                         |
| APPLICATION(S)     | APPLICATIONS     | APPLICATION(S)           | Y                       |
|                    | APPLICATION      |                          |                         |
| APPLICATORFUL(S)   | APPFUL           | APPLICATORFUL/S          | Y                       |
|                    | APPLICATORFUL/S  |                          |                         |
|                    | APPLICATOR       |                          |                         |
|                    | APPLICATORFUL    |                          |                         |
|                    | APPLICATORFULS   |                          |                         |
|                    | APPLICATORS      |                          |                         |
| BAR(S)             | BAR              | BARS                     | Y                       |
|                    | BARS             |                          |                         |
| CAP/TAB            | TAB-CAPS         | TAB-CAPS                 | Y                       |
|                    | TAB-CAP          |                          |                         |
|                    | TAB/CAP          |                          |                         |
| CAPLET(S)          | CAPLET           | CAPLETS                  | Y                       |
|                    | CAPLETS          |                          |                         |
| CAPSULE(S)         | CAP              | CAPSULE(S)               | Y                       |
|                    | CAPS             |                          |                         |
|                    | CAPSULE          |                          |                         |
|                    | CAPSULES         |                          |                         |
| CENTIMETER(S)      | CENTIMETER       | CENTIMETERS              | Y                       |
|                    | CM               |                          |                         |
|                    | CMS              |                          |                         |
|                    | CENTIMETERS      |                          |                         |
| DROP(S)            | DROP             | DROP(S)                  | Y                       |
|                    | DROPS            |                          |                         |
|                    | DRP              |                          |                         |
|                    | DRPS             |                          |                         |
|                    | GTT              |                          |                         |
|                    | GTTS             |                          |                         |
| EACH               | EA               | EACH                     | Y                       |
|                    | EACHES           |                          |                         |
| ENEMA(S)           | ENEMA            | ENEMAS                   | Y                       |
|                    | ENEMAS           |                          |                         |
| GRAM(S)            | G                | GRAMS                    | N                       |
|                    | GM               |                          |                         |
|                    | GMS              |                          |                         |
|                    | GRAM             |                          |                         |
|                    | GRAMS            |                          |                         |
| IMPLANT(S)         | IMPLANT          | IMPLANTS                 | Y                       |
|                    | IMPLANTS         |                          |                         |
| INCH(ES)           | IN               | INCH(ES)                 | Y                       |
|                    | INCH             |                          |                         |
|                    | INCHES           |                          |                         |
| INHALATION(S)      | INH              | INHALATIONS              | Y                       |
|                    | INHALATION       |                          |                         |
|                    | INHL             |                          |                         |
|                    | INHALATIONS      |                          |                         |
| INSERT(S)          | INSERT           | INSERTS                  | Y                       |
|                    | INSERTS          |                          |                         |
| LITER(S)           | L                | LITERS                   | Y                       |
|                    | LITER            |                          |                         |
|                    | LITERS           |                          |                         |
|                    | LITRE(S)         |                          |                         |
| LOZENGE(S)         | LOZENGE          | LOZENGES                 | Y                       |
|                    | LOZENGES         |                          |                         |
| MG-PE              | MG PE            | MG PE                    | N                       |
| MICRO UNIT(S)      | MICRO UNIT       | MICRO UNITS              | N                       |
|                    | MICRO UNITS      |                          |                         |
|                    | MICROUNIT        |                          |                         |
|                    | MICROUNITS       |                          |                         |
| MICROGRAM(S)       | MCG              | MICROGRAM(S)             | N                       |
|                    | MCGS             |                          |                         |
|                    | MICROGRAM        |                          |                         |
|                    | MICROGRAMS       |                          |                         |
| MILLIEQUIVALENT(S) | MILLIEQUIVALENT  | MILLIEQUIVALENTS         | N                       |
|                    | MILLIEQUIVALENTS |                          |                         |
|                    | MEQ              |                          |                         |
|                    | MEQS             |                          |                         |
| MILLIGRAM(S)       | MGS              | MILLIGRAMS               | N                       |
|                    | MILLIGRAM        |                          |                         |
|                    | MILLIGRAMS       |                          |                         |
|                    | MG               |                          |                         |
| MILLILITER(S)      | MILLILITER       | MILLILITERS              | Y                       |
|                    | MILLILITERS      |                          |                         |
|                    | MILILITERS       |                          |                         |
|                    | MILILITER        |                          |                         |
|                    | ML               |                          |                         |
|                    | MLS              |                          |                         |
|                    | CC               |                          |                         |
|                    | CCS              |                          |                         |
| MILLIMOLE(S)       | MILLIMOL         | MILLIMOLES               | N                       |
|                    | MILLIMOLE        |                          |                         |
|                    | MILLIMOLES       |                          |                         |
|                    | MILLIMOLS        |                          |                         |
|                    | MM               |                          |                         |
|                    | MMOL             |                          |                         |
|                    | MMOLE            |                          |                         |
|                    | MMOLES           |                          |                         |
|                    | MMOLS            |                          |                         |
| MILLIONUNIT(S)     | MILI U           | MILLIONUNIT(S)           | N                       |
|                    | MILI UNIT        |                          |                         |
|                    | MILI UNITS       |                          |                         |
|                    | MILU             |                          |                         |
|                    | MIU              |                          |                         |
|                    | MU               |                          |                         |
|                    | MILLION UNT      |                          |                         |
| NANOGRAM(S)        | NANOGRAM         | NANOGRAMS                | N                       |
|                    | NANOGRAMS        |                          |                         |
|                    | NG               |                          |                         |
|                    | NGS              |                          |                         |
| OVULE(S)           | OVULE            | OVULE(S)                 | Y                       |
|                    | OVULES           |                          |                         |
| PACKAGE(S)         | PACKAGE          | PACKAGES                 | Y                       |
|                    | PACKAGES         |                          |                         |
|                    | PKGS             |                          |                         |
|                    | PKG              |                          |                         |
| PACKET(S)          | PACKET           | PACKETS                  | Y                       |
|                    | PACKETS          |                          |                         |
| PAD(S)             | PAD              | PADS                     | Y                       |
|                    | PADS             |                          |                         |
| PATCH(ES)          | PATCH            | PATCHES                  | Y                       |
|                    | PATCHES          |                          |                         |
| PELLET(S)          | PELLET           | PELLETS                  | Y                       |
|                    | PELLETS          |                          |                         |
| PIECE(S)           | PIECE            | PIECE(S)                 | Y                       |
|                    | PIECE OF GUM     |                          |                         |
|                    | PIECES           |                          |                         |
|                    | PIECES OF GUM    |                          |                         |
| PUFF(S)            | PUFF             | PUFF(S)                  | Y                       |
|                    | PUFFS            |                          |                         |
| SACHET(S)          | SACHET           | SACHETS                  | Y                       |
|                    | SACHETS          |                          |                         |
| SCOOPFUL(S)        | SCOOP            | SCOOPFULS                | Y                       |
|                    | SCOOPFUL         |                          |                         |
|                    | SCOOPFULS        |                          |                         |
|                    | SCOOPS           |                          |                         |
|                    | SCOOPSFUL        |                          |                         |
|                    | SCP              |                          |                         |
| SPRAY(S)           | SPR              | SPRAY(S)                 | Y                       |
|                    | SPRAY            |                          |                         |
|                    | SPRAYS           |                          |                         |
| SQUIRT(S)          | SQUIRT           | SQUIRTS                  | Y                       |
|                    | SQUIRTS          |                          |                         |
| STRIP(S)           | STRIP            | STRIP(S)                 | Y                       |
|                    | STRIPS           |                          |                         |
| SUPPOSITOR(IES)    | SUPP             | SUPPOSITORY/IES          | Y                       |
|                    | SUPPOSITORIES    |                          |                         |
|                    | SUPPOSITORY      |                          |                         |
| TABLESPOONFUL(S)   | TABLESPOONFUL    | TABLESPOONFULS           | Y                       |
|                    | TABLESPOONFULS   |                          |                         |
| TABLET(S)          | TABLET           | TABLET(S)                | Y                       |
|                    | TABLETS          |                          |                         |
|                    | TABS             |                          |                         |
|                    | TAB              |                          |                         |
| TEASPOONFUL(S)     | TEASPOONFUL      | TEASPOONFULS             | Y                       |
|                    | TEASPOONFULS     |                          |                         |
| THOUSAND UNITS     | THOUU            | TU                       | N                       |
|                    | TU               |                          |                         |
| TROCHE(S)          | TROCHE           | TROCHES                  | Y                       |
|                    | TROCHES          |                          |                         |
| UNIT(S)            | U                | UNIT(S)                  | N                       |
|                    | UNIT             |                          |                         |
|                    | UNITS            |                          |                         |
|                    | UNT              |                          |                         |
|                    | UNTS             |                          |                         |
|                    | IU               |                          |                         |
| VAGINAL INSERT     | VAGINAL INSERTS  | VAGINAL INSERT           | Y                       |
| VAGINAL RING       | VAG RING         | VAGINAL RING             | Y                       |
|                    | VAG RINGS        |                          |                         |
|                    | VAGINAL RINGS    |                          |                         |
| VIAL(S)            | VIAL             | VIALS                    | Y                       |
|                    | VIALS            |                          |                         |
|                    | VIL              |                          |                         |
| WAFER(S)           | WAFER            | WAFERS                   | Y                       |
|                    | WAFERS           |                          |                         |

# # Appendix C: List of Dosage Forms to Exclude from Dosage Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The file on your system may have more entries than are listed here. To get a complete listing, do a FileMan print for the NAME (#.01) field in the DOSAGE FORM file (#50.606). Only print those entries that have the EXCLUDE FROM DOSAGE CHECKS field (#11) set to ‘YES’.

| Dosage Forms to Exclude from Dosage Checks |                               |     |                   |
|------------------------------------------------|-------------------------------|-----|-------------------|
| ACCESS PIN                                     | GLOVE                         |     | PUDDING           |
| ADAPTER                                        | GLVOE                         |     | PUMP              |
| AEROSOL                                        | GRAFT,TOP                     |     | PWDR,RENST-IRRG   |
| AEROSOL,RTL                                    | GRANULES                      |     | PWDR,RENST-TOP    |
| AEROSOL,TOP                                    | INJ/TAB                       |     | RINSE,ORAL        |
| AEROSOL,VAG                                    | IRRIGATION SET                |     | SET               |
| APPLICATOR                                     | IRRIGATION SLEEVE             |     | SET,INFUSION      |
| BAG                                            | IRRIGATOR                     |     | SHAMPOO           |
| BANDAGE                                        | IUD                           |     | SOAP/DETERGENT    |
| BAR,CHEWABLE                                   | JELLY                         |     | SOLN              |
| BAR,TOP                                        | JELLY,NASAL                   |     | SOLN,CONTACT LENS |
| BARRIER                                        | JELLY,TOP                     |     | SOLN,CONTROL      |
| BEADS,TOP                                      | JELLY,VAG                     |     | SOLN,DENTAL       |
| BELT                                           | KIT                           |     | SOLN,DIALYSIS     |
| BLOCK                                          | LANCET                        |     | SOLN,IRRG         |
| CANNULA                                        | LENS,HARD                     |     | SOLN,ITRC         |
| CAP,IRRIGATION                                 | LENS,SOFT                     |     | SOLN,OPH IRRG     |
| CAP/INJ                                        | LINIMENT                      |     | SOLN,TOP          |
| CATHETER                                       | LIQUID,AEROSOL                |     | SOLN,URH          |
| CHAMBER                                        | LIQUID,DENT                   |     | SPIRIT            |
| CLAMP                                          | LIQUID,NUTRITIONAL SUPPLEMENT |     | SPONGE            |
| COLLAR                                         | LIQUID,OPH                    |     | SPRAY,ORAL        |
| CONE                                           | LIQUID,RTL                    |     | SPRAY,TOP         |
| CONTAINER                                      | LIQUID,TOP                    |     | STICK             |
| CONVEX INSERT                                  | LIQUID,VAG                    |     | STICK,TOP         |
| CREAM                                          | LOTION                        |     | STOCKING          |
| CREAM,ORAL                                     | LOTION,TOP                    |     | STOMA CAP         |
| CREAM,OTIC                                     | MAGMA                         |     | STOMA CONE        |
| CREAM,RTL                                      | MASK                          |     | STRIP             |
| CREAM,TOP                                      | MCG/0.4ML                     |     | STRIP,OPH         |
| CREAM,VAG                                      | MILK                          |     | SUPP/CR/LOTION    |
| CREAM/TAB,VAG                                  | MISCELLANEOUS                 |     | SUSP,TOP          |
| CRUSHER                                        | MOUTHWASH                     |     | SUTURE            |
| CRYSTAL                                        | NEEDLE                        |     | SWAB,TOP          |
| DENTAL CONE                                    | NUTRACEUTICAL                 |     | SYRINGE           |
| DEVICE                                         | OIL                           |     | SYRINGE/NDL       |
| DIAPHRAGM                                      | OIL,TOP                       |     | TAB,EFFERVSC,TOP  |
| DISK                                           | OINT,DENT                     |     | TAB,NOT ORAL      |
| DOUCHE                                         | OINT,OPH                      |     | TAB,ORAL/VAG      |
| DRAIN                                          | OINT,RTL                      |     | TAB,TEST          |
| DRESSING                                       | OINT,TOP                      |     | TAB/SUPP          |
| DRESSING,TOP                                   | OINT,VAG                      |     | TAMPON            |
| EMULSION,TOP                                   | OINT/SUSP                     |     | TAPE              |
| EXTRACT                                        | OINTMENT                      |     | TEA               |
| FACEPLATE                                      | OPH IRR                       |     | TEST STRIP        |
| FILM                                           | PAD                           |     | TINCTURE          |
| FILM,CONT REL                                  | PAD,TOP                       |     | TINCTURE,TOP      |
| FLANGE CAP                                     | PASTE                         |     | TOOTHPASTE        |
| FLUFF                                          | PLASTER,TOP                   |     | TOOTHPOWDER       |
| FLUID EXTRACT                                  | POUCH                         |     | TUBE              |
| FOAM,TOP                                       | POUCH COVER                   |     | UNIT/TEST         |
| GAS                                            | POULTICE                      |     | VIAL              |
| GAUZE                                          | POWDER                        |     | WAFER             |
| GEL                                            | POWDER,AEROSOL                |     | WAFER,TOP         |
| GEL,DENT                                       | POWDER,INTRAPLEURAL           |     | WASHER            |
| GEL,NASAL                                      | POWDER,RTL                    |     | WAX               |
| GEL,ORAL                                       | POWDER,SPRAY                  |     | WIPE              |
| GEL,TOP                                        | POWDER,VAG                    |     |                   |
| GEL,VAG                                        | POWDER,TOP                    |     |                   |

# # Appendix D: VA Products with OVERRIDE DF DOSE CHK EXCLUSION field set to ‘Yes’

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The file on your system may have more entries than are listed here. To get a complete listing, do a FileMan print for the NUMBER, NAME (#.01), and DOSAGE FORM (#1) fields in the VA PRODUCT file (#50.68) and the EXCLUDE FROM DOSAGE CHECKS field (#11) in the DOSAGE FORM file (#50.606). Only print those entries that have the OVERRIDE DF DOSE CHK EXCLUSION field (#31) in the VA PRODUCT file (#50.68) set to ‘YES’. Sort the list by DOSAGE FORM and within DOSAGE FORM by NAME.

| DOSAGE FORM     | IEN | VA PRODUCT NAME                                              | DF Excluded (Y/N) |
|---------------------|---------|------------------------------------------------------------------|-----------------------|
| BAR,CHEWABLE    | 7994    | CHOLESTYRAMINE 4GM BAR,CHEWABLE                                  | Y                     |
| CAP,ORAL        | 3402    | CYANOCOBALAMIN (CO-57) 0.5MIC CAP                                | N                     |
| CAP,ORAL        | 9149    | EMPTY GELATIN CAP,CLEAR SZ 0                                     | N                     |
| CAP,ORAL        | 9148    | EMPTY GELATIN CAP,CLEAR SZ 00                                    | N                     |
| CAP,ORAL        | 9147    | EMPTY GELATIN CAP,CLEAR SZ 000                                   | N                     |
| CAP,ORAL        | 9150    | EMPTY GELATIN CAP,CLEAR SZ 1                                     | N                     |
| CAP,ORAL        | 9151    | EMPTY GELATIN CAP,CLEAR SZ 2                                     | N                     |
| CAP,ORAL        | 9152    | EMPTY GELATIN CAP,CLEAR SZ 3                                     | N                     |
| CAP,ORAL        | 9153    | EMPTY GELATIN CAP,CLEAR SZ 4                                     | N                     |
| CAP,ORAL        | 1137    | IPODATE NA 500MG CAP                                             | N                     |
| CAP,ORAL        | 6350    | LACTOSE 100% CAP                                                 | N                     |
| CAP,ORAL        | 6348    | LACTOSE 200MG CAP                                                | N                     |
| CAP,ORAL        | 6349    | LACTOSE 250MG CAP                                                | N                     |
| CAP,ORAL        | 7486    | SODIUM IODIDE,I-123,100MIC CAP                                   | N                     |
| CAP,ORAL        | 7488    | SODIUM IODIDE,I-123,200MIC CAP                                   | N                     |
| CAP,ORAL        | 923     | SODIUM IODIDE,I-131,100MIC CAP                                   | N                     |
| CAP,ORAL        | 920     | SODIUM IODIDE,I-131,15MIL CAP                                    | N                     |
| CAP,ORAL        | 922     | SODIUM IODIDE,I-131,1MIL CAP                                     | N                     |
| CAP,ORAL        | 917     | SODIUM IODIDE,I-131,50MIL CAP                                    | N                     |
| CAP,ORAL        | 918     | SODIUM IODIDE,I-131,8-100MIC CAP                                 | N                     |
| CAP,SA          | 1138    | IPODATE NA 500MG CAP,SA                                          | N                     |
| ELIXIR          | 9543    | AROMATIC ELIXIR                                                  | N                     |
| ELIXIR          | 9566    | AROMATIC ELIXIR                                                  | N                     |
| ELIXIR          | 9655    | AROMATIC ELIXIR                                                  | N                     |
| ENEMA           | 3445    | BARIUM SO4 64.4% ENEMA                                           | N                     |
| ENEMA           | 3444    | BARIUM SO4 55% ENEMA                                             | N                     |
| ENEMA           | 3443    | BARIUM SO4 70% ENEMA                                             | N                     |
| FLUID EXTRACT   | 7928    | CASCARA SAGRADA 1GM/ML FLUID EXTRACT,ORAL                        | Y                     |
| GEL,RTL         | 17015   | HEMORRHOIDAL GEL,RTL                                             | N                     |
| GRANULES        | 6635    | CITRIC ACID 1.5GM/SIMETHICONE/NA BICARB 2GM/PKT PWDR             | Y                     |
| GRANULES        | 7434    | CITRIC ACID 1GM/POTASSIUM CITRATE 3.3GM/PKT PWDR                 | Y                     |
| GRANULES        | 6634    | CITRIC ACID 2.3GM/SIMETHICONE 0.3GM/NA BICARB 3.1GM/PKT GRANULES | Y                     |
| GRANULES        | 12610   | FOSFOMYCIN TROMETHAMINE 3GM GRANULES SACHET                      | Y                     |
| GRANULES        | 7945    | LACTOBACILLUS 1GM/PKT GRANULES                                   | Y                     |
| GRANULES        | 9024    | LECITHIN GRANULES                                                | Y                     |
| GRANULES        | 348     | MAGNESIUM SULFATE GRANULES                                       | Y                     |
| GRANULES        | 19872   | MONTELUKAST NA 4MG/PKT GRANULES                                  | Y                     |
| GRANULES        | 9095    | PSYLLIUM 2.5GM/SUCROSE 2.4GM/5GM GRANULES                        | Y                     |
| GRANULES        | 8384    | SENNA CONC 326MG/5GM GRANULES                                    | Y                     |
| GRANULES        | 15882   | SENNOSIDES 15MG/5GM GRANULES                                     | Y                     |
| INHALANT        | 5745    | METHOXYFLURANE 99.9% INHL                                        | N                     |
| INHALANT        | 5746    | METHOXYFLURANE INHL                                              | N                     |
| INHL,NASAL      | 9346    | ETHER                                                            | N                     |
| INHL,NASAL      | 14931   | NITRIC OXIDE 100PPM GAS                                          | N                     |
| INHL,NASAL      | 14930   | NITRIC OXIDE 800PPM GAS                                          | N                     |
| INJ             | 7721    | ACCU-BLOC PERIFIX CONTINUOUS EPIDURAL ANESTHESIA                 | N                     |
| INJ             | 3720    | ACCU-BLOC PERIFIX CUSTOM EPIDURAL ANESTHESIA                     | N                     |
| INJ             | 7716    | ACCU-BLOC PERIFIX CUSTOM EPIDURAL ANESTHESIA                     | N                     |
| INJ             | 7718    | ACCU-BLOC PERIFIX CUSTOM EPIDURAL ANESTHESIA                     | N                     |
| INJ             | 7722    | ACCU-BLOC PERIFIX CUSTOM EPIDURAL ANESTHESIA                     | N                     |
| INJ             | 7740    | ACCU-BLOC PERIFIX CUSTOM EPIDURAL ANESTHESIA                     | N                     |
| INJ             | 7738    | ACCU-BLOC SPINOCAN CUSTOM SPINAL TRAY SSK                        | N                     |
| INJ             | 3843    | ACCUGUIDE CENTRAL VENOUS CATHETER KIT C1606AX                    | N                     |
| INJ             | 7728    | ACCUGUIDE CENTRAL VENOUS CATHETER KIT C1608MC                    | N                     |
| INJ             | 3326    | ALBUMIN,AGGREGATED 0.03% (STERILE DILUENT) INJ                   | N                     |
| INJ             | 925     | ALBUMIN,CHROMATED SERUM,CR-51 50MCG/ML INJ                       | N                     |
| INJ             | 906     | ALBUMIN,IODINATED,I-131,SERUM 10MG/ML INJ                        | N                     |
| INJ             | 7785    | ALLERGENIC EXT,AGARICUS CAMPESTRIS 800MCG/ML INJ                 | N                     |
| INJ             | 6773    | ALLERGENIC EXT,ALTERNARIA ALTERNATA 800MCG/ML INJ                | N                     |
| INJ             | 7786    | ALLERGENIC EXT,CALVATIA CYANTHIFORMIS 800MCG/ML INJ              | N                     |
| INJ             | 7787    | ALLERGENIC EXT,CLADOSPORIUM CLADOSPORIS 800MCG/ML INJ            | N                     |
| INJ             | 7788    | ALLERGENIC EXT,COPRINUS MICACEUS 800MCG/ML INJ                   | N                     |
| INJ             | 7789    | ALLERGENIC EXT,FULIGO SEPTICA 800MCG/ML INJ                      | N                     |
| INJ             | 7790    | ALLERGENIC EXT,LYCOPERDON PYRIFORME 800MCG/ML INJ                | N                     |
| INJ             | 7791    | ALLERGENIC EXT,PENICILLIUM FREQUENTANS 800MCG/ML INJ             | N                     |
| INJ             | 7792    | ALLERGENIC EXT,USTILAGO MAYDIS 800MCG/ML INJ                     | N                     |
| INJ             | 3896    | ALLERGENIC EXTRACT, 10 TREE MIX 10000 PNU/ML INJ                 | N                     |
| INJ             | 3897    | ALLERGENIC EXTRACT, 10 TREE MIX 20000 PNU/ML INJ                 | N                     |
| INJ             | 3863    | ALLERGENIC EXTRACT, 2 GRASS MIX 10000PNU/ML INJ                  | N                     |
| INJ             | 3864    | ALLERGENIC EXTRACT, 2 GRASS MIX 20000PNU/ML INJ                  | N                     |
| INJ             | 3868    | ALLERGENIC EXTRACT, 3 GRASS MIX, SOUTHERN 10000PNU/ML INJ        | N                     |
| INJ             | 3869    | ALLERGENIC EXTRACT, 3 GRASS, SOUTHERN 20000PNU/ML INJ            | N                     |
| INJ             | 3938    | ALLERGENIC EXTRACT, 4 MOLD MIX 10000PNU/ML INJ                   | N                     |
| INJ             | 3865    | ALLERGENIC EXTRACT, 7 GRASS MIX 10000PNU/ML INJ                  | N                     |
| INJ             | 3866    | ALLERGENIC EXTRACT, 7 GRASS MIX 20000PNU/ML INJ                  | N                     |
| INJ             | 3894    | ALLERGENIC EXTRACT, 7 TREE MIX 10000 PNU/ML INJ                  | N                     |
| INJ             | 3895    | ALLERGENIC EXTRACT, 7 TREE MIX 20000PNU/ML INJ                   | N                     |
| INJ             | 3867    | ALLERGENIC EXTRACT, 9 GRASS MIX, SOUTHERN 10000PNU/ML INJ        | N                     |
| INJ             | 4010    | ALLERGENIC EXTRACT, ANTIGENS, MIXED INJ                          | N                     |
| INJ             | 3900    | ALLERGENIC EXTRACT, BIRCH 10000PNU/ML INJ                        | N                     |
| INJ             | 3956    | ALLERGENIC EXTRACT, BLUEGRASS, ANNUAL 10000PNU/ML INJ            | N                     |
| INJ             | 3957    | ALLERGENIC EXTRACT, BLUEGRASS, CANADA 10000PNU/ML INJ            | N                     |
| INJ             | 3927    | ALLERGENIC EXTRACT, CAT EPITHELIA 10000PNU/ML INJ                | N                     |
| INJ             | 4006    | ALLERGENIC EXTRACT, CAT EPITHELIUM 20000PNU/ML INJ               | N                     |
| INJ             | 3928    | ALLERGENIC EXTRACT, CATTLE EPITHELIA 20000PNU/ML INJ             | N                     |
| INJ             | 3993    | ALLERGENIC EXTRACT, CLADOSPORIUM HERBARUM 10000PNU/ML INJ        | N                     |
| INJ             | 3960    | ALLERGENIC EXTRACT, CORN 10000PNU/ML INJ                         | N                     |
| INJ             | 3929    | ALLERGENIC EXTRACT, DOG EPITHELIA 10000PNU/ML INJ                | N                     |
| INJ             | 3930    | ALLERGENIC EXTRACT, DOG EPITHELIA 20000PNU/ML INJ                | N                     |
| INJ             | 3970    | ALLERGENIC EXTRACT, FALSE RAGWEED 10000PNU/ML INJ                | N                     |
| INJ             | 3971    | ALLERGENIC EXTRACT, FALSE RAGWEED 20000PNU/ML INJ                | N                     |
| INJ             | 3925    | ALLERGENIC EXTRACT, FEATHER MIX 10000PNU/ML INJ                  | N                     |
| INJ             | 3926    | ALLERGENIC EXTRACT, FEATHER MIX 20000PNU/ML INJ                  | N                     |
| INJ             | 3933    | ALLERGENIC EXTRACT, FUNGI, ASPERGILLUS FUMIGATUS 10000PNU/ML INJ | N                     |
| INJ             | 3934    | ALLERGENIC EXTRACT, FUNGI, CANDIDA ALBICANS 10000PNU/ML INJ      | N                     |
| INJ             | 3990    | ALLERGENIC EXTRACT, GRAIN MILL DUST 10000PNU INJ                 | N                     |
| INJ             | 3991    | ALLERGENIC EXTRACT, GRAIN MILL DUST 20000PNU/ML INJ              | N                     |
| INJ             | 4014    | ALLERGENIC EXTRACT, GRASS, 7 MIX INJ                             | N                     |
| INJ             | 4013    | ALLERGENIC EXTRACT, GRASS, 9 SOUTHERN                            | N                     |
| INJ             | 3870    | ALLERGENIC EXTRACT, GRASS, BERMUDA 10000PNU/ML INJ               | N                     |
| INJ             | 3958    | ALLERGENIC EXTRACT, GRASS, BROME 10000PNU/ML INJ                 | N                     |
| INJ             | 3872    | ALLERGENIC EXTRACT, GRASS, JOHNSON 10000PNU/ML INJ               | N                     |
| INJ             | 3873    | ALLERGENIC EXTRACT, GRASS, KENTUCKY BLUE 10000PNU/ML INJ         | N                     |
| INJ             | 3961    | ALLERGENIC EXTRACT, GRASS, MEADOW FESCUE 10000PNU/ML INJ         | N                     |
| INJ             | 3874    | ALLERGENIC EXTRACT, GRASS, ORCHARD 10000PNU/ML INJ               | N                     |
| INJ             | 3962    | ALLERGENIC EXTRACT, GRASS, QUACK 10000PNU/ML INJ                 | N                     |
| INJ             | 3875    | ALLERGENIC EXTRACT, GRASS, REDTOP 10000PNU/ML INJ                | N                     |
| INJ             | 3959    | ALLERGENIC EXTRACT, GRASS, REED CANARY 10000PNU/ML INJ           | N                     |
| INJ             | 3963    | ALLERGENIC EXTRACT, GRASS, RYE, GIANT WILD 10000PNU/ML INJ       | N                     |
| INJ             | 3964    | ALLERGENIC EXTRACT, GRASS, RYE, ITALIAN 10000PNU/ML INJ          | N                     |
| INJ             | 3876    | ALLERGENIC EXTRACT, GRASS, RYE, PERENNIAL 10000PNU/ML INJ        | N                     |
| INJ             | 3965    | ALLERGENIC EXTRACT, GRASS, SALT 10000PNU/ML INJ                  | N                     |
| INJ             | 3877    | ALLERGENIC EXTRACT, GRASS, SWEET VERNAL 10000PNU/ML INJ          | N                     |
| INJ             | 3878    | ALLERGENIC EXTRACT, GRASS, TIMOTHY, 10000PNU/ML, INJ             | N                     |
| INJ             | 3966    | ALLERGENIC EXTRACT, GRASS, VELVET 1000PNU/ML INJ                 | N                     |
| INJ             | 3974    | ALLERGENIC EXTRACT, GRASS, WESTERN WATER HEMP 10000PNU/ML INJ    | N                     |
| INJ             | 4004    | ALLERGENIC EXTRACT, GRASS, WESTERN WHEAT 10000PNU/ML INJ         | N                     |
| INJ             | 3935    | ALLERGENIC EXTRACT, HELMINTHOSPORIUM SATIVUM 10000PNU/ML INJ     | N                     |
| INJ             | 3936    | ALLERGENIC EXTRACT, HORMODENDRUM HORDEI 10000PNU/ML INJ          | N                     |
| INJ             | 4007    | ALLERGENIC EXTRACT, HORSE EPITHELIA 10000PNU/ML INJ              | N                     |
| INJ             | 3940    | ALLERGENIC EXTRACT, HOUSE DUST 10000PNU/ML INJ                   | N                     |
| INJ             | 3942    | ALLERGENIC EXTRACT, HOUSE DUST 2% INJ                            | N                     |
| INJ             | 3939    | ALLERGENIC EXTRACT, HOUSE DUST 20000PNU/ML INJ                   | N                     |
| INJ             | 3941    | ALLERGENIC EXTRACT, HOUSE DUST INJ                               | N                     |
| INJ             | 3921    | ALLERGENIC EXTRACT, INSECT, BEE 10000PNU/ML INJ                  | N                     |
| INJ             | 3922    | ALLERGENIC EXTRACT, INSECT, BEE 20000PNU/ML INJ                  | N                     |
| INJ             | 4015    | ALLERGENIC EXTRACT, INSECT, STINGING MIX INJ                     | N                     |
| INJ             | 3923    | ALLERGENIC EXTRACT, INSECT, WASP 20000PNU/ML INJ                 | N                     |
| INJ             | 3924    | ALLERGENIC EXTRACT, INSECT, YELLOW JACKET 20000PNU/ML INJ        | N                     |
| INJ             | 3883    | ALLERGENIC EXTRACT, LAMB QUARTERS 10000PNU/ML INJ                | N                     |
| INJ             | 3967    | ALLERGENIC EXTRACT, MARSH ELDER MIX 10000PNU/ML INJ              | N                     |
| INJ             | 3968    | ALLERGENIC EXTRACT, MARSH ELDER MIX 20000PNU/ML INJ              | N                     |
| INJ             | 3932    | ALLERGENIC EXTRACT, MOLD, ALTERNARIA TENUIS 10000PNU/ML INJ      | N                     |
| INJ             | 3992    | ALLERGENIC EXTRACT, MOLD, BOTRYTIS CINEREA 10000PNU/ML INJ       | N                     |
| INJ             | 3994    | ALLERGENIC EXTRACT, MOLD, CURVULARIA LUNATA 10000PNU/ML INJ      | N                     |
| INJ             | 3995    | ALLERGENIC EXTRACT, MOLD, EPICOCCUM PURPURASCENS 10000PNU/ML INJ | N                     |
| INJ             | 3996    | ALLERGENIC EXTRACT, MOLD, FUSARIUM OXYSPORUM 10000PNU/ML INJ     | N                     |
| INJ             | 3997    | ALLERGENIC EXTRACT, MOLD, MUCOR RACEMOSUS 10000PNU/ML INJ        | N                     |
| INJ             | 3998    | ALLERGENIC EXTRACT, MOLD, PHOMA BETAE 10000PNU/ML INJ            | N                     |
| INJ             | 3999    | ALLERGENIC EXTRACT, MOLD, PULLULARIA PULLULANS 10000PNU/ML INJ   | N                     |
| INJ             | 4000    | ALLERGENIC EXTRACT, MOLD, RHIZOPUS ARRHIZUS 10000PNU/ML INJ      | N                     |
| INJ             | 4001    | ALLERGENIC EXTRACT, MOLD, STEMPHYLLUM BOTRYOSUM 10000PNU/ML INJ  | N                     |
| INJ             | 4002    | ALLERGENIC EXTRACT, MOLD, TRICHO. MENTAGROPHYTES 10000PNU/ML INJ | N                     |
| INJ             | 4003    | ALLERGENIC EXTRACT, MOLD, TRICOTHECIUM ROSEUM 10000PNU/ML INJ    | N                     |
| INJ             | 3884    | ALLERGENIC EXTRACT, MUGWORT, COMMON 10000PNU/ML INJ              | N                     |
| INJ             | 3937    | ALLERGENIC EXTRACT, PENICILLIN 10000PNU/ML INJ                   | N                     |
| INJ             | 4011    | ALLERGENIC EXTRACT, PER PRESCRIPTION 10000PNU/ML INJ             | N                     |
| INJ             | 4012    | ALLERGENIC EXTRACT, PER PRESCRIPTION 20000PNU/ML INJ             | N                     |
| INJ             | 3885    | ALLERGENIC EXTRACT, PIGWEED, ROUGH 10000PNU/ML INJ               | N                     |
| INJ             | 3969    | ALLERGENIC EXTRACT, PIGWEED, SPINY 10000PNU/ML INJ               | N                     |
| INJ             | 3886    | ALLERGENIC EXTRACT, PLANTAIN, ENGLISH 10000PNU/ML INJ            | N                     |
| INJ             | 3887    | ALLERGENIC EXTRACT, PLANTAIN, ENGLISH 20000PNU/ML INJ            | N                     |
| INJ             | 4008    | ALLERGENIC EXTRACT, RABBIT EPITHELIA 10000PNU/ML INJ             | N                     |
| INJ             | 3893    | ALLERGENIC EXTRACT, RAGWEED, WEST 10000PNU/ML INJ                | N                     |
| INJ             | 3890    | ALLERGENIC EXTRACT, SAGEBRUSH, COMMON 10000PNU/ML INJ            | N                     |
| INJ             | 3891    | ALLERGENIC EXTRACT, SAGEBRUSH, COMMON 20000PNU/ML INJ            | N                     |
| INJ             | 3892    | ALLERGENIC EXTRACT, SCALE MIX 10000PNU/ML INJ                    | N                     |
| INJ             | 4009    | ALLERGENIC EXTRACT, SHEEP WOOL 10000PNU/ML INJ                   | N                     |
| INJ             | 3920    | ALLERGENIC EXTRACT, STINGING INSECT MIX 20000PNU/ML INJ          | N                     |
| INJ             | 3919    | ALLERGENIC EXTRACT, STINGING INSECTS MIX 10000PNU/ML INJ         | N                     |
| INJ             | 3973    | ALLERGENIC EXTRACT, SUGAR BEET 10000PNU/ML INJ                   | N                     |
| INJ             | 3888    | ALLERGENIC EXTRACT, THISTLE, RUSSIAN 10000PNU/ML INJ             | N                     |
| INJ             | 3978    | ALLERGENIC EXTRACT, TREE, ARIZONA ASH 10000PNU/ML INJ            | N                     |
| INJ             | 3898    | ALLERGENIC EXTRACT, TREE, ASH MIX 10000PNU/ML INJ                | N                     |
| INJ             | 3899    | ALLERGENIC EXTRACT, TREE, BEECH 10000PNU/ML INJ                  | N                     |
| INJ             | 3980    | ALLERGENIC EXTRACT, TREE, BOX ELDER 10000PNU/ML INJ              | N                     |
| INJ             | 3981    | ALLERGENIC EXTRACT, TREE, BOX ELDER 20000PNU/ML INJ              | N                     |
| INJ             | 3903    | ALLERGENIC EXTRACT, TREE, COTTONWOOD, FREMONT 1000PNU/ML INJ     | N                     |
| INJ             | 3982    | ALLERGENIC EXTRACT, TREE, COTTONWOOD, WESTERN 10000PNU/ML INJ    | N                     |
| INJ             | 3983    | ALLERGENIC EXTRACT, TREE, COTTONWOOD, WESTERN 20000PNU/ML INJ    | N                     |
| INJ             | 3904    | ALLERGENIC EXTRACT, TREE, ELM MIX 10000PNU/ML INJ                | N                     |
| INJ             | 3905    | ALLERGENIC EXTRACT, TREE, ELM MIX 20000PNU/ML INJ                | N                     |
| INJ             | 3984    | ALLERGENIC EXTRACT, TREE, ELM, CHINESE 10000PNU/ML INJ           | N                     |
| INJ             | 3985    | ALLERGENIC EXTRACT, TREE, HAZELNUT, CALIFORNIA 10000PNU/ML INJ   | N                     |
| INJ             | 3907    | ALLERGENIC EXTRACT, TREE, HICKORY 10000PNU/ML INJ                | N                     |
| INJ             | 3908    | ALLERGENIC EXTRACT, TREE, MAPLE 10000PNU/ML INJ                  | N                     |
| INJ             | 4005    | ALLERGENIC EXTRACT, TREE, MAPLE MIX 20000PNU/ML INJ              | N                     |
| INJ             | 3906    | ALLERGENIC EXTRACT, TREE, MESQUITE 10000PNU/ML INJ               | N                     |
| INJ             | 3909    | ALLERGENIC EXTRACT, TREE, MOUNTAIN CEDAR 10000PNU/ML INJ         | N                     |
| INJ             | 3986    | ALLERGENIC EXTRACT, TREE, MULBERRY MIX 10000PNU/ML INJ           | N                     |
| INJ             | 3910    | ALLERGENIC EXTRACT, TREE, OAK MIX 10000PNU/ML INJ                | N                     |
| INJ             | 3911    | ALLERGENIC EXTRACT, TREE, OAK MIX 20000PNU/ML INJ                | N                     |
| INJ             | 3902    | ALLERGENIC EXTRACT, TREE, OAK, CALIFORNIA LIVE 20000PNU/ML INJ   | N                     |
| INJ             | 3901    | ALLERGENIC EXTRACT, TREE, OAK, CALIFORNIA LIVE, 10000PNU/ML, INJ | N                     |
| INJ             | 3912    | ALLERGENIC EXTRACT, TREE, OLIVE 10000PNU/ML INJ                  | N                     |
| INJ             | 3913    | ALLERGENIC EXTRACT, TREE, OLIVE 20000PNU/ML INJ                  | N                     |
| INJ             | 3979    | ALLERGENIC EXTRACT, TREE, OREGON ASH 10000PNU/ML INJ             | N                     |
| INJ             | 3914    | ALLERGENIC EXTRACT, TREE, PECAN 10000PNU/ML INJ                  | N                     |
| INJ             | 3915    | ALLERGENIC EXTRACT, TREE, POPLAR MIX 10000PNU/ML INJ             | N                     |
| INJ             | 3916    | ALLERGENIC EXTRACT, TREE, POPLAR MIX 20000PNU/ML                 | N                     |
| INJ             | 3976    | ALLERGENIC EXTRACT, TREE, RED ALDER 10000PNU/ML INJ              | N                     |
| INJ             | 3987    | ALLERGENIC EXTRACT, TREE, SWEET GUM 10000PNU/ML INJ              | N                     |
| INJ             | 3917    | ALLERGENIC EXTRACT, TREE, SYCAMORE 10000PNU/ML INJ               | N                     |
| INJ             | 3977    | ALLERGENIC EXTRACT, TREE, TAG ALDER 10000PNU/ML INJ              | N                     |
| INJ             | 3918    | ALLERGENIC EXTRACT, TREE, WALNUT 10000PNU/ML INJ                 | N                     |
| INJ             | 3988    | ALLERGENIC EXTRACT, TREE, WILLOW MIX 10000PNU/ML INJ             | N                     |
| INJ             | 3989    | ALLERGENIC EXTRACT, TREE, WILLOW MIX 20000PNU/ML INJ             | N                     |
| INJ             | 3880    | ALLERGENIC EXTRACT, WEED, CARELESS 10000PNU/ML INJ               | N                     |
| INJ             | 3881    | ALLERGENIC EXTRACT, WEED, KOCHIA 10000PNU/ML INJ                 | N                     |
| INJ             | 3882    | ALLERGENIC EXTRACT, WEED, KOCHIA 20000PNU/ML INJ                 | N                     |
| INJ             | 3972    | ALLERGENIC EXTRACT, WEED, SHEEP SORREL 10000PNU/ML INJ           | N                     |
| INJ             | 3879    | ALLERGENIC EXTRACT, WEED, WEST MIX 10000PNU/ML INJ               | N                     |
| INJ             | 3975    | ALLERGENIC EXTRACT, WEED, YELLOW DOCK 10000PNU/ML INJ            | N                     |
| INJ             | 6380    | ALLERGENIC EXTRACT,HONEY BEE VENOM INJ                           | N                     |
| INJ             | 6381    | ALLERGENIC EXTRACT,HORNET INJ                                    | N                     |
| INJ             | 6388    | ALLERGENIC EXTRACT,STINGING INSECT INJ                           | N                     |
| INJ             | 3889    | ALLERGENIC EXTRACT,THISTLE,RUSSIAN 20000PNU/ML INJ               | N                     |
| INJ             | 6382    | ALLERGENIC EXTRACT,WASP INJ                                      | N                     |
| INJ             | 6387    | ALLERGENIC EXTRACT,YELLOW JACKET INJ                             | N                     |
| INJ             | 3954    | ALUM PRECIPITATED POISON IVY EXTRACT 10000PNU/ML INJ             | N                     |
| INJ             | 12841   | ASPERGILLUS FUMIGATUS 1:500 INJ                                  | N                     |
| INJ             | 12497   | CANDIDA 1:100 SKIN TEST                                          | N                     |
| INJ             | 16406   | CANDIDA 1:1000 SKIN TEST                                         | N                     |
| INJ             | 12498   | CANDIDA 1:500 SKIN TEST                                          | N                     |
| INJ             | 12499   | CANDIDA ALBICANS SKIN TEST                                       | N                     |
| INJ             | 12776   | CANDIDA ALBICANS/COCCIDIOIDIN INJ TEST KIT                       | N                     |
| INJ             | 12775   | CANDIDA ALBICANS/HISTOPLASMIN INJ TEST KIT                       | N                     |
| INJ             | 12777   | CANDIDA ALBICANS/MUMPS INJ TEST KIT                              | N                     |
| INJ             | 4507    | CHYMOPAPAIN 2nKatU/ML INTRADISCAL                                | N                     |
| INJ             | 12528   | COCCIDIODIN 1:10 SKIN TEST                                       | N                     |
| INJ             | 12527   | COCCIDIODIN 1:100 SKIN TEST                                      | N                     |
| INJ             | 936     | DIATRIZOATE MEGLUMINE 18% INJ                                    | N                     |
| INJ             | 931     | DIATRIZOATE MEGLUMINE 28.5%/DIATRIZOATE NA 29.1% INJ             | N                     |
| INJ             | 933     | DIATRIZOATE MEGLUMINE 30% INJ                                    | N                     |
| INJ             | 926     | DIATRIZOATE MEGLUMINE 30% SOLN                                   | N                     |
| INJ             | 932     | DIATRIZOATE MEGLUMINE 30%/EDETATE DISODIUM 0.4MG INJ             | N                     |
| INJ             | 1346    | DIATRIZOATE MEGLUMINE 34.3%/DIATRIZOATE NA 35%/IODINE 37% INJ    | N                     |
| INJ             | 944     | DIATRIZOATE MEGLUMINE 50%/DIATRIZOATE NA 25% INJ                 | N                     |
| INJ             | 930     | DIATRIZOATE MEGLUMINE 52%/DIATRIZOATE NA 8% INJ                  | N                     |
| INJ             | 1143    | DIATRIZOATE MEGLUMINE 52.7%/IODIPAMIDE MEGLUMINE 26.8% SOLN      | N                     |
| INJ             | 929     | DIATRIZOATE MEGLUMINE 60% INJ                                    | N                     |
| INJ             | 949     | DIATRIZOATE MEGLUMINE 60% SOLN                                   | N                     |
| INJ             | 945     | DIATRIZOATE MEGLUMINE 60%/DIATRIZOATE NA 30% INJ                 | N                     |
| INJ             | 934     | DIATRIZOATE MEGLUMINE 66%/DIATRIZOATE NA 10% INJ                 | N                     |
| INJ             | 935     | DIATRIZOATE MEGLUMINE 76% INJ                                    | N                     |
| INJ             | 927     | DIATRIZOATE MEGLUMINE 85% INJ                                    | N                     |
| INJ             | 950     | DIATRIZOATE NA 20% INJ                                           | N                     |
| INJ             | 940     | DIATRIZOATE NA 20% SOLN                                          | N                     |
| INJ             | 941     | DIATRIZOATE NA 25% INJ                                           | N                     |
| INJ             | 937     | DIATRIZOATE NA 50% INJ                                           | N                     |
| INJ             | 12522   | DILUENT, STERILE FOR FLOLAN                                      | N                     |
| INJ             | 3373    | FAST-PAK ANGIOGRAPHY KIT WITH VASCORAY                           | N                     |
| INJ             | 4485    | GLYCERIN 10% INJ                                                 | N                     |
| INJ             | 4484    | GLYCERIN 25% INJECTION                                           | N                     |
| INJ             | 4483    | GLYCERIN 50% INJECTION                                           | N                     |
| INJ             | 352     | HISTAMINE PO4 0.275MG/ML INJ                                     | N                     |
| INJ             | 351     | HISTAMINE PO4 2.75MG/5ML INJ                                     | N                     |
| INJ             | 350     | HISTAMINE PO4 2.75MG/ML INJ                                      | N                     |
| INJ             | 6244    | INULIN 100MG/ML INJ                                              | N                     |
| INJ             | 1437    | IODAMIDE MEGLUMINE 24% INJ                                       | N                     |
| INJ             | 1436    | IODAMIDE MEGLUMINE 65% INJ                                       | N                     |
| INJ             | 1080    | IODIPAMIDE MEGLUMINE 10.3% INJ                                   | N                     |
| INJ             | 1079    | IODIPAMIDE MEGLUMINE 52% INJ                                     | N                     |
| INJ             | 12567   | IODIXANOL 270mgI/ml INJ                                          | N                     |
| INJ             | 12568   | IODIXANOL 320mgI/ml INJ                                          | N                     |
| INJ             | 7490    | IODOHIPPURATE NA,I-123, 1MIL/ML INJ                              | N                     |
| INJ             | 913     | IODOHIPPURATE NA,I-131,2MIL/VIL INJ                              | N                     |
| INJ             | 3762    | IOHEXOL 302MG/ML INJ                                             | N                     |
| INJ             | 3758    | IOHEXOL 388.3MG/ML INJ                                           | N                     |
| INJ             | 3763    | IOHEXOL 435MG/ML INJ                                             | N                     |
| INJ             | 3759    | IOHEXOL 517.7MG/ML INJ                                           | N                     |
| INJ             | 3760    | IOHEXOL 647.1MG/ML INJ                                           | N                     |
| INJ             | 3761    | IOHEXOL 755MG/ML INJ                                             | N                     |
| INJ             | 1410    | IOPAMIDOL 408MG/ML INJ                                           | N                     |
| INJ             | 1412    | IOPAMIDOL 410MG/ML INJ                                           | N                     |
| INJ             | 1414    | IOPAMIDOL 510MG/ML INJ                                           | N                     |
| INJ             | 1413    | IOPAMIDOL 51MG/ML INJ                                            | N                     |
| INJ             | 1408    | IOPAMIDOL 612MG/ML INJ                                           | N                     |
| INJ             | 1409    | IOPAMIDOL 755MG/ML INJ                                           | N                     |
| INJ             | 3369    | IOTHALAMATE NA 54.3% KIT                                         | N                     |
| INJ             | 12571   | IOVERSOL 160MG/ML INJ                                            | N                     |
| INJ             | 12570   | IOVERSOL 240MG/ML INJ                                            | N                     |
| INJ             | 12572   | IOVERSOL 300MG/ML INJ                                            | N                     |
| INJ             | 12569   | IOVERSOL 320MG/ML INJ                                            | N                     |
| INJ             | 12573   | IOVERSOL 350MG/ML INJ                                            | N                     |
| INJ             | 12982   | IOXILAN 300mgI/ml INJ                                            | N                     |
| INJ             | 12983   | IOXILAN 350mgI/ml INJ                                            | N                     |
| INJ             | 12780   | LOXILAN 300mgI/ml INJ                                            | N                     |
| INJ             | 12781   | LOXILAN 350mgI/ml INJ                                            | N                     |
| INJ             | 3625    | METRIZAMIDE 13.5GM/VIL INJ                                       | N                     |
| INJ             | 3624    | METRIZAMIDE 2.5GM/VIL INJ                                        | N                     |
| INJ             | 3622    | METRIZAMIDE 3.75GM/VIL INJ                                       | N                     |
| INJ             | 3623    | METRIZAMIDE 6.75GM/VIL INJ                                       | N                     |
| INJ             | 15913   | OCTAFLUOROPROPANE MICROSPHERE 10MG/ML INJ,SUSP                   | N                     |
| INJ             | 3955    | POISON IVY EXTRACT INJ                                           | N                     |
| INJ             | 12877   | PROSTASCINT KIT (CAPROMAB PENDETIDE)                             | N                     |
| INJ             | 12849   | SAMARIUM Sm153 LEXIDRONAM 1850MBq/ML INJ,VIL,2ML                 | N                     |
| INJ             | 909     | SELENOMETHIONINE,SE-75,550MIC/VIL INJ                            | N                     |
| INJ             | 468     | SODIUM CHLORIDE (PF) 0.9% INJ                                    | N                     |
| INJ             | 452     | SODIUM CHLORIDE 0.45% INJ                                        | N                     |
| INJ             | 463     | SODIUM CHLORIDE 0.45% INJ                                        | N                     |
| INJ             | 479     | SODIUM CHLORIDE 0.45% INJ                                        | N                     |
| INJ             | 464     | SODIUM CHLORIDE 0.5% INJ                                         | N                     |
| INJ             | 474     | SODIUM CHLORIDE 0.9% (PF) INJ                                    | N                     |
| INJ             | 510     | SODIUM CHLORIDE 0.9% (PF) INJ,SYRINGE,10ML                       | N                     |
| INJ             | 507     | SODIUM CHLORIDE 0.9% (PF) INJ,SYRINGE,3ML                        | N                     |
| INJ             | 509     | SODIUM CHLORIDE 0.9% (PF) INJ,SYRINGE,5ML                        | N                     |
| INJ             | 508     | SODIUM CHLORIDE 0.9% (PF) INJ,SYRINGE,5ML/10ML                   | N                     |
| INJ             | 448     | SODIUM CHLORIDE 0.9% INJ                                         | N                     |
| INJ             | 451     | SODIUM CHLORIDE 0.9% INJ                                         | N                     |
| INJ             | 477     | SODIUM CHLORIDE 0.9% INJ                                         | N                     |
| INJ             | 17385   | SODIUM CHLORIDE 0.9% INJ,SYR,10ML POSIFLUSH                      | N                     |
| INJ             | 7604    | SODIUM CHLORIDE 0.9% W/LOW DISSOLVED OXYGEN                      | N                     |
| INJ             | 2948    | SODIUM CHLORIDE 0.9%/BENZYL ALCOHOL 0.9% INJ                     | N                     |
| INJ             | 2949    | SODIUM CHLORIDE 0.9%/BENZYL ALCOHOL 2% INJ                       | N                     |
| INJ             | 2950    | SODIUM CHLORIDE 0.9%/BENZYL ALCOHOL INJ                          | N                     |
| INJ             | 14236   | SODIUM CHLORIDE 0.9%/BENZYL ALCOHOL INJ,30ML                     | N                     |
| INJ             | 2724    | SODIUM CHLORIDE 0.9%/METHYLPARABEN/PROPYLPARABEN INJ             | N                     |
| INJ             | 505     | SODIUM CHLORIDE 0.9%/METHYLPARABEN/PROPYLPARABEN INJ,TUBEX,2.5ML | N                     |
| INJ             | 6392    | SODIUM CHLORIDE 0.9%/PHENOL 0.4% INJ                             | N                     |
| INJ             | 907     | SODIUM CHROMATE,CR-51,250MIC/VIL INJ                             | N                     |
| INJ             | 6721    | SODIUM CITRATE 46.7% INJ                                         | N                     |
| INJ             | 3406    | TECHNESCAN GLUCEPTATE INJ                                        | N                     |
| INJ             | 3407    | TECHNESCAN MDP KIT                                               | N                     |
| INJ             | 3409    | TECHNETIUM 99M DTPA PENTETATE KIT                                | N                     |
| INJ             | 3408    | TECHNETIUM Tc 99m DISOFENIN 20MG INJ                             | N                     |
| INJ             | 7456    | TECHNETIUM Tc 99m NOFETUMOMAB MERPENTAN INJ                      | N                     |
| INJ             | 16864   | TRICHOPHYTON MENTAGROPHYTES 1:200 INJ                            | N                     |
| INJ             | 13369   | TRICHOPHYTON MENTAGROPHYTES 1:500 INJ                            | N                     |
| INJ             | 12657   | TRICOPHYTON MENTAGROPHYTES 1:500 INJ                             | N                     |
| INJ             | 2422    | WATER FOR INJECTION                                              | N                     |
| INJ             | 16431   | WATER FOR INJECTION,BACTERIOSTATIC,10ML                          | N                     |
| INJ             | 16432   | WATER FOR INJECTION,BACTERIOSTATIC,30ML                          | N                     |
| INJ             | 16430   | WATER FOR INJECTION,STERILE,100ML                                | N                     |
| INJ             | 16427   | WATER FOR INJECTION,STERILE,10ML                                 | N                     |
| INJ             | 16428   | WATER FOR INJECTION,STERILE,20ML                                 | N                     |
| INJ             | 16425   | WATER FOR INJECTION,STERILE,30ML                                 | N                     |
| INJ             | 16429   | WATER FOR INJECTION,STERILE,50ML                                 | N                     |
| INJ             | 16426   | WATER FOR INJECTION,STERILE,5ML                                  | N                     |
| INJ             | 2939    | WATER/BENZYL ALCOHOL 0.5% INJ                                    | N                     |
| INJ             | 2937    | WATER/BENZYL ALCOHOL 0.9% INJ                                    | N                     |
| INJ             | 2938    | WATER/BENZYL ALCOHOL 1.5% INJ                                    | N                     |
| INJ             | 2940    | WATER/BENZYL ALCOHOL INJ                                         | N                     |
| INJ             | 6851    | WATER/METHYLPARABEN 0.05%/PROPYLPARABEN 0.005% INJ               | N                     |
| INJ             | 2427    | WATER/METHYLPARABEN 0.1%/PROPYLPARABEN 0.025% INJ                | N                     |
| INJ             | 6850    | WATER/METHYLPARABEN 0.1%/PROPYLPARABEN 0.025% INJ                | N                     |
| INJ             | 6852    | WATER/METHYLPARABEN 0.12%/PROPYLPARABEN 0.012% INJ               | N                     |
| INJ,CONC, W/BUF | 3931    | ALLERGENIC EXTRACT,DOG EPITHELIA INJ                             | N                     |
| INJ,CONC, W/BUF | 7637    | ALLERGENIC EXTRACT,DUST INJ                                      | N                     |
| INJ,CONC, W/BUF | 7635    | ALLERGENIC EXTRACT,FOOD,WHEAT INJ                                | N                     |
| INJ,CONC, W/BUF | 6772    | ALLERGENIC EXTRACT,MIXED ANTIGENS                                | N                     |
| INJ,CONC, W/BUF | 7636    | ALLERGENIC EXTRACT,MOLD INJ                                      | N                     |
| INJ,CONC, W/BUF | 7638    | ALLERGENIC EXTRACT,POLLEN INJ                                    | N                     |
| INJ,CONC, W/BUF | 7634    | ALLERGENIC EXTRACT,RAGWEED STOCK POLLEN INJ                      | N                     |
| INJ,REPOSITORY  | 7777    | ADRENOCORTICOTROPIN (ACTH 1-18),I-125 (TYR) 40UNT/ML INJ         | N                     |
| INJ,REPOSITORY  | 7778    | ADRENOCORTICOTROPIN (ACTH 1-18),I-125 (TYR) 80UNT/ML INJ         | N                     |
| INJ,SOLN        | 7719    | ACCU-BLOC CUSTOM EPIDURAL ANESTHESIA                             | N                     |
| INJ,SOLN        | 7720    | ACCU-BLOC PERIFIX CUSTOM EPIDURAL ANESTHESIA                     | N                     |
| INJ,SOLN        | 7725    | ACCU-BLOC PERIFIX CUSTOM EPIDURAL ANESTHESIA                     | N                     |
| INJ,SOLN        | 7741    | ACCU-BLOC PERIFIX CUSTOM EPIDURAL ANESTHESIA                     | N                     |
| INJ,SOLN        | 7743    | ACCU-BLOC PERIFIX CUSTOM EPIDURAL ANESTHESIA                     | N                     |
| INJ,SOLN        | 7726    | ACCU-BLOCK KIT                                                   | N                     |
| INJ,SOLN        | 7493    | ALBUMIN HUMAN 21MG/STANNOUS TARTRATE 0.23MG INJ                  | N                     |
| INJ,SOLN        | 7492    | ALBUMIN HUMAN 7MG/STANNOUS TARTRATE 0.08MG INJ                   | N                     |
| INJ,SOLN        | 3398    | ALBUMIN,IODINATED SERUM (I-125) 10MIC/1.5 INJ                    | N                     |
| INJ,SOLN        | 3399    | ALBUMIN,IODINATED SERUM (I-125) 10MIC/IODINE (I-125) 0.01 MIC IJ | N                     |
| INJ,SOLN        | 3397    | ALBUMIN,IODINATED SERUM (I-125) 10MIL/ML INJ                     | N                     |
| INJ,SOLN        | 3330    | ALBUMIN,MICROSPHERE HUMAN SERUM 5MG/UNT INJ                      | N                     |
| INJ,SOLN        | 3208    | ALCOHOL,ABSOLUTE 98% INJ                                         | N                     |
| INJ,SOLN        | 3220    | ALCOHOL,ABSOLUTE 98% INJ,AMP,1ML                                 | N                     |
| INJ,SOLN        | 3222    | ALCOHOL,ABSOLUTE 98% INJ,AMP,50ML                                | N                     |
| INJ,SOLN        | 3221    | ALCOHOL,ABSOLUTE 98% INJ,AMP,5ML                                 | N                     |
| INJ,SOLN        | 6742    | ALLERGENIC EXT,HOUSE DUST CONC 0.4GM/ML INJ                      | N                     |
| INJ,SOLN        | 6769    | ALLERGENIC EXTRACT 0.744ML INJ                                   | N                     |
| INJ,SOLN        | 6768    | ALLERGENIC EXTRACT 0.996ML INJ                                   | N                     |
| INJ,SOLN        | 6771    | ALLERGENIC EXTRACT 1 UNT/ML INJ                                  | N                     |
| INJ,SOLN        | 6770    | ALLERGENIC EXTRACT 1.5ML INJ                                     | N                     |
| INJ,SOLN        | 6767    | ALLERGENIC EXTRACT 4.98ML INJ                                    | N                     |
| INJ,SOLN        | 7541    | ALLERGENIC EXTRACT EPIDERMAL INJ                                 | N                     |
| INJ,SOLN        | 7537    | ALLERGENIC EXTRACT GRASSES INJ                                   | N                     |
| INJ,SOLN        | 6766    | ALLERGENIC EXTRACT INJ                                           | N                     |
| INJ,SOLN        | 7542    | ALLERGENIC EXTRACT INJ                                           | N                     |
| INJ,SOLN        | 7532    | ALLERGENIC EXTRACT INSECTS HOUSEHOLD INJ                         | N                     |
| INJ,SOLN        | 7534    | ALLERGENIC EXTRACT MIXED EPIDERMALS INJ                          | N                     |
| INJ,SOLN        | 7528    | ALLERGENIC EXTRACT MIXED GRASSES INJ                             | N                     |
| INJ,SOLN        | 7533    | ALLERGENIC EXTRACT MIXED INHL INJ                                | N                     |
| INJ,SOLN        | 7531    | ALLERGENIC EXTRACT MIXED INSECT STINGING INJ                     | N                     |
| INJ,SOLN        | 7530    | ALLERGENIC EXTRACT MIXED MOLDS INJ                               | N                     |
| INJ,SOLN        | 7527    | ALLERGENIC EXTRACT MIXED TREES INJ                               | N                     |
| INJ,SOLN        | 7529    | ALLERGENIC EXTRACT MIXED WEEDS INJ                               | N                     |
| INJ,SOLN        | 7538    | ALLERGENIC EXTRACT TREES INJ                                     | N                     |
| INJ,SOLN        | 7539    | ALLERGENIC EXTRACT WEEDS INJ                                     | N                     |
| INJ,SOLN        | 6749    | ALLERGENIC EXTRACT, ALTERNARIA MOLD 10% INJ                      | N                     |
| INJ,SOLN        | 6744    | ALLERGENIC EXTRACT, ALTERNARIA MOLD 10000 PNU/ML INJ             | N                     |
| INJ,SOLN        | 6747    | ALLERGENIC EXTRACT, ALTERNARIA MOLD 2% INJ                       | N                     |
| INJ,SOLN        | 6745    | ALLERGENIC EXTRACT, ALTERNARIA MOLD 20000 PNU/ML INJ             | N                     |
| INJ,SOLN        | 6746    | ALLERGENIC EXTRACT, ALTERNARIA MOLD 40000 PNU/ML INJ             | N                     |
| INJ,SOLN        | 6748    | ALLERGENIC EXTRACT, ALTERNARIA MOLD 5% INJ                       | N                     |
| INJ,SOLN        | 6743    | ALLERGENIC EXTRACT, ALTERNARIA MOLD 5000 PNU/ML INJ              | N                     |
| INJ,SOLN        | 7540    | ALLERGENIC EXTRACT, DUST, AUTOGENOUS 1 UNT/ML INJ                | N                     |
| INJ,SOLN        | 6755    | ALLERGENIC EXTRACT, HORSE DANDER 1% INJ                          | N                     |
| INJ,SOLN        | 6757    | ALLERGENIC EXTRACT, HORSE DANDER 10% INJ                         | N                     |
| INJ,SOLN        | 6753    | ALLERGENIC EXTRACT, HORSE DANDER 10000PNU/ML INJ                 | N                     |
| INJ,SOLN        | 6754    | ALLERGENIC EXTRACT, HORSE DANDER 20000PNU/ML INJ                 | N                     |
| INJ,SOLN        | 6756    | ALLERGENIC EXTRACT, HORSE DANDER 5% INJ                          | N                     |
| INJ,SOLN        | 6752    | ALLERGENIC EXTRACT, HORSE DANDER 5000PNU/ML INJ                  | N                     |
| INJ,SOLN        | 3953    | ALLERGENIC EXTRACT, HOUSE DUST 1 UNT/ML INJ                      | N                     |
| INJ,SOLN        | 3943    | ALLERGENIC EXTRACT, HOUSE DUST 10000 PNU/ML INJ                  | N                     |
| INJ,SOLN        | 3944    | ALLERGENIC EXTRACT, HOUSE DUST 20000PNU/ML INJ                   | N                     |
| INJ,SOLN        | 3945    | ALLERGENIC EXTRACT, HOUSE DUST 40000 PNU/ML INJ                  | N                     |
| INJ,SOLN        | 3946    | ALLERGENIC EXTRACT, HOUSE DUST 50000 PNU/ML INJ                  | N                     |
| INJ,SOLN        | 3947    | ALLERGENIC EXTRACT, HOUSE DUST INJ                               | N                     |
| INJ,SOLN        | 7526    | ALLERGENIC EXTRACT, SHORT RAGWEED 1 UNT / TALL RAGWEED 1 UNT INJ | N                     |
| INJ,SOLN        | 6764    | ALLERGENIC EXTRACT, SHORT RAGWEED ALTERNARIA 10 % INJ            | N                     |
| INJ,SOLN        | 6759    | ALLERGENIC EXTRACT, SHORT RAGWEED ALTERNARIA 10000 PNU/ML INJ    | N                     |
| INJ,SOLN        | 6762    | ALLERGENIC EXTRACT, SHORT RAGWEED ALTERNARIA 2 % INJ             | N                     |
| INJ,SOLN        | 6760    | ALLERGENIC EXTRACT, SHORT RAGWEED ALTERNARIA 20000 PNU/ML INJ    | N                     |
| INJ,SOLN        | 6761    | ALLERGENIC EXTRACT, SHORT RAGWEED ALTERNARIA 40000 PNU/ML INJ    | N                     |
| INJ,SOLN        | 6763    | ALLERGENIC EXTRACT, SHORT RAGWEED ALTERNARIA 5 % INJ             | N                     |
| INJ,SOLN        | 6758    | ALLERGENIC EXTRACT, SHORT RAGWEED ALTERNARIA 5000 PNU/ML INJ     | N                     |
| INJ,SOLN        | 6385    | ALLERGENIC EXTRACT, WASP 1 % INJ                                 | N                     |
| INJ,SOLN        | 6386    | ALLERGENIC EXTRACT, WASP 10 % INJ                                | N                     |
| INJ,SOLN        | 6383    | ALLERGENIC EXTRACT, WASP 10000 PNU/ML INJ                        | N                     |
| INJ,SOLN        | 6384    | ALLERGENIC EXTRACT, WASP 20000 PNU/ML INJ                        | N                     |
| INJ,SOLN        | 3950    | ALLERGENIC EXTRACT,HOUSE DUST,STOCK 10000UNT/ML INJ              | N                     |
| INJ,SOLN        | 3949    | ALLERGENIC EXTRACT,HOUSE DUST,STOCK 1000UNT INJ                  | N                     |
|                     | 3951    | ALLERGENIC EXTRACT,HOUSE DUST,STOCK 1000UNT/ML INJ               |                       |
| INJ,SOLN        | 3952    | ALLERGENIC EXTRACT,HOUSE DUST,STOCK 100UNT/ML INJ                | N                     |
| INJ,SOLN        | 6751    | ALLERGENIC EXTRACT,MOLDS MIXTURE INJ                             | N                     |
| INJ,SOLN        | 6738    | ALLERGENIC EXTRACT,TIMOTHY GRASS POLLEN 1 % INJ                  | N                     |
| INJ,SOLN        | 6735    | ALLERGENIC EXTRACT,TIMOTHY GRASS POLLEN 10000 PNU/ML INJ         | N                     |
| INJ,SOLN        | 6739    | ALLERGENIC EXTRACT,TIMOTHY GRASS POLLEN 2 % INJ                  | N                     |
| INJ,SOLN        | 6736    | ALLERGENIC EXTRACT,TIMOTHY GRASS POLLEN 20000 PNU/ML INJ         | N                     |
| INJ,SOLN        | 6740    | ALLERGENIC EXTRACT,TIMOTHY GRASS POLLEN 3 % INJ                  | N                     |
| INJ,SOLN        | 6737    | ALLERGENIC EXTRACT,TIMOTHY GRASS POLLEN 40000 PNU/ML INJ         | N                     |
| INJ,SOLN        | 6741    | ALLERGENIC EXTRACT,TIMOTHY GRASS POLLEN 5 % INJ                  | N                     |
| INJ,SOLN        | 7536    | ALLERGENIC EXTRACTS DIAGNOSTIC SCRATCH TEST INJ                  | N                     |
| INJ,SOLN        | 7435    | ALLERGENIC EXTRACTS INTRADERMAL INJ                              | N                     |
| INJ,SOLN        | 7535    | ALLERGENIC EXTRACTS MIXED INHL EPIDERMAL INJ                     | N                     |
| INJ,SOLN        | 7732    | CENTRAL VEIN CATHETERIZATION KIT                                 | N                     |
| INJ,SOLN        | 947     | DIATRIZOATE MEGLUMINE 30%/EDETATE CA DISODIUM 0.05MG/ML INJ      | N                     |
| INJ,SOLN        | 946     | DIATRIZOATE MEGLUMINE 60% INJ                                    | N                     |
| INJ,SOLN        | 7731    | DIGITAL KIT                                                      | N                     |
| INJ,SOLN        | 7171    | DYE EVANS BLUE 5MG/ML INJ                                        | N                     |
| INJ,SOLN        | 2978    | DYE FDC (BLUE \#2) 8MG/ML INJ                                    | N                     |
| INJ,SOLN        | 3401    | FERROUS CITRATE (FE-59) 25MIL/ML INJ                             | N                     |
| INJ,SOLN        | 7479    | FIBRINOGEN 1MG/IODINE (I-125) 154 MIC INJ                        | N                     |
| INJ,SOLN        | 17002   | FLUDEOXYGLUCOSE F 18 (10-100 MCI/ML) INJ                         | N                     |
| INJ,SOLN        | 17037   | GADOBENOATE DIMEGLUMINE 529MG/ML INJ,SOLN                        | N                     |
| INJ,SOLN        | 9907    | GADODIAMIDE 287MG/ML INJ                                         | N                     |
| INJ,SOLN        | 11742   | GADODIAMIDE 287MG/ML INJ                                         | N                     |
| INJ,SOLN        | 8877    | GADOPENTETATE DIMEGLUMINE 469.01MG/ML INJ,SOLN                   | N                     |
| INJ,SOLN        | 14381   | GADOVERSETAMIDE 330.9MG/ML INJ                                   | N                     |
| INJ,SOLN        | 7489    | GALLIUM CHLORIDE (GA-67) 2MIL/NA CITRATE 2.5% INJ                | N                     |
| INJ,SOLN        | 3396    | GALLIUM CITRATE (GA-67) 2MIL/ML INJ                              | N                     |
| INJ,SOLN        | 7457    | GALLIUM CITRATE (GA-67) 2MIL/NA CITRATE 2MG INJ                  | N                     |
| INJ,SOLN        | 7459    | GLUCEPTATE NA 200MG/STANNOUS CL 0.06MG/TIN 0.07MG INJ            | N                     |
| INJ,SOLN        | 7333    | GLUCEPTATE SODIUM 200MG/STANNOUS CHLORIDE 0.1MG INJ              | N                     |
| INJ,SOLN        | 6765    | GLYCERIN 50%/SODIUM CHLORIDE 0.9%/PHENOL 0.4% INJ                | N                     |
| INJ,SOLN        | 6724    | HAEMO-PAK UNIT FOR PLASMAPHERESIS                                | N                     |
| INJ,SOLN        | 19983   | IOBENGUANE I 123 370MBQ/VIL INJ,SOLN                             | N                     |
| INJ,SOLN        | 914     | IODOHIPPURATE NA,I-131,0.25MIL INJ                               | N                     |
| INJ,SOLN        | 915     | IODOHIPPURATE NA,I-131,0.2MIL/ML INJ                             | N                     |
| INJ,SOLN        | 916     | IODOHIPPURATE NA,I-131,0.8MIL INJ                                | N                     |
| INJ,SOLN        | 1411    | IOPAMIDOL 261MG/ML INJ                                           | N                     |
| INJ,SOLN        | 6633    | IOPHENDYLATE 100% INJ                                            | N                     |
| INJ,SOLN        | 12427   | IOPROMIDE 150mgI/ml INJ                                          | N                     |
| INJ,SOLN        | 12428   | IOPROMIDE 240mgI/ml INJ                                          | N                     |
| INJ,SOLN        | 12429   | IOPROMIDE 300mgI/ml INJ                                          | N                     |
| INJ,SOLN        | 12430   | IOPROMIDE 370mgI/ml INJ                                          | N                     |
| INJ,SOLN        | 3362    | IOTHALAMATE MEGLUMINE 17.2% SOLN                                 | N                     |
| INJ,SOLN        | 3375    | IOTHALAMATE MEGLUMINE 30% INJ                                    | N                     |
| INJ,SOLN        | 3367    | IOTHALAMATE MEGLUMINE 43% INJ                                    | N                     |
| INJ,SOLN        | 3359    | IOTHALAMATE MEGLUMINE 52%/IOTHALAMATE NA 26% INJ                 | N                     |
| INJ,SOLN        | 3364    | IOTHALAMATE MEGLUMINE 60% INJ                                    | N                     |
| INJ,SOLN        | 3361    | IOTHALAMATE NA 54.3% INJ                                         | N                     |
| INJ,SOLN        | 3365    | IOTHALAMATE NA 66.8% INJ                                         | N                     |
| INJ,SOLN        | 3363    | IOTHALAMATE NA 80% INJ                                           | N                     |
| INJ,SOLN        | 8875    | IOTROLAN 190MG/ML INJ INTH                                       | N                     |
| INJ,SOLN        | 8876    | IOTROLAN 240MG/ML INJ INTH                                       | N                     |
| INJ,SOLN        | 3467    | IOXAGLATE MEGLUMINE 393/IOXAGLATE NA 196MG/ML INJ                | N                     |
| INJ,SOLN        | 3468    | IOXAGLATE MEGLUMINE 393MG/IOXAGLATE NA 196 MG/ML INJ,SYR,125ML   | N                     |
| INJ,SOLN        | 7165    | ISOSULFAN BLUE 1% INJ                                            | N                     |
| INJ,SOLN        | 7462    | MEDRONATE DISODIUM 10MG/STANNOUS CHLORIDE 0.85MG INJ             | N                     |
| INJ,SOLN        | 7336    | METHYLENE DIPHOSPHONIC ACID 8MG/STANNOUS CL 0.85MG INJ           | N                     |
| INJ,SOLN        | 7335    | MICROLITE INJ                                                    | N                     |
| INJ,SOLN        | 7730    | MODEL SP5800 \#8 INTRODUCER KIT                                  | N                     |
| INJ,SOLN        | 3385    | MOLYBDENUM (MO-99) 100MIL INJ                                    | N                     |
| INJ,SOLN        | 3390    | MOLYBDENUM (MO-99) 150MIL INJ                                    | N                     |
| INJ,SOLN        | 3386    | MOLYBDENUM (MO-99) 200MIL INJ                                    | N                     |
| INJ,SOLN        | 3391    | MOLYBDENUM (MO-99) 3000MIL INJ                                   | N                     |
| INJ,SOLN        | 3387    | MOLYBDENUM (MO-99) 300MIL INJ                                    | N                     |
| INJ,SOLN        | 3388    | MOLYBDENUM (MO-99) 400MIL INJ                                    | N                     |
| INJ,SOLN        | 3392    | MOLYBDENUM (MO-99) 50 MIL/ML INJ                                 | N                     |
| INJ,SOLN        | 3389    | MOLYBDENUM (MO-99) 500MIL INJ                                    | N                     |
| INJ,SOLN        | 7499    | MPI MDP KIT INJ                                                  | N                     |
| INJ,SOLN        | 7654    | MULTITEST CMI,SKIN TEST ANTIGENS                                 | N                     |
| INJ,SOLN        | 7498    | PENTETATE CA TRISODIUM 20.6MG/STANNOUS CL 0.21MG INJ             | N                     |
| INJ,SOLN        | 7497    | PENTETATE CA TRISODIUM 3MG/STANNOUS CHLORIDE 0.15MG INJ          | N                     |
| INJ,SOLN        | 7491    | PENTETATE INDIUM DISODIUM (IN-111) INJ                           | N                     |
| INJ,SOLN        | 7500    | PENTETATE PENTASODIUM 5MG/STANNOUS CL 0.25MG INJ                 | N                     |
| INJ,SOLN        | 7436    | POISON IVY/OAK/SUMAC EXTRACTS COMBINED INJ                       | N                     |
| INJ,SOLN        | 7334    | PYROLITE INJ                                                     | N                     |
| INJ,SOLN        | 3400    | RED CELL TAGGING KIT INJ                                         | N                     |
| INJ,SOLN        | 7606    | ROSE BENGAL SODIUM,I-131,0.5MIL/ML INJ                           | N                     |
| INJ,SOLN        | 7605    | ROSE BENGAL SODIUM,I-131,O.5MIL INJ                              | N                     |
| INJ,SOLN        | 3403    | SCHILLING TEST KIT                                               | N                     |
| INJ,SOLN        | 911     | SELENOMETHIONINE,SE-75 300MIC/ML,INJ                             | N                     |
| INJ,SOLN        | 910     | SELENOMETHIONINE,SE-75,0.1MIL/ML INJ                             | N                     |
| INJ,SOLN        | 912     | SELENOMETHIONINE,SE-75,0.3MIL INJ                                | N                     |
| INJ,SOLN        | 908     | SODIUM CHROMATE,CR-51,100MIC/ML INJ                              | N                     |
| INJ,SOLN        | 3383    | SODIUM HYDROXYMETHANE DIPHOSPHONATE 2MG/STANNOUS CL 0.16MG INJ   | N                     |
| INJ,SOLN        | 921     | SODIUM IODIDE,I-131,0.067MIL/ML SOLN                             | N                     |
| INJ,SOLN        | 919     | SODIUM IODIDE,I-131,7.05MIL SOLN                                 | N                     |
| INJ,SOLN        | 3384    | SODIUM MOLYBDATE (V1) 50MIL INJ                                  | N                     |
| INJ,SOLN        | 1442    | SODIUM PERTECHNETATE (Tc 99m) 60MIL INJ                          | N                     |
| INJ,SOLN        | 1441    | SODIUM PERTECHNETATE (Tc 99m) 9MG/ML INJ                         | N                     |
| INJ,SOLN        | 3404    | SODIUM PHOSPHATE (P-32) 0.16MIL/ML INJ                           | N                     |
| INJ,SOLN        | 7514    | SODIUM THIOSULFATE 1.1NS/TECHNETIUM (Tc 99m) 3MIL INJ            | N                     |
| INJ,SOLN        | 7496    | STANNOUS CL,ANHYDROUS 0.42MG/SUCCIMER 1.2MG INJ                  | N                     |
| INJ,SOLN        | 11788   | STRONTIUM-89 CL 148MBq,4mCi/10ML INJ                             | N                     |
| INJ,SOLN        | 7454    | TECHNETIUM (Tc 99m) 10MIL INJ                                    | N                     |
| INJ,SOLN        | 7455    | TECHNETIUM (Tc 99m) 30MIL INJ                                    | N                     |
| INJ,SOLN        | 7453    | TECHNETIUM Tc 99m 0 INJ                                          | N                     |
| INJ,SOLN        | 3394    | THALLOUS CHLORIDE (TL-201) 1MIL INJ                              | N                     |
| INJ,SOLN        | 3393    | THALLOUS CHLORIDE (TL-201) 1MIL/ML INJ                           | N                     |
| INJ,SOLN        | 3395    | THALLOUS CHLORIDE (TL-201) 2MIL/ML INJ                           | N                     |
| INJ,SOLN        | 16360   | TOSITUMOMAB IODINE-131 0.61MCI/ML INJ                            | N                     |
| INJ,SOLN        | 16361   | TOSITUMOMAB IODINE-131 VIAL 5.6MCI/ML                            | N                     |
| INJ,SOLN        | 7830    | YTTERBIUM (YB-169) DTPA 2.5MIC/VIL INJ                           | N                     |
| INJ,SUSP        | 7461    | AGGREGATED ALBUMIN(HUMAN)                                        | N                     |
| INJ,SUSP        | 3871    | ALLERGENIC EXTRACT, GRASS, BERMUDA INJ,SUSP                      | N                     |
| INJ,SUSP        | 3948    | ALLERGENIC EXTRACT, HOUSE DUST INJ,SUSP                          | N                     |
| INJ,SUSP        | 7337    | AN-MDP TECHNETIUM TC 99M MEDRONATE KIT                           | N                     |
| INJ,SUSP        | 3405    | CHROMIC PO4 (P-32) 7MIL/ML INJ,SUSP                              | N                     |
| INJ,SUSP        | 7463    | DISOFENIN 20MG/STANNOUS CHLORIDE 0.24MG INJ,SUSP                 | N                     |
| INJ,SUSP        | 7460    | PULMOLITE INJ,SUSP                                               | N                     |
| INJ,SUSP        | 3377    | TECHNESCAN MAA INJ,SUSP                                          | N                     |
| INJ,SUSP        | 7495    | TECHNETIUM TC 99M MAA MULTIDOSE INJ,SUSP                         | N                     |
| INJ,SUSP        | 7494    | TECHNETIUM TC 99M MAA UNIT DOSE INJ,SUSP                         | N                     |
| KIT             | 1709    | HEMOPHILUS B POLYSACCHARIDE VACCINE 150MCG/NACL 0.9% INJ         | Y                     |
| KIT             | 7842    | INSECT STING TREATMENT KIT INJ                                   | Y                     |
| KIT             | 13013   | ROTAVIRUS TETRAVALENT VACCINE LIVE SOLN,ORAL,KIT,2.5ML           | Y                     |
| KIT             | 9509    | THIOPENTAL NA 1GM/VIL/WATER 40ML INJ                             | Y                     |
| KIT             | 9510    | THIOPENTAL NA 2.5GM/VIL/WATER 100ML INJ                          | Y                     |
| KIT             | 9506    | THIOPENTAL NA 250MG/VIL/NACL 0.9% KIT,INJ                        | Y                     |
| KIT             | 9507    | THIOPENTAL NA 400MG/VIL/NACL 0.9% KIT,INJ                        | Y                     |
| KIT             | 9508    | THIOPENTAL NA 500MG/VIL/NACL 0.9% KIT,INJ                        | Y                     |
| KIT             | 9512    | THIOPENTAL NA 500MG/VIL/WATER 20ML INJ                           | Y                     |
| KIT             | 9511    | THIOPENTAL NA 5GM/VIL/WATER 200ML INJ                            | Y                     |
| KIT             | 1716    | TUBERCULIN,OLD 5UNT/TEST INJ                                     | Y                     |
| KIT             | 1430    | TUBERCULIN,PURIFIED PROTEIN DERIVATIVE 5UNT/TEST INJ             | Y                     |
| LIQUID          | 9654    | ACIDULATED PHOSPHATE FLUORIDE 0.02% LIQUID                       | N                     |
| LIQUID          | 17509   | ACIDULATED PHOSPHATE FLUORIDE 0.044% LIQUID                      | N                     |
| LIQUID          | 9303    | ALCOHOL/BENZOIC ACID/EUCALYPTOL/METHYL SALICYLATE/THYMOL LIQUID  | N                     |
| LIQUID          | 10187   | ALCOHOL/EUCALYPTOL/MENTHOL/ME SALICYLATE/THYMOL MOUTHWASH        | N                     |
| LIQUID          | 3447    | BARIUM SO4 37.5% LIQUID                                          | N                     |
| LIQUID          | 3448    | BARIUM SO4 45% LIQUID                                            | N                     |
| LIQUID          | 3416    | BARIUM SO4 70% LIQUID,ORAL                                       | N                     |
| LIQUID          | 9318    | BAY RUM                                                          | N                     |
| LIQUID          | 3216    | BEER, CAN, 360ML                                                 | N                     |
| LIQUID          | 9640    | BENZALKONIUM CL 0.05%/OXYQUINOLINE SO4 LIQUID                    | N                     |
| LIQUID          | 7382    | BENZALKONIUM CL 0.2%/BENZOCAINE 18% LIQUID,DENT                  | N                     |
| LIQUID          | 9034    | BENZALKONIUM CL 17% LIQUID                                       | N                     |
| LIQUID          | 9035    | BENZALKONIUM CL 50% LIQUID                                       | N                     |
| LIQUID          | 9119    | BENZOCAINE 2.5%/CLOVE OIL 2.5% LIQUID                            | N                     |
| LIQUID          | 9459    | COMPLEAT REGULAR FORMULA LIQUID                                  | N                     |
| LIQUID          | 16862   | CRANBERRY JUICE                                                  | N                     |
| LIQUID          | 7413    | CRESOL 35%/FORMALDEHYDE 1% LIQUID                                | N                     |
| LIQUID          | 19166   | ENSURE LIQUID BUTTER PECAN                                       | N                     |
| LIQUID          | 7415    | EUCALYPTOL 93%/MENTHOL 3%/THYMOL 4% LIQUID                       | N                     |
| LIQUID          | 8560    | F D & C RED \#3 2% LIQUID                                        | N                     |
| LIQUID          | 16861   | GRAPEFRUIT JUICE                                                 | N                     |
| LIQUID          | 7414    | IODINE 6.2%/KI 4.45%/ZN P-PHENOSULFONATE 4.2% LIQUID             | N                     |
| LIQUID          | 9463    | ISOSOURCE LIQUID (VANILLA)                                       | N                     |
| LIQUID          | 17392   | JEVITY 1.5CAL LIQUID                                             | N                     |
| LIQUID          | 11722   | JEVITY LIQUID TUBE FEEDING                                       | N                     |
| LIQUID          | 13733   | JEVITY PLUS LIQUID TUBE FEEDING                                  | N                     |
| LIQUID          | 9383    | OLEIC ACID LIQUID                                                | N                     |
| LIQUID          | 8176    | SUSTACAL CHOCOLATE                                               | N                     |
| LIQUID          | 8177    | SUSTACAL EGG NOG                                                 | N                     |
| LIQUID          | 12127   | SUSTACAL HC LIQUID CHOCOLATE                                     | N                     |
| LIQUID          | 12126   | SUSTACAL HC LIQUID EGGNOG                                        | N                     |
| LIQUID          | 12125   | SUSTACAL HC LIQUID VANILLA                                       | N                     |
| LIQUID          | 8178    | SUSTACAL VANILLA                                                 | N                     |
| LIQUID          | 12123   | SUSTACAL W/FIBER LIQUID CHOCOLATE                                | N                     |
| LIQUID          | 12124   | SUSTACAL W/FIBER LIQUID STRAWBERRY                               | N                     |
| LIQUID          | 12122   | SUSTACAL W/FIBER LIQUID VANILLA                                  | N                     |
| LIQUID          | 15621   | VALERIAN LIQUID                                                  | N                     |
| LIQUID          | 3218    | WHISKEY                                                          | N                     |
| LIQUID          | 3217    | WINE                                                             | N                     |
| LIQUID          | 9405    | XYLENE,ANHYDROUS LIQUID                                          | N                     |
| LIQUID,ORAL     | 3449    | BARIUM SO4 1.5% LIQUID,ORAL                                      | N                     |
| LIQUID,ORAL     | 942     | DIATRIZOATE NA 42% LIQUID,ORAL                                   | N                     |
| LIQUID,ORAL     | 16632   | METHYLBENZETHONIUM CL 0.1% (AL & SF) LIQUID,ORAL                 | N                     |
| LIQUID,ORAL     | 14920   | METHYLBENZETHONIUM CL 0.1% LIQUID,ORAL                           | N                     |
| LIQUID,ORAL     | 20086   | RESOURCE DAIRY THICK VANILLA (NECTAR)                            | N                     |
| LIQUID,ORAL     | 20087   | RESOURCE DAIRY THICK VANILLA (HONEY)                             | N                     |
| LIQUID,ORAL     | 18131   | SIMPLYTHICK LIQUID,ORAL                                          | N                     |
| LIQUID,ORAL     | 18133   | SIMPLYTHICK LIQUID,ORAL HONEY                                    | N                     |
| LIQUID,ORAL     | 18132   | SIMPLYTHICK LIQUID,ORAL NECTAR                                   | N                     |
| LIQUID,ORAL     | 18154   | SOUR CHERRY JUICE                                                | N                     |
| LIQUID,ORAL     | 10128   | SUSPENDING VEHICLE (SF) LIQUID,ORAL                              | N                     |
| LIQUID,ORAL     | 10127   | SUSPENDING VEHICLE LIQUID,ORAL                                   | N                     |
| LIQUID,ORAL     | 7614    | SYRUP \#1 (MIKART) LIQUID                                        | N                     |
| LOZENGE         | 8787    | THROAT DISCS                                                     | N                     |
| MISCELLANEOUS   | 12611   | HELIDAC THERAPY PACK                                             | Y                     |
| MISCELLANEOUS   | 12862   | PREVPAC PATIENT THERAPY PAK                                      | Y                     |
| MOUTHWASH       | 18599   | BIOTENE MOUTHWASH                                                | Y                     |
| MOUTHWASH       | 18602   | CHLORHEXIDINE GLUCONATE 0.12% (AF) RINSE,ORAL                    | Y                     |
| MOUTHWASH       | 8197    | CHLORHEXIDINE GLUCONATE 0.12% RINSE,ORAL                         | Y                     |
| MOUTHWASH       | 17882   | PHENOL (DILUTE) 0.6% (AF) MOUTHWASH                              | Y                     |
| MOUTHWASH       | 16153   | PHENOL (DILUTE) 1.4% (AF) MOUTHWASH                              | Y                     |
| MOUTHWASH       | 4403    | SODIUM FLUORIDE 0.02% MOUTHWASH                                  | Y                     |
| OIL             | 9000    | COD LIVER OIL                                                    | Y                     |
| OIL             | 8666    | MINERAL OIL,EXTRA HEAVY                                          | Y                     |
| OIL             | 8669    | MINERAL OIL,HEAVY                                                | Y                     |
| OIL             | 8672    | MINERAL OIL,HEAVY,30ML                                           | Y                     |
| OIL             | 8668    | MINERAL OIL,MEDIUM                                               | Y                     |
| OIL             | 12057   | TRIGLYCERIDES,MEDIUM CHAIN OIL                                   | Y                     |
| OINT,TOP        | 626     | NITROGLYCERIN 2% OINT,TOP                                        | Y                     |
| PATCH           | 14347   | CAPSAICIN 0.25% PATCH                                            | N                     |
| PATCH           | 17524   | MENTHOL 1.4% PATCH                                               | N                     |
| PATCH           | 19676   | METHOL 5% PATCH                                                  | N                     |
| PATCH           | 18517   | TRANSMITTER PATCH MMT-7006                                       | N                     |
| PELLET          | 6914    | CELLULOSE,OXIDIZED 100% PELLET                                   | N                     |
| PELLET          | 9790    | OSCILLOCOCCINUM PELLET                                           | N                     |
| POWDER          | 3705    | SODIUM POLYSTYRENE SULFONATE PWDR                                | Y                     |
| POWDER,ORAL     | 9223    | AMIN-AID INSTANT DRINK PWDR                                      | N                     |
| POWDER,ORAL     | 3425    | BARIUM SO4 180GM/CUP PWDR,ORAL                                   | N                     |
| POWDER,ORAL     | 3426    | BARIUM SO4 8GM/CUP PWDR                                          | N                     |
| POWDER,ORAL     | 3415    | BARIUM SO4 95 % PWDR,ORAL                                        | N                     |
| POWDER,ORAL     | 3442    | BARIUM SO4 98.14% PWDR,ORAL                                      | N                     |
| POWDER,ORAL     | 12637   | BETAINE 1GM/1.7GM PWDR,ORAL                                      | N                     |
| POWDER,ORAL     | 13431   | BOOST PWDR VANILLA                                               | N                     |
| POWDER,ORAL     | 12386   | CARNATION INSTANT BREAKFAST PWDR,35.8GM                          | N                     |
| POWDER,ORAL     | 12129   | CASEC POWDER,ORAL                                                | N                     |
| POWDER,ORAL     | 12405   | CELLULOSE POWDER                                                 | N                     |
| POWDER,ORAL     | 9457    | CITROTEIN POWDER (ORANGE)                                        | N                     |
| POWDER,ORAL     | 9458    | CITROTEIN POWDER (PUNCH)                                         | N                     |
| POWDER,ORAL     | 12226   | CORPAK PRO-MIX \#22-9804 20GM/PKT PWDR                           | N                     |
| POWDER,ORAL     | 943     | DIATRIZOATE NA PWDR,ORAL                                         | N                     |
| POWDER,ORAL     | 17809   | ELECTROLYTE PWDR,ORAL                                            | N                     |
| POWDER,ORAL     | 17307   | ELECTROLYTE PWDR,ORAL ADULT PKT                                  | N                     |
| POWDER,ORAL     | 17810   | ELECTROLYTE PWDR,ORAL PKT                                        | N                     |
| POWDER,ORAL     | 10222   | ENSURE PWDR VANILLA                                              | N                     |
| POWDER,ORAL     | 11736   | FIBRAD PWDR,ORAL                                                 | N                     |
| POWDER,ORAL     | 9224    | HEPATIC-AID II POWDER (CHOCOLATE)                                | N                     |
| POWDER,ORAL     | 9226    | HEPATIC-AID II POWDER (CUSTARD)                                  | N                     |
| POWDER,ORAL     | 9225    | HEPATIC-AID II POWDER (EGGNOG)                                   | N                     |
| POWDER,ORAL     | 18506   | JUVEN PWDR PKT,23GM GRAPE                                        | N                     |
| POWDER,ORAL     | 18505   | JUVEN PWDR PKT,23GM ORANGE                                       | N                     |
| POWDER,ORAL     | 14281   | LIPISORB PWDR                                                    | N                     |
| POWDER,ORAL     | 12128   | LONALAC POWDER,ORAL                                              | N                     |
| POWDER,ORAL     | 9473    | MERITENE POWDER (CHOCOLATE)                                      | N                     |
| POWDER,ORAL     | 9474    | MERITENE POWDER (EGG NOG)                                        | N                     |
| POWDER,ORAL     | 9476    | MERITENE POWDER (MILK CHOCOLATE)                                 | N                     |
| POWDER,ORAL     | 9472    | MERITENE POWDER (PLAIN)                                          | N                     |
| POWDER,ORAL     | 9477    | MERITENE POWDER (STRAWBERRY)                                     | N                     |
| POWDER,ORAL     | 9475    | MERITENE POWDER (VANILLA)                                        | N                     |
| POWDER,ORAL     | 14287   | NEOCATE ONE+ PWDR                                                | N                     |
| POWDER,ORAL     | 10244   | POLYCOSE PWDR,ORAL                                               | N                     |
| POWDER,ORAL     | 11729   | PROMOD PWDR,ORAL                                                 | N                     |
| POWDER,ORAL     | 19488   | PROTEIN SUPPLEMENT,PRONUTRA PWDR PKT, 37GM                       | N                     |
| POWDER,ORAL     | 19943   | PROTEIN SUPPLEMENT,PROPASS PWDR                                  | N                     |
| POWDER,ORAL     | 19281   | PROTEIN SUPPLEMENT,PROPASS PWDR PKT,8GM                          | N                     |
| POWDER,ORAL     | 17725   | RESOURCE BENEPROTEIN PWDR                                        | N                     |
| POWDER,ORAL     | 19376   | RESOURCE BENEPROTEIN PWDR,227GM                                  | N                     |
| POWDER,ORAL     | 17726   | RESOURCE BENEPROTEIN PWDR,PKT,7GM                                | N                     |
| POWDER,ORAL     | 9241    | S-M-A IRON FORTIFIED,INFANT FORMULA PWDR                         | N                     |
| POWDER,ORAL     | 9245    | S-M-A LO-IRON,INFANT FORMULA PWDR                                | N                     |
| POWDER,ORAL     | 17858   | THICK & EASY PWDR                                                | N                     |
| POWDER,ORAL     | 17857   | THICK & EASY PWDR PKT,8GM                                        | N                     |
| POWDER,ORAL     | 18562   | THICK & EASY THICKEND COFFEE (HONEY) PWDR PKT,12GM               | N                     |
| POWDER,ORAL     | 18561   | THICK & EASY THICKEND COFFEE (NECTAR) PWDR PKT,12GM              | N                     |
| POWDER,ORAL     | 18559   | THICK & EASY THICKEND TEA (HONEY) PWDR,PKT,12GM                  | N                     |
| POWDER,ORAL     | 18558   | THICK & EASY THICKEND TEA (NECTAR) PWDR PKT,12GM                 | N                     |
| POWDER,ORAL     | 12426   | THICKENUP POWDER                                                 | N                     |
| POWDER,ORAL     | 16179   | THICK-IT 2 POWDER                                                | N                     |
| POWDER,ORAL     | 16194   | THICK-IT POWDER                                                  | N                     |
| POWDER,ORAL     | 9227    | TRAUM-AID HBC PWDR (LEMONCREME)                                  | N                     |
| POWDER,ORAL     | 14144   | VITAL HIGH NITROGEN 79GM PWDR/PKT VANILLA                        | N                     |
| POWDER,ORAL     | 11735   | VITAL HIGH NITROGEN PWDR VANILLA                                 | N                     |
| POWDER,ORAL     | 12508   | VIVONEX T.E.N. POWDER,PKT,80.4GM                                 | N                     |
| POWDER,ORAL     | 3029    | XYLOSE 100GM/BTL PWDR,ORAL                                       | N                     |
| PWDR,RENST-ORAL | 15985   | ALITRAQ VANILLA 76GM/PKT PWDR                                    | N                     |
| PWDR,RENST-ORAL | 3440    | BARIUM SO4 315GM PWDR,ORAL                                       | N                     |
| PWDR,RENST-ORAL | 3439    | BARIUM SO4 96% PWDR                                              | N                     |
| PWDR,RENST-ORAL | 14862   | IMMUNOCAL PWDR,PKT,10GM                                          | N                     |
| PWDR,RENST-ORAL | 1136    | IPODATE CA 3GM/PKG PWDR                                          | N                     |
| PWDR,RENST-ORAL | 19601   | RESOURCE ARGINAID (CHERRY) 4.5GM/PKT,9.2GM                       | N                     |
| PWDR,RENST-ORAL | 19603   | RESOURCE ARGINAID (LEMON) 4.5GM/PKT,9.2GM                        | N                     |
| PWDR,RENST-ORAL | 19602   | RESOURCE ARGINAID (ORANGE) 4.5GM/PKT,9.2GM                       | N                     |
| PWDR,RENST-ORAL | 14326   | SCANDISHAKE PWDR/PKT,85GM CHOCOLATE                              | N                     |
| PWDR,RENST-ORAL | 14325   | SCANDISHAKE PWDR/PKT,85GM STRAWBERRY                             | N                     |
| PWDR,RENST-ORAL | 14327   | SCANDISHAKE PWDR/PKT,85GM VANILLA                                | N                     |
| PWDR,RENST-ORAL | 8180    | SUSTACAL PWDR CHOCOLATE                                          | N                     |
| PWDR,RENST-ORAL | 8181    | SUSTACAL PWDR VANILLA                                            | N                     |
| PWDR,RENST-ORAL | 8189    | SUSTAGEN PWDR CHOCOLATE                                          | N                     |
| PWDR,RENST-ORAL | 8190    | SUSTAGEN PWDR VANILLA                                            | N                     |
| PWDR,RENST-ORAL | 12511   | VIVONEX FLAVOR PACKET CHERRY-VANILLA                             | N                     |
| PWDR,RENST-ORAL | 12512   | VIVONEX FLAVOR PACKET LEMON-LIME                                 | N                     |
| PWDR,RENST-ORAL | 12513   | VIVONEX FLAVOR PACKET ORANGE-PINEAPPLE                           | N                     |
| PWDR,RENST-ORAL | 12509   | VIVONEX FLAVOR PACKET RASPBERRY                                  | N                     |
| PWDR,RENST-ORAL | 12510   | VIVONEX FLAVOR PACKET VANILLA                                    | N                     |
| PWDR,RENST-ORAL | 12514   | VIVONEX PEDIATRIC POWDER,PKT,51GM                                | N                     |
| PWDR,RENST-ORAL | 12515   | VIVONEX PLUS POWDER,PKT,84GM                                     | N                     |
| RINSE,ORAL      | 8193    | CHLORHEXIDINE GLUCONATE 0.12% RINSE,ORAL                         | Y                     |
| SOLN,ORAL       | 9257    | BENZOCAINE 6.3%/PHENOL 0.5% SOLN,DENT                            | N                     |
| SOLN,ORAL       | 928     | DIATRIZOATE MEGLUMINE 66%/DIATRIZOATE NA 10% SOLN,ORAL           | N                     |
| SOLN,ORAL       | 938     | DIATRIZOATE MEGLUMINE 66%/DIATRIZOATE NA 10% SOLN,ORAL/RTL       | N                     |
| SOLN,ORAL       | 16926   | DYE FDC (BLUE \#1) SOLN,ORAL                                     | N                     |
| SOLN,ORAL       | 924     | SODIUM IODIDE,I-131,2MIL/ML SOLN,ORAL                            | N                     |
| SUSP            | 17828   | BARIUM SO4 0.1% SUSP,ORAL                                        | N                     |
| SUSP            | 3441    | BARIUM SO4 1.2% SUSP                                             | N                     |
| SUSP            | 18417   | BARIUM SO4 1.3% SUSP                                             | N                     |
| SUSP            | 3417    | BARIUM SO4 1.5% SUSP,ORAL                                        | N                     |
| SUSP            | 3465    | BARIUM SO4 100% SUSP,ORAL                                        | N                     |
| SUSP            | 3464    | BARIUM SO4 2.1% SUSP                                             | N                     |
| SUSP            | 3454    | BARIUM SO4 2.2% SUSP,ORAL                                        | N                     |
| SUSP            | 3457    | BARIUM SO4 35% SUSP,ORAL                                         | N                     |
| SUSP            | 3450    | BARIUM SO4 4.5% SUSP,ORAL                                        | N                     |
| SUSP            | 17829   | BARIUM SO4 40% SUSP,ORAL                                         | N                     |
| SUSP            | 3455    | BARIUM SO4 5% SUSP,ORAL                                          | N                     |
| SUSP            | 3453    | BARIUM SO4 50% SUSP                                              | N                     |
| SUSP            | 3446    | BARIUM SO4 55% SUSP,ORAL                                         | N                     |
| SUSP            | 3422    | BARIUM SO4 60% SUSP                                              | N                     |
| SUSP            | 3423    | BARIUM SO4 70% SUSP,RTL                                          | N                     |
| SUSP            | 7779    | PROPYLIODONE 60% SUSP                                            | N                     |
| SUSP            | 3378    | TECHNETIUM-99m 2.5MIL AGGREGATED ALBUMIN (HUMAN) INJ             | N                     |
| SUSP,ORAL       | 15180   | RADIACARE WOUND RINSE, ORAL,SUSP                                 | N                     |
| SUSP,RTL        | 3413    | BARIUM SO4 57% SUSP,RTL                                          | N                     |
| SUSP,RTL        | 3414    | BARIUM SO4 61% SUSP,RTL                                          | N                     |
| SUSP,RTL        | 3438    | BARIUM SO4 75% SUSP,RTL                                          | N                     |
| SUSP,RTL        | 3420    | BARIUM SO4 85% SUSP,RTL                                          | N                     |
| SYRINGE         | 2737    | TETANUS IMMUNE GLOBULIN,HUMAN 250UNT/ML INJ,SYRINGE,1ML          | Y                     |
| SYRUP           | 7233    | BROWN MIXTURE                                                    | N                     |
| SYRUP           | 9395    | SIMPLE SYRUP                                                     | N                     |
| SYRUP           | 9560    | WILD CHERRY SYRUP                                                | N                     |
| SYRUP           | 9623    | WILD CHERRY SYRUP                                                | N                     |
| SYRUP,ORAL      | 14922   | CHERRY SYRUP                                                     | N                     |
| TAB             | 5365    | AMINO ACIDS TAB                                                  | N                     |
| TAB             | 3451    | BARIUM SO4 650MG TAB                                             | N                     |
| TAB             | 12951   | CHLOROPHYLL 20MG TAB                                             | N                     |
| TAB             | 17176   | CHLOROPHYLLIN 3MG/THYMOL 0.6MG TAB                               | N                     |
| TAB             | 9190    | CHLOROPHYLLIN COPPER COMPLEX 100MG TAB                           | N                     |
| TAB             | 9192    | CHLOROPHYLLIN COPPER COMPLEX 14MG TAB                            | N                     |
| TAB             | 14289   | CHLOROPHYLLIN COPPER COMPLEX 33.3MG TAB                          | N                     |
| TAB             | 3358    | IOCETAMIC ACID 750MG TAB                                         | N                     |
| TAB             | 3790    | IOPANOIC ACID 500MG TAB                                          | N                     |
| TAB             | 9537    | OAT BRAN 800MG TAB                                               | N                     |
| TAB             | 6995    | PLACEBO TAB                                                      | N                     |
| TAB             | 12258   | STERICOL DEODORANT TAB -NOT FOR ORAL USE                         | N                     |
| TAB             | 1996    | METHENAMINE TAB FOR TIMED BURNING (DO NOT TAKE)                  | N                     |
| TAB,CHEWABLE    | 9536    | OAT BRAN 800MG TAB,CHEWABLE                                      | N                     |
| TAB,EFFERVSC    | 10160   | ENZYMATIC CLEANER (PANCREATIN) TAB,OPH,EFFERVSC                  | N                     |
| TAB,EFFERVSC    | 10107   | ENZYMATIC CLEANER (SUBTILISIN A) TAB,OPH,EFFERVSC                | N                     |
| TAB,EFFERVSC    | 10108   | ENZYMATIC CLEANER (ULTRAZYME) TAB,OPH,EFFERVSC                   | N                     |
| TAB,SOLUBLE     | 10022   | ANTI-RUST TAB (NOT FOR ORAL USE)                                 | N                     |
| TAB,SOLUBLE     | 11713   | APPLIANCE DEODORANT TAB (DO NOT TAKE)                            | N                     |
| TAB,SOLUBLE     | 10159   | ENZYMATIC CLEANER (OPTI-FREE) TAB,OPH                            | N                     |
| TAB,SOLUBLE     | 10161   | ENZYMATIC CLEANER (PANCREATIN) TAB,OPH                           | N                     |
| TAB,SOLUBLE     | 10003   | ENZYMATIC CLEANER (PAPAIN) TAB,OPH                               | N                     |
| TAB,SOLUBLE     | 10158   | ENZYMATIC CLEANER (PAPAIN) TAB,OPH                               | N                     |
| TAB,SOLUBLE     | 19991   | SODIUM CHLORIDE 1GM (TOPICAL) TAB,SOLUBLE                        | N                     |
| TAB,SOLUBLE     | 496     | SODIUM CHLORIDE 250MG TAB, OPH                                   | N                     |
| TINCTURE        | 658     | BELLADONNA ALKALOIDS 0.27MG/ML TINCTURE                          | Y                     |
| TINCTURE        | 660     | BELLADONNA ALKALOIDS 0.3MG/ML TINCTURE                           | Y                     |
| TINCTURE        | 655     | BELLADONNA LEAF 0.3MG/ML TINCTURE                                | Y                     |

## # # Appendix E: Examples of Local Medication Route Mappings to Standard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Medication Routes (File 51.2) | Standard Route | FDB Route    | Outpatient Expansion               |
|-----------------------------------|--------------------|------------------|----------------------------------------|
| AFFECTED AREA                     | TOPICAL            | TOPICAL          | TOPICALLY TO AFFECTED AREA             |
| AGAINST CHEST WALL                | TRANSDERMAL        | TRANSDERMAL      | AGAINST CHEST WALL                     |
| APPLY TO NARES                    | NASAL              | INTRANASAL       |                                        |
| BLADDER INSTILATTION              | IRRIGATION         | IRRIGATION       |                                        |
| BLOOD TEST                        | NOT APPLICABLE     | NOT APPLICABLE   |                                        |
| BOTH EARS                         | OTIC               | OTIC             | BOTH EARS                              |
| BOTH EYES                         | OPHTHALMIC         | OPHTHALMIC       | BOTH EYES                              |
| BUCCAL                            | BUCCAL             | BUCCAL           | CHEEK AND GUM UNTIL DISSOLVED          |
| BY MOUTH                          | ORAL               | ORAL             | MOUTH                                  |
| BY MOUTH OR INTRAMUSCULARLY       | NOT APPLICABLE     | NOT APPLICABLE   |                                        |
| BY MOUTH OR INTRAVENOUSLY         | NOT APPLICABLE     | NOT APPLICABLE   |                                        |
| CATHETER                          | URETHRAL           | INTRA-URETHRAL   |                                        |
| CAUDAL BLOCK                      | INTRACAUDAL        | CAUDAL BLOCK     |                                        |
| CONTACTS                          | OPHTHALMIC         | OPHTHALMIC       | CONTACTS                               |
| DEEP IM                           | INTRAMUSCULAR      | INTRAMUSCULAR    |                                        |
| DENTAL                            | DENTAL             | DENTAL           |                                        |
| DENTAL ORAL TOPICAL               | DENTAL             | DENTAL           | IN MOUTH                               |
| EACH EYE                          | OPHTHALMIC         | OPHTHALMIC       | EACH EYE                               |
| EPIDURAL                          | EPIDURAL           | EPIDURAL         |                                        |
| EXTERNALLY                        | TOPICAL            | TOPICAL          | EXTERNALLY                             |
| FINGERSTICK                       | NOT APPLICABLE     | NOT APPLICABLE   |                                        |
| FOR BLOOD GLUCOSE TEST USE        | NOT APPLICABLE     | NOT APPLICABLE   | FOR BLOOD GLUCOSE TEST USE             |
| FOR COLOSTOMY USE                 | NOT APPLICABLE     | NOT APPLICABLE   | FOR COLOSTOMY USE                      |
| FOR INCONTINENT USE               | NOT APPLICABLE     | NOT APPLICABLE   | FOR INCONTINENT USE                    |
| FOR INSULIN INJECTION PURPOSE     | NOT APPLICABLE     | NOT APPLICABLE   | FOR INSULIN INJECTION PURPOSE          |
| FOR INTRAVENOUS INFUSION PURPOSE  | INTRAVENOUS        | INTRAVENOUS      | FOR INTRAVENOUS INFUSION PURPOSE       |
| FOR OSTOMY CARE USE               | NOT APPLICABLE     | NOT APPLICABLE   | FOR OSTOMY CARE USE                    |
| G TUBE                            | ENTERAL            | ORAL             | GASTRIC TUBE                           |
| GARGLE                            | ORAL               | ORAL             | GARGLE                                 |
| GASTROSTOMY TUBE                  | ENTERAL            | ORAL             |                                        |
| INFILTRATION                      | INFILTRATION       | INFILTRATION     |                                        |
| INHALATION                        | INHALATION         | INHALATION       | INHALATION                             |
| INHALATION NASAL                  | NASAL              | INTRANASAL       | NASAL INHALATION                       |
| INHALATION ORAL                   | INHALATION         | INHALATION       | ORAL INHALATION                        |
| INTRA-ABDOMINAL                   | INTRAPERITONEAL    | INTRAPERITONEAL  |                                        |
| INTRA-AMNIOTIC                    | INTRA-AMNIOTIC     |                  |                                        |
| INTRA-ARTERIAL                    | INTRA-ARTERIAL     | INTRA-ARTERIAL   |                                        |
| INTRA-ARTICULAR                   | INTRA-ARTICULAR    | INTRA-ARTICULAR  | INTO THE JOINT                         |
| INTRABURSAL                       | INTRABURSAL        | INTRABURSAL      |                                        |
| INTRACARDIAC                      | INTRACARDIAC       | INTRACARDIAC     |                                        |
| INTRA-CAVERNOUSLY                 | INTRACAVERNOSAL    | INTRA-CAVERNOSAL | INTRA-CAVERNOUSLY                      |
| INTRACAVITY                       | INTRACAVITARY      | INTRACAVITY      |                                        |
| INRTRACORPOREAL                   | INTRACAVERNOSAL    | INTRA-CAVERNOSAL | INTO PENIS                             |
| INTRADERMAL                       | INTRADERMAL        | INTRADERMAL      | INTRADERMAL                            |
| INTRAFOLLICULAR                   | \<LEAVE UNMAPPED\> |                  |                                        |
| INTRAMUSCULAR                     | INTRAMUSCULAR      | INTRAMUSCULAR    | INTRAMUSCULAR                          |
| INTRAMUSCULAR                     | INTRAMUSCULAR      | INTRAMUSCULAR    |                                        |
| INTRAMUSCULARLY OR BY MOUTH       | NOT APPLICABLE     | NOT APPLICABLE   |                                        |
| INTRANASALY                       | NASAL              | INTRANASAL       | IN NOSTRIL(S)                          |
| INTRAOCULAR                       | INTRAOCULAR        | INTRAOCULAR      | IN EYE(S)                              |
| INTRAPERITONEAL                   | INTRAPERITONEAL    | INTRAPERITONEAL  |                                        |
| INTRASPINAL                       | INTRASPINAL        | INTRASPINAL      |                                        |
| INTRASYNOVIAL                     | INTRASYNOVIAL      | INTRASYNOVIAL    |                                        |
| INTRATHECAL                       | INTRATHECAL        | INTRATHECAL      |                                        |
| INTRATHORACIC                     | \<LEAVE UNMAPPED\> |                  |                                        |
| INTRATRACHEAL                     | INTRATRACHEAL      | INTRATRACHEAL    |                                        |
| INTRAUTERINE                      | INTRAUTERINE       | INTRAUTERINE     |                                        |
| INTRAVENEOUS (PCA)                | INTRAVENOUS        | INTRAVENOUS      |                                        |
| INTRAVENOUS                       | INTRAVENOUS        | INTRAVENOUS      | INTRAVENOUS                            |
| INTRAVENOUS DEVICE                | NOT APPLICABLE     | NOT APPLICABLE   |                                        |
| INTRAVENOUSLY OR BY MOUTH         | NOT APPLICABLE     | NOT APPLICABLE   |                                        |
| INTRAVESICAL                      | INTRAVESICAL       | INTRAVESICAL     |                                        |
| INTRAVITREOUS                     | INTRAVITREAL       | INTRAVITREAL     |                                        |
| IRRIGATION                        | IRRIGATION         | IRRIGATION       |                                        |
| IRRIGATION OPHTHALMIC             | IRRIGATION         | IRRIGATION       |                                        |
| IV PIGGYBACK                      | INTRAVENOUS        | INTRAVENOUS      |                                        |
| IV PUSH                           | INTRAVENOUS        | INTRAVENOUS      |                                        |
| J TUBE                            | E                  | ORAL             |                                        |
| LEFT EAR                          | OTIC               | OTIC             | LEFT EAR                               |
| LEFT EYE                          | OPHTHALMIC         | OPHTHALMIC       | LEFT EYE                               |
| MISCELLANEOUS                     | NOT APPLICABLE     | NOT APPLICABLE   |                                        |
| NASAL                             | NASAL              | INTRANASAL       |                                        |
| NASAL                             | NASAL              | INTRANASAL       |                                        |
| NASA L CANNULA                    | NASAL              | INTRANASAL       | NASAL CANNULA                          |
| NASO-GASTRIC TUBE                 | ENTERAL            | ORAL             | VIA NG TUBE                            |
| NEBULIZER                         | INHALATION         | INHALATION       | VIA NEBULIZER                          |
| NG TUBE                           | ENTERAL            | ORAL             | NASO-GASTRIC TUBE                      |
| NOSE                              | NASAL              | INTRANASAL       | EACH NOSTRIL                           |
| NOSTRIL                           | NASAL              | INTRANASAL       | ONE NOSTRIL                            |
| ONE NOSTRIL                       | NASAL              | INTRANASAL       | ALTERNATE NOSTRIL                      |
| OPHTHALMIC                        | OPHTHALMIC         | OPHTHALMIC       | AFFECTED EYE(S)                        |
| ORAL INHALATION                   | ORAL               | ORAL             | BY MOUTH                               |
| ORAL TOPICAL                      | ORAL               | ORAL             | IN MOUTH                               |
| ORAL/RECTAL                       | NOT APPLICABLE     | NOT APPLICABLE   |                                        |
| OTIC                              | OTIC               | OTIC             | AFFECTED EAR(S)                        |
| PEG TUBE                          | ORAL               | ORAL             | VIA PEG TUBE                           |
| PERCUTANEOUS                      | TRANSDERMAL        | TRANSDERMAL      |                                        |
| PERITONEAL DIALYSIS               | INTRAPERITONEAL    | INTRAPERITONEAL  | PERITONEAL DIALYSIS                    |
| PREP KIT                          | NOT APPLICABLE     | NOT APPLICABLE   |                                        |
| RECTAL                            | RECTAL             | RECTAL           | RECTUM                                 |
| RECTALLY                          | RECTAL             | RECTAL           | RECTALLY                               |
| RECTAL ORAL                       | NOT APPLICABLE     | NOT APPLICABLE   | RECTALLY AND ORALLY                    |
| RETROBULBAR                       | RETROBULBAR        | RETROBULBAR      |                                        |
| RIGHT EAR                         | OTIC               | OTIC             | RIGHT EAR                              |
| RIGHT EYE                         | OPHTHALMIC         | OPHTHALMIC       | RIGHT EYE                              |
| SUBCUTANEOUS                      | SUBCUTANEOUS       | SUBCUTANEOUS     | UNDER THE SKIN                         |
| SUBCUTANEOUS INTRAVENOUS          | NOT APPLICABLE     | NOT APPLICABLE   |                                        |
| SUBLINGUAL                        | SUBLINGUAL         | SUBLINGUAL       | UNDER THE TONGUE                       |
| TOPICAL                           | TOPICAL            | TOPICAL          | TOPICALLY                              |
| TOPICAL BUCCAL                    | BUCCAL             | BUCCAL           | ON TONGUE TO DISSOLVE AND THEN SWALLOW |
| TOPICAL DENTAL                    | DENTAL             | DENTAL           | MOUTH                                  |
| TRACH                             | INTRATRACHEAL      | INTRATRACHEAL    | FOR TRACH CARE                         |
| TRANSDERMAL                       | TRANSDERMAL        | TRANSDERMAL      | ON SKIN                                |
| URETHRAL                          | URETHRAL           | INTRA-URETHRAL   | URETHRALLY                             |
| VAGINAL                           | VAGINAL            | VAGINAL          | VAGINAL                                |
| VAGINAL TOPICAL                   | VAGINAL            | VAGINAL          | TO VAGINA AREA                         |
| VAGINALLY                         | VAGINAL            | VAGINAL          | VAGINALLY                              |
| VIA FEEDING TUBE                  | ENTERAL            | ORAL             | VIA FEEDING TUBE                       |

*Page included for two-sided copying*

## # Appendix F: Local Possible Dosages Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\(3041\) ABACAVIR SO4 600MG/LAMIVUDINE 300MG TAB

RESTRICTED TO ID

Strength: Units: Application Package: OU

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: ABACAVIR SO4 600MG/LAMIVUDINE 300MG TAB

\(667\) ABACAVIR300/LAMIVUDINE150/ZDV 300MG TAB

RESTRICTED TO INFECTIOUS DISEASE

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: ABACAVIR SO4 300MG/LAMIVUDINE 150MG/ZIDOVUDINE 300MG TAB

\(2587\) ACETAMINOPHEN 160MG/5ML LIQUID

Strength: 160 Units: MG/5ML Application Package: OUX

Local Possible Dosages:

1 TABLESPOONFUL

Numeric Dose: 480 Dose Unit: MILLIGRAM(S) Package: IO

2 TABLESPOONFULS

Numeric Dose: 960 Dose Unit: MILLIGRAM(S) Package: IO

1 TEASPOONFUL

Numeric Dose: 160 Dose Unit: MILLIGRAM(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 320 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: ACETAMINOPHEN 160MG/5ML LIQUID

\(8404\) ACETAMINOPHEN 325MG TAB

Strength: 325 Units: MG Application Package: UOX

Local Possible Dosages:

1 TABLET

Numeric Dose: 325 Dose Unit: MILLIGRAM(S) Package: IO

2 TABLET(S)

Numeric Dose: 650 Dose Unit: MILLIGRAM(S) Package: IO

1-2 TABLET(S)

Numeric Dose: 650 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: ACETAMINOPHEN 325MG TAB

\(264\) ACETAMINOPHEN 650MG RTL SUPP

Strength: 650 Units: MG Application Package: UOX

Local Possible Dosages:

1 SUPPOSITORY

Numeric Dose: 650 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: ACETAMINOPHEN 650MG SUPP,RTL

\(342\) ACETAMINOPHEN WITH CODEINE 30MG TAB

Strength: Units: Application Package: ONX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

2 TABLETS

Numeric Dose: 2 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: CODEINE 30MG/ACETAMINOPHEN 300MG TAB

\(7423\) ACETAMINOPHEN/CODEINE 30MG TAB U/D 25'S

Strength: Units: Application Package: NU

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: CODEINE 30MG/ACETAMINOPHEN 300MG TAB

\(971\) ACETAMINOPHEN/CODEINE(120-12MG)/5ML ELIX

Dispense only on multi. of 118 (118, 236, 354, 472 ML)

Strength: Units: Application Package: ONX

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 1 Dose Unit: TEASPOONFUL(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 2 Dose Unit: TEASPOONFUL(S) Package: IO

1 TABLESPOONFUL

Numeric Dose: 1 Dose Unit: TABLESPOONFUL(S) Package: IO

2 TABLESPOONFULS

Numeric Dose: 2 Dose Unit: TABLESPOONFUL(S) Package: IO

VA PRODUCT MATCH: CODEINE 12MG/ACETAMINOPHEN 120MG/5ML ELIXIR

\(7245\) ACETAMINOPHEN/CODEINE(300MG/30MG)/12.5ML

Strength: Units: Application Package: UN

Local Possible Dosages:

1 CUP 12.5ML(300/30MG)

Numeric Dose: 2.5 Dose Unit: TEASPOONFUL(S) Package: I

2 CUP(S) 25ML (600/60MG)

Numeric Dose: 5 Dose Unit: TEASPOONFUL(S) Package: I

VA PRODUCT MATCH: CODEINE 12MG/ACETAMINOPHEN 120MG/5ML ELIXIR

\(3868\) ACETIC ACID 2% OTIC SOL

Strength: Units: Application Package: XUO

Local Possible Dosages:

1 DROP

Numeric Dose: 1 Dose Unit: DROP(S) Package: IO

2 DROPS

Numeric Dose: 2 Dose Unit: DROP(S) Package: IO

VA PRODUCT MATCH: ACETIC ACID 2% SOLN,OTIC

\(5927\) ACETIC ACID 2.47/AL SO4 0.79% OTIC SOLN

Strength: Units: Application Package: UOX

Local Possible Dosages:

1 DROP

Numeric Dose: 1 Dose Unit: DROP(S) Package: IO

2 DROPS

Numeric Dose: 2 Dose Unit: DROP(S) Package: IO

VA PRODUCT MATCH: ACETIC ACID 2.47%/ALUMINUM SO4 0.79% SOLN,OTIC

\(3997\) ACETIC ACID 2/HC 1% OTIC SOLN

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 DROP

Numeric Dose: 1 Dose Unit: DROP(S) Package: IO

2 DROPS

Numeric Dose: 2 Dose Unit: DROP(S) Package: IO

VA PRODUCT MATCH: ACETIC ACID 2%/HYDROCORTISONE 1% SOLN,OTIC

\(749\) ACETYLCHOLINE CL 1% SOLN,OPH

RESTRICTED TO OPHTHALMOLOGY

Strength: Units: Application Package: UOX

Local Possible Dosages:

1 DROP

Numeric Dose: 1 Dose Unit: DROP(S) Package: IO

2 DROPS

Numeric Dose: 2 Dose Unit: DROP(S) Package: IO

VA PRODUCT MATCH: ACETYLCHOLINE CL 1% SOLN,OPH

\(173\) ACETYLCYSTEINE 10% INHL SOLN 10ML

ORDER IN INCREMENTS OF 3'S

Strength: Units: Application Package: OUX

Local Possible Dosages:

4MLS

Numeric Dose: 4 Dose Unit: MILLILITER(S) Package: IO

10MLS

Numeric Dose: 10 Dose Unit: MILLILITER(S) Package: IO

5MLS

Numeric Dose: 5 Dose Unit: MILLILITER(S) Package: IO

6MLS

Numeric Dose: 6 Dose Unit: MILLILITER(S) Package: IO

1ML

Numeric Dose: 1 Dose Unit: MILLILITER(S) Package: IO

0.5ML

Numeric Dose: 0.5 Dose Unit: MILLILITER(S) Package: IO

VA PRODUCT MATCH: ACETYLCYSTEINE 10% (PF) SOLN,INHL,10ML

\(5234\) ACETYLCYSTEINE 10% INHL SOLN 30ML

DO YOU NEED TO ORDER ALBUTEROL/ATROVENT WITH THIS ORDER.

Strength: Units: Application Package: UOX

Local Possible Dosages:

600MG/6ML

Numeric Dose: 600 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: ACETYLCYSTEINE 10% SOLN,INHL,30ML

\(1634\) ACETYLCYSTEINE 20% INHL SOLN 10ML

DO YOU NEED TO ORDER ALBUTEROL/ATROVENT WITH THIS ORDER.

Strength: Units: Application Package: OUX

Local Possible Dosages:

600MG/3ML

Numeric Dose: 600 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: ACETYLCYSTEINE 20% SOLN,INHL

\(24224\) ACIDOPHILUS CAP \*N/F\*

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 CAPSULE

Numeric Dose: 1 Dose Unit: CAPSULE(S) Package: IO

2 CAPSULES

Numeric Dose: 2 Dose Unit: CAPSULE(S) Package: IO

VA PRODUCT MATCH: ACIDOPHILUS CAP

\(800\) ACTIVATED CHARCOAL USP 25GM/120 ML

Strength: Units: Application Package: UOX

Local Possible Dosages:

25 GM

Numeric Dose: 25 Dose Unit: GRAM(S) Package: IO

50 GM

Numeric Dose: 50 Dose Unit: GRAM(S) Package: IO

VA PRODUCT MATCH: CHARCOAL,ACTIVATED 25GM/120ML LIQUID

\(1259\) ACTIVATED CHARCOAL WITH SORBITOL LIQ

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 1 Dose Unit: TEASPOONFUL(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 2 Dose Unit: TEASPOONFUL(S) Package: IO

1 TABLESPOONFUL

Numeric Dose: 1 Dose Unit: TABLESPOONFUL(S) Package: IO

2 TABLESPOONFULS

Numeric Dose: 2 Dose Unit: TABLESPOONFUL(S) Package: IO

VA PRODUCT MATCH: CHARCOAL,ACTIVATED 25GM/SORBITOL 120ML LIQUID

\(2676\) ALBUT 3/IPRAT 0.5MG/3ML DUONEB INH 3ML

INPATIENT USE ONLY

Strength: Units: Application Package: UX

Local Possible Dosages:

ONE BULLET (3ML)

Numeric Dose: 3 Dose Unit: MILLILITER(S) Package: IO

VA PRODUCT MATCH: ALBUTEROL SO4 3MG/IPRATROPIUM BR 0.5MG/3ML INHL,3ML

\(24415\) ALBUTEROL 90/IPRATROP 18MCG 200D PO INHL

AVOID WITH PEANUT ALLERGY

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 PUFF

Numeric Dose: 1 Dose Unit: INHALATION(S) Package: IO

2 PUFFS

Numeric Dose: 2 Dose Unit: INHALATION(S) Package: IO

1 SPRAY

Numeric Dose: 1 Dose Unit: SPRAY(S) Package: IO

2 SPRAYS

Numeric Dose: 2 Dose Unit: SPRAY(S) Package: IO

1 INHALATION

Numeric Dose: 1 Dose Unit: INHALATION(S) Package: IO

2 INHALATIONS

Numeric Dose: 2 Dose Unit: INHALATION(S) Package: IO

VA PRODUCT MATCH: ALBUTEROL 90MCG/IPRATROPIUM BR 18MCG/SPRAY INHALER,ORAL,14.7GM

\(4111\) ALBUTEROL 90MCG (CFC-F) 200D ORAL INHL

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 PUFF

Numeric Dose: 1 Dose Unit: INHALATION(S) Package: IO

2 PUFFS

Numeric Dose: 2 Dose Unit: INHALATION(S) Package: IO

VA PRODUCT MATCH: ALBUTEROL SO4 90MCG/ACTUAT (CFC-F) INHL,ORAL,8.5GM

\(7055\) ALBUTEROL SO4 0.083% INHL 3ML

Strength: Units: Application Package: UOX

Local Possible Dosages:

ONE BULLET (3ML)

Numeric Dose: 3 Dose Unit: MILLILITER(S) Package: IO

VA PRODUCT MATCH: ALBUTEROL SO4 0.083% INHL,3ML

\(24006\) ALDESLEUKIN 22MILLION UNT/VIL INJ

CAUTION!!! CAN ONLY BE ORDER BY A HEM/ONC ATTENDING

Strength: 22 Units: MILLION UNT/VIL Application Package: IOUX

Local Possible Dosages:

22 MILLION UNITS/VIAL

Numeric Dose: 22 Dose Unit: MILLIONUNIT(S) Package: IO

VA PRODUCT MATCH: ALDESLEUKIN 22MILLION UNT/VIL INJ

\(4157\) ALENDRONATE 70/VIT D TAB \*N/F\*

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: ALENDRONATE SODIUM 70MG/CHOLECALCIFEROL 2800UNIT TAB

\(8138\) ALFENTANIL 500MCG/ML 5ML INJ 10'S

RESTRICTED TO OR & ANES

Strength: 500 Units: MCG/ML Application Package: UOSX

Local Possible Dosages:

500 MCG/ML

Numeric Dose: 500 Dose Unit: MICROGRAM(S) Package: O

1000 MCG/2 ML

Numeric Dose: 1000 Dose Unit: MICROGRAM(S) Package: O

1500 MCG/3ML

Numeric Dose: 1500 Dose Unit: MICROGRAM(S) Package: O

2000 MCG/4ML

Numeric Dose: 2000 Dose Unit: MICROGRAM(S) Package: O

2500 MCG/5ML

Numeric Dose: 2500 Dose Unit: MICROGRAM(S) Package: O

3000 MCG/6ML

Numeric Dose: 3000 Dose Unit: MICROGRAM(S) Package: O

VA PRODUCT MATCH: ALFENTANIL HCL 500MCG/ML INJ

\(2156\) ALOH/MG CARB/NA ALGINATE 140MG/5ML LIQ

GAVISCON,FOAMICON, ALENIC ALKA LIQUID.CMOP DISP MULTIPLE OF 360'S

Strength: Units: Application Package: UOX

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 1 Dose Unit: TEASPOONFUL(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 2 Dose Unit: TEASPOONFUL(S) Package: IO

1 TABLESPOONFUL

Numeric Dose: 1 Dose Unit: TABLESPOONFUL(S) Package: IO

2 TABLESPOONFULS

Numeric Dose: 2 Dose Unit: TABLESPOONFUL(S) Package: IO

VA PRODUCT MATCH: AL OH 31.5MG/MG CARB 137.5/NA ALGINATE 136MG/5ML LIQUID

\(10966\) ALOH/MGOH/SIMTH REG STRENGTH CHEW TAB

Strength: Units: Application Package: UO

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: AL OH 200MG/MG OH 200MG/SIMETHICONE 20MG TAB,CHEWABLE

\(139\) ALPHA-1-PROTEINASE INHIBITOR,1000MG INJ \*N/F\*

Strength: 1000 Units: MG/VIAL Application Package: OUIX

Local Possible Dosages:

1000 MG/VIAL

Numeric Dose: 1000 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: ALPHA-1-PROTEINASE INHIBITOR,HUMAN 1000MG/VIL INJ

\(24118\) ALPROSTADIL 1000MCG URETHRAL SUPP

RESTRICTED TO ANDROLOGY/UROLOGY-LIMIT 6/MONTH

Strength: 1000 Units: MCG Application Package: OX

Local Possible Dosages:

1 SUPPOSITORY

Numeric Dose: 1 Dose Unit: SUPPOSITOR(IES) Package: IO

VA PRODUCT MATCH: ALPROSTADIL 1000MCG SUPP,URETHRAL

\(10968\) ALUMINUM HYDOXIDE GEL 320MG/5ML SUSP

Strength: 320 Units: MG/5ML Application Package: UOX

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 320 Dose Unit: MILLIGRAM(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 640 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: ALUMINUM HYDROXIDE 320MG/5ML SUSP

\(2756\) ALUMINUM W/MAGNESIA HYDROX GEL 180ML \*N/F\*

Strength: Units: Application Package: OX

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 1 Dose Unit: TEASPOONFUL(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 2 Dose Unit: TEASPOONFUL(S) Package: IO

1 TABLESPOONFUL

Numeric Dose: 1 Dose Unit: TABLESPOONFUL(S) Package: IO

2 TABLESPOONFULS

Numeric Dose: 2 Dose Unit: TABLESPOONFUL(S) Package: IO

VA PRODUCT MATCH: ALUMINUM HYDROXIDE 225MG/MAGNESIUM HYDROXIDE 200MG/5ML SUSP,ORAL

\(2529\) AMANTADINE 50MG/5ML SYRUP (ML)

Strength: 50 Units: MG/5ML Application Package: UOX

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 50 Dose Unit: MILLIGRAM(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 100 Dose Unit: MILLIGRAM(S) Package: IO

1 TABLESPOONFUL

Numeric Dose: 150 Dose Unit: MILLIGRAM(S) Package: IO

2 TABLESPOONFULS

Numeric Dose: 300 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: AMANTADINE HCL 50MG/5ML SYRUP

\(2277\) AMILORIDE HCL 5/HCTZ 50MG TAB \*N/F\*

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: AMILORIDE HCL 5MG/HYDROCHLOROTHIAZIDE 50MG TAB

\(5481\) AMINO ACID INJ 8.5% 500ML

Strength: Units: Application Package: UOIX

Local Possible Dosages:

42.5 GM (500ML)

Numeric Dose: 42.5 Dose Unit: GRAM(S) Package: IO

Local Possible Dosages:

500ML

Numeric Dose: 500 Dose Unit: MILLILITER(S) Package: IO

VA PRODUCT MATCH: FREAMINE 8.5% INJ

\(5127\) AMINOBENZOATE POTASSIUM 0.5GM CAP \*N/F\*

Strength: 0.5 Units: GM Application Package: OX

Local Possible Dosages:

1 CAPSULE

Numeric Dose: 0.5 Dose Unit: GRAM(S) Package: IO

2 CAPSULES

Numeric Dose: 1 Dose Unit: GRAM(S) Package: IO

VA PRODUCT MATCH: POTASSIUM PARA-AMINOBENZOATE 0.5GM CAP

\(23857\) AMINOCAPROIC ACID SYRUP 250MG/ML \*N/F\*

Strength: 250 Units: MG/ML Application Package: OUX

Local Possible Dosages:

2 ML

Numeric Dose: 500 Dose Unit: MILLIGRAM(S) Package: IO

1 ML

Numeric Dose: 250 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: AMINOCAPROIC ACID 250MG/ML SYRUP

\(5328\) AMINOHIPPURATE SODIUM 2GM/10ML INJ. \*N/F\*

Strength: Units: Application Package: UOX

Local Possible Dosages:

2GM(10ML)

Numeric Dose: 2 Dose Unit: GRAM(S) Package: IO

1GM(5ML)

Numeric Dose: 1 Dose Unit: GRAM(S) Package: IO

VA PRODUCT MATCH: AMINOHIPPURATE NA 20% INJ

\(424\) AMITRIPTYLINE 25/PERPHENAZINE 2MG TAB \*N/F\*

MAXIMUM 30 DAY SUPPLY

Strength: Units: Application Package: UOX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: AMITRIPTYLINE HCL 25MG/PERPHENAZINE 2MG TAB

\(426\) AMITRIPTYLINE 25/PERPHENAZINE 4MG TAB \*N/F\*

MAXIMUM 30 DAYS SUPPLY

Strength: Units: Application Package: UOX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: AMITRIPTYLINE HCL 25MG/PERPHENAZINE 4MG TAB

\(5662\) AMITRIPTYLLINE 50MG/PERPHEN. 4MG TAB \*N/F\*

Strength: Units: Application Package: UO

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: AMITRIPTYLINE HCL 50MG/PERPHENAZINE 4MG TAB

\(5263\) AMLODIPINE/ATORVASTATIN CA 2.5/10 MG TAB \*N/F\*

Strength: Units: Application Package: X

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: AMLODIPINE BESYLATE 2.5MG/ATORVASTATIN CA 10MG TAB

\(5262\) AMLODIPINE/ATORVASTATIN CA 5/10 MG TAB \*N/F\*

Strength: Units: Application Package: X

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: AMLODIPINE BESYLATE 5MG/ATORVASTATIN CA 10MG TAB

\(1640\) AMPICILLIN NA 1GM/VI INJ

Strength: 1 Units: GM/VIAL Application Package: UOIX

Local Possible Dosages:

1GM

Numeric Dose: 1 Dose Unit: GRAM(S) Package: O

VA PRODUCT MATCH: AMPICILLIN NA 1GM/VIL INJ

\(4404\) AMPICILLIN NA 2GM/VI INJ

Strength: 2 Units: GM/VIAL Application Package: IUOX

Local Possible Dosages:

2GM

Numeric Dose: 2 Dose Unit: GRAM(S) Package: O

VA PRODUCT MATCH: AMPICILLIN NA 2GM/VIL INJ

\(10970\) AMOX 250MG/CLAV K 62.5MG CHEW TAB \*N/F\*

Strength: Units: Application Package: U

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: AMOXICILLIN TRIHYDRATE 250MG/CLAVULANATE K 62.5MG TAB,CHEWABLE

\(6197\) AMOXICILLIN 250/CLAV K 125MG TAB

ANTIBIOTIC-MAXIMUM 30 DAY SUPPLY

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: AMOXICILLIN TRIHYDRATE 250MG/CLAVULANATE K 125MG TAB

\(8061\) AMOXICILLIN 250MG/5ML 150ML SUSP

THERAPEUTIC INTERCHANGE FOR AMPICILLIN-MAX 30 DAY SUPPLY

Strength: 250 Units: MG/5ML Application Package: UOX

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 250 Dose Unit: MILLIGRAM(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 500 Dose Unit: MILLIGRAM(S) Package: IO

1 TABLESPOONFUL

Numeric Dose: 750 Dose Unit: MILLIGRAM(S) Package: IO

2 TABLESPOONFULS

Numeric Dose: 1500 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: AMOXICILLIN 250MG/5ML SUSP,ORAL

\(5175\) AMOXICILLIN 400/CLAV K 57MG/5ML SUSP

CMOP Minimum Use Item - Local Fill

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 1 Dose Unit: TEASPOONFUL(S) Package: O

2 TEASPOONFULS

Numeric Dose: 2 Dose Unit: TEASPOONFUL(S) Package: O

5 ML

Numeric Dose: 5 Dose Unit: MILLILITER(S) Package: I

10 ML

Numeric Dose: 10 Dose Unit: MILLILITER(S) Package: I

VA PRODUCT MATCH: AMOXICILLIN 400MG/CLAVULANATE K 57MG/5ML SUSP

\(6198\) AMOXICILLIN 500/CLAV K 125MG TAB

ANTIBIOTIC-MAXIMUM 30 DAY SUPPLY

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: AMOXICILLIN TRIHYDRATE 500MG/CLAVULANATE K 125MG TAB

\(24028\) AMOXICILLIN 875/CLAV K 125MG TAB

ANTIBIOTIC-MAXIMUM 30DAYS SUPPLY

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: AMOXICILLIN TRIHYDRATE 875MG/CLAVULANATE K 125MG TAB

\(8279\) AMOXICILLIN/CLAVULANATE 250MG/5ML 150ML

FOR G-TUBE/DYSPHAGIA PATIENTS ONLY

Strength: Units: Application Package: XOU

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 1 Dose Unit: TEASPOONFUL(S) Package: IO

VA PRODUCT MATCH: AMOXICILLIN TRIHYDRATE 250MG/CLAVULANATE K 62.5MG/5ML SUSP

\(1513\) AMPICILLIN 250MG/5ML SUSP 100ML \*N/F\*

Strength: 250 Units: MG/5ML Application Package: UOX

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 250 Dose Unit: MILLIGRAM(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 500 Dose Unit: MILLIGRAM(S) Package: IO

1 TABLESPOONFUL

Numeric Dose: 750 Dose Unit: MILLIGRAM(S) Package: IO

2 TABLESPOONFULS

Numeric Dose: 1500 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: AMPICILLIN 250MG/5ML SUSP

\(1271\) AMPRENAVIR 15MG/ML SOLN ORAL \*N/F\*

Strength: 75 Units: MG/5ML Application Package: X

Local Possible Dosages:

75MG/5ML

Numeric Dose: 75 Dose Unit: GRAM(S) Package: O

300MG/20ML

Numeric Dose: 300 Dose Unit: GRAM(S) Package: O

600MG/40ML

Numeric Dose: 600 Dose Unit: GRAM(S) Package: O

VA PRODUCT MATCH: AMPRENAVIR 75MG/5ML SOLN,ORAL

\(233\) AMYL NITRITE 0.3ML INHALENT

Strength: Units: Application Package: UOX

Local Possible Dosages:

1 PUFF

Numeric Dose: 1 Dose Unit: INHALATION(S) Package: IO

2 PUFFS

Numeric Dose: 2 Dose Unit: INHALATION(S) Package: IO

1 INHALATION

Numeric Dose: 1 Dose Unit: INHALATION(S) Package: IO

2 INHALATIONS

Numeric Dose: 2 Dose Unit: INHALATION(S) Package: IO

1 SPRAY

Numeric Dose: 1 Dose Unit: SPRAY(S) Package: IO

2 SPRAYS

Numeric Dose: 2 Dose Unit: SPRAY(S) Package: IO

VA PRODUCT MATCH: AMYL NITRITE 0.3ML/AMP,INHL

\(6730\) APAP 325/BUTALBITAL 50/CAFF 40MG TAB

Strength: Units: Application Package: OXU

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: APAP 325MG/BUTALBITAL 50MG/CAFN 40MG TAB

\(7456\) APPLE CIDER VINEGAR CAP/TAB \*N/F\*

Strength: Units: Application Package: X

Local Possible Dosages:

1 CAP/TAB

Numeric Dose: 1 Dose Unit: CAP/TAB Package: IO

2 CAP/TABS

Numeric Dose: 2 Dose Unit: CAP/TAB Package: IO

VA PRODUCT MATCH: APPLE CIDER VINEGAR CAP/TAB

\(7478\) APRACLONIDINE HCL 0.5% OPH SOLN

ALL ORDERS RESTRICTED TO OPHTHALMOLOGY

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 DROP

Numeric Dose: 1 Dose Unit: DROP(S) Package: IO

2 DROPS

Numeric Dose: 2 Dose Unit: DROP(S) Package: IO

VA PRODUCT MATCH: APRACLONIDINE HCL 0.5% SOLN,OPH

\(7947\) ARFORMOTEROL 7.5MCG/ML SOLN INHL 2ML \*N/F\*

Strength: Units: Application Package: XO

Local Possible Dosages:

15 MCG (2 ML)

Numeric Dose: 15 Dose Unit: MICROGRAM(S) Package: IO

VA PRODUCT MATCH: ARFORMOTEROL TARTRATE 7.5MCG/ML SOLN,INHL,2ML

\(3694\) ARIPIPRAZOLE 1MG/ML LIQ 150ML \*N/F\*

Strength: 1 Units: MG/ML Application Package: UX

Local Possible Dosages:

1MG/1ML

Numeric Dose: 1 Dose Unit: MILLIGRAM(S) Package: O

2MG/2ML

Numeric Dose: 2 Dose Unit: MILLIGRAM(S) Package: O

VA PRODUCT MATCH: ARIPIPRAZOLE 1MG/ML SOLN,ORAL

\(4060\) ARTIFICIAL SALIVA

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 CUP (30 ML)

Numeric Dose: 30 Dose Unit: MILLILITER(S) Package: IO

2 CUPS (60 ML)

Numeric Dose: 2 Dose Unit: MILLILITER(S) Package: IO

VA PRODUCT MATCH: SALIVA,ARTIFICIAL

\(5648\) ARTIFICIAL SALIVA LOZENGE

ORDER BY EACH LOZENGE(90/BX)

Strength: Units: Application Package: XOU

Local Possible Dosages:

1 LOZENGE

Numeric Dose: 1 Dose Unit: LOZENGE(S) Package: IO

2 LOZENGES

Numeric Dose: 2 Dose Unit: LOZENGE(S) Package: IO

VA PRODUCT MATCH: SALIVA,ARTIFICIAL LOZENGE

\(5530\) ARTIFICIAL TEARS POLYVINYL ALCOHOL

FIRST DRUG OF CHOICE SUBSITUTITION PETMITTED ONLY IF DOCUMENTED ADR

Strength: Units: Application Package: UOX

Local Possible Dosages:

1 DROP

Numeric Dose: 1 Dose Unit: DROP(S) Package: IO

2 DROPS

Numeric Dose: 2 Dose Unit: DROP(S) Package: IO

VA PRODUCT MATCH: POLYVINYL ALCOHOL 1.4% SOLN,OPH

\(3721\) ARTIFICIAL TEARS POLYVINYL ALCOHOL (PF)

NOT TO BE USED UNLESS DOCUMENTED ADR TO ARTIFICIAL TEARS.

Strength: Units: Application Package: XOU

Local Possible Dosages:

1 DROP

Numeric Dose: 1 Dose Unit: DROP(S) Package: IO

2 DROPS

Numeric Dose: 2 Dose Unit: DROP(S) Package: IO

VA PRODUCT MATCH: POLYVINYL ALCOHOL 1% (PF) SOLN,OPH

\(3555\) ASA 325/BUTALBITAL 50/CAFF 40MG TAB

Strength: Units: Application Package: ONUX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: ASA 325MG/BUTALBITAL 50MG/CAFN 40MG TAB

\(2317\) ASA 770MG/CAFN 60MG/ORPHENADRINE 50MG \*N/F\*

Strength: Units: Application Package: OX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: ASA 770MG/CAFN 60MG/ORPHENADRINE CITRATE 50MG TAB

\(8380\) ASCORBIC ACID 500MG/5ML SYRUP \*N/F\*

Strength: 500 Units: MG/5ML Application Package: OUX

Local Possible Dosages:

1 TABLESPOONFUL

Numeric Dose: 1500 Dose Unit: MILLIGRAM(S) Package: IO

2 TABLESPOONFULS

Numeric Dose: 3000 Dose Unit: MILLIGRAM(S) Package: IO

1 TEASPOONFUL

Numeric Dose: 500 Dose Unit: MILLIGRAM(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 1000 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: ASCORBIC ACID 500MG/5ML SYRUP

\(5877\) ASPARAGINASE 10,000UNITS/10ML VIAL

CAUTION!!! CAN ONLY BE ORDER BY A HEM/ONC ATTENDING

Strength: 10000 Units: UNT/VIL Application Package: OUIX

Local Possible Dosages:

10000 UNITS/VIAL

Numeric Dose: 10000 Dose Unit: UNIT(S) Package: IO

20000 UNITS/2 VIALS

Numeric Dose: 20000 Dose Unit: UNIT(S) Package: IO

VA PRODUCT MATCH: ASPARAGINASE 10000UNT/VIL INJ

\(1860\) ASPIRIN 25MG/DIPYRIDAMOLE 200MG SA CAP

MUST USE PLAVIX/AGGRENOX CONSULT REQUEST.

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 CAPSULE

Numeric Dose: 1 Dose Unit: CAPSULE(S) Package: IO

VA PRODUCT MATCH: ASPIRIN 25MG/DIPYRIDAMOLE 200MG CAP,SA

\(1928\) ATENOLOL 100/CHLORTHALIDONE 25MG TAB

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: ATENOLOL 100MG/CHLORTHALIDONE 25MG TAB

\(1925\) ATENOLOL 50/CHLORTHALIDONE 25MG TAB

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 TABLET

Numeric Dose: 1 Dose Unit: TABLET(S) Package: IO

VA PRODUCT MATCH: ATENOLOL 50MG/CHLORTHALIDONE 25MG TAB

\(10802\) ATOVAQUONE 750MG/5ML SUSP (210ML)

ALL ORDERS RESTRICTED TO INFECTIOUS DISEASE SERVICE

Strength: 750 Units: MG/5ML Application Package: OUIX

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 750 Dose Unit: MILLIGRAM(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 1500 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: ATOVAQUONE 750MG/5ML SUSP,ORAL

\(767\) ATROPINE SULFATE 1% OPH SOLN

ALL ORDERS RESTRICTED TO OPHTHALMOLOGY

Strength: Units: Application Package: UOX

Local Possible Dosages:

1 DROP

Numeric Dose: 1 Dose Unit: DROP(S) Package: IO

2 DROPS

Numeric Dose: 2 Dose Unit: DROP(S) Package: IO

VA PRODUCT MATCH: ATROPINE SO4 1% SOLN,OPH

\(1201\) AZELASTINE 137MCG/SPRAY 200D NASAL INHL \*N/F\*

Strength: Units: Application Package: UOX

Local Possible Dosages:

1 SPRAY

Numeric Dose: 1 Dose Unit: SPRAY(S) Package: IO

2 SPRAYS

Numeric Dose: 2 Dose Unit: SPRAY(S) Package: IO

VA PRODUCT MATCH: AZELASTINE HCL 137MCG/SPRAY INHL,NASAL,30ML

\(268\) CARBIDOPA/LEVODOPA 12.5/50 TAB UD

PACKED FROM BULK(1/2 OF 25/100)

Strength: Units: Application Package: U

Local Possible Dosages:

12.5/50MG

Numeric Dose: 1 Dose Unit: TABLET(S) Package: I

VA PRODUCT MATCH: CARBIDOPA 25MG/LEVODOPA 100MG TAB

\(1231\) CARBIDOPA/LEVODOPA 25/100 CR TAB UD

Strength: Units: Application Package: U

Local Possible Dosages:

25/100MG

Numeric Dose: 1 Dose Unit: TABLET(S) Package: I

VA PRODUCT MATCH: CARBIDOPA 25MG/LEVODOPA 100MG TAB,SA

\(5720\) CARMUSTINE 7.7MG IMPLANT WAFER \*N/F\*

Strength: 7.7 Units: MG Application Package: U

Local Possible Dosages:

1 WAFER

Numeric Dose: 7.7 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: CARMUSTINE 7.7MG IMPLANT WAFER

\(684\) CHLORHEXIDINE 0.12% (PERIDEX) 473ML BT

RESTRICTED TO RX BY DENTIST (INPT & OUTPT) \*\*\* ORDER BY ML

Strength: Units: Application Package: UOX

Local Possible Dosages:

WITH ONE CAPFUL

Numeric Dose: 15 Dose Unit: MILLILITER(S) Package: O

ONE CAPFUL

Numeric Dose: 15 Dose Unit: MILLILITER(S) Package: I

VA PRODUCT MATCH: CHLORHEXIDINE GLUCONATE 0.12% RINSE,ORAL

\(5122\) CHOLESTYRAMINE 4GM/5GM LIGHT POWDER

ORDER BY THE GM(210GM/42 DOSES/CAN)\*\*\*FILLED AT CMOP ONLY

Strength: 4 Units: GM/5GM Application Package: OX

Local Possible Dosages:

1 SCOOPFUL(4GM)

Numeric Dose: 4 Dose Unit: GRAM(S) Package: O

2 SCOOPFULS(8GM)

Numeric Dose: 8 Dose Unit: GRAM(S) Package: O

3 SCOOPFULS(12GM)

Numeric Dose: 12 Dose Unit: GRAM(S) Package: O

VA PRODUCT MATCH: CHOLESTYRAMINE 4GM/5GM (LIGHT) PWDR

\(4933\) CHOLESTYRAMINE 4GM/9GM ORAL PWD PKT

Strength: Units: Application Package: OX

Local Possible Dosages:

1 PACKET

Numeric Dose: 1 Dose Unit: PACKET(S) Package: IO

2 PACKETS

Numeric Dose: 2 Dose Unit: PACKET(S) Package: IO

VA PRODUCT MATCH: CHOLESTYRAMINE 4GM/9GM PWDR,PKT

\(5728\) CHONDROITIN 40MG/HYALURONATE 30MG/ML OPH

OR ONLY

Strength: Units: Application Package: U

Local Possible Dosages:

0.5 ML

Numeric Dose: 0.5 Dose Unit: MILLILITER(S) Package: I

VA PRODUCT MATCH: CHONDROITIN NA 40MG/HYALURONATE NA 30MG/ML INJ,OPH,SYRINGE,0.5ML

\(7714\) CILASTATIN NA 250MG/IMIPENEM 250MG INJ

Strength: Units: Application Package: U

Local Possible Dosages:

250MG

Numeric Dose: 1 Dose Unit: VIAL(S) Package: I

VA PRODUCT MATCH: CILASTATIN NA 250MG/IMIPENEM 250MG/VIL INJ IV

\(1857\) CILASTATIN NA 500MG/IMIPENEM 500MG INJ

Strength: Units: Application Package: UI

Local Possible Dosages:

500MG

Numeric Dose: 1 Dose Unit: VIAL(S) Package: I

VA PRODUCT MATCH: CILASTATIN NA 500MG/IMIPENEM 500MG/VIL INJ IV

\(1549\) CLINDAMYCIN 600MG/4ML INJ

Strength: 150 Units: MG/ML Application Package: UOIX

Local Possible Dosages:

450MG

Numeric Dose: 450 Dose Unit: MILLIGRAM(S) Package: O

600MG

Numeric Dose: 600 Dose Unit: MILLIGRAM(S) Package: O

VA PRODUCT MATCH: CLINDAMYCIN PO4 150MG/ML INJ

\(784\) CLOTRIMAZOLE 10MG TROCHE

Strength: 10 Units: MG Application Package: UOX

Local Possible Dosages:

1 TROCHE

Numeric Dose: 10 Dose Unit: MILLIGRAM(S) Package: IO

2 TROCHES

Numeric Dose: 20 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: CLOTRIMAZOLE 10MG TROCHE

\(1073\) DEXTROSE 10% INJ IN 0.45%NaCl 1000ML

Strength: Units: Application Package: OIX

Local Possible Dosages:

1000ML

Numeric Dose: 1000 Dose Unit: MILLILITER(S) Package: IO

VA PRODUCT MATCH: DEXTROSE 10%/NACL 0.45% INJ

\(3684\) DEXTROSE 15GM/37.5GM SQUEEZE TUBE

Strength: 15 Units: GM Application Package: OUX

Local Possible Dosages:

CONTENTS OF TUBE

Numeric Dose: 15 Dose Unit: GRAM(S) Package: IO

VA PRODUCT MATCH: DEXTROSE 15GM/37.5GM SQUEEZE TUBE

\(3586\) DIPHTHERIA/TETANUS TOXOID ADSORBED INJ

Strength: Units: Application Package: OUX

Local Possible Dosages:

0.5 ML

Numeric Dose: 0.5 Dose Unit: MILLILITER(S) Package: IO

VA PRODUCT MATCH: DIPHTHERIA TOXOID/TETANUS TOXOID ADSORBED INJ

\(5650\) DOPAMINE 400MG/D5W 250ML INJ

Strength: 1.6 Units: MG/ML Application Package: I

Local Possible Dosages:

2.5 MCG/KG/MIN

Numeric Dose: \<LEAVE BLANK\> Dose Unit: \<LEAVE BLANK\> Package: I

5 MCG/KG/MIN

Numeric Dose: \<LEAVE BLANK\> Dose Unit: \<LEAVE BLANK\> Package: I

VA PRODUCT MATCH: DOPAMINE HCL 1.6MG/ML/DEXTROSE 5% INJ

\(3033\) EPI-PEN 0.3MG/0.3ML INJECTOR

Strength: 0.3 Units: MG/0.3ML Application Package: OUX

Local Possible Dosages:

0.3 ML

Numeric Dose: 0.3 Dose Unit: MILLILITER(S) Package: O

VA PRODUCT MATCH: EPINEPHRINE (EPI-PEN) 0.3MG/0.3ML INJECTOR

\(4489\) EPOETIN ALFA,RECOMB 10,000 UNT/ML INJ

This is the 1ml single dose vial

Strength: 10000 Units: UNT/ML Application Package: OUX

Local Possible Dosages:

10,000 UNITS

Numeric Dose: 10000 Dose Unit: UNIT(S) Package: O

VA PRODUCT MATCH: EPOETIN ALFA,RECOMBINANT 10000UNT/ML INJ

\(7955\) ESTRADIOL ACETATE 0.05MG/24HR VAG RING \*N/F\*

Strength: Units: Application Package: OX

Local Possible Dosages:

1 RING

Numeric Dose: 1 Dose Unit: VAGINAL RING Package: IO

VA PRODUCT MATCH: ESTRADIOL ACETATE 0.05MG/24HR RING,VAG

\(3767\) FENTANYL 100MCG/H (10MG) TRANSDERM PATCH

With 28 DAY FILL PREFERRED-OPIOID CONSULT REQUIRED

Strength: Units: Application Package: OUCNX

Local Possible Dosages:

1 PATCH

Numeric Dose: 1 Dose Unit: PATCH(ES) Package: O

100MCG/HR

Numeric Dose: 1 Dose Unit: PATCH(ES) Package: I

2 PATCHES

Numeric Dose: 2 Dose Unit: PATCH(ES) Package: O

200MCG/HR

Numeric Dose: 2 Dose Unit: PATCH(ES) Package: I

300MCG/HR

Numeric Dose: 3 Dose Unit: PATCH(ES) Package: I

3 PATCHES

Numeric Dose: 3 Dose Unit: PATCH(ES) Package: O

400MCG/HR

Numeric Dose: 4 Dose Unit: PATCH(ES) Package: I

4 PATCHES

Numeric Dose: 4 Dose Unit: PATCH(ES) Package: O

VA PRODUCT MATCH: FENTANYL 100MCG/HR PATCH

\(547\) FLUORESCEIN NA 25% INJ \*N/F\*

Strength: Units: Application Package:

Local Possible Dosages:

1 ML

Numeric Dose: 250 Dose Unit: MILLIGRAM(S) Package: IO

2 MLS

Numeric Dose: 500 Dose Unit: MILLIGRAM(S) Package: IO

1 MG

Numeric Dose: 1 Dose Unit: MILLIGRAM(S) Package: IO

2 MGS

Numeric Dose: 2 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: FLUORESCEIN NA 25% INJ

\(2855\) FLUPHENAZINE CONC 1MG UD

Strength: 1 Units: MG/ML Application Package: U

Local Possible Dosages:

1 TEASPOONFUL

Numeric Dose: 5 Dose Unit: MILLIGRAM(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 10 Dose Unit: MILLIGRAM(S) Package: IO

1 TABLESPOONFUL

Numeric Dose: 15 Dose Unit: MILLIGRAM(S) Package: IO

2 TABLESPOONFULS

Numeric Dose: 30 Dose Unit: MILLIGRAM(S) Package: IO

> **NOTE:** Strength of 1 does not match NDF strength of 5.

VA PRODUCT MATCH: FLUPHENAZINE HCL 5MG/ML LIQUID,ORAL

\(4408\) FOSPHENYTOIN 500MG-PE/10ML INJ

Strength: Units: Application Package: I

Local Possible Dosages:

500MG-PE (10ML)

Numeric Dose: 500 Dose Unit: MG-PE Package: IO

250MG-PE (5ML)

Numeric Dose: 250 Dose Unit: MG-PE Package: IO

100MG-PE (20ML)

Numeric Dose: 100 Dose Unit: MG-PE Package: IO

\(3847\) GLUCOSE 24GM ORAL LIQUID \*N/F\*

For glucose tolerance testing ONLY.

Strength: 24 Units: GM Application Package: UOX

Local Possible Dosages:

1 BOTTLE (24 GRAM)

Numeric Dose: 24 Dose Unit: GRAM(S) Package: IO

2 BOTTLES (48 GRAM)

Numeric Dose: 48 Dose Unit: GRAM(S) Package: IO

VA PRODUCT MATCH: GLUCOSE 24GM LIQUID,ORAL

\(11116\) GOSERELIN 10.8MG-90 DAY INJ

RESTRICTED TO UROLOGY AND ONCOLOGY

Strength: 10.8 Units: MG Application Package: OUX

Local Possible Dosages:

1 INJECTION

Numeric Dose: 10.8 Dose Unit: MILLIGRAM(S) Package: IO

2 INJECTIONS

Numeric Dose: 21.6 Dose Unit: MILLIGRAM(S) Package: IO

1 IMPLANT

Numeric Dose: 10.8 Dose Unit: MILLIGRAM(S) Package: IO

2 IMPLANTS

Numeric Dose: 21.6 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: GOSERELIN ACETATE 10.8MG INJ,IMPLANT

\(154\) HEPARIN 1,000 UNIT/ML 10ML INJ

Strength: 1000 Units: UNT/ML Application Package: OIX

Local Possible Dosages:

1000UNITS/ML

Numeric Dose: 1000 Dose Unit: UNIT(S) Package: IO

2000UNITS/2ML

Numeric Dose: 2000 Dose Unit: UNIT(S) Package: IO

3000UNITS/3ML

Numeric Dose: 3000 Dose Unit: UNIT(S) Package: IO

4000UNITS/4ML

Numeric Dose: 4000 Dose Unit: UNIT(S) Package: IO

5000UNITS/5ML

Numeric Dose: 5000 Dose Unit: UNIT(S) Package: IO

6000UNITS/6ML

Numeric Dose: 6000 Dose Unit: UNIT(S) Package: IO

7000UNITS/7ML

Numeric Dose: 7000 Dose Unit: UNIT(S) Package: IO

8000UNITS/8ML

Numeric Dose: 8000 Dose Unit: UNIT(S) Package: IO

9000UNITS/9ML

Numeric Dose: 9000 Dose Unit: UNIT(S) Package: IO

10000UNITS/10ML

Numeric Dose: 10000 Dose Unit: UNIT(S) Package: IO

VA PRODUCT MATCH: HEPARIN NA 1000UNT/ML INJ

\(3608\) HEPATITIS B IMMUNE GLOBULIN (IM) INJ

For IM Use Only

Strength: Units: Application Package: OUXI

Local Possible Dosages:

1ML

Numeric Dose: 1 Dose Unit: MILLILITER(S) Package: IO

2ML

Numeric Dose: 2 Dose Unit: MILLILITER(S) Package: IO

3ML

Numeric Dose: 3 Dose Unit: MILLILITER(S) Package: IO

4ML

Numeric Dose: 4 Dose Unit: MILLILITER(S) Package: IO

5ML

Numeric Dose: 5 Dose Unit: MILLILITER(S) Package: IO

VA PRODUCT MATCH: HEPATITIS B IMMUNE GLOBULIN (IM) INJ

\(4497\) HYDROCORTISONE 100MG/60ML ENEMA

Strength: 100 Units: MG/60ML Application Package: UOX

Local Possible Dosages:

1 ENEMA (100MG/60ML)

Numeric Dose: 100 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: HYDROCORTISONE 100MG/60ML ENEMA

\(5462\) HYDROMORPHONE HCL 3MG RTL SUPP \*N/F\*

Requires written RX with DEA/VA# before RX can be dispensed

Strength: 3 Units: MG Application Package: OUNX

Local Possible Dosages:

1 SUPPOSITORY

Numeric Dose: 3 Dose Unit: MILLIGRAM(S) Package: O

2 SUPPOSITORIES

Numeric Dose: 6 Dose Unit: MILLIGRAM(S) Package: O

VA PRODUCT MATCH: HYDROMORPHONE HCL 3MG SUPP,RTL

\(4011\) INTEFERON ALFA-2b 18 MILLION UNT/VIL INJ

RESTRICTED VA NATIONAL FORMULARY ITEM - JUSTIFICATION REQUIRED

Strength: 18 Units: MILLION UNT/VIL Application Package: OX

Local Possible Dosages:

18 MILLION UNITS

Numeric Dose: 18 Dose Unit: MILLIONUNIT(S) Package: O

VA PRODUCT MATCH: INTERFERON ALFA-2B,RECOMBINANT 18 MILLION UNT/VIL INJ

\(2080\) LACRISERT 5MG INSERT N/F \*N/F\*

ORDER BY EACH INSERT(60/BX)

Strength: 5 Units: MG/UNT Application Package: OUX

Local Possible Dosages:

1 INSERT

Numeric Dose: 1 Dose Unit: INSERT(S) Package: IO

VA PRODUCT MATCH: HYDROXYPROPYL CELLULOSE 5MG/UNT INSERT,CONT REL,OPH

\(1747\) LACTULOSE 10GM/15ML SYRUP

Strength: 10 Units: GM/15ML Application Package: UOX

Local Possible Dosages:

1 TABLESPOONFUL

Numeric Dose: 10 Dose Unit: GRAM(S) Package: IO

2 TABLESPOONFULS

Numeric Dose: 20 Dose Unit: GRAM(S) Package: IO

VA PRODUCT MATCH: LACTULOSE 10GM/15ML SYRUP

\(2884\) LACTULOSE SYRUP 20GM/30ML UD

\*\*\*USE IN OUTPATIENT FOR PASSES ONLY\*\*\*

Strength: 20 Units: GM/15ML Application Package: UOX

Local Possible Dosages:

1 CUPFUL(20GMS)

Numeric Dose: 20 Dose Unit: GRAM(S) Package: O

> **NOTE:** Strength of 20 does not match NDF strength of 10.

VA PRODUCT MATCH: LACTULOSE 10GM/15ML SYRUP

\(4526\) LEVALBUTEROL HCL 0.63MG/3ML SOLN,INHL \*N/F\*

ORDER IN INCREMENTS OF 24'S(24/BX)ALBUTEROL IS 1ST LINE

Strength: 0.63 Units: MG/ML Application Package: OXU

Local Possible Dosages:

1 VIAL(0.63MG/3ML)

Numeric Dose: 0.63 Dose Unit: MILLIGRAM(S) Package: O

0.63MG/3ML

Numeric Dose: 3 Dose Unit: MILLILITER(S) Package: I

> **NOTE:** Strength of 0.63 does not match NDF strength of 0.21.

VA PRODUCT MATCH: LEVALBUTEROL HCL 0.21MG/ML SOLN,INHL,3ML

\(2886\) LITHIUM CITRATE 150MG/2.5ML UD

Strength: 4 Units: MEQ/5ML Application Package: U

Local Possible Dosages:

4MEQ(150MG/2.5ML)

Numeric Dose: 150 Dose Unit: MILLIGRAM(S) Package: I

> **NOTE:** Strength of 4 does not match NDF strength of 8.

VA PRODUCT MATCH: LITHIUM CITRATE 8MEQ/5ML SYRUP

\(2885\) LITHIUM CITRATE 600MG/10ML UD

TO BE USED IN OUTPATIENT FOR PASSES ONLY!

Strength: 8 Units: MEQ/5ML Application Package: UO

Local Possible Dosages:

1 CUP(600MG)

Numeric Dose: 600 Dose Unit: MILLIGRAM(S) Package: O

16MEQ(600MG/10ML)

Numeric Dose: 600 Dose Unit: MILLIGRAM(S) Package: I

VA PRODUCT MATCH: LITHIUM CITRATE 8MEQ/5ML SYRUP

\(855\) MAGNESIUM CITRATE LIQUID

CMOP DISPENSES AS BOTTLES

Strength: Units: Application Package: UOX

Local Possible Dosages:

ONE BOTTLE (300CC)

Numeric Dose: 300 Dose Unit: MILLILITER(S) Package: IO

ONE-HALF BOTTLE (150CC)

Numeric Dose: 150 Dose Unit: MILLILITER(S) Package: IO

VA PRODUCT MATCH: MAGNESIUM CITRATE LIQUID,ORAL

\(3607\) MESALAMINE 4GM/60ML ENEMA \*N/F\*

ORDER BY EACH BOTTLE

Strength: 4 Units: GM/60ML Application Package: OUX

Local Possible Dosages:

1 BOTTLE(60ML)

Numeric Dose: 4 Dose Unit: GRAM(S) Package: IO

VA PRODUCT MATCH: MESALAMINE 4GM/60ML SUSP,RTL

\(4238\) METHADONE 10MG/ML CONC.(DILUTED BY RPH)

RESTRICTED TO PSYCH..DISPENSE FROM VAULT WEEKDAYS 8AM TO 4:30PM

Strength: Units: Application Package: ONUX

Local Possible Dosages:

ONE 10MG BOTTLE

Numeric Dose: 10 Dose Unit: MILLIGRAM(S) Package: IO

ONE 15MG BOTTLE

Numeric Dose: 15 Dose Unit: MILLIGRAM(S) Package: IO

ONE 20MG BOTTLE

Numeric Dose: 20 Dose Unit: MILLIGRAM(S) Package: IO

ONE 5MG BOTTLE

Numeric Dose: 5 Dose Unit: MILLIGRAM(S) Package: IO

ONE 25MG BOTTLE

Numeric Dose: 25 Dose Unit: MILLIGRAM(S) Package: IO

ONE 30MG BOTTLE

Numeric Dose: 30 Dose Unit: MILLIGRAM(S) Package: IO

ONE 35MG BOTTLE

Numeric Dose: 35 Dose Unit: MILLIGRAM(S) Package: IO

ONE 40MG BOTTLE

Numeric Dose: 40 Dose Unit: MILLIGRAM(S) Package: IO

ONE 45MG BOTTLE

Numeric Dose: 45 Dose Unit: MILLIGRAM(S) Package: IO

ONE 50MG BOTTLE

Numeric Dose: 50 Dose Unit: MILLIGRAM(S) Package: IO

ONE 55MG BOTTLE

Numeric Dose: 55 Dose Unit: MILLIGRAM(S) Package: IO

ONE 60MG BOTTLE

Numeric Dose: 60 Dose Unit: MILLIGRAM(S) Package: IO

ONE 65MG BOTTLE

Numeric Dose: 65 Dose Unit: MILLIGRAM(S) Package: IO

ONE 70MG BOTTLE

Numeric Dose: 70 Dose Unit: MILLIGRAM(S) Package: IO

ONE 75MG BOTTLE

Numeric Dose: 75 Dose Unit: MILLIGRAM(S) Package: IO

ONE 80MG BOTTLE

Numeric Dose: 80 Dose Unit: MILLIGRAM(S) Package: IO

ONE 85MG BOTTLE

Numeric Dose: 85 Dose Unit: MILLIGRAM(S) Package: IO

ONE 90MG BOTTLE

Numeric Dose: 90 Dose Unit: MILLIGRAM(S) Package: IO

ONE 95MG BOTTLE

Numeric Dose: 95 Dose Unit: MILLIGRAM(S) Package: IO

ONE (100MG) BOTTLE

Numeric Dose: 100 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: METHADONE HCL 10MG/ML SOLN,ORAL

\(1598\) METHYLENE BLUE 1% 10ML S.S.

Strength: Units: Application Package: X

Local Possible Dosages:

1 AMPULE

Numeric Dose: 100 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: METHYLENE BLUE 1% INJ

\(7452\) NEUTRA-PHOS POTASSIUM (SF)1.45GM/PKT

MIX CT'NS OF 1 PK'T WITH 2.5 OZ. WATER OR JUICE. STIR WELL&TAKE ASAP

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 PACKET

Numeric Dose: 1 Dose Unit: PACKET(S) Package: IO

2 PACKETS

Numeric Dose: 2 Dose Unit: PACKET(S) Package: IO

VA PRODUCT MATCH: PHOSPHORUS 250MG/POTASSIUM 14.25MEQ/PKT PWDR

\(23706\) NICOTINE 14MG/24HR PATCH

Strength: 14 Units: MG/24HRS Application Package: OUX

Local Possible Dosages:

1 PATCH

Numeric Dose: 1 Dose Unit: PATCH(ES) Package: IO

VA PRODUCT MATCH: NICOTINE 14MG/24HRS PATCH

\(11027\) NICOTINE 21MG/24HR PATCH

Strength: 21 Units: MG/24HRS Application Package: OUX

Local Possible Dosages:

1 PATCH

Numeric Dose: 1 Dose Unit: PATCH(ES) Package: IO

VA PRODUCT MATCH: NICOTINE 21MG/24HRS PATCH

\(24301\) NICOTINE 2MG GUM

Strength: 2 Units: MG Application Package: OU

Local Possible Dosages:

1 PIECE

Numeric Dose: 2 Dose Unit: MILLIGRAM(S) Package: IO

2 PIECES

Numeric Dose: 4 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: NICOTINE POLACRILEX 2MG TAB,CHEWG GUM

\(5350\) NICOTINE 4MG GUM,CHEWABLE N/F \*N/F\*

ORDER BY EACH PIECE(110/BX)\*\*\*FILLED FROM CMOP\*\*\*

Strength: 4 Units: MG Application Package: OX

Local Possible Dosages:

1 PIECE

Numeric Dose: 1 Dose Unit: PIECE(S) Package: O

VA PRODUCT MATCH: NICOTINE POLACRILEX 4MG TAB,CHEWG GUM

\(5369\) NICOTINE POLACRILEX 2MG LOZENGE \*N/F\*

ORDER BY EACH LOZENGE(72/BX)

Strength: 2 Units: MG Application Package: XO

Local Possible Dosages:

1 LOZENGE

Numeric Dose: 2 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: NICOTINE POLACRILEX 2MG LOZENGE

\(5370\) NICOTINE POLACRILEX 4MG LOZENGE \*N/F\*

ORDER BY EACH LOZENGE(72/BX)

Strength: 4 Units: MG Application Package: XO

Local Possible Dosages:

1 LOZENGE

Numeric Dose: 4 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: NICOTINE POLACRILEX 4MG LOZENGE

\(2473\) NITROGLYCERIN 0.1MG/HR (2.5MG/D) PATCH

Strength: Units: Application Package: UOX

Local Possible Dosages:

1 PATCH

Numeric Dose: 1 Dose Unit: PATCH(ES) Package: O

1 PATCH(0.1MG/HR)

Numeric Dose: 1 Dose Unit: PATCH(ES) Package: I

VA PRODUCT MATCH: NITROGLYCERIN 0.1MG/HR PATCH

\(250\) NITROGLYCERIN OINTMENT 2% (60GM)

ORDER BY GM (60GM = 1 TUBE)

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 INCH

Numeric Dose: 1 Dose Unit: INCH(ES) Package: IO

1/2 INCH

Numeric Dose: 0.5 Dose Unit: INCH(ES) Package: IO

VA PRODUCT MATCH: NITROGLYCERIN 2% OINT,TOP

\(4978\) NITROGLYCERIN 0.4MG 200D ORAL SPRAY \*N/F\*

Strength: 0.4 Units: MG/SPRAY Application Package: OUX

Local Possible Dosages:

1 SPRAY

Numeric Dose: 0.4 Dose Unit: MILLIGRAM(S) Package: IO

VA PRODUCT MATCH: NITROGLYCERIN 0.4MG/SPRAY AEROSOL

\(5978\) PILOCARPINE HCL 3% OPH SOLN

Strength: Units: Application Package: UOX

Local Possible Dosages:

1 DROP

Numeric Dose: 1 Dose Unit: DROP(S) Package: IO

2 DROPS

Numeric Dose: 2 Dose Unit: DROP(S) Package: IO

VA PRODUCT MATCH: PILOCARPINE HCL 3% SOLN,OPH

\(4003\) POLIOVIRUS VACCINE INACTIVATED INJ

Strength: Units: Application Package: OUX

Local Possible Dosages:

0.5ML

Numeric Dose: 0.5 Dose Unit: MILLILITER(S) Package: IO

VA PRODUCT MATCH: POLIOVIRUS VACCINE INACTIVATED (IPOL)

\(5469\) POLYETHYLENE GLYCOL 17GM PWD PACKETS

MIX 1 PACKET IN 8oz OF WATER OR JUICE

Strength: Units: Application Package: U

Local Possible Dosages:

1 PACKET(17GM)

Numeric Dose: 17 Dose Unit: GRAM(S) Package: IO

VA PRODUCT MATCH: POLYETHYLENE GLYCOL 3350 17GM/PKT PWDR,ORAL

\(5061\) POLYETHYLENE GLYCOL 3350 ORAL PWD

ORDER BY THE GM(510GM/BT)

Strength: Units: Application Package: XO

Local Possible Dosages:

1 CAPFUL(17GM)

Numeric Dose: 17 Dose Unit: GRAM(S) Package: IO

VA PRODUCT MATCH: POLYETHYLENE GLYCOL 3350 PWDR,ORAL

\(4770\) SALMETEROL 50MCG/BLSTR PO INHL DISKUS 60

Strength: Units: Application Package: OUX

Local Possible Dosages:

1 PUFF

Numeric Dose: 1 Dose Unit: INHALATION(S) Package: IO

VA PRODUCT MATCH: SALMETEROL XINAFOATE 50MCG/BLISTER INHL,ORAL,DISKUS,60

\(606\) SODIUM POLYSTYRENE SULF 15GM/60ML SUSP

Strength: 15 Units: GM/60ML Application Package: UOX

Local Possible Dosages:

1 TABLESPOONFUL

Numeric Dose: 1 Dose Unit: TABLESPOONFUL(S) Package: O

2 TABLESPOONFULS

Numeric Dose: 2 Dose Unit: TABLESPOONFUL(S) Package: O

1 TEASPOONFUL

Numeric Dose: 5 Dose Unit: MILLILITER(S) Package: IO

2 TEASPOONFULS

Numeric Dose: 10 Dose Unit: MILLILITER(S) Package: IO

VA PRODUCT MATCH: SODIUM POLYSTYRENE SULFONATE 15GM/60ML SUSP