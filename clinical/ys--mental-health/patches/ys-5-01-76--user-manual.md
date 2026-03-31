---
title: YS*5.01*76 Mental Health Assistant Phase 2 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Mental Health Assistant Phase 2
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01*76
group_key: "YS:YS:5.01"
file_numbers: []
security_keys: []
menu_options: 2
description: The primary goal is to make the VistA Mental Health Package (MHP) V. 5.01, an effective and more efficient tool for use by mental health clinicians and patients with the creation of a windows based application for the most commonly used options in the MHP. Currently the MHP is administered through V
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - health
  - mental
  - test
  - assistant
  - contents
  - window
  - example
  - tests
  - manual
page_count: 0
word_count: 23875
section_count: 19
table_count: 87
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: JUNE 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys50176_mha2_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys50176_mha2_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/001.png)

MENTAL HEALTH ASSISTANT

VERSION 2 (MHA 2)

USER MANUAL

PATCH YS\*5.01\*76

JUNE 2003

V*ist*A Health System Design & Development

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [VistA Mental Health Assistant Version 2 (MHA 2) Software Application](#vista-mental-health-assistant-version-2-mha-2-software-application)
    - [Intended Audience](#intended-audience)
    - [MHA Version 2 User Manual Sections](#mha-version-2-user-manual-sections)
- [Orientation](#orientation)
  - [MHA Version 2 Documentation Retrieval Information](#mha-version-2-documentation-retrieval-information)
    - [MHA 2 Documentation Retrieval Locations](#mha-2-documentation-retrieval-locations)
    - [<span class="mark">REDACTED</span> VistA Website Locations:](#span-classmarkredactedspan-vista-website-locations)
    - [Related Manuals](#related-manuals)
- [Introduction](#introduction)
    - [VistA Mental Health Assistant (MHA) Software Features:](#vista-mental-health-assistant-mha-software-features)
- [# Enhancements and Modifications](#enhancements-and-modifications)
  - [Enhancements:](#enhancements)
  - [Modifications](#modifications)
- [Secure Desktop Information](#secure-desktop-information)
    - [Patient Entry](#patient-entry)
    - [First Warning Dialog Box](#first-warning-dialog-box)
    - [Second Warning Dialog Box](#second-warning-dialog-box)
    - [Authorized Keystrokes](#authorized-keystrokes)
    - [Unauthorized Keystrokes](#unauthorized-keystrokes)
    - [Excessive Use of Unauthorized Keystrokes](#excessive-use-of-unauthorized-keystrokes)
    - [Termination of Mental Health Assistant](#termination-of-mental-health-assistant)
- [Use of the Software](#use-of-the-software)
  - [Contingency Planning](#contingency-planning)
  - [Security Keys](#security-keys)
  - [Windows Conventions](#windows-conventions)
  - [Starting MHA Software Application](#starting-mha-software-application)
    - [Selecting a VistA Server](#selecting-a-vista-server)
    - [VistA Sign-on](#vista-sign-on)
    - [MHA Crash Recovery Files](#mha-crash-recovery-files)
    - [Patient Selection](#patient-selection)
    - [Viewing Patient’s Demographics](#viewing-patients-demographics)
    - [Viewing Patient’s Demographics (continues)Example: This is the same Patient Demographics window used for the Enlarged Test Reports. The Copy, Print, Save to File, and Close functions are the same as the Enlarged Test Report function. Click on the any one of the desired four command buttons located at the bottom of the Patient Demographics window to activate the function.](#viewing-patients-demographics-continuesexample-this-is-the-same-patient-demographics-window-used-for-the-enlarged-test-reports-the-copy-print-save-to-file-and-close-functions-are-the-same-as-the-enlarged-test-report-function-click-on-the-any-one-of-the-desired-four-command-buttons-located-at-the-bottom-of-the-patient-demographics-window-to-activate-the-function)
  - [Mental Health Assistant Main Window](#mental-health-assistant-main-window)
    - [Selecting Mental Health Assistant Tabs](#selecting-mental-health-assistant-tabs)
  - [Selecting Graphs From the File menu](#selecting-graphs-from-the-file-menu)
    - [Selecting Graphs PRINT](#selecting-graphs-print)
    - [Selecting Graphs COPY](#selecting-graphs-copy)
    - [Selecting Graphs SAVE AS](#selecting-graphs-save-as)
    - [### Selecting Exit from File Menu](#selecting-exit-from-file-menu)
  - [Actions Menu](#actions-menu)
  - [Tools Menu](#tools-menu)
    - [Selecting DEFAULT START TAB](#selecting-default-start-tab)
    - [Selecting START TAB (continues)](#selecting-start-tab-continues)
    - [Selecting DEFAULT FORM SIZE/POSITION option](#selecting-default-form-sizeposition-option)
  - [Help Menu](#help-menu)
    - [Selecting SHOW HINTS](#selecting-show-hints)
    - [Selecting TEST INFORMATION](#selecting-test-information)
    - [Selecting ABOUT option](#selecting-about-option)
    - [Selecting ENLARGED REPORT option](#selecting-enlarged-report-option)
    - [Selecting ENLARGED REPORT option (continues)](#selecting-enlarged-report-option-continues)
    - [Selecting Copy](#selecting-copy)
    - [Selecting Copy (continues)Example: After the Test Report is copied, the Mental Health Assistant Information dialog box is displayed stating, “The test report has been copied onto the Window’s clipboard. If you like, you may paste it into an open text document.” Click the OKcommand button to paste the test report into an open text document.](#selecting-copy-continuesexample-after-the-test-report-is-copied-the-mental-health-assistant-information-dialog-box-is-displayed-stating-the-test-report-has-been-copied-onto-the-windows-clipboard-if-you-like-you-may-paste-it-into-an-open-text-document-click-the-okcommand-button-to-paste-the-test-report-into-an-open-text-document)
    - [Selecting Print](#selecting-print)
    - [Save To File](#save-to-file)
    - [Save To File (continues)Example: The Save Aswindow is then displayed for the user to choose to a file name and folder location to save the Test Report.](#save-to-file-continuesexample-the-save-aswindow-is-then-displayed-for-the-user-to-choose-to-a-file-name-and-folder-location-to-save-the-test-report)
    - [Close](#close)
    - [Append Comments option](#append-comments-option)
    - [Append Comments (continues)Example: To Append Comments the user musttype all comments within the text entry box displayed in this example.](#append-comments-continuesexample-to-append-comments-the-user-musttype-all-comments-within-the-text-entry-box-displayed-in-this-example)
    - [Append Comments Cancel option](#append-comments-cancel-option)
    - [Append Comments Save option](#append-comments-save-option)
    - [Append Comments Save (continues)Example: After the Appended Comments are saved, a message is displayed on the Mental Health Assistant main window stating, “This note will be appended to completed test.”](#append-comments-save-continuesexample-after-the-appended-comments-are-saved-a-message-is-displayed-on-the-mental-health-assistant-main-window-stating-this-note-will-be-appended-to-completed-test)
    - [Multi-Scale Graphs](#multi-scale-graphs)
    - [Selecting Scale Group, Part 2](#selecting-scale-group-part-2)
    - [Copy Graph](#copy-graph)
    - [Paste Graph](#paste-graph)
    - [Print Graph](#print-graph)
    - [Save Graph](#save-graph)
    - [Save As](#save-as)
    - [Copy Table](#copy-table)
    - [Paste Table](#paste-table)
    - [Print Table](#print-table)
    - [Save Table](#save-table)
    - [Save Table (continues)](#save-table-continues)
    - [Close](#close-1)
    - [Close (continues)](#close-continues)
  - [Selecting and Administering New Psychological Tests](#selecting-and-administering-new-psychological-tests)
    - [Order Tests Tab](#order-tests-tab)
    - [Order Tests Tab](#order-tests-tab-1)
    - [Available Tests](#available-tests)
    - [Restarting Incomplete Tests](#restarting-incomplete-tests)
    - [Restarting Incomplete Tests (continues)](#restarting-incomplete-tests-continues)
    - [Restarting Incomplete Tests (continues)](#restarting-incomplete-tests-continues-1)
    - [Restarting Incomplete Tests (continues)](#restarting-incomplete-tests-continues-2)
    - [Test Batteries](#test-batteries)
    - [Selecting a Test from Test Batteries](#selecting-a-test-from-test-batteries)
    - [Transferring TEST BATTERIES to TEST CHOSEN](#transferring-test-batteries-to-test-chosen)
    - [Staff Entry](#staff-entry)
    - [Staff Entry (continues)](#staff-entry-continues)
    - [Staff Entry (continues)](#staff-entry-continues-1)
    - [New Question](#new-question)
    - [Close/Continue](#closecontinue)
    - [Close/Continue](#closecontinue-1)
    - [Clerk Entry](#clerk-entry)
    - [Mental Health Assistant Information dialog box](#mental-health-assistant-information-dialog-box)
    - [PTSD Checklist M window](#ptsd-checklist-m-window)
    - [Jump](#jump)
    - [Close](#close-2)
    - [Patient Entry](#patient-entry-1)
  - [Addiction Severity Index (ASI)](#addiction-severity-index-asi)
    - [ASI Window](#asi-window)
    - [ASI Data Entry](#asi-data-entry)
    - [Selecting an Unsigned ASI](#selecting-an-unsigned-asi)
    - [Business Rules](#business-rules)
    - [Options Menu](#options-menu)
    - [Help Menu Options](#help-menu-options)
    - [About Mental Health Assistant](#about-mental-health-assistant)
    - [New Features](#new-features)
    - [Domain Scores](#domain-scores)
    - [Domain Scores](#domain-scores-1)
    - [Item Trends (continued)](#item-trends-continued)
    - [Graphing a Different Item](#graphing-a-different-item)
    - [Returning to the ASI Window](#returning-to-the-asi-window)
  - [Global Assessment of Functioning (GAF)](#global-assessment-of-functioning-gaf)
    - [GAF Tab](#gaf-tab)
    - [GAF Tab](#gaf-tab-1)
    - [GAF Due](#gaf-due)
    - [Previous Rating/GAF Criteria](#previous-ratinggaf-criteria)
- [Glossary](#glossary)
- [Appendix A](#appendix-a)
  - [Shortcut Keys](#shortcut-keys)
- [Appendix B](#appendix-b)
  - [Windows Conventions](#windows-conventions-1)
> **NOTE:** The Veterans Health Administration (VHA) fully supports Section 508 of The Rehabilitation Act and is committed to equal access for all users. While every effort has been made to ensure Section 508 compliance, we realize that there may be other issues. If you have questions or would like to see a copy of the Compliance Action Plan for future releases, please contact:
<span class="mark">REDACTED</span>

## V*ist*A Mental Health Assistant Version 2 (MHA 2) Software Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Information Systems and Architecture (V*ist*A) Mental Health Assistant Version 2 (MHA 2) User Manual for Patch YS\*5.01\*76, provides the Department of Veterans Affairs Medical Center (DVAMC) Information Resource Management (IRM) staff and other DVAMC users with a straightforward means for implementing and utilizing the MHA 2 software application. Detailed instructions, functional requirements, and examples for using the MHA GUI software application are illustrated in this user manual.

### Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audience for the MHA 2 User Manual includes mental health clinicians, clerks, and patients.

### MHA Version 2 User Manual Sections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Version 2 (Patch YS\*5.01\*76) User Manual focuses on easy-to-follow step-by-step instructions. This user manual consists of the following sections:

> **NOTE:** The screen captures examples text is written in support of Section 508 compliance. Commands to utilize options are bolded.

Table Of Contents (TOC): The TOC provides references to major chapters and/or sections of the user manual.

Orientation: This section address package or audience specific notations or directions.

Introduction: This section conveys the major functions, purposes, and how the software accomplishes the objectives.

Secure Desktop Information: This section contains security measures pertaining to the Mental Health Assistant software application and data.

Use of the Software: This section describes what the user needs to know in order to competently operate the MHA 2, software application, including screen captures examples.

Glossary: This section contains the glossary of terms that are related to the MHA 2 software application.

Appendix A: This section contains a list of shortcut keys use in the Mental Health Assistant Version 2, Graphical User Interface software application:

Appendix B: This section contains descriptions of the many window commands and features used in MHA 2.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## MHA Version 2 Documentation Retrieval Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File NameContentsRetrieval Formats

YS50176_MHA2_IG.PDF YS_MHA2 Installation Guide BINARY

YS50176_MHA2_IG.DOC YS_MHA2 Installation Guide BINARY

YS50176_MHA2_UM.PDF YS_MHA2 User Manual BINARY

YS50176_MHA2_UM.DOC YS_MHA2 User Manual BINARY

### MHA 2 Documentation Retrieval Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** All sites are encouraged to use the File Transfer Protocol (FTP) capability. Use the FTP address “*download.vista.med.va.gov*” (without the quotes) to connect to the first available FTP server where the files are located.

MHA Version 2 Installation Guide and User Manual files are available at the following Office of Information Field Offices (OIFOs) ANONYMOUS.SOFTWARE directories.

OI FIELD OFFICEFTP ADDRESSDIRECTORY

================ ================== ========================

### <span class="mark">REDACTED</span> V*ist*A Website Locations:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MHA Version 2, Installation Guide (i.e., YS50176_MHA2_IG.PDF and YS50176_MHA2_IG.DOC), and User Manual (i.e., YS50176_MHA2_UM.PDF and YS50176_MHA2_UM.DOC) are available in MS Word Format (DOC) and Portable Document Format (PDF) at the following Website locations:

#### V*ist*A Mental Health Version 5.01 Home Page:

<span class="mark">REDACTED</span>

#### V*ist*A Documentation Library (VDL):

<http://www.va.gov/vdl/>

### Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Mental Health (MH) Addiction Severity Index Multimedia Version (ASI-MV) Installation and User Guide (Patch YS\*5.01\*67)
# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary goal is to make the V*ist*A Mental Health Package (MHP) V. 5.01, an effective and more efficient tool for use by mental health clinicians and patients with the creation of a windows based application for the most commonly used options in the MHP. Currently the MHP is administered through V*ist*A’s roll-and-scroll technology. Interviews are generally recorded on paper and entered later by the clinician or clerk because the roll and scroll environment is not conducive to following the natural flow of conversation. Development of the Mental Health window based software application used for entering and displaying Addiction Severity Index (ASI), Global Assessment of Functioning (GAF) score, and over 50 psychological tests makes the MHP user-friendlier. This enhancement also provides a Graphical User Interface (GUI) format for the entry of ASI assessments, GAF, and displaying of reports and results of psychological tests and interviews.

### V*ist*A Mental Health Assistant (MHA) Software Features:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ASI – Addiction Severity Index:

Graph numeric results from ASI responses.

Functionality to display the ASI entry screens in tabbed sections on one screen.

Create functionality to display ASI test date, type of interview and interviewer and responses to previous interviews.

Create Item report with narrative responses.

Create Narrative reports from ASI responses.

Create Follow-up report from ASI interviews and responses.

#### GAF – Global Assessment Functioning:

Present GAF scores in a graphical format.

Display on-line cross-reference data with rating criteria.

Provide functionality to notify the user when selected patients have not had a GAF Score within the last 90 days. (GAF Due tab).

#### Psychological Tests and Interviews:

Graph single scale instruments to reflect trend in patient symptoms.

Create an order entry screen to select tests and interviews.

Create an option for entry of tests and interviews by patients.

Create an option for entry of tests and interviews by staff.

Create a graphical representation of multi-scale instruments.

Create a report of incomplete tests, interviews and batteries by date.

Create a report to print results of psychological interviews and tests.

#### ASI Functionality

> **NOTE:** The New ASI functionality is NOT a self-administered version of ASI, and should NOT be used for patient entry of ASI responses.

#### New ASI Tab:

The New ASITab functionality lists all previous ASI interviews and makes it easy to view either the Item Report or Narrative Report for a selected interview. To assist with ASI performance measure compliance, the interval since the last interview is now displayed.

#### User-Friendly Interface:

This new user-friendly interface functionality allows staff to quickly enter data, to easily jump from one item to another, and to enter free text comments at any time. This functionality should greatly reduce data entry time, whether transcribing interview results from a paper form or entering them on-line during an interview

#### Edit/Sign an Unsigned ASI Report:

Provides the user the ability to Edit/sign an Unsigned ASI report. This function is enabled ONLY if the selected ASI report is not signed. The previous functionality to limited the signer to the user listed as the interviewer.

#### Data Views:

Data Views present graphical and tabular data across multiple interviews.

#### Domain Scores:

Domain Scores functionality provides users with the opportunity to see either problem severity ratings or evaluation factor scores (see Alterman, et al., \[1998\] “New scales to assess change in the Addiction Severity Index for the opioid, cocaine, and alcohol dependent”, *Psychology of Addictive Behavior,* 12, 233-246). The Domain Scores also consist of the new Data Views functionality.

#### Item Trends:

Item Trends functionality provides display responses to selected individual items, assist with treatment planning, and treatment outcome monitoring. Item Trends also includes the new Data Views functionality.

#### GAF Functionality

#### GAF Tabs:

Provides the user with an easy way to enter GAF ratings and to see previous ratings, which are graphed to indicate trends. When entering a new rating, the rating is associated with the GAF rating criteria. This function increases the reliability of ratings and reduces inter-rater variability in the assignment of GAF ratings.

#### GAF Criteria:

The first display seen when accessing the GAF tab for the first time after a new patient selection is made. The first entry in the Range/Criteria list box is displayed. A rating of 1 is in the New GAF rating spin edit control, the Evaluation Date is set to today's date, and the Save Rating command button disabled.

#### GAF Previous Ratings:

The GAF Previous Ratings functionality provides a tabular and graphical representation of all previous GAF ratings as well as the rating criteria for the specified new GAF rating.

#### GAF Toggle Buttons:

Toggle between GAF Previous Ratings and GAF Criteria functionalities.

#### Enter/Retrieve GAF Ratings:

Enhanced the ability of the staff to enter and retrieve GAF ratings. It provides text and graphical reports of historical data stored in the V*IST*A MHP database.

#### GAF Editing Rating:

The GAF Edit Rating function allows a user to change or delete a rating made within the previous two days or to mark an older rating as Entered in Error. GAF Ratings can ONLY be edited by the user who entered the ratings. The GAF Ratings function is enabled ONLY if the MHA user entered the selected rating.

#### GAF Due:

When the GAF Due functionality is activated an Information dialog box is displayed stating “This patient has not had an outpatient GAF in the past 90 days. Would you like to do a GAF rating now?”

#### Psychological Tests and Interviews Functionality

#### Order Tests Tab:

Allows users to specify the staff ordering the test and to select from tests that are available to the staff ordering the test. Three data entry modes are available: (1) Staff entry is optimized for the entry of staff rating data (e.g., the AIMS), which requires the user to see the test questions and answers. (2) Clerk entry is optimized for transcribing test data from paper answer sheets. (3) Patient entry is optimized for on-line testing of patients. The patient entry function contains security features to prevent unattended patients from using the PC in unauthorized ways.

#### Psychological Test Data Entry:

Enhances the ability of both staff and patients to enter psychological test data.

#### Reports and Graphical Displays:

Creates reports and graphical displays of complex tests by sub category or scales. Allows user to select sets of scores to graph for multi-scale tests.

#### Psychological Test Orders:

Creates psychological test order windows that displays tests that can be ordered based on the provider privileges.

#### Users Selection:

Allows users to select multiple tests, interviews, and batteries.

#### Display Combinations:

Provide functionality to display a combination of scale scores, tables and graphs for an individual patient on one screen.

#### Graphing Multiple Instances:

Graph multiple instances of the same tests (i.e., 4 CAGE tests given on 4 days).

#### Copying:

Allows user to copy text reports, data tables, or graphs to the Windows clipboard or to save to a file.

#### Test Results Tab:

All previous tests completed by selected patient are listed on the Test Results tab. A text report is shown for the selected test, and graphs of numeric scores are available across all instances of a given test.

# # Enhancements and Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

V*ist*A MHA Version 2, Patch YS\*5.01\*76, exports the following software changes:

## Enhancements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Four new psychological tests, the Millon Behavioral Medicine Diagnostic (MBMD), the Beck Depression Inventory-II (BDI2), the Millon Clinical Multiaxial Inventory-III (MCMI3) and the Brief Symptom Inventory 18 (BSI18) have been added to the MH INSTRUMENT file (#601). All can now be administered using MHA. The results of the MCMI3, the BSI18, and MBMD can be viewed using the multi-scale graph window (the BDI2 is a single scale instrument). Context sensitive descriptions of the new tests were added to the Help file.

2\. Entries to the COPYRIGHT HOLDER file (#601.3) have been made for the new psychological tests MBMD, BDI2, MCMI3, and BSI18.

3\. For the psychological test Minnesota Multiphasic Personality Inventory-2 (MMPI2), several changes have been made in the scales that are scored and displayed. Five new scales are now scored (the PSY-5 Personality Psychopathology Five). The Subtle-Obvious and Non-K Corrected scales are no longer scored or displayed. The user can choose to display all validity scales at once (Expanded Validity) or just the L, F, K scales (Basic Validity). In MHA Version 2 the multi-scale graph option has been revised to display the new scales.

4\. On the main window of Test Results, Order Tests, ASI or GAF tabs, a right mouse click brings up a pop-up menu with options for each of the enabled buttons on the active tab.

5\. A pop-up menu was added to the window used for graphically displaying the results of both multi-scale tests and ASI domain scores. The pop-up menu, which is activated by a right-click, permits the user to copy, print or save either a graph or a table.

6\. When MHA 2, is launched from the CPRS Tools menu, MHA 2, accepts parameters (such as Patient DFN) passed by CPRS. This eliminates the need to select a patient a second time and ensures that the same patient is always selected by both applications, if both are open. When CPRS is closed, MHA 2 will closed automatically.

7\. MHA 2 can be launched from the CPRS Tools menu without having to sign on a second time if the RPC Broker workstation client software is installed on the PC and single sign-on is enabled on V*ist*A.

8\. Upon closing the Staff Entry window, the user is given the option of saving the test results to V*ist*A. Previously, the option of saving results were given only if all the test questions had not been answered. Completed tests were automatically saved. The change gives the user control over whether the data are saved and makes the exit process the same whether the test was completed or not.

9\. To make the patient selection key sequence the same as that used in CPRS, the Select Patient menu caption was changed from “<u>S</u>elect New Patient” to “Select <u>N</u>ew Patient”.

10\. If a patient is deceased, the user is notified of that and asked if they want to proceed before allowing entry of a new GAF rating, psychological test, or ASI. If the user proceeds, the GAF rating date or ASI admission/interview dates cannot be greater than the date of death. Constraining the date of psychological test data for staff and clerk entry will require a modification to the MH INSTRUMENT file (#601).

11\. ASI comment fields were saved to V*ist*A in a way that caused word wrap problems. The comments fields now are formatted correctly.

12\. In MHA Version 1, the ASI data-entry form, when clicking on an up or down arrow in a spin-edit item, the spin-edit item with focus was increased or decreased. Any up or down arrow click would have its impact on the field with focus, even arrows for other items. The current version allows only the up and down arrows associated with that spin-edit item to have any effect.

13\. In MHA Version 1, the executable was named YS50171_MHA.exe to reflect both the associated VistA patch (YS\*5.01\*71) and the Delphi application build number (123). However, this method of naming the executable will require a new name with each release, which will increase the difficulty of installing future releases. In MHA Version 2, the executable is named YS_MHA.exe, which will be used for all future MHA software releases.

## Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. In MHA Version 1, some windows were closed by a button captioned “Close” and others were closed by a button captioned “Return”. All such buttons are now captioned “Close”.

2\. On the Staff Entry window, the button that returns the user to a previously answered question was captioned “Back Up.” Because this caption could be misunderstood as meaning data would be saved to a backup archive, the caption was changed to “Previous.”

3\. By convention, “OK” buttons appear to the left of “Cancel” buttons, but on some MHA windows their positions were reversed. These two buttons now appear in conventional order on all windows.

4\. To make them more readable, the "\>" captions on the buttons on the Order Tests tab were changed to bold font.

5\. The MMP2S is a short form of the MMPI2. In MHA Version 1, scores from the two forms of the test could not be compared on the multi-scale graph window. The user is now given that option.

6\. When printed, graphs did not include the patient name and yellow lines were not visible on monochrome printers. Patient name is now a footer on all printed graphs, and the yellow lines have been made black.

7\. The following instruments in the MH INSTRUMENT file (#601) are copyrighted tests that VA Central Office (VACO) does not have a license to use (i.e., 16PF, MMPI, M168, MCMI, CES, CPI, FES, FIRO, GES, MYER, WES, and SII). When the user selects one of these instruments they receive the message “USER,MARK is NOT AUTHORIZED to order Instrument GES.” Now, when the user selects one of these instruments the message displayed is “\[VACO currently does not have a license to use this test\].” This message is only displayed on the list manager version of Mental Health V. 5.01. In MHA Version 2, non-copyrighted tests are not viewable in the Available Tests box.

8.The ASI NARRATIVE file (#604.68) data has been edited to correct problems with the logic and executable code to produce a report for the Addiction Severity Index that reads like a clinician's written report. The entries modified are GENERAL, FULL ITEM REPORT, LITE ITEM REPORT, FOLLOWUP ITEM REPORT, FOLLOWUP NARRATIVE, ASI-MV ITEM REPORT and the ASI-MV NARRATIVE.

9\. During initialization of the main window of the Test Results tab, the appropriate notice did not appear if the user did not have the YSP key and the first test in the list of previous tests was non-exempt.

10\. An error occurred if the Domain Scores button on the main window of the ASI tab was clicked for a patient for whom there were no complete ASI records to display. This problem was corrected by disabling the button if the patient did not have at least one signed ASI with all questions answered (i.e., not a G-12 record).

11\. Short-cut keys were working on the main, staff entry and clerk entry windows even though the Alt key was not pressed. This has now been corrected to work only when the Alt key has been pressed.

12\. Signing an ASI-MV was not possible without first loading the data into the ASI data entry window. Because there are some differences between the ASI-MV and a regular ASI, loading the ASI-MV into the ASI data entry window caused data validation errors when the record was saved to V*ist*A. Signing an ASI-MV is now possible without loading the results into the data entry window.

13\. Incorrect source code was used to determine whether the user was the ASI interviewer, who is the only person who can sign the interview. Consequently, a new ASI could not be signed without first saving it to V*ist*A and then reloading it into the data entry window.

14\. On the main window of the Order Tests tab, if either the list box containing test choices or the list box containing tests that had been selected had focus, context sensitive help was not available for the selected test in the list box. The context ID of the selected test now is set on the list box click event.

15\. In MHA Version 1, comments in the ASI were not saved for Spiritual Status and Leisure Time Status. In MHA Version 2, these comments are now saved.

16\. Sometimes, when MHA Version 1 is run as a server application, the help file could not be found. In MHA Version 2 the help file path is now dynamically set.

17\. When using option, Delete unsigned ASI \[YSAS ASI DATA DELETION\] the user received an error %DSM-E-STRLEN, string too long, DSM-I-ATLABEL, TLD+11^YSASSEL:1. This error occurred on a test patient. An initial ASI is administered to a patient once they enter the substance abuse program. A follow-up ASI is then administered every six months the patient is in the program. This error has been corrected by lowering the \$PIECE field position TO from 40 to 20.

18\. When a user selects the multi-graph button for multi-graph tests (i.e., MMPI2) undefined variable error occurs. This error has been corrected.

19\. When a user selects the multi-graph button for multi-graph tests for the SF36 and the score equals 100, they received an “invalid integer” message. On the multiscale window, the table now lists the correct scale scores (i.e., real numbers, not integers). This has been corrected in the MHA GUI source.

20\. The instruction text for patient administered tests in MHA Version 1 are too small and did not contrast well with the grey background. In MHA Version 2, the font size has been increased 10 and the background color has been changed to white.

21\. When a user selected the Test Results tab, and from the list of available tests an interview was selected, an undefined error at R1+1of YIHISTF resulted. The problem is that the user should not have been able to select an interview, example the PSOC or MROS. The API to fill the Test List box has been modified to now just pass tests to display for selection.

22\. When the user selects options Mental Health \[YSUSER\], Clinical Record \[YSCLINRECORD\], Tests and interviews (results) \[YSPRINT\], selects a Patient and then from the list of instruments completed selects the instrument 'HX2'. Because the site had the missing node ^YTD(601.2,YSDFN,1,YSET,1,YSED,U1), the undefined error occurred at R1+4^YIHISTF. This error has been corrected.

23\. Routine YTRPWRP has been modified to correct the Salt Lake City VAMC problem with MHA hanging while retrieving of test results when using the Test Results tab.

# Secure Desktop Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains security measures pertaining to the Mental Health Assistant software application and data.

The Secure Desktop is a set of security features intended to prevent unattended patients taking on-line tests from using the Personal Computer (PC) for other purposes. The SecureDesktop features construct the Patient Entry window to cover the entire PC desktop. Non-alphanumeric keys are trapped to keep the patient from using the task bar and operating system functions (such as Task Manager).

The following security features cannot be defeated once the Patient Entry window becomes active, so it is essential that all other applications be closed and data saved before Patient Entry begins:

> **NOTE:** The Patient Entry function is the only test data entry method that activates the Secure Desktop features. Therefore, neither Staff Entry nor Clerk Entry should be used for the on-line testing of patients.

Excessive non-alphanumeric keystrokes are interpreted as “hacking” efforts and MHA is terminated.

At the end of the testing session, MHA is terminated.

On termination of MHA, the Windows NT session is logged off, which means the user has to enter their NT user name and password to log back on to the desktop.

### Patient Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The following is an example of the Mental Health Assistant Order Tests window containing Patient Entry. When Patient Entry is selected the Secured Desktop features are activate. After the Patient Entry selection is made, two Warning dialog boxes are displayed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/002.png)

### First Warning Dialog Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The first Warning Dialog Box states “After this programs ends, it is going to automatically log you off from the Windows NT Network.” Click on the YEScommand button to proceed. The YEScommand button response displays a second Warning dialog box. ClickCancel to return to the Windows NT Network.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/003.png)

### Second Warning Dialog Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The second Warning dialog box states, “Use ONLY Alpha-Numeric Keys on the keyboard from this point on.” Click the OK command button to continue the Patient Entry functions.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/004.png)

### Authorized Keystrokes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Authorized keystrokes are entered in response to the on-screen questions. Authorized keys are A..Z, a..z, 0..9, ENTER and SHIFT key. Keystrokes trigger the next question to be displayed.

### Unauthorized Keystrokes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Unauthorized keystrokes are entered in response to the on-screen questions. Unauthorized keystrokes are all that are not listed above. Keystrokes trigger the default Windows screensaver to activate, hiding what else is on the screen display. Keystrokes have no other significant effect on the psych test. USER MUST NOT BE ABLE TO ACCESS UNAUTHORIZED DATA OR PROGRAMS.

### Excessive Use of Unauthorized Keystrokes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Strike 5-10 unauthorized keystrokes. Windows shuts down all active programs and logs off the current user, forcing a user to log on again.

### Termination of Mental Health Assistant

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete a test. Windows shuts down all active programs and logs off the current user, forcing a user to log on again.

# Use of the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes what is needed to successfully use the new Mental Health Assistant Version 2, software application enhanced components for Addition Severity Index (ASI), Global Assessment of Functioning (GAF), and Psychological Tests and Interviews.

NOTES:

Please see Appendix A, (i.e., located in the back of this manual) for a revised list of MHA 2 shortcut keys. The list can be removed from this manual for easy access and viewing.

Please see Appendix B, (i.e., located in the back of this manual) for a list of the MHA window conventions. The list can be removed from this manual for easy access and viewing.

## Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each facility using the MHA software application must develop a local contingency plan to be used in the event of application problems in a live environment. The facility contingency plan must identify procedures used for maintaining the functionality provided by the software in the event of a system outage.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA software application did not release any new security keys, however, the YSP security key is required to control access to the results of “non-exempt” tests. Holders of the YSP security key are controlled (i.e., given out by the Chief of Psychology or a senior psychologist) at a facility that does not have a Chief of Psychology. The Chief of Psychology or senior psychologist also determines which tests are “exempt” (i.e., the results can be seen by anyone), and which are “non-exempt” (i.e., require the YSP key to see the results).

## Windows Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The startup, setup, and assignment functions for MHA use a Graphical User Interface (GUI). You may refer to the Appendix B, Windows Conventions for an explanation of the windows elements and form buttons used by the module.

## Starting MHA Software Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Double click the MHA icon ![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/005.png) on the desktop to start. If the user is able to connect to more than one server, the user must select the server they want to connect to. Otherwise, V*ist*A logon screen appears on the desktop.

### Selecting a V*ist*A Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the PC Workstation is configured to interact with more than one V*ist*A server, the user will be prompted to select a server from a list of servers. However, most PC workstations are not set up this way. Note: The following Connect To dialog box example may not be seen.

Example: From the Connect To dialog box, select the appropriate VISTA server and click on the OK command button.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/006.png)

### V*ist*A Sign-on

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the V*ist*A Sign-ondialog box enter the standard V*ist*A Access Code and Verify Code and click the OKcommand button to access V*ist*A.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/007.png)

### MHA Crash Recovery Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Mental Health Assistant software application is closed normally after administering psychological testing sessions or ASI data entry, the software prompts the user to save any unsaved data. This process will not occur if MHA is shutdown improperly (i.e., power outage). To prevent data loss resulting from improper program closure, MHA creates a temporary crash file on the local PC when psychological tests or ASI data entry is being preformed. This file is updated every time a new entry is made; therefore, the file is always current. Upon normal program closure, this crash file is erased. However, the crash file still exists if MHA is closed improperly. Every time MHA begins, it looks for the temporary crash file on the PC hard drive. If the file exists, the data in the file are uploaded to the V*IST*A MHP database so the user can restart the incomplete psychological test session or ASI data entry.

Example: Whenever the MHA software application is shutdown improperly the following Mental Health Assistant Information dialog box is displayed. Click on the OK command button to save the data into the temporary MHA crash file.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/008.png)

### Patient Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Selection window contains the Patient Selection function. The Patient Selection window is the same functionality used by Computerized Patient Record System (CPRS).

Example: Select the Patient Selection window. Click the vertical scroll bar to scroll through the Patientstext entry boxlist to attain a Patient Selection. After the patient selection is made, click on the OKcommandbutton to advance to the next window. Note: Alternatively, you may double-click on the selected patient’s name, (which eliminates the need to click on the OKcommandbutton) or you may enter the patient’s last name in the Patients text entry box and click on the OKcommand button.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/009.png)

### Viewing Patient’s Demographics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health Assistant window contains the Patient’s Demographics functionality.

Example: To view Patient’s Demographics, select the Mental Health Assistantwindow. Click on the blue button (as displayed in this example) located on the upper left side of the window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/010.png)

### Viewing Patient’s Demographics *(continues)*Example: This is the same Patient Demographics window used for the Enlarged Test Reports. The Copy, Print, Save to File, and Close functions are the same as the Enlarged Test Report function. Click on the any one of the desired four command buttons located at the bottom of the Patient Demographics window to activate the function.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/011.png)

## Mental Health Assistant Main Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health Assistant main window contains the File, Options, and Help menus, which are located on the menu bar just below the Mental Health Assistant main window label. This window also contains the [Test Results](#_Psychological_Test_Results_1), [Order Tests](#selecting-and-administering-new-psychological-tests), [ASI](#addiction-severity-index-asi), and [GAF](#_GAF) tabs, located on the bottom left side of the main window. These tabs represent the four major functions of the MHA software application. You may access the tabs by clicking on the name of the desired tab. It is also possible to specify a [default start tab](#selecting-default-start-tab), (i.e., the tab that appears first when a new patient is selected).

### Selecting Mental Health Assistant Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Assistant main window, click on the desired tab (i.e., Test Results example), located on the bottom left side of the window, to access the function.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/012.png)  
<u>File Menu</u>

The Mental Health Assistant File menu contains the following options:

1\. Select new patient – This option allows the user to select a patient for all four MH test functions (i.e., Test Results, Order Tests, ASI, and GAF).

2\. Refresh Patient Data– This option reloads the list of all previously administered psychological tests, the list of all previously administered ASIs, and previous GAF ratings for the selected patient. Note that these three lists are all loaded when a patient is selected, and they are updated if a new test, ASI or GAF rating is made using MHA. Thus, it is expected that this option will not be used very often. There are only two situations in which it might be helpful:

\(1\) If, while MHA is open and a patient is selected, data is entered for that patient using the roll-and-scroll interface, the Refresh Patient Data option could be used to load that new data into the MHA lists. (2) If multiple stand-alone sessions of MHA are open at the same time with the same patient selected, then data entered in one session could be updated in a second session by using the Refresh Patient Data option in the second session. It is not anticipated, though, that many clinicians will opt to have multiple sessions of MHA active at the same time.

3. Report/Tables option - contains a drop down list to Print, Copy, and Save As. The Print, Copy, and Save As options allow the user to print and save Report/Tables files to desired locations. The Report/Table option appears as a pop-up window with a right click on the window. The pop-up window functions the same way as the drop down list.
4. Graphs option - contains a drop down list to Print, Copy, and Save As. The Print, Copy, and Save As options allow the user to print and save Graphs to desired locations. The Graphs option appears as a pop-up window with a right click on the window. The pop-up window functions the same way as the drop down list.

5.Exit option - allows the user to close MHA.

#### Select New Patient

Example: From the Mental Health Assistant Test Results window, click on the File menu. From the Filedrop down menu list, click on the Select new patient option.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/013.png)

#### Refresh Patient Data

Example: From the Mental Health Assistant Test Results window, click on the File menu. From the Filedrop down menu list, click on the Refresh Patient Data option.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/014.png)

#### Selecting Reports/Tables

> **NOTE:** The Report/Tables command button is enabled if a text report or a table is already visible in the window.

Example: From the Mental Health Assistant Test Results window, click on the File menu, located on the left side of the menu bar to pull down the File menu. Click on the Reports/Tables option to display the drop down menu list to Print,Copy, and Save As.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/015.png)

#### Selecting Report/Tables Print option 

Example: From the Reports/Tables option, select the Print option. This option will print the report, graph, or table that is displayed on the PC desktop.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/016.png)

#### Selecting Report/Tables Copy option

Example: From the Reports/Tables drop down menu, Click on Copy. This option will copy the report, graph, or table into the Windows clipboard.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/017.png)

#### Selecting Report/Tables Copy option (continues)

Example: After copying the Report/Table, the Mental Health Assistant Information dialog box is displayed stating, “The test report has been copied to the Windows clipboard. If you like, you may paste into an open text document.” Click on the OKcommand button to paste the text document.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/018.png)

#### Selecting Report/Tables Save As option

> **NOTE:** The default file type for reports is a text file (.txt) extension; for tables and graphs it is the Excel file (.xls) extension.

Example: From the Reports/Tables option drop down list, click on the Save Ascommand button to save a report or table.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/019.png)

#### Selecting Report/Tables Save As option (continues)

Example: After the Save As function is selected, a Save As window is displayed prompting for a file name.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/020.png)

## Selecting Graphs From the File menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Mental Health Assistant Test Results window, clickonFile, from the File drop down menu list, click onGraphs. The Graphs drop down menu list contains the Print, Copy, and Save As options, click on the desired option to activate the function. Note: The Graphs menu is enabled if a Graph is visible.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/021.png)

### Selecting Graphs PRINT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Test Results window, click on File, from the File drop down menu list, click on Graphs, then click on Print to print the graph displayed in the window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/022.png)

### Selecting Graphs COPY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Test Results window, click on File, from the File drop down menu, click on Graphs, then clickCopy to copy the graph displayed in the window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/023.png)

### Selecting Graphs SAVE AS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Test Results window, click on File, from the File drop down menu list, click on Graphs, then clickSave As to save the graph displayed in the window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/024.png)

### ### Selecting Exit from File Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Assistant ASI window, click on File. From the File drop down menu list, click onExit to close a MHA session. MHA sessions can also be closed by clicking on the X, located on the upper right side of the window title bar.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/025.png)

## Actions Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health Assistant Actions Menu is an alternative to the command buttons at the top of the active window as well as an alternative method of changing tabs. Each command button has a corresponding menu option. Every menu option has a shortcut (i.e., an Alt-Key combination) that results in the same action as would a click on the corresponding command button. Thus, the Actions menu may be helpful to users who do not use a mouse.

The specific menu options shown under the Actions Menus depends on the active window. Whether a menu option is enabled depends on whether the corresponding command button is enabled. Thus, Patient Demographics and GAF Due options are shown on all active windows because the corresponding command buttons are always shown. The Change Tab menu option also is always shown.

When the Test Results window is active, Multi-scale Graphs, Enlarge Reports, and Append Comments menu options are shown.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/026.png)

  
Example: When the Order Tests window is active, window-specific menu options include Staff Entry, Clerk Entry, Patient Entry, Select Battery, and Delete All Chosen Tests.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/027.png)

Example: Window-specific menu options when the ASI window is active include New ASI, Domain Scores, and Item Trends.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/028.png)

Example: If the GAF window with all the GAF rating criteria is active, menu options include Previous Ratings, Save Rating, and Edit Rating.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/029.png)

Example: If the GAF window with the previous ratings is shown, the window-specific menu options are GAF Criteria, Save Rating, and Edit Rating.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/030.png)

## Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health Assistant Tools menu contains the Start Tab and Default Form/Size Position options.

Start Tab option - determines the screen that appears when the user starts the application. The user may select one of the following:

1\. Test Results

2\. Order Tests

3\. ASI

4\. GAF

5\. Tab in use when program closed.

The Start Tab allows the user to tailor MHA to their typical work patterns.

Default Form Size/Position option (i.e., checked or not checked) - saves the status from one MHA session to another, so the Default Form Size/Position settings or the user-preferred settings can always be used. The first time a MHA session is started, the Default Form Size/Position option is checked and the default settings are used.

### Selecting DEFAULT START TAB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Assistant GAF window, click on Tools. Click on Start Tab and the Start Tab window is displayed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/031.png)

### Selecting START TAB (continues)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Start Tab dialog box, click the appropriate radio button to make a selection. Click the OK command button to accept the selection or the Cancel command button to cancel the selection.

<span id="_Psychological_Test_Results" class="anchor"></span>![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/032.png)

### Selecting DEFAULT FORM SIZE/POSITION option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Default Form Size/Position option is checked, this function is used. If it is not checked, the Default Form Size/Position that was true when the MHA session was closed the last time is used. The status of the Default Form Size/Position option (i.e., checked or not checked) is saved from one MHA session to another, so the Default Form Size/Position settings or the user-preferred settings can always be used. The first time a MHA session is started, the Default Form Size/Position option is checked and the default settings are used.

Example: From the Mental Health Assistant window, click onTools, and click on Default Form Size/Position. The check-mark symbol displayed beside the Default Form Size/Position option toggles on and off and the window size will adjust accordingly.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/033.png)

## Help Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MHA Help menu contains the Show Hints, Test Information, and the About options:

### Selecting SHOW HINTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA contains a large number of hints that pop-up when the cursor passes over various parts of the window. Show Hints explains how to use parts of the MHA application over which the cursor is placed. These hints are helpful for new users of the MHA software application. However, we give the user control over whether or not the hints shall appear. If Show Hints is checked (i.e., which is set as the default the first time MHA is run on a PC) the hints are displayed. If Show Hints is selected all hints are turned off. The hints can be turned on again by selecting Show Hints. When a MHA session is ended, the status of Show Hints (i.e., checked or unchecked) is saved and restored when the next session begins.

Example: From the Mental Health Assistant window, click on Help and then click on Show Hints. The check mark shown next to Show Hints toggles on and off, and hints are then displayed when Show Hints is checked.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/034.png)

### Selecting TEST INFORMATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Test Information display a Help file containing a brief description of each test in the Mental Health Package. Test Information is enabled only if the Test Results tab or Order Tests tab function is active.

Example: From the Mental Health Assistant window, clickHelp and click on Test Information from the drop down list menu. The following MHA help file test examples are displayed. Pressing F1 when either the Test Results tab or Order Tests tab function is active also displays the MHA help file.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/035.png)

### Selecting ABOUT option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Please furnish the following information if reporting a problem with MHA.

Example: From the Mental Health Assistant window, selectHelp and click on the About option. The About Mental Health Assistant window is displayed with text stating “Mental Health Assistant (MHA), Module Version: 1.0.0.117, Server Version: NA, Client Patch Version: 1.0.0.117, Sever Patch Version Required: 71, Compile Date: 03/20/2002 10:09:06 AM, CRC: 85747543, Developed by the Department of Veterans Affairs. Unauthorized access or misuse of this system and/or it’s data is a federal crime. Use of all data shall be in accordance with VA Policy on security and privacy of the MHA version being used.” A note is also included in the window regarding VHA fully support Section 508 of The Rehabilitation Act. Click on the OK command button, located on the bottom left side of the window to exit.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/036.png)

<u>Psychological Test Results</u>

All previous tests completed by the selected patient are listed on the [Test Results](#_Test_Results_Tab) tab, and one of those tests is always highlighted (by default, the first test in the list is highlighted when the user first access this tab). A text-based report for the highlighted test is shown. If the highlighted test has a numeric score, only one scale, and if the test has been completed more than once, a graphical display of those scores is presented. Buttons on the Test Results tab enable user to invoke other forms that [graph](#multi-scale-graphs) the results of multi-scale tests, show a [full-screen view](#_Enlarged_Report) of the text report for the highlighted test, and enable the user to [append comments](#_Append_Comments) to the results of the highlighted test.

<span id="_Test_Results_Tab" class="anchor"></span>

#### Selecting Test Results Tab

#### Sort by Date or Name

Example: From the Mental Health Assistant main window click on the Test Results tab, located on the bottom left side of the window. From the Sort Tests By dialog box, click on the Date or Nameradio buttons. Tests are sorted either in reverse chronological order by date of completion or by name, depending on the selection.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/037.png)

### Selecting ENLARGED REPORT option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Assistant Test Results window, click on the Enlarge Reportcommand button, located below the menu taskbar, to enlarge the test report display.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/038.png)

### Selecting ENLARGED REPORT option (continues)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: This is the Enlarged Test Report display viewed on the desktop.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/039.png)

### Selecting Copy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: To copy a Test Report,click the Copycommand button, located at the bottom right of the Test Reportwindow. The Test Report is then copied onto the Window’s clipboard to be pasted into an open text document.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/040.png)

### Selecting Copy *(continues)*Example: After the Test Report is copied, the Mental Health Assistant Information dialog box is displayed stating, “The test report has been copied onto the Window’s clipboard. If you like, you may paste it into an open text document.” Click the OKcommand button to paste the test report into an open text document.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/041.png)

### Selecting Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Test Report window, click on the Printcommand button, located on the bottom right side of the window. This prints the Test Report that is displayed on the desktop.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/042.png)

### Save To File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: To activate the Save to File function for a Test Report, click the Save to Filecommand button located on the bottom right side of the Test Report window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/043.png)

### Save To File *(continues)*Example: The Save Aswindow is then displayed for the user to choose to a file name and folder location to save the Test Report.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/044.png)

### Close

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Test Report window,click the Close command button, located on the bottom right side of the window to close to the Test Results window.

<span id="_Append_Comments" class="anchor"></span>![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/045.png)

### Append Comments option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Assistantmain window,click on the Test Results tab, located on the bottom left side of the window. Click on the AppendCommentscommand button, located below the menu bar to display the AppendComments window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/046.png)

### Append Comments *(continues)*Example: To Append Comments the user musttype all comments within the text entry box displayed in this example.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/047.png)

### Append Comments Cancel option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the text entry box type in some comments and click on the Cancel command button, located on the bottom right side of the of the text entry box. The text entry box closes without appending the comments to the Test Results Report.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/048.png)

### Append Comments Save option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the text entry box, type in comments and click the Save command button, located on the bottom right side of the text entry box. The text entry box closes and the comments are appended to the Test Results Report.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/049.png)

### Append Comments Save *(continues)*Example: After the Appended Comments are saved, a message is displayed on the Mental Health Assistant main window stating, “This note will be appended to completed test.”

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/050.png)

### Multi-Scale Graphs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Selecting a Multi-Scale test enables the Multi-Scale Graphs commend button if the user has permission to access the results of non-exempt tests (i.e., user must be assigned the YSP key). Selecting a single scale test disables the Multi-Scale Graphs button. Selecting a Multi-Scale test (i.e., MMPI-2) enables the Multi-Scale Graphs button.

#### Enabling Multi-Scale Graphs

Example: From the Mental Health Assistant main window, click on the Test Results tab, located on the bottom left side of the window. Click on a single scale test (e.g., AUDIT, CAGE, or BDI), located in the Date/Test list box, located below the blue command button. Click on the Multi-Scale Graphs command button, located below the taskbar, when enabled to activate multi-scale graphs. The Multi-Scale graph MMP12 PROFILE display is for a patient with two MMPI-2 tests.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/051.png)

#### Requesting Multi-Scale Graphs

Example: All previous administration selected tests attributes are available on the MMP12 scores window. To access any of the previous administration selected tests, from the Select MMp12 Date(s) list box select the most recent selected test date (shown in reverse chronological order), indicated by a check mark within the check box. The groups of scales for selected test are displayed in the SelectMMp12 Scales list box, located on the lower left side of window. All scale scores for each administration selected tests date appear in the Scale/Date list box, located on the lower right side of the window. The first group of selected scale scores is displayed in the center lower Scale list box. That group of scale scores for the most recent selected test is graphed and displayed in the ExpandedValidity Scale list box, located on upper right side of the window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/052.png)

#### Selecting Dates for Tests to be Graphed, Part 1

Example: From the MMP12 scores for Error window, the Select MMp12 Date(s) list box, located on the upper left side of the window, is displaying two check boxes showing two check marks for two different dates. To check or uncheck dates, click on the desired check boxcheck mark. Note: Checking any of the first five dates in the list will result in those tests being graphed. Checking any date found below the fifth test will result in a message saying only the first five dates can be graphed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/053.png)  
Selecting Dates of Tests to be Graphed, Part 2

Example: From the MMP12 scores for Error window, click on the date that is already checked mark in the check box located in the Select MMp12 Date(s) list box, located on the upper left side of the window. Note: If the date is already checked it will be unchecked. If the date is unchecked, it will be checked. If the date is not one of the five most recent dates, nothing will happen.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/054.png)

#### Selecting Scale Group, Part 1

Example: From the MMP12 scores for Error window, the Select MMp12 Scales list box is displayed in the lower left side of the window. To select a group of scale scores, click on the desired group displayed within the list box. The selected scale group names, dates, and scores are displayed in the Scales list box, located on the lower right side of the window. The Clinical Scales were chosen from the Select MMPI-2 Scale list box group of scale scores. The Clinical scale scores for the date checked were graphed. The Clinical Scales graph is displayed on the top right side of the window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/055.png)

### Selecting Scale Group, Part 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the MMP12 scores window, the Select MMP12 Scales list box is displayed in the lower left side of the window. To select a group of scale scores, click on the desired group of scale scores (Psychopathic Deviate (Harris-Lingoes)), displayed within the Select MMP12 Scales list box. The Scale list box is located in the lower center of the window displaying the selected scale group (Pd2 Authority Problems) names, dates, and scores. The MMPI-2 scale Psychopathic Deviate (Harris-Lingoes) group is graphed and displayed in the upper right side of window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/056.png)

### Copy Graph

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the MMP12 scores window, select the desired group of scale scores graph to be copied. Click on the Copy Graph command button, located on the bottom left side of the window to copy the desired group of scale scores graph. After the graph is copied the Mental Health Assistant Information dialog box is displayed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/057.png)

### Paste Graph

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The Mental Health Assistant Information dialog box is displaying text stating, “The graph has been copied to the Windows clipboard. If you like, you may paste it into another document (e.g., an MS Word document).” To paste a graph, click on the OK command button, located on the lower center of the Informationdialog box. The graph is pasted to the Windows clipboard.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/058.png)

### Print Graph

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the MMP12 scores for Error window, select the desired group of scale scores graph to be printed. Click on the Print Graph command button, located on the bottom left side of the window to print the desired group of scale scores graphs.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/059.png)

### Save Graph

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the MMP12 scores for Error window, click on the Save Graph tab, located on the bottom left side of the window to save a graph. A Save As dialog box is displayed. This allows the user to specify the directory path and filename to be used for saving the graph as a bitmap (BMP) file.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/060.png)

### Save As

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The Save As dialog box is displaying the current Mental Health Assistant default directory in the Save indrop down list box. The “Test Scores.bmp” format is the default file name displayed in this example.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/061.png)

### Copy Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the MMP12 scores window, click on the Copy Tabletab, located on the bottom center of the window. The table is then copied to the Windows clipboard.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/062.png)

### Paste Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The Mental Health Assistant Information dialog box is displaying text stating, “The table has been copied to the Windows clipboard. If you like, you may paste it into an open MS Excel spreadsheet”. Click on the OK command button, located on the lower center of the Informationdialog box to paste the table into open MS Excel spreadsheet.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/063.png)

### Print Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the MMP12 scores for Error window, select the desired table to be printed from the Select MMP12 Scales list box. Click on the Print Table tab, located on the bottom center of the window to print the selected table.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/064.png)

### Save Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the MMP12 scores for Error window, click on the Save Table tab, located on the bottom right side of the window to save a table. A Save As dialog box is displayed. This allows the user to specify the directory path and filename used for saving the table as a MS Excel (.xls) file.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/065.png)

### Save Table (continues)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The Save As dialog box is displaying the current Mental Health Assistant default directory in the Save indrop down list box. The “Test Scores.xls” Excel File extension is the default file name displayed in this example.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/066.png)

### Close

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the MMP12 scores for window, click on the Close command button (located on bottom right of window) and the main Mental Health Assistant Test Results window reappears.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/067.png)

### Close (continues)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: After clicking on the Close command button, the main Mental Health Assistant Test Results window reappears.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/068.png)

## Selecting and Administering New Psychological Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Order Tests Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Order Tests tab enables the user to order new tests to administer to selected patient and specify the data entry mode for the ordered tests. First, the user must specify the user’s name that is requesting the test to be ordered. By default, the user requesting the test to be ordered is identified as the session user. However, another user may be specified as the user requesting the test to be ordered, in which case, the original user’s name that requested the test is notified by E-mail that tests were administered in his/her name. The available set of tests that can be ordered depends on the user access privileges (i.e., whether the user ordering the test has the YSP key assigned).

#### Order Tests in Three Ways:

1\. An existing test battery may be selected (i.e., test batteries which are created in V*IST*A MHP database using the MHS Manager\Psych Test Utilities\Test Battery Utility \[YSTESTBAT\].

2\. An incomplete test may be restarted if it has not been too long since it was first started.

3\. New tests may be selected individually and their order of administration specified.

Order Tests Permits User to select one of three Data Entry Modes

1\. Staff entry, which is optimized for staff data entry when the staff person wishes to see test questions and answers while entering data.

2\. Clerk entry, which is optimized for staff data entry when the staff person does not wish to see test questions and answers while entering data. This is the best option to use for transcribing answers from an answer sheet.

3\. Patient entry, which is optimized for on-line administration of tests to the patient.

### Order Tests Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Patient entry invokes special security measures to prevent patients from using the PC for any other purpose than answering questions. Because security measures are not invoked for the staff entry and clerk entry modes, they must not be used for the on-line administration of tests to patients.

#### Tests Ordered By

Example: From the Mental Health Assistant main window, click on the Order Tests tab, located below the taskbar. Click on the Test Ordered By drop down list box scroll bardown arrow to select a different provider. After clicking on the Test Ordered By drop down list boxscroll bar arrow, a list of providers names are displayed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/069.png)

### Available Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Which tests appear in the Available Tests list box depends on the user’s access privileges to order tests (i.e., user must hold the YSP security key). By default, the user that ordered the test is identified as the MHA session user. However, another user may be specified as the user requesting the test to be ordered, in which case, the original user’s name that requested the test is notified by E-mail that tests were administered in his/her name.

Example: From the Mental Health Assistant Order Test window, to select an AvailableTest, click on the desired test name within the Available Tests list box, located below the taskbar. The selected text name is then highlighted and ready for transferring to the Tests Chosen list box, which is also, located below the taskbar. To transfer the selected test to the Tests Chosen list box,click on the \> right arrow transfer button, located on the column between the two list boxes. Alternatively, double-click on the desired test name in the Available Tests list box to transfer the desired test to the Tests Chosen list box.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/070.png)

#### AVAILABLE TEST transferred to Tests Chosen List Box

Example: From the Mental Health Assistant Order Test window, the Tests Chosen list box is displaying ONE test name that is transferred from the Available Tests list box to the Tests Chosen list box.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/071.png)

#### AVAILABLE TEST transferred to Tests Chosen

> **NOTE:** An asterisk (\*) is appended at the end of an incomplete test name.

Example: From the Mental Health Assistant Order Tests window, the Tests Chosen list box is displaying the TWO test names that were transferred from the Available Tests list box.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/072.png)

#### Transferring One TESTS CHOSEN back to Available Tests

Example: From the Mental Health Assistant Order Test window,select the desired test name(s) displayed in the Tests Chosen list box to transfer back to the Available Tests list box. When the desired test name(s) is highlighted, click on the \< left arrow transfer button, located on the column between the two list boxes to transfer the selected test back to the Available Tests list box. Alternatively, double-click on the desired test name(s) displayed in the Tests Chosen list box to transfer the selected test back to the Available Tests list box.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/073.png)

#### Transferring all AVAILABLE TESTS from Tests Chosen

Example: From the Mental Health Assistant Order Tests window,click on ALL test names displayed in the Tests Chosen list box, located below the taskbar to transfer back ALL tests to the Available Tests list box. When all test names are highlighted, click on the \<\<two left arrows transfer button, located on the column between the two list boxes to transfer ALL tests back to the Available Tests list box. Alternatively, double-click on all test names displayed in the Tests Chosen list box to transfer all tests back to the Available Tests list box.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/074.png)

#### All Tests Transferred back to Available Tests List Box

Example: From the Mental Health Assistant Order Tests window, the Tests Chosen list box is now empty. This illustrates that ALL tests have been transferred back the Available Tests list box.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/075.png)

### Restarting Incomplete Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Whether an incomplete test can be restarted depends on how long ago it was first entered in the V*IST*A Mental Health Package (MHP) database. The permissible lapse is a local site parameter that is set using MHS Manager\Psych Test Utilities\Edit Instrument Restart Limit \[YSINST RESTART LIMIT\] option. Incomplete tests entered using the clerk entry method of the MHP roll-and-scroll version, must be completed using the same method. Incomplete tests cannot be completed using the new MHA GUI software application. Such tests are shown in normal font.

Example: From the Mental Health Assistant Order Tests window, the Incomplete Tests list box, located below the Test Batteries list box displays an example of the incomplete test Date, Test name, and Items Answered in strikeout font.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/076.png)

### Restarting Incomplete Tests (continues)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restarting an incomplete test from the Available Tests list box is no different from starting a new test, so that process is not described here.

Example: From the Mental Health Assistant Order Tests window,Incomplete Test list box, located on the lower left side of the window displays all incomplete test Dates, Test names, and the number of Items Answered. Incomplete tests that can be restarted are shown in bold font in the Incomplete Test list box. These incomplete tests also are included in the Available Tests list box with an asterisk appended to the incomplete test name. An alternative method of restarting an incomplete test is to double-click on an incomplete test name displayed in the Incomplete Tests list box. To run the test, you may first have to start a test and then save the results before you complete the test.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/077.png)

### Restarting Incomplete Tests (continues)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Assistant Order Tests window, double-click on an incomplete test (bold font) displayed in the Incomplete Tests list box to move the incomplete test to the Available Tests list box.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/078.png)

### Restarting Incomplete Tests (continues)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example:Double clicking on the AUDIT incomplete test, located in the Incomplete Test list box moves the AUDIT incomplete test to the Tests Chosen list box, located below the taskbar on the right side of the window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/079.png)

### Test Batteries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Test Batteries Cannot Be Created Using MHA

Test batteries cannot be created using MHA software application. Instead test batteries must be created using the V*IST*A MHP, MHS Manager\Psych Test Utilities\Test Battery Utility \[YSTESTBAT\] option. Existing test batteries are displayed in the Test Batteries list box, located on the left side of the Mental Health Assistant Order Test window. *(TIP: If you are not sure which tests are in a battery, make sure [Show Hints](#selecting-show-hints) is checked and then single-click on the battery name. The names of the tests that comprise the battery will be shown).* If a battery contains a test not available to the user ordering the test, that test will not be administered

#### Transferring TEST BATTERIES to TESTS CHOSEN

Test batteries located within in the Test Batteries list box may be transferred to the Tests Chosen list box, by clicking on the testbattery nameonce until it becomes highlighted, and then clicking on the \> right arrow transfer command button, located to the right of the Test Batteries list box.Alternatively, double-clicking on the highlighted test battery name will also transfer the selected test battery from the Test Batteries list box to the Tests Chosen list box.

### Selecting a Test from Test Batteries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Assistant Order Tests window, the Test Batteries list box is located on the left side of the window, just below the taskbar. To select a test battery from the Test Batteries list box, click on the desired test battery name (i.e., NEUR2), which becomes highlighted and the test battery selection is completed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/080.png)

### Transferring TEST BATTERIES to TEST CHOSEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Assistant Order Tests window, the Test Batteries list box is located on the left side of the window, just below the taskbar. In this example, a battery named NEUR2 is highlighted, which is made up of the MISS and the STAI tests. To transfer the selection to the Tests Chosenlist box, either double-click on NEUR2 or click on the“\>”right arrow transfer command button, located to the right of the Test Batteries list box to transfer the MISS and STAI tests to the Tests Chosen list box.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/081.png)

### Staff Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Staff entry of test data permits the staff person to see the text of the test questions and answers as the data are entered. This might be the optimal method for entering staff rating data (e.g., AIMS or BPRS).

> **NOTE:** Because this data entry method does not secure the PC desktop, it should never be used for patient data entry.

Example: From Mental Health Assistant Order Tests window click on the Staff Entry command button located on the taskbar.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/082.png)

### Staff Entry (continues)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Order Tests window,click on the StaffEntry command button, located below the menu bar. If an invalid user click on the Staff Entry command button the Mental Health Assistant Informational dialog box appears alerting the user that, “This option is for staff use only. Using it with patients is likely to result in a serious breach of confidently. Are you sure you want to use the staff entry mode?” Click on the No command button located on right side of the Mental Health Assistant Informational dialog box to terminate this selection.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/083.png)

### Staff Entry (continues)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Order Tests window, click on the StaffEntry command button, located below the menu bar. The Mental Health Assistant Informational dialog box appears alerting the user that, “This option is for staff use only. Using it with patients is likely to result in a serious breach of confidently. Are you sure you want to use the staff entry mode?” Click on the Yes command button to continue. The Staff Entry CAGE window is displayed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/084.png)

#### Staff Entry Window

Example: This is an example of the Staff Entry window when a test is started. The name of the test is located on the Staff Entry window title bar (i.e., CAGE). The Staff Entry window contains a three-part display table, which is located just below the Staff Entrywindow title bar. The first part of the table contains the test instructions and the text first question. The second part of the table, located below the test instructions and the text first question table contains the response items. The third part of the table located below the response item table, lists the answers given to previous questions. This table is blank when a test begins because no previous questions have been answered.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/085.png)

#### Staff Entry Window (continues)

Example: From the Staff Entry window status bar, located at the bottom of the window contains the copyright Public Domain (i.e., test holder if any), No. of skipped items, Number of Items, and the Number Remaining.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/086.png)<u>Answering a Question from Staff Entry window</u>

To answer a question located on the Staff Entry window (i.e. CAGE), you may either click on the desired response in the list of response item, type in the first letter, or response item number of the desired response. The selected response is displayed in the list of previous answers and the next question is presented.

Example: On the third table, the user entered a Y in the Ans. text dialog box or clicked Y= Yes in the second table of the CAGE second question. That answer is shown in the table of previous answers, and question 2 is presented.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/087.png)  
<u>Previous</u>

The Previoustab located on the Staff Entry window (i.e. CAGE), enable the user to return to a previously answered question so the answer can be changed. By Clicking on the Previous tab previous test questions and answers are displayed. The answer entered for the previous test question is highlighted. Note: The Previous tab is not enabled if you are on the first question of a test.

Example: The user is on question 3 of the Staff Entry window (i.e., CAGE). Clicking on the Previous tab located on the bottom of the window will take the user back to question 2. Note: Before clicking on the Previous tab, the table of previous answers indicates that the patient’s answer to question 2 was No. When question 2 is presented again, No is highlighted in the set of possible answers.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/088.png)

#### Previous (continues)

Example: From the Staff Entry window (i.e., CAGE), the user is now previous on Question 2.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/089.png)  
Using the Vertical Scrolls Bar to Previous

The Previous command button returns the user to the previous question, which is fine if you want to back up to just one question. However, it is an inefficient way of jumping from, say, question 300 to question 180. A quicker way of returning to a much earlier question in the test is to use the vertical scrolls bar to scroll back in the table of previous answers to the question to which you want to return and then click on that row of the table. Scroll to a previous answer and click on that row of the table, the selected test question and answers are presented. The answer previously entered for the selected question is highlighted.

#### Using the Vertical Scrolls Bar to Previous (continues)

Example: Example: From the PTSD Checklist M window, the user is on question 13 of the PCLM and decides to change the answer to question 4. To do so, use the vertical scrolls bar, located on the lower right side of the window located on the third table to go back to the table of previous answers to question 4 and click on that row. Question 4 is then presented, and the previous answer is highlighted.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/090.png)

#### Using the Vertical Scrolls Bar to Previous (continues)

Example: The user is now returned to Question 4, located on the PTSD Checklist M window. Below the Question 4 table, 2 A little bit is selected and highlighted in that row of the second table.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/091.png)

### New Question

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the PTSD Checklist M window, the New Questioncommand button, which is enabled only if the user is not on the first remaining unanswered question in the test, jumps to the next unanswered question.

Back up to a previous question will enable the New Questionbutton. Click on the New Questionbutton and the next unanswered question is presented and the New Questioncommandbutton is disabled.

#### New Question (continues)

Example: The user had entered answers for the first 15 questions of the PCLM before returning to question 4 to change that answer (see previous example). The Staff Entry window advanced to question 5, but the user wanted to go back to question 15, which is the next unanswered question. Clicking on the New Question button accomplished this.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/092.png)

#### New Question (continues)

Example: From the PTSD Checklist M window, using the New Question button, question 16 is now displayed in the table.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/093.png)

### Close/Continue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PTSD Checklist M window contains the Close command button, located on the bottom right side of the window. The Close command button will display Continue if the current test is not the last test in the set of tests ordered, and is showing Close, if it is the last test. In either case, clicking on the Close button triggers the following sequence of events:

MHA checks to see if the current test is completed.

If the test is completed, the answers are saved to V*IST*A without asking the user.

If the test is not completed, the user is asked if she/he wants to complete it.

a\) If the user says YES, the sequence is terminated and the user is returned to the Staff Entry window.

b\) If the user says NO, he/she is asked if she/he wants to save the incomplete results. If the user says yes, incomplete results are saved. Otherwise, they are not.

4\. If the current test is not the last test in the set of tests ordered (i.e., the button caption says Continue), the next test in the set is started.

5\. If the current test is the last test in the set of tests ordered (i.e., the button caption displays Close), the staff entry form closes and the Test Results tab of the main form is shown.

Click on the Close/Continue command button under various conditions (e.g., one test ordered, multiple tests ordered, current test complete or not complete). Steps 1-5, as described above, are followed depending on the specific conditions in effect.

### Close/Continue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The following example is displaying question 15 of the 17 questions in the PCLM. PCLM is the only test selected (or is the last test in the list), so the Close command button displays Close. Clicking on the Close command button displays the following two Mental Health Assistant Information dialog boxes.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/094.png)

#### Mental Health Assistant Information Dialog Box YES command

Example: The Mental Health Assistant Information dialog box text is stating, “This PCLM is not completed yet. Do you want to finish it now?” If the YES command button is selected, the Staff Entry window is displayed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/095.png)

#### Mental Health Assistant Information Dialog Box NO command

If the NO command button is selected, Mental Health Assistant Information dialog box text is stating, “PCLM answers have not been saved to V*IST*A. Do you want to save those answers now?” If the YES command button is selected, the answer is saved. Note: Whether you say yes or no to the question about saving answers, the Staff Entry window will close because you said you did not want to finish the PCLM and there is no other test to administer.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/096.png)

### Clerk Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Clerk Entry is the optimal way of transcribing test results from an answer sheet when the user does not need to see the text of the test questions and answers as the data are entered. Because this data entry method does not secure the PC desktop, it should never be used for patient data entry.

Example: From Mental Health Assistant Order Tests tab window, click on the ClerkEntry command button, located on the taskbar to activate the ClerkEntry function. Once this function is activated the Mental Health Assistant Information dialog box will appear alerting the user this function is for staff use ONLY.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/097.png)

### Mental Health Assistant Information dialog box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The Mental Health Assistant Informational dialog box appears alerting the user that, “This option is for staff use only. Using it with patients is likely to result in a serious breach of confidently. Are you sure you want to use the clerk entry mode?” Click on the YES command button to access the PTSD Checklist M window for the first selected test.

> **NOTE:** Clicking the NOcommand button returns the user back to the Mental Health Assistant Order Tests tab window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/098.png)

### PTSD Checklist M window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The PTSD Checklist M window status bar, located on the bottom of the window displays the test current item number, valid choices for that item, and total number of items in the test. The number of cells in the data entry table equals to the number of items in the test, up to 10 cells per row. The data entry table column heading (Item No.) specifies the question number within the group of questions for a given row.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/099.png)

#### Entering Data

Example: To speed up the data entry process, use the keyboard to enter a valid choice. That choice is inserted into the corresponding cell of the table and the next cell is highlighted, and a 1 is typed the text box. Compare the following window display with the previous example. Note: A 1 was inserted in cell 1 and cell 2 is highlighted.

<span id="_Changing_a_Previous" class="anchor"></span>![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/100.png)

#### Changing a Previous Answer

> **NOTE:** You cannot skip a question by clicking on a cell that follows the first unanswered question. In the following example you cannot skip question 16 by clicking on cell 17. You must answer question 16 first. If you want to skip question 16, highlight that cell and type “X” into the cell text box.

Example: From the PTSD Checklist M window, click on the cell of a previous question and type in a valid entry. That entry is inserted into the corresponding cell text box and the next cell text box is highlighted. The user entered 15 answers for the PCLM and then clicked on cell 12 to change the answer to question 12. Cell 12 is highlighted to indicate it is the active cell. The status bar, located on the bottom of the window is updated to reflect the item number and valid entries for the highlighted cell text box.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/101.png)

#### Date Test Administered

Example: The calendar is, by default, set to today’s date. Because the user may be transcribing the results of a test the patient took on an earlier date, the calendar can be changed to select a previous date. However, a future date cannot be selected. Click on the Date Test Administered drop-down arrow, located to the right of the date, and a pop-up calendar appears. Click first on a future date and then an earlier date. Clicking on a future date does nothing. Clicking on an earlier date changes test administration date. The calendar is displaying a test administered on March 7, 2003, and transcribed on March 12, 2003.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/102.png)

### Jump

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example:Note, If you have gone back to change an answer to previously answered question, the Jump command is enabled. From the PTSD Checklist M window, click on a previous answer to enable Jump. Click on the Jump command button and the first empty cell is highlighted. If 15 questions have been answered but question 12 is highlighted, the Jumpcommand button is enabled (see [*Changing a Previous Answer*](#_Changing_a_Previous)). Clicking on the Jumpcommand button highlights cell 16, which is the first unanswered question.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/103.png)

### Close

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The behavior of the Close command button is the same as that of the [Continue/Close button](#closecontinue) on the staff entry form.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/104.png)

### Patient Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Entry supports the on-line testing of patients, which is by far the most common method of computerized testing in VHA. Patient Entry is a simplified version of the [Staff Entry](#staff-entry) (the table of previous answers is not shown) with added security features to prevent unattended patients from using the PC for unauthorized purposes.

Example: From the Mental Health Assistant Order Tests tab window, click on Patient Entry command button, located on the taskbar to activate the Patient Entry function. After clicking on the Patient Entry the secured desktop functionality is activated and Mental Health Assistant Warning dialog box is displayed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/105.png)

#### First Warning dialog box

Example: The <u>first</u> Warning dialog box is displayed each time the Patient Entry is selected stating, “Are you prepared to continue now?” Clicking the YES command button continues on to the second the Mental Health Assistant Warning dialog box. Note: Clicking on the Cancel command button will exit the application and return back to the PC desktop.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/106.png)

#### Second Warning dialog box

Example: The <u>second</u> Warning dialog box text is stating, “Use only Alpha-numeric keys on the keyboard from this point on.” Click the OKcommand button to continue to the three-part display test entry table.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/107.png)

## Addiction Severity Index (ASI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ASI Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This window lists all previous ASI interviews and makes it easy to view either the item report or narrative report for a selected interview. To help with ASI performance measure compliance, the interval since the last interview is displayed in the status bar.

Example: From the Mental Health Assistant main window, click on the ASI tab, (located at the bottom of the window) to view the ASI Window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/108.png)

#### Selecting a Previous Interview

Example: To select a pervious interview, click on the desired previous interview shown within the list box (located just below the taskbar).

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/109.png)

#### Selecting Report Option

Example: From the ASI window, the Report Option, is located on the right side of the list box, displays the Narrative Report or Item Report options. Click on Narrative Report or Item Report to make a selection.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/110.png)

### ASI Data Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The New ASI button, when clicked, provides user-friendly interface for entering interview data. This new function enables staff to quickly enter data, to easily jump from one item to another, and to enter free-text comments at any time. The ASI Data Entry should greatly reduce data entry time, whether transcribing interview results from a paper form or entering them on-line during an interview. Note: The ASI Data Entry is not a self-administered version of ASI, and should not be used for patient entry of ASI responses.

Example: From the ASI window, click on the New ASI command button, located on the task bar to activate the ASI Data Entry form.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/111.png)

Example: When the New ASI button is clicked, the ASI data entry form is presented. The General Information section is shown with its first item highlighted The first item, G3, is automatically set to the user's last selection. In addition, the items G4. Date of Admission and G5. Date of Interview, contains today’s date as defaults; item G9. Contact Type is set to 1. In person and G11. Interviewer is set to the staff member who logon to MHA; item G12. Special is set to N. Interview completed. The status bar at the bottom of the window provides context sensitive hints for the active test item.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/112.png)

ASI utilizes several types of window components, such as, the drop-down list box, check boxes, radio buttons, etc. The use of these components is explained below.

#### Drop-Down List Box

Example: In the General Information section, click on the down arrow of Item G3. Program Type. The drop-down list box contains 21 ASI program types, which are displayed eight at a time.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/113.png)

#### Drop-Down List Box Navigation and Selection:

There are several ways to select the desired program type in item G3. Program Type and we will use this as an example for all drop-down list boxes in the ASI.

1\) Use the keyboard up and down arrow keys to navigate through the list of program types in item G3. Program Type. The highlighted item will move as you press the arrows. To select the desired program, press the Enter key.

2\) Type in the first few letters of the desired program in the text entry box. The full name of the program will appear, if this is the desired program, press the Enter key and you will move to the next ASI item.

3\) Using the mouse, click on the vertical scroll bar, located on the right side of the drop-down list box, to slide up or down to view the list of programs. Click on the desired program and it will appear in the text entry box and the drop-down list will disappear.

4\) With the mouse, click on the vertical scroll bar up and down arrows to view the list of program types. To select the G3. Program Type using the keyboard, press the Tab or Enter key. The highlighted item is selected.

#### Date Items - Part I

Example: Click on the down arrow of Item G4. Date of Admission and a calendar will appear. The status bar hints (located at the bottom of this window) are updated and displayed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/114.png)

Date Item Navigation and Selection:

To navigate the calendar using the keyboard, follow these instructions:

Press the left and right arrow keys to change days.

Shift-left and shift-right to change months.

Pressing the Home key moves to the first day of the month.

Press the Tab or Enter key to select the date and to close the calendar.

Clicking the mouse on a day will select the day and close the calendar.

Clicking on the left and right arrows will change the month.

Date Fields - Part IIExample: Type a date in the text entry box of G4. Date of Admission. Date entry for this item can be simple text that conforms to various date templates. The date can be typed directly in the text entry box. The following formats are accepted: 4/14/2001, 4-14-01, 4.14.01, and 4,14,2001. Notice that the year can be entered as last two digits or four digits. Acceptable delimiters are the backslash, period, comma and dash. Note: Future dates are not accepted.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/115.png)

#### Check Boxes and Check Marks

Example: Item G8. Interview For (ASI Type): click on a check box (or its text), and a check mark appears in the check box. Other check marks, if present, are removed. Using the keyboard, press the keys “1”, “2”, or “3” and the appropriate check box is checked and the next ASI item is highlighted. While mouse input is effective, experienced users find keyboard entry to be quicker and easier. If an incorrect key is pressed, an error message will appear.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/116.png)

  
Check Boxes Navigation and Selection:

To make a choice in the check box, do one of the following:

1\) Type the number on the keyboard that corresponds to the choice. This is the fastest way to enter data in the ASI. You will notice that the choice will be checked (other boxes that might have been checked will become blank). The program will move automatically to the next ASI item (if the “Speed Tab” option is active).

2\) Click on the choice.

#### Spin Edit - Part I

Example: In item G14 How long have you lived at this address, type the number of years—an acceptable number is from 0 to 99—and then press either the Tab or Entry key. The “Months:” will then become the active item and is highlighted. If an incorrect number is entered, an error message will appear.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/117.png)

#### Spin Edit - Part II

Example: Click on the up or down arrows of the spin-edit field of item G14. The number in the spin-edit box will increase or decrease by one. The spin-edit item can be increased by one when the up arrow receives a mouse click, or when the up-arrow key is pressed. To decrease the value, click on the down arrow or press the down arrow key. A number will not increase beyond the limit of the acceptable range. To move to the next item, press the Tab or Enter key.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/118.png)

  
With the general description of the ways to enter data into the ASI data entry form—drop-down list, date fields, and so on—there are two items that may need a more complete description, Item G8 and Item G12.

#### Item G8 - Part I

The ASI is a questionnaire with three different versions; Full Intake, Lite Intake and Follow-up. When the user makes a selection on Item G8, the computer screen may change momentarily to provide the proper list of items for that version of the ASI. The Full Intake version of the ASI is presented initially by default.

Example: Click on the 2.Lite Intake on Item G8. Since the user may have entered data before selecting the form to use—Full, Lite, or Follow-up—this dialog window allows the user to either use the default responses, or to maintain the responses already completed. This avoids the removal of user-entered data.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/119.png)

#### Item G8 - Part II

Example: The Addiction Severity Index Informationdialog box states, “Do you wish to set the items that follow to their default response? \[This may change responses you have already entered.\]”

Click the Yes button located within the Informationdialog box and the Lite Intake items will appear with default values set for: G3, G4, G5, G9, and G11.

Click on the No button located within the ASI Informationdialog box. Lite Intake items will appear without default values set for G3, G4, G5, G9 and G11, maintaining the values entered by the user.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/120.png)

#### Item G8 - Part III

Example: The 3. Follow-up is selected by the user on Item G8. Notice that the items have changed in comparison the initial Full ASI items.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/121.png)

#### Item G8 – Part IV

Example: If the user incorrectly selects Item G8. Interview Form (ASI Type) - 3. Follow-up for a new patient, who has never had a Full Intake or Lite Intake, the Addiction Severity Index Informationdialog box is displayed stating, “This is the veteran’s first ASI and it must be either a Full or Lite Intake.”

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/122.png)

#### Item G12

Example: On Item G12, click on:

1. Patient Terminated or
2. Patient Refused or
3. Patient unable to respond

The following Mental Health Assistant Information dialog box is displayed indicating that default values will not be set for the user.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/123.png)

#### Item G12 (continued)

Example: The Addiction Severity Index Information dialog box is displayed indicating, “The many default answers provided on this form will not be honored when an ASI is only partially completed. Only the items that you actually answer will be saved.”

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/124.png)

#### Item G19 - Part I

Example: Click on 6. Other (Specify) on Item G19. G20 will become active. The edit box is active only when item G19 is “6Other (Specify)”. Otherwise the edit box is disabled (user cannot write to it).

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/125.png)

#### Item G19 - Part II

Example: Item G19, click on:

1. No or
X. Not Answered or
N. Not Applicable.

The edit box below, if active become inactive and G20 will also become inactive with a value of “N”.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/126.png)

There are a number of items in the ASI that become inactive (no user response is possible) when a previous item is answered in a certain way. This is done to speed data entry and to avoid errors.

#### Medical Status

Example: Click on the tab labeled Medical, located on the left side at the bottom of the form. The data entry form will move to the Medical Status section of the ASI. By pressing the Alt-M keys, the same result will occur. This is the same procedure for moving to any of the other sections of the ASI—click on the tab or press Alt-Key (the proper key is underlined on the tab label, e.g., G for General Information, M for Medical).

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/127.png)

#### Medical Status Comments

Example: Type comments in the Medical Status Comments text box, located on the bottom of the form. The Medical Status Comments text box accepts free text. Each section of the ASI has a comment text box.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/128.png)

### Selecting an Unsigned ASI 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the ASI window, click on the desired interview shown in the list box containing a NO response (located under the Signed heading in the title bar) to select an unsigned ASI-MV interview. After the selection is made (highlighted), double-clicking on the highlighted selection will update the report before proceeding onto the Electronic Signature form. Note: Clicking on a Signed ASI-MV also performs the same function.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/129.png)

#### Previously Signed ASI 

Example: After selecting a signed ASI, the following Mental Health Assistant dialog box is displayed stating, “A signed ASI cannot be changed or edited.” Click on the OK button to return back to the ASI window.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/130.png)

### Business Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Business rules check to see whether pairs of responses are logically consistent. The table below lists all of these rules and their actions.

Example: Select a rule from the table below. Answer the specified items in a way that should trigger a message. The specified message should appear.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 49%" />
<col style="width: 10%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Item #'s</strong></th>
<th><strong>Coding Error</strong></th>
<th><strong>Cross Check Message</strong></th>
<th><p><strong>Yes/No</strong></p>
<p><strong>OK</strong></p></th>
<th><strong>Cursor movement</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>G19 and G20</td>
<td>G19&gt;1, and G20=0,00, or N</td>
<td>In the last question (G19), you recorded that the patient has been in a controlled environment in the past 30 days, this question, (G20) how many days, should be greater than 0.</td>
<td>OK</td>
<td>Pop-up after G20 is entered. Cursor doesn't move.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>G19 and M1</td>
<td>G19=4, and M1=0, 00, N.</td>
<td>You recorded in the general information section (G19), that the patient had been hospitalized for medical problems in the past 30 days. This hospitalization would usually be coded in this question. Do you want to recode M1?</td>
<td>Yes/No</td>
<td>Pop-up after M1 is entered. If <strong>"Yes"</strong>, the cursor doesn't move. If <strong>"No"</strong>, cursor moves to M3.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>G19 and M2</td>
<td>G19=4 and M2 years or months &gt;0, 00, or N.</td>
<td>In the general information section (G19), you recorded that the patient had been hospitalized this month for medical problems. The correct coding in M2 is usually 00 00 in this case. Do you want to recode M2?</td>
<td>Yes/No</td>
<td><p>After M2 is entered.</p>
<p>If <strong>"Yes"</strong>, the cursor doesn't move. If <strong>"No"</strong>, cursor moves to M3.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>M6 and M7</td>
<td>M6&gt;0, and M7=0.</td>
<td>In the last question, you recorded that the patient experienced some medical problems in the past 30 days. If this were true, then we would expect that the patient would be at least slightly bothered by these problems. Do you want to recode M7?</td>
<td>Yes/No</td>
<td>After M7 is entered. If <strong>"Yes"</strong>, the cursor doesn't move. If <strong>"No"</strong>, cursor moves to M8.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>M6, M7 and M8</td>
<td>M6=0 or 00, and M7 or M8&gt;0.</td>
<td>In question M6, you recorded that the patient experienced no medical problems in the past 30 days, since they report being troubled or wanting treatment (M7 or M8), it is fair to expect that they had some problem days. Go back to M6 and identify the number of days the problem has bothered them.</td>
<td>OK</td>
<td><p>After M8 is entered.</p>
<p>Cursor moves back to M6.</p></td>
</tr>
</tbody>
</table>

Example: Select a rule from the table below. Answer the specified items in a way that should trigger a message. The specified message should appear.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 49%" />
<col style="width: 10%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>E1a</td>
<td>E1a&lt;4</td>
<td>You are reporting that the patient has had less than 4 years of education, this is rare. Please review this; did you include home schooling, grade school, etc.? Do you want to change E1?</td>
<td>Yes/No</td>
<td>Pop-up after E1b is entered. If <strong>"Yes"</strong>, the cursor moves to E1a. If <strong>"No"</strong>, cursor moves to E2.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>E4 and E5</td>
<td>E4=0 and E5=1</td>
<td>If the client does not have a driver's license, E5 is always coded as <strong>"No"</strong>. This is because E5 asks about the car as a way of evaluating ability to travel to and from a job. If the client does not have a license, they cannot "get credit" for having a car! The computer has made this change for you.</td>
<td>OK</td>
<td><p>Pop-up after E5 is entered.</p>
<p>This is a forced change – there is not an option to leave E5=1 if E4=0.</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>E8 and E9</td>
<td>E8=0 and E9=1</td>
<td>In the last question (E8), you said no one contributes to the client's support, and in this question, you are saying the client gets most of his or her support from someone. Do you want to change your answer in E8?</td>
<td>Yes/No</td>
<td>Pop-up after E9 is entered. If <strong>"Yes"</strong>, the cursor moves to E8. If <strong>"No"</strong>, cursor moves to E10.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>E11 and E12</td>
<td>E11=0 or 00 and E12&gt;0</td>
<td>In the last question (E11), you recorded that the patient was not paid for working at all in the past month. If this is the case, E12 is generally $ 0. Do you want to change E11?</td>
<td>Yes/No</td>
<td>Pop-up after E12 is entered. If <strong>"Yes"</strong>, the cursor moves to E11. If <strong>"No"</strong>, cursor moves to E13.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>E11&gt;0 and E12=0, 00, 000, or 0000</td>
<td>In the last question (E11), you recorded that the patient was paid for working this month. If this is the case, E12 is generally not $ 0, unless the patient has collected no money for their work. Do you want to change E12?</td>
<td>Yes/No</td>
<td>Pop-up after E12 is entered. If <strong>"Yes"</strong>, the cursor doesn’t move. If <strong>"No"</strong>, cursor moves to E13.</td>
</tr>
</tbody>
</table>

Example: Select a rule from the table below. Answer the specified items in a way that should trigger a message. The specified message should appear.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 49%" />
<col style="width: 10%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>E15 and M5</td>
<td>E15=0, 00, 000, 0000, or 00000 and M5=1</td>
<td>You recorded earlier (M5), that the patient receives a pension for a medical problem. This income is generally recorded in E15 unless they did not receive any cash this month. Do you want to change E15?</td>
<td>Yes/No</td>
<td>Pop-up after E15 is entered. If <strong>"Yes"</strong>, the cursor doesn’t move. If <strong>"No"</strong>, cursor moves to E16.</td>
</tr>
<tr class="odd">
<td>E19 and E20</td>
<td>E19&gt;0 and E20=0</td>
<td>In E19, you recorded that the patient experienced some employment problems in the past 30 days. If this were true, then we would expect that the patient would be at least slightly bothered by these problems. Do you want to recode E20?</td>
<td>Yes/No</td>
<td>Pop-up after E20 is entered. If <strong>"Yes"</strong>, the cursor doesn’t move. If <strong>"No"</strong>, cursor moves to E21.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>D1a and D2a</td>
<td>D2a &gt;D1a</td>
<td>You recorded that the patient drank "to intoxication" (D2) more days than total number of days drinking any alcohol at all (D1). Probe and recode D1. Remember D2 is a sub-set of D1.</td>
<td>OK</td>
<td><p>After D2a is entered.</p>
<p>Cursor moves to D1a.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>D1b and D2b</td>
<td>D2b &gt; D1b</td>
<td>You recorded that the patient drank "to intoxication" (D2) more years than total number of years drinking any alcohol at all (D1). Probe and recode D1. Remember D2 is a sub-set of D1.</td>
<td>Ok</td>
<td><p>After D2b is entered.</p>
<p>Cursor moves to D1b.</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>D1-D12 and G20</td>
<td>G20&gt;0 and any item D1a-D12a=30</td>
<td>You recorded in the general information section that the patient had been in a controlled environment in the past month, yet they used either drugs or alcohol every day. Please review this. Do you want to change any information in the drug/alcohol grid?</td>
<td>Yes/No</td>
<td>Pop-up after D12a is entered. If <strong>"Yes"</strong>, the cursor moves to D1a. If <strong>"No"</strong>, cursor moves to D12b.</td>
</tr>
</tbody>
</table>

Example: Select a rule from the table below. Answer the specified items in a way that should trigger a message. The specified message should appear.

|                  |                              |                                                                                                                                                                                                                                                           |        |                                                                                                        |
|------------------|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------|
|                  |                              |                                                                                                                                                                                                                                                           |        |                                                                                                        |
| D14 and D1-D12   | D14=3 - 12 or 16 and D1a\>15 | You report that the patient's problem does not include alcohol, however, the patient used alcohol at least 15 days in the past month. Please review this and consider option "Alcohol and one or more drugs" for question D14. Do you want to change D14? | Yes/No | Pop-up after D14 is entered. If "Yes", the cursor does not move. If "No", cursor moves to D15. |
|                  |                              |                                                                                                                                                                                                                                                           |        |                                                                                                        |
| D16 and D1a-D12a | D16=0 or 00 and D1a-D12a\>0  | You recorded that the patient is "still sober", however, drug or alcohol use in the past 30 days is documented in the drug and alcohol grid. Please review this. Do you want to change D16?                                                               | Yes/No | Pop-up after D16 is entered. If "Yes", the cursor does not move. If "No", cursor moves to D17. |
| D17              | D17\>5                       | You recorded more than 5 episodes of DT's for this patient. This is extremely rare, please review the definition of DT's if you are unsure. Do you want to change it?                                                                                     | Yes/No | Pop-up after D17 is entered. If "Yes", the cursor does not move. If "No", cursor moves to D18. |
| D19 and D21      | D19=0 or 00 and D21\>00      | You recorded that the patient never had any treatments for alcohol abuse, so \# of detox treatments is not applicable. Do you want to recode (D19), the total number of treatments received?                                                              | Yes/No | Pop-up after D21 is entered. If "Yes", the cursor moves to D19. If "No", cursor moves to D23.  |
|                  |                              |                                                                                                                                                                                                                                                           |        |                                                                                                        |
| D19 and D21      | D19\>0, and D21\>D19         | You recorded that the patient had more detox treatments than the total number of treatments received for alcohol abuse. Remember D21 is a sub-set of D19. Do you want to recode D19?                                                                      | Yes/No | Pop-up after D21 is entered. If "Yes", the cursor moves to D19. If "No", cursor moves to D23.  |

Example: Select a rule from the table below. Answer the specified items in a way that should trigger a message. The specified message should appear.

|                    |                                                          |                                                                                                                                                                                                                                                                                                                                |        |                                                                                                        |
|--------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------|
|                    |                                                          |                                                                                                                                                                                                                                                                                                                                |        |                                                                                                        |
| D20 and D22        | D20\>0, and D22\>D20                                     | You recorded that the patient had more detox treatments that the total number of treatments received for drug abuse. Remember D22 is a sub-set of D20. Do you want to recode D20?                                                                                                                                              | Yes/No | Pop-up after D22 is entered. If "Yes", the cursor moves to D20. If "No", cursor moves to D24.  |
|                    |                                                          |                                                                                                                                                                                                                                                                                                                                |        |                                                                                                        |
| D20 and D22        | D20=0 or 00 and D22\>00                                  | You recorded that the patient never had any treatments for drug abuse, so \# of detox treatments is not applicable. Do you want to recode (D20), the total number of treatments received?                                                                                                                                      | Yes/No | Pop-up after D22 is entered. If "Yes", the cursor moves to D20. If "No", cursor moves to D24.  |
|                    |                                                          |                                                                                                                                                                                                                                                                                                                                |        |                                                                                                        |
| D3a-D12a, and, D24 | Any item D3a-D12a\>0 and D24=0, 00, 000, 0000, or 00000. | You recorded days of drug use in the past 30 days, but no money spent on drugs, please review this. Do you want to change D24?                                                                                                                                                                                                 | Yes/No | Pop-up after D24 is entered. If "Yes", the cursor does not move. If "No", cursor moves to D25. |
| D26, D28, and D30  | D26\>0 and D28 and/or D30=0                              | In an earlier question (D26), you recorded that the patient had experienced some days with alcohol problems in the past 30 days. If this is true, then we would expect the patient would be at least slightly bothered or slightly in need of treatment for these problems. Do you want to change your code on D28 and/or D30? | Yes/No | Pop-up after D30 is entered. If "Yes", the cursor moves to D28. If "No", cursor moves to D27.  |
|                    |                                                          |                                                                                                                                                                                                                                                                                                                                |        |                                                                                                        |
| D26, D28, and D30  | D26=0 or 00 and D28 or D30\>0.                           | In an earlier question (D26), you recorded that the patient had no alcohol problems in the past 30 days. Since they report being troubled or wanting treatment, it is fair to expect that they had some problem days. Go back to D26 and identify the number of days the problem has bothered them.                            | OK     | Pop-up after D30 is entered. Cursor moves to D26.                                                      |

Example: Select a rule from the table below. Answer the specified items in a way that should trigger a message. The specified message should appear.

|                         |                                          |                                                                                                                                                                                                                                                                                                                            |        |                                                                                                        |
|-------------------------|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------|
|                         |                                          |                                                                                                                                                                                                                                                                                                                            |        |                                                                                                        |
| D27, D29, and D31       | D27\>0 and D29 and/or D31=0              | In an earlier question (D27), you recorded that the patient had experienced some days with drug problems in the past 30 days. If this is true, then we would expect the patient would be at least slightly bothered or slightly in need of treatment for these problems. Do you want to change your code on D2 and/or D31? | Yes/No | Pop-up after D31 is entered. If "Yes", the cursor moves to D29. If "No", cursor moves to D32.  |
|                         |                                          |                                                                                                                                                                                                                                                                                                                            |        |                                                                                                        |
| D27, D29, and D31       | D27=0 and D29 or D31\>0.                 | In an earlier question (D27), you recorded that the patient had no problems with drugs in the past 30 days. Since they report being troubled or wanting treatment, it is fair to expect that they had some problem days. Go back to D27 and identify the number of days the problem has bothered them.                     | OK     | Pop-up after D31 is entered. Cursor moves to D27.                                                      |
|                         |                                          |                                                                                                                                                                                                                                                                                                                            |        |                                                                                                        |
| L3-L16 and L17          | L3 through L16 total \> L17              | You recorded the patient had more convictions than the total number of times they were arrested and charged (L3 to L16). This is unusual. Do you want to change L17?                                                                                                                                                       | Yes/No | Pop-up after L17 is entered. If "Yes", the cursor does not move. If "No", cursor moves to L18. |
|                         |                                          |                                                                                                                                                                                                                                                                                                                            |        |                                                                                                        |
| L2 and L3-L16, L18-L20. | L2=1 and all L3-L16 and L18-L20=0 or 00. | In an earlier question (L2), you indicated the patient is on probation or parole. However, no arrests or charges are documented in items L3-L20. Do you want to recode any legal charges?                                                                                                                                  | Yes/No | Pop-up after L20 is entered. If "Yes", the cursor moves to L3. If "No", cursor moves to L21.   |
|                         |                                          |                                                                                                                                                                                                                                                                                                                            |        |                                                                                                        |
| L24 and L3-L16, L18-L20 | L24=1, and L3-L16 and L18-L20=0 or 00    | You recorded the patient is awaiting charges, trial or sentence (L24), but no arrests and/or charges are coded in L3-L16 or L18-L20. Do you want to recode any of the charges?                                                                                                                                             | Yes/No | Pop-up after L24 is entered. If "Yes", the cursor moves to L3. If "No", cursor moves to L25.   |

Example: Select a rule from the table below. Answer the specified items in a way that should trigger a message. The specified message should appear.

|                   |                                    |                                                                                                                                                                                                                                                                                                                    |        |                                                                                                        |
|-------------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------------------------------------------------------------------------------------------------------|
|                   |                                    |                                                                                                                                                                                                                                                                                                                    |        |                                                                                                        |
| L24 and L25       | L24=0, and L25\>0                  | You recorded the patient was not awaiting charges, trial or sentence (L24), yet you coded a charge in L25 (which would be not applicable). Do you want to recode L24?                                                                                                                                              | Yes/No | Pop-up after L25 is entered. If "Yes", the cursor moves to L24. If "No", cursor moves to L26.  |
|                   |                                    |                                                                                                                                                                                                                                                                                                                    |        |                                                                                                        |
| L26 and G19       | G19=2 and L26=0 or 00              | In the general information section, you recorded that the patient had been in jail in the past 30 days, this is usually also represented in L26. Do you want to change your code on L26?                                                                                                                           | Yes/No | Pop-up after L26 is entered. If "Yes", the cursor does not move. If "No", cursor moves to L27. |
|                   |                                    |                                                                                                                                                                                                                                                                                                                    |        |                                                                                                        |
| L27 and E17       | E17\>0 and L27=00                  | In the employment section, you recorded that the patient had illegal income in the past 30 days, this is usually also documented in L27. Do you want to change your code on L27?                                                                                                                                   | Yes/No | Pop-up after L27 is entered. If "Yes", the cursor does not move. If "No", cursor moves to L28. |
|                   |                                    |                                                                                                                                                                                                                                                                                                                    |        |                                                                                                        |
| F30, F32, and F34 | F30\>0 and F32 and/or F34=0        | In an earlier question (F30), you recorded that the patient had some family conflicts in the past 30 days. If this is true, then we would expect that the patient would be at least slightly bothered or slightly in need of treatment. Do you want to recode F32 or F34?                                          | Yes/No | Pop-up after F34 is entered. If "Yes", the cursor moves to F32. If "No", cursor moves to F31.  |
|                   |                                    |                                                                                                                                                                                                                                                                                                                    |        |                                                                                                        |
| F30, F32, and F34 | F30=0 or 00 and F32 and/or F34\>0. | In an earlier question (F30), you recorded that the patient had no family conflicts in the past 30 days. Since they report being troubled or wanting treatment, it is fair to expect that they had some problem days. Do you want to go back to F30 and identify the number of days the problem has bothered them? | Yes/No | Pop-up after F34 is entered. Cursor moves to F30.                                                      |

Example: Select a rule from the table below. Answer the specified items in a way that should trigger a message. The specified message should appear.

|                   |                                                             |                                                                                                                                                                                                                                                                                                                         |        |                                                                                                               |
|-------------------|-------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------|
|                   |                                                             |                                                                                                                                                                                                                                                                                                                         |        |                                                                                                               |
| F31, F33, and F35 | F31\>0 and F33 and/or F35=0                                 | In an earlier question (F31), you recorded that the patient had some conflicts with others in the past 30 days. If this is true, then we would expect that the patient would be at least slightly bothered or slightly in need of treatment for this recent problem. Do you want to recode F33 or F35?                  | Yes/No | Pop-up after F35 is entered. If "Yes", the cursor moves to F33. If "No", cursor moves to F36.         |
|                   |                                                             |                                                                                                                                                                                                                                                                                                                         |        |                                                                                                               |
| F31, F33, and F35 | F31=0 and F33 or F35\>0.                                    | In an earlier question (F31), you recorded that the patient had no conflicts with others in the past 30 days. Since they report being troubled or wanting treatment, it is fair to expect that they had some problem days. Do you want to go back to F31 and identify the number of days the problem has bothered them? | Yes/No | Pop-up after F35 is entered. Cursor moves to F31.                                                             |
|                   |                                                             |                                                                                                                                                                                                                                                                                                                         |        |                                                                                                               |
| P1, P2 and P10a/b | P1 + P2=0 or 00 and P10 a or b (past 30 days or lifetime)=1 | You recorded that the patient has not had inpatient or outpatient treatment for psychiatric problems (P1 and P2), yet they have attempted suicide. Please review treatment they may have received for the suicide attempt. Do you want to recode P1 or P2?                                                              | Yes/No | Pop-up after P10a and b are entered. If "Yes", the cursor moves to P1. If "No", cursor moves to P11a. |
|                   |                                                             |                                                                                                                                                                                                                                                                                                                         |        |                                                                                                               |
| P1, P2 and P11a/b | P1 + P2=0 or 00 and P11 a or b (past 30 days or lifetime)=1 | You recorded that the patient has not had inpatient or outpatient treatment for psychiatric problems (P1 and P2), yet they have been prescribed medications for psychiatric problems. Please review treatment they may have received. Do you want to recode P1 or P2?                                                   | Yes/No | Pop-up after P11a and b are entered. If "Yes", the cursor moves to P1. If "No", cursor moves to P12.  |
|                   |                                                             |                                                                                                                                                                                                                                                                                                                         |        |                                                                                                               |
| P3 and E15        | E15=0, 00, 000, 0000, or 0000 and P3=1                      | You recorded that the patient receives a pension for a psychiatric problem (P3). Unless they did not receive any cash this month, this income is generally recorded in the employment question about pension money received (E15). Go back and change E15 in the Employment section.                                    | OK     | Pop-up after P3 is entered. Cursor doesn’t move.                                                              |

Example: Select a rule from the table below. Answer the specified items in a way that should trigger a message. The specified message should appear.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 49%" />
<col style="width: 10%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>P4a-P10a and P12</td>
<td>P4a through P10a=0 or 00, and P12&gt;0</td>
<td>You report that the patient has had problems in the past 30 days, but none are recorded in the psychiatric symptom list P4 through P10. Please review P4 through P10, do you want to go back and change the code of any of the symptoms?</td>
<td>Yes/No</td>
<td>Pop-up after P12 is entered. If <strong>"Yes"</strong>, the cursor moves to P4. If <strong>"No"</strong>, cursor moves to P13.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>P4a-P10a and P12</td>
<td>P4a through P10a&gt;0 and P12=0</td>
<td>You report that the patient has had no problems in the past 30 days, but problems are evident from the psychiatric symptom list P4 through P10, please probe about the number of days these symptoms bothered the client and recode P12.</td>
<td>OK</td>
<td>Pop-up after P12 is entered. Cursor does not move.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>P9a and P10a</td>
<td>P9a and/or P10a=1</td>
<td>You report that the client has said they have either suicidal ideation or have attempted suicide in the past 30 days. Probe further for a plan for the suicide and/or dates of the suicide attempt. Notify your supervisor of these responses.</td>
<td>OK</td>
<td>After P10a is entered. <strong>Cursor moves to P10b.</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>P12, P13, and P14</td>
<td>P12&gt;0 and P13 and/or P14=0.</td>
<td>You report that the patient had psychiatric problems in the past 30 days, (P12). Given these problems, we would expect that the patient would be at least slightly bothered or slightly in need of treatment for this recent problem, please recode P13 and/or P14.</td>
<td>OK</td>
<td>After P14 is entered. Cursor moves to P12.</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>P12, P13, and P14</td>
<td>P12=0 or 00 and P13 or P14&gt;0.</td>
<td>You report that the patient had no psychiatric problems in the past 30 days (P12). If they report being troubled or wanting treatment, it is fair to expect that they had some problem days. Go back to P12 and identify the number of days the symptoms have bothered the client.</td>
<td>OK</td>
<td><p>After P14 is entered.</p>
<p>Cursor moves to P12.</p></td>
</tr>
</tbody>
</table>

### Options Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the ASI Data Entry form, click on Options, located on the left side of the menu bar and the drop-down menu will appear. The drop-down menu contains the three options, Default Form Size/Position, Highlight Color, and Speed Tab.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/131.png)

#### Default Form Size/Position

The Default Form Size/Position option is the same as the [Default Form Size/Position](#_Psychological_Test_Results) option located on the main Mental Health Assistant window and will not be listed again.

#### Highlight Color

Example: From the ASI Options, click on the Highlight Colordrop-down list box, the Highlight color list will appear. Colors used to depict highlighted-text can be modified by the user. The default colors are black lettering on a yellow background. To change the foreground or background, use the Highlight ColorForeground or Backgrounddrop-down list boxes to select the desired colors. If the user selects the same color for both foreground and background, the item would not be visible and an error message would appear.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/132.png)

#### Speed Tab

The Speed Tab is provided to make data entry faster. ASI Items that require a simple click (or single keystroke) will move to the next item without the user pressing the Tab or Enter keys. This is particularly helpful on the Social and Psychiatric sections of the ASI.

Example: From the ASI Data Entry form, click on Options and, from the drop-down menu click on Speed Tab. The “Speed Tab” is toggled, (i.e., checked if unchecked, or unchecked if checked).

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/133.png)

### Help Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Opening the Help File

Example: From the ASI Data Entry form, click on the Help menu, then click on Clinical Use of ASI. The Help file designed for the clinician is opened. The information displayed is from the University of Pennsylvania/Veterans Administration Center for Studies of Addiction (1977).

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/134.png)

#### Using the Help Index

The Help Index contains information concerning the operation of the Mental Health programs.

Example: From the ASI Data Entry form, click on the Help menu. From the Help menu drop-down list box, click on the Help Index option, which displays the Help Topics. Below the Help Topics: ASI.hlx window the Index and Find tabs are displayed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/135.png)

### About Mental Health Assistant

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the ASI Data Entry form, click on the Help menu and the [About Form](#selecting-about-option) is displayed. To close the window, click on the OK button, or click on the ‘X’ located on the upper right corner of the About Mental Health Assistant title bar, or press CTL+O from the keyboard.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/136.png)  
Close an ASI Data Entry form

You can exit the ASI Data Entry form by doing one of the following:

1)  Press the ESC key
2)  Press the Alt-F4 key combination
3)  Click on the File\|Exit Menu
4)  Click on the “Finish” button (located at the end of the Psychiatric section)

When one of these methods is used to exit the form, an Addition Severity Index Termination window will appear. Here are the options presented in that window:

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/137.png)

1\) Cancel (Return to ASI, Do not exit) or press ALT+C.Note: The user is returned to the ASI Data Entry form acknowledging that more work is needed on the ASI.

2\) Exit immediately (Save nothing) or press ALT+E.Note: The user may exit the ASI Data Entry form without saving any data. This options returns the user back to the ASI window.

3\) Finish later (Save but do not sign) or press ALT+F.Note: The ASI is saved to complete at a later time. This options returns the user back to the ASI window.

4\) Save and sign or press ALT+S.Note: This option will verify the items for appropriate responses—see business rules—and ensure that the ASI is complete. Once the ASI is verified and saved, the user can provide an electronic signature.

### New Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the new way to entry an ASI, two new “data views” are provided by the release of MHA. Both Domain Scores and Item Trends functionality present graphical and tabular data across multiple interviews.

- The Domain Scores gives the user the opportunity to see either problem severity ratings or evaluation factor scores (see Alterman, et al., \[1998\] “New scales to assess change in the Addiction Severity Index for the opioid, cocaine, and alcohol dependent”, *Psychology of Addictive Behavior,* 12, 233-246).
- The Item Trends displays responses to selected individual items. These new ASI “data views” assist with treatment planning and treatment outcome monitoring.

### Domain Scores

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Domain Scores is the same display as the [multi-scale graphs](#multi-scale-graphs) Test Results, so additional displays of the Domain Scores are not shown.

Example: Click on the Domain Scores button and the Domain Score results are depicted in graph and text formats.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/138.png)

### Domain Scores

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example:Domain Scores results are depicted in graph and text formats.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/139.png)  
Item Trends

Example:Click on the Item Trends button to display the Item-level data in tabular and graphical form across interviews.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/140.png)

### Item Trends (continued)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: Item Trends in graphical form

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/141.png)

### Graphing a Different Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example:Click on a different row in the table of item data. The new row is highlighted and the data for that item is graphed. In this example, the item was changed from M6 (previous example) to D23 by clicking on the D23 row. D23 data are graphed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/142.png)

### Returning to the ASI Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example:Click on the ASI Reports button. The original view of the ASI window is restored.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/143.png)

## Global Assessment of Functioning (GAF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Global Assessment of Functioning (GAF) component is used in the Veterans Health Administration (VHA) to monitor the current and global overall rating functioning of mental health patients. The rating is based on an integrative evaluation of the patient’s functioning in a variety of domains, including psychiatric symptoms as well as social, family, legal, and vocational adjustment.

The new MHA functionality notifies the user when selected patients have not had a GAF Score within the last 90 days. This notification is accomplished by a command button, which states either GAF Due or GAF not due. If the user selects the “GAF Due” command button, they are presented with a dialog box that asks the user if they want to do a GAF now. If the user selects “YES”, they are taken to the GAF tab automatically.

### GAF Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The GAF tab affords the user an easy way to enter GAF ratings and to see previous ratings, which are graphed to indicate trends. When entering a new rating, the rating is associated with the GAF rating criteria. This new function increases the reliability of ratings and reduces inter-rater variability in the assignment of GAF ratings.

### GAF Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the main Mental Health Assistant window, click on the GAF tab, located on the bottom left side of window. When the GAF tab is activated for the first time, (i.e., after a new patient is selected), the GAF Due command button, located on the right side of the taskbar, is displaying the New GAF rating spin edit control box (defaulted to 1), the Evaluation Date entry box (defaulted to today’s date), and the Save Rating command button is disabled. The GAF Range and Criteria table first row is highlighted.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/144.png)

### GAF Due

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The GAF Duecommand button is located on the upper right side of the Mental Health Assistant main window, regardless of which tab you are on. The GAF Duecommand button is enabled if the patient has not had a GAF in the previous 90 days. Clicking on the GAF Duecommand button when enabled activates the following Mental Health Assistant Information dialog box.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/145.png)

#### Mental Health Assistant Information dialog box

Example: The Mental Health Assistant Information dialog box states, “This patient has not had an outpatient GAF in the past 90 days. Would you like to do a GAF rating now?”

Click on the Nocommand button or press ALT+N on the keyboard to exit the Mental Health Assistant Information dialog box without changing the tabs.

Click on the Yes command button or press ALT+Y on the keyboard to activate the following GAF Due command button and to display the GAF criteria table.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/146.png)

### Previous Rating/GAF Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The previous ratings view includes a tabular and graphical representation of all previous GAF ratings as well as the rating criteria for the specified GAF rating. The GAF Criteria/Previous Ratings command button caption always toggles to the view not currently shown.

Example: Click on the GAF Criteria command button, located on the right side of the (blue) patient identification command button to toggle between the GAF Criteria and the Previous Ratings views.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/147.png)

#### Entering a Rating Using GAF Criteria

Example: Click on any row of the GAF criteria table. The mid-level rating for that criterion range is entered in the New GAF Rating spin edit control box, and the Save Rating button is enabled. In this example, clicking on the 31-40 range criteria inserts a 35 in the New GAF Rating and enables the Save Rating command button.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/148.png)

#### Entering a Rating Using The Spin Edit Control

Change the rating by typing a number between 1-100 in the New GAF rating spin edit control box or by clicking on the up or down arrows. The rating in the New GAF rating spin edit control box will change. Alpha characters or numbers outside the 1-100 range are not accepted. In the Previous Ratings view the GAF criteria for the specified rating is shown. In the GAF Criteria view, the selected row in the criteria table corresponds to the specified rating. The Save Rating command button is enabled.

Example: Changing the rating to 47 changes displays the appropriate criteria in the Previous Ratings view and enables the Save Rating command button.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/149.png)

#### Changing Evaluation Date

Example: From the Evaluation Date entry box, click on the down arrow to select a previous or present date. Clicking on the down arrow produces a calendar. Clicking on a date within the calendar will insert a new date into the date entry box. Note: Future dates and months cannot be selected. To select a previous monthclick on the left arrow located on the top of the calendar. To select the present monthclick on the right arrow located on the top of the calendar month

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/150.png)

#### Save

Example: Click on the Save command button. The New GAF rating displayed in the spin edit control box is saved. The New GAF rating date is displayed in the Evaluation Date entry box, and the session user is the rater. The Previous Ratings is updated. The Save Rating command button is disabled. The GAF Due command button is disabled and the caption is changed to GAF Not Due. A New GAF rating of 47 is saved as shown in this example.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/151.png)

#### Edit Rating

Example: The Edit Rating command button allows a user to change or delete a rating made within the previous 2 days or to mark a pervious rating as Entered in Error. Ratings can ONLY be edited by the user that entered then. The Edit Rating command button is enabled only if the MHA session user entered the selected rating.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/152.png)

#### Edit Rating (continue)

Example:Clicking on the Edit Rating command button when enabled brings up the following Mental Health Assistant Information dialog box if the rating is more than two days old.

The Mental Health Assistant Information dialog box states, “You are about to mark the GAF entered on 03/01/2002 as “entered in Error.” If you make this change, you will not be able to undo it.

Do you want to continue?”

Click on the OK command button to continue.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/153.png)

#### Rating Is Marked As Entered In Error

Example: When the user clicks the OK command button located on the Mental Health Assistant Information dialog box, the rating is marked as Entered in Error. This is indicated in the list of previous ratings by strike out font. The rating is no longer included in the graph of previous ratings.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/154.png)

#### Edit Rating

Example:Clicking on the Edit Rating command button, displays a GAF rating (i.e., one less than two days old). The user is presented with a choice of either changing or deleting the GAF rating and then the Edit GAF dialog window is displayed.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/155.png)

#### Edit Rating (continues)

Example: From the previous example, the Edit Rating command button is selected and the following Edit GAF dialog window is displayed:

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/156.png)

#### Edit Rating (continues)

Example: If the Change Rating radio button is clicked, the spin edit control box is displayed to allow the rating to be changed. The new rating overwrites the previous one when the OK command button is pressed. In this example, the Change Rating radio button is clicked and the rating made on 05/16/2002 has been changed to 53. The OK command button is enabled.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/157.png)

#### Edit Rating (continues)

Example: Clicking the OK command button on the previous Edit GAF dialog window changes the rating to the new value and returns the user to the GAF tab. Compare the rating for 05/16/2002 in the table and graph below with the table and graph in the original Edit Rating example.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/158.png)

#### Delete Rating

Example:Clicking the Delete Rating radio button deletes the rating when the OK command button is pressed. In this example, the Delete Rating radio button is pressed, which enables the OK command button. When the OK command button is clicked, the rating made on 05/16/2002 is deleted.

![](ys-5-01-76-mental-health-assistant-phase-2-user-manual/159.png)

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The list of terms are related to the Mental Health Assistant software application:
|               |                                                                                                                                                                                                                                        |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Terms     | Descriptions                                                                                                                                                                                                                       |
|               |                                                                                                                                                                                                                                        |
| API:      | Application Programmer Interface                                                                                                                                                                                                       |
|               |                                                                                                                                                                                                                                        |
| ASI:      | Addiction Severity Index                                                                                                                                                                                                               |
|               |                                                                                                                                                                                                                                        |
| CLIENT:   | A computer that accesses shared network resources provided by another computer (called a) server.                                                                                                                                      |
|               |                                                                                                                                                                                                                                        |
| CLOSE:    | Closes the window. If there are any changes that have not been saved, you will get a confirmation message asking you if you want to continue without saving; save before exiting; or cancel the close action and return to the window. |
|               |                                                                                                                                                                                                                                        |
| CPRS:     | Computer Patient Record System                                                                                                                                                                                                         |
|               |                                                                                                                                                                                                                                        |
| DBIA:     | Database Integration Agreement                                                                                                                                                                                                         |
|               |                                                                                                                                                                                                                                        |
| desktop:      | The background on your, on which windows, icon, and dialog boxes appear.                                                                                                                                                               |
|               |                                                                                                                                                                                                                                        |
| EDIT:     | Used to edit position information.                                                                                                                                                                                                     |
|               |                                                                                                                                                                                                                                        |
| EDIT BOX  | This is a box where the user can type in free text from the keyboard.                                                                                                                                                                  |
|               |                                                                                                                                                                                                                                        |
| Element Name: | Globally unique descriptive name for the field.                                                                                                                                                                                        |
|               |                                                                                                                                                                                                                                        |
| Enhancement:  | An ‘enhancement’ to an already existing Class I software package is the introduction of new or improved functionality.                                                                                                                 |
|               |                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Terms     | Descriptions                                                                                                                                                                                                                                                                                                                                                                               |
|               |                                                                                                                                                                                                                                                                                                                                                                                                |
| FTP:          | File Transfer Protocol                                                                                                                                                                                                                                                                                                                                                                         |
|               |                                                                                                                                                                                                                                                                                                                                                                                                |
| GAF:      | Global Assessment of Functioning                                                                                                                                                                                                                                                                                                                                                               |
|               |                                                                                                                                                                                                                                                                                                                                                                                                |
| Group:        | In User Manager, an account containing other accounts that are called members. The permissions and rights granted to a group are also provided to its members, which makes groups a convenient way to grant common capabilities to collections of user accounts. For Windows NT, groups are managed with User Manager. For Windows NT Server, groups are managed with User Manager of Domains. |
|               |                                                                                                                                                                                                                                                                                                                                                                                                |
| GUI:      | Graphical User Interface.                                                                                                                                                                                                                                                                                                                                                                      |
|               |                                                                                                                                                                                                                                                                                                                                                                                                |
| HL7:          | Health Level 7                                                                                                                                                                                                                                                                                                                                                                                 |
|               |                                                                                                                                                                                                                                                                                                                                                                                                |
| IMR:          | Information Resources Management                                                                                                                                                                                                                                                                                                                                                               |
|               |                                                                                                                                                                                                                                                                                                                                                                                                |
| Length (LEN): | The maximum number of characters that one occurrence of the data field may occupy.                                                                                                                                                                                                                                                                                                             |
|               |                                                                                                                                                                                                                                                                                                                                                                                                |
| LIST BOX: | Box that shows a list of items. If more items exist than can be seen in the box, a scroll bar appears on the side of the box. Selecting an entry from a list box requires either double clicking the entry or single clicking the entry and pressing the spacebar.                                                                                                                             |
|               |                                                                                                                                                                                                                                                                                                                                                                                                |
| MHP:      | Mental Health Package                                                                                                                                                                                                                                                                                                                                                                          |
|                        |                                                                                                                                                                                                                                                                                                                            |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Terms              | Descriptions                                                                                                                                                                                                                                                                                                           |
|                        |                                                                                                                                                                                                                                                                                                                            |
| OK COMMAND BUTTON: | Adds the new entry after the data has been entered.                                                                                                                                                                                                                                                                        |
|                        |                                                                                                                                                                                                                                                                                                                            |
| OPTION BUTTON:     | A small round button that appears in a dialog box. Within a group of related option buttons, you can select only one button at time.                                                                                                                                                                                       |
| PACKAGE:           | An icon that represents an embedded or linked object. When you choose the package, the application that was used to create the object either plays the object (such as sound file) or opens and displays the object.                                                                                                       |
|                        |                                                                                                                                                                                                                                                                                                                            |
| PASSWORD:          | A unique string of characters that must be entered before a logon or an access is authorized. A password is a security measure used to restrict logons to user accounts and access to computer systems and resources. For Windows NT, a password for a user account can be up to 14 characters long and is case-sensitive. |
|                        |                                                                                                                                                                                                                                                                                                                            |
| PATH:              | Specifies the location of a file within the directory tree. For example, to specify the path of a file named README.WRI located in the WINDOWS directory on drive C, you would type c:\windows\readme.wri.                                                                                                             |
|                        |                                                                                                                                                                                                                                                                                                                            |
| PID:               | Patient Identification                                                                                                                                                                                                                                                                                                     |
<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Terms</strong></td>
<td><strong>Descriptions</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><h4 id="previous">PREVIOUS</h4></td>
<td>Previous enable the user to return to a previously answered question so the answer can be changed.</td>
</tr>
<tr class="even">
<td><h4 id="section-2"></h4></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>PSYCHOLOGIST:</strong></td>
<td>Performs patient care duties in accordance with Clinical Privileges as assigned or granted by the appropriate governing committee in the area of Psychology and Mental Health. This may include individuals, family and group counseling and psychotherapy, assertiveness, and other behavior training, etc.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>RADIO BUTTON:</strong></td>
<td>Radio buttons appear in sets. Each button represents a single choice and normally only one button may be selected at any one time. For example, MALE or FEMALE may be offered as choices through two radio buttons. Click in the button to select it.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p><strong>RIGHT MOUSE BUTTON or</strong></p>
<p><strong>SHIFT F10:</strong></p></td>
<td>You may click the right mouse button or press Shift F10 for a popup box of menu items.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>RPC BROKER:</strong></td>
<td>Remote Producers Call Broker</td>
</tr>
</tbody>
</table>
|                             |                                                                                                                                                                                                                                                                                                                                            |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Terms                   | Descriptions                                                                                                                                                                                                                                                                                                                           |
|                             |                                                                                                                                                                                                                                                                                                                                            |
| RPC:                    | Remote Producers Call, a message-passing facility that allows a distributed application to call services available on various computers in a network. Used during remote administration of computers.                                                                                                                                      |
|                             |                                                                                                                                                                                                                                                                                                                                            |
| Save to File (Save AS): | This is a standard feature of Microsoft applications where the user can type the name of the file to be saved. The user can also define the drive and directory where the file is to be saved. In some cases the file name presented in the edit box is sufficient and the user merely needs to click on the “Ok” button to save the file. |
|                             |                                                                                                                                                                                                                                                                                                                                            |
| SHARE:                  | To make resources, such as directories, printers, and ClipBook pages, available to network users.                                                                                                                                                                                                                                          |
|                             |                                                                                                                                                                                                                                                                                                                                            |
| Status Bar:             | A line of information related to the application running in the window. Usually located at the bottom of a window. Not all windows have a status bar.                                                                                                                                                                                      |
|                             |                                                                                                                                                                                                                                                                                                                                            |
| Task List:              | A window that shows all running applications and enables you to switch between them. You can open Task List by choosing Switch To from the Control menu or by pressing CTRL=ESC.                                                                                                                                                           |
|                      |                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Terms            | Descriptions                                                                                                                                                                                                                                                                                                                                                    |
|                      |                                                                                                                                                                                                                                                                                                                                                                     |
| Tab Key:         | Use the TAB key or the mouse to move between fields. Do not use the RETURN key. The RETURN key is usually reserved for the default command button or action (except in menu fields).                                                                                                                                                                                |
|                      |                                                                                                                                                                                                                                                                                                                                                                     |
| TCP/IP:          | Transmission Communication Protocol/Internet Protocol                                                                                                                                                                                                                                                                                                               |
|                      |                                                                                                                                                                                                                                                                                                                                                                     |
| TEXT BOX:        | Type the desired characters into the edit box. The selected entry will not be effective until you tab off or exit from the text box.                                                                                                                                                                                                                                |
|                      |                                                                                                                                                                                                                                                                                                                                                                     |
| TOOLBAR:         | A series of shortcut buttons providing quick access to commands. Usually located directly below the menu bar. Not all windows have a toolbar.                                                                                                                                                                                                                       |
|                      |                                                                                                                                                                                                                                                                                                                                                                     |
| TRANSPORT LAYER: | The fourth layer of the OSI model. It ensures that messages are delivered error-free, in sequence, and with no losses or duplications. This layer repackages messages for their efficient transmission over the network. At the receiving end, the Transport layer unpacks the message, reassembles the original messages, and sends an acknowledgement of receipt. |
|                      |                                                                                                                                                                                                                                                                                                                                                                     |
| UID:             | Unique Identifier                                                                                                                                                                                                                                                                                                                                                   |
|                  |                                                                                                                                                                                                                                                                           |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Terms        | Descriptions                                                                                                                                                                                                                                                          |
|                  |                                                                                                                                                                                                                                                                           |
| VA:              | Veterans Administration                                                                                                                                                                                                                                                   |
|                  |                                                                                                                                                                                                                                                                           |
| VHA:             | Veterans Health Administration                                                                                                                                                                                                                                            |
|                  |                                                                                                                                                                                                                                                                           |
| VAMC:            | Department of Veterans Affairs Medical Center                                                                                                                                                                                                                             |
|                  |                                                                                                                                                                                                                                                                           |
| VERA:        | Veterans Equitable Resource                                                                                                                                                                                                                                               |
|                  |                                                                                                                                                                                                                                                                           |
| VISN:        | Veterans Integrated Service Network                                                                                                                                                                                                                                       |
|                  |                                                                                                                                                                                                                                                                           |
| V*IST*A: | Veterans Health Information Systems and Technology Architecture                                                                                                                                                                                                           |
|                  |                                                                                                                                                                                                                                                                           |
| WORKSTATION: | In general, a powerful computer having considerable calculating and graphics capability. For Windows NT, computers running the windows NT operating systems are called workstations, as distinguished from computers running Windows NT Server, which are called servers. |

# Appendix A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a list of shortcut keys use by the V*ist*A Mental Health Assistant Graphical User Interface software application:

> **NOTE:** When going from one menu option to a sub-menu, do not release the Alt key.

## Shortcut Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

About Window

> Alt-O OK

> ESC Exit

Append Test Comments Window

> Alt-C Cancel

> Alt-S Save

> ESC Exit

ASI Window

> Alt-C Actions Menu

> Alt-E Edit ASI

> Alt-F File Menu

> Alt-G GAF

> Alt-H Help Menu

> Alt-I Item Trends

> Alt-L Tools Menu

> Alt-N Patient Information

> Alt-T Test Results

> Alt-O Order Tests

> Alt-S Domain Scores

> Alt-W New ASI data entry

> Alt-1 Narrative Report

> Alt-2 Item Report

> ESC Exit

ASI Data Entry Window

Alt-D Drug/Alcohol Use Section

Alt-E Employment/Support Section

Alt-G General Information Section

Alt-H Help

Alt-I Spiritual Comments Section

Alt-L Legal Status Section

Alt-M Medical Status Section

Alt-O Options

Alt-P Psychiatric Status Section

Alt-R Leisure Comments Section

Alt-S Family/Social Relationships Section

Alt-A Family History Section

Alt-F4 Exit

ESC Exit

F1 Help for the highlighted item

Main Menus

> Alt-F File

> E Exit

> Alt-O Options

> D Default Window Size/Position

> H Highlight Color

> S Speed Tab

> Alt-H Help

> S Show Clinical Hints

> C Clinical Use of ASI

> I Help Index

> A About

> ASI Options Window

> Alt-C Cancel

> Alt-O OK

> ESC Exit

> ASI Signature Window

> Alt-C Cancel

> Alt-O OK

> ESC Exit

> ASI Termination Window

> Alt-C Cancel

> Alt-E Exit

> Alt-F Finish later

> Alt-S Save and sign

> ESC Exit

Clerk Entry Window

> Alt-J Jump

> Alt-C Close

> ESC Exit

Edit GAF Rating Window

Alt-C Cancel

Alt-O OK

ESC Exit

Main Window

Main Menus

> Alt-F File

> Alt-S Select New Patient

> Alt-R Reports/Tables

> Alt-P Print

> Alt-C Copy

> Alt-S Save As

> Alt-G Graphs

> Alt-P Print

> Alt-C Copy

> Alt-S Save As

> Alt-C Actions

> (Visible when on Test Results tab)

> Alt-M Multiscale Graphs

> Alt-E Enlarge Report

> Alt-A Append Comments

> (Visible when on Order Tests tab)

> Alt-S Staff Entry

> Alt-K Clerk Entry

> Alt-P Patient Entry

> (Visible when on ASI tab)

> Alt-W New ASI

> Alt-S Domain Scores

> Alt-I Item Trends

> (Visible when on GAF tab)

> Alt-P Previous Ratings

> Alt-S Save Rating

> Alt-E Edit Rating

> (Visible on all tabs)

> Alt-T Change Tab

> Alt-T Test Results

> Alt-O Order Tests

> Alt-A ASI

> Alt-G GAF

> Alt-D Patient Demographics

> Alt-U GAF Due

> Alt-S Tools

> Alt-S Start Tab

> Alt-D Default Form Size/Position

> Alt-H Help

> Alt-S Show Hints

> Alt-T Test Information

> Alt-A About

Pop-Up Menus

> Alt-R Reports/Tables

> Alt-P Print

> Alt-C Copy

> Alt-S Save As

> Alt-G Graphs

> Alt-P Print

> Alt-C Copy

> Alt-S Save As

> Alt-T Test Results

Alt-O Order Tests

Alt-A ASI

Alt-G GAF

(Visible from Test Results tab)

> Alt-M Multiscale Graphs

> Alt-E Enlarge Report

> Alt-A Append Comments

(Visible from Order Tests tab)

> Alt-S Staff Entry

> Alt-K Clerk Entry

> Alt-P Patient Entry

(Visible from ASI tab)

> Alt-W New ASI

> Alt-S Domain Scores

> Alt-I Item Trends

(Visible from GAF tab)

> Alt-P Previous Ratings

> Alt-S Save Rating

> Alt-E Edit Rating

ESC Exit

MCMI2 Window

Alt-O OK

Alt-I Inpatient

Alt-U Outpatient

Alt-1 Less than 1 week

Alt-2 One to 4 weeks

Alt-3 One to 3 months

Alt-4 Three to 12 months

Alt-5 Periodic; 1 to 3 years

Alt-6 Continuous; 1 to 3 years

Alt-7 Periodic; 3 to 7 years

Alt-8 Continuous; 3 to 7 years

Alt-9 More than 7 years

Alt-0 Cannot categorize

ESC Exit

Patient Demographics Window

Alt-O Copy

Alt-P Print

Alt-S Save to File

> Alt-C Close

ESC Exit

Test Entry Window (both Staff and Patient Entry)

Alt-B Backup

Alt-N New Question

> Alt-C Close

ESC Exit

Test Graph Window (also ASI Domain Score Window)

Alt-O Copy Graph

Alt-P Print Graph

Alt-S Save Graph

Alt-Y Copy Table

Alt-E Print Table

Alt-A Save Table

> Alt-C Close

ESC Exit

Test Report Window

Alt-O Copy

Alt-P Print

Alt-S Save to File

> Alt-C Close

ESC Exit

Start Tab Options Window

Alt-C Cancel

Alt-O OK

Alt-1 Test Results

Alt-2 Order Tests

Alt-3 ASI

Alt-4 GAF

ESC Exit

# Appendix B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains descriptions of the many windows commands and features used in MHA GUI software application:

## Windows Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cancel

Cancels the latest entry (up until the OK or SAVE button is clicked).

Check Box

Toggles between a YES/NO and ON/OFF setting. Usually a square box containing a check mark or *x*. Clicking the box or pressing the spacebar toggles the check box setting.

Close

Closes the window. If there are any changes that have not been saved, you will get a confirmation message asking you if you want to continue without saving; save before exiting; or cancel the close action and return to the window.

Command Button

The Command button initiates an action. It is a rectangular box with a label that specifies what the button does. Command buttons that end with three dots indicate that a subsidiary screen may be evoked by selecting the command.

Date Field

Identified by “\_\_/\_\_/\_\_” or a date “mm/dd/yy”. Will usually have an associated popup calendar. Double clicking with the mouse inside the date edit box, or tabbing to the edit box and then pressing the F2 key, displays the calendar. Clicking on the desired date, or using the arrow keys to move to a date and then pressing the spacebar, selects the date. Each component of the date (month/day/year) must consist of two characters (i.e., 02/02/96). The selected entry will not be effective until you tab off or exit from the date field.

Drop Down List

A list box containing an arrow button on the right side which displays one entry at a time. Choose from a vertical list of choices. Select the entry you want by clicking the list entry. You cannot type in this box, only select an item from the list. Once an entry is selected, it cannot be deleted - only changed. If \<None\> is the last entry, selecting it will clear the list entry. If \<More\> is the last entry, selecting it will display additional entries. The selected entry will not be effective until you tab off or exit from the drop down list.

Edit

Used to edit position information.

Edit Box

This is a box where the user can type in free text from the keyboard.

F2 Key

Where there is an additional action, which may be taken on a field, pressing the F2 key will initiate that action.

Form Buttons

Buttons, which appear on tab pages, apply only to that tab and not the entire form. If there are action buttons on both the tab page and the form, the tab button should normally be clicked first.

Help

Provides help for the area you are currently working in.

List Box

List Box that shows a list of items. If more items exist than can be seen in the box, a scroll bar appears on the side of the box. Selecting an entry from a list box requires either double clicking the entry or single clicking the entry and pressing the spacebar.

Lookup Box

Choose from a vertical list of choices. By typing in a few characters and pressing the ENTER or TAB key, a list of matching entries drops down. Select the entry you want by clicking the list entry. Entering a question mark and then pressing ENTER or TAB, or clicking the down arrow on an empty edit field, gives a complete listing of available entries. If \<More\> is the last entry, selecting it will display additional entries.

OK

Adds the new entry after the data has been entered.

Radio Button

Radio buttons appear in sets. Each button represents a single choice and normally only one button may be selected at any one time. For example, MALE or FEMALE may be offered as choices through two radio buttons. Click in the button to select it.

Right Mouse Button or Shift F10

You may click the right mouse button or press Shift F10 for a popup box of menu items.

Save

Saves all changes made since the last save action. If you attempt to save and all required fields have not yet been completed, you will receive notification that the required fields must be completed before saving.

Save to File (Save AS)

This is a standard feature of Microsoft applications where the user can type the name of the file to be saved. The user can also define the drive and directory where the file is to be saved. In some cases the file name presented in the edit box is sufficient and the user merely needs to click on the “Ok” button to save the file.

Tab Key

Use the TAB key or the mouse to move between fields. Do not use the RETURN key. The RETURN key is usually reserved for the default command button or action (except in menu fields).

#### Text Box

Type the desired characters into the edit box. The selected entry will not be effective until you tab off or exit from the text box.

View Box

This is a box that displays text but does not allow editing (read only).