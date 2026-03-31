---
consolidated_title: "blind rehab release notes"
app_code: ANRV
doc_type: release-note
master_source: "Blind Rehab Version 5.1 Release Notes"
master_pub_date: September 1999
consolidated_from: 11 versions
prior_versions:
  - "Blind Rehab Version 5.1.10 Release Notes"
  - "Blind Rehab Version 5.1.12 Release Notes"
  - "Blind Rehab Version 5.1.13 Release Notes"
  - "Blind Rehab Version 5.1.15 Release Notes"
  - "Blind Rehab Version 5.1.16 Release Notes"
  - "Blind Rehab Version 5.1.17 Release Notes"
  - "Blind Rehab Version 5.1.18 Release Notes"
  - "Blind Rehab Version 5.1.3 Release Notes"
  - "Blind Rehab Version 5.1.9 Release Notes"
  - "Blind Rehab Version 5 Release Notes"
---

**Blind Rehabilitation (ANRV)**

## Release Notes

<!-- image -->


September 1999 (Version 5.0 VA Release)

August 2022


Office of Information and Technology (OIT)

Revision History

| Date   |   Version | Description      | Author              |
|--------|-----------|------------------|---------------------|
| 8/2022 |       5.1 | Initial baseline | Booz Allen Hamilton |

Table of Contents

Introduction	1

Purpose	1

Audience	1

This Release	1

New Features and Functions Added	1

New Tab – Print VIST Roster Sorts Menu	2

BR Patient Submenu Update	2

Enhancements and Modifications to Existing	3

Create Referral	3

Referral Roster	3

Modify Referral (Search) Submenu Update	3

Removed Items	4

Administration Menu	4

Enter/Edit Menu	5

Print Individual Records Menu	6

Print Reports Menu	6

Known Issues	6

Product Documentation	7

### Introduction

The Blind and Visual Impairment Continuum of Care application provides enhanced tracking, and reporting, of the blind rehabilitation services provided to veterans.  Features include Electronic referral process to track patient applications for service, notifications feature to alert users of pending referrals, encounters/progress notes will be automatically created, nationwide centralization of BRVS services data to allow nationwide reporting, ad-hoc reporting capabilities, allows the ability to track BRVS patient care access across institutions, and patients can be referred or transferred to other institutions if they move without having to recreate patient data. The VistA namespace is ANRV.

This patch includes many changes and enhancements to Blind Rehabilitation.

### Purpose

These release notes cover the changes to Blind Rehabilitation for this release.

### Audience

This document targets users and administrators of Blind Rehabilitation and applies to the changes made between this release and any previous release for this software.

### This Release

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issue for Blind Rehabilitation 5.1.

#### New Features and Functions Added

The following are the new features and functions added to the BR 5.1 release.

- Two Factor authentication (2FA) – logon using Personal Identification Verification (PIV) pin.
- A pagination feature was added for search results. The user can select from a dropdown of 5,10,15 or 20 rows displayed per page. The application defaults to 10 rows per a page. Arrows are enabled for moving to the next, previous, or the next set of page results. The previous BR version 5.0 displayed search results in its entirety on a single page.
- The BRS VA TRM/VA Security Standards will be updated. The deployment will be replaced with a VA Enterprise Cloud (VAEC) implementation, using cloud service provider Amazon Web Services (AWS).
- Addition of a **SAVE** button on each page AND the ability to stay on the page that was saved.
- 508 Compliant changes
    - Ensure that no page element is coded as a table
    - Fixed missing labels and markings of mandatory fields *
    - Exportable report tables do not have &lt;th&gt; header cells
    - Removed verbiage "Select menu item on the left"
    - Error alert message is sent to the screen for BR Patient
    - VIST Annual Review Edit Review buttons have unique labels

#### New Tab – Print VIST Roster Sorts Menu

Previously, the **Print VIST Roster Sorts** Menu was a submenu under the **Print Reports** Menu. Now it is a main tab.

The Patient Type drop down box was removed from each report criteria since the low vision patient option was removed throughout the application.

#### BR Patient Submenu Update

BR 5.1 consolidates ALL Mandatory fields onto a preliminary screen that comes up first after selecting the patient. This is highly critical when ADDING a new case to 5.1 as the act of adding the patient is done on one page and then saved before automatically entering the rest of BR Patient option.

The following are Basic Information mandatory field(s):

- Ocular Health
- Patient History
- Living Arrangements
- Blind Rehabilitation Experience

The completion of this page will register the patient after you click **Save and Continue** . The page(s) following will allow you to skip to different patient information by clicking on any of the boxes as in the sample display below.

Figure 1: BR Patient Page Display

<!-- image -->

If data is entered and user clicks on **Previous** , **Save** or **Next** button, the data will be saved. Clicking on the **Done** button however will not save the data and user will be returned to the home page.

Edit **BR patient** under **Financial /Benefits**

- SMC Rating box removed
- Paragraph level box removed
- Annual household income was changed to Monthly Household income

#### Enhancements and Modifications to Existing

The following are the enhancements and modifications to the BR 5.1 release.

- Reports were updated from Crystal to Jasper.
- The **Help – Application** under each submenu was moved to a main menu tab.
- The **Logout** button was moved to the upper right corner next to the user’s login name displayed.
- After a report is displayed, the submenu on the left side remains available on version 5.1 You will not have to click on the main tab at the top of the page after a report is displayed to get back to the list of submenus.

#### Create Referral

Fee Basis was changed to VA funded but this field is slated to be removed.

#### Referral Roster

For all the Referral reports - The ALL option is the default selection whereas previously “All” had to be selected.

#### Modify Referral (Search) Submenu Update

“All” is the default selection for Referred to Institutions, Initiating Areas, Statuses, &amp; Referral Types.

#### Removed Items

The following have been removed for the BR 5.1 release.

- The **Waitlist Reporting Menu** and **Skip to Main Content** tabs were removed.
- Entries &amp; Reports related to the following categories: Low Vision Patient, VARO Claims, and Education &amp; In Service Activities were removed.

#### Administration Menu

The following were removed from Administration tab submenu:

- TIU Document Definitions
- MPI Patient Registration
- Patient ICN Lookup
- Patients not registered with MPI
- Visual Acuity Discrepancy

Table 1: Administration Screen Updates

| BR 5.0 Administration   | BR 5.1 Administration   |
|-------------------------|-------------------------|
| <!-- image -->          | <!-- image -->          |

#### ##### 4.3.3 

#### Enter/Edit Menu

The following submenu items were removed:

- Low Vision Patient
- Education Service Activities
- VARO Claims
- Annual Outcome Survey
- Pre/Post Blind Rehab Survey
- Modify Converted National Waitlist Record
- VIST Visits
- BRC Clinical Assessments
- Create Treatment Plan
- Modify Treatment Plan
- Enter Non-Treatment Plan Training
- Enter Treatment Plan or Training

Table 2: Enter/Edit Screen Updates

| BR 5.0 Enter/enter   | BR 5.1 Enter/Edit   |
|----------------------|---------------------|
| <!-- image -->       | <!-- image -->      |

#### ##### 4.3.6 

#### Print Individual Records Menu

The following submenus were removed:

- Treatment Plan
- Training History
- Annual Outcome Survey
- Pre/Post Blind Rehab survey

Records can now be exported in different formats (csv, PDF, Word). Previously the records displayed did not have an export option available but had a “Use printer friendly page” option which has since been removed from 5.1 version.

#### Print Reports Menu

The following submenus were removed:

- Low Vision Patients Report
- VARO Claim List
- Education &amp; In Service Activities
- VIST Visits Date List
- BRC Pre-Admission By Priority Level
- BRC Workload Monthly Summary
- BRC Workload Monthly Summary By VISN
- BRC Workload Semi-Annual Summary
- BRC Workload Monthly Summary By VISN
- BROS Workload Summary
- BROS Workload Summary By VISN

#### Known Issues

Certain patient demographics will not populate until the overnight patient demographics update process runs

1.	Refresh speed in BR Patient Search. Varies from 12 – 30 seconds on average (to bring up the Mandatory Fields). Takes an additional amount of time (usually equal to the 1st delay) to bring up the Basic Information (screen #1).

2.	Deceased Patient Notification Delete option. Is inconsistent with deletion, sometimes takes 3 tries or more.

3.	Fixing the referrals totals in the VIST Roster Summary Report. This section of the report is currently not working in 5.1.

4.	Fixing the PSD Update for key demographic fields on newly added veterans to 5.1. Currently, address/phone, period of service, race, gender is not updating until the next PSD Update is run (which is now set to nightly). In BR-5.0, this information is updated upon saving the new addition record in 5.0.

5.	Fixing the Print VIST Roster Summary Report issues previously identified (i.e., ICD-10 eye codes, reporting referrals, etc.).

6.	Tweaking the Print Labels feature to better center the printed information near the middle of the Avery Label in each column AND include the 10th row of labels.

*********************************NOTE*****************************

Fixing the PSD Update for newly added Sensitive Record Veterans to 5.1. Currently, Social Security Number (SSN) is not updating until the next PSD Update is run (which is now set to nightly). In BR 5.0, this information is updated upon saving the new addition record in 5.0.

********************************************************************

### Product Documentation

The following documents apply to this release:

- User Manual
- Technical Manual
- Deployment, Installation, Back-out and Rollback Guide

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Blind Rehab Version 5.1.3 Release Notes

### General Updates

The System Administrator role has undergone an update which allows them to update a user’s **DUZ** code. The **Patient Search** functionality can now be utilized by entering the first initial of a patient’s last name as well as the last four digits of their social security number. When a column sort for **Referrals Found** is used, and the **Edit** button is selected, users will now see that patients will match against the data in their respective row. Users will also see that patient records for **Additional Medical Treatment Information** are displayed correctly. **Patient mailing labels** will now print correctly on Avery 3x10 label sheets. The **VIST Annual Review** date on an exported VIST Roster list will be displayed in the correct format. In addition to the forementioned updates, the following new referral types have been added to the application.

- BROS Poly Vision Therapy – 1st Experience
- BROS Poly Vision Therapy – Additional Training
- Vision Therapy – 1st Experience
- Vision Therapy – Additional Training

Changes have also been made for the JAWS screen reader. These improvements include updates towards conveying alert messages and page load completion and the addition of the **Alt+K** hotkey for the **OK** button.

#### Administration Page

System Administrators can now update a user’s **DUZ** code as depicted in Figure 1.

<!-- image -->

Figure 1: BR Staff DUZ Code Field

#### BR Patient Enter/Edit

The **Patient Search** field now has a bolder outline, allowing users to locate the field with more ease.

<!-- image -->

Figure 2: Local VistA Site Search

After searching and selecting a patient, the selected patient appears in the **Patient Already Selected** dialog. To view the selected patient, click **OK** . A JAWS user can now utilize the **Alt+K** hotkey to select the **OK** button.

<!-- image -->

Figure 3: Patient Already Selected Dialog

When the user clicks the **Save and Continue** button and required fields are left blank, JAWS will read an alert message for every required field left blank as depicted in Figure 13.

<!-- image -->

Figure 4: Basic Information with Error Messages

#### Create Referrals

New referral types are depicted in Figure 5.

<!-- image -->

Figure 5: Enter New Referral for this Patient

#### Modify Referral (Search)

The **Modify Referral (Search)** reflects the new referral types added as depicted in Figure 6. The referral types will be alphabetized in a future patch.

<!-- image -->

Figure 6: Referral Types

After the list of referrals found is displayed in a table, it is presented in descending order by **Created Date** . When clicking on the column headers to sort, the **Edit** button now correctly reflects the data for the row you wish to edit as depicted in Figure 7.

<!-- image -->

Figure 7: Referrals Found Table

#### Referral Status Save is Read by JAWS

Changes made to a referral status for the **Modify Referral (Search)** and **Modify Referral By Patient** functionalities will produce a message stating that the referral status was saved. This message is now read by JAWS.

<!-- image -->

Figure 8: Change Referral Status

#### JAWS Supported Versions

REDACTED. Figure 9 depicts the supported JAWS versions in a table format.

<!-- image -->

Figure 9: Supported JAWS Versions

#### JAWS 2020 Users Workarounds

When registering a new patient, JAWS will read error messages when pressing the **Enter** key on the **Save and Continue** button. JAWS will not read error messages when utilizing the **Alt + S** hotkey.

<!-- image -->

Figure 10: Save and Continue Button for Registering New Patient

Once a new patient has been registered, the **Edit Blind Patient** section will display boxes numbered 1-10 as depicted in Figure 11. JAWS will read these boxes as **Tabs** .

<!-- image -->

Figure 11: Edit Blind Patient Tabs

Users that have JAWS 2020 or later versions can use the **Tab** key to navigate through the 10 **Edit Blind Patient** tabs. The **Space** bar can be used to select an **Edit Blind Patient** tab.

Users that have JAWS 2021 or later versions can utilize the appropriate keystrokes to bring up the JAWS links list. JAWS will read the **Edit Blind Patient** tabs from the links list.

<!-- image -->

Figure 12: Edit Blind Patient Tabs Link List

#### VIST Annual Review

When required fields are left blank, JAWS will read an alert message for every required field left blank as depicted in Figure 13.

<!-- image -->

Figure 13: Error Messages for Blank Required Fields

A **Patient Search** can now be performed with the first initial of the patient’s last name and the last four digits of their social security number as depicted in Figure 14.

<!-- image -->

Figure 14: BR Patient Search

#### Benefits &amp; Services Checklist

The alert message for a successful save for the **Benefits and Services Checklist** functionality is now announced by JAWS.

<!-- image -->

Figure 15:Enter Benefits and Services Checklist

#### Letters and Labels

1. To create a current list, go to **Print Patient Mailing Labels** and select your desired institution. Click **Submit** .
<!-- image -->

Figure 16: Patient Mailing Labels – Select Patient Criteria

1. Click the corresponding **Remove** button for the labels you do not want as depicted in Figure 17. Once complete, click **Continue** .
<!-- image -->

Figure 17: Mailing Label Table

1. Go back to **Print Patient Mailing Labels** . The option to use the list you edited will be available in the **Select Patients Method** list as depicted in Figure 18.
<!-- image -->

Figure 18: Patient Mailing Labels – Current List

**NOTE:** The list you created will not exist after you Logout.

The exported PDF file now prints a sheet of 3x10 labels.

#### Print Individual Records

The display for patient records was updated to remove the **Last Medical Exam** date.

REDACTED

Figure 19: Individual Patient Record

#### Print Reports

Exported reports now have the correct date format of MM/DD/YYYY as depicted in Figure 20.

<!-- image -->

Figure 20: Report Data Download

#### Workaround for Referrals Summary Report

1. Navigate to **Enter/Edit** then **Modify Referral (Search).**
2. From the **Select Institution search type** list, select **Referrals From your Institution.**
3. Select **All** from the **Referred To Institutions** list.
4. Select the desired various referral types.
5. Select the desired date range.

The example below shows the referrals to all institutions from 01/01/2022 to 12/30/2022 for BRC referral types, referred from Baltimore VAMC institutions, that were Admitted.

<!-- image -->

Figure 21: Modify Referrals

The search yielded 6 referrals of BRC type from Baltimore VMAC that were Admitted for 2022.

<!-- image -->

Figure 22: Referrals Found

### From: Blind Rehab Version 5.1.9 Release Notes

## JAWS Supported Versions

The supported JAWS versions can be found at the following link: [Job Access With Speech (JAWS) (va.gov)](https://gcc02.safelinks.protection.outlook.com/?url=https%3A%2F%2Ftrm.oit.va.gov%2FToolPage.aspx%3Ftid%3D42&data=05%7C01%7C%7Cc0b03b3a1bb84568d34108daf8b0f59b%7Ce95f1b23abaf45ee821db7ab251ab3bf%7C0%7C0%7C638095736153024832%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=9kiFzzj%2FYZIN4T01FLUUkqhvpFqxRt5b6vTi5p03OFg%3D&reserved=0) 9 depicts the supported JAWS versions in a table format.

Figure 10 - Supported JAWS Versions

<!-- image -->

### From: Blind Rehab Version 5.1.13 Release Notes

## Enhancements and Modifications to Existing

The following are the enhancements and modifications to the Blind Rehabilitation 5.1.13 release.

- Enhancements for users who require the use of JAWS(Job Access With Speech)
- Patient Search allows patient names that include an apostrophe
- Edit Blind Patient text boxes expand as additional text is entered
- Update field label for “Gender” to “Sex”
- Update to the VIST Summary report Referral Applications section

### Enhancements for users requiring use of JAWS

Several enhancements were made to help navigating the Blind Rehabilitation application when using JAWS.

1. The regions on the page are now properly marked so that JAWS users can use keys SHIFT + R to navigate the regions on each page.
2. After adding patient search criteria and clicking the “Search” button, focus will now move to the patient search results table rather than focus remaining at the Search button.
3. Previously, JAWS was counting the tab subtask heading as an item in the list when landing on it. For instance, when a user would land on the Enter/Edit subtask, JAWS would say there were 9 in the list when there were only 8 subtasks. The application has now been corrected to only give the number of subtasks in the list.
4. On the Enter/Edit BR Patient, Edit Blind patient page, there are tabs 1-10 that can be navigated to by using the TAB key. Previously, JAWS would announce the name of the tab and link making it a bit confusing to the user that there may have been 2 items when actually there is only 1 link.

### Patient Search accommodates names that contain an apostrophe

Previously, the **Patient Search** or **BR Patient Search** feature would not recognize a name that contained an apostrophe in VistA. Patient Search will pull in names from VistA if you search with the apostrophe in the search criteria box. However, the patient search results table may or may not display the name with the apostrophe. In this case, the search criteria used for BR Patient Search must be what is shown on their patient record.

Figure 1 - Blind Patient Search results

<!-- image -->

If the patient's last name displayed an apostrophe in their patient record during enrollment, it must be included in the search criteria for BR Patient Search. Otherwise, it will not find the patient name.

Figure 2 - BR Patient Search result when ‘ is not included

<!-- image -->

Figure 3 - BR Patient Search result with ' in last name

<!-- image -->

### Edit Blind Patient text boxes expand as additional lines of text are entered

The text boxes for patient history expands as additional lines of text are entered. Previously it was a fixed size and visually limited the lines of text in the display unless you put your cursor in the text box and used your mouse or arrow keys to view additional text.

Figure 4 - Text Area expands with data entered

<!-- image -->

Figure 5 - Patient Work History

<!-- image -->

### Field label update for “Gender” to “Sex”

The field label for “Gender” has been updated to “Sex”. This is present in the Current Patient Selected box and on the Patient’s Record.

Figure 6 - Current Patient box

<!-- image -->

### VIST Roster Summary report – Referral Applications summary

The VIST Roster Summary report has been updated for the Referral Applications summary section. Previously, it would show the summary of the BRC &amp; non-BRC referrals that were made from the institution. The change was made to reflect all the VA type referrals that are made to your institution and are completed by the VA. However, the non-VA type referrals statistics are still for those referrals made from a VA institution. The Completions for Non-VA type referrals will be zero unless the VA source choses to complete the non-VA referral. Otherwise, the VA cannot directly receive the referral status from the other agency.

Figure 7 - VIST Referrals Application non-BRC

<!-- image -->

### Known Issues

Patient last names that display in VistA with an apostrophe, may or may not display the ‘ character in the name in the patient search results. The user must be aware to include or not include the ‘ in the last name when executing a BR Patient Search.

### From: Blind Rehab Version 5.1.10 Release Notes

## Sensitive Patient

The **Enter New Blind Patient** has been corrected to show if a patient has a restricted record and will be marked with (Sensitive).

Figure 1 – Full Social Security Number (Sensitive) displayed

<!-- image -->

A Search Result for a patient already on the roster will be identified as *SENSITIVE* before they are selected for use. This applies when a user does a BR Patient Search under ENTER/EDIT or PRINT INDIVIDUAL RECORDS.

Figure 2 – Patient Already Selected box

<!-- image -->

## BR Patient/Patient Record

The Enter New Blind Patient – Patient Record can be viewed prior to the commencement of the enrollment process. Clicking on the active Name link will display their record which includes Address, Phone Number, Date of Birth, Period of Service, and Priority Level. After a patient is found from Patient Search and selected, a user can click the patient’s name link to display their record.

Figure 3 – Patient Name link opens Patient Record

<!-- image -->

Figure 4 - Patient Record displays Service Connection and Rated Disabilities

<!-- image -->

After a patient’s Basic Information is entered (Save and Continue is executed), the Edit Blind Patient page displays Service Connection and Rated Disabilities (if applicable).

Figure 5 - Patient Eligibility and Rated Disabilities are displayed

<!-- image -->

A patient may or may not have any Rated Disabilities or Eligibility listed. If there is nothing listed for them in VistA, you will see the words “No Data” under Basic Information Details.

Figure 6 – Rated Disabilities for a patient with no data

<!-- image -->

After a patient has been added to the roster, the Print Individual Records, Patient Record will also display the patient’s information. This includes Address, Phone Number, Period of Service, Service Connection, Priority Group, and Rated disabilities if the patient had this information in their VistA.

If a patient is already on the roster and has an address or phone number update in VistA, the patient record in Blind Rehabilitation should reflect the updates within minutes.

Figure 7 – Print Individual Record – Patient Record

<!-- image -->

If a patient is from a different institution from the user, the patient’s record will not display their Service Connected Percentage or their Rated Disabilities.

## Print VIST Roster Sorts Reports

If a patient has an address or phone number update in VistA, the Print VIST Roster reports by Address/Phone will update for that patient after PSD Updater has run which occurs daily(usually runs overnight). Therefore, these reports may not reflect updated patient demographics until the next day. A patient address update could also impact these Print VIST Roster Sorts Reports depending on what was changed.

- By Address
- By State
- By County
- By City
- By Zip Code

If an update is needed to these reports immediately, the user should go to Enter/Edit -&gt; BR Patient and execute Save and Continue. This will force a save of their updated information to the BR database.

## Letters and Labels

The Print Letters may not have the updated patient address if it was changed during the current day. PSD Updater needs to be run or the user must execute Save and Continue in Enter/Edit -&gt; BR Patient.

Similarly, the Print Patient Mailing Labels may not have the Veteran’s updated address if it was changed the during the current day. To force an update, execute Save and Continue in Enter/Edit -&gt; BR Patient or run PSD Updater.

## Modify Referral

For BRC type referrals, the Admission date will be limited to be set to the current date or before. The user is prohibited from choosing a date in the future or a date before the Scheduled date. The user can update the Scheduled date to the current date if needed and then set the Admission date to the current date.

The Discharged date will be prohibited to being set to a date in the future or a date prior to the Admit date.

### From: Blind Rehab Version 5.1.18 Release Notes

## Enhancements and Modifications to Existing Application

The following are the enhancements and modifications to the Blind Rehabilitation BR 5.1.14 release.

- Enhancements to the User Notifications on the Welcome page
- Enhancements to the Edit Blind Patient Page
- Referrals Information no longer displays previous Admit/Discharged date
- Include deceased patients who was removed from VIST Roster Sorts reports
- VIST Annual Review - Type and Location choices were modified for Complete Status
- Corrections to the sorting function on the Create Referrals search results

### Enhancements to the User Notifications

The Deceased Patient Notifications were not removed on the first attempt to delete and has been corrected. In addition, the name of the patient has been added to the Deceased Patient Notification link. These notifications will appear for users that were tracking the deceased patient. In addition, if the user had created any referrals for the deceased patient, the patient name and referral number will appear in the Referral Cancellation notification link. This should help increase efficiency as users will not have to open each link to view the patient name and/or referral information to evaluate if the notification is applicable to them.

Any Deceased patient notifications that were created before BR 5.1\_14, will not be updated with the patient name. However, any of the links should be removed upon the first attempt to delete the notification.

Figure 1 – Deceased Patient Notifications without patient name

<!-- image -->

Figure 2 – Deceased Patient Notifications with patient name and referral #

<!-- image -->

### Enhancements to Edit Blind Patient page

Some enhancements were made to the Edit Blind Patient tabs for the following:

- 2 Ocular Health – 
			the field “Use of Eye Prosthesis” is marked as mandatory
- 3 Patient History – 
		the field “Sight Loss Caused Job Loss?” is marked as mandatory
- 9 Rehabilitation Experience – 
		Vision Therapy types were added to the “Type of Training” drop down list

Figure 3 – “Use of Eye Prothesis” field under Ocular Health

<!-- image -->

Figure 4 - Vision Therapy types added to Type of Training

<!-- image -->

### Referrals Information no longer displays previous Admit/Discharged

The following fields were removed from the Referral Information screen since they were not being used.

- Previous Admit Date
- Previous Discharge Date
- Previous Program Type

Figure 5 - Referral Information

<!-- image -->

### VIST Annual Review modifications

When a VIST Annual Review is entered with a Status = COMPLETE, the user can no longer choose “Not Applicable” for Type or Location. For Status = “Could Not Contact”, “No Show”, or “Declined,” Type and Location default to “Not Applicable.”

Figure 6 - VIST Annual Reviews

<!-- image -->

### Existing Referrals table

The Create Referral Search results table sort by Created Date previously was not sorting chronologically. If you click the sort icon, it will sort by created date in ascending order. If you click it again, it will display it in descending order.

Figure 7 - Sort on Existing Referrals

<!-- image -->

### “Include Deceased patients?” was removed from VIST Roster Sorts

The checkbox to “Include Deceased Patients?” has been removed from all the VIST Roster Sorts report pages. Enabling the checkbox did not include any deceased patients on the reports since deceased patients are removed from the VIST roster when the date of death is entered in VistA.

Figure 8 - "Include Deceased Patients?" on VIST Roster Sorts

<!-- image -->

### Known Issues

The updates made in this release will most likely need users to do a hard refresh. Some browsers store files in their cache therefore; you may not experience the updates with this software until your cache is cleared. Complete these 2 steps to enable the fixes included in the release.

1. To refresh CSS, execute: CTRL+F5
2. To clear your cache, execute the following keystrokes:
    - 2.1. CTRL+ SHIFT + DELETE – Settings window will open
    - 2.2. TAB to the “Cached images” and ensure the box is checked
    - 2.3. TAB to the “Clear Now” button and press ENTER
    - 2.4. CTRL + W to close the Settings window

### From: Blind Rehab Version 5.1.16 Release Notes

### Enhancements for low vision users

The text for User Notifications on the Home page has been enhanced so that the color contrast is stronger when a user hovers on the link. Previously, the text color upon hover did not meet the 508 color contrast criteria.

Figure 1 – User Notifications

<!-- image -->

### Enhancements for users who require a screen reader

The Application Help contained links that were not understood by users relying on a screen reader for navigation. An icon link for social media sites in the main window for Help was previously reciting incoherent text. This link has been removed since it is not used.

The Page Help link in the main region of each page previously lacked keyboard accessibility for navigation when using a screen reader. Since users do not typically use the page help link, it has been removed from every page. The Application Help tab contains the same Help information and remains available to all users.

Figure 2 – Example of page with Help icon

<!-- image -->

Figure 3 - Application Help page displaying social media icon

<!-- image -->

### Pop up modals require confirmation

Previously, pop-up modals would allow users to TAB outside the window and return to the application without closing the pop up. Unsighted users would be unaware that the pop-up modal was still open. The application has been updated so that users cannot continue to use the application without first acknowledging and closing the pop-up window.

These pop-up windows can occur in the following scenarios:

- User attempts to enter/edit data for a patient that is not registered
- User attempts to enter/edit data for a deceased patient
- Warning timeout window opens when a user leaves their session idle

If a user TABs outside the pop-up modal, they will be navigated around the browser window but will not be allowed back to the Blind Rehabilitation application until the pop-up window has been closed.

Figure 4 – Error Encountered for unregistered patient

<!-- image -->

Figure 5 - Error Encountered for deceased patient

<!-- image -->

### VIST Roster Summary update for BRC type referrals

The VIST Roster Summary Report for the VIST Referral Applications (BRC) statistics has been modified. The Submitted column is for all the BRC type referrals that have been referred from your institution. The Admitted and Discharged columns are based on all the BRC type referrals that have been referred to your institution which is unchanged from the previous release.

The section for VIST Referral Applications for non-BRC referrals was not changed.

Figure 6 - VIST Roster Summary Report

<!-- image -->

### Known Issues

If you leave your log in session idle for several minutes and then click submit button for a report, you may see an error message flash on the screen. The error message disappears and the report displays to the screen without error.

Figure 7 - Example Error Message

<!-- image -->

### From: Blind Rehab Version 5.1.12 Release Notes

## Patient with only a last name

The **Enter New Blind Patient** will now accommodate a patient that has no first or middle name.

Figure 1 - Patient with last name only

<!-- image -->

Patient with a last name only is successfully enrolled and placed on the roster.

Figure 2 - Patient with last name only on the roster

<!-- image -->

## Edit Blind Patient Headings

The Edit Blind Patient Page now has headings making it easier for JAWS users to navigate the page. When JAWS is running, the SHIFT +H keys will allow the user to move from heading to heading.

Figure 3 – Edit Blind Patient list of headings

<!-- image -->

## Deceased patient pop-up message

When a deceased patient is selected on the Create Referral page, a popup message appears asking the user to choose whether they want to continue. Jaws will read the message and is keyboard accessible to select whether they wish to continue with selecting the deceased patient.

Figure 4 – Confirmation pop-up

<!-- image -->

After selecting the deceased patient in the patient already selected box, there is another pop-up message indicating that you may not create referrals for a deceased patient.

Figure 5 - Referral cannot be created for deceased patient

<!-- image -->

## Referral Admit/Discharge calendar icon format issue

The calendar for Admit and Discharge Date were mis formatted. A user may have to execute the key stroke CTRL +F5 the first time to make your browser recache Cascading Style Sheet (CSS).

The calendar was misaligned in the previous release. It has been corrected on GUI version 5.1.8.

Figure 6 - Admit/Discharge Date calendar format issue

<!-- image -->

### From: Blind Rehab Version 5 Release Notes

## Table of Contents

## Introduction	1

Documentation Retrieval	1

VistA Intranet	1

What’s New in Blind Rehab v5.0.29	2

*General User experience changes	2*

*Administrative Users/System Changes	2*

Appendix	3

Introduction

**NOTE** **:** These Release Notes are for Blind Rehabilitation Version 5.0.29.4. For the initial release and other releases of Blind Rehabilitation, refer to the ‘ *Blind Rehabilitation Release Notes 5.0.28.doc’* .

## Documentation Retrieval

REDACTED

| ***File Name***   | ***Description***                                                           | ***Retrieval Format***   |    |
|-------------------|-----------------------------------------------------------------------------|--------------------------|----|
| ANRV5_0CIG.PDF    | * Blind Rehabilitation Centralized Server Installation/Implementation Guide | Binary                   |    |
| ANRV5_0VIG.PDF    | ** Blind Rehabilitation  Installation/Implementation Guide                  | Binary                   |    |
| ANRV5_0RN.PDF     | Blind Rehabilitation Release Notes                                          | Binary                   |    |
| ANRV5_0TM.PDF     | Blind Rehabilitation Technical Manual/Security Guide                        | Binary                   |    |
| ANRV5_0UM.PDF     | Blind Rehabilitation User Manual                                            | Binary                   |    |

***** This Installation Guide is only for Centralized Servers, not to be used at the field  site.

****** This Installation/Implementation Guide is for field  sites.

## Intranet

Documentation for this product is available on the intranet at the following address:

[http://www.va.gov/vdl/](http://www.va.gov/vdl/) .

This address takes you to the VistA Documentation Library (VDL), which has a listing of all of the clinical software manuals. Within the Clinical Section, Click on the Blind Rehabilitation link and it will take you to the Blind Rehab documentation.

The link below allows access to the Blind Rehabilitation home page:

http://vista.med.va.gov/clinicalspecialties/vist/index.htm

## What’s New in Blind Rehab v5.0.29

The Blind Rehabilitation package (BR-PKG-5.0.29.6) consists of changes to the JAVA components, SDS upgrade from ver.10 to ver. 18 and upgrade to KAAJEE version from 1.0.0.019 to 1.0.1.003

This BR package addresses thirteen specific functionality remedy tickets and two data base performance improvement remedy tickets.

### General User experience changes

- Reformatted the Login screen by removing the  ‘Reset’ button(HD292560)
- ‘Tracked By’ changes
    - Controlled by Role (not everyone’s staff record will appear in ‘Tracked by’)
        - VIST Coordinator, BROS, Low Vision(HD191284)
    - Only active staff records will appear in ‘Tracked by’
    - New staff added to ‘Tracked by’ without an application restart(HD386545)
- 508 issue with ‘Individual Wait list Records’(HD386546)
- Help file is corrected for ‘Modify Converted National Waitlist Record’(HD386611)
- Enter/Edit:
    - Dependents names that contain an apostrophe will display correctly (O’Brien)(HD386600)
    - Prior Rehab Training (Page4) will not accept future date for any prior training and fields masked for Prior Rehab Training ‘NO’.(HD386601)
    - A deceased patient cannot be added to BR application.(HD386604)
    - Execution of functionality is prevented for deceased patients (HD386612)

### Administrative Users/System Changes

- Edit BR Staff Screen now accepts Activation date less than or equal to deactivation date. (HD386603)
- Institution added/removed for a user, the user no longer has to logout of BR 5.0(HD403034)
- BR CO can now manage institutions better via the following changes(HD386547)
    - On Edit BR Institution, a new feature is added to display the number of active users attached to the Institution and the Institution cannot be inactivated when there is staff attached.
- SDS upgrade from v.10 to v.18
- KAAJEE upgrade from 1.0.0.019 to 1.0.1.003
- BR 5.0 application validation against the Internet Explorer 7 (HD184543)
- Database performance improvement by

- Audit Trail table partitioning(HD388035)
- Dropping indexes on Audit Trail table(HD410584)

## Appendix

| **Remedy ID/Defect ID**   | **Issue**                                                                                             | **Description**                                                                                                                                                                                                                                                                                                      | **Solution**                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|---------------------------|-------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HD292560/  BLRHB00000512  | Users resetting login after AC/VC entered                                                             | On the Login screen, after entering AV codes press Enter, it should perform Login, not Reset.  This is very frustrating, since it forces user to re-enter the AV codes.  User must also then either press the login button (further down the page) or tab 4 times and press enter.                                   | SDS and KAAJEE upgraded for this feature. The Reset button is removed.  On the Login screen, after entering AV codes press Enter, it performs Login.                                                                                                                                                                                                                                                                                                                |
| HD191284/  BLRHB00000513  | Users showing up twice under "Tracked by" option                                                      | Users showing up twice under "Tracked by" option for those who have multiple staff records                                                                                                                                                                                                                           | The ‘Tracked by’ list would display users with the following three roles:  VIST Coordinator  BROS  **Low Vision**                                                                                                                                                                                                                                                                                                                                                   |
| HD184543/  BLRHB00000514  | Blind Rehab 5.0: Print option/report data                                                             | This is an older problem with Blind Rehab 5.0: Print option/report data issues. User was using I.E. 7.0.                                                                                                                                                                                                             | Blind Rehab application has been validated /tested the with I.E 7                                                                                                                                                                                                                                                                                                                                                                                                   |
| HD386545/  BLRHB00000501  | “Tracked by” list not updated by new staff                                                            | When a new user is added to the BR application using the BR Staff task menu from the Administrator Menu, the new user is not appearing in the “Tracked By” field.                                                                                                                                                    | This issue is occurring due to the Staff being loaded at the time of application is started.  Fixed it to reflect the changes in the Staff table dynamically rather than wait for the Application server reboot.                                                                                                                                                                                                                                                    |
| HD386547/  BLRHB00000505  | Inactive Institution appearing in the Enter/Edit Menus                                                | Institution whose status in BR Institutions menu of the Administrator menu was changed to inactive is still appearing in the Institutions field of the various Task Menus of the Enter/Edit menu                                                                                                                     | The fix is based on the enhancement request. The institution cannot inactivate if there is any staff associated with the institution. If there is no staff associated to the institution then that can be inactivated and hence the institution will not appear in the institutions field of the various task menus of the Enter/Edit menu.                                                                                                                         |
| HD386600/  BLRHB00000506  | Enter/Edit BR Patient - Dependents field does not accept names with apostrophe                        | Enter/Edit BR Patient screen - Dependents field does not accept names with apostrophe                                                                                                                                                                                                                                | Dependents field can have an apostrophe in their name. Ex: O’Brien                                                                                                                                                                                                                                                                                                                                                                                                  |
| HD386601/  BLRHB00000507  | On the Enter/Edit BR Patient screen Prior Rehab Training is accepting past date                       | On the Enter/Edit BR Patient screen, if there is any prior BR Training it should accept past date instead it is accepting future date and if we select NO for Prior Rehab Training remaining fields are not getting masked.                                                                                          | The fix is applied on Page 4 of the Enter/Edit BR Patient screens where the three fields under “Any Prior Blind Rehab Training?” should not be editable unless that field is set to “YES” and for the Date of training that should allow past and current date                                                                                                                                                                                                      |
| HD386603/  BLRHB00000508  | BR Staff task menu Accepting Activation date greater than deactivation date                           | BR Staff task menu is accepting an activation date greater than deactivation date                                                                                                                                                                                                                                    | Edit BR Staff screen  is fixed  to accept the activation date less than or equal to deactivation date with a user message                                                                                                                                                                                                                                                                                                                                           |
| HD386611/  BLRHB00000510  | Wrong Help File displayed on the Converted National Waitlist Records Found - Count Screen             | Wrong help file is displayed on the Converted National Waitlist Records Found - Count screen                                                                                                                                                                                                                         | Correct Help file “Modify Converted National Waitlist Record” is updated                                                                                                                                                                                                                                                                                                                                                                                            |
| HD386604/  BLRHB00000509  | Date of Death before Activation Date                                                                  | A deceased patient can be added to the Blind Rehabilitation application, and therefore, on the “Additions to VIST Roster” report for some deceased patients the “Enrollment Date” is later than the “Date of Death”. Application allows users to make a patient as deceased from the existing patient status screen. | A deceased patient cannot be added to the Blind Rehabilitation application in future. On patient status screen it is fixed by removing the DECEASED from the dropdown. This avoids manual update to patient record as deceased.                                                                                                                                                                                                                                     |
| HD386612/  BLRHB00000511  | Prevent execution of functionality for a deceased patient                                             | Prevent execution of functionality for a deceased patient such as not permitting activation or enrollment of deceased patients throughout the application                                                                                                                                                            | The below screens fixed to prevent execution of functionality for a deceased patient.  In all the below screens, all the fields have been marked as non-editable for  a deceased patient, so no normal functionality can be performed for deceased patient.  Enter/Edit BR Patient  Enter/Edit Low Vision Patient  Enter/Edit Patient Status  Enter/Edit Create Referral  Enter/Edit VARO Claims  Enter/Edit Eye Exam (Eligibility)  Benefits and Service Checklist |
| HD403034/  BLRHB00000540  | Institution is added/removed from current user, user will no longer have to logout of 5.0 application | Staff has to logout of the BR application so that they can see the correct list of institution associated with the staff anytime they make change to the institutions attached to the staff.                                                                                                                         | when an institution is added or removed from a user, user will no longer have to logout of the 5.0 application                                                                                                                                                                                                                                                                                                                                                      |
| HD410584                  | System Operating Extremely Slow                                                                       | Improve system performance by removing the indexes on the Audit Trail table                                                                                                                                                                                                                                          | This is a Database patch consists of the data scripts for dropping the indexes and creating the indexes on the AUDIT_TRAIL table                                                                                                                                                                                                                                                                                                                                    |
| HD388035                  | AUDIT\_TRAIL table vexes DBA                                                                          | A high volume of audit trail records may cause database performance problems. Improve System Performance by archiving over 2.5 million Audit Trail records to a separate archive table                                                                                                                               | This is a Database Patch. There are more than 2.5 million records in Audit Trial table and it has become an issue for a DBA in backing up the Audit Trail records. To reduce the backup issue and also to improve the performance of the BR application for audit trial transactions, the Audit trial table records moved to history table. The Audit  trail records and Audit trial history records are combined for the AUDIT_TRAIL view                          |
| HD386546/ BLRHB00000503   | Screen reader not reporting record contents correctly                                                 | 508 compliance issue: Individual Wait List Records-Regular screen shows information on one line.  The screen reader shows info on two lines                                                                                                                                                                          | The fix is validated with the Accessibility team. It is corrected to display the information on one line.                                                                                                                                                                                                                                                                                                                                                           |
