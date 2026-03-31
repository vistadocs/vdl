---
title: Outpatient Pharmacy Version 7 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: > The Outpatient Pharmacy (OP) package provides a way to manage the medication regimen of veterans seen in the outpatient clinics and to monitor and manage the workload and costs in the Outpatient Pharmacy.
audience: 
keywords: 
  - table
  - contents
  - actions
  - outpatient
  - pharmacy
  - action
  - bingo
  - drug
  - added
  - board
page_count: 0
word_count: 1149
section_count: 8
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/op_7_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/op_7_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

![](outpatient-pharmacy-version-7-release-notes/001.png)

OUTPATIENT PHARMACY (OP)RELEASE NOTES

December 1997

Office of the Chief Information Officer

Introduction

> The Outpatient Pharmacy (OP) package provides a way to manage the medication regimen of veterans seen in the outpatient clinics and to monitor and manage the workload and costs in the Outpatient Pharmacy.

> The primary benefits to the veteran are the assurance that he or she is receiving the proper medication and the convenience of obtaining refills easily. The clinicians and pharmacists responsible for patient care benefit from a complete, accurate, and current medication profile available at any time to permit professional evaluation of treatment plans. Utilization, cost, and workload reports provide management cost controlling tools while maintaining the highest level of patient care.

> The release notes provide a brief description of the changes in version 7.0 of the Outpatient Pharmacy software package.

> A number of site parameters allow the individual Department of Veterans Affairs Medical Center (VAMC) to customize the package to meet local needs. The users’ manual describes these site parameters and the ways they influence the operation of the package.

> This version (7.0) of the Outpatient Pharmacy software package can only be run with a standard MUMPS operating system. It also requires the following Department of Veterans Affairs (VA) software applications:

> <u>Package</u> <u>Minimum Version Needed</u>

> Pharmacy Data Management 1.0

> VA FileMan 21.0

> Kernel 8.0

> PMIS 5.3

> National Drug File 3.16

> Integrated Billing 2.0

> Fee Basis 3.5

> Adverse Reaction Tracking 4.0

> Inpatient Medications 4.5

> IFCAP 5.0

> Laboratory 5.2

> Order Entry/Results Reporting 3.0

> The above software is not included in this package and must be installed before this package is completely functional.

# Enhancements and Changes in Outpatient Version 7.0


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Enhancements and Changes in Outpatient Version 7.0](#enhancements-and-changes-in-outpatient-version-70)
  - [Outpatient Pharmacy List Manager](#outpatient-pharmacy-list-manager)
  - [Actions able to be entered using List Manager](#actions-able-to-be-entered-using-list-manager)
  - [## Outpatient Pharmacy Hidden Actions](#outpatient-pharmacy-hidden-actions)
    - [Speed Actions](#speed-actions)
    - [Other Outpatient Pharmacy ListMan Actions](#other-outpatient-pharmacy-listman-actions)
    - [Other Screen Actions](#other-screen-actions)
  - [Functionality](#functionality)
  - [Mail Group Setup for the HL7 External Interface](#mail-group-setup-for-the-hl7-external-interface)
  - [Archiving \[PSO ARCHIVE\]](#archiving-pso-archive)
  - [The following routines will be deleted for OP. V. 7.0.](#the-following-routines-will-be-deleted-for-op-v-70)
> In addition to reading this manual, you should also read the Implementation and Maintenance section of the Technical Manual.

## Outpatient Pharmacy List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The main change to version 7.0 is the use of ListMan to section actions and the interface with Computerized Patient Record System (CPRS) V. 1.0.

> List Manager is a tool designed so that a list of items can be presented to the user for an action.

> For Outpatient Pharmacy, the List Manager does the following:

- allows the pharmacist or technician to browse through a list of actions
- allows the pharmacist or technician to take action against those items
- allows the user to select an action that displays an action or informational profile
- allows the user to select a different action without leaving an option.

> When processing an order now you will see that the screen has dramatically changed from the previous version. The new screen was designed using List Manager.

> This new screen gives you more information and easier accessibility to vital reports and areas of a patient’s chart you may wish to see.

> Outpatient Pharmacy List Manager Screen

> Screen title: The screen title changes according to what type of information List Manager is displaying (e.g., Patient Information, Medication Profile, New OP Order (ROUTINE), etc.).

> Allergy indicator: This indicator displays when there has been information entered into the ALLERGY field for the patient.

> Header area: The header area is a “fixed” (non-scrollable) area that displays patient information.

> List area: (scrolling region) This area scrolls (like the previous version) and displays the information that you can take action on.

> Message window: This section displays a plus (+) sign, minus (-) sign, or informational text (i.e., Enter ?? for more actions). If you enter a plus sign at the action prompt, List Manager will “jump” forward a page. If a minus sign is displayed and you enter it at the action prompt, List Manager will “jump” back a screen. The plus and minus signs are only valid actions if they are displayed in the message window.

> Action area: A list of actions display in this area of the screen. If you enter a double question mark (??) at the “Select Item(s)” prompt, you will receive a “hidden” list of additional actions that are available to you. Outpatient Pharmacy hidden actions are displayed with the letters (OP) next to the action.

## Actions able to be entered using List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Actions are entered by typing the name(s), or synonym(s) at the “Select Item(s)” prompt. In addition to the various actions that may be available specific to the option you are working in, List Manager provides generic actions applicable to any List Manager screen. You may enter a double question mark (??) at the “Select Action” prompt for a list of all actions available. The following is a list of generic List Manager actions with a brief description. The synonym for each action is shown in brackets following the action name. Entering the synonym is the quickest way to select an action. Outpatient Pharmacy hidden actions are displayed with the letters (OP) next to the action.

> Action Description

> Next Screen \[+\] move to the next screen (may be shown as a default).

> Previous Screen \[-\] move to the previous screen.

> Up a Line \[UP\] move up one line.

> Down a Line \[DN\] move down one line.

> Shift View to Right \[\>\] move the screen to the right if the screen width is more than 80 characters.

> Shift View to Left \[\<\] move the screen to the left if the screen width is more than 80 characters.

> First Screen \[FS\] move to the first screen.

> Last Screen \[LS\] move to the last screen.

> Go to Page \[GO\] move to any selected page in the list.

> Re Display Screen \[RD\] redisplay the current.

> Print Screen \[PS\] prints the header and the portion of the list currently displayed.

> Print List \[PL\] prints the list of entries currently displayed.

> Search List \[SL\] finds selected text in list of entries.

> Auto Display (On/Off) \[ADPL\] toggles the menu of actions to be displayed/not displayed automatically.

> Quit \[QU\] exits the screen (may be shown as a default).

## ## Outpatient Pharmacy Hidden Actions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The OP hidden actions will display with the previous hidden actions once you select a completed or finished order and enter a double question mark (??) at the “Select Action” prompt.

> The following hidden actions appear on the prescription profile screen and can only be applied to one order at a time.

> Activity Logs \[AL\] displays the Activity Logs.

> Copy \[CO\] allows the user to copy and edit an order.

> Hold \[HD\] places an order on a hold status.

> Other OP Actions \[OTH\] allows the user to choose from the following sub-actions:

> Progress Note \[PN\],

> Action Profile \[AP\],

> Print Medication Instructions \[MI\], or

> Display Orders’ Statuses \[DO\].

> Patient Information \[PI\] shows patient information, allergies, adverse reactions, and pending clinic appointments.

> Pull Rx \[PP\] action taken to pull an Rx(s) early from suspense.

> Reprint \[RP\] reprints the label.

> Unhold \[UH\] removes an order from a hold status.

> Verify \[VF\] allows the pharmacist to verify an order a pharmacy technician has entered.

### Speed Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> These OP actions are referred to as “speed actions” and appear on the medication profile screen. These actions can be applied to one or more orders at a time.

> Reprint \[RP\] reprints the label.

> Renew \[RN\] a continuation of a medication authorized by the provider.

> Refill \[RF\] a second or subsequent filling authorized by the provider.

> Discontinue \[DC\] status used when an order was made inactive either by a new order or by the request of a physician.

> Release \[RL\] action taken at the time the order is filled and ready to be given to the patient.

> Pull Rx \[PP\] action taken to pull an Rx(s) early from suspense.

> Inpat. Profile \[IP\] action taken to view an Inpatient Profile.

### Other Outpatient Pharmacy ListMan Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Exit \[EX\] allows you to exit processing pending orders.

> AC Accept

> BY Bypass

> DC Discontinue

> ED Edit

> FN Finish

### Other Screen Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Edit/Enter Allergy/ADR Data \[EA\] provides access to the Adverse Reaction Tracking package to allow entry and/or edit of allergy adverse reaction data for the patient. See the Adverse Reaction Tracking package documentation for more information on allergy/ADR processing.

> Detailed Allergy Display \[DA\] displays a detailed listing of the selected item from the patient’s allergy/ADR list. Entry to the Edit Allergy/ADR Data action is provided with this list also.

> Patient Record Update \[PU\] allows editing of patient data such as SSN, birthdate, address, phone, outpatient narrative, etc.

> New Order \[NO\] allows new orders to be entered for the patient.

> Exit Patient List \[EX\] allows you to exit patient’s Patient Information screen so that a new patient can be selected.

## Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Update Provider Name

> When a provider’s name is edited in an Rx, the name is updated for all fills. This change occurs on any level (original, refill, or partial). If the provider’s name is changed, a message will be displayed warning the user that the provider’s name will change on all levels. Provider fields in the PRESCRIPTION file (#52) will no longer be able to be edited through VA FileMan.

> Prevent Duplicate Prescriptions when Renewing more than Once

> OP version 7.0 now prevents duplicate Rx numbers when the same Rx is renewed more than once.

> Cost Data

- Partial Rx’s are included in the cost data. Partial Rx’s count as refills on cost reports.
- New *Purge Drug Cost Data* \[PSO PURGE DRUG COST\] option located under the Supervisor’s menu, purges data from the DRUG COST file (#50.9).
- The cost compile for the daily and monthly cost reports currently uses the fill date. These compile jobs have been changed to use the fill date and the release date.

> Print Template Misspelled-300

> A correction has been made for a print template for the DRUG COST file (#50.9). The word Statistics is now spelled correctly.

> Division Costs by Drug Report

> A new column has been added to the Division Costs by Drug report, which is found under the *Cost Analysis Reports* \[PSO CST\] menu. This column is the Total Qty column, which represents the total quantity dispensed of each particular drug.

> Pharmacy Statistics by Division

> Previously, there was only one way to run the *Pharmacy Statistics* \[PSO COST STATISTICS\] option, found under the *Cost Analysis Reports* \[PSO CST\] menu. That method only showed the totals for all divisions together. The new functionality will still have this same option, but there is a new option called *Sort Statistics By Division* \[PSO COST STATS BY DIVISION\], which is found under the *Pharmacy Cost StatisticsMenu* \[PSO COST STAT MENU\]. This new option will allow sorting by division, and will provide totals for each division, in addition to a total for all the divisions.

> Drug Allergy Order Checks

- Drug Allergy checks are done in V. 7.0. Interventions are allowed to be entered (optionally).
- Order check will be displayed from the CPRS package.

## Mail Group Setup for the HL7 External Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A mail group and device must be set up in order to run the HL7 external interface. The recommended name of the mail group is PSO HLGROUP1. The recommended device name is PSO HLDEVICE1.

Speed Actions

- Renew, Refills, Cancel/Discontinue, Release, and Pull Rx(s) from Suspense actions.
- Progress Notes (entry point to be provided by TIU when available)

  New Fields
- Two new fields for the MEDICATION INSTRUCTION file (#51): MED ROUTE, SCHEDULE.

> Enhanced Action/Information Profiles

- Action Profile Sort

> New functionality is provided to make it easier to sort Action Profiles by clinic. Clinic groups can now be set up and any number of clinics can be assigned to a Clinic Group. Action Profiles can now be sorted by Patient, by Clinic, or by Clinic Group. If Clinic Group is chosen, Action Profiles for all Clinics assigned to that Clinic Group will be printed.

- Action Profile (Polypharmacy) Report

When printing Action profiles, the user is now prompted to print a Polypharmacy report. If you answer Yes to this prompt, the next prompt will ask for the minimum number of active prescriptions for the report. A system parameter was added to control the displaying of this prompt. The system parameter must be set to Yes in order for the question to be asked.

- New ACTION PROFILE MESSAGE field

> A new field has been added to the DRUG file (#50). This field is called the ACTION PROFILE MESSAGE (OP), and whatever is entered for a particular drug prints on the Action Profile when that particular drug prints.

Options and Actions

> The following menu options no longer appear under the *Rx (Prescriptions)* \[PSO RX\] option menu, but have been included as part of the ListMan functionality as actions.

- *Edit Prescriptions* \[PSO RXEDIT\] Refills are no longer entered using the edit action.
- *Hold Features* ... \[PSO RXHOLD\]

> *Hold Rx* \[ PSO HOLDRX\]

> *Unhold Rx* \[PSO UNHOLDRX\]

- *New Prescription Entry* \[PSO NEW\]
- *Partial Prescription* \[PSO RXPAR\]
- *Refill Prescriptions* \[PSO REF\]

> ListMan functionality allows users to have access to multiple actions without having to jump to different menu options.

## * Archiving* \[PSO ARCHIVE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Save* \[PSOARCSV\] option on this menu has been changed to *SavetoTape* \[PSO ARCHIVE TAPE SAVE\]. In addition, there are three new options on the *Archiving* \[PSO ARCHIVE\] menu.

- Archive to File \[PSO ARCHIVE FILE SAVE\]

> This option records all information about the archived prescriptions gathered by the Find option to a Host File Server (HFS) file.

- File Retrieval \[PSO ARCHIVE FILE RETRIEVE\]

> This option reads information from the HFS file and prints a summary of all prescriptions for the selected patient.

- Print Archived Prescriptions \[PSO ARINDEX\]

> This option enables you to print a list of archived prescriptions from the PHARMACY ARCHIVE file (#52.8) with this option.

> Copy Medication Order Action

A new Copy action (ListMan) was added for this version. This action allows users to select an existing order, copy the current data, and edit any fields needed.

> *Rx Verification by Clerk* Option

> The *RxVerification* \[PSO VR\] option has been changed to *Rx Verification by Clerk* \[PSO VR\]. This change is due to patient verification being part of the ListMan order processing.

> New *External Interface Menu*

> A new *External Interface Menu* \[PSO EXTERNAL INTERFACE\] has been added. This menu contains options for using an external interface device. The options are *Purge External Batches* \[PSO INTERFACE PURGE\], *Reprint External Batches* \[PSO INTERFACE REPRINT\], and *View External Batches* \[PSO INTERFACE VIEW\].

> Return to Stock Enhancements

> When returning medications to stock, refills are no longer lost. If a refill is returned to stock the refill is deleted. If the original is returned, it is not deleted but marked as returned. To re-dispense an original fill the user must use the reprint option to re-dispense the medication. This allows the original fill to be released.

> New Suspense Functions

- New Print from Suspense File sort:

> The *Print from Suspense File* \[PSO PNDLBL\] option now allows sorting by DEA Special Handling, in addition to sorting by Patient Name and SSN. If the user chooses to sort by DEA Special Handling, the labels are sorted by three categories within the DEA Special Handling field.

> 1\) All DEA’s containing an A or a C

> 2\) All DEA’s containing an S

> 3\) All others not containing an A, S, or C

> Within each of these three categories, another sort is done by Patient Name or SSN.

- Print from Suspense File queue:

> When queuing the *Print from Suspense File* \[PSO PNDLBL\] option, the user no longer has to wait while all the labels are being queued. One job will queue, with minimal waiting. Also, instead of a tasked job for each patient, only one job will be sent to TaskMan, which will make it easier to stop the job once it has begun.

- New *Delete Printed Rx’s from Suspense* \[PSO PNDPRI\] option:

> A new option is available to delete Rx’s from suspense that have already been printed. It allows the user to delete one Rx, all for a patient, all within a specified date range, or by printed batches.

- When using the *Pull Early From Suspense* \[PSO PNDRX\] option, the Method of Pickup is able to be edited, in addition to Routing.
- *Reset and Print Again* \[PSO PNDRPT\] option:

> The *Reset and Print Again* \[PSO PNDRPT\] option has been changed to *Reprint Batches from Suspense* \[PSO PNDRPT\]. Every time the *Print from Suspense File* \[PSO PNDLBL\] option is run, those Rx’s will be associated with a batch. When the *Reprint Batches from Suspense* \[PSO PNDRPT\] option is run, the user is asked to reprint a batch, instead of a date range. The user is able to see what labels printed with the batch before they reset it to print.

- Delete from Suspense default:

> All prescriptions that are pulled early from suspense will be deleted from suspense. Since they can no longer be reset to print again because they are not part of a batch, there is no reason to keep them in suspense. Only Rx’s that are printed from suspense are part of a reprintable batch.

> *Edit* action

> Using the *Edit* action in ListMan, the Days Supply field is now able to be edited to a number over 30. Other checks are taken into account, such as the type of drug, the number of refills, and the Rx Patient Status, among others.

> *  
> Expire Prescriptions* \[PSO EXPIRE INITIALIZE\]

> This option initializes a daily job that will mark any prescription as expired that has yesterday as an expiration date.

> *Purge Drug Cost Data* \[PSO PURGE DRUG COST\]

> To purge drug cost data from the DRUG COST file (#50.9) a starting and ending date is entered. The job can then be run immediately or queued.

> Reports/Profiles

- The 45 days cutoff for screen profiles has been increased to 120 days. This will allow Rx’s that have been discontinued or are expired to be renewed (if applicable).
- Medication Profile sort

> There are three ways to sort the printing of the Medication Profiles. They are Date, Class, and Medication. New functionality provides additional sorts within each of these three categories. After choosing to sort by one of these three categories, a prompt is given that asks to print all from the category, or only print a select group from within the category chosen. If a select group is chosen, the user is asked the From and To range for the category.

- *List Prescriptions on Hold* \[PSO HOLDRPT\] option

> Previous functionality for the *List Prescriptions on Hold* \[PSO HOLDRPT\] option did not provide any sorting capability. The new functionality for this option allows sorting by Division, and within Division sorting by Hold Reason, and within Hold Reason sorting by Hold Date.

> Bingo Board

> The enhancements to the Bingo Board in version 7.0 are the result of decisions made by the Pharmacy EP and feedback from the user community. The enhancements include the following:

- The *Start Bingo BoardDisplay*\[PSO BINGO START\] option has been changed so that the bingo board can be started without tying up a terminal or requiring the user who starts it to have multiple sign-on capability. A site parameter has been added to indicate whether or not a dedicated device has been reserved. If so, the user is prompted to enter the device name. If a dedicated device is setup, the user is able to automatically start or stop the board via TaskMan. The user is also prompted for a Display Group which is saved as a site parameter. This option requires working with local Information Resources Management (IRM) to complete its setup.
- Names now display differently on the bingo board. Names and ticket numbers can be displayed alphabetically in one column, and new names to the board will appear in reverse video for a user-defined amount of time. The user enters the time when creating a display group and it is stored in the GROUP DISPLAY file (#59.3).
- A field has been added to the GROUP DISPLAY file (#59.3) to record the frequency for updating the bingo board monitor.
- The *Status of Patient’s Order* \[PSO BINGO STATUS\] option has been added to report the status of an order. The statuses are Processing, Ready for Pickup, or Picked Up. A new field has been created in the PATIENT NOTIFICATION (RX READY) file (#52.11) to hold this data.
- Fields have been added in the WAITING TIME file (#52.12) to record average and total waiting times.
- For the *Remove Patient’s Name from Monitor* \[PSO BINGO DELETE PATIENT\] option, the entry is no longer completely deleted. Rather, the patient’s name is removed from the display monitor only. The entry remains in the file.
- Sites should run the *Enter/Edit Display* \[PSO BINGO ENTER/EDIT DISPLAY\] option to edit the display groups that are already defined because new fields have been added.
- The statistics report has been enhanced. Minimum, maximum, and average indicators have been added. Printing of a notice on the label printer if a particular Rx is not filled within a site-defined time is now available.
- Pull Early from Suspense is included as a source for Bingo Board.
- Barcode Refill/Renew is included as a source for Bingo Board.
- The finish process for orders input via CPRS are now a source for bingo board.

Updating Computerized Patient Record System (CPRS) with Outpatient Pharmacy Orders

> On patient selection, CPRS will be updated with OP orders.

  
Obsolete Options, Templates, and Routines

> The options and templates below will be deleted during the installation of the Outpatient Pharmacy package V. 7.0.

|                           |                                      |
|---------------------------|--------------------------------------|
| Option Name           | Menu Text                        |
| PSO DRUG                  | Drug Enter/Edit                      |
| PSO DRUGMENU              | Drug/Drug Interaction Functions      |
| PSO HOLDRX                | Hold Rx                              |
| PSO INTERACTION           | Drug Interactions Menu               |
| PSO INTERACTION LOCAL ADD | Enter/Edit Local Drug Interaction    |
| PSO INTERACTION SEVERITY  | Edit Drug Interaction Severity       |
| PSO LAB MONITOR           | Mark/Unmark Lab Monitor Drugs        |
| PSO NEW                   | New Prescription Entry               |
| PSO REF                   | Refill Prescriptions                 |
| PSO RXEDIT                | Edit Prescriptions                   |
| PSO RXHOLD                | Hold Features                        |
| PSO RXPAR                 | Partial Prescription                 |
| PSO SIGED                 | Medication Instruction File Add/Edit |
| PSO UNHOLDRX              | Unhold Rx                            |
| PSO FACILITY SETUP        | Enter Facility Data for Clozapine    |
| PSO MARK DRUG             | Mark Clozapine Drug                  |
| PSOL UNMARK DRUG          | Unmark Clozapine Drug                |
| PSOARCCO                  | Find                                 |
| PSOARCHLIST               | List One Patient’s Archived Rx’s     |
| PSOARCIN                  | Tape Retrieval                       |
| PSOARCPURGE               | Purge                                |
| PSOARCSV                  | Save                                 |

- The templates below are obsolete for the O P V .7 .0 software product.

|                        |          |
|------------------------|----------|
| Input              | File |
| PSO DRUG               | \#50     |
| PSO SIGED              | \#51     |
| PSO BATCH PARTIAL      | \#52     |
|                        |          |
| Print              | File |
| PSO ACTION PROFILE \#3 | \#44     |
| PSOBJP                 | \#52     |
|                        |          |
| Sort:              | File |
| PSOBJP                 | \#52     |

## The following routines will be deleted for OP. V. 7.0.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|          |          |          |          |          |
|----------|----------|----------|----------|----------|
| PSOCLDRG | PSOCLUS1 | PSOCLUS2 | PSOCLUS3 | PSOCSRL1 |
| PSOCSTAR | PSODRUG  | PSOGMINS | PSOGMP12 | PSOGMP25 |
| PSOLIST  | PSONODIB | PSONUM   | PSOPOST3 | PSOPRE   |
| PSORX    | PSORXPAR |          |          |          |

  
Order Checks

Outpatient Pharmacy checks for the following items:

- Drug/drug interactions
- Duplicate drug
- Duplicate Drug class
- Drug/allergies