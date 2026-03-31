---
title: PADP Version 1 Admission-Nursing Data Collection User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Admission-Nursing Data Collection
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
description: - [Revision History](#revision-history) - [# Introduction](#introduction) - [Using Admission – Nursing Data Collection](#using-admission-nursing-data-collection) - [Opening Admission – Nursing Data Collection](#opening-admission-nursing-data-collection) - [No Previously Saved Information](#no-previo
audience: 
keywords: 
  - admission
  - nursing
  - collection
  - class
  - patient
  - table
  - padp
  - manual
  - contents
  - version
page_count: 0
word_count: 5083
section_count: 8
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Assessment_Documentation_Package/nupa1_0_dcum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Assessment_Documentation_Package/nupa1_0_dcum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=193"
---

---
title: Patient Assessment Documentation Package (PADP)
---

C3-C1 Conversion Project

Admission - Nursing Data Collection User Manual  
for NUPA Version 1.0

![](padp-version-1-admission-nursing-data-collection-user-manual/001.png)

April 2012

Office of Information and Technology (OIT)

Office of Enterprise Development (OED)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [# Introduction](#introduction)
- [Using Admission – Nursing Data Collection](#using-admission-nursing-data-collection)
  - [Opening Admission – Nursing Data Collection](#opening-admission-nursing-data-collection)
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
  - [Working in the Template](#working-in-the-template)
    - [Moving through the Template with a Mouse](#moving-through-the-template-with-a-mouse)
    - [Moving through the Template without a Mouse](#moving-through-the-template-without-a-mouse)
- [Navigating the Admission - Nursing Data Collection Tabs](#navigating-the-admission-nursing-data-collection-tabs)
  - [Belongings (Belong)](#belongings-belong)
  - [Orientation to Unit (Orient)](#orientation-to-unit-orient)
  - [Vital Signs (V/S)](#vital-signs-vs)
  - [View Text (View Text)](#view-text-view-text)
    - [Signing Note and Consults from within the Template](#signing-note-and-consults-from-within-the-template)
- [Glossary](#glossary)
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
<td>December 2010</td>
<td>1.0</td>
<td><p>Initial version for v1.0</p>
<p>Split Assessment manual into two manuals</p>
<p><em>Admission – RN Assessment User Manual</em></p>
<p><em>Nursing Data Collection User Manual</em></p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>January 2011</td>
<td>1.1</td>
<td><ul>
<li><p>Changed dates to January 2011</p></li>
<li><p>Updated with additional comments from Judy</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>February 2011</td>
<td>1.2</td>
<td><ul>
<li><p>Changed dates to February 2011</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>March 2011</td>
<td>1.3</td>
<td><ul>
<li><p>Changed dates to April 2011</p></li>
</ul>
<ul>
<li><p>Updated with Judy’s comments</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>April 2011</td>
<td>1.4</td>
<td>Updated RoboHelp with this file</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>May 2011</td>
<td>1.5</td>
<td><ul>
<li><p>Changed dates to May 2011</p></li>
<li><p>Added (NUPA*1) namespace</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>October 2011</td>
<td>1.6</td>
<td><ul>
<li><p>Added C3-C1 Conversion Project</p></li>
<li><p>Changed dates to October 2011</p></li>
<li><p>Prepped for national release</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>November 2011</td>
<td>1.7</td>
<td><ul>
<li><p>Changed dates to November 2011</p></li>
<li><p>Updated for build v14</p></li>
<li><p>Changed dates to December 2011</p></li>
<li><p>Updated for build v15</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>December 2011</td>
<td>1.8</td>
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
<td>1.9</td>
<td><ul>
<li><p>Changed NUPA 1.0 to NUPA Version 1.0</p></li>
<li><p>Updated for build v16</p></li>
<li><p>Changed dates to February 2012</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>February 2012</td>
<td>2.0</td>
<td>Updated the Vitals tab</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>March 2012</td>
<td>2.1</td>
<td><ul>
<li><p>Changed dates to March 2012</p></li>
<li><p>Prepped for April national release</p></li>
<li><p>Changed dates to April 2012</p></li>
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

# Using Admission – Nursing Data Collection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Data Collection tabs contain information that is collected by any nursing personnel. This information is located on tabs: Belongings, Orientation to the Unit, and Vital Signs.

## Opening Admission – Nursing Data Collection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You access the Admission -Nursing Data Collection through CPRS from the Tools menu.

1.  Open CPRS.
8.  Select a patient.
9.  Click Tools.
10. Select Data Collection.  
    Enter a patient window automatically opens to the CPRS patient.

> **NOTE:** You may have to re-enter your CPRS access and verify codes, depending on local site setup.

![](padp-version-1-admission-nursing-data-collection-user-manual/002.png)

Access through CPRS

### No Previously Saved Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Enter a patient window displays.

![](padp-version-1-admission-nursing-data-collection-user-manual/003.png)

Admission – Nursing Data Collection, Enter a patient window with no previously saved information

1.  Select an Assessment Type.
11. Click Start Note.  
    The nursing data collection template opens to the Belongings tab for the CPRS patient.

### Previously Entered Information Available for One Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](padp-version-1-admission-nursing-data-collection-user-manual/004.png)

Patient selection window with previously entered information available for one patient

#### Restore Patient’s Data/No

If you previously entered data on one patient, you are prompted with: *You have previously saved data on a note for patient \<PADPPATIENT,ONE \>*

1.  Select an Assessment Type.
2.  Select No.  
    The patient’s information is deleted, but the Internal Entry Number (IEN) for the patient displays in the Enter a patient text box.
12. Click Start Note.  
    The template opens to the Belongings tab and you can enter new data for that CPRS patient.
13. Optional: You can delete the IEN of that CPRS patient, enter the name of a different patient, and click Start Note.

> **NOTE:** The Internal Entry Number (IEN) is a unique, computer-generated number that identifies a specific patient in your system. The IEN has no impact on the completed assessment, nor does it display again.

#### Restore Patient’s Data/Yes

If you previously entered data on one patient, you are prompted with: *You have previously saved data on a note for patient \<PADPPATIENT,ONE \>*

1.  Select an Assessment Type.
14. Select Yes.
15. Click Start Note.  
    The template opens to the Belongings tab for the CPRS patient with the data restored.

### Previously Entered Information Available for Two or More Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have previously stored data from more than one patient, you are asked if you want to view a list of those patients.

![](padp-version-1-admission-nursing-data-collection-user-manual/005.png)

Patient selection window with previously entered information available for more than one patient

#### View the Patients?/No

If you select No, the patient’s name displays in the Enter a patient text box as a number that identifies the CPRS patient.

1.  Select an Assessment Type.
16. Click Start Note.  
    The template opens to the Belongings tab.

![](padp-version-1-admission-nursing-data-collection-user-manual/006.png)

Patient selection window with No selected

#### View the Patients?/Yes

1.  Select Yes.
17. Select an Assessment Type.  
    Patient Selection window displays with a list of patients with saved data.

![](padp-version-1-admission-nursing-data-collection-user-manual/007.png)

Patient Selection List

#### Patient on the List

1.  Select a name.
18. Click OK.  
    The template opens to the Belongings tab.

#### Patient not on the List

1.  Click Cancel.  
    The number that represents your CPRS patient is in the Enter a patient text box.
19. Click the Start Note.  
    The template opens to the Belongings tab.

![](padp-version-1-admission-nursing-data-collection-user-manual/008.png)

Admission – Nursing Data Collection, Belongings (Belong) tab window, Bel Page 1

### Patient not yet Assigned to an Inpatient Bed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a patient is not assigned an inpatient bed, a location pop-up automatically displays over the Belongings window.

![](padp-version-1-admission-nursing-data-collection-user-manual/009.png)

Location pop-up: Select visit location

1.  Select a current patient location, i.e., outpatient clinic.  
    Navigate quickly to the current location by entering the first letter of the location.
20. Click OK.

## Saving and Uploading Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto Save

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data are saved automatically. Frequency of auto save is set locally.

![](padp-version-1-admission-nursing-data-collection-user-manual/010.png)

Saving data: percentage saved indicator  
(bottom right corner of the window)

### Manual Save

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can save data by using the File menu on any tab.

![](padp-version-1-admission-nursing-data-collection-user-manual/011.png)

Admission – Nursing Data Collection window, File menu

### Upload Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a note you must upload the data into VistA and CPRS:

1.  Open the File menu on any tab and select Upload Data.  
    Results from your upload display, verifying that the data is uploaded.

![](padp-version-1-admission-nursing-data-collection-user-manual/012.png)

Admission – Nursing Data Collection, Upload results window

> **NOTE:** The *unsigned* note, selected consults, and PCE data/Health Factors are uploaded into CPRS and VistA.

21. If the information is incomplete, an Error Listing window displays indicating the pages within specific tabs that require attention.
- The tabs with pages that require attention are blue.

![](padp-version-1-admission-nursing-data-collection-user-manual/013.png)

Admission – Nursing Data Collection, Error Listing window

- Once the pages are completed, the tab returns to gray.
1.  Double-click an item to go to the page that requires attention.
1.  When all the errors are completed, select Upload Data again.

### Save and Exit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To save data and temporarily leave the template:

1.  Open the File menu on any tab.
22. Select Save and Exit.
23. When you re-open the template, your previously entered data is there.

### Save Now

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To save data, but not close the template and continue to enter data:

1.  Open the File menu on any tab.
24. Select Save Now.
25. Continue to enter data for the current patient.

### Exit 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From any tab, click X in the top right corner of the window.  
    Warning message displays.

![](padp-version-1-admission-nursing-data-collection-user-manual/014.png)

Warning pop-up: Do you really wish to exit?

26. Click Yes.
27. From any tab, open the File menu and click Exit.  
    Warning message displays.
28. Click Yes.

### Signing Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Go to CPRS to sign your uploaded, *unsigned* notes.

You can also sign *unsigned* notes after the upload from the View Text tab in the template.

1.  Click View Text.

![](padp-version-1-admission-nursing-data-collection-user-manual/015.png)

Admission – Nursing Data Collection, View Text tab after upload

29. Click Sign Note/Consults.

![](padp-version-1-admission-nursing-data-collection-user-manual/016.png)

Admission – Nursing Data Collection with Sign Note/Consults button

30. Enter your electronic signature and click Accept e-sig.
31. To prevent the signing of an uploaded note, click Cancel e-sig.

## Working in the Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To complete the template, move through the fields from left to right and then down.
32. The active page displays first and the page tab is white.
33. Each field with an asterisk (\*) must have an entry.
34. A field without an asterisk is optional.
35. You must enter optional information where appropriate for the patient.

### Moving through the Template with a Mouse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click a tab at the bottom of any of the Admission - Nursing Data Collection windows.  
    The selected tab opens.

![](padp-version-1-admission-nursing-data-collection-user-manual/017.png)

Admission – Nursing Data Collection tabs

36. Open the Tabs menu and select a tab from the list.  
    The selected tab opens.

![](padp-version-1-admission-nursing-data-collection-user-manual/018.png)

Admission – Nursing Data Collection Tabs menu

### Moving through the Template without a Mouse

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Ctrl-Alt Keys

You can move from tab to tab using Ctrl+Alt+\<letter\>. The list contains the keys to use for each of the tabs.

| Tab         | Keys        |
|-------------|-------------|
| Belongings  | Ctrl+Alt+B  |
| Orientation | Ctrl +Alt+O |
| Vital Signs | Ctrl +Alt+U |
| View Text   | Ctrl +Alt+V |

#### #### Go to radiogroup

The Go to radiogroup: is designed to navigate the templates with keyboard commands, when the mouse stops working during a patient assessment. It also satisfies the 508-compliant requirement, under Section 508 of the Rehabilitation Act, to be able to navigate the templates without using a mouse.

![](padp-version-1-admission-nursing-data-collection-user-manual/019.png)

Go button

1.  Use the Tab key to move to the bottom of the page.
37. Use the arrow keys to move up/down in the Go to radiogroup: list.
38. Click Go.

or

1.  Click the drop-down arrow in the Go to radiogroup: drop-down list.
39. Select a radiogroup.
40. Click Go.

# Navigating the Admission - Nursing Data Collection Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Admission – Nursing Data Collection template has four tabs. It can be part of the Admission – RN Assessment template or as a standalone template.

## Belongings (Belong)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Belongings tab contains information about items the patient brought to the hospital, disposition of the items, and items that the patient took home.

1.  Admission – Nursing Data Collection opens to the Belongings (Belong) tab, Bel Page 1.

![](padp-version-1-admission-nursing-data-collection-user-manual/020.png)

Admission – Nursing Data Collection, Belongings (Belong) tab, Bel Page 1 window  
Does patient have items to inventory/Not at this time

![](padp-version-1-admission-nursing-data-collection-user-manual/021.png)

Admission – Nursing Data Collection, Belongings (Belong) tab, Bel Page 1 window  
Does patient have items to inventory/Yes

41. Populate Bel Page 1.
42. Select Yes or No in the Does patient have items to inventory radiogroup.
- If you select No, go on to another tab.
- If you select Yes, additional fields are made available.
1.  Make appropriate selections on Bel Page 1.
2.  Click Print to print the page.
43. Click Bel Page 2.  
    Bel Page 2 displays.

![](padp-version-1-admission-nursing-data-collection-user-manual/022.png)

Admission – Nursing Data Collection, Belongings (Belong) tab, Bel Page 2 window

44. Populate Bel Page 2.
1.  Complete all the fields with asterisks; they are required fields.
2.  Click Print to print the page.
45. Click Bel Page 3.  
    Bel Page 3 displays.

![](padp-version-1-admission-nursing-data-collection-user-manual/023.png)

Admission – Nursing Data Collection, Belongings (Belong) tab, Bel Page 3 window

46. Populate Bel Page 3.
1.  Complete all the fields with asterisks; they are required fields.
3.  Click Print to print the page.
47. Click Bel Page 4.  
    Bel Page 4 displays.

![](padp-version-1-admission-nursing-data-collection-user-manual/024.png)

Admission – Nursing Data Collection, Belongings (Belong) tab, Bel Page 4 window

48. Populate Bel Page 4.
1.  Complete all the fields with asterisks; they are required fields.
4.  Click Print to print the page.

## Orientation to Unit (Orient)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Orientation to Unit tab allows you to indicate the unit areas to which you oriented the patient.

1.  Click Orient.  
    Orient window displays.

![](padp-version-1-admission-nursing-data-collection-user-manual/025.png)

Admission – Nursing Data Collection, Orientation to Unit (Orient) tab window

49. In the Patient/family/support person oriented to unit list box, select:
- Yes-patient oriented to unit or
- Yes-family/support person oriented to unit
- No-patient unable to respond
- No family/support person available

> Oriented to list box displays with a list of orientation activities.

![](padp-version-1-admission-nursing-data-collection-user-manual/026.png)

Admission – Nursing Data Collection, Orientation to Unit (Orient) tab window  
Yes-patient oriented to unit

![](padp-version-1-admission-nursing-data-collection-user-manual/027.png)

Admission – Nursing Data Collection, Orientation to Unit (Orient) tab window  
Yes-family/support person oriented to unit

![](padp-version-1-admission-nursing-data-collection-user-manual/028.png)

Admission – Nursing Data Collection, Orientation to Unit (Orient) tab window  
No-patient unable to respond

![](padp-version-1-admission-nursing-data-collection-user-manual/029.png)

Admission – Nursing Data Collection, Orientation to Unit (Orient) tab window  
No family/support person available

50. In the Oriented to list box, select one or more areas to which you oriented the patient.

## Vital Signs (V/S)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vital Signs tab allows you to document the patient’s vital signs at admission. The vital signs include temperature, pulse, respiration, blood pressure, height, weight, pain, pulse oximetry, and circumference /girth.

> **NOTE:** When you click Upload Vitals, vital signs are uploaded immediately into the Vitals package.

![](padp-version-1-admission-nursing-data-collection-user-manual/030.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window

1.  Click V/S.  
    V/S displays.
1.  Complete all the fields with asterisks; they are required fields.
5.  Click each Click to enter qualifiers, to select qualifiers for each of the vitals.

> **NOTE:** Remember to enter units where appropriate.  
Example

- Entering the temperature, depending on the type of thermometer used, select C for Centigrade or F for Fahrenheit.
- Entering the height and weight, depending on the instruments used, select CM or IN and KG or LB.

![](padp-version-1-admission-nursing-data-collection-user-manual/031.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window, Qualifiers - Temp

![](padp-version-1-admission-nursing-data-collection-user-manual/032.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window, Qualifiers - Pulse

![](padp-version-1-admission-nursing-data-collection-user-manual/033.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window, Qualifiers - Resp

![](padp-version-1-admission-nursing-data-collection-user-manual/034.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window, Qualifiers - BP

![](padp-version-1-admission-nursing-data-collection-user-manual/035.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window, Qualifiers – Height

![](padp-version-1-admission-nursing-data-collection-user-manual/036.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window, Qualifiers - Weight

![](padp-version-1-admission-nursing-data-collection-user-manual/037.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window, Qualifiers – Pulse Ox

![](padp-version-1-admission-nursing-data-collection-user-manual/038.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window, Qualifiers - Circumference

51. Click Save Qualifiers, after selecting qualifiers for the individual vitals.
52. To remove incorrect qualifiers entered in error, click Cancel *before saving*.
53. Click Upload Vitals.  
    Information pop-up displays.

![](padp-version-1-admission-nursing-data-collection-user-manual/039.png)

Information pop-up: Vitals will now be uploaded.

54. Click OK.  
    Information pop-up displays.

![](padp-version-1-admission-nursing-data-collection-user-manual/040.png)

Information pop-up: Vitals uploaded!

55. Click OK.

![](padp-version-1-admission-nursing-data-collection-user-manual/041.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window with Qualifiers

56. If you select the Vitals cannot be taken at this time or the patient refused check box,  
    enter a reason in the \*Why were vitals not taken text box in the lower left corner of the page.

![](padp-version-1-admission-nursing-data-collection-user-manual/042.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window  
Vitals cannot be taken at this time or patient refused

57. If you select the Could not obtain height and/or the Could not obtain weight check boxes at time of assessment, enter a reason in the \*Why were vitals not taken text box in the lower left corner of the page.

![](padp-version-1-admission-nursing-data-collection-user-manual/043.png)

Admission – Nursing Data Collection, Vitals (V/S) tab window  
Could not obtain height/Could not obtain weight

## View Text (View Text)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Text tab is a review of all the information entered for a patient during data collection.

![](padp-version-1-admission-nursing-data-collection-user-manual/044.png)

Admission – Nursing Data Collection, View Text Tab, after Upload

1.  Click View Text.  
    The View Text window scrolls through the data collection for review.
58. Review the patient data.
59. Open the File menu and select Upload Data.  
    Upload results window displays.

### Signing Note and Consults from within the Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Manage consults according to medical center policy. If nurses at your site do not order consults, upload a mandatory consult, but do not sign it.  
The identified provider will be notified that there is a consult to sign.

You can sign *unsigned* notes after the upload from the View Text tab in the template.

1.  Click Close on the Upload results window.  
    Sign Note/Consults button displays.

![](padp-version-1-admission-nursing-data-collection-user-manual/045.png)

Admission – Nursing Data Collection with Sign Note/Consults button

60. Click Sign Note/Consults.  
    If the button does not display, upload again.

![](padp-version-1-admission-nursing-data-collection-user-manual/046.png)

Admission – Nursing Data Collection with Sign Note/Consults button

> **NOTE:** If there is only a note to sign, the button is Note.  
If there is a consult to sign, the button is Sign Note/Consults.

61. Enter your electronic signature code and click Accept e-sig.  
    Information pop-up displays, *Note signed!*.
62. Click OK.
63. To prevent the signing of an uploaded note, click Cancel e-sig.

> **NOTE:** It is safer to go to CPRS, read the note in CPRS, and sign the note in CPRS.

- An unsigned note can be edited.
- A signed note cannot be edited.

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
For additional PADP information, refer to the user manuals for *Admission – RN Assessment*, *RN Reassessment*, and *Interdisciplinary Plan of Care*.
Documentation for NUPA Version 1.0 is also available on
- VA Software Documentation Library in the Clinical Section  
  <http://www4.va.gov/vdl/>
- PADP SharePoint for NUPA Version 1.0 <http://vaww.oed.portal.va.gov/programs/class3_to_class1/padp/field_development>
