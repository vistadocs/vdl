---
title: Benefits Management Version 4 Release Notes-Extract Enhancements Phases I thru II
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: Extract Enhancements Phases I thru II
app_code: PSU
app_name: "Pharmacy: Benefits Management"
section: CLI
app_status: active
pkg_ns: PSU
patch_ver: 4
patch_id: PSU*4
group_key: "PSU:PSU:4"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - shall
  - patient
  - table
  - contents
  - pharmacy
  - total
  - number
  - units
  - extract
  - phase
page_count: 0
word_count: 5620
section_count: 15
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/psu_4_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/psu_4_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=91"
---

> ![](benefits-management-version-4-release-notes-extract-enhancements-phases-i-thru-i/001.png)

PHARMACY BENEFITS MANAGEMENT(PBM)Extract EnhancementsRELEASE NOTES

June 2005

VistA Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [User Interfaces](#user-interfaces)
  - [Hardware Interfaces](#hardware-interfaces)
  - [Software Interfaces](#software-interfaces)
  - [Communications Interfaces](#communications-interfaces)
  - [Enhancements Summary](#enhancements-summary)
  - [Pre-Installation Setup](#pre-installation-setup)
- [New Features](#new-features)
  - [New Extracts](#new-extracts)
    - [Phase I](#phase-i)
    - [Phase II](#phase-ii)
  - [New Options](#new-options)
    - [Phase I](#phase-i-1)
    - [Phase II](#phase-ii-1)
  - [New Fields](#new-fields)
    - [Phase I](#phase-i-2)
    - [Phase II](#phase-ii-2)
  - [New Reports](#new-reports)
    - [Phase I](#phase-i-3)
    - [Phase II](#phase-ii-3)
- [Modified Features](#modified-features)
  - [Modified Extracts](#modified-extracts)
    - [Phase I](#phase-i-4)
    - [Phase II](#phase-ii-4)
  - [Modified Options](#modified-options)
    - [Phase I](#phase-i-5)
    - [Phase II](#phase-ii-5)
  - [Modified Fields](#modified-fields)
  - [Modified Reports](#modified-reports)
- [New Functionality](#new-functionality)
- [Impact on Other VistA Software Packages](#impact-on-other-vista-software-packages)
Pharmacy Benefits Management (PBM) V. 4.0 is a new enhanced version of the software and replaces PBM Version 3.0. It contains enhancements to support the Veterans Affairs National Formulary (VANF), disease management issues, and patient safety initiatives.

## User Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software product shall conform to the existing VistA conventions and utilize a roll and scroll based interface. Software modifications shall be tested by Department of Veterans Affairs (VA) facilities to ensure that the software modifications meet the needs of the Veterans Health Administration (VHA) user.

## Hardware Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product shall run on standard hardware platforms used by the Department of Veterans Affairs Healthcare facilities. These systems consist of standard or upgraded Alpha AXP clusters and run VMS DSM, Cache NT, or Cache VMS.

## Software Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following software must be running to support the enhancements requested.

|                                                              |                            |
|--------------------------------------------------------------|----------------------------|
| Package                                                  | Minimum Version Needed |
| Adverse Reaction Tracking (ART)                              | 4.0                        |
| Auto Replenishment/Ward Stock (AR/WS)                        | 2.3                        |
| Controlled Substances (CS)                                   | 3.0                        |
| Drug Accountability                                          | 3.0                        |
| Inpatient Medications                                        | 5.0                        |
| Integrated Funds Control, Accounting and Procurement (IFCAP) | 5.1                        |
| Kernel                                                       | 8.0                        |
| Laboratory                                                   | 5.2                        |
| MailMan                                                      | 8.0                        |
| National Drug File (NDF)                                     | 4.0                        |
| Outpatient Pharmacy                                          | 7.0                        |
| Patient Care Encounter (PCE)                                 | 1.0                        |
| Patient Information Management System (PIMS)                 | 5.3                        |
| Pharmacy Data Management (PDM)                               | 1.0                        |
| VA FileMan                                                   | 22.0                       |
| Visit Tracking                                               | 2.0                        |

## Communications Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The extracted data is electronically exported via MailMan to the PBM national database at Hines from each VA medical center or outpatient clinic. MailMan messages are downloaded to text files onto the PBM network and run through a translation program. The data is then appended to an existing PBM Pharmacy dispensing master file.

## Enhancements Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following summarizes changes that were made to the PBM application during recent enhancements. More detailed descriptions may be found in the remainder of this document.

Phase I Enhancements

The following enhancements were introduced with the release of PSU\*3\*19. This functionality has been used in the field for the past two years.

- Created new extracts to gather Patient Demographics, Outpatient Visits, Inpatient Patient Treatment File (PTF) Records, and Provider Data.
- Modified the Pharmacy Patient Intravenous (IV), Pharmacy Patient Unit Dose (UD), Prescription, and CS extracts to remove and add data elements.
- Created new fields in the PHARMACY PATIENT file (#55) to track when pharmacy services were first provided to the patient.
- Modified the Description within the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option and the *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option to include the new extracts and the primary files from which the data is extracted.
- Created summary reports for Patient Demographics when the IV, UD, or Prescription extracts are run.
- Created a Provider Data Summary Report to assist sites in cleaning up and updating provider data records.
- Provided users with the ability to generate a detailed MailMan message without having to transmit to the PBM national database at Hines.

  
Phase II Enhancements

The following enhancements are being introduced with the release of PBM V. 4.0.

- Created two new extracts to gather patient Allergy/Adverse reactions and Vital/Immunization data.
- Modified the IV, UD, AR/WS Stats, Prescription, and CS extracts for Automated Management Information System (AMIS) reporting.
- Modified the IV, UD, AR/WS Stats, and Prescription extracts by adding new data elements.
- Created the following options to support the new functionality:
  - *Retransmit Patient Demographic Data* \[PSU RETRANSMIT PATIENT DATA\]
  - *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\]
  - *PBM Manager Menu* \[PSU PBM MANAGER MENU\]
- Modified the Description within the *Pharmacy Background Job Check* \[PSU PBM JOB CHECK\] option to adjust the number of days from six (6) to three (3) for a report to be completed.
- Provided for Division/Outpatient Site assignments for data extracted from AR/WS Stats, CS, and Procurement, excluding Integrated Funds Control, Accounting, and Procurement (IFCAP).
- Created new summary reports for AMIS reporting.
- Decreased extraction times by collecting patient demographic data in real time.

## Pre-Installation Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Parameters

All sites need to set up parameters for the new global ^PSUDEM prior to installing PSU 4.0. Refer to the PBM Extract Enhancements Installation Guide dated June 2005 for detailed instructions.

*(This page included for two-sided copying.)*

<span id="_Toc107123910" class="anchor"></span>

# New Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section documents features that were added during the PBM Enhancements project.

## New Extracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New extracts were added to the PBM application to provide additional data as described below. The output for all of these extracts provides the facility number at which the database resides to identify the sender of the MailMan message. If no data exists for any of the data fields to be extracted, a null value is sent.

### Phase I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following extracts were added with the release of PSU\*3\*19 and have been in use in the field for the past two years.

Patient Demographics

The Patient Demographics extract provides a means to collect demographic information for all patients within a facility with two exceptions: test patients and patients with a date of death before 7/1/98. Prior to PBM V. 4.0, this information could be obtained manually as part of the autojob. The autojob option has been modified, but the user may still run this information manually through the *PBM Manager Menu* \[PSU PBM MANAGER MENU\] option.

Outpatient Visits

The Outpatient Visits extract reports all outpatient visits within the reporting month within the V POV file (#9000010.07). Only those visits with associated ICD and/or CPT codes are extracted.

Inpatient PTF Record

The Inpatient PTF Record collects inpatient treatment file data. For inpatient stays, the discharge date is used to identify and extract PTF records. The start date of this extract shall be the discharge date 30 days prior to the first date of the reporting period. For example, if the reporting period is the month of August, the start date for this extract shall be 8/1 minus 30 days.

Provider Data

The Provider Data Extract incorporates provider data elements currently pulled from the IV, UD, and Prescription, as well as additional requested elements. The extract criterion is based on whether or not any provider data elements are extracted in any other PBM software extracts.

### Phase II

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following extracts were added with the release of PBM V. 4.0 and are new to the field.

Allergy/Adverse Event

The Allergy/Adverse Event extract collects allergy and adverse reactions documented for a patient using the verification date/time for the reporting period. Only verified allergy and adverse reactions shall be extracted by using the verification date/time. Any allergy or adverse reaction marked as entered in error shall be screened out. Allergy or adverse reaction data will not be extracted in the following circumstances:

- Allergy or adverse reactions entered for a test patient. A test patient is identified by having five leading zeros in the SOCIAL SECURITY NUMBER field (#.09) and/or having the TEST PATIENT INDICATOR field (#.6) set to ‘Yes’ in the PATIENT file (#2).
- Allergy or adverse reactions to an immunization recorded in the Patient Care Encounter (PCE) application. Allergy or adverse reactions shall only be extracted from the PATIENT ALLERGIES file (#120.8).

All event date/time(s) recorded in the ADVERSE REACTION REPORT file (#120.85) within the reporting period for a verified allergy/adverse reaction shall be extracted.

Vital/Immunization Record

The Vital/Immunization Record extract collects patients’ vital and immunization records, and both types of records are transmitted in the same MailMan message. The latest vital measurements for each vital type requested and immunization data are extracted using the date/time that the vitals were taken or the immunization was given for the reporting period. Data is not extracted for test patients, who are identified by having five leading zeros in the SOCIAL SECURITY NUMBER field (#.09) and/or having the TEST PATIENT INDICATOR field (#.6) set to ‘Yes’ in the PATIENT file (#2).

Any vital measurement marked as entered in error shall be screened out. Vital measurements are extracted for the following vital types:

- Blood Pressure
- Height
- Weight
- Pain
- Pulse
- Pulse Oximetry

<span id="_Toc107123912" class="anchor"></span>

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new options were created to support the enhanced functionality in the PBM V. 4.0 application.

### Phase I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new options were added during Phase I of this project.

### Phase II

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options were added with the release of PBM V. 4.0 and are new to the field.

*Retransmit Patient Demographic Data*\[PSU RETRANSMIT PATIENT DATA\]

The *Retransmit Patient Demographic Data* \[PSU RETRANSMIT PATIENT DATA\] option was created to retransmit patient demographic data stored in the new PBM file. When a user first enters the option, the software shall display the purpose of this option and the dates available for inclusion in the extract. Full months are available for monthly extract retransmissions, or a date range may be selected from the available dates. Modified patient data is available for the preceding 90 days.

*Map Pharmacy Locations*\[PSU MAP PHARMACY LOCATIONS\]

The *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] option was created to allow a user to map Area of Uses from the AR/WS Stats application, Narcotic Area of Uses from the CS application, and Pharmacy Locations from the Drug Accountability application to a specific Division or Outpatient Site.

*PBM Manager Menu*\[PSU PBM MANAGER MENU\]

This option was created to grant the user access to the following options:

- *Manual Pharmacy Statistics* \[PSU PBM MANUAL\]
- *Retransmit Patient Demographic Data* \[PSU RETRANSMIT PATIENT DATA\]
- *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\]

<span id="_Toc107123913" class="anchor"></span>

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new fields were created to support the enhanced functionality in the PBM V. 4.0 application.

### Phase I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new fields were added with the release of PSU\*3\*19 and have been in use in the field for the past two years. These fields were created in the PHARMACY PATIENT file (#55) to track when pharmacy services were first provided to the patient. Outpatient Pharmacy and Inpatient Medications applications were modified to populate both of these fields.

First Service Date

The FIRST SERVICE DATE field (#.07) populates with the prescription login date when the IV or UD order is entered and verified for a patient who is not found in the PHARMACY PATIENT file (#55) and/or for whom no prescription or orders are stored. The date entered is the date the first prescription is entered and verified into the system.

Actual/Historical Flag

The ACTUAL/HISTORICAL FLAG field (#.08) records whether the date entered is the actual or historical date that a patient first received pharmacy services. This field contains an “A” for “Actual” whenever a prescription (IV or UD) is entered and verified for a patient who is not found in the PHARMACY PATIENT file (#55) and/or for whom no prescription (IV or UD) orders are stored. For all historical dates populated, the software shall populate this new field with an “H” for “Historical.” Once the population of historical data is complete, the user who initiated the install and the members of the PSU PBM mail group shall receive a MailMan message with a subject of “BUILD OF FIRST PHARMACY SERVICE INFO COMPLETE.”

### Phase II

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new fields were added to PHARMACY SYSTEM file (#59.7) during Phase II of this project:

PBM AR/WS AOU MAPPINGS multiple (#90.01)

AR/WS AOU field (#.01)

DIVISION field (#.02)

OUTPATIENT SITE field (#.03)

PBM CS NAOU MAPPINGS multiple (#90.02)

CS NAOU field (#.01)

DIVISION field (#.01)

OUTPATIENT SITE field (#.02)

PBM DA PHARM LOC MAPPINGS multiple (#90.03)

DA PHARMACY LOCATION field (#.01)

DIVISION field (#.02)

OUTPATIENT SITE FIELD (#.03)

The following new file and fields were added:

PBM PATIENT DEMOGRAPHICS file (#59.9)

EVENT DATE/TIME field (#.01)

PATIENT field (#.02)

A new PBM PATIENT DEMOGRAPHICS file (#59.9) was added to PBM V. 4.0 as a repository in which to temporarily store new or updated patient demographic data in real time until the data is compiled and transmitted on a monthly basis to the PBM national database. Only one demographics record per patient shall be retained in the file for a reporting period. The data is retained in this file for 75 days, after which time it is purged.

## New Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New reports were created to provide the user with more detailed information. These reports are described in this section.

### Phase I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new reports were added with the release of PSU\*3\*19 and have been in use in the field for the past two years.

Patient Demographics Summary Report

This report is automatically generated when an IV, UD, or Prescription extract is run. The report displays a heading of “Unique Patients Report” for the specific extract.

Example: Patient Demographics Summary Report

Subj: V. 4.0 PBMPD 30109 605 JERRY L PETTIS VAMC \[#9138\] 09/01/04@10:24

18 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

PHARMACY INPATIENT (IV) UNIQUE PATIENTS REPORT SEP 01, 2004

-------------------------------------------------------------------------------

SEP 01, 2001 through SEP 30, 2001

===============================================================================

UNIQUE

---------------------------------------------------------------------

Total unique Inpatients across all divisions: 330

Total unique Outpatients across all divisions: 169

---------------------------------------------------------------------

JERRY L PETTIS VAMC Division: 451

------------

Total of all Divisions: 451

\* This report includes Outpatients receiving IV orders.

\*\*PLEASE NOTE: Final TOTAL may not match sum of all SUBTOTALS. A patient may

have been provided pharmacy services at more than one outpatient and/or

inpatient division.

  
Provider Summary Report

This report was created to assist sites in cleaning up and updating provider data records. A Provider message summary report shall be generated when the monthly *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] or the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] options are run. It shall not be generated if the user runs the IV, UD, Prescription or Patient Demographics extract using the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option. The user shall be able to run this report independent of any other extract. No other output shall be generated other than this report, even though the report’s extract criteria is based on the IV, UD, Prescription, and Patient Demographics extracts. The user shall be warned when selecting this report through the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] option that it may take a while for the report to be generated and that it is recommended to be run off peak hours.

Example: Provider Summary Report

Subj: V. 4.0 PBMPRO 30109 605 JERRY L PETTIS VAMC \[#7668\] 07/18/04@19:41

432 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Provider Summary Report JUL 18, 2004

SEP 01, 2001 through SEP 30, 2001

-------------------------------------------------------------------------------

Total Number of Incomplete Provider Records Extracted: 252

-------------------------------------------------------------------------------

IEN Provider Name (SSN) Missing Data

-------------------------------------------------------------------------------

3 PBMPROVIDER,ONE (????) SSN

78 PBMPROVIDER,TWO (0036) PROVIDER CLASS

238 PBMPROVIDER,THREE (5698) SPECIALTY

SUBSPECIALTY

549 PBMPROVIDER,FOUR (????) SSN

SPECIALTY

SUBSPECIALTY

607 PBMPROVIDER,FIVE (6026) PROVIDER CLASS

Subj: V. 4.0 PBMPRO 30109 605 JERRY L PETTIS VAMC \[#7668\] Page 2

-------------------------------------------------------------------------------

642 PBMPROVIDER,SIX (9499) PROVIDER CLASS

658 PBMPROVIDER,SEVEN (1826) SERVICE/SECTION

1131 PBMPROVIDER,EIGHT (6200) SERVICE/SECTION

1177 PBMPROVIDER,NINE (2889) SERVICE/SECTION

1495 PBMPROVIDER,TEN (6385) PROVIDER CLASS

1599 PBMPROVIDER,ELEVEN (5911) SERVICE/SECTION

1618 PBMPROVIDER,TWELVE (4511) SERVICE/SECTION

1834 PBMPROVIDER,THIRTEEN (3045) PROVIDER CLASS

1868 PBMPROVIDER,FOURTEEN (0711) PROVIDER CLASS

SERVICE/SECTION

SPECIALTY

SUBSPECIALTY

1883 PBMPROVIDER,FIFTEEN (0660) SERVICE/SECTION

1896 PBMPROVIDER,SIXTEEN (7456) PROVIDER CLASS

SPECIALTY

SUBSPECIALTY

1897 PBMPROVIDER,SEVENTEEN (9472) PROVIDER CLASS

1919 PBMPROVIDER,EIGHTEEN (9754) PROVIDER CLASS

2001 PBMPROVIDER,NINETEEN (2958) PROVIDER CLASS

2023 PBMPROVIDER,TWENTY (0582) PROVIDER CLASS

### Phase II

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following report was added with the release of PBM V. 4.0 and is new to the field.

AMIS Summary Report

The Statistical Data Summary Report has been eliminated from the IV, UD, ARWS Stats, and CS extracts and replaced with the AMIS Summary Report, which is broken down by Division. The AMIS Summary Report was also added to the Prescription extract; however, the Statistical Data Summary report was retained in that extract.

Example: AMIS Summary Report

Subj: V.4.0 PBMIV 30109 605 JERRY L PETTIS VAMC \[#7571\] 07/16/04@14:39

62 lines

From: PBMPHARMACIST,TWO In 'IN' basket. Page 1

------------------------------------------------------------------------------

IV AMIS Summary for SEP 1,2001 through SEP 30,2001 for JERRY L PETTIS VAMC

NET Cost/

LVPs LVPs LVPs LVPs LVPs Total NET LVPs

Division DISP RET DES CAN DISP Cost DISP

------------------------------------------------------------------------------

JERRY L PETTIS VA 884 0 0 0 883 \$ 417.05 \$ .47

------------------------------------------------------------------------------

Total 884 0 0 0 883 \$ 417.05 \$ .47

NET Cost/

IVPBs IVPBs IVPBs IVPBs IVPBs Total NET IVPBs

Division DISP RET DES CAN DISP Cost DISP

------------------------------------------------------------------------------

*(This page included for two-sided copying.)*

# Modified Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section documents features that were modified during the PBM Enhancements project.

## Modified Extracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The section describes modifications made to existing extracts.

### Phase I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following changes in data elements have existed in the field for the past two years.

The data elements that changed with the release of PSU\*3\*19 are listed below.

The following data elements were removed from the IV, UD, and Prescription extracts:

- Provider Class
- Provider Service/Section
- Provider Specialty
- Provider Subspecialty

The following data elements were added to the extracts listed below:

IV Extract

- Patient Integrated Control Number from the PATIENT file (#2)
- Provider Local Internal Entry Number (IEN) from the NEW PERSON file (#200)
- Stop Date/Time of Order from the STOP DATE/TIME sub-field (#.03)

UD Extract

- Patient Integrated Control Number (ICN) from the PATIENT file (#2)
- Provider Local Internal Entry Number (IEN) from the NEW PERSON file (#200)
- Stop Date/Time of Order from the STOP DATE/TIME sub-field (#34)

Prescription Extract

- Patient Integrated Control Number (ICN) from the PATIENT file (#2)
- Provider Local Internal Entry Number (IEN) from the NEW PERSON file (#200)
- Cancel Date from the CANCEL DATE field (#26.1)

CS Extract

- Patient Integrated Control Number (ICN) from the PATIENT file (#2)

### Phase II

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](benefits-management-version-4-release-notes-extract-enhancements-phases-i-thru-i/002.png)Note: Enhancements to the AR/WS Stats, Procurement, and CS extracts during Phase II shall require users to map pharmacy-defined locations from the AR/WS Stats, CS, and Drug Accountability applications to a specific Medical Center Division or Outpatient Pharmacy Site. HL7 links and protocols will have to be loaded at all facilities and in the PBM national database in order for the messaging to function properly.

The enhancements described in this section were made in PBM V. 4.0 and are new to the field.

IV Extract

The following new data elements were added to the IV extract to support AMIS reporting.

- *Number of IV Bags/Syringes Dispensed*: If the DAILY USAGE is set to “Yes”, the ACTION is set to “Dispensed”, and the DATE is within the reporting period, the number of LABELS (1 label = 1 bag/syringe) shall be counted. The number of LABELS for all DATES within the reporting period shall be totaled, and the total number of IV bags/ syringes dispensed shall be transmitted. If there are no LABELS with the ACTION of “Dispensed” to be counted for the reporting period, a value of “0” shall be transmitted.
- *Number of IV Bags/Syringes Recycled*: If the DAILY USAGE is set to “Yes”, the ACTION is set to “Recycled”, and the DATE is within the reporting period, the number of LABELS (1 label = 1 IV bag/syringe) shall be counted. The number of LABELS for all DATES within the reporting period shall be totaled, and the total number of IV bags/syringes recycled shall be transmitted. If there are no LABELS to be counted for the reporting period, a value of “0” shall be transmitted.
- *Number of IV Bags/Syringes Destroyed*: If the DAILY USAGE is set to “Yes”, the ACTION is set to “Destroyed”, and the DATE is within the reporting period, the number of LABELS (1 label = 1 IV bag/syringe) shall be counted. The number of LABELS for all DATES within the reporting period shall be totaled, and the total number of IV bags/syringes destroyed shall be transmitted. If there are no LABELS to be counted for the reporting period, a value of “0” shall be transmitted.
- *Number of IV Bags/Syringes Canceled*: If the DAILY USAGE is set to “Yes”, the ACTION is set to “Canceled”, and the DATE is within the reporting period, the number of LABELS (1 label = 1 IV bag/syringe) shall be counted. The number of LABELS for all DATES within the reporting period shall be totaled, and the total number of IV bags/syringes canceled shall be transmitted. If there are no LABELS to be counted for the reporting period, a value of “0” shall be transmitted.
- *Units Dispensed*: An IV record will usually have at least one additive and one solution. The number of units dispensed for each IV Additive or solution shall be calculated as described below.
  - IV Additive – The total units dispensed for an IV Additive shall be calculated using the following formula:

Total Units Dispensed (IV Additive) = Number of IV bags/syringes dispensed\* Strength of the IV Additive (Truncate strength units).

> Example: If 10 IV bags were dispensed for Cefazolin 1GM (strength=1GM, the total units dispensed would equal 10 (10\*1).

- IV Solution – The total units dispensed for an IV Solution shall be transmitted. The total shall be calculated using the following formula:

Total Units Dispensed (IV Solution) = Number of IV bags/syringes dispensed \* Volume of IV Solution (Truncate “ML” units).

Example: If 10 IV bags were dispensed for 5% Dextrose 50ML (volume = 50ML), the total units dispensed would equal 500 (10\*50).

- *Units Recycled*: An IV record will usually have at least one additive and one solution. The number of units recycled for each IV Additive or solution shall be calculated as described below.
  - IV Additive – The total units recycled for an IV Additive shall be calculated using the following formula:

Total Units Recycled (IV Additive) = Number of IV bags/syringes recycled\* Strength of the IV Additive (Truncate strength units).

Example: If 10 IV bags were recycled for Cefazolin 1GM, the total units recycled would equal 10 (10\*1).

- IV Solution – The total units recycled for an IV Solution shall be transmitted. The total shall be calculated using the following formula:

Total Units Recycled (IV Solution) = Number of IV bags/syringes recycled \* Volume of IV Solution (Truncate “ML” units).

Example: If 10 IV bags were recycled for 5% Dextrose 50ML, the total units recycled would equal 500 (10\*50).

- *Units Destroyed*: An IV record will usually have at least one additive and one solution. The number of units destroyed for each IV Additive or IV Solution shall be calculated as described below.
  - IV Additive – The total units destroyed for an IV Additive shall be calculated using the following formula:

Total Units Destroyed (IV Additive) = Number of IV bags/syringes destroyed \* Strength of the IV Additive (Truncate strength units).

Example: If 10 IV bags were destroyed for Cefazolin 1GM, the total units destroyed would equal 10 (10\*1).

- IV Solution – The total units destroyed for an IV Solution shall be transmitted. The total shall be calculated using the following formula:

Total Units Destroyed (IV Solution) = Number of IV bags/syringes destroyed \* Volume of IV Solution (Truncate “ML” units).

Example: If 10 IV bags were destroyed for 5% Dextrose 50ML, the total units destroyed would equal 500 (10\*50).

- *  
  Units Canceled*: An IV record will usually have at least one additive and one solution. The number of units canceled for each IV Additive or solution shall be calculated as described below.
  - IV Additive – The total units canceled for an IV Additive shall be calculated using the following formula:

Total Units canceled (IV Additive) = Number of IV bags/syringes canceled \* Strength of the IV Additive (Truncate strength units).

Example: If 10 IV bags were canceled for Cefazolin 1GM, the total units canceled would equal 10 (10\*1).

- IV Solution – The total units canceled for an IV Solution shall be transmitted. The total shall be calculated using the following formula:

Total Units Canceled (IV Solution) = Number of IV bags/syringes canceled \* Volume of IV Solution (Truncate “ML” units).

Example: If 10 IV bags were canceled for 5% Dextrose 50ML, the total units canceled would equal 500 (10\*50).

UD Extract

The following new data elements were added to the UD extract.

- *Total Dispensed Amount*: If the How sub-field (#.05) is set to “1” from Pick list, “2” Pre-exchange units, or “3” Extra Units dispensed, and the dispense date/time is within the reporting period, the AMOUNT sub-field (#.03) for each dispense drug shall be counted. The dispensed amount for all dispense date/time within the reporting period for each dispense drug shall be added in order to calculate the total dispensed amount. The total dispensed amount shall be transmitted. If there is no amount to be counted for the reporting period, a value of “0” shall be transmitted.
- *Total Returned Amount*: If the How sub-field (#.05) is set to “4” returns and the dispense date/time is within the reporting period, the returned AMOUNT sub-field (#.03) for each dispense drug shall be counted. The returned amount for all dispense date/times within the reporting period for each dispense drug shall be totaled, and the total returned amount shall be transmitted. If there is no returned amount to be counted for the reporting period, a value of “0” shall be transmitted.

  
AR/WS Stats Extract

The AR/WS Stats extract was modified to provide a means to break down all AR/WS Stats dispensing workload by Division or Outpatient Site. This is accomplished through the new *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] option, which is described in a previous section of this document and in the PBM V. 4.0 User Manual.

<u>New Data Elements</u>

The two data elements described below were added to the AR/WS Stats extract.

*Total Quantity Dispensed*: If the CATEGORY sub-field (#.01) is set to ‘Automatic Replenishment’ or ‘Ward Stock’, the quantity dispensed shall be counted for each dispense drug. The sum of all quantities dispensed shall be transmitted as the Total Quantity Dispensed data element.

*Total Quantity Returned*: If the CATEGORY sub-field (#.01) is set to ‘Returns – Auto Replenished’ or ‘Returns – Ward Stocked’ the quantity returned shall be counted for each dispense drug. The sum of all quantities returned shall be transmitted as the Total Quantity Returned data element.

<u>Modified Data Elements</u>

One data element was modified within the AR/WS Stats extract. The Sender (facility number) shall be based on the Medical Center Division or the Outpatient Site that the Area of Use is mapped to. The ability to map Area of Uses to a specific Medical Center Division or Outpatient Site is provided by the new *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] option.

The software shall check if the Area of Use is mapped to either a Medical Center Division or Outpatient Site. If the Area of Use is not mapped, the dispensing data shall be attributed to the main facility where the database resides.

  
Prescription Extract

The Prescription extract was modified to no longer extract the Dosing Instructions (SIG). A null value shall be sent in piece 21 of the prescription record.

The following new data elements were added to the Prescription extract:

- *Finishing Person*: The Internal Entry Number (IEN) of the pharmacist who finished the outpatient medication order shall be extracted. The IEN shall be appended to the facility station number and transmitted as a single data element. The facility station number is currently transmitted in the second piece of the prescription record.
- *CMOP ID*: The Consolidated Mail Outpatient Pharmacy (CMOP) identification for the drug extracted. If a drug is not matched to a VA Product or if a CMOP identification is not assigned for the VA Product to which the drug is matched, a null value shall be transmitted.
- *Clinic of Origin*: The location of the clinic associated with the prescription. If no clinic exists for the prescription, a null value shall be transmitted.
- *Login Date of Fill*: The date/time the prescription fill was entered into the system.
- *Copay Status*: The copay eligibility of a prescription.
- *Expanded Patient Instructions*: Expanded patient instructions to accommodate longer and more detailed instructions for the patient. If no patient instructions exist, a null value shall be transmitted.
- *MultiDose Indicator*: For a complex prescription record, the following data elements that comprise the dosing sequence will repeat.
- Dosage Ordered
- Dispense Units Per Dose
- Units
- Noun
- Duration
- Conjunction
- Route
- Schedule
- Verb

If a prescription record contains more than one dosing sequence, an ‘M’ shall be transmitted to flag the prescription record as having multiple dosing sequences. If only one dosing sequence exists a null value shall be transmitted.

- *Dosage Ordered*: The dosage ordered for the prescription drug.
- *Dispense Units Per Dose*: The dispense units per dose for the prescription drug.
- *Unit*: The unit associated with the dosage ordered.
- *Noun*: The Noun associated with the prescription drug. If no value exists, a null value shall be transmitted.
- *Duration*: The length of time that a medication should be given. If no duration exists a null value shall be transmitted. Duration may be entered in minutes, hours, days, weeks, or months. The internal format of the data shall be extracted; for example, “14D or 14” represents “14 days”, “1W” represents “1 week”.
- *Conjunction*: The conjunction for a complex dose. If no conjunction exists, a null value shall be transmitted. The internal format of the data shall be extracted; for example, “A” for “And”, “T” for “Then”, and “X” for “Except”.
- *Route*: How the medication is to be administered.
- *Schedule*: How often the medication is to be taken.
- *Verb*: Helps to describe how the medication should be taken. If no value is found, a null value shall be transmitted.
- *Rx – Multiple Dosing Sequence*: For prescription records, that have more than one dosing sequence, the prescription record shall be transmitted twice. The prescription record with the first dosing sequence shall ONLY be sent in the current ‘PBMOP’ MailMan message. The prescription record in its entirety, with all dosing sequences shall be transmitted in a new ‘PBMOP(MULTIDOSE)’ MailMan message.

Procurement Extract

The Procurement extract was modified to provide a means to break down all Procurement dispensing workload by Division or Outpatient Site. This is accomplished through the new *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] option, which is described in a previous section of this document and in the PBM V. 4.0 User Manual.

CS Extract

The CS extract was modified to provide a means to break down all CS dispensing workload by Division or Outpatient Site. These modifications are described below.

- *Facility Number (Sender)*: The facility number (sender) shall be based on the Medical Center Division or Outpatient Site that the Narcotic Area of Use is mapped to. The ability to map Narcotic Area of Uses to a specific Medical Center Division or Outpatient Site is provided by the new *Map Pharmacy Locations* \[PSU MAP PHARMACY LOCATIONS\] option.
- *Unmapped Narcotic Area of Use*: The software shall check if the Narcotic Area of Use is mapped to either a Medical Center Division or Outpatient Site. If the Narcotic Area of Use is not mapped, the dispensing data shall be attributed to the main facility where the database resides.

<span id="_Toc107123917" class="anchor"></span>

## Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following describes modifications made to options during the PBM Enhancements project.

### Phase I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following modifications were made with the release of PSU\*3\*19 and have been used in the field for the past two years.

The Description within the *Manual Pharmacy Statistics* \[PSU PBM MANUAL\] and *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] options were modified to include the following new extracts and the primary files from which the data is extracted:

- Patient Demographics
- Outpatient Visits
- Inpatient PTF Record
- Provider Data
- Laboratory

### Phase II

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the release of PBM V. 4.0, the following options were modified.

The Description within the *Pharmacy Background Job Check* \[PSU PBM JOB CHECK\] option was modified to adjust the number of days from six (6) to three (3) for a report to complete.

Example:

A MailMan message will be sent to the local PSU PBM mail group and to the National PBM group at Hines if the report has not completed in 3 days.

The *Automatic Pharmacy Statistics* \[PSU PBM AUTO\] option was modified for the Patient Demographics extract. It now considers only new or modified patient data for the last month, which decreases extraction time.

## Modified Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No fields were modified during the PBM Enhancement project.

## Modified Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No reports were modified as a result of the enhancements described in this document. However, the Statistical Data Summary report has been eliminated from the IV, UD, AR/WS Stats, and CS extracts and replaced with the AMIS Summary Report.

<span id="_Toc107123920" class="anchor"></span>

# New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Phase II of the PBM Enhancements project provides the user with the following added functionality:

- Ability to generate a detailed MailMan message without having to transmit to the PBM national database at Hines.
- Decreased extraction times by collecting patient demographic data in real time.
- Ability to retransmit the Patient Demographics extract for a month or a date range up to yesterday minus 75 days.

# Impact on Other VistA Software Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The enhancements described in this document did not have any impact on other VistA software packages.

*(This page included for two-sided copying.)*