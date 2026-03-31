---
title: "CPRS User Manual:List Manager Clinician's Getting Started Guide"
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: "CPRS :List Manager Clinician's Getting Started Guide"
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - orders
  - cprs
  - patient
  - order
  - clinician
  - manager
  - class
  - manual
page_count: 0
word_count: 11540
section_count: 45
table_count: 5
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: March 2005
revision_count: 6
revision_newest: 3/15/05
revision_oldest: 6/29/00
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/cprslmum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/cprslmum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Computerized Patient Record System (CPRS)

  Clinician’s Getting Started Guide:  
  List Manager Version
---

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/001.png)

March 2005

Office of Information and Technology (OIT)

Revision History

| Date      | Revision | Description                                                                                                           | Author   |
|-----------|----------|-----------------------------------------------------------------------------------------------------------------------|----------|
| 3/15/05   | Various  | Changes for SOP compliance about displaying sensitive patient data.                                                   | Redacted |
| 8/15/2003 | 18,51    | Added a note about Code Set Versioning changes in entering new problems. Added a note about CSV or Consults Ordering. |          |
| 12/02     | 27-31    | Added changes for event-delayed orders.                                                                               |          |
| 12/2021   |          | Added information about Copay prompts                                                                                 |          |
| 9/11/01   |          | Added information about medication changes that come about as a result of POE.                                        |          |
| 6/29/00   |          | Added to note about IV meds with more than one additive being saved as IV Fluids.                                     |          |
| 6/29/00   |          | Added note that outpatient med active status now displays as “active (susp)”.                                         |          |
| 6/29/00   |          | Added note about outpatient med orders requiring authorized provider signature prior to release.                      |          |

Table used for formatting, only.Revision History, including date of changes, version number, description of change, and author of change.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [What is CPRS?](#what-is-cprs)
  - [Using CPRS Documentation](#using-cprs-documentation)
    - [Related Manuals](#related-manuals)
    - [World Wide Web](#world-wide-web)
    - [First Time VISTA Users](#first-time-vista-users)
  - [Conventions in This Manual](#conventions-in-this-manual)
  - [Notifications](#notifications)
  - [CPRS and the List Manager User Interface](#cprs-and-the-list-manager-user-interface)
  - [List Manager Conventions](#list-manager-conventions)
- [Using CPRS](#using-cprs)
  - [Entering CPRS](#entering-cprs)
  - [Selecting a Patient](#selecting-a-patient)
- [The Cover Sheet](#the-cover-sheet)
  - [Actions](#actions)
  - [More Actions](#more-actions)
  - [Alerts, Allergies, and Patient Postings](#alerts-allergies-and-patient-postings)
  - [Allergies/Alerts Detailed Display](#allergiesalerts-detailed-display)
- [Chart Contents](#chart-contents)
- [Problems](#problems)
  - [Change View](#change-view)
- [Notes](#notes)
- [Orders](#orders)
  - [Reviewing orders](#reviewing-orders)
  - [Change View](#change-view-1)
  - [Order Screen Actions](#order-screen-actions)
  - [Add New Orders](#add-new-orders)
    - [Placing an Event-Delayed Order](#placing-an-event-delayed-order)
    - [Changing the Release Event of an Existing Order](#changing-the-release-event-of-an-existing-order)
    - [Removing the Release Event from an Existing Order](#removing-the-release-event-from-an-existing-order)
    - [Manually Releasing Event-Delayed Orders](#manually-releasing-event-delayed-orders)
    - [Viewing Event Delayed Orders After they are Released](#viewing-event-delayed-orders-after-they-are-released)
  - [Quick Orders](#quick-orders)
  - [Order Sets](#order-sets)
  - [Reviewing and Signing New Orders](#reviewing-and-signing-new-orders)
  - [Adding New Orders](#adding-new-orders)
  - [Ordering, by Service/Category](#ordering-by-servicecategory)
  - [Ordering Parameters/Activity/Patient Care Orders/Free Text](#ordering-parametersactivitypatient-care-ordersfree-text)
  - [Ordering Diets](#ordering-diets)
  - [Overview of New CPRS/POE Functionality](#overview-of-new-cprspoe-functionality)
  - [Ordering Outpatient Medications with a Simple Dose](#ordering-outpatient-medications-with-a-simple-dose)
  - [Ordering Outpatient Medications with Complex Doses](#ordering-outpatient-medications-with-complex-doses)
  - [Ordering Inpatient Medications with a Simple Dose](#ordering-inpatient-medications-with-a-simple-dose)
  - [Ordering Inpatient Medications with a Complex Dose](#ordering-inpatient-medications-with-a-complex-dose)
  - [Ordering IV Fluids](#ordering-iv-fluids)
  - [Ordering Imaging or Radiology Exams](#ordering-imaging-or-radiology-exams)
  - [Ordering Labs](#ordering-labs)
  - [Ordering Consults & Procedures](#ordering-consults-procedures)
- [Meds](#meds)
  - [Meds Change View](#meds-change-view)
- [Labs](#labs)
  - [Lab Change View](#lab-change-view)
- [Consults](#consults)
- [Imaging](#imaging)
  - [Change View](#change-view-2)
- [D/C Summaries](#dc-summaries)
- [Reports](#reports)
  - [Results Reporting](#results-reporting)
- [Personal Preferences](#personal-preferences)
  - [Personal Preferences Menu](#personal-preferences-menu)
  - [GUI Cover Sheet Display Parameters](#gui-cover-sheet-display-parameters)
  - [Notification Mgmt Menu Options](#notification-mgmt-menu-options)
  - [Personal Patient List Menu](#personal-patient-list-menu)
  - [Patient Selection Preference Menu](#patient-selection-preference-menu)
  - [Display Patients Linked to Me via Teams](#display-patients-linked-to-me-via-teams)
  - [Display My Teams](#display-my-teams)
- [Helpful Hints](#helpful-hints)
- [Glossary](#glossary)
- [# Appendix: Screen Actions](#appendix-screen-actions)

## What is CPRS? 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System V. 1.0 (CPRS) is a Veterans Health Information Systems and Technology Architecture (VISTA) computer application. CPRS enables you to enter, review, and continuously update all information connected with any patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries.

CPRS not only allows you to keep comprehensive patient records, but it also enables you to review and analyze the data gathered on any patient in a way that directly supports clinical decision-making.

## Using CPRS Documentation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Computerized Patient Record System V. 1.0 Installation GuideComputerized Patient Record System V. 1.0 Setup GuideComputerized Patient Record System V. 1.0 Technical ManualText Integration Utility (TIU) Clinical Coordinator and User ManualConsult/Request Tracking User Manual*

### World Wide Web

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS documentation is also available on the VISTA Intranet. The Intranet version will be constantly updated, and thus might contain more current information than this print version.

Intranet address: vista.med.va.gov/cprs/

### First Time VISTA Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are unfamiliar with this package or other Veterans Health Information Systems and Technology Architecture (VISTA) software applications, we recommend that you study the User’s Guide to Computing. This orientation guide is a comprehensive handbook for first-time users of any VISTA application to help you become familiar with basic computer terms and the components of a computer. It is reproduced and distributed periodically by the Kernel Development Group. To request a copy, contact your local Information Resources Management Service (IRMS) staff.

## Conventions in This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Option examples: Menus and examples of computer dialogue that you see on the screen are shown in courier font in boxes:

Select Menu Option:

User Response: User responses are shown here in bold, but do not appear bold on the screen. The bold part of the entry is the letter or letters that must be typed so that the computer can identify the response. In most cases, you need only enter the first few letters. This increases speed and accuracy.

Select PATIENT NAME: Cprspatient, One

> **NOTE:** Names and social security numbers used in the examples are fictitious.

\<Enter\> This indicates the Enter or Return key, which is pressed after every response you enter or when you wish to bypass a prompt, accept a default (//), or return to a previous action. In this manual, it is only shown in examples when it might be unclear that such a keystroke must be entered.

^, ^^, ^^^ Enter the Up-arrow (also known as a caret or circumflex) at a prompt to leave the current option, menu, sequence of prompts, or help. To get completely out of your current context and back to your original menu, you may need to enter two or three up-arrows. (You may see a message, “Press RETURN to continue or ^ or ^^ to exit:” after each screen in a series of screen displays; e.g., for reports or online help.)

?, ??, ??? Enter one, two, or three question marks at a prompt for help about the menu, option, or prompt you are at. One question mark elicits a brief statement of what information is appropriate for responding to the prompt; two question marks show a list (and sometimes descriptions) of more actions; and three question marks provide more detailed help, including a list of possible answers, if appropriate.

Defaults (//) Defaults are responses provided to speed up your entry process. They are either the most common responses, the safest responses, or the previous response.

> Example: Select Action: Quit//

Replace..With If the default entry is longer than 20 characters, you will see the “Replace. With”

editor instead of the double slashes (//).

1.  Enter @ after Replace if you want to replace the entire default entry, or type one or two letters followed by three dots ( ) to change part of the letters (e.g., to correct a misspelling),
2.  press Return,
3.  When the word With appears, type the correct name

> Example:

> Provider: Clinical Coordinator Replace Co... With Nurse

\>\> Side-arrows (Greater-than/Less-than; shift-comma, shift,period) indicate that more information is available on the right side of the screen. Enter these arrows at any prompt. If the arrows appear in front of an order, it means that the order requires action by a clerk or nurse.

+, - The plus symbol at the bottom left-hand side of a screen of information indicates that more than one screen of information exists. Use the plus and minus keys to navigate up and down. If the + is displayed in front of a lab order, it means that the lab test will be done multiple times, according to a selected schedule.

Shortcut You can jump through a sequence of actions and screens by entering the names (or their abbreviations) separated by semi-colons.

> Shortcut Example: CC;O;AD;L will take you through Chart Contents, Orders, Add Orders, and to Lab.

Icons

Icons used to highlight key points in this manual include:

| ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/002.png) | Required security keys                                             |
|--------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| \+                                                                                                                 | Indicates important information that the user should take note of. |

Icons used in manualDecorative table used to display the key icon, denoting a security key is required, and the plus icon, indicating important information the user should take note of.

## Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Notifications are important messages that alert providers to certain clinical events (for example, a critical lab value). Some notifications are for information only; others allow you to take follow-up action to the event that triggered the notification. They may also notify providers of conditions such as unsigned orders. Notifications are automatically deleted after being displayed or when a follow-up action is taken.

Notifications are retained for a predetermined amount of time (up to 30 days), after which they may be sent to another destination, such as your MailMan surrogate or your supervisor. Confer with your CAC to establish and set up these options. You can also confer with your CAC to select what types of notifications you will receive. Some notifications are mandatory, however, and cannot be disabled. See the Personal Preferences section in this manual for further information about notifications.

## CPRS and the List Manager User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS was built to run in both the Windows operating environment (usually referred to simply as Windows) and on terminals. The Windows version of CPRS is described in another manual. This manual describes the terminal, text-based version of CPRS.

If you are not already familiar with List Manager applications, this section will take you on a quick tour of the interface. If you are already familiar with the List Manager interface, you can skip to the next section, Using CPRS.

List Manager is designed to display a list of clinical items (based on criteria you set) that you perform various actions on. An example of a CPRS screen in List Manager format is shown here, with explanations of the various components on the screen.

## List Manager Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

List Manager is a tool designed so that a list of items can be presented to the user to perform *actions* on.

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/003.png)

Description of List Manager Screen Components

<table>
<caption>Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th>Component</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Screen title</td>
<td>The screen title changes according to what type of information List Manager is displaying (e.g., Chart Contents, Cover Sheet, Active Orders, lab Orders, etc.). Use this title as an identifier to confirm your location at any time.</td>
</tr>
<tr class="even">
<td>Header area</td>
<td>The header area is a “fixed” (non-scrollable) area that displays patient information. It also tells if there is more than one page of information and which page you’re currently on (e.g., Page: 1 of 3).</td>
</tr>
<tr class="odd">
<td>List area</td>
<td>(scrolling region) This area scrolls and displays the information that you can take action on.</td>
</tr>
<tr class="even">
<td>Message window</td>
<td><p>This section displays a plus (+) sign, minus (-) sign, &gt;&gt; symbols, or informational text (i.e., Enter ?? for more actions). A plus sign means more information is available; enter it at the action prompt to “jump” forward a page; a minus sign “jumps” back a screen.; &gt; moves you to more information on the right; and &lt; moves you back to the left or main screen. Other allowable actions may be displayed in the</p>
<p>message window.</p></td>
</tr>
<tr class="odd">
<td>Action area</td>
<td>A list of actions display in this area of the screen. If you enter double question marks (??) at the “Select Action(s)” prompt, you are shown a “hidden” list of additional actions that are available to you.</td>
</tr>
</tbody>
</table>

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

# Using CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Entering CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can take several routes to get into CPRS to enter orders and progress notes, review them, and display reports and results for individual patients. The route you choose depends on how your site has set up your menus, what your primary purpose is, and what seems most convenient to you.

- The CPRS Clinician Menu on the main Clinician’s Menu.
- One of the following menus or options on the Clinician’s Menu
- Add New Orders
- Act on Existing Orders
- Results Reporting

This Guide describes going through the CPRS Clinician Menu, which provides a multi-faceted view of a patient’s medical record.

When you enter the CPRS Clinician Menu, you will see this screen:

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/004.png)

## Selecting a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Selection screen offers three methods for finding your patient:

- Entering a name from a list (if you have one defined and set as your default,
- Entering a patient’s name (or last initial + last 4 letters of SSN) at the Select Patient prompt, or
- Entering FD (Find Patient), entering a ward or clinic name, then selecting a patient name from the list that appears.

# The Cover Sheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cover Sheet of the selected patient chart displays the patient’s name, SSN, date of birth, age, unit/location, allergies/adverse reactions, patient postings, vitals, immunizations, and service connection.

\+ NOTES:

> • You may only have one patient chart open at any given time

> • Two users may not simultaneously take actions on orders for the same patient

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/005.png)

## Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter the display numbers of the items you wish to change or act on. A menu of available actions is then presented for selection. You can also choose the action first and then the item.

- Enter NW to document a new allergy.
- Enter AD to add new orders for this patient from any page in the chart.
- Enter CC to see a list of the other “pages” of the chart.
- Enter SP to select a different patient.
- Enter ?? to see a list of other actions available.

## More Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you enter two question marks (??) at the prompt, the following (hidden) actions are displayed. They can also be used at any prompt.

\+ Next Screen UP Up a Line AD Add New Orders

\- Previous Screen DN Down a Line RV Review New Orders

FS First Screen \> Shift View to Right CWAD Display CWD Info

LS Last Screen \< Shift View to Left PI Patient Inquiry

GO Go to Page PS Print Screen SL Search List

RD Redisplay Screen PT Print List EX Exit

ADPL Auto Display On/Off

## Alerts, Allergies, and Patient Postings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can access some patient information directly from the Cover Sheet, without going to other tabs.

- Allergies
- Patient Postings
- Recent Vitals
- Immunizations
- Eligibility

From this screen, you can view a detailed display of any of these items, or you can record new allergies.

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/006.png)

## Allergies/Alerts Detailed Display 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/007.png)

# Chart Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Chart is composed of screens that represent the pages of a traditional paper patient chart. The Chart Contents screen provides easy, logical access to other screens that show specialized patient information.

Cover Sheet Orders Imaging Reports

Problems Meds Consults

Notes Labs D/C Summaries

When you choose most of these, the first thing you see is a list of current items for this patient (active problems, progress notes, lab results, orders, or meds). You can then review any of the items in greater detail, edit or cancel them if appropriate, or order new ones.

HINT: To quickly jump through a series of screens, enter the names or abbreviations of the actions, separated by semi-colons. Example: CC;Orders;Meds.

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/008.png)

# Problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Problems tab is used to document and track a patient’s health care problems. It provides you with a current and historical view of the patient’s problems across clinical specialties and it allows you to trace each identified problem through the VISTA system in terms of treatment, test results, and outcome. To go to the Problems screen, select the Problems tab at the bottom of the Chart Contents screen.

In the Problems tab, you can change the display to see customized lists of problems, edit a problem to reflect changes, and add a new problem.

*To enter the Problems screen:*

1.  Go into the Clinician Menu and select OE for CPRS Clinician Menu.
2.  The patient selection screen appears, with your personal patient list if you’ve created one (through Personal Preferences).
3.  Select a patient from the list, or enter another one.
4.  The Cover Sheet for this patient appears.
5.  Choose Chart Contents (CC); the Chart Contents tabs appear at the bottom of the screen.

> Hint: Enter CC;P for a shortcut  

> ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/009.png)

6.  Choose Problems from the Chart Contents list.
7.  The Problem List appears. The default is to show Active Problems (status is listed on the far right of the screen).

> Problem List Example  

> ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/010.png)

8.  If you select one of the listed problems to review, you can choose one of the actions displayed below: Inactivate, Remove, Add Comment, or Detailed Display.  
      
    ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/011.png)
9.  To add a new problem, enter NW at the Select: Chart Contents: prompt, and then answer the prompts as shown in the example below:  
      
    ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/012.png)

> ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/013.png)

> Note: When you enter a new problem, CPRS will check to see if the code for that problem is active as of the date entered as part of Code Set Versioning (CSV). If not, it will ask you change the code for the problem before allowing the user to enter the problem.

## Change View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you select Change View here, you can change the display to a different status; i.e., inactive problems or both inactive and active problems.

> ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/014.png)

# Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can review, enter, sign, or edit progress notes for one patient at a time through the CPRS. To review, edit, or sign progress notes for multiple patients, use the Text Integration Utilities menu.

*To enter a Progress Note:*

1.  Go into the Clinician Menu and select OE for CPRS Clinician Menu.
2.  The patient selection screen appears, with your personal patient list if you’ve created one (through Personal Preferences).
3.  Select a patient from the list, or enter another one.
4.  The Cover Sheet for this patient appears.
5.  Choose Chart Contents (CC).

> Shortcut: Enter CC;N

> ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/015.png)

6.  Choose Notes from the Chart Contents list.
7.  A list of notes appears (the default is to show Signed Notes).  
      
    ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/016.png)
8.  Enter NW for Write New Note. Respond to the following prompts as appropriate.  
      
    ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/017.png)

> ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/018.png)

*To sign a Progress Note:*

1.  Select Notes from the Chart Components screen.  
      
    ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/019.png)
2.  Select CV for Change View, to see all your unsigned notes.  
      
    ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/020.png)
3.  Enter the number of the note to be signed.  
      
    ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/021.png)
4.  The selected unsigned note and actions appear. Select Sign

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/022.png)

# Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Orders tab, you can review current orders for a patient and place new orders for consults, medications, lab tests, radiology procedures, diets, consults, and procedures, as well as nursing and activity orders.

## Reviewing orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  After selecting a patient, select the Chart Contents (CC) action.  
      
    ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/023.png)
2.  Select the Orders tab.
3.  The Active Orders screen for your patient is displayed.  
      
    ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/024.png)

> NOTE: + in front of a Lab order indicates that this order will be done multiple times according to a selected schedule.

## Change View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change the way orders are displayed by selecting Change View at the Active Orders screen and choosing one of the criteria listed. You can save a view to be your default view; i.e., the view that displays whenever you go into the orders screen.

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/025.png)

Short Format Example

This format doesn’t list the requestor or stop date.

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/026.png)

## Order Screen Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you select an order (by entering the number of the order at the Select Action prompt), a list of actions appears that you can perform on that order.

+ NOTE: This is a significant change from OE/RR, where the actions were visible at the bottom of the review screen before you selected an order.

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/027.png)

These actions are described on the next page.

Order Actions

<table>
<caption>Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Change</td>
<td>Inpatient Medications allows editing of orders while they are still pending. Other service/sections require the old order to be “DC’d” (cancelled) and a new order to be added, if the original was incorrect. Changed orders appear on the Review Screen as DC’d orders, along with the new order.</td>
</tr>
<tr class="even">
<td>Renew</td>
<td>If allowed by the service (usually only Pharmacy), you can renew/reinstate order(s) that have been discontinued.</td>
</tr>
<tr class="odd">
<td>Discontinue</td>
<td>Lets you discontinue orders that haven’t been released to the service yet or that hasn’t expired yet. After you request that an order be discontinued, you must electronically sign it or indicate that it’s been signed on the chart. It will then show up on the “New/Unsigned Orders” screen as a discontinued order. If an order is discontinued by the service, a notification will be triggered that the order (for discontinuation) requires a chart signature.</td>
</tr>
<tr class="even">
<td>Sign</td>
<td>This lets you sign an order electronically by entering your electronic signature code, or indicate that the order was signed on-chart.</td>
</tr>
<tr class="odd">
<td>Hold</td>
<td>You can place an Order on hold, preventing further processing until "unhold" action or expiration of order. Not all packages may allow their orders to be placed on hold; Pharmacy orders may be placed on hold, but Lab orders can’t.</td>
</tr>
<tr class="even">
<td>Release Hold</td>
<td>This action allows an order to continue its processing.</td>
</tr>
<tr class="odd">
<td>Flag</td>
<td>This action lets you place a notice that the order needs clarification or further instructions.</td>
</tr>
<tr class="even">
<td>Unflag</td>
<td>Takes the flag off after clarification or instructions are received.</td>
</tr>
<tr class="odd">
<td>Ward Comments</td>
<td>You can add ward comments about an order; these will be displayed on the Details screen.</td>
</tr>
<tr class="even">
<td>Details</td>
<td>More information about the selected order is displayed.</td>
</tr>
<tr class="odd">
<td>Results</td>
<td>Allows you to (enter or view) results for an order.</td>
</tr>
<tr class="even">
<td>Alert Results</td>
<td>Allows you to (enter or view) alert results for an order.</td>
</tr>
<tr class="odd">
<td>Copy</td>
<td>This is a shortcut that allows you to copy an order, rather than having to completely write a new order. This action is useful for when hospital policy requires that new orders be written periodically, or when orders are discontinued for ward transfers.</td>
</tr>
<tr class="even">
<td><p>Print</p>
<p>Labels</p>
<p>Work Copies Service Copies Requisitions Chart Copies</p></td>
<td>When you select the Print action, it presents the types of printing allowed. You can print Labels or Requisitions. You can print a copy of all current orders, by service or Ward, using a pre-defined format. Each hospital can only have one format for Service Copies or Work Copies. These copies will normally be printed on a service printer. You can print a copy of all current orders that would appear on a patient’s chart, using a pre-defined format. <em><strong>Each hospital can only have one format for Chart Copies.</strong></em></td>
</tr>
</tbody>
</table>

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

## Add New Orders 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add New Orders action leads to the Add Orders screen. The Add Orders screen varies widely from user to user, based on how your local coordinators have set it up to best fit your needs. You can order from many services, by individual order, by several selections separated by commas, or by a range of numbers separated by a hyphen. After completing one order, you proceed automatically to the next.

When you have finished placing orders, enter Q. You will then be prompted to sign these new orders. When the order(s) are signed, service copies print to the appropriate area(s) for action. Chart copies may print at the nurses’ station/patient location.

Items with ellipses (…) after them bring up menus of available items within that category. Other orders are “quick orders.” These are commonly ordered items that have been set up with pre-defined defaults, reducing the number of prompts.

Add Orders Screen Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/028.png)

An event-delayed order is an order that is executed only after a predefined event (known as a release event) occurs. A release event can be an event such as an admission, discharge, or transfer. For example, you could write an event-delayed diet order that would not execute until a patient is transferred to a specific ward.

A CAC defines the release events at your site. (For more information on defining release events, see Appendix G of the CPRS List Manager Technical Manual or the Event- Delayed Orders topic in the CPRS GUI Technical Manual). Once a CAC has defined a release event, you can write an order that will not execute until that release event occurs.

### Placing an Event-Delayed Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To place an event-delayed order, follow these steps:

1.  From the Orders tab, select Delayed Orders by typing TD.
2.  Enter the name or number of the release event at the Select RELEASE EVENT prompt.

CPRS will return to the Orders tab screen. The name of the release event that you selected will appear at the top of the screen. If there are existing orders for that release event, they will appear on the tab.  
  
![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/029.png)

3.  Add a new order by typing NW.
4.  Enter the order as you normally would.

### Changing the Release Event of an Existing Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To change the release event of an existing order, follow these steps:

1.  From the Orders tab, select Delayed Orders by typing TD.
2.  At the Select RELEASE EVENT prompt, select the release event currently associated with the existing order.  
    >   
    > The orders associated with that release event will appear.
3.  Type the number of the order that you would like to change.  
    >   
    > ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/030.png)
4.  Select Edit Release Event by typing Edit Release at the Select Action prompt.
5.  Type No at the Remove the release event from these orders? prompt.
6.  Select a new release event at the Select RELEASE EVENT prompt.

### Removing the Release Event from an Existing Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove the release event from an existing order, follow these steps:

1.  From the Orders tab, select Delayed Orders by typing TD.
2.  At the Select RELEASE EVENT prompt, select the release event currently associated with the order.

> The orders associated with that release event will appear.

3.  Type the number of the order that you would like to change.  
    >   
    > ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/031.png)
4.  Select Edit Release Event by typing Edit Release at the Select Action prompt.
5.  Type Yes at the Remove the release event from these orders? prompt.

### Manually Releasing Event-Delayed Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To release an event-delayed order manually (before the delay event occurs) follow these steps:

> **NOTE:** You must sign an order before it can be released.

1.  From the Orders tab, select Delayed Orders by typing TD.
2.  At the Select RELEASE EVENT prompt, select the release event currently associated with the order.

> The orders that are associated with the release event will appear in a numbered list.

3.  Type the number of the order that you would like to release.

> The order that you selected will be highlighted.

4.  Select Release Orders by typing R.
5.  If the Patient Location prompt appears, enter a location.
6.  If the Enter your Current Signature Code prompt appears, enter your signature code
7.  Enter the appropriate response at the Should the orders be printed using the new location? prompt.
8.  Enter the appropriate response at the Print CHART COPY for the orders ? prompt.
9.  Enter the appropriate response at the Print LABELS? for the orders prompt  
    >   
    > ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/032.png)

### Viewing Event Delayed Orders After they are Released

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Orders tab, select Change View by typing CV.
2.  Select Auto DC/Release Event by typing A.
3.  At the Select Patient Event prompt, enter the release event associated with the orders you would like to view.

> The appropriate orders will appear on the Orders tab.

## Quick Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Quick Orders allow you to enter diets, labs, meds, etc. without going through as many steps. These are types of orders that clinicians have determined to be their most commonly ordered items, with standard collection times, routes, and other conditions. To select a quick order from the AD order screen, simply enter the number shown on your Add Orders menu (other than the \#s for the categories LABORATORY, MEDICATIONS, IMAGING, DIETETICS, etc.), then the conditions for the order are displayed for you to accept, edit, or cancel.

## Order Sets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Order sets are comprised of a group of related quick orders. The purpose is to minimize the number of prompts to answer for a common protocol or set of orders.

See your coordinator or the CPRS Set-Up Guide for instructions about creating order sets. If your site has created order sets (e.g., for admission orders, pre-op orders, etc.), you can select one from the Add Orders screen.

## Reviewing and Signing New Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- After you have entered all of your orders for a patient and you accept the default of DONE at the Select Action Prompt, you are returned to the Cover Sheet. If you enter Q to exit the patient chart, the New Orders screen is displayed and you are prompted to sign all orders you have just placed.

> You can also enter RV from other screens where Review New Orders doesn’t appear as an action (it’s on the hidden menu). You can then sign all orders, if you wish.

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/033.png)

In order to sign some medication orders, you may need to indicate whether

- Radiation
- Persian Gulf War
- Head or Neck Cancer

## Adding New Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sequence of Screens and Actions

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/034.png)

## Ordering, by Service/Category

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Movement

You can order patient movements - Admit, Transfer, Discharge, and Treating Specialty changes - with this order type.

Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/035.png)

## Ordering Parameters/Activity/Patient Care Orders/Free Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Parameters, Activity, Patient Care, and Free Text orders are different kinds of orders that are placed for nursing and ward staff to take action on. They print only at the patient’s ward/ location, and are not transmitted electronically to other Services for completion.

Examples of these various kinds of nursing orders are:

Documentation Symbols and Descriptions

| Order type   | Order                                     |
|--------------|-------------------------------------------|
| Paramters    | vital signs                               |
| Activity     | bed rest, ambulate, up in chair           |
| Patient Care | skin and wound care, drains, hemodynamics |
| Free text    | immunizations                             |

Table used for formatting purposes onlySample Documentation Symbols Descriptions. An "i" with a circle around it indicates additional information. A triangle with an exclamation point inside indicates caution.

Pre-defined nursing orders (quick orders) may be available under various sub-menus. Nursing orders may also be composed by selecting the Text Only option from the Order Screen. These orders require the ward staff to take action to complete the request.

Patient Care Orders Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/036.png)

## Ordering Diets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Press \<Enter\> after you enter each response.

1.  Select 40, Dietetics, from the Add Orders screen.
2.  Enter the number (1) from the list of diet options.
3.  At the Diet prompt, type in the specific diet. A Diet prompt appears which provides for combination diets. Each combination is entered separately, e.g. Low Sodium \<Enter\> High protein \<Enter\>. If additional types are not desired, press \<Enter\>.
4.  Enter the Effective date/time. (Automatically defaults to NOW.)
5.  Enter the Expiration date/time. (Usually +28D for Med. and Psych. and +84D for EC)
6.  Indicate the Delivery type. (Defaults to the unit’s specific policy.)
7.  The order displays. Select Edit, Cancel, or Place.

> **NOTE:** If you enter a diet request after routine meal times, you will automatically be prompted for a late tray. If needed, select the time of delivery.

## Overview of New CPRS/POE Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To make it easier for providers to enter medication orders and have fewer orders that needed to be changed by pharmacy and sent back for provider signature, the Pharmacy Ordering Enhancement (POE) project was undertaken. The aim of this project was to make it easier for clinicians to enter medication orders and have the computer do the work in the background to also get pharmacists the information they need to fill the orders appropriately.

In doing this, the ORDER DIALOG file was changed to alter how CPRS prompts clinicians for the information needed in a way that is more natural for them and will hopefully reduce the number of orders that need to be edited and sent back for signature again. Changes include removing the Dispense drug prompt and instead request a dose, using an API to ensure that the VA policy that a provider ordering a controlled substance must have a DEA or VA number, autocalculation of the quantity if a common dispense drug and a standard schedule are entered, and the availability of standard schedules to name a few.

For the List Manager interface, the changes will be seen in the dialogs that you normally use. In addition, another Medications item called Medications may have been added to your ordering menu. The Medications item can be used in addition to the existing dialogs for INPATIENT MEDS, OUTPATIENT MEDS, and IV FLUIDS. The only difference between this new dialog and the Inpatient and Outpatient dialogs is that Medications will automatically assign the ordering context (Inpatient vs. Outpatient) based on the selected patient's current admission/visit status. The Medications item provides a single dialog for medication orders instead of forcing the provider to pick among the INPATIENT MEDS, OUTPATIENT MEDS, and IV FLUIDS order dialogs. If the provider wants to use those specific dialogs, they are still available.

> Note: With the new Medications item, the provider will not be able to write a prescription if the patient is currently admitted, or order an inpatient IV med for a patient in an outpatient clinic (i.e. you won’t be able to write an order for the opposite context).

> Therefore, the old INPATIENT MEDS, OUTPATIENT MEDS, and IV FLUIDS items should still be available for the provider to use.

There are several other changes that are explained in the POE Release Notes.

## Ordering Outpatient Medications with a Simple Dose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select Medications or your normal outpatient medications menu item from your Add Order Screen (AD).
2.  Type in the medication name.
3.  Select the medication formulation.

> Note: CPRS now uses a look up from Pharmacy to check if the selected medication is a controlled substance that will require the signature of a provider with a DEA or VA number or a Schedule II (i.e., narcotics) drug that requires a wet signature (rather than an electronic one). For controlled substances, CPRS displays the message “Provider must have DEA# or VA# to order this drug!” Before an order for a controlled substance can be entered, the provider selected for the encounter must be able to sign the order. You may need to exit the dialog, change the provider, and then reenter the dialog. For a Schedule II (i.e., narcotics), the message is “This order will require a wet signature!”

> Non-formulary medications are identified by the words “non-formulary” in parenthesis to the right of the medication. For example, you might see if you type in aspirin as the medication.

> ASPIRIN SUPP,RTL (non-formulary)

4.  For a simple dose, type N and press \<Enter\>.
5.  Select the dose, if one is displayed, or enter a dose.
6.  Enter Route. (Automatically defaults to the common route for this drug).
7.  Enter a Schedule.

> A message may display indicating what the normal fill for the selected medication is.

8.  Enter a Days Supply. (The default fill is usually displayed.)
9.  Enter the Quantity needed.
10. Enter Refills. This prompt must be answered. Enter 0 if no refills are desired.
11. Enter the method of delivery (WINDOW (automatic default), clinic or mail).
12. Enter a priority.
13. Enter comments if needed or desired.
14. The prescription displays. Select Edit, Cancel, or Place.
15. Enter another medication if desired. If you are finished and want to exit, press \<Enter\>.

Example: Ordering an Outpatient Medication with a Simple Dose

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/037.png)

## Ordering Outpatient Medications with Complex Doses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select Medications or your normal outpatient medications menu item from your Add Order Screen (AD).
2.  Type in the medication name.
3.  Select the medication formulation.

> Note: CPRS now uses a look up from Pharmacy to check if the selected medication is a controlled substance that will require the signature of a provider with a DEA or VA number or a Schedule II (i.e., narcotics) that requires a wet signature (rather than an electronic one). For controlled substances, CPRS displays the message “Provider must have DEA# or VA# to order this drug!” Before an order for a controlled substance can be entered, the provider selected for the encounter must be able to sign the order. You may need to exit the dialog, change the provider, and then reenter the dialog. For a Schedule II (i.e., narcotics), the message is “This order will require a wet signature!”

> Non-formulary medications are identified by the words “non-formulary” in parenthesis to the right of the medication. For example, you might see if you type in aspirin as the medication.

> ASPIRIN SUPP,RTL (non-formulary)

4.  For a complex dose, type Y and press \<Enter\>.
5.  Select the first dose, if one is displayed, or enter a first dose.
6.  Enter Route. (Automatically defaults to the common route for this drug).
7.  Enter a Schedule.

> A message may display indicating what the normal fill for the selected medication is.

8.  Enter How Long the patient should take this dose.
9.  If you want to enter another dose, select a conjunction (the choices are and, then, or except). When you are through entering additional doses, press \<Enter\> at this prompt.
10. Repeat steps 5-9 as needed to create the complex dose.
11. Enter a Days Supply. (The default fill is usually displayed.)
12. Enter the Quantity needed. If a common dispense drug can be found, the application will try to calculate the quantity using this formula: schedule x days supply = quantity.
13. Enter Refills. This prompt must be answered. Enter 0 if no refills are desired.
14. Enter the method of delivery (WINDOW (automatic default), clinic or mail).
15. Enter a priority.
16. Enter comments if needed or desired.
17. The prescription displays. Select Edit, Cancel, or Place.
18. Enter another medication if desired. If you are finished and want to exit, press \<Enter\>.

Example: Entering an Outpatient Order with a Complex Dose

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/038.png)

Example: Entering an Outpatient Order with a Complex Dose (cont’d.)

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/039.png)

## Ordering Inpatient Medications with a Simple Dose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select Medications or your normal inpatient medications menu item from the Add Order Screen (AD).
2.  Type in the medication name.
3.  Select the medication formulation.

> Note: CPRS now uses a look up from Pharmacy to check if the selected medication is a controlled substance that will require the signature of a provider with a DEA or VA number. For controlled substances, CPRS displays the message “Provider must have DEA# or VA# to order this drug!” Before an order for a controlled substance can be entered, the provider selected for the encounter must be able to sign the order. You may need to assign a different provider for the encounter.

> Non-formulary medications are identified by the words “non-formulary” in parenthesis to the right of the medication. For example, you might see if you type in aspirin as the medication.

> ASPIRIN SUPP,RTL (non-formulary)

4.  For a simple dose, type N and press \<Enter\>.
5.  If possible doses have been entered, CPRS provides a list of possible doses. Select a listed dose or enter a dose.
6.  Enter Route. (Automatically defaults to the common route for this drug).
7.  Enter schedule, e.g., QID. Use caution when entering schedule. Use ALL uppercase, Use H for hour(s), and leave a space between time and PRN, e.g., Q4-6H PRN.
8.  CPRS shows you the next scheduled administration time. Indicate whether you want to give the first dose now.

> Note: Be careful when using “Give First Dose Now” that you do not overmedicate the patient. If you select yes to the prompt “Give First Dose Now?”, a separate order will be created for the “Now” dose and another order will be created for the other dose. Check that the combination of the Now dose and the original schedule does not overmedicate the patient.

9.  Type in provider comments, if any, e.g., X 7 days, or special instructions.
10. The order displays. Select Edit, Cancel, or Place.
11. Enter another medication if desired or at the Medication prompt, press \<Enter\>.

Example: Entering an Inpatient Medication with a Simple Dose

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/040.png)

## Ordering Inpatient Medications with a Complex Dose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select Medications or your normal outpatient medications menu item from the Add Order Screen (AD).
2.  Type in the medication name.
3.  Select the medication formulation.

> Note: CPRS now uses a look up from Pharmacy to check if the selected medication is a controlled substance that will require the signature of a provider with a DEA or VA number. For controlled substances, CPRS displays the message “Provider must have DEA# or VA# to order this drug!” Before an order for a controlled substance can be entered, the provider selected for the encounter must be able to sign the order. You may need to exit the dialog, change the provider, and then reenter the dialog.

> Non-formulary medications are identified by the words “non-formulary” in parenthesis to the right of the medication. For example, you might see if you type in aspirin as the medication.

> ASPIRIN SUPP,RTL (non-formulary)

4.  For a simple dose, type Y and press \<Enter\>.
5.  If possible doses have been entered, CPRS provides a list of possible doses. Select a listed dose or enter a dose.
6.  Enter Route. (Automatically defaults to the common route for this drug).
7.  Enter schedule, e.g., QID. Use caution when entering schedule. Use ALL uppercase, Use H for hour(s), and leave a space between time and PRN, e.g., Q4-6H PRN.
8.  Enter for how long (the number of days).
9.  Select a conjunction (and or then) if you want to enter another dose, or when finished with dosing information, press \<Enter\> to go to the next prompt.
10. Repeat steps 5-9 until you have the dose as you want it.
11. Indicate whether you want to give the first dose now.

> Note: Be careful when using “Give First Dose Now” that you do not overmedicate the patient. If you select yes to the prompt “Give First Dose Now?”, a separate order will be created for the “Now” dose and another order will be created for the other dose. CPRS also display a message: “First Dose NOW is in addition to those already entered. Please adjust the duration of the first one, if necessary.” Check that the combination of the Now dose and the original schedule does not overmedicate the patient.

12. Type in provider comments, if any, e.g., X 7 days, or special instructions.
13. The order displays. Select Edit, Cancel, or Place.
14. Enter another medication if desired or at the Medication prompt, press \<Enter\>.

Example: Entering an Inpatient Order with Complex Dosing

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/041.png)

## Ordering IV Fluids

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select IVs.from the Add Order Screen (AD).
2.  Available options are displayed; for example:
- IV FLUIDS (WITH ADMIXTURE)...
- IV MEDS...
- \[others, e.g., IV FLUIDS (NO ADDITIVES)...\]
3.  A fluid with NO ADDITIVE leads to the free text/word-processing screen for order entry.
4.  A fluid with an ADMIXTURE leads to the IV pharmacy package.
    1.  Type in fluid desired (Use ?? for available selections). Entering a BASE fluid, i.e., D5, produces a fluid selection list containing that base.
    2.  Enter Volume of fluid if different from default.
    3.  Enter Additive by typing in the name of the additive.
    4.  Additive will again be prompted for to allow for additional additives. Bypass by pressing \<Enter\> if no other additives are desired.
    5.  Enter infusion rate in number(s) only. The numeric indicates the rate in cc/hr. Pharmacy uses ML/HR.
    6.  Enter provider comments if desired, e.g. -- \# of days or special instructions, e.g. MVI in one bag per day. NOTE-Placing the name of an additive as a comment DOES NOT constitute a valid order unless it is also entered at the Additive prompt.
    7.  The order displays. Select Edit, Cancel, or Place.
    8.  Respond Y or N to the prompt for another request.

> **NOTE:** An IV MEDICATION leads to the Inpatient Medication package. Answer these prompts like any other inpatient medication. If you enter an IV MEDICATION with more than one additive, it will be saved as an IV FLUID so that all additives can be saved and displayed.

## Ordering Imaging or Radiology Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select the radiology procedure from the Common Radiology Procedure List by entering the appropriate number. This list automatically displays (enter ?? for additional choices).
2.  Enter Modifier(s) if appropriate, e.g., Right, Portable (enter ?? for a complete list of choices).
3.  Enter a Reason for the Request.
4.  The order displays. Select Edit, Cancel, or Place.
5.  Respond Y or N to the prompt for Another Request.

## Ordering Labs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter the name of the lab tests desired.
2.  Choose the method of collection Send to Lab, Ward Collect and Deliver, Lab Blood Team, or Immediate Collect by Lab Team.
3.  Enter the collection date and time, e.g., T+3@0500, or Now.
4.  Enter the Urgency.
5.  Enter how often. (NOTE: If you select that this order will be done multiple times, a + will appear in front of the Lab order on the Orders screen).
6.  The choices you have made are displayed.
7.  Choose place, edit, or cancel.

> NOTE: An Order Check notice such as the following might appear. This notice states that an order is a duplicate of a previously placed order for this patient. You have the option to place, edit, or cancel the order, based on this information.

> ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/042.png)

## Ordering Consults & Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select 90, Other Orders, from the Add Orders screen.
2.  Enter the service/specialty you’re requesting the consultation from.
3.  Enter the reason for the request.
4.  Specify whether the service rendered will be on an inpatient or outpatient basis.
5.  Enter the urgency for the consultation (stat, routine, within 48 hours, or within 72 hours).
6.  Enter the place of Consultation (bedside or consultant’s choice).
7.  Enter the provisional diagnosis.

> Note: CPRS checks if the diagnosis code is active as of the entry date as specified in Code Set Versioning (CSV). If the code is inactive, the user must change the code before proceeding. The check would occur on copy and change as well.

8.  A list of the categories and their responses is displayed; verify or edit these by selecting Place, Edit, or Cancel.
9.  You can now add another consult order or exit.

# Meds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can review and order Meds either through the Meds tab in Chart Contents or through the Add New Orders option on the Orders tab.

Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/043.png)

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/044.png)

Meds Detailed Display

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/045.png)

## Meds Change View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Change View in Meds lets you change your view from Inpatient to Outpatient or to change the date range.

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/046.png)

> **NOTE:** The Active status for outpatient meds will display as “active (susp)” to improve clarity.

# Labs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can review and order Labs either through the Labs tab in Chart Contents or through the Add New Orders option on the Orders tab.

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/047.png)

## Lab Change View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Change View in Lab lets you change the date range to be displayed, to go to a specific section of Lab to see results, or to use a list format for display. Examples of the Go To a Section and List Format are shown here.

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/048.png)

Go To a Section Example:

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/049.png)

Go To a Section Example, cont’d:

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/050.png)

Use List Format Example:

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/051.png)

# Consults

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can enter, edit, and review consult and procedure requests through CPRS.

1.  Go into the Clinician Menu and select OE for CPRS Clinician Menu.
2.  The patient selection screen appears, with your personal patient list if you’ve created one (through Personal Preferences).
3.  Select a patient from the list, or enter another one.
4.  The Cover Sheet for this patient appears.

Example:

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/052.png)

5.  Choose Chart Contents and then Consults (Shortcut: CC;CONS).
6.  The Consults screen appears with a list of consults for this patient, and possible actions you can perform at this time (e.g., order a new consult or procedure).

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/053.png)

7.  You can also see more details about any of the consults listed, view results for completed consults, or you can print the Consult Form 513, by entering the number of one of the consults and then the appropriate action’s initial.

> ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/054.png)

> Results Display

> ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/055.png)

8.  You can now print a 513, order new consults or procedures, return to Chart Contents, select a new patient, or exit from the patient’s chart.
+ NOTE: Occasionally a consult result is linked to the wrong consult. Information on how to make corrections is contained in the Consult/Request Tracking documentation.

# Imaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can review Radiology results by choosing the Imaging tab in Chart Contents or by selecting Results Reporting from the Clinician menu. You can also order new tests through the Imaging tab or by going through the Add New Orders option on the Orders tab.

To review Radiology Results:

1.  After selecting a patient, select Chart Contents and then the Imaging tab.
2.  The following screen appears:

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/056.png)

3.  The Imaging Procedures screen appears:

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/057.png)

## Change View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action in Imaging lets you change your view to a different date range or

a smaller number of items.

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/058.png)

# D/C Summaries 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can review, edit, and write new Discharge Summaries through CPRS.

1.  Select D/C Summaries from Chart Contents.
2.  If one or more Discharge Summaries are listed, select a number of one you wish to review or take action on. If you pick Detailed Display, the entire Discharge Summary is displayed (screen-by-screen) in the List Manager list area.

> ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/059.png)

3.  New actions are displayed on the screen; select one of these.

> ![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/060.png)

Discharge Summary Detailed Display Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/061.png)

# Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can view or print reports and results from either the Results Reporting option on the Clinician Menu or from the Reports tab on the Chart Contents screen. The Reports tab only lets you print for individual patients. The RR option lets you select more than one patient at a time.

Reports Tab

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/062.png)

Example: Shortcut:

Select CC;R

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/063.png)

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/064.png)

Lab Cumulative Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/065.png)

Dietetic Profile Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/066.png)

Health Summary Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/067.png)

## Results Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can print reports for multiple patients (e.g., all of the patients in a ward, or all of a patients on a Personal or Team List) through the Results Reporting option on the Clinician Menu.

Order Summary for Date/Time Range Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/068.png)

Order Summary for Date/Time Range Example, cont’d

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/069.png)

# Personal Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can change many of the parameters that control the way CPRS works for you. The Personal Preferences Menu on your Clinician Menu contains sub-menus that may allow you to change which notifications and order checking messages you get, the team or personal lists you will use, and the default patients you’ll have.

## Personal Preferences Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Option or Menu</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GUI Cover Sheet Display Parameters</td>
<td>This option lets you modify the default number of days to display on the cover sheet.</td>
</tr>
<tr class="even">
<td>Notification Mgmt Menu</td>
<td>This menu contains an option that allows you to review the notifications you should be currently receiving. You may also have an option for adding or removing notifications to those you are scheduled to receive (whether you have this depends on local site set-up). Use this option to turn notifications on or off. You may also be able to remove all of your existing notifications via a purge option.</td>
</tr>
<tr class="odd">
<td>Order Checking Management Menu</td>
<td>This menu contains one or two options (depending on local set-up) which allow you to check which order checks you get and possibly to set parameters for order checking.</td>
</tr>
<tr class="even">
<td>Personal Patient List Menu</td>
<td><p>Options on this menu allow clinicians to create patient lists by ward, clinic, or by patient to use for displaying results or creating reports. You can build lists, delete lists, merge lists,</p>
<p>add or remove patients from lists, or inquire to a file of patient lists.</p></td>
</tr>
<tr class="odd">
<td>Patient Selection Preference Mgmt</td>
<td>This menu allows you to set default parameters for patient lists.</td>
</tr>
<tr class="even">
<td>Display Patients Linked to Me via Teams</td>
<td>This option displays patients linked to the current user via teams from the OE/RR LIST file [#100.21].</td>
</tr>
<tr class="odd">
<td>Display My Teams</td>
<td>This option displays teams linked to the current user.</td>
</tr>
</tbody>
</table>

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

To access the Personal Preferences Menu:

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/070.png)

## GUI Cover Sheet Display Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/071.png)

## Notification Mgmt Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options may be available on your Personal Preference Menu, depending on how your local coordinators have set up your menus.

| Option                                        | Description                                                                                                                                                                                                                                                                                        |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enable/Disable My Notifications               | If you have this option, you can indicate that a notification should not be processed for you.                                                                                                                                                                                                     |
| Erase All of My Notifications                 | Use this option to erase all of your own notifications.                                                                                                                                                                                                                                            |
| Send me a MailMan bulletin for Flagged Orders | Enter Yes to send a bulletin to the order’s Current Provider (usually the Ordering Provider) when an order is flagged for clarification. This parameter has no effect on the Flagged Orders notification which is also triggered when an order is flagged for clarification.                       |
| Set Notification Display Sort Method (GUI)    | Method for sorting notifications when displayed in the GUI, including by Patient, Type (Notification name), and Urgency. Within these sort methods notifications are presented in reverse chronological order.                                                                                     |
| Send me a MailMan Bulletin for Flagged Orders | If this is turned on, a MailMan bulletin is sent to the order's Current Provider (usually the Ordering Provider) when the order is flagged for clarification. This parameter has no effect on the Flagged Orders notification, which is also triggered when an order is flagged for clarification. |
| Show Me the Notifications I Can Receive       | This option displays if and why you are a recipient for each notification.                                                                                                                                                                                                                         |
| Set Surrogate to Receive My Notifications     | Sets up a surrogate to receive all notifications (OE/RR alerts) for you.                                                                                                                                                                                                                           |

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

Show Me the Notifications I Can Receive

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/072.png)

Show Me the Notifications I Can Receive, cont’d

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/073.png)

Explanations of ON/OFF For This User and Why

<table>
<caption>Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th>Reason</th>
<th>Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Division/System value is Mandatory</td>
<td>Either the site or the CPRS package determined that a notification is mandatory for either a division or a hospital.</td>
</tr>
<tr class="even">
<td>OERR value is Mandatory</td>
<td>The notification is exported as mandatory.</td>
</tr>
<tr class="odd">
<td>OERR value is Disabled</td>
<td>The site disabled the mandatory status of an exported notification.</td>
</tr>
<tr class="even">
<td>No Disabled values found</td>
<td><p>No one (a manager, coordinator, or user) has disabled this</p>
<p>notification.</p></td>
</tr>
<tr class="odd">
<td>User value is Disabled</td>
<td>A manager, coordinator, or user disabled this notification for this user.</td>
</tr>
</tbody>
</table>

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

Disabling a Notification Example

The process for disabling a notification seems counter-intuitive. When the program asks if you want to add a new Notification, logically you’d want to say “No,” but the program is really asking if you want to add a new notification to a temporary list for consideration about enabling or disabling. The program is using a generic FileMan callwe hope that in the near future a more user- friendly utility will be written for this option.

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/074.png)

Order Checking Mgmt Menu

| Reason                                     | Explanation                                                                                                                          |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| Show Me the Order Checks I Can Receive     | This option processes each order check to determine if and why you receive an order check message during the ordering process.       |
| Enable/Disable an Order Check for Yourself | A list of available order checks is displayed when you enter a question mark. You can then select order checks to enable or disable. |

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

Enable/Disable an Order Check for Yourself Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/075.png)

## Personal Patient List Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CACs can help setup team lists for groups of clinicians and related hospital personnel. Clinicians can create patient lists by ward, clinic, or by patient to use for displaying results or creating reports. You can build lists, delete lists, merge lists, add or delete patients from lists, or inquire to a file of patient lists.

If you have a list defined and loaded (as determined in the Personal Preferences options), the list will be available every time you select the CPRS Clinician Menu. You then select a patient from the list. This list can also be used for printing reports.

The team lists also help determine who receives notifications for patients defined on the lists.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 13%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Synonym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Build Patient List Menu</td>
<td>AD</td>
<td><p>Options on this menu allow you to create patient lists by patient, ward, or clinic. These lists can then be used to display results or to print reports, or can be merged with</p>
<p>other lists.</p></td>
</tr>
<tr class="even">
<td>Delete Existing List(s)</td>
<td>DE</td>
<td>When you no longer need a patient list that you have built, you can use this option to delete the list.</td>
</tr>
<tr class="odd">
<td>Examine/ Print Existing List(s)</td>
<td>EX</td>
<td><p>This option allows you to examine or print an existing</p>
<p>patient list.</p></td>
</tr>
<tr class="even">
<td>Load Primary Patient List</td>
<td>LO</td>
<td>This option loads into the current session the user’s primary patient list.</td>
</tr>
<tr class="odd">
<td>Merge Existing Lists</td>
<td>ME</td>
<td>This option lets you merge the patients from one or several lists together to create a bigger or more comprehensive list.</td>
</tr>
</tbody>
</table>

Build Patient List Menu Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/076.png)

## Patient Selection Preference Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options that let you set default parameters for patient lists.

<table>
<caption>Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1. Display Your Patient List Source</td>
<td>This option lets you display a user’s default patient list source.</td>
</tr>
<tr class="even">
<td>2. Set My Preferred Clinic Friday</td>
<td>This option lets you specify the clinic that will be the default source of Friday's patient list.</td>
</tr>
<tr class="odd">
<td>3. Set My Preferred Clinic Monday</td>
<td>This option lets you specify the clinic that will be the default source of Monday's patient list.</td>
</tr>
<tr class="even">
<td><p>4. Set My Preferred Clinic</p>
<p>Saturday</p></td>
<td><p>This option lets you specify the clinic that will be the</p>
<p>default source of Saturday's patient list.</p></td>
</tr>
<tr class="odd">
<td>5. Set My Preferred Clinic Start Date</td>
<td>Patients with appointment dates as early as this date will be added to the Clinic List. Patients will be added with appointment dates between START DATE and STOP DATE.</td>
</tr>
<tr class="even">
<td>6. Set My Preferred Clinic Stop Date</td>
<td>Patients with appointment dates as recent as this date will be added to the Clinic List.Patients will be added with appointment dates between START DATE and STOP DATE.</td>
</tr>
<tr class="odd">
<td>7. Set My Preferred Clinic Sundays</td>
<td>This option lets you specify the clinic that will be the default source of Sunday's patient list.</td>
</tr>
<tr class="even">
<td>8. Set My Preferred Clinic Thursday</td>
<td><p>This option lets you specify the clinic that will be the</p>
<p>default source of Thursday's patient list.</p></td>
</tr>
<tr class="odd">
<td>9. Set My Preferred Clinic Tuesday</td>
<td>This option lets you specify the clinic that will be the default of Tuesday's patient list.</td>
</tr>
<tr class="even">
<td>10. Set My Preferred Clinic Wednesday</td>
<td><p>This option lets you specify the clinic that will be the</p>
<p>default source of Wednesday's patient list.</p></td>
</tr>
<tr class="odd">
<td>11. Set My Preferred List Source</td>
<td>This option lets you specify the default preference for patient list source.</td>
</tr>
<tr class="even">
<td>12. Set My Preferred Provider</td>
<td><p>Provider who is basis for building the Provider List of</p>
<p>patients.</p></td>
</tr>
<tr class="odd">
<td>13. Set My Preferred Sort Order for Patient List</td>
<td><p>This option lets you specify the default sort order for the patient list. Room/Bed is valid only for inpatients list (Ward, Team/Personal, Provider, Specialty).</p>
<p>Appointment Date is valid only for outpatient lists</p>
<p>(Clinic)</p></td>
</tr>
<tr class="even">
<td>14. Set My Preferred Team List</td>
<td>This option lets you specify the Team/Personal list to be the default source of patients.</td>
</tr>
<tr class="odd">
<td>15. Set My Preferred Treating Specialty</td>
<td>This option lets you specify the Treating Specialty used as a source for patients on the Specialty List.</td>
</tr>
<tr class="even">
<td>16. Set My Preferred Ward</td>
<td><p>This option lets you specify the Ward that will be the</p>
<p>default list of patients.</p></td>
</tr>
</tbody>
</table>

Table used for formatting purposes onlySample Tier Support Contact Information, including name, role, organization, and contact information.

Display Your Patient List Source Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/077.png)

## Display Patients Linked to Me via Teams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lets you see what patients are on teams that you are currently on.

Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/078.png)

## Display My Teams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lets you see what teams you are currently on.

Example

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/079.png)

# Helpful Hints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- ACTIONS

> Actions (also known as protocols) are the items listed on the bottom part of the list manager screens. Sometimes these are processes that you can perform on screen items (processes such as sign, print, discontinue, renew, etc.), and sometimes they are the names of other screens (chart tabs) that you can go to.

> NOTE: Order actions in CPRS work differently from OE/RR. In CPRS, you must pick an order from the review screen before the available actions appear at the bottom of the screen. In OE/RR the actions were visible at the bottom of the review screen before you selected an order.

- CHART TABS

> Chart Tabs are another name for the Chart Contents actions or pages. They allow you the following choices: Orders, Notes, Meds, Lab, D/C Summaries, and Problem Lists. (They are called Tabs to be consistent with the GUI version of CPRS, which uses the Windows convention of having tab-like graphic images for selecting options.) If you select one of these tabs, you will be given the option of NW. This allows you to write new notes, meds, labs, and problems without going through the order screen. You may also view results relating to these tabs by using the following steps: (1) Select CC; (2) Select a tab; e.g., consults, lab, (3) Select the number of the item you want information on, (4) Select Detailed Display.

- CONSULTS

> Consults may be ordered via CPRS by selecting Other from the Add Orders screen or by selecting the Consults tab. You can also see Consults results through CPRS.

- DETAILED DISPLAY

> When you select the action Detailed Display (DD) you can see additional information about an order, including Who entered the order, what physician or nurse initiated the order, and the date the order was entered or discontinued. You may view this information by selecting the number of the order in question, and then choosing Detailed Display .

- ELECTRONIC SIGNATURE

> An Electronic signature must accompany all orders entered by a physician, nurse practitioner, or physician’s assistant. These orders are not released to the services until signed (except for verbal orders). For outpatient medications, the order must be signed by an authorized provider. Verbal, telephoned, and written orders cannot be released to the pharmacy until they are signed.

> Note: The purpose of this is to comply with VHA policy. You can read the policy on the intranet at http://vaww.va.gov/pub/direc/health/manual/020704.htm.

- EXPIRED MED ORDERS

> Expired Med orders remain on the order screen for a time designated by your site.

- \>\> INDICATORS

> The “greater-than” symbols (\>\>) beside an order indicates that this order needs to be completed or have action taken by a nurse or ward clerk.

> When \>\> is shown in the black bar of the List Manager screen, it means that more information is available to the right of the screen; enter one or more of these symbols to see this information.

- INORDERABLE ITEM IN PHARMACY

> This is a notation that is seen when the pharmacy has changed its dispense drugs. An inorderable item can’t be renewed. The med in question can be continued by choosing the Change option, which automatically DCs the original and creates a new order that will be renewable thereafter. The Change option takes you through each field of the medication and allows you to edit as needed.

- LAB TIP

> To change a lab urgency “on-the-fly”: When you select a quick order from the menu, enter the number of the item followed by =\*.

- MEDICATION ENTRY TIPS
  1.  Always use upper case when entering the schedule. The approved abbreviation for hours is H. If other letters are listed, such as hr or hrs, the pharmacy package doesn’t read the schedule accurately, and incorrect times will appear on your MARS. Currently administration times can be edited under the Unit Dose option only.
  2.  Enter the Schedules for these orders as follows: Insulin BID  
      > BID-INSULIN  
      > ISMO BID-ISMO PRN  
      > Q4-6H PRN
  3.  Multiple Meds may be renewed or discontinued by selecting the order numbers, pressing enter, and choosing Renew or DC.
  4.  Hard copies of orders automatically print to the service(s).
  5.  Meds for discharge or pass can be selected and converted to outpatient status. This prevents the need for carbon copies of orders with original signatures. To place Meds on hold, enter a free-text order. Pharmacy considers orders to be either active or discontinued. They do not act on Hold orders. This is an action taken only by a unit’s nursing staff.
  6.  If an order is questioned by pharmacy, it will be flagged, stating the reason for the flag, and the physician receives a View Alert. A Med can be unflagged if you choose the Med in question and then select UNFLAG.
  7.  Verbal orders cause a View Alert to be automatically generated for the physician who needs to electronically sign the order.
- NOTES

> Progress Notes can be accessed directly from the patient’s chart or through TIU as a separate menu option.

- PATIENT LISTS

> You can set up a specific list as your default. To enter a list, choose CHANGE VIEW (CV), then select WARD, CLINIC, or PROVIDER, etc., enter the name of the group (e.g., 2 west), then choose SV to save the list. This list must be saved after its selection for it to become your default. To change from one chart to another, the SP (Select Patient) choice returns the screen to your default list where you can select another patient. You may also enter a patient from another area of the unit by choosing FD (Find Patient) and entering the patient’s name. FD can be used even if you already have another unit loaded as your default list.

- QUICK ORDERS

> Quick Orders allow you to enter labs and meds without going through as many steps. They are selected from the AD order screen by simply selecting a number (other than the \#s for the categories LABORATORY, MEDICATIONS, IMAGING, DIETETICS, etc.). Quick Orders are ones that physicians have determined to be their most commonly ordered items and have standard collection times, routes, and other conditions.

- REPORTS

> Reports for individual patients are available from the Reports tab. Reports for a ward/clinic can be found under the Results Reporting menu option. To print a Ward Summary, follow these steps:

1.  Select Results Reporting
2.  Select patient or patients
3.  Enter the range of numbers you want
4.  Choose \#8 to print Daily Order Summary, or \#11 for Chart Copies of orders
5.  Enter date range
6.  Answer Yes to Display only those orders placed on this day: NO//
7.  Enter a printer name or hit ENTER at the DEVICE: HOME// prompt (This can also be queued)

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>Table used for formatting purposes onlyGlossary </caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>+ A plus sign (+) in front of a Progress Note indicates that the note has addenda. A + in front of a lab order indicates that this lab test will be done multiple times according to a selected schedule.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>&gt;&gt; These arrows (displayed in the center black bar) indicate that more information can be seen by scrolling to the left. If they are displayed beside an order, it means that a nurse or clerk needs to take action on the order.</td>
</tr>
<tr class="even">
<td></td>
<td>CPRS Computerized Patient Record System, the VISTA package (in both GUI and character-based formats) that provides access to most components of the patient chart.</td>
</tr>
<tr class="odd">
<td></td>
<td>ASU Authorization/Subscription Utility, a VISTA application (initially released with TIU) that allows VAMCs to assign privileges such as who can do what in ordering, signing, releasing orders, etc.</td>
</tr>
<tr class="even">
<td>Chart Contents</td>
<td><p>The various components of the Patient Record, equivalent to the</p>
<p>major categories of a paper record; for example, Problem List, Progress Notes, Orders, Labs, Meds, Reports, etc. In CPRS, these components are listed at the bottom of the screen, to be selected individually for performing actions.</p></td>
</tr>
<tr class="odd">
<td></td>
<td>Consults Consult/Request Tracking, a VISTA product that is also part of CPRS (it can function as part of CPRS, independently as a standalone package, or as part of TIU). It’s used to request and track consultations or procedures from one clinician to another clinician or service.</td>
</tr>
<tr class="even">
<td></td>
<td>Cover Sheet A screen of the CPRS patient chart that displays an overview of the patient’s record.</td>
</tr>
<tr class="odd">
<td>CWAD</td>
<td><p>Crises, Warnings, Allergies/Adverse Reactions, and Directives.</p>
<p>These are displayed on the Cover Sheet of a patient’s computerized record, and can be edited, displayed in greater detail, or added to. See Patient Postings.</p></td>
</tr>
<tr class="even">
<td>D/C Summary</td>
<td>Discharge Summary; see below.</td>
</tr>
<tr class="odd">
<td>Discharge Summary</td>
<td><p>A component of TIU that can function as part of CPRS, Discharge</p>
<p>Summaries are recapitulations of a patient’s course of care while in the hospital.</p></td>
</tr>
<tr class="even">
<td></td>
<td>GUI Graphical User Interface—a Windows-like screen with pull-down menus, icons, pointer device, etc.</td>
</tr>
<tr class="odd">
<td></td>
<td>Health Summary A VISTA product that can be viewed through CPRS, Health Summaries are components of patient information extracted from other VISTA applications.</td>
</tr>
<tr class="even">
<td></td>
<td>Imaging A VISTA product that is also a component of CPRS; it includes Radiology, X-rays, Nuclear Medicine, etc.</td>
</tr>
<tr class="odd">
<td>Notifications</td>
<td><p>Alerts regarding specific patients that appear on the CPRS patient</p>
<p>chart. They can be responded to through “VA View Alerts.”</p></td>
</tr>
<tr class="even">
<td></td>
<td>OE/RR Order Entry/Results Reporting, a VISTA product that evolved into the more comprehensive CPRS.</td>
</tr>
<tr class="odd">
<td></td>
<td>Order Checking A component of CPRS that reviews orders as they are placed to see if they meet certain defined criteria that might cause the clinician placing the order to change or cancel the order (e.g., duplicate orders, drug-drug/diet/lab test interactions, etc.).</td>
</tr>
<tr class="even">
<td></td>
<td>PCMM Patient Care Management Module, a VISTA product that manages patient/provider lists.</td>
</tr>
<tr class="odd">
<td>Patient Postings</td>
<td><p>A component of CPRS that includes messages about patients; an</p>
<p>expanded version of CWAD (see above).</p></td>
</tr>
<tr class="even">
<td>Progress Notes</td>
<td>A component of TIU that can function as part of CPRS.</td>
</tr>
<tr class="odd">
<td></td>
<td>Quick Orders Quick Orders allow you to enter many kinds of orders without going through as many steps. They are types of orders that physicians have determined to be their most commonly ordered items and that have standard collection times, routes, and other conditions.</td>
</tr>
<tr class="even">
<td></td>
<td>Reports A component of CPRS that includes Health Summary, Action Profile, and other summarized reports of patient care.</td>
</tr>
<tr class="odd">
<td></td>
<td><p>TIU Text Integration Utilities; a package for document handling, that includes Consults, Discharge Summary, and Progress Notes, and will later add other document types such as surgical pathology reports.</p>
<p>TIU components can be accessed for individual patients through the CPRS, or for multiple patients through the TIU interface.</p></td>
</tr>
<tr class="even">
<td></td>
<td>VISN Veterans Information System Network, the regional organizations for managing computerization within a region.</td>
</tr>
<tr class="odd">
<td></td>
<td>VISTA Veterans Information Systems Technology Architecture, the new name for DHCP.</td>
</tr>
</tbody>
</table>
Table used for formatting purposes onlyGlossary

# # Appendix: Screen Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Actions available, by tab

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/080.png)

![](cprs-user-manual-list-manager-clinician-s-getting-started-guide/081.png)