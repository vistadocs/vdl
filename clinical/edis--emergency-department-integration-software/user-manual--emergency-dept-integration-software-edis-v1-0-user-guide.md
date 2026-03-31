---
title: Emergency Dept Integration Software (EDIS) Version 1.0 User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: 
app_code: EDIS
app_name: Emergency Department Integration Software
section: CLI
app_status: archive
pkg_ns: EDIS
patch_ver: 1.0
patch_id: EDIS*1.0
group_key: "EDIS:EDIS:1.0"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Revision History](#revision-history) - [Emergency Department Integration Software](#emergency-department-integration-software) - [About this Guide](#about-this-guide) - [Section 508 of the Rehabilitation Act of 1973](#section-508-of-the-rehabilitation-act-of-1973) - [Recommendations for JAWS User
audience: 
keywords: 
  - patient
  - edis
  - patients
  - table
  - contents
  - locate
  - keyboard
  - emergency
  - board
  - arrow
page_count: 0
word_count: 26516
section_count: 41
table_count: 9
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edp_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Emergency_Dept_Integration_Software_Archive/edp_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=358"
---

![](emergency-dept-integration-software-edis-version-1-0-user-guide/001.png)

Emergency Department Integration Software

User Guide

September 2010

![](emergency-dept-integration-software-edis-version-1-0-user-guide/002.png)

Health Systems Design and Development

VA Health Information Technology

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Emergency Department Integration Software](#emergency-department-integration-software)
  - [About this Guide](#about-this-guide)
  - [Section 508 of the Rehabilitation Act of 1973](#section-508-of-the-rehabilitation-act-of-1973)
    - [Recommendations for JAWS Users](#recommendations-for-jaws-users)
  - [Role-based Access to Views](#role-based-access-to-views)
  - [Document Conventions](#document-conventions)
  - [Workstation Requirements](#workstation-requirements)
    - [Flash Player: Minimum Requirements for Microsoft Windows](#flash-player-minimum-requirements-for-microsoft-windows)
    - [Flash Player: Minimum Requirements for Apple Mac OS](#flash-player-minimum-requirements-for-apple-mac-os)
    - [JAWS Workstation Requirements](#jaws-workstation-requirements)
  - [Application Timeouts](#application-timeouts)
  - [Preventing Accidental Application Sign-Outs](#preventing-accidental-application-sign-outs)
- [Getting Started](#getting-started)
  - [Launch EDIS](#launch-edis)
  - [Log In](#log-in)
    - [Changing Your Verify Code](#changing-your-verify-code)
  - [EDIS Views](#edis-views)
    - [Select a View](#select-a-view)
  - [Work with Data Grids](#work-with-data-grids)
    - [Arrange Columns](#arrange-columns)
    - [Resize Columns](#resize-columns)
    - [Sort Information within Columns](#sort-information-within-columns)
  - [Access Help Files](#access-help-files)
  - [Understanding EDIS and CPRS Interactions](#understanding-edis-and-cprs-interactions)
  - [Using EDIS with Appointment Management](#using-edis-with-appointment-management)
    - [Benefits of this Method](#benefits-of-this-method)
    - [Drawbacks of this Method](#drawbacks-of-this-method)
    - [Best Practice for Using EDIS with Appointment Management](#best-practice-for-using-edis-with-appointment-management)
    - [Processes with Unscheduled Appointments (in Appointment Management) that Lead to Errors](#processes-with-unscheduled-appointments-in-appointment-management-that-lead-to-errors)
  - [Using EDIS with PCE](#using-edis-with-pce)
    - [Benefits of this Method](#benefits-of-this-method-1)
    - [Drawbacks of this Method](#drawbacks-of-this-method-1)
    - [Best Practice for Using EDIS with PCE](#best-practice-for-using-edis-with-pce)
    - [Why this Is Best Practice](#why-this-is-best-practice)
    - [Processes with PCE that Lead to Errors](#processes-with-pce-that-lead-to-errors)
- [Notifications](#notifications)
  - [Patient-Selection Messages](#patient-selection-messages)
- [Sign In View](#sign-in-view)
  - [Add Patients to EDIS from the Sign In View](#add-patients-to-edis-from-the-sign-in-view)
    - [Adding Patients Using the Search for Patient in VistA Selection](#adding-patients-using-the-search-for-patient-in-vista-selection)
    - [Adding Patients Using the Enter Name Selection](#adding-patients-using-the-enter-name-selection)
    - [Adding Patients Using the Ambulance Is Arriving Selection](#adding-patients-using-the-ambulance-is-arriving-selection)
    - [Add Information to the Patient Information Pane](#add-information-to-the-patient-information-pane)
    - [Definitions for Nationally Released Source Selections](#definitions-for-nationally-released-source-selections)
- [Identify Patients](#identify-patients)
  - [Identifying Patients](#identifying-patients)
- [Triage View](#triage-view)
  - [Add Patients to EDIS from the Triage View](#add-patients-to-edis-from-the-triage-view)
    - [Adding Patients Using the Search for Patient in VistA Selection](#adding-patients-using-the-search-for-patient-in-vista-selection-1)
    - [Adding Patients Using the Enter Name Selection](#adding-patients-using-the-enter-name-selection-1)
    - [Adding Patients Using the Ambulance Is Arriving Selection](#adding-patients-using-the-ambulance-is-arriving-selection-1)
  - [Add Triage Information](#add-triage-information)
    - [Definitions for Status Selections](#definitions-for-status-selections)
  - [Create a Visit in CPRS](#create-a-visit-in-cprs)
- [Update View](#update-view)
  - [Add or Update Information in the Patient Information Pane](#add-or-update-information-in-the-patient-information-pane)
  - [Create a Visit](#create-a-visit)
    - [Setting a Primary Provider for Your Patient’s Visit](#setting-a-primary-provider-for-your-patients-visit)
- [Disposition View](#disposition-view)
  - [Select a Disposition](#select-a-disposition)
    - [Definitions for National Dispositions](#definitions-for-national-dispositions)
  - [Select a Reason for Delay](#select-a-reason-for-delay)
    - [Definitions for National Reason-for-Delay Selections](#definitions-for-national-reason-for-delay-selections)
  - [Enter ICD-9-CM Diagnoses](#enter-icd-9-cm-diagnoses)
  - [Enter Free-Text Diagnoses](#enter-free-text-diagnoses)
  - [Remove Patients](#remove-patients)
  - [Remove Patients Entered in Error](#remove-patients-entered-in-error)
- [Edit Closed View](#edit-closed-view)
- [Display Board View](#display-board-view)
  - [Viewing the Display Board](#viewing-the-display-board)
- [Assign Staff View](#assign-staff-view)
  - [Add Providers, Residents, and Nurses](#add-providers-residents-and-nurses)
  - [Remove Providers, Residents, and Nurses](#remove-providers-residents-and-nurses)
  - [Configure Colors for Providers, Residents, and Nurses](#configure-colors-for-providers-residents-and-nurses)
- [Reports View](#reports-view)
  - [Eleven Standard Reports](#eleven-standard-reports)
    - [Column Headings](#column-headings)
    - [Standard Reports](#standard-reports)
    - [Cross Reference and Provider Reports](#cross-reference-and-provider-reports)
  - [Run and View Reports](#run-and-view-reports)
    - [Print Reports](#print-reports)
    - [Export Reports](#export-reports)
- [Configure View](#configure-view)
  - [Room and Area Configurations](#room-and-area-configurations)
    - [Add, Configure, and Edit Rooms and Areas](#add-configure-and-edit-rooms-and-areas)
  - [Display Board Configurations](#display-board-configurations)
    - [Add a New Display Board](#add-a-new-display-board)
    - [Add Display Board Columns](#add-display-board-columns)
    - [Configure or Edit Display Board Columns](#configure-or-edit-display-board-columns)
    - [Specify the Order of Display Board Columns](#specify-the-order-of-display-board-columns)
    - [Resize Display Board Columns](#resize-display-board-columns)
    - [Remove Display Board Columns](#remove-display-board-columns)
    - [Save Display Board Configuration Changes](#save-display-board-configuration-changes)
  - [Configure Colors](#configure-colors)
    - [Configure Colors (General Instructions)](#configure-colors-general-instructions)
    - [Configure Colors for Status and Acuity Values](#configure-colors-for-status-and-acuity-values)
    - [Configure Colors for Urgency – Lab Values](#configure-colors-for-urgency-lab-values)
    - [Configure Colors for Urgency – Radiology Values](#configure-colors-for-urgency-radiology-values)
    - [Configure Colors for Total Elapsed Minutes](#configure-colors-for-total-elapsed-minutes)
    - [Configure Colors for Minutes at Location](#configure-colors-for-minutes-at-location)
    - [Configure Colors for Minutes for Lab Order](#configure-colors-for-minutes-for-lab-order)
    - [Configure Colors for Minutes for Imaging Order](#configure-colors-for-minutes-for-imaging-order)
    - [Configure Colors for Minutes for Unverified Orders](#configure-colors-for-minutes-for-unverified-orders)
  - [Configure Parameters](#configure-parameters)
    - [Include Residents on Entry Form](#include-residents-on-entry-form)
    - [Require a Diagnosis](#require-a-diagnosis)
    - [Require ICD-9-CM or Free Text Diagnoses](#require-icd-9-cm-or-free-text-diagnoses)
    - [Require Disposition to Remove Patients](#require-disposition-to-remove-patients)
    - [Require a Reason for Delay](#require-a-reason-for-delay)
    - [Configure Shift Parameters](#configure-shift-parameters)
    - [Set a Default Room or Area for Patients Arriving by Ambulance](#set-a-default-room-or-area-for-patients-arriving-by-ambulance)
    - [Set a Default Room or Area](#set-a-default-room-or-area)
    - [Save Parameter Selections](#save-parameter-selections)
  - [Add Choices to Selection Lists](#add-choices-to-selection-lists)
    - [Add Status, Disposition, Delay Reason, and Source Selections](#add-status-disposition-delay-reason-and-source-selections)
- [Index](#index)
1.  The revision-history cycle begins after the initial version of the user guide has been completed and approved .mode
|      |                  |             |                 |        |
|------|------------------|-------------|-----------------|--------|
| Date | Patch or Version | Description | Project Manager | Author |
|      |                  |             |                 |        |
|      |                  |             |                 |        |
|      |                  |             |                 |        |
|      |                  |             |                 |        |

# Emergency Department Integration Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Emergency Department Integration Software (EDIS) incorporates several Web-based views that extend the current Computerized Patient Record System (CPRS) to help healthcare professionals track and manage the flow of patient care in the emergency-department setting. EDIS views are based on a class-three application developed by the Upstate New York Veterans Health Care Network—or Veterans Integrated Services Network (VISN) 2. Most views are site configurable. EDIS enables you to:

- Add emergency-department patients to the application’s display board
- View information about patients on the display board
- Edit patient information
- Remove patients from the display board
- Create administrative reports

The application also includes views for entering patients’ dispositions, removing patients from the display board, and configuring the display board.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide steps you through the process of performing the following tasks:

- Launch Emergency Department Integration Software (EDIS)
- Sign in patients to the emergency department (when you use the VistA Scheduling package (also known as Appointment Manager) to make appointments for—or check patients into—the emergency department, EDIS automatically adds the patients to its Active Patients list)
- Enter Emergency Severity Index (ESI) values for triaged patients
- Create emergency-department visits in the CPRS Patient Care Encounters (PCE) package (if not using Appointment Manager)
- Update patient information as patients progress through the emergency-care process
- View the display board
- Enter patients’ dispositions in EDIS
- Enter patients’ discharge diagnoses in EDIS and CPRS
- Remove patients from the display board (this task incorporates disposing patients, which supports discharge and admit processes)
- Make site- and shift-relevant staff assignments
- Edit visit-related information
- Create reports
- Configure the application using its graphical user interface (GUI) tools

![](emergency-dept-integration-software-edis-version-1-0-user-guide/003.png)

> Figure 1: EDIS user interface.

## Section 508 of the Rehabilitation Act of 1973 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Portable Document File (PDF) version of this guide supports assistive reading devices such as Job Access with Speech (JAWS). Because the views that comprise EDIS provide graphical user interface (GUI) access to underlying functionality, the guide includes steps for accessing application functionality via mouse devices and keyboard actions (when keyboard actions are available).

### Recommendations for JAWS Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To effectively use EDIS with JAWS, the EDIS project team offers the following recommendations:

1.  Use JAWS 10.
2.  Use JAWS forms mode; most functions work best in Forms mode.
3.  In JAWS 10, use JAWS Verbosity settings to turn off Autoforms mode.
4.  Make sure the latest Flex scripts are installed on your machine. (You can download JAWS scripts for Flex 3—an executable file—at <http://www.adobe.com/accessibility/products/flex/jaws.html>.)

Flex applications behave a bit differently than do regular Web applications—a result of the way Flash and Flex interact with browsers and JAWS screen readers. JAWS, Flex, and EDIS work together best with IE 6.0. (Testers experienced a few problems with IE 7.0 and Firefox.) Regardless of which browser you use, you can expect a slight learning curve.

## Role-based Access to Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS provides role-based access to the specific functionality sets that are available through its views. If the application does not display in its left-hand menu pane, one or more of the views this guide describes, your current role may not be compatible with functionality that the views include. Please contact your information resource management (IRM) or clinical application coordinator (CAC) staff if you have questions about your role. Please see *Emergency Department Integration Software Technical Manual—M Server* for information about configuring role-based access to application functionality.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Bold type indicates application elements (views, panes, links, buttons, and text boxes, for example) and key names.
- Key names appear in angle brackets \<\>.
- *Italicized* text indicates special emphasis.
- The warning icon ([![](emergency-dept-integration-software-edis-version-1-0-user-guide/004.png)](http://www.google.com/imgres?imgurl=http://www.shingleberrysigns.com/design_icon/warning%25201.gif&imgrefurl=http://www.shingleberrysigns.com/design_a_sign.php&usg=__wZUf1BihAcvMKNvqvpQGCx7UNtM=&h=1247&w=1413&sz=23&hl=en&start=3&sig2=6o6B87g3UKWHWxoCjJwZWQ&um=1&itbs=1&tbnid=_VZGtdgK3Q6_5M:&tbnh=132&tbnw=150&prev=/images%3Fq%3Dwarning%26um%3D1%26hl%3Den%26safe%3Dactive%26sa%3DN%26tbs%3Disch:1&ei=gscYTMqpDcqNnQedre2dCg)) indicates items of particular importance.
- Within the confines of this user guide, the terms *visit* and *encounter* are synonymous.

## Workstation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS runs in Adobe Flash Player, which in turn runs in a Web browser. If you do not have Flash Player 9.0 or above installed on your computer, EDIS will prompt you to download and install it. Installation requires administrator access to your machine; you may need assistance from an IT representative at your site.

### Flash Player: Minimum Requirements for Microsoft Windows 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Intel Pentium II 450MHz or faster processor (or equivalent), AMD Athlon 600MHz or faster processor (or equivalent)
- 128MB RAM
- Browsers:

> Browser Requirements for Flash Player 9.x

| Platform                   | Browser                                                                                                                           |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Windows Vista              | Internet Explorer 7, Firefox 2.0, AOL 9                                                                                           |
| Windows XP                 | Internet Explorer 6.0 or later, Firefox 1.x, Firefox 2.x, Mozilla 1.x or later, Netscape 7.x or later, AOL 9, Opera 7.11 or later |
| Windows Server 2003        | Internet Explorer 6.0 or later, Firefox 1.x, Firefox 2.x                                                                          |
| Windows 2000               | Internet Explorer 5.x, Firefox 1.x, Firefox 2.x, Mozilla 1.x, Netscape 7.x or later, AOL 9, Opera 7.11 or later                   |
| Windows Millennium Edition | Internet Explorer 5.5, Firefox 1.x, Mozilla 1.x, Netscape 7.x or later, AOL 9, Opera 7.11 or later                                |
| Windows 98                 | Internet Explorer 6.0 or later, Firefox 1.x, Mozilla 1.x, Netscape 7.x or later, Opera 7.11 or later                              |

> Browser Requirements for Flash Player 10.x

| Platform            | Browser                                                                                                         |
|---------------------|-----------------------------------------------------------------------------------------------------------------|
| Windows Vista       | Microsoft Internet Explorer 7.0 or later, Firefox 2.x, Firefox 3.x, AOL 9, Safari 3.x                           |
| Windows XP          | Microsoft Internet Explorer 6.0 or later, Firefox 2.x, Firefox 3.x, AOL 9, Opera 9.5 or later, Safari 3.x       |
| Windows Server 2003 | Microsoft Internet Explorer 6.0 or later, Firefox 2.x, Firefox 3.x                                              |
| Windows 2000        | Internet Explorer 5.x, Firefox 1.x, Firefox 2.x, Mozilla 1.x, Netscape 7.x or later, AOL 9, Opera 7.11 or later |
| Windows Server 2008 | Internet Explorer 7.0 or later, Firefox 3.x                                                                     |
| Windows 2000        | Internet Explorer 6.0, Firefox 2.x, Firefox 3.x, AOL 9, Opera 9.5                                               |

### Flash Player: Minimum Requirements for Apple Mac OS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- PowerPC G3 500MHz or faster processor or Intel Core Duo 1.33GHz or faster processor
- 128MB RAM
- Browsers:

> Browser Requirements for Flash Player 9.x

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Platform</th>
<th>Browser</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Mac OS X 10.1 or later<br />
(PowerPC)</td>
<td>Firefox 1.x, Mozilla 1.x, Netscape 7.x or later, AOL for Mac OS X, Opera 6, Safari 1.x or later</td>
</tr>
<tr class="even">
<td>Mac OS X 10.4.x or later (Intel)</td>
<td>Firefox 1.5.0.3 or later, Opera 6, Safari 2.x or later</td>
</tr>
</tbody>
</table>

> Browser Requirements for Flash Player 10.x

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Platform</th>
<th>Browser</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Mac OS X 10.4 or 10.5<br />
(PowerPC)</td>
<td>Firefox 2.x, Firefox 3.x, AOL for Mac OS X, Opera 9.5, Safari 3.x</td>
</tr>
<tr class="even">
<td>Mac OS X 10.4.x or 10.5 (Intel)</td>
<td>Firefox 2.x, Firefox 3.x, Opera 9.5, Safari 3.x</td>
</tr>
</tbody>
</table>

### JAWS Workstation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are a JAWS user, you or your site’s IRM staff must download and install Adobe Flex accessibility scripts. To download JAWS scripts for Flex 3, go to <http://www.adobe.com/accessibility/products/flex/jaws.html>. Click the executable file to install the scripts on your machine. These scripts work for JAWS 9 and 10; however, the EDIS project team recommends that you use JAWS 10 for the best results with EDIS.

Flex applications behave a bit differently than do regular Web applications—a result of the way Flash and Flex interact with browsers and JAWS screen readers. JAWS, Flex, and EDIS work together best with IE 6.0. (Testers experienced a few problems with IE 7.0 and Firefox.) Regardless of which browser you use, you can expect a slight learning curve.

1.  JAWS 10 users must turn off Autoforms mode (use the JAWS Verbosity settings).

## Application Timeouts 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS uses the same parameter settings that CPRS uses for application timeouts and timeout countdowns: namely, ORWOR TIMEOUT CHART and ORWOR TIMEOUT COUNTDOWN settings. IRM personnel enter values for these parameters at the site level. Emergency-department managers usually *do not* determine them. For many sites, EDIS and CPRS are set to time out after 15 minutes of inactivity.

If the ORWOR TIMEOUT CHART parameter contains a value, this value determines the amount of time that EDIS can sit idle before it displays a timeout warning and begins its countdown. (The ORWOR TIMEOUT CHART parameter supports a maximum timeout value of 2147483 seconds. Sites can determine local timeout values that are smaller than or equal to this maximum value.)

If the ORWOR TIMEOUT CHART parameter contains no value, EDIS uses the value of the Timed Read (DTIME) parameter, which is available through VistA’s user setup menu. The value of the ORWOR TIMEOUT COUNTDOWN setting determines the length of the application’s timeout countdown.

EDIS displays its timeout message and countdown within the browser, at the bottom of the current EDIS view. Because JAWS cannot read this message, EDIS also sounds a chime as it begins its timeout countdown.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/005.png)

> Figure 2: The EDIS timeout warning and countdown.

1.  If users are simultaneously running CPRS and EDIS, an active CPRS window can obscure the EDIS timeout warning and countdown. In high-use situations—in triage areas where several users share a single instance of CPRS and EDIS, for example—facilities may want to consider using separate screens for each application. This solution helps ensure that both applications are fully visible.

## Preventing Accidental Application Sign-Outs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS may automatically sign you out when you launch other Web applications—such as UpToDate—while it is running. You can prevent this from happening by cancelling the selection of Internet Explorer’s Reuse windows for launching shortcuts setting. The following fix-it-yourself solution should be available to all users (administrative access is not required).

1.  Launch Internet Explorer and click Tools on the main menu.
2.  Select Internet Options.
3.  Select the Advanced tab in the Internet Options dialog box.
4.  In the Browsing list, find the Reuse windows for launching shortcuts or (depending on the version of Internet Explorer you are using) Reuse windows for launching shortcuts (when tabbed browsing is off) setting.
5.  If this setting is selected, click the checkbox to cancel the selection.

> ![](emergency-dept-integration-software-edis-version-1-0-user-guide/006.png)

> Figure 3: The Internet Options dialog box, Advanced tab, Browsing list.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Launch EDIS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your IRM or CAC staff hasn’t provided a desktop shortcut or added an EDIS link to your CPRS Tools menu, you can access EDIS by pointing your browser to REDACTED—the application’s Uniform Resource Locater (URL).

If you want to access the application’s main electronic whiteboard (or big-board) display, use the following URL: REDACTED. If you want to access a secondary big-board display, use this URL:REDACTED. (Replace *\[boardname\]* with the name of the display board you want to view.)

When you access these URLs, the application's security system automatically redirects you to the login page. As it does this, the security system begins its authentication process.

#### Adding EDIS to your Internet Explorer Favorites 

If you bookmark the EDIS login page, the link you initially create will bypass the application’s redirection-authentication process and the application’s security system will deny you access. You can remedy this situation by editing your bookmark link.

1.  In Internet Explorer, right-click the EDIS login bookmark and select Properties.
2.  Edit the URL field to contain either REDACTED or REDACTED
3.  Click OK.

You can also create desktop shortcuts using these URLs.

## Log In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you launch EDIS, the application displays a login view that uses credentials stored in your local VistA system.

To log in:

1.  Type your VistA access and verify codes in the Access Code and Verify Code boxes, respectively.
1.  Select your site in the Institution list. EDIS uses a persistent cookie to preselect your site upon subsequent logins, but only on the specific machine you used when you made this selection. You must select your site from the Institution list each time you use a new computer. (Your site may have configured a desktop shortcut that eliminates the need for this step by preselecting your institution.)
2.  Failure to select the correct institution is the most common cause of unsuccessful login attempts.
2.  Click Login or press the \<Enter\> key.

### Changing Your Verify Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For user authentication, EDIS relies on Kernel Authentication and Authorization for Java 2 Enterprise Edition (KAAJEE)—which is the only VA-approved login security package. KAAJEE limitations prevent EDIS from offering functionality that allows you to change your verify code *within* the EDIS application. When your VistA verify code expires, you can change it in CPRS or another VistA application. EDIS will then accept the change.

## EDIS Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following is a list and brief explanation of each view.

3.  Not all views are available to all users. EDIS offers site-configurable, role-based access to views. If you do not have access to a view that you need, speak with the IRM or CAC staff responsible for role-based access at your site.

#### Sign In

The Sign In view enables you to add patients to the application and the display board. This view also allows you to add for-display complaints, assign rooms or areas, and select patients’ sources (the places from which patients have come—onsite clinics or offsite nursing homes, for example).

#### Triage

The Triage view enables you to add patients to the display board; add their acuity, nurse, provider, and resident assignments; specify the clinic location that EDIS will use to create PCE visits (if applicable); and add or update patients’ source and room or area assignments.

#### Update

The Update view enables you to add patients’ status information and comments that the application does *not* display on the display board. You can also add or update physician, resident, nurse, and room or area assignments.

#### Disposition

The Disposition view enables you to enter patients’ dispositions and diagnoses (either International Classification of Diseases, Ninth Revision, Clinical Modifications \[ICD-9-CM\] or free-text, if the system administrator allows free-text entries). If patients’ stays have exceeded the national emergency-department visit limit (currently six hours), the application may require you to select a reason for delay. If it does, this view will include a list of reasons from which you can choose. You can also add or update patients’ status and provider and resident assignments from this view.

#### Edit Closed

The Edit Closed view enables you to edit patients’ information after their emergency-department visits have ended.

#### Display Board

The Display Board view is a PC-based version of your site’s main electronic white-board—or big-board—display. You can configure multiple big-board displays for your site. However, you can view only your site’s main display board using the PC-based Display Board view.

#### Assign Staff

The Assign Staff view enables you to create site-specific staff-selection lists. You can also use this view to assign color indicators for individual staff members.

#### Reports

The Reports view enables you to select date ranges for, and run, 11 standard reports. EDIS also includes two restricted reports that require security-key access.

#### Configure

The Configure view enables you to localize the tracking application. For example, it enables you to assign locally meaningful color codes for patients’ acuities and statuses, populate pick lists with the names of your site’s treatment areas, set up display boards that contain only relevant information, and more.

### Select a View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click the view you want to access on the left-hand view-selection menu. This menu is available from all application views. Keyboard: use the \<Tab\> key to locate the left-hand view-selection menu. Use the \<Down Arrow\> and \<Up Arrow\> keys to locate the view you want to select. Use the \<Spacebar\> key to select the view.

## Work with Data Grids

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS commonly displays information using a tabular—or grid—format. The application’s data grids allow you to:

- Arrange columns
- Resize columns
- Sort within columns
2.  The results of these actions are temporary. EDIS does not retain data-grid changes.

### Arrange Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform a drag-and-drop operation:

1.  Point to a column header and hold down the left mouse button.
5.  Still holding down the left mouse button, move the column header to a new location.
6.  Release the left mouse button.

### Resize Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform a drag-and-drop operation:

1.  Point your mouse to a column boarder in the header row. EDIS displays a column slider in place of the pointer.
2.  Hold down the left mouse button and move the boarder to a new location.
3.  Release the left mouse button.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/007.png)

> Figure 4: The slider for resizing columns.

### Sort Information within Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can sort the information within most columns.

- Click a column header to sort the information within the column in descending order.
- Click the column header again to sort the column’s contents in ascending order.

> ![](emergency-dept-integration-software-edis-version-1-0-user-guide/008.png)

> Figure 5: Sort information within columns by clicking on column headers.

## Access Help Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Click the Help button to access view-specific Help files. Keyboard: use the \<Tab\> key to locate the Help button and use the \<Spacebar\> key to select the button.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/009.png)

> Figure 6: The Help button is located in the right-hand corner of the application’s title bar.

## Understanding EDIS and CPRS Interactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can successfully integrate CPRS with EDIS in one of two ways:

- Create an unscheduled appointment in Appointment Management; when you create an unscheduled appointment for a clinic location your site has specified in the EDPF LOCATION parameter, EDIS adds the patient to the EDIS Active Patients list.
- Create an unscheduled visit (encounter) via patient care encounters (PCE).

Each method has strengths and weaknesses. As is the case for any patient-scheduling system, less-than-optimal practices can lead to duplicated encounters. Sections 2.7 and 2.8 provide information that may help you choose the method that’s best for your location. Please read these two sections carefully.

## Using EDIS with Appointment Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Benefits of this Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your site maintains the advantage of having a selectable list of triaged emergency-department patients available on the CPRS Patient Selection view. This list of scheduled (that is, Appointment Management-created) appointments is not available via the PCE method.

### Drawbacks of this Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful CPRS and EDIS integration using this method requires intensive (recommended twenty-four-hours a day, seven days a week—or 24x7) secretarial and administrative support. For this method to work, your site must create an appointment for each emergency-department patient before doing anything else–which requires round-the-clock support of administrative staff who have access to Appointment Management.

### Best Practice for Using EDIS with Appointment Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Add Patients to Appointment Management First:

> When a patient presents to the emergency department for evaluation, a member of your site’s administrative staff immediately creates an appointment for the patient in Appointment Management. This creates a selectable visit in CPRS and adds the patient to EDIS. The triage nurse must subsequently add additional data to EDIS.

####### EXAMPLE:

- Ms. Jones arrives at 11:30.
- At 11:32, a member of the administrative staff uses Appointment Management to create an appointment for Ms. Jones.
- EDIS automatically displays Ms. Jones on its Active Patients list.
- The triage nurse sees Ms. Jones at 11:35 and completes her EDIS triage information; the nurse then opens CPRS and writes a triage note *under the visit in CPRS that corresponds to Ms. Jones’s emergency-department appointment*.
- The emergency-department provider selects this same visit in CPRS when he or she writes notes or orders related to Ms. Jones’s emergency-department care.

#### Why this Is Best Practice

CPRS was created long before EDIS. It has not been changed to recognize that EDIS exists.

### Processes with Unscheduled Appointments (in Appointment Management) that Lead to Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

4.  [![](emergency-dept-integration-software-edis-version-1-0-user-guide/010.png)](http://www.google.com/imgres?imgurl=http://www.shingleberrysigns.com/design_icon/warning%25201.gif&imgrefurl=http://www.shingleberrysigns.com/design_a_sign.php&usg=__wZUf1BihAcvMKNvqvpQGCx7UNtM=&h=1247&w=1413&sz=23&hl=en&start=3&sig2=6o6B87g3UKWHWxoCjJwZWQ&um=1&itbs=1&tbnid=_VZGtdgK3Q6_5M:&tbnh=132&tbnw=150&prev=/images%3Fq%3Dwarning%26um%3D1%26hl%3Den%26safe%3Dactive%26sa%3DN%26tbs%3Disch:1&ei=gscYTMqpDcqNnQedre2dCg)The following list contains things you should not do. We have included this section to help you troubleshoot problems that can occur when your site uses EDIS with unscheduled appointments in Appointment Management.
1.  Creating unscheduled appoints just before the midnight hour:  
    Appointments will disappear at midnight for patients who have unscheduled appointments for times that precede the midnight hour and for whom emergency-department personnel have completed neither documentation nor orders before midnight. When this occurs, your site must reenter the vanished appointments, thus creating both second appointments and duplicate PCE encounters. This problem is the result of CPRS business logic, which exists outside of EDIS.
2.  Failing to select the proper appointment when writing notes or ordering tests:  
    Providers and nurses create duplicate PCE encounters if they fail to select the proper appointment in CPRS when writing notes or ordering tests.
3.  Writing notes or orders before creating unscheduled appointments:  
    Providers and nurses create duplicate PCE encounters when they write orders or notes before administrative personnel have created unscheduled appointments for their patients.

## Using EDIS with PCE 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Benefits of this Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Integrating EDIS with CPRS via PCE does *not* require intensive (recommended 24x7) support from personnel who have access to Appointment Management. (The Appointment Management method requires sites to create appointments for patients before doing anything else, which in turn requires round-the-clock support from administrative personnel who have access to Appointment Management.)

### Drawbacks of this Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When sites switch from using Appointment Management to PCE, their users no longer have a list on their Patient Selection (initial) view of CPRS from which they can select patients who have emergency-department appointments. This list of scheduled (that is, Appointment Management-created) appointments only appears when sites use the Appointment Management method. As a result of not having this list, looking up patients who were discharged in the past (days or weeks ago) is a little more difficult in CPRS. However, authorized users can easily look up these patients in the EDIS Edit Closed view.

### Best Practice for Using EDIS with PCE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Place Patient on EDIS First with Provider Name:

When a patient presents to the emergency department for evaluation, someone notifies the triage nurse and adds the patient to EDIS. The person who adds the patient to EDIS must also add a provider name at this step. Assigning a provider in EDIS creates an unscheduled visit (encounter) in CPRS. Providers and nurses can subsequently write their notes and orders under this visit.

Although assigning a nurse in EDIS can also generate a visit in CPRS, it doesn’t always. Nurse assignments generate selectable visits in CPRS only if your hospital configures nurses with an active person class in VistA’s New Person file. Some sites do not allow this practice. In addition, using nursing assignments to create PCE visits makes nurses primary providers in EDIS-generated encounters. Primary providers must change these placeholder assignments for visits other than nursing-only visits. To do this, primary providers should select Yes when CPRS prompts them to identify themselves as primary providers for encounters they are signing.

EXAMPLE \#1:

- At 11:31, a member of the administrative staff or a triage nurse adds Mr. Jones to EDIS and assigns Dr. Smith as Mr. Jones’s provider.
- This creates an 11:31 visit (encounter) for Mr. Jones in CPRS.
- The triage nurse opens CPRS, enters Mr. Jones’s chart, starts note, and *selects the emergency-department visit that already appears in CPRS.*
- The triage nurse writes and signs the note.
- Mr. Jones’s provider writes a note or orders, also selecting the visit that EDIS already created in CPRS.

> In this example, if the initially assigned provider is not the primary provider for the visit, the primary provider must select himself or herself when he or she signs the note. Someone (the provider, a clerk, or another emergency-department staff member) must also update EDIS to reflect the correct primary provider.

EXAMPLE \#2:

- At 11:31, an LPN adds Mr. Jones to EDIS.
- Mr. Jones’s triage nurse has an active person class in VistA’s New Person file and opens a PCE encounter for Mr. Jones’s visit in CPRS as a provider.
- A provider sees Mr. Jones; the provider (or a charge nurse or clerk) adds the provider’s name in EDIS.
- When he is signing the encounter in CPRS, the provider identifies himself as the primary provider for the encounter.

> Had no primary provider seen Mr. Jones (if he had left without being seen, for example) the triage nurse would close the encounter as a nurse-only visit.

### Why this Is Best Practice

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS was created long before EDIS and has not been updated to recognize that EDIS exists.

The PCE system is limited—it cannot create visits unless users enter primary providers or diagnoses for the encounters. If users add patients to EDIS without selecting their primary providers or diagnoses, EDIS cannot give to CPRS the information that CPRS must supply to the PCE application, and PCE cannot create the encounters. This is a limitation of the PCE application, not a limitation of EDIS. Because diagnoses are rarely available early in the patient-care process, the best practice is to select a provider when you add a patient to EDIS.

5.  When patients present before midnight but providers do not treat them until after midnight, the providers must be certain to select the EDIS-created visit from the preceding day, as opposed to opening new (duplicate) visits.

### Processes with PCE that Lead to Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

6.  [![](emergency-dept-integration-software-edis-version-1-0-user-guide/011.png)](http://www.google.com/imgres?imgurl=http://www.shingleberrysigns.com/design_icon/warning%25201.gif&imgrefurl=http://www.shingleberrysigns.com/design_a_sign.php&usg=__wZUf1BihAcvMKNvqvpQGCx7UNtM=&h=1247&w=1413&sz=23&hl=en&start=3&sig2=6o6B87g3UKWHWxoCjJwZWQ&um=1&itbs=1&tbnid=_VZGtdgK3Q6_5M:&tbnh=132&tbnw=150&prev=/images%3Fq%3Dwarning%26um%3D1%26hl%3Den%26safe%3Dactive%26sa%3DN%26tbs%3Disch:1&ei=gscYTMqpDcqNnQedre2dCg)The following list contains things you should not do. We have included this section to help you troubleshoot problems that can occur when your site uses EDIS with the PCE system.
1.  Failing to select a provider when adding a patient to EDIS:  
    When you fail to select a provider, EDIS cannot create a visit (encounter) in CPRS.
2.  Failing to add a patient upon his or her arrival:  
    Duplicate encounters will result if users fail to add patients to EDIS (and select a provider) until after clinicians have started writing notes or orders.
3.  Failing to select the EDIS-created visit when starting notes or writing orders:  
    Duplicate encounters will result if nurses and providers fail to select the visit EDIS creates when they start notes or create orders.
4.  Continuing to use Appointment Management for some patients:  
    Implementing two separate process flows can confuse staff and lead to errors.

# Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patient-Selection Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you select patients who are already registered in your local VistA system, EDIS may display one or more of the following messages:

Restricted Record Warning: this message appears when you select a patient whose records contain sensitive information. Only authorized users may view these records.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/012.png)

> Figure 7: Restricted Record warning (sensitive patient data).

Patient Record Flags: EDIS displays these advisory messages when you add patients whose records are flagged in VistA. You can view patient record flags after you’ve added patients by clicking the Flag button, which appears on the Patient Information bar when you select the Sign In, Triage, Update, Disposition, or Edit Closed view.

When you click the Flag button, EDIS displays important information to help you and other clinical staff better care for patients whose behavior or medical conditions warrant special attention. The application displays patient-record flags in the Active Flag window.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/013.png)

> Figure 8: The Active Flag window.

Duplicate Selection: EDIS displays this advisory when you attempt to add patients who are already active in the application.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/014.png)

> Figure 9: The Duplicate Selection warning.

Multiple Patient icon: the application alerts you to the possibility of confusing patients’ identities by displaying an icon (![](emergency-dept-integration-software-edis-version-1-0-user-guide/015.png)) when two or more patients share the same last name or at least two consecutive ending digits of their social security numbers.

# Sign In View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS automatically adds patients when you use VistA’s Scheduling (Appointment Management) package to create an emergency department appointment for patients.

The EDPF LOCATION parameter, which holds your site’s emergency department location or locations, controls this functionality. Parameter settings ensure that only emergency-department check-ins and appointments add patients to EDIS.

You can also add patients to the application from its Sign In and Triage views.

## Add Patients to EDIS from the Sign In View 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](emergency-dept-integration-software-edis-version-1-0-user-guide/016.png)

> Figure 10: The Add Patient dialog box.

#### - Click Add Patient in the upper right-hand corner of the Active Patients list. Keyboard: use the \<Tab\> key to locate the Add Patient button and press the \<Spacebar\> key to select it. The application displays the Add Patient dialog box, which offers the following three selections*:*

- [*Search for Patient in VistA*](#_Adding_Patients_Using): enables you to add patients who are already in your local VistA system
- [*Ambulance Is Arriving, Patient Name Is Unknown:*](#Ambulance_arriving_unk_patient) enables you to add information for patients whose identities are unknown (EDIS does not create PCE visits for these patients until someone adds them via a VistA search)
- [*Enter Name, Patient Is Not in VistA*](#Patient_not_registered) enables you to add patients who are not in your local VistA system (EDIS does not create PCE visits for these patients until someone adds them via a VistA search)
3.  EDIS does not activate the Add Patient button when you are already in the process of signing in a patient. To activate the Add Patient button in this case, you must click Save to complete the sign-in process for the current patient or Cancel to cancel the process and discard the information you’ve entered.

### Adding Patients Using the Search for Patient in VistA Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If necessary, select Search for Patient in VistA. (Search for Patient in VistA is the application’s default selection; in most cases, you won’t need to manually select this button.) Keyboard: if the Search for Patient in VistA button isn’t already selected, use the \<Tab\> key to locate the selected button (Enter Name, Patient Is Not in VistA or Ambulance Is Arriving, Patient Name Is Unknown). Use the \<Up Arrow\> key to locate the Search for Patient in VistA button and use the \<Spacebar\> key to select it.
7.  Type all or part of the patient’s name in the Find Patient box using this format: Surname,Firstname. For example, you can search using the patient’s surname only, or the patient’s surname and the first initial of his or her first name. You can also search using the initial letter of the patient’s surname concatenated with the last four digits of his or her Social Security number (X9999 format), the patient’s entire Social Security number (SSN), or the last four digits of his or her SSN.
7.  Use an underscore to denote spaces in names. For example, if the patient’s name is O Hara, type O_Hara.
8.  Click Search or press the \<Enter\> key.
9.  The Add Patient dialog box lists possible matches. Select the correct patient and click Continue or press the \<Enter\> key. Keyboard: use the \<Down Arrow\> and \<Up Arrow\> keys to locate the correct patient. Press the \<Enter\> key to select the patient or use the \<Tab\> key to locate the Continue button and then press the \<Spacebar\> key to select it.

The application displays the [Patient Information](#patient_info_pane_sign_in) pane.

### Adding Patients Using the Enter Name Selection 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Find Patient search list does not contain a match, add the patient using the Enter Name, Patient Is Not in VistA selection.

1.  In the Add Patient dialog box, select EnterName, Patient Is Not in VistA. Keyboard: use the \<Tab\> key to locate the currently selected button and use the \<Down Arrow\> or \<Up Arrow\> key to locate the Enter Name, Patient Is Not in VistA button. Press the \<Spacebar\> key to select this button.
10. EDIS automatically populates the Patient Name box with the name you typed to initiate the VistA search. If this name is incorrect or incomplete, type the patient’s full name in the Patient Name box using this format: Lastname,Firstname. Keyboard: use the \<Tab\> key to locate the Patient Name box.
11. Press the \<Enter\> key or click Continue.

The application displays the [Patient Information](#patient_info_pane_sign_in) pane.

#### Adding Unidentified Patients

When you must add unresponsive patients whose identities you do not know, use the Enter Name, Patient Is Not in VistA selection and follow the naming protocol defined in section 12 of VHA Directive 2006-036: *Data Quality Requirements for Identity Management and Master Patient Index Functions*. (Use the name *UU-UNRESPONSIVE,PATIENT* for the first such patient, *UU-UNRESPONSIVE,PATIENT A* for the second, *UU-UNRESPONSIVE,PATIENT B* for the third, and so forth. You can find the full text of this directive at REDACTED

### Adding Patients Using the Ambulance Is Arriving Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS enables you to add unknown patients who are arriving by ambulance or other types of emergency transportation, thereby allowing you to make room, provider, and nurse assignments before these patients arrive.

1.  Select Ambulance Is Arriving, Patient Name Is Unknown. Keyboard: use the \<Tab\> key to locate the currently selected button, and use the \<Down Arrow\> key to locate the Ambulance Is Arriving, Patient Name Is Unknown button. Press the \<Spacebar\> key to select this button.
12. Click Continue. Keyboard: use the \<Tab\> key to locate the Continue button and use the \<Spacebar\> key to select it.

The application displays the [Patient Information](#_Add_Information_to) pane.

8.  EDIS reports do not reflect the number of patients whom users add to the application via this method.  
      
    Also, EDIS creates its Time In timestamps when users identify patients in VistA or create unscheduled appointments for them in Appointment Management. As a result, sites must correct EDIS’s Time In values to reflect the times these patients actually arrived at the emergency department.

### Add Information to the Patient Information Pane

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In the Complaint for Display Board box, type the complaint you want the application to present on the big board display. This information is mandatory; you must type a complaint in this box or the application will not add your patient. The box accepts up to 50 characters. Keyboard: press the \<Tab\> key to locate the Complaint for Display Board box.
13. Open the Room / Area list. Select a room or area. Room or area information is mandatory. The application’s default selection is the waiting room. Keyboard: use the \<Tab\> key to locate the Room / Area list and use the \<Down Arrow\> and \<Up Arrow\> keys to select a room or area from the list.
14. Open the Source list and select the source of the patient’s emergency-department visit—an offsite clinic, for example. (Definitions for nationally released sources are available in [section 4.1.5](#source_definitions) of this guide.) Keyboard: use the \<Tab\> key to locate the Source list and use the \<Down Arrow\> and \<Up Arrow\> keys to select a source from the list.
15. Click Save to save the patient’s sign-in information and add him or her to the display board.

> -or-

> Click Cancel to cancel the sign-in process. Keyboard: use the \<Tab\> key to locate the Save or Cancel button. Use the \<Spacebar\> key to select the button.

> ![](emergency-dept-integration-software-edis-version-1-0-user-guide/017.png)

> Figure 11: The Patient Information pane.

### Definitions for Nationally Released Source Selections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDIS technical working group (TWG) has provided the following definitions for nationally released source selections:

Non-VA Clinic/Office—a non-VA clinic, primary care, or other type of provider sent the patient.

VA Clinic, Off-Site—an offsite VA clinic—a community-based outpatient clinic (CBOC), for example—sent the patient.

On-Site Clinic—an onsite physician, nurse practitioner, physician assistant, nurse, or other care provider sent the patient for evaluation.

Non-VA Nursing Home—a non-VA community living center (CLC) sent the patient.

VA Nursing Home, Off-Site—an off-campus VA CLC transferred the patient.

On-Site Nursing Home—an on-campus VA CLC transferred the patient.

Walk In—the patient presents from outside the community without a referral—regardless of his or her mode of transportation.

Transfer, Other—other facilities transferred the patient (VA ED-to-ED transfers for subspecialty care would be included in this category).

# Identify Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Identify Patient button enables you to identify patients in VistA after you’ve added them to the application via the Enter Name – Patient Is Not in VistA or Ambulance Is Arriving, Patient Name Is Unknown selection. This button also allows you to identify patients who arrived by ambulance and are not in VistA. Identify Patient is available only for patients whom users added via one of these selections. The application displays this button on the Patient Information bar in the following views:

- Sign In
- Triage
- Update
- Disposition
- Edit Closed

If you or another user has added the wrong patient using the Search for Patient in VistA selection, you can remove the patient from the board by selecting Patient Name Entered in Error on the Disposition list. (See Section 8, “Disposition View.”)

![](emergency-dept-integration-software-edis-version-1-0-user-guide/018.png)

> Figure 12: The Identify Patient button.

## Identifying Patients 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In the Active Patients list, select the patient whom you want to identify. Keyboard: use the \<Tab\> key to locate the Active Patients list and use the \<Down Arrow\> key to enter the list. Use the \<Down Arrow\> or \<Up Arrow\> key to select a patient from the list.
3.  Click the Identify Patient button in the Patient Information bar. The application displays the Identify Patient dialog box. Keyboard: use the \<Tab\> key to locate the Identify Patient button. Use the \<Spacebar\> key to select the button.
4.  Type all or part of the patient’s name in the Find Patient box using this format: Surname,First name. For example, you can search using the patient’s surname only, or the patient’s surname and the first initial of his or her first name. You can also search using the initial letter of the patient’s surname concatenated with the last four digits of his or her Social Security number (X9999 format), the patient’s entire Social Security number (SSN), or the last four digits of his or her SSN.
5.  Select the patient from this list and press the \<Enter\> key or click Continue. Keyboard: use the \<Down Arrow\> and \<Up Arrow\> keys to locate the patient’s name. Use the \<Enter\> key to select the patient. You can also select the patient by using the \<Tab\> key to locate the Continue button and the \<Spacebar\> key to select the button.
6.  If your patient is not on the list and you added him or her via the Ambulance Is Arriving, Patient Name Is Unknown selection, click the Enter Name, Patient Is Not in VistA button. Keyboard: use the \<Tab\> key to locate the Search for Patient in VistA button and then use the \<Down Arrow\> key to locate the Enter Name, Patient Is Not in VistA button. Press the \<Spacebar\> key to select this button.
7.  EDIS automatically populates the Patient Name box with the name you typed in the Find Patient box. Correct this name if necessary. Keyboard: use the \<Tab\> key to locate the Patient Name box.
8.  Press the \<Enter\> key or click Continue. Keyboard: use the \<Tab\> key to locate the Continue button and use the \<Spacebar\> key to select it.
9.  Click Save. Keyboard: use the \<Tab\> key to locate the Save button and use the \<Spacebar\> key to select the button.

# Triage View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Triage view to edit or update information that you gather as part of the triage process. From this view, you can update patients’ display-board complaints; include additional, not-for-display information about their complaints (optional); update their room or area assignments; add information about their acuities; make nursing, provider, and resident assignments; update or add their sources (on-site clinics, nursing homes, and so forth); and specify a clinic location for the patient’s emergency-department visit. You can also add patients to the display board from the Triage view.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/019.png)

> Figure 13: The Triage view.

## Add Patients to EDIS from the Triage View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](emergency-dept-integration-software-edis-version-1-0-user-guide/020.png)

> Figure 14: The Add Patient dialog box.

- Click Add Patient in the upper right-hand corner of the Active Patients list. Keyboard: use the \<Tab\> key to locate the Add Patient button and press the \<Spacebar\> key to select it. The application displays the Add Patient dialog box, which offers the following three selections*:*
- [*Search for Patient in VistA*](#_Adding_Patients_Using): enables you to add patients who are already in your local VistA system
- [*Ambulance Is Arriving, Patient Name Is Unknown:*](#Ambulance_arriving_unk_patient) enables you to add information for patients whose identities are unknown (EDIS does not create PCE visits for these patients until someone adds them via a VistA search)
- [*Enter Name, Patient Is Not in VistA*](#Patient_not_registered) enables you to add patients who are not in your local VistA system (EDIS does not create PCE visits for these patients until someone adds them via a VistA search)
4.  EDIS does not activate the Add Patient button when you are already in the process of signing in or triaging a patient. To activate the Add Patient button in this case, you must click Save to complete the triage process for the current patient or Cancel to cancel the process and discard the information you’ve entered.

### Adding Patients Using the Search for Patient in VistA Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If necessary, select Search for Patient in VistA. (Search for Patient in VistA is the application’s default selection; in most cases, you won’t need to manually select this button.) Keyboard: if the Search for Patient in VistA button isn’t selected, use the \<Tab\> key to locate the selected button (Enter Name, Patient Is Not in VistA or Ambulance Is Arriving, Patient Name Is Unknown). Use the \<Up Arrow\> key to locate the Search for Patient in VistA button, and use the \<Spacebar\> key to select it.
16. Type all or part of the patient’s name in the Find Patient box using this format: Surname, First name. For example, you can search using the patient’s surname only, or the patient’s surname and the first initial of his or her first name. You can also search using the initial letter of the patient’s surname concatenated with the last four digits of his or her Social Security number (X9999 format), the patient’s entire Social Security number (SSN), or the last four digits of his or her SSN. Keyboard: use the \<Tab\> key to locate the Find Patient box.
9.  Use an underscore to denote spaces in names. For example, if the patient’s name is O Hara, type O_Hara.
17. Click Search or press the \<Enter\> key.
18. The Add Patient dialog box lists possible matches. Select the correct patient and press the \<Enter\> key or click Continue. Keyboard: use the \<Down Arrow\> or \<Up Arrow\> key to locate the correct patient. Press the \<Enter\> key to select the patient. You can also select the patient by using the \<Tab\> key to locate the Continue button and then pressing the \<Spacebar\> key to select the button.
10. EDIS starts its timer when you click Continue.

The application displays the Patient Information pane.

### Adding Patients Using the Enter Name Selection 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Find Patient search list does not contain a match, add the patient using the Enter Name, Patient Is Not in VistA selection.

1.  In the Add Patient dialog box, select Enter Name, Patient Is Not in VistA. Keyboard: use the \<Tab\> key to locate the Search for Patient in VistA (or currently selected) button. Use the \<Down Arrow\> (or \<Up Arrow\>) key to locate the Enter Name, Patient Is Not in VistA button. Use the \<Spacebar\> key to select this button.
19. Type the patient’s full name in the Patient Name box using this format: Lastname,First name. Keyboard: use the \<Tab\> key to locate the Patient Name box.
20. Click Continue or press the \<Enter\> key.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/021.png)

> Figure 15: The Enter Name, Patient Is Not in VistA button.

The application displays the Patient Information pane.

#### Adding Unidentified Patients

When adding unresponsive patients whose identities you do not know, use the Enter Name, Patient Is Not in VistA selection and follow the naming protocol defined in section 12 of VHA Directive 2006-036: *Data Quality Requirements for Identity Management and Master Patient Index Functions*. (Use the name *UU-UNRESPONSIVE,PATIENT* for the first such patient, *UU-UNRESPONSIVE,PATIENT A* for the second, *UU-UNRESPONSIVE,PATIENT B* for the third, and so forth. You can find the full text of this directive at REDACTED

### Adding Patients Using the Ambulance Is Arriving Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS enables you to prepare for unknown patients who are arriving by ambulance or other types of emergency transportation. You can make room, provider, and nurse assignments before these patients arrive.

1.  Select Ambulance Is Arriving, Patient Name Is Unknown. Keyboard: use the \<Tab\> key to locate the currently selected button (Search for Patient in VistA or Enter Name, Patient Is Not in VistA). Use the \<Down Arrow\> key to locate the Ambulance Is Arriving, Patient Name Is Unknown button.
21. Click Continue. Keyboard: use the \<Tab\> key to locate the Continue button and use the \<Spacebar\> key to select it.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/022.png)

> Figure 16: The Add Patient dialog box with the Ambulance Is Arriving, Patient Name Is Unknown button selected.

The application displays the Patient Information pane.

## Add Triage Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In the Active Patients list, select the patient whose triage information you want to enter. Keyboard: use the \<Tab\> key to locate the Active Patients list. Use the \<Down Arrow\> key to enter the list, and use the \<Down Arrow\> and \<Up Arrow\> keys to locate the patient you want to select. The Patient Information pane displays current information for the selected patient.
10. If applicable, update the patient’s display-board complaint in the Complaint for Display Board box. If you added the patient from the Triage view, you must type a display-board complaint. The application will not allow you to add the patient if the Complaint for Display Board box is empty. Keyboard: use the \<Tab\> key to locate the Complaint for Display Board box.
11. In the Long Complaint (optional) box, you may type supplementary information about the patient’s display-board complaint. Keyboard: use the \<Tab\> key to locate the Long Complaint (optional) box.
12. If applicable, open the Room / Area list and make or update the patient’s room or area assignment. (Room or area information is mandatory; the waiting room is the application’s default selection.) Keyboard: use the \<Tab\> key to locate the Room / Area list, and use the \<Down Arrow\> and \<Up Arrow\> keys to select a room or area from the list.
13. Select an acuity value from the Acuity list. Acuity information is mandatory for this view. If you do not select an acuity, the application will not allow you to save your updates or edits. Keyboard: use the \<Tab\> key to locate the Acuity list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select an acuity.
5.  EDIS supports the Emergency Severity Index (ESI) triage algorithm, which ranks patients’ acuities using the numbers 1 (most urgent) through 5 (least urgent). Please visit the [Agency for Healthcare Research and Quality ESI](http://www.ahrq.gov/research/esi) Web site for more information.
14. Open the Status list and select the patient’s status. Keyboard: use the \<Tab\> key to locate the Status list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select a status from the list. (You can find a list of status definitions in [section 6.2.1](#status_definitions) of this guide.)
15. Select a provider from the Provider list. Keyboard: use the \<Tab\> key to locate the Provider list and use the \<Down Arrow\> and \<Up Arrow\> keys to select the patient’s provider assignment from the list. The Provider list is also available on the Update and Disposition views.
16. If the Resident list (controlled by a site-selectable parameter) is available, select a resident from the list. Keyboard: use the \<Tab\> key to locate the Resident list and use the \<Down Arrow\> and \<Up Arrow\> keys to select a resident from the list. If the Resident list is available on the Triage view, it is also available on the Update and Disposition views.
17. Select a nurse from the Nurse list. Keyboard: use the \<Tab\> key to locate the Nurse list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select a nurse from the list. The Nurse list is also available on the Update view.
11. When you make a provider assignment in EDIS, the application automatically creates a Patient Care Encounter (PCE) visit in CPRS—if it hasn’t already done so, or unless the provider does not have an active person class in VistA.  
      
    EDIS does not create visits for patients you’ve added using the Enter Name, Patient Is Not in VistA and Ambulance Is Arriving, Patient Name Is Unknown selections. It does not create visits when you enter only resident or nurse assignments. However, EDIS does create visits in CPRS for nurse assignments if the nurses in question are listed in VistA’s Provider file.  
      
    EDIS does not register patients.
18. If applicable, add or edit the patient’s source from the Source list. (Definitions for nationally released sources are available in [section 4.1.5](#source_definitions) of this guide.) Keyboard: use the \<Tab\> key to locate the Source list and use the \<DownArrow\> and \<Up Arrow\> keys to select a source from the list.
19. If the Clinic list is available, select the location that you want EDIS to use for creating the patient’s PCE visit. This list is controlled by site-selected parameters. If your site’s emergency department has only one location, or uses only one location at any given time, this list may not be available. The list is also unavailable if a PCE visit is already associated with the patient’s emergency-department episode of care.
20. Click Save to save your edits and updates or click Cancel to close the Patient Information pane without saving your changes. *The Save button is available only after you’ve added or updated information in the Patient Information pane.* Keyboard: use the \<Tab\> key to locate either the Save or Cancel button. Press the \<Spacebar\> key to select the button.

### Definitions for Status Selections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDIS TWG has provided the following definitions for nationally released status selections:

Admitted—the patient is admitted, but is still in the emergency department.

ED Boarding \[Hold\]—the patient is admitted and is designated as a holder (extended time in the emergency department).

Discharged—the patient is discharged, but is still in the emergency department.

ED Observation Unit—the patient is an observation patient under the emergency department’s care.

ED Patient—the patient is an emergency department patient (after triage).

En Route/Prearrival—the patient is en route to the emergency department.

Awaiting Triage—the patient is at the emergency department and is awaiting triage.

Other Status-list selections are site configurable.

## Create a Visit in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Adding a provider (or a nurse who has an active person class in the New Person file) in EDIS automatically creates a PCE visit in CPRS—*unless EDIS has already created a visit for this particular emergency-department episode of care (through Appointment Management, for example) or the provider does not have an active person class in VistA’s New Person file.* To reduce the possibility of creating duplicate PCE visits in CPRS, EDIS checks back one hour for PCE visit entries associated with the emergency department location your site’s IT staff has specified.

(EDPF LOCATION parameter settings and—if applicable—Clinic list selections determine the location EDIS uses to create visits.)

The application creates only one PCE visit in CPRS for each emergency-department episode of care (or encounter).You can avoid creating duplicate visits for the same episode of care by selecting the visit that EDIS creates when you complete patients’ emergency-department encounters in CPRS.

REDACTED

> Figure 17: Adding provider assignments in EDIS creates PCE visits in CPRS.

# Update View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Update view enables you to add or update the following information:

- Room or area assignments
- Patients’ statuses
- Provider assignments
- Resident assignments
- Nurse assignments
- Comments

![](emergency-dept-integration-software-edis-version-1-0-user-guide/023.png)

> Figure 18: The Update view.

## Add or Update Information in the Patient Information Pane

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click Update in the application’s left-hand menu bar. Keyboard: use the \<Tab\> key to locate the left-hand menu bar and use the \<Up Arrow\> or \<Down Arrow\> key to locate the Update view. Press the \<Spacebar\> key to select this view.
21. Select from the Active Patients list the patient whose information you want to edit or update. Keyboard: use the \<Tab\> key to locate the Active Patients list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select from the list the patient whose data you want to update.
22. In the Patient Information pane, select and edit the fields and staff assignments you want to update. Keyboard: use the \<Tab\> key to locate information fields. Use the \<Down Arrow\> and \<Up Arrow\> keys to select items from lists.
23. When you make a provider assignment in EDIS, the application automatically creates a PCE visit in CPRS—if it hasn’t already done so, or unless the provider does not have an active person class in VistA. EDIS does not create visits for patients you’ve added using the Enter Name, Patient Is Not in VistA or Ambulance Is Arriving, Patient Name Is Unknown selections.
6.  As a rule, EDIS requires you to enter a provider before allowing you to remove a patient from the board. Exceptions to this rule apply to the following dispositions: Patient Name Entered in Error, Left Without Being Treated/Seen, and Sent to Nurse Eval / Drop In Clinic.
24. Click Save to save your edits and updates or click Cancel to close the Patient Information pane without saving your changes. Keyboard: use the \<Tab\> key to locate the Save or Cancel button. Use the \<Spacebar\> key to select the button*. The Save button is available only after you’ve added or updated information in the Patient Information pane.*

## Create a Visit 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Adding a provider in EDIS automatically creates a PCE visit in CPRS—*unless EDIS has already created a PCE visit for this particular emergency-department episode of care, the patient hasn’t yet been identified in VistA, or the provider you assigned does not have a valid person class in VistA.* To reduce the possibility of creating duplicate visits, EDIS checks back one hour for PCE visit entries associated with the emergency department location you or your site’s IT staff have specified. (EDPF LOCATION parameter settings and—if applicable—Clinic list selections determine the location EDIS uses to create visits. The Clinic list is available on the Triage view.)

The application creates only one PCE visit in CPRS for each emergency-department episode of care (or encounter).You can avoid creating duplicate visits for the same episode of care by selecting the visit that EDIS creates when you complete patients’ emergency-department encounters in CPRS. EDIS displays a green checkmark in the DisplayBoard view’s Visit column to indicate that it has created a visit in CPRS.

### Setting a Primary Provider for Your Patient’s Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- When you select a physician from EDIS’s Provider list, the application sets the physician as the primary provider for your patient’s visit in CPRS. If you subsequently change the assigned physician in EDIS, EDIS assigns the new physician as the primary provider for the visit in CPRS. In this case, EDIS assigns the originally selected physician as a secondary provider.
- When you select a primary provider for the patient’s emergency-department visit in CPRS, EDIS updates its Provider selection to reflect this change.

# Disposition View 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Disposition view enables you to enter patients’ dispositions and either free-text or ICD-9-CM diagnoses, depending upon how your site sets the application’s parameters.

If your site has enabled coded diagnoses, entering a diagnosis in EDIS adds the diagnosis to the emergency-department visit EDIS creates in CPRS. Conversely, adding a diagnosis *forthe current emergency-department visit* in CPRS automatically adds the diagnosis in EDIS. (EDIS creates the visit when you select a provider in the Update or Triage view, or when you add a diagnosis in the Disposition view.) For example, a possible workflow for providers might include adding patients’ discharge diagnoses in CPRS when the providers are signing notes and completing EDIS-created encounters. In this workflow, EDIS would automatically update these patients’ diagnoses in its Disposition view.

Also depending on your site’s configuration, the Disposition view may require you to select a disposition or a delay reason (for patients whose emergency-department stays have exceeded your site’s specified time limit), or both. In addition, this view enables you to add or update provider and resident assignments, update room and area assignments, update patients’ statuses, and remove patients from the display board.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/024.png)

> Figure 19: Disposition view with ICD-9-CM diagnoses enabled.

## Select a Disposition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click Disposition on the left-hand menu pane. Keyboard: from the left-hand menu pane, use the \<Up Arrow\> or \<Down Arrow\> key to locate Disposition. Press the \<Spacebar\> key to select Disposition.
25. Select a patient in the Active Patients list. The application displays the Patient Information pane. Keyboard: use the \<Tab\> key to locate the Active Patients list. Use the \<Down Arrow \> and \<Up Arrow\> keys to select a patient from the list.
26. Open the Disposition list and select a disposition. Depending upon your site’s configuration, the application may require a disposition before allowing you to remove a patient from the display board. Keyboard: use the \<Tab\> key to locate the Disposition list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select a disposition from the list.
27. Click Save to save your changes or click Cancel to close the Patient Information pane without saving your changes. Keyboard: use the \<Tab\> key to locate the Save or Cancel button. Use the \<Spacebar\> key to select the button.
7.  The Save button is available only after you’ve added or updated information in the Disposition pane.

### Definitions for National Dispositions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDIS TWG offers the following definitions for nationally released dispositions:

Admitted to VA Ward—the patient was admitted to an inpatient location, *not* including an ICU, telemetry, or psychiatric unit.

AMA—the patient left against medical advice *after signing a form*; the patient may or may not have been medically evaluated before leaving.

Sent to Urgent Care Clinic—the patient was discharged from the emergency department and referred to another evaluation clinic at the same site; some degree of triage is necessary to make this judgment.

Deceased—the patient is dead.

Eloped—the patient left the emergency department and his or her disposition is unknown; a nurse or physician may have seen and evaluated the patient.

Patient Name Entered in Error—the patient’s name was entered in error; this disposition removes the patient from the board.

Home—the patient was discharged to his or her previous living arrangement.

Admitted to ICU—the patient was admitted to an inpatient critical care unit.

Left Without Being Treated/Seen—the patient left the emergency department before receiving treatment *and before signing the form;* this is not the same as AMA, which assumes the patient signed a form before leaving.

Sent to Nurse Eval / Drop-in Clinic—the patient was discharged from the emergency department and referred to another on-campus *same-day* evaluation clinic; some degree of triage is necessary to make this judgment.

Admitted to Psychiatry—the patient was admitted to an inpatient psychiatric unit.

Admitted to Telemetry—the patient was admitted to an inpatient telemetry unit.

Transferred to a Non-VA Facility—the patient was discharged from the emergency department and sent to another, non-VA, facility.

Transferred to VA Facility—the patient was discharged from the emergency department and sent to another VA facility.

Sites can activate and inactivate these dispositions. The application allows your site to configure additional, site-specific dispositions.

8.  To capture admission-delay times for reporting, you must change patients’ statuses to Admitted and then immediately select Admitted to VA Ward as their dispositions. Unless you intend to remove patients from the board, click Save. Do not click Save & Remove from Board, which will prematurely remove your patients from the EDIS tracking application.

## Select a Reason for Delay

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- If the Delay Reason list is available, open it and select a reason for delay. Depending upon your site’s configuration, the application may require a reason for delay when patients’ emergency-department visits have exceeded a specified number of minutes. Keyboard: use the \<Tab\> key to locate the Delay Reason list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select a delay reason from the list. The Delay Reason list is available only under the following conditions:
  - Your site requires a delay reason *and*
  - The patient’s stay has exceeded the site-determined limit *and*
  - The patient is not in an observation ward
- Click Save to save your changes or Cancel to close the Patient Information pane without saving your changes. Keyboard: use the \<Tab\> key to locate the Save or Cancel button. Use the \<Spacebar\> key to select the button.
9.  If your site requires a reason for delay and the patient’s stay has exceeded the maximum number of minutes your site has specified, the application will require you to enter a delay reason before it allows you to remove the patient from the display board.

### Definitions for National Reason-for-Delay Selections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDIS TWG offers the following definitions for nationally released reason-for-delay selections. Your site is not required to include all selections in its pick list. EDIS test sites recommend limiting pick lists to reasons that are relevant at your site because over-long lists affect compliance.

Obtain Accepting Physician—the delay was caused by the inability to find an accepting physician to admit the patient. This selection includes the elapsed time between determining the patient’s need for admission and obtaining an accepting physician.

Admit Physician Writing Dispo—the delay resulted from the physician’s failure to write the patient’s admit or discharge order. This selection includes the elapsed time between when the patient was ready for his or her disposition and when the physician wrote the order to admit or discharge the patient.

Admitting Physician Evaluation—the delay was related to the admitting physician’s evaluation and confirmation of the patient’s disposition. For this selection, delay time begins when the physician sees the patient and ends when:

- H&P is done
- Ancillary studies that are necessary for disposing the patient are done and resulted
- The patient is ready to be disposed

Patient Admitted to Observation—the delay resulted from the patient’s admission to observation. This selection includes the elapsed time between when the patient was ready to be disposed and the time the physician wrote an order to admit the patient to 23 hours of emergency department or floor observation.

Obtain Ambulance Services—the delay resulted from the time it took to obtain ambulance services. This selection includes the elapsed time between when emergency department staff requested ambulance services and the time the ambulance arrived.

Obtain Consultant—the delay resulted from an ordered consultation’s lack of completion. This selection includes the elapsed time from when a physician ordered a consultation to the time the physician obtained the consultation.

ED to Hospital Bed—the delay represents the difference between the time the patient was assigned a hospital bed and the time the patient was transported from the emergency department; for example, this delay could represent the time emergency department staff spent waiting for an escort, for a bed to be cleaned, for a nursing report, or for staffing.

Obtain Escort—the delay resulted from the time it took to obtain an escort for the purpose of transporting the patient *(not including transport to a hospital bed—use ED to Hospital Bed for this reason)*. This selection includes the time that elapsed between when the emergency department called an escort and the time the escort arrived to transport the patient to a clinic, radiology, or another ancillary department.

Patient Transport Home—the delay resulted from an inability to find transportation for a discharged patient or the time it took the identified source of transportation to arrive at the emergency department. This selection includes the elapsed time between when the patient was ready for discharge and the time the patient left the emergency department.

Obtain Imaging Results—the delay resulted from time spent waiting to obtain imaging results. This selection includes the elapsed time between when the imaging study was completed and the time the study was resulted.

Obtain Imaging Studies—the delay resulted from time spent waiting for imaging studies. This selection includes the elapsed time between when the physician ordered the imaging study and the time the study was done and ready for interpretation.

Obtain Inpatient Bed—the delay resulted from the time spent waiting for an impatient bed assignment. This selection includes the elapsed time between when the physician wrote the admission order and the time bed control or the house supervisor assigned the patient to a bed—the time an ICU patient waited for an ICU bed to open up, for example.

Interfacility Transfer—the delay was caused by an inability to transfer the patient to another facility in a timely manner.

Obtain Lab Results—the delay was caused by the lack of a timely turnaround for laboratory tests. This selection includes the elapsed time between when labs were drawn or obtained and the time the labs were resulted.

Obtain Lab Studies—the delay was caused by an inability to get labs drawn in a timely fashion. This selection includes the elapsed time between when the physician wrote the lab order and the time the lab test was drawn.

On-call Staff—the delay was caused by an inability to contact on-call staff.

Overcrowding of ED—the delay resulted from waiting for an emergency department bed to become available (includes hallway beds and beds that were unavailable because of staffing issues); no beds were available for inbound ambulances, including hallway beds.

Obtain Drugs/Pharmacology—the delay was caused by an inability to get ordered drugs from the pharmacy. This selection includes the elapsed time between when the physician ordered the medications and the time the emergency department received the medications.

ED Physician Limits—the delay resulted from time the physician spent seeing patients. This selection includes the elapsed time between when the patient was placed in a bed and when the physician saw the patient. For example, this reason for delay might apply if five patients presented with chest pains, all within 10 minutes.

ED Staff Limits—the delay resulted from a failure to process the patient (see the patient or accomplish orders, for example) in a timely manner because of insufficient staffing. This selection includes the elapsed time between when the physician wrote an order (to splint a broken ankle, for example) and the time the order was accomplished.

Obtain Medical Supplies—the delay resulted from an inability to obtain medical supplies (splints, crutches, and c-line kits, for example) in a timely manner. This selection includes elapsed time from when emergency department personnel ordered the supplies (or identified the need for them) and the time the emergency department received the supplies.

Arrange Emergency Surgery—the delay resulted from the time it took to get the patient (who needed surgery) to the operating room.

Patient Transport Other—the delay resulted from the time it took to find transportation for the patient to a location other than home. This selection includes the elapsed time between when the patient was ready for transport and the time the patient left the emergency department.

## Enter ICD-9-CM Diagnoses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Type a diagnosis in the Diagnosis search box and click Search or press the \<Enter\> key. The application lists possible matches from VistA’s ICD-9-CM code base. Keyboard: use the \<Tab\> key to locate the Diagnosis search box. Type a diagnosis in the box and press the \<Enter\> key.
22. Select an ICD-9-CM diagnosis from the Diagnosis search list and click Add or press the \<Enter\> key. The application adds this diagnosis to the Selected Diagnoses list. Keyboard: use the \<Down Arrow\> and \<Up Arrow\> keys to locate the diagnosis you want to select. Press the \<Enter\> key to select the diagnosis. To select another diagnosis from the same search list, use the \<Tab\> key to reenter the list. Use the \<Down Arrow\> and \<Up Arrow\> keys to locate the additional diagnosis, and press the \<Enter\> key to select this diagnosis. You can also select diagnoses by using the \<Tab\> key to locate the Add button, then pressing the \<Spacebar\> key to select the button.
23. To remove a diagnosis from the Selected Diagnoses list, select the diagnosis and click Remove or press the \<Delete\> key. Keyboard: use the \<Tab\> key to locate the Selected Diagnoses list. Use the \<Down Arrow\> and \<Up Arrow\> keys to locate the diagnosis you want to remove. Press the \<Delete\> key to remove the diagnosis. You can also simultaneously press the \<Shift\> and \<Tab\> keys to locate the Remove button, and then press the \<Spacebar\> key to remove the selected diagnosis.
24. Repeat steps 1–3 as needed.
25. In the Selected Diagnoses list, select a primary diagnosis and click Set as Primary Diagnosis. Keyboard: in the Selected Diagnoses list, use the \<Down Arrow\> and \<Up Arrow\> keys to locate the primary diagnosis. Use the \<Tab\> key to locate the Set as Primary Diagnosis button, and use the \<Spacebar\> key to select this button.
26. Click Save to save your changes or Cancel to close the Patient Information pane without saving your changes. Keyboard: use the \<Tab\> key to locate the Save or Cancel button. Use the \<Spacebar\> key to select the button.
10. Saving an ICD-9-CM diagnosis in EDIS adds the diagnosis to the patient’s emergency-department visit in CPRS. If EDIS hasn’t already created a PCE visit for this patient, it will also create a visit at this time. The application does not add free-text diagnoses to the patient’s visit in CPRS.

## Enter Free-Text Diagnoses 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can type in free-text diagnoses only if your site has set the parameter that enables you to do so.

1.  Type a diagnosis or procedure in the Diagnosis box and click Add or press the \<Enter\> key. Keyboard: use the \<Tab\> key to locate the Diagnosis box. Type a diagnosis in the box and press the \<Enter\> key. You can also press the \<Tab\> key to locate the Add button and press the \<Spacebar\> key to select the button. The application displays your diagnosis or procedure in the Selected Diagnoses list.
2.  To remove an item from the SelectedDiagnoses list, select the item and click Remove or press the \<Delete\> key. Keyboard: use the \<Tab\> key to locate the SelectedDiagnoses list and use the \<Down Arrow\> and \<Up Arrow\> keys to locate and select the diagnosis you want to remove. Use the \<Delete\> key to remove the diagnosis. You can also remove the diagnosis by simultaneously pressing the \<Shift\> and \<Tab\> keys to locate the Remove button, then pressing the \<Spacebar\> key to select the button.
3.  Repeat steps 1–2 as needed.
4.  In the Selected Diagnoses list, choose a primary diagnosis, then click Set as Primary Diagnosis. Keyboard: use the \<Tab\> key to enter the Selected Diagnoses list and the \<Down Arrow\> and \<Up Arrow\> keys to locate the primary diagnosis. Use the \<Tab\> key to locate the Set as Primary Diagnosis button and use the \<Spacebar\> key to select it.
5.  Click Save to save your changes or click Cancel to close the Patient Information pane without saving your changes. Keyboard: use the \<Tab\> key to locate the Save or Cancel button. Use the \<Spacebar\> key to select the button.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/025.png)

> Figure 20: The Disposition view with free-text diagnoses enabled.

## Remove Patients 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Click the Save & Remove from Board button to save changes and remove patients from the display board. Keyboard: use the \<Tab\> key to locate the Save & Remove from Board button. Use the \<Spacebar\> key to select the button.

> This button is available only after users have entered all of the disposition information your site’s EDIS implementation requires. If you haven’t entered a provider or acuity, the application alerts you to do these things before it allows you to save your changes and remove your patient from the board—unless your patient’s disposition is Patient Name Entered in Error, Left Without Being Treated / Seen, or Sent to Nurse Eval / Drop In Clinic.

> Clicking the Save & Remove from Board button removes patients from the display board and saves previously unsaved changes. While the application retains information about the visits of patients you’ve removed from the display board, only users who have access to the Edit Closed view will have direct access to this information. Users who have access to the Reports view will have indirect access to this information.

## Remove Patients Entered in Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Open the Disposition list. Keyboard: use the \<Tab\> key to locate the Disposition list.
28. Select Patient Name Entered in Error. Keyboard: use the \<Down Arrow\> key to select Patient Name Entered in Error.
29. Click Save & Remove from Board. Keyboard: use the \<Tab\> key to locate the Save & Remove from Board button and press the \<Spacebar\> key to select it.

# Edit Closed View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This view enables authorized users to edit the EDIS records of patients who are no longer on the display board. EDIS logs all changes for subsequent reference (as it does with changes users make while patients are still signed in to the emergency department). If your site uses PCE instead of Appointment Management, the Edit Closed view provides a lookup tool; you can use this view to search for specific patients who visited your emergency department on a specific date.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/026.png)

> Figure 21: The Edit Closed view.

1.  Click Edit Closed on EDIS’s left-hand navigation menu. Keyboard: use the \<Tab\> key to locate the left-hand menu. Use the \<Down Arrow\> or \<Up Arrow\> key to locate Edit Closed. Press the \<Spacebar\> key to select Edit Closed.
2.  Type a date (mm/dd/yy format) or all or part of the patient’s name (Surname, First name format) in the Patient Name or Date box. For example, you can type the patient’s surname initial, entire surname, or surname and first-name initial. You can also type the patient’s full SSN, the initial letter of the patient’s surname concatenated with the last four digits of his or her SSN (X9999 format), the word *today* (for a list of today’s visits), or t-n ( where *t* represents today, and *n* represents the number of days prior to today). Keyboard: use the \<Tab\> key to locate the Patient Name or Date box.
3.  Click Search or press the \<Enter\> key. EDIS lists possible matches in the search-results list.
4.  Select from this list the patient whose record you want to update. EDIS displays the Patient Information pane, which contains information about the selected patient’s emergency department visit. Keyboard: use the \<Tab\> key to locate the search-results list. Use the \<Down Arrow\> key to enter the list and the \<DownArrow\> and \<Up Arrow\> keys to select the patient whose record you want to update.
5.  To identify a previously unidentified patient, click Identify Patient in the Patient Information bar. EDIS displays the Add Patient dialog box. Keyboard: use the \<Tab\> key to locate the Identify Patient button and use the \<Spacebar\> key to select it.
6.  The Add Patient dialog offers two ways to identify patients: Search for Patient in VistA and Enter Name, Patient Is Not in VistA. Search for Patient in VistA is the application’s default selection. To search for the patient in VistA, type all or part of the patient’s name in the Find Patient box (Surname,Firstname format) and either click Search or press the \<Enter\> key. You may also type the patient’s full SSN, the last four digits of the patient’s SSN, or the initial letter of the patient’s surname concatenated with the last four digits of his or her SSN (X9999 format). EDIS displays a list of possible matches.
7.  Select the patient’s name and click Continue. Keyboard: use the \<Down Arrow\> and \<Up Arrow\> keys to locate the patient’s name. Press the \<Enter\> key to select the name.
    1.  If the patient is not included in the list, select Enter Name, Patient Is Not in VistA. EDIS displays the Patient Name box. Keyboard: use the \<Tab\> key to locate the Search for Patient in VistA button, then use the \<Down Arrow\> key to locate the EnterName, Patient Is Not in VistA button. Press the \<Spacebar\> key to select this button.
    2.  Type the patient’s name in the Patient Name box and click Continue. Keyboard: use the \<Tab\> key to locate the Continue button and use the \<Spacebar\> key to select this button.
8.  Add or update other data-entry fields as necessary. You can add information to, or update, the following fields: Complaint for Display Board, Long Complaint (optional), Room / Area, Acuity, Status, Provider, Resident, Nurse, Comments, Source, Disposition, Delay Reason, Selected Diagnoses, Time In, and Time Out. (Click the Time In or Time Out spin-box arrows or use the \<Up Arrow\> and \<Down Arrow\> keys to edit the patient’s time in or time out.)
9.  Click Save to save your changes or click Cancel to discard them. Keyboard: use the \<Tab\> key to locate the Save or Cancel button and use the \<Spacebar\> key to select the button of your choice.
11. If you attempt to change the time out value (or other value) for a patient who left the emergency department before he or she was seen, EDIS will not allow you to save your change until you add a provider name.
12. The Save button is available only after you’ve added or updated information in the Patient Information pane. The application allows you to save your changes only if all required data fields contain valid entries.

# Display Board View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your site can configure one or more display boards, depending on its needs. The Display Board view offers a PC- or workstation-based preview of your site’s main electronic whiteboard display configuration. If you have access to this view, you can customize it as you would any other grid-based view:

- Arrange columns
- Resize columns
- Sort within columns

See the “[Work with Data Grids](#work_with_grids)” section of this document for information about how to arrange, resize, and sort within columns.

2.  Sorting information within columns in the PC-based Display Board view does not cause EDIS to similarly sort information in large electronic (LCD) whiteboard display columns. EDIS sorts large display columns first in the order of the rooms and areas listed in the Room / Area configuration subview and then in the order of patients’ acuities.

You cannot save layout changes you make from within this view. Further, the changes you make appear only on your local machine (as opposed to the large display). To request permanent changes in the display-board view, please contact the person who configures EDIS for your site (usually an IRM or CAC staff member).

![](emergency-dept-integration-software-edis-version-1-0-user-guide/027.png)

> Figure 22: The Display Board view.

## Viewing the Display Board

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PC-based Display Board view contains only the columns your site has selected for its main display board. Following is a list of the columns from which your site can choose:

Room / Bed: patients’ locations

Clinic: the emergency department’s clinic locations

Patient Name: patients’ display names

Patient X9999: an alternative way to display patients’ names (the first letter of patients’ surnames concatenated with the last four digits of their Social Security numbers)

Visit Created: a check box that indicates whether or not EDIS has created a PCE visit in CPRS

Comment: optional comments

Complaint: patients’ display-board complaints

Provider Initials: providers’ initials

Resident Initials: residents’ initials

Nurse Initials: nurses’ initials

Acuity: patients’ acuities

Status: patients’ statuses

Lab Active/Complete: the total number of patients’ active laboratory orders relative to the total number of their completed laboratory orders

Imaging Active/Complete: the total number of patients’ active imaging orders relative to the total number of their completed imaging orders

New (Unverified) Orders: patients’ unverified orders (values decrement when nurses verify the orders in CPRS and when ancillary services \[lab and imaging\] complete the orders)

Total Minutes: the total number of minutes that patients have been in the emergency department

Minutes at Location: the total number of minutes that patients have been in their present locations

13. EDIS displays information only for laboratory, imaging, and new orders that are associated with patients’ current emergency-department visits.

# Assign Staff View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This view allows authorized users to add staff names to—and remove them from—pick lists that are available in the Triage, Update, Disposition, and Edit Closed views. You can also configure text and background colors for staff assignments.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/028.png)

> Figure 23: The Assign Staff view.

## Add Providers, Residents, and Nurses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Type the name of a physician, resident, or nurse in the view’s Providers, Residents, or Nurses search box, respectively. EDIS displays a list of possible matches from your local VistA system. (Nurse search lists are based on your site’s EDPF NURSE STAFF SCREEN parameter setting.) Keyboard: use the \<Tab\> key to locate the Providers, Residents, or Nurses search box.
30. Select the name of the physician, resident, or nurse you want to add and click Add or press the \<Enter\> key. EDIS adds the name to the Provider, Resident, or Nurse list, respectively. Keyboard: use the \<Down Arrow\> key to enter the search list. Use the \<Down Arrow\> and \<Up Arrow\> keys to locate the name of the physician, resident, or nurse you want to add. Press the \<Enter\> key to add this name.
31. Click Save Staff Changes to save your additions. Keyboard: use the \<Tab\> key to locate Save Staff Changes and use the \<Spacebar\> key to select it.

## Remove Providers, Residents, and Nurses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In the Provider,Resident, or Nurse list, select the physician, resident, or nurse whose name you want to remove. Keyboard: use the \<Tab\> key to locate the Provider, Resident, or Nurse list. Use the \<Down Arrow\> and \<Up Arrow\> keys to locate the name of the provider, resident, or nurse you want to remove.
2.  Click Remove or press the \<Delete\> key.
32. Click Save Staff Changes to save your changes. Keyboard: use the \<Tab\> key to locate the Save Staff Changes button and use the \<Spacebar\> key to select the button.

## Configure Colors for Providers, Residents, and Nurses 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application allows you to configure text and background colors for providers, residents, and nurses.

1.  Select a physician, resident, or nurse in the Provider,Resident, or Nurse list. EDIS displays the Use Color check box. Keyboard: use the \<Tab\> key to locate the Provider,Resident, or Nurse list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select a name from the list.
33. Select the Use Color check box. Keyboard: use the \<Tab\> key to locate the Use Color check box and use the \<Spacebar\> key to select it.
34. To configure a color for text, click the color-selection box labeled Text. EDIS displays a color-selection grid ( ![](emergency-dept-integration-software-edis-version-1-0-user-guide/029.png) ). Click a color in the grid to select a text color. Keyboard actions are not available for this step.
35. To configure a background color, click the color-selection box labeled Back. EDIS displays a color-selection grid. Click a color in the grid to select a background color. Keyboard actions are not available for this step.
36. Click Save Staff Changes to save your color selections. Keyboard: use the \<Tab\> key to locate the Save Staff Changes button and use the \<Spacebar\> key to select it.
14. Colors you configure for staff assignments will not appear on the display board unless colors (in general) are enabled for staff assignments in the Configuration view’s Display Board subview.

# Reports View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS can control access to the Reports view in several ways. For example, the application can deny access (in which case you don’t see the Reports selection on the application’s left-hand menu). It can also enable you to run and view eleven standard reports, and allow you to print reports and export them for use in spreadsheet applications such as Microsoft Excel. (Sites control user access to EDIS’s export feature via the EDPR EXPORT security key. Sites also use security keys to control access to two restricted reports.)

## Eleven Standard Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Column Headings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS’s eleven standard reports are data grids that include one or more of the following columns:

- IEN: the EDIS internal entry number
- Time In: the time at which an EDIS user identified and added the patient, or the time at which an Appointment Management user created an emergency-department appointment for the patient
- Time Out: the time at which an EDIS user closed the patient’s emergency department visit
- Complaint: the patient’s display-board complaint
- MD: the initials of the patient’s physician
- Acuity: the patient’s acuity level
- Elapsed: total elapsed time (from the patient’s time in to his or her time out, in minutes; asterisks indicate stays that have exceeded the current nationally recognized stay limit of 360 minutes)
- Triage: the elapsed time between the patient’s time in and his or her initial acuity assessment
- Wait: the elapsed time between the patient’s time in and his or her first assignment to a location other than the waiting room
- Disposition (Dispo): the patient’s disposition
- Admission Decision (Adm Dec): the elapsed time between the patient’s time in and the request for an inpatient bed (this value requires a disposition of Admitted to VA Ward or Admitted to ICU)
- Admission Delay (Adm Delay): the elapsed time between the patient’s Time Out (the time the patient was removed from the board) and the time of the patient’s first admitting-disposition assignment
- Diagnosis: the patient’s diagnosis
- ICD9: the patient’s ICD-9-CM diagnosis

#### Disposition Abbreviations

The EDIS TWG provided the following abbreviations for nationally released dispositions; EDIS reports use these abbreviations when space is limited:

| VA  | Admitted to VA Ward                  |
|-----|--------------------------------------|
| AMA | AMA                                  |
| CL  | Sent to Clinic                       |
| D   | Deceased                             |
| E   | Eloped                               |
| ERR | Patient Name Entered in Error        |
| H   | Home                                 |
| ICU | Admitted to ICU                      |
| L   | Left Without Being Treated/Seen      |
| NEC | Sent to Evaluation / Same-Day Clinic |
| PSY | Admitted to Psychiatry               |
| T   | Admitted to Telemetry                |
| NVA | Transferred to Non-VA Facility       |
| O   | Transferred to VA Facility           |

### Standard Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](emergency-dept-integration-software-edis-version-1-0-user-guide/030.png)

> Figure 24: The Reports view list of eleven standard reports.

Activity Report: for each patient whose visit falls within the date and-time range you select, this report lists available information in the following columns:

- IEN
- Time In
- Time Out
- Complaint
- MD
- Acuity
- Elapsed
- Triage
- Wait
- Disposition (Dispo)
- Admission Decision (Adm Dec)
- Admission Delay (Adm Delay)
- Diagnosis
- ICD9

In addition, this report provides averages for several important time-based measurements (Admission Decision,Admission Delay, Elapsed, Wait, and Triage) in several patient categories:

- All patients
- All patients who were admitted
- All patients who were not admitted
- All patients in each of the following disposition categories: Deceased (D), Eloped (E), Patient Name Entered in Error (ERR), Home (H), Admitted to ICU (ICU), Left Without Being Treated/Seen (L), Sent to Nurse Eval / Drop In Clinic (NEC), Transferred to non-VA Facility (NVA), Admitted to Psychiatry (PSY), Admitted to Telemetry (T), and Admitted to VA Ward (VA).

![](emergency-dept-integration-software-edis-version-1-0-user-guide/031.png)

> Figure 25: The Activity report. Print functionality is enabled for users who receive the Reports view.

Acuity Report: this report displays statistics that measure patient workload for each acuity level. For the date-and-time range you select, statistics show the number of patients who fell into each acuity category, the number of patients in each category who were admitted, and the number in each category who were admitted to a VA facility. The Acuity report also provides the following average times for patients in each acuity category:

- Admission Decision (all facilities)
- Admission Decision (VA facilities)
- Admission Delay (VA facilities)
12. Test sites found that this report times out for date ranges that cover a large number of visits (1,400 visits within a one-month range, for example). They recommend clicking Continue and toggling between the Display Board and Reports views to get data from extended time ranges.

Also, if your site’s process results in a number of patients whom you’ve removed from the board using the Patient Name Entered in Error selection, you should correct the report’s total number of patients by subtracting the number of patients who were entered in error.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/032.png)

> Figure 26: The Acuity report.

Delay Report: this report presents information about patients whose emergency department stays exceeded the nationally recognized limit (six hours or 360 minutes). For each patient whose stay exceeded this limit, the Delay report displays available information in the following columns:

- IEN
- Time In
- Elapsed
- Disposition
- Delay Reason
- MD
- Admission Decision (Adm Dec)
- Admission Delay (Adm Delay)
- Acuity
- Diagnosis

![](emergency-dept-integration-software-edis-version-1-0-user-guide/033.png)

> Figure 27: The Delay report.

15. EDIS does not include in its Delay and Delay Summary reports patients whose emergency-department visits are not yet closed—regardless of the number of hours their visits have consumed.

Delay Summary Report: this report presents average visit and decision-to-admit times (and other important information) for the following three visit categories:

- All emergency department visits
- All visits that resulted in VA-facility admissions
- All visits that did not result in VA-facility admissions

This report also presents acuity-based tallies for each applicable reason for delay.

Again, if your site’s process results in a number of patients whom you’ve removed from the board using the Patient Name Entered in Error selection, you should subtract this number from the report’s total number of visits and from visits that didn’t result in VA-facility admissions.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/034.png)

> Figure 28: The Delay Summary report.

ED BVAC Patients: the ED BVAC (Emergency Department Behavioral VA Care) Patients report captures the following information for behavioral-health patients:

- Time In
- Time Out
- Complaint
- MD
- Acuity
- Elapsed
- Triage
- Disposition
- Admission Decision (Adm Dec)
- Admission Delay (Adm Delay)
- Diagnosis
- ICD9 (ICD-9-CM codes for this report are greater than 290 and less than 316)

This report also provides service-related information such as whether or not the patient is a Vietnam veteran, has been exposed to Agent Orange, has a VA pension, and so forth.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/035.png)

> Figure 29: The ED BVAC Patients report.

Exposure Report: this report identifies patients and staff who may have been in the emergency department when a contagious patient was present for treatment. To run the report, you enter the internal entry number (IEN) from the contagious patient’s Visit file (#9000010). EDIS then uses information in this file to compile lists of all patients and staff who were in the emergency department during the time of the contagious patient’s visit.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/036.png)

> Figure 30: The Exposure report.

Missed Opportunities Report: this report displays the following information about patients whose dispositions are AMA (left against medical advice), L (left without being treated or seen), or E (eloped):

- IEN
- Time In
- Complaint
- MD
- Acuity
- Elapsed
- Triage
- Wait
- Disposition
- Admission Decision (Adm Dec)

If your site assigns a nurse to left-without-being-seen (LWBS) callbacks, the nurse must either have access to the Xref report or the application’s Edit Closed view (to search for LWBS patients by Time In values).

![](emergency-dept-integration-software-edis-version-1-0-user-guide/037.png)

> Figure 31: The Missed Opportunities report.

Orders by Acuity: for each acuity, this report tallies the number of medication, laboratory, imaging, consultation, and other orders emergency-department personnel placed during the date-and-time range you specify.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/038.png)

> Figure 32: The Orders by Acuity report.

Patient Intake Report: the Patient Intake report provides time-of-day and day-of-week statistics regarding the number of patients who visited the emergency department during the date and time range you enter.

Columns contain day-of-week tallies cover the entire time-and-date range against which you run the report. For example, if the date range you enter includes two Tuesdays, the intersection of the Tue column and the 0700-0800 row displays the total number of patients who visited the emergency department on both Tuesdays between the hours of 7:00 a.m. and 8:00 a.m. The Total column contains a sum of all day-based totals across each time-based row. For example, in the 0700-0800 row, the Total column contains a sum of daily totals from the Sun through Sat columns.

For each time-based row, the Avg/Day column presents an average that is based on the figure in the Total column and the total number of days in the date range you select. For example, if your date range is January 1, 2009 through January 31, 2009, the total number of days (the denominator) will be 31.

The report’s Avg/Hour row contains an average that is based on the total number of visits in each day-based column divided by the total number of hours for each day in the search range you select. For example, in the Sun column, the application calculates the following average: the total number of Sunday visits (the value in the Total row, Sun column) divided by 24 (the number of hours in a day) multiplied by the number of Sundays in the date range you select.

16. The Patient Intake report does not include maximum, minimum, and mean calculations.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/039.png)

> Figure 33: The Patient Intake report.

Shift Report: this report is limited to one day of reporting and presents a shift-based calculation of the following data categories:

- Carried over at Report Start
- Number of New Patients
- Number of Patients Discharged
- Number Dec (Decision) to Admit to VA
- Number Dec (Decision) to Admit to Other
- Number over Six Hours
- Number Waiting for Triage
- Number of Occupied Beds
- Number of Missed Opportunities
- Number Deceased
- Number With No Disposition
- Carry over to Next Shift

![](emergency-dept-integration-software-edis-version-1-0-user-guide/040.png)

> Figure 34: The Shift report.

VA Admissions Report: this report uses Disposition selections to identify patients who were admitted to VA facilities (VA wards, intensive care units \[ICUs\], telemetry, and observation wards, for example) during the time-and-date range you specify.

The report contains available information in the following columns:

- IEN
- Time Out
- Complaint
- MD
- Acuity
- Disposition
- Adm Dec (Admission Decision)
- Adm (Admission) Delay
- Diagnoses
- ICD9

The report also provides averages for patients who fall into each applicable VA-admission category.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/041.png)

> Figure 35: The VA Admissions report.

### Cross Reference and Provider Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS also provides two restricted-access reports: the Patient XRef (Cross Reference) and Provider reports. Because these two reports contain personally identifying information, you need special security keys (in VistA) to access and run them

XREF: this report provides a cross reference between the EDIS IEN and patient identifiers (including patients’ surname initials concatenated with the last four digits of their SSNs).

![](emergency-dept-integration-software-edis-version-1-0-user-guide/042.png)

> Figure 36: The Patient XRef (Cross Reference) report.

Provider: The Provider report lists the total number of patients each provider saw during the date and time range you specify. It also provides a by-shift and by-acuity count of patients, the time between each patient's emergency-department time in and his or her diagnosis, and the time between each patient’s provider assignment and his or her disposition.

13. If the Provider report’s MD Assign to Dispo(sition) column contains only zeros, your site probably doesn’t require providers to enter a disposition before releasing patients.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/043.png)

> Figure 37: The Provider report.

## Run and View Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select Reports on the application’s left-hand menu bar. Keyboard: use the \<Tab\> key to locate the left-hand menu bar. Use the \<Up Arrow\> or \<Down Arrow\> key to locate Reports. Use the \<Spacebar\> key to select Reports.
37. Select a report from the Report list. Keyboard: use the \<Tab\> key to locate the Report list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select a report from the list.
38. Click the Calendar icon (![](emergency-dept-integration-software-edis-version-1-0-user-guide/044.png)) and select a starting date for your report or type a starting date in the Start Date box using this format: mm/dd/yyyy. (The application automatically formats shorter dates. For example, if you type 8/8/09, the application reformats the date as 08/08/2009.) Keyboard: use the \<Tab\> key to locate the Start Date box.
39. Select a starting time in the Start Time box (![](emergency-dept-integration-software-edis-version-1-0-user-guide/045.png)). Keyboard: use the \<Tab\> key to locate the hour selector in the Start Time box. Select a start-time hour using the \<Down Arrow\> and \<Up Arrow\> keys. Use the \<Tab\> key to locate the minutes selector in the Start Time box. Use the \<Down Arrow\> and \<Up Arrow\> keys to select start-time minutes.
40. If you are running the Exposure report, type the contagious patient’s IEN in the visit IEN box. The Exposure report does not require a date range.
41. Click the Calendar icon in the Stop Date area and select a stop date for your report or type a stop date in the Stop Date box. Keyboard: use the \<Tab\> key to locate the Stop Date box. The Shift and Exposure reports do not require stop dates.
42. Select a stop time in the Stop Time box. Keyboard: use the \<Tab\> key to locate the hour selector in the Stop Time box. Use the \<Down Arrow\> and \<Up Arrow\> keys to select an hour. Use the \<Tab\> key to locate the minutes selector in the Stop Time box. Use the \<Down Arrow\> and \<Up Arrow\> keys to select stop-time minutes.
43. Click Run Report. Keyboard: use the \<Tab\> key to locate the Run Report button and use the \<Spacebar\> key to select the button.
14. If your reports contain negative numbers, the problem could lie with logic that EDIS’s reports functionality inherited from the class-three Syracuse application. Syracuse reporting logic assumes that users will enter information in a certain sequence. For example, the application assumes that users will assign a provider before entering a patient’s disposition. To calculate the time that elapsed between a patient’s provider assignment and disposition, the application subtracts provider-entry time from disposition-entry time. If users assign providers after they’ve entered dispositions, reports such as the Provider report will contain negative numbers.  
      
    Negative numbers can also be a result of not-so-careful data entry. For example, suppose a patient’s stay began on July 10 at 11:00 p.m. and ended on July 11 at 1:00 a.m. Further, suppose someone mistakenly removed this patient from the board at 11:55 p.m. When correcting this error, if the user corrects the patient’s time-out hour-and-minute value, but neglects to update the date value, the patient’s time-out value will be chronologically before his or her time-in value, and EDIS will calculate the patient’s stay at -22 hours.
15. When reports exceed your application window’s viewing capacity, the application includes a scroll bar, as it does in the following screen capture:

REDACTED

### Print Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To print a report, click Print. The Print button is in the upper right-hand corner of the Reports view. Keyboard: use the \<Tab\> key to locate the Print button and use the \<Spacebar\> key to select it. The application displays your operating system’s print dialog.

### Export Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click Export. If you are authorized to export reports, you’ll find this link in the upper right-hand corner of the Reports view. Keyboard: use the \<Tab\> key to locate Export and use the \<Spacebar\> key to select it.
2.  In the Select location for download by dialog box, select a location for your exported report. Keyboard: use the \<Tab\> key to locate the Save in selector. Use the \<Down Arrow\> and \<Up Arrow\> keys to find a location for your exported report. Press the \<Enter\> key to select the location.
3.  In the File name box, type a name for your exported report. Keyboard: use the \<Tab\> key to locate the File name box. *If you want to export the report as an Excel spreadsheet, append the .xls extension before saving.*
4.  Click Save. Keyboard: use the \<Tab\> key to locate the Save button and use the \<Spacebar\> key to select it.
5.  The application displays a message informing you that your download is complete. Click Close to dismiss the message. Keyboard: use the \<Spacebar\> key to select the Close button.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/046.png)

> Figure 39: Exported Activity report in Microsoft Excel.

# Configure View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This view allows authorized users to create customized big-board (usually large LED or plasma) displays and configure the application to include locally meaningful pick lists. Specifically, the view provides subviews that allow you to configure:

- Room and area selections
- Status, disposition, delay-reason, and source selections
- Display-board options
- Colors
- Parameters

## Room and Area Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Room / Area subview enables you to:

- Add or configure rooms and areas
- Specify display names for rooms and areas
- Determine when the display board displays rooms and areas
- Select a default status for patients who occupy specific rooms or areas
- Mark rooms or areas inactive
- Select the occupancy category into which rooms and areas fall (multiple patient, single patient, and so forth)
- Indicate areas that contain two or more beds (for exposure reports)
- Specify the electronic white-board display on which rooms and areas appear
- Configure background and text colors for rooms and areas

### Add, Configure, and Edit Rooms and Areas

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](emergency-dept-integration-software-edis-version-1-0-user-guide/047.png)

> Figure 40: The Configure view—Room / Area subview.

1.  Select the Room / Area subview. Keyboard: use the \<Tab\> key to locate the left-hand view-selection menu. Use the \<Down Arrow\> and \<Up Arrow\> keys to locate the Configure view. Use the \<Spacebar\> key to select this view. Use the \<Tab\> key to locate the Room / Area subview and use the \<Spacebar\> or \<Enter\> key to select it.
4.  Click Add Room/Area. The application displays the Room / Area Edit pane and adds a new placeholder row in the Rooms / Areas grid. Keyboard: use the \<Tab\> key to locate the Add Room/Area button and use the \<Spacebar\> key to select it.
5.  To edit an existing room or area, click the room or area in the Rooms / Areas grid. Keyboard: use the \<Tab\> key to locate the Rooms / Areas grid. Use the \<Down Arrow\> key to enter the grid, and use the \<Down Arrow\> and \<Up Arrow\> keys to select a room or area.
27. In the Name box (Edit pane), replace the application’s placeholder name (new1) with the name of the room you want to add. *The application does not support duplicate room or area names.* Keyboard: use the \<Tab\> key to locate the Name box.
28. In the Display Name box, replace the placeholder name (new1) with the name you want EDIS to display. Keyboard: use the \<Tab\> key to locate the Display Name box. *The application does not support duplicate display names for rooms and areas.*
29. Select one of the following three options from the Display When list: Occupied, Always, or Never. Your selection determines when EDIS displays the room or area on the large electronic whiteboard display. Keyboard: use the \<Tab\> key to locate the Display When list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select an option from this list.
30. To configure a default status for patients who are assigned to the new room (optional), select a status from the Default Status list. (Sites can configure their own selections for this list.) Keyboard: use the \<Tab\> key to locate the Default Status list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select a default status from the list.
31. If the new room or area is currently inactive, select the Inactive? checkbox. Keyboard: use the \<Tab\> key to locate the Inactive? checkbox. Use the \<Spacebar\> key to select (or cancel the selection of) the Inactive? checkbox.
32. From the Category list, select the occupancy category into which the room or area falls. Keyboard: use the \<Tab\> key to locate the Category list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select an occupancy category from the list.
33. If a room or area contains two or more beds, type in the Shared Name box a name that associates the beds. For example, if area OBS contains two beds, OBS-1 and OBS-2, configure a room or area for each bed and type OBS in the Shared Name box for both OBS-1 and OBS-2. Keyboard: use the \<Tab\> key to locate the Shared Name box.
34. If your site uses more than one large electronic whiteboard display, type in the UseBoard box the name of the display board on which the room or area will appear. All patients appear on the application’s main electronic whiteboard display. Keyboard: use the \<Tab\> key to locate the UseBoard box.
35. Select the Use Color check box to configure a text and/or background color for the room or area. (Optional. See section 13.1.1.1, “Configuring Color for Rooms and Areas.”)
36. To dismiss the Edit pane and view all columns in the Rooms / Areas grid, click All Columns. Keyboard: use the \<Tab\> key to locate the All Columns button and use the \<Spacebar\> key to select it.
37. Click Save Room / Area Changes to save your changes. The application displays a message that tells you it has successfully saved your changes. Click Close to dismiss this message. Keyboard: use the \<Tab\> key to locate the Save Room / Area Changes button. Use the \<Spacebar\> key to select the Save Room / Area Changes button. Use the \<Tab\> key to locate the Close button, use the \<Spacebar\> key to select the Close button.

#### Configuring Colors for Rooms and Areas

The application allows you to configure text and background colors for rooms and areas.

1.  Select the Use Color checkbox. Keyboard: use the \<Tab\> key to locate the Use Color check box. Use the \<Spacebar\> key to select (or cancel the selection of) this check box.
2.  To configure a color for text, click the color-selection box labeled Text. EDIS displays a color-selection grid ( ![](emergency-dept-integration-software-edis-version-1-0-user-guide/048.png) ). Click a color in the grid to select it as a text color. General keyboard actions are not available for this step; however, JAWS users can type hexadecimal color codes for text.
3.  To configure a background color, click the color-selection box labeled Back. EDIS displays a color-selection grid. Click a color in the grid to select it as a background color. General keyboard actions are not available for this step; however, JAWS users can type hexadecimal color codes for backgrounds.
4.  Click Save Room / Area Changes to save your color selections. Keyboard: use the \<Tab\> key to locate the Save Room / Area Changes button and use the \<Spacebar\> key to select it.
16. [![](emergency-dept-integration-software-edis-version-1-0-user-guide/049.png)](http://www.google.com/imgres?imgurl=http://www.shingleberrysigns.com/design_icon/warning%25201.gif&imgrefurl=http://www.shingleberrysigns.com/design_a_sign.php&usg=__wZUf1BihAcvMKNvqvpQGCx7UNtM=&h=1247&w=1413&sz=23&hl=en&start=3&sig2=6o6B87g3UKWHWxoCjJwZWQ&um=1&itbs=1&tbnid=_VZGtdgK3Q6_5M:&tbnh=132&tbnw=150&prev=/images%3Fq%3Dwarning%26um%3D1%26hl%3Den%26safe%3Dactive%26sa%3DN%26tbs%3Disch:1&ei=gscYTMqpDcqNnQedre2dCg)Colors you configure for room and area assignments will not appear on the display board unless colors (in general) are enabled for room and area selections in the Configuration view’s Display Board subview.

#### Specifying the Order of Rooms and Areas

Use a drag and drop operation to change the order of rooms and areas in the Rooms / Areas grid. EDIS bases the order of its Room / Area selection lists on the order of rooms and areas in the Rooms / Areas grid. Keyboard actions are not available for drag-and-drop operations.

## Display Board Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](emergency-dept-integration-software-edis-version-1-0-user-guide/050.png)

> Figure 41: The Configure view—Display Board subview.

The Display Board subview enables you to:

- Add a new large electronic whiteboard display
- Add or remove display-board columns
- Edit column headers
- Identify information upon which you want to base cell colors in display-board columns
- Identify information upon which you want to base colors in display-board rows
- Reposition and resize display-board columns
- Select optimal display sizes
- Configure the display’s font size and scroll-delay time
- Compress (squish) all data rows into a single, no-scroll view (if possible)

EDIS enables you to configure each display board separately. Simply select the board you want to configure in the Board Name list. The application displays editable information about the board in the Board Properties pane.

### Add a New Display Board

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDIS enables you to create multiple large electronic whiteboard displays. However, be advised: *you cannot delete display boards after you’ve saved them.*

1.  Click Add Board. EDIS adds a placeholder name (new1) in the Board Name list and the Board Name box, which is located in the Board Properties pane. Keyboard: use the \<Tab \> key to locate the Add Board button and use the \<Spacebar\> key to select the button.
38. In the Board Name box, replace the placeholder name with the name you want to use for this new display board. Each display board must have a unique name. Keyboard: use the \<Tab\> key to locate the Board Name box.
39. (Optional) In the Row Color Based On list, select a display-board item upon which you want to base row colors. Keyboard: use the \<Tab\> key to locate the Row Color Based On list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select an item from the list.
40. In the Display Size list, select the screen size of your display board. Display sizes are site configurable. If the Display Size list does not contain your new board’s screen size, ask your site’s CAC or IRM staff to add the size in VistA. Keyboard: use the \<Tab\> key to locate the Display Size list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select a display size from the list.
41. In the Font Size spin box, type or select a font size for your new display board. Available font sizes range from six to 36 points. The Preview Display Board pane dynamically displays your font choices. Keyboard: use the \<Tab\> key to locate the Font Size box. Type a font size, or use the \<Down Arrow\> and \<Up Arrow\> keys to select a font size.
42. (Optional) Select the Squish Rows To Fit (if possible) check box. This selection allows EDIS to compress all data rows to completely fit within your site’s display screen, if this is possible. To ensure readability, the application compresses data only down to a row size of 18 points and a font size of nine points. *If, after applying the maximum compression, your site’s data will still not fit within a single display view, the application applies scrolling functionality and restores the display board’s font size to the value in the Font Size spin box.* Keyboard: use the \<Tab\> key to locate the Squish (if possible) checkbox. Use the \<Spacebar\> key to select—or cancel the selection of—the checkbox.
43. In the Scroll Delay spin box, type or select a scroll-delay time (in seconds). The application automatically activates scrolling when the screen’s real estate is not sufficient to display all of the patients who are currently on the Active Patients list. The delay-time setting determines how long screen contents remain stationary. For example, suppose your display can accommodate only 20 patients and 25 patients are currently on the list. Further, suppose that the EDIS scroll-delay time is set at five seconds. In this case, EDIS displays the first 20 patients for five seconds, then scrolls to display the remaining five patients for five seconds, and so forth. Keyboard: use the \<Tab\> key to locate the Scroll Delay box. Type a delay time or use the \<Up Arrow\> and \<Down Arrow\> keys to select a delay time.
17. EDIS refreshes the display board every 30 seconds. Each refresh resets the display-board view. Set scroll-delay intervals that allow the application to display all patients within the span of a single refresh cycle. (JAWS users can disable automatic refresh functionality and manually refresh the display board by pressing the \<F7\> key. However, automatic refresh is disabled only when JAWS is running.)

### Add Display Board Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Display boards can include any of the following columns:

- Room / Bed: the rooms, beds, and areas associated with the display board
- Patient Name: the patients’ surnames
- Patient X9999: the first initials of the patients’ surnames concatenated with the last four digits of their Social Security numbers
- Visit Created: checkmarks that indicate EDIS has created visits for the patients in CPRS or blank spaces that indicate EDIS has not created visits
- Complaint: the patients’ display-board complaints
- Comments: comments users have entered via the Update view
- Provider Initials: the initials of the providers users have selected via the Triage, Update, or Disposition views
- Resident Initials: the initials of the residents users have selected via the Triage , Update, or Disposition views
- Nurse Initials: the initials of the nurses users have selected via the Triage and Update views
- Acuity: the acuities users have entered via the Triage view
- Status: the statuses users have entered via the Update and Disposition views
- Lab Active/Complete: the number of active laboratory orders associated with the patients’ emergency-department visits over the number of completed laboratory orders
- Imaging Active/Complete: the number of active imaging orders associated with the patients’ emergency-department visits over the number of completed imaging orders
- New (Unverified) Orders: the number of unverified orders associated with the patients’ emergency-department visits (for sites using CPRS 26, EDIS decrements this number when unverified orders are completed; for sites using CPRS 27, EDIS decrements this number when unverified orders are verified)
- Total Minutes: the number of minutes from patients’ time-in values (the times users added patients to—or identified them in—EDIS) to the present
- Minutes at Location: the number of minutes patients have been assigned to their present locations

![](emergency-dept-integration-software-edis-version-1-0-user-guide/051.png)

> Figure 42: The Add Column list.

1.  Click to open the Add Column list. Keyboard: use the \<Tab\> key to locate the Add Column list. Press the \<Spacebar\> key to open the list.
6.  Click to select a column name from the Add Column list. The Preview Display Board pane dynamically displays columns as you add them. Keyboard: use the \<Down Arrow\> and \<Up Arrow\> keys to locate the name of the column you want to add. Use the \<Spacebar\> or \<Enter\> key to select the column.
44. Repeat steps 1 and 2 as necessary. Keyboard: the application maintains its focus on the Add Column list, so you won’t need to locate the Add Column list t anew with each new column addition. Simply press the \<Spacebar\> key to reopen the list.
18. After you add columns, you can specify their order using a drag-and-drop operation (see Section 13.2.4, “Specify the Order of Display Board Columns”). Keyboard operations are not available for post-addition column ordering. If you exclusively use keyboard actions, please add columns in the order in which you want them to appear on your large electronic whiteboard display.

### Configure or Edit Display Board Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In the Selected Columns list, click the column whose properties you want to configure or edit. Keyboard: use the \<Tab\> key to locate the Selected Columns list. Use the \<Down Arrow\> key to enter the list. Use the \<Down Arrow\> and \<Up Arrow\> keys to locate the column you want to configure.
45. In the Header box, which is located in the Column Properties pane, replace the application’s default or current header (optional). Keyboard: use the \<Tab\> key to locate the Header box.
46. Select an item in the Color Based On list (optional). Your selection here determines the criteria the application uses to display color configurations in big-board display columns. *The application gives preference to colors you configure for columns over colors you configure for rows.* List items include: Status / Acuity, Status, Acuity, Room / Bed, Provider, Resident, Nurse, Urgency – Lab, Urgency – Radiology, Total Elapsed Minutes, Minutes at Location, Minutes for Lab Order, Minutes for Imaging Order, and Minutes for Unverified Order.
19. Although you configure color selections in the Assign Staff view and the Colors and Room / Area subviews, the Display Board subview of the Configuration view is where you determine which of these colors the board displays and where it displays them.

    Your selection determines which color or colors appear on the display board for the column you’ve selected. For example, suppose you select the Status column. Then suppose you click this column’s Color Based On list and select Acuity. In this case, the board will display in its Status column colors you have configured for acuity.

### Specify the Order of Display Board Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can specify the order of large electronic whiteboard display columns by using a drag-and-drop operation in either the Preview Display Board pane or the Selected Columns list.

To perform a drag-and-drop operation, click a column header and, without releasing your mouse button, move the header to its new location. Release the mouse button. Keyboard actions are not available for drag-and-drop operations. To reorder columns using your keyboard, remove columns in the Selected Columns list and re-add them in the order in which you want them to appear on the display.

### Resize Display Board Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You resize columns in the Preview Display Board pane by using a drag-and-drop operation (keyboard actions are not available):

1.  Point your mouse at the border of the column you want to resize.
47. When your mouse pointer becomes a slider ( ![](emergency-dept-integration-software-edis-version-1-0-user-guide/052.png) ) hold down your right mouse button and drag the boarder to resize the column.
48. Release your mouse button.

### Remove Display Board Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can remove columns from the Selected Columns list in any of the following ways:

- Remove a single column: click an individual column in the Selected Columns list and press the \<Delete\> key. Keyboard: use the \<Tab\> key to locate the Selected Columns list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select the column you want to remove. Press the \<Delete\> key to remove the column.
- Remove a group of columns: select a group of columns in the Selected Columns list by clicking the first column in the group, then pressing and holding down the \<Ctrl\> key as you click the remaining columns. Release the \<Ctrl\> key and press the \<Delete\> key to remove the group. Keyboard: use the \<Tab\> key to locate the Selected Columns list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select the first column in the group. Press and hold down the \<Ctrl\> key while using the \<Down Arrow\> and \<Up Arrow\> keys to locate additional columns in the group. Press the \<Spacebar\> key to select each of these columns. Release the \<Ctrl\> key and press the \<Delete\> key to delete the group.
- Remove a range of columns: select a range of columns in the Selected Columns list by clicking the first column in the range, then pressing and holding down the \<Shift\> key as you click the last column. Release the \<Shift\> key and press the \<Delete\> key to remove the range. Keyboard: use the \<Tab\> key to locate the Selected Columns list. Use the \<Up Arrow\> and \<Down Arrow\> keys to locate the first column in the range. Press and hold down the \<Shift\> key while using the \<Up Arrow\> or \<Down Arrow\> key to select the remaining columns in the range. Release the \<Shift\> key and press the \<Delete\> key to remove the range.

### Save Display Board Configuration Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click Save Display Board Changes. EDIS displays an Alert message to confirm that it has successfully saved your changes. Click Close to dismiss this message. Keyboard: use the \<Tab\> key to locate the Save Display Board Changes button. Press the \<Spacebar\> key to select the button. Use the \<Tab\> key to locate the Close button, and use the \<Spacebar\> key to select it.

## Configure Colors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](emergency-dept-integration-software-edis-version-1-0-user-guide/053.png)

> Figure 43: The Configure view—Colors subview, Status / Acuity selected.

The Colors subview enables you to configure colors for the following items:

- Status / Acuity
- Status
- Acuity
- Urgency – Lab
- Urgency – Radiology
- Total Elapsed Minutes
- Minutes at Location
- Minutes for Lab Order
- Minutes for Imaging Order
- Minutes for Unverified Order

You can configure colors for rooms and areas on the Room / Area subview. Configure colors for emergency-department staff on the Assign Staff view.

### Configure Colors (General Instructions)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](emergency-dept-integration-software-edis-version-1-0-user-guide/054.png)

> Figure 44: The Use Color check box

You can configure colors for any tracking item for which EDIS displays the Use Color check box:

1.  Select the Use Color checkbox. The application displays the Text and Back color-selection boxes. Keyboard: use the \<Tab\> key to locate the Use Color check box. Use the \<Spacebar\> key to select it.
7.  To configure a text color, click the Text box. The application displays the color-selection grid (![](emergency-dept-integration-software-edis-version-1-0-user-guide/055.png)). Click a color within the grid to select it as the text color. Keyboard actions are not available for this step; however, JAWS users may type in a hexadecimal color code.
8.  To configure a background color, click the Back box. EDIS displays the color-selection grid. Click a color within the grid to select it as the background color. Keyboard actions are not available for this step; however JAWS users may type in a hexadecimal color code.

### Configure Colors for Status and Acuity Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can configure colors for all status values. The following initial values ship with the application:

- Admitted
- Awaiting Triage
- ED Boarding \[Hold\]
- ED Observation Unit
- ED Patient
- En Route/Prearrival
- Discharged

You can also configure colors for the following acuity values. (The application supports Emergency Severity Index \[ESI\] acuity values.)

- 1 (most urgent)
- 2
- 3
- 4
- 5 (least urgent)

In addition, you can use the Status / Acuity selection to configure colors for the combined set of these status and acuity values.

20. Color-map selections in the Colors subview must match at least one color selection in the Display Board subview. For example, if you configure colors for the Status / Acuity selection in the Colors subview, select Status / Acuity in the Colors Based On column or Row Color list in the Display Board subview. Also note: if you configure colors for the Status/Acuity selection and also for the Acuity and/or Status selections, the application will display the colors you configured for Status / Acuity.
1.  In the Available Color Maps list, select Status, Acuity, or Status / Acuity. EDIS displays the Colors for Status, Colors for Acuity, or Colors for Status / Acuity grid, respectively. Keyboard: use the \<Tab\> key to locate the Available Color Maps list. Use the \<Down Arrow\> or \<Up Arrow\> keys to select Status / Acuity, Status, or Acuity.
9.  To configure colors for a value listed in the corresponding grid, select the value. Keyboard: use the \<Tab\> key to locate the grid. Use the \<Down Arrow\> and \<Up Arrow\> keys to select a value within the grid.
10. Click the Use Color checkbox and follow the instructions in Section 13.3.1 [“Configure Colors (General Instructions).”](#colors_general) Keyboard: use the \<Tab\> key to locate the Use Color check box. Use the \<Spacebar\> key to select the check box.
11. Repeat steps 1–3 to configure colors for additional values.
12. Click Save Color Changes to save your color configurations. The application displays an Alert message to inform you that it has saved your color selections. Click Close to dismiss this message. Keyboard: use the \<Tab\> key to locate Save Color Changes and use the \<Spacebar\> key to select it. Use the \<Tab\> key to locate the Close button and use the \<Spacebar\> key to select it.

### Configure Colors for Urgency – Lab Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](emergency-dept-integration-software-edis-version-1-0-user-guide/056.png)

> Figure 45: The Colors for Urgency - Lab grid.

You can configure colors for the following values:

- No Orders
- Active Orders
- STAT Orders
1.  In the Available Color Maps list, select Urgency - Lab. EDIS displays the Colors for Urgency - Lab grid. Keyboard: use the \<Tab\> key to locate the Available Color Maps list. Use the \<Down Arrow\> key to enter the list, and use the \<Down Arrow\> or \<Up Arrow\> keys to locate Urgency – Lab.
13. To configure colors for a value listed in the grid, select the value, then select the Use Color check box. Keyboard: use the \<Tab\> key to locate the Urgency – Lab grid. Use the \<Down Arrow\> and \<Up Arrow\> keys to select a value in the grid. Use the \<Tab\> key to locate the Use Color checkbox, and use the \<Spacebar\> key to select it.
14. Follow the steps in Section 13.3.1 “[Configure Colors (General Instructions)](#colors_general)” to configure colors for the value.
15. Repeat steps 1–3 to configure colors for additional values.
16. Click Save Color Changes to save your color configurations. The application displays an Alert message to inform you that it has saved your color selections. Click Close to dismiss this message. Keyboard: use the \<Tab\> key to locate Save Color Changes and use the \<Spacebar\> key to select it. Use the \<Tab\> key to locate the Close button and use the \<Spacebar\> key to select it.

### Configure Colors for Urgency – Radiology Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can configure colors for the following values:

- No Orders
- Active Orders
- STAT Orders

![](emergency-dept-integration-software-edis-version-1-0-user-guide/057.png)

> Figure 46: Colors for Urgency – Radiology grid.

1.  In the Available Color Maps list, select Urgency - Radiology. EDIS displays the Colors for Urgency – Radiology grid. Keyboard: use the \<Tab\> key to locate the Available Color Maps list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select Urgency – Radiology.
17. To configure colors for a value listed in the Colors for Urgency – Radiology grid, select the value, then select the Use Color checkbox. Keyboard: use the \<Tab\> key to locate the Colors for Urgency – Radiology grid. Use the \<Down Arrow\> and \<Up Arrow\> keys to select a value. Use the \<Tab\> key to locate the Use Color checkbox and use the \<Spacebar\> key to select it.
18. Follow the steps in Section 13.3.1 “[Configure Colors (General Instructions)](#colors_general)” to configure colors for the value.
19. Repeat steps 1–3 to configure colors for additional values.
20. Click Save Color Changes to save your color configurations. The application displays an Alert message to inform you that it has saved your color selections. Click Close to dismiss this message. Keyboard: use the \<Tab\> key to locate Save Color Changes and use the \<Spacebar\> key to select it. Use the \<Tab\> key to locate the Close button and use the \<Spacebar\> key to select it.

### Configure Colors for Total Elapsed Minutes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application measures total elapsed minutes from patients’ Time In values.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/058.png)

> Figure 47: Configure colors for Total Elapsed Minutes selection.

1.  Select Total Elapsed Minutes in the Available Color Maps list. The application displays the Colors for Total Elapsed Minutes grid. Keyboard: use the \<Tab\> key to locate the Available Color Maps list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select Total Elapsed Minutes.
49. To add a time value to the Starting at Elapsed Minute column, click Add. The application displays the Starting at Elapsed Minute box. Keyboard: use the \<Tab\> key to locate the Add button and use the \<Spacebar\> key to select it.
50. Type a starting value in the Starting at Elapsed Minute box. EDIS uses this value to determine when to display your color configuration. Keyboard: use the \<Tab\> key to locate the Starting at Elapsed Minute box.
51. To associate a color with this value, select the Use Color checkbox and follow the steps in Section 13.3.1 “[Configure Colors (General Instructions)](#colors_general).”
52. Repeat steps 1 through 4 to configure colors for additional Starting at… minutes as necessary.
53. Click Save Color Changes to save your color configurations. The application displays an Alert message to inform you that it has saved your color selections. Click Close to dismiss this message. Keyboard: use the \<Tab\> key to locate Save Color Changes and use the \<Spacebar\> key to select it. Use the \<Tab\> key to locate the Close button and use the \<Spacebar\> key to select it.

### Configure Colors for Minutes at Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The application measures elapsed times from patients’ most recent room assignments.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/059.png)

> Figure 48: The Colors for Minutes at Location grid.

1.  Select Minutes at Location in the Available Color Maps list. The application displays the Colors for Minutes at Location grid. Keyboard: use the \<Tab\> key to locate the Available Color Maps list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select Minutes at Location.
54. To add a time value to the Starting at Elapsed Minute column, click Add. The application displays the Starting at Elapsed Minute box. Keyboard: use the \<Tab\> key to locate the Add button.
55. Type a starting value in the Starting at Elapsed Minute box. Keyboard: use the \<Tab\> key to locate the Starting at Elapsed Minute box.
56. To associate a color with this value, select the Use Color checkbox and follow the steps in Section 13.3.1 “[Configure Colors (General Instructions)](#colors_general).”
57. Repeat steps 1 through 4 to configure colors for additional Starting at… values as necessary.
58. Click Save Color Changes to save your color configurations. The application displays an Alert message to inform you that it has saved your color selections. Click Close to dismiss this message. Keyboard: use the \<Tab\> key to locate Save Color Changes and use the \<Spacebar\> key to select it. Use the \<Tab\> key to locate the Close button and use the \<Spacebar\> key to select it.

### Configure Colors for Minutes for Lab Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Values measure times from when orders were released to the laboratory.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/060.png)

> Figure 49: The Colors for Minutes for Lab Order grid.

1.  Select Minutes for Lab Order in the Available Color Maps list. The application displays the Colors for Minutes for Lab Order grid. Keyboard: use the \<Tab\> key to locate the Available Color Maps list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select Minutes for Lab Order.
59. To add a time value to the Starting at Elapsed Minute column, click Add. The application displays the Starting at Elapsed Minute box. Keyboard: use the \<Tab\> key to locate the Add button.
60. Type a starting value in the Starting at Elapsed Minute box. Keyboard: use the \<Tab\> key to locate the Starting at Elapsed Minute box.
61. To associate a color with this value, select the Use Color checkbox and follow the steps in Section 13.3.1 “[Configure Colors (General Instructions)](#colors_general).”
62. Repeat steps 1 through 4 to configure colors for additional starting-at minutes as necessary.
63. Click Save Color Changes to save your color configurations. The application displays an Alert message to inform you that it has saved your color selections. Click Close to dismiss this message. Keyboard: use the \<Tab\> key to locate Save Color Changes and use the \<Spacebar\> key to select it. Use the \<Tab\> key to locate the Close button and use the \<Spacebar\> key to select it.

### Configure Colors for Minutes for Imaging Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Values measure time from when orders are released to radiology.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/061.png)

> Figure 50: The Colors for Minutes for Imaging Order grid.

1.  Select Minutes for Imaging Order in the Available Color Maps list. The application displays the Colors for Minutes for Imaging Order grid. Keyboard: use the \<Tab\> key to locate the Available Color Maps list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select Minutes for Imaging Order.
64. To add a time value to the Starting at Elapsed Minute column, click Add. The application displays the Starting at Elapsed Minute box. Keyboard: use the \<Tab\> key to locate the Add button and use the \<Spacebar\> key to select the button.
65. Type a starting value in the Starting at Elapsed Minute box. Keyboard: use the \<Tab\> key to locate the Starting at Elapsed Minute box.
66. To associate a color with this value, select the Use Color checkbox and follow the steps in Section 13.3.1 “[Configure Colors (General Instructions)](#colors_general).”
67. Repeat steps 1 through 4 to configure colors for additional Starting at… values as necessary.
68. Click Save Color Changes to save your color configurations. The application displays an Alert message to inform you that it has saved your color selections. Click Close to dismiss this message. Keyboard: use the \<Tab\> key to locate Save Color Changes and use the \<Spacebar\> key to select it. Use the \<Tab\> key to locate the Close button and use the \<Spacebar\> key to select it.

### Configure Colors for Minutes for Unverified Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Values measure time from when orders are released.

![](emergency-dept-integration-software-edis-version-1-0-user-guide/062.png)

> Figure 51: The Colors for Minutes for Unverified Order grid.

1.  Select Minutes for Unverified Order in the Available Color Maps list. The application displays the Colors for Minutes for Unverified Orders grid. Keyboard: use the \<Tab\> key to locate the Available Color Maps list. Use the \<Down Arrow\> and \<Up Arrow\> keys to select Minutes for Unverified Order.
69. To add a time value to the Starting at Elapsed Minute column, click Add. The application displays the Starting at Elapsed Minute box. Keyboard: use the \<Tab\> key to locate the Add button and press the \<Spacebar\> key to select it.
70. Type a starting value in the Starting at Elapsed Minute box. Keyboard: use the \<Tab\> key to locate the Starting at Elapsed Minute box.
71. To associate a color with this value, select the Use Color checkbox and follow the steps in Section 13.3.1 “[Configure Colors (General Instructions)](#colors_general).”
72. Repeat steps 1 through 4 to configure colors for additional Starting at… values as necessary.
73. Click Save Color Changes to save your color configurations. The application displays an Alert message to inform you that it has saved your color selections. Click Close to dismiss this message. Keyboard: use the \<Tab\> key to locate Save Color Changes and use the \<Spacebar\> key to select it. Use the \<Tab\> key to locate the Close button and use the \<Spacebar\> key to select it.

## Configure Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](emergency-dept-integration-software-edis-version-1-0-user-guide/063.png)

> Figure 52: The Configure view—Parameters subview.

The Parameters subview allows you to set the following parameters:

- Show residents on entry form—This parameter enables sites that have residents to include them on the application’s data entry form. Fields for making and editing resident selections are available on the Triage, Update, Disposition, and Edit Closed views.
- Diagnosis is required before removing a patient—When sites select this parameter, EDIS requires emergency-department personnel to enter diagnoses as a precondition to removing patients from the display board—unless the patient’s disposition is one of the following: Patient Name Entered in Error,Left Without Being Treated/Seen, or Sent to Nurse Eval / Drop In Clinic.
- Diagnosis must be coded as ICD—When sites select this parameter, the application uses VistA’s ICD-9-CM search for all diagnosis entries. When sites do not select this parameter, the application uses a free-text field to record diagnoses.
- Disposition is required before removing patient—When sites select this parameter, the application requires emergency department personnel to enter dispositions before removing patients from the display board.
- Delay reason is required for visits exceeding \[site-specified\] minutes—When sites select this parameter, the application does not allow users to remove patients whose stays have exceeded a specific number of minutes without first entering a reason for delay—except when the patient’s disposition indicates that he or she has been assigned to an observation ward.
- Arriving Ambulance Room/Area is—This parameter enables sites to select a default room or area for patients who are arriving by ambulance or other emergency-transport vehicles.
- Default Room/Area is—This parameter enables sites to select a default room or area.

The Parameters subview also enables sites to specify shift start times and durations. The application uses this information to pull data for shift reports.

### Include Residents on Entry Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Select the Show residents on entry form checkbox. Keyboard: use the \<Tab\> key to locate the Show residents on entry form checkbox. Use the \<Spacebar\> key to select the checkbox.
- Clear the checkbox to remove the resident-selection list from the entry form. Keyboard: use the \<Spacebar\> key to clear the checkbox.

### Require a Diagnosis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Select the Diagnosis is required before removing patient checkbox. Keyboard: use the \<Tab\> key to locate the Diagnosis is required before removing patient checkbox. Use the \<Spacebar\> key to select the checkbox.
- Clear the checkbox to remove the requirement. Keyboard: use the \<Spacebar\> key to clear the checkbox.

### Require ICD-9-CM or Free Text Diagnoses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- To require ICD-9-CM diagnoses, select the Diagnosis must be coded as ICD checkbox. Keyboard: use the \<Tab\> key to locate the Diagnosis must be coded as ICD checkbox. Use the \<Spacebar\> key to select the checkbox.
- To require free-text diagnoses, do not select—or clear the selection of—the Diagnosis must be coded as ICD checkbox. Keyboard: use the \<Spacebar\> key to clear the selection of the checkbox.

### Require Disposition to Remove Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Select the Disposition is required before removing patient checkbox. Keyboard: use the \<Tab\> key to locate the Disposition is required before removing patient checkbox. Use the \<Spacebar\> key to select the checkbox.
- To remove the requirement, clear the checkbox. Keyboard: use the \<Spacebar\> key to clear the checkbox.

### Require a Reason for Delay

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Select the Delay reason is required for visits exceeding …minutes checkbox. In the minutes box, type or select a number of minutes after which the application should require a reason for delay. Keyboard: use the \<Tab\> key to locate the Delay reason is required for visits exceeding…minutes checkbox. Use the \<Spacebar\> key to select the checkbox. Use the \<Tab\> key to locate the minutes box. Type a number of minutes or use the \<Up Arrow\> or \<Down Arrow\> key to select a number of minutes.
21. The national visit limit for emergency departments is currently six hours (360 minutes).
- Clear the checkbox to remove the requirement. Keyboard: use the \<Spacebar\> key to clear the checkbox.

### Configure Shift Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- In the First shift begins at box, type the time (in hours and minutes—hh:mm) your site’s first shift begins. Keyboard: use the \<Tab\> key to locate the First shift begins at box.
- In the Shift duration is…hours and minutes boxes, type or select the hours and minutes that mark the duration of your site’s shifts. Keyboard: use the \<Tab\> key to locate the Shift duration is…hours and minutes boxes. Type hours and minutes or use the \<Up Arrow\> or \<Down Arrow\> key to select hours and minutes.

### Set a Default Room or Area for Patients Arriving by Ambulance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a room or area from the Arriving Ambulance Room/Area is list. Keyboard: use the \<Tab\> key to locate the Arriving Ambulance Room/Area is list. Use the \<Up Arrow\> or \<Down Arrow\> key to select a default room or area from the list.

### Set a Default Room or Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a room or area from the Default Room/Area is list. Keyboard: use the \<Tab\> key to locate the Default Room/Areais list. Use the \<Up Arrow\> or \<Down Arrow\> key to select a default room or area from the list.

### Save Parameter Selections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click Save Parameter Changes. The application displays an Alert message to inform you that it has successfully saved your changes. Click Close to dismiss this message. Keyboard: use the \<Tab\> key to locate the Save Parameter Changes button. Use the \<Spacebar\> key to select the button. Use the \<Tab\> key to locate the Close button and use the \<Spacebar\> key to select it.

Some parameter settings require you to log out of the application and log back in. For example, if you select the Diagnosis must be coded as ICD checkbox, you must log out and log back in to see the change on the application’s Disposition view. Likewise, after selecting the Show residents on entry form checkbox, you must log out and log back in to see resident lists on the application’s Update view.

## Add Choices to Selection Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](emergency-dept-integration-software-edis-version-1-0-user-guide/064.png)

> Figure 53: Configure view—Selections subview.

> The Selections subview enables you to add locally meaningful choices to selection lists that ship with EDIS. Specifically, you can add selections to the following lists:

- Status: the application ships with the following statuses:
  - Admitted
  - Awaiting Triage
  - Discharged
  - ED Boarding \[Hold\]
  - ED Observation Unit
  - ED Patient
  - En Route/Prearrival
- Disposition: the application ships with the following dispositions:
  - Admitted to VA Ward
  - Admitted to Telemetry
  - Admitted to ICU
  - Admitted to Psychiatry
  - Home
  - AMA (left against medical advice)
  - Left Without Being Treated/Seen
  - Eloped
  - Transferred to VA Facility
  - Transferred to non-VA Facility
  - Deceased
  - Sent to Nurse Eval / Drop In Clinic
  - Sent to Urgent Care Clinic
  - Patient Name Entered in Error
- Delay Reason: the application ships with the following reasons for delay:
  - Obtain Inpatient Bed
  - ED to Hospital Bed
  - Obtain Imaging Results
  - Obtain Imaging Studies
  - Obtain Drugs/Pharmacology
  - Obtain Lab Results
  - Obtain Lab Studies
  - Obtain Medical Supplies
  - Arrange Emergency Surgery
  - Obtain Consultant
  - On-call Staff
  - Patient Transport Home
  - Overcrowding of ED
  - Patient Transport Other
  - Obtain Accepting Physician
  - Obtain Escort
  - Admitting Physician Evaluation
  - Admit Physician Writing Dispo
  - Patient Admitted to Observation
  - ED Staff Limits
  - ED Physician Limits
  - Interfacility Transfer
  - Obtain Ambulance Services
- Source: the application ships with the following sources:
  - Non-referred
  - On-site Clinic
  - On-site Nursing Home
  - VA Clinic, Off-site
  - VA Nursing Home, Off-site
  - Non-VA Clinic/Office
  - Non-VA Nursing Home
  - Transfer, Other

The EDIS technical working group (TWG) and technical advisory group (TAG) have vetted these default lists. When sites add selections, the application denotes them by displaying the word *local* in the subview’s National Name column.

### Add Status, Disposition, Delay Reason, and Source Selections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select Status, Disposition, Delay Reason, or Source in the Selection List. The application displays the Selections for Status, Selections for Disposition, Selections for Delay Reason, or Selections for Source grid, respectively. (Definitions for nationally released sources are available in [section 4.1.5](#source_definitions) of this guide; definitions for nationally released statuses are available in [section 6.2.1](#status_definitions); definitions for nationally released dispositions are available in [section 8.1.1](#_Definitions_for_National); and definitions for nationally released delay reasons are available in [section 8.2.1](#_Definitions_for_National_).) Keyboard: use the \<Tab\> key to locate the Selection List. Use the \<Down Arrow\> and \<Up Arrow\> keys to select Status, Disposition, Delay Reason, or Source.
74. Click Add. The application displays the Edit Selection Item pane. Keyboard: use the \<Tab\> key to locate the Add button and use the \<Spacebar\> key to select the button.
75. In the Name box (Edit Selection Item pane), type a name for the selection you want to add. Keyboard: use the \<Tab\> key to locate the Name box.
76. In the Abbreviation box , type an abbreviation for the item you want to add. EDIS uses this abbreviation for its large electronic whiteboard display. Keyboard: use the \<Tab\> key to locate the Abbreviation box.
77. *Status selection additions*: if applicable, type the letter *A* (for *admitted*) or the letter *O* (for *observation*), or both in the Flags box. EDIS uses these flags for reporting and to determine whether or not it should require a reason for delay when emergency-department stays exceed site-specified time limits. Keyboard: use the \<Tab\> key to locate the Flags box.
78. *Disposition selection additions*: if applicable, type *VA* (for *VA admission*), *A* (for *admitted*), or *M* (for *missed opportunity*) in the Flags box. EDIS uses these flags for reporting. Keyboard: use the \<Tab\> key to locate the Flags box.
79. (Optional) If you want to inactivate the new item, select the Inactive check box. The application does not include inactive items on its selection lists. Keyboard: use the \<Tab\> key to locate the Inactive check box and use the \<Spacebar\> key to select it.
80. (Optional) Change the order in which EDIS displays list selections in its data views by using a drag-and-drop operation to reorder selections in the Selections for Status, Selections for Disposition, Selections for Delay Reason, or Selections for Source lists. Keyboard instructions are not available for this step.
81. Click Save Selection List Changes to save your additions (or edits). EDIS displays an Alert message to tell you it successfully saved your changes. Click Close to dismiss this message. Keyboard: use the \<Tab\> key to locate the Save Selection List Changes button and use the \<Spacebar\> key to select the button. Use the \<Tab\> key to locate the Close button and use the \<Spacebar\> key to select it.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Activity report 48
Acuity entries 28
Acuity report 49
Add patient
Add information to the Patient Information pane 19
Adding unidentified patients 19, 26
Ambulance Is Arriving, Patient Name Is Unknown 19, 26
Enter Name, Patient Is Not in VistA 18
Enter Name, Patient Is Not in VistA 25
Search for Patient in VistA 18, 24
Triage view 24
Add patients
Identify patients 21
Add triage information 28
Adding a new display board 64
Adding choices to selection lists 82
Adding display-board columns 65
Adding EDIS to IE Favorites 7
Adding providers, residents, and nurses to staff pick lists 45
Adding status, disposition, delay reason, and source selections to selection lists 84
Adding, configuring, and editing rooms and areas 61
Adobe Flash Player 3
Application timeouts 5
Arrange columns 9
Arranging display-board columns 68
Assign Staff view 9, 45
Adding providers, residents, and nurses to staff pick lists 45
Configuring colors for providers, residents, and nurses 46
Removing providers, residents, and nurses from staff pick lists 46
Clinic entries 29
Colors subview, Configure view
Configuring colors 70
Configuring colors for Minutes at Location values 75
Configuring colors for Minutes for Imaging Order values 77
Configuring colors for Minutes for Lab Order values 76
Configuring colors for Minutes for Unverified Orders values 78
Configuring colors for status and acuity values 71
Configuring colors for Total Elapsed Minutes values 74
Configuring colors for Urgency - Lab values 72
Configuring colors for Urgency - Radiology values 73
General instructions for configuring colors 70
Complaint for display board entries 28
Configure view 9, 61
Display board configuration 64
Configuring colors 70
Configuring colors for Minutes at Location values 75
Configuring colors for Minutes for Imaging Order values 77
Configuring colors for Minutes for Lab Order values 76
Configuring colors for Minutes for Unverified Orders values 78
Configuring colors for providers, residents, and nurses 46
Configuring colors for status and acuity values 71
Configuring colors for Total Elapsed Minutes values 74
Configuring colors for Urgency - Lab values 72
Configuring colors for Urgency - Radiology values 73
Configuring or editing display-board columns 67
Configuring shift parameters 81
Creating a visit in CPRS 32
Creating visits in CPRS 29
Cross Reference (XRef) report 57
Data grids 9
Arrange columns 9
Resize columns 9
Sort columns 10
Definitions for source selections (national) 20
NHCI 20
Non-VA Clinic/Office 20
Non-VA Nursing Home 20
On-Site Clinic 20
On-Site Nursing Home 20
Self-Referred 20
Transfer, Other 20
VA Clinic, Off-Site 20
VA Nursing Home, Off-Site 20
Definitions for status selections (national) 29
Admitted 29
Awaiting Triage 29
Discharged 29
ED Boarding \[Hold} 29
ED Observation Unit 29
ED Patient 29
En Route/Prearrival 29
Delay reason definitions 35
Admit Physician Writing Dispo 35
Admitting Physician Evaluation 35
Arrange Emergency Surgery 37
ED Physician Limits 37
ED Staff Limits 37
ED to Hospital Bed 36
Interfacility Transfer 36
Obtain Accepting Physician 35
Obtain Ambulance Services 36
Obtain Consultant 36
Obtain Drugs/Pharmacology 37
Obtain Escort 36
Obtain Imaging Results 36
Obtain Imaging Studies 36
Obtain Inpatient Bed 36
Obtain Lab Results 37
Obtain Lab Studies 37
Obtain Medical Supplies 37
On-call Staff 37
Overcrowding of ED 37
Patient Admitted to Observation 36
Patient Transport Home 36
Patient Transport Other 37
Delay report 50
Delay Summary report 51
Display board configuration 64
Display Board subview, Configure view
Adding a new display board 64
Adding display-board columns 65
Arranging display-board columns 68
Configuring or editing display-board columns 67
Removing display-board columns 68
Resizing display-board columns 68
Saving display-board configurations 69
Display Board view 8
Disposition definitions (national) 34
Admitted to ICU 34
Admitted to Psychiatry 34
Admitted to Telemetry 35
Admitted to VA Ward 34
AMA 34
Deceased 34
Eloped 34
Home 34
Left Without Being Treated/Seen 34
Patient Name Entered in Error 34
Sent to Nurse Eval / Drop-in Clinic 34
Sent to Urgent Care Clinic 34
Transferred to a Non-VA Facility 35
Transferred to VA Facility 35
Disposition view 8, 33
Entering free-text diagnoses 38
Entering ICD-9-CM diagnoses 38
Removing patients from the board 39
Removing patients who were entered in error 40
Selecting a disposition 34
Selecting a reason for delay 35
ED BVAC Patients report 51
EDIS and CPRS interactions 10
EDIS integration via Appointment Manager 11
EDIS integration via PCE 12
Edit Closed view 8, 41
Emergency Severity Index
ESI 28
Entering free-text diagnoses 38
Entering ICD-9-CM diagnoses 38
Exporting reports 60
Exposure report 52
General instructions for configuring colors 70
Help files 10
Identify patients 21
Including residents on the entry form 80
Integrating via Appointment Manager 10
Integrating via PCE 10
JAWS (Job Access with Speech
Recommendations for JAWS users 2
JAWS (Job Access with Speech) 2
Launch EDIS 7
Log in 7
Long complaint entries 28
Missed Opportunities report 53
Notifications *See* also: Alerts
Duplicate patient selection warning 16
Multiple patient icon 16
Patient record flags 15
Patient selection messages 15
Nurse entries 28
Orders by Acuity report 54
Parameters subview, configure view
Including residents on the entry form 80
Parameters subview, Configure view 79
Configuring shift parameters 81
Requiring a disposition to remove patients from the board 81
Requiring a reason for delay 81
Requiring diagnoses 80
Requiring ICD-9-CM or free-text diagnoses 80
Saving parameter selections 81
Setting a default room or area 81
Setting a default room or area for patients arriving by ambulance 81
Patient Intake report 54
PC-based Display Board view 43
Viewing the PC-based display board 43
Preventing EDIS from accidentally closing 5
Printing reports 60
Provider entries 28
Provider report 57
Rehabilitation Act of 1973 (Section 508)
Job Access with Speech (JAWS) 2
Removing display-board columns 68
Removing patients from the board 39
Removing patients who were entered in error 40
Removing providers, residents, and nurses from staff pick lists 46
Reports v iew
Acuity report (standard) 49
Reports view 9, 47
Activity report (standard) 48
Column headings for reports 47
Cross Reference (XRef) report (restricted) 57
Delay report (standard) 50
Delay Summary report (standard) 51
Disposition abbreviations for reports 47
ED BVAC Patients report (standard) 51
Exporting reports (restricted action) 60
Exposure report (standard) 52
Missed Opportunities report (standard) 53
Orders by Acuity report (standard) 54
Patient Intake report (standard) 54
Printing reports 60
Provider report (restricted) 57
Running and viewing reports 59
Shift report 55
VA Admissions report (standard) 56
Requirements
Browser requirements for Flash Player 3
Flash Player minimum requirements for Apple Mac OS 4
Job Access with Speech workstation requirements 4
Workstation 3
Requiring a disposition to remove patients from the board 81
Requiring a reason for delay 81
Requiring diagnoses 80
Requiring ICD-9-CM or free-text diagnoses 80
Resident entries 28
Resize columns 9
Resizing display-board columns 68
Restricted record warning 15
Role-based access *See* Views
Room / Area subview, Configure view 61
Adding, configuring, and editing rooms and areas 61
Configuring colors for rooms and areas 63
Specifying the order of rooms and areas 63
Room and area entries 28
Running and viewing reports 59
Saving display-board configurations 69
Saving parameter selections 81
Selecting a disposition 34
Selecting a reason for delay 35
Selecting views 9
Selections subview, Configure view 82
Adding status, disposition, delay reason, and source selections to selection lists 84
Setting a default room or area 81
Setting a default room or area for patients arriving by ambulance 81
Setting patients' primary providers 32
Shift report 55
Sign In view 8, 17
Add patients 17
Sort columns 10
Source entries 29
Specifying the order of rooms and areas 63
Status entries 28
Triage view 8, 23
Add triage information 28
Creating visits in CPRS 29
Update view 8, 31
Add update information 31
Creating a visit in CPRS 32
Setting patients' primary providers 32
VA Admissions report 56
Verify code (change) 8
Views 8
Assign Staff 9
Configure 9
Display Board 8
Disposition 8
Edit Closed 8
Reports 9
Sign In 8
Triage 8
Update 8
Workstation requirements 3
