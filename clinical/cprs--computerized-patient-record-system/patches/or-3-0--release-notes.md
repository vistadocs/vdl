---
title: OR*3*0*626 (MOCHA 3.0 Combined Build Enhancement) Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*0
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - order
  - check
  - table
  - pharmacogenomic
  - contents
  - drug
  - interaction
  - checks
  - phenotype
  - pharmacy
page_count: 0
word_count: 2976
section_count: 12
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_626_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_626_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

![](or-3-0-626-mocha-3-0-combined-build-enhancement-release-notes/001.png)

Medication order check HEalthcare application (mocha) v3.0

Release Notes

PSJ\*5\*447, PSO\*7\*737, and OR\*3\*626  
(MOCHA 3.0 PGX Combined Build 1.0)

PSS\*1\*262 and PSN\*4\*576 (Stand Alone)

August 2025

Product Development

*(This page included for two-sided copying.)*
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Enhancements](#enhancements)
- [Menu Changes](#menu-changes)
  - [New Options](#new-options)
  - [Changed Options](#changed-options)
  - [Deleted Options](#deleted-options)
  - [Menu Changes](#menu-changes-1)
- [File Changes](#file-changes)
  - [New Files](#new-files)
  - [New Fields](#new-fields)
  - [Modified Fields](#modified-fields)
- [Other Changes](#other-changes)
  - [Intervention Type additions](#intervention-type-additions)
  - [Order Check additions](#order-check-additions)
  - [Web Server addition](#web-server-addition)
  - [Web Service addition](#web-service-addition)
- [# Known Anomalies](#known-anomalies)
The goal of the Medication Order Check Healthcare Application (MOCHA) project is to provide the best medication decision support system in health care. The first phase, MOCHA v1.0, implemented enhanced order checking functionality utilizing the First Databank (FDB) MedKnowledge Framework Application Program Interfaces (APIs) and database for Drug Interaction and Duplicate Therapy order checks. MOCHA v2.0 implemented the Maximum Single Dose Order Check for simple and complex medication orders. Mocha 2.1 implemented the Maximum Daily Dose Order Check for simple medication orders. Mocha 3.0 implements Pharmacogenomic (PGx) order checking, providing guidance for appropriate drug therapy and helping ensure the most effective treatments possible.
This release notes document provides a brief description of the new features and functions of the MOCHA v3.0 patches listed in the table below. More detailed information on the functionality can be found in the application user and technical manuals located on the VA Software Document Library (VDL).
| Application                                | Patch       |
|--------------------------------------------|-------------|
| Outpatient Pharmacy                        | PSO\*7\*737 |
| Inpatient Medications                      | PSJ\*5\*447 |
| Pharmacy Data Management (PDM)             | PSS\*1\*262 |
| Computerized Patient Records System (CPRS) | OR\*3\*626  |
| National Drug File                         | PSN\*4\*576 |

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA v3.0 will provide the following enhancements:

- Implement PGx order checks, high and medium severity, for PGx eligible medication orders entered in Outpatient Pharmacy, Inpatient Medications, and Computerized Patient Record System (CPRS) applications.
- Make ‘Additional Information’ (like a monograph) available to CPRS and Pharmacy users for all high and medium severity PGx order checks.
- Retrieve patient genomic lab data from the Health Data Repository (HDR) to be used for the PGx order checks.
- Provide a ‘Screen’ message to CPRS/Pharmacy users that when appropriate will suggest that additional information or testing needs to be provided for the drug being entered to do a PGx order check.
- Apply suppression rules to the PGx Order checks to ensure a PGx order check is displayed only when necessary.
- Provide error/exception messages when a PGx order check cannot be performed for whatever reason.
- Create a new Pharmacy option called Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] that allows a user to enter drug(s), gene(s), phenotype(s), and genotype(s) and see the PGx Order checks returned from the vendor for the data entered. The option can also be run by patient, where the patient’s genomic lab results and PGx eligible drug(s) from his/her current profile are used to retrieve PGx order checks.
- Require a CPRS override reason for PGx order checks with a high severity.
- Require a Pharmacy intervention for PGx order checks with a high severity.
- Store PGx order check information in the ORDER CHECK INSTANCES (#100.05) File for PGx order checks seen in CPRS.
- Store PGx order check information in the CANCELLED ORDERS AND ORDER CHECKS (#100.3) File when a CPRS user exits during the entry of a new order without completing the order.
- Restructure some of the Pharmacy Data Management menus to group like options together for a more logical display.
- Send an Email to a Pharmacy Benefits Management (PBM) mail group when genomic data is retrieved from the HDR for a PGx order check and the gene or phenotype cannot be resolved to an acceptable term that the vendor is expecting. PBM will investigate accordingly.
- Create two new entries in the CPRS ORDER CHECKS (#100.8) File: PHARMACOGENOMICS HIGH and PHARMACOGENOMICS MODERATE.
- Create two new entries in the APSP INTERVENTION TYPE (9009032.2) File: PHARMACOGENOMIC HIGH ORDER CHECK and PHARMACOGENOMIC MEDIUM ORDER CHECK.
- Add two new PGx fields to the VA PRODUCT (#50.68) File. The PGX ELIGIBLE (#46) Field is used to identity VA Products that are PGx eligible, meaning that when a medication order is placed for a drug matched to a VA Product with the PGX ELIGIBLE (#46) Field set to Yes, then a PGx order check will be performed on that medication order. The other field, PGX SUPPRESSED (#47), is currently not in use.
- Add two new fields to the DRUG INGREDIENT (#50.416) File. The PGX ELIGIBLE (#5) Field and the PGX SUPPRESSED (#6) Field will be used in the suppression logic that determines if a medium PGx order check should be suppressed.
- Add the VA PHARMACOGENOMICS URL (#103) Field to the PHARMACY SYSTEM (#59.7) File. This field will be used for the Uniform Resource Locator (URL) link in the PGx order check text when the HDR is unreachable, which is where the URL is normally retrieved from.
- Create the new PHARMACOGENOMIC GENES (#51.26) File. This file will be used to resolve genes received from the HDR to the correct vendor version name of that gene so the PGx order check is successfully performed. This file will also be used as a gene lookup in the new Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option.
- Created the new PHARMACOGENOMIC PHENOTYPES (#51.28) File. This file will be used to resolve phenotypes received from the HDR to the correct vendor version name of that phenotype so the PGx order check is successfully performed. This file will also be used as a phenotype lookup in the new Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option.
- Create the PHARMCOGENOMIC EMAIL LOG (#51.29) File. This file is used to track genes and phenotypes received from the HDR that cannot be found in the PHARMACOGENOMIC GENES (#51.26) File and the PHARMACOGENOMIC PHENOTYPES (#51.28) File. PBM will correct the unresolved genes and phenotypes accordingly.

# Menu Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new option has been added to Pharmacy Data Management:

- The new Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option allows a user to test combinations of prospective drug(s), gene(s), phenotype(s), and genotype(s), to see the PGx Order checks returned from the vendor. The user will be prompted for drug(s), gene(s), phenotype(s), and genotype(s), and that data will be sent to the vendor as a medication order, and the resulting PGx order checks will be displayed to the user. The option can also be run by patient, where the patient’s genomic lab results and PGx eligible drug(s) from his/her current profile are used to retrieve PGx order checks.

## Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options have been changed:

- The Lookup into Dispense Drug File \[PSS LOOK\] option has been enhanced to display the PGX ELIGIBLE (#46) Field and PGX SUPPRESSED (#47) Field from the VA PRODUCT (#50.68) File for DRUG (#50) File entries matched to the National Drug File.
- The Inquire to National Files \[PSNACT\] option has been enhanced to display the PGX ELIGIBLE (#46) Field and PGX SUPPRESSED (#47) Field from the VA PRODUCT (#50.68) File for all VA Product displays.
- All options in Pharmacy that can generate new medication orders have been updated to now provide PGx order checks.

## Deleted Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No options have been deleted.

## Menu Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option has been added to the Outpatient Pharmacy Manager \[PSO MANAGER\] menu option:

Select Outpatient Pharmacy Manager \<TEST ACCOUNT\> Option: ?

Archiving ...

Autocancel Rx's on Admission

Bingo Board ...

Change Label Printer

Check Drug Interaction

Check Pharmacogenomic Interaction \*\*\*New option added here \*\*\*

Clozapine Pharmacy Manager ...

Copay Menu ...

DUE Supervisor ...

Enter/Edit Clinic Sort Groups

External Interface Menu ...

Label/Profile Monitor Reprint

Maintenance (Outpatient Pharmacy) ...

Medication Profile

Output Reports ...

Pharmacy Intervention Menu ...

Process Order Checks

Release Medication

Return Medication to Stock

Rx (Prescriptions) ...

ScripTalk Main Menu ...

Supervisor Functions ...

Suspense Functions ...

Update Patient Record

Verification ...

- The Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option has been added to the Pharmacist Menu \[PSO USER1\] menu option:

Select Pharmacist Menu \<TEST ACCOUNT\> Option: ?

Bingo Board User ...

Change Label Printer

Change Suspense Date

Check Drug Interaction

Check Pharmacogenomic Interaction \*\*\*New option added here \*\*\*

DUE Supervisor ...

Enter/Edit Clinic Sort Groups

External Interface Menu ...

Medication Profile

Pharmacy Intervention Menu ...

Print from Suspense File

Process Order Checks

Pull Early from Suspense

Queue CMOP Prescription

Release Medication

Return Medication to Stock

Rx (Prescriptions) ...

Update Patient Record

Verification ...

- The Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option has been added to the Unit Dose Medications \[PSJU MGR\] menu option:

Select Unit Dose Medications \<TEST ACCOUNT\> Option: ?

> Align Labels (Unit Dose)

> Discontinue All of a Patient's Orders

> Clozapine Inpatient Medications Manager ...

> ECO Edit Clinic Med Orders Start Date/Time

> EUP Edit Inpatient User Parameters

> IOE Inpatient Order Entry

> IPF Inpatient Profile

> Check Drug Interaction

> Check Pharmacogenomic Interaction \*\*\*New option added here\*\*\*

> INQuiries Menu ...

> Label Print/Reprint

> Non-Verified/Pending Orders

> Order Entry

> PADE Main Menu ...

> PAtient Profile (Unit Dose)

> Reports Menu ...

> Supervisor's Menu ...

- The Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option has been added to the IV Menu \[PSJI MGR\] menu option:

> Select IV Menu \<TEST ACCOUNT\> Option: ?

> CRL Change Report/Label Devices (IV)

> CIR Change to Another IV Room (IV)

> Drug Inquiry (IV)

> ECO Edit Clinic Med Orders Start Date/Time

> IOE Inpatient Order Entry

> IPF Inpatient Profile

> Barcode ID - Return and Destroy (IV)

> Check Drug Interaction

> Check Pharmacogenomic Interaction \*\*\*New option added here\*\*\*

> Label Menu (IV) ...

> Manufacturing List (IV)

> Order Entry (IV)

> Profile (IV)

> REPorts (IV) ...

> RETurns and Destroyed Entry (IV)

> SUSpense Functions (IV) ...

> Update Daily Ward List (IV)

> Ward List (IV)

- The Check Pharmacogenomic Interaction \[PSS CHECK PGX INTERACTION\] option and the Check Drug Interaction \[PSS CHECK DRUG INTERACTION\] option have been added to the Order Check Management \[PSS ORDER CHECK MANAGEMENT\] menu option:

> Select Order Check Management \<TEST ACCOUNT\> Option: ?

> Check Drug Interaction \*\*\*Option added\*\*\*

> Check Pharmacogenomic Interaction \*\*\*Option added\*\*\*

> Request Changes to Enhanced Order Check Database

Report of Locally Entered Interactions

- The Check Drug Interaction \[PSS CHECK DRUG INTERACTION\] option has been removed from the Pharmacy Data Management \[PSS MGR\] menu option:

Select Pharmacy Data Management \<TEST ACCOUNT\> Option: ?

CMOP Mark/Unmark (Single drug)

Dosages ...

Drug Enter/Edit

Order Check Management ...

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

Send Drug File Entries to External Interface

IV Additive/Solution ...

Warning Builder

Warning Mapping

PEPS Services ...

Inpatient Drug Management ...

~~Check Drug Interaction~~ \*\*\*Option removed\*\*\*

Infusion Instruction Management ...

Orders for MRRs With Removal Properties

# File Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\#51.26 PHARMACOGENOMIC GENES

This file contains a list of standard genes, associated synonyms, and a corresponding

> vendor gene for every standard gene. This file also contains a list of phenotypes that are appropriate for each gene. The associated vendor gene will be used for the pharmacogenomic order checks provided by the vendor. Updates cannot be made at a local facility.

> \#51.28 PHARMACOGENOMIC PHENOTYPES

> This file contains a list of standard phenotypes, associated synonyms, and a

> corresponding vendor phenotype for every standard phenotype. The associated

> vendor phenotype will be used for the pharmacogenomic order checks provided

> by the vendor. Updates cannot be made at a local facility.

\# 51.29 PHARMACOGENOMIC EMAIL LOG

This file contains genes and phenotypes that were received from the HDR to be used

for PGX order checks for a patient, but could not be mapped to a vendor gene or

phenotype. This file also tracks the emails sent to a PBM mail group responsible for

investigating and resolving these discrepancies.

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\#50.416 DRUG INGREDIENTS File

50.416,5 PGX ELIGIBLE PGX;1 SET (Required) (audited)

If this field is set to Yes, then this ingredient will participate in the PGx profile suppression rules.

50.416,6 PGX SUPPRESSED PGX;2 SET (Required) (audited)

If this field is set to Yes, then this ingredient will participate in the PGx profile suppression rules.

\#50.68 VA PRODUCT File

50.68,46 PGX ELIGIBLE PGX;1 SET (Required) (audited)

If this field is set to Yes, then any medication order for a drug matched to this VA Product will

participate in Pharmacogenomic (PGx) order checks.

50.68,47 PGX SUPPRESSED PGX;2 SET (Required) (audited)

If this field is set to Yes, then any profile medication order for a drug matched to this VA

Product will participate in the suppression rules for Pharmacogenomic (PGx) order checks.

\*\*\*Note: this field is not currently in use\*\*\*

\#51.26 PHARMACOGENOMIC GENES File

51.26,.01 NAME 0;1 FREE TEXT (Required)

This is the name of the gene. This field, in addition to the synonyms also in this file, will enable the

software to derive a vendor gene to be used in the pharmacogenomic order check for medication

orders.

51.26,1 FIRST DATABANK GENE 0;2 FREE TEXT (Required)

This field provides the mapping from the lab test gene to the First Databank gene. The First

Databank gene will be used when processing the pharmacogenomic order checks provided by First

DataBank.

51.26,2 SYNONYM 1;0 Multiple \#51.262

51.262,.01 SYNONYM 0;1 FREE TEXT (Multiply asked)

This is a synonym for the NAME field, which is the name of the gene. The synonym will be used for

mapping genes from lab test results to a First Databank gene that can be used in pharmacogenomic

order checking.

51.26,3 STANDARD PHENOTYPE 2;0 POINTER Multiple \#51.263

51.263,.01 STANDARD PHENOTYPE 0;1 POINTER TO PHARMACOGENOMIC

PHENOTYPES FILE (#51.28) (Multiply asked)

This phenotype is appropriate for the gene. It will be used in the Check Pharmacogenomic

Interaction \[PSS PGX TEST OPTION\] Option to limit the selection to only appropriate

phenotypes for each selected gene.

\*\*\*Note – There are other fields in this file that have to do with that standardization of the file

and the assignment of VHA Unique IDs (VUIDs). As of the release of Mocha 3.0, this file has not

been standardized and therefore these fields will not have data and are not in use.

\#51.28 PHARMACOGENOMIC PHENOTYPES File

51.28,.01 NAME 0;1 FREE TEXT (Required)

This is the name of the phenotype. This field, in addition to the synonyms also in this file,

will enable the software to derive a vendor phenotype to be used in the pharmacogenomic

order check for medication orders.

51.28,1 FIRST DATABANK PHENOTYPE 0;2 FREE TEXT (Required)

This field provides the mapping from the lab test phenotype to the First Databank phenotype.

The First Databank phenotype will be used when processing the pharmacogenomic order

checks provided by First DataBank.

51.28,2 SYNONYM 1;0 Multiple \#51.282

51.282,.01 SYNONYM 0;1 FREE TEXT (Multiply asked)

This is a synonym for the NAME field, which is the name of the phenotype. The synonym

will be used for mapping phenotypes from lab test results to a First Databank phenotype that

can be used in pharmacogenomic order checking.

\*\*\*Note – There are other fields in this file that have to do with that standardization of the file

and the assignment of VHA Unique IDs (VUIDs). As of the release of Mocha 3.0, this file has not

been standardized and therefore these fields will not have data and are not in use.

\# 51.29 PHARMACOGENOMIC EMAIL LOG File

51.29,.01 PATIENT 0;1 POINTER TO PATIENT FILE (#2) (Required)

This is the name of a patient.

51.29,1 PATIENT ICN 0;2 FREE TEXT

This is the patient's Integration Control Number (ICN).

51.29,2 GENE 1;0 Multiple \#51.292 (Add New Entry without Asking)

51.292,.01 GENE 0;1 FREE TEXT (Required)

This is the gene from the patient's lab data that can't map to a vendor gene.

51.292,1 PHENOTYPE 0;2 FREE TEXT

This is the phenotype from the patient's lab data that can't map to a vendor phenotype.

51.292,2 UNRESOLVED FLAG 0;3 SET (Required)

Identify if the mapping issue is on the gene, phenotype, or both.

51.292,3 EMAIL DATE 0;4 DATE (Required)

This is the date an email was sent to the Pharmacy Benefits Management (PBM) Outlook

mail group.

51.292,4 PATIENT LOCATION 0;5 FREE TEXT

This is the patient's location/site.

51.292,5 ORIGINATING PACKAGE 0;6 SET

This is the application where the order check attempt occurred but could not be performed

because of the unresolvable gene and/or phenotype.

\#59.7 PHARMACY SYSTEM File

59.7,103 VA PHARMACOGENOMICS URL PGX;1 FREE TEXT

This is the Uniform Resource Locator (URL) for the VA National Pharmacogenomics

program. This URL will be used for display when the URL normally received from the

Health Data Repository (HDR) is not available.

## Modified Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No previously existing fields have been modified.

# Other Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A summary of delivered additions/changes follows.

## Intervention Type additions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add the following two new entries to the APSP INTERVENTION TYPE (#9009032.3) File. The appropriate entry will auto-populate into the intervention when an intervention is created for a PGx Order Check.

PHARMACOGENOMIC HIGH ORDER CHECK

PHARMACOGENOMIC MEDIUM ORDER CHECK

## Order Check additions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Add the following two new entries to the ORDER CHECK (100.8) File, to allow CPRS to display and track the new PGx order checks.

> PHARMACOGENOMICS HIGH

> PHARMACOGENOMICS MODERATE

## Web Server addition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add the following entry to the WEB SERVER (#18.12) File. This, in conjunction with

the new PSS PGX -HDR SERVICE Web Service, enables the retrieval of patient

genomic data from the HDR so the most accurate PGx order checks can be performed for the

patient.

PSS PGX-WEB SERVER

## Web Service addition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add the following entry to the WEB SERVICE (#18.02) File. This, in conjunction with

the new PSS PGX -HDR SERVER Web Server, enables the retrieval of patient genomic

data from the HDR so the most accurate PGx order checks can be performed for the patient.

PSS PGX-WEB SERVICE

# # Known Anomalies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a list of known anomalies:

1.  When the profile suppression rules are applied against a PGx Medium severity order check and the order check should be suppressed because of the similar profile order, the order check does not get suppressed if the profile order is a Renewed IV Order.
2.  Some of the PGx field definitions in the VA PRODUCT (#50.68) File and the DRUG INGREDIENT (#50.416) need updated. The field descriptions were entered early in the project and since then the usage of some of these fields have changed, but the field descriptions were never updated accordingly.
3.  In the unlikely event of a rollback, upon a successful rollback of the OR\*3\*626 patch, this installation message that is written to the screen has the wrong patch number and a typo in the PGx monographs the word successful, but the rollback functionality was still successful: Patch OR\*3\*262 rollback successful!
4.  When a pharmacy technician enters or finishes an order that becomes a prescription and a high PGx check was received on the order, the order is treated as any order entered by a technician where there was no high order check received.
5.  When signing an order in CPRS for a medication order that had a combination of Drug Interaction Monographs and PGx monographs (called “Additional Information” in Pharmacy), the PGx monographs are not selectable.
6.  When using the Check PEPS Services Setup \[PSS CHECK PEPS SERVICES SETUP\] option in Pharmacy Data Management, a hard error may occur, depending on local DRUG (#50) File setup.
7.  The field description for the STANDARD PHENOTYPE (#.01) field of the STANDARD PHENOTYPE (#51.263) Subfile of the PHARMACOGENOMIC GENES (#51.26) file references in incorrect option name. \[PSS PGX TEST OPTION\]  should be changed to \[PSS CHECK PGX INTERACTION\].