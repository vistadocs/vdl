---
consolidated_title: "release notes cprs gui 26"
app_code: CPRS
doc_type: RN
master_source: "OR*3*215 Release Notes CPRS GUI 26"
master_pub_date: May 2006
consolidated_from: 3 versions
prior_versions:
  - "OR*3*252 Release Notes CPRS GUI 26"
  - "OR*3*258 Release Notes CPRS GUI 26"
---

![](or-3-215-release-notes-cprs-gui-26/001.png)

<span class="smallcaps">CPRS GUI version 26</span><span class="smallcaps">(Patch# OR\*3.0\*215)</span><span class="smallcaps">Release Notes</span><span class="smallcaps">May 2006</span>

<span id="_Toc133804694" class="anchor"></span>Table of Contents

<span id="_Toc133804695" class="anchor"></span>Installation Requirements

<span id="_Toc133804696" class="anchor"></span>Required Patches

Before you can install the CPRS v.26 file OR_30_215.KID, which contains patch OR\*3.0\*215, you must install the following required patches:

- DG\*5.3\*554
- GMRV\*5.0\*3
- IB\*2.0\*267
- IB\*2.0\*317
- OR\*3.0\*198 
- OR\*3.0\*220
- OR\*3.0\*229
- OR\*3.0\*235
- OR\*3.0\*239
- OR\*3.0\*241
- PSJ\*5.0\*112
- PSJ\*5.0\*127
- PSS\*1.0\*93
- PXRM\*1.5\*12
- SD\*5.3\*285
- SD\*5.3\*316
- TIU\*1.0\*175
- TIU\*1.0\*202

<span id="_Toc133804697" class="anchor"></span>Related Patches

The following patches are required for functionality but are not required for installation:

- FH\*5.5\*1
- FH\*5.5\*2
- GMTS\*2.7\*78
- OSLC\*337\*2
- PSO\*7.0\*210
- TIU\*1.0\*186
- XU\*8.0\*265
- XU\*8.0\*337
- XU\*8.0\*361
- XU\*8.0\*395

> **NOTE:** CPRS GUI version 26 requires Internet Explorer 4.0 (IE4) or later. However, PKI functionality requires IE 5.5 or later with 128-bit encryption.

<span id="_Toc133804698" class="anchor"></span>CPRSUpdate

- Range Check Errors – This is identified as Known Issue \# 4 described in the “Known Issues” section below. There is a defect in CPRSUpdate (released with OR\*3.0\*10) which results in range check errors to occur on workstations that have not been rebooted in 24.85 days or more. To prevent the errors from occurring, perform a PC reboot of all PCs prior to the GOLD server copy of the CPRS executable being put in place.
- Unzipping Files and Date/Time Issues – Some ZIP extraction utilities may produce extracted files with the current date/time instead of the files’ original date/times. Before extracting the files, note the file date/times inside the ZIP for CPRSChart.EXE, the help files, and BORLNDMM.DLL. Move these files to the appropriate directory where they can be accessed by all CPRS workstations. After moving the files, compare the file date/times of the extracted copies to those contained in the ZIP. They should be the same. If this is not the case, the CPRSUpdate application may not function correctly.

<span id="_Toc133804699" class="anchor"></span>Environment Check

During internal testing of CPRS GUI v26 and the New Term Rapid Turnaround (NTRT) update of allergy terms a problem was identified. During the NTRT updates when a term's new definition is propagated down through the existing allergies, the patient's orders are checked to see if there is any interaction between the drug ordered and the allergy information.

During that check, a routine from CPRS is invoked to obtain the patient's current orders. That routine is also included in OR\*3.0\*215. As a result, if the NTRT update is running and the site installs OR\*3.0\*215 it's possible to get an error that will cause the NTRT updating to stop.

As a result, developers added an environment check to the OR\*3.0\*215 install that will check if an NTRT update is active. If it is, the user is given a warning message and the installation stops.

> **NOTE:** Please ensure that the environment check passes before distributing the OR\*3.0\*215 CPRS executable.

<span id="_Toc133804700" class="anchor"></span>Installation Compliance Date

The compliance date for installation of OR\*3\*215 is 45 days. The extended date is due, in part, to NTRT updates that are scheduled for Thursdays. It is possible that the NTRT updates could extend into Friday. Sites should NOT schedule the installation of OR\*3\*215 if an Allergies NTRT update is scheduled. These updates are announced via an ANR NTRT Update Information bulletin distributed via Outlook. The bulletin includes the date/time of the update as well as the entities included in the update.

The following patches have also extended their compliance dates to 45 days due to their interrelationship with OR\*3\*215: GMRV\*5\*3, TIU\*1\*202, SD\*5.3\*285, TIU\*1\*184, GMTS\*2.7\*78, PSS\*1\*93, PSO\*7\*214, DG\*5.3\*554, USR\*1\*27.

<span id="_Toc133804701" class="anchor"></span>Additional Required DLL

In order to execute, CPRS GUI v26 requires that an additional Dynamic Link Library (DLL) be accessible in the workstation's search path. The DLL (borlndmm.dll) was exported in advance with CPRS v25 (OR\*3\*195) to ensure that it is in place BEFORE V26 IS INSTALLED. In v25, the existing autoupdate functionality was enhanced so that borlndmm.dll would be copied to the workstation from the GOLD server directory at the same time that the CPRSChart.exe and HLP files were updated. If you use the autoupdate functionality, this update would/will occur when automatically updating from any earlier CPRS version to v25 or higher. The update can be confirmed by the presence of borlndmm.dll in the path defined in the workstation's PATH variable, or in the same directory as CPRSChart.exe after the autoupdate.

If borlndmm.dll is placed in the GOLD directory after v26 is installed, the autoupdate will NOT include the borlndmm.dll and CPRS GUI v26 will not execute. In this case, sites must use SMS continuous push to install the borlndmm.dll on all workstations.

This DLL manages memory when CPRS accesses external Dynamic Link Libraries such as \_VitalsViewEnter.dll.

<span id="_Toc133804702" class="anchor"></span>Local Order Dialogs

If your site has created any local order dialogs from national order dialogs the installer of this patch will receive a bulletin mail message informing them of local order dialogs that may need to be reviewed and updated since this patch modifies nationally exported order dialogs.

<span class="smallcaps">  
</span><span id="_Toc133804703" class="anchor"></span><span class="smallcaps">Patient Safety Issues</span>

- PSI-03-033: Use of “Suspended” Causing Problems (Remedy 67681) – A status of suspended was confusing to some clinicians. As a result, some medications were thought to be discontinued or expired when they were not. After discussion with the CPRS Clinical Workgroup, the status was changed to “Active/Susp” to make the meaning of the status clearer. A description of the status was also added to medication order detailed displays on the Meds and orders tab.

HDS software involved in resolving PSI-03-033: OR\*3.0\*215, GMTS\*2.7\*78, and TIU\*1\*202.

- PSI-03-035: Modifiers for Vitals Should Appear on Cover Sheet (Remedy HD70215) – Previously, vitals modifiers measurements did not appear on the CPRS Cover Sheet. With this patch and the new vitals features, users can enter and view vitals with modifiers.

HDS software involved in resolving PSI-03-035: OR\*3.0\*215.

- Follow-up to PSI-03-060: IV Fluid Order Dialog Duration Limits Created (NOIS HIN-1203-42283 closed with OR\*3.0\*195 release, OR\*3.0\*195 Known Issue \# 2) – Developers changed the IV Fluid Dialog IV duration limit field to restrict the number of digits that can be entered based on the duration type: 2 digits for days, hours, and liters or 4 digits for milliliters.

  PSI-03-060 was closed with the release of OR\*3.0\*195.

Related Issue: PSJ\*5\*120 implemented changes to do a compare of the value entered by the user and parameter settings. It acts on the lowest value. So, in some cases the value entered by CPRS will be ignored if one of the other comparison values is less.

For example,

- If a drug has a day limit of 5 days
- The pharmacist finishes the order as an Admixture that is set up for 1 day
- The provider entered a duration of 10 days

The system would use 1 day

- PSI-04-011:Medical Clerk Placing Medication Orders (Remedy 88582) – In the reported incident, a medical clerk who only held SDMOB and SDOB security keys and was not “authorized to write med orders” in the NEW PERSON file (#200) was able to electronically enter medication orders for a provider. The responsibility for the medication order lies with the physician who signed the order.

Keys and parameters control who is prohibited from either signing or entering orders in CPRS. A user who holds NO keys can enter medication orders in CPRS. In CPRS, only the following users MAY NOT place orders:

- Users whose ordering capability was disabled by parameter “ORWOR DISABLE ORDERING”
- Users who hold more than one ordering signature key: OREMAS, ORELSE, ORES (multiple key conflict)

Other than the above users, regardless of what key users hold (no key, “provider”, or OR\* key), they are all allowed to place orders. But users without ORE\* keys cannot sign and release orders; the medication orders would remain unreleased until signed by a valid provider.

For a no-key user, CPRS cannot tell whether the user is a medical clerk, a medical student, or an outpatient clerk. The last two types of users may need to enter medication orders that would be signed later by a provider.

Sites can control entry of orders by administrative staff and clerks in the following ways:

- To disable an individual user’s capability to enter any clinical order, sites can use the parameter “ORWOR DISABLE ORDERING”.
- To prevent a clerk from entering medication orders, sites can set the parameter OR OREMAS MED ORDERS.
- To prevent a clerk from entering Non-VA medication information, the site can use the parameter OR OREMAS NON-VA MED ORDERS.

No changes to CPRS were made. Documentation changes in OR\*3.0\*215 will address this patient safety issue.

HDS software involved in resolving PSI-04-011: OR\*3.0\*215 and CPRS ReEngineering. CPRS ReEngineering will implement a new system for restricting medication ordering, and evaluating role-based privileges for medication order management.  This system will include tools identifying the roles/users and their ordering privileges.

- PSI-04-012: Show Consult Details(Remedy 67913) – From the Notes tab, it was too easy for a user to miss the Reason for Consult. To address this problem, developers added a “Show Details” button to the title/consult selection (Progress Note Properties) screen. If a consult is selected, the button is enabled. If clicked, the identical detailed display shown on the Consults tab appears in a separate window, including a Print button.

HDS software involved in resolving PSI-04-012: OR\*3.0\*215 and CPRS ReEngineering. CPRS ReEngineering will utilize an indicator to differentiate a consult result from a progress note (e.g., different icon) when browsing notes on the Notes tab if a note is a consult result.

-   
  PSI-04-040: Order Checks Now Appear to Signing Provider (E3R 16750) – CPRS will now display order checks when a provider signs orders, even if the nurse entering the order has taken the “Release w/out MD signature” action. Previously, this was not the case.

HDS software involved in resolving PSI-04-040: OR\*3.0\*215.

- PSI-04-047:Changing “IV Fluids” to “Infusions” (Remedy 70980) – Pharmacy finishes some “injectables” as Unit Dose and some as IV fluids for workflow and accounting purposes. Because there was a concern that some medications that CPRS displayed under the “IV Fluids” display group are not administered intravenously, developers made the following changes:
- “IV Fluid” display group was changed to “Infusion” for IV orders.
- “IV Fluid” order menu was changed to “IV Fluid and Infusion”.
- “IV Fluid” order dialog's title was changed to “Infusion”.

HDS software involved in resolving PSI-04-047: OR\*3.0\*215.

- PSI-04-053: Deletion of Entered in Error Medication Orders (Remedy 68321) – A site entered an order that had a dangerously incorrect dosage, but the order was discontinued immediately when the error was discovered. The order remained visible on the patient's long profile. Because the site sometimes reprints a label off of an inactive order, the site reprinted it once by mistake.  With OR\*3\*215, these changes to restrict actions on erroneous DC’d orders will be required in both CPRS and Inpatient Medications: 
- Site will no longer be able to take an action on orders that were entered in error.
- A new DC/Entered in Error view was created that can be accessed from the custom view.
- The default selection for the DC reasons was removed from CPRS.
- A signature is now required for any orders that was DC’d with a DC reason.
- A bulletin will be sent to Pharmacy when an order is DC’d with a reason of Entered in Error. 

HDS software involved in resolving PSI-04-053: OR\*3.0\*215 and CPRS ReEngineering. CPRS ReEngineering will provide functionality that will allow for changing the DC reason.

- PSI-04-056: Renewed One-Time Complex Inpatient Medication Orders Do Not Display in BCMA (NOIS MIN-1104-40006 closed with the release of PSJ\*5.0\*127) – Following a decision by the Inpatient Medications workgroup, developers changed CPRS to prevent users from selecting one-time schedules for complex inpatient medications. Users can still select the Give Additional Dose Now check box for one-time orders.

HDS software involved in resolving PSI-04-056: OR\*3.0\*215.

-   
  PSI-04-063: Users Can No Longer Take Actions on Orders Discontinued with Entered in Error (Remedy 71078) – Per a decision by the CPRS Clinical Workgroup, developers made a change to CPRS so that users can no longer take actions on orders that are discontinued with a reason of “entered in error”.

HDS software involved in resolving PSI-04-063: OR\*3.0\*215 and CPRS ReEngineering. CPRS ReEngineering will provide functionality that will allow for changing the DC reason.

- PSI-04-065: Remote Data in CPRS GUI Safety and Usability Issues (Remedy 71084) – Previously, if users selected a report prior to selecting from which sites they wanted data, there was no indication that they were not receiving data. The tab would appear, but there would be no remote data because CPRS was written so that the user should select the desired sites and then the desired reports or lab information. Developers corrected this problem.

HDS software involved in resolving PSI-04-065: OR\*3.0\*215.

- PSI-04-066: Expiring Medication Alert Not Generated When Patients on Pass (Remedy 70916) – When patients went on a pass, their medications were placed on hold and because the alert checked against active medications only, the Expiring Medications alert was not triggered. To correct this problem, developers changed the alert to check against active and on hold medications, and the *CPRS Technical Manual* was updated to state that medications with a status of HOLD also trigger this alert.

HDS software involved in resolving PSI-04-066: OR\*3.0\*215.

- PSI-04-067, PSI-04-069: Duration Required for Complex Inpatient Medication Orders Using Then Conjunction and User Must Explicitly Enter Conjunction (Remedy 71096 &71072) – To address these patient safety issues, CPRS now requires the user to enter a duration when selecting “Then” for part of an inpatient medication complex order. Hover text has been added to the drop-down box for Then/And. In addition, CPRS no longer auto-populates the “then/and” column on complex orders. The user must select the conjunction “then” or “and” for each row except the last row in a complex order. CPRS will not save the order if the user has not filled in the “then” or “and” in a valid row.

HDS software involved in resolving PSI-04-067 and PSI-04-069: OR\*3.0\*215.

- PSI-04-068:Uncosigned Progress Notes without Expected Cosigner (Remedy 69324) – Previously, a document with an the author and title that required cosignature could be entered in TIU by means other than the CPRS GUI, but no expected cosigner was identified when the note was entered. Entry of the note could happen through upload or through the note being created automatically by another package. If the author who required cosignature then edited the note in CPRS and signed it using the “Review/Sign Changes” menu item, the cosignature requirement was not enforced as it was if using the “Action/Sign” menu item. The result was a note that required cosignature, but did not have an expected cosigner identified. This note then essentially became invisible to most users of the electronic record. Developers added the same cosigner logic to the Review/Sign Changes item that is on the Action \| Sign menu for consistency.

HDS software involved in resolving PSI-04-068: OR\*3.0\*215.

- PSI-05-002: If a Date/Time Prompt Is Defined in the ORDER DIALOG file (# 101.41) to REQUIRE TIME (as well as the date), then CPRS GUI Will Honor that Setting (Remedy 71166) – Certain generic orders, restraints, require that a time be entered for the nursing order. The workgroup agreed that this was a defect and the software was corrected.

HDS software involved in resolving PSI-05-002: OR\*3.0\*215.

- PSI-05-015: Complex Medication Orders Can Lose Part of The Order on Transfer (Remedy 71262) – In this case, there was a complex outpatient order for a drug where the order is for 3x500mg tablets in the morning and 4X500mg tablets at night. The site has 1500mg as a selectable dose but does not have 2000mg in their the DRUG file (# 50). When the complex order is selected for transfer to inpatient, the inpatient complex order contains the first line of 1500mg in the morning, but not the second line of 2000mg in the evening. It is unknown how long this problem has existed. CPRS allowed the clinician to sign order without any warning that evening dose was not entered.

Resolution:

- Modify the software so that the free-text value populates the dosage fields in the inpatient dialog.
- Remove the old order text from the information box.
- Resize the order dialog and the information box so it is easier to see the active scroll bar.
- Remove boxes from the order caption.

HDS software involved in resolving PSI-05-015: OR\*3.0\*215.

- PSI-05-017: Error in Dose When Copying Order (Remedy 71250) – This PSI addresses the problem of copying an order that has been changed to a new order. Previously in CPRS, the original order text and the new order text would appear in the order dialog’s information box, on the Orders tab, and on the Meds tab. But it was hard to differentiate the most recent order text from the original order text without looking at the text in detail. Developers made some changes to address this problem:
- The order text no longer displays the old order text on the Orders tab or on the Meds tab.
- When copying to a new order, CPRS no longer displays the old order text in the order dialog’s information box. The caption in the order text will now display the most recent order text.
- To make it easier to see that the information window’s scroll bar is active (that there is additional text), developers slightly enlarged the order dialog form.

CPRS still displays the word “Change” before the order text to let the users know that the order was altered at some time. If the users want to see the original order’s detail, they can still view the detail display of the order.

HDS software involved in resolving PSI-05-017: OR\*3.0\*215.

- PSI-05-018, PSI-06-042: Complex Order Units for Duration Field Reverting to Days (Remedy HD71285, HD138222) – For the first part of a complex order, if the user changed the units in the duration field (the default is days), the units would changed back to days when the user moved off that field. Developers corrected this problem.

HDS software involved in resolving PSI-05-018: OR\*3.0\*215.

- PSI-05-026: Expected First Dose Display: CPRS Should Not Strip Out PRN from Schedule (Remedy 87028 closed with the release of PSJ\*5.0\*133) – Previously, CPRS displayed an Expected First Dose on Inpatient Medication schedules with PRN in the base schedule name, but did not display an Expected First Dose on schedules that included a base schedule and a check in the PRN box. In addition, it was noted that BCMA treats any schedule with PRN in its name as a PRN schedule, so there should be no Expected First Dose displayed.

To correct problem for Simple Dose inpatient medication orders, CPRS will no longer look at the schedule text to determine if the schedule is a PRN schedule. CPRS will pass the base schedule and whether PRN has been checked to Inpatient Medications and Inpatient Medications will pass back an indicator telling CPRS if the schedule is considered a PRN schedule. If it is a PRN schedule, CPRS will not display an Expected First Dose.

For a complex inpatient medication order, CPRS will use only the schedule and the PRN checkbox in the first row to determine if the Expected First Dose should display in the order dialog. CPRS will not display the Expected First Dose if one the following is true; the schedule in the first row has a schedule type of PRN, the PRN checkbox in the first row is checked, or if pharmacy cannot determine the expected first dose based on the schedule information in the first row.

HDS software involved in resolving PSI-05-026: OR\*3.0\*215 and OR\*3.0\*243. OR\*3.0\*243 will address the problem in the complex tab of the medication order dialog. OR\*3.0\*243 will also not display the expected first dose if it is an on-call schedule.

- PSI-05-031: Terminated Users Not Displaying in Certain Selection Lists or Views (Remedy 86736) – CPRS excluded terminated users from the selection list for “Notes by author”, as well as in the “Notes - custom view” and problem list “Filters” screen. This has been corrected.

  HDS software involved in resolving PSI-05-031: OR\*3.0\*215.
- PSI-05-033: Drug Message Doesn't Always Display (Remedy 70869) – If the user changes medications in the order dialog box, the Message field from File 50 did not always display for the new drug after selecting a dose. This has been corrected.

HDS software involved in resolving PSI-05-033: OR\*3.0\*215.

- PSI-05-040: Medication Order Comments Not Displaying Properly (Remedy 91982) – CPRS was incorrectly wrapping some of the medication comment text, which might make it appear that text was missing. The text was present, but the display could lead the user to think that information was missing. This has been corrected.

HDS software involved in resolving PSI-05-040: OR\*3.0\*215.

- PSI-05-047: OERR/IV Meds, Problem with IV Order Not Being Visible When Patient Was Admitted While Order Was Still Pending (Remedy 95680) – When a patient was in an outpatient setting and the clinician wrote orders, if the patient was admitted while the orders were pending, it was difficult to ensure that those orders were correctly carried out. The Inpatient Medications for Outpatients (IMO) project addresses this issue. As part of that project, CPRS developers made a change so that if a patient is admitted from an IMO clinic location before orders are signed, CPRS prompts the users to select where the inpatient medication, infusion, or nursing text orders should be handled—in the IMO clinic location or whether they should be handled on the ward.  This should help resolve this type of problem.

HDS software involved in resolving PSI-05-047: OR\*3.0\*215.

- PSI-05-077: CPRS Cover Sheet / Vitals Can Misalign Vitals Labels and Values (Remedy 107085) – If a user selects vitals from the CPRS coversheet and utilizes the scroll bar on the side, the values scroll up but the Y axis that contains the vitals name, such as Temperature, Pulse, etc., stays stationary, resulting, for example, in a value for a Pulse aligning on the grid with the Temperature label. The user could misinterpret the data thinking that the pulse was really the temperature.

HDS software involved in resolving PSI-05-077: OR\*3.0\*215.

- PSI-05-081: Order Check Window Cutting Off Verbiage of Orders (Remedy 107292) – Developers added a fix as directed by the CPRS Clinical Workgroup. The user can view all of the order check text by hovering the cursor over the window to display a hover hint with the complete text.

HDS software involved in resolving PSI-05-081: OR\*3.0\*215 and CPRS ReEngineering. CPRS ReEngineering will assess the possibility of completely recoding the order check windows so that the display box is not limited by the 256 height restriction for the display area.

- PSI-05-083: Priority Field in the Order Dialog Accepts Free-Text (Remedy 108406) – Developers changed the priority field so that users could not enter free-text. Previously, if free-text was entered, the text was ignored and the priority was set to Routine. The Priority field will accept a null value (the user can select the priority and remove the text), which Pharmacy will treat as a priority of Routine.

HDS software involved in resolving PSI-05-083: OR\*3.0\*215 and CPRS ReEngineering. CPRS ReEngineering will provide clinicians with the capability of documenting administration of one-time inpatient medication orders in CPRS similar to the Med Order Button in BCMA.

- PSI-05-091: Order Quantity Field Entry Problems on Change or Copy Action (Remedy 112181) – Previously, if a user began to copy or change an order, the dialog that came up had a 0 (zero) in the Quantity field, and if the user clicked in the field to change the quantity, the user could click to the left of the zero and enter a number while the zero remained—making a quantity of 100 rather than 10, for example. To address these issues, developers changed CPRS so that the quantity from the original order is displayed in the Quantity filed. Developers also changed CPRS so that if the user “clicks” into the Quantity, Days Supply, and/or Refill fields, the value in the field is highlighted so that typing will overwrite the value.

HDS software involved in resolving PSI-05-091: OR\*3.0\*215.

- PSI-05-093: Personal Quick Orders with TIU Objects (Remedy 70924) – CPRS allows users to place TIU patient data objects, such as patient name, allergies, etc., in word processing fields. These objects can be saved in quick orders and they resolve appropriately. However, previously, if a user created a personal quick order, the objects did not resolve each time. So, if a user put a patient name object in the order, the name that appeared in the order would always be the name that was there when the personal quick order was saved. To correct this problem, CPRS now prohibits the saving of quick orders that contain patient data objects.

HDS software involved in resolving PSI-05-093: OR\*3.0\*215.

- PSI-05-096: Loss of Templated Reason for Request (Remedy 113377, OR\*3.0\*195 Known Issue \# 8) –Previously, if a user typed the service name rather than selecting if from the list, the prerequisites or templates did not pop up or populate the Reason for Request. Developers corrected the problem. These items will appear whether the user types the service name or selects it from the list.

HDS software involved in resolving PSI-05-096: OR\*3.0\*215.

- PSI-05-109: CPRS RDV Radiology Reports and One Day Selection Problem (Remedy 119689) – Previously, if a user set the date range for Remote Data Views Radiology reports using the From and To fields and set both date as the current day, CPRS did not display the reports. Developers corrected this problem.

HDS software involved in resolving PSI-05-109: OR\*3.0\*215 and VistAWeb v6.

- PSI-05-110: Changing a Diet Order in CPRS Does Not Warn User that Diet Will Be Replaced (Remedy 120487 & 127367) – Previously, if a user entered a diet order, the order automatically replaced any existing diet order, and if no stop date was entered, any future diet order was also replaced. Diet orders have always worked this way in CPRS. To give the user a warning, if the patient has a current diet order or a future diet order where the date of the order they are entering overlaps the future order date, developers added a popup box to Inpatient Diet ordering that warns the user that the new order they are entering will replace the current diet, and if the user does not enter a stop date, that any future diets will also be replaced. The warning message contains the text of any applicable diets.

HDS software involved in resolving PSI-05-110: OR\*3.0\*215 and CPRS ReEngineering. CPRS ReEngineering will reevaluate other ordering functionality to determine if it would be better/more consistent to allow users to change a current diet order rather than creating a new order.

- PSI-05-112: Multiple Entries for Volume Do Not Display on Initial Entry to the IV Ordering Screen (Remedy 119250) – If a user entered the IV Ordering screen and selected the Solutions tab, CPRS did not display the values for volume if there were multiple values. The drop-down box did appear after clicking in the Volume window. If the user selected the Additives tab first and then the Solutions tab, the drop-down box with the volume values appeared as it should. Developers changed CPRS so that when the user orders an IV fluid, CPRS will automatically display the Volume drop-down box the initial time a user entered either the Solutions or the Additives tab.

HDS software involved in resolving PSI-05-112: OR\*3.0\*215.

- PSI-06-035: Patient Orders Appearing under the Wrong Category on the Orders Tab (Remedy 134817) – This problem occurred when a patient is in the process of being admitted. Usually within 15 to 20 minutes of the ADT movement, the provider placed one or more orders through an order set or quick orders that included medications. The medications on the Orders tab displayed under the Outpatient Meds service. However, on the Meds Tab, all the orders display under the Inpatient Meds section. The medications do appear in BCMA. With CPRS 26, an order may be entered for inpatient at an outpatient location. When the order is signed, the order location is changed back to the inpatient location. If the patient is admitted before the orders are signed, a warning is displayed alerting the user that all additional orders will use the ward as the location.

HDS software involved in resolving PSI-06-035: OR\*3.0\*215.

<span id="_Toc133804704" class="anchor"></span><span class="smallcaps">Known Issues</span>

There are six known issues with CPRS v.26, and a CCOW/VPN Known Issue.

- Known Issue \# 1:PSI-06-007: IMO Text Orders Are Not Accessible on Nurse Dashboard – IMO Nursing Text Orders are displayed under the new IMO display group, Clinic Orders, because these text orders are frequently protocol orders and should be associated with the other IMO orders. However, because these text orders display under Clinic Orders, they are not accessible from the Nurse Dashboard.

Impact: The impact of this problem is minimal due to the low number of sites using Care Management. Nurses will need to use CPRS along with Care Management to get all of the information. Additionally, many sites have defined local display groups for text orders. Any text order that is not a member of the Nursing display group will experience the same problem.

Workarounds: To make these appear in the Care Management Nurse Dashboard, the Clinic Orders display group must be a member of the Nursing display group.

Resolution: This issue will be resolved with ORRC\*1\*3.

- Known Issue \# 2:PSI-06-021: IMO & Care Management: Verify column headlights in Care Management – If a user orders inpatient medications from an IMO location, they will display under the Verify column in Care Management. Other types of orders such as for Radiology, Lab, etc. will not display under the Verify column in Care Management.

Impact: The impact of this problem is minimal due to the low number of sites using Care Management. Nurses will need to use CPRS along with Care Management to get all of the information.

Workarounds: There is no known workaround for this issue.

Resolution: To be determined.

- Known Issue \# 3: Problem OR ALLERGY ENTERED IN ERROR Parameter Inheritance – If the sites set the OR ALLERGY ENTERED IN ERROR to YES at the highest class level, all of the lower or subclasses could also mark allergies as entered in error. This is functioning correctly. However, if a site set the highest level to YES and then set one of the lower classes to NO, the lower class setting was ignored and users in the lower class who should not have been able to mark allergies as entered in error could do so. Or, if the settings were reversed with the highest class set to NO and the lower class set to YES, the user would not be able to mark them.

Impact: The impact of this issue is minimal. In CPRS GUI v25 anyone can mark an allergy as entered in error. Because the inheritance is not functioning correctly, sites may not be controlling the ability to mark allergies as entered in error as they want: individuals that sites do not want to mark allergies as entered in error may be able to or individuals who should be able to mark an allergy as entered in error, may not be able to do so.

Workarounds: If sites want to set only the highest level setting, no other work is required. However, if sites want to set lower-level subclasses differently, they should not set the highest level class, but must then set each individual subclass.

Resolution: This issue will be resolved with OR\*3.0\*243.

-   
  Known Issue \# 4: Rational Clearquest ticket 11208: CPRSUpdate causing Range Check errors – There is a defect in CPRSUpdate (released with OR\*3.0\*10) which results in range check errors on workstations which have not been rebooted in 24.85 days or more. To prevent the errors from occurring, perform a PC reboot of all PCs prior to the GOLD server copy of the CPRS executable being put in place.

Impact: The impact of this issue is minimal. The impact is that CPRSUpdate will not run unless the workstations are rebooted.

Workarounds: Perform a PC reboot of all PCs prior to the GOLD server copy of the CPRS executable being put in place.

Resolution: This will be fixed by patch OR\*3.0\*252.

- Known Issue \# 5: Expiring Meds Alert NOT Firing for IMO Orders (CQ 11409) – Expiring meds notifications are sent based on the display group in CPRS. Because IMO orders are displayed under the CLINIC ORDERS display group and this group is not checked for expiring medications, no expiring meds notification is performed.

Impact: The impact of this issue is moderate. Expiring med alerts will not be triggered and clinicians will need to be more vigilant in watching these medications, but the impact should be small because IMO medications will normally be given in clinic.

Workarounds: None

Resolution: This will be fixed by patch OR\*3.0\*251.

- Known Issue \#6: When Trying to Use Drug Class, the Graph Is Blank (CQ 11408) – When using Drug Class to set up public views for graphs, the graph is blank. If you select a drug class, it does not display.

Impact: The impact of this issue is moderate. Users will not be able to graph drug classes but may use other methods, such as the drug name.

Workaround: None

Resolution: This will be fixed by patch OR\*3.0\*251.

- CCOW/VPN Known Issue: CCOW May Not Work Properly If You Use VPN to Access the VA Network Remotely. If you receive an error message when you use CCOW-compliant applications via VPN, the current workaround is to disable the context. If you are using multiple VistA applications while CCOW is disabled, please be sure to verify the active patient when switching applications.

Resolution: The Sentillion v3.9.1 upgrade will resolve this issue, as will (independently) the VPN upgrade, however the availability for these upgrades is not known at this time.

- ADDITIONAL ISSUES – During the testing of CPRS GUI v.26 (OR\*3.0\*215), internal Software Quality Assurance (SQA) and the test sites discovered additional issues that were not resolved in OR\*3.0\*215. A document listing these issues is available upon patch release on the CPRS page: <http://vista.med.va.gov/cprs/>

<span id="_Toc133804705" class="anchor"></span><span class="smallcaps">New Functionality</span>

- Adding VistaWeb to the CPRS Tools menu
- Adverse Reaction Tracking (ART) / Allergies
- Blood Bank (VBECS) Order Dialog Enhancements
- CCOW User Context
- Consults
- Enhanced Graphing Tools (multi-axis)
- HDR Support for Remote Data Views
- Inpatient Medications for Outpatients (IMO)
- MyHealth*e*Vet/Patient Insurance Identifier
- Non-VA Medications
- Notifications
- Orders
- Patient Record Flags, Phase II
- Program Enhancements for Outpatient Meals
- Progress Notes Text Search
- Reminders
- Remote Data Views (RDV)
- Scheduling-Redesign changes
- Support for Patient Financial Services System (PFSS)
- Vitals

  Adding VistaWeb to the CPRS Tools menu

To access VistaWeb, CPRS originally used an entry on the CPRS Tools menu as discussed in the informational patch OR\*3.0\*230. In CPRS GUI v.26, developers added a way to make VistaWeb the default for viewing data from other sites. This can be done in two ways: an option on the list when the Remote Data button is selected will change the default to VistaWeb if checked or a selection the user can make by choosing Tools \| Options and then going to the Reports tab. Users can choose to use VistaWeb as their default or keep the current Remote Data Views as their default.

Because this option is available, sites can choose to remove the VistaWeb item from the Tools menu or leave it there. Below is an example listing of the CPRS GUI Tools Menu with the VistaWeb option:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[DEVCUR.FO-SLC.MED.VA.GOV\]

9 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 9 Package ORDER ENTRY/RESULTS REPORTING

Parameters set for 'Package' may be replaced if ORDER ENTRY/RESULTS REPORTING is installed in this account.

-- Setting CPRS GUI Tools Menu for Package: ORDER ENTRY/RESULTS REPORTING --

Select Sequence: ?

Sequence Value

-------- -----

1 &Time=Clock.exe

2 &Calculator=Calc.exe

3 &Windows Introduction=WinHlp32 Windows.hlp

4 &Notepad=Notepad.exe

5 VistAWeb=https://vistaweb.med.va.gov

Select Sequence: 5

Sequence: 5// 5

Name=Command: VistAWeb=https://vistaweb.med.va.gov

Modifications:

Changing the default sets a new parameter that stores the user preference for Remote Data, ORWRP VISTAWEB:

NAME: ORWRP VISTAWEB

DISPLAY TEXT: Replace RDV with VistaWeb

VALUE TERM: REPLACE RDV WITH VISTAWEB

VALUE DATA TYPE: yes/no

VALUE HELP: Enter YES to make VistaWeb the default for viewing remote data.

DESCRIPTION:

This parameter determines which tool to use for viewing remote patient data, VistaWeb or RDV (Remote Data Views).

PRECEDENCE: 1 ENTITY FILE: USER

PRECEDENCE: 2 ENTITY FILE: DIVISION

PRECEDENCE: 3 ENTITY FILE: SYSTEM

PRECEDENCE: 4 ENTITY FILE: PACKAGE

- Developers added code that checks this parameter value for default Remote Data preference.
- The new RPC for parameter check is ORWCIRN VISTAWEB
- The new RPC for changing parameter is ORWCIRN WEBCH

Based on the value of the ORWRP VISTAWEB parameter, the Remote Data button invokes RDV or VistaWeb accordingly.

Changes

- The ORWRP VISTAWEB parameter can be edited in both CPRS Vista and GUI parameter edit options.
- This parameter is on the ORQP REPORT MGR MENU, which is accessed from the GUI Parameters menu.
- The parameter can also be edited from the GUI Tools Options menu item and selecting the Reports Tab.
- To make it easy to set VistaWeb as the user’s default choice, developers added a new item to the drop-down list of remote sites. The first item in the list of checkboxes is “Use WebVista from now on”. When the user selects “Use WebVista from now on”, the Remote Data button will then invoke the VistaWeb application.
- To change back to RDV after changing this parameter to use VistaWeb, users can go to the Tools \| Options \| Reports menu and reselect RDV, or ask a clinical coordinator to change the parameter from their menu in VistA.

Instructions for Removing VistaWeb from CPRS Tools Menu

Patch OR\*3.0\*230 gave a detailed explanation and instructions for adding VistaWeb to the CPRS Tools Menu. If sites have added VistaWeb to the tools menu, they may now want to remove this option because CPRS v.26 has implemented VistaWeb as an alternative for RDV by allowing the Remote Data button bring up VistaWeb. Here are the instructions for removing VistaWeb from the tools menu:

Removing CPRS User Hyperlink to the CPRS Tools Menu

There are two paths available to add the VistAWeb hyperlink to the CPRS Tools Menu

1.  Go to the GUI Tools Menu using one of the paths below:

Path \#1

1)  At Select OPTION NAME: \<type\> ORMGR
2)  From Select CPRS Manager Menu Option: \<type\> PE (CPRS Configuration (Clin Coord) ...)
3)  From Select CPRS Configuration (Clin Coord) Option: \<type\> GP (GUI Parameters...)
4)  From Select GUI Parameters Option: \<type\> TM (GUI Tool Menu Items)

  
Path \#2

1)  At Select OPTION NAME: \<type\> XPAR MENU TOOLS
2)  From Select General Parameter Tools Option: \<type\> EP (Edit Parameter Values)
3)  From Select PARAMETER DEFINITION NAME: \<type\> ORWT TOOLS MENU
2.  From the list of parameter entities displayed, choose 4 to set the CPRS GUI Tools Menu at the System level.
3.  At the “Select Sequence:” prompt enter '?' to view the current items on the CPRS GUI Tools Menu
4.  Enter an appropriate sequence number. For example, in the following situation you would choose '5' to select VistaWeb:

Sequence Value

-------- -----

1 &Time=Clock.exe

2 &Calculator=Calc.exe

3 &Windows Introduction=WinHlp32 Windows.hlp

4 &Notepad=Notepad.exe

5 VistAWeb=https://vistaweb.med.va.gov

Select Sequence:

5.  Enter '@' at the Sequence prompt.
6.  The item is now deleted.
7.  Now you can exit the option and verify that the Menu item shows up.

<span id="_Toc133804706" class="anchor"></span>Adverse Reaction Tracking (ART) / Allergies

Causative Agent Not Found Informational Text Box – This dialog was enhanced to provide additional instructions to the user.

Blood Bank (VBECS) Order Dialog Enhancements

> Developers made changes to CPRS by including a new order dialog to support VBECS (VistA Blood Establishment Computer Software), however it won’t be active or accessible until VBECS and OR\*3.0\*212 are both also installed. Additional CPRS changes are also planned for OR\*3.0\*243.

<span id="_Toc133804707" class="anchor"></span>CCOW User Context

Developers added new support for the CCOW/User Context (UC) standard to CPRS. With the appropriate Kernel patches installed, this support will enable single sign on for UC-aware GUI applications (e.g., CPRS, Care Management, or Vitals). If a user has logged in to a UC-aware application (entered their access and verify codes and gotten in), then while the application is still connected to VistA and the user then launches other GUI applications that are UC-aware, the user will not be required to enter access and verify codes again. This support works with Delphi clients, Web applications, and Java applications. Simplified sign-on and CCOW user context have been enabled. The default functionality is to proceed with simplified sign-on, if all patches are in place, on both VistA and CCOW vault. The command-line parameter "CCOW=PATIENTONLY" will disable on a single shortcut basis. For complete details, see documentation at: [<u>http://vista.med.va.gov/kernel/sso/download.asp#documentation</u>](http://vista.med.va.gov/kernel/sso/download.asp#documentation)

For Shared PCs

Developers added a new command-line parameter to allow enabling of patient context without also enabling user context. This should alleviate many of the problems reported by test sites related to workstations shared by multiple users. To enable patient context, but not user context, include the parameter CCOW=PATIENTONLY on the command line of the shortcut, following CPRSChart.EXE and/or any other command-line parameters. If the shortcut has several command-line parameters other than CCOW= (such as SPLASH= or P=), where the CCOW parameter falls in the order is not important, but only one “CCOW=” parameter (DISABLE/FORCE/PATIENTONLY) may be used on any given shortcut. If more than one CCOW= command-line parameter is included, CPRS will use the first parameter it encounters (reading left to right).

<span id="_Toc133804708" class="anchor"></span>Consults

The behavior of the ORWOR SHOW CONSULTS parameter and the “nag” screen has been modified in accordance with review by the CPRS Clinical Workgroup. The “Would you like to see a list...” dialog has been eliminated. The new behavior is as follows:

- Parameter set to NO

The list of consults is not initially displayed on the note title screen, regardless of whether there are pending consults the user is able to resolve. Clicking a Consults-class title will still display the list of unresolved consults, if any.

- Parameter set to YES
- If there are unresolved consults for the user, the user is presented directly with the note title screen with the list of unresolved consults displayed.
- If there are no unresolved consults for the user, the list of consults is not displayed on the note title screen. Clicking a Consults-class title will still display the list of consults.  
    
  Once on the note title screen, if the user selects a consult, and then clicks a non-Consults title, a new warning is displayed, indicating that the selected title will not complete the selected consult:
- If the user answers YES/CONTINUE with this title, the list of consults is hidden, and the user clicks OK as usual to start the note without completing a consult.
- If the user answers NO, the selected title is deselected, the consults list remains visible, and the user is allowed to choose another title, and then click OK to continue with the completion of the consult.

<span id="_Toc133804709" class="anchor"></span>Enhanced Graphing

CPRS developers added new graphing capabilities. The new features are dependent on the new Clinical Reminders indexing tool. If the site has run the index, users will be able to graph numerical data such as lab results and vitals as well as episodes and events such as medications and exam dates. Graphing can be accessed from the Reports tab, the Labs tab, the Tools menu, or from any tab using the shortcut key Ctrl + G. On the Reports tab, the graphing pane is embedded in the tab, but from the other locations, the graphing features are launched is a separate window that can stay open while browsing the patient’s chart. Essentially, users can graph anything anywhere. All types of data can be graphed together for comparisons within the same time frame. The user can display the information on the same graph to show the relationship between the two items or on separate graphs.

<span id="_Toc133804710" class="anchor"></span>HDR Support for Remote Data Views

- With HDR the Remote Data Button Will Only Turn Blue if Data Is Available from Sites Other than HDR – Developers added code to support Clinical Workgroup recommendations regarding HDR reports in the Reports Tab. The change modifies the trigger that causes the Remote Data button text to turn blue. If the HDR facility is included in the list, at least one additional facility must be included for the RDV button to turn blue.
- Parameter to Control Remote Data Views Access to the HDR – CPRS developers created a new parameter ORWRP HDR ON that controls whether a site will query the HDR for remote data. This parameter will be OFF when exported, so that sites will not be querying the HDR. (This item is also in another section of this document.)

> **WARNING:** Sites should not enable this parameter until they receive official instructions. There is the possibility that inaccurate or misaligned data could be displayed in CPRS.

<span id="_Toc133804711" class="anchor"></span>Inpatient Medications for Outpatients (IMO)

As stated in the OR\*3.0\*195 patch description, Inpatient Medications for Outpatients (IMO) features will not be available in CPRS until patch SD\*5.3\*285. Because SD\*5.3\*285 is a required patch for OR\*3.0\*215, once OR\*3.0\*215 is installed IMO functionality will be available for use. Refer to the IMO Release Notes (PSJ_5_P121RN.doc) that will be released with patch PSJ\*5\*121.

<span id="_Toc133804712" class="anchor"></span>MyHealth*e*Vet/Patient Insurance Identifier

CPRS now has a button to quickly access a patient’s MyHealth*e*Vet or patient insurance information. The button is located next to the Flag button. Unlike other buttons, this button is only visible if the patient has MyHealth*e*Vet information or insurance information. If the patient has neither, the button does not display. If the patient has one, but not the other, the button displays the wording for what the patient has. If the patient has both, the top half of the button is labeled MHV and will access MyHealth*e*Vet information, and the bottom half of the button is labeled Pt Insur and will bring up a detailed display with the patient’s current insurance information. By placing the mouse over each part of the button, the hover hint indicates whether the patient has MyHealth*e*Vet data or insurance information.

> **NOTE:** The MyHealtheVet functionality will not begin to appear until MyHealtheVet In Person Authentication is released.

<span id="_Toc133804713" class="anchor"></span>Non-VA Meds

Non-VA Quick Orders – Developers added the ability to create and use quick orders for non-VA medication orders. The non-VA quick orders can be autoaccepted.

<span id="_Toc133804714" class="anchor"></span>Notifications

- Alert Sort Order Now Saves – Developers added code to save the direction of the alert sort direction (ascending or descending) in the CPRS GUI
- Separation of Notifications for Inpatient and Outpatient Expiring Orders (E3R 12229) – Developers added a new notification, MEDICATIONS EXPIRING - OUTPT and changed the name of the notification MEDICATIONS EXPIRING to MEDICATIONS EXPIRING - INPT. MEDICATIONS EXPIRING - OUTPT will affect orders entered on an outpatient, and MEDICATIONS EXPIRING - INPT will affect orders entered on an inpatient.

> **NOTE:** Please be aware that if the MEDICATIONS EXPIRING - OUTPT notification is turned on, there is the potential for a significant increase in the number of alerts generated. Please thoroughly examine the parameters that control the generation of this new notification using the NOTIFICATION MGMT MENU options “Enable/Disable Notifications”, “Set Default Recipient(s) for Notifications” and “Set Provider Recipients for Notifications”.

- CPRS GUI Parameter to Allow Deletion of Non-CPRS Alert Using Remove Button (Remedy 70715, Remedy 70953, Remedy 70910, E3R 19155) – Developers added a new parameter ORB REMOVE NON-OR to CPRS that enables sites to designate which non-CPRS (non-OERR) alerts that can be deleted without processing using the Remove button in the CPRS GUI. Sites can only set the ORB REMOVE NON-OR parameter at the System level.  
    
  To use this parameter, sites enter the alert identifier (or the first few characters of the alert identifier) for each type of alert users can remove using the Remove button. The alert identifier or XQAID can be found in the ALERT ID field of the ALERT file \[#8992\]. For example, to remove NOIS alerts enter FSC as the parameter value. Sites may enter as many alert identifiers as desired to enable removing of multiple alert types.

> **NOTE:** Use caution when designating which alerts users should be allowed to remove. Entering too much information (characters of the alert ID) may not cover all types of the alerts. Only use that portion of the alert ID which is consistent for the alert type you wish to remove. Most alert IDs include information specific to the patient or instance which triggered the alert. For example, a NOIS alert's ID might actually look like FSC-M,275546. Entering the entire alert ID in this parameter will only allow removal of this specific alert. However if you use FSC for the parameter value, all NOIS alerts can be removed. Entering too little information could enable users to remove alerts that should not be removed.

> The following are examples of non-OR alert IDs:

> NO-ID;17;3040628.131502 \[Taskman alert\] - use NO-ID in parameter TIUERR,3423,1;1450;3040518.125801 \[TIU error alert\] - use TIUERR TIU28907;17;3040720.134827 \[TIU alert\] - use TIU in parameter

For the above examples, for instance, entering TIU will also enable removing TIUERR alerts. Use TIUERR if you only want to Remove TIUERR alerts.

The option path for setting the parameter to enable removing non-OR alerts is:

Select OPTION NAME: ORMGR CPRS Manager Menu menu

…

PE CPRS Configuration (Clin Coord) ...

…

Select CPRS Manager Menu Option: PE CPRS Configuration (Clin Coord)

…

GP GUI Parameters ...

…

Select CPRS Configuration (Clin Coord) Option: GP GUI Parameters

…

NON GUI Remove Button Enabled for Non-OR Alerts

Select GUI Parameters Option: NON GUI Remove Button Enabled for Non-OR Alerts

Setting Remove Non-OR Alerts Without Processing for System: ZZZ

Select Alert ID: XXX

Are you adding XXX as a new Alert ID? Yes// YES

Alert ID: XXX// XXX

Enable removing this type of alert?: YES

The following is an example of finding an alert ID in FileMan.

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: ALERT//

Select ALERT RECIPIENT: CPRSPROVIDER,FOUR

RECIPIENT: CPRSPROVIDER,FOUR

ALERT DATE/TIME: FEB 00, 2004@00:00:00 ALERT ID: TIUERR7;1450;3040202.141536

MESSAGE TEXT: FILING ERROR: JAS Invalid Report Type encountered.

ACTION FLAG: RUN ROUTINE ENTRY POINT: DISPLAY

AROUTINE NAME: TIUPEVNT

DATA FOR ALERT: 7;FILING ERROR: JAS Invalid Report Type encountered. ;3315;

ALERT DATE/TIME: FEB 00, 2004@00:00:00 ALERT ID: OR,57,50;1326;3040202.120248

MESSAGE TEXT: CPRSPATIENT, (C7895): \[CARD\] New order(s) placed.

ACTION FLAG: RUN ROUTINE ENTRY POINT: NEWORD

AROUTINE NAME: ORB3FUP1 CAN DELETE WITHOUT PROCESSING: YES

DAYS FOR SURROGATE: 0 DAYS FOR SUPERVISOR: 0

DAYS FOR BACKUP REVIEWER: 2 DATA FOR ALERT: 10000274;1@OR\|

PATIENT: CPRSPATIENT,TWELVE

<span id="_Toc133804715" class="anchor"></span>Orders

Discontinuing an “Entered in Error” Order Generates a Bulletin – CPRS now generates a bulletin when a user discontinues a drug order and the reason is “Entered in Error.” The new bulletin name is OR DRUG ORDER CANCELLED. The new bulletin will be sent to the new mail group named OR DRUG ORDER CANCELLED.

<span id="_Toc133804716" class="anchor"></span>Patient Record Flags, Phase II

Developers added the ability to show which Progress Note provides the supporting clinical information for an assignment (new, activate, continue, entered in error, or inactivate) of a Patient Record Flag (PRF). The Progress Note title displays in the detailed display of a PRF.

Also, when a user selects the appropriate Progress Note title to provide the clinical reasons for a PRF, the user must choose to which flag assignment (activate, inactivate, continue, etc.) the note pertains. The user can no longer write the note first and then create the flag.

On the Patient Record Flags popup, CPRS now has an area that displays the signed linked notes that are related to the flag. Users can click an entry to bring up the related progress note in a separate detail window from which the note can be viewed or printed.

Please see patches TIU\*1.0\*184, USR\*1.0\*27, and DG\*5.3\*554 for more information.

<span id="_Toc133804717" class="anchor"></span>Program Enhancements for Outpatient Meals

Developers have added code to CPRS version 26 to support the ordering of recurring and special meals for outpatients, in conjunction with the release of Dietetics version 5.5. The same options that exist with inpatient diets are also available with outpatient meals: tubefeeding, early/late tray, isolation/precautions, and additional order. Dietetics 5.5 must be installed for the outpatient meals functionality to be enabled in CPRS.

Before users can order meals for outpatients, sites must set up the following in the Nutrition & Food Service package:

- Outpatient meal locations
- Outpatient diets
- To activate the "bagged meal" checkbox to appear in CPRS, the field "PROVIDE BAGGED MEALS?" in the COMMUNICATIONS OFFICE file must be set to YES. It only appears on the Early/Late Tray tab, and on the popup Late Tray dialog.

Sites will also need to do the following in the CPRS package:

- Add order dialogs FHW SPECIAL MEAL and/or FHW OP MEAL to the CPRS Write Orders order dialog so that it is available to users

For special meals to auto-generate meal vouchers, CACs or other individuals can give the Nutrition and Food Service key (FHAUTH) to some users so that when the user electronically signs the order, the meal voucher is authorized. If the user who signs the order does not have the FHAUTH key, the meal voucher will not be authorized until a wet signature is applied by an authorized individual. Special meal vouchers include the initial letter of the patient's surname plus last 4 numbers of the patient's social security number (SSN) when printed from CPRS.

As part of the install process, CPRS sets a value for three parameters that control print format for the Outpatient meal ticket. These parameters are listed below and the value for the Dietetics package is shown in parenthesis following the name of the parameter.

- ORPF WARD REQUISITION HEADER (FH OUTPT MEAL HEADER)
- ORPF WARD REQUISITION FORMAT (FH OUTPT MEAL TICKET)
- ORPF WARD REQUISITION FOOTER (FH OUTPT MEAL FOOTER)

These three print formats should not be altered.

Outpatient meals will not auto-DC on admission unless an auto-DC rule is created under the Event-Delayed Orders menu in CPRS. To make outpatient meals discontinue when the patient is admitted, an ADMISSION rule should be created and include the Dietetics package. Any recurring outpatient meal that is discontinued, whether manually or auto-DC’d, will also discontinue any associated early/late trays, tube feedings, and additional orders.

Displaying Outpatient Meals Ordered prior to CPRS v.26 Installation

Patch FH\*5.5\*2, released 3/2/2006, includes a routine \[FHPST2\] which can be run to update the Orders (#100) file with any outpatient meals ordered in VISTA prior to CPRS v26.  The FHPST2 routine does not need to be run until <u>AFTER</u> CPRS v26 is installed.  Running the FHPST2 routine in an environment that does not have CPRS v26 will NOT cause any damage.  The routine will simply error out since the CPRS v26 routines are not yet present.  Once CPRS v26 is installed the update can be run at anytime.

The Clinical Application Coordinators and the Nutrition & Food Service ADPAC/Staff should discuss the advantages of running this routine which are described below.

CPRS v26 allows ordering outpatient meals through CPRS – up until now you could only order through VistA options – because of this change the routine FHPST2 will allow the data previously entered in VistA to show on the CPRS orders tab.

If you have not implemented outpatient meals prior to the installation of CPRS v26 you do not need to do anything.  Just as a reminder, implementing outpatient meals is OPTIONAL.

If you are running outpatient meals now, once the new CPRS v26 is installed you will not be able to see outpatient meal data entered before CPRS v26 was installed…you will only be able to see orders entered after the installation.   If you want to be able to view this “historical” data (–i.e. entered before CPRS v26) then IRMS should run this routine.  If it is not important to view the past data in CPRS then IRMS does not have to run the routine. 

<span id="_Toc133804718" class="anchor"></span>Progress Notes Text Search

Developers added a new text search feature. This feature searches the current list of notes to find all notes that contain the exact text that a user enters and then displays those notes in the treeview of the Notes tab.

<span id="_Toc133804719" class="anchor"></span>Reminders

Before CPRS v.26, any Reminder that received an M error or the Due Status could not be determined, the Reminder would not display on the Cover Sheet. Now with Reminders 2.0 and CPRS v.26, the following occurs:

- If the Reminder receives an M error, the Reminder will appear on the Cover Sheet with a status of Error. If the user clicks on the Reminder the Clinical Maintenance window displays with a message reading “Contact your Clinical Reminders Coordinator”.
- If the Due Status could not be determined, the Reminder displays on the Cover Sheet with a status of “CNBD”. Please refer to the *Clinical Reminders* 2.0 manual for more detail information.

<span id="_Toc133804720" class="anchor"></span>Remote Data Views

Developers enhanced the current RDV feature on the Reports tab to support the display of clinical data stored in the Health Data Repository Historical (HDR-Hx) and Health Data Repository Interim Messaging Solution (HDR-IMS). When ready, these two databases will include clinical data from all Veterans Administration Medical Centers (VAMCs), and in the future, some Department of Defense data as well.

Patient data housed in the HDR-Hx and HDR-IMS databases shall displayed on the Reports tab in the same manner that data from other VAMCs and Federal Health Information Exchange (FHIE) is now displayed.

> **NOTE:** The enhanced RDV changes shall remain dormant until such time that the HDR and Clinical Data Services (CDS) are ready to receive and transmit data. At that time patch OR\*3.0\*238 will be released to implement the enhancements.

<span id="_Toc133804721" class="anchor"></span>Scheduling Redesign Changes

CPRS now includes support for the new Scheduling changes. In preparation for future Scheduling package changes, developers modified CPRS to properly handle situations when the Scheduling system is unavailable. If the Scheduling system was unavailable, CPRS users would not be able to do certain things such as using a patient’s list of clinic visits, defining a personal list using clinics, and viewing future appointments on patients. The other functions of CPRS would continue; users could still select any patient and get just about any information other than appointment data. Users could still lookup clinic names and get patient demographics, etc.

<span id="_Toc133804722" class="anchor"></span>Support for Patient Financial Services System (PFSS)

The purpose of the Patient Financial Services System (PFSS) project is to help automate the billing process by sending needed billing information to the commercial-off-the-shelf (COTS) billing replacement software. The CPRS portion of the PFSS project consists of two phases. The first phase is contained in CPRS v26. Thus CPRS developers have made several changes to CPRS v26 for PFSS. These changes have no affect on any of the sites unless the PFSS parameter (ORWPFSS ACTIVE) is defined and activated. Even upon activation, the sites should see no change to CPRS functionality. The only sites which should define and activate the PFSS parameter are the PFSS test sites. All other sites should not be affected.

The following changes were made to CPRS v26 for PFSS, however the code is controlled by the ORWPFSS ACTIVE parameter and will remain off at all sites, except those testing PFSS:

- The parameter ORWPFSS ACTIVE, when defined and activated, will cause the patient visit string to be stored in the ORDER file (# 100). The patient visit string functionality has been in CPRS for several years but never activated. Note that the ORWPFSS ACTIVE parameter must be defined and activated. The ORWPFSS ACTIVE parameter is defined and managed through the routine ORWPFSS0.
- In addition to the ORWPFSS ACTIVE parameter, developers added new Radiology and Laboratory order dialogs. These enable the patient visit string data to be stored in the ORDER file (# 100) when the parameter ORWPFSS ACTIVE is defined and activated.
- Additional changes to the CPRS GUI to support passing the visit string, but the changes have no affect unless the ORWPFSS ACTIVE parameter is defined and active.

> **NOTE:** The ORWPFSS ACTIVE parameter will not be utilized in phase two of the CPRS PFSS project. Its function will be replaced by an IBB parameter. Thus, the ORWPFSS ACTIVE parameter is used only for testing the storage of the patient visit string in CPRS v26.

<span id="_Toc133804723" class="anchor"></span>VistaWeb Parameter Added

A new parameter has been created to allow sites to edit the web address that points to the VistaWeb interface. Prior to this change, the web address was hard coded in Delphi. Now sites can change this parameter for testing in test accounts, or if the VistaWeb web address changes in the future. The new parameter is ORWRP VISTAWEB ADDRESS. The parameter value should not include any parameters because they will be calculated when the request is made. For example, if the VistaWeb address is:

[https://vhaiswwebv7.vha.med.va.gov/vistaweb/ToolsPage.aspx?q9gtw0=660&xqi4z=%DFN&yiicf=%DUZ](https://vhaiswwebv7.vha.med.va.gov/vistaweb/ToolsPage.aspx?q9gtw0=660&xqi4z=%DFN&yiicf=%25DUZ)

The value of ORWRP VISTAWEB ADDRESS should be:

<https://vhaiswwebv7.vha.med.va.gov/vistaweb/ToolsPage.aspx>

If no value is entered for this parameter, then CPRS will default to: <https://vistaweb.med.va.gov>

<span id="_Toc133804724" class="anchor"></span>Vitals

CPRS will use a new Vitals component enabling users to enter modifiers with vitals, such as standing, sitting, right arm, left arm, etc. Graphing tools are also included with new component. This feature requires a new dynamic link library (GMV_VitalsViewEnter.dll) that must be present for the new vitals features to run correctly; refer to GMRV\*5\*3 for more information.

Vitals and modifiers can now be entered via the GUI by clicking on the Cover Sheet or through the vitals tab on the encounter form (Remedy 69670).

<span id="_Toc133804725" class="anchor"></span><span class="smallcaps">Defect Fixes</span>

<span id="_Toc133804726" class="anchor"></span>Allergies

- Support for Allergy Synonyms – Developers added support for synonyms, if present, in the SIGNS/SYMPTOMS selection box.
- Marking Allergies as Entered in Error Now Controlled by Parameter(OR\*3.0\*195 Known Issue \# 1) – In CPRS v25, any user could enter new allergies, mark a patient as NKA (no known allergies), and mark allergies entered in error from the cover sheet and the detailed display window. In v.26, the Entered in Error option requires the new parameter OR ALLERGY ENTERED IN ERROR to be enabled for the user. The other options remain open to all users as before. This parameter may be set at the system, user class, and the user level.
- Message Now Includes the Same Warning – The “Bulletin has been sent” message that CPRS displays after the user requests the addition of a new causative agent now includes the same warning included in the bulletin about that reactant not being added to the patient's record.
- Backspace to Clear Severity Results in Last Entry Displayed Storing – In the Enter Allergy/Adverse Reaction dialogue if the user selects a severity and then backspaces to clear that entry, the record is stored with the last severity displayed in that field. It should have stored with NO SEVERITY, severity in not a required field. This could result in incorrect severity status being associated with the entry.
- If 39 or More Signs/Symptoms Are Entered in Enter Allergy/Adverse Reaction Dialog, CPRS Returns an M Error – If 39 or more signs/symptoms are entered in Enter Allergy/Adverse Reaction dialog, CPRS returns an M error, kicks the user out of CPRS, and locks up the Cover Sheet for that patient for all users. If users have the Cover Sheet set up as their default tab, they get kicked out as soon as they open this patient. If another tab is their default, users are kicked out if they select the Cover sheet for this patient. If users select the patient on which this error has occurred and select postings (the CWAD button, which indicated there are Allergies for the patient) from any tab, they get the same M error. If the Allergy is marked Entered in Error from the ART package, the Allergy display and the Cover Sheet for that patient return to normal.
- Comments Can Be Blank Although Parameter Is Set To Require Originator Comments For Observed/Drug Allergy – When the GMR Site Allergy Parameters are set to require comments during entry of an observed drug allergy, if text is entered into the comment section and then cleared out, the record is stored with a blank allergy text. If there is no attempt to enter comment text at all, the user gets a message that comments are required.
- Free-Text Signs and Symptoms No Longer Allowed – To support data standardization efforts, developers removed the ability to enter free-text signs/symptoms. Users must now select items from the list of available signs/symptoms.
-   
  Inconsistent Sending of Bulletin for Marked on Chart – CPRS always sent the “Marked on Chart” bulletin if the user entered an allergy from the Orders tab. CPRS never sent the bulletin if the user entered the allergy from the Cover Sheet. This inconsistency has been corrected, and CPRS will never send the bulletin when the user enters a new allergy (regardless of whether it is entered from the Orders tab or Cover Sheet).
- Missing Scroll Bar on Allergy “Entered in Error” Form – On the form to mark an allergy as Entered in Error, the Comments box did not provide a vertical scroll bar for lengthy comments.
- Blank Symptom Error (Remedy 90006) – The error \<SUBSCRIPT\>UPDATE+34^GMRAGUI1 was occurring when a blank symptom was entered. This has been fixed.
- Allergy Dialog Embedded in a Clinical ReminderNo Longer Available (Remedy 110527, OR\*3.0\*195 Known Issue \# 6) – When you click on the box that is supposed to call up the allergy dialog, the allergy dialog does not display. This has been fixed.
- Allergy Signs/Symptoms Entered with a Double-Click Cause Allergy Comments To Be Deleted (Remedy 133444) – When an allergy is entered by double-clicking on the signs/symptoms and then allergy comments are entered, the allergy comments are deleted when the OK button is selected. Because of this the allergy comments are not viewable when the allergy is selected, and they are not stored in VISTA. This has been fixed.

<span id="_Toc133804727" class="anchor"></span>CCOW

- CCOW Disconnect Problems Corrected – Developers added code to handle a CCOW disconnect problem. Now if the user's connection to the context vault fails, CPRS will display an appropriate error message, and the user can continue in most cases. In previous versions, such disconnects often required that CPRS close.
- CCOW Not Breaking Context Correctly – If CPRS begins a patient change and the user chooses to break context because of work in progress in another application, CPRS would refresh the current patient’s information instead of loading the newly selected patient’s information. This has been corrected.
- Context Change Not Allowed with New Vitals Functionality – If another application (A) , or another instance of CPRS (A), attempts a patient change while one instance of CPRS (B) has the Vitals DLL window open, CPRS (B) will be unable to respond to the CCOW survey from the vault requesting permission. In that case, (A) will display a dialog, provided by Sentillion, with "Cancel" and "Break" buttons enabled. If the user chooses "Cancel", the original (A) patient will be redisplayed, and no patient change will occur in (A). If the user chooses "Break", (A) will break from context and change patients, leaving (B) in context with the original patient. There is extensive documentation of all of this behavior in the HL7 CCOW standards documentation, as well as in the documentation from Sentillion.
- Size of CCOW Icons Increased – In response to site concerns about CCOW icon visibility and prominence, developers increased the size of the CCOW icons next to the patient name block.
- CCOW Link Incorrectly Displaying as Linked – If a user has two instances of CPRS open and is connected to two different VistA accounts, selecting a new patient in one will correctly display the “No Patient Selected” screen in the other. If the user then chooses to select a new patient in that disabled copy, but cancels from the patient selection screen, the previous patient for that copy will be displayed, and the CCOW icon will display as “linked”. There will then be two different patients displayed on the screen, both appearing as linked to the patient context. This has been corrected by reverting to the “No Patient Selected” screen if the user cancels, if that screen had previously been displayed.
- Rejoin/Set New Context Causes Loss of Note Text for an Unsigned Note (Remedy 120996) – A provider started a new note in CPRS GUI and it had several lines of text. She realized that she needed further data from VistAWeb but noted that the link was broken for her current CPRS session. She then clicked on File \| Rejoin \| Set New Context and that switched her from the Notes tab to the Cover Sheet. She then accessed VistAWeb using the Tools menu, obtained the needed data from another facility, and closed VistAWeb. The CPRS session was still up and open. She clicked back to the Notes tab where she saw the unsigned note with the header of title, date, author, etc. but the note text was gone. This has been corrected.

<span id="_Toc133804728" class="anchor"></span>CIDC

- HNC Check Box Not Updating Correctly – If a user entered a problem for a patient and indicated that it was associated with Head and Neck Cancer (HNC) and then selected a prosthetics consult and chose that problem, the HNC check box should have been checked, but it was not. The HNC checkbox should now update correctly.
- CIDC Info Incorrectly Required for Discontinued Orders (Remedy 119371) – Orders that are discontinued by a nurse and require a provider’s signature no longer require entry of a diagnosis.
- Prompt Providers for CIDC Information Only for Patients with Active Insurance – This feature was added to v26.
- Inability to Sign ConsultOrders – CIDC providers frequently are unable to sign consult orders; they receive a message that the consult needs a diagnosis although consult order do not require one, and it is even indicated as “N/A”. Developers changed CPRS to ensure that orders with N/A status do not require a diagnosis.
- Sign Orders Window Not Forcing User to Enter Diagnosis – On the Sign Orders window, if the user unchecked the treatment factors and signed the orders, CPRS did not prompt users to enter a diagnosis for each order. Developers changed this and CPRS will now require CIDC users to enter a diagnosis.
- CIDC-related Record Locking Causes Undefined Error (OR\*3.0\*195 Known Issue \# 5) – When users are placing orders, very infrequently an invalid order IEN is stored in the ORDER file (# 100)—specifically, the second node of ^OR(100—resulting in orders being locked on the users at the ancillary level and an undefined error occurring in routine ORWDXR. This error has only been reported by two of the four OR\*3.0\*195 test sites that have installed both CPRS GUI v.25 (OR\*3\*195) and CIDC and have enabled CIDC. To correct this, sites either installed the released OR\*3.0\*229 patch if the site has CPRS v25 installed or installed CPRS v26.

<span id="_Toc133804729" class="anchor"></span>Consults

- Unknown Significant Findings Problem Corrected (Remedy 70231) – Regardless of the value selected for “Significant Findings”, the value stored was the ampersand (&) character, which was subsequently treated as if “Unknown” had been selected. This has been corrected.
- \<Space Bar\> Changed to Not Select Item – If users were ordering a consult from the “generic” consult dialog window and the user pressed the \<Space Bar\> while trying to type in the Consult Service name, the consult that was listed before pressing the \<Space Bar\> was automatically selected. Developers made the \<Space Bar\> enter a space rather than select an item.
- Drawer Missing on Consults Tab (Remedy 95278) – Developers corrected the problem of the Consults tab drawers not displaying.
- Consults Dialog Navigation Problem (Remedy 95986) – If a user tabbed off of the “New Procedure” button, CPRS frequently gave a “cannot focus disabled or invisible window” error. Developers corrected this problem.

<span id="_Toc133804730" class="anchor"></span>Encounter

- Workload Will No Longer Be Required for Non-Count Clinics (Remedy 70381)
- Some Codes Not Available in Lexicon Look Up on the Encounter Form and Consults Tab for Procedures (Remedy 85910) – When a provider went to look up a procedure, the code that the provider was looking for did not appear. In this case, codes 12001, 12002, 12007 were not available to provider when searching for Repair of Superficial Wounds. The Lexicon look up did display codes 12004, 12005, and 12006, but not the other choices. Developers corrected the problem and CPRS now displays all the appropriate codes.
- Reminder Dialog Visit Information Prompts Are Not Enabled when the Same Prompts Are Enabled on the Encounter Form (Remedy 114557) – The visit information requested on the Encounter form did not match the visit information requested from reminder dialogs. When a user opened the encounter form on an outpatient and specific visit information needed to be entered (i.e., SC, Combat Vet, etc.), if the user opened a reminder dialog that contained a Visit button, the same visit information did not show as needing to be entered.
- Length of Comment Field on Encounter Form Changed (Remedy 70222) – Developers changed the Comment field on the Health Factor tab of the Encounter Form to accept only 245 characters. This stops the data loss.

<span id="_Toc133804731" class="anchor"></span>Event Capture Interface

Event Capture Report Can Now Be Viewed (Remedy 70642) – Previously, CPRS users who did not have the “EC GUI CONTEXT” menu option could not view the event capture report on Reports tab. This has been corrected.

<span id="_Toc133804732" class="anchor"></span>Graphing

Reference range displayed on graph in CPRS GUI (Remedy 69284) — In the LABORATORY TEST file (# 60) for the test ALT, a new site/specimen was added (PLASMA) with a new reference range. On the CPRS GUI Labs tab, if the user selected Graph, the graph displayed the patient's results for the date range selected. Within the range selected, there were results for serum and plasma, but the reference range displayed on the graph is for the serum only, and not the plasma. This was corrected in that specimens are now split as separate graphs.

<span id="_Toc133804733" class="anchor"></span>Labs

Grid Index Out of Range Error Corrected (Remedy 69456) – Developers corrected a “Grid Index Out of Range” error on the Labs tab.

<span id="_Toc133804734" class="anchor"></span>Miscellaneous

- Corrected a Rare “\<PARAMETER\> VARVAL^XWBLIB” Server Error Occurring when a User Clicked on a Tools Menu Item (Remedy 71079).
- Hidden Windows – Developers added a change to CPRS that should address the issue of CPRS windows coming up behind other windows and causing the appearance that CPRS is locked up.
- Subscribe to Team Combo Box Problem – The Subscribe to a team combo box under Tools \| Options \| Lists/Teams was not behaving consistently, whether using the mouse or the keyboard. The confirmation message should now appear on the first try, instead of the second.
- Remove OTHER from Location Selection Lists in CPRS (Remedy 114751) – Hospital locations of type “Other”, coded as “Z” in the HOSPITAL LOCATION file (# 44), will no longer be selectable as locations for new visits. This change was endorsed by the CPRS Clinical Workgroup on Dec 14, 2005. Only locations of type “Clinic” (“C”) will now be selectable.
- Inactive CPT Codes Are Selectable in CPRS when Using Clinical Lexicon to Search for CPT Procedures (Remedy 85748) – A site reported having this occur on more than one procedure. One example is upon searching for code 11441, the user didn’t know the code so “benign” was entered at the search prompt. At that point, the inactive version of that code was the only selectable choice for code 11441. The provider then chose the inactive code and it appeared that the system accepted the code and the provider exited the encounter. The routine ORWPCE was modified to restrict selection of inactive CPT codes to correct this problem.
- Problem with Location for Current Activities (Remedy 92847) – On the visit selection screen, if a clinic with a very long name appeared in the list of clinic appointments, the status of that appointment would not be visible without causing a hover hint to display the full width of the line item. This problem was first reported in CPRS v.23 and has now been corrected.
- Unable to Choose a Printer—No Dialog Box (Remedy 95594) – When users were trying to print Progress Notes and had more than one Windows Printers set up, the notes were automatically printing to the default Windows Printer. They used to be able to choose which Windows Printer they wanted. Resolution: A Windows printer dialog box now executes when File \| Print is selected.
- The Help File Has Been Changed to Show “D - Alert Date/Time” for Sorting Notifications Using the Keyboard (Remedy 70891) – Users who do not use the mouse can sort Notifications in ascending order (alphabetical order or most recent Date/Time) using only the keyboard. When users sort using the Ctrl + \<key\> combination, CPRS will recognize either upper or lower case letters (this feature is not case-sensitive). Users can sort Notifications using a number of Ctrl + \<key\> combinations.
- Corrected Error \<SUBSCRIPT\>LISTN+2^XTER1A that Occurred when RPC ORVAA VAA Was Invoked (Remedy 98025)
- User Cannot Change Font Size in CPRS (Remedy 71244) – Upon setting the font size larger in CPRS, some of the action buttons no longer appeared. This has been corrected.
- JAWS Problem Opening Note from Notification – When processing notifications the user may now press \<Enter\> to process the notification.
- Consult Ordering: Can't Select Service/Specialty when Quick Orders Exist – The arrow keys can now be used to navigate the Consult Dialog Service/Specialty list.

<span id="_Toc133804735" class="anchor"></span>Non-VA Meds

- NON-VA MEDS Missing the Frequency (Remedy 97562) – If a provider enters a NON-VA MED and defines the dose, route, and frequency, then the “pseudo-order” contains all of the parts. Once verified then it becomes active. If a user then views this data on the Meds tab, on Reports tab under the Ad hoc for NON-VA MEDS, or in patient data objects for templates that bring in the active medications, then it has all the parts of the order except the frequency. If a user then views this on the orders tab, it is shown correctly there.
- Non-VA Med Entry Shows Up Initially in the Inpatient Medication Section and then Transfers to the Appropriate Section on the Meds Tab Display after It Has Been Signed (Remedy 70852) – This has confused staff who cancelled their entry and did not enter non VA meds because they appeared to be inpatient meds. This has been corrected.
- Entire Non-VA Med Sig Not Displaying on the Meds Tab – This has been corrected to display the entire Sig.
- Non-VA Meds Cannot Focus on Invisible or Disabled Window – If a user attempted to right-click on the yellow Info box on the Non-VA Meds dialog, CPRS displayed the error: Cannot Focus on Invisible or Disabled Window. Developers have corrected this problem.
- Non-VA Meds PRN Orders Do Not Expand Correctly – If users enter a Non-VA Med order with PRN, the PRN does not expand to read “as needed” in the Sig. field at the bottom of the dialog. Developers corrected this problem.
-   
  Schedule for Non-VA Medication Orders Not Retained when Changing the Order – When changing a Non-VA medication order, the schedule and/or the PRN indication was not retained from the original order. Developers corrected this problem.
- Non-VA Meds Order PRN Indication Not Clearing – If a user was entering Non-VA Medication orders, checked the PRN box, accepted an order, and then began another Non-VA Medication Order, the PRN box stayed checked from one entry to the next. Developers corrected this problem.
- Non-VA Medication Order Drug Selection List Not Scrolling Appropriately – In the Non-VA Medication Order dialog if a user typed a few characters, the list did not scroll so that medications beginning with those letters displayed. For example, if a user entered “asp”, the list should scroll to the medications beginning with “asp” such as aspirin, but it did not. Developers corrected this problem.

<span id="_Toc133804736" class="anchor"></span>Notes/Consults/Discharge Summary/Surgery Tabs

- Default Note Title Note Being Automatically Highlighted – If a TIU default title was assigned to a user and the user started a new note, CPRS did not highlight the default note title for selection. Developers corrected this problem.
- Cosignature Requirement Now Based on Document Date (Remedy 84578) – Developers changed the code so that the evaluation of cosignature requirement is now based on the document date, not the current date. This change will occur after sites install patch TIU\*1.0\*175.
- Removed Additional Signer Still Appearing (Remedy 70686) – If a user was adding additional signers for a document and then removed some of the names from the list before clicking OK, those erroneous entries were sometimes still appearing with the document as additional signers. This occurred for any name in the list that also had a title (e.g., M.D., Pharmacist, HIM, etc.) appended to the name in the left-hand lookup box. This has been corrected.
- List of Unresolved Consults Displays Inappropriately – If a user had a TIU default note title defined that was not in the Consults document class of titles, then the list of unresolved consults that normally displayed when beginning a new note did not display, regardless of the value of the ORWOR SHOW CONSULTS parameter. Developers corrected this problem.
- Title Will Not Resolve Consult Warning – When the user begins a new note and the list of unresolved consults is visible because of a YES setting for parameter ORWOR SHOW CONSULTS, CPRS displays a warning if the user selects any non-consults title that the selected title cannot be used to complete consults. No consult needs to be previously selected from the list for this warning to appear. If the user’s default TIU title is a non-consults title, that title will still be preselected when the form displays, but the above warning will not appear until the user clicks OK.
- Very Easy to Bypass Reason for Request (Remedy 71208) – When ordering a new consult in CPRS v25, unless the user actively clicks on the consult name, under Consult to Service/Specialty, the user can proceed directly to typing in a reason for request, and completely bypass existing prerequisites and templated reason for request. Consequently, consults can be submitted with missing, incomplete, or erroneous information in the reason for request. This has been fixed.
- User Able to Sign Consult Request Without Completing Diagnosis (Remedy 94656) – If a Service name was highlighted (but not selected) and the consult request could be processed without entering a Provisional diagnosis by using the Diagnosis button, even though it’s set to required for that service in the REQUEST SERVICES file (# 123.5).
- Site Not Receiving IFCs (Remedy 71016) – Developers limited the maximum length of the Provisional Diagnosis entry box to 180 characters to match the REQUEST/CONSULTATION file (# 123) data dictionary. The previously unlimited length was causing intermittent messaging problems with interfacility consults (IFCs) if a user exceeded this length. There should be no noticeable impact to most users with this change, which included the ordering and edit/resubmit screens for both consults and procedures.
- Selecting TIU Default Location No Longer Requires Additional Click (Remedy 95758) – Previously, if a user began a new TIU note, had a default TIU location defined, and was required to enter a visit location, the dialog appeared to have the default location selected, but it did not. The dialog required the user to explicitly select the location. Developers corrected this so that the default location is selected by default, and the user can then click or select OK to proceed.
- Cosignature Dialog Problem Addressed – Developers previously corrected a “List Index Out of Bounds” error on the cosigner selection box that occurred if the user exited that box with no text entered. Developers addressed the situation where partial text is entered but no match found.
- Treeview No Longer Expands to Show Addenda During Keyword Search – When a user is doing a keyword search on note subjects or titles from the Custom View menu option, if the only reason for a parent document to be expanded in the left-hand treeview is the fact that its addendum also matches the search criteria, then that parent will NOT be expanded. If the user has the listview above the note text pane open (such as when the user selects the All signed Notes note grouping), addenda will still appear as matching items in that listview.
- Cannot Create Addendum to a Document Requiring Cosigner (Remedy 97133) – If a document required a cosigner based on TIU document parameter settings, and that document also allowed only one note per visit, it was impossible to create an addendum to that type of document. CPRS improperly enforced the “one note per visit” rule from the note title selection screen for addenda. Developers corrected this problem.
- Changes Made to Spelling and Grammar Checking to Correct Problems – When clicking the spelling or grammar check menus, the first thing that happens is a forced silent autosave of the note’s current text prior to passing that text to the MS-Word spell-checker. Developers added an additional automatic autosave of the note text immediately upon return from the spelling and grammar checks on the Notes, Consults, Discharge Summary, and Surgery tabs. This will now occur with no user action. Those autosaves have been enhanced so that the note text will be placed in the “TEXT” nodes of the document in the TIU DOCUMENT file (# 8925), instead of in the edit buffer's “TEMP” nodes. The effect of this change will be that if a spell-check error occurs and the user gets kicked out of CPRS, when the user goes back in and selects that note, the text will be visible and editable automatically, allowing a complete recovery. Depending on the exact code location/timing of the still-unknown spell-check error, the note may or may not include any changes made during the spell-check.
- Notes Tab Consults Addendum Cosignature Issue Corrected – On the Notes tab, if the user were adding an addendum to a consults-titled document that requires cosignature, the addendum will also require cosignature, and the cosigner selection screen will display. Previously, CPRS required the user to select a consult on that screen, and the cosigner box would be hidden behind that consult selection box. Developers corrected both problems. Additionally, if the user cancelled from that screen, the addendum would still be opened for editing. Developers also corrected this problem.
- Unable to Locate Active User (Remedy 98681) – Terminated and disusered users were being excluded from the selection list for Notes by author, as well as in the Notes - custom view and the Problem List Filters screen. The problem was that users, now inactive, may have once written notes or added problems. Since inactive users were being excluded from the selection list, there was no way to do a search of items limited to that author. This has been corrected.
- User Able to Sign Addendum without Identifying Cosigner (Remedy 70528) – Users (residents) could make and sign addenda without specifying a cosigner that would otherwise require a cosigner. Here is how this can happen:
1.  Right click on document or go to action then make addendum.
2.  'ADDENDUM PROPERTIES' pops open and prompts for a cosigner.
3.  The expected cosigner field can be left blank and user clicks on the CANCEL button.
4.  A blank addendum opens and user types in text.
5.  Click on file and SELECT NEW PATIENT and user is then able to sign addendum and not be prompted for a cosigner.
6.  Status of addendum is UNCOSIGED without a cosigner specified.

This has been corrected.

<span id="_Toc133804737" class="anchor"></span>Notifications

- ORMTIME Notifications Not Being Triggered (Remedy 70734) – Developers corrected a problem that occurred when trying to trigger ORMTIME-driven notifications if an order does not contain a specific piece of information (a “3” global node). When an order is being updated due to recent/new activity, this piece of information will not exist in the order. This has been corrected.
- The Package-Level Value for ORWOR EXPIRED ORDERS Did Not Make It into the Post Init for OR\*3\*190 (Remedy 71062) – OR\*3\*215 exports the Package level value for ORWOR EXPIRED ORDERS.  Prior to OR\*3\*215, no value existed at the Package level and the software would search for med orders that have expired. Essentially it would not find any expired orders. If sites have this parameter set at the System level, they should check to ensure that it is set correctly. <span class="mark"></span>
- Experiencing a Very Long Delay when Accessing a Patient's Active Medications (Remedy 70274) – There is a distinct correlation noticed on response time when performing a detailed display on a medication that contains a long medication history. Waits of 1-2 minutes have been the average for processing patient orders within the GUI. CPRS GUI v26 was modified to NOT look back more than 90 days for orders when processing the remote procedure call (RPC) ORWORB KILLUNVER MEDS ALERT. The fix was also extended to RPC ORWORB KILL UNVER ORDERS ALERT that acts similarly. These RPC s are commonly called in the CPRS GUI to clean up related alerts.
- Upon Forwarding Alerts, Sometimes Get RESETUP+4^XQALFWD (Remedy 125632) – This has been fixed; ORB31 was modified to prevent the error.
- Corrected \<UNDEFINED\>DEL+2^ORB3FUP1 Error – This occurred when a user processed the same notification which had been processed by a different user.

<span id="_Toc133804738" class="anchor"></span>Orders

- Drug Message Not Displaying (Remedy 70639) – In an order dialog, if a user clicked the “Change” button to select a new drug, the drug message did not display. This has been corrected.
- Number of Medication Refills Not Calculating Correctly (Remedy 70657) – The CPRS outpatient medication order dialog was not correctly calculating the number of refills for outpatient medications. Developers corrected this problem.
- Flagging an Order Can Cause CPRS to Send Notifications to Incorrect Providers (Remedy 71152) – “FLAGGED ORDER FOR CLARIFICATION” alerts were sent to providers other than those specified by the notification’s Provider Recipient parameter. In the reported instance, the site pharmacist flagged the order to notify the ordering provider of the need to renew the expiring medications. The site had the notification set to go to the ordering provider only. However, additional providers also received the notification. This was caused in the GUI by flagging an order and naming one or more additional recipients for the notification. If the user then flagged another order in the same CPRS session, CPRS did not clear the additional recipients and they received the notification also. This has now been corrected.
- One-Time Schedule Still Appearing when Creating a Complex Inpatient Order – Developers made some changes and CPRS now behaves as follows:
- One-time schedules will not display in the schedule selection drop-down box for inpatient complex orders.
- If the user selects a one-time schedule on the dosage tab and then switches to the complex tab, the schedule field will be blank.
- If the user selects a schedule on the Dosage tab that is not a one-time schedule and then switches to the complex tab, the selected schedule should appear in the Schedule field.
- Date Range for Orders Not Current (Remedy 70202) – If users set the orders view to a date range that goes back 3 months through NOW, showing all orders and all services, CPRS does not always display the most recent orders, regardless of order status. Developers corrected this problem.
- Radiology Ordering Dialog Problem (Remedy 111354) – If users did a “Change” for RAD/VASC/NUC MED orders, the image type/location reverted to blank and the date to today. Developers corrected this problem.
- Incorrect Orderable Item Selected (Remedy 95917) – If a user edited an unreleased order and selected a different orderable item, CPRS incorrectly entered a different orderable item from the one that was selected.
- Two Orderable Dispense Drugs, Only One Message Shows – If there are two dispense drugs under the same orderable item with different messages in the message field, only one of the messages will show in the pop up box in CPRS. This has been fixed so that both messages display.
- Corrected \<UNDEFINED\>RENEW+51^ORWDXR Errors – Developers added code to insure records without a valid order ID will not be sent to routine ORWDBA1.
- Corrected Grammar So Messages Now Read:
- You cannot renew the clinical medication order
- You cannot place inpatient medication orders from a clinic location for selected patient.
- You cannot renew inpatient medication orders from a clinic location for selected patient.
- Removed Any Leading Spaces from Free-Text EnteredSchedule – This was done because the schedule was not expanding to read correctly, but the user was allowed to accept the order.
- Duration Field on Complex Medication Orders No Longer Allows Non Numeric Character Inputs – The warning message reads: “Please use numeric characters only.”
- Change Made to Retain the Last Day-Of-Week when PRN Is Entered Manually – Previously, the last day of the schedule was not retained.
- Auto-Accept IV Quick Orders Stop Time Now Calculated Based On Rate And Duration – Previously the stop time defaulted to the package/ward stop date/time.
- Unreleased Orders Will Not Require a DC reason – Previously these orders required a Discontinue reason.
- Quick Outpatient Med Order Without a Route No Longer Defaults to First Route on Drop-Down List – For the order to be accepted, the user must explicitly enter a route.
- Corrected Access Violation upon CPRS Timeout when Viewing Order Details
- Message Added to Medication Order Dialog – On the Medication Order dialog’s Complex tab, developers added a warning message to tell users that if they switch from the Complex tab to the Dosage (simple) tab, they will lose their current data. This message dialog gives the user the choice of choosing OK to switch to the Dosage tab and lose the data or choosing Cancel to remain on the Complex tab and retain the items already entered.
- Generic Text Quick Orders Not Displaying Under Clinic Orders – Developers corrected a problem with Generic Text Quick Orders not showing under Clinic Orders when placed from an IMO location.
- Inpatient Medication Orders with PRN Cancel Due to Invalid Schedule (Remedy 94417) – If a user entered a medication order with PRN and then cleared the schedule field by pressing the \<Space Bar\>, CPRS displayed an error message but would allow the user to continue and receive additional errors. Developers changed CPRS to not accept spaces at the beginning of a schedule.
- Infusion Rate Field Check Added – Developers added a check to the Infusion Rate field in the IV order dialog form to validate that the value entered in the Infusion Rate field is in one of the following formats “NNNN.NN or text@labels per day”
- Warning on Complex Order Tab Changed – Developers changed the warning message that CPRS displays when a user attempts to switch between the Complex and the Dosage tab. Developers also changed the code so that this warning message only appears if something is in one of the following fields: Dosage, Schedule, Duration, or Sequence.
- Medication Selection List Problem Corrected(Remedy 95302, 96342) – Developers corrected an UNDEFINED FVSUB^ORWUL error that occurred when the last entry in the list is selected or when a user types in first few letters of the name of the drug that is the last entry on the list.
- Dietetics Dialog Changed to Use ML Not CC – Developers altered the Dietetics tubefeeding order dialog to use “ml” rather than “cc”. Although the two units reflect the same measurement, “cc” is included on JCAHO’s list of unapproved abbreviations.
- Imaging Order Fields Incorrectly Reverting to Defaults When Changing the Order – When a user edited (changed) an existing imaging order, several fields were reverting to the defaults when opening the dialog, rather than correctly populating with the contents of the order being edited. This was a problem because the user should not be able to change the imaging type although the user can change the other fields. This was an inconsistency between CPRS List Manager and GUI code that has been present for a very long time. Developers corrected this problem: the fields will now be as they were in the original order and all fields except the imaging type can be changed.
- Disable Encounter Location Changes while in Order Dialogs – Previously, a user could begin writing orders and with the order dialog still open, select the Encounter button and change the encounter location. Because the order dialog did not update based on the changed location, the orders could be assigned to the wrong location or might even display medications that were not appropriate for that location. Developers made a change so that users will not be able to access the Encounter button next to the patient name while in the following order dialogs: Inpatient/Outpatient medications orders, Non-VA Medications, IVM medications, Laboratory, Radiology, Consults, Procedures, and Vital order dialogs. When the user closes the order dialog, the user can use the Encounter button to change the encounter location.
- PRN Being Dropped When Changing Simple Outpatient Medication Order To Complex – If a user entered a simple outpatient medication order and selected PRN as part of the schedule and then changed from the Dosage tab to the Complex tab, CPRS did not carry the PRN designation into the complex order. Developers changed CPRS to retain the PRN in this situation.
- “Non-Standard” Schedules Now Appropriately Designated as “Day-of-Week” Schedules – Because of possible confusion due to the wording in CPRS, developers changed the wording of “non-standard” schedule to “Day-of-Week” schedule. The change was made on the order dialog that has the Schedule Builder link.
- Schedule Builder Button To Select Everyday Added – Developers added an Everyday button to the Day of Week Schedule Builder dialog. When the user selects this button, all days of the week are checked.
- Day-of-Week Schedule Builder Does Not Accept Free-Text – Users cannot type text directly into the information box at the bottom of the Day-Of-Week schedule builder. Developers changed this so that users would not attempt to enter text only to have CPRS reject the schedule when it attempted to validate the schedule. Users must use the checkboxes, time columns, and the Add and Remove buttons to enter the appropriate day of the week and the time. Developers added hover hints to the buttons.
- Admin Time Only Schedule Are No Longer Allowed in CPRS(E3R 19324) – Previously, users could enter Admin time only schedule. If the user attempts this, CPRS displays a dialog stating that this is not allowed. The user will not be able to accept a schedule until a day of the week is selected.
- Clinic Meds Display Group for IMO Orders Changed to Clinic Orders – Developers changed the label of the Clinic Meds display group to Clinic Orders to better reflect orders written from IMO locations.
- IMO Orders Can Now Be Printed in the Clinic Location – Previously, for IMO orders, if a provider selected the “Clinic” Location as where a medication should be administered, there was no way to print the order in the clinic location. Developers changed the CPRS so that if the provider selects ‘No’ when asked “Should the orders be printed using the new location?”, the Orders will be printed at the Clinic. Otherwise, the orders will print at the Ward.
- Change to Auto-Calculation in the Dosage and Days Supply Fields (Remedy 107184) – There was a problem when the user copied to a new order or changed an order. When loading the order dialog for editing, CPRS would make an initial call to calculate the days supply and quantity fields. A problem could occur with a drug that did not have a possible dosage. Developers made a change to prevent these fields from being calculated when the dialog was loaded. If the user changes any of the fields that would affect the order, such as Dosage, Schedule, or Duration, CPRS will recalculate the Day Supply and/or the Quantity field each time one of these fields is changed.
- Changed The Conjunction Box Warning Message

From:

A duration is required when using “Then” as a conjunction.

To:

A duration is required when using “Then” as a conjunction. The patient will be instructed to take these doses consecutively, not concurrently.

- Order-Level Locking Corrected (Remedy 113212) – On the Meds tab, CPRS was not performing an order-level lock check when changing an order. Without the lock, it was possible for a user to change a pending order at the same time a pharmacist was finishing the order. Developers corrected this problem.
- Radiology Order Dialog Displaying Inactive Radiologists – CPRS was displaying inactive radiologists in the Approving Radiologists list. Developers changed CPRS to filter the approving radiologist list by inactive date.
- IV Order Spelling Correction – Developers changed the misspelled word “Strenth” to “Strength”.
- TIU Objects May be Used in Generic Text Orders (Remedy 123303, E3R 18901) – The text should wrap correctly in the ORDER TEXT field in the detailed display of these text orders.
- Dosage Not Correctly Interpreted when Finishing Order from a Quick Order (Remedy 87476) –When placing a quick order for a complex inpatient medication order, the incorrect Unit Dose for the medication was appearing in the Pharmacy screen when the Pharmacist was completing the order. This has been fixed.
- PRN Quick Orders Not Working (Remedy 94396) – Inpatient and outpatient quick orders with schedules such as Q4H-PRN were not working properly, causing the clinician to reselect the schedule from the drop-down list. The dialogs were displaying Q4H- in the schedule field and the PRN box is checked. If the clinician clicks on Accept the following message is presented: “This order cannot be saved for the following reason(s): Unable to resolve non-standard schedule”. Developers corrected this problem.
- Service Connection Prompt Not Being Answered in CPRS (Remedy 129246) – The problem was the inconsistent appearance of a service connection (SC) prompt in CPRS and the pharmacy package. The problem occurred when a signed medication order was changed, causing the SC to be dropped from signature form. This was resolved by changing the code to call the new CoPay RPC, which is the same RPC being used by CIDC.

<span id="_Toc133804739" class="anchor"></span>Order Checks

- User Can Now Press \<Enter\> After Entering a Reason for Overriding an Order Check – If a user got an order check, decided to override the order check, and entered a reason for override, the user was required to click the Submit button or tab to the Submit button and press \<Enter\>. Developers have made a change the enables the user to press \<Enter\> immediately after typing the reason, and the \<Enter\> will by default be the same as using the Submit button.

<span id="_Toc133804740" class="anchor"></span>Orders—Delayed

- Treating Specialty Selection Error Corrected (Remedy 95330) – If a user edited a delayed order that contained the prompt OR GTX TREATING SPECIALTY, and if the release event involved had specific treating specialties assigned, then if a user typed in the treating specialty combo box, CPRS would clear the selection list, leaving it empty. The user then could not select a treating specialty. Developers corrected this problem.
- Delayed Diet Orders Incorrectly Prompting for Late Tray (Remedy 93955) – For delayed release diet orders, because the start date is unknown at the time of ordering, CPRS should never prompt the user for a late tray. Developers corrected this problem.

<span id="_Toc133804741" class="anchor"></span>Order Signature

- Access Violation When Signing Orders – When the user either selected orders and then the Action/Sign menu, or when the user caused the Review/Sign changes screen to appear, an access violation frequently occurred. Developers corrected the problem.
- Some Discontinued Orders Now Require a Signature – Following direction from the CPRS Clinical Workgroup and to help resolve PSI-04-063, developers changed CPRS to require a signature for orders that have been discontinued in CPRS. All discontinued orders that require a reason for discontinuing will now require a signature.

<span id="_Toc133804742" class="anchor"></span>Order Signature (Digital)/PKI

CPRS Inappropriately Requiring Digital Signature Card(Remedy 70928) – If clinicians were using the PKI digital signature feature, CPRS was requiring them to insert their card when the order was not being signed, such as when a note but not the order was being signed, when closing CPRS and choosing “Don’t Sign”, and when changing a patient and choosing “Don’t Sign”. Developers have corrected this problem.

<span id="_Toc133804743" class="anchor"></span>Parameters

- Incorrect Parameter Description (Remedy 69506) – Previously, the parameter description referenced the wrong parameter for individual time and occurrence settings. In the last part of the description ORWRP TIME/OCC LIMITS ALL has been changed to ORWRP TIME/OCC LIMITS INDV.
- Parameter to Control Remote Data Views Access to the HDR – CPRS developers created a new parameter ORWRP HDR ON that controls whether a site will query the HDR for remote data. This parameter will be OFF when exported, so that sites will not be querying the HDR.

> **WARNING:** Sites should not enable this parameter until they receive official instructions. There is the possibility that inaccurate or misaligned data could be displayed in CPRS. A future patch will either provide instructions or activate the ORWRP HDR ON parameter.

<span id="_Toc133804744" class="anchor"></span>Patient Information Bar

Problems with Sizing, Scroll Bars, and Difficult Navigation to Information – If the size of the CPRS window was changed, there were some concerns that not all information from the buttons on the Patient Information bar would be visible or easily found. One method of addressing this problem was to add items to the View Menu. The View menu now has a submenu, “Information” that contains actions to all buttons (Patient Inquiry, Flag, Reminder, etc.) on the Patient Information bar. When the width of the CPRS form is small or font size large, some buttons may be overlaid and not accessible, users can use this menu to access any button.

<span id="_Toc133804745" class="anchor"></span>Patient Inquiry (Demographics)

- Patient Inquiry Button Information Slowly Disappears (Remedy 70321) – CPRS users would occasionally experience a problem with the patient name and social security number (SSN) disappearing from the Patient Inquiry button. This has been corrected.
- New API Call for Insurance Information in Demographics – Because an existing API call that returns patient insurance information for display will soon be retired, developers added a new call to return this same information in the patient demographics screen. Users should not notice a difference in the information returned.

<span id="_Toc133804746" class="anchor"></span>Problems Tab

Problems Tab Message Clarified – If a user were adding or editing a problem on the Problems tab, navigated to another tab in the chart, and then attempted to close CPRS, CPRS displays a message asking the user to confirm “Discard Changes (yes/no)”. However, the message did not indicate that it related to the problem being entered or edited. Developers clarified the message box to direct the user to the Problems tab.

<span id="_Toc133804747" class="anchor"></span>Reminders

- Date/Time for Vitals Entry through Reminders Changed (Remedy 70610) – Developers changed the Reminder dialog to use the Default Date/Time of NOW instead of the encounter date/time when entering vitals through a reminder dialog.
- Prompt Changed for Skin Reading (Remedy 70631) – Previously, the number selector for Skin Reading had values from zero to ten. However, clinicians had different interpretation of what zero meant than developers did. Developers changed the Reminder dialog’s Skin Reading prompt to a combo box to allow for a null value—meaning that the test had not been read—and a zero meaning the test had been read and it was negative. The correct value can then be stored in the note.
- Reminder Dialog Branching Logic Not Working When Editing a Dialog That Is Already on the Coversheet and/or If The Dialog Is in the Other Categories FolderNote: For information on branching logic, see the *Clinical Reminder Manager’s Manual* on the VistA Documentation Library (VDL).

Developers corrected two problems with the branching logic:

- The branching logic was not working when adding branching logic to a dialog that is already defined on the coversheet and CPRS is open. The branching logic would not work unless the reminder is removed from the coversheet or CPRS is restarted.
- Branching logic was not working for Reminder Dialogs that are defined only in the Other Categories folders.

Developers changed the M dialog loader code so that it passes the patient-specific flag when the dialog is loaded into CPRS. This change associates the patient-specific flag with the dialog itself and not the reminder. This fix also resolves the problem with dialogs in the Other Categories folder not working with branching logic. If adding branching logic to a dialog that is already on the coversheet and CPRS is open, the Refresh Reminder Dialog button will cause CPRS to reload the dialog and the patient-specific flag will be passed up at that time.

- Disappearing Splitter Bar Corrected (Remedy 69801) – If a user expanded the text box over the buttons on the Reminder dialog with the splitter bar and left it that way, the splitter bar became inaccessible and the user could not get back to the buttons. This has been corrected and the splitter bar now remains accessible.
- Hospital Location Error (Remedy 71112) – Users were receiving an “ERROR:HOSPITAL LOCATION Missing is not in file 44 Value:0” error. This error occurs when the following steps are taken:
1.  Start a new note.
2.  Enter a vital through a reminder dialog and finish the dialog.
3.  Save the note without signature.
4.  Sign-out and sign back into CPRS.
5.  Do not select a location.
6.  Edited the previous note.
7.  Re-enter vital data through a reminder dialog and finish the dialog. The error will occur here because the vital entry does not have a location to say where the vital was taken.

The fix for this problem is to default the Hospital locations to the location of the note if a location is not selected for the user.

- Support for Future Mental Health Patch – Developers added code to handle the new Mental Health test format that will be released with YS\*5.01\*85. The changes make CPRS backward-compatible—able to handle both formats.

<span id="_Toc133804748" class="anchor"></span>Remote Data Views

Remote Data View Site Tabs Changed to Buttons to Visually Distinguish Which Tab Is Selected – When using Remote Data Views (RDV), the user might find it difficult to determine which tab was selected. To address this issue, developers changed the tabs to buttons so that it is easier to distinguish which site’s data the user is viewing.

<span id="_Toc133804749" class="anchor"></span>Reports/Health Summary

- Inappropriate Text Displaying on Health Summary Ad Hoc Subdialog – If the user were creating an Ad Hoc Health Summary, one of the subitem menus from which the user would select had some inappropriate characters (letters) displaying by the up and down arrow buttons. Developers corrected this.
- Additional Vitals Measurements Added to CPRS Reports – Developers modified Vitals Reports on the Reports tab to include pain, central venous pressure (CVP), Pulse Oximetry (P Ox%), and Circumference/ Girth (C/G).
-   
  Changes Related to the Health Data Repository (HDR) – A number of changes have been implemented to support HDR. HDR reports will not be available until the HDR is online. It is being noted here so that sites are aware that there have been changes added in support of HDR. These changes should not have any impact on the Reports Tab. The following components are being added with this version:
- Routine: ORWRP4 (new) ORWRP3, ORDV04 (changed)
- RPC: ORWRP4 HDR MODIFY
- Fields added to The OE/RR REPORT file (# 101.24)
- .45 HDR REPORT
- .46 HDR ROUTINE
- .47 HDR ENTRY POINT
- 1 (under Columns multiple) HDR MODIFIER

<span id="_Toc133804750" class="anchor"></span>Section 508, Resizing, and Font Issues

- Resizing Issue Corrected (Remedy 70573) – Developers increased the size of IV Fluid Order dialog to prevent the Additives tab from overlapping the additives text field.
- IV Fluid Order Dialog Missing Text – On the IV Fluid Order dialog at the top of the upper left panel, there is a blank field of normal size before the additives are inserted. After the additives are inserted, this field is reduced in size so that the top half of the text is missing making it very difficult to read. Developers corrected this problem.
- Focus Problem Involving Multiple Dialogs Fixed – If a user had a child window open and switched focus to the window behind it, the user could not get the focus back to the original child window using a keystroke. Now ALT+F1 puts the focus back to the topmost child window.
- Dialog Size Retention – If a user changes the size of the following dialogs and closes the dialog, CPRS stores the size and displays the dialog at the same size the next time it is opened.
- Problems Details dialog on the Cover Sheet
- Medication Details dialog on the Meds tab
- Select Lab Test by Date dialog on the Labs tab
- Discharge Summaries Properties Dialog on the D/C Summ tab
- Encounter Form (Remedy 70365)
- Consult order dialog
- Procedure order dialog
- Button Problem and Size Retention Corrected – Developers corrected problems with the display of buttons at different font sizes for the following dialogs:
- 'Print Setup' Dialog(Remedy 70367) – The OK and Cancel buttons now display properly in font sizes greater than 8. The size of the dialog is saved from session to session.
- Template Dialog (Remedy 70233) – When a user selects a font preference larger than 8, templates no longer pull up with the Preview, OK and Cancel buttons on top of each other. Also, when the template is resized, the size is saved.
- Duplicate Order Checks Dialog (Remedy 70541) – The Continue and Cancel Selected Orders buttons will no longer be chopped off with any font greater than 8 pt. Now this Dialog will also save its size, from use to use.
-   
  Details Dialog – Developers adjusted the Details window properties so that the Print and Close buttons can be accessed at all font sizes. The following were affected: Active Problems, Active Meds, Recent Labs, Appointment/Visits/Admissions when a note is opened, Crisis/Warning notes/directives, problem on Problem tab, Med on Meds tab, order on Orders tab.
- Renew Orders Dialog Display Issues – If a user changed fonts, some display problems could occur, such as column headers not displaying correctly, one pane displaying too large, buttons not displaying, or information being off the dialog and no scroll bars appearing so that the user could get to the information. The issues have been corrected.
- Current Activities Dialog – Developers made changes so that this dialog worked with large fonts, such as 24 points.
- New Procedure and New Consult Dialog – Developers made changes to ensure that these dialogs worked correctly at all available font sizes.
- Consults Text “Hiding” behind the Treeview Button – Developers corrected this problem.
- Button Display Problem on Location for Current Activities Window – When the user opened the Location for Current Activities window, the OK and Cancel buttons were not always visible. The user could not resize the window to make CPRS display the buttons nor did changing the font size help.
- Height of Templates Drawer Not Saved on Surgery Tab – Developers corrected this problem. CPRS now saves the height of the Surgery tab’s Templates drawer between sessions.
- Non-Formulary Options Dialog Buttons and Size Retention Problems Resolved – The buttons on this dialog are now visible at larger font sizes. The form also remembers its size. The position will be centered on CPRS main form.
- Meds Pane Resizing Could Cause Problems – It was possible for the user to resize the panes on the Meds tab and make it difficult to then resize them again. Developers fixed this problem.
- Meds Tab Columns Can Be Dragged Off the Screen ­– Users could reposition the columns on the Meds tab off the screen, confusing users who might not see the expected columns. Developers added code for all three headers so that users cannot drag them out of sight, off the display area.
- Order Procedure Dialog 508 Problem Corrected – When displayed in size 10 fonts, CPRS no longer truncates the word “Inpatient” under the “patient will be seen as:” group box of the New Procedure dialog.
- Patient Selection List Repeated Names – If a user scrolled down to the bottom of some selection lists, patient or clinic names might be repeated at the bottom of the list. Developers corrected this problem.
- Non-VA Meds Column Resizing Problem Corrected – If users resized the Non-VA Medications pane on the Meds Tab, the column headers resized correctly, but the same columns in the medication rows do not resize appropriately; they remained where they were. Developers corrected this problem.
- Provider and Location Box for Current Activities – The provider list will now default to a larger display and will also enlarge as the form is enlarged.
-   
  Reason for Request Field Hidden at Higher Font Sizes – The Reason for Request field on the Consults dialog is now visible at higher font sizes. Please note that if all the components cannot fit on the dialog because of its size, CPRS will display vertical and horizontal scroll bars.
- Insufficient Room on the Outpatient Medication Renewal Form – Previously, the bottom line of refills/pickup was cut off; there was not enough room for the complete order. If the user adjusted the size of the dialog, CPRS did not store the new size between sessions. CPRS now stores the size.
- Sizing Problems with the Orders, Meds, Problems Tabs Tables – The tables (or grids) on these tabs have a feature to keep columns visible. When expanded, they “snap” back to their width when the length of the title bar exceeds the tables’ width. When changing fonts or widening the form width of CPRS, it is possible to have the title bar exceeding its intended length making it difficult to resize the columns. Developers added a change to CPRS so that users can always make the width of the column smaller, regardless of the title bar length. You can also click any of the title bar buttons (or column headers) to “autosize” the field widths to an optimal width, which makes all of the columns fit in the window. The autosize also occurs when changing fonts. This avoids the need for horizontal scrolling of the table.
- Outpatient Meds Dialog Size Too Small – Previously, for the renewal of outpatient medications, the outpatient medications dialog box initially opened too small. Developer corrected this problem. The dialog will initially open larger.
- Renew Medication Order Text Cut Off – The Renew medication order text displayed on the button and the header were being cut off. Developers added a change so that the buttons and header will no longer shrink below a minimum size.
- Resolved “Cannot focus...” then “List out of bounds” Errors – This correction affects both inpatient and outpatient medication order dialogs. If a new order is placed, and then the provider decides to make a change in the route, and uses the \<Enter\> key to accept the order, the following error displays: Cannot focus a disabled window or invisible window. After closing the error, the change of the route is entered, but when the provider tries to sign the order, sometimes a “List out of bounds” error displays. The “Cannot focus…” error was also occurring on orders without a route or dosage.

<span id="_Toc133804751" class="anchor"></span>Sign-On

Problem with CPRS “Hanging” If User Does Not Have the CPRS GUI Chart Option (Remedy 70567) – If a user did not have access to the option OR CPRS GUI CHART, CPRS displayed an error message saying “Application context could not be created!” when the user tried to launch CPRS. When the user clicked OK, CPRS would hang instead of closing. This has been corrected.