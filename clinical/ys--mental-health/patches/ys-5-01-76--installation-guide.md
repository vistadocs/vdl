---
title: YS*5.01*76 Mental Health Assistant Phase 2 Installation Guide
doc_type: IG
doc_label: Installation Guide
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
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - test
  - patient
  - array
  - health
  - ytapi
  - mental
  - software
  - return
page_count: 0
word_count: 10427
section_count: 35
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys50176_mha2_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/ys50176_mha2_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

![](ys-5-01-76-mental-health-assistant-phase-2-installation-guide/001.png)

MENTAL HEALTH ASSISTANT

VERSION 2 (MHA 2)

INSTALLATION GUIDE

PATCH YS\*5.01\*76

June 2003

V*ist*A Health System Design & Development

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
  - [Section 508 of The Rehabilitation Act](#section-508-of-the-rehabilitation-act)
    - [VistA Mental Health Assistant Version 2, (MHA 2) 508 Compliance](#vista-mental-health-assistant-version-2-mha-2-508-compliance)
  - [MHA 2 Software Application](#mha-2-software-application)
    - [### MHA 2 Installation Guide Orientation:](#mha-2-installation-guide-orientation)
  - [Software and Documentation Retrieval Information](#software-and-documentation-retrieval-information)
    - [Anonymous Software Directory](#anonymous-software-directory)
    - [MHA 2 Software and Documentation Files Retrieval Format](#mha-2-software-and-documentation-files-retrieval-format)
    - [VistA Mental Health Version 5.01 Home Page:](#vista-mental-health-version-501-home-page)
    - [VistA Documentation Library (VDL):](#vista-documentation-library-vdl)
- [Introduction](#introduction)
  - [Overview](#overview)
    - [VistA Mental Health Assistant Version 2, Software Features](#vista-mental-health-assistant-version-2-software-features)
  - [VistA MHA 2, Functionality](#vista-mha-2-functionality)
    - [Addiction Severity Index (ASI):](#addiction-severity-index-asi)
    - [Global Assessment of Functioning (GAF)](#global-assessment-of-functioning-gaf)
    - [Psychological Tests and Interviews:](#psychological-tests-and-interviews)
  - [Secure Desktop Information](#secure-desktop-information)
    - [Patient Entry Window](#patient-entry-window)
    - [Unauthorized Keystrokes](#unauthorized-keystrokes)
    - [Excessive Use of Unauthorized Keystrokes](#excessive-use-of-unauthorized-keystrokes)
    - [Termination of Mental Health Assistant](#termination-of-mental-health-assistant)
- [# Enhancements and Modifications](#enhancements-and-modifications)
  - [Enhancements:](#enhancements)
  - [Modifications](#modifications)
- [Security Information](#security-information)
  - [Security Management](#security-management)
    - [Security Features:](#security-features)
    - [Remote Systems:](#remote-systems)
    - [Archiving/Purging:](#archivingpurging)
    - [Contingency Planning:](#contingency-planning)
    - [Interfacing:](#interfacing)
    - [Electronic Signatures:](#electronic-signatures)
    - [Menus](#menus)
    - [Security Keys:](#security-keys)
    - [File Security:](#file-security)
    - [References:](#references)
    - [Official Policies:](#official-policies)
- [Pre-Installation Information](#pre-installation-information)
  - [Recommended Users:](#recommended-users)
    - [Information Resources Management (IRM) Staff](#information-resources-management-irm-staff)
    - [Mental Health Clinicians](#mental-health-clinicians)
  - [Test Sites](#test-sites)
  - [Windows Conventions](#windows-conventions)
  - [## ## VistA Operating System](#vista-operating-system)
  - [## VistA Operating System Performance Capacity](#vista-operating-system-performance-capacity)
  - [MHA Central Processing Unit (CPU) Requirement](#mha-central-processing-unit-cpu-requirement)
  - [MHA Software Application Installation Time](#mha-software-application-installation-time)
  - [## ## Users on the System](#users-on-the-system)
  - [Backup Routines](#backup-routines)
  - [## Kernel Installation and Distribution System (KIDS)](#kernel-installation-and-distribution-system-kids)
  - [Namespace](#namespace)
  - [MHA 2 Software Application Requirements](#mha-2-software-application-requirements)
  - [Required Patches](#required-patches)
  - [MHA 2 Menu/Options Changes](#mha-2-menuoptions-changes)
  - [### YS Broker1 \[YS BROKER1\] Option](#ys-broker1-ys-broker1-option)
  - [Database Integration Agreements (DBIAs)](#database-integration-agreements-dbias)
  - [Data Dictionary Changes](#data-dictionary-changes)
    - [MH INSTRUMENT file (#601):](#mh-instrument-file-601)
    - [COPYRIGHT HOLDER file (#601.3):](#copyright-holder-file-6013)
    - [ASI NARRATIVE file (#604.68):](#asi-narrative-file-60468)
  - [Remote Procedures](#remote-procedures)
    - [MHA New YT RPCs](#mha-new-yt-rpcs)
    - [New Registration DG RPCs](#new-registration-dg-rpcs)
  - [Routine Summary](#routine-summary)
- [Installation Instructions](#installation-instructions)
  - [Server:](#server)
  - [MHA Installation Example:](#mha-installation-example)
- [# Post Installation Instructions](#post-installation-instructions)
  - [Client Software:](#client-software)
  - [IRM Staff:](#irm-staff)
  - [VistA MHA 2 Files Retrieval Locations and Formats](#vista-mha-2-files-retrieval-locations-and-formats)
    - [VISTA MHA 2 Files Retrieval Formats](#vista-mha-2-files-retrieval-formats)
  - [Mental Health Assistant Install Windows Illustrations](#mental-health-assistant-install-windows-illustrations)
    - [Installing Mental Health Assistant on your Computer](#installing-mental-health-assistant-on-your-computer)
    - [Setup complete](#setup-complete)

## Section 508 of The Rehabilitation Act

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The Veterans Health Administration (VHA) fully supports Section 508 of The Rehabilitation Act and is committed to equal access for all users. While every effort has been made to ensure Section 508 compliance, we realize that there may be other issues. If you have questions or would like to see a copy of the Compliance Action Plan for future releases, please contact:

<span class="mark">REDACTED</span>

### V*ist*A Mental Health Assistant Version 2, (MHA 2) 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In MHA Version 1, on the Order Tests tab the only way to move a test from the list of available tests to the list of selected tests (or back) without using the mouse was to use options under the Actions option on the main menu. In MHA Version 2, it is now also possible to tab to the select, delete, or delete all buttons; and select, delete, and delete all menu options have been added to the pop-up menu.

## MHA 2 Software Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Information Systems and Architecture (V*ist*A) Mental Health Assistant Version 2 (MHA 2), Installation Guide Patch YS\*5.01\*76, provides detailed instructions and requirements for installing and implementing the Graphical User Interface (GUI) software application.

### ### MHA 2 Installation Guide Orientation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The screen captures examples text is written in support of Section 508 compliance. Commands to utilize options are bolded.

Introduction: This section includes an overview of the major functions, purposes, and how the GUI software application accomplishes the objectives.

Enhancements and Modifications: This section contains software changes exported by MHA 2, Patch YS\*5.01\*76.

Security Information: This section addresses any unique legal requirements and responsibilities pertaining to the Mental Health Assistant Version 2, software application and necessary security measures to protect the integrity of the software and its data.

Pre-installation Information: This section provides information needed prior to installing MHA Version 2, patch YS\*5.01\*76.

Installation Instructions: This section contains instructions and examples of MHA Version 2, patch YS\*5.01\*76 installation process.

Post Installation Instruction: This provides directions for implementing the V*ist*A Mental Health Package enhancements to interact with the MHA Version 2, software application.

## Software and Documentation Retrieval Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** All sites are encouraged to use the File Transfer Protocol (FTP) capability. Use the FTP address “download.vista.med.va.gov” (without the quotes) to connect to the first available FTP server where the files are located.

### Anonymous Software Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

V*ist*A Mental Health Assistant Version 2 Patch YS\*5.01\*76 files, Installation Guide (i.e., YS50176_MHA2_IG.DOC and YS50176_MHA2_IG.PDF), and User Manual (i.e., YS50176_MHA2_UM.DOC and YS50176_MHA2_UM.PDF) are available on the Office of Information Field Offices (OIFOs) ANONYMOUS SOFTWARE directory FTP addresses listed below:

OIFOsFTP ADDRESSDIRECTORY

<span class="mark">REDACTED</span>

<span class="mark">REDACTED</span>

<span class="mark">REDACTED</span>

### MHA 2 Software and Documentation Files Retrieval Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA 2 Patch YS\*5.01\*76 exports the following files:

File NameContentsRetrieval Formats

YS_501_76.KID ASCII

YS50176_Setup_124.exe Mental Health Assistant BINARY

This file is the complete install for the Mental Health

Assistant GUI Version 1.0.2.9, client.

\- YS_MHA.exe MHA2 Executable

\- YS_MHA_SD.exe Secure Desktop Executable

\- YS_MHA_KH.DLL Keyboard Hook DLL used by Secure Desktop

\- YS_MHA.Hlp Online help file

\- YS_MHA.GID Online help configuration file

\- YS50176_MHA2_IG.PDF YS_MHA2 Installation Guide BINARY

\- YS50176_MHA2_IG.DOC YS_MHA2 Installation Guide BINARY

\- YS50176_MHA2_UM.PDF YS_MHA2 User Manual BINARY

\- YS50176_MHA2_UM.DOC YS_MHA2 User Manual BINARY  
MHA 2 Documentation Website Locations

MHA Version 2, Installation Guide (i.e., YS50176_MHA2_IG.PDF & YS50176_MHA2_IG.DOC), and User Manual (i.e., YS50176_MHA2_UM.PDF & YS50176_MHA2_UM.DOC) are available in MS Word Format (DOC) and Portable Document Format (PDF) at the following Website locations:

### VistA Mental Health Version 5.01 Home Page:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

### V*ist*A Documentation Library (VDL):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<http://www.va.gov/vdl/>

Table Of Contents

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary goal is to make the V*ist*A Mental Health Package (MHP) V. 5.01 an effective, more efficient tool for use by mental health clinicians and their patients with the creation of a windows based application for the most commonly used options in the MHP. Currently the MHP is administered through V*ist*A’s roll-and-scroll technology. Interviews are generally recorded on paper and entered later by the clinician or clerk because the roll and scroll technology is not conducive to following the natural flow of conversation. The development of a windows based software application to enter and display the Global Assessment of Functioning (GAF) score, the Addiction Severity Index (ASI), and 60 psychological tests will make the MHP more user-friendly. This will provide a Graphical User Interface (GUI) format for the entry of GAF, ASI assessments, display of reports and results of psychological tests and interviews.

### V*ist*A Mental Health Assistant Version 2, Software Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ASI – Addiction Severity Index:

- Graph numeric results from ASI responses.
- Functionality to display the ASI entry screens in tabbed sections on one screen.
- Create functionality to display ASI test date, type of interview and interviewer and responses to previous interviews.
- Create Item report with narrative responses.
- Create Narrative reports from ASI responses.
- Create Follow-up report from ASI interviews and responses.

#### GAF – Global Assessment of Functioning:

- Present GAF scores in a graphical format.
- Display on-line cross-reference data with rate criteria.
- Provide functionality to notify the user when selected patients have not had a GAF Score within the last 90 days. (GAF Due tab).

#### Psychological Tests and Interviews:

- Graph single scale instruments to reflect trend in patient symptoms.
- Create an order entry screen to select tests and interviews.
- Create an option for entry of tests and interviews by patients.
- Create an option for entry of tests and interviews by staff.
- Graphical representation of multi-scale instruments.
- Create a report of incomplete tests, interviews and batteries by date.
- Create a report to print results of psychological interviews and tests.

## V*ist*A MHA 2, Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Version 2 exports the Graphical User Interface (GUI) to the MHP most frequently used functionality (i.e., Addiction Severity Index (ASI), Global Assessment of Functioning (GAF), and Psychological testing).

### Addiction Severity Index (ASI):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Enhances the ability of staff to enter ASI data into V*ist*A by clinicians, patients, and data-entry clerks.
- Enhances the ability of staff to retrieve reports.
- Simplifies entry of ASI interview responses.
- Presents ASI scores from multiple interviews in sections and in graphical format.
- Provides functionality to assess multiple interviews simultaneously.
- Displays narrative and item reports in a text format.
- Checks the internal consistency of the ASI items.
- Displays graphically item trends and domain scores for ASI.
- ASI tab - lists all previous ASI interviews and makes it easy to view either the item report or narrative report for a selected interview. To help with ASI performance measure compliance, the interval since the last interview is displayed. Two new ASI data view functions (i.e., Domain Scores and Item Trends) are created by the MHA software application. These new data view functions present graphical and tabular data across multiple interviews. The Domain Scores gives the user the opportunity to see either problem severity ratings or evaluation factor scores. The new Item Trends displays responses to selected individual items. These ASI data view options will assist with treatment planning and treatment outcome monitoring. A user-friendly interface for entering interview data is provided. This function enables staff to quickly enter data, to easily jump from one item to another, and to enter free text comments at any time. This should greatly reduce data entry time, whether transcribing interview results from a paper form, or entering them on-line during an interview.

### Global Assessment of Functioning (GAF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- MHA 2 provides text and graphical reports of historical data stored in the V*ist*A Mental Health Package V. 5.01. This enhances the ability of the staff to enter and retrieve GAF ratings.
- Presents GAF scores in a graphical format.
- GAF reminder
- Associates GAF criteria with the rating made.
- Graphs of previous GAF ratings.
- GAF tab - provides the user with an easy way to enter GAF ratings and to see previous ratings, which are graphed to indicate trends. When entering a new rating, the rating is associated with the GAF rating criteria. It is anticipated this association will increase the reliability of ratings and reduce inter-rater variability in the assignment of GAF ratings.

### Psychological Tests and Interviews:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Enhances the ability of both staff and patients to enter psychological test data.
- Creates reports and graphical displays of complex tests by sub category or scales. Allows user to select sets of scores to graph for multi-scale tests.
- Creates psychological test order windows that displays tests that can be ordered based on the provider privileges.
- Allows users to select multiple tests, interviews, and batteries.
- Provides functionality to display a combination of scale scores, tables and graphs for an individual patient on one screen.
- Graph multiple instances of the same tests (i.e., 4 CAGE tests given on 4 days).
- Allows user to copy to the Windows clipboard or to save to a file, text reports, data tables, or graphs.

#### Test Results Tab:

- All previous tests completed by selected patient are listed on the Test Results tab. A text report is shown for the selected test, and graphs of numeric scores are available across all instances of a given test.

#### Order Tests Tab:

- The Order Tests tab allows the user to specify the staff ordering the test and to select from tests that are available to the staff ordering the test. Three data entry modes are available: (1) Staff entry is optimized for the entry of staff rating data (e.g., the AIMS), which requires the user to see the test questions and answers. (2) Clerk entry is optimized for transcribing test data from paper answer sheets. (3) Patient entry is optimized for on-line testing of patients. The patient entry option contains security features to prevent unattended patients from using the PC in unauthorized ways.

#### Patient Demographics

- Displays patient demographics data, which can be printed, copied to the Windows clipboard, or saved to a text file.

## Secure Desktop Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** The Patient Entrywindow is the only test data entry method that activates the Secure Desktop features. Therefore, neither Staff Entry nor Clerk Entry should be used for the on-line testing of patients.

The Secure Desktop is a set of security features intended to prevent unattended patients taking on-line tests from using the PC for other purposes. SecureDesktop commands the Patient Entry window to cover the entire PC desktop. Non-alphanumeric keys are trapped to keep the patient from using the task bar and operating system functions (such as Task Manager).

The following security features cannot be defeated once the Patient Entry window becomes active, so it is essential that all other applications be closed and data saved before Patient Entry begins:

- Excessive non-alphanumeric keystrokes are interpreted as “hacking” efforts and MHA is terminated.
- At the end of the testing session, MHA is terminated.
- On termination of MHA, the Windows NT session is logged off, which means the user has to enter their NT user name and password to log back on to the desktop.

### Patient Entry Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The following Patient Entry window activates the secured desktop features when the Patient Entry is selected. After the Patient Entry selection is made, two Warning dialog boxes are displayed.

![](ys-5-01-76-mental-health-assistant-phase-2-installation-guide/002.png)

#### First Warning Dialog Box

Example: The <u>first</u> Warning Dialog Box states “After this programs ends, it is going to automatically log you off from the Windows NT Network.” Click on the YEScommand button to proceed. The YEScommand button response displays a second Warning dialog box. ClickCancel to return to the Windows NT Network.

![](ys-5-01-76-mental-health-assistant-phase-2-installation-guide/003.png)

#### Second Warning Dialog Box

Example: The <u>second</u> Warning dialog box states, “Use ONLY Alpha-Numeric Keys on the keyboard from this point on.” Click on the OK command button to continue the Patient Entry functions.

![](ys-5-01-76-mental-health-assistant-phase-2-installation-guide/004.png)  
<u>Authorized Keystrokes</u>

Authorized keystrokes are entered in response to the on-screen questions. Authorized keys are A..Z, a..z, 0..9, ENTER and SHIFT key. Keystrokes trigger the next question to be displayed.

### Unauthorized Keystrokes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Unauthorized keystrokes are entered in response to the on-screen questions. Unauthorized keystrokes are all that are not listed above. Keystrokes trigger the default Windows screensaver to activate, hiding what else is on the screen display. Keystrokes have no other significant effect on the psych test. USER MUST NOT BE ABLE TO ACCESS UNAUTHORIZED DATA OR PROGRAMS.

### Excessive Use of Unauthorized Keystrokes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Strike 5-10 unauthorized keystrokes. Windows shuts down all active programs and logs off the current user, forcing a user to log on again.

### Termination of Mental Health Assistant

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete a test window shuts down all active programs and logs off the current user, forcing a user to log onto the system again.

# # Enhancements and Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Version 2, Patch YS\*5.01\*76 is following exporting the following software changes:

## Enhancements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Four new psychological tests, the Millon Behavioral Medicine Diagnostic (MBMD), the Beck Depression Inventory-II (BDI2), the Millon Clinical Multiaxial Inventory-III (MCMI3) and the Brief Symptom Inventory 18 (BSI18) have been added to the MH INSTRUMENT file (#601). All can now be administered using MHA. The results of the MCMI3, the BSI18, and MBMD can be viewed using the multi-scale graph window (the BDI2 is a single scale instrument). Context sensitive descriptions of the new tests were added to the Help file.

2\. Entries to the COPYRIGHT HOLDER file (#601.3) have been made for the new psychological tests MBMD, BDI2, MCMI3, and BSI18.

3\. For the psychological test Minnesota Multiphasic Personality Inventory-2 (MMPI2), several changes have been made in the scales that are scored and displayed. Five new scales are now scored (the PSY-5 Personality Psychopathology Five). The Subtle-Obvious and Non-K Corrected scales are no longer scored or displayed. The user can choose to display all validity scales at once (Expanded Validity) or just the L, F, K scales (Basic Validity). In MHA Version 2 the multi-scale graph option has been revised to display the new scales.

4\. On the main window of Test Results, Order Tests, ASI or GAF tabs, a right mouse click brings up a pop-up menu with options for each of the enabled buttons on the active tab.

5\. A pop-up menu was added to the window used for graphically displaying the results of both multi-scale tests and ASI domain scores. The pop-up menu, which is activated by a right-click, permits the user to copy, print or save either a graph or a table.

6\. If MHA is launched from the CPRS Tools menu, MHA accepts parameters (such as Patient DFN) passed by CPRS. This eliminates the need to select a patient a second time and ensures that the same patient is always selected by both applications if both are open. When CPRS is closed, MHA will be closed automatically.

7\. MHA can be launched from the CPRS Tools menu without having to sign on a second time if the RPC Broker workstation client software is installed on the PC and single sign-on is enabled on V*ist*A.

8\. Upon closing the Staff Entry window, the user is given the option of saving the test results to V*ist*A. Previously, the option of saving results were given only if all the test questions had not been answered. Completed tests were automatically saved. The change gives the user control over whether the data are saved and makes the exit process the same whether the test was completed or not.

9\. To make the patient selection key sequence the same as that used in CPRS, the Select Patient menu caption was changed from “<u>S</u>elect New Patient” to “Select <u>N</u>ew Patient”.

10\. If a patient is deceased, the user is notified of that and asked if they want to proceed before allowing entry of a new GAF rating, psychological test, or ASI. If the user proceeds, the GAF rating date or ASI admission/interview dates cannot be greater than the date of death. Constraining the date of psychological test data for staff and clerk entry will require a modification to the MH INSTRUMENT file (#601).

11\. ASI comment fields were saved to V*ist*A in a way that caused word wrap problems. The comments fields now are formatted correctly.

12\. In MHA Version 1, the ASI data-entry form, when clicking on an up or down arrow in a spin-edit item, the spin-edit item with focus was increased or decreased. Any up or down arrow click would have its impact on the field with focus, even arrows for other items. The current version allows only the up and down arrows associated with that spin-edit item to have any effect.

13\. In MHA Version 1, the executable was named YS50171_MHA.exe to reflect both the associated VistA Patch YS\*5.01\*71 and the Delphi application build number (123). However, this method of naming the executable will require a new name with each release, which will increase the difficulty of installing future releases. In MHA Version 2, the executable is named YS_MHA.exe, which will be used for all future MHA software releases.

## Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. In MHA Version 1, some windows were closed by a button captioned “Close” and others were closed by a button captioned “Return”. All such buttons are now captioned “Close”.

2\. On the Staff Entry window, the button that returns the user to a previously answered question was captioned “Back Up.” Because this caption could be misunderstood as meaning data would be saved to a backup archive, the caption was changed to “Previous.”

3\. By convention, “OK” buttons appear to the left of “Cancel” buttons, but on some MHA windows their positions were reversed. These two buttons now appear in conventional order on all windows.

4\. To make them more readable, the “\>” captions on the buttons on the Order Tests tab were changed to bold font.

5\. The MMP2S is a short form of the MMPI2. In MHA Version 1, scores from the two forms of the test could not be compared on the multi-scale graph window. The user is now given that option.

6\. When printed, graphs did not include the patient name and yellow lines were not visible on monochrome printers. Patient name is now a footer on all printed graphs, and the yellow lines have been made black.

7\. The following instruments in the MH INSTRUMENT (#601) file: 16PF, MMPI, M168, MCMI, CES, CPI, FES, FIRO, GES, MYER, WES, and SII are copyrighted tests that VACO does not have a license to use. When the user selects one of these instruments they receive the message “USER,MARK is NOT AUTHORIZED to order Instrument GES.” Now, when the user selects one of these instruments the message returned is “\[VACO currently does not have a license to use this test\].” This message is only displayed on the list manager version of Mental Health V. 5.01. In the MHA GUI non-copyrighted tests that VACO does not have a license to use are not viewable from Available Lists box.

8.The ASI NARRATIVE file (#604.68) data has been edited to correct problems with the logic and executable code to produce a report for the Addiction Severity Index that reads like a clinician's written report. The entries modified are GENERAL, FULL ITEM REPORT, LITE ITEM REPORT, FOLLOWUP ITEM REPORT, FOLLOWUP NARRATIVE, ASI-MV ITEM REPORT and the ASI-MV NARRATIVE.

9\. During initialization of the main window of the Test Results tab, the appropriate notice did not appear if the user did not have the YSP key and the first test in the list of previous tests was non-exempt.

10\. An error occurred if the Domain Scores button on the main window of the ASI tab was clicked for a patient for whom there were no complete ASI records to display. This problem was corrected by disabling the button if the patient did not have at least one signed ASI with all questions answered (i.e., not a G-12 record).

11\. Short-cut keys were working on the main, staff entry and clerk entry windows even though the Alt key was not pressed. This has now been corrected to work only when the Alt key has been pressed.

12\. Signing an ASI-MV was not possible without first loading the data into the ASI data entry window. Because there are some differences between the ASI-MV and a regular ASI, loading the ASI-MV into the ASI data entry window caused data validation errors when the record was saved to V*ist*A. Signing an ASI-MV is now possible without loading the results into the data entry window.

13\. Incorrect source code was used to determine whether the user was the ASI interviewer, who is the only person who can sign the interview. Consequently, a new ASI could not be signed without first saving it to V*ist*A and then reloading it into the data entry window.

14\. On the main window of the Order Tests tab, if either the list box containing test choices or the list box containing tests that had been selected had focus, context sensitive help was not available for the selected test in the list box. The context ID of the selected test now is set on the list box click event.

15\. In MHA Version 1, ASI comments were not saved for Spiritual Status and Leisure Time Status. In MHA Version 2, these comments are now saved.

16\. Sometimes, when MHA Version 1, is run as a server application, the Help file could not be found. In MHA Version 2, the help file path is now dynamically set.

17\. When using option, Delete unsigned ASI \[YSAS ASI DATA DELETION\] the user received an error %DSM-E-STRLEN, string too long, DSM-I-ATLABEL, TLD+11^YSASSEL:1. This error occurred on a test patient. An initial ASI is administered to a patient once they enter the substance abuse program. A follow-up ASI is then administered every six months the patient is in the program. This error has been corrected by lowering the \$PIECE field position TO from 40 to 20.

18\. When a user selects the multi-graph button for multi-graph tests (i.e., MMPI2) undefined variable error occurs. This error has been corrected.

19\. When a user selects the multi-graph button for multi-graph tests for the SF36 and the score equals 100, they received an “invalid integer” message. On the multiscale window, the table now lists the correct scale scores (i.e., real numbers, not integers). This has been corrected in the MHA GUI source.

20\. The instruction text for patient administered tests in MHA Version 1, is too small and did not contrast well with the grey background. In MHA Version 2, the font size has been increased to 10 points and the background color has been changed to white.

# Security Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section addresses any unique legal requirements and responsibilities pertaining to the Mental Health Assistant Version 2, software application and necessary security measures to protect the integrity of the software and its data.

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no unique legal requirements pertaining to Mental Health Assistant software application with the exception that some of the psychological tests are copyrighted. Copyrighted tests are used by permission of the copyright holders. Use of these tests must be consistent with contracts between VHA and copyright holders.

### Security Features:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Secure Desktop

Secure Desktop is a set of security features intended to prevent unattended patients taking on-line tests from using the Personal Computer (PC) for other purposes. The Secure Desktop features construct the Patient Entry window to cover the entire PC desktop. Non-alphanumeric keys are trapped to keep the patient from using the task bar and operating system functions (such as Task Manager). The Patient Entry function is the only test data entry method that activates the Secure Desktop features. Therefore, neither Staff Entry nor Clerk Entry should be used for the on-line testing of patients. The Secure Desktop security features cannot be defeated once the Patient Entry window becomes active. Excessive non-alphanumeric keystrokes are interpreted as “hacking” efforts and MHA is terminated. At the end of the testing session, MHA is terminated. Upon termination the Windows NT session is logged off, which means the user has to enter their NT user name and password to log back on to the desktop.

#### Mail Groups:

No mail groups are required for MHA Version 2 software release.

#### Alerts:

No alerts are required for MHA Version 2.

### Remote Systems:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All GAF scores entered through the Mental Health Assistant GAF tab are dynamically sent to the National Patient Care Database (NPCD) at the Austin Automation Center (AAC).

V*ist*A MHA 2, contains the following Remote Procedures (RPCs):

#### MH YT and YS RPCs

YTAPI ASI FACTORS

YTAPI ASI LISTER

YTAPI ASI PNOTE

YTAPI ASI SAVE DATA

YTAPI ASI SIGNER

YTAPI CLERK RESPONSES

YTAPI GET ASI RESPONSES

YTAPI GET INCOMPLETE

YTAPI LIST INCOMPLETES

YTAPI LISTALL

YTAPI LISTONE3

YTAPI NEW ASI

YTAPI NEW GAF

YTAPI OUTNOTE

YTAPI PREVIEW

YTAPI PRIVLEGE

YTAPI QUEST

YTAPI SAVE INCOMPLETES

YTAPI SAVE TEST COMMENT

YTAPI SAVEIT

YTAPI SCOREIT

YTAPI SHOWALL

YTAPI SHOWIT

YTAPI TEST BATTERY

YTAPI TEST BULLETIN

YTRP INSTRUMENT REPORT

YSRP ASI ITEM

YSRP ASI NARRATIVE

#### Registration DG RPCs

NAME: DGWPT CLINRNG TAG: CLINRNG

ROUTINE: DGWPT RETURN VALUE TYPE: ARRAY

DESCRIPTION: Returns a list of selectable options from which a user

can choose a date range for appointments.

NAME: DGWPT DFLTSRC TAG: DFLTSRC

ROUTINE: DGWPT RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: Return user’s default patient list source.

NAME: DGWPT DIEDON TAG: DIEDON

ROUTINE: DGWPT RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: Returns date of death if patient has expired. Otherwise

returns 0.

NAME: DGWPT SAVDFLT TAG: SAVDFLT

ROUTINE: DGWPT RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: Saves user's preference for default list source.

NAME: DGWPT SELCHK TAG: SELCHK

ROUTINE: DGWPT RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: Returns a 1 if the patient record is flagged as sensitive,

otherwise returns 0.

NAME: DGWPT SELECT TAG: SELECT

ROUTINE: DGWPT RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: RPC to return key information on a patient as follows:

1 2 3 4 5 6 7 8 9 10 11 12 13 14

NAME^SEX^DOB^SSN^LOCIEN^LOCNM^RMBD^CWAD^SENSITIVE^ADMITTED^CONV^SC^SC%^ICN

NAME: DGWPT TOP TAG: TOP

ROUTINE: DGWPT RETURN VALUE TYPE: ARRAY

DESCRIPTION: Returns the last selected patient by the defined user.

NAME: DGWPT1 PRCARE TAG: PRCARE

ROUTINE: DGWPT1 RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: Return primary care information for a patient in the format:

VAL=Primary Care Team^Primary Care Provider^Attending

NAME: DGWPT BYWARD TAG: BYWARD

ROUTINE: DGWPT RETURN VALUE TYPE: ARRAY

DESCRIPTION: Returns a list of patients currently residing on a specified

ward location.

### Archiving/Purging:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA 2 software does not include archiving and/or purging capabilities.

### Contingency Planning:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each facility using the MHA software application must develop a local contingency plan to be used in the event of application problems in a live environment. The facility contingency plan must identify procedures used for maintaining the functionality provided by the software in the event of a system outage.

### Interfacing:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The non-menu option, YS BROKER1 \[YS BROKER1\] contains the context necessary to interface MHA Version 2, software application to the V*ist*A database.

### Electronic Signatures:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Version 2, Addiction Severity Index (ASI) software component utilizes the electronic signature functionality.

### Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA 2 software does not contain any menu options of particular interest to Information Security Officers (ISOs).

### Security Keys:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA 2, software application did not release any new security keys. However, the YSP security key is required to control access to the results of “non-exempt” tests. Holders of the YSP security key are controlled (i.e., given out by the Chief of Psychology or a senior psychologist) at a facility that does not have a Chief of Psychology. The Chief of Psychology or senior psychologist also determines which tests are “exempt” (i.e., the results can be seen by anyone), and which are “non-exempt” (i.e., require the YSP key to see the results).

### File Security:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no file security associated with the release of MHA Version 2 software application.

### References:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel V. 8.0 Systems Manual

### Official Policies:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no official policy unique to the MHA Version 2 software application regarding the modification of the software and distribution of the product.

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following information contains recommendations and requirements that should be acknowledged prior to installing V*ist*A Mental Health Assistant Version 2 Patch YS\*5.01\*76:

## Recommended Users:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Information Resources Management (IRM) Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM staff is recommended for installing and supporting MHA 2, Patch YS\*5.01\*76 requirements.

### Mental Health Clinicians

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that Mental Health clinicians enter the MH patient demographics data and define the MH interviews parameters.

## Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA 2 Patch YS\*5.01\*76 has been tested at the following sites:

|                                    |                       |
|------------------------------------|-----------------------|
| Test Sites                     | Hardware Platform |
| <span class="mark">REDACTED</span> | DEC Alpha VMS/DSM     |
|                                    |                       |
| <span class="mark">REDACTED</span> | Wintel NT/Cache       |
|                                    |                       |
| <span class="mark">REDACTED</span> | DEC Alpha VMS/DSM     |
|                                    |                       |
| <span class="mark">REDACTED</span> | DEC Alpha VMS/DSM     |
|                                    |                       |
| <span class="mark">REDACTED</span> | DEC Alpha VMS/DSM     |
|                                    |                       |
| <span class="mark">REDACTED</span> | DEC Alpha VMS/DSM     |

## Windows Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA 2 software application uses a Graphical User Interface (GUI) for the startup, setup, and assignment functions.

## ## ## V*ist*A Operating System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health V. 5.01 Package currently runs on the standard hardware platforms used by the Department of Veterans Affairs Health Care System facilities. These hardware platforms consist of standard or upgraded Alpha AXP clusters, and run either VMS or NT and the Open M product. All current 486 sites are being converted to Alpha 1000A AXP Cluster, NT and Open M platforms.

## ## V*ist*A Operating System Performance Capacity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no significant changes in the performance capacity of the V*ist*A operating system once the Mental Health Assistant Version 2 Patch YS\*5.01\*76 is installed. The software application should not create any appreciable global growth or network transmission problems. There are no memory constraints.

## MHA Central Processing Unit (CPU) Requirement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA 2 software application for Windows 2000 or NT Operating System CPU requirement is a minimum of 133 MHz.

## MHA Software Application Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA 2 Patch YS\*5.01\*76 installation time is less than 5 minutes during off peak hours.

## ## ## Users on the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA users may remain on the system. However, installation of Patch YS\*5.01\*76, should be done during off peak hours.

## Backup Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that a backup of the transport global be performed before installing the V*ist*A Mental Health Assistant Version 2, Patch YS\*5.01\*76.

## ## Kernel Installation and Distribution System (KIDS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health Assistant Version 2 Patch YS\*5.01\*76 distribution is using KIDS.

> **NOTE:** For further instructions on using KIDS, please refer to the Kernel Version 8.0 Systems Manual.

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mental Health Assistant Version 2 Patch YS\*5.01\*76 namespace is YS.

## MHA 2 Software Application Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following software MUST be installed prior to installing MHA 2, patch YS\*5.01\*76:

#### Software Applications Versions

Kernel 8.0

VA FileMan 22.0

Mailman 7.1

RPC Broker 1.1

Toolkit 7.3

Mental Health 5.01

## Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches MUST be installed prior to installing MHA 2 Patch YS\*5.01\*76:

#### Software Applications Patches

Mental Health V. 5.01 YS\*5.01\*38

YS\*5.01\*53

YS\*5.01\*54

YS\*5.01\*67

YS\*5.01\*71

## MHA 2 Menu/Options Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ### YS Broker1 \[YS BROKER1\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The non-menu option, YS BROKER1 \[YS BROKER1\] contains the context necessary to interface the V*ist*A Mental Health Assistant Version 2 software application to the V*ist*A database.

## Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following DBIAs were approved for the release of V*ist*A MHA software application:

DBIA \#418 - Mental Health is also a subscriber to IA \#418. This agreement is written more specifically than IA \#564 and outlines the fields and cross-references access by the application. IA \#564 gives the access by nodes rather than field names. Requested the additional cross-reference be added to \#418.

DBIA \#564 - Mental Health has subscribed to IA \#564, but we also need to do a Global Read of ^DGPT("AF".

DBIA \#1024 - Health Summary accesses file ^DIC(40.7, to display the Name of the Clinic Stop in one of its components.

DBIA \#1649 - ORQPT DEFAULT PATIENT LISTS: This remote procedure returns the current user's default patient list wards to be used in the Mental Health Assistant GUI.

DBIA \#1676 - ORQPT WARDS: This remote procedure returns a list of wards to be used in the Mental Health Assistant GUI.

DBIA \#3371 - ORWU HASKEY: This remote procedure returns 1 if a user holds a security key, otherwise 0 to be used in the Mental Health Assistant GUI.

## Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files changes were created for the MHA GUI Version II:

### MH INSTRUMENT file (#601):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MH INSTRUMENT file (#601) was edited to add the following four new psychological tests:

- Millon Behavioral Medicine Diagnostic (MBMD)
- Beck Depression Inventory-II (BDI2)
- Millon Clinical Multiaxial Inventory-III (MCMI3)
- Brief Symptom Inventory 18 (BSI18)

MH INSTRUMENT file (#601) message text was changed from “BLOW, JOE is NOT AUTHORIZED to order Instrument GES” to “\[VACO currently does not have a license to use this test\]” because the following instruments stored in this file are copyrighted tests and VA Central Office (VACO) does not have a license to use: 16PF, MMPI, M168, MCMI, CES, CPI, FES, FIRO, GES, MYER, WES, and SII.

> **NOTE:** This message is only displayed on the roll ‘n’ scroll version of Mental Health V. 5.01.

The Minnesota Multiphasic Personality Inventory-2 (MMPI2) psychological test contains several changes in the scales that are scored and displayed. Five new scales are now scored (i.e., PSY-5 Personality Psychopathology Five). The Subtle-Obvious and Non-K Corrected scales are no longer scored or displayed. The user can choose to display all validity scales at once (Expanded Validity) or just the L, F, K scales (Basic Validity).

### COPYRIGHT HOLDER file (#601.3):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file was edited to add three of the four new psychological tests (i.e., MBMD, MCMI3 and BSI18). The new psychological test BDI2 is non-copyrighted and does not need to be added to the COPYRIGHT HOLDER file (#601.3).

### ASI NARRATIVE file (#604.68):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASI NARRATIVE file (#604.68) was modified to correct problems with the logic and executable code that produces the Addiction Severity Index Report that reads like a clinician's written report. The entries modified are GENERAL, FULL ITEM REPORT, LITE ITEM REPORT, FOLLOWUP ITEM REPORT, FOLLOWUP NARRATIVE, ASI-MV ITEM REPORT and the ASI-MV NARRATIVE.

## Remote Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

V*IST*A MHA Patch YS\*5.01\*76, uses the following Remote Procedures (RPCs):

### MHA New YT RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: YTAPI ASI FACTORS TAG: EN

ROUTINE: YSASFS RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: Input IEN of file 604, Addiction Severity Index. Returns the 5

factor scores for an ASI in the following format:

YSDATA(1)=\[DATA\]

YSDATA(2)=ALCOHOL^FACTOR SCORE^T SCORE

YSDATA(6)=LEGAL^FACTOR SCORE^T SCORE

INPUT PARAMETER: IEN REQUIRED: YES

DESCRIPTION: An IEN for file 604 "Addiction Severity Index".

NAME: YTAPI ASI LISTER TAG: LISTASI

ROUTINE: YTAPI8 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: This API lists all ASI administrations for a specified patient.

Input required: DFN (ien of file 2)

Output is in the following format:

YSDATA(1)=\[DATA\]

YSDATA(2)= IEN^DATE OF INTERVIEW^CLASS^SPECIAL^ESIGNED

YSDATA(X)= IEN^DATE OF INTERVIEW^CLASS^SPECIAL^ESIGNED

0 RETURNED IF NO ADMINS

NAME: YTAPI ASI PNOTE TAG: ASIPN

ROUTINE: YTAPI9 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: This API creates a Pnote in TIU based on the ASI report.

Input required: IEN of file 604, Addiction Severity Index.

Output is only to show success or failure of the operation.

YSDATA(1)=\[DATA\]/\[ERROR\]

YSDATA(2)=OK Progress Note created/No Pnote entered

NAME: YTAPI ASI SAVE DATA TAG: SAVASI

ROUTINE: YTAPI9 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: This API saves data to the file 604, Addiction Severity Index.

Required input: YSIEN ,ien of the file 604 entry

YS(1)=file 604 field number^value to save

YS(x)=file 604 field number^value to save

Output: only to indicate success vs error

YSDATA(1)=\[DATA\]

YSDATA(2)=OK ASI SAVE YSIEN

NAME: YTAPI ASI SIGNER TAG: SIGN

ROUTINE: YTAPI8 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: Allows interviewer to sign ASI, transcriber to "sign off" and send

a bulletin.

Input Required:

CODE: electronic signature code

IEN: ien of ASI in file 604

Output: reports on status of the operation only

YSDATA(1)=\[DATA\]

YSDATA(2)=1^ASI SIGNED

NAME: YTAPI CLERK RESPONSES TAG: CLERK

ROUTINE: YTAPI9 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: This API returns the possible answer alternatives for each

question in a test or interview from file 601, Psychological Testing

Input Required: Code , the test/interview code ie MMPI2

Output: YSDATA(1)=\[DATA\]

> YSDATA(x)=Question number^A^string with approriate answers (i.e., TFX)

NAME: YTAPI GET ASI RESPONSES TAG: GETASI

ROUTINE: YTAPI8 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: This API returns the ASI responses for a specified ASI

administration.

Input required: DFN ; ien of file 2 Patient

IEN; ien of file 604 Addiction Severity Index

Output: YSDATA(1)=\[DATA\]

YSDATA(x)= Field \#^Question name^is it Required^Answer

NAME: YTAPI GET INCOMPLETE TAG: GETINC

ROUTINE: YTAPI7 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: API to retrieve partially completed psychological tests.

Input Required: DFN ien of file 2 Patient

YSCODE; code for entry in file 601 Psychological Testing Output:

YSDATA(1)=\[DATA\]

YSDATA(2)=INSTRUMENT^DATE ENTERED^DATE ADMINISTERED CLERICALLY^NEXT ITEM^VALID RESPONSE STRING^CLERK TEST^ORDERED BY^DATE BEGUN

YSDATA(3)=responses 1-200

YSDATA(4)=responses 201-400

YSDATA(5)=responses 401-600

NAME: YTAPI LIST INCOMPLETES TAG: LISTINC

ROUTINE: YTAPI7 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: API to return a list of incomplete psychological tests.

Input Required: DFN ; ien of file 2 Patient

Output: YSDATA(1)=\[DATA\]

YSDATA(X)=CODE^DATE OF ADMIN^(not) restartable

NAME: YTAPI LISTALL TAG: LISTALL

ROUTINE: YTAPI RETURN VALUE TYPE: ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: This API returns all psychological test administrations for a

specified patient during a specified time period. No scoring is returned.

ASI s and optionally GAF s are also returned.

Input:

DFN : patient internal identifier

BEGIN: inclusive date in %DT acceptable format (11/11/2011)

to begin search \[optional\]

END: inclusive date in %DT acceptable format (11/11/2011)

to end search \[optional\]

CODE: YS("CODE")="GAF" set to optionally return GAF

administrations

Output:

YSDATA(1)=\[DATA\]

YSDATA(x)= internal administration date^external administration

date^test code

Data is sorted in order of most recent administration to the

oldest administration.

If no administrations are found YSDATA(2) will not be returned.

NAME: YTAPI LISTONE TAG: LISTONE

ROUTINE: YTAPI RETURN VALUE TYPE: ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: This API returns all psychological test administrations for

a specified patient during a specified time period for a specified test

or instrument. If a scale is also specified, scoring for that scale is

returned. User must have adequate privileges to receive this information

(i.e., often the YSP KEY).

Input:

DFN : patient internal identifier

CODE: Test code from file 601 including "ASI" and "GAF" e.g.

"CAGE", "BDI"

BEGIN: inclusive date in %DT acceptable format (11/11/2011) to begin

search \[optional\]

END: inclusive date in %DT acceptable format (11/11/2011) to end

search \[optional\]

LIMIT: constrains to the last N administrations \[optional\]

Scale: scale number from file 601 or 1-7 on ASI \[optional\]

Output:

YSDATA(1)=\[DATA\]

YSDATA(x)= internal administration date ^ external administration

date^test code \[^scale name^raw score^transformed score\]

Data is sorted in order of most recent administration to the oldest administration.

If no administrations are found Array(2) will not be returned.

If patient has no psych testing at all an error will be returned.

NAME: YTAPI NEW ASI TAG: ADDER

ROUTINE: YTAPI8 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: This remote procedure allows new entries to be added to the

ADDICTION SEVERITY INDEX file (#604).

Input required: none

Output:

YSDATA(1)=\[DATA\]

YSDATA(2)= IEN created in file 604

NAME: YTAPI NEW GAF TAG: ENT

ROUTINE: YSGAFAP1 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: Allows entry of a new GAF rating.

Input Required:

DFN - Patient IEN

GAF - GAF Score (Axis 5)

DATE - Date/Time of Diagnosis

STAFF - Diagnosis By DUZ

Output: only reports success vs. error

YSDATA(1)=\[DATA\] VS. YSDATA(1)=\[ERROR\]

NAME: YTAPI OUTNOTE TAG: OUTNOTE

ROUTINE: YTAPI5 RETURN VALUE TYPE: ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: This API returns text to be entered in a progress note

based on the outcome of a test administration. Input is the output of

SCOREIT or PREVIEW API. Output adds this text to the output YSDATA

Input:

Array(2)= Patient Name^Test Code^Test Title^Internal Admin date^External

Admin Date ^Ordered by

Array(3)=R1^Responses 1-200 undelimited

Array(4)=R2^ Responses 201-400 undelimited (even if less than 200)

Array(5)=R3^ Responses 401-600 undelimited

Array(6)=S1^Scale Name^Raw Score^Transformed Score

Array(7)=S2^ Scale Name^Raw Score^Transformed Score

And onward as needed

Output:

Array(2)= Patient Name^Test Code^Test Title^Internal Admin date^External

Admin Date ^Ordered by

Array(3)=R1^Responses 1-200 undelimited

Array(4)=R2^ Responses 201-400 undelimited (even if less than 200)

Array(5)=R3^ Responses 401-600 undelimited

Array(6)=S1^Scale Name^Raw Score^Transformed Score

Array(7)=S2^ Scale Name^Raw Score^Transformed Score

And onward as needed

Array("ON")= output text

NAME: YTAPI PREVIEW TAG: PREVIEW

ROUTINE: YTAPI4 RETURN VALUE TYPE: ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: This API allows scoring of patient responses to a test or

interview without making changes in the M database. The patient ien,

the test code, and administration date is required along with the

responses. All responses are checked for validity. Scoring is returned

in the output documented in the SCOREIT API.

Input:

DFN: patient internal identifier

CODE: Test code from file 601 or "ASI" e.g. "CAGE", "BDI"

ADATE: inclusive administration date in %DT acceptable format

(11/11/2011)

Staff: DUZ of professional ordering the test

R1: string of patient responses 1-200

R2: string of patient responses 201-400 \[as needed\]

R3: string of patient responses 401-600 \[as needed\]

Output:

Array(2)= Patient Name^Test Code^Test Title^Internal Admin date^External

Admin Date ^Ordered by

Array(3)=R1^Responses 1-200 undelimited

Array(4)=R2^ Responses 201-400 undelimited (even if less than 200)

Array(5)=R3^ Responses 401-600 undelimited

Array(6)=S1^Scale Name^Raw Score^Transformed Score

Array(7)=S2^ Scale Name^Raw Score^Transformed Score

And onward as needed

NAME: YTAPI PRIVLEGE TAG: PRIVL

ROUTINE: YTAPI5 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: Returns user privilege to see psych test results.

Input: YSCODE; code of test or interview to check privileges for Output:

YSDATA(1)=\[DATA\]

YSDATA(2)=1^user privileged for all tests or

YSDATA(2)=1^exempt test" or

YSDATA(2)=1^interview or

YSDATA(2)=1^exempt test or

YSDATA(2)=0^no access

NAME: YTAPI QUEST TAG: QUEST

ROUTINE: YTAPI6 RETURN VALUE TYPE: ARRAY

AVAILABILITY: RESTRICTED

DESCRIPTION: Returns flat array with data about a psychological test.

This API returns the text, bottom, introduction and possible correct

responses for all items in a test in file 601. It will work only for

tests as opposed to interviews or batteries. The ASI is not supported.

Input:

CODE: Test code from file 601 e.g. "CAGE", "BDI"

Output:

Array(1)=\[DATA\] ;indicates successful call

Array(2)=MMPI2 ;SECOND LINE IS TEST Code

Array(x)=first item number^I^introductory text

Array(x)=first item number^T^text of question

Array(x)=first item number^A^allowed responses

Array(x)= first item number^R^response cues

Array(x)=last item number^I^introductory text

Array(x)=last item number^T^text of question

Array(x)=last item number^A^allowed responses

Array(x)=last item number^R^response cues

NAME: YTAPI SAVE INCOMPLETES TAG: SAVEINC

ROUTINE: YTAPI7 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: API to save responses of partially completed psychological

tests.

Input:

DFN ;ien of file 2 Patient

YSCODE: code of test in file 604

YSNEXT: next item number to be answered

YSORDER: DUZ of staff ordering test

R1: array of answers 1-200

R2: array of answers 201-400

R3: array of answers 401-600

Output:

YSDATA(1)=\[DATA\]

YSDATA(2)=saved ok

NAME: YTAPI SAVE TEST COMMENT TAG: ADDCOMM

ROUTINE: YTRPEXT RETURN VALUE TYPE: ARRAY

DESCRIPTION: This API is used to add comments to completed tests

and interviews.

INPUT PARAMETER: YSDATA PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 200 REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION: The YSDATA contains the following information:

YSDATA=DFN^DUZ^DATE/TIME TEST ENTERED^NAME OF

TEST^AUTHOR^TOTAL LINES OF COMMENT

DFN: Pointer to the Patient file

DATE/TIME TEST ENTERED: FileMan date/time format

NAME OF TEST: Test name in the MH INSTRUMENT file (#601)

DUZ and AUTHOR: Pointer to the New Person file \#200

INPUT PARAMETER: YSCOMMT PARAMETER TYPE: LIST

MAXIMUM DATA LENGTH: 200 REQUIRED: YES

SEQUENCE NUMBER: 2

DESCRIPTION:

YSCOMMT array contains comment lines to be filed.

RETURN PARAMETER DESCRIPTION:

RESULT(1)="\[ERROR\]",RESULT(2)=" No test found"

RESULT(1)="\[DATA\]",RESULT(2)="Save ok"

RESULT(1)="\[ERROR\]",RESULT(2)="Comment line not created"

RESULT(1)="\[ERROR\]",RESULT(2)="No comment entered"

NAME: YTAPI SAVEIT TAG: SAVEIT

ROUTINE: YTAPI1 RETURN VALUE TYPE: ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: This API allows saving of patient responses to a test

or interview in the M database. The patient ien, the test code,

and administration date is required along with the responses. All responses

are checked for validity. No scoring is returned but successful addition to

the M database is indicated.

Input:

DFN : patient internal identifier

CODE: Test code from file 601 or "ASI" e.g. "CAGE", "BDI"

ADATE: inclusive administration date in %DT acceptable format (11/11/2011)

Staff: DUZ of professional ordering the test

R1: string of patient responses 1-200

R2: string of patient responses 201-400 \[as needed\]

R3: string of patient responses 401-600 \[as needed\]

Output:

Array(1)=\[DATA\] indicates successful call

NAME: YTAPI SCOREIT TAG: SCOREIT

ROUTINE: YTAPI2 RETURN VALUE TYPE: ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: This API returns all scoring information for a specified

patient given a specified administration date for a specified test or

instrument. User must have adequate privileges to receive this

information (i.e. often the YSP KEY).

Input:

DFN : patient internal identifier

CODE: Test code from file 601 or "ASI" e.g. "CAGE", "BDI"

ADATE: inclusive administration date in %DT acceptable format (11/11/2011)

Output:

Array(2)= Patient Name^Test Code^Test Title^Internal Admin date^External

Admin Date ^Ordered by

Array(3)=R1^Responses 1-200 undelimited

Array(4)=R2^ Responses 201-400 undelimited (even if less than 200)

Array(5)=R3^ Responses 401-600 undelimited

Array(6)=S1^Scale Name^Raw Score^Transformed Score

Array(7)=S2^ Scale Name^Raw Score^Transformed Score

And onward as needed

NAME: YTAPI SHOWALL TAG: SHOWALL

ROUTINE: YTAPI3 RETURN VALUE TYPE: ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: This API returns the text, bottom, introduction and possible

correct responses for all items in a test in file 601. It will work only

for tests as opposed to interviews or batteries. The ASI is not supported.

Input:

CODE: Test code from file 601 e.g. "CAGE", "BDI"

Output:

Array(1)=\[DATA\] ;indicates successful call

Array(2)=MMPI2 ;SECOND LINE IS TEST Code

Array(item number,"I",line number)=introductory text

Array(item number,"T", line number)=text of question

Array(item number,"R",0)=allowed responses

Array(item number,"R",line number)= response cues

NAME: YTAPI SHOWIT TAG: SHOWIT

ROUTINE: YTAPI3 RETURN VALUE TYPE: ARRAY

AVAILABILITY: AGREEMENT

DESCRIPTION: This API returns the text, bottom, introduction and possible

correct responses for a specified test item in file 601. It will work only

for tests as opposed to interviews or batteries. The ASI is not supported.

Input:

CODE: Test code from file 601 e.g. "CAGE", "BDI" ITEM: a positive

whole number between 1 and the highest item number for the

specified test.

Output:

Array(1)=\[DATA\] ;indicates successful call

Array(2)=MMPI2^1 ;SECOND LINE IS TEST Code^ item number

Array(item number,"I",line number)=introductory text

Array(item number,"T", line number)=text of question

Array(item number,"R",0)=allowed responses

Array(item number,"R",line number)= response cues

NAME: YTAPI TEST BATTERY TAG: BATT

ROUTINE: YTAPI9 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: Returns a list of all available test batteries and

the tests within them.

Input: none

Output:

YSDATA(1)=\[DATA\]

YSADAT(x)=battery name^test1^test2^test3^test4

NAME: YTAPI TEST BULLETIN TAG: SNDBUL

ROUTINE: YTAPI9 RETURN VALUE TYPE: ARRAY

AVAILABILITY: SUBSCRIPTION

DESCRIPTION: When a clerk gives a psychological test by order of a

clinician, a VISTA email bulletin is sent to that clinician,

informing him/her of the administration of the test, the date, the

clerk and the patient.

Input: DFN ;ien of file 2 Patient

YSORD ;DUZ of ordering clinician

Output:

only success vs. error is reported.

YSDATA(1)=\[DATA\]

NAME: YTRP INSTRUMENT REPORT TAG: INTRMNT

ROUTINE: YTRPWRP RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: PUBLIC WORD WRAP ON: TRUE

DESCRIPTION: This remote procedure allows staff to print out

psychological tests and interview reports.

INPUT PARAMETER: YSDFN PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30 REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION: YSDFN is a pointer to the Patient file \#2.

INPUT PARAMETER: YSXT PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 60 REQUIRED: YES

SEQUENCE NUMBER: 2

DESCRIPTION: This variable contains "Test Completion Date,Name

of the test", for example 3000721,223.

The Name of the test and Completion Date are field 0.1 and field 1 of the

Psych Instrument Patient file \#601.2.

RETURN PARAMETER DESCRIPTION: RESULT returns the test text report for

a selected patient and a given test completion date.

NAME: YSRP ASI ITEM TAG: ASIITM

ROUTINE: YSASRPWP RETURN VALUE TYPE: GLOBAL ARRAY

WORD WRAP ON: TRUE

DESCRIPTION: This procedure prints the selected Addiction Severity Index

in a captioned format.

INPUT PARAMETER: YSASDA PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30 REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION: YSASDA is a pointer to the Addiction Severity Index

file (#604).

RETURN PARAMETER DESCRIPTION: RESULT contains the item report for

the selected ASI.

NAME: YSRP ASI NARRATIVE TAG: ASINAR

ROUTINE: YSASRPWP RETURN VALUE TYPE: GLOBAL ARRAY

AVAILABILITY: PUBLIC WORD WRAP ON: TRUE

DESCRIPTION: This procedure prints the selected ASI in narrative form.

INPUT PARAMETER: YSASDA PARAMETER TYPE: LITERAL

MAXIMUM DATA LENGTH: 30 REQUIRED: YES

SEQUENCE NUMBER: 1

DESCRIPTION:

YSASDA is a pointer to the Addiction Severity Index file \#604.

RETURN PARAMETER DESCRIPTION: RESULT contains the narrative report for

the selected ASI.

### New Registration DG RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: DGWPT CLINRNG TAG: CLINRNG

ROUTINE: DGWPT RETURN VALUE TYPE: ARRAY

DESCRIPTION: Returns a list of selectable options from which a user

can choose a date range for appointments.

NAME: DGWPT DFLTSRC TAG: DFLTSRC

ROUTINE: DGWPT RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: Return user’s default patient list source.

NAME: DGWPT DIEDON TAG: DIEDON

ROUTINE: DGWPT RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: Returns date of death if patient has expired. Otherwise

returns 0.

NAME: DGWPT SAVDFLT TAG: SAVDFLT

ROUTINE: DGWPT RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: Saves user's preference for default list source.

NAME: DGWPT SELCHK TAG: SELCHK

ROUTINE: DGWPT RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: Returns a 1 if the patient record is flagged as sensitive,

otherwise returns 0.

NAME: DGWPT SELECT TAG: SELECT

ROUTINE: DGWPT RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: RPC to return key information on a patient as follows:

1 2 3 4 5 6 7 8 9 10 11 12 13 14

NAME^SEX^DOB^SSN^LOCIEN^LOCNM^RMBD^CWAD^SENSITIVE^ADMITTED^CONV^SC^SC%^ICN

NAME: DGWPT TOP TAG: TOP

ROUTINE: DGWPT RETURN VALUE TYPE: ARRAY

DESCRIPTION: Returns the last selected patient by the defined user.

NAME: DGWPT1 PRCARE TAG: PRCARE

ROUTINE: DGWPT1 RETURN VALUE TYPE: SINGLE VALUE

DESCRIPTION: Return primary care information for a patient in the format:

VAL=Primary Care Team^Primary Care Provider^Attending

NAME: DGWPT BYWARD TAG: BYWARD

ROUTINE: DGWPT RETURN VALUE TYPE: ARRAY

DESCRIPTION: Returns a list of patients currently residing on a specified

ward location.

## Routine Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The second line of the routine now looks like: \<tab\> 5.01;; MENTAL HEALTH;\*\*\[patch list\]\*\*; Dec 30, 1994

Example: Checksum Values

Routine Name Before Patch After Patch Patch List

YSASFM 4829236 4845118 24,30,32,37,38,

55,76

YSASNAR 11815417 11861142 24,30,37,38,44,

55,67,76

YSASSEL 8843928 8843828 24,30,38,76

YSASPRT 2116236 2161961 24,30,38,76

YSMTI3 7243669 7694272 53,71,76

YTAPI 9597980 9459304 53,71,76

YTAPI1 3829862 3787747 53,71,76

YTAR 17157520 17228546 37,54,76

YTAR1 6302994 6356397 37,76

YTBI 10263261 13766056 76

YTBSI18 N/A 2756187 76

YTCLERK 10603997 10744720 19,76

YTCLERK1 5889838 5941523 10,19,76

YTMBMD N/A 7302508 76

YTMCMI3 N/A 7153377 76

YTMCMI3A N/A 10735202 76

YTMCMI3R N/A 6136574 76

YTMMPI2B 15991750 17200069 10,31,76

YTRPWRP 3186347 3199257 10,31,76

> **NOTE:** Sites should use CHECK^XTSUMBLD to verify checksums.

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** V*IST*A Mental Health Assistant Patch YS\*5.01\*76, uses the Kernel Installation and Distribution System (KIDS). For further instructions on using KIDS, please refer to the Kernel V. 8.0 Systems Manual.

## Server:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This patch should be installed during ‘OFF PEAK’ hours when few or no users are on the system. Installation of the patch will take less than 5 minutes.

1\. Use the ‘LOAD A DISTRIBUTION’ option on the PackMan menu. The Host File name is YS_501_76.KID. Answer YES to the question:

> “Want to Continue with Load? YES//”

2\. The patch has now been loaded into a Transport global on your system. You now need to use KIDS to install the Transport global. On the KIDS menu, under the ‘Installation’ menu, use the following options:

> Print Transport Global

> Compare Transport Global to Current System

> Verify Checksums in Transport Global

> Backup a Transport Global

3\. Users may remain on the system, but installation should be done at off peak hours.

4\. Installation will take less than five minutes.

5\. From the ‘Installation Menu’ of the KIDS menu, run the option ‘Install Package(s)’ Select the package ‘YS\*5.01\*76’ and proceed with install.

6\. When prompted “Want KIDS to INHIBIT LOGONs during the install//” respond NO.

> When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//” respond NO.

7\. Place the MENTAL HEALTH ASSISTANT VERSION 2 USER MANUAL in a location that can be accessed by MHA users.

8\. Please refer to the POST INSTALLATION INSTRUCTIONS section of the MENTAL HEALTH ASSISTANT VERSION 2 INSTALLATION GUIDE to install the MHA software.

9\. Place the option YS BROKER1 \[YS BROKER1\] on the Mental Health users secondary menu.

## MHA Installation Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Programmer Options Option: KIDS Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select Kernel Installation & Distribution System Option: INSTALLation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

PU Patch Update

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select Installation Option: 1 Load a Distribution

Enter a Host File: USER\$:\[LLIN\]YS_501_76.KID;1

KIDS Distribution saved on Mar 18, 2003@17:36:41

Comment: MENTAL HEALTH ASSISTANT RELEASE

This Distribution contains Transport Globals for the following Package(s):

Build YS\*5.01\*76 has been loaded before, here is when:

YS\*5.01\*76 Install Completed

was loaded on Mar 18, 2003@15:57:42

OK to continue with Load? NO// YES\<RET\>

Distribution OK!

Want to Continue with Load? YES// \<RET\>

Loading Distribution...

YS\*5.01\*76

Use INSTALL NAME: YS\*5.01\*76 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

PU Patch Update

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: YS\*5.01\*76 Loaded from Distribution 3/18/03@17:42:0

4

=\> MENTAL HEALTH ASSISTANT RELEASE ;Created on Mar 18, 2003@17:36:41

This Distribution was loaded on Mar 18, 2003@17:42:04 with header of

MENTAL HEALTH ASSISTANT RELEASE ;Created on Mar 18, 2003@17:36:41

It consisted of the following Install(s):

YS\*5.01\*76

Checking Install for Package YS\*5.01\*76

Install Questions for YS\*5.01\*76

Incoming Files:

601 MH INSTRUMENT (including data)

> **NOTE:** You already have the 'MH INSTRUMENT' File.

I will OVERWRITE your data with mine.

601.3 COPYRIGHT HOLDER (including data)

> **NOTE:** You already have the 'COPYRIGHT HOLDER' File.

I will OVERWRITE your data with mine.

601.6 MH MULTIPLE SCORING (including data)

> **NOTE:** You already have the 'MH MULTIPLE SCORING' File.

I will OVERWRITE your data with mine.

604.68 ASI NARRATIVE (including data)

> **NOTE:** You already have the 'ASI NARRATIVE' File.

I will OVERWRITE your data with mine.

Want KIDS to INHIBIT LOGONs during the install? YES// NO\<RET\>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO\<RET\>

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//\<RET\> VIRTUAL CONNECTION

Install Started for YS\*5.01\*76 :

Mar 18, 2003@17:42:31

Build Distribution Date: Mar 18, 2003

YS\*5.01\*76

─────────────────────────────────────────────────────────────────────────────

Installing Routines:

Mar 18, 2003@17:42:32

Installing Data Dictionaries:

Mar 18, 2003@17:42:32

Installing Data:

Mar 18, 2003@17:42:55

Updating Routine file...

Updating KIDS files...

YS\*5.01\*76 Installed.

Mar 18, 2003@17:42:56

Install Message sent \#8227970

─────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

# # Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the V*ist*A Mental Health Assistant Version 2 Patch YS\*5.01\*76, has been successfully installed the following instructions must be applied for the software application to function as designed:

## Client Software:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This version of the client software can be installed as either a patch to the existing client software or as a new installation.

## IRM Staff:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** USERS installing 1.0.2.9 software on a Window NT or Windows 2000 environment must have Administrator privileges on the PC Workstation platform.

> **NOTE:** In MHA Version 1, the executable was named YS50171_MHA.exe to reflect both the associated VistA Patch YS\*5.01\*71 and the Delphi application build number (123). However, this method of naming the executable will require a new name with each release, which will increase the difficulty of installing future releases. In MHA Version 2, the executable is named YS_MHA.exe, which will be used for all future MHA software releases.

## V*ist*A MHA 2 Files Retrieval Locations and Formats

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Version 2, software files are available on the following OIFOs ANONYMOUS. SOFTWARE directories. All sites are encouraged to use their FTP capability to obtain these files. Use the FTP address “download.vista.med.va.gov” (without the quotes) to connect to the first available FTP server where the files are located.

OIFOsFTP ADDRESSDIRECTORYAlbany ftp.fo-albany.med.va.gov \[ANONYMOUS.SOFTWARE\]

Hines ftp.fo-hines.med.va.gov \[ANONYMOUS.SOFTWARE\]

Salt Lake City ftp.fo-slc.med.va.gov \[ANONYMOUS.SOFTWARE\]

### V*IST*A MHA 2 Files Retrieval Formats

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File NameContentsRetrieval Formats

YS_501_76.KID ASCII

YS50176_Setup_124.exe Mental Health Assistant BINARY

This file is the complete install for the Mental Health

Assistant GUI Version 1.0.2.9 client.

\- YS_MHA.exe MHA2 Executable

\- YS_MHA_SD.exe Secure Desktop Executable

\- YS_MHA_KH.DLL Keyboard Hook DLL used by Secure Desktop

\- YS_MHA.Hlp Online Help file

\- YS_MHA.GID Online Help configuration file

\- YS50176_MHA2_IG.PDF YS_MHA2 Installation Guide BINARY

\- YS50176_MHA2_IG.DOC YS_MHA2 Installation Guide BINARY

\- YS50176_MHA2_UM.PDF YS_MHA2 User Manual BINARY

\- YS50176_MHA2_UM.DOC YS_MHA2 User Manual BINARY

2\. Copy the YS50176_Setup_124.EXE to an empty (temporary or scratch) directory.

3\. Run the YS50176_Setup_124.EXE file (i.e., double click on it). This starts the MHA 2, installation process. (See the Mental Health Assistant Version 2 software Installation process illustrations on the following pages).

## Mental Health Assistant Install Windows Illustrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following illustrates the Mental Health Assistant Install windows. When the default responses are accepted, MHA 2 is installed into the appropriate V*ist*A directory on the user’s workstation.

### Installing Mental Health Assistant on your Computer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: From the Mental Health Assistant Welcome dialog box, click on the Next command button (located at the bottom of the window) to continue with the install. The Choose Destination Location dialog box will appear next stating, “Which drive do you want to install this program into?”

![](ys-5-01-76-mental-health-assistant-phase-2-installation-guide/005.png)  
<u>Choose Destination Location</u>

Example: The Choose Destination Location dialog box text asks “Which directory do you want to install this program into? We strongly recommend that while the drive can be modified, the default directory be used (Drive:\Program Files\Vista\YSMHA).

Which directory do you want to install this program into?

To install to the directory displayed below, click Next.

To install to a different directory, click Browse and select another directory.

![](ys-5-01-76-mental-health-assistant-phase-2-installation-guide/006.png)

### Setup complete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The Setupcomplete dialog box text states that, “The Mental Health Assistant has been properly installed. You may start the software by clicking on the icon on your desktop.”

Click on the Finish command button (located within the dialog box bottom right side) and the MHA software application setup is complete.

![](ys-5-01-76-mental-health-assistant-phase-2-installation-guide/007.png)