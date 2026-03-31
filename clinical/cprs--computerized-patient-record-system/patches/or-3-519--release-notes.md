---
title: OR*3*519 31MA Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 31MA
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*519
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - pdmp
  - cprs
  - table
  - contents
  - patient
  - release
  - issues
  - notes
  - associated
  - query
page_count: 0
word_count: 1430
section_count: 7
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/OR_3_0_519_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/OR_3_0_519_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

---
title: <span id="_Toc205632711" class="anchor"></span>Computerized Patient Record System
---

CPRS v31MA COMBINED BUILD 1.0

(OR\*3\*519, GMRC\*3\*145, TIU\*1\*328, GMTS\*2.7\*134)

Release Notes

![](or-3-519-31ma-release-notes/001.png)

November 2020

Office of Information & Technology (OI&T)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Audience](#audience)
- [# New Features](#new-features)
    - [Prescription Drug-Monitoring Program (PDMP)](#prescription-drug-monitoring-program-pdmp)
    - [Decision Support Tool](#decision-support-tool)
  - [Patient Safety Issues](#patient-safety-issues)
  - [Known Issues](#known-issues)
  - [Remote Procedures Associated](#remote-procedures-associated)
  - [Parameter Definitions Associated](#parameter-definitions-associated)
  - [Parameter Templates Associated:](#parameter-templates-associated)
- [Defects](#defects)
- [Product Documentation](#product-documentation)
This multi-patch CPRS v31 MA COMBINED BUILD 1.0 Release Notes describes new features, enhancements to existing features, and defect corrections to the CPRS v31 Mission Act (MA) software which includes the following patches:
| Application/Version            | Patch      | Description                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Order Entry/Results Reporting v3.0 | OR\*3.0\*519   | This CPRS enhancement to support Prescription Drug-Monitoring Program (PDMP) integration will allow for more efficient and effective team-based care when prescribing controlled substances to Veterans, by providing ad-hoc PDMP queries for retrieving the data, results, and automatic generation of a progress note for the medical record. |
| Text Integration Utilities v1.0    | TIU\*1.0\*328  | This patch installs a new Document Class entitled PDMP TITLES and a new Document Title entitled STATE PRESCRIPTION DRUG MONITORING PROGRAM.                                                                                                                                                                                                     |
| Consult/Request Tracking v3.0      | GMRC\*3.0\*145 | This GMRC patch facilitates the DST integration by adding new data values to the consult ordering process and the necessary routine enhancements.                                                                                                                                                                                               |
| Health Summary v2.7                | GMTS\*2.7\*134 | This patch adds the following new health summary components: PDMP AOD ALL to return Accounting of Disclosures for PDMP queries                                                                                                                                                                                                                  |
Patches (OR\*3.0\*519, TIU\*1.0\*328, GMRC\*3.0\*145, and GMTS\*2.7\*134) are being released in the Kernel Installation and Distribution System (KIDS) multi-package build CPRS V31MA COMBINED BUILD 1.0.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of CPRS v31MA COMBINED BUILD 1.0 release and applies to the changes made between this release and any previous release for this software.

For each patch in this multi-patch release, the following sections provide a summary of the new features, enhancements and modifications to the existing software, defects, and any known issues.

# # New Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Prescription Drug-Monitoring Program (PDMP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Prescription Drug-Monitoring Program (PDMP) integration allows for more efficient and effective team-based care when prescribing controlled substances to Veterans by providing an ad-hoc PDMP query for retrieving data and the automatic generation of a progress note for the medical record.

This enhancement to CPRS will enable authorized users (prescribers and pharmacists) and licensed delegates to submit (on demand), PDMP queries for use in patient care related decision making and automatically update patient medical records and notes:

- View and retrieve controlled substance prescription monitoring data from external sources and within patients electronic medical records
- Automatically generate patient progress notes
- Query and easily utilize prescription and patient prescription history on an ad-hoc and recurring basis
- Perform audit functions that ensure compliance

> **NOTE:** At the time of national release, not all States are participating in the automated CPRS PDMP query process. If the State where VA care is being provided is not yet participating, the following message will be displayed when initiating a PDMP query from CPRS:

> The PDMP functionality using CPRS from the user’s Facility \[division name\] is currently unavailable due to state-specific legislation in \[2-letter state code\]. Coordinators at your facility will notify facility staff when this functionality is permitted. Please access your State PMP Portal to initiate a manual PDMP query.

On the REDACTED, a link displays showing which States are currently able to use this functionality. It will be updated as new States participate.

![](or-3-519-31ma-release-notes/002.png)

In this example, the PDMP Button is displayed on the Ribbon Bar

<u>PDMP Process</u>

1.  Select the PDMP Query button. If you are a delegate, select an authorized user from the "Select Authorized User list, and then click "Accept."

> The PDMP button changes to "PDMP Cancel." This displays while the query is sent to the PDMP system outside of CPRS and the user waits for the results of the query to be filled.

2.  While the query is running in the background, the user can continue to work in CPRS.

> Note: The time it takes for this query search is out of CPRS' control.

3.  When the query results are available, the PDMP button changes to “PDMP Results.” Click the button and an additional dialog page opens for the user to review the results.

    Note: If encounter information has not been entered, the encounter information dialog will appear before the PDMP report is displayed. You must complete the encounter information dialog before proceeding.
4.  A form displays under the report, enter comments if needed.
5.  You will have the option to select "Cancel without Update" or "Done and Create Note."
6.  If you select Done and Create Note, a progress note is automatically generated. The note must be signed by the Authorized User, or if a Delegate initiated the query, the note must be signed by both the Delegate and an Authorized User.
7.  At this point, you have finished your review of the PDMP data and the button returns to the initial PDMP Query state.

> For specific information, please refer to the *CPRS v31MA User Manual (cprsguium.docx)*<u>PDMP Links</u>

CPRS Mission Act Training Resources:

REDACTED

Map of States Participation in Automated CPRS PDMP Query:

REDACTED

### Decision Support Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** At the time of national release, these new DST features of CPRS GUI are dormant and not enabled. Sites will continue to use their existing tools and processes regarding DST. These integrated features will be enabled in a future release of CPRS GUI.

The Veterans Health Administration (VHA) Office of Community Care created the real-time Decision Support Tool (DST) to help care providers and Veterans quickly review the criteria recommended in the VA Mission Act of 2018, determine whether a given Veteran is eligible and would be best served utilizing the Veterans Community Care Program, and document the decision rationale in the Veteran's health record.

The existing process will be modified so DST consult ordering can fully be completed within the Computerized Patient Record System (CPRS). The user interface will display on the *Order A Consult window in CPRS* and will be updated to include:

1.  A Launch DST button that is active for outpatient orders when the Consult to Service/Specialty, Urgency, and Clinically Indicated Date (CID) have been selected.
2.  A new message box located above the Launch DST button to provide status messages from the DST application.

## Patient Safety Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known issues for CPRS V31MA COMBINED BUILD 1.0.

## Remote Procedures Associated

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Remote Procedure Name</u> <u>New/Modified/Deleted</u>

ORPDMP CHCKTASK New

ORPDMP GETCACHE New

ORPDMP STOPTASK New

ORPDMP STRTPDMP New

ORPDMP VIEWEDREPORT New

ORPDMPNT MAKENOTE New

ORPDMPNT RECNTNOTE New

ORQQCN ISPROSVC Modified

ORWPT GET FULL ICN New

## Parameter Definitions Associated

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For further information, please see *Appendix E: - Parameters By Name in theCPRS Technical Manual: GUI Version.*

OR PDMP BACKGROUND RETRIEVAL

OR PDMP COMMENT LIMIT

OR PDMP COPY/PASTE ENABLED

OR PDMP DAYS BETWEEN REVIEWS

OR PDMP DELEGATION ENABLED

OR PDMP DISCLOSED TO

OR PDMP NOTE TEXT

OR PDMP NOTE TITLE

OR PDMP OPEN TIMEOUT

OR PERSON CLASS

OR PDMP POLLING INTERVAL

OR PDMP REVIEW FORM

OR PDMP SHOW BUTTON

OR PDMP TIME TO CACHE URL

OR PDMP TIMEOUT QUERY

OR PDMP TURN ON

OR PDMP USE DEFAULT BROWSER

## Parameter Templates Associated:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Parameter Template Name</u> <u>New/Modified/Deleted</u>

ORQQCN CTB ACTION ENABLE New

ORQQCN DST/CTB URL/SERVICES New

# Defects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  CPRS issues (a.k.a. Controlled substance order allowed without Dig Sig)

> <u>Problem</u>: Through a series of renewals and discontinues of a previously discontinued order for a controlled substance, it is possible for the order to be put through again without a digital signature.

> <u>Resolution</u>: After renewing an order, the orders list in CPRS is updated. This removes any "ghost" orders that could be pushed through without a digital signature.

3.  Postings window on CPRS Cover Sheet does not display postings dates

> <u>Problem</u>: The Postings pane of the Cover Sheet should display the posting and the date the posting was created. The redesigned Cover Sheet of CPRS GUI v31b inadvertently dropped the date column from the display.

> <u>Resolution</u>: The date column of the Postings pane has been restored.

4.  Supplemental O2 Flow Rate Missing from CPRS Cover Sheet Vitals Pane

> <u>Problem</u>: In CPRS v31a, the Vitals panel displayed the supplemental O2 flow rate. The redesigned Cover Sheet of CPRS GUI v31b inadvertently dropped the supplemental O2 flow rate from the display.

> <u>Resolution</u>: The Supplemental O2 flow rate display has been restored.

5.  Copy and paste error - Microsoft Skype and Note to Note

> <u>Problem</u>: With the copy/paste feature of CPRS v31b disabled, when pasting data from MS Skype into a note, the note text becomes locked and the text carries from patient to patient (note to note). It was also noted that when copying data from a note in CPRS, users were unable to paste that text into another note in CPRS.

> <u>Resolution</u>: The VA is transitioning from MS Skype to Teams, which will prevent users from experiencing this issue as Teams does not create the same condition with pasting into a note as found in Skype. The CPRS GUI code was also updated to prevent this sort of condition again should another application present the same environment.

6.  List index out of bounds error when processing mammogram result view alerts

> <u>Problem:</u> When processing alerts through the 'old mammogram results' (pre-SMART) alert process, A 'List index out of bounds' access violation can occur. When using the SMART process, these errors are not occurring.

> <u>Resolution:</u> The CPRS GUI code was updated to remove the condition that would cause a list index out of bounds error when trying to process the alert.

7.  List index out of bounds error when trying to process deferred alert

> <u>Problem</u>: A deferred alert was not being properly removed from the list of alerts used by the CPRS GUI code. After deferring an alert and then clicking "Process All" a list index out of bounds error would occur.

> <u>Resolution</u>: The CPRS GUI code was updated to properly account for deferred in alerts. After deferring an alert, and then clicking the "Process All" button for remaining alerts, users are taken into the patient chart as expected.

8.  CPRS order menus do not remember size and position.

> <u>Problem</u>: The order menu windows in CPRS GUI are often reported to open in unexpected locations, and do not remember location or size when moved or resized. Users reports described various outcomes such as the "Done" button being pushed off the visible screen and also the order menus opening over top of information the user needed to see (e.g. referencing patient age when ordering labs).

> <u>Resolution</u>: CPRS order menus will now remember both size and position.

> Note: users that open CPRS on different computers that have monitors/screens with different size and/or resolution, may still experience order menus opening in unexpected locations. For example, using CPRS on a computer with a large monitor one day, and then opening CPRS on a laptop with a smaller screen on the following day would be one such situation that may place the order menu in an unsatisfactory location.

9.  SMART dialog not opening when processing all alerts

> <u>Problem</u>: When selecting a group of alerts on the patient selection screen of CPRS GUI, and that list includes a SMART alert, when the SMART alert is processed, the SMART dialog does not open and processing continues to the next alert

> <u>Resolution</u>: Changes have been made to alert processing from the patient selection screen, specifically when processing multiple alerts at a time. Prior to these changes, long text alerts and SMART alerts would process first, before any other alerts. And these two types of alerts were processed from the patient selection screen, before alert processing took you to the chart for any other alert type. Processing multiple alerts from the patient selection screen will now process them in order, moving from one alert to the next using the Next button in the bottom right corner of the screen. Note that processing alerts from the View Patient Notifications dialog has not changed - since that dialog will only process one alert at a time, the existing functionality was sufficient:

1.  Processing long text alerts tied to a patient (tickler alerts) will now take the user to that patient in the chart, going to the default user tab, or the current tab if the user is set up to use the last selected tab on patient change.
2.  Processing SMART alerts will now take users to the Notes tab in the patient chart before prompting if the user wishes to create a new note or make an addendum to an existing note.
3.  When processing multiple alerts, and any of those alerts take the user outside the patient selection screen, any long text alerts—which are not tied to a patient and are created by using the VistA XQALERT MAKE option—will now be processed within the patient chart, with no patient selected. When closing the long text alert dialog, users will be required to either process the next alert, or to stop processing alerts and return to the patient selection dialog - i.e. users will not be allowed to explore CPRS without a patient selected.
10. Support Integer Division IDs for Reminder Assignments

> <u>Problem</u>: When a site's division ID contains a decimal point, it was excluded from the list of available divisions when trying to build the list of CPRS GUI Cover Sheet reminders.

> <u>Resolution</u>: The CPRS GUI code was updated to account for a decimal point in a site division ID.

11. Vitals Pane Date/Time Display is Truncated on CPRS Cover Sheet

> <u>Problem</u>: The Vitals pane cuts off the time portion of the date/time display column. The column could be widened, but that was only temporary and would be reset whenever the patient information was refreshed or a new patient was selected.

> <u>Resolution</u>: The time portion of the date/time display column is no longer cut off. Selecting a new patient or refreshing patient information will not reset the column display width and cut off the time display.

12. CPRS Issues When Copying/pasting into Note Templates and Editing Notes

> <u>Problem</u>: Seemingly random access violations were occurring in CPRS when copying and pasting text into note templates, and also when editing notes.

> <u>Resolution</u>: Two issues were corrected in CPRS GUI with the exception logging code and the code that scrubs the clipboard.

13. Women's Health Cover Sheet Form Does Not Report Error

> <u>Problem</u>: After entering data via the Women's Health - Pregnancy and Lactation Status Update form on the Cover Sheet tab, if an error occurs in VistA while saving the data, that error message is not displayed to the user. In this scenario, the error message should appear explaining why the data was not saved.

> <u>Resolution</u>: CPRS was updated to display the error message if one is received from VistA upon saving the new pregnancy and/or lactation status.

14. Women's Health Panel Shows Not Applicable Instead of Error

> <u>Problem</u>: Given a female patient between the ages of 10 and 52, when an error occurs in retrieving the data for the Women's Health panel on the Cover Sheet, the panel shows Not Applicable. When the phrase Not Applicable is clicked on, a Detail dialog does not appear. An example error message is "Could not determine applicability; Reminder definition does not exist". In this situation, the Women's Health Panel should show Error instead of Not Applicable and when the word Error is clicked, the detail dialog should appear containing the error message.

> <u>Resolution</u>: CPRS was updated to display the word Error rather than Not Applicable in the Women's Health panel and to display the error message in the Details dialog that appears when the word Error is clicked on.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to standardized software document changes and VDL updates, the CPRSv31MissionAct documentation will be released and stored with the software on the sFTP site for 45 day compliance period. The documents will then be loaded and stored on the VDL. The documents and manuals may be downloaded from [REDACTED](https://download.vista.med.va.gov/index.html/SOFTWARE).

The following documents apply to this release:

<u>Documentation Title</u> <u>Filename</u>

CPRS Technical Manual: GUI Version CPRSGUITM.PDF

CPRS User Guide: GUI Version CPRSGUIUM.PDF

CPRS Technical Manual CPRSLMTM.PDF

CPRS GUI v.31 MA (Patch OR\*3.0\*519) OR_30_519_RN.PDF

Release Notes

CPRS GUI v.31 MA Installation Guide OR_30_519_DIBR.PDF

Consult/Request Tracking Technical Manual constm.pdf

Consult/Request Tracking User Manual consum.pdf

Text Integration Utilities Technical Manual TIUTM.PDF

Health Summary User Manual HSUM_2_7_UM.PDF

These CPRS documents can be found in the VA Software Document Library (VDL) at:  
<https://www.va.gov/vdl/application.asp?appid=62>