---
title: SR*3*166 Surgery NSQIP-CICSP 2008 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Surgery NSQIP-CICSP 2008
app_code: SR
app_name: Surgery
section: CLI
app_status: archive
pkg_ns: SR
patch_ver: 3
patch_id: SR*3*166
group_key: "SR:SR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - surgery
  - contents
  - risk
  - updates
  - nsqip
  - assessment
  - enhancements
  - edit
  - transmissions
page_count: 0
word_count: 1378
section_count: 7
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2008
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_p166_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_p166_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=403"
---

![](sr-3-166-surgery-nsqip-cicsp-2008-release-notes/001.png)

Surgery NSQIP-CICSP Enhancements 2008

Release Notes

SR\*3\*166

April 2008

VistA Health Systems Design & Development
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [NSQIP Enhancements](#nsqip-enhancements)
- [Field Updates](#field-updates)
- [Option Updates](#option-updates)
  - [List of Surgery Risk Assessments](#list-of-surgery-risk-assessments)
  - [M&M Verification Report](#mm-verification-report)
  - [Risk Model Lab Test](#risk-model-lab-test)
  - [Anesthesia Technique (Enter/Edit)](#anesthesia-technique-enteredit)
  - [Preoperative Information (Enter/Edit)](#preoperative-information-enteredit)
  - [Print a Surgery Risk Assessment](#print-a-surgery-risk-assessment)
- [Data Transmissions](#data-transmissions)
- [CICSP Enhancements](#cicsp-enhancements)
- [Field Updates](#field-updates-1)
- [Option Updates](#option-updates-1)
- [Data Transmissions](#data-transmissions-1)
This project enhances the Surgery Risk Assessment module of the Veterans Health Information Systems and Technology Architecture (VistA) Surgery application. The purpose of the Surgery Risk Assessment module is to facilitate data entry of both preoperative and postoperative patient information pertaining to surgical risk assessments, and to transmit the data to a national database. Although all surgical risk data are transmitted to the national database, the cardiac and non-cardiac programs have separate executive boards, and cardiac surgical cases are assessed and tracked separately from non-cardiac surgical cases.
Clinical nurse reviewers enter both preoperative and postoperative patient data into the electronic data collection instrument in the VistA Surgery Risk Assessment module for both programs. Various reports and screen displays give the local medical center staff a mechanism for tracking and evaluating surgical risk and operative mortality at the local level, while transmission to the national database allows for the statistical analysis of trends and quality improvement on a national scale.
These enhancements provide users with the current data forms and definitions used to collect data for the National Surgery Quality Improvement Program (NSQIP) and Continuous Improvement In Cardiac Surgery Program (CICSP).
The software provides the following enhancements:
- Addition of new data fields
- Changes to existing data fields
- Changes to data entry screens
- Changes to reports used in the Surgery Risk Assessment management process
- Changes to the Surgery Risk Assessment transmissions
*(This page included for two-sided copying.)*

# NSQIP Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NSQIP Enhancements include data dictionary updates, option modifications, and data transmission updates.

# Field Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following field in the SURGERY file (#130) is added for NSQIP.

- A new field titled Date Surgery Consult Requested has been added. It represents the date that a request for consult was sent to Surgery Service.

The following field in the SURGERY file (#130) is modified:

- The ANESTHESIA TECHNIQUE field is updated to include a new selection (REGIONAL).

The following fields in the SURGERY file (#130) have been modified to include changes in the field definition or help text.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name and Number</strong></th>
<th><strong>Description of Change</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CLOSTRIDIUM DIFFICILE COLITIS</td>
<td>Description field update for NSQIP</td>
</tr>
<tr class="even">
<td>SURGERY CONSULT DATE</td>
<td><p>Description field update for NSQIP</p>
<p>Field title updated to remove reference to CT</p></td>
</tr>
</tbody>
</table>

The following data changes have been made to the PERIOPERATIVE OCCURRENCE CATEGORY file (#136.5).

| Occurrence Category                      | Description of Change          |
|----------------------------------------------|------------------------------------|
| CLOSTRIDIUM DIFFICILE COLITIS (C. DIFFICILE) | Description field update for NSQIP |

# Option Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options/reports have been modified.

## List of Surgery Risk Assessments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This *List of Surgery Risk Assessments* option has been updated. Existing reports have been revised and new reports have been added.

#### List of Transmitted Assessments

> When printing the List of Transmitted Assessments the system prompts the user as to whether to sort and/or view Assessed Cases, Non-Assessed Cases, or Both.

> When printing the List of Transmitted Assessments, after the Date Range prompts, a new prompt has been added to ask the user as to whether to sort by Date of Operation or Date of Transmission.

#### List of Eligible Cases

> When printing the List of Eligible Cases, the system prompts the user as to whether to sort and/or view Assessed Cases, Non-Assessed Cases, or Both.

#### Create List of Cases without CPT Code

> The List of Cases without CPT Codes has been added to the reports contained in the *List of Surgery Risk Assessments* option.

> The List of Cases without CPT Codes has been added as \#10 on the list of reports that can be selected.

> The list shall include all cases that have not been coded with CPT codes.

#### Create Summary List of Assessed Cases

> The Summary List of Assessed Cases has been added to the reports contained in the *List of Surgery Risk Assessments* option.

> The Summary List of Assessed Cases has been added as \#11 on the list of reports that can be selected.

> The report prompts the user for date range, all or selected surgical specialties, and division.

> The report provides a total count of closed and transmitted cases sorted by specialty.

## M&M Verification Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to assist the nurse reviewer, an enhancement has been made to the *M&M VerificationReport* contained within the *Surgery Risk Assessment Menu*. The following data elements have been added to the *M&M VerificationReport*:

- Case Number
- CPT Code
- Time of Death
- Review of Death Comments.

## Risk Model Lab Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to assist the nurse reviewer, a new option has been created in the *Surgery Risk AssessmentMenu* called *Risk Model Lab Test (Enter/Edit)* which will allow the nurse to map NSQIP-CICSP data in the Risk Model Lab Test (#139.2) file. The option synonym is ERM.

## Anesthesia Technique (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When REGIONAL is entered as the Anesthesia Technique, the template logic mimics the existing OTHER or LOCAL prompts.

#### ## Anesthesia AMIS

The *Anesthesia AMIS* option has been removed from the *Anesthesia* menu.

## Preoperative Information (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following items shall be removed from the *Preoperative Information (Enter/Edit)* option screens:

> On page 1 of the option, Pack Years and Pre-Illness Function Status are removed.

> On page 2 of the option, Paraplegia and Quadriplegia are removed.

#### The following fields will be modified on the *Preoperative Information (Enter/Edit)* option screens:

> The Height field displayed on the GENERAL section has been modified. The most recent Height value also displays the date the measurement was obtained.

## Print a Surgery Risk Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A modification shall be made to the printing function. If the users responds YES to the initial prompt of “Do you want to batch print assessments for a specific date range?”, the system will prompt user for an individual subspecialty or all cases. The system will then sort and display/print list based upon user response.

# Data Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data transmissions to the national database also include the new data elements for NSQIP.

The following new fields have been added to the data transmissions:

- Date Surgery Consult Requested
- Surgery Consult Date

The following fields have been removed from the data transmissions:

- Quadriplegia/Tetraplegia/Quadriparesis (Y/N)
- Paraplegia/Paraparesis (Y/N)
- Functional Health Status Prior to Current Illness
- Pack/Year Cigarette History

# CICSP Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CICSP enhancements include data dictionary updates, option modifications, and data transmission updates.

# Field Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following fields in the SURGERY file (#130) have been modified:

#### - The system no longer accepts an entry of NS for “No Study” when entering the Patient’s Height.

#### - System no longer accepts an entry of NS for “No Study” when entering the Patient’s Weight.

- The “Date Patient Extubated” description has been updated to the following:

> Indicate the date that the endotracheal tube is pulled for the first time after surgery. If a tracheostomy is performed to replace an oral intubation tube, intubation is considered continuous so the patient has not been extubated as long as the patient continues to require ventilator support. If the patient dies while intubated, indicate the date of death for this data element. Indicate “extubated prior to leaving the OR” in the Resource Comment if patient is extubated prior to leaving the OR.

> RI - The patient remains intubated and on ventilator at 30 days after surgery.

- A new field, Primary Cause for Delay for Cardiac Surgery, has been added to document the cause of delay if the delay is greater than 30 days.

> The definition for the Primary Cause for Delay for Cardiac Surgery is the following:

> This field contains the primary cause for delay. If a Cardiac patient's surgery is greater than 30 days from initial VA Cardiothoracic Surgery Consultation (as calculated between the CT CONSULT DATE to DATE OF SURGERY), user shall enter cause as defined in the field. If date is less than or equal to 30 days, system shall automatically default entry to None.

>          - Resource Limitation: Due to staffing or other facility limitation,

>            e.g., OR scheduling, physician availability, ICU bed capacity

>          - Patient Health: Due to patient health issue, e.g., vascular consult,

>            additional tests

>          - Patient Preference: Due to a non-health related patient preference,

>            e.g., vacation

>          - Other

>          - NS/Unknown: Unable to Locate Reason for Delay. Entering "NS" for "No

>            Study/Unknown" is also allowed.

- None
- The “Repeat Ventilator Support within 30 days” description has been updated to the following in the SURGERY file (#130) and in the PERIOPERATIVE OCCURRENCE CATEGORY file (#136.5):

> Indicates if the patient was placed on ventilator support postoperatively within 30 days and this repeat ventilator support is related to the index operation (For example, the patient is on the ventilator intra-op and immediately post-op.  Then the patient is weaned and the ventilator is discontinued.  Later, the patient gets into trouble and mechanical ventilation has to be reinstated.) However, if the patient returns to the OR within 30 days and gets extubated immediately after, it is not considered repeat ventilator support.

# Option Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options have been modified as described.

- An enhancement to the *Operative Risk Summary Data (Enter/Edit)* option allows users to enter a value of NS (No Study) into the Physician’s Preoperative Estimate of Operative Mortality. Upon entry of NS, the system automatically populates the Date/Time of Estimate of Operative Mortality with a value of NS.
- Under the current *Update Assessment Status to 'COMPLETE'* option, the system lists items missing from the assessment based upon the order in the field number in SURGERY (#130) file. An enhancement to this option changes the list of missing items to display in the same order as the standard assessment screens.
- Under the *Cardiac Procedures Operative Data(Enter/Edit)* option, the system initially prompts the user to “Select Operative Information to Edit.” A new entry of “N” allows the user to “Set All to No” for the 22 Cardiac Procedures. A verification prompt follows to ensure that the user understands the entry.
- The *Resource Data* option has been updated. When the user edits the Date/Time Discharged from ICU, the system provides the user a select option to allow the user to pull date/time from the existing list of possible entries or manually enter a date/time.
- The *Laboratory Test Results (Enter/Edit)* option is updated to flag lab results out of range.

# Data Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data transmissions to the CICSP database now include Cause for Delay for Surgery.