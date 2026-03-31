---
title: PSO*7*354 Outpatient Pharmacy Automation Interface Expansion (OPAI) Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Outpatient Pharmacy Automation Interface Expansion (OPAI)
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*354
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - dispensing
  - automated
  - devices
  - outpatient
  - pharmacy
  - site
  - table
  - contents
  - device
  - drug
page_count: 0
word_count: 1781
section_count: 4
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p354_pss_1_156_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p354_pss_1_156_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

![](pso-7-354-outpatient-pharmacy-automation-interface-expansion-opai-release-notes/001.png)

Outpatient Pharmacy Automation Interface Expansion

Release Notes

PSS\*1\*156 & PSO\*7\*354

March 2012

Product Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Pharmacy Data Management V. 1.0](#pharmacy-data-management-v-10)
    - [OPAI Sub-File](#opai-sub-file)
    - [Drug Enter/Edit \[PSS DRUG ENTER/EDIT\] Option](#drug-enteredit-pss-drug-enteredit-option)
  - [Outpatient Pharmacy V. 7.0](#outpatient-pharmacy-v-70)
    - [Pharmacy Automated Dispensing Devices File (#52.53)](#pharmacy-automated-dispensing-devices-file-5253)
    - [Enter/Edit Automated Dispensing Devices](#enteredit-automated-dispensing-devices)
    - [OPAI Sub-File (#59.20081)](#opai-sub-file-5920081)
    - [Enter/Edit \[PSO SITE PARAMETERS\] Option](#enteredit-pso-site-parameters-option)
    - [Selected Printer Information](#selected-printer-information)
    - [Additional Information](#additional-information)
  - [Using the Automated Dispensing Device (ADD) Functionality](#using-the-automated-dispensing-device-add-functionality)
The Outpatient Pharmacy Automation Interface Functionality Expansion project is an enhancement to the Veterans Health Information Systems and Technology Architecture (VistA) Outpatient Pharmacy Automated Interface (OPAI). OPAI is used to send data to non - VistA pharmacy automation systems based upon the VistA Health Level 7 (HL7) Standards. Currently, OPAI is limited to sending data to only one dispensing device. This project provides OPAI with the capability to send data to multiple dispensing devices.
This project includes enhancements to the Outpatient Pharmacy interfaces. It does not include interfaces to automated dispensing systems used for inpatient medications. The enhancement to OPAI is restricted to HL7 Version 2.4. OPAI HL7 Version 2.2 is not supported by this project.
The OPAI Functionality Expansion release includes patches PSO\*7\*354 and PSS\*1\*156. These patches address specific functional enhancements to the software as listed in New Service Request (NSR), 20070106, and as approved by the Health Provider Systems Enterprise Systems Manager.
These patches provide functionality that allows changes to an Automated Dispensing Device (ADD) to enable pharmacists at a site to use more than one dispensing device at the same time. While the installation of the patches is required, the use of the multi-dispensing device functionality is left up to the site.
Installation instructions are included in the patch descriptions. Below is a list of the applications involved in this project along with their associated patch number:
<u>APPLICATION/VERSION PATCH</u>
PHARMACY DATA MANAGEMENT PSS\*1\*156
OUTPATIENT PHARMACY PSO\*7\*354
These patches should be installed in the order outlined above.

## Pharmacy Data Management V. 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*156 is being released as part of Pharmacy Legacy Enhancements to address the OPAI Enhancements. Veterans Affairs Medical Center (VAMC) facilities have moved to using multiple vendors for automated medication dispensing systems to improve the efficiency of outpatient pharmacy operations. The following enhancements were made to the Pharmacy Data Management software to allow any one division to have more than one automated dispensing device communicating with VistA through OPAI. A drug can be set up with an automated dispensing device to send data to a specific dispensing device.

The following associated patch must be installed before PSS\*1\*156:

> PSS\*1\*155

### OPAI Sub-File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new field \#906, sub-file \#50.0906 named OPAI was created in the DRUG file (#50). A drug and automated dispensing device can be setup for a specific division. The sub-file contains the following new fields:

DIVISION:

> This is the division associated with the automated dispensing device for the drug. The field is a pointer to the OUTPATIENT SITE file (#59).

WINDOW DNS NAME:

> This field is a pointer to the PHARMACY AUTOMATED DISPENSING DEVICES file (#52.53). This is the name of the automated dispensing device associated with this site. Orders with a WINDOW route will be sent to this ADD.

MAIL DNS NAME:

> This field is a pointer to the PHARMACY AUTOMATED DISPENSING DEVICES file (#52.53). This is the name of the automated dispensing device associated with this site. Orders with a MAIL route will be sent to this automated dispensing device.

### Drug Enter/Edit \[PSS DRUG ENTER/EDIT\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option was modified to add the new fields from the DRUG file (#50). This option should be used when a drug is to be sent to a specific dispensing device. Additionally, the “OP EXTERNAL DISPENSE” question was displayed only when a drug was associated with National Drug File (NDF). This association was removed so that the question is always asked. Below is an example of adding an automated dispensing device to a drug.

> Select OPTION NAME: PSS DRUG ENTER/EDIT Drug Enter/Edit

> Select DRUG GENERIC NAME: CIMETIDINE 200MG TAB GA301

> ...OK? Yes// (Yes)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This entry is marked for the following PHARMACY packages:

> Outpatient

> Unit Dose

> Non-VA Med

> GENERIC NAME: CIMETIDINE 200MG TAB Replace

> VA CLASSIFICATION: GA301//

> DEA, SPECIAL HDLG: 6P//

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> This entry is marked for the following PHARMACY packages:

> Outpatient

> Unit Dose

> Non-VA Med

> MARK THIS DRUG AND EDIT IT FOR:

> O - Outpatient

> U - Unit Dose

> I - IV

> D - Drug Accountability

> C - Controlled Substances

> X - Non-VA Med

> Enter your choice(s) separated by commas : O

> O - Outpatient

> \*\* You are NOW editing OUTPATIENT fields. \*\*

> AN Outpatient Pharmacy ITEM? Yes// (Yes)

> .

> .

> QUANTITY DISPENSE MESSAGE:

> OP EXTERNAL DISPENSE: YES//

> Defining a dispensing device at the drug level for a division will override

> the dispensing device settings in the OUTPATIENT SITE File (#59). If populated,

> the drug will be sent to the dispensing device for that division.

> Select DIVISION: XXXXX//

> DIVISION: XXXXX//

> WINDOW DNS NAME: SCRIPTPRO1//

> MAIL DNS NAME: SCRIPTPRO2//

> Select DIVISION:

## Outpatient Pharmacy V. 7.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSO\*7\*354 is being released as part of Pharmacy Legacy Enhancements to address the OPAI Enhancements. VAMC facilities have moved to using multiple vendors for automated medication dispensing systems to improve the efficiency of outpatient pharmacy operations. Patch PSO\*7\*354 makes the enhancements below to the Outpatient Pharmacy software, which allows any one division to have more than one automated dispensing device communicating with VistA through the OPAI.

The following associated patches must be installed before PSO\*7\*354:

> PSO\*7\*312

> PSO\*7\*330

> PSS\*1\*156

> PSO\*7\*359

> PSO\*7\*387

### Pharmacy Automated Dispensing Devices File (#52.53)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entries in this file are required only if the site wants to utilize the multiple dispensing functionality. The new file contains the following fields:

NAME:

> A free-text field that is between 3-30 characters in length; it is the name given to the automated dispensing device.

DNS:

> A free-text field that is between 1-50 characters in length; it stores the DNS name or IP address of the automated dispensing device.

PORT:

> This field is a numeric between 1 and 65535 with no decimal places. It stores the port associated with the automated dispensing device.

INACTIVE DATE:

> This is a date field, not required, but used to inactivate the OPAI connection to an automated dispensing device.

### Enter/Edit Automated Dispensing Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new menu option named *Enter/Edit Automated Dispensing Devices* \[PSO AUTO DISPENSING DEVICE\] option is used to maintain the PHARMACY AUTOMATED DISPENSING DEVICES file (#52.53). The option is located under the *Maintenance (Outpatient Pharmacy)* \[PSO MAINTENANCE\] menu. All automated dispensing devices used by an outpatient division should be set-up using this option. Below is an example of adding an automated dispensing device.

> Select ADD Name: OPTIFILL1

> Are you adding 'OPTIFILL1' as

> a new PHARMACY AUTOMATED DISPENSING DEVICES (the 7TH)? No// Y (Yes)

> PHARMACY AUTOMATED DISPENSING DEVICES DNS: 10.9.5.165

> PHARMACY AUTOMATED DISPENSING DEVICES PORT: 8060

> PHARMACY AUTOMATED DISPENSING DEVICES INACTIVE DATE:

> NAME: OPTIFILL1//

> DNS: 10.9.5.165//

> PORT: 8060//

> INACTIVE DATE:

### OPAI Sub-File (#59.20081)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new sub-file (#59.20081) multiple named OPAI was added to the DISPENSING SYSTEM PRINTER sub-file (#59.02008) in the OUTPATIENT SITE file (#59). The sub-file contains the following new fields:

DNS NAME:

> This field is a pointer to the PHARMACY AUTOMATED DISPENSING DEVICES file (#52.53).

CATEGORY:

> The CATEGORY field is a set of codes and is a required field. Categories provide the flexibility of routing RXs to different automated dispensing devices. The following are the valid codes:

| MCS  | MAIL - CS               |
|------|-------------------------|
| MNCS | MAIL - NCS              |
| MAIL | MAIL                    |
| WCS  | WINDOW - CS             |
| WNCS | WINDOW - NCS            |
| WIND | WINDOW                  |
| CS   | CONTROLLED SUBSTANCE    |
| NCS  | NONCONTROLLED SUBSTANCE |
| A    | ANY                     |
| S    | STORAGE                 |

> Note: The “ANY” category is only allowed (with the exception of S-storage) if no other categories are selected for the automated dispensing device and vice versa (i.e., if any other category is selected for the automated dispensing device, then the “ANY” category shall not be selectable). The “ANY” category will not work with any other category except “STORAGE”.

> Note: “STORAGE” denotes a 24/7 prescription pickup kiosk that stores prescriptions filled electronically by pharmacy and enables pharmacy customers to pick up their prescriptions without waiting in line. It enhances patient satisfaction, ensures the right prescription is delivered to the right patient thus enhancing patient safety, saving pharmacy time, and giving inventory control over the medications dispensed.

> The “S” category is allowed in combination with other categories and as standalone.

> Example: Allowable Category Combinations

> Allowable Category combinations when associating multiple automated dispensing devices to one dispensing printer:

1.  MCS, MNCS, WCS, WNCS, S\*
2.  MCS, MNCS, WIND, S\*
3.  WCS, WNCS, MAIL, S\*
4.  CS, MNCS, WNCS, S\*
5.  NCS, WCS, MCS, S\*
6.  MAIL, WIND, S\*
7.  CS, NCS, S\*
8.  ANY, S\*
9.  S\*

> \*Multiple storage devices can be associated with one dispensing printer.

> To avoid conflict, only certain category permutations shall be allowed.

> For example, users shall not be able to define categories of MCS to one automated dispensing device and MAIL for a different automated dispensing device linked to the same dispensing printer. Otherwise, a controlled substance Rx with a route of Mail would have the potential of being routed to two different automated dispensing devices, which presents a conflict.

> Within each set identified above, there can be any combination within each category (for example in \#1, categories MCS and WNCS can both be defined for a dispensing printer).

Again, the “ANY” category will not work with any other category except “STORAGE”.

The software will not allow the same category to be defined for different automated dispensing devices associated with a printer.

> **NOTE:** In order to exit the CATEGORY field, you must either enter ^ DNS NAME or select the “S” category.

### Enter/Edit \[PSO SITE PARAMETERS\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Site Parameter Enter/Edit* \[PSO SITE PARAMETERS\] option was modified for addition of the new fields in the OPAI multiple (#59.20081) in the OUTPATIENT SITE file (#59). To send data to a specific dispensing device, the setup must be associated with a printer. Below is an example of adding automated dispensing devices to a printer.

> Select OPTION NAME: PSO SITE PARAMETERS Site Parameter Enter/Edit

> Site Parameter Enter/Edit

> Outpatient Pharmacy software - Version 7.0

> Division: XXXXX 500

> You are logged on under the XXXXX division.

> Select PROFILE PRINTER: HOME// GENERIC INCOMING TELNET

> Select LABEL PRINTER: HOME// GENERIC INCOMING TELNET

> OK to assume label alignment is correct? YES//

> Bingo Board Display: OUTPATIENT//

> Select SITE NAME: XXXXX 500

> Select DISPENSING SYSTEM PRINTER: LEX1\$PRT

> DISPENSING SYSTEM PRINTER: LEX1\$PRT//

> Select DNS NAME: SCRIPTPRO1

> CATEGORY: CS CONTROLLED SUBSTANCE

> Select DNS NAME: SCRIPTPRO2

> CATEGORY: NON NONCONTROLLED SUBSTANCE

> CATEGORY: NONCONTROLLED SUBSTANCE//

### Selected Printer Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During prescription processing, if the printer selected has automated dispensing devices defined, the Rx will be routed to the appropriate automated dispensing devices. A message will display indicating the automated dispensing devices where the Rx will be routed. Below is an example of the routing message:

> PRESCRIPTIONS SENT TO:

> OPTIFILL1

> 100002815 ACETAMINOPHEN 325MG C.T.

> 100002816 AMOXICILLIN 250MG CAP

> 100002824 AMOXAPINE 50MG TAB

> SCRIPTPRO1

> 100002844 CIMETIDINE 200MG TAB

### Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new Integration Control Registration (ICR) \#5579 was created to grant the Pharmacy Data Management package read access to the PHARMACY AUTOMATED DISPENSING DEVICES file (#52.53).

The User Group requested that when a dispense complete message is received by VistA from the external dispensing interface, and if the mail tracking information is included in the 13th piece of the RXD segment, the activity log in the PRESCRIPTION file (#52) be updated with this information.

During testing, a problem was discovered in the *Print from Suspense File* \[PSO PNDLBL\] and *Reprint Batches from Suspense* \[PSO PNDRPT\] options. The ZTIO variable, which stores the label printer, was being reset to null after processing each patient prescription. As a result, a printer defined with multiple automated dispensing devices was not routing prescriptions properly. Routines PSOSULBL and PSOSUSRP were modified to address this problem.

## Using the Automated Dispensing Device (ADD) Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For sites wanting to continue with the current OPAI process, no change is necessary after installing the patches. If a site wants to take advantage of the multiple automated dispensing device functionality, the steps below should be followed:

1.  Setup the automated dispensing devices (ADD) using the new option, *Enter/Edit Automated Dispensing Devices* \[PSO AUTO DISPENSING DEVICE\] under *Maintenance (Outpatient Pharmacy)* \[PSO MAINTENANCE\].
2.  Setup the Dispensing System Printer(s), and then link to the appropriate automated dispensing devices using the option *Site Parameter Enter/Edit* \[PSO SITE PARAMETERS\].
3.  If orders for a specific drug need to be sent to a specific automated dispensing device, use the Drug *Enter/Edit* \[PSS DRUG ENTER/EDIT\] option to setup the automated dispensing device for that drug.
4.  Using the *Site Parameter Enter/Edit* \[PSO SITE PARAMETERS\] option, ensure that the appropriate settings are done for the following fields:
    - EXTERNAL INTERFACE should be set to either a ‘1’, ‘2’, ‘3’ or ‘4’ for orders to be sent to the external interface.

> 1- FOR SEND ALL ORDERS AND PRINT LABEL

> 2- FOR SEND ALL ORDERS AND DON'T PRINT LABEL

> 3- FOR SEND MARKED ORDERS AND DON'T PRINT

> 4 - FOR SEND MARKED ORDERS AND PRINT LABEL.

- automated dispense should be set to ‘HL7 V.2.4.’
- logical link should be set to ‘PSO DISP.’
- FILE RELEASE DATE/TIME: should be set to ‘YES’ (for bidirectional transmission – to get release data from the automated dispensing devices).

The setup of the Dispensing System Printer is the key to determine how orders will be sent to automated dispensing devices. The following are possible setup scenarios.

<u>No Dispensing System Printers</u>

If there is <u>no</u> Dispensing System Printer defined in the OUTPATIENT SITE file (#59), orders will be sent to the automated dispensing device based on the setting of the DISPENSE DNS NAME field (#2006) and DISPENSE DNS PORT field (#2007) in the OUTPATIENT SITE file (#59).

<u>Dispensing System Printers only</u>

If there are Dispensing System Printers and no associated automated dispensing devices in the OUTPATIENT SITE file (#59), orders will be sent to the automated dispensing device based on the setting of the DISPENSE DNS NAME field (#2006) and DISPENSE DNS PORT field (#2007) in the OUTPATIENT SITE file (#59).

<u>Dispensing System Printers and automated dispensing devices in OUTPATIENT SITE file (#59)</u>

If there are Dispensing System Printers and associated automated dispensing devices in the OUTPATIENT SITE file (#59), the order will be sent to the appropriate automated dispensing device.

<u>Dispensing System Printers and automated dispensing devices in OUTPATIENT SITE file (#59) and DRUG file (#50)</u>

If there are Dispensing System Printers and associated ADDs in the OUTPATIENT SITE file (#59) and automated dispensing devices in DRUG file (#50), the order will be sent to the ADD defined in the DRUG file (#50) for that division.

If there are Dispensing System Printers and associated automated dispensing devices in the OUTPATIENT SITE file (#59), but no automated dispensing devices in DRUG file (#50), the order will be sent to the appropriate automated dispensing device defined in the OUTPATIENT SITE file (#59).

Example: Create Rx order to sent to multiple ADDs

> Select OPTION NAME: PSO LM BACKDOOR ORDERS Patient Prescription Processing

> Patient Prescription Processing

> Outpatient Pharmacy software - Version 7.0

> Division: XXXXX 500

> PU Patient Record Update NO New Order

> PI Patient Information SO Select Order

> Select Action: Next Screen// NO New Order

> Eligibility: SERVICE CONNECTED 50% to 100% SC%: 60

> RX PATIENT STATUS: OPC//

> DRUG: BETA-CAROTENE

> Lookup: GENERIC NAME

> BETA-CAROTENE 30MG CAP DE890

> ...OK? Yes// (Yes)

> No Enhanced Order Checks can be performed.

> Reason: Vendor Database cannot be reached.

> Press Return to continue...:

> Now doing allergy checks. Please wait...

> VERB: TAKE

> Available Dosage(s)

> 1\. 30MG

> 2\. 60MG

> Select from list of Available Dosages, Enter Free Text Dose

> or Enter a Question Mark (?) to view list: 1 30MG

> You entered 30MG is this correct? Yes// YES

> VERB: TAKE

> DISPENSE UNITS PER DOSE(CAPSULE): 1// 1

> Dosage Ordered: 30MG

> NOUN: CAPSULE

> ROUTE: PO//

> Schedule: QAM (EVERY MORNING)

> LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

> CONJUNCTION:

> PATIENT INSTRUCTIONS:

> (TAKE ONE CAPSULE BY BY MOUTH EVERY MORNING)

> DAYS SUPPLY: (1-90): 30//

> QTY ( ) : 30// 30

> COPIES: 1// 1

> \# OF REFILLS: (0-11): 11//

> PROVIDER: OPPHARMACIST,FOUR//

> CLINIC: LAB// LAB

> MAIL/WINDOW: WINDOW// WINDOW

> METHOD OF PICK-UP:

> REMARKS:

> ISSUE DATE: MAY 26,2011// (MAY 26, 2011)

> FILL DATE: (5/26/2011 - 5/26/2012): MAY 26,2011// (MAY 26, 2011)

> Nature of Order: WRITTEN// W

> WAS THE PATIENT COUNSELED: NO// NO

> Do you want to enter a Progress Note? No// NO

> Rx \# 100002998 05/26/11

> OPPATIENT,TEN \#30

> TAKE ONE CAPSULE BY BY MOUTH EVERY MORNING

> BETA-CAROTENE 30MG CAP

> OPPHARMACIST,FOUR OPPHARMACIST,NINE

> \# of Refills: 11

> SC Percent: 60%

> Disabilities:

> LIMITED MOTION IN CERVICAL SPINE 60% - SERVICE CONNECTED

> Was treatment for a Service Connected condition? NO

> Is this correct? YES//

> Label Printer: TELNET-IN

> LABEL: QUEUE/CHANGE PRINTER/HOLD/SUSPEND or '^' to bypass Q// UEUE

> Select LABEL DEVICE: LEXMARK5\$PRT Plano

> LABEL(S) QUEUED TO PRINT

> PRESCRIPTIONS SENT TO:

> OPTIFILL1

> 100002998 BETA-CAROTENE 30MG CAP

> STORAGE DEVICES

> STORAGE_I

> 100002998 BETA-CAROTENE 30MG CAP

> PROFILES MUST BE SENT TO PRINTER !!

> Select PROFILE DEVICE: HOME//

Example: <span class="mark">REDACTED</span>VAMC dispensing system printer and ADDs set-up.

The <span class="mark">REDACTED</span>VAMC test site has configured seven (7) dispensing printers and two (2) automated dispensing devices to be used by seven (7) active divisions. Below is an example of the Orlando set-up in the OUTPATIENT SITE file (#59).

| DIVISION                           | DISPENSING SYSTEM PRINTER | ADD       | CATEGORY |
|----------------------------------------|-------------------------------|---------------|--------------|
| <span class="mark">REDACTED</span>CBOC | ORMCPTPHARM1                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM2                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM3                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM4                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM5                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP10                | VIE-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP6                 | VIE-SCRIPTPRO | ANY          |
| <span class="mark">REDACTED</span> OPC | ORMCPTPHARM1                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM2                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM3                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM4                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM5                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP10                | VIE-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP6                 | VIE-SCRIPTPRO | ANY          |
| <span class="mark">REDACTED</span>CBOC | ORMCPTPHARM1                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM2                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM3                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM4                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM5                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP10                | VIE-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP6                 | VIE-SCRIPTPRO | ANY          |
| <span class="mark">REDACTED</span>CBOC | ORMCPTPHARM1                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM2                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM3                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM4                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM5                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP10                | VIE-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP6                 | VIE-SCRIPTPRO | ANY          |
| <span class="mark">REDACTED</span>CBOC | ORMCPTPHARM1                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM2                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM3                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM4                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM5                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP10                | VIE-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP6                 | VIE-SCRIPTPRO | ANY          |
| <span class="mark">REDACTED</span>VAMC | ORMCPTPHARM1                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM2                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM3                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM4                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM5                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP10                | VIE-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP6                 | VIE-SCRIPTPRO | ANY          |
| VIERA OPC                              | ORMCPTPHARM1                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM2                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM3                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM4                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORMCPTPHARM5                  | ORL-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP10                | VIE-SCRIPTPRO | ANY          |
|                                        | ORVIPTPHARMP6                 | VIE-SCRIPTPRO | ANY          |