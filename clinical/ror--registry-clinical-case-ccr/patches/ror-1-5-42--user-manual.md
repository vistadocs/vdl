---
title: ROR*1.5*42 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: 
app_code: ROR
app_name: "Registry: Clinical Case (CCR)"
section: CLI
app_status: active
pkg_ns: ROR
patch_ver: 1.5
patch_id: ROR*1.5*42
group_key: "ROR:ROR:1.5"
file_numbers: 
  - 60
  - 63
security_keys: 
  - ROR VA IRM
menu_options: 12
description: The Clinical Case Registries (CCR) software application collects data on the population of Veterans with certain clinical conditions, including two national registries for [Hepatitis C](#Glos_HEPC) and [Human Immunodeficiency Virus](#Glos_HIV) (HIV) infections, and 51 generic, local registries.
audience: 
keywords: 
  - class
  - table
  - report
  - registry
  - span
  - contents
  - href
  - blockquote
  - colspan
  - patients
page_count: 0
word_count: 85418
section_count: 129
table_count: 158
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Clinical_Case_Registries/ror1_5_42um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Clinical_Case_Registries/ror1_5_42um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=126"
---

Clinical Case Registries (CCR)

| ![](ror-1-5-42-user-manual/001.png) |
|-----------------------------------------------------------------------------------------------------------------------|

<span id="_Ref272342025" class="anchor"></span>Table 1 – Typographical Conventions

User Manual

*Documentation Revised June 2024For Patch ROR\*1.5\*42  
*THIS PAGE INTENTIONALLY LEFT BLANK

Revision History

<table>
<caption><p><span id="_Toc167263940" class="anchor"></span>Table 2 – Graphic Icons</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 47%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description</th>
<th>Author / Role</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>June, 2024</td>
<td>Final release for Patch ROR*1.5*42. See <a href="#patch-ror1.542">Table 66</a> for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>April, 2023</td>
<td>Final release for Patch ROR*1.5*41. See <a href="#patch-ror1.541">Table 64</a> for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>November, 2022</td>
<td>Final release for Patch ROR*1.5*40. See <a href="#patch-ror1.540">Table 62</a> for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>January, 2022</td>
<td>Final release for Patch ROR*1.5*39. See <a href="#patch-ror1.539">Table 60</a> for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>June, 2021</td>
<td>Final release for Patch ROR*1.5*38. See Table 58 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>November, 2020</td>
<td>Final release for Patch ROR*1.5*37. See Table 56 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>May, 2020</td>
<td>Final release for Patch ROR*1.5*36. See <a href="#patch-ror1.536">Table 54</a> for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>November, 2019</td>
<td>Final release for Patch ROR*1.5*35. See Table 52 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>March, 2019</td>
<td>Final release for Patch ROR*1.5*34. See Table 50 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>July, 2018</td>
<td>Final release for Patch ROR*1.5*33. See Table 48 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>April, 2018</td>
<td>Final release for Patch ROR*1.5*32. See Table 46 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>November, 2017</td>
<td>Final release for Patch ROR*1.5*31. See Table 44 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>May, 2017</td>
<td>Final release for Patch ROR*1.5*30. See Table 42 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>December, 2016</td>
<td>Final release for Patch ROR*1.5*29. See Table 40 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>May, 2016</td>
<td>Final release for Patch ROR*1.5*28. See Table 44 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>June, 2015</td>
<td>Final release for Patch ROR*1.5*26. See Table 36 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>June, 2015</td>
<td>Final release for Patch ROR*1.5*25. See Table 34 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>April, 2015</td>
<td>Final release for Patch ROR*1.5*27. See Table 32 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>October, 2014</td>
<td>Final release for Patch ROR*1.5*24. See Table 30 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>August, 2014</td>
<td>Final release for Patch ROR*1.5*22. See Table 28 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>April, 2014</td>
<td>Final release for Patch ROR*1.5*21. See Table 26 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>August, 2014</td>
<td>Final release for Patch ROR*1.5*19. See Table 24 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>March, 2013</td>
<td>Final release for Patch ROR*1.5*20. See Table 22 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>August, 2012</td>
<td>Final release for Patch ROR*1.5*18. See Table 20 for Details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>April, 2012</td>
<td><p>Final release for Patch ROR*1.5*17. See Table 18 for Details.</p>
<p><em>Documentation Only change:</em> Added “Return to Local Reports Table” links to each subsection of Section 10</p></td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>September, 2011</td>
<td><p>Final release for Patch ROR*1.5*15. See Table 16 for Details.</p>
<p><em>Documentation Only change:</em> Reworked Section 10 – Local Reports to remove redundancy and reduce the size of the document.</p></td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>March, 2011</td>
<td>Patch ROR*1.5*14. See <em>User Manual</em> for details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>December, 2010</td>
<td><p>Final release for Patch ROR*1.5*13. See Table 12 for Details.</p>
<p><em>Documentation Only change:</em> Moved Resource material formerly in Appendix A, Appendix B, CCR:HIV Registry Pending Patient Worksheet, Appendix C, and Appendix D to main body of text.</p></td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>April, 2010</td>
<td><p>Final release for Patch ROR*1.5*10: See Table 11 for details.</p>
<p>The numerous footnotes concerning changes made by various patches were moved to the end of the document as endnotes, rather than footnotes.</p></td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>(unknown)</td>
<td>Patch ROR*1.5*9 was a maintenance bug fix, and is not documented in this manual.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>September, 2009</td>
<td>Patch ROR*1.5*8: See Table 10 for details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>July, 2008</td>
<td>Patch ROR*1.5*7: See Table 9 for details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>May, 2008</td>
<td>Patch ROR*1.5*6: See Table 8 for details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>March, 2008</td>
<td>Patch ROR*1.5*5: See Table 7 for details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>December, 2007</td>
<td>Patch ROR*1.5*4: See Table 6 for details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>November, 2007</td>
<td>Patch ROR*1.5*3: See Table 5 for details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>October, 2007</td>
<td>Patch ROR*1.5*2: See Table 4 for details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>October 2006</td>
<td>Patch ROR*1.5*1: See Table 3 for details.</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="odd">
<td>February 2006</td>
<td>Completely updated for CCR Version 1.5</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
<tr class="even">
<td>June 2002</td>
<td>Initial release of CCR Version 1.0</td>
<td>See CCR Redacted document for the list of authors and roles.</td>
</tr>
</tbody>
</table>

<span id="_Toc167263940" class="anchor"></span>Table 2 – Graphic Icons

Table of Contents

Table of Figures

Table of Tables

![](ror-1-5-42-user-manual/002.png)

# Orientation 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Orientation](#orientation)
  - [Clinical Case Registries Software Application](#clinical-case-registries-software-application)
  - [Purpose of the Manual](#purpose-of-the-manual)
  - [Recommended Users](#recommended-users)
  - [Typographical Conventions Used in the Manual](#typographical-conventions-used-in-the-manual)
  - [Related Documents](#related-documents)
  - [Disclaimer](#disclaimer)
  - [Navigating Hyperlinks](#navigating-hyperlinks)
- [Introduction](#introduction)
  - [Overview](#overview)
  - [Software Features and Functions](#software-features-and-functions)
  - [About Clinical Case Registries 1.5](#about-clinical-case-registries-15)
  - [Decommissioned Software](#decommissioned-software)
    - [Immunology Case Registry v2.1](#immunology-case-registry-v21)
  - [Hepatitis C Case Registry v1.0](#hepatitis-c-case-registry-v10)
    - [Automatic Pending Case Identification](#automatic-pending-case-identification)
    - [‘Local Fields’ For Customizing Local Registry Specific Data](#local-fields-for-customizing-local-registry-specific-data)
    - [CCR Procedures Report](#ccr-procedures-report)
    - [Optional Entry of Risk Behavior](#optional-entry-of-risk-behavior)
  - [CCR Patches ROR\1.5\X](#ccr-patches-ror15x)
    - [Patch ROR\1.5\1](#patch-ror151)
    - [Patch ROR\1.5\2](#patch-ror152)
    - [Patch ROR\1.5\3](#patch-ror153)
    - [Patch ROR\1.5\4](#patch-ror154)
    - [Patch ROR\1.5\5](#patch-ror155)
    - [Patch ROR\1.5\6](#patch-ror156)
    - [Patch ROR\1.5\7](#patch-ror157)
    - [Patch ROR\1.5\8](#patch-ror158)
    - [Patch ROR\1.5\10](#patch-ror1510)
    - [Patch ROR\1.5\13](#patch-ror1513)
    - [Patch ROR\1.5\14](#patch-ror1514)
    - [Patch ROR\1.5\15](#patch-ror1515)
    - [Patch ROR\1.5\17](#patch-ror1517)
    - [Patch ROR\1.5\18](#patch-ror1518)
    - [Patch ROR\1.5\20](#patch-ror1520)
    - [Patch ROR\1.5\19](#patch-ror1519)
    - [Patch ROR\1.5\21](#patch-ror1521)
    - [Patch ROR\1.5\22](#patch-ror1522)
    - [Patch ROR\1.5\24](#patch-ror1524)
    - [Patch ROR\1.5\27](#patch-ror1527)
    - [Patch ROR\1.5\25](#patch-ror1525)
    - [Patch ROR\1.5\26](#patch-ror1526)
    - [Patch ROR\1.5\28](#patch-ror1528)
    - [Patch ROR\1.5\29](#patch-ror1529)
    - [Patch ROR\1.5\30](#patch-ror1530)
    - [Patch ROR\1.5\31](#patch-ror1531)
    - [Patch ROR\1.5\32](#patch-ror1532)
    - [Patch ROR\1.5\33](#patch-ror1533)
    - [Patch ROR\1.5\34](#patch-ror1534)
    - [Patch ROR\1.5\35](#patch-ror1535)
    - [Patch ROR\1.5\36](#patch-ror1536)
    - [Patch ROR\1.5\37](#patch-ror1537)
    - [Patch ROR\1.5\38](#patch-ror1538)
    - [Patch ROR\1.5\39](#patch-ror1539)
    - [Patch ROR\1.5\40](#patch-ror1540)
    - [Patch ROR\1.5\41](#patch-ror1541)
    - [Patch ROR\1.5\42](#patch-ror1542)
  - [Obtaining Software and Documentation](#obtaining-software-and-documentation)
  - [Accessibility Features in Clinical Case Registries 1.5](#accessibility-features-in-clinical-case-registries-15)
  - [VistA Documentation on the Intranet](#vista-documentation-on-the-intranet)
- [About the CCR Interface](#about-the-ccr-interface)
  - [Remote Procedure Calls and the Broker](#remote-procedure-calls-and-the-broker)
  - [Graphical User Interface Conventions](#graphical-user-interface-conventions)
    - [Windows](#windows)
    - [Pop-up Windows](#pop-up-windows)
    - [Windows GUI Elements](#windows-gui-elements)
    - [Text Box](#text-box)
    - [Checkbox](#checkbox)
    - [Radio button](#radio-button)
    - [Command buttons and Command icons](#command-buttons-and-command-icons)
    - [Date field](#date-field)
    - [Drop-Down List](#drop-down-list)
    - [List Box](#list-box)
    - [Faded (“Grayed Out”) Choices](#faded-grayed-out-choices)
    - [Keyboard Commands](#keyboard-commands)
    - [Fields with Non-White Background](#fields-with-non-white-background)
    - [Tab Key](#tab-key)
    - [Changing (Resizing) a Window](#changing-resizing-a-window)
    - [Cancel](#cancel)
    - [Close](#close)
    - [Edit](#edit)
    - [Find](#find)
    - [Help](#help)
    - [OK](#ok)
    - [Save](#save)
    - [Save As](#save-as)
    - [Search](#search)
    - [Selecting Multiple Items from a List](#selecting-multiple-items-from-a-list)
    - [Undo](#undo)
    - [Right-Click Menus](#right-click-menus)
    - [Pop-up Calendars](#pop-up-calendars)
    - [System Timeout](#system-timeout)
    - [Security Keys](#security-keys)
  - [Assistive Technology](#assistive-technology)
    - [Using the \< Alt \> and \< Esc \> Keys](#using-the-alt-and-esc-keys)
    - [Resizing the Screen](#resizing-the-screen)
    - [Changing the Screen Colors and Options](#changing-the-screen-colors-and-options)
    - [Windows Accessibility Shortcuts](#windows-accessibility-shortcuts)
  - [StickyKeys](#stickykeys)
  - [FilterKeys](#filterkeys)
  - [ToggleKeys](#togglekeys)
  - [MouseKeys](#mousekeys)
  - [HighContrast](#highcontrast)
    - [Tab Order on Report Setup Screens](#tab-order-on-report-setup-screens)
    - [Activating Drop-Down Lists](#activating-drop-down-lists)
    - [Navigating the Date Picker Calendar Pop-ups](#navigating-the-date-picker-calendar-pop-ups)
    - [Dual-List Controls](#dual-list-controls)
    - [Row and Header Information in Grids](#row-and-header-information-in-grids)
    - [Context-Sensitive Menus](#context-sensitive-menus)
- [Local Registry Population and Update](#local-registry-population-and-update)
  - [Initial Data Load](#initial-data-load)
  - [Population of the Local Registry](#population-of-the-local-registry)
  - [Deceased Check](#deceased-check)
- [Signing On and Opening a Clinical Case Registry](#signing-on-and-opening-a-clinical-case-registry)
- [Registry Window Menus](#registry-window-menus)
  - [File Menu](#file-menu)
    - [File \| Open Registry menu option](#file-open-registry-menu-option)
    - [File \| Save As menu option](#file-save-as-menu-option)
    - [File \| Close and Close All menu options](#file-close-and-close-all-menu-options)
    - [File \| Page Setup, Print Preview, and Print menu options](#file-page-setup-print-preview-and-print-menu-options)
    - [File \| Preferences menu option](#file-preferences-menu-option)
    - [File \| Rejoin Clinical Context menu option](#file-rejoin-clinical-context-menu-option)
    - [File \| Break the Clinical Link menu option](#file-break-the-clinical-link-menu-option)
    - [File \| Exit menu option](#file-exit-menu-option)
  - [Registry Menu](#registry-menu)
    - [Registry \| Confirm/Edit menu option](#registry-confirmedit-menu-option)
    - [Registry \| CDC menu option (CCR:HIV only)](#registry-cdc-menu-option-ccrhiv-only)
    - [Registry \| Show Registry Users menu option](#registry-show-registry-users-menu-option)
    - [Registry \| Edit Site Parameters menu option](#registry-edit-site-parameters-menu-option)
  - [Lab Tests tab](#lab-tests-tab)
  - [Registry Meds tab](#registry-meds-tab)
  - [Notifications tab](#notifications-tab)
  - [Local Fields tab](#local-fields-tab)
  - [Reports Menu](#reports-menu)
    - [Report List Option](#report-list-option)
  - [Window Menu](#window-menu)
  - [Help Menu](#help-menu)
    - [Help \| Help Topics menu option](#help-help-topics-menu-option)
    - [Help \| What’s New menu option](#help-whats-new-menu-option)
    - [Help \| Registry Info menu option](#help-registry-info-menu-option)
    - [Help \| CCOW menu option](#help-ccow-menu-option)
    - [Help \| About CCR menu option](#help-about-ccr-menu-option)
- [Setting Up Site-Specific Parameters](#setting-up-site-specific-parameters)
  - [Adding Lab Tests](#adding-lab-tests)
    - [Adding Lab Tests for Local Registries](#adding-lab-tests-for-local-registries)
  - [Removing Laboratory Tests](#removing-laboratory-tests)
  - [Adding Registry Medications](#adding-registry-medications)
  - [Removing Registry Medications](#removing-registry-medications)
  - [Adding Notifications](#adding-notifications)
  - [Removing Notifications](#removing-notifications)
  - [Adding Local Fields](#adding-local-fields)
  - [Inactivating or Deleting Local Fields](#inactivating-or-deleting-local-fields)
  - [Reactivating Local Fields](#reactivating-local-fields)
  - [Confirming Local Field Changes](#confirming-local-field-changes)
  - [Changing System Default Settings](#changing-system-default-settings)
    - [Changing the Maximum Number of Patients to Retrieve](#changing-the-maximum-number-of-patients-to-retrieve)
    - [Changing the RPC Broker Timeout Parameter](#changing-the-rpc-broker-timeout-parameter)
    - [Changing the Screen Colors and Options](#changing-the-screen-colors-and-options-1)
    - [Restoring Default GUI Settings](#restoring-default-gui-settings)
- [Registry Window Tabs](#registry-window-tabs)
  - [Task Manager tab](#task-manager-tab)
    - [Task column](#task-column)
    - [Type column](#type-column)
    - [Description column](#description-column)
    - [Scheduled column](#scheduled-column)
    - [Status column](#status-column)
    - [Progress column](#progress-column)
    - [Completed column](#completed-column)
    - [Comment column](#comment-column)
    - [Refresh button](#refresh-button)
    - [New Report button](#new-report-button)
    - [Open Report button](#open-report-button)
    - [View Log button](#view-log-button)
    - [Delete button](#delete-button)
    - [Right-Click Menu options](#right-click-menu-options)
  - [Managing Reports from the Task Manager view](#managing-reports-from-the-task-manager-view)
    - [Viewing a Report](#viewing-a-report)
    - [Copying Text from a Report](#copying-text-from-a-report)
    - [Changing the Text Size of a Report](#changing-the-text-size-of-a-report)
    - [Finding Text on a Report](#finding-text-on-a-report)
    - [Sorting/Ordering the Information on a Report](#sortingordering-the-information-on-a-report)
    - [Saving a Report](#saving-a-report)
    - [Exporting a Report to Excel or Access](#exporting-a-report-to-excel-or-access)
    - [Printing a Report](#printing-a-report)
    - [Deleting a Report](#deleting-a-report)
    - [Closing a Report](#closing-a-report)
    - [Technical Log tab](#technical-log-tab)
    - [From: and To: Date fields](#from-and-to-date-fields)
  - [Refresh button](#refresh-button-1)
  - [Types of Logged Activities](#types-of-logged-activities)
  - [Managing Logged Activities from the Technical Log tab](#managing-logged-activities-from-the-technical-log-tab)
  - [Registry tab](#registry-tab)
    - [Note on Pending Patients](#note-on-pending-patients)
    - [Search button](#search-button)
    - [Edit button](#edit-button)
    - [CDC button](#cdc-button)
    - [Delete button](#delete-button-1)
    - [Patient field](#patient-field)
    - [Only Confirmed After checkbox](#only-confirmed-after-checkbox)
    - [Patient List Display](#patient-list-display)
  - [Name column](#name-column)
  - [Date of Birth column](#date-of-birth-column)
  - [Confirmed column](#confirmed-column)
  - [Selection Site column](#selection-site-column)
  - [Selected column](#selected-column)
  - [Selection Rule column](#selection-rule-column)
  - [Using the Registry tab](#using-the-registry-tab)
    - [Searching for Patients](#searching-for-patients)
    - [Deleting a Patient](#deleting-a-patient)
    - [Using the Patient Data Editor Window](#using-the-patient-data-editor-window)
    - [Clinical Status tab](#clinical-status-tab)
    - [Optional Risk Factors tab](#optional-risk-factors-tab)
    - [Local Fields tab](#local-fields-tab-1)
    - [Editing a Patient Record](#editing-a-patient-record)
    - [Deleting a Patient Record](#deleting-a-patient-record)
  - [CDC Window](#cdc-window)
    - [Form tab](#form-tab)
    - [Preview tab](#preview-tab)
    - [Preview (page 2) tab](#preview-page-2-tab)
    - [<u>P</u>rint icon](#upurint-icon)
    - [Print Blank icon](#print-blank-icon)
    - [<u>S</u>ave button](#usuave-button)
    - [Cancel button](#cancel-button)
    - [Zoom <u>I</u>n and Zoom <u>O</u>ut icons](#zoom-uiun-and-zoom-uouut-icons)
    - [Fit <u>W</u>idth icon](#fit-uwuidth-icon)
    - [Zoom <u>1</u>:1 icon](#zoom-u1u1-icon)
    - [AutoFit checkbox](#autofit-checkbox)
    - [Close the CDC form](#close-the-cdc-form)
  - [Viewing a Patient’s CDC Report](#viewing-a-patients-cdc-report)
  - [Printing a Patient’s CDC Report](#printing-a-patients-cdc-report)
  - [Entering Information on a Patient’s CDC Report](#entering-information-on-a-patients-cdc-report)
    - [SECTION I – STATE AND LOCAL USE ONLY](#section-i-state-and-local-use-only)
    - [SECTION II – DATE FORM WAS COMPLETED](#section-ii-date-form-was-completed)
    - [SECTION III – DEMOGRAPHIC INFORMATION](#section-iii-demographic-information)
    - [SECTION IV – FACILITY OF DIAGNOSIS](#section-iv-facility-of-diagnosis)
    - [SECTION V – PATIENT HISTORY](#section-v-patient-history)
    - [SECTION VI – LABORATORY DATA](#section-vi-laboratory-data)
  - [HIV ANTIBODY TESTS AT DIAGNOSIS (Indicate first test):](#hiv-antibody-tests-at-diagnosis-indicate-first-test)
  - [POSITIVE HIV DETECTION TEST (Record earliest test)](#positive-hiv-detection-test-record-earliest-test)
  - [DETECTABLE VIRAL LOAD TEST (record most recent test)](#detectable-viral-load-test-record-most-recent-test)
  - [IMMUNOLOGIC LAB TESTS](#immunologic-lab-tests)
    - [SECTION VII – STATE AND LOCAL USE ONLY](#section-vii-state-and-local-use-only)
    - [SECTION VIII – CLINICAL STATUS](#section-viii-clinical-status)
    - [SECTION IX – TREATMENT/SERVICES REFERRALS (optional)](#section-ix-treatmentservices-referrals-optional)
    - [SECTION X – COMMENTS](#section-x-comments)
- [Registry Reports](#registry-reports)
  - [Registry Reports Window](#registry-reports-window)
    - [Accessing the Registry Reports Window](#accessing-the-registry-reports-window)
  - [Reports Menu](#reports-menu-1)
  - [New Report button and right-click menu option](#new-report-button-and-right-click-menu-option)
    - [Date Range Parameters](#date-range-parameters)
    - [Include Patients Confirmed in the Registry checkboxes](#include-patients-confirmed-in-the-registry-checkboxes)
    - [Other Registries modes](#other-registries-modes)
    - [Load / Save / Default Parameters Buttons](#load-save-default-parameters-buttons)
  - [Generating a Report](#generating-a-report)
    - [Scheduling a Report](#scheduling-a-report)
    - [Discontinuing a Scheduled Report](#discontinuing-a-scheduled-report)
- [Local Reports](#local-reports)
  - [Report Title](#report-title)
  - [Scheduled To Run On Pane](#scheduled-to-run-on-pane)
  - [Include Patients Confirmed in the Registry](#include-patients-confirmed-in-the-registry)
  - [Date Range Pane(s)](#date-range-panes)
  - [Report Elements to Include](#report-elements-to-include)
  - [Utilization Date Range](#utilization-date-range)
  - [Divisions](#divisions)
  - [Clinics](#clinics)
  - [Select Patient](#select-patient)
  - [Other Diagnoses](#other-diagnoses)
  - [Diagnosis Date Range](#diagnosis-date-range)
  - [Report Type (Complete/Summary)](#report-type-completesummary)
  - [BMI Date Range](#bmi-date-range)
  - [BMI Result Ranges](#bmi-result-ranges)
  - [Other Registries](#other-registries)
  - [Local Fields](#local-fields)
  - [Load Parameters](#load-parameters)
  - [Patients](#patients)
    - [Clinic Follow Up Report Patients Pane](#clinic-follow-up-report-patients-pane)
    - [Combined Med Labs Report Patients Pane](#combined-med-labs-report-patients-pane)
    - [Hepatitis A Report Patients Pane](#hepatitis-a-report-patients-pane)
    - [Hepatitis B Report Patients Pane](#hepatitis-b-report-patients-pane)
    - [Procedures Report Patients Pane](#procedures-report-patients-pane)
  - [Vaccination Date Range](#vaccination-date-range)
  - [Immunity Date Range](#immunity-date-range)
  - [Medications Date Range](#medications-date-range)
  - [Medications](#medications)
  - [Lab Tests Date Range](#lab-tests-date-range)
  - [Lab Tests](#lab-tests)
  - [ICD](#icd)
  - [Type of Utilization](#type-of-utilization)
  - [Registry Status](#registry-status)
  - [Report-Specific Options](#report-specific-options)
    - [General Utilization and Demographic Report Options](#general-utilization-and-demographic-report-options)
    - [List of Registry Patients Report Options](#list-of-registry-patients-report-options)
  - [General Report Options](#general-report-options)
    - [Lab Utilization and Radiology Utilization Report Options](#lab-utilization-and-radiology-utilization-report-options)
  - [Liver Score Date Range by Range Report](#liver-score-date-range-by-range-report)
  - [Liver Score Result Ranges](#liver-score-result-ranges)
  - [Activity](#activity)
  - [Refill Type](#refill-type)
  - [Procedures](#procedures)
  - [CPT](#cpt)
  - [Lab Test Group Result](#lab-test-group-result)
  - [Registry Medications – Investigational Drugs](#registry-medications-investigational-drugs)
  - [Renal Function Date Range and Results](#renal-function-date-range-and-results)
  - [Treatment History](#treatment-history)
  - [DAA Start Date Range](#daa-start-date-range)
  - [Lab Tests Date Range Weeks After DAA Start](#lab-tests-date-range-weeks-after-daa-start)
  - [VERA Reimbursement Report Options](#vera-reimbursement-report-options)
  - [Birth Sex](#birth-sex)
  - [Additional Identifiers](#additional-identifiers)
  - [OEF/OIF](#oefoif)
  - [SVR](#svr)
  - [Liver Score Date and Result Ranges](#liver-score-date-and-result-ranges)
  - [DAA Prescriptions](#daa-prescriptions)
  - [Age Range](#age-range)
  - [Future Appointments](#future-appointments)
- [Resources](#resources)
  - [About CCR:HEPC](#about-ccrhepc)
    - [Overview](#overview-1)
    - [Treatment Recommendations](#treatment-recommendations)
    - [Registry Selection Rules](#registry-selection-rules)
    - [About Historic Hepatitis C Case Registry patients](#about-historic-hepatitis-c-case-registry-patients)
  - [About CCR:HIV](#about-ccrhiv)
    - [Overview](#overview-2)
    - [Treatment Recommendations](#treatment-recommendations-1)
    - [Registry Selection Rules](#registry-selection-rules-1)
  - [About Local Registries](#about-local-registries)
    - [Overview](#overview-3)
    - [Local Registry Selection Rules](#local-registry-selection-rules)
  - [CCR:HIV Registry Pending Patient Worksheet](#ccrhiv-registry-pending-patient-worksheet)
  - [Clinical Case Registries Shortcut Keys](#clinical-case-registries-shortcut-keys)
  - [Command Line Switches](#command-line-switches)
- [Troubleshooting](#troubleshooting)

## Clinical Case Registries Software Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Case Registries (CCR) software application supports the maintenance of local and national registries for clinical and resource tracking of care for patients with certain clinical conditions. Registries for [Hepatitis C](#Glos_HepatitisC) (CCR:HEPC) and [Human Immunodeficiency Virus](#Glos_HIV) (CCR:HIV) are available as well as 51 local, generic registries. This application allows access to important demographic and clinical data on all VHA patients with these conditions, and provides many capabilities to VA facilities that provide care and treatment to patients with these conditions, including clinical categorization of patients and automatic transmission of data to the VA's [National Case Registry](#Glos_NCR). It also provides clinical and administrative reports for local medical center use.

CCR accesses several other [Veterans Health Information Systems and Technology Architecture](#Glos_VistA) (VistA) files that contain information regarding other diagnoses, prescriptions, surgical procedures, laboratory tests, radiology exams, patient demographics, hospital admissions, and clinical visits. This access allows identified clinical staff to take advantage of the wealth of data supported through VistA.

## Purpose of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Clinical Case RegistriesUser Manual* provides detailed instructions for using the CCR software and its [graphical user interface](#Glos_GUI) (GUI). Throughout this document, the acronym CCR always refers to the application and its features, not to the individual registries. The HIV and Hepatitis C registries are referred to as CCR:HIV and CCR:HEPC, respectively.

![](ror-1-5-42-user-manual/003.png) See 11.1, About CCR:HEPC and 11.2, About CCR:HIV for registry-specific information.

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCR software is designed for use by designated Registry Coordinators, Managers, and Clinicians who are responsible for and provide care to VA patients with registry-specific conditions.

## Typographical Conventions Used in the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, the following fonts and other conventions are used:

| Font                       | Used for…                                                           | Examples:                                                                        |
|--------------------------------|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| Blue text, underlined          | Hyperlink to another document or URL                                    | [xxx.xxx.xxx.xxx](xxx.xxx.xxx.xxx)                                                   |
| Green text, dotted underlining | Hyperlink within this document                                          | See CCR Patches ROR\*1.5\*X for details.                                             |
| Courier New                    | Patch names, VistA filenames                                            | ROR\*1.5\*2, XYZ file \#798.1                                                        |
| Franklin Gothic Demi           | Keyboard keys, button and command icon names, panel, pane and tab names | \< F1 \>, \< Alt \>, \< L \>, \< Enter \>, \[OK\], Other Registries                  |
| Microsoft Sans Serif           | Software Application names                                              | Clinical Case Registries (CCR)                                                       |
|                                | Registry names                                                          | CCR:HIV                                                                              |
|                                | Database field names                                                    | Mode field                                                                           |
|                                | Report names                                                            | Procedures report                                                                    |
| Times New Roman                | Normal text                                                             | “… designed for use by designated Registry Coordinators, Managers, and Clinicians….” |
| Times New Roman Italic         | Text emphasis                                                           | “It is *very* important…”                                                            |
|                                | National and International Standard names                               | *International Statistical Classification of Diseases and Related Health Problems*   |
|                                | Document names                                                          | *Clinical Case RegistriesUser Manual*                                             |

<span id="_Ref259107385" class="anchor"></span>Table 3 – Patch ROR\*1.5\*1

| Graphic                                                                                                                                                                         | Used for…                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| ![](ror-1-5-42-user-manual/004.png)                                | Information of particular interest regarding the current subject matter                |
| ![](ror-1-5-42-user-manual/005.png)                                               | A tip or additional information that may be helpful to the user                        |
| ![](ror-1-5-42-user-manual/006.png)  | A warning concerning the current subject matter                                        |
| ![](ror-1-5-42-user-manual/007.png)                   | Information about the history of a function or operation; provided for reference only. |
| ![](ror-1-5-42-user-manual/008.png) | More information on a specific subject, either in this document or somewhere else.     |

<span id="_Ref259107375" class="anchor"></span>Table 4 – Patch ROR\*1.5\*2

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These related documents are available at <http://www.va.gov/vdl/application.asp?appid=126>.

- *Clinical Case Registries 1.5 Installation & Implementation Guide*
- *Clinical Case Registries 1.5 Release Notes*
- *Clinical Case Registries 1.5 Technical Manual / Security Guide*

## Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref259107361" class="anchor"></span>Table 5 – Patch ROR*1.5*3</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Disclaimer:</strong> The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref259107361" class="anchor"></span>Table 5 – Patch ROR\*1.5\*3

## Navigating Hyperlinks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this document, you will find hyperlinks of various types like those indicated in Table 1, above. Some will be to other places in this document, while others will take you to websites or other documents stored online. If the hyperlink is to another place in this document, use the web toolbar “back” button (![](ror-1-5-42-user-manual/009.png) ) to return to the point in the document where you clicked the link. If the link is external and takes you to a website, use the back button in your browser to return.

If you do not see the back button in the program you are using to read this document, use your program's View menu to turn on the Web toolbar. For example, in Microsoft® Word® first click <u>V</u>iew, then <u>T</u>oolbars; make sure the Web toolbar is selected.  

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Case Registries (CCR) software application collects data on the population of Veterans with certain clinical conditions, including two national registries for [Hepatitis C](#Glos_HEPC) and [Human Immunodeficiency Virus](#Glos_HIV) (HIV) infections, and 51 generic, local registries.

Data from the registries is used for both clinical and administrative reporting on a local level for the generic registries and a local and national level for Hepatitis C and HIV. Each facility can produce local reports (information related to patients seen in their system). Reports from the national database are used to monitor clinical and administrative trends, including issues related to patient safety, quality of care, and disease evolution across the national population of patients.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Clinical Case Registries (CCR) introduces a single software package to support both the Hepatitis C Registry and the Human Immunodeficiency Virus (HIV) Registry (former Immunology Case Registry or ICR) and the generic registries. Previously, the two national registries were created and maintained through two separate software packages. The functional requirements for these registries were substantially the same, so this software has now been designed to support all registries.

The software uses pre-defined selection rules that identify patients with possible Hepatitis C and/or HIV (such as a disease related [International Statistical Classification of Diseases and Related Health Problems,](#Glos_ICD9) nineth edition ([ICD-9](#Glos_ICD9)) and tenth edition ([ICD-10](#Glos_ICD10)) codes or a positive result on an antibody test) and adds them to the registry.

A nightly background process transmits a set of predefined data via [HL7](#Glos_HL7) to the national CCR database at [Corporate Data Center Operations](#Glos_CDCO) (CDCO).[^1] Data from both registries is aggregated in the same message. The CCR software creates a limited set of database elements to be stored locally in the VistA system, and focuses on assuring that the local listing is complete and accurate, that the desired data elements are extracted, and that data elements are appropriately transmitted to the national database.

| ![](ror-1-5-42-user-manual/010.png) | Note: Effective with CCR 1.5.10 (Patch ROR\*1.5\*10), patients who are on the Pending list *are* selected for this extract. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref259107348" class="anchor"></span>Table 6 – Patch ROR\*1.5\*4

| ![](ror-1-5-42-user-manual/011.png) | Note: Effective with CCR 1.5.13 (Patch ROR\*1.5\*13), the nightly and historical extracts are modified to include ORC and RXE segments for Non-VA medications for registry patients. Non-VA medication data will be pulled if the DOCUMENTED DATE (#11) or the DISCONTINUED DATE (#6) in the NON-VA MEDS sub-file (#52.2) of the PHARMACY PATIENT file (#55) is within the extract range. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref259107335" class="anchor"></span>Table 7 – Patch ROR\*1.5\*5

| ![](ror-1-5-42-user-manual/012.png) | Note: Effective with Patch ROR\*1.5\*14, the extract code pulls Purchased Care Data. New ZIN/ZSV/ZRX segments were added to the HL7 message for this purpose. This change is transparent and seamless to users; no changes in process or method were made. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref259107323" class="anchor"></span>Table 8 – Patch ROR\*1.5\*6

| ![](ror-1-5-42-user-manual/013.png) | Note: Effective with Patch ROR\*1.5\*18, additional local, generic registries were added. These local registries do not transmit back to the national database. This manual refers to “HIV and Hepatitis Registries” frequently. Any functional differentiation between the national HIV/HepC registries and the local, generic registries will be called out, when necessary. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref259107312" class="anchor"></span>Table 9 – Patch ROR\*1.5\*7

<table>
<caption><p><span id="_Ref259107302" class="anchor"></span>Table 10 – Patch ROR*1.5*8</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/014.png)</th>
<th><p>Note:  Effective with Patch ROR*1.5*19, The CCR package now differentiates between ICD-9-CM and ICD-10-CM diagnosis codes in the Data Extraction Process.</p>
<p>The nightly extract continues to extract ICD-9 codes (because of backpulls for new patients where all historical data for the past 20 years is extracted and overlap time) and are able to extract ICD-10 codes from whatever fields have new ICD-10 codes.</p>
<p>The Dates of Interest are specific to the dates of registry-specific diagnosis or lab test results found in the searched files, and are the dates upon which the code set for the extract is based.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref259107302" class="anchor"></span>Table 10 – Patch ROR\*1.5\*8

| ![](ror-1-5-42-user-manual/015.png) | Note: Effective with Patch ROR\*1.5\*26, 2 additional local registries were added (Total Knee Replacement and Total Hip Replacement). These local registries do not transmit back to the national database. This manual refers to “HIV and Hepatitis Registries” frequently. Any functional differentiation between the national HIV/HepC registries and the local, generic registries will be called out, when necessary. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref257981135" class="anchor"></span>Table 11 – Changes for Patch ROR\*1.5\*10

| ![](ror-1-5-42-user-manual/016.png) | Note: Effective with Patch ROR\*1.5\*28, 5 additional local registries were added (Crohn’s Disease, Dementia, Hepatitis B, Thyroid Cancer and Ulcerative Colitis). These local registries do not transmit back to the national database. This manual refers to “HIV and Hepatitis Registries” frequently. Any functional differentiation between the national HIV/HepC registries and the local, generic registries will be called out, when necessary. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref267464954" class="anchor"></span>Table 12 – Changes for Patch ROR\*1.5\*13

| ![](ror-1-5-42-user-manual/017.png) | Note: Effective with Patch ROR\*1.5\*30, 2 additional local registries were added (Hypoparathyroidism and Idiopathic Pulmonary Fibrosis). These local registries do not transmit back to the national database. This manual refers to “HIV and Hepatitis Registries” frequently. Any functional differentiation between the national HIV/HepC registries and the local, generic registries will be called out, when necessary. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref267465276" class="anchor"></span>Table 13 – Global Updates for Patch ROR\*1.5\*13

| ![](ror-1-5-42-user-manual/018.png) | Note: Effective with Patch ROR\*1.5\*31, 2 additional local registries were added (Adrenal Adenoma and Movement Disorders). These local registries do not transmit back to the national database. This manual refers to “HIV and Hepatitis Registries” frequently. Any functional differentiation between the national HIV/HepC registries and the local, generic registries will be called out, when necessary. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc167263952" class="anchor"></span>Table 14 – Changes for Patch ROR\*1.5\*14

| ![](ror-1-5-42-user-manual/019.png) | Note: Effective with Patch ROR\*1.5\*32, 2 additional local registries were added (Frailty and Transgender). These local registries do not transmit back to the national database. This manual refers to “HIV and Hepatitis Registries” frequently. Any functional differentiation between the national HIV/HepC registries and the local, generic registries will be called out, when necessary. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="Table_Global_Updates" class="anchor"></span>Table 15 – Global Updates for Patch ROR\*1.5\*14

| ![](ror-1-5-42-user-manual/020.png) | Note: Effective with Patch ROR\*1.5\*33, 6 additional local registries were added (Transplant Heart, Transplant Intestine, Transplant Kidney, Transplant Liver, Transplant Lung and Transplant Pancreas). These local registries do not transmit back to the national database. This manual refers to “HIV and Hepatitis Registries” frequently. Any functional differentiation between the national HIV/HepC registries and the local, generic registries will be called out, when necessary. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="Table_16" class="anchor"></span>Table 16 – Changes for Patch ROR\*1.5\*15

| ![](ror-1-5-42-user-manual/021.png) | Note: Effective with Patch ROR\*1.5\*34, 3 additional local registries were added (Interstitial Lung Disease, Lymphoma and Non-Alcoholic SteatoHepatitis). These local registries do not transmit back to the national database. This manual refers to “HIV and Hepatitis Registries” frequently. Any functional differentiation between the national HIV/HepC registries and the local, generic registries will be called out, when necessary. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc167263955" class="anchor"></span>Table 17 – Global Updates for Patch ROR\*1.5\*15

| ![](ror-1-5-42-user-manual/022.png) | Note: Effective with Patch ROR\*1.5\*35, patients with HIV and/or Hepatitis C are automatically added to the respective registries and the “pending status” was decommissioned. Two additional local registries were added (Head and Neck Squamous Cell Cancer and Hypothyroidism). These local registries do not transmit back to the national database. This manual refers to “HIV and Hepatitis Registries” frequently. Any functional differentiation between the national HIV/HepC registries and the local, generic registries will be called out, when necessary. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref320706470" class="anchor"></span>Table 18 – Changes for Patch 17

| ![](ror-1-5-42-user-manual/023.png) | Note: Effective with Patch ROR\*1.5\*36, an additional local registry was added (COVID-19). This local registry does not transmit back to the national database. This manual refers to “HIV and Hepatitis Registries” frequently. Any functional differentiation between the national HIV/HepC registries and the local, generic registries will be called out, when necessary. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Toc167263957" class="anchor"></span>Table 19 – Global Updates for Patch ROR\*1.5\*17

| ![](ror-1-5-42-user-manual/024.png) | Note: Effective with Patch ROR\*1.5\*37, an additional local registry was added (Recent Patients). This local registry does not transmit back to the national database. This manual refers to “HIV and Hepatitis Registries” frequently. Any functional differentiation between the national HIV/HepC registries and the local, generic registries will be called out, when necessary. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="_Ref348005671" class="anchor"></span>Table 20 – Changes for Patch 18

The registries at each facility will store selected HIV and Hepatitis C data from 1985 to the present.

## Software Features and Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCR provides these key features:

- Easy data access and navigation of the data files via the GUI.
- Semi-automatic sign-on to the VistA databases via the web-based GUI; a separate VistA log-in is not required, nor is emulation software such as !KEA or Attachmate Reflection.
- Automated development of local lists of patients with evidence of HIV or Hepatitis C infection.
- Automatic transmission of patient data from the local registry lists to a national database.
- Robust reporting capabilities.

CCR also provides the following functions:

- Tracking of patient outcomes relating to treatment.
- Identification and tracking of important trends in treatment response, adverse events, and time on therapy.
- Monitoring quality of care using both process and patient outcome measures.

## About Clinical Case Registries 1.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Version 1.5 of the CCR software (published via Patch ROR\*1.5\*1) introduced a single software package to support both the CCR:HEPC Registry and the CCR:HIV Registry (also called the Immunology Case Registry (ICR)). CCR provides access to both CCR:HIV and CCR:HEPC from a single interface; previously, these two registries were created and maintained through two separate software packages. Since the functional requirements for these registries were substantially the same, they were combined.

CCR 1.5 has also been enhanced by automation of the data collection system and transformed from an administrative database into a clinically relevant tool for patient management.

Each patch released since the original iteration of CCR 1.5 has added improvements and fixes; see CCR Patches ROR\*1.5\*X for details.

CCR consists of several parts:

- Data stored in VistA database files
- [M](#Glos_M) Programs in the ROR namespace
- [Data Dictionaries](#Glos_DD) necessary to achieve the specified requirements
- A [Delphi](#Glos_Delphi)-based [graphical user interface](#Glos_GUI) (GUI) “front-end” application
- Relevant [Remote Procedure Call](#Glos_RPC) (RPC) protocols

## Decommissioned Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Immunology Case Registry v2.1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patients from ICR version 2.1 were migrated to CCR:HIV during the installation of patch ROR\*1\*5 (March 2004). After a transitional period when the two packages were used concurrently, ICR 2.1 was removed from service by patch IMR\*2.1\*21 (October 2005).

## Hepatitis C Case Registry v1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Hepatitis C Case Registry (HCCR) v1.0 was removed from service with the release of CCR 1.5. Historical patient data from the previous Hepatitis C Registry was migrated to CCR:HEPC.

### Automatic Pending Case Identification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patients with laboratory evidence or registry-related [International Statistical Classification of Diseases and Related Health Problems,](#Glos_ICD9) tenth edition (commonly abbreviated as “ICD-10”) codes will be identified by the system and their records will be added to the registry. Previously patients with HIV or Hepatitis C were added to the registry list with a status of “pending.” Effective with Patch 35 (ROR\*1.5\*35), the pending status was decommissioned and patients were automatically added to the respective registries.

CCR users are not permitted to manually enter patient information.

Patients confirmed into the registry can be completely deleted from the registry. For example, if a patient is determined to not actually have the condition (due to a false positive screening test result, etc.), the registry coordinator can delete that patient.

| ![](ror-1-5-42-user-manual/025.png) | Note: See section titled [Note on Pending Patients](#note-on-pending-patients) for more information. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|

<span id="_Ref331507206" class="anchor"></span>Table 21 – Global Updates for Patch ROR\*1.5\*18

### ‘Local Fields’ For Customizing Local Registry Specific Data 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the CCR GUI for both the HIV and Hepatitis C registries, users with administrator [keys](#Glos_SecurityKeys) will be able to define data collection attributes and assign names to them. These local fields will serve as manual toggles in the Patient Data Editor and as filters that can be used in the report selection panels. Titles and descriptions of local fields can be edited as free text fields without deleting all associated information.

### CCR Procedures Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Procedures report allows you to select multiple CPT codes to produce a report that will list all patients who had the selected CPT codes in a selected date range.

### Optional Entry of Risk Behavior 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/026.png) HIV Risk Factors. Effective with Patch 14, completion of the Risk Factors tab questions in the Patient Data Editor regarding HIV risk behavior is optional.

## CCR Patches ROR\*1.5\*X

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes provided by patches in the ROR\*1.5 series are shown in the following tables. Under “Type,” “E” indicates an enhancement, “F” indicates a fix, and “M” indicates a data modification. Click on the green links below to jump directly to a specific patch.

| [Patch ROR\*1.5\*1](#patch-ror1.51)                          |                                                              | [Patch ROR\*1.5\*2](#patch-ror1.52)                         |                                       |                                       | [Patch ROR\*1.5\*3](#patch-ror1.53) | [Patch ROR\*1.5\*4](#patch-ror1.54)   | [Patch ROR\*1.5\*5](#patch-ror1.55)   | [Patch ROR\*1.5\*6](#patch-ror1.56)   | [Patch ROR\*1.5\*7](#patch-ror1.57)   |
|--------------------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------|---------------------------------------|---------------------------------------|-------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|---------------------------------------|
| [Patch ROR\*1.5\*8](#patch-ror1.58)                          |                                                              | (Patch ROR\*1\*9: maintenance patch; not documented herein) |                                       |                                       |                                     | [Patch ROR\*1.5\*10](#patch-ror1.510) | [Patch ROR\*1.5\*13](#patch-ror1.513) | [Patch ROR\*1.5\*14](#patch-ror1.514) | [Patch ROR\*1.5\*15](#patch-ror1.515) |
| (Patch ROR\*1\*16: maintenance patch; not documented herein) |                                                              |                                                             | [Patch ROR\*1.5\*17](#patch-ror1.517) |                                       |                                     | [Patch ROR\*1.5\*18](#patch-ror1.518) | [Patch ROR\*1.5\*19](#patch-ror1.519) | [Patch ROR\*1.5\*20](#patch-ror1.520) | [Patch ROR\*1.5\*21](#patch-ror1.521) |
| [Patch ROR\*1.5\*22](#patch-ror1.522)                        | (Patch ROR\*1\*23: maintenance patch; not documented herein) |                                                             |                                       |                                       |                                     | [Patch ROR\*1.5\*24](#patch-ror1.524) | [Patch ROR\*1.5\*27](#patch-ror1.527) | [Patch ROR\*1.5\*25](#patch-ror1.525) | [Patch ROR\*1.5\*26](#patch-ror1.526) |
| [Patch ROR\*1.5\*28](#patch-ror1.528)                        | [Patch ROR\*1.5\*29](#patch-ror1.529)                        |                                                             |                                       | [Patch ROR\*1.5\*30](#patch-ror1.530) |                                     | [Patch ROR\*1.5\*31](#patch-ror1.531) | [Patch ROR\*1.5\*32](#patch-ror1.532) | [Patch ROR\*1.5\*33](#patch-ror1.533) | [Patch ROR\*1.5\*34](#patch-ror1.534) |
| [Patch ROR\*1.5\*35](#patch-ror1.535)                        | [Patch ROR\*1.5\*36](#patch-ror1.536)                        |                                                             |                                       | [Patch ROR\*1.5\*37](#patch-ror1.537) |                                     | [Patch ROR\*1.5\*38](#patch-ror1.538) | [Patch ROR\*1.5\*39](#patch-ror1.539) | [Patch ROR\*1.5\*40](#patch-ror1.540) | [Patch ROR\*1.5\*41](#patch-ror1.541) |
| [Patch ROR\*1.5\*42](#patch-ror1.542)                        |                                                              |                                                             |                                       |                                       |                                     |                                       |                                       |                                       |                                       |

<span id="_Ref348005730" class="anchor"></span>Table 22 – Changes for Patch 20

### Patch ROR\*1.5\*1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                                                                                                                                                                                        | Type |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| 1   | Selected (Date) and Selection Rule columns added to the patient list on the Registry tab.                                                                                                                                                          | E    |
| 2   | When a report is opened, the Task Manager tab is activated.                                                                                                                                                                                        | E    |
| 3   | The Mode field is added to the Local Fields and Other Registries panels of the Report parameters to provide patient *include* and *exclude* filters.                                                                                               | E    |
| 4   | A Delete button is added to the Patient Data Editor dialog box.                                                                                                                                                                                    | E    |
| 5   | A Patients panel is added to the Procedures report to use selected procedures performed and selected procedures not performed within a date range.                                                                                                 | E    |
| 6   | A Procedures panel is added to the Procedures report to indicate whether a procedure is an inpatient or outpatient one                                                                                                                             | E    |
| 7   | The ICD-9 panel of the Diagnoses report is modified to be able to define groups and add ICD-9 codes to the groups.                                                                                                                                 | E    |
| 8   | The Check if patient ever had an AIDS-OI checkbox is automatically selected and the Date of AIDS-OI field is populated if an indicator disease Def box is selected in Section VIII of the CDC form in the Clinical Status section.                 | E    |
| 9   | A new patient search parameter is added for the Registry tab: \# followed by the patient’s 11-digit coded SSN.                                                                                                                                     | E    |
| 10  | The output format of the Combined Meds and Labs report is modified.                                                                                                                                                                                | E    |
| 11  | The Patient Medication History report is modified with the addition of two radio buttons, Consider All and Selected Only to the Select Patient panel.                                                                                              | E    |
| 12  | The Date of Death column has been removed from the Current Inpatient List report (it was redundant).                                                                                                                                               | E    |
| 13  | Fixed Microsoft® Windows Server 2003® issue.                                                                                                                                                                                                       | F    |
| 14  | Fixed missing CDC bitmap error.                                                                                                                                                                                                                    | F    |
| 15  | Fixed incorrect printing of the CDC form.                                                                                                                                                                                                          | F    |
| 16  | Increased the time out values.                                                                                                                                                                                                                     | F    |
| 17  | The GUI code was amended to allow a maximum number of patients to retrieve to 65535.                                                                                                                                                               | F    |
| 18  | The RORTSK10 and RORTSK11 routines have been amended to store original values and encode them on the fly when report is loaded by the GUI, to allow for storing special characters.                                                                | F    |
| 19  | The RORLOCK routine has been amended to display the user name locking records.                                                                                                                                                                     | F    |
| 20  | Typographical errors in the comment lines have been fixed in the , RORLOCK, RORX003, RORX003A, and RORX007A routines.                                                                                                                              | F    |
| 21  | Direct access to the PRESCRIPTION file (#52) has been replaced with the corresponding APIs. The following routines have been modified: RORHL03, RORHL031, and RORHL07.                                                                             | M    |
| 22  | Direct access to the PHARMACY PATIENT file (#55) has been replaced with the corresponding APIs. The following routines have been modified: RORHL03, RORHL07, RORHL071, and RORHL15.                                                                | M    |
| 23  | Comments in the source code of the following routines (mostly, the lists of integration agreements) have been updated: RORHL01, RORHL05, RORHL06, RORHL07, RORHL08, RORHL09, RORHL10, RORHL11, RORHL12, RORRP015, RORUTL05,RORX005A, and RORXU006. | M    |
| 24  | The 42600-7 LOINC code has been added to the VA HIV Lab search criteria in the ROR LAB SEARCH file.                                                                                                                                                | M    |
| 25  | DARUNAVIR, EFAVIRENZ/EMTRICITABINE/TENOFOVIR, and TIPRANAVIR have been added to the list of HIV generic drugs in the ROR GENERIC DRUG file (#799.51)                                                                                               | M    |
|     | Installation routines used by the ROR 1.5 KIDS build (RORP000, RORP000A and RORP00B) have been deleted.                                                                                                                                            |      |

<span id="_Toc167263961" class="anchor"></span>Table 23 – Global Updates for Patch ROR\*1.5\*20

### Patch ROR\*1.5\*2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                              | Type |
|-----|------------------------------------------------------------------------------------------|------|
| 1   | Fixed RPC Broker timeout issue.                                                          | F    |
| 2   | Fixed issues with duplicates in patient list.                                            | F    |
| 3   | Fixed issues with lower-case characters in lab tests and medications data.               | F    |
| 4   | Fixed issue with Reporting date entry not accepting “-T.”                                | F    |
| 5   | Fixed issue with un-checking of local fields in the Patient Data Editor not being saved. | F    |
| 6   | Fixed issues with run-time errors using \$QUERY on non-Caché platforms.                  | F    |
| 7   | Fixed issues with non-SSN patient identifier appearing on reports at non-VA sites.       | F    |

<span id="_Ref403740377" class="anchor"></span>Table 24 – Changes for Patch 19

### Patch ROR\*1.5\*3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                               | Type |
|-----|-------------------------------------------------------------------------------------------|------|
| 1   | Accommodated Patch RA\*5\*75 (Radiology), which introduced a Reason for Study data field. | E    |
| 2   | Addition of Task Control flag (“M”) which signals the system to disable HL7 messaging.    | E    |

<span id="_Toc167263963" class="anchor"></span>Table 25 – Global Updates for Patch ROR\*1.5\*19

### Patch ROR\*1.5\*4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                                      | Type |
|-----|--------------------------------------------------------------------------------------------------|------|
| 1   | Added two additional ICD-9 codes needed for the nightly ROR registry update and data extraction. | E    |

<span id="_Ref379354454" class="anchor"></span>Table 26 – Changes for Patch 21

### Patch ROR\*1.5\*5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                          | Type |
|-----|--------------------------------------------------------------------------------------|------|
| 1   | Fixed issue with Procedures without a Provider not being sent to AAC.                | F    |
| 2   | Added drug identified as needed for nightly ROR registry update and data extraction. | E    |

<span id="_Toc167263965" class="anchor"></span>Table 27 – Global Updates for Patch ROR\*1.5\*21

### Patch ROR\*1.5\*6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                               | Type |
|-----|-----------------------------------------------------------|------|
| 1   | Added generic drug RALTEGRAVIR to VA GENERIC file \#50.6. | E    |

<span id="_Ref395527788" class="anchor"></span>Table 28 – Changes for Patch 22

### Patch ROR\*1.5\*7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                              | Type |
|-----|----------------------------------------------------------|------|
| 1   | Added generic drug ETRAVIRINE to VA GENERIC file \#50.6. | E    |

<span id="_Toc167263967" class="anchor"></span>Table 29 – Global Updates for Patch ROR\*1.5\*22

### Patch ROR\*1.5\*8

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref384131049" class="anchor"></span>Table 30 – Changes for Patch 24</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 84%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th>Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Fixed the “access violation” seen when selecting Diagnoses Report (Remedy Tickets HD0000000262208 and HD0000000262209).</td>
<td>F</td>
</tr>
<tr class="even">
<td>2</td>
<td>Inserted a Comment Field in the Pending Patient File necessary for tracking special conditions for a patient.</td>
<td>E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Added the Comments panel to the Patient Data Editor screen (see 2 above).</td>
<td>E</td>
</tr>
<tr class="even">
<td>4</td>
<td>Added the Comment field to Processing Pending Patient screen (see 2 above).</td>
<td>E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Added a refresh to the Processing Pending Patient screen when comment is added or deleted (see 2 above).</td>
<td>E</td>
</tr>
<tr class="even">
<td>6</td>
<td>Added radio buttons “Include,” “Exclude,” or “Ignore” to provide a filter limiting reports to patients who have diagnoses based on International Classification of Diseases, 9th edition (ICD-9) codes in Common Templates or Your Templates. This filter applies to all reports except the Diagnoses Report.</td>
<td>E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Modified the Combined Meds and Labs report to require the user to assign a group name.</td>
<td>E</td>
</tr>
<tr class="even">
<td>8</td>
<td>Modified the Combined Meds and Labs report to provide the option to limit lab results to most recent.</td>
<td>F</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Modified the Combined Meds and Labs report to "Include All" or "Selected Only" for lab results (Remedy Ticket HD0000000232223).</td>
<td>E</td>
</tr>
<tr class="even">
<td rowspan="2">10</td>
<td rowspan="2">Modified the Combined Meds and Labs report, Pharmacy Prescription Utilization report, and the Patient Medication History report to include a new method of handling Investigational Drugs and Registry Medications on the <strong>Medications panel</strong> drop-down list.</td>
<td rowspan="2">E</td>
</tr>
<tr class="odd">
</tr>
<tr class="even">
<td>11</td>
<td><p>Technical Writer review included these updates:</p>
<ol type="1">
<li><p>Changes the sort order of entries in this table to show most recent changes at top.</p></li>
<li><p>To comply with National Documentation Standards, pagination of introductory material has been revised and minor format changes have been made to headings, table headings and footers.</p></li>
<li><p>Provides numbered section/paragraph headings.</p></li>
<li><p>Moves “what’s new” information for all patches to new section: CCR Patches ROR*1.5*X.</p></li>
<li><p>Adopts use of <a href="#ROR158_TW_Review">green dotted-underline text</a> for hyperlinks internal to this document.</p></li>
<li><p>Adds information about the Remote Procedure Call Broker.</p></li>
<li><p>Expands information on typographical conventions and notes/warnings icons.</p></li>
<li><p>Substitutes new pointer diagram for “fuzzy” image previously used.</p></li>
<li><p>Removes references to “other registries;” the HIV and HEPC registries are the only ones within the current scope of CCR.</p></li>
<li><p>Adopts use of the term “command icon” to denote dedicated areas on menu bars which can be clicked to perform functions similar to those performed by command buttons.</p></li>
<li><p>Changes the date associated with the FDA-approved list of generic medicines which are contained in the Generic Registry Medications list from November 2005 to June, 2008.</p></li>
<li><p>Substituted VistA logo for internal CCR logo on cover to meet OED Documentation Standards requirement.</p></li>
</ol></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Ref384131049" class="anchor"></span>Table 30 – Changes for Patch 24

### Patch ROR\*1.5\*10

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc167263969" class="anchor"></span>Table 31 – Global Updates for Patch ROR*1.5*24</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 31%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="5">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="6">1</td>
<td colspan="5">Adds new ICD-9 diagnosis groups to the Common Templates:</td>
<td rowspan="6">M</td>
</tr>
<tr class="even">
<td colspan="3">HCC</td>
<td>155.0</td>
<td>MAL NEO LIVER, PRIMARY</td>
</tr>
<tr class="odd">
<td colspan="3" rowspan="4">Esophageal Varices</td>
<td>456.0</td>
<td>ESOPHAG VARICES W BLEED</td>
</tr>
<tr class="even">
<td>456.1</td>
<td>ESOPH VARICES W/O BLEED</td>
</tr>
<tr class="odd">
<td>456.20</td>
<td>BLEED ESOPH VAR OTH DIS</td>
</tr>
<tr class="even">
<td>456.21</td>
<td>ESOPH VARICE OTH DIS NOS</td>
</tr>
<tr class="odd">
<td rowspan="16">2a</td>
<td colspan="5">Adds LOINC codes to CCR:HIV Patient ID:</td>
<td rowspan="16">M</td>
</tr>
<tr class="even">
<td><strong>LOINC_NUM</strong></td>
<td><strong>SHORTNAME</strong></td>
<td colspan="3"><strong>LONG_COMMON_NAME</strong></td>
</tr>
<tr class="odd">
<td>34591-8</td>
<td>HIV1 Ab Fld Ql EIA</td>
<td colspan="3">HIV 1 Ab [Presence] in Body fluid by Immunoassay</td>
</tr>
<tr class="even">
<td>34592-6</td>
<td>HIV1 Ab Fld Ql IB</td>
<td colspan="3">HIV 1 Ab [Presence] in Body fluid by Immunoblot (IB)</td>
</tr>
<tr class="odd">
<td>43009-0</td>
<td>HIV1+2 IgG Ser Ql</td>
<td colspan="3">HIV 1+2 IgG Ab [Presence] in Serum</td>
</tr>
<tr class="even">
<td>43010-8</td>
<td>HIV1+2 Ab XXX Ql</td>
<td colspan="3">HIV 1+2 Ab [Presence] in Unspecified specimen</td>
</tr>
<tr class="odd">
<td>43185-8</td>
<td>HIV 1 &amp; 2 Ab Patrn Ser IB-Imp</td>
<td colspan="3">HIV 1 &amp; 2 Ab band pattern [interpretation] in Serum by Immunoblot (IB)</td>
</tr>
<tr class="even">
<td>43599-0</td>
<td>HIV1 Ab Ser IF-aCnc</td>
<td colspan="3">HIV 1 Ab [Units/volume] in Serum by Immunofluorescence</td>
</tr>
<tr class="odd">
<td>44533-8</td>
<td>HIV1+2 Ab Ser Donr Ql</td>
<td colspan="3">HIV 1+2 Ab [Presence] in Serum from donor</td>
</tr>
<tr class="even">
<td>44607-0</td>
<td>HIV1 Ser EIA-Imp</td>
<td colspan="3">HIV 1 [interpretation] in Serum by Immunoassay</td>
</tr>
<tr class="odd">
<td>44873-8</td>
<td>HIV1+2 Ab Ser Ql IB</td>
<td colspan="3">HIV 1+2 Ab [Presence] in Serum by Immunoblot (IB)</td>
</tr>
<tr class="even">
<td>49580-4</td>
<td>HIV1+2 Ab XXX Ql Rapid</td>
<td colspan="3">HIV 1+2 Ab [Presence] in Unspecified specimen by Rapid test</td>
</tr>
<tr class="odd">
<td>49905-3</td>
<td>HIV1 Ab XXX Ql Rapid</td>
<td colspan="3">HIV 1 Ab [Presence] in Unspecified specimen by Rapid test</td>
</tr>
<tr class="even">
<td>5221-7</td>
<td>HIV1 Ab Ser Ql IB</td>
<td colspan="3">HIV 1 Ab [Presence] in Serum by Immunoblot (IB)</td>
</tr>
<tr class="odd">
<td>53379-4</td>
<td>HIV1 Ab XXX Ql</td>
<td colspan="3">HIV 1 Ab [Presence] in Unspecified specimen</td>
</tr>
<tr class="even">
<td>54086-4</td>
<td>HIV1+2 IgG Bld.Dot Ql</td>
<td colspan="3">HIV 1+2 IgG Ab [Presence] in Blood dot (filter paper)</td>
</tr>
<tr class="odd">
<td rowspan="7">2b</td>
<td colspan="5">Adds LOINC Codes to CCR:HEPC Patient ID:</td>
<td rowspan="7">M</td>
</tr>
<tr class="even">
<td><strong>LOINC NUM</strong></td>
<td><strong>SHORTNAME</strong></td>
<td colspan="3"><strong>LONG_COMMON_NAME</strong></td>
</tr>
<tr class="odd">
<td>47365-2</td>
<td>HCV Ab Ser Donr Ql EIA</td>
<td colspan="3">Hepatitis C virus Ab [Presence] in Serum from donor by Immunoassay</td>
</tr>
<tr class="even">
<td>47441-1</td>
<td>HCV Ab Ser Donr Ql</td>
<td colspan="3">Hepatitis C virus Ab [Presence] in Serum from donor</td>
</tr>
<tr class="odd">
<td>48576-3</td>
<td>HCV RNA XXX Ql bDNA</td>
<td colspan="3">Hepatitis C virus RNA [Presence] in Unspecified specimen by Probe &amp; signal amplification method</td>
</tr>
<tr class="even">
<td>51655-9</td>
<td>HCV RNA Fld Ql PCR</td>
<td colspan="3">Hepatitis C virus RNA [Presence] in Body fluid by Probe &amp; target amplification method</td>
</tr>
<tr class="odd">
<td>51657-5</td>
<td>HCV Ab Fld Ql</td>
<td colspan="3">Hepatitis C virus Ab [Presence] in Body fluid</td>
</tr>
<tr class="even">
<td>3</td>
<td colspan="5"><p>Updates (by changing date selection criteria) the Microbiology data extraction code to capture missing Microbiology data. Extract now uses “completion date” and/or “date collected.”</p>
<p><em>Prior to this patch, the Microbiology data extraction was pulling data based on the 'completion date' (DATE REPORT COMPLETED, #.03 in the MICROBIOLOGY sub-file #63.05 of the LAB DATA file #63) alone. It was found that many sites do not populate that field, causing microbiology data to be omitted from the nightly extract to the central registry. The extract will now pull data based on the 'date collected' (DATE/TIMESPECIMEN TAKEN, #.01) if the 'completion date' is null.</em></p></td>
<td>E</td>
</tr>
<tr class="odd">
<td>4</td>
<td colspan="5"><p>Corrects Problem List Extraction by using DATE RESOLVED versus DATE RECORDED.</p>
<p><em>Previously, the Problem List Extraction was pulling data from the wrong field (DATE RECORDED, #1.09) to populate the 'date resolved' field in the extract. Data is now correctly pulled from the DATE RESOLVED field (#1.07) of the PROBLEM file (#9000011).</em></p></td>
<td>F</td>
</tr>
<tr class="even">
<td>5</td>
<td colspan="5"><p>Adds new OBR and OBX segments to the nightly extract to pull Immunization data and Skin Test data for Registry patients (see <em>CCR Technical Manual</em>).</p>
<p><em>The nightly and historical extracts have been enhanced to include OBR and OBX segments for Immunization data and Skin Test data for registry patients. Immunization data and Skin Test data will be pulled if the DATE LAST MODIFIED (#.13 in the VISIT file (#9000010) is within the extract range. For details of the data included in the segments, please refer to the CCR Technical Manual.</em></p></td>
<td>E</td>
</tr>
<tr class="odd">
<td>6</td>
<td colspan="5"><p>Changes nightly data extract to include patients on the Pending list.</p>
<p><em>The CCR data extract (both nightly and historical) previously included data for 'confirmed' patients only. It will now include data for 'pending' patients as well. Previously, the DON'T SEND field (#11) in the ROR REGISTRY RECORD file (#798) was set to 'true' when a pending patient was added to the registry. With patch 10, the DON'T SEND field will be set to 'true' for test patients only.</em></p></td>
<td>E</td>
</tr>
<tr class="even">
<td rowspan="5">7</td>
<td colspan="5">Adds three new reports:</td>
<td rowspan="5">E</td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>Model for End-Stage Liver Disease (MELD) Score by Range</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>Body Mass Index (BMI) by Range</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>Renal Function by Range</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><em>These reports can be executed from the GUI application. See the User Manual for additional report information.</em></td>
</tr>
<tr class="odd">
<td>8</td>
<td colspan="5">Modifies existing report headers to reflect the Other Diagnosis filter (added by ROR*1.5*8)</td>
<td>E</td>
</tr>
<tr class="even">
<td>9</td>
<td colspan="5">Adds ALL REGISTRY MEDICATIONS to the <strong>Medications Selection panel</strong> via a new <strong>[ All Registry Meds]</strong> button. This is included in the Combined Meds and Labs, Patient Medication History, and Pharmacy Prescription Utilization reports.</td>
<td>E</td>
</tr>
<tr class="odd">
<td>10</td>
<td colspan="5"><p>Adds new checkbox to display Pending Comments on the List of Registry Patients report.</p>
<p><em>The "List of Registry Patients" report has been enhanced to include a "Pending Comments" column added to the Report Options. If this option is checked, an additional column called Pending Comments will be added as the right-most column of the report. If the Registry Status' Pending check box is not checked, the Pending Comments option will be disabled.</em></p></td>
<td>E</td>
</tr>
<tr class="even">
<td>11</td>
<td colspan="5"><p>Replaces Direct global and FileMan reads to the International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM) files with calls using supported Application Program Interfaces (APIs).</p>
<p><em>To support encapsulation of data in the ICD-9-CM package, direct global and FileMan reads previously used in the ROR namespace were replaced with calls using supported ICD-9-CM APIs. These supported APIs retrieve Diagnosis information needed by the CCR application for the extracts and reports.</em></p></td>
<td>E</td>
</tr>
<tr class="odd">
<td>12</td>
<td colspan="5"><p>Modifies Other Diagnosis filter to allow the user to remove group header from the “selected” box when the user removes a group from the “selected” panel.</p>
<p><em>If the user highlights the header and presses the delete key, the header will be deleted. In addition, if the user highlights the header and hits the left arrow, the header will be deleted. Previously, the header was not being removed from the selected box.</em></p>
<p><em>Reports with the 'Other Diagnoses' filter have been modified to display the selected diagnoses in the report header. One of the three formats shown below will be displayed on the report, depending on what the user selected.</em></p>
<p><em>Diagnoses: All</em></p>
<p><em>Diagnoses: Include abc, def, etc.</em></p>
<p><em>Diagnoses: Exclude abc, def, etc.</em></p></td>
<td>M</td>
</tr>
<tr class="even">
<td>13</td>
<td colspan="5">Modifies the “Help About” popup to conform to VA standards, including hyperlinks to reference documents.</td>
<td>E</td>
</tr>
<tr class="odd">
<td>14</td>
<td colspan="5">Modifies the online help file to make it <a href="#Glos_CSH">context-sensitive</a>.</td>
<td>E</td>
</tr>
<tr class="even">
<td>15</td>
<td colspan="5">Updates the GUI application to work toward adherence to the <a href="#Glos_508">Section 508</a> standards.</td>
<td>M</td>
</tr>
<tr class="odd">
<td>16</td>
<td colspan="5">Reports XML code have been updated to address a bug introduced in Internet Explorer 7 that was causing page breaks to not work correctly.</td>
<td>F</td>
</tr>
</tbody>
</table>

<span id="_Toc167263969" class="anchor"></span>Table 31 – Global Updates for Patch ROR\*1.5\*24

### Patch ROR\*1.5\*13

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                                                                                                                                                                                                                                                                                                                    | Type |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| 1   | Adds LOINC code 57006 to the VA HEPC entry of the Lab Search criteria in the ROR LAB SEARCH file (#798.9), sub-file LAB TEST (#2).                                                                                                                                                                                                                                             | M    |
| 2   | Enhances the nightly and historical HL7 extracts to include ORC and RXE segments for Non-VA medications for registry patients. Non-VA medication data will be pulled if the DOCUMENTED DATE (#11) or the DISCONTINUED DATE (#6) in the NON-VA MEDS sub-file (#52.2) of the PHARMACY PATIENT file (#55) is within the extract range.                                            | E    |
| 3   | Enhances the Patient Medication History report to allow users to select the most recent fill only, or all fills. The report output has been enhanced to include a column displaying the number of fills remaining.                                                                                                                                                             | E    |
| 4   | Reports BMI by Range, MELD Score by Range, and Renal Function by Range have been enhanced to allow users to sort the report output by the calculations. The BMI by Range report can be sorted by the BMI score. The MELD Score by Range report can be sorted by the MELD or the MELD-Na score. The Renal Function by Range report can be sorted by the CrCL or the eGFR score. | E    |
| 5   | All reports (except Outpatient Utilization, Inpatient Utilization, List of Registry Patients, and Current Inpatient List) will allow users to select specific clinics or divisions. All reports (except List of Registry Patients and Current Inpatient List) will allow users to select specific patients.                                                                    | E    |
| 6   | When users want to select specific medications in the Combined Meds And Labs report, the Patient Medication History report, or the Pharmacy Prescription Utilization report, the text in the search box will automatically convert to uppercase.                                                                                                                               | E    |
| 7   | The CCR GUI application will now check VistA for the CCR server version, and it will display a message if the CCR GUI and the CCR server version are out of sync with each other.                                                                                                                                                                                              | E    |
| 8   | The CCR GUI was updated to work towards becoming fully compliant with the [Section 508](#Glos_508) standards and initiatives.                                                                                                                                                                                                                                                  | F    |
| 9   | An historical data extraction for Non-VA meds is added to the ROR HISTORICAL DATA EXTRACTION file (#799.6). It will automatically execute during the next nightly extract, and there is no manual intervention required by the sites. The extraction date range for this historical data extraction is 1/1/1985 through current date (installation date).                      | E    |
| 10  | Global updates as indicated in Table 13.                                                                                                                                                                                                                                                                                                                                       | E    |

<span id="_Ref413242888" class="anchor"></span>Table 32 – Changes for Patch 27

<table>
<caption><p><span id="_Toc167263971" class="anchor"></span>Table 33 – Global Updates for Patch ROR*1.5*27</p></caption>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name and Number</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR LAB SEARCH (#798.9)</td>
<td>LOINC value 57006 is added to the VA HEPC Lab Search criteria in sub-file LAB TEST (#2).</td>
</tr>
<tr class="even">
<td>ROR DATA AREA (#799.33)</td>
<td>New entry “Non-VA Meds” is added to the file.</td>
</tr>
<tr class="odd">
<td>ROR XML ITEM (#799.31)</td>
<td>New entries “REFILLS”, “ALL_FILLS”, and “RECENT_FILLS” are added to the file.</td>
</tr>
<tr class="even">
<td>ROR REPORT PARAMETERS (#799.34)</td>
<td><p><em>Entries modified:</em></p>
<p>General Utilization and Demographics</p>
<p>Clinic Follow Up</p>
<p>Inpatient Utilization</p>
<p>Lab Utilization</p>
<p>Radiology Utilization</p>
<p>Pharmacy Prescription Utilization</p>
<p>Registry Lab Tests by Range</p>
<p>Patient Medication History</p>
<p>Combined Meds and Labs</p>
<p>Diagnoses</p>
<p>Registry Medications</p>
<p>Procedures</p>
<p>Outpatient Utilization</p>
<p>VERA Reimbursement Report</p>
<p>BMI by Range</p>
<p>MELD Score by Range</p>
<p>Renal Function by Range</p></td>
</tr>
<tr class="odd">
<td>DIALOG (#.84)</td>
<td><p><em>Entries modified:</em></p>
<p>7981011.001 Patient Medication History (HTML)</p>
<p>7981011.002 Patient Medication History (CSV)</p>
<p>7981018.001 BMI Report by Range (HTML)</p>
<p>7981018.002 BMI Report by Range (CSV)</p>
<p>7981019.001 MELD Report by Range (HTML)</p>
<p>7981019.002 MELD Report by Range (CSV)</p>
<p>7981020.001 Renal Function by Range (HTML)</p>
<p>7981020.002 Renal Function by Range (CSV)</p>
<p>7981999.001 Common XSL templates (HTML)</p></td>
</tr>
<tr class="even">
<td>REMOTE PROCEDURE (#8994)</td>
<td>New entry “ROR GET M VERSION” is added to the file. This RPC is used to determine whether the CCR GUI application version is in sync with the last CCR M patch installed.</td>
</tr>
<tr class="odd">
<td>OPTION (#19)</td>
<td>The RPC “ROR GET M VERSION” is added to the RPC list for the existing ROR GUI entry.</td>
</tr>
<tr class="even">
<td>ROR HISTORICAL DATA EXTRACTION (#799.6)</td>
<td>Entry “NON-VA MEDS” is added to the file.</td>
</tr>
</tbody>
</table>

<span id="_Toc167263971" class="anchor"></span>Table 33 – Global Updates for Patch ROR\*1.5\*27

### Patch ROR\*1.5\*14

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                                                                                                                                                                                                                                                                            |     | Type |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | The 13 risk factors for the HIV registry have been changed from mandatory to optional.                                                                                                                                                                                                                                                 | E   |      |
| 2   | Currently, within the Patient Data Editor in the HIV registry, the user is prompted to click a checkbox if the patient "ever had an AIDS OI." This prompt and checkbox has been replaced with the question "Did the patient ever have an AIDS OI?" and the option to select either Yes, No, or Unknown has been added to the checkbox. | E   |      |
| 3   | The following mandatory question has been added to the Patient Data Editor: "Was your VHA facility/station the first health care setting (VA or non-VA) to diagnose HIV?" along with a checkbox to select either Yes, No or Unknown.                                                                                                   | E   |      |
| 4   | A new column has been added to the List of Registry Patients Report that allows the user to select "Diagnosed at this Facility". This column indicates whether this facility was the first health care setting (VA or Non-VA) to diagnose HIV.                                                                                         | E   |      |
| 5   | The nightly extract has been enhanced to include Purchased Care data for registry patients.                                                                                                                                                                                                                                            | E   |      |
| 6   | The "MELD Score by Range" report has been renamed to "Liver Score By Range".                                                                                                                                                                                                                                                           | E   |      |
| 7   | The "Liver Score by Range" report now includes the list of LOINC codes used in the report.                                                                                                                                                                                                                                             | E   |      |
| 8   | The "Renal Score by Range" report now includes the list of LOINC codes used in the report.                                                                                                                                                                                                                                             | E   |      |
| 9   | The "Liver Score by Range" report now includes APRI and FIB-4 calculations.                                                                                                                                                                                                                                                            | E   |      |
| 10  | Patients will be automatically confirmed into the HEPC Registry if they have a positive Hepatitis C Virus (HCV) viral load test result.                                                                                                                                                                                                | E   |      |
| 11  | This patch brings the Clinical Case Registries (CCR) application into 508 compliance in many areas.                                                                                                                                                                                                                                    | E   |      |
| 12  | An historical data extraction for Purchased Care is added to the ROR HISTORICAL DATA EXTRACTION file (#799.6) for automatic execution during the next nightly extract.                                                                                                                                                                 | E   |      |
| 13  | Global updates as indicated in [Table 15](#Table_Global_Updates).                                                                                                                                                                                                                                                                      |     |      |

<span id="_Ref406404119" class="anchor"></span>Table 34 – Changes for Patch 25

<table>
<caption><p><span id="_Toc167263973" class="anchor"></span>Table 35 – Global Updates for Patch ROR*1.5*25</p></caption>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name and Number</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR LAB SEARCH (#798.9)</td>
<td><p>HCV Viremic LOINC values are added to the VA HEPC Lab Search criteria in sub-file LAB TEST (#2):</p>
<p>11011</p>
<p>29609</p>
<p>34703</p>
<p>34704</p>
<p>10676</p>
<p>20416</p>
<p>20571</p>
<p>49758</p>
<p>50023</p></td>
</tr>
<tr class="even">
<td>ROR XML ITEM (#799.31)</td>
<td>New entries "FIRSTDIAG" , "LOINC_CODES","APRI", and "FIB4" are added to the file.</td>
</tr>
<tr class="odd">
<td>ROR DATA AREA (#799.33)</td>
<td>New entry “Purchased Care” is added to the file.</td>
</tr>
<tr class="even">
<td>DIALOG (#.84)</td>
<td><p>7981001.001 List of Registry Patients (HTML)</p>
<p>7981019.001 Liver Report by Range (HTML)</p>
<p>7981019.002 Liver Report by Range (CSV)</p>
<p>7981020.001 Renal Function by Range (HTML)</p>
<p>7981997.001 Patient data Templates (HTML)</p></td>
</tr>
<tr class="odd">
<td>ROR HIV Record (#799.4)</td>
<td><p>1. New field HIV DX: FIRST DIAGNOSED HERE (#12.08) is added to the file.</p>
<p>2. The CLINICAL AIDS field (#.02) is updated to include the value of "UNKNOWN" in the set of codes.</p></td>
</tr>
<tr class="even">
<td>ROR HISTORICAL DATA EXTRACTION (#799.6)</td>
<td>Entry “PURCHASED CARE” is added to the file.</td>
</tr>
</tbody>
</table>

<span id="_Toc167263973" class="anchor"></span>Table 35 – Global Updates for Patch ROR\*1.5\*25

### Patch ROR\*1.5\*15

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                                                                                                                                                                                                                                                                                                                                                                             |     | Type |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | Three new HCV generic Drugs, Telaprevir, Boceprevir and Rilpivirine were approved by the FDA in May, 2011. These three medications have been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medications.                                                                                                                              | E   |      |
| 2   | The Renal Function by Range Report has been enhanced to include a new option for calculating the eGFR called the CKD-EPI equation. The CKD-EPI GFR is an estimate of glomerular filtration (GFR) using serum creatinine and demographic factors. It is a relatively new equation that is believed to be superior to the MDRD GFR equation. If selected, the CKD-EPI scores are summarized on the report by chronic kidney disease stage | E   |      |
| 3   | The result ranges panel on the Renal Function by Range report will include a note that reads, "Lab tests used to calculate renal function are identified by LOINC code. Your local lab ADPAC should be contacted regarding errors in LOINC codes."                                                                                                                                                                                      | M   |      |
| 4   | The header on the Renal Function by Range report currently reads, "Lab tests used to calculate Cockcroft-Gault and/or eGFR by MDRD scores are identified by LOINC code." This text will be updated to read, "Lab tests used in calculations are identified by LOINC code."                                                                                                                                                              | M   |      |
| 5   | The cover sheet text of the Renal Function by Range report will be amended to include the list of LOINC codes that are used. The new text on the Renal Function by Range report will read, "Lab tests used to calculate scores are identified by LOINC code. Your local lab ADPAC should be contacted regarding errors in LOINC codes."                                                                                                 | E   |      |
| 6   | The Liver Score by Range report has been modified to display only those tests used in the calculation of the liver scores selected by the user If the user selects the APRI and/or FIB4 tests, then the Bili, Cr, INR, and Na rows should not appear on the report. If the user selects the MELD and/or MELDNA tests, then the AST, Platelet, and ALT rows should not appear on the report.                                             | M   |      |
| 7   | The result ranges panel on the Liver Score by Range report will include a note that reads, "Lab tests used in calculations are identified by LOINC code. Your local lab ADPAC should be contacted regarding errors in LOINC codes."                                                                                                                                                                                                     | M   |      |
| 8   | Users may now use Diagnosed at this VA as a local field. This is a CCR:HIV only option.                                                                                                                                                                                                                                                                                                                                                 | E   |      |
| 9   | Users may now type ?? or click the All Divisions button to display all Divisions in the left-hand pick box.                                                                                                                                                                                                                                                                                                                         | E   |      |
| 10  | The CDC Form has been modified to correct the transposition of check box values for the Bisexual male and Intravenous/injection drug user questions.                                                                                                                                                                                                                                                                                    | F   |      |
| 11  | The CDC Form has been modified to check the appropriate checkbox if the user selects 'yes' to the question Received Clotting Factor for Hemophilia/Coagulation disorder.                                                                                                                                                                                                                                                                | F   |      |
| 12  | An invalid date check and error message have been added for the question, Received transfusion of blood/blood components (other than clotting factor) on the Risk Factors tab in the Patient Editor.                                                                                                                                                                                                                                | E   |      |
| 13  | A future date check and error message have been added for the question, Received transfusion of blood/blood components (other than clotting factor) on the Risk Factors tab in the Patient Editor.                                                                                                                                                                                                                                  | E   |      |
| 14  | A future date check and error message have been added for the question, Did the patient ever have an AIDS OI? on the Clinical Status in the Patient Editor.                                                                                                                                                                                                                                                                         | E   |      |
| 15  | An historical data extraction for Non-VA Meds has been added to the ROR HISTORICAL DATA EXTRACTION file (#799.6) for automatic execution during the next nightly extract.                                                                                                                                                                                                                                                               | E   |      |
| 16  | The Date Range panels (Date Range, Medications Date Range, Lab Tests Date Range and Utilization Date Range) were re-designed for easier use with Assistive Technology.                                                                                                                                                                                                                                                  | M   |      |

<span id="_Ref419454734" class="anchor"></span>Table 36 – Changes for Patch 26

<table>
<caption><p><span id="_Toc167263975" class="anchor"></span>Table 37 – Global Updates for Patch ROR*1.5*26</p></caption>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name and Number</th>
<th>Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR LIST ITEM (#799.1)</td>
<td>New entries "eGFR by CKD-EPI," "eGFR by CKD-EPI"</td>
</tr>
<tr class="even">
<td>ROR XML ITEM (#799.31)</td>
<td>New entries "HIV_DX, " "MDRD," "CKD," "NPMDRD" and "NPCKD" are added to the file.</td>
</tr>
<tr class="odd">
<td>ROR GENERIC DRUG (#799.51)</td>
<td>New entries "Telaprevir," "Rilpivirine," "Boceprevir"</td>
</tr>
<tr class="even">
<td>DIALOG (#.84)</td>
<td><p>7981020.001 Renal Function by Range (HTML)</p>
<p>7981020.002 Renal Function by Range (CSV)</p>
<p>7981998.001 CSS and Scripts</p></td>
</tr>
<tr class="odd">
<td>ROR HISTORICAL DATA EXTRACTION (#799.6)</td>
<td>Entry “NON-VA MEDS” is added to the file.</td>
</tr>
</tbody>
</table>

<span id="_Toc167263975" class="anchor"></span>Table 37 – Global Updates for Patch ROR\*1.5\*26

### Patch ROR\*1.5\*17

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc167263976" class="anchor"></span>Table 38 – Changes for Patch 28</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>A new HIV generic drug, EMTRICI./RILPIVIRINE/TENOFOVIR (Complera) was approved by the Food and Drug Administration (FDA). This new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients taking the new medication.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>The List of Registry Patients report has been enhanced to allow users to specify an Only Confirmed After date. If the user selects this feature, the Pending box will be disabled. This will allow users to generate a list of recently confirmed patients that have been added to the registry after a specific date.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>A new diagnosis group, Post Traumatic Stress Disorder (PTSD), has been added to the common templates. The ICD code for PTSD is 309.81.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>Lab test selection on the Lab Utilization report, the Combined Meds and Labs report, the DAA Lab Monitoring report and the Edit Site Parameters option in the GUI has been changed to be case insensitive. For example, if a user enters "zinc" as a search criterion, all test names for "zinc" will be returned regardless of the case of the test name in file #60 (e.g. zinc, Zinc, ZINC, zINC, etc.). This problem was reported in Remedy ticket #215842.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>The text on the Result Ranges panel and the report header of the Liver</p>
<p>Score by Range report have been modified to provide additional instruction.</p></td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>6</td>
<td>The text on the Result Ranges panel and the report header of the Renal Function by Range report have been modified to provide additional instruction.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>7</td>
<td>A new HepC report, Potential DAA Candidates, has been added to identify patients who may be eligible for the new HepC Direct Acting Anti-Viral(DAA) medications. The user may request a list of HepC patients with treatment histories of 'naive' and/or 'experienced'. Patients who are 'naive' have never taken any registry medications. Patients who are 'experienced' have not received DAA medications but have taken other registry medications. The user may choose to exclude experienced patients who have fills for other registry medications within a specified number of days.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>8</td>
<td>A new HepC report, DAA Lab Monitoring, has been added to monitor laboratory results for patients who have taken DAAs. The user may display the two most recent test results prior to the first DAA fill date as well as selected lab test results for X weeks after the first DAA fill date. The user may also restrict the lab test results after the first DAA fill date to be the most recent. Any registry medications for the patient filled 60 days before the first DAA fill date through today display automatically on the report.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>9</td>
<td>The preview and printing of the CDC form has been modified to correct the transposition of check box values for the risk factors, Bisexual male and the Intravenous/injection drug user.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>10</td>
<td>An installation problem with the CCR help file referenced in Remedy ticket #233500 is corrected.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>11</td>
<td>This patch brings the Clinical Case Registries (CCR) application into 508 compliance in many areas.</td>
<td colspan="2">F</td>
</tr>
</tbody>
</table>

<span id="_Toc167263976" class="anchor"></span>Table 38 – Changes for Patch 28

<table>
<caption><p><span id="_Toc167263977" class="anchor"></span>Table 39 – Global Updates for Patch ROR*1.5*28</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR LIST ITEM (#799.1)</td>
<td>New entries “HCV”, “HCV_DATE”, “STATUS, GT”, “FILL_MED”, “NAIVE”, “EXP”, “EXP_DAYS”, “TREATMENT_HISTORY”, “FILL_DATE”, “DATE_RANGE_4”, “WEEKS_AFTER”, “DAA_FILL”, “WKS_LAB”, “CONFDT_AFTER”, “CONFIRM_AFTER”</td>
</tr>
<tr class="even">
<td>ROR REPORT PARAMETERS (#799.34)</td>
<td>New entries “Potential DAA Candidates”, “DAA Lab Monitoring”, “Pharmacy Prescription Utilization”</td>
</tr>
<tr class="odd">
<td>ROR GENERIC DRUG (#799.51)</td>
<td>New entries “EMTRICI./RILPIVIRINE/TENOFOVIR”</td>
</tr>
<tr class="even">
<td>DIALOG (#.84)</td>
<td><p>7980000.018 Report options</p>
<p>7981019.001 Liver Report by Range (HTML)</p>
<p>7981020.001 Renal Function by Range (HTML)</p>
<p>7981021.001 Potential DAA Candidates (HTML)</p>
<p>7981021.002 Potential DAA Candidates (CSV)</p>
<p>7981022.001 DAA Lab Monitoring (HTML)</p>
<p>7981022.002 DAA Lab Monitoring (CSV)</p>
<p>7981995.001 Lab data templates (HTML)</p>
<p>7981998.001 CSS and Scripts</p>
<p>7981999.001 Common XSL templates (HTML)</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167263977" class="anchor"></span>Table 39 – Global Updates for Patch ROR\*1.5\*28

### Patch ROR\*1.5\*18

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref491453222" class="anchor"></span>Table 40 – Changes for Patch 29</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch is designed to allow reporting tools used with the national Hepatitis C and HIV registries to be used with local registries. Sixteen new local registries are added based on ICD9 codes provided by the national Office of Public Health/Population Health. The new registries represent patient diagnostic groups for:</p>
<ul>
<li><p>Alzheimer's Disease</p></li>
<li><p>Amputation</p></li>
<li><p>Breast Cancer</p></li>
<li><p>Cerebrovascular Disease (CVD)</p></li>
<li><p>Chronic Obstructive Pulmonary Disease (COPD)</p></li>
<li><p>Chronic Renal Disease (CRD)</p></li>
<li><p>Congestive Heart Failure (CHF)</p></li>
<li><p>Diabetes</p></li>
<li><p>Dyslipidemia</p></li>
<li><p>Hypertension</p></li>
<li><p>Ischemic Heart Disease (IHD)</p></li>
<li><p>Low Vision/Blind</p></li>
<li><p>Mental Health</p></li>
<li><p>Osteoarthritis</p></li>
<li><p>Multiple Sclerosis</p></li>
<li><p>Rheumatoid Arthritis</p></li>
</ul></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>An option, Initialize new registries (one time) is provided to schedule the initial build of the new registries. The option is locked with the ROR VA IRM security key. It is run one time and will search for patients with qualifying ICD9 codes linked to outpatient visits, problem lists and inpatient stays back to 1/1/1985. Patients added to a local registry are automatically confirmed. The confirmation date is set to the earliest date of the qualifying ICD9 code. Registries are not available to users until they are initialized.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Once the registries are initialized, the nightly job (ROR TASK) searches for new patients with qualifying ICD9 codes. Patients added to one of the 16 local registries are automatically confirmed. The confirmation date is set to the date of the qualifying ICD code.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>Only data from the national registries for HIV and Hepatitis C will be transmitted to the national database.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>Two new security keys have been added, ROR VA GENERIC ADMIN and ROR VA GENERIC USER. These keys only provide access to the local registries. Users assigned the new ROR VA GENERIC ADMIN key will have the ability to delete patients from any of the sixteen local registries. Patients are deleted immediately and the deletion is logged in the technical log. If the patient has a future qualifying result, the patient is added back to the appropriate registry.</p>
<p>Users with the ROR VA GENERIC USER key will have the ability to run</p>
<p>reports on all the local registries.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td>It will no longer be necessary to run the option, Re-index the ACL cross-reference manually after assigning or un-assigning a security key. The user's access privileges will be automatically updated at the time the user logs on.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>7</td>
<td>The Select a Registry screen displayed when the user logs on, will list all the registries to which the user has keys. The national registries for Hepatitis C and HIV will be listed first. The local registries will be listed next in alphabetical order separated from the national registries by a blank line.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>8</td>
<td>The Patient screen for local registries does not include a Pending only checkbox or a Pending Comments column because patients added to local registries are automatically confirmed.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>9</td>
<td><p>Site parameters can be customized for local registries. The site parameters screen displays tabs for Lab Tests, Notifications and Local Fields. A generic tab on the right side of the screen displays laboratory tests. Select local laboratory tests under the Registry Lab tab and move them to the right. Once a laboratory test is added, it is displayed in the middle pane of the Registry Lab Patient Data Editor.</p>
<p>The names of VistA users who need to receive notifications about problems in registry processes can be added under the Notifications tab.</p>
<p>Local fields can also be added to individual local registries. These fields are used to include/exclude patients from reports.</p></td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>The following reports can be run for local registries:</p>
<ul>
<li><p>BMI by Range Report</p></li>
<li><p>Clinic Follow Up Report</p></li>
<li><p>Combined Meds and Labs Report</p></li>
<li><p>Current Inpatient List Report</p></li>
<li><p>Diagnosis Report</p></li>
<li><p>General Utilization and Demographics Report</p></li>
<li><p>Procedures Report</p></li>
<li><p>Radiology Utilization Report</p></li>
<li><p>Inpatient Utilization Report</p></li>
<li><p>Lab Utilization Report</p></li>
<li><p>Liver Score by Range Report</p></li>
<li><p>Outpatient Utilization Report</p></li>
<li><p>Patient Medication History Report</p></li>
<li><p>Pharmacy Prescription Utilization Report</p></li>
<li><p>Renal Function by Range Report</p></li>
</ul></td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>11</td>
<td>The List of Registry Patients can be run for local registries but has been modified for use with local registries. The Pending checkbox has been removed from the Report Status panel. Pending comments and First diagnosed at this facility checkboxes have been removed from the Report Options panel.</td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>12</td>
<td><p>The following reports are not supported for local registries:</p>
<ul>
<li><p>Registry Lab Tests by Range Report</p></li>
<li><p>DAA Lab Monitoring Report</p></li>
<li><p>Potential DAA Candidates Report</p></li>
<li><p>Registry Medications Report</p></li>
<li><p>VERA Reimbursement Report</p></li>
</ul></td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>13</td>
<td>If the user has keys for the registries, the Other Registries selection panel will display those registries. Registries listed in this panel can be used to include/exclude patients on reports.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>14</td>
<td>The Common Template for Depression has been deleted and replaced with two new Common Templates for Major Depression and Other Depression. These templates are used to filter patients based on diagnoses when running reports.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>15</td>
<td>ROR TASK has been modified to automatically update all registries. It is no longer necessary to list registries in the TASK PARAMETERS field. The description of the option has been modified to reflect this change.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>16</td>
<td>The Select Patient panel has been added to the DAA Lab Monitoring report.</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref491453222" class="anchor"></span>Table 40 – Changes for Patch 29

<table>
<caption><p><span id="_Toc167263979" class="anchor"></span>Table 41 – Global Updates for Patch ROR*1.5*29</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR REGISTRY PARAMETERS(#798.1)</td>
<td>New entries “VA DIABETES”, “VA MENTAL HEALTH”, “VA CHF”, “VA IHD”, “VA BREAST CA”, “VA HTN”, “VA CVD”, “VA OSTEOARTHRITIS”, “VA COPD”, “VA DYSLIPIDEMIA”, “VA CRD”, “VA ALZHEIMERS”, “VA RHEUM”, “VA AMPUTATION”, “VA BLIND”, “VA MULTIPLE SCLEROSIS.</td>
</tr>
<tr class="even">
<td>ROR SELECTION RULE(#798.2)</td>
<td><p>New entries “VA ALZHEIMERS PROBLEM”, VA ALZHEIMERS PTF”, “VA ALZHEIMERS VPOV”, “VA AMPUTATION PROBLEM”, “VA AMPUTATION PTF”, “VA AMPUTATION VPOV”, “VA BLIND PROBLEM”, “VA BLIND PTF”, “VA BLIND VPOV”, “VA BREAST CA PROBLEM”, “VA BREAST CA PTF”, “VA BREAST CA VPOV”, “VA CHF PTF”, “VA CHF PROBLEM”, VA CHF VPOV”, “VA COPD PROBLEM”, “VA COPD PTF”, “VA COPD VPOV”, “VA CRD PROBLEM”, “VA CRD PTF”, “VA CRD VPOV”, “VA CVD PROBLEM”, “VA CVD PTF”, “VA CVD VPOV”, “VA DIABETES PROBLEM”, “VA DIABETES PTF”, “VA DIABETES VPOV”, “VA DYSLIPIDEMIA PROBLEM”, “VA DYSLIPIDEMIA PTF”, “VA DYSLIPIDEMIA VPOV”, “VA HTN PROBLEM”, “VA HTN PTF”, “VA HTN VPOV”, “VA IHD PROBLEM”, “VA IHD PTF”, “VA IHD VPOV”, “VA MENTAL HEALTH PROBLEM”, “VA MENTAL HEALTH PTF”, “VA MENTAL HEALTH VPOV”, “VA MULTIPLE SCLEROSIS PROBLEM”, “VA MULTIPLE SCLEROSIS PTF”, “VA MULTIPLE SCLEROSIS VPOV”, “VA OSTEOARTHRITIS PROBLEM”, “VA OSTEOARTHRITIS PTF”, “VA OSTEOARTHRITIS VPOV”, “VA RHEUM PROBLEM”, “VA RHEUM PTF”, “VA RHEUM VPOV”,</p>
<p>Modified entries “VA HEPC PROBLEM”, “VA HEPC PTF”, “VA HEPC VPOV”, “VA HIV PROBLEM”, “VA HIV PTF”, “VA HIV VPOV”</p></td>
</tr>
<tr class="odd">
<td>ROR ICD SEARCH (#798.5)</td>
<td>New entries “VA DIABETES”, “VA MENTAL HEALTH”,“VA CHF”,“VA IHD”,“VA BREAST CA”,“VA HTN”,“VA CVD”,“VA OSTEOARTHRITIS”,“VA COPD”,“VA DYSLIPIDEMIA”,“VA CRD”,“VA ALZHEIMERS”,“VA RHEUM”,“VA AMPUTATION”,“VA BLIND”,“VA MULTIPLE SCLEROSIS”</td>
</tr>
<tr class="even">
<td>ROR LIST ITEM(#799.1)</td>
<td>New entries “BMI”,“MELD”,“MELD-Na”, “APRI”, “FIB-4”, “Creatinine clearance by Cockcroft-Gault”, “eGFR by MDRD”, “eGFR by CKD-EPI”</td>
</tr>
<tr class="odd">
<td>ROR METADATA (#799.2)</td>
<td>Modified entries “45”, “9000010.07”, “9000011”</td>
</tr>
<tr class="even">
<td>PARAMETERS (#8989.5)</td>
<td><p>New Entries “Other Depression”, “Major Depression”</p>
<p>Deleted Entries “Depression”</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167263979" class="anchor"></span>Table 41 – Global Updates for Patch ROR\*1.5\*29

### Patch ROR\*1.5\*20

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref491453306" class="anchor"></span>Table 42 – Changes for Patch 30</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch adds the following medication:</p>
<ul>
<li><p>VA Product: COBICISTAT/ELVITEGRAVIR/EMTRICITABINE/TENOFOVIR DF TAB, ORAL, 23233</p></li>
<li><p>VA Generic: COBICISTAT/ELVITEGRAVIR/EMTRICITABINE/TENOFOVIR, 4753</p></li>
</ul>
<ol type="1">
<li><p>VA Product: COBICISTAT/ELVITEGRAVIR/EMTRICITABINE/TENOFOVIR DFTAB,ORAL</p></li>
<li><p>VA Generic Name: COBICISTAT/ELVITEGRAVIR/EMTRICITABINE/TENOFOVIR</p></li>
<li><blockquote>
<p>Dosage Form: TAB,<br />
ORAL</p>
</blockquote></li>
<li><blockquote>
<p>Strength: (5)<br />
Units:</p>
</blockquote></li>
<li><p>Nat' Formulary Name: COBICISTAT/ELVITEGRAVIR/EMTRICITABINE/TENOFOVIR TAB,ORAL</p></li>
<li><blockquote>
<p>VA Print Name: STRIBILD ORAL TAB</p>
</blockquote></li>
<li><p>VA Product Identifier: C1522</p></li>
<li><p>Transmit to CMOP: Yes</p></li>
<li><p>VA Dispense Unit: TAB</p></li>
</ol></td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref491453306" class="anchor"></span>Table 42 – Changes for Patch 30

<table>
<caption><p><span id="_Toc167263981" class="anchor"></span>Table 43 – Global Updates for Patch ROR*1.5*30</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>ROR GENERIC DRUG file</p>
<p>(#799.51)</p></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc167263981" class="anchor"></span>Table 43 – Global Updates for Patch ROR\*1.5\*30

### Patch ROR\*1.5\*19

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref448302953" class="anchor"></span>Table 44 – Changes for Patch 31</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>Registry update process allows the Reason for Selection</p>
<p>for a patient added to a Registry to include ICD-10 code in outpatient</p>
<p>file, ICD-10 code in inpatient file, or ICD-10 code in Problem List.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>ICD-10 diagnoses and ICD-10 procedure codes can be searched for in the</p>
<p>Report parameters.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>ICD-10 diagnoses codes can be saved in Your Templates along with</p>
<p>ICD-9 diagnoses codes.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>Common Templates are updated to include ICD-10 codes. Note:</p>
<p>Pre-install routine saves the current Common Templates in ^TMP("ROR",$J)</p>
<p>global before updating them with ICD-9 and ICD-10 codes. Any changes done</p>
<p>to Common Templates will be lost after the installation of this patch.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Reports show ICD-10 diagnoses and procedure codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>CCR Registry information that is sent to the National Database via HL7</p>
<p>messages now differentiates between ICD-9 and ICD-10 diagnosis codes.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>The CCR PD team released CCR Patch ROR*1.5*17 on June 18, 2012, which added the new PTSD Common Template and two new HEPC reports.</td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>8</td>
<td>The CCR PD team released CCR Patch ROR*1.5*18, which includes the minimal technical code and data dictionary changes for 16 new registries. The changes have been absorbed into ROR*1.5*19 so that both patches may co-exist.</td>
<td colspan="2">M</td>
</tr>
</tbody>
</table>

<span id="_Ref448302953" class="anchor"></span>Table 44 – Changes for Patch 31

<table>
<caption><p><span id="_Toc167263983" class="anchor"></span>Table 45 – Global Updates for Patch ROR*1.5*31</p></caption>
<colgroup>
<col style="width: 55%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR SELECTION RULE file (#798.2)</td>
<td><p>CODING SYSTEM field (#7)</p>
<p>VA HIV PROBLEM</p>
<p>VA HIV PROBLEM (ICD10)</p>
<p>VA HIV PTF</p>
<p>VA HIV PTF (ICD10)</p>
<p>VA HIV VPOV</p>
<p>VA HIV VPOV (ICD10)</p>
<p>VA HEPC PROBLEM</p>
<p>VA HEPC PROBLEM (ICD10)</p>
<p>VA HEPC PTF</p>
<p>VA HEPC PTF (ICD10)</p>
<p>VA HEPC VPOV</p>
<p>VA HEPC VPOV (ICD10)</p></td>
</tr>
<tr class="even">
<td>ROR REGISTRY PARAMETERS file (#798.1)</td>
<td><p>VA HIV</p>
<p>VA HEPC</p></td>
</tr>
<tr class="odd">
<td>ROR REPORT PARAMETERS file (#799.34)</td>
<td><p>Entries:</p>
<p>Diagnoses (#13)</p>
<p>Procedures (#15)</p></td>
</tr>
<tr class="even">
<td>ROR XML ITEM file (#799.1)</td>
<td><p>ICD</p>
<p>ICD10</p>
<p>ICDFILT</p>
<p>ICDLST</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167263983" class="anchor"></span>Table 45 – Global Updates for Patch ROR\*1.5\*31

### Patch ROR\*1.5\*21

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref514740506" class="anchor"></span>Table 46 – Changes for Patch 32</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch adds the following medication:</p>
<ul>
<li><p>VA Product: DOLUTEGRAVIR</p></li>
<li><p>VA Generic: DOLUTEGRAVIR</p></li>
</ul>
<p>This new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>A new local registry, Obstructive Sleep Apnea (VA APNEA), was added based on ICD9 codes provided by the  national Office of Public Health/Population Health. </td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>An additional selection panel titled "Sex" will be created.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>An additional selection panel titled "Additional Identifier" will be created.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>To  facilitate off-line record matching, patient ICN will be added to all reports, except the Current Inpatient List.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td>The "Utilization Date Range" selection panel will be added to the Diagnosis Report in order to provide sites with the ability to run reports that limit output to patients with utilization within a specific date range.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>Report enhancement for screen on gender.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>8</td>
<td>Report enhancement for addition of optional ICN column.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>9</td>
<td>The nightly HL7 message will be updated to also include the number of reports run in all of the local registries including the new Obstructive Sleep Apnea Registry.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>10</td>
<td><p>This patch brings the Clinical Case Registries (CCR) application into</p>
<p>508 compliance in many areas.</p></td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref514740506" class="anchor"></span>Table 46 – Changes for Patch 32

<table>
<caption><p><span id="_Toc167263985" class="anchor"></span>Table 47 – Global Updates for Patch ROR*1.5*32</p></caption>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR REGISTRY PARAMETERS(#798.1)</td>
<td>New entry “VA APNEA”</td>
</tr>
<tr class="even">
<td>ROR SELECTION RULE(#798.2)</td>
<td>New entries “VA APNEA PROBLEM”, “VA APNEA PTF”, “VA APNEA VPOV”, “VA APNEA PROBLEM (ICD10)”, “VA APNEA PTF (ICD10)”, “VA APNEA VPOV (ICD10)”</td>
</tr>
<tr class="odd">
<td>ROR ICD SEARCH (#798.5)</td>
<td>New entry “VA APNEA”</td>
</tr>
<tr class="even">
<td>ROR XML ITEM(#799.31)</td>
<td>New entries “MALE”, “FEMALE”</td>
</tr>
<tr class="odd">
<td><p>ROR GENERIC DRUG file</p>
<p>(#799.51)</p></td>
<td>Add DOLUTEGRAVIR</td>
</tr>
</tbody>
</table>

<span id="_Toc167263985" class="anchor"></span>Table 47 – Global Updates for Patch ROR\*1.5\*32

### Patch ROR\*1.5\*22

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref20138964" class="anchor"></span>Table 48 – Changes for Patch 33</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch adds the following medication:</p>
<ul>
<li><p>VA Product: SIMEPREVIR</p></li>
<li><p>VA Generic: SIMEPREVIR</p></li>
<li><p>VA Product: SOFOSBUVIR</p></li>
<li><p>VA Generic: SOFOSBUVIR</p></li>
</ul>
<p>These new medications have been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking these new medications.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>An additional selection panel titled "OEF/OIF" will be created in the CCR GUI to allow selection of report content by a check for patient's OEF/OIF service status.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Report enhancements for screen on OEF/OIF/OND period of service, including updating the ROR REPORT PARAMETERS file (#799.34), field PARAMETER PANELS field (#1) to include the new panel '25' for OEF/OIF/OND.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>All local registries will be updated with the appropriate International Classification of Diseases, Tenth Revision (ICD-10) codes for compliance with national mandates.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>A modification was made to the RULE NAME field (#.01) in the ROR SELECTION RULE file (#798.2). The length of the field was increased from 30 to 40 characters.</td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>6</td>
<td>A modification was made to the SELECTION RULE field (#.01), of the SELECTION RULE field (#3) (subfile #798.13) of the ROR REGISTRY PARAMETERS file (#798.1). The length of the field was increased from 30 to 40 characters.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>7</td>
<td>The system will now notify a mail group if the nightly job [ROR TASK] does not run due to the initiating user no longer possessing the ROR VA IRM security key.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>8</td>
<td><p>This patch brings the Clinical Case Registries (CCR) application into</p>
<p>508 compliance in many areas.</p></td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref20138964" class="anchor"></span>Table 48 – Changes for Patch 33

<table>
<caption><p><span id="_Toc167263987" class="anchor"></span>Table 49 – Global Updates for Patch ROR*1.5*33</p></caption>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR ICD SEARCH file (#798.5)</td>
<td>Add appropriate new ICD-10 codes for each local registry in the ICD CODE subfield (#1).  Refer to the technical documentation for the specific codes assigned to each registry.</td>
</tr>
<tr class="even">
<td>ROR REPORT PARAMETERS file (#799.34)</td>
<td>Add panel ‘25’ for OEF/OIF/OND to the PARAMETER PANELS (#1) field for all reports.</td>
</tr>
<tr class="odd">
<td><p>ROR GENERIC DRUG file</p>
<p>(#799.51)</p></td>
<td>Add SIMEPREVIR and SOFOSBUVIR</td>
</tr>
</tbody>
</table>

<span id="_Toc167263987" class="anchor"></span>Table 49 – Global Updates for Patch ROR\*1.5\*33

### Patch ROR\*1.5\*24

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref20138862" class="anchor"></span>Table 50 – Changes for Patch 34</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>Eight new local registries were added based on ICD9 codes provided by the  national Office of Public Health/Population Health. </p>
<p>Osteoporosis (VA OSTEOPOROSIS), Prostate Cancer (VA PROSTATE CANCER), Lung Cancer (VA LUNG CANCER), Melanoma (VA MELANOMA), Colorectal Cancer (VA COLORECTAL CANCER), Pancreatic Cancer (VA COLORECTAL CANCER), Hepatocellular Carcinoma (VA HCC), ALS (VA ALS)</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>Removal of the requirement that a Hepatitis C GT lab test must be specified in the site parameters before the Potential DAA Candidates report can be run.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Addition of new HIV antibody and antigen codes to the VA HIV registry.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>Addition of new LOINC codes to the Hepatitis C registry antibody search.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>A new Hepatitis C report, Sustained Virologic Response, has been added to identify patients who have had a SVR after treatment with HepC antiviral medications.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td>A modification was made to copy CCR application help files to the local workstation when CCR is accessed on a server or network.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>7</td>
<td><p>This patch brings the Clinical Case Registries (CCR) application into</p>
<p>508 compliance in many areas.</p></td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref20138862" class="anchor"></span>Table 50 – Changes for Patch 34

<table>
<caption><p><span id="_Toc167263989" class="anchor"></span>Table 51 – Global Updates for Patch ROR*1.5*34</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR REGISTRY PARAMETERS(#798.1)</td>
<td><p>New entries “VA OSTEOPOROSIS”, “VA PROSTATE CANCER”, “VA LUNG CANCER”, “VA MELANOMA”, “VA COLORECTAL CANCER”, “VA PANCREATIC CANCER”, “VA HCC”, “VA ALS”.</p>
<p>Modified entry “VA HEPC”</p></td>
</tr>
<tr class="even">
<td>ROR SELECTION RULE(#798.2)</td>
<td><p>New entries “VA OSTEOPOROSIS PROBLEM”, “VA OSTEOPOROSIS PTF”, “VA OSTEOPOROSIS VPOV”, “VA OSTEOPOROSIS PROBLEM (ICD10)”, “VA OSTEOPOROSIS PTF (ICD10)”, “VA OSTEOPOROSIS VPOV (ICD10)”, “VA PROSTATE CANCER PROBLEM”, “VA PROSTATE CANCER PTF”, “VA PROSTATE CANCER VPOV”,</p>
<p>“VA PROSTATE CANCER PROBLEM (ICD10)”, “VA PROSTATE CANCER PTF (ICD10)”, “VA PROSTATE CANCER VPOV (ICD10)”, “VA LUNG CANCER PROBLEM”, “VA LUNG CANCER PTF”, “VA LUNG CANCER VPOV”, “VA LUNG CANCER PROBLEM (ICD10)”, “VA LUNG CANCER PTF (ICD10)”, “VA LUNG CANCER VPOV (ICD10)”, “VA MELANOMA PROBLEM”, “VA MELANOMA PTF”, “VA MELANOMA VPOV”, “VA MELANOMA PROBLEM (ICD10)”, “VA MELANOMA PTF (ICD10)”, “VA MELANOMA VPOV (ICD10)”, “VA COLORECTAL CANCER PROBLEM”, “VA COLORECTAL CANCER PTF”, “VA COLORECTAL CANCER VPOV”, “VA COLORECTAL CANCER PROBLEM (ICD10)”, “VA COLORECTAL CANCER PTF (ICD10)”, “VA COLORECTAL CANCER VPOV (ICD10)”, “VA PANCREATIC CANCER PROBLEM”, “VA PANCREATIC CANCER PTF”, “VA PANCREATIC CANCER VPOV”, “VA PANCREATIC CANCER PROBLEM (ICD10)”, “VA PANCREATIC CANCER PTF (ICD10)”, “VA PANCREATIC CANCER VPOV (ICD10)”, “VA HCC PROBLEM”, “VA HCC PTF”, “VA HCC VPOV”, “VA HCC PROBLEM (ICD10)”, “VA HCC PTF (ICD10)”, “VA HCC VPOV (ICD10)”, “VA ALS PROBLEM”, “VA ALS PTF”, “VA ALS VPOV”, “VA ALS PROBLEM (ICD10)”, “VA ALS PTF (ICD10)”, “VA ALS VPOV (ICD10)”</p></td>
</tr>
<tr class="odd">
<td>ROR ICD SEARCH (#798.5)</td>
<td>New entries “VA OSTEOPOROSIS”, “VA PROSTATE CANCER”, “VA LUNG CANCER”, “VA MELANOMA”, “VA COLORECTAL CANCER”, “VA PANCREATIC CANCER”, “VA HCC”, “VA ALS””</td>
</tr>
<tr class="even">
<td>ROR XML ITEM(#799.31)</td>
<td>New entry “LAST_TAKEN”</td>
</tr>
<tr class="odd">
<td>ROR REPORT PARAMETERS (#799.34)</td>
<td>New entry “Sustained Virologic Response”</td>
</tr>
</tbody>
</table>

<span id="_Toc167263989" class="anchor"></span>Table 51 – Global Updates for Patch ROR\*1.5\*34

### Patch ROR\*1.5\*27

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref504495747" class="anchor"></span>Table 52 – Changes for Patch 35</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch adds the following new medications:</p>
<ul>
<li><p>VA Product: ABC/DOL/3TC</p></li>
<li><p>VA Generic: ABACAVIR/DOLUTEGRAVIR/LAMIVUDINE</p></li>
<li><p>VA Product: LED/SOF</p></li>
<li><p>VA Generic: LEDIPASVIR/SOFOBUVIR</p></li>
<li><p>VA Product: OBV/PTV/r+DSV</p></li>
<li><p>VA Generic: DASABUVIR/OMBITASVIR/PARITAPREVIR/RITONAVIR</p></li>
</ul>
<p>These new medications have been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medications.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>Modifications to the Potential <a href="#Glos_DAA">DAA</a> Candidate report to remove exclusion of patients who received Boceprevir or Telaprevir.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Modifications to the Potential <a href="#Glos_DAA">DAA</a> Candidate report to remove exclusion of patients who do not have genotype 1.</td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>4</td>
<td>Correct the definition of Sustained virologic response (SVR) by removing the criteria that patients whose lab results starts with “&gt;” have SVR.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>5</td>
<td>Correct the List of Patients Report selection screen by disabling the Registry Status Pending Comment check box if Pending is not checked. (GUI)</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>6</td>
<td>Update Help Files Copied to Local Drive for Network Installations (GUI)</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>7</td>
<td>This patch brings the Clinical Case Registries (CCR) application into Section 508 compliance in many areas.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>8</td>
<td>Modified the global lock logic in routine RORLOCK to utilize the minimum default lock time system variable DILOCKTM rather than 3 seconds. This is a correction for a SACC violation reported in Remedy ticket #968114 (DILOCKTM not being utilized).</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>9</td>
<td>Resolved a problem involving a maxstring error occurring in the nightly job. This was reported in Remedy tickets # 1228316 and 1227499.  The workaround for the sites was to inactivate some or all of the 8 registries added by patch ROR*1.5*24.  The post install for this patch will reactivate any of these 8 registries that have been marked as inactive.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>10</td>
<td>Added entries to the ROR LIST ITEM file to make sure the proper Result Ranges panels appear on the BMI by Range, Liver Score by Range and Renal Function by Range reports.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>11</td>
<td>The version of the CCR software is updated to 1.5.27</td>
<td colspan="2">M</td>
</tr>
</tbody>
</table>

<span id="_Ref504495747" class="anchor"></span>Table 52 – Changes for Patch 35

<table>
<caption><p><span id="_Toc167263991" class="anchor"></span>Table 53 – Global Updates for Patch ROR*1.5*35</p></caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR GENERIC DRUG #799.51</td>
<td><p>Added entries for</p>
<ul>
<li><p>VA Product: ABC/DOL/3TC</p></li>
</ul>
<blockquote>
<p>VA Generic: ABACAVIR/DOLUTEGRAVIR/LAMIVUDINE</p>
</blockquote>
<ul>
<li><p>VA Product: LED/SOF</p></li>
</ul>
<blockquote>
<p>VA Generic: LEDIPASVIR/SOFOBUVIR</p>
</blockquote>
<ul>
<li><p>VA Product: OBV/PTV/r+DSV</p></li>
</ul>
<blockquote>
<p>VA Generic: DASABUVIR/OMBITASVIR/PARITAPREVIR/RITONAVIR</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc167263991" class="anchor"></span>Table 53 – Global Updates for Patch ROR\*1.5\*35

### Patch ROR\*1.5\*25

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                                                                                                                                                                                                                                                          |     | Type |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | The HL7 nightly extract option Registry Update & Data Extraction \[ROR TASK\] was modified to extract up to 25 ICD-10 diagnoses and procedures contained in an inpatient record.                                                                                                                                     | E   |      |
| 2   | The process to populate a new registry with qualifying patients was modified to use up to 25 ICD-10 diagnoses and procedures contained in an inpatient record.                                                                                                                                                       | E   |      |
| 3   | The selection logic for all CCR reports that screen the output based on diagnosis has been modified to check the additional fields added to the PTF file for ICD-10.                                                                                                                                                 | E   |      |
| 4   | The HL7 nightly extract option Registry Update & Data Extraction \[ROR TASK\] was modified so the Admitting Diagnosis OBX segment extraction logic only extracts the data from the PTF file (#45) for the PRINCIPAL DIAGNOSIS pre-1986 field (#80) if the PRINCIPAL DIAGNOSIS field (#79) does not contain any data. | M   |      |

<span id="_Toc167263992" class="anchor"></span>Table 54 – Changes for Patch 36

<table>
<caption><p><span id="_Toc167263993" class="anchor"></span>Table 55 – Global Updates for Patch ROR*1.5*36</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR METADATA file (#799.2)</td>
<td><p>Added new entries for:</p>
<p>SECONDARY DIAGNOSIS 10</p>
<p>SECONDARY DIAGNOSIS 11</p>
<p>SECONDARY DIAGNOSIS 12</p>
<p>SECONDARY DIAGNOSIS 13</p>
<p>SECONDARY DIAGNOSIS 14</p>
<p>SECONDARY DIAGNOSIS 15</p>
<p>SECONDARY DIAGNOSIS 16</p>
<p>SECONDARY DIAGNOSIS 17</p>
<p>SECONDARY DIAGNOSIS 18</p>
<p>SECONDARY DIAGNOSIS 19</p>
<p>SECONDARY DIAGNOSIS 20</p>
<p>SECONDARY DIAGNOSIS 21</p>
<p>SECONDARY DIAGNOSIS 22</p>
<p>SECONDARY DIAGNOSIS 23</p>
<p>SECONDARY DIAGNOSIS 24</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167263993" class="anchor"></span>Table 55 – Global Updates for Patch ROR\*1.5\*36

### Patch ROR\*1.5\*26

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                                                                                                                                                                                                                 |     | Type |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | Conversion of GUI from Delphi 2006 to Embarcardero XE5.                                                                                                                                                                                                                     | E   |      |
| 2   | Enhanced reporting functionality: A new Selection Panel on each report to allow the user to limit the report to Veterans based on the two categories of No SVR and SVR. This selection panel will not be included on the SVR report.                                        | E   |      |
| 3   | Enhanced reporting functionality: Updated the existing Potential Direct Acting Antiviral (DAA) Candidate report by adding an optional filter based on Fibrosis-4 (FIB-4) score and Liver Score Date Range filter(which are an options in the Liver Score by Range report) . | E   |      |
| 4   | Enhanced reporting functionality: Updated the existing save as functionality so that when a user saves a report as a csv file that the information for all Veterans appears in one worksheet                                                                                | E   |      |
| 5   | Create New Diagnosis group for Liver Transplantation and add it to the Common Templates. The new group will be defined using ICD-9 and ICD-10 codes.                                                                                                                        | E   |      |
| 6   | Create two new Local Registries, Total Knee Replacement and Total Hip Replacement. The new local registries will be defined using ICD-9, ICD-10, and CPT Codes.                                                                                                             | E   |      |
| 7   | Update M version check                                                                                                                                                                                                                                                      | E   |      |
| 8   | The version of the CCR software is updated to 1.5.26                                                                                                                                                                                                                        | E   |      |
| 9   | Modified Custom Controls within the CCR GUI to ensure Section 508 Certification.                                                                                                                                                                                            | E   |      |
| 10  | A situation reported in Remedy ticket INC000001240065 that involved the registry initialization job starting to run within a time period when it was supposed to be suspended has been fixed.                                                                               | F   |      |

<span id="_Ref54003633" class="anchor"></span>Table 56 – Changes for Patch 37

<table>
<caption><p><span id="_Toc167263995" class="anchor"></span>Table 57 – Global Updates for Patch ROR*1.5*37</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DIALOG (#.84)</td>
<td><p><em>Entries modified:</em></p>
<p>7981003.002 General Utiliz. and Demogr (CSV)</p>
<p>7981008.002 VERA Reimbursement Report (CSV)</p>
<p>7981011.002 Patient Medication History (CSV)</p>
<p>7981012.002 Combined Meds and Labs Report(CSV)</p>
<p>7981013.002 Diagnoses(CSV)</p>
<p>7981015.002 Procedures(CSV)</p>
<p>7981018.002 BMI Report by Range (CSV)</p>
<p>7981020.002 Renal Function by Range (CSV)</p>
<p>7981021.001 Potential DAA Candidates (HTML)</p>
<p>7981021.002 Potential DAA Candidates (CSV)</p>
<p>7981022.002 DAA Lab Monitoring(CSV)</p>
<p>7981023.001 Sustained Virologic Reponse (HTML)</p>
<p>7981023.002 Sustained Virologic Reponse (CSV)</p>
<p>7981999.001 Common XSL templates (HTML)</p>
<p>7981999.002 Common XSL templates (CSV)</p></td>
</tr>
<tr class="even">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>Entries New:</em></p>
<p>VA TOTAL HIP</p>
<p>VA TOTAL KNEE</p>
<p><em>Entries modified:</em></p>
<p>VA ALS</p>
<p>VA ALZHEIMERS</p>
<p>VA AMPUTATION</p>
<p>VA APNEA</p>
<p>VA BLIND</p>
<p>VA BREAST CA</p>
<p>VA CHF</p>
<p>VA COLORECTAL CANCER</p>
<p>VA COPD</p>
<p>VA CRD</p>
<p>VA CVD</p>
<p>VA DIABETES</p>
<p>VA DYSLIPIDEMIA</p>
<p>VA HCC</p>
<p>VA HEPC</p>
<p>VA HIV</p>
<p>VA HTN</p>
<p>VA IHD</p>
<p>VA LUNG CANCER</p>
<p>VA MELANOMA</p>
<p>VA MENTAL HEALTH</p>
<p>VA OSTEOARTHRITIS</p>
<p>VA OSTEOPOROSIS</p>
<p>VA PANCREATIC CANCER</p>
<p>VA PROSTRATE CANCER</p>
<p>VA RHEUM</p></td>
</tr>
<tr class="odd">
<td>ROR SELECTION RULE (#798.2)</td>
<td><p><em>Entries New:</em></p>
<p>VA TOTAL HIP CPT PTF PROC</p>
<p>VA TOTAL HIP ICD PTF PROC</p>
<p>VA TOTAL HIP ICD PTF PROC (ICD10)</p>
<p>VA TOTAL KNEE CPT PTF PROC</p>
<p>VA TOTAL KNEE ICD PTF PROC</p>
<p>VA TOTAL KNEE ICD PTF PROC (ICD10)</p>
<p><em>Entries modified:</em></p></td>
</tr>
<tr class="even">
<td>ROR ICD SEARCH (#798.5)</td>
<td><p><em>Entries New:</em></p>
<p>VA TOTAL HIP</p>
<p>VA TOTAL KNEE</p>
<p><em>Entries modified:</em></p></td>
</tr>
<tr class="odd">
<td>ROR LIST ITEM (#799.1)</td>
<td><p><em>Entries New:</em></p>
<p>APRI (VA TOTAL HIP)</p>
<p>APRI (VA TOTAL KNEE)</p>
<p>BMI (VA TOTAL HIP)</p>
<p>BMI (VA TOTAL KNEE)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA TOTAL HIP)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA TOTAL KNEE)</p>
<p>eGFR by CKD-EPI (VA TOTAL HIP)</p>
<p>eGFR by CKD-EPI (VA TOTAL KNEE)</p>
<p>eGFR by MDRD (VA TOTAL HIP)</p>
<p>eGFR by MDRD (VA TOTAL KNEE)</p>
<p>FIB-4 (VA TOTAL HIP)</p>
<p>FIB-4 (VA TOTAL KNEE)</p>
<p>MELD (VA TOTAL HIP)</p>
<p>MELD (VA TOTAL KNEE)</p>
<p>MELD-Na (VA TOTAL HIP)</p>
<p>MELD-Na (VA TOTAL KNEE)</p>
<p>Registry Lab (VA TOTAL HIP)</p>
<p>Registry Lab (VA TOTAL KNEE)</p>
<p><em>Entries modified:</em></p></td>
</tr>
<tr class="even">
<td>ROR METADATA (#799.2)</td>
<td><p><em>Entries New:</em></p>
<p>INPATIENT ICD PROCEDURES</p>
<p>INPATIENT CPT</p>
<p><em>Entries modified:</em></p></td>
</tr>
<tr class="odd">
<td>ROR XML ITEM(#799.31)</td>
<td><p><em>Entries New:</em></p>
<p>SVR</p>
<p><em>Entries modified:</em></p></td>
</tr>
<tr class="even">
<td>ROR REPORT PARAMETERS(#799.34)</td>
<td><p><em>Entries New:</em></p>
<p><em>Entries modified:</em></p>
<p>BMI by Range</p>
<p>Clinic Follow Up</p>
<p>Combined Meds and Labs</p>
<p>Current Inpatient List</p>
<p>DAA Lab Monitoring</p>
<p>Diagnoses</p>
<p>General Utilization and Demographics</p>
<p>Inpatient Utilization</p>
<p>Lab Utilization</p>
<p>List of Registry Patients</p>
<p>Liver Score by Range</p>
<p>Outpatient Utilization</p>
<p>Patient Medication History</p>
<p>Pharmacy Prescription Utilizatization</p>
<p>Potential DAA Candidates</p>
<p>Procedures</p>
<p>Radiology Utilization</p>
<p>Registry Lab Tests by Range</p>
<p>Registry Medications</p>
<p>Renal Function by Range</p></td>
</tr>
<tr class="odd">
<td>PARAMETER (#8989.5)</td>
<td><p><em>Entry new</em>:</p>
<blockquote>
<p>ENTITY: CLINICAL CASE REGISTRIES</p>
<p>PARAMETER: ROR REPORT PARAMS TEMPLATE</p>
<p>INSTANCE: 13::Liver Transplantation</p>
<p>VALUE: CCR Predefined Report Template</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc167263995" class="anchor"></span>Table 57 – Global Updates for Patch ROR\*1.5\*37

### Patch ROR\*1.5\*28

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref85799636" class="anchor"></span>Table 58 – Changes for Patch 38</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Conversion of GUI from Delphi XE5 to Delphi XE8.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>Create five new Local Registries; Crohn’s Disease, Dementia, Hepatitis B, Thyroid Cancer and Ulcerative Colitis. The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>It was discovered that the CCR national database is missing some problem list entries for the patients in the HIV and Hepatitis-C registries dating from 2009 through 2011. To recover this data, this patch will force the CCR nightly job [ROR TASK] to perform a one time re-extract of all problem list entries that were added from 1/1/2009 to the present for patients in these two registries. This may cause a slight increase in the amount of time it takes the nightly job to finish the first time it runs after the installation of this patch.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>4</td>
<td>A problem was discovered with the header display if a user selects the “Complete” or “Summary” report option when running a report. The words “Complete Report” or “Summary Report” are supposed to display after the label Options:, but currently, nothing is being displayed there.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>This patch adds the following new medications:</p>
<ul>
<li><blockquote>
<p>HIV registry: ATAZANAVIR/COBICISTAT</p>
</blockquote></li>
<li><blockquote>
<p>HIV registry: COBICISTAT/DARUNAVIR</p>
</blockquote></li>
<li><blockquote>
<p>HIV registry: ELVITEGRAVIR</p>
</blockquote></li>
<li><blockquote>
<p>HIV registry: ELBASVIR/GRAZOPREVIR</p>
</blockquote></li>
<li><blockquote>
<p>Hepatitis C registry: OMBITASVIR/PARATEPREVIR/RITONAVIR</p>
</blockquote></li>
<li><blockquote>
<p>Hepatitis C registry: DACLATASVIR</p>
</blockquote></li>
</ul>
<p>These new medications have been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medications.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td>An additional selection panel titled "DAA Prescriptions" will be created for the DAA Lab Monitoring report.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>The INPATIENT UTILIZATION report was modified to correct a defect found where the ICN value does not appear on the report when the user selects to include additional identifier in the report.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>8</td>
<td><p>When the VA TOTAL KNEE and VA TOTAL HIP registries were added to</p>
<p>the CCR system by a previous patch, the word Registry was not added to the display name of the registries. This was fixed in this patch by adding the word 'Registry' to the entry in the SHORT DESCRIPTION (#4) field of the ROR REGISTRY PARAMETERS file (#798.1) for the VA TOTAL KNEE and VA TOTAL HIP registry entries.</p></td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>9</td>
<td>A modification was made to allow the DAA Lab Monitoring report to use all drugs defined for the registry as well as locally defined drugs as screening criteria for the report.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>10</td>
<td>The version of the CCR software is updated to 1.5.28</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref85799636" class="anchor"></span>Table 58 – Changes for Patch 38

<table>
<caption><p><span id="_Toc167263997" class="anchor"></span>Table 59 – Global Updates for Patch ROR*1.5*38</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DIALOG (#.84)</td>
<td><p><em>Entries modified:</em></p>
<p>7981999.001 Common XSL templates (HTML)</p></td>
</tr>
<tr class="even">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>Entries New:</em></p>
<p>VA CROHNS</p>
<p>VA DEMENTIA</p>
<p>VA HEPB</p>
<p>VA THYROID CA</p>
<p>VA UC</p>
<p><em>Entries modified:</em></p>
<p>VA TOTAL HIP</p>
<p>VA TOTAL KNEE</p></td>
</tr>
<tr class="odd">
<td>ROR SELECTION RULE (#798.2)</td>
<td><p><em>Entries New:</em></p>
<p>VA CROHNS PTF</p>
<p>VA CROHNS PTF (ICD10)</p>
<p>VA CROHNS PROBLEM</p>
<p>VA CROHNS PROBLEM (ICD10)</p>
<p>VA CROHNS VPOV</p>
<p>VA CROHNS VPOV (ICD10)</p>
<p>VA DEMENTIA PTF</p>
<p>VA DEMENTIA PTF (ICD10)</p>
<p>VA DEMENTIA PROBLEM</p>
<p>VA DEMENTIA PROBLEM (ICD10)</p>
<p>VA DEMENTIA VPOV</p>
<p>VA DEMENTIA VPOV (ICD10)</p>
<p>VA HEPB PTF</p>
<p>VA HEPB PTF (ICD10)</p>
<p>VA HEPB PROBLEM</p>
<p>VA HEPB PROBLEM (ICD10)</p>
<p>VA HEPB VPOV</p>
<p>VA HEPB VPOV (ICD10)</p>
<p>VA THYROID CA PTF</p>
<p>VA THYROID CA PTF (ICD10)</p>
<p>VA THYROID CA PROBLEM</p>
<p>VA THYROID CA PROBLEM (ICD10)</p>
<p>VA THYROID CA VPOV</p>
<p>VA THYROID CA VPOV (ICD10)</p>
<p>VA UC PTF</p>
<p>VA UC PTF (ICD10)</p>
<p>VA UC PROBLEM</p>
<p>VA UC PROBLEM (ICD10)</p>
<p>VA UC VPOV</p>
<p>VA UC VPOV (ICD10)</p>
<p><em>Entries modified:</em></p></td>
</tr>
<tr class="even">
<td>ROR ICD SEARCH (#798.5)</td>
<td><p><em>Entries New:</em></p>
<p>VA CROHNS</p>
<p>VA DEMENTIA</p>
<p>VA HEPB</p>
<p>VA THYROID CA</p>
<p>VA UC</p>
<p><em>Entries modified:</em></p></td>
</tr>
<tr class="odd">
<td>ROR LIST ITEM (#799.1)</td>
<td><p><em>Entries New:</em></p>
<p>APRI (VA CROHNS)</p>
<p>APRI (VA DEMENTIA)</p>
<p>APRI (VA HEPB)</p>
<p>APRI (VA THYROID CA)</p>
<p>APRI (VA UC)</p>
<p>BMI (VA CROHNS)</p>
<p>BMI (VA DEMENTIA)</p>
<p>BMI (VA HEPB)</p>
<p>BMI (VA THYROID CA)</p>
<p>BMI (VA UC)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA CROHNS)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA DEMENTIA)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA HEPB)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA THYROID CA)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA UC)</p>
<p>eGFR by CKD-EPI (VA CROHNS)</p>
<p>eGFR by CKD-EPI (VA DEMENTIA)</p>
<p>eGFR by CKD-EPI (VA HEPB)</p>
<p>eGFR by CKD-EPI (VA THYROID CA)</p>
<p>eGFR by CKD-EPI (VA UC)</p>
<p>eGFR by MDRD (VA CROHNS)</p>
<p>eGFR by MDRD (VA DEMENTIA)</p>
<p>eGFR by MDRD (VA HEPB)</p>
<p>eGFR by MDRD (VA THYROID CA)</p>
<p>eGFR by MDRD (VA UC)</p>
<p>FIB-4 (VA CROHNS)</p>
<p>FIB-4 (VA DEMENTIA)</p>
<p>FIB-4 (VA HEPB)</p>
<p>FIB-4 (VA THYROID CA)</p>
<p>FIB-4 (VA UC)</p>
<p>MELD (VA CROHNS)</p>
<p>MELD (VA DEMENTIA)</p>
<p>MELD (VA HEPB)</p>
<p>MELD (VA THYROID CA)</p>
<p>MELD (VA UC)</p>
<p>MELD-Na (VA CROHNS)</p>
<p>MELD-Na (VA DEMENTIA)</p>
<p>MELD-Na (VA HEPB)</p>
<p>MELD-Na (VA THYROID CA)</p>
<p>MELD-Na (VA UC)</p>
<p>Registry Lab (VA CROHNS)</p>
<p>Registry Lab (VA DEMENTIA)</p>
<p>Registry Lab (VA HEPB)</p>
<p>Registry Lab (VA THYROID CA)</p>
<p>Registry Lab (VA UC)</p>
<p><em>Entries modified:</em></p></td>
</tr>
<tr class="even">
<td>ROR XML ITEM(#799.31)</td>
<td><p><em>Entries New:</em></p>
<p>DAA_DRUGS</p>
<p><em>Entries modified:</em></p></td>
</tr>
<tr class="odd">
<td>ROR REPORT PARAMETERS(#799.34)</td>
<td><p><em>Entries modified:</em></p>
<p>DAA Lab Monitoring Report</p></td>
</tr>
<tr class="even">
<td>ROR GENERIC DRUG (#799.51)</td>
<td><p><em>Entries New:</em></p>
<p>DACLATASVIR</p>
<p>OMBITASVIR/PARATEPREVIR/R</p>
<p>ATAZANAVIR/COBICISTAT</p>
<p>COBICISTAT/DARUNAVIR</p>
<p>ELVITEGRAVIR</p>
<p>ELBASVIR/GRAZOPREVIR</p>
<p><em>Entries modified:</em></p></td>
</tr>
</tbody>
</table>

<span id="_Toc167263997" class="anchor"></span>Table 59 – Global Updates for Patch ROR\*1.5\*38

### Patch ROR\*1.5\*29

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                                                                                                                                                                                                                                                                                |     | Type |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | An additional selection panel titled "Diagnosis Date Range" will be created for the reports that use Other Diagnoses panel.                                                                                                                                                                                                                | E   |      |
| 2   | A new Hepatitis A report has been added to identify patients who either had Hepatitis A vaccine or have immunity to the Hepatitis A virus – or to identify patients who have not had the Hepatitis A vaccine and are not immune. It is available to all registries                                                                         | E   |      |
| 4   | A new Hepatitis B report is to identify patients who either had Hepatitis B vaccine or have immunity to the Hepatitis B virus and do not have chronic HBV – or to identify patients who have not had Hepatitis B vaccine and are not immune and do not have chronic HBV. It is available to all registries except the Hepatitis B registry | E   |      |
| 5   | An additional selection panel titled "Patients" will be created for the Hepatitis A report.                                                                                                                                                                                                                                                | E   |      |
| 6   | An additional selection panel titled "Patients" will be created for the Hepatitis B report.                                                                                                                                                                                                                                                | E   |      |
| 7   | An additional selection panel titled "Vaccinations Date Range" will be created for the Hepatitis A and Hepatitis B reports.                                                                                                                                                                                                                | E   |      |
| 8   | An additional selection panel titled "Immunity Date Range" will be created for the Hepatitis A and Hepatitis B reports.                                                                                                                                                                                                                    | E   |      |
| 9   | A modification was made to allow the DAA Lab Monitoring report to use all drugs defined for the registry as well as locally defined drugs as screening criteria for the report.                                                                                                                                                            | E   |      |
| 10  | The version of the CCR software is updated to 1.5.29                                                                                                                                                                                                                                                                                       | E   |      |

<span id="_Toc167263998" class="anchor"></span>Table 60 – Changes for Patch 39

<table>
<caption><p><span id="_Toc167263999" class="anchor"></span>Table 61 – Global Updates for Patch ROR*1.5*39</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DIALOG (#.84)</td>
<td><p><em>Entries modified:</em></p>
<p>7981999.001 Common XSL templates (HTML)</p>
<p>7980000.018 Report options</p>
<p><em>Entries new:</em></p>
<p>7981024.001 Hepatitis A Report (HTML)</p>
<p>7981024.002 Hepatitis A Report (CSV)</p>
<p>7981025.001 Hepatitis B Report (HTML)</p>
<p>7981025.002 Hepatitis B Report (CSV)</p></td>
</tr>
<tr class="even">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>Entries modified:</em></p>
<p>VA ALS</p>
<p>VA ALZHEIMERS</p>
<p>VA AMPUTATION</p>
<p>VA ALZHEIMERS</p>
<p>VA AMPUTATION</p>
<p>VA APNEA</p>
<p>VA BLIND</p>
<p>VA BREAST CA</p>
<p>VA CHF</p>
<p>VA COLORECTAL CANCER</p>
<p>VA COPD</p>
<p>VA CRD</p>
<p>VA CROHNS</p>
<p>VA CVD</p>
<p>VA DEMENTIA</p>
<p>VA DIABETES</p>
<p>VA DYSLIPIDEMIA</p>
<p>VA HCC</p>
<p>VA HEPB</p>
<p>VA HEPC</p>
<p>VA HIV</p>
<p>VA HTN</p>
<p>VA IHD</p>
<p>VA LUNG CANCER</p>
<p>VA MELANOMA</p>
<p>VA MENTAL HEALTH</p>
<p>VA MULTIPLE SCLEROSIS</p>
<p>VA OSTEOARTHRITIS</p>
<p>VA OSTEOPOROSIS</p>
<p>VA PANCREATIC CANCER</p>
<p>VA PROSTATE CANCER</p>
<p>VA RHEUM</p>
<p>VA THYROID CA</p>
<p>VA TOTAL HIP</p>
<p>VA TOTAL KNEE</p>
<p>VA UC</p></td>
</tr>
<tr class="odd">
<td>ROR XML ITEM(#799.31)</td>
<td><p><em>Entries new:</em></p>
<p>DATE_RANGE_5</p>
<p>DATE_RANGE_6</p>
<p>DATE_RANGE_7</p>
<p>HEPAIMM</p>
<p>HEPBIMM</p>
<p>NOHEPAIMM</p>
<p>NOHEPBIMM</p>
<p>HEPAVAC</p>
<p>HEPBVAC</p>
<p>NOHEPAVAC</p>
<p>NOHEPBVAC</p>
<p>VAC</p>
<p>VACCINE</p>
<p>VACCINES</p>
<p>VAC_DATE</p>
<p>VAC_NAME</p></td>
</tr>
<tr class="even">
<td>ROR REPORT PARAMETERS(#799.34)</td>
<td><p><em>Entries new:</em></p>
<p>Hepatitis A Vaccine or Immunity</p>
<p>Hepatitis B Vaccine or Immunity</p>
<p><em>Entries modified:</em></p>
<p>BMI by Range</p>
<p>Clinic Follow Up</p>
<p>Combined Meds and Labs</p>
<p>Current Inpatient List</p>
<p>DAA Lab Monitoring</p>
<p>General Utilization and Demographics</p>
<p>Inpatient Utilization</p>
<p>Lab Utilization</p>
<p>List of Registry Patients</p>
<p>Liver Score by Range</p>
<p>Outpatient Utilization</p>
<p>Patient Medication History</p>
<p>Pharmacy Prescription Utilization</p>
<p>Potential DAA Candidates</p>
<p>Procedures</p>
<p>Radiology Utilization</p>
<p>Registry Lab Tests by Range</p>
<p>Registry Medications</p>
<p>Renal Function by Range</p>
<p>Sustained Virologic Response</p>
<p>VERA Reimbursement Report</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167263999" class="anchor"></span>Table 61 – Global Updates for Patch ROR\*1.5\*39

### Patch ROR\*1.5\*30

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc167264000" class="anchor"></span>Table 62 – Changes for Patch 40</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Create two new Local Registries; Hypoparathyroidism and Idiopathic Pulmonary Fibrosis. The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td>It was discovered that the Hepatitis A and Hepatitis B reports were not finding all patients who have laboratory documented immunity.   HCV and HIV labs have always used case insensitive searches for positive LOINC results so results entered in mixed case  were missed.  The code has been modified to ignore case when searching for results.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>3</td>
<td>The caption on the Sex panel has been modified from Sex to Birth Sex. The output for the report headers and report columns were modified appropriately.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td><p>This patch adds the following new medication:</p>
<ul>
<li><p>Hepatitis C registry: SOFOSBUVIR/VELPATASVIR</p></li>
</ul>
<p>The new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>The warning on the Potential DAA Candidates report has been updated to  remove the reference  to genotype 1, as the report no longer requires genotype 1.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Additional CCR GUI updates were made to work towards becoming fully</p>
<p>compliant with the Section 508 standards.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>The version of the CCR software is updated to 1.5.30</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc167264000" class="anchor"></span>Table 62 – Changes for Patch 40

<table>
<caption><p><span id="_Toc167264001" class="anchor"></span>Table 63 – Global Updates for Patch ROR*1.5*40</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DIALOG (#.84)</td>
<td><p><em>Entries modified:</em></p>
<p>7981003.001 General Util. and Demographics (HTML)</p>
<p>7981003.002 General Util. and Demographics (CSV)</p>
<p>7981997.001 Patient data templates (HTML)</p>
<p>7981997.002 Patient data templates (CSV)</p>
<p>7981999.001 Common XSL templates (HTML)</p></td>
</tr>
<tr class="even">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>New Entries</em></p>
<p>VA IPF</p>
<p>VA HYPOPARA</p></td>
</tr>
<tr class="odd">
<td>ROR SELECTION RULE (#798.2)</td>
<td><p><em>Entries New:</em></p>
<p>VA IPF</p>
<p>VA HYPOPARA</p></td>
</tr>
<tr class="even">
<td>ROR ICD SEARCH (#798.5)</td>
<td><p><em>Entries New:</em></p>
<p>VA IPF</p>
<p>VA HYPOPARA</p></td>
</tr>
<tr class="odd">
<td>ROR XML ITEM(#799.31)</td>
<td><p><em>Entries new:</em></p>
<p>BIRTHSEX</p>
<p>BIRTHSEX_SUMMARY</p></td>
</tr>
<tr class="even">
<td>ROR GENERIC DRUG (#799.51)</td>
<td><p><em>Entries new:</em></p>
<p>Hepatitis C registry: SOFOSBUVIR/VELPATASVIR</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167264001" class="anchor"></span>Table 63 – Global Updates for Patch ROR\*1.5\*40

### Patch ROR\*1.5\*31

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc167264002" class="anchor"></span>Table 64 – Changes for Patch 41</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Create two new Local Registries; Adrenal Adenoma and Movement Disorders. The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>This patch adds the following new medication:</p>
<ul>
<li><p>Hepatitis C registry: SOFOSBUVIR/VELPATASVIR /VOXILAPREVIR</p></li>
</ul>
<p>The new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>In the CCR GUI, a new AGE_RANGE panel has been added to all reports to allow filtering by age or date of birth. The new panel has been added in the GUI after the “Birth Sex” panel and a new column for Age/DOB has been added to all report headers following the Last 4 digits of SSN column. If the user selects all for “Age Range” no Age/DOB column is added.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>On the Pharmacy Prescription Utilization report, it was discovered that the patient ICN was missing on the portion of the report that lists the Highest Combined Outpatient (OP) and Inpatient (IP) Utilization Summary. The report has been updated to include the ICN.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>5</td>
<td>On the Diagnoses report, a modification was made to keep the display of Date of Death (DOD) consistent with other reports. Currently, if a time piece exists in VistA for the DOD, the Diagnoses report displays the DOD as the date with the time included. All the other reports display the DOD as just the date without the time. The time stamp has been removed from the Date of Death column on the Diagnoses report to ensure consistency among reports.</td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>6</td>
<td>In the CCR GUI, the caption on the Additional Identifier panel has been modified from Additional Identifier to Additional Identifiers.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>7</td>
<td>In the CCR GUI, two new options have been added to the Additional Identifiers panel to allow the Patient Aligned Care Team (PACT) and/or Primary Care Provider (PCP) to be included on all the reports. Two new report columns, entitled “PACT” and “PCP,” will be added to the report output following the column titled “ICN.” If selected, these new report columns will be added everywhere “ICN” currently appears in reports.  The column widths for these new columns will be sized to accommodate approximately 30 characters.  If a patient does not have a PACT or PCP, the output will be blank.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>8</td>
<td>In the CCR GUI, a modification was made on several of the “utilization” reports when the user selects the “Include details” option the associated edit control color has been updated to indicate to the user that the control is enabled.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>9</td>
<td><p>In the CCR GUI, a modification was made on the reports listed below to disable the Additional Identifiers panel if the Summary option was selected.</p>
<ul>
<li><p>BMI by Range</p></li>
<li><p>Diagnoses</p></li>
<li><p>General Utilization and Demographics</p></li>
<li><p>Inpatient Utilization</p></li>
<li><p>Lab Utilization</p></li>
<li><p>Outpatient Utilization</p></li>
<li><p>Pharmacy Prescription Utilization</p></li>
<li><p>Procedures</p></li>
<li><p>Radiology Utilization</p></li>
<li><p>Registry Medications</p></li>
<li><p>Renal Function by Range</p></li>
<li><p>VERA Reimbursement</p></li>
</ul></td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>10</td>
<td>On the General Utilization and Demographics report, a modification was made to the report to remove the “No data has been found” message if the Summary option is selected and there was data to generate a summary.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>11</td>
<td>The version of the CCR software is updated to 1.5.31</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc167264002" class="anchor"></span>Table 64 – Changes for Patch 41

<table>
<caption><p><span id="_Toc167264003" class="anchor"></span>Table 65 – Global Updates for Patch ROR*1.5*41</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DIALOG (#.84)</td>
<td><p><em>Entries modified:</em></p>
<p>7981002.001 Current Inpatient List (HTML)</p>
<p>7981002.002 Current Inpatient List (CSV)</p>
<p>7981003.001 General Utiliz. and Demogr. (HTML)</p>
<p>7981003.002 General Utiliz. and Demogr. (CSV)</p>
<p>7981004.001 Clinic Follow Up (HTML)</p>
<p>7981004.002 Clinic Follow Up (CSV)</p>
<p>7981006.002 Laboratory Utilization (CSV)</p>
<p>7981007.001 Radiology Utilization (HTML)</p>
<p>7981007.002 Radiology Utilization (CSV)</p>
<p>7981008.001 VERA Reimbursement Report (HTML)</p>
<p>7981008.002 VERA Reimbursement Report (CSV)</p>
<p>7981009.001 Pharmacy Prescription Utilization (HTML)</p>
<p>7981009.002 Pharmacy Prescription Utilization (CSV)</p>
<p>7981010.001 Registry Lab Tests by Range (HTML)</p>
<p>7981010.002 Registry Lab Tests by Range (CSV)</p>
<p>7981011.001 Patient Medication History (HTML)</p>
<p>7981011.002 Patient Medication History (CSV)</p>
<p>7981012.001 Combined Meds and Labs Report (HTML)</p>
<p>7981012.002 Combined Meds and Labs Report (CSV)</p>
<p>7981013.001 Diagnoses (HTML)</p>
<p>7981013.002 Diagnoses (CSV)</p>
<p>7981014.001 Registry Medications Report (HTML)</p>
<p>7981014.002 Registry Medications Report (CSV)</p>
<p>7981015.001 Procedures (HTML)</p>
<p>7981015.002 Procedures (CSV)</p>
<p>7981016.001 Outpatient Utilization (HTML)</p>
<p>7981016.002 Outpatient Utilization (CSV)</p>
<p>7981018.002 BMI Report by Range (CSV)</p>
<p>7981019.002 Liver Report by Range (CSV)</p>
<p>7981019.001 Liver Report by Range (HTML)</p>
<p>7981020.001 Renal Function by Range (HTML)</p>
<p>7981020.002 Renal Function by Range (CSV)</p>
<p>7981021.001 Potential DAA Candidates (HTML)</p>
<p>7981021.002 Potential DAA Candidates (CSV)</p>
<p>7981022.001 DAA Lab Monitoring (HTML)</p>
<p>7981022.002 DAA Lab Monitoring (CSV)</p>
<p>7981023.001 Sustained Virologic Response (HTML)</p>
<p>7981023.002 Sustained Virologic Response (CSV)</p>
<p>7981024.001 Hepatitis A Report (HTML)</p>
<p>7981024.002 Hepatitis A Report (CSV)</p>
<p>7981025.001 Hepatitis B Report (HTML)</p>
<p>7981025.002 Hepatitis B Report (CSV)</p>
<p>7981995.001 Lab data templates (HTML)</p>
<p>7981996.001 Pharmacy data templates (HTML)</p>
<p>7981997.001 Patient data templates (HTML)</p>
<p>7981997.002 Patient data templates (CSV)</p>
<p>7981999.001 Common XSL templates (HTML)</p>
<p>7981999.002 Common XSL templates (CSV)</p></td>
</tr>
<tr class="even">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>Entries New:</em></p>
<p>VA ADRENAL ADENOMA</p>
<p>VA MOVEMENT DISORDERS</p></td>
</tr>
<tr class="odd">
<td>ROR SELECTION RULE (#798.2)</td>
<td><p><em>Entries New:</em></p>
<p>VA ADRENAL ADENOMA PROBLEM</p>
<p>VA ADRENAL ADENOMA PROBLEM (ICD10)</p>
<p>VA ADRENAL ADENOMA PTF</p>
<p>VA ADRENAL ADENOMA PTF (ICD10)</p>
<p>VA ADRENAL ADENOMA VPOV</p>
<p>VA ADRENAL ADENOMA VPOV (ICD10)</p>
<p>VA MOVEMENT DISORDERS PROBLEM</p>
<p>VA MOVEMENT DISORDERS PROBLEM (ICD10)</p>
<p>VA MOVEMENT DISORDERS PTF</p>
<p>VA MOVEMENT DISORDERS PTF (ICD10)</p>
<p>VA MOVEMENT DISORDERS VPOV</p>
<p>VA MOVEMENT DISORDERS VPOV (ICD10)</p></td>
</tr>
<tr class="even">
<td>ROR ICD SEARCH (#798.5)</td>
<td><p><em>Entries New:</em></p>
<p>VA ADRENAL ADENOMA</p>
<p>VA MOVEMENT DISORDERS</p></td>
</tr>
<tr class="odd">
<td>ROR LIST ITEM (#799.1)</td>
<td><p><em>Entries New:</em></p>
<p>APRI (VA ADRENAL ADENOMA)</p>
<p>APRI (VA MOVEMENT DISORDERS)</p>
<p>BMI (VA ADRENAL ADENOMA)</p>
<p>BMI (VA MOVEMENT DISORDERS)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA ADRENAL ADENOMA)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA MOVEMENT DISORDERS)</p>
<p>eGFR by CKD-EPI (VA ADRENAL ADENOMA)</p>
<p>eGFR by CKD-EPI (VA MOVEMENT DISORDERS)</p>
<p>eGFR by MDRD (VA ADRENAL ADENOMA)</p>
<p>eGFR by MDRD (VA MOVEMENT DISORDERS)</p>
<p>FIB-4 (VA ADRENAL ADENOMA)</p>
<p>FIB-4 (VA MOVEMENT DISORDERS)</p>
<p>MELD (VA ADRENAL ADENOMA)</p>
<p>MELD (VA MOVEMENT DISORDERS)</p>
<p>MELD-Na (VA ADRENAL ADENOMA)</p>
<p>MELD-Na (VA MOVEMENT DISORDERS)</p>
<p>Registry Lab (VA ADRENAL ADENOMA)</p>
<p>Registry Lab (VA MOVEMENT DISORDERS)</p>
<p><em>Entries modified</em>:</p>
<p>HIV WB</p></td>
</tr>
<tr class="even">
<td>ROR XML ITEM (#799.31)</td>
<td><p><em>Entries New:</em></p>
<p>AGE_RANGE</p>
<p>PACT</p>
<p>PCP</p></td>
</tr>
<tr class="odd">
<td>ROR REPORT PARAMETERS(#799.34)</td>
<td><p><em>Entries New:</em></p>
<p>Age Range new panel #21 is added to all reports</p>
<p>- BMI by Range</p>
<p>- Clinic Follow Up</p>
<p>- Combined Meds and Labs</p>
<p>- Current Inpatient List</p>
<p>- DAA Lab Monitoring</p>
<p>- Diagnoses</p>
<p>- Hepatitis A Vaccine or Immunity</p>
<p>- Hepatitis B Vaccine or Immunity</p>
<p>- Inpatient Utilization</p>
<p>- Lab Utilization</p>
<p>- List of Registry Patients</p>
<p>- Liver Score by Range</p>
<p>- Outpatient Utilization</p>
<p>- Pharmacy Prescription Utilization</p>
<p>- Potential DAA Candidates</p>
<p>- Procedures</p>
<p>- Radiology Utilization</p>
<p>- Registry Lab Tests by Range</p>
<p>- Registry Medications</p>
<p>- Renal Function by Range</p>
<p>- Sustained Virologic Response</p>
<p>- VERA Reimbursement Report</p></td>
</tr>
<tr class="even">
<td>ROR GENERIC DRUG (#799.51)</td>
<td><p><em>Entries new:</em></p>
<p>Hepatitis C registry: SOFOSBUVIR/VELPATASVIR/VOXILAPREVIR</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167264003" class="anchor"></span>Table 65 – Global Updates for Patch ROR\*1.5\*41

### Patch ROR\*1.5\*32

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref69462109" class="anchor"></span>Table 66 – Changes for Patch 42</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Create two new Local Registries; Transgender and Frailty. The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>This patch adds the following new medication:</p>
<ul>
<li><p>HEP C registry: GLECAPREVIR/PIBRENTASVIR</p></li>
<li><p>HIV registry: DOLUTEGRAVIR/RILPIVIRINE</p></li>
</ul>
<p>The new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>In the CCR GUI, a new “Admitting Diagnosis” column has been added to the Current Inpatient List report. The new column will be located after the “Room-Bed” column.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>On the Hepatitis A and Hepatitis B Immunity reports, the report results have been modified to look at the most recent immune status.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>5</td>
<td><p>The Patient Medication History report has been modified to include all medications even if the drugs are unmatched to the VA Products.</p>
<p>To resolve this issue the following changes have been made:</p>
<ul>
<li><p>The post install routine of the patch has been designed to collect existing drug matching on daily basis and store them in ROR files.</p></li>
<li><p>A nightly job which will be executed automatically is called Schedule ROR Drug Match [ROR DRUG MATCH]</p></li>
<li><p>The Patient Medication report has been modified to check the new matching nodes created by this patch if they do not exist in pharmacy side.</p></li>
</ul></td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>6</td>
<td>In the CCR GUI, the title on the Patient Data Editor screen has been modified to display the correct registry name when a local registry is selected.</td>
<td colspan="2">F</td>
</tr>
<tr class="odd">
<td>7</td>
<td>In the CCR GUI, the BMI by Range and Renal Function by Range CSV report output has been modified to not display "No data has been found" when the Summary only option was selected for the report.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>8</td>
<td>In the CCR GUI, a "More" button has been added after the "Patients found" count when there are more patients than the maximum number of patients to retrieve setting is set for.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>9</td>
<td>The version of the CCR software is updated to 1.5.32</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref69462109" class="anchor"></span>Table 66 – Changes for Patch 42

<table>
<caption><p><span id="_Toc167264005" class="anchor"></span>Table 67 – Global Updates for Patch ROR*1.5*42</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DIALOG (#.84)</td>
<td><p><em>Entries modified:</em></p>
<p>7981002.001 Current Inpatient List (HTML)</p>
<p>7981002.002 Current Inpatient List (CSV)</p>
<p>7981018.002 BMI Report by Range (CSV)</p>
<p>7981020.002 Renal Function by Range (CSV)</p></td>
</tr>
<tr class="even">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>Entries New:</em></p>
<p>VA TRANSGENDER</p>
<p>VA FRAILTY</p></td>
</tr>
<tr class="odd">
<td>ROR SELECTION RULE (#798.2)</td>
<td><p><em>Entries New:</em></p>
<p>VA TRANSGENDER PROBLEM</p>
<p>VA TRANSGENDER PROBLEM (ICD10)</p>
<p>VA TRANSGENDER PTF</p>
<p>VA TRANSGENDER PTF (ICD10)</p>
<p>VA TRANSGENDER VPOV</p>
<p>VA TRANSGENDER VPOV (ICD10)</p>
<p>VA FRAILTY PROBLEM</p>
<p>VA FRAILTY PROBLEM (ICD10)</p>
<p>VA FRAILTY PTF</p>
<p>VA FRAILTY PTF (ICD10)</p>
<p>VA FRAILTY VPOV</p>
<p>VA FRAILTY VPOV (ICD10)</p></td>
</tr>
<tr class="even">
<td>ROR ICD SEARCH (#798.5)</td>
<td><p><em>Entries New:</em></p>
<p>VA TRANSGENDER</p>
<p>VA FRAILTY</p></td>
</tr>
<tr class="odd">
<td>ROR LIST ITEM (#799.1)</td>
<td><p><em>Entries New:</em></p>
<p>APRI (VA TRANSGENDER)</p>
<p>APRI (VA FRAILTY)</p>
<p>BMI (VA TRANSGENDER)</p>
<p>BMI (VA FRAILTY)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA TRANSGENDER)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA FRAILTY)</p>
<p>eGFR by CKD-EPI (VA TRANSGENDER)</p>
<p>eGFR by CKD-EPI (VA FRAILTY)</p>
<p>eGFR by MDRD (VA TRANSGENDER)</p>
<p>eGFR by MDRD (VA FRAILTY)</p>
<p>FIB-4 (VA TRANSGENDER)</p>
<p>FIB-4 (VA FRAILTY)</p>
<p>MELD (VA TRANSGENDER)</p>
<p>MELD (VA FRAILTY)</p>
<p>MELD-Na (VA TRANSGENDER)</p>
<p>MELD-Na (VA FRAILTY)</p>
<p>Registry Lab (VA TRANSGENDER)</p>
<p>Registry Lab (VA FRAILTY)</p></td>
</tr>
<tr class="even">
<td>ROR GENERIC DRUG (#799.51)</td>
<td><p><em>Entries new:</em></p>
<p>HEP C registry: GLECAPREVIR/PIBRENTASVIR</p>
<p>HIV registry: DOLUTEGRAVIR/RILPIVIRINE</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167264005" class="anchor"></span>Table 67 – Global Updates for Patch ROR\*1.5\*42

### Patch ROR\*1.5\*33

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc167264006" class="anchor"></span>Table 68 – Software and Documentation Download Sites</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Create six new Local Registries; Transplant Heart, Transplant Intestine, Transplant Kidney, Transplant Liver, Transplant Lung and Transplant Pancreas. The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>This patch adds the following new medications:</p>
<ul>
<li><p>HIV registry: BICTEGRAVIR/EMTRICITABINE/TENOFOVIR ALAFENAMIDE</p></li>
<li><p>HIV registry: EFAVIRENZ/LAMIVUDINE/TENOFOVIR DISOPROXIL FUMARATE</p></li>
<li><p>HIV registry: LAMIVUDINE/TENOFOVIR DISOPROXIL FUMARATE</p></li>
</ul>
<p>The new medications have been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medications.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>In the CCR GUI, a new “Future Appointments” panel has been added to the following reports for all registries:</p>
<ul>
<li><p>BMI by Range</p></li>
<li><p>Combined Meds and Labs</p></li>
<li><p>Hepatitis A Vaccine or Immunity</p></li>
<li><p>Hepatitis B Vaccine or Immunity</p></li>
<li><p>Liver Score by Range</p></li>
<li><p>Registry Lab Tests by Range</p></li>
<li><p>Renal Function by Range</p></li>
</ul>
<p>It has also been in the Hepatitis C registry to the following report:</p>
<ul>
<li><p>Potential DAA Candidates</p></li>
</ul>
<p>The new panel has been added after the “Additional Identifiers” panel and a new “Next Appt” column has been added to the report data columns. If the user selects “All patients” then no “Next Appt” column is added.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>New LOINC codes have been added to the ROR LAB SEARCH file (#798.9) to add patients to the HIV pending patient list</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>5</td>
<td>On the Combined Meds and Labs, DAA Lab Monitoring, Hepatitis A Vaccine or Immunity and Hepatitis B Vaccine or Immunity reports, it was discovered sorting on the ICN, PACT or PCP columns was not working. The reports have been updated to sort properly on the ICN, PACT or PCP columns.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>6</td>
<td>The version of the CCR software is updated to 1.5.33</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc167264006" class="anchor"></span>Table 68 – Software and Documentation Download Sites

<table>
<caption><p><span id="_Toc167264007" class="anchor"></span>Table 69 – Software Distributives</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DIALOG (#.84)</td>
<td><p><em>Entries modified:</em></p>
<p>7981010.001 Registry Lab Tests by Range (HTML)</p>
<p>7981010.002 Registry Lab Tests by Range (CSV)</p>
<p>7981012.001 Combined Meds and Labs (HTML)</p>
<p>7981012.002 Combined Meds and Labs (CSV)</p>
<p>7981018.002 BMI Report by Range (CSV)</p>
<p>7981019.002 Liver Score by Range (CSV)</p>
<p>7981020.002 Renal Function by Range (CSV)</p>
<p>7981021.002 Potential DAA Candidates (CSV)</p>
<p>7981022.001 DAA Lab Monitoring (HTML)</p>
<p>7981024.001 Hepatitis A Report (HTML)</p>
<p>7981024.002 Hepatitis A Report (CSV)</p>
<p>7981025.001 Hepatitis B Report (HTML)</p>
<p>7981025.002 Hepatitis B Report (CSV)</p>
<p>7981997.001 Patient data templates (HTML)</p>
<p>7981999.001 Common XSL templates (HTML)</p>
<p>7981999.002 Common XSL templates (CSV)</p></td>
</tr>
<tr class="even">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>Entries New:</em></p>
<p>VA TRANSPLANT HEART</p>
<p>VA TRANSPLANT INTESTINE</p>
<p>VA TRANSPLANT KIDNEY</p>
<p>VA TRANSPLANT LIVER</p>
<p>VA TRANSPLANT LUNG</p>
<p>VA TRANSPLANT PANCREAS</p></td>
</tr>
<tr class="odd">
<td>ROR SELECTION RULE (#798.2)</td>
<td><p><em>Entries New:</em></p>
<p>VA TRANSPLANT HEART PROBLEM</p>
<p>VA TRANSPLANT HEART PROBLEM (ICD10)</p>
<p>VA TRANSPLANT HEART PTF</p>
<p>VA TRANSPLANT HEART PTF (ICD10)</p>
<p>VA TRANSPLANT HEART VPOV</p>
<p>VA TRANSPLANT HEART VPOV (ICD10)</p>
<p>VA TRANSPLANT INTESTINE PROBLEM</p>
<p>VA TRANSPLANT INTESTINE PROBLEM (ICD10)</p>
<p>VA TRANSPLANT INTESTINE PTF</p>
<p>VA TRANSPLANT INTESTINE PTF (ICD10)</p>
<p>VA TRANSPLANT INTESTINE VPOV</p>
<p>VA TRANSPLANT INTESTINE VPOV (ICD10)</p>
<p>VA TRANSPLANT KIDNEY PROBLEM</p>
<p>VA TRANSPLANT KIDNEY PROBLEM (ICD10)</p>
<p>VA TRANSPLANT KIDNEY PTF</p>
<p>VA TRANSPLANT KIDNEY PTF (ICD10)</p>
<p>VA TRANSPLANT KIDNEY VPOV</p>
<p>VA TRANSPLANT KIDNEY VPOV (ICD10)</p>
<p>VA TRANSPLANT LIVER PROBLEM</p>
<p>VA TRANSPLANT LIVER PROBLEM (ICD10)</p>
<p>VA TRANSPLANT LIVER PTF</p>
<p>VA TRANSPLANT LIVER PTF (ICD10)</p>
<p>VA TRANSPLANT LIVER VPOV</p>
<p>VA TRANSPLANT LIVER VPOV (ICD10)</p>
<p>VA TRANSPLANT LUNG PROBLEM</p>
<p>VA TRANSPLANT LUNG PROBLEM (ICD10)</p>
<p>VA TRANSPLANT LUNG PTF</p>
<p>VA TRANSPLANT LUNG PTF (ICD10)</p>
<p>VA TRANSPLANT LUNG VPOV</p>
<p>VA TRANSPLANT LUNG VPOV (ICD10)</p>
<p>VA TRANSPLANT PANCREAS PROBLEM</p>
<p>VA TRANSPLANT PANCREAS PROBLEM (ICD10)</p>
<p>VA TRANSPLANT PANCREAS PTF</p>
<p>VA TRANSPLANT PANCREAS PTF (ICD10)</p>
<p>VA TRANSPLANT PANCREAS VPOV</p>
<p>VA TRANSPLANT PANCREAS VPOV (ICD10)</p></td>
</tr>
<tr class="even">
<td>ROR ICD SEARCH (#798.5)</td>
<td><p><em>Entries New:</em></p>
<p>VA TRANSPLANT HEART</p>
<p>VA TRANSPLANT INTESTINE</p>
<p>VA TRANSPLANT KIDNEY</p>
<p>VA TRANSPLANT LIVER</p>
<p>VA TRANSPLANT LUNG</p>
<p>VA TRANSPLANT PANCREAS</p></td>
</tr>
<tr class="odd">
<td>ROR LIST ITEM (#799.1)</td>
<td><p><em>Entries New:</em></p>
<p>APRI (VA TRANSPLANT HEART)</p>
<p>APRI (VA TRANSPLANT INTESTINE)</p>
<p>APRI (VA TRANSPLANT KIDNEY)</p>
<p>APRI (VA TRANSPLANT LIVER)</p>
<p>APRI (VA TRANSPLANT LUNG)</p>
<p>APRI (VA TRANSPLANT PANCREAS)</p>
<p>BMI (VA TRANSPLANT HEART)</p>
<p>BMI (VA TRANSPLANT INTESTINE)</p>
<p>BMI (VA TRANSPLANT KIDNEY)</p>
<p>BMI (VA TRANSPLANT LIVER)</p>
<p>BMI (VA TRANSPLANT LUNG)</p>
<p>BMI (VA TRANSPLANT PANCREAS)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA TRANSPLANT HEART)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA TRANSPLANT INTESTINE)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA TRANSPLANT KIDNEY)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA TRANSPLANT LIVER)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA TRANSPLANT LUNG)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA TRANSPLANT PANCREAS)</p>
<p>eGFR by CKD-EPI (VA TRANSPLANT HEART)</p>
<p>eGFR by CKD-EPI (VA TRANSPLANT INTESTINE)</p>
<p>eGFR by CKD-EPI (VA TRANSPLANT KIDNEY)</p>
<p>eGFR by CKD-EPI (VA TRANSPLANT LIVER)</p>
<p>eGFR by CKD-EPI (VA TRANSPLANT LUNG)</p>
<p>eGFR by CKD-EPI (VA TRANSPLANT PANCREAS)</p>
<p>eGFR by MDRD (VA TRANSPLANT HEART)</p>
<p>eGFR by MDRD (VA TRANSPLANT INTESTINE)</p>
<p>eGFR by MDRD (VA TRANSPLANT KIDNEY)</p>
<p>eGFR by MDRD (VA TRANSPLANT LIVER)</p>
<p>eGFR by MDRD (VA TRANSPLANT LUNG)</p>
<p>eGFR by MDRD (VA TRANSPLANT PANCREAS)</p>
<p>FIB-4 (VA TRANSPLANT HEART)</p>
<p>FIB-4 (VA TRANSPLANT INTESTINE)</p>
<p>FIB-4 (VA TRANSPLANT KIDNEY)</p>
<p>FIB-4 (VA TRANSPLANT LIVER)</p>
<p>FIB-4 (VA TRANSPLANT LUNG)</p>
<p>FIB-4 (VA TRANSPLANT PANCREAS)</p>
<p>MELD (VA TRANSPLANT HEART)</p>
<p>MELD (VA TRANSPLANT INTESTINE)</p>
<p>MELD (VA TRANSPLANT KIDNEY)</p>
<p>MELD (VA TRANSPLANT LIVER)</p>
<p>MELD (VA TRANSPLANT LUNG)</p>
<p>MELD (VA TRANSPLANT PANCREAS)</p>
<p>MELD-Na (VA TRANSPLANT HEART)</p>
<p>MELD-Na (VA TRANSPLANT INTESTINE)</p>
<p>MELD-Na (VA TRANSPLANT KIDNEY)</p>
<p>MELD-Na (VA TRANSPLANT LIVER)</p>
<p>MELD-Na (VA TRANSPLANT LUNG)</p>
<p>MELD-Na (VA TRANSPLANT PANCREAS)</p></td>
</tr>
<tr class="even">
<td>ROR GENERIC DRUG (#799.51)</td>
<td><p><em>Entries new:</em></p>
<p>HIV registry: BICTEGRAVIR/EMTRICITABINE/TENOFOVIR ALAFENAMIDE</p>
<p>HIV registry: EFAVIRENZ/LAMIVUDINE/TENOFOVIR</p>
<p>DISOPROXIL FUMARATE</p>
<p>HIV registry: LAMIVUDINE/TENOFOVIR DISOPROXIL</p>
<p>FUMARATE</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167264007" class="anchor"></span>Table 69 – Software Distributives

### Patch ROR\*1.5\*34

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc167264008" class="anchor"></span>Table 70 – Selecting and Changing Date Elements</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Create three new Local Registries; Lymphoma, Non-Alcoholic SteatoHepatitis (NASH) and Interstitial Lung Disease (ILD). The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>This patch adds the following new medication:</p>
<ul>
<li><blockquote>
<p>HIV registry: COBICISTAT/DARUNAVIR/EMTRICITABINE/TENOFOVIR AF</p>
</blockquote></li>
</ul>
<p>The new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>In the CCR GUI, the “Future Appointments” panel has been added to the following reports for all registries:</p>
<ul>
<li><blockquote>
<p>Diagnoses</p>
</blockquote></li>
<li><blockquote>
<p>Procedures</p>
</blockquote></li>
</ul>
<p>The panel has been added after the “Additional Identifiers” panel and the “Next Appt” column has been added to the report data columns. If the user selects “All patients” then no “Next Appt” column is added.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>On all reports where the “Future Appointments” panel is available, a new “Clinic Name” column has been added to the right of the “Next Appt” column in the report output. If the user selects “All patients” then no “Clinic Name” column is added.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>On the Hepatitis A and Hepatitis B reports, fixed the display on LOINC codes on the report header.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>6</td>
<td>On the Current Inpatient List report, an “Admission Date” column has been added to the left of the “Admitting Diagnosis” column on the report output.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>7</td>
<td>On the Hepatitis A and Hepatitis B reports, the tool tips on the Vaccination Date Range and Immunity Date Range panels have been fixed.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>8</td>
<td>The version of the CCR software is updated to 1.5.34</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc167264008" class="anchor"></span>Table 70 – Selecting and Changing Date Elements

<table>
<caption><p><span id="_Toc167264009" class="anchor"></span>Table 71 – Task Manager Status Column Entries</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DIALOG (#.84)</td>
<td><p><em>Entries modified:</em></p>
<p>7981002.002 Current Inpatient List (CSV)</p>
<p>7981010.002 Registry Lab Tests by Range (CSV)</p>
<p>7981012.001 Combined Meds and Labs (HTML)</p>
<p>7981012.002 Combined Meds and Labs (CSV)</p>
<p>7981013.001 Diagnoses (HTML)</p>
<p>7981013.002 Diagnoses (CSV)</p>
<p>7981015.001 Procedures (HTML)</p>
<p>7981015.002 Procedures (CSV)</p>
<p>7981018.002 BMI Report by Range (CSV)</p>
<p>7981019.002 Liver Score by Range (CSV)</p>
<p>7981020.002 Renal Function by Range (CSV)</p>
<p>7981021.002 Potential DAA Candidates (CSV)</p>
<p>7981024.001 Hepatitis A Report (HTML)</p>
<p>7981024.002 Hepatitis A Report (CSV)</p>
<p>7981025.001 Hepatitis B Report (HTML)</p>
<p>7981025.002 Hepatitis B Report (CSV)</p>
<p>7981997.001 Patient data templates (HTML)</p>
<p>7981999.002 Common XSL templates (CSV)</p></td>
</tr>
<tr class="even">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>Entries New:</em></p>
<p>VA LYMPHOMA</p>
<p>VA NASH</p>
<p>VA ILD</p></td>
</tr>
<tr class="odd">
<td>ROR SELECTION RULE (#798.2)</td>
<td><p><em>Entries New:</em></p>
<p>VA LYMPHOMA PROBLEM</p>
<p>VA LYMPHOMA PROBLEM (ICD10)</p>
<p>VA LYMPHOMA PTF</p>
<p>VA LYMPHOMA PTF (ICD10)</p>
<p>VA LYMPHOMA VPOV</p>
<p>VA LYMPHOMA VPOV (ICD10)</p>
<p>VA NASH PROBLEM</p>
<p>VA NASH PROBLEM (ICD10)</p>
<p>VA NASH PTF</p>
<p>VA NASH PTF (ICD10)</p>
<p>VA NASH VPOV</p>
<p>VA NASH VPOV (ICD10)</p>
<p>VA ILD PROBLEM</p>
<p>VA ILD PROBLEM (ICD10)</p>
<p>VA ILD PTF</p>
<p>VA ILD PTF (ICD10)</p>
<p>VA ILD VPOV</p>
<p>VA ILD VPOV (ICD10)</p></td>
</tr>
<tr class="even">
<td>ROR ICD SEARCH (#798.5)</td>
<td><p><em>Entries New:</em></p>
<p>VA LYMPHOMA</p>
<p>VA NASH</p>
<p>VA ILD</p></td>
</tr>
<tr class="odd">
<td>ROR LIST ITEM (#799.1)</td>
<td><p><em>Entries New:</em></p>
<p>APRI (VA LYMPHOMA)</p>
<p>APRI (VA NASH)</p>
<p>APRI (VA ILD)</p>
<p>BMI (VA LYMPHOMA)</p>
<p>BMI (VA NASH)</p>
<p>BMI (VA ILD)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA LYMPHOMA)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA NASH)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA ILD)</p>
<p>eGFR by CKD-EPI (VA LYMPHOMA)</p>
<p>eGFR by CKD-EPI (VA NASH)</p>
<p>eGFR by CKD-EPI (VA ILD)</p>
<p>eGFR by MDRD (VA LYMPHOMA)</p>
<p>eGFR by MDRD (VA NASH)</p>
<p>eGFR by MDRD (VA ILD)</p>
<p>FIB-4 (VA LYMPHOMA)</p>
<p>FIB-4 (VA NASH)</p>
<p>FIB-4 (VA ILD)</p>
<p>MELD (VA LYMPHOMA)</p>
<p>MELD (VA NASH)</p>
<p>MELD (VA ILD)</p>
<p>MELD-Na (VA LYMPHOMA)</p>
<p>MELD-Na (VA NASH)</p>
<p>MELD-Na (VA ILD)</p></td>
</tr>
<tr class="even">
<td>ROR XML ITEM (#799.31)</td>
<td><p><em>Entries new:</em></p>
<p>FUT_CLIN</p></td>
</tr>
<tr class="odd">
<td>ROR GENERIC DRUG (#799.51)</td>
<td><p><em>Entries new:</em></p>
<p>HIV registry: COBICISTAT/DARUNAVIR/EMTRICITABINE/TENOFOVIR AF</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167264009" class="anchor"></span>Table 71 – Task Manager Status Column Entries

### Patch ROR\*1.5\*35

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc167264010" class="anchor"></span>Table 72 – Report Files</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Create two new Local Registries; Head and Neck Squamous Cell Cancer and Hypothyroidism. The new local registries will be defined using ICD-9 and ICD-10 codes.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>This patch adds the following new medication:</p>
<ul>
<li><blockquote>
<p>HIV registry: DORAVIRINE</p>
</blockquote></li>
<li><blockquote>
<p>HIV registry: DORAVIRINE /LAMIVUDINE/TENOFOVIR</p>
</blockquote></li>
<li><blockquote>
<p>HIV registry: DOLUTEGRAVIR/LAMIVUDINE</p>
</blockquote></li>
</ul>
<p>The new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>3</td>
<td>The two national registries, Hepatitis C and HIV, will now auto-confirm patients like the rest of the registries. At the time of the patch installation, any pending patients will be automatically confirmed setting the confirmation date to the patch installation date and any pending comments for those patients will be deleted.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>The CCR software now supports 2 factor authentication (2FA) and single sign on using the new RPC broker.</td>
<td colspan="2">E</td>
</tr>
<tr class="odd">
<td>5</td>
<td>The CCR help system has been completely re-designed to work with Windows 10.</td>
<td colspan="2">F</td>
</tr>
<tr class="even">
<td>6</td>
<td>The version of the CCR software is updated to 1.5.35</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc167264010" class="anchor"></span>Table 72 – Report Files

<table>
<caption><p><span id="_Toc167264011" class="anchor"></span>Table 73 – Technical Tab Message Icons</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>Entries New:</em></p>
<p>VA HEAD AND NECK</p>
<p>VA HYPOTHYROIDISM</p></td>
</tr>
<tr class="even">
<td>ROR SELECTION RULE (#798.2)</td>
<td><p><em>Entries New:</em></p>
<p>VA HEAD AND NECK PROBLEM</p>
<p>VA HEAD AND NECK PROBLEM (ICD10)</p>
<p>VA HEAD AND NECK PTF</p>
<p>VA HEAD AND NECK PTF (ICD10)</p>
<p>VA HEAD AND NECK VPOV</p>
<p>VA HEAD AND NECK VPOV (ICD10)</p>
<p>VA HYPOTHYROIDISM PROBLEM</p>
<p>VA HYPOTHYROIDISM PROBLEM (ICD10)</p>
<p>VA HYPOTHYROIDISM PTF</p>
<p>VA HYPOTHYROIDISM PTF (ICD10)</p>
<p>VA HYPOTHYROIDISM VPOV</p>
<p>VA HYPOTHYROIDISM VPOV (ICD10)</p></td>
</tr>
<tr class="odd">
<td>ROR ICD SEARCH (#798.5)</td>
<td><p><em>Entries New:</em></p>
<p>VA HEAD AND NECK</p>
<p>VA HYPOTHYROIDISM</p></td>
</tr>
<tr class="even">
<td>ROR LIST ITEM (#799.1)</td>
<td><p><em>Entries New:</em></p>
<p>APRI (VA HEAD AND NECK)</p>
<p>APRI (VA HYPOTHYROIDISM)</p>
<p>BMI (VA HEAD AND NECK)</p>
<p>BMI (VA HYPOTHYROIDISM)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA HEAD AND NECK)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA HYPOTHYROIDISM)</p>
<p>eGFR by CKD-EPI (VA HEAD AND NECK)</p>
<p>eGFR by CKD-EPI (VA HYPOTHYROIDISM)</p>
<p>eGFR by MDRD (VA HEAD AND NECK)</p>
<p>eGFR by MDRD (VA HYPOTHYROIDISM)</p>
<p>FIB-4 (VA HEAD AND NECK)</p>
<p>FIB-4 (VA HYPOTHYROIDISM)</p>
<p>MELD (VA HEAD AND NECK)</p>
<p>MELD (VA HYPOTHYROIDISM)</p>
<p>MELD-Na (VA HEAD AND NECK)</p>
<p>MELD-Na (VA HYPOTHYROIDISM)</p></td>
</tr>
<tr class="odd">
<td>ROR GENERIC DRUG (#799.51)</td>
<td><p><em>Entries new:</em></p>
<p>HIV registry: DORAVIRINE</p>
<p>HIV registry: DORAVIRINE /LAMIVUDINE/TENOFOVIR</p>
<p>HIV registry: DOLUTEGRAVIR/LAMIVUDINE</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167264011" class="anchor"></span>Table 73 – Technical Tab Message Icons

### Patch ROR\*1.5\*36

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                                                                 |     | Type |
|-----|-----------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | Create new Local Registry; COVID-19. The new local registry will be defined using ICD-10 codes.                             | E   |      |
| 2   | The Lab Tests tab of the Edit Site Parameters screen has been fixed to not display the Microsoft Window's control name.     | F   |      |
| 3   | The Registry Meds tab of the Edit Site Parameters screen has been fixed to not display the Microsoft Window's control name. | F   |      |
| 4   | The version of the CCR software is updated to 1.5.36                                                                        | E   |      |

<span id="_Toc167264012" class="anchor"></span>Table 74 – Technical Log Activity Types

<table>
<caption><p><span id="_Toc167264013" class="anchor"></span>Table 75 – Date Range Parameters</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>Entries New:</em></p>
<p>VA COVID19</p></td>
</tr>
<tr class="even">
<td>ROR SELECTION RULE (#798.2)</td>
<td><p><em>Entries New:</em></p>
<p>VA COVID19 PROBLEM</p>
<p>VA COVID19 PROBLEM (ICD10)</p>
<p>VA COVID19 PTF</p>
<p>VA COVID19 PTF (ICD10)</p>
<p>VA COVID19 VPOV</p>
<p>VA COVID19 VPOV (ICD10)</p></td>
</tr>
<tr class="odd">
<td>ROR ICD SEARCH (#798.5)</td>
<td><p><em>Entries New:</em></p>
<p>VA COVID19</p></td>
</tr>
<tr class="even">
<td>ROR LIST ITEM (#799.1)</td>
<td><p><em>Entries New:</em></p>
<p>APRI (VA COVID19)</p>
<p>BMI (VA COVID19)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA COVID19)</p>
<p>eGFR by CKD-EPI (VA COVID19)</p>
<p>eGFR by MDRD (VA COVID19)</p>
<p>FIB-4 (VA COVID19)</p>
<p>MELD (VA COVID19)</p>
<p>MELD-Na (VA COVID19)</p>
<p>Default COVID-19</p>
<p>COVID-19 Virus Tests</p>
<p>COVID-19 Serology Tests</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167264013" class="anchor"></span>Table 75 – Date Range Parameters

### Patch ROR\*1.5\*37

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                                                                                                                                                                   |     | Type |
|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | Create new Local Registry; Recent Patients. The new local registry will be defined using patient admission and visit dates. It will contain only those patients who have been seen in the previous two years at the facility. | E   |      |
| 2   | The VA COVID19 registry which was added with the previous patch, ROR\*1.5\*36, is modified to check Lab tests for positive test results for certain LOINC values.                                                             | E   |      |
| 3   | The version of the CCR software is updated to 1.5.37                                                                                                                                                                          | E   |      |

<span id="_Ref302375747" class="anchor"></span>Table 76 – Local Report Elements

<table>
<caption><p><span id="_Toc167264015" class="anchor"></span>Table 77 – HEPC Registry Selection via ICD-9 CM Diagnostic Codes</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>Entries New:</em></p>
<p>VA RECENT PATIENTS</p>
<p><em>Modified entry:</em></p>
<p>VA COVID19</p></td>
</tr>
<tr class="even">
<td>ROR SELECTION RULE (#798.2)</td>
<td><p><em>Entries New:</em></p>
<p>VA RECENT PATIENTS PTF (VA RECENT PATIENTS)</p>
<p>VA RECENT PATIENTS VISIT (VA RECENT PATIENTS)</p>
<p>VA COVID19 LAB (VA COVID19)</p></td>
</tr>
<tr class="odd">
<td>ROR LAB SEARCH (#798.9)</td>
<td><p><em>Entries New:</em></p>
<p>34 additional LOINCs added to the VA COVID19 entry.</p></td>
</tr>
<tr class="even">
<td>ROR LIST ITEM (#799.1)</td>
<td><p><em>Entries New:</em></p>
<p>APRI (VA RECENT PATIENTS)</p>
<p>BMI (VA RECENT PATIENTS)</p>
<p>Creatinine clearance by Cockcroft-Gault (VA RECENT PATIENTS)</p>
<p>eGFR by CKD-EPI (VA RECENT PATIENTS)</p>
<p>eGFR by MDRD (VA RECENT PATIENTS)</p>
<p>FIB-4 (VA RECENT PATIENTS)</p>
<p>MELD (VA RECENT PATIENTS)</p>
<p>MELD-Na (VA RECENT PATIENTS)</p>
<p>Recent Patients Medications (VA RECENT PATIENTS)</p>
<p>Recent Patients Lab Tests (VA RECENT PATIENTS)</p></td>
</tr>
<tr class="odd">
<td>ROR METADATA (#799.2)</td>
<td><p><em>For file 45 PTF</em></p>
<p>ADMISSION DATE (VA RECENT PATIENTS)</p>
<p><em>For file 9000010 VISIT</em></p>
<p>VISIT/ADMIT DATE&amp;TIME (VA RECENT PATIENTS)</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167264015" class="anchor"></span>Table 77 – HEPC Registry Selection via ICD-9 CM Diagnostic Codes

### Patch ROR\*1.5\*38

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| \#  | Description                                                                                                                                                                                                                                                                                                                                                                                                            |     | Type |
|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|------|
| 1   | The Clinical Case Registries (CCR) identifies patients with positive antibody results for inclusion in the HIV and HCV registries. This patch fixes an error where patients with laboratory results that are not positive are incorrectly categorized as positive and are incorrectly included in the HIV and HCV registries. Code changes have been made to the RORUPD04 and RORX024A routines to rectify this issue. | F   |      |
| 2   | The version of the CCR software is updated to 1.5.38                                                                                                                                                                                                                                                                                                                                                                   | E   |      |

<span id="_Toc167264016" class="anchor"></span>Table 78 – HEPC Registry Selection via ICD-10 CM Diagnostic Codes

| File Name and Number | Update                         |
|--------------------------|------------------------------------|
|                          | No global updates in this release. |

<span id="_Toc167264017" class="anchor"></span>Table 79 – HEPC Registry Selection via LOINC Codes

### Patch ROR\*1.5\*39

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc167264018" class="anchor"></span>Table 80 – HIV Registry Selection via ICD-9 CM Diagnostic Codes</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>The display of Social Security Numbers (SSNs) and the last 4 of the SSN has been removed from all screens and report output (see NOTE below).</p>
<p><strong>NOTE:</strong> In May 2007, Office of Management and Budget (OMB) issued memorandum M-07-16, Safeguarding Against and Responding to the Breach of Personally Identifiable Information, requiring agencies to review their use of Social Security Numbers (SSNs) and to explore alternatives to using SSNs as personal identifiers for Federal employees and in Federal programs.</p></td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>2</td>
<td>The version of the CCR software is updated to 1.5.39</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc167264018" class="anchor"></span>Table 80 – HIV Registry Selection via ICD-9 CM Diagnostic Codes

<table>
<caption><p><span id="_Toc167264019" class="anchor"></span>Table 81 – HIV Registry Selection via ICD-10 CM Diagnostic Codes</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DIALOG (#.84)</td>
<td><p><em>Entries modified:</em></p>
<p>7981010.002 Registry Lab Tests by Range (CSV)</p>
<p>7981011.001 Patient Medication History (HTML)</p>
<p>7981011.002 Patient Medication History (CSV)</p>
<p>7981012.001 Combined Meds and Labs Report (HTML)</p>
<p>7981012.002 Combined Meds and Labs Report (CSV)</p>
<p>7981013.002 Diagnoses (CSV)</p>
<p>7981014.002 Registry Medications Report (CSV)</p>
<p>7981015.001 Procedures (HTML)</p>
<p>7981015.002 Procedures (CSV)</p>
<p>7981018.002 BMI Report by Range (CSV)</p>
<p>7981019.002 Liver Report by Range (CSV)</p>
<p>7981021.002 Potential DAA Candidates (CSV)</p>
<p>7981022.001 DAA Lab Monitoring (HTML)</p>
<p>7981022.002 DAA Lab Monitoring (CSV)</p>
<p>7981023.002 Sustained Virologic Response (CSV)</p>
<p>7981024.002 Hepatitis A Report (CSV)</p>
<p>7981025.002 Hepatitis B Report (CSV)</p>
<p>7981997.001 Patient data templates (HTML)</p>
<p>7981997.002 Patient data templates (CSV)</p>
<p>7981999.001 Common XSL templates (HTML)</p>
<p>7981999.002 Common XSL templates (CSV)</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167264019" class="anchor"></span>Table 81 – HIV Registry Selection via ICD-10 CM Diagnostic Codes

### Patch ROR\*1.5\*40

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc167264020" class="anchor"></span>Table 82 – HIV Registry Selection via LOINC Codes</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch adds the following new medications:</p>
<ul>
<li><blockquote>
<p>HIV registry: CABOTEGRAVIR</p>
</blockquote></li>
<li><blockquote>
<p>HIV registry: CABOTEGRAVIR/RILPIVIRINE</p>
</blockquote></li>
</ul>
<p>The new medications have been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medications.</p></td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>2</td>
<td>The version of the CCR software is updated to 1.5.40</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Toc167264020" class="anchor"></span>Table 82 – HIV Registry Selection via LOINC Codes

<table>
<caption><p><span id="_Toc167264021" class="anchor"></span>Table 83 – List of Local Registries</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR GENERIC DRUG (#799.51)</td>
<td><p><em>Entries new:</em></p>
<p>HIV registry: CABOTEGRAVIR</p>
<p>HIV registry: CABOTEGRAVIR/RILPIVIRINE</p></td>
</tr>
</tbody>
</table>

<span id="_Toc167264021" class="anchor"></span>Table 83 – List of Local Registries

### Patch ROR\*1.5\*41

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref331063624" class="anchor"></span>Table 84 – Local Registries ICD-9 Codes</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch changes the value of the NATIONAL (#.09) field in the ROR REGISTRY PARAMETERS (#798.1) file for two entries:</p>
<ul>
<li><blockquote>
<p>Hepatitis C registry: VA HEPC</p>
</blockquote></li>
<li><blockquote>
<p>HIV registry: VA HIV</p>
</blockquote></li>
</ul>
<p>Before the patch, the value is "1" (i.e., YES).</p>
<p>After the patch, the value is "0" (i.e., NO).</p>
<p>Prior to this patch, these two registries were considered "national" and their patient data was transmitted to a national database every day. All other registries in the package are considered "local" and their patient data is not transmitted to any other database.</p>
<p>With this patch, these two registries are changed to "local" too and their patient data will no longer be transmitted to any other database.</p></td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>2</td>
<td>The version of the CCR software is updated to 1.5.41</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref331063624" class="anchor"></span>Table 84 – Local Registries ICD-9 Codes

<table>
<caption><p><span id="_Ref382479993" class="anchor"></span>Table 85 – Local Registries ICD-10 Codes</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>Entries modified:</em></p>
<p>VA HEPC</p>
<p>VA HIV</p></td>
</tr>
</tbody>
</table>

<span id="_Ref382479993" class="anchor"></span>Table 85 – Local Registries ICD-10 Codes

### Patch ROR\*1.5\*42

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref421020281" class="anchor"></span>Table 86 – Local Registries CPT Codes</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 86%" />
<col style="width: 0%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>#</th>
<th colspan="2">Description</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><p>This patch adds the following new medication:</p>
<ul>
<li><blockquote>
<p>HIV registry: LENACAPAVIR</p>
</blockquote></li>
</ul>
<p>The new medication has been added to the ROR GENERIC DRUG (#799.51) file and can now be selected on reports to provide information about the patients who are taking the new medication.</p></td>
<td colspan="2">M</td>
</tr>
<tr class="even">
<td>2</td>
<td>The VA TRANSGENDER registry is inactivated. The REGISTRY STATUS field (#11) of the ROR REGISTRY PARAMETERS (#798.1) file for this registry is set to 1 (i.e., INACTIVE). The daily update process will no longer update this registry. Also, this registry will no longer appear in the list of registries displayed to the users so they will not be able to select it.</td>
<td colspan="2">M</td>
</tr>
<tr class="odd">
<td>3</td>
<td>The Graphical User Interface (GUI) now supports the latest changes to the RPC Broker package. The latest Personal Identity Verification (PIV) certificate will be selected automatically, however, a new "/showcerts" command line switch was added to allow the user to display the PIV certificate selection screen in case it is needed.</td>
<td colspan="2">E</td>
</tr>
<tr class="even">
<td>4</td>
<td>The version of the CCR software is updated to 1.5.42</td>
<td colspan="2">E</td>
</tr>
</tbody>
</table>

<span id="_Ref421020281" class="anchor"></span>Table 86 – Local Registries CPT Codes

<table>
<caption><p><span id="_Ref54005739" class="anchor"></span>Table 87 – COVID-19 Registry Selection via LOINC Codes</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name and Number</strong></th>
<th><strong>Update</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR REGISTRY PARAMETERS (#798.1)</td>
<td><p><em>Entries modified:</em></p>
<p>VA TRANSGENDER</p></td>
</tr>
<tr class="even">
<td>ROR GENERIC DRUG (#799.51)</td>
<td><p><em>Entries new:</em></p>
<p>HIV registry: LENACAPAVIR</p></td>
</tr>
</tbody>
</table>

<span id="_Ref54005739" class="anchor"></span>Table 87 – COVID-19 Registry Selection via LOINC Codes

## Obtaining Software and Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCR 1.5 software distributives and documentation files are available for downloading from the following locations.

| Name            | Address                   | Directory |
|-----------------|---------------------------|-----------|
| VistA downloads | See CCR Redacted document | software  |

Documentation is also available on the VistA Document Library (VDL) website. See <http://www.va.gov/vdl/application.asp?appid=126>. The documentation set includes:

- *Installation Guide*
- *Release Notes*
- *Technical Manual / Security Guide*
- *User Manual* revision for ROR\*1.5\*42 (this document)

The CCR software and accompanying guides and manuals are distributed as the following set of files:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 55%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Contents</th>
<th>Retrieval Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ROR1_5P42GUI.ZIP</td>
<td><p>Zipped GUI distributive:</p>
<p>► CCRSETUP.EXE</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>ROR1_5P42DOC1.ZIP</td>
<td><p>Zipped DOC distributive, which includes both .PDF and .DOCX formats:</p>
<p>► User Manual (ROR1_5_42UM)</p></td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>ROR1_5P42DOC2.ZIP</td>
<td><p>► Installation Guide (ROR1_5_42IG)</p>
<p>► Technical Manual / Security Guide (ROR1_5_42TM)</p>
<p>► Release Notes (ROR1_5_42RN)</p></td>
<td>BINARY</td>
</tr>
</tbody>
</table>

## Accessibility Features in Clinical Case Registries 1.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Keyboard shortcuts make the CCR GUI accessible to a wide range of users, including those with limited dexterity, low vision, or other disabilities.[^2]

![](ror-1-5-42-user-manual/027.png) See 11.5 below for a complete list of keyboard shortcuts.

## VistA Documentation on the Intranet 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for this product, including all of the software manuals, is available in the VistA Document Library (VDL). The Clinical Case Registries documentation may be found at <http://www.va.gov/vdl/application.asp?appid=126>.

For additional information about the CCR, access the CCR Home Page at the following address: See CCR Redacted document.

Training links and information are also available in the CCR Redacted document.

# About the CCR Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCR acts as a “front-end” application which allows users to access data stored in VistA. It runs on a computer workstation and provides a [graphical user interface](#Glos_GUI) (GUI) which replaces the traditional “[roll’n’scroll](\l)” interface used in VistA.

## Remote Procedure Calls and the Broker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCR uses a protocol known as a [Remote Procedure Call](#Glos_RPC) (RPC). An RPC enables CCR to communicate directly with (*“call”*) VistA to find and display, on the user’s workstation, data stored on another computer (the VistA server).

The RPC Broker is “helper” software that allows a computer program to make remote procedure calls from one computer to another, via a network. The Broker establishes a common and consistent foundation for client/server applications written under the VistA umbrella. The Broker acts as a bridge connecting the client application front-end on the workstation (in this case, CCR) to the M-based data and business rules on the server. It serves as the communications medium for messaging between VistA client/server applications. Upon receipt, the message is decoded, the requested remote procedure call is activated, and the results are returned to the calling application. Thus, the Broker helps bridge the gap between the traditionally proprietary VA software and other types of software.

In order to use CCR, the user must have a special kind of VistA option (called a B-type option) assigned on the primary or secondary VistA menu. This option is designed to be run only by the RPC Broker, and cannot be run from the menu system.

Use of CCR also requires that the list of RPC Broker servers which the user is authorized to access be maintained on the workstation. The RPC Broker server to be used is defined by executing the program serverlist.exe, which is described in the RPC Broker *Systems Manual* (revised 2005-02-28), which is also available on the VDL. Both xwb1_1ws.exe and serverlist.exe, which are mentioned in those manuals, are distributed as part of the Broker.

See also <http://www.hardhats.org/cs/broker/docs/xwb1_1rn.html> for more helpful information about installing and configuring ServerList.exe.

## Graphical User Interface Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCR uses a graphical user interface (GUI) similar to those used in many Microsoft Windows® or Apple Macintosh® programs. If you have already used programs on these platforms, the CCR GUI will seem familiar to you. CCR is only implemented on the Microsoft Windows platform at this time.

If you have little or no familiarity with the Microsoft Windows GUI environment, information can be found by accessing the Microsoft Windows Help file. Additionally, brief descriptions of the GUI features used in the CCR application are provided in the following sections.

### Windows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An “application window” is the area on your computer screen used by a program. If you have more than one program running at the same time, you can go from one program to another by clicking in each application window. You can also move, close, or minimize the application window to make room for another window. (See Help in Windows for further instructions on these functions.)

The CCR uses the [Multiple Document Interface](#Glos_MDI) (MDI). Several “child” windows can be open inside the main “parent” application window at the same time. A child window either provides access to a registry (such as CCR:HIV or CCR:HEPC) or contains a document (such as a report). You can switch between these windows using the Windows menu or [keyboard shortcuts](#clinical-case-registries-shortcut-keys).

### Pop-up Windows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These are “miniature” windows that pop up within a window to provide or request information. Ordinarily, they require some action before they will disappear. Clicking on buttons with the words \[OK\], \[Cancel\], \[Exit\], or something similar usually closes these windows. Sometimes, they can be closed by pressing the \< Esc \> key.

### Windows GUI Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe typical Windows GUI elements.

### Text Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/028.png) Type the desired characters into the text (edit) box. The selected entry will not be effective until you tab away from or otherwise exit from the text box.

### Checkbox

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A checkbox toggles between a YES/NO, ON/OFF setting. It is usually a square box containing a check mark    or X  X . Clicking the box or pressing the spacebar toggles the checkbox setting. In some instances, checkboxes may be used to provide more than one choice; in such cases, more than one box can be selected. Sometimes, a pre-determined “default” entry will be made for you in a checkbox; you can change the default if needed.

### Radio button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/029.png)A radio button, also known as an option button, is a small, hollow circle adjacent to text. Radio buttons appear in sets. Each button represents a single choice and normally only one button may be selected at any one time. Clicking on the radio button places a solid dot in the circle, selecting the option. Clicking a selected radio button de-selects it, removing the dot. As one radio button is selected, others within the category switch off. For example, Male or Female may be offered as choices through two radio buttons, but you can only select one of the choices.

### Command buttons and Command icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/030.png)</p>
<p>![](ror-1-5-42-user-manual/031.png)</p>
<p>![](ror-1-5-42-user-manual/032.png)</p>
<p>![](ror-1-5-42-user-manual/033.png)</p></th>
<th><p>A command button initiates an action. It is a rectangular “3-dimensional” shape with a label that specifies what action will be performed when the button is clicked. Common examples are shown at left. Command buttons that end with three dots indicate that selecting the command may evoke a subsidiary window.</p>
<p>In some cases, a command icon performs the same function, but appears on the menu bar and has a plain, flat appearance. One example is shown at left.</p>
<p>In the text of this document, both command button and command icon names appears inside square brackets. <em>Examples:</em> [Search], [Save].</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Date field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The date field is identified by “\_\_/\_\_/\_\_” or a date format like “mm/dd/yyyy” and will usually have an associated popup calendar (see Pop-up Calendars). The month and day components of the date must consist of two digits and the year must consist of four digits (*e.g.*, 02/02/1996). The selected entry will not be effective until you tab away from or otherwise exit the date field.

### Drop-Down List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/034.png) A drop-down list is displayed as a box with an arrow button on the right side. Such boxes usually display one entry at a time. Choose from a vertical list of choices that display when you click the downward arrow. Select the entry you want by clicking the list entry.

If None is the last entry, selecting it will clear the list entry. If More… is the last entry, selecting it will display additional options. The selected entry will not be effective until you tab away from or otherwise exit the drop-down list.

### List Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/035.png)The list box shows a list of items. If more items exist than can be seen in the box, a scroll bar appears on the side of the box. Click the desired entry to select it from the list.

### Faded (“Grayed Out”) Choices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/036.png) | Fields or choices (as in list boxes) that appear with faded letters (“grayed out”) are currently unavailable, meaning they cannot be selected. |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|

### Keyboard Commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/037.png) | Keyboard commands can be used throughout the CCR application by pressing and holding the \< Alt \> key and then pressing the appropriate key to perform the command. The key to press in order to perform the command is identified by an underlined character on the screen. For example, the Task Manager tab can be displayed by pressing and holding the \< Alt \> key and then pressing the \< T \> key. |
|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Keyboard keys and onscreen buttons are shown in different style brackets throughout this manual to differentiate them from on-screen buttons or menu options: \< Ctrl \> and \< Enter \> are on the keyboard, \[Close\] is a command button or icon on the screen.

![](ror-1-5-42-user-manual/038.png) See 11.5 below for a complete list of keyboard shortcuts.

### Fields with Non-White Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Items in fields that appear with a non-white background can be selected— but cannot be modified directly in that field.

![](ror-1-5-42-user-manual/039.png)

### Tab Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the \< Tab \> key or the mouse to move between fields. Do *not* use the \< Enter \> or \< Return \> key, which is usually reserved for the default command button or action.

### Changing (Resizing) a Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most windows and columns displayed in the CCR application can be resized. To change the size of a window, position the mouse pointer over the right edge of the column or the outside edge of the window, left click, and while holding the mouse button down, move the mouse and “drag” to change the size of the window or column. Position the mouse pointer over one corner and drag diagonally to increase the size of the entire window.

| ![](ror-1-5-42-user-manual/040.png) | Note: In CCR, changes to the window and column sizes are maintained in subsequent sessions. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|

| ![](ror-1-5-42-user-manual/041.png) | Note: Also see Figure 1 – Resizing the Screen for tips on how to maximize or minimize windows using the keyboard. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|

### Cancel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When used in a prompt, Cancel allows you to cancel the action about to be taken. For example, when closing an application, you may be prompted to validate the action to close. If you click the \[Cancel\] button, the application will not close and you will resume from the point at which the close action was initiated.

### Close

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This command closes the active window. CCR uses a window-within-a-window display. The main application window is the Clinical Case Registries (CCR) window, and the CCR:HEPC or CCR:HIV window is displayed in the child window.

Close the active registry window:

- by selecting Close from the File menu
- by pressing and holding the \< Ctrl \> key and then pressing \< F4 \>
- by clicking on the X in upper right corner of the child window
- in report setup windows and pop-ups, by pressing the \< Esc \> key

Close and exit the CCR application:

- by selecting Exit from the File menu
- by pressing and holding the \< Alt \> key and then pressing the \< F4 \> key
- by clicking on the X in the upper right corner of the main application window

### Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This command is used to edit information.

### Find

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This command is used to find an entry. Enter the search string and click \[OK\]. Note that many searches are case-sensitive and that most searches are “begins with” (rather than “contains”) searches.

### Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides generalized help on the application, or specialized help for the area in which you are currently working. The CCR application has an online help file; while running the application, press the \< F1 \> key to access help.

### OK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirms the input and initiates the action defined by the window.

### Save

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Saves all changes made since the last save action. If you attempt to save and all required fields have not yet been completed, you will receive notification that the required fields must be completed before saving.

### Save As

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This command is used to export to a file a report produced in CCR. With the report open, clicking on the Save As… menu option will produce a save dialog window labeled “Save the report as.” Indicate the file location (folder) where you wish to store the report, name the file and choose the format in which it will be saved.

### Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When at least one character is typed in a lookup dialog box, clicking the \[Search\] button will bring up matching entries. In many cases, leaving the lookup box blank will find all such records.

### Selecting Multiple Items from a List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout the CCR application, a variety of lists are available from which you may select one or more items.

To select all items in a range between two separate entries, hold the \< Shift \> key and click on the first item in the range, and then click the last item in the range. The first and last item, as well as all of the items between, will be highlighted.

To select multiple separate entries from a list, hold the \< Ctrl \> key and click each of the items you want to select. In some cases, the number of such items that can be selected may be limited.

### Undo

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Undoes all changes made since the last save action and redisplays the original data.

### Right-Click Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most Windows-based applications provide some sort of pull-down menu (often called a “context menu”) when you click the right mouse button over a GUI element.

| *Example:* | ![](ror-1-5-42-user-manual/042.png) |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------|

Depending upon which CCR window is open (which is where the term “context menu” comes from), the following right-click menu options will be available:

| Window               | Right-Click Menu Options                                  |
|----------------------|-----------------------------------------------------------|
| Task Manager tab | New Report, Open Report, View Report, Delete, Refresh     |
| Registry tab     | CDC… *(in* CCR*:HIV only)*, Confirm/Edit…, Delete         |
| Reports window   | Back, Forward, Cancel, Copy, Select All, Text Size, Find… |

### Pop-up Calendars

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pop-up calendars are used throughout the CCR application. The default date display is usually the current date. The default date is highlighted with a red circle.

| *Example:* | ![](ror-1-5-42-user-manual/043.png) |
|------------|-----------------------------------------------------------------------------------------------------------------------------------|

You can select or change the date displayed on the calendar using the methods described in the following table:

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>To Select/Change…</th>
<th>Do this:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Month</strong></td>
<td><p>![](ror-1-5-42-user-manual/044.png)</p>
<p>Click on the month at the top of the calendar to display a list of all months, and then select one.</p>
<p>Or, you can change one month at a time by clicking the left ![](ror-1-5-42-user-manual/045.png) and right ![](ror-1-5-42-user-manual/046.png) arrow buttons.</p></td>
</tr>
<tr class="even">
<td><strong>Day</strong></td>
<td><p>Click the actual day of the week on the calendar.</p>
<p>To select today's date, click the highlighted (circled) date on the calendar display.</p></td>
</tr>
<tr class="odd">
<td><strong>Year</strong></td>
<td><p>Click on the year. Up and down arrow buttons display for you to increase or decrease the year.</p>
<p>![](ror-1-5-42-user-manual/047.png)</p></td>
</tr>
</tbody>
</table>

Also see [Navigating the Date Picker Calendar Pop-ups](#navigating-the-date-picker-calendar-pop-ups) for information on how to use the keyboard for calendar controls.

### System Timeout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you connect to the database, the application extracts the timeout value assigned to you and applies it as the application timeout value. If no value is assigned, the default value of 60 minutes will be used.

If there is no keyboard or mouse activity during the timeout period, the “Application Time Out” message window (similar to the example screen below) displays for 15 seconds. If there is still no activity within 15 seconds, the application automatically closes; a countdown of seconds remaining is displayed.

![](ror-1-5-42-user-manual/048.png)

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access CCR, you must have a valid VistA account and must be assigned at least one of the following VistA [security keys](#Glos_SecurityKeys):

- ROR VA GENERIC USER or ROR VA GENERIC ADMIN
- ROR VA HIV USER or ROR VA HIV ADMIN
- ROR VA HEPC USER or ROR VA HEPC ADMIN
- ROR VA IRM

USER: Users with the ROR VA HIV/HEPC USER key will be displayed on the Show Registry Users window as “User.”

> ![](ror-1-5-42-user-manual/049.png) *Users* will be able to run reports for the specified registry. The ROR VA GENERIC USER key grants the user access to any local registries added in Patch18 and any subsequent patches.

ADMIN: Users with the ROR VA HIV/HEPC ADMIN key will be displayed on the Show Registry Users window as “Administrator.”

> ![](ror-1-5-42-user-manual/050.png) *Administrators* will have full GUI access that will enable them to run reports, create local fields, and edit, confirm and delete patient records for the specified registry. The ROR VA GENERIC ADMIN key grants the user administration access to any local registries added in Patch18 and any subsequent patches.

IRM: Users with the ROR VA IRM key will be displayed on the Show Registry Users window as “[IRM](#Glos_IRM).”

> ![](ror-1-5-42-user-manual/051.png) *IRM users* will have access to all CCR files in VistA but no access to the GUI. This key should be assigned to the IRM personnel authorized to maintain and troubleshoot the CCR package.

If any unauthorized users access this system, a VA alert will be sent to persons identified to receive registry notifications stating the date and time of the violation and the name of the user who attempted to access the system; a record of the access violation will be written to the Access Violations folder of the Technical Log.

## Assistive Technology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some of the current features of the CCR navigation may not be intuitive if you are using assistive technology (for example, a screen reader like [JAWS](#Glos_JAWS)). In addition to using the mouse, each function may also be selected by using keystrokes; these keystrokes are identified in the discussions which follow.

### Using the \< Alt \> and \< Esc \> Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In many situations, pressing \< Alt \> + a letter that represents the function will perform a function (for example, \< Alt \>+\< P \> activates the Re<u>p</u>orts menu).

\< Alt \>+\< F4 \> closes the screen (and, in most cases in CCR, closes the application as well).

\< Esc \> often may be used to close dialog boxes and pop-ups.

### Resizing the Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instead of clicking the Maximize ![](ror-1-5-42-user-manual/052.png) button, you can press \< Alt \>+\< space \> and then select Ma<u>x</u>imize by pressing \< x \>. If you wish to minimize the screen, you may press \< Alt \>+\< space \> and then select Mi<u>n</u>imize by pressing \< n \>.

![](ror-1-5-42-user-manual/053.png)

<span id="_Ref259173608" class="anchor"></span>Figure 1 – Resizing the Screen

### Changing the Screen Colors and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See 7.11.3 below for information on changing screen colors and options for improved accessibility.

### Windows Accessibility Shortcuts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Windows operating system offers a number of accessibility shortcuts which can be useful. These are “toggled” options, meaning that you perform the specified action once to turn the option on and then again to turn it off. You should be aware, however…

| ![](ror-1-5-42-user-manual/054.png) | Warning: Using some of these options will drastically change the way your computer keyboard functions. If all else fails, reboot your computer to clear any such selections. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Each option will produce a popup confirmation window like those pictured below. Each of these confirmation pop-ups has the same two choice buttons, in this order left to right: \[Yes\] and \[No\]. \[Yes\] is always the default choice.

## StickyKeys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

StickyKeys lets you use the \< Shift \>, \< Ctrl \> or \< Alt \> keys by pressing one key at a time, rather than having to press these keys in conjunction with another key.

Press \< Shift \> five times to toggle StickyKeys on and off:

![](ror-1-5-42-user-manual/055.png)

<span id="_Toc167263767" class="anchor"></span>Figure 2 – Turning on StickyKeys

## FilterKeys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FilterKeys causes Windows to ignore brief or repeated keystrokes and slows down the keyboard repeat rate.

Press down and hold the right-hand \< Shift \> key for eight seconds to toggle FilterKeys on and off:

![](ror-1-5-42-user-manual/056.png)

<span id="_Toc167263768" class="anchor"></span>Figure 3 – Turning On FilterKeys

## ToggleKeys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ToggleKeys causes a tone to sound when you press the \< Caps Lock \>, \< Num Lock \>, or \< Scroll Lock \> keys.

Press down and hold the \< Num Lock \> key for five seconds to turn ToggleKeys on and off:

![](ror-1-5-42-user-manual/057.png)

<span id="_Toc167263769" class="anchor"></span>Figure 4 – Turning On ToggleKeys

## MouseKeys 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MouseKeys lets you control the mouse pointer by using the numeric keypad on your keyboard.

Press the left-hand \< Alt \> key plus the left-hand \< Shift \> key plus the \< Num Lock \> key to toggle MouseKeys on and off:

![](ror-1-5-42-user-manual/058.png)

<span id="_Toc167263770" class="anchor"></span>Figure 5 – Turning On MouseKeys

## HighContrast

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HighContrast improves readability for people with visual impairments by applying a special system color scheme and font size.

Press the left-hand \< Shift \> key plus the left-hand \< Alt \> key plus the \< Print Screen \> key to toggle HighContrast on and off:

![](ror-1-5-42-user-manual/059.png)

<span id="_Toc167263771" class="anchor"></span>Figure 6 – Turning on HighContrast

### Tab Order on Report Setup Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the various report setup screens, the tab order, the order in which screen elements are selected when you press the \< Tab \> key, is as follows and as shown in Figure 7. The general flow is top-left of the screen to the bottom-right of the screen. The List of Registry Patients report setup screen is shown as an example and may not contain all the elements listed below.

The tab position cycles through each option, beginning with:

1.  Scheduled to Run on Pane:

> Day field \| Time field \| Repeat field

> Comment field

2.  Birth Sex Pane:

> Both radio button \| Female Only radio button \| Male Only radio button

3.  Age Range Pane:

> The drop-down list is selected with the default of All.

> Current Age drop-down list \| From field \| To field

> Date of Birth drop-down list \| From field (date picker) \| To field (date picker)

4.  OEF/OIF Pane:

> All periods of service radio button \| Include only OEF/OIF radio button \| Exclude OEF/OIF radio button

5.  SVR Pane:

> All Patients radio button \| SVR Only radio button \| No SVR radio button

6.  Additional Identifiers Pane:

> Include Patient ICN in the report checkbox \| Include PACT Team in the report checkbox \| Include PCP in the report checkbox

7.  Include Patients confirmed in the registry Pane:

> Before the date range checkbox \| During the date range checkbox \| After the date range checkbox

8.  Report Type Pane:

> Complete radio button \| Summary radio button

9.  \[Result Name\] Date Range Pane:

> The Year drop-down list is selected. The tab following that is the Year field, and then the Fiscal check box.

> Year drop-down list \| Year field \| Fiscal checkbox

> Quarter drop-down list \| Year field \| Fiscal checkbox \| Quarter drop-down list (I, II, III, IV)

> Custom drop-down list \| Start Date field (date picker) \| End Date field (date picker)

> Cutoff drop-down list \| Cutoff Date field

10. Result Ranges checkboxes (if more than one, in order from top to bottom):

> Most recent radio button \| as of radio button \| as of date field

11. Other Diagnoses Pane:

> Ignore radio button

> Include Codes radio button

> Exclude Codes radio button

> Template Type selection field (only if Include Codes is selected)

> Template names (only if Include Codes is selected and a Template Type chosen)

12. Other Registries Mode selection field (must click or press \< Space \> and then click down arrow or press \< Down \> button to access drop-down list). Only available if you have access to Other Registries.
13. Local Fields Mode selection field (must click or press \< Space \> and then click down arrow or press down \< Down \> button to access drop-down list). Only available if the site has created Local Fields.
14. \[<u>L</u>oad Parameters\] button
15. \[<u>S</u>ave Parameters\] button
16. \[<u>D</u>efault Parameters\] button
17. \[<u>R</u>un\] button
18. \[Cancel\] button

![](ror-1-5-42-user-manual/060.png)

<span id="_Ref248562621" class="anchor"></span>Figure 7 – Report Setup Screen Tab Order

### Activating Drop-Down Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can activate drop-down lists from the keyboard. Simply tab to the drop-down list field and press \< F4 \> or \< Alt \>+\<  \> (“Alt” key plus the down arrow key).

### Navigating the Date Picker Calendar Pop-ups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the date selection pop-up calendars (known as “date pickers”) may be somewhat problematic for those using screen readers such as [JAWS](#Glos_JAWS). The pop-up date picker calendar is essentially a graphic, rather than text, feature. Although it’s designed for quick navigation using the mouse, the following keys can also be used to navigate the calendar pop-ups:

- \< F4 \> or \< Alt \>+\<  \> (“Alt” key plus the down arrow key) can be used to display the drop-down calendar.
- \< Page Up \> displays the previous month.
- \< Page Down \> displays the following month.
- \< Ctrl \>+\< Page Up \> displays the same month in the previous year.
- \< Ctrl \>+\< Page Down \> displays the same month in the following year.
- \< Arrow \> keys (left, right, up, down) change the day of the month. If you continue to arrow up, down, left or right, the month will eventually change accordingly.
- \< Ctrl \>+\< Home \> jumps to the first day of the month.
- \< End \> jumps to the last day of the month displayed.
- \< Enter \> selects date chosen and closes the pop-up.
- \< Esc \> closes the pop-up without making a selection (but remember that you must make a selection before you can proceed to the next step).

### Dual-List Controls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCR contains a number of “dual-list” controls. For example, a list of “available” names (of drugs, etc.) may be displayed on the left side of such a control.

You may choose one or more of the names and move it to the “selected” list on the right side of the control by clicking a right-pointing arrow command icon in the center between the two lists, or the double right-pointing arrow to move all the names to the selected list.

Likewise, you may choose a selected name and remove it from the selected list by clicking a left-pointing arrow command icon, or click the left-pointing double arrow to remove all of the names from the selected list.

Effective with CCR 1.5.13, you may use \< Enter \> instead of the command icons to move individual names from one list to the other.

In addition, when a dual-list control is selected and a screen reader is active:

- The column header for the left-hand list is changed to Available Name and the right-hand column header is changed to Selected Name.
- The left- and right-pointing arrows and double arrows are changed to words (Add, Remove, Add All and Remove All).

### Row and Header Information in Grids

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In any data table or grid (where rows and columns are displayed)…

- \< Insert \>+\<  \> (“Insert” key plus the down arrow key) will cause JAWS to say the current row and header information. See your JAWS manual for more information.

### Context-Sensitive Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- \< Shift \>+\< F10 \> will display context-sensitive menus where appropriate.

# Local Registry Population and Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Initial Data Load 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Initial creation of the CCR patient lists were based on the patient lists in the CCR:ICR and CCR:HEPC Registries.

## Population of the Local Registry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This method of populating the local registry will occur during each of the automatic nightly updates.

The CCR application searches inpatient files (#45 PTF), outpatient files (#9000010 VISIT), and the problem list (#9000011 PROBLEM)to identify patients with registry-specific ICD codes, and searches the laboratory files (#63 LAB DATA) for positive registry-specific antibody test results. These ICD codes and antibody tests are defined for each registry. As CCR recognizes the earliest instance of data that indicates a positive result, it adds the patient to the registry.

If review of a patient indicates that the patient is not truly infected– for example, the coding was done in error– the patient should be deleted from the registry. After this action is taken for a patient, the software will not again select the same patient based on the same data. If there are multiple instances of erroneous coding for the same patient, the system will recognize the subsequent instance of such coding and again add the patient to the registry. Local facilities should take appropriate action to correct any miscoding identified in the record.

In the event that a patient is confirmed in the registry and later information reveals that the patient is not positive for the monitored condition, that patient should be deleted from the registry.

| ![](ror-1-5-42-user-manual/061.png) | Note: See section titled [Note on Pending Patients](#note-on-pending-patients) for more information. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|

## Deceased Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A check of the Patient file \[#2\] will be performed for each patient in the local registry to validate whether or not the patient is deceased. If a registry coordinator becomes aware of a patient death that is not reflected in the record, he or she should contact the appropriate Medical Administration Service (MAS) or Decedent Affairs staff to have the death recorded in the system.

# Signing On and Opening a Clinical Case Registry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to the registries is obtained through the Clinical Case Registries package. You must first sign on to the CCR to open these registries.

You can sign onto CCR after the application has been added to your Computerized Patient Record System (CPRS) Tools menu or installed on your workstation and you have been assigned a security key by your local Automated Data Processing Application Coordinator (ADPAC) or Information Security Officer (ISO).

To start the CCR application, follow these steps:

1.  ![](ror-1-5-42-user-manual/062.png) Select CCR from your Tools menu within CPRS, or double-click the CCR shortcut on your desktop.

| ![](ror-1-5-42-user-manual/063.png) | Note: The first time you run the program from a shortcut, especially if you are working from a remote location, you may see the following or a similar warning. This is a Microsoft Windows message, wanting to know if you wish to permit the CCR application permission to “break though” the Windows [firewall](#Glos_firewall) in order to make the connection to the server. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![](ror-1-5-42-user-manual/064.png)

<span id="_Toc167263773" class="anchor"></span>Figure 8 – Windows Security Warning

2.  ![](ror-1-5-42-user-manual/065.png) Click the \[<u>U</u>nblock\] button.

> After you unblock the program (if necessary), the Connect To window displays:

> ![](ror-1-5-42-user-manual/066.png)

<span id="_Toc167263774" class="anchor"></span>Figure – Connect To Pop-up

> If you are launching CCR from CPRS Tools, the correct account information will automatically appear. If you are launching CCR from a desktop icon, you may need to ask your IRM support person for the account information to enter.

| ![](ror-1-5-42-user-manual/067.png) | Note: The Connect To window appears only if the site has multiple servers; otherwise the VistA Sign-on window automatically displays as shown in step 2. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|

3.  Click \[OK\].

> After connecting to the appropriate account, the VistA Sign-on window opens.

> ![](ror-1-5-42-user-manual/068.png)

<span id="_Toc167263775" class="anchor"></span>Figure 10 – VistA Sign-on Window

> Type your access code into the Access Code field and press \< Tab \> (or click in the Verify Code field).

| ![](ror-1-5-42-user-manual/069.png) | Note: If you launch CCR from CPRS Tools and your workstation is configured for [Clinical Context Object Workgroup](#Glos_CCOW) standard (CCOW) and Single Sign-On, the VistA Sign-on window will not open at this point. You will be automatically signed in to CCR using your CPRS access code and verify code. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](ror-1-5-42-user-manual/070.png) | Note: You may also type both the access code followed by a semicolon \< ; \> and then the verify code in the Access Code box. After you have done this, press \< Enter \> or click \[OK\]. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

4.  Type your verify code into the Verify Code field and press \< Enter \> or click \[OK\]. The Select a Registry window opens.

![](ror-1-5-42-user-manual/071.png)

<span id="_Toc167263776" class="anchor"></span>Figure 11 – Select a Registry Pop-up

5.  Click a registry name to select it, and then click \[OK\].

> The selected registry opens in the main CCR window. If you have access to only one registry, it will open automatically.

> You can also set up your desktop shortcut to specify which registry is to open automatically.

> ![](ror-1-5-42-user-manual/072.png) See 11.6 below for information on command-line switches for use in the shortcut.

# Registry Window Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Registry Window Menus are displayed in the menu bar near the top of the window. The menus are <u>F</u>ile, Registr<u>y</u>, Re<u>p</u>orts, <u>W</u>indow, and <u>H</u>elp.

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/073.png)</th>
<th rowspan="2"><p>![](ror-1-5-42-user-manual/074.png)</p>
<p><span id="_Toc167263777" class="anchor"></span>Figure 12 – Sample Menu Drop-Down List</p></th>
</tr>
<tr class="odd">
<th>When you click one of these, a list of menu options (a “drop-down” list) is displayed. Note that although the same menu list is presented throughout the session, the choices available from the drop-down list may vary depending on which registry is in use, which operation is being carried out at the time, and which role(s) you are assigned.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## File Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The File Menu displays the following menu options (note how some options may be “grayed out”):

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/075.png)</p>
<p><span id="_Toc167263778" class="anchor"></span>Figure 13 – File Menu Drop-Down List</p></th>
<th><ul>
<li><p><u>O</u>pen Registry</p></li>
</ul>
<ul>
<li><p>Save As… | Save As…</p></li>
<li><p>C<u>l</u>ose</p></li>
<li><p>Close All</p></li>
<li><p>Page Setup or Page Setup</p></li>
<li><p>Print Preview… | Print Preview…</p></li>
<li><p>Print… | Print…</p></li>
<li><p>Preferences</p></li>
<li><p>Rejoin Clinical Context | Rejoin Clinical Context</p></li>
<li><p>Break the Clinical Link | Break the Clinical Link</p></li>
<li><p>E<u>x</u>it</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### File \| Open Registry menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The <u>F</u>ile, <u>O</u>pen Registry menu option is used to open a CCR session. More than one CCR session can be opened at the same time. The registry displayed is named in the blue bar located at the top of the window.

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">![](ror-1-5-42-user-manual/076.png)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>When you first run the application, you may be asked which registry you wish to use (see right). To view the number and type of all open sessions, or to select another open session to view, go to the Window Menu.</p>
<p>The selected registry opens in the main CCR window. If you have access to only one registry, it will open automatically.</p>
<p><strong>Note:</strong> The figure to the right is an example of the Select a Registry screen and may not display all the registries available.</p></td>
<td><p>![](ror-1-5-42-user-manual/077.png)</p>
<p><span id="_Toc167263779" class="anchor"></span>Figure 14 – Select a Registry Pop-up</p></td>
</tr>
<tr class="even">
<td colspan="2"><p>You can also set up your desktop shortcut to specify which registry is to open automatically.</p>
<p>![](ror-1-5-42-user-manual/078.png) See 11.6 below for information on command-line switches for use in the shortcut.</p></td>
</tr>
</tbody>
</table>

### File \| Save As menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/079.png)</p>
<p><span id="_Toc167263780" class="anchor"></span>Figure 15 – File | Save As menu option</p></th>
<th>The Save As menu option on an active report window opens a window used to export reports produced in CCR. This menu option will be unavailable (“grayed out”) when the active window is not a report.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### File \| Close and Close All menu options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/080.png)</p>
<p><span id="_Toc167263781" class="anchor"></span>Figure 16 – File | Close &amp; Close All menu options</p></th>
<th>The Close menu option closes only the active window that is displayed. The Close All menu option closes all child windows listed in the Window Menu.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### File \| Page Setup, Print Preview, and Print menu options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/081.png)</p>
<p><span id="_Toc167263782" class="anchor"></span>Figure 17 – File | Page Setup &amp; Print menu options</p></th>
<th><p>These options are available only when a report is selected as the active window.</p>
<p>The Page Setup menu option launches the Page Setup window from which you can set margins, paper source, paper size, page orientation, and other layout options.</p>
<p>The Print Preview menu option will show how the file will appear when you print it.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The Print menu option opens the Print window from which you can print the active document and select printing options.

These three menu options are normally used to format and print reports from the registry data. They will be unavailable (“grayed out”) when the active window is not a report.

### File \| Preferences menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/082.png)</p>
<p><span id="_Toc167263783" class="anchor"></span>Figure 18 – File | Preferences menu option</p></th>
<th>The Preferences… menu option allows you to customize general and appearance-related settings that affect the CCR window and its behavior.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### File \| Rejoin Clinical Context menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 29%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/083.png)</p>
<p><span id="_Toc167263784" class="anchor"></span>Figure 19 – File | Rejoin Clinical Context menu option</p></th>
<th colspan="2"><p>This menu option enables you to participate in a CCOW Clinical Context and synchronize your CCR clinical data with other CCOW-compliant applications. For example, when CCR and CPRS are both open and are sharing a context, if you change to a different patient in one application, the other application will change to that patient as well.</p>
<p>If CCOW is installed, then by default, the CCOW link is automatically active. You can tell whether CCOW is running by observing the bottom right-hand corner of the CCR window.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>![](ror-1-5-42-user-manual/084.png) In the illustration at right, CCOW is not active, and the user has right-clicked the “no” symbol to display the options, which are grayed-out in this sample:</p>
<ul>
<li><blockquote>
<p>Rejoin and Use Application Data</p>
</blockquote></li>
<li><blockquote>
<p>Rejoin and Use Global Data</p>
</blockquote></li>
<li><blockquote>
<p>Break the Clinical Link</p>
</blockquote></li>
</ul>
<p>If CCOW were active, these options would be available for the user.</p></td>
<td>![](ror-1-5-42-user-manual/085.png)</td>
</tr>
</tbody>
</table>

### File \| Break the Clinical Link menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/086.png)</p>
<p><span id="_Toc167263785" class="anchor"></span>Figure 20 – File | Break the Clinical Link menu option</p></th>
<th>When a CCOW Clinical Context link is active (allowing you to work on two different patients when multiple CCOW-compliant applications are open), this menu option enables you to discontinue the link. For example, if CCR and CPRS are both open and you would like to open a different patient file in each application, select Break the Clinical Link to de-synchronize the clinical data.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### File \| Exit menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/087.png)</p>
<p><span id="_Toc167263786" class="anchor"></span>Figure 21 – File | Exit menu option</p></th>
<th><p>The Exit menu option is used to close the CCR application and all open sessions. You will be prompted to confirm this selection:</p>
<p>![](ror-1-5-42-user-manual/088.png)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Registry Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clicking on Registry automatically takes you to the Registry tab and displays the following menu options:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/089.png)</p>
<p><span id="_Toc167263787" class="anchor"></span>Figure 22 – Registry Menu Drop-Down List</p></th>
<th><ul>
<li><p>Edit… | Edit… or Confirm… | Confirm… (depending on circumstances; see below)</p></li>
<li><p>CDC… (only if CCR:HIV is open)</p></li>
<li><p>Show Registry Users…</p></li>
<li><p>Edit Site Parameters…</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Registry \| Confirm/Edit menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/090.png)</p>
<p><span id="_Toc167263788" class="anchor"></span>Figure 23 – Registry | Confirm/Edit menu option</p></th>
<th>This menu option will appear as Confirm… or Edit… depending on which patient is selected. If you select a patient with a status of Pending, the Confirm… menu option will allow you to open the patient record and verify that the patient does or does not belong in the registry. If you select a patient who has already been confirmed in the registry, the Edit… menu option allows you to update the patient’s record. If you have not yet selected a patient, the option will be unavailable ("grayed-out").</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Registry \| CDC menu option (CCR:HIV only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If CCR:HIV is open, and at least one patient has been found, clicking this option opens a window designed according to the CDC case report form. Select information already in the system (demographic data) is automatically inserted into the form. For information on the CDC form, see page [174](#cdc-window).

### Registry \| Show Registry Users menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/091.png)</p>
<p><span id="_Toc167263789" class="anchor"></span>Figure 24 – Registry | Show Registry Users menu option</p></th>
<th>This menu option displays the Users of the Registry window. From this window, you can view the names of CCR users, their Internal Entry Number (IEN), and the type(s) of user access granted to each user.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CCR users can be granted one or more of the following types of access:</p>
<ul>
<li><p>User – can generate reports but not enter/ edit patient data</p></li>
<li><p>Admin – can enter/edit patient data or registry parameters and generate reports</p></li>
<li><p>IRM – can install, remove or change programming</p></li>
</ul></th>
<th><p>![](ror-1-5-42-user-manual/092.png)</p>
<p><span id="_Toc167263790" class="anchor"></span>Figure 25 – Registry Users List</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The type of access that is granted to a user is controlled by the assignment of Security Keys. For more information about security keys, see page [89](#security-keys).

### Registry \| Edit Site Parameters menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><p>This menu option displays the Site Parameters window. From this window, you can add or remove values that define the system profile for each registry at the local facility. You will not be able to edit any of the national CCR values.</p>
<p>Use the following four tabs to set your local Site Parameters:</p>
<ul>
<li><p>Lab Tests</p></li>
<li><p>Registry Meds</p></li>
<li><p>Notifications</p></li>
<li><p>Local Fields</p></li>
</ul></th>
<th><p>![](ror-1-5-42-user-manual/093.png)</p>
<p><span id="_Toc167263791" class="anchor"></span>Figure 26 – Registry | Edit Site Parameters menu option</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Lab Tests tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/094.png) From this tab, you can indicate which local lab tests (orderable items), from the LAB TEST file \#60, are used for reporting registry-specific results. These values are used for reports throughout the CCR.

| ![](ror-1-5-42-user-manual/095.png) | Important: If a facility has used numerous local names to refer to these tests over the years, then all of these test names should be selected, including those that have been “Z’d out” (a lab test that is no longer in use and has one or more “Z” characters appended to the beginning of the test name). This is especially important at merged facilities. Registry coordinators should confer with their clinical staff and Lab ADPAC to assure that all variations of test names are entered. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Registry Meds tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/096.png) From this tab, you can view two lists of medications used in the active registry: Local Registry Medications, and Generic Registry Medications.

- The Local Registry Medications list identifies registry-related drugs and dosages used at the facility but not already included in the National Registry Medication list. This list appears in the upper right pane and can be modified by local registry coordinators. In general there will be no or very few medications that are not already included in the National Registry Medication list.
- The Generic Registry Medications list contains all generic medications relevant to the registry that have been approved by the FDA as of June, 2008. The VA generic name is used because it includes all formulations and strengths of the drug. Local names for these medications are not displayed in this list. The Generic Registry Medications list appears in the lower right pane, and cannot be modified locally. As new medications receive FDA approval and are placed on the VA formulary, the National Registry Medications list in ROR REGISTRY PARAMETERS File \#798.1 will be updated.

In most cases, the local coordinator will not need to add to this list. An exception might be when a new medication (not just a different dosage form, but a new medication altogether) to treat the registry specific condition is FDA approved. It can take some time for the VA Generic name to be set up in the local system, and patients may receive the new medication prior to the VA Generic name being set up. In this situation the local dispensing pharmacy creates a local drug name for the new drug, which the coordinator can add to the Local Registry Medications list. When the VA Generic name is installed in the system, the local Pharmacy ADPAC links any previously created local drug names to the new VA Generic name.

## Notifications tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/097.png) From this tab, you can add to or remove from the list of people who have been identified as registry coordinators or who have been selected to receive notifications. These users will receive alerts generated by the CCR system when a registry error occurs, such as a problem in the transmission of data or attempted access by an unauthorized user. Notifications are typically sent to the IRM support person and the registry coordinator.

## Local Fields tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/098.png) From this tab, you can create and define fields to track pertinent aspects of care for your local environment. For example, you can set up fields in the Hepatitis C registry to document sustained viral response and another to note that a patient refused a liver biopsy. These fields can be applied to a patient through the Patient Data Editor screen. Local fields are available to all users of the registry and are registry specific – if you create a field in CCR:HEPC, it will not appear in CCR:HIV.

## Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/099.png)</p>
<p><span id="_Toc167263792" class="anchor"></span>Figure 27 – Reports Menu Drop-Down List</p></th>
<th><p>The Re<u>p</u>orts menu displays the list of reports that are available to you, and also offers a Report List option. When you select a report from the list, a secondary Registry Reports window displays the specific parameters and criteria that you can select to generate the report. The Task Manager tab of the GUI is automatically activated when the Reports menu is opened.<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p>
<p>For details on individual reports, see Registry Reports.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>added this functionality.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

### Report List Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/100.png)</p>
<p><span id="_Toc167263793" class="anchor"></span>Figure 28 – Reports | Report List menu option</p></th>
<th><p>The Report List… option provides you with an alternate method of generating reports.</p>
<p>When you select this option, a secondary Registry Reports window displays two panes.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>The left pane, under the heading List of Reports, displays an alphabetical list of the reports that are available to you. From this List of Reports, you can select the report to generate. The selected report is identified with an arrow.</p>
<p>The right pane displays the specific parameters and criteria that you can select to generate the report.</p></td>
</tr>
<tr class="even">
<td colspan="2"><p>![](ror-1-5-42-user-manual/101.png)</p>
<p><span id="_Toc167263794" class="anchor"></span>Figure 29 – Sample Report Setup Screen</p></td>
</tr>
</tbody>
</table>

For details on individual reports, see Registry Reports.

## Window Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 16%" />
<col style="width: 42%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/102.png)</p>
<p><span id="_Toc167263795" class="anchor"></span>Figure 30 – Window Menu Drop-Down List</p></th>
<th colspan="2">Each session of the registry and each report selected for display will appear in its own window within the larger CCR window. You can choose to display these windows in several ways using the Window menu to select the following menu options:</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><ul>
<li><p>The <u>C</u>ascade menu option allows you to cascade the view of all open windows. Cascading the windows stacks them so that each window title bar is visible.</p></li>
<li><p>The Tile menu options – Tile <u>H</u>orizontally and Tile <u>V</u>ertically – allow you to view the windows in these display modes.</p></li>
<li><p>The <u>M</u>inimize All menu option places the open windows in the minimized mode, meaning that the window is not open and cannot be viewed, but the title of the window is displayed in the bottom part of the CCR window.</p></li>
<li><p>The <u>A</u>rrange All menu option arranges the icons of minimized child windows in the bottom part of the CCR main window.</p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">In the area below the <u>A</u>rrange All menu option, you can view the number of open windows, including registry windows and any reports that are being viewed. The open windows are listed numerically in the order in which they were opened.</td>
<td colspan="2"><p>![](ror-1-5-42-user-manual/103.png)</p>
<p><span id="_Toc167263796" class="anchor"></span>Figure 31 – Window | Active Registry</p></td>
</tr>
</tbody>
</table>

![](ror-1-5-42-user-manual/104.png) The current active window is identified with a bullet. To activate another window, click the desired window on the drop-down menu.

## Help Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Help menu displays the following menu options:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/105.png)</p>
<p><span id="_Toc167263797" class="anchor"></span>Figure 32 – Help Menu Drop-Down List</p></th>
<th><ul>
<li><p>Help Topics</p></li>
<li><p>What’s New</p></li>
<li><p>Registry Info</p></li>
<li><p>CCOW Status</p></li>
<li><p>About…</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Help \| Help Topics menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The CCR Online Help file is launched from the Help Topics menu option, or by pressing \< F1 \>. The drop-down Help menu offers you the Help Topics page (sort of a table of contents for the help file), while \< F1 \> offers you help related to the specific screen and entry field that you are viewing when you press the \< F1 \> key. The Help file includes instructions, procedures, and other information to help you use the CCR application. *Note:* The display you see in the actual help file may vary from the illustration below.

![](ror-1-5-42-user-manual/106.png)

<span id="_Toc167263798" class="anchor"></span>Figure 33 – Sample Online Help Page

> **NOTE:** Effective with Patch 35 (ROR\*1.5\*35), the application help was redesigned to work on Windows 10.

### Help \| What’s New menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCR Online Help file is launched from the Help \| What’s New menu option and the What’s New page is displayed. A screen similar to the following will be displayed.

![](ror-1-5-42-user-manual/107.png)

<span id="_Toc167263799" class="anchor"></span>Figure 34 – What’s New Help Page

### Help \| Registry Info menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Registry Information pane is launched from the Help \| Registry Info menu option.

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/108.png)</p>
<p><span id="_Toc167263800" class="anchor"></span>Figure 35 – Help | Registry Info pop-up</p></th>
<th><p>This pane displays basic information about the active registry including the following items as shown in the example in Figure 35:</p>
<ul>
<li><p>Date of the last registry update (the date any changes were made to your local registry list)</p></li>
<li><p>Date of the last data extraction</p></li>
<li><p>Number of active patients in the registry during the last update</p></li>
<li><p>Server version, latest patch number, and the patch installation date</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Help \| CCOW menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCOW allows VistA applications to synchronize their clinical context based on the [HL7](#Glos_HL7) [Clinical Context Object Workgroup](#Glos_CCOW) standard. In simple terms, this means that if CCOW-compliant applications are sharing context and one of the applications changes to a different patient, the other applications will change to that patient as well.

The CCOW Status pane is launched from the CCOW menu option. It displays information about whether or not the [Contextor](#Glos_Contextor) software has been installed, and whether the application is participating in a clinical context.

![](ror-1-5-42-user-manual/109.png)

<span id="_Toc167263801" class="anchor"></span>Figure 36 – Contextor Status pane

For more information about the CCOW standards for VistA applications, see the Workgroup web site at: See CCR Redacted document.

### Help \| About CCR menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/110.png)</p>
<p><span id="_Toc167263802" class="anchor"></span>Figure 37 – Help | About panel</p></th>
<th><p>This menu option displays the About Clinical Case Registries pane. It shows basic information about the current file version including the release date, patch number, where the Clinical Case Registries software was developed and the software compile date. Click [OK] or press the &lt; Esc &gt; key to close the pane.</p>
<p>For CCR 1.5.10, this window was modified to meet current VA GUI Standards and Conventions requirements.</p>
<p>Use this option to determine which version of the GUI that you have installed. If the GUI and VistA software versions do not match, you may encounter problems with the application. For example, if your site has installed Patch ROR*1.5*42, your GUI should also be at Patch level 42.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> **NOTE:** The software compile date and CRC value shown in the figure above are examples and may not match the values shown using the Help \| About menu option. (See Section 6.0 of the *CCR Release Notes* for the actual software compile date and CRC value.)

# Setting Up Site-Specific Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each medical center or site that uses CCR can set the following parameters:

- [Lab Tests](#adding-lab-tests)
- [Registry Medications](#adding-registry-medications)
- [Notifications](#_Changing_ICR_System_Default Setting)
- [Local Fields](#adding-local-fields)
- [Preferences](#changing-system-default-settings) (default settings)

## Adding Lab Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Lab Tests tab on the Site Parameters window to indicate which local lab tests (local test names) should be used to report HIV- or Hepatitis C-specific results.

| ![](ror-1-5-42-user-manual/111.png) | Note: These parameters must be set up in order for the Registry Lab Tests By Range report to work properly. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|

1.  From the Registry menu, select Edit Site Parameters. The same choices are available for either registry. Click the Lab Tests tab.

> ![](ror-1-5-42-user-manual/112.png)

2.  On the right pane, select a lab test category by clicking its tab. Note that the selected tab (HepC Ab in the example below) appears to be “depressed” on screen.

> ![](ror-1-5-42-user-manual/113.png)

<span id="_Toc167263803" class="anchor"></span>Figure 38 – Site Parameters panes

> Depending on the size of the window, some of the available tabs may not appear at first. If this is the case, either expand the window, or use the left and right scroll buttons ![](ror-1-5-42-user-manual/114.png) to display more choices.

> CCR:HIV tabs include CD4 count, CD4 %, HIV Viral Load, HIV Ab and HIV Confirm.

> CCR:HEPC tabs include HepC Ab, HepC RIBA, HepC Qual, HepC Quant, and HepC Genotype.

3.  In the search box on the left pane, type a partial or full name of the test you want to add in the Target field, and then press \< Enter \> or click the \[Start Search\] command icon (magnifying glass) ( ![](ror-1-5-42-user-manual/115.png) ).

| ![](ror-1-5-42-user-manual/116.png) | Note: The system will search for tests using *begins with* criteria. That is, the search will find tests whose names *begin with* the letters typed in the target field. If the characters you supply are merely *contained in* the test name, the test will not be found. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](ror-1-5-42-user-manual/117.png) | Important: \[Search\] entries must be in ALL UPPER-CASE characters. Using lower-case or mixed-case entries will not work! |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|

| ![](ror-1-5-42-user-manual/118.png) | Important: When you start a search, the magnifying glass icon changes to a red X (![](ror-1-5-42-user-manual/119.png)) (although you may not see this, if the search is a short one). Click the X (or press \< Ctrl \>+\< Alt \>+\< C \>) to stop the search at any time. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

> The left-side pane displays the test(s) which match the criteria in the Target field. From the left-hand pane, select the test(s) that you want to add to the tab you have selected in the right-side pane, and then click the right arrow ( ![](ror-1-5-42-user-manual/120.png) ) to transfer the selected test(s) to the right-side pane. You can add *all* the tests shown on the left-side pane by clicking the double right arrow ( ![](ror-1-5-42-user-manual/121.png) ):

> ![](ror-1-5-42-user-manual/122.png)

<span id="_Toc167263804" class="anchor"></span>Figure 39 – Adding Tests to Site Parameters

> Conversely, you can use the double left arrow ![](ror-1-5-42-user-manual/123.png) to remove all tests from the right pane.

> *See also* 3.3.8 above for information on using assistive technology with this and similar screens.

| ![](ror-1-5-42-user-manual/124.png) | Important: If a facility has used numerous local names to refer to these tests over the years, then all of these test names should be selected, including those that have been “Z’d out” (a lab test that is no longer in use and has one or more “Z” characters appended to the beginning of the test name). This is especially important at merged facilities. Registry coordinators should confer with their clinical staff and Lab ADPAC to ensure that all variations of test names are entered. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

4.  ![](ror-1-5-42-user-manual/125.png) Click the \[Save\] button to save any changes…

> ![](ror-1-5-42-user-manual/126.png) …or click \[Cancel\] to close without saving.

| ![](ror-1-5-42-user-manual/127.png) | Note: You will be prompted to save or cancel your changes if you attempt to close the window without first clicking the \[Save\] button. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|

### Adding Lab Tests for Local Registries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the user selects Registry Edit Site Parameters, the system will display tabs for Lab Tests, Notifications, and Local Fields.

![](ror-1-5-42-user-manual/128.png)

<span id="_Toc167263805" class="anchor"></span>Figure 40 – Local Registry Display Tabs

A generic tab on the right side of the screen will display laboratory tests. The user may select tests as Registry Lab and move them to the right. Once a user has selected a laboratory test as a Registry Lab, it will be displayed in the middle pane of the Registry Lab Tests Patient Data Editor. The Type of Test column will indicate the test is a registry lab.

## Removing Laboratory Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Site Parameters window to remove local lab tests (local test names) from the report categories used to report HIV- and Hepatitis C-specific information.

From the Registry menu, select Edit Site Parameters. The same choices are available for either registry. Click the Lab Tests tab.

![](ror-1-5-42-user-manual/129.png)

On the right pane, select a lab test category by clicking its tab. Note that the selected tab (HepC Ab in the example below) appears to be “depressed” on screen.

![](ror-1-5-42-user-manual/130.png)

<span id="_Toc167263806" class="anchor"></span>Figure 41 – Site Parameters panes

Depending on the size of the window, some of the available tabs may not appear at first. If this is the case, either expand the window, or use the left and right scroll buttons (![](ror-1-5-42-user-manual/131.png)) to display more choices.

The right-side pane displays a list of the laboratory tests that have been added to each report category type.

1.  On the right pane, select a lab test category by clicking its tab. A list of the tests associated with the selected category displays in the right side pane.
2.  Select the test(s) from the right side pane that you want to remove. The left red arrow (![](ror-1-5-42-user-manual/132.png)) becomes available. Click the left arrow to delete the selected test(s) from the right side pane.  
    *  
    See also* 3.3.8 above for information on using assistive technology with this and similar screens.
3.  ![](ror-1-5-42-user-manual/133.png) Click the \[Save\] button to save any changes…  
    ![](ror-1-5-42-user-manual/134.png) …or click \[Cancel\] to close without saving.

| ![](ror-1-5-42-user-manual/135.png) | Note: You will be prompted to save or cancel your changes if you attempt to close the window without first clicking the \[Save\] button. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|

## Adding Registry Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(See Adding Lab Tests for illustrations of adding laboratory tests. The general process of adding Registry Medications is similar.)

Use the Registry Meds tab on the Site Parameters window to identify medications and dosages used at the facility that are not included in the Generic Registry Medications list. The medications included in the Generic Registry Medications are listed in the lower right pane.

Registry medications are used to treat the condition being tracked and not complications of the disease or its treatment. For example, the CCR:HIV tracks [antiretrovirals](#Glos_ARV) but not PCP prophylaxis drugs; the CCR:HEPC tracks [peginterferon](#Glos_Peginterferon) and [ribavirin](#Glos_Ribavirin) but not [epoetin](#Glos_Epoetin).

In most cases, the local coordinator will not need to add to this list. An exception might be when a new medication (not just a different dosage form, but a new medication altogether) to treat the registry specific condition is FDA approved. It can take some time for the VA Generic name to be set up in the local system, and patients may receive the new medication prior to the VA Generic name being set up. In this situation the local dispensing pharmacy creates a local drug name for the new drug, which the coordinator can add to the Local Registry Medications list. When the VA Generic name is installed in the system, the local Pharmacy ADPAC links any previously created local drug names to the new VA Generic name.

1.  From the Registry menu, select Edit Site Parameters. The same choices are available for either registry. Click the Registry Meds tab.
2.  At the top of the left-side pane, type a partial or full name of the drug you want to add in the Target field, and then press \< Enter \> or click the \[Start Search\] button (magnifying glass icon).

| ![](ror-1-5-42-user-manual/136.png) | Note: The system will search for drugs using *begins with* criteria. That is, the search will find drugs whose names *begin with* the letters typed in the target field. If the characters you supply are merely *contained in* the drug name, the test will not be found. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](ror-1-5-42-user-manual/137.png) | Important: When you start a search, the magnifying glass icon changes to a red X (![](ror-1-5-42-user-manual/138.png)) (although you may not see this, depending on how long the search takes). Click the X (or press \< Ctrl \>+\< Alt \>+\< C \>) to stop the search at any time. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

> The left-side pane displays the drugs that match the criteria in the Target field.

3.  Select the drug(s) you want to add from the left-side pane, and then click the right arrow or double-click the name to transfer the selected drug(s) to the upper right-side pane. Add all drugs on the left-side pane by clicking the double right arrows.

> *See also* 3.3.8 above for information on using assistive technology with this and similar screens.

4.  ![](ror-1-5-42-user-manual/139.png) Click the \[Save\] button to save any changes…

> ![](ror-1-5-42-user-manual/140.png) …or click \[Cancel\] to close without saving.

| ![](ror-1-5-42-user-manual/141.png) | Note: You will be prompted to save or cancel your changes if you attempt to close the window without first clicking the \[Save\] button. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|

## Removing Registry Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(See Removing Laboratory Tests for illustrations of removing laboratory tests. The general process of removing Registry Medications is similar.)

It is generally *not necessary to remove* a mediation from this list unless it was somehow entered in error. Even if a medication used historically becomes outdated and no longer used, it should remain on the list, because removing it would mean the software would omit past instances in which it was used to treat the registry condition. You can remove local names for registry medications from the Registry Meds tab on the Site Parameters window.

1.  From the Registry menu, select Edit Site Parameters, and then click the Registry Meds tab.  
      
    The upper right-side pane displays a list of the medications identified as being used locally at the facility, in addition to the generic medications listed in the lower right-side pane.
2.  From the upper right-side pane, select the drug(s) to remove, and then click the left arrow ( ![](ror-1-5-42-user-manual/142.png) ) to delete the drug(s) from the list.  
    *  
    See also* 3.3.8 above for information on using assistive technology with this and similar screens.
3.  ![](ror-1-5-42-user-manual/143.png) Click the \[Save\] button to save any changes…  
    ![](ror-1-5-42-user-manual/144.png) …or click \[Cancel\] to close without saving.

| ![](ror-1-5-42-user-manual/145.png) | Note: You will be prompted to save or cancel your changes if you attempt to close the window without first clicking the \[Save\] button. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|

## Adding Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(See Adding Lab Tests for illustrations of adding laboratory tests. The general process of adding Notifications is similar.)

Certain users such as IRM staff and Registry Coordinators can receive system-generated notifications and alerts when problems occur with the registry, such as a problem in the transmission of data or attempted access by an unauthorized user. Use this procedure to assign these alerts through the Registry menu.

1.  From the Registry menu, select Edit Site Parameters, and then click the Notifications tab.
2.  ![](ror-1-5-42-user-manual/146.png) Enter a partial or full surname of the user you want to add in the Target field at the top of the left hand pane, and then press \< Enter \> or click the \[Start Search\] button (magnifying glass icon).

| ![](ror-1-5-42-user-manual/147.png) | Note: The system will search for users using *begins with* criteria. That is, the search will find users whose names *begin with* the letters typed in the target field. If the characters you supply are merely *contained in* the user’s name, the user will not be found. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](ror-1-5-42-user-manual/148.png) | Important: \[Search\] entries must be in ALL UPPER-CASE characters. Using lower-case or mixed-case entries will not work! |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|

| ![](ror-1-5-42-user-manual/149.png) | Important: When you start a search, the magnifying glass icon changes to a red X (![](ror-1-5-42-user-manual/150.png)) (although you may not see this, depending on how long the search takes). Click the X (or press \< Ctrl \>+\< Alt \>+\< C \>) to stop the search at any time. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

> The left-side pane displays a list of users matching the criteria in the Target field.

| ![](ror-1-5-42-user-manual/151.png) | Tip: Clicking the \[Start Search\] button when the Target field is empty will return all selectable user names in the left-side pane. This is the entire list of all people with VistA access and would likely take several minutes to process, often exceeding the system timeout parameter. There are few if any times when this option would be used. |
|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

3.  From the left-side pane, select the name of the user(s) to add, and then click the right arrow or double-click the name to transfer it to the right-side pane. Add all users on the left-side pane by clicking the double right arrow.

> *See also* 3.3.8 above for information on using assistive technology with this and similar screens.

4.  ![](ror-1-5-42-user-manual/152.png) Click the \[Save\] button to save any changes…

> ![](ror-1-5-42-user-manual/153.png) …or click \[Cancel\] to close without saving.

| ![](ror-1-5-42-user-manual/154.png) | Note: You will be prompted to save or cancel your changes if you attempt to close the window without first clicking the \[Save\] button. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|

| ![](ror-1-5-42-user-manual/155.png) | Note: The notifications functionality remains the same for all registries as it does in the Hepatitis C and HIV registries. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|

## Removing Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

(See Removing Laboratory Tests for illustrations of removing laboratory tests. The general process of removing Notifications is similar.)

| ![](ror-1-5-42-user-manual/156.png) | Warning: Users who are removed from the Notifications list will no longer receive system-generated alerts when problems occur. However, removing a name from the Notifications list does *not* remove that person’s access to the registry. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Notifications are managed through the Notifications tab on the Site Parameters window.

1.  From the Registry menu, select Edit Site Parameters, and then click the Notifications tab.

> ![](ror-1-5-42-user-manual/157.png)

> The right-side pane displays a list of users who are currently set to receive notifications.

2.  From the right-side pane, select the name of the user(s) to remove, and then click the left arrow to delete the name of the user from the list.  
      
    *See also* 3.3.8 above for information on using assistive technology with this and similar screens.
3.  ![](ror-1-5-42-user-manual/158.png) Click the \[Save\] button to save any changes…  
    ![](ror-1-5-42-user-manual/159.png) …or click \[Cancel\] to close without saving.

| ![](ror-1-5-42-user-manual/160.png) | Note: You will be prompted to save or cancel your changes if you attempt to close the window without first clicking the \[Save\] button. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|

## Adding Local Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local Fields can be used to track pertinent aspects of care in your local environment. For example, you can add fields to track which patients attended an educational group session, or track a particular test result. These will be available to all users of the registry and are registry specific – if you create a field in CCR:HEPC, it will not appear in CCR:HIV.

From the Registry menu, select Edit Site Parameters.

![](ror-1-5-42-user-manual/161.png)

The same choices are available for either registry.

![](ror-1-5-42-user-manual/162.png)

<span id="_Toc167263807" class="anchor"></span>Figure 42 – Edit Site Parameters \| Selecting Local Fields tab

![](ror-1-5-42-user-manual/163.png) Click the Local Fields tab.

The Local Fields window contains the list of pre-defined local fields, if any…

![](ror-1-5-42-user-manual/164.png)

<span id="_Toc167263808" class="anchor"></span>Figure 43 – Edit Site Parameters \| Local Fields tab

If no local fields have been defined, the window will be empty, and the \[<u>A</u>dd\] command icon will be available…

![](ror-1-5-42-user-manual/165.png)

<span id="_Toc167263809" class="anchor"></span>Figure 44 – Edit Site Parameters \| Local Fields tab (Add button)

In either case, the process of adding a local field is the same.

1.  Click the \[<u>A</u>dd\] command icon. A blank entry row appears in the list. Note that the row background is white, indicating fields in which you can enter data:

> ![](ror-1-5-42-user-manual/166.png)

2.  Click inside the Name field and enter a brief label that reflects what the field means. This label will appear in the Patient Data Editor window, so it needs to be clear what the field indicates.
3.  Click the Description field and enter a concise description for the new field.

> ![](ror-1-5-42-user-manual/167.png)

<span id="_Toc167263810" class="anchor"></span>Figure – Edit Site Parameters \| Adding a Local Field

4.  Click \[<u>A</u>pply\] to save the new field and continue to work with local fields, or click \[Save\] to save the new field and close the window. Click \[Cancel\] to close without saving.

To verify that the newly created field is operational, open a patient record in the Patient Data Editor (see [Editing a Patient Record](#editing-a-patient-record)) and click on the Local Fields tab. The newly-created field will be available there.

| ![](ror-1-5-42-user-manual/168.png) | Note: The local fields functionality remains the same for all registries as it does in the Hepatitis C and HIV registries. The sites may create local fields that apply to individual local new registries and that can be used to include/exclude in the local field selection panel on reports. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## Inactivating or Deleting Local Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/169.png) | Tip: If a Local Field is no longer needed, you can inactivate it or delete it. In most cases it is preferable to inactivate a local field, rather than delete it. Inactivated local fields remain on this list but no longer appear elsewhere in the registry, such as in the Patient Data Editor window or as choices when running reports. Inactivated fields can be reactivated for use at a later date. Deleted local fields are removed from the system entirely and cannot be restored. |
|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

> 1\. From the Registry menu, select Edit Site Parameters, and then click the Local Fields tab.

> The Local Fields window opens, containing the list of existing local fields.

> ![](ror-1-5-42-user-manual/170.png)

<span id="_Toc167263811" class="anchor"></span>Figure 46 – Edit Site Parameters \| Local Fields tab (showing existing Local Fields)

2.  ![](ror-1-5-42-user-manual/171.png) Note that the \[Delete\] command icon is unavailable. Click a field to select it.

> ![](ror-1-5-42-user-manual/172.png) The \[Delete\] command icon becomes available.

3.  Click the \[Delete\] command icon. A confirmation dialog box opens:

> ![](ror-1-5-42-user-manual/173.png)

<span id="_Toc167263812" class="anchor"></span>Figure 47 – Delete Local Fields Confirmation pop-up

- Click \[Yes\] to *delete the field* and remove all of its related values from patient records.
- Click \[No\] to *inactivate the field* and leave the related values in patient records. “Inactivated” fields will not appear in the Patient Data Editor window or in reports, but they will appear on this list.
- Click \[Cancel\] to leave the selected field as it is.

## Reactivating Local Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a Local Field has been inactivated, you can reactivate or “restore” it (deleted fields cannot be restored).

1.  From the Registry menu, select Edit Site Parameters, and then click the Local Fields tab.

    The Local Fields window opens, containing a list of existing local fields. An inactivated local field has a date in the Inactivated column.

    ![](ror-1-5-42-user-manual/174.png)

<span id="_Toc167263813" class="anchor"></span>Figure 48 – Edit Site Parameters \| Local Fields tab (showing Inactivated Field)

2.  Click an inactivated Local Field to select it, and then click the \[Res<u>t</u>ore\] command icon. Or, right-click the field and select Restore from the context menu:

    ![](ror-1-5-42-user-manual/175.png)

<span id="_Toc167263814" class="anchor"></span>Figure 49 – Edit Site Parameters \| Local Fields Context menu

The date is removed from the Inactivated column, and the local field is available to use again.

3.  ![](ror-1-5-42-user-manual/176.png) Click \[<u>A</u>pply\] to save the restored field and continue to work with Local Fields…

    ![](ror-1-5-42-user-manual/177.png) … or click the \[Save\] button to save the restored field and continue to work with Local Fields…

    ![](ror-1-5-42-user-manual/178.png) …or click \[Cancel\] to close the Local Fields pane without saving.

## Confirming Local Field Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you make any changes on the Local Fields pane, you will be prompted to save your work when you close the pane:

![](ror-1-5-42-user-manual/179.png)

<span id="_Toc167263815" class="anchor"></span>Figure 50 – Edit Site Parameters \| Local Fields Change confirmation

![](ror-1-5-42-user-manual/180.png) Click \[<u>Y</u>es\] to save any changes made and close…

![](ror-1-5-42-user-manual/181.png) … or click the \[<u>N</u>o\] button to discard any changes and close…

![](ror-1-5-42-user-manual/182.png) …or click \[Cancel\] to close the Local Fields pane without saving any changes.

## Changing System Default Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following settings allow you to customize the way your system performs and how the GUI looks.

### Changing the Maximum Number of Patients to Retrieve

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can speed up your searches by limiting the number of patients to be retrieved in each search. Be aware, however, that setting a lower value in registries with large numbers of patients may result in incomplete reports.

1.  From the File menu, select Preferences.

> ![](ror-1-5-42-user-manual/183.png)

<span id="_Toc167263816" class="anchor"></span>Figure 51 – File \| Preferences menu option

> The Preferences window displays.

> ![](ror-1-5-42-user-manual/184.png)

<span id="_Toc167263817" class="anchor"></span>Figure 52 – Preferences window

2.  On the <u>G</u>eneral tab of the Preferences window, type the maximum number of patients to retrieve in the applicable field.

| ![](ror-1-5-42-user-manual/185.png) | Tip: The default number of maximum patients to retrieve is 300. In registries with larger volumes of patients, it will be helpful to set this value fairly high. |
|---------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|

3.  ![](ror-1-5-42-user-manual/186.png) Click the \[Restore <u>D</u>efaults\] button to restore the default values…

> ![](ror-1-5-42-user-manual/187.png) …or click the \[Save\] button to save any changes…

> ![](ror-1-5-42-user-manual/188.png) …or click \[Cancel\] to close without saving.

> The Preferences window automatically closes.

### Changing the RPC Broker Timeout Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select Preferences from the File menu.

> The Preferences window displays. Make sure the General tab is selected.

> ![](ror-1-5-42-user-manual/189.png)

<span id="_Toc167263818" class="anchor"></span>Figure 53 – Preferences window (Broker Timeout)

2.  Tab to (or click in) the RPC Broker Timeout (sec) field. Select the number of seconds from the RPC Broker Timeout (sec) dropdown list.

| ![](ror-1-5-42-user-manual/190.png) | Tip: The default number of seconds before timeout is 60. |
|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|

3.  ![](ror-1-5-42-user-manual/191.png) Click the \[Restore <u>D</u>efaults\] button to restore the default values…

> ![](ror-1-5-42-user-manual/192.png) …or click the \[Save\] button to save any changes…

> ![](ror-1-5-42-user-manual/193.png) …or click \[Cancel\] to close without saving.

> The Preferences window automatically closes.

### Changing the Screen Colors and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select Preferences from the File menu.

> The Preferences window displays.

> ![](ror-1-5-42-user-manual/194.png)

<span id="_Toc167263819" class="anchor"></span>Figure 54 – Preferences window (General tab displayed)

2.  Click the Appearance tab. The Appearance pane displays:

> ![](ror-1-5-42-user-manual/195.png)

<span id="_Toc167263820" class="anchor"></span>Figure 55 – Preferences window (Appearance tab displayed)

3.  ![](ror-1-5-42-user-manual/196.png) Click the Display Hints checkbox to enable [tool tips](#Glos_ToolTips) throughout the application.
4.  Click a GUI Element name (for example, *Read-only Controls*) to select it and activate the color options.

> ![](ror-1-5-42-user-manual/197.png)

<span id="_Toc167263821" class="anchor"></span>Figure 56 – Preferences window (Appearance \| Colors)

5.  Select a Foreground Color from the drop-down list to set the text color for the selected element. You may select from approximately 20 actual colors, or match the element to some color scheme already set for your Windows installation.

> ![](ror-1-5-42-user-manual/198.png)

<span id="_Toc167263822" class="anchor"></span>Figure 57 – Preferences window (Appearance \| Colors \| Foreground)

6.  ![](ror-1-5-42-user-manual/199.png) Click the \[Restore <u>D</u>efaults\] button to restore the default values…

> ![](ror-1-5-42-user-manual/200.png) …or click the \[Save\] button to save any changes…

> ![](ror-1-5-42-user-manual/201.png) …or click \[Cancel\] to close without saving.

> If you select \[Save\] or \[Cancel\], the Preferences window automatically closes. Otherwise, continue below.

7.  Select a Background Color from the drop-down list to set the background color for the selected element. Repeat the process shown above to modify Background Color. Again, you may select from approximately 20 actual colors, or match the element to some color scheme already set for your Windows installation. Be careful not to select a background color that’s the same color as the foreground color previously selected!

> ![](ror-1-5-42-user-manual/202.png)

<span id="_Toc167263823" class="anchor"></span>Figure 58 – Preferences window (Appearance \| Colors \| Background)

> The selected colors are shown in the Text Sample box at the bottom of the Options window.

8.  ![](ror-1-5-42-user-manual/203.png) Click the \[Restore <u>D</u>efaults\] button to restore the default values…

> ![](ror-1-5-42-user-manual/204.png) …or click the \[Save\] button to save any changes…

> ![](ror-1-5-42-user-manual/205.png) …or click \[Cancel\] to close without saving.

> The Preferences window closes and selected colors and options are displayed throughout the GUI.

### Restoring Default GUI Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the <u>F</u>ile menu, select Preferences.

> ![](ror-1-5-42-user-manual/206.png)

<span id="_Toc167263824" class="anchor"></span>Figure 59 – File \| Preferences menu option

> The Preferences window displays:

> ![](ror-1-5-42-user-manual/207.png)

<span id="_Toc167263825" class="anchor"></span>Figure 60 – Preferences window (General tab displayed)

2.  ![](ror-1-5-42-user-manual/208.png) Click the \[Restore Defaults\] button.

> The system defaults are displayed in the Preferences window.

3.  ![](ror-1-5-42-user-manual/209.png) Click the \[Save\] button to save any changes…

> The system defaults are restored for all options and the Preferences window automatically closes.

  

# Registry Window Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you open a registry, a “child” window is displayed inside the main application window. This window contains registry-specific interface elements. When the registry window is activated, the main menu of the application is updated with the registry-specific menus and options.

The main Registry window is divided into sections that are accessible through the Task Manager, Technical Log, and Registry tabs.

![](ror-1-5-42-user-manual/210.png)

<span id="_Toc167263826" class="anchor"></span>Figure 61 – Three Major Tabs

## Task Manager tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Task Manager tab displays a list of the reports that a user has generated. Each report is associated with a task number. Adjacent to the task number is the name of the report, the date and time that the report is scheduled to run, the status of the report, its progress, the date and time the report was completed and any comments that were entered when the report was selected.

![](ror-1-5-42-user-manual/211.png)

<span id="_Toc167263827" class="anchor"></span>Figure 62 – Task Manager tab

| ![](ror-1-5-42-user-manual/212.png) | Tip: Completed reports appear on the Task Manager tab for 14 days after they finish running, at which point they are automatically deleted from the list. To save a report for use beyond that 14 day period, see the instructions on page 151. |
|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

You can sort the information displayed on the Task Manager tab in ascending or descending order by clicking the column headings.

From the Task Manager tab, you can view completed reports, generate new reports, delete generated reports from the list, and check the status of reports that are in progress.

### Task column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/213.png) The Task column displays the unique system generated task number associated with the report. The task number is used for tracking purposes. This column is frequently displayed with all except the letter “T” hidden; you may have to expand the column width to see the full label.

### Type column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/214.png) The Type column displays the type of task performed by the user. For this release of the CCR, the task type will always be Report.

### Description column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/215.png) The Description column displays the name of the report.

### Scheduled column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/216.png) The Scheduled column displays the date and time at which the report is scheduled to run.

### Status column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/217.png) The Status column displays the status of the report in progress. The following table lists the status values and their meanings.

| Status                | Description                                                                                            |
|-----------------------|--------------------------------------------------------------------------------------------------------|
| Active: Pending       | The report is scheduled, but not yet running                                                           |
| Active: running       | The scheduled report is running                                                                        |
| Active: Suspended     | The report is suspended                                                                                |
| Inactive: Crashed     | The report crashed due to runtime errors or system shutdown                                            |
| Inactive: Errors      | The report was completed with errors (the results can be incomplete)                                   |
| Inactive: Finished    | The scheduled report was completed successfully                                                        |
| Inactive: Interrupted | The report was stopped by the user (using the VistA Menu option)                                       |
| Stopping              | The user attempted to delete the report task, but the report has not yet been deleted from the system. |

### Progress column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/218.png) The Progress column displays the progress of the report as a percentage of completion.

### Completed column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/219.png) The Completed column displays the date and time the report completed running.

### Comment column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/220.png) The Comment column displays the text from the Comment field on the Report setup window, if any. This column displays up to 60 characters.

### Refresh button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/221.png) The \[Refresh\] button updates the Task Manager tab by displaying any new data on the status of reports that has been added since the window was accessed.

| ![](ror-1-5-42-user-manual/222.png) | Note: Clicking the \[Refresh\] button does *not* update the data contained in a report that has already completed. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|

### New Report button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/223.png) The \[New Report\] button displays the Registry Reports window from which you can select and generate new reports.

### Open Report button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/224.png) The \[Open Report\] button allows you to view a selected report.

![](ror-1-5-42-user-manual/225.png) If no report is selected in the Task Manager tab, this button will be deactivated (“grayed out”).

### View Log button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/226.png) The \[View Log\] button switches the main window display from the Task Manager tab to the Technical Log tab and displays detail for the selected report. See the Technical Log Tab section (page [156](#technical-log-tab)) for more information.

![](ror-1-5-42-user-manual/227.png) If no report is selected in the Task Manager tab, this button will be unavailable (“grayed out”).

### Delete button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/228.png) The \[Delete\] button allows you to delete a selected report from the Task Manager tab display. You will be prompted to confirm that the selected report should be deleted.

![](ror-1-5-42-user-manual/229.png) If no report is selected, the \[Delete\] button will be unavailable (“grayed out”).

### Right-Click Menu options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following menu options are available from the Task Manager tab display when you click the right mouse button anywhere on the tab:

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 32%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/230.png)</p>
<p><span id="_Toc167263828" class="anchor"></span>Figure 63 – Task Manager Context Menu options</p></th>
<th><ul>
<li><blockquote>
<p>New Report…</p>
</blockquote></li>
<li><blockquote>
<p>Open Report</p>
</blockquote></li>
<li><blockquote>
<p>View Task Log</p>
</blockquote></li>
<li><blockquote>
<p>Delete</p>
</blockquote></li>
<li><blockquote>
<p>Refresh</p>
</blockquote></li>
</ul></th>
<th><p>![](ror-1-5-42-user-manual/231.png)</p>
<p><span id="_Toc167263829" class="anchor"></span>Figure 64 – Task Manager Context Menu options (some unavailable)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The Open Report, View Task Log, and Delete menu options are only activated and selectable when you click the right-side mouse button on a task. If you right-click elsewhere, these options are unavailable (“grayed out”).

## Managing Reports from the Task Manager view

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Viewing a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the \[Open Report\] button from the Task Manager tab to view a selected report:

1.  From the task list in the Task Manager window, select the report you want to view.

![](ror-1-5-42-user-manual/232.png)

<span id="_Toc167263830" class="anchor"></span>Figure 65 – Task Manager tab Showing Status Column

| ![](ror-1-5-42-user-manual/233.png) | Note: Check the Status column to be sure that the report has finished running (Inactive:Finished). |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|

2.  ![](ror-1-5-42-user-manual/234.png) Once you select a report, the \[Open Report\] button becomes available. Click the \[Open Report\] button, or double-click the selected report.  
    >   
    > The selected report displays; the BMI by Range report is seen here as an example.

![](ror-1-5-42-user-manual/235.png)

<span id="_Toc167263831" class="anchor"></span>Figure 66 – Sample Report Output

| ![](ror-1-5-42-user-manual/236.png) | Note: If the report is large, it may take several minutes for the report to display. The screen will temporarily appear blank and the words “Loading and Transforming the report” will appear in the bottom left hand corner while the report is loading for display. Please be patient. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

To open multiple reports for viewing, minimize the open report or select the registry name from the Window menu, then repeat steps 1 and 2. Or, press \< Ctrl \> + \< F6 \> to switch back to the Task Manager view, and then repeat steps 1 and 2.

### Copying Text from a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When viewing a report, you can copy and paste the report text.

1.  While viewing the report output, right-click anywhere on the report display.

> The right-click pop-up menu displays.

> ![](ror-1-5-42-user-manual/237.png)

<span id="_Toc167263832" class="anchor"></span>Figure 67 – Sample Report Output (showing Context menu)

2.  From the right-click menu, choose Select All.

> The text of the report is highlighted:

![](ror-1-5-42-user-manual/238.png)

<span id="_Toc167263833" class="anchor"></span>Figure 68 – Sample Report Output (showing all content selected)

3.  From the right-click menu, select Copy.
4.  Place the cursor in the document where you want to paste the report output, then press \< Ctrl \> + \< V \>, or select Paste from the right-click menu.

> The report text will be pasted to the selected location.

| ![](ror-1-5-42-user-manual/239.png) | Note: The above procedure will copy the report data as text. To be able to sort and otherwise manipulate the data in a report, use the Save as command on the File menu to export to a file which you can then open in another program (e.g., Excel or Access) instead of using this copy-and-paste function. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Changing the Text Size of a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change the size of the text in the report output.

1.  While viewing the report output, right-click anywhere on the report display.  
      
    The right-click pop-up menu displays.
2.  Select Text Size, and then select the desired text size from the options displayed.

### Finding Text on a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Find option on the right-click menu while viewing a report to search for a word or term in the report.

1.  While viewing the report output, right-click anywhere on the report display.  
      
    The right-click pop-up menu displays.
2.  Click Find. The Find window displays:

![](ror-1-5-42-user-manual/240.png)

<span id="_Toc167263834" class="anchor"></span>Figure 69 – Report Output Find pop-up

3.  ![](ror-1-5-42-user-manual/241.png) Type the word or term you want to find in the Fi<u>n</u>d what: field.  
      
    ![](ror-1-5-42-user-manual/242.png) You can search for a match to the whole word only…  
      
    ![](ror-1-5-42-user-manual/243.png) … or match by case (the default search is case-insensitive).  
      
    ![](ror-1-5-42-user-manual/244.png) You can also search up or down the report by selecting a radio button.
4.  ![](ror-1-5-42-user-manual/245.png) Click the \[Find Next\] button to find the next instance of the selected word or term.
5.  ![](ror-1-5-42-user-manual/246.png) Click \[Cancel\] to close the Find dialog popup.

### Sorting/Ordering the Information on a Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When viewing a report, you can change the order in which the information is presented by clicking the heading of a column. All tables of the same type are sorted in the same way. For example, if you sort an Outpatient Drugs table by Number of Fills in the Pharmacy Prescription Utilization, then this kind of table will be sorted in the same way in all other sections of the report.

![](ror-1-5-42-user-manual/247.png)

<span id="_Toc167263835" class="anchor"></span>Figure 70 – Sample Report Output (showing sort column)

| ![](ror-1-5-42-user-manual/248.png) | Note: Some columns cannot be sorted. Column headings that can be used for sorting are indicated with <u>Bold, Blue, Underlined</u> text. The above sample shows the report sorted on the <u>SSN</u> column. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

The information in the selected column will be displayed in either ascending or descending order and the items in the associated columns will be reordered accordingly. The report columns only sort in either ascending or descending order.

### Saving a Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can save report output to an alternate location from an active report window; for example, you can export it for use in another application.

| ![](ror-1-5-42-user-manual/249.png) | Important: Reports which contain patient information must be handled in accordance with established policies for confidential medical information. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|

1.  While viewing the selected report, select the File menu, and then choose Save As.

> ![](ror-1-5-42-user-manual/250.png)

<span id="_Toc167263836" class="anchor"></span>Figure 71 – Sample Report Output (“Save As” to file)

> The Save the Report As window displays:

![](ror-1-5-42-user-manual/251.png)

<span id="_Toc167263837" class="anchor"></span>Figure 72 – Sample Report Output (“Save As” dialog)

2.  Select the location to which to save the report (the “My Documents” folder is shown here).
3.  Enter a name for the report in the File name field. To facilitate later use, use a name that indicates what is in the report and the date it was run– *e.g.*, “HIV Inputs 2009-Jan-05.csv”.
4.  Select a format from the Save as type drop down list. Reports can be saved in the following formats:
- [Comma-Separated values](#Glos_CSV) file (\*.csv)
- [HTML](#Glos_HTML) Document (\*.htm, \*.html)
- [XML](#Glos_XML) Document (\*.xml)
5.  Click \[Save\].

> The Save the Report As window automatically closes; the report is saved to the selected location.

### Exporting a Report to Excel or Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Saving a report in comma-separated values (.CSV) format automatically exports (saves) the contents of the report to a file in a location determined by you during the save process.

The following list describes how the tables for each of the reports will be saved:

| Report                                          | Files                           |
|-------------------------------------------------|---------------------------------|
| BMI by Range                                    | Single file                     |
| Clinic Follow Up                                | Single file (Summary not saved) |
| Combined Meds and Labs                          | Single file                     |
| Current Inpatient List                          | Single file                     |
| Diagnoses                                       | Single file                     |
| DAA Lab Monitoring (for CCR:HEPC only)          | Single file                     |
| General Utilization and Demographics            | Single file                     |
| Hepatitis A Vaccine or Immunity                 | Single file                     |
| Hepatitis B Vaccine or Immunity                 | Single file                     |
| Inpatient Utilization                           | Single file                     |
| Lab Utilization                                 | Single file                     |
| List of Registry Patients                       | Single file                     |
| Liver Score by Range                            | Single file                     |
| Outpatient Utilization                          | Single file                     |
| Patient Medication History                      | Single file                     |
| Pharmacy Prescription Utilization               | Single file                     |
| Potential DAA Candidates (for CCR:HEPC only)    | Single file                     |
| Procedures                                      | Single file                     |
| Radiology Utilization                           | Single file                     |
| Renal Function by Range                         | Single file                     |
| Registry Lab Tests by Range                     | Single file                     |
| Registry Medications                            | Single file                     |
| Sustained Virolgic Response (for CCR:HEPC only) | Single file                     |
| VERA Reimbursement (for CCR:HIV only)           | Single file                     |

| ![](ror-1-5-42-user-manual/252.png) | Note: Effective with Patch ROR\*1.5\*26, all reports saved in comma-separated values (.CSV) format will be stored as a single file. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|

### Printing a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can print the report from an active report window. The font size selected for the report window affects the corresponding printout; therefore, it is recommended to select smaller fonts before printing wide reports.

| ![](ror-1-5-42-user-manual/253.png) | Important: Use only secure printers to produce reports that contain patient information. When you print a report that contains patient information, retrieve it from the printer as soon as possible. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

1.  While viewing the selected report, select Print from the File menu.

> The Print window displays:

![](ror-1-5-42-user-manual/254.png)

<span id="_Toc167263838" class="anchor"></span>Figure 73 – File \| Print menu option

2.  From the Print window, if necessary, select the printer from which to print the report and select the printing options.
3.  Click Apply if different printing options were selected from the Print window, and then click \[Print\].

> The selected report prints.

| ![](ror-1-5-42-user-manual/255.png) | Note: You can also print a report after saving it in .CSV, .HTML, or .XML format using the appropriate applications: Microsoft Word, Microsoft Excel, Microsoft Access, etc. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Deleting a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can delete a report from the Task Manager tab.

1.  From the Task Manager tab, select the report you want to delete. To select more than one report, hold down the \< Ctrl \> key and click each report name to select it.
2.  Select \[Delete\].

![](ror-1-5-42-user-manual/256.png)

<span id="_Toc167263839" class="anchor"></span>Figure 74 – Task Manager tab (Report Task Selected for Deletion)

> You will be prompted to confirm the delete command.

> ![](ror-1-5-42-user-manual/257.png)

<span id="_Toc167263840" class="anchor"></span>Figure 75 – Task Deletion Confirmation pop-up

3.  Click \[Yes\] or \[Yes to All\] to delete the report(s).

| ![](ror-1-5-42-user-manual/258.png) | Note: Reports are automatically deleted 14 days after the date on which they were generated. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|

### Closing a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Close an active report window by selecting Close from the File menu. Or, in most cases, press the \< Esc \> key. You can also close a report by clicking the ![](ror-1-5-42-user-manual/259.png) in the upper right corner of the *report window*:

![](ror-1-5-42-user-manual/260.png)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/261.png)</th>
<th><p><strong>Caution:</strong> Clicking the ![](ror-1-5-42-user-manual/262.png) on the Clinical Case Registries window will also close the CCR application. A prompt will display asking you to confirm:</p>
<p>![](ror-1-5-42-user-manual/263.png)</p>
<p><span id="_Toc167263841" class="anchor"></span>Figure 76 – Close Window Confirmation pop-up</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Technical Log tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/264.png) | Tip: Information on the Technical Log tab will not be used by most clinicians; the following is included primarily for reference purposes. |
|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|

![](ror-1-5-42-user-manual/265.png) The Technical Log tab displays information regarding processes that are scheduled and performed in the registry. The tasks and events associated with registry processes are logged and displayed in a folder tree view in the left pane of the Technical Log tab view. Each folder in the tree is displayed with its associated task type and the date/time when the task occurred. The folders in the tree view are displayed chronologically for the past 7 days in descending order, with the most recent tasks at the top of the list. You can use the date range parameters to view more than seven days.

You can expand the folders to view the message details of the logged tasks. When a task is selected from the tree view, the message details about the task are displayed in the right pane. The types of message details that can be displayed include Warning, Information, Database Error, Data Quality, and Error.

This table shows the icons that are displayed adjacent to the messages associated with the logged tasks:

| Icon                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ror-1-5-42-user-manual/266.png)        | Informational Message: These messages present general information.                                                                                                                                                                                                                                                                      |
| ![](ror-1-5-42-user-manual/267.png) | Data Quality Message: These messages present information about problems with data quality. You can inform the IRM group with the details regarding these messages, though this is not mandatory.                                                                                                                                        |
| ![](ror-1-5-42-user-manual/268.png)               | Warning Message: These messages are largely informational with the exception of the “*Registry VA is awaiting ACK*” warning. If this warning is the most recent message in the log, the IRM group should be notified; you can assume that an acknowledgment for the last extract has not yet been received.                             |
| ![](ror-1-5-42-user-manual/269.png)       | Database Error Message: The IRM group should be informed of the details within these messages.                                                                                                                                                                                                                                          |
| ![](ror-1-5-42-user-manual/270.png)                | Error Message: *The IRM group MUST be informed of the details of these messages.* The message “*Error(s) during processing of the patient data*” indicates that the processing of the patient stopped but the job itself continued processing. All other Error Messages indicate that the running process had to stop due to the error. |

### From: and To: Date fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/271.png) The From: and To: date fields allow you to adjust the display of the Technical Log tab, by displaying those tasks and events that occurred within a selected date range. The default Technical Log view includes tasks that occurred within one week of the current date, and the date range can be expanded to include earlier activities.

## Refresh button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/272.png) The \[Refresh\] refresh button updates the Technical Log display with new activities that have taken place since the last time the window was refreshed.

## Types of Logged Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following types of activities are displayed in the Technical Log:

| Activity Type    | Description                                                                                                                                                                                                                                                                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Extraction  | Indicates that data was extracted from the registry. The activity details include the start and end dates and times of each extraction, the number of patients processed, the number of patients processed with errors, the processing rate and the registries updated.                                                                                                     |
| Report           | Indicates that a user generated a report. The activity details include the start and end date and time the report was generated and the task number.                                                                                                                                                                                                                        |
| Registry Update  | Indicates that an update was made to the active registry. The activity details include the start and end dates and times of each update, the number of patients processed, the number of patients processed with errors, the processing rate and the registries updated.                                                                                                    |
| Access Violation | Indicates that an unauthorized user attempted to access CCR data. An alert will display on the unauthorized user’s window stating that access is denied. Simultaneously and for each violation, those CCR users who receive notifications will receive an alert, and the name of the unauthorized user is recorded in the Technical Log along with the unauthorized action. |

## Managing Logged Activities from the Technical Log tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Viewing the Technical Log

1.  Click the Technical Log tab to display the Technical Log window.

> ![](ror-1-5-42-user-manual/273.png)

<span id="_Toc167263842" class="anchor"></span>Figure 77 – Technical Log tab

2.  Using the From: and To: date fields, select a date range from the drop-down calendars.
3.  ![](ror-1-5-42-user-manual/274.png) Click the \[Refresh\] button to display the activities that fall within the selected date range.
4.  You can resize the left pane to see more information. Or, you can “hover” your mouse pointer over the folder title to get a tip on what the contents are:

> ![](ror-1-5-42-user-manual/275.png)

<span id="_Toc167263843" class="anchor"></span>Figure 78 – Technical Log tab (showing "tip" for one task folder)

> You can select (left-click on) a folder name to get an overall picture of what’s in that folder:

> ![](ror-1-5-42-user-manual/276.png)

<span id="_Toc167263844" class="anchor"></span>Figure 79 – Technical Log tab (showing summary for selected folder)

Viewing Activity Details

1.  In the left pane, click the plus-sign (![](ror-1-5-42-user-manual/277.png)) next to the activity folder to expand the heading and view all the messages associated with the selected activity. Information regarding the selected activity will display in the right pane.
2.  Click the message you want to view in the left pane. Information regarding the selected message will display in the right pane.

> ![](ror-1-5-42-user-manual/278.png)

<span id="_Toc167263845" class="anchor"></span>Figure 80 – Technical Log tab (showing summary and detail for selected folder)

3.  Repeat as necessary to view all the associated messages and details.

## Registry tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/279.png) The Registry tab displays the primary interface for selecting patients and performing patient-related tasks. From the Registry tab, you can search for existing patients, edit a patient’s record, and generate, view, and print a CDC form for a patient (CCR:HIV only).

The Registry tab is automatically activated when the Registry menu is selected, or if the Re<u>g</u>istry tab label is clicked:

![](ror-1-5-42-user-manual/280.png)

<span id="_Toc167263846" class="anchor"></span>Figure 81 – HIV/HEP-C Registry tab

If the user selects one of the 51 local registry options from the Select a Registry screen, the system will display a registry screen similar to that of the standard screen for the Hepatitis C and HIV registries.

![](ror-1-5-42-user-manual/281.png)

<span id="_Toc167263847" class="anchor"></span>Figure 82 – Local Registry Tab

### Note on Pending Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCR application searches inpatient files, outpatient files, and the problem list to identify patients with registry-specific ICD codes. For the HIV and Hepatitis C registries, the application also searches the laboratory files for positive registry-specific antibody test results. These ICD codes and antibody tests are defined for each registry. As CCR recognizes the earliest instance of data that meets the registry selection criteria, it adds the patient to the registry.

With the installation of Patch 35 (ROR\*1.5\*35) any HIV or Hepatitis C pending patients will be automatically updated to confirmed and the confirmation date set to the date when Patch 35 (ROR\*1.5\*35) is installed.

Prior to Patch 35 (ROR\*1.5\*35), the HIV and Hepatitis C registries patients were added in a pending status. These pending patients had to be reviewed locally, and either confirmed as having the registry-specific condition, or deleted from the registry.

Effective with Patch 35 (ROR\*1.5\*35), the HIV and Hepatitis C registries will add patients automatically to the registry lists similar to the other local registries.

| ![](ror-1-5-42-user-manual/282.png) | Note: Some references to pending patients have been left in this manual when it provides additional information or provides historical context. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|

### Search button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/283.png) The \[Search\] button activates the search function based on the searchable information in the Patient field and/or on the additional search options.

The system will search for names that *begin with* the characters typed in the Patient field, not based upon whether the string of characters is *contained* within a word. For example, typing “Car” in the target field would return “Carter” and “Carmichael,” but not “McCarthy.”

If no search criteria are provided, CCR will attempt to return all patient records; this requires considerable time, possibly exceeding system timeout parameters, and should not generally be attempted.

| ![](ror-1-5-42-user-manual/284.png) | Tip: You can also use the \[Search\] command icon ![](ror-1-5-42-user-manual/285.png) (inside the Patient name field) in place of the \[Search\] button, or press the Enter key while in the Patient name field. |
|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

When you run the search, the results are displayed. The following example shows only those patients confirmed into the registry after the date specified (Only confirmed after:):

![](ror-1-5-42-user-manual/286.png)

<span id="_Toc167263848" class="anchor"></span>Figure 83 – Registry tab (search results displayed)

### Edit button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/287.png) ![](ror-1-5-42-user-manual/288.png) This button allows you to update the patient’s record.

### CDC button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/289.png) The \[CDC\] button is only available in CCR:HIV. It allows you to access the CDC window (see [CDC Window below](#cdc-window)) for a selected patient. You can enter information on a new CDC form, or edit, view, and print an existing form.

### Delete button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/290.png) The \[Delete\] button allows you to delete a record for a patient from the registry. You will be prompted to confirm before the patient record is deleted.

If a patient record is deleted because the patient was selected for the registry based on erroneous coding or a false positive test result, that patient will not be selected again based on the same instance of erroneous coding or false positive test result. However, if there are multiple instances of erroneous coding or additional false positive tests results, the patient will be selected and added sequentially based on each instance. If such situations are observed, it is advisable to address the local coding issue.

### Patient field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/291.png)You can enter searchable information in the Patient field to search for a patient or list of patients to view in the Patient Display list.

Note the magnifying glass icon ![](ror-1-5-42-user-manual/292.png) inside the Patient field box. You may click this to start the patient search or press the \[Enter\] key, rather than using the \[Search\] button on the menu bar.

Searchable information includes the patient’s full last name, the first one or more characters of the patient’s last name, the patient’s SSN, the last four digits of the patient’s SSN, or a combination of the first letter of the patient’s last name and the last four digits of the patient’s SSN. You can also use \# followed by the patient’s 11-digit coded SSN (#12345678910) as a search parameter.[^3]

| ![](ror-1-5-42-user-manual/293.png) | Note: When the coded SSN is valid and the corresponding patient is in the registry, the patient’s record populates the list of patients; otherwise, the list of patients is cleared. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/294.png)</th>
<th><p><strong>Note:</strong> If your search returns no records, the following message will display. Click on the [OK] button to close the message and continue.</p>
<p>![](ror-1-5-42-user-manual/295.png)</p>
<p><span id="_Toc167263849" class="anchor"></span>Figure 84 – "No registry records" pop-up</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Only Confirmed After checkbox

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/296.png) The Only confirmed after checkbox allows you to search for patients in the registry who were added to the registry after a selected date. When you check this box, the adjacent date field is activated and you can enter a date.

### Patient List Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient List displays the patients whose records match the search criteria in the Patient field. The patient records will be displayed alphabetically according to their last names. Note that in this case, the search box was left blank–– which returned all 25 records. Be careful doing this kind of search unless you are sure that the number of records is fairly low!

![](ror-1-5-42-user-manual/297.png)

<span id="_Toc167263850" class="anchor"></span>Figure 85 – Registry tab (displaying search results)

The following columns are displayed in the Patient List: ![](ror-1-5-42-user-manual/298.png)

- Name
- Date Of Birth
- Confirmed (date)
- Selection Site
- Selected (date) [^4]
- Selection Rule

You can resize these columns, and you can click any column heading to sort or reorder the Patient List display by that heading.

| ![](ror-1-5-42-user-manual/299.png) | Note: The Date of Death and Sex columns, formerly displayed on this screen, were removed per revised requirements.[^5] |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|

## Name column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/300.png) |     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| The Name column displays the full name of the patient. The names are listed alphabetically by last name.                                                    |     |

## Date of Birth column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/301.png) |     |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| The Date of Birth column displays the patient’s date of birth.                                                                                                      |     |

## Confirmed column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/302.png) |     |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| The Confirmed column displays the date that the patient was confirmed in the registry.                                                                           |     |

For patients whose records existed in the Hepatitis C Case Registry, the Confirmed column displays the date of the patient’s addition to the Hepatitis C Case Registry – either at the initial creation of the registry or subsequent selection by the nightly update. For patients whose records existed in ICR 2.1, this column displays the date of their earliest selection rule. For patients whose records existed in the ICR 2.1 but who did not have a selection criterion, the Confirmed column displays the date the CCR:ICR was created. For patients subsequently added to CCR:ICR, the Confirmed column displays the date that the patient was confirmed in the registry. For all subsequent patient entries in either the CCR:HEPC or CCR:HIV, the Confirmed column displays the date that the patient was confirmed in the registry.

## Selection Site column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/303.png)                                                                        |     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| For multidivisional facilities, the Selection Site column displays the clinical site where the initial triggering ICD code or positive laboratory test was entered, if it can be determined. This column will be empty for older patients. |     |

## Selected column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/304.png) |     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| The Selected column displays the date of the earliest selection rule to simplify the processing of pending patients.[^6]                                        |     |

## Selection Rule column

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/305.png) |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The Selection Rule column displays the short description of the earliest selection rule to simplify the processing of pending patients.                               |

## Using the Registry tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Searching for Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can search for patients in the registry by using the Patient field and setting additional search options.

1.  Enter searchable information about the patient in the Patient field.  
      
    *Searchable information* includes the patient’s last name, the first one or more characters of the patient’s last name, the patient’s SSN, the last four digits of the patient’s SSN, or a combination of the first letter of the patient’s last name and the last four digits of the patient’s SSN.[^7] You can also use \# followed by the patient’s 11-digit coded SSN (#12345678910) as a search parameter.
2.  Select additional search criteria if necessary:  
      
    Check the Only confirmed after: checkbox and select a date to limit the search to patients who were added to the registry after the selected date.
3.  Click the \[Search\] button or press \< Enter \> to start the search.

| ![](ror-1-5-42-user-manual/306.png) | Tip: You can also use the \[Search\] command icon ![](ror-1-5-42-user-manual/307.png) (inside the Patient name field) in place of the \[Search\] button. |
|---------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

> The system will search for names that begin with the characters typed in the Patient field, not based upon whether the string of characters is contained within a word. For example, typing “car” in the target field would return “Carter” and “Carmichael,” but not “McCarthy.”

> When the search begins, the Patients Found indicator automatically updates as patients are found to match the search criteria. The patient(s) matching the search criteria will be displayed in the Patient List display.

> Note the magnifying glass icon ![](ror-1-5-42-user-manual/308.png) inside the Patient field box. You may click this to start the patient search, rather than using the \[Search\] button on the menu bar.

| ![](ror-1-5-42-user-manual/309.png) | Note: The system will search for records using *begins with* criteria. That is, the search will find records for patients whose names *begin with* the letters typed in the target field. If the characters you supply are merely *contained in* the patient name, the record will not be found. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](ror-1-5-42-user-manual/310.png) | Important: \[Search\] entries must be in ALL UPPER-CASE characters. Using lower-case or mixed-case entries will not work! |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|

| ![](ror-1-5-42-user-manual/311.png) | Important: When you start a search, the magnifying glass icon changes to a red X (![](ror-1-5-42-user-manual/312.png)) (although you may not see this, depending on how long the search takes). Click the X (or press \< Ctrl \>+\< Alt \>+\< C \>) to stop the search at any time. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/313.png)</th>
<th><p><strong>Note:</strong> If your search returns no records, the following message will display. Click on the [OK] button to close the message and continue.</p>
<p>![](ror-1-5-42-user-manual/314.png)</p>
<p><span id="_Toc167263851" class="anchor"></span>Figure 86 – "No registry records" pop-up</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> If the search criteria return too many patient records to display, you will be prompted to narrow your search criteria. After you press \[OK\], the screen will display the initial part of the results of your search. You can then work with the partial results, or narrow your search criteria further.

> Alternately, in order to display more patients, you can adjust the parameter that controls the maximum number of patients to retrieve. For more information, see [Changing the Maximum Number of Patients to Retrieve](#_Changing_the_Maximum_Number of Pati), page [134](#changing-the-maximum-number-of-patients-to-retrieve).

### Deleting a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can delete a patient from the CCR by using the Delete button or the right-click menu from the Patient List display.

1.  Select the patient you want to delete from the Patient List display.
2.  Click the \[Delete\] button or select Delete from the right-click menu. The confirmation dialog box displays.
3.  Click \[Yes\] to complete the delete process or click \[No\] to cancel.

### Using the Patient Data Editor Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Data Editor window is accessed from the Registry tab, and is used to edit a patient’s record.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>Patient Confirmed in Registry</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>![](ror-1-5-42-user-manual/315.png)</p>
<p><span id="_Ref22630224" class="anchor"></span>Figure – Patient Data Editor (Patient Confirmed)</p></td>
</tr>
</tbody>
</table>

You can edit a patient’s record using the fields, buttons, and checkbox options displayed on the following tabs:

1.  Clinical Status tab – available in all registries. *See* 8.4.4 below.
2.  Risk Factors tab – available in CCR:HIV only. *See* 8.4.5 below.
3.  Local Fields tab – available in all registries and customized at the local level. Usage is optional. *See* 8.4.6 below.

Basic identifying information is included at the top of the window, showing the SSN, patient name, date of birth, and status.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/316.png)</th>
<th><p><strong>Note:</strong> If the patient does not belong in the registry…</p>
<p>![](ror-1-5-42-user-manual/317.png) Click the [Delete] button in the bottom left corner of the window. The Patient Data Editor closes and a Delete patient pop-up displays. Click [Yes] to remove the patient from the registry. <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>added a description of the new button on the Patient Data Editor–Delete.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/318.png)</th>
<th><p><strong>Note:</strong> Effective with CCR 1.5.15 (Patch ROR*1.5*15):</p>
<p>An invalid date check has been added, and an error message will be displayed if the date entered is an invalid date on the <strong>Risk Factors Tab</strong> for the question Received transfusion of blood/blood components (other than clotting factor).</p>
<p>![](ror-1-5-42-user-manual/319.png)</p>
<p>A future date check has been added, and an error message will be displayed if the date entered is a future date on the following tabs:</p>
<ul>
<li><p><strong>Risk Factors Tab</strong></p></li>
</ul>
<blockquote>
<p>For the question Received transfusion of blood/blood components (other than clotting factor).</p>
</blockquote>
<p>![](ror-1-5-42-user-manual/320.png)</p>
<ul>
<li><p><strong>Clinical Status Tab</strong></p></li>
</ul>
<blockquote>
<p>For the question Did the patient ever have an AIDS OI?</p>
</blockquote>
<p>![](ror-1-5-42-user-manual/321.png)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

See Figure 88 Figure 87and surrounding text for more information on using the Patient Data Editor.

### Clinical Status tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/322.png) The Clinical Status tab on the Patient Data Editor window allows you to enter or view information regarding the patient’s current clinical status. Refer to Figure 88 for more information

### Optional Risk Factors tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/323.png) In CCR:HIV, the Risk Factors tab lists a series of questions from the CDC form regarding HIV risk behavior. These questions are optional, however if you choose to answer the questions, check Yes, No, or Unk. (unknown) for each question.

### Local Fields tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/324.png) The Local Fields tab allows you to enter registry-specific information regarding the patient’s health history in locally configured fields (see page [126](#adding-local-fields) for details).

### Editing a Patient Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow this procedure to edit or update a patient record. This procedure is typically used by CCR:HIV users to add or update information regarding AIDS-defining opportunistic infections (AIDS-OI) or HIV risk behavior information. This procedure is also used in both CCR:HIV and CCR:HEPC to update information in Local Fields.

1.  In the Registry tab view, search for the patient to be edited. The patient(s) matching the search criteria are displayed in the Patient List.
2.  Double-click the patient name, or click the patient name and then click the \[Edit\] button. The Patient Data Editor window displays.

> ![](ror-1-5-42-user-manual/325.png)

<span id="_Ref22630416" class="anchor"></span>Figure 88 – Patient Data Editor (Record Selected for Editing)

3.  In the Clinical Status tab view, select a value for Was your VHA facility/station the first health care setting (VA or non-VA) to diagnose HIV? (CCR:HIV only).
4.  In the Clinical Status tab view, select a value for Did the patient ever have an AIDS OI? If Yes is selected, enter the date of the diagnosis in the Date of AIDS OI box. (CCR:HIV only)

| ![](ror-1-5-42-user-manual/326.png) | Note: The Check if patient ever had an AIDS-OI checkbox is automatically selected and the Date of AIDS-OI field is populated. If an indicator disease Def box is selected in Section VIII of the CDC form in the Clinical Status section. [^8] |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

1.  If the Check if patient ever had an AIDS-OI checkbox is previously selected (manually or automatically), neither its status nor the date is automatically updated when indicator diseases are updated.
2.  The Date of AIDS OI field uses the date of the first indicator disease listed on the CDC form.
3.  Because the indicator disease date only uses month and year to populate the Date of AIDS OI field, the day is always 1.
- If month is omitted, January is used.
- If both month and year are omitted, current month and year are used.
5.  In the Risk Factors tab view, click the Yes, No, or Unk (Unknown) checkboxes to update the patient’s HIV risk behavior information. (CCR:HIV only)

![](ror-1-5-42-user-manual/327.png)

<span id="_Ref70871930" class="anchor"></span>Figure 89 – Patient Data Editor (Risk Factors Tab)

6.  In the Local Fields tab view, click the checkboxes to add or update information as necessary. The Local Fields tab may not be visible if your site does not use local fields.
7.  When you have completed your entries in the Patient Data Editor, click the appropriate button to close the window:
- \[Delete\] to delete the patient from the registry; you will be asked to confirm the delete action
- \[Save\] to save the changes made to the record
- \[Cancel\] to close the Patient Data Editor window without saving the changes

### Deleting a Patient Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow these steps to delete a patient record:

1.  In the Registry tab view, search for the patient to be deleted. The patient(s) matching the search criteria are displayed in the Patient List.
2.  Click the name of patient to be deleted, and then click \[Delete\], or select Delete from the right-click menu. The confirmation dialog box displays.
3.  Click \[Yes\] to complete the delete process, or click \[No\] to cancel.

## CDC Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/328.png) | Note: The CDC window is available only in CCR:HIV. You must have found at least one patient before using this window. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|

![](ror-1-5-42-user-manual/329.png) You can open the CDC window using the \[CDC\] button on the Registry tab; by selecting CDC from the Registry menu; or by selecting CDC from the right-click menu in the Patient List:

![](ror-1-5-42-user-manual/330.png)

<span id="_Toc167263855" class="anchor"></span>Figure 90 – CDC Window

The CDC window allows you to enter the information necessary to complete the 10 sections of the CDC Adult HIV/AIDS Confidential Case Report for a patient, edit some of the fields, and view and print a patient’s existing CDC report.

The CDC window displays two panes.

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><p>The left pane contains CDC parameter groups, a list of the ten sections of the CDC report.</p>
<p>![](ror-1-5-42-user-manual/331.png)</p>
<p><span id="_Toc167263856" class="anchor"></span>Figure 91 – CDC Window (Parameter Groups pane)</p></th>
<th><p>The right pane displays the form used to enter the patient’s data.</p>
<p>![](ror-1-5-42-user-manual/332.png)</p>
<p><span id="_Toc167263857" class="anchor"></span>Figure 92 – CDC Window (Patient Data pane)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

You can navigate to each of the 10 sections of the CDC report by using the scroll bar, or by clicking the Group Title of the desired section under CDC parameter groups in the left pane.

![](ror-1-5-42-user-manual/333.png) You can hide or display this pane by clicking the \[<u>G</u>roup Titles\] command icon.  
The following tabs are displayed above the right pane of the CDC window:

- Form
- Preview
- Preview (page 2)

### Form tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/334.png) The <u>F</u>orm tab displays the GUI through which you can enter a patient’s information. The information is displayed on the completed Adult HIV/AIDS Confidential Case Report.

### Preview tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/335.png) The Pre<u>v</u>iew tab display shows you how the CDC report will appear when printed. The Preview tab displays the first page of the 2-page CDC Adult HIV/AIDS Confidential Case Report, which contains sections I through VI.

### Preview (page 2) tab 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/336.png) The Preview (page 2) tab display shows you how the CDC report will appear when printed. The Preview (page 2) tab displays the second page of the 2-page CDC Adult HIV/AIDS Confidential Case Report, which contains sections VII through X.

### <u>P</u>rint icon

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/337.png) The \[<u>P</u>rint\] command icon allows you to print the selected patient’s CDC report.

### Print Blank icon

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/338.png) The \[Print Blank\] command icon allows you to print a blank CDC report.

### <u>S</u>ave button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/339.png) The \[Save\] button saves the information entered from the CDC Form tab and automatically closes the CDC window.

### Cancel button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/340.png) The \[Cancel\] button closes the CDC form without saving any changes made.

### Zoom <u>I</u>n and Zoom <u>O</u>ut icons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/341.png)</p>
<p>![](ror-1-5-42-user-manual/342.png)</p></th>
<th>The [Zoom <u>I</u>n] and [Zoom <u>O</u>ut] command icons allow you to incrementally enlarge or reduce the Preview and Preview (page 2) tab displays within the CDC window.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Fit <u>W</u>idth icon

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/343.png) The \[Fit <u>W</u>idth\] command icon automatically adjusts the size of the Preview and Preview (page 2) display to fit the width of the CDC window.

### Zoom <u>1</u>:1 icon

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/344.png) The \[Zoom <u>1</u>:1\] command icon automatically enlarges the Preview and Preview (page 2) tab display at a 1:1 ratio.

### AutoFit checkbox

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/345.png) The AutoFit checkbox automatically adjusts the size of the form so that it fits the width of the window when the window is resized.

### Close the CDC form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you have completed your entries on the CDC form, close the CDC window by doing one of the following on any of the ten CDC form parts:

- \[Save\] to save the record
- \[Cancel\] to cancel any changes to CDC information

## Viewing a Patient’s CDC Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Registry tab, select a patient from the Patient List display.
2.  ![](ror-1-5-42-user-manual/346.png) Click the \[CDC\] button.

> The CDC window displays the selected patient’s CDC report. Use the Preview and Preview (page 2) tabs to view how the CDC report will appear when printed.

## Printing a Patient’s CDC Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Registry tab, select a patient from the Patient List display.
2.  ![](ror-1-5-42-user-manual/347.png) Click the \[CDC\] button.

> The CDC window displays the selected patient’s CDC report. Use the Preview and Preview (page 2) tabs to view how the CDC report will appear when printed.

3.  ![](ror-1-5-42-user-manual/348.png) Click the \[<u>P</u>rint\] command icon. The Print dialog displays (note that your options may vary from those shown here):

> ![](ror-1-5-42-user-manual/349.png)

<span id="_Toc167263858" class="anchor"></span>Figure 93 – Print dialog

4.  Select any necessary printing options from the Print dialog, and then click \[OK\].

## Entering Information on a Patient’s CDC Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following procedure can be used to create a new CDC report for a patient, or edit the information on a patient’s existing CDC report.

1.  From the Registry tab, select the patient from the Patient List display.
2.  ![](ror-1-5-42-user-manual/350.png) Click the \[CDC\] button. The multi-part CDC window displays:

![](ror-1-5-42-user-manual/351.png)

<span id="_Toc167263859" class="anchor"></span>Figure 94 – CDC Window

3.  ![](ror-1-5-42-user-manual/352.png) Make sure the <u>F</u>orm tab is selected.
4.  ![](ror-1-5-42-user-manual/353.png) From the <u>F</u>orm tab, use the \[<u>G</u>roup Titles\] command icon or the scroll bar to navigate to the field(s) you want to enter/edit.
5.  ![](ror-1-5-42-user-manual/354.png) After entering the patient’s information or editing the existing information, click \[Save\].

> The patient’s CDC report is saved and the CDC window automatically closes.

> Detailed information regarding each of the Group Title sections of the CDC report is provided in the following figures and accompanying text.

![](ror-1-5-42-user-manual/355.png)

<span id="_Toc167263860" class="anchor"></span>Figure 95 – Sections I, II, and III of the CDC Form

### SECTION I – STATE AND LOCAL USE ONLY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/356.png) Information in this section is read-only and cannot be entered or edited from the <u>F</u>orm tab. The address is obtained from PATIENT file \#2. If there is an error in the address, contact Patient Registration to correct the Patient File which will then populate the CDC form with the corrected information.

### SECTION II – DATE FORM WAS COMPLETED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/357.png) The current date is the default date and will be displayed automatically. To change the date, enter or select from the drop-down calendar the date that the CDC report form was completed. The date must be the current date or earlier. A future date cannot be entered.

### SECTION III – DEMOGRAPHIC INFORMATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/358.png) The following information can be entered or edited from this section:

- The patient’s diagnostic status at the time of the report, and the age of the patient at the time of the diagnosis.
- The patient’s country of birth, and the city, state, county, and country in which the patient resided at the time of the diagnosis.

The other fields in section III are read-only and cannot be entered or edited from the Form tab. The date of birth, current status, sex, ethnicity and race information is obtained from the Patient File \#2. If there are errors in these fields, please contact Patient Registration to correct the Patient File which will then populate the CDC form with the corrected information.

![](ror-1-5-42-user-manual/359.png)

<span id="_Toc167263861" class="anchor"></span>Figure 96 – Sections IV and V of the CDC Form

### SECTION IV – FACILITY OF DIAGNOSIS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/360.png) The following information can be entered or edited from this section:

- Facility Name – Enter the name of the facility where the patient was diagnosed.
- City – Enter the name of the city in which the facility is located.
- State – From the drop-down list, select the name of the state in which the facility is located.
- Country – Enter the name of the country in which the facility is located.
- Facility Setting – Select the appropriate facility setting by clicking a checkbox: Public, Private, Federal, or Unk. (unknown).
- Facility Type – Select the appropriate facility type by clicking a checkbox: Physician, HMO; Hospital, Inpatient; or Other. If Other, enter the type of facility in the field provided.

### SECTION V – PATIENT HISTORY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/361.png) The Patient History section is read-only and displays the information entered from the Risk Factors tab on the Patient Data Editor window.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/362.png)</th>
<th><p><strong>Note:</strong> Patch ROR*1.5*15 corrected two issues in the Patient History section on the CDC form:</p>
<p>When a user answers the question After 1977 and preceding the first positive HIV antibody test or AIDS diagnosis this patient had: HETEROSEXUAL relations with any of the following: Bisexual male; Intravenous Injection drug user, the checkbox values are transposed in the Center for Disease Control (CDC) form. When the user makes a selection in the Patient Editor, the appropriate checkbox will be checked in the CDC form.</p>
<p>When a user selects Yes to the question Received clotting factor for hemophilia/coagulation disorder in the Patient Editor, the Yes checkbox in the CDC form is not checked. When the user makes a selection in the Patient Editor, the appropriate checkbox will be checked in the CDC form.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### SECTION VI – LABORATORY DATA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/363.png)

<span id="_Toc167263862" class="anchor"></span>Figure 97 – Section VI of the CDC Form

![](ror-1-5-42-user-manual/364.png) This section is divided into four subsections:

## HIV ANTIBODY TESTS AT DIAGNOSIS (Indicate first test):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/365.png) If the tests listed in this section were performed, use the checkboxes and fields to indicate the month and year (MM/YY) the test(s) were performed and one of the following results:

- ![](ror-1-5-42-user-manual/366.png) Pos (positive)
- ![](ror-1-5-42-user-manual/367.png) Neg (negative)
- ![](ror-1-5-42-user-manual/368.png) Ind (indeterminate)

![](ror-1-5-42-user-manual/369.png) Use the Not Done checkbox to indicate that a test was not performed. If a test other than those listed was used, enter the name of the Other HIV antibody test in the field provided, and use the checkboxes to record the outcome of the test.

## POSITIVE HIV DETECTION TEST (Record earliest test) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/370.png) Use the checkboxes to select the type of test. Enter the month and year (MM/YY) of the test in the field provided. If a test other than the ones listed was used, specify the type of test in the field provided.

## DETECTABLE VIRAL LOAD TEST (record most recent test)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/371.png) Select one of the following test types from the Test Type drop-down list:

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/372.png)</th>
<th><ul>
<li><p>NASBA (Organon)</p></li>
<li><p>RT-PCR (Roche)</p></li>
<li><p>bDNA (Bayer)</p></li>
<li><p>Other</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Enter the COPIES/ML for the selected test type in the fields provided.

If applicable, enter the month and year (MM/YY) and test type of the last documented negative HIV test in the fields provided.

| ![](ror-1-5-42-user-manual/373.png) | Note: Data *must* be entered manually, even if the test was performed at the VA facility, and data entered here does *not* become part of the patient’s record in CPRS or CCR. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Use the applicable checkbox to indicate whether the HIV diagnosis is documented by a physician. If the Yes checkbox is selected, enter the date the physician documented the HIV diagnosis in the field provided.

## IMMUNOLOGIC LAB TESTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/374.png) Type the applicable CD4 counts and percentages, and the month and year (MM/YY) of each of the tests in the fields provided.

| ![](ror-1-5-42-user-manual/375.png) | Note: Data must be entered manually, even if the test was performed at the VA facility, and data entered here does *not* become part of the patient’s record in CPRS or CCR. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/376.png)</p>
<p><span id="_Toc167263863" class="anchor"></span>Figure 98 – Sections VII and VIII of the CDC Form</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### SECTION VII – STATE AND LOCAL USE ONLY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/377.png) Note that background of the Physician field is other than white, indicating that you cannot type directly into the field. You must use the \[Select\] button to insert the name of the physician in the Physician field.

1.  ![](ror-1-5-42-user-manual/378.png) Click the \[Select\] button.

> The VistA User Selector window displays:

> ![](ror-1-5-42-user-manual/379.png)

<span id="_Toc167263864" class="anchor"></span>Figure 99 – VistA User Selector pop-up

> The Medical Record No. field is automatically populated with the selected patient’s medical record number.

2.  ![](ror-1-5-42-user-manual/380.png) Type the full or partial last name of the physician, then press \< Enter \> or click \[Find the Physician\].

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>The list will update to display those physician names that match the search criteria.</th>
<th><p>![](ror-1-5-42-user-manual/381.png)</p>
<p><span id="_Toc167263865" class="anchor"></span>Figure 100 – VistA User Selector (showing search results)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Select the name of the physician from the list, and then click \[<u>S</u>elect Physician\].

> The VistA User Selector window automatically closes and the selected name will be displayed in the Physician field of the CDC form.

> The selected physician’s Phone number and Hospital information will be automatically populated in the fields provided. The current user’s name and phone number automatically populate the Person Completing Form and Phone fields.

### SECTION VIII – CLINICAL STATUS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 56%" />
<col style="width: 11%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/382.png)</th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>![](ror-1-5-42-user-manual/383.png)</p>
<p><span id="_Toc167263866" class="anchor"></span>Figure 101 – Section VIII of the CDC Form</p></td>
<td><p>Use the applicable checkboxes to indicate whether the patient’s clinical record was reviewed.</p>
<p>Enter the month and year (MM/YY) the patient was diagnosed as asymptomatic or symptomatic in the fields provided.</p>
<p>Use the checkboxes to select the applicable AIDS INDICATOR DISEASES. Use the Def. checkbox to indicate a definitive diagnosis and the Pres. checkbox (when provided) to indicate a presumptive diagnosis. Enter the month and year (MM/YY) of the diagnosis for each selected disease in the field provided.</p></td>
</tr>
</tbody>
</table>

| ![](ror-1-5-42-user-manual/384.png) | Note: When an indicator disease Def checkbox is selected, the Check if patient ever had an AIDS-OI checkbox and the Date of AIDS-OI field are automatically populated on the Patient Data Editor in the Clinical Status tab of the Registry tab. [^9] |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

All reporting areas (i.e., the 50 states, the District of Columbia, Puerto Rico, and other U.S. jurisdictions in the Pacific and Caribbean) report tuberculosis (TB) cases to the CDC using a standard case report form. If the selected patient has been diagnosed with M. tuberculosis, pulmonary and/or M. tuberculosis, disseminated or extrapulmonary, type the applicable Report of a Verified Case of Tuberculosis case number in the RVCT CASE NO. field.

Use the applicable checkbox to indicate whether in the absence of positive HIV test results, the patient has an immunodeficiency that would disqualify him/her from the AIDS case definition. Select Yes, No, or Unk. (unknown).

### SECTION IX – TREATMENT/SERVICES REFERRALS (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/385.png) This section of the CDC report is optional.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/386.png)</p>
<p><span id="_Toc167263867" class="anchor"></span>Figure 102 – Section IX of the CDC Form</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Use the applicable checkboxes to indicate:

- Whether the patient has been informed of his/her HIV infection
- Whether the patient’s partners will be notified about HIV exposure, and the resource that will be used to provide counseling
- The types of services to which the patient has been referred or is receiving
- Whether or not the patient is receiving or has received anti-retroviral therapy and/or PCP prophylaxis
- Whether or not the patient has been enrolled in a clinical trial, and whether the clinical trial is NIH sponsored
- Whether or not the patient has been enrolled in a clinic and whether the clinic is HRSA sponsored
- The *primary* source of reimbursement for the patient’s treatment

![](ror-1-5-42-user-manual/387.png) The FOR WOMEN subsection allows you to enter information specific to female patients. This subsection will be unavailable for male patients.

Use the applicable checkboxes to indicate:

- If the patient is receiving or has been referred to gynecological services
- If the patient is currently pregnant
- If the patient has delivered live born infants. If Yes is checked, complete these additional fields:

> Select the Child’s Date of Birth, and then enter the name of the hospital at which the child was born, the city and state in which the hospital is located, and the child’s Soundex and Patient Numbers in the fields provided.

### SECTION X – COMMENTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/388.png) Type your comments in the field provided. The Comments field can accommodate 300 characters.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](ror-1-5-42-user-manual/389.png)</p>
<p><span id="_Toc167263868" class="anchor"></span>Figure 103 – Section X of the CDC Form</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](ror-1-5-42-user-manual/390.png) Click the \[Save\] button to save any changes, or…

![](ror-1-5-42-user-manual/391.png) Click \[Cancel\] to close without saving.

# Registry Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A key benefit of the CCR is its reporting capability. Approximately eighteen standard reports are available in both Clinical Case Registries, and one additional report is available in CCR:HIV.

All of these reports are set up from the Reports menu. You can set specific reporting options for each report, and schedule a date and time for the report to run. After the report is generated, you can view, save, and print the report from the Task Manager tab.

Improved reporting functionality allows clinicians and administrators to:

- Track important aspects of care through customizable report parameters, including “*not”* logic (for example, find patients on drug X who *did not* have a particular lab test)~
- Save report parameters for later re-use
- \[Search\] the population of patients co-infected with both Hepatitis C and HIV, and return results on a single integrated report
- Create patient-based Divisional reporting

See Section 10 Local Reports for detailed information and examples of each report.

## Registry Reports Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Registry Reports window is the window from which you can select the specific parameters and criteria used to generate the selected report. The Registry Reports window can be displayed in a single pane, or 2-pane mode. When the Registry Reports window is accessed from the Report menu, Report List menu option, or the New Report button, it is displayed in the 2-pane mode:

![](ror-1-5-42-user-manual/392.png)

<span id="_Toc167263869" class="anchor"></span>Figure 104 – Sample Report Setup window, Double-Pane Mode (showing "Show Report List" option)

The left pane displays the List of Reports from which you can select a report to run. The right pane displays the reporting criteria that you can select for the report.

![](ror-1-5-42-user-manual/393.png)You can hide or display the List of Reports via the Show Report List box. To show the reports in single-pane mode, uncheck the Show Report List box:

![](ror-1-5-42-user-manual/394.png)

<span id="_Toc167263870" class="anchor"></span>Figure 105 – Sample Report Setup window, Single-Pane Mode

### Accessing the Registry Reports Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can access the Registry Reports window using the following methods:

- Select a report from the Reports menu
- Select Reports List from the Reports menu
- Click the \[New Report\] button in the Task Manager view
- Select New Report from the right-click menu in the Task Manager view

## Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reports menu displays the list of all available reports. When you select a report from the list, a secondary Registry Reports window displays the specific parameters and criteria that you can select to generate the report.

- You can also select Report List from the Reports menu. When you select this option, the Registry Reports window displays a list of all available reports on the left side of the window. You can select a report to generate from this List of Reports, and the selected report is identified with an arrow. The right-side pane displays the specific parameters and criteria that you can select to generate the report.

## New Report button and right-click menu option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Task Manager tab view, you can access the Registry Reports window by clicking the \[New Report\] button, or by selecting New Report from the right-click menu.

The Registry Reports window displays a list of all available reports on the left side of the window. You can select a report to generate from this List of Reports, and the selected report is identified with an arrow. The right pane displays the specific parameters and criteria you can select to generate the report.

### Date Range Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most registry reports allow you to set Date Range parameters to determine the window of time from which to capture the data for the report.

If date range parameters are incorrectly set, a warning will prompt you to check the Report Period parameters when you click the \[Run\] button. For example, if a Quarter is selected but no Year, you will be warned that the Year or Quarter value is not valid.

See Pop-up Calendars on page [87](#pop-up-calendars) for information on how to use the various pop-up calendar functions.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Parameters</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Year</td>
<td><p>Enter the four digit year in <strong>YYYY</strong> format.</p>
<p>The Year date range parameter will include all relevant data within the selected calendar year (January 1 through December 31) on the report. Check the <strong>Fiscal</strong> box to include all data within the selected fiscal year (October 1 through September 30) on the report.</p></td>
</tr>
<tr class="even">
<td>Quarter</td>
<td><p>Select a quarter (<strong>I – IV</strong>) from the drop-down list.</p>
<p>Used with the Year date range parameter, the Quarter parameter allows you to include on the report only relevant data within the selected quarter of the selected year. The appropriate date range is automatically selected for calendar or fiscal quarters.</p></td>
</tr>
<tr class="odd">
<td>Custom</td>
<td><p>Use the Custom date range parameter to include on the report only relevant data within a selected date range inclusive of the selected start and end dates of the date range.</p>
<p>Enter the start date of the date range in the left-side field, or click the left arrow button next to the field to automatically set the date field to 12/30/1899 to include all data.</p>
<p>Enter the end date in the right-side field, or click the right arrow button next to the field to set the date field to the current date.</p></td>
</tr>
<tr class="even">
<td>Cut Off</td>
<td><p>Define a time range to be included on the report using the Cutoff option. Enter a value for the amount of time, in days, to “go back” from the current date, using digits and the &lt; W &gt; and &lt; M &gt; keys to specify the number in weeks or months.</p>
<p>For example, enter <strong>20</strong> in the Cut Off field to include data from the last 20 days through the current day on the report. <strong>30W</strong> will include data from the last 30 weeks through the current day, and <strong>2M</strong> will include data from the last two months through the current day.</p></td>
</tr>
</tbody>
</table>

### Include Patients Confirmed in the Registry checkboxes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many of the reports allow you to include patients who were added to the registry before, during, and/or after the selected date range by checking one or more of the checkboxes provided. An error message will display if no checkbox is selected.

### Other Registries modes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“Modes” replace the checkboxes formerly available in this section.[^10]

Many of the reports include patients who appear in the registry that you are signed into with the option to include/exclude[^11] patients who are in any other registry selected to which the user has keys. See [selecting a mode](#SelectMode) for instructions on using the Mode selector.

The software checks the registries associated with specified patients and/or registries not associated with specified patients. If not marked, the registries are ignored.

### Load / Save / Default Parameters Buttons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The \[<u>L</u>oad Parameters\] and \[<u>S</u>ave Parameters\] buttons allow you to save and later reuse a report set up. These buttons are located at the bottom of the Registry Reports window and are available for all reports.

The \[<u>D</u>efault Parameters\] button allows you to clear current values and load default parameters for a report.[^12]

When you click \[<u>S</u>ave Parameters, all the selections you have made in each section of the Registry Reports window will be stored as a template.

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><p>When you click [<u>L</u>oad Parameters]<strong>,</strong> two lists of saved templates will be displayed– Common Templates are issued with the software package and are available to all users; Your Templates are available only to you, not to all registry users – and you can select one to automatically “fill in” the fields of the report form.</p>
<p>When you load a template, it will overwrite what you have already entered on a screen. Once a template is opened, you can modify the parameters to meet your current needs.</p>
<p>You can delete a template by selecting it and then clicking the ![](ror-1-5-42-user-manual/395.png) button next to the template list selector (at right, shown as “grayed out”).</p></th>
<th><p>![](ror-1-5-42-user-manual/396.png)</p>
<p><span id="_Toc167263871" class="anchor"></span>Figure 106 – Open Report Parameters pop-up (showing “Delete” command icon)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Generating a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a general procedure for selecting and setting up a report in CCR; not all of these options and settings are available in each report, but the process is essentially the same for all reports. If you want detailed information for a particular report, see the Local Reports section for more information.

1.  Select a report from the Reports menu. The Registry Reports window displays the reporting criteria selections for the selected report.
2.  Select a Date Range, if applicable, for the selected report. See the [Date Range Parameters](#_Generating_a_Report) topic for more information.
3.  Select a date and time in the Scheduled to Run on section. If no other date and time are specified, the report will begin running immediately.

| ![](ror-1-5-42-user-manual/397.png) | Note: Some reports require little processing and can quickly retrieve and display the data for the selected report. However, reports that are likely to require more processing time – such as those with large numbers of patients and/or several variables – should be scheduled to run on a date and time when VistA server resources are not being used as heavily. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

4.  Select a Repeat interval, if desired: select 1D to repeat this report each day after its first run, or select 1M to repeat it one month from its first run. To run this report on the first of each month at 4:00 AM, select 1M(1@4AM). Leave this field blank if repeated reporting is not required.
5.  Check one or more of the Include Patients Confirmed to the Registry checkboxes to include patients who were added to the registry before, during, and/or after the selected date range, or any combination of the three. See [Include Patients Confirmed in the Registry](#include-patients-confirmed-in-the-registry) for more information.

| ![](ror-1-5-42-user-manual/398.png) | Note: Patch ROR\*1.5\*10 introduced a new capability for several reports by adding a new \[All Registry Meds\] button on the Medications panel for the Combined Meds and Labs, Patient Medication History, and Pharmacy Prescription Utilization reports. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

6.  ![](ror-1-5-42-user-manual/399.png) The \[All Registry Meds\] button defaults to not available (“grayed out”).

> ![](ror-1-5-42-user-manual/400.png) The button becomes available when you choose Selected only (rather than Include all) under Medications:

> ![](ror-1-5-42-user-manual/401.png)

<span id="_Toc167263872" class="anchor"></span>Figure 107 – Medications pane, showing "All Registry meds" button

When the \[All Registry Meds\] button is clicked, all the Registry medications are displayed, and you may select one or more medications to be included in the report. Before selecting any medications, however, you must enter a name for the first group in the field on the right-hand pane. If you do not do so, you will see an error popup:

![](ror-1-5-42-user-manual/402.png)

<span id="_Toc167263873" class="anchor"></span>Figure 108 – Group Name Reminder pop-up

Enter the Group Name…

![](ror-1-5-42-user-manual/403.png)

<span id="_Toc167263874" class="anchor"></span>Figure 109 – Entering and Adding the Group Name

…and then click the large plus sign ( ![](ror-1-5-42-user-manual/404.png) ) button to add the group to the right column. The Group Name (for example, “MyGroup”) is then displayed in the right column of the pane:

![](ror-1-5-42-user-manual/405.png)

<span id="_Toc167263875" class="anchor"></span>Figure 110 – Group Name Displayed

Make your selection(s) from the left-hand column by clicking on the medication name and then clicking the right arrow to move the medication to the right column of the pane. Select and click the left arrow (only available when at least one medication is in the right column) to remove that medication from your list. Use the double arrows to move *all* medications to/from the right column.

![](ror-1-5-42-user-manual/406.png)

<span id="_Toc167263876" class="anchor"></span>Figure 111 – Selecting Medications

7.  Select the additional criteria specific to the selected report that you want to include. Refer to the [Local Reports](#_ICR_Reports) section for detailed information regarding each of the reports.
8.  Click the \[Run\] button to request the report.

> ![](ror-1-5-42-user-manual/407.png)

<span id="_Toc167263877" class="anchor"></span>Figure 112 – Requested Report in Task Manager

> The Task Manager tab will display the reports that have been requested. If the report is scheduled to run in the future, the date and time the report is scheduled to run will be displayed in the Scheduled column. The Status column will display the status of the report being run. The Progress column will display the progress of the report as a percentage of completion.

> ![](ror-1-5-42-user-manual/408.png) Click the \[Refresh\] button to update the Progress column.

> The generated report will be displayed in Task Manager for two weeks. After two weeks, the system will automatically delete the report from the list. You can access the report at any time during the two-week window to view, sort, print, delete, and/or save the report to an alternate location. Refer to the [Managing Reports from Task Manager](#managing-reports-from-the-task-manager-view) section for more information.

### Scheduling a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Scheduled to Run on section of the Registry Reports window to set a date, time, and frequency to run the selected report.

1.  Enter the date on which you want to report to run in the Day field.
2.  Select a time for the report to run in the At field. Click the hour in the time field, and then use the arrow buttons to select the hour. Repeat this process for minutes, seconds, and AM/PM options.
3.  To run the selected report once, leave the Repeat field empty. To automatically repeat the report, select a time interval from the Repeat drop-down list:
- Select 1D to run the report once each day at the selected time.
- Select 1M to run the report monthly on the same date each month.

| ![](ror-1-5-42-user-manual/409.png) | Note: Be sure that the date selected for monthly recurring reports occurs in each subsequent month. For example, a monthly recurring report that is set to run on the 31<sup>st</sup> will not be produced for months that have less than 31 days |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

- Select 1M(1@4AM) to run the report on the first day of each month at 4AM.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/410.png)</th>
<th><blockquote>
<p><strong>Note:</strong> Enter a future date to prevent the report from running immediately.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Enter a comment up to 60 characters in the Comment field. This Comment will display on the Task Manager (and in the header on the finished report) and can be used to provide report characteristics to help distinguish reports if you are running multiple reports.

4.  When you have completed each section of the report window, click \[Run\] to queue the report.

### Discontinuing a Scheduled Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a report that is scheduled to run repeatedly at specified intervals is no longer needed, you can discontinue the report in the future by performing the following steps:

1.  In the Task Manager tab view, locate the task description for the next date and time the report is scheduled to run. Click the task to select it. Note that when a task is selected, the \[<u>D</u>elete\] button comes active:

![](ror-1-5-42-user-manual/411.png)

<span id="_Toc167263878" class="anchor"></span>Figure 113 – Report Selected (note Delete button available)

2.  ![](ror-1-5-42-user-manual/412.png) Click the \[<u>D</u>elete\] button, or select <u>D</u>elete from the right-click menu. A confirmation dialog box displays.

> ![](ror-1-5-42-user-manual/413.png)

<span id="_Toc167263879" class="anchor"></span>Figure 114 – Task Deletion Confirmation pop-up

3.  Click \[<u>Y</u>es\] (or \[Yes to <u>A</u>ll\] if more than one task has been selected). The scheduled report(s) will be discontinued.<span id="_ICR_Reports" class="anchor"></span>

# Local Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the local reports, in the main Registr<u>y</u> window, select the Re<u>p</u>orts menu, and select the appropriate report. Table 76 lists each report, its function and the panes included in the report. To view instructions for each included field, click the hyperlink in the Panes Included column. When all of the fields in the report are completed, click:

1.  Run. Click \[Run\]; The report is added to the Task Manager tab and will run at the specified date and time.
2.  Cancel. To discard your entries and cancel the report, click \[Cancel\].

The following reports are available for all registries and will function as intended for the Hepatitis C and HIV registries, without change.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>BMI by Range Report</p></li>
<li><p>Clinic Follow Up Report</p></li>
<li><p>Combined Meds and Labs Report</p></li>
<li><p>Current Inpatient List Report</p></li>
<li><p>Diagnosis Report</p></li>
<li><p>General Utilization and Demographics Report</p></li>
<li><p>Hepatitis A Report</p></li>
<li><p>Hepatitis B Report (not available to Hepatitis B registry)</p></li>
<li><p>Inpatient Utilization Report</p></li>
</ul></th>
<th><ul>
<li><p>Lab Utilization Report.</p></li>
<li><p>Liver Score by Range Report</p></li>
<li><p>List of Registry Patients Report</p></li>
<li><p>Outpatient Utilization Report</p></li>
<li><p>Patient Medication History Report</p></li>
<li><p>Pharmacy Prescription Utilization Report</p></li>
<li><p>Procedures Report</p></li>
<li><p>Radiology Utilization Report</p></li>
<li><p>Renal Function by Range Report</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The following local reports are only available for the Hepatitis C and HIV registries. These reports will not be displayed in the Reports List of any other registry:

- DAA Lab Monitoring Report (HEPC Only)
- Potential DAA Candidates Report (HEPC Only)
- Registry Lab Tests by Range Report
- Registry Medications.
- Sustained Virologic Response Report (HEPC Only)
- VERA Reimbursement Report (HIV Only)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 68%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Report Name</th>
<th>Report Function</th>
<th>Panes Included</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Body Mass Index (BMI) by Range</td>
<td>The BMI by Range report is one of three “by range” reports introduced by Patch ROR*1.5*10. It provides a list of patients whose body mass index (BMI) is within a user-specified range (low to high) and within a specified date range or the most recent observation. A complete or summary report is available.</td>
<td><p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#future-appointments">Future_Appointments</a></p>
<p><a href="#Report_Type">Report Type</a></p>
<p><a href="#BMI_Date_Range">BMI Date Range</a></p>
<p><a href="#BMI_Result_Range">BMI Result Ranges</a></p>
<p><a href="#Utilization_Date_Range">Utilization Date Range</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="even">
<td>Clinic Follow Up</td>
<td>The Clinic Follow Up report is designed to help you identify patients who have or have not attended specified clinics in your health care system. This report displays a list of living patients who were or were not seen in selected clinics, and/or received any care during the selected date range selected.</td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#clinic-follow-up-report-patients-pane">Patients</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="odd">
<td>Combined Meds and Labs</td>
<td><p>The Combined Meds and Labs report is a complex report that identifies patients in the registry who received specific medication and/or specific laboratory tests within a specified date range. This report can be run for pharmacy alone, laboratory alone, or both. In addition, a range can be placed on numeric lab test results to permit searching for patients with particular values.</p>
<p>This report identifies patients using the following basic logic:</p>
<ul>
<li><p>People who did or did not receive medication(s) (single or groups) and/or</p></li>
<li><p>People who did or did not receive lab test(s) (you can filter values for numeric tests)</p></li>
<li><p>People who had some type of utilization</p></li>
</ul>
<p>The date ranges can vary between these three areas to permit, for example, the viewing of labs for an extended period beyond the prescription period. These three main filters along with specific medication and lab test selection can be used to run queries of the following types:</p>
<ul>
<li><p>Find patients with particular lab results who are not receiving medication for this condition (<em>e.g.,</em> high cholesterol who are not on a statin).</p></li>
<li><p>Find patients receiving a medication who are not receiving appropriate monitoring (<em>e.g.,</em> on ribavirin who have not had a CBC).</p></li>
</ul>
<p>Queries can also be constructed to answer complex questions such as “Are patients on contraindicated drug combinations and if there is a lab test marker for toxicity or treatment failure, who has abnormal labs?”</p>
<p>Both the input screen and the output format of the Combined Meds and Labs report were modified for CCR 1.5.<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p>
<p>When both Received selected medication(s) <em>and</em> Selected lab tests were performed are selected, the report contains a set of meds tables and a set of labs tables by patient.</p>
<blockquote>
<p><em>Example:</em> Patient A – Meds, Labs; Patient B – Meds, Labs<br />
Meds table is sorted by medication names in ascending order.<br />
Labs table is sorted by test names in ascending order and then by result dates in descending order.</p>
</blockquote>
<p>When either Received selected medication(s) <em>or</em> Selected lab tests were performed is selected, the report contains lists of patients in separate labs tables and meds tables.</p>
<p>When both Did not receive selected medication(s) <em>and</em> No selected lab tests were performed are selected, the report contains a list of patients who have neither labs nor meds.</p>
<p>The Only patients who have received any care during the date range checkbox is mainly used with Did not receive selected medication(s) and No selected lab tests were performed.</p></td>
<td><p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#future-appointments">Future_Appointments</a></p>
<p><a href="#combined-med-labs-report-patients-pane">Patients</a></p>
<p><a href="#medications-date-range">Medications Date Range</a></p>
<p><a href="#medications">Medications</a></p>
<p><a href="#lab-tests-date-range">Lab Tests Date Range</a></p>
<p><a href="#lab-tests">Lab Tests</a></p>
<p><a href="#Utilization_Date_Range">Utilization Date Range</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="even">
<td>Current Inpatient List</td>
<td><p>The Current Inpatient List report lists the names of patients who are assigned an inpatient bed at the time the report is run. If no active patients are currently inpatients, no report will be generated; however, a notification alert will be sent to the requestor of the report.</p>
<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/414.png)</th>
<th><strong>Note:</strong> To identify a list of inpatients during a specific time period, use the <a href="#_Single_Patient_Drug_History Report">Inpatient Utilization report</a> instead of this one.</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td><p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="odd">
<td>Direct Acting Antivirus (DAA) Lab Monitoring</td>
<td><p>![](ror-1-5-42-user-manual/415.png)The DAA Lab Monitoring report monitors lab results for patients who have been selected to receive HCV registry medications. This report is similar functionally to the Combined Meds &amp; Lab report, but several variables will be preset to prevent user error and to make the report more compact.</p>
<p>To be included in the report:</p>
<ul>
<li><p>Patients must be in the HepC Registry</p></li>
<li><p>Patients must be alive</p></li>
<li><p>Patient must have at least one outpatient, inpatient, refill or partial med fill for Boceprevir and/or Telaprevir within the user selected time frame.</p></li>
</ul></td>
<td><p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#future-appointments">Future_Appointments</a></p>
<p><a href="#daa-prescriptions">DAA Prescriptions</a></p>
<p>DAA Start Date Range</p>
<p>Lab Tests Date Range Weeks After DAA Start</p>
<p>Lab Tests</p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="even">
<td>Diagnoses</td>
<td><p>The Diagnoses report identifies patients who have particular ICD-9 codes for a particular condition. The system searches completed admissions, outpatient visits, and entries in the Problem List file for ICD-9 codes assigned to any registry patients within the selected date range.</p>
<p>The Diagnose<strong>s</strong> report selects a patient only when the patient has at least one ICD-9 code from each non-empty group; otherwise all patient diagnoses are disregarded and not included in counts.<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></p>
<p>Remember that the “ignore, include or exclude” filter is <em>not</em> available for this report.</p></td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#future-appointments">Future_Appointments</a></p>
<p><a href="#Report_Type">Report Type</a></p>
<p><a href="#icd">ICD</a></p>
<p><a href="#Utilization_Date_Range">Utilization Date Range</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="odd">
<td>General Utilization and Demographics</td>
<td>The General Utilization and Demographics report provides a list of patients with specified types of utilization during a defined period. Additional demographic information, such as age and race, can be included in the final report. Patients that have been inactivated due to death are included in this report if they required health care within the selected date range.</td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="\l"><span>OEF/OIF</span></a></p>
<p><a href="\l"><span>SVR</span></a></p>
<p><a href="\l"><span>Additional Identifiers</span></a></p>
<p><a href="#Report_Type">Report Type</a></p>
<p><a href="#type-of-utilization">Type of Utilization</a></p>
<p><a href="#general-utilization-and-demographic-report-options">Report Options</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="even">
<td>Hepatitis A report</td>
<td>Hepatitis A Vaccine report is to identify patients who either had Hepatitis A vaccine or have immunity to the Hepatitis A virus – or to identify patients who have not had the Hepatitis A vaccine and are not immune.</td>
<td><p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="\l"><span>OEF/OIF</span></a></p>
<p><a href="\l"><span>SVR</span></a></p>
<p><a href="\l"><span>Additional Identifiers</span></a></p>
<p><a href="#future-appointments">Future_Appointments</a></p>
<p><a href="#hepatitis-a-report-patients-pane">Patients</a></p>
<p><a href="#vaccination-date-range">Vaccination Date Range</a></p>
<p><a href="#immunity-date-range">Immunity Date Range</a></p>
<p><a href="#lab-tests-date-range">Lab Tests Date Range</a></p>
<p><a href="#lab-tests">Lab Tests</a></p>
<p><a href="#Utilization_Date_Range">Utilization Date Range</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="odd">
<td>Hepatitis B report</td>
<td>Hepatitis B Vaccine report is to identify patients who either had Hepatitis B vaccine or have immunity to the Hepatitis B virus – or to identify patients who have not had the Hepatitis B vaccine and are not immune. Not available for the Hepatitis B registry.</td>
<td><p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="\l"><span>OEF/OIF</span></a></p>
<p><a href="\l"><span>SVR</span></a></p>
<p><a href="\l"><span>Additional Identifiers</span></a></p>
<p><a href="#future-appointments">Future_Appointments</a></p>
<p><a href="#hepatitis-b-report-patients-pane">Patients</a></p>
<p><a href="#vaccination-date-range">Vaccination Date Range</a></p>
<p><a href="#immunity-date-range">Immunity Date Range</a></p>
<p><a href="#lab-tests-date-range">Lab Tests Date Range</a></p>
<p><a href="#lab-tests">Lab Tests</a></p>
<p><a href="#Utilization_Date_Range">Utilization Date Range</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="even">
<td>Inpatient Utilization</td>
<td>The Inpatient Utilization report provides a list of patients or summary data on patients who were hospitalized in a specified period, with the option of additional filters.</td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#general-report-options">Options</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="odd">
<td>Lab Utilization</td>
<td>The Lab Utilization report provides a list of the number of lab orders and lab results during the selected date range. The report can be run for either individual tests or for panels (e.g., Hgb or CBC). This report includes only information about the <em>number</em> of tests performed, not about the results. The report only includes completed tests and does not cover the microbiology package.</td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#lab-utilization-and-radiology-utilization-report-options">Report Options</a></p>
<p><a href="#lab-tests">Lab Tests</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="even">
<td>List of Registry Patients</td>
<td>The List of Registry Patients report displays a complete list of patients in the local registry. Registry specific information (such as date confirmed and some patient identifiers) can be printed with this report.</td>
<td><p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#registry-status">Registry Status</a></p>
<p><a href="#list-of-registry-patients-report-options">Report Options</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="odd">
<td>Liver Score by Range Report</td>
<td><p>Effective with Patch ROR*1.5*14, the MELD Score by Range report has been renamed and is now the Liver Score by Range report. It provides a list of patients and their liver scores within a user-specified range (low to high score) and either the most recent score or observations during a specified date range. The user can select from APRI, FIB-4, Model for End-Stage Liver Disease (MELD) or MELD with Incorporation of Serum Sodium (MELD-Na) scores. The report allows the user to select any single score or a combination of up to two liver scores. If selecting multiple scores, the user can select the APRI and FIB-4 combination or the MELD and MELD-Na combination. If APRI is selected, the user must enter the upper limit of normal (ULN) for the AST value to be used in the calculation.</p>
<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/416.png)</th>
<th><p><strong>Notes:</strong> Effective with CCR 1.5.10 (Patch ROR*1.5*10):</p>
<ol type="1">
<li><p>For patients where a value cannot be calculated because there are no lab tests, the lab Result field will be blank and the MELD (and/or MELD-Na) column will be blank.</p></li>
<li><p>Results will be ignored if the SPECIMEN TYPE (file 63.04, field #.05) contains UA or UR.</p></li>
<li><p>For patients where the Creatinine result is &gt;12 (invalid), earlier results will be checked for a valid value. If no valid value is found, the Result field will contain the invalid result with “” next to it, and both scores will be blank (not calculated).</p></li>
<li><p>For patients where the Sodium result is &lt;100 or &gt;180 (invalid), earlier results will be checked for a valid value. If no valid value is found, the Result field will contain the invalid result with “” next to it, and the MELD-Na score will be blank (not calculated).</p></li>
<li><p>If you do not select (check) either report (MELD or MELD-Na) in the <strong>Result Ranges</strong> panel, the report will display both scores.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>![](ror-1-5-42-user-manual/417.png)</td>
<td><p><strong>Notes:</strong> Effective with CCR 1.5.15 (Patch ROR*1.5*15):</p>
<p>The “Liver Score by Range” report includes rows for tests that are not related to the test(s) selected by the user. Test rows should no longer appear if they are not used in the report calculations. If the user selects the APRI and/or FIB4 tests, then the Bili, Cr, INR, and Na rows should not appear on the report. If the user selects the MELD and/or MELDNA tests, then the AST, Platelet, and ALT rows should not appear on the report.</p></td>
</tr>
</tbody>
</table></td>
<td><p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#future-appointments">Future_Appointments</a></p>
<p><a href="#liver-score-date-range-by-range-report">Liver Score Date Range</a></p>
<p><a href="#liver-score-result-ranges">Result Ranges</a></p>
<p><a href="#Utilization_Date_Range">Utilization Date Range</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p>Other Diagnoses</p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="even">
<td>Outpatient Utilization</td>
<td>The Outpatient Utilization report provides a count of outpatient clinic utilization during the specified date range with an option to identify patients with the highest utilization. There is no specific detail on which patients went to which clinics or when they went– use the <a href="#_ARV_Combination_Report">Clinic Follow Up</a> report for that purpose.</td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#general-report-options">Options</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="odd">
<td>Patient Medication History</td>
<td><p>The Patient Medication History report provides all inpatient and outpatient prescription fills for selected patients over a specified time period. This report searches inpatient unit dose, IV medications, and outpatient prescriptions for any or specified prescription fills.</p>
<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/418.png)</th>
<th><strong>Note:</strong> Effective with CCR 1.5.13 (Patch ROR*1.5*13), this report is enhanced to allow users to select the most recent fill only, or all fills. The report output has been enhanced to include a column displaying the number of fills remaining.</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#activity">Activity</a></p>
<p><a href="#refill-type">Report Options</a></p>
<p><a href="#medications">Medications</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="even">
<td>Pharmacy Prescription Utilization</td>
<td>The Pharmacy Prescription Utilization report provides a count of prescriptions filled during a specified date range, with the option of identifying patients with the highest utilization. This report does not include information about specific medications filled by individual patients; use the <a href="#activity">Patient Medication History</a> report for that information.</td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#activity">Activity</a></p>
<p><a href="#general-report-options">Options</a></p>
<p><a href="#medications">Medications</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="odd">
<td>Potential DAA Candidates</td>
<td><p>![](ror-1-5-42-user-manual/419.png) The Potential DAA Candidates report identifies patients that may be eligible for the new HepC DAAs. The report is for HepC patients only. The report provides a list of patients that may be eligible for the new medications based on the following criteria:</p>
<ul>
<li><p>Patients must be in the HepC Registry</p></li>
<li><p>Patients must be alive</p></li>
<li><p>If the patient has ever received either Boceprevir or Telaprevir, that patient will be excluded from the report.</p></li>
</ul>
<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/420.png)</th>
<th><p><strong>Notes:</strong> If you receive error messages stating No tests have been identified for the HepC GT site parameter, No tests have been identified for HepC QUAL or HepC QUANT site parameters, or both, the registry coordinator must set the appropriate site parameters. Refer to Section 7 Setting Site Parameters for more information.</p>
<p>Effective with CCR 1.5.24 (Patch ROR*1.5*24), the requirement to have a HepC GT lab test defined has been removed.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td><p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p>Treatment History</p>
<p><a href="#liver-score-date-and-result-ranges">Liver Score Date and Result Ranges</a></p>
<p><a href="#Utilization_Date_Range">Utilization Date Range</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p>Clinics</p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="even">
<td>Procedures</td>
<td><p>The Procedures report provides a list of patients or summary data on patients who had a selected procedure during the specified date range, with the option of additional filters.<a href="#fn3" class="footnote-ref" id="fnref3" role="doc-noteref"><sup>3</sup></a> This report searches on inpatient and outpatient procedures.</p>
<p>The sorting of the Procedures report was changed for CCR 1.5. <a href="#fn4" class="footnote-ref" id="fnref4" role="doc-noteref"><sup>4</sup></a></p>
<ul>
<li><p>When the report is sorted by patient data, the procedures are grouped by patient.</p></li>
<li><p>When the report is sorted by procedure data, the report is <em>not</em> grouped and the patient data is duplicated in each row.</p></li>
</ul>
<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/421.png)</th>
<th><strong>Note:</strong> If a patient is not selected for a report, all corresponding procedures are disregarded and not included in counts.</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#future-appointments">Future_Appointments</a></p>
<p><a href="#procedures">Procedures</a></p>
<p><a href="#Patients">Patients</a></p>
<p><a href="#Report_Type">Report Type</a></p>
<p><a href="#icd">ICD</a></p>
<p><a href="#cpt">CPT</a></p>
<p><a href="#Utilization_Date_Range">Utilization Date Range</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p>Clinics</p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="odd">
<td>Radiology Utilization</td>
<td>The Radiology Utilization report provides a count of radiology procedures utilized within the specified date range, with an option to identify the patients with the highest utilization.</td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#lab-utilization-and-radiology-utilization-report-options">Report Options</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="even">
<td>Registry Lab Tests by Range</td>
<td>The Registry Lab Tests by Range report allows the user to search for registry-specific lab tests and to filter on results of laboratory tests where the results are in a numeric format. In order for this report to work, the Registry Labs list must be set up and current at your facility; see the <a href="#adding-lab-tests">Adding Lab Tests</a> section for details on how to set up local Registry Labs.</td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#future-appointments">Future_Appointments</a></p>
<p><a href="#lab-tests-date-range">Result Ranges</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="odd">
<td>Registry Medications</td>
<td>The Registry Medications report provides counts and/or names of patients who received at least one prescription fill for a registry specific medication during a defined period.</td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#activity">Activity</a></p>
<p><a href="#Report_Type">Report Type</a></p>
<p><a href="#registry-medications-investigational-drugs">Medications</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="even">
<td>Renal Function by Range</td>
<td><p>The Renal Function by Range report provides a list of patients whose renal function scores are within a user-specified range (low to high scores) and either the most recent score or scores or observations within a specified date range. The report includes the most recent Creatinine Clearance by Cockcroft-Gault or Estimated Glomerular Filtration Rate (eGFR) by Modification of Diet in Renal Disease Study (MDRD) Equation for patients in registry, with the ability to limit it to a range of Creatinine Clearance or Estimated GFR and ability to limit it to patients with utilization in a user specified range.</p>
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/422.png)</th>
<th><p><strong>Notes:</strong> Effective with CCR 1.5.10 (Patch ROR*1.5*10):</p>
<p>The following formulas will be used for the calculations of the Renal Function by Range report:</p>
<p><strong>Cockcroft-Gault</strong> = (140-age) x ideal weight in kilograms (* 0.85 if female) / Creatinine *72</p>
<p><em>Ideal weight in kilograms calculated:</em></p>
<p>Males = 51.65 + (1.85*(height in inches - 60))</p>
<p>Females = 48.67 + (1.65 * (height in inches – 60))</p>
<blockquote>
<p><strong>MDRD</strong> = 175 x creatinine ^-1.154 x age^-0.203 x (1.212 if Black – so have to check race field to see if race is 2054-5) x 0.742 if female</p>
<p>Height will be pulled from the GMRV VITAL MEASUREMENT FILE (#120.5) where VITAL TYPE field (.03) equals HEIGHT. The vital measurement will be pulled from the Rate FIELD (1.2).</p>
<p>The patient’s information, sex and race, will be determined using data in the PATIENT file (#2) through the ^VADPT API.</p>
</blockquote>
<p>Results will be ignored if the SPECIMEN TYPE (file 63.04, field #.05) contains UA or UR.</p>
<p>For patients where the Cr result is &gt;12 (invalid), earlier results will be checked for a valid value. If no valid value is found, the Result field will contain the invalid result with “” next to it, and both scores will be blank (not calculated).</p>
<p>For patients where the Height is &lt;36 or &gt;96, or contains ‘CM’ (measurement in centimeters is invalid), the Result field will contain the invalid result with “” next to it, and the CrCL will be blank (not calculated).</p>
<p>If you do not select (check) either report (CrCl or eGFR) in the <strong>Result Ranges</strong> panel, the report will display both scores.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/423.png)</th>
<th><p><strong>Notes:</strong> Effective with CCR 1.5.15 (Patch ROR*1.5*15):</p>
<p>The “Renal Function by Range” report will now include an option to calculate CKD-EPI scores. A checkbox to select “eGFR by CKD-EPI” will be added to the Result Ranges panel. A CKD-EPI column will be added to the report. The current eGFR column heading will be changed to MDRD.</p>
<p>The Creatinine LOINC codes that are used on existing calculations will be utilized, 15045-8, 21232-4, 2160-0. The CKD-EPI formula is eGFR by CKD-EPI = 141 x min(Scr/k, 1)<sup>a</sup> x max(Scr/k, 1)<sup>-1.209</sup> x 0.993<sup>Age</sup> x 1.159 [if black] x 1.018 [if female], where Scr = serum creatinine, k = 0.7 for females and 0.9 for males, a = -0.329 for females and -0.411 for males, min indicates the minimum of Scr/k or 1, and max indicates the maximum of Scr/k or 1.</p>
<p>In addition, the Report Summary table will be modified to read “Number of Patients by MDRD” and “Number of Patients by CKD-EPI.” If the user chooses MDRD, CKD-EPI is hidden, and vice versa. If the user chooses both MDRD and CKD-EPI, information for both is displayed.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td><p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#svr">SVR</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#future-appointments">Future_Appointments</a></p>
<p><a href="#Report_Type">Report Type</a></p>
<p>Renal Function Date Ranges</p>
<p><a href="#renal-function-date-range-and-results">Result Ranges</a></p>
<p><a href="#Utilization_Date_Range">Utilization Date Range</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="odd">
<td>Sustained Virologic Response</td>
<td><p>![](ror-1-5-42-user-manual/424.png) The Sustained Virologic Response report identifies patients who have had a SVR after treatment with HepC antiviral medications.  The report is for HepC patients only. The report provides a list of patients who appear to have a SVR based on the following criteria:</p>
<ul>
<li><p>Patients must be in the HepC Registry</p></li>
<li><p>Patients must have received treatment with at least one HepC registry medication</p></li>
<li><p>Patients must have all undetectable HCV RNA tests after the calculated end of all HepC antiviral medications</p></li>
</ul>
<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/425.png)</th>
<th><strong>Note:</strong> If you receive error messages stating No tests have been identified for HepC QUAL or HepC QUANT site parameters, the registry coordinator must set the appropriate site parameters. Refer to Section 7 Setting Site Parameters for more information.</th>
</tr>
</thead>
<tbody>
</tbody>
</table></td>
<td><p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#Utilization_Date_Range">Utilization Date Range</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p>Clinics</p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
<tr class="even">
<td>VERA Reimbursement</td>
<td>![](ror-1-5-42-user-manual/426.png) The <a href="#Glos_VERA">Veterans Equitable Resource Allocation</a> (VERA) Reimbursement report is available only in the CCR:HIV Registry and can provide counts and/or names of patients who meet criteria for complex care or basic care reimbursement based on care received for HIV. The report can also include patients on investigational medications although these patients currently do not receive complex care reimbursement if they receive only investigational <a href="#Glos_ARV">antiretrovirals</a> (ARVs). Please note that it is possible that a patient who meets criteria for basic level based on HIV related factors could meet criteria for complex level based on other conditions. Also note that the report logic is based on the current VERA algorithms which may change in the future.</td>
<td><p><a href="#Date_Range_Panes">Date Range</a></p>
<p><a href="#scheduled-to-run-on-pane">Scheduled to Run On</a></p>
<p><a href="#include-patients-confirmed-in-the-registry">Include Patients Confirmed in the Registry</a></p>
<p><a href="#birth-sex">Birth Sex</a></p>
<p><a href="#age-range">Age Range</a></p>
<p><a href="#oefoif">OEF/OIF</a></p>
<p><a href="#additional-identifiers">Additional Identifiers</a></p>
<p><a href="#treatment-history">Options</a></p>
<p><a href="#registry-medications-investigational-drugs">Medications</a></p>
<p><a href="#Divisions">Divisions</a></p>
<p><a href="#Clinics">Clinics</a></p>
<p><a href="#Select_Patient">Select Patient</a></p>
<p><a href="#Other_Diagnoses">Other Diagnoses</a></p>
<p><a href="#_Toc471288454">Diagnosis Date Range</a></p>
<p><a href="#Other_Registries">Other Registries</a></p>
<p><a href="#Local_Fields">Local Fields</a></p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>added information about the output format of the report; ROR*1.5*10 changed the input screen.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>added information about the logic for the Diagnoses report with the modified ICD-9 panel.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn3"><p>added a statement to reflect the new search parameter.<a href="#fnref3" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn4"><p>added information about the sorting logic.<a href="#fnref4" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

## Report Title

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The report title is displayed at the top of the report screen.

## Scheduled To Run On Pane

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select a date and time in the Scheduled to Run on section. If no other date and time are specified, the report will begin running immediately.
2.  Select a Repeat interval, if desired: select 1D to repeat this report each day after its first run, or select 1M to repeat it one month from its first run. To run this report on the first of each month at 4:00 AM, select 1M(1@4AM). Leave this field blank if repeated reporting is not required.
3.  Enter a Comment in the field provided, if desired.

| ![](ror-1-5-42-user-manual/427.png) | Note: Some reports require little processing and can quickly retrieve and display the data for the selected report. However, reports that are likely to require more processing time – such as those with large numbers of patients and/or several variables – should be scheduled to run on a date and time when VistA server resources are not being used as heavily. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Return to Local Reports table

## Include Patients Confirmed in the Registry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set the Include patients confirmed in the registry parameters (see the [Generating a Report](#generating-a-report) topic for detailed instructions.).

<span id="Date_Range_Panes" class="anchor"></span>Return to Local Reports table

## Date Range Pane(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most registry reports allow you to set Date Range parameters to determine the window of time from which to capture the data for the report. Depending on the report, one or more Date range selections may be made. For example, in the Combined Meds and Labs report, you may specify date ranges for Medications, Lab Tests, and Utilization.

If date range parameters are incorrectly set, a warning will prompt you to check the Report Period parameters when you click the \[Run\] button. For example, if a Quarter is selected but no Year, you will be warned that the Year or Quarter value is not valid.

See Pop-up Calendars for information on how to use the various pop-up calendar functions.

Refer to Section 9.1.2 Date Range Parameters for information on the date range parameters.

Return to Local Reports table

## Report Elements to Include

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All reports give you some latitude as to what elements are included in the report. All have the options Include all and Selected only, which allow you to specify whether you want to see all the data about the report subject. For example, in the Combined Meds and Labs report, you can specify all medications or select certain medications (or groups of medications) to be included. In that same report, you can specify that you want to see results on all lab tests, or only selected ones.

Note that the Combined Meds and Labs report offers the option to Include All or Selected only. There is also an option to Display all or Only most recent in time period lab tests. Both option sets were added with CCR 1.5.8.

<span id="Utilization_Date_Range" class="anchor"></span>Return to Local Reports table

## Utilization Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set the Utilization Date Range (see the Generating a Report topic for detailed instructions on date ranges).

<span id="Divisions" class="anchor"></span>Return to Local Reports table

## Divisions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Divisions panel to select one or more Divisions to be included in the report. Include All and Selected only appear on the Divisions panel.[^13]

![](ror-1-5-42-user-manual/428.png)

<span id="_Toc167263880" class="anchor"></span>Figure 115 – Divisions

- Enter “??” in the Search box to display all available divisions in the left-hand list box.
- Click Include All to report on all divisions. If you choose Include All, the report considers all registry patients.
- Click Selected only to report on patient(s) seen in one or more specific divisions. If you choose Selected only, the report includes only those patients who had utilization in the selected division(s).
- The \[All Divisions\] button will be disabled when the Include All radio button is selected and enabled when the Selected Only radio button is selected.

<span id="Clinics" class="anchor"></span>Return to Local Reports table

## Clinics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the radio buttons, select one or more clinics in the Clinics section:

- Click Include All to select all clinics to be included the report
- Click Selected only to specify one or more particular clinics to be included in the report. Use the clinic selection panes to locate and select the clinics:

> ![](ror-1-5-42-user-manual/429.png)

<span id="_Toc167263881" class="anchor"></span>Figure 116 – Clinic Follow Up Report Setup Screen (Clinics pane)

- Enter the first few letters of the clinic name, and then click the \[Search\] button. A list of matching clinic locations is displayed below the search field. Clinic names are the same ones used in the appointment scheduling process.
- Select a clinic name, and then click the right arrow to move it to the right pane. Repeat this procedure until all desired clinics are selected and appear in the right pane.

> ![](ror-1-5-42-user-manual/430.png)

<span id="_Toc167263882" class="anchor"></span>Figure 117 – Report Setup Screen (Clinics pane), showing Clinic Names being selected

- To remove a selected clinic, click the name of the clinic in the right pane and click the left arrow button.

<span id="Select_Patient" class="anchor"></span>Return to Local Reports table

## Select Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click Selected only to specify one or more particular patients to be included in the report. If you choose Selected only, the Other Registries and Local Fields panels are disabled and the report includes only selected patients. If a patient did not receive selected medications, the patient is added to the report anyway with No Data as the indicator.

![](ror-1-5-42-user-manual/431.png)

> <span id="_Toc167263883" class="anchor"></span>Figure 118 – Select Patient

- Enter the first few letters of the patient’s name (default), the last four digits of the SSN, dateofbirth, age, or dateofdeath and click the \[Search\] button.
- A list of matching patients displays below the search field.
- To move a patient to the right pane, select a name and click the single right arrow. Repeat this process until all desired patients are selected and appear in the right pane.
- To move a patient back to the left pane, select a name and click the single left arrow. Repeat this process until all desired patients are selected and appear in the left pane.
- To move all the names to the right pane, click the double right arrows.
- To move all the names back to the left pane, click the double left arrows.

<span id="Other_Diagnoses" class="anchor"></span>Return to Local Reports table

## Other Diagnoses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/432.png) Note that the report also offers the option to Ignore, Include or Exclude Codes in Other Diagnoses. This was added with CCR 1.5.8. In this pane:

- Select Ignore to ignore any other diagnoses that may be present.
- Select Include Codes to specify which other diagnosis codes should be considered.
- Select Exclude Codes to specify which diagnosis codes should *not* be considered.

> In the latter two cases, you will be able to specify Your Templates (if you have any defined) or Common Templates to be used.

- From the pull-down list, select one of the template classes. The list of templates appears in the left pane:

![](ror-1-5-42-user-manual/433.png)

<span id="_Toc167263884" class="anchor"></span>Figure 119 – Other Diagnoses pane

- Highlight the desired template name. The red right arrow (![](ror-1-5-42-user-manual/434.png)) command icon becomes available above the double arrows; click the arrow to move the template to the right pane. In this case, the Alcohol template was selected and moved to the right pane:

![](ror-1-5-42-user-manual/435.png)

<span id="_Toc167263885" class="anchor"></span>Figure 120 – Other Diagnoses pane (selecting individual Codes to be included)

- Note the plus sign (![](ror-1-5-42-user-manual/436.png)) to the left of the template name. Click to expand the template and display the diagnosis names associated with that template:

![](ror-1-5-42-user-manual/437.png)

<span id="_Toc167263886" class="anchor"></span>Figure 121 – Other Diagnoses pane (selecting All Codes)

- Or, use the double right arrow ![](ror-1-5-42-user-manual/438.png) to move all the diagnosis templates to the right pane.
- Once the diagnoses are displayed in the right pane, you can select one or more and use the left red arrow ![](ror-1-5-42-user-manual/439.png) to remove that specific diagnosis from the right-hand panel. Or, use the double left arrow ![](ror-1-5-42-user-manual/440.png) to remove all the diagnoses from the right-hand panel.

In CCR 1.5.8, when you used this filter and then removed a previously-selected group of diagnoses from the right pane, the group header would remain in the right pane. Effective with CCR 1.5.10, you may also remove the header from the selected panel. Highlight the group header and press the \[Delete\] key to remove the header. Or, highlight the group header and click the left red arrow to delete the header.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 50%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/441.png)</th>
<th colspan="2"><p><strong>Note:</strong> Patch ROR*1.5*10 added a new ICD-9 diagnosis group to the Common Templates</p>
<p><strong>Note:</strong> Patch ROR*1.5*19 added ICD-10 diagnoses groups to the Common Templates</p>
<p><strong>Note:</strong> Patch ROR*1.5*26 added a new ICD-9 and ICD-10 diagnoses group to the Common Templates</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"></td>
<td><strong>Hepatocellular Carcinoma (HCC):</strong> 155.0</td>
<td><strong>Esophageal varices:</strong> 456.0, 456.1, 456.20, 456.21</td>
</tr>
<tr class="even">
<td><em>HCC is a primary malignancy (cancer) of the liver. Most cases of HCC are secondary to either a viral hepatitide infection (hepatitis B or C) or cirrhosis (alcoholism being the most common cause of hepatic cirrhosis). It is also known as primary liver cancer or hepatoma.</em></td>
<td><em>Esophageal varices are fragile, swollen veins at the base of the muscular tube (esophagus) that serves as the conduit between the mouth and the stomach.</em></td>
</tr>
<tr class="odd">
<td></td>
<td><em>ICD-9 155.0: Malignant neoplasm of liver primary</em></td>
<td><p><em>456.0: Esophageal varices with bleeding</em></p>
<p><em>456.1: Esophageal varices without bleeding</em></p>
<p><em>456.20: Esophageal varices in diseases classified elsewhere with bleeding</em></p>
<p><em>456.21: Esophageal varices in diseases classified elsewhere without bleeding</em></p></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Liver Transplantation (ICD-9):</strong> V42.7, 996.82</td>
<td><strong>Liver Transplantation (ICD-10):</strong> T86.4%, Z48.23%, Z94.4</td>
</tr>
</tbody>
</table>

<span id="_Toc471288454" class="anchor"></span>Return to Local Reports table

## Diagnosis Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the reports that include Other Diagnoses section and a set of ICDs diagnoses groups are selected, set a Diagnosis Date Range.

![](ror-1-5-42-user-manual/442.png)

> <span id="_Toc167263887" class="anchor"></span>Figure 122 – Diagnosis Date Range

<span id="Report_Type" class="anchor"></span>Return to Local Reports table

## Report Type (Complete/Summary)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/443.png)

> <span id="_Toc167263888" class="anchor"></span>Figure 123 – Report Type

Using the radio buttons, select the Report Type: Complete or Summary.

<span id="BMI_Date_Range" class="anchor"></span>Return to Local Reports table

## BMI Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/444.png)

<span id="_Toc167263889" class="anchor"></span>Figure 124 – BMI Date Range

Specify the BMI Date Range by checking either Most recent BMI or BMI as of. In the latter case, enter the “as of” date.

<span id="BMI_Result_Range" class="anchor"></span>Return to Local Reports table

## BMI Result Ranges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/445.png)

<span id="_Toc167263890" class="anchor"></span>Figure 125 – Result Ranges

Set the Result Ranges for the BMI report by checking the box and entering the low and high values as appropriate.

| ![](ror-1-5-42-user-manual/446.png) | Note: Effective with CCR 1.5.10 (Patch ROR\*1.5\*10), if you do not select (check) BMI in the Result Ranges panel, the report will display the BMI score. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<span id="Other_Registries" class="anchor"></span>Return to Local Reports table

## Other Registries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/447.png) In this section, <span id="SelectMode" class="anchor"></span>select a Mode, to *include* in or *exclude* from the report, patients with HIV/HEPC co-infection, who also meet the above criteria. [^14]

> ![](ror-1-5-42-user-manual/448.png)

<span id="_Toc167263891" class="anchor"></span>Figure 126 – Other Registries

You must click in the space immediately below the Mode button to display the drop-down list arrow. Click the arrow to see the choices and make your selection:

> ![](ror-1-5-42-user-manual/449.png)

<span id="_Toc167263892" class="anchor"></span>Figure 127 – Other Registries, Highlighted Choices

Under Registry Description, select a registry to *include* in or *exclude* from the report.

![](ror-1-5-42-user-manual/450.png)

<span id="_Toc167263893" class="anchor"></span>Figure 128 – Include/Exclude Registries

<span id="Local_Fields" class="anchor"></span>Return to Local Reports table

## Local Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/451.png)

<span id="_Toc167263894" class="anchor"></span>Figure 129 – Local Fields

![](ror-1-5-42-user-manual/452.png) In the Local Fields section, select a Mode, to *include* in or *exclude* from the report output, patients associated with the local field. If you select more than one filter, the search will look for people with filter \#1 *and* filter \#2 *and* filter \#3, and so on (see [Adding Local Fields](#adding-local-fields) for more information) .[^15] Note that Local Fields choices will only be seen if your site has created any local fields.

Return to Local Reports table

## Load Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/453.png) Load Parameters. If parameters have previously been saved (refer to Section 9.1.5 Load / Save / Default Parameters Buttons), the parameters can be loaded. Click the \[Load Parameters\] button to use a pre-defined set of ICD-9 codes for a particular condition, such as depression or diabetes. The Open Report Parameters popup displays:

![](ror-1-5-42-user-manual/454.png)

<span id="_Toc167263895" class="anchor"></span>Figure 130 – Open Report Parameters

Look in. From the pull-down list, select Common Templates or Your Templates.Template Name. Select the template name from the pull-down list provided and click \[Open\]. The associated diagnosis codes are loaded into the Registry Reports window. Or, click \[Cancel\] to stop the selection process.

| ![](ror-1-5-42-user-manual/455.png) | Note: If multiple diagnosis codes are selected, the report will include any patient who has at least one of the selected codes. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|

![](ror-1-5-42-user-manual/456.png) Save Parameters. To save this report set-up for future use, click the \[Save Parameters\] button. The Save Report Parameters as window opens; enter a template name and click \[Save\].

<span id="Patients" class="anchor"></span>Return to Local Reports table

## Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patients pane has different options for five different local reports:

- Clinic Follow Up Report
- Combined Meds and Labs Report
- Hepatitis A Report
- Hepatitis B Report
- Procedures Report

Each report is detailed in the sections below.

Return to Local Reports table

### Clinic Follow Up Report Patients Pane

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check one or more Patients checkboxes to include the following types of patients:

![](ror-1-5-42-user-manual/457.png)

<span id="_Toc167263896" class="anchor"></span>Figure 131 – Patients Pane on the Clinic Follow-Up Report

- Seen in selected clinics includes patients seen (with a completed encounter) in the specified clinics. Patients who had appointments but were “no shows” or who cancelled the appointment will not show up as “Seen.”
- Not seen in selected clinics includes patients who were *not* seen in the specified clinics, including patients who died during or after the time period.
- Only patients who have received care during the date range includes patients that have received some care of any type (clinic visit, inpatient stay, pharmacy refill, etc.) during the selected date range.
  - If this checkbox is unchecked, the report will check all living patients in the registry against the selected clinics.
  - Check this box in conjunction with the Notseeninselectedclinics box to find a list of patients who had some type of utilization at your facility but who were not seen in the selected clinics.

Return to Local Reports table

### Combined Med Labs Report Patients Pane

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check one or more Patients checkboxes to include the following types of patients:

![](ror-1-5-42-user-manual/458.png)

<span id="_Toc167263897" class="anchor"></span>Figure 132 – Patients Pane on the Combined Med Labs Report

- Received selected medication(s) includes patients who received the medications specified in the Medications section, during the Medications Date Range.
- Did not receive selected medication(s) includes patients who did not receive any of the medications specified in the Medications section, during the Medications Date Range.
- Selected lab tests were performed includes patients who received the lab test(s) specified in the Lab Tests section, during the selected Lab Date Range.
- No selected lab tests were performed includes patients who did not receive the lab test(s) specified in the Lab Tests section, during the Lab Date Range.

Only patients who have received care during the date range includes patients that have received care of any type (clinic visit, inpatient stay, pharmacy refill, etc.) during the Utilization Date Range. If this checkbox is unchecked, the report will check all living patients in the registry against the selected medications and/or lab tests.

Return to Local Reports table

### Hepatitis A Report Patients Pane

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Hepatitis A Report only, if a vaccination-related box is checked in the Patients section, set a Vaccination Date Range. If an immunity-related box is checked in the Patients section, set a Immunity Date Range.

![](ror-1-5-42-user-manual/459.png)

<span id="_Toc167263898" class="anchor"></span>Figure 133 – Patients Pane on the Hepatitis A Report

- Hepatitis A vaccination includes patients who received a hepatitis A vaccination during the Vaccination Date Range.
- No Hepatitis A includes patients who did not receive a hepatitis A vaccination during the Vaccination Date Range.
- Hepatitis A immunity includes patients that had laboratory documentation of hepatitis A immunity during the Immunity Date Range.
- No Hepatitis A immunity includes patients who did not have laboratory documentation of hepatitis A immunity during the Immunity Date Range.

Return to Local Reports table

### Hepatitis B Report Patients Pane

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Hepatitis B Report only, if a vaccination-related box is checked in the Patients section, set a Vaccination Date Range. If an immunity-related box is checked in the Patients section, set a Immunity Date Range.

![](ror-1-5-42-user-manual/460.png)

<span id="_Toc167263899" class="anchor"></span>Figure 134 – Patients Pane on the Hepatitis B Report

- Hepatitis B vaccination includes patients who received a hepatitis B vaccination during the Vaccination Date Range.
- No Hepatitis B includes patients who did not receive a hepatitis B vaccination during the Vaccination Date Range.
- Hepatitis B immunity includes patients that had laboratory documentation of hepatitis B immunity during the Immunity Date Range.
- No Hepatitis B immunity includes patients who did not have laboratory documentation of hepatitis B immunity during the Immunity Date Range.

Return to Local Reports table

### Procedures Report Patients Pane 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check one or more Patients checkboxes to include in your report patients associated with selected procedures performed or no selected procedures performed in a specified date range. Selecting the Only patients who have received care during the date range checkbox activates the Utilization Date Range Panel.[^16]

![](ror-1-5-42-user-manual/461.png)

<span id="_Toc167263900" class="anchor"></span>Figure 135 – Patients Pane on the Procedures Report

- The Only patients who have received care during the date range checkbox is mainly used in combination with No selected procedures were performed.
- Selected procedures were performed includes patients who received the type of procedure(s) specified in the Procedures section.
- No selected procedures were performed includes patients who did not receive the type of procedure(s) specified in the Procedures section.
- Only patients who have received care during the date range includes patients that have received care of any type (clinic visit, inpatient stay, pharmacy refill, etc.) during the Utilization Date Range. If this checkbox is unchecked, the report will check all living patients in the registry against the procedures.

Return to Local Reports table

## Vaccination Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Hepatitis A or Hepatitis B Report, if a vaccination-related box is checked in the Patients section, set a Vaccination Date Range.

![](ror-1-5-42-user-manual/462.png)

<span id="_Toc167263901" class="anchor"></span>Figure 136 – Vaccination Date Range

Return to Local Reports table

## Immunity Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Hepatitis A or Hepatitis B Report, if an immunity-related box is checked in the Patients section, set an Immunity Date Range.

![](ror-1-5-42-user-manual/463.png)

> <span id="_Toc167263902" class="anchor"></span>Figure 137 – Immunity Date Range

Return to Local Reports table

## Medications Date Range 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Combined Meds Labs Report, if a medications-related box is checked in the Patients section, set a Medications Date Range.

![](ror-1-5-42-user-manual/464.png)

<span id="_Toc167263903" class="anchor"></span>Figure 138 – Medication Date Range

Return to Local Reports table

## Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select one or more Medications:

![](ror-1-5-42-user-manual/465.png)

<span id="_Toc167263904" class="anchor"></span>Figure 139 – Medications

- Click Include All to select all medications for inclusion in the report
- Click Selected only to specify one or more particular medications to be included in the report. Use the medication selection panes to find and select the meds:
  - Select a type of medication name from the drop-down list. Medications are listed by formulation, VA generic name, VA Drug class codes or names, and by other registry-specific groups (registry meds, investigational drugs).
  - Enter the first few letters of the medication in the left-side field and click the \[Search\] button. A list of matching meds is displayed below the search field. When you are using the search box to select specific medications for this report, the text in the search box will automatically convert to uppercase.
  - Select a medication name. The right arrow (![](ror-1-5-42-user-manual/466.png)) command icon then appears. Click the arrow to move the selected medication to the right pane. The medications will be automatically categorized in the list. Repeat this procedure until all desired meds are selected and appear in the right pane.

> You can use Groups to find patients who received a combination of medications:

- Before selecting any medications, type a name for the first group in the field on the right-hand pane, and then click the large plus sign ( ![](ror-1-5-42-user-manual/467.png) ) button. The Group Name is then displayed in the right pane:

> ![](ror-1-5-42-user-manual/468.png)

- \[Search\] for and select the medications to be included in this group, and then click the right-arrow ![](ror-1-5-42-user-manual/469.png) command icon to move them to the right pane. The medications will be automatically categorized under the Group name in the list.
- Type a name for the next group in the right-side field, and then click the plus-sign button to add the new group name to the Medications list in the right pane. Add medications to this group using the steps above.
- Repeat this process to create as many groups as you need. The report will look for patients that have at least one prescription fill from each group.

> CCR uses *“or”* logic within a group, and *“and”* logic between groups. If you have only one group on your report, the report includes any patient who received at least one drug in the group. If you have multiple groups, it includes patients who received at least one medication from ALL groups.

- To remove a selected medication, click the name of the medication in the right pane and click the left arrow command icon.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/470.png)</th>
<th><p><strong>Note:</strong> Selected medications remain on the selected list, so be sure to remove them if you do not want to include them the next time you run this report. ![](ror-1-5-42-user-manual/471.png)</p>
<p><span id="_Toc167263905" class="anchor"></span>Figure 140 – Combined Meds &amp; Labs Report Setup Screen (showing Generic Medication Names )</p>
<p>Review your selections by clicking the <strong>+</strong> or <strong>–</strong> signs to expand or collapse the lists in the right pane.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Investigational Drugs and Registry Medications. CCR 1.5.8 introduced a new method of handling Investigational Drugs and Registry Medications.

| ![](ror-1-5-42-user-manual/472.png) | History: Prior to Patch ROR\*1.5\*8, there was a default group on the right pane called Medications which included checkbox options for Registry Medications and Investigational Drugs. Consequently, the drop-down only had four options (Formulations, Generic Names, VA Class Codes and VA Class Names). |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Now, Investigational Drugs and Registry Medications appear on the drop-down list:

![](ror-1-5-42-user-manual/473.png)

<span id="_Toc167263906" class="anchor"></span>Figure 141 – Combined Meds & Labs Report Setup Screen (showing Registry Medication and Investigational Drugs Names)

When you enter a Group name (MyName in this example) and then click the “add” ( ![](ror-1-5-42-user-manual/474.png) ) button, the sub-groups Individual Formulations, Generic and Drug Classes appear in the right hand pane:

![](ror-1-5-42-user-manual/475.png)

<span id="_Toc167263907" class="anchor"></span>Figure 142 – Combined Meds & Labs Report Setup Screen (showing Group Name)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/476.png)</th>
<th><p><strong>Note:</strong> If you select Investigational Drugs then the bottom left hand panel would display all the drugs with the VA Drug Class Code = IN140 (in the HEPC registry) or IN150 (in the HIV registry).</p>
<p>Since the drop down already has the option to select based on VA Class Code, if you select Investigational Drugs that should trigger the routine to retrieve drugs based on VA Class Code 140 or 150 as appropriate.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Aggregate By. You can format the output report in one of two ways.

![](ror-1-5-42-user-manual/477.png) Click an Aggregate By option radio button to format the final report by either the generic name or by individual formulations. Use the formulation option for investigational drugs or newly-approved medications where a Generic Name does not yet exist in the local pharmacy file.

| ![](ror-1-5-42-user-manual/478.png) | Tip: If a medication is missing on a report, re-run it using individual formulations to see if it shows up. |
|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|

| ![](ror-1-5-42-user-manual/479.png) | Note: Using these radio buttons does not affect the report set-up form. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|

Return to Local Reports table

## Lab Tests Date Range 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a lab-related box is checked in the Patients section, set a Lab Tests Date Range.

![](ror-1-5-42-user-manual/480.png)

<span id="_Toc167263908" class="anchor"></span>Figure 143 – Lab Test Date Range

Return to Local Reports table

## Lab Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select one or more Lab Tests:

![](ror-1-5-42-user-manual/481.png)

> <span id="_Toc167263909" class="anchor"></span>Figure 144 – Lab Tests

- Click Include All to select all lab tests to be included the report
- Click Selected only to specify one or more particular tests to be included in the report. Use the lab test selection panes to locate and select the tests:
  - Enter the first few letters of the lab test name and then click the \[Search\] button. A list of matching lab tests is displayed below the search field.
  - Select a lab test name and then click the right arrow (![](ror-1-5-42-user-manual/482.png)) to move the test to the right pane. Optionally, enter a Low and/or High value to search for a particular result on that test. (Decimals are acceptable, but do not use commas in these fields.)
  - Repeat this procedure until all desired tests are selected and appear in the right pane.
  - To remove a selected test, click the name of the clinic in the right pane, and then click the left arrow command icon.

| ![](ror-1-5-42-user-manual/483.png) | Note: If more than one test is selected, the report will include patients with *any one* of those tests in the selected time period. The Low and High ranges will place an additional filter on the test such that the patient must have at least ONE result within the range to be included in the report. The search is *inclusive* of the values listed in low and high fields, and if only a low or high value is listed, the report will return patients with a result above the low or below the high, respectively. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

CCR 1.5.8 added a new feature:  the ability to Include All or Selected only. There is also an option to Display all or Only most recent in time period lab tests. These radio buttons appear on the Combined Meds and Labs report only, they are not included on the Lab Utilization report. Click the appropriate radio button to make this selection:

![](ror-1-5-42-user-manual/484.png)

Return to Local Reports table

## ICD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select one or more diagnoses in the ICD section:

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/485.png)</th>
<th><p><strong>Note:</strong> The updated ICD selection panel allows you to define groups and add ICD codes to the groups. The OR logic is used for codes inside the groups and the AND logic is used between the groups. <a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p>
<p>The codes of each predefined ICD list are associated with the group of the same name. When a list is loaded, the content of the target ICD list is not cleared, but rather the new group is added to the list.<br />
<em>Example:</em> Load the Hepatitis C and Diabetes Type I or II lists. The target ICD list contains both groups, and other report parameters are not affected.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>added information about the modified loading of the predefined ICD-9 lists.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

![](ror-1-5-42-user-manual/486.png)

> <span id="_Toc167263910" class="anchor"></span>Figure 145 -- ICD

The name of the default group is Diagnoses.

- Click Include All to select all ICD codes for inclusion in the report.
- Click Selected only to specify one or more particular ICD-9 codes to be included in the report. Use the selection panes to locate and select the codes:
  - Select the type of code, ICD-9 or ICD-10
  - Enter all or part of the description or diagnosis code, and then click the \[Search\] button. A list of matching diagnoses is displayed below the search field.
  - Select a diagnosis, and then click the right arrow to move it to the right pane. Repeat this procedure until all desired diagnoses are selected and appear in the right pane.
  - To remove a selected code, click the name of the code in the right pane and click the left arrow button.

Return to Local Reports table

## Type of Utilization 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check one or more Types of Utilization checkboxes to include them in the report.

![](ror-1-5-42-user-manual/487.png)

> <span id="_Toc167263911" class="anchor"></span>Figure 146 – Type of Utilization

- Allergy – patient had an allergy added
- Cytopathology – a test performed
- Inpatient Data – in an inpatient bed section
- Inpatient pharmacy – unit dose medication orders, not necessarily dispensed
- IV Drugs – any IV, including fluids, piggy packs, syringes, TPN (if in the system)
- Laboratory – any laboratory test (except Microbiology)
- Microbiology – any microbiology test
- Outpatient Clinic Stop – any clinic stop
- Outpatient Pharmacy – any original, refill, or partial prescription based on Fill date, not Release date (Fill is when the pharmacy put the medication in the bottle, Release is when it is actually given to the patient)
- Radiology – any procedure performed
- Surgical Pathology – any test performed

> These 11 clinical areas can be used in any combination. If a patient died during the specified date range, they will be included in the report if they had utilization.

Return to Local Reports table

## Registry Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ror-1-5-42-user-manual/488.png)

> <span id="_Toc167263912" class="anchor"></span>Figure 147 – Registry Status

Using the check boxes, select the desired patient’s Registry Status: Confirmed or Only confirmed after \[select date\].

Return to Local Reports table

## Report-Specific Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two reports have Report Options panes:

- General Utilization and Demographic
- List of Registry Patients

The functionality of the panes are similar, however, the list options are different. The panes are described in detail in the sections below.

Return to Local Reports table

### General Utilization and Demographic Report Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check one or more Report Options to include detailed demographic information on your population with utilization.

![](ror-1-5-42-user-manual/489.png)

> <span id="_Toc167263913" class="anchor"></span>Figure 148 – Report Options

- Age – calculated at the midpoint of the specified date range, or at the time of death if applicable. The summary also reports average and median age for the selected population.
- Birth Sex – Male or Female, as listed in the VistA patient file.
- ConfirmationDate – the date confirmed into the registry. With the initial CCR 1.5 registry build, all Hepatitis C registry patients were assigned the same confirmation date, as this information was new at the time for that registry.
- DateofBirth – as listed in the local VistA patient file.
- DateofDeath – as listed in the local VistA patient file.
- Race – categorized as: American Indian or Alaska Native, Asian, Black or African American, Declined to answer, Multiple values, No data, Unknown by patient, and White. Taken from the local VistA patient file.
- Risk (HIV Registry only) – reflects the Patient History questions in the Patient Data Editor.
- SelectionDate – The first date that a selection rule criteria was found for the patient
- Type of Utilization – a list of type(s) of utilization found for a given patient.

Return to Local Reports table

### List of Registry Patients Report Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check one or more Report Options checkboxes to include the field on the report. An additional column heading will be added to the report for each checkbox that is checked.

> ![](ror-1-5-42-user-manual/490.png)

<span id="_Toc167263914" class="anchor"></span>Figure 149 – List of Registry Patients Report Options

- Confirmationdate – the date the patient was confirmed into the registry
- DateofDeath – taken from the local VistA patient file
- ReasonsSelectedfortheRegistry – the selection rule (ICD codes or lab test results) that identified the patient as a pending patient for the registry.
- SelectionDate – the earliest date that a registry specific selection rule was found.

Return to Local Reports table

## General Report Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a report Options setting:

![](ror-1-5-42-user-manual/491.png)

> <span id="_Toc167263915" class="anchor"></span>Figure 150 – Inpatient Utilization Report Options

- Click SummaryOnly to include total counts for numbers of patients and number of admissions.
- Click Includedetails and set a Numberofuserswithhighestutilization value to include a list of the highest-utilizing patients and the number of stays and number of days utilized during the report period. To see this level of detail on all patients, enter a number equal to (or greater than) the number of all patients in the registry

Return to Local Reports table

### Lab Utilization and Radiology Utilization Report Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a variation for the Lab Utilization and Radiology Utilization Reports. Follow the procedures in Section 10.1.25, with the additional instructions for the Minimum number of procedures/results to display field:

![](ror-1-5-42-user-manual/492.png)

> <span id="_Toc167263916" class="anchor"></span>Figure 151 – Lab Utilization Report Options

- Click Include details to request details on the patients with highest utilization and/or for tests with at least a minimum number of results. Set the Numberofuserswithhighestutilization to a number equal to or greater than the total number of patients in the registry if you want to see all lab utilization for all registry patients. Set the Minimumnumberofprocedures/resultstodisplay to 1 to include every lab test or procedure that is selected in the report.

Return to Local Reports table

## Liver Score Date Range by Range Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set the Liver Score Date Range by checking either Most recent Liver score or Liver score as of. In the latter case, enter the as of date.

![](ror-1-5-42-user-manual/493.png)

> <span id="_Toc167263917" class="anchor"></span>Figure 152 – Liver Score Date Range

Return to Local Reports table

## Liver Score Result Ranges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set the Result Ranges for the calculation(s) selected by checking the desired range(s) and entering the low and high values, as appropriate.

![](ror-1-5-42-user-manual/494.png)

<span id="_Toc167263918" class="anchor"></span>Figure 153 – Result Ranges

Return to Local Reports table

## Activity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set the Activity parameters to include Inpatient and/or Outpatient

![](ror-1-5-42-user-manual/495.png)

> <span id="_Toc167263919" class="anchor"></span>Figure 154 – Activity

Return to Local Reports table

## Refill Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Under Report Options, select the desired refill type: Display all fills or Only most recent in time period.

![](ror-1-5-42-user-manual/496.png)

> <span id="_Toc167263920" class="anchor"></span>Figure 155 – Refill Type

Return to Local Reports table

## Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check one or more Procedures checkboxes to include Inpatient, Outpatient, or both types of procedures. [^17]

![](ror-1-5-42-user-manual/497.png)

<span id="_Toc167263921" class="anchor"></span>Figure 156 – Procedures

- If only Inpatient (ICD) procedures are selected, the Procedures report uses “or” logic for ICD codes inside the groups, while using “and” logic between groups.
- If only Outpatient (CPT) procedures are selected, a patient is added to the Procedures report when the patient has at least one CPT code selected on the CPT report parameters panel.
- If both Inpatient (ICD-9/ICD-10) and Outpatient (CPT) procedures are selected, a patient is added to the Procedures report when the patient has either at least one inpatient procedure (ICD-9/ICD-10) or at least one selected outpatient procedure (CPT-4).
- The Procedures panel works in conjunction with the Return to Local Reports table
- Patients panel.
1.  If No selected procedures were performed is selected in the Patients panel, the patient is added to the report only when no outpatient procedures and inpatient procedures are found in at least one of the groups.
2.  If Only patients who have received care during the date range is selected in the Patients panel, the patient utilization for the specified date range is reviewed. If there is no patient utilization for the date range, the patient is excluded from the report.

Return to Local Reports table

## CPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select one or more CPT codes:

![](ror-1-5-42-user-manual/498.png)

<span id="_Toc167263922" class="anchor"></span>Figure 157 – CPT Codes

- Click IncludeAll to include all codes in the report
- Click Selectedonly to specify one or more particular codes to be included in the report. Use the selection panes to locate and select the codes:
  - Enter a partial or full description of the code, and then click the \[Search\] button. A list of matching codes is displayed below the search field.
  - Select a code, and then click the right arrow to move it to the right pane. Repeat this procedure until all desired codes are selected and appear in the right pane.
  - To remove a selected code, click the name of the code in the right pane, and then click the left-arrow button.

| ![](ror-1-5-42-user-manual/499.png) | Note: Resources are available to determine the inpatient ICD codes and outpatient CPT-4 codes for specific procedures. Consult with local support staff for the tools available in your facility. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Return to Local Reports table

## Lab Test Group Result 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Result Ranges panel to select one or more Registry lab tests and set high and low limits for each test’s results:

![](ror-1-5-42-user-manual/500.png)

<span id="_Toc167263923" class="anchor"></span>Figure 158 – Lab Test Group Result Range

- Click a LabTestGroup checkbox to select it, and then enter a Low and/or a High value to limit the search for a particular result on that test. Decimals are acceptable, but do not use commas in these fields.
- Specifying low and/or high ranges places an additional filter on the test: a patient must have *at least one result* within the range from each selected test to be included in the report.
- The report includes results that are equal to the specified low or high and all values in between. If only low or only high values are selected, the report will return patients with a result at or above the low or at or below the high, respectively. For example, if you want a report of patients with a result less than 200, enter 199 as the upper limit.

Return to Local Reports table

## Registry Medications – Investigational Drugs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Medications panel, check the InvestigationalDrugs checkbox to add investigational medications to your report. If checked, the final report will aggregate by dispensed drug, as investigational medications are not assigned a VA generic name. If this box is not checked, the report will aggregate by generic name.

![](ror-1-5-42-user-manual/501.png)

> <span id="_Toc167263924" class="anchor"></span>Figure 159 – Registry Medications – Investigational Drugs

Return to Local Reports table

## Renal Function Date Range and Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select the appropriate Renal Function Date Range or the Most recent renal function.

![](ror-1-5-42-user-manual/502.png) Set the result ranges for the Creatinine clearance by Cockcroft-Gault, eGFR by MDRD, eGFR by CKD-EPI or any combination of the three reports by checking the desired range(s) and (optionally) entering the low and high values as appropriate.

> **NOTE:** The Summary under Report Type is only available when the eGFR by MDRD option is selected under Result Ranges.

![](ror-1-5-42-user-manual/503.png)

![](ror-1-5-42-user-manual/504.png)

<span id="_Toc167263925" class="anchor"></span>Figure 160 – Renal Function Date Range and Results

Return to Local Reports table

## Treatment History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/505.png) | ![](ror-1-5-42-user-manual/506.png) This panel is only available in the CCR:HEPC Registry. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Select HepC antiviral naïve or HepC antiviral treatment experienced, as appropriate. The options are not mutually exclusive; the user can select both options.

![](ror-1-5-42-user-manual/507.png)

<span id="_Toc167263926" class="anchor"></span>Figure 161 – Treatment History Panel

- If the user selects HepC antiviral naïve, the system will include patients that have never had prior prescriptions for any HCV registry medications prior to the present day.
- If the user selects HepC antiviral experienced, the system will include patients that have had a prior prescription for any of the HCV registry medications prior to and including the present day.
- If the user selects HepC antiviral experienced, the Exclude patients on treatment i.e. with HCV antiviral treatment within X days, is enabled to allow the user to define the time period (in a T-minus format) to exclude patients currently on treatment. The valid range for this option is 1 to 9999 days. If a patient filled any registry medicines within X days prior to running the report, the patient will be excluded from the report.

Return to Local Reports table

## DAA Start Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/508.png) | ![](ror-1-5-42-user-manual/509.png) This panel is only available in the CCR:HEPC Registry. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Select the appropriate type of date range from the Type drop-down menu. The options are:

- Year
- Quarter
- Custom
- Cutoff

![](ror-1-5-42-user-manual/510.png)

<span id="_Toc167263927" class="anchor"></span>Figure 162 – DAA Start Date Range Panel

In the corresponding text box, enter the appropriate year, quarter or cutoff date.

- The cutoff options selects all patients receiving medication prior to that date
- The custom date range requires establishing the beginning and end date:

![](ror-1-5-42-user-manual/511.png)

<span id="_Toc167263928" class="anchor"></span>Figure 163 – Custom DAA Date Range

Select the Fiscal check box to designate the time frame as a fiscal year.

Return to Local Reports table

## Lab Tests Date Range Weeks After DAA Start

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/512.png) | ![](ror-1-5-42-user-manual/513.png) This panel is only available in the CCR:HEPC Registry. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

![](ror-1-5-42-user-manual/514.png)

<span id="_Toc167263929" class="anchor"></span>Figure 164 – Lab Tests Date Range Weeks After DAA Start

To list the selected lab test results performed after the DAA start date, enter a valid range of 1-999 weeks in the Include labs done weeks after the DAA start text box.

Select the Include two most recent prior to DAA start date checkbox to include the two most recent test results, if any, for the user-selected lab tests prior to the first DAA fill date.

Return to Local Reports table

## VERA Reimbursement Report Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/515.png) | ![](ror-1-5-42-user-manual/516.png) This report is only available in the CCR:HIV Registry. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Check one or more Options checkboxes to select the type(s) of patients to be included, and/or additional information to appear in the report:

![](ror-1-5-42-user-manual/517.png)

> <span id="_Toc167263930" class="anchor"></span>Figure 165 – Vera Reimbursement Report Options

- Complex Care – patients with a clinical AIDS diagnosis as manually entered by local staff on the Patient Data Editor and/or those who have received at least one prescription (inpatient or outpatient) for any ARV in the specified time period, *excluding* investigational ARV drugs.
- Basic Care – patients with utilization during the period and no clinical AIDS diagnosis and who did not receive an ARV.
- Include list of patients – provides a full list of patients’ names by complex or basic care.
- Include Summary ARV use table – provides a count of patients that received each medication, grouped by VA Generic name, in the specified time period.

Return to Local Reports table

## Birth Sex

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Birth Sex panel, select whether the report output is to be filtered by gender. The default is to include both males and females.

![](ror-1-5-42-user-manual/518.png)

> <span id="_Toc167263931" class="anchor"></span>Figure 166 – Birth Sex

Return to Local Reports table

## Additional Identifiers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Additional Identifiers panel, check one or more checkboxes to include additional information in the report output. The Additional Identifiers can be displayed on all reports except the Current Inpatient List report.

![](ror-1-5-42-user-manual/519.png)

> <span id="_Toc167263932" class="anchor"></span>Figure 167 – Additional Identifiers

- Include patient ICN in the report – display the patient ICN in the report output
- Include PACT Team in the report – display the Patient Aligned Care Team (PACT) in the report output
- Include PCP in the report – display the Primary Care Provider (PCP) in the report output

Return to Local Reports table

## OEF/OIF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the OEF/OIF panel, select whether the report output is to be filtered by Operation Enduring Freedom (OEF) and Operation Iraqi Freedom (OIF) patients. The report output can also be filtered to exclude OEF/OIF patients. The default is to include all periods of service.

![](ror-1-5-42-user-manual/520.png)

> <span id="_Toc167263933" class="anchor"></span>Figure 168 – OEF/OIF

Return to Local Reports table

## SVR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/521.png) | ![](ror-1-5-42-user-manual/522.png) This panel is only available in the CCR:HEPC Registry. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

In the SVR panel, select whether the report output is to be filtered by patients who have had a SVR after treatment with HepC antiviral medications. “All Patients” selects patients with and without a SVR, “SVR Only” selects only patients with a SVR, and “No SVR” selects patients with no SVR. The default is to include all patients.

![](ror-1-5-42-user-manual/523.png)

> <span id="_Toc167263934" class="anchor"></span>Figure 169 – SVR

Return to Local Reports table

## Liver Score Date and Result Ranges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/524.png) | ![](ror-1-5-42-user-manual/525.png) This panel is only available in the CCR:HEPC Registry. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

In the Liver Date and Result Score Ranges panel, select whether the report output is to be filtered by patients and their FIB-4 liver scores within a user-specified range (low to high score) and either the most recent score or observations during a specified date range.

Set the Liver Score Date Range by checking either Most recent Liver score or Liver score as of. In the latter case, enter the as of date.

Set the Result Ranges for FIB-4 calculation by checking the Select box and entering the low and high values, as appropriate.

The default is “Most recent Liver Score” and the FIB-4 Select box unchecked.

![](ror-1-5-42-user-manual/526.png)

> <span id="_Toc167263935" class="anchor"></span>Figure 170 – FIB-4

| ![](ror-1-5-42-user-manual/527.png) | Note: If the Select FIB-4 box is not checked, the report will not be filtered by Liver Score Date and Results Range. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|

Return to Local Reports table

## DAA Prescriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/528.png) | ![](ror-1-5-42-user-manual/529.png) This panel is only available in the CCR:HEPC Registry. |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

In the DAA Prescriptions panel, select whether the report output is to be filtered by HepC antiviral medication prescription type. “In-house only” selects patients with prescriptions written by a VA provider and “Choice only” selects patients with prescriptions written by a Choice provider and filled at a VA pharmacy. The default is to include all prescriptions.

![](ror-1-5-42-user-manual/530.png)

> <span id="_Toc167263936" class="anchor"></span>Figure 171 – DAA Prescriptions

Return to Local Reports table

## Age Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Age Range panel, select whether the report output is to be filtered by current age or date of birth. “Current Age” selects patients whose current age falls between the From and To ages specified. “Date of Birth” selects patients whose date of birth falls between the From and To date specified. The default is to include all ages.

![](ror-1-5-42-user-manual/531.png)

> <span id="_Toc167263937" class="anchor"></span>Figure 172 – Age Range

Return to Local Reports table

## Future Appointments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Future Appointments panel, select whether the report output is to be filtered by upcoming appointments within the specified number of days. The default is to include all patients.

![](ror-1-5-42-user-manual/532.png)

> <span id="_Toc167263938" class="anchor"></span>Figure 173 – Future Appointments

Return to Local Reports table

# Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## About CCR:HEPC 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Hepatitis C Case Registry (CCR:HEPC) contains important demographic and clinical data on all VHA patients identified with Hepatitis C infection. The registry extracts VistA pharmacy, laboratory, and pathology databases in order to provide the key clinical information needed to track disease stage, disease progression, and response to treatment. Data from the Hepatitis C Case Registry is used on the national, regional, and local level to track and optimize clinical care of Hepatitis C infected Veterans served by VHA. National summary information (without personal identifiers) will be available to VA Central Office for overall program management as well as to inform Veterans Service Organizations, Congress, and to other federal public health and health care agencies.

### Treatment Recommendations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCR software is meant to supplement data gathering that can be used by local clinicians in their patient care management model.

For patients with Hepatitis C infection, VA treatment guidelines for care may be seen at See CCR Redacted document.

### Registry Selection Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCR:HEPC identifies patients with Hepatitis C-related ICD codes, positive Hepatitis C antibody test results, or positive qualitative Hepatitis C RNA test results. The software recognizes the earliest instance of data that indicates Hepatitis C infection and adds the patient to the registry.

| ![](ror-1-5-42-user-manual/533.png) | Note: See section titled [Note on Pending Patients](#note-on-pending-patients) for more information. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|

Patients are automatically added nightly to the local registry list when one or more of the following ICD-9 and ICD-10 diagnosis codes are listed on a patient’s problem list, inpatient discharge diagnoses, or outpatient encounter diagnoses:

| Hepatitis C-related Diagnoses                           | ICD-9 CM Diagnostic Codes |
|---------------------------------------------------------|---------------------------|
| Hepatitis C Carrier                                     | V02.62                    |
| Acute Hepatitis C with hepatic coma                     | 070.41                    |
| Chronic Hepatitis C with hepatic coma                   | 070.44                    |
| Acute Hepatitis C without mention of hepatic coma       | 070.51                    |
| Chronic Hepatitis C without mention of hepatic coma     | 070.54                    |
| Unspecified Hepatitis C without mention of hepatic coma | 070.70                    |
| Unspecified Hepatitis C with hepatic coma               | 070.71                    |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th>![](ror-1-5-42-user-manual/534.png)</th>
<th><p><strong>Note:</strong> Effective in ICD-10 Remediation CCR Patch ROR*1.5*19, the VistA CCR package now uses the “ICD-10” code set designations in the Reason for Selection within the VistA CCR Patient Data Editor Selection Rules:</p>
<ul>
<li><p>ICD-10 code in problem list</p></li>
<li><p>ICD-10 code in outpatient file</p></li>
<li><p>ICD-10 code in inpatient file</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| Hepatitis C-related Diagnoses                      | ICD-10 CM Diagnostic Codes |
|----------------------------------------------------|----------------------------|
| Acute hepatitis C without hepatic coma             | B17.10                     |
| Acute hepatitis C with hepatic coma                | B17.11                     |
| Chronic viral hepatitis C                          | B18.2                      |
| Unspecified viral hepatitis C without hepatic coma | B19.20                     |
| Unspecified viral hepatitis C with hepatic coma    | B19.21                     |
| Carrier of viral hepatitis C                       | Z22.52                     |

The ICD-9 and ICD-10 diagnostic codes are maintained as part of the standard software program. Updates will be released as needed in subsequent patches to the software and will be loaded by local IRM staff.

Patients are also automatically added nightly to the local registry when a positive test result is reported for a Hepatitis C antibody test or a qualitative Hepatitis C RNA viral load. Hepatitis C antibody tests and RNA tests are identified using the following Logical Observation Identifiers Names Codes (LOINCs).

| ![](ror-1-5-42-user-manual/535.png) | Note: Some of the codes shown here may not yet be valid at the National level. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|

| Hepatitis C-related Laboratory Tests                                                              | LOINC                                                                                           |
|---------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| Hepatitis C virus RNA                                                                             | 11011-4, 29609-5, 34703-9, 34704-7, 10676-5, 20416-4, 20571-6, 49758-6, 50023-1                 |
| Hepatitis C Antibody Test                                                                         | 13955-0, 16128-1, 16129-9, 16936-7, 22327-1, 33462-3, 34162-8, 39008-8, 40762-2, 5198-7, 5199-5 |
| Hepatitis C RIBA Test                                                                             | 24011-9                                                                                         |
| Hepatitis C virus IgG Ab \[Units/volume\] in Serum by Immunoassay                                 | 57006-9                                                                                         |
| Hepatitis C virus Antibody \[Presence\] in Body fluid                                             | 51657-5                                                                                         |
| Hepatitis C virus Antibody \[Presence\] in Serum from donor                                       | 47441-1                                                                                         |
| Hepatitis C virus Antibody \[Presence\] in Serum from donor by Immunoassay                        | 47365-2                                                                                         |
| Hepatitis C virus RNA \[Presence\] in Body fluid by Probe & target amplification method           | 51655-9                                                                                         |
| Hepatitis C virus RNA \[Presence\] in Unspecified specimen by Probe & signal amplification method | 48576-3                                                                                         |
| Qualitative Hepatitis C RNA Test                                                                  | 11259-9, 5010-4, 5011-2, 5012-0, 6422-0                                                         |

Positive results are identified as results that are equal to “P” or that contain “POS” “DETEC” or “REA” and do not contain “NEG” “NO” “UNDET” or “IND.” Comparisons are not case sensitive.

| ![](ror-1-5-42-user-manual/536.png) | Note: Because this information is a critical factor in the determination of a patient being added to this registry, it is important to validate, with the [Laboratory Information Manager](#Glos_LIM), the LOINC Code mapping and how results are entered for the Hepatitis C lab tests. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### About Historic Hepatitis C Case Registry patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All patients in the previous Hepatitis C Case Registry are automatically “grandfathered” into CCR:HEPC as confirmed registry patients. Previous versions of Hepatitis C Case Registry software did not include the use of a “pending” status nor require verification prior to activation in the registry, though local coordinators were tasked to routinely review lists of newly selected patients and delete any found not to meet registry criteria.

At the time the original Hepatitis C Case Registry software was first installed, a background process was run that applied these selection rules to historic data beginning January 1, 1996. For that one-time post installation process only, patients whose only indication of Hepatitis C was ICD codes (i.e., no antibody test result in the system) were required to have at least two instances of a Hepatitis C related ICD code in order to be added to the registry. After that initial registry compilation, a single outpatient or inpatient Hepatitis C related ICD code was sufficient to add a patient to the registry.

Facilities who are concerned that their CCR:HEPC patient list includes a large number of patients who were inappropriately added can utilize CCR report functions (e.g., Lab test report to look for confirmatory testing) to identify and delete patients who do not truly meet registry criteria.

Effective in ICD-10 Remediation CCR Patch ROR\*1.5\*19, the CCR package is able to extract patients from historical encounters that contain HEPC or HIV ICD diagnosis codes by changing the Date of Interest from the historical encounter visit date to the date the historical encounter was created.

The updated software allows a patient to be added to the pending list of the registry if the following conditions for the historical encounter visit date are met:

- The visit date is *on or after* the ICD-10 Activation date.
- The visit date is created *on or after* the ICD-10 Activation date.
- The visit date contains HEPC or HIV ICD10 diagnosis codes.

## About CCR:HIV

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCR:HIV contains important demographic and clinical data on VHA patients identified with HIV infection. The registry extracts data from VistA admissions, allergy, laboratory, outpatient, pathology, pharmacy, and radiology databases. This is done to provide the key clinical information needed to track disease stage, disease progression, response to treatment, and support administrative reporting.

Data from the CCR:HIV is used on the national, regional, and local level to track and optimize clinical care of HIV-infected Veterans served by VHA. National summary information (without personal identifiers) will be available to VA Central Office for overall program management as well as to inform Veterans Service Organizations, Congress, and other federal public health and health care agencies.

### Treatment Recommendations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCR:HIV is meant to supplement data gathering that can be used by local clinicians in their patient care management model.

For patients with HIV infection, VA recommends clinicians consult the Kaiser Family Foundation-Department of Human Health Services treatment guidelines for HIV care. These guidelines may be seen at <http://www.aidsinfo.nih.gov/guidelines/>.

### Registry Selection Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCR:HIV identifies patients with HIV-related ICD-9 codes or positive HIV antibody test results. The software recognizes the earliest instance of data that indicates HIV infection and adds the patient to the registry.

| ![](ror-1-5-42-user-manual/537.png) | Note: See section titled [Note on Pending Patients](#note-on-pending-patients) for more information. |
|------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|

Patients are automatically added nightly to the local registry list when one or more of the following ICD-9 and ICD-10 diagnosis codes are listed on a patient’s problem list, inpatient discharge diagnoses, or outpatient encounter diagnoses:

| HIV-related Diagnoses                                              | ICD-9 Diagnostic Code |
|--------------------------------------------------------------------|-----------------------|
| Asymptomatic Human Immunodeficiency Virus \[HIV\] Infection Status | V08.                  |
| Human Immunodeficiency Virus (HIV) Disease                         | 042.x                 |
| HIV Causing Other Specific Disorder                                | 043.x                 |
| HIV Causing Other Specific Acute Infection                         | 044.x                 |
| Human Immunodeficiency Virus, Type 2 (HIV 2)                       | 079.53                |
| Nonspecific Serologic Evidence Of HIV                              | 795.71                |
| Positive Serology/Viral HIV                                        | 795.8                 |

| HIV-related Diagnoses                                                                        | ICD-10 Diagnostic Code |
|----------------------------------------------------------------------------------------------|------------------------|
| Human immunodeficiency virus \[HIV\] disease                                                 | B20.                   |
| Human immunodeficiency virus, type 2 \[HIV 2\] as the cause of diseases classified elsewhere | B97.35                 |
| Asymptomatic human immunodeficiency virus \[HIV\] infection status                           | Z21.                   |
| HIV complicating pregnancy, first trimester                                                  | O98.711                |
| HIV complicating pregnancy, second trimester                                                 | O98.712                |
| HIV complicating pregnancy, third trimester                                                  | O98.713                |
| HIV complicating pregnancy, unspecified trimester                                            | O98.719                |
| HIV complicating childbirth                                                                  | O98.72                 |
| HIV complicating the puerperium                                                              | O98.73                 |
| Positive Serology/Viral HIV                                                                  | 795.8                  |

The ICD-9 diagnostic codes are maintained as part of the standard software program. Updates will be released as needed in subsequent patches to the software and will be loaded by local IRM staff.

Patients are also automatically added nightly to the local registry pending patient list when a positive test result is reported for an HIV antibody test or HIV Western Blot test. HIV antibody tests and Western Blot tests are identified using the following Logical Observation Identifiers Names Codes (LOINCs).

| ![](ror-1-5-42-user-manual/538.png) | Note: Some of the codes shown here may not yet be valid at the National level. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|

| HIV-related Laboratory Tests                                                 | LOINC                                                                                                                                                                            |
|------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HIV 1 \[interpretation\] in Serum by Immunoassay                             | 44607-0                                                                                                                                                                          |
| HIV 1 Antibody \[Presence\] in Body fluid by Immunoassay                     | 34591-8                                                                                                                                                                          |
| HIV 1 Antibody \[Presence\] in Body fluid by Immunoblot (IB)                 | 34592-6, 5221-7                                                                                                                                                                  |
| HIV 1 Antibody \[Presence\] in CSF by Immunoblot (IB)                        | 28004-0                                                                                                                                                                          |
| HIV 1 Antibody \[Presence\] in Unspecified specimen                          | 53379-4                                                                                                                                                                          |
| HIV 1 Antibody \[Presence\] in Unspecified specimen by Rapid test            | 49905-3                                                                                                                                                                          |
| HIV 1 Antibody \[Units/volume\] in Serum by Immunofluorescence               | 43599-0                                                                                                                                                                          |
| HIV 1 Antibody Test                                                          | 13499-9, 14092-1, 16974-8, 16975-5, 21007-0, 22356-0, 29327-4, 29893-5, 32571-2, 33866-5, 35437-3, 35438-1, 35438-9, 40732-0, 41143-9, 41144-7, 41145-4, 5220-9, 68961-2, 7917-8 |
| HIV 1 Antibody + Antigen in Serum                                            | 51866-2                                                                                                                                                                          |
| HIV 1 Western Blot Test                                                      | 21009-6                                                                                                                                                                          |
| HIV 1+2 Antibody \[Presence\] in Body Fluid                                  | 57975-5                                                                                                                                                                          |
| HIV 1+2 Antibody \[Presence\] in Serum by Immunoblot (IB)                    | 44873-8                                                                                                                                                                          |
| HIV 1+2 Antibody \[Presence\] in Serum from donor                            | 44533-8                                                                                                                                                                          |
| HIV 1+2 Antibody \[Presence\] in Unspecified specimen                        | 43010-8                                                                                                                                                                          |
| HIV 1+2 Antibody \[Presence\] in Unspecified specimen by Rapid test          | 49580-4                                                                                                                                                                          |
| HIV 1+2 Antibody Test                                                        | 22357-8, 31201-7, 32602-5, 40733-8, 42768-2, 48345-3, 5223-3, 69668-2, 73906-0, 7918-6, 80203-3                                                                                  |
| HIV 1+2 Antibody band pattern \[interpretation\] in Serum by Immunoblot (IB) | 43185-8                                                                                                                                                                          |
| HIV 1+2 IgG Antibody \[Presence\] in Blood dot (filter paper)                | 54086-4                                                                                                                                                                          |
| HIV 1+2 IgG Antibody \[Presence\] in Serum                                   | 43009-0                                                                                                                                                                          |
| HIV 1+2 Antibody + HIV 1 P24 Antigen in Serum                                | 56888-1, 58900-2, 75666-8, 85037-0                                                                                                                                               |
| HIV 2 Antibody Test                                                          | 22358-6, 30361-0, 33806-1, 33807-9, 5224-1, 5225-8, 7919-4, 81641-3                                                                                                              |
| HIV 2 Western Blot Test                                                      | 31073-0                                                                                                                                                                          |

Positive results are identified as results that are equal to “P” or that contain “POS” “DETEC” or “REA” and do not contain “NEG” “NO” “UNDET” or “IND.” Comparisons are *not* case sensitive.

| ![](ror-1-5-42-user-manual/539.png) | Note: Because this information is a critical factor in the determination of a patient being added to this registry, it is important to validate, with the [Laboratory Information Manager](#Glos_LIM), the LOINC Code mapping and how results are entered for the HIV lab tests. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## About Local Registries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCR reporting tools can be used with Local Registries based on either ICD-9 or ICD-10. The ICD-9 and ICD-10 codes, as determined by the Population Health Group, within the Office of Public Health, are specified in Table 84 and Table 85. CPT codes for the Total Knee Replacement Registry and the Total Hip Replacement Registry and LOINC codes for the COVID-19 Registry are specified in Table 86, and Table 87 respectively. Initially, the conditions of interest will be determined based on input from a variety of stakeholders, including the Population Health Group, Patient Care Services, Quality and Safety, and the Office of Information Analytics. Patch 18 included 16 initial conditions of interest. Subsequent patches have added registries to address additional conditions of interest. The Local Registries are in distinction to the existing, national CCR Hepatitis C and HIV registries.

| ![](ror-1-5-42-user-manual/540.png) | Note: The Transgender Registry was inactivated in Patch 42. The daily update process will no longer update this registry. Also, this registry will no longer appear in the list of registries displayed to the users so they will not be able to select it. |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Registry Name                                  | Added in Patch |
|------------------------------------------------|----------------|
| Adrenal Adenoma Registry                       | 31             |
| ALS Registry                                   | 24             |
| Alzheimer's Disease Registry                   | 18             |
| Amputation Registry                            | 18             |
| Breast Cancer Registry                         | 18             |
| Cerebrovascular Disease Registry               | 18             |
| Chronic Obstructive Pulmonary Disease Registry | 18             |
| Chronic Renal Disease Registry                 | 18             |
| Colorectal Cancer Registry                     | 24             |
| Congestive Heart Failure (CHF) Registry        | 18             |
| COVID-19                                       | 36             |
| Crohn’s Disease Registry                       | 28             |
| Dementia Registry                              | 28             |
| Diabetes Registry                              | 18             |
| Dyslipidemia Registry                          | 18             |
| Frailty Registry                               | 32             |
| Head and Neck Squamous Cell Cancer Registry    | 35             |
| Hepatitis B Registry                           | 26             |
| Hepatocellular Carcinoma Registry              | 24             |
| Hypertension Registry                          | 18             |
| Hypoparathyroidism Registry                    | 30             |
| Hypothyroidism Registry                        | 35             |
| Idiopathic Pulmonary Fibrosis (IPF) Registry   | 30             |
| Interstitial Lung Disease (ILD) Registry       | 34             |
| Ischemic Heart Disease (IHD) Registry          | 18             |
| Low Vision / Blind Registry                    | 18             |
| Lung Cancer Registry                           | 24             |
| Lymphoma Registry                              | 34             |
| Melanoma Registry                              | 24             |
| Mental Health Registry                         | 18             |
| Movement Disorders Registry                    | 31             |
| Multiple Sclerosis Registry                    | 18             |
| Non-Alcoholic SteatoHepatitis (NASH)           | 34             |
| Obstructive Sleep Apnea Registry               | 21             |
| Osteoarthritis Registry                        | 18             |
| Osteoporosis Registry                          | 24             |
| Pancreatic Cancer Registry                     | 24             |
| Prostate Cancer Registry                       | 24             |
| Recent Patients Registry                       | 37             |
| Rheumatoid Arthritis Registry                  | 18             |
| Thyroid Cancer Registry                        | 28             |
| Total HIP Replacement Registry                 | 26             |
| Total KNEE Replacement Registry                | 26             |
| Transgender Registry                           | 32             |
| Transplant Heart Registry                      | 33             |
| Transplant Intestine Registry                  | 33             |
| Transplant Kidney Registry                     | 33             |
| Transplant Liver Registry                      | 33             |
| Transplant Lung Registry                       | 33             |
| Transplant Pancreas Registry                   | 33             |
| Ulcerative Colitis Registry                    | 28             |

### Local Registry Selection Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCR will search back to 01/01/1985 to identify patients with the qualifying ICD-9 or ICD-10 codes. Patients with a qualifying ICD-9 or ICD-10 code or laboratory result will be automatically confirmed into the local registry for the condition of interest. The confirmation date will be set to be the earliest date of the qualifying ICD-9 or ICD-10 code or the qualifying laboratory result.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>Registry</th>
<th>ICD-9 Codes</th>
</tr>
<tr class="odd">
<th><p>Adrenal Adenoma Registry</p>
<p>(VA ADRENAL ADENOMA)</p></th>
<th>225.3, 227.0, 255.8, 255.9</th>
</tr>
<tr class="header">
<th><p>ALS Registry</p>
<p>(VA ALS)</p></th>
<th>335.20</th>
</tr>
<tr class="odd">
<th><p>Alzheimer's Disease Registry</p>
<p>(VA ALZHEIMERS)</p></th>
<th>331.0</th>
</tr>
<tr class="header">
<th><p>Amputation Registry</p>
<p>(VA AMPUTATION)</p></th>
<th>997.60, 997.61, 997.62, 997.69, V49.60, V49.61, V49.62, V49.63, V49.64, V49.65, V49.66, V49.67, V49.70, V49.71, V49.72, V49.73, V49.74, V49.75, V49.76, V49.77, 885.0, 885.1, 886.0, 886.1, 887.0, 887.1, 887.2, 887.3, 887.4, 887.5, 887.6, 887.7, 895.0, 895.1, 896.0, 896.1, 896.2, 896.3, 897.0, 897.1, 897.2, 897.3, 897.4, 897.5, 897.6, 897.7, 905.9</th>
</tr>
<tr class="odd">
<th><p>Breast Cancer Registry</p>
<p>(VA BREAST CA)</p></th>
<th>174.0, 174.1, 174.2, 174.3, 174.4, 174.5, 174.6, 174.8, 174.9, 175.0, 175.9, 233.0</th>
</tr>
<tr class="header">
<th><p>Cerebrovascular Disease Registry</p>
<p>(VA CVD)</p></th>
<th>430., 431., 433.01, 433.11, 433.21, 433.31, 433.81, 433.91, 434.00, 434.01, 434.10, 434.11, 434.90, 434.91, 435.0, 435.1, 435.3, 435.8, 435.9, 436., 997.02</th>
</tr>
<tr class="odd">
<th><p>Chronic Obstructive Pulmonary Disease Registry</p>
<p>(VA COPD)</p></th>
<th>491.0, 491.1, 491.2, 491.20, 491.21, 491.22, 491.8, 491.9, 492.0, 492.8, 493.20, 493.21, 493.22, 496.</th>
</tr>
<tr class="header">
<th><p>Chronic Renal Disease Registry</p>
<p>(VA CRD)</p></th>
<th>016.00, 016.01, 016.02, 016.03, 016.04, 016.05, 016.06, 095.4, 189.0, 189.9, 223.0, 236.91, 249.40, 249.41, 250.40, 250.41, 250.42, 250.43, 271.4, 274.10, 283.11, 403.01, 403.11, 403.91, 404.02, 404.03, 404.12, 404.13, 404.92, 404.93, 440.1, 442.1, 572.4, 580.0, 580.4, 580.81, 580.89, 580.9, 581.0, 581.1, 581.2, 581.3, 581.81, 581.89, 581.9, 582.0, 582.1, 582.2, 582.4, 582.81, 582.89, 582.9, 583.0, 583.1, 583.2, 583.4, 583.6, 583.7, 583.81, 583.89, 583.9, 584.5, 584.6, 584.7, 584.8, 584.9, 585., 585.1, 585.2, 585.3, 585.4, 585.5, 585.6, 585.9, 586., 587., 588.0, 588.81, 588.89, 588.9, 591., 753.12, 753.13, 753.14, 753.15, 753.16, 753.17, 753.19, 753.20, 753.21, 753.22, 753.23, 753.29, 794.4, 588.1</th>
</tr>
<tr class="odd">
<th><p>Colorectal Cancer Registry</p>
<p>(VA COLORECTAL CANCER)</p></th>
<th>153.0, 153.1, 153.2, 153.3, 153.4, 153.5, 153.6, 153.7, 153.8, 153.9, 154.0, 154.1, 230.3, 230.4, V10.05, V10.06</th>
</tr>
<tr class="header">
<th><p>Congestive Heart Failure (CHF) Registry</p>
<p>(VA CHF)</p></th>
<th>398.91, 402.01, 402.11, 402.91, 404.01, 404.11, 404.91, 404.03, 404.13, 404.93, 428.0, 428.1, 428.20, 428.21, 428.22, 428.23, 428.30, 428.31, 428.32, 428.33, 428.40, 428.41, 428.42, 428.43, 428.9</th>
</tr>
<tr class="odd">
<th><p>COVID-19 Registry</p>
<p>(VA COVID19)</p></th>
<th>-</th>
</tr>
<tr class="header">
<th>Crohn’s Disease Registry (VA CROHNS)</th>
<th>555.0, 555.1, 555.2, 555.9</th>
</tr>
<tr class="odd">
<th>Dementia Registry (VA DEMENTIA)</th>
<th>046.11, 046.19, 046.3, 046.79, 290.0, 290.10, 290.11, 290.12, 290.13, 290.2, 290.21, 290.3, 290.4, 290.41, 290.42, 290.43, 291.2, 292.82, 294.10, 294.11, 294.20, 294.21, 294.8, 331.0, 331.11, 331.19, 331.82</th>
</tr>
<tr class="header">
<th><p>Diabetes Registry</p>
<p>(VA DIABETES)</p></th>
<th>249.00, 249.01, 249.10, 249.11, 249.20, 249.21, 249.30, 249.31, 249.40, 249.41, 249.50, 249.51, 249.60, 249.61, 249.70, 249.71, 249.80, 249.81, 249.90, 249.91, 250.00, 250.01, 250.02, 250.03, 250.10, 250.11, 250.12, 250.13, 250.20, 250.21, 250.22, 250.23, 250.30, 250.31, 250.32, 250.33, 250.40, 250.41, 250.42, 250.43, 250.50, 250.51, 250.52, 250.53, 250.60, 250.61, 250.62, 250.63, 250.70, 250.71, 250.72, 250.73, 250.80,250.81,250.82,250.83, 250.90, 250.91, 250.92, 250.93, 357.2, 362.01, 362.02, 362.03, 362.04, 362.05, 362.06, 366.41</th>
</tr>
<tr class="odd">
<th><p>Dyslipidemia Registry</p>
<p>(VA DYSLIPIDEMIA)</p></th>
<th>272.0, 272.2, 272.4</th>
</tr>
<tr class="header">
<th><p>Frailty Registry</p>
<p>(VA FRAILTY)</p></th>
<th>799.3</th>
</tr>
<tr class="odd">
<th><p>Head and Neck Squamous Cell Cancer Registry</p>
<p>(VA HEAD AND NECK)</p></th>
<th>-</th>
</tr>
<tr class="header">
<th><p>Hepatitis B Registry</p>
<p>(VA HEPB)</p></th>
<th>70.2, 70.20, 70.21, 70.22, 70.23, 70.3, 70.30, 70.31, 70.32, 70.33, V02.61</th>
</tr>
<tr class="odd">
<th><p>Hepatocellular Carcinoma Registry</p>
<p>(VA HCC)</p></th>
<th>155.0</th>
</tr>
<tr class="header">
<th><p>Hypertension Registry</p>
<p>(VA HTN)</p></th>
<th>362.11, 401.0, 401.1, 401.9, 402.00, 402.01, 402.10, 402.11, 402.90, 402.91, 403.00, 403.01, 403.10, 403.11, 403.90, 403.91, 404.00, 404.01, 404.02, 404.03, 404.10, 404.11, 404.12, 404.13, 404.90, 404.91, 404.92, 404.93, 405.01, 405.09, 405.11, 405.19, 405.91, 405.99, 437.2</th>
</tr>
<tr class="odd">
<th><p>Hypoparathyroidism Registry</p>
<p>(VA HYPOPARA)</p></th>
<th>252.1</th>
</tr>
<tr class="header">
<th><p>Hypothyroidism Registry</p>
<p>(VA HYPOTHYROIDISM)</p></th>
<th>243., 244.0, 244.1, 244.2, 244.3, 244.8, 244.9, 246.1, 293.0, 293.1, 701.8</th>
</tr>
<tr class="odd">
<th><p>Idiopathic Pulmonary Fibrosis (IPF) Registry</p>
<p>(VA IPF)</p></th>
<th>516.31</th>
</tr>
<tr class="header">
<th><p>Interstitial Lung Disease (ILD) Registry</p>
<p>(VA ILD)</p></th>
<th>501., 508.1, 495.9, 518.89, 515., 516.0, 516.1, 516.2, 516.30, 516.31, 516.32, 516.33, 516.34, 516.35, 516.36, 516.37, 516.4, 516.5, 516.61, 516.62, 516.63, 516.64, 516.69, 516.9, 517.8, 714.81</th>
</tr>
<tr class="odd">
<th><p>Ischemic Heart Disease (IHD) Registry</p>
<p>(VA IHD)</p></th>
<th>410.00, 410.01, 410.02, 410.10, 410.11, 410.12, 410.20, 410.21, 410.22, 410.30, 410.31, 410.32, 410.40, 410.41, 410.42, 410.50, 410.51, 410.52, 410.60, 410.61, 410.62, 410.70, 410.71, 410.72, 410.80, 410.81, 410.82, 410.90, 410.91, 410.92, 411.0, 411.1, 411.81, 411.89, 412., 413.0, 413.1, 413.9, 414.00, 414.01, 414.02, 414.03, 414.04, 414.05, 414.06, 414.07, 414.12, 414.2, 414.3, 414.8, 414.9</th>
</tr>
<tr class="header">
<th><p>Low Vision / Blind Registry</p>
<p>(VA BLIND)</p></th>
<th>369.00, 369.01, 369.02, 369.03, 369.04, 369.05, 369.06, 369.07, 369.08, 369.10, 369.11, 369.12, 369.13, 369.14, 369.15, 369.16, 369.17, 369.18, 369.20, 369.21, 369.22, 369.23, 369.24, 369.25, 369.3, 369.4, 369.60, 369.61, 369.62, 369.63, 369.64, 369.65, 369.66, 369.67, 369.68, 369.69, 369.70, 369.71, 369.72, 369.73, 369.74, 369.75, 369.76, 369.8, 369.9</th>
</tr>
<tr class="odd">
<th><p>Lung Cancer Registry</p>
<p>(VA LUNG CANCER)</p></th>
<th>162.2, 162.3, 162.4, 162.5, 162.8, 162.9, 231.2, V10.11</th>
</tr>
<tr class="header">
<th><p>Lymphoma Registry</p>
<p>(VA LYMPHOMA)</p></th>
<th>202.80, 201.90</th>
</tr>
<tr class="odd">
<th><p>Melanoma Registry</p>
<p>(VA MELANOMA)</p></th>
<th>172.0, 172.1, 172.2, 172.3, 172.4, 172.5, 172.6, 172.7, 172.8, 172.9</th>
</tr>
<tr class="header">
<th><p>Mental Health Registry</p>
<p>(VA MENTAL HEALTH)</p></th>
<th>296.20, 296.21, 296.22, 296.23, 296.24, 296.25, 296.26, 296.30, 296.31, 296.32, 296.33, 296.34, 296.35, 296.36, 309.81, 295.00, 295.01, 295.02, 295.03, 295.04, 295.05, 295.10, 295.11, 295.12, 295.13, 295.14, 295.15, 295.20, 295.21, 295.22, 295.23, 295.24, 295.25, 295.30, 295.31, 295.32, 295.33, 295.34, 295.35, 295.40, 295.41, 295.42, 295.43, 295.44, 295.45, 295.50, 295.51, 295.52, 295.53, 295.55, 295.60, 295.61, 295.62, 295.63, 295.64, 295.65, 295.70, 295.71, 295.72, 295.73, 295.74, 295.75, 295.80, 295.81, 295.82, 295.83, 295.84, 295.85, 295.90, 295.91, 295.92, 295.93, 295.94, 295.95, 296.00, 296.01, 296.02, 296.03, 296.04, 296.05, 296.06, 296.10, 296.11, 296.12, 296.13, 296.14, 296.15, 296.16, 296.40, 296.41, 296.42, 296.43, 296.44, 296.45, 296.46, 296.50, 296.51, 296.52, 296.53, 296.54, 296.55, 296.56, 296.60, 296.61, 296.62, 296.63, 296.64, 296.65, 296.66, 296.7, 296.80, 296.81, 296.82, 296.89, 293.83, 296.90, 296.99, 298.0, 300.4, 301.12, 309.0, 309.1, 311. </th>
</tr>
<tr class="odd">
<th><p>Movement Disorders Registry</p>
<p>(VA MOVEMENT DISORDERS)</p></th>
<th>331.82, 332.0, 332.1, 333.0, 333.1, 333.4, 333.5, 333.6, 333.72, 333.7, 333.79, 333.85, 333.94, 334.3, 781.0, 781.2, 781.3, 527.7, 333.81, 333.82, 333.83, 333.2, 333.90, 333.91, 333.3, 307.20, 307.22, 307.23</th>
</tr>
<tr class="header">
<th><p>Multiple Sclerosis Registry</p>
<p>(VA MULTIPLE SCLEROSIS)</p></th>
<th>340. </th>
</tr>
<tr class="odd">
<th><p>Non-Alcoholic SteatoHepatitis (NASH) Registry</p>
<p>(VA NASH)</p></th>
<th>571.8, 571.40, 571.41, 571.49</th>
</tr>
<tr class="header">
<th><p>Obstructive Sleep Apnea Registry</p>
<p>(VA APNEA)</p></th>
<th>327.21, 327.23, 780.51, 780.53, 780.57, 786.03, 786.04</th>
</tr>
<tr class="odd">
<th><p>Osteoarthritis Registry</p>
<p>(VA OSTEOARTHRITIS)</p></th>
<th>715.00, 715.04, 715.09, 715.10, 715.11, 715.12, 715.13, 715.14, 715.15, 715.16, 715.17, 715.18, 715.20, 715.21, 715.22, 715.23, 715.24, 715.25, 715.26, 715.27, 715.28, 715.30, 715.31, 715.32, 715.33, 715.34, 715.35, 715.36, 715.37, 715.38, 715.80, 715.89, 715.90, 715.91, 715.92, 715.93, 715.94, 715.95, 715.96, 715.97, 715.98, 720.0, 721.0, 721.1, 721.2, 721.3, 721.90, 721.91</th>
</tr>
<tr class="header">
<th><p>Osteoporosis Registry</p>
<p>(VA OSTEOPOROSIS)</p></th>
<th>733.00, 733.01, 733.02, 733.03, 733.09</th>
</tr>
<tr class="odd">
<th><p>Pancreatic Cancer Registry</p>
<p>(VA PANCREATIC CANCER)</p></th>
<th>157.0, 157.1, 157.2, 157.3, 157.4, 157.8, 157.9</th>
</tr>
<tr class="header">
<th><p>Prostate Cancer Registry</p>
<p>(VA PROSTATE CANCER)</p></th>
<th>185., 233.4, V10.46</th>
</tr>
<tr class="odd">
<th>Recent Patients (VA RECENT PATIENTS)</th>
<th>Selection is based on any Admission or Visit date within the last two years. The nightly ROR TASK has been modified to add or remove patients based upon a two year window.</th>
</tr>
<tr class="header">
<th><p>Rheumatoid Arthritis Registry</p>
<p>(VA RHEUM)</p></th>
<th>714.0, 714.1, 714.2, 714.30, 714.31, 714.32, 714.33</th>
</tr>
<tr class="odd">
<th><p>Thyroid Cancer Registry</p>
<p>(VA THYROID CA)</p></th>
<th>193., V10.87</th>
</tr>
<tr class="header">
<th><p>Total HIP Replacement Registry</p>
<p>(VA TOTAL HIP)</p></th>
<th>0.70, 00.71, 00.72, 00.73, 00.74, 00.75, 00.76, 00.77, 81.51, 81.52, 81.53</th>
</tr>
<tr class="odd">
<th><p>Total KNEE Replacement Registry</p>
<p>(VA TOTAL KNEE)</p></th>
<th>00.80, 00.81, 00.82, 00.83, 00.84, 81.54, 81.55</th>
</tr>
<tr class="header">
<th><p>Transgender Registry</p>
<p>(VA TRANSGENDER)</p></th>
<th>302.3, 302.50, 302.6, 302.85 (see Note in Section 11.3.1)</th>
</tr>
<tr class="odd">
<th><p>Transplant Heart Registry</p>
<p>(VA TRANSPLANT HEART)</p></th>
<th>996.83, V42.1, V43.21, V43.22</th>
</tr>
<tr class="header">
<th><p>Transplant Intestine Registry</p>
<p>(VA TRANSPLANT INTESTINE)</p></th>
<th>996.87, V42.84</th>
</tr>
<tr class="odd">
<th><p>Transplant Kidney Registry</p>
<p>(VA TRANSPLANT KIDNEY)</p></th>
<th>V42.0</th>
</tr>
<tr class="header">
<th><p>Transplant Liver Registry</p>
<p>(VA TRANSPLANT LIVER)</p></th>
<th>996.82, V42.7</th>
</tr>
<tr class="odd">
<th><p>Transplant Lung Registry</p>
<p>(VA TRANSPLANT LUNG)</p></th>
<th>996.84, V42.6</th>
</tr>
<tr class="header">
<th><p>Transplant Pancreas Registry</p>
<p>(VA TRANSPLANT PANCREAS)</p></th>
<th>996.86, V42.83</th>
</tr>
<tr class="odd">
<th><p>Ulcerative Colitis Registry</p>
<p>(VA UC)</p></th>
<th>556.0, 556.1, 556.2, 556.3, 556.4, 556.5, 556.6, 556.8, 556.9</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Registry (Abbreviation)</th>
<th>ICD-10 Codes</th>
</tr>
<tr class="odd">
<th><p>Adrenal Adenoma Registry</p>
<p>(VA ADRENAL ADENOMA)</p></th>
<th>D35.00, D35.01, D35.02, E27.0, E27.8, E27.9</th>
</tr>
<tr class="header">
<th><p>ALS</p>
<p>(VA ALS)</p></th>
<th>G12.21</th>
</tr>
<tr class="odd">
<th><p>Alzheimer's Disease Registry</p>
<p>(VA ALZHEIMERS)</p></th>
<th>G30.0, G30.1, G30.8, G30.9</th>
</tr>
<tr class="header">
<th><p>Amputation Registry</p>
<p>(VA AMPUTATION)</p></th>
<th><p>S48.011A, S48.011D, S48.011S, S48.012A, S48.012D, S48.012S, S48.019A, S48.019D, S48.019S, S48.021A, S48.021D, S48.021S, S48.022A, S48.022D, S48.022S, S48.029A, S48.029D, S48.029S, S48.111A, S48.111D, S48.111S, S48.112A, S48.112D, S48.112S, S48.119A, S48.119D, S48.119S, S48.121A, S48.121D, S48.121S, S48.122A, S48.122D, S48.122S, S48.129A, S48.129D, S48.129S, S48.911A, S48.911D, S48.911S, S48.912A, S48.912D, S48.912S, S48.919A, S48.919D, S48.919S, S48.921A, S48.921D, S48.921S, S48.922A, S48.922D, S48.922S, S48.929A, S48.929D, S48.929S, S58.011A, S58.011D, S58.011S, S58.012A, S58.012D, S58.012S, S58.019A, S58.019D, S58.019S, S58.021A, S58.021D, S58.021S, S58.022A, S58.022D, S58.022S, S58.029A, S58.029D, S58.029S, S58.111A, S58.111D, S58.111S, S58.112A, S58.112D, S58.112S, S58.119A, S58.119D, S58.119S, S58.121A, S58.121D, S58.121S, S58.122A, S58.122D, S58.122S, S58.129A, S58.129D, S58.129S, S58.911A, S58.911D, S58.911S, S58.912A, S58.912D, S58.912S, S58.919A, S58.919D, S58.919S, S58.921A, S58.921D, S58.921S, S58.922A, S58.922D, S58.922S, S58.929A, S58.929D, S58.929S, S68.011A, S68.011D, S68.011S, S68.012A, S68.012D, S68.012S, S68.019A, S68.019D, S68.019S, S68.021A, S68.021D, S68.021S, S68.022A, S68.022D, S68.022S, S68.029A, S68.029D, S68.029S, S68.110A, S68.110D, S68.110S, S68.111A, S68.111D, S68.111S, S68.112A, S68.112D, S68.112S, S68.113A, S68.113D, S68.113S, S68.114A, S68.114D, S68.114S, S68.115A, S68.115D, S68.115S, S68.116A, S68.116D, S68.116S, S68.117A, S68.117D, S68.117S, S68.118A, S68.118D, S68.118S, S68.119A, S68.119D, S68.119S, S68.120A, S68.120D, S68.120S, S68.121A, S68.121D, S68.121S, S68.122A, S68.122D, S68.122S, S68.123A, S68.123D, S68.123S,</p>
<p>S68.124A, S68.124D, S68.124S, S68.125A, S68.125D, S68.125S, S68.126A, S68.126D, S68.126S, S68.127A, S68.127D, S68.127S, S68.128A, S68.128D, S68.128S, S68.129A, S68.129D, S68.129S, S68.411A, S68.411D, S68.411S, S68.412A, S68.412D, S68.412S, S68.419A, S68.419D, S68.419S, S68.421A, S68.421D, S68.421S, S68.422A, S68.422D, S68.422S, S68.429A, S68.429D, S68.429S, S68.511A, S68.511D, S68.511S, S68.512A, S68.512D, S68.512S, S68.519A, S68.519D, S68.519S, S68.521A, S68.521D, S68.521S, S68.522A, S68.522D, S68.522S, S68.529A, S68.529D, S68.529S, S68.610A, S68.610D, S68.610S, S68.611A, S68.611D, S68.611S, S68.612A, S68.612D, S68.612S, S68.613A, S68.613D, S68.613S, S68.614A, S68.614D, S68.614S, S68.615A, S68.615D, S68.615S, S68.616A, S68.616D, S68.616S, S68.617A, S68.617D, S68.617S, S68.618A, S68.618D, S68.618S, S68.619A, S68.619D, S68.619S, S68.620A, S68.620D, S68.620S, S68.621A, S68.621D, S68.621S, S68.622A, S68.622D, S68.622S, S68.623A, S68.623D, S68.623S, S68.624A, S68.624D, S68.624S, S68.625A, S68.625D, S68.625S, S68.626A, S68.626D, S68.626S, S68.627A, S68.627D, S68.627S, S68.628A, S68.628D, S68.628S, S68.629A, S68.629D, S68.629S, S68.711A, S68.711D, S68.711S, S68.712A, S68.712D, S68.712S, S68.719A, S68.719D, S68.719S, S68.721A, S68.721D, S68.721S, S68.722A, S68.722D, S68.722S, S68.729A, S68.729D, S68.729S, S78.011A, S78.011D, S78.011S, S78.012A, S78.012D, S78.012S, S78.019A, S78.019D, S78.019S, S78.021A, S78.021D, S78.021S, S78.022A, S78.022D, S78.022S, S78.029A, S78.029D, S78.029S, S78.111A, S78.111D, S78.111S, S78.112A, S78.112D, S78.112S, S78.119A, S78.119D, S78.119S, S78.121A, S78.121D, S78.121S, S78.122A, S78.122D, S78.122S, S78.129A, S78.129D, S78.129S,</p>
<p>S78.911A, S78.911D, S78.911S, S78.912A, S78.912D, S78.912S, S78.919A, S78.919D, S78.919S, S78.921A, S78.921D, S78.921S, S78.922A, S78.922D, S78.922S, S78.929A, S78.929D, S78.929S, S88.011A, S88.011D, S88.011S, S88.012A, S88.012D, S88.012S, S88.019A, S88.019D, S88.019S, S88.021A, S88.021D, S88.021S, S88.022A, S88.022D, S88.022S, S88.029A, S88.029D, S88.029S, S88.111A, S88.111D, S88.111S, S88.112A, S88.112D, S88.112S, S88.119A, S88.119D, S88.119S, S88.121A, S88.121D, S88.121S, S88.122A, S88.122D, S88.122S, S88.129A, S88.129D, S88.129S, S88.911A, S88.911D, S88.911S, S88.912A, S88.912D, S88.912S, S88.919A, S88.919D, S88.919S, S88.921A, S88.921D, S88.921S, S88.922A, S88.922D, S88.922S, S88.929A, S88.929D, S88.929S, S98.111A, S98.111D, S98.111S, S98.112A, S98.112D, S98.112S, S98.119A, S98.119D, S98.119S, S98.121A, S98.121D, S98.121S, S98.122A, S98.122D, S98.122S, S98.129A, S98.129D, S98.129S, S98.131A, S98.131D, S98.131S, S98.132A, S98.132D, S98.132S,</p>
<p>S98.139A, S98.139D, S98.139S, S98.141A, S98.141D, S98.141S, S98.142A, S98.142D, S98.142S, S98.149A, S98.149D, S98.149S, S98.211A, S98.211D, S98.211S, S98.212A, S98.212D, S98.212S, S98.219A, S98.219D, S98.219S, S98.221A, S98.221D, S98.221S,</p>
<p>S98.222A, S98.222D, S98.222S, S98.229A, S98.229D, S98.229S, S98.311A, S98.311D, S98.311S, S98.312A, S98.312D, S98.312S, S98.319A, S98.319D, S98.319S, S98.321A, S98.321D, S98.321S, S98.322A, S98.322D, S98.322S, S98.329A, S98.329D, S98.329S,</p>
<p>S98.911A, S98.911D, S98.911S, S98.912A, S98.912D, S98.912S, S98.919A, S98.919D, S98.919S, S98.921A, S98.921D, S98.921S, S98.922A, S98.922D, S98.922S, S98.929A, S98.929D, S98.929S, T87.30, T87.31, T87.32, T87.33, T87.34, T87.40, T87.41, T87.42, T87.43, T87.44, T87.50, T87.51, T87.52, T87.53, T87.54, T87.81, T87.89, T87.9</p></th>
</tr>
<tr class="odd">
<th><p>Breast Cancer Registry</p>
<p>(VA BREAST CA)</p></th>
<th>C50.011, C50.012, C50.019, C50.021, C50.022, C50.029, C50.111, C50.112, C50.119, C50.121, C50.122, C50.129, C50.211, C50.212, C50.219, C50.221, C50.222, C50.229, C50.311, C50.312, C50.319, C50.321, C50.322, C50.329, C50.411, C50.412, C50.419, C50.421, C50.422, C50.429, C50.511, C50.512, C50.519, C50.521, C50.522, C50.529, C50.611, C50.612, C50.619, C50.621, C50.622, C50.629, C50.811, C50.812, C50.819, C50.821, C50.822, C50.829, C50.911, C50.912, C50.919, C50.921, C50.922, C50.929, D05.00, D05.01, D05.02, D05.10, D05.11, D05.12, D05.80, D05.81, D05.82, D05.90, D05.91, D05.92, Z85.3, Z86.000</th>
</tr>
<tr class="header">
<th><p>Cerebrovascular Disease Registry</p>
<p>(VA CVD)</p></th>
<th>I63.00, I63.011, I63.012, I63.019, I63.02, I63.031, I63.032, I63.039, I63.09, I63.10, I63.111, I63.112, I63.119, I63.12, I63.131, I63.132, I63.139, I63.19, I63.20, I63.211, I63.212, I63.219, I63.22, I63.231, I63.232, I63.239, I63.29, I63.30, I63.311, I63.312, I63.319, I63.321, I63.322, I63.329, I63.331, I63.332, I63.339, I63.341, I63.342, I63.349, I63.39, I63.40, I63.411, I63.412, I63.419, I63.421, I63.422, I63.429, I63.431, I63.432, I63.439, I63.441, I63.442, I63.449, I63.49, I63.50, I63.511, I63.512, I63.519, I63.521, I63.522, I63.529, I63.531, I63.532, I63.539, I63.541, I63.542, I63.549, I63.59, I63.6, I63.8, I63.9, I69.30, I69.31, I69.320, I69.321, I69.322, I69.323, I69.328, I69.331, I69.332, I69.333, I69.334, I69.339, I69.341, I69.342, I69.343, I69.344, I69.349, I69.351, I69.352, I69.353, I69.354, I69.359, I69.361, I69.362, I69.363, I69.364, I69.365, I69.369, I69.390, I69.391, I69.392, I69.393, I69.398</th>
</tr>
<tr class="odd">
<th><p>Congestive Heart Failure (CHF) Registry</p>
<p>(VA CHF)</p></th>
<th>I09.81, I50.1, I50.20, I50.21, I50.22, I50.23, I50.30, I50.31, I50.32, I50.33, I50.40, I50.41, I50.42, I50.43, I50.9</th>
</tr>
<tr class="header">
<th><p>Chronic Obstructive Pulmonary Disease Registry</p>
<p>(VA COPD)</p></th>
<th>J40., J41.0, J41.1, J41.8, J42., J43.0, J43.1, J43.2, J43.8, J43.9, J44.0, J44.1, J44.9</th>
</tr>
<tr class="odd">
<th><p>Chronic Renal Disease Registry</p>
<p>(VA CRD)</p></th>
<th>I13.0, I13.10, I13.11, I13.2, N18.1, N18.2, N18.3, N18.4, N18.5, N18.6, N18.9, R88.0, Z49.01, Z49.02, Z49.31, Z49.32, Z94.0, Z99.2</th>
</tr>
<tr class="header">
<th><p>Colorectal Cancer Registry</p>
<p>(VA COLORECTAL CANCER)</p></th>
<th>C18.%, C19, C20</th>
</tr>
<tr class="odd">
<th><p>COVID-19 Registry</p>
<p>(VA COVID19)</p></th>
<th>U07.1</th>
</tr>
<tr class="header">
<th><p>Crohn’s Disease Registry</p>
<p>(VA CROHNS)</p></th>
<th>K50.00, K50.011, K50.012, K50.013, K50.014, K50.018, K50.019, K50.10, K50.111, K50.112, K50.113, K50.114, K50.118, K50.119, K50.80, K50.811, K50.812, K50.813, K50.814, K50.818, K50.819, K50.90, K50.911, K50.912, K50.913, K50.914, K50.918, K50.919</th>
</tr>
<tr class="odd">
<th><p>Dementia Registry</p>
<p>(VA DEMENTIA)</p></th>
<th>A81.00, A81.01, A81.09, A81.2, A81.89, A81.9, F01.50, F01.51, F02.80, F02.81, F03.90, F03.91, F10.27, F19.97, G23.1, G30.0, G30.1, G30.8, G30.9, G31.01, G31.09, G31.83, G90.3</th>
</tr>
<tr class="header">
<th><p>Diabetes Registry</p>
<p>(VA DIABETES)</p></th>
<th>E08.00, E08.01, E08.10, E08.11, E08.21, E08.22, E08.29, E08.311, E08.319, E08.321, E08.329, E08.331, E08.339, E08.341, E08.349, E08.351, E08.359, E08.36, E08.39, E08.40, E08.41, E08.42, E08.43, E08.44, E08.49, E08.51, E08.52, E08.59, E08.610, E08.618, E08.620, E08.621, E08.622, E08.628, E08.630, E08.638, E08.641, E08.649, E08.65, E08.69, E08.8, E08.9, E09.00, E09.01, E09.10, E09.11, E09.21, E09.22, E09.29, E09.311, E09.319, E09.321, E09.329, E09.331, E09.339, E09.341, E09.349, E09.351, E09.359, E09.36, E09.39, E09.40, E09.41, E09.42, E09.43, E09.44, E09.49, E09.51, E09.52, E09.59, E09.610, E09.618, E09.620, E09.621, E09.622, E09.628, E09.630, E09.638, E09.641, E09.649, E09.65, E09.69, E09.8, E09.9, E10.10, E10.11, E10.21, E10.22, E10.29, E10.311, E10.319, E10.321, E10.329, E10.331, E10.339, E10.341, E10.349, E10.351, E10.359, E10.36, E10.39, E10.40, E10.41, E10.42, E10.43, E10.44, E10.49, E10.51, E10.52, E10.59, E10.610, E10.618, E10.620, E10.621, E10.622, E10.628, E10.630, E10.638, E10.641, E10.649, E10.65, E10.69, E10.8, E10.9, E11.00, E11.01, E11.21, E11.22, E11.29, E11.311, E11.319, E11.321, E11.329, E11.331, E11.339, E11.341, E11.349, E11.351, E11.359, E11.36, E11.39, E11.40, E11.41, E11.42, E11.43, E11.44, E11.49, E11.51, E11.52, E11.59, E11.610, E11.618, E11.620, E11.621, E11.622, E11.628, E11.630, E11.638, E11.641, E11.649, E11.65, E11.69, E11.8, E11.9, E13.00, E13.01, E13.10, E13.11, E13.21, E13.22, E13.29, E13.311, E13.319, E13.321, E13.329, E13.331, E13.339, E13.341, E13.349, E13.351, E13.359, E13.36, E13.39, E13.40, E13.41, E13.42, E13.43, E13.44, E13.49, E13.51, E13.52, E13.59, E13.610, E13.618, E13.620, E13.621, E13.622, E13.628, E13.630, E13.638, E13.641, E13.649, E13.65, E13.69, E13.8, E13.9, Z46.81, Z96.41</th>
</tr>
<tr class="odd">
<th><p>Dyslipidemia Registry</p>
<p>(VA DYSLIPIDEMIA)</p></th>
<th>E78.0, E78.1, E78.2, E78.3, E78.4, E78.5</th>
</tr>
<tr class="header">
<th><p>Frailty Registry</p>
<p>(VA FRAILTY)</p></th>
<th>M62.84, R54.</th>
</tr>
<tr class="odd">
<th><p>Head and Neck Squamous Cell Cancer Registry</p>
<p>(VA HEAD AND NECK)</p></th>
<th>C00.0, C00.1, C00.2, C00.3, C00.4, C00.5, C00.6, C00.8, C00.9, C01., C02.0, C02.1, C02.2, C02.3, C02.4, C02.8, C02.9, C03.0, C03.1, C03.9, C04.0, C04.1, C04.8, C04.9, C05.0, C05.1, C05.2, C05.8, C05.9, C06.0, C06.1, C06.2, C06.80, C06.89, C06.9, C07., C08.0, C08.1, C08.9, C09.0, C09.1, C09.8, C09.9, C10.0, C10.2, C10.3, C10.4, C10.8, C10.9, C11.0, C11.1, C11.2, C11.3, C11.8, C11.9, C12., C13.0, C13.1, C13.2, C13.8, C13.9, C14.0, C14.2, C14.8, C30.0, C30.1, C31.0, C31.1, C31.2, C31.3, C31.8, C31.9, C32.0, C32.1, C32.2, C32.3, C32.8, C32.9, C33., C43.0, C43.10, C43.11, C43.111, C43.112, C43.12, C43.121, C43.122, C43.20, C43.21, C43.22, C43.30, C43.31, C43.39, C43.4, C44.00, C44.01, C44.02, C44.09, C44.101, C44.102, C44.1021, C44.1022, C44.109, C44.1091, C44.1092, C44.111, C44.112, C44.1121, C44.1122, C44.119, C44.1191, C44.1192, C44.121, C44.122, C44.1221, C44.1222, C44.129, C44.1291, C44.1292, C44.131, C44.1321, C44.1322, C44.1391, C44.1392, C44.191, C44.192, C44.1921, C44.1922, C44.199, C44.1991, C44.1992, C44.201, C44.202, C44.209, C44.211, C44.212, C44.219, C44.221, C44.222, C44.229, C44.291, C44.292, C44.299, C44.300, C44.301, C44.309, C44.310, C44.311, C44.319, C44.320, C44.321, C44.329, C44.390, C44.391, C44.399, C44.40, C44.41, C44.42, C44.49, C4A.10, C4A.11, C4A.111, C4A.112, C4A.12, C4A.121, C4A.122, C4A.20, C4A.21, C4A.22, C4A.30, C4A.31, C4A.39, C4A.4, C73., C75.0, C76.0, C77.0</th>
</tr>
<tr class="header">
<th><p>Hepatitis B Registry</p>
<p>(VA HEPB)</p></th>
<th>B16.0, B16.1, B16.2, B16.9, B17.0, B18.0, B18.1, B19.10, B19.11, Z22.51</th>
</tr>
<tr class="odd">
<th><p>Hepatocellular Carcinoma Registry</p>
<p>(VA HCC)</p></th>
<th>C22.0</th>
</tr>
<tr class="header">
<th><p>Hypertension Registry</p>
<p>(VA HTN)</p></th>
<th>H35.031, H35.032, H35.033, H35.039, I10., I11.0, I11.9, I12.0, I12.9, I13.0, I13.10, I13.11, I13.2, I15.0, I15.1, I15.2, I15.8, I15.9, I67.4, I87.301, I87.302, I87.303, I87.309, I87.311, I87.312, I87.313, I87.319, I87.321, I87.322, I87.323, I87.329, I87.331, I87.332, I87.333, I87.339, I87.391, I87.392, I87.393, I87.399, O10.02, O10.03, O10.12, O10.13, O10.22, O10.23, O10.32, O10.33, O10.42, O10.43, O10.92, O10.93, O11.1, O11.2, O11.3,O11.9</th>
</tr>
<tr class="odd">
<th><p>Hypoparathyroidism Registry</p>
<p>(VA HYPOPARA)</p></th>
<th>E20.0, E20.8, E20.9, E89.2</th>
</tr>
<tr class="header">
<th><p>Hypothyroidism Registry</p>
<p>(VA HYPOTHYROIDISM)</p></th>
<th>E03.0, E03.1, E03.2, E03.3, E03.4, E03.5, E03.8, E03.9</th>
</tr>
<tr class="odd">
<th><p>Idiopathic Pulmonary Fibrosis (IPF) Registry</p>
<p>(VA IPF)</p></th>
<th>J84.112</th>
</tr>
<tr class="header">
<th><p>Interstitial Lung Disease (ILD) Registry</p>
<p>(VA ILD)</p></th>
<th>J84.10, J84.89, J84.01, J84.03, J84.02, J84.111, J84.112, J84.113, J84.114, J84.115, J84.2, J84.116, J84.117, J84.81, J84.82, J84.841, J84.842, J84.83, J84.843, J84.848, J84.9, D86.0, D86.1, D86.2, J99., M32.13, M33.01, M35.02, M33.11, M33.91, M33.21, M05.19, M05.112, M05.111, M05.119, M05.121, M05.122, M05.129, M05.131, M05.132, M05.139, M05.141, M05.142, M05.149, M05.151, M05.152, M05.159, M05.161, M05.162, M05.169, M05.171, M05.172, M05.179, J61., J70.1, J67.9</th>
</tr>
<tr class="odd">
<th><p>Ischemic Heart Disease (IHD) Registry</p>
<p>(VA IHD)</p></th>
<th>I20.1, I20.8, I20.9, I21.01, I21.02, I21.09, I21.11, I21.19, I21.21, I21.29, I21.3, I21.4, I22.0, I22.1, I22.2, I22.8, I22.9, I23.0, I23.1, I23.2, I23.3, I23.4, I23.5, I23.6, I23.7, I23.8, I24.0, I24.1, I24.8, I24.9, I25.10, I25.110, I25.111, I25.118, I25.119, I25.2, I25.5, I25.6, I25.700, I25.701, I25.708, I25.709, I25.710, I25.711, I25.718, I25.719, I25.720, I25.721, I25.728, I25.729, I25.730, I25.731, I25.738, I25.739, I25.750, I25.751, I25.758, I25.759, I25.760, I25.761, I25.768, I25.769, I25.790, I25.791, I25.798, I25.799, I25.810, I25.811, I25.812, I25.83, I25.89, I25.9, I20.0</th>
</tr>
<tr class="header">
<th><p>Low Vision / Blind Registry</p>
<p>(VA BLIND)</p></th>
<th><p>H54.0, H54.2, H54.3, H54.7, H54.8, H54.10, H54.11, H54.12, H54.40, H54.41, H54.42, H54.50, H54.51, H54.52, H54.60, H54.61,</p>
<p>H54.62</p></th>
</tr>
<tr class="odd">
<th><p>Lung Cancer Registry</p>
<p>(VA LUNG CANCER)</p></th>
<th>C34.%</th>
</tr>
<tr class="header">
<th><p>Lymphoma Registry</p>
<p>(VA LYMPHOMA)</p></th>
<th>C91.50, C91.51, C91.52, C84.70, C84.71, C84.72, C84.73, C84.74, C84.75, C84.76, C84.77, C84.78, C84.79, C84.60, C84.61, C84.62, C84.63, C84.64, C84.65, C84.66, C84.67, C84.68, C84.69, C85.10, C85.11, C85.12, C85.13, C85.14, C85.15, C85.16, C85.17, C85.18, C85.19, C83.50, C83.51, C83.52, C83.53, C83.54, C83.55, C83.56, C83.57, C83.58, C83.59, C88.0, C88.3, C88.4, C83.70, C83.71, C83.72, C83.73, C83.74, C83.75, C83.76, C83.77, C83.78, C83.79, C83.10, C83.11, C83.12, C83.13, C83.14, C83.15, C83.16, C83.17, C83.18, C83.19, C82.60, C82.61, C82.62, C82.63, C82.64, C82.65, C82.66, C82.67, C82.68, C82.69 C84.A0, C84.A1, C84.A2, C84.A3, C84.A4, C84.A5, C84.A6, C84.A7, C84.A8, C84.A9, C82.50, C82.51, C82.52, C82.53, C82.54, C82.55, C82.56, C82.57, C82.58, C82.59, C83.30, C83.31, C83.32, C83.33, C83.34, C83.35, C83.36, C83.37, C83.38, C83.39, C86.0, C86.1, C86.2, C86.3, C86.4, C86.5, C86.6, C82.90, C82.91, C82.92, C82.93, C82.94, C82.95, C82.96, C82.97, C82.98, C82.99, C82.00, C82.01, C82.02, C82.03, C82.04, C82.05, C82.06, C82.07, C82.08, C82.09, C82.10, C82.11, C82.12, C82.13, C82.14, C82.15, C82.16, C82.17, C82.18, C82.19, C82.20, C82.21, C82.22, C82.23, C82.24, C82.25, C82.26, C82.27, C82.28, C82.29, C82.30, C82.31, C82.32, C82.33, C82.34, C82.35, C82.36, C82.37, C82.38, C82.39, C82.40, C82.41, C82.42, C82.43, C82.44, C82.45, C82.46, C82.47, C82.48, C82.49, C82.80, C82.81, C82.82, C82.83, C82.84, C82.85, C82.86, C82.87, C82.88, C82.89, C85.90, C85.91, C85.92, C85.93, C85.94, C85.95, C85.96, C85.97, C85.98, C85.99, C96.A, C81.90, C81.91, C81.92, C81.93, C81.94, C81.95, C81.96, C81.97, C81.98, C81.99, C81.30, C81.31, C81.32, C81.33, C81.34, C81.35, C81.36, C81.37, C81.38, C81.39, C81.40, C81.41, C81.42, C81.43, C81.44, C81.45, C81.46, C81.47, C81.48, C81.49, C81.20, C81.21, C81.22, C81.23, C81.24, C81.25, C81.26, C81.27, C81.28, C81.29, C81.00, C81.01, C81.02, C81.03, C81.04, C81.05, C81.06, C81.07, C81.08, C81.09, C81.10, C81.11, C81.12, C81.13, C81.14, C81.15, C81.16, C81.17, C81.18, C81.19, C81.70, C81.71, C81.72, C81.73, C81.74, C81.75, C81.76, C81.77, C81.78, C81.79, C83.80, C83.81, C83.82, C83.83, C83.84, C83.85, C83.86, C83.87, C83.88, C83.89, C84.40, C84.41, C84.42, C84.43, C84.44, C84.45, C84.46, C84.47, C84.48, C84.49, C83.00, C83.01, C83.02, C83.03, C83.04, C83.05, C83.06, C83.07, C83.08, C83.09, C84.90, C84.91, C84.92, C84.93, C84.94, C84.95, C84.96, C84.97, C84.98, C84.99, C84.Z0, C84.Z1, C84.Z2, C84.Z3, C84.Z4, C84.Z5, C84.Z6, C84.Z7, C84.Z8, C84.Z9, C85.20, C85.21, C85.22, C85.23, C85.24, C85.25, C85.26, C85.27, C85.28, C85.29, C83.90, C83.91, C83.92, C83.93, C83.94, C83.95, C83.96, C83.97, C83.98, C83.99, C85.80, C85.81, C85.82, C85.83, C85.84, C85.85, C85.86, C85.87, C85.88, C85.89</th>
</tr>
<tr class="odd">
<th><p>Melanoma Registry</p>
<p>(VA MELANOMA)</p></th>
<th>C43.%</th>
</tr>
<tr class="header">
<th><p>Mental Health Registry</p>
<p>(VA MENTAL HEALTH)</p></th>
<th>F06.32, F06.34, F20.0, F20.1, F20.2, F20.3, F20.5, F20.9, F20.81, F20.89, F25.0, F25.1, F25.8, F25.9, F30.2, F30.3, F30.4, F30.8, F30.9, F30.10, F30.11, F30.12, F30.13, F31.0, F31.2, F31.4, F31.5, F31.9, F31.10, F31.11, F31.12, F31.13, F31.30, F31.31, F31.32, F31.60, F31.61, F31.62, F31.63, F31.64, F31.70, F31.71, F31.72, F31.73, F31.74, F31.75, F31.76, F31.77, F31.78, F31.81, F31.89, F32.0, F32.1, F32.2, F32.3, F32.4, F32.5, F32.9, F33.0, F33.1, F33.2, F33.3, F33.8, F33.9, F33.40, F33.41, F33.42, F34.1, F34.8, F34.9, F39., F43.10, F43.11, F43.12, F43.21, F43.23</th>
</tr>
<tr class="odd">
<th><p>Movement Disorders Registry</p>
<p>(VA MOVEMENT DISORDERS)</p></th>
<th>G20., G21.0, G21.11, G21.19, G21.2, G21.3, G21.4, G21.8, G21.9, G23.0, G23.1, G23.2, G23.8, G23.9, G24.01, G24.02, G24.09, G24.1, G24.2, G24.3, G24.4, G24.5, G24.8, G24.9, G25.0, G25.1, G25.2, G25.3, G25.4, G25.5, G25.61, G25.69, G25.70, G25.71, G25.79, G25.81, G25.82, G25.83, G25.89, G25.9, G26, G31.83, G10, K11.7</th>
</tr>
<tr class="header">
<th><p>Multiple Sclerosis Registry</p>
<p>(VA MULTIPLE SCLEROSIS)</p></th>
<th>G35</th>
</tr>
<tr class="odd">
<th><p>Non-Alcoholic SteatoHepatitis (NASH) Registry</p>
<p>(VA NASH)</p></th>
<th>K75.81, K76.0</th>
</tr>
<tr class="header">
<th><p>Obstructive Sleep Apnea Registry</p>
<p>(VA APNEA)</p></th>
<th>G47.30, G47.31, G47.32, G47.33, G47.34, G47.35, G47.36, G47.37, G47.39</th>
</tr>
<tr class="odd">
<th><p>Osteoarthritis Registry</p>
<p>(VA OSTEOARTHRITIS)</p></th>
<th>M15.0, M15.1, M15.2, M15.3, M15.4, M15.8, M15.9, M16.0, M16.2, M16.4, M16.6, M16.7, M16.9, M16.10, M16.11, M16.12, M16.30, M16.31, M16.32, M16.50, M16.51, M16.52, M17.0, M17.2, M17.4, M17.5, M17.9, M17.10, M17.11, M17.12, M17.30, M17.31, M17.32, M18.0, M18.2, M18.4, M18.9, M18.10, M18.11, M18.12, M18.30, M18.31, M18.32, M18.50, M18.51, M18.52, M19.011, M19.012, M19.019, M19.021, M19.022, M19.029, M19.031, M19.032, M19.039, M19.041, M19.042, M19.049, M19.071, M19.072, M19.079, M19.90, M19.91, M19.92, M19.93, M19.111, M19.112, M19.119, M19.121, M19.122, M19.129, M19.131, M19.132, M19.139, M19.141, M19.142, M19.149, M19.171, M19.172, M19.179, M19.211, M19.212, M19.219, M19.221, M19.222, M19.229, M19.231, M19.232, M19.239, M19.241, M19.242, M19.249, M19.271, M19.272, M19.279</th>
</tr>
<tr class="header">
<th><p>Osteoporosis Registry</p>
<p>(VA OSTEOPOROSIS)</p></th>
<th>M80.%, M81.%</th>
</tr>
<tr class="odd">
<th><p>Pancreatic Cancer Registry</p>
<p>(VA PANCREATIC CANCER)</p></th>
<th>C25.%</th>
</tr>
<tr class="header">
<th><p>Prostate Cancer Registry</p>
<p>(VA PROSTATE CANCER)</p></th>
<th>C61</th>
</tr>
<tr class="odd">
<th>Recent Patients (VA RECENT PATIENTS)</th>
<th>Selection is based on any Admission or Visit date within the last two years. The nightly ROR TASK has been modified to add or remove patients based upon a two year window.</th>
</tr>
<tr class="header">
<th><p>Rheumatoid Arthritis Registry</p>
<p>(VA RHEUM)</p></th>
<th>M05.00, M05.09, M05.10, M05.011, M05.012, M05.019, M05.021, M05.022, M05.029, M05.031, M05.032, M05.039, M05.041, M05.042, M05.049, M05.051, M05.052, M05.059, M05.061, M05.062, M05.069, M05.071, M05.072, M05.079, M05.111, M05.112, M05.119, M05.121, M05.122, M05.129, M05.131, M05.132, M05.139, M05.141, M05.142, M05.149, M05.151, M05.152, M05.159, M05.161, M05.162, M05.169, M05.171, M05.172, M05.179, M05.19, M05.20, M05.211, M05.212, M05.219, M05.221, M05.222, M05.229, M05.231, M05.232, M05.239, M05.241, M05.242, M05.249, M05.251, M05.252, M05.259, M05.261, M05.262, M05.269, M05.271, M05.272, M05.279, M05.29, M05.30, M05.311, M05.312, M05.319, M05.321, M05.322, M05.329, M05.331, M05.332, M05.339, M05.341, M05.342, M05.349, M05.351, M05.352, M05.359, M05.361, M05.362, M05.369, M05.371, M05.372, M05.379, M05.39, M05.40, M05.411, M05.412, M05.419, M05.421, M05.422, M05.429, M05.431, M05.432, M05.439, M05.441, M05.442, M05.449, M05.451, M05.452, M05.459, M05.461, M05.462, M05.469, M05.471, M05.472, M05.479, M05.49, M05.50, M05.511, M05.512, M05.519, M05.521, M05.522, M05.529, M05.531, M05.532, M05.539, M05.541, M05.542, M05.549, M05.551, M05.552, M05.559, M05.561, M05.562, M05.569, M05.571, M05.572, M05.579, M05.59, M05.60, M05.611, M05.612, M05.619, M05.621, M05.622, M05.629, M05.631, M05.632, M05.639, M05.641, M05.642, M05.649, M05.651, M05.652, M05.659, M05.661, M05.662, M05.669, M05.671, M05.672, M05.679, M05.69, M05.70, M05.711, M05.712, M05.719, M05.721, M05.722, M05.729, M05.731, M05.732, M05.739, M05.741, M05.742, M05.749, M05.751, M05.752, M05.759, M05.761, M05.762, M05.769, M05.771, M05.772, M05.779, M05.79, M05.80, M05.811, M05.812, M05.819, M05.821, M05.822, M05.829, M05.831, M05.832, M05.839, M05.841, M05.842, M05.849, M05.851, M05.852, M05.859, M05.861, M05.862, M05.869, M05.871, M05.872, M05.879, M05.89, M05.9, M06.00, M06.011, M06.012, M06.019, M06.021, M06.022, M06.029, M06.031, M06.032, M06.039, M06.041, M06.042, M06.049, M06.051, M06.052, M06.059, M06.061, M06.062, M06.069, M06.071, M06.072, M06.079, M06.08, M06.09, M06.1, M06.20, M06.211, M06.212, M06.219, M06.221, M06.222, M06.229, M06.231, M06.232, M06.239, M06.241, M06.242, M06.249, M06.251, M06.252, M06.259, M06.261, M06.262, M06.269, M06.271, M06.272, M06.279, M06.28, M06.29, M06.30, M06.311, M06.312, M06.319, M06.321, M06.322, M06.329, M06.331, M06.332, M06.339, M06.341, M06.342, M06.349, M06.351, M06.352, M06.359, M06.361, M06.362, M06.369, M06.371, M06.372, M06.379, M06.38, M06.39, M06.4, M06.80, M06.811, M06.812, M06.819, M06.821, M06.822, M06.829, M06.831, M06.832, M06.839, M06.841, M06.842, M06.849, M06.851, M06.852, M06.859, M06.861, M06.862, M06.869, M06.871, M06.872, M06.879, M06.88, M06.89, M06.9, M08.00, M08.011, M08.012, M08.019, M08.021, M08.022, M08.029, M08.031, M08.032, M08.039, M08.041, M08.042, M08.049, M08.051, M08.052, M08.059, M08.061, M08.062, M08.069, M08.071, M08.072, M08.079, M08.08, M08.09, M08.1, M08.20, M08.211, M08.212, M08.219, M08.221, M08.222, M08.229, M08.231, M08.232, M08.239, M08.241, M08.242, M08.249, M08.251, M08.252, M08.259, M08.261, M08.262, M08.269, M08.271, M08.272, M08.279, M08.28, M08.29, M08.3, M08.40, M08.411, M08.412, M08.419, M08.421, M08.422, M08.429, M08.431, M08.432, M08.439, M08.441, M08.442, M08.449, M08.451, M08.452, M08.459, M08.461, M08.462, M08.469, M08.471, M08.472, M08.479, M08.48, M12.00, M12.011, M12.012, M12.019, M12.021, M12.022, M12.029, M12.031, M12.032, M12.039, M12.041, M12.042, M12.049, M12.051, M12.052, M12.059, M12.061, M12.062, M12.069, M12.071, M12.072, M12.079, M12.08, M12.09</th>
</tr>
<tr class="odd">
<th><p>Thyroid Cancer Registry</p>
<p>(VA THYROID CA)</p></th>
<th>C73., Z85.850</th>
</tr>
<tr class="header">
<th><p>Total HIP Replacement Registry</p>
<p>(VA TOTAL HIP)</p></th>
<th>0SR9%, 0SRB%, 0SRA0, 0SRE0</th>
</tr>
<tr class="odd">
<th><p>Total KNEE Replacement Registry</p>
<p>(VA TOTAL KNEE)</p></th>
<th>0SRC%, 0SRD%, 0SRT0, 0SRU0, 0SRV0, 0SRW0</th>
</tr>
<tr class="header">
<th><p>Transgender Registry</p>
<p>(VA TRANSGENDER)</p></th>
<th>F64.0, F64.1, F64.2, F64.8, F64.9, F65.1 (see Note in Section 11.3.1)</th>
</tr>
<tr class="odd">
<th><p>Transplant Heart Registry</p>
<p>(VA TRANSPLANT HEART)</p></th>
<th>T86.20, T86.21, T86.22, T86.23, T86.290, T86.298, T86.30, T86.31, T86.32, T86.33, T86.39, Z48.21, Z48.280, Z94.1, Z94.3</th>
</tr>
<tr class="header">
<th><p>Transplant Intestine Registry</p>
<p>(VA TRANSPLANT INTESTINE)</p></th>
<th>T86.850, T86.851, T86.852, T86.858, T86.859, Z94.82</th>
</tr>
<tr class="odd">
<th><p>Transplant Kidney Registry</p>
<p>(VA TRANSPLANT KIDNEY)</p></th>
<th>T86.10, T86.11, T86.12, T86.13, T86.19, Z48.22, Z94.0</th>
</tr>
<tr class="header">
<th><p>Transplant Liver Registry</p>
<p>(VA TRANSPLANT LIVER)</p></th>
<th>T86.40, T86.41, T86.42, T86.43, T86.49, Z48.23, Z94.4</th>
</tr>
<tr class="odd">
<th><p>Transplant Lung Registry</p>
<p>(VA TRANSPLANT LUNG)</p></th>
<th>T86.30, T86.31, T86.32, T86.33, T86.39, T86.810, T86.811, T86.812, T86.818, T86.819, Z48.24, Z48.280, Z94.2</th>
</tr>
<tr class="header">
<th><p>Transplant Pancreas Registry</p>
<p>(VA TRANSPLANT PANCREAS)</p></th>
<th>Z94.83</th>
</tr>
<tr class="odd">
<th><p>Ulcerative Colitis Registry</p>
<p>(VA UC)</p></th>
<th>K51.00, K51.011, K51.012, K51.013, K51.014, K51.018, K51.019, K51.20, K51.211, K51.212, K51.213, K51.214, K51.218, K51.219, K51.011, K51.30, K51.311, K51.312, K51.313, K51.314, K51.318, K51.319, K51.40, K51.411, K51.412, K51.413, K51.414, K51.418, K51.419, K51.50, K51.511, K51.512, K51.513, K51.514, K51.518, K51.519, K51.80, K51.811, K51.812, K51.813, K51.814, K51.818, K51.819, K51.90, K51.911, K51.912, K51.913, K51.914, K51.918, K51.919</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Registry (Abbreviation)</th>
<th>CPT Codes</th>
</tr>
<tr class="odd">
<th><p>Total KNEE Replacement Registry</p>
<p>(VA TOTAL KNEE)</p></th>
<th>27447</th>
</tr>
<tr class="header">
<th><p>Total HIP Replacement Registry</p>
<p>(VA TOTAL HIP)</p></th>
<th>27130, 27132</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

| COVID-19 related Laboratory Tests      | LOINC                                                                                    |
|----------------------------------------|------------------------------------------------------------------------------------------|
| SARS coronavirus 2 N gene              | 94307-6, 94308-4, 94311-8, 94316-7, 94533-7, 94756-4, 94757-2, 94760-6, 94766-3, 95409-9 |
| SARS coronavirus 2                     | 94309-2, 94500-6, 94565-9, 94660-8, 94759-8, 94819-0, 94822-4, 94845-5, 95406-5          |
| SARS-like coronavirus N gene           | 94310-0                                                                                  |
| SARS coronavirus 2 RdRp gene           | 94314-2, 94534-5                                                                         |
| SARS-related coronavirus E gene        | 94315-9, 94758-0, 94765-5                                                                |
| SARS-related coronavirus RNA           | 94502-2                                                                                  |
| SARS coronavirus 2 Ag                  | 94558-4                                                                                  |
| SARS coronavirus 2 ORF1ab region       | 94559-2, 94639-2                                                                         |
| SARS coronavirus 2 S gene              | 94640-0, 94641-8, 94767-1                                                                |
| SARS-related coronavirus RNA           | 94647-5                                                                                  |
| SARS coronavirus+SARS coronavirus 2 Ag | 95209-3                                                                                  |

Positive results are identified as results that are equal to “P” or that contain “POS” “DETEC” or “REA” and do not contain “NEG” “NO” “UNDET” or “IND.” Comparisons are *not* case sensitive.

## CCR:HIV Registry Pending Patient Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HIV Pending Patient Worksheet Name: Last 4: Pt should be added to ICR: ❑YES ❑NO

1.  HIV positive test result /other evidence: ❑NONE - delete from registry

| ❑   | \+ ELISA date:          | ❑   | \+ Western Blot date: |
|-----|-------------------------|-----|-----------------------|
| ❑   | \+ HIV Viral load date: | ❑   | Narrative Note date:  |

2.  HIV Risk info: ❑UNKNOWN

| ❑   | Sex with male                                                           | ❑   | HETEROSEXUAL relations with transfusion recipient with documented HIV infection  |
|-----|-------------------------------------------------------------------------|-----|----------------------------------------------------------------------------------|
| ❑   | Sex with female                                                         | ❑   | HETEROSEXUAL relations with transplant recipient with documented HIV infection   |
| ❑   | Injected nonprescription drug                                           | ❑   | HETEROSEXUAL relations with PWA or documented HIV+, risk not specified           |
| ❑   | Received clotting factor for hemophilia / coagulation disorder          | ❑   | Received transfusion of blood/blood component (other than clotting factor)       |
| ❑   | HETEROSEXUAL relations with bisexual male                               | ❑   | Received transfusion of blood/blood component (other than clotting factor)       |
| ❑   | HETEROSEXUAL relations with injection drug user                         | ❑   | Mycobacterium avium complex or M. kansasii, disseminated or extrapulmonary: date |
| ❑   | HETEROSEXUAL relations with person with hemophilia/coagulation disorder | ❑   | Received transplant of tissue/organ(s) or artificial insemination                |
|     |                                                                         | ❑   | Worked in health care or clinical laboratory setting                             |

3.  AIDS OI History ❑ NONE

| ❑   | Candidiasis of bronchi, trachea, or lungs: date                                                           | ❑   | Lymphoma, Burkitt's (or equivalent term): date                                             |
|-----|-----------------------------------------------------------------------------------------------------------|-----|--------------------------------------------------------------------------------------------|
| ❑   | Candidiasis, esophageal: date                                                                             | ❑   | Lymphoma, immunoblastic (or equivalent term): date                                         |
| ❑   | Cervical cancer, invasive: date                                                                           | ❑   | Lymphoma, primary, of brain: date                                                          |
| ❑   | Coccidioidomycosis, disseminated or extrapulmonary: date                                                  | ❑   | Lymphoma, immunoblastic (or equivalent term): date                                         |
| ❑   | Cryptococcosis, extrapulmonary: date                                                                      | ❑   | Lymphoma, primary, of brain: date                                                          |
| ❑   | Cryptosporidiosis, chronic intestinal (\>1 month's duration): date                                        | ❑   | Mycobacterium avium complex or M. kansasii, disseminated or extrapulmonary: date           |
| ❑   | Cytomegalovirus disease (other than liver, spleen, or nodes): date                                        | ❑   | Mycobacterium tuberculosis, any site (pulmonary or extrapulmonary): date                   |
| ❑   | Cytomegalovirus retinitis (with loss of vision): date                                                     | ❑   | Mycobacterium, other species or unidentified species, disseminated or extrapulmonary: date |
| ❑   | Encephalopathy, HIV-related: date                                                                         | ❑   | Pneumocystis carinii pneumonia: date                                                       |
| ❑   | Herpes simplex: chronic ulcer(s) (\>1 month's duration); or bronchitis, pneumonitis, or esophagitis: date | ❑   | Pneumonia, recurrent: date                                                                 |
| ❑   | Histoplasmosis, disseminated or extrapulmonary: date                                                      | ❑   | Progressive multifocal leukoencephalopathy: date                                           |
| ❑   | Isosporiasis, chronic intestinal (\>1 month's duration) : date                                            | ❑   | Salmonella septicemia, recurrent: date                                                     |
| ❑   | Kaposi's sarcoma: date                                                                                    | ❑   | Toxoplasmosis of brain: date                                                               |
| ❑   |                                                                                                           | ❑   | Wasting syndrome due to HIV: date                                                          |

4. COMMENTS:

## Clinical Case Registries Shortcut Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the following table, two or more keys connected by a comma (,) indicate that the keys should be pressed in succession. Keys connected by a plus sign (+) indicate that the keys should be pressed at the same time.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 27%" />
<col style="width: 29%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>Window</th>
<th>Option/Text</th>
<th>Shortcut</th>
<th>Action / Opens</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Any</td>
<td></td>
<td><blockquote>
<p>&lt; F1 &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Online Help file</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"></td>
</tr>
<tr class="odd">
<td rowspan="23">Main (Registry)</td>
<td><blockquote>
<p><u>F</u>ile menu</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; , &lt; F &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Open Registry</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; , &lt; F &gt; , &lt; O &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Select a Registry to open</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Save As…</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; , &lt; F &gt; , &lt; A &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Close</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; , &lt; F &gt;, &lt; L &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Close All</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; , &lt; F &gt;, &lt; C &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Page Setup…</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Print Preview…</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Print…</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; , &lt; F &gt; , &lt; P &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Preferences</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Preferences</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Rejoin Clinical Context…</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Break the Clinical Link…</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Exit</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; , &lt; F &gt;, &lt; X &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Registr<u>y</u> menu</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; , &lt; Y &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>&lt; Ctrl &gt; + &lt; F6 &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Next registry</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>&lt; Shift &gt; + &lt; Ctrl &gt; + &lt; F6 &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Previous registry</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>&lt; Ctrl &gt; + &lt; F4 &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Close current registry</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Edit (HIV)</p>
</blockquote></td>
<td><blockquote>
<p>&lt; E &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Human Immunodeficiency Virus Patient Data Editor</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CDC (HIV)</p>
</blockquote></td>
<td><blockquote>
<p>&lt; C &gt;</p>
</blockquote></td>
<td><blockquote>
<p>CDC (Form)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Show Registry users…</p>
</blockquote></td>
<td><blockquote>
<p>&lt; S &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Users of the (HIV or HEPC) Registry</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Edit Site Parameters…</p>
</blockquote></td>
<td><blockquote>
<p>&lt; D &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Confirm (HEPC)</p>
</blockquote></td>
<td><blockquote>
<p>&lt; C &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Hepatitis C Patient Data Editor</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Show Registry Users</p>
</blockquote></td>
<td><blockquote>
<p>&lt; S &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Users of the (HIV or HEPC) Registry</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Edit Site Parameters</p>
</blockquote></td>
<td><blockquote>
<p>&lt; D &gt;</p>
</blockquote></td>
<td><blockquote>
<p>(HIV or HEPC) Site Parameters</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="7">(HIV or HEPC) Site Parameters</td>
<td></td>
<td><blockquote>
<p>&lt; Ctrl &gt; + &lt; Alt &gt; + &lt; C &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Cancel a search (dual-list selectors on site parameters form, patient search)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>&lt; Space &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Move the record between lists (dual-list selectors)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>&lt; Enter &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Edit cell value (local fields)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Lab Test tab</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; L &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Registry Meds tab</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; M &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Notifications tab</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; N &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Local Fields tab</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; F &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="18">Reports Menu</td>
<td><blockquote>
<p>Reports menu</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; P &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Clinic Follow Up</p>
</blockquote></td>
<td><blockquote>
<p>&lt; C &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Combined Meds and Labs</p>
</blockquote></td>
<td><blockquote>
<p>&lt; O &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Current Inpatient List</p>
</blockquote></td>
<td><blockquote>
<p>&lt; U &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Diagnoses</p>
</blockquote></td>
<td><blockquote>
<p>&lt; D &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>General Utilization and Demographics</p>
</blockquote></td>
<td><blockquote>
<p>&lt; G &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Inpatient Utilization</p>
</blockquote></td>
<td><blockquote>
<p>&lt; I &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Lab Utilization</p>
</blockquote></td>
<td><blockquote>
<p>&lt; L &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>List of Registry Patients</p>
</blockquote></td>
<td><blockquote>
<p>&lt; S &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Outpatient Utilization</p>
</blockquote></td>
<td><blockquote>
<p>&lt; T &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patient Medication History</p>
</blockquote></td>
<td><blockquote>
<p>&lt; P &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pharmacy Prescription Utilization</p>
</blockquote></td>
<td><blockquote>
<p>&lt; H &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Procedures</p>
</blockquote></td>
<td><blockquote>
<p>&lt; E &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Radiology Utilization</p>
</blockquote></td>
<td><blockquote>
<p>&lt; A &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Registry Lab Tests by Range</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Y &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Registry Medications</p>
</blockquote></td>
<td><blockquote>
<p>&lt; M &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VERA Reimbursement Report (HIV only)</p>
</blockquote></td>
<td><blockquote>
<p>&lt; V &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Report List</p>
</blockquote></td>
<td><blockquote>
<p>&lt; R &gt;</p>
</blockquote></td>
<td><blockquote>
<p>List of Reports panel</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="6"><blockquote>
<p>Window Menu</p>
</blockquote></td>
<td><blockquote>
<p>Window menu</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; W &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Cascade</p>
</blockquote></td>
<td><blockquote>
<p>&lt; C &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Tile Horizontally</p>
</blockquote></td>
<td><blockquote>
<p>&lt; H &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Tile Vertically</p>
</blockquote></td>
<td><blockquote>
<p>&lt; V &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Minimize All</p>
</blockquote></td>
<td><blockquote>
<p>&lt; M &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Arrange All</p>
</blockquote></td>
<td><blockquote>
<p>&lt; A &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="5"><blockquote>
<p>Help Menu</p>
</blockquote></td>
<td><blockquote>
<p>Help menu</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; H &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Help Topics</p>
</blockquote></td>
<td><blockquote>
<p>&lt; F1 &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Registry Info</p>
</blockquote></td>
<td><blockquote>
<p>&lt; R &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCOW Status</p>
</blockquote></td>
<td><blockquote>
<p>&lt; C &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>About</p>
</blockquote></td>
<td><blockquote>
<p>&lt; A &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 27%" />
<col style="width: 29%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>Window</th>
<th>Option/Text</th>
<th>Shortcut</th>
<th>Action / Opens</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="12">Report Parameters</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>&lt; Ctrl &gt; + &lt; Alt &gt; + &lt; C &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Cancel a search (double-pane selectors on report parameters forms, patient search)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>&lt; Space &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Move the record between lists (double-pane selectors)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>&lt; Tab &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Move through the report parameters</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>&lt; F1 &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Online Help</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Load Parameters</p>
</blockquote></td>
<td><blockquote>
<p>&lt; L &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Save Parameters</p>
</blockquote></td>
<td><blockquote>
<p>&lt; S &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Default Parameters</p>
</blockquote></td>
<td><blockquote>
<p>&lt; D &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Run</p>
</blockquote></td>
<td><blockquote>
<p>&lt; R &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>&lt; Ctrl &gt; + &lt; F6 &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Next report output</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>&lt; Shift &gt; + &lt; Ctrl &gt; + &lt; F6 &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Previous report output</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>&lt; Ctrl &gt; + &lt; F4 &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Close current report output</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="7">Task Manager tab</td>
<td></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; T &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>&lt; Delete &gt;</p>
</blockquote></td>
<td><blockquote>
<p>In Task list, delete selected records</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Refresh</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; R &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>New Report</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; N &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Open Report</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; O &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>View Log</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; V &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Delete</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; D &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="2">Tech-nical Log tab</td>
<td></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; T &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Refresh</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; R &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="7">Registry tab</td>
<td></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; G &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>&lt; Enter &gt;</p>
</blockquote></td>
<td><blockquote>
<p>(HIV or HEPC) Patient Data Editor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>[Search]</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; R &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Edit (HIV)</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; I &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Human Immunodeficiency Virus Registry Patient Data Editor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Confirm (HEPC)</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; I &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Hepatitis C Registry Patient Data Editor</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CDC (HIV)</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; C &gt;</p>
</blockquote></td>
<td><blockquote>
<p>CDC (Form)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Delete</p>
</blockquote></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; D &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="7"><p>(HIV or HEPC)</p>
<p>Registry Patient Data Editor</p></td>
<td></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; I &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>&lt; Enter &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Edit cell value (local fields)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>&lt; Space &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Toggle a checkbox (local fields)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Clinical Status tab</p>
</blockquote></td>
<td><blockquote>
<p>&lt; L &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Risk Factors tab (HIV)</p>
</blockquote></td>
<td><blockquote>
<p>&lt; R &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Local Fields tab</p>
</blockquote></td>
<td><blockquote>
<p>&lt; F &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Save</p>
</blockquote></td>
<td><blockquote>
<p>&lt; S &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="6">CDC (HIV)</td>
<td></td>
<td><blockquote>
<p>&lt; Alt &gt; + &lt; C &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Form tab</p>
</blockquote></td>
<td><blockquote>
<p>&lt; F &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Preview tab</p>
</blockquote></td>
<td><blockquote>
<p>&lt; V &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Preview page 2 tab</p>
</blockquote></td>
<td><blockquote>
<p>&lt; 2 &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Save</p>
</blockquote></td>
<td><blockquote>
<p>&lt; S &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>&lt; Tab &gt;</p>
</blockquote></td>
<td><blockquote>
<p>Move through the form parameters</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="7">CDC Form</td>
<td></td>
<td><blockquote>
<p>&lt; F &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Group Titles (CDC Parameter groups)</p>
</blockquote></td>
<td><blockquote>
<p>&lt; G &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Zoom In</p>
</blockquote></td>
<td><blockquote>
<p>&lt; I &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Zoom Out</p>
</blockquote></td>
<td><blockquote>
<p>&lt; O &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Fit Width</p>
</blockquote></td>
<td><blockquote>
<p>&lt; W &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Zoom 1:1</p>
</blockquote></td>
<td><blockquote>
<p>&lt; 1 &gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Print</p>
</blockquote></td>
<td><blockquote>
<p>&lt; P &gt;</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

## Command Line Switches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](ror-1-5-42-user-manual/541.png) | Command line switches control basic behavior of the application. They can be appended after the executable name in the <u>T</u>arget field of the application shortcut. Names of the switches are case-insensitive. |
|-----------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

|  Switch                              | Description                                                                                                                     |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| /?, /h,-?, -h                        | Display a dialog box containing a short description of the command line switches accepted by the application (see above figure) |
| /at, -at                             | Turn assistive technology ON for non-JAWS users                                                                                 |
| /noccow, /ccow=off-noccow, -ccow=off | Disable the context management) functionality completely.                                                                       |
| /ccow=patientonly-ccow=patientonly   | Disable the user context functionality (Single Sign-On).                                                                        |
| /p=, /port=-p=, -port=, P=           | Instruct the application to use a non-standard port number on the VistA server.                                                 |
| /r=, /=-r=, -registry=, R=           | Forces the GUI to open only the registry with provided name.                                                                    |
| /s=, /server=-s=, -server=, S=       | Instruct the application to connect to the server defined by the provided host name or IP address.                              |
| /showcerts, -showcerts               | Instruct the application to display the PIV certificate selection screen.                                                       |

Examples:

…\ClinicalCaseRegistries.exe /S=MIRROR /R="VA HIV”

…\ClinicalCaseRegistries.exe /S="1.1.1.1" /P=1111

…\ClinicalCaseRegistries.exe -R="VA HIV"

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Listed below are some commonly asked questions and answers.

How do I check which version of CCR I’m using?

The easier way is to use the Help \| About CCR menu option screen. Your version should match this figure.

When I run CCR, I get a version mismatch error. What do I do?

The CCR Graphical User Interface (GUI) communicates with VistA using a Remote Procedure Call (RPC) to verify that the GUI and MUMPS code versions match. This check is done as soon as the CCR application starts. If you see this warning, either the GUI or the MUMPS code needs to be updated. Contact your local IRM for assistance.

What do I do if I get a connection error with a WSAEADDRNOTAVAIL code?

The CCR Graphical User Interface (GUI) needs the server name or IP address and port so that it knows where to get the VistA data from. Contact your local IRM to make sure the Command Line Switches are set up correctly for your location.

What do I do if I get a connection error with a WSACONNREFUSED code?

The CCR Graphical User Interface (GUI) needs the server name or IP address and port so that it knows where to get the VistA data from. This error can indicate that the specified port is incorrect or that the RPC Broker is not functioning properly. Contact your local IRM to make sure the Command Line Switches are set up correctly for your location and that the RPC Broker is running.

Who do I contact if I have another type of question or error?

Contact your local IRM for any setup related questions. Your local IRM may instruct you to contact the National Help desk if it is an application error.

########### Glossary[^18]

| [  A  ](\l)   | [  B  ](#G_B) | [  C  ](#G_C) | [  D  ](#G_D) | [  E  ](#G_E) | [  F  ](#G_F) | [  G  ](#G_G) | [  H  ](#G_H) | [  I  ](#G_I) |     | [  K  ](#G_K) | [  L  ](#G_L) | [  M  ](#G_M) |
|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|---------------|-----|---------------|---------------|---------------|
| [  N  ](#G_N) | [  O  ](#G_O) | [ P ](#G_P)   |               | [  R  ](#G_R) | [  S  ](#G_S) | [  T  ](#G_T) | [  U  ](#G_U) | [  V  ](#G_V) |     | [  X  ](#G_X) |               |               |
| [0-9](#G_09)  |               |               |               |               |               |               |               |               |     |               |               |               |

*Control-click character to see entries; missing character means no entries for that character.*

| Term or Acronym                                 | Description                    |
|-------------------------------------------------|--------------------------------|
| <span id="G_09" class="anchor"></span>0 - 9 |                                |
| 508                                             | *See* [Section 508](#Glos_508) |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Term or Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><strong>A</strong></td>
</tr>
<tr class="even">
<td colspan="2">AAC</td>
<td><em>See</em> <a href="#Glos_CDCO">Corporate Data Center Operations</a><strong>.</strong></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_AccessCode" class="anchor"></span>Access Code</td>
<td>With each sign-on to <a href="#Glos_VistA">VistA</a>, the user must enter two codes to be recognized and allowed to proceed: the Access Code and Verify Code. The Access Code is assigned by IRM Service and is used by the computer to recognize the user. Each user has a unique access code. The only way this code can be changed is for the IRM Service to edit it. When the code is established by IRM, it is encrypted; that is, it is “scrambled” according to a cipher. The code is stored in the computer only in this encrypted form. Thus, even if the access code is viewed, the viewer cannot determine what the user actually types to tell the computer this code. <em>See also</em> <a href="#Glos_VerifyCode">Verify Code</a>.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_AIDS" class="anchor"></span>Acquired Immunodeficiency Syndrome (AIDS)</td>
<td>AIDS is a disease of the human immune system caused by the human immunodeficiency virus (HIV). This condition progressively reduces the effectiveness of the immune system and leaves individuals susceptible to opportunistic infections and tumors.</td>
</tr>
<tr class="odd">
<td colspan="2">ADPAC</td>
<td><em>See</em> <a href="#Glos_ADPAC">Automated Data Processing Application Coordinator</a><strong>.</strong></td>
</tr>
<tr class="even">
<td colspan="2">AIDS</td>
<td><em>See</em> <a href="#Glos_AIDS">Acquired Immunodeficiency Syndrome</a><strong>.</strong></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_AIDSOI" class="anchor"></span>AIDS-defining Opportunistic Infection (AIDS-OI)</td>
<td>Those illnesses said to be AIDS defining. “Opportunistic infections” are infections that take advantage of a weakened immune system.</td>
</tr>
<tr class="even">
<td colspan="2">AIDS-OI</td>
<td><em>Acronym</em> for <a href="#Glos_AIDSOI">AIDS-defining Opportunistic Infection</a></td>
</tr>
<tr class="odd">
<td colspan="2">AITC</td>
<td><em>See</em> <a href="#Glos_AITC">Austin Information Technology Center</a></td>
</tr>
<tr class="even">
<td colspan="2">AMIS</td>
<td><em>See</em> <a href="#Glos_AMIS">Automated Management Information System</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_ARV" class="anchor"></span>Antiretroviral (medications)</td>
<td><p>Medications for the treatment of infection by <a href="#Glos_retrovirus">retroviruses</a>, primarily <a href="#Glos_HIV">HIV</a>.</p>
<p><em>See also</em> <a href="#Glos_HAART">Highly Active Antiretroviral Therapy</a>.</p></td>
</tr>
<tr class="even">
<td colspan="2">ARV</td>
<td><em>See</em> <a href="#Glos_ARV">Antiretroviral (medications).</a></td>
</tr>
<tr class="odd">
<td colspan="2">Austin Automation Center (AAC)</td>
<td><em>See</em> <a href="#Glos_CDCO">Corporate Data Center Operations</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_AITC" class="anchor"></span>Austin Information Technology Center (AITC)</td>
<td>AITC is a recognized, award-winning Federal data center within the Department of Veterans Affairs (VA). It provides a full complement of cost-efficient e-government solutions to support the information technology (IT) needs of customers within the Federal sector. AITC has also implemented a program of enterprise “best practice” initiatives with major vendor partners that ensures customers receive enhanced, value-added IT services through the implementation of new technologies at competitive costs.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_ADPAC" class="anchor"></span>Automated Data Processing Application Coordinator (ADPAC)</td>
<td>The ADPAC is the person responsible for planning and implementing new work methods and technology for employees throughout a medical center. ADPACs train employees and assist users when they run into difficulties, and needs to know how all components of the system work. ADPACs maintain open communication with their supervisors and Service Chiefs, as well as their counterparts in Fiscal and Acquisitions and Materiel Management (A&amp;MM), or Information Resource Management (IRM).</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_AMIS" class="anchor"></span>Automated Management Information System (AMIS)</td>
<td>The VHA Decision Support System (DSS) is a national automated management information system based on commercial software to integrate data from clinical and financial systems for both inpatient and outpatient care. The commercial software is utilized with interfaces developed to transport data into the system from the <a href="#Glos_VistA">Veterans Health Information Systems and Technology Architecture</a> (VistA), the National Patient Care Database (NPCD), the Patient Treatment File (PTF), and various VA financial information systems. The VHA began implementation of DSS in 1994. Full implementation was completed in 1999 and DSS is now used throughout the VA healthcare system.</td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="2">to Glossary Contents</td>
</tr>
</tbody>
</table>

| Term or Acronym                            |                      | Description                                                                                                                                    |
|--------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="G_B" class="anchor"></span>B |                      |                                                                                                                                                |
| B-Type Option                              |                      | In [VistA](#Glos_VistA), an option designed to be run only by the [RPC Broker](#Glos_RPCBroker), and which cannot be run from the menu system. |
| [ BACK ](#glossary)                    | to Glossary Contents |                                                                                                                                                |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Term or Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><span id="G_C" class="anchor"></span><strong>C</strong></td>
</tr>
<tr class="even">
<td colspan="2">CCOW</td>
<td><em>See</em> <a href="#Glos_CCOW">Clinical Context Object Workgroup</a></td>
</tr>
<tr class="odd">
<td colspan="2">CCR</td>
<td><em>See</em> <a href="#Glos_CCR">Clinical Case Registries</a></td>
</tr>
<tr class="even">
<td colspan="2">CDC</td>
<td><em>See</em> <a href="#Glos_CDC">Centers for Disease Control and Prevention</a></td>
</tr>
<tr class="odd">
<td colspan="2">CDCO</td>
<td><em>See</em> <a href="#Glos_CDCO">Corporate Data Center Operations</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CDC" class="anchor"></span>Centers for Disease Control and Prevention (CDC)</td>
<td><p>The CDC is one of the major operating components of the United States Department of Health and Human Services. It includes a number of Coordinating Centers and Offices which specialize in various aspects of public health, as well as the National Institute for Occupational Safety and Health (NIOSH).</p>
<p><em>See</em> <a href="http://www.cdc.gov/about/organization/cio.htm">http://www.cdc.gov/about/organization/cio.htm</a></p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_CCR" class="anchor"></span>Clinical Case Registries (CCR)</td>
<td>The Clinical Case Registries <strong>(</strong>CCR) application collects data on the population of Veterans with certain clinical conditions, namely <a href="#Glos_HepatitisC">Hepatitis C</a> and <a href="#Glos_HIV">Human Immunodeficiency Virus</a> (HIV) infections.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CCOW" class="anchor"></span>Clinical Context Object Workgroup (CCOW)</td>
<td><p>CCOW is an <a href="#Glos_HL7">HL7</a> standard protocol designed to enable disparate applications to synchronize in real-time, and at the user-interface level. It is vendor independent and allows applications to present information at the desktop and/or portal level in a unified way.</p>
<p>CCOW is the primary standard protocol in healthcare to facilitate a process called "Context Management." Context Management is the process of using particular "subjects" of interest (e.g., user, patient, clinical encounter, charge item, etc.) to 'virtually' link disparate applications so that the end-user sees them operate in a unified, cohesive way.</p>
<p>Context Management can be utilized for both CCOW and non-CCOW compliant applications. The CCOW standard exists to facilitate a more robust, and near "plug-and-play" interoperability across disparate applications.</p>
<p>Context Management is often combined with <a href="#Glos_SingleSignOn">Single Sign On</a> applications in the healthcare environment, but the two are discrete functions. Single Sign On is the process that enables the secure access of disparate applications by a user through use of a single authenticated identifier and password.</p></td>
</tr>
<tr class="odd">
<td colspan="2">Comma-Delimited Values (CDV)</td>
<td><em>See</em> <a href="#Glos_CSV">Comma-Separated Values</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CSV" class="anchor"></span>Comma-Separated Values (CSV)</td>
<td>“Separated” or “delimited” data files use specific characters (delimiters) to separate its values. Most database and spreadsheet programs are able to read or save data in a delimited format. The comma-separated values file format is a delimited data format that has fields separated by the comma character and records separated by newlines. Excel can import such a file and create a spreadsheet from it.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_CPRS" class="anchor"></span>Computerized Patient Record System (CPRS)</td>
<td>A Computerized Patient Record (CPR) is a comprehensive database system used to store and access patients’ healthcare information. CPRS is the Department of Veteran’s Affairs electronic health record software. The CPRS organizes and presents all relevant data on a patient in a way that directly supports clinical decision making. This data includes medical history and conditions, problems and diagnoses, diagnostic and therapeutic procedures and interventions. Both a graphic user interface version and a character-based interface version are available. CPRS provides a single interface for health care providers to review and update a patient’s medical record, and to place orders, including medications, special procedures, x-rays, patient care nursing orders, diets, and laboratory tests. CPRS is flexible enough to be implemented in a wide variety of settings for a broad spectrum of health care workers, and provides a consistent, event-driven, Windows-style interface.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CSH" class="anchor"></span>context-sensitive help</td>
<td><p>Online help is topic-oriented, procedural or reference information delivered through computer software. It is a form of user assistance. Most online help is designed to give assistance in the use of a software application or operating system, but can also be used to present information on a broad range of subjects.</p>
<p>When a user presses the [F1] key while using the GUI application, the application automatically opens the online help file (which is distributed and installed alongside the application file itself).</p>
<p><strong>Context-sensitive help</strong> is a kind of online help that is obtained from a specific point in the state of the software, providing help for the situation that is associated with that state.</p>
<p>Context-sensitive help, as opposed to general online help or online manuals, doesn't need to be accessible for reading as a whole. Each topic is supposed to describe extensively one state, situation, or feature of the software.</p>
<p>Context-sensitive help can be implemented using <a href="http://en.wikipedia.org/wiki/Tooltip">tooltips</a>, which either provide a terse description of a <a href="http://en.wikipedia.org/wiki/GUI_widget">GUI widget</a> or display a complete topic from the help file. Other commonly used ways to access context-sensitive help start by clicking a button. One way uses a per widget button that displays the help immediately. Another way changes the <a href="http://en.wikipedia.org/wiki/Mouse_pointer">mouse pointer</a> shape to a question mark, and then, after the user clicks a widget, the help appears.</p>
<p>Context-sensitive help is most used in, but is not limited to, <a href="http://en.wikipedia.org/wiki/GUI">GUI</a> environments. Examples are <a href="http://en.wikipedia.org/wiki/Microsoft">Microsoft's</a> <a href="http://en.wikipedia.org/wiki/Windows_Help">WinHelp</a>, <a href="http://en.wikipedia.org/wiki/Sun_Microsystems">Sun's</a> <a href="http://en.wikipedia.org/wiki/JavaHelp">JavaHelp</a> or Panviva's <a href="http://www.supportpoint.com/">SupportPoint</a>.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_Contextor" class="anchor"></span><em>Contextor</em> software</td>
<td><p>Sentillion <em>Contextor</em> can be embedded within an application to implement most of <a href="#Glos_CCOW">CCOW</a>'s context participant behaviors. <em>Contextor</em> is compatible with any CCOW-compliant context manager and is designed to simplify writing applications that support the CCOW standard. It includes these development environment components:</p>
<ul>
<li><p>CCOW-compliant code samples of Windows and Web applications</p></li>
<li><p>Development-only version of Sentillion Context Manager</p></li>
<li><p>Development tools for simulating and observing the behavior of a context-enabled desktop</p></li>
<li><p>Configuration and administration tool</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CDCO" class="anchor"></span>Corporate Data Center Operations (CDCO)</td>
<td>Federal data center within the Department of Veterans Affairs (VA). As a franchise fund, or fee-for-service organization, CDCO-Austin provides cost-efficient IT enterprise solutions to support the information technology needs of customers within the Federal sector. <em>Formerly</em> the Austin Automation Center (AAC); <em>formerly</em> the Austin Information Technology Center (AITC).</td>
</tr>
<tr class="odd">
<td colspan="2">CPRS</td>
<td><em>See</em> <a href="#Glos_CPRS">Computerized Patient Record System</a></td>
</tr>
<tr class="even">
<td colspan="2">CPT</td>
<td><em>See</em> <a href="#Glos_CPT">Current Procedural Terminology</a></td>
</tr>
<tr class="odd">
<td colspan="2">CSV</td>
<td><em>See</em> <a href="#Glos_CSV">Comma-Separated Values</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_CPT" class="anchor"></span>Current Procedural Terminology (CPT)</td>
<td><p>CPT® is the most widely accepted medical nomenclature used to report medical procedures and services under public and private health insurance programs. CPT codes describe a procedure or service identified with a five-digit CPT code and descriptor nomenclature. The CPT code set accurately describes medical, surgical, and diagnostic services and is designed to communicate uniform information about medical services and procedures among physicians, coders, patients, accreditation organizations, and payers for administrative, financial, and analytical purposes. The current version is the CPT 2009.</p>
<p><em>Note:</em> CPT® is a registered trademark of the American Medical Association.</p></td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="2">to Glossary Contents</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>Term or Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><span id="G_D" class="anchor"></span><strong>D</strong></td>
</tr>
<tr class="even">
<td>DAA</td>
<td><em>See</em> <a href="#Glos_DAA">Direct Acting Antiviral</a></td>
</tr>
<tr class="odd">
<td><span id="Glos_DBIA" class="anchor"></span>Database Integration Agreement (DBIA)</td>
<td><strong>M</strong> code is not “compiled and linked,” so any code is open to anyone to call. The same is true for the data. This permits an incredible level of integration between applications, but it is “too open” for some software architects' liking. The VA has instituted Database Integration Agreements to enforce external policies and procedures to avoid unwanted dependencies.</td>
</tr>
<tr class="even">
<td><span id="Glos_DD" class="anchor"></span>Data Dictionary</td>
<td>A data structure that stores meta-data, i.e. data about data. The term “data dictionary” has several uses; most generally it is thought of as a set of data descriptions that can be shared by several applications. In practical terms, it usually means a table in a database that stores the names, field types, length, and other characteristics of the fields in the database tables.</td>
</tr>
<tr class="odd">
<td>DBIA</td>
<td><em>See</em> <a href="#Glos_DBIA">Database Integration Agreement</a></td>
</tr>
<tr class="even">
<td><span id="Glos_Delphi" class="anchor"></span>Delphi</td>
<td><p>Borland® Delphi® is a software development package that allows creation of applications which allow manipulation of live data from a database. Among other things, Delphi is an object-oriented, visual programming environment used to develop 32-bit applications for deployment in the Windows environment. This is the software that was used to produce the Query Tool application.</p>
<p><em>See also</em> <a href="http://www.borland.com/us/products/delphi/index.html"><span>http://www.embarcadero.com/products/delphi</span></a>.</p></td>
</tr>
<tr class="odd">
<td>DFN</td>
<td>File Number—the local/facility patient record number (patient file internal entry number)</td>
</tr>
<tr class="even">
<td><span id="Glos_DAA" class="anchor"></span>Direct Acting Antiviral (DAA)</td>
<td>A medication that interacts directly with viral proteins to inhibit viral replication.</td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td>to Glossary Contents</td>
</tr>
</tbody>
</table>

| Term or Acronym                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |     |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| <span id="G_E" class="anchor"></span>E                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |     |
| <span id="Glos_Epoetin" class="anchor"></span>Epoetin                       | Epoetin Alfa is used for treating anemia in certain patients with kidney failure, HIV, or cancer.                                                                                                                                                                                                                                                                                                                                                                                                |     |
| <span id="Glos_XML" class="anchor"></span>Extensible Mark-up Language (XML) | An initiative from the W3C defining an “extremely simple” dialect of [SGML](#Glos_SGML) suitable for use on the World-Wide Web.                                                                                                                                                                                                                                                                                                                                                                  |     |
| Extract Data Definition                                                     | A set of file and field numbers which identify the data that should be retrieved during the extraction process.                                                                                                                                                                                                                                                                                                                                                                                  |     |
| Extract Process                                                             | This process is run after the [update process](#Glos_UpdateProcess). This function goes through patients on the local registry and, depending on their status, extracts all available data for the patient since the last extract was run. This process also updates any demographic data held in the local registry for all existing patients that have changed since the last extract. The extract transmits any collected data for the patient to the national database via [HL7](#Glos_HL7). |     |
| [ BACK ](#glossary)                                                     | to Glossary Contents                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |     |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 1%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_F" class="anchor"></span><strong>F</strong></td>
</tr>
<tr class="even">
<td colspan="2">FDA</td>
<td colspan="3"><em>See</em> <strong>Food and Drug Administration</strong></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_FileMan" class="anchor"></span>FileMan</td>
<td colspan="3"><p>FileMan is a set of <a href="#Glos_M">M</a> utilities written in the late 1970s and early 1980s which allow the definition of data structures, menus and security, reports, and forms.</p>
<p>Its first use was in the development of medical applications for the Veterans Administration (now the Department of Veterans Affairs). Since it was a work created by the government, the source code cannot be copyrighted, placing that code in the public domain. For this reason, it has been used for rapid development of applications across a number of organizations, including commercial products.</p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_firewall" class="anchor"></span>firewall</td>
<td colspan="3">A firewall is a part of a computer system or network that is designed to block unauthorized access while permitting authorized communications. It is a device or set of devices configured to permit, deny, encrypt, decrypt, or proxy all (in and out) computer traffic between different security domains based upon a set of rules and other criteria.</td>
</tr>
<tr class="odd">
<td colspan="2">Food and Drug Administration (FDA)</td>
<td colspan="3">FDA is an agency of the United States Department of Health and Human Services and is responsible for regulating and supervising the safety of foods, dietary supplements, drugs, vaccines, biological medical products, blood products, medical devices, radiation-emitting devices, veterinary products, and cosmetics. The FDA also enforces section 361 of the Public Health Service Act and the associated regulations, including sanitation requirements on interstate travel as well as specific rules for control of disease on products ranging from pet turtles to semen donations for assisted reproductive medicine techniques.</td>
</tr>
<tr class="even">
<td colspan="2">Function key</td>
<td colspan="3">A key on a computer or terminal keyboard which can be programmed so as to cause an operating system command interpreter or application program to perform certain actions. On some keyboards/computers, function keys may have default actions, accessible on power-on. For example, <strong>&lt;F1&gt;</strong> is traditionally the function key used to activate a help system.</td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_G" class="anchor"></span><strong>G</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_Globals" class="anchor"></span>Globals</td>
<td colspan="3"><p><a href="#Glos_M">M</a> uses globals, variables which are intrinsically stored in files and persist beyond the program or process completion. Globals appear as normal variables with the caret character in front of the name. For example, the <strong>M</strong> statement…</p>
<p>SET ^A(“first_name”)=”Bob”</p>
<p>…will result in a new record being created and inserted in the file structure, persistent just as a file persists in an operating system. Globals are stored, naturally, in highly structured data files by the language and accessed only as <strong>M</strong> globals. Huge databases grow randomly rather than in a forced serial order, and the strength and efficiency of <strong>M</strong> is based on its ability to handle all this flawlessly and invisibly to the programmer.</p>
<p>For all of these reasons, one of the most common <strong>M</strong> programs is a database management system. <a href="#Glos_FileMan">FileMan</a> is one such example. <strong>M</strong> allows the programmer much wider control of the data; there is no requirement to fit the data into square boxes of rows and columns.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_GUI" class="anchor"></span>Graphical User Interface (GUI)</td>
<td colspan="3"><p>A graphical user interface (or GUI, often pronounced “gooey”) is a graphical (rather than purely textual) user interface to a computer. A GUI is a particular case of user interface for interacting with a computer which employs graphical images and widgets in addition to text to represent the information and actions available to the user. Usually the actions are performed through direct manipulation of the graphical elements. A GUI takes advantage of the computer’s graphics capabilities to make the program easier to use.</p>
<p><em>Sources:</em></p>
<p><a href="http://en.wikipedia.org/wiki/GUI">http://en.wikipedia.org/wiki/GUI</a></p>
<p><a href="http://www.webopedia.com/TERM/G/Graphical_User_Interface_GUI.html">http://www.webopedia.com/TERM/G/Graphical_User_Interface_GUI.html</a></p>
<p><em>See also</em> <a href="#Glos_UserInterface">User Interface</a></p></td>
</tr>
<tr class="even">
<td colspan="2">GUI</td>
<td colspan="3"><em>See:</em> <a href="#Glos_GUI">Graphical User Interface</a></td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th>Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_H" class="anchor"></span><strong>H</strong></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">HAART</td>
<td colspan="2"><em>See</em> <a href="#Glos_HAART">Highly Active Antiretroviral Treatment</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_HL7" class="anchor"></span>Health Level 7 (HL7)</td>
<td colspan="2"><p>One of several American National Standards Institute (ANSI)–accredited Standards Developing Organizations operating in the healthcare arena. "Level Seven" refers to the highest level of the International Standards Organization's (ISO) communications model for Open Systems Interconnection (OSI)— the application level. The application level addresses definition of the data to be exchanged, the timing of the interchange, and the communication of certain errors to the application. The seventh level supports such functions as security checks, participant identification, availability checks, exchange mechanism negotiations and, most importantly, data exchange structuring. HL7 focuses on the interface requirements of the entire health care organization. Source:</p>
<p>http://www.hl7.org/about/.</p></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_HEPC" class="anchor"></span>Hep C; HEPC</td>
<td colspan="2"><a href="#Glos_HepatitisC">Hepatitis C</a>; the <a href="#Glos_HEPC">Hepatitis C Registry</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_HepatitisC" class="anchor"></span>Hepatitis C</td>
<td colspan="2"><p>A liver disease caused by the hepatitis C virus (HCV). HCV infection sometimes results in an acute illness, but most often becomes a chronic condition that can lead to cirrhosis of the liver and liver cancer.</p>
<p><em>See</em> <a href="http://www.cdc.gov/hepatitis/index.htm">http://www.cdc.gov/hepatitis/index.htm</a></p></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_HAART" class="anchor"></span>Highly Active Antiretroviral Treatment (HAART)</td>
<td colspan="2">Antiretroviral drugs are medications for the treatment of infection by retroviruses, primarily <a href="#Glos_HIV">HIV</a>. When several such drugs, typically three or four, are taken in combination, the approach is known as highly active antiretroviral therapy, or HAART. The American National Institutes of Health and other organizations recommend offering antiretroviral treatment to all patients with <a href="#Glos_AIDS">AIDS</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">HIV</td>
<td colspan="2"><em>See</em> <a href="#Glos_HIV">Human Immunodeficiency Virus</a></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">HL7</td>
<td colspan="2"><em>See</em> <a href="#Glos_HL7">Health Level 7</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">HTML</td>
<td colspan="2"><em>See</em> <a href="#Glos_HTML">Hypertext Mark-up Language</a></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_HIV" class="anchor"></span>Human Immunodeficiency Virus (HIV)</td>
<td colspan="2"><p>HIV is a lentivirus (a member of the retrovirus family) that can lead to acquired immunodeficiency syndrome (<a href="#Glos_AIDS">AIDS</a>), a condition in humans in which the immune system begins to fail, leading to life-threatening opportunistic infections. HIV is different from most other viruses because it attacks the immune system. The immune system gives our bodies the ability to fight infections. HIV finds and destroys a type of white blood cell (T cells or CD4 cells) that the immune system must have to fight disease.</p>
<p>See <a href="http://www.cdc.gov/hiv/">http://www.cdc.gov/hiv/</a>.</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_hypertext" class="anchor"></span>hypertext</td>
<td colspan="2">A term coined around 1965 for a collection of documents (or "nodes") containing cross-references or "links" which, with the aid of an interactive browser program, allow the reader to move easily from one document to another.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_HTML" class="anchor"></span>Hypertext Mark-up Language (HTML)</td>
<td colspan="2">A <a href="#Glos_hypertext">hypertext</a> document format used on the World-Wide Web. HTML is built on top of <a href="#Glos_SGML">SGML</a>. "Tags" are embedded in the text. A tag consists of a "&lt;", a "directive" (in lower case), zero or more parameters and a "&gt;". Matched pairs of directives, like "&lt;title&gt;" and "&lt;/title&gt;" are used to delimit text which is to appear in a special place or style.</td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="4">to Glossary Contents</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_I" class="anchor"></span><strong>I</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_ICD9" class="anchor"></span>ICD-9</td>
<td colspan="3"><p><em>International Statistical Classification of Diseases and Related Health Problems</em>, ninth edition (commonly abbreviated as “ICD-9”) provides numeric codes to classify diseases and a wide variety of signs, symptoms, abnormal findings, complaints, social circumstances and external causes of injury or disease. Every health condition can be assigned to a unique category and given a code, up to six characters long. Such categories can include a set of similar diseases. The “-9” refers to the ninth edition of these codes; the tenth edition has been published, but is not in widespread use at this time.</p>
<p><em>See also</em> <a href="#Glos_CPT">Current Procedural Terminology</a></p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_ICD10" class="anchor"></span>ICD-10</td>
<td colspan="3"><p><em>International Statistical Classification of Diseases and Related Health Problems</em>, tenth edition (commonly abbreviated as “ICD-10”) consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.</p>
<p><em>See also</em> <a href="#Glos_CPT">Current Procedural Terminology</a></p></td>
</tr>
<tr class="even">
<td colspan="2">ICN</td>
<td colspan="3"><em>See</em> <a href="#Glos_ICN">Integration Control Number</a></td>
</tr>
<tr class="odd">
<td colspan="2">ICR</td>
<td colspan="3">See <a href="#Glos_ICN">Immunology Case Registry</a></td>
</tr>
<tr class="even">
<td colspan="2">IEN</td>
<td colspan="3"><em>See</em> <a href="#Glos_IEN">Internal Entry Number</a></td>
</tr>
<tr class="odd">
<td colspan="2">Immunology Case Registry (ICR)</td>
<td colspan="3">Former name for <a href="#Glos_CCR">Clinical Case Registries</a> HIV (CCR:HIV).</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_IRM" class="anchor"></span>Information Resources Management (IRM)</td>
<td colspan="3">The service which is involved in planning, budgeting, procurement and management-in-use of VA's information technology investments.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_ICN" class="anchor"></span>Integration Control Number</td>
<td colspan="3">The national VA patient record number.</td>
</tr>
<tr class="even">
<td colspan="2">Interface</td>
<td colspan="3">An interface defines the communication boundary between two entities, such as a piece of software, a hardware device, or a user.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_IEN" class="anchor"></span>Internal Entry Number (IEN)</td>
<td colspan="3">The number which uniquely identifies each item in the VistA database.</td>
</tr>
<tr class="even">
<td colspan="2">IRM</td>
<td colspan="3"><em>See</em> <a href="#Glos_IRM">Information Resources Management</a></td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

| Term or Acronym                                                          |                      |                                                                                                                                                                                                                                                                                                                     | Description |     |
|--------------------------------------------------------------------------|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|-----|
| J                                                                    |                      |                                                                                                                                                                                                                                                                                                                     |             |     |
| JAWS                                                                     |                      | *See* [Job Access with Speech](#Glos_JAWS)                                                                                                                                                                                                                                                                          |             |     |
| <span id="Glos_JAWS" class="anchor"></span>Job Access with Speech (JAWS) |                      | Acronym for *Job Access with Speech*. Refers to a software product for visually impaired users. The software is produced by the Blind and Low Vision Group of Freedom Scientific. See <http://en.wikipedia.org/wiki/JAWS_%28screen_reader%29> and <http://www.freedomscientific.com/fs_products/software_jaws.asp>. |             |     |
|                                                                          |                      |                                                                                                                                                                                                                                                                                                                     |             |     |
| [ BACK ](#glossary)                                                  | to Glossary Contents |                                                                                                                                                                                                                                                                                                                     |             |     |

| Term or Acronym                                 |                      |                                                                                 | Description |     |
|-------------------------------------------------|----------------------|---------------------------------------------------------------------------------|-------------|-----|
| <span id="G_K" class="anchor"></span>K      |                      |                                                                                 |             |     |
| !KEA                                            |                      | Terminal emulation software. No longer in use in VHA; replaced by *Reflection*. |             |     |
| <span id="Glos_Keys" class="anchor"></span>Keys |                      | *See* [Security Keys](#Glos_Keys)                                               |             |     |
| [ BACK ](#glossary)                         | to Glossary Contents |                                                                                 |             |     |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_L" class="anchor"></span><strong>L</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_LIM" class="anchor"></span>Laboratory Information Manager (LIM)</td>
<td colspan="3">Manager of the laboratory files in VistA. Additional duties include creation of new tests, interface set-up and maintenance of instruments, coordination with staff outside of lab to create quick orders, order sets and other <a href="#Glos_CPRS">Computerized Patient Record System</a> functions.</td>
</tr>
<tr class="odd">
<td colspan="2">Local Registry</td>
<td colspan="3">The local file of patients that were grandfathered into the registry or have passed the selection rules and been added to the registry.</td>
</tr>
<tr class="even">
<td colspan="2">Local Registry Update</td>
<td colspan="3">This process adds new patients (that have had data entered since the last update was run and pass the selection rules) to the local registry.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_LOINC" class="anchor"></span>Logical Observation Identifiers Names and Codes (LOINC)</td>
<td colspan="3"><p>LOINC<sup>©</sup> is designed to facilitate the exchange and pooling of clinical results for clinical care, outcomes management, and research by providing a set of universal codes and names to identify laboratory and other clinical observations. The Regenstrief Institute, Inc., an internationally renowned healthcare and informatics research organization, maintains the LOINC database and supporting documentation.</p>
<p><em>See</em> <a href="http://loinc.org/">http://loinc.org/</a></p></td>
</tr>
<tr class="even">
<td colspan="2">LOINC</td>
<td colspan="3"><em>See</em> <a href="#Glos_LOINC">Logical Observation Identifiers Names and Codes</a></td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_M" class="anchor"></span><strong>M</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_M" class="anchor"></span>M</td>
<td colspan="3"><p><strong>M</strong> is a procedural, interpreted, multi-user, general-purpose programming language designed to build and control massive databases. It provides a simple abstraction that all data values are strings of characters, and that all data can be structured as multiple dimensional arrays. MUMPS data structures are sparse, using strings of characters as subscripts.</p>
<p><strong>M</strong> was formerly (and is still commonly) called MUMPS, for <em>Massachusetts General Hospital Utility Multiprogramming System</em>.</p></td>
</tr>
<tr class="odd">
<td colspan="2">Massachusetts General Hospital Utility Multi-Programming System</td>
<td colspan="3"><em>See</em> <a href="#Glos_M">M</a><strong>.</strong></td>
</tr>
<tr class="even">
<td colspan="2">MDI</td>
<td colspan="3"><em>See</em> <a href="#Glos_MDI">Multiple Document Interface</a></td>
</tr>
<tr class="odd">
<td colspan="2">Medical SAS Datasets</td>
<td colspan="3">The VHA Medical SAS Datasets are national administrative data for VHA-provided health care utilized primarily by Veterans, but also by some non-Veterans (e.g., employees, research participants).</td>
</tr>
<tr class="even">
<td colspan="2">Message (HL7)</td>
<td colspan="3"><p>A <em>message</em> is the atomic unit of data transferred between systems. It is comprised of a group of segments in a defined sequence. Each message has a message type that defines its purpose. For example, the ADT (admissions/discharge/transfer) Message type is used to transmit portions of a patient’s ADT data from one system to another. A three character code contained within each message identifies its type.</p>
<p><em>Source:</em> Health Level Seven, Health Level Seven, Version 2.3.1, copyright 1999, p. E-18., quoted in <strong>See CCR Redacted document</strong>.</p></td>
</tr>
<tr class="odd">
<td colspan="2">Middleware</td>
<td colspan="3">In computing, middleware consists of software agents acting as an intermediary between different application components. It is used most often to support complex, distributed applications. The software agents involved may be one or many.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_MDI" class="anchor"></span>Multiple Document Interface (MDI)</td>
<td colspan="3"><p>MDI is a Windows function that allows an application to display and lets the user work with more than one document at the same time. This interface improves user performance by allowing them to see data coming from different documents, quickly copy data from one document to another and many other functions.</p>
<p>These files have the .MDI filename extension.</p></td>
</tr>
<tr class="odd">
<td colspan="2">MUMPS</td>
<td colspan="3"><em>See</em> <a href="#Glos_M">M</a></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2">Term or Acronym</th>
<th colspan="2">Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_N" class="anchor"></span><strong>N</strong></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3">Namespace</td>
<td>A logical partition on a physical device that contains all the artifacts for a complete <a href="#Glos_M">M</a> system, including <a href="#Glos_Globals">globals</a>, <a href="#Glos_Routine">routines</a>, and libraries. Each namespace is unique, but data can be shared between namespaces with proper addressing within the routines. In VistA, namespaces are usually dedicated to a particular function. The <strong>ROR</strong> namespace, for example, is designed for use by <a href="#Glos_CCR">CCR</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">National Case Registry (NCR)</td>
<td>All sites running the CCR software transmit their data to the central database for the registry.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="3">National Patient Care Database (NPCD)</td>
<td><p>The NPCD is the source data for the VHA Medical SAS Datasets. NPCD is the VHA's centralized relational database (a data warehouse) that receives encounter data from VHA clinical information systems. It is updated daily.</p>
<p>NPCD records include updated patient demographic information, the date and time of service, the practitioner(s) who provided the service, the location where the service was provided, diagnoses, and procedures. NPCD also holds information about patients' assigned Primary Care Provider and some patient status information such as exposure to Agent Orange, Ionizing Radiation or Environmental Contaminants, Military Sexual Trauma, and Global Assessment of Functioning.</p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">NPCD</td>
<td><em>See</em> <a href="#Glos_NPCD">National Patient Care Database</a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="4">to Glossary Contents</td>
</tr>
</tbody>
</table>

| Term or Acronym                            |                      | Description |                            |     |
|--------------------------------------------|----------------------|-------------|----------------------------|-----|
| <span id="G_O" class="anchor"></span>O |                      |             |                            |     |
| OEF                                        |                      |             | Operation Enduring Freedom |     |
| OIF                                        |                      |             | Operation Iraqi Freedom    |     |
| OND                                        |                      |             | Operation New Dawn         |     |
| [ BACK ](#glossary)                    | to Glossary Contents |             |                            |     |

| Term or Acronym                                                   |                      |                                                                                                                                                                                                                                                                                                                                                                        | Description |
|-------------------------------------------------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| <span id="G_P" class="anchor"></span>P                        |                      |                                                                                                                                                                                                                                                                                                                                                                        |             |
| <span id="Glos_Peginterferon" class="anchor"></span>peginterferon |                      | Peginterferon alfa-2b is made from human proteins that help the body fight viral infections. Peginterferon alfa-2b is used to treat chronic hepatitis C in adults, often in combination with another medication called [ribavirin](#Glos_Ribavirin).                                                                                                                   |             |
| protocol                                                          |                      | A protocol is a convention or standard that controls or enables the connection, communication, and data transfer between two computing endpoints. In its simplest form, a protocol can be defined as the rules governing the syntax, semantics, and synchronization of communication. Protocols may be implemented by hardware, software, or a combination of the two. |             |
| [ BACK ](#glossary)                                           | to Glossary Contents |                                                                                                                                                                                                                                                                                                                                                                        |             |

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th>Description</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><span id="G_R" class="anchor"></span><strong>R</strong></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Reflection</td>
<td colspan="2"><strong>Terminal emulation software</strong> used to connect personal computers to mainframe servers made by IBM, Hewlett Packard and other manufacturers running UNIX, VMS and other operating systems.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Registry</td>
<td colspan="2">The VHA Registries Program supports the population-specific data needs of the enterprise including (but not limited to) the <a href="#Glos_CCR">Clinical Case Registries</a>, Oncology Tumor Registry, Traumatic Brain Injury Registry, Embedded Fragment Registry and Eye Trauma Registry.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Registry Medication</td>
<td colspan="2">A defined list of medications used for a particular registry.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_RPC" class="anchor"></span>Remote Procedure Call (RPC)</td>
<td colspan="2"><p>A type of protocol that allows one program to request a service from a program located on another computer network. Using RPC, a system developer need not develop specific procedures for the server. The client program sends a message to the server with appropriate arguments and the server returns a message containing the results of the program executed. In this case, the GUI client uses an RPC to log the user on to <strong>VistA</strong>. And to call up, and make changes to, data that resides on a <strong>VistA</strong> server.</p>
<p><em>See also</em> <a href="#Glos_RPCBroker">Remote Procedure Call (RPC) Broker</a></p></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_RPCBroker" class="anchor"></span>Remote Procedure Call (RPC) Broker</td>
<td colspan="2"><p>A piece of middleware software that allows programmers to make program calls from one computer to another, via a network. The RPC Broker establishes a common and consistent foundation for client/server applications being written under the VistA umbrella. The RPC Broker acts as a bridge connecting the client application front-end on the workstation (in this case, the Delphi Query Tool application) to the M –based data and business rules on the server. It serves as the communications medium for messaging between VistA client/server applications. Upon receipt, the message is decoded, the requested remote procedure call is activated, and the results are returned to the calling application. Thus, the RPC Broker helps bridge the gap between the traditionally proprietary VA software and other types of software.</p>
<p><em>See also</em> <a href="#Glos_RPC">Remote Procedure Call (RPC)</a></p></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_retrovirus" class="anchor"></span>Retrovirus</td>
<td colspan="2">Any of a family of single-stranded RNA viruses having a helical envelope and containing an enzyme that allows for a reversal of genetic transcription, from RNA to DNA rather than the usual DNA to RNA, the newly transcribed viral DNA being incorporated into the host cell's DNA strand for the production of new RNA retroviruses: the family includes the AIDS virus and certain oncogene-carrying viruses implicated in various cancers.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_Ribavirin" class="anchor"></span>ribavirin</td>
<td colspan="2">Ribavirin is an antiviral medication. Ribavirin must be used together with an interferon alfa product (such as <a href="#Glos_Peginterferon">Peginterferon</a>)to treat chronic hepatitis C.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Roll-and-scroll, roll’n’scroll</td>
<td colspan="2">“Scrolling” is a display framing technique that allows the user to view a display as moving behind a fixed frame. The scrolling action typically causes the data displayed at one end of the screen to move across it, toward the opposite end. When the data reach the opposite edge of the screen they are removed (i.e., scroll off of the screen). Thus, old data are removed from one end while new data are added at the other. This creates the impression of the display page being on an unwinding scroll, with only a limited portion being visible at any time from the screen; i.e., the display screen is perceived as being stationary while the displayed material moves (scrolls) behind it. Displays may be scrolled in the top-bottom direction, the left-right direction, or both. Traditionally, VistA data displays have been referred to as “roll-and-scroll” for this reason.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">ROR</td>
<td colspan="2">The ROR <a href="#Glos_Namespace">namespace</a> in <a href="#Glos_M">M</a>, used for the CCR application and related <strong>VistA</strong> data files.</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_Routine" class="anchor"></span>Routine</td>
<td colspan="2">A set of programming instructions designed to perform a specific limited task.</td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">RPC</td>
<td colspan="2"><em>See</em> <a href="#Glos_RPC">Remote Procedure Call (RPC)</a></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">RPC Broker</td>
<td colspan="2"><em>See</em> <a href="#Glos_RPCBroker">Remote Procedure Call Broker</a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="4">to Glossary Contents</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_S" class="anchor"></span><strong>S</strong></td>
</tr>
<tr class="even">
<td colspan="2">screen reader</td>
<td colspan="3"><p>“Screen reader” software is designed to make personal computers using Microsoft Windows® accessible to blind and visually impaired users. It accomplishes this by providing the user with access to the information displayed on the screen via text-to-speech or by means of braille display and allows for comprehensive keyboard interaction with the computer.</p>
<p>It also allows users to create custom scripts using the JAWS Scripting Language, which can alter the amount and type of information which is presented by applications, and ultimately makes programs that were not designed for accessibility (such as programs that do not use standard Windows controls) usable through JAWS.</p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_508" class="anchor"></span>Section 508</td>
<td colspan="3"><p>Section 508 of the Rehabilitation Act as amended, <a href="http://frwebgate.access.gpo.gov/cgi-bin/getdoc.cgi?dbname=browse_usc&amp;docid=Cite:+29USC794d">29 U.S.C. Section 794(d)</a>, requires that when Federal agencies develop, procure, maintain, or use electronic and information technology, they shall ensure that this technology is accessible to people with disabilities. Agencies must ensure that this technology is accessible to employees and members of the public with disabilities to the extent it does not pose an “undue burden.” Section 508 speaks to various means for disseminating information, including computers, software, and electronic office equipment.</p>
<p>The Clinical Case Registry must be 508 compliant, able to extract data as needed including <a href="#Glos_SNOMED">SNOMED</a> codes.</p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SecurityKeys" class="anchor"></span>Security Keys</td>
<td colspan="3">Codes which define the characteristic(s), authorization(s), or privilege(s) of a specific user or a defined group of users. The VistA option file refers to the security key as a “lock.” Only those individuals assigned that “lock” can used a particular VistA option or perform a specific task that is associated with that security key/lock.</td>
</tr>
<tr class="odd">
<td colspan="2">Selection Rules</td>
<td colspan="3">A pre-defined set of rules that define a registry patient.</td>
</tr>
<tr class="even">
<td colspan="2">Sensitive Information</td>
<td colspan="3">Any information which requires a degree of protection and which should be made available only to authorized system users.</td>
</tr>
<tr class="odd">
<td colspan="2">Server</td>
<td colspan="3">In information technology, a server is a computer system that provides services to other computing systems—called clients—over a network. The server is where VistA M-based data and Business Rules reside, making these resources available to the requesting server.</td>
</tr>
<tr class="even">
<td colspan="2">SGML</td>
<td colspan="3"><em>See</em> <a href="#Glos_SGML">Standardized Generic Markup Language</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_SingleSignOn" class="anchor"></span>Single Sign On</td>
<td colspan="3">Single Sign On is the process that enables the secure access of disparate applications by a user through use of a single authenticated identifier and password.</td>
</tr>
<tr class="even">
<td colspan="2">Site Configurable</td>
<td colspan="3">A term used to refer to features in the system that can be modified to meet the needs of each local site.</td>
</tr>
<tr class="odd">
<td colspan="2">SNOMED</td>
<td colspan="3"><em>See</em> <a href="#Glos_SNOMED">Systematized Nomenclature of Medicine</a></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_SGML" class="anchor"></span>Standardized Generic Markup Language (SGML)</td>
<td colspan="3">A generic markup language for representing documents. SGML is an International Standard that describes the relationship between a document’s content and its structure. SGML allows document-based information to be shared and re-used across applications and computer platforms in an open, vendor-neutral format.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_SNOMED" class="anchor"></span>Systematized Nomenclature of Medicine (SNOMED)</td>
<td colspan="3">SNOMED is a terminology that originated as the systematized nomenclature of pathology (SNOP) in the early 1960s under the guidance of the College of American Pathologists. In the late 1970s, the concept was expanded to include most medical domains and renamed SNOMED. The core content includes text files such as the concepts, descriptions, relationships, ICD mappings, and history tables. SNOMED represents a terminological resource that can be implemented in software applications to represent clinically relevant information comprehensive (&gt;350,000 concepts) multi-disciplinary coverage but discipline neutral structured to support data entry, retrieval, maps etc.</td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_T" class="anchor"></span><strong>T</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_TSPR" class="anchor"></span>Technical Services Project Repository (TSPR)</td>
<td colspan="3"><p>The TSPR is the central data repository and database for VA Health IT (VHIT) project information.</p>
<p><strong>See CCR Redacted document</strong>.</p></td>
</tr>
<tr class="odd">
<td colspan="2">Terminal emulation software</td>
<td colspan="3">A program that allows a personal computer (PC) to act like a (particular brand of) terminal. The PC thus appears as a terminal to the host computer and accepts the same escape sequences for functions such as cursor positioning and clearing the screen. Attachmate <em>Reflection</em> is widely used in VHA for this purpose.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_ToolTips" class="anchor"></span>Tool tips</td>
<td colspan="3">Tool tips are “hints” assigned to menu items which appear when the user “hovers” the mouse pointer over a menu.</td>
</tr>
<tr class="odd">
<td colspan="2">TSPR</td>
<td colspan="3"><em>See</em> <a href="#Glos_TSPR">Technical Services Project Repository</a></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 78%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_U" class="anchor"></span><strong>U</strong></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_UserInterface" class="anchor"></span>User Interface</td>
<td colspan="3"><p>A user interface is the means by which people (the users) interact with a particular machine, device, computer program or other complex tool (the system). The user interface provides one or more means of:</p>
<p>• Input, which allows the users to manipulate the system</p>
<p>• Output, which allows the system to produce the effects of the users’ manipulation</p>
<p>The interface may be based strictly on text (as in the traditional “roll and scroll” IFCAP interface), or on both text and graphics.</p>
<p>In computer science and human-computer interaction, the user interface (of a computer program) refers to the graphical, textual and auditory information the program presents to the user, and the control sequences (such as keystrokes with the computer keyboard and movements of the computer mouse) the user employs to control the program.</p>
<p><em>See also</em> <a href="#Glos_GUI">Graphical User Interface</a></p></td>
</tr>
<tr class="odd">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 0%" />
<col style="width: 79%" />
<col style="width: 0%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Term or Acronym</th>
<th colspan="2">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><span id="G_V" class="anchor"></span><strong>V</strong></td>
</tr>
<tr class="even">
<td colspan="2">VERA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VERA">Veterans Equitable Resource Allocation</a></td>
</tr>
<tr class="odd">
<td colspan="2">Vergence</td>
<td colspan="3"><em>Vergence</em>® software from Sentillion provides a single, secure, efficient and safe point of access throughout the healthcare enterprise, for all types of caregivers and applications. <em>Vergence</em> unifies single sign-on, role-based application access, context management, strong authentication and centralized auditing capabilities into one fully integrated, out-of-the box clinical workstation solution.</td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_VerifyCode" class="anchor"></span>Verify Code</td>
<td colspan="3"><p>With each sign-on to VistA, the user must enter two codes to be recognized and allowed to proceed: the <em>Access Code</em> and <em>Verify Code</em>. Like the Access Code, the Verify Code is also generally assigned by IRM Service and is also encrypted. This code is used by the computer to verify that the person entering the access code can also enter a second code correctly. Thus, this code is used to determine if users can verify who they are.</p>
<p><em>See also</em> <a href="#Glos_AccessCode">Access Code</a></p></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VERA" class="anchor"></span>Veterans Equitable Resource Allocation (VERA)</td>
<td colspan="3"><p>Since 1997, the VERA System has served as the basis for allocating the congressionally appropriated medical care budget of the Department of Veterans Affairs (VA) to its regional networks. A 2001 study by the RAND Corporation showed that “[in] spite of its possible shortcomings, VERA appeared to be designed to meet its objectives more closely than did previous VA budget allocation systems.”</p>
<p><em>See</em> <a href="http://www.rand.org/pubs/monograph_reports/MR1419/">http://www.rand.org/pubs/monograph_reports/MR1419/</a></p></td>
</tr>
<tr class="even">
<td colspan="2"><span id="Glos_VistA" class="anchor"></span>Veterans Health Information Systems and Technology Architecture (VistA)</td>
<td colspan="3">VistA is a comprehensive, integrated health care information system composed of numerous software modules.</td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VHA" class="anchor"></span>Veterans Health Administration (VHA)</td>
<td colspan="3">VHA administers the United States Veterans Healthcare System, whose mission is to serve the needs of America’s Veterans by providing primary care, specialized care, and related medical and social support services.</td>
</tr>
<tr class="even">
<td colspan="2">VHA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VHA">Veterans Health Administration</a></td>
</tr>
<tr class="odd">
<td colspan="2"><span id="Glos_VISN" class="anchor"></span>Veterans Integrated Service Network (VISN)</td>
<td colspan="3"><a href="#Glos_VHA">VHA</a> organizes its local facilities into networks called VISNS (VA Integrated Service Networks). At the VISN level, VistA data from multiple local facilities may be combined into a data warehouse.</td>
</tr>
<tr class="even">
<td colspan="2">VISN</td>
<td colspan="3"><em>See</em> <a href="#Glos_VISN">Veterans Integrated Service Network</a></td>
</tr>
<tr class="odd">
<td colspan="2">VistA</td>
<td colspan="3"><em>See</em> <a href="#Glos_VistA">Veterans Health Information Systems and Technology Architecture</a></td>
</tr>
<tr class="even">
<td><a href="#glossary"> <strong>BACK</strong> </a></td>
<td colspan="3">to Glossary Contents</td>
<td></td>
</tr>
</tbody>
</table>

| Term or Acronym                            |                      |                                                | Description |
|--------------------------------------------|----------------------|------------------------------------------------|-------------|
| <span id="G_X" class="anchor"></span>X |                      |                                                |             |
| XML                                        |                      | *See* [Extensible Mark-up Language](#Glos_XML) |             |
| [ BACK ](#glossary)                    | to Glossary Contents |                                                |             |

########### Index

A

Access rights. *See* Security Keys

Activity Detail

view in Technical Log, 160

Activity log

window, 158

Add

a CDC report, 175

a Pending patient to registry, 97

lab tests to Registry, 119

Local Fields, 126

medications to Registry, 122

notifications, 124

ADMIN security key, 89

Adult HIV/AIDS Confidential Case Report, 175

AIDS-OI

Clinical Status, 171, 185

application shortcut

target field, 289

B

Break the Clinical Link, 107

Broker Timeout settings, 135

C

CCOW

break the clinical link, 107

check status, 117

rejoin the clinical context, 106

CCR

access rights, 89

downloading software, 77

features of, 5

identify patients, 97

intranet Home Page, 79

overview of, 5, 294

recommended users of, 1

run a report, 194

sign on, 99

CDC Form

Section VIII, 185

CDC report

about the, 174

Print, 177

Update, 178

View, 177

Change

report output appearance, 150

screen colors, 90

system settings, 133

Clinic Follow-Up report, 201

Clinical Status

AIDS-OI, 171

Combined Meds and Labs report, 202

command line switches, 289

Confirm/Edit

menu option, 107

context management

disable, 290

Copy

text from a report, 148

Current Inpatient List report, 203

D

Data Quality message, 157

Database Error, 157

Deceased check, 97

Delete

report from the Task Manager, 155

Diagnoses report, 205

disable

single sign-on, 290

Documentation

in VistA Document Library, 79

Download CCR software, 77

E

Edit Site Parameters. *See* Site Parameters

Error messages, 157

F

Features of CCR, 294

File Menu options, 103

G

General Utilization and Demographics report, 205

GUI

parts of the screen, 81

right-click menu options, 86

H

HCCR. *See* CCR:HEPC

Help menu options, 115

Hepatitis C Registry. See CCR:HEPC

HIV Registry. See CCR:HIV

I

ICD-9 codes

used to identify registry patients, 97

ICR. *See* CCR:HIV, *See* CCR:HIV

Inpatient Utilization report, 209

IRM

security key, 89

L

Lab Tests

add to Registry, 119

Registry report, by range, 218

remove from Registry, 121

Lab Utilization report, 209

List of Registry Patients report, 210

Local Fields

add, 126

reactivate, 132

remove, 130

Login. *See* Sign on to CCR

M

Medications

add to Registry, 122

Registry report, 219, 220

remove from Registry, 124

Menu

File, 103

Help, 115

Registry, 107

Reports, 112

Window, 114

message

Data Quality, 157

Database Error, 157

Error, 157

Warning, 157

N

nonstandard port number, 290

Notifications

add, 124

list of users receiving, 126

remove, 126

O

Outpatient Utilization report, 212

P

Parts of the screen, 82

Patient

deceased, 97

delete a, 174

edit a, 170

identify a Pending, 97

list of all in registry, 210

list of all inpatients, 203

Medication History report, 213

update a CDC Report, 178

Patient Data Editor

window, 168

Patient List Display

Selected column, 166

Selection Rule column, 166

Pending

add patient to registry, 97

Pharmacy Prescription Utilization report, 214

port number

nonstandard, 290

Preferences, setting, 133

Print

report output, 154

R

Registry Coordinator, 111

Registry Lab Tests report, 218

Registry Medications

add, 122

remove, 124

Registry Medications report, 219, 220

Registry Menu options, 107

registry name, 290

Rejoin Clinical Context, 106

Report

change sort order in the output, 150

Clinic Follow-up, 201

Combined Meds & Labs, 202

copy results to another application, 148

create a, 194

Current Inpatient List, 203

delete from Task Manager list, 155

Diagnoses, 205

General Utilization and Demographics, 205

Inpatient Utilization, 209

Lab Utilization, 209

List of Registry Patients, 210

Outpatient Utilization, 212

Pharmacy Prescription Utilization, 214

print a, 154

Registry Lab Tests, 218

Registry Medications, 219, 220

VERA Reimbursement, 223

view from Task Manager screen, 146

Report parameters

Mode field, 193

Reports menu options, 112

Right-Click menus, 87

S

Save

report output to a file, 151

search parameters as a template, 193

Search

for a patient, 166

for text in a report, 150

ARV drugs, 124

Select a Registry. *See* Sign on to CCR

server

host name, 290

IP address, 290

Setting Preferences, 133

shortcut

target field, 289

Show Registry Users, 108

Sign on to CCR, 99

single sign-on

disable, 290

Site Parameters

add Lab Tests, 119

add Local Fields, 126

add Notifications, 124

add Registry Medications, 122

menu option, 109

Start. *See* Sign on to CCR

switches

command line, 289

System Profile. See Site Parameters

System Settings. *See* Preferences

T

target field, 289

Task Manager

delete a report, 155

view a report, 146

Technical Log

Activity types, 157

tab view, 146, 156

view activity detail, 158

U

Update

CDC Report, 178

user context

disable, 290

USER security key, 89

Utilization Reports

General and Demographics, 205

Inpatient, 209

Lab, 209

Outpatient, 212

Pharmacy Prescription, 214

V

VERA Reimbursement report, 223

View

reports from the Task Manager, 146

Technical Log, 156

W

Warning message, 157

Window

about the CCR GUI, 82

Patient Data Editor, 168

Window menu options, 114

Windows

about right-click menus, 86

ENDNOTES

Begin on next page

###########  Endnotes

########### 

[^1]: CDCO was formerly known as the Austin Automation Center (AAC). CDCO is managed by the VHA Center for Quality Management in Public Health (CQMPH).

[^2]: added accessibility information for Section 508 compliance.

[^3]: updated the set of valid patient search parameters to use \# followed by the patient’s 11-digit coded SSN.

[^4]: added Selected and Selection Rule as columns on the list of Patients.

[^5]: Patch ROR\*1.5\*10 September 2010 removed the Date of Death and Sex columns on the list of Patients.

[^6]: added descriptions for Selected and Selection Rule columns.

[^7]: updated the set of valid patient search parameters to use \# followed by the patient’s 11-digit coded SSN.

[^8]: added a note to indicate that the AIDS-OI checkbox and its date field are automatically populated when an indicator disease Def box is selected in Section VIII of the CDC form in the Clinical Status section.

[^9]: added a note to indicate that when an indicator disease Def box is selected, the AIDS-OI checkbox and the date field are automatically populated on the Patient Data Editor in the Clinical Status tab of the Registry tab.

[^10]: changed checkboxes to modes in the heading.

[^11]: added “exclude” to the sentence in Other Registries modes.

[^12]: added a description for the new button on each Report setup–Default Parameters.

[^13]: added information about the new functionality of the modified Patient Medication History report.

[^14]: updated this step to reflect the addition of the Mode field to Other Registries.

[^15]: updated this step to reflect the addition of the Mode field to Local Fields.

[^16]: added this step to reflect the addition of the Patients checkboxes.

[^17]: added this step to reflect the addition of the Inpatient/Outpatient checkboxes.

[^18]: Document revision for Patch ROR\*1.5\*10, July 2010, added/expanded many definitions and much explanatory material.