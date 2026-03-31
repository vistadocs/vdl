---
title: OR*3*190 Release Notes CPRS GUI 24
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: CPRS GUI 24
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*190
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: "- GMTS\2.7\65—requires: - PSO\7.0\132 - PSJ\5.0\107 - PSS\1.0\69 - OR\3.0\127 - OR\3.0\163 - OR\3.0\164 - OR\3.0\176 - OR\3.0\178 - OR\3.0\183 - OR\3.0\186 - OR\3.0\187 - OR\3.0\196 - TIU\1.0\183"
audience: 
keywords: 
  - cprs
  - order
  - orders
  - nois
  - patient
  - dialog
  - medication
  - button
  - corrected
  - developers
page_count: 0
word_count: 5632
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_190rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_190rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

RELEASE NOTESFORCPRS GUI VERSION 24PATCH# OR\*3.0\*190

INSTALLATION REQUIREMENTS

Before you can install OR\*3.0\*190, you must install the following:

- GMTS\*2.7\*65—requires:
  - PSO\*7.0\*132
- PSJ\*5.0\*107
- PSS\*1.0\*69
- OR\*3.0\*127
- OR\*3.0\*163
- OR\*3.0\*164
- OR\*3.0\*176
- OR\*3.0\*178
- OR\*3.0\*183
- OR\*3.0\*186
- OR\*3.0\*187
- OR\*3.0\*196
- TIU\*1.0\*183

> **NOTE:** CPRS GUI version 24 REQUIRES Internet Explorer 4.0 (IE4) or later. However, IE 5.5 or later with 128-bit encryption is required for PKI functionality.

Possible Class III Software Conflict

Pharmacy developers modified the Outpatient Pharmacy V7.0 application programming interface (API) PSOHCSUM to also return the list of Non-VA Meds for the patient. Other applications may use this API to extract data from the pharmacy files for use with the Health Summary. Some sites identified at least one Class III routine (OMED^AOVTIU) that no longer worked once the new version of the PSOHCSUM API was installed.

To prevent this problem, you must identify any Class III software used by your site that currently uses this API and make the necessary code modifications to handle the Non-VA Meds list returned.

Below you will find a complete description of the fields returned by this API and an example showing what the API returns.

PSOHCSUM API Fields:

^TMP("PSOO",\$J,"NVA",N,0)= 1p. ORDERABLE ITEM\_" "\_DOSE FORM

2p. STATUS ("Discontinued" OR "Active")

3p. START DATE (FM FORMAT - Can be imprecise)

4p. CPRS ORDER \# (Pointer to file \#100)

5p. DATE/TIME DOCUMENTED (FM FORMAT)

6p. DOCUMENTED BY (Pointer to file \#200)\_";"\_NAME

7p. DISCONTINUED DATE/TIME (FM FORMAT)

^TMP("PSOO",\$J,"NVA",N,1,0)= 1p. DOSAGE

2p. MED ROUTE

3p. SCHEDULE

4p. DRUG (Pointer to file \#50\_";"\_DRUG NAME)

5p. CLINIC (Pointer to file \#44\_";"\_CLINIC)

^TMP("PSOO",\$J,"NVA",N,"DSC",NN,0)= 1p. STATEMENT/EXPLANATION/COMMENTS

N & NN are just sequential numbers.

Example of what the PSOHCSUM API returns:

^TMP("PSOO",541123963,"NVA",1,0) = THIOGUANINE TAB^Active^^12870^3040407.125112^10000000013;CPRSPATIENT,TWO^

^TMP("PSOO",541123963,"NVA",1,1,0) = 40MG^MOUTH^3XW^35;THIOGUANINE 40MG TABS^161;LAB

^TMP("PSOO",541123963,"NVA",1,"DSC",1,0) = PATIENT DECIDED TO BUY FROM WALGRENS BECAUSE FO COPAY.

^TMP("PSOO",541123963,"NVA",2,0) = BACITRACIN OINT,TOP^Active^^12871^3040407.125117^10000000013;UTAH,JIM^

^TMP("PSOO",541123963,"NVA",2,1,0) = LIBERALLY^AFFECTED AREA^^2827;NEOSPORIN 1/32 OZ PKTS OINT^161;LAB

Known Interface Issues and Workarounds

CPRS GUI v.24 has two minor issues that users can quickly correct:

- Meds Tab Display-When a user logs in to CPRS GUI v.24 for the first time and changes the size of the panes (Inpatient Meds, Non-VA Meds, and Outpatient Meds) on the Meds tab, CPRS may not save the resizing correctly. To fix this problem, the user should simply log out of CPRS and log back in. The user can then change the size of the panes on the Meds tab and CPRS will save them correctly for that user.
- Display of Reminder Dialogs Using 8 Point Font-CPRS has a long-standing problem with some reminder dialogs displaying extra text or checkboxes. If a user sees this problem, the user should resize the dialog and the extra items will be removed.

NEW FUNCTIONALITY

Allergy / Adverse Reaction Tracking

- CPRS no longer allows users to enter free-text causative agents. When users attempt to enter a causative agent that is not in the GMR ALLERGIES file, CPRS instructs them to try alternate spellings or names, or to contact their allergy coordinator for assistance. If patch GMRA\*4.0\*17 is installed, users can automatically (via an option) send to their local allergy mail group a bulletin requesting that the new causative agent be added to the GMR ALLERGIES file for future selection.

Herbal / OTC / Non-VA Medications

E3Rs: 1495314954

> 1588616979  
  
Documentation of herbal, Over-the-Counter (OTC) and non-VA medications (medications dispensed outside the VA system) can now be accomplished through a special Pharmacy ordering dialog. This group of herbal, OTC, and medications dispensed outside the VA are collectively called Non-VA Meds. Users can document Non-VA Meds by selecting the Orders tab, selecting Meds, Non-VA from the Write Order list, and entering a new order for the Non-VA Med. Non-VA Meds do not require an electronic signature. Once documented, Non-VA Meds appear under a separate heading on the Orders and Meds tabs. Order checking occurs for Non-VA Meds.

> NOTE: For this version of the CPRS GUI, quick orders for Non-VA Meds are not supported.

Developers added a new parameter OR OREMAS NON-VA MED ORDERS. This parameter determines if clerks (i.e., users holding the OREMAS key) are allowed to act on non-VA med orders. If sites set this parameter to YES, clerks can enter new non-VA Med orders or DC non-VA med orders and send them to Pharmacy for reports and order checks. If sites set this parameter to UNRELEASED ONLY, clerks are restricted to only entering unreleased orders. If sites set this parameter to NO, CPRS prohibits clerks from handling non-VA med orders.

> NOTE: Non-VA Meds support only a NONE value in the SIGNATURE REQUIRED field of the PSH OERR dialog.

Clinical Coordinators or IRM personnel can set the OR OREMAS NON-VA MED ORDERS Parameter through the CLINICAL COORDINATORS MISCELLANEOUS PARAMETERS option as shown below:

Select CPRS Manager Menu Option: PE CPRS Configuration (Clin Coord)

…

MI Miscellaneous Parameters

…

Select CPRS Configuration (Clin Coord) Option: mi Miscellaneous Parameters

Miscellaneous OE/RR Definition for System:

-----------------------------------------------------------------------

Active Orders Context Hours 0

Allow Clerks to act on Med Orders YES

Allow Clerks to act on Non-VA Med Orders

Review / Sign Changes

Combat Veteran – Developers added a co-pay column for marking a medication as related to Combat Veteran service. This column will not be active until supporting patches have been completed and installed on your system.

Encounters

Combat Veteran – Developers added a Combat Veteran Related service connection category to the encounter form. This will not be active until supporting patches have been completed and installed on your system.

Reminders

Combat Veteran – On the Visit Information Dialog, developers added a Combat Veteran Related service connection category. This will not be active until supporting patches have been completed and installed on your system.

Orders

Add Recently Expired Orders to Order tab View Menu (PSI-03-014, E3R 17567, NOIS: HAM-1202-22074) – Developers added to the Order tab View menu the option to view recently expired orders. The modification extends to the Expiring Orders display so that if no expiring orders are found, this option displays recently expired orders. Sites can set the number of hours in the past to search for expired orders through the ORWOR EXPIRED ORDERS parameter. The default/CPRS package-level value is 72 hours.

PATIENT SAFETY ISSUES

To make it easier to see what patient safety issues were resolved by this CPRS GUI version, they are grouped here. These same items can be found in the New Functionality or Bug Fix sections of these release notes.

ORDERS

- PSI -03-014 Add Recently Expired Orders to Order tab View Menu (E3R 17567, NOIS: HAM-1202-22074) – Developers added the option to view recently expired orders to the Order tab View menu. The modification extends to the Expiring Orders display so that if no expiring orders are found, this option displays recently expired orders. Sites can set the number of hours in the past to search for expired orders through the ORWOR EXPIRED ORDERS parameter. The default/CPRS package-level value is 72 hours.
- PSI-03-038 Change Location and Display of Information Box on the Medication Order Dialog (NOIS BHS-0803-11189) – In medication order dialogs, when the user tried to click on information box to close it, the dosage could be accidentally changed. In this version, the initial position of the information box will be little lower than top of the comment box and dosage change will make the information box disappear.
- PSI-03-042 Added Order Checks on Renewals (NOIS CLL-0902-40134, ANC-0803-51943, CPH-0601-41699) - When doing order renewal in CPRS, there was no order checking taking place. This has been fixed.
- Patient Safety Issues PSI-03-052 Removal of Action Alerts by Individual  
  >   
  > NOIS MAD-0803-41908SHE-0803-51672DAY-0903-40968HIN-1003-42160 \\E3R 18434Changes to Remove Button for Deleting Alerts - Developers moved the Remove button on the Alert display to the far right making it harder for users to accidentally select “Remove”. Developers modified the delete action when Remove button is clicked to only delete the selected alert(s) for the current user/recipient. (Previously, using the Remove button deleted the alert for all recipients of the alert if the Notification Deletion parameter indicated the alert should be deleted for All Recipients.) In addition, developers added the ORB REMOVE parameter so sites can flag what CPRS Notifications/alerts can be deleted without processing via the Remove button. If an alert does not have the parameter set to ‘yes’, the alert cannot be deleted via the Remove button.
-   
  PSI-04-003 Disallowing Default Medication Selection for Medication Ordering (NOIS MIN-0104-41341, E3R 18710, PSI-04-003) - When a user types some text in the Medications selection box, CPRS scrolls the list to the first matching entry, but no entry will be automatically selected. The user must either click on the desired entry in the list or tab to the list, use the down arrow to highlight the entry, and press \<Enter\> to select the desired entry. Auto-selecting if there is only one match is a much more complicated solution, and is not included in this fix. For now, the user must make a conscious selection. This fix was added for non-VA medications as well.
- PSI-04-008 Outpatient Medication Order Quantity Update Error (NOIS WIM-0204-21575, PSI-04-008) - Previously, during the ordering process for an Outpatient medication, if the provider selected a schedule and then changed it to a ONE-TIME schedule, the quantity did not recalculate correctly. Developers corrected this so that if the provider selects a one-time schedule or non-standard schedule, the quantity is reset to zero, and the provider must enter a valid quantity before accepting the order. This fix was added for non-VA medications also.

BUG FIXES

Alerts

- Patient Safety Issues PSI-03-052 Removal of Action Alerts by Individual  
    
  NOIS MAD-0803-41908SHE-0803-51672DAY-0903-40968HIN-1003-42160 \\E3R 18434Changes to Remove Button for Deleting Alerts - Developers moved the Remove button on the Alert display to the far right making it harder for users to accidentally select “Remove”. Developers modified the delete action when Remove button is clicked to only delete the selected alert(s) for the current user/recipient. (Previously, using the Remove button deleted the alert for all recipients of the alert if the Notification Deletion parameter indicated the alert should be deleted for All Recipients.) In addition, developers added the ORB REMOVE parameter so sites can flag what CPRS Notifications/alerts can be deleted without processing via the Remove button. Non-CPRS-OR alerts cannot be deleted via the Remove button. If a CPRS-OR alert does not have the parameter set to ‘yes’, the alert cannot be deleted via the Remove button.
- NOIS FAR-0903-41288MAC-0803-61076E3R 18405Saving User Alert Sorting - Developers added a way to store a user’s alert display sorting in the ORB SORT METHOD parameter. Now, when a user clicks on an alert column to change the sorting, it is stored in the parameter for use next time he/she looks at alerts in CPRS GUI. To support this change, developers modified the ORB SORT METHOD values. The “T:type” sort method has been changed to “M:message”. New values include: “I:info”, “L:location”, “D:date/time”, “F:forwarded by/when”. Pre-existing “T:type” values are converted to “M:message” during patch installation. Other existing site values are carried over.
- Alerts Not Showing Patient SSN (NOIS: HUN-0903-22468) – Previously, if a patient had a short name, Kernel formatted the information by inserting spaces between the name and the social security number (SSN), which caused formatting error when processing the alert for display in the CPRS GUI. The last four SSN+1 for patients with short names should now be displayed.
-   
  Added the Ability to Sort Notifications Using the Keyboard - Developers made a change to enable users who do not use the mouse to sort Notifications in ascending order (alphabetical order or most recent Date/Time) using the keyboard only. A limitation exists in the programming environment that does not allow the user to user the same key combination to then reverse the sort. Making this change would not be trivial and will not be addressed in this version of the CPRS GUI. When users sort using the Ctrl + \<key\> combination, CPRS will recognize either upper or lower case letters (this feature is not case-sensitive). Users can sort Notifications using the following Ctrl + \<key\> combinations:

Key Combination Column Sorted

Ctrl + I Info

Ctrl + P Patient

Ctrl + L Location

Ctrl + U Urgency

Ctrl + R Patient

Ctrl + M Message

Ctrl + F Forwarded By/When

- Prevent Processing and Deletion of Local, Follow-up Action Alerts in CPRS GUI (MIN-0903-42340, REN-1003-61436) – Previously, local alerts were treated as informational alerts and were deleted before follow up actions were taken (in List Manager). Local alerts are no longer treated as informational alerts. With this patch, users trying to process a local, follow-up action alert through the Process button will receive the warning message “Alert cannot be processed by CPRS GUI”.
- Pressing Enter to Process Notifications - Developers added a change that enables users to simply select one or more Notifications, press \<Enter\> and the Notifications will begin processing.
- NOIS PSI-03-014HAM-1202-22074HIN-0702-42148CHA-0602-31214MWV-0502-21845Showing Recently Expired Medications if No Expiring Medications Found - During the follow-up action for a Medication Expiring alert, if no expiring medications are found, CPRS displays recently expired medications.
- Patient Location Display (NOIS: HVH-0903-11533) - Patient locations were not displayed in the Location column in all possible instances. Now for all inpatient OR alerts, patient location is displayed in the Location column whenever known. For outpatients, TIU and other alerts, the patient location will be blank. (Patient location cannot be determined for these alerts.)
- Corrected Problem with Unrecognized Characters in a Lab Result (NOIS MIW-0903-40510) – When a site's lab results included "-----", it caused undefined variable errors. Developers fixed the problem.

Review / Sign Changes Screen

Corrected Display when Changing Patients via Notifications (NOIS LEB-1003-20996, TAM-0903-30555, LEX-1003-40596) – When processing Notifications, CPRS opens different patients’ records that require a follow up action. Sometimes when changing patients via a notification, CPRS did not properly clear the items on the Review/Sign Changes screen as they were when changing patients via a new patient selection. This has been corrected.

Patient Record Flags

- Addition of Patient Record Flag Pop-Up Box (NOIS MAC-0903-61494, PHO-0903-60782) - In the Patient Selection screen when the user double-clicked to select a patient, a patient record flag box displayed on the Patient Selection screen, but before the user could read it, CPRS went directly to the default tab. This has been fixed. There will be a popup box to display active patient flags after the patient is selected.
- Sensitive Patient Warning Placed before Patient Record Flag Pop-Up Appears (NOIS HIN-1003-40302) - If a user selects a sensitive patient, the sensitive patient warning box displays and the user must click on this box before the user can proceed.

SURGERY TAB

All remote procedure calls related to the display of the Surgery case's OpTop have now been removed.

Problems Tab

Recent Code Set Versioning changes precluded users from changing an existing problem to a free-text or 799.9 entry, but a user could enter a new free-text problem. This discrepancy has been corrected so that changing an existing problem to free text or 799.9 is allowed.

Orders

- Added Order Checks on Renewals (NOIS CLL-0902-40134, ANC-0803-51943, CPH-0601-41699) - When doing order renewal in CPRS, there was no order checking taking place. This has been fixed.
- Corrected Med Dialog Tab Sequence (NOIS SUX-0103-42343) - The tab key sequence in medication order dialog is now the right sequence.
- Corrected Display on Verify Dialog (NOIS SUX-1003-40755) - At a screen resolution of 600x800 or lower, users could not see the OK and Cancel buttons of the Associated Complex Order Verify Window. This has been fixed.
- Corrected Renewal of Med with Give Additional Dose Now (NOIS ASH-0803-30045) - For a regular medication order with Give Additional Dose Now selected, CPRS did not allow the provider to renew the order. This has been fixed.
- Copying of Orders with Inactive Drugs (NOIS MON-0603-51257) - CPRS was allowing users to copy existing medication orders with inactive drugs. This problem has been fixed. Now, if a user attempts to copy an order with an inactive drug, CPRS displays the warning message “The drug had been inactivated” and the copy action will be canceled.
- Quick Order with PRN (NOIS ERI-0803-21714) – When a quick order created with a schedule containing PRN (i.e., Q8H PRN) was loaded, CPRS had the PRN box checked correctly but the EXPECTED FIRST DOSE administrative time still showed up. This has been fixed.
- Procedure Quick Order Containing No Service (NOIS UNY-0903-10610) - If a procedure quick order contains no service and more than one service is selectable for that procedure, the service combo box should NOT be disabled. This has been fixed.
- New Options Have Been Added to the Clinical Coordinator’s GUI Parameters Menu – The options GUI Expired Orders Search Hours and GUI Remove Button Enabled have been added to the Clinical Coordinator’s GUI Parameters menu as shown below:

Select CPRS Manager Menu Option: PE CPRS Configuration (Clin Coord)

GP GUI Parameters ...

Select CPRS Configuration (Clin Coord) Option: GP GUI Parameters

CS GUI Cover Sheet Display Parameters ...

HS GUI Health Summary Types

TM GUI Tool Menu Items

MP GUI Parameters - Miscellaneous

UC GUI Clear Size & Position Settings for User

RE GUI Report Parameters ...

NV GUI Non-VA Med Statements/Reasons

EX GUI Expired Orders Search Hours

RM GUI Remove Button Enabled

- The GUI Expired Orders Search Hours parameter enables sites to determine how many hours back in time to search for expired orders. CPRS displays these orders in the “Recently Expired Orders” view on the Orders tab.
- The GUI Remove Button Enabled parameter enables sites to select CPRS-OR notifications/alerts that can be deleted via the Remove button. In effect, this option allows sites to determine which CPRS-OR alerts can be deleted without processing. Non-CPRS-OR alerts cannot be deleted via the Remove button.
-   
  NOIS UNY-0603-11980MWV-0302-22601CLE-1102-40793Inpatient to Outpatient Medication Name Problem - When users transferred an inpatient medication order to an outpatient medication, if the medication’s dispense drug name differed for inpatient and outpatient, the drug name was pulled into dosage in the transferred order. This has been fixed.
- Radiology Quick Order Losing Modifier (NOIS BIL-0903-30864) - For personal radiology quick orders, the predefined modifier was not held during the order placing. This has been fixed.
- Incorrect Dialog Displaying to Verify Multiple-Day Lab Orders (NOIS BOI-1103-50612) - A user verifying multiple-day lab orders could get a pop-up “Associated Complex Orders” window with the text of “You have requested to verify a medication order which was entered as part of a complex order…”. This has been fixed.
- List Out of Bounds Error for Meds Requiring a DEA Number (NOIS SDC-1203-60379) - When placing an order set with a medication that requires a DEA number, if user did not have \#DEA, a “list index out of bounds” error would occur. This has been fixed.
- Problem with Non-Formulary Medication Orders (NOIS CAH-0303-30751) - Providers using medication order entry are having problems with ordering Non-Formulary medications. Occasionally, when a NF orderable item is entered in CPRS, once the \<enter\> is given or click on OK the screen grays out and the user is unable to proceed. It’s been fixed.
- Disallowing Default Medication Selection for Medication Ordering (NOIS MIN-0104-41341, E3R 18710, PSI-04-003) - When a user types some text in the Medications selection box, CPRS scrolls the list to the first matching entry, but no entry will be automatically selected. The user must either click on the desired entry in the list or tab to the list, use the down arrow to highlight the entry, and press \<Enter\> to select the desired entry. Auto-selecting if there is only one match is a much more complicated solution, and is not included in this fix. For now, the user must make a conscious selection. This fix was added for non-VA medications also.
- Outpatient Medication Order Quantity Update Error (NOIS WIM-0204-21575, PSI-04-008) - Previously, during the ordering process for an Outpatient medication, if the provider selected a schedule and then changed it to a ONE-TIME schedule, the quantity did not recalculate correctly. Developers corrected this so that if the provider selects a one-time schedule or non-standard schedule, the quantity is reset to zero, and the provider must enter a valid quantity before accepting the order.
-   
  Resizing Problem Making Procedure Reason for Request Box Not Display (NOIS ALB-0204-50425, MAC-0104-61043) – In procedure ordering, the "Reason for Request" entry box was not resizing properly, causing it sometimes not to be visible. This has been corrected.
- Quick Order for Wrong Patient Type (NOIS CHA-1003-30379) - For an outpatient, the user selected the Outpatient Medication Order dialog and in the list of quick orders an inpatient quick order was displayed with the outpatient quick orders. This has been fixed so that CPRS displays only outpatient quick orders if the patient is an outpatient.
- CPRS Order File Not Updating Correctly (NOIS CMS-0503-31313) – If a user copied a prescription in Outpatient Pharmacy (using the hidden option of copy in Patient Prescription Processing \[PSO LMBACKDOOR ORDERS\]), accepted the order, and then edited the provider field of the RX, the prescription file was updated but the order file in CPRS was not updated with correct provider. This has been corrected.
- CPRS Order Dialog Allowed the Selection of Medications for Those Ordering Supplies (NOIS HIN-0800-42602) - When placing “PSO SUPPLY” orders, the outpatient medication order dialog displayed, and the user could select regular medications. This has been corrected. If a supply quick order is loaded in the dialog, the user would not be allowed to select medications.
- Release Orders Form Display Problem (NOIS SFC-0204-60917) - On the “Release Orders” form, the last event was cut off and user could not see it. This has been corrected.
- Medication Selection Problem (NOIS PUG-0703-50915) - When entering a medication from the meds tab or the orders tab in GUI and after the user has entered an orderable item name by typing a few letters, a pick list displayed. If the user wanted the first item displayed in the list that is not a personal quick order, but rather then clicking exactly on the item, the user inadvertently clicks just above the selection (between the orderable item name and the horizontal bar that separates the pick list from a users personal quick orders), the medication dialog box opens with the orderable item field populated with the name just above the item the user wanted. Because the selection is hidden, the user may not notice the mistake and that could lead to a medication error. The root cause is the malfunction of the Borland Delphi component “TlistView”. To finally correct the problem, Borland must distribute an updated TlistView component. Right now, to help reduce possible medication errors, when the mouse hovers over a medication or clicks on a medication, the medication will be highlighted.
- Buttons Display Corrected on Release Orders to Service Dialog (Font Issue) - When a user selected 10pt or higher fonts as their preference, the OK and Cancel buttons did not display on the "Release orders to service" dialog box. This has been corrected and the buttons should reposition themselves correctly at all fonts/window sizes.
- Procedure Order Dialog Navigation Corrected - Previously, if the user in the Inpatient/Outpatient was using the arrow keys for navigation, the user could arrow from one radio button to another and then off that control. The arrow key should move the focus from one radio button to another within the group box, but moving off the control should require using the tab key. Developers therefore put Inpatient/Outpatient radio buttons on the New Procedure dialog into a group box to prevent the user from being able to arrow off of the group. The user must now tab to leave the group box.
- ICD 9 Codes and Treatment Factors in Detailed Display - Developers added ICD 9 codes and treatment factors (SC/EI) to the detailed displays that have these items defined.
- Quick Order Quantity and Supply Changing Corrected - When opening a quick order with free-text dosage, the pre-defined values in the supply and quantity fields changed. This has been corrected.

Event Delayed Orders

- EDO Manual Release Fix (NOIS (NOL-0903-70631 and TAM-0803-31743) - For an outpatient, the manual-release type of event-delayed outpatient order could not be manually released. This is now fixed.
- Fixed Display of Long List of EDO – (NOIS TAM-0803-30773, LOM-1003-60667) - For a long delayed event list, in the event selection box, users could not scroll down to the bottom event and the bottom event is not viewable to user. It’s fixed.
- Inaccurate Display Text for Delayed Events (NOIS CPH-1202-41910) - CPRS GUI did not show the Display Text for delayed events exactly as the text was entered. This has been corrected.
- Change Location and Display of Information Box on the Medication Order Dialog (PSI-03-038, NOIS BHS-0803-11189) – In medication order dialogs, when the user tried to click on information box to close it, the dosage could be accidentally changed. In this version, the initial position of the information box will be little lower than top of the comment box and dosage change will make the information box disappear.

Notes Tab

- Previously, CPRS GUI 23 (v23.9 and above) disabled the "New Note" button as soon as it was clicked to prevent a variety of errors, including signed blank notes, resulting from multiple clicks. This version contains additional logic to prevent this from happening via other combinations of clicks (menu, then button, EDIT then NEW, ADDENDUM then NEW, etc). It is also no longer possible to drag a note in the treeview at the same time that a note is being edited. Previously, any of the above actions could have lead to a situation where two "New Note in Progress" nodes could appear in the treeview, and that could in turn lead to one of those notes being signed while containing no text. It should no longer be possible under any of these circumstances to reach a situation where two notes are both in progress in the treeview at the same time.

Notes/Discharge Summaries

When clicking the CHANGE button while editing an existing document, it was possible for the AUTHOR or COSIGNER/ATTENDING combo box to appear without the currently defined entry. This has been corrected.

Templates

- Template Dialog Performance Degradation - Modified code that from an older version of CPRS that caused degradation in template dialog performance.
- Reloading Boilerplate Text - Reloading boilerplate text was working correctly on the Notes tab, but not on the other three TIU-related tabs: Consults, Surgery, and Discharge Summary. This was happening after selecting the "Change" button and reselecting the same title, then attempting to reload boilerplate text. The message "There is no boilerplate assigned to this title" was displayed to the user. This has been corrected so that all four tabs now work correctly in that scenario.
- Template Dialog Window Changed Back to Height from Previous CPRS Version (ASH-0803-30980) – Developers changed the template dialog window height back to what it was in version 20.

Encounters

- Adding Encounters from the Problem List (NOIS: PUG-0702-51422) - When a diagnosis was selected via the Problem List section, the "Add to Problem List" checkbox remained enabled for that item. In this version, the checkbox will only be enabled if any item in the currently highlighted list was NOT selected via the Problem List. Clicking the checkbox will now only display "Add" next to those items that were selected by other means.
- Encounter Button Problem Resolved (NOIS PAL-1003-61241, PUG-0503-50095) - On the Notes, Consults, D/C Summ, and Surgery tabs, users were receiving access violations when clicking the Encounter button more than once. Developers corrected the problem by disabling the button after it is clicked once. The button is then re-enabled when the encounter form is closed.
-   
  Encounter Location Problem Corrected - Previously, on the Provider & Location For Current Activities dialog if a user highlighted a Clinic Appointment/Visit and pressed \<Enter\>, the Encounter Location edit box was not updated with the correct encounter. For the update to happen correctly, the user had to highlight the Clinic Appointment/Visit then press the Spacebar (which caused the Encounter Location editbox to be updated), and when the user closed the dialog, the correct encounter was displayed on the CPRS header bar. Developers have corrected this: The Encounter Location edit box is now automatically updated when the user highlights the Clinic Appointment/Visit and presses \<Enter\> on the Provider and Location for Current Activities dialog.

Reminders

- Change to Whether Reminder Dialogs Store Text - Before CPRS 22 the Reminder Dialog stored the dialog text on the first load. With CPRS 22, the Reminder Dialog was changed to not store the dialog text, which meant that dialogs were reloading every time a user clicked on a dialog, slowing down the application. This change was made for the Women’s Health/CPRS Integration project in CPRS GUI version 24 to look for a flag to determine if CPRS should store the dialog text. If this flag was not found, the dialog text would be stored; but if the flag is found, the dialog text will not be stored. This new flag is currently assigned to two reminders that will not be released until after Reminders version 2.0 is released.
- Required Mental Health Test in a Reminder Dialog – This CPRS GUI version has new code that will make a Mental Health test required in a Reminder Dialog. Reminders version 2.0 must be installed for this functionality to work.
- Null Subscript Error Fix – A users received a “Null Subscript” error when loading the list of Clinical Reminders to be evaluated in CPRS. Developers made a minor update to the routine ORQQPX to fix this problem.
- Hyperlink Problem (NOIS DUR-0903-30815) – Developers fixed hyperlinks that weren’t activating in Reminder dialogs.
- Inappropriate Text Being Passed to Progress Note (NOIS TAM-0903-32504) – If a user processed a reminder dialog that contained a force value for a Primary Diagnosis, which is something internal to the reminder dialog creation, CPRS would include the text “Primary Diagnosis” in the progress note when the user finished the dialog. This problem has been corrected: CPRS will not pass the text to the progress note.
- Comment Prompt Maximum Number of Characters Changed - Developers changed the maximum number of characters for the Comment prompt to 245. Previously, the comment field was too long and could cause an error.

Server Allocation Errors

Returned ORCH CONTEXT MEDS Settings (NOIS: BAY-0903-30560 and CHA-0603-31953) - If a user set a broad date range for displaying active medication orders on the Meds tab, server side allocation errors might occur. This functionality has been returned to its former state with “ORCH CONTEXT MEDS” settings.

Patient Bar Remote Data Views (RDV) List Box

- The RDV List box “all sites” selection now selects all the other sites correctly when space bar is pressed.
- Keyboard Commands Added For Remote Data Views Button - Developers added code so that using Ctrl +Alt +R or Ctrl +Alt +r will activate the Remote Data button.

Section 508 Changes

- Groupbox Titles - JAWS now reads Groupbox titles. For this to work you must use JAWS 5.0 and have the included CPRS JAWS Configuration file(s).
- Drawer Buttons (Notes Tab) - JAWS now reads Drawers Buttons as a button. For JAWS to read it correctly, you must use JAWS 5.0 or higher and have the included CPRS JAWS Configuration file(s).
- Template Editor Graphics - The graphics on the Template Editor Dialog now speak meaningful text with JAWS. For this to work you must use JAWS 5.0 and have the included CPRS JAWS Configuration file(s).
- Change/New Problem Screen Unknown Radio Button – On he Change/New Problem window, the “unknown” radio button under the “Immediacy” section is now spoken correctly. For this to work you must use JAWS 5.0 and have the included CPRS JAWS Configuration file(s).

Event Capture Interface

Date/Time Passed to ECS Application Corrected (NOIS BIR-0703-31839, LIT-1203-70083) - For an inpatient, the date/time passed to the ECS application in the CPRS Event Capture Interface defaulted to the patient admission date instead of the current date. This has been fixed.

Allergy/Adverse Reaction Tracking

- File Order in List of Causative AgentsChanged - The DRUG INGREDIENTS and DRUG CLASS files have been moved farther down the list of files containing matching causative agent search terms. This is to encourage the user to select from other files first (VA Allergies, National and Local Drug) to ensure the best potential for order checking.
- Allergy Lookup Screen Cancel Button Action Corrected - If the user clicked "Cancel" on the allergy lookup screen, CPRS next displayed the allergy entry dialog instead of canceling completely out of the action. This has been corrected.

Clinical Context Management (CCOW)

- Refresh Problem Corrected - In previous CPRS versions, selecting "File/Refresh Patient" also caused a refresh of the current context, which resulted in other linked applications needing to respond to an unnecessary context change request. This has been corrected.
- User Last or Initial Tab Not Being Respected (NOIS MIN-0204-42074) – Developers fixed a problem related to the user's last and/or initial tab settings not being respected on a change of patient.

Patient Selection

- Patient Selection Screen – On the Patient Selection list, users can now press the “Enter” key without generating error messages.
- Changed Display When Clinic Is the Source of Patient Lists (NOIS: CLA-0304-21070) - When the source of the patient list is a “clinic” source, developers made a change so that a second column of the patient names (duplicated names except in the case of “-Alias” listing) no longer displays.

Consults and Procedures

Display Problem Corrected – On the New Consult and New Procedure dialogs, developers corrected the display of the Inpatient/Outpatient radio buttons to remain visible inside their parent group box at all font sizes.

TIU Autosave

Problem with Autosave Corrected - A minor bug was found and corrected which could rarely occur but which could have serious consequences if it did. If the total length of a TIU document was an exact multiple of 300 lines, there was a possibility that some of that document's text might not be saved. Other documents were not affected.