---
title: OR*3.0*539 (CPRS v32a) Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: (CPRS v32a)
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3.0
patch_id: OR*3.0*539
group_key: "CPRS:OR:3.0"
file_numbers: []
security_keys: []
menu_options: 5
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - cprs
  - order
  - notes
  - table
  - contents
  - release
  - hitps
  - added
  - notification
  - allergy
page_count: 0
word_count: 5105
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_0_539_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_0_539_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

---
title: |
  <span id="_Hlk36805776" class="anchor"></span>Computerized Patient Record System GUI v32a

  Release Notes

  ![](or-3-0-539-cprs-v32a-release-notes/001.png)
---

January 2024

Office of Information and Technology (OI&T)

Revision History

<table>
<caption>Revision HistoryThis table lists the history for each revision of this document by row in descending order</caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 17%" />
<col style="width: 34%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version/Patch</th>
<th>Change</th>
<th>Project Manager</th>
<th>Technical Writer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>01/2024</td>
<td>OR*3.0*615</td>
<td><p>Added <a href="#_Surrogate_Settings_(NSR">NSR 20071216</a>, and <a href="#similar-provider-lookup-improvements-nsr-20140211">NSR 20140211</a> to New Features and Functions Added.</p>
<p>Added <a href="#hitps_196">HITPS 196</a>, <a href="#hitps_1131">HITPS 1131</a>, and <a href="#hitps_1711">HITPS 1711</a> to Patient Safety Issue.</p>
<p>Added <a href="#new_7499">HITPS-7499</a> to INC13521395</p>
<p>Added <a href="#write_orders">Write Orders Menu</a> to the Defect Tracking System Items.</p></td>
<td>CPRS development team</td>
<td>CPRS development team</td>
</tr>
</tbody>
</table>

Revision HistoryThis table lists the history for each revision of this document by row in descending order

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [Audience](#audience)
- [This Release](#this-release)
  - [Non-CPRS Features that Affect CPRS Functionality](#non-cprs-features-that-affect-cprs-functionality)
  - [New Features and Functions Added](#new-features-and-functions-added)
    - [Real-Time Notification of Potentially Missed Order Checks (NSR 20060710)](#real-time-notification-of-potentially-missed-order-checks-nsr-20060710)
    - [Allergy Order Check Enhancement (NSR 20070203)](#allergy-order-check-enhancement-nsr-20070203)
    - [Order Flag Recommendations (NSR 20110719)](#order-flag-recommendations-nsr-20110719)
    - [Change in Unflagging Capabilities (NSR 20071103)](#change-in-unflagging-capabilities-nsr-20071103)
    - [Update Surrogate Management Functionality within CPRS GUI (NSR 20171216)](#update-surrogate-management-functionality-within-cprs-gui-nsr-20171216)
    - [Adverse Reaction Reporting File Modification (NSR 20120404)](#adverse-reaction-reporting-file-modification-nsr-20120404)
    - [Progress Notes Display Misleading (Addresses HITPS-397) (NSR 20070817)](#progress-notes-display-misleading-addresses-hitps-397-nsr-20070817)
    - [Identify Required Fields in TIU Note Templates and Notify of Missing Required Fields (NSR 20100706)](#identify-required-fields-in-tiu-note-templates-and-notify-of-missing-required-fields-nsr-20100706)
    - [Create Separate Alert for Prosthetics (NSR 20110210)](#create-separate-alert-for-prosthetics-nsr-20110210)
    - [Confirm Provider Selected with Similar Names (NSR 20110606)](#confirm-provider-selected-with-similar-names-nsr-20110606)
    - [Limiting Additional Signers List (NSR 20120101)](#limiting-additional-signers-list-nsr-20120101)
    - [Nature of Order Default (NSR 20120601)](#nature-of-order-default-nsr-20120601)
    - [VistA Evolution Anatomic Pathology Order Dialogs (NSR 20140511)](#vista-evolution-anatomic-pathology-order-dialogs-nsr-20140511)
    - [CPRS Modification Unified Action Profile (NSR 20130714)](#cprs-modification-unified-action-profile-nsr-20130714)
    - [First Dose Now (NSR 20130802)](#first-dose-now-nsr-20130802)
    - [Surrogate Settings (NSR 20071216)](#surrogate-settings-nsr-20071216)
    - [Similar Provider Lookup Improvements (NSR 20140211)](#similar-provider-lookup-improvements-nsr-20140211)
  - [Patient Safety Issues](#patient-safety-issues)
  - [Defect Tracking System Items](#defect-tracking-system-items)
  - [Known Issues](#known-issues)
- [New Parameters](#new-parameters)
- [Modified Parameters](#modified-parameters)
- [Product Documentation](#product-documentation)
These Release Notes describe the new features and changes to the CPRS software that are a part of CPRS GUI version 32a, which includes both a GUI executable and an M patch, OR\*3.0\*539.
CPRS GUI v32a includes new features, enhancements to existing features, and defect corrections.
Below is a list of all the applications involved in this project along with their patch numbers:
APPLICATION/VERSION PATCH
-------------------------------------------------------------------------------------------------------
TEXT INTEGRATION UTILITIES v1.0 TIU\*1.0\*339
ADVERSE REACTION TRACKING v4.0 GMRA\*4.0\*63
CONSULT/REQUEST TRACKING v3.0 GMRC\*3.0\*84  
GEN. MED. REC. – VITALS v5.0 GMRV\*5.0\*43  
MENTAL HEALTH V5.01 YS\*5.01\*170
LAB SERVICE V5.2 LR\*5.2\*544
ORDER ENTRY/RESULTS REPORTING v3.0 OR\*3.0\*539
The patches are being released in the KIDS multi-package build, CPRS V32A COMBINED BUILD 1.0.

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes summarize the changes to CPRS GUI v32a.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets CPRS GUI v32a users and administrators.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions, enhancements and modifications to the existing software, and any known issues for CPRS GUI v32a.

## Non-CPRS Features that Affect CPRS Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There were no changes in software outside of CPRS that affected CPRS functionality.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the new and enhanced features and functions added to the CPRS GUI v32a release.

### Real-Time Notification of Potentially Missed Order Checks (NSR 20060710)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you enter a patient allergy, the CPRS GUI now displays a warning if a reactant selected is a drug ingredient that will not support a drug allergy order check at the drug class level.

After you enter a new allergy, if you click on any drug ingredient listed in the Drug Ingredients File dropdown, you will get a notification that Drug Class cross checking will not occur unless you check the checkbox, as shown in the screenshot below. The notification is highlighted in red for emphasis. This change fixes patient safety items in [HITPS 196](#hitps_196).

![](or-3-0-539-cprs-v32a-release-notes/002.png)

### Allergy Order Check Enhancement (NSR 20070203)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a new allergy is documented for a patient with an active drug profile, that new allergy is now compared to the active profile for any potential adverse reactions.

The system now checks the current active Patient Medication Profile against any new allergy/ADR entries using CPRS, VistA IP/OP Pharmacy and Adverse Reaction Tracking.

If an Active medication order is found, the system will show users that a notification will be sent to providers. The notification is based on recipients for the NEW ALLERGY ENTERED/ACTIVE MED notification. A user can add additional recipients to receive this notification. Upon selection of the notification in the CPRS GUI, the user will be taken to view the appropriate order.

Here is an example of the allergy order check enhancement on an existing medication order, which will be found when a new allergy is entered:  
  
![](or-3-0-539-cprs-v32a-release-notes/003.png)

In the screenshot below, a user enters a new allergy for the existing medication order and clicks OK, successfully entering the new allergy.  The existing medication search will begin at this time.  
  
![](or-3-0-539-cprs-v32a-release-notes/004.png)  
  
If an existing medication is found, the user will see a notification.  If more than one medication order is found, the user will see multiple dialogs, one after the other listing the appropriate information.  The notification shows 1) the existing medication order name and order number, and 2) the list of recipients based on the order and the Set Provider Recipients for Notifications \[ORB3 PROVIDER RECIPIENTS\] option settings for the notification. The user will be able to add additional notification recipients.  
  
![](or-3-0-539-cprs-v32a-release-notes/005.png)  
  
The notification will display with the text "Review New Allergy Entered on Active Med".  When a user processes the alert, it gets processed for all other recipients.

![](or-3-0-539-cprs-v32a-release-notes/006.png)  
  
Processing the notification on the CPRS GUI will take the user to the Orders tab and display the New Allergy Conflict view. It will list the specific Order related to the notification processed.

![](or-3-0-539-cprs-v32a-release-notes/007.png)

A new clinical report has been added to the Reports tab. When the user clicks on Pharmacy Active Meds With Allergies, a list of reports of medications affected by an allergy entered for a patient will appear. When the user clicks on a report, details about the allergy and the medication will appear.

![](or-3-0-539-cprs-v32a-release-notes/008.png)

### Order Flag Recommendations (NSR 20110719)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several enhancements to the Order Flag functionality:

- On the Flag Order screen, the Reason field now allows up to 240 characters, you can select multiple recipients to receive the alert and you can set up a “No Action Alert”, an informational alert that the user doesn’t need to act on. In the screenshot below, the user has changed the “No Action Alert” date by clicking on the ellipsis and three recipients have been added.  
    
  ![](or-3-0-539-cprs-v32a-release-notes/009.png)
- The GUI Parameter Menu has a new menu option, GUI Order Flagging/Unflagging Setup, which contains the following flagging parameter: OR FLAG ORDER EXPIRE DEFAULT. This parameter sets the default number of hours that the GUI Order Flag will be active. If you do not set this parameter, the default will be twenty-four hours.
- You can now comment on the flagged order by accessing the Action menu and clicking on the Flag Comment option or right-clicking on a flagged order and then, clicking on the Flag Comment option, as shown in the screenshot below.  
    
  ![](or-3-0-539-cprs-v32a-release-notes/010.png)  
    
  In the screenshot below, the user is adding a comment to the flagged Order.  
    
  ![](or-3-0-539-cprs-v32a-release-notes/011.png)
- The Order Details page now has details about flagging, including order flag history, as shown in the screenshot below.  
    
    
  ![](or-3-0-539-cprs-v32a-release-notes/012.png)
- Two new flagging notifications have been added: “Comment Added to Flagged Order: \<drug\>” and “Order flag expired for \<drug\> on \<date\>”, as shown in the highlighted examples in the screenshot below.  
    
  ![](or-3-0-539-cprs-v32a-release-notes/013.png)

### Change in Unflagging Capabilities (NSR 20071103)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS is now enabling sites to restrict which users can unflag an order.

- Two parameters have been added to the new GUI Order Flagging/Unflagging Setup menu:
  - OR UNFLAGGING RESTRICTIONS: Permits the CPRS GUI application to enable/disable unflagging restrictions on flagged orders. This parameter can be set at the Package, System, and Division levels. The OR\*3\*539 patch sets this flag to “Yes” at the package level.
  - OR UNFLAGGING MESSAGE: Allows the CPRS GUI application to set a customized message to send to users who cannot unflag an order because they do not have the proper security key. This parameter can be set at the Package, System, and Division levels. The OR\*3\*539 patch sets this message to “You are not allowed to un-flag this order based on your security keys and the order type”.
- The Order Unflagging Key Setup option has been added to the GUI Order Flagging/Unflagging Setup menu.
- To unflag an order, the user must meet one of the following requirements:
  - The user is assigned the ORES key
  - The user is assigned another security key that the site designates (the site can determine which keys can unflag orders)
  - The user is the person who flagged the order
  - The user is a flag order recipient
- If a user tries to unflag an order, but does not have the correct security key, the error message listed on the screenshot will display:  
    
  ![](or-3-0-539-cprs-v32a-release-notes/014.png)

### Update Surrogate Management Functionality within CPRS GUI (NSR 20171216)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Surrogate Management functionality within the CPRS GUI has been updated to match the functionality provided by the List Manager/Kernel settings.

Surrogate Management functionality is in a new location on the CPRS GUI. It has been removed from the Notifications tab and now has its own tab in in the Tools \| Options section.

The Surrogates tab allows you to add, edit and remove multiple surrogates for a provider on a single screen. It displays a list of all current and future surrogates and prevents you from scheduling more than one surrogate for the same date/time period.  
  
The screenshot displays the updates to the Surrogate functionality.

![](or-3-0-539-cprs-v32a-release-notes/015.png)

### Adverse Reaction Reporting File Modification (NSR 20120404)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS now requires you to enter at least one Sign/Symptom or enter a comment of at least four characters when documenting a historical allergy/adverse drug reaction. You now have the option to enter the severity level for an historical reaction.

When entering a historical allergy, you will now receive an error message if you do not select a symptom or have a comment of four or more characters, as shown in the screenshot below.

![](or-3-0-539-cprs-v32a-release-notes/016.png)

### Progress Notes Display Misleading (Addresses HITPS-397) (NSR 20070817)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS has been modified to display more complete progress notes lists. Currently on the Notes tab, under the View \| Custom View menu option, you can specify a maximum number of notes to display by inputting a value in the Max Number to Return field. CPRS has added two features on the tree view for the Progress Notes display: a “Show More” item and another display category called “Older signed notes with recent addenda”.

- Show More: If the user has more notes available than the maximum allowed, a “Show More” entry displays in the tree view. If the user double clicks “Show More”, CPRS downloads another set of notes as the initial maximum. If there are still more notes available, “Show More” appears again until there are no more notes to display.  
    
  In the screenshot below, if the select patient has 300 total notes and the Maximum Number of Notes is set to 30, when the Notes tab initially opens, 30 Notes will display in the tree view. A Show More item will display at the end of the tree view because there are more notes. If the user selects Show More, another 30 notes will be listed. If the user selects Show More again, another 30 notes and the Show More item will display. This process will continue until all the notes have been listed.  
    
  ![](or-3-0-539-cprs-v32a-release-notes/017.png)
- Older signed notes with recent addenda: Sometimes one or more notes outside the maximum range will have an addendum inside the range. These notes are added to the bottom of the list, under the date of the parent note.  
    
  In the example below, the last two notes have recent addenda but are well outside the range of the rest of the notes. This makes it appear that there are no notes between the last normal note (dated April 2019) and the older parent note with the recent addendum (dated March 2009).  
    
  ![](or-3-0-539-cprs-v32a-release-notes/018.png)  
    
  To prevent the appearance of a gap in notes, these older notes are now separated from the rest of the notes after the “Show More” entry, marked with the label, “Older signed notes with recent addenda”, as shown in the screenshot below:  
    
  ![](or-3-0-539-cprs-v32a-release-notes/019.png)  
    
  As shown above, both Show More and Older signed notes with recent addenda can be in the tree view.

### Identify Required Fields in TIU Note Templates and Notify of Missing Required Fields (NSR 20100706)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS can now identify unanswered required fields when a user is attempting to submit a note. A Required Fields Navigation Panel has been added to the TIU templates and unanswered required fields can be highlighted in a different color.  
  
You can choose the navigation panel position, select the highlight color of the unanswered required fields and disable highlighting by accessing Tools \| Options \| Notes and clicking on the Required Fields button, which will display the TIU Templates screen, as shown in the screenshot below:  
  
![](or-3-0-539-cprs-v32a-release-notes/020.png)  
The navigation bar on the TIU note template (highlighted in red in the screenshot below) provides a count of all unanswered required fields and provides navigation buttons to allow the user to jump directly to the required field. In addition to the \* used to identify required fields, all incomplete required fields are highlighted within the template, as shown in the screenshot below.

![](or-3-0-539-cprs-v32a-release-notes/021.png)  
  
Once the required field is filled in, the counter will reduce and the highlight for the field will be removed. You can change the highlight color and navigation bar position by right-clicking on the template.

### Create Separate Alert for Prosthetics (NSR 20110210)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS now enables a separate update alert for prosthetics requests that can be configured at the user or team level, separately from other consult alerts. It essentially moves all the "Add Comment" alert traffic for prosthetics consults into its own alert. It looks and functions the same as the current "Add Comment" (CONSULT/REQUEST UPDATED) alert.  
  
A new notification, PROSTHETICS CONSULT UPDATED, has been added to the CPRS v32a release. It gets generated whenever users add comments to or take the schedule action for a prosthetics consult in the CPRS GUI.

A screenshot of the Prosthetics alert is displayed below.  
  
![](or-3-0-539-cprs-v32a-release-notes/022.png)

### Confirm Provider Selected with Similar Names (NSR 20110606)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS has been modified to prompt the user for confirmation when providers with similar names are selected.

If the last name and the first two letters of the first name match another provider, CPRS will display the Similar Providers screen, which will prompt the user to select the right provider from a list of providers with similar names, as shown in the screenshot below. This functionality exists in thirty-seven areas of CPRS, but it always works the same way.  
  
![](or-3-0-539-cprs-v32a-release-notes/023.png)

### Limiting Additional Signers List (NSR 20120101)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS now provides the ability to limit the names displayed to the user in a CPRS-presented drop-down list. It uses data from File \#200 to display and allow selection of only active users who have CPRS COR tab access.

The new parameter, OR CPRS USER CLASS EXCLUDE, is being utilized to limit additional signers and has been created to store an ASU User Class. Sites can set this parameter to a new or existing ASU User Class. For example, if OR CPRS USER CLASS EXCLUDE is set to the ASU User Class, Clinical Dietician, the result is that all users in the Clinical Dietician ASU User Class will no longer get listed in the Additional Signers user selection box in CPRS.

### Nature of Order Default (NSR 20120601)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites can now select a default (Verbal\|Telephone\|Policy) for the nature of order or leave the default blank and require the user to select a method. This default selection can be done at the user or system level through the OR NATURE DEFAULT parameter. The nature of order options are highlighted in yellow in the screenshot.  
  
![](or-3-0-539-cprs-v32a-release-notes/024.png)

### VistA Evolution Anatomic Pathology Order Dialogs (NSR 20140511)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>NOTE</u>: The Anatomic Pathology Order Dialog functionality is not currently available but will be available soon. Sites will be notified when this feature becomes available.

Anatomic Pathology (AP) laboratory service now has a mechanism for clinicians to provide required patient-, procedure-, and specimen-specific information to facilitate specimen processing by pathologists. 

A new Anatomic Pathology Order Dialog is available with the following available order types:

- Bone Marrow
- Bronchial Biopsy
- Bronchial Cytology
- Dermatology
- Fine Needle Aspirate
- Gastrointestinal Endoscopy
- General Fluid
- Gynecology (Pap Smear)
- Renal Biopsy
- Tissue Exam
- Urine
- Urology, Bladder/Ureter
- Urology, Prostate

When opening the Anatomic Pathology order dialog, you must first select one of the available order types, such as seen below, for example Bone Marrow, Bronchial Biopsy.  
  
![](or-3-0-539-cprs-v32a-release-notes/025.png)  
  
Because each order type may require different information, different order dialog fields display when the user selects an order type.  

Common areas of Anatomic Pathology Order dialogs are listed below:  
  
![](or-3-0-539-cprs-v32a-release-notes/026.png)

1.  Order-specific fields such as Urgency and Collection Date/Time.
2.  List of Specimens for this order.
3.  The Current Specimen being viewed in box 4.
4.  Specimen-specific fields, such as the Specimen Description/Anatomic Site and Collection Sample.
5.  Button to delete the current specimen.
6.  Several Multiple tabs to enter free text fields, such as Clinical History.

Some dialogs have a “+” button at the top of the list of specimens. Other dialogs have a dropdown list to add an additional specimen. Each dialog has a different set of specimen-specific fields. Some dialogs have additional Clinical History fields.

When you click Accept Order, CPRS displays a preview dialog with all the order details displayed.  
  
![](or-3-0-539-cprs-v32a-release-notes/027.png)

### CPRS Modification Unified Action Profile (NSR 20130714)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>NOTE</u>: The United Action Profile is not currently available, but will be available soon. Sites will be notified when this feature becomes available.

The United Action Profile (UAP) allows providers to effectively review medications for discharge medication reconciliation. It is used to reconcile medication discrepancies. The UAP view assembles inpatient/outpatient meds in adjacent actional couplets, allowing providers to reconcile discrepancies at the time of a patient’s discharge from inpatient care.  
  
The UAP has been added to the CPRS GUI, as shown in the screenshot below, with the UAP title highlighted in red. The UAP displays a unified view of medication orders and is controlled by the OR UNIFIED ACTION PROFILE OFF site parameter.  
  
![](or-3-0-539-cprs-v32a-release-notes/028.png)  
  
You can access the UAP through the View menu:  
  
![](or-3-0-539-cprs-v32a-release-notes/029.png)

### First Dose Now (NSR 20130802) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There has been a change to First Dose NOW. Before the CPRS v32a release, if a dose was ordered NOW in addition to a scheduled dose, both orders would have the same priority. However, in CPRS v32a, the dose ordered NOW has a priority of STAT\* while the remaining doses are given the requested priority. The priority is stored in the ORDER URGENCY file and it defaults to ASAP. Otherwise, it is stored in the Kernel Site Parameters file under ORDER URGENCY ASAP ALTERNATIVE.

The confirmation dialog wording has changed for First Dose NOW. Here is the wording before the CPRS v32a release:  
  
![](or-3-0-539-cprs-v32a-release-notes/030.png)

And here is the wording for CPRS v32a:  
  
![](or-3-0-539-cprs-v32a-release-notes/031.png)

Before the CPRS v32a release, the signed First Dose order looked like this:  
  
![](or-3-0-539-cprs-v32a-release-notes/032.png)

In CPRS v32a, the signed First Dose order looks like this:  
  
![](or-3-0-539-cprs-v32a-release-notes/033.png)

### Surrogate Settings (NSR 20071216) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This NSR enhances the surrogate setting screen in the CPRS GUI. A provider can now independently set up multiple/sequential surrogates in the CPRS GUI like they can in the VistA roll and scroll. In the image below, multiple surrogates have been added. This change fixes patient safety item [HITPS 1131](#hitps_1131).

![](or-3-0-539-cprs-v32a-release-notes/034.png)

### Similar Provider Lookup Improvements (NSR 20140211) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This NSR addresses the issue of incorrectly selected providers by adding a Similar Name pop-up when selecting a provider with another/multiple similar names. This pop-up displays when the user enters orders and identifies additional signers/cosigners on notes. This change fixes patient safety item [HITPS-1711](#hitps_1711).

![](or-3-0-539-cprs-v32a-release-notes/035.png)

## Patient Safety Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HITPS-294/307: Progress Notes not ALL being displayed.  
  Resolution: This issue was corrected in NSR 20070817 – Progress Notes Display Misleading.
- HITPS-397: Progress Notes Misleading.  
  Resolution: This issue was corrected in NSR 20070817 – Progress Notes Display Misleading.
- HITPS 1963: Unauthorized provider who attempted to order Clozapine bypassed alert and assumed the medication had been ordered  
  Resolution: Enhanced the messaging. Clarified the message that the user is not authorized to order Clozapine.
- HITPS 1519: VBEC BLOOD BANK order dialog changes.  
  Resolution: The CPRS GUI was modified to clearly specify that the date/time is applied to all components. Dialog form was updated to work with font sizes 8 through 14.
- HITPS 799: Display of Non-VA meds confusing to provider when renewing, reviewing or discontinuing meds.  
  Resolution: On the Orders tab, a “Documentation” title was added to Non-VA Meds text:  
  ![](or-3-0-539-cprs-v32a-release-notes/036.png)  
    
  On the Meds tab, a “Documentation” title was added to the Non-VA Medications section header:  
  ![](or-3-0-539-cprs-v32a-release-notes/037.png)  
    
  On the Meds tab, “Document Non-VA Meds” was added to the Action and right-click menus:  
  ![](or-3-0-539-cprs-v32a-release-notes/038.png)  
    
  ![](or-3-0-539-cprs-v32a-release-notes/039.png)
- HITPS-7541: Medication order details with incorrect dispensed drug.  
  Resolution: Corrected a problem introduced by Nurse Verification changes done in OR\*3\*413. User can now see the Medication Order Details with the correct dispensed drug.
- HITPS-7551: Inpatient order was for valproic acid, dispense drug came through as trazodone.  
  Resolution: Same as the resolution for HITPS-7541.
- HITPS 1842: Always show flagged orders on active and current views.  
  Resolution: Fixed in NSR 20110719 – Order Flag Recommendations
- <span id="hitps_196" class="anchor"></span>HITPS 196: Allergy ingredient order checks not triggering.  
  Resolution: Fixed in [NSR 20060710](#real-time-notification-of-potentially-missed-order-checks-nsr-20060710) – Potentially Missed Order Checks for Ingredients
- <span id="hitps_1131" class="anchor"></span>HITPS 1131: Limitation in GUI CPRS setting multiple surrogates.  
  Resolution: Fixed in [NSR 20071216](#_Surrogate_Settings_(NSR) – Surrogate Settings
- <span id="hitps_1711" class="anchor"></span>HITPS 1711: Providers receive incorrect notifications if there is more than one with the same last name.  
  Resolution: Fixed in [NSR 20140211](#similar-provider-lookup-improvements-nsr-20140211) – Similar Provider Lookup Improvements

## Defect Tracking System Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  INC13521395 (<span id="new_7499" class="anchor"></span>HITPS-7499) - CPRS RTC Order Rejected Due to Today in the Date field  
    Problem: When creating an RTC order with a date of TODAY or t (lowercase T), the order is rejected.  
    Resolution: The RTC form now converts dates of TODAY or t to T (uppercase t).
2.  INC15380193 - Prosthetics consults requiring Clinically Indicated Date

Problem: When processing a prosthetics consult quick order that is not an auto-accept quick order, the CID field is enabled and mandatory. The CID should not be enabled when placing prosthetics consult orders as that date is not used in downstream processing of prosthetics consults.

Resolution: The CID field has been restored to being disabled when processing any/all

types of prosthetics consult orders.

3.  INC000000069337 FAR-1100-41820 PPD Reminder Dialog does not send over a 0 reading VISTAOR-22049 \<SYNTAX\>PROCESS+10^ORB3FUP1 Error When Viewing Notification From the All Current Notifications Dialog

Problem: Dialog progress note text is not displaying PPD skin test reading in mm when completed. When a user who is not the recipient of the “Pregnant. Potentially harmful medication. Counsel risk/benefit.” Notification attempts to view that notification from the All Current Notifications dialog, this error is generated.

Resolution: The code called by the View button in the All Current Notifications dialog was modified to no longer generate the error.

4.  INC15619999 - IOW - CPRS v31MA - couple of users that get an CRC: E24FCC35 error when using copy/pasting in to Reminder Dialog  
    INC15665178 - CPRS v31MA: Copying and pasting data in the Reminder Dialog for the KC-PRIOR APPROVAL/NONFORMULARY CONSULT NOTE  
    INC16364483 - CPRS v31MA- CPRS issues: Pharmacy Special Medication Request Reminder Dialog - Error CRC: EEDFAE4  
    ICN12220159 – Get kicked out of CPRS, After recent changes CPRS, several times (but not all) when I try to copy and paste  
    Problem: In certain circumstances, when a user is attempting to copy text into the CPRS GUI, the user will receive an access violation error.  
    Resolution: This issue was caused by a defect in CPRS's memory cleanup. The cleanup code has been corrected to prevent the error.
5.  INC13146720 CPRS Issue with Nurse Verified Orders  
    INC13724258 Medication Order Details with Incorrect Dispensed Drug  
    INC13848885 CPRS Issue with Nurse Verified Orders – When a nurse goes to verify an order in CPRS, sometime the wrong dispense drug  
    INC14130255 Order Detail in CPRS Showing Different Dispense Drug from Ordered Drug

Problem: When a nurse goes to verify an order in CPRS, the wrong dispense drug was showing up. If two orders are selected in the verification process followed by the order details of the first order, the dispense drug that showed up was for the second order. This issue was introduced by OR\*3\*413.

Resolution: In routine ORCACT0, the global ^TMP("PS",\$J) gets created but was not cleaned up after use. A kill statement was added to clean up the global.

6.  <span id="write_orders" class="anchor"></span>Write Orders Menu doesn’t always display (documentation) for Non-Va meds

Problem: The menu display wasn't properly defaulting the text to the order dialog item display text if one existed and the menu did not have a value already.

Resolution: Corrected the display issue.

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  VISTAOR-26366 Fix Patient Selection on Personal Lists Screen  
    Description: If you go to Tools \| Options \| Lists/Teams \| Personal Lists, you will see a dialog where you can select different patients. In CPRS v31MA, when you enter the last name initial and the last four digits of the SSN to pick a patient (in the same way that you do it on the Patient Selection screen), the system selects the desired patient. But in CPRS v32a, the system doesn’t do anything.  
    Workaround: In the Personal Lists window, click on the Patient radio button. Enter the last name initial and the last four SSN digits and then, click on the Tab key. This issue was found during CPRS v32a production testing in Philadelphia. It will be resolved in CPRS v32b.

# New Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32a has new parameters from the CPRS (parameters that start with OR) package.

- OR CPRS USER CLASS EXCLUDE
- OR FLAG ORDER EXPIRE DEFAULT
- OR NATURE DEFAULT
- OR SIMILAR NAMES ENABLED
- OR UNFLAGGING MESSAGE
- OR UNFLAGGING RESTRICTIONS
- ORQQXQ SURROGATE DEFAULTS

# Modified Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- ORB ARCHIVE PERIOD
- ORB DELETE MECHANISM
- ORB FORWARD BACKUP REVIEWER
- ORB FORWARD SUPERVISOR
- ORB FORWARD SURROGATES
- ORB PROCESSING FLAG
- ORB PROVIDER RECIPIENTS
- ORB URGENCY
- ORQQCN CTB PATH
- ORQQCN DST CONS DECISION
- ORQQCN DST CONS SAVE
- ORQQCN DST PATH
- ORQQCN DST PROD URL
- ORQQCN DST TEST URL
- ORQQCN DST/CTB FEATURE SWITCH

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

- *Adverse Reaction Tracking User Manual*
- *CPRS User Guide: GUI Version*
- *CPRS Technical Manual: GUI Version*
- *CPRS GUI v32a Release Notes* (this document)
- *CPRS GUI v32a Deployment, Installation, Back Out and Roll Back Guide*
- *Consult/Request Tracking User Manual*
- *Consult/Request Tracking Technical Manual*
- *Mental Health and Mental Health Assistant Version 3 Technical Manual/Security Guide*
- Online Help System