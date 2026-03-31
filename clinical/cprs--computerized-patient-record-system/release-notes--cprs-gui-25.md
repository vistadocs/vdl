---
consolidated_title: "release notes cprs gui 25"
app_code: CPRS
doc_type: RN
master_source: "OR*3*195 Release Notes CPRS GUI 25"
master_pub_date: revision_count: 0
consolidated_from: 3 versions
prior_versions:
  - "OR*3*231 Release Notes CPRS GUI 25"
  - "OR*3*235 Release Notes CPRS GUI 25"
---

<span class="smallcaps">Release Notes</span><span class="smallcaps">for</span><span class="smallcaps">CPRS GUI version 25</span><span class="smallcaps">Patch OR\*3.0\*195</span>

<span class="smallcaps">Installation Requirements</span>

The following section gives you the required patches for OR\*3.0\*195 and the order in which they should be installed.

Required Patches

Before you can install OR\*3.0\*195, you must install the following patches:

- IBD\*3\*51
- ICD\*18\*6
- ICPT\*6\*14
- LEX\*2\*25
- OR\*3\*183
- OR\*3\*186
- OR\*3\*190
- OR\*3\*213
- ORRC\*1\*1
- PSJ\*5\*111
- TIU\*1\*178
- TIU\*1\*179
- XU\*8\*330
- XU\*8\*352
- XWB\*1.1\*35

> **NOTE:** Clinical Indicators Data Capture (CIDC) functionality requires several additional patches. Allergy features also require two additional patches AFTER OR\*3.0\*195: OR\*3.0\*216 and GMRA\*4.0\*21.

> **NOTE:** CPRS GUI version 25 requires Internet Explorer 4.0 (IE4) or later. However, PKI functionality requires IE 5.5 or later with 128-bit encryption.

Installation Instructions

CPRS GUI version 25 consists of three patches. The patches are combined in host file OR_30_195_PSJ_PSS.KID in order to simplify installation at Veterans Health Administration (VHA) facilities. Installation of this host file should be coordinated among the three packages affected since only one installation is necessary. The patches are:

- PSS\*1\*59 PHARMACY DATA MANAGEMENT
- PSJ\*5\*111 INPATIENT MEDICATIONS
- OR\*3\*195 ORDER ENTRY/RESULTS REPORTING

Please review the Installation Instructions/Release Notes for each of the patches, PSJ\*1\*59, PSJ\*5\*111, and OR\*3\*195, before installing OR_30_195_PSJ_PSS.KID.WARNING: PSJ\*5\*111 contains routines that may overwrite Class III modifications for Omnicell, Pyxis and McKesson, among others.

> **NOTE:** IMO features will not be available in the CPRS until patch SD\*5.3\*285 is installed in your account. This patch is currently under development.

Please see patch OR\*3.0\*195 for detailed instructions on the installation and post-installation steps necessary to install this software.

Known Issues

Listed below are eight known issues identified with the release of OR\*3\*195. Per Executive Directive Memorandum “Software Release with Known Defect Reporting,” the following information regarding each known issue is provided below: the defect/issue, risks/impacts, and workarounds (alternative methods to do the job).

The justification for release with these eight defects/issues is as follows:

The release of CPRS will support many interdependent projects, these include but are not limited to Inpatient Meds for Outpatients, Non Standard Schedules, Clinical Indicators/Data Capture as well as resolving many patient safety issues some of which are over a year old and are related to the Allergy Adverse Reaction enhancements contained in this release. There are also over 100 NOIS calls resolved by this release. Additional delays in releasing CPRS v25 will put the release of CPRS v26 in jeopardy. Most of the defects are minor inconveniences and the high level ones identified by the test sites are listed in the release notes and patch description message. HSD&D has received concurrence from Cynthia Kindred, ADD for Health Data Systems and Martha Gerard, QA manager for Health Data Systems.

Issue 1: Any CPRS User Can Mark an Allergy as “Entered In Error” or Add a New Allergy

Defect/Issue – Risk/Impact: When patches OR\*3\*195, GMRA\*4.0\*21, and OR\*3\*216 have been installed, users will be able to add a new allergy as well as marking an existing allergy as "entered in error" directly from the Cover Sheet. CPRS GUI v25 does not restrict which users can perform these actions.

Workarounds: None

Resolution: This issue is scheduled to be resolved in CPRS GUI v.26 (OR\*3\*215). A parameter will be added that will control who can use the “entered in error” option from the Cover Sheet and the Orders tab (to be consistent). The ability to add a new allergy or to mark the patient as NKA will not be restricted.

Issue 2: "Duration or Total Volume" Overrides IV Room Site Parameter

Defect/Issue – Risk/Impact: PSI-03-060 "IV Fluid Dialog" has been addressed in CPRS GUI v25 by adding a new field "Duration or Total Volume" to the IV dialog per the CPRS Clinical Workgroup recommendation. By using this field, a provider can specify duration (length) or total volume for the IV order. This new field when utilized as a duration, however, will override the IV Room site parameter LVP'S GOOD FOR HOW MANY DAYS.

Workarounds:

- When pharmacists are finishing the order, if they see an IV order written with a duration, closely review to make sure it’s appropriate.
- Advise providers to not use the duration field unless they want to override the IV policies.

Resolution: PSJ\*5\*113 partially addresses this issue in that the stop date calculation for IV orders will be modified to treat "Duration or Total Volume" the same as all other stop date parameters that exist (it will no longer override the default). CPRS Clinical Workgroup input is still necessary to discuss the issue of there being no limit to the new field.

Issue 3: Prohibition against Ordering Inpatient Medications for an Inpatient from an Outpatient Location

Defect/Issue – Risk/Impact: With CPRS v.25, some concerns about ordering inpatient medications from outpatient locations have come up. One possible scenario was as follows:

> It is not unusual that a very sick patient would be quickly admitted to an ICU bed without the patient’s encounter, note, or all admission orders being completed.  Thus, the situation described below could happen again.

> 1.       Patient is checked in to the outpatient Urgent Care clinic.

> 2.       Patient is admitted to an inpatient ward/unit.

> 3.       While the patient has an inpatient status, the provider opens the patient's chart to complete the UCC Encounter. In doing so, he used the "File ---\> Update Provider/Location" option to change the location back to the "Urgent Care".

> 4.       When finished with the encounter, the provider (leaving the patient's location as "Urgent Care") proceeded with entering other orders (including inpatient meds) intended for the inpatient unit/ward. The system allowed the provider to sign those orders. The orders displayed in the appropriate display group in CPRS.

> 5.       However, the inpatient med orders (both unit dose and IV orders) did not appear in BCMA.

As a result, the CPRS Clinical Workgroup endorsed the decision to prohibit ordering of inpatient medications for inpatient from outpatient locations because of possible patient safety issues. The resolution to this question is as follows:

Workarounds: None

Resolution: The short-term resolution to this issue has been implemented in CPRS GUI v.25 and is as follows: If the user attempts to order inpatient medications for an inpatient from an outpatient location, CPRS should discontinue the order process and return the user to original Orders or Meds tab display.

The long-term resolution to this issue includes both Pharmacy and CPRS changes. The CPRS component is scheduled for CPRS GUI v.26 (OR\*3\*215). PSJ\*5\*112 and PSS\*1\*86 are the Pharmacy components necessary to allow sites more freedom with the IMO clinics. Changes include:

- Auto-dc of IMO orders on admission and discharge will be on a clinic basis.
- Seeing the orders in BCMA will also be done on a clinic basis.

Issue 4: Remote Data Views Retrieval of Discharge Summary from Sites with Different Versions of CPRS Can Cause Missing Text

Defect/Issue – Risk/Impact: The Code Text Descriptor project determined that ICD codes and associated diagnosis information should not display in the detailed information of the Discharge Summary report format. Developers made this change, which made the v.25 report different from the v.24 report. Because the reports are different, if users at a site running one version of CPRS request a Clinical Reports Discharge Summary from a site running a different version of CPRS through Remote Data Views, the report may be missing some text or may not display correctly as described below:

- When a v.24 site user requests a discharge summary from a v.25 site, the \[+\] column will not indicate that there is detailed information available. The other main columns will be correct as the majority of the columns were undisturbed. When the user clicks on an entry, the details will display in the lower pane. The top-most information related to who entered it and when will be correct. Also, the detail pane will display "DIAGNOSIS:" but there will not be any data.
- When a v.25 site user requests a discharge summary from a v.24 site, CPRS displays the following informational box and the request will not be completed: “Programmer message: One or more column ID’s in file 101.24 do not match ID’s coded in extract routine”.

Workarounds: None

Resolution: This discrepancy between reports occurs only when the sites involved are running different versions of CPRS: v.25 and a previous version of CPRS. If both sites are running the same version of CPRS, the problem does not occur. When all sites have installed CPRS GUI v.25, the report formats will match and this will no longer be an issue.

Issue 5: CIDC-related Record Locking Causes Undefined Error

Defect/Issue – Risk/Impact: This error has only been reported by two of the four test sites that have installed both CPRS GUI v.25 (OR\*3.0\*195) and CIDC and have enabled CIDC. When users are placing orders, very infrequently an invalid order IEN is stored in the second node of ^OR(100, resulting in orders being locked on the users at the ancillary level and an undefined error occurring in routine ORWDXR.

Workarounds: To address this problem, CPRS developers created a fix for sites with CIDC currently in their accounts that prevents these invalid IENs from being stored in their ORDERS file, ^OR(100). Enterprise VistA Support (EVS) has the fix and can assist sites that are experiencing this problem.

Resolution: The same fix identified as a workaround will be in patch OR\*3\*229. This prevents the order locking problem. Site testing for OR\*3\*229 is expected to begin on January 27, 2005, with a release to follow shortly after OR\*3\*195. CPRS GUI v.26 will also include an additional Delphi fix which prevents the sending of an invalid IEN.

Issue 6: New Allergy Dialog Does Not Launch Directly from Reminder Dialogs

Defect/Issue – Risk/Impact: With the new Allergy functionality, allergies are no longer entered as orders but are entered directly into the Allergy package. To make these changes, developers created a new dialog that is installed with the new Allergy functionality (using patches OR\*3.0\*195, GMRA\*4.0\*21, and OR\*3.0\*216). After these patches are installed, any Reminder dialog that contains GMRAOR ALLERGY ENTER/EDIT as a finding item will NOT bring up the allergy dialog when the user clicks the Finish button.

Workarounds: San Diego, one of the test sites for OR\*3\*195, discovered this problem and offered the following workaround:

Instead of embedding the allergy dialog directly into the Clinical Reminder, San Diego placed it on an order menu and then embedded the order menu into the reminder. The result is one extra click for the user, but the dialog then works as it should.

Resolution: This issue is scheduled to be resolved in CPRS GUI v.26 (OR\*3\*215).

Issue 7: Free-Text Entry Could Cause Incorrect Dosage

Defect/Issue – Risk/Impact: PSI-05-004 - This problem could occur when a user is writing medication orders: simple and complex inpatient orders, simple and complex outpatient orders, or non-VA medications. When a dosage was already entered by the user or by a quick order and the user clicks in the field to edit the dosage rather than selecting a different dosage from the available list, the highlighted dosage is replaced by the first character of the new dosage, but then the cursor incorrectly moves back to the left and types over that character when the user types additional numbers. For example, if a quick order contained a dosage of 75MG and the user attempted to change to 25MG, the user would highlight the dosage if necessary, type the 2, which would appear, but the cursor would then incorrectly move back to the far left and replace the 2 with a 5 when the user typed the 5. This would create a dosage of 5MG instead of the intended 25MG. The cursor movement occurs with the first character only. This problem is scheduled to be resolved in CPRS GUI v.26 (OR\*3\*215).

Workarounds: To mitigate this problem in the interim, if users choose to edit the dosage, they should choose from the list of available dosages.

Other suggestions to avoid this problem include

- Sites can help their providers by creating quick orders with common dosages so that providers can choose an appropriate quick order and will not have to edit the dosage manually.
- Sites can try to ensure that sufficient dosages are available in the drop-down list so that providers can select the dosage rather than manually editing it.
- Instruct providers to use \<Delete\> key on keyboard rather than \<Backspace\> key to clear the dosage field. The cursor placement problem does not occur when the \<Delete\> key is used. Thus, manual entry of the order will not be affected by incorrect cursor position.

Resolution: This problem is scheduled to be resolved in CPRS GUI v.26 (OR\*3\*215).

Issue 8: Typing Service Name Can Prevent Entry of Prerequisites and Templated Reason for Request

When ordering a consult, if a user types the service name followed by the Tab key, or clicks in any other field, the user will bypass the fields for Prerequisites and templated Reason for Request. This may result in submitted consults with missing, incomplete, or erroneous information in those fields.

Workarounds: Instruct users to select the service name from the displayed list or type the service name followed by the Enter key. These actions will ensure that the Prerequisites and templated Reason for Request fields display for entry.

Resolution: To be decided.

ADDITIONAL ISSUES

During the testing of CPRS GUI v.25 (OR\*3.0\*195), internal Software Quality Assurance (SQA) and the test sites discovered additional issues that were not resolved in OR\*3.0\*195. A document listing these issues is available upon patch release on the CPRS page: [<u>http://vista.med.va.gov/cprs/</u>](http://vista.med.va.gov/cprs/)

Patient Safety Issues

- PSI-03-036 Event Delayed Orders Status Issues (MOU-0803-30190, ISL-0903-50918) - Developers addressed a problem with locking event-delayed orders that allowed users to act on orders in close succession and could create two of the same order with statuses, such as discontinued and active. Additional locks have been added to prevent this from happening. See also PSI-04-010.
- PSI-03-051 Remote Data Views User Names Inappropriately Displaying in CPRS Selection Lists (NOIS TOM-0503-41438, BRX-1003-11098, LEX-0302-40449) – Because they were users on the system, CPRS displayed providers in selection lists (such as consults, consigners, etc.) that belonged to other facilities and used Remote Data Views. Some users would select the incorrect non-local provider and the local provider would not receive important information. This has been corrected.
- PSI-03-059Problem with CPRS Dosage Matching (NOIS CPH-1203-42234) - This issue arose when a provider typed a value in the Medication Order dialog’s Dosage field and accepted the default selection without checking to ensure that it was correct. Developers have changed the way CPRS matches what users type, making it much more difficult for users to select the wrong dosage. Unless the dosages users want are not listed in the Dosage pane, it may now be as quick for users to select a dosage from the list using their mouse (or tab and arrow keys) as it is to select the default dosage that CPRS displays in the Dosage field. Users must now type more characters (numbers, letters, spaces, and decimal points) to highlight an appropriate dosage in the list. Users may continue to type free-text dosages.
- PSI-03-060 New IV Fluid Duration or Total Volume Field Added (HIN-1203-42283) - Developers added a new field—Duration or Total Volume—to the IV Fluid Order dialog. This field enables users to specify a maximum duration or total volume for their IV orders, helping ensure that patients do not receive IV fluids for too long or receive too much fluid.
- PSI-04-001 Template Field Data Not in Final Note (SLC-0901-51635) - When a user selected template fields and then selected the Next button, CPRS did not put the template field information in to the final progress note. Developers corrected this problem.
-   
  PSI-04-016 Autosave Changes to Help User Save Data if Note Experiences a Problem (NOIS: TUA-0104-31822, MON-0304-52402) - In previous CPRS versions, CPRS gave no indication to the user if an autosave experienced an error, which usually occurred on a long note and usually because of unknown connectivity issues. On occasion, a cryptic developer debugging message would be displayed, but the message did not help the user much and also caused CPRS to shutdown. Developers made changes to this version so that if an error occurs, CPRS advises the user to retry via CTRL-SHIFT-S (save and continue) or "Save without signature" to improve chances to recover any text that was not correctly saved due to the error. If this process continues to fail, CPRS instructs the user to copy and paste the text of the note to MS-Word before continuing or exiting CPRS.
- PSI-04-020Child Event-Delayed Orders Do Not Have a Location (NOIS CAH-0404-31873, AMA-0903-71117) - Previously, when a user entered a delayed order for lab, and the order is a complex order (same order multiple times), the "child" orders did not get assigned a location when the delayed event occurs. This causes the lab orders to not appear on ward collection lists and other places, which may mean the orders are missed. This problem is described in PSI-04-020. Developers corrected this problem and created a post-install routine that identifies any existing lab orders that do not have a location and sends an email report to the designated person or group.
- PSI-04-023 Lab Info Box Display Problem (NOIS MAC-0903-60683) - The Lab Info Box now displays its text at the top not the bottom.
- PSI-04-039 Problem List Entry OK Button Unavailable at Font Size 8 (NOIS BUT-0704-21314) - If the font size on the Problem List Entry is greater than 8, the user is unable to access the OK button to accept the new problem. This has been corrected
- PSI-04-042 Message Text Problem in Dialog (NOIS PAL-0704-60893) - Developers corrected a problem where all of the text in a Radiology dialog message area could not be viewed. CPRS displayed part of the text, but there were no scroll bars and the user could not view the remaining text.
- PSI-04-048 Problem Entry Goes in Wrong Chart (NOIS MAC-0904-60407) – If a user began entering a problem on a patient’s Problems tab in CPRS and then decided not to and went to select another patient, CPRS prompted the user if it should discard the changes. If the user selected Cancel, and then opened another patient’s chart in CPRS, the partially finished problem was there and could be entered for the wrong patient. This has been corrected. If the user selects Cancel, CPRS returns to the Problems tab, but does not carry the information into another patient’s record.
- PSI -04-054 Context Problem Could Present Incorrect Data - Developers fixed a problem affecting users holding the ORELSE key and with the site parameter OR SIGNATURE DEFAULT ACTION set to "Release w/o Signature". On acceptance of a patient change request from another application, CPRS displayed the signature box before the patient change would be allowed to continue. This was incorrect CCOW behavior. But clicking CANCEL on that signature dialog then resulted in the previous patient's orders still being listed on the Review/Sign Changes screen for the newly synchronized patient. This now works correctly.
- PSI-04-055 Auto-selection of Medication Schedule - Prior to the non-standard schedule project included in CPRS v.25, a provider entering an inpatient medication order could type in any free text schedule. If what the provider typed was not in the schedule list but passed the format validation, it would be accepted as a non-standard schedule. With the non-standard schedule project, the provider must now choose a schedule from the list or use the Other option to build a customized day-of-week/time administration schedule.

  Again, in previous CPRS versions, when the provider typed in characters to select a schedule, CPRS would match as many characters as it could and then auto-select the first schedule in the list that most closely matched. For example, if Q12H was the first in the list and the provider typed Q1, typed return or tab, Q12H would be selected—even if the provider really wanted Q18H. This could lead to problems if the provider did not carefully review the orders entered before accepting and signing them.

  What is fixed in v25:
- If a provider enters a schedule that is not included in the schedule list, the schedule field will remain blank until a valid entry is selected. For example, if a provider enters Q5, but there is no schedule with those characters, no schedule will be auto-selected.
- If a provider types characters that match more than one schedule (for example, Q3 would match Q3H and Q36H), the software will fill in the schedule field with the first entry in the schedule list that matches those characters. Therefore, providers must continue to diligently review their orders.

  What will need to wait for a later release of CPRS GUI:
- ComboBox controls currently scroll down and auto-select the first entry that matches what is typed. To change to not auto-select the first entry but require an actual click or some other action will require a custom control.

<span class="smallcaps">New Features and Changes in CPRS v.25</span>

Patch OR\*3\*195, version 25 of the CPRS GUI introduces the following main features in addition to the enhancements and fixes listed subsequently:

- Clinical Indicators Data Capture (CIDC)
- Allergy/Adverse Reaction Tracking (with OR\*3\*216 & GMRA\*4\*21)
- Non-Standard Schedules for Meds
- A "Clinic Medications" Display Group
- Separate Cover Sheet and PCE Date Range Parameters

Clinical Indicators Data Capture (CIDC)

> **NOTE:** Sites should not implement these features until they receive guidance from the VHA Chief Business Office (CBO). If you have any questions, please contact Dan Speece, CBO Implementation Manager for CIDC, at (202) 254-0137.Note: Providers will not see most CIDC changes in CPRS until the site enables a system-level switch and IRM or CAC staff enables a user-level switch (parameter) for specific providers. Some changes for co-pay on service connection will be available as soon as CIDC patches from other packages are installed.

The new Clinical Indicators Data Capture (CIDC) features require users who hold the Provider key and the ORES key to enter Diagnoses and Treatment Factors (SC, CV, AO, IR, EC, MST, and/or HNC) for specific kinds of orders. CPRS will prompt users who hold the Provider and ORELSE key for the information, but entry for these users is optional. Diagnoses must be added for the following types of orders:

> CPRS Orders for Billing Setting

> Laboratory Outpatient only  
> Radiology Both Inpatient & Outpatient  
> Prosthetics Both Inpatient & Outpatient  
> Outpatient Pharmacy Outpatient only

Clinicians will be required to enter at least one diagnosis for each of the above orders, but can enter up to four. If the clinician enters multiple diagnoses, the first diagnosis the clinician enters will be the primary diagnosis by default. The provider, however, can change which diagnosis is designated as the primary diagnosis. The clinician must also enter Treatment Factors for any qualifying patient; qualifying patients will have the check boxes appear on the Electronic Signature dialogs and the Diagnosis tab of the Encounter form.

- To help clinicians enter diagnoses more efficiently, developers have added the ability to do the following:
- When on the Electronic Signature dialogs, clinicians can use the Shift + Click or Ctrl + Click features to highlight multiple orders that can then be assigned the same diagnoses.
- Clinicians can copy a diagnosis from one order and paste it one or multiple other orders.
- Clinicians can create and edit a Personal Diagnoses List. This list is specific to the individual clinician. Clinicians can add any diagnosis to this list so that it is available to help them specify clinical indicator information when signing the appropriate orders.
- Also, to help speed Treatment Factor entry, developers added code so that if a problem on the Problem List has associated Treatment Factors and the Provider signing orders selects that diagnosis using the Problem List as a source, CPRS automatically populates the appropriate boxes on the Electronic Signature dialogs with those Treatment Factors. Clinicians will be able to edit them or accept them as they are populated. To use this feature effectively, clinicians will need to ensure that the problems on the Problem list have the Treatment Factors associated with them.
- Developers added a feature that supports the clinician’s workflow by displaying diagnoses entered for today’s orders on the Diagnosis Tab of the Encounter form (today in this case means within 24 of the visit for this particular patient). In addition, if the clinician does the Encounter form first, the diagnoses enter on the Diagnosis tab of the encounter form will be a choice on the Assign Diagnosis to Order(s) dialog that clinicians will use the assign a diagnosis for each appropriate order he or she will sign.
- Developers also added a feature that will copy the Treatment Factors when clinicians use the Copy, Change, or Renew actions on orders.
- Shortcut Keys Added to Display Hover Hints and Move to the Grid of Orders – Developers added shortcut keys to help keyboard users display hover hints and move to the grid of orders.  
    
  Definitions for service connection and treatment factors are available to users by hovering the cursor over the term or using the appropriate keyboard shortcut. Users can also move to list of orders using a keyboard shortcut. The shortcuts are shown in the list below:
- Service connection (SC) Alt + c
- Combat Veteran (CV) Alt + v
- Agent Orange (AO) Alt + o
- Ionizing Radiation (IR) Alt + r
- Environmental contaminants(EC) Alt + e
- Military Sexual Trauma (MST) Alt + m
- Head and/or Neck Cancer (HNC) Alt + n
- Move to the list of orders Alt + s

Allergy/Adverse Reaction Tracking

The following functionality is available only to sites that have installed patches OR\*3.0\*195, OR\*3.0\*216, and GMRA\*4.0\*21. Sites that have not installed these patches will continue to receive the ART functionality that exists in CPRS GUI 24.

- Allergies No Longer Entered as Orders (NOIS: SHR-0603-71103) – At sites that have installed the patches listed above, users can no longer enter allergies and adverse reactions as orders that are placed in the *ORDERS* file. Patch OR\*3.0\*216 exports a modified order-dialog entry—*GMRAOR ALLERGY*—in the *ORDER DIALOG* file. This entry enables CPRS to interact directly with the Adverse Reaction Tracking (ART) package (i.e., CPRS adds new allergies and adverse reactions directly into the ART package as users submit them.)

With supporting patches OR\*3.0\*216 and GMRA\*4.0\*21, CPRS GUI 25 does not display allergy information on the Orders tab. It displays allergy information only on the Cover Sheet tab. Nevertheless, users can still enter allergy information from the Orders tab by selecting Allergies in the Write Orders pane. (i.e., users can still go to a familiar place to enter allergies.)

In addition, users can no longer select OTHER ALLERGY/ADVERSE REACTION as a type of causative agent, nor can they select OTHER REACTION as a type of sign/symptom. Changes to the ART package have eliminated these items as choices. These changes mark a continuing effort to end free-text and unspecific entries.

Also, CPRS now requires users to enter information about the nature of the reaction that they are documenting (Allergy, Pharmacological, or Unknown).

Finally, CPRS GUI 24 introduced a dialog through which users can request that a causative agent be added to their site’s *ALLERGIES* file. Users access this dialog via a warning that pops up when they attempt to enter a free-text causative agent. The warning dialog asks users to indicate—by clicking either its YES or NO button—if they want to send a causative-agent inclusion request. In CPRS GUI 24, the default button was YES. In CPRS GUI 25, the default button is NO. Furthermore, when users click the system X button (located in the top right-hand corner of each screen) to exit any of the screens that comprise the inclusion-request dialog, CPRS now cancels the request action.

 

- Allergy Changes on the Cover Sheet –CPRS now enables users to perform several ART-related actions from the Cover Sheet tab—including the following:
  - Enter new allergy
  - Mark selected allergy as entered in error
  - Mark patient as having “No Known Allergies” (NKA)

When users right click within the Allergies/Adverse Reactions pane, CPRS displays a menu offering the three selections listed in the previous paragraph (or a subset of these selections, depending on allergy information that is currently active for the selected patient). When users select one of the allergies listed within the Allergies/Adverse Reactions pane, CPRS opens a dialog that displays details about this allergy—as it always has. However, this dialog now includes two additional buttons: Add New and Entered in Error. As the names of these buttons suggest, clicking them enables users to add new allergies and designate the selected allergy as entered in error, respectively. When users mark allergy entries as entered in error, the ART package notifies (via MailMan bulletins) sites’ GMRA MARK CHART mail group.

Depending on how sites have configured their *GMR ALLERGIES SITE PARAMETERS* files, the ART package could also send bulletins to one or more of the following mail groups: GMRA VERIFY DRUG ALLERGY, GMRA VERIFY FOOD ALLERGY, and GMRA VERIFY OTHER ALLERGY. In addition, marking an allergy entry as entered in error triggers the Text Integration Utility (TIU) package to generate an Allergy/Adverse Reaction progress note that is sent to the originator to document the erroneous entry.

Whether users enter new allergies via the Cover Sheet or Orders tab, CPRS displays an Enter Allergy or Adverse Reaction dialog, through which users enter adverse reactions and allergies directly into the ART package. This dialog includes several changes, including the following changes:

- CPRS uses the default of Now for the origination date. This date is set by CPRS when the user enters the allergy and the user cannot edit it.
- CPRS no longer allows future dates for observed allergies; if users attempt to enter future dates, CPRS prevents them from doing so when they click OK to submit their allergy entries
- A new button containing a question mark is associated with the Severity dialog; when users select this button, CPRS displays a text box defining severity selections
- CPRS displays a hover hint when users mouse over the Observed and Historical option buttons; a user group (as opposed to OI staff) specified the text of the hover-hint
- When the amount of text in the Comments dialog exceeds its viewing area, CPRS adds a scroll bar to the dialog
- Developers altered the tabbing sequence to more closely match users’ expectations
- When a user marks an allergy as an Observed, Drug allergy or as Entered in Error, the action generates a Progress Note for the user who marked it as such to sign. Once the user who marked the allergy as an Observed Drug allergy or as entered in error signs the note or an administrative user signs the note, all CPRS users can view the note. In the case of Entered in Error, this will let users know that the allergy was removed from the list.

The Enter Allergy or Adverse Reaction dialog also contains a new check box: ID Band Marked. If the patients are inpatients and the sites have set the MARK ID BAND parameter in the *GMR ALLERGY SITE PARAMETERS* file to 1(YES), users can select this check box to indicate whether they have marked allergies and adverse reactions on the patient’s identification (ID ) bands. If users submit an allergy entry without selecting activated ID Band Marked check box, the ART package automatically notifies sites’ GMRA MARK CHART mail group via a MailMan bulletin. *GMR ALLERGY SITE PARAMETER* file settings also determine to which verification mail groups (GMRA VERIFY DRUG ALLERGY, GMRA VERIFY FOOD ALLERGY, or GMRA VERIFY OTHER ALLERGY) the ART package sends MailMan bulletins when users enter specific combinations of allergy information. (See the [*Adverse Reaction Tracking Technical Manual*](http://www.va.gov/vdl/VistA_Lib/Clinical/CPRS-Advrs_Reaction_Trk_(ART)/allr4_tm.pdf) for information about how to configure the *GMR ALLERGY SITE PARAMATER* file.)

Non-Standard Schedules

When placing inpatient medication orders, users can no longer enter free-text schedules. Instead, users must select standard schedules from the Schedule list box or select Other from the Schedule list box to create a customized day-of-week or admin/time schedule. If users try to copy, transfer, or renew inpatient medication orders, CPRS allows only orders with valid schedules to proceed.

> **NOTE:** If the user selects Other to create a customized schedule, the order may require that the pharmacist and the physician work out a valid schedule, which might delay the order becoming active. The parameter ORWIM NSS MESSAGE enables sites to customize the message in the text box on the Order with Schedule “OTHER” dialog to inform providers that a delay may be caused or give instructions. A default message appears in the text box if the site does not enter one.

Inpatient Medications for Outpatients (IMO)

> **NOTE:** IMO features will not be available in the CPRS until patch SD\*5.3\*285 is installed in your account. This patch is currently under development.

- IMO Orders Displayed under Clin. Meds on the Orders Tab - When IMO orders are placed from an authorized IMO location for an outpatient, CPRS will save newly placed Unit Dose and IV fluid orders under the “Clin. Meds” group.
- New Clinic Medications Display Group For Inpatient Medications for Outpatients (IMO) Orders - Developers created a new display group, *CLINIC MEDICATIONS*, for IMO orders. On the Orders tab, CPRS displays IMO orders under the new display group (Clin. Med). On the Meds tab, CPRS displays IMO orders sorted at the top of the Inpatient Medications pane with the ordering location in the last column. (To view all IMO orders, users can select View \| Custom Order View from the main menu, then, in the Service/Section pane of the Custom Order View dialog box, click to expand PHARMACY and select CLINIC MEDICATIONS.) Users cannot transfer IMO orders. To add the Clinic Medications display group to the Order tab, use the following instructions:

For CPRS to display the Clinic Medications display group on the Orders tab (the display group that shows Inpatient Medications for Outpatients), sites will need to make an entry in the ORWOR CATEGORY SEQUENCE parameter at the package or system level depending on which level the site uses.

Sites may choose for themselves what sequence number to assign to Clinic Medications based on where they would like the IMO orders to display. Because it is a medication order, sites may want to place it close to the other medication display groups (Inpt. Meds, Out. Meds, Non-VA Meds).

The user that adds this entry to the parameter will need to check whether your site uses Package or System level setting for this parameter. As with all parameters, the lower level setting takes precedence so if your site has defined System level settings, the System level would be used rather than Package level. If your site uses the Package level settings, someone at your site will need to add Clinic Medications to the Package level settings.

> **NOTE:** To change the parameter at the Package level, the user making the change must be in programmer mode. Changes at the system level do not require the user to be in Programmer mode. Only authorized users should make this change.

Manually Updating ORWOR CATEGORY SEQUENCE

First, you need to check the settings for this parameter to determine if you need to add Clinic Medications to the Package or System level settings for the ORWOR CATEGORY SEQUENCE parameter. Then, you can add this entry to the sequence at the appropriate level.

To check the parameter values and add the display group "Clin. Meds”, use the following steps:

1.  Login to the List Manager interface to your system.
2.  At the Option Name prompt, type ORMGR and press \<Enter\>.
3.  At the CPRS Manager Menu Option prompt, type IR and press \<Enter\>.
4.  At the CPRS Configuration (IRM) Option prompt, type XX and press \<Enter\>.
5.  To list values for this parameter, at the General Parameter Tools Option prompt, type LV and press \<Enter\>.
6.  At the Parameter Definition Name prompt, type ORWOR CATEGORY SEQUENCE and press \<Enter\>.

> Below is an example of how to list the parameter values.

Select OPTION NAME: ORMGR CPRS Manager Menu

Select CPRS Manager Menu Option: IR CPRS Configuration (IRM)

Select CPRS Configuration (IRM) Option: XX General Parameter Tools

Select General Parameter Tools Option: LV List Values for a Selected

Parameter

Select PARAMETER DEFINITION NAME: ORWOR CATEGORY SEQUENCE Orders

Category Sequence

The display should look similar to what is below.

Values for ORWOR CATEGORY SEQUENCE

Parameter Instance Value

--------------------------------------------------------------------------

--

PKG: ORDER ENTRY/RESULTS REPOR 10 M.A.S.

PKG: ORDER ENTRY/RESULTS REPOR 20 ALLERGIES

PKG: ORDER ENTRY/RESULTS REPOR 30 VITALS/MEASUREMENTS

PKG: ORDER ENTRY/RESULTS REPOR 35 ACTIVITY

PKG: ORDER ENTRY/RESULTS REPOR 40 NURSING

PKG: ORDER ENTRY/RESULTS REPOR 50 DIETETICS

PKG: ORDER ENTRY/RESULTS REPOR 60 IV MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 65 OUTPATIENT MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 68 NON-VA MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 70 INPATIENT MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 75 LABORATORY

PKG: ORDER ENTRY/RESULTS REPOR 80 IMAGING

PKG: ORDER ENTRY/RESULTS REPOR 90 CONSULTS

PKG: ORDER ENTRY/RESULTS REPOR 100 PROCEDURES

PKG: ORDER ENTRY/RESULTS REPOR 110 SURGERY

PKG: ORDER ENTRY/RESULTS REPOR 120 OTHER HOSPITAL

SERVICES

In the above example, there are only Package level settings. If you see only “PKG”, your site uses the Package level setting and you will need to add CLINIC MEDICATIONS to your Package level. If you see one or more "SYS" listings, it indicates your site is not using the Package-level values and you must add CLINIC MEDICATIONS to your System level values.

> **NOTE:** To change the parameter at the Package level, the user making the change must be in programmer mode. Changes at the system level do not require the user to be in Programmer mode. Only authorized users should make this change.

7.  If you are going to add this entry to the Package level settings, go into Programmer mode (if you are not already in it) and then return to the General Parameter Tools option.
8.  At the General Parameter Tools Option prompt, type EP and press \<Enter\>.
9.  At the Parameter Definition Name prompt, type ORWOR CATEGORY SEQUENCE and press \<Enter\>.
10. If in Programmer mode, select whether you want to change the Package or System level.
11. At the Enter Selection prompt, type the sequence number that will place and press \<Enter\>.

> **NOTE:** If you are not sure what the other items in the sequence are type a question mark and press \<Enter\>.

12. At the Select Sequence prompt, type *the appropriate number* and press \<Enter\>.
13. At the Are you adding *the number* as a new Sequence prompt, type Y and press \<Enter\>.
14. The Sequence prompt should then appear with the number you typed, press \<Enter\>.
15. At the Display Group prompt, type CLINIC and press \<Enter\>.
16. To verify that it has been entered correctly, you could press \<Enter\> until you return to the General Parameter Tools option and type LV and press \<Enter\> to view the settings again.

Below is an example of how to make this entry at the package level.

Select OPTION NAME: ORMGR CPRS Manager Menu

Select CPRS Manager Menu Option: IR CPRS Configuration (IRM)

Select CPRS Configuration (IRM) Option: SS ??

Select CPRS Configuration (IRM) Option: XX General Parameter Tools

LV List Values for a Selected Parameter

LE List Values for a Selected Entity

LP List Values for a Selected Package

LT List Values for a Selected Template

EP Edit Parameter Values

ET Edit Parameter Values with Template

EK Edit Parameter Definition Keyword

Select General Parameter Tools Option: LV List Values for a Selected Parameter

Select PARAMETER DEFINITION NAME: ORWOR CATEGORY SEQUENCE

Values for ORWOR CATEGORY SEQUENCE

Parameter Instance Value

----------------------------------------------------------------------------

PKG: ORDER ENTRY/RESULTS REPOR 10 M.A.S.

PKG: ORDER ENTRY/RESULTS REPOR 20 ALLERGIES

PKG: ORDER ENTRY/RESULTS REPOR 30 VITALS/MEASUREMENTS

PKG: ORDER ENTRY/RESULTS REPOR 35 ACTIVITY

PKG: ORDER ENTRY/RESULTS REPOR 40 NURSING

PKG: ORDER ENTRY/RESULTS REPOR 50 DIETETICS

PKG: ORDER ENTRY/RESULTS REPOR 60 IV MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 65 OUTPATIENT MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 68 NON-VA MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 69 CLINIC MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 70 INPATIENT MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 75 LABORATORY

PKG: ORDER ENTRY/RESULTS REPOR 80 IMAGING

PKG: ORDER ENTRY/RESULTS REPOR 90 CONSULTS

PKG: ORDER ENTRY/RESULTS REPOR 100 PROCEDURES

PKG: ORDER ENTRY/RESULTS REPOR 110 SURGERY

PKG: ORDER ENTRY/RESULTS REPOR 120 OTHER HOSPITAL SERVICES

Enter RETURN to continue or '^' to exit:

LV List Values for a Selected Parameter

LE List Values for a Selected Entity

LP List Values for a Selected Package

LT List Values for a Selected Template

EP Edit Parameter Values

ET Edit Parameter Values with Template

EK Edit Parameter Definition Keyword

Select General Parameter Tools Option: EP Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: ORWOR CATEGORY SEQUENCE

ORWOR CATEGORY SEQUENCE may be set for the following:

8 System SYS \[EXPCUR.FO-SLC.MED.VA.GOV\]

10 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 10 Package ORDER ENTRY/RESULTS REPORTING

Parameters set for 'Package' may be replaced if ORDER ENTRY/RESULTS REPORTING is installed in this account.

Setting ORWOR CATEGORY SEQUENCE for Package: ORDER ENTRY/RESULTS REPORTING

Select Sequence: ?

Sequence Value

-------- -----

10 M.A.S.

20 ALLERGIES

30 VITALS/MEASUREMENTS

35 ACTIVITY

40 NURSING

50 DIETETICS

60 IV MEDICATIONS

65 OUTPATIENT MEDICATIONS

68 NON-VA MEDICATIONS

70 INPATIENT MEDICATIONS

75 LABORATORY

80 IMAGING

90 CONSULTS

100 PROCEDURES

110 SURGERY

120 OTHER HOSPITAL SERVICES

Select Sequence: 69

Are you adding 69 as a new Sequence? Yes// YES

Sequence: 69// 69

Display Group: CLINIC MEDICATIONS

Select Sequence:

ORWOR CATEGORY SEQUENCE may be set for the following:

8 System SYS \[EXPCUR.FO-SLC.MED.VA.GOV\]

10 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

Enter selection: 10 Package ORDER ENTRY/RESULTS REPORTING

Cover Sheet / Encounters

Date Ranges - Developers have changed the parameters that control the date ranges for Appointments/Visits/Admissions on the Cover Sheet and the Visits on the Provider & Location for Current Activities dialog box (also called the Encounter Form).

In previous versions of CPRS, there were four parameters, two pairs, to control these date ranges. However, in practice, CPRS only used one parameter in each pair to control visit, admission, and appointment date ranges on the Cover Sheet and Encounter Form.

The field requested changes and developers have created five new parameters to control date ranges. The five new parameters are as follows:

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><strong>LM Display Name</strong></th>
<th><strong>Set in CPRS GUI?</strong></th>
<th><strong>Who can set?</strong></th>
<th><strong>Possible values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em><strong>ORQQCSDR CS RANGE START</strong></em></td>
<td>Cover Sheet Appts &amp; Visits START Range</td>
<td>Yes (user level) —Tools | options, General Tab, Date Range Defaults</td>
<td><p>User level—Users or CACs</p>
<p>Other Levels—CACs</p></td>
<td>1 to 999 (days before today)</td>
</tr>
<tr class="even">
<td><em><strong>ORQQCSDR CS RANGE STOP</strong></em></td>
<td>Cover Sheet Appts &amp; Visits STOP Range</td>
<td>Yes (user level)—Tools | options, General Tab, Date Range Defaults</td>
<td><p>User level—Users or CACs</p>
<p>Other Levels—CACs</p></td>
<td>1 to 999 (days in the future)</td>
</tr>
<tr class="odd">
<td><em><strong>ORQQEAPT ENC APPT START</strong></em></td>
<td>Encounter Appts START Range</td>
<td>Yes (user level)—Tools | Options, General Tab, Other Parameters…</td>
<td><p>User level—Users or CACs</p>
<p>Other Levels—CACs</p></td>
<td>1 to 999 (days before today)</td>
</tr>
<tr class="even">
<td><em><strong>ORQQEAPT ENC APPT STOP</strong></em></td>
<td>Encounter Appts STOP Range</td>
<td>Yes (user level)—Tools | Options, General Tab, Other Parameters…</td>
<td><p>User level—Users or CACs</p>
<p>Other Levels—CACs</p></td>
<td>1 to 999 (days in the future)</td>
</tr>
<tr class="odd">
<td><em><strong>ORQQEAFL ENC APPT FUTURE LIMIT</strong></em></td>
<td>Future Days Limit For PCE Selection</td>
<td>No—List Manager Only</td>
<td>IRM and CACs only</td>
<td>0 to 180 days (in the future)</td>
</tr>
</tbody>
</table>

The following comparison illustrates List Manager menu changes under the *CAC CSGUI Cover Sheet Display Parameters* ... menu option:

<u>Old Menu Text (4 Items):</u>

Appt Search Start Date

Appt Search Stop Date

Visit Search Start Date

Visit Search Stop Date

<u>New Menu Text (5 Items):</u>

Enc Appt Range Start Offset

Enc Appt Range Stop Offset

Future Days Limit For PCE Selection

Cover Sheet Visit Range Start

Cover Sheet Visit Range Stop

Two parameters, ORQQCSDR CS RANGE START and ORQQCSDR CS RANGE STOP control the date ranges for Appointments/Visits/Admissions appearing on the Cover Sheet. Two parameters, ORQQEAPT ENC APPT START and ORQQEAPT ENC APPT STOP control the date ranges for encounter information. One ORQQEAFL ENC APPT FUTURE LIMIT provides sites with a way to inform users that they are selecting a future appointment outside of the range permitted by local policy.

Users can also specify a temporary encounter date range from the Provider & Location for Current Activities dialog box by selecting the Clinic Appointments tab and clicking the Date Range button.

> **NOTE:** The *Future Days Limit For PCE Selection* \[*ORQQEAFL ENC APPT FUTURE LIMIT*\] parameter determines the number of days in the future that users can select for encounter appointments without receiving a warning. While users can still select future dates for encounter appointments that fall outside this parameter’s setting, the parameter enables sites to provide feedback via a warning indicating users may be violating local policies.

> Use the following guidelines for entering the allowable values listed above:

- Cover Sheet Appts & Visits START Range: use the usual T-xx method
- Cover Sheet Appts & Visits STOP Range: use the usual T+xx method
- Encounter Appts START Range: use a positive number *before* today
- Encounter Appts STOP Range: use a positive number *after* today
- Encounter Days Limit for PCE Selection: use a positive number from 0 to 180

Installation Notes:

- PACKAGE-LEVEL SETTINGS - During installation, post-install code examines the division-, system-, and package-level settings of the two previously used parameters (*ORQQVS SEARCH RANGE START* and O*RQQAP SEARCH RANGE STOP*) and populates only the package-level start and stop values of the new parameter pairs. If the post-install code finds no settings, it uses default settings of T-90 and T+90 to populate values for the new pairs at the package level.
- USER-LEVEL SETTINGS - The post-install code also examines current user-level settings for the two previously used parameters (see above) and populates both new parameter pairs with these values.

> **NOTE:** If users have current settings (using each half of the previous two pairs of parameters), their Cover Sheet tab and Provider & Location for Current Activities dialog box date ranges won’t change following patch installation. Because many users may now wish these date ranges to be different, after sites install the patch, it might be good to alert users to the possibility of setting these date ranges differently.

- NEW *ORQQEAFL ENC APPT FUTURE LIMIT* PARAMETER - The post-install code populates the *ORQQEAFL ENC APPT FUTURE LIMIT* parameter at the package level with a value of 7 (for seven days).

After the post-install code has made these changes, sites can alter the settings for the new *ORQQEAPT ENC APPT START*, *ORQQEAPT ENC APPT STOP*, *ORQQCSDR CS RANGE START,* and *ORQQCSDR CS RANGE STOP* parameters, if needed, at the following levels: system, division, location, and user. (Sites can use the system-level setting to set defaults for all users who do not set these parameters themselves.) Sites can also set a value for the *ORQQEAFL ENC APPT FUTURE LIMIT* parameter: there is no user-level setting for this parameter.

Provider Selection Lists

CPRS GUI 25 uses a new cross-reference and enhanced Kernel code to improve performance in creating provider selection lists.

<span class="smallcaps">Bug Fixes</span>

Patient Record Flags (PRF)

PRF Data Removed from Patient Selection Screen - Due to privacy concerns, developers removed the Patient Record Flag information that previously displayed on the Patient Selection Screen. If a patient has a record flag, CPRS displays the information in a pop-up box after the patient has been selected and CPRS has displayed appropriate warnings and collected audit information about who is accessing the record.

Template Dialogs

Performance Improvement - Developers made changes to improve template dialog performance.

Event Delayed Orders

- Event Delayed Orders Status Issues (MOU-0803-30190, ISL-0903-50918 PSI-03-036) - Developers addressed a problem with locking event-delayed orders that allowed users to act on orders in close succession and could create two of the same order with statuses, such as discontinued and active. Additional locks have been added to prevent this from happening. See also PSI-04-010.
- Event Delay Default Order Now Displayed on Delayed and Active Views (NOIS HUN-0103-20454) - Previously, if a user changed a patient movement order (admission, discharge, or transfer) that had been entered using the Event Delayed Default Order dialog, the order was visible only on the Delayed Orders view. Developers have corrected this, and these changed orders display on both the delayed and active order views with a status of “unreleased”.
- New IV Fluid Duration or Total Volume Field Added (PSI-03-060, HIN-1203-42283) - Developers added a new field “Duration or Total volume” to the IV Fluids order dialog. By using this field, a user can specify the maximum duration or total volume for the IV order to better insure the patient does not receive their IV for too long or receive too much fluid.
- Disparity Between BCMA and CPRS Order StatusAssociated NOIS
- BAY-1003-32131
- LIT-0903-71958
- CLE-0903-41758
- SAJ-0903-71602
- LOM-0803-61259
- MOU-0803-30190
- LEX-0603-41753
- FAV-0403-71497

Pharmacy orders were showing a status of active on the meds tab and in BCMA, but which were discontinued on the CPRS side. Developers discovered that the orders were being released more than once as part of the delayed order processing. This was caused by multiple processes trying to act on delayed orders at the same time causing the orders to release simultaneously, which caused the problem with the pharmacy orders.

The first protocol processed on the DGPM PATIENT MOVEMENT list inadvertently released the lock on the patient record so that other movements could be entered or edited. The lock should be maintained until the entire list of protocols has been processed.

Patch DG\*5.3\*549 will now maintain the lock on the patient's movement record until protocol processing has finished and stop users or other protocols from simultaneously processing the patient's movement information. In addition, developers added CPRS code to prevent users from manually releasing orders while the event is being processed. Conversely, if a user is manually releasing orders, the processing of the delayed event due to a patient movement will be held until the user is finished with the manual release of orders.

- Locking Problem Allowing Same IENs for Orders (NOIS LAH-1203-61784) - In very rare cases, a lock being released before the data was written to the global and that could allow the same internal entry number to be used during event delayed order writing. Developers made changes to ensure that the lock stays in place until all data is recorded before releasing the entry.
- Child EDO Orders Not Being Canceled when Parent Is Canceled (NOIS AMA-0403-71196) - When a patient is discharged, all existing delayed events that were written during the admission and that haven't been acted on yet are canceled. For a child order, only the parent event and its related orders were canceled. The child orders could not be acted upon after the parent was canceled. This has been corrected.
- Child Event-Delayed Orders Do Not Have a Location (PSI-04-020, NOIS CAH-0404-31873, AMA-0903-71117) – Previously, when a user entered a delayed order for lab, and the order is a complex order (same order multiple times), the "child" orders did not get assigned a location when the delayed event occurs. This causes the lab orders to not appear on ward collection lists and other places, which may mean the orders are missed. This problem is described in PSI-04-020. Developers corrected this problem and created a post-install routine that identifies any existing lab orders that do not have a location and send an email report to the designated person or group.

Orders

- Order Set Problem Corrected (NOIS MAC-1101-62553, TUC-0103-62288) - A problem was reported with an order set containing an order menu that contained another order set. If the order set were executed to the end, it cannot return the upper level order menu for selection. This has been corrected.
- Order with Priority Set to Done Not Discontinued (NOIS MIN-0203-42113) - If a provider changed a pending order’s priority to “done”, the original order did not get discontinued and still had a pending status. This has been corrected.
- Inappropriate Prompting for Co-Pay Information Corrected (NOIS JAC-1202-71057) - Users were prompted for co-pay exemptions on outpatient medications given during treatment. They should not be asked. This has been corrected.
- Mismatched Orders Between Outpatient Pharmacy and CPRS (NOIS UNY-0103-12342) - When pharmacists changed the dispense unit field in Outpatient Pharmacy, it did not create a new order with changed dispense units in CPRS and that resulted in mismatched orders. This has been corrected.
- Dosage Conversion in Sig Corrected (NOIS TUA-0204-30045) - Possible dosages like 1.5 did not convert to text as “one and one-half” in order sig field. This has been corrected.
- Problem with CPRS Dosage Matching (PSI-03-059, NOIS CPH-1203-42234) – Previously, in the medication order dialog, when a provider typed in part of a dosage, CPRS would try to highlight the correct dosage based on the first character the user entered. If the provider was not careful about checking the dosage, it was possible to select the wrong dosage if the dosages began with the same first character (e.g., 2mg and 200mg) and the provider accepted what was highlighted without reviewing the selection.  
    
  Developers have changed the way CPRS matches what is typed to make it much more difficult for CPRS to select the wrong dosage. Users will have to type in more characters (numbers, letters, spaces, and decimal points) to highlight the appropriate dosage from those displayed on the list. It may be as quick to use the mouse or tab and arrow keys to select the dosage from the list. Users may continue to type in free-text dosages.  
    
  For example, if CPRS displays dosages of 2mg, 2.5mg, 20mg, and 200mg for a medication, the minimum number of characters for a match is two because the shortest dosage (2mg) is three characters. The table below shows what the user would need to type to match the dosage:

  Dosage Text typed to highlight

  2mg 2m

  2.5mg 2.

  20mg 20

  200mg 200
- List Manager Verification Problem Fixed - This patch corrects a problem with verifying orders. On rare occasions, a user does not see the verify option when reviewing orders in the List Manager interface. This has been corrected.
- Additional List Manager Verification Problem (NOIS: SHR-0603-70545) - In the list manager interface, if the last order processed for a patient when building the active orders list is a renewed prescription, the verify options are not displayed when the order is selected. This has been corrected.
- For Discontinued Child Orders, Providers Must Sign All or None (NOIS MIN-0304-42815) - When a user discontinued a complex order, CPRS discontinued all child orders also. On the “Review/Sign Changes” dialog or “Sign selected orders” dialog, CPRS allowed the user to uncheck each individual child order, leaving some of the child orders signed and others unsigned. This has been corrected. The Provider must now sign all child orders or none after a Discontinue action.
- Order Dialog Closing Corrected (NOIS ATG-0304-32328) - After a user opened the order dialog and then switched to another tab, the order dialog was forced to close. This has been corrected.
- Dosage with Half Tablets Not Expanding Correctly in Instruction Field (NOIS TUA-0104-31631) - When a user chose an outpatient medication that contains a dosage that uses half tablets along with a whole tablet, the dosage was not expanding to read correctly in the CPRS instruction field. An example would be Lopressor 75mg dosage that is built on the 50mg tab. When the user chooses the 75mg dose, the text should read “one and one-half tablet” in the instruction field in CPRS instead of 1.5 tablets. This has been corrected.
- Display Problem Corrected (NOIS CPH-0703-42298, NTH-0703-71061) – Previously, if entering a lab quick order, a user could enter a value for the "Collection Date/Time". If the user tried to enter a date value of T+1D (today plus one day), T+1W (today plus one week), T+1M (today plus one month), and T+1Y (today plus one year), CPRS was only reading the first part of “T+1”, ignoring the units, and displaying "TOMORROW" for all of them. This has been fixed.

Non-VA Meds

- Change in Non-VA Meds Display - The Comments section of the Non-VA Med order form now only displays the expanded schedule.
- No Signature Required on Discontinue (NOIS: DUR-0704-31206) - An electronic signature is no longer required upon discontinuing a Non-VA med.

Order Checks

Order Checks Occurring for Different Ordering and Signing Clinicians (PSI-04-040 and E3R 16750) - Previously, order checks did not display upon order signature if the user signing the order is different than the user entering the order. Developers corrected this and reactivated order checking if the user signing the order is different than the user entering the order.

Procedures

Procedure Dialog Error Message Corrected - When ordering a new procedure via the basic dialog, but not using a quick order, CPRS would display a message reading "no services available for this procedure". This has been prevented because the user has not selected a procedure yet.

Patient Demographics

Patient Demographic Server Error Corrected (NOIS: MAD-1001-41873) - If a null value for DFN was passed to the patient demographics call, a server error could occur at VADPT0+6. This has been corrected.

Encounters

Workload Not Required (NOIS: PUG-1103-50094) - Workload will no longer be required when signing notes for cancelled or no-show appointments, or for non-count historical clinics.

Consults

- The Consults Prerequisite Pop-Up Box Opens at Bottom of Text (NOIS: PUG-0803-51430) - When there is a long prerequisite text, the Consults Prerequisite pop-box was opening at the bottom of the text rather than at the top. Developers have corrected this and the box opens at the top of the text.
- Consults Information Updated for Care Management (NOIS PAL-0204-60417, MIN-0504-41044, CLA-0704-20322) - When a user does a group update of consults and the consults are set to Complete, Care Management was producing a result headlight to the ordering provider for every patient that had a consult group updated. The ordering provider is intentionally excluded from receiving notifications on these consults and should be exempt from acknowledging these results in Care Management. Developers made changes so that group updated consults no longer require a result acknowledgement.

Code Set Versioning

- CSV Code Checks Removed - When developers added Code Set Versioning (CSV) support GUI v22, not all required CSV patches had yet been released. Developers included numerous checks for the presence of these patches in the code to ensure correct behavior in either their presence or their absence. Because all of these patches have now been released, and the mandatory install date has long since passed, these checks have now been removed in the interest of performance, especially as related to the encounter form. The CSV patches have instead been added to the REQUIRED BUILDS list for this version.
- \# Marker Added to the Problem List Inactive View - On the Problems tab, inactive problems with inactive ICD codes were flagged with the "#" marker on the "Both Active and Inactive" view, but not on the "Inactive" view. The "#" will now appear for these problems in both cases.
- ICD9 Code and Diagnosis Removed from Printed Discharge Summary on Reports Tab - To comply with Code Set Versioning (CSV) requirements, developers changed the discharge summary entry on the reports tab to no longer display the ICD9 code or the diagnosis. Previously, if a discharge summary were linked to a problem, and the detailed display were printed, the ICD9 code and the corresponding diagnosis were displayed. The ICD9 code and diagnosis fields have been removed from the printed copy at the request of the CSV workgroup.

Tools Menu

- Error Message about Inconsistent Local File Entries - If a site had inconsistent local file entries for the "Options/Tools" menu, an error message would appear. Such entries should not normally occur because XPAR entry validation normally precludes the inconsistencies. Developers made a change so that CPRS will now display a warning message and the application will continue to run.
- Tools Menu Range Check Error Fixed (NOIS ANN-1203-40706 and duplicates) - The Tools menu currently supports the definition of only 31 items in the ORWT TOOLS MENU parameter. If more than 31 items were defined, a "range check" error would occur on startup, causing CPRS to shut down. Developers have now prevented the error, and CPRS provides a warning to the user that not all defined items may be displayed.
- Warning about Too Many Items on the Tools Menu Moved - The warning message about too many items defined for the tools menu has been moved from the initial CPRS startup sequence to the first time a user clicks on the Tools menu to open it. The warning will only be displayed the first time the Tools menu is displayed.

Notes, Consults, Discharge Summary, Surgery Tabs

- Autosave Changes to Help User Save Data if Note Experiences a Problem (NOIS TUA-0104-31822, MON-0304-52402, PSI-04-016) - In previous CPRS versions, CPRS gave no indication to the user if an autosave experienced an error, which usually occurred on a long note and usually because of unknown connectivity issues. On occasion, a cryptic developer debugging message would be displayed, but the message did not help the user much and also caused CPRS to shutdown. Developers made changes to this version so that if an error occurs, CPRS advises the user to retry via CTRL-SHIFT-S (save and continue) or "Save without signature" to improve chances to recover any text that was not correctly saved due to the error. If this process continues to fail, CPRS instructs the user to copy and paste the text of the note to MS-Word before continuing or exiting CPRS.
-   
  Disallowing Signature of Empty Notes When Application Disconnect Occurs - If a user is disconnected from the server after creating a new document, but before any text has been either saved or autosaved, the result is a blank unsigned document in TIU. On a hard disconnect, there is no way for either CPRS or TIU to prevent this from happening. In previous versions, if the user then logged in again, and attempted to sign that blank document, ignoring the warning about "possible missing text", a signed blank document would result. In this version, if the document is empty, as determined via a TIU API also used in LM, CPRS will not allow the user to sign the document.

TIU NOTES

- RPC "TIU ONE VISIT NOTE?" Problem Resolved - When determining if more than one note of a particular Document Type is allowed to be added to a particular visit, the RPC was not using a guaranteed method of choosing the correct visit. This change eliminates the possibility of the RPC choosing an incorrect visit to check.
- Actions Prevented on Note When Viewed from Consults Tab (NOIS PUG-0303-52230) - If a users was viewing a note on the Consults tab, CPRS did not allow any action to be taken on it from the Notes tab. Now, actions on the Notes tab will be prevented only if the note is actually being edited on the Consults tab. The reverse scenario was already working correctly.
- Template Field Data Not in Final Note (SLC-0901-51635, PSI-04-001) - When a user selected template fields and then selected the Next button, CPRS did not put the template field information in to the final progress note. Developers corrected this problem.

Discharge Summaries

- TIU Parameter For More than One Discharge Summary Now Respected (NOIS STX-1203-71286, BUT-0704-21314 PSI-04-039) - The TIU document parameter allowing or disallowing more than one note per visit was not being respected for documents in the Discharge Summary class on this tab. Until this version, only one document of the DISCHARGE SUMMARY class was allowed per admission, regardless of the value of the document parameter.

> **NOTE:** It is HIGHLY recommended that the overall DISCHARGE SUMMARY class be set to restrict its members to one occurrence per admission, and that if multiple interim summaries are to be used, the parameter be set individually for those titles, overriding the CLASS setting.

-   
  Warning about No Summary Selected - When a user selected the Identify Additional Signers option (Alt+A+I) with no matching Summary selected, it now displays a message informing the user of the problem. Also, if users utilize certain keystroke combinations (Alt-A-M, Alt-A-C, Alt-A-B, Alt-A-L, Alt-A-D, Alt-A-E, Alt-A-G) and no Discharge Summary is selected CPRS now displays a message informing the user.

Reminders

Historical Dates Entered Through Reminder Dialogs Not Updating PCE (NOIS CHS-0103-41180) – Developers fixed a problem involving historical dates entered through Reminder dialogs that did not update PCE. To correct this problem, developers no longer use the TaskMan variable ZTSYNC if the encounter date is a historical date. By not setting this variable, TaskMan will not check file \#14.8 for the encounter visit string. As soon as this patch is installed, sites can file historical encounter data for any date. This patch only fixes the problem for any historical date entered AFTER this patch is installed.

Sites will need to do some clean up on their systems if the site was having a problem with a historical date (i.e. 11/14/2001 or 11/2001).

Instructions for Correcting Inaccurate Historical Data

There is a coding fix to prevent future problems. In addition, the following steps provide a manual clean-up of old data. The three steps to the manual fix are outlined in detail below with example screen captures of the process. The three steps are

1.  Identify entries in file 14.8 (TASK SYNC FLAG) that were blocked by Taskman.
2.  Identify any encounter dates that are still pending with a status of 4 in file 14.4 (TASKS) that end with E, i.e. ORW0;3040100;E (see example below).
3.  Requeue all pending jobs to be filed by Taskman.

> **NOTE:** Any historical data that was entered before CPRS 25 that does not show in PCE will need to be manually cleaned up.

Manual Clean-up Step 1:

Steps to check if your site has historical data blocked by TaskMan

1.  Go to the main FileMan menu
2.  Select "SEARCH FILE ENTRIES" option \# 3
3.  Select file number 14.8 for the file to search through
4.  At the "SEARCH FOR TASK SYNC FLAG FIELD:" prompt, type "Name"
5.  At the "CONDITION:" prompt, type "contains"
6.  At the CONTAINS: prompt, type ";E~"
7.  Sort by Name
8.  Request the output to print both the Number (IEN) and the Name field
9.  If a list is returned, then you have previous Historical Encounter date that has been blocked by FileMan

Example Screen Capture of Manual Clean –up Step 1:

VA FileMan 22.0

Select OPTION: D\_ \_SEARCH FILE ENTRIES

OUTPUT FROM WHAT FILE: TASKS// 14.8 TASK SYNC FLAG (223 entries)

-A- SEARCH FOR TASK SYNC FLAG FIELD: NAME

-A- CONDITION: CONTAINS

-A- CONTAINS: ;E~

-B- SEARCH FOR TASK SYNC FLAG FIELD:

IF: A// NAME CONTAINS ";E~"

STORE RESULTS OF SEARCH IN TEMPLATE:

SORT BY: NAME//

START WITH NAME: FIRST//

FIRST PRINT FIELD: NUMBER

THEN PRINT FIELD: NAME

THEN PRINT FIELD:

Heading (S/C): TASK SYNC FLAG SEARCH Replace

DEVICE: '\_ \_ ANYWHERE Right Margin: 80//

TASK SYNC FLAG SEARCH JAN 17,2005 11:13 PAGE 1

NUMBER NAME

--------------------------------------------------------------------------------

126 ORW0;3000501;E~ORW/PXAPI RESOURCE

127 ORW0;3000606;E~ORW/PXAPI RESOURCE

124 ORW0;3010125;E~ORW/PXAPI RESOURCE

240 ORW0;3040100;E~ORW/PXAPI RESOURCE

227 ORW0;3040101;E~ORW/PXAPI RESOURCE

128 ORW27;3020314.12;E~ORW/PXAPI RESOURCE

6 MATCHES FOUND.

Manual Clean-up Step 2:

The next thing to do is to check to see if any of the encounter dates from the above list are still pending in TaskMan.

1.  Re-select the SEARCH FILE ENTRIES" option
2.  Select file \#14.4 as the file to search through
3.  At the "SEARCH FOR TASK SYNC FLAG FIELD:" prompt, type "Task Description"
4.  At the "CONDITION:" prompt, type contains
5.  At the CONTAINS: prompt, type "Data from CPRS to PCE"
6.  Sort by Number
7.  Request the Number (IEN), Sync Flag, and the Status Code fields in your output.

  
Example Screen Capture of Manual Clean –up Step 2:

Select OPTION: SEARCH FILE ENTRIES

OUTPUT FROM WHAT FILE: TASK SYNC FLAG// 14.4 TASKS (751 entries)

-A- SEARCH FOR TASK'S FIELD: 41 Task Description

-A- CONDITION: CONTAINS

-A- CONTAINS: Data from CPRS to PCE

-B- SEARCH FOR TASK'S FIELD:

IF: A//

Task Description CONTAINS (case-insensitive) "DATA FROM CPRS TO PCE"

STORE RESULTS OF SEARCH IN TEMPLATE:

SORT BY: NUMBER//

START WITH NUMBER: FIRST//

FIRST PRINT FIELD: NUMBER

THEN PRINT FIELD: Sync Flag

THEN PRINT FIELD: Sta

1 Status Code

2 Status DT

3 Status Notes

CHOOSE 1-3: 1 Status Code

THEN PRINT FIELD:

Heading (S/C): TASK'S SEARCH//

DEVICE: ;;99999999 ANYWHERE Right Margin: 80//

TASK'S SEARCH JAN 17,2005 11:14 PAGE 1

Status

NUMBER Sync Flag Code

--------------------------------------------------------------------------------

146780 ORW4;3050106.1044;D 4

150124 ORW0;3040100;E 4 \<== Requeue entries that end with E and have a status of 4

2 MATCHES FOUND.

All entries with that end in E with a status of four are pending in the TaskMan and have not been filed.

Manual Clean-up Step 3:

To get these jobs that are pending to file, do the following steps.

1.  Select the ENTER OR EDIT FILE ENTRIES option \#1
2.  At the INPUT TO WHAT FILE: prompt, enter file \#14.8
3.  At the EDIT WHICH FIELD prompt, enter name
4.  At the Select TASK SYNC FLAG NAME prompt, type the name from file 14.8 that should be deleted
5.  Delete the entries by entering the @ sign
6.  Do this for each entry in the File \#14.8 that you want to delete
7.  Once all of the appropriate entries in File \#14.8 are deleted, go to TaskMan
8.  Select the Requeue Tasks option
9.  At the Task Number prompt, enter the value from the number field in your output from file \#14.4
10. Repeat step 9 for each item in the output from file 14.4
11. Once all pending jobs have been requeued, then you are done.

Example Screen Capture of Manual Clean –up Step 3:

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: TASKS// 14.8 TASK SYNC FLAG (223 entries)

EDIT WHICH FIELD: ALL// NAME

THEN EDIT FIELD:

Select TASK SYNC FLAG NAME: ORW0;3040101;E~ORW/PXAPI RESOURCE

NAME: ORW0;3040101;E~ORW/PXAPI RESOURCE Replace @

SURE YOU WANT TO DELETE THE ENTIRE 'ORW0;3040101;E~ORW/PXAPI RESOURCE' TASK S

YNC FLAG? Y

(Yes)

Select OPTION NAME: TASKMAN MAN

1 TASKMAN MANAGEMENT XUTM MGR Taskman Management menu

2 TASKMAN MANAGEMENT UTILITIES XUTM UTIL Taskman Management Utilities menu

CHOOSE 1-2: 1 XUTM MGR Taskman Management menu

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

Cleanup Task List

Print Options Recommended for Queueing

Select Taskman Management Option: Requeue Tasks

Task Number: 150124

150124: DQSAVE^ORWPCE1, Data from CPRS to PCE. Device ORW/PXAPI RESOURCE.

DVF,DEV. From Today at 11:10, By you. Being prepared.

Requeue for what time: NOW// (JAN 17, 2005@11:16:38)

Do you wish to change the Device the task goes to:? No// NO

Task requeued!

Once All Task numbers identified that end with E and have a status of 4 in Step 2 above have been requeued as outlined in “Manual Clean-up Step 3”, the manual clean up is complete.

Notifications / Alerts

Change in Notification Date Format - Developers changed the format of notifications and alerts from displaying the year first (2004/03/22) to display it last (03/22/2004)

CCOW

- Problem with Synchronizing Patients in Test and Production Accounts (NOIS HIN-0404-40973, HEH-0304-41674, AUG-0304-32696, LOU-0404-40570) – Developers corrected a problem that allowed a user to synchronize to the same patient in both the production and mirrored test accounts with two different instances of CPRS. CPRS now distinguishes between test and production accounts and no longer allows synchronization between the two. Also, if a user is running CPRS in a test account and brings up the same patient in Care Management in a production account and selected Go to Chart, a new instance of CPRS for the selected patient is launched in the production account. The opposite is also true, if the user had CPRS open in production and opened Care Management in test and selected Go to Chart, a new instance CPRS would launch in the test account. The CPRS fix works with the fix in Care Management patch ORRC\*1\*1.
- Context Problem Could Present Incorrect Data (PSI-04-054) – Developers fixed a problem affecting users holding the ORELSE key and with the site parameter OR SIGNATURE DEFAULT ACTION set to "Release w/o Signature". On acceptance of a patient change request from another application, CPRS displayed the signature box before the patient change would be allowed to continue. This was incorrect CCOW behavior. But clicking CANCEL on that signature dialog then resulted in the previous patient's orders still being listed on the Review/Sign Changes screen for the newly synchronized patient. This now works correctly.

Problems

- Display of Problem List Items Corrected – Developers corrected the count of problems displayed to read "0 of 0" if no problems are found for the patient.
- Problems Tab Not Clearing on Cancel (NOIS MAC-0904-60407 PSI-04-048) - If a user was editing a problem and attempted to select a new patient before saving the changes, CPRS prompted the user to either "Discard Changes or Cancel". If the user selected "Cancel", CPRS would bring up the new patient’s record, but the problem edit screen was not cleared. If the user went to the Problems tab for the new patient, CPRS was still displaying the previous entry underway for the previous patient. The problem has been corrected.
- Problems Tab Not CCOW-Aware - If a user were editing a problem and a patient change request were received from another application, the user was not advised of the consequences of accepting the patient change before saving the problem changes. The problem has been corrected.

Labs

Lab Panel Results Incorrectly Passing Information to Care Management (NOIS MAN-0304-10554) - If a test in a lab panel is resulted as critical or abnormal and verified, the headlight color in Care Management displays appropriately as a red square. If lab verifies a different test in the same panel at a later time as normal, the headlight color reverts to blue due to the overwriting of the abnormal result flag stored with the order. Developers corrected this problem so that the abnormal flag is maintained and the headlight display in Care Management is correct.

Section 508 Changes, Font and Window Size Issues

Labs Tab

- Labs Test Window Focus - If you cancel out of the Select Lab Tests window, the focus now remains on the correct Lab test.
- Lab Info Box Display (NOIS MAC-0903-60683, PSI-04-023) - The Lab Info Box now displays its text at the top not the bottom.

About Dialog

The tab order now starts on the first Text object. And the user can tab through all of the text, not just part of it. This allows screen readers to read the text.

Copy Orders Dialog

The text displayed can now be tabbed to and read by screen readers. The tab order has also been fixed, and the listbox that appears, now has a label so the screen reader user will know what he or she is tabbing into.

Radiology Orders Dialog

Imaging Message Box Display (NOIS RIC-0204-22248, PAL-0704-60893, PSI-04-042) - The imaging message text box will now display text at top not the bottom. Also, there was a problem where scroll bars did not appear preventing users from viewing all the text in the message box. Developers corrected this and users can now view all the text.

General: Listboxes & Comboboxes

Listboxes and comboboxes now by default select the first Item in the list when no item has been previously selected and the control did not gain focus from a mouse click.

Multiple Dialogs

Dialogs Now Correctly Save Their Size & Positioning - Forms that save their size & positioning now use a common Object to save the data to rather than making an RPC call every time the form is open and closed. Then one call is made when the application closes saving the data with 1 RPC call. Users should not notice any differences, but overall server (m-side) performance should improve slightly.

<u>  
Provider</u> <u>&</u> <u>Location</u> <u>For</u> <u>Current</u> <u>Activities</u> <u>Dialog</u>

- JAWS now reads the Clinic Appointments/Visits list caption correctly.
- Correct Navigation for Location on the Current Activities Form - You can now navigate to the Hospital Admission and New Visit tabs using the keyboard.
- Location for Current Activities Now Uses Correct Focus - In connection with the “Location for Current Activities Form”, the New Visit tab no longer automatically changes focus to the edit box.

Notes Tab

- List Selected Documents Window JAWS Change - JAWS will now read the "Where Either Of" in the bottom section of the window. To test, use ALT-V-M on the Notes Tab, this brings up the List Selected Documents window.
- Corrected Tabbing - When Editing/Creating a Note you can now tab to drawer buttons.
- Drawers Navigation Corrected - Previously, users could get to the hidden drawer buttons by using the arrow keys when the buttons are hidden. Developers disabled navigating the drawer buttons with the arrow keys, so that the visually impaired users don’t have problems.
- Corrected Focus Problem after User Signed a Note - After a user signed a note, the note is removed from All Unsigned Notes pane. Previously, CPRS did not then focus on the Note TreeView. Now, the first Item in the TreeView gains focus.
- Notes Properties Dialog - Date Range dialog boxes now highlight the text when they receive focus.
- New Note Tab Order Corrected - Using Shift+tab now moves backwards in the tab order correctly from New Notes.
- Tabbing Problems Corrected - All controls on the Notes Tab can now be accessed with Tab and Shift + Tab.

Encounter Form

Users can now use the keyboard to access the tabs on the encounter form.

Meds Tab

Developers added code to save user settings when the location of the splitters is changed. The Non-VA Meds display also now resizes when the user resizes the form vertically.

Problems Tab

- Overlay Problem Corrected – Previously, if the user opened the New/Edit Problem window, the View Options and Problem Categories were overlaying each other. This has been corrected. The tab order now stays consistent afterwards also.
- Service Edit Box Correction - If a user selected the Service edit box in the Change Problem window, JAWS spoke something strange. This has been corrected.
- Buttons Not Visible on Problems Edit Form - Developers added 3 panels to the form. The form can now handle all the font sizes above 8.
- Problem Lexicon Search Dialog Focus Corrected - Developers corrected the focus on the Problem List Lexicon Search so that after a search CPRS sets the focus to list box.
- Font Resizing Warning Added to the Edit/Add Problem Dialog - The Add/Edit Problem Dialog has to be closed to change font sizes. If this dialog is open when the user tries to change font sizes, CPRS now displays a message telling the user that they need to close the Edit/Add Problem dialog to change the font size and CPRS does not allow the font to resize until the dialog is closed.
- Text Moved to Correct Font Problem - Developers moved the "No Problems Found" text to the "Description" column to correct some font resizing issues.
- OK Button Now Visible on Problems Add Entry Form (NOIS BUT-0704-21314, PSI-04-039) - If the font size on the Problem List Entry is greater than 8, the user is unable to access the OK button to accept the new problem.

Non<u>-Modal</u> Dialogs

Previously, if a user was in a non-modal dialog (one that allows you to also work on the CPRS window behind it) and the user changed to another application and back to CPRS, the focus was no longer on the dialog. Developers made a change and now non-modal dialogs keep their focus when the user switches to another application and comes back into CPRS.

Review<u>/</u>Sign Changes and Sign Orders <u>Dialogs</u>

- Text No Longer Absent When Form Resized - "Signature will be applied to checked items" label no longer disappears when the form is resized.
- Changes to Enable Better Focus Tracking – Previously, it was difficult to tell what control (button, field, etc.) had focus when tabbing through the controls on the Review / Sign Changes and Sign Order dialogs. Developers created a new dialog component to correct the (TORStaticText). Now, when a user tabs to different controls, the on-screen text displays in bold font when the corresponding control has focus.
- Keyboard Shortcut for Signature Screens - Developers added an Alt+S hot-key to the Sign Orders and Review/Sign Changes dialogs to allow a user to move the focus to the first order, regardless of where the focus currently is.
- Question Marks that Were Not Spoken Now Cleared - When the checkboxes on the CIDC sign orders grid gains focus using the Tab key, the blue question mark in the checkboxes are now being cleared. That is, if a checkbox is tabbed into using the Tab key, and that checkbox contains a question mark, that checkbox is cleared. This change was made to accommodate screen reading software that could only determine if a box was checked or unchecked, but could not speak the question mark.
- Check List Box Now Reading Correctly with Configuration File - The Window-Eyes screen reader software was not able to correctly read the Check List Box control (the ones used for indicating Treatment Factor and Service Connection information) on the CIDC Sign / Review and Sign Orders screens. To correct this problem, developers have distributed a Window-Eyes (WE) configuration file “CPRSCHAR.we” that users must install in the “WINEYES\Users\Default” directory on the machine running WE. Then, it will read the Check List Box.

Remote Data

- Tabbing Changed for Remote Data Views - Previously, the Remote Data Views ListBox did not respect tabbing. It now acts correctly. You can tab to the Remote Data button, use the \<Spacebar\> to open the list of sites, and navigate to the list of sites using the Tab key.
- Remote Data Views Shortcut Key – Users can now toggle the Remote Data button using Alt+R.

Consult Dialog

- Consults Keyboard Navigation Corrected - Now a user can browse Service/Specialty with up and down arrows and select a service or specialty with the \<Enter\> key or space bar.
- Resizing Problem Corrected - The consults Reason for Request box and its label were not displaying or resizing properly. This has been corrected.
- Consults Order Dialog Tab Order Corrected – Developers corrected the tab order on the Consults Order dialog.

Options Dialog

Users can now use the TAB key to move between tabs on the Options dialog.

Consults, Refill, and Renew Dialogs

These dialogs now retain their size and adjust correctly for font changes.

Send Alert Form

Send Alert Window Pane Title Incomplete - The captions above the list box now display their title correctly.

Template Editor

- Template Editor Dialog Focus Problem Corrected – Previously, if the user checked the Active checkbox, CPRS did not keep the focus on the checkbox. This has been corrected. If the user checks on the Active checkbox, the focus remains on the Active check box if it can obtain focus.
- Preview Template Dialog now remembers its size.

<u>Reports</u> <u>Tab</u>

- Refresh Problem Corrected - Developers changed the tabs for individual reports to be actual tabs instead of buttons. Now when a user navigates with the arrow keys, the Remote Data Views reports will refresh.
- Date Range Cancel Error Corrected - Selected Date Range, this no longer generates an invalid date error when clicking cancel.
- Inappropriate Errors on the Ad Hoc Health Summary - Extraneous characters were displaying behind the up and down arrows on the Ad Hoc Health Summary Form.

Orders

Orders on Chart Dialog Font Problem –Developers made a change so that the form displays font sizes 10 and larger correctly.

CWAD Patient Postings Dialog

- Label Corrected and Close Button Added - Developers changed code so that screen readers now read the label at the top of the allergies list box. Developers also added a Close button.
- Imaging Order Dialog Problem Corrected - Developers fixed the Imaging type combobox so that Window-Eyes now reads it correctly.

JAWS Screen Reader Compatibility

JAWS Not Correctly Reading Some CPRS Controls – Developers made a change to the JAWS definition files so that it correctly reads custom list boxes like on the Meds tab. To correct the problem, developers added TCaptionListBox=MS Active Accessibility to the Windows Classes definition, in the JAWS definition file.

<u>Consults</u> <u>Tab</u>

- Screen Reader Reading Hidden Controls - Developers corrected a problem so that screen Readers no Longer read two hidden controls when the user navigates from the New Consult button using the arrow keys.
- Screen Readers Unable to Access Print Screen Text - On the Consults tab Print Screen (Alt-A-C-P), users can now tab to the text of the Print Screen, and screen readers have access to the text.
- Prerequisite Screen Button Overlap - When a uses ordered a consult from a menu, if the font size was changed the Continue and Cancel buttons on the Prerequisite Screen overlapped. Developers have corrected this.
- Tab Order Corrected – Developers corrected the tab order on the Consults Order form.
- Navigation Corrected - A JAWS screen reader user was trying to work with consults, but was having trouble getting the focus were it needed to be. After the user selected a Consult type, the focus went to the Patient Info button on the main header. Because the focus went to Patient Info after the user selected a Consult, when a JAWS user then used \<Spacebar\>, the Patient Inquiry dialog would appear and focus would never land on the Notes field as it should. Developers corrected this so that the Notes field gets focus instead.

<u>Reminders Dialog</u>

- Reminder Dialog Font Resize Warning Added - Reminder dialogs must be closed to change font sizes. If a dialog is open when the user tries to change font sizes, CPRS now displays a message telling the user that they need to close the Reminder dialog to change the font size and CPRS does not allow the font to resize until the dialog is closed.
- Reminder Dialog Now Saves Size and Location (NOIS HOU-0104-70560) – The Reminders dialog now saves its last size and position and opens there the next time it opens.
- Reminder Dialog Checks Indent Progress Note (NOIS PUG-1203-51384) - The Reminder Dialog looks only at the Indent Progress Note to determine if a Dialog Group sub items should be indented in the Progress Note.

Patient lookup Dialog

Developers corrected the font resizing issue.

Discharge Summaries

When a discharge summary is NOT selected, the Alt+A+C combination will now cause the 'No Summary Selected' window to appear when the Alt+A+C option is not disabled.