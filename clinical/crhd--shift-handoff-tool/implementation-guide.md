---
title: Shift Handoff Tool Version 1 Implementation Guide & Technical Manual
doc_type: IG-IMP
doc_label: Implementation Guide
doc_layer: anchor
doc_subject: & Technical Manual
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
description: 
audience: 
keywords: 
  - handoff
  - table
  - shift
  - contents
  - tool
  - crhd
  - team
  - patient
  - files
  - technical
page_count: 0
word_count: 4318
section_count: 16
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Shift_Handoff_Tool/crhdigtm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Shift_Handoff_Tool/crhdigtm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=175"
---

---
title: |
  Shift Handoff Tool

  Implementation Guide

  and

  Technical Manual

  ![](shift-handoff-tool-version-1-implementation-guide-technical-manual/001.png)
---

Clinician Desktop Service

Veterans Health Information Technology

Version 1

October 2018

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date         | Description                                                        | Author                             |
|--------------|--------------------------------------------------------------------|------------------------------------|
| October 2018 | [Setup: New SERVICE/SECTION](#creating-a-new-servicesection-entry) | <span class="mark">REDACTED</span> |
| June 2008    | Initial Release                                                    | <span class="mark">REDACTED</span> |

Table : Contents of SHIFTHANDOFFTOOL.ZIP

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
- [Introduction](#introduction)
- [Installation](#installation)
  - [Server Installation](#server-installation)
  - [Client Installation](#client-installation)
    - [Tools Menu](#tools-menu)
- [Maintenance](#maintenance)
  - [Secondary Menu](#secondary-menu)
  - [Security Keys](#security-keys)
  - [Parameters](#parameters)
- [Setup](#setup)
    - [Shift Handoff Manager](#shift-handoff-manager)
    - [Creating a New SERVICE/SECTION Entry](#creating-a-new-servicesection-entry)
    - [Preference Configuration](#preference-configuration)
  - [Handoff (HOT) Team Manager](#handoff-hot-team-manager)
    - [Create new HOT List](#create-new-hot-list)
    - [Delete HOT List](#delete-hot-list)
    - [Configure HOT List](#configure-hot-list)
- [Exported Items](#exported-items)
  - [Assign Menu to Secondary Menu](#assign-menu-to-secondary-menu)
  - [Security Keys](#security-keys-1)
  - [Files](#files)
    - [Data Dictionaries](#data-dictionaries)
  - [Routines](#routines)
  - [Globals](#globals)
  - [Application Programmer Interfaces](#application-programmer-interfaces)
- [How to Generate On-Line Documentation](#how-to-generate-on-line-documentation)
  - [Routines](#routines-1)
  - [Files](#files-1)
- [External Relationships](#external-relationships)
- [Troubleshooting](#troubleshooting)
This manual covers technical aspects of the Shift Handoff Tool for Information Resource Management Service (IRMS) staff and Clinical Applications Coordinators (CACs). Included are installation, setup, and maintenance instructions as well as complete technical data.
The Shift Handoff Tool is a utility that assists hospital staff going off shift to create a report for the incoming shift. This report contains demographic and medical information about each patient being handed off. At a minimum it shows medications and allergies, but can be customized to show other medical information that is relevant to the patient’s condition.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is both an M (or Server) component and a Windows (or Client) component. All the required files are contained in the distribution zip file: SHIFTHANDOFFTOOL.ZIP

| File                 | Description                                              |
|----------------------|----------------------------------------------------------|
| ShiftHandoffTool.exe | ShiftHandoffTool Executable                              |
| CRHD.HLP             | CRHD Help File                                           |
| CRHDIG.DOC           | Install Guide (Word Version)                             |
| CRHDIG.PDF           | Install Guide                                            |
| CRHDIGTM.DOC         | Implementation Guide and Technical Manual (Word Version) |
| CRHDIGTM.PDF         | Implementation Guide and Technical Manual                |
| CRHDUM.DOC           | User Manual (Word Version)                               |
| CRHDUM.PDF           | User Manual                                              |
| CRHDRN.DOC           | CRHD Release Notes (Word Version)                        |
| CRHDRN.PDF           | CRHD Release Notes                                       |

Table : Content of the CRHD HANDOFF PARAMETERS (#183) file

## Server Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the Shift Handoff Tool Install Guide (CRHDIG.PDF) for complete instructions on installation of the M component.

## Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of the Windows component will vary according to your own local management policies. Basically, it consists of the following steps:

1.  Place the executable, ShiftHandoffTool.exe, and the help file, CRHD.hlp, in the same directory on each workstation or on a network drive accessible from each workstation.
2.  Add Shift Handoff Tool to the Tools menu of CPRS.

In addition, you can also setup the Shift Handoff Tool to run as a standalone application by doing the following to workstations in the hospital area(s) that are going to use this tool:

- Place a shortcut to ShiftHandoffTool.exe on the desktop. The parameters on the command line of this shortcut (S= and P=) must be the same as the parameters in the CPRS shortcut. S=Vista Server P=RPC Broker Port

### Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may set up the tools menu on the User, Location, Service, Division, or System level. The lowest level overrides higher levels.

Select GUI Parameters Option: ?

CS GUI Cover Sheet Display Parameters ...

HS GUI Health Summary Types

TM GUI Tool Menu Items

MP GUI Parameters - Miscellaneous

UC GUI Clear Size & Position Settings for User

RE GUI Report Parameters ...

NV GUI Non-VA Med Statements/Reasons

RM GUI Remove Button Enabled

NON GUI Remove Button Enabled for Non-OR Alerts

EIE GUI Mark Allergy Entered in Error

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select GUI Parameters Option: TM GUI Tool Menu Items

CPRS GUI Tools Menu may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[DEVCUR.FO-SLC.MED.VA.GOV\]

Enter selection: 3 Division INSTITUTION

Select INSTITUTION NAME: salt

1 SALT LAKE CITY UT EES 925

2 SALT LAKE CITY UT NHC 6609AA

3 SALT LAKE CITY UT USAF 660CZ

4 SALT LAKE CITY HCS UT VAMC 660

5 SALT LAKE CITY OIFO UT ISC 5000

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 5 SALT LAKE CITY OIFO UT ISC 5000

------- Setting CPRS GUI Tools Menu for Division: SALT LAKE CITY OIFO -------Select Sequence: 2

Are you adding 2 as a new Sequence? Yes// y YES

Sequence: 2// 2

Name=Command: &Shift Handoff Tool=C:/CPRS/ShiftHandoffTool.exe S=%SVR P=%PORT

Select Sequence:

# Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Secondary Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CRHD SHIFT CHANGE HANDOFF is the secondary menu exported with this application. You cannot run ShiftHandoff.exe from a workstation unless you have this menu option or you have programmer access mode. All users of this application should have this menu assigned to them as a secondary menu or as part of their primary menu tree.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following keys are exported for use with the Shift Handoff Tool:

CRHD SHIFT CHG HANDOFF MGR (This gives access to Preference Page)

CRHD HOT TEAM MGR (This gives access to the configuration Handoff Tool (HOT) list)

## Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following parameters are kept in the CRHD HANDOFF PARAMETERS (#183) file.

| Parameter Name        | Description                                 |
|-----------------------|---------------------------------------------|
| TEMP_FLD_1_TITLE      | Temporary field 1 Title                     |
| TEMP_FLD_2_TITLE      | Temporary field 2 Title                     |
| TEMP_FLD_3_TITLE      | Temporary field 3 Title                     |
| TEMP_FLD_4_TITLE      | Temporary field 4 Title                     |
| TEMP_FLD_COLOR        | Temporary field color                       |
| TEMP_FLD_FONTCOLOR    | Temporary field font color                  |
| STUDENT               | Medical Students and phone                  |
| RESIDENT              | Resident and phone                          |
| PATIENT_DEMOGRAPHICS  | Patient demographics                        |
| PATIENT_DEMO_PRINTLBL | Print patient demographics labels           |
| MED_DETAIL_FLG        | Include Meds details                        |
| MED_EXCLUDE_IV        | Exclude IVs from Med list                   |
| CONSULTS              | Consults request                            |
| LABS_IMAGING          | Labs and Radiology                          |
| PRINT_ORIENTATION     | Portrait/Landscape                          |
| ORDER_BY              | Sort patients by for printed report         |
| MULTI_DNR             | Display multiple active DNR orders if found |
| FILE_Location         | Team Info file location                     |

Table : Contents of the VistA PARAMETER DEFINITION FILE (#8989.51) File

The following parameters are stored in the VistA PARAMETER DEFINITION FILE (#8989.51) file:

| Parameter Name           | Description                        |
|--------------------------|------------------------------------|
| CRHD DEFAULT PREFERENCE  | Default Preference                 |
| CRHD DNR ORDER TITLE     | DNR search strings                 |
| CRHD DNR ORDERABLE ITEMS | DNR search items                   |
| CRHD TEMP FLD EXPIRE     | Temporary field expiration in days |

Table : CRHD Handoff Configuration File Parameters

# Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Managers and Clinical Application Coordinators (CACs) do not need to use VistA to manage team lists and preferences. Holders of the CRHD SHIFT CHG HANDOFF MGR key have access to the Preference Configuration dialog and can enter and manage multiple configurations. Holders of the CRHD HOT TEAM MGR key have access to the Handoff Team (HOT) list management dialog.

An important point is that each list, including HOT lists, has a different setup associated with it. Many aspects of the final printout can be managed separately for each list. The Shift Handoff Manager or CAC for each service should study the options carefully so lists can be configured to the greatest possible advantage.

### Shift Handoff Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Preference Configuration menu command does not appear on the File menu unless the user holds the CRHD SHIFT CHG HANDOFF MGR key.

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/002.png)

Selecting this menu command brings up the selection dialog:

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/003.png)

Preferences can only be named after providers, teams, service, or divisions that already exist in the system. Notice, for example, that all medical centers are listed. These are only used as names for profiles and do not interact with any system external to your local site.

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/004.png)

Notice above that we have five preferences defined, one is name after a local clinic, another is names after a provider, and three of them are named after medical centers. All are simply being used as names of preferences in our local system.

### Creating a New SERVICE/SECTION Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Though VistA is not needed to manage team lists and preferences, it is necessary to use VistA to create a new SERVICE/SECTION.

> **NOTE:** This file requires programmer access (@) to add or edit items. The requestor will need to work with their local/regional systems manager to request the changes.

VistA FileMan may be used to create the new SERVICE/SECTION entry as in the example below.

> VA FileMan 22.2

> Select OPTION: ENTER OR EDIT FILE ENTRIES

> Input to what File: SERVICE/SECTION// (158 entries)

> EDIT WHICH FIELD: ALL//

> Select SERVICE/SECTION NAME: TEST THERAPY

> Are you adding 'TEST THERAPY' as a new SERVICE/SECTION (the 159TH)? No// Y (Yes)

> SERVICE/SECTION MAIL SYMBOL: JSGT

> SERVICE/SECTION PARENT SERVICE: 117

> 1 117 PHYSICAL THERAPY 117

> 2 117 SPEECH THERAPY 117 SPEECH THERAPY

> CHOOSE 1-2: 1 PHYSICAL THERAPY 117

> ABBREVIATION: JSGT

> DESCRIPTION:

> Edit? NO//

> MAIL SYMBOL: JSGT//

> PARENT SERVICE: PHYSICAL THERAPY//

> TYPE OF SERVICE: C PATIENT CARE

> CHIEF: Staff, Chief

> Select CHIEF PHONE:

> ASST CHIEF:

> Select ASST CHIEF PHONE:

> LOCATION:

> MIS COSTING CODE:

> COST CENTER:

> TYPE OF COSTING SECTION:

> AMBULATORY CARE FLAG:

> Select DATE CLOSED:

> NATIONAL SERVICE:

> COORDINATOR (IRM):

> Select SERVICE/SECTION NAME:

Once the new SERVICE/SECTION has been created, login to the Shift Handoff Tool GUI application. Select File/Preference Configuration (or \< Ctrl \> \<Alt\> \< P \>) from the top menu bar.

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/005.png)

Then select the \[ Service \] button. Highlight in the list box the Service you would like to add to the CRHD HANDOFF PARAMETERS NAME file (#183) and double click or select \< Enter \>. Reminder, the service MUST exist in SERVICE/SECTION file (#49) for it to show up in this list.

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/006.png)

The Shift Handoff Preference Configuration window for the Service Name that was selected will be displayed. Select the \[ SUBMIT DATA \] button at the bottom of this window.

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/007.png)

If VistA FileMan is now used to inquire on the CRHD HANDOFF PARAMETERS NAME file (#183), the Service should now be seen.

> VA FileMan 22.2

> Select OPTION: INQUIRE TO FILE ENTRIES

> Output from what File: SERVICE/SECTION// 183 CRHD HANDOFF PARAMETERS (4 entries)

> Select CRHD HANDOFF PARAMETERS NAME: ?

> Answer with CRHD HANDOFF PARAMETERS NAME

> Choose from:

> EDUCATION

> TEST THERAPY

> Select CRHD HANDOFF PARAMETERS NAME: NAME

> Searching for a NEW PERSON, (pointed-to by NAME)

> Searching for a OE/RR LIST, (pointed-to by NAME)

> Searching for a FACILITY TREATING SPECIALTY, (pointed-to by NAME)

> Searching for a TEAM, (pointed-to by NAME)

> Searching for a SERVICE/SECTION, (pointed-to by NAME)

> TEST THERAPY JSGT PHYSICAL THERAPY

> ...OK? Yes// (Yes)

> Another one:

> Standard Captioned Output? Yes// (Yes)

> Include COMPUTED fields: (N/Y/R/B): NO// BOTH Computed Fields and Record Number (IEN)

> NUMBER: 4 NAME (SRV): TEST THERAPY

> NAME: PATIENT_DEMOGRAPHICS VALUE: 2,6,7,8,12,,5

> NAME: PATIENT_DEMO_PRINTLBL VALUE: 0

> NAME: MED_DETAIL_FLG VALUE: 0

> NAME: PRINT_ORIENTATION VALUE: L

> NAME: CONSULTS VALUE: 0

> NAME: LABS_IMAGING VALUE: 0

> NAME: MED_EXCLUDE_IV VALUE: 0

> NAME: ORDER_BY VALUE: 0

> NAME: MULTI_DNR VALUE: 0

> NAME: TEMP_FLD_COLOR VALUE: 65535

> NAME: TEMP_FLD_FONTCOLOR VALUE: 0

> Select CRHD HANDOFF PARAMETERS NAME:

### Preference Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Preference Configuration dialog has seven (7) tabs. They are Patient Demographics, Data Objects, Temporary Fields, Contact List, DNR Order, Print Option, and Team Information. The setting on each of these can be changed using the parameters that are exported with this application. However, all settings can be completely controlled by the Preference Configuration dialog.

#### Patient Demographics

The Patient Demographics tab looks like this:

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/008.png)

Name, Age, Sex, Ward, and Room/Bed are all mandatory and cannot be unchecked. Full SSN and Last 4 SSN refers to what will print out on the report. The full SSN appears on the screen in either case. (We recommend that you select Last 4 SSN because it is more consistent with privacy considerations.) One or the other must be displayed. Displaying the Date of Birth, Attending, Primary Care Prv, Adm Date, Day of Adm, and Adm Dx are all optional.

#### Data Objects

The Data Objects control what data objects display on the screen and are printed on the report. The tab appears as such:

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/009.png)Medications will display and be listed, the only option is whether a summary or detailed medication list is used. IVs can be excluded from the medication list (which, if chosen, excludes all IV medications including antibiotics). The Consults and Labs/Imaging check boxes control whether these lists will be present on the screen or report. Multi DNR orders controls whether just the most recent DNR order appears, or all DNR orders are listed. Show Labels for Patient Demographics, if left unchecked, will not label this information on the printout.

#### Temporary Fields

You can detail up to four additional fields for providers to enter context sensitive information about each patient. In the Patient Data dialog these fields appear with a different background indicating data can be entered. The default color is a deep yellow intended to suggest a Post-it<sup>®</sup> note. This is because none of the information is kept permanently as part of the patient record. The tab looks like this:

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/010.png)

The default is that the title of each field is blank. Blank fields <u>do not</u> appear on the Patient Data dialog, so if you wish to use these temporary fields you must enable them by assigning a name to them (like HPI, etc.)

If you don’t like the bright yellow background, you can select a more preferred background color and font color to use for these fields with the controls in the lower right-hand corner of this tab. You must press both the Select Color and then click on the Submit Data button to make a color change permanent.

In the upper right-hand corner of the tab is a selection box marked Expiration. This is the number of days any information entered in the temp fields is retained. This data is kept in the CRHD TEMPORARY DATA (#183.2) file. The count starts whenever data is entered or modified in one of the temp fields. Once expiration has been reached, the information entered in each temporary field is deleted. The expiration can only be set on the Division level, all lists below Division inherit that value. The intention of this system is to provide a mechanism for the passing of context sensitive information from shift to shift during an incidence of care. Any information that needs to be preserved in the patient record must be entered via CPRS and then signed.

The maximum value of the Expiration field is 7 days. When temporary fields are accessed, the last date edited is checked. If the day plus Expiration is less than the present date, the field is blanked out. This is done on a field by field, patient by patient basis.

Temporary field names are limited to 30 characters.

#### Contact List

The contact list is only used if there is no defined contact list with the team. The recommendation it to make entries at the Division level, that way all lists in the division inherit the contacts. This is an example of a possible division level contact list:

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/011.png)

As with other dialogs for maintaining lists in Shift Handoff Tool, items are deleted by double clicking or by right clicking and selecting delete from the drop-down menu.

#### DNR Order

The DNR Order tab is provided as a way to map local Do Not Resuscitate (DNR) order names. To this point, DNR orders are strictly controlled by the local medical center policy. In some cases, different terminology is used. In other cases, more than one DNR order is present among the orderable items to cover varying situations, such as differentiating between cardiac and pulmonary DNR circumstances. The DNR Order tab looks like this:

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/012.png)

This tab gives you two ways to define DNR orders. The first, in the left hand box, allows you to type in strings and phrases that are typically present in a DNR order. Type the strings or phrases into the text box and press the Enter key. What you type is added to the list. (As with many things in VistA, it is not case sensitive.) You can double click on an item to remove it from the list.

The second, in the remainder of the tab, is to specify specific items from the orderable items file to be included. Type search terms into the text box at the top of the center column. Select orderable items by double clicking on them, or selecting them and hitting the Add key. The list of orderable items with their Internal Entry Numbers (IENs) is built in the right hand frame. To delete items from this list within the right window pane, either double click on the item or select it and then click on the Remove key.

#### Print Option

The Print Option tab allows you to specify preferences for the printout. It allows you to specify Portrait or Landscape orientation of the printing, and it allows you to select the print order, either alphabetically by patient, by room number, or by patient location. The tab looks like this:

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/013.png)

#### Team Information

The Team Information tab specifies a file location to find text information files about the team. These files can be accessed a number of places while running the application. The default location is the directory which the application is executed from. This is usually, but not always, C:\Program Files\Vista\ShiftHandoff\\ When specifying an alternate location be sure to use the backslash character “\\ to separate fields and indicate the end of the address as in this example:

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/014.png)

These files can be created by you and must reside either on the workstation that will be used or on a Windows server accessible from a workstation. The naming convention is the name of the team followed by the .TXT extension. Notepad can be used to initially create these files. You can override the file name with the Assign Providers to Team/List dialog.

> **NOTE:** Back and front slashes (\\ and /), asterisks (\*), and question marks (?), as well as most other punctuation cannot be used as part of file name. Rather than require sites using this feature to change team names, you can use the Assign Providers to Team/List dialog to supply an alias that the system will use as a file name.

Once created, users with the CRHD HOT TEAM MGR key can edit the team information from ShiftHandoffTool.exe. Holders of this key get the following right-click menu:

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/015.png)

> **NOTE:** This file is for team-centric information, not patient information. All users need to be cautioned that no patient, individually identifiable information should be placed in this file.

## Handoff (HOT) Team Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users with the CRHD HOT TEAM MGR key have access to the Handoff Tool (HOT) List creation and management functions. HOT Lists are only maintained within the Shift Handoff application and have no relation to lists maintained in VistA. When this key is present in a user’s account, the File menu command HOT List Configuration becomes active.

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/016.png)

Selecting this command opens the TEAM dialog, that looks like this:

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/017.png)

From this dialog your can do three things:

1.  Create a new HOT List.
2.  Delete a HOT List.
3.  Configure a HOT List (i.e., add patients, delete patients, add provider information connected to a specific patient, add providers, delete providers, add information about each provider on the team.

The only constraint on HOT Lists is that they are for inpatients only. Patients cannot be added to HOT lists unless they have been admitted and a patient will be automatically removed when a discharge action is taken on that patient.

### Create new HOT List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a new HOT List, simply type its name in the text box at the top of the dialog. When you press enter or click the OK button, it asks, “Do you want to Save \_\_\_\_\_ as a New Team?” If you answer yes, it goes on to the next dialog.

### Delete HOT List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To delete a hot list, select it, right click, then select Delete from the drop-down menu. Here is an example:

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/018.png)

### Configure HOT List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here is an example of the HOT List configuration dialog:

![](shift-handoff-tool-version-1-implementation-guide-technical-manual/019.png)

Each HOT List has patients and providers associated with it. The providers can be assigned one of six roles: ATTN, RES, INTERN, FELLOW, MED STUDENT, or NURSE. The office phone and digital pager numbers come from the New Person file and are included on the HOT list. These numbers may be overridden from this dialog (but will not update the New Person file). Also, privileges to modify this list can be granted by checking the appropriate box(s) Modify Patient List or Modify Provider List.

Each patient can have an Attending, Resident, Intern, Fellow, Med Student, and Nurse assigned separately to it. Patients are automatically deleted from the list when a discharge action is taken on them.

> **NOTE:** As with other parts of the Shift Handoff Tool, the information entered into this dialog is not kept in the VistA team files. Thus the assignments of providers is only for the purposes of the HOT list and do not impact team information within CPRS/VistA.

# Exported Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Assign Menu to Secondary Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CRHD SHIFT CHANGE HANDOFF must be assigned to a user to use the Shift Handoff Tool. If a user tries to execute the Shift Handoff Tool GUI (from either the tools menu or from an icon) and they have not been assigned the CRHD SHIFT CHANGE HANDOFF option, the program immediately shuts down.

The recommended placement for the CRHD SHIFT CHANGE HANDOFF option is to set it up as a secondary menu. This option can also be added to a provider’s primary menu.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CRHD SHIFT CHG HANDOFF MGR (Preference setup) (only a few should hold this key, maybe the Clinical Application Coordinator)

CRHD HOT TEAM MGR ( HOT Team manager)

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### CRHD TEMPORARY DATA (#183.2)

This file stores the temporary data entered for each patient. Data fields: Temporary field name, Patient, Author, Date Entered, Last Edit by, Date/Time of Last Edit, Private (not used), Read Only (not used).

#### CRHD HANDOFF PARAMETERS (#183)

Preference configuration parameters are stored in this file. The following files are pointed to files:

| File Number | File Name                     |
|-------------|-------------------------------|
| 200         | USER                          |
| 100.21      | OE/RR TEAM                    |
| 45.7        | TREATING SPECIALTY (Not used) |
| 404.51      | SD TEAM (Not used)            |
| 49          | SERVICE (Not used)            |
| 44          | LOCATION                      |
| 4           | DIVISION                      |

Table : RPC Exported with Shift Handoff Tool

Data fields: Name, Entity Name, Value, List Value

#### CRHD TEAM CONTACT LIST (#183.4)

This file stores contact information for providers assigned to the selected list.

Data fields: Team, Providers, Class, Pager, Office Phone, Filename.

#### CRHD HOT TEAM PATIENT LIST (#183.3)

This file stores a list of patients and providers for the lists created within the Shift Handoff Tool.

Data fields: Team, Inactive (not used), Patients, Attending, Resident, Intern, Fellow, Med Student, Nurse, Providers, Class, Modify Patient List, Modify Provider List, Pager, Office Phone.

### Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The number-space for Shift Handoff Tool files is 183. A listing of these files can be obtained by using the VA FileMan option DILIST (List File Attributes). Depending on the FileMan template used to print the listing, this option will print out all or part of the data dictionary for the Shift Handoff Tool files.

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines are exported with the CRHD build:

CRHD GET THE PATIENT DATA ELEMENTS FOR CHANGEOVER LIST

CRHD1 ADDED TO WORK WITH HAND OFF TEAM SECTION

CRHD10 ASSIGN PROVIDERS TO A TEAM LIST

CRHD11 GET USERS PARAMETERS

CRHD2 GET DATA ITEMS FOR CHANGEOVER LIST

CRHD3

CRHD4 GET USERS PARAMETERS

CRHD5 MISC ROUTINE FOR HAND-OFF TOOL

CRHD6 MISC ROUTINE FOR HAND-OFF TOOL

CRHD7 TEAM ROSTER

CRHD8 RETURNS THE TEXTS OF AND ORDER

CRHD9 HANDOFF TEAM LIST

CRHDAM

CRHDDNR GET ACTIVE DNR ORDER

CRHDDR RETRIEVE DNR ORDERS USING ORDER DIALOG

CRHDPL Find personal lists for changeover list

CRHDUD New Person general information

CRHDUT GET THE PATIENT DATA ELEMENTS FOR HANDOFF LIST

CRHDUT2 GET THE PATIENT DATA ELEMENTS FOR HANDOFF LIST CONTINUED

## Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The shift Handoff Tool creates one global, ^CHRD(.

## Application Programmer Interfaces 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table shows Remote Procedure Calls (RPCs) that are exported with and used by the Shift Handoff Tool along with the corresponding M code entry point:

| Remote Procedure Call       | M Entry Point   |
|-----------------------------|-----------------|
| CRHD ADDITIONAL USER INFO   | AUSRINFO^CRHDUT |
| CRHD ALL USER PARAMETERS    | GETALLP^CRHD4   |
| CRHD AVAILABLE PARAMETERS   | GETALLPL^CRHD11 |
| CRHD COMB TM LIST           | TMCOMB^CRHD10   |
| CRHD DEFAULT PREFERENCE     | DEFPREF^CRHD11  |
| CRHD DELETE A PREFERENCE    | DELPREF^CRHD5   |
| CRHD GET CONSULT            | CONSULT^CRHDUT  |
| CRHD GET DNR TITLES         | GETDNRT^CRHD4   |
| CRHD GET IMAGING            | IMAGING^CRHDUT  |
| CRHD GET LABS               | LABS^CRHDUT     |
| CRHD GET ONE PARAMETER      | GETONEP^CRHD4   |
| CRHD GET ORDERABLE ITEMS    | LORDITM^CRHDDR  |
| CRHD GET PAT LIST           | GETPTLST^CRHD3  |
| CRHD GET PREFERENCES        | GETP^CRHD6      |
| CRHD GET TEAM PHONE NUMBERS | TEAMMEM^CRHD7   |
| CRHD GET TEMP FLD           | GTEMPTXT^CRHD3  |
| CRHD GET USER DIVISIONS     | USERDIV^CRHD5   |
| CRHD GET USER PARAMETERS    | GETIT^CRHD11    |
| CRHD GET XPAR VALUES        | GETPAR2^CRHD6   |
| CRHD HOT CAN EDIT           | CANEDIT^CRHD9   |
| CRHD HOT DELETE PAT/PRV     | DELENTS^CRHD1   |
| CRHD HOT DELETE TEAM LIST   | HOTMDEL^CRHD9   |
| CRHD HOT MODIFY LIST        | MOD^CRHD9       |
| CRHD HOT PATIENT LIST       | HOPLIST^CRHD9   |
| CRHD HOT PATPRV             | PATPRV^CRHD9    |
| CRHD HOT PROVIDER BY CLASS  | HOTMMEMS^CRHD1  |
| CRHD HOT PROVIDER LIST      | HODLIST^CRHD9   |
| CRHD HOT PROVIDER LIST2     | HOTMMEM^CRHD1   |
| CRHD HOT PROVIDER PATIENTS  | HOTPRVPT^CRHD1  |
| CRHD HOT PRV INFO           | PRVINFO^CRHD9   |
| CRHD HOT TEAM LIST          | HOLIST^CRHD9    |
| CRHD HOT TEAM PHONE INFO    | HOTEAM^CRHDUD   |
| CRHD HOT TEAM SAVE          | HOTMSAVE^CRHD9  |
| CRHD HOT TM MGR             | HOTMMGR^CRHD1   |
| CRHD INPT LIST              | LISTINPT^CRHD3  |
| CRHD IS RECORD LOCKED       | LOCK^CRHD2      |
| CRHD LIST DIVISIONS         | DIV^CRHD5       |
| CRHD LIST SERVICES          | SRV^CRHD5       |
| CRHD MGR                    | MGR^CRHD7       |
| CRHD MOD TM PROVIDERS       | TMMOD^CRHD10    |
| CRHD PAT ACTMEDS            | ACTMED^CRHD     |
| CRHD PAT ALLERGIES          | ALG^CRHD        |
| CRHD PAT CODESTS            | CODESTS^CRHD    |
| CRHD PAT DEMO               | PATDEMO^CRHD    |
| CRHD SAVE DNR TITLES        | SAVEP^ CRHD6    |
| CRHD SAVE PARAMETERS        | SAVEPARM^CRHD4  |
| CRHD SAVE TEMP FLD          | TEMPDATA^CRHD2  |
| CRHD SAVE XPAR PARAMETERS   | SAVEP2^CRHD6    |
| CRHD SERVICE INFO           | SRV^CRHDUD      |
| CRHD SORT PRINT LIST        | SORT^CRHD8      |
| CRHD TM PRV INFO            | TMPRVINF^CRHD10 |
| CRHD TM PRV LIST            | TMLIST ^CRHD10  |
| CRHD USER PHONE INFO        | DISPEMP^CRHDUD  |
| CRHD USER PHONE NUMBERS     | USERPHPG^CRHD9  |

# How to Generate On-Line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespace for the Shift Handoff Tool application is CRHD. A listing/printout of any or all of the Shift Handoff Tool routines can be produced by using the Kernel option XUPRROU (List Routines). This option is found on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option. When prompted with “routine(s) ? \>:” type in CRHD\* to get a listing of all Shift Handoff Tool routines.

The first line of each routine contains a brief description of the general function of the routine. A listing of just the first line of each Shift Handoff Tool routine can be produced by using the Kernel option XU FIRST LINE PRINT (First Line Routine Print). This option is found on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The number-space for Shift Handoff Tool files is 183. A listing of these files can be obtained by using the VA FileMan option DILIST (List File Attributes). Depending on the FileMan template used to print the listing, this option will print out all or part of the data dictionary for the Shift Handoff Tool files.

# External Relationships 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are DBIAs (Data Base Integration Agreements) covering the following procedure calls:

ORQPT DEFAULT LIST SORT DEFSORT^ ORQPTQ11

ORQPT DEFAULT LIST SOURCE DEFSRC^ORQPTQ11

ORQPT PROVIDER PATIENTS PROVPTS^ORQPTQ2

ORQPT SPECIALTIES SPEC^ORQPTQ2

ORQPT SPECIALTY PATIENTS SPECPTS^ORQPTQ2

ORQPT TEAM PATIENTS TEAMPTS^ORQPTQ1

ORQPT TEAMS TEAMS^ORQPTQ1

ORQPT WARDS WARD^ORQPTQ2

ORWPT BYWARD BYWARD^ORWPT

ORWPT LAST5 LAST5^ORWPT

ORWPT FULLSSN FULLSSN^ORWPT

ORWPT LIST ALL LISTALL^ORWPT

ORWTPP DELLIST DELLIST^ORWTPP

ORWTPP NEWLIST NEWLIST^ORWTPP

ORWTPP PLISTS PLISTS^ORWTPP

ORWTPP SAVELIST SAVELIST^ORWTPP

ORWU NEWPERS NEWPERS^ORWU

ORWU USERINFO USERINFO^ORWU

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Question: A user tries to run Shift Handoff Tool, either from the Tools menu or from the icon, and the splash screen just appears for half a second and then it is gone. This user cannot run the application. What is wrong?

Answer: Make sure the user has the CRHD SHIFT CHANGE HANDOFF menu option assigned to them.

Question: We used to use the CAIRO shift handoff software and some of our providers prefer it. However, when members of the same team look at the new Shift Handoff Tool it appears as though data is missing. What’s going on?

Answer: CAIRO and the Shift Handoff Tool use different files. On installation data is copied from the old CAIRO files into the new Shift Handoff Tool files so that operations can proceed seamlessly. However, the two applications do not talk to one another. All providers must use the new Shift Handoff Tool executable in order for the new software to work properly.

Question: Our printed reports go on forever, repeating the same data on the last pages. What’s going on and how can we fix it?

Answer: This is a known bug. Before printing, review the report with the print preview menu option. If a repeat is found in the output causing the printout to loop endlessly, several things can be done:

- Find the patient where the looping starts and reduce the amount of information in the temporary fields. This will change the formatting of the output and may solve the problem.
- Go back to the Preference Configuration, Print Option tab and change the Page Orientation from Landscape to Portrait.
- Go back to the Preference Configuration, Data Objects tab and change the Med Detail to Med Summary.
- Go back to the Preference Configuration, Data Objects tab and select Exclude IVs