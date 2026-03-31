---
title: NPM Operational Summary
doc_type: POM
doc_label: Production Operations Manual
doc_layer: plain
doc_subject: 
app_code: NPM
app_name: National Patch Module
section: INF
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: Patch ModuleOperational SummaryDecentralized Hospital Computer ProgramREDACTED Information Systems CenterTroy, New YorkDecember 1992PATCH MODULE OPERATIONAL SUMMARYTABLEO FCONTENTS===================================================================Introduction 1
audience: 
keywords: 
  - patch
  - package
  - patches
  - verified
  - completed
  - report
  - status
  - unverified
  - developer
  - subject
page_count: 0
word_count: 3220
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/National_Patch_Module_(NPM)/pmuser.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/National_Patch_Module_(NPM)/pmuser.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=20"
---

Patch ModuleOperational SummaryDecentralized Hospital Computer ProgramREDACTED Information Systems CenterTroy, New YorkDecember 1992PATCH MODULE OPERATIONAL SUMMARYTABLEO FCONTENTS===================================================================Introduction 1

Developer Section 3

> Add a Patch 3

> Add Package to Patch Module 3

> Completed/Unverified Patch Report 3

> Copy a Patch into a New Patch 3

> Create a PackMan Message 4

> Delete an Unverified Patch 4

> Display a Completed/Unverified Patch 4

> Edit a Patch 4

> Extended Display of a Patch 4

> Forward a Completed/Unverified Patch Message 4

> Package Management 5

> Enter/Edit Authorized Users 5

> Key Allocation for Patch Functions 5

> List of Package Users 6

> Under Development Patch Report 6

Verifier Section 7

> Completed Patch Summary for Assigned Packages 7

> Completed/Unverified Patch Report 7

> Display a Completed/Unverified Patch 7

> Forward a Completed/Unverified Patch Message 7

> Verified Patch Summary Report by Date 7

> Verify a Patch (and/or edit internal comments) 7

IRM/Support Section 8

> All Verified Patches for a Package 8

> Detailed Report of Verified Patches by Date 8

> Display a Patch 8

> Display Number of New Patches 8

> Forward a Verified Patch Message 8

> New Patch Report 9

> Patch Options Documentation 9

> Select Packages for Notification 9

> Set All Patches for Selected Packages as Printed 9

> Summary Report of All Patches for a Package 9

> Verified Patch Summary Report by Date 9

PATCH MODULE OPERATIONAL SUMMARYTABLEO FCONTENTS===================================================================

> Output Displays 10

> Summary Report of All Patches for a Package 10

> Verified Patch Summary Report by Date 11

Introduction

The National Patch Module (NPM) is a software package that provides a database for the distribution of software patches and updates for the Department of Veterans Affairs' Decentralized Hospital Computer Program (DHCP). Options are provided for systematic entry and review of patches by developers, review and release of patches by verifiers, and display and distribution of the released verified patches to the users.

Once a problem is found in DHCP software and the solution identified, a developer enters a patch in the NPM identified by package namespace, version, and a patch number. At this point, the patch entry has a status of "under development" and is accessible only by other developers of the package. When the patch is completed and ready for review, a second developer changes the status to "completed/unverified" and the patch becomes available for review by designated verifiers of the package. After the verifier(s) have checked the patch and determined that it is ready for release, the status is changed to "verified". The patch is automatically distributed and becomes available for display by users.

The Patch Process

Developers have access to a package by being defined for that package in the DHCP PATCH/PROBLEM PACKAGE file (#11007). Access to developer menus is keyed with the A1AE DEV security key.

When a developer adds a patch to a package, a patch designation (i.e. package namespace\*version\*patch number) is generated for the patch and the status is set to "under development". Once the patch is added, it may be edited by any authorized developer of the package. To aid patch preparation, text and/or routine information may be copied into the DESCRIPTION, ROUTINE DESCRIPTION and MESSAGE text fields of the patch from an input PackMan message. The input PackMan message is generated in the development account and sent to the queue, Q-PATCH.VA.GOV. at FORUM. This message is typically generated as soon as the patched routines are available in the development account. For routine patches, it must be sent to FORUM before the patch is completed because the routines to be patched must be copied from the input message into the DHCP PATCH MESSAGE file (#11005.1) to allow the creation of the "completed-unverified" PackMan message which is sent to the verifiers.

To help in the development and release of patches that have dependencies on other patches, there is an ASSOCIATED PATCHES field where other patches may be entered as references. If the associated patch has to be verified and installed first, it may be flagged to prevent verification of the patch being edited until the associated patch is verified. There is a HOLD DATE field that can be used to prevent verification/release until a certain date.

Introduction

Verifiers have access to a package by being defined as support personnel and verifier for that package in File \#11007. Access to the verifier menus is keyed with the A1AE PHVER security key. Verifiers have menu options to print completed-unverified patches and summaries. When a patch is completed by a developer, a completed-unverified patch message containing patched routines is sent to the verifier's domain for testing.

The Verify a Patch option displays the selected completed-unverified patch before prompting the user to change the status. Any associated patches are listed, indicating that concurrent or sequential release/verification is required. Holding dates are displayed if applicable. Patches with holding dates cannot be verified before that date. Any previous patches to routines in the selected patch are also displayed.

When a patch is verified, a sequence number is generated by package and version. This SEQ \# becomes part of the subject of the verified patch message to aid in release sequence identification. The verified patch summary is also sorted by sequence number to identify patch release sequence.

IRM and Support patch users have options to display and print verified patches and summaries. Users may select packages to enable automatic notification of new verified patches. Users who have selected a package for notification can also utilize an option which will print all new verified patches for selected packages. Verified patch messages are normally sent to G.SUPPORT at each ISC on release; however, users have the option to select a patch and forward the verified patch message to anyone.

Developer Section

This menu permits an authorized developer who holds the A1AE DEVELOPER key to add/edit patches. Using the Package Management option, developers can add other development personnel, support personnel, and verifiers associated with the package. Using the Delete an Unverified Patch option, developers can delete patches which have a status of "under development" or "completed/unverified". Using the Copy a Patch into a New Patch option, developers can copy existing patches into new patches under the same or a different version. The menu also provides the following print options: Extended Display of a Patch, Display a Completed/Unverified Patch, Completed/Unverified Patch Report, and Under Development Patch Report.

Add a Patch

This function permits authorized developers to add a new patch to a specific version of a package. Patches are unique by their designation and have the following format: package namespace\*

version number\*system assigned patch number. When the patch is added, the system assigns it a patch status of "under development". A developer other than the one entering the patch must review the patch and change the status to "completed/unverified" using the Edit a Patch option.

Add Package to Patch Module

This option allows users to add packages to the DHCP PATCH/PROBLEM PACKAGE file (#11007). Only holders of security key A1AE MGR may access this option.

Completed/Unverified Patch Report

This print option generates a report of completed/unverified patches for a selected package and version. Only an authorized developer or verifier of the package may use this option. The user has the option of sorting the report by patch designation, category, or priority. The report contains detailed information about each patch including the patch subject, description, category, priority, and status; information about the users who entered the patch and completed the patch; and a routine information section showing coding changes.

Copy a Patch into a New Patch

This function permits authorized developers of a package to copy information from an existing patch into a new patch. The new patch must be for the same package, but can be for a different version. You will be prompted for a patch to copy, then the version number of the new patch being created. The system assigns a patch designation to the new patch, and you are asked if you want to add this patch. If you respond YES, you will be prompted for the subject of the new patch. The new patch is automatically assigned a status of "under development". The user entering and date entered is set by the system. The priority, category(s), patch description, and all routine information is copied over from the existing patch into the new patch.

Developer Section

Create a PackMan Message

This option allows a developer to create an input PackMan message from the local routine directory, if the routines and version are present.

Delete an Unverified Patch

This function permits authorized developers of a package to delete an incorrect patch which has a status of "under development" or "completed/unverified". Only these types of patches may be deleted since only the developer(s) and verifier(s) are aware of the patch. The system assigned patch number will then be reassigned to the next patch. When a patch has a status of "verified" or "entered in error", the patch cannot be deleted since users have been notified of the patch. If there is an error to a verified patch, the developer must change the status of the patch to "entered in error" via the edit function. If the status is changed to "entered in error", a message is sent to the users who printed the patch.

Display a Completed/Unverified Patch

This option permits display of a completed/unverified patch. The user must be an authorized developer or verifier to use this option. When looking up a patch, the values for the following fields can be entered as the look-up value: patch designation, package, patch subject, routine. There is also a key word in context cross-reference on the SUBJECT field that can be used. The display contains the patch subject, description, category, priority, and status. The display also contains information about the users who entered and completed the patch and a routine information section showing coding changes.

Edit a Patch

This function permits authorized developers of a package to edit a patch. The option is also used by a developer other than the one who entered the patch to review the patch and change the status to "completed/unverified". When looking up a patch, the values for the following fields can be entered as the look-up value: patch designation, package, patch subject, routine name. There is also a key word in context cross-reference on the SUBJECT field that can be used. Which fields may be edited are dependent on the value of the STATUS field.

Extended Display of a Patch

This option allows the developer to view an extended display of a patch. Information regarding who has printed the patch is available through this option. You may display when a selected user printed the patch or the entire patch with all users who printed it. Note this option prints the fields as they exist in FileMan and NOT the way they are displayed in the patch report.

Forward a Completed/Unverified Patch Message

This option allows a user to forward a completed/unverified patch message by patch designation to selected users.

Developer Section

Package Management

> Enter/Edit Authorized Users

> This function permits authorized developers of a package to add development personnel, support personnel, and verifiers. The following three keys are automatically allocated to the user when entered as a developer, support person or verifier: A1AE DEVELOPER, A1AE SUPPORT, and A1AE PHVER. These keys may be manually allocated/deallocated using the Key Allocation for Patch Functions option. For authorized developers to receive the Developer Menu, they must be given the A1AE DEVELOPER key; for verifiers to receive the Verifier Menu, they must be given the A1AE PHVER key. If the support person is also a verifier of the package, then a V should be entered at the verifier prompt. The developer can also specify whether or not user selection of a package is permitted. If selection is permitted, any user can select this package via the Select Packages for Notification option. This selection causes 1) automatic notification of patches via MailMan and 2) printing of new patches for this package whenever the user enters the New Patch Report option.

> Key Allocation for Patch Functions

> This function allows the package developers and the Patch Module coordinator to allocate patch module keys to other users. When a holder of a key is edited, the user is informed for what other packages the holder may need the key. The user is then asked if s/he wants to delete the holder. The following keys are available.

> 1\) A1AE PHVER - This key allows the user to have access to the Verifier Menu of the Patch User Menu.

> 2\) A1AE DEVELOPER - This key allows the user to have access to the Developer's Menu of the Patch User Menu.

> 3\) A1AE XUSEC - This key allows the user (usually a developer) to have access to the Key Allocation of Patch Functions option of the Package Management menu. If a user has this key s/he can give out the following keys through this option: A1AE SUPPORT, A1AE DEVELOPER, and A1AE PHVER.

> 4\) A1AE SUPPORT - This key allows the holder access to the Support Menu of the Patch User Menu. This menu has been removed in Version 2.0 of the Patch Module. The key is being left in the module for future enhancements.

> 5\) A1AE MGR - This key allows the user to have access to the Patch Module Management Menu of the Patch User Menu. Also, the user will be able to allocate all A1AE keys through this option.

Developer Section

> List of Package Users

> This function generates a report of user information about a selected package. The user must be an authorized developer of the package to utilize this option. The report contains the developers, support personnel, and any selected users associated with the package.

Under Development Patch Report

This print option generates a report of under development patches for a selected package and version. The user must be an authorized developer of the package to use this option. The user has the option of sorting the report by patch designation, category, or priority. The report contains detailed information about each patch including the patch subject, description, category, priority, and status; information about the users who entered the patch and completed the patch; and a routine information section showing coding changes.

Verifier Section

This menu provides the holder of the A1AE PHVER key with the options needed to verify, display, and print completed/unverified patches for those packages for which s/he is a verifier.

Completed Patch Summary for Assigned Packages

This prints a summary report for all completed/unverified patches in all assigned packages.

Completed/Unverified Patch Report

This print option generates a report of completed/unverified patches for a selected package and version. Only an authorized developer or verifier of the package may use this option. The user has the option of sorting the report by patch designation, category, or priority. The report contains detailed information about each patch including the patch subject, description, category, priority, and status; information about the users who entered the patch and completed the patch; and a routine information section showing coding changes.

Display a Completed/Unverified Patch

This option permits display of a completed/unverified patch. The user must be an authorized developer or verifier to use this option. When looking up a patch, the values for the following fields can be entered as the look-up value: patch designation, package, patch subject, routine. There is also a key word in context cross-reference on the SUBJECT field that can be used. The display contains the patch subject, description, category, priority, and status. The display also contains information about the users who entered and completed the patch and a routine information section showing coding changes.

Forward a Completed/Unverified Patch Message

This option allows a user to forward a completed/unverified patch message by patch designation to selected users.

Verified Patch Summary Report by Date

This print option generates a report of verified patches for a select package, or all selected packages for a specified date range. The report contains the patch designation, subject, date completed, and priority.

Verify a Patch (and/or edit internal comments)

Using this option, authorized verifiers of a package can change the status of a "completed/

unverified" patch to the "verified" status. When the verifier changes the status of a patch to "verified", a bulletin is sent to user(s) who have requested notification of patches for the package and a message containing the patch is sent to G.SUPPORT@ISCs. The patch is then available to all patch users.

IRM/Support Section

This is the main menu for patch/problem options. Depending on what keys the user holds, some options will or will not appear.

All Verified Patches for a Package

This print option generates a report of all verified patches for a selected package and version. The user has the option of sorting the report by patch designation, status, category, or priority. The report contains detailed information about each patch including the patch subject, description, category, priority, and status; information about the users who entered the patch, completed the patch, and verified the patch; and a routine information section showing coding changes.

Detailed Report of Verified Patches by Date

This print option generates a detailed report of verified patches for a select package, or all selected packages for a specified date range. The report contains detailed information about each patch including the patch subject, description, category, priority, and status; information about the users who entered the patch, completed the patch, and verified the patch; and a routine information section showing coding changes.

Display a Patch

This option permits the user to display a verified or entered in error patch for any package in the PATCH file. A new patch which is displayed but not printed will appear as new until it is printed. When looking up a patch, the values for the following fields can be entered as the look-up value: patch designation, package, patch subject, routine name. There is also a key word in context cross-reference on the SUBJECT field that can be used. If a patch has the status of "verified", the display contains the patch subject, description, category, priority, and status. The display contains information about the users who entered the patch, completed the patch, and verified the patch. Coding changes are shown in the routine information section of the display.

> **NOTE:** If a patch has the status of "entered in error", only the patch designation, status, package, priority, subject, and entered in error description fields are displayed.

Display Number of New Patches

This option displays a summary of the number of new patches for selected packages. This display includes the package name, number of new patches, and date any patches were last printed for the package. A patch is new if it has not been printed by the user, and it has a status of "verified". Once a new patch has been printed, it will no longer be counted on this summary display.

Forward a Verified Patch Message

This option allows a user to forward a verified patch message by patch designation to

selected users.

IRM/Support Section

New Patch Report

This print option generates a report of new patches for any selectable package in the PATCH file, or all selected packages. A patch is new if it has not been printed by the user, and it has a status of "verified". Once a new patch has been printed, it is no longer available under this option but can be viewed via any of the other print options for verified patches. The report contains detailed information about each patch including the patch subject, description, category, priority, and status; information about the users who entered the patch, completed the patch, and verified the patch; and a routine information section showing coding changes.

Patch Options Documentation

This print option generates a report of all the options available for recording, printing, and maintaining patch information.

Select Packages for Notification

This option permits the user to choose those packages for which they want to receive automatic notification of new patches via MailMan. Once the user selects a package, s/he will be shown the number of new patches associated with the package(s) when signing into the Patch Module. These new patches will automatically be available via the New Patch Report option. Packages may be entered individually, or ALL can be entered to receive patches for all user selectable packages. The user may stop notification of patches for a particular package via this option by selecting the package and responding YES to stop notification. The user can also enter "-"

{PACKAGE NAME} at the package prompt to stop notification.

Set All Patches for Selected Packages as Printed

This option allows a new user of the Patch Module to update the printed status of all patches for all selected packages. This option is used so that patches that were verified previous to the selection of the package by the user no longer appear on new patch displays. The patches may still be viewed and printed through other options.

Summary Report of All Patches for a Package

This option permits the user to display a summary report of all patches for a selected package and version. The report contains the patch designation, subject, status, and routines.

Verified Patch Summary Report by Date

This print option generates a report of verified patches for a select package, or all selected packages for a specified date range. The report contains the patch designation, subject, date completed, and priority.  
IRM/Support Section

Summary Report of All Patches for a Package

Select PACKAGE: RT RECORD TRACKING RT

Select VERSION: 1// Date Verified: 03-25-89

Sort by reverse SEQ \# ? No//

Patch Summary Report NOV 10,1992 15:20 PAGE 1

Designation

SEQ Subject Status Routine

--------------------------------------------------------------------

RT\*1\*1 1 TEST 10 V 05/20/90

RT\*1\*2 2 Disable LAYGO for Sc V 05/07/90 RTQ2

RT\*1\*5 3 TEST COPY V 09/22/92 RT

RTQ

Hold date 10/19/92

Associated patches: (v)A1AE\*1\*6 install with patch \`RT\*1\*17'

(c)DVB\*11\*3 install with patch \`RT\*1\*17'

(v)RA\*1.1 \<\<= must be installed BEFORE \`RT\*1\*17'

-----------------------------------------------------------------------------RT\*1\*4 4 TEST 11 V 05/21/90 RT

-----------------------------------------------------------------------------RT\*1\*3 5 TEST 14 RTTEST V 05/22/90 RTSM6

-----------------------------------------------------------------------------RT\*1\*6 6 TEST 12 V 05/21/90 RT

-----------------------------------------------------------------------------RT\*1\*7 7 TEST BULLETIN V 10/26/92 RT

RTQ2

Hold date 10/26/92

----------------------------------------------------------------------------

RT\*1\*10 TEST DESCRIPTION INP U 06/13/91

-----------------------------------------------------------------------------RT\*1\*11 TEST DES COPY U 06/13/91 RT

RTQ

------------------------------------------------------------------------------RT\*1\*12 TEST DES1 C 09/15/92

-----------------------------------------------------------------------------RT\*DBA\*13 TST SUMMARY C 09/14/92

-----------------------------------------------------------------------------RT\*1\*14 TEST COPY/PATCH CHEC C 10/19/92 RT

RTQ

RTQ2

Hold date 10/19/92

Associated patches: (v)A1AE\*1\*6 install with patch \`RT\*1\*34'

(c)DVB\*1\*3 \<\<= must be installed BEFORE \`RT\*1\*34'

-----------------------------------------------------------------------------

IRM/Support Section

Verified Patch Summary Report by Date

Do you want to Print Patches for a Specific Package? No// Y

Select PACKAGE: RT RECORD TRACKING RT

\*\*\*\* Date Range of Verified Patches \*\*\*\*

Beginning DATE : T-999 (FEB 15, 1990)

Ending DATE : T (NOV 10, 1992)

DEVICE: HOME// Decnet RIGHT MARGIN: 80//

Patch SEQ \# Patch Subject Date Priority

Designation Verified

-----------------------------------------------------------------------------

RT\*1.26\*17 14 TEST COPY SEP 22, 1992 MANDATORY

Hold date: OCT 19, 1992

Associated patches: (v)A1AE\*1\*6 install with patch

(u)RA\*2.08\*5 \<\<= must be installed BEFORE

RT\*1\*4 13 TEST DEMO COPY SEP 16, 1992 EMERGENCY

RT\*1\*18 12 TEST : SEP 15, 1992 EMERGENCY

RT\*1\*3 11 DEMO PATCH JUN 12, 1991 MANDATORY

Associated patches: (v)RT\*1.25\*3 \<\<= must be installed BEFORE

RT\*1\*19 9 TST MAR 19, 1991 MANDATORY

RT\*1\*20 8 TEST20 NEW MAIL,PRINT MAR 19, 1991 MANDATORY

RT\*1\*14 7 TEST 14 RTTEST MAY 22, 1990 MANDATORY

RT\*1\*11 6 TEST 11 MAY 21, 1990 MANDATORY

RT\*1\*12 5 TEST 12 MAY 21, 1990 MANDATORY

RT\*1\*13 4 TEST 13 MAY 21, 1990 MANDATORY

RT\*1\*10 3 TEST 10 MAY 20, 1990 MANDATORY

RT\*1\*8 2 TEST 8 MAY 17, 1990 MANDATORY

RT\*1\*2 1 Disable LAYGO for Schedu MAY 7, 1990 MANDATORY