---
title: Mental Health Assistant Patient Plan - Assign  Assessment - Staff Entry Web User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Mental Health Assistant Patient Plan - Assign  Assessment - Staff Entry Web
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: ![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/001.png)
audience: 
keywords: 
  - patient
  - table
  - assessment
  - entry
  - staff
  - contents
  - assign
  - assignment
  - mental
  - health
page_count: 0
word_count: 4030
section_count: 7
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/CLIN_0004AY_UM_158_MHA_WEB.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/CLIN_0004AY_UM_158_MHA_WEB.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

Patient Plan - Assign Assessment - Staff Entry(MHA Web)

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/001.png)

User Manual

Version 3 (MHA3)

May 2021

Office of Information and Technology (OI&T)

Product Development

Revision History

|               |          |                                                                           |                     |
|---------------|----------|---------------------------------------------------------------------------|---------------------|
| Date          | Revision | Description                                                               | Author(s)           |
| May 2021      | 1.3      | Patch number 158. Remove references to “PaSE” and replace with “MHA Web”. | Booz Allen Hamilton |
| February 2021 | 1.2      | Revised/added screenshots for updates to application                      | Booz Allen Hamilton |
| January 2021  | 1.1      | Revised/added screenshots for updates to application                      | Booz Allen Hamilton |
| December 2020 | 1.0      | Initial creation of MHA Web User Manual                                   | Booz Allen Hamilton |

<u>Table of Contents</u>

# MHA Web Application User Manual Content


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [MHA Web Application User Manual Content](#mha-web-application-user-manual-content)
- [Mental Health Assistant – Main Web Page Sections](#mental-health-assistant-main-web-page-sections)
  - [MHA Web Header](#mha-web-header)
    - [Active Assignments](#active-assignments)
    - [Completed Assignments](#completed-assignments)
    - [Creating an Assignment](#creating-an-assignment)
    - [Instrument Categories](#instrument-categories)
    - [View All Instruments](#view-all-instruments)
    - [View Instruments Categories](#view-instruments-categories)
    - [Instrument Chosen](#instrument-chosen)
    - [Tools](#tools)
    - [Ordered By](#ordered-by)
    - [Interviewer](#interviewer)
    - [Location](#location)
    - [Consult](#consult)
    - [Cancel](#cancel)
    - [Patient Entry](#patient-entry)
    - [Staff Entry](#staff-entry)
  - [Reviewing Assignment IDs in Active Assignments Table](#reviewing-assignment-ids-in-active-assignments-table)
    - [Edit an Assignment](#edit-an-assignment)
    - [Delete an Assignment](#delete-an-assignment)
  - [Executing a Staff Entry Assignment](#executing-a-staff-entry-assignment)
    - [Cancel](#cancel-1)
    - [Finish](#finish)
    - [Save Note](#save-note)
    - [Do Not Save Note](#do-not-save-note)
    - [Copy Text](#copy-text)
    - [Restricted Instrument(s)](#restricted-instruments)
  - [Reviewing Completed Assessments (Reports / Graphs)](#reviewing-completed-assessments-reports-graphs)
    - [Reports](#reports)
    - [Graphs](#graphs)
  - [Application Time-Out Warnings](#application-time-out-warnings)
    - [Staff Entry 10-Minute Timeout:](#staff-entry-10-minute-timeout)
    - [MHA Web Server Timeout:](#mha-web-server-timeout)
  - [Special Instrument Notification in Staff Entry](#special-instrument-notification-in-staff-entry)
![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/002.png)
Click on the MHA Web option located on the CPRS tools menu item to start Mental Health Assistant – Web (MHA Web). The VA Single Sign-On page is displayed.
\*\*\*NOTE\*\*\* When launching MHA Web from within CPRS, the application will open with the patient record for the current patient having focus in CPRS.  If the user changes the patient in CPRS, MHA Web will NOT automatically update, as this functionality does not work.  A refresh of the page will not result in MHA Web refreshing the patient data to the new patient.  In order to avoid potential erroneous patient record updates for the wrong patient, MHA Web must be closed and re-launched every time the user changes the patient in CPRS.  <u>Patient name must be verified before entering questionnaire data</u>.
![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/003.png)
There are 3 options for signing into the application using the VA Single Sign-On page:
- VA PIV Card
- Windows Authentication
- VA Network ID
The most common single sign-on used is the VA PIV Card validating your credentials with your VA PIV Card PIN.
![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/004.png)
The Windows Authentication sign-on option will use your credentials that were validated on initial login to the VA network to validate your credentials/access to the application. The sign-in method used the least is the VA Network ID option, which is disabled for most users. This option requires a PIV exemption in order to gain access to the application.
![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/005.png)

# Mental Health Assistant – Main Web Page Sections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health Assistant – Web (MHA Web) is divided into three sections. These sections are:

- MHA Web Header
- Active Assignments
- Completed Assignments

Example: Mental Health Assistant – Webmain page

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/006.png)

## MHA Web Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MHA Web Header displays the currently selected patient’s name and last 4, along with Print and Help buttons. All functions performed in MHA Web apply to this patient.

### Active Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Active Assignments table displays all staff and patient entry assessments that have been assigned to the patient. These assignments can be edited, executed or deleted, based on situational requirements. Reference the “Edit an Assignment” and “Delete an Assignment” sections of this document for more detail.

Example: Active Assignments table

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/007.png)

### Completed Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Completed Assignments section displays all instruments that have been completed by a patient. In order to see the history of a specific instrument, select the instrument and then select the desired date from the list of dates that appears on the left side of the instrument report field.

#### Example: Completed Assignments field 

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/008.png)

### Creating an Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Web provides users the ability to create assignments for patients. In order to create an assignment, the user must select the Add Assignment icon ![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/009.png) above the “Active Assignments” table. This action will cause a new screen to appear. This is the “Assign Assessment” modal which will be used for assigning instrument(s) to a patient and completing the assignment creation process. This modal is also the starting point for a staff entered assessment. This will be covered in greater detail in the Executing a Staff Entry Assignment section of this document.

#### Example: Assign Assessment Modal 

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/010.png)

The first step to creating an assignment for a patient is selecting the desired instrument(s) for that patient. In order to select an instrument, the user must ‘check’ the box beside the instrument name. If more than 1 instrument is desired, the user must ‘check’ the box beside all desired instruments.

Example: Assign Assessment Modal

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/011.png)

<u>  
</u>

### Instrument Categories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The instruments have been sorted into sub-lists under specific categories. If the user is unable to locate the desired instrument for the patient, the user can select the ![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/012.png) icon next to a category to expand the list of instruments within that category. Inversely, if the user wants to reduce the list of instruments within a category, they need to select the ![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/013.png) icon.

Example: Expanded Category

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/014.png)

<u>  
</u>

### View All Instruments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the user does not know which category the instrument(s) they are looking for are associated with, there is a View All Instruments option at the bottom of the screen that allows the user to list all available instruments in alphabetical order. In order to access the full list of available instruments, the user can use the scroll bar to move down the page to find the desired instrument(s).

Example: Expanded Category

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/015.png)

Example: Assign Assessment Modal

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/016.png)

<u>  
</u>

### View Instruments Categories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inversely, if the user wants to return to the categorized view of the available instruments, they can select the View Instrument Categories option and the modal will return to the original display format.

Example: Assign Assessment Modal

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/017.png)

### Instrument Chosen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the instrument(s) are selected, the user can see those instruments in the Instruments Chosen field on the right side of the Assign Assessment modal.

Example: Instruments Chosen Field

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/018.png)

<u>  
</u>

### Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user is given the ability to adjust the order of the instruments by using the Up and Down arrows to prioritize the list of instruments in a multi-instrument assessment. There is also a Delete button that allows the user to remove instrument(s) from the list before creating the assignment. The user needs to select the instrument(s) they do NOT want to include in the assessment (instrument(s) will be highlighted), and then select the Delete button.

Example: Instruments Chosen Field (Tools)

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/019.png)

### Ordered By

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user must select the name of the individual ordering the assessment. The text search for this field is dynamic, and as soon as the user has entered at least 2 letters into the field, the application will begin searching for and returning to the user a list of viable names in a drop-down field. Highlighting or selecting the name will finish the process of entering the “Ordered By” name. This is a required field, and without it filled in, the assignment will not be created.

Example: Ordered By Field

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/020.png)

<u>  
</u>

### Interviewer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user must select the name of the individual interviewing the patient for the assessment. The text search for this field is dynamic, and as soon as the user has entered at least 2 letters into the field, the application will begin searching for and returning to the user a list of viable names in a drop-down field. Highlighting or selecting the name will finish the process of entering the “Interviewer” name. This is a required field and without it filled in, the assignment will not be created.

Example: Interviewer Field

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/021.png)

### Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user must select the name of the location the assessment. The text search for this field is dynamic, and as soon as the user has entered at least 2 letters into the field, the application will begin searching for and returning to the user a list of viable names in a drop-down field. Highlighting or selecting the name will finish the process of entering the “Location” name. This is a required field, and without it filled in, the assignment will not be created.

Example: Location Field

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/022.png)

<u>  
</u>

### Consult

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user has the option to select a consult if there is a consult related to the assessment. The “Consult” can be selected be clicking the drop-down arrow beside the “Consult” field and selecting the appropriate consult from the displayed list. This is an optional field and is NOT required in order to complete the assignment creation process.

Example: Consult Field

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/023.png)

### Cancel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the user does not want to continue with the creation of an assignment, they can select the Cancel button, which will close the “Assign Assessment” modal and return the user to the MHA Web landing page.

Example: Assign Assessment Action Buttons

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/024.png)

### Patient Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When selecting the Patient Entry button, the application will create an Assignment ID that will be displayed in a small window on the screen. This number is the ‘PIN’ that will be given to a patient in order for the patient to complete their assessment.

Example: Assign Assessment Action Buttons

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/025.png)

The patient name must be verified before entering questionnaire data.  Once verified, the clinician or other representative in the MH clinic will provide the PIN to the patient.  The patient will use either a kiosk or an iPad, enter the PIN and the last 4 numbers of their SSN into the landing page of the Patient Entry application, and complete the desired administration(s) for the clinician.  For a more detailed explanation of the process for using the Patient Entry application, reference the “MHA Patient Entry User Manual” in the VDL

Example: Patient Entry Assignment ID Modal

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/026.png)

### Staff Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When selecting the Staff Entry button, the application will immediately launch the assessment in Staff Entry mode. This is the mode the clinician will use to complete the patient assessment. Further detailed information regarding this functionality can be found in the Executing a Staff Entry Assignment section.

Example: Assign Assessment Action Buttons

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/027.png)

The patient name must be verified before entering questionnaire data.

## Reviewing Assignment IDs in Active Assignments Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you create an Assignment ID by selecting the Patient Entry button in the Assign Assessments modal, the Active Assignments table is automatically updated with the new Assignment ID.

Example: Active Assignments Table

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/028.png)

If needed, the user can edit or delete the Assignment ID, whether it be “Patient” or “Staff” entry, by selecting the appropriate icon at the top of the table.

### Edit an Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to edit an assignment, select the Assignment ID you wish to edit by checking the checkbox beside that ID. Then, select the edit icon ![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/029.png)in order to perform the desired action. The Edit Assignment window will appear allowing you to perform the same functions as you would when creating an assignment with 2 exceptions. You will not be able to change the Ordered By nor the Consult fields. To save any changes, select the Save button. If you do NOT want to save changes made to the assignment, select the Cancel button. Either action will return the user to the MHA Web landing page.

\*\*\*NOTE\*\*\* It is important to remember that an Assignment ID CANNOT be edited once the assessment has been started (anything above 0% complete). If an assignment is partially complete, the ‘edit’ option will not be available to the user. The only options are to complete the assignment or delete it.Example: Edit Assignment Window

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/030.png)

### Delete an Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to delete an assignment, select the Assignment ID you wish to delete by checking the checkbox beside that ID. Then, select the Delete icon ![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/031.png) in order to perform the desired action. The Delete Assignment window will appear allowing you to review and confirm the assignment before deleting it. To delete the assignment, select the Delete button. If you do NOT want to delete the assignment, select the Cancel button. Either action will return the user to the MHA Web landing page.

\*\*\*NOTE\*\*\* You can delete an assignment ID once the assessment has begun (anything above 0% complete). If an assignment is partially complete, the ‘delete’ option will be available to the user. The only options for the assignment are completing the assignment or deleting it.Example: Delete Assignment Window

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/032.png)

## Executing a Staff Entry Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the setup of an assignment has been completed, and the user selects the Staff Entry button, the “Staff Entry” mode of MHA Web will automatically launch and allow the user to begin completing assessment(s).

Example: Staff Entry Execution Screen

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/033.png)

### Cancel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the user decides they do not want to complete the assessment, they can select the Cancel button to end the “Staff Entry” session. MHA Web will prompt the user to confirm their selection by opening a “Cancel Assessment” modal. The user can either select “Yes” to continue, or “No” to return to the assessment. If the user selects “Yes”, the user will be returned to the MHA Web landing page and a “Staff” assignment will be created in the “Active Assignments” table. In the event there are multiple instruments in the assignment, “Staff Entry” will take the user to the next instrument in the assignment after selecting Cancel. This will continue until the user has cancelled out of all instruments in the assignment.

Example: Cancel Assessment Modal

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/034.png)

### Finish

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once an assessment has been completed, the user can select the Finish button, where MHA Web will open the Progress Note window that allows the user to “Save Note”, “Do Not Save Note” or “Copy Text”.

Example: Finished Assessment (Unsubmitted)

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/035.png)

Example: Finished Assessment (Submitted)

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/036.png)

### Save Note

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Selecting the Save Note button will create a progress note for the administration in CPRS, and the progress note will also be accessible in the “Completed Instruments” section of MHA Web.

Example:Save Note Button

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/037.png)

### Do Not Save Note

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Selecting the Do Not Save Note button will NOT create a progress note for the administration in CPRS. However, the report created from the completed administration will be accessible in the “Completed Instruments” section of MHA Web.

Example: Do Not Save Note Button

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/038.png)

### Copy Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Selecting the Copy Text button allows the user to copy the progress note information to the clipboard for pasting into other applications.

Example: Copy Text Button

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/039.png)

### Restricted Instrument(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the instrument being completed in the assessment is a restricted instrument, when the user selects Finish, MHA Web will NOT create a progress note to be stored in CPRS, and a modal will appear notifying the user as much. Selecting Continue will return the user to the MHA Web main landing page where they can then select the instrument name and view the report for that date of completion.

Example: Restricted Instrument Warning Modal

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/040.png)

## Reviewing Completed Assessments (Reports / Graphs) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon the completion of an assessment by either the patient, or a user, a report is generated for the completed assessment and is viewable in the “Completed Instruments” section of the main MHA Web landing page. In order to view this report, the user needs to select the desired instrument name, and then select the appropriate date for the report. Once selected, MHA Web will display the details of the report for review.

Example: Completed Instruments Field – Displayed Report

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/041.png)

### Graphs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option to review the data within the report in a graphical format is also available to the user. The user must select the ![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/042.png) icon in order to see display the data. The history of all assessments related to that selected instrument will be available for review, and a table of information will be provided for reference.

Example: Graphed Instrument Results Display

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/043.png)

A legend is provided below the graph that displays the metric associated with each graphed color for assessments that have multi-value metrics. This information comes directly from the data table below the graph.

The user can also use the slider bar at the top of the graph to display data based on a date range desired by the user. The user must use their mouse to click on the slide bar and then drag it right or left to gain the desired display of graphed data.

Example: Graph Slider Bar Adjustments (Expanded Range)

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/044.png)

Example: Graph Slider Bar Adjustments (Narrowed Range)

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/045.png)

The table can also be filtered for specific trending information if the user so desires. This can be accomplished by selecting the ![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/046.png) icon beside a specific category in order to expand the subcategories and review the results. In order to graph the results for this subcategory, select the checkbox beside the category in the data reference table. The graphical display will automatically update based on the user selection, and the legend will also update to reflect which colors are associated with each component of the subcategories. Inversely, if the user wants to close the expanded category, they need to select the ![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/047.png) icon.

Example: Expanded Category w/ Refreshed Data

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/048.png)

## Application Time-Out Warnings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Web has 2 different timeout requirements. These are relative to the function and security of the application.

### Staff Entry 10-Minute Timeout: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the user is completing an administration and is idle for 10 minutes, MHA Web will automatically end that session and return the user to the main landing page of the application. At the 9-minute mark, a warning modal will appear allowing the user to continue the administration or log out of the administration.

Example: 10-Minute Timeout Modal

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/049.png)

### MHA Web Server Timeout: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the user is inactive in the application for 1 hour, MHA Web will automatically end that session and log the user out of the application. At the 50-minute mark, a warning modal will appear allowing the user to continue the session or be automatically logged out of the session.

Example: 1 Hour Timeout Modal

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/050.png)

## Special Instrument Notification in Staff Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Certain instruments require special training/certification before they can be executed by a clinician. When a clinician attempts to complete any of the MOCA instruments, a warning modal will appear that informs them of the requirement for the certification training required in order to administer the instrument, and this modal must be acknowledged before the clinician can proceed with the administration.

Example: MOCA Certification Modal

![](mental-health-assistant-patient-plan-assign-assessment-staff-entry-web-user-manu/051.png)