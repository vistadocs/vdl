---
title: PSB*3*83/87 OR*3*417 Clinical Ancillary Services (CAS) Inpatient Medication Administration - Transdermal Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: OR*3*417 Clinical Ancillary Services (CAS) Inpatient Medication Administration - Transdermal
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3*83
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 1
description: This document provides a feature summary of the Clinical Ancillary Services (CAS) - Development – Delivery of Pharmacy Enhancements (DDPE) Inpatient Medication Administration – Transdermal Enhancements for Bar Code Medication Administration (BCMA) v3.0 project, patch PSB\3\83, PSB\3\87, and Associat
audience: 
keywords: 
  - medication
  - removal
  - bcma
  - site
  - span
  - table
  - contents
  - time
  - report
  - class
page_count: 0
word_count: 5414
section_count: 14
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p83_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p83_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

> ![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/001.png)

Clinical Ancillary Services (CAS) - Development – Delivery of Pharmacy Enhancements (DDPE)INPATIENT MEDICATION ADMINISTRATION – TRANSDERMAL ENHANCEMENTSfor BCMA V. 3.0

####### RELEASE NOTES

PSB\*3\*83, PSB\*3\*87, and OR\*3\*417

> December 2016

Office of Information & Technology (OI&T)

Table of Contents

Table of Figures

# Inpatient Medication Administration – Transdermal Enhancements


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Inpatient Medication Administration – Transdermal Enhancements](#inpatient-medication-administration-transdermal-enhancements)
- [Introduction](#introduction)
  - [BCMA Highlights](#bcma-highlights)
  - [BCMA GUI](#bcma-gui)
  - [BCBU - PSB\3\87](#bcbu-psb387)
- [BCMA Screen Examples](#bcma-screen-examples)
  - [BCMA Unit Dose Virtual Due List (VDL) Example](#bcma-unit-dose-virtual-due-list-vdl-example)
  - [Next Dose Action Column Information](#next-dose-action-column-information)
  - [Unit Dose VDL Information](#unit-dose-vdl-information)
- [Viewing and Printing Reports](#viewing-and-printing-reports)
  - [Existing Report Modifications](#existing-report-modifications)
  - [BCMA Report Examples](#bcma-report-examples)
- [Anatomic Location for Medication Administrations](#anatomic-location-for-medication-administrations)
  - [BCMA Site Parameter Application for Anatomic Location](#bcma-site-parameter-application-for-anatomic-location)
  - [User Screens for Anatomic Location](#user-screens-for-anatomic-location)
  - [Clinic Orders](#clinic-orders)
- [User Documentation](#user-documentation)
- [Associated Files and Fields](#associated-files-and-fields)
- [Associated Forms](#associated-forms)
- [Associated Options](#associated-options)
- [Parameter Definitions](#parameter-definitions)
- [Associated Remote Procedure Calls](#associated-remote-procedure-calls)
- [Associated Template](#associated-template)
- [Patient Safety Issue Corrections](#patient-safety-issue-corrections)
- [Remedy Tickets Resolved](#remedy-tickets-resolved)
- [New Service Requests (NSRs) Resolved](#new-service-requests-nsrs-resolved)
- [BCMA Online Help Update](#bcma-online-help-update)
- [Installation Details](#installation-details)
  - [Patch PSS\1\191 Related Information](#patch-pss1191-related-information)
  - [Patch PSJ\5\315 Related Information](#patch-psj5315-related-information)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document provides a feature summary of the Clinical Ancillary Services (CAS) - Development – Delivery of Pharmacy Enhancements (DDPE) Inpatient Medication Administration – Transdermal Enhancements for Bar Code Medication Administration (BCMA) v3.0 project, patch PSB\*3\*83, PSB\*3\*87, and Associated patch OR\*3.0\*417.

Installation instructions for PSB\*3\*83, PSB\*3\*87, and OR\*3.0\*417 are included in the patch description and the Installation Guide.

The following patches are associated and must be installed before PSB\*3\*83:

- PSB\*3.0\*70             
- PSB\*3.0\*76             
- PSJ\*5.0\*315            
- PSB\*3.0\*94             
- PSB\*3.0\*81             
- PSB\*3.0\*86             
- PSB\*3.0\*72        

\*\*\*  WARNING FOR ALL SITES CURRENTLY USING WMA  \*\*\*

                  (Wireless Medication Administration)

                            From CareFusion

The below 15 VAMC sites should not install patch PSB\*3\*83 until the site has confirmed they have received CareFusion's software update:

Pyxis Med Administration Verification VA v. 5.1

 

<span class="mark">REDACTED</span>

Installation of BCMA Patch PSB\*3.0\*83 may cause your WMA application to stop functioning as you would expect it to. In order for the WMA devices to work properly with PSB\*3.0\*83 installed, you must contact CareFusion, the WMA vendor, to obtain the most current version of the WMA software.

The following patches are associated and must be installed before OR\*3\*417:

- OR\*3\*350
- OR\*3\*361
- PSJ\*5\*315
- PSB\*3\*83

Please refer to section 16 for details on patches PSS\*1\*191 and PSJ\*5\*315, which prepared the way for patches PSB\*3\*83 and OR\*3\*417. User action is required to ensure a smooth transition to new functionality. Note that PSB\*3\*83 is required for OR\*3\*417.

## BCMA Highlights

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The enhancements within Inpatient Medication Administration – Transdermal intend to provide a solution to address the errors in transdermal medication administration processes that have led to adverse patient events. The following features related to transdermal medications are needed by the business for patient care to avert these errors in the future, by implementing the following capabilities within Inpatient Medication Administration:

- Create a mechanism to remind the user to “follow-up” on certain medications requiring additional steps in administration or assessment, e.g., alert the user to remove a transdermal medication at a specified time.
- Ensure previous statuses of multi-step medications appear in the Medication Administration History reports, e.g., the date and time a transdermal medication was applied will remain visible after it has been marked “removed.”
- Enhance the current mechanism used to document and display the anatomic location of injectable medications to support transdermal medications as well. Implementation includes changing the terminology of “Injection site” throughout the applications including Inpatient Medication Administration and Veterans Health Information and Systems Technology Architecture (VistA). Any field names used to store or refer to “location” data within VistA are evaluated as to whether or not the terminology needs to be changed. For example, if the field in VistA is named “IV Location”, the name of the field is changed to simply “Location” so that when data from the field are pulled into reports, the field name adequately reflects the updated contents.
- A change to any order involving a transdermal medication forces a misleading “remove patch” alert to appear. The software is changed to differentiate between a change and a discontinued order and display an appropriate and corresponding alert.

> **NOTE:** Based on decision from the Bar Code Resource Office (BCRO), the new features introduced by this project are not applicable to medication orders placed via the CPRS Med Order Button feature in BCMA. Any order for a medication requiring removal (MRR) (i.e., transdermal patch) which is ordered using the CPRS Med Order Button (MOB) in BCMA is exempt from the features included in the new MRR functionality. Any MRRs that have dosage form “patch” which are entered using the CPRS MOB will continue to operate as they do now, e.g. continuing to appear on the BCMA VDL in a “given” status until marked as removed by the user. The medication will not display the new “requires removal icon” and the user will not receive any alert to remove the medication at a specific time.

## BCMA GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This BCMA enhancement also includes a new Graphical User Interface (GUI) executable, BCMA GUI PSB3_0P83.EXE. Installation of this GUI is required immediately after the PSB\*3\*83 patch install for the patch to function.

Features of the BCMA GUI provided by this project are listed below.

1.  Changed the current GUI Unit Dose tab column labeled "Admin Time" to "Next Dose Action".
2.  The "Next Dose Action" column now contains both the next admin times for scheduled administrations and the next Removal time for medications requiring removal (MRRs). The initial login to BCMA sorts the Unit Dose tab in ascending order by this column, so older actions for medications are at the top of the VDL display.
    1.  The Next Action of an administration contains the word "DUE," followed by the scheduled admin time in the standard date@admin time format currently in use.
    2.  The Next Action of a removal contains the word "REMOVE," followed by the scheduled removal time in the standard date@time format.
    3.  The Next Action of an administration that is past due to be given contains the word "LATE," followed by the scheduled admin time in the standard date@admin time format currently in use.
    4.  The Next Action of a removal that is past due to be removed contains the words "LATE-RM," followed by the scheduled removal time in the standard date@time format.
3.  Changed the current GUI column labeled "Wit" to "Alert".
4.  The Alert column still has the ability to display the Witness Required icon and also displays a new Remove icon.
    1.  The icon is displayed only for MRR type meds that were Given and whose next Action is for Removal.
5.  Early/Late warnings are also associated with medications being removed early or late using the same early/late time range that is used for early or late medication admins.
    1.  User comments are prompted for and stored upon continuing with the Early/Late removal action.
6.  Variances are tracked for Early/Late Removals for MRRs in the same manner as they are currently for Early/Late medication administrations and now appear on the Medication Variance Log report.
7.  BCMA Medication Administration History (MAH) report now includes the associated Give actions which were previously overwritten by Remove actions. MRR Removal Times are printed directly below the current Admin Times.
8.  BCMA Administration Times report by Patient has added “(RM)” if MRR removal is the action that needs to be performed within the report parameters. The Print by Ward report now includes Removals in the count of actions scheduled for the report time period.
9.  BMCA Medication Log now prints the historical Give date/time of the MRRs which previously only showed the Remove date/time if that was the last action. Both actions are now available for reporting. The column heading has been changed from "Inj Site" to "Body Site" and the medication detail body text displays the proper label of "Inj Site:" or "Derm Site:" prior to the name of the body site for that medication.
10. BCMA Missed Medications report has added Removals that are past due as noted by “(Remove)” to missed Gives that are currently reported. The column heading has been changed from "Admin Date/Time" to "Missed Date/Time".
11. BCMA Display Order report includes the Removal Times for MRRs directly below the current Admin Times.
12. BCMA Medication History report now prints a prior Give line item directly below the current status line item of Remove for MRRs. The Given administration action was previously overwritten by the Removed last action in the record so the history of the Give information and was not available. This information is now being retrieved from the Audit log and printed on this report. The report header line has replaced "Injection Site" with "Body Site".
13. BCMA Due List report adds Remove Times for MRRs below the Admin Times on this report.
14. BCMA Coversheet Medication Overview and the Coversheet Expired/DC'd/ Expiring Orders reports now include Missed Removals and Removals that are due.
15. A body site diagram is added to the BCMA Parameter GUI client application for the purpose of showing a dot on the body diagram that is associated with the text representation of that site location on the body.
16. The BCMA Parameter GUI client application has access to a new kernel parameter titled in GUI application as "Dermal Site History Max Days.” This allows the BCMA coordinator the ability to control how many days of prior dermal body site location history appears, when a clinician is giving a new dermal medication that is prompting for a body site location.
17. The *Orders for MRRs With Removal Properties* \[PSS MRR ORDERS DIAGNOSTIC RPT\] option, found on the *Pharmacy Data Management* \[PSS MGR\] menu, is also placed on the *Bar Code Medication Administration Manager* \[PSB MGR\] menu.
18. Order Details report accessed via CPRS includes the Removal Times for MRRs directly below the current Admin Times. This was added via OR\*3.0\*417.

## BCBU - PSB\*3\*87

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSB\*3\*87 will enhance the BAR CODE MEDICATION ADMINISTRATION (BCMA) Backup System (BCBU) to support Medications Requiring Removal (MRR). The Backup

System will be able to store the Removal times and duration of administration associated with each medication order.

This patch will add two new fields to the ORDER NUMBER (#53.702) sub-file  under the BCMA BACKUP DATA (#53.7) file.  The two new fields are the REMOVE TIMING (#7.4) field and DURATION OF ADMINISTRATION (#7.5) field. These fields implement changes that will support enhancements to Medical Administration Record(s) MAR reports in the BCBU application.

The MAR reports will print each Scheduled Removal times for MRR medications in the Grid in the same manner as Admin times.  The Remove times will appear below the current scheduled Administration time in the Grid and will be separated by the Label "Remove" in the times column.  Asterisks will print in the body of the Grid in each Removal action box for removal times that are not valid per the Date in that column heading.

The MAR reports will also no longer display the Order number of the

medications being administered.

Please refer to the BCMA Backup System (BCBU) Installation Guide for

PSB\*3\*87 for installation details.

# BCMA Screen Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Cover Sheet, Unit Dose, IVP/IVPB and IV tabs, the column formerly named “Wit” is now named “Alert”.  For medications requiring removal, the “Alert” column on the Cover Sheet and Unit Dose tabs will contain a new “Requires Removal” icon. At the bottom of the BCMA main screen, a new Alert Legend displays, listing the icons that can display in the new Alert column, as shown in Figure 1.

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/002.png)

<span id="_Toc468870949" class="anchor"></span>Figure 1. BCMA Main Screen with New Column Name and Legend

The new “Requires Removal” icon displays in the Icon Legend, which is available via the View menu, as shown in Figure 2.

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/003.png)

<span id="_Toc468870950" class="anchor"></span>Figure 2. Icon Legend with New “Requires Removal” Icon

## BCMA Unit Dose Virtual Due List (VDL) Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “Admin Time” column is replaced by the “Next Dose Action” column, which contains information on medication that is late and/or due for removal along with the admin date and time. If a medication is late, the text is in red. If a cell in the Alert column contains the Requires Removal icon and the medication is due to be removed, the hover hint text consists of “REMOVE” along with the removal date and time, as shown in Figure 3.

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/004.png)

<span id="_Toc468870951" class="anchor"></span>Figure 3. Unit Dose VDL with Hover Text and Next Dose Action Column

## Next Dose Action Column Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rules for information included in the Next Dose Action column are listed below.

> **NOTE:** For non-standard schedules such as DAY@HHMM, HHMM or other odd schedules, Removal Times cannot be calculated due to the lack of a Frequency. Regardless of the Prompt for Removal in BCMA code value for the orderable item, no Removal Times will display in BCMA for these non-standard schedules. These types of schedules must be avoided for Medications Requiring Removal (MRR) orders.

- If the next action for a Continuous medication order is for it to be administered (i.e., Given), the Next Dose Action column contains the word “DUE” and the next Admin Time as a date/time on a separate line. This applies to all Unit Dose medication orders, not just those for medications requiring removal.
- If the next action for a Continuous medication order for a medication requiring removal is for it to be Removed, the Next Dose Action column contains the word “REMOVE” and the next Removal Time as a date/time on a separate line.
- If the next action for a Continuous Inpatient medication order is for it to be administered (i.e., Given), but is late, the Next Dose Action column contains the word “LATE” and the next Admin Time as a date/time on a separate line, with all text in red font. The BCMA site parameter “Allowable Time Limits (In Minutes) After Scheduled Admin / Removal Time” is used as the basis for determining if the medication order is late to be Given.

> Note: This is not applicable to Clinic Orders, which are never designated as LATE.

- Continuous Inpatient medication orders for which the Next Dose Action column contains the word “LATE”, along with the Admin Time, remain on the VDL for up to 12 hours, regardless of whether or not the Admin Time falls within the Start Time and Stop Time for the VDL Parameters in the BCMA main screen. For Continuous Inpatient medication orders with multiple administrations per day, once a LATE dose has been given, any previous LATE doses that continue to display on the VDL cannot be given, i.e., scan option is no longer available. The medication can still be marked as Held or Refused, Comments added, etc.
- If the next action for a Continuous Inpatient medication order for a medication requiring removal is for it to be Removed, but is late, the Next Dose Action column contains “LATE-RM” and the next Removal Time as a date/time on a separate line, with all text in red font. The BCMA site parameter “Allowable Time Limits (In Minutes) After Scheduled Admin / Removal Time” is used as the basis for determining if the medication order is late for Removal.

> Note: This is not applicable to Clinic Orders, which are never designated as LATE-RM.

- Continuous Inpatient medication orders for medications requiring removal, when the Next Dose Action column contains “LATE-RM” and Removal Time, remain on the VDL for a period of time based on the Meds Requiring Removal (MRR) Display Duration site parameter, which is the number of days after the Stop Date for the order. If the value of the site parameter is Always Display (which how sites typically set it), the medication order continues to display on the VDL until it is marked as removed, regardless of the order Stop Date, even if the order is discontinued or expires, or the patient is discharged or re-admitted.

> Note: This is applicable to all medications that require removal, not just those with dosage form containing the word “PATCH”.

- If the next action for a PRN or On Call medication order is for it to be administered (i.e., Given), the Next Dose Action column is empty (i.e., blank). This applies to all Unit Dose medication orders, not just those for medications requiring removal.
- If the next action for a One Time medication order is for it to be administered (i.e., Given), the Next Dose Action column contains the word “DUE”, with no date/time. This applies to all Unit Dose medication orders, not just those for medications requiring removal.
- On the Unit Dose VDL in Inpatient Order Mode, the default sort order upon logging in to BCMA is in ascending order based on the date/time in the Next Dose Action column, so “older” items are at the top.
- Clinic Orders display on the VDL on the date of the patient’s appointment, regardless of Start Time for the medication order, so the medication can be administered if the patient arrives at the clinic earlier than their scheduled appointment time. This is for all Clinic Orders on all VDL tabs, not just those for medications requiring removal. The initial default sort order on the VDL (all 3 tabs) is based on the Clinic Location name.

## Unit Dose VDL Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rules for information included on the Unit Dose VDL tab are listed below.

- After a medication order for a medication requiring removal has been administered (i.e., Given), the medication order administration (i.e., row) stays on the VDL until it is marked as Removed (as it does currently when the Orderable Item has dosage form containing the word “PATCH”), whether or not the Removal Time falls within the Start Time and Stop Time for the VDL Parameters in the BCMA main screen.
- For a medication order for a medication requiring removal that has been administered (status = Given), if a user attempts to Mark the medication order as Removed when it is too early (i.e., before the scheduled Removal Time), a message dialog displays to alert the user as shown in Figure 4.

> ![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/005.png)

<span id="_Toc468870952" class="anchor"></span>Figure 4. Alert Message When User Attempts to Mark as Removed

> If the user enters a comment, the “OK” button is enabled, as shown in Figure 5. When the user clicks OK, the medication is marked as removed.

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/006.png)

<span id="_Toc468870953" class="anchor"></span>Figure 5. Alert Message When Comment Has Been Entered

# Viewing and Printing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Existing Report Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Existing report enhancements include:

- Removal times have been added where there are admin times for medications requiring removal (MRR)
- Both “Removal” and “Given” administration information is available for reporting.
- The new anatomic locations for MRRs are included in BCMA reports.
- The word “Injection Site” has been replaced with “Body Site” in report column headers that could include both Dermal Sites for MRRs and Injection Sites for non-MRRs.
- The word “Injection Site” has been replaced with “Dermal Site” when the orderable item for the medication order is an MRR for reports with one specific medication.

The following BCMA reports have been enhanced with this information.

- Medication Admin History (MAH)
- Missed Medications
- Admin Time
- Medication Log
- Medication History
- Due List
- Display Order
- Medication Variance Log
- Cover Sheet Report: Medication Overview
- Cover Sheet Report: Expired/DC’d/Expiring Orders
- Order Detail Report

## BCMA Report Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/007.png)

<span id="_Toc468870954" class="anchor"></span>Figure 6. Medication Administration History (MAH) Report

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/008.png)

<span id="_Toc468870955" class="anchor"></span>Figure 7. Missed Medications Report

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/009.png)

<span id="_Toc468870956" class="anchor"></span>Figure 8. Administration Times Report by Patient

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/010.png)

<span id="_Toc468870957" class="anchor"></span>Figure 9. Medication Log Report

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/011.png)

<span id="_Toc468870958" class="anchor"></span>Figure 10. Medication History Report

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/012.png)

<span id="_Toc468870959" class="anchor"></span>Figure 11. Due List Report

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/013.png)

<span id="_Toc468870960" class="anchor"></span>Figure 12. Display Order Report

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/014.png)

<span id="_Toc468870961" class="anchor"></span>Figure 13. Medication Variance Log Report

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/015.png)

<span id="_Toc468870962" class="anchor"></span>Figure 14. Cover Sheet Report: Medication Overview – Active Orders Report

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/016.png)

<span id="_Toc468870963" class="anchor"></span>Figure 15. Cover Sheet Report: Expired/DC’d/Expiring Orders Report

![Figure 16. Order Detail Report (With Removal Times)](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/017.png)

*Figure 16. Order Detail Report (With Removal Times)*

# Anatomic Location for Medication Administrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updates to the BCMA Site Parameter application and BCMA software reflect the addition of “Body Site” to include both Injection site and medications requiring removal.

## BCMA Site Parameter Application for Anatomic Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the BCMA Site Parameters application, on the Parameters tab, in the Misc. Options section, a new site parameter is created, called “Dermal Site History Max Days”. It displays directly below the existing “Injection Site History Max Hours” site parameter.

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/018.png)

<span id="_Toc468870964" class="anchor"></span>Figure 16. Example of new Dermal Site History Max Days Site Parameter

In the BCMA Site Parameters application, on the Default Answer Lists tab, a new default answer list with list name “Body Sites” is available, which will allow both Injection Sites (for injection type medications) and Dermal Sites (for medications requiring removal) to be defined in a single list.

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/019.png)

<span id="_Toc468870965" class="anchor"></span>Figure 17. Body Sites List on BCMA Site Parameters Application

> **NOTE:** click on an item in the list to highlight a location on the body (green dot.) Alternatively, when you click on a green dot, this will highlight an item in the list with a green checkmark.

Upon installation of the software for this project, no values are automatically populated in the new Body Sites default answer list. However, all items that are currently in the facility’s existing Injection Sites default answer list are copied over to the new Body Sites default answer list, with the Item name for each one the same, and with the Injection Site attribute automatically selected for each.

As part of the installation of the software, after the Injection Sites copy has completed, the facility’s existing Injection Sites default answer list is deleted, since it is no longer needed.

At the top of the Body Sites default answer list display (on the Default Answer Lists tab, with Body Sites list selected), the right-click menu contains the options to Add New, Delete, or Edit existing items.

When the “Edit Layout” button above the body diagram image is clicked, the Body Site Editor window displays. On the right side of the Body Site Editor window, the Name, Injection Site, and Dermal Site columns display, with the Name listed, and “Y” in the Injection Site and/or Dermal Site columns, based on the definition of the item in the list.

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/020.png)

<span id="_Toc468870966" class="anchor"></span>Figure 18. Body Site Editor Window for Body Sites Default Answer List

> **NOTE:** Once you are inside the Body Site Editor , you can click and drag items from the body diagram on the left over to the Body Sites List on the right. Once you associate an item on the diagram with an item on the list, the item will have a green check mark next to it. You can hover over items on the diagram to view the associated item. Darker circles on the body diagram indicate associated items on the list.

## User Screens for Anatomic Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a medication requiring removal (i.e., orderable item has “Prompt for Removal in BCMA” set to 1, 2, or 3) is being administered (Given), the user is prompted to select the Dermal Site, i.e., the location or position on the patient’s body where the medication is placed. A “Dermal Site Needed!” window displays, which is similar to the existing “Injection Site Needed!” expanded window that displays for injection type medications.

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/021.png)

<span id="_Toc468870967" class="anchor"></span>Figure 19. Dermal Site Needed! Window

In the Dermal Site Needed! window, the “Previous Dermal Sites” section contains the Dermal Site that was selected for the last 4 instances for the same orderable item for the medication requiring removal that is in the process of being administered (Given).

> **NOTE:** The Injection Site History option, which is available in the right-click menu for qualifying items on the Unit Dose and IVP/IVPB VDL, is renamed “Body Site History” to designate that this applies to both patches and injections.

The Due List menu option renamed as “Body Site History” is enabled if the item selected from the Unit Dose or IVP/IVPB VDL is a medication requiring removal. When the Body Site History option is selected for a medication requiring removal, the new Dermal Site History window displays.

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/022.png)

<span id="_Toc468870968" class="anchor"></span>Figure 20. Due List Menu Option for Body Site History When MRR Selected from VDL

When the Body Site History option is selected for a medication defined as an injection, the existing Injection Site History window displays.

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/023.png)

<span id="_Toc468870969" class="anchor"></span>Figure 21. Due List Menu Option for Body Site History When Injection Selected from VDL

In the Dermal Site History window that displays for medications requiring removal when either the Body Site History right-click or Due List menu option is selected, the “Previous Dermal Sites” section contains the Dermal Site that was selected for the last 4 instances for the same orderable item for the medication requiring removal that is in the process of being administered (Given).

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/024.png)

<span id="_Toc468870970" class="anchor"></span>Figure 22. Dermal Site History Window

The Scan IV window that displays when IV medications are being administered contains a Select an Injection Site field, which now displays items from the Body Sites default answer list that are defined as Injection Site, instead of from the now-defunct Injection Sites default answer list.

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/025.png)

<span id="_Toc468870971" class="anchor"></span>Figure 23. Scan IV Window with Select an Injection Site Field

If the medication order being edited in the Edit Med Log window is for a medication that is defined as a medication requiring removal (i.e., orderable item has “Prompt for Removal in BCMA” set to Yes), and the medication has been administered, e.g., status is Given or Removed, and a Dermal Site was selected, the field is labeled as “Dermal Site”, and the drop-down list displays items from the Body Sites default answer list that are defined as Dermal Site.

![](psb-3-83-87-or-3-417-clinical-ancillary-services-cas-inpatient-medication-admini/026.png)

<span id="_Toc468870972" class="anchor"></span>Figure 24. Edit Med Log Window with New Dermal Site Field Enabled

## Clinic Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinic Orders display on the VDL on the date of the patient’s appointment, regardless of Start Time for the medication order, so the medication can be administered if the patient arrives at the clinic earlier than their scheduled appointment time. This is for all Clinic Orders, not just those for medications requiring removal. Clinic Orders with specific Admin Time(s), the order displays on the VDL <u>and</u> is available for administration based on the Expected First Dose for the Start Date. The initial default sort order on the VDL (all 3 tabs) is based on the Clinic Location name.

# User Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation distributed with this project includes the following and may be retrieved from the VistA Documentation Library (VDL) on the Internet at the following link: [Pharm: Bar Code Medication Administration (BCMA)](http://www.va.gov/vdl/application.asp?appid=84).

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
<td>PSB_3_UM_CHAPTERS_1_thru_6_R1216.PDF</td>
<td><p>BCMA V.3.0 GUI User Manual – Chapters</p>
<p>1 through 6</p></td>
</tr>
<tr class="even">
<td>PSB_3_UM_CHAPTERS_7_thru_13_R1216.PDF</td>
<td><p>BCMA V.3.0 GUI User Manual – Chapters</p>
<p>7 through 13</p></td>
</tr>
<tr class="odd">
<td>PSB_3_MAN_UM_R1216.PDF</td>
<td>BCMA V.3.0 Manager’s User Manual</td>
</tr>
<tr class="even">
<td>PSB_3_UM_NURSE_CHUI_R1216.PDF</td>
<td>BCMA V.3.0 Nursing CHUI User Manual</td>
</tr>
<tr class="odd">
<td>PSB_3_TM_R1216.PDF</td>
<td>BCMA V.3.0 Technical Manual/Security Guide</td>
</tr>
<tr class="even">
<td>PSB_3_P83_RN.PDF</td>
<td>Release Notes – BCMA V.3.0 (PSB*3*83)</td>
</tr>
</tbody>
</table>

# Associated Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Name (Number)               | Field Name (Number)                                                                   | New/Mod/Del |
|--------------------------------------|-------------------------------------------------------------------------------------------|-----------------|
| BCMA MEDICATION LOG (53.79)          | SCHEDULED REMOVAL TIME (.17)                                                              | New             |
|                                      | DERMAL SITE (.18)                                                                         | New             |
|                                      | ACTION DATE/TIME (.06)                                                                    | Mod             |
|                                      | SCHEDULED ADMINISTRATION TIME (.13)                                                       | Mod             |
| DISPENSE DRUG (53.795)               | PROMPT FOR REMOVAL IN BCMA (.06)                                                          | New             |
| BCMA MEDICATION VARIANCE LOG (53.78) | EVENT (.05) - Add a new code to the set of codes for the EVENT field: 4:EARLY/LATE REMOVE | Mod             |

# Associated Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Form Name    | File Name (Number)      | New/Mod/Del |
|------------------|-----------------------------|-----------------|
| PSB MED LOG EDIT | BCMA MEDICATION LOG (53.79) | Mod             |
| PSB NEW UD ENTRY | BCMA MEDICATION LOG (53.79) | Mod             |

# Associated Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name        | Type | New/Modified/Deleted |
|------------------------|----------|--------------------------|
| PSB MGR                | Menu     | Modified                 |
| PSB GUI CONTEXT - USER | Broker   | Modified                 |

# Parameter Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Parameter Name          | New/Modified/Deleted |
|-----------------------------|--------------------------|
| PSB AL GROUPS               | New                      |
| PSB AL IMAGE GENERAL        | New                      |
| PSB AL IMAGES               | New                      |
| PSB AL MASTER LIST          | New                      |
| PSB LIST ANATOMIC LOCATIONS | New                      |
| PSB LIST BODY SITES         | New                      |

# Associated Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| RPC Name         | New/Modified/Deleted |
|----------------------|--------------------------|
| PSB COVERSHEET1      | Modified                 |
| PSB GETINJECTIONSITE | Modified                 |
| PSB GETORDERTAB      | Modified                 |
| PSB GETSETWP         | New                      |
| PSB MED LOG LOOKUP   | Modified                 |
| PSB TRANSACTION      | Modified                 |
| PSB VALIDATE ORDER   | Modified                 |

# Associated Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Template Name | Type | File Name (Number)       | New/Mod/Del |
|-------------------|----------|------------------------------|-----------------|
| PSB DIVISION      | KERNEL   | PARAMETER TEMPLATE (8989.52) | Mod             |

# Patient Safety Issue Corrections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Patient Safety Issue corrections are made with this patch:

- PSPO00000885: BCMA reports are misleading when patches are Removed depending on dates chosen to run the report <span class="mark">REDACTED</span>
- PSPO00001978: BCMA does not prompt user to remove a transdermal patch when the removal time differs from the next administration time.
- PSPO00002222: IV bag that should have been invalid due to provider comment changes was inadvertently made available for infusion.
- PSPO00002333: BCMA Missed Medications report does not include orders with a status of "Renewed".
- PSPO00002803: Scanning of barcode on medication package focuses the default to the "OK" button and removes warning screen from view
- PSPO00003011: Inability to administer medications in clinic until exact appointment time may cause delay in medication administration or treatment. <span class="mark">REDACTED</span>

# Remedy Tickets Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Remedy Tickets were resolved with this patch:

| Name           | Description                                                                                 |
|--------------------|-------------------------------------------------------------------------------------------------|
| INC000000216580    | No "G" for a given patch dose                                                                   |
| INC000000218095(d) | Patch removal deletes original administration                                                   |
| INC000000960057    | Provider Comments IV Bag Parameter has no effect on IV Bag Administration                       |
| INC000000984066    | Orders with a Status of Renewed don't display on the Coversheet                                 |
| INC000001224198    | The "Invalid Medication Lookup" and "Scanned Drug Not Found" pop-ups have the focus set to "OK" |

# New Service Requests (NSRs) Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The project’s scope of changes includes addressing the following New Service Requests (NSRs) and Patient Safety issues:

- NSR 20141012: Pharmacy Safety Enhancements: <span class="mark">REDACTED</span>
- NSR 20120312: Create Reminder Mechanism to Remove Transdermal Medications: <span class="mark">REDACTED</span>
- NSR 20101105: Add Transdermal Patch Removal to BCMA Missed Med Report: <span class="mark">REDACTED</span>
  - PSPO00001978: BCMA does not prompt user to remove a transdermal patch when the removal time differs from the next administration time: <span class="mark">REDACTED</span>
- NSR 20110810: Transdermal Patch Documentation Disappears in BCMA: <span class="mark">REDACTED</span>
- NSR 20071011: Change Terminology for Injection Site: <span class="mark">REDACTED</span>
- NSR 20071004: Patch PSB\*3\*32 Pop Up Alert: <span class="mark">REDACTED</span>

# BCMA Online Help Update 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BCMA GUI Online Help system has been updated to include all released BCMA PSB\*3\*83 functionality.

# Installation Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation details are contained in the Patch Description.

## Patch PSS\*1\*191 Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*191 added the PROMPT FOR REMOVAL IN BCMA field (#12) to the ORDERABLE ITEM file (#50.7) with the ability to designate Orderable Items as Medications Requiring Removal using the following code values:

- NULL/0 = No Removal Required
- 1 = Removal at Next Administration
- 2 = Removal Period Optional Prior to Next Administration
- 3 = Removal Period Required Prior to Next Administration.

All Orderable Items except for items that contain dosage form Patch will have a NULL value for the new Prompt for Removal in BCMA (#12) field.

A post-install routine forces all Orderable Items containing dosage form Patch to automatically be set to Code Value 1 – Removal at Next Administration (No Medication-Free period between administrations).

A post-install report included in the patch install will produces a report consisting of a list of items from the Pharmacy Orderable Item File where the dosage form contains the word ‘Patch’ and the Prompt for Removal in BCMA field was set to 1 by the post-install routine. This report needs to be reviewed so that Pharmacy can make the changes in Pharmacy Orderable Item file, Prompt for Removal in BCMA field to correctly assign each Orderable Item that is an MRR to the correct code value.

## Patch PSJ\*5\*315 Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSJ\*5\*315 added the prompt for users to enter DURATION OF ADMINISTRATION based on the value stored in the PROMPT FOR REMOVAL IN BCMA field (#12) and then calculate and store the appropriate removal times.

Orders for MRRs with Removal Properties Report (MRR Active Orders Report) shows patients with orders that have Medications Requiring Removal (MRRs) that were Finished and Active prior to the install of patch PSJ\*5\*315.

A post-install report of information from the Orders for MRRs with Removal Properties Report will be produced immediately after the installation of the PSJ\*5\*315 patch and will be sent to the VistA Email addresses of users with the PSJI MGR, PSJU MGR, PSJU RPH, and PSJ RPHARM keys.