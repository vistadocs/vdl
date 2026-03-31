---
title: OR*3.0*453 Provider Role Tool User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: Provider Role Tool
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3.0
patch_id: OR*3.0*453
group_key: "CPRS:OR:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - provider
  - orders
  - table
  - contents
  - role
  - tool
  - patient
  - window
  - patients
  - date
page_count: 0
word_count: 4594
section_count: 18
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2021
revision_count: 3
revision_newest: 7/28/2021
revision_oldest: 7/6/2020
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/prt_ug_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/prt_ug_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>CPRS Provider Role Tool (PRT)

  User Guide: GUI Version

  V1.0
---

![](or-3-0-453-provider-role-tool-user-guide/001.png)

July 2021

Office of Information and Technology (OI&T)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date      | Revision | Description                                                                                                                                        | Author                |
|-----------|----------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| 7/28/2021 | 0.04     | OR\*3.0\*453: Redacted the manual for the VA Document Library (VDL). Removed names in revision history, port numbers and links to software builds. | CPRS Development Team |
| 3/4/2021  | 0.03     | OR\*3.0\*453: updated the Preparing for a Provider Role Change, Move Patient Orders to a New Provider sections                                     | REDACTED              |
| 7/6/2020  | 0.02     | Patch OR\*3.0\*453: revisions                                                                                                                      | REDACTED              |
| May 2020  | 0.01     | Revising per dev review                                                                                                                            | REDACTED              |

Table used for formatting, only.Revision History, including date of changes, version number, description of change, and author of change.

Artifact Rationale

Per the Veteran-focused Integrated Process (VIP) Guide, the User’s Guide is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A User Guide is a technical communication document intended to give assistance to people using a particular system, such as VistA end users. It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most user guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The User Guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required if applicable to your product.

Table of Contents

Table of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
    - [Assumptions](#assumptions)
    - [Coordination](#coordination)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operation](#continuity-of-operation)
- [Getting Started](#getting-started)
  - [Logging On](#logging-on)
  - [System Menu](#system-menu)
    - [Logging in to the Stand-alone PRT through Two-Factor Authentication](#logging-in-to-the-stand-alone-prt-through-two-factor-authentication)
    - [Logging in to the Stand-Alone PRT without Two-Factor Authentication](#logging-in-to-the-stand-alone-prt-without-two-factor-authentication)
    - [Logging into PRT through the CPRS GUI](#logging-into-prt-through-the-cprs-gui)
  - [Changing User ID and Password](#changing-user-id-and-password)
  - [Exit System](#exit-system)
  - [Caveats and Exceptions](#caveats-and-exceptions)
- [Using the Software](#using-the-software)
  - [Preparing for a Provider Role Change](#preparing-for-a-provider-role-change)
  - [Viewing the PRT Main Window](#viewing-the-prt-main-window)
    - [Window Layout](#window-layout)
    - [Buttons & Menu Items](#buttons-menu-items)
  - [How to Reassign Patient Orders](#how-to-reassign-patient-orders)
    - [Select a Current Provider and An Order Date Range](#select-a-current-provider-and-an-order-date-range)
    - [Select a New Provider for Reassigned Orders](#select-a-new-provider-for-reassigned-orders)
    - [Move Patient Orders to a New Provider](#move-patient-orders-to-a-new-provider)
    - [Reassign Orders](#reassign-orders)
  - [How to View a Patient’s Orders](#how-to-view-a-patients-orders)
  - [How to Create an Audit Report](#how-to-create-an-audit-report)
- [Troubleshooting](#troubleshooting)
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide instructions on how to use the Provider Role Tool (PRT) application.

The Provider Role Tool enables authorized users to reassign future alerts for *qualifying patient orders* from a current provider to one or more new providers. It handles the cases where a provider changes roles while remaining at the same site (for example, a provider who moves from VA to DOD but does not relocate or a resident who rotates from one specialty service to another, i.e.: Oncology to Surgery). The goal is for the current provider to no longer receive notifications for orders written in the previous role, while being able to receive notifications for orders written in the new role. The purpose is to improve patient care by having alerts available to the provider now responsible for continuing that patient’s treatment or therapy.

One way to think of the Provider Role Tool is to consider it a more advanced version of the CPRS Surrogates feature. The Surrogates feature lets you redirect all notifications from one provider to another – useful when one provider is on vacation. Provider Role Tool redirects only selected notifications – those related to qualifying orders issued while the current provider was acting in a now-discontinued role or capacity at a given site.

The Provider Role Tool application swaps “qualifying” patient orders from an original provider to a substitute provider. The reassignment ensures that the original provider won’t receive any notifications associated with the orders in question, but that the substitute provider will receive them. (A “qualifying” patient order is an open order issued by the original provider during a specified time period --by default, the last calendar year).

The Provider Role Tool implements VA New Service Request (NSR) 20130504. The program is independent from CPRS but works with CPRS GUI servers.

NSR 20130504 was written because of a provider who moved from VA to DOD while remaining at the same site. After the role change, the provider was no longer looking after VA patients, and was instead responsible for DOD patients. This role change put the facility into a difficult situation. If they assigned a surrogate for the original provider, that surrogate received order notifications for the original provider’s VA *and* DOD patients. If they did not assign a surrogate, the original provider continued to receive notifications for VA patients. They needed a solution that would let the original provider move on to new duties without receiving notifications for orders issued in the abandoned VA role.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Users: The Provider Role Tool will be used by personnel that sites designate to reassign responsibility from one provider to another. It is assumed that using Provider Role Tool will be an administrative function, perhaps performed by a Clinical Application Coordinator (CAC). The CAC can perform this function under the direction of clinical personnel who can speak to how qualifying orders will be reassigned to one or more different providers. However, it is up to sites to decide on the process to reassign orders.
- Accessibility: The Provider Role Tool is fully compliant with Section 508 accessibility directives.
- Provider Role Tool GUI Interface: The Provider Role Tool was built to run in the Microsoft Windows operating environment.

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To use the Provider Role Tool, sites will need to coordinate the installation and make sure the correct users are authorized to use the software.

- For installation, sites need to coordinate their local resources with Information Technology Operations and Services (ITOPS) support. The site Computerized Patient Record System (CPRS) Coordinator may be involved in selecting which users will need to use Provider Role Tool. It is anticipated that CACs will use the Provider Role Tool to reassign orders to new providers.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government during their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

*The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.*

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses several methods to highlight different aspects of the material.

- Descriptive text is presented in a proportional font (as represented by this font).
- Note: Notes are used to call a user’s attention to an important matter or idea. It will be in bold.
- Warning: This paragraph is a caution for users that if they do something, the result could be serious, including loss of data.
- “Snapshots” of computer online displays (for example, character-based screen captures/dialogs) and computer source code are shown in a non-proportional font and enclosed within a box.

Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

- Also included are Graphical User Interface (GUI) Microsoft Windows images (for example, dialogs or forms).

![](or-3-0-453-provider-role-tool-user-guide/002.png)

<span id="_Toc44880883" class="anchor"></span>Figure 1: Provider Role Tool server connection dialog

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### VA Document Library 

Provider Role Tool documentation is available on the VA Document Library (VDL):  
<http://www.va.gov/vdl>  

#### Online Help

Instructions, procedures, and other information are available from the Provider Role Tool online help file. You may access the help file by clicking Help \| Contents from the menu bar or by pressing the F1 key while any Provider Role Tool dialog is open. Much of the information in this User Manual is also in the Provider Role Tool online help.

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Name                                      | Role                       | Org  | Contact Info                                                                   |
|-------------------------------------------|----------------------------|------|--------------------------------------------------------------------------------|
| CPRS Clinical Application Coordinator     | Tier 0 Support             | VHA  | Local Clinical App Coordinator information should be available from your site. |
| OI&T National Service Desk                | Tier 1 Support             | OI&T | REDACTED                                                                       |
| Health Product Support                    | Tier 2 Support             | VHA  | REDACTED                                                                       |
| OI&T System Admin/Field Operation Support | Tier 2 & 3 support         | OI&T | REDACTED                                                                       |
| VistA Patch Maintenance                   | Tier 3 Application Support | OI&T | REDACTED                                                                       |

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

Table 1: Tier Support Contact Information

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool is a client-server GUI application that enables users to reassign existing orders to another provider. This reassignment often happens because a provider is changing roles but is remaining at the same location. For example, a reassignment would happen if a provider was working for the VA but took a position with a Department of Defense co-located site. The provider would still be at a VA site but would no longer be responsible for VA patients.

The Provider Role Tool GUI is a front-end application that interacts with the VistA database using CPRS communication protocols. It affects which users receive notifications.

To launch the Provider Role Tool, users will either select an item from the CPRS Tools menu or activate it from an icon.

Once logged in, the user can select the provider whose orders need to be changed and the date range for those orders. After selecting the provider, patients with orders from the selected provider display on the left side of the main PRT window.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Role Tool runs on workstations that have CPRS installed on them. It communicates with servers that interact with the VistA database, as shown below.

![](or-3-0-453-provider-role-tool-user-guide/003.png)

<span id="_Toc44880884" class="anchor"></span>Figure 2: Data Flow between VistA and CPRS Workstation

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Figure 2 above.

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only users who have been assigned the OR PRT ACCESS key may use the Provider Role Tool application.

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the VistA database is functioning and can be accessed, Provider Role Tool should be available. The protection of data and other items are related to the VistA database, not PRT.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can launch Provider Role Tool directly from an icon or from the CPRS Tools menu. If the site chooses to use Provider Role Tool from the Tools menu, CACs or other support personnel will need to add the menu item to CPRS.

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section will give instructions on the ways that a user can access the Provider Role Tool.

### Logging in to the Stand-alone PRT through Two-Factor Authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use your Personal Identification Verification (PIV) card and Personal Identification Number (PIN) to access PRT.

To login to the Provider Role Tool with your PIV card:

1.  Double-click the PRT icon on your desktop. You will immediately see the Provider Role Tool Server Connection Dialog.  
      
    ![](or-3-0-453-provider-role-tool-user-guide/004.png)

> <span id="_Toc44880885" class="anchor"></span>Figure 3: Provider Role Tool Server Connection Dialog

2.  In the Windows Security dialog, select the certificate associated with your PIV card and click “OK”.

> ![](or-3-0-453-provider-role-tool-user-guide/005.png)

> <span id="_Toc44880886" class="anchor"></span>Figure 4: Windows Security Dialog – VistA Logon Certificate Selection

3.  Enter your PIN and click “OK”.  
      
    ![](or-3-0-453-provider-role-tool-user-guide/006.png)

> <span id="_Toc44880887" class="anchor"></span>Figure 5 – PIN dialog

4.  On the System Use Notification window, click “OK”.  
    Note: After you click “OK”, you will see the PRT main window and will not need to enter your Access and Verify Codes.

### Logging in to the Stand-Alone PRT without Two-Factor Authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you don’t have a PIV card, do the following:

1.  Double-click the PRT icon on your desktop.
2.  On the VistA Sign-On dialog, input your Access Code and your Verify Code and click “OK”.

![](or-3-0-453-provider-role-tool-user-guide/007.png)

<span id="_Toc44880888" class="anchor"></span>Figure 6: VistA Sign-On dialog

### Logging into PRT through the CPRS GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  On the CPRS main menu, click “Tools”.
2.  Click “Provider Role Tool”.

## Changing User ID and Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users will use the same credentials that they use to access VistA or CPRS. Whenever those credentials need to be renewed, the same credentials will be used for Provider Role Tool.

## Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To exit the system, the user either selects the X in the upper right corner of the dialog or selects File \| Exit on the menu bar.

## Caveats and Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Preparing for a Provider Role Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It’s important to properly research and prepare before attempting a provider role change. Remember that the Provider Role Tool, though it displays patient names, is reassigning *orders*, not patients. The purpose of the application is to ensure that new notifications for recently issued orders go to a newly designated provider(s).

To successfully implement a provider role change using the Provider Role Tool, you should answer these questions before attempting a transfer:

1.  Who is changing roles? The management team identifies the provider changing roles.
2.  What patients have qualifying orders? The management team identifies patients who will be affected by the role change. Provider Role Tool defines these patients as those who have qualifying orders issued by the provider changing roles during a specified time period.
3.  Who will receive order notifications for these qualifying orders? The management team identifies the new provider(s) who will now manage the patients and orders formerly assigned to the departing provider.
4.  How far back are we going? The management team also determines a time period covered by the transfer, such as “all orders from one year ago until today at midnight”.
5.  How will we allocate transfers between multiple new providers? The management team specifies how patients/orders will be allocated between new providers. This could be simple, as in “evenly divide patients between these three new providers”. Or it could be complex, as in “find all the cardiac patients and assign them to provider X and find all the orthopedic patients and assign them to provider Y”.
6.  Are the designated new providers aware of this pending transfer? It’s incumbent on the management team to get “buy-in” from the new providers that will suddenly be receiving order notifications for patients formerly managed by the previous provider.
7.  Are the designated new providers able to receive the appropriate order notifications? You can’t transfer orders to a new provider who isn’t able to receive order notifications.
8.  Are you sure simple surrogacy is not sufficient? Provider Role Tool is designed to serve the business case where a provider is changing roles *at the same site*. If the provider is retiring or leaving the site, other business processes are probably more appropriate.

The Provider Role Tool can optionally assist in discovering patients and orders for a departing provider. For example, a user can enter a departing provider and a date range, and “assign” them to a new provider. In the Qualifying Orders window, Provider Role Tool will present a detailed listing of qualified orders for each patient. The management team can use this listing when designating which patients/orders go to each newly designated provider.

## Viewing the PRT Main Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Window Layout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After logging in, the user will see the Reassign Patient Orders window, which is the main window for the Provider Role Tool.

![](or-3-0-453-provider-role-tool-user-guide/008.png)

<span id="_Toc44880889" class="anchor"></span>Figure 7: Provider Role Tool Main Window

The main Provider Role Tool window has three sections:

- Left side: Selects and displays a current provider and associated patients/orders associated with that provider and the chosen date range  
    
  ![](or-3-0-453-provider-role-tool-user-guide/009.png)

> <span id="_Toc44880890" class="anchor"></span>Figure 8: Left side of the Provider Role Tool Main Window  

- Right side: Selects and displays new providers and the patients/orders assigned to each.

![](or-3-0-453-provider-role-tool-user-guide/010.png)

> <span id="_Toc44880891" class="anchor"></span>Figure 9: Right side of the Provider Role Tool Main Window

- Center: Buttons to move patients between old and new providers:  
    
  ![](or-3-0-453-provider-role-tool-user-guide/011.png)

> <span id="_Toc44880892" class="anchor"></span>Figure 10: Center Portion of the Main Provider Role Tool Window

The screen capture below shows a typical Provider Role Tool session in mid-progress. The user has already selected a current provider, added two new providers, and has transferred patients from the current provider to the new provider. However, the changes have not been applied yet.

![](or-3-0-453-provider-role-tool-user-guide/012.png)

<span id="_Toc44880893" class="anchor"></span>Figure 11: A typical Provider Role Tool session after the user has added a new provider

Additional features in the Provider Role Tool GUI:

- Most tables and lists have popup or context menus with additional actions. When in doubt, right click to see if a menu pops up.
- The main screen supports drag and drop. You can drag patients from left to right or between providers in the right panel.
- Some tables support double click. You can double click a patient to see associated orders.
- Most tables and lists support multiple selections using standard Windows techniques.

### Buttons & Menu Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All buttons on the main window have corresponding menu commands in the “Edit” main menu. All buttons and menu items have shortcuts (command keys) that are displayed when the “ALT” key is pressed.

- Choose Current Provider and Order Dates: Displays a popup dialog (see additional help) in which the user can select the current provider from a list. The user can also modify the default selection period, which defaults to the past calendar year. Upon selection, the patients list at left screen will be populated with patients. The order count for each patient displays to the right of their names.
- Add Selected: Moves the *selected* current provider’s patients (at left screen) to the selected new provider (at right screen).
- Add All: Moves all current provider’s patients (at left screen) to the selected new provider (at right screen).
- Undo Selected: Removes all *selected* patients at right screen (new provider) and restores them at left screen (current provider). It also removes all selected new providers.
- Undo All: Removes all patients at right screen (new provider) and restores them at left screen (current provider). It also removes all new providers.

## How to Reassign Patient Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are four phases in moving patient orders from a current provider to one or more new providers:

1.  Select a Current Provider and an Order Date Range.
2.  Select a New Provider for reassigned orders.
3.  Move Patient Orders to the New Provider.
4.  Reassign Orders.

### Select a *Current* Provider and An Order Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first phase of reassigning patient orders is to select a current provider and an order date range:

1.  On the View menu, select one of the following:
    1.  All orders by patient.
    2.  All orders by patient and transfer type.
    3.  Individual orders by patient and transfer type.
2.  Click the “Choose Current Provider/Order Dates” button on the main window or select Edit \| Choose Current Provider/Order Dates on the menu.

> ![](or-3-0-453-provider-role-tool-user-guide/013.png)

> <span id="_Toc44880894" class="anchor"></span>Figure 12: Choose Current Provider/Order Dates (highlighted in red for clarity)  

1.  In the Select Current Provider and Order Dates dialog box, perform the following:
    1.  Select an “Orders Start Date” and an “Orders Stop Date”. To set a new date, select the “Orders Start Date” or “Orders Stop Date” calendar and type a date.
    2.  Type the last name (or part of the last name) of a provider or click on a name in the drop-down.
    3.  If desired, check the “Include terminated providers that hold the PROVIDER key” checkbox.
    4.  Click “OK”.

> ![](or-3-0-453-provider-role-tool-user-guide/014.png)

> <span id="_Toc44880895" class="anchor"></span>Figure 13: Select Current Provider and Order Dates window (highlighted in yellow for clarity)

> Notes: The default “Orders Start Date” is one year ago from today and the default “Orders Stop Date” is the current date.  
> The “Orders Start Date” can be any date in the past, but the “Orders Stop Date” cannot be a future date.  
> The dialog box does a search by last name, not by first or middle name. You can only type the name of one provider.

> **WARNING:** Selecting a new provider and date range will erase any unapplied assignments you have made in the Provider Role Tool: Reassign Signed Patient Orders window.

### Select a *New* Provider for Reassigned Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The second phase of reassigning patient orders is to select a new provider.

1.  Click “Add New Provider” on the main window or select Edit \| Add New Provider on the menu.

> ![](or-3-0-453-provider-role-tool-user-guide/015.png)

> <span id="_Toc44880896" class="anchor"></span>Figure 14: Add New Provider selected (highlighted in red for clarity)

2.  In the Add New Provider dialog box, perform the following:
    1.  Type the last name (or part of the last name) of a provider or click on a name in the drop-down. You can select only one new provider at a time.
    2.  Click “OK”.

> ![](or-3-0-453-provider-role-tool-user-guide/016.png)

> <span id="_Toc44880897" class="anchor"></span>Figure 15: Add New Provider (highlighted in yellow for clarity)

2.  To add multiple new providers, repeat the steps above as often as needed.

> Note: After a new provider is added, the Reassign Signed Patient Orders window will look like this:  

> ![](or-3-0-453-provider-role-tool-user-guide/017.png)

> <span id="_Toc44880898" class="anchor"></span>Figure 16: Reassign Signed Patient Orders window after a new provider has been added

### Move Patient Orders to a New Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The third phase of reassigning patient orders is to move the patient orders to new providers and apply the changes.

1.  In the Provider Role Tool: Reassign Signed Patient Orders window, do the following:
    1.  Click on a new provider.
    2.  Click on a patient name.

![](or-3-0-453-provider-role-tool-user-guide/018.png)

<span id="_Toc44880899" class="anchor"></span>Figure 17: Reassign Signed Patient Orders window after a patient and new provider have been selected  

2.  Click the “Add Selected” button on the main window or select Edit \| Add Selected on the menu.  
    Note: You can assign all patients to a new provider by clicking on the “Add All” button or selecting Edit \| Add All.
3.  Click the “Apply Changes” button on the main window or select Edit \| Apply Changes on the menu.

> ![](or-3-0-453-provider-role-tool-user-guide/019.png)

> <span id="_Toc44880900" class="anchor"></span>Figure 18: Reassign Signed Patient Orders window before “Apply Changes” has been clicked (highlighted in red for clarity)

### Reassign Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The fourth phase of reassigning patient orders is to complete the Reassign Orders dialog, which makes the changes permanent.

After the user has clicked the “Apply Changes” button, the Review Orders (Review and Execute) window will display. Because this is an irreversible change, Provider Role Tool requires this deliberate review step. The Review and Execute window displays the orders that need to be reassigned, and the user must click the Reassign Orders button to complete the reassignment process.

To complete the order reassignment:

1.  Accept the default “Effective Date” of today or change to a future date. The “Effective Date” cannot be a past date.

> ![](or-3-0-453-provider-role-tool-user-guide/020.png)

> <span id="_Toc44880901" class="anchor"></span>Figure 19: Reassign Orders button, highlighted in red for clarity

2.  Review the list of reassigned orders.

> Note: The review screen will likely have hundreds or possibly thousands of individual orders. The tool presents the list and requires another button click mainly as a “stop and pause” feature.

3.  Click the “Reassign Orders” button to complete reassignment.
4.  When the Transfer Completed window appears, click “OK”.  
      
    ![](or-3-0-453-provider-role-tool-user-guide/021.png)

    <span id="_Toc44880902" class="anchor"></span>Figure 20 – Transfer Completed window
5.  Review the results to see if any reassignments failed.
6.  Optionally copy the reassignment results to the Windows clipboard by right-clicking on the Reassign Orders (Review and Execute) screen and clicking “Copy Results to Clipboard”.

> ![](or-3-0-453-provider-role-tool-user-guide/022.png)

> <span id="_Toc44880903" class="anchor"></span>Figure 21 – Copy Results to Clipboard

7.  Return to the main window by clicking the “X” in the top right corner.

Below is a screen capture showing the text report pasted into Notepad.

![](or-3-0-453-provider-role-tool-user-guide/023.png)

<span id="_Toc44880904" class="anchor"></span>Figure 22: Notepad text report

## How to View a Patient’s Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once patients are listed in either pane of the main window, the user can bring up the Qualifying Orders for Patient(s) window and view the details about the orders.

A qualifying order has the following characteristics:

- It was issued by the selected provider.
- It was issued during the selected date range.
- It is a signed order.
- It is in a state identified as potentially generating a future notification.

The Qualifying Orders for Patient(s) window has three sections:

- Qualifying orders for the selected patient are listed on the left side of the window. Some orders may be in an expired or discontinued state, but these orders are still considered qualifying orders.
- The details about an order are shown on the right side of the window.
- The order transfer history is listed on the bottom right side of the window.

To view a patient’s orders:

1.  Select a current or new provider on the Provider Role Tool: Reassign Signed Patient Orders window (the main window).
3.  In the Qualifying Orders for Patient(s) window, perform one of the following tasks:
    1.  Double-click on a patient on either the left or right pane.
    2.  Right-click on a patient on either the left or right pane and then, click on “Show Orders for selected patient(s)”.
4.  To view the details and transfer history of a patient’s order, left-click, right-click or press the shift key on a patient’s name.
5.  Click the “Close” button to go back to the main window.

> ![](or-3-0-453-provider-role-tool-user-guide/024.png)

> <span id="_Toc44880905" class="anchor"></span>Figure 23: Qualifying Orders for Patient(s)

## How to Create an Audit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The audit report displays all order reassignments that occurred within a specific time period at the VistA site that you are affiliated with.

You will see order reassignments in all statuses for all patients transferred from and to all providers at your VistA site within a specified time period.

The audit report default Stop Date is the current date and the default Start Date is one year behind today’s date.

To create an audit report:

1.  On the PRT Menu, select View \| Audit Report.
2.  On the Audit Report window, do the following:
    1.  Select an “Audit Start Date” and an “Audit Stop Date”. To set a new date, select the “Audit Start Date” or “Audit Stop Date” calendar and type a date.
    2.  Click the “Build Report” button.
    3.  To view details about an order, click on an order and then, click the “Show Orders” button. You will then
    4.  To view details about an order, click on the order and then, click the “Show Orders” button. You will be taken to the Qualifying Orders for Patient(s) window.
    5.  To go back to the main window, click the “Close” button.

> ![](or-3-0-453-provider-role-tool-user-guide/025.png)

> <span id="_Toc44880906" class="anchor"></span>Figure 24: Audit Report

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the user receives an error stating they are not authorized to use Provider Role Tool, verify the user is assigned the OR PRT ACCESS key.

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| 2FA   | Two-Factor Authentication                                                                                   |
|-------|-------------------------------------------------------------------------------------------------------------|
| CAC   | Clinical Application Coordinator                                                                            |
| CD2   | Critical Decision Point \#2                                                                                 |
| CPRS  | Computerized Patient Record System.                                                                         |
| DOD   | Department of Defense                                                                                       |
| GUI   | Graphical User Interface                                                                                    |
| ITOPS | Information Technology Operations and Services (formerly known as Service Delivery and Engineering \[SDE\]) |
| MVI   | Master Veteran Index                                                                                        |
| NSR   | New Service Request                                                                                         |
| PIN   | Personal Identification Number                                                                              |
| PIV   | Personal Identification Verification                                                                        |
| PRT   | Provider Role Tool                                                                                          |
| SDE   | Service Delivery and Engineering                                                                            |
| VA    | Veterans Affairs                                                                                            |
| VDL   | VA Document Library                                                                                         |
| VIP   | Veteran-focused Integration Process                                                                         |
| VistA | Veterans Health Information Systems and Technology Architecture                                             |