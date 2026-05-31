---
title: GMRV*5*3 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: GMRV
app_name: Vitals/Measurements
section: CLI
app_status: active
pkg_ns: GMRV
patch_ver: 5
patch_id: GMRV*5*3
group_key: GMRV:GMRV:5
file_numbers: []
security_keys: []
menu_options: 0
description: '- Vitals/Measurements Release Notes - Concurrence to Release Software with Known Defects...'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 2506
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: April 2006
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Clinical/Vitals_Measurements/vitl5_p3_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Vitals_Measurements/vitl5_p3_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=107
audit_applied: '2026-05-31'
master_source: GMRV*5*3 Release Notes
master_pub_date: April 2006
consolidated_from: 3 versions
prior_versions:
- GMRV*5*22 Release Notes
- GMRV*5*23 Release Notes
consolidated_title: release notes
---

![](gmrv-5-3-release-notes/001.png)

VITALS / MEASUREMENTSRELEASE NOTES

Patch GMRV\*5.0\*3

April 2006

Health Systems Design & Development

Provider Systems

# Vitals/Measurements Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Vitals/Measurements Release Notes](#vitalsmeasurements-release-notes)
  - [Concurrence to Release Software with Known Defects](#concurrence-to-release-software-with-known-defects)
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
This release has been checked for 508 compliance as a component of CPRS. The entire application is scheduled for a compliance review in the near future. Any compliance issues found during the review will be corrected by a patch after the review.
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
This patch provides the following functionality changes:
1.  This patch provides a Dynamic Link Library (DLL) file that will be called from CPRS v26. This DLL provides a Graphical User Interface (GUI) called Vitals Lite; Vitals Lite replaces the CPRS functionality for entering and displaying patient vitals data, and adds new vitals-related functionality for the CPRS user.
> When the user clicks on the vitals portion of the CPRS Coversheet, the Vitals Lite window opens. The user will be able to:
- View patient vitals data in a graph and grid format.
- Select date ranges for retrieving data
- Select vital types to plot on the graph
- Select Intake and Output (I&O) values to plot on the graph (liquid values only)
- Use zoom features to view the graph data
- Display the numerical values on the graph
- Display the graph in 3-d format
- Print a graph to a Windows-type printer
- View the qualifier abbreviations along with the numerical values in the grid (new)
- View the name of the person who entered the data and the hospital location associated with the record in the grid, except for I&O values (new)
- Change the background color of the graph (new)
- Enter vitals data using locally-configured input templates (new)
- Mark existing records as entered-in-error (new)
- Display patient allergy data (new)
> For CPRS users who have access to the Encounter button, the Enter Vitals window can also be opened from the Notes tab. On the Notes tab, the user clicks on the "Encounter" button to select or create an encounter, then the "Vitals" tab on the encounter form, and the "Enter Vitals" button to invoke the DLL. The user will be able to enter vitals data using existing input templates.
> If CPRS v26 is not installed, this DLL will merely reside on the system. It will not adversely affect CPRS v25. This DLL is not called by the Vitals.exe or VitalsManager.exe files that make up the Vitals Graphical User Interface (GUI).
2.  This patch makes the existing Vitals GUI (Vitals.exe) compliant with the Clinical Context Object Workgroup (CCOW) standard. When the Vitals GUI is invoked, by default, it is CCOW-enabled.
> It checks to see what other GUIs are currently running on the user's workstation. It sends current user and patient information to the CCOW "vault" which coordinates user and patient information for the GUIs that are running. If another CCOW-enabled application is running when the Vitals GUI is invoked, the Vitals GUI will open automatically without the need for a second sign-on. If a patient is already selected in the open GUI, the Vitals GUI will open with the patient being used by the open application.
> <u>NOTE:</u> CCOW may not work properly if you use VPN to access the VA network remotely. This is a known issue: if you receive an error message when you  use CCOW-compliant applications via VPN, the current workaround is to disable the context. If you are using multiple VistA applications while CCOW is disabled, please be sure to verify the active patient when switching applications.
1.  Users can completely disable the CCOW functionality at start up time by adding a parameter setting to the shortcut used to invoke the Vitals GUI. This will force the user to sign on and select a patient when invoking the Vitals GUI.  
    To disable CCOW functionality:
    - Right click on the Vitals icon on your desktop
    - Select the Properties option
    - Select the Shortcut tab
    - Go to the Target textbox
    - Add a space to the end of the text followed by "/NOCCOW" without the quotes
    - Click Apply, and then click OK.
> Example of Target textbox:
> "C:\Program Files\vista\Vitals\Vitals.exe" /NOCCOW
2.  Users can disable the automatic sign on, but allow the automatic selection of a patient by adding a different parameter setting to the shortcut used to invoke the Vitals GUI. This will force the user to sign on. If a patient is already selected in an open GUI, the Vitals GUI will open automatically with the patient being used by that open application.
> To disable the automatic sign on, but keep the automatic patient selection:
- Right click on the Vitals icon on your desktop
- Select the Properties option
- Select the Shortcut tab
- Go to the Target textbox
- Add a space to the end of the text followed by "CCOW=PATIENTONLY" without the quotes
- Click Apply, and then click OK.
> Example of Target textbox:
> "C:\Program Files\vista\Vitals\Vitals.exe" /CCOW=PATIENTONLY
3.  This patch provides a new Application Programming Interface (API) for use by the Health Summary (HS) package. This new API returns non-numeric values (e.g., Refused) for display in the HS ad hoc reports. HS patch GMTS\*2.7\*78 must also be installed for the non-numeric values to appear in the HS ad hoc reports.
4.  The following changes have been made to the Vitals GUI main screen:
1.  Updates have been made to increase compatibility with assistive technology. Keyboard shortcuts and navigation options are added to make the GUI accessible to a wider range of users, including those who have limited dexterity, low vision, or other disabilities.
2.  Patient identification information is now displayed in the title bar.
3.  The patient identification button in the navigation bar is now accessible by using the \<Tab\> key. Pressing the \<Enter\> or \<Return\> key while this button is active will open the Patient Inquiry report window.
4.  New options are available in the FILE menu:
    - Patient Inquiry – This option allows the user to view patient demographic information in a separate report window.
    - Data Grid Report – This option allows the user to view the information from the data grid in a text-based report format.
    - Rejoin Clinical Link – This option allows the user to join the CCOW context, using one of the following two options. If you want the other open applications to synchronize with the current patient in the active application, select "Use this Application's Data." If you want the current application to synchronize with the patient that is open in another application, select "Use Global Data."
    - Break the Clinical Link – This option allows the user to break the CCOW context and use any patient regardless of the patient selected in the CCOW application.
    - Show Status – This option allows the user to view information on CCOW, such as whether or not the Contextor software has been installed, and whether the application is participating in a clinical context.
    - Show/Hide Graph Options – This option toggles between showing and hiding graph functions.
    - Select Graph Color – This option allows the user to change the background color of the data graph.
    - Print Graph – This option allows the user to print the graph to a Windows-type printer.
5.  The patient selection buttons for "Ward", "Unit", "Team", "Clinic" and "All" are changed from radio buttons to ordinary buttons.
6.  An "Input Vitals for the Selected Patients" button is added to the bottom of the patient selector pane in the main Vitals window. When the user selects more than one patient at a time, this button must be clicked to enter vitals data for those patients. If only one patient is selected, only the "Enter Vitals" button will be available.
7.  New icons are added to the graph display to allow zooming functionality. A text box allows the user to select the percentage of change when zooming. The default is 10.
8.  The data grid shows the name of the person who entered the data and the hospital location associated with the record, except for I&O values.
9.  New graphs are available:
    - CVP for Central Venous Pressure
    - BMI for Body Mass Index
    - B/P–Weight for Blood Pressure and Weight
    - Intake for intake amounts recorded in the GEN. MED. REC. - I/O package
    - Output for output amounts recorded in the GEN. MED. REC. - I/O package
      Note: I/O values reflect liquid values only.
5.  The following changes have been made to the Vitals data input screen:
1.  Patient identification information is now displayed in the title bar.
2.  The patient identification button in the navigation bar is now accessible by using the \<Tab\> key. Pressing the \<Enter\> or \<Return\> key while this button is active will open the Patient Inquiry report window.
3.  "Enable U" and "Enable R" buttons are added to allow the user to enable/disable the Unavailable and Refused checkboxes on the vitals input template.
4.  The "Save And Exit" button allows the user to save the record and exit the input template with one click.
6.  Changes to the Hospital Location screen allow the selection of a location:
1.  associated with an Appointment
2.  associated with an Admission
3.  by Location Name.
7.  The following command line parameters are no longer supported:
1.  /brokertimeout
2.  /nonsharedbroker
> If these command line parameters are used in a shortcut, they will be ignored by Vitals.

## Concurrence to Release Software with Known Defects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Concurrence was obtained to release this patch with the following known defects:

1.Patch/Project Name: GMRV\*5.0\*3

2.Description of Waiver Request: This patch has been tested in production accounts since late August 2005. The latest test version, T19, was sent to the test sites on March 21, 2006. The goal was to make T19 the final version. Since then, several minor problems have been discovered. To fix these problems requires a new test version along with an extra week of testing. This patch is required by CPRS v26. This patch should be installed about one week before CPRS v26 so that sites can have adequate time to place the Dynamic Link Library (DLL) file that comes with this patch to the necessary servers and workstations where CPRS v26 will look for it. CPRS v26 is slated for release on May 5, 2006. Therefore, we wish to release T19 as is and we will fix these defects in a future patch.

3.Project Team Point of Contact Information: Frank Traxler

4.List of outstanding Issues: Frank Traxler

1.  Problem Reporting System Number: CQ 11263
    1.  Problem Reporting System Description: The "Data Grid Report" displays only the values that are visible in the data grid on the screen. If the selected date range includes twenty columns of data, but only six columns appear on the screen, then only the data from the visible six columns appear in the "Data Grid Report" screen.
    2.  Impact: There is little or no impact to users who are not visually impaired which is the major number of users of the software. There is an impact to visually impaired users who may not realize that only a subset of records from the data grid are displayed in the "Data Grid Report" screen.
    3.  Workaround: The user can change the focus of the data grid to highlight other records and rerun the "Data Grid Report" to display other subsets of the data.
    4.  Comments: The workaround is possible, but not intuitive to a visually impaired user. Some additional thought and input is needed especially from visually impaired users to improve this feature. Rather than create a hasty solution or delay the release of the patch, we would like to gather further input and solutions and fix the problem in the next GUI-related patch.
2.  Problem Reporting System Number: CQ 11175
    1.  Problem Reporting System Description: When there are too many qualifiers in a data grid cell, you cannot always see the rightmost text in the cell and the cell cannot be expanded.
    2.  Impact: Vital types that allow three or four qualifiers are mostly affected by this problem.
    3.  Workaround: Users can click on the vital type name above the data graph to open another screen which displays all of the qualifiers information for the records in the data grid.
    4.  Comments: We will research possible solutions such as making the data cells wider or scrollable.
3.  Problem Reporting System Number: CQ 11373
    1.  Problem Reporting System Description: When entering a Pulse Oximetry value in Vitals User and Vitals Lite, the user can enter a flow rate and concentration percentage value with a qualifier of "Room Air". The "Room Air" qualifier implies that the patient was not receiving oxygen so there should not be a flow rate or concentration percentage value entered. There are software checks to prevent this from happening, but there is one way around those checks. Select "Room Air" first, click the OK button, go back into the drop down list and enter a flow rate or concentration percent value, and do not touch the textbox with the "Room Air" qualifier.
    2.  Impact: The impact is a user may wonder why there is a flow rate or oxygen concentration when the patient is on "Room Air".
    3.  Workaround: If the user re-selects "Room Air" before saving the record, the flow rate and oxygen concentration values are removed.
    4.  Comments: We will fix this in the next patch.
4.  Problem Reporting System Number: CQ 11231
    1.  Problem Reporting System Description: When editing qualifiers in Vitals User's "Edit User Templates" option, an access violation and list out of bounds error can occur. To create the problem select a vital type that has qualifiers, make some changes, save the changes, change the qualifiers without re-selecting the vital type and save the change. This generates an access violation and/or list out of bounds error.
    2.  Impact: The user has to close the template editor screen and re-open to do any further editing. The impact should be small. Input templates are not created or edited very often. In some facilities, the creation and editing of templates is limited to Clinical Applications Coordinators (CACs) only.
    3.  Workaround: The workaround is to close the screen and re-enter it.
    4.  Comments: This can be fixed in the next patch.
5.  Problem Reporting System Number: None
    1.  Problem Reporting System Description: When the Vitals User interface is run, "All Results" are selected for the date range and the "Data Grid Report" is run, an extra line may appear in the report display. That extra line contains a date and time, but no vitals signs data after it. The date and time value is erroneous. There is no data for the patient with this date and time.
    2.  Impact: This may be confusing to the user who will wonder why there are no values following the date/time.
    3.  Workaround: This happens when the date range is "All Results". The date range default is 7 days for an inpatient and 6 months for an outpatient. Users can use the defaults. A user may want to see all data for a patient, but will mostly want to see only recent values.
    4.  Comments: We will fix this in the next patch when we fix issue 4.1.
6.  Problem Reporting System Number: CQ 11374
    1.  Problem Reporting System Description: The "Print Qualifiers Table" report in the Vitals Manager module will error out if the user selects a printer that does not allow queuing. The option should not allow the user to select printers that do not allow queuing of the output.
    2.  Impact: The impact is very low. The Vitals Manager module is limited to a very small number of users such as Clinical Application Coordinators (CACs) and Information Resource Management Services (IRMS) users. This report is not a regular or commonly printed report.
    3.  Workaround: The workaround is to select a printer that does allow queuing of output.
    4.  Comments: We will fix this in the next patch.
7.  Problem Reporting System Number: CQ 11387
    1.  Problem Reporting System Description: The slider bar above the data grid can be used to traverse grid. Moving the pointer on the slider bar to the right will display more recent records in the grid. Moving the pointer to the left, will display older records. At times, the pointer on the slider bar is on the far left end of the slider even though there are older records in the grid. The user must drag the pointer to the right to see those older records. This is counter to how the slider bar should work.
    2.  Impact: The impact is low. The problem does not always occur.
    3.  Workaround: The user can still drag the pointer to traverse the data in the grid.
    4.  Comments: We will fix this in the next patch.
3.  Justification of Request: These issues were discovered after the final version of the patch was made. We feel the defects are minor and have little impact on the users or the quality of the data. Therefore, these defects should not delay the release of the patch. This patch is required for CPRS v26 which is also near to release. Any delay in the GMRV\*5.0\*3 patch may impact the release of CPRS v26.
6. Plan for Addressing Known Defects: We feel these defects can be addressed in the next patch that modifies the Vitals Graphical User Interfaces.