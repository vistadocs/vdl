---
title: MOCHA Version 1 Combined Builds Enhancements 1 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: Combined Builds Enhancements 1
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 1
patch_id: PSO*1
group_key: "PSO:PSO:1"
file_numbers: []
security_keys: []
menu_options: 0
description: The goal of the Pharmacy Reengineering (PRE) project is to replace the current M-based suite of pharmacy applications with a system that will better meet the current and expected business needs for the Department of Veterans Affairs (VA) and address the ever-changing patient safety issues. The first
audience: 
keywords: 
  - order
  - table
  - drug
  - clinic
  - contents
  - date
  - orders
  - inpatient
  - pharmacy
  - check
page_count: 0
word_count: 2283
section_count: 7
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/m1e1_pso_7_psj_5_pss_1_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/m1e1_pso_7_psj_5_pss_1_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

![](mocha-version-1-combined-builds-enhancements-1-release-notes/001.png)

Medication order check healthcare application (mocha) v1.0 ENHANCEMENTS 1

Release Notes

PSO\*7\*390, PSO\*7\*417, PSJ\*5\*260, PSJ\*5\*268, PSJ\*5\*288, PSS\*1\*164, PSS\*1\*169

January 2013

Product Development

*(This page included for two-sided copying.)*Table of Contents

# *(This page included for two-sided copying.)*


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying)
- [Introduction](#introduction)
- [Enhancements](#enhancements)
- [Installation Information](#installation-information)
- [Menu Changes](#menu-changes)
  - [New Options](#new-options)
  - [Changed Options](#changed-options)
  - [Deleted Options](#deleted-options)
  - [New Files](#new-files)
  - [New Fields](#new-fields)
- [Other Functionality](#other-functionality)
  - [Clinic Orders](#clinic-orders)
- [Impacts to Other Packages](#impacts-to-other-packages)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The goal of the Pharmacy Reengineering (PRE) project is to replace the current M-based suite of pharmacy applications with a system that will better meet the current and expected business needs for the Department of Veterans Affairs (VA) and address the ever-changing patient safety issues. The first phase, Medication Order Check Healthcare Application (MOCHA) v1.0, implements enhanced order checking functionality utilizing Health*e*Vet (H*e*V) compatible architecture and First DataBank (FDB), Drug Information Framework (DIF), and Application Program Interfaces (APIs). A Graphical User Interface (GUI) application has been developed for maintenance of FDB custom tables. A process to automatically update the standard and custom FDB data at each instance of the Cache’ database will also be provided.

This release notes document provides a brief description of the new features and functions of the MOCHA v1.0 Enhancements 1 (Enh 1) patches listed in the table below. More detailed information on the functionality can be found in the Application user and technical manuals found on the VistA Documentation Library (VDL).

| Application                    | Patch                                 |
|--------------------------------|---------------------------------------|
| Outpatient Pharmacy            | PSO\*7\*390, PSO\*7\*417              |
| Inpatient Medications          | PSJ\*5\*260, PSJ\*5\*268, PSJ\*5\*288 |
| Pharmacy Data Management (PDM) | PSS\*1\*164, PSS\*1\*169              |

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA Version 1 Enhancement 1provides the following enhancements:

- Adds and stores signs/symptoms to Allergy/ADR order check displays
- Provides an option on the medication profile to allow a user to check for drug-drug interactions and allergies before the drug is entered for that patient
- Adds a field on the patient medication profile header that displays the Creatinine Clearance (CRCL), if available
- Adds a field on the patient medication profile header that provides the user with the Body Surface Area (BSA) information
- All order checks will be performed upon verification of Inpatient non-verified orders
- Simplifies the prompts seen in Inpatient Medications, when a therapeutic duplication message allows an existing order to be discontinued
- Include IMO/Clinic orders to the enhanced order check process currently being performed in Backdoor Outpatient Pharmacy, and add recently discontinued and recently expired IMO/Clinic orders to the enhanced order check process currently being performed for Inpatient Medications.
- When processing an Inpatient or Outpatient Medication order (s) in backdoor pharmacy, in addition to the existing Allergy/ADR order check information, the Observed/Historical data is displayed with the related Allergy/ADR and on the order check.
- For a significant drug interaction message, the display states “Pending Order” and will be corrected to display “Pending Drug”
- Decouples the automated dispensing machine interface calls from the current Inpatient Medication (IP) package routines. This will alleviate the need to reenter the local modifications related to the automated dispensing machine interface calls to the routines when they are updated by a patch installation.
- Adds order checks for clinic orders
- New report under the PEPS Services menu to list when the Vendor Interface was unavailable
- Provides the ability to print the ‘Check PEPS Services Setup’ messages
- Changes the Dose Units listing so that the list displays alphabetically
- Provides an option to identify unmapped Local Possible Dosages: Find Unmapped Local Possible Dosages \[PSS LOCAL DOSAGES EDIT ALL\]
- Fixes a hard error when processing outpatient speed renew.
- Will not allow a user to select a supply item during Inpatient Medication Profile hidden option Check Drug Interaction.
- Fixes the scroll off issue during duplicate therapy order display.

# Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA v1.0 Enhancements 1 consists of eight VistA patches and one “.kid” file, which will be released together and must be installed together. Full installation instructions can be found in the patch descriptions on FORUM, however the list of patches (and one “.kid” file) and the order in which they must be installed are as follows:

1.  OR\*3\*352
2.  PSS\*1\*164
3.  PSS\*1\*169
4.  PSO\*7\*390
5.  PSO\*7\*417
6.  PSJ\*5\*268
7.  \<xxx\>\_1_0_P23.kid
8.  PSJ\*5\*260
9.  PSJ\*5\*288

For the “.kid” file, value of \<xxx\> will be determined by the ward automated dispensing equipment in use at your facility. If no ward automated dispensing equipment is in use, this file will not be needed. For those sites using Pyxis, xxx=PPU, for Omnicell sites, xxx=OPU, and for McKesson sites, xxx=MPU. To obtain this file or if additional information is required regarding this “.kid” file, please contact your site’s Informatix contact.

# Menu Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches PSJ\*5\*260 and PSO\*7\*390 introduced a menu change to the *Rx (Prescriptions*) menu, *Unit Dose Medication Menu*, *IV Menu*, *Outpatient Pharmacy Pharmacist Menu,* and *Outpatient Pharmacy Manager Menu*. The new option Check Drug Interaction was added to the menus. Details on the new menu option can also be found in the user manuals.

- Inpatient Medications Nurse’s User Manual v5.0
- Inpatient Medications Pharmacist’s User Manual v5.0
- Outpatient Pharmacy Manager's User Manual v7.0
- Outpatient Pharmacy Pharmacist’s User Manual v7.0
- Outpatient Pharmacy Technician's User Manual v7.0

#### Restructured Rx (Prescriptions) Menu (changes are in bold)

- *Patient Prescription Processing*
- *Barcode Rx Menu ...*
- *Check Drug Interaction*
- *Complete Orders from OERR*
- *Discontinue Prescription(s)*
- *Edit Prescriptions*
- *ePharmacy Menu ...*
- *List One Patient's Archived Rx's*
- *Manual Print of Multi-Rx Forms*
- *Reprint an Outpatient Rx Label*
- *Signature Log Reprint*
- *View Prescriptions*

#### Restructured Unit Dose Menu (changes are in bold)

Select Unit Dose Medications Option: ?

Align Labels (Unit Dose)

Discontinue All of a Patient's Orders

EUP Edit Inpatient User Parameters

ESD Edit Patient's Default Stop Date

Hold All of a Patient's Orders

IOE Inpatient Order Entry

IPF Inpatient Profile

Check Drug Interaction

INQuiries Menu ...

Label Print/Reprint

Non-Verified/Pending Orders

Order Entry

PAtient Profile (Unit Dose)

PIck List Menu ...

Reports Menu ...

Supervisor's Menu ...

#### Restructured IV Menu (changes are in bold)

Select IV Menu Option: ?

CRL Change Report/Label Devices (IV)

CIR Change to Another IV Room (IV)

Drug Inquiry (IV)

IOE Inpatient Order Entry

IPF Inpatient Profile

Barcode ID – Return and Destroy (IV)

Check Drug Interaction

Label Menu (IV) ...

Manufacturing List (IV)

Order Entry (IV)

Profile (IV)

REPorts (IV) ...

RETurns and Destroyed Entry (IV)

SUPervisor's Menu (IV) ...

SUSpense Functions (IV) ...

Update Daily Ward List (IV)

Ward List (IV)

#### Restructured Outpatient Pharmacy Pharmacist Menu (changes are in bold)

- *Bingo Board User ...*
- *Change Label Printer*
- *Change Suspense Date*
- *Check Drug Interaction*
- *DUE Supervisor ...*
- *Enter/Edit Clinic Sort Groups*
- *External Interface Menu ...*
- *Medication Profile*
- *Pharmacy Intervention Menu ...*
- *Print from Suspense File*
- *Process Drug/Drug Interactions*
- *Pull Early from Suspense*
- *Queue CMOP Prescription*
- *Release Medication*
- *Return Medication to Stock*
- *Rx (Prescriptions) ...*
- *Update Patient Record*
- *Verification ...*

#### Restructured Outpatient Pharmacy Manager Menu (changes are in bold)

- *Archiving…*
- *Autocancel Rx's on Admission*
- *Bingo Board...*
- *Change Label Printer*
- *Check Drug Interaction*
- *Clozapine Pharmacy Manager...*
- *Copay Menu…*
- *DUE Supervisor...*
- *Enter/Edit Clinic Sort Groups*
- *External Interface Menu...*
- *Label/Profile Monitor Reprint*
- *Maintenance (Outpatient Pharmacy)...*
- *Medication Profile*
- *Output Reports...*
- *Pharmacy Intervention Menu...*
- *Process Drug/Drug Interactions*
- *Release Medication*
- *Return Medication to Stock*
- *Rx (Prescriptions)...*
- *ScripTalk Main Menu...*
- *Supervisor Functions...*
- *Suspense Functions...*
- *Update Patient Record*
- *Verification...*

Patch PSS\*1\*169 introduced two menu changes to the *Pharmacy Data Management* menu. The new options Check Drug Interaction and Print Interface Data File were added to the menu. Details on the new menu options can also be found in the *Pharmacy Data Management User Manual v1.0*.

#### Restructured Pharmacy Data Management Menu (changes are in bold)

*Dosages ...*

> *Dosage Form File Enter/Edit*

> *Enter/Edit Dosages*

> *Most Common Dosages Report*

> *Noun/Dosage Form Report*

> *Review Dosages ReportLocal Possible Dosages ReportRequest Change to Dose UnitDrug Enter/EditOrder Check Management…*

> *Request Changes to Enhanced Order Check Database*

> *Report of Locally Entered InteractionsElectrolyte File (IV)Lookup into Dispense Drug FileMedication Instruction Management ...Medication Instruction File Add/EditMedication Instruction File ReportMedication Routes Management ...Medication Route File Enter/EditMedication Route Mapping ReportMedication Route Mapping History ReportRequest Change to Standard Medication RouteDefault Med Route for OI ReportOrderable Item Management ...*

> *Edit Orderable Items*

> *Dispense Drug/Orderable Item Maintenance*

> *Orderable Item/Dosages Report*

> *Patient Instructions Report*

> *Orderable Item ReportFormulary Information ReportDrug Text Management ...*

> *Drug Text Enter/Edit*

> *Drug Text File ReportPharmacy System Parameters EditStandard Schedule Management ...*

> *Standard Schedule Edit*

> *Administration Schedule File ReportSynonym Enter/EditControlled Substances/PKI Reports…*

> *DEA Spec Hdlg & CS Fed Sch Discrepancy*

> *Controlled Substances Not Matched to NDF*

> *CS (DRUGS) Inconsistent with DEA Spec Hdlg*

> *CS (Ord. Item) Inconsistent with DEA Spec HdlgSend Entire Drug File to External InterfaceIV Additive/Solution…IV Additive ReportIV Solution ReportMark PreMix SolutionsWarning BuilderWarning MappingPEPS Services…*

> *Check Vendor Database Link*

> *Check PEPS Services Setup*

> *Schedule/Reschedule Check PEPS Interface*

> *Print Interface Data File*

> *Inpatient Drug Management…*

> *ADditives File*

> *Dispense Drug Fields*

> *Dispense Drug/ATC Set Up*

> *Edit Cost Data*

> *EDit Drug Cost (IV)*

> *MARk/Unmark Dispense Drugs For Unit Dos*

> *PRimary Solution File (IV)*

> *Check Drug Interaction*

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following items are the new options:

- *Check Drug Interactions* option allows a user to check interactions between two or more drugs independent of a patient profile.
- *Print Interface Data File* option allows you to print a report from the VENDOR INTERFACE DATA file (#59.74) which keeps track of when and for how long the vendor interface is unavailable while a background process monitors the status of the interface and records in this file when the interface is down, when it becomes available again, and the total time it was unavailable.
- *Find Unmapped Local Possible Dosages* option allows the user to identify all Local Possible Dosages that are eligible for dosage checks and do not have either the Numeric Dose or Dose Unit populated. This option was originally installed with PSS\*1\*129 and subsequently removed upon the installation of MOCHA v1.0. This is a standalone option and should be assigned to users who maintain the local Drug File (usually the pharmacy ADPAC).

## Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## Deleted Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

# Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Clinic Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinic orders are created via CPRS generally using the Meds Inpatient tab or the IV Fluids tab. Drug orders that have a clinic and an appointment date and time are considered clinic orders. The clinic must be defined with ‘ADMINISTER INPATIENT MEDS?’ prompt answered YES under the SETUP A CLINIC \[SDBUILD\] option in the Scheduling package. Defining the clinic in this manner ensures that an appointment date and time are defined. Orders placed via backdoor Inpatient Medications are not considered clinic orders.

MOCHA v1.0 Enhancement 1 adds drug interaction and therapeutic duplication order checks for clinic orders to Outpatient Pharmacy. Previously Inpatient Medications package performed order checks on active, pending and non-verified clinic orders. With the MOCHA v1.0 Enhancement 1, Inpatient Medications will perform enhanced order checks for recently discontinued and expired Inpatient Medications clinic orders.

For both packages, the system will display clinic orders in a standard format to differentiate them from Inpatient Medications and Outpatient Pharmacy order checks.

Discontinued/expired orders must have a stop date within the last 90 days to be evaluated during enhanced order checks. For pending clinic orders, a variety of start and stop dates are available based on the information that the provider enters during initial order entry. The following are the scenarios that drive which dates will be displayed for the clinic order:

- If there are start/stop dates defined, they are displayed.
- If there are no stop/start dates defined, the ‘requested start/stop dates’ will be displayed with the word “Requested” prior to the start/stop date header.
- If there are no requested start/stop dates defined, the order date will be displayed and the start/stop date headers will be displayed with “\*\*\*\*\*\*\*\*” for the date.
- If there is either a requested start date or a requested stop date, the available date will be displayed and “\*\*\*\*\*\*\*\*” will be displayed for the undefined date.

Unit dose clinic order example:

Now Processing Enhanced Order Checks!  Please wait...

This patient is receiving the following order(s) that have a CRITICAL Drug

Interaction with CIMETIDINE 300 MG:

      Clinic Order: PHENYTOIN 100MG CAP (DISCONTINUED)

          Schedule: Q8H

           Dosage: 100MG

        Start Date: FEB 27, 2012@13:00

         Stop Date: FEB 28, 2012@15:22:27

Concurrent use of cimetidine or ranitidine may result in elevated levels

of and toxicity from the hydantoin. Neutropenia and thrombocytopenia have

been reported with concurrent cimetidine and phenytoin. 

IV Clinic order example:

This patient is receiving the following order(s) that have a CRITICAL Drug

Interaction with WARFARIN 2MG TAB:

      Clinic Order: POTASSIUM CHLORIDE 20 MEQ (ACTIVE)

Other Additive(s): MAGNESIUM SULFATE 1 GM (1), CALCIUM GLUCONATE 1 GM (2),

                    HEPARIN 1000 UNITS, CIMETIDINE 300 MG

       Solution(s): DEXTROSE 20% 500 ML 125 ml/hr

                    AMINO ACID SOLUTION 8.5% 500 ML 125 ml/hr

        Start Date: APR 05, 2012@15:00

         Stop Date: APR 27, 2012@24:00

The pharmacologic effects of warfarin may be increased resulting in severe

bleeding.

Therapeutic Duplication - IV and Unit Dose clinic order therapeutic duplications display in the same format as drug interactions.

Unit Dose Example:

================================================================================

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es):

Drug(s) Ordered:

   POTASSIUM CHLORIDE 30 MEQ

         Clinic Order: POTASSIUM CHLORIDE 10MEQ TAB  (PENDING)

             Schedule: BID

               Dosage: 20MEQ

Requested Start Date: NOV 20, 2012@17:00

            Stop Date: \*\*\*\*\*\*\*\*

Class(es) Involved in Therapeutic Duplication(s): Potassium

================================================================================

Do you wish to continue with the current order? YES//

IV Example:

================================================================================

This patient is already receiving the following INPATIENT and/or OUTPATIENT

order(s) for a drug in the same therapeutic class(es):

Drug(s) Ordered:

   CEFAZOLIN 1 GM

         Clinic Order: CEFAZOLIN 2 GM (PENDING)

          Solution(s): 5% DEXTROSE 50 ML

           Order Date: NOV 20, 2012@11:01

           Start Date: \*\*\*\*\*\*\*\*

            Stop Date: \*\*\*\*\*\*\*\*

         Clinic Order: CEFAZOLIN SOD 1GM INJ (EXPIRED)

          Solution(s): 5% DEXTROSE 50 ML

           Start Date: OCT 24, 2012@16:44

            Stop Date: OCT 25, 2012@24:00

Class(es) Involved in Therapeutic Duplication(s): Beta-Lactams,

   Cephalosporins, Cephalosporins - 1st Generation

================================================================================

Do you wish to continue with the current order? YES//

# Impacts to Other Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR\*3\*352 will be released in conjunction with PSO\*7\*390, PSO\*7\*417, PSJ\*5\*260, PSJ\*5\*268, PSJ\*5\*288, PSS\*1\*164, and PSS\*1\*169. It provides CPRS functionality for the enhancements to MOCHA 1.0.

Sites that utilize the Informatix dispensing machine interface will need to obtain and install the appropriate update from Informatix. This update will be delivered in a host file, appropriate to the machine type used at each site. This update will need to be loaded after PSJ\*5\*268, and before any attempt is made to use the machine interface. The table below lists the appropriate host file for each machine interface.

| File Name       | Machine Type |
|-----------------|--------------|
| PPU_1_0_P23.kid | Pyxis        |
| OPU_1_0_P23.kid | Omnicell     |
| MPU_1_0_P23.kid | McKesson     |