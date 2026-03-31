---
title: PSJ*5*111 Release Notes-IMO/IMR-Phase II
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: IMO/IMR-Phase II
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*111
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: To install the necessary patches, you must install the Computerized Patient Record System (CPRS) V. 1.0 GUI V. 25 multi-package build, following its installation instructions.
audience: 
keywords: 
  - inpatient
  - order
  - medication
  - orders
  - clinic
  - medications
  - cprs
  - table
  - contents
  - outpatients
page_count: 0
word_count: 2742
section_count: 8
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p111_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p111_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

> ![](psj-5-111-release-notes-imo-imr-phase-ii/001.png)

Inpatient Medication Orders for OutpatientsandInpatient Medication Reqs for SFG IRA – Phase II

####### RELEASE NOTES 

OR\*3\*195 (with GUI V. 25)

PSS\*1\*59

PSJ\*5\*111

January 2005

V*IST*A Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [Inpatient Medication Orders for Outpatients](#inpatient-medication-orders-for-outpatients)
  - [Inpatient Medications V. 5.0](#inpatient-medications-v-50)
  - [Order Entry Results Reporting V. 3.0 (CPRS)](#order-entry-results-reporting-v-30-cprs)
  - [Scheduling V. 5.3](#scheduling-v-53)
- [Inpatient Medication Requirements for SFG IRA – Phase II](#inpatient-medication-requirements-for-sfg-ira-phase-ii)
  - [Inpatient Medications V. 5.0 and Pharmacy Data Management V. 1.0](#inpatient-medications-v-50-and-pharmacy-data-management-v-10)
  - [Order Entry Results Reporting V. 3.0 (CPRS)](#order-entry-results-reporting-v-30-cprs-1)
- [Installation](#installation)
  - [Overview](#overview)
  - [Post-Installation Setup](#post-installation-setup)
This document provides a brief description of the new features and functions of the Inpatient Medication Orders for Outpatients and the Inpatient Medication Requirements for SFG IRA – Phase II projects. These projects consist of multiple patches, which must be installed for the functionality to perform.
This product shall run on standard hardware platforms used by the Department of Veterans Affairs (VA) Healthcare facilities. These systems consist of standard or upgraded Alpha AXP clusters and run VMS DSM, or Cache VMS.
The following software must be running to support the enhancements requested:
- Kernel V. 8.0
- VA FileMan V. 22.0
- MailMan V. 8.0
- Inpatient Medications V. 5.0
- Scheduling V. 5.3
- Order Entry Results Reporting V. 3.0 (CPRS)
- Bar Code Medication Administration V. 3.0 (BCMA)
![](psj-5-111-release-notes-imo-imr-phase-ii/002.png)Note: PSI-03-060 "IV Fluid Dialog" has been addressed in CPRS GUI V. 25 by adding a new field "Duration or Total Volume" to the IV dialog per the CPRS Clinical Workgroup recommendation. By using this field, a user can specify administrative duration or total volume for the IV order. This new field, when utilized as a duration, however, will override the IV Room site parameter LVP'S GOOD FOR HOW MANY DAYS, as well as any other time restrictions on Orderable Items. Additional CPRS Clinical and Inpatient Medications Workgroup discussion is necessary to determine a resolution to this issue.
*(This page included for two-sided copying.)*

# Inpatient Medication Orders for Outpatients 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new features, functions, and enhancements of the Inpatient Medication Orders for Outpatients (IMO) are grouped and discussed below. These changes will give the user the ability to order unit dose medications for outpatients. This project consists of multiple patches, which must be installed for the functionality to perform.

- SD\*5.3\*285 (to be released separately at a later date)
- OR\*3\*195 (with GUI V. 25)
- PSS\*1\*59
- PSJ\*5\*111

## Inpatient Medications V. 5.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the functionality required for permitting Inpatient Medication unit dose orders for Outpatients.

New Functionality

<u>Unit Dose Medications</u>

Modifications were made to most Unit Dose Medications options to allow processing of unit dose orders for patients currently in or with an appointment scheduled for a clinic that allows Inpatient Medication orders. The order will be associated with a specific clinic and appointment. However, the order may cover more than one appointment. The existing IV order functionality for Outpatients that are not in a clinic that allows administration of Inpatient Medications for Outpatients will not be affected by this enhancement.

1)  All Inpatient Medications unit dose orders for Outpatients shall sort under the Clinic or Clinic Group for the following options:
    1.  *Non-Verified/Pending Orders – Pending/Non-Verified Order Totals Display*
    2.  *Non-Verified/Pending Orders – Unit Dose Orders Selection Display*
1)  The Patient Information Display screen was modified to add Clinic and Date/Time of Appointment. Only those appointments with a clinic that allows administration of Inpatient Medications will be displayed.
2)  The software was modified to allow an Inpatient Medications unit dose non-verified order for an outpatient to be selected, finished, accepted and verified via the following options:
    1.  *Non-Verified Orders*
    2.  *Inpatient Order Entry  
        *
3)  The clinic and appointment date and time that the order is associated with will be stored in the PHARMACY PATIENT file (#55) for both unit dose and IV orders.
4)  Modifications were made to specific Reports on the Reports Menu that will allow sorting and reporting for patients that are currently in or with an appointment scheduled for a clinic that allows administration of Inpatient Medication orders for Outpatients. The following options were modified to allow selection by the Ward Group ^OTHER or to select Outpatients:
    1.  *Inpatient Profile*
    2.  *Action Profile \#1*
    3.  *Medications Due Worksheet*
    4.  *Patient Profile Extended*
5)  Modifications were made to specific Reports on the Reports Menu that will allow sorting and reporting by Clinic and Clinic Group for patients that are currently in or with an appointment scheduled for a clinic that allows administration of Inpatient Medication orders for Outpatients. The following options were modified:
    1.  *Action Profile \#2*
    2.  *Patient Profile (Unit Dose)*
    3.  *Inpatient Stop Order Notices*
    4.  *Label Print/Reprint*
6)  The Medication Administration Record (MAR) reports were modified in the following ways:
    1.  Allow selection of Clinic and Clinic Group, to include Outpatients with Inpatient Medication orders.
    2.  Leave the Room/Bed blank when printing Outpatients.
    3.  Change the ‘Ward’ to ‘Loc’.
    4.  Print Ward for Loc for Inpatients and hospital location for Loc for Outpatients.
7)  Messaging between CPRS and Inpatient Medications has been changed to include the appointment date/time for Inpatient Medication orders for Outpatients that are associated with a clinic appointment.
8)  A new option has been added to allow the definition of clinic stop date calculations for hospital locations that allow administration of Inpatient Medications for Outpatients. The new option is: *Clinic Stop Dates,* under the PSJU MGR menu. If no stop date has been defined and an order is placed, the system uses 14 days as the default calculation.

## Order Entry Results Reporting V. 3.0 (CPRS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the functionality that CPRS now provides to permit an ordering provider to enter an Inpatient Medication (unit dose) order for any Outpatient in an authorized HOSPITAL LOCATION file (#44) as established by the Location for Current Activities.

New Functionality

CPRS was modified to present the user with the Inpatient Medication Order Dialog in conjunction with the Inpatient Orderable Item Medication list when an order is placed for an Outpatient from an authorized Hospital Location.

When a user selects the Inpatient Medication Order action in a Hospital Location that is not authorized, they shall continue to be presented with the IV Medication Orderable Item list. If an IV Medication order needs to be placed for an Outpatient from an authorized clinic, sites that have not added the IV Medications list to the Write Order list will need to do so.

Inpatient Medication (unit-dose) orders are permitted for Outpatients when the following conditions are met:

- The patient has a status of *Outpatient.*
- The patient has an appointment on the current day, or a day in the future, in an authorized Hospital Location.
- The unit dose order is being placed against an authorized Hospital Location.
- The order is placed from the CPRS Orders Tab or the CPRS Meds Tab when the parameter ORWDX is set with a menu pointing to the Inpatient Medication order dialog.

The system was modified to permit Inpatient Medication orders to be placed for patients in an authorized clinic, without a scheduled appointment, when the visit is concurrent with placement of the order. This permission allows designated Hospital Locations, such as the Emergency Room, to submit Inpatient orders in the absence of a scheduled appointment in an authorized clinic.

Inpatient Medication orders written for outpatients have the status of inpatient orders. They are:

- Filled by Inpatient Pharmacy
- Dispensed by Inpatient Pharmacy
- Displayed in CPRS as inpatient orders

CPRS continues to apply all existing medication order checks to the Inpatient Medication orders written for Outpatients.  
Providers are permitted to use Personal Quick Orders to submit orders from the Inpatient Medication Orderable Item list when such orders are congruent with the patient’s appointment in an authorized Hospital location. Medication quick orders that have been created and placed on site-defined order menus shall perform according to existing functionality.

Users shall continue to be permitted to define the date range of appointments listed in the Location for Current Activities box with the appointments/visits conforming to the API ORWCV VST.

Modified and New Routines

<u>ORWDX (Modified)</u>

Before saving the Inpatient Medication Order for an Outpatient (IMO), the routine will run an internal check to see if it is an IMO order. If true, the display group will be set to inpatient display group. The order will be saved with the appointment data.

<u>ORMBLD (New)</u>

Previously, the Health Level Seven (HL7) message of Inpatient Medication order was passed to the Inpatient Medications package from CPRS side without the scheduled appointment data. The HL7 message of Inpatient Medication order shall now include the appointment data along with the order’s data.

<u>ORWDXA (New)</u>

When any of the copy, change, and renew actions are being taken on IMO orders, the validation routine shall check the authorization of the hospital location. If it is an authorized location, the action can proceed, otherwise, action shall be denied.

CPRS Modifications for Inpatient Medications Interface

CPRS shall pass to the Inpatient Medication (IPM) the IEN of the HOSPITAL LOCATION file (#44) from which the medication orders are being written and the appointment the order is being written against. CPRS shall use the existing HL7 messaging with IPM.

CPRS Requirements for Post-Entry Action

IMO orders are eligible for post-entry actions when the order-action is submitted against an appointment/visit in an authorized clinic on the current day or in the future. The following actions are permitted:

- Change
- Copy to New Order
- Renew

The system was modified to display warning dialogs if a user attempts a post-entry edit action on an existing IMO order from an unauthorized clinic or if the action is not permitted.

## Scheduling V. 5.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the functionality that Scheduling will provide to define Inpatient Medications orders in the HOSPITAL LOCATION file (#44) and in the API, which will return the necessary information to CPRS to process an order.

![](psj-5-111-release-notes-imo-imr-phase-ii/003.png)Note: SD\*3\*285 will not be released at this time. It is scheduled to be released after CPRS GUI V. 25, but prior to March 1, 2005.

New Functionality

The HOSPITAL LOCATION file (#44) was modified to add the ADMINISTER INPATIENT MEDS? field (#2802). Valid values are YES and null. A YES value indicates that the clinic is authorized to dispense Inpatient Medications to Outpatients. This field is editable to allow a YES to be deleted.

The *Set-up a Clinic* option was modified to include a prompt for the new ADMINISTER INPATIENT MEDS? field (#2802).

A new *Inpatient Medications to Clinic* option was added, which enables Non-Scheduling users to modify the values of the ADMINISTER INPATIENT MEDS? field (#2802) outside of the *Set-up a Clinic* option. This option allows the user to select the clinic in the HOSPITAL LOCATION NAME field (#.01) and enter YES to designate the clinic is authorized to dispense Inpatient Medications to Outpatients in the ADMINISTER INPATIENT MEDS?” field (#2802).

Scheduling provides an API to return the date/time of a scheduled appointment or checked-in visit in an authorized clinic for a selected patient. The date/time of the checked-in visit shall be not less than <today@.0001> and not greater than [today @2359](mailto:today@2359). Appointments scheduled for the current day or a day in the future are allowed regardless of check-in status.

  
<span id="_Toc91412028" class="anchor"></span>*(This page included for two-sided copying.)*

# Inpatient Medication Requirements for SFG IRA – Phase II 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a brief description of the new features, functions, and enhancements of the Inpatient Medication Requirements for SFG IRA – Phase II project. This project consists of multiple patches, which must be installed for the functionality to perform.

- OR\*3\*195 (with GUI V. 25)
- PSS\*1\*59
- PSJ\*5\*111

## Inpatient Medications V. 5.0 and Pharmacy Data Management V. 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Medications Requirements for the Special Focus Group IRA – Phase II project will prevent users from entering free-text schedules for inpatient medication orders. This change was requested for patient safety purposes. There have been problems with the calculation of the correct frequency for schedules that are entered as free-text. The best example is the schedule “EVERY NIGHT”. A person can interpret this easily. However, using pattern matching logic, the only character that is recognized is the letter ‘H’, which would indicate an ‘hourly’ schedule, rather than the once-a-day that is being requested.

For the purposes of this project a valid schedule must meet one of the following conditions:

- Defined in the ADMINISTRATION SCHEDULE file (#51.1)
- Contain PRN, if the rest of the schedule is in the ADMINISTRATION SCHEDULE file (#51.1), i.e., Q4H PRN, where Q4H is in 51.1.
- Day-of-Week or <Day-of-Week@admin> time schedule
- Admin-time only schedule format

The patch PSS\*1\*59 helps accomplish this by changing the validation of schedules entered through Computerized Patient Record System (CPRS) V. 1.0. This validation requires that schedule meet the valid schedule guidelines above. In addition, this patch modifies the definition of schedules in the ADMINISTRATION SCHEDULE file (#51.1). To accomplish this, the following changes are being made to the PSSJ SCHEDULE EDIT input template:

- Do not allow entry of a schedule with the name of “OTHER”.
- Do not allow entry of administration times for odd schedules.
- Display the calculated frequency to the user.

Based on the upcoming requirement from the Joint Commission on Accreditation of Hospital Organizations, schedule names that are considered dangerous will no longer be allowed. The four schedules that will no longer be allowed are: QD, HS, TIW and QOD. These schedules cannot be used either alone or as part of a schedule name. For example: QD is not allowed. Neither is QD ONCE.

The Inpatient Medications patch PSJ\*5\*111 helps accomplish the goals of the Inpatient Medications Requirements for the Special Focus Group IRA – Phase II project by ensuring that no order will be allowed to become active if the schedule does not meet the guideline outlined above.

![](psj-5-111-release-notes-imo-imr-phase-ii/004.png)Note: No changes are forced for currently active orders. However, when an action other than discontinue is taken on the order, the software will require the user to select a schedule that meets the valid schedule conditions listed above.

## Order Entry Results Reporting V. 3.0 (CPRS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When placing inpatient medication orders, users can no longer enter free-text schedules. Instead, users must select standard schedules from the Schedule list box or select “OTHER” from the Schedule list box to create a customized day-of-week or admin/time schedule. If users try to copy, transfer, or renew inpatient medication orders, CPRS allows only orders with valid schedules to proceed.

![](psj-5-111-release-notes-imo-imr-phase-ii/005.png)Note: If the user selects “OTHER” to create a customized schedule, the order may require that the pharmacist and the physician work out a valid schedule, which might delay the order becoming active. The parameter ORWIM NSS MESSAGE enables sites to customize the message in the text box on the Order with Schedule “OTHER” dialog to inform providers that a delay may be caused or give instructions. A default message appears in the text box if the site does not enter one.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install the necessary patches, you must install the Computerized Patient Record System (CPRS) V. 1.0 GUI V. 25 multi-package build, following its installation instructions.

## Post-Installation Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you are ready to implement Inpatient Medication Orders for Outpatients, you will need to perform the following setup actions.

#### CPRS V. 1.0 

You will need to add the Clinic Medications display group. Please refer to the CPRS V. 1.0 GUI V. 25 Release Notes (OR_30_195RN.PDF) for detailed instructions on adding the Clinic Medications display group.

#### Scheduling V. 5.3 

Use the *Set-up a Clinic* option or the *Inpatient Medications To Clinic* option to mark the appropriate HOSPITAL LOCATIONS as able to administer inpatient medications.

*(This page included for two-sided copying.)*

#