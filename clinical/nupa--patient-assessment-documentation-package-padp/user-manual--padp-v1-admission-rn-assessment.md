---
title: PADP Version 1 Admission-RN Assessment User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Admission-RN Assessment
app_code: NUPA
app_name: Patient Assessment Documentation Package (PADP)
section: CLI
app_status: active
pkg_ns: NUPA
patch_ver: 1
patch_id: NUPA*1
group_key: "NUPA:NUPA:1"
file_numbers: []
security_keys: []
menu_options: 0
description: "--- title: <span id=\\"_top\\" class=\\"anchor\\"></span>Patient Assessment Documentation Package (PADP) ---"
audience: 
keywords: 
  - assessment
  - admission
  - padp
  - manual
  - version
  - patient
  - window
  - table
  - contents
  - skin
page_count: 0
word_count: 12530
section_count: 25
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Assessment_Documentation_Package/nupa1_0_aum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Assessment_Documentation_Package/nupa1_0_aum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=193"
---

---
title: <span id="_top" class="anchor"></span>Patient Assessment Documentation Package (PADP)
---

C3-C1 Conversion Project

Admission – RN Assessment User Manual  
for NUPA Version 1.0

![](padp-version-1-admission-rn-assessment-user-manual/001.png)

April 2012

Office of Information and Technology (OIT)

Office of Enterprise Development (OED)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [# Introduction](#introduction)
- [Using Admission – RN Assessment](#using-admission-rn-assessment)
  - [Opening Admission – RN Assessment](#opening-admission-rn-assessment)
    - [No Previously Saved Information](#no-previously-saved-information)
    - [Previously Entered Information Available for One Patient](#previously-entered-information-available-for-one-patient)
    - [Previously Entered Information Available for Two or More Patients](#previously-entered-information-available-for-two-or-more-patients)
    - [Patient not yet Assigned to an Inpatient Bed](#patient-not-yet-assigned-to-an-inpatient-bed)
  - [Saving and Uploading Data](#saving-and-uploading-data)
    - [Auto Save](#auto-save)
    - [Manual Save](#manual-save)
    - [Upload Data](#upload-data)
    - [Save and Exit](#save-and-exit)
    - [Save Now](#save-now)
    - [Exit](#exit)
    - [Signing Notes](#signing-notes)
  - [Working in a Care Plan](#working-in-a-care-plan)
    - [Viewing Interventions Entered Previously during an Assessment](#viewing-interventions-entered-previously-during-an-assessment)
    - [Entering Problems and Interventions](#entering-problems-and-interventions)
    - [Other Interventions](#other-interventions)
  - [Working in the Consults](#working-in-the-consults)
  - [Working in the Template](#working-in-the-template)
    - [Moving through the Template using the Mouse](#moving-through-the-template-using-the-mouse)
    - [Moving through the Template without a Mouse](#moving-through-the-template-without-a-mouse)
- [Navigating the Admission – RN Assessment Tabs](#navigating-the-admission-rn-assessment-tabs)
  - [General Information (Gen Inf)](#general-information-gen-inf)
    - [Adding an Allergy](#adding-an-allergy)
    - [Initiating a Social Work Consult for Advance Directives](#initiating-a-social-work-consult-for-advance-directives)
    - [Documenting Infection Control Information](#documenting-infection-control-information)
    - [Changing Emergency Contact Information](#changing-emergency-contact-information)
  - [Vital Signs (V/S)](#vital-signs-vs)
  - [Education (Educ)](#education-educ)
  - [Pain (Pain)](#pain-pain)
  - [IV (IV)](#iv-iv)
    - [No IV/Vascular Access Devices](#no-ivvascular-access-devices)
    - [Peripheral Lines - IV Periph](#peripheral-lines-iv-periph)
    - [Central IV Lines – IV Central](#central-iv-lines-iv-central)
    - [Dialysis Ports - IV Dialysis](#dialysis-ports-iv-dialysis)
    - [General Observations/Comments – IV Page 4](#general-observationscomments-iv-page-4)
    - [Care Plan - IV CP](#care-plan-iv-cp)
  - [Respiratory (Resp)](#respiratory-resp)
  - [Cardiovascular (CV)](#cardiovascular-cv)
  - [Neurology (Neuro)](#neurology-neuro)
  - [Gastrointestinal (GI)](#gastrointestinal-gi)
  - [Genitourinary (GU)](#genitourinary-gu)
  - [Musculoskeletal (M/S)](#musculoskeletal-ms)
  - [Skin (Skin)](#skin-skin)
    - [Documenting Pressure Ulcers](#documenting-pressure-ulcers)
    - [Pressure Ulcer Drop-downs](#pressure-ulcer-drop-downs)
    - [Documenting Skin Alterations](#documenting-skin-alterations)
    - [Skin Alteration Drop-downs](#skin-alteration-drop-downs)
  - [Psychosocial (P/S)](#psychosocial-ps)
  - [Restraints (Rest/Restr)](#restraints-restrestr)
  - [Mental Health (MH)](#mental-health-mh)
  - [Functional (Func)](#functional-func)
  - [Discharge Planning (DP)](#discharge-planning-dp)
  - [PCE Data (PCE)](#pce-data-pce)
    - [Reminders Due (Display Only)](#reminders-due-display-only)
    - [Clinical Maintenance](#clinical-maintenance)
    - [Reminder Inquiry](#reminder-inquiry)
    - [Resolve Inpatient Nursing Clinical Reminders](#resolve-inpatient-nursing-clinical-reminders)
  - [View Text (View Text)](#view-text-view-text)
    - [Signing Note and Consults from within the Template](#signing-note-and-consults-from-within-the-template)
- [Patient Unable to Respond](#patient-unable-to-respond)
- [Glossary](#glossary)
- [Appendix A Assessment Contingency Note](#appendix-a-assessment-contingency-note)
<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 38%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>May 2010</td>
<td>1.0</td>
<td>Initial version for v1.0</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>August 2010</td>
<td>1.1</td>
<td>Add content</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>August 2010</td>
<td>1.2</td>
<td>Format content</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>September 2010</td>
<td>1.3</td>
<td><ul>
<li><p>Split manual into three manuals</p></li>
</ul>
<p><em>Admission – RN Assessment and Nursing Data Collection User Manual</em></p>
<ul>
<li><p>Changed dates to October</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>November 2010</td>
<td>1.3</td>
<td><ul>
<li><p>Changed dates to November</p></li>
<li><p>Updated topics to be the same as online help</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>December 2010</td>
<td>1.4</td>
<td><ul>
<li><p>Changed dates to December</p></li>
<li><p>Pulled issues from this doc for team review</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>December 2010</td>
<td>1.5</td>
<td><p>Removed the Nursing Data Collection section to create a 4th user manual</p>
<p><em>Admission – RN Assessment</em></p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>January 2011</td>
<td>1.6</td>
<td><ul>
<li><p>Changed dates to January 2011</p></li>
<li><p>Updated with additional comments from Judy</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>February 2011</td>
<td>1.7</td>
<td>Changed dates to February 2011</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>March 2011</td>
<td>1.8</td>
<td><ul>
<li><p>Changed dates to April 2011</p></li>
<li><p>Updated with Judy’s comments</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>April 2011</td>
<td>1.9</td>
<td>Updated RoboHelp with this file</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>May 2011</td>
<td>2.0</td>
<td><ul>
<li><p>Changed dates to May 2011</p></li>
<li><p>Added (NUPA*1) namespace</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>October 2011</td>
<td>2.1</td>
<td><ul>
<li><p>Added C3-C1 Conversion Project</p></li>
<li><p>Changed dates to October 2011</p></li>
<li><p>Prepped for national release</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>November 2011</td>
<td>2.2</td>
<td><ul>
<li><p>Changed dates to November 2011</p></li>
<li><p>Updated for build v14</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>December 2011</td>
<td>2.3</td>
<td><ul>
<li><p>Changed dates to December 2011</p></li>
<li><p>Changed <em>Admission – RN Reassessment</em> to <em>RN Reassessment</em></p></li>
<li><p>Updated for build v15</p></li>
<li><p>Updated for new assessment executables</p></li>
<li><p>Changed dates to January 2012</p></li>
<li><p>Prepped for national release</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>January 2012</td>
<td>2.4</td>
<td><ul>
<li><p>Changed NUPA *1 to NUPA Version 1.0</p></li>
<li><p>Updated for build v16</p></li>
<li><p>Changed dates to February 2012</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>February 2012</td>
<td>2.5</td>
<td><ul>
<li><p>Updated the Neuro tab</p></li>
<li><p>Updated the Vitals tab</p></li>
<li><p>Updated the Psychosocial tab</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>March 2012</td>
<td>2.6</td>
<td><ul>
<li><p>Changed dates to March 2012</p></li>
<li><p>Prepped for April national release</p></li>
<li><p>Changed dates to April 2012</p></li>
<li><p>Added Appendix A: Assessment Contingency Note</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

# # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Assessment Documentation Package (PADP) Version 1.0 is a Veterans Health Information Systems and Technology Architecture (VistA) software application that enables Registered Nurses (RNs) to document, in a standardized format, patient care during an inpatient stay. Although the content is standardized for use across the VA system, some parameters can be set to support the unique processes at individual medical centers.

PADP interfaces directly with several VistA applications, including Computerized Patient Record System (CPRS), Clinical Reminders, Consult Tracking, Allergy/Adverse Reaction Tracking, Mental Health Assistant, Vitals, and Patient Care Encounter (PCE).

PADP is a Delphi application, which supports RNs in documenting patient care during an inpatient stay. It includes the following templates:

- Admission – RN Assessment allows RNs to document the status of the patient at admission.
- Admission – Nursing Data Collection allows Licensed Practical Nurses (LPNs) and other nursing staff, including the RN, to enter basic patient data, such as vitals and belongings at the time of admission.
- RN Reassessment allows RNs to document the condition of the patient on a regular basis and any time during the inpatient stay.
- Interdisciplinary Plan of Care interfaces with admission and reassessment data, and allows additional information to be entered by the RN and other health care personnel (physicians, social workers, chaplain, etc.). All clinical staff can enter information into the Plan of Care. The Plan of Care can be printed and given to the patient when appropriate.

PADP consists of a KIDS build, NUPA 1.0, and four (4) Delphi GUI templates in three executables.

1.  The executable, Admassess.exe, contains the Admission - RN Assessment template and the Admission - Nursing Data Collection template.
2.  The executable, Admassess_Shift.exe, contains the RN Reassessment template.
3.  The executable, Admassess_Careplan.exe, contains the Interdisciplinary Plan of Care template.

Each template is associated with a note.

- The Admission - RN Assessment template is associated with the note: RN Admission Assessment
- The Admission - Nursing Data Collection template is associated with the note: Nursing Admission Data Collection
- The RN Reassessment template is associated with the note: RN Reassessment
- The Interdisciplinary Plan of Care template is associated with the note: Interdisciplinary Plan of Care

PADP adds to VistA, a new namespace (NUPA), four (4) Progress Notes, five (5) printouts, fourteen (14) files, thirty-six (36) parameters, and new health factors. The 5 printouts are:

1.  The Daily Plan<sup>®</sup> is a health summary designed to be given to the patient and family
4.  Plan of Care is a plan designed to guide the nursing staff
5.  Discharge Plan is for discharge planners
6.  Belongings is a list of patient belongings
7.  Safe Patient Handling is designed to guide the transfer of a patient

# Using Admission – RN Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Registered Nurses (RNs) or ancillary nursing personnel use the Admission - RN Assessment template to document inpatient care in a standardized format. With the assessment template, you collect basic information associated with the patient at the time of admission, such as vitals, level of pain, skin condition, and status of respiration.

## Opening Admission – RN Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You access the Admission – RN Assessment through CPRS from the Tools menu.

1.  Open CPRS.
1.  Select a patient.
2.  Click Tools.
3.  Select Admission Assessment.  
    Enter a patient window automatically opens to the CPRS patient.

> **NOTE:** You may have to re-enter your CPRS access and verify codes, depending on local site setup.

![](padp-version-1-admission-rn-assessment-user-manual/002.png)

Access through CPRS

### No Previously Saved Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter a patient window displays.

![](padp-version-1-admission-rn-assessment-user-manual/003.png)

Admission – RN Assessment, Enter a patient window with no previously saved information

1.  Select an Assessment Type.
4.  Click Start Note.  
    The assessment template opens to the General Information tab for the CPRS patient.

### Previously Entered Information Available for One Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](padp-version-1-admission-rn-assessment-user-manual/004.png)

Patient selection window with previously entered information available for one patient

#### Restore Patient’s Data/No

If you previously entered data on one patient, you are prompted with: *You have previously saved data on a note for patient \<PADPPATIENT,ONE \>.*

1.  Select an Assessment Type.
2.  Select No.  
    The patient’s information is deleted, but the Internal Entry Number (IEN) for the patient displays in the Enter a patient text box.
3.  Click Start Note.  
    The template opens to the General Information tab and you can enter new data for that CPRS patient.
4.  Optional: You can delete the IEN of that CPRS patient, enter the name of a different patient, and click Start Note.

> **NOTE:** The Internal Entry Number (IEN) is a unique, computer-generated number that identifies a specific patient in your system. The IEN has no impact on the completed assessment, nor does it display again.

#### Restore Patient’s Data/Yes

If you previously entered data on one patient, you are prompted with: *You have previously saved data on a note for patient \<PADPPATIENT,ONE \>.*

1.  Select an Assessment Type.
5.  Select Yes.
6.  Click Start Note.  
    The template opens to the General Information tab for the CPRS patient with the data restored.

### Previously Entered Information Available for Two or More Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have previously stored data from more than one patient, you are asked if you want to view a list of those patients.

![](padp-version-1-admission-rn-assessment-user-manual/005.png)

Patient selection window with previously entered information available for more than one patient

#### View the Patients?/No

If you say No, the patient’s name displays in the Enter a patient text box as a number that identifies the CPRS patient.

1.  Select Assessment Type.
7.  Click Start Note.  
    The template opens to the General Information tab.

#### View the Patients?/Yes

1.  Select Yes.
8.  Select an Assessment Type.  
    Patient Selection window displays with a list of patients with saved data.

![](padp-version-1-admission-rn-assessment-user-manual/006.png)

Patient Selection List

#### Patient on the List

1.  Select a name.
8.  Click OK.  
    The template opens to the General Information tab.

#### Patient not on the List

1.  Click Cancel.  
    The number that represents your CPRS patient is in the Enter a patient text box.
9.  Click the Start Note.  
    The template opens to the General Information tab.

![](padp-version-1-admission-rn-assessment-user-manual/007.png)

Admission – RN Assessment, General Information (Gen Inf) tab window, Gen I Page 1

### Patient not yet Assigned to an Inpatient Bed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a patient is not assigned an inpatient bed, a location pop-up automatically displays over the General Information window.

![](padp-version-1-admission-rn-assessment-user-manual/008.png)

Location pop-up: Select visit location

1.  Select a current patient location, i.e., outpatient clinic.  
    Navigate quickly to the current location by entering the first letter of the location.
10. Click OK.

## Saving and Uploading Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto Save

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data are saved automatically. Frequency of auto-save is set locally.

![](padp-version-1-admission-rn-assessment-user-manual/009.png)

Saving data: percentage saved indicator  
(bottom right corner of the window)

### Manual Save

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can save data by using the File menu on any tab.

![](padp-version-1-admission-rn-assessment-user-manual/010.png)

Admission – RN Assessment window, File menu

### Upload Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a note you must upload the data into VistA and CPRS:

1.  Open the File menu on any tab and select Upload Data.  
    Results from your upload display, verifying that the data are uploaded.

![](padp-version-1-admission-rn-assessment-user-manual/011.png)

Admission – RN Assessment, Upload results window

> **NOTE:** The *unsigned* note, selected consults, and PCE data/Health Factors are uploaded into CPRS and VistA.

11. If the information is incomplete, an Error Listing window displays indicating the pages within specific tabs that require attention.
- The tabs with pages that require attention are blue.

![](padp-version-1-admission-rn-assessment-user-manual/012.png)

Admission – RN Assessment, Error Listing window

- Once the pages are completed, the tab returns to gray.
1.  Double-click an item to go to the page that requires attention.
2.  When all the errors are completed, select Upload Data again.

### Save and Exit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To save data and temporarily leave the template:

1.  Open the File menu on any tab.
12. Select Save and Exit.
13. When you reopen the template, your previously entered data is there.

### Save Now

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To save data, but not close the template and continue to enter data:

1.  Open the File menu on any tab.
14. Select Save Now.
15. Continue to enter data for the current patient.

### Exit 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From any tab, click X in the top right corner of the window.  
    Warning message displays.

![](padp-version-1-admission-rn-assessment-user-manual/013.png)

Warning pop-up: Do you really wish to exit?

2.  Click Yes.

or

1.  From any tab, open the File menu and click Exit.  
    Warning message displays.
3.  Click Yes.

### Signing Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Go to CPRS to sign your uploaded, *unsigned* notes and consults.

You can also sign *unsigned* notes after the upload from the View Text tab in the template.

1.  Click View Text.

![](padp-version-1-admission-rn-assessment-user-manual/014.png)

Admission – RN Assessment, View Text tab after upload

16. Click Sign Note/Consults.

![](padp-version-1-admission-rn-assessment-user-manual/015.png)

Admission – RN Assessment with Sign Note/Consults button

9.  Enter your electronic signature and click Accept e-sig.
17. To prevent the signing of an uploaded note, click Cancel e-sig.

> **NOTE:** If there is only a note to sign, the button is Note.  
If there is a consult to sign, the button is Sign Note/Consults.<span id="_Ref270329679" class="anchor"></span>

## Working in a Care Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Care Plan page for each section of the Admission – RN Assessment works the same way. The steps apply to each of the care plan (CP) pages. Creating a Rest CP is an example of how to work in any of the care plans.

Example – Creating a Rest CP

On Rest Page 1, select the Restraints Initiated/maintained check box. Click Rest CP to open the restraints care plan.

![](padp-version-1-admission-rn-assessment-user-manual/016.png)

Admission – RN Assessment, \<Restraints\> - Problems/Interventions/Desired Outcomes, \<Rest\> CP window

### Viewing Interventions Entered Previously during an Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click \<Rest\> CP.  
    Rest CP - the \<Restraints\> - Problems/Interventions/Desired Outcomes window displays.
18. Click View all interventions to view a list of interventions.  
    The Intervention List displays.

![](padp-version-1-admission-rn-assessment-user-manual/017.png)

Rest CP window, Intervention List window

19. Click Close.

### Entering Problems and Interventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select a problem in the Select Problem(s) list box.  
    The desired outcome and interventions for the selected problem display.

![](padp-version-1-admission-rn-assessment-user-manual/018.png)

Admission – RN Assessment, \<Restraints\> - Problems/Interventions/Desired Outcomes \<Rest\> CP window

2.  Select one or more interventions in the Select Interventions list box.
3.  Click Add/Change to transfer the intervention to the care plan.  
    Information pop-up displays.

![](padp-version-1-admission-rn-assessment-user-manual/019.png)

Information pop-up: 1 intervention added!

4.  Click OK.
20. To add interventions for additional problems, repeat steps 1 through 4, as necessary.

### *Other* Interventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some interventions generate a pop-up to enter interventions that are not on the predefined list.

1.  Select an *Other* intervention in the Select Interventions list box.  
    The *Other* interventions pop-up displays.

![](padp-version-1-admission-rn-assessment-user-manual/020.png)

Admission – RN Assessment, \<Restraint\> – Problems/Interventions/Desired Outcomes, \<Rest\> CP window, Interventions: Other Treatments pop-up

21. Type the *other* intervention into the text box.
22. Click OK.
23. Click Add/Change to transfer the intervention to the care plan.  
    Information pop-up displays.

![](padp-version-1-admission-rn-assessment-user-manual/021.png)

Information pop-up: 1 intervention added!

24. Click OK.
25. To add additional *other* interventions, repeat steps 1 through 5, as necessary.<span id="_Ref273355528" class="anchor"></span>

## Working in the Consults

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All the consults in Admission – RN Assessment work the same way. The following steps apply to each of the consults. When a consult is required, a mandatory consult message is highlighted in red. Ordering a Chaplain Consult is an example of how to work in any of the consults.

Example – Ordering a Chaplain Consult

Order a Chaplain Consult from Gen Inf tab, Gen I Page 2 in the Spiritual/Cultural Assessment section.

The Chaplain Consult is mandatory when the patient answers Yes to any one of the following questions.

- Are there religious practices or spiritual concerns the patient wants the chaplain, physician, and other health care team members to immediately know about?
- Patient requests an immediate visit from the Chaplain?
- Does patient have a pastor or clergy who should be notified of this hospitalization?
1.  Select Yes and a message indicating the consult is mandatory displays:  
    Chaplain consult mandatory

![](padp-version-1-admission-rn-assessment-user-manual/022.png)

Admission – RN Assessment, General Information (Gen Inf) tab, Gen I Page 2 window  
Spiritual/Cultural Assessment

2.  Click \<Chaplain Consult\>.  
    The \<INPATIENT CHAPLAIN\> Consult window displays.

![](padp-version-1-admission-rn-assessment-user-manual/023.png)

INPATIENT CHAPLAIN Consult window

1.  Complete all fields with asterisks; they are required fields.
2.  Click Upload Consult.  
    Information pop-up displays indicating the consult is uploaded with the RN Admission Assessment note.

![](padp-version-1-admission-rn-assessment-user-manual/024.png)

Information pop-up: Consult will be uploaded with the note.

26. Click OK.  
    On the Gen Inf tab, Gen I Page 2, under Chaplain Consult, Will Send displays.

![](padp-version-1-admission-rn-assessment-user-manual/025.png)

Admission – RN Assessment, General Information (Gen Inf) tab, Gen I Page 2 window  
Spiritual/Cultural Assessment

> **NOTE:** Manage consults according to medical center policy. If nurses at your site do not order consults, upload a mandatory consult, but do not sign it.  
The identified provider will be notified that there is a consult to sign.

## Working in the Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To complete the template, move through the fields from left to right and then down.
4.  The active page displays first and the page tab is white.
5.  Each tab across the bottom is subdivided into pages, which display on the right above the bar of tabs.
6.  Each field with an asterisk (\*) must have an entry.
7.  A field without an asterisk is optional.
8.  You must enter optional information where appropriate for the patient.

### Moving through the Template using the Mouse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click a tab at the bottom of any of the Admission – RN Assessment windows.  
    The selected tab opens.

![](padp-version-1-admission-rn-assessment-user-manual/026.png)

Admission – RN Assessment tabs

2.  Open the Tabs menu and select a tab from the list.  
    The selected tab opens.

![](padp-version-1-admission-rn-assessment-user-manual/027.png)

Admission – RN Assessment, Tabs menu

### Moving through the Template without a Mouse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Ctrl-Alt Keys

You can move from tab to tab using Ctrl+Alt+\<letter\>. The list contains the keys to use for each of the tabs.

| Tab                 | Keys        |
|---------------------|-------------|
| General Information | Ctrl +Alt+G |
| Belongings          | Ctrl +Alt+B |
| Orientation         | Ctrl +Alt+O |
| Vital Signs         | Ctrl +Alt+U |
| Education           | Ctrl +Alt+E |
| Pain                | Ctrl +Alt+P |
| IV                  | Ctrl +Alt+I |
| Respiratory         | Ctrl +Alt+R |
| Cardiovascular      | Ctrl +Alt+L |
| Neurological        | Ctrl +Alt+N |
| Gastrointestinal    | Ctrl +Alt+A |
| Genitourinary       | Ctrl +Alt+T |
| Musculoskeletal     | Ctrl +Alt+M |
| Skin                | Ctrl +Alt+S |
| Psychosocial        | Ctrl +Alt+Y |
| Restraints          | Ctrl +Alt+Z |
| Mental Health       | Ctrl +Alt+H |
| Functional          | Ctrl +Alt+F |
| Discharge Planning  | Ctrl +Alt+D |
| PCE                 | Ctrl +Alt+X |
| View Text           | Ctrl +Alt+V |

#### Go to radiogroup

The Go to radiogroup: is designed to navigate the templates with keyboard commands, when the mouse stops working during a patient assessment. It also satisfies the 508-compliant requirement, under Section 508 of the Rehabilitation Act, to be able to navigate the templates without using a mouse.

![](padp-version-1-admission-rn-assessment-user-manual/028.png)

Go button

1.  Use the Tab key to move to the bottom of the page.
9.  Use the arrow keys to move up/down in the Go to radiogroup: list.
10. Click Go.

or

1.  Click the drop-down arrow in the Go to radiogroup: drop-down list.
27. Select a radiogroup.
28. Click Go.

# Navigating the Admission – RN Assessment Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Admission – RN Assessment template has 21 tabs.

> **NOTE:** For information on the Belongings and Orientation to Unit tabs, refer to the *Admission – Nursing Data Collection User Manual*.

## General Information (Gen Inf)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Admission – RN Assessment template opens to the General Information (Gen Inf) tab, the first tab at the bottom on the left.

1.  Populate Gen I Page 1.
29. In the Patient/family/support person able to respond to questions box, select Yes or No.
- If you select Yes, the application automatically enters Yes in each tab. You must also enter from whom the information is obtained.

![](padp-version-1-admission-rn-assessment-user-manual/029.png)

Admission – RN Assessment, General Information (Gen Inf) tab, Gen I Page 1 window  
Patient/family/support person able to respond to questions/Yes

- If you select No, when a patient is unable to answer questions and there are no family members or others to contribute to the assessment, some of the fields will be unavailable.  
  The unavailable questions are passed forward into the RN Reassessment to answer later, if possible.
- When you select No, you must manually select patient status on each tab.
30. Make appropriate selections on Gen I Page 1.

![](padp-version-1-admission-rn-assessment-user-manual/030.png)

Admission – RN Assessment, General Information (Gen Inf) tab, Gen I Page 1,  
Patient/family/support person able to respond to questions/No

10. Click Gen I Page 2.  
    Gen I Page 2 displays.  
    Allergies are added in the Allergies text box.

![](padp-version-1-admission-rn-assessment-user-manual/031.png)

Admission – RN Assessment, General Information (Gen Inf) tab, Gen I Page 2 window

31. Populate Gen I Page 2.

### Adding an Allergy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Allergies/Adverse Reactions are uploaded immediately into the Allergy/Adverse Reaction Package when saved.

> **NOTE:** Follow your local medical center policy with regard to adding allergies.

1.  Click Add New Allergy.  
    The Add New Allergies window displays.

![](padp-version-1-admission-rn-assessment-user-manual/032.png)

Add New Allergies window

2.  Type 3-5 letters of the reported allergy into the Search for text box.
32. Click Search.
33. Double-click an allergy in the Allergy list.  
    The Sign/Symptoms list box displays.

![](padp-version-1-admission-rn-assessment-user-manual/033.png)

Add New Allergies window with Sign/Symptoms available

34. In the Observed/Historical text box, select Observed or Historical.
35. In the Nature of reaction drop-down text box, select Allergy, Pharmacological, or Unknown.
36. In the Signs/Symptoms list, select the identified signs/symptoms.
37. Click OK and the allergy is saved in the Adverse Drug Reaction (ADR) file.  
    Information pop-up displays to confirm the allergy is saved.

![](padp-version-1-admission-rn-assessment-user-manual/034.png)

Information pop-up: Allergy save done!

38. Click OK.
39. Click Close to return to Gen I Page 2.

### Initiating a Social Work Consult for Advance Directives

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All of the consults in Admission – RN Assessment work the same way; refer to the instructions in *Working in the Consults* on page [15](#_Ref273355528).

1.  Click Gen I Page 3.  
    Gen I Page 3 displays with the Advance Direction section available.

![](padp-version-1-admission-rn-assessment-user-manual/035.png)

Admission – RN Assessment, General Information (Gen Inf) tab, Gen I Page 3 window  
Advance Directive/Yes

40. Populate Gen I Page 3.
- Make appropriate selections in the Advance Directive section.
- If the patient wants to initiate or make changes to an Advance Directive, a Social Work Consult is required.

![](padp-version-1-admission-rn-assessment-user-manual/036.png)

Admission – RN Assessment, General Information (Gen Inf) tab, Gen I Page 3 window  
Advance Directive/No

### Documenting Infection Control Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](padp-version-1-admission-rn-assessment-user-manual/037.png)

Infection Control Information/MRSA

1.  Make appropriate selections in the Infection Control section.
41. Enter infection control and Methicillin-Resistant Staphylococcus Aureus (MRSA) collection information.

### Changing Emergency Contact Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click Gen I Page 4.  
    Gen I Page 4 displays with the Emergency contact information, Support person contact information, and General observations/comments text boxes available for additional information.

![](padp-version-1-admission-rn-assessment-user-manual/038.png)

Admission – RN Assessment, General Information (Gen Inf) tab, Gen I Page 4 window

![](padp-version-1-admission-rn-assessment-user-manual/039.png)

Emergency Contact Information for patient and support person

2.  To update the emergency contact information, click Change Contact.  
    The Emergency contact information section expands.
42. Complete all the fields with asterisks; they are required fields.
43. Click Save Contact.
44. To cancel the update, click Cancel Contact before you click Save Contact.
45. Document the name and contact information of the patient’s support person.  
    It is required information.

  

## Vital Signs (V/S)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vitals tab contains information about the patient’s vital signs at admission. The vital signs include temperature, pulse, respiration, blood pressure, height, weight, pain, pulse oximetry, and circumference /girth.

> **NOTE:** When you click Upload Vitals, vital signs are immediately uploaded into the Vitals package.

![](padp-version-1-admission-rn-assessment-user-manual/040.png)

Admission – RN Assessment, Vitals (V/S) tab window

1.  Click V/S.  
    Vitals (V/S) displays.
1.  Complete all the fields with asterisks; they are required fields.
3.  Click each Click to enter qualifiers, to select qualifiers for each of the vitals.

> **NOTE:** Remember to enter units where appropriate.  
Example

- Entering the temperature, depending on the type of thermometer used, select C for Centigrade or F for Fahrenheit.
- Entering the height and weight, depending on the instruments used, select CM or IN and KG or LB.

![](padp-version-1-admission-rn-assessment-user-manual/041.png)

Admission – RN Assessment, Vitals (V/S) tab window, Qualifiers - Temp

![](padp-version-1-admission-rn-assessment-user-manual/042.png)

Admission – RN Assessment, Vitals (V/S) tab window, Qualifiers - Pulse

![](padp-version-1-admission-rn-assessment-user-manual/043.png)

Admission – RN Assessment, Vitals (V/S) tab window, Qualifiers - Resp

![](padp-version-1-admission-rn-assessment-user-manual/044.png)

Admission – RN Assessment, Vitals (V/S) tab window, Qualifiers - BP

![](padp-version-1-admission-rn-assessment-user-manual/045.png)

Admission – RN Assessment, Vitals (V/S) tab window, Qualifiers – Height

![](padp-version-1-admission-rn-assessment-user-manual/046.png)

Admission – RN Assessment, Vitals (V/S) tab window, Qualifiers - Weight

![](padp-version-1-admission-rn-assessment-user-manual/047.png)

Admission – RN Assessment, Vitals (V/S) tab window, Qualifiers – Pulse Ox

![](padp-version-1-admission-rn-assessment-user-manual/048.png)

Admission – RN Assessment, Vitals (V/S) tab window, Qualifiers - Circumference

46. Click Save Qualifiers, after selecting qualifiers for the individual vitals.
47. To remove incorrect qualifiers entered in error, click Cancel before saving.
48. Click Upload Vitals.  
    Information pop-up displays.

![](padp-version-1-admission-rn-assessment-user-manual/049.png)

Information pop-up: Vitals will now be uploaded.

1.  Click OK.  
    Information pop-up displays.

![](padp-version-1-admission-rn-assessment-user-manual/050.png)

Information pop-up: Vitals uploaded!

4.  Click OK.

![](padp-version-1-admission-rn-assessment-user-manual/051.png)

Admission – RN Assessment, Vitals (V/S) tab window  
with Last Vitals

11. If you select the Vitals cannot be taken at this time or the patient refused check box,  
    enter a reason in the \*Why were vitals not taken text box in the lower left corner of the page.

![](padp-version-1-admission-rn-assessment-user-manual/052.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window  
Vitals cannot be taken at this time or patient refused

12. If you select the Could not obtain height and/or the Could not obtain weight check boxes at time of assessment, enter a reason in the \*Why were vitals not taken text box in the lower left corner of the page.

![](padp-version-1-admission-rn-assessment-user-manual/053.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window  
Could not obtain height/Could not obtain weight

## Education (Educ)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Education Assessment tab contains an educational and a readiness to learn assessment. The Educational Assessment is unavailable when the patient cannot respond.

![](padp-version-1-admission-rn-assessment-user-manual/054.png)

Admission – RN Assessment, Educational Assessment (Educ) tab, Educ Page 1 window  
Patient/family/support person able to respond to questions/Yes

1.  Click Educ.  
    Educ Page 1 displays.
2.  Populate Educ Page 1.  
    Complete all the fields with asterisks; they are required fields.

![](padp-version-1-admission-rn-assessment-user-manual/055.png)

Admission – RN Assessment, Educational Assessment (Educ) tab, Educ Page 1 window  
Patient/family/support person able to respond to questions/No

49. Click Educ CP.  
    Educ CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/056.png)

Admission – RN Assessment, Education – Problems/Interventions/Desired Outcomes, Educ CP window

50. Populate Educ CP.  
    Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

## Pain (Pain)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pain tab contains questions related to pain, pain location, and type of pain.

![](padp-version-1-admission-rn-assessment-user-manual/057.png)

Admission – RN Assessment, Pain Assessment (Pain) tab, Pain Page 1 window  
Is pain a problem for the patient/Yes

1.  Click Pain.  
    Pain Page 1 displays.
2.  Populate Pain Page 1.
1.  Select a radio button in the Is pain a problem for the patient group. The fields that display vary depending on the response for this query.
- Yes
- No
- Unable to respond to questions
5.  Select a radio button in the Is patient on Palliative/Comfort Care group.

Is pain a problem for the patient/Yes

1.  If a patient reports that pain is a problem (even if there is no pain currently), select Yes.
1.  The Other Pain and Other Pain 2 pages are available when the patient identifies multiple pain locations. There are five pain location sections.
6.  Identify Pain Location \#1 and document the behavioral indicators.
7.  Complete all fields with asterisks; they are required fields.
51. Pain Comm and Pain CP are always available, so you can enter comments or interventions, when appropriate.

![](padp-version-1-admission-rn-assessment-user-manual/058.png)

Admission – RN Assessment, Pain Assessment (Pain) tab, Pain Page 1 window  
Other pain location selected

52. When Pain Location \#1 is complete and you have more pain locations to document, select the Other pain location check box.  
    The Other Pain page displays.

![](padp-version-1-admission-rn-assessment-user-manual/059.png)

Admission – RN Assessment, Pain Assessment (Pain) tab, Other Pain window  
Pain Location \#2 and Pain Location \#3

53. Optional: Populate the Other Pain page.
1.  Identify Pain Location \#2/Pain Location \#3 and document the behavioral indicators.
8.  Complete all fields with asterisks; they are required fields.
54. When Pain Locations \#2 and \#3 are complete and you have more pain locations to document, select the More pain location check box.  
    The Other Pain 2 displays.

![](padp-version-1-admission-rn-assessment-user-manual/060.png)

Admission – RN Assessment, Pain Assessment (Pain) tab, Other Pain 2 window  
Pain Location \#4 and Pain Location \#5

55. Optional: Populate the Other Pain 2 page.
1.  Identify Pain Location \#4/Pain Location \#5 and document the behavioral indicators.
9.  Complete all fields with asterisks; they are required fields.
56. If you require more than five pain locations, continue to document on the Pain Comm page in the General observations/comments text box.

Is pain a problem for the patient/No

![](padp-version-1-admission-rn-assessment-user-manual/061.png)

Admission – RN Assessment, Pain Assessment (Pain) tab, Pain Page 1 window,  
Is pain a problem for the patient/No

1.  If the patient does not complain of pain, select No.
1.  The Other Pain and Other Pain 2 pages are unavailable.
2.  Many fields are unavailable.
57. Select a radio button in the Is patient on Palliative/Comfort Care group.

Is pain a problem for the patient/Unable to respond to questions

![](padp-version-1-admission-rn-assessment-user-manual/062.png)

Admission – RN Assessment, Pain Assessment (Pain) tab, Pain Page 1 window  
Is pain a problem for the patient/Unable to respond to questions

1.  When Unable to respond to questions is selected on Pain Page 1
1.  Type an explanation for unable to respond in the Explain why patient unable to respond to questions text box.
2.  Select behavioral indications in the Does patient exhibit behavioral indicators related to pain list box.
3.  Select a radio button in the Is patient on Palliative/Comfort Care group.
58. Click Pain Comm.  
    Pain Comm displays.

![](padp-version-1-admission-rn-assessment-user-manual/063.png)

Admission – RN Assessment, Pain Assessment (Pain) tab, Pain Comm window

59. Populate Pain Comm, if necessary.  
    Use the General observations/comments text box for additional information.
60. Click Pain CP.  
    Pain CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/064.png)

Admission – RN Assessment, Pain – Problems/Interventions/Desired Outcomes, Pain CP window

61. Populate Pain CP.  
    Refer to the instructions in *Working in a Care Plans* on page [11](#_Ref270329679).

## IV (IV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IV tab contains information about IV devices, IV locations, and dialysis ports.

### No IV/Vascular Access Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click IV.  
    IV Periph displays.
62. If a patient has no IVs or dialysis access in place, select the No IV/vascular access devices check box and none of the IV pages or Add New IV Location are available.
63. Move to the next tab.

![](padp-version-1-admission-rn-assessment-user-manual/065.png)

Admission – RN Assessment, IV (IV) tab, IV Periph window  
No IV vascular access devices selected

### Peripheral Lines - IV Periph

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click IV.  
    IV Periph displays.
2.  Populate IV Periph.
3.  Click Add New IV Location.  
    The Location drop-down list box displays in the Edit Peripheral Line site \#1 section.

![](padp-version-1-admission-rn-assessment-user-manual/066.png)

Admission – RN Assessment, IV (IV) tab, IV Periph window

64. Select a location.  
    Additional fields become available.
65. Complete all the fields with asterisks; they are required fields.
66. To cancel entered data *before upload*, click Cancel edit.
67. To upload the data, click OK.  
    Information pop-up displays.

![](padp-version-1-admission-rn-assessment-user-manual/067.png)

Information pop-up: IV edits will be uploaded with the note.

> **NOTE:** The IV information is not uploaded until the RN Admission Assessment note is uploaded.

68. Click OK.  
    IV Periph tab redisplays with a location added.

![](padp-version-1-admission-rn-assessment-user-manual/068.png)

Admission – RN Assessment, IV (IV) tab, IV Periph window  
with a peripheral line location

69. To add another IV location, repeat steps 1 through 8.

> **NOTE:** There is no limit to the number of IV locations you can enter.

![](padp-version-1-admission-rn-assessment-user-manual/069.png)

Admission – RN Assessment, IV (IV) tab, IV Periph window  
with two peripheral lines added

### Central IV Lines – IV Central

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click IV Central.  
    IV Central displays.
2.  Populate IV Central.

![](padp-version-1-admission-rn-assessment-user-manual/070.png)

Admission – RN Assessment, IV (IV) tab, IV Central window

3.  Click Add New CL Location.  
    The Type and Location drop-down list boxes display in the Edit Central Line site \#1 section.
70. Select a type and a location.
71. Complete all the fields with asterisks; they are required fields.
72. To cancel entered data *before upload*, click Cancel edit.
73. To upload the data, click OK.  
    Information pop-up displays.

![](padp-version-1-admission-rn-assessment-user-manual/071.png)

Information pop-up: Central line edits will be uploaded with the note.

74. Click OK.
75. To add another central line, repeat steps 1 through 8.

### Dialysis Ports - IV Dialysis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click IV Dialysis.  
    IV Dialysis displays.
2.  Populate IV Dialysis.

![](padp-version-1-admission-rn-assessment-user-manual/072.png)

Admission – RN Assessment, IV (IV) tab, IV Dialysis window  
with no Dialysis location

3.  Click Add New Dialysis Location.  
    The Type and Select Dialysis location drop-down list boxes display in the Edit Dialysis access location \#1 section.

![](padp-version-1-admission-rn-assessment-user-manual/073.png)

Admission – RN Assessment, IV (IV) tab, IV Dialysis window  
with Edit Dialysis access location \#1

4.  Select a type and a location.

> **NOTE:** When you select AV Fistula or AV Graft for Type, a warning message displays to advise against using the patient’s affected arm for BP or needle sticks.  
You must place an arm band on the affected limb to prevent any mishaps.

![](padp-version-1-admission-rn-assessment-user-manual/074.png)

Warning pop-up:  
Place arm band. No blood pressure or needle sticks in the arm that the AV Fistula is in!

76. Complete all the fields with asterisks; they are required fields.
77. To cancel entered data *before upload*, click Cancel edit.
78. To upload the data, click OK.  
    Information pop-up displays.

![](padp-version-1-admission-rn-assessment-user-manual/075.png)

Information pop-up: Dialysis edits will be uploaded with the note.

79. Click OK.
80. To add another dialysis access location, repeat steps 1 through 8.

### General Observations/Comments – IV Page 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click IV Page 4.  
    IV Page 4 displays.

![](padp-version-1-admission-rn-assessment-user-manual/076.png)

Admission – RN Assessment, IV (IV) tab, IV Page 4 window

81. Populate IV Page 4.  
    Use the General observations/comments text box for additional information.

### Care Plan - IV CP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click IV CP.  
    IV CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/077.png)

Admission – RN Assessment, IV – Problems/Interventions/Desired Outcomes, IV CP window

82. Populate IV CP.
83. Add/Change problems/interventions, if necessary.
84. Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

## Respiratory (Resp)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Respiratory Assessment tab contains an assessment of the patient’s breathing at admission.

![](padp-version-1-admission-rn-assessment-user-manual/078.png)

Admission – RN Assessment, Respiratory Assessment (Resp) tab, Resp Page 1 window

1.  Click Resp.  
    Resp Page 1 displays.
2.  Populate Resp Page 1.
1.  Use the Respiratory rate text box to enter the patient’s current respiratory rate.
2.  Complete all the fields with asterisks; they are required fields.
85. Click Resp Page 2.  
    Resp Page 2 displays.

![](padp-version-1-admission-rn-assessment-user-manual/079.png)

Admission – RN Assessment, Respiratory Assessment (Resp) tab, Resp Page 2 window

86. Populate Resp Page 2.
1.  Complete all the fields with asterisks; they are required fields.
10. When Home oxygen is selected under Respiratory device, the Respiratory Consult is available.  
    Order a consult according to your medical center policy.
11. Refer to the instructions in *Working in the Consults* on page [15](#_Ref273355528).
87. Click Resp Page 3.  
    Resp Page 3 displays.

![](padp-version-1-admission-rn-assessment-user-manual/080.png)

Admission – RN Assessment, Respiratory - Problems/Interventions/Desired Outcomes, Resp Page 3 window  
contains the Tobacco screen

88. Populate Resp Page 3.
1.  If the patient has a tracheostomy, complete fields with asterisks; they are required fields.
12. Complete the Tobacco fields with asterisks; they are required fields.

> **NOTE:** Health Factors are deposited into PCE for Clinical Reminder resolution and/or cohort identification.

89. Click Resp CP.  
    Resp CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/081.png)

Admission – RN Assessment, Respiratory - Problems/Interventions/Desired Outcomes, Resp CP window

90. Populate Resp CP.  
    Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

## Cardiovascular (CV)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Cardiovascular Assessment tab contains a history of the patient’s cardiovascular health.

![](padp-version-1-admission-rn-assessment-user-manual/082.png)

Admission – RN Assessment, Cardiovascular Assessment (CV) tab, CV Page 1 window

1.  Click CV.  
    CV Page 1 displays.
91. Populate CV Page 1.
1.  Complete all the fields with asterisks; they are required fields.
13. Use the Extremities comments text box for additional information, if necessary.
92. Click CV Page 2.  
    CV Page 2 displays.

![](padp-version-1-admission-rn-assessment-user-manual/083.png)

Admission – RN Assessment, Cardiovascular Assessment (CV) tab, CV Page 2 window

93. Populate CV Page 2.
1.  Complete all the fields with asterisks; they are required fields.
2.  Use the General observations/comments text box for additional information.
94. Click CV CP.  
    CV CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/084.png)

Admission – RN Assessment, Cardiovascular – Problems/Interventions/Desired Outcomes, CV CP window

95. Populate CV CP.  
    Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

## Neurology (Neuro)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Neurological Assessment tab contains an assessment of brain related issues and includes instructions for assessing the patient’s level of consciousness.

The directions for the *Glasgow Coma Scale* are on Neuro Page 1. The score is automatically calculated and transferred to the finished RN Admission Assessment note.

![](padp-version-1-admission-rn-assessment-user-manual/085.png)

Admission – RN Assessment, Neurological Assessment (Neuro) tab, Neuro Page 1 window

1.  Click Neuro.  
    Neuro Page 1 displays.
96. Populate Neuro Page 1.  
    Complete all the fields with asterisks; they are required fields.
97. Click Neuro Page 2.  
    Neuro Page 2 displays.

![](padp-version-1-admission-rn-assessment-user-manual/086.png)

Admission – RN Assessment, Neurological Assessment (Neuro) tab, Neuro Page 2 window

98. Populate Neuro Page 2.
1.  Complete all the fields with asterisks; they are required fields.
14. Use the General observations/comments text box for additional information.
99. Click Neuro CP.  
    Neuro CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/087.png)

Admission – RN Assessment, Neurological Assessment (Neuro) tab, Neuro CP window

100. Populate Neuro CP.  
     Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

## Gastrointestinal (GI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Gastrointestinal Assessment tab contains abdominal and bowel assessments, a nutrition screening, and a dietary history.

- On GI Page 3, when any items listed under the Nutrition consult guidelines are selected, a Nutrition Consult is required.
- On GI Page 3, when any Dysphagia question is answered with Yes, a Speech Consult is required.

![](padp-version-1-admission-rn-assessment-user-manual/088.png)

Admission – RN Assessment, Gastrointestinal Assessment (GI) tab, GI Page 1 window

1.  Click GI.  
    GI Page 1 displays.
101. Populate GI Page 1.  
     Complete all the fields with asterisks; they are required fields.
102. Click GI Page 2.  
     GI Page 2 displays.

![](padp-version-1-admission-rn-assessment-user-manual/089.png)

Admission – RN Assessment, Gastrointestinal Assessment (GI) tab, GI Page 2 window

103. Populate GI Page 2.  
     Complete all the fields with asterisks; they are required fields.
104. Click GI Page 3.  
     GI Page 3 displays.

![](padp-version-1-admission-rn-assessment-user-manual/090.png)

Admission – RN Assessment, Gastrointestinal Assessment (GI) tab, GI Page 3 window

105. Populate GI Page 3.
1.  Complete all the fields with asterisks; they are required fields.
15. Use the General observations/comments text box for additional information
16. GI Page 3 contains Speech Consult and Nutrition Consult.  
    Refer to the instructions in *Working in the Consults* on page [15](#_Ref273355528).
106. Click GI CP.  
     GI CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/091.png)

Admission – RN Assessment, Gastrointestinal – Problems/Interventions/Desired Outcomes, GI CP window

107. Populate GI CP.  
     Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

## Genitourinary (GU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Genitourinary Assessment tab contains information about the quality and quantity of urine.

Questions about urine are optional because patients may not be able to void at time of the assessment.

![](padp-version-1-admission-rn-assessment-user-manual/092.png)

Admission – RN Assessment, Genitourinary Assessment (GU) tab, GU Page 1 window

1.  Click GU.  
    GU Page 1 displays.
108. Populate GU Page 1.  
     Complete all the fields with asterisks; they are required fields.
109. Click GU Page 2.  
     GU Page 2 displays.

![](padp-version-1-admission-rn-assessment-user-manual/093.png)

Admission – RN Assessment, Genitourinary Assessment (GU) tab, GU Page 2 window  
Male patient information available

![](padp-version-1-admission-rn-assessment-user-manual/094.png)

Admission – RN Assessment, Genitourinary Assessment (GU) tab, GU Page 2 window  
Female patient information available

> **NOTE:** The sex-specific questions (male/female) are optional. The exception is for female patients; the pregnancy responses are required.

110. Populate GU Page 2.
1.  When a patient has genitourinary devices, additional fields are made available.
17. Complete all the fields with asterisks; they are required fields.
18. Use the General observations/comments text box for additional information.
111. Optional: If the Women’s Health Consult is set up at your site, the button displays on GU Page 2; refer to the instructions in *Working in the Consults* on page [15](#_Ref273355528).
112. Click GU CP.  
     GU CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/095.png)

Admission – RN Assessment, Genitourinary – Problems/Interventions/Desired Outcomes, GU CP window

113. Populate GU CP.  
     Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

## Musculoskeletal (M/S)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Musculoskeletal Assessment tab contains information about the patient’s muscular and skeletal history.

Directions for the *Morse Fall Scale* are on M/S Page 2. The directions are only on the template and are not transferred into the completed Progress Note.

- The Total Morse score for fall risk for the patient is calculated automatically as you select responses for history of falling, secondary diagnosis, ambulatory aid, gait/transferring, and marital status.
- The Morse Score is pulled forward to the M/S CP page to guide the entry of interventions.
1.  Click M/S.  
    M/S Page 1 displays.

![](padp-version-1-admission-rn-assessment-user-manual/096.png)

Admission – RN Assessment, Musculoskeletal Assessment (M/S) tab, M/S Page 1 window

114. Populate M/S Page 1.
1.  Complete all the fields with asterisks; they are required fields.
19. Use the General observations/comments text box for additional information.
115. Click M/S Page 2.  
     M/S Page 2 displays.

![](padp-version-1-admission-rn-assessment-user-manual/097.png)

Admission – RN Assessment, Musculoskeletal Assessment (M/S) tab, M/S Page 2 window

116. Populate M/S Page 2.  
     Complete all the fields with asterisks; they are required fields.
117. Click M/S CP.  
     M/S CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/098.png)

Admission – RN Assessment, Musculoskeletal – Problems/Interventions/Desired Outcomes M/S tab,  
M/S CP window

118. Populate M/S CP.  
     Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

> **NOTE:** *Universal Fall Precautions* must be completed for all patients.

## Skin (Skin)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Skin Assessment tab contains information about the condition of the patient’s skin – pressure ulcers and skin alterations.

Directions for the *Braden Scale for Predicting Pressure Sore Risk* are on Skin Page 3.

- The Total Score for the patient is calculated automatically as you select scores (1-4) for sensory perception, moisture, activity, mobility, nutrition, and friction and shear.
- The Braden Score is pulled forward to the Skin CP page to guide the entry of interventions.

Skin CP contains patient/caregiver skin care education, including risk for skin breakdown and prevention/treatment of problems related to skin integrity.

![](padp-version-1-admission-rn-assessment-user-manual/099.png)

Admission – RN Assessment, Skin Assessment (Skin) tab, Skin Page 1 window

1.  Click Skin.  
    Skin Page 1 displays.
2.  Populate Skin Page 1.
1.  Complete all the fields with asterisks; they are required fields.
20. Use the General observations/comments text box for additional information.

### Documenting Pressure Ulcers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Skin Page 1 tab, select Pressure ulcers and the Skin Pr Ul 1 tab becomes available.

![](padp-version-1-admission-rn-assessment-user-manual/100.png)

Admission – RN Assessment, Skin Assessment (Skin) tab, Skin Page 1 window  
Pressure ulcers selected

1.  Click Skin Pr Ul 1.  
    Skin Pr Ul 1 displays.
3.  Populate Skin Pr Ul 1.
1.  Enter Location and Stage for up to six pressure ulcer locations.  
    The fields with asterisks are required fields.
21. Enter a Description of ulcer/dressing, if appropriate.

![](padp-version-1-admission-rn-assessment-user-manual/101.png)

Admission – RN Assessment, Skin Assessment (Skin) tab, Skin Pr Ul 1 window

### Pressure Ulcer Drop-downs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](padp-version-1-admission-rn-assessment-user-manual/102.png)

Skin Assessment - Pressure Ulcer \#1/Location

![](padp-version-1-admission-rn-assessment-user-manual/103.png)

Skin Assessment - Pressure Ulcer \#1/Stage

119. To enter more than six pressure ulcer locations, select the More pressure ulcer locations check box.  
     Skin Pr Ul 2 becomes available.

![](padp-version-1-admission-rn-assessment-user-manual/104.png)

Admission – RN Assessment, Skin Assessment (Skin) tab, Skin Pr Ul 1 window  
More pressure ulcer locations selected

![](padp-version-1-admission-rn-assessment-user-manual/105.png)

Admission – RN Assessment, Other Pressure Ulcers, Skin Pr Ul 2 window

120. Click Skin Pr Ul 2.  
     Skin Pr Ul 2 displays.
121. Populate Skin Pr Ul 2.
1.  Enter Location and Stage for six additional pressure ulcer locations.  
    The fields with asterisks are required fields.
22. Enter a Description of ulcer/dressing, if appropriate.

### Documenting Skin Alterations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Skin Page 1 tab, select Other skin alterations and the Skin Alt 1 tab becomes available.

![](padp-version-1-admission-rn-assessment-user-manual/106.png)

Admission – RN Assessment, Skin Assessment (Skin) tab, Skin Page 1 window  
Other skin alterations selected

1.  Click Skin Alt 1.  
    Skin Alt 1 displays.

![](padp-version-1-admission-rn-assessment-user-manual/107.png)

Admission – RN Assessment, Skin Assessment (Skin) tab, Skin Alt 1 window  
Skin Alterations \#1-#6

122. Populate Skin Alt 1.
1.  Enter Type, Location, and Size for up to six (#1-#6) other skin alterations.  
    The fields with asterisks are required fields.
23. Enter a Description of skin alteration, if appropriate.

### Skin Alteration Drop-downs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](padp-version-1-admission-rn-assessment-user-manual/108.png)

Skin Assessment – Skin Alteration \#1/Type

![](padp-version-1-admission-rn-assessment-user-manual/109.png)

Skin Assessment – Skin Alteration \#1/Location

![](padp-version-1-admission-rn-assessment-user-manual/110.png)

Skin Assessment – Skin Alteration \#1/Size

![](padp-version-1-admission-rn-assessment-user-manual/111.png)

Admission – RN Assessment, Skin Assessment (Skin) tab, Skin Alt 1 window  
More skin alterations selected

123. To enter more than six skin alterations locations, select the More skin alterations check box.  
     Skin Alt 2 becomes available.
124. Click Skin Alt 2.  
     Skin Alt 2 displays.

![](padp-version-1-admission-rn-assessment-user-manual/112.png)

Admission – RN Assessment, Skin Assessment (Skin) tab, Skin Alt 2 window  
Skin Alterations \#7-#12

125. Populate Skin Alt 2.
1.  Enter Type, Location, and Size for up to six (#7-#12) additional skin alterations.  
    The fields with asterisks are required fields.
2.  Enter a Description of skin alteration, if appropriate.
126. Click Skin Page 3.  
     Skin Page 3 displays.

![](padp-version-1-admission-rn-assessment-user-manual/113.png)

Admission – RN Assessment, Skin Assessment (Skin) tab, Skin Page 3 window  
Braden Scale for Predicting Pressure Sore Risk

127. Populate Skin Page 3.
1.  Complete all the fields with asterisks; they are required fields.
24. Order a Nutrition Consult and/or Wound Care Consult, if necessary.  
    Refer to the instructions in *Working in the Consults* on page [15](#_Ref273355528).
128. Click Skin CP.  
     Skin CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/114.png)

Admission – RN Assessment, Skin – Problems/Interventions/Desired Outcomes, Skin CP window

129. Populate Skin CP.
1.  If you gave skin education information to the patient or caregiver, you must select Yes for Patient/caregiver education provided.
2.  Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

## Psychosocial (P/S)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Psychosocial Assessment contains information about abuse-verbal, physical, financial, sexual, and neglect. During admission, each patient receives a comprehensive psychosocial assessment.

- Suicide Risk is on P/S Page 2.
- Questions concerning elopement, contraband, and chemical dependencies are on P/S Page 3.
- Directions for the *Clinical Institute Withdrawal Assessment (CIWA)* are on the CIWA page.
1.  The CIWA Score for the patient is calculated automatically as you select a response level for nausea/vomiting, tremor, paroxysmal sweats, anxiety, agitation, tactile disturbances, auditory disturbances, visual disturbances, headache, and orientation/clouding of sensorium.
2.  The CIWA Score is pulled forward to the P/S CP page to guide the entry of interventions.

![](padp-version-1-admission-rn-assessment-user-manual/115.png)

Admission – RN Assessment, Psychosocial Assessment (P/S) tab, P/S Page 1 window

1.  Click P/S.  
    P/S Page 1 displays.
130. Populate P/S Page 1.
1.  Complete all the fields with asterisks; they are required fields.
25. If the patient answers Yes to any of the abuse questions, a Social Work Consult is required.
- Refer to the instructions in *Working in the Consults* on page [15](#_Ref273355528).
- For emphasis, the notify provider, send consult, and follow your state’s reporting regulations will be highlighted in red.
131. Click P/S Page 2.  
     P/S Page 2 (Suicide Risk Screen - Ask Patient) displays.

![](padp-version-1-admission-rn-assessment-user-manual/116.png)

Admission – RN Assessment, Psychosocial Assessment (P/S) tab, P/S Page 2 window  
Have you secretly had thoughts about hurting yourself/Yes

132. Populate P/S Page 2.
1.  Complete all the fields with asterisks; they are required fields.
26. If the patient answers Yes to Have you secretly had thoughts about hurting yourself, you must Notify provider and Keep patient under close observation.
133. Click P/S Page 3.  
     P/S Page 3 displays.

![](padp-version-1-admission-rn-assessment-user-manual/117.png)

Admission – RN Assessment, Psychosocial Assessment (P/S) tab, P/S Page 3 window

134. Populate P/S Page 3.
1.  Complete all the fields with asterisks; they are required fields.
27. Answer Yes to any of the Elopement Screen questions and a Social Work Consult is required.
- The patient is a potential wandering/elopement risk.
- Refer to the instructions in *Working in the Consults* on page [15](#_Ref273355528).
28. P/S Page 3 contains the Alcohol use section.

![](padp-version-1-admission-rn-assessment-user-manual/118.png)

Alcohol use section

135. If there is the possibility of alcohol withdrawal, select the Possibility of alcohol withdrawal check box to display the CIWA page.
1.  Complete all the CIWA fields with asterisks; they are required fields.
29. Alert the physician of the possibility of alcohol withdrawal.

![](padp-version-1-admission-rn-assessment-user-manual/119.png)

Admission – RN Assessment, Psychosocial Assessment (P/S) tab, CIWA window

136. Click P/S Page 4.  
     P/S Page 4 displays.

![](padp-version-1-admission-rn-assessment-user-manual/120.png)

Admission – RN Assessment, Psychosocial Assessment (P/S) tab, P/S Page 4 window

137. Populate P/S Page 4.  
     Use the General observations/comments text box for additional information.
138. Click P/S CP.  
     P/S CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/121.png)

Admission – RN Assessment, Psychosocial Assessment (P/S) tab, P/S PC window

139. Populate P/S CP.  
     Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

## Restraints (Rest/Restr)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two categories of restraints.

- Patient is pulling at lines/tubes used in their treatment or is unable to follow instructions, endangering their medical/surgical recovery. Patient is not violent or self-destructive
- Patient’s behavior is aggressive or violent presenting an immediate, serious danger to his/her safety or that of others

![](padp-version-1-admission-rn-assessment-user-manual/122.png)

Admission – RN Assessment, Restraints (Rest) tab, Restr Page 1 window

1.  Click Rest.  
    Restr Page 1 displays.
140. Select the Restraints Initiated/maintained check box.  
     The reasons for restraint become available.

![](padp-version-1-admission-rn-assessment-user-manual/123.png)

Admission – RN Assessment, Restraints (Rest) tab, Restr Page 1 window  
with restraints initiated/maintained

1.  When you select, Patient is pulling at lines/tubes used in their treatment or is unable to follow instructions endangering their medical/surgical recovery. Patient is not violent or self-destructive, the following window displays.

![](padp-version-1-admission-rn-assessment-user-manual/124.png)

Admission – RN Assessment, Restraints (Rest) tab, Restr Page 1 window  
Patient is pulling at lines/tubes used in their treatment or is unable to follow instructions endangering their medical/surgical recovery. Patient is not violent or self-destructive selected

2.  When you select, Patient’s behavior is aggressive or violent presenting an immediate serious danger to his/her safety or that of others, the following window displays.

![](padp-version-1-admission-rn-assessment-user-manual/125.png)

Admission – RN Assessment, Restraints (Rest) tab, Restr Page 1 window  
Patient’s behavior is aggressive or violent presenting an immediate serious danger to his/her safety  
or that of others selected

141. Populate Restr Page 1.
1.  Select a Reason for restraint.
30. Complete all the fields with asterisks; they are required fields.  
    Questions are based on standards for documenting seclusion or restraint.
142. Click Restr CP.  
     Restr CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/126.png)

Admission – RN Assessment, Restraints - Problems/Interventions/Desired Outcomes, Restr CP window

143. Populate Restr CP.  
     Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

## Mental Health (MH)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health Assessment tab contains the patient’s mental health history.

1.  Click MH.  
    MH Page 1 displays.
1.  For patients not admitted to acute psychiatry and do not have a history of specific major mental illnesses, MH Page 2 is unavailable.

![](padp-version-1-admission-rn-assessment-user-manual/127.png)

Admission – RN Assessment, Mental Health Assessment (MH) tab, MH Page 1 window  
when patient is not admitted to acute psychiatry

31. For patients admitted to acute psychiatry or have a history of a major mental illness, MH Page 2 is available and must be completed.

![](padp-version-1-admission-rn-assessment-user-manual/128.png)

Admission – RN Assessment, Mental Health Assessment (MH) tab, MH Page 1 window  
when patient is admitted to acute psychiatry

144. Populate MH Page 1.  
     Complete all the fields with asterisks; they are required fields.
145. Click MH Page 2.  
     MH Page 2 displays.

![](padp-version-1-admission-rn-assessment-user-manual/129.png)

Admission – RN Assessment, Mental Health Assessment (MH) tab, MH Page 2 window

146. Populate MH Page 2.
1.  Complete all the fields with asterisks; they are required fields.
2.  Use the General observations/comments text box for additional information.
147. Click MH CP.  
     MH CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/130.png)

Admission – RN Assessment, Mental Health Assessment (MH) tab, MH CP window

148. Populate MH CP.  
     Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

## Functional (Func)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Functional Assessment tab contains information about the patient’s independence/dependence in activities of daily living.

Directions for the *Katz Index of Independence in Activities of Daily Living* are on Func Page 1. The Total Score for the patient is calculated automatically as you select Independence/Dependence for six activities.

![](padp-version-1-admission-rn-assessment-user-manual/131.png)

Admission – RN Assessment, Functional Assessment (Func) tab, Func Page 1 window

1.  Click Func.  
    Func Page 1 displays.
149. Populate Func Page 1.  
     Complete all the fields with asterisks; they are required fields.

> **NOTE:** Refer to provider for evaluation, if patient has a Katz score of 4 or less, or a decrease in the level of independence and changes have occurred within the past month.

150. Click Func Page 2.  
     Func Page 2 displays.
- If the patient is independent and cooperative, no additional entries are necessary on Func Page 2.

![](padp-version-1-admission-rn-assessment-user-manual/132.png)

Admission – RN Assessment, Functional Assessment (Func) tab, Func Page 2 window  
when the patient is independent

- If the patient is dependent and completely uncooperative, additional entries are necessary on Func Page 2.

![](padp-version-1-admission-rn-assessment-user-manual/133.png)

Admission – RN Assessment, Functional Assessment (Func) tab, Func Page 2 window  
when the patient is dependent

151. Populate Func Page 2.
1.  Complete all the fields with asterisks; they are required fields.
32. Use the General observations/comments text box for additional information.
152. Click Func Page 3.  
     Func Page 3 displays.

![](padp-version-1-admission-rn-assessment-user-manual/134.png)

Admission – RN Assessment, Functional Assessment (Func) tab, Func Page 3 window

153. Populate Func Page 3.
1.  Complete the fields as necessary.
33. Click Print.
34. Print Func Page 3 and give it to the staff handling the move of the patient.
154. Click Func CP.  
     Func CP page displays.

![](padp-version-1-admission-rn-assessment-user-manual/135.png)

Admission – RN Assessment, Functional Assessment (Func) tab, Func CP window

155. Populate Func CP.  
     Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).

## Discharge Planning (DP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Discharge Planning tab contains information about home environment, living arrangements, and special equipment, if required for discharge.

Information about the legal/medical guardian is pulled from the question asked in P/S Page 3. You cannot edit it from the DP tab. If the information is not correct, return to P/S Page 3 to correct.

![](padp-version-1-admission-rn-assessment-user-manual/136.png)

Admission – RN Assessment, Discharge Planning (DP) tab, DP Page 1 window

1.  Click DP.  
    DP Page 1 displays.
156. Populate DP Page 1.
1.  Complete all the fields with asterisks; they are required fields.
35. Use the General observations/comments for additional information.
157. Click DP CP.  
     DP CP displays.

![](padp-version-1-admission-rn-assessment-user-manual/137.png)

Admission – RN Assessment, Discharge Planning – Problems/Interventions/Desired Outcomes,  
DP CP window

158. Populate DP CP.
1.  Complete the fields as necessary.  
    Refer to the instructions in *Working in a Care Plan* on page [11](#_Ref270329679).
36. Complete a Social Work Consult or Discharge Planning Consult, if required.  
    Refer to the instructions in *Working in the Consults* on page [15](#_Ref273355528).
37. Optional: Complete a Telehealth Consult or a Home Care Consult, if set up by your medical center.

> **NOTE:** If an item in the Anticipated Discharge Plan Goals list box contains \*\*, a Social Work Consult or Discharge Planning Consult is required.

## PCE Data (PCE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PCE (Patient Care Encounter) Data tab is optional and may not be set up at your medical center. The PCE tab includes a list of all clinical reminders due for the patient.

> **NOTE:** The clinical reminders must be set up by your facility.

Use the PCE tab to document specific clinical reminders completed by the inpatient nurse at admission.

1.  Click PCE.  
    PCE tab displays.

![](padp-version-1-admission-rn-assessment-user-manual/138.png)

Admission – RN Assessment, PCE Data (PCE) tab window with reminders loading

![](padp-version-1-admission-rn-assessment-user-manual/139.png)

Admission – RN Assessment, PCE Data (PCE) tab window after reminders are loaded

### Reminders Due (Display Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The list of all clinical reminders due for the patient is for display only. You cannot take action on the clinical reminders from within the assessment template.

### Clinical Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select a clinical reminder in the Reminders Due list box.
159. Click Clinical Maintenance.  
     Information about when the reminder is due or was last done, displays in the Maintenance Results list box.

![](padp-version-1-admission-rn-assessment-user-manual/140.png)

Clinical Maintenance

### Reminder Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click Reminder Inquiry.  
Information about the logic of the selected reminder displays in the Inquiry Results list box.

![](padp-version-1-admission-rn-assessment-user-manual/141.png)

Reminder Inquiry

### Resolve Inpatient Nursing Clinical Reminders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select an item in the Inpatient Nursing PCE Information list box.

![](padp-version-1-admission-rn-assessment-user-manual/142.png)

PCE Data, Resolve Inpatient Nursing Clinical Reminders

160. Click Resolve.  
     The Resolve Reminder Pain Risk, Mgmt, and Assessment window displays with items appropriate for the selected item.

![](padp-version-1-admission-rn-assessment-user-manual/143.png)

Resolve Reminder Pain Risk, Mgmt, and Assessment window

161. Select a radio button from Received?
162. Select an item from Level of Understanding.
163. Click Resolve.  
     Information pop-up displays indicating the reminder is resolved.

![](padp-version-1-admission-rn-assessment-user-manual/144.png)

Information pop-up: Reminder resolved!

164. Click OK.  
     The text that is added to the Progress Note displays in the Text (will be added to note) text box.

![](padp-version-1-admission-rn-assessment-user-manual/145.png)

Text (will be added to note)

## View Text (View Text)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Text tab is a review of all the information entered for a patient during the admission assessment.

![](padp-version-1-admission-rn-assessment-user-manual/146.png)

Admission – RN Assessment View Text tab window

1.  Click View Text.  
    The View Text window scrolls through the admission assessment for review.
165. Review the patient admission assessment.

### Signing Note and Consults from within the Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the assessment, you may be prompted to enter a mandatory consult, which will be uploaded with the assessment note.

> **NOTE:** Manage consults according to medical center policy. If nurses at your site do not order consults, upload a mandatory consult, but do not sign it.  
The identified provider will be notified that there is a consult to sign.

Go to CPRS to sign your uploaded, *unsigned* notes and consults.

You can sign *unsigned* notes after the upload from the View Text tab in the template.

1.  Click View Text.

![](padp-version-1-admission-rn-assessment-user-manual/147.png)

Admission – RN Assessment with Sign Note/Consults button

13. Click Sign Note/Consults.  
    If the button does not display, upload again.

![](padp-version-1-admission-rn-assessment-user-manual/148.png)

Admission – RN Assessment with Sign Note/Consults button

> **NOTE:** If there is only a note to sign, the button is Note.  
If there is a consult to sign, the button is Sign Note/Consults.

14. Enter your electronic signature and click Accept e-sig.  
    Information pop-up displays, *Note signed!*.
166. Click OK.
167. To prevent the signing of an uploaded note, click Cancel e-sig.

> **NOTE:** It is safer to go to CPRS, read the note in CPRS, and sign the note in CPRS.

- An unsigned note can be edited.
- A signed note cannot be edited.

# Patient Unable to Respond

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An incomplete admission assessment is filed when the patient cannot respond to admission assessment questions and there is no caregiver available to provide the necessary data.

The following screen captures are examples of the tabs when No is selected for Patient/family/support person able to respond to questions.

![](padp-version-1-admission-rn-assessment-user-manual/149.png)

Admission – RN Assessment, General Information (Gen Inf) tab, Gen I Page 1 window

![](padp-version-1-admission-rn-assessment-user-manual/150.png)

Admission – RN Assessment, General Information (Gen Inf) tab, Gen I Page 2 window

![](padp-version-1-admission-rn-assessment-user-manual/151.png)

Admission – RN Assessment, General Information (Gen Inf) tab, Gen I Page 3 window

![](padp-version-1-admission-rn-assessment-user-manual/152.png)

Admission – RN Assessment, Educational Assessment (Educ) tab, Educ Page 1 window

![](padp-version-1-admission-rn-assessment-user-manual/153.png)

Admission – RN Assessment, Pain Assessment (Pain) tab, Pain Page 1 window

![](padp-version-1-admission-rn-assessment-user-manual/154.png)

Admission – RN Assessment, Respiratory Assessment (Resp) tab, Resp Page 1 window

![](padp-version-1-admission-rn-assessment-user-manual/155.png)

Admission – RN Assessment, Respiratory Assessment tab, Resp Page 3 window

![](padp-version-1-admission-rn-assessment-user-manual/156.png)

Admission – RN Assessment, Neurological Assessment (Neuro) tab, Neuro Page 1 window

![](padp-version-1-admission-rn-assessment-user-manual/157.png)

Admission – RN Assessment, Neurological Assessment (Neuro) tab, Neuro Page 2 window

![](padp-version-1-admission-rn-assessment-user-manual/158.png)

Admission – RN Assessment, Gastrointestinal Assessment (GI) tab, GI Page 1 window

![](padp-version-1-admission-rn-assessment-user-manual/159.png)

Admission – RN Assessment, Gastrointestinal Assessment (GI) tab, GI Page 2 window

![](padp-version-1-admission-rn-assessment-user-manual/160.png)

Admission – RN Assessment, Gastrointestinal Assessment (GI) tab, GI Page 3 window

![](padp-version-1-admission-rn-assessment-user-manual/161.png)

Admission – RN Assessment, Genitourinary Assessment (GU) tab, GU Page 1 window

![](padp-version-1-admission-rn-assessment-user-manual/162.png)

Admission – RN Assessment, Musculoskeletal Assessment (M/S) tab, M/S Page 1 window

![](padp-version-1-admission-rn-assessment-user-manual/163.png)

Admission – RN Assessment, Musculoskeletal Assessment (M/S) tab, M/S Page 2 window

![](padp-version-1-admission-rn-assessment-user-manual/164.png)

Admission – RN Assessment, Skin Assessment (Skin) tab, Skin Page 1 window

![](padp-version-1-admission-rn-assessment-user-manual/165.png)

Admission – RN Assessment, Psychosocial Assessment (P/S) tab, P/S Page 1 window

![](padp-version-1-admission-rn-assessment-user-manual/166.png)

Admission – RN Assessment, Psychosocial Assessment (P/S) tab, P/S Page 2 window

![](padp-version-1-admission-rn-assessment-user-manual/167.png)

Admission – RN Assessment, Psychosocial Assessment (P/S) tab, P/S Page 3 window

![](padp-version-1-admission-rn-assessment-user-manual/168.png)

Admission – RN Assessment, Mental Health Assessment (MH) tab, MH Page 1 window

![](padp-version-1-admission-rn-assessment-user-manual/169.png)

Admission – RN Assessment, Mental Health Assessment (MH) tab, MH Page 2 is unavailable

![](padp-version-1-admission-rn-assessment-user-manual/170.png)

Admission – RN Assessment, Functional Assessment (Func) tab, Func Page 1 window

![](padp-version-1-admission-rn-assessment-user-manual/171.png)

Admission – RN Assessment, Functional Assessment (Func) tab, Func Page 2 window

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADPAC</td>
<td>Automated Data Processing Application Coordinator</td>
</tr>
<tr class="even">
<td>ART</td>
<td>Adverse Reactions Tracking</td>
</tr>
<tr class="odd">
<td>BCE</td>
<td>Bar Code Expansion</td>
</tr>
<tr class="even">
<td>BCE-PPI</td>
<td>Bar Code Expansion-Positive Patient Identification</td>
</tr>
<tr class="odd">
<td>BCMA</td>
<td>Bar Code Medication Administration</td>
</tr>
<tr class="even">
<td>Belong</td>
<td>Belongings</td>
</tr>
<tr class="odd">
<td>CAC</td>
<td>Clinical Application Coordinator</td>
</tr>
<tr class="even">
<td>CIWA</td>
<td>Clinical Institute Withdrawal Assessment.--CIWA</td>
</tr>
<tr class="odd">
<td>Class 1 (C1)</td>
<td>Software produced inside of the Office of Enterprise Development (PD) organization</td>
</tr>
<tr class="even">
<td>Class 3 (C3)</td>
<td><p>Also known as Field Developed Software</p>
<p>Refers to all VHA software produced outside of the Office of Enterprise Development (PD) organization</p></td>
</tr>
<tr class="odd">
<td>CMS</td>
<td>Centers for Medicaid and Medicare Services</td>
</tr>
<tr class="even">
<td>COTS</td>
<td>Commercial Off the Shelf</td>
</tr>
<tr class="odd">
<td>CP</td>
<td>Care Plan</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td>Computerized Patient Record System</td>
</tr>
<tr class="odd">
<td>CV</td>
<td>Cardiovascular Assessment</td>
</tr>
<tr class="even">
<td>Delphi</td>
<td>Programming language used to develop the CPRS chart</td>
</tr>
<tr class="odd">
<td>DFN</td>
<td>Data File Number</td>
</tr>
<tr class="even">
<td>DP</td>
<td>Discharge Planning</td>
</tr>
<tr class="odd">
<td>Educ</td>
<td>Educational Assessment</td>
</tr>
<tr class="even">
<td>Func</td>
<td>Functional Assessment</td>
</tr>
<tr class="odd">
<td>Gen Inf</td>
<td>General Information tab</td>
</tr>
<tr class="even">
<td>GI</td>
<td>Gastrointestinal Assessment</td>
</tr>
<tr class="odd">
<td>GU</td>
<td>Genitourinary Assessment</td>
</tr>
<tr class="even">
<td>GUI</td>
<td>Graphical User Interface</td>
</tr>
<tr class="odd">
<td>ICD</td>
<td>International Classification of Diseases</td>
</tr>
<tr class="even">
<td>ICN</td>
<td>The patient’s national identifier, Integration Control Number</td>
</tr>
<tr class="odd">
<td>IDPA</td>
<td>Interdisciplinary Patient Assessment - involves multiple disciplines responsible for assessing the patient from their perspective and expertise.</td>
</tr>
<tr class="even">
<td>IDPC</td>
<td>Interdisciplinary Plan of Care - The entry of treatment plans by multiple disciplines to meet JCAHO requirements</td>
</tr>
<tr class="odd">
<td>IV</td>
<td>Intravenous</td>
</tr>
<tr class="even">
<td>IV Central</td>
<td>Central IV lines</td>
</tr>
<tr class="odd">
<td>IV Dialysis</td>
<td>IV Dialysis ports</td>
</tr>
<tr class="even">
<td>IV Periph</td>
<td>IV Peripheral lines</td>
</tr>
<tr class="odd">
<td>JCAHO</td>
<td>Joint Commission on Accreditation of Healthcare Organizations</td>
</tr>
<tr class="even">
<td>LPN</td>
<td>Licensed Practical Nurse</td>
</tr>
<tr class="odd">
<td>M/S</td>
<td>Musculoskeletal Assessment</td>
</tr>
<tr class="even">
<td>MAS</td>
<td>Medical Administration Service</td>
</tr>
<tr class="odd">
<td>MH</td>
<td>Mental Health Assessment</td>
</tr>
<tr class="even">
<td>MRSA</td>
<td>Methicillin-Resistant Staphylococcus Aureus</td>
</tr>
<tr class="odd">
<td>NAA</td>
<td>Nursing Admission Assessment</td>
</tr>
<tr class="even">
<td>Neuro</td>
<td>Neurological Assessment</td>
</tr>
<tr class="odd">
<td>NHIA</td>
<td>Nursing Healthcare Informatics Alliance</td>
</tr>
<tr class="even">
<td>NPAT</td>
<td>National Patient Assessment Templates</td>
</tr>
<tr class="odd">
<td>NUPA</td>
<td>Namespace assigned to the Patient Assessment Documentation Package (PADP) by Database Administrator</td>
</tr>
<tr class="even">
<td>OED</td>
<td>Office of Enterprise Development</td>
</tr>
<tr class="odd">
<td>OERR</td>
<td>Order Entry Results Reporting</td>
</tr>
<tr class="even">
<td>OIT</td>
<td>Office of Information and Technology</td>
</tr>
<tr class="odd">
<td>ONS</td>
<td>Office of Nursing Services</td>
</tr>
<tr class="even">
<td>Orient</td>
<td>Orientation to Unit</td>
</tr>
<tr class="odd">
<td>P/S</td>
<td>Psychosocial Assessment</td>
</tr>
<tr class="even">
<td>PADP</td>
<td>Patient Assessment Documentation Package</td>
</tr>
<tr class="odd">
<td>Pain</td>
<td>Pain Assessment</td>
</tr>
<tr class="even">
<td>PC</td>
<td>Plan of Care</td>
</tr>
<tr class="odd">
<td>PCE</td>
<td>Patient Care Encounter</td>
</tr>
<tr class="even">
<td>PD</td>
<td>Product Development</td>
</tr>
<tr class="odd">
<td>PHR</td>
<td>Patient Health Record</td>
</tr>
<tr class="even">
<td>Prob</td>
<td>Problems/Interventions/Desired Outcomes tab in the RN Reassessment</td>
</tr>
<tr class="odd">
<td>Resp</td>
<td>Respiratory Assessment</td>
</tr>
<tr class="even">
<td>Rest (or Restr)</td>
<td>Restraints</td>
</tr>
<tr class="odd">
<td>RN</td>
<td>Registered Nurse</td>
</tr>
<tr class="even">
<td>RPC</td>
<td>Remote Procedure Call</td>
</tr>
<tr class="odd">
<td>RSD</td>
<td>Requirements Specification Document</td>
</tr>
<tr class="even">
<td>Section 508</td>
<td>Under Section 508 of the Rehabilitation Act, as amended (29 U.S.C. 794d) Public Law 106-246 (http://va.gov/accessible) agencies must provide employees and members of the public who have disabilities access to electronic and information technology that is comparable to the access available to employees and members of the public who are not individuals with disabilities</td>
</tr>
<tr class="odd">
<td>Skin</td>
<td>Skin Assessment</td>
</tr>
<tr class="even">
<td>SNOMED – CT</td>
<td>Systemized Nomenclature of Medicine Clinical Terms</td>
</tr>
<tr class="odd">
<td>TIU</td>
<td>Text Integration Utilities Program<br />
All text in CPRS is stored in TIU</td>
</tr>
<tr class="even">
<td>TJC</td>
<td>The Joint Commission</td>
</tr>
<tr class="odd">
<td>V/S</td>
<td>Vital Signs</td>
</tr>
<tr class="even">
<td>VA</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="odd">
<td>VAMC</td>
<td>Department of Veterans Affairs Medical Center</td>
</tr>
<tr class="even">
<td>VANOD</td>
<td>VA Nursing Outcomes Database</td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="even">
<td>VistA</td>
<td><p>Veterans Health Information Systems and Technology Architecture</p>
<p>An enterprise-wide information system built around an electronic health record used throughout the Department of Veterans Affairs medical system.</p></td>
</tr>
<tr class="odd">
<td>Vital Qualifiers</td>
<td><p>Provide detail in to the unit of measurement used with the vital signs.</p>
<p>Height in inches or centimeters?</p>
<p>Weight in pounds or kilograms?</p></td>
</tr>
</tbody>
</table>
For additional PADP information, refer to the user manuals for *RN Reassessment*, *Admission – Nursing Data Collection*, and *Interdisciplinary Plan of Care*.
Documentation for NUPA Version 1.0 is also available on
- VA Software Documentation Library in the Clinical Section  
  <http://www4.va.gov/vdl/>
- PADP SharePoint for NUPA Version 1.0 <http://vaww.oed.portal.va.gov/programs/class3_to_class1/padp/field_development>

# Appendix A Assessment Contingency Note

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](padp-version-1-admission-rn-assessment-user-manual/172.png)

During system downtimes, print a copy of the attached *Assessment Contingency Note* and use it to perform an *Admission RN Assessment*.