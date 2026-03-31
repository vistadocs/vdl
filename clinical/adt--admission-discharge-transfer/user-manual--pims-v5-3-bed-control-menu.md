---
title: PIMS Version 5.3 User Manual - Bed Control Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Bed Control Menu
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: active
pkg_ns: ADT
patch_ver: 5.3
patch_id: ADT*5.3
group_key: "ADT:ADT:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - patient
  - table
  - contents
  - acute
  - crisis
  - admission
  - discharge
  - suicidal
  - transfer
  - notification
page_count: 0
word_count: 7796
section_count: 17
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/dg_reg_bc_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/dg_reg_bc_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

---
title: |
  ADT Module/Bed Control Menu

  PIMS Version 5.3

  User Manual
---

![](pims-version-5-3-user-manual-bed-control-menu/001.png)

Original Software Release: August 1997

Revised: November 2025

Office of Information and Technology (OI&T)

Revision History

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 42%" />
<col style="width: 20%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description (Patch # if applicable)</strong></th>
<th><strong>Project Manager</strong></th>
<th><strong>Technical Writer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/2025</td>
<td>DG*5.3*1117 documentation updates to Section 2.1.10 Admitted for Acute Suicidal Crisis prompt, added subsections 2.1.10.1 Edit Acute Suicidal Crisis Admission, added subsection 2.1.10.1.1 Edit Acute Suicidal Crisis Admission Prior to Discharge, added subsection 2.1.10.1.2 Edit Acute Suicidal Crisis Admission After Discharge, added subsection 2.1.10.2 Delete Acute Suicidal Crisis Admission. Updated section 2.14.8 and added subsections 2.14.8.1 Edit Acute Suicidal Crisis Transfer, added subsection 2.14.8.1.1 Edit Acute Suicidal Crisis Transfer Before Discharge, added subsection 2.14.8.1.2 Edit Acute Suicidal Crisis Transfer After Discharge; added subsection 2.14.8.2 Delete Acute Suicidal Crisis Transfer</td>
<td>Booz Allen Hamilton</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>10/2024</td>
<td><p>DG*5.3*1104 documentation updates to Section 2.1.10 Admitted for Acute Suicidal Crisis prompt (new), 2.6.7 and 2.6.8 Discharge COMPACT Act special scenarios (new) and</p>
<p>Section 2.14.8 Treatment for Acute Suicidal Crisis prompt (new)</p></td>
<td>Booz Allen Hamilton</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>12/2016</td>
<td><p>DG*5.3*926 documentation updates to Section “2.6.1 “Death” or “Death with Autopsy” Discharge Types:”</p>
<ul>
<li><blockquote>
<p>Added the SUPPORTING DOCUMENT TYPE field and defined the contents when populated (“VAMC EHR INPATIENT DEATH”).</p>
</blockquote></li>
</ul>
<p>NOTE: The Revision History for this manual was started as of Patch DG*5.3*926.</p></td>
<td>Master Veteran Index Project Team</td>
<td>Master Veteran Index Project Team</td>
</tr>
<tr class="even">
<td>8/1997</td>
<td>Initial document.</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
- [Bed Control Menu](#bed-control-menu)
  - [Admit a Patient](#admit-a-patient)
    - [Admission Type and Ward Location must Coincide](#admission-type-and-ward-location-must-coincide)
    - [Notification of Admission Sent to Health Information Management Section](#notification-of-admission-sent-to-health-information-management-section)
    - [Third Party Review Form for Veterans with Private Medical Insurance](#third-party-review-form-for-veterans-with-private-medical-insurance)
    - [Print Patient Wristband](#print-patient-wristband)
    - [Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group](#notification-of-vacant-bed-sent-to-dg-bldg-management-mail-group)
    - [Notification of Patient's Insurance Coverage Sent to Hospital Personnel](#notification-of-patients-insurance-coverage-sent-to-hospital-personnel)
    - [Notification of Verified Eligibility for Scheduled Admissions or Waiting List Entries](#notification-of-verified-eligibility-for-scheduled-admissions-or-waiting-list-entries)
    - [ADMISSION OE/RR NOTIFICATION may be Displayed with V. 2.2 (or Higher) of Order Entry/Results Reporting](#admission-oerr-notification-may-be-displayed-with-v-22-or-higher-of-order-entryresults-reporting)
    - [Notification of Discharge Sent to Patient’s Primary Care Team](#notification-of-discharge-sent-to-patients-primary-care-team)
    - [Admitted for Acute Suicidal Crisis prompt](#admitted-for-acute-suicidal-crisis-prompt)
  - [Cancel a Scheduled Admission](#cancel-a-scheduled-admission)
  - [Check-in Lodger](#check-in-lodger)
    - [Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group](#notification-of-vacant-bed-sent-to-dg-bldg-management-mail-group-1)
  - [Delete Waiting List Entry](#delete-waiting-list-entry)
    - [Multidivisional Facilities Set Up with Separate Waiting Lists](#multidivisional-facilities-set-up-with-separate-waiting-lists)
  - [Detailed Inpatient Inquiry](#detailed-inpatient-inquiry)
  - [Discharge a Patient](#discharge-a-patient)
    - [“Death” or “Death with Autopsy” Discharge Types](#death-or-death-with-autopsy-discharge-types)
    - [Absent Sick in Hospital (ASIH) Included in Discharge Types](#absent-sick-in-hospital-asih-included-in-discharge-types)
    - [Notification of Discharge Deleted Sent to Health Information Management Section](#notification-of-discharge-deleted-sent-to-health-information-management-section)
    - [Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group](#notification-of-vacant-bed-sent-to-dg-bldg-management-mail-group-2)
    - [DECEASED OE/RR NOTIFICATION may be Displayed for Death Discharges with V. 2.2 (or Higher) of Order Entry/Results Reporting](#deceased-oerr-notification-may-be-displayed-for-death-discharges-with-v-22-or-higher-of-order-entryresults-reporting)
    - [Notification of Discharge Sent to Patient’s Primary Care Team](#notification-of-discharge-sent-to-patients-primary-care-team-1)
    - [Discharge Acute Suicidal Crisis Care](#discharge-acute-suicidal-crisis-care)
  - [DRG Calculation](#drg-calculation)
  - [Extended Bed Control](#extended-bed-control)
    - [Assign Patient to Primary Care Team](#assign-patient-to-primary-care-team)
    - [Print Patient Wristband](#print-patient-wristband-1)
    - [Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group](#notification-of-vacant-bed-sent-to-dg-bldg-management-mail-group-3)
  - [Lodger Check-out](#lodger-check-out)
    - [Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group](#notification-of-vacant-bed-sent-to-dg-bldg-management-mail-group-4)
  - [Provider Change](#provider-change)
  - [Schedule an Admission](#schedule-an-admission)
    - [Third Party Review Form for Veterans with Private Medical Insurance](#third-party-review-form-for-veterans-with-private-medical-insurance-1)
  - [Seriously Ill List Entry](#seriously-ill-list-entry)
  - [Switch Bed](#switch-bed)
    - [Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group](#notification-of-vacant-bed-sent-to-dg-bldg-management-mail-group-5)
  - [Transfer a Patient](#transfer-a-patient)
    - [Transfer Types and Actions are Defined in Edit Bed Control Movement Types option of ADT System Definition Menu](#transfer-types-and-actions-are-defined-in-edit-bed-control-movement-types-option-of-adt-system-definition-menu)
    - [Update Admission Record and Removing Patient from Seriously Ill List](#update-admission-record-and-removing-patient-from-seriously-ill-list)
    - [Patient Authorized/Unauthorized Absence](#patient-authorizedunauthorized-absence)
    - [Interward Transfers Not Allowed in System](#interward-transfers-not-allowed-in-system)
    - [Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group](#notification-of-vacant-bed-sent-to-dg-bldg-management-mail-group-6)
    - [Print Patient Wristband](#print-patient-wristband-2)
    - [Notification of Patient Transfer sent to Primary Care Team](#notification-of-patient-transfer-sent-to-primary-care-team)
    - [Acute Suicidal Crisis Transfer](#acute-suicidal-crisis-transfer)
  - [Treating Specialty Transfer](#treating-specialty-transfer)
  - [Waiting List Entry/Edit](#waiting-list-entryedit)
    - [Remove Patient from Waiting List](#remove-patient-from-waiting-list)
    - [Multidivisional Facilities Set Up with Separate Waiting Lists](#multidivisional-facilities-set-up-with-separate-waiting-lists-1)
    - [Consistency Checker Corrects Inconsistencies](#consistency-checker-corrects-inconsistencies)
The Bed Control menu contains the options which record and track inpatient movements. It also provides for entry of patients onto the Seriously Ill and Waiting Lists. Admissions, transfers, and discharges are entered/edited through options on the Bed Control menu. These movements are tracked by the system for use by other functions such as PTF. They are also reflected on your site's Daily Gains and Losses Sheet and Bed Status Report as well as a number of other reports produced by the system. The following is a list of options contained in this menu and a brief description of their major function.

# Bed Control Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an overview and description for each option located on the PIMS V. 5.3 ADT Module Bed Control Menu. More detail is provided for each option on the following pages.

- Admit a Patient

This option is used to admit a patient to the medical center or edit/delete a previously entered admission.

- Cancel a Scheduled Admission

This option is used to cancel previously scheduled admissions which are not automatically cancelled by the system.

- Check-in Lodger

This option is used to check-in a lodger to your facility or another facility.

- Delete Waiting List Entry

This option is used to remove a patient from the admission waiting list.

- Detailed Inpatient Inquiry

This option is used to view patient movement information pertaining to a specific admission for an individual patient.

- Discharge a Patient

This option is used to record the discharge of a patient from inpatient care.

- DRG Calculation

This option can be used to compute the appropriate Diagnostic Related Group based on diagnoses and procedures.

- Extended Bed Control

This option is used to edit inpatient movements related to a patient's current or past period of care.

- Lodger Check-out

This option is used to check-out a lodger from your facility or another facility.

- Provider Change

This option is used to enter changes in provider during an inpatient stay for a selected patient.

- Schedule an Admission

This option is used to schedule a patient for a future admission to a ward or treating specialty.

- Seriously Ill List Entry

This option is used to place patients onto or remove them from the medical center's Seriously Ill List.

- Switch Bed

This option is used to record a patient's transfer from one room-bed to another on the same ward.

- Transfer a Patient

This option is used to enter a patient's interward transfers, absence movements, and corresponding returns.

- Treating Specialty Transfer

This option is used to record the change of a patient's treating specialty when the patient does not physically move to a different location.

- Waiting List Entry/Edit

This option is used to place patients on the waiting list for admission to the facility and to edit waiting list entries.

## Admit a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Admit a Patient option is used to admit a patient to the medical center or edit/delete a previously entered admission. Prior inactive admission records can also be selected for editing or deleting as long as the PTF record has not been closed.

New patients may be added to the system through this option. You will need to enter the basic information required to add a new patient. In an emergency situation, you may choose not to enter the entire patient record (10-10 data) at that time. You should then go in at a later time under the Register a Patient option in Registration to complete the entire record.

### Admission Type and Ward Location must Coincide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several types of data may now be displayed (Means Test, primary care, appointment, etc.). The system will next prompt for the admission data. The admission type and ward location must coincide. For example, if the READMISSION TO NHCU/DOM admission type is selected, the patient must be placed on a NHCU or DOM ward. If TO ASIH is selected, only non-NHCU and non-DOM wards will be selectable.

### Notification of Admission Sent to Health Information Management Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the PRINT PTF MESSAGE parameter is set to YES, messages will be transmitted to the Health Information Management Section (HIMS) through this option. When there is a new admission, patient data and admitting diagnosis will be sent to the HIMS printer. If the diagnosis is changed during an editing session, a message will be sent with the new diagnostic information.

### Third Party Review Form for Veterans with Private Medical Insurance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Third Party Review Sheet may be printed through this option if the patient is a veteran and has private medical insurance. The veteran's insurance information is displayed if the coverage has not expired. Information concerning pre-admission certification, second surgical opinion, length of stay review, and bill status is found on this form.

### Print Patient Wristband

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient wristbands may also be printed through this option. Such requests must be sent to a bar code printer.

### Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you make a change to the room/bed, you will be asked if you would like to notify Building Management of the vacated bed. A YES response at this prompt will generate a MailMan bulletin to all members assigned to the DG BLDG MANAGEMENT mail group. If no members have been assigned to this mail group, no message will be sent.

### Notification of Patient's Insurance Coverage Sent to Hospital Personnel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Utilizing this option may cause a MailMan bulletin to be sent to appropriate hospital personnel alerting them of the patient's insurance coverage. The bulletin, UR ADMISSION BULLETIN, will only be sent if members have been assigned to the DGPM UR ADMISSION mail group and the selected patient has at least one active insurance policy on the date of admission.

### Notification of Verified Eligibility for Scheduled Admissions or Waiting List Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FUTURE ACTIVITY SCHEDULED bulletin is sent when veterans with verified eligibility and either scheduled admissions or waiting list entries are admitted. It contains a list of all scheduled admissions and waiting list entries on file for the patient and is sent to the mail group users designated in the UNVERIFIED ADMIT GROUP field of the MAS PARAMETERS file. If the patient is a non-veteran, this information will be included in the NON-VETERAN ADMISSION bulletin. If the patient's eligibility is not verified, this information will be included in the VETERAN ADMISSION WITHOUT VERIFIED ELIGIBILITY bulletin.

### ADMISSION OE/RR NOTIFICATION may be Displayed with V. 2.2 (or Higher) of Order Entry/Results Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An ADMISSION OE/RR NOTIFICATION may be displayed with V. 2.2 or higher of Order Entry/Results Reporting. The notification will only be displayed for patients who are defined in an OE/RR LIST entry and will only be displayed to users defined in that list entry.

*REF: Please refer to the Order Entry/Results Reporting documentation for more information concerning OE/RR notifications, if needed.*

### Notification of Discharge Sent to Patient’s Primary Care Team

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Primary Care Management Module (PCMM) is loaded, a MailMan message will be sent to the patient’s primary care team members who chose to receive inpatient notifications when the patient is admitted.

If the patient has dual eligibility, you will be asked for the eligibility associated with the admission.

If the selected admitting regulation has subcategories, you will be asked to select the appropriate subcategory.

### Admitted for Acute Suicidal Crisis prompt 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new required prompt has been integrated into the Admissions workflow to record this inpatient stay as an Acute Suicidal Crisis. This prompt serves to indicate the inpatient care is related to Comprehensive Prevention, Access to Care, and Treatment (COMPACT) Act Acute Suicidal Crisis Episodes of Care (EOC). It begins or closes the COMPACT Act Acute Suicidal Crisis benefit; therefore, it is essential to refer to the supporting documentation.

If the appropriate documentation from the attending provider or their designee states this inpatient stay is related to an Acute Suicidal Crisis, follow these steps:

1)  At the Admitting Regulation prompt, type COMPACT Act.
2)  At the “Admitted for Acute Suicidal Crisis?” type “Yes” to begin a COMPACT Act Episode of Care.
1.  *The* “Admitted for Acute Suicidal Crisis?// Yes” is defaulted to Yes when the patient has an open Episode of Care in EOC file \#818. The “Admitted for Acute Suicidal Crisis?// No” *is defaulted to No, when the patient does not have an open Episode of Care in EOC file \#818.*
3)  At the confirmation prompt, “This Admission will begin the COMPACT Act benefit. Are you sure?” type “Yes” to confirm. This value will not only start a new Episode of Care and begin the 30-day inpatient benefit period but will also mark the inpatient stay as related to Acute Suicidal Crisis. This value is shared with VistA Integrated Billing so that the first-party co-pay for this inpatient stay will be cancelled.

When “Yes” is entered, this value is displayed on both the Patient Treatment File (PTF) 101 screen and on the first 501 screen. This value is stored in the PTF file (#45) and a pointer to this value is stored in the COMPACT ACT EPISODE OF CARE file (#818). This value is shared with VistA Integrated Billing so that the first-party co-pay for this inpatient stay will be cancelled.

When “Are you sure” prompt is answered No, you will be prompted again to answer “Admitted for Acute Suicidal Crisis?”

4)  At the “Acute Suicidal Crisis Start Date?: NOW//, select NOW or enter the Start Date of the Acute Suicidal Crisis; if documentation states the Start of the acute suicidal crisis is earlier than NOW, for example, if the Acute Suicidal Crisis began at a Community Emergency Department and now the patient is being admitted for an inpatient stay, the Start Date of the Acute Suicidal Crisis should be the date when the care began in the Community.
2.  When a patient is admitted for acute suicidal crisis upon discharge the outpatient episode and benefit period automatically opens.

#### Edit an Acute Suicidal Crisis Admission 

If notification or documentation is received that an error is found and the record should not be marked as Acute Suicidal Crisis, then correct the admission if the PTF is open. If the PTF record is closed, the movements for that admission should be corrected by reopening the PTF and correcting the movements for that admission. Inpatient care provided does not quality for the benefits under the COMPACT Act; therefore, first-party copayments will apply for this type of care unless the patient is eligible for another benefit under a different authority

#### Edit Acute Suicidal Crisis Admission Before Discharge 

When there is one movement in EOC File (#818), AND an edit to acute suicidal crisis prompt occurs prior to discharge, then the inpatient episode of care is closed with final status “Entered in Error” and the movement is removed from EOC File (#818). To edit the “Admitted for Acute Suicidal Crisis? Yes//” prompt from Yes to No, follow the steps below.

1.  Navigate to the admission record
2.  At the Admitted for Acute Suicidal Crisis? Yes// prompt, answer No. The “No” value is displayed on the PTF 101 and 501 screens; in addition, the 501 screen will not display COMPACT Act data (such as start date, remaining days, or benefit end date). When answered No (prior to patient discharge), the movement is removed from EOC File (#818). EOC File data may be viewed using option: COMPACT ACT DISPLAY EOC DATA.
3.  At “This action will end the benefit. Are you sure?” answer Yes (if answered No, the “Admitted for Acute Suicidal Crisis” prompt will redisplay). When answered “Yes”, this value ends inpatient COMPACT Act benefit; benefit end is captured in the EOC File (benefit end date is the date in which the change is made and may be different than admission date). The EOC File captures and displays Episode Final Status of ‘Entered in Error’ and the movement is removed from the EOC File. EOC File data may be viewed using option: COMPACT ACT DISPLAY EOC Data.
3.  The “Are you sure?” prompt is not displayed when the patient has multiple movements in the EOC File (#818) and the earliest movement is open. The “Are you sure” prompt only displays when the edit action is ending the COMPACT Act Inpatient benefit period.

#### Edit Acute Suicidal Crisis Admission After Discharge

4.  When “Admitted for Acute Suidical Crisis?” is Yes, then upon discharge, the Outpatient Episode and benefit period is automatically open. Edits to movements after discharge will not impact the Open Outpatient Episode or benefit period.

When editing an Acute Suicidal Crisis admission after discharge (changing Acute Suicidal Crisis prompt from Yes to No), the ‘Are you sure’ prompt is not displayed, since the Inpatient benefit period ended upon discharge. To edit the “Admitted for Acute Suicidal Crisis” prompt from Yes to No, after patient is discharged, follow the steps below:

1.  Navigate to the patient’s admission record
4.  At the Admitted for Acute Suicidal Crisis? Yes// prompt, answer No.

    When answered “No”, the EOC File (#818) removes the movement, but does not capture Final Episode Status “Entered in Error”, because there is an Open Outpatient Episode and benefit period. The “No” value is displayed on the PTF 101 and 501 screens. EOC File data may be viewed using option: COMPACT ACT DISPLAY EOC DATA.

#### Delete Acute Suicidal Crisis Admission

If notification or documentation is received that an error is found and the patient’s

admission record requires deletion, then follow the steps below to delete the admission

record:

1.  Navigate to menu option: Extended Bed Control and patient movement record
2.  Choose Admit a Patient
3.  When the patient’s admission record is displayed, type “@” and press enter
4.  At the ‘are you sure” prompt, answer “Yes” and press enter

    Note: Deleting Acute Suicidal Crisis admission ends inpatient episode and benefit period and removes all associated movements from the EOC File (#818) and PTF File \#45.

    When deleting COMPACT Act admission prior to discharge, then Episode Final Status is displayed “Entered in Error”, COMPACT Act Inpatient benefits end on the date of deletion.

    When deleting COMPACT Act admission after discharge, then Episode Final Status is null (Outpatient Episode and benefit period is open).

## Cancel a Scheduled Admission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows you to cancel scheduled admissions. All questions must be answered before a scheduled admission can be cancelled.

## Check-in Lodger

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Check-in Lodger option is used to check a lodger into your facility. It may also be used to check in a patient lodged at an area hotel/motel at VA expense or housed at another VA. Lodging at another VA would most likely occur in a metropolitan area where there are several VA facilities in close proximity to one another.

You may enter a new lodger episode or edit the check in date, check in type, transfer facility, ward location, room-bed, reason for lodging, and lodging comments for an existing episode.

*NOTE: The transfer facility must be in the INSTITUTION file before it can be selected through this option. This may be done through the Institution File Enter/Edit option in the ADT Supervisor Menu by holders of the DG INSTITUTION security key.*

### Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the DG BLDG MANAGEMENT mail group has been populated, making a change to the room-bed while utilizing this option may cause a MailMan bulletin to be generated to Building Management Service informing them a bed has been vacated and will require cleaning.

## Delete Waiting List Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delete Waiting List Entry option is used to remove a patient from the admission waiting list.

### Multidivisional Facilities Set Up with Separate Waiting Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At multidivisional facilities, each division will be set up with a separate waiting list.

## Detailed Inpatient Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Detailed Inpatient Inquiry option is used to view all information for a specific patient concerning an individual admission.

Once the patient name is entered, all admissions for that patient are displayed in groups of 5 for selection. When the admission is selected, all admission, transfer, treating specialty transfer, and discharge information for that admission is displayed.

## Discharge a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Discharge a Patient option is used to record the discharge of a patient from inpatient care. Patient discharges can be edited and deleted through this option. You may also assign a patient to primary care and to a primary care team during the discharge process.

When a patient who has an active admission is selected, Means Test, primary care, and patient status data will be displayed. The system will next prompt for a discharge date and discharge type. If there is no active admission for the patient, you will be prompted with the most recent discharge date and type for editing. Only the most recent inactive discharge may be selected for editing or deleting.

### “Death” or “Death with Autopsy” Discharge Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To discharge an inpatient that has died, use discharge type “Death” or “Death with Autopsy.” The software automatically populates the SOURCE OF NOTIFICATION FOR THE DATE OF DEATH, SUPPORTING DOCUMENT TYPE, and the DATE OF DEATH fields. It populates the SOURCE OF NOTIFICATION FOR THE DATE OF DEATH field with “Inpatient at VAMC,” and then records the date of last entry or update on the DATE OF DEATH field, and populates the SUPPORTING DOCUMENT TYPE field with “VAMC EHR INPATIENT DEATH,” and then records information about the submitter (user) making the entry or change.

### Absent Sick in Hospital (ASIH) Included in Discharge Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a patient is Absent Sick in Hospital (ASIH) for less than 30 days, FROM ASIH and CONTINUED ASIH (other facility) will be included in the available discharge types for selection.

### Notification of Discharge Deleted Sent to Health Information Management Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the PRINT PTF MESSAGE parameter in the MAS Parameter Entry/Edit option (ADT System Definition Menu) is set to YES, messages will be transmitted to HIMS (Health Information Management Section) automatically when a discharge is deleted.

### Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan bulletin will be generated upon discharge to notify Building Management of the vacated bed. This bulletin is sent to all members assigned to the DG BLDG MANAGEMENT mail group. If no members have been assigned to this mail group, no message will be sent.

### DECEASED OE/RR NOTIFICATION may be Displayed for Death Discharges with V. 2.2 (or Higher) of Order Entry/Results Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A DECEASED OE/RR NOTIFICATION may be displayed for death discharges with V. 2.2 or higher of Order Entry/Results Reporting. The notification will only be displayed for patients who are defined in an OE/RR LIST entry and will only be displayed to users defined in that list entry.

*REF: Please refer to the Order Entry/Results Reporting documentation for more information concerning OE/RR notifications, if needed.*

### Notification of Discharge Sent to Patient’s Primary Care Team

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a patient is discharged, a MailMan message will be sent to the patient’s primary care team members who chose to receive inpatient notifications.

### Discharge Acute Suicidal Crisis Care 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a patient who is in a COMPACT Act Acute Suicidal Crisis Episode of Care, and the EOC started as inpatient (receiving 30 days of inpatient care benefit), then upon discharge, the system automatically updates the episode and EOC File (#818) to Outpatient and opens the 90-day Outpatient benefit period.

When the patient’s EOC started as outpatient, and then the patient is admitted, upon patient discharge the EOC File (#818) automatically updates the benefit from Inpatient to Outpatient and displays the Outpatient episode start and benefit period. EOC data may be viewed by users who hold the PX EOC Edit security key, in option: COMPACT ACT DISPLAY EOC DATA.

#### Delete Acute Suicidal Crisis Discharge

If notification or documentation is received that an error is found and the patient’s discharge record requires deletion, then follow the steps below to delete the discharge:

1.  Navigate to menu option: Extended Bed Control and patient movement record
2.  Choose Discharge Patient
3.  When the patient’s discharge record is displayed, type “@” and press enter
4.  At the ‘are you sure” prompt, answer “Yes” and press enter
5.  When deleting a discharge, the EOC File (#818), closes the Outpatient benefit period and opens the earliest Inpatient benefit period. EOC data may be viewed by those who have PX EOC Edit security key, using option: COMPACT ACT DISPLAY EOC DATA.

## DRG Calculation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DRG Calculation option is used to compute and display the Diagnosis Related Group (DRG) for a patient based on that patient's diagnoses and any operations/procedures performed. If you enter an INACTIVE diagnosis code, a message will be displayed and the prompt will be repeated.

You will be prompted for the DXLS. Answer with the ICD Code Number of the diagnosis responsible for the major portion of the patient stay. Multiple secondary diagnoses and operations/procedures may also be entered.

The following is a list of those items that are computed and displayed for the DRG:

- Avg len of stay - The VA national length of stay for the DRG.
- Weight - The weighted work unit (WWU) value assigned to the DRG.
- Low day(s) - The VA low trim point day for the assigned DRG.
- High days - The VA high trim point day for the assigned DRG.
- Local Breakeven - The day on which actual cost of care equals the estimated allocation for the assigned DRG for the individual medical center.
- Local low day(s) - The low trim point day established by the individual medical center for the assigned DRG.
- Local High days - The high trim point day established by the individual medical center for the assigned DRG.

The data may be calculated for VA or non-VA patients. The system does not store the DRG compiled for each patient. It is recalculated each time this option is utilized.

## Extended Bed Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Extended Bed Control option is used to edit inpatient transactions for a specific admission episode. You may edit admissions, or enter/edit transfers and discharges. Only those admissions where the PTF record has not been closed may be edited.

Depending on your selection, you may be prompted for admission record data fields, data fields pertaining to a patient transfer, or those pertaining to a patient discharge.

*REF: Please refer to the appropriate option documentation for assistance in answering these prompts, where necessary. Those options are Admit a Patient, Transfer a Patient, and Discharge a Patient.*

The PTF record is automatically updated when changes are made through this option.

### Assign Patient to Primary Care Team

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may assign a patient to a primary care team through this option via the discharge functionality.

### Print Patient Wristband

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may print a patient wristband through this option. Such requests must be sent to a bar code printer.

### Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you edit the room/bed through the admit or transfer patient functions, you will be asked if you would like to notify Building Management of the vacated bed. A YES response at this prompt will generate a MailMan bulletin to all members assigned to the DG BLDG MANAGEMENT mail group. This bulletin is automatically generated when a new transfer or discharge is entered. If no members have been assigned to this mail group, the prompt to send the bulletin will not appear.

## Lodger Check-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lodger Check-out option is used to check a lodger out of your facility, to check out patients lodged at an area hotel/motel at VA expense, or housed at another VA. You may also edit the checkout date and disposition of an existing lodger episode.

### Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan bulletin may be generated to Building Management Service when this option is utilized if the DG BLDG MANAGEMENT mail group has been populated and a bed was entered when the selected lodger was checked in.

## Provider Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Provider Change option is used to enter changes in provider (primary or attending physician) during an inpatient stay for a selected patient. You may also edit existing provider changes through this option. By entering provider changes, a historical record is created of all providers associated with the patient during the hospital stay.

This option should be used if the treating specialty remains the same but a change in provider occurs. A patient movement record will be created for each provider change.

## Schedule an Admission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Schedule an Admission option is used to schedule a patient for a future admission to the medical center or edit an existing scheduled admission. Patients may be scheduled to a specific ward or treating specialty.

### Third Party Review Form for Veterans with Private Medical Insurance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may choose to print the Third Party Review form through this option. This form is used in connection with veterans who have private medical insurance. The insurance data will not be displayed on the form if the insurance has expired.

## Seriously Ill List Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Seriously Ill List Entry option is used to place patients on or remove patients from the medical center's Seriously Ill List.

*REF: A list of patients who are currently on the Seriously Ill List can be obtained using the Seriously Ill Inpatient Listing option under the Inpatient Report Menu, ADT Outputs Menu.*

## Switch Bed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Switch Bed option is used to record a change in a patient's bed assignment within the same ward.

### Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you make a change to the room/bed, you will be asked if you would like to notify Building Management of the vacated bed. A YES response at this prompt will generate a MailMan bulletin to all members assigned to the DG BLDG MANAGEMENT mail group. If no members have been assigned to this mail group, you will not be prompted to send the bulletin.

## Transfer a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transfer a Patient option is used to enter and edit patient transfers for PTF records which have not been closed.

Action in this function varies depending upon what transfer types have been defined as active at your facility, the transfer type involved in the transfer, and whether you are editing an old or adding a new transfer date for the patient.

### Transfer Types and Actions are Defined in Edit Bed Control Movement Types option of ADT System Definition Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each transfer type and its corresponding action are defined through the Edit Bed Control Movement Types option of the ADT System Definition Menu. For example, for certain transfer types, you may be prompted through the process of entering/editing the Treating Specialty. This occurs if the ASK TREATING SPECIALTY field of the Edit Bed Control Movement Types option has been answered YES for the particular transfer type you are working with. The actions in this option will vary depending upon your site's definition of each bed control movement type.

### Update Admission Record and Removing Patient from Seriously Ill List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A patient's admission record may be updated in this option if you are transferring the patient to ASIH from NHCU/DOM. *REF: Please review the 2.1 Admit a Patient option in this document for more information.* You may also place a patient on or remove a patient from the Seriously Ill List. This will only occur if the ward the patient is being transferred to is designated as a Seriously Ill ward through the Ward Definition Entry/Edit option of the ADT System Definition Menu or if the patient is currently Seriously Ill.

### Patient Authorized/Unauthorized Absence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a patient is released on AUTH ABSENCE 96 HOURS OR LESS (pass) and does not return, the transfer type of this transfer should be changed to AUTHORIZED ABSENCE. A transfer of FROM AUTHORIZED TO UNAUTHORIZED ABSENCE can then be entered. A second alternative would be to return the patient from pass (FROM AUTH. ABSENCE OF 96 HOURS OR LESS) and then place him/her out on UNAUTHORIZED ABSENCE when appropriate.

### Interward Transfers Not Allowed in System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system will not allow an interward transfer to a ward or a different designation than the ward the patient is currently assigned to. For example, if the patient is assigned to a hospital ward, the system will not allow an interward transfer to a NH ward.

### Notification of Vacant Bed sent to DG BLDG MANAGEMENT Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When editing the ROOM-BED field of an existing transfer, the bed availability display shows all available beds for selection. If you make a change to the room/bed, you will be asked if you would like to notify Building Management of the vacated bed. A YES response at this prompt will generate a MailMan bulletin to all members assigned to the DG BLDG MANAGEMENT mail group. If you enter a NEW movement which frees a bed, the bulletin will be generated automatically. If no members have been assigned to this mail group, no message will be sent.

### Print Patient Wristband

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may print a patient wristband through this option. The patient wristband is generated with bar-coded social security number and will contain patient name, primary long ID (usually SSN), date of birth, patient religion, an allergy flag, and may contain ward location. Requests to print patient wristbands must be sent to a bar code printer.

### Notification of Patient Transfer sent to Primary Care Team

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When using the transfer functionality, a MailMan message may be sent to the patient’s primary care team members who chose to receive inpatient notifications.

### Acute Suicidal Crisis Transfer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new required prompt has been integrated into the Admissions workflow to record this inpatient stay as an Acute Suicidal Crisis. This prompt serves to indicate the inpatient care for this movement is related to COMPACT Act Acute Suicidal Crisis Episodes of Care (EOC). This prompt can begin a new EOC if one does not already exist; therefore, it is essential to refer to the supporting documentation.

If the appropriate documentation from the attending provider or their designee states that this inpatient movement is related to an Acute Suicidal Crisis, follow this direction and notes.

1)  At the prompt, “Was treatment for Acute Suicidal Crisis? No//, type “Yes” to begin a COMPACT Act Episode of Care. “Was treatment for Acute Suicidal Crisis?” prompt is defaulted to “Yes” when there is an open episode in EOC File (#818). When defaulted to “Yes” the “Are you sure?” prompt (shown in step 2) is not displayed.
2)  This value may not only start a new Episode of Care and begin the 30-day inpatient benefit period, but also marks whether the care for this movement is related to the Acute Suicidal Crisis or not. This value is displayed on the PTF 101 and the 501 screens and stored in the PTF file (45) and the 501 sub-file (#45.02). This value is shared with VistA Integrated Billing so that the first-party co-pay for this inpatient stay will be cancelled.
3)  NOTE – when prompt, “This action will end the episode of care. Are you sure?”, is answered “No”, then the prompt “Was treatment for Acute Suicidal Crisis? Yes// will display again.

#### Edit Acute Suicidal Crisis Transfer

IMPORTANT– Editing the value entered at the Treated for Acute Suicidal Crisis? prompt may impact the Inpatient episode of care and 30-day benefit period. If the appropriate documentation from the attending provider or their designee states the transfer is not related to an Acute Suicidal Crisis, then correct the transfer if the PTF is open. If the PTF record is closed, the movements for that admission should be corrected by reopening the PTF and correcting the movements for that admission. Editing the “Treated for Acute Suicidal Crisis?” prompt from Yes to No means Inpatient care furnished is not eligible for the COMPACT Act benefit; therefore, first party copays will be charged for this care unless the patient is eligible for another benefit under some other authority.

#### Edit Acute Suicidal Crisis Transfer Before Discharge 

When there is one movement in EOC File (#818), and an edit to “Treated for Acute Suicidal Crisis?” prompt occurs prior to discharge, then the Inpatient Episode of Care is closed with final status “Entered in Error” and the movement is removed from EOC File (#818). To edit the “Treated for Acute Suicidal Crisis? Yes//” prompt from Yes to No, follow the steps below.

1.  Navigate to the patient’s transfer record
5.  At the Treated for Acute Suicidal Crisis? Yes// prompt, answer No. The No value for this movement is shared and displayed on the PTF 101 and 501 screens; (if the patient has an open Acute Suicidal Crisis movement, the start date and remaining days will display on the 501 screen)
6.  At “This action will end the benefit. Are you sure?” answer Yes (if answered No, the “Treated for Acute Suicidal Crisis” prompt will redisplay). When answered “Yes”, this value ends inpatient COMPACT Act benefit; benefit end is captured in the EOC File (inpatient benefit end date is the date in which the change is made). The EOC File captures and displays Episode Final Status of ‘Entered in Error’ and the movement is removed from the EOC File. EOC File data may be viewed using option: COMPACT ACT DISPLAY EOC DATA.
6.  The “Are you sure?” prompt is not displayed when the patient has multiple movements in the EOC File (#818) and the earliest movement is open. The “Are you sure” prompt only displays when the edit action is ending the COMPACT Act Inpatient benefit period.

#### Edit Acute Suicidal Crisis Transfer After Discharge

7.  When “Treated for Acute Suicidal Crisis?” is Yes, then upon discharge, the Outpatient Episode and benefit period is automatically open. Edits to movements after discharge will not impact the Open Outpatient Episode or benefit period. Episode Final Status of ‘Entered in Error’ is not captured due to Open Outpatient Episode. The ‘Are you sure?” prompt is not displayed due to Open Outpatient Epsidoe.

To edit the “Treated for Acute Suicidal Crisis” prompt from Yes to No, after patient is discharged, follow the steps below:

1.  Navigate to the patient’s transfer record
7.  At the “Treated for Acute Suicidal Crisis? Yes//” prompt, answer No.

    When answered “No”, the movement is removed from the EOC File (#818) and shares this value with the PTF 101 and 501 screens; if the patient has at least one Acute Suicidal Crisis movement after discharge, the PTF 501 screen will display the Outpatient COMPACT Start Date and Remaining Days. If all movements ‘Treated for Acute Suidcial Crisis?” are changed to No after discharge, then Outpatient COMPACT Start Date and Remaining Days is not displayed on the PTF 501 screen.

#### Delete Acute Suicidal Crisis Transfer

If notification or documentation is received that an error is found and the patient’s transfer record requires deletion, then follow the steps below to delete a transfer record:

1.  Navigate to menu option: Extended Bed Control and patient movement record
2.  Choose Transfer a Patient
3.  When the patient’s transfer record is displayed, type “@” and press enter
4.  At the ‘are you sure” prompt, answer “Yes” and press enter

    Note: Deleting a transfer will remove the movement from the EOC File (#818) and the PTF File (#45 and subfile \#45.02). If the patient has more than one movement in the EOC File (#818), then deleting the Acute Suicidal Crisis transfer may not end inpatient episode and benefit period – the system will keep the earliest movement open before discharge. If all movements are deleted prior to discharge, the EOC File will remove all movements and display Episode Final Status “Entered in Error”; the Inpatient Episode End Date reflects the date of deletion.

    Upon discharge, the Inpatient benefit period ends as of discharge date, and the Outpatient benefit period automatically opens. Deleting Acute Suicidal Crisis movements after discharge will not impact the Open Outpatient episode and benefit period. COMPACT Act Inpatient benefits end on the date of deletion. When deleting COMPACT Act tranfer after discharge, then Episode Final Status is null (Outpatient Episode and benefit period is open)

## Treating Specialty Transfer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Treating Specialty Transfer option is used to change the assigned treating specialty responsible for the patient's care when the patient is not making a physical location transfer.

After the patient is selected, Means Test data and information related to the patient’s last in-house stay may be displayed. At the prompt, select “More” if you wish to display pending appointments and clinic enrollments.

A patient may be assigned to only one treating specialty at a time. Every treating specialty is associated with a PTF bed section. The system automatically matches the patient's assigned treating specialty with the appropriate bed section. More than one treating specialty may be associated with the same PTF bed section.

## Waiting List Entry/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Waiting List Entry/Edit option is used to place a patient on the waiting list for admission to the medical center or nursing home care unit or to edit the data for a patient already on the list.

### Remove Patient from Waiting List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Delete Waiting List Entry option must be used to remove a patient from the waiting list. A list of patients who are currently on the waiting list may be obtained through the Waiting List Output option.

### Multidivisional Facilities Set Up with Separate Waiting Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At multidivisional facilities, each division is set up with a separate waiting list. New waiting list divisions may be added. Waiting list divisions must be chosen from those divisions already established at your medical center and defined in the MEDICAL CENTER DIVISION file.

### Consistency Checker Corrects Inconsistencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the execution of this option, the Consistency Checker is run to determine if any inconsistent data is present. If there are any inconsistencies, a message will appear listing the fields not specified and you will be prompted to correct these inconsistencies before continuing.