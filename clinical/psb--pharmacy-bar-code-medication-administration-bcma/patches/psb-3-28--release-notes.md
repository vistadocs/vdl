---
title: PSB*3*28 BCMA Version 3 Release Notes-Managing Scanning Failures (MSF)
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: BCMA Version 3 -Managing Scanning Failures (MSF)
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: active
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3*28
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - scan
  - unable
  - medication
  - bcma
  - table
  - contents
  - rights
  - patient
  - scanning
  - report
page_count: 0
word_count: 5885
section_count: 10
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p28_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)/psb_3_p28_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=84"
---

> ![](psb-3-28-bcma-version-3-release-notes-managing-scanning-failures-msf/001.png)

MANAGING SCANNING FAILURES IN BCMA (MSF)

RELEASE NOTES

PSB\*3\*28

####### 

January 2009

Office of Enterprise Development

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Install Notes](#install-notes)
  - [Dependencies](#dependencies)
  - [Required Preparation before Running PSB\3\28](#required-preparation-before-running-psb328)
    - [Server-side (VistA)](#server-side-vista)
    - [Client (GUI)](#client-gui)
  - [Installation Instructions](#installation-instructions)
- [New Features](#new-features)
  - [New Unable to Scan Options](#new-unable-to-scan-options)
    - [Unable to Scan Wristband](#unable-to-scan-wristband)
    - [Unable to Scan Medications](#unable-to-scan-medications)
  - [New Take Action on Bag option](#new-take-action-on-bag-option)
  - [New MailMan Notification Feature](#new-mailman-notification-feature)
  - [New Unable to Scan Reports](#new-unable-to-scan-reports)
    - [General Information](#general-information)
    - [Unable to Scan (Detailed) Report](#unable-to-scan-detailed-report)
    - [Unable to Scan (Summary) Report](#unable-to-scan-summary-report)
  - [New “5 Rights Override” Site Parameters](#new-5-rights-override-site-parameters)
    - [Rights Override for Unit Dose Administrations](#rights-override-for-unit-dose-administrations)
    - [Rights Override for IV Administrations](#rights-override-for-iv-administrations)
  - [New Limited Access Mode](#new-limited-access-mode)
    - [Features <u>not</u> available in Limited Access](#features-unotu-available-in-limited-access)
    - [Features available in Limited Access](#features-available-in-limited-access)
- [Summary of Change Control Board Rulings](#summary-of-change-control-board-rulings)
- [Known Issues](#known-issues)
This document provides a description of changes to the Bar Code Medication Administration (BCMA) software (patch PSB \*3\*28).
Previously, there was no way to track when and why bar code scanning was not used. The purpose of the Managing Scanning Failures (MSF) functionality is to encourage bar code scanning over manual entry, capture information on why scanning was bypassed, create reports that notify Pharmacy, Nursing and Performance Improvement Services of system issues that cause nurses to bypass scanning and to create problem alerts so they can be resolved in a timely manner.
The MSF functionality has been enhanced to provide users with an automated reporting method of bar code scanning failures of both patient wristbands and medication bar code labels. This will shorten the resolution time and allow for proactive analysis of the failure information, in order to prevent future scanning failures. This enhancement allows nurses to automatically notify staff of problems without disrupting their normal routine. This enhancement shall allow quantification of system issues so that performance improvement teams can target areas needing improvement and compare before and after results to determine if solutions were effective. The ability to ensure that safety checks in BCMA are used as intended – in support of the five rights of medication administration such that the nurse administers the right dose of the right medication in the right route to the right patient at the right time, will be improved.
With this release, a new mode of patient record access, Limited Access BCMA, is provided. The new mode of access allows medication administering users to gain access to BCMA without being at the patient’s bedside, to access patient records for non-medication administration documentation, review and reporting purposes, without having to scan patient wristbands.
The BCMA application along with bar code technology allows clinicians to document active medication administrations to patients at the bedside or other points of care. The Managing Scanning Failures functionality provides a streamlined process to continue working in the event of a scanning failure.

# Install Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Released patch PSB\*3\*43 must be installed prior to installing PSB\*3\*28.
- Released patch PSB\*3\*25 must be installed prior to installing PSB\*3\*28.

## Required Preparation before Running PSB\*3\*28

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps must be performed after installation, but before executing PSB\*3\*28.

### Server-side (VistA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Define a mail group in VistA for individuals who will receive MailMan message notifications for wristband and scanning failures. For example, you may include individuals from Pharmacy, Nursing, and Performance Improvement Services. Then enter the name of the group you created into the BCMA Parameters application under Mail Groups, Unable to Scan.
- Assign security key PSB UNABLE TO SCAN only to users who have the authority to access and run the MSF Unable to Scan reports. Check site policy to determine which users will be running Unable to Scan reports, such as BCMA Coordinators, Nurse Managers, etc.
- To ensure that the Unable to Scan reports correctly find and display data, verify the following:
  - Active nurse units in the NURS LOCATION file must be properly associated with their corresponding institution in the INSTITUTION file.
  - Active MAS wards in the WARD LOCATION file must be properly associated with their nurse units in the NURS LOCATION file.
  - Active users of BCMA must be properly associated to their corresponding institution by making sure that they are assigned to the correct division(s) in the NEW PERSON file.

### Client (GUI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Ensure that the BCMA 5 Rights Override parameters are checked in the BCMA Site Parameters application, IF you want users to be able to administer Unit Dose and IV medications via the Unable to Scan—Verify Five Rights option. Check your site policy to determine whether or not this feature will be used in your facility.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following are the instructions for installing the BCMA GUI client application, using the InstallShield program.

1.  Double-click on the InstallShield executable file, PSB3_0P28.exe. This will start the InstallShield Wizard, and the Welcome dialog displays, as shown in Figure 1. Be sure the title bar displays PSB\*3\*28. Click Next to continue.

    ![](psb-3-28-bcma-version-3-release-notes-managing-scanning-failures-msf/002.png)

    Figure 1 – InstallShield Wizard Welcome Dialog
2.  Select the Destination Folder in which to install the client application. Choose either the default location or click Change to install to an alternate destination folder. See Figure 2. Click Next to continue.

    ![](psb-3-28-bcma-version-3-release-notes-managing-scanning-failures-msf/003.png)

    Figure 2 – Choose Destination Folder
3.  Select the Setup Type of installation. The “Typical” option only installs the BCMA.EXE application. The Complete option will install all features, including the BCMA.EXE application and the BCMAPar.EXE application. The Custom option is rarely needed, but will allow you to check on disk space before the installation and select features to include or exclude. See Figure 3. Click Next to continue.

    ![](psb-3-28-bcma-version-3-release-notes-managing-scanning-failures-msf/004.png)

    Figure 3 – Choose Setup Type
4.  Click on the Install button to finish the installation process. See Figure 4.

    ![](psb-3-28-bcma-version-3-release-notes-managing-scanning-failures-msf/005.png)

    Figure 4 – Ready to Install
5.  The last step in preparing to run BCMA is to create a desktop shortcut (and similarly for BCMAPar if you use that program, too). You must edit the shortcut properties to include the server (S) and port (P) at the end of the Target field with the following syntax. See Figure 5.

    <u>Target Syntax</u>:

> “\<Path to BCMA.EXE\>\BCMA.exe” S=\<server IP address\> P=\<port number\>

<u>Target Example</u>:

> “C:\Program Files\vista\BCMA\BCMA.exe” S=1.2.3.4 P=9999

> Note: To create a desktop shortcut for the BCMA Parameters application, create a new shortcut and follow the example above, replacing BCMA.exe with BCMAPar.exe.

> ![Figure 5 – Example of the BCMA desktop shortcut](psb-3-28-bcma-version-3-release-notes-managing-scanning-failures-msf/006.png)

*Figure 5 – Example of the BCMA desktop shortcut*
showing server and port assignments

6.  After you start up BCMA, click Help on the menu bar and then click About. You will see the dialog shown in Figure 6.

![](psb-3-28-bcma-version-3-release-notes-managing-scanning-failures-msf/007.png)![Figure 6 – Help/About Screen for BCMA](psb-3-28-bcma-version-3-release-notes-managing-scanning-failures-msf/008.png)

*Figure 6 – Help/About Screen for BCMA*

7.  If you install BCMAPar, click Help on the menu bar and then click About. You will see the dialog shown in Figure 7.

    ![](psb-3-28-bcma-version-3-release-notes-managing-scanning-failures-msf/009.png)  
    Figure 7 – Help/About Screen for BCMAPar

# New Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following describes the new features and functionality included in patch PSB\*3\*28.

## New Unable to Scan Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Unable to Scan Wristband

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following changes and enhancements were added to the BCMA GUI to allow the user to document when a wristband scanning failure occurs:

- The “Patient Lookup” dialog was renamed to “Scan Patient Wristband” dialog.
- Upon opening BCMA or selecting the Open Patient Record command, the “Scan Patient Wristband” dialog displays.
- The Scan Patient Wristband entry field was removed, and a new “Unable to Scan” option was created for use when the nurse is unable to scan the patient’s wristband.
- A scanner status indicator displays whether the scanner is Ready (green) or Not Ready (red).
- An Enable Scanner button is provided to set the scanner to Ready status, when needed.
- Selecting the Unable to Scan option displays the Unable to Scan dialog box, which allows the user to select a required Unable to Scan Reason from a drop-down list, and enter an optional 150 character comment.
- Wristband scanning failure reasons are built into the system. Selections include:  
  Damaged Wristband, Scanning Equipment Failure, and Unable to Determine.
- After entering the Unable to Scan information, the user performs a patient lookup via the BCMA Patient Select dialog, and then confirms the patient’s identity. During an Unable to Scan event, the nurse must confirm that two forms of patient identifiers were used by reading a new confirmation statement and checking the confirmation checkbox before BCMA will open the patient record.
- Upon opening a patient record using the Unable to Scan process, an “Unable to Scan event” is logged in a file, and a MailMan message is sent to the Unable to Scan mail group defined in the BCMA Site Parameters application.
- Discharged and deceased patients cannot be opened via scanning or unable to scan.
- Discharged and deceased patients can be opened only via Limited Access, Read-Only, and Edit Med Log.
- Attempts to open a discharged or deceased patient will not be counted on the Unable to Scan Summary report.

### Unable to Scan Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following changes and enhancements were added to the BCMA GUI to allow the user to document when a medication or IV bag scanning failure occurs:

#### General Information

- The Scan Medication Bar Code entry box was removed from the BCMA VDL.
- Menu options “Display Drug IEN” and “Available Bags” were removed from the system.
- Display of Drug IEN’s and Available Bag numbers were removed from pop-up messages, missing dose requests, and the Due List report.
- The “Unable to Scan” menu options are disabled for orders on Provider Hold, when the selected administration has a status of Given, and when operating BCMA in Read-Only and Limited Access modes.
- For PRN administrations, if an Unable to Scan event is cancelled at any point during the administration process, the PRN pain score will not be sent to the Vitals package.

#### Unit Dose / IV Push Orders

- For Unit Dose administrations, the “Drug IEN Code” option has been removed from the Due List and right-click menus and has been replaced with the “Unable to Scan” option.
- Selecting the Unable to Scan option displays the Unable to Scan dialog box, which displays administration information, and allows the nurse to select a required Unable to Scan Reason from a drop-down list, and enter an optional 150 character comment.
- Medication scanning failure reasons are built into the system. Selections include: Damaged Medication Label, Dose Discrepancy, No Bar Code, Scanning Equipment Failure, and Unable to Determine.
- After entering the Unable to Scan information, the Medication Verification dialog displays, where the nurse should first attempt to verify the medication in hand against the selected order.
  - The Verify Medication option allows the nurse to verify the medication being administered by typing a matching IEN or NDC from the bar code label of the medication package in hand
    - Upon entering a matching IEN or NDC number, the nurse can proceed with the medication administration.
    - When entering a bar code number, no letters, spaces or punctuation marks are allowed. For non-IV administrations, if the entry contains non-numeric characters, a warning message displays: “When typing a bar code, enter numeric values only (omit non-numeric characters).” Click OK to retry.
    - When the Verify Medication entry matches the medication or bag on the order, the following data are displayed in a scrolling text box: Dosage/infusion rate, Units/Dose, med route, and special instructions. This information assists the nurse in the verification process, especially for fractional and multiple dose orders.
    - If the number entered does not match the dispense drug being administered for the selected order, an “Invalid Medication – Do Not Give” error message displays.
    - If no match could be obtained, the bar code number is unreadable, or there is no bar code label, the Verify Five Rights option may be used.
    - Refer to your BCMA Coordinator and site policy for guidance on the use of the Verify Medication option and contacting Pharmacy to address bar code label problems.
  - The Verify Five Rights option allows the nurse to administer the medication without entering a matching IEN or NDC number.
    - The nurse must place a checkmark in each of the five checkboxes to document that the five rights of medication administration have been physically verified (right patient, right medication, right dose, right route, right time).
    - This option is only available if the Five Rights Override Parameter is enabled for Unit Dose medications in the BCMA Site Parameters application.
    - If the Five Rights Override Parameter is turned off, you will not be able to administer the medication.
    - Refer to your BCMA Coordinator and site policy for guidance on the use of the Verify Five Rights option.

#### IV Piggyback / IV Orders

- For IV Piggyback and IV orders, the “Unable to Scan” and “Unable to Scan – Create WS” options were added to the Due List menu and the right-click menu in the administration window.
- For IV Piggyback orders, the “Available Bags” option has been removed from the Due List and right-click menus and has been replaced with the “Unable to Scan” option.
- For IV orders on the IV tab, the “Unable to Scan” option is only available at the order level; it is not available at the IV bag level in the IV Bag Chronology window.
- For IV Piggyback and IV Administrations where the bag is labeled by Pharmacy, the nurse selects the administration/order then selects the “Unable to Scan” option.
- Selecting the Unable to Scan option displays the Unable to Scan dialog box, which displays administration information, and allows the nurse to select a required Unable to Scan Reason from a drop-down list, and enter an optional 150 character comment. Note that Bag ID field shows “N/A” since the bag number will not be known at that point in the workflow.
- Medication scanning failure reasons are built into the system. Selections include: Damaged Medication Label, Dose Discrepancy, No Bar Code, Scanning Equipment Failure, and Unable to Determine.
- After entering the Unable to Scan information, the Medication Verification dialog displays, where the nurse should first attempt to verify the IV bag in hand against the selected order.
  - The Verify Medication option allows the nurse to verify the IV medication being administered by typing a matching IV bag number from the bar code label of the medication package in hand.
    - Upon entering a matching IV bag number, the nurse can proceed with the medication administration.
    - When entering a bag ID number, no spaces or punctuation marks are allowed. Entries are automatically forced to uppercase.
    - When the entry matches the bag ID number on the order, a confirmation box displays the additives and solutions, allowing the nurse to confirm the bag components before continuing.
    - If the number entered does not match the dispense drug being administered for the selected order, an “Invalid Medication – Do Not Give” error message displays.
    - If no match could be obtained, the bar code number is unreadable, or there is no bar code label, the Verify Five Rights option may be used.
    - Refer to your BCMA Coordinator and site policy for guidance on the use of the Verify Medication option and contacting Pharmacy to address bar code label problems.
  - The Verify Five Rights option allows the nurse to administer the IV medication without entering a matching IV bag number.
    - The nurse must place a checkmark in each of the five checkboxes to document that the five rights of medication administration have been physically verified (right patient, right medication, right dose, right route, right time).
    - This option is only available if the Five Rights Override Parameter is enabled for IV medications in the BCMA Site Parameters application.
    - If the Five Rights Override Parameter is turned off, you will not be able to administer the medication.
    - Refer to your BCMA Coordinator and site policy for guidance on the use of the Verify Five Rights option.
- IV bags marked as Held, Refused, and Missing Dose can be set to the Infusing state via scanning and via the Unable to Scan process.
- When selecting Unable to Scan on the last Infusing pharmacy bag on an IV order, the user is prompted to complete the bag, and fill out the IV Scan dialog, then is returned to the VDL. No additional Unable to Scan event is logged for completing the bag.

#### Ward Stock (IV and IVPB) Orders

- For Ward Stock (IV and IVPB) orders that have bag components that do not scan, the user can select “Unable to Scan – Create WS” from the Due List menu and the right-click menu.
- The Unable to Scan dialog displays first, allowing the nurse to select a required Unable to Scan Reason from a drop-down list, and enter an optional 150 character comment.
- The Ward Stock window then displays, instructing the user to type the IEN/NDC from the bar code label of each additive and solution that will not scan, while ignoring all non-numeric characters on the bar code label. The user is instructed to press Enter after each item, and when all desired additives and solutions are listed, to click OK.
- The user can also attempt to scan the additive and solution bar codes (that will scan) into the Ward Stock window.
- In the event that the user (forgets to press Enter and instead) clicks OK while an IEN or NDC number is still displayed in the scan bar code field, the OK button will automatically function as an Enter key. If there is no number in the scan bar code field, the OK button functions normally.
- Administering a Ward Stock IV order via Unable to Scan – Create WS logs only ONE Unable to Scan event. Unlike the Multiple/Fractional Dose window, the Ward Stock window does NOT supply an Unable to Scan button for each additive and solution.
- IEN/NDC entries typed in the Ward Stock IV window do NOT count towards scanner bypass keyed entry totals.
- The Five Rights Override feature is <u>not</u> available for Ward Stock IV orders.

## New Take Action on Bag option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The previous “Take Action on WS” option, which only applied to Ward Stock bags, has been replaced by the “Take Action on Bag” option.

- Take Action on Bag can be applied to any Infusing or Stopped IV bag, whether delivered from Pharmacy or Ward Stock.
- This option is only available on the IV tab of the BCMA VDL. It displays on both the right-click menu and the Due List menu whenever a Stopped or Infusing bag is highlighted in the IV bag chronology window.
- Selecting Take Action on Bag displays the IV Scan dialog, allowing the user to perform one of the following actions:
  - To document an Infusing bag as Stopped or Completed.
  - To document a Stopped bag as Infusing or Completed.
- Advantages of the Take Action on Bag option:
  - User can Stop or Complete an Infusing bag without having to rescan the IV bag.
  - If an IV bag will not scan, using Take Action on Bag allows the user to avoid logging duplicate Unable to Scan events each time an action is taken on an IV bag that cannot be scanned.
- Alternatively, if the Unable to Scan option is used to Complete or Stop an Infusing bag (instead of using Take Action on Bag), an Unable to Scan event will be logged and a notification email will be sent.

## New MailMan Notification Feature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A new MailMan notification feature was developed to assist in tracking and troubleshooting wristband and medication bar code scanning failures without interrupting the administration workflow.
- When the user logs an “Unable to Scan” event, a MailMan message is sent to a new mail group specified in the BCMA Site Parameters application.
- The subject line of the message indicates whether it is a wristband or medication scanning failure.
- The body of the message contains user name, date/time of event, patient name and last four digits of the SSN, order number, ward location/room, type of bar code issue, medication, reason for scan failure and user’s comment.
- Unit Dose orders will display dispense drug, Drug IEN, and dosage ordered.
- IV Orders will display Unique ID (Bag ID typed by User or Wardstock) and orderable item.
- Whenever the Five Rights Override is utilized, a system generated comment will be included with the user comment, indicating that the Five Rights Override was used for a particular administration.

## New Unable to Scan Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new scanning failure reports were created to help sites identify areas for process improvement and education.

### General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Unable to Scan Detailed and Summary reports are only available on the BCMA GUI Reports menu. These reports are not available through the BCMA VistA menu interface.
- Only users holding the new PSB UNABLE TO SCAN security key can see and access the Unable to Scan reports from the BCMA Reports menu.
- Unable to Scan reports are filtered by the user’s division, i.e., the division the user selected upon logging into BCMA. This is most useful to large, integrated sites. If a BCMA Coordinator has access to multiple divisions, s/he can select the desired division then run the Unable to Scan reports. The user’s division will print on the report header.
- Note that the division filtering feature does not apply to printing by Ward (user-selected Ward or Nurse Unit) and does not affect the Ward drop down list.
- These reports can be run without having a patient record open on the VDL.
- Data for a wristband scanning failure is logged after you complete the Unable to Scan process and successfully select, confirm, and open the patient record.
- Data for a medication scanning failure are logged after you complete the Unable to Scan process and complete all steps of the medication administration. Canceling out of the Unable to Scan process or canceling a medication administration at any point in the process will not log the Unable to Scan event.
- A new “Exclude MAS Wards” checkbox has been added to both Unable to Scan report dialogs. This option filters out the MAS Wards from the Ward drop-down list, making it easier to select a Nurse Unit from the drop down list. This checkbox is selected by default.
- User-specified report criteria prints on the report header.
- Nurse unit names may be preceded by “NUR” on the report headers, e.g., NUR GEN MED, This is a function of the file, not BCMA.
- Note that the “Print Selected Patients on Ward” option on other BCMA reports is not applicable to Unable to Scan reports, and is therefore not available.
- Output options include:
  - Preview: View report on-screen, then Print or Cancel.
  - Print: Print directly to printer, with option to Queue Report to print a later time.

### Unable to Scan (Detailed) Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Provides detailed information for each scanning failure logged via Unable to Scan functionality.
- This report can be run without having a patient record open on the VDL.
- This report is only accessible to users with the PSB UNABLE TO SCAN security key.
- The following information is included in the report:
1.  Patient Name
2.  Date/Time of UTS Event
3.  Location (Ward/Room-Bed)
4.  Type of Scanning Failure
5.  Drug Item (ID#)
6.  User’s Name
7.  Reason for UTS
8.  Comments (System and/or User)
- At report run-time, the user may specify the following criteria.
1.  Start Date, Stop Date
2.  Start Time, Stop Time
3.  Type of Scanning Failure
4.  Unable to Scan Reason
5.  Report selection options:
- All Wards/Patients
- Ward (user selected Ward or Nurse Unit)
  - Exclude Inactive Wards (checked): Filters out the Inactive Wards and Nurse Units from the Ward drop-down list
  - Exclude MAS Wards (checked): Filters out the MAS Wards from the Ward drop-down list
6.  Sort criteria: Choose up to three levels of sort fields (Primary/Second/Third).
- The defaults for the Unable to Scan (Detailed) dialog are as follows:
  - Start Date/Time is (Today-6)@0001
  - Stop Date/Time is Today@2400
  - All Scanning Failures
  - All Reasons
  - All Wards/Patients
  - Primary sort only, by Date/Time of Scanning Failure (Ascending). The Date field can be sorted in Ascending or Descending order.
- The report will begin searching for Unable to Scan events that occurred on or after the Start Date @ Start Time specified and will stop searching for Unable to Scan events that occurred before or on the Stop Date @ Stop Time specified. To run this report for a single shift, the user can specify a time range within a particular day, or across two days, e.g., 01/01/2009@2000 through 01/02/2009@0800.
- For IV orders with multiple additives/solutions, only the first orderable item displays on Unable to Scan Detailed report and the Unable to Scan MailMan message.
- Whenever the Five Rights Override is utilized, a system generated comment will be included with the user comment, indicating that the Five Rights Override was used for a particular administration.

### Unable to Scan (Summary) Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Provides the total number and percentages of wristbands scanned, wristbands by-passed, medications scanned, and medications by-passed.
- Note that all scans are counted in the Summary report, whether or not an administration is cancelled at any point in the process.
- Use of Undo Given or status changes made in Edit Med log or Manual Medication Entry will not subtract from counts or change results previously displayed on Unable to Scan Detailed or Summary reports.
- The following information is included on the report:
1.  Wristband Totals (counts and percentages)
    1.  Processed via Scanner
    2.  Processed via Scanner By-Pass (includes Unable to Scan events and keyed entries.)
2.  Medication Label Totals (counts and percentages)
    1.  Processed via Scanner
    2.  Processed via Scanner By-Pass (includes Unable to Scan events, keyed entries, and VistA Manual Med Entries)
3.  Total Medications Scanned
4.  Total Medications Bypassed
- At report run-time, the user may specify the following criteria.
1.  Start Date, Stop Date
2.  Start Time, Stop Time
3.  Report selection options include:
- Entire facility (1 page report): This (default) option prints a one-page summary report for the entire facility.
- Nurse Unit/Location (1 Unit per page): Prints a summary page for each nurse unit in the facility.
- Ward (user selected Ward or Nurse Unit)
  - Exclude Inactive Wards (checked): Filters out the Inactive Wards and Nurse Units from the Ward drop-down list
  - Exclude MAS Wards (checked): Filters out the MAS Wards from the Ward drop-down list
- The defaults for the Unable to Scan (Summary) dialog are as follows:
  - Start Date/Time is (Today-6)@0001
  - Stop Date/Time is Today@2400
  - Entire Facility
- The report will begin searching for events that occurred on or after the Start Date @ Start Time specified and will stop searching for events that occurred before or on the Stop Date @ Stop Time specified. To run this report for a single shift, the user can specify a time range within a particular day, or across two days, e.g., 01/01/2009@2000 through 01/02/2009@0800.
- By design, the Unable to Scan Summary report includes and displays blank and inactive Nurse Units, if there are Unable to Scan events registered for those units.
- By design, the Unable to Scan Summary report tracks all wristband scans, even scanned events that do not match any valid Social Security Number (SSN), e.g., a wristband with an invalid SSN. When printing the Summary report by Nurse Unit, the report will include a page with a placeholder nurse unit, called “Unidentifiable Patient,” in order to track these erroneous wristband scans.

## New “5 Rights Override” Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new “5 Rights Override” parameters were added to the BCMA GUI Site Parameters application as part of the Managing Scanning Failures functionality.

- There are two new parameters: 5 Rights Override for Unit Dose administrations and a 5 Rights Override for IV administrations.
- These parameters display as checkboxes with a default setting of not selected.
- When selected, these parameters enable the “Verify 5 Rights” option during the Unable to Scan Medication Verification step for the type of administration selected (Unit Dose or IV).
- Enable the BCMA 5 Rights Override parameters ONLY IF your nurses will be permitted to administer Unit Dose and/or IV medications via the Unable to Scan—Verify Five Rights option.
- Before implementing this feature, check your site policy to determine whether or not this feature will be used in your facility.
- If these parameters are not selected at your facility, and the nurse is unable to scan a medication and unable to type a matching bar code number in order to verify the medication in hand, BCMA will not allow the administration to be documented as Given.

### Rights Override for Unit Dose Administrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the “5 Rights Override for Unit Dose Administrations” checkbox is selected, a site is allowed to control the Unable to Scan verification process of Unit Dose medications, permitting a nurse to proceed with a unit dose administration by verifying the 5 rights of medication administration -- without typing a matching bar code number.

### Rights Override for IV Administrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the “5 Rights Override for IV Administrations” checkbox is selected, a site is allowed to control the unable to scan verification process or IV medications permitting a nurse to proceed with an IV administration by verifying the 5 rights of medication administration without typing a matching Bag ID number.

## New Limited Access Mode

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new mode of patient record access, called “Limited Access,” was developed to allow users to access BCMA without being at the patient’s bedside and to access patient records for non-medication administration documentation, review, and reporting purposes without having to scan patient wristbands.

- The Limited Access option is available on the File Menu.
- All users, except those with PSB READ ONLY security keys, can select the Limited Access option.
- Upon selecting this option from the File Menu, the Patient Select dialog box displays, allowing the user to search for a patient by patient name, social security number, room-bed, or ward.

### Features <u>not</u> available in Limited Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Administration of a medication via scanning. The scanner status remains in a Not Ready state whenever a patient record is opened in BCMA Limited Access mode.
- Administration of a medication via Unable to Scan functionality. The Unable to Scan and Unable to Scan—Create WS options will be disabled.
- Modification of any IV or Ward Stock IV administration. Unable to Scan, Unable to Scan—Create WS, and Take Action on Bag options will be disabled.
- Marking a patch as Removed. The option to mark a patch as Removed will be disabled.
- Use of the CPRS Med Order button. The entry of an order via the CPRS Med Order button will be disabled.

### Features available in Limited Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Unit Dose, IVP/IVPB, and IV medication tabs display the patient’s Virtual Due List.
- The Edit Med Log option.
- All options within the File, View, Reports, Tools, and Help menus.
- BCMA Patient Record Flag functionality.
- Patient demographics.
- The ability to view allergies from the Allergies button.
- Virtual Due List Parameters and Schedule type selections.
- Adding a comment to an administration via any Add Comment option.
- Marking appropriate administrations as Held or Refused.
- Marking a Given Administration as Undo Given.
- Submitting a Missing Dose Request via any Missing Dose option.
- Documenting PRN Effectiveness through the right-click menu, Due List menu, and via BCMA Clinical Reminders.
- All BCMA reports by patient and by ward.
- All Due List menu options except for Take Action on Bag and Unable to Scan options.
- All IV medication tab options within the IV Bag Chronology tree view, except for Take Action on Ward Stock and Unable to Scan options.
- The Cover Sheet tab.

# Summary of Change Control Board Rulings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Change Requests were implemented:

- An entry field is provided for the user to type the human readable medication number from the bar code label in order to verify the medication being administered. \[per CCB ruling on CR#4\]
- The Drug IEN or synonym is not displayed within the Unable to Scan dialog box. \[per CCB ruling on CR#4\]
- The list of available bags is not displayed. \[per CCB ruling on CR#4\]
- The Multiple Dose dialog displays, with an Unable to Scan button to the right of each dispense drug where no action has been taken on the drug. \[per CCB ruling on CR#5\]
- In the Multiple Dose dialog, the Unable to Scan button no longer displays after a successful scan, or when the Unable to Scan process has been completed successfully for that dispense drug. \[per CCB ruling on CR#5\]
- An instruction displays on the Ward Stock dialog box, instructing the user to enter numeric values only (and omit non-numeric characters). \[per CCB ruling on CR#7\]
- Two new BCMA “5 Rights Override” site parameters were added for Unit Dose medications and IV medications. If these parameters are set, an override mechanism allows the nurse to document that the five rights of medication administration have been physically verified (right patient, right medication, right dose, right route, right time) and continue with the medication administration within the existing workflow – without entering a matching bar code number of the medication and/or bag. \[per CCB ruling on CR#4\]

# Known Issues 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Due to variations in scanner models and speed settings, long NDC numbers may register erroneously as keyed entries on the Summary report. If this becomes a problem, the BCMA Coordinator and IRM personnel can opt to use a new command line parameter to alter the algorithm that detects keyed entries. More information on this can be found in the Manager’s User Manual.
- Under certain conditions, a blank page is printed at the end of the Unable to Scan detailed report.
- PSB\*3\*32 defect: an IVPB order that is reversed with Undo-GIVEN and re-infused will not display the injection site popup although the order will be marked as given.
- PSB\*3\*32 defect: In the PRN Overview report, the patient’s age appears as a negative number.