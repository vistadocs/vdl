---
title: PSJ*5*113 Release Notes-IMR-Increment I
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: IMR-Increment I
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*113
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: - [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying) - [# Introduction](#introduction) - [Patch PSJ\5\113 – Order Entry Enhancements](#patch-psj5113-order-entry-enhancements) - [Patch PSS\1\143 – Order Entry Validation for Administration Times](#patch-pss1143-or
audience: 
keywords: 
  - schedule
  - order
  - administration
  - validation
  - times
  - time
  - table
  - contents
  - entered
  - frequency
page_count: 0
word_count: 1472
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_113_pss_1_143_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_113_pss_1_143_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

> ![](psj-5-113-release-notes-imr-increment-i/001.png)

Inpatient Medications (IMR)Order Validation Project

####### RELEASE NOTES

PSJ\*5\*113

PSS\*1\*143

June 2010

Office of Enterprise Development

Table of Contents

# *(This page included for two-sided copying.)*


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying)
- [# Introduction](#introduction)
  - [Patch PSJ\5\113 – Order Entry Enhancements](#patch-psj5113-order-entry-enhancements)
  - [Patch PSS\1\143 – Order Entry Validation for Administration Times](#patch-pss1143-order-entry-validation-for-administration-times)
- [Order Entry/Order Validation Enhancements](#order-entryorder-validation-enhancements)
  - [Order Validation Checks](#order-validation-checks)
  - [Sequence of Schedule Type and Schedule Prompts](#sequence-of-schedule-type-and-schedule-prompts)
  - [PSS SCHEDULE EDIT OPTION Validation](#pss-schedule-edit-option-validation)
- [Modifications for VistA Help Text](#modifications-for-vista-help-text)

# # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document provides a brief description of the enhanced features of the Order Validation defined by the BCMA-Inpatient Medications Request for Special Focus Group SFG Initial Request Analysis (IRA). The Release Notes include changes from Inpatient Medications patch PSJ\*5\*113 and Pharmacy Data Management patch PSS\*1\*143.

## Patch PSJ\*5\*113 – Order Entry Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previously Inpatient Medications allowed orders to be created with conflicting administration times, frequencies, schedules, and schedule types. These orders were not always displayed correctly on the Virtual Due List (VDL) in the Barcode Medication Administration (BCMA) application. This enhancement adds several new order validation checks to improve the data that is displayed on the VDL. These order validation requirements will apply to Unit Dose orders and to intermittent IV orders. (IV orders do not have Schedule Type.)

## Patch PSS\*1\*143 – Order Entry Validation for Administration Times

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*143 adds validation checks to the Standard Schedule Edit \[PSS SCHEDULE EDIT\] option to prevent the Standard Administration Times, Ward Administration Times, Frequency and Schedule Type fields of a schedule from conflicting with one another.

# Order Entry/Order Validation Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Order Validation Checks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These order validation checks will apply to Unit Dose orders and to intermittent IV orders.

![](psj-5-113-release-notes-imr-increment-i/002.png)Note: IV orders do not have Schedule Type.

#### Order Validation Check One

> For intermittent IV orders, references to an order’s Schedule Type will refer to either the TYPE OF SCHEDULE from the Administration Schedule file (#51.1), or PRN for schedule names in PRN format, or CONTINUOUS for schedule names in Day of Week format.

#### Order Validation Check Two

> The system shall use the schedule type of the schedule from the Administration Schedule file independent of the schedule name when processing an order to determine if administration times are required for a particular order.

- Order Validation Check Three

If an order has the Schedule Type of Continuous, the Schedule entered is NOT in Day of Week (Ex. MO-FR) or PRN (Ex. TID PC PRN) format, and the frequency associated with the schedule is one day (1440 minutes) or less, the system will not allow the number of administration times associated with the order to be greater than the number of administration times calculated for that frequency. The system will allow for the number of administration times to be LESS than the calculated administration times for that frequency but not less than one administration time. (For example, an order with a schedule of BID is associated with a frequency of 720 minutes.  The frequency is divided into 1440 minutes (24 hours) and the resulting calculated administration time is two.  For this order, the number of administration times allowed may be no greater than two, but no less than one.  Similarly, a schedule frequency of 360 minutes must have at least one administration time but cannot exceed four administration times.)

If an order has the Schedule Type of Continuous, the Schedule entered is NOT in Day of Week (Ex. MO-FR) or PRN (Ex. TID PC PRN) format, and the frequency associated with the schedule is greater than one day (1440 minutes) and evenly divisible by 1440, only one administration time is permitted. (For example, an order with a schedule frequency of 2880 minutes must have ONLY one administration time.  If the frequency is greater than 1440 minutes and not evenly divisible by 1440, no administration times will be permitted.)

The system shall present warning/error messages to the user if the number of administration times is less than or greater than the maximum admin times calculated for the schedule or if no administration times are entered. If the number of administration times entered is less than the maximum admin times calculated for the schedule, the warning message: “The number of admin times entered is fewer than indicated by the schedule.” shall appear. In this case, the user will be allowed to continue after the warning. If the number of administration times entered is greater than the maximum admin times calculated for the schedule, the error message: “The number of admin times entered is greater than indicated by the schedule.” shall appear. In this case, the user will not be allowed to continue after the warning. If no admin times are entered, the error message: “This order requires at least one administration time.” shall appear. The user will not be allowed to accept the order until at least one admin time is entered.

- Order Validation Check Four

If an order has a Schedule Type of Continuous and is an Odd Schedule {a schedule whose frequency is not evenly divisible by or into 1440 minutes (1 day)}, the system shall prevent the entry of administration times. For example, Q5H, Q17H – these are not evenly divisible by 1440. In these cases, the system shall prevent access to the administration times field. No warning message is presented.

- Order Validation Check Five

If an order has a Schedule Type of Continuous with a non-odd frequency of greater than one day, (1440 minutes) the system shall prevent more than one administration time, for example, schedules of Q72H, Q3Day, and Q5Day.

If the number of administration times entered exceeds one, the error message: “This order requires one admin time” shall appear. If no administration times are entered, the error message: “This order requires at least one administration time.” shall appear. The user will not be allowed to accept the order until at least one admin time is entered.

- Order Validation Check Six

If an order has a Schedule Type of One Time, or if an order is entered with a schedule that is defined in the schedule file as One Time, the system shall prevent the user from entering more than one administration time.

If more than one administration time is entered, the error message: “This is a One Time Order - only one administration time is permitted.” shall appear. No administration times are required.

- Order Validation Check Seven

For an order with a Schedule Type of Continuous where no doses/administration times are scheduled between the order’s Start Date/Time and the Stop Date/Time, the system shall present a warning message to the user and not allow the order to be accepted or verified until the Start/Stop Date Times, schedule, and/or administration times are adjusted so that at least one dose is scheduled to be given.

If the stop time will result in no administration time between the start time and stop time, the error message: “There must be an admin time that falls between the Start Date/Time and Stop Date/Time.” shall appear.

## Sequence of Schedule Type and Schedule Prompts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to PSJ\*5\*113, the order of the prompts in Inpatient Medications order entry was Schedule Type followed by Schedule. The sequence of the prompts was changed so that the Schedule prompt falls before the Schedule Type prompt.

#### Schedule Validation Requirement One

> When a schedule is selected at the Schedule Field, the system shall default the Schedule Type for the schedule entered from the Administration Schedule File into the order.

#### Schedule Validation Requirement Two

> If the user changes the schedule, a warning message will be generated stating that the administration times and the schedule type for the order will be changed to reflect the defaults for the new schedule selected.

> The warning message: “This change in schedule also changes the ADMIN TIMES and SCHEDULE TYPE of this order.” shall appear.

#### Schedule Validation Check Three

> If the schedule type is changed from Continuous to PRN during an edit, the system shall automatically remove any administration times that were associated with the schedule so that the order will not include administration times.

## PSS SCHEDULE EDIT OPTION Validation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Validation checks were added to the Standard Schedule Edit \[PSS SCHEDULE EDIT\] option to prevent the Standard Administration Times, Ward Administration Times, Frequency and Schedule Type fields of a schedule from conflicting with one another.

#### Schedule Edit Validation One

> The system shall validate for schedules with a Schedule Type of Continuous and a frequency of 1 day (1440 minutes) or less that the number of administration times is less than or equal to 1440 divided by the frequency. For example, a schedule frequency of 720 minutes must have at least one administration time and cannot exceed two administration times. Similarly, a schedule frequency of 360 minutes must have at least one administration time but cannot exceed four administration times.

> The system shall present warning/error messages to the user if the number of administration times is less than or greater than the maximum admin times calculated for the schedule or if no administration times are entered. If the number of administration times entered is less than the maximum admin times calculated for the schedule, the warning message: “The number of admin times entered is fewer than indicated by the schedule.” shall appear. In this case, the user will be allowed to continue after the warning. If the number of administration times entered is greater than the maximum admin times calculated for the schedule, the error message: “The number of admin times entered is greater than indicated by the schedule.” shall appear. The user will not be allowed to accept the order until the number of admin times is adjusted. If no admin times are entered, the error message: “This order requires at least one administration time.” shall appear. The user will not be allowed to accept the order until at least one admin time is entered.

#### Schedule Edit Validation Two

> The system shall validate for frequencies greater than one day (1440 minutes), that only one administration time is permitted. The system shall present an error message to the user if more than one administration time is entered.

> The error message: “This schedule has a frequency greater than one day (1440 minutes). More than one Administration Time is not permitted.” shall appear if more than one administration time is entered.

#### Schedule Edit Validation Three 

> In the Standard Administration Times and the Ward Administration Times fields in the PSS SCHEDULE EDIT option, for a schedule that has a Schedule Type of Continuous, the system shall prevent a user from entering administration times to Odd Schedules {a schedule whose frequency is not evenly divisible by or into 1440 minutes (1 day)}.

> The system shall present an error message to the user if an administration time is entered. The error message: “This is an odd schedule that does not require administration times. BCMA will determine the administration times based off the start date/time of the medication order.” shall appear.

#### Schedule Edit Validation Four

> A validation to TYPE OF SCHEDULE field in the PSS SCHEDULE EDIT was added to remove frequency from the schedule file entry, if the TYPE OF SCHEDULE is changed from CONTINUOUS to ONE TIME, PRN, ON CALL, or DAY OF WEEK.

> The warning message: “The Type of Schedule has changed. The frequency will be removed.” shall appear.

#### Schedule Edit Validation Five

> In the PSS SCHEDULE EDIT option, the system shall prevent a user from creating Day of Week (DOW) schedules that are not in the correct day of week order. The correct order is: SU-MO-TU-WE-TH-FR-SA. The system shall display an error message if the user does not enter the correct order.

> The error message: “The day of the week schedule must be in the correct day of week order. The correct order is: SU-MO-TU-WE-TH-FR-SA.” shall appear.

![](psj-5-113-release-notes-imr-increment-i/003.png)Note: In order to create a schedule with a TYPE OF SCHEDULE of PRN, the last four characters of the schedule name must be “ PRN”, i.e., a space followed by PRN.

Sites should check their ADMINISTRATION SCHEDULE (#51.1) file for schedules that contain PRN in the TYPE OF SCHEDULE (#5) field, but do not contain “ PRN” (SPACE PRN) at the end of the schedule name. These schedules should either be renamed to conform to the PRN naming convention (space PRN appended to the schedule name), or they should no longer be used.

# Modifications for VistA Help Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Help Text in Inpatient Order Entry was modified to add additional text so that the user is able to see the added constraints when entering Administration Times.

*(This page included for two-sided copying.)*

# .
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)