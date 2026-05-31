---
title: Mental Health Assistant User Manual (YS*5.01*224)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: null
app_code: YS
app_name: Mental Health
section: CLI
app_status: archive
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01
group_key: YS:YS:5.01
file_numbers: []
security_keys: []
menu_options: 1
description: The Missed Assignments view allows the user to view a list of all patient(s) that have not completed their remote assessment(s).
audience: End users (clinical / administrative, per package)
keywords: []
page_count: 0
word_count: 11427
section_count: 20
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: May 2024
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Mental_Health_Archive/mha_web_um.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Mental_Health_Archive/mha_web_um.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=370
audit_applied: '2026-05-31'
master_source: Mental Health Assistant User Manual (YS*5.01*224)
master_pub_date: May 2024
consolidated_from: 2 versions
prior_versions:
- Mental Health Assistant User Manual (YS*5.01*265)
consolidated_title: mental health assistant user manual
---

Mental Health AssistantUser Manual

![](mental-health-assistant-user-manual-ys-5-01-224/001.png)

December 2020Revised: May 2024Version 3.0

Office of Information and Technology (OIT)

Product Development

Revision History

| Date          | Revision | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Author(s)            |
|---------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|
| May 2024      | 3.0      | YS\*5.01\*224 update MHA to further enhance the integration with MHC and adds new instruments. Updated Sections 1 thru 6. Replaced Section 5.3 with completely new data and associated Figures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Booz Allen Hamilton  |
| August 2023   | 2.2      | YS\*5.01\*221 update MHA Web to further enhance the integration with MHC and updates multiple instruments. Updated Sections 1 & 4.3, Figures 7, 9 & 99. Added new Figures 27 & 102,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Booz Allen Hamilton  |
| June 2023     | 2.1      | YS\*5.01\*208 update MHA Web to further enhance the integration with MHC and adds a new instrument.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Booz Allen Hamilton  |
| January 2023  | 2.0      | YS\*5.01\*204 updates MHA Web application to allow integration with the MHC application, adds new instruments. New sections: 3 and [7](\l). Updated sections: 2, 3, 4, and [5](\l). New figures: 6-9, 12-26, 30, 39-41, 46, 54-62, 79-82, 90-92, 95-102, 104-123, 135, 156-158. New figures: 6-9, 12-26, 30, 39-41, 46, 54-62, 79-82, 90-92, 95-102, 104-123, 135, 156-158.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Liberty IT Solutions |
| October 2022  | 1.10     | YS\*5.01\*202 enhances the MHA Web application with many updates including: MHA Dashboard is a new feature that is integrated into the MHA Web application along with new instruments, updates to graphing and other functionality. Modifying Progress Note filing to consolidate multiple instruments into a single Progress Note for Patient Entry, Adding the ability to print blank instrument/single instrument, Added category to NUDESC(Cognitive), SIP-AD-30(Sleep), SIP-AD-START(Sleep), and SWEMWBS(Quality of Life), Added Instruments EHS-14, PEB-27, WBS, ASRS and DAR-5, Added interpretive text for certain instruments in Special Reports, Update MCMI4 to allow up to 13 skipped questions, Updated favorites functionality to be included in the cog dropdown menu on MHA Web landing page, Special Reports - Added ability to create a single graph based on multiple scales. New sections are: 4.1.2 and 5. New Figures: Figure 28, 31, 34, 36, 42, 44, 51 & 94. | Liberty IT Solutions |
| May 2022      | 1.9      | YS\*5.01\*199 enhances the MHA Web application with many updates including: Multi-Instrument assignments consolidated into a single note in CPRS, Special Reports: Allow CAT/Non-CAT to be displayed simultaneously on Special Reports, Special Reports Stored as User Preferences, Batteries - Default the Battery group to expanded, Deactivate Print button when on Add Comments page, Staff Entry - Hide the options button, Update the Help PDF document, Add CCOW banner and icon, Graphing - Enable Personality instruments, Graphing – Dashed lines display after 10th item graphed, Graphing - Table scale group check box is non-functional, UI - Adjust instrument hover over to exclude some fields.                                                                                                                                                                                                                                                                     | Liberty IT Solutions |
| January 2022  | 1.8      | YS\*5.01\*187 enhances the MHA Web application with many updates including: Add the ability to save and get Instrument Report preferences, add Delete Instrument Administration for users with administrative access, add instrument full name and description, add user interface to configure and view Special Graph Reports, add the ability to configure batteries, Display Assignment Date in the Active Assignments, Update the High Risk/Positive response flags for instrument administrations, and Instrument graph enhancements. Updated sections are: 2.5.1, 2.5.3, 2.6.4, 2.6.5, and 2.6.6. Updated/new figures are: 59, 60, 61, 62, 63, 69, 80, 81, 82, 83, 84, 85, 86, 87, 88, and 89.                                                                                                                                                                                                                                                                                 | Liberty IT Solutions |
| October 2021  | 1.7      | YS\*5.01\*181 enhances the MHA Web application with a number of updates: Update C-SSRS for 0 days to complete, add MoCA instrument Attestation, Instrument Batteries, Associate a Consult in Assignment/Instrument Admin, Add Comments to an Instrument Administration, Set Graphing preferences, Remove long vertical gaps in MHA Core reports, Support Delete an Instrument Admin, Support Delete list of Instruments from Assignment, Updates New/Edit Assignment functionality including Days to Restart, Fix bug for calculating Positive Response/High Risk on instrument tab, 508 Defect Fixes. Updated sections are: 2.3.13, 2.5.1, 2.5.2, and 4.5.4. Updated figures are 5, 10, 11, 12, 63.                                                                                                                                                                                                                                                                                 | Liberty IT Solutions |
| October 2021  | 1.6      | YS\*5.01\*182 MHA Computerized Adaptive Testing. Adds the capability for Computerized Adaptive Testing (CAT) and Computerized Adaptive Diagnosis (CAD) to the web version of MHA. Update to 2.2. New sections are 2.3.1, 2.3.2, 2.3.3, 2.3.4, 2.3.5, 2.3.6, 2.3.7, 2.3.8, 2.3.9, 2.3.10, 2.3.11, 2.3.12, 2.3.13, 2.3.14, 2.3.15, 2.3.16, 2.3.17, 2.3.18, 2.3.19, 2.3.20, 2.3.21, and 2.3.22. New figures are 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, and 61.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Liberty IT Solutions |
| July 2021     | 1.5      | YS\*5.01\*178 MHA Web Staff Entry Update. Store and retrieve last used settings when creating an assignment, store and retrieve Favorite Instrument List, 508 defect fixes. Added screenshots for updates to application, new figures are 7, 8, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, and 34.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Liberty IT Solutions |
| June 2021     | 1.4      | YS\*5.01\*179 MHA Web Staff Entry CCOW Integration. See 1.1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Liberty IT Solutions |
| March 2021    | 1.3      | YS\*5.01\*158. Remove references to "PaSE" and replace with "MHA Web".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Booz Allen Hamilton  |
| February 2021 | 1.2      | Revised/added screenshots for updates to application                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Booz Allen Hamilton  |
| January 2021  | 1.1      | Revised/added screenshots for updates to application                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Booz Allen Hamilton  |
| December 2020 | 1.0      | Initial creation of MHA Web User Manual                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Booz Allen Hamilton  |

Revision HistoryPorvides a history of revisions of this document

Table of Contents

List of Figures

# MHA 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [MHA](#mha)
- [MHA Overview](#mha-overview)
  - [Starting MHA](#starting-mha)
  - [CCOW Information](#ccow-information)
    - [CPRS Connected Context](#cprs-connected-context)
    - [CPRS Disconnected Context](#cprs-disconnected-context)
    - [CPRS Rejoin/Reestablish Context](#cprs-rejoinreestablish-context)
    - [MHA Connected Context](#mha-connected-context)
    - [MHA Unable to Connect to Context](#mha-unable-to-connect-to-context)
    - [Multiple MHA Instances Open](#multiple-mha-instances-open)
  - [Login Options](#login-options)
    - [VA PIV Card](#va-piv-card)
- [MHA Banner](#mha-banner)
  - [Help Link](#help-link)
  - [Preferences](#preferences)
    - [Batteries](#batteries)
    - [Favorites](#favorites)
- [MHA Patient Plan](#mha-patient-plan)
  - [Active Assignments Panel](#active-assignments-panel)
    - [Review Active Assignment(s)](#review-active-assignments)
    - [Print Blank Instruments](#print-blank-instruments)
  - [Creating Assignment(s) for Staff Entry and Patient Entry](#creating-assignments-for-staff-entry-and-patient-entry)
    - [How to Create a Staff Entry/Patient Entry Assignment](#how-to-create-a-staff-entrypatient-entry-assignment)
  - [Creating Assignment(s) for MHC – on a Veterans Personal Device - Remote Administrations](#creating-assignments-for-mhc-on-a-veterans-personal-device-remote-administrations)
    - [How to Create an MHC (Veterans Personal Device) Assignment](#how-to-create-an-mhc-veterans-personal-device-assignment)
  - [Staff Entry – Executing a Staff Entry Assignment](#staff-entry-executing-a-staff-entry-assignment)
    - [Delete](#delete)
    - [Save and Exit](#save-and-exit)
    - [CAT Specific Actions](#cat-specific-actions)
    - [Finishing an Administration](#finishing-an-administration)
    - [Restricted Instrument(s)](#restricted-instruments)
  - [Completed Instruments](#completed-instruments)
    - [Reviewing Completed Instruments (Reports / Graphs)](#reviewing-completed-instruments-reports-graphs)
    - [Reports](#reports)
    - [Graphs](#graphs)
    - [Append Comments](#append-comments)
    - [Delete Assignment](#delete-assignment)
    - [Printing](#printing)
    - [Special Reports](#special-reports)
  - [MHA Server Timeout](#mha-server-timeout)
  - [Special Instrument Notification in Staff Entry](#special-instrument-notification-in-staff-entry)
  - [Logout](#logout)
- [MHA Dashboard](#mha-dashboard)
  - [Accessing Review Assessments](#accessing-review-assessments)
  - [Review Assessment(s) Dashboard View](#review-assessments-dashboard-view)
    - [View Assessment(s) Overview](#view-assessments-overview)
    - [View Site Assessment(s) Dashboard View](#view-site-assessments-dashboard-view)
  - [Missed Assignments View](#missed-assignments-view)
    - [Overview](#overview)
    - [Missed Assignments Columns](#missed-assignments-columns)
    - [Missed Assignments Search](#missed-assignments-search)
    - [Missed Assignments Sorting](#missed-assignments-sorting)
- [MHA Patient Entry](#mha-patient-entry)
  - [Patient Entry Instrument Completion](#patient-entry-instrument-completion)
    - [Login](#login)
    - [Welcome Screen](#welcome-screen)
    - [Completing an Administration](#completing-an-administration)
    - [Navigating Patient Entry](#navigating-patient-entry)
- [Troubleshooting](#troubleshooting)
  - [Error Selecting a Division](#error-selecting-a-division)
  - [Service Errors](#service-errors)
    - [Mental Health Checkup Service is Unavailable](#mental-health-checkup-service-is-unavailable)
    - [Mobile Secure Token Service is Unavailable](#mobile-secure-token-service-is-unavailable)
    - [IAM SSOi Service is Unavailable](#iam-ssoi-service-is-unavailable)
    - [VistA Service is Unavailable](#vista-service-is-unavailable)
- [Acronyms](#acronyms)
The Mental Health Assistant (MHA) application is the management tool for clinicians to create assignments for Veterans (both remote and inside a clinic) to complete, create and complete administrations through a Staff Entry interface, and review completed assessment reports. The MHA application was developed to create an effective and efficient tool for Mental Health (MH) clinicians and primary care clinicians to track assessment completion and administration trending. This provides MH providers and managers tools (i.e., reports, graphs, etc.) to ensure effective MH care for Veterans. MHA supports MH instruments (e.g., psychological tests, structured interviews, and staff rating scales). Pain assessments, nursing assessments, and additional instruments that are not available elsewhere in the Computerized Patient Record System (CPRS)/Veterans Information System and Technology Architecture (VistA) systems. Overall, MHA provides clinicians with a singular point for assessment assignment and report review from VistA data within a compact and user-friendly format. Core MHA has enjoyed widespread usage among MH clinicians over the past several years, and the current revisions of MHA and Mental Health Package (MHP) initiate steps toward re-engineering VistA Mental Health functionality.
The Mental Health Checkup (MHC) Provider Application and MHA have merged to allow providers to create assignments for Veterans to complete outside of the Mental Health Clinic. This merger gives the provider flexibility to monitor the Veteran as needed, instead of only during a Mental Health visit.

# MHA Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA is divided into multiple logical sections. These sections are:

- MHA Banner
- MHA Patient Plan
  - Active Assignments
  - Completed Assignments
- MHA Dashboard
  - Review Assessment(s)
  - Missed Assignments
- Logout

## Starting MHA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA is launched from the CPRS Tools menu [(Figure 1](#_Ref164164961)). To begin, access the CPRS Tools menu and select MHA. The VA Single Sign-On page is displayed [(Figure 2](\l)).

> **NOTE:** Individual site CPRS Tools menu may be set up differently than the image below.

<span id="_Ref164164961" class="anchor"></span>Figure CPRS Tools Menu - MHA

![](mental-health-assistant-user-manual-ys-5-01-224/002.png)

<span id="_Ref110949642" class="anchor"></span>Figure Single Sign-On Page

![](mental-health-assistant-user-manual-ys-5-01-224/003.png)

## CCOW Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinical Context Object Workgroup (CCOW) is the mechanism that allows MHA to follow patient changes that happen in CPRS. If the CCOW icon shows broken or banner (red or yellow) MHA cannot follow the patient change notification from CPRS. There are multiple conditions that can cause this issue.

### CPRS Connected Context

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If context is connected, an icon on the top left of CPRS displays a blue body with a linked chain ([Figure 3](#_Ref164165205)). MHA responds to the patient changes made in CPRS.

<span id="_Ref164165205" class="anchor"></span>Figure CPRS CCOW Connected

![](mental-health-assistant-user-manual-ys-5-01-224/004.png)

### CPRS Disconnected Context

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If context is disconnected, an icon on the top left of CPRS displays multiple bodies with a broken chain ([Figure 4](#_Ref164345024)), MHA will NOT respond to patient changes made in CPRS.

<span id="_Ref164345024" class="anchor"></span>Figure CPRS CCOW Not Connected

![](mental-health-assistant-user-manual-ys-5-01-224/005.png)

### CPRS Rejoin/Reestablish Context

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To reestablish patient context in CPRS, select File-\>Rejoin patient link-\>Use existing context. To create a new context in CPRS, select File-\>Rejoin patient link-\>Set new context [(Figure 5](#_Ref164165344)).

<span id="_Ref164165344" class="anchor"></span>Figure Set Context

![](mental-health-assistant-user-manual-ys-5-01-224/006.png)

### MHA Connected Context

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When launching MHA from CPRS, MHA will attempt to join the context session already established. If it is successful, the banner will not display any warnings (See Figure 6) and the CCOW connected icon (See Figure 6) will be displayed in the right-hand corner.

<span id="_Ref164165413" class="anchor"></span>Figure MHA Landing Page - CCOW Connected

![](mental-health-assistant-user-manual-ys-5-01-224/007.png)

### MHA Unable to Connect to Context

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When launching MHA from CPRS, MHA will attempt to join the context session already established. If it is unsuccessful, but not due to having multiple MHA instances open, the following window will be displayed (with the yellow banner).

<span id="_Toc167187275" class="anchor"></span>Figure MHA Landing Page - CCOW Not Connected

![](mental-health-assistant-user-manual-ys-5-01-224/008.png)

### Multiple MHA Instances Open

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When launching MHA from CPRS, MHA will detect any other currently running instances and provide the user a warning (Figure 8) and then display a red notification on the banner (Figure 9).

<span id="_Ref164165558" class="anchor"></span>Figure MHA Context Already Joined Message

![](mental-health-assistant-user-manual-ys-5-01-224/009.png)

<span id="_Ref164165594" class="anchor"></span>Figure Multiple MHA Instances Running

![](mental-health-assistant-user-manual-ys-5-01-224/010.png)

## Login Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 3 options for signing into the application using the VA Single Sign-On page:

- VA Personal Identity Verification (PIV) card [(Figure 10](#_Ref164165655)).
- Windows Authentication [(Figure 11](#_Ref164166172)).
- VA Network ID ([Figure 11](#_Ref164166172)).

### VA PIV Card

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The most common single sign-on used is the VA PIV card validating user credentials with their VA PIV card Personal Identification Number (PIN).

\*\*\*NOTE\*\*\* The user must have associated the PIV card with the VistA instance being used, otherwise a Division Selection error will be received. \*\*\*

<span id="_Ref164165655" class="anchor"></span>Figure VA PIV Card Login

![](mental-health-assistant-user-manual-ys-5-01-224/011.png)

#### Windows Authentication Network ID

The Windows Authentication sign-on option uses user credentials that were validated on initial login to the Veterans Administration (VA) network to validate their credentials/access to the application. The sign-in method used the least is the VA Network ID option, which is disabled for most users. This option requires a PIV exemption to gain access to the application.

<span id="_Ref164166172" class="anchor"></span>Figure VA Network ID Option

![](mental-health-assistant-user-manual-ys-5-01-224/012.png)

# MHA Banner

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MHA banner displays the Help and Preferences options, the currently selected patient's name and last 4 numbers of their social security number (SSN), and the CCOW status. All functions performed in MHA Patient View apply to the patient displayed in the banner.

<span id="_Ref125440935" class="anchor"></span>Figure Context Change Popup

![](mental-health-assistant-user-manual-ys-5-01-224/013.png)

There is an icon on the right side of the MHA banner that informs the provider of their CCOW connectivity. If the icon is blue with a connected chain link, the CCOW connection is active (Figure 13).

<span id="_Ref164166710" class="anchor"></span>Figure Connected CCOW Icon

![](mental-health-assistant-user-manual-ys-5-01-224/014.png)

If the icon displays 3 different colored figures with a broken chain link, the CCOW connection is inactive ([Figure 14](\l)).

<span id="_Toc167187282" class="anchor"></span>Figure CCOW Not Connected

![](mental-health-assistant-user-manual-ys-5-01-224/015.png)

## Help Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Selecting the Help link within the MHA banner opens the MHA Quick Start Guide as a Portable Document Format (PDF) file. This PDF is used to give the provider an overview of MHA and its many features.

<span id="_Toc167187283" class="anchor"></span>Figure Quick Start Guide

![](mental-health-assistant-user-manual-ys-5-01-224/016.png)

## Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Preferences button ![](mental-health-assistant-user-manual-ys-5-01-224/017.png) is available on the Banner to the left of the patient's name. Clicking the Preferences button accesses a dropdown menu where Batteries and Favorites can be configured.

### Batteries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Batteries can be used to group instruments that are commonly assigned together. Clicking the Preferences button displays a dropdown menu where Batteries can be selected. This opens the Manage Batteries window.

<span id="_Toc167187284" class="anchor"></span>Figure Batteries - Initial Manage Batteries Window

![](mental-health-assistant-user-manual-ys-5-01-224/018.png)

To create a new Battery, select the + symbol. The Battery Name is a required field. If the user does not enter a Battery Name, an error message appears. Until the Battery Name is entered the Battery cannot be created.

<span id="_Toc167187285" class="anchor"></span>Figure 17: Batteries - Manage Batteries with Error Message

![](mental-health-assistant-user-manual-ys-5-01-224/019.png)

Selecting the ![](mental-health-assistant-user-manual-ys-5-01-224/020.png) button brings up the list of all instruments to customize the Battery. Select the ![](mental-health-assistant-user-manual-ys-5-01-224/021.png) button to save the Battery once the desired instruments have been added. A confirmation text is displayed to show the Battery has been created and the new Battery appears under the Batteries field.

<span id="_Toc167187286" class="anchor"></span>Figure 18: Batteries - Battery Creation Confirmation

![](mental-health-assistant-user-manual-ys-5-01-224/022.png)

Once a Battery has been created, the order of the instruments can be modified by selecting an instrument and using drag and drop to move it to the desired position.

The user can also delete batteries from the Manage Batteries window. Selecting the ![](mental-health-assistant-user-manual-ys-5-01-224/023.png) button causes a confirmation message to appear. Selecting Delete removes the selected battery.

<span id="_Toc167187287" class="anchor"></span>Figure 19: Batteries – Delete Battery Confirmation

![](mental-health-assistant-user-manual-ys-5-01-224/024.png)

Once a Battery has been created, it is ready to be used within the Create/Edit Assignment windows. The created Battery appears at the top left of these windows and can be customized using the normal workflow of MHA.

<span id="_Toc167187288" class="anchor"></span>Figure 20: Batteries - Create Assignment Window

![](mental-health-assistant-user-manual-ys-5-01-224/025.png)

### Favorites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Frequently used instruments can be configured from this interface. Favorites will allow pre-selected instruments to be placed in the Favorites category on the Assignment screens. You can have up to eight instruments in the Favorites list.

To add a new Favorite, use the Preferences icon and select Favorites.

<span id="_Toc167187289" class="anchor"></span>Figure 21: Initial Favorites Interface

![](mental-health-assistant-user-manual-ys-5-01-224/026.png)

To add a new Favorite, click the box next to the instrument name. The instrument name will appear in the Favorites Chosen list.

<span id="_Toc167187290" class="anchor"></span>Figure 22: Favorites Interface - Instrument Added

![](mental-health-assistant-user-manual-ys-5-01-224/027.png)

To add a new Favorite, click the box next to the instrument name. The instrument name will appear in the Favorites Chosen list.

<span id="_Toc167187291" class="anchor"></span>Figure 23: Favorites: Multiple Favorites

![](mental-health-assistant-user-manual-ys-5-01-224/028.png)

Drag and drop is used to adjust the order of the instruments in the Favorites Chosen list.

# MHA Patient Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA has two separate functionalities, Patient Plan and Dashboard. The Patient Plan is applicable to the current patient in context while the Dashboard view provides a broader view of patient data and information.

- MHA Banner
- Active Assignments
- Completed Instruments
- Logout

## Active Assignments Panel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Active Assignments table displays assignments created for the Veteran, including Patient Entry (assignments completed by the patient inside of a VA clinic on an iPad or kiosk), Staff Entry (the provider records the answers for the patient) and Mental Health Checkup (MHC) assignments (assignments scheduled for the Veteran to complete remotely). These assignments can be edited, executed, or deleted, based on situational requirements. Reference the Edit an Active Assignment and [Delete an Active Assignment](\l) sections of this document for more detail.

An icon ![](mental-health-assistant-user-manual-ys-5-01-224/029.png) to collapse the Active Assignments field is located at the bottom right. This allows the user to have a better view of the data on the right side of the screen when viewing Reports, Graphs, etc.

<span id="_Toc167187292" class="anchor"></span>Figure 24: Active Assignments Table

![](mental-health-assistant-user-manual-ys-5-01-224/030.png)

### Review Active Assignment(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a provider creates an Assignment, the Active Assignment table is automatically updated with the new information. In-Clinic Assignments (Patient Entry or Staff Entry) can be edited or deleted until they have been started. Once an assignment has been started (Progress \> 0%), it can only be deleted. Remote assignments (MHC) can be edited while displayed on the Active Assignments panel. Staff Entry assignments will also be displayed if they are not completed.

<span id="_Toc167187293" class="anchor"></span>Figure 25: Active Assignments Table

![](mental-health-assistant-user-manual-ys-5-01-224/031.png)

#### Edit an Active Assignment

To edit an active assignment, click the checkbox beside the desired assignment and select the edit icon ![](mental-health-assistant-user-manual-ys-5-01-224/032.png). Staff Entry assignments cannot be edited.

1.  Patient Entry Assignment - The Edit Assignment window appears (Figure 26) allowing the same functions as when creating an assignment with one exception, the Ordered By field cannot be changed. The Save button must be clicked to save any changes. The Cancel button closes the Edit Assignment window with no changes made. Either action returns the user to the MHA landing page.

> \*\*\*NOTE\*\*\* It is important to remember that an Assignment CANNOT be edited once it has started (anything above 0% complete). If an assignment is partially complete, the 'edit' option will not be available to the user. The only options are to complete the assignment or delete it.\*\*\*

<span id="_Ref111711962" class="anchor"></span>Figure 26: Edit Patient Entry/Staff Entry Assignment Window

![](mental-health-assistant-user-manual-ys-5-01-224/033.png)

2.  MHC/Remote Assignment - The Edit Assignment window appears

> (Figure 27) allowing the same functions as when creating an assignment with one exception, the Ordered By field cannot be changed. The Save button must be clicked to save any changes. The Cancel button closes the Edit Assignment window with no changes made. Either action returns the user to the MHA landing page.

> \*\*\*NOTE\*\*\* It is important to remember that an Assignment CANNOT be edited once it has started (anything above 0% complete). If an assignment is partially complete, the 'edit' option will not be available to the user. The only options are to complete the assignment or delete it.\*\*\*

<span id="_Ref142986104" class="anchor"></span>Figure 27: Editing Scheduled Assignment

![](mental-health-assistant-user-manual-ys-5-01-224/034.png)

#### Delete an Active Assignment

To delete an active assignment, click the checkbox beside the desired assignment and select the Delete icon ![](mental-health-assistant-user-manual-ys-5-01-224/035.png). The Delete Assignment (Figure 28) window appears allowing the provider to review and confirm the assignment before deletion. To finish the deletion, the provider must select the Delete button. If the provider does NOT want to delete the assignment, they must select the Cancel button. Either action returns the user to the MHA landing page.

<span id="_Ref111712177" class="anchor"></span>Figure 28: Delete Assignment Window

![](mental-health-assistant-user-manual-ys-5-01-224/036.png)

### Print Blank Instruments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can print out blank instruments by selecting the ![](mental-health-assistant-user-manual-ys-5-01-224/037.png) button at the top of the Active Assignments panel. The user is taken to the Print Blank Instrument selection window where blank instrument(s) can be selected to be printed. Upon selecting the Print button at the bottom right, the user is redirected to the Print Preview screen. The print preview for a blank instrument is shown in Figure 29.

<span id="_Ref112157561" class="anchor"></span>Figure 29: Print Blank Instrument Window

![](mental-health-assistant-user-manual-ys-5-01-224/038.png)

<span id="_Toc167187298" class="anchor"></span>Figure 30: Sample Blank Instrument

![](mental-health-assistant-user-manual-ys-5-01-224/039.png)

## Creating Assignment(s) for Staff Entry and Patient Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA gives providers the ability to create assignments for patients to be completed inside of the Mental Health facility via Staff Entry or Patient Entry; or outside of the clinic on a Veterans Device (See Section [4.3](#creating-assignments-for-mhc-on-a-veterans-personal-device---remote-administrations)).

### How to Create a Staff Entry/Patient Entry Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create an assignment the user must select the Add Assignment icon ![](mental-health-assistant-user-manual-ys-5-01-224/040.png) above the Active Assignments table.

There will be two choices:

- VA Device/Staff Entry – Assignments to be completed inside the VA facility.
- Veterans Device (MHC) – Assignments to be completed on the Veterans Device outside of a VA facility.

<span id="_Ref125446950" class="anchor"></span>Figure 31: Create Assignments Menu

![](mental-health-assistant-user-manual-ys-5-01-224/041.png)

The Create AssignmentVA Device/Staff Entry window opens and displays a list of instruments as well as a section on information about the assignment. This is also the starting point for a staff entered assessment (for more information, see Section [5.1](#accessing-review-assessments)). The user can hover over an instrument to display the instrument's full name and can navigate to the ? to display greater detail on the instrument.

<span id="_Ref112229526" class="anchor"></span>Figure : Create Assignment Window

![](mental-health-assistant-user-manual-ys-5-01-224/042.png)

#### Create Staff Entry/Patient Entry Assignment Window

The Create Assignment Window is broken into three sections:

- Instrument Categories
- Assignment Options
- Action Buttons

#### Instrument Categories

The instruments are sorted into defined categories. If the user is unable to locate the desired instrument for the patient, the user can select the ![](mental-health-assistant-user-manual-ys-5-01-224/043.png) icon next to a category to expand the list of instruments within that category. Inversely, if the user wants to reduce the list of instruments within a category, they need to select the ![](mental-health-assistant-user-manual-ys-5-01-224/044.png) icon.

<span id="_Toc167187301" class="anchor"></span>Figure 33: Expanded Category

![](mental-health-assistant-user-manual-ys-5-01-224/045.png)

#### View All Instruments

If the user does not know which category the instrument(s) they are looking for are associated with, there is a View All Instruments option at the bottom of the screen that allows the user to list all available instruments in alphabetical order. To access the full list of available instruments, the user can use the scroll bar to move down the page to find the desired instrument(s).

<span id="_Toc167187302" class="anchor"></span>Figure 34: View All Instruments

![](mental-health-assistant-user-manual-ys-5-01-224/046.png)

<span id="_Ref112229776" class="anchor"></span>Figure : Staff Entry/Patient Entry Create Assignment Window with All Instruments Showing

![](mental-health-assistant-user-manual-ys-5-01-224/047.png)

#### View Instruments in Categories

If the user wants to return to the categorized view of the available instruments, they can select the View Instrument Categories option and the modal returns to the original display format.

<span id="_Toc167187304" class="anchor"></span>Figure 36: Add Instrument Grouping

![](mental-health-assistant-user-manual-ys-5-01-224/048.png)

<span id="_Ref112229767" class="anchor"></span>Figure 37: Create Assignment Window with Groups Showing

![](mental-health-assistant-user-manual-ys-5-01-224/049.png)

#### Staff Entry/Patient Entry Instrument Chosen Field

Once the instrument(s) are selected, the user can see those instruments in the Instruments Chosen field on the right side of the Create Assignment window.

<span id="_Toc167187306" class="anchor"></span>Figure : Instruments Chosen Field

![](mental-health-assistant-user-manual-ys-5-01-224/050.png)

#### Staff Entry/Patient Entry Instrument Ordering

The user is given the ability to adjust the order of the instruments by using the Up and Down arrows to prioritize the list of instruments in a multi-instrument assessment. There is also a Delete button that allows the user to remove instrument(s) from the list before creating the assignment. The user needs to select the instrument(s) they do NOT want to include in the assessment (instrument(s) is/are highlighted), and then select the Delete button.

<span id="_Toc167187307" class="anchor"></span>Figure 39: Instruments Chosen Field (Tools)

![](mental-health-assistant-user-manual-ys-5-01-224/051.png)

#### Staff Entry/Patient Entry Configure Favorites

MHA provides the functionality to add up to 8 items to a Favorites list.

- To add items to the Favorites list, the user must select the instruments from the Create Assignment window which adds them to the Instruments Chosen box. From the Instruments Chosen box, the user then needs to click the desired instrument (highlight) and click the Add to Favorites button.
- To delete instruments from the Favorites list, the user must select the instruments that already exist in the Favorites group, which adds the selection into the Instruments Chosen box. In the Instruments Chosen box, select (highlight) the instrument and click on the Remove from Favorites button to remove the instruments from the Favorites section.
- The user can also access the Favorites interface via the dropdown menu from the cog icon on the MHA Banner.
- If the user attempts to add more than eight instruments to the Favorites list, an error message will be displayed (Figure 40).

<span id="_Ref111712827" class="anchor"></span>Figure 40: Staff Entry/Patient Entry - Error Message - Maximum Number of Favorites

![](mental-health-assistant-user-manual-ys-5-01-224/052.png)

<span id="_Toc167187309" class="anchor"></span>Figure 41: Staff Entry/Patient Entry - Favorites List – Expanded

![](mental-health-assistant-user-manual-ys-5-01-224/053.png)

<span id="_Ref125446951" class="anchor"></span>Figure 42:Staff Entry/Patient Entry - Favorites List - Collapsed View

![](mental-health-assistant-user-manual-ys-5-01-224/054.png)

#### Staff Entry/Patient Entry - Assignment Options

#### Ordered By (Instruments Ordered By)

The user must select the name of the person ordering the assessment and who will be responsible for signing any related Progress Note. The text search for this field is dynamic, and as soon as the user has entered at least 2 letters into the field, a list of possible matches will be returned in a dropdown field. Highlighting and selecting the name will finish the process of entering the Ordered By name. This is a required field.

\*\*\*NOTE\*\*\* The name is entered Last Name,First Name with no space in between the names. \*\*\*

<span id="_Ref112229753" class="anchor"></span>Figure 43: Ordered By: Field

![](mental-health-assistant-user-manual-ys-5-01-224/055.png)

#### Staff Entry/Patient Entry Interviewer

The user must select the name of the person interviewing the patient for the assessment. The text search for this field is dynamic, and as soon as the user has entered at least 2 letters into the field, a list of possible matches is returned in a dropdown field. Highlighting and selecting the name finishes the process of entering the Interviewer name. This is a required field.

\*\*\*NOTE\*\*\* The name is entered Last Name,First Name with no space in between the names. \*\*\*

<span id="_Toc167187312" class="anchor"></span>Figure 44: Interviewer Field

![](mental-health-assistant-user-manual-ys-5-01-224/056.png)

#### Staff Entry/Patient Entry - Location (Visit Location)

The user must select the name of the location of the assessment. The text search for this field is dynamic, and as soon as the user has entered at least 2 letters into the field, a list of possible matches is returned in a dropdown field. Highlighting and selecting the name finishes the process of entering the Location name. This is a required field.

<span id="_Ref112229759" class="anchor"></span>Figure 45: Location Field

![](mental-health-assistant-user-manual-ys-5-01-224/057.png)

#### Staff Entry/Patient Entry - Date (Date of Administration)

The user has the option to select a Date for the date related to the assessment. The Date can be selected by clicking the field and selecting the appropriate date from the displayed list. This is a required field.

<span id="_Toc167187314" class="anchor"></span>Figure 46: Date Field

![](mental-health-assistant-user-manual-ys-5-01-224/058.png)

#### Staff Entry/Patient Entry - Consult (Link with Consult)

The user has the option to select a consult if there is a consult related to the assessment. The Consult can be selected be clicking the dropdown arrow beside the Consult field and selecting the appropriate consult from the displayed list. This is an optional field and is NOT required.

<span id="_Ref125446952" class="anchor"></span>Figure 47: Staff Entry/Patient Entry - Create Assignment - Consult Field

![](mental-health-assistant-user-manual-ys-5-01-224/059.png)

#### Staff Entry/Patient Entry Action Buttons

The following paragraphs detail the action buttons.

#### Staff Entry/Patient Entry Cancel

If the user does not want to continue with the creation of an assignment, they can select the Cancel button, which closes the Create Assignment window and returns the user to the MHA landing page.

<span id="_Toc167187316" class="anchor"></span>Figure 48: Create Assignment - Action Buttons

![](mental-health-assistant-user-manual-ys-5-01-224/060.png)

#### Patient Entry

When selecting the Patient Entry button, the application creates an Assignment ID that is displayed in a small window on the screen. This number is the PIN that is given to a patient so the patient can complete their assignment. For a more detailed explanation of the process for using the Patient Entry application, reference the MHA Patient Entry section in this document.

<span id="_Toc167187317" class="anchor"></span>Figure 49: Create Assignment - Patient Entry Action Button

![](mental-health-assistant-user-manual-ys-5-01-224/061.png)

<span id="_Toc167187318" class="anchor"></span>Figure 50: Create Assignment - Patient Entry PIN

![](mental-health-assistant-user-manual-ys-5-01-224/062.png)

#### Staff Entry

When selecting the Staff Entry button, the application immediately launches the assessment in Staff Entry mode. This is the mode the clinician uses to complete the patient assessment. Further detailed information regarding this functionality can be found in the Executing a Staff Entry Assignment of Section [4.4](#staff-entry-executing-a-staff-entry-assignment).

\*\*\*NOTE\*\*\* Multi-instrument Staff Entry assessment results will be consolidated into a single Progress Note upon completion. \*\*\*

<span id="_Toc167187319" class="anchor"></span>Figure 51: Create Assignment – Staff Entry Action Button

![](mental-health-assistant-user-manual-ys-5-01-224/063.png)

#### Create CAT Assignment

CAT assignments can only be used with Patient Entry or Staff Entry. The first step to creating a Computerized Adaptive Testing (CAT) assignment for a patient is selecting the desired instrument(s) for that patient. To select an instrument, the user must 'check' the box beside the instrument name. If more than 1 instrument is desired, the user must 'check' the boxes beside all desired instruments.

\*\*\*NOTE\*\*\* The selection of a CAT instrument disables all non-CAT instruments from selection. \*\*\*

<span id="_Ref112229744" class="anchor"></span>Figure 52: Create Assignment – CAT

![](mental-health-assistant-user-manual-ys-5-01-224/064.png)

#### CAT Timeframe

When administering a CAT instrument, the user is provided the opportunity to specify the timeframe related to the responses from the patient. If the user desires the answers to be associated with the patient's health over the past week, then the user can select Past week. There are several options available to the user for selection, but the default is Past 2 weeks.

<span id="_Toc167187321" class="anchor"></span>Figure 53: Create Assessment – CAT Timeframe

![](mental-health-assistant-user-manual-ys-5-01-224/065.png)

#### CAT Language

When administering a CAT instrument, the user is provided the opportunity to specify the preferred language for the patient. Currently, only the English version is available, but Spanish is being investigated for a future release.

<span id="_Toc167187322" class="anchor"></span>Figure 54: Create Assessment – CAT Language

![](mental-health-assistant-user-manual-ys-5-01-224/066.png)

## Creating Assignment(s) for MHC – on a Veterans Personal Device - Remote Administrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The merger of MHA with MHC gives providers the ability to create assignments for Veterans to be completed via a Veterans Device outside of the Mental Health facility. To generate an assignment, all required fields must be completed and then the Schedule button must be selected. The provider can determine how the assignment is communicated to the Veteran (email, text message or both).

### How to Create an MHC (Veterans Personal Device) Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create an assignment, the user must select the Add Assignment icon ![](mental-health-assistant-user-manual-ys-5-01-224/067.png) above the Active Assignments table.

There will be two choices:

- VA Device/Staff Entry – Assignments to be completed inside the VA facility.
- Veterans Device (MHC) – Assignments to be completed on the Veterans Device outside of a VA facility.

<span id="_Ref125446953" class="anchor"></span>Figure 55: Create Assignments Menu

![](mental-health-assistant-user-manual-ys-5-01-224/068.png)

The Create AssignmentVeteran's Device (MHC) window opens and displays a list of instruments available to be sent to a Veteran, as well as a section on information about the assignment. The user can hover over an instrument to display the instrument's full name and can navigate to the ? to display greater detail on the instrument.

<span id="_Toc167187324" class="anchor"></span>Figure 56: MHC Create Assignment Window

![](mental-health-assistant-user-manual-ys-5-01-224/069.png)

#### Create MHC Assignment Window

The Create Assignment Window is broken into three steps:

- Step 1 – Select patient notification method
- Step 2 – Select instrument
- Step 3 – Schedule instrument(s)

#### Step 1: Selection Patient Notification Method

Notifications can be sent to a Veteran two ways, via email or via text message. If the Veteran has an email or phone number that is currently available, they will be displayed with those defaults displayed and boxes already checked.

<span id="_Toc167187325" class="anchor"></span>Figure 57: MHC - Select Patient Notification

![](mental-health-assistant-user-manual-ys-5-01-224/070.png)

#### MHC – Step 2: Select Instrument

The instruments are sorted into pre-defined categories. The instruments can also be displayed alphabetically by clicking the View All Instruments link at the top of the Select Instrument section. Instruments can also be searched for by entering the first few letters of the instrument name. To add an instrument to the schedule, click on the checkbox next to the instrument name.

<span id="_Toc167187326" class="anchor"></span>Figure 58: MHC - Select Instrument

![](mental-health-assistant-user-manual-ys-5-01-224/071.png)

#### Add Favorites

Favorites can be added inside of the Select Instrument section. To add an instrument to a favorite, click the checkbox beside the instrument and click the star beside the instrument name.

<span id="_Toc167187327" class="anchor"></span>Figure 59: Add Favorites in MHC Create Assignment Screen

![](mental-health-assistant-user-manual-ys-5-01-224/072.png)

#### Remove Favorites

Favorites can also be removed inside of the Select Instrument section. To remove an instrument from the Favorites list, click the Trash Can beside the instrument name in the Favorites list.

<span id="_Toc167187328" class="anchor"></span>Figure 60: Remove Favorites in MHC Create Assignment Screen

![](mental-health-assistant-user-manual-ys-5-01-224/073.png)

#### MHC - Schedule Instrument(S) Section

If the user does not know which category the instrument(s) they are looking for is/are associated with, there is a View All Instruments option at the bottom of the screen that allows the user to list all available instruments in alphabetical order. To access the full list of available instruments, the user can use the scroll bar to move down the page to find the desired instrument(s).

<span id="_Toc167187329" class="anchor"></span>Figure : MHC - Schedule Instrument(s) – No Instrument Selected

![](mental-health-assistant-user-manual-ys-5-01-224/074.png)

#### MHC - Schedule Instrument(s) Options

There are multiple decisions that must be made when creating remote assignment. These range from the instrument that is assigned to instructions that can be sent to the Veteran regarding completion of the assignment. The required field (fields marked with an \*) must be filled in to schedule the assignment. Each instrument in the assignment may have different selections for the parameters.

- Instrument – An individual instrument (measure, test, etc.) to be assigned to the Veteran.
- Frequency – How often should the instrument be sent to the Veteran.
- Response Window – How long after the Veteran receives the assignment does it need to be completed. The response window will vary depending upon the Frequency of the instrument.
- How Many – How many iterations of the instrument will be sent to the Veteran.
- Start Date – When does the assignment begin. Can be the current day or a future date up to a year.
- Clinic – The location that the assignment should be associated with. (Defaulted to the Location used in Staff Entry/Patient Entry assignments).
- Instructions – Any specific instructions that the provider wants to send to the Veteran.
- Schedule - To submit and schedule the instruments and create the assignments.

<span id="_Toc167187330" class="anchor"></span>Figure : MHC - Schedule Instrument(s) - Multiple Instruments Selected

![](mental-health-assistant-user-manual-ys-5-01-224/075.png)

#### MHC assessment completion

When a Veteran completes an assessment, an email notification will always be sent to the responsible Provider. If the Veteran assessment responses indicate suicidality, the email subject will state "MH Checkup Patient has indicated suicidality".

When the Veteran sees the completion screen and suicidality is indicated, a message will appear recommending them to contact their provider or the Veteran Crisis Line.

<span id="_Toc167187331" class="anchor"></span>Figure - MHA Patient Facing Application

![](mental-health-assistant-user-manual-ys-5-01-224/076.png)

## Staff Entry – Executing a Staff Entry Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the setup of an assignment has been completed and the user selects the Staff Entry button, the Staff Entry mode of MHA automatically launches and allows the user to begin completing assessment(s). Completing a multi-instrument assignment in Staff Entry creates a single Progress Note in CPRS if Save Note is selected after the administration is completed.

<span id="_Ref125446954" class="anchor"></span>Figure 64: Staff Entry Execution Screen

![](mental-health-assistant-user-manual-ys-5-01-224/077.png)

### Delete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the provider decides they do not want to complete the assessment, they can select the Delete button at the bottom of the Staff Entry page. The provider is returned to the MHA landing page and Staff assignment is not created in the Active Assignments table. In the event there are multiple instruments in the assignment, Staff Entry takes the user to the next instrument in the assignment after selecting Delete. This continues until the user has deleted all instruments in the current assignment (Figure 65).

<span id="_Ref111794668" class="anchor"></span>Figure 65: Staff Entry Action Buttons

![](mental-health-assistant-user-manual-ys-5-01-224/078.png)

### Save and Exit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the provider decides to leave the administration and wants to save the results entered, or save the administration for later completion, they can select the Save and Exit button at the bottom of the page (Figure 65). Staff Entry presents the user with a warning popup outlining the time to finish the administration and provide them a choice to continue or cancel this action (Figure 66). If the provider selects No, they remain in the administration. If they select Yes, the provider is returned to the MHA landing page and a Staff assignment ID is created in the Active Assignments table.

<span id="_Ref111794748" class="anchor"></span>Figure 66: Staff Entry Save and Exit Warning Popup

![](mental-health-assistant-user-manual-ys-5-01-224/079.png)

### CAT Specific Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following paragraphs cover actions specific to the CAT administration.

#### Finish Actions Staff Entry – CAT Terms of Service

The Terms of Service for the CAT administration must be accepted before the administration can begin. A detailed outline of the Terms of Service can be viewed by selecting the HERE link in the webpage. Click the I Agree button to continue to the CAT instrument administration.

<span id="_Toc167187335" class="anchor"></span>Figure 67: Staff Entry - CAT Terms of Service

![](mental-health-assistant-user-manual-ys-5-01-224/080.png)

#### Staff Entry – CAT - Begin Questions

This window displays the instructions on the completion of the CAT assignment and should be reviewed thoroughly by the user before proceeding. Click the Begin questions button to continue (Figure 68).

<span id="_Ref111795745" class="anchor"></span>Figure 68: CAT Begin Questions

![](mental-health-assistant-user-manual-ys-5-01-224/081.png)

#### Staff Entry – CAT - Timeframe Reminder

A timeframe reminder window appears which displays the timeframe selected during the creation of the CAT administration. This is the timeframe to use when answering the questions (Figure 69).

<span id="_Ref111795799" class="anchor"></span>Figure 69: CAT Timeframe Reminder

![](mental-health-assistant-user-manual-ys-5-01-224/082.png)

#### Staff Entry – CAT Administration Questions

CAT administrations are always executed one question at a time. Due to the complexity of the questions for multi-CAT administrations, neither question numbers nor progress status are displayed to the user and the ability to go backward and answer a previous question is not available to the user during a CAT administration (Figure 70).

<span id="_Ref111795942" class="anchor"></span>Figure 70: CAT Administration Questions

![](mental-health-assistant-user-manual-ys-5-01-224/083.png)

### Finishing an Administration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once an assessment is complete, the user can select the Finish button and MHA opens the Progress Note window that allows the user to Save Note, Do Not Save Note, or Copy Text (Figure 71).

<span id="_Ref111796169" class="anchor"></span>Figure 71: Finish Button

![](mental-health-assistant-user-manual-ys-5-01-224/084.png)

#### Save Note

Selecting the Save Note button creates a Progress Note for the administration in CPRS (Figure 73). The report created from the completed administration is accessible in the Completed Instruments section of MHA.

#### Do Not Save Note

Selecting the Do Not Save Note button will NOT create a Progress Note for the administration in CPRS (Figure 73). However, the report created from the completed administration is accessible in the Completed Instruments section of MHA. Choosing to not save a Note will present a confirmation dialog (Figure 72) allowing the decision to be reviewed. Selecting "Yes" will file the results, but not create a Progress Note. Selecting "No" will take the user back to the Progress Note window.

<span id="_Ref164178309" class="anchor"></span>Figure : Do Not Save Progress Note

![](mental-health-assistant-user-manual-ys-5-01-224/085.png)

#### Copy Text

Selecting the Copy Text button allows the user to copy the Progress Note information to the clipboard for pasting into other applications (Figure 73).

<span id="_Ref111796259" class="anchor"></span>Figure 73: Save Progress Note Action Buttons

![](mental-health-assistant-user-manual-ys-5-01-224/086.png)

### Restricted Instrument(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the instrument being completed in the assessment is a restricted instrument, MHA will NOT create a Progress Note to be stored in VistA when the provider selects Finish and a popup will appear notifying the provider of this (Figure 74). Selecting Continue returns the user to the MHA main landing page where they can then select the instrument name and view the report for that date of completion.

<span id="_Ref111796487" class="anchor"></span>Figure 74: Restricted Instrument Warning Popup

![](mental-health-assistant-user-manual-ys-5-01-224/087.png)

## Completed Instruments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Completed Instruments section displays all instruments that have been completed for a patient from any application that saves data to VistA. To see the history of a specific instrument, select the instrument and then select the desired date from the list of dates that appears on the left side of the instrument report field.

<span id="_Toc167187343" class="anchor"></span>Figure : Completed Instruments Field

![](mental-health-assistant-user-manual-ys-5-01-224/088.png)

### Reviewing Completed Instruments (Reports / Graphs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon the completion of an assessment by either the patient or a user, a report is generated for the completed assessment and is viewable in the Completed Instruments section of the main MHA landing page. To view this report, the user needs to select the desired instrument name and then select the appropriate date for the report. Once selected, MHA will display the details of the report for review (Figure 76).

<span id="_Ref111796609" class="anchor"></span>Figure 76: Completed Instruments - Displayed Report

![](mental-health-assistant-user-manual-ys-5-01-224/089.png)

There are two icons that might appear on a Completed Instrument header, High Risk Response and Positive Response icons ![](mental-health-assistant-user-manual-ys-5-01-224/090.png). The High-Risk Response icon ![](mental-health-assistant-user-manual-ys-5-01-224/091.png) indicates that a patient has answered a question (or a set of questions) indicating suicidality. The Positive Response icon ![](mental-health-assistant-user-manual-ys-5-01-224/092.png) indicates that a patient has answered a question (or a set of questions) that indicate a positive direction to alert the provider that additional clinical assessment is indicated.

### Graphs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option to review the data within the report in a graphical format is also available to the user. The user must select the ![](mental-health-assistant-user-manual-ys-5-01-224/093.png) icon to display the data. The history of all assessments related to that selected instrument is available for review, and a table of information is provided for reference (Figure 77).

<span id="_Ref111796667" class="anchor"></span>Figure 77: Graphed Instrument Results

![](mental-health-assistant-user-manual-ys-5-01-224/094.png)

A legend is provided to the right of the graph which shows the metric that is displayed in the graph. The legend is color-coded for easier viewing of assessments that have multi-value metrics. This information comes directly from the data table below the graph (Figure 77).

> The user can also use the slider bar at the top of the graph to display data based on a desired date range. The user must use their mouse to click on the slide bar and then drag it right or left to gain the desired display of graphed data (Figure 78 and Figure 79).

<span id="_Ref111797259" class="anchor"></span>Figure 78: Graph Slider Bar Adjustments (Expanded Range)

![](mental-health-assistant-user-manual-ys-5-01-224/095.png)

<span id="_Ref111797312" class="anchor"></span>Figure 79: Graph Slider Bar Adjustments (Narrowed Range)

![](mental-health-assistant-user-manual-ys-5-01-224/096.png)

The table can also be filtered for specific trending information if the user so desires. This can be accomplished by selecting the ![](mental-health-assistant-user-manual-ys-5-01-224/097.png) icon beside a specific category to expand the subcategories and review the results. To graph the results for this subcategory, select the checkbox beside the category in the data reference table. The graphical display automatically updates based on the user selection, and the legend also updates to reflect which colors are associated with each component of the subcategories. Inversely, if the user wants to close the expanded category, they must select the ![](mental-health-assistant-user-manual-ys-5-01-224/098.png) icon (Figure 80).

<span id="_Ref111797372" class="anchor"></span>Figure 80: Data Table - Expanded Categories

![](mental-health-assistant-user-manual-ys-5-01-224/099.png)

### Append Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An additional option for appending comments to the patient report has been added to MHA. By selecting the ![](mental-health-assistant-user-manual-ys-5-01-224/100.png) icon, the screen updates to display two additional fields. The first is Previous Comments, which allows the user to see comments that have already been added to the report. The second is New Comment, which is a required field to save the changes and allows the user to add additional notes to the patient's report. After entering the desired information, the user can select Save to add those changes to the report or Cancel to discard the changes. Once the changes have been made, they cannot be removed.

\*\*\*NOTE\*\*\* Print functionality is not available from the Append Comments view

(Figure 81). \*\*\*

<span id="_Ref111797493" class="anchor"></span>Figure 81: Append Comments Screen

![](mental-health-assistant-user-manual-ys-5-01-224/101.png)

### Delete Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By selecting the ![](mental-health-assistant-user-manual-ys-5-01-224/102.png) icon, the user will be prompted with the Warning popup. The user can select either the Cancel or Confirm button. Selecting Cancel will exit the popup without deleting an assignment; selecting the Confirm button will prompt another modal stating Information. The user can then close the popup and the completed report will be deleted from MHA. The Reports window refreshes automatically and displays the most recently completed report.

> **NOTE:** \*\*\* The option to delete an assignment has been granted to users with the required VistA keys. If the user does not have the appropriate permissions to delete a report, then a message will appear stating: You do not have VistA permission to delete Completed Reports. Please contact your supervisor or ADPAC/CAC for assistance [(Figure 82, Figure 83, Figure 84](#_Ref125445518)) Please see KB0116992 - MHA Web: Deleting an Erroneously Completed Report in Mental Health Assistant Web for more information\*\*\*

<span id="_Ref164178919" class="anchor"></span>Figure 82: Delete Assignment Popup

![](mental-health-assistant-user-manual-ys-5-01-224/103.png)

<span id="_Ref164178940" class="anchor"></span>Figure 83: Assignment Deleted Popup

![](mental-health-assistant-user-manual-ys-5-01-224/104.png)

<span id="_Ref125445518" class="anchor"></span>Figure 84: Permission Notification

![](mental-health-assistant-user-manual-ys-5-01-224/105.png)

### Printing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can print the current report or graph that is selected. Depending on what is being displayed (report or graph), clicking the ![](mental-health-assistant-user-manual-ys-5-01-224/106.png) button takes the provider to a print screen to confirm the selection. This works for the different graphing options Column and Line Graph (Figure 85, Figure 86, Figure 87). When printing a report, the last 4 of the patient SSN will be removed.

<span id="_Ref111797701" class="anchor"></span>Figure 85: Printing - Report Screen

![](mental-health-assistant-user-manual-ys-5-01-224/107.png)

<span id="_Ref111797705" class="anchor"></span>Figure 86: Printing - Column Graph

![](mental-health-assistant-user-manual-ys-5-01-224/108.png)

<span id="_Ref111797708" class="anchor"></span>Figure 87: Printing - Line Graph

![](mental-health-assistant-user-manual-ys-5-01-224/109.png)

### Special Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Special Reports allows the provider to view and compare graphs for up to eight different instruments simultaneously on a single page view. It also allows the creation of a single graph using up to 4 scales to compare disparate instrument results.

#### Special Reports – Multiple Graphs

To configure multiple graphs on a single page, select the +/- symbol to display the instrument list. Up to 8 instruments can be selected at one time. The Show Line Graph button can also be selected to change all bar graphs to line graphs. A slider is active above each graph to zoom in on specific points within each graph. The user can swap the order of the displayed graphs using the ![](mental-health-assistant-user-manual-ys-5-01-224/110.png) button.

<span id="_Toc167187356" class="anchor"></span>Figure Special Reports - No Instruments

![](mental-health-assistant-user-manual-ys-5-01-224/111.png)

<span id="_Toc167187357" class="anchor"></span>Figure Special Reports - Instrument Selection

![](mental-health-assistant-user-manual-ys-5-01-224/112.png)

<span id="_Toc167187358" class="anchor"></span>Figure Special Reports - Multiple Instruments

![](mental-health-assistant-user-manual-ys-5-01-224/113.png)

#### Special Reports – Single Graph

Selecting the Single Graph button allows the user to view different measures from the selected instruments on a single graph. Up to 4 different scales can be selected from the instruments displayed in Multiple Graphs tab. The scales of the selected instruments can be chosen by using the carat to expand the scales next to the instrument name and clicking the checkbox beside the desired scale.

<span id="_Toc167187359" class="anchor"></span>Figure Special Reports - Single Graph with No Scales

![](mental-health-assistant-user-manual-ys-5-01-224/114.png)

<span id="_Toc167187360" class="anchor"></span>Figure Special Reports - Single Graph with Multiple Scales

![](mental-health-assistant-user-manual-ys-5-01-224/115.png)

## MHA Server Timeout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MHA user will receive the timeout notification at the value specified in VistA. At the timeout -5-minute mark, a warning modal appears allowing the user to continue the session or be automatically logged out of the session. If the Continue button is not selected, MHA automatically ends that session and logs the user out of the application (Figure 93).

<span id="_Ref164246166" class="anchor"></span>Figure Timeout Popup

![](mental-health-assistant-user-manual-ys-5-01-224/116.png)

## Special Instrument Notification in Staff Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Certain instruments require special training/certification before they can be executed by a clinician. When a clinician attempts to complete any of the Montreal Cognitive Assessment (MoCA) instruments, a warning modal appears that informs them of the requirement for the certification training required to administer the instrument, this modal must be acknowledged before the clinician can proceed with the administration. If the provider answers No to the Attestation, the assignment will be deleted, and the provider will be returned to the Landing Page.

<span id="_Toc167187362" class="anchor"></span>Figure MoCA Attestation Popup

![](mental-health-assistant-user-manual-ys-5-01-224/117.png)

## Logout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MHA footer contains a Logout button that should be used every time the provider is leaving the application. This redirects the user to the Identity and Access Management (IAM) logout page, click Logout on this page as well. Do NOT close the browser using the X/Close button in the upper-right corner from within MHA. This ensures the user is logged completely out of Identity Management.

<span id="_Ref125446980" class="anchor"></span>Figure MHA Logout Button

![](mental-health-assistant-user-manual-ys-5-01-224/118.png)

<span id="_Toc167187364" class="anchor"></span>Figure IAM (SSOi) Logout Button

![](mental-health-assistant-user-manual-ys-5-01-224/119.png)

<span id="_Toc167187365" class="anchor"></span>Figure Logged Out Screen

![](mental-health-assistant-user-manual-ys-5-01-224/120.png)

# MHA Dashboard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following paragraphs provide details on accessing and using the Dashboard. The Dashboard consists of three views contained within two tabs, Review Assessments tab and Missed Assignments tab. The Review Assessments tab contains 2 views, Views Assessments and View Site Assessments.

## Accessing Review Assessments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once successfully logged into MHA, select the Dashboard ![](mental-health-assistant-user-manual-ys-5-01-224/121.png) to open the Dashboard view.

<span id="_Toc167187366" class="anchor"></span>Figure Accessing Dashboard from MHA

![](mental-health-assistant-user-manual-ys-5-01-224/122.png)

## Review Assessment(s) Dashboard View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Review Assessment(s) view is designed to allow Providers to see quickly what assessments assigned through the MHC Assignment window have been completed by Veterans. There are two sub-views underneath, the currently logged in Providers view and the Site Assessment(s) view.

<span id="_Ref142986064" class="anchor"></span>Figure Review Assessment(s) Dashboard

![](mental-health-assistant-user-manual-ys-5-01-224/123.png)

### View Assessment(s) Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Assessment(s) Dashboard displays all completed assessments that were performed by the Veteran through the MHC Patient Application that have not been reviewed by the provider. By default, it is filtered to assessment statuses that require a provider's attention (Needs Review & Overdue). This filter can be changed by selecting the desired Review Status (if more than one is desired, use CTRL + Click to select). There is a Date Range available to limit the amount of data returned to the provider. The options are 14 days (default), 30 days, 6 months and 1 year.

#### View Assessment(s) Columns

The View Assessment(s) Dashboard limits the data displayed to the currently logged in provider. There are nine columns in the View Assessment(s) Dashboard. Each column can be filtered by typing into the text entry box to limit the data displayed. Deleting the filter will display all data again.

- Patient - The name of the patient that completed the assessment.
- Provider – The provider that ordered the assessment. Also, the person responsible for signing the Progress Note (if desired).
- Instrument – The instrument that was completed in the assessment.
- Score – If a score is calculated, it will be displayed in this column. Instruments that do not have a score will display a 0 for the value.
- Severity – The calculated severity of the assessment based upon the supplied responses. This will vary from instrument to instrument. There will be times when a severity is None but a warning for Positive Response is displayed due to the way a particular question was answered in the assessment.
- Completed Date – The date the Veteran completed the assignment through the MHC Patient Application.
- Review By – The date the assessment must be reviewed according to the Office of Mental Health and Suicide Prevention guidance.
  - Results with a potential for critical score require review within one business day.
  - Results without a potential for critical score require review within three business days.
- Review Status – The current review status of the assessment. There are two possible states:
  - Needs Reviewed – Still in the queue to be reviewed.
  - Overdue – The review date has passed, and the assessment review is now overdue. The row will be highlighted in a pink color.
- Action
  - View Report icon – ![](mental-health-assistant-user-manual-ys-5-01-224/124.png) This icon will bring up a window displaying a view of the selected assessment. Clicking View Report will mark the assessment as Reviewed (Figure 100).
    - View Report Window - The View Report window will have the same tools available as in the Patient Plan Completed Instruments along with an additional Create Note icon. The user will be able to view all assessments of the current instruments, view graphs, append comments and print the report/graphs. Clicking the Create Note icon ![](mental-health-assistant-user-manual-ys-5-01-224/125.png) will display a Progress Note window that will allow the user to edit the progress note and then Save the Note. Clicking Do Not Save Note, will still save the assessment, just will not create a Progress Note. This is the same window that will appear if the Create Note button is selected from the Dashboard.

<span id="_Ref164335067" class="anchor"></span>Figure View Report Window

![](mental-health-assistant-user-manual-ys-5-01-224/126.png)

- Create Note icon – ![](mental-health-assistant-user-manual-ys-5-01-224/127.png)This icon will display the same template as clicking Create Note from inside of the View Report screen. This will also mark the assessment as Reviewed.

<span id="_Toc167187369" class="anchor"></span>Figure Create Progress Note Window

![](mental-health-assistant-user-manual-ys-5-01-224/128.png)

- Send Patient Feedback icon – ![](mental-health-assistant-user-manual-ys-5-01-224/129.png)This icon opens a dialog which will allow the provider to send feedback to the Veteran.

<span id="_Ref142986252" class="anchor"></span>Figure Send Feedback to Veteran

![](mental-health-assistant-user-manual-ys-5-01-224/130.png)

### View Site Assessment(s) Dashboard View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Site Assessment(s) Dashboard displays all assessments completed on a Veterans device that are not reviewed for the entire site (3-digit code). There is a Date Range available to limit the amount of data returned to the provider. The options are 14 days (default), 30 days, 6 months and 1 year. When clicking on this link, a warning will appear verifying the provider has a need to know before viewing the data.

<span id="_Toc167187371" class="anchor"></span>Figure View Site Assessment(s) Warning

![](mental-health-assistant-user-manual-ys-5-01-224/131.png)

<span id="_Ref166075700" class="anchor"></span>Figure View Site Assessment(s) Dashboard

![](mental-health-assistant-user-manual-ys-5-01-224/132.png)

#### View Site Assessment(s) Columns

The View Assessment(s) Dashboard displays all assessment reports for all patients and all providers.

- Patient - The name of the patient that completed the assessment.
- Provider – The provider that ordered the assessment. Also, the person responsible for signing the Progress Note.
- Instrument – The instrument that was completed in the assessment.
- Score – If a score is calculated, it will be displayed in this column. Instruments that do not have a score will display a 0 for the value
- Severity – The calculated severity of the assessment based upon the supplied responses. This will vary from instrument to instrument. There will be times when a severity is None but a warning for Positive Response is displayed due to the way a particular question was answered in the assessment.
- Completed Date – The date the Veteran completed the assignment through the MHC Patient Application
- Review By – The date the assessment must be reviewed according to the Office of Mental Health and Suicide Prevention guidance.
  - Results with a potential for critical score require review within one business day
  - Results without a potential for critical score require review within three business days.
- Review Status – The current review status of the assessment. There are two possible states
  - Needs Reviewed – Still in the queue to be reviewed.
  - Overdue – The review date has passed, and the assessment review is now overdue
- Action
  - View Report icon – ![](mental-health-assistant-user-manual-ys-5-01-224/133.png) This icon (Figure 104) will bring up a window displaying a view of the selected assessment.
    - View Report Window - The View Report window will have the same tools available as in the Patient Plan Completed Instruments along with an additional Create Note icon. The user will be able to view all assessments of the current instruments, view graphs, append comments and print the report/graphs. Clicking the Create Note icon ![](mental-health-assistant-user-manual-ys-5-01-224/134.png) will display a Progress Note window that will allow the user to edit the progress note and then Save the Note.
    - Message – Clicking the Message icon ![](mental-health-assistant-user-manual-ys-5-01-224/135.png) will open a Teams message to the responsible provider.

## Missed Assignments View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following paragraphs detail the Missed Assignments view.

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Missed Assignments view allows the user to view a list of all patient(s) that have not completed their remote assessment(s).

<span id="_Ref125448052" class="anchor"></span>Figure Missed Assignments View

![](mental-health-assistant-user-manual-ys-5-01-224/136.png)

### Missed Assignments Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Missed Assignments view allows the user to view a list of all patient(s) that have not completed their remote assessment(s).

- Patient - The name of the patient that completed the assessment.
- Provider – The provider that ordered the assessment. Also, the person responsible for signing the Progress Note
- Start Date – When the assignment was supposed to begin.
- Due On – When the assignment was supposed to be completed by the patient.
- Instrument – Acronym of the instrument that was supposed to be completed by the patient.

### Missed Assignments Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A search capability is provided to allow for locating data based on a text string. To access the search feature, click on the search box in the upper right-hand corner and begin entering the string you wish to search.

<span id="_Toc167187374" class="anchor"></span>Figure Missed Assignments View Search

![](mental-health-assistant-user-manual-ys-5-01-224/137.png)

### Missed Assignments Sorting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The fields in the Missed Assignments view can be sorted by selecting the arrows ![](mental-health-assistant-user-manual-ys-5-01-224/138.png) beside the field name. The view can be switched between ascending and descending order.

# MHA Patient Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following paragraphs provide details on Patient Entry.

## Patient Entry Instrument Completion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once an assignment has been created for a patient using the Patient Entry button in the Instrument Administrator, the patient can use the generated Assignment ID to access and complete their assignments.

### Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Details on logging in to Patient Entry:

- The version number of Patient Entry is displayed in light-gray text in the upper left corner of the application (Figure 107).
- The login page requires the unique ID of the assignment a patient is trying to access (the number that is displayed to the provider when the assignment is created) and the last four digits of their SSN.
- Patient must enter the information and click Login to continue.
- Incorrect information triggers a popup identifying an error.

<span id="_Ref164337118" class="anchor"></span>Figure Patient Entry Login Screen

![](mental-health-assistant-user-manual-ys-5-01-224/139.png)

### Welcome Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Once logged in, patients are directed to the Welcome Screen (Figure 108). Patients should check to make sure their information in the top right corner is correct.
- If their information is incorrect, they should click Logout and inform their provider.
- Patients should review the table displaying their pending questionnaires.
  1.  The estimated time to complete each instrument is displayed on the right side of the table.
  2.  The total estimated time to complete all instruments is displayed below the table.
  3.  If there is only one pending questionnaire, it will not be shown in the table format.
  4.  Completed questionnaires will show as Complete instead of showing an estimated time.
- Clicking Begin loads the first questionnaire. If a patient is unable to work on a questionnaire at this time, they should click Logout.

<span id="_Ref164337223" class="anchor"></span>Figure Patient Entry Welcome Screen

![](mental-health-assistant-user-manual-ys-5-01-224/140.png)

### Completing an Administration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Patients now see the view in the following figure (Figure 109).
  1.  The current instrument is always displayed in the upper left, and the progress is a darkened tab in the navigation bar. Patient information is always displayed in the upper right.
  2.  Progress is displayed by the bar along the bottom of the screen for the current instrument, as well as in each tab for that instrument.
  3.  The version number for Patient Entry is moved to the bottom left corner of the window.

<span id="_Ref112222669" class="anchor"></span>Figure 109: Patient Entry Completing Administration

![](mental-health-assistant-user-manual-ys-5-01-224/141.png)

- Questions can be answered by clicking on the button next to the appropriate answer.
- Selecting an answer automatically takes the patient to the next question if Use speed tab is checked.
- If Use speed tab is checked, pressing a number key on the keyboard that corresponds with an answer to the question selects that answer, if the question is in focus.
1.  This moves patient to the next question.
2.  Focus is shown by the yellow box (Figure 110).

<span id="_Ref112075821" class="anchor"></span>Figure 110: Patient Entry Focus

![](mental-health-assistant-user-manual-ys-5-01-224/142.png)

- If Use speed tab is not checked, click Next Question to move on.
  - Prior Question is disabled on the first question.
- Clicking the Save and Exit button allows patients to exit the administration and finish it at another time.
  - A popup asks patients to confirm their choice.

<span id="_Toc167187379" class="anchor"></span>Figure 111: Patient Entry Incomplete Assignment

![](mental-health-assistant-user-manual-ys-5-01-224/143.png)

- Clicking a different instrument's name in the navigation bar moves patient to that instrument. Current progress will be saved.

<span id="_Ref112140772" class="anchor"></span>Figure 112: Patient Entry Skipped Question

![](mental-health-assistant-user-manual-ys-5-01-224/144.png)

- If questions have been skipped, the tab will display a red exclamation mark

  (Figure 112).
- A popup will show any skipped questions and ask patient to confirm their choice

  (Figure 113).

<span id="_Ref112140828" class="anchor"></span>Figure 113: Patient Entry Incomplete Assignment

![](mental-health-assistant-user-manual-ys-5-01-224/145.png)

- Once all applicable questions have been answered, click Submit (Figure 114).
1.  The Submit button is only available once all questions in a questionnaire have been viewed.
2.  Submitting sends the finished questionnaire to the assigning clinician and all answers are final.

<span id="_Ref112077432" class="anchor"></span>Figure 114: Patient Entry Submit Button

![](mental-health-assistant-user-manual-ys-5-01-224/146.png)

- If there are multiple questionnaires in a patient's assigned administration, they are shown this screen confirming they have been submitted (Figure 115).

<span id="_Ref112075280" class="anchor"></span>Figure 115: Patient Entry Success Submission

![](mental-health-assistant-user-manual-ys-5-01-224/147.png)

- Click Continue if ready to complete the next questionnaire.
- If not ready to complete the shown questionnaire, click Save and Exit. This saves all progress on any questionnaire not yet submitted and returns to the login screen.
- If the questionnaire is incomplete, it will display this screen instead (Figure 116).
- Patients are informed how many days remain to complete the questionnaire.
- Patients still have the option to Continue or Save & Exit.

<span id="_Ref112074472" class="anchor"></span>Figure 116: Patient Entry Incomplete Assessment

![](mental-health-assistant-user-manual-ys-5-01-224/148.png)

### Navigating Patient Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- To go back to a question, click the Prior Question button.

<span id="_Toc167187385" class="anchor"></span>Figure 117: Patient Entry Navigation

![](mental-health-assistant-user-manual-ys-5-01-224/149.png)

- Patients may review their answers at any time using the Review Answers button.
- A popup appears that shows all questions in the current instrument and any selected answers (Figure 118).

<span id="_Ref112078519" class="anchor"></span>Figure 118: Patient Entry Review Answers

![](mental-health-assistant-user-manual-ys-5-01-224/150.png)

- Patients can click on any question in this popup to be returned to that question.
- Once all applicable questions have been answered, click Submit.
- Submitted questionnaires will be visually identified in the navigation bar.
- The tab will have 100% progress, a checkmark, and will be disabled.

<span id="_Toc167187387" class="anchor"></span>Figure 119: Patient Entry Completed Assessment

![](mental-health-assistant-user-manual-ys-5-01-224/151.png)

- Answer all questions on remaining questionnaires and click Submit on each.

<span id="_Toc167187388" class="anchor"></span>Figure 120: Submit Button

![](mental-health-assistant-user-manual-ys-5-01-224/152.png)

- After the last questionnaire in the administration is complete, patients are shown the completion screen.
- Patients should click Logout and return the device to their provider if necessary.
1.  At any other point within the application, idle logout happens after 5 minutes. Patients are notified before this occurs.
2.  On this page, automatic logout will occur in 10 seconds.

<span id="_Toc167187389" class="anchor"></span>Figure 121: Submitted Notification

![](mental-health-assistant-user-manual-ys-5-01-224/153.png)

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Error Selecting a Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Ref125450150" class="anchor"></span>Figure 122: Error selecting a division

![](mental-health-assistant-user-manual-ys-5-01-224/154.png)

This is actually a very common problem in the MHA user community but it's an issue that is out of the control of the MHA team. The usual issue is that when onboarding occurred, a step was missed to associate the PIV card with the VistA/CPRS instance being used. There is a Help Desk article on how to complete the association. If more assistance is needed, please submit a YourIT ticket to the Help Desk asking to associate the PIV card with the correct VistA instance. See (KB0116974 - MHA Web: Gain Access to Mental Health Assistance Web) for more information.

## Service Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are four different service errors that can occur which will affect MHA. If an error occurs, it will be displayed below the Banner.

<span id="_Toc167187391" class="anchor"></span>Figure 123: Example of Service Errors Expanded

![](mental-health-assistant-user-manual-ys-5-01-224/155.png)

Each error can be collapsed to save screen space:

<span id="_Ref125450153" class="anchor"></span>Figure 124: Example of Service Errors Collapsed

![](mental-health-assistant-user-manual-ys-5-01-224/156.png)

Clicking on any service name will display the complete error again

### Mental Health Checkup Service is Unavailable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All scheduling related functionality is disabled until the service has been restored.

### Mobile Secure Token Service is Unavailable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All scheduling related functionality is disabled until the service has been restored.

### IAM SSOi Service is Unavailable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA Identity and Access Management application is currently unavailable. User will not be able to log into MHA until the service has been restored.

### VistA Service is Unavailable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All patient data is unavailable until the service has been restored.

# Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term | Meaning                                             |
|----------|---------------------------------------------------------|
| ADPAC    | Automated Data Processing Application Coordinator       |
| CAC      | Clinical Application Coordinators                       |
| CAT      | Computerized Adaptive Testing                           |
| CCOW     | Clinical Context Object Workgroup                       |
| CPRS     | Computerized Patient Record System                      |
| IAM      | Identity and Access Management                          |
| ID       | Identification                                          |
| MH       | Mental Health                                           |
| MHA      | Mental Health Assistant                                 |
| MHC      | Mental Health Checkup                                   |
| MHP      | Mental Health Package                                   |
| MoCA     | Montreal Cognitive Assessment                           |
| OIT      | Office of Information and Technology                    |
| PDF      | Portable Document Format                                |
| PIN      | Personal Identification Number                          |
| PIV      | Personal Identity Verification                          |
| SSN      | Social Security Number                                  |
| SSOi     | Single Sign-On Internal                                 |
| VA       | Veterans Administration                                 |
| VistA    | Veterans Information System and Technology Architecture |
AcronymsList of acronyms used throughout this document.
