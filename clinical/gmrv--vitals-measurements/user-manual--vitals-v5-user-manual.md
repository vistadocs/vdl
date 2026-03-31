---
title: Vitals Version 5 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: GMRV
app_name: Vitals/Measurements
section: CLI
app_status: active
pkg_ns: GMRV
patch_ver: 5
patch_id: GMRV*5
group_key: "GMRV:GMRV:5"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - vitals
  - class
  - patient
  - button
  - template
  - table
  - graph
  - vital
  - figure
  - even
page_count: 0
word_count: 18499
section_count: 28
table_count: 0
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: October 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vitals_Measurements/vitl5_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vitals_Measurements/vitl5_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=107"
---

![](vitals-version-5-user-manual/001.png)

Vitals / MeasurementsUser Manual

October 2002

GMRV\*5.0\*23

Office of Information & Technology

Office of Enterprise Development

#### Revision History

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 56%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Revision</td>
<td>Description</td>
<td>Author</td>
</tr>
<tr class="even">
<td><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>September 2009</td>
<td>5.23</td>
<td><p>Sections updated for Patch 23 (GMRV*5.0*23):</p>
<p>- updated Title Page</p>
<p>- updated Revision History</p>
<p>- updated Table of Contents</p>
<p>- updated Introduction, page 1-2 and 1-4</p>
<p>- updated Using Vitals Manager, pages 2-<a href="#_Ref118625129">2</a>, 2-3, 2-4, 2-5, 2-7, 2-8, and 2-9</p>
<p>- updated Using Vitals, pages 3-3, and 3-4</p>
<p>- updated Entering Vitals Data, pages 4-3, 4-4, 4-6, 4-7, 4-10, 4-12, 4-14, 4-15, 4-16, and 4-21</p>
<p>- added “Enter Vitals Menu Bar” section, page 4-8.</p>
<p>- updated Reports, pages 5-2, 5-3, 5-4</p>
<p>- updated Appendix A – Access Key Listing, pages 6-2</p>
<p>- updated Appendix C – Using Vitals in CPRS, pages 8-5, 8-6, and 8-7</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>April 2006</td>
<td>5.3</td>
<td><p>Sections updated for Patch 3 (GMRV*5.0*3):</p>
<p>- updated Title Page</p>
<p>- updated Revision History</p>
<p>- updated Table of Contents, all pages</p>
<p>- updated Introduction, page 1-<a href="#_Ref118625018">1</a>, 1-2</p>
<p>- removed Implementation and Maintenance chapter</p>
<p>- updated Using Vitals Manager, pages 2-<a href="#_Ref118625129">2</a>, 2-5, 2-<a href="#_Ref118625402">6</a></p>
<p>- removed Package Operation chapter; replaced with new Using Vitals chapter, updated all pages</p>
<p>- updated Entering Vitals Data, all pages</p>
<p>- updated Reports, all pages</p>
<p>- updated Appendix A, all pages</p>
<p>- updated Appendix B, page 7-3, 7-4</p>
<p>- added Appendix C – Using Vitals in CPRS v26</p>
<p>- updated Glossary, all pages</p>
<p>- updated Index, all pages</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>October 2003</td>
<td>5.1</td>
<td><p>Sections updated for Patch 1 (GMRV*5.0*1):</p>
<p>Revision History</p>
<p>Table of Contents</p>
<p>Site Files</p>
<p>Entering Vitals Data</p>
<p>Reports</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>January 2002</td>
<td>5.0</td>
<td>Initial Publication</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch GMRV*5.0*23 September 2009 Patch 23 release added.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

*This page intentionally left blank for double-side printing.*

######### Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [[^2]Functionality](#2functionality)
  - [Information on GUI software](#information-on-gui-software)
  - [> [^4]Accessibility Features in Vitals 5.0](#4accessibility-features-in-vitals-50)
  - [Adding Vitals to the Tools Menu in CPRS](#adding-vitals-to-the-tools-menu-in-cprs)
- [[^6]Using Vitals Manager](#6using-vitals-manager)
  - [Getting Started with Vitals Manager](#getting-started-with-vitals-manager)
  - [[^7]Managing Vitals Categories and Qualifiers](#7managing-vitals-categories-and-qualifiers)
  - [Printing a Qualifiers Table](#printing-a-qualifiers-table)
  - [Editing Abnormal Values](#editing-abnormal-values)
  - [Editing System Parameters](#editing-system-parameters)
  - [Creating/Editing a Template](#creatingediting-a-template)
- [[^18]Using Vitals](#18using-vitals)
  - [Getting Started with Vitals](#getting-started-with-vitals)
  - [Overview of the Vitals window](#overview-of-the-vitals-window)
  - [Editing User Options](#editing-user-options)
  - [About CCOW](#about-ccow)
    - [Joining a Clinical Context](#joining-a-clinical-context)
    - [Breaking the Clinical Link](#breaking-the-clinical-link)
    - [Showing status](#showing-status)
- [Entering Vitals Data](#entering-vitals-data)
  - [Selecting a Patient and a Template](#selecting-a-patient-and-a-template)
  - [[^24]Entering Data for a Single Patient](#24entering-data-for-a-single-patient)
    - [[^30]Enter Vitals Menu Bar](#30enter-vitals-menu-bar)
  - [[^31]Entering Data for Multiple Patients](#31entering-data-for-multiple-patients)
  - [Creating a User Template](#creating-a-user-template)
  - [Viewing Allergies](#viewing-allergies)
  - [[^38]Marking Vitals as Entered in Error](#38marking-vitals-as-entered-in-error)
- [Reports](#reports)
  - [[^41]Viewing a Graphic Report](#41viewing-a-graphic-report)
  - [[^42]Printing a Report](#42printing-a-report)
- [[^46]Appendix A – Access Key Listing](#46appendix-a-access-key-listing)
- [Appendix B – Customizing the Client Installation](#appendix-b-customizing-the-client-installation)
- [[^48]Appendix C – Using Vitals in CPRS](#48appendix-c-using-vitals-in-cprs)
  - [Overview of Vitals Lite](#overview-of-vitals-lite)
  - [Opening the Vitals Lite window in CPRS](#opening-the-vitals-lite-window-in-cprs)
  - [Viewing Data in Vitals Lite](#viewing-data-in-vitals-lite)
  - [Entering Vitals in Vitals Lite](#entering-vitals-in-vitals-lite)
  - [Correcting Vitals in CPRS](#correcting-vitals-in-cprs)
- [Glossary](#glossary)
- [# Index](#index)
The Vitals/Measurements application is designed to store in the patient's electronic medical record all vital signs and various measurements associated with a patient's hospital stay or outpatient clinic visit. Data entered can be accessed by several VistA (Veterans Health Information Systems and Technology Architecture) applications (e.g., CPRS, Health Summary) that interface with the Vitals/Measurements application.
[^1]The Vitals application is composed of two modules: Vitals and Vitals Manager. Each module is accessed separately through GUI executable icons on the user’s desktop. The Vitals module is used to enter patient data, and is assigned to clinical staff. The Vitals Manager module is used to manage the Vitals templates and abnormal values ranges, and is assigned to the Clinical Application Coordinator, package coordinator, and Information Resource Management Service (IRMS) staff.
A Dynamic Link Library (DLL) file is also provided to allow other applications to use the Vitals/Measurements GUI. See Appendix C for more information on the DLL.
GMV MANAGER is the only security key in this application. This key controls access to the Vitals Manager module. This key also allows a user to view/create/edit all other user’s templates in the Vitals Manager module; without this key the user can only view, create, or edit their own user templates. This key should be assigned to the package coordinator.

## [^2]Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

• Provides a GUI (Graphical User Interface) to make collecting and viewing of data easier. Additional information on GUI software is contained at the end of this chapter.

> • Supports documentation of a patient's vital signs (e.g., temperature, pulse, and respiration), and tracks a patient's height, weight, central venous pressure (CVP), circumference/girth and oxygen saturation via oximetry with supplemental oxygen information. Also supports documentation of detailed or positional blood pressures for a patient (for example, bilateral blood pressures taken in a sitting position).

> • Displays latest information on all of the patient's vitals/measurements in both metric equivalents and U.S. customary units (when appropriate) along with the date/time the information was obtained, and the name of the user who entered the information.

> • Allows facilities to establish hospital-wide high and low values for most vital signs and measurements. Identifies abnormal values, those values outside the high and low range, on vitals/measurements reports.

> • Allows users to record a reason for the omission of a patient's vitals/measurements (such as Patient on Pass).

> • Associates qualifiers (alpha characters appended to the measurement's numeric value) to provide a more detailed description of the patient's vitals/measurements.

> • Contains online help windows to assist users. Online help is accessed through the Help menu at the top of the screen, or by pressing the F1 key on the keyboard.

> • Displays graphic reports on workstation monitors, and provides a variety of printable reports. Reports can be printed for an individual patient or for multiple patients.

> • [^3]Provides APIs that pass patient vitals/measurements information within a specific date range to the other VistA applications.

> • Provides compliance with the Clinical Context Object Workgroup (CCOW) standard. The CCOW standard provides a way for applications to know which other applications are currently running, and which patients are selected in those applications.

> • Supports an interface to vital signs monitor connected to the workstation.

## Information on GUI software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## > [^4]Accessibility Features in Vitals 5.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Keyboard shortcuts and navigation options have been added to make the GUI accessible to a wider range of users, including those who have limited dexterity, low vision, or other disabilities. See Appendix A for a complete listing of access keys and shortcuts.

> Intranet WWW Documentation

Documentation for this product (including user manual, technical manual and package security guide, release notes, and installation guide) is available on the VA intranet at the following address: <span class="mark">REDACTED</span>

GUI and Windows

GUI stands for Graphical User Interface, most frequently seen as the Windows screen. If you have already used programs with these screens, then the Vitals GUI screen will seem familiar to you. The Vitals GUI is only implemented on the Windows platform at this time.

If you have little or no familiarity with Windows, you can browse through the Windows help file for information about the basics of using Windows. Also, see the next few paragraphs for brief descriptions of some GUI features.

> To access the Windows Help File, click the Start button in the taskbar and click Help. Use this help file as a reference whenever you have general questions about Windows.

> The following is an example of the control elements found in a GUI screen:

![](vitals-version-5-user-manual/002.png)

Figure ‑

Windows

An “application window” is the area on your computer screen used by a program. If you have more than one program running at the same time, you can go from one program to another by clicking in each application window. The currently active window contains a colored bar (usually blue) at the top of the window. An inactive window contains a gray bar at the top of the window. You can also move, close, or minimize the application window to make room for another window. (See Help in Windows for further instructions on these functions.)

Inactive window Active window

> ![](vitals-version-5-user-manual/003.png)

[^5]Figure ‑

Pop-up Windows

These are “mini” windows that pop up within a window to provide or request information. Usually they require some action before they will go away. Clicking on buttons with the words Cancel, Exit, or something similar closes these windows.

Menus

Menus are shown in the gray bar near the top of the window. Some examples of menus are: File, Edit, Reports, and Help — typical menus for most Windows applications. When you click on one of these, a list of options is displayed.

> Help

> Online help and documentation are available in several formats: hints, context-sensitive help, menu help, and Internet Web documentation.

> Hints

> Place the cursor over a specific button and a pop-up box will appear containing a short description of that button.

> Context-Sensitive Help

> Use the “F1” key at any time to obtain help on the current screen.

> Menu Help

> Select the Help Menu at the top of the screen. A Table of Contents opens. Choose one of the contents, or type in a topic you want help on. A screen appears containing help about that subject.

> Access Keys

> Use access keys to quickly get to an option through the pull-down menus by holding down the Alt key and pressing the underlined letter of the desired pull-down menu, then (still holding down the Alt key) press the underlined letter of the desired option. Some other screen components (e.g., buttons such as OK) can also be reached by holding down the Alt key and pressing the underlined letter for that screen component. Some buttons and icons can be invoked by holding down the Ctrl key and pressing a letter key. A few can be invoked by pressing a function key (e.g., F5). See Appendix A for a full list of access keys.

> Tool Bars

> Tool bars are shown in the gray bar below the Menu bar. The tool bar contains icons (with or without text) that invoke functionality when clicked on using the mouse. For example, the printer icon opens a dialog box allowing the user to select a printer.

> Trees

> Trees are lists that the user can expand or collapse in order to navigate to needed information. The plus sign (+) to the left of a tree item indicates that tree item contains additional entries. Clicking on the plus sign will expand the tree list to display those additional entries. A minus sign (-) will appear to the left of the tree list instead of a plus sign after that item is clicked. Clicking on the minus sign will collapse the list to hide the items again.

## Adding Vitals to the Tools Menu in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A site may use the Tools menu to give users access to other client software from within CPRS. The parameter, ORWT TOOLS MENU, is used to set up the list of software that appears on the menu. This parameter may be set up for the site, then overridden as appropriate at the division, service, and user levels.

Each item entered on the menu should have the form, NAME=COMMAND. NAME is the name you want the user to see on the menu. An ampersand may be used in front of a letter to allow keyboard access to the menu item. The COMMAND may be a line that can be executed by Windows. It may also be any file for which Windows has a file association.

Example: Create a User tools menu that contains Vitals and Vitals Manager.

Select General Parameter Tools Option: ep Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: orwt TOOLS MENU CPRS GUI Tools MenuORWT TOOLS MENU may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[REGION 5\]

4 System SYS \[OEC.ISC-SLC.VA.GOV\]

Enter selection: 1 User NEW PERSON

Select NEW PERSON NAME: VITUSER, THREE CT

-------------- Setting ORWT TOOLS MENU for User: VITUSER, THREE --------------

Select Sequence: 1

Are you adding 1 as a new Sequence? Yes// YES

Sequence: 1// 1

Name=Command: Vitals=\<directory_name\>”\Vitals.exe” /p=%PORT /s=%SRV /cprs /dfn=%DFN

Select Sequence: 2

Are you adding 2 as a new Sequence? Yes// YES

Sequence: 2// 2

Name=Command: Vitals Manager=\<directory_name\>”\VitalsManager.exe” /p=%PORT /s=%SRV /cprs /dfn=%DFN

Select Sequence:

Note the quotation marks in the Vitals and Vitals Manager examples. A path that contains space characters (like C:\Program Files\\..) must be surrounded by quotation marks. Entries on the command line may also contain parameters.

It is possible to pass context-sensitive parameters. These are parameters that are entered as placeholders, and then converted to the appropriate values at runtime. These placeholder parameters are:

%SRV = Server name for the current broker connection.

%PORT = Port number for the current broker connection.

%MREF = M code giving the global reference where the patient DFN is stored.

%DFN = The actual DFN of the currently selected patient.

%DUZ = Internal entry number of the current user.

So, if you have another application that needs to know, for example, the identity of the current user and currently selected patient, you could list %DUZ and %DFN as parameters in the command that executes that program.

When the user clicks “Vitals” from the Tools menu, Vitals will be called and the actual server, port, and global reference will be substituted as command line parameters.

# [^6]Using Vitals Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals Manager allows a site’s administrator (CAC, IRMS) to define the way that vitals appear in the Vitals/Measurements application. This includes activities such as creating and editing templates, associating qualifiers with different vital types, setting normal/abnormal value ranges for each vital type, and printing a list of qualifiers and their associated categories and vital types.

The Vitals Manager module is used to maintain the site files and settings necessary for a site to operate the software, and the Vitals (user) module is used to collect, store and display patient data. All the options discussed in this chapter are contained in the Vitals Manager module.This chapter shows you how to:

1\. [Start the Vitals Manager module](#getting-started-with-vitals-manager)

2\. [Manage Vitals Categories and Qualifiers](#_Managing_Vitals_Categories_and Qual)

3\. [Print a qualifiers table](#printing-a-qualifiers-table)

4\. [Edit abnormal values](#editing-abnormal-values)

5\. [Create/edit a template](#creatingediting-a-template)

## Getting Started with Vitals Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you double click on the Vitals Manager icon, enter your access and verify codes at the VistA sign-on window, and click on the OK button, the main window will open (Figure 2‑1):

![](vitals-version-5-user-manual/004.png)

Figure ‑

## [^7]Managing Vitals Categories and Qualifiers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Qualifiers describe how patient vital signs and measurements were taken. These qualifiers are categorized by location (e.g., right arm, left leg), position (e.g., lying, sitting, standing), method (e.g., cuff, Doppler, assisted ventilator, etc.), site (e.g., right, left), quality (e.g., actual, estimated), and cuff size (e.g., adult, small adult, pediatric). Synonyms are used as qualifier abbreviations and are appended to the measurement's numeric values on some displays.

[^8]Vital types, categories, and qualifiers are nationally defined and cannot be changed locally. Each vital type may be linked to one or more categories, and each category may be linked to one or more qualifiers. The linkages between qualifiers, categories, and vital types are also nationally defined and cannot be changed locally. (See the National Term Rapid Turnaround web site at <span class="mark">REDACTED</span> to request a qualifier change.)

To view the categories and qualifiers that are associated with a particular vital type, double-click the Vitals folder to display the full list of vital types, then click on a vital type to view. A list of categories and qualifiers displays on the right side of the Vitals Manager window (Figure 2‑2):

![](vitals-version-5-user-manual/005.png)

Figure ‑

## Printing a Qualifiers Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Qualifiers Table is a list of all qualifiers for each vital type and its categories, including each qualifier’s synonym. The Package Coordinator may use this list to determine the accuracy and completeness of the qualifier selection. Qualifiers that are not associated with a category and vital type do not appear in this list.

To print the Qualifiers Table go through the main menu bar and select File, Print Qualifiers Table. The following screen appears:

![](vitals-version-5-user-manual/006.png)

[^9]Figure ‑

Select an appropriate device in the Device field. Select a date/time to queue this report in the Queue To Run at field. The default date/time is the current server date/time. This report can’t be queued to run for a past date/time. Click the OK button to print the report.

## Editing Abnormal Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An abnormal value is defined as a value outside the normal range for a vital type. You can define what these high/low values should be so that when a user enters a vital/measurement outside the normal range of values for a vital type, the value will show on the data table as an abnormal value. It will be bold, or a different color dependent upon how it is defined in the User Options option in the Vitals module. User Options is used to define what the text should look like in the data table (bold, different color, etc.) for both normal and abnormal values. Refer to the section on [Editing User Options](#_Editing_User_Options_2) in the Entering Vitals Data chapter in this manual.

To edit abnormally high and low vital type values double click on the Abnormal Values folder to open it, then click on the vital type you wish to edit high/low values for. The following window appears (Figure 2‑4):

![](vitals-version-5-user-manual/007.png)

[^10]Figure ‑

You can either move the bar up or down to change the abnormal value or type in the abnormal value. If you type in a value, the meter will not reflect the value until you click in an area outside the box where you entered the value. Click the Save Abnormal Values button next to the Abnormal Values heading at the top of the window to save the values.

## Editing System Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 3 system parameters in the Vitals Manager module. They are:

> Allow User Templates

> Help Menu Web Address

> Version Compatibility

To edit system parameters double click on the System Parameters folder to open it (Figure 2‑5). Below are instructions for editing each of the system parameters.

Allow User Templates allows a CAC or package coordinator to decide whether a clinician should be able to create/edit user templates in the Vitals Manager and Vitals modules. When the checkbox is checked, a clinician is able to create/edit user templates in the Vitals Manager and Vitals modules.

Help Menu Web Address contains the address for the Vitals Home Page and directs the user’s default browser to this page when accessed.

Version Compatibility is used to check if a client version is compatible or not with the current version of Vitals running on the VistA M server. All previously installed versions of Vitals/Measurements are listed in this parameter. Only the version(s) that are compatible with the current server version are checked. These versions are identified by their executable name and the Windows file version. Because backward compatibility is required, more than one version of the software may be flagged as compatible.

![](vitals-version-5-user-manual/008.png)

[^11]Figure ‑

Click the Save System Parameters button next to the System Parameters heading at the top of the window to save the values.Special Note: The VistA server install (KIDS Build) will automatically set the Help Menu Web Address and Version Compatibility parameters for the client/server versions being installed. After an installation this parameter should be carefully reviewed. Modification of this parameter should not be needed unless the site is testing a patch or performing local modifications to the client software.

## Creating/Editing a Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Templates are a set of vitals/measurements grouped together to make data entry simpler and easier. Using the Vitals Manager module, templates can be created for the following categories[^12]:

> System – Templates are available to all system users

> Division – Templates are available to all users within a division (for multi-divisional sites)

> Location – Templates are available to all users within a particular ward , team, or clinic

> User – Templates are available only to the individual user who created the template

> **NOTE:** The Allow User Templates system parameter must be checked and system parameters must be saved in order to see User templates.

All templates are created the same way. The following instructions show how to create/edit a template for a Location.

To create a new template, go through the main menu bar and select Templates, New Template. You can also click on the Create a New Vitals Input Template button on the toolbar to create a new template. The following window appears (Figure 2‑6).

![](vitals-version-5-user-manual/009.png)

Figure ‑

In the Type section of the window, select the type of template you want to add by clicking the appropriate radio button. In this case the type selected is Location.

![](vitals-version-5-user-manual/010.png)

Figure ‑

Enter the name of the (division, location, user) this template is to be associated with in the Division/Location/User Name field (Figure 2‑7). In this case the field says Location Name. For Location, only entries in the Hospital Location (#44) file may be selected. For Division, only entries in the Institution (#4) file may be selected. For User, only entries in the New Person (#200) file may be selected. For System, only entries in the Kernel System Parameters (#8989.3) file may be selected.

Enter the name of the template you want to add in the Template Name field (maximum length is 30 characters).

Enter a short description of the template in the Template Description field (maximum length is 50 characters). This field is optional. Click the OK button to create the blank template.

![](vitals-version-5-user-manual/011.png)

[^13]Figure ‑

[^14]Your new blank template appears on the screen (Figure 2‑8). Now you can edit your template to add vital types and qualifiers to it. Click the Add button on the right side of the screen display to add vital types to the template and the following window appears.

![](vitals-version-5-user-manual/012.png)

Figure ‑

Click on each of the vital types you want to add to your template (Figure 2‑9). You may select multiple vital types by holding down the Ctrl key and selecting multiple vital types, or hold down the Shift key to select a range of vital types. Click the OK button when finished.

![](vitals-version-5-user-manual/013.png)

[^15]Figure ‑

[^16]Your template now has vital types, but no default qualifiers (Figure 2‑10). To assign default qualifiers you must select each vital type to edit it. Select a vital type by clicking on it, and the qualifiers for that vital type appear in a drop-down list on the bottom portion of the screen.

![](vitals-version-5-user-manual/014.png)

[^17]Figure ‑ – The Template Editor screen

Select the qualifiers desired by clicking on the desired entry in the list. Only one qualifier can be selected from each category (Figure 2‑11). You can select US or Metric scale for each appropriate vital type from the Measurement box. US is the default. Qualifiers are automatically saved.

Now your template is complete.

Make a template a default by going through the main menu bar and selecting Templates, Set Default Template, or click the Set Template as Default button on the toolbar. The default templates show up with a yellow icon on the list on the left side of the screen.

Each Division, Location, and User (e.g., 3AS) can have only one template at a time designated as the default. Designating a template as a default is merely a way to indicate a preference for that template. You do not have to indicate a template as a default. However, it is recommended that you designate one System level template as a default. When first time users enter patient data, the default System template will be displayed until the user selects another template instead.

Select a vital type and click the Delete button on the right side of the Template Editor screen to remove a vital type from the template.

Use the up/down arrow buttons to move vital types around in the list.

Go through the main menu bar and select Templates, Save Template, or click on the Save Template button to save the template settings.

To delete a template, highlight the template name, then from the main menu bar select Templates, Delete Template, or click on the Delete Template button.

# [^18]Using Vitals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter contains an overview of the features and options available in the Vitals module.

Online help is available throughout the Vitals application. Click the Help menu at the top of the screen to see a table of contents and index containing help on how to enter data, print reports, etc. There is help available on every screen by pressing the F1 key.

This chapter contains the following topics and sections:

1\. [Start the Vitals module](#getting-started-with-vitals)

2\. Get an [Overview of the Vitals window](#_Overview_of_the_Vitals window)

3\. Customize the GUI by [editing User Options](#_Editing_User_Options_1)

4\. Learn about [CCOW](#about-ccow) and Clinical Context management

## Getting Started with Vitals 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To open the Vitals application, double-click the Vitals icon on your desktop, or select Vitals from your CPRS Tools menu. Enter your access and verify codes at the VistA sign-on window, and then click the OK button. The main Vitals window opens:

![](vitals-version-5-user-manual/015.png)

Figure ‑

## Overview of the Vitals window 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vitals window is divided into two main sections: the Patient Selector panel on the left, and the Vitals Data area on the right. In the example above (Figure 3‑1), the Vitals Data area is empty because a patient has not yet been selected.

The screen layout is saved between sessions, so the last lookup that was used appears when opening the Vitals module. For example, if “Ward” was the last selection made in the Patient Group List, then it will be the default selection when the current session is opened. The software will display previous values as defaults whenever possible. See the [Selecting a Patient and a Template](#_Selecting_a_Patient_and a Template) section (page [4-1](#_Ref123015344)) for more information about the Patient Selector panel.

The Vitals application contains a navigation bar across the top of the main window:

![](vitals-version-5-user-manual/016.png)

- The Patient Name-SSN-DOB box at left is a button. Clicking this button opens a Patient Inquiry screen containing general information such as address, status, and appointments for this patient. This report can be printed. See Figure 4‑4.
- The Hospital Location-Date box is an informational area that displays the patient’s current hospital location, if one has been assigned, and the currently selected date range.
- The Pt <u>S</u>elect button opens and closes the Patient Selector panel. See Figure 4‑3.
- The <u>E</u>nter Vitals button opens the Vitals Input screen when a single patient is selected so users can select templates and enter vitals data. See Figure 4‑6.

  If multiple patients are selected, the <u>E</u>nter Vitals button will be unavailable; instead, a button labeled Input Vitals for the Selected Patients will become available. This button is located at the bottom of the Patient Selector pane. See Figure 4‑8.
- The Alle<u>r</u>gies button opens a list of any allergies the patient may have.

A similar navigation bar is available at the top of the Enter Vitals window:

![](vitals-version-5-user-manual/017.png)

- The Patient Name-SSN-DOB box at left is a button. Clicking this button opens a Patient Inquiry screen containing general information such as address, status, and appointments for this patient. This report can be printed. See Figure 4‑4.
- The Hospital Location-Date box is an informational area that displays the patient’s current hospital location, if one has been assigned, and the currently selected date range.
- [^19]Read Monitor retrieves data from a vital sign monitor connected to the workstation.
- The <u>D</u>ate/Time button opens a date/time selection window. See Figure 4‑7
- The <u>H</u>ospital button opens a hospital location selection window. See Figure 4‑5.
- The Exp. Vie<u>w</u> button opens and closes the template selection panel at the left side of the Enter Vitals window. See Figure 4‑6.
- The Latest <u>V</u>. button opens and closes the latest vitals display panel at the bottom of the Enter Vitals window. See Figure 4‑6.

<span id="_Editing_User_Options_1" class="anchor"></span>

## Editing User Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can customize the Vitals windows by choosing how to display the text on the data table and the latest vitals area. You can change the color of the text, the background color, bold the text, and show qualifier abbreviations. To edit these preferences, go through the main menu bar and select File, User Options. The following window appears (Figure 3‑2).

![](vitals-version-5-user-manual/018.png)

[^20]Figure ‑

Preferences can be set for both normal and abnormal values. Click the Text button to select a text color for the table and latest vitals display. Click the Background button to select a background color for the table and latest vitals display. Check the Bold checkbox to make the text bold. Check the Show Qualifiers checkbox to show qualifier abbreviations with each value.

Click the Defaults button to restore default settings. Default settings for normal values are:

> Text is black, Background is white, Bold is not checked, and Show Qualifiers is checked.

Default settings for abnormal values are:

> Text is red, Background is white, Bold is not checked, and Show Qualifiers is checked.

The Search Delay setting allows the user to define a time lag to use between entering characters and beginning the patient lookup. If the time lag passes before the next character is typed, the patient lookup component will use the characters already entered to create a selection list.

![](vitals-version-5-user-manual/019.png)

[^21]Figure ‑

Select the appropriate search delay in seconds from the dropdown list (Figure 3‑3).

Click the Apply button to save the settings. Click the OK button when finished.

## About CCOW

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinical Context Management (also called “CCOW”) is a way for VistA applications to synchronize their clinical context based on the Clinical Context Object Workgroup standard. In simple terms, this means that if CCOW-compliant applications are sharing context and one of the applications changes to a different patient, the other applications will change to that patient as well. By default, the CCOW link is automatically active. (See Appendix C for information on using /noccow or /ccow=patientonly switches to disable CCOW or limit its functionality.)

Vitals has been made CCOW-compliant and can now synchronize with other CCOW-compliant VistA applications. For example, if you are logged in on CPRS (which is also CCOW-compliant) and clicked the Vitals link, the Vitals GUI will be launched and will open the same patient that is active in CPRS. You can also open two different Vitals sessions and not synchronize them, allowing you to view two patients’ charts at the same time.

For more information about the CCOW standards for VistA applications, see the Workgroup web site at: <span class="mark">REDACTED</span> .

The CCOW icon shows whether Vitals is linked with other CCOW compliant applications on the desktop. One of these three icons will display:

![](vitals-version-5-user-manual/020.png) Active – A single figure with a chain link indicates that CCOW link is active.

![](vitals-version-5-user-manual/021.png) Broken – Multiple figures with a broken chain link indicates that the CCOW link has been broken and that the applications are no longer synchronized.

![](vitals-version-5-user-manual/022.png) Unavailable – A red circle with a diagonal line through it indicates that the Contextor software has not been installed and CCOW is not available.

### Joining a Clinical Context

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCOW clinical link is automatically active, and will remain active unless you break the clinical link. To manually join the clinical context, go through the File menu and select Rejoin Clinical Link. If you want the other open applications to synchronize with the current patient in the active application, select Use this Application’s Data. If you want the current application to synchronize with the patient that is open in another application, select Use Global Data.

The CCOW icon changes to Active and all open VistA applications are synchronized.

### Breaking the Clinical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To break the CCOW Clinical Context link, go through the File menu and select Break the Clinical Link.

The CCOW icon changes to Broken and the VistA applications are un-synchronized, allowing you to work on two different patients when multiple CCOW-compliant applications are open..

### Showing status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To see information about CCOW, go through the File menu and select Show Status. An information window opens, stating whether or not the Contextor software has been installed, and whether the application is participating in a clinical context.

*This page intentionally left blank for double-side printing.*

# Entering Vitals Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vitals module is used to enter vitals data, create user templates, view allergies, and mark incorrect vitals as entered in error. These topics are discussed in this chapter. The Vitals module also lets the user print several different Vitals reports; this is discussed in the [Reports](#reports) chapter in this manual.

This chapter shows you how to:

- [Select a patient for vitals entry](#_Select_a_Patient_and a Template)
- [Enter vitals data](#_Entering_Vitals_Data_1)
- [Create a user template](#creating-a-user-template)
- [View allergies](#viewing-allergies)
- [Mark vitals as entered in error](#marking-vitals-as-entered-in-error)
- [Edit user options](#_Editing_User_Options)

## Selecting a Patient and a Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enter vitals data, you will use a template. Templates are a set of vitals/measurements grouped together to make data entry simpler and easier. Templates for system, divisions, locations, and users can be created in the Vitals Manager module. Refer to the section on [Creating/Editing a Template](#creatingediting-a-template) in the Using Vitals Manager chapter of this manual for more information on creating/editing templates for system, divisions, locations, and users. If allowed, templates can be created for yourself as a user in the Vitals module. These templates are called user templates. For information on creating a user template refer to the section on [Creating a User Template](#creating-a-user-template) later in this chapter.

The Patient Selector must be open in order to select a patient. To open the Patient Selector, go through the main menu bar and select File, [^22]Pt Select, or click the Pt Select button on the top right side of the screen. The last lookup that was used appears when opening the Patient Selector.

Patients can be selected by Unit, Ward, Team, Clinic, or All. “Unit” allows the user to select from a list of Nursing units. “Ward” allows the user to select from a list of MAS Wards. “Team” allows the user select from a list of teams defined in the OE/RR List file (#100.21). “Clinic” allows the user select from a list of clinics for a predetermined period of time (e.g., Today, Yesterday, Past week). “All” allows the user to select a single patient by name or SSN.

To begin selecting patient names, click the desired tab under Patient Groups List (in this example “All” is selected), then enter the first few letters of the patient’s name, or the last four digits of the patient’s Social Security Number. A list of patients matching those criteria are listed on the bottom left portion of the screen (Figure 4‑1).

![](vitals-version-5-user-manual/023.png)

[^23]Figure ‑

At this point you can either select a single patient name or multiple patient names.

## [^24]Entering Data for a Single Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a patient name by double clicking it. A confirmation screen appears (Figure 4‑2).

![](vitals-version-5-user-manual/024.png)

Figure ‑

This screen shows you additional information on the selected patient. If the patient selected is a sensitive patient, a sensitive patient screen will appear telling you that this patient’s information is available on a need-to-know basis only. Click the OK button to confirm your patient selection.

The patient information opens in the Vitals window (Figure 4‑3), showing existing data on a graph and in a spreadsheet-like data grid. You can access a text-only version of the data grid by going through the File menu and selecting Data Grid Report.

![](vitals-version-5-user-manual/025.png)

[^25]Figure ‑

The time scale runs from left to right, displaying the most recent values on the far right side of the graph and grid. You can move left and right across the graph by moving the slider bar between the graph and the grid. To expand the graph and grid displays for the selected patient, click the Pt Select button to close the Patient Selector pane.

You can view patient data within a selected date range: “Six Months” is selected in the example above (Figure 4‑3). Select a predetermined time frame by clicking one of the values on the left of the graph: “Today” displays today’s data only, “T-1” displays data for today plus one previous day, “T-7” displays data for today plus seven previous days, and so on. “All Results” displays all available vitals data for the selected patient. If you would rather define your own dates, click the Date Range button, then set "Start with" and "Go to" dates.

You can view 15 different types of graphs for the selected date range. Select a graph type from the Graph drop-down list, or click a vital type row heading in the grid to graph that vital type. The TPR graph is selected in the example above, showing Temp, Pulse, and Respiration values.

[^26]Four Graph Options checkboxes are available on the left side of the graph. If the check boxes are not visible, right-click the screen (but not on the graph itself) and select Graph Options. This menu option may also be selected from the File menu.

- Click the Values checkbox to display a numeric label for each point on the graph.
- Click the Time Scale checkbox to view the graph in actual time instead of evenly distributed intervals. You can also click on a data point in the graph to see additional information about the vitals that were entered on that day.
- Click the 3D checkbox to create a 3D effect on the graph. This option is only available when the Time Scale checkbox has been checked.
- Click the Allow Zoom checkbox to zoom the graph view in or out. You can zoom in by clicking inside the graph and dragging a selection box around one or more data values to view in detail, or by clicking the Zoom Graph In button (the magnifying glass icon with the plus sign in the center). You can zoom out by clicking the Zoom Graph Out button (the magnifying glass icon with the minus sign in the center.) Enter a new value in the Zoom Percent text box to change the zoom percentage (default is 10). Click the Reset Zoom button to reset the Zoom Percent box to its original value.

Two additional graph options can be accessed from this window. Right-click the screen (but not on the graph itself) to display these menu options, or select them from the File menu:

- Select Graph Color allows you to set the background color of the graph.
- Print Graph allows you to send the graph display to a printer. The graph will be printed as it appears on the screen at the time of printing.

The remaining right-click menu options (Entered in Error, Enter Vitals, and Allergies) are described later in this chapter.

You can view a report containing general patient information by clicking the patient name button at the top left corner of the screen, by selecting Patient Inquiry from the File menu, or by selecting Pt Info from the View menu (Figure 4‑4) .

![](vitals-version-5-user-manual/026.png)

Figure ‑

Click the Print button to print this report. Click the Close button to close this screen.

Click the Enter Vitals button to go to the Enter Vitals screen. The Hospital Location Selector window opens first (Figure 4‑5). If a location has been assigned to the patient already, the Hospital Location window will not open.

> ![](vitals-version-5-user-manual/027.png)

Figure ‑

To select a location, click one of the three tabs in the Hospital Location Selector:

- The Appointments tab lists all appointments for this patient for the last year. Click an appointment to select that clinic location.
- The Admissions tab lists all existing admissions for this patient. Click an admission to select that hospital location.
- The Name tab allows you to search for all available hospital locations. Enter the first few letters of the location name to open a list of matching locations, then click one to select it.

Click the Select button to complete the Hospital Location selection, or click the Cancel button to cancel the selection.

The Enter Vitals window opens, showing the selected patient’s name, Social Security number, and date of birth in the upper left corner of the window. The selected Hospital Location and current Date/Time are also shown at the top of the window.

![](vitals-version-5-user-manual/028.png)

[^27]Figure ‑

[^28]Click the Read Monitor button (Figure 4‑6) to retrieve vital sign readings from a vital sign monitor (VSM) connected to the workstation. The vital sign readings that appear on the VSM screen will be sent to the "Enter Vitals" screen and pasted into the input template.

Click on the Date/Time button to select a different date or time (Figure 4‑7). The default date/time is the current server date/time.

![](vitals-version-5-user-manual/029.png)

[^29]Figure ‑

Select a date from the calendar by clicking on it, or click Today to select the current date. Select a time either by entering in the time in the Time field, or by selecting the time using the hour and minute lists under the Time field, or click Now to select the current time. Click the Midnight button to select 12:00 midnight. Click the OK button to complete the selection, or click the Cancel button to cancel the selection. You cannot select a date/time in the future.

Select a template from the Templates list on the left side of the screen (Figure 4‑6). Templates are categorized by System, Division, Location, and User. Templates for system, division, and location are available to everybody. You can select anybody’s user template as long as you have the GMV MANAGER key. If you do not have the GMV MANAGER key, only your own user templates will be available in the User category. Contact your IRMS support person if you think you should have the GMV MANAGER key.

Enter values for the vital types by typing them in the appropriate box. The default qualifiers for each vital type appear to the right of the down arrow button for each vital type. Click the down-arrow button next to each vital type to select a different qualifier, if necessary.

> Note: BMI is calculated from Height and Weight values and cannot be entered here.

To enter a non-numeric value for a particular vital sign or measurement, use one of these options:

- Click Patient on Pass to mark all vitals as "Pass" for this date/time.
- Click the U… checkbox next to any vital sign to indicate that information is unavailable.
- Click the R… checkbox next to any vital sign to indicate that the patient refused that measurement.

> The last two options are available only if the Enable U. and/or Enable R. boxes at the top of the Enter Vitals window are checked.

Click the Save button to save the data for these vital types. Click the Save And Exit button to save the data for these vital types and close the Enter Vitals window. Click the Exit button to close the Enter Vitals window without saving any data.

The look of the Units column can be changed by checking the Units as Drop Down List box. When the Units column is set to a metric setting, the data entry for that vital type is expected to be a metric reading. If the user wants to enter the reading in US Standard format, select the US Standard format from the Units column. To make US Standard the default for a vital type, the template definition must be edited. Refer to the [Creating a User Template](#creating-a-user-template) section for more information on creating/editing templates.

Click the Exp. View button to view/hide the Template fields on the left side of the screen. Click the LatestV button to view/hide the latest vitals display on the bottom of the screen. The latest vitals display shows the most recent reading for each vital type on record for the patient. If there is no reading for a vital type (e.g., CVP), then that vital type is not listed.

### [^30]Enter Vitals Menu Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may also access the functions described above using the menu bar on the Enter Vitals screen, which allows access using only the keyboard. (See Appendix A for a complete list of access keys.)

The menu bar lies below the title bar. The Enter Vitals menu bar contains two options: File and View. Click an option on the menu bar to list all the operations you can perform from within that menu. Click the desired option to execute a specific function.

Each menu option and its corresponding suboptions display as follows:

#### File

The following options are available from the File menu:

- Patient Inquiry
- Latest Vitals Report
- Read Monitor:
- Date/Time (Ctrl + D)
- Hospital (Ctrl + H)
- Save
- Exit

#### View

The following options are available from the View menu:

- Expanded View
- Latest Vitals
- Enable U
- Enable R
- Unit as Drop Down List

## [^31]Entering Data for Multiple Patients 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have taken vitals for a group of patients in one ward or unit, these instructions will help you enter the vitals for all the patients in one session. The Location and Date/Time settings remain the same throughout the session, so you can quickly enter the same vitals information for each patient in the list.

Select multiple patients by holding down the Ctrl key and clicking on specific patients, or hold down the Shift key to select a range of patients. To select an entire ward you must first select all the names in the ward.

Once you have selected the patients (Figure 4‑8), click the Input Vitals for the Selected Patients button at the bottom left corner of the screen.

![](vitals-version-5-user-manual/030.png)

Figure ‑

No confirmation screen will appear when multiple patients are selected, but if any sensitive patients are selected, a confirmation screen will appear for each sensitive patient. You must respond to these screens before the Enter Vitals window will open.

[^32]You may receive the following warning: “You must leave the CCOW patient context to work with multiple patients.” Go to the File menu and select Break the Clinical Link to turn off the CCOW functionality.

The Hospital Location Selector window opens first (Figure 4‑9). If a location has been assigned to the first patient already, the Hospital Location window will not open.

> ![](vitals-version-5-user-manual/031.png)

Figure ‑

To select a location, click one of the three tabs on the Hospital Location Selector:

- The Appointments tab lists all appointments for this patient for the last year. Click an appointment to select that clinic location.
- The Admissions tab lists all existing admissions for this patient. Click an admission to select that hospital location.
- The Name tab allows you to search for all available hospital locations. Enter the first few letters of the location name to open a list of matching locations, then click one to select it.

Click the Select button to complete the Hospital Location selection, or click the Cancel button to cancel the selection.

The Enter Vitals window opens (Figure 4‑10). The Patient List on the top left portion of the screen contains the list of patients that were previously selected. The arrow indicates which patient you are entering data for – in this example, VITPATIENT,FOUR.

![](vitals-version-5-user-manual/032.png)

[^33]Figure ‑

Click the Read Monitor button (Figure 4‑10) to retrieve vital sign readings from a vital sign monitor (VSM) connected to the workstation. The vital sign readings that appear on the VSM screen will be sent to the "Enter Vitals" screen and pasted into the input template.

Click on the Date/Time button and select a date/time (refer to Figure 4‑7). The default date/time is the current server date/time. The selected date/time appears in the top Navigation Bar.

Select a template from the Templates list on the left side of the screen (Figure 4‑10). Templates are categorized by System, Division, Location, and User. Templates for system, division, and location are available to everybody. You can select anybody’s user template as long as you have the GMV MANAGER key. If you do not have the GMV MANAGER key, only your own user templates will be available in the User category. Contact your IRMS support person if you think you should have the GMV MANAGER key.

Enter values for the vital types by typing them in the appropriate box. The default qualifiers for each vital type appear to the right of the down arrow button for each vital type. Click the down arrow button next to each vital type to select a different qualifier, if necessary.

> Note: BMI is calculated from Height and Weight values and cannot be entered here.

To enter a non-numeric value for a particular vital sign or measurement, use one of these options:

- Click Patient on Pass to mark all vitals as "Pass" for this date/time.
- Click the U… checkbox next to any vital sign to indicate that information is unavailable.
- Click the R… checkbox next to any vital sign to indicate that the patient refused that measurement.

> The last two options are available only if the Enable U. and/or Enable R. boxes at the top of the Enter Vitals window are checked.

Click the Save button to save the data for these vital types and move on to the next patient. Click the Exit button to exit the template without saving any data.

If you select another patient name without clicking the Save button, this message appears:

![](vitals-version-5-user-manual/033.png)

Figure ‑

Click Yes to save the original patient’s data and switch to the new patient. Click No to switch to the new patient without saving the original patient’s data.

The look of the Units column can be changed by checking the Units as Drop Down List box. When the Units column is set to a metric setting that means the data entry for that vital type is expected to be a metric reading. If the user wants to enter the reading in US Standard format then select the US Standard format from the Units column. To make US Standard the default for a vital type, the template definition must be edited. Refer to the section on [Creating a User Template](#creating-a-user-template) for more information on creating/editing templates.

Click the Exp View button to view/hide the Template fields on the left side of the screen. Click the LatestV button to view/hide the latest vitals display on the bottom of the screen. The latest vitals display shows the most recent reading for each vital type on record for the patient. If there is no reading for a vital type (e.g., CVP), then that vital type is not listed.

## Creating a User Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Templates are a set of vitals/measurements grouped together to make data entry simpler and easier. If the system parameter Allow User Templates in the Vitals Manager module is checked, you may create/edit your own templates in this screen. If Allow User Templates is not checked, then the creation of user templates is not allowed. Refer to the section called [Editing System Parameters](#_Editing_System_Parameters) in the Using Vitals Manager chapter for more information.

To create/edit a template for a system, division, or location refer to the section called [Creating/Editing a Template](#creatingediting-a-template) in the Using Vitals Manager chapter of this manual.

To create or edit a user template, go through the main menu bar and select File, Edit User Templates. The following window appears (Figure 4‑12).

![](vitals-version-5-user-manual/034.png)

[^34]Figure ‑

You can only see templates that you created in this window: if you have not created any templates, all fields in this window will be empty. Click the New Template button at the bottom of the window to create a new template for yourself as a user.

![](vitals-version-5-user-manual/035.png)

Figure ‑

Enter a name for the template in the Template Name field (maximum length is 30 characters) (Figure 4‑13). The name should help the user distinguish what the template does. Click the OK button to continue.

![](vitals-version-5-user-manual/036.png)

[^35]Figure ‑

Your new blank template appears in the list on the left side of the screen (Figure 4‑14). Click on the name of your new template to select it. Enter a short description of the template in the Description field (maximum length is 50 characters). This field is optional.

Now you can edit your template to add vital types and qualifiers to it. Click the Add button on the right side of the screen (Figure 4‑14) to add vital types to the template. The following window appears.

![](vitals-version-5-user-manual/037.png)

Figure ‑

Click on each of the vital types you want to add to your template (Figure 4‑15). You may select multiple vital types by holding down the Ctrl key and selecting multiple vital types, or hold down the Shift key to select a range of vital types.

![](vitals-version-5-user-manual/038.png)

Figure ‑

[^36]Your template now has vital types, but no default qualifiers (Figure 4‑16). To assign default qualifiers you must select each vital type to edit it. Select a vital type by clicking on it, and the qualifiers for that vital type appear in a dropdown list on the bottom portion of the screen.

![](vitals-version-5-user-manual/039.png)

Figure ‑

Select the qualifiers desired by selecting from the dropdown list. Only one qualifier can be selected from each category (Figure 4‑17). You can select US or Metric scale from the Measurement box for each vital type where appropriate. US Standard is the default.

![](vitals-version-5-user-manual/040.png)

Figure ‑

Now your template is complete (Figure 4‑18). Click Save to save this new template and add it to the User Templates list. The template is ready to use.

 

[^37]If you would like to edit an existing User Template, click the template name in the User Templates list to select it. Any of the following items may be updated:

- Change the Template Name (up to 30 characters)
- Change the Template Description (up to 50 characters)
- To add a new vitals type, click the plus sign button and select one or more vitals types
- To delete an existing vital type, select the vital type and then click the minus sign button
- To add or modify qualifiers for a vital type, select the vital type and then check or clear the checkboxes in the Qualifiers list. If no qualifiers are available for the selected vital type, the Qualifiers list will be empty.

When you are finished making changes to the template, click the Save button at the bottom of the window. The template is ready to use.

If you would like to delete an existing User Template, click the template name in the User Templates list to select it, then click the Delete button at the bottom of the window.

Click the Close button at the bottom of the window to return to the main Vitals window.

## Viewing Allergies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view any allergies this patient may have, click on the Allergies button at the top of the main Vitals window. The Allergy Display screen opens (Figure 4‑19).

![](vitals-version-5-user-manual/041.png)

Figure ‑

Click the Close button to close this window.

## [^38]Marking Vitals as Entered in Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals data values cannot be deleted once they have been saved – if incorrect vitals data have been saved, they must be marked "Entered in Error" and replaced with corrected data. Any data values that have been marked "in error" will continue to be stored in the Vitals database, but will not be displayed in the patient’s data grid and graph.

Users can mark any vitals that were incorrectly entered as “entered in error” by using this option. Users will still need to go back and enter a new entry to correct the entry that will be marked as entered in error. Refer to [Entering Vitals Data](#_Entering_Vitals_Data_1) for more information.

To mark vitals data as entered in error, a patient must be selected in the main Vitals window.

Locate the incorrect vitals data, then click its column heading in the graph (Figure 4‑20). The Entered In Error window opens, listing all the vitals entries for the selected date.

![](vitals-version-5-user-manual/042.png)

[^39]Figure ‑

Alternately, you can right-click on the graph and select Entered In Error from the pop-up menu or from the File menu. Select a date by clicking the down-arrow button to display a calendar. The default date is today. September 15, 2005 is selected in this example.

Select the incorrect entry by clicking on the entry – Blood Pressure is selected in this example (Figure 4‑20). You can select multiple entries by holding down the Shift key or the Control key and clicking the entries to select them.

Select the reason the entry or entries are incorrect by clicking the appropriate radio button in the Reason section. Click the Mark as Entered in Error button to mark the vitals as entered in error.

[^40]Note: Records entered through the Clinical Observations (CliO) package cannot be changed to Entered in Error here. They must be addressed in the CliO package.

![](vitals-version-5-user-manual/043.png)

Figure ‑

A confirmation screen appears (Figure 4‑21). Click the Yes button to confirm the entry is correct. Click the No button to select a different entry.

You may now enter new vitals data to replace the incorrect entries, if necessary.

To print a list of all Entered In Error vitals for this patient, see the [Printing a Report](#printing-a-report) section.

<span id="_Editing_User_Options" class="anchor"></span>  
*This page intentionally left blank for double-side printing.*

# Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vitals module is used to print several different Vitals reports. The viewing and printing of these reports is discussed in this chapter. The Vitals module also lets the user enter vitals data, create user templates, view allergies, mark incorrect vitals as entered in error, and edit user preferences for data display on the vitals data table, these topics are discussed in the [Entering Vitals Data](#entering-vitals-data) chapter in this manual.

This chapter shows you how to:

1\. [View a graphic report](#viewing-a-graphic-report)

2\. [Print a report](#printing-a-report)

## [^41]Viewing a Graphic Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a patient is selected in the main Vitals window, existing vitals data values are displayed on the right side of the window in a graph (top) and a grid (bottom). The time scale runs from left to right, displaying the most recent values on the far right. You can select a date range and a type of graph to narrow down the amount of data to be displayed.

To view a graphic report for a particular patient, use one of the following methods to select a date range from the box on the top left side of the reports screen:

- Click a predetermined time frame from the box on the left of the graph. TODAY displays today’s data only, T-1 displays data for today plus one previous day, T-7 displays data for today plus seven previous days, and so on up to Two Years worth of past data. All Results displays all available vitals data for the selected patient.
- Click Date Range to select a customized date range, then set "Start with" and "Go to" dates.

All data within the selected date range is displayed in the graph and grid. This example shows the graph portion only (Figure 5‑1):

![](vitals-version-5-user-manual/044.png)

Figure ‑

You can view 15 different types of graphs for the selected date range for this patient. Select a graph type from the Graph drop-down list next to the slider bar, or click a vital type row heading in the grid to graph that particular vital type. The “TPR” graph is selected in this example (Figure 5‑1), showing Temp, Pulse, and Respiration values.

> **NOTE:** Intake and Output values are obtained from the I&O application and displayed in the bottom rows of the data grid. These rows show the total amount of liquid for the day, in milliliters, and do not include solids. Because these rows display total values, the Entered By and Location values are not tracked for Intake and Output.

Four Graph Options checkboxes are available on the left side of the graph. If the check boxes are not visible, right-click the screen (but not on the graph itself) and select Graph Options. This menu option may also be selected from the File menu.

- Click the Values checkbox to display a numeric label for each point on the graph.
- Click the Time Scale checkbox to view the graph in actual time instead of evenly distributed intervals. You can click on a data point in the graph to see additional information about the vitals that were entered that day.
- Click the 3D checkbox to create a 3D effect on the graph. This option is only available if the Time Scale checkbox has been checked.
- Click the Allow Zoom checkbox to zoom the graph view in or out. You can zoom in by clicking inside the graph and dragging a selection box around one or more data values to view them in detail, or by clicking the Zoom Graph In icon (the magnifying glass icon with the plus sign in the center). You can zoom out by clicking the Zoom Graph Out button (the magnifying glass icon with the minus sign in the center.) Enter a new value in the Zoom Percent text box to change the zoom percentage (default is 10). Click the Reset Zoom button to reset the Zoom Percent box to its original value.

Two additional graph options can be accessed from this window. Right-click the screen (but not on the graph itself) to display these menu options, or select them from the File menu:

- Select Graph Color allows you to set the background color of the graph.
- Print Graph allows you to send the graph display to a printer. The graph will be printed as it appears on the screen at the time of printing, for the selected patient only.

## [^42]Printing a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[^43]Four standard reports are available in the Vitals application:

Cumulative Vitals Report Available for single patient, entire ward, or selected rooms on a ward

Latest Vitals by Location Available for an entire ward

Latest Vitals Display for a Patient Available for single patient only

Vitals Entered in Error for a Patient Available for single patient only

These reports cannot be viewed on-screen; they must be sent to a printer. These reports require a printer that can handle 80 or more columns:

To print a report, go through the main menu bar and select Reports, then select the report you want to queue. The following window appears (Figure 5‑2).

![](vitals-version-5-user-manual/045.png)

[^44]Figure ‑

The selected report appears in the Select Report field. You may select a different report from the drop-down list in this field, if necessary.

In the Include Patients section, you may select a specific patient, an entire ward, or specific rooms/beds on a ward. The default patient is the currently selected patient. Ward and Room/Beds do not apply when a specific patient is selected.

Enter a Start Date and an End Date for the selected report, if appropriate. The default date for Start Date and End Date is today. Start/End dates do not apply when printing the Latest Vitals by Location report, or the Latest Vitals Display for a Patient report.

Select a device from the Select Device field by typing in a partial name and selecting the appropriate device from the list.

You can also select a date/time to print this report (default is today). Reports cannot be queued to print for a past date/time.

Click the Print button to print the report. A dialog box appears indicating the success or failure of the queuing of the report.

[^45]Note: As of Patch GMRV\*5.0\*23, three reports were moved from the File menu to the Reports menu:

- Patient Inquiry
- Allergies
- Data Grid Report

In addition, a new report, Graph Report, was added to the Reports menu. The Graph Report option was added to convey trending information to users using screen readers.

# [^46]Appendix A – Access Key Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a listing of access keys for the Vitals and Vitals Manager applications.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 48%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Screen</strong></th>
<th><strong>Option / Button Text</strong></th>
<th><strong>Access Key</strong></th>
<th><strong>Shortcut<br />
Key #1</strong></th>
<th><strong>Shortcut<br />
Key #2</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Main User</td>
<td><strong>File</strong> Menu</td>
<td>Alt + F</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Enter Vitals</td>
<td>E</td>
<td>Ctrl + E</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Printer Setup</td>
<td>P</td>
<td>Ctrl + P</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Entered in Error</td>
<td>N</td>
<td>Ctrl + R</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Edit User templates</td>
<td>U</td>
<td>Ctrl + U</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>User Options</td>
<td>S</td>
<td>Ctrl + S</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Rejoin Clinical Link</td>
<td>R</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Use this Application’s Data</td>
<td></td>
<td>Ctrl + A</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Use Global Data</td>
<td></td>
<td>Ctrl + G</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Break the Clinical Link</td>
<td>B</td>
<td>Ctrl + B</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Show Status</td>
<td>H</td>
<td>Ctrl + O</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Select Graph Color</td>
<td>C</td>
<td>Ctrl + Alt + C</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Print Graph</td>
<td>I</td>
<td>F9</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Exit</td>
<td>X</td>
<td>Ctrl + Alt + X</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Reports</strong> Menu</td>
<td>Alt + P</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Patient Inquiry</td>
<td>P</td>
<td>Ctrl + Alt + Q</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Allergies</td>
<td>R</td>
<td>Ctrl + L</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Data Grid Report</td>
<td>D</td>
<td>Ctrl + Alt + G</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Graph Report</td>
<td>G</td>
<td>Ctrl + Alt + R</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Cumulative Vitals Report</td>
<td>C</td>
<td>Ctrl + F1</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Latest Vitals by Location</td>
<td>L</td>
<td>Ctrl + F2</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Latest Vitals Display for a Patient</td>
<td>A</td>
<td>Ctrl + F3</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Print Vitals Entered in Error for Patient</td>
<td>I</td>
<td>Ctrl + F4</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>View</strong> Menu</td>
<td>Alt + V</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Graph Options</td>
<td>G</td>
<td>Ctrl + Alt + O</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Pt Select</td>
<td>S</td>
<td>Ctrl + Alt + S</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Help</strong> Menu</td>
<td>Alt + H</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Index</td>
<td>I</td>
<td>Ctrl + X</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Vitals Web Site</td>
<td>W</td>
<td>Ctrl + W</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>About</td>
<td>A</td>
<td>Ctrl + T</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Unit button</td>
<td></td>
<td>Alt + U</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Ward button</td>
<td></td>
<td>Alt + W</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Team button</td>
<td></td>
<td>Alt + T</td>
<td></td>
</tr>
<tr class="even">
<td rowspan="2"><p>Main User</p>
<p>(cont)</p></td>
<td>Clinic button</td>
<td></td>
<td>Alt + C</td>
<td></td>
</tr>
<tr class="odd">
<td>All button</td>
<td></td>
<td>Alt + A</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Patient List</td>
<td></td>
<td>Alt + I</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Date</td>
<td></td>
<td>Alt + D</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Graph</td>
<td></td>
<td>Alt + G</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Values checkbox</td>
<td></td>
<td>Alt + L</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Time Scale checkbox</td>
<td></td>
<td>Alt + M</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>3D checkbox</td>
<td></td>
<td>Alt + 3</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Allow Zoom checkbox</td>
<td></td>
<td>Alt + Z</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Enter Vitals button</td>
<td></td>
<td>Alt + E</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Patient Inquiry button</td>
<td></td>
<td>Ctrl + I</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Print</td>
<td></td>
<td>Ctrl + P</td>
<td>F9</td>
</tr>
<tr class="even">
<td></td>
<td>Allergies button</td>
<td></td>
<td>Alt + R</td>
<td>Ctrl + L</td>
</tr>
<tr class="odd">
<td></td>
<td>Pt Select button</td>
<td></td>
<td>Alt + S</td>
<td>Ctrl+Alt+S</td>
</tr>
<tr class="even">
<td>Enter Vitals</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Templates</td>
<td></td>
<td>Alt + T</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Date/Time button</td>
<td></td>
<td>Alt + D</td>
<td>Ctrl + D</td>
</tr>
<tr class="odd">
<td></td>
<td>Hospital button</td>
<td></td>
<td>Alt + H</td>
<td>Ctrl + H</td>
</tr>
<tr class="even">
<td></td>
<td>Exp View button</td>
<td></td>
<td>Alt + W</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Latest V button</td>
<td></td>
<td>Alt + V</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Enable U.</td>
<td></td>
<td>Alt + U</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Enable R</td>
<td></td>
<td>Alt + R</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Patient on Pass</td>
<td></td>
<td>Alt + P</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Units as Drop Down List</td>
<td></td>
<td>Alt + N</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Save And Exit button</td>
<td></td>
<td>Alt + A</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Save button</td>
<td></td>
<td>Alt + S</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Exit button</td>
<td></td>
<td>Alt + X</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Read Monitor</td>
<td></td>
<td>Alt + M</td>
<td></td>
</tr>
<tr class="even">
<td rowspan="2"><p>Hospital Location</p>
<p>Selector</p></td>
<td>Appointments tab</td>
<td></td>
<td>Alt + P</td>
<td></td>
</tr>
<tr class="odd">
<td>Admissions tab</td>
<td></td>
<td>Alt + M</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Name tab</td>
<td></td>
<td>Alt + N</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Select button</td>
<td></td>
<td>Alt + S</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Cancel button</td>
<td></td>
<td>Alt + C</td>
<td></td>
</tr>
<tr class="odd">
<td>Select Date/Time</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>OK button</td>
<td></td>
<td>Alt + O</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Cancel button</td>
<td></td>
<td>Alt + C</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Today button</td>
<td></td>
<td>Alt + T</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>&lt;&lt;&lt; button</td>
<td></td>
<td>Alt + &lt;</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>&gt;&gt;&gt; button</td>
<td></td>
<td>Alt + &gt;</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Now button</td>
<td></td>
<td>Alt + N</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Midnight button</td>
<td></td>
<td>Alt + M</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Time</td>
<td></td>
<td>Alt + I</td>
<td></td>
</tr>
<tr class="even">
<td>Printer Setup</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Name</td>
<td></td>
<td>Alt + N</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Properties</td>
<td></td>
<td>Alt + P</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Size</td>
<td></td>
<td>Alt + Z</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Source</td>
<td></td>
<td>Alt + S</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Portrait</td>
<td></td>
<td>Alt + O</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Landscape</td>
<td></td>
<td>Alt + A</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Network</td>
<td></td>
<td>Alt + W</td>
<td></td>
</tr>
<tr class="even">
<td>Entered In Error</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Select Date</td>
<td></td>
<td>Alt + D</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Incorrect Date/Time</td>
<td></td>
<td>Alt + T</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Incorrect Reading</td>
<td></td>
<td>Alt + R</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Incorrect Patient</td>
<td></td>
<td>Alt + P</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Invalid Record</td>
<td></td>
<td>Alt + E</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Mark as Entered in Error</td>
<td></td>
<td>Alt + M</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Cancel</td>
<td></td>
<td>Alt + C</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Create/Edit user templates</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>File</strong> Menu</td>
<td>Alt + F</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>New Template</td>
<td>W</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Delete</td>
<td>D</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Save</td>
<td>S</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Exit</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Vitals</strong> Menu</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Add</td>
<td>A</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Delete</td>
<td>D</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Down</td>
<td>W</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Up</td>
<td>U</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>User Templates</td>
<td></td>
<td>Alt + U</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Template Name</td>
<td></td>
<td>Alt + N</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Description</td>
<td></td>
<td>Alt + E</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Template Vitals</td>
<td></td>
<td>Alt + V</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Metric</td>
<td></td>
<td>Alt + M</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Up arrow icon</td>
<td></td>
<td>Ctrl + U</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Down arrow icon</td>
<td></td>
<td>Ctrl + W</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Plus sign icon</td>
<td></td>
<td>Ctrl + A</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Minus sign icon</td>
<td></td>
<td>Ctrl + D</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Delete</td>
<td></td>
<td>Alt + D</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Save</td>
<td></td>
<td>Alt + S</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>New Template</td>
<td></td>
<td>Alt + W</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Close</td>
<td></td>
<td>Alt + C</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Templates</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Name</td>
<td>Alt + N</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Description</td>
<td>Alt + E</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Up</td>
<td>Ctrl +U</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Down</td>
<td>Ctrl + W</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Add</td>
<td>Ctrl + A</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Delete</td>
<td>Alt + D</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Metric</td>
<td>Alt + M</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Default</td>
<td>Alt + L</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">User Preferences</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Defaults</td>
<td></td>
<td>Alt + D</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Apply</td>
<td></td>
<td>Alt + A</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>OK</td>
<td></td>
<td>Alt + O</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Cancel</td>
<td></td>
<td>Alt + C</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Text (Normal Values)</td>
<td></td>
<td>Alt + T</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Background (Normal Values)</td>
<td></td>
<td>Alt + B</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Text (Abnormal Values)</td>
<td></td>
<td>Alt + X</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Background (Abnormal)</td>
<td></td>
<td>Alt + G</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Search Delay</td>
<td></td>
<td>Alt + S</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">Report Options</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Select Report</td>
<td></td>
<td>Alt + R</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Patient</td>
<td></td>
<td>Alt + T</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Patients Located at</td>
<td></td>
<td>Alt + L</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Start Date</td>
<td></td>
<td>Alt + S</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>End Date</td>
<td></td>
<td>Alt + E</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Device</td>
<td></td>
<td>Alt + D</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Queue To Run At</td>
<td></td>
<td>Alt + Q</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Print</td>
<td></td>
<td>Alt + P</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Cancel</td>
<td></td>
<td>Alt +C</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="5"></td>
</tr>
<tr class="even">
<td colspan="2">Vitals Manager</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>File</strong> Menu</td>
<td>Alt + F</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Print Qualifiers Table</td>
<td>P</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Exit</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>System Parameters</strong> Menu</td>
<td>Alt + S</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Save Systems Parameters</td>
<td>S</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Abnormal Values</strong> Menu</td>
<td>Alt + B</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Save Abnormal Values</td>
<td>A</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Templates</strong> Menu</td>
<td>Alt + T</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>New Template …</td>
<td>N</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Save Template</td>
<td>S</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Delete Template …</td>
<td>D</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Set Default Template</td>
<td>E</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Qualifiers</td>
<td></td>
<td>Alt + Q</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Help</strong> Menu</td>
<td>Alt + H</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Index</td>
<td>I</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Contents</td>
<td>C</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Vitals Website</td>
<td>W</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>About</td>
<td>A</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">System Parameters</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Allow User Templates</td>
<td>Alt + U</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Help Menu Web Address</td>
<td>Alt + W</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Version Compatibility</td>
<td>Alt + V</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch GMRV*5.0*23 September 2009 Added Read Monitor shortcut key.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

*This page intentionally left blank for double-side printing.*

# Appendix B – Customizing the Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The client installation by default installs and builds the icons and program folder items without any command line switches. Vitals/Measurements utilizes the ServerList utility of the RPC Broker for selecting a server to connect to if it is configured on the client workstation. Instructions for configuration and utilization of the ServerList utility can be found in the RPC Broker documentation located on the VDL. If the ServerList utility has not been configured on the client, the applications by default will attempt to connect to the server identified in the users HOSTS file as BROKERSERVER on Listener Port 9200. Adding command line parameters to the shortcuts as shown below by right clicking the appropriate Vitals/Measurements application icon and selecting the Properties menu item can easily override these parameters.

![](vitals-version-5-user-manual/046.png)

Figure ‑

The above (Figure 7‑1) is a standard properties view of the Vitals icon as displayed when right clicking the icon. Select the Shortcut tab to proceed with customization.

![](vitals-version-5-user-manual/047.png)

Figure ‑

This example (Figure 7‑2) will attempt to connect the application to the server identified in your HOSTS file as *yourserver* and will use listener port 9200.

Vitals/Measurements V. 5.0 command line parameters available from the command prompt or within Windows shortcut definitions are:

> Vitals.exe \[/server=*servername*\] \[/port=*listenerport*\]  
> \[/tempdir=*temporarydirectory*\] \[/helpdir=*helpdirectory*\] [^47]\[/debug={on\|off}\] \[/noccow\] \[/ccow=patientonly\]

> VitalsManager.exe \[/server=*servername*\] \[/port=*listenerport*\] \[/helpdir=*helpdirectory*\]  
> \[/debug={on\|off}\]

<table>
<colgroup>
<col style="width: 0%" />
<col style="width: 21%" />
<col style="width: 53%" />
<col style="width: 24%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a><strong>Switches</strong></td>
<td><strong>Description</strong></td>
<td><strong>Example</strong></td>
</tr>
<tr class="even">
<td colspan="2">/server</td>
<td><p>Specifies an alternate server to connect to. The server must be defined in the clients hosts. file.</p>
<p>Default Hosts. file locations:</p>
<p>NT 4.0/W2K = c:\winnt\system32\drivers\etc\hosts.</p>
<p>Windows 9x = c:\windows\hosts.</p>
<p>Default = BROKERSERVER</p></td>
<td>/server=vista</td>
</tr>
<tr class="odd">
<td colspan="2">/port</td>
<td><p>Specifies an alternate listener port on the selected server. This is the TCP/IP port that the broker is running on VistA server.</p>
<p>Default = 9200</p></td>
<td>/port=9200</td>
</tr>
<tr class="even">
<td colspan="2">/tempdir</td>
<td><p>Location accessible to the client workstation and current user for storage of temporary scratch files.</p>
<p>Default = <em>application_directory</em>\temp</p></td>
<td>/tempdir=C:\temp</td>
</tr>
<tr class="odd">
<td colspan="2">/helpdir</td>
<td><p>Location of the Vitals/Measurements windows help files.</p>
<p>Default = <em>application_directory</em>\help</p></td>
<td>/helpdir=C: \help</td>
</tr>
<tr class="even">
<td colspan="2">/debug</td>
<td><p>Set the debug mode for both the RPC Broker and the Vitals/Measurements application.</p>
<p>Default = Off.</p></td>
<td>/debug=On</td>
</tr>
<tr class="odd">
<td>/noccow</td>
<td>The application will not check the CCOW context at all. This switch forces the user to sign on and select a patient when invoking the Vitals GUI.</td>
<td>/noccow</td>
<td></td>
</tr>
<tr class="even">
<td>/ccow=patientonly</td>
<td>The application will use CCOW, but will be set to check for patient context only. Automatic sign on will be disabled, but the automatic selection of a patient will be enabled. If a patient is selected in an open application, Vitals will automatically open the patient being used by that application.</td>
<td>/ccow=patientonly</td>
<td></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Patch GMRV*5.0*3 April 2006 Added /noccow and /ccow=patientonly switches and descriptions. Removed /brokertimout and /nonsharedbroker switches and descriptions as they are no longer available.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

*This page intentionally left blank for double-side printing.*

# [^48]Appendix C – Using Vitals in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch GMRV\*5.0\*3 provides a Dynamic Link Library (DLL) file that allows other applications to use a limited set of Vitals/Measurements features within their own applications. This DLL is currently used by CPRS v26 or later, and the features appear on screen as part of the Vitals Lite window.

The DLL name is GMV_VitalsViewEnter.dll and it is automatically installed as part of the patch. This DLL is not called by the Vitals.exe or VitalsManager.exe files that make up the Vitals Graphical User Interface (GUI), and it does not need to be registered in the Windows registry.

 

## Overview of Vitals Lite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the user clicks on the Vitals section of the CPRS Cover Sheet, the DLL is invoked and the Vitals Lite window opens. From this window, the user can:

- View patient vitals data in a graph and grid format.
- Select date ranges for retrieving data
- Select vital types, intake and output values (liquid values only) to plot on the graph
- Use zoom features to view the graph data
- Display numerical values for each point on the graph
- Display the graph in 3-D format
- Print a graph to a Windows-type printer
- View the qualifier abbreviations along with the numerical values in the grid
- View the name of the person who entered the data and the hospital location associated with the record in the grid (except for I&O values)
- Change the background color of the graph
- Enter vitals data using existing input templates
- Mark existing records as entered in error
- Display patient allergy data.

 

The following sections describe the Vitals Lite functionality in CPRS. See the *CPRS User Guide* in the VistA Documentation Library for more detailed information about CPRS.

## Opening the Vitals Lite window in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In CPRS, select a patient and open the Cover Sheet. Click anywhere inside the Vitals section to open the Vitals Lite window:

![](vitals-version-5-user-manual/048.png)

The Vitals Lite window displays the selected patient’s vitals and measurements in a graph and a spreadsheet-like grid. The next three sections describe how to view existing vitals, enter vitals, and correct vitals for this patient.

## Viewing Data in Vitals Lite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vitals-version-5-user-manual/049.png)

The time scale runs from left to right, displaying the most recent values on the far right side of the graph and grid. You can move left and right across the graph by moving the slider bar between the graph and the grid.

You can view patient data within a selected date range: “Six Months” is selected in the example above. Select a predetermined time frame by clicking one of the values on the left of the graph: “Today” displays today’s data only, “T-1” displays data for today plus one previous day, “T-7” displays data for today plus seven previous days, and so on. “All Results” displays all available vitals data for the selected patient. If you would rather define your own dates, click the Date Range button, then set "Start with" and "Go to" dates.

The patient data on the grid can also be viewed as a text report, by selecting Data Grid Report from the File menu.

You can view 15 different types of graphs for the selected date range. Select a graph type from the Graph drop-down list, or click a vital type row heading in the grid to graph that vital type. The TPR graph is selected in the example above, showing Temp, Pulse, and Respiration values.

Four Graph Options checkboxes are available on the left side of the graph. If the check boxes are not visible, right-click the screen (but not on the graph itself) and select Graph Options. This menu option may also be selected from the File menu.

- Click the Values checkbox to display a numeric label for each point on the graph.
- Click the Time Scale checkbox to view the graph in actual time instead of evenly distributed intervals. You can also click on a data point in the graph to see additional information about the vitals that were entered on that day.
- Click the 3D checkbox to create a 3D effect on the graph. This option is only available if the Time Scale checkbox is checked.
- Click the Allow Zoom checkbox to zoom the graph view in or out. You can zoom in by clicking inside the graph and dragging a selection box around one or more data values to view in detail, or by clicking the Zoom Graph In button (the magnifying glass icon with the plus sign in the center). You can zoom out by clicking the Zoom Graph Out button (the magnifying glass icon with the minus sign in the center.) Enter a new value in the Zoom Percent text box to change the zoom percentage (default is 10). Click the Reset Zoom button to reset the Zoom Percent box to its original value.

Two additional graph options can be accessed from this window. Right-click the screen (but not on the graph itself) to display these menu options, or select them from the File menu:

- Select Graph Color allows you to set the background color of the graph.
- Print Graph allows you to send the graph display to a printer. The graph will be printed as it appears on the screen at the time of printing.

The remaining right-click menu options (Entered in Error, Enter Vitals, and Allergies) are described later in this chapter.

You can view a report containing general patient information by clicking on the patient name button at the top left corner of the screen, or by selecting Patient Inquiry from the File menu.

## Entering Vitals in Vitals Lite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click the Enter Vitals button at the top of the Vitals Lite window. The Enter Vitals window for the selected patient opens:

![](vitals-version-5-user-manual/050.png)

> **NOTE:** If you have access to the Encounter button, the Enter Vitals window can also be opened from the CPRS Notes tab:

- In the Notes window, click the Encounter button and select an existing appointment or admission, or create a new one.
- In the Encounter window, click the Vitals tab, then click the Enter Vitals button to invoke the DLL and open the Enter Vitals window. The user will be able to enter vitals data using existing input templates.

[^49]The Enter Vitals window opens, showing the selected patient’s name, Social Security number, and date of birth in the upper left corner of the window. The selected Hospital Location and current Date/Time are also shown at the top of the window.

- [^50]Click the Read Monitor button to retrieve vital sign readings from a vital sign monitor (VSM) connected to the workstation.
- Click the Date/Time button to select a different date or time.
- Click the Hospital button to select a different hospital location.

The list of available vital types is determined by the template that is selected. Select a template from the Templates list on the left side of the window. See page [2-6](#creatingediting-a-template) for information about using the Vitals Manager module to create and update templates.

Enter values for the vital types by typing them in the appropriate box. The default qualifiers for each vital type appear to the right of the down arrow button for each vital type. To select a different qualifier, click the down-arrow button next to each vital type.

> NOTE: To enter a non-numeric value for a particular vital sign or measurement, use one of these options:

- Click Patient on Pass to mark all vital signs as "Pass" for this date/time.
- Click the U… checkbox next to any vital to indicate that information is unavailable.
- Click the R… checkbox next to any vital to indicate that the patient refused that measurement.

> The last two options are available only if the Enable U. and/or Enable R. boxes at the top of the Enter Vitals window are checked.

Click the Save button to save the data for these vital types. Click the Save And Exit button to save the data for these vital types and close the Enter Vitals window. Click the Exit button to close the window without saving any data.

## Correcting Vitals in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vitals data values cannot be deleted once they have been saved – if incorrect vitals data have been saved, they must be marked "Entered in Error" and replaced with corrected data. Any data values that have been marked "in error" will continue to be stored in the Vitals database, but will not be displayed in the patient’s data grid and graph.

Users can mark any vitals that were incorrectly entered as “entered in error” by using this procedure. Users will still need to go back and add a new entry to correct the entry that will be marked as entered in error.

Click the Entered in Error button at the top of the Vitals Lite window, or right-click on the grid and select Entered In Error from the pop-up window, or from the File menu. The Entered in Error window for the selected patient opens:

![](vitals-version-5-user-manual/051.png)

[^51]Note: Records entered through the Clinical Observations (CliO) package cannot be changed to Entered in Error here. They must be addressed in the CliO package.

Select a date by clicking the down-arrow button to display a calendar. The default date is today. October 9, 2005 is selected in the example above.

Select the incorrect vitals entry by clicking it – Pain is selected in the example above. You can select multiple entries by holding down the Ctrl key and clicking the entries to select them.

Select the reason the entry or entries are incorrect by clicking the appropriate radio button in the Reason section. Click the Mark as Entered in Error button to mark the vitals as entered in error.

You may now enter new vitals data to replace the incorrect entries, if necessary

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access Code A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.
ADP Coordinator / ADPAC / Application Coordinator Automated Data Processing Application Coordinator. The person responsible for implementing an application developed to support a specific functional area such as Nursing, PIMS, etc.
Application A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users. Examples of VistA applications are the PIMS and Vitals/Measurements application.
[^52]Application Data From a CCOW perspective, this is the patient record that is open in the active application. When joining a clinical context, select Use Application Data to force all open CCOW-compliant applications to switch to the patient that is open in the active application.
Archive The process of moving data to some other storage medium, usually a magnetic disk, and deleting the information from active storage in order to free-up disk space on the system.
Backup Procedures The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.
BMI A patient's body mass index, which is calculated by dividing the person's weight in kilograms by the square of his height in meters.
Bulletin A canned message that is automatically sent by MailMan to a user when something happens to the database.
CCOW Clinical Context Object Workgroup standard. CCOW provides a way for applications to know which other applications are running and which patients are selected in those applications. This standard allows for synchronization of patient data across all open applications.
Data Dictionary A description of file structure and data elements within a file.
DLL Dynamic Link Library
Device A hardware input/output component of a computer system (e.g., CRT, printer).
Edit Used to change/modify data typically stored in a file.
Field A data element in a file.
File The M construct in which data is stored for retrieval at a later time. A group of related records.
File Manager or FileMan Within this manual, FileManager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/ search related data in a file; a data base.
Global An M term used when referring to a file stored on a storage medium, usually a magnetic disk. In the Vitals software, for example, vitals data is stored in one global, and patient data is stored in another global.
[^53]Global Data From a CCOW perspective, this is the patient record that all CCOW-compliant applications are focused on. When joining a clinical context, select Use Global Data to synchronize the active application with the patient that is open in the other applications.
GMRV This signifies the General Medical Record namespace assigned to the Vitals/Measurements application.
GMRY This signifies the General Medical Record namespace assigned to the Intake and Output application.
GMV Vitals/Measurements namespace, parent package to GMRV.
GUI Graphical User Interface – a Windows-like screen that uses pull-down menus, icons, pointer devices, and other metaphor-type elements that can make a computer program more understandable, easier to use, allow multi-processing (more than one window or process available at once), and so on.
I&O The Intake and Output application.
IRMS Information Resource Management Service.
Kernel A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include: MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.
M Formerly known as MUMPS or the Massachusetts (General Hospital) Utility Multi-Programming System. This is the programming language used for all VistA applications.
MailMan An electronic mail, teleconferencing, and networking system.
Menu A set of options or functions available to users for editing, formatting, generating reports, etc.
Module A component of the Vitals software application that covers a single topic or a small section of a broad topic.
Namespace A naming convention followed in the VA to identify various applications and to avoid collision between applications. It is used as a prefix for all routines and globals used by the application. The Vitals package uses GMV as its namespace.
OIFO Office of Information Field Office, formerly known as Information Resource Management Field Office, and Information Systems Center.
Option A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions. For example, the GMV V/M GUI is the main menu for the Vitals/Measurements application.
Package Otherwise known as an application. A set of M routines, files, documentation and installation procedures that support a specific function within VistA (e.g., the ADT and Vitals/Measurements applications).
Password A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).
[^54]Patient Context From a CCOW perspective, a patient context session is created for a single client device with at least one CCOW participant "joined" to the context session. If a user is running Vitals and CPRS from a single workstation, each application is a participant in the patient context session, and when a patient record is open in one application, the same patient record is automatically opened in all other participating applications.
PIMS Patient Information Management System previously known as the MAS Package.
Pointer A special data type of VA FileMan that takes its value from another file. This is a method of joining files together and avoiding duplication of information.
Program A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
Protocol A single entry point referencing multiple routine entry points to execute several inter related, required processes which perform specific functions. When multiple protocols are associated with a single procedure (i.e., intravenous lines or IV lines), they are found grouped under a single option.
Qualifier A word that gives a more detailed description of an item.
Queuing The scheduling of a process/task to occur at a later time. Queuing is normally done if a task uses up a lot of computer resources.
Routine A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
Security Key A function which unlocks specific options and makes them accessible to an authorized user.
Sensitive Information Any information which requires a degree of protection and which should be made available only to authorized users.
Site Configurable A term used to refer to features in the system that can be modified to meet the needs of each site.
Software A generic term referring to a related set of computer programs.
Synonym A qualifier abbreviation appended to vitals/measurements numeric values on graphic reports.
Task Manager or TaskMan A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.
User A person who enters and/or retrieves data in a system, usually utilizing a CRT.
[^55]User Context CCOW allows users to authenticate and sign-on to multiple applications that are CCOW-enabled and User Context-aware using a single set of credentials. This reduces the need for multiple ID's and passwords in the VistA clinician desktop environment. If a user is running Vitals on a workstation and the CCOW user context is enabled, additional CCOW applications can be opened automatically without requiring the user to sign in again.
Utility An M program that assists in the development and/or maintenance of a computer system.
Verify Code A unique security code which serves as a second level of security access. Use of this code is site specific; sometimes used interchangeably with a password.
VistA Veterans Health Information Systems and Technology Architecture.
Vital Type A category of vital sign or measurement (e.g., pulse, respiration, blood pressure, temperature).
Workstation A personal computer running the Windows 9x or NT operating system.

# # Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A

Abnormal Values

appearance in Vitals, 3-4

set ranges for Vitals, 2-3

Access Keys, i, 6-1

Accessibility, 1-2

Add

a Vitals link to the CPRS Tools menu, 1-5

Qualifiers to Vitals types, 2-2

Templates, 2-6

Vitals for multiple patients, 4-10

Vitals for one patient, 4-3

Allergies

button, 3-2

view, 4-19

B

Break the Clinical Link, 3-5

Buttons, in Vitals windows, 3-2

C

Categories, 2-2

CCOW

break the clinical link, 3-5

overview, 3-4

rejoin the clinical context, 3-5

show status, 3-5

Context management, 3-4

Correct inaccurate Vitals Data, 4-20

CPRS, 1-6, *See* Vitals Lite

CPRS Tools Menu

add a link to Vitals, 1-5

Create a User Template, 4-14

Customize the Client Installation, 7-1

D

Data Grid Report, 4-3

Date/Time Selector button, 3-3

Delete Vitals. *See* Entered in Error

Division Template. *See* Vitals Manager

DLL, 8-1

Documentation, 1-2

E

Edit

Abnormal Values settings, 2-3

Qualifiers, 2-2

System Parameters, 2-4

User Options settings, 3-3

Vitals data, 4-20

Enter Vitals

for multiple patients, 4-10

for one patient, 4-3

Enter Vitals button, 3-2

Entered in Error, 4-20

Entering Vitals Data, 4-1

Expand View button, 3-3

G

Glossary, 9-1

Graph Options

setting, 4-4

Graphic Reports, 5-1

H

Hospital Selector button, 3-3

I

Installation

options to customize the client, 7-1

Intake / Output, 5-2

J

Join a clinical context, 3-5

L

Latest Vitals button, 3-3

Location Template. *See* Vitals Manager

M

Managing Site Files

Abnormal Values ranges, 2-3

Categories and Qualifiers, 2-2

Overview of Vitals Manager, 2-1

System Parameters, 2-4

Templates, 2-6

N

Navigation Bars, 3-2

O

Open

Vitals, 3-1

Vitals Manager, 2-1

Options

edit User Preferences, 3-3

Overview of GUI software, 1-2

P

Package Operation. *See* Using Vitals

Patient Selector button, 3-2

Preferences. *See* User Options for Vitals

Print

general patient information, 4-5

Qualifiers Table report, 2-3

Vitals reports, 5-2

Q

Qualifiers, 2-2

R

Rejoin Clinical Context, 3-5

Reports

overview of, 5-2

printing, 5-3

viewing data in a graph, 5-1

S

Security keys, 1-1

Shortcut Keys, i, 6-1

Show CCOW Status, 3-5

Site Files. *See* Vitals Manager

System Overview, 1-1

System Parameters, 2-4

System Template. *See* Vitals Manager

T

Templates

creating and editing, 2-6

selecting, 4-1

types of, 2-6

User, 4-14

U

User Options for Vitals, 3-3

User Template

create a, 4-14

delete a, 4-18

edit a, 4-18

V

Version Compatibility. *See* System Parameters

View

Allergies, 4-19

CCOW status, 3-5

general patient information, 4-5

Intake/Output values in a report, 5-2

Vitals data in a graph, 5-1

Vitals

application features, 1-1

enter data for multiple patients, 4-10

enter data for one patient, 4-3

link to the CPRS Tools Menu, 1-5

make corrections, 4-20

Overview, 3-1

overview of main window, 3-2

selecting a template and patient, 4-1

Vitals Lite, 8-1

Vitals Manager

create or edit a Template, 2-6

edit Abnormal Values, 2-3

edit System Parameters, 2-4

Overview, 2-1

print a Qualifiers Table report, 2-3

work with Categories and Qualifiers, 2-2

[^1]: Patch GMRV\*5.0\*3 April 2006 Included module and security information from former Installation chapter; added new information about the DLL.

[^2]: Patch GMRV\*5.0\*3 April 2006 Updated entire section for clarity and to reflect current functionality.

[^3]: Patch GMRV\*5.0\*23 September 2009 Deleted reference to archiving/purging and printing graphic reports and modified wording.

[^4]: Patch GMRV\*5.0\*3 April 2006 Added accessibility information for Section 508 compliance.

[^5]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture.

[^6]: Patch GMRV\*5.0\*3 April 2006 Removed the original Chapter 2 “Installation and Implementation”. Changed this chapter title from “Site Parameters” to more accurately reflect chapter content.

[^7]: Patch GMRV\*5.0\*3 April 2006 Combined “Adding Vitals Qualifiers” and “Associating Vitals Qualifiers with a Category” sections into new “Managing Vitals Categories and Qualifiers” section to reflect new functionality.

[^8]: Patch GMRV\*5.0\*23 September 2009 Deleted reference to graphic reports and modified references to qualifiers. Updated screen capture.

[^9]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture.

[^10]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture.

[^11]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture.

[^12]: <span id="_Ref118625402" class="anchor"></span> Patch GMRV\*5.0\*3 April 2006 Updated the template category descriptions for clarity.

[^13]: Patch GMRV\*5.0\*1 October 2003 “Template Vitals” added to screen capture

[^14]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture.

[^15]: Patch GMRV\*5.0\*1 October 2003 “Template Vitals” added to screen capture

[^16]: Patch GMRV\*5.0\*23 September 2009 Modified Figure 2‑10 and the following paragraph.

[^17]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture.

[^18]: Patch GMRV\*5.0\*3 April 2006 Changed chapter title from “Package Operation” to more accurately reflect the chapter content; updated this entire chapter to provide an overview of the GUI and its functionality, and added CCOW information.

[^19]: Patch GMRV\*5.0\*23 September 2009 Added Read Monitor description.

[^20]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture.

[^21]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture.

[^22]: Patch GMRV\*5.0\*3 April 2006 Updated the Pt Select menu item name.

[^23]: Patch GMRV\*5.0\*3 April 2006 New screen capture.

[^24]:  Patch GMRV\*5.0\*3 April 2006 Updated this entire section to reflect new functionality and GUI appearance: replaced all screen shots; updated Vitals window descriptions, features, and workflow; added descriptions of Graph Options and right-click menu options.

[^25]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture to include “Data Source” row.

[^26]: Patch GMRV\*5.0\*23 September 2009 Renamed Show/Hide Graph Options to Graph Options.

[^27]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture to include menu bar, “Data Source” column, and “Read Monitor” button.

[^28]: Patch GMRV\*5.0\*23 September 2009 Added “Read Monitor” button description.

[^29]: Patch GMRV\*5.0\*1 October 2003 New date/time format

[^30]: Patch GMRV\*5.0\*23 September 2009 Added “Enter Vitals Menu Bar” section.

[^31]: Patch GMRV\*5.0\*3 April 2006 Updated this entire section to reflect new functionality and GUI appearance: replaced all screen shots; updated Vitals window descriptions, features, and workflow; added description of CCOW.

[^32]: Patch GMRV\*5.0\*23 September 2009 Altered CCOW warning.

[^33]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture to include menu bar, “Data Source” column, and “Read Monitor” button. Added “Read Monitor” button description.

[^34]: Patch GMRV\*5.0\*23 September 2009 Screen redesigned.

[^35]: Patch GMRV\*5.0\*23 September 2009 Screen capture redesigned and buttons renamed.

[^36]: Patch GMRV\*5.0\*23 September 2009 Modified wording in first two sentences.

[^37]: Patch GMRV\*5.0\*3 April 2006 Reorganized the template editing options for clarity.

[^38]:  Patch GMRV\*5.0\*3 April 2006 Updated this entire section: added brief explanation of why Entered in Error is necessary; updated the procedure to include right-click menu and column-heading access options and alternate procedure flow; replaced outdated screen shots; added report-printing reference.

[^39]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture.

[^40]: Patch GMRV\*5.0\*23 September 2009 Added CliO package note.

[^41]: Patch GMRV\*5.0\*3 April 2006 Updated descriptions of graph and table; new screen capture

[^42]:  Patch GMRV\*5.0\*3 April 2006 Updated the Reports descriptions and printing requirements.

[^43]: Patch GMRV\*5.0\*23 September 2009 Updated report list.

[^44]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture.

[^45]: Patch GMRV\*5.0\*23 September 2009 Added note about report updates.

[^46]: Patch GMRV\*5.0\*3 April 2006 Updated entire Access Keys chart; added Shortcut Keys columns.

[^47]: Patch GMRV\*5.0\*3 April 2006 Added examples for new /noccow and /ccow=patientonly switches.

[^48]:  Patch GMRV\*5.0\*3 April 2006 Added Appendix to describe new DLL functionality.

[^49]: Patch GMRV\*5.0\*23 September 2009 Updated screen capture.

[^50]: Patch GMRV\*5.0\*23 September 2009 Added “Read Monitor” button description.

[^51]: Patch GMRV\*5.0\*23 September 2009 Added CliO package note.

[^52]: Patch GMRV\*5.0\*3 April 2006 Added definitions for Application Data, CCOW and DLL.

[^53]: Patch GMRV\*5.0\*3 April 2006 Added definition for Global Data.

[^54]: Patch GMRV\*5.0\*3 April 2006 Added definition for Patient Context.

[^55]: Patch GMRV\*5.0\*3 April 2006 Added definition for User Context.