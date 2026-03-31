---
title: PSB*3*70 BCMA Clinic Orders, High Risk, etc T@Project Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: BCMA Clinic Orders, High Risk, etc T@Project
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3*70
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 0
description: This document provides a feature summary of the Clinic Orders for BCMA functionality and Witness for High Risk/High Alert Drugs for Bar Code Medication Administration (BCMA) v3.0 project, patch PSB\3\70.
audience: 
keywords: 
  - clinic
  - orders
  - witness
  - high
  - bcma
  - table
  - contents
  - risk
  - order
  - medication
page_count: 0
word_count: 8725
section_count: 10
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p70_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p70_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

> ![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/001.png)

Clinic Orders and Witness for High Risk/High Alert Drugs for BCMA v3.0

####### RELEASE NOTES

PSB\*3\*70

December 2013

Product Development (PD)

Table of Contents

# Clinic Orders


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Clinic Orders](#clinic-orders)
- [Introduction](#introduction)
- [Displaying Clinic Orders in BCMA](#displaying-clinic-orders-in-bcma)
- [Viewing a Patient’s Clinic Order Medications](#viewing-a-patients-clinic-order-medications)
  - [View Menu Option](#view-menu-option)
  - [When Patient Status is: Admitted](#when-patient-status-is-admitted)
  - [When Patient Status is: Not Admitted](#when-patient-status-is-not-admitted)
- [Displaying Clinic Orders on the Cover Sheet](#displaying-clinic-orders-on-the-cover-sheet)
- [Administering Clinic Orders in BCMA](#administering-clinic-orders-in-bcma)
- [BCMA Clinic Order Terminology](#bcma-clinic-order-terminology)
- [Display Alerts](#display-alerts)
- [Process for Administering Clinic Orders in BCMA](#process-for-administering-clinic-orders-in-bcma)
- [Working with Large Volume IV Clinic Orders](#working-with-large-volume-iv-clinic-orders)
- [Last Action and PRN/Effectiveness for Clinic Orders](#last-action-and-prneffectiveness-for-clinic-orders)
- [Meds on Patient Indicators](#meds-on-patient-indicators)
  - [Infusing IV Indicator](#infusing-iv-indicator)
  - [Stopped Indicator](#stopped-indicator)
  - [Patches Indicator](#patches-indicator)
  - [No Indicators/Multiple Indicators](#no-indicatorsmultiple-indicators)
- [Patch Administrations Expired or Discontinued](#patch-administrations-expired-or-discontinued)
- [Viewing and Printing Clinic Order Reports](#viewing-and-printing-clinic-order-reports)
  - [Mutually Exclusive Reports](#mutually-exclusive-reports)
  - [Combined Reports](#combined-reports)
    - [MAH Report](#mah-report)
    - [Med Log Report](#med-log-report)
- [Mutually Exclusive Reports – Select Clinics Functionality](#mutually-exclusive-reports-select-clinics-functionality)
- [BCMA Missing Dose Request Parameter for Clinic Orders](#bcma-missing-dose-request-parameter-for-clinic-orders)
- [Additional Information](#additional-information)
- [Witness for High Risk/High Alert Drugs](#witness-for-high-riskhigh-alert-drugs)
- [Introduction](#introduction-1)
- [Defining High Risk/High Alert Medications](#defining-high-riskhigh-alert-medications)
- [New Icon Added to Icon Legend](#new-icon-added-to-icon-legend)
- [“Wit” Column Added to the VDL](#wit-column-added-to-the-vdl)
- [BCMA Witness Sign-on Dialog](#bcma-witness-sign-on-dialog)
- [Witnessing High Risk/High Alert Drugs When a Witness is Required](#witnessing-high-riskhigh-alert-drugs-when-a-witness-is-required)
- [Witnessing High Risk/High Alert Drugs When a Witness is Recommended and Witness is Provided](#witnessing-high-riskhigh-alert-drugs-when-a-witness-is-recommended-and-witness-is-provided)
- [Witnessing High Risk/High Alert Drugs When a Witness is Recommended and No Witness is Provided](#witnessing-high-riskhigh-alert-drugs-when-a-witness-is-recommended-and-no-witness-is-provided)
- [Error Messages for Witness Validation](#error-messages-for-witness-validation)
- [Witness Information Stored in Medication Log](#witness-information-stored-in-medication-log)
- [User Documentation](#user-documentation)
- [Associated Files and Fields](#associated-files-and-fields)
- [Associated Forms](#associated-forms)
- [Associated Options](#associated-options)
- [Parameter Definitions](#parameter-definitions)
- [Associated Remote Procedure Calls](#associated-remote-procedure-calls)
- [Associated Security Keys](#associated-security-keys)
- [Associated Templates](#associated-templates)
- [Patient Safety Issue Corrections](#patient-safety-issue-corrections)
- [Remedy Tickets Resolved](#remedy-tickets-resolved)
- [New Service Requests (NSRs) Resolved](#new-service-requests-nsrs-resolved)
- [BCMA Online Help Update](#bcma-online-help-update)
- [Installation Details](#installation-details)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document provides a feature summary of the Clinic Orders for BCMA functionality and Witness for High Risk/High Alert Drugs for Bar Code Medication Administration (BCMA) v3.0 project, patch PSB\*3\*70.

­­­­­­­­­­­­­

Installation instructions for PSB\*3\*70 are included in the patch description and the Installation Guide.

The following patches are associated and must be installed before PSB\*3\*70:

- PSB\*3\*54
- PSB\*3\*64
- PSB\*3\*66
- PSJ\*5\*279
- PSB\*3\*74

Highlights

- Clinic orders display on the Cover Sheet, Unit Dose, Intravenous Push (IVP)/Intravenous Piggy Back (IVPB) and Intravenous (IV) tabs.
- Choice of order modes – Inpatient or Clinic, and both order modes are available in Read Only as well as Limited Access BCMA.
- Indicator displays next to the Inpatient order mode, showing green when active Inpatient orders exist for the patient and/or there are discontinued/expired Inpatient orders on which action can be taken or white when no active Inpatient orders exist and there are no discontinued/expired orders in Inpatient order mode on which action can be taken.
- Indicator displays next to the Clinic order mode, showing green when active Clinic orders exist for the patient and/or there are discontinued/expired Clinic orders on which action can be taken or white when no active Clinic orders exist and there are no discontinued/expired orders, in Clinic order mode on which action can be taken.
- Clinic Order Date area replaces the Virtual Due List (VDL) Parameters area when the Clinic order mode is selected.
- When Clinic order mode is selected, clinic medication orders display on all medication tabs including the Cover Sheet.
- New “Clinic” column, displaying the clinic name, added on all mediation tabs including the Cover Sheet, when Clinic order mode is selected.
- Ability to view and administer clinic medications that are due each day and to see active clinic orders that were due prior to today and after today.
- Ability to see all IV orders that have been infused, whether infused in an Inpatient ward or clinic.
- Ability to see Clinic order IV bags that have not been completed until marked as completed.
- Last Action column updated on Unit Dose and IVP/IVPB tabs to reflect action taken and date/time of action, whether in an Inpatient ward or in a Clinic.
- Ability to see on the Pro Re Nata (PRN) Med Log dialog, all pending PRN administrations that need effectiveness documentation, whether given in an Inpatient ward or in a Clinic.
- Last Given calculation and date updated on the PRN medication log dialog reflects the last date/time the orderable item was given and the elapsed time since it was last given, whether in an Inpatient ward or in a Clinic.
- All pending PRN Effectiveness entries, along with the Location given, displayed in the PRN Medication Log dialog, whether the PRN med was originally given in an Inpatient ward or in a Clinic.
- New indicators display on the VDL when the patient has any Infusing IV’s, Stopped IV’s, and Patches that are not removed.
- CPRS Med Order Button (CMOB) disabled for Clinic Order mode, whether the patient is admitted or not. CMOB is also disabled when in Inpatient order mode, when the patient is not admitted (not assigned to room/bed).
- BCMA Splash Screen Text revised to agree with Clinical Product Support (CPS).
- Character-based User Interface (CHUI) reports for Ward Administration Times, Due List and Missed Medications will include Inpatient data only.
- PSB Missing Dose Request option removed from Manager, Pharmacist and Nurse CHUI menus.

Clinic Order Reports

- Mutually exclusive reports (GUI) which separate Inpatient data from Clinic order data are available. These include the Admin Times, Due List, Missed Meds and Cover Sheet reports. Reports are available for one or more clinics.
- Combined reports which include both Inpatient data and Clinic order data are available. These include the Medication Admin History (MAH), Med Log, Med History, IV Bag Status, Med Therapy and PRN Effectiveness reports.

BCMA Site Parameters Application Updated

- Added field in the BCMA Parameters application for a division Clinic Missing Dose Request Printer.

BCMA Supports Scanning of Veterans Health Information Card (VHIC)

- BCMA supports scanning of the patient wristband (SSN), the legacy VIC card (SSN), the pilot card (new VIC#), the interim VHIC (SSN), and the final VHIC card (new VIC#). BCMA does not support the Magnetic Stripe input from the new VHIC card.

BCMA Online Help System Updated

- The Online Help system has been updated for BCMA to include Clinic Orders and Witness for High Risk/High Alert administrations.

NOTE*:* In current-state Computerized Patient Record System (CPRS), providers must use the Inpatient Medication and Infusion ordering dialogs to place clinic orders. The capability to write clinic orders for patients with a status of “Inpatient” does not exist. Clinic orders can only be written on a patient with a status of “Outpatient” in current-state CPRS.When CPRS, V30, is implemented, a provider will be able to write Clinic Orders for both Inpatients and Outpatients.

# Displaying Clinic Orders in BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA displays clinic orders on the Cover Sheet, Unit Dose, IVP/IVPB and IV tabs. The user may select between two mutually exclusive “Order Modes.” The following Inpatient/Clinic Order Mode Indicators Table explains the possible display combinations.

Inpatient/Clinic Order Mode Indicators Table

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/002.png)

> **NOTE:** Orders associated with outpatient clinics, that are not technically “Clinic Orders,” will display in the Inpatient Order Mode in BCMA. Clinic Orders display within the Clinic Order Service in the Orders tab in CPRS.

# Viewing a Patient’s Clinic Order Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## View Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The view menu option provides a quick way to select between Inpatient or Clinic order mode.

Example: View Menu Option

> ![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/003.png)

> User may select the following new shortcut keys to switch between Inpatient or Clinic order mode:

- F2 Inpatient Order Mode
- F3 Clinic Order Mode

## When Patient Status is: Admitted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system selects a default order mode based on the patient admission status, when the patient record is opened. If the patient is admitted to a ward, BCMA selects the Inpatient order mode. An indicator displays next to the Inpatient order mode, showing green, when active inpatient orders exist for the patient and/or an action can be taken on an expired or discontinued order, or white when no active Inpatient orders exist and no action can be taken on an expired or discontinued Inpatient order.

> When the Inpatient order mode is selected, the Order Mode indicator shows Inpatient orders exist, and the Virtual Due List Parameters section displays.

Example: Inpatient Mode Selected

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/004.png)

> When the Inpatient order mode is selected, Inpatient medication orders, only, display on the Cover Sheet, Unit Dose, IVP/IVPB and IV tabs.

## When Patient Status is: Not Admitted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system selects a default order mode based on the patient admission status, when the patient record is opened. If the patient status is not admitted, the system defaults to the Clinic order mode. An indicator displays next to the Clinic order mode, showing green when active clinic orders exist for the patient and/or action can be taken on an expired or discontinued order or white when no active clinic orders exist and no action can be taken on expired/discontinued Clinic orders.

> When the Clinic order mode is selected, the Order Mode indicator shows clinic orders exist, and the Clinic Order Date area replaces the Virtual Due List Parameters area on the screen.

> Only clinic medication orders display on the Cover Sheet, Unit Dose, IVP/IVPB and IV tabs. The clinic order date defaults to Today’s date regardless of whether there are active orders to be administered today.

Example: Clinic Mode Selected

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/005.png)

> In the Clinic order mode, the column entitled “Clinic” displays the clinic name associated with the order on the Cover Sheet, Unit Dose, IVP/IVPB and IV tabs. The HSM column is removed from the Unit Dose tab. “Location” is blank for patients that are not admitted.

Example: Clinic Column

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/006.png)

> **NOTE:** If “AUTO-DC IMO ORDERS?” is set to “Yes” in the CLINIC DEFINITION (#53.46) file when a clinic patient is admitted, Active Unit Dose and IVP/IVPB clinic orders are discontinued, at which point they will not display on the VDL, except for Expired/Discontinued Patch orders that display for the number of days defined by the “Patch Display Duration” parameter or until removed by a nurse.

If “AUTO-DC IMO ORDERS?” is set to “No” in the CLINIC DEFINTION (#53.46) file, when a clinic patient is admitted, Unit Dose and IVP/IVPB clinic orders will remain displayed on the VDL in Clinic Order Mode.

# Displaying Clinic Orders on the Cover Sheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When Clinic order mode is selected, only clinic orders are displayed on the Medication Overview, PRN Overview, IV Overview, and Expired/DC’d/Expiring views of the Cover Sheet.

When Clinic order mode and Cover Sheet are selected, the clinic order date, calendar, navigation arrows, and Today button are disabled.

When Clinic order mode is selected and focus goes from the Cover Sheet back to a medication tab (UD, IVP/IVPB), the Clinic order date field, Today button, and navigation arrows are re-enabled, and the previous date selected is active.

If the user switches from Inpatient to Clinic order mode while on the Cover Sheet tab, the Medication Overview view displays as the initial default view. If the user selects Medication Overview or PRN Overview, orders that have expired or have been discontinued within the last 7 days are displayed in the Expired/DC’d orders section.

Example: Clinic Mode and Cover Sheet  
(Medication Overview)

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/007.png)

If the user selects the Expired/DC’d/Expiring orders view, orders that have expired or have been discontinued within the last 7days are displayed in the Expired/DC’d orders section. Orders expiring within the next 7 days are displayed in the Expiring within next 7 days orders section.

Example: Clinic Mode and Cover Sheet  
(Expired/DC’d/Expiring Orders)

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/008.png)

> **NOTE:** The system ignores the parameters for Allowable Time Limits (Before Scheduled Admin Time and After Scheduled Admin Time) when displaying clinic orders on the cover sheet.

# Administering Clinic Orders in BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can access the BCMA VDL to view and administer clinic medications that are due each day. This includes active clinic orders that were due prior to today so that medications may be administered to a patient who arrives late for an appointment. The user can also see active clinic orders that are due after today, so that medications may be administered to a patient who arrives early for an appointment.

The Clinic Order Date defaults to today’s date, regardless of whether there are active orders to be administered today. If no active clinic orders display on the Unit Dose or the IVP/IVPB tabs for the selected date and/or selected schedule types, the following message displays on the VDL: “There are no administrations to display, based on your current Clinic Order Date and/or Schedule Type selections.”

# BCMA Clinic Order Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following BCMA Clinic Order definitions are only applicable to the BCMA VDL, not the Cover Sheet.

- ACTIVE ORDERS only display in BCMA Clinic order mode, if the order is active relative to TODAY, meaning the Order Start Date must be less than or equal to TODAY, and the Order Stop Date must be greater than or equal to TODAY.
- FUTURE ADMINISTRATIONS only display in BCMA Clinic order mode for an ACTIVE ORDER, as defined above, for a date in the future, only if the schedule and admin time matches the selected Clinic Order Date. User can take an action on a future Administration on an ACTIVE ORDER.
- PAST ADMINISTRATIONS only display in BCMA Clinic order mode for an ACTIVE ORDER, as define above, for a date in the past, only if the schedule and admin time matches the selected Clinic Order Date. User can take an action on a PAST ADMINISTRATION on an ACTIVE ORDER.
- FUTURE ORDERS should never display in BCMA Clinic order mode, since the order start date is greater that TODAY and user cannot take an action on a FUTURE ORDER.

# Display Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following alerts pertain to clinic order administrations and display in the Medication Log dialog prior to administration:

- An alert displays on the Medication Log dialog, requiring a comment, if user attempts to administer a clinic medication on a day other than the scheduled day.
- An alert, “You are about to give a medication that is scheduled for \<Future Date\>” in bold text in the Medication Log dialog message box, if user attempts to administer a clinic medication for a future administration of an active order. A comment is required before user is allowed to continue.
- An alert, “You are about to give a medication that was scheduled for \<Past Date\>” in bold text in the Medication Log dialog message box, if user attempts to administer a clinic medication for a past administration of an active order. A comment is required before user is allowed to continue.
- An alert also displays on the Medication Log dialog, if user attempts to administer a medication (Orderable Item) that was already given within the last 120 minutes, whether the medication was given in Inpatient or Clinic order mode.

> **NOTE:** The parameters for Allowable Time Limits (Before Scheduled Admin Time and After Scheduled Admin Time) are ignored when displaying and administering clinic orders on the VDL, meaning that alerts are not displayed when clinic orders are administered early or late.

# Process for Administering Clinic Orders in BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- In the Clinic Order Date area on the Unit Dose and IVP/IVPB tabs of the BCMA VDL, the user may select a single clinic date to display, using the left and right navigation arrows, or the user may click the drop-down arrow to the right of the date to display the calendar pop-up.
- When the patient record is opened the Clinic Order date defaults to TODAY.

Example: Clinic Order Date Selection

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/009.png)

- A “Today” button allows the user to return to today’s date while in Clinic order mode. The button is enabled when the Clinic Order Date is set to a date other than today’s date, and the user has selected the Unit Dose or IVP/IVPB tab. It is disabled when the Clinic Order Date is set to today’s date.

Example: Clinic Order “Today” Button

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/010.png)

- After a date is selected, all active Clinic Orders for the patient are displayed for a 24 hour period on the selected date (0001 to 2359), based on the clinic order’s start date, stop date, schedule, and admin times.  
    
  Note: Clinic orders, for which the order start date/time is in the future, do not display on the VDL.
- Once a date is selected, and orders that are due are displayed, the administration workflow continues, such that the nurse can scan the medication to be given or use Unable to Scan functionality to administer the medication.
- Actions taken (Status) on non-PRN clinic order administrations on PREVIOUS or FUTURE DATES remain displayed on the VDL, as long as the order is still active, even after refresh.
- After user refreshes, the “Given” status of all PRN clinic orders (administered TODAY, administered on PREVIOUS dates, or administered on FUTURE dates) is cleared.

# Working with Large Volume IV Clinic Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The nurse can see all available IV bags on active IV orders for both Inpatient and Clinic orders to infuse, monitor or take action on the bags as needed.

IV bags on active Clinic orders for bags that have not been completed will display on the VDL until they are marked as completed.

IV bags on Expired/Discontinued Clinic orders that have not been completed will display on the VDL for a maximum of 7 days or until they are marked as completed.

When the user is in the Clinic order mode and selects the IV tab:

- The Clinic Order Date Selection field, navigation arrows, and Today button are disabled, as date selection and navigation are not applicable to large volume IV orders.
- Active IV Clinic orders display based on the order’s start date/time and stop date/time.
- Expired IV Clinic orders no longer display, unless the bag is still infusing or stopped.
- You may complete infusing IV bags on expired orders, regardless of whether they were infused in a Clinic or an Inpatient location.
- Clinic order IV bags only display on Expired/Discontinued IV Clinic orders if an IV bag on the order is Stopped or Infusing for a maximum of 7 days, or until you complete them.
- You may infuse or take action on bags on active IV orders and on Expired/Discontinued IV orders in both Clinic and Inpatient order modes.
- If “AUTO-DC IMO ORDERS?” is set to “Yes” in the CLINIC DEFINITION (#53.46) file, when a Clinic patient is admitted:
  - Active IV Clinic orders are discontinued.
  - Infusing and Stopped IV bags on Expired/Discontinued orders remain displayed in the clinic order mode for a maximum of 7 days, or until you complete them.
- If “AUTO-DC IMO ORDERS?” is set to “No” in the CLINIC DEFINITION (#53.46) file, any existing active IV Clinic orders display in the Clinic order mode.
- If there are no active IV clinic orders, and no action to be taken on Expired/Discontinued IV Clinic orders, the following message displays on the VDL: “There are no administrations to display.”

# Last Action and PRN/Effectiveness for Clinic Orders 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can verify that the last action taken on a particular administration reflects the status and date acted on that medication, whether the action was taken in an inpatient ward or in a clinic.

- The Last Action column on the Unit Dose and IVP/IVPB tabs is updated to reflect the action taken and date/time of the action on that orderable item, whether the action was taken in an inpatient ward or in a clinic.

Example: Last Action Column on VDL

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/011.png)

- The Last Given calculation and date are updated on the PRN Medication Log dialog to reflect the last date/time the orderable item was given and the elapsed time since it was last given, whether last given in an inpatient ward or in a clinic.

Example: Last Given Calculation and Date/time Given on PRN Med Log

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/012.png)

- The user will see the date and time a PRN medication was last given, including the calculation of time elapsed, whether the medication was given in an inpatient ward or in a clinic.
- All pending PRN administrations that need effectiveness documentation, whether given in an inpatient ward or in a clinic, are displayed on the PRN Med Log.
- All pending PRN Effectiveness entries, along with the Location given, are displayed in the PRN Medication Log dialog, whether the PRN med was originally given in an inpatient ward or in a clinic. Ward names and clinic names display in the Location column.

Example: PRN Effectiveness Entries on the PRN  
Medication Log Dialog

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/013.png)

- The Location column, on the PRN Effectiveness Log dialog, is updated to include the Clinic Name that is associated with the orderable item, when administered in a clinic.
- For non-admitted patients with Clinic Orders, the BCMA Clinical Reminders marquee includes up to the last four administrations requiring PRN Effectiveness documentation, and the PRN Effectiveness Log dialog displays PRN administrations requiring effectiveness documentation for a period of 24 hours.
- For admitted patients with Clinic Orders, the BCMA Clinical Reminders marquee includes up to the last four administrations requiring PRN Effectiveness documentation, and the PRN Effectiveness Log dialog displays PRN administrations requiring effectiveness documentation based on the BCMA Site Parameter, PRN Documentation (in hours).
- The Last four PRN Effectiveness entries, under the BCMA Clinic Reminders marquee are updated, whether the PRN medication was originally given in an inpatient ward or in a clinic.

Example: Last Four PRN Effectiveness Entries under  
BCMA Clinical Reminders

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/014.png)

# Meds on Patient Indicators

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three separate indicators display on the VDL to the left of BCMA Clinical Reminders, in a group entitled “Meds on Patient,” when the patient has currently Infusing IV’s, Stopped IV’s, or Patches that are not removed. The indicators are applicable to active Inpatient or Clinic orders of if there is action that can be taken on an active, Expired, and/or Discontinued order.

> **NOTE:** When Meds on Patient Indicators display, the user may need to switch tabs or order modes to find Infusing IVs, Stopped IVs or Patches on which action can be taken.

## Infusing IV Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Infusing IV indicator displays the words “Infusing IV’s” in red bold text, only when there is one or more active, expired, and /or discontinued Infusing IV’s on the patient, in either Clinic or Inpatient order mode.

Example: Infusing IV Indicator

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/015.png)

## Stopped Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Stopped IV indicator displays the words “Stopped IV’s” in red bold text, only when there is one or more active, expired, and/or discontinued Stopped IV’s on the patient, in either Clinic or Inpatient order mode.

Example: Stopped IV Indicator

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/016.png)

## Patches Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patches indicator displays the word “Patches” in red bold text, only when there is one or more active, expired, and/or discontinued patches that are not removed from the patient, in either Clinic or Inpatient order mode.

Example: Patch Indicator

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/017.png)

## No Indicators/Multiple Indicators

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If any of the indicators are applicable, the system displays the “Meds on Patient” group box with a light colored background; otherwise, the box displays no indicators with a gray background.

Example: No Indicators

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/018.png)

> The “Meds on Patients” group box can be blank, or display up to a total of three indicators, when all three conditions are met.

Example: Multiple Indicators

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/019.png)

# Patch Administrations Expired or Discontinued

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can view Clinic patch administrations as well as Inpatient patch administrations that are expired or discontinued on the VDL.

- The system displays both Clinic and Inpatient patch administrations in the “Given Patches that are Expired or Discontinued” popup on the VDL.
- The count (Patch \# of \#) is updated to include the total number of patch administrations in the “Given Patches that are Expired or Discontinued” popup and whether they are Clinic or Inpatient.
- The Location (Ward name or Clinic name) where the patch was administered in the facility is displayed above the medication in the popup. The word “INPATIENT” is displayed for ward based administrations, and the Clinic name is displayed for clinic based administrations in bold uppercase.
- When the user selects “Mark Removed,” the system marks the patch administration “Removed” from the appropriate mode (Clinic or Inpatient).

> **NOTE:** The BCMA site parameter “Patch Display Duration” applies to patches administered in both Inpatient and Clinic order modes. If “AUTO-DC IMO ORDERS?” is set to “Yes” in the CLINIC DEFINITION (#53.46) file, when a Clinic patient is admitted, Expired/Discontinued orders remain displayed in Clinic order mode for the number of days defined by the “Patch Display Duration” parameter, or until removed by a nurse. If “AUTO-DC IMO ORDERS?” is set to “No” in the CLINIC DEFINTION (#53.46) file, when a Clinic patient is admitted, any existing patch orders display in Clinic order mode.

Example: Given Patches Expired  
or Discontinued Popup

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/020.png)

# Viewing and Printing Clinic Order Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A variety of reports displaying Clinic Order data are available.

Some reports separate Inpatient data from Clinic order data. These reports are referred to as “Mutually Exclusive” reports. Other reports always include both Inpatient data and Clinic order data. These reports are referred to as “Combined” reports.

## Mutually Exclusive Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Mutually Exclusive reports include the following:

- Admin Times Report
- Due List Report
- Missed Meds Report
- Cover Sheet Reports

> These reports may be run for either Inpatient or Clinic orders for a single patient. Reports may also be run for Clinic orders, only, for all patients in one or more selected Clinics. BCMA remembers the last mode the user was in, Inpatient or Clinic, so that when the user runs reports, without a patient selected, the correct mode defaults.

> When the Print by “Clinic” option is selected, the user may select one or more clinics to include in the reports. See the “[Mutually Exclusive Reports – Select Clinics Functionality](#mah-report)” section.

> **NOTE:** When including Clinic Orders in the Due List Report and the four Cover Sheet Reports, parameters for Allowable Time Limits (Before Scheduled Admin Time and After Scheduled Admin Time) are ignored.

- If a patient record is open:
- The report dialog Print by selection always defaults to “Patient.”
- If the user selects the “Inpatient” Order Mode on the VDL, the report dialog Include Orders selection defaults to “Inpatient Orders.” The Print by selection defaults to “Patient,” Print by “Ward” is enabled, and Print by “Clinic” is disabled.

Example: Inpatient Orders/Default to Print by Patient

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/021.png)

- If the user selects the “Clinic” Order Mode on the VDL, the report dialog Include Orders selection defaults to “Clinic Orders.” The Print by selection defaults to “Patient,” Print by “Ward” is disabled, and Print by “Clinic” is enabled.

Example: Clinic Orders/Default to Print by Patient

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/022.png)

- If the user changes the report dialog Include Orders selection from “Inpatient Orders” to “Clinic Orders” (or vice versa), the dependent corresponding Print by option must also change.
-   
  > If no patient record is open:
- The report dialog Print by selection defaults to “Ward” or “Clinic,” based on user parameter that indicates the last mode that the user selected, and Print by “Patient” is disabled.
- If the user chooses “Inpatient Orders” for the Include Orders selection, the report dialog Print by selection defaults to “Ward.”

Example: Include Inpatient Orders/Default to Print by Ward

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/023.png)

- If the user chooses “Clinic Orders” for the Include Orders selection, the report dialog Print by selection defaults to “Clinic.”

Example: Include Clinic Orders/Default to Print by Clinic

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/024.png)

The report header will display “Include Clinic Orders Only” for reports that include only Clinic Order data. The report header will display “Include Inpatient Orders Only” for reports that include only Inpatient order data.

When printing mutually exclusive reports for Clinic orders only, the system includes the Clinic Name associated with each clinic administration and displays the word “Location” in the header, where appropriate, to indicate where the administration took place.

Example: Administration Times Report

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/025.png)

## Combined Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Combined reports include the following:

- MAHReport
- Med Log Report
- Med History Report
- IV Bag Status Report
- Med Therapy Report
- PRN Effectiveness Report

> Both Inpatient and Clinic Order data for the selected patient are included in these reports. The inpatient nurse can see any IVs that were infused in Clinic that must be marked as completed. The clinic nurse can see any IVs that were infused in Inpatient that must be marked as completed.

> The inpatient nurse can run a PRN Effectiveness report that combines both inpatient and clinic data for a single patient to help document PRN effectiveness for medications administered in Clinic. The clinic nurse, likewise, can document PRN effectiveness for medications administered in Inpatient.

> Each report dialog contains the following message: “This report includes both Inpatient and Clinic Order data.”

> The Print by “Clinic” option is disabled since selecting clinics is not allowed when printing these combined reports.

- If a patient record is open:
- The Print by “Patient” option is enabled, and the report dialog Print by selection defaults to “Patient.”

Example: Default to Print by Patient

> ![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/026.png)

- If no patient record is open:
- The Print by “Patient” option is disabled, and the report dialog Print by selection defaults to “Ward.”

Example: Default to Print by Ward

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/027.png)

> The header of all reports displays the wording “Include Inpatient and Clinic Orders.”

### MAH Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Inpatient nurse may print this report by ward or by patient. The Clinic nurse will print this report by patient.

MAH Report for a Single Patient

- If a patient has Inpatient orders, the header “\*\*INPATIENT ORDERS\*\*” is printed, followed by a list of all of the patient’s Inpatient orders in two groups:

Continuous Unit Dose and IV orders

PRN, STAT, and One-Time orders

> The word “INPATIENT” is displayed above the Order Start Date for each medication administered in an inpatient ward.

- If a patient has Clinic Orders, the header “\*\*CLINIC ORDERS\*\*” is printed, followed by a list of all of the patient’s Clinic orders in two groups:

Continuous Unit Dose and IV orders

PRN, STAT, and One-Time orders

> The Clinic name is displayed above the Order Start Date for each medication administered in a clinic.

> Within each group, the orders are sorted alphabetically by medication name.

> A combined legend prints at the end of the report, containing nurse initials for both Inpatient and Clinic administrations, if applicable.

> The word “Location” displays above the “Start Date” in the left hand column header.

Example: MAH Report for Single Patient

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/028.png)

MAH Report for a Selected Ward of Nurse Unit

> All patients assigned to the selected ward or nurse unit are printed as a series of single patient reports as described above for a single patient.

Example: MAH Report by Selected Ward

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/029.png)

### Med Log Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Inpatient nurse may print this report by ward or by patient. If no patient is selected, the report defaults to by Ward, then the nurse can select one patient on the ward (typical).

> The Clinic nurse will print this report by patient.

> The Medication Log report displays the Inpatient Ward name (where the medication was administered) above the Start Date for each medication administered in an inpatient ward.

> The report displays the Clinic name (where the medication was administered) above the Start Date for each medication administered in a clinic. The report displays the word “Location” above the “Activity Date” in the left hand column header.

Example: Medication Log Report

> ![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/030.png)

# Mutually Exclusive Reports – Select Clinics Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user may select one or more clinics for clinic-based mutually exclusive reports by specifying a search prefix entry for their division/location that searches from the beginning of the clinic name, and a search text entry that searches within the clinic name to filter the list of available clinics to a more manageable list.

When the “Clinic Orders” option in the Include Orders section of the report dialog is selected, the “Select Clinics” button allows the user to print reports by clinic.

To print reports by Clinic:

- The user clicks the Select Clinics button to display the Clinic Selection dialog.
- The user enters search criteria in the “Enter Search Prefix” field and clicks Search (example: AL – Albany), and/ or
- The user enters a clinic name in the “Enter Search Text” field (example: DERM) and clicks Search.
- The user selects the clinic by clicking on it or using Shift-Click or Ctrl-click to select multiple clinics to include in the report.
- The user clicks Add, and the selected clinics move to the Selected Clinics box.
- The user clicks OK, the data in the Selected Clinics window will be used for the report, and the number of clinics selected will be reflected on the requesting report dialog.

Example: Clinic Selection - Enter Search Prefix Field

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/031.png)

Example: Clinic Selection - Enter Search Text Field

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/032.png)

> Note: Previous prefix and search entries are retained and displayed for the user from session to session. If either search entry is invalid or not found, the error message: “Invalid Clinic Lookup” displays.

> Note: Although multiple searches that can result in duplicates displayed in the Selected Clinics windows are allowed, all reports that allow clinic selection display the list of selected clinics sorted in alphanumeric order without duplicates in the “Search List” portion of the report header.

Example: Medication Due List Report

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/033.png)

# BCMA Missing Dose Request Parameter for Clinic Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user may set the MISSING DOSE PRINTER field in the CLINIC DEFINITION (#53.46) file according to the following 3-tiered approach to defining a clinic missing dose request printer.

- This field allows the user to specify a printer device that is located at a particular clinic in order to send all missing dose requests for this clinic to the specified printer.

Example: Specifying a Printer Device for the Clinic

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/034.png)

- If no specific Clinic Missing Dose Request Printer device is defined above for this particular clinic, missing dose requests will print on a general Clinic Missing Dose Request Printer that is defined for the division in the BCMA Parameters Tab Output Devices.

Example: BCMA Parameters Tab Output Devices

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/035.png)

- If no specific Clinic Missing Dose Request Printer device is defined above for this particular clinic, AND no general Clinic Missing Dose Request Printer is defined for a division in the BCMA Parameters Tab Output Devices, then all missing dose requests for both clinic and inpatient orders will print on the Inpatient Missing Dose Request Printer defined for the division in the BCMA Parameters Tab Output Devices.

Example: BCMA Parameters Tab Output Devices

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/036.png)

# Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA Backup System (BCBU)

BCMA patch PSB\*3\*70 does not provide contingency backup for Clinic Orders.  PSB\*3\*73 has been developed so that the Class 1 Bar Code Back Up (BCBU) will include Clinic Orders. This patch is currently in test and is expected to be released in the next month.  If you have questions please file a REMEDY ticket.

Unable to Scan Functionality

BCMA allows clinic patients to be retrieved using Unable to Scan functionality, but does not log Unable to Scan events for retrieval of clinic patients.

BCMA allows clinic medications to be administered using Unable to Scan functionality, but does not log Unable to Scan events for administration of medications.

BCMA does not track keyed entries during retrieval of clinic patient records or administration of clinic administrations.

The Unable to Scan Detailed and Summary reports only include data for Inpatient administrations.

> **NOTE:** Unable to Scan logging for retrieval of Clinic patients and administration of Clinic Orders will be implemented in a future increment.

# Witness for High Risk/High Alert Drugs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The overall goal of this new functionality is to provide a trigger mechanism to alert the the nurse to easily identify high risk/high alert medications that require/recommend a witness on the VDL and Cover Sheet, and prompt for witness credentials within the administration workflow.

The Icon ![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/037.png) appears in the “Wit” column on the Cover Sheet, Unit Dose, IVP/IVPB and IV tabs to alert the user that a High Risk/High Alert medication is to be administered, requiring/recommending a second signature from licensed personnel. When the user’s cursor hovers over the icon, the following text displays: “High Risk/High Alert – Witness Required/Recommended.”

The witness provides an independent double check for a high risk/high alert medication in BCMA and is automatically prompted for their credentials before the medication is administered and allowed to add an optional comment to the patient record. The witness name, the date/time witnessed, and the optional witness comment are stored in the Medication Log.

Highlights

- High risk/high alert drugs that are flagged in the drug file as recommending/requiring a witness are now easily identified on the BCMA VDL and Cover Sheet.
- A new column entitled “Wit” has been added to the Cover Sheet and all medication tabs on the VDL to display the high risk/high alert icon when a witness is recommended/required for the administration.
- New BCMA Witness Sign-On dialog for administrations recommending/requiring a witness automatically captures witness credentials and optional comment within the administration workflow. If user was previously prompted for quantity and units, the dialog displays the quantity and units to be administered.
- Witness Information is stored in the Med Log, displayed on the Medication Log report, and prints additional details in the audit log.
- If a High Risk/High Alert medication is flagged as “Required to witness,” the medication cannot be documented as Given/Infusing without a witness.
- If a High Risk/High Alert medication is flagged as “Recommended to witness,” the medication can be documented as Given/Infusing without a witness.

# Defining High Risk/High Alert Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local site policy dictates which High Risk/High Alert medications are to be marked as “Recommended to witness” versus “Required to witness” in BCMA. Sites should carefully consider which High Risk/High Alert medications are marked as “Recommended to witness,” as those medications will be allowed to be administered without a witness in BCMA. Conversely, High Risk/High Alert medications that are marked as “Required to witness” must be administered with an authorized witness, and cannot be documented as “Given” or “Infusing” without the witness.

Your nursing and pharmacy staff will work together to assign a Witness HR Order Code in their local PHARMACY ORDERABLE ITEM FILE (#50.7) to control whether a witness is required or recommended for a particular medication and the impact on the workflow. The four qualifying codes are as follows:

| Code     | Witness Required/Recommended                                           |
|--------------|----------------------------------------------------------------------------|
| Code 0/Null: | Not a High Risk/High Alert drug (default)                                  |
| Code 1:      | High Risk/High Alert – Not required to witness in BCMA (Pharmacy use only) |
| Code 2:      | High Risk/High Alert – Recommended to witness in BCMA                  |
| Code 3:      | High Risk/High Alert – Required to witness in BCMA                     |

> **NOTE:** All drugs flagged with a Code 2 or Code 3 will display the High Risk/High Alert icon and hover text in BCMA, and will display the witness sign-on prompt within the administration workflow.

# New Icon Added to Icon Legend

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Icon ![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/038.png) appears on the VDL to indicate that medications require or recommend a witness before being administered.

<u>Example: Icon Legend</u>

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/039.png)

# “Wit” Column Added to the VDL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new column for witness has been added to the left of the active medication. If the Icon ![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/040.png) appears in the “Wit” column on the Cover Sheet, Unit Dose, IVP/IVPB and IV tabs it alerts the user that a High Risk/High Alert medication is either required or recommended to be administered with an independent double check and second signature from licensed personnel.

The system allows the user to sort the icons in the witness column by clicking on the column heading “Wit,” or by selecting the Due List menu, Sort by, then Witness.

The system automatically prompts for the witness sign-on, determines if the witness is authorized to witness a high risk/high alert medication administration and stores the information with the patient’s record so that the process is integrated into the administration workflow.

<u>Example: “Wit” Column on the VDL</u>

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/041.png)

Example: Hover Text on the Cover Sheet

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/042.png)

Example: Hover Text on the VDL

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/043.png)

# BCMA Witness Sign-on Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCMA Witness Sign-On Dialog is displayed last in the administration workflow, just before the Give/Infuse action. The following administration information is displayed at the top of the dialog:

- Medication (Orderable Item)
- Scheduled Admin Time
- Schedule Type
- Dosage/Infusion Rate
- Units Per Dose
- Last Action, if applicable
- Bag ID or N/A
- Quantity and Units Documented, if applicable
- Medication Route
- Special Instructions/Other Print Info
- Dispense Drugs/Medications/Solutions

The following information displays at the bottom of the Witness Sign-On dialog in a group entitled “Witness Sign-On:”

- Witness Access Code field
- Witness Verify code field
- If Witness is recommended, the following message displays: “This drug is a High Risk/High Alert medication that *recommends* a second signature from licensed personnel for administration.”
- If Witness is required, the following message displays: “This drug is a High risk/High Alert medication that *requires* a second signature from licensed personnel for administration.”

Example: BCMA – Witness Sign-On Dialog

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/044.png)

# Witnessing High Risk/High Alert Drugs When a Witness is Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a medication is flagged with a Code 3 (Required to witness), the BCMA Witness Sign-On dialog will display last in the administration workflow. The administering nurse must identify and obtain their witness, and have them perform the independent double check, according to user’s local site policy for High Risk/High Alert administrations.

At the BCMA Witness Sign-On dialog:

- The witness reviews the administration information and enters their Access and Verify codes.
- The witness can enter an optional comment, up to 150 characters in length, and clicks OK.
- The witness must click OK to complete the administration or click Cancel to display the “Order Administration Cancelled” confirmation dialog then click OK to acknowledge the cancellation and to return to the VDL.

  Note: The prompt for changing the user’s Verify code is not supported.
- If the Witness Sign-On Credentials are valid:
- User is returned to the VDL.
- The administration is marked as “Given” or “Infusing.”

> Note: The High Risk/High Alert Drug code values for each medication/additive/solution are included in the order. The Witness IEN, Date/Time, Optional Comment and Witness HR Order Code (the highest value of all High Risk/High Alert Drug code values in the order), are determined and stored. The “Witnessed?” flag is set to a value of Yes, indicating the administration was witnessed.

Example: BCMA – Initial Witness Sign-On Dialog  
for a High Risk/High Alert Administration  
when Witness is Required

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/045.png)

- If previously prompted for Quantity and Units, the BCMA Witness Sign dialog will display the Quantity and Units to be administered.

Example: BCMA – Witness Sign-On Dialog with  
Quantity and Units Display for a High Risk/High Alert  
Administration when Witness is Required

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/046.png)

- If the Witness Sign-On credentials are invalid:
- An Error message will display, based on the reason the credentials were not validated. User clicks OK to clear the error and return to the BCMA Witness Sign‑On Dialog.

> Note: See section entitled “Error Messages for Witness Validation” for all witness sign-on error messages.

- The administration workflow will not continue until the witness enters a valid Access and Verify code and has authority to be a witness.
- To cancel the administration, the user clicks Cancel to display the “Order Administration Cancelled” dialog, then clicks OK to acknowledge the cancellation and to return to the VDL.
-   
  > If Witness Sign-On credentials are blank:
- The Error message: “An authorized witness must sign on before you are able to administer this High Risk/High Alert medication” and the OK button displays.

Example: Information Message when User Attempts to Proceed  
without Authorized Witness Access and Verify Codes

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/047.png)

- User clicks OK to clear the error and return to the BCMA Witness Sign‑On Dialog to retry.
- The administration will not continue until the witness enters a valid Access and Verify code and has authority to be a witness.
- To cancel the administration, user clicks Cancel to display the “Order Administration Cancelled” dialog, then clicks OK to acknowledge the cancellation and to return to the VDL.

# Witnessing High Risk/High Alert Drugs When a Witness is Recommended and Witness is Provided

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a medication is flagged with a Code 2 (Recommended to witness), the BCMA Witness Sign-On dialog will display last in the administration workflow. The administering nurse identifies and obtains witness, and has them perform the independent double check, according to local site policy for High Risk/High Alert administrations.

At the BCMA Witness Sign-On dialog:

- The witness should review the administration information and enter their Access and Verify codes.
- The witness may enter an optional comment, up to 150 characters in length.
- The witness clicks OK to complete the administration or clicks Cancel to display the “Order Administration Cancelled” confirmation dialog, then clicks OK to acknowledge the cancellation and return to the VDL.
- If the Witness Sign-On Credentials are valid:
- User is returned to the VDL.
- The administration is marked as “Given” or “Infusing.”

> Note: The High Risk/High Alert Drug code values for each medication/additive/solution are included in the order. The Witness IEN, Date/Time, Optional Comment and Witness HR Order Code (the highest value of all High Risk/High Alert Drug code values in the order), are determined and stored. The “Witnessed?” flag is set to a value of Yes, indicating the administration was witnessed.

Example: BCMA Witness Sign-On Dialog  
for a High Risk/High Alert Administration  
when Witness is Recommended

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/048.png)

- If the Witness Sign-On credentials are invalid:
- An error message will display, based on the reason the credentials were not validated. User clicks OK to clear the error and return to the BCMA Witness Sign‑On Dialog.

> Note: See section entitled “Error Messages for Witness Validation” for all witness sign-on error messages.

- For High Risk/High Alert medications that are flagged as recommended to witness, if user has a witness available, the credentials entered must be valid.
- To cancel the administration, user clicks Cancel to display the “Order Administration Cancelled” confirmation dialog, then clicks OK to acknowledge the cancellation and to return to the VDL.

# Witnessing High Risk/High Alert Drugs When a Witness is Recommended and No Witness is Provided

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a medication is flagged with a Code 2 (Recommended to Witness), the BCMA Witness Sign-On dialog will display last in the administration workflow.

At the BCMA Witness Sign-On dialog:

- The user leaves the Access and Verify codes blank and clicks OK.
- The warning message: “You are attempting to administer a High Risk/High Alert drug without the presence of an authorized witness. Actions taken will be recorded in the audit log. Do you want to continue WITHOUT A WITNESS?” displays.

Example: Warning Message when Attempting  
to Administer a High Risk/High Alert Drug Without a Witness

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/049.png)

- User clicks No to return to the BCMA Witness Sign-On dialog to enter witness credentials.
- User clicks Yes to return to the BCMA Witness Sign-On dialog and acknowledge the message.
- The Access Code and Verify Code fields are grayed out, and the OK button is disabled.

Example: BCMA Witness Sign On Dialog with  
Acknowledgement of Administering a High Risk/High Alert Medication  
without a Witness

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/050.png)

- User reads the acknowledgement message: “I acknowledge that I am administering this High Risk/High Alert medication without the presence of an authorized witness” and checks the box. The OK button is enabled only after the acknowledgment checkbox is completed.
- User enters an optional comment, up to 150 characters in length.
- User selects one of the following:
- Clicks OK to complete the administration and return to the VDL. The administration is marked as “Given” or “Infusing.”
- Clicks Cancel to display the “Order Administration Cancelled” dialog. Clicks OK to acknowledge the cancellation and to return to the VDL.

# Error Messages for Witness Validation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA authenticates witness credentials based on the witness’ access and verify codes, security keys, and primary and secondary menu options. The conditions are checked in the sequence specified below, such that if more than one condition is applicable to the witness, the first matching condition will determine the error message displayed.

- If the Witness Access and Verify Codes are not valid
- The error message “Invalid Witness sign-on” displays.
- User clicks OK to clear the error and return to the BCMA Witness Sign-On dialog.

Example: Error Message when  
Witness Credentials  
are Not Valid

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/051.png)

- If the witness is a student holding the PSB STUDENT Key and is attempting to witness for self or any other user
- The error message: “A student does not have authority to witness a High Risk/High Alert administration” displays.
- User clicks OK to clear the error and return to the BCMA Witness Sign-On dialog.

Example: Error Message when Student User  
Attempts to Sign-On as Witness

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/052.png)

- If the witness is a user holding the PSB NO WITNESS key, they are identified as unauthorized to witness high risk/high alert administrations.
- The error message: “You do not have authority to witness a High Risk/High Alert administration” displays.
- User clicks OK to clear the error and return to the BCMA Witness Sign-On dialog.

> Note: The PSB NO WITNESS security key is assigned to personnel who are BCMA users, but are not authorized to witness High Risk/High Alert administrations such as Unlicensed Assistive Personnel and Respiratory Therapists.

Example: Error Message when User holding  
PSB NO WITNESS key Attempts to Sign-On as Witness

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/053.png)

- If the witness is a Read-Only user holding the PSB READ ONLY Key:
- The error message “Read-Only users do not have authority to witness a high risk/high alert administration” displays.
- User clicks OK to clear the error and return to the BCMA Witness Sign-On dialog.

Example: Error Message when User holding  
PSB READ ONLY key Attempts to Sign-On as Witness

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/054.png)

- If the witness is a user holding the PSB INSTRUCTOR Key that is currently logged on with a student holding the PSB STUDENT key:
- The error message: “An instructor monitoring a student does not have authority to witness a High Risk/High Alert administration” displays.
- User clicks OK to clear the error and return to the BCMA Witness Sign-On dialog.

> Note: Users holding the PSB INSTRUCTOR key may serve as a witness, if they are not the primary instructor that is currently signed on with a user holding the PSB STUDENT key for the purpose of monitoring that student.

Example: Error Message when  
Instructor currently logged  
in with Student Attempts to Sign-On as Witness

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/055.png)

- If the witness Access Code and Verify Code are the same as the administering nurse user:
- The error message: “Cannot Witness for yourself” displays.
- User clicks OK to clear the error and return to the BCMA Witness Sign-On dialog.

Example: Error Message when Current User  
Attempts to Witness Own Administration

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/056.png)

- If the user does not have PSB GUI CONTEXT – USER menu option assigned to their primary or secondary menu:
- The error message: “A non-BCMA user does not have authority to witness a High Risk/High Alert administration” displays.
- User clicks OK to clear the error and return to the BCMA Witness Sign-On dialog.

> Note: A witness must be a BCMA user and must have the PSB GUI CONTEXT – USER menu option assigned to their primary or secondary menu. The user is not prompted for Electronic Signature (eSig), even when a division sets the parameter to require eSig for sign-on to BCMA.

Example: Error Message when Non-BCMA User  
Attempts to Sign-On as Witness

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/057.png)

- If an invalid VistA user attempts to sign-on as witness:
- The error message: “Invalid VistA user – No Primary menu setup for this user in the New Person file” displays.
- User clicks OK to clear the error and return to the BCMA Witness Sign-On dialog.

Example: Error Message when Invalid VistA User  
Attempts to Sign-On as Witness

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/058.png)

# Witness Information Stored in Medication Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Medication Log report stores witness information for high risk/high alert medication administrations, including the witness name, date/time witnessed and optional witness comment, if the user selects to include comments on the Witness sign-on dialog. The witness information is captured in the Comments and Audits sections of the Medication Log.

If the user chooses to “Include Comments” on the Medication Log Report dialog, the following witness information appears in the body of the report:

- For High Risk/High Alert administrations marked as “Recommended” or “Required” that are witnessed: Witness Last Name, Witness First Name, Witnessed Date@Time, and Optional Comment.
- For High Risk/High Alert administrations marked as “Recommended to Witness” that are <u>not</u> witnessed: “Witnessed?: No” and Optional Comment.
- For High Risk/High Alert administrations that are marked as “Given,” then later marked as “Undo Given,” prior witness information and any witness comments are removed from the body of the Med Log report.

Witness information is included in the Audits section of the Medication Log Report, if the user selects “Include Audits” on the Medication Log Report dialog.

Example: Medication Log Report

![](psb-3-70-bcma-clinic-orders-high-risk-etc-t-project-release-notes/059.png)

# User Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation distributed with this project includes the following and may be retrieved from the VISTA Documentation Library (VDL) on the Internet at the following address: <http://www.va.gov/vdl>.

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><u>File Names</u></th>
<th><u>Description</u></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSB_3_UM_CHAPTERS_1_thru_6_R1213.PDF</td>
<td><p>BCMA V.3.0 GUI User Manual – Chapters</p>
<p>1 through 6</p></td>
</tr>
<tr class="even">
<td>PSB_3_UM_CHAPTERS_7_thru_13_R1213.PDF</td>
<td><p>BCMA V.3.0 GUI User Manual – Chapters</p>
<p>7 through 13</p></td>
</tr>
<tr class="odd">
<td>PSB_3_MAN_UM_R1213.PDF</td>
<td>BCMA V.3.0 Manager’s User Manual</td>
</tr>
<tr class="even">
<td>PSB_3_P70_MAN_UM_CP.PDF</td>
<td><p>BCMA V.3.0 Manager’s User Manual Change</p>
<p>Pages PSB*3*70</p></td>
</tr>
<tr class="odd">
<td>PSB_3_TM_R1213.PDF</td>
<td>BCMA V.3.0 Technical Manual/Security Guide</td>
</tr>
<tr class="even">
<td>PSB_3_P70_TM_CP.PDF</td>
<td>BCMA V.3.0 Technical Manual Security Guide Change Pages PSB*3*70</td>
</tr>
<tr class="odd">
<td>PSB_3_P70_RN.PDF</td>
<td>Release Notes – BCMA V.3.0 (PSB*3*70)</td>
</tr>
<tr class="even">
<td>PSB_3_P70_IMR6_IG.PDF</td>
<td>Installation Guide – BCMA V.3.0 (PSB*3*70)</td>
</tr>
</tbody>
</table>

# Associated Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Name                     | Field Name             | New/Mod/Del |
|-----------------------------------|----------------------------|-----------------|
| BCMA MEDICATION LOG (53.79)       | WITNESS DATE/TIME (.28)    | New             |
|                                   | ADMIN WITNESSED BY (.29)   | New             |
|                                   | WITNESS COMMENT (.31)      | New             |
| DISPENSE DRUG (53.795)            | HIGH RISK/HIGH ALERT (.05) | New             |
| ADDITIVES (53.796)                | HIGH RISK/HIGH ALERT (.05) | New             |
| SOLUTIONS (53.797)                | HIGH RISK/HIGH ALERT (.05) | New             |
| BCMA MISSING DOSE REQUEST (53.68) | CLINIC (1)                 | New             |
| BCMA REPORT REQUEST (53.69)       | SORT BY (.11)              | Mod             |
|                                   | ORDERS TYPE MODE C/I (4)   | New             |
|                                   | CLINIC TO PRINT (5)        | New             |

# Associated Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Form Name             | File Name (Number)            | New/Mod/Del |
|---------------------------|-----------------------------------|-----------------|
| PSB MISSING DOSE FOLLOWUP | BCMA MISSING DOSE REQUEST (53.68) | Mod             |
| PSBO MD                   | BCMA REPORT REQUEST (53.69)       | Mod             |

# Associated Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name          | Type    | New/Modified/Deleted |
|--------------------------|-------------|--------------------------|
| PSB MISSING DOSE REQUEST | run routine | Deleted                  |

# Parameter Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Parameter Definitions   | New/Deleted |
|-----------------------------|-----------------|
| PSB PRINTER CO MISSING DOSE | New             |

# Associated Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| RPC Name            | New/Modified/Deleted |
|-------------------------|--------------------------|
| PSB CLINICLIST          | New                      |
| PSB GETCOVERSHEET1      | Modified                 |
| PSB GETORDERTAB         | Modified                 |
| PSB MEDS ON PATIENT     | New                      |
| PSB REPORT              | Modified                 |
| PSB SUBMIT MISSING DOSE | Modified                 |
| PSB TRANSACTION         | Modified                 |
| PSB USERLOAD            | Modified                 |
| PSB USERSAVE            | Modified                 |
| PSB WITNESS             | New                      |

# Associated Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Security Key Name | New/Deleted |
|-----------------------|-----------------|
| PSB NO WITNESS        | New             |

# Associated Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Template Name | Type | File Name (Number) | New/Mod/Del |
|-------------------|----------|------------------------|-----------------|
| PSB DIVISION      | KERNEL   | 8989.52                | Mod             |

# Patient Safety Issue Corrections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Patient Safety Issue corrections are made with this patch:

- PSPO 2265 – Field populated in error with scanner using medication bar code.
- PSPO 2247 – No prompt for quantity given for injectable medication
- PSPO 164 – IV duration not displaying in BCMA
- PSPO 521 – IVs hung just before the IV order is set to expire

# Remedy Tickets Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Remedy Tickets were resolved with this patch:

| Name         | Description                                                                                                         |
|------------------|-------------------------------------------------------------------------------------------------------------------------|
| INC0000000591804 | Error - \<UNDEFINED\>SCANPT+29^PSBRPC                                                                                   |
| INC0000000705800 | PSPO \#2247 - No prompt for amount given for injectable med.                                                            |
| INC0000000711794 | PSPO \#2265 - Field populated in error with scanner using med barcode.                                                  |
| INC0000000426560 | Have to select a check box that they have confirmed sensitive patient's identities without seeing date of birth and SSN |
| INC0000000776745 | Inpatient Medications - IV Orders Issue                                                                                 |
| INC0000000776117 | Multiple missing doses are not appearing in BCMA                                                                        |

# New Service Requests (NSRs) Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following NSR was resolved with this patch:

| Number | Name      |
|------------|---------------|
| 20070506   | Clinic Orders |

# BCMA Online Help Update 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCMA GUI Online Help system has been updated to include all released BCMA PSB\*3\*70 functionality.

# Installation Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation details are contained in the Patch Description and Installation Guide, “BCMA Clinic Orders, High Risk High Alert Drugs, IV Bag Logic, T@0 Project Installation Guide.”

See the Installation Guide for information about the Shared RPC Broker.