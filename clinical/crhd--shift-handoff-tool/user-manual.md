---
title: Shift Handoff Tool Version 1 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: CRHD
app_name: Shift Handoff Tool
section: CLI
app_status: active
pkg_ns: CRHD
patch_ver: 1
patch_id: CRHD*1
group_key: "CRHD:CRHD:1"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 19%\\" /> <col style=\\"width: 43%\\" /> <col style=\\"width: 37%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th>Date</th> <th>Description of Change</th> <th>Technical Writer, Project Manager</th> </tr> </thead> <tbody> <tr class=\\"odd\\"> <td>June 2008</td> <td>Initial R"
audience: 
keywords: 
  - table
  - contents
  - handoff
  - shift
  - tool
  - patient
  - team
  - version
  - manual
  - patients
page_count: 0
word_count: 5290
section_count: 14
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2008
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Shift_Handoff_Tool/crhdum.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Shift_Handoff_Tool/crhdum.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=175"
---

Shift Handoff Tool Version 1.0User Manual

![](shift-handoff-tool-version-1-user-manual/001.png)

June 2008

Department of Veterans AffairsOffice of Information and Technology (OI&T)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 43%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description of Change</th>
<th>Technical Writer, Project Manager</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>June 2008</td>
<td>Initial Release</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>March 2017</td>
<td><p>Patch CRHD*1*6</p>
<p>Two-factor authentication (2FA)</p>
<p>Pages <a href="#how-to-start-shift-handoff-tool">6</a>, <a href="#shift-handoff-tool-at-a-glance">36</a>.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

## Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There has been a great deal of variability in Physician to Physician communication. This is recorded in the medical literature.

The Shift Handoff Tool was developed by the Indianapolis VAMC Development Group under the project name CAIRO with assistance and testing from the following sites: Washington DC VAMC, Dallas VAMC, Loma Linda VAMC, Central Iowa (Des Moines and Iowa City VAMC), White River Junction VAMC, Denver VAMC, Ann Arbor VAMC, San Antonio VAMC, and Altoona VAMC.

The design and development of the Physician Handoff Tool seeks to address the variability in Physician to Physician communication at Patient Handoff.

Data elements such as Demographics, Code Status, Allergies, Medications, Problem List, Admitting Diagnosis, Laboratory and Consults orders are some of the data elements communicated in a standardized way by this tool.

By providing a tool to do this, it is hoped that errors in care will be prevented because the information will be communicated in a clear, readable, standardized format.

A handoff report can be printed and carried with the physician.

The information can be printed out and carried with the Physician during rounds. Notes can be written on the paper copy and re-entered into the Shift Handoff Tool for the providers on the next shift.

Table of Contents

# Startup


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Preface](#preface)
- [Startup](#startup)
  - [How to Start Shift Handoff Tool](#how-to-start-shift-handoff-tool)
- [Menus](#menus)
  - [File](#file)
    - [Windows Operation](#windows-operation)
  - [Edit](#edit)
  - [Directory](#directory)
    - [Phone Directory](#phone-directory)
    - [Team Info](#team-info)
  - [Help](#help)
- [Preferences](#preferences)
  - [Multiple Forms](#multiple-forms)
    - [Working Example](#working-example)
  - [Selecting a Patient list](#selecting-a-patient-list)
  - [Patient Data Dialog](#patient-data-dialog)
    - [Patient Demographics](#patient-demographics)
    - [Contact Information](#contact-information)
    - [Code Status](#code-status)
    - [Temporary Fields](#temporary-fields)
    - [Meds](#meds)
    - [Covering Phy](#covering-phy)
    - [Allergies](#allergies)
    - [Labs/Imaging](#labsimaging)
    - [Consults](#consults)
    - [File Menu](#file-menu)
    - [Team Info Menu](#team-info-menu)
    - [Help Menu](#help-menu)
    - [Add/Delete Patients](#adddelete-patients)
    - [Delete Personal list.](#delete-personal-list)
    - [Add providers to a List](#add-providers-to-a-list)
  - [H.O.T List](#hot-list)
    - [Create a H.O.T List (Hand-Off Team)](#create-a-hot-list-hand-off-team)
    - [Creating a New Team List](#creating-a-new-team-list)
    - [Adding New Patients and Providers to the List](#adding-new-patients-and-providers-to-the-list)
- [Print A Report](#print-a-report)
  - [Print/Preview Window](#printpreview-window)
  - [Print Document](#print-document)
- [Shift Handoff Tool at a Glance](#shift-handoff-tool-at-a-glance)

## How to Start Shift Handoff Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two ways to start the shift handoff tool depending on how IRM set things up. They are:

1.  From the icon.
2.  ![](shift-handoff-tool-version-1-user-manual/002.png)From the CPRS Tools menu.

To start from and Icon simply double click the Shift Handoff Tool icon on your desktop:

To start from the CPRS tools menu, follow these steps:

1.  Log into CPRS
2.  Go to the Tools menu in CPRS, select the Shift Handoff Tool option from the drop down list.

Either way you will have to log into the Shift Handoff Tool using your CPRS sign on credentials.

![](shift-handoff-tool-version-1-user-manual/003.png)

Select PIV Credentials

![](shift-handoff-tool-version-1-user-manual/004.png)

Enter Your PIN

![](shift-handoff-tool-version-1-user-manual/005.png)

Click OK

# Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Functions within this application are accessed one of three ways: Buttons, the menu bar, and drop-down menus. If you don’t see the action you want in the buttons or menu bar, try right-clicking on the object.

Other actions that work throughout this application:

- Single-click—selects an object but takes no other action. Usually it just highlights the objects in preparation for you to take another action, such as right-clicking as described below.
- Double-clicking—means activate the current selection. If you are building a list, double clicking moves an item into the list. If you have already built a list, sometimes double-clicking deletes an item and at other times right-clicking will reveal a drop-down menu with delete on it. Try right-clicking first.
- Shortcuts—many actions such as menu commands have keyboard shortcuts. If a menu command has a keyboard shortcut it will be listed next to the command in the menu. Example: Change Preference in the File menu has the shortcut Ctrl+Alt+C. This signifies a key chord in which you press all three keys simultaneously.

If a menu command is grey or missing, it is not currently available. Availability is determined by what keys and other privileges are held, and what screen you are currently viewing.

## File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The menu commands under the File menu are:

- Change Preference—may be used at any time by any user to change the presence set that controls the appearance of and information in the report.
- Assign Providers to Team/List—if active, brings you to a dialog to assign or edit providers for the currently selected list.
- Preference Configuration—only applies to holders of the CRHD SHIFT CHG HANDOFF MGR security key, allows editing of any preference set.
- HOT List Configuration—only applies to holders of the CRHD HOT TEAM MGR security key.
- Exit—one of eight ways to close the program. Can you name the other seven? (Answer on the next page.)

### Windows Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One of the advantages of Windows is that much of the look and feel of a program is controlled by the operating system. This frees the program to work on more important stuff, but it also means that there is more than one way to perform most operations in a Windows program. This sometimes causes confusion because one teacher may show you one way to do something and another teacher may show you a completely different way to do the same thing. It can also be an advantage. That is, if you know two ways of doing something, you may choose to use the method you are most comfortable with.

There are eight (8) ways to close Shift Handoff Tool (and most Windows programs). They are:

1.  From the File menu, select Exit.
2.  Hold the Ctrl key down while pressing X.
3.  Hold the Alt key down while pressing F4.
4.  Click on the X in the upper right-hand corner of the window.
5.  Click on the icon in the upper left-hand corner of the window and select Close from the resulting drop-down menu.
6.  Right click in the title bar and select Close from the resulting drop-down menu.
7.  Press the keys Ctrl+Alt+Del simultaneously. When the Windows Security window opens, click the Task Manager Window. From the Applications tab, select Shift Handoff Tool. Then click on the End Task button.
8.  Shut down the machine. When a Windows machine is shut down, Windows first closes all running programs, assuming you are running Windows XP.

## Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the Edit menu, you can change the font used in text boxes, button caps, and some other places in the windows and dialogs that make up the tool. The following picture shows the font being changed to 24 points. (A point is 1/72 inch, so 24 point letters are one third of an inch high).

![](shift-handoff-tool-version-1-user-manual/006.png)

The larger font sizes tend to crowd the panes in dialogs. Most dialogs in Shift Handoff Tool can be resized by positioning the cursor at a corner, holding down the left mouse button, and dragging the mouse.

## Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two commands under the Directory menu: Phone Dir and Team Info as shown in this screen shot:

![](shift-handoff-tool-version-1-user-manual/007.png)

### Phone Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When selecting the Phone Directory, select a directory listing based on Team, Person, Specialty, Service, or HOT List as in this screen shot:

![](shift-handoff-tool-version-1-user-manual/008.png)

The data on each person is taken from the New Person File. It includes: Name, Title, Extension, Pager, Room Number, Email Address, Fax Number, Service, Service Mail Code.

![](shift-handoff-tool-version-1-user-manual/009.png)

### Team Info

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu option looks for a text document by the same name as the team list, the document can be used to share general information and announcements with the team using this team list. Such information as the time of rounds or replacements because of vacation schedules are appropriate for this document. Care should be taken for keep patient specific information out. Patient specific information needs to be reserved for the temporary fields.

Holders of the CRHD SHIFT CHG HANDOFF MGR key may edit this document. It can be re-saved by right clicking in the text field and choosing Save from the drop-down menu.

Create a text file by the same name as the team list, (name must match exactly), this file must be located in the same directory as the Hand-off tool or a directory specified in the preference setup. It can be displayed or printed. A hint will be display with the files last edit date. It will be up to your site in deciding how this file is used and maintained.

> **NOTE:** This file is for team-centric information, not patient information. All users need to be cautioned that no patient, individually identifiable information should be placed in this file.

You can override the location by putting a directory address in the Preference Configuration dialog Team Information tab and you can override the file name with the Assign Providers to Team/List dialog.

## Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Help menu gives you two choices. The first, Content, opens the help file for this application. The second, About, gives important information about the program including the version and places you can go for additional information about the application.

# Preferences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your Clinical Applications Coordinator (CAC) or Shift Handoff Manager can set up Handoff Team (HOT) lists and set different preference configuration for each list. All configurations available are listed for you to choose upon entry into the program. The dialog to accomplish this looks like this:

![](shift-handoff-tool-version-1-user-manual/010.png)

To get past this dialog to the main program, double click on one of the Preference names. You can make whatever Preference you choose your default preference by answering affirmatively to this dialog:

![](shift-handoff-tool-version-1-user-manual/011.png)

## Multiple Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each division, service, team, and user can have their own configuration. The configuration controls what data appears on in the Patient Data dialog and in turn on the printed report. Each team should work closely with their Clinical Applications Coordinator (CAC) or Shift Handoff Manager to make sure the configurations available closely meet the team needs. On the other hand, a proliferation of configurations can lead to confusion. Here is a rundown on what can be controlled by careful configuration management:

![](shift-handoff-tool-version-1-user-manual/012.png)

Each Preference form or setup has the mandatory fields of

- Patient demographics
  - Name
  - SSN
  - Age
  - Sex
  - Ward
  - Room/Bed
- Active medications
- Code status
- Allergies

Optional fields are:

- patient demographics
  - Date of Birth
  - Admission Date
  - Admission Diagnosis
  - Team
  - Attending
  - Primary Care Provider
  - Day in Admission (length of stay)
  - Whether the SSN is printed as all 9 or last 4
- Zero to four Temporary fields
- Whether medications list as detail or summary
- Exclude IVs from medication list
- Consult Orders
- Labs/Imaging Orders
- List of Team Residents
- List of Team Medical Students
- Whether patient demographics print with or without labels
- Whether the printout will be oriented portrait or landscape
- What order the printout will be by:
  - Patient
  - Room/Bed Location
  - Patient Location

Additionally, each team can have an information file that team members can access from the program display.

### Working Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Suppose Ambulatory Care wanted their printout to include the following fields:

Temporary field 1: HPI

Temporary field 2: Problems

Temporary field 3: Clinical Course

And suppose Orthopedics wanted their printout to include these fields:

Temporary field 1: HPI-M

Temporary field 2: Problems

Temporary field 3: To Do List

Temporary field 4: Pending Workup

Notice the field named Problems the data displays for both teams:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Team setup: Ambulatory Care</p>
<p>![](shift-handoff-tool-version-1-user-manual/013.png)</p></th>
<th><p>Team setup: Orthopedics</p>
<p>![](shift-handoff-tool-version-1-user-manual/014.png)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Notice that the data in the Temporary field labeled Problems is the same for this patient in both forms. This is because temporary fields with the same label are shared between forms. This is also why the first field, labeled HPI (for History of Present Illness) is labeled HPI-M in the Orthopedics form—so the same data will not appear in both the Ambulatory Care and Orthopedics form. Your CAC is responsible for coordinating the naming of temporary fields so the unwanted clashing will not occur between forms.

> **NOTE:** Temporary fields are just that, temporary. They are never permanently stored in VistA. The default storage time is 2 days. If you require your temporary fields to persist longer, talk with your CAC or Shift Handoff Manager.

Any data intended for permanent retention must be entered into a clinical note and signed.

## Selecting a Patient list

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have a CPRS GUI Default Patient List the list is already selected.

If you do not have Default Patient List or if the list is empty you can select another list.

If the list you selected has no patients, ‘No patients found’ will display in the Patient box.

Once you have selected a list type that item will turn red and the type will appear in the ‘Type Name’ box.

To see the patients assigned to a list, single click the list name and the patients will display in the Patient box on the right. The name of the list selected will appear in the ‘List Name’ box.

To select a list you can double click the list or hit the Submit button at the bottom of the screen.

You cannot select multiple lists.

![](shift-handoff-tool-version-1-user-manual/015.png)

## Patient Data Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen capture shows a list that was selected from the screen above. To see each patient’s data click on the Patient and the data will update. You may also delete a patient from the list by right clicking and select delete from the pop-up menu.

This is the preliminary screen you have to go through before obtaining a printout. The intention is for you to review each patient’s data before going on.

![](shift-handoff-tool-version-1-user-manual/016.png)

The following data elements are displayed:

### Patient Demographics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Name, SSN, Room, Team (specialty), AGE, Sex, DOB, Location, Adm Date, Adm DX, Day/Adm. The full SSN is displayed here, Your print out has the option to be printed with full SSN or just the last 4 of the SSN—this is controlled by the preference setup. For patient privacy we recommend that you only print the last 4 of the SSN.

#### Attn (Attending) field

This information comes from the patient’s record in Vista.

#### PCP (primary care provider) field

This information comes from the patient’s record in Vista.

### Contact Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Optional - set up from the Preference page, the selection page or the HOT list configuration. If you have access (talk with your CAC), you can right click on the list name and select Assign Providers to Team/List from the drop-down menu as in this example:

![](shift-handoff-tool-version-1-user-manual/017.png)

### Code Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This data comes from the orders file. There is an attempt to locate an orderable item or an order that matches the DNR text from the Preference page. The patient’s active orders are scanned for orderable items. If no order is found then the DNR text parameter is used. If an order is not found the message Code Status Not Found is displayed.

Remember: This is an attempt to find a DNR order, if a DNR order is not found that does not mean there is no order. The ultimate responsibility is on the physician to verify this information.

### Temporary Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can have up to four temporary fields defined. If a temporary field is defined in the preference setup, it will display for every patient on your list. The data in these fields is entered by Shift Handoff Tool users to reflect the current state and needs of the patient. These fields are managed by their names—fields with the same name in different preference setups are the same. If your clinic wants unique data then the field name needs to be made unique by adding a list identifier (example: ADMISSION DIAGNOSIS-CARDIAC-ICU has different contents than ADMISSION DIAGNOSIS-ER). Each field name is limited to 30 characters.

The user and date/time are saved with the text every time a temporary field is edited and checked every time the field is accessed for display or printing. If the information in the field for a patient is older that the expiration parameter set in the preference, the field is reset.

There is a limit of 720 characters for each temporary field. Attempts to put more text in a temporary field, such as when data is copied and pasted from a progress note, results in the text being truncated losing any text that exceeded the 720 character limit. The intent of these temporary fields are to transfer the most pertinent facts about the care needs of patients from one shift to another, not to exhaustively document the condition of the patients.

> **NOTE:** Temporary Fields are limited to 720 characters each.

### Meds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Medications come from the patient record and are not editable by users. Medications can be displayed as a summary (names only) or as a detailed view. These setting are can be changed in the Preference Configuration menu – data object tab.

### Covering Phy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Covering Physician is an editable field that follows each patient, this data will display on the printout in the patient demographic section. It can be filled in here by any user. It has no time limit.

### Allergies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Allergies come from the patient record and are not editable by users.

### Labs/Imaging 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Optionally Labs and Imaging orders can be displayed on the Enter/Edit temporary data screen. The data comes from the patient’s record in Vista. Only appears on the Patient Data dialog, does not go through to the printed report because of space requirements.

### Consults 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Optionally Consult orders can be displayed on the Enter/Edit temporary data screen—data comes from the patient’s record in Vista. Only appears on the Patient Data dialog, does not go through to the printed report because of space requirements.

### File Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Save - Save temporary data.

Print - Send data to printer.

Preview - Preview report.

Exit - Close screen return to Select List Screen.

#### HOT List Menu

List by Provider – if setup, list all patients on the Handoff Team (HOT) List that are assigned to a provider.

### Team Info Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu option looks for a text document by the same name as the team list, the document can be used to share general information and announcements with the team using this team list. Such information such as the time of rounds or clinician replacements because of vacation schedules are appropriate for this document. Care should be taken for keeping patient specific information out. Patient specific information needs to be reserved for the temporary fields.

Holders of the CRHD SHIFT CHG HANDOFF MGR key may edit this document. It can be re-saved by right clicking in the text field and choosing Save from the drop-down menu.

### Help Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Specific help for the Patient Data dialog is displayed from the help menu in this dialog. Pressing the F1 key has the same effect as selecting Content from this Help menu.  
Managing Lists

### Add/Delete Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can add or delete patients from your list. To add: Select patients from the Patient list box and double click. To delete: Select patient from the ‘Patient’ box and right click and select delete. For the H.O.T. List, if you hold the manager key (CRHD SHIFT CHG HANDOFF MGR) you will be able to add patients to the list from the selection screen. You will have the following options:

![](shift-handoff-tool-version-1-user-manual/018.png)

1.  Create a New Personal List
3.  Create a one-time List
4.  Save Personal List – add or delete patients from an existing Personal List. (note: any personal list can be accessed from the team lookup).
5.  Save HOT List – need the HOT List manager’s key (CRHD HOT TEAM MGR) to add or delete from HOT lists.

### Delete Personal list.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select the list to delete and right click.

![](shift-handoff-tool-version-1-user-manual/019.png)

### Add providers to a List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can get to a dialog that assigns providers to a list by right-clicking on that list and selecting Assign Providers to Team/List. If it is anything other than a Personal list you will need permission to perform this task—see your CAC or Shift Handoff Manager for this permission.

![](shift-handoff-tool-version-1-user-manual/020.png)

The following dialog appears:

![](shift-handoff-tool-version-1-user-manual/021.png)

The Office Phone and Pager are initially retrieved from the New Person file. You can override these numbers by typing in new numbers in this dialog. Shift Handoff Tool does not update the NEW PERSON file., so if these numbers need to be changed permanently they will have to be changed using the VistA USER MANAGEMENT menu option.

> **NOTE:** If you use special characters (such as the slash /) within your team name, remember that windows does not allow special characters for filenames, So in order for you to be able to pull up the team information file, please use the alias field for the team name. This alias can either be just the team name (without the special characters), or the fully qualified field name with directory and server locations.  
Create your Personal List using CPRS Tool menu

Select the Options option from the Tools drop-down list.

![](shift-handoff-tool-version-1-user-manual/022.png)

From the Lists/Teams tab, click on the Personal Lists… button.

![](shift-handoff-tool-version-1-user-manual/023.png)

![](shift-handoff-tool-version-1-user-manual/024.png)

## H.O.T List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Hot List is a team list that is totally maintained by the users of the Shift Handoff Tool. This list is not connected to any of the CPRS list, patients and provider are added and removed by HOT List manager or users granted access to the list. When patients are discharged they fall off the list. Patients will not be automatically added if admitted.

### Create a H.O.T List (Hand-Off Team)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you hold the manager’s key (CRHD HOT TEAM MGR) you can create HOT list.

From the File drop down menu, select the HOT List Config option

![](shift-handoff-tool-version-1-user-manual/025.png)

Select the Team, click ‘OK’ button, if you are creating a New Team see ‘Creating a New Team List’ below

![](shift-handoff-tool-version-1-user-manual/026.png)

### Creating a New Team List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Type in the new team name, click the ‘OK’ button. You should see the following message screen.

![](shift-handoff-tool-version-1-user-manual/027.png)

![](shift-handoff-tool-version-1-user-manual/028.png)

Click the ‘Yes’ button. You will see ‘Adding new patients and providers to the list.’

### Adding New Patients and Providers to the List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two ways to add patients to the HOT List, from the HOT List Configuration menu option and from the Main Selection window.

Adding patients and providers from the HOT List Configuration Menu:

![](shift-handoff-tool-version-1-user-manual/029.png)

Initially the HOT List Manager will have to grant you access to the List. (See Granting Access to HOT List below).

Select Patient from the left side list and click the ‘Add’ button, this will add the patients name to the list on the right. Once the patients are listed on the right side you can assign an Attending, Resident, Intern, Fellow, Medical Student and a Nurse. Assigning provider to patients is optional.

This information is not used to compose the contact list for providers, medical Students and Nurses. You can get a list of patients assigned to a provider in this section. The providers in this section are not necessarily listed as the providers assigned to the HOT team.

To assign provider to the team select the Provider from the left side list at the bottom half of the screen. Click the ‘Add’ button; this will add the provider to the list on the bottom right list. You can now setup the contact information that will be printed on the team list print out. If you add contact information make sure you hit the ‘Save Changes’ button to save this information. Although contact information is optional assigning a class is recommended because this information is used in ordering providers on the printed document.

#### Granting Access to the HOT List

By adding a check in the checkbox and saving the information grants providers access to add patients and/or providers to the HOT List.

-Modify Patient List – if this is checked the provider can add patients to the team list.  
-Modify Provider List – if this is checked the provider can add other providers to the list.

MAKE SURE YOU CLICK ‘SUBMIT DATA’ BUTTON to save data.

> **NOTE:** This list does not interact with CPRS or any Vista team list, so assigning only means for the use of this tool with the H.O.T list.

Adding patients from the Main Selection Window:

First select the HOT List, (remember you must have access to add patients to the list)

![](shift-handoff-tool-version-1-user-manual/030.png)

Select the Patient option and select a patient from the list by clicking on that patient. You will have the option to Save H.O.T. List, Create a Personal List or use the list as a One Time (temporary) list. By selecting the Save H.O.T. List this actually saves the patient permanently to the list (unless the patient is discharged or someone with the proper access removes them).

![](shift-handoff-tool-version-1-user-manual/031.png)

The following two screen capture shows where the data is displayed.

![](shift-handoff-tool-version-1-user-manual/032.png)

![](shift-handoff-tool-version-1-user-manual/033.png)

# Print A Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the Shift Handoff Tool is to pass vital patient information along to the next shift. One way to do this is to review the information available on the screen. Another way is to print a report of the patient information which can then be physically passed on to the next shift. It is highly recommended that you print the report. Some information is more visible on a printed report. Say you have two providers, one provider is looking at a computer screen and the other provider is looking at a printed report, both providers will absorb different information about the patients under their care.

## Print/Preview Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](shift-handoff-tool-version-1-user-manual/034.png)We suggest that you preview the report before printing it. This is done by selecting PreView Report from the File menu.

A window such as this opens:

![](shift-handoff-tool-version-1-user-manual/035.png)

> **NOTE:** Alterations are made to the printed report if the preference setup uses four (4) temporary fields and the patient has a large amount of Meds. To save print space Med descriptions are limited to 15 characters each.

## Print Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Report Preview window has a button bar to assist you in reviewing the report.

![](shift-handoff-tool-version-1-user-manual/036.png)

#### File Buttons

You can save this report, load a previous report, or print the report. Saved reports have a .NDR extension. These files can only be viewed by using the Shift Handoff Tool application.

#### Navigation Buttons

These are made to look like the buttons on a CD or DVD player. You can go to the first page, the last page, the next page, or the previous page. The window pane to the right of the navigation buttons shows which page you are on and how many total pages there are.

#### Zoom Buttons

These standard zoom icons allow you to zoom in (increase the size) by 10% each click, same for zoom out, then you can zoom to fit the window width or fit the whole page to the window size. The window pane to right of Zoom shows the current zoom percent.

#### Exit Button

The button that looks like a door, provides an alternate way of exiting the report window. You can also select exit from the File menu, click on the X button in the upper right corner, or right click on the title bar icon and select close.

> **NOTE:** In Shift Handoff Tool printouts are limited to 50 pages. When previewing the report you should check to see if this limit has been reached. If it has, it usually means printing has gone into an endless loop. These loops are caused by temporary fields continuing onto the next page. Correct the situation by limiting or cutting down the size of temporary fields that cross page boundaries.

# Shift Handoff Tool at a Glance 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><p>![](shift-handoff-tool-version-1-user-manual/037.png)</p>
<p>1. Start the Shift Handoff Tool from the CPRS Tools drop-down menu. You will need to enter your CPRS signon credentials to log into the application.</p></th>
<th><p>![](shift-handoff-tool-version-1-user-manual/038.png)</p>
<p>2. Select List to print: Double click list or hit Submit button.</p>
<p>Right click patient name in ‘Patient Box’ to delete patient from list.</p>
<p>Personal List only – Right click on selected Personal list to delete a Personal List.</p>
<p>HOT List – if you hold the manager key you are allowed to delete a HOT list.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>![](shift-handoff-tool-version-1-user-manual/039.png)</p>
<p>3. Enter/Edit data.</p>
<p>Yellow boxes: Editable fields. (Note: These fields are controlled by an expiration date.)</p>
<p>White boxes: Uneditable fields, data comes from Vista.</p>
<p>SAVE DATA, by moving from one field to another initiates the save field or hit the SAVE button at top of screen.</p></td>
<td><p>![](shift-handoff-tool-version-1-user-manual/040.png)</p>
<p>4. Print or Preview Report.</p></td>
</tr>
</tbody>
</table>