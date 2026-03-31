---
title: AICS Version 3 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: IBD
app_name: Automated Information Collection System (AICS)
section: FIN
app_status: active
pkg_ns: IBD
patch_ver: 3
patch_id: IBD*3
group_key: "IBD:IBD:3"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Critical Elements of a Scannable Form](#critical-elements-of-a-scannable-form) - [New Options](#new-options) ![](aics-version-3-release-notes/001.png) aUTOMATED iNFORMATIONCOLLECTION SYSTEMAICSRELEASE NOTES April 1997 Health Systems Design & Development (HSD&D) Table of Contents I. Introduction 1
audience: 
keywords: 
  - form
  - aics
  - paper
  - keyboard
  - workstation
  - forms
  - scanner
  - scanning
  - software
  - image
page_count: 0
word_count: 7569
section_count: 1
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Info_Collection_Sys_(AICS)/aics3_0rl.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Auto_Info_Collection_Sys_(AICS)/aics3_0rl.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=30"
---

## Table of Contents

    - [Critical Elements of a Scannable Form](#critical-elements-of-a-scannable-form)
    - [New Options](#new-options)
![](aics-version-3-release-notes/001.png)
aUTOMATED iNFORMATIONCOLLECTION SYSTEMAICSRELEASE NOTES
April 1997
Health Systems Design & Development (HSD&D)
Table of Contents
I. Introduction 1II. Client 3
> Overview 3
> Critical Elements of a Scannable Form 4
> Workstation Setup 5
> Communications 7
> New Features 7
> Example of the AICS Workstation Software 8
> Use of Paper Keyboard 12
> Exception Handling 13
III. Server 15
> New Options 15
> Changed Options 15
> New Blocks 18
> New Files 19
> New Fields 19
> New Protocols 20
> New Security Keys 20
> New Package Interface 20
> Changed Forms 20
IV. Appendix - Scanner Calibration 21
I. Introduction
AICS V. 3.0 will introduce a complete solution to the scanning of Encounter Forms designed by the M-Server side of AICS and the subsequent transmission of the encounter data to PCE for storage. This is a very complex process requiring four main components we need to understand in detail. The four components are:
1.  AICS V. 2.1 Forms Design/ Forms Printing/ Forms Definition/ Forms Tracking,
1.  AICS V. 3.0 Workstation Software,
1.  AICS V. 3.0 Server software,
1.  Paper Keyboard, a commercial scanning software package from Datacap, Inc.
Many changes and enhancements on the V*IST*A (Server) side have been added in this version of AICS to make this package more efficient and user friendly.
II\. Client
Overview
The process of developing scannable Encounter Forms is nearly complete at most medical centers. They have installed AICS V. 2.1 and have begun converting their forms to a scannable format. AICS V. 2.1 Forms Design software and AICS V. 3.0 Server Software are the parts of the process that reside on the traditional M V*IST*A environment. In GUI software development we refer to this as the Server. The AICS V. 3.0 workstation software and the commercial product Paper Keyboard reside on Windows based PCs. This is referred to as the Client. The purpose of the AICS V. 3.0 workstation software is to:
1.  Provide a consistent user interface,
1.  Handle communications between the client and the server,
1.  Control the Scanning process and provide site configurable operations,
1.  Handle communication with Paper Keyboard.
The process was designed to be simple to operate from a user perspective. When scannable forms are printed, they automatically update the Form Definition file and the Form Tracking file. After the form is completed, the user signs into the workstation software, puts the form into the scanner, and clicks Start. That’s it. At this point the data is now stored in PCE and/or Scheduling.
From a technical perspective this is much more complicated. From the point the user clicked start, a number of separate operations occurred. Most of the operations can return errors or alternate actions if not successful. The following is a list of the operations as they occur.
1.  AICS workstation gives Paper Keyboard (through DDE) consecutive commands.
    1.  Open the master form spec file (we’ll discuss form spec files later.)
    2.  Scan the page.
    3.  Save the image as TEMP.TIF, if duplex scanner, repeats b and c to save back pages as btemp.tif, then reloads temp.tif image to process first page.
    4.  Recognize the page.
    5.  If it can’t find the scannable page block, it rotates the form 180 degrees and repeats Step 1d. (Only does this once per image.)
2.  Paper Keyboard responds.
    1.  If a form spec for the form design does not exist, it requests it.
    2.  Sends the form ID to the workstation.
    3.  Jumps to the form spec file for the form design.
3.  AICS Workstation gives Paper Keyboard command to save image as appropriate.
4.  AICS Workstation hangs while form spec file loads.
5.  AICS Workstation sends second recognize command to Paper Keyboard.
6.  Paper Keyboard responds with data.
7.  AICS Workstation sends the data to the AICS Server.
8.  AICS Server:
    1.  Formats the data for PCE,
    2.  Sends the data to PCE (this is in itself a complex process),
    3.  Reviews errors and warnings that were returned,
    4.  Updates Forms Tracking,
    5.  Expands data to human readable format and returns it to the AICS Workstation.
9.  Paper Keyboard automatically jumps back to Master Form Spec.
10. AICS Hangs while FORM SPEC file loads.
11. Go to Step 1.
As you can see there are a number of issues that need further discussion. These include discussion of critical elements of a Scannable form, workstation setup/files/file types, communication, use of the AICS workstation software, use of Paper Keyboard, and exception handling.
Prior to beginning scanning you should check each form to make sure that the form design is compatible with scanning. The easiest way to do this is to print an Encounter Form for an appointment and use one of the AICS Manual Data Entry options to enter the data from the form. Manual Data Entry uses the form design very similarly to the way scanning uses the form design. If data passes correctly using Manual Data Entry, then the form design should be scannable.

### Critical Elements of a Scannable Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AICS uses a technology called Image Scanning. A complete image of the form is created and displayed in Paper Keyboard. Three types of recognition are used to find data on the form.
1.  Optical Mark Recognition (OMR) is used to identify predefined areas that have been written in or colored in. This includes the bubbles printed on the AICS forms.
2.  Optical Character Recognition (OCR) is used to read pre-printed characters on the page, such as the Form Design Number.
3.  Intelligent Character Recognition (ICR) is used to read hand print (not cursive writing) from predefined blocks on the form. (These blocks are often called combs.)
There are certain elements that are included on every form. They are: anchors, form design number, printed form ID, page, checksum values, and scan mark.
> **NOTE:** Before scanning can be done the scanner must be calibrated. The Appendix at the end of this manual lists the steps to take in order to calibrate your scanner.
Workstation Setup
<u>Installation of Scanner</u>
Installation of scanners should be done by someone comfortable with installing new hardware on a PC. Each scanner will require one or more interface cards that should already be installed. There are three common types of interface cards: a SCSI card, such as that used by the HP Scan Jets; Kofax Interface cards, such as those used by the Bell & Howell scanners; and the Dunord controller, such as those used by the Fujitsu. Some scanners can use more than one type of controller. Most duplex scanners use two cards; for example, the Bell & Howell CopyScan II uses two Kofax cards. Most of these cards also require installation of software that may want to know IRQs, IO Address ranges, or other hardware settings. Most are documented moderately well.
<u>Installation of Paper Keyboard</u>
Workstations will come with Paper Keyboard installed. If not, Paper Keyboard has its own installation software and it is a fairly straightforward windows install. It is recommended that the software be installed in the default directories. As part of the install the user is asked if they will be designing forms on the workstation. For AICS they should answer that they will not be designing forms. In order to complete the install the user will need to know information about the scanner attached to the PC. A hardware key is shipped with each manual. These must be installed on the parallel port of the workstation. Another device, such as a printer, can also be installed on the end of this key.
<u>Installation of RPC Broker</u>
The RPC Broker should be installed on the workstation prior to installation of the AICS workstation software. Successful installation can be tested with EGCHO.EXE that will allow the user to sign on to V*IST*A and perform various demonstrations. (See the RPC Broker documentation for correct installation procedures.)
<u>Installation of AICS Software</u>
The AICS workstation software will be loaded using a standard windows setup routine built using the Wise Installation software. The files will be stored in the VISTA /AICS directory. This includes the files IBDSCAN.EXE, the main executable, and the IBDABT.DLL. Parameters for the software will be stored in the AICS section of the Vista.ini file. The on-line tutorial files are stored in VISTA \AICS\Tutorials\\ They are: Ibdcalib.exe, Ibddemo.exe, Ibddhcp.exe, Ibdpref.exe.
<u>Form Spec Files</u>
The AICS workstation software controls Paper Keyboard through a combination of DDE and Form Spec files (\*.fs). There are two different master form spec files that will be exported, AICSMSTR.FS and AICSSCAN.FS. (They implement two different workstation modes of operation.) In addition, every form design gets a uniquely named form spec file. Currently, these are named EFnnnnnn.fs, where nnnnn is the form design number printed on the form. These \*.fs files are stored in the root directory of Paper Keyboard, as that is where it expects to find them (\paperkey.) The EF\*.FS files are generated on the fly by the server and are uploaded to the workstation, transparent to the user.
<u>Image Files</u>
Images from the scanning software are stored in a directory specified in the parameters. The default directories are Vista/AICS/Images and Vista/AICS/Unrf (unrf := unrecognizable forms.) Each workstation can enter a single uppercase workstation ID (A to T.) The images are stored as Type + workstation ID + Form ID + Page .TIF. Type is either null, if saved during scan only operations; "V", if stored as Validation Required during unattended operations; or "U", if an unrecognizable form. (An unrecognizable form is a scannable form where either the form design, form ID, or page number was null, zero, or didn't match its check sum or didn't match in the form tracking file.) Image VA3441.tif would be page one of form id 344 (unique to patient/form/appt) from workstation A and requires user validation. Some medical centers have indicated that they may store Image files on a network drive and use a single workstation/user to do validation.
<u>File Maintenance</u>
There are options available to allow deleting of form spec(\*.FS) and image(\*.TIF) from the AICS workstation software.
Communications
There are two types of communications in use in the AICS workstation software. The AICS workstation communicates to the AICS Server and V*IST*A through the RPC Broker, recently released by the Kernel. In addition, the AICS workstation software communicates with Paper Keyboard through the use of Dynamic Data Exchange (DDE) supported by Windows message handlers.
New Features
1.  Provides client/server based full image scanning on a PC workstation. Connection to the host computer system (server) is via TCP. Scanning utilizes Optical Mark Recognition for selection of items on a pick list, Optical Character Recognition to read the form and patient identification fields, and Intelligent Character Recognition to read hand print in special boxes and combs.
1.  AICS's client (workstation) user interface was built using Borland's Delphi, a commercial GUI development tool, integrated with a commercial scanning and forms processing software package (Paper Keyboard by Datacap.)
1.  Delphi allows the user of the AICS scanning software to see a windows-based application for the scanning front end including point and click mouse recognition instead of the traditional V*IST*A menu/option/keyboard based processing. It handles security and data communications between Paper Keyboard and the server system.
1.  Paper Keyboard is an image scanning product that provides a number of features, including the ability to create its FORM SPECIFICATION file on the server (V*IST*A) and to automatically upload it to the client workstation. Sites are allowed a number of configurations. Scanning, forms validation, and user validation of forms can be combined or separate functions. Unattended modes will allow the site to maximize the use of personnel.
To access the scanning software, a user must have the IBD SCANNING WORKSTATION option as a secondary menu option assigned to them within V*IST*A.
Data scanned for each encounter will be sent to PCE in a seamless integration just as in manual data entry.
Example of the AICS Workstation Software
The AICS workstation software was designed to be simple to use. Scanning is performed via the Scanning Work Center screen. This is the main AICS workstation screen. From here you can see the settings of the current parameters being used, the status of Paper Keyboard, and data from the form currently being used. There are a number of menus and options that can be accessed from this screen, many of them accessed via speed buttons on the tool bar. In addition, a few of the most common processing statistics are displayed at the bottom of the screen.
Scanning Work Center
![](aics-version-3-release-notes/002.png)
After starting the AICS workstation software, the user must log on to V*IST*A to create a connection. If Paper Keyboard is not running, AICS will start it. Most of the AICS functionality requires that the user is logged in and Paper Keyboard is running. To start Scanning, all the user has to do is click on the Start button. Processing should then proceed according to the workstation preferences. The Stop button will allow for interruption of processing when a continuous scanning mode is in affect. A new page is added to the scanning work center for each page scanned. The processing steps and results of scanning are displayed for each image scanned.
Preferences Screen
![](aics-version-3-release-notes/003.png)
The workstation parameters may be edited in the Preferences window. There are four workstation modes.
1.  Centralized scanning performs the full Scan, Recognize, Validate, Transmit cycle of operations for multiple forms, as might be done in a centralized scanning area. It uses a continuous scan mode, where it will continue to scan new pages as long as the scanner contains paper.
2.  Decentralized scanning performs the same process as centralized processing, except for one form at a time, as might more commonly occur in a clinic area.
3.  The workstation mode of scanning only performs the scan, recognize, and save image functions.
4.  The Validation Workstation mode allows the user to load images previously saved, and perform the validation and transmission steps for each form.
AICS also supports a network configuration. Forms can be scanned in one location and the images saved to a network drive. One or more Validation workstations could then read the images from multiple scanning stations. Sites choosing to run a network configuration should edit the path for images to the correct network path. Each workstation is assigned a workstation identifier. This is a single uppercase alpha from A to T. This identifier is used in the name of the images saved. For sites running a network configuration, this may be a primary indication of where the image came from.
Checking Attended operations puts Paper Keyboard into an interactive edit mode. Bubbles on the form not completely filled out, misaligned forms, or hand print fields can all cause Paper Keyboard to prompt the user. When running in unattended mode, any forms requiring user validation are automatically stored as images for processing later. Initial use of AICS should be in attended mode. As operations smooth out, sites may want to explore use of unattended mode to maximize staff time.
Many of the parameters are mutually exclusive. Turning Export Data to V*IST*A off will allow users to practice scanning without sending data to V*IST*A. When running the workstation in Validation mode the parameter to Save Images can not be turned on.
The parameter to show raw data will cause the data as sent from Paper Keyboard to the AICS workstation software to be appended to the bottom of the display for each page. This is a useful validation and debugging tool. One can see the number of data items sent from the scanning software to the workstation and compare this to the results of scanning. In addition, one can usually decipher the data from the bubbles by reviewing the Form Definition file and the Form Tracking file.
Statistics Screen
![](aics-version-3-release-notes/004.png)
Use of Paper Keyboard
Users will need to interact with Paper Keyboard in a number of ways. Primary interaction will be during interactive edit of forms. Paper Keyboard recognizes each field with a confidence level. If the confidence level is below that specified in the form spec, a user will be prompted to verify the result. In addition, the selection rules specified in forms design are enforced by the FORM SPEC file. If the primary provider field has a selection rule of exactly one and two bubbles are checked, then Paper Keyboard will prompt the user to resolve the discrepancy.
On the View menu are several parameters. Show Bounds and Auto Scroll should be checked. The Actual size magnification should work fine, though users may want other settings.
On the Edit menu is a Preferences Option. Operational Control should be Manual. Run Programs, Interactive Edit, and Export Data should be checked.
Users should become familiar with the Scanner Settings option found on the Edit Menu to calibrate the scanner. Calibrating the scanner is done by trial and error. An image is scanned and then the upper left anchor is located by modifying the vertical and horizontal offsets. The right top anchor is then located by modifying the horizontal calibrated units. The bottom anchors are then located by modifying the vertical calibrated units. This is repeated until settings are found that allow for consistent location of anchors.
Forms that have been copied by a copier will probably not be scannable. Because it is nearly impossible to copy a page exactly square, there is significant probability that Paper Keyboard will not find the anchors of the form. In addition, each time a page is copied there is some distortion of the image. This distortion can also cause misreading of the data on the form. During early testing we were warned that changes in the size of the paper as small as that caused by changes in humidity could affect the reliability of scanning. While we have not found this to be true, the AICS implementation is one with a small margin of error.
Exception Handling
There are three areas where exception handling comes into play, on the workstation during scanning, on the AICS Server, and while PCE attempts to store the data. The most common types of exceptions will be those returned by PCE for missing or inaccurate data. These exceptions are stored by PCE and the fact that an exception occurred is stored in the Forms Tracking file. Errors that occur in the AICS Server software generally are due to database problems or when conflicts in data cannot be resolved. Partial data may be passed to PCE. Both PCE and AICS errors and warnings are stored in the AICS ERROR AND WARNING LOG file (#359.3) and can be printed from the server and viewed on the client.
Generally if some condition exists during scanning and recognition that causes the recognition of a form to fail in Paper Keyboard, the image is stored and named as described above. These images can then be reloaded into Paper Keyboard and an attempt made to resolve the problem. If the problem cannot be resolved, Paper Keyboard supports printing of the image so that data entry can be performed via any of the existing options.
III\. Server

### New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IBDF EF FORM COMPONENTS
A new List Manager display has been added to the package. This new display lists the contents of a form (without displaying them.) It lists the contents of each block, the name of the block, starting row and column, width and height of the block. Two actions are included on this screen, EX Expand Item and BC Block Components. Expand Item allows the user to do an inquiry of the block and its components listed in the Block file (#357.1.) The Block Components action gives the user a more exact makeup of the block and the data it displays. It lists the component, it’s type (selection list, hand print field or data field), row, column, and block separators. For selection lists, it also lists the subcolumn information, the Type (text or marking), Data (code, short description), Width of the subcolumn, Qualifier, Selection Rule, and whether it is editable.
IBDF PRINT ERROR LIST
A new report has been added to the Reports and Utilities menu that will list all errors that occurred during scanning of forms. Both AICS and PCE have the ability to reject all data or partial data from the scanning of Encounter Forms. All errors are stored in the AICS ERROR AND WARNING LOG file (#359.3). These errors can be listed by the date that the error occurred and then by user allowing sites to pull the associated Encounter Forms and correct the encounter data using one of the data entry methods.
IBD SCANNING WORKSTATION
This new option will be transparent to most users, but it must be given as a secondary menu to users who will be using the scanning software.
Changed Options
IBD MANUAL DATA ENTRY
The three manual data entry options have been modified to allow entry of provider if a provider block is on the form but no providers are specified for the clinic. In addition, if the parameter to send data to PCE is set to send in the background, a new resource device will be used so that the number of jobs created is manageable.
Manual Data entry requires that the forms are scannable, requiring the same as scanning. If you are using the Forms Data Entry, users are told that they cannot do data entry if the form is not scannable. If using one of the other data entry methods, non-scannable forms are skipped. Also, if a block does not have bubbles for marking areas, it is skipped in data entry. Please make sure, if using data entry, that your forms are scannable.
IBDF BACKROUND JOB
The main print job, the Automatic Print Queue, now excludes test patients (those patients whose SSN is made up with five leading zeros.) Patch DG\*5.3\*72 provides a standard way in which to enter and identify test patients in a production account. The evening print job should not contain printed Encounter Forms for test patients. The manual print options do not exclude the printing of test patient Encounter Forms, so that in the event testing needs to be done using a test patient, the Encounter Form can be printed.
The ability to specify a time to print has been added as a parameter to the Queuing Parameters screen for the Automatic Print Queue. This allows a parameter group to print at different times each evening. A new field has been added to the ENCOUNTER FORM PARAMETERS file (#357.09) under the PRINT MGR'S QUEUING PARAM NAME field multiple(#11). The new field is TIME QUEUED (#13). The Queuing Parameters screen now displays the time queued after the device prompt (Device/Time Queued: ). The Add and Edit actions prompt for this new field so the user can input the time queued.
The PF Print Forms One Group action prints the Encounter Forms when the action is called and disregards the Time Queued parameter.
IBDF EDIT CLINIC REPORTS
A new field has been added called DON’T USE PCMM PROVIDERS. Normally AICS defaults to using PCMM providers if they exist for a clinic rather than using the providers in the clinic setup. Answering YES to this new field will cause AICS to not use the PCMM providers. This has been requested by sites trying to implement PCMM but who have not completed the setup.
IBDF EDIT ENCOUNTER FORMS
The ability to ask for an alternative narrative and clinical lexicon has been turned on in V. 3.0. Two new fields have been added to File \#357.95. Field \#2.01 stores the Alternative Narrative, and Field \# 2.02 stores the Clinical Lexicon. Changes were made to the list template \[IBDF QUICK SELECTION EDIT\] to allow for the display of these two new fields and changes were required to allow the add and edit actions to collect the data. Changes were also made to allow moving of the information to Forms Tracking and PCE. Both Data Entry and Scanning will now pass this data to PCE.
Changes to the resequencing of selection lists have been incorporated in this release. The user is now given the choice to resequence one or any number of groups within the block or resequence the entire block. The Fast Selection Edit action screen allows the user to resequence by groups and not blocks (RS Resequence Group.) A new List Manager protocol has been added to allow for this (IBDF QUICK GROUP RESEQUENCE.)
An additional enhancement to the resequencing allows the user to resequence either the whole group or block taking into account the place holders or disregarding them. Some users use the place holders as additional narrative (disregard the place holder) and some use this place holder field as subheaders or separators for related data (taking into account the place holder as a separator.) The same type of resequencing that has always been there is still the same. Users can resequence alphabetically or numerically. There have also been changes to the edit template \[IBDF EDIT PLACE HOLDERS\]. This closes E3R \#8926.
CPT multipliers have been added. When editing a CPT type block, the Forms Creator is now given the ability to enter a quantity for any given CPT code. Leaving the quantity field blank will pass through one occurrence of the code. Filling in any number greater than one in the quantity field will result in the narrative being updated to reflect the quantity selected. When CPT codes are passed to PCE, if a quantity has been entered, it will be passed along for storage in the encounter.
The ability to pass along more than one Diagnostic Code when only one code has been bubbled is now available. The Forms Creator is now given the ability to select a second and/or third code to pass along to PCE when the original code is bubbled. It is important for the Forms Creator to affect the narrative text so that Practitioners are aware that multiple codes will be passed to PCE. AICS does not automatically alter the text in this instance.
IBDF SETUP AUTO CLINIC PRINT
Under this option there is an action to pull up the Clinic Group Menu. This is where you can enter/edit Clinic Groups. Under the Add and Edit Clinic Group actions there is a new wildcard feature when entering clinic names. If the user adds part of the name of the clinic followed by a " \* ", all of the clinics with the same beginning letters before the " \* " will be added to the Clinic Group.
IBDF FORMS TRACKING
Forms Tracking enhancements have been added for this version of AICS. Now the user has the ability to obtain a report by requesting Clinic Groups. The user will now only have to put in the name of the Clinic Group instead of each clinic individually. The report will now allow the sort to be by Patient, Clinic, or Clinic Groups. Closes E3R \#8699.
This report now has the option to be printed to the screen or to a device.
Another enhancement is that it now lists by date order within the clinics. Closes E3R \#8700.
Two new actions have been added to the screen for Forms Tracking. The addition of Delete Entry (DL) allows the user to delete a Forms Tracking entry. To delete any entry the user must have the IBD MANAGER key. If the user does not have this key, deletion will occur only under certain conditions. The addition of the Rel Forms w/Lost Pages (RL) action allows the user to release the data to PCE without delay due to pending pages.
The Statistics Report now includes the \# and % of forms entered through Data Entry (DE) and \# and % sent to PCE.
IBDF UTIL MAINTENANCE UTILITY
This option now allows the user to search for and display active codes on forms. The user will be prompted for the code to search for and all forms that have that code will be displayed to the screen.
New Blocks
PRACTITIONER (V3.0)
Tool kit block name and headers have been changed from Provider to Practitioner, and a secondary practitioner bubble has been added to the block. This caused a new toolkit block to be added.
HIDDEN CLASSIFICATIONS (V3.0)
A Scannable Hidden Service Connected Questions block has been added. The block prints only those Service Connected questions that are applicable for a given patient. Two marking area type sub-columns exist for the bubbling in of YES or NO as answers to the Service Connected questions.
PATIENT IMMUNIZATIONS (V3.0)
By adding qualifiers to this toolkit block, a new block was created.
EYE ART I V. 3.0
This new block contains pictures of eyes for Ophthalmology Clinic.
EYE ART II V. 3.0
This new block contains pictures of eyes for Ophthalmology Clinic.
New Files
The new file, AICS ERROR and WARNING LOG (#359.3), was added to track errors that occurred during scanning so that sites could list the associated forms and correct the encounter data.
New FieldsFILE 357.95
2.01 ALTERNATIVE NARRATIVE
2.02 CLINICAL LEXICON
2.03 SECOND CODE
2.04 THIRD CODE
FILE 357.09
.08 FILL % FOR BUBBLES
.09 BACKGROUND % FOR BUBBLES
.1 DAYS TO PRINT 1010F
1.02 STOP DEFAULTING C/O DATE/TIME
> (This new parameter should be filled in if the user does not want the scanning software to default the checkout date/time to that of the time of scanning if there is not a checkout date/time in PCE or no checkout date/time on the Encounter Form.)
> \*\*\*PANDAS sites must enter YES at this prompt.\*\*\*FILE 409.95
.1 DON'T USE PCMM PROVIDERS
New Protocols
IBDF QUICK GROUP RESEQUENCE
This protocol allows the users to resequence by groups only. It is accessed under the FS Fast Selection Edit action.
New Security Keys
IBD MANAGER
This key should be allocated to users who need to perform functions in AICS that should not be allocated to all users of the package. Currently, holders of this key will be allowed to delete any Forms Tracking entry, while other users will only be allowed to delete entries meeting specific criteria. This key also allows the user to use the Rel Forms w/Lost Pages action on the Forms Tracking option display screen. Holders of this key are also prompted for additional scanning parameters in the Edit Site Parameters option: Fill % For Bubbles and Background % For Bubbles.
IBD SCAN MANAGER
This key must be assigned to users who use the AICS Workstation software and scan Encounter Form data to V*IST*A.
New Package Interface
DG 1010F PRINT
This will print a 1010F with the Encounter Form if a new Means Test or Copay Test is due within the number of days you specified in the AICS Parameters (the default is 30.)
Changed Forms
WORK COPY
Renamed Garbage form to the name Workcopy
IV\. Appendix - Scanner Calibration
Paper Keyboard is the proprietary software that was chosen to interface the AICS workstation with a scanner. Many different types of scanners may be used, and as a result of the differences between them, it may be necessary to calibrate your scanner with Paper Keyboard. Calibration should only be necessary under the following circumstances.
1.  Initial scanner hook-up on a workstation.
1.  Scanner is replaced at a workstation.
1.  Sheet feed mechanism is added or removed from the scanner.
1.  Paper Keyboard continually cannot recognize anchors on your form, forcing you to manually locate them.
    In order to calibrate Paper Keyboard with your scanner, it is necessary to understand the components on a form that make it scannable. They are:
1.  Anchor Marks: used to align the form,
1.  Scannable Page Block: used to determine if the page is scannable,
1.  Form, ID and Page Numbers: used to recognize the form being read.
![](aics-version-3-release-notes/005.png)
During scanning, a Form Specification file is loaded that tells Paper Keyboard where to look for the anchors and scannable page block on a form. Paper Keyboard will attempt to locate these items in order to align the form before recognizing the data on the form. Sometimes, due to variations in scanners and/or shrinkage of forms, Paper Keyboard will not be able to locate these items. Calibrating Paper Keyboard with your scanner upon initial setup should prevent this from occurring. To calibrate the scanner, you should follow these steps:
1.  Select a form to calibrate from.
1.  Use a form that has actual printed patient data.
1.  Do not use a form that does not have a FORM or ID number located on the top of the form.
1.  If you are using a Bell & Howell scanner on this workstation, AND you will be using the duplex feature (reading both sides at once), select a form that has been printed duplex with a short-edge binding (form is printed head to toe on both sides of the paper.)
1.  You do NOT need to calibrate for each different form you have. You are simply selecting a form to use as a guide.
1.  Start up the AICS software.
2.  Highlight the key located in the upper left-hand corner of the AICS window. This will result in a sign-on to V*IST*A. It is necessary to be signed-on to V*IST*A to calibrate your forms, since any file specifications not already resident on the workstation will automatically be retrieved from V*IST*A during the calibration process.
3.  Select the Options menu from the menu bar located at the top of the screen.
4.  From the Options menu, select Preferences.
5.  From the Preferences screen, select the Advanced button located at the lower right hand corner of the window.
6.  You are now in the AICS Advanced Preferences window. You MUST calibrate your scanner twice. The first time through, you will calibrate for a normal page orientation, and the second time through you will calibrate for a rotated page orientation. This will allow Paper Keyboard to read your form whether it is fed in right-side-up or up-side-down. Select the page orientation you wish to calibrate for by pressing the appropriate button:
1.  Calibrate Normal Scanner Settings, or
1.  Calibrate Rotated Scanner Settings.
7.  You are now prompted to be sure the paper is in the scanner. To determine which way your paper should be facing, see the following chart.
<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><strong>Normal Calibration</strong></th>
<th><p><strong>Rotated</strong></p>
<p><strong>Calibration</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Hewlett Packard</td>
<td>Front side of EF facing up and positioned upright in the scanner</td>
<td>Back side of EF facing up and positioned upside down in the scanner</td>
</tr>
<tr class="even">
<td>Bell &amp; Howell</td>
<td>Front side of EF facing up and positioned upright in the scanner</td>
<td>Front side of duplexed short-edge binding EF facing up and positioned upright in the scanner</td>
</tr>
</tbody>
</table>
9.  The Scanner Settings dialogue box should be displayed on your screen. For the time being, we will simply close this window.
    Click the Cancel button located at the bottom of the window.
10. The form image should be visible on your screen. You may maximize the window for ease of viewing.
11. To determine whether you need to turn off duplexing, refer to the following chart. If you do not need to turn duplexing off, proceed to the next step.
|                 | Normal Calibration | Rotated Calibration   |
|-----------------|------------------------|---------------------------|
| Hewlett Packard | Not applicable         | Not applicable            |
| Bell & Howell   | Turn off duplexing     | Do NOT turn off duplexing |
> To turn off duplexing if applicable:
1.  Select the Edit menu from the menu bar;
1.  Choose Scanner Settings from the pop-up menu;
1.  If the Double Sided box is checked, you must click on it to turn it off;
1.  You MUST remember to turn this back on before you save your configuration. You will be alerted to turn this feature back on in a later step.
12. If you are using a Bell and Howell scanner and you are calibrating for a rotated page orientation, you will need to click the scan button to retrieve the image of the second page.
1.  Click the button on the left hand side of the screen that looks like a scanner.
1.  Once the image is loaded, you will be looking at the back side of your form.
12. What to look for on the image.
1.  On this first pass, you are working with a Master Form Specification. This file only knows about a few items on your form. They are:
1.  Anchors,
1.  Form \#,
1.  ID \#,
1.  Checksums,
1.  Page \#,
1.  Scannable page block.
1.  Be sure that you can see each of these items clearly. If they are too dark (ink appears blotted), or too light (image appears to fade out), you may need to adjust your scanner brightness. To do so:
1.  Click Edit on the menu bar,
1.  Select Scanner Settings from the pop-up window,
1.  Alter the brightness setting by dragging the center block in either direction,
1.  Click OK to accept new settings,
1.  Click on the box that looks like a scanner, located on the left side of the Paper Keyboard screen. Be sure you put the paper back into the sheet feeder of your scanner the same way you did in Step 8.
1.  Check your brightness again. If you are not satisfied, you should repeat this step until your brightness settings are acceptable.
1.  Surrounding each of the first 5 items, you should see a red box. This is the location that Paper Keyboard is looking for for these items. On the last item (Scannable page block), you should see a red square within the black block on the form.
1.  Within the boxes that surround your page anchors, you should see a red cross-hair. This cross-hair should be positioned on top of your anchors.
12. How to calibrate the Master Form Spec.
1)  Start by looking at the top-left anchor. Paper Keyboard must be able to find this anchor to position itself from when locating the remaining items on a form. If the anchor is not completely within the red box, and/or the red cross hair does not locate the anchor, you should adjust your offset units. Vertical offset units are adjusted when the image scanned too high or too low. Horizontal offset units are adjusted when the image scanned too far to the left or right. To change the offset units:
1.  Click on the Edit menu located at the top of the Paper Keyboard window,
1.  Select Scanner Settings from the pop up window,
1.  Modify either the vertical or horizontal offset units:
|                 | Vertical Offset Units | Horizontal Offset Units |
|-----------------|---------------------------|-----------------------------|
| Positive Number | Moves red squares ↓       | Moves red squares →         |
| Negative Number | Moves red squares ↑       | Moves red squares ←         |
1.  Only modify one number at a time,
1.  Look again at the top-left anchor. If changes are still required, go back to the beginning of this step.
2)  Once you are satisfied with the positioning of your top left anchor, you will need to look at the Form and ID numbers:
1.  The red boxes should completely surround each number with sufficient room at the end of the numbers for growth.
1.  If the boxes are not positioned sufficiently, you will need to adjust your offset units as you did in Step 14a.
1.  Each time you modify a value, you will need to go back to the beginning of Step 14 and proceed from there. This will allow you to be sure the changes have not had negative affects on prior steps.
3)  You should now look at the checksum number located in the top-middle portion of the page, as well as the page number and the top-right anchor. If the red boxes do not surround these items, you will need to adjust the calibrated scale. Vertical calibrated scales are adjusted when the length of the image is too short or long. Horizontal calibrated scales are adjusted when the width of the image is too fat or thin. To change the calibrated scales:
1.  Click on the Edit menu located at the top of the Paper Keyboard window,
1.  Select Scanner Settings from the pop up window,
1.  Modify either the vertical or horizontal calibrated scales as follows.
|                 | Vertical Calibrated Scale | Horizontal Calibrated Scale |
|-----------------|-------------------------------|---------------------------------|
| Positive Number | Stretches red image ↓         | Stretches red image →           |
| Negative Number | Shrinks red image ↑           | Shrinks red image ←             |
1.  Only modify one number at a time.
1.  Each time you modify a value, you will need to go back to the beginning of Step 14 and proceed from there. This will allow you to be sure the changes have not had negative affects on prior steps.
4)  You should now look at the anchors on the bottom of your form as well as the scannable page block. If your anchors are not found, or a red square does not fall inside the scannable page block, you will need to adjust your calibrated scale. Vertical calibrated scales are adjusted when the length of the image is too short or long. Horizontal calibrated scales are adjusted when the width of the image is too fat or thin. To change the calibrated scales:
1.  Click on the Edit menu located at the top of the Paper Keyboard window,
1.  Select Scanner Settings from the pop up window,
1.  Modify either the vertical or horizontal calibrated scales as follows.
|                 | Vertical Calibrated Scale | Horizontal Calibrated Scale |
|-----------------|-------------------------------|---------------------------------|
| Positive Number | Stretches red image ↓         | Stretches red image →           |
| Negative Number | Shrinks red image ↑           | Shrinks red image ←             |
1.  Only modify one number at a time.
1.  Each time you modify a value, you will need to go back to the beginning of Step 14 and proceed from there. This will allow you to be sure the changes have not had negative affects on prior steps.
15. How to switch form specification files.
1.  We’re not done yet! So far, Paper Keyboard has only looked at the key items on our form. We must now allow it to see our bubbles to determine if we calibrated right!
1.  To look at the bubbles involves several steps. First we must close down the Master Form Specification file, and then we must open the Form Specification file that is specific to the form we have chosen to use. Fortunately, Paper Keyboard will do this automatically by recognizing the fields we have just allowed it to find. To do so:
1.  Click on the R button that is located on the left hand side of the Paper Keyboard screen,
1.  After a few seconds, Paper Keyboard will close the Master Form Specification file and will automatically open form specific Form Specification file. You can tell that this has happened by viewing the name in the top blue bar on the Paper Keyboard screen. It will no longer say AICS Master Form Spec, but should instead say Encounter Form \#, where \# is from your form.
1.  In some instances, instead of opening the new FORM SPEC file, you will be prompted to validate some information, such as Page \#, Form \# or ID \#. This means that Paper Keyboard did not find these values where it expected to find them, or it was not confident with what it read in these fields (possibly due to a brightness issue.) If this is the case, you should:
1.  Click Cancel on the field value dialogue box,
1.  Click Discard when prompted with a warning,
1.  Return to Step 14 and begin the calibration process again.
15. Checking the bubbles.
1)  Now that we are working with a new FORM SPECIFICATION file, we will need to scan the form in again. Take the same form and place it back on the scanner in the SAME position that you originally placed it in.
1.  Click on the button that looks like a scanner. It is located on the left hand side of the Paper Keyboard screen. This will feed the form through the scanner again.
1.  If you are using a Bell & Howell, and you are calibrating for a rotated page orientation, you will need to click on the scan button a second time. (You do not need to put the paper back in the scanner to do this.) This will replace the image of the front page with the image of the back page.
1)  To see the bubbles, we must now recognize the image.
1.  Click on the R button located on the left hand side of the Paper Keyboard screen.
1.  Within a few seconds, you should see your image, with red boxes surrounding each of your bubbles.
1.  Move the field value dialogue box out of viewing range by dragging and dropping the box out of the way.
1.  You need to make sure that the red boxes surround the bubbles on top as well as those further down on your page. If you don’t feel that Paper Keyboard is locating the bubbles sufficiently, you will need to adjust your calibrated scale.
1.  Move the field value dialogue box back into view, and click on the cancel button. Discard the data when prompted to do so.
1.  Click on the Edit menu located at the top of the Paper Keyboard window.
1.  Select Scanner Settings from the pop up window.
1.  Modify either the vertical or horizontal calibrated scales.
|                 | Vertical Calibrated Scale | Horizontal Calibrated Scale |
|-----------------|-------------------------------|---------------------------------|
| Positive Number | Stretches red image ↓         | Stretches red image →           |
| Negative Number | Shrinks red image ↑           | Shrinks red image ←             |
1.  Only modify one number at a time.
1.  Each time you modify a value, you will need to go back to the beginning of Step 14 and proceed from there. This will allow you to be sure the changes have not had negative affects on prior steps.
17. To determine whether you need to turn duplexing back on, refer to the following chart. If you do not need to turn duplexing back on, proceed to the next step.
|                 | Normal Calibration | Rotated Calibration     |
|-----------------|------------------------|-----------------------------|
| Hewlett Packard | Not applicable         | Not applicable              |
| Bell & Howell   | Turn duplexing back on | Verify that duplexing is on |
1.  To turn duplexing back on if applicable:
1.  Select the Edit menu from the menu bar,
1.  Choose Scanner Settings from the pop-up menu,
1.  If the Double Sided box is not checked, you must click on it to turn it on.
18. Before saving your settings, you must discard the image. To do so, bring the Field Value dialog box back into view.
1.  Click on the Cancel button.
1.  Click Discard to get rid of the image.
19. Leaving Paper Keyboard.
1.  Do NOT shut (X) or minimize (-) Paper Keyboard. Shutting Paper Keyboard will result in a loss of all the calibration settings you just entered, as well as prohibiting any future work from within the AICS Scanning Workstation. Minimizing Paper Keyboard will result in oddities during the scanning process.
1.  If you have maximized Paper Keyboard, you should choose the cascaded tile button located in the upper right hand corner of the screen. This will restore Paper Keyboard to its original size.
1.  Use Alt-Tab to bring the AICS Workstation screen to the foreground.
1.  Save your settings.
1.  Select the SAVE SCANNER SETTINGS button.
1.  Don’t forget that you have to calibrate twice! Once for a normal page orientation, and once for a rotated orientation. If you want to calibrate again, return to Step 7.
2.  To end the calibration process:
1.  Select the CLOSE button to return to the Preferences screen,
1.  From the Preferences screen, select the OK button.
You are now in the AUTOMATED INFORMATION COLLECTION SYSTEM screen.
