---
title: Anticoagulation Management Tool User Manual
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: Anticoagulation Management Tool
app_code: AMT
app_name: Anticoagulation Management Tool
section: CLI
app_status: active
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
  - patient
  - anticoagulation
  - table
  - contents
  - tool
  - management
  - visit
  - date
  - manual
  - other
page_count: 0
word_count: 7545
section_count: 9
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: March 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Anticoagulation_Management_Tool/am_oramum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Anticoagulation_Management_Tool/am_oramum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=188"
---

---
title: <span id="_Toc495855387" class="anchor"></span>
---

Anticoagulation Management Tool

User Manual

(Patch OR\*3.0\*600)

![](anticoagulation-management-tool-user-manual/001.png)

Initial Release: March 2010

Revised: February 2024

Office of Enterprise Development

Revision History

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 54%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description of Change</th>
<th>Authors</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Feb 2024</td>
<td><p>Patch OR*3.0*600</p>
<p>Added Anticoagulation Team Patient List to the <a href="#anticoagulation-team-patient-list">First Visit</a> and <a href="#anticoagulation-team-patient-list-1">Subsequent Visits</a> sections.</p>
<p>Updated title page, footer, and table of contents</p></td>
<td>CPRS development team</td>
</tr>
<tr class="even">
<td>Feb 2018</td>
<td>Patch <a href="#OR_3_447_2018Feb">OR*3.0*447</a> – Updated “Note” under “Steps for Using this Tool” to include the 2FA changes.</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>Mar 2015</td>
<td>Patch OR*3*391 – ICD-10 Remediation changes.</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>Sept 2013</td>
<td>Patch OR*3.0*354</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="odd">
<td>Sept 2011</td>
<td>Patch OR*3.0*339</td>
<td><mark>redacted</mark></td>
</tr>
<tr class="even">
<td>Mar 2010</td>
<td>Initial Release</td>
<td><mark>redacted</mark></td>
</tr>
</tbody>
</table>

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Related Manuals](#related-manuals)
- [Steps for Using this Tool](#steps-for-using-this-tool)
  - [First Visit](#first-visit)
    - [![](anticoagulation-management-tool-user-manual/003.png)With the new patient selected in CPRS, select Anticoagulation from the Tools menu](#anticoagulation-management-tool-user-manual003pngwith-the-new-patient-selected-in-cprs-select-anticoagulation-from-the-tools-menu)
    - [![](anticoagulation-management-tool-user-manual/004.png)A confirmation dialog appears, respond Yes](#anticoagulation-management-tool-user-manual004pnga-confirmation-dialog-appears-respond-yes)
    - [Fill in Demographics Tab](#fill-in-demographics-tab)
    - [Continuing to the Pt Preferences tab, update the Orientation Date and fill in the Duration](#continuing-to-the-pt-preferences-tab-update-the-orientation-date-and-fill-in-the-duration)
    - [Continue to the Enter Information tab](#continue-to-the-enter-information-tab)
    - [Leave the program through the Exit tab](#leave-the-program-through-the-exit-tab)
  - [Subsequent Visits](#subsequent-visits)
    - [Patient Selection](#patient-selection)
    - [Demographics Tab](#demographics-tab)
    - [Pt Preferences Tab](#pt-preferences-tab)
    - [Flow Sheet Tab](#flow-sheet-tab)
    - [Enter Information Tab](#enter-information-tab)
    - [Note: Dosing calculation warns if dosing exceeds maximum daily dose.](#note-dosing-calculation-warns-if-dosing-exceeds-maximum-daily-dose)
    - [Complications Tab](#complications-tab)
    - [Exit Tab](#exit-tab)
    - [Note: If you are creating an intake note and there is a pending consult request, Anticoagulator will display a dialog asking if you want to use complete the consult. The Anticoagulator can complete the consult regardless of consult status.](#note-if-you-are-creating-an-intake-note-and-there-is-a-pending-consult-request-anticoagulator-will-display-a-dialog-asking-if-you-want-to-use-complete-the-consult-the-anticoagulator-can-complete-the-consult-regardless-of-consult-status)
    - [When the dialog displays asking if you want to complete the consult, select yes.](#when-the-dialog-displays-asking-if-you-want-to-complete-the-consult-select-yes)
    - [Select the Consult you want to complete and select OK.](#select-the-consult-you-want-to-complete-and-select-ok)
    - [Sign the Note.](#sign-the-note)
    - [The consults is completed without any other intervention.](#the-consults-is-completed-without-any-other-intervention)
    - [Utilities Tab](#utilities-tab)
- [Reporting](#reporting)
  - [In VistA](#in-vista)
  - [In CPRS](#in-cprs)
- [Frequently Asked Questions](#frequently-asked-questions)
  - [Urgency](#urgency)
  - [Reporting Time](#reporting-time)
  - [INR Graph](#inr-graph)
- [Glossary](#glossary)
- [Appendix A: Patient Care Encounter Considerations](#appendix-a-patient-care-encounter-considerations)
- [Index](#index)
This tool was developed at the Portland VA Medical Center to help simplify the complex, time consuming processes required to manage outpatients on anticoagulation medication.
With the Anticoagulation Management Tool, you can:
- Order lab tests
- Enter outside lab results
- Review lab data
- Make an appointment
- Enter and sign progress notes
- Complete encounter data
- Complete the consult if consults are used to initiate entry into the Anticoagulation clinic
- Print a variety of patient letters
Upon exiting the program all activities within the program are recorded on an Anticoagulation flow sheet maintained on the Computerized Patient Record System (CPRS) Reports tab. The Anticoagulation Tracking provides clinic staff a mechanism of ensuring continuous patient monitoring *with a built-in mechanism that alerts staff when patients haven’t been monitored in a timely period.* A Lost to Follow-up list is maintained to ensure that staff knows of patients who need attention.
The tool uses the international normalized ratio (INR) for measuring blood clotting, excluding all other measurements. This is because the result (in seconds) for a prothrombin time performed on a normal individual varies depending on what type of analytical system is used. This is due to the differences between batches of the manufacturer's tissue factor used in the reagent to perform the test. The INR standardizes the results.
INR is the ratio of a patient's prothrombin time to a normal (control) sample, raised to the power of the International Sensitivity Index (ISI) value for the analytical system used. Each manufacturer assigns an ISI value for any tissue factor they manufacture. (This value indicates how a particular batch of tissue factor compares to an internationally standardized sample. The ISI is usually between 1.0 and 2.0.)
> ![](anticoagulation-management-tool-user-manual/002.png)

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two other manuals that give information on the Anticoagulation Management Tool. They are both much more technical than this manual and intended for use to set up and modify the tool. These are:

> *Anticoagulation Management Tool Installation Guide*

> *Anticoagulation Management Tool Technical Manual*

# Steps for Using this Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## First Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ![](anticoagulation-management-tool-user-manual/003.png)With the new patient selected in CPRS, select Anticoagulation from the Tools menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ![](anticoagulation-management-tool-user-manual/004.png)A confirmation dialog appears, respond Yes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note:

| ![](anticoagulation-management-tool-user-manual/005.png) | <span id="OR_3_447_2018Feb" class="anchor"></span>*OR\*3.0\*447 updated the Anticoagulation Tool to become two factor authentication (2FA) compliant. You may be asked to reenter your PIV credentials at this time. If the SSOi service is down or disabled, you will instead be prompted for your Access Code and Verify Code. The Anticoagulation Tool is not Clinical Context Object Workgroup (CCOW) enabled, so your Information Resource Manager (IRM) must explicitly allow Auto Sign-on through Kernel and Systems Manager Menu (EVE) settings for you to repeatedly enter the tool without re-authentication.* |
|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Fill in Demographics Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Fields in yellow must be addressed this first time through. Other fields, such as the Clinic Name may also be filled in:

#### Clinic Name

> If it is not automatically filled in, you must enter information in the Clinic Name field. If there is more than one clinic at your site they are all represented in a dropdown list.

> ![](anticoagulation-management-tool-user-manual/006.png)

#### Indication

How the indications work at your site and for your clinic will depend on the set up that occurs at your site. If no defaults are set, the dialog will look like the screen capture above.

The application can be set up to use a default primary indication, a default secondary indication, or both a default primary and secondary indication. The application has a way to enter a default primary indication (For Therapeutic Drug Monitoring (V58.83) as recommended by American Hospital Association and the VA’s Pharmacy Benefits Management). Your site can also set up a default secondary indication (Long Term Current Use of Anticoagulants (ICD-9-CM V58.61)). The dialog will look like the screen capture below when the user selects a clinic name.

![](anticoagulation-management-tool-user-manual/007.png)

If the clinic is set up to use the defaults, when you fill in clinic name, the Primary and Secondary indication is automatically filled in. You can add an Additional indication if wanted or needed.

#### ICD-9 Codes

Currently, using ICD-9 codes, there are ten (10) additional indications hard-coded into the program and the Other option through which users can enter a different ICD-9 code. The ICD-9 codes are listed below by the display text and code followed by the ICD-9-CM description.

Add’l Indications can be set thus:

- A Fib (427.31): Atrial Fibrillation
- A Flutter (427.32): Atrial Flutter
- Antiphospholipid Antibodies (286.9): Coagulat Defect NEC/NOS (CC)
- Antithrombin III Deficiency (286.9): Coagulat Defect NEC/NOS (CC)
- Apical Thrombus (429.79): Other Sequelae of MI NEC (CC)
- Arterial Thrombosis (444.9): Arterial Embolism NOS (CC)
- CAD (Coronary Art Dis) (414.00): Cor Atheroscl Unsp Typ-Ves
- CHF (Cong Heart Fail) (428.0): Congest Heart Fail Unspecified
- CVA (437.9): Cerebovasc Disease NOS
- Cardiomyopathy (425.4): Prim Cardiomyopathy NEC (CC)
- Carotid Stenosis – Plaque (433.10): Occl & Sten/Car Art w/o CRB Inf
- Cerebrovascular Disease (436): Acute but ill-defined cerebrovasc disease
- Clotted Graft (996.74): Comp-Oth Vasc Dev/Graft (CC)
- DVT (453.89): Acute ven emb and thromb oth spec veins
- Enctr for Tx Drug Monitoring (V58.83): Encounter for therapeutic drug monitoring
- Hypercoag state (289.81): Primary hypercoagulable state
- L/T (Current) Anticoag Use (V58.61): Long-term (Current) use of anticoagulant

> Note: This will only display in the list if it is not already assigned as a default secondary indication.

- LV Thrombus (429.79): Other Sequelae of MI NEC (CC)
- Mesenteric Thrombosis (557.0): Occl & Sten/Car Art w/o CRB Inf
- PAD (Peripheral Art Dis) (443.9): Periph Vascular Dis NOS
- PE(415.19): Other pulmonary embolism and infarction
- Prophylaxis S/P Ortho Surgery (V54.89): Other Orthopedic Aftercare
- Recurrent DVT (453.79): Chronic Embolism Veins NEC (CC)
- Recurrent PE (416.2): Chronic Pulmonary Embolism (CC)
- TIA(435.9): Unspecified transient cerebral ischemia
- Valve-Mech (V43.3): Heart valve replaced by other means
- Valve-Tissue (V42.2): Heart valve replaced by transplant
- Other allows you to enter an International Statistical Classification of Diseases, Ninth Revision (ICD-9) code. All the others already supply the appropriate ICD-9 code to workload. If you use Other, make sure you have the current ICD-9 code to enter into the dialog.

In the near future (currently scheduled for October 1, 2015), the VA will discontinue use of ICD-9 and begin using International Statistical Classification of Diseases, Tenth Revision (ICD-10) codes. This patch provides the ICD-10 codes to support Anticoagulation Management and enables facilities to specify an ICD-10 diagnosis that will be filed automatically as the Primary Indication for Care at each Anticoagulation clinic location for visits which occur after ICD-10-CM implementation and one that can be filed as a secondary indication for care. There are also the additional indications.

![](anticoagulation-management-tool-user-manual/008.png)

#### ICD-10 Codes

The available ICD-10 codes (in the format of *Display Text (code): description*) under Add’l Indications are listed below:

- A Fib (I48.91): Unspecified atrial fibrillation
- A Flutter (I48.92): Unspecified atrial flutter
- Act Prot C Res (D68.51): Activated protein C resistance
- Acute MI (within 4 weeks) (I21.3): ST elevation (STEMI) myocardial infarction of unsp site
- Antiphospholipid Synd (D68.61): Antiphospholipid syndrome
- CVA (unspecified sequela) (I69.30): Unspecified sequelae of cerebral infarction
- Cerebrovascular Disease (I67.89): Other cerebrovascular disease
- DVT Bilat LE Unspec Veins (I82.403): Acute embolism and thombos unsp deep veins of low extrm, bilat
- DVT LLE Unspecified Veins (I82.402): Acute embolism and thombos unsp deep veins of left low extrem
- DVT RLE Unspecified Veins (I82.401): Acute embolism and thombos unsp deep veins of right low extrem
- DVT Uspec veins, unspec LE (I82.409): Acute embolism and thombos unsp deep vn unsp lower extremity
- DVT oth spec veins not in LE (I82.890): Acute embol and thromb of oth spec veins
- Enctr for Tx Drug Monitoring (Z51.81): Encounter for therapeutic drug level monitoring
- Hypercoag State (D68.59): Other primary thrombophilia
- L/T (Current) Anticoag Tx (Z79.01): Long term (current) use of anticoagulant
- Lupus Anticoag Synd (D68.62): Lupus anticoagulant syndrome
- Old MI (\> 4 wks, no curr symp) (I25.2): Old myocardial infarction
- Oth Prim Thrombophilia (D68.59): Other primary thrombophilia
- PE (I26.99): Other pulm embol w/o acute cor pulmonale
- Prothromin Gene Mut (D68.52): Prothrombin gene mutation
- TIA (G45.9): Transient cerebral ischemic attack, unspecified
- Valve-Mech (Z95.2): Presence of prosthetic heart valve
- Valve-Tissue (Z95.3): Presence of xenogenic heart valve

> Note:

| ![](anticoagulation-management-tool-user-manual/009.png) | *The ICD-10-CM codes corresponding to the ICD-9-CM indications used since 2008 were identified using the General Equivalence Mappings, which are developed and maintained by The Centers for Medicare & Medicaid Services (CMS) and the Centers for Disease Control and Prevention (CDC). Note that the indication "Hypercoag State" (ICD-9-CM 289.81) may map to any of five ICD-10-CM indications (Activated protein C resistance, Antiphospholipid syndrome, Lupus anticoagulant syndrome, Other primary thrombophilia, or Prothrombin gene mutation), and so the list is slightly larger, allowing more specificity. The remaining indications mapped more easily into ICD-10-CM in one-to-one fashion.* |
|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

- Other: When the user selects Other, the user can search for an appropriate terms using the same Lexicon search used by CPRS on the Encounter form.

![](anticoagulation-management-tool-user-manual/010.png)

Selecting Other brings up the Lookup Diagnosis dialog.

The user then types part or all of a term to search for (in the example below, the search text is “mesenteric throm”.

![](anticoagulation-management-tool-user-manual/011.png)

After the user selects search, the application will search for possible matches and display them in the term pane as shown below:

![](anticoagulation-management-tool-user-manual/012.png)

The user then selects the appropriate term and it displays in the Add’l Indication field.

![](anticoagulation-management-tool-user-manual/013.png)

The appropriate code will be sent to PCE as a secondary indication. The area below is actually on the Exit tab.

![](anticoagulation-management-tool-user-manual/014.png)

#### Goal

The Goal is expressed as an INR range. The ranges 1.5 to 2.5, 2.0 to 3.0, and 2.5 to 3.5 are pre-loaded into the program for your selection. If none of these reflects the goal you want, you can select other and enter Minimum and Maximum INR values.

#### Other Controls

The controls hidden by the text pane may be seen by clicking the X button. These controls are described in the [Subsequent Visits](#anticoagulation-team-patient-list) section of this manual.

### Continuing to the Pt Preferences tab, update the Orientation Date and fill in the Duration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This tab is important for recording primary and secondary phone numbers, and who in the household is authorized to receive information regarding the patient. The patient home and work phone are automatically filled in from the patient record. Other preference information that is known should be included at this time:

![](anticoagulation-management-tool-user-manual/015.png)

Takes meds in A.M. is a reminder about this patient’s schedule.

Eligible for LMWH Bridging sets a flag in the flowsheet to indicate that the patient is at higher risk for thromboembolic events. The patient should be bridged with Low Molecular Weight Heparin (LMWH) to reduce the time window during which the patient has a low prothrombin time when warfarin is withheld for invasive procedures. If this box is checked a dialog opens to allow you to enter comments. Both the flag and the comments are entered into the flowsheet report.

Signed Agreement is for local use. Not all medical centers have a treatment agreement. If your hospital or clinic has one, this field can be used to indicate the patient has signed one.

Restrict draw days pops up a dialog so that you can enter days of the week that a draw should not be scheduled. The program will enforce this restriction and also display the No draws on information on subsequent uses of the program.

Pt has given permission to leave anticoag msg on msg machine is set if the patient has given explicit permission to leave an anticoagulation message on his or her message machine.

Pt has given permission to leave msg with person(s) listed below: Allows you to list the names of people who the patient has given explicit permission for the clinic to leave anticoagulation messages.

Special Instructions: Leaves a place for you to enter persistent information about this patient that is important for the treatment team to remember. Home Phone and Work Phone are automatically filled in here form the patient’s medical record.

Secondary Indication(s)/Risks: Is a place to record risk factors that specifically bear on anticoagulation treatment of this patient. Also, if the patient has important secondary indications they should be listed here.

Start Date: Was automatically filled in during the first invocation of this program for this patient. It may be changed by the user at any time.

Stop Date: Is automatically filled in when d/c from clinic is checked.

d/c from clinic is checked when the patient’s treatment is discontinued.

Orientation Date: Is automatically filled in when the program is initially run for this patient. It may be changed at any time, especially if the first visit did not correspond to the patient’s orientation.

Level of complexity: Allows the user to stratify less stable patients to a higher priority team list for closer monitoring. Complex should be defined locally, but indicates a condition that requires closer monitoring than a routine patient. Consideration for Complex status might be:

- New starts
- Patients interrupting therapy for surgery
- Patients with drug interactions

Save/Exit is disabled for a first time patient. You must go through to the Exit tab in order to create a record in the Anticoagulation Flowsheet file.

Apply saves the data on the tab and allows you to go on to other tabs and complete the visit. Visit completion is done on the Exit tab.

### Continue to the Enter Information tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter Information is really three tabs: Enter Outside Lab Data, New Flow Sheet Entry, and Complications.

![](anticoagulation-management-tool-user-manual/016.png)

Enter information that is important from the patient encounter.

- You will need to use the Enter Outside Lab Data tab if the INR and/or hematocrit (HCT) is reported from a site other than your VA facility.
- You may need to use the Complications tab to document bleeding or thromboembolic events.
- You will need to use the New Flow Sheet Entry to enter comments on this visit and to change the dosage schedule. You can also indicate if the patient missed the appointment.

#### Using the Missed Appointment Button

> **IMPORTANT:** If a patient misses an appointment, use the Missed Appt. button on the New Flow Sheet tab. It is located next to the Pt. Notice field. If you select this button, AMT sets a flag that shows that the patient missed the appointment as shown below:

![](anticoagulation-management-tool-user-manual/017.png)

By using the Missed Appt. button, the Utilities tab correctly reflects a missed appointment instead of the last seen. The application also properly changes the flow sheet within the AMT based on an INR that pre-dates a missed appointment.

### Leave the program through the Exit tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first time through, the following reminder appears:

![](anticoagulation-management-tool-user-manual/018.png)

By clicking OK the following dialog appears:

![](anticoagulation-management-tool-user-manual/019.png)

![](anticoagulation-management-tool-user-manual/020.png)

You can toggle back and forth between the note edit and the rest of the Exit Tab by pressing the Cancel button/Intake Note button on the bottom of the tab.

All information necessary to track this patient is kept in the Anticoagulation Flowsheet file and is accessible through the Anticoagulation Management Tool. The tool only presents a clinical note during intake and discontinuation (D/C). If you want to create a clinical note for each visit, use the Interim Note button on the bottom of the Exit Tab.  
You must leave the program though the Exit tab to save the data you have entered and to properly record workload information.

![](anticoagulation-management-tool-user-manual/021.png)

The Anticoagulation Management Tool does not use the appointment system. It assumes either telephone contact or a walk-in clinic visit on the date of the scheduled lab draw.

#### Patient Letter

If the Complete Visit or Missed Appointment button under Letters is selected, a dialog opens that contains controls for you to customize the letter:

![](anticoagulation-management-tool-user-manual/022.png)![](anticoagulation-management-tool-user-manual/023.png)

#### Anticoagulation Team Patient List 

When exiting the program, the user must complete the current patient’s visit. When the visit is completed, the patient is either retained or removed from the Anticoagulation Team list.

A patient remains on the list if:

- The INR draw date is the current day or any day preceding the current date for completed visits. This including completed backdated visits.
- If there was a Temp Save made on the patient. Temp Saves are made on current day’s date for INR Draw.

A patient is removed from the list if:

- The INR Draw date is scheduled any day after the current date with Completed Visits.
- The INR Draw date is scheduled any day after the current date with Completed Visits featuring Next Day Call Back
- 

## Subsequent Visits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Patient Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a patient is entered into the Anticoagulation Management Tool by following the instructions in [First Visit](#first-visit) above, the patient is in the system. This means that when the date of the next scheduled INR visit comes around, a nightly task puts the name on one or both of the Anticoagulation Team lists. The lists should be labeled (all) or (complex) and may have a different name than that shown in the example. (Note that the team lists used for your clinic may be different from the ones in this example depending upon your local setup.)

Here is a portion of the CPRS Patient Selection dialog showing the selection of a Anticoagulation Management patient.

![](anticoagulation-management-tool-user-manual/024.png)

On subsequent visits by the client, the tool is always entered through the Demographics tab (unless the record was temp saved, then it goes directly to the New Flow Sheet Entry sub-tab of the Enter Information tab). Instead of a list of things to do, the clinician is presented with a graph showing all INR readings in the patient file, as well as % in goal of INRs reported since the first visit, the visit show rate, and the date of the last hematocrit (HTC) or hemoglobin (Hgb):

![](anticoagulation-management-tool-user-manual/025.png)

From here you may proceed to the other tabs as necessary. If you are completing the visit, you should at least go to the Enter Information tab where the visit comments can be filled out. To complete a visit you need to exit through the Exit tab to schedule the next INR draw and complete Patient Care Encounter information.

In the following sections each tab is presented and features that are useful during subsequent visits are explained.

### Demographics Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Demographics Tab has two controls you can use:

![](anticoagulation-management-tool-user-manual/026.png)

#### Switch Button

This button switches the Percent in Goal from ALL to stable. ALL includes all readings displayed. Stable only calculates Percent in Goal for INRs reported when the patient was in Routine (not Complex) status.

#### Set Reminder Button

The Set Reminder button allows you to set a reminder that comes up when the tool is entered for the current patient. This permits the communication of important patient information with other members of the anticoagulation team.

![](anticoagulation-management-tool-user-manual/027.png)

The Reminder Date must be set to any future date and is the first date the reminder will pop up. The reminder will continue to pop up when the tool is invoked for this patient until it is cleared or a new reminder is entered.

The Reminder Text is for you to type any message you would like future users to have about this patient.

The three buttons perform the obvious chores: Clear Reminder, OK to, and Cancel to get out of the dialog without making any changes.

After a reminder has been set, the button caption will change to View Reminder.

### Pt Preferences Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pt Preferences tab has the following controls:

Takes meds in A.M. is a reminder about this patient’s schedule.

Signed Agreement is for local use. Not all medical centers have a treatment agreement. If your hospital or clinic has one, this field can be used to indicate the patient has signed one.

No draws on pops up a dialog so that you can enter days of the week that a draw should not be scheduled. The program will enforce this restriction and also display the No draws on information on subsequent uses of the program.

Eligible for LMWH Bridging allows you to enter comments for the medical record if Low Molecular Weight Heparin (LMWH) bridging is imminent. A text box opens and you can type instructions relating to this therapy.

Pt has given permission to leave anticoag msg on msg machine is set if the patient has given explicit permission to leave an anticoagulation message on his or her message machine.

Pt has given permission to leave msg with person(s) listed below: Allows you to list the names of people who the patient has given explicit permission for the clinic to leave anticoagulation messages.

Special Instructions: Leaves a place for you to enter persistent information about this patient that is important for the treatment team to remember. Home Phone and Work Phone are automatically filled in here form the patient’s medical record.

Secondary Indication(s) / Risks: Is a place to record risk factors that specifically bear on anticoagulation treatment of this patient.

Include in Note? if checked includes the contents of the Secondary Indications(s) / Risks field in the clinical note.

Start Date: Was automatically filled in during the first invocation of this program for this patient. It may be changed by the user at any time.

Stop Date: Is automatically filled in when d/c from clinic is checked.

d/c from clinic is checked when the patient’s treatment is discontinued. Once this is checked, Inactive Patient appears at the top of the window next to the patient’s name.

> **NOTE:** | ![](anticoagulation-management-tool-user-manual/028.png) | If a patient is being transferred to another anticoagulation clinic, check this box, exit the flowsheet, then reenter the Anticoagulation Management Tool. On reentry you can enter the new clinic in the Demographics tab. |
|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Orientation Date: Is automatically filled when the program is initially run for this patient. It may be changed at any time, especially if the first visit did not correspond to the patient’s orientation.

  
Level of complexity: Allows the user to stratify less stable patients to a higher priority team list for closer monitoring. Complex should be defined locally, but indicates a condition that requires closer monitoring than a routine patient. Consideration for Complex status might be:

- New starts
- Patients interrupting therapy for surgery
- Patients with drug interactions

Save/Exit saves the information on the tab without completing the visit. It can be used to update demographic or preference information on a patient. Restricted draw days are not saved unless the visit is completed.

Apply saves the data on the tab and allows you to go on to other tabs and complete the visit. Visit completion is done on the Exit tab.

### Flow Sheet Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This tab gives a detailed listing of INR tests in the patient record. The Edit button allows you to edit any information in the table. This is especially useful if an obvious error has been made, or additional information relevant to the patient visit becomes available after completion of the encounter (e.g., the patient calls back to report a missed dose):

![](anticoagulation-management-tool-user-manual/029.png)

### Enter Information Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter Information tab is really three tabs: Enter Outside Lab Data, New Flow Sheet Entry, and Complications.

#### Enter Outside Lab Data

This tab is used when the patient is getting INRs from a source other than the medical center’s lab facility.

![](anticoagulation-management-tool-user-manual/030.png)

#### New Flow Sheet Entry

This sub-tab of the Enter Information tab is used to enter comments about the visit and to change the medication schedule, if necessary.

![](anticoagulation-management-tool-user-manual/031.png)

This sub-tab has the following controls:

Pt Notice: Documents the typical way communication occurs with the patient. One medical center uses V for clinic visit, M for message, and P for phone contact. This is a clear text field, so can receive any code or phrase agreed upon by tool users.

Missed Appt button sets the Missed Appointment flag in the Anticoagulation file. This is used by the program to calculate the Show Rate given on the Demographics tab.

Clear INR deletes the current INR reading. After this has been clicked, the button reverts to undo, which restores the INR reading.

OK the comment entered.

Cancel clears the INR information.

Pill Strength: Allows you to enter a pill strength other than 5 mg. Five mg is the default because most medical centers only stock that pill strength.

Change daily dosing activates entries in the New Daily Dosing fields. You may change either tablets or milligrams (mgs) and the corresponding entry is updated based on the Pill Strength. Press OK to go forward with these setting or Cancel to restore the original values.

### Note: Dosing calculation warns if dosing exceeds maximum daily dose. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To change tablet strength, check here.

![](anticoagulation-management-tool-user-manual/032.png)

If the dosage seems excessive, Anticoagulator asks you if you wish to exceed 30 milligrams per day.

![](anticoagulation-management-tool-user-manual/033.png)

Record total weekly dose check if you want the weekly total to appear in the flow sheet; in cases, like complex patients where the dose is still being adjusted, this can be unchecked so these transition dosages are not reflected on the flowsheet.

### Complications Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a sub-tab of the Enter Information tab. It contains the following controls:

Date of complication: Is automatically filled in with today’s date. It can be changed if the complication occurred previously.  
The following check boxes are included. All that apply may be checked:

- Death
- Requiring transfusion of 2 or more units
- Resulting in hospitalization
- Drop in hemoglobin of 2mg/dl or more
- Bleed into critical area or organ
- Other (add comment)
- Minor
- Complication Comment
- Thrombotic event: EXPLAIN

If Complication Comment and/or Thrombotic event is checked, a dialog opens for entry of a text comment.

File complication and EXIT button is selected if the information was received at other than a visit (phone or clinic). This will put the complications information into the patient record and immediately exit the tool.

File on completion button is selected when it is a regular clinic or phone visit. This allows you to go on to the Exit tab to complete the visit.

Cancel has the obvious meaning.

### Exit Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This tab allows you to set a date for the next appointment, complete workload information, generate letters for the patient, and complete the visit.

#### Set Date for the Next Appointment

![](anticoagulation-management-tool-user-manual/034.png)The patient automatically shows up on the team list for the date shown in this section of the tab. There are two buttons that automatically set this date to two weeks or four weeks. Alternatively, you can click on the down arrow and select a different date or type in a different date.

> **NOTE:** If you select a draw date that is on the weekend, a dialog displays to warn you so that you can change to a Monday draw if necessary as shown below.

![](anticoagulation-management-tool-user-manual/035.png)

#### Labs and PCE Data

The center part of the tab shows Lab order information and workload (PCE) data. If one or more of the check boxes are checked, it means that lab is automatically ordered for the Return for INR Draw date. The PCE Data includes the primary ICD-9 code that was set during the initial visit, and has a radio button for the type of visit is. Only one radio button may be selected per visit. Alternatively, you may select the Do not file data for this visit and no workload will be collected.

![](anticoagulation-management-tool-user-manual/036.png)

![](anticoagulation-management-tool-user-manual/037.png)The bottom part of this dialog has a number of different controls as buttons.

The controls on this tab are:

Letters: If one of the letters buttons is selected, a dialog opens to allow customized instructions to be included with the letter and the flowsheet report. A check button also appears allowing you to include the instructions in the progress note.

> Missed Appointment prints a missed appointment letter to the clinic printer.

> Completed Visit prints a completed visit letter to the clinic printer. This letter includes the anticoagulant dosage schedule for the patient.

Progress Notes: Intake Note, D/C Note, Interim Note files the corresponding progress note in the patient record with the information entered during this visit. The program will ask you to electronically sign the note.

### Note: If you are creating an intake note and there is a pending consult request, Anticoagulator will display a dialog asking if you want to use complete the consult. The Anticoagulator can complete the consult regardless of consult status. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When the dialog displays asking if you want to complete the consult, select yes. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](anticoagulation-management-tool-user-manual/038.png)

### Select the Consult you want to complete and select OK. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Sign the Note.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The consults is completed without any other intervention.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Temp Save saves the information entered during this visit without completing the visit.

Complete visit completes the visit and exits the program.

#### #### Anticoagulation Team Patient List 

When exiting the program, the user must complete the current patient’s visit. When the visit is completed, the patient is either retained or removed from the Anticoagulation Team list.

A patient remains on the list if:

- The INR draw date is the current day or any day preceding the current date for completed visits. This including completed backdated visits.
- If there was a Temp Save made on the patient. Temp Saves are made on current day’s date for INR Draw.

A patient is removed from the list if:

- The INR Draw date is scheduled any day after the current date with Completed Visits.
- The INR Draw date is scheduled any day after the current date with Completed Visits featuring Next Day Call Back.

### Utilities Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Utilities Tab has a number of functions that include the entire clinic, not just the currently selected patient. The controls on this tab include:

Percent in Goal shows the patients that are within goal during the last number of days entered in the box. This looks like:

![](anticoagulation-management-tool-user-manual/039.png)

45 day clinic load: Displays the number of patients scheduled for INR tests during each clinic day in the next 45 days.

Pts lost to follow up lists the patients in the anticoagulation program who have not been seen recently. The number of days used in this report can be filled into the box provided. Patients listed are those who have not had the Complete button selected in the number of days the user selects.

Unlock Record pops up a dialog that lists all locked medical records in the VistA system. Many of these are on the list because the record is currently in use by another hospital employee. It is possible for a record to stay locked when it is not in use under specific conditions, such as power failure or workstation crash while the patient record is open. This dialog allows you to unlock records that you select. This feature should be used with extreme care.

# Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## In VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following menu options are available under VistA:

- Anticoagulation Complication Report \[ORAM COMPLICATIONS REPORT\]
- All Anticoagulation Patients \[ORAM PATIENT LIST ALL\]
- Complex Anticoagulation Patients \[ORAM PATIENT LIST COMPLEX\]
- Next Lab Patient List \[ORAM PATIENT LIST NEXT LAB\]
- Single Patient TTR \[ORAM ROSENDAAL SINGLE PT TTR\]
- Calculate TTR (Rosendaal Method) \[ORAM ROSENDAAL TTR REPORT\]

TTR stands for Time in Therapeutic Range.

Users who have access to the Calculate TTR (Rosendaal Method) can include or exclude inactive patients and their missed appointments as shown below:

> Calculate TTR (Rosendaal Method)

> Select one of the following:

> I Include inactive patients and missed appointments

> E Exclude inactive patients and missed appointments

It also provides two umbrella menu actions that give access to the Anticoagulation Complication Report, Calculate TTR (Rosendaal Method), and Single Patient TTR. It is:

- Anticoagulation Management Reports \[ORAM REPORTS MENU\]
- Anticoagulation Patient Lists \[ORAM PATIENT LIST MENU\]

These reports must be assigned to the clinic personnel who need them in the performance of their duties.

To have access to the reports on the menu, you must have them assigned to you on your menu tree. See your local IRM for assistance.

## In CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Flowsheet data from the Anticoagulation Management Tool (AMT) are viewable from the CPRS Reports Tab. It is filed under Clinical Reports then Anticoagulation Flowsheet as shown in this screen shot:

![](anticoagulation-management-tool-user-manual/040.png)

# Frequently Asked Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Urgency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Q: Lab test quick order parameters are incorrect.

Your CBC quick order Urgency is probably set to something like ROUTINE. (It is important to have all the order fields populated in the quick order, otherwise VistA generates processing errors.) Occasionally you may need an Urgency of STAT. There is no way to change this value from the Anticoagulation Management Tool.

A: Switch in to CPRS and correct the Urgency before exiting the AMT flowsheet.

## Reporting Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Q: Reports come out for 30 days. I would like a longer reporting time.

A: The reporting time is controlled by an XPAR parameter called ORWRP TIME/OCC LIMITS ALL. Your ADPAC or CAC can adjust this parameter on the USER, DIVISION, SYSTEM, or PACKAGE level. A USER, DIVISION, or SYSTEM value overrides a PACKAGE value,

## INR Graph

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Q: The data points are too close together on the INR Graph (Demographics Tab) to be useful.

A: You can zoom in on this graph with your mouse. While pressing the left mouse button move the cursor to outline the area of the graph you are interested in. When you release the mouse button the program zooms in on the outlined area. (The same is also true for all graphs created from the CPRS Reports and Labs tabs.)

Q: I would like to see the INR Graph on the Demographics Tab upon processing a new patient, but AMT always displays New Patient Entry Instructions. Occasionally I would like to see the INR Graph instead.

A: On the same line as the title New Patient Entry Instructions there is a button with an X in it. Click this button to see the INR Graph.

# Glossary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>CPRS</strong></th>
<th>Computerized Patient Record System. A user interface for the popular Windows operating system to the Department of Veterans Affairs hospital software system (VistA). The original design criterion was to allow most hospital employees to access patient medical data without the use of command line processing. Eventually CPRS will allow medical record access from any Graphical User Interface (GUI) such as used on Unix, Linux, and OS X.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>HCT</strong></td>
<td>Hematocrit. One of the lab numbers followed by the Anticoagulation Management Tool. It reports the proportion of blood volume occupied by red blood cells.</td>
</tr>
<tr class="even">
<td><strong>ICD-9</strong></td>
<td>International Statistical Classification of Diseases and Related Health Problems. This coding system has become a standard used by insurance companies for claims and billing purposes. Thus the VA uses it to retrieve to help produce revenue by sending insurance claims for non-service connected work done at its medical centers. This numbering classification is updated often and care must be taken to use currently valid codes.</td>
</tr>
<tr class="odd">
<td><strong>INR</strong></td>
<td><p>International Normalized Ratio: The INR is used to the exclusion of other measurements because the result (in seconds) for a prothrombin time performed on a normal individual varies depending on what type of analytical system is used. This is due to the differences between batches of the manufacturer's tissue factor used in the reagent to perform the test. The INR standardizes the results.</p>
<p>INR is the ratio of a patient's prothrombin time to a normal (control) sample, raised to the power of the International Sensitivity Index (ISI) value for the analytical system used. Each manufacturer assigns an ISI value for any tissue factor they manufacture. (This value indicates how a particular batch of tissue factor compares to an internationally standardized sample. The ISI is usually between 1.0 and 2.0.)</p>
<p>The INR formula is:</p>
<p>![](anticoagulation-management-tool-user-manual/041.png)</p></td>
</tr>
<tr class="even">
<td><strong>ISI</strong></td>
<td>International Sensitivity Index. This value indicates how a particular batch of tissue factor compares to an internationally standardized sample. The ISI is usually between 1.0 and 2.0.</td>
</tr>
<tr class="odd">
<td><strong>PCE</strong></td>
<td>Patient Care Encounter. This is VistA’s way of accounting for clinical time. PCE data is passed to the financial services and, if the visit was not service connected, to the patient’s insurance company. Funds paid to the VA by insurance companies help defray a large part of the expenses in running the Veterans Health Administration (VHA).</td>
</tr>
<tr class="even">
<td><strong>Prothrombin Time</strong></td>
<td>A measurement of the time it takes, in seconds, for blood to coagulate. Because of the wide variability of laboratory tests to determine prothrombin time it has become standard practice to use a derived measurement, the INR, for clinical data.</td>
</tr>
<tr class="odd">
<td><strong>Rosendall Method</strong></td>
<td>A calculation method for Time in Therapeutic Range (TTR) that looks at the amount of time between visits to determine how long the patient might have been within therapeutic range. This is more complex than the calculation on the Demographics tab, which looks at how many visits had INR results in range, then divides by the total number of visits.</td>
</tr>
<tr class="even">
<td><strong>Single Sign On</strong></td>
<td>SSO. This is a VistA Kernel extension that allows multiple executions from a single workstation without a repeat of the authentication process. It is usually associated with User Context (UC) through CCOW (for Clinical Context Object Workgroup). The Anticoagulation Management Tool is SSO aware, but without User Context through CCOW. If you feel you need to use Single Sign On at your workstation, contact your Information Resource Manager (IRM) or Chief Information Officer (CIO).</td>
</tr>
<tr class="odd">
<td><strong>VistA</strong></td>
<td>Veterans Health Information Systems and Technology Architecture. This is a replacement nomenclature the Decentralized Hospital Computer Program originally developed starting in 1977 for VA hospitals. The adoption of the new name in 1996 acknowledges the maturity of the system to a point where it is moving toward a more centralized architecture with communication of patient data between medical centers and the Department of Defense.</td>
</tr>
</tbody>
</table>

# Appendix A: Patient Care Encounter Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Care Encounter (PCE) is that part of VistA that keeps track of information about each ambulatory care service provided in order in order to give both local and national management the information they need to make timely decisions about resource allocation. This is accomplished by reporting PCE data to the National Patient Care Data Base (NPCDB) and local reporting. The data is also reflected in the Health Summary for each patient. In recent years PCE’s function has been expanded to assist medical centers in the recovery of funds from insurance companies for non-service connected care.

When the Anticoagulation Management Tool is initially set up Current Procedure Terminology (CPT) codes are entered and put on file for each of the following anticoagulation encounters:

- Simple Phone Visit
- Complex Phone Visit
- Letter to Patient
- Orientation Class
- Initial Office Visit
- Subsequent Visit

These codes are recorded on both the division (medical center) and clinic level. If no code is entered in the clinic setup, the program uses the division code.

These codes need to be kept current because the American Medical Association (AMA) changes them on an annual basis.

A number of things can go wrong with PCE entries, so the following options are provided in VistA (terminal roll-n-scroll) mode:

- PCE Encounter Data Entry \[PXCE ENCOUNTER DATA ENTRY\] give access to workload reports and allows the entry, but not correction, of encounter data.
- PCE Encounter Data Entry and Delete \[PXCE ENCOUNTER ENTRY & DELETE\] fixes certain erroneous encounter information.
- PCE Encounter Data Entry - Supervisor \[PXCE ENCOUNTER ENTRY SUPER\] can be used to fix any erroneous encounters.

Members of each anticoagulation team should have one or more of these menus assigned to them depending upon their role within the team.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

45 day clinic load, 34
A Fib, 5
A Flutter, 5
Add’l Indications, 5
Anticoagulation Team list, 22
Apply, 14, 26
appointment system, 19
appointment, missed, 16
Atrial Fibrillation, 5
Atrial Flutter, 6
Cerebral Vascular Accident, 6
Change daily dosing, 29
Clear INR, 29
Clinic Name, 4
complete a consult, 33
Complete visit, 33
Complete Visit, 20
Completed Visit, 33
Complications, 15
Complications Tab, 30
Consults, 33
CPRS Patient Selection, 22
CVA, 6
d/c from clinic, 14, 25
D/C Note, 33
Date for the Next Appointment, 32
Date of complication, 30
Demographics Tab, 24
dosage, maximum, 29
Duration, 13
DVT, 6
Eligible for LMWH Bridging, 13, 25
enlarge INR Graph, 38
Enter Information tab, 15
Enter Information Tab, 28
Enter Outside Lab Data, 15, 28
excessive blood clotting, 6
Exit tab, 17
Exit Tab, 32
First Visit, 3
Flow Sheet Tab, 27
Frequently Asked Questions, 38
Hypercoag state, 6
ICD-10 codes, 7
ICD-9 codes, 5
Include in Note?, 25
Indication
additional, 5
primary default, 4
secondary default, 4
INR, 1
INR draw, 23
INR Graph, 38
Intake Note, 33
Interim Note, 18, 33
international normalized ratio (INR), 1
interrupting therapy for surgery, 14
Introduction, 1
Labs, ordering, 32
Level of complexity, 14, 26
LMWH Bridging, 13
Low Molecular Weight Heparin (LMWH), 13
Maximum dosage, 30
mechanical valve, 8
Missed appointment, 16
Missed Appointment, 20, 29, 33
New Flow Sheet Entry, 15, 29
New Patient Entry Instructions, 38
No draws on, 25
Orientation Date, 13, 14, 25
ORWRP TIME/OCC LIMITS ALL, 38
Outside Lab Data, 15, 28
Patient Care Encounter, 41
Patient Letter, 20, 21, 34
Patient Selection, 22
PCE data, 32
PE, 6
pending consults, 33
permission to leave anticoag msg on msg, 14
permission to leave msg with person(s), 14
Pill Strength, 29
Primary default indication, 5
Pt has given permission, 25
Pt Notice, 29
Pt Preferences Tab, 25
Pts lost to follow up, 35
Pulmonary Embolism, 6
recommended setting, 6
Record total weekly dose, 30
Related Manuals, 2
Reminder Date, 24
Reminder Text, 24
Reporting, 36, 38
Reporting Time, 38
Restrict draw, 14
Risks, 25
Save/Exit, 14, 26
Secondary default indication, 5
Secondary Indication(s) / Risks, 25
Secondary Indication(s)/Risks, 14
see the INR Graph, 38
Set Date for the Next Appointment, 32
Set Reminder, 24
Signed Agreement, 14, 25
Special Instructions, 14, 25
Start Date, 14, 25
STAT, 38
Stop Date, 14, 25
Subsequent Visits, 22
Switch Button, 24
Takes meds in A.M, 13
Takes meds in A.M., 25
Team lists, 22
Temp Save, 33
TIA, 6
transferred, 25
Unlock Record, 35
Urgency, 38
Utilities Tab, 34
zoom, 38
