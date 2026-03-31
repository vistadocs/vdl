---
consolidated_title: "cmop user manual"
app_code: PSX
doc_type: UM
master_source: "CMOP Version 2 User Manual (Updated PSX*2*98)"
master_pub_date: August 2016
consolidated_from: 2 versions
prior_versions:
  - "CMOP Version 2 User Manual (Updated PSX*2*91)"
---

# Consolidated Mail Outpatient Pharmacy (CMOP)

# Version 2.0

# User Manual

<!-- image -->

August 2016

(Revised August 2024)


Office of Information and Technology (OIT)

########### Revision History

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All”, replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

| Date    | Revised Pages                                                                                   | Patch Number   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------|-------------------------------------------------------------------------------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 8/2024  | Page 15                                                                                         | PSX*2*98       | Added Rx level Mail Exemption                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 12/2022 | Page 14, 15, ii, ii                                                                             | PSX*2*97       | Changed Outpatient Site file (#59) field names for Days to Pull from Suspense fields (#3, #3.1, #3.3, #3.4)  Updated Setup Auto-transmission, Print From Suspense File, Rest and Print Again.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 09/2021 | Page 52,145,146                                                                                 | PSX*2*91       | Updated CMOP Not Transmitted Rx List Message to remove reference to ROI.  Added 3/4 Days Supply Bypass.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 05/2020 | Page 22, 46                                                                                     | PSX*2*89       | Updated references to the max days allowed in Non-CS Days to Transmit and CS Days to Transmit fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 06/2016 | Page 51                                                                                         | PSX*2*79       | Updated Title Page to current OI&amp;T standards  Remove reference to DEA Special Handling field for billable status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 01/2016 | Cover Page, 138, 140                                                                            | PSX*2.0*77     | Updated date on Cover Page.  Replaced CMOP Not Dispensed Rx List bulletin with updated example showing that the CMOP Not Dispensed Rx List bulletin is modified to include the standard symbols denoting additional information used by Outpatient Pharmacy . Prescription numbers for ePharmacy claims are marked with ‘e’. Prescription numbers with a first party copay shall be marked with ‘$’.  Replaced CMOP Not Transmitted Rx List bulletin with updated example showing that the CMOP Not Transmitted Rx List Bulletin is modified to show new text providing reasons the prescriptions in the message did not transmit to CMOP, displays the first date of the attempted submission, the number of times the prescription submission has been attempted the first unsuccessful transmit, and the bulletin displays the correct site name of the CMOP transaction in the subject line.  REDACTED |
| 11/2014 | Page 17, 17a, 17b                                                                               | PSX*2.0*76     | Replaced the example for Drug Enter/Edit with an updated example.  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 11/2013 | Throughout (minor nonsubstantive changes).  18, 20, 20, 34, 35, 28, 29, 30, 51, 129a, 129b, 130 | PSX*2*74       | Electronic Data Interchange (EDI) New Standards and Operating Rules – VHA Provider-side Technical Compliance Requirements TAC-12-03366 Project.  Cosmetic changes (standardized fonts). Changed all references from version 6 to version 7 and standardized wording for blank pages (without using change pages).  Edited Revision History, p. 47 verbiage. Updated p.50 to add patch-specific functionality. Added 129a, 129b to include conditions under which the prescription will rejected.  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                 |
| 11/2009 | 137a-b                                                                                          | PSX*2*68       | Alerts for a discontinued CMOP prescription  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 07/2009 | i-ii, 50a-50b                                                                                   | PSX*2*65       | ePharmacy Iteration II – Phase 4 project:  Updated revision history, ¾ days’ supply functionality, and host error functionality.  REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 04/2006 | v-viii,  30, 41-42, 46-50,  50a-b, 126, 137                                                     | PSX*2*48       | HIPAA NCPDP Global Project:  Updated Table of Contents;  Updated “Functionality for Returning Med to Stock” verbiage;  Updated View Prescriptions Example to include ECME Activity and Reject Logs; Updated Print from Suspense options and reflowed text onto following pages;  Added Third Party Electronic Claims Submission of CMOP Prescriptions;  Added ECME transmission to the Flow Chart for Processing a CMOP Transmission in Appendix D;  Added example of an “e-Pharmacy CMOP Not Transmitted Rx List Message” to Appendix E.  REDACTED                                                                                                                                                                                                                                                                                                                                                        |
| 10/2003 | 24, 24a                                                                                         | PSX*2*41       | Updated example for scheduling of auto-transmissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 09/2002 | Title Page;  i-(ii);  65-66.                                                                    | PSX*2*34       | Updated Title Page and Revision History; modified description of Unreleased Rx’s Report to include new sort and print options.  Formatting change unrelated to the patch: Header for example of Rejected Messages Report moved to same page as body of report.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 05/2002 | Title Page;  i-viii;  (61)-62;  67-(68).                                                        | PSX*2*32       | Updated Title page; added Revision History page and renumbered Preface and Table of Contents pages; added new CMOP DRUG Cost Missing report; and amended Facility Activity Report description to add time range.  Screen captures on updated pages re-formatted to new standards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 12/1997 |                                                                                                 |                | Original Released User Manual.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

**Preface**

Version 2.0 of Consolidated Mail Outpatient Pharmacy (CMOP) software processes and automatically transmits prescription data from a Veterans Affairs Medical Center to a CMOP host facility. The CMOP host facility then mails prescriptions from an integrated and highly automated outpatient prescription dispensing system. This CMOP user manual is intended for pharmacists and pharmacy technicians who are familiar with the functionality of Outpatient Pharmacy Version 7.0.

Introduction to the User Manual	1

Package Functional Description	1

About This Manual	1

Intranet	1

Special Instructions for the “First Time” Computer User	1

Special Notations	2

Change Pages	2

Package Management/Legal Requirements	2

CHAPTER 1: REMOTE MEDICAL CENTER	3

Section 1: CMOP Site Manager Menu	4

Getting Out of an Option	4

Activate/Inactivate CMOP Processing	4

Display System Setup	6

Purge Status of CMOP Rx Queue	6

CMOP Drug/Item Management	7

Loop CMOP Match to Local Drug File	7

CMOP Mark/Unmark (Single drug)	8

CMOP Data from Your Local Drug File	9

Drug Enter/Edit	10

Drugs not Flagged for CMOP Transmission	12

Reports	12

Count of CMOP Suspended Rx’s	12

Medical Center Activity Report	13

Rx Workload Report	13

Turnaround Time Report	13

Resubmit CMOP Rx	13

Transmission Menu	14

Comment Enter/Edit	14

Re-transmit CMOP Data	14

Setup Auto-transmission	14

View Transmission	16

Section 2: Modified Outpatient Pharmacy Options	17

Using the Outpatient Pharmacy Manager Menu	17

Released and Unreleased Prescription Report	18

Release Medication	19

Rx (Prescriptions)	20

Barcode Rx Menu	20

Barcode Batch Prescription Entry	20

Cancel Prescriptions	21

Edit Prescriptions	21

Hold Features	22

Hold Rx	22

Unhold Rx	23

New Prescription Entry	23

Refill Prescriptions	26

View Prescriptions	26

Delete a Prescription	28

Suspense Functions	28

Change Suspense Date	29

Delete From Suspense File	29

Print From Suspense File	29

Pull Early From Suspense	31

Reset and Print Again	31

Update Patient Record	32

Third Party Electronic Claims Submission of CMOP Prescriptions	33

CHAPTER 2: HOST CMOP FACILITY	35

Section 1: CMOP System Management Menu	36

Transmission Review	36

Interface Menu	37

Monitor CMOP Interface	38

Start CMOP Interface	38

Stop CMOP Interface	40

Operations Management	40

Start/Stop Background Filer	40

Nightly Purge of CMOP Database	40

Nightly Purge of Release Data	40

Purge of Release Messages	41

Resend Release Data to VAMCs	41

System Parameter Enter/Edit	41

Display System Status	42

Reports	43

Transmission Report Summary	43

Rejected Messages Report	43

Unreleased Rx’s Report	44

Duplicate Release Data Report	44

Facility Activity Report	45

Turnaround Time Report	45

Report of Release Data Returned	45

Print Rejected Orders	45

Print Transmission Labels	45

Label Restart Utility	45

Reprint Transmission Labels	46

Rx Inquiry	46

Manual/Barcode Release Prescription	47

Unhold Transmission	47

View Transmission	48

Enter/Edit Transmission Comments	48

CMOP Drug/Item Management	48

Loop CMOP Match to Local Drug File	49

CMOP Mark/Unmark (Single drug)	50

CMOP Data from Your Local Drug File	51

Drug Enter/Edit	52

Drugs not Flagged for CMOP Transmission	53

Facility Cost Management	53

Date Range Compile/Recompile Cost Data	54

Drug Cost by Drug Report	55

Drug Cost by Drug Report for One Month	57

Drug Cost by Facility Report	60

High Cost Rx Report	61

Initialize the Nightly Compile Job	61

One Day Compile/Recompile Cost Data	62

Purge Cost Data	63

Update Rx COST in Master Database	63

Archive CMOP Data	64

Archive Monthly CMOP Data	64

Purge Archived CMOP Data	65

Retrieve Archived CMOP Data	65

Glossary	67

APPENDICES	70

Appendix A: Interface Message Examples	71

Appendix B: Label Examples	73

Appendix E: CMOP MailMan Messages	86

Mail Messages Seen At Remote Medical Centers	86

Mail Messages Seen At CMOP Facilities	91

## Table of Contents

## ## Introduction to the User Manual

### Package Functional Description

The Consolidated Mail Outpatient Pharmacy (CMOP) software package establishes an interface for the electronic transfer of information between Veterans Affairs Medical Centers (VAMCs) and the Consolidated Mail Outpatient Pharmacy host system for an integrated and highly automated outpatient prescription dispensing system.

### About This Manual

This manual contains a description of all the Consolidated Mail Outpatient Pharmacy options and the Outpatient Pharmacy (OP) options that have been modified to incorporate functionality necessary for CMOP. For an example of the Outpatient Pharmacy functionality for these options, we recommend the users refer to the *Outpatient Pharmacy User Manual Version 6.0* .

This manual is divided into two chapters. The first chapter consists of two sections that contain options used by the remote medical centers. The first section of Chapter One comprises the *CMOP Site Manager Menu* options. The second section contains the Outpatient Pharmacy options modified for CMOP. The modifications to the OP options, for the most part, are not apparent to the user. These modified Outpatient Pharmacy options are only used at the remote medical centers.

Chapter Two contains the options necessary for the host CMOP facility. These options are listed under the *CMOP System Management Menu* .

An index and appendices are located at the end of this manual and contain added information and guidance for the user. The appendices cover information such as interface log messages, examples of CMOP Rx labels, an example of marking CMOP drugs when a new dispense unit is required, a flowchart showing the processing of a CMOP prescription, and examples of MailMan messages.

### Intranet

Documentation for this product can now be found on the intranet. You will find it at the following address:

REDACTED

This address will take you to the Clinical Products page where you will find a listing of all the clinical software manuals. Click on the Consolidated Mail Outpatient Pharmacy (CMOP) link and it will take you to the CMOP Homepage. You can also get there by going straight to the following address: REDACTED

+	Remember to bookmark this site for future reference.

### Special Instructions for the “First Time” Computer User

If you are unfamiliar with the CMOP package or other Veterans Health Information Systems and Technology Architecture (VistA) software applications, we recommend that you study the DHCP *User’s Guide to Computing.* This orientation guide is a comprehensive handbook benefiting first time users of any VistA application. The purpose of the introductory material is to help you become familiar with basic computer terms and the components of a computer. It is reproduced and distributed periodically by the Kernel Development Group. To request a copy, contact your local Information Resources Management (IRM) staff.

### Special Notations

In this manual, the user’s response is underlined and in **bold** type, but will not appear on the screen underlined and bold. The underlined and bold part of the entry is the letter or letters that must be typed so that the computer can identify the response. In most cases, you need only enter the first few letters. This increases speed and accuracy.

Every response you type must be followed by pressing the return key (or enter key for some keyboards). Whenever the return or enter key should be pressed, you will see the symbol **&lt;RET&gt;** . This symbol is not shown but is implied if there is underlined and bold input.

Throughout the package, help frames may be accessed from most prompts by entering one, two, or three question marks (?, ??, ???).

Within the examples representing actual terminal dialogues, the author may offer information about the dialogue. This information is enclosed in brackets (e.g., *[Screen Clears])* and will not appear on the screen.

### Change Pages

Future modifications to the software may require changes to the documentation. Change pages will contain the new version number and date in the footer. Vertical lines in the margin may also be used to further highlight changes on a page.

### Package Management/Legal Requirements

This package does not impose any additional legal requirements on the user, nor does it relieve the user of any legal requirements. All users are reminded that many of the reports generated by this package contain confidential patient information, which is protected by the Privacy Act. Names and social security numbers used in the examples are fictitious.

**Icons**

Icons used to highlight key points in this manual are defined as follows:

<!-- image -->

Required security keys

Indicates the user should take note of the information.

## CHAPTER 1: REMOTE MEDICAL CENTER

## Section 1: CMOP Site Manager Menu

<!-- image -->

**PSXCMOPMGR**

The CMOP site manager uses the options on this menu to manage the operations necessary for the Consolidated Mail Outpatient Pharmacy. This menu contains the following options:

*Activate/Inactivate CMOP Processing*

*Display System Setup*

*Purge Status of CMOP Rx Queue*

*CMOP Drug/Item Management...*

*Reports Menu...*

*Resubmit CMOP Rx*

*Transmission Menu...*

### Getting Out of an Option

To stop what you are doing, enter an up-arrow (^). You can use the up-arrow at any prompt to terminate the line of questioning. Continue entering up-arrows to completely exit from the system.

### Activate/Inactivate CMOP Processing

<!-- image -->

**PSXCMOPMGR**

The CMOP site manager selects this option to request that the remote medical center be activated or inactivated for CMOP processing of outpatient prescriptions.

When the remote medical center enters a request to activate for CMOP processing, a notification message is sent to the CMOP for the request. The message triggers an ALERT to the CMOP manager at the host facility to take action on the request. If the CMOP takes action to grant the request to activate, the remote entry in the CMOP NATIONAL SITE file (#552) is marked Active. A return confirmation message is sent to the facility to activate the entry and notify the requester that the system has been activated and CMOP processing may begin. If the CMOP takes action to deny the request, a return notification message advises the requester of the action to deny.

**Example: Activate/Inactivate CMOP Processing**

***[This is the remote.]***

Select CMOP Site Manager Menu Option: **A** ctivate/Inactivate CMOP Processing

**************************************************************

> **WARNING:** There are Rx's currently suspended for CMOP.

If you inactivate CMOP processing:

1)  These Rx's will not transmit to the CMOP, but will remain

in the RX SUSPENSE file.  These Rx's cannot be accessed by

Outpatient Pharmacy options.  Ideally, these Rx's should

be transmitted or printed before inactivation takes place.

If CMOP processing is activated, these prescriptions can

be transmitted.

2)  Before inactivating, please have all pharmacy users sign

off until inactivation is complete.  CMOP Rx's input by

users who do not sign off the system will be suspended for

CMOP transmission. (See #1)

3)  Your current auto transmission schedule will be

cancelled on inactivation.

**************************************************************

REGION 1 CMOP is the current active CMOP system.

Do you want to Inactivate the REGION 1 CMOP system? NO// **Y** ES

Are you sure? NO// **Y** ES

The REGION 1 CMOP system has been inactivated.

Activate another system? NO// **&lt;RET&gt;**

Select CMOP Site Manager Menu Option: **&lt;RET&gt;**

***[This is the host.]***

Enter  "VA   VIEW ALERTS     to review alerts

Select CMOP Site Manager Menu Option: **VIE** w Alerts

1.I  BIRMINGHAM, AL.has inactivated CMOP processing.

Select from 1 to 1

or enter ?, A, I, P, M, R, or ^ to exit: **??**

YOU MAY ENTER:

A number in the range 1 to 1 to select specific alert(s)

for processing.

A to process all of the pending alerts in the order shown.

I to process all of the INFORMATION ONLY alerts, if any, without further ado.

P to print a copy of the pending alerts on a printer

M to receive a MailMan message containing a copy of these pending alerts

R to Redisplay the available alerts

^ to exit

Select from 1 to 1

or enter ?, A, I, P, M, R, or ^ to exit: **A**

Processed Alert Number 1

BIRMINGHAM, AL.has inactivated CMOP processing.

***[This is the remote.]***

Select CMOP Site Manager Menu Option: **A** ctivate/Inactivate CMOP Processing

Enter CMOP System: **REGION 1 CMOP** INACTIVE

Enter mailman domain: XXXX-XXXX.XXX.XX.XXX// **&lt;RET&gt;**

CMOP SYSTEM STATUS

REGION 1 CMOP  (INACTIVE)     No current transmission

CMOP Domain                 : BAB.ISC-BIRM.XX.XXX

Last Batch Transmitted      : 167

CMOP RX Queue purged        : JUN 3,1996@13:41:16

Auto Transmission setup     : NO

Are you sure you want to activate the REGION 1 CMOP system? NO// **Y** ES

Request to activate sent to REGION 1 CMOP.

***[This is the host.]***

Select CMOP Site Manager Menu Option: **VIE** w Alerts

1.   BIRMINGHAM, AL. has submitted a request to activate CMOP processing.

Select from 1 to 1

or enter ?, A, I, P, M, R, or ^ to exit: **A**

Select one of the following:

A         APPROVED

D         DISAPPROVED

BIRMINGHAM, AL. has submitted a request to activate CMOP processing.

Select: **A** PPROVED

***[This is the remote.]***

Select CMOP Site Manager Menu Option: **VIE** w Alerts

1.I  Permission to transmit to REGION 1 CMOP has been received.

Select from 1 to 1

or enter ?, A, I, P, M, R, or ^ to exit: **A**

Processed Alert Number 1

Permission to transmit to REGION 1 CMOP has been received.

Select CMOP Site Manager Menu Option: **&lt;RET&gt;**

### Display System Setup

This option displays on the screen the following information for the currently **active** CMOP System:

1. **System Name**

1. **Status** (Active/Inactive)

1. **CMOP Domain**

(Receiver address from CMOP SYSTEM file (#550) for use by transmission protocol)

1. **Transmission Status**

Current status of CMOP processing (Transmitting data or No current transmission).

1. **Last Batch Transmission**

Batch number last transmitted to the CMOP.

1. **Auto-transmission Setup**

YES indicates a background job has been queued to transmit CMOP data and it will be rescheduled to transmit automatically.

1. **CMOP Rx Queue Purge Date/Time**

Date and time of the last auto-purge of the CMOP RX QUEUE file (#550.1).

### Purge Status of CMOP Rx Queue

This option provides a status report of the latest purge of the CMOP Rx queue. This report prints to the screen only. This report includes the date and time of the last purge, the starting and ending message number, and the total orders purged.

### CMOP Drug/Item Management

<!-- image -->

**PSXCMOPMGR**

The CMOP Manager uses this submenu to perform operations required to transmit selected drug/items to the CMOP host facility.

*Loop CMOP Match to Local Drug File*

*CMOP Mark/Unmark (Single drug)*

*CMOP Data from Your Local Drug File*

*Drug Enter/Edit*

*Drugs not Flagged for CMOP Transmission*

#### Loop CMOP Match to Local Drug File

<!-- image -->

**PSNMGR**

With this option users select entries in the local DRUG file (#50), review NATIONAL DRUG file (NDF) (#50.6) matches, and mark entries to transmit to the CMOP.

**Example: Loop CMOP Match to Local Drug File**

Select CMOP Site Manager Menu Option: **CMOP D** rug/Item Management

Select CMOP Drug/Item Management Option: **L** oop CMOP Match to Local Drug File

This option allows you to choose entries from your drug file and helps you

review your NDF matches and mark individual entries to send to CMOP.

If you mark the entry to transmit to CMOP, it will replace your Dispense Unit

with the VA Dispense Unit. In addition, you may overwrite the local drug name

with the VA Print Name and the entry will remain uneditable.

Do you wish to loop through the whole file?

(If you answer "NO", you will loop through ONLY the ones previously marked as

"Do not transmit to CMOP").

Enter Yes or No: **N** O

I have to build a table before you can begin "looping" so let me put you on

"hold" for a moment.

...............................................................

VA Print Name: GUAIFENESIN 100MG/5ML SYRUP         VA Dispense Unit: ML

Local Drug Generic Name: GUAIFENESIN 100MG/5ML LIQUID

VA Drug Class: RE302

ORDER UNIT: 120ML

DISPENSE UNITS/ORDER UNITS: 120

DISPENSE UNIT: MG/ML

PRICE PER DISPENSE UNIT: 0.01

** This entry has been previously marked NOT to transmit to CMOP **

Do you wish to mark this drug to transmit to CMOP?

Enter Yes or No: **Y** ES

Your old Dispense Unit  MG/ML  does not match the new one  ML.

You may wish to edit the Price Per Order Unit and/or the Dispense

Units Per Order Unit.

PRICE PER ORDER UNIT: 0.01// **&lt;RET&gt;**

DISPENSE UNITS PER ORDER: 120// **&lt;RET&gt;**

Do you wish to overwrite your local name?

Enter Yes or No: **Y** ES

VA Print Name: GUAIFENESIN 100MG/5ML SYRUP

Local Drug Name                            CMOP?    VA D.U.        O.W.?

------------------------------------------------------------------------------

1. GUAIFENESIN 100MG/5ML SYRUP               YES      ML             YES

Price Per Order Unit = 0.01

Dispense Units Per Order Unit = 120

If you answer "Yes" you will go to the next VA Print Name. If you answer "No"

you will go back through this particular VA Print Name group.

Are you sure everything is correct?

Enter Yes or No: **Y** ES

You've completed marking everything that is possible.

#### CMOP Mark/Unmark (Single drug)

<!-- image -->

**PSNMGR**

The user can mark or unmark a single drug for transmission to the CMOP with this option.

If a drug marked for CMOP in the DRUG file (#50) needs to be edited, the entry must be unmarked for CMOP using the *CMOP Mark/Unmark (Single drug)* option. Once editing is completed, the drug must be re-marked for CMOP using the *CMOP Mark/Unmark (Single drug)* option.

*****IMPORTANT*****

When using the option *CMOP Mark/Unmark (Single drug)* to mark a drug for CMOP the user **must** update the cost information in the DRUG file (#50) to ensure the cost data for the refill will be correct.

**Example 1: Marking a CMOP Drug (Single drug)**

Select CMOP Site Manager Menu Option: **CMOP D** rug/Item Management

Select CMOP Drug/Item Management Option: **CMOP M** ark/Unmark (Single drug)

This option allows you to choose entries from your drug file and helps you

review your NDF matches and mark individual entries to send to CMOP.

If you mark the entry to transmit to CMOP, it will replace your Dispense Unit

with the VA Dispense Unit. In addition, you may overwrite the local drug name

with the VA Print Name and the entry will remain uneditable.

Select DRUG GENERIC NAME: **GUAIFENESIN 100MG/5ML LIQUID** RE302

Local Drug Generic Name: GUAIFENESIN 100MG/5ML LIQUID

ORDER UNIT: 120ML

DISPENSE UNITS/ORDER UNITS: 120

DISPENSE UNIT: EA

PRICE PER DISPENSE UNIT: 0.01

VA Print Name: GUAIFENESIN 100MG/5ML SYRUP       VA Dispense Unit: ML

VA Drug Class: CN103

Do you wish to mark this drug to transmit to CMOP?

Enter Yes or No: **Y** ES

QUANTITY DISPENSE MESSAGE: **ENTER IN MULTIPLES OF 120.**

Your old Dispense Unit  EA  does not match the new one  ML.

You may wish to edit the Price Per Order Unit and/or The Dispense

Units Per Order Unit.

PRICE PER ORDER UNIT: 3.70// **1.20**

DISPENSE UNITS PER ORDER UNIT: 1// **120**

Do you wish to overwrite your local name?

Enter Yes or No: **Y** ES

Select DRUG GENERIC NAME: **&lt;RET&gt;**

**Example 2: Unmarking a CMOP Drug (Single drug)**

Select CMOP Site Manager Menu Option: **CMOP D** rug/Item Management

Select CMOP Drug/Item Management Option: **CMOP M** ark/Unmark (Single drug)

This option allows you to choose entries from your drug file and helps you

review your NDF matches and mark individual entries to send to CMOP.

If you mark the entry to transmit to CMOP, it will replace your Dispense Unit

with the VA Dispense Unit. In addition, you may overwrite the local drug name

with the VA Print Name and the entry will remain uneditable.

Select DRUG GENERIC NAME: **GUAIFENESIN 100MG/5ML SYRUP** RE302

Local Drug Generic Name: GUAIFENESIN 100MG/5ML SYRUP

ORDER UNIT: 120ML

DISPENSE UNITS/ORDER UNITS: 120

DISPENSE UNIT: ML

PRICE PER DISPENSE UNIT: 0.01

VA Print Name: GUAIFENESIN 100MG/5ML SYRUP            VA Dispense Unit: ML

VA Drug Class: CN103

Do you wish to UNmark this drug to transmit to CMOP?

Enter Yes or No: **Y** ES

Select DRUG GENERIC NAME: **&lt;RET&gt;**

#### CMOP Data from Your Local Drug File

The user prints a report of data in the local DRUG file (#50) marked to transmit to the CMOP using this option. The report groups drugs together that are matched to the same VA Print Name along with the VA Dispense Unit. This report must be sent to a printer.

**Example: CMOP Data from Your Local Drug File**

Select CMOP Site Manager Menu Option: **CMOP D** rug/Item Management

Select CMOP Drug/Item Management Option: **CMOP D** ata from Your Local Drug File

This option will produce a report to help you review your NDF matches.

The report will group drugs together that are matched to the same VA Print

Name along with the VA Dispense Unit. These will be used for CMOP purposes.

You may queue the report to print, if you wish.

DEVICE: [Select print device.] [This report must be sent to a printer.]

report follows

LOCAL DRUGS MATCHED TO THE SAME VA PRINT NAME

Date printed: SEP 15,1996

Page: 1

VA PRINT NAME                                          VA DISPENSE UNIT

Local GENERIC NAME                                    Local DISPENSE UNIT

------------------------------------------------------------------------------

ACETAMINOPHEN 650MG RTL SUPP                           EA

ACETAMINOPHEN 650MG RTL SUPP                          EA

ACETAZOLAMIDE 125MG TAB                                TAB

ACETAZOLAMIDE 125MG TAB                               TAB

ACETAZOLAMIDE 250MG TAB                                TAB

ACETAZOLAMIDE 250MG TAB                               TAB

ACETAZOLAMIDE 500MG SA CAP                             CAP

ACETAZOLAMIDE 500MG SA CAP                            CAP

ACETIC ACID 0.25% IRRG SOLN                            ML

ACETIC ACID 0.25% IRRG SOLN                           ML

ACETIC ACID 2% OTIC SOLN                               ML

ACETIC ACID 2% OTIC SOLN                              ML

ACETIC ACID 2/ALUM ACET 10.79% OTIC SOLN               ML

ACETIC ACID 2/ALUM ACET 10.79% OTIC SOLN              ML

ACETIC ACID 2/DESONIDE 0.05% OTIC SOLN                 ML

ACETIC ACID 2/DESONIDE 0.05% OTIC SOLN                ML

*[This report has been abbreviated to save space.]*

#### Drug Enter/Edit

<!-- image -->

**PSXCMOPMGR**

With this option the user adds new drugs to the file, edits existing drugs, and inactivates drugs. When an entry in DRUG file (#50) is marked for CMOP, the GENERIC NAME and DISPENSE UNIT fields **cannot** be edited. If editing of these fields is necessary, the entry must be unmarked for CMOP using the *CMOP Mark/Unmark (Single drug)* option. Once editing is completed, the drug must be re-marked for CMOP using the *CMOP Mark/Unmark (Single drug)* option.

**Example: Drug Enter/Edit**

Select OPTION NAME: PSS DRUG ENTER/EDIT       Drug Enter/Edit

Drug Enter/Edit

Select DRUG GENERIC NAME: AMOXAPIN

Lookup: GENERIC NAME

1   AMOXAPINE 100MG TAB           CN601

2   AMOXAPINE 25MG TAB           CN601

3   AMOXAPINE 50MG TAB           CN601

CHOOSE 1-3: 1  AMOXAPINE 100MG TAB         CN601

******************************************************************************

This entry is marked for the following PHARMACY packages:

Outpatient

Unit Dose

Non-VA Med

GENERIC NAME: AMOXAPINE 100MG TAB// &lt;RET&gt;

VA CLASSIFICATION: CN601// &lt;RET&gt;

DEA, SPECIAL HDLG: 6P// &lt;RET&gt;

DAW CODE: &lt;RET&gt;

NATIONAL FORMULARY INDICATOR: NO

LOCAL NON-FORMULARY: N/F// &lt;RET&gt;

VISN NON-FORMULARY: V-N/F// &lt;RET&gt;

Select DRUG TEXT ENTRY: &lt;RET&gt;

Select FORMULARY ALTERNATIVE: NORTRIPTYLINE HCL 25MG CAP

// &lt;RET&gt;

Select SYNONYM: 4037// &lt;RET&gt;

SYNONYM: 4037// &lt;RET&gt;

INTENDED USE: QUICK CODE// &lt;RET&gt;

NDC CODE: &lt;RET&gt;

Select SYNONYM: &lt;RET&gt;

MESSAGE: NATL N/F (IEN)// &lt;RET&gt;

RESTRICTION: &lt;RET&gt;

FSN: &lt;RET&gt;

NDC: 52544-0381-01// &lt;RET&gt;

INACTIVE DATE: &lt;RET&gt;

WARNING LABEL SOURCE is 'NEW'.

The following WARNING LABEL may continue to be used for a limited time for some

external interfaces.

WARNING LABEL: 1,9,11,33// &lt;RET&gt;

Current Warning labels for AMOXAPINE 100MG TAB

No warnings from the new data source exist for this drug.

Verify that the drug is matched to the National Drug File.

Labels will print in the order in which they appear for local and CMOP fills:

1   -MAY CAUSE DROWSINESS- Alcohol may intensify this effect. USE CARE when

driving or when operating dangerous machinery.

9       DO NOT TAKE non-prescription drugs without medical advice.

11  Avoid prolonged exposure to SUNLIGHT and finish all this medication unless

otherwise directed by prescriber.

33  SEE MEDICATION INFORMATION SHEET FOR DRUG INFO

Pharmacy fill card display: DRUG WARNING 1,9,11,33

NEW WARNING LABEL LIST: 1,9,11,33

Would you like to edit this list of warnings? N// &lt;RET&gt;

ORDER UNIT: BT// &lt;RET&gt;

PRICE PER ORDER UNIT: 68.82// &lt;RET&gt;

DISPENSE UNIT: TAB// &lt;RET&gt;

DISPENSE UNITS PER ORDER UNIT: 100// &lt;RET&gt;

NCPDP DISPENSE UNIT: EACH// &lt;RET&gt;

NCPDP QUANTITY MULTIPLIER: 1// &lt;RET&gt;

PRICE PER DISPENSE UNIT: 0.688

points to AMOXAPINE 100MG TAB in the National Drug file.

This drug has already been matched and classified with the National Drug

file. In addition, if the dosage form changes as a result of rematching,

you will have to match/rematch to Orderable Item.

This drug has also been marked to transmit to CMOP.

If you choose to rematch it, the drug will be marked NOT TO TRANSMIT to CMOP.

Do you wish to match/rematch to NATIONAL DRUG file? No// &lt;RET&gt;

Just a reminder...you are editing AMOXAPINE 100MG TAB.

Strength from National Drug File match =&gt; 100    MG

Strength currently in the Drug File    =&gt; 100    MG

Strength =&gt; 100   Unit =&gt; MG

POSSIBLE DOSAGES:

DISPENSE UNITS PER DOSE: 1         DOSE: 100MG           PACKAGE: IO

DISPENSE UNITS PER DOSE: 2         DOSE: 200MG           PACKAGE: IO

LOCAL POSSIBLE DOSAGES:

Do you want to edit the dosages? N// &lt;RET&gt;

******************************************************************************

This entry is marked for the following PHARMACY packages:

Outpatient

Unit Dose

Non-VA Med

MARK THIS DRUG AND EDIT IT FOR:

O  - Outpatient

C  - Controlled Substances

X  - Non-VA Med

Enter your choice(s) separated by commas : &lt;RET&gt;

** You are NOW in the ORDERABLE ITEM matching for the dispense drug. **

AMOXAPINE 100MG TAB is already matched to

AMOXAPINE TAB

Do you want to match to a different Orderable Item? NO// &lt;RET&gt;

#### Drugs not Flagged for CMOP Transmission

This report generates a list of items in the local DRUG file (#50) which are available at the CMOP, but have not been marked for transmission. This report must be sent to a printer.

**Example: Drugs not Flagged for CMOP Transmission**

Select CMOP Site Manager Menu Option: **CMOP D** rug/Item Management

Select CMOP Drug/Item Management Option: **DRUGS NOT** Flagged for CMOP Transmission

This report will print all drugs marked for Outpatient use which are non-

controlled substances and are not marked to transmit to CMOP.

This report requires 132 columns.

You may queue the report to print, if you wish.

DEVICE: [Select print device.] [This report must be sent to a printer.]

report follows

OUTPATIENT DRUGS NOT MARKED TO SEND TO CMOP

Date printed: FEB 15,1997

Page: 1

LOCAL DRUG NAME                         STATUS        VA PRINT NAME

---------------------------------------------------------------------------------------------

ALDOCLOR-150 TAB                        NOT MARKED    CHLOROTHIAZIDE 150/METHYLDOPA 250MG TAB

ALDOCLOR-250 TAB                        NOT MARKED    CHLOROTHIAZIDE 250/METHYLDOPA 250MG TAB

ANAMINE SYRUP                           NOT MARKED    CTM 2/PSEUDOEPHEDRINE 30MG/5ML LIQUID

ANTHRA-DERM OINT 0.25% 1.5OZ            NOT MARKED    ANTHRALIN 0.25% OINT

ANTHRALIN 1.0% CR 50GM                  NOT MARKED    ANTHRALIN 1% CREAM

APRESAZIDE 100/50 CAP                   NOT MARKED    HYDRALAZINE 100/HCTZ 50MG CAP

APRESAZIDE 50/50 CAP                    NOT MARKED    HYDRALAZINE 50/HCTZ 50MG CAP

APRESOLINE-ESIDRIX TAB                  NOT MARKED    HYDRALAZINE 25/HCTZ 15MG TAB

ARISTO-PAK 4MG TAB                      DO NOT SEND   TRIAMCINOLONE 4MG TAB

ARISTOCORT A 0.1% OINT 60GM             NOT MARKED    TRIAMCINOLONE ACETONIDE 0.1% OINT

*[This report has been abbreviated to save space.]*

### Reports

This menu provides reports available at the CMOP remote medical centers which contain information on data transmitted to the host facility.

*Count of CMOP Suspended Rx’s*

*Medical Center Activity Report*

*Rx Workload Report*

*Turnaround Time Report*

#### Count of CMOP Suspended Rx’s

This option is used to count suspended CMOP Rx’s sorted by day. The report contains the suspense date, the number of CMOP Rx’s queued, transmitted, printed locally, and the total number of CMOP Rx’s in suspense.

#### Medical Center Activity Report

This option allows you to print a report of  the totals by transmission the number of orders and Rx’s transmitted to the CMOP Host facility and the number of those Rx’s that are released, not dispensed and unreleased.

#### Rx Workload Report

This report provides daily totals for a selected date range listing prescriptions entered with a mail and window routing, mail and window prescriptions released by Outpatient, and prescriptions released by CMOP. The OTHER column totals all other prescriptions, i.e., cancelled, deleted, etc.

#### Turnaround Time Report

This option prints the CMOP Rx Turnaround Time report for the selected date range. The report is based on the time difference between the  transmission date/time and the date/time the pharmacist at the CMOP marked the prescription as completed/released. Information includes the average, minimum, and maximum turnaround times, and the total number of Rx’s released. This report must be queued to a printer.

### Resubmit CMOP Rx

<!-- image -->

**PSXRESUB**

The resubmit option allows designated Outpatient Pharmacy users to send Rx’s back to the CMOP that were returned as Not Dispensed, but have no apparent problems. Ordinarily, Rx’s that have problems will be corrected through the edit option and re-suspended to be sent back to the CMOP. If the Rx has no apparent problem, and the user has communicated with the Host CMOP, then this option can be used to send the Rx back. The Rx can only be resubmitted once. After one resubmission, the Rx must be printed locally.

You may not resubmit if the following conditions exist.

1. The NOT DISPENSED fill is a Duplicate Fill.
2. The fill does not have a CMOP status of NOT DISPENSED.
3. The fill has already been resubmitted.
4. The NOT DISPENSED fill is not the last fill in the Rx.

**Example:**

Select OPTION NAME: **CMOP SITE** Manager Menu

Select CMOP Site Manager Menu Option: **RES** ubmit CMOP Rx

CMOP Prescription Resubmission Utility

Enter the Rx # to resubmit: **15666**

You have chosen Rx # 15666 to be resubmitted to the CMOP.

Do you want to continue? :  (Y/N): NO// **Y** ES

RX# 15666  SUSPENDED FOR CMOP TRANSMISSION  02-18-97.

Enter the Rx # to resubmit: **&lt;RET&gt;**

Select CMOP Site Manager Menu Option: **&lt;RET&gt;**

### Transmission Menu

<!-- image -->

**PSX XMIT**

The user controls batch transmission operations with this submenu.

*Comment Enter/Edit*

*Re-transmit CMOP Data*

*Setup Auto-transmission*

*View Transmission*

#### Comment Enter/Edit

The user selects this option to make notes or comments regarding a specific transmission. The batch number is entered, the batch information is displayed, and the user is prompted for comments. Batch information includes the division, CMOP, batch number, sender, transmission and received date/time, beginning and ending order numbers, and the total orders and Rx’s.

#### Re-transmit CMOP Data

<!-- image -->

**PSXRTRAN**

Users of this option must hold the PSX XMIT, PSXCMOPMGR, and the PSXRTRAN keys to re-transmit data previously transmitted to the CMOP. At the “Select CMOP TRANSMISSION” prompt the user enters the transmission number that needs to be re-transmitted. Previous transmission summary data is then displayed for the user’s review. The user is then asked “Are you sure you want to Re-transmit this batch?”

#### Setup Auto-transmission

<!-- image -->

**PSXAUTOX**

This option allows holders of the security key, PSXAUTOX, to schedule or unschedule the CMOP transmission process to run automatically in the background on a scheduled basis.

The user enters data to schedule a recurring transmission. At the selected time, the job runs in the background. Data queued for CMOP transmission in the RX SUSPENSE file (#52.5) are transmitted. If no data are found, the job is rescheduled to run using the frequency information from the CMOP SYSTEM file (#550).

This option has been modified to include a system parameter, NUMBER OF DAYS TO TRANSMIT. This parameter indicates the number of days to transmit thru for an automatic data transmission. If this field is null or contains a zero the auto transmissions will select data through **today** as the default. If the field contains a number, n, from 1 to 15, transmission data will be selected for T+n days. The maximum NUMBER OF DAYS TO TRANSMIT is fifteen(15)

<!-- image -->

**Note:** the CMOP system parameter for non-controlled substance auto-transmissions, NUMBER OF DAYS TO TRANSMIT is different from the Outpatient site parameter, DAYS TO PULL SUSP CMOP NON-CS (#3.4). For example, if the NUMBER OF DAYS TO TRANSMIT is two (2) and the DAYS TO PULL SUSP CMOP NON-CS is seven (7) the initial transmission data will be selected for T+2 days. Once selected, for every patient with an Rx in this date range, the software will then look ahead in RX SUSPENSE file (#52.5) for any Non-CS Rxs for these patients for an additional seven days (T+2+7days). If the patients have Rx’s for this date range, they will be added to the data transmission.

With PSX*2*98, the CMOP functionality for prescriptions is being modified so that a check will be made to the PRESCRIPTION file (#52) to see if a MAIL EXEMPTION has been entered.  If a MAIL EXEMPTION has been entered, then the MAIL EXEMPTION will be used to determine the Days to Pull from Suspense.  If no MAIL EXEMPTION has been entered, then the Days to Pull from Suspense will default to the patient level mail preference in the PHARMACY PATIENT file (#55).

<!-- image -->

**Note:** Controlled Substance CMOP auto-transmissions also use two parameters, the CS DAYS TO TRANSMIT from the CMOP SYSTEM file (#550) and the DAYS TO PULL SUSP CMOP CS field (#3.1) from the OUTPATIENT SITE file (#59). The CS DAYS TO TRANSMIT is used for the initial search for suspended CS prescriptions to include. For example, if the CS DAYS TO TRANSMIT is three(3) days and the DAYS TO PULL SUSP CMOP CS is two(2) days the transmission data will be selected for T+3 days. If a patient has at least one CS prescription in the date range, any other CS prescriptions for the patient that are in suspense for an additional 2 days (T+3+2) will also be transmitted.

When an automatic transmission is modified, ensure your site contacts your CMOP liaison prior to changing any transmission times. Only one automatic transmission at a time is allowed; the CS and non-CS transmissions are scheduled at different times to allow one to finish before the next one starts.

When an automatic transmission schedule is cancelled any queued transmissions will run to completion. No further automatic transmissions will be scheduled.

**+** Each division with data to transmit creates a transmission and all usual mail messages are sent. If two divisions have data to transmit, two independent transmissions are created, etc.

**Example: Setup Auto-transmission**

Select Transmission Menu Option: **S** etup Auto-transmission

CS Transmission               Non-CS Transmission

Scheduled to Run

Frequency (hrs)

Thru days

Tasking ID

Select one of the following:

C         Controlled Substance

N         NON-Controlled Substance

Edit     CS &lt;C&gt;  or  NON-CS &lt;N&gt; : **C**

= = = = =

QUEUED TO RUN AT WHAT TIME: AUG 19,2002@23:00

DEVICE FOR QUEUED JOB OUTPUT: **&lt;RET&gt;**

QUEUED TO RUN ON VOLUME SET: **&lt;RET&gt;**

RESCHEDULING FREQUENCY: **24H**

TASK PARAMETERS: **&lt;RET&gt;**

SPECIAL QUEUEING: **&lt;RET&gt;**

CS DAYS TO TRANSMIT: 5// **&lt;RET&gt;**

= = = = =

CS Transmission               Non-CS Transmission

Scheduled to Run         AUG 19,2002@23:00

Frequency (hrs)          24H

Thru days                5

Tasking ID               1117268

Select one of the following:

C         Controlled Substance

N         NON-Controlled Substance

Edit     CS &lt;C&gt;  or  NON-CS &lt;N&gt; : **N**

= = = = =

Edit Option Schedule

Option Name: PSXR SCHEDULED NON-CS TRANS

Menu Text: Scheduled Non-CS Transmission             TASK ID:

QUEUED TO RUN AT WHAT TIME: AUG 19,2002@21:00

DEVICE FOR QUEUED JOB OUTPUT: **&lt;RET&gt;**

QUEUED TO RUN ON VOLUME SET: **&lt;RET&gt;**

RESCHEDULING FREQUENCY: **24H**

TASK PARAMETERS: **&lt;RET&gt;**

SPECIAL QUEUEING: **&lt;RET&gt;**

NON-CS DAYS TO TRANSMIT: 8// **&lt;RET&gt;**

= = = = =

CS Transmission               Non-CS Transmission

Scheduled to Run         AUG 19,2002@23:00             AUG 19,2002@21:00

Frequency (hrs)          24H                           24H

Thru days                5                             8

Tasking ID               1117268                       1117269

Select one of the following:

C         Controlled Substance

N         NON-Controlled Substance

Edit     CS &lt;C&gt;  or  NON-CS &lt;N&gt; : **&lt;RET&gt;**

NON-CS New Schedule Sent to CMOP

CS New Schedule Sent to CMOP

Select Transmission Menu Option: **&lt;RET&gt;**

#### View Transmission

With this option the user can display the following status information for a selected transmission. (Default number is the **last** transmission transmitted.)

Transmission #	Sender (User)

Status	Transmission Date/Time

Pharmacy Division	Received Date/Time

Beginning Order Number	Total Rx’s Transmitted

Ending Order Number

Total Patient Orders Transmitted

Comments *[This field will be displayed only if data is present.]*

Re-transmission Data *[This field will be displayed only if data is present.]*

## Section 2: Modified Outpatient Pharmacy Options

The Outpatient Pharmacy (OP) options in this section have been modified for use with the Consolidated Mail Outpatient Pharmacy (CMOP) Version 2.0 product. A description of the modifications for CMOP can be found in this section. The modifications to the OP options, for the most part, are not apparent to the user. These modified Outpatient Pharmacy options are only used at the remote medical centers.

For an example of the Outpatient Pharmacy functionality for these options, we recommend the users refer to the *Outpatient Pharmacy User Manual Version 6.0* .

### Using the Outpatient Pharmacy Manager Menu

**Outpatient Pharmacy Manager**

The *Outpatient Pharmacy Manager* menu [PSO MANAGER] should be assigned to supervisors, package coordinators, and members of the Automated Data Processing/Information Resources Management (ADP/IRM) staff.

The Outpatient Pharmacy package provides a method for managing the medications given to veterans who have visited a clinic or who have received prescriptions upon discharge from the hospital. Prescription labels are automatically generated and refill request forms are printed. Medication histories are kept on-line to permit checks for potential interactions. Profiles can be generated to assist the clinician in managing the patient’s medication regimen. Management reports aid the pharmacy in controlling inventory and costs.

A number of site parameters allow the individual Department of Veterans Affairs Medical Center (VAMC) to customize the package to meet local needs.

The following menu contains the options for the outpatient pharmacy manager.

*Archiving ...*

*Autocancel Rx’s on Admission*

*Bingo Board ...*

*Clozapine Pharmacy Manager ...*

*Copay Menu ...*

****†*** *Drug Enter/Edit*

*Drug Interactions Menu ...*

*DUE Supervisor ...*

*Label/Profile Monitor Reprint*

******* *Maintenance (Outpatient Pharmacy) ...*

*Medication Profile*

******* *Output Reports ...*

*Pharmacy Intervention Menu ...*

******* *Release Medication*

******* *Return Medication to Stock*

******* *Rx (Prescriptions) ...*

******* *Supervisor Functions ...*

******* *Suspense Functions ...*

***** *Update Patient Record*

*Verification ...*

***** These options from the Outpatient Pharmacy V. 7.0 package have been modified or contain suboptions which have been modified for CMOP.

**†** This option has been modified for CMOP and can be found on the *Outpatient Pharmacy Manager* menu, the *Maintenance (Outpatient Pharmacy)* menu, and the *Supervisor Functions* menu of Outpatient Pharmacy V. 7.0.

**Drug Enter/Edit**

By using the *Drug Enter/Edit* option the pharmacy supervisor can add new drugs to the file, edit existing drugs, and inactivate drugs. This option can be found on the *Outpatient Pharmacy Manager* menu, the *Maintenance (Outpatient Pharmacy)* menu, and the *Supervisor Functions* menu of Outpatient Pharmacy V. 7.0.

***CMOP Functionality for the Drug Enter/Edit Option***

When an entry in the DRUG file (#50) has been marked for CMOP, the GENERIC NAME and DISPENSE UNIT fields **cannot** be edited. If editing of these fields is necessary, the entry must be unmarked for CMOP using the *CMOP Mark/Unmark (Single drug)* option. Once editing is completed, the drug must be re-marked for CMOP using the *CMOP Mark* / *Unmark (Single drug)* option.

The QUANTITY DISPENSE MESSAGE field does not display in the Outpatient Pharmacy *Drug Enter/Edit* option. It is recommended that the user enter or edit drugs through the *CMOP Drug/Item Management* menu.

**Output Reports**

The *Output Reports* menu generates a variety of management reports. These reports contain current medication profiles, utilization, cost, and workload information which help management maintain the highest level of patient care.

*Action Profile  (132 COLUMN PRINTOUT)*

*Alpha Drug List and Synonyms*

*AMIS Report*

*Commonly Dispensed Drugs*

*Cost Analysis Reports ...*

*Daily AMIS Report*

*Drug List By Synonym*

*Inactive Drug List*

*Management Reports Menu ...*

*Monthly Drug Cost*

*Narcotic Prescription List*

*Non-Formulary List*

*Poly Pharmacy Report*

******* *Released and Unreleased Prescription Report*

***** This option from Outpatient Pharmacy V. 7.0 has been modified for CMOP.

#### Released and Unreleased Prescription Report

This option generates a report of released and unreleased or only unreleased prescriptions by date range. The default start date is T-30. If the package was installed less than 30 days ago, the default date will be the date the package was installed. The end date default will be the current date.

***CMOP Functionality for Released and Unreleased Prescription Report***

This option has been modified by adding a column to indicate if the prescription is a CMOP prescription and a column to indicate the CMOP status.

### Release Medication

The pharmacist uses the *Release Medication* option at the time the prescription is filled and ready to be given to the patient. This option is batch processed by the pharmacist. This option decreases the inventory, updates certain fields in the global, and generates a copay action if it is applicable to the prescription. Communication is made with the Integrated Funds Control, Accounting, and Procurement (IFCAP) and Medical Care Cost Recovery (MCCR) software to generate copay charges. IFCAP and MCCR software handle patient billing, tracking of charges, and payments received.

If a prescription has any status other than Active or Refill the user will be given one of the following error messages: Prescription has a status of (status) and is not eligible for release, prescription was deleted, improper barcode format, or non-existent prescription.

If you release a prescription and receive a message that the partial prescription was released and there is a refill that has not been released, you must re-enter the prescription number.

+	This is a mandatory function that **must** be used by the pharmacy.

*** **Information** ***

There exists a possibility that a patient can lose credit for a fill/refill. If a fill/refill is released and then returned to stock, the fill/refill **cannot** be re-released. The fill/refill is lost and is charged against the total number of fill/refills for this prescription.

***CMOP Functionality for Release Medication***

A CMOP Rx originally suspended for transmission to the CMOP may be released using this option, **if and only if,** it has been printed locally. CMOP Rx’s marked Queued for Transmission, Loading for Transmission, or Transmission Completed may **not** be released using this option. Transmitted Rx’s are automatically released by a background process once dispense information is returned from the host facility. Inventory is not decreased for CMOP dispensed prescriptions.

**Returning Medication to Stock**

The *Return to Stock* option functionality is used when a prescription has been released, but has been refused, not picked up, or not given to the patient for some reason. Comments can be entered to explain why the medication was returned to stock.

A prescription can only be returned to stock if the prescription status is Active, Cancelled, Expired, or Released. If the prescription is **not** released, there is no need to return it to stock. This function increases the inventory so that a more current inventory level is maintained by the Outpatient Pharmacy package.

This option also removes a copay charge if it is applicable to the prescription. It is highly recommended that you use this option.

*** **Information** ***

There exists a possibility that a patient can lose credit for a fill/refill. If a fill/refill is released and then returned to stock, the fill/refill cannot be re-released. The fill/refill is lost and is charged against the total number of fill/refills for this prescription.

***CMOP Functionality for Return Medication to Stock***

Prescriptions dispensed by the CMOP can be returned to stock at the medical center.

### Rx (Prescriptions)

The *Rx (Prescriptions)* menu allows the pharmacist to manipulate information that pertains to prescriptions. When a screen profile is displayed for any of the following options the letter (R) will appear next to the last fill date for any prescriptions that have been returned to stock.

The options in this menu are listed below.

******* *Barcode Rx Menu ...*

******* *Barcode Batch Prescription Entry*

*Check Quality of Barcode*

******* *Cancel Prescription*

******* *Edit Prescriptions*

*Hold Features ...*

******* *Hold Rx*

*List Prescriptions on Hold*

******* *Unhold Rx*

*List One Patient’s* Arc *hived Rx’s*

******* *New Prescription Entry*

******* *Partial Prescription*

******* *Refill Prescriptions*

******* *Reprint an Outpatient Label*

******* *View Prescriptions*

***** These options or suboptions from Outpatient Pharmacy V. 7.0 have been modified for CMOP.

#### Barcode Rx Menu

This *Barcode Rx Menu* contains options that allow batch barcoding for refills and renewals of prescriptions and an option to check the quality of the barcode print.

******* *Barcode Batch Prescription Entry*

*Check Quality of Barcode*

***** This option has been modified for CMOP and can be found under the *Barcode Rx Menu* on the *Rx (Prescriptions)* menu of Outpatient Pharmacy V. 7.0.

#### Barcode Batch Prescription Entry

This option is used to enter refills or renewals using barcodes in a batch entry.

***CMOP Functionality for Barcode Batch Prescription Entry***

Prescriptions entered using this option will be screened and suspended for CMOP transmission if all the CMOP criteria are met.

#### Cancel Prescriptions

The *Cancel Prescription* option allows the pharmacist to either discontinue a prescription without deleting its records from the files, or reinstate a cancelled prescription. A cancelled prescription remains on the patient profile and an entry in the activity log for the cancellation is made. The cancelled prescription will carry a status of Cancelled or C and cannot be refilled or reprinted.

The label can be entered or wanded if you are cancelling or reinstating the prescription by the prescription number or the patient name.

***CMOP Functionality for Cancel Prescription***

CMOP functionality for *Cancel Prescription* is the same as Outpatient Pharmacy V. 7.0. for all Rx’s. Reinstate screens **all** Rx’s for the CMOP criteria. If the Rx meets the criteria it is suspended for CMOP transmission and a message is displayed indicating the suspense date. If the fill date of a CMOP Rx is in the past, the prescription is reinstated, but not suspended for transmission. If the fill date is today or in the future, the CMOP Rx is suspended for CMOP processing for that date.

#### Edit Prescriptions

The pharmacy manager and pharmacist use the *Edit Prescriptions* option to edit information for a specific prescription. This option prints a label only if the prescription being edited has an Active status.

Copay will update the current copayment charge for a prescription, if and only if, an edit of the DAYS SUPPLY field changes the number of units charged. The updating procedure takes place in the background with no additional input required by the user. For example, a copayment charge unit is 30 days and the charge is $2.00. If a prescription was filled for 31 days, the charge would be $4.00. If the prescription was filled for 60 days, the charge would still be $4.00. Editing the PATIENT STATUS field does **not** update or change copayment status or charges for the prescription.

***CMOP Functionality for Edit Prescriptions***

Currently CMOP prescriptions may not be edited during the transmission process. The following criteria are required for editing of CMOP prescriptions.

DRUG NAME – CMOP to NON-CMOP and vice versa.

1. Edit – If the Rx has **ever** been transmitted (loading/transmitted) to the CMOP – No Edit.
2. If the Rx has **never** been released – Allow Edit.

MAIL/WINDOW – Currently able to be edited at each fill level.

1. If the original is in suspense, “Queued for Transmission” for CMOP, and is edited from MAIL to WINDOW, the Rx is not transmitted. It is handled as any Outpatient Pharmacy Rx.

1. No editing is allowed if the Rx is loading or transmitting to the CMOP.

1. Editing a CMOP window Rx (not on suspense) to mail does **not** send the Rx to the CMOP.

1. A window CMOP Rx on suspense edited to mail is “Queued for Transmission” to the CMOP.

1. If editing a refill which is the most current fill then the same rules apply. Edits of past fills do not affect CMOP.

TRADENAME – Currently able to be edited at each fill level.

1. A CMOP Rx entered with a tradename will not be sent to CMOP:

If deleting a tradename and the last fill is in suspense, change the entry to “Queued for Transmission” to the CMOP.

*View Prescriptions* will look odd, but the CMOP group stated this was acceptable.

CRITERIA FOR EDITING OTHER FIELDS -

1. If Rx released, **no editing** of

ISSUE DATE

FILL DATE

1. If fill being edited has been transmitted, **no editing** of

QUANTITY

DAYS SUPPLY

# OF REFILLS

1. The following fields may be edited:

PATIENT STATUS

PROVIDER

CLINIC

SIG

COPIES

METHOD OF PICKUP

REMARKS

DIVISION

PHARMACIST

LOT # (LOT # field in OP V. 7.0)

+	If a medication error is discovered on a CMOP transmitted prescription, the user should contact the CMOP and request the prescription be cancelled on the vendor system.

#### Hold Features

The *Hold Features* menu contains the options listed below for the hold features. When using this menu the user can place a prescription on hold, generate a list of prescriptions on hold, or remove a prescription from hold.

******* *Hold Rx*

*List Prescriptions on Hold*

******* *Unhold Rx*

***** These options have been modified for CMOP and can be found on the *Rx (Prescriptions)* menu of Outpatient Pharmacy V. 7.0.

#### Hold Rx

This function allows the pharmacist to place a prescription on hold.

***CMOP Functionality for Hold Rx***

CMOP Rx’s cannot be placed on hold during CMOP transmission.

#### Unhold Rx

This suboption allows the pharmacist to move a prescription from a Hold status and place it in an Active status.

***CMOP Functionality for Unhold Rx***

The *Unhold Rx* option screens the Rx for CMOP criteria. If the criteria are met, the Rx is suspended for transmission to the CMOP and a message is displayed indicating the suspense date. The screening for CMOP is performed after the “MAIL/WINDOW” prompt and response.

#### New Prescription Entry

The *New Prescription Entry* option allows the user to enter new prescriptions or renew existing prescriptions.

***CMOP Functionality for New Prescription Entry***

On prescription order entry, CMOP drug/items marked as “MAIL” are automatically placed on suspense and flagged for transmission to the CMOP host facility. CMOP drug/items marked as “WINDOW” are **not** automatically suspended or flagged for transmission, but are processed in the usual manner for windows. All screens, system/site parameter checks, etc., are performed in the background, therefore, transparent to the user.

If the fill date entered is today, on completion of Rx order entry for a patient, the normal prompt, “LABEL: QUEUE/HOLD/SUSPEND or ^ to bypass”, is presented.

After the user’s response, a message is displayed listing CMOP Rx’s which have been suspended for CMOP transmission.

If the fill date is in the future, the queue/hold/suspend/bypass prompt is not displayed. Only the CMOP transmission is displayed.

**Example: New Prescription Entry**

Select Outpatient Pharmacy Manager Option: **RX** (Prescriptions)

Select Rx (Prescriptions) Option: **N** ew Prescription Entry

Select PATIENT NAME: **CMOPPATIENT3,ONE** 02-23-74     000579013

MAS ELIGIBILITY: OTHER FEDERAL AGENCY

WEIGHT(Kg):                              HEIGHT(cm):

DISABILITIES:

123 OAK STREET

PLANO  TEXAS  75024

DATE OF BIRTH: FEB 23,1974// **&lt;RET&gt;**

STREET ADDRESS [LINE 1]: 123 OAK STREET// **&lt;RET&gt;**

STREET ADDRESS [LINE 2]: **&lt;RET&gt;**

STREET ADDRESS [LINE 3]: **&lt;RET&gt;**

CITY: PLANO// **&lt;RET&gt;**

STATE: TEXAS// **&lt;RET&gt;**

ZIP+4: 75024// **&lt;RET&gt;**

PHONE NUMBER [RESIDENCE]: 5555555555// **&lt;RET&gt;**

CNH CURRENT: **&lt;RET&gt;**

FEE HOSPITAL I.D.: **&lt;RET&gt;**

TEMPORARY ADDRESS ACTIVE?: NO// **&lt;RET&gt;**

REMARKS: **&lt;RET&gt;**

# RX #    DRUG                          STAT QTY ISS-DT LST-FL REF-RM DAYS

1    15151   AMPICILLIN 250MG/5ML SUSP      S    30 10-26  10-26   11     30

* indicates prescription is not renewable

(R) indicates last fill returned to stock

Press RETURN to continue: **&lt;RET&gt;**

ALLERGIES:

ADVERSE REACTIONS:

RENEW 1 – 1 &gt; **&lt;RET&gt;**

NEW RX FOR CMOPPATIENT3,ONE?:  (Y/N/P/R/A): Y// **&lt;RET&gt;** ES

PATIENT STATUS: OTHER FEDERAL// &lt;RET&gt;

DRUG: ISONIAZID

1   ISONIAZID 100MG TAB             AM500

2   ISONIAZID 100MG/ML INJ             AM500     N/F

3   ISONIAZID 300MG TAB             AM500

CHOOSE 1-3: 1

Checking for Drug/Drug Interactions !

SIG: **BID** (TWICE A DAY)

QTY ( TAB ) : **60**

COPIES: 1// **&lt;RET&gt;** 1

DAYS SUPPLY:  (1-90): 30// **&lt;RET&gt;**

# OF REFILLS:  (0-11): 11// **&lt;RET&gt;**

PROVIDER: CMOPPROVIDER1,TWO

CLINIC: 1 WEST

MAIL/WINDOW: WINDOW// **MAIL**

REMARKS: **&lt;RET&gt;**

ISSUE DATE: TODAY// **&lt;RET&gt;** (JAN 03, 1997)

FILL DATE:  (1/3/97 – 99/99/99): TODAY// **&lt;RET&gt;** (JAN 03, 1997)

Rx # 15266             01/03/97

CMOPPATIENT3,ONE                  #60

TWICE A DAY

ISONIAZID 100MG TAB

CMOPPROVIDER1,TWO               CMOPPHARMACIST2,THREE

# of Refills: 11

Is this correct? YES// **&lt;RET&gt;**

NEW RX FOR CMOPPATIENT3,ONE?:  (Y/N/P/R/A): Y// **N** O

LABEL: QUEUE/HOLD/SUSPEND or '^' to bypass Q// **&lt;RET&gt;** UEUE

RX# 15266  SUSPENDED FOR CMOP TRANSMISSION  01-03-97.

Select PATIENT NAME: **&lt;RET&gt;**

***Renew***

On renew, the data from the original Rx is passed to the renewed Rx. Once renewed, the “Edit renewed Rx? ” prompt is displayed. Mail/window must be reviewed for each Rx renewed. The “ MAIL/WINDOW” prompt appears after the first “FILL DATE” prompt.

**Example: Renew a Prescription**

Select Outpatient Pharmacy Manager Option: **RX** (Prescriptions)

Select Rx (Prescriptions) Option: **N** ew Prescription Entry

Select PATIENT NAME: **CMOPPATIENT3,ONE** 02-23-74     000579013

ELIGIBILITY: AID &amp; ATTENDANCE

WEIGHT(Kg):                              HEIGHT(cm):

DISABILITIES:

123 OAK STREET

ANYTOWN  TEXAS  75024

DATE OF BIRTH: FEB 23,1974// **&lt;RET&gt;**

STREET ADDRESS [LINE 1]: 123 OAK STREET// **&lt;RET&gt;**

STREET ADDRESS [LINE 2]: **&lt;RET&gt;**

STREET ADDRESS [LINE 3]: **&lt;RET&gt;**

CITY: PLANO// **&lt;RET&gt;**

STATE: TEXAS// **&lt;RET&gt;**

ZIP+4: 75024// **&lt;RET&gt;**

PHONE NUMBER [RESIDENCE]: 5555555555// **&lt;RET&gt;**

CNH CURRENT: **&lt;RET&gt;**

FEE HOSPITAL I.D.: **&lt;RET&gt;**

TEMPORARY ADDRESS ACTIVE?: NO// **&lt;RET&gt;**

REMARKS: **&lt;RET&gt;**

# RX #    DRUG                          STAT QTY ISS-DT LST-FL REF-RM DAYS

1    10882G  DIAZOXIDE 50MG CAP             A    60 07-11  10-19    2     15

2    11453D  HALOPERIDOL 20MG TAB           A*  100 07-11  10-19    3      5

3    15267   NAPROXEN 375MG TAB             S    60 01-03  01-03   11     30

4    10883F  QUINIDINE SULFATE 200MG TAB    A   120 07-11  10-19    1     30

* indicates prescription is not renewable

(R) indicates last fill returned to stock

Press RETURN to continue: **&lt;RET&gt;**

ALLERGIES:

ADVERSE REACTIONS:

RENEW 1 – 4 &gt; **1**

FILL DATE:  (1/3/97 – 99/99/99): TODAY// **&lt;RET&gt;** (JAN 03, 1997)

MAIL/WINDOW: WINDOW// **MAIL**

Now Renewing Rx # 10882G   Drug: DIAZOXIDE 50MG CAP

Checking for Drug/Drug Interactions !

10882H       DIAZOXIDE 50MG CAP               QTY: 60  PHYS: CMOPPROVIDER1,TWO

# OF REFILLS: 4  ISSUED: 01-03-97  SIG: bidap  FILLED: 01-03-97

Edit renewed Rx ? Y// **&lt;RET&gt;** ES

ISSUE DATE: TODAY// **&lt;RET&gt;** (JAN 03, 1997)

FILL DATE:  (1/3/97 – 99/99/99): JAN 3,1997// **&lt;RET&gt;** (JAN 03, 1997)

PROVIDER: CMOPPROVIDER1,TWO // CMOPPROVIDER1,TWO

# OF REFILLS:  (0-11): 11// **&lt;RET&gt;**

REMARKS: RENEWED FROM RX # 10882G  Replace **&lt;RET&gt;**

MAIL/WINDOW: WINDOW// **MAIL**

CLINIC: 1 NORTH// **&lt;RET&gt;** 1 NORTH

Rx # 10882H            01/03/97

CMOPPATIENT3,ONE                   #60

bidap

DIAZOXIDE 50MG CAP

CMOPPROVIDER1,TWO               CMOPPHARMACIST2,THREE

# of Refills: 11

Is this correct? YES//

NEW RX FOR CMOPPATIENT3,ONE ?:  (Y/N/P/R/A): Y// **N** O

LABEL: QUEUE/HOLD/SUSPEND or '^' to bypass Q// **&lt;RET&gt;** UEUE

RX# 10882H  SUSPENDED FOR CMOP TRANSMISSION  01-03-97.

Select PATIENT NAME: **&lt;RET&gt;**

**Partial Prescription**

By using this option the pharmacist can partially refill a prescription without eliminating one of the refills allowed by the original prescription.

***CMOP Functionality for Partial Prescription***

A partial fill entered for a CMOP prescription **cannot** be suspended. If a prescription is suspended for transmission to CMOP, the user can pull the prescription or enter a partial and print the label.

#### Refill Prescriptions

This option allows the pharmacy manager or pharmacist to process refills for existing prescriptions.

Copayment only affects this option in the background. You do not see a prompt relating to copayment for the *Refill Prescriptions* option. At the time of refilling a prescription, the computer system already knows the copayment eligibility of the veteran. When the prescription was first ordered, veteran eligibility for copayment was determined. If the veteran was charged a copayment for the original prescription, he or she will be charged for the refill.

+	Refill a prescription only after the original label has been printed. If you do not wait until after the original label has been printed you will produce a label for the last fill only.

***CMOP Functionality for Refill Prescriptions***

Refilled prescriptions are handled using the same functionality as *New Prescription Entry.* (See the *Rx (Prescriptions)* menu.)

#### View Prescriptions

With this option the user can view on screen the most complete information available for a specific prescription. The activity log lists the date, reason, prescription reference (Rx Ref), the initiator of the activity, and comments. The label log lists the date, prescription reference (Rx Ref), the person who printed it, and comments. Prescriptions in a Deleted status cannot be viewed.

***CMOP Functionality for View Prescriptions***

CMOP information related to this Rx has been added to the information displayed. The CMOP event log lists the date, prescription reference (RX REF), CMOP status, the CMOP, and comments.

**Example: View Prescriptions**

Select Outpatient Pharmacy Manager Option: **RX** (Prescriptions)

Select Rx (Prescriptions) Option: **V** iew Prescriptions

VIEW PRESCRIPTION: **383021** FAMOTIDINE 20 MG TAB

Rx View (Active)              Sep 23, 2005@16:30:13          Page:    1 of    1

CMOPPATIENT10,TEN

PID: 000-00-1165                                 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN 1,1965 (40)                             Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

--------------------------------------------------------------------------------

Rx #: 383021$e

Orderable Item: FAMOTIDINE TAB

CMOP Drug: FAMOTIDINE 20 MG TAB

*Dosage: 20MG

Verb: TAKE

Dispense Units: 1

Noun: TABLET

*Route: ORAL

*Schedule: 6

Patient Instructions:

SIG: TAKE ONE TABLET BY MOUTH 6

Patient Status: OPT NSC

Issue Date: 09/09/05                 Fill Date: 09/10/05

Last Fill Date: 09/10/05 (Mail, Transmitted)

Last Release Date:                              Lot #:

Expires: 09/10/06                       MFG:

Days Supply: 1                            QTY (TAB): 1

# of Refills: 11                       Remaining: 11

Provider: CMOPPROVIDER2,TWO

Routing: Mail

Copies: 1

Clinic: Not on File

Division: KENAI VA CBOC (463GB)

Pharmacist:

Patient Counseling: NO

Remarks:

Finished By: CMOPPHARMACIST3,THREE

Entry By: CMOPPHARMACIST3,THREE            Entry Date: 09/09/05 08:41:23

Original Fill Released:       Routing: Mail

Press RETURN to continue or "^" to exit: **&lt;RET&gt;**

Refill Log:

# Log Date   Refill Date  Qty               Routing  Lot #       Pharmacist

===============================================================================

There are NO Refills For this  Prescription

Partial Fills:

# Log Date   Date     Qty              Routing    Lot #        Pharmacist

===============================================================================

There are NO Partials for this Prescription

Activity Log:

# Date        Reason         Rx Ref         Initiator Of Activity

===============================================================================

1   09/09/05    SUSPENSE       ORIGINAL       CMOPPHARMACIST3,THREE

Comments: RX Placed on Suspense for CMOP until 09-10-05

2   09/09/05    PROCESSED      ORIGINAL       CMOPPHARMACIST3,THREE

Comments: Transmitted to LEAVENWORTH CMOP

Press RETURN to continue or "^" to exit: **&lt;RET&gt;**

Copay Activity Log:

# Date        Reason               Rx Ref         Initiator Of Activity

===============================================================================

There's NO Copay activity to report

Label Log:

# Date        Rx Ref                    Printed By

===============================================================================

There are NO Labels printed.

ECME Log:

# Date        Rx       Ref         Initiator Of Activity

===============================================================================

1   09/09/05@16:22:04    ORIGINAL       CMOPPHARMACIST3,THREE

Comments: Submitted to ECME: CMOP TRANSMISSION (NDC: 20233-0344-33)

ECME REJECT Log

# Date/Time         Rx Ref    Reject                       STATUS

===============================================================================

1   9/09/05@16:24:14  ORIGINAL  DRUG UTILIZATION REVIEW      UNRESOLVED

CMOP Event Log:

Date/Time             Rx Ref  TRN-Order       Stat             Comments

===============================================================================

09/09/05@0944         Orig    2686-1            TRAN

Press RETURN to continue or "^" to exit: **&lt;RET&gt;**

VIEW PRESCRIPTION: **&lt;RET&gt;**

Select Rx (Prescriptions) Option: **&lt;RET&gt;**

**Supervisor Functions**

The *Supervisor Functions* menu contains seventeen options that the package coordinator uses for implementation as well as maintenance of the various files for the basic running of the Outpatient Pharmacy software.

*Add New Providers*

*Daily Cost Compilation*

******* *Delete a Prescription*

****†*** *Drug Enter/Edit*

*Drug/Drug Interaction Functions...*

*Edit Provider*

*Initialize Cost Statistics*

*Inter-Divisional Processing*

*Inventory Menu*

*Lookup Clerk by Code*

*Mark/Unmark Lab Monitor Drugs*

*Medication Instruction File Add/Edit*

*Monthly Cost Compilation*

*Pharmacist Enter/Edit*

*Recompile AMIS Data*

*Site Parameter Enter/Edit*

*View Provider*

***** These options from the Outpatient Pharmacy V. 7.0 *Supervisor Functions* menu have been modified for CMOP.

**†** An example of this option can be found under the *CMOP Drug/Item Management* menu and the *Outpatient Pharmacy Manager* menu in this manual. This option has been modified for CMOP and can be found on the *Outpatient Pharmacy Manager* menu, the *Maintenance (Outpatient Pharmacy)* menu, and the *Supervisor Functions* menu of Outpatient Pharmacy V. 7.0.

#### Delete a Prescription

The pharmacy manager uses this option to change a prescription status to Deleted. Deleted prescriptions do not appear on any profiles.

+	In Outpatient Pharmacy V. 7.0 a released prescription can only be deleted **after** it has been returned to stock.

***CMOP Functionality for Delete a Prescription***

A CMOP prescription cannot be deleted if the status is Transmitted or Dispensed.

### Suspense Functions

The *Suspense Functions* option produces a menu that allows the user to print or delete various entries in the RX SUSPENSE file (#52.5) and print out statistics about entries in the RX SUSPENSE file (#52.5). This file contains prescription labels that have been suspended for printing at a later time. Each prescription label has an associated suspense date which is the fill or refill date.

Copayment only affects this option in the “background”. If a prescription has a copayment charge and is placed in the RX SUSPENSE file (#52.5), the copayment document is printed and a charge is generated when the label prints.

******* *Change Suspense Date*

*Count of Suspended Rx’s by Day*

******* *Delete From Suspense File*

*Log of Suspended Rx’s by Day (this Division)*

******* *Print From Suspense File*

******* *Pull Early From Suspense*

******* *Reset and Print Again*

***** These options from Outpatient Pharmacy V. 7.0 have been modified for CMOP.

#### Change Suspense Date

This option allows the pharmacist to change the suspense date for a specific prescription. The new suspense date becomes the fill/refill date automatically. With this option the pharmacist is also able to delete a specific prescription from suspense.

***CMOP Functionality for Change Suspense Date***

For CMOP prescriptions, suspense dates are changed, the Rx is “unmarked” for transmission for the original date, and then “marked” for transmission for the new suspense date. The user is **not notified** that the suspense date change was for a CMOP Rx.

#### Delete From Suspense File

This option allows the manager to delete from the RX SUSPENSE file (#52.5) the records of all the prescriptions which have already been printed prior to the user specified number of days. This specified number of days must be set from 7 to 90 days at the “DAYS PRINTED RX STAYS IN 52.5” prompt in the *Site Parameter Enter/Edit* option. The task is set to run every 7 days at the user specified time. The user may also requeue or dequeue this task using this option. Once a prescription is deleted from suspense, it cannot be reset for reprinting.

***CMOP Functionality for Delete From Suspense File***

CMOP prescriptions will not be deleted from the RX SUSPENSE file (#52.5) during the data transmission process.

#### Print From Suspense File

This option allows the user to print labels from the RX SUSPENSE file. First, enter the “Print Through” date. Any prescriptions with a suspense date on or before the date entered will print. Additionally, if a patient has at least one prescription on or before the date entered, any other prescriptions for that patient that are in suspense for the specified number of days defined in the Days to Pull from Suspense fields (#3, #3.1, #3.3, #3.4) of the OUTPATIENT SITE file (#59) will be pulled from suspense and printed.

For example, if today’s date is entered and Patient A has a prescription to be printed through today, all of Patient A's prescriptions for today and the number of days set in the DAYS TO PULL SUSP LOCAL NON-CS field (#3) in the OUTPATIENT SITE file (#59) will be printed. If there are no prescriptions for Patient A through  today, no labels will print.

A short profile for every patient for whom you are printing a label for a new prescription is also printed if your site parameters are set for this profile.

***CMOP Functionality for Print From Suspense File***

A date range is selected and “scanned ahead” for a pre-selected number of days to collect all entries on patients for this transmission. “Days to print from suspense” is currently a site parameter in Outpatient Pharmacy Version 7.0.

Selecting the *Print From Suspense File* option displays the following for users who hold the CMOP security keys, PSXCMOPMGR and PSX XMIT:

1 – Initiate Standard CMOP Transmission

2 – Initiate CS CMOP Transmission

3 – Print Current Division – Standard CMOP from Suspense

4 – Print Current Division – CS CMOP from Suspense

5 – Standard Print from Suspense

Select (1, 2, 3, 4, 5):

1-Initiate Standard CMOP Transmission will gather (Non-Controlled Substances) CMOP data “Queued for Transmission” for the selected date range and transmit to the CMOP. The sender will receive a “Transmission Confirmation” message via MailMan when the data transmission is completed.

+	Prior to transmitting, the data will be screened for exceptions (window, tradename, non-CMOP, Refill-Too-Soon/DUR rejects, Reject Resolution Required rejects, etc.). (See CMOP Transmission Process for additional information.)

2-Initiate CS CMOP Transmission will gather Controlled Substances CMOP data “Queued for Transmission” for the selected date range and transmit to the CMOP. The sender will receive a “Transmission Confirmation” message via MailMan when the data transmission is completed.

+	Prior to transmitting, the data will be screened for exceptions (window, tradename, non-CMOP, Refill-Too-Soon/DUR rejects, Reject Resolution Required rejects, etc.). (See CMOP Transmission Process for additional information.)

3-Print Current Division – Standard CMOP from Suspense gathers Non-Controlled Substances data for the selected date range and prints the labels. NO DATA will TRANSMIT to the CMOP.  Drugs or items for all labels printed should be filled locally. All usual outpatient prompts will be displayed.

+	The entries are automatically sorted by Patient name and the “SORT BY PATIENT NAME OR ID#: (P/I)” prompt is not displayed.

4-Print Current Division – CS CMOP from Suspense gathers Controlled Substances data for the selected date range and prints the labels. NO DATA will TRANSMIT to the CMOP.  Drugs or items for all labels printed should be filled locally. All usual outpatient prompts will be displayed.

+	The entries are automatically sorted by Patient name and the “SORT BY PATIENT NAME OR ID#: (P/I)” prompt is not displayed.

5-Standard Print from Suspense will print all labels for Rx's NOT 'Queued to Send' for the selected date range.  All usual outpatient prompts will be displayed.

+	Combinations of the selections presented above are allowed with the exception of 1,2 or 2,1.

#### Pull Early From Suspense

This option is used by the pharmacy manager, pharmacist, or the technician to pull a specific prescription or all prescriptions for a patient from the RX SUSPENSE file (#52.5) early.

***CMOP Functionality for Pull Early From Suspense***

A CMOP prescription can be pulled from suspense only if the CMOP INDICATOR is set to “Queued for Transmission”. The prescription is marked as printed and the CMOP INDICATOR reset to “Printed Locally”. The Rx is **not** transmitted to the CMOP and the user is **not notified** that a CMOP prescription was printed.

#### Reset and Print Again

This reset/reprint option allows the manager to reset the RX SUSPENSE file (#52.5) so that labels that have already been printed once can be printed again. This routine is useful if certain portions of the previously printed labels are unusable.

**+** This option **only** resets for the date range specified by the user. The DAYS TO PULL SUSP CMOP NON-CS site parameter is **not** taken into consideration during reset.

Labels are printed through the date selected by the user.

A short profile for every patient for whom you are printing a label for a new prescription may also be printed if your site parameters are set for this profile.

***CMOP Functionality for Reset and Print Again***

Selecting the *Reset and Print Again* option displays the following only to users who hold the CMOP security keys, PSXCMOPMGR and PSX XMIT:

1-Reset CMOP and Transmit

2-Reset CMOP and Print Again

3-Standard Reset and Print Again

Select (1,2,3): **1** Reset CMOP and Transmit

1-Reset CMOP and Transmit resets CMOP entries which have “printed but not transmitted” for the selected date range. The user is prompted for a date to transmit through and the transmission is queued.

Are you sure you want to continue?  NO//

Yes – Resets CMOP data and transmits to the CMOP.

No – Exits.

Select (1,2,3): **2** Reset CMOP and Print Again

2-Reset CMOP and Print Again resets and prints labels for CMOP entries which have been printed by the *Print CMOP from Suspense* option and have not transmitted. There is **no data transmitted** to the CMOP. The Rx’s for the labels printed must be filled locally.

Are you sure you want to continue?  NO//

Yes-Resets CMOP data and prints labels.

No-Exits.

Select (1,2,3): **3**

3-Standard Reset and Print Again  resets and prints all outpatient labels not “Queued for Transmission” and usual outpatient prompts are displayed.

+	No provision is made to allow print of labels for CMOP data which has already “transmitted.”

### Update Patient Record

The *Update Patient Record* option allows the user to add a new patient to the system or to update the current patient information in the computer.

***CMOP Functionality for Update Patient Record***

New functionality to this option has been added to decide at a patient level whether a patient’s Rx’s will be transmitted to the CMOP.

**Example: Update Patient Record**

Select Outpatient Pharmacy Manager Option: **UPDATE** Patient Record

Select Patient: **CMOPPATIENT3,ONE** 02-23-74     000579013

CMOPPATIENT3,ONE                        ID#:   000-57-9013

123 OAK STREET                          DOB:   FEB 23,1974

PLANO                                 PHONE:   5555555555

TEXAS  75024                           ELIG:

WEIGHT(Kg):                              HEIGHT(cm):

DISABILITIES:

ALLERGIES:

ADVERSE REACTIONS:

SOCIAL SECURITY NUMBER: 000579013// **^**

&gt;&gt;PHARMACY PATIENT DATA&lt;&lt;

CAP: SAFETY// **&lt;RET&gt;**

MAIL: DO NOT MAIL// **??**

This field is used to:

A) Determine whether this patient's Rx's are to be sent to the CMOP, or

retained for local distribution. If 2-4 are selected, none of this

patient's Rx's will be transmitted to the CMOP.

B) Select what the mail priority is.  The CMOP choices are limited to (0)

REGULAR and (1) CERTIFIED. Local mail may be designated (3) LOCAL -

REGULAR or (4) LOCAL – CERTIFIED. The 'DO NOT MAIL' code (2) may be used

to ensure that the patient's Rx's are not mailed.

Choose from:

0        REGULAR MAIL

1        CERTIFIED MAIL

2        DO NOT MAIL

3        LOCAL – REGULAR MAIL

4        LOCAL – CERTIFIED MAIL

MAIL: DO NOT MAIL// **&lt;RET&gt;**

DIALYSIS PATIENT: **&lt;RET&gt;**

MAIL STATUS EXPIRATION DATE: **??**

Examples of Valid Dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T   (for TODAY),  T+1 (for TOMORROW),  T+2,  T+7,  etc.

T-1 (for YESTERDAY),  T-3W (for 3 WEEKS AGO), etc.

If the year is omitted, the computer uses the CURRENT YEAR.

This field places a time limit on the 'Do Not Mail', 'Local – Regular

Mail' and 'Local – Certified Mail' conditions in the 'MAIL' field.

If a date is placed in this field and the software detects that the date

the Rx is processed is greater than the date in the field (past the

expired date) a default value of 'Regular Mail' will be assumed for the

'MAIL' field.

> **NOTE:** The actual value of the 'MAIL' field will not be changed by the

software, but can only be modified by a user editing the 'MAIL' field.

MAIL STATUS EXPIRATION DATE: **T** (FEB 24, 1997)

NARRATIVE: **&lt;RET&gt;**

PATIENT STATUS: SC// **^**

### Third Party Electronic Claims Submission of CMOP Prescriptions

Patch PSX*2*48 modifies the CMOP application to submit electronic claims for prescriptions that are transmitted to CMOP centers to be filled and dispensed remotely. All the prescriptions that are ready to be included on the batch to be transmitted to CMOP are first transmitted to the third party insurance. Once this first step is completed, the system waits 60 seconds before starting the actual transmission to CMOP. This process will affect the existing CMOP functionality in two ways:

1. If a response from the third party payer is not received by the time the prescription is about to be transmitted to CMOP, it is skipped and remains in the queue for the next CMOP transmission. A MailMan message containing all the prescriptions that were skipped and that remain in the queue is generated at the end of the process and is transmitted to all the holders of the PSXMAIL security key. If no users on the system have this key, the message is sent to all the users holding the PSXCMOPMGR security key.
2. Under certain conditions, the prescription is not sent to CMOP and remains in the queue to be transmitted after the third party reject is resolved:

- The third party payer rejects the claim due to a DUR or a Refill Too Soon finding.
- The patient eligibility is TRICARE or CHAMPVA and the third party payer rejects the claim for any reason.
- The patient eligibility is VETERAN, the prescription is an original fill that is unreleased, the third party payer rejects the claim due to a Reject Resolution Required reject, and the total gross amount of the prescription is at or above the user defined threshold amount for the Reject Resolution Required reject.

The prescription will not be transmitted to CMOP until the reject is resolved by the user through the Outpatient Pharmacy V. 7.0 application. Two options have been created for the pharmacy users to resolve these rejects:

*Third Party Payer Rejects – Worklist	[PSO REJECTS WORKLIST]*

*Third Party Payer Rejects – View/Process	[PSO REJECTS VIEW/PROCESS]*

The above options reside in the *ePharmacy Menu* [PSO EPHARMACY MENU] option, which can be found under the *Rx (Prescriptions)* [PSO RX] option.

Patch PSX*2*65 modifies the CMOP application to prevent ePharmacy prescriptions from being pulled early from suspense until 3/4 of the days’ supply of the Rx/fill has elapsed. The system will not hold a prescription for 3/4 days’ supply when the:

- Previous fill was not ECME billable
- Rx is flagged for SC or EI
- Rx is non-billable
- Patient does not currently have insurance

Patch PSX*2*65 also modifies the CMOP application to prevent ePharmacy prescriptions from being filled/sent to CMOP when a host processing error occurs when a claim is submitted through ECME. The host processing errors are identified by ePharmacy reject codes M6, M8, NN, and 99. The following conditions apply when this scenario occurs:

- The transmission of the Rx/fill will be delayed 1 day in hopes that the host processing issues will be resolved.
- An activity log entry will be defined to state the date/time along with a comment stating that the Rx/fill was left in suspense hold due to a host processing error.

- This added functionality does not include the Pull Early from Suspense function.

The 3/4 days supply processing can be bypassed for billable prescriptions with third party insurance by using the hidden action “BY” on the Outpatient Medications Screen or selecting option “BY” on the ePharmacy Menu. The user will have the ability to undo the Bypass from the Outpatient Medications Screen.

## CHAPTER 2: HOST CMOP FACILITY

## Section 1: CMOP System Management Menu

<!-- image -->

**PSXCMOPMGR**

Management personnel use this menu to control operations of the Consolidated Mail Outpatient Pharmacy.

*Transmission Review*

*Interface Menu ...*

*Operations Management ...*

*Display System Status*

*Reports Menu ...*

*Rx Inquiry*

*Manual/Barcode Release Prescription*

*Unhold Transmission*

*View Transmission*

*Enter/Edit Transmission Comments*

*CMOP Drug/Item Management ...*

*Facility Cost Management ...*

*Archive CMOP Data ...*

**Getting Out of an Option**

To stop what you are doing, enter an up-arrow (^). You can use the up-arrow at any prompt to terminate the line of questioning and return to the previous level in the routine. Continue entering up-arrows to completely exit from the system.

### Transmission Review

<!-- image -->

**PSXCMOPMGR**

With this option the user can display the status of current transmissions. The user can print a summary of all statuses or a summary for each status. The following is an explanation of the statuses:

S = Summary

Q = Queued

P = Processed

C = Closed

H = Hold

L = Labels Printed

**Example: Transmission Review**

Select CMOP System Management Menu Option: **T** ransmission Review

Select one of the following:

S         Summary

Q         Queued

P         Processed

C         Closed

H         Hold

L         Labels Printed

Select: Q// **S** ummary

Select one of the following:

A         Ascending Order

D         Descending Order

Enter response: Ascending// **A** scending Order

Enter Begin Date for Report:  TODAY// **T-30** (FEB 22, 1997)

Enter End Date for Report:  TODAY// **T** (MAR 24, 1997)

DEVICE: [Select Print Device]

report follows on the next page

TRANSMISSIONS SUMMARY

2/22/97 THRU 3/24/97

RECEIVED            FROM                   BATCH      TOTAL    TOTAL   STATUS

DATE/TIME                                  NUMBER     ORDERS    RXS

------------------------------------------------------------------------------

FEB 25,1997@09:32   BIRMINGHAM             521-750       1        3  Closed

FEB 25,1997@15:53   BIRMINGHAM             521-751       1        2  Hold

FEB 25,1997@15:55   BIRMINGHAM             521-752       1        2  Hold

MAR 6,1997@13:41    BIRMINGHAM             521-753       3       10  Processed

MAR 7,1997@09:34    BIRMINGHAM             521-754       1        1  Queued

MAR 18,1997@09:55   BIRMINGHAM             521-755       1        1  Closed

MAR 18,1997@14:20   BIRMINGHAM             521-756       1        1  Closed

MAR 20,1997@14:25   BIRMINGHAM             521-757       2        5  Closed

MAR 20,1997@15:11   BIRMINGHAM             521-758       1        2  Hold

MAR 20,1997@15:13   BIRMINGHAM             521-759       1        2  Hold

MAR 20,1997@15:20   BIRMINGHAM             521-760       1        2  Closed

MAR 24,1997@13:54   BIRMINGHAM             521-761       3        6  Queued

MAR 24,1997@14:01   BIRMINGHAM             521-762       3        6  Closed

MAR 24,1997@14:03   BIRMINGHAM             521-763       1        2  Closed

Press RETURN to continue: **&lt;RET&gt;**

Select CMOP System Management Menu Option: **&lt;RET&gt;**

### Interface Menu

This menu contains options which control the operations of the CMOP interface. When the user enters the *Interface Menu* the one of the following current statuses of the interface communication link is displayed.

A	All Transmissions Queued. Sends all transmissions in the queue to the vendor. The interface will NOT stop after all transmissions have been sent to the vendor system.

S	Single Transmission. Only sends the transmission selected to the vendor. The interface will stop when the transmission download has completed.

P	Prioritize Queue. Allows the user to establish a priority for sending transmissions to the vendor. The interface will NOT stop after all transmissions have been sent to the vendor.

Q	Query Request. Allows the user to initiate a query request. Once the query request is complete the interface stops.

*Monitor CMOP Interface*

*Start CMOP Interface*

*Stop CMOP Interface*

#### Monitor CMOP Interface

<!-- image -->

**PSXCMOPMGR**

This option is used to display the CMOP Interface Log. The log contains the date and time and message. (See Appendix A for a complete listing of the Interface Log messages.)

#### Start CMOP Interface

<!-- image -->

**PSXCMOPMGR**

With this option the user activates the communication link with the vendor system and enables the transfer of data from the VistA CMOP system to the vendor for dispensing. When the CMOP Manager selects the *Start CMOP Interface* option the following four selections are displayed:

*All Transmissions Queued*

This selection will start the interface and download all transmissions in FIFO order. Once the queue is empty a query request will be initiated. The interface remains running and future transmissions will be downloaded as soon as they are queued. If no transmissions are in the queue, query requests will be initiated as per the “Query Request Interval” site parameter.

*Single Transmission*

The CMOP Manager has the option to download a single transmission to the vendor if the queue priority parameter is set to prioritize. Only one transmission number can be entered. This transmission will download to the vendor, all other transmissions will remain in the queue. Once the transmission has been downloaded to the vendor, the interface will be stopped.

*Prioritize Queue*

If Prioritize Queue is selected a report of the current queue will be displayed. This report will list all transmissions waiting to be downloaded to the vendor and will be in first-in first-out (FIFO) order. Each transmission will be assigned a sequence number in the report. At the end of the report, the prompt, “Prioritize Queue NO//” will be displayed. If the default of NO is selected the transmissions will be downloaded in FIFO order. If YES is selected, the prompt “Enter Queue Order:” will be displayed. The user will enter the sequence to download the transmissions. The transmissions will be resequenced in this order. If the report displays 10 transmissions, and the user wants to put sequence number 6 at the head of the queue and let the other transmissions download in FIFO order, they only need to enter 6 at the Enter Queue Order prompt. If the user doesn’t enter a sequence, the default will be to download the transmissions in FIFO order. Only those transmissions that are in the queue when this report is printed will be affected by the prioritization process. The interface will continue to run downloading transmissions as they are queued or initiating queries.

*Query Request*

This selection allows the CMOP Manager to initiate a query without downloading transmissions. Once the query is completed the interface will be stopped. If the Query Request Interval has not expired and this option is selected, a message similar to the following will be displayed.

“Another query cannot be initiated for 52 minutes.”

**Example: Start the CMOP Interface**

Select CMOP System Management Menu Option: **I** nterface Menu

Select Interface Menu Option: **STA** rt CMOP Interface

Select one of the following:

A         All Transmissions Queued

S         Single Transmission

P         Prioritize Queue

Q         Query Request

Enter response: A// **P** rioritize Queue

CMOP TRANSMISSION QUEUE

Feb 18, 1997@14:59

SEQ #  TRANSMISSION    DIVISION                RECEIVED DATE  ORDERS/RXS

------------------------------------------------------------------------------

1   521-590         Birmingham              Feb 18@04:30:35   120/165

2   589-131         Kansas City             Feb 18@05:10:45   54/67

3   521-591         Birmingham              Feb 18@06:07:03   354/411

4   589-130         Kansas City             Feb 18@05:00:00   360/548

PRIORITIZE QUEUE: NO// **Y** ES

Enter Priority: **1,4,2,3** [If the user wants the queue to go in the order, 4,1,2,3, entering 4 at this prompt will suffice.]

CMOP TRANSMISSION QUEUE

Feb 18, 1997@14:59

* Priority

SEQ #  TRANSMISSION    DIVISION                RECEIVED DATE  ORDERS/RXS

------------------------------------------------------------------------------

1   521-590         Birmingham              Feb 18@04:30:35   120/165

*    4   589-131         Kansas City             Feb 18@05:10:45   54/67

2   521-591         Birmingham              Feb 18@06:07:03   354/411

3   589-130         Kansas City             Feb 18@05:00:00   360/548

Accept Sequence? YES// **&lt;RET&gt;**

Press RETURN to start interface, "^" to quit:

*[The following screen will be displayed anytime one of the options have been selected. The screen will refresh every 30 seconds unless the user enters an ^.]*

*** Interface STARTED ***

CMOP SYSTEM STATUS

Interface             : RUNNING

Transmissions Queued  : 1.................Orders/Rx's: 1/1

Last Order Processed  : 521-748-26........PHARMACY...............Feb 19@09:52

Last Query Completed  : #551..............1 Rx's.................Feb 19@09:52

*****Release Data Acknowledgements &gt; 24 hours OUTSTANDING*****

Background Process                        Last Ran               Scheduled For

Release Data Filed in Master Database.....Feb 26@14:47...........Feb 26@15:02

Database Purge............................Feb 25@16:13...........Feb 26@16:13

Release File Purge........................Feb 25@23:01...........Feb 26@23:01

Release Acknowledgement File Purge........Feb 25@23:30...........Feb 26@23:30

Enter "^" to quit **^**

*** Interface STARTED ***

Select Interface Menu Option: **&lt;RET&gt;**

**Example 2: Query Request**

Select Interface Menu Option: **START** CMOP Interface

Select one of the following:

A         All Transmissions Queued

S         Single Transmission

P         Prioritize Queue

Q         Query Request

Enter response: A// **Q** uery Request

Another query cannot be initiated for 52 minutes.

Select Interface Menu Option: **&lt;RET&gt;**

#### Stop CMOP Interface

<!-- image -->

**PSXCMOPMGR**

This option stops the CMOP interface data transmission.

### Operations Management

This menu manages the day to day operations of the background procedures necessary for transmission data management.

*Start/Stop Background Filer*

*Nightly Purge of CMOP Database*

*Nightly Purge of Release Data*

*Purge of Release Messages*

*Resend Release Data to VAMCs*

*System Parameter Enter/Edit*

#### Start/Stop Background Filer

This option enables the user to schedule or unschedule the background filer that files the released data in the CMOP MASTER DATABASE file (#552.4). When the user enters a starting date and time, the message “Job Started” is displayed. If the background filer is stopped the message “Job Stopped” is displayed.

#### Nightly Purge of CMOP Database

This option schedules or unschedules the nightly job to purge the CMOP DATABASE file (#552.2). To start the nightly purge of the CMOP database, enter the date and time.

#### Nightly Purge of Release Data

This option is used to schedule or unschedule the nightly background job to purge release data. To start the purge of release data, enter the date and time. All data already filed in the CMOP MASTER DATABASE file (#552.4) will be deleted.

#### Purge of Release Messages

With this option you are able to start or stop the background job that purges the stored data pertaining to the release data mail messages that are returned to the medical centers. You are asked to enter the number of days of data you want to keep. This number also determines the amount of data that will appear on the Report of Release Data Returned and the Resend Release Data reports. For example, if you enter 10 days, then each of the reports will provide information for that number of days. Any data older than 10 days will be purged.

#### Resend Release Data to VAMCs

This option provides you with a report by medical center of any release data mail messages that have not been acknowledged within 24 hours. A release data mail message is one that has been returned by the medical center and completely filed at the CMOP facility. At the end of the report you will receive the prompt, “Resend Messages”. You can enter a list of numbers separated by commas. The specified messages will be returned to the medical center as one new mail message. If there aren’t any unacknowledged messages for the medical center selected, the you will get the message, “No data for the report”. This report can be sent to the screen or it can be sent to a printer.

**Example: Resend Release Data**

Select Operations Management Option: **Resend** Release Data to VAMCs

Select Facility or RETURN for all: &lt; **ENT** &gt;

DEVICE: [Select Print Device]

RELEASE DATA RETURNED SINCE Feb 16, 1997

BIRMINGHAM, AL.

PRINTED Feb 25, 1997

DATE/TIME DATA RETURNED             Rx's    ACKNOWLEDGED

========================================================

Feb 19, 1997 1:52:34 pm               15        YES

Feb 24, 1997 10:16:39 am               7        NO

========================================================

TOTAL                 RETURNED                  22

ACKNOWLEGDED              15

NOT ACKNOWLEDGED           7

TOTALS FOR ALL SITES  RETURNED                  22

ACKNOWLEDGED              15

NOT ACKNOWLEDGED           7

Enter RETURN to continue or '^' to exit: &lt; **ENT** &gt;

Resend a Release Message? &lt; **ENT** &gt;

This is a required response. Enter '^' to exit

Resend a Release Message? **Y** ES

Select Facility: **521**

RELEASE DATA NOT ACKNOWLEDGED

BIRMINGHAM, AL.

Feb 25, 1997

MESSAGE   DATE/TIME DATA RETURNED    TOTAL Rx's

===============================================

1   Feb 24, 1997 10:11:63 am            7

Resend messages:  (1-1): 1

Enter time:  NOW// &lt; **ENT** &gt;  (FEB 25, 1997@15:45:06)

Job Started.

Select Operations Management Option: &lt; **ENT** &gt;

#### System Parameter Enter/Edit

This option displays the current site parameter settings and allows editing of those that can be changed.

**Query Request Interval** This parameter controls the time interval between query requests. The time is entered as hours or fractions of an hour.

**Query Limit Request** This parameter controls the number of Rx’s that the VistA system will accept during a query.

**Days to Retain Release** This parameter controls the number of days release

**Summary** acknowledgement summaries will be retained in the CMOP OPERATIONS file.

**CMOP Drug Cost** This parameter controls whether a CMOP DRUG Cost

**Missing Report** Missing error report is generated.

**Example: System Parameter Enter/Edit**

Select Operations Management Option: **S** ystem Parameter Enter/Edit

Query Request Interval:  1 hr // &lt; **ENT** &gt;  ( 1 hr )

Query Limit Request:  10000 // &lt; **ENT** &gt;

Days to Retain Release Summary:  10 // &lt; **ENT** &gt;

CMOP DRUG Cost Missing reports: YES// ?

Do you want the “CMOP DRUG Cost Missing” error report generated? (Y/N)

Choose from:

Y	YES

N	NO

CMOP DRUG Cost Missing reports: YES// &lt; **ENT** &gt;

Select Operations Management Option: &lt; **ENT** &gt;

### Display System Status

This option displays a screen of information for use by the CMOP Site Manager to review the status of CMOP processes. Information includes statuses on the CMOP interface, nightly background jobs, etc. This data should be reviewed regularly to ensure all processes are running as scheduled.

+	Release Data Acknowledgments &gt; 24 hours OUTSTANDING is a notification that release data has been returned to a remote medical center and not acknowledged within 24 hours. Use the *Resend Release Data* option to resend the data to the medical center.

+	Rejected Orders OUTSTANDING is a notification that patient order(s) have been rejected by the vendor system. The *Rejected Messages Report* option should be used to print a report of these orders.

**Example: Display System Status**

Select CMOP System Management Menu Option: **D** isplay System Status

CMOP SYSTEM STATUS

Interface             : STOPPED

Transmissions Queued  : Nothing in the Queue

Last Order Processed  : 521-3-12..........BIRMINGHAM (C).........Feb 26@10:16

Last Query Completed  : #3................7 Rx's.................Feb 26@10:16

*****Release Data Acknowledgments &gt; 24 hours OUTSTANDING*****

*****Rejected Orders OUTSTANDING*****

Background Process                       Last Ran               Scheduled For

Release Data Filed in Master Database....Feb 26@12:17...........Feb 26@12:32

Database Purge.......................................Not Scheduled

Release File Purge.......................Feb 25@23:00...........Feb 26@23:00

Release Acknowledgement File Purge.......Feb 25@23:30...........Feb 26@23:30

### Reports

<!-- image -->

**PSXCMOPMGR**

This menu provides reports available at the CMOP host facility which contain information on data transmissions received from remote facilities.

*Transmission Report Summary*

*Rejected Messages Report*

*Unreleased Rx's Report*

*Duplicate Release Data Report*

*Facility Activity Report*

*Turnaround Time Report*

*Report of Release Data Returned*

*Print Rejected Orders*

*Print Transmission Labels*

*Label Restart Utility*

*Reprint Transmission Labels*

#### Transmission Report Summary

This option is used to print a report of prescription data for the selected data transmission. The user can only select transmissions which are waiting to download to the automated system.

The report contains the data transmission number, facility, division, the date the transmission was received, total number of orders and prescriptions, and the name of the patient, SSN, Rx number, barcode, and drug name.

#### Rejected Messages Report

This option prints information for any rejected messages of a data transmission for review by the CMOP manager. The date range selected by the user is based on the processed date and time.

**Example: Rejected Messages Report**

Select CMOP System Management Menu Option: **RE** ports Menu

Select Reports Option: **REJ** ected Messages Report

ENTER BEGINNING DATE :  NOW// &lt; **ENT** &gt;

ENTER ENDING DATE :  NOW// &lt; **ENT** &gt;

DEVICE: [Select print device.]

**Example: Rejected Messages Report** (continued)

CMOP Rejected Messages for Transmission # 521-367

Printed : NOV 10,1997@10:27:13

Facility : BIRMINGHAM, AL.              Division:  BIRMINGHAM (C)

Received on  Nov 02, 1997 3:44          Total Orders:  4    Total Rx’s:  14

ORDER          NAME        RX NUMBER  BAR CODE       DRUG NAME

------------------------------------------------------------------------------

7  REJECTED REASON:   DATA ERROR

CMOPPATIENT3,ONE      11636A     521-52066      ALBUTEROL SULFATE 4MG TAB

10971E     521-52067      HALOPERIDOL 20MG TAB

10345K     521-52069      IBUPROFEN 600MG TAB

11757B     521-52070      ISONIAZID 100MG TAB

8  REJECTED REASON:   DATA ERROR

CMOPPATIENT4,ONE      11597E     521-52071      ALBUTEROL 90MCG 200D ORAL

11433E     521-52072      ALUMINUM CL HEXAHYDRATE 2

11247F     521-52073      AMINOPHYLLINE 100MG TAB

11325H     521-52074      AMITRIPTYLINE HCL 10MG TA

9  REJECTED REASON:   DATA ERROR

CMOPPATIENT5,ONE     15167      521-52057      NAPROXEN 375MG TAB

10  REJECTED REASON:   DATA ERROR

CMOPPATIENT18,ONE     11376D     521-52059      AMILORIDE HCL 5MG TAB

11417E     521-52060      AMPICILLIN 250MG/5ML SUSP

200012B    521-52062      FOLIC ACID 1MG TAB

11706E     521-52063      IBUPROFEN 600MG TAB

200011D    521-52064      ISONIAZID 100MG TAB

#### Unreleased Rx’s Report

With this option the user can print a summary of all prescription data in the CMOP Master Database that have not been released. The summary contains the facility, pharmacy division, date transmitted and received, the Rx number, drug ID, and the number of fills. The report will sort by the order number within the batches displayed.  This report can be printed for a selection of date ranges, facilities, and type of transmissions (Controlled Substances and Non-Controlled Substances).

#### Duplicate Release Data Report

This report may be accessed in one of two ways.

1) When the system automatically detects duplicate Rx’s, an alert is generated. Processing this alert will cause the report to print. Answering yes to the “Delete these Rx’s” release data purge prompt found at the end of the report will mark these Rx’s for deletion by the background filer.

2) The report can also be generated by using the option “PSX DUPLICATE RX PURGE”. This option performs the same function as #1 except it gives the user the chance to access the list of duplicates when necessary and not just when an alert is generated.

**Example: Duplicate Release Data Report**

Select CMOP System Management Menu Option: **D** uplicate Release Data Report

DEVICE: [Select Print Device]

Duplicate Rx Report

BIRMINGHAM, AL.

Rx #            Query #    Completed Time   Orig Qry    Orig Completed Time

----------------------------------------------------------------------------

15548               510    02/29/97@10:44        509    2/29/97@10:37

15549               510    02/29/97@10:44        509    2/29/97@10:37

15550               510    02/29/97@10:44        509    2/29/97@10:37

15551               510    02/29/97@10:44        509    2/29/97@10:37

15552               510    02/29/97@10:44        509    2/29/97@10:37

Delete these Rx's? YES// &lt; **ENT** &gt;

Select CMOP System Management Menu Option: &lt; **ENT** &gt;

#### Facility Activity Report

This option prints a report, by facility, for a selected date and time range. The report lists each transmission and the current count of Rx’s that are completed, cancelled, and unreleased at the time of the report.

#### Turnaround Time Report

This option queues the CMOP Rx Turnaround Time report for the selected date range. The report is based on the time difference between the transmission date and time and the date and time the pharmacist at the CMOP marked the prescription as completed and released. Information includes the average, minimum, and maximum turnaround times, and the total number of Rx’s released. Due to the time required to compile the data for this report, it can only be sent to a printer.

#### Report of Release Data Returned

This option provides a report by medical center of all release data that has been returned to the medical center. Totals for the number of Rx’s returned, Rx’s acknowledged, and Rx’s not acknowledged are provided for each medical center. A grand total is provided at the end of the report. At the end of the report, if there are messages that have not been acknowledged within a 24 hour period, you will receive the prompt, “Resend Messages”. If the you respond yes, the process will automatically go to the *Resend Release Data* option. If there are no unacknowledged messages, the user will not be prompted to resend messages. This report can be sent to the screen or to a printer.

#### Print Rejected Orders

This option allows the user to print all rejected orders for a selected transmission. Labels cannot be printed while the CMOP interface is running.

#### Print Transmission Labels

<!-- image -->

**PSXCMOPMGR**

This option allows printing of labels for prescription data received by the CMOP. The user selects a transmission Facility Batch number to be printed. All labels “Queued to send” for this transmission are printed.

#### Label Restart Utility

<!-- image -->

**PSXCMOPMGR**

This option enables the user to print a range of CMOP transmission labels that have jammed during normal or reprint label print operations.

**Example: Label Restart Utility**

Select CMOP System Management Menu Option: **RE** ports

Select Reports Option: **L** abel Restart Utility

CMOP LABEL RESTART UTILITY

To run the Label Restart Utility you will need the Rx number of the last USEABLE Rx that printed, as well as the CMOP Order # where the error occurred.

Did the error occur during Reprint? NO// **&lt;RET&gt;**

Enter Beginning CMOP Order #: 521-310-1

Enter Ending CMOP Order #: 521-310-4

Enter the last USABLE Rx number printed or 'RETURN' to start at the first Rx in order: **??**

You selected CMOP order # 521-310-1

If this is correct, please choose the last USABLE Rx that printed

from the following list:

CMOPPATIENT31,ONE

15112          ASPIRIN 325MG TAB

15114          CIMETIDINE 200MG TAB

Enter the last USABLE Rx number printed or 'RETURN' to start at the first Rx in order: **15112**

Select Label Printer: *[Select print device.]*

OK TO ASSUME LABEL ALIGNMENT IS CORRECT ?:  (Y/N): YES// **&lt;RET&gt;**

Requested Start Time: NOW// **&lt;RET&gt;** (FEB 20, 1997@10:21:21)

LABELS Queued to Print!!

Select Reports Menu Option: **&lt;RET&gt;**

#### Reprint Transmission Labels

<!-- image -->

**PSXCMOPMGR**

This option enables users at the host CMOP facilities to reprint transmission labels. To reprint the transmission labels, enter the facility-batch number.

### Rx Inquiry

<!-- image -->

**PSXCMOPMGR**

With this option the user can select a specific transmission and prescription for review.

**Example 1: Rx Inquiry Received, but not Released**

Select CMOP System Management Menu Option: **RX** Inquiry

Select Facility Batch Reference # : 521-473

TRANSMITTED :JAN 15,1997@11:58:15     RECEIVED   : JAN 15,1997@11:58:15

TO VENDOR  :

RX # : 11698C

ORIGINAL        DRUG ID : I0005       QTY : 120      COST :

RX STATUS : RECEIVED

Select Facility Batch Reference # : **&lt;RET&gt;**

Select CMOP System Management Menu Option: **&lt;RET&gt;**

**Example 2: Rx Inquiry Received and Released**

Select CMOP System Management Menu Option: **RX** Inquiry

Select Facility Batch Reference # : 521-336

TRANSMITTED :OCT 27,1996@15:29:13     RECEIVED   : OCT 27,1996@15:29:13

TO VENDOR  : NOV 17,1996@16:55:40

RX # : **11780B** REC'D FROM VENDOR  : NOV 17,1996@16:55:39

ORIGINAL        DRUG ID : V0006       QTY : 50       COST : 0.067

RX STATUS : PROCESSED       COMPLETED NOV 17,1996@16:55   AUTOMATED

NDC : 1234TEST5678          BY EMPLOYEE : CMOPPHARMACIST28,THREE

PROCESSED DT/TM : NOV 17,1996@17:03:46          QUERY ID # 311

LOT # : 1234TST     EXP DATE : JUL 7,1997

Select Facility Batch Reference # : **&lt;RET&gt;**

Select CMOP System Management Menu Option: **&lt;RET&gt;**

### Manual/Barcode Release Prescription

<!-- image -->

**PSXCMOPMGR**

This option allows the user at the host facility to release a prescription for a label printed by the VistA system. In order to manually release an Rx, the user must hold the PSXCMOPMGR key. This option is **not** used to release prescriptions dispensed by the automated non-VistA vendor system.

If an Rx is rejected by the vendor system it will remain on the CMOP system until it is printed and released. In some infrequent cases there is an Rx that should be cancelled instead of printed and released. This option has been created to handle the entry of the cancellation in the CMOP RELEASE file to allow the information to be returned to the VAMC and update the PRESCRIPTION file (#52).

**Example: Manual/Barcode Release Prescription**

Select CMOP System Management Menu Option: **M** anual/Barcode Release Prescription

This option will only release/complete Rx's which have labels printed manually

Select one of the following:

R         RELEASE

C         NOT DISPENSED

Enter response: **C** NOT DISPENSED

Enter Cancel Reason: QUANTITY OR DISPENSE PROBLEM.

Enter PHARMACIST: **CMOPPHARMACIST30** ,THREE        CT

Enter/Wand PRESCRIPTION number: **521-53319**

RX# 521-53319 not dispensed.

### Unhold Transmission

This option allows a user holding the PSXCMOPMGR key to remove a transmission from a Hold status and allows the transmission to download to the automated vendor system.

**Example: Unhold a Transmission**

Select CMOP System Management Menu Option: **Unhold Transmission**

Select CMOP REFERENCE FACILITY BATCH REFERENCE: 521-409

The original transmission, 521-408 has already been sent to the automated

vendor system.

Transmission, 521-409 is a retransmission of 521-408 and can not be queued.

Select CMOP System Management Menu Option: **&lt;RET&gt;**

### View Transmission

This option enables the user to display information for a specified transmission. The user must enter the facility number followed by the batch number to view the transmission.

**Example: View Transmission**

Select CMOP System Management Menu Option: **View Transmission**

Select CMOP REFERENCE FACILITY BATCH REFERENCE: 597-8881

VIEW TRANSMISSION

Transmission     : 597-8881            Transmitted  : Sep 14, 1996 10:13:08 am

Status           : Processed           Received     : Sep 14, 1996 10:28 am

Division         : LINCOLN             Processed    : Sep 14, 1996 10:46:01 am

Sender           : CMOPPHARMACIST30,THREE

Beginning order #: 1                   Total orders : 126

Ending order #   : 126                 Total Rx's   : 283

Select CMOP System Management Menu Option: **&lt;RET&gt;**

### Enter/Edit Transmission Comments

This option allows the host CMOP users to enter or edit transmission comments. The user selects this option to make notes or comments regarding a specific transmission. The batch number is entered, the batch information is displayed, and the user is prompted for comments.

**Example: Enter/Edit Transmission Comments**

Select CMOP System Management Menu Option: **E** nter/Edit transmission comments

Select CMOP REFERENCE FACILITY BATCH REFERENCE: 521-409

Transmission     : 521-409             Transmitted  : Nov 29, 1996 2:33:25 pm

Status           : Hold                Received     : Nov 29, 1996 2:33:57 pm

Division         : BIRMINGHAM (C)

Sender           : CMOPPHARMACIST30,THREE

Beginning order #: 1                   Total orders : 2

Ending order #   : 2                   Total Rx's   : 6

Retransmission of 521-408

COMMENTS:

1&gt;THIS IS A RETRANSMISSION OF 521-408 BECAUSE FIRST TRANSMISSION FAILED.

2&gt; &lt;RET&gt;

EDIT Option: **&lt;RET&gt;**

Select CMOP System Management Menu Option: **&lt;RET&gt;**

### CMOP Drug/Item Management

<!-- image -->

**PSXCMOPMGR**

This submenu is used by the CMOP Manager to perform operations required to transmit selected drug/items to the CMOP host facility.

*Loop CMOP Match to Local Drug File*

*CMOP Mark/Unmark (Single drug)*

*CMOP Data from Your Local Drug File*

*Drug Enter/Edit*

*Drugs not Flagged for CMOP Transmission*

#### Loop CMOP Match to Local Drug File

<!-- image -->

**PSNMGR**

This option allows users to select entries in the local DRUG file (#50), review NDF matches, and mark entries to transmit to the CMOP.

**Example: Loop CMOP Match to Local Drug File**

Select CMOP Site Manager Menu Option: **CMOP D** rug/Item Management

Select CMOP Drug/Item Management Option: **L** oop CMOP Match to Local Drug File

This option allows you to choose entries from your drug file and helps you

review your NDF matches and mark individual entries to send to CMOP.

If you mark the entry to transmit to CMOP, it will replace your Dispense Unit

with the VA Dispense Unit. In addition, you may overwrite the local drug name

with the VA Print Name and the entry will remain uneditable.

Do you wish to loop through the whole file?

(If you answer "NO", you will loop through ONLY the ones previously marked as

"Do not transmit to CMOP").

Enter Yes or No: **N** O

I have to build a table before you can begin "looping" so let me put you on

"hold" for a moment.

...............................................................

VA Print Name: GUAIFENESIN 100MG/5ML SYRUP         VA Dispense Unit: ML

Local Drug Generic Name: GUAIFENESIN 100MG/5ML LIQUID

VA Drug Class: RE302

ORDER UNIT: 120ML

DISPENSE UNITS/ORDER UNITS: 120

DISPENSE UNIT: MG/ML

PRICE PER DISPENSE UNIT: 0.01

** This entry has been previously marked NOT to transmit to CMOP **

Do you wish to mark this drug to transmit to CMOP?

Enter Yes or No: **Y** ES

Your old Dispense Unit  MG/ML  does not match the new one  ML.

You may wish to edit the Price Per Order Unit and/or the Dispense

Units Per Order Unit.

PRICE PER ORDER UNIT: 0.01// **&lt;RET&gt;**

DISPENSE UNITS PER ORDER: 120// **&lt;RET&gt;**

Do you wish to overwrite your local name?

Enter Yes or No: **Y** ES

VA Print Name: GUAIFENESIN 100MG/5ML SYRUP

Local Drug Name                            CMOP?    VA D.U.        O.W.?

------------------------------------------------------------------------------

1. GUAIFENESIN 100MG/5ML SYRUP                YES      ML             YES

Price Per Order Unit = 0.01

Dispense Units Per Order Unit = 120

If you answer "Yes" you will go to the next VA Print Name. If you answer "No"

you will go back through this particular VA Print Name group.

Are you sure everything is correct?

Enter Yes or No: **Y** ES

You've completed marking everything that is possible.

#### CMOP Mark/Unmark (Single drug)

<!-- image -->

**PSNMGR**

With this option the user can mark or unmark a single drug for transmission to the CMOP.

+	If a drug marked for CMOP in the DRUG file (#50) needs to be edited, the entry must be unmarked for CMOP using the *CMOP Mark/Unmark (Single drug)* option. Once editing is completed, the drug must be re-marked for CMOP using the *CMOP Mark/Unmark (Single drug)* option.

*****IMPORTANT*****

When using the option *CMOP Mark/Unmark (Single drug)* to mark a drug for CMOP the user **must** update the cost information in the DRUG file (#50) to ensure the cost data for the refill will be correct.

**Example 1:  Marking a CMOP Drug (Single drug)**

Select CMOP Site Manager Menu Option: **CMOP D** rug/Item Management

Select CMOP Drug/Item Management Option: **CMOP M** ARK/Unmark (Single drug)

This option allows you to choose entries from your drug file and helps you

review your NDF matches and mark individual entries to send to CMOP.

If you mark the entry to transmit to CMOP, it will replace your Dispense Unit

with the VA Dispense Unit. In addition, you may overwrite the local drug name

with the VA Print Name and the entry will remain uneditable.

Select DRUG GENERIC NAME: **GUAIFENESIN 100MG/5ML LIQUID** RE302

Local Drug Generic Name: GUAIFENESIN 100MG/5ML LIQUID

ORDER UNIT: 120ML

DISPENSE UNITS/ORDER UNITS: 120

DISPENSE UNIT: EA

PRICE PER DISPENSE UNIT: 0.01

VA Print Name: GUAIFENESIN 100MG/5ML SYRUP       VA Dispense Unit: ML

VA Drug Class: CN103

Do you wish to mark this drug to transmit to CMOP?

Enter Yes or No: **Y** ES

QUANTITY DISPENSE MESSAGE: **ENTER IN MULTIPLES OF 120.**

Your old Dispense Unit  EA  does not match the new one  ML.

You may wish to edit the Price Per Order Unit and/or The Dispense

Units Per Order Unit.

PRICE PER ORDER UNIT: 3.70// **1.20**

DISPENSE UNITS PER ORDER UNIT: 1// **120**

Do you wish to overwrite your local name?

Enter Yes or No: **Y** ES

Select DRUG GENERIC NAME: **&lt;RET&gt;**

**Example 2:  Unmarking a CMOP Drug (Single drug)**

Select CMOP Site Manager Menu Option: **CMOP D** rug/Item Management

Select CMOP Drug/Item Management Option: **CMOP M** ark/Unmark (Single drug)

This option allows you to choose entries from your drug file and helps you

review your NDF matches and mark individual entries to send to CMOP.

If you mark the entry to transmit to CMOP, it will replace your Dispense Unit

with the VA Dispense Unit. In addition, you may overwrite the local drug name

with the VA Print Name and the entry will remain uneditable.

Select DRUG GENERIC NAME: **GUAIFENESIN 100MG/5ML SYRUP** RE302

Local Drug Generic Name: GUAIFENESIN 100MG/5ML SYRUP

ORDER UNIT: 120ML

DISPENSE UNITS/ORDER UNITS: 120

DISPENSE UNIT: ML

PRICE PER DISPENSE UNIT: 0.01

VA Print Name: GUAIFENESIN 100MG/5ML SYRUP            VA Dispense Unit: ML

VA Drug Class: CN103

Do you wish to UNmark this drug to transmit to CMOP?

Enter Yes or No: **Y** ES

Select DRUG GENERIC NAME: **&lt;RET&gt;**

#### CMOP Data from Your Local Drug File

This option is used to print a report of data in your local DRUG file (#50) marked to transmit to the CMOP. This report must be sent to a printer.

**Example: CMOP Data from Your Local Drug File**

Select CMOP System Management Menu Option: **CMOP D** rug/Item Management

Select CMOP Drug/Item Management Option: **CMOP D** ata from Your Local Drug File

This option will produce a report to help you review your NDF matches.

The report will group drugs together that are matched to the same VA Print

Name along with the VA Dispense Unit. These will be used for CMOP purposes.

You may queue the report to print, if you wish.

DEVICE: [Select print device.] [This report must be sent to a printer.]

report follows

LOCAL DRUGS MATCHED TO THE SAME VA PRINT NAME

Date printed: FEB 15,1997

Page: 1

VA PRINT NAME                                          VA DISPENSE UNIT

Local GENERIC NAME                                    Local DISPENSE UNIT

------------------------------------------------------------------------------

ACETAMINOPHEN 650MG RTL SUPP                           EA

ACETAMINOPHEN 650MG RTL SUPP                          EA

ACETAZOLAMIDE 125MG TAB                                TAB

ACETAZOLAMIDE 125MG TAB                               TAB

ACETAZOLAMIDE 250MG TAB                                TAB

ACETAZOLAMIDE 250MG TAB                               TAB

ACETAZOLAMIDE 500MG SA CAP                             CAP

ACETAZOLAMIDE 500MG SA CAP                            CAP

ACETIC ACID 0.25% IRRG SOLN                            ML

ACETIC ACID 0.25% IRRG SOLN                           ML

ACETIC ACID 2% OTIC SOLN                               ML

ACETIC ACID 2% OTIC SOLN                              ML

ACETIC ACID 2/ALUM ACET 10.79% OTIC SOLN               ML

ACETIC ACID 2/ALUM ACET 10.79% OTIC SOLN              ML

*[This report has been abbreviated to save space.]*

#### Drug Enter/Edit

<!-- image -->

**PSXCMOPMGR**

With this option the user can add new drugs to the file, edit existing drugs, and inactivate drugs.

***CMOP Functionality for Drug Enter/Edit***

When an entry in DRUG file (#50) has been marked for CMOP, the GENERIC NAME, and DISPENSE UNIT fields **cannot** be edited. If editing of these fields is necessary, the entry must be unmarked for CMOP using the *CMOP Mark/Unmark (Single drug)* option. Once editing is completed, the drug must be re-marked for CMOP using the *CMOP Mark/Unmark (Single drug)* option.

**Example: Drug Enter/Edit**

Select CMOP System Management Menu Option: **CMOP D** rug/Item Management

Select CMOP Drug/Item Management Option: **DRUG E** nter/Edit

Select DRUG GENERIC NAME: **AMOXA**

1   AMOXAPIN 100 MG TAB

2   AMOXAPINE 100MG TAB             CN601     N/F

3   AMOXAPINE 150MG TAB                  N/F     12-10-84

CHOOSE 1-3: 2

DO YOU WANT TO MARK THIS DRUG AS AN Outpatient Pharmacy ITEM? YES// **N** (NO)

GENERIC NAME: AMOXAPINE 100MG TAB// **AMOXAPIN 100MG**

CMOP drug names may not be edited.??

Answer must be 1-40 characters in length

GENERIC NAME: AMOXAPINE 100MG TAB// **&lt;RET&gt;**

MESSAGE: **&lt;RET&gt;**

QUANTITY DISPENSE MESSAGE: 5ml 10 ml only // **?**

Answer must be 1-68 characters in length.  Do not enter special characters

such as quotes, semicolons, colons.

QUANTITY DISPENSE MESSAGE: 5ml 10 ml only // **&lt;RET&gt;** [Do not enter special characters, e.g., semi-colon (;), caret (^), grave (`), forward slash (/), or colon (:).]

VA CLASSIFICATION: CN601// **&lt;RET&gt;**

DEA, SPECIAL HDLG: 6// **&lt;RET&gt;**

MAXIMUM DOSE PER DAY: **&lt;RET&gt;**

STANDARD SIG: **&lt;RET&gt;**

FSN: **&lt;RET&gt;**

NDC: 0005-5391-23// **&lt;RET&gt;**

WARNING LABEL: **&lt;RET&gt;**

Select SYNONYM: ASENDIN 100MG TAB// **&lt;RET&gt;**

SYNONYM: ASENDIN 100MG TAB// **&lt;RET&gt;**

INTENDED USE: **&lt;RET&gt;**

NDC CODE: **&lt;RET&gt;**

Select SYNONYM: **&lt;RET&gt;**

REORDER LEVEL: **&lt;RET&gt;**

ORDER UNIT: BT// **&lt;RET&gt;**

PRICE PER ORDER UNIT: 27.23// **&lt;RET&gt;**

NORMAL AMOUNT TO ORDER: **&lt;RET&gt;**

DISPENSE UNIT: TAB// **CAP**

Dispense unit of CMOP drug cannot be edited!??

Answer must be 1-10 characters in length.

DISPENSE UNIT: TAB// **&lt;RET&gt;**

DISPENSE UNITS PER ORDER UNIT: 100// **&lt;RET&gt;**

PRICE PER DISPENSE UNIT is 0.272

SOURCE OF SUPPLY: **&lt;RET&gt;**

NON-FORMULARY: N/F// **&lt;RET&gt;**

INACTIVE DATE: **&lt;RET&gt;**

CURRENT INVENTORY: 89970// **&lt;RET&gt;**

Select DRUG GENERIC NAME: **&lt;RET&gt;**

#### Drugs not Flagged for CMOP Transmission

This report lists items in the local DRUG file (#50) which are available at the CMOP, but have not been marked for transmission.

**Example: Drugs not Flagged for CMOP Transmission**

Select CMOP System Management Menu Option: **CMOP D** rug/Item Management

Select CMOP Drug/Item Management Option: **DRUGS NOT** Flagged for CMOP Transmission

This report will print all drugs marked for Outpatient use which are non-

controlled substances and are not marked to transmit to CMOP.

This report requires 132 columns.

You may queue the report to print, if you wish.

DEVICE: [Select print device.] [This report must be sent to a printer.]

report follows

OUTPATIENT DRUGS NOT MARKED TO SEND TO CMOP

Date printed: FEB 15,1997

Page: 1

LOCAL DRUG NAME                         STATUS        VA PRINT NAME

---------------------------------------------------------------------------------------------

ALDOCLOR-150 TAB                        NOT MARKED    CHLOROTHIAZIDE 150/METHYLDOPA 250MG TAB

ALDOCLOR-250 TAB                        NOT MARKED    CHLOROTHIAZIDE 250/METHYLDOPA 250MG TAB

ANAMINE SYRUP                           NOT MARKED    CTM 2/PSEUDOEPHEDRINE 30MG/5ML LIQUID

ANTHRA-DERM OINT 0.25% 1.5OZ            NOT MARKED    ANTHRALIN 0.25% OINT

ANTHRALIN 1.0% CR 50GM                  NOT MARKED    ANTHRALIN 1% CREAM

APRESAZIDE 100/50 CAP                   NOT MARKED    HYDRALAZINE 100/HCTZ 50MG CAP

APRESAZIDE 50/50 CAP                    NOT MARKED    HYDRALAZINE 50/HCTZ 50MG CAP

APRESOLINE-ESIDRIX TAB                  NOT MARKED    HYDRALAZINE 25/HCTZ 15MG TAB

ARISTO-PAK 4MG TAB                      DO NOT SEND   TRIAMCINOLONE 4MG TAB

ARISTOCORT A 0.1% OINT 60GM             NOT MARKED    TRIAMCINOLONE ACETONIDE 0.1% OINT

*[This report has been abbreviated to save space.]*

### Facility Cost Management

This menu contains options that enable the user to manage the cost compilation and print the cost reports for the Consolidated Mail Outpatient Pharmacy system.

*Date Range Compile/Recompile Cost Data*

*Drug Cost by Drug Report*

*Drug Cost by Drug Report for One Month*

*Drug Cost by Facility Report*

*High Cost Rx Report*

*Initialize the Nightly Compile Job*

*One Day Compile/Recompile Cost Data*

*Purge Cost Data*

*Update Rx COST in Master Database*

#### Date Range Compile/Recompile Cost Data

<!-- image -->

**PSXCOST**

This option compiles or recompiles cost data for a date range specified by the user. Before the data for the specified date range is compiled, the data for the date range is deleted from the CMOP COST STATS file (#552.5).

If a background job is queued to run or is running that compiles or purges cost data for the same date range you have selected or for dates that overlap your date range, you **cannot** queue your compile/recompile job. (See Example 2.)

The average number of prescriptions filled in a day is 10,000 per site. To recompile an average month takes several hours.

+	The cost data for the specified date range is compiled using the data in the CMOP MASTER DATBASE file (#552.4) not by totaling the daily entries in the CMOP COST STATS file (#552.5).

**Example 1:  Date Range Compile/Recompile Cost Data**

Select CMOP System Management Menu Option: **F** acility Cost Management

Select Facility Cost Management Option: **DA** te Range Compile/Recompile Cost Data

Beginning date: **T-180** (SEP 01, 1996)

Ending date: **T-1** (FEB 27, 1997)

Are you sure? N// **Y** YES

Monthly data compilation queued from Sep 01, 1996 to Nov 1996.

Requested Start Time: NOW// **&lt;RET&gt;** (FEB 28, 1997@12:21:41)

Task Queued!

Daily data compilation queued from Dec 01, 1996 to Feb 27, 1997.

Requested Start Time: NOW// **&lt;RET&gt;** (FEB 28, 1997@12:21:46)

Task Queued!

Select Facility Cost Management Option: **&lt;RET&gt;**

**Example 2:  Date Range Compile/Recompile Cost Data**

Select CMOP System Management Menu Option: **F** acility Cost Management

Select Facility Cost Management Option: **DA** te Range Compile/Recompile Cost Data

Beginning date: **T-30** (JAN 29, 1997)

Ending date: **T** (FEB 28, 1997)

Are you sure? N// **Y** ES

Your task cannot be queued. The following active task(s) is for the same

date range you have selected or for dates that overlap your date range.

Status   Activity  Data Date Range   Task#  Task Started

------------------------------------------------------------------------------

Running   Compile 12/01/96-02/27/97 69870  02/28/97@1221

Queued by: CMOPPHARMACIST30,THREE

Queued    Compile 02/28/97-02/28/97 69828  02/28/97@0100

Queued by: CMOPPHARMACIST2,THREE

Queued    Compile 02/28/97-02/28/97 69827  02/28/97@0100

Queued by: CMOPPHARMACIST27,THREE

Beginning date: **&lt;RET&gt;**

Select Facility Cost Management Option: **&lt;RET&gt;**

#### Drug Cost by Drug Report

This option prints a report of drug cost by drug. The report lists the drug name, number of original fills, number of refills, total fills, total cost, average cost per dispense unit, and average cost per fill. The report can be printed for a specific facility or all facilities, and a specific division or all divisions. If the facility has more than one division and all divisions are selected, a summary sheet prints. The summary report contains a total for each division and a grand total for the facility.

**Example: Drug Cost by Drug Report**

Select CMOP System Management Menu Option: **F** acility Cost Management

Select Facility Cost Management Option: **DR**

1    Drug Cost by Drug Report

2    Drug Cost by Drug Report for One Month

3    Drug Cost by Facility Report

CHOOSE 1-3: **1** Drug Cost by Drug Report

Do you want to look at data concerning a specific drug? Y// **N** O

Beginning Date: **T-60** (DEC 25, 1996)

Ending Date: **T** (FEB 23, 1997)

Print data for a specific facility? Y// **N** O

DEVICE: [Select print device.] [This report must be sent to a 132-column printer.]

PRINTED: FEB 23,1997@11:23:59                                                          PAGE 1

DRUG COST BY DRUG FOR BIRMINGHAM, AL.

DEC 25,1996 TO FEB 23,1997

DIVISION: BIRMINGHAM

ORIGN                    TOTAL             TOTAL    AVG COST   AVG COST per

DRUG                               FILLS       REFILLS      FILLS              COST    per FILL   DISPENSE UNIT

===============================================================================================================

ACETAMINOPHEN 325MG TAB                4             4          8              1.94        0.24        0.003

ACETAMINOPHEN 500MG CAP                1             2          3              0.00        0.00        0.000

ACETAZOLAMIDE 500MG SA CAP             1             0          1              5.73        5.73        0.229

ACETIC ACID 0.25% IRRG SOLN            2             0          2            284.35      142.18        2.585

ACYCLOVIR 200MG CAP                    1             0          1             47.80       47.80        0.478

ALBUTEROL 90MCG 200D ORAL INHL         0             2          2            429.25      214.63        4.250

ALBUTEROL SULFATE 2MG TAB              0             1          1              0.08        0.08        0.090

ALBUTEROL SULFATE 4MG TAB              0             1          1              5.16        5.16        0.172

ALLOPURINOL 100MG TAB                  1             2          3              3.84        1.28        0.024

ALUMINUM CL HEXAHYDRATE 20% TOP SOLN   1             0          1            636.25      636.25        5.090

AMANTADINE HCL 100MG CAP               1             3          4             91.16       22.79        0.214

AMIKACIN SULFATE 250MG/ML INJ          2             1          3           5190.00     1730.00       17.300

AMILORIDE HCL 5/HCTZ 50MG TAB          2             0          2             32.70       16.35        0.218

*[Portions of this report have been abbreviated to save space.]*

PRINTED: FEB 23,1997@11:23:59                                                                       PAGE 2

DRUG COST BY DRUG FOR BIRMINGHAM, AL.

DEC 25,1996 TO FEB 23,1997

DIVISION: BIRMINGHAM

ORIGN                    TOTAL             TOTAL    AVG COST   AVG COST per

DRUG                               FILLS       REFILLS      FILLS              COST    per FILL   DISPENSE UNIT

===============================================================================================================

METHOCARBAMOL 500MG TAB                0             1          1              2.88        2.88        0.024

NADOLOL 40MG TAB                       0             1          1             30.50       30.50        0.305

NAPROXEN 375MG TAB                     2             0          2             53.12       26.56        0.332

NIACIN 500MG TAB                       1             0          1             23.85       23.85        0.265

RANITIDINE HCL 150MG TAB               0             1          1             35.52       35.52        0.592

UNKNOWN                                3             1          4              0.00        0.00        0.000

VERAPAMIL HCL 120MG TAB                7             2          9             85.70        9.52        0.095

---------------------------------------------------------------------------------------------------------------

DIVISION TOTAL                        99            96        195          15643.26       80.22        0.877

PRINTED: FEB 23,1997@11:23:59                                                                       PAGE 3

DRUG COST BY DRUG FOR BIRMINGHAM, AL.

DEC 25,1996 TO FEB 23,1997

DIVISION: BIRMINGHAM (C)

ORIGN                    TOTAL             TOTAL    AVG COST   AVG COST per

DRUG                               FILLS       REFILLS      FILLS              COST    per FILL   DISPENSE UNIT

===============================================================================================================

AMINOPHYLLINE 100MG TAB                0             1          1              0.50        0.50        0.005

AMOXAPINE 25MG TAB                     0             1          1             15.70       15.70        0.157

---------------------------------------------------------------------------------------------------------------

DIVISION TOTAL                         0             2          2             16.20        8.10        0.081

PRINTED: FEB 23,1997@11:23:59                                                                       PAGE 4

DRUG COST BY DRUG FOR BIRMINGHAM, AL.

DEC 25,1996 TO FEB 23,1997

DIVISION: PHARMACY

ORIGN                    TOTAL             TOTAL    AVG COST   AVG COST per

DRUG                               FILLS       REFILLS      FILLS              COST    per FILL   DISPENSE UNIT

===============================================================================================================

AMIKACIN SULFATE 250MG/ML INJ          1             0          1           1730.00     1730.00       17.300

AMIODARONE HCL 200MG TAB               1             0          1             37.38       37.38        1.246

AMITRIPTYLINE 50/PERPHENAZINE 4MG TAB  1             0          1             35.30       35.30        0.353

CIMETIDINE 200MG TAB                   1             0          1             12.65       12.65        0.253

VERAPAMIL HCL 120MG TAB                1             0          1              6.70        6.70        0.067

---------------------------------------------------------------------------------------------------------------

DIVISION TOTAL                         5             0          5           1822.03      364.41        4.795

PRINTED: FEB 23,1997@11:23:59                                                   PAGE 5

DRUG COST BY DRUG FOR BIRMINGHAM, AL.

DEC 25,1996 TO FEB 23,1997

DIVISION: ALL DIVISIONS

ORIGN                    TOTAL             TOTAL    AVG COST   AVG COST per

DIVISION                           FILLS       REFILLS      FILLS              COST    per FILL   DISPENSE UNIT

===============================================================================================================

BIRMINGHAM                            99            96        195          15643.26       80.22        0.877

BIRMINGHAM (C)                         0             2          2             16.20        8.10        0.081

PHARMACY                               5             0          5           1822.03      364.41        4.795

---------------------------------------------------------------------------------------------------------------

FACILITY TOTAL                       104            98        202          17481.49       86.54        0.949

#### Drug Cost by Drug Report for One Month

This option prints a monthly drug cost report for a month specified by the user. The report lists the total fills, total quantity, total cost, average cost per dispense unit, and formulary/non-formulary. It can be printed for a specified drug or all drugs, a specified facility or all facilities, and a specific division or all divisions. A total for all divisions is included at the end of the report. The minimum total number of refills and minimum total cost are assigned by the user to further refine this report.

**Example: Drug Cost by Drug Report for One Month**

Select CMOP System Management Menu Option: **F** acility Cost Management

Select Facility Cost Management Option: **DR**

1    Drug Cost by Drug Report

2    Drug Cost by Drug Report for One Month

3    Drug Cost by Facility Report

CHOOSE 1-3: **2** Drug Cost by Drug Report for One Month

Enter Month/Year: **11/97** (NOV 1996)

Do you want to look at data concerning a specific drug? Y// **N** O

Print data for a specific facility? Y// **&lt;RET&gt;** ES

Select FACILITY: **BIRM** INGHAM, AL.                                   521

Print data for a specific division? Y// **&lt;RET&gt;** ES

Select DIVISION: **BIRM** INGHAM (C)

Select Minimum Total number of Refills: :  (0-50): 0// **&lt;RET&gt;**

Select Minimum Total Cost: :  (0-9999): 0// **&lt;RET&gt;**

DEVICE: [Select print device.] [This report must be sent to a 132-column printer.]

PRINTED: DEC 23,1996@12:17:57                                                     PAGE: 1

MONTHLY DRUG COST REPORT FOR BIRMINGHAM, AL.

NOV 1996

MINIMUM REFILLS OF 0 AT A MINIMUM COST OF $0

DIVISION: BIRMINGHAM (C)

TOTAL         TOTAL          TOTAL      AVG COST per

DRUG                                              FILLED        QUANTITY         COST      DISPENSE UNIT                     N/F

==================================================================================================================================

ACETAMINOPHEN 325MG TAB                                2            400          1.20             0.003

ACETAMINOPHEN 500MG CAP                                2            120          1.08             0.009                *** N/F ***

ACETAZOLAMIDE 500MG SA CAP                             2            200         45.80             0.229                *** N/F ***

ACETIC ACID 0.25% IRRG SOLN                            1             30         77.55             2.585

ACETOHEXAMIDE 500MG TAB                                3            145         22.77             0.157                *** N/F ***

ACETOPHENAZINE MALEATE 20MG TAB                        1            100         21.20             0.212                *** N/F ***

ACETYLCYSTEINE 10% INH SOLN 30ML                       1              3        103.05            34.350                *** N/F ***

ACYCLOVIR 200MG CAP                                    1             50         23.90             0.478

ACYCLOVIR NA 500MG/VI INJ                              2            100       1546.50            15.465

ALBUTEROL 90MCG 200D ORAL INHL                         6             15         34.85             2.293

ALBUTEROL SULFATE 4MG TAB                              5            110         13.76             0.125

ALLOPURINOL 100MG TAB                                  2            130          2.40             0.018

ALUMINUM CL HEXAHYDRATE 20% TOP SOLN                   3            135        661.70             4.901                *** N/F ***

AMANTADINE HCL 100MG CAP                               4            275         10.70             0.039

AMCINONIDE 0.1% OINT                                   1              3         14.85             4.950                *** N/F ***

AMIKACIN SULFATE 250MG/ML INJ                          2              7        121.10            17.300

AMILORIDE HCL 5MG TAB                                  3            300         33.00             0.110

AMINOPHYLLINE 100MG TAB                                2            200          0.50             0.003                *** N/F ***

AMINOPHYLLINE 500MG RTL SUPP                           1            100        312.00             3.120                *** N/F ***

AMITRIPTYLINE 10/PERPHENAZINE 2MG TAB                  3            300         43.50             0.145                *** N/F ***

AMITRIPTYLINE HCL 10MG TAB                             2            200          1.10             0.006

AMOXAPINE 100MG TAB                                    1             60         16.32             0.272                *** N/F ***

AMOXAPINE 25MG TAB                                     1             10          0.00             0.000                *** N/F ***

AMOXAPINE 50MG TAB                                     1            100          0.00             0.000

AMPICILLIN 250MG/5ML SUSP                              2              0          0.03             1.545                *** N/F ***

ASCORBIC ACID 250MG TAB                                2            200          0.50             0.003                *** N/F ***

ASPIRIN 325MG TAB                                      2            200          0.50             0.003

BETAXOLOL 0.5% OPHT SOLN 5ML                           2              6         46.50             7.750

CAPTOPRIL 100MG TAB                                    1             75         60.38             0.805                *** N/F ***

CIMETIDINE 200MG TAB                                   2            200         25.30             0.127

DIAZOXIDE 50MG CAP                                     2             62         23.99             0.390                *** N/F ***

FOLIC ACID 1MG TAB                                    13            680          2.94             0.004

FUROSEMIDE 40MG TAB                                    2            100          0.60             0.006

HALOPERIDOL 20MG TAB                                  22           4420       6235.28             1.411                *** N/F ***

IBUPROFEN 600MG TAB                                   22           2360         61.71             0.026

ISOCARBOXAZID 10MG TAB                                 2             60          0.00             0.000                *** N/F ***

ISONIAZID 100MG TAB                                   13           1390         54.60             0.039

LEVODOPA 250MG TAB                                     2            100          8.40             0.084                *** N/F ***

NADOLOL 40MG TAB                                       3            120         36.60             0.305                *** N/F ***

NAPROXEN 375MG TAB                                     2            200         33.20             0.166                *** N/F ***

NEOMYCIN SULFATE 500MG TAB                             2            130         12.61             0.097

NIACIN 500MG TAB                                       4            370         98.05             0.265                *** N/F ***

QUINIDINE SULFATE 200MG TAB                            1            120          3.72             0.031

PRINTED: DEC 23,1996@12:17:57                                                                                            PAGE: 2

MONTHLY DRUG COST REPORT FOR BIRMINGHAM, AL.

NOV 1996

MINIMUM REFILLS OF 0 AT A MINIMUM COST OF $0

DIVISION: BIRMINGHAM (C)

TOTAL         TOTAL          TOTAL      AVG COST per

DRUG                                              FILLED        QUANTITY         COST      DISPENSE UNIT                     N/F

==================================================================================================================================

RANITIDINE HCL 150MG TAB                               4            400        236.82             0.592

UNKNOWN                                                2              3         57.94            19.313

VERAPAMIL HCL 120MG TAB                                4            190         12.73             0.067

ZINC SULFATE 220MG CAP                                 3            180          2.16             0.012

----------     ----------    ----------

DIVISION TOTAL                                       166          14658      10123.38

PRINTED: DEC 23,1996@12:17:57                                                                                            PAGE: 3

MONTHLY DRUG COST REPORT FOR BIRMINGHAM, AL.

NOV 1996

MINIMUM REFILLS OF 0 AT A MINIMUM COST OF $0

DIVISION: ALL

TOTAL         TOTAL          TOTAL

DIVISION                                          FILLED        QUANTITY         COST                                        N/F

==================================================================================================================================

BIRMINGHAM (C)                                       166         14658       10123.38

----------    ----------    ----------

FACILITY TOTAL                                       166         14658       10123.38

#### Drug Cost by Facility Report

This option prints a summary report of drug cost by facility and division. The report lists the division, total original fills, total refills, total fills, total cost, and average cost per fill. It prints all drug for all facilities or a specific facility, all divisions, or a specific division.

**Example: Drug Cost by Facility Report**

Select CMOP System Management Menu Option: **F** acility Cost Management

Select Facility Cost Management Option: **DR**

1    Drug Cost by Drug Report

2    Drug Cost by Drug Report for One Month

3    Drug Cost by Facility Report

CHOOSE 1-3: **3** Drug Cost by Facility Report

Beginning Date: **T-60** (JAN 07, 1997)

Ending Date: **T** (MAR 06, 1997)

Print data for a specific facility? Y// **N** O

DEVICE: [Select print device.] [This report must be sent to a 132-column printer.]

report follows

PRINTED: MAR 6,1997@15:21:18                                                       PAGE 1

DRUG COSTS BY FACILITY FOR BIRMINGHAM, AL.

JAN 7,1997 TO MAR 6,1997

ORIGN                 TOTAL          TOTAL        AVG COST

DIVISION                      FILLS     REFILLS     FILLS           COST        per FILL

========================================================================================

BIRMINGHAM (C)                    1           1         2           9.36            4.68

PRINTED: MAR 6,1997@15:21:18                                                       PAGE 2

DRUG COSTS BY FACILITY FOR LOUISVILLE, KY.

JAN 7,1997 TO MAR 6,1997

ORIGN                 TOTAL          TOTAL        AVG COST

DIVISION                      FILLS     REFILLS     FILLS           COST        per FILL

========================================================================================

LOUISVILLE                        1           0         1          20.00           20.00

LOUISVILLE OUTPATIENT             0           1         1          15.00           15.00

----------------------------------------------------------------------------------------

TOTAL                             1           1         2          35.00           17.50

#### High Cost Rx Report

This option prints the High Cost Rx report for a specific facility or all facilities. The report contains the prescription number, drug name, quantity dispensed, drug cost, and total drug cost for each prescription. The CMOP MASTER DATABASE file (#552.4) is searched for prescriptions with the total cost greater than or equal to an amount specified by the user.

**Example: High Cost Rx Report**

Select CMOP System Management Menu Option: **F** acility Cost Management

Select Facility Cost Management Option: **H** igh Cost Rx Report

Beginning Date: **T-1** (MAR 12, 1997)

Ending Date: **T** (MAR 13, 1997)

Print data for a specific facility? Y// **&lt;RET&gt;** ES

Select FACILITY: **BIRM** INGHAM, AL.                                   521

Dollar Limit (Minimum Total Cost):  (0-9999): 30// **&lt;RET&gt;**

DEVICE: [Select print device.]

report follows

PRINTED: MAR 13, 1997@07:38:08                                         PAGE 1

HIGH COST REPORT FOR BIRMINGHAM, AL.

FILLS THAT COST AT LEAST $30 -- FROM MAR 12,1997 TO MAR 13,1997

RX #         DRUG                                QTY     COST    TOTAL COST

------------------------------------------------------------------------------

200012       FOLIC ACID 1MG TAB                   30 x  4.250  = 127.50

11601B       RANITIDINE HCL 150MG TAB           100.01x 0.592  =  59.21

10981B       NITROGLYCERIN 0.15MG SL TAB         100 x  1.820  = 182.00

11760        ACETIC ACID 0.25% IRRG SOLN          30 x  2.585  =  77.55

* 11728        AMCINONIDE 0.1% CREAM               100 x  4.950  = 495.00

11554A       AMIKACIN SULFATE 250MG/ML INJ         5 x 17.300  =  86.50

11553A       HALOPERIDOL 20MG TAB                100 x  1.901  = 190.10

11427B       ACETYLCYSTEINE 10% INH SOLN 30ML      3 x 34.350  = 103.05

* 11193C       ZIDOVUDINE 100MG CAP                 40 x  1.970  =  78.80

* 11561B       CAPTOPRIL 100MG TAB                  75 x  0.805  =  60.38

10581D       XEROFORM PETROLATUM DRESSING 5X9IN    5 x  6.100  =  30.50

* 11355A       RANITIDINE HCL 150MG TAB            100 x  0.592  =  59.20

* 11595A       ZIDOVUDINE 100MG CAP                100 x  1.970  = 197.00

11513D       HALOPERIDOL 20MG TAB                300 x  1.901  = 570.30

11769        HALOPERIDOL 20MG TAB                 50 x  1.901  =  95.05

No. of Fills=15      '*' indicates a refill

#### Initialize the Nightly Compile Job

<!-- image -->

**PSXCOST**

This option queues a nightly job that compiles yesterday’s cost data and adds the data to the CMOP COST STATS file (#552.5). The user can specify the time the job is tasked to run or accept the default of one o’clock in the morning. The nightly job also queues the next nightly job. It is recommended this job be tasked to run at night at a time convenient to the site.

Two months of daily data are retained in the CMOP COST STATS file (#552.5). On the first of each month, the daily cost data is purged for the third month back and replaced with one entry for the month.

**Example:** Today is 12/1/96. Daily cost data entries for 10/96 through 11/96 are retained in the CMOP COST STATS file (#552.5). The daily entries for 9/96 are replaced with a monthly entry.

+	The entry for the month is compiled using the data in the CMOP MASTER DATABASE file (#552.4), not by totaling the daily entries in the CMOP COST STATS file (#552.5).

If the entries are not the 30 most recent entries, the nightly compile job will delete cost job tasking entries in the CMOP OPERATIONS file (#554).

**Example: Initialize the Nightly Compile Job**

Select CMOP System Management Menu Option: **F** acility Cost Management

Select Facility Cost Management Option: **I** nitialize the Nightly Compile Job

A job will be tasked every night which compiles yesterday’s cost

statistics. This job should be run during off hours. The suggested

time is 1 o'clock in the morning.

** CAUTION: Check with IRM to make sure the

job has not already been queued.

Continue? N// **Y** ES

Enter date/time: MAR 7,1997@01:00// **&lt;RET&gt;** (MAR 07, 1997@01:00)

Task Queued !

Select Facility Cost Management Option: **&lt;RET&gt;**

#### One Day Compile/Recompile Cost Data

<!-- image -->

**PSXCOST**

This option compiles or recompiles cost data for a day specified by the user.

If a background job is queued to run or is running that compiles or purges cost data for the same date range you have selected or for dates that overlap your date range, you **cannot** queue your compile/recompile job.

**Example: One Day Compile/Recompile Cost Data**

Select CMOP System Management Menu Option: **F** acility Cost Management

Select Facility Cost Management Option: **O** ne Day Compile/Recompile Cost Data

Date: **T-1** (FEB 15, 1997)

Are you sure? N// **Y** ES

One Day data compilation queued from Feb 15,1997 to Feb 15, 1997.

Requested Start Time: NOW// **&lt;RET&gt;** (FEB 15, 1997@08:20:39)

Task Queued !

Select Facility Cost Management Option: **&lt;RET&gt;**

#### Purge Cost Data

<!-- image -->

**PSXCOST**

This option deletes data from the CMOP COST STATS file (#552.5). The data for the oldest date is deleted through a date specified by the user.

If a background job is queued to run or is running that compiles or purges cost data for the same date range you have selected or for dates that overlap your date range, you **cannot** queue your purge job until the background job has completed.

+	Data for three **complete** months will remain in the file.

**Example 1:  Purge Cost Data**

Select CMOP System Management Menu Option: **F** acility Cost Management

Select Facility Cost Management Option: **P** urge Cost Data

Data for three complete months must remain in the cost file.

JAN 1996 through JUN 1996 can be purged.

Purge data from JAN 1996 through: **6 96** (JUN 1996)

Purge from JAN 1996 to JUN 1996

Are you sure? N// **Y** ES

Requested Start Time: NOW// **&lt;RET&gt;** (OCT 12, 1996@14:26:53)

Task Queued !

Select Facility Cost Management Option: **&lt;RET&gt;**

**Example 2:  Purge Cost Data**

Select CMOP System Management Menu Option: **F** acility Cost Management

Select Facility Cost Management Option: **P** urge Cost Data

The cost file contains data beginning with JUL 1996.

Data for three complete months must remain

in the cost file. No data can be purged.

Select Facility Cost Management Option: **&lt;RET&gt;**

#### Update Rx COST in Master Database

<!-- image -->

**PSXCOST**

This option is a background job and is used to update the drug costs in the CMOP MASTER DATABASE file (#552.4).

**Example: Update Rx COST in Master Database**

Select Facility Cost Management Option: **U** pdate Rx COST in Master Database

Enter Begin Date : **T-10** (FEB 27, 1997)

Enter End Date : **T** (MAR 08, 1996)

Requested Start Time: NOW// **&lt;RET&gt;** (MAR 08, 1997@10:33:30)

Job Queued

Select Facility Cost Management Option: **&lt;RET&gt;**

### Archive CMOP Data

This is the master archive menu for CMOP MASTER DATABASE file (#552.4) and CMOP REFERENCE file (#552.1).

*Archive Monthly CMOP Data*

*Purge Archived CMOP Data*

*Retrieve Archived CMOP Data*

#### Archive Monthly CMOP Data

1. Be sure to record the tape number on the tape label. The tape index number consists of two parts:

1)  29705 – The year/month being archived in FileMan format.

2)  1 – The sequence number of the tape being used. If more than one tape is required for a month then 297051 is incremented to 297052.

1. Start and end times are provided so that you can compute how much time it will take to complete subsequent archives.

1. When the data is archived, the original files are marked “uneditable”, so be sure you want to archive the data you have selected before you commit. You can archive the same data twice, though. In this instance the tape number will be the same except for the last digit which will be incremented by one.

**Example: Archive Monthly CMOP Data**

Select Archive CMOP Data Option: **A** rchive Monthly CMOP Data

ENTER MONTH/YEAR TO ARCHIVE :  02/97// **&lt;RET&gt;**

CMOP MASTER DATABASE ARCHIVE

Do you want to continue? :  (Y/N): NO// **Y** ES

Select Tape Drive: *[Select Tape Drive]*

//   REWIND? NO// **Y** (YES)

CMOP MASTER DATABASE ARCHIVE       MAR 20,1997@08:45:56

Recording data on tape # 297021. Write this number on the tape label!!

TRANSMISSION #      TOT ORDERS      TOT Rx's

521-1                        1             2

521-2                        7            15

521-3                        4             7

Total # of Transmissions Archived: 3

Total # of Rx's Archived         : 24

Total Bytes Archived             : 6054

Completed: MAR 20,1997@08:46   Closing Tape Device...

Select Archive CMOP Data Option: **&lt;RET&gt;**

#### Purge Archived CMOP Data

This option is used to purge data that has already been archived from the CMOP MASTER DATABASE file and the CMOP REFERENCE file.

**Example: Purge Archived CMOP Data**

Select Archive CMOP Data Option: **P** urge Archived CMOP Data

ENTER MONTH/YEAR TO PURGE :  11/97// **&lt;RET&gt;**

CMOP MASTER DATABASE PURGE

Total transmissions to be purged  : 2

Total orders to be purged         : 3

Total Rx's to be purged           : 6

Do you want to continue? :  (Y/N): NO// **Y** ES

Transmission# 521-306 has been purged.

Transmission# 521-307 has not been archived yet and may not be purged.

Select Archive CMOP Data Option: **&lt;RET&gt;**

#### Retrieve Archived CMOP Data

This option enables you to retrieve archived Rx’s from tape.

**Example: Retrieve Archived CMOP Data**

Select Archive CMOP Data Option: **R** etrieve Archived CMOP Data

Enter Archived CMOP Transmission Number: 521-662

Enter Rx # to report or return for all: ALL// **&lt;RET&gt;**

Select Printer:   [Select Print Device]

Please mount tape #: 296031

Press Return when ready... **&lt;RET&gt;**

Select Tape Drive: *[Select Tape Drive]* //   REWIND? NO// **Y** (YES)

CMOP MASTER DATABASE ARCHIVE       MAR 21,1997@09:38:02

ARCHIVE REPORT FOR TRANSMISSION # 521-662

by CMOPPHARMACIST30,THREE  on MAR 21,1997

Status: CLOSED                       Trans D/T: MAR 22, 1996@09:18:49

Received D/T: MAR 22, 1996@09:19:11       Closed D/T: MAR 25, 1996@12:28:41

Processed D/T: MAR 25, 1996@11:21:54      Start Seq #: 7

End Seq #: 9                         Total Orders: 3

Total Rx's: 12                        Purge Status: PURGE COMPLETE

Retrans:                           Orig Trans #:

Division: BIRMINGHAM                   Site Name: BIRMINGHAM, AL.

Sender: CMOPPHARMACIST30,THREE

LABEL LOG:

DATE PRINTED                  PRINTED BY

-------------------------------------------------

MAR 25,1996@11:21:54          CMOPPHARMACIST28,THREE

Rx #             : 15355E          Fill #       : 0         Qty: 77472219.54

Employee Name    : CMOPPHARMACIST28,THREE

Price/Disp Unit  : 0.003           Drug ID #    : A0022

Release Status   : COMPLETED       Release Type : MANUAL

Rx Status        : PROCESSED       NDC          :

Carrier          :                 Package ID # :

Date Shipped     :

Processed D/T    : MAR 25, 1996@12:28:25  Completed D/T: MAR 25, 1996@12:23:25

Remote Error Cond:

Cancel Reason    :

==========================================================================

Rx #             : 15356D          Fill #       : 0         Qty: 100

Employee Name    : CMOPPHARMACIST28,THREE

Price/Disp Unit  : 17.300          Drug ID #    : A0505

Release Status   : COMPLETED       Release Type : MANUAL

Rx Status        : PROCESSED       NDC          :

Carrier          :                 Package ID # :

Date Shipped     :

Processed D/T    : MAR 25, 1996@12:28:25  Completed D/T: MAR 25, 1996@12:23:48

Remote Error Cond:

Cancel Reason    :

==========================================================================

Rx #             : 15368C          Fill #       : 0         Qty: 100

Employee Name    : CMOPPHARMACIST28,THREE

Price/Disp Unit  :                 Drug ID #    : V0006

Release Status   : COMPLETED       Release Type : MANUAL

Rx Status        : PROCESSED       NDC          :

Carrier          :                 Package ID # :

Date Shipped     :

Processed D/T    : MAR 25, 1996@12:28:25  Completed D/T: MAR 25, 1996@12:24:03

Remote Error Cond:

Cancel Reason    :

==========================================================================

Rx #             : 15103G          Fill #       : 0         Qty: 120

Employee Name    : CMOPPHARMACIST28,THREE

Price/Disp Unit  : 0.033           Drug ID #    : I0005

Release Status   : COMPLETED       Release Type : MANUAL

Rx Status        : PROCESSED       NDC          :

Carrier          :                 Package ID # :

Date Shipped     :

Processed D/T    : MAR 25, 1996@12:28:25  Completed D/T: MAR 25, 1996@12:24:13

Remote Error Cond:

Cancel Reason    :

==========================================================================

Rx #             : 11597G          Fill #       : 0         Qty: 2

Employee Name    : CMOPPHARMACIST28,THREE

Price/Disp Unit  : 4.250           Drug ID #    : A0105

Release Status   : COMPLETED       Release Type : MANUAL

Rx Status        : PROCESSED       NDC          :

Carrier          :                 Package ID # :

Date Shipped     :

Processed D/T    : MAR 25, 1996@12:28:29  Completed D/T: MAR 25, 1996@12:24:27

Remote Error Cond:

Cancel Reason    :

==========================================================================

*[This example has been abbreviated to save space.]*

Select Archive CMOP Data Option: **&lt;RET&gt;**

## Glossary

**Action Profile** A list of all active and recently cancelled or expired prescriptions for a patient sorted by classification. This profile also includes a signature line for each prescription to allow the physician to cancel or renew it.

**Activity Log** A log, by date, of changes made to or actions taken on a prescription. An entry is made in this log each time the prescription is edited, cancelled, reinstated after being cancelled, or renewed. An entry will be made into this log when the Rx is suspended for CMOP and when the Rx is transmitted to CMOP.

**CMOP** Acronym for **C** onsolidated **M** ail **O** utpatient **P** harmacy.

**CMOP Event Statuses** A CMOP Rx can have the following statuses:

**Dispensed** The Rx was filled and mailed by the CMOP facility.

**Not Dispensed** The Rx was not filled by the CMOP facility.

**ReSubmitted** The Rx was resubmitted to the CMOP facility.

**ReTransmitted** The Rx was retransmitted to the CMOP facility because of a problem with the original transfer.

**Transmitted** The Rx has been sent to the CMOP facility for processing

**CMOP Indicator** The CMOP indicator is the status of the CMOP Rx in suspense.

**DEA** Acronym for **D** rug **E** nforcement **A** gency.

**DEA Special** The Drug Enforcement Agency  special handling code

**Handling** used for drugs to designate if they are over-the counter, narcotics, bulk compounds, supply items, etc.

**Drug/Drug** The pharmacological or clinical response to the

**Interaction** administration of a drug combination different from that anticipated from the known effects of the two agents when given alone.

**Expiration** The date on which a prescription is no longer active.

**Host** A host is a CMOP facility that receives prescription data and actually fills and mails the prescriptions to the veteran.

**Issue Date** The date on which the prescription was written. This date is usually, but not always, the same as the first fill date. This date cannot be later than the first fill date.

**Intranet** A company-wide computer network available via modem that connects users.

**Label/Profile** A file for each printer which records, in the order in

**Monitor** which they were printed, the last 1000 labels or profiles printed on that printer. This allows a rapid reprint of a series of labels or profiles which were damaged by a printer malfunction or other event.

**Medication Profile** A list of all active or recently cancelled or expired prescriptions for a patient sorted either by date, drug, or classification. Unlike the action profile, this profile is for information only and does not provide a signature line for a physician to indicate action to be taken on the prescription.

**Partial Prescription** A prescription which has been filled for a quantity smaller than requested. A possible reason for a partial fill is that a patient is to return to the clinic in ten days but the prescription calls for a thirty day supply. Partials do count as workload but do not count against the total number of refills for a prescription.

**PRESCRIPTION INDEX** The PRESCRIPTION INDEX field of the RX1

**field** segment is the unique key used to identify an individual prescription. It contains the Facility ID, Rx Number, and the Fill Number of a previously received prescription.

**Prescription Status** A prescription can have one of nine of the following statuses.

**Active** A prescription with this status can be filled or refilled.

**Cancelled** This status is used when a prescription was made inactive either by a new prescription or by the request of a physician.

**Deleted** This status is used when a prescription is deleted. Prescriptions are no longer physically deleted from the system, but marked as deleted. Once a prescription is marked deleted no access is allowed other than view.

**Expired** This status indicates the expiration date has passed.

**Note:** A prescription which was cancelled or has expired more recently than the date specified by the cutoff date, typically 45 days in the past, can still be acted upon.

**Hold** A prescription that was placed on hold due to reasons determined by the pharmacist.

**Non-verified** Depending on a site parameter, prescriptions entered by a technician do not become active until they are reviewed by a pharmacist. Until such review, they remain non-verified and cannot be printed, cancelled, or edited except through the *Verification* menu.

**Pending Due** This status is given to prescriptions when a drug/drug

**to Drug** interaction is encountered during the new order entry

**Interactions** or editing of a prescription.

**Refill** A second or subsequent filling authorized by the provider.

**Suspended** A prescription which will be filled at some future date.

**Remote Medical** A remote medical center is a VAMC outpatient

**Center** pharmacy that transmits prescription data to the host CMOP for filling and mailing.

**Reprinted Label** Unlike a partial prescription, a reprint does not count as workload.

**Sig** The instructions printed on the label.

**Significant** The potential for harm is either rare or generally known so that it is reasonable to expect that all prescribers have taken this information into account.

**Suspense** A prescription may not be able to be filled on the day it was requested. When the prescription is entered, a label is not printed. Rather, the prescription is put in the RX SUSPENSE file (#52.5) to be printed at a later date.

**VistA** Acronym for **V** eterans Health **I** nformation **S** ystems and **T** echnology **A** rchitecture.

## APPENDICES

### Appendix A: Interface Message Examples

**Interface Log Messages**

**+** XXX-XXX = Transmission #

XXX-XXX-XXX = Order #

xx = Query #

**ACK**

ACK1 ACK message never received for order #XXX-XXX-XXX

ACK2 EOT received with no terminator while waiting for ACK message

ACK3 EOT received while waiting for ACK message

ACK4 ENQ received with no terminator while waiting for ACK message

ACK5 Unexpected character received: \_$S(X&gt;31:$C(X),1:)\_ (\_X\_) while waiting for ACK message

ACK6 Timeout Timer D reading ACK message

ACK7 ACK message longer than 240 characters

ACK8 ACK message did not end with ETX

ACK9 ACK was null

ACK10 Timeout reading ACK checksum

ACK11 ACK checksum contained an invalid hex digit (\_X\_)

ACK12 ACK checksum does not match

ACK13 Order #XXX-XXX-XXX was rejected by CMOP

ACK14 ENQ received with no terminator

ACK15 MSA order # did not match XXX-XXX-XXX # expected

**Send Messages**

Transmission # XXX-XXX finished downloading.

Downloading Transmission # XXX-XXX

Batch Header Rejected by Vendor for Transmission XXX-XXX

Batch Header for transmission XXX-XXX rejected max times. DHCP Stopping interface.

SND1 Timer A timeout after sending a line of text.

SND2 ACK Received with bad block number after sending line of text, ASCII (\_$G(X)\_)  \_X

Expected ASCII (\_$G(PSXBLK)\_).

SND3 NAK Received with no terminator after sending a line of text.

SND4 NAK Received after sending a line of text.

SND5 EOT Received with no terminator after sending a line of text.

SND6 Garbage received after sending a line of text. (\_X\_)

SND7 EOT Received, aborting send.

SND8 Aborting Send.  Error processing order

# XXX-XXX-XXX.  Text: \_PSXTXT

SND9 ACK,\_$G(PSXBLK)\_ received with no terminator after sending a line of text.

STP Stopping the interface now

**Master Messages**

MST1 ENQ received with no terminator while Bidding for Master status.

MST2 NAK received with no terminator while Bidding for Master status.

MST3 ACK without 0 received while Bidding for Master status.

MST4 Garbage received while Bidding for Master status.

MST5 NAK received while Bidding for Master status.

MST6 No response from CMOP while Bidding for Master Status

MST7 Simultaneous bid for Master status by CMOP and DHCP.

MST8 ACK received with no terminator while Bidding for Master status.

MST9 CMOP won't respond, waiting 45 seconds to try again

**Query Messages**

QUERY # XX initiated.\_$G(PSXQRYA)

QUERY # XX completed.\_$G(PSXQRYA)

QRY1	QRY message never received for Query # XX

QRY2 EOT received with no terminator while waiting for QRY message

QRY3 EOT received while waiting for QRY message

QRY5 Unexpected character received: \_$S(X&gt;31:

$C(X),1:)\_ (\_X\_) while waiting for RY message

QRY5 Unexpected character received: \_X\_

QRY6 Timeout Timer D reading RY message

QRY7	QRY message longer than 240 characters

QRY8	QRY message did not end with ETX

QRY9	QRY was null

QRY10 Timeout reading QRY checksum

QRY11 QRY checksum contained an invalid hex digit (\_X\_)

QRY12 QRY checksum does not match

QRY13 Message # XX was rejected by OM CS

QRY14 ENQ received with no terminator

QRY15 MSA message ID did not match PSXQRYID #  expected

QRY16 Block count greater than 7.

QRY17 Wrong Block count received.

QRY18 Maximum retries reached for receiving  message.

QRY19 Maximum Rxs received, Query terminated.

QRY20 No activity on line continuing to  monitor.

### Appendix B: Label Examples

Figure 1: Example of a CMOP Rx Label (Part 1)

<!-- image -->

Figure 2: Example of a CMOP Rx Label (Part 2)

<!-- image -->

Figure 3: Example of a CMOP Rx Label (Part 3)

<!-- image -->

Figure 4: Example of a CMOP Rx Label (Part 4)

<!-- image -->

**Appendix C: Marking CMOP Drugs When a New Dispense Unit Is Required**

The following method is used by several facilities to ease the process of marking CMOP drugs when a new dispense unit is required. There are several ways to complete this process and this is an example of just one method several sites have found helpful.

Table 1: Marking CMOP Drugs - Actions

| **Action to be Taken**                                                                                                                                                                                                                                                                                                            | **Example**                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1.	Select the  *CMOP Drug/Item Management*  option.                                                                                                                                                                                                                                                                               | Select CMOP Site Manager Menu Option:  **CMOP D**  rug/Item Management                                                                                                                                                                                                                                                                                                                                                                                    |
| 2.	Next select the  *Drug Enter/Edit*  option.                                                                                                                                                                                                                                                                                    | Select CMOP Drug/Item Management Option:  **DRUG E**  nter/Edit                                                                                                                                                                                                                                                                                                                                                                                           |
| 3.	Enter the old generic drug name.  *[The dispense unit is one box.]*                                                                                                                                                                                                                                                            | Select DRUG GENERIC NAME:  **H3616 HOLLISTER #3616 5'S**  XA402    DRAINABLE POUCH/CONVEX BARRIER 1 1/2"                                                                                                                                                                                                                                                                                                                                                  |
| 4.	Mark the drug as an outpatient pharmacy item.                                                                                                                                                                                                                                                                                  | DO YOU WANT TO MARK THIS DRUG AS AN Outpatient Pharmacy ITEM? YES//  **Y**  (YES)                                                                                                                                                                                                                                                                                                                                                                         |
| 5.	Edit the old drug name.  *[At this point, replace the first letter of the drug name with a lower case z plus the first letter of the drug name so it will not appear again unless requested.]*                                                                                                                                 | GENERIC NAME: HOLLISTER #3616 5'S//  Replace  **H**  With  **zH**  Replace  zHOLLISTER#3616 5'S                                                                                                                                                                                                                                                                                                                                                           |
| 6.	Exit the option by entering an up-arrow (^) at the “MESSAGE” prompt. This will return you to the “Select DRUG GENERIC NAME” prompt.                                                                                                                                                                                            | MESSAGE: DRAINABLE POUCH/CONVEX BARRIER 1 1/2" Replace  **^**                                                                                                                                                                                                                                                                                                                                                                                             |
| 7.	Enter the new drug name.  *[Since this name will be overwritten with the VA Print name it can be named anything you prefer.]*                                                                                                                                                                                                  | Select DRUG GENERIC NAME:  **HOL3616**  ARE YOU ADDING 'HOL3616' AS A NEW DRUG (THE NTH)?  **Y**  (YES)  DRUG NUMBER: 6528//  **&lt;RET&gt;**  DRUG VA CLASSIFICATION:  **&lt;RET&gt;**  DRUG FSN:  **&lt;RET&gt;**  DRUG NATIONAL DRUG CLASS:  **&lt;RET&gt;**  DRUG NON-FORMULARY:  **&lt;RET&gt;**  DRUG INACTIVE:  **&lt;RET&gt;**  DRUG MESSAGE:  AVAILABLE AT CMOP.  DRUG RESTRICTION:  **&lt;RET&gt;**                                             |
| 8.	Again mark the new drug as an outpatient pharmacy item.                                                                                                                                                                                                                                                                        | DO YOU WANT TO MARK THIS DRUG AS AN Outpatient Pharmacy ITEM? NO//  **Y**  (YES)                                                                                                                                                                                                                                                                                                                                                                          |
| 9.	Enter an up-arrow (^) to exit the option.                                                                                                                                                                                                                                                                                      | GENERIC NAME: HOL3616//  **^**  Select DRUG GENERIC NAME:  **^**                                                                                                                                                                                                                                                                                                                                                                                          |
| NEXT. . .                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 10.	Enter VA FileMan.  *[If you do not have access to VA FileMan, give a list to your IRM contact displaying the  name of the drug data is to be transferred from and the name of the drug you wish the data to be transferred to.]*                                                                                              | Select CMOP Drug/Item Management Option:  **^^FM**  VA FileMan  VA FileMan Version 20.0                                                                                                                                                                                                                                                                                                                                                                   |
| 11.	Select the  *Transfer Entries*  option.                                                                                                                                                                                                                                                                                       | Select VA FileMan Option:  **TRANSFER ENTRIES**                                                                                                                                                                                                                                                                                                                                                                                                           |
| 12.	 Then select the  *Transfer File Entries*  option.                                                                                                                                                                                                                                                                            | Select TRANSFER OPTION:  **TRANSFER FILE ENTRIES**                                                                                                                                                                                                                                                                                                                                                                                                        |
| 13.	Enter DRUG into the “INPUT TO WHAT FILE “ prompt.                                                                                                                                                                                                                                                                             | INPUT TO WHAT FILE:  **DRUG**  (4046)  TRANSFER FROM FILE: DRUG//  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                        |
| 14.	Enter the new drug in the “TRANSFER DATA INTO WHICH DRUG” prompt.                                                                                                                                                                                                                                                             | TRANSFER DATA INTO WHICH DRUG:  **HOL3616**  *[This is the new drug.]*                                                                                                                                                                                                                                                                                                                                                                                    |
| 15.	Enter the name of the old drug at the “TRANSFER FROM DRUG” prompt.                                                                                                                                                                                                                                                            | TRANSFER FROM DRUG:  **zHOLLISTER#3616**  *[This is the old drug.]*                                                                                                                                                                                                                                                                                                                                                                                       |
| 16.	Do not delete the old entry.                                                                                                                                                                                                                                                                                                  | WANT TO DELETE THIS ENTRY AFTER IT'S TRANSFERRED? NO//  **&lt;RET&gt;**  ...EXCUSE ME, THIS MAY TAKE A FEW MOMENTS...                                                                                                                                                                                                                                                                                                                                     |
| 17.  ****IMPORTANT****  Do not update the pointers.  *[This will edit all the prescriptions on file to the new dru*  g  *, but*  ***will not***  *edit the quantity.]*                                                                                                                                                            | SINCE THE TRANSFERRED ENTRY MAY HAVE BEEN 'POINTED TO' BY ENTRIES IN THE 'DRUG' FILE,ETC.,  DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? NO//  **&lt;RET&gt;**                                                                                                                                                                                                                                                                    |
| NEXT. . .                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 18.	Again select the  *CMOP Drug/Item Management*  option.                                                                                                                                                                                                                                                                        | Select CMOP Site Manager Menu Option:  **CMOP D**  rug/Item Management                                                                                                                                                                                                                                                                                                                                                                                    |
| 19.	Next select the  *Drug Enter/Edit*  option.                                                                                                                                                                                                                                                                                   | Select CMOP Drug/Item Management Option:  **DRUG E**  nter/Edit                                                                                                                                                                                                                                                                                                                                                                                           |
| 20.	Enter the old drug name at the “Select DRUG GENERIC NAME” prompt.                                                                                                                                                                                                                                                             | Select DRUG GENERIC NAME:  **zHOLLISTER#3616 5'S**                                                                                                                                                                                                                                                                                                                                                                                                        |
| 21.	Mark the drug as an outpatient pharmacy item.                                                                                                                                                                                                                                                                                 | DO YOU WANT TO MARK THIS DRUG AS AN Outpatient Pharmacy ITEM? NO//  **Y**  (YES)                                                                                                                                                                                                                                                                                                                                                                          |
| 22.	Press return (  **&lt;RET&gt;**  ) at the “GENERIC NAME” prompt.                                                                                                                                                                                                                                                              | GENERIC NAME: zHOLLISTER#3616 5'S Replace  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                |
| 23.	Enter a message.  *[This step is optional, but several medical centers have found it to be helpful for their Automated Data Processing Applications Coordinator (ADPAC.) When a drug is selected and this message appears, it should indicate to the user that the incorrect drug has been selected.]*                        | MESSAGE:**INACTIVE**                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 24.	Enter ^SYNONYM to jump to the SYNONYM field.                                                                                                                                                                                                                                                                                  | VA CLASSIFICATION: XA402//  **&lt;RET&gt;**  DEA,SPECIAL HDLG: S//  **^SYNONYM**                                                                                                                                                                                                                                                                                                                                                                          |
| 25.	Enter the @ sign to delete all the synonyms from the old drug.  *[This is necessary to prevent calling up the old drug instead of the new one.]*                                                                                                                                                                              | Select SYNONYM: H3616//  **@**  SURE YOU WANT TO DELETE THE ENTIRE 'H3616'SYNONYM?  **Y**  (YES)  SELECT SYNONYM:  **&lt;RET&gt;**  *[This option has been abbreviated to save space.]*                                                                                                                                                                                                                                                                   |
| 26.	At the “INACTIVATE DATE” prompt, enter today’s date to inactivate the old drug.                                                                                                                                                                                                                                               | INACTIVATE DATE:  **T**  (OCT 26, 1996)                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 27.	Enter an up-arrow (^) at the “REORDER LEVEL” prompt to take you back to the “Select DRUG GENERIC NAME” prompt.                                                                                                                                                                                                                | REORDER LEVEL:  **^**                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 28.	Select the new drug.                                                                                                                                                                                                                                                                                                          | Select DRUG GENERIC NAME:  **HOL3616**  XA402   Available at CMOP                                                                                                                                                                                                                                                                                                                                                                                         |
| 29.	Accept the default of YES at the “DO YOU WANT TO MARK THE DRUG AS AN Outpatient Pharmacy ITEM” prompt.                                                                                                                                                                                                                        | DO YOU WANT TO MARK THIS DRUG AS AN Outpatient Pharmacy ITEM? YES//  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                      |
| 30.	Continue to press return (  **&lt;RET&gt;**  ) through the option.                                                                                                                                                                                                                                                            | GENERIC NAME: HOL3616//  **&lt;RET&gt;**  *[This option has been abbreviated to save space.]*                                                                                                                                                                                                                                                                                                                                                             |
| 31.	Edit the DISPENSE UNIT and the DISPENSE UNITS PER ORDER UNIT to reflect the requirements of the VA Print Name                                                                                                                                                                                                                 | DISPENSE UNIT: BOX//  **EA**  DISPENSE UNITS PER ORDER UNIT: 1//  **5**                                                                                                                                                                                                                                                                                                                                                                                   |
| 32.	Continue to press return (  **&lt;RET&gt;**  ) to exit the option.                                                                                                                                                                                                                                                            | *[This option has been abbreviated to save space.]*                                                                                                                                                                                                                                                                                                                                                                                                       |
| 33.	Select the  *CMOP Mark/Unmark (Single drug)*  option from the  *CMOP Drug/Item Management*  menu.  The drug can now be marked for CMOP. It does not have to be matched to the NATIONAL DRUG file (#50.6) (NDF) if the old drug was matched. If it was not matched, you will have to match, verify, and merge the drug in NDF. | Select CMOP Drug/Item Management Option:  **CMOP M**  ark/Unmark (Single drug)  This option allows you to choose entries from your drug file and helps you review your NDF matches and mark individual entries to send to CMOP.  If you mark the entry to transmit to CMOP, it will replace your Dispense Unit with the VA Dispense Unit. In addition, you may overwrite the local drug name with the VA Print Name and the entry will remain uneditable. |
| 34.	Enter the name of the new drug.                                                                                                                                                                                                                                                                                               | Select DRUG GENERIC NAME:  **HOL3616**  XA402   Available at CMOP                                                                                                                                                                                                                                                                                                                                                                                         |
| 35.	Information will display for the new drug.                                                                                                                                                                                                                                                                                    | Local Drug Generic Name: HOL3616  ORDER UNIT: BX  DISPENSE UNITS/ORDER UNITS: 5  DISPENSE UNIT: EA  VA Print Name: POUCH,DRAINABLE,FIRST CHOICE H#3616 VA Dispense Unit: EA  VA Drug Class: XA402                                                                                                                                                                                                                                                         |
| 36.	Enter YES to mark the drug to transmit to the CMOP.                                                                                                                                                                                                                                                                           | Do you wish to mark this drug to transmit to CMOP?  Enter Yes or No:  **Y**  ES                                                                                                                                                                                                                                                                                                                                                                           |
| 37.	Enter a quantity dispense message to assist the user inputting the prescription information.                                                                                                                                                                                                                                  | QUANTITY DISPENSE MESSAGE:  **5EA = 1 BOX = 30 DAY SUPPLY**                                                                                                                                                                                                                                                                                                                                                                                               |
| 38.	Enter YES to overwrite your local name.                                                                                                                                                                                                                                                                                       | Do you wish to overwrite your local name?  Enter Yes or No:  **Y**  ES                                                                                                                                                                                                                                                                                                                                                                                    |
| 39.	Press return (  **&lt;RET&gt;**  ) to exit the  *CMOP Mark/Unmark (Single drug)*  option                                                                                                                                                                                                                                      | Select DRUG GENERIC NAME:  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                                                                                                |
| NEXT. . .                                                                                                                                                                                                                                                                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 40.	Select the  *CMOP Drug/Item Management*  option.                                                                                                                                                                                                                                                                              | Select CMOP Site Manager Menu Option:  **CMOP D**  rug/Item Management                                                                                                                                                                                                                                                                                                                                                                                    |
| 41.	Select the  *Drug Enter/Edit*  option.                                                                                                                                                                                                                                                                                        | Select CMOP Drug/Item Management Option:  **DRUG E**  nter/Edit                                                                                                                                                                                                                                                                                                                                                                                           |
| 42.	Select the new drug generic name.                                                                                                                                                                                                                                                                                             | Select DRUG GENERIC NAME:  **HOL3616**  POUCH,DRAINABLE,FIRSTCHOICE H#3616                                                                                                                                                                                                                                                                                                                                                                                |
| 43.	Mark the drug as an outpatient pharmacy item.                                                                                                                                                                                                                                                                                 | DO YOU WANT TO MARK THIS DRUG AS AN Outpatient Pharmacy ITEM? NO//  **Y**  (YES)                                                                                                                                                                                                                                                                                                                                                                          |
| 44.	Press return (  **&lt;RET&gt;**  ) at the “GENERIC NAME” and “MESSAGE” prompts.                                                                                                                                                                                                                                               | GENERIC NAME: POUCH,DRAINABLE,FIRSTCHOICE H#3616 Replace  **&lt;RET&gt;**  MESSAGE: Available at CMOP//  **&lt;RET&gt;**                                                                                                                                                                                                                                                                                                                                  |
| 45.	Enter a quantity dispense message to assist the user inputting the prescription information.                                                                                                                                                                                                                                  | QUANTITY DISPENSE MESSAGE:  **5EA = 1 BOX = 30 DAY SUPPLY**                                                                                                                                                                                                                                                                                                                                                                                               |
| 46.	Exit the  *Drug Enter/Edit*  option.                                                                                                                                                                                                                                                                                          | VA CLASSIFICATION:XA402//  **&lt;RET&gt;**  DEA, SPECIAL HDLG:S//  **^**                                                                                                                                                                                                                                                                                                                                                                                  |

**Appendix D: Flowchart for Processing a CMOP Prescription**

A single line border indicates that the action is a MEDICAL CENTER ACTIVITY.

A double line border indicates that the action is a HOST CMOP ACTIVITY.

Rx Entered at Medical Center

Rx Screened for CMOP Criteria

Drug Marked for CMOP in DRUG file (#50)

Mail-No CMOP

No Tradename

Rx Meets CMOP Criteria

<!-- image -->

Suspended for CMOP Transmission in RX SUSPENSE file (#52.5)

<!-- image -->

CMOP INDICATOR field in RX SUSPENSE file (#52.5) = Queued for Transmission

<!-- image -->

Activity Log in file #52=Suspended for CMOP Transmission

<!-- image -->

User Selects Initiate A Transmission

TRANSMIT DATA THRU TODAY// **&lt;RET&gt;**

ARE YOU SURE YOU WISH TO CONTINUE ? NO// **Y** ES

<!-- image -->

Transmission Job is Queued

Xmit Status in CMOP SYSTEM file (#550) = Transmitting Data

Select All Rx’s Queued for Transmission from Rx Suspense

Send/Transmit selected Rx’s to ECME for electronic billing

Wait to receive response from payer

(15 seconds for each e-billable Rx; 2 hours max.)

(e.g., 300 e-billable Rx’s = 4500 seconds/3600 = 1.25 hrs)

From the selected Rx’s, filter Rx’s that have unresolved DUR/REFILL TOO SOON rejects

From the remaining list, filter Rx’s for which the 3 rd party payer has not responded

A MailMan message is generated and sent to PSXMAIL keyholders

Mark Selected Rx’s CMOP Indicator = Loading for Transmission

Rescreens Data for CMOP Transmission

Builds Transmission Data in CMOP RX QUEUE file (#550.1)

CMOP Error Encountered Message Created for Rx’s which

Were Selected, but not Transmitted

Creates Transmission Number in CMOP TRANSMISSION file (#550.2)

Creates MailMan Message for Transmission Data and Sends to the Host CMOP Server

Transmission Confirmation Message Generated

Creates Transmission Entry in the CMOP EVENT MULTIPLE

Subfile of PRESCRIPTION file (#52) Marking the Entry as Transmitted

An Entry Is Made in the ACTIVITY LOG Subfile in PRESCRIPTION file (#52) as Transmitted to CMOP

CMOP Indicator in File #52.5 for All Transmitted Rx’s = Transmission Completed

Xmit Status in CMOP SYSTEM file (#550) = No Current Transmission

Data Has Transmitted/Job Is Complete

<!-- image -->

Transmission Message Is Received at CMOP Facility by the CMOP Server

<!-- image -->

Transmission Job is Queued

Xmit Status in CMOP SYSTEM file (#550) = Transmitting Data

Select All Rx’s Queued for Transmission from Rx Suspense

Send/Transmit selected Rx’s to ECME for electronic billing

Wait to receive response from payer

(15 seconds for each e-billable Rx; 2 hours max.)

(e.g., 300 e-billable Rx’s = 4500 seconds/3600 = 1.25 hrs)

From the selected Rx’s, filter Rx’s that have unresolved DUR/REFILL TOO SOON rejects

The third party payer rejects the claim due to a DUR or a Refill Too Soon finding

The patient eligibility is TRICARE or CHAMPVA and the

third party payer rejects the claim for any reason

The patient eligibility is VETERAN, the prescription is an original fill that is unreleased,

the third party payer rejects the claim due to a Reject Resolution Required reject,

and the total gross amount of the prescription is at or above the user defined threshold amount

for the Reject Resolution Required reject.

From the remaining list, filter Rx’s for which the 3 rd party payer has not responded

A MailMan message is generated and sent to PSXMAIL keyholders

Mark Selected Rx’s CMOP Indicator = Loading for Transmission

Rescreens Data for CMOP Transmission

Builds Transmission Data in CMOP RX QUEUE file (#550.1)

CMOP Error Encountered Message Created for Rx’s which

Were Selected, but not Transmitted

Creates Transmission Number in CMOP TRANSMISSION file (#550.2)

Creates MailMan Message for Transmission Data and Sends to the Host CMOP Server

Transmission Confirmation Message Generated

Creates Transmission Entry in the CMOP EVENT MULTIPLE

Subfile of PRESCRIPTION file (#52) Marking the Entry as Transmitted

An Entry Is Made in the ACTIVITY LOG Subfile in PRESCRIPTION file (#52) as Transmitted to CMOP

CMOP Indicator in File #52.5 for All Transmitted Rx’s = Transmission Completed

Xmit Status in CMOP SYSTEM file (#550) = No Current Transmission

Data Has Transmitted/Job Is Complete

<!-- image -->

Transmission Message Is Received at CMOP Facility by the CMOP Server

<!-- image -->

Tasked Job Performs the Following:

Data Is Downloaded Into CMOP DATABASE file (#552.2)

for Transmission to the Vendor

Data Is Entered in the CMOP MASTER DATABASE file (#552.4)

<!-- image -->

CMOP Review Message Containing a List of All Rx’s for This Transmission Is Sent

<!-- image -->

Transmission Acknowledgement Message Is Created and Sent to the Medical Center

<!-- image -->

Acknowledgement Message Received by the CMOP Server at Medical Center

<!-- image -->

Tasked Job Completes the Following:

Acknowledgement Date/Time Is Filed in the CMOP TRANSMISSION

file (#550.2)

<!-- image -->

The Transmission Phase of the Rx Is Completed

<!-- image -->

The Rx Is Downloaded to the Vendor Automated Dispensing System for Filling

<!-- image -->

Download Acknowledgement Message is Created and Sent to the Medical Center

<!-- image -->

Download Acknowledgement message is received by CMOP Server at the Medical Center

<!-- image -->

Downloaded Data is purged from the CMOP RX QUEUE file (#550.1)

<!-- image -->

Rx Release Data Is Received by CMOP VistA from the Vendor System

<!-- image -->

Rx Data Stored Temporarily in the CMOP RELEASE file (#552.3)

<!-- image -->

The CMOP Background Filer Files Data Listed Ready to File from CMOP RELEASE file (#552.3), Files It in the CMOP MASTER DATABASE

file (#552.4), and Marks the Rx Status = Released

<!-- image -->

The Background Filer Selects All Data Marked Released In the CMOP MASTER DATABASE file (#552.4), Builds a CMOP Release MailMan Message for Each Facility Having Released Data and Marks the Rx Status = Returned

<!-- image -->

The Mail Message Is Sent to the Medical Centers to the CMOP Server

*****USERS DO NOT RECEIVE THESE MESSAGES*****

<!-- image -->

Release Data Message Is Received by the CMOP Server

<!-- image -->

Job Is Tasked to File Release Information from the Release

Data Message into the PRESCRIPTION file (#52). This Action Will Release the Rx and Generate Any Prescription Copayment Necessary

<!-- image -->

A Return Release Acknowledgement Message Is Built on Completion of Filing the Rx’s. This Message Is Sent to the Host Facility

<!-- image -->

CMOP Server at the CMOP Host Facility to Update the CMOP MASTER DATABASE file (#552.4).

### Appendix E: CMOP MailMan Messages

The Consolidated Mail Outpatient Pharmacy software generates numerous MailMan messages to notify pharmacy personnel regarding the status of background procedures. Messages received by the host CMOP and the medical centers are included here with a description of the content. All messages are sent to users who hold the CMOP Manager security key (PSXCMOPMGR).

#### Mail Messages Seen At Remote Medical Centers

1.	The **CMOP Activation Request** message is generated when the Outpatient Pharmacy personnel submit a request to activate the medical center facility to do CMOP processing. This message only indicates that a user has selected to activate the site using the CMOP Site Manager option *Activate/Inactivate CMOP Processing* . **Activation does not take place until a response is received from the CMOP host.**

Subj: CMOP Activation Request  [#38898] 11 Dec 96 10:03  5 Lines

From: POSTMASTER (Sender: OPPHARMACIST2,THREE)  in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

Request to activate.

CMOP            :  LEAVENWORTH

Requester       :  OPPHARMACIST2,THREE

Action Date/Time:  DEC 11,1996@10:03

2.	The **CMOP Activation Approved** message is returned from the CMOP facility when the CMOP Manager has approved the activation request. At the time of this message, an alert is also generated to all CMOP Manager key holders indicating the approval. At this time, the site becomes active for CMOP processing. **Pharmacy users should sign off the system completely. The users should sign back onto the system after receiving the approval message to set up the appropriate CMOP/Outpatient site parameters. All prescriptions  processed after the site parameters are set up for CMOP will be screened and suspended for CMOP if transmission criteria is met.**

An example of this message is shown on the following page

Subj: CMOP Activation Approved  [#33619] 09 Feb 97 11:50  6 Lines

From: POSTMASTER                          in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

Request to activate CMOP processing.

CMOP             :  LEAVENWORTH

Approving Offical:  CMOPPHARMACIST30,THREE

Action Date/Time :  FEB 9,1997@11:50

Action           :  Approved

3.	The **CMOP Transmission Confirmation** message is created when medical center CMOP transmission data has been handed to MailMan for delivery to the CMOP host facility. The subject line of the message will include the transmission number. Each **successful** transmission will generate a transmission confirmation message. **If a user initiates a transmission and does not receive a transmission confirmation message, the medical center IRM Service should be contacted for assistance.**

Subj: CMOP 521-737 Transmitted  [#38862] 09 Feb 97 08:15  8 Lines

From: POSTMASTER (Sender: CMOPPHARMACIST30,THREE)  in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

CMOP TRANSMISSION CONFIRMATION:

Pharmacy Division    :  BIRMINGHAM

Batch Number         :  521-737

Transmitted by       :  CMOPPHARMACIST30,THREE

Date/Time            :  FEB 4,1997@08:15:48

Total orders/Rx's    :  1/5

Beginning order #    :  12

Ending order #       :  12

4.	The **CMOP Transmission Acknowledgment** message is created by the host CMOP software when the data transmission is received, data is validated, and loaded into safe storage in the CMOP database. This message serves two purposes. Initially the message is delivered to the remote medical center to the PSXMAIL key holders to indicate that the CMOP has successfully received the data transmitted. The message is also delivered to the medical center CMOP server software and is used to file the date and time the data was received at the CMOP in the transmission entry in the CMOP TRANSMISSION file (#550.2). Receipt of **both** the Transmission Confirmation and the Transmission Acknowledgment messages for a single transmission confirm that the data transmitted and downloaded to the CMOP facility successfully.

Subj: CMOP 521-524 Acknowledged.  [#34712] 04 Apr 95 17:17  8 Lines

From: POSTMASTER                            in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

CMOP TRANSMISSION ACKNOWLEDGEMENT:

Pharmacy Division    :  BIRMINGHAM

Batch Number         :  521-737

Transmitted by       :  CMOPPHARMACIST30,THREE

Date/Time            :  FEB 4,1997@09:16:43

Total orders/Rx's    :  1/5

Beginning order #    :  12

Ending order #       :  12

5.	The **CMOP Error Encountered** message is created when medical center CMOP transmission data has been handed to MailMan for delivery to the CMOP host facility. This message is a direct result of the CMOP software screening prescriptions suspended for CMOP during data transmission. **If a problem is detected with a prescription selected for transmission, the prescription is not transmitted to the CMOP, but is noted in this message to the user to provide information to correct the problem** . If the data is corrected as noted in this message, the prescription will be included in the next transmission. If the data problem is not corrected, the prescription will continue to be listed in this message each time a transmission is initiated. **If the data is not corrected the prescription will never be transmitted.** The CMOP Error Encountered message may be sent in varying formats depending on the data problems to be reported. Two examples are shown on the following page.

**Example 1**

Subj: CMOP Error Encountered  [#34392] 11 Dec 96 08:43  16 Lines

From: POSTMASTER (Sender: CMOPPHARMACIST30,THREE)  in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

An error has been encountered while processing prescription data for the

Consolidated Mail Outpatient Pharmacy system.

Date/Time    :  DEC 11,1996@08:43

Process      :  Data Validation

Error Type   :  Invalid or missing data

Description  :

RX #     Fill            Data Field

155465A    Original      Duplicate Rx

Action Taken:  Rx's not sent to CMOP but still suspended for transmission.

Recommended action:  Correct invalid data.

**Example 2**

Subj: CMOP Error Encountered  [#38880] 05 Dec 96 14:14  21 Lines

From: POSTMASTER (Sender: OPPHARMACIST2,THREE)  in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

An error has been encountered while processing prescription data for the

Consolidated Mail Outpatient Pharmacy system.

Date/Time	:  DEC 5,1996@14:14

Process	:  Transmission of Batch Data

Error Type	:  Invalid or missing data

Description  :

The following data is missing in the OUTPATIENT SITE file.

State

Street Address

City

Zip Code

Area Code

Phone Number

Action Taken:  No data transmission will occur without this information.

Recommended action:  Correct invalid data.

6.	The **CMOP Inactivation Notice** message is generated when the Outpatient Pharmacy personnel selects to inactivate the medical center using the CMOP Site Manager menu option *Activate/Inactivate CMOP Processing.* **Inactivation of CMOP processing is immediately effective** . **Users who do not sign off and then sign back onto the system when inactivation takes place will continue to do CMOP processing.**

Subj: CMOP Inactivation Notice  [#38894] 05 Dec 96 10:57  05 Lines

From: POSTMASTER (Sender: OPPHARMACIST2,THREE)  in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

Inactivation notice sent

CMOP            :  LEAVENWORTH

Requester       :  OPPHARMACIST2,THREE

Action Date/Time:  DEC 5,1996@10:57

7.	The **CMOP Auto-Transmission Schedule** message is generated when the Outpatient Pharmacy personnel use the *Setup Auto-transmission* option from the *CMOP Site Manager* menu to set up an automated transmission schedule to the CMOP host facility. **The message notifies key holders that manual transmissions are not necessary to transmit data** . Transmissions will begin automatically on the date and time indicated and continue for the selected frequency until the transmissions are unscheduled or modified.

Subj: CMOP Auto-Transmission Schedule  [#38875] 11 Dec 96 09:32  7 Lines

From: POSTMASTER (Sender: CMOPPHARMACIST30,THREE)  in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

Auto-transmission Schedule.

Auto-transmission Schedule.

Facility                       :  BIRMINGHAM, AL.

Date Initiated                 :  Dec 11, 1996@09:32

Begin Automatic Transmissions  :  Dec 11, 1996@09:32

Number of days to transmit thru:  1

Scheduling Frequency (hours)   :  6

Initiating Official            :  CMOPPHARMACIST30,THREE

8.	The **CMOP Not Dispensed Rx List** message is generated when release information indicates a prescription has been cancelled ( **not dispensed** ) by the vendor automated system. The prescription at the remote medical center is marked **not dispensed** in the PRESCRIPTION file (#52). The prescription is not marked with a status of Cancelled. The prescriptions may be filled locally, edited and re-suspended, or resubmitted for CMOP processing. Cancellation reasons are listed with the Rx number and other transmission information to assist the user in correcting the cause of the cancellation and re-submitting the prescription for filling by the CMOP. A separate message is created for each pharmacy division.

The CMOP Not Dispensed RX List message includes the standard symbols denoting additional information used by the Outpatient Pharmacy.

- Prescription numbers with a corresponding ePharmacy claim are marked with ‘e’.

- Prescription numbers with a first party copay are marked with ‘$’.

Subj: GENERIC CITY CMOP Not Dispensed Rx List, [#78218200] 07/15/14@23:01 15

lines

From: POSTMASTER - POSTMASTER In 'IN' basket. Page 1

-------------------------------------------------------------------------------

Not Dispensed Rx Report for the GENERIC CITY Division.

The following prescriptions were not dispensed by the vendor:

Patient: PSXPATIENT,ONE 				SSN: ###-##-####

Rx #: ########$e (REF5) Qty: 2 Trans #: 55403

Drug: CATHETER SILASTIC 22FR 30CC

Transmitted under CMOP ID: XX923

Reason: NOT STOCKED CONTACT CMOP WITH USAGE

Instructions: Prescriptions cannot be processed at CMOP for the reason listed

above. Please review the prescription and take the appropriate action(s).

If you have any questions, contact your CMOP contact person.

9.	The **CMOP Acknowledgement not Received** message is sent when a Transmission Acknowledgement message has not been received for a previous transmission after 24 hours. The CMOP software checks each transmission entry in the CMOP TRANSMISSION file (#550.2) 24 hours after the data is transmitted to ensure that the data was received at the CMOP host facility. If an acknowledgement date/time has not been filed for the transmission, this message reminds the key holders that the Transmission Acknowledgement message has not yet been received. The user should first contact the medical center IRM Service and request that the MailMan queue be checked to see if the transmission was sent. If it has been sent, the CMOP Manager at the host facility should be contacted to determine if there is another reason for the delay.

Subj: CMOP Acknowledgement not Received  [#38915] 20 FEB 97 15:56  3 Lines

From: POSTMASTER                           in 'IN' basket.   Page 1

------------------------------------------------------------------------------

An acknowledgement message for transmission # 739 has not been

received within the specified time.  Please contact the CMOP facility

to see if there is a problem.

10. The **CMOP Recovery Message** is sent whenever a failed CMOP transmission is detected. This message is simply a notification message that the last transmission did not complete. CMOP recovery procedures were initiated to reset the data so that it will be transmitted in the next transmission for that division.

Subj: CMOP Recovery Message BIRMINGHAM, AL.  [#3288] 21 Feb 97 10:29 CST

11 Lines

From: &lt;POSTMASTER@BAB.ISC-BIRM.XX.XXX&gt;  in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

The last CMOP transmission did not complete properly. The data for this

transmission will be sent to the CMOP during the next transmission for

that division.

If you have scheduled auto transmissions for CMOP, please check to see

that they are still scheduled for the correct time.

This message is just a notification that problems were detected with the last

transmission and that the data was sent to the CMOP facility for processing.

If you are getting this message frequently, please contact your IRM staff.

Otherwise there is not anything that you need to do.

11. The e-Pharmacy **CMOP Not Transmitted Rx List Message** lists all e-billable prescriptions for which no response has been received from the third party payer. The  prescriptions listed have not been transmitted to CMOP and remain in the CMOP queue.

The prescriptions remain in the CMOP queue and transmit when the response from the third party payer is received, or the non-billable issue is resolved. Examples of non-billable issues are prescriptions for sensitive medications that need Release of Information and prescriptions for non-billable drugs (e.g., Over the Counter (OTC) products for CHAMPVA and TRICARE patients.)

The CMOP Not Transmitted Rx List Message displays the first date of the attempted submission, the number of times the prescription submission has been attempted and the date of the first unsuccessful transmit. The CMOP Not Transmitted Rx List message also displays the site name in the subject line.

Subj: ePHARMACY – CMOP Not TRANSMITTED RX List for site GENERIC CITY [#233739]

05/16/13@09:22

From: CMOP Package In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The prescriptions listed in this message did not transmit to CMOP for one of

the reasons below:

A response from the third party payer was not received

OR

The prescriptions are non-billable in VistA

The prescriptions will remain in the CMOP queue and will transmit when the

response from the third party payer is received, or the non-billable issue

is resolved.

Division: GENERIC CITY

-------------------------------------------------------------------------------

NOT TRANSMITTED

RX#/Fill	 PATIENT(LAST4) 	DRUG 				1ST DT #DAYS

--------------------------------------------------------------------------------

##########A/1 	PSXPATIENT,ONE(####) 	METOPROLOL TARTRATE 50M 	07/19/14 3

##########A/1 	PSXPATIENT,ONE(####) 	ALBUTEROL 100/IPRATRO 2 	07/19/14 3

##########A/1 	PSXPATIENT,ONE(####) 	FLUOCINONIDE 0.05% OINT 	07/19/14 3

##########A/10 PSXPATIENT,TWO(####) 	AMITRIPTYLINE 100MG TAB 	07/19/14 3

Total GENERIC CITY: 2 Patients and 4 Prescriptions.

12. The Message for Discontinued CMOP Prescription lists discontinued prescriptions with a status of Transmitted or Retransmitted

**Example 1 –** Discontinued by a Background Process

When a CMOP prescription with a status of Transmitted or Retransmitted is discontinued by a background process to the Outpatient Pharmacy options, e.g. CPRS or Registration V. 5.3 packages, then an email will be sent to the PSX EXTERNAL DISPENSE ALERTS mail group (if no recipients are defined in the new mail group, the message will be sent to PSXCMOPMGR key holders) notifying that a prescription was just discontinued for that prescription and that the CMOP status for the prescription just discontinued was either Transmitted or Retransmitted.

Subj: TROY – DC Alert on CMOP Rx 123456789 TRANSMITTED  [#90494]

03/03/09@17:37 8 lines

From: POSTMASTER  In 'IN' basket.   Page 1  *New*

------------------------------------------------------------------------

Rx #: 123456789   Fill: 0

Patient: OUTPATIENT,DCONE (6660)

Drug: TAMOXIFEN CITRATE 10MG TABS

Rx Status: DISCONTINUED BY PROVIDER

Processing Status: TRANSMITTED to CMOP on 02/27/09

Provider: OPPROVIDER, PROV

********    Please contact CMOP or take appropriate action    ********

Enter message action (in IN basket): Ignore//

------------------------------------------------------------------------

**Example 2** Discontinued by a Foreground Pharmacy Process

When a CMOP prescription with a status of Transmitted or Retransmitted is discontinued by a foreground Pharmacy process due to a duplicate drug scenario that would trigger the duplicate to be discontinued, then the Processing Status field of the duplicate drug message is highlighted to alert the user.

------------------------------------------------------------------------

Duplicate Drug A AND Z OINTMENT in Prescription: 123456789

Status: Active                       Issued: 11/27/09

Processing Status: Transmitted to CMOP on 11/27/09

SIG: APPLY 1 TUBE TO AFFECTED AREA TWICE A DAY

QTY: 1                         # of refills: 5

Provider: OPPROVIDER, PROV     Refills remaining: 5

Last filled on: 11/27/09

Days Supply: 5

------------------------------------------------------------------------

Discontinue RX # 123456789?

In the above example, the line “Processing Status: Transmitted to CMOP on 11/27/09” is bold.

#### Mail Messages Seen At CMOP Facilities

1.	The **CMOP Activation Request** message is generated when the Outpatient Pharmacy personnel submit a request to activate the medical center facility to do CMOP processing. This message is received at the host CMOP facility and notifies the CMOP Manager that a medical center is requesting to activate CMOP processing. An alert is also generated at the time of this message which requires a response from the CMOP Manager before the medical center can begin CMOP processing. This message is also used to update the CMOP NATIONAL SITE file (#552).

Subj: CMOP Activation Request  [#38899] 05 Dec 96 10:58  5 Lines

From: POSTMASTER      in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

Request to activate CMOP processing.

Facility         :  BIRMINGHAM, AL.

Requester        :  OPPHARMACIST2,THREE

Request date/time:  DEC 5,1996@10:58

2.	The **CMOP Activation Approval** message is sent to all holders of the key (PSXMAIL) at the host facility. This message notifies the manager that a medical center has now been activated to transmit data to the CMOP.

Subj: CMOP Activation Approval  [#38908] 11 Dec 96 10:28  6 Lines

From: POSTMASTER (Sender: CMOPPHARMACIST30,THREE)  in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

Request to activate CMOP processing.

Facility         :  BIRMINGHAM, AL.

Requester        :  CMOPPHARMACIST30,THREE

Request date/time:  DEC 11,1996@10:28

Action taken     :  Approved

3.	The **CMOP Inactivation Notice** is received by the CMOP host facility when the medical center inactivates CMOP processing. This message triggers an inactivation flag in the CMOP NATIONAL SITE file (#552). This flag indicates the medical center is inactive and data cannot be received from that medical center until a request to activate CMOP processing is received by the host and approved by the CMOP manager.

Subj: CMOP Inactivation Notice,BIRMINGHAM,AL. [#38895] 09 Feb 96 11:50 5 Lines

From: POSTMASTER     in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

Notice to Inactivate CMOP Processing.

Facility               :  BIRMINGHAM, AL.

Notifying Official     :  CMOPPHARMACIST30,THREE

Notification date/time :  FEB 9,1996@11:50

4.	The **CMOP (Batch Number) from (Site) Received** message is created when data is downloaded successfully into the CMOP database files at the host facility. This message informs the CMOP personnel that a transmission has arrived and is ready to transfer to the automated vendor system. If the CMOP interface is running when this data is received, it is automatically scheduled and downloaded to the vendor system without delay.

Subj: CMOP 521-737 from BIRMINGHAM Received.  [#34543] 04 Feb 95 15:52 8 Lines

From: POSTMASTER (Sender: CMOPPHARMACIST30,THREE)  in 'IN' basket.   Page 1

------------------------------------------------------------------------------

CMOP TRANSMISSION RECEIVED:

Pharmacy Division    :  BIRMINGHAM

Batch Number         :  521-737

Transmitted by       :  CMOPPHARMACIST30,THREE

Date/Time            :  Feb 04, 1997@08:43:44

Total orders/Rx's    :  1/5

Beginning order #    :  12

Ending order #       :  12

5.	The **CMOP Review # (Batch Number)** message is created on successful receipt of data from the medical center. This message provides a hard copy summary report of all prescriptions included in the transmission.

Subj: CMOP Review # 521-737, BIRMINGHAM  [#34227] 11 Dec 97 08:43  9 Lines

From: POSTMASTER                       in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

BIRMINGHAM, AL.     521-737     TRANSMITTED: DEC 11,1996@08:43:29

ORD#     PATIENT          RX#          FILL          DRUG NAME

------------------------------------------------------------------------------

12   CMOPPATIENT3,ONE   15525B         ORIG  ACETAMINOPHEN 325MG TAB

15634A         ORIG  AMINOPHYLLINE 500MG RTL SUPP

15631A         ORIG  AMITRIPTYLINE HCL 75MG TAB

15625A         ORIG  AMOXICILLIN 500MG CAP

11642K         ORIG  ISONIAZID 100MG TAB

6.	The **CMOP Auto-Transmission Schedule** message is generated when the Outpatient Pharmacy personnel use the *Setup Auto-transmission* option on the *Transmission Menu* to set up an automated transmission schedule to the CMOP host facility. **The message notifies the host CMOP personnel that the medical center has set up a schedule for automatic transmissions.** Transmissions will begin automatically on the date and time indicated and continue for the selected frequency until the transmissions are unscheduled or modified. This information is recorded in the CMOP NATIONAL SITE file (#552).

Subj: CMOP Auto-Transmission Schedule, BIRMINGHAM, AL.  [#38881]

11 Dec 96 09:33  7 Lines

From: POSTMASTER (Sender: CMOPPHARMACIST30,THREE)  in 'IN' basket.   Page 1  **NEW**

------------------------------------------------------------------------------

Auto-Transmission Schedule.

Facility                       :  BIRMINGHAM, AL.

Initiating Official            :  CMOPPHARMACIST30,THREE

Begin Automatic Transmissions  :  Dec 11, 1996@09:32

Scheduling Frequency (hours)   :  6

Number of days to transmit thru:  1

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: CMOP Version 2 User Manual (Updated PSX*2*91)

## Consolidated Mail Outpatient Pharmacy (CMOP) Version 2.0 User Manual

<!-- image -->

## August 2016 (Revised September 2021) Department of Veterans Affairs Office of Information and Technology (OIT)

## Revision History

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists 'All', replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

| Date    | Revised Pages        | Patch Number   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------|----------------------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 09/2021 | Page 52,145,146      | PSX*2*91       | Updated CMOP Not Transmitted Rx List Message to remove reference to ROI. Added 3/4 Days Supply Bypass.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 05/2020 | Page 22, 46          | PSX*2*89       | Updated references to the max days allowed in Non- CS Days to Transmit and CS Days to Transmit fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 06/2016 | Page 51              | PSX*2*79       | Updated Title Page to current OI&T standards Remove reference to DEA Special Handling field for billable status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 01/2016 | Cover Page, 138, 140 | PSX*2.0*77     | Updated date on Cover Page. Replaced CMOP Not Dispensed Rx List bulletin with updated example showing that the CMOP Not Dispensed Rx List bulletin is modified to include the standard symbols denoting additional information used by Outpatient Pharmacy . Prescription numbers for ePharmacy claims are marked with 'e'. Prescription numbers with a first party copay shall be marked with '$'. Replaced CMOP Not Transmitted Rx List bulletin with updated example showing that the CMOP Not Transmitted Rx List Bulletin is modified to show new text providing reasons the prescriptions in the message did not transmit to CMOP, displays the first date of the attempted submission, the number of times the prescription submission has been attempted the first unsuccessful transmit, and the bulletin displays the correct site name of the CMOP transaction in the subject line. REDACTED |
| 11/2014 | Page 17, 17a, 17b    | PSX*2.0*76     | Replaced the example for Drug Enter/Edit with an updated example. REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

| Date    | Revised Pages                                                                                  | Patch Number   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|---------|------------------------------------------------------------------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 11/2013 | Throughout (minor nonsubstantive changes). 18, 20, 20, 34, 35, 28, 29, 30, 51, 129a, 129b, 130 | PSX*2*74       | Electronic Data Interchange (EDI) New Standards and Operating Rules - VHA Provider-side Technical Compliance Requirements TAC-12-03366 Project. Cosmetic changes (standardized fonts). Changed all references from version 6 to version 7 and standardized wording for blank pages (without using change pages). Edited Revision History, p. 47 verbiage. Updated p.50 to add patch-specific functionality. Added 129a, 129b to include conditions under which the prescription will rejected. REDACTED                                      |
| 11/2009 | 137a-b                                                                                         | PSX*2*68       | Alerts for a discontinued CMOP prescription REDACTED                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 07/2009 | i-ii, 50a-50b                                                                                  | PSX*2*65       | ePharmacy Iteration II - Phase 4 project: Updated revision history,¾ days' supply functionality, and host error functionality. REDACTED                                                                                                                                                                                                                                                                                                                                                                                                      |
| 04/2006 | v-viii, 30, 41-42, 46-50, 50a-b, 126, 137                                                      | PSX*2*48       | HIPAA NCPDP Global Project: Updated Table of Contents; Updated 'Functionality for Returning Med to Stock' verbiage; Updated View Prescriptions Example to include ECME Activity and Reject Logs; Updated Print from Suspense options and reflowed text onto following pages; Added Third Party Electronic Claims Submission of CMOP Prescriptions; Added ECME transmission to the Flow Chart for Processing a CMOP Transmission in Appendix D; Added example of an 'e-Pharmacy CMOP Not Transmitted Rx List Message' to Appendix E. REDACTED |
| 10/2003 | 24, 24a                                                                                        | PSX*2*41       | Updated example for scheduling of auto- transmissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 09/2002 | Title Page; i-(ii); 65-66.                                                                     | PSX*2*34       | Updated Title Page and Revision History; modified description of Unreleased Rx's Report to include new sort and print options. Formatting change unrelated to the patch: Header for example of Rejected Messages Report moved to same page as body of report.                                                                                                                                                                                                                                                                                |

| Date    | Revised Pages                         | Patch Number   | Description                                                                                                                                                                                                                                                                      |
|---------|---------------------------------------|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 05/2002 | Title Page; i-viii; (61)-62; 67-(68). | PSX*2*32       | Updated Title page; added Revision History page and renumbered Preface and Table of Contents pages; added new CMOP DRUG Cost Missing report; and amended Facility Activity Report description to add time range. Screen captures on updated pages re-formatted to new standards. |
| 12/1997 |                                       |                | Original Released User Manual.                                                                                                                                                                                                                                                   |

## Preface

Version 2.0 of Consolidated Mail Outpatient Pharmacy (CMOP) software processes and automatically transmits prescription data from a Veterans Affairs Medical Center to a CMOP host facility. The CMOP host facility then mails prescriptions from an integrated and highly automated outpatient prescription dispensing system. This CMOP user manual is intended for pharmacists and pharmacy technicians who are familiar with the functionality of Outpatient Pharmacy Version 7.0.

## REDACTED

This address will take you to the Clinical Products page where you will find a listing of all the clinical software manuals. Click on the Consolidated Mail Outpatient Pharmacy (CMOP) link and it will take you to the CMOP Homepage. You can also get there by going straight to the following address: REDACTED

+ Remember to bookmark this site for future reference.

## Special Instructions for the 'First Time' Computer User

If you are unfamiliar with the CMOP package or other Veterans Health Information Systems and Technology Architecture (VistA) software applications, we recommend that you study the DHCP User's Guide to Computing. This orientation guide is a comprehensive handbook benefiting first time users of any VistA application. The purpose of the introductory material is to help you become familiar with basic computer terms and the components of a computer. It is reproduced and distributed periodically by the Kernel Development Group. To request a copy, contact your local Information Resources Management (IRM) staff.

## Icons

Icons used to highlight key points in this manual are defined as follows:

<!-- image -->

<!-- image -->

Required security keys

Indicates the user should take note of the information.

## PSXCMOPMGR

The CMOP site manager uses the options on this menu to manage the operations necessary for the Consolidated Mail Outpatient Pharmacy. This menu contains the following options:

Activate/Inactivate CMOP Processing Display System Setup Purge Status of CMOP Rx Queue CMOP Drug/Item Management... Reports Menu... Resubmit CMOP Rx Transmission Menu...

## PSXCMOPMGR

The CMOP site manager selects this option to request that the remote medical center be activated or inactivated for CMOP processing of outpatient prescriptions.

When the remote medical center enters a request to activate for CMOP processing, a notification message is sent to the CMOP for the request. The message triggers an ALERT to the CMOP manager at the host facility to take action on the request. If the CMOP takes action to grant the request to activate, the remote entry in the CMOP NATIONAL SITE file (#552) is marked Active. A return confirmation message is sent to the facility to activate the entry and notify the requester that the system has been activated and CMOP processing may begin. If the CMOP takes action to deny the request, a return notification message advises the requester of the action to deny.

## Example: Activate/Inactivate CMOP Processing

## [This is the remote.]

```
Select CMOP Site Manager Menu Option: A ctivate/Inactivate CMOP Processing ************************************************************** WARNING:  There are Rx's currently suspended for CMOP. If you inactivate CMOP processing: 1)  These Rx's will not transmit to the CMOP, but will remain in the RX SUSPENSE file.  These Rx's cannot be accessed by Outpatient Pharmacy options.  Ideally, these Rx's should be transmitted or printed before inactivation takes place. If CMOP processing is activated, these prescriptions can be transmitted. 2)  Before inactivating, please have all pharmacy users sign off until inactivation is complete.  CMOP Rx's input by users who do not sign off the system will be suspended for CMOP transmission. (See #1) 3)  Your current auto transmission schedule will be cancelled on inactivation.
```

```
************************************************************** REGION 1 CMOP is the current active CMOP system. Do you want to Inactivate the REGION 1 CMOP system? NO// Y ES Are you sure? NO// Y ES The REGION 1 CMOP system has been inactivated. Activate another system? NO// <RET> Select CMOP Site Manager Menu Option: <RET>
```

## [This is the host.]

```
Enter  "VA   VIEW ALERTS     to review alerts Select CMOP Site Manager Menu Option: VIE w Alerts 1.I  BIRMINGHAM, AL.has inactivated CMOP processing. Select from 1 to 1 or enter ?, A, I, P, M, R, or ^ to exit: ?? YOU MAY ENTER: A number in the range 1 to 1 to select specific alert(s) for processing. A to process all of the pending alerts in the order shown. I to process all of the INFORMATION ONLY alerts, if any, without further ado. P to print a copy of the pending alerts on a printer M to receive a MailMan message containing a copy of these pending alerts R to Redisplay the available alerts ^ to exit Select from 1 to 1 or enter ?, A, I, P, M, R, or ^ to exit: A Processed Alert Number 1 BIRMINGHAM, AL.has inactivated CMOP processing.
```

## [This is the remote.]

```
Select CMOP Site Manager Menu Option: A ctivate/Inactivate CMOP Processing Enter CMOP System: REGION 1 CMOP INACTIVE Enter mailman domain: XXXX-XXXX.XXX.XX.XXX// <RET> CMOP SYSTEM STATUS REGION 1 CMOP  (INACTIVE)     No current transmission CMOP Domain                 : BAB.ISC-BIRM.XX.XXX Last Batch Transmitted      : 167 CMOP RX Queue purged        : JUN 3,1996@13:41:16 Auto Transmission setup     : NO Are you sure you want to activate the REGION 1 CMOP system? NO// Y ES Request to activate sent to REGION 1 CMOP.
```

## [This is the host.]

```
Select CMOP Site Manager Menu Option: VIE w Alerts 1.   BIRMINGHAM, AL. has submitted a request to activate CMOP processing. Select from 1 to 1 or enter ?, A, I, P, M, R, or ^ to exit: A
```

```
Select one of the following: A         APPROVED D         DISAPPROVED BIRMINGHAM, AL. has submitted a request to activate CMOP processing. Select: A PPROVED
```

## [This is the remote.]

```
Select CMOP Site Manager Menu Option: VIE w Alerts 1.I  Permission to transmit to REGION 1 CMOP has been received. Select from 1 to 1 or enter ?, A, I, P, M, R, or ^ to exit: A Processed Alert Number 1 Permission to transmit to REGION 1 CMOP has been received. Select CMOP Site Manager Menu Option: <RET>
```

## Loop CMOP Match to Local Drug File

## PSNMGR

<!-- image -->

With this option users select entries in the local DRUG file (#50), review NATIONAL DRUG file (NDF) (#50.6) matches, and mark entries to transmit to the CMOP.

## Example: Loop CMOP Match to Local Drug File

```
Select CMOP Site Manager Menu Option: CMOP D rug/Item Management Select CMOP Drug/Item Management Option: L oop CMOP Match to Local Drug File This option allows you to choose entries from your drug file and helps you review your NDF matches and mark individual entries to send to CMOP. If you mark the entry to transmit to CMOP, it will replace your Dispense Unit with the VA Dispense Unit. In addition, you may overwrite the local drug name with the VA Print Name and the entry will remain uneditable. Do you wish to loop through the whole file? (If you answer "NO", you will loop through ONLY the ones previously marked as "Do not transmit to CMOP"). Enter Yes or No: N O I have to build a table before you can begin "looping" so let me put you on "hold" for a moment. ............................................................... VA Print Name: GUAIFENESIN 100MG/5ML SYRUP         VA Dispense Unit: ML Local Drug Generic Name: GUAIFENESIN 100MG/5ML LIQUID VA Drug Class: RE302 ORDER UNIT: 120ML DISPENSE UNITS/ORDER UNITS: 120 DISPENSE UNIT: MG/ML PRICE PER DISPENSE UNIT: 0.01 ** This entry has been previously marked NOT to transmit to CMOP ** Do you wish to mark this drug to transmit to CMOP? Enter Yes or No: Y ES Your old Dispense Unit  MG/ML  does not match the new one  ML. You may wish to edit the Price Per Order Unit and/or the Dispense Units Per Order Unit. PRICE PER ORDER UNIT: 0.01// <RET> DISPENSE UNITS PER ORDER: 120// <RET> Do you wish to overwrite your local name? Enter Yes or No: Y ES
```

<!-- image -->

```
VA Print Name: GUAIFENESIN 100MG/5ML SYRUP Local Drug Name                            CMOP?    VA D.U.        O.W.? ------------------------------------------------------------------------------1. GUAIFENESIN 100MG/5ML SYRUP               YES      ML             YES Price Per Order Unit = 0.01 Dispense Units Per Order Unit = 120 If you answer "Yes" you will go to the next VA Print Name. If you answer "No" you will go back through this particular VA Print Name group. Are you sure everything is correct? Enter Yes or No: Y ES You've completed marking everything that is possible.
```

## CMOP Mark/Unmark (Single drug)

## PSNMGR

The user can mark or unmark a single drug for transmission to the CMOP with this option.

If a drug marked for CMOP in the DRUG file (#50) needs to be edited, the entry must be unmarked for CMOP using the CMOP Mark/Unmark (Single drug) option. Once editing is completed, the drug must be re-marked for CMOP using the CMOP Mark/Unmark (Single drug) option.

## ***IMPORTANT***

When using the option CMOP Mark/Unmark (Single drug) to mark a drug for CMOP the user must update the cost information in the DRUG file (#50) to ensure the cost data for the refill will be correct.

## Example 1: Marking a CMOP Drug (Single drug)

```
Select CMOP Site Manager Menu Option: CMOP D rug/Item Management Select CMOP Drug/Item Management Option: CMOP M ark/Unmark (Single drug) This option allows you to choose entries from your drug file and helps you review your NDF matches and mark individual entries to send to CMOP. If you mark the entry to transmit to CMOP, it will replace your Dispense Unit with the VA Dispense Unit. In addition, you may overwrite the local drug name with the VA Print Name and the entry will remain uneditable. Select DRUG GENERIC NAME: GUAIFENESIN 100MG/5ML LIQUID RE302 Local Drug Generic Name: GUAIFENESIN 100MG/5ML LIQUID ORDER UNIT: 120ML DISPENSE UNITS/ORDER UNITS: 120 DISPENSE UNIT: EA PRICE PER DISPENSE UNIT: 0.01 VA Print Name: GUAIFENESIN 100MG/5ML SYRUP       VA Dispense Unit: ML VA Drug Class: CN103 Do you wish to mark this drug to transmit to CMOP? Enter Yes or No: Y ES QUANTITY DISPENSE MESSAGE: ENTER IN MULTIPLES OF 120.
```

```
Your old Dispense Unit  EA  does not match the new one  ML. You may wish to edit the Price Per Order Unit and/or The Dispense Units Per Order Unit. PRICE PER ORDER UNIT: 3.70// 1.20 DISPENSE UNITS PER ORDER UNIT: 1// 120 Do you wish to overwrite your local name? Enter Yes or No: Y ES Select DRUG GENERIC NAME: <RET>
```

## Example 2: Unmarking a CMOP Drug (Single drug)

```
Select CMOP Site Manager Menu Option: CMOP D rug/Item Management Select CMOP Drug/Item Management Option: CMOP M ark/Unmark (Single drug) This option allows you to choose entries from your drug file and helps you review your NDF matches and mark individual entries to send to CMOP. If you mark the entry to transmit to CMOP, it will replace your Dispense Unit with the VA Dispense Unit. In addition, you may overwrite the local drug name with the VA Print Name and the entry will remain uneditable. Select DRUG GENERIC NAME: GUAIFENESIN 100MG/5ML SYRUP RE302 Local Drug Generic Name: GUAIFENESIN 100MG/5ML SYRUP ORDER UNIT: 120ML DISPENSE UNITS/ORDER UNITS: 120 DISPENSE UNIT: ML PRICE PER DISPENSE UNIT: 0.01 VA Print Name: GUAIFENESIN 100MG/5ML SYRUP            VA Dispense Unit: ML VA Drug Class: CN103 Do you wish to UNmark this drug to transmit to CMOP? Enter Yes or No: Y ES Select DRUG GENERIC NAME: <RET>
```

## CMOP Data from Your Local Drug File

The user prints a report of data in the local DRUG file (#50) marked to transmit to the CMOP using this option. The report groups drugs together that are matched to the same VA Print Name along with the VA Dispense Unit. This report must be sent to a printer.

## Example: CMOP Data from Your Local Drug File

```
Select CMOP Site Manager Menu Option: CMOP D rug/Item Management Select CMOP Drug/Item Management Option: CMOP D ata from Your Local Drug File This option will produce a report to help you review your NDF matches. The report will group drugs together that are matched to the same VA Print Name along with the VA Dispense Unit. These will be used for CMOP purposes. You may queue the report to print, if you wish. DEVICE: [Select print device.] [This report must be sent to a printer.] report follows LOCAL DRUGS MATCHED TO THE SAME VA PRINT NAME Date printed: SEP 15,1996 Page: 1 VA PRINT NAME                                          VA DISPENSE UNIT Local GENERIC NAME                                    Local DISPENSE UNIT ------------------------------------------------------------------------------ACETAMINOPHEN 650MG RTL SUPP                           EA ACETAMINOPHEN 650MG RTL SUPP                          EA ACETAZOLAMIDE 125MG TAB                                TAB ACETAZOLAMIDE 125MG TAB                               TAB ACETAZOLAMIDE 250MG TAB                                TAB ACETAZOLAMIDE 250MG TAB                               TAB
```

<!-- image -->

[This report has been abbreviated to save space.]

<!-- image -->

## Drug Enter/Edit

## PSXCMOPMGR

With this option the user adds new drugs to the file, edits existing drugs, and inactivates drugs. When an entry in DRUG file (#50) is marked for CMOP, the GENERIC NAME and DISPENSE UNIT fields cannot be edited. If editing of these fields is necessary, the entry must be unmarked for CMOP using the CMOP Mark/Unmark (Single drug) option. Once editing is completed, the drug must be re-marked for CMOP using the CMOP Mark/Unmark (Single drug) option.

## Example: Drug Enter/Edit

```
Select OPTION NAME: PSS DRUG ENTER/EDIT       Drug Enter/Edit Drug Enter/Edit Select DRUG GENERIC NAME: AMOXAPIN Lookup: GENERIC NAME 1   AMOXAPINE 100MG TAB           CN601 2   AMOXAPINE 25MG TAB           CN601 3   AMOXAPINE 50MG TAB           CN601 CHOOSE 1-3: 1  AMOXAPINE 100MG TAB         CN601 ****************************************************************************** This entry is marked for the following PHARMACY packages: Outpatient Unit Dose Non-VA Med GENERIC NAME: AMOXAPINE 100MG TAB// <RET> VA CLASSIFICATION: CN601// <RET> DEA, SPECIAL HDLG: 6P// <RET> DAW CODE: <RET> NATIONAL FORMULARY INDICATOR: NO LOCAL NON-FORMULARY: N/F// <RET> VISN NON-FORMULARY: V-N/F// <RET> Select DRUG TEXT ENTRY: <RET> Select FORMULARY ALTERNATIVE: NORTRIPTYLINE HCL 25MG CAP // <RET> Select SYNONYM: 4037// <RET> SYNONYM: 4037// <RET> INTENDED USE: QUICK CODE// <RET> NDC CODE: <RET> Select SYNONYM: <RET> MESSAGE: NATL N/F (IEN)// <RET> RESTRICTION: <RET> FSN: <RET> NDC: 52544-0381-01// <RET> INACTIVE DATE: <RET> WARNING LABEL SOURCE is 'NEW'. The following WARNING LABEL may continue to be used for a limited time for some external interfaces. WARNING LABEL: 1,9,11,33// <RET> Current Warning labels for AMOXAPINE 100MG TAB
```

```
No warnings from the new data source exist for this drug. Verify that the drug is matched to the National Drug File. Labels will print in the order in which they appear for local and CMOP fills: 1   -MAY CAUSE DROWSINESS- Alcohol may intensify this effect. USE CARE when driving or when operating dangerous machinery. 9       DO NOT TAKE non-prescription drugs without medical advice. 11  Avoid prolonged exposure to SUNLIGHT and finish all this medication unless otherwise directed by prescriber. 33  SEE MEDICATION INFORMATION SHEET FOR DRUG INFO Pharmacy fill card display: DRUG WARNING 1,9,11,33 NEW WARNING LABEL LIST: 1,9,11,33 Would you like to edit this list of warnings? N// <RET> ORDER UNIT: BT// <RET> PRICE PER ORDER UNIT: 68.82// <RET> DISPENSE UNIT: TAB// <RET> DISPENSE UNITS PER ORDER UNIT: 100// <RET> NCPDP DISPENSE UNIT: EACH// <RET> NCPDP QUANTITY MULTIPLIER: 1// <RET> PRICE PER DISPENSE UNIT: 0.688 points to AMOXAPINE 100MG TAB in the National Drug file. This drug has already been matched and classified with the National Drug file. In addition, if the dosage form changes as a result of rematching, you will have to match/rematch to Orderable Item. This drug has also been marked to transmit to CMOP. If you choose to rematch it, the drug will be marked NOT TO TRANSMIT to CMOP. Do you wish to match/rematch to NATIONAL DRUG file? No// <RET> Just a reminder...you are editing AMOXAPINE 100MG TAB. Strength from National Drug File match => 100    MG Strength currently in the Drug File    => 100    MG Strength => 100   Unit => MG POSSIBLE DOSAGES: DISPENSE UNITS PER DOSE: 1         DOSE: 100MG           PACKAGE: IO DISPENSE UNITS PER DOSE: 2         DOSE: 200MG           PACKAGE: IO LOCAL POSSIBLE DOSAGES: Do you want to edit the dosages? N// <RET> ****************************************************************************** This entry is marked for the following PHARMACY packages: Outpatient Unit Dose Non-VA Med MARK THIS DRUG AND EDIT IT FOR: O  - Outpatient C  - Controlled Substances X  - Non-VA Med Enter your choice(s) separated by commas : <RET> ** You are NOW in the ORDERABLE ITEM matching for the dispense drug. ** AMOXAPINE 100MG TAB is already matched to AMOXAPINE TAB Do you want to match to a different Orderable Item? NO// <RET>
```

## Drugs not Flagged for CMOP Transmission

This report generates a list of items in the local DRUG file (#50) which are available at the CMOP, but have not been marked for transmission. This report must be sent to a printer.

## Example: Drugs not Flagged for CMOP Transmission

<!-- image -->

| Select CMOP Site Manager Menu Option: CMOP D rug/Item Management                                                                                                                                                          | Select CMOP Site Manager Menu Option: CMOP D rug/Item Management                                                                                                                                                          | Select CMOP Site Manager Menu Option: CMOP D rug/Item Management                                                                                                                                                          | Select CMOP Site Manager Menu Option: CMOP D rug/Item Management                                                                                                                                                          |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select CMOP Drug/Item Management Option: DRUGS NOT Flagged for CMOP Transmission                                                                                                                                          | Select CMOP Drug/Item Management Option: DRUGS NOT Flagged for CMOP Transmission                                                                                                                                          | Select CMOP Drug/Item Management Option: DRUGS NOT Flagged for CMOP Transmission                                                                                                                                          | Select CMOP Drug/Item Management Option: DRUGS NOT Flagged for CMOP Transmission                                                                                                                                          |
| This report will print all drugs marked for Outpatient use which are non- controlled substances and are not marked to transmit to CMOP. This report requires 132 columns. You may queue the report to print, if you wish. | This report will print all drugs marked for Outpatient use which are non- controlled substances and are not marked to transmit to CMOP. This report requires 132 columns. You may queue the report to print, if you wish. | This report will print all drugs marked for Outpatient use which are non- controlled substances and are not marked to transmit to CMOP. This report requires 132 columns. You may queue the report to print, if you wish. | This report will print all drugs marked for Outpatient use which are non- controlled substances and are not marked to transmit to CMOP. This report requires 132 columns. You may queue the report to print, if you wish. |
| DEVICE: [Select print device.] [This report follows                                                                                                                                                                       | report must be sent to a printer.]                                                                                                                                                                                        | report must be sent to a printer.]                                                                                                                                                                                        | report must be sent to a printer.]                                                                                                                                                                                        |
| LOCAL DRUG NAME STATUS VA PRINT NAME ----------------------------------------------------------------------------------                                                                                                   | LOCAL DRUG NAME STATUS VA PRINT NAME ----------------------------------------------------------------------------------                                                                                                   | LOCAL DRUG NAME STATUS VA PRINT NAME ----------------------------------------------------------------------------------                                                                                                   | LOCAL DRUG NAME STATUS VA PRINT NAME ----------------------------------------------------------------------------------                                                                                                   |
| -----------                                                                                                                                                                                                               | -----------                                                                                                                                                                                                               | -----------                                                                                                                                                                                                               | -----------                                                                                                                                                                                                               |
| ALDOCLOR-150 TAB NOT MARKED CHLOROTHIAZIDE 150/METHYLDOPA 250MG TAB                                                                                                                                                       | ALDOCLOR-150 TAB NOT MARKED CHLOROTHIAZIDE 150/METHYLDOPA 250MG TAB                                                                                                                                                       | ALDOCLOR-150 TAB NOT MARKED CHLOROTHIAZIDE 150/METHYLDOPA 250MG TAB                                                                                                                                                       | ALDOCLOR-150 TAB NOT MARKED CHLOROTHIAZIDE 150/METHYLDOPA 250MG TAB                                                                                                                                                       |
| ALDOCLOR-250 TAB NOT MARKED CHLOROTHIAZIDE 250/METHYLDOPA 250MG TAB                                                                                                                                                       | ALDOCLOR-250 TAB NOT MARKED CHLOROTHIAZIDE 250/METHYLDOPA 250MG TAB                                                                                                                                                       | ALDOCLOR-250 TAB NOT MARKED CHLOROTHIAZIDE 250/METHYLDOPA 250MG TAB                                                                                                                                                       | ALDOCLOR-250 TAB NOT MARKED CHLOROTHIAZIDE 250/METHYLDOPA 250MG TAB                                                                                                                                                       |
| ANAMINE SYRUP NOT MARKED CTM 2/PSEUDOEPHEDRINE 30MG/5ML LIQUID                                                                                                                                                            | ANAMINE SYRUP NOT MARKED CTM 2/PSEUDOEPHEDRINE 30MG/5ML LIQUID                                                                                                                                                            | ANAMINE SYRUP NOT MARKED CTM 2/PSEUDOEPHEDRINE 30MG/5ML LIQUID                                                                                                                                                            | ANAMINE SYRUP NOT MARKED CTM 2/PSEUDOEPHEDRINE 30MG/5ML LIQUID                                                                                                                                                            |
| ANTHRALIN 1.0% CR 50GM NOT MARKED ANTHRALIN 1% CREAM                                                                                                                                                                      | ANTHRALIN 1.0% CR 50GM NOT MARKED ANTHRALIN 1% CREAM                                                                                                                                                                      | ANTHRALIN 1.0% CR 50GM NOT MARKED ANTHRALIN 1% CREAM                                                                                                                                                                      | ANTHRALIN 1.0% CR 50GM NOT MARKED ANTHRALIN 1% CREAM                                                                                                                                                                      |
| APRESAZIDE 100/50 CAP NOT MARKED HYDRALAZINE 100/HCTZ 50MG                                                                                                                                                                | APRESAZIDE 100/50 CAP NOT MARKED HYDRALAZINE 100/HCTZ 50MG                                                                                                                                                                | APRESAZIDE 100/50 CAP NOT MARKED HYDRALAZINE 100/HCTZ 50MG                                                                                                                                                                | APRESAZIDE 100/50 CAP NOT MARKED HYDRALAZINE 100/HCTZ 50MG                                                                                                                                                                |
| CAP                                                                                                                                                                                                                       | CAP                                                                                                                                                                                                                       | CAP                                                                                                                                                                                                                       | CAP                                                                                                                                                                                                                       |
| APRESAZIDE 50/50 CAP                                                                                                                                                                                                      | NOT                                                                                                                                                                                                                       | MARKED                                                                                                                                                                                                                    | HYDRALAZINE 50/HCTZ 50MG CAP                                                                                                                                                                                              |
| APRESOLINE-ESIDRIX TAB NOT MARKED HYDRALAZINE 25/HCTZ 15MG TAB                                                                                                                                                            | APRESOLINE-ESIDRIX TAB NOT MARKED HYDRALAZINE 25/HCTZ 15MG TAB                                                                                                                                                            | APRESOLINE-ESIDRIX TAB NOT MARKED HYDRALAZINE 25/HCTZ 15MG TAB                                                                                                                                                            | APRESOLINE-ESIDRIX TAB NOT MARKED HYDRALAZINE 25/HCTZ 15MG TAB                                                                                                                                                            |
| ARISTO-PAK 4MG                                                                                                                                                                                                            | DO                                                                                                                                                                                                                        |                                                                                                                                                                                                                           | 4MG TAB                                                                                                                                                                                                                   |
| TAB NOT SEND TRIAMCINOLONE ARISTOCORT A 0.1% OINT 60GM NOT MARKED TRIAMCINOLONE ACETONIDE                                                                                                                                 | TAB NOT SEND TRIAMCINOLONE ARISTOCORT A 0.1% OINT 60GM NOT MARKED TRIAMCINOLONE ACETONIDE                                                                                                                                 | TAB NOT SEND TRIAMCINOLONE ARISTOCORT A 0.1% OINT 60GM NOT MARKED TRIAMCINOLONE ACETONIDE                                                                                                                                 | TAB NOT SEND TRIAMCINOLONE ARISTOCORT A 0.1% OINT 60GM NOT MARKED TRIAMCINOLONE ACETONIDE                                                                                                                                 |
| OINT                                                                                                                                                                                                                      | OINT                                                                                                                                                                                                                      | OINT                                                                                                                                                                                                                      | OINT                                                                                                                                                                                                                      |
| 0.1%                                                                                                                                                                                                                      | 0.1%                                                                                                                                                                                                                      | 0.1%                                                                                                                                                                                                                      | 0.1%                                                                                                                                                                                                                      |

[This report has been abbreviated to save space.]

## Count of CMOP Suspended Rx's

This option is used to count suspended CMOP Rx's sorted by day. The report contains the suspense date, the number of CMOP Rx's queued, transmitted, printed locally, and the total number of CMOP Rx's in suspense.

## Medical Center Activity Report

This option allows you to print a report of  the totals by transmission the number of orders and Rx's transmitted to the CMOP Host facility and the number of those Rx's that are released, not dispensed and unreleased.

## Rx Workload Report

This report provides daily totals for a selected date range listing prescriptions entered with a mail and window routing, mail and window prescriptions released by Outpatient, and prescriptions released by CMOP. The OTHER column totals all other prescriptions, i.e., cancelled, deleted, etc.

## Turnaround Time Report

This option prints the CMOP Rx Turnaround Time report for the selected date range. The report is based on the time difference between the  transmission date/time and the date/time the pharmacist at the CMOP marked the prescription as completed/released. Information includes the average, minimum, and maximum turnaround times, and the total number of Rx's released. This report must be queued to a printer.

## PSXRESUB

The resubmit option allows designated Outpatient Pharmacy users to send Rx's back to the CMOP that were returned as Not Dispensed, but have no apparent problems. Ordinarily, Rx's that have problems will be corrected through the edit option and re-suspended to be sent back to the CMOP. If the Rx has no apparent problem, and the user has communicated with the Host CMOP, then this option can be used to send the Rx back. The Rx can only be resubmitted once. After one resubmission, the Rx must be printed locally.

You may not resubmit if the following conditions exist.

1. The NOT DISPENSED fill is a Duplicate Fill.
2. The fill does not have a CMOP status of NOT DISPENSED.
3. The fill has already been resubmitted.
4. The NOT DISPENSED fill is not the last fill in the Rx.

## Example:

```
Select OPTION NAME: CMOP SITE Manager Menu Select CMOP Site Manager Menu Option: RES ubmit CMOP Rx CMOP Prescription Resubmission Utility Enter the Rx # to resubmit: 15666 You have chosen Rx # 15666 to be resubmitted to the CMOP. Do you want to continue? :  (Y/N): NO// Y ES RX# 15666  SUSPENDED FOR CMOP TRANSMISSION  02-18-97. Enter the Rx # to resubmit: <RET> Select CMOP Site Manager Menu Option: <RET>
```

## PSX XMIT

The user controls batch transmission operations with this submenu.

Comment Enter/Edit Re-transmit CMOP Data Setup Auto-transmission View Transmission

## Comment Enter/Edit

The user selects this option to make notes or comments regarding a specific transmission. The batch number is entered, the batch information is displayed, and the user is prompted for comments. Batch information includes the division, CMOP, batch number, sender, transmission and received date/time, beginning and ending order numbers, and the total orders and Rx's.

## Re-transmit CMOP Data

## PSXRTRAN

Users of this option must hold the PSX XMIT, PSXCMOPMGR, and the PSXRTRAN keys to retransmit data previously transmitted to the CMOP. At the 'Select CMOP TRANSMISSION' prompt the user enters the transmission number that needs to be re-transmitted. Previous transmission summary data is then displayed for the user's review. The user is then asked 'Are you sure you want to Re-transmit this batch?'

## Setup Auto-transmission

## PSXAUTOX

This option allows holders of the security key, PSXAUTOX, to schedule or unschedule the CMOP transmission process to run automatically in the background on a scheduled basis.

The user enters data to schedule a recurring transmission. At the selected time, the job runs in the background. Data queued for CMOP transmission in the RX SUSPENSE file (#52.5) are transmitted. If no data are found, the job is rescheduled to run using the frequency information from the CMOP SYSTEM file (#550).

This option has been modified to include a system parameter, NUMBER OF DAYS TO TRANSMIT. This parameter indicates the number of days to transmit thru for an automatic data transmission. If this field is null or contains a zero the auto transmissions will select data through today as the default. If the field contains a number, n, from 1 to 15, transmission data will be selected for T+n days. The maximum NUMBER OF DAYS TO TRANSMIT is fifteen(15)

<!-- image -->

> **NOTE:** the CMOP system parameter for non-controlled substance auto-transmissions, NUMBER OF DAYS TO TRANSMIT is different from the Outpatient site parameter, DAYS TO PULL FROM SUSPENSE. For example, if the NUMBER OF DAYS TO TRANSMIT is two (2) and the DAYS TO PULL FROM SUSPENSE is seven (7) the initial transmission data will be selected for T+2 days. Once selected, for every patient with an Rx in this date range, the software

<!-- image -->

<!-- image -->

will then look ahead in RX SUSPENSE file (#52.5) for any Rxs for these patients for an additional seven days (T+2+7days). If the patients have Rx's for this date range, they will be added to the data transmission.

<!-- image -->

> **NOTE:** Controlled Substance CMOP auto-transmissions also use two parameters, the CS DAYS TO TRANSMIT from the CMOP SYSTEM file (#550) and the DAYS TO PULL SUSPENSE CMOP CS field (#3.1) from the OUTPATIENT SITE file (#59). The CS DAYS TO TRANSMIT is used for the initial search for suspended CS prescriptions to include. For example, if the CS DAYS TO TRANSMIT is three(3) days and the DAYS TO PULL SUSPENSE CMOP CS is two(2) days the transmission data will be selected for T+3 days. If a patient has at least one CS prescription in the date range, any other CS prescriptions for the patient that are in suspense for an additional 2 days (T+3+2) will also be transmitted.

When an automatic transmission is modified, ensure your site contacts your CMOP liaison prior to changing any transmission times. Only one automatic transmission at a time is allowed; the CS and non-CS transmissions are scheduled at different times to allow one to finish before the next one starts.

When an automatic transmission schedule is cancelled any queued transmissions will run to completion. No further automatic transmissions will be scheduled.

<!-- image -->

+ Each division with data to transmit creates a transmission and all usual mail messages are sent. If two divisions have data to transmit, two independent transmissions are created, etc.

................................................................example follows on the next page ............................................................

## Example: Setup Auto-transmission

```
Select Transmission Menu Option: S etup Auto-transmission CS Transmission               Non-CS Transmission Scheduled to Run Frequency (hrs) Thru days Tasking ID Select one of the following: C         Controlled Substance N         NON-Controlled Substance Edit     CS <C>  or  NON-CS <N> : C = = = = = QUEUED TO RUN AT WHAT TIME: AUG 19,2002@23:00 DEVICE FOR QUEUED JOB OUTPUT: <RET> QUEUED TO RUN ON VOLUME SET: <RET> RESCHEDULING FREQUENCY: 24H TASK PARAMETERS: <RET> SPECIAL QUEUEING: <RET> CS DAYS TO TRANSMIT: 5// <RET> = = = = =
```

```
CS Transmission               Non-CS Transmission Scheduled to Run         AUG 19,2002@23:00 Frequency (hrs)          24H Thru days                5 Tasking ID               1117268 Select one of the following: C         Controlled Substance N         NON-Controlled Substance Edit     CS <C>  or  NON-CS <N> : N = = = = = Edit Option Schedule Option Name: PSXR SCHEDULED NON-CS TRANS Menu Text: Scheduled Non-CS Transmission             TASK ID: QUEUED TO RUN AT WHAT TIME: AUG 19,2002@21:00 DEVICE FOR QUEUED JOB OUTPUT: <RET> QUEUED TO RUN ON VOLUME SET: <RET> RESCHEDULING FREQUENCY: 24H TASK PARAMETERS: <RET> SPECIAL QUEUEING: <RET> NON-CS DAYS TO TRANSMIT: 8// <RET> = = = = = CS Transmission               Non-CS Transmission Scheduled to Run         AUG 19,2002@23:00             AUG 19,2002@21:00 Frequency (hrs)          24H                           24H Thru days                5                             8 Tasking ID               1117268                       1117269 Select one of the following: C         Controlled Substance N         NON-Controlled Substance Edit     CS <C>  or  NON-CS <N> : <RET> NON-CS New Schedule Sent to CMOP CS New Schedule Sent to CMOP Select Transmission Menu Option: <RET>
```

## Outpatient Pharmacy Manager

The Outpatient Pharmacy Manager menu [PSO MANAGER] should be assigned to supervisors, package coordinators, and members of the Automated Data Processing/Information Resources Management (ADP/IRM) staff.

The Outpatient Pharmacy package provides a method for managing the medications given to veterans who have visited a clinic or who have received prescriptions upon discharge from the hospital. Prescription labels are automatically generated and refill request forms are printed. Medication histories are kept on-line to permit checks for potential interactions. Profiles can be generated to assist the clinician in managing the patient's medication regimen. Management reports aid the pharmacy in controlling inventory and costs.

A number of site parameters allow the individual Department of Veterans Affairs Medical Center (VAMC) to customize the package to meet local needs.

The following menu contains the options for the outpatient pharmacy manager.

*†

```
Archiving ... Autocancel Rx's on Admission Bingo Board ... Clozapine Pharmacy Manager ... Copay Menu ... Drug Enter/Edit Drug Interactions Menu ... DUE Supervisor ... Label/Profile Monitor Reprint * Maintenance (Outpatient Pharmacy) ... Medication Profile * Output Reports ... Pharmacy Intervention Menu ... * Release Medication * Return Medication to Stock * Rx (Prescriptions) ... * Supervisor Functions ... * Suspense Functions ... * Update Patient Record Verification ...
```

* These options from the Outpatient Pharmacy V. 7.0 package have been modified or contain suboptions which have been modified for CMOP.

This option has been modified for CMOP and can be found on the Outpatient Pharmacy Manager menu, the Maintenance (Outpatient Pharmacy) menu, and the Supervisor Functions menu of Outpatient Pharmacy V. 7.0.

## Drug Enter/Edit

By using the Drug Enter/Edit option the pharmacy supervisor can add new drugs to the file, edit existing drugs, and inactivate drugs. This option can be found on the Outpatient Pharmacy Manager menu, the Maintenance (Outpatient Pharmacy) menu, and the Supervisor Functions menu of Outpatient Pharmacy V. 7.0.

## CMOP Functionality for the Drug Enter/Edit Option

When an entry in the DRUG file (#50) has been marked for CMOP, the GENERIC NAME and DISPENSE UNIT fields cannot be edited. If editing of these fields is necessary, the entry must be unmarked for CMOP using the CMOP Mark/Unmark (Single drug) option. Once editing is completed, the drug must be re-marked for CMOP using the CMOP Mark / Unmark (Single drug) option.

The QUANTITY DISPENSE MESSAGE field does not display in the Outpatient Pharmacy Drug Enter/Edit option. It is recommended that the user enter or edit drugs through the CMOP Drug/Item Management menu.

## Output Reports

The Output Reports menu generates a variety of management reports. These reports contain current medication profiles, utilization, cost, and workload information which help management maintain the highest level of patient care.

Action Profile  (132 COLUMN PRINTOUT) Alpha Drug List and Synonyms AMIS Report Commonly Dispensed Drugs Cost Analysis Reports ... Daily AMIS Report Drug List By Synonym Inactive Drug List Management Reports Menu ... Monthly Drug Cost Narcotic Prescription List Non-Formulary List Poly Pharmacy Report

* Released and Unreleased Prescription Report

* This option from Outpatient Pharmacy V. 7.0 has been modified for CMOP.

## Released and Unreleased Prescription Report

This option generates a report of released and unreleased or only unreleased prescriptions by date range. The default start date is T-30. If the package was installed less than 30 days ago, the default date will be the date the package was installed. The end date default will be the current date.

## CMOP Functionality for Released and Unreleased Prescription Report

This option has been modified by adding a column to indicate if the prescription is a CMOP prescription and a column to indicate the CMOP status.

## *** Information ***

There exists a possibility that a patient can lose credit for a fill/refill. If a fill/refill is released and then returned to stock, the fill/refill cannot be re-released. The fill/refill is lost and is charged against the total number of fill/refills for this prescription.

## CMOP Functionality for Release Medication

A CMOP Rx originally suspended for transmission to the CMOP may be released using this option, if and only if, it has been printed locally. CMOP Rx's marked Queued for Transmission, Loading for Transmission, or Transmission Completed may not be released using this option. Transmitted Rx's are automatically released by a background process once dispense information is returned from the host facility. Inventory is not decreased for CMOP dispensed prescriptions.

## Returning Medication to Stock

The Return to Stock option functionality is used when a prescription has been released, but has been refused, not picked up, or not given to the patient for some reason. Comments can be entered to explain why the medication was returned to stock.

A prescription can only be returned to stock if the prescription status is Active, Cancelled, Expired, or Released. If the prescription is not released, there is no need to return it to stock. This function increases the inventory so that a more current inventory level is maintained by the Outpatient Pharmacy package.

This option also removes a copay charge if it is applicable to the prescription. It is highly recommended that you use this option.

## *** Information ***

There exists a possibility that a patient can lose credit for a fill/refill. If a fill/refill is released and then returned to stock, the fill/refill cannot be re-released. The fill/refill is lost and is charged against the total number of fill/refills for this prescription.

## CMOP Functionality for Return Medication to Stock

Prescriptions dispensed by the CMOP can be returned to stock at the medical center.

## Barcode Rx Menu

This Barcode Rx Menu contains options that allow batch barcoding for refills and renewals of prescriptions and an option to check the quality of the barcode print.

* Barcode Batch Prescription Entry Check Quality of Barcode

* This option has been modified for CMOP and can be found under the Barcode Rx Menu on the Rx (Prescriptions) menu of Outpatient Pharmacy V. 7.0.

## Barcode Batch Prescription Entry

This option is used to enter refills or renewals using barcodes in a batch entry.

## CMOP Functionality for Barcode Batch Prescription Entry

Prescriptions entered using this option will be screened and suspended for CMOP transmission if all the CMOP criteria are met.

## Cancel Prescriptions

The Cancel Prescription option allows the pharmacist to either discontinue a prescription without deleting its records from the files, or reinstate a cancelled prescription. A cancelled prescription remains on the patient profile and an entry in the activity log for the cancellation is made. The cancelled prescription will carry a status of Cancelled or C and cannot be refilled or reprinted.

The label can be entered or wanded if you are cancelling or reinstating the prescription by the prescription number or the patient name.

## CMOP Functionality for Cancel Prescription

CMOP functionality for Cancel Prescription is the same as Outpatient Pharmacy V. 7.0. for all Rx's. Reinstate screens all Rx's for the CMOP criteria. If the Rx meets the criteria it is suspended for CMOP transmission and a message is displayed indicating the suspense date. If the fill date of a CMOP Rx is in the past, the prescription is reinstated, but not suspended for transmission. If the fill date is today or in the future, the CMOP Rx is suspended for CMOP processing for that date.

## Edit Prescriptions

The pharmacy manager and pharmacist use the Edit Prescriptions option to edit information for a specific prescription. This option prints a label only if the prescription being edited has an Active status.

Copay will update the current copayment charge for a prescription, if and only if, an edit of the DAYS SUPPLY field changes the number of units charged. The updating procedure takes place in the background with no additional input required by the user. For example, a copayment charge unit is 30 days and the charge is $2.00. If a prescription was filled for 31 days, the charge would be $4.00. If the prescription was filled for 60 days, the charge would still be $4.00. Editing the PATIENT STATUS field does not update or change copayment status or charges for the prescription.

## CMOP Functionality for Edit Prescriptions

Currently CMOP prescriptions may not be edited during the transmission process. The following criteria are required for editing of CMOP prescriptions.

DRUG NAME - CMOP to NON-CMOP and vice versa.

- Edit - If the Rx has ever been transmitted (loading/transmitted) to the CMOP No Edit.
- If the Rx has never been released - Allow Edit.

MAIL/WINDOW - Currently able to be edited at each fill level.

- If the original is in suspense, 'Queued for Transmission' for CMOP, and is edited from MAIL to WINDOW, the Rx is not transmitted. It is handled as any Outpatient Pharmacy Rx.
- No editing is allowed if the Rx is loading or transmitting to the CMOP.
- Editing a CMOP window Rx (not on suspense) to mail does not send the Rx to the CMOP.
- A window CMOP Rx on suspense edited to mail is 'Queued for Transmission' to the CMOP.

+

- If editing a refill which is the most current fill then the same rules apply. Edits of past fills do not affect CMOP.

TRADENAME - Currently able to be edited at each fill level.

- A CMOP Rx entered with a tradename will not be sent to CMOP:

If deleting a tradename and the last fill is in suspense, change the entry to 'Queued for Transmission' to the CMOP.

View Prescriptions will look odd, but the CMOP group stated this was acceptable.

## CRITERIA FOR EDITING OTHER FIELDS -

- If Rx released, no editing of

ISSUE DATE

FILL DATE

- If fill being edited has been transmitted, no editing of

QUANTITY

DAYS SUPPLY

## Hold Features

The Hold Features menu contains the options listed below for the hold features. When using this menu the user can place a prescription on hold, generate a list of prescriptions on hold, or remove a prescription from hold.

* Hold Rx List Prescriptions on Hold
* Unhold Rx

* These options have been modified for CMOP and can be found on the Rx (Prescriptions) menu of Outpatient Pharmacy V. 7.0.

## Hold Rx

This function allows the pharmacist to place a prescription on hold.

## CMOP Functionality for Hold Rx

CMOP Rx's cannot be placed on hold during CMOP transmission.

## Unhold Rx

This suboption allows the pharmacist to move a prescription from a Hold status and place it in an Active status.

## CMOP Functionality for Unhold Rx

The Unhold Rx option screens the Rx for CMOP criteria. If the criteria are met, the Rx is suspended for transmission to the CMOP and a message is displayed indicating the suspense date. The screening for CMOP is performed after the 'MAIL/WINDOW' prompt and response.

## New Prescription Entry

The New Prescription Entry option allows the user to enter new prescriptions or renew existing prescriptions.

## CMOP Functionality for New Prescription Entry

On prescription order entry, CMOP drug/items marked as 'MAIL' are automatically placed on suspense and flagged for transmission to the CMOP host facility. CMOP drug/items marked as 'WINDOW' are not automatically suspended or flagged for transmission, but are processed in the usual manner for windows. All screens, system/site parameter checks, etc., are performed in the background, therefore, transparent to the user.

If the fill date entered is today, on completion of Rx order entry for a patient, the normal prompt, 'LABEL: QUEUE/HOLD/SUSPEND or ^ to bypass', is presented.

After the user's response, a message is displayed listing CMOP Rx's which have been suspended for CMOP transmission.

If the fill date is in the future, the queue/hold/suspend/bypass prompt is not displayed. Only the CMOP transmission is displayed.

## Example: New Prescription Entry

```
Select Outpatient Pharmacy Manager Option: RX (Prescriptions) Select Rx (Prescriptions) Option: N ew Prescription Entry Select PATIENT NAME: CMOPPATIENT3,ONE 02-23-74     000579013 MAS ELIGIBILITY: OTHER FEDERAL AGENCY WEIGHT(Kg):                              HEIGHT(cm): DISABILITIES: 123 OAK STREET PLANO  TEXAS  75024 DATE OF BIRTH: FEB 23,1974// <RET> STREET ADDRESS [LINE 1]: 123 OAK STREET// <RET> STREET ADDRESS [LINE 2]: <RET> STREET ADDRESS [LINE 3]: <RET> CITY: PLANO// <RET> STATE: TEXAS// <RET> ZIP+4: 75024// <RET> PHONE NUMBER [RESIDENCE]: 5555555555// <RET> CNH CURRENT: <RET> FEE HOSPITAL I.D.: <RET> TEMPORARY ADDRESS ACTIVE?: NO// <RET> REMARKS: <RET> #    RX #    DRUG                          STAT QTY ISS-DT LST-FL REF-RM DAYS
```

## Renew

On renew, the data from the original Rx is passed to the renewed Rx. Once renewed, the 'Edit renewed Rx? ' prompt is displayed. Mail/window must be reviewed for each Rx renewed. The ' MAIL/WINDOW' prompt appears after the first 'FILL DATE' prompt.

## Example: Renew a Prescription

```
Select Outpatient Pharmacy Manager Option: RX (Prescriptions) Select Rx (Prescriptions) Option: N ew Prescription Entry Select PATIENT NAME: CMOPPATIENT3,ONE 02-23-74     000579013 ELIGIBILITY: AID & ATTENDANCE WEIGHT(Kg):                              HEIGHT(cm): DISABILITIES: 123 OAK STREET ANYTOWN  TEXAS  75024 DATE OF BIRTH: FEB 23,1974// <RET> STREET ADDRESS [LINE 1]: 123 OAK STREET// <RET>
```

<!-- image -->

```
STREET ADDRESS [LINE 2]: <RET> STREET ADDRESS [LINE 3]: <RET> CITY: PLANO// <RET> STATE: TEXAS// <RET> ZIP+4: 75024// <RET> PHONE NUMBER [RESIDENCE]: 5555555555// <RET> CNH CURRENT: <RET> FEE HOSPITAL I.D.: <RET> TEMPORARY ADDRESS ACTIVE?: NO// <RET> REMARKS: <RET>
```

```

## Partial Prescription

By using this option the pharmacist can partially refill a prescription without eliminating one of the refills allowed by the original prescription.

## CMOP Functionality for Partial Prescription

A partial fill entered for a CMOP prescription cannot be suspended. If a prescription is suspended for transmission to CMOP, the user can pull the prescription or enter a partial and print the label.

## Refill Prescriptions

This option allows the pharmacy manager or pharmacist to process refills for existing prescriptions.

Copayment only affects this option in the background. You do not see a prompt relating to copayment for the Refill Prescriptions option. At the time of refilling a prescription, the computer system already knows the copayment eligibility of the veteran. When the prescription was first ordered, veteran eligibility for copayment was determined. If the veteran was charged a copayment for the original prescription, he or she will be charged for the refill.

+ Refill a prescription only after the original label has been printed. If you do not wait until after the original label has been printed you will produce a label for the last fill only.

## CMOP Functionality for Refill Prescriptions

Refilled prescriptions are handled using the same functionality as New Prescription Entry. (See the Rx (Prescriptions) menu.)

## View Prescriptions

With this option the user can view on screen the most complete information available for a specific prescription. The activity log lists the date, reason, prescription reference (Rx Ref), the initiator of the activity, and comments. The label log lists the date, prescription reference (Rx Ref), the person who printed it, and comments. Prescriptions in a Deleted status cannot be viewed.

## CMOP Functionality for View Prescriptions

CMOP information related to this Rx has been added to the information displayed. The CMOP event log lists the date, prescription reference (RX REF), CMOP status, the CMOP, and comments.

## Example: View Prescriptions

<!-- image -->

```
Patient Instructions: SIG: TAKE ONE TABLET BY MOUTH 6 Patient Status: OPT NSC Issue Date: 09/09/05                 Fill Date: 09/10/05 Last Fill Date: 09/10/05 (Mail, Transmitted) Last Release Date:                              Lot #: Expires: 09/10/06                       MFG: Days Supply: 1                            QTY (TAB): 1 # of Refills: 11                       Remaining: 11 Provider: CMOPPROVIDER2,TWO Routing: Mail Copies: 1 Clinic: Not on File Division: KENAI VA CBOC (463GB) Pharmacist: Patient Counseling: NO Remarks: Finished By: CMOPPHARMACIST3,THREE Entry By: CMOPPHARMACIST3,THREE            Entry Date: 09/09/05 08:41:23 Original Fill Released:       Routing: Mail Press RETURN to continue or "^" to exit: <RET> Refill Log: #  Log Date   Refill Date  Qty               Routing  Lot #       Pharmacist =============================================================================== There are NO Refills For this  Prescription Partial Fills: #   Log Date   Date     Qty              Routing    Lot #        Pharmacist =============================================================================== There are NO Partials for this Prescription Activity Log: #   Date        Reason         Rx Ref         Initiator Of Activity =============================================================================== 1   09/09/05    SUSPENSE       ORIGINAL       CMOPPHARMACIST3,THREE Comments: RX Placed on Suspense for CMOP until 09-10-05 2   09/09/05    PROCESSED      ORIGINAL       CMOPPHARMACIST3,THREE Comments: Transmitted to LEAVENWORTH CMOP Press RETURN to continue or "^" to exit: <RET> Copay Activity Log: #   Date        Reason               Rx Ref         Initiator Of Activity =============================================================================== There's NO Copay activity to report Label Log: #   Date        Rx Ref                    Printed By =============================================================================== There are NO Labels printed. ECME Log: #   Date        Rx       Ref         Initiator Of Activity =============================================================================== 1   09/09/05@16:22:04    ORIGINAL       CMOPPHARMACIST3,THREE Comments: Submitted to ECME: CMOP TRANSMISSION (NDC: 20233-0344-33) ECME REJECT Log #   Date/Time         Rx Ref    Reject                       STATUS =============================================================================== 1   9/09/05@16:24:14  ORIGINAL  DRUG UTILIZATION REVIEW      UNRESOLVED CMOP Event Log: Date/Time             Rx Ref  TRN-Order       Stat             Comments =============================================================================== 09/09/05@0944         Orig    2686-1            TRAN Press RETURN to continue or "^" to exit: <RET> VIEW PRESCRIPTION: <RET> Select Rx (Prescriptions) Option: <RET>
```

## Supervisor Functions

The Supervisor Functions menu contains seventeen options that the package coordinator uses for implementation as well as maintenance of the various files for the basic running of the Outpatient Pharmacy software.

Add New Providers Daily Cost Compilation

* Delete a Prescription
* Drug Enter/Edit Drug/Drug Interaction Functions... Edit Provider Initialize Cost Statistics Inter-Divisional Processing Inventory Menu Lookup Clerk by Code Mark/Unmark Lab Monitor Drugs Medication Instruction File Add/Edit Monthly Cost Compilation Pharmacist Enter/Edit Recompile AMIS Data Site Parameter Enter/Edit View Provider
* These options from the Outpatient Pharmacy V. 7.0 Supervisor Functions menu have been modified for CMOP.

An example of this option can be found under the CMOP Drug/Item Management menu and the Outpatient Pharmacy Manager menu in this manual. This option has been modified for CMOP and can be found on the Outpatient Pharmacy Manager menu, the Maintenance (Outpatient Pharmacy) menu, and the Supervisor Functions menu of Outpatient Pharmacy V. 7.0.

## Delete a Prescription

The pharmacy manager uses this option to change a prescription status to Deleted. Deleted prescriptions do not appear on any profiles.

+ In Outpatient Pharmacy V. 7.0 a released prescription can only be deleted after it has been returned to stock.

## CMOP Functionality for Delete a Prescription

A CMOP prescription cannot be deleted if the status is Transmitted or Dispensed.

## Change Suspense Date

This option allows the pharmacist to change the suspense date for a specific prescription. The new suspense date becomes the fill/refill date automatically. With this option the pharmacist is also able to delete a specific prescription from suspense.

## CMOP Functionality for Change Suspense Date

For CMOP prescriptions, suspense dates are changed, the Rx is 'unmarked' for transmission for the original date, and then 'marked' for transmission for the new suspense date. The user is not notified that the suspense date change was for a CMOP Rx.

## Delete From Suspense File

This option allows the manager to delete from the RX SUSPENSE file (#52.5) the records of all the prescriptions which have already been printed prior to the user specified number of days. This specified number of days must be set from 7 to 90 days at the 'DAYS PRINTED RX STAYS IN 52.5' prompt in the Site Parameter Enter/Edit option. The task is set to run every 7 days at the user specified time. The user may also requeue or dequeue this task using this option. Once a prescription is deleted from suspense, it cannot be reset for reprinting.

## CMOP Functionality for Delete From Suspense File

CMOP prescriptions will not be deleted from the RX SUSPENSE file (#52.5) during the data transmission process.

## Print From Suspense File

This option allows the user to print labels from the RX SUSPENSE file. First, enter the 'Print Through' date. Any prescriptions with a suspense date on or before the date entered will print. Additionally, if a patient has at least one prescription on or before the date entered, any other prescriptions for that patient that are in suspense for the specified number of days defined in the DAYS TO PULL FROM SUSPENSE field (#3) of the OUTPATIENT SITE file (#59) will be pulled from suspense and printed.

For example, if today's date is entered and Patient A has a prescription to be printed through today, all of Patient A's prescriptions for today and the number of days set in the DAYS TO PULL FROM SUSPENSE field (#3) in the OUTPATIENT SITE file (#59) will be printed. If there are no prescriptions for Patient A through  today, no labels will print.

A short profile for every patient for whom you are printing a label for a new prescription is also printed if your site parameters are set for this profile.

## CMOP Functionality for Print From Suspense File

A date range is selected and 'scanned ahead' for a pre-selected number of days to collect all entries on patients for this transmission. 'Days to print from suspense' is currently a site parameter in Outpatient Pharmacy Version 7.0.

Selecting the Print From Suspense File option displays the following for users who hold the CMOP security keys, PSXCMOPMGR and PSX XMIT:

```
1 - Initiate Standard CMOP Transmission 2 - Initiate CS CMOP Transmission 3 - Print Current Division - Standard CMOP from Suspense 4 - Print Current Division - CS CMOP from Suspense 5 - Standard Print from Suspense Select (1, 2, 3, 4, 5):
```

- 1-Initiate Standard CMOP Transmission will gather (Non-Controlled Substances) CMOP data 'Queued for Transmission' for the selected date range and transmit to the CMOP. The sender will receive a 'Transmission Confirmation' message via MailMan when the data transmission is completed.
+ Prior to transmitting, the data will be screened for exceptions (window, tradename, non-CMOP, Refill-Too-Soon/DUR rejects, Reject Resolution Required rejects, etc.). (See CMOP Transmission Process for additional information.)
- 2-Initiate CS CMOP Transmission will gather Controlled Substances CMOP data 'Queued for Transmission' for the selected date range and transmit to the CMOP. The sender will receive a 'Transmission Confirmation' message via MailMan when the data transmission is completed.
+ Prior to transmitting, the data will be screened for exceptions (window, tradename, non-CMOP, Refill-Too-Soon/DUR rejects, Reject Resolution Required rejects, etc.). (See CMOP Transmission Process for additional information.)
- 3-Print Current Division - Standard CMOP from Suspense gathers Non-Controlled Substances data for the selected date range and prints the labels. NO DATA will TRANSMIT to the CMOP.  Drugs or items for all labels printed should be filled locally. All usual outpatient prompts will be displayed.
+ The entries are automatically sorted by Patient name and the 'SORT BY PATIENT NAME OR ID#: (P/I)' prompt is not displayed.
- 4-Print Current Division - CS CMOP from Suspense gathers Controlled Substances data for the selected date range and prints the labels. NO DATA will TRANSMIT to the CMOP.  Drugs or items for all labels printed should be filled locally. All usual outpatient prompts will be displayed.
+ The entries are automatically sorted by Patient name and the 'SORT BY PATIENT NAME OR ID#: (P/I)' prompt is not displayed.

5-Standard Print from Suspense will print all labels for Rx's NOT 'Queued to Send' for the selected date range.  All usual outpatient prompts will be displayed.

+ Combinations of the selections presented above are allowed with the exception of 1,2 or 2,1.

## Pull Early From Suspense

This option is used by the pharmacy manager, pharmacist, or the technician to pull a specific prescription or all prescriptions for a patient from the RX SUSPENSE file (#52.5) early.

## CMOP Functionality for Pull Early From Suspense

A CMOP prescription can be pulled from suspense only if the CMOP INDICATOR is set to 'Queued for Transmission'. The prescription is marked as printed and the CMOP INDICATOR reset to 'Printed Locally'. The Rx is not transmitted to the CMOP and the user is not notified that a CMOP prescription was printed.

## Reset and Print Again

This reset/reprint option allows the manager to reset the RX SUSPENSE file (#52.5) so that labels that have already been printed once can be printed again. This routine is useful if certain portions of the previously printed labels are unusable.

<!-- image -->

+ This option only resets for the date range specified by the user. The DAYS TO PULL FROM SUSPENSE site parameter is not taken into consideration during reset.

Labels are printed through the date selected by the user.

A short profile for every patient for whom you are printing a label for a new prescription may also be printed if your site parameters are set for this profile.

## CMOP Functionality for Reset and Print Again

Selecting the Reset and Print Again option displays the following only to users who hold the CMOP security keys, PSXCMOPMGR and PSX XMIT:

```
1-Reset CMOP and Transmit 2-Reset CMOP and Print Again 3-Standard Reset and Print Again Select (1,2,3): 1 Reset CMOP and Transmit
```

- 1-Reset CMOP and Transmit resets CMOP entries which have 'printed but not transmitted' for the selected date range. The user is prompted for a date to transmit through and the transmission is queued.

```
Are you sure you want to continue?  NO//
```

Yes - Resets CMOP data and transmits to the CMOP. No - Exits.

```
Select (1,2,3): 2 Reset CMOP and Print Again
```

- 2-Reset CMOP and Print Again resets and prints labels for CMOP entries which have been printed by the Print CMOP from Suspense option and have not transmitted. There is no data transmitted to the CMOP. The Rx's for the labels printed must be filled locally.

Are you sure you want to continue?  NO//

```
Yes-Resets CMOP data and prints labels. No-Exits. Select (1,2,3): 3
```

- 3-Standard Reset and Print Again  resets and prints all outpatient labels not 'Queued for Transmission' and usual outpatient prompts are displayed.
+ No provision is made to allow print of labels for CMOP data which has already 'transmitted.'

## CMOP Functionality for Update Patient Record

New functionality to this option has been added to decide at a patient level whether a patient's Rx's will be transmitted to the CMOP.

## Example: Update Patient Record

```
Select Outpatient Pharmacy Manager Option: UPDATE Patient Record Select Patient: CMOPPATIENT3,ONE 02-23-74     000579013 CMOPPATIENT3,ONE                        ID#:   000-57-9013 123 OAK STREET                          DOB:   FEB 23,1974 PLANO                                 PHONE:   5555555555 TEXAS  75024                           ELIG: WEIGHT(Kg):                              HEIGHT(cm): DISABILITIES: ALLERGIES: ADVERSE REACTIONS: SOCIAL SECURITY NUMBER: 000579013// ^ >>PHARMACY PATIENT DATA<< CAP: SAFETY// <RET> MAIL: DO NOT MAIL// ?? This field is used to: A) Determine whether this patient's Rx's are to be sent to the CMOP, or retained for local distribution. If 2-4 are selected, none of this patient's Rx's will be transmitted to the CMOP. B) Select what the mail priority is.  The CMOP choices are limited to (0) REGULAR and (1) CERTIFIED. Local mail may be designated (3) LOCAL REGULAR or (4) LOCAL - CERTIFIED. The 'DO NOT MAIL' code (2) may be used to ensure that the patient's Rx's are not mailed. Choose from: 0        REGULAR MAIL 1        CERTIFIED MAIL 2        DO NOT MAIL 3        LOCAL - REGULAR MAIL 4        LOCAL - CERTIFIED MAIL
```

```
MAIL: DO NOT MAIL// <RET> DIALYSIS PATIENT: <RET> MAIL STATUS EXPIRATION DATE: ?? Examples of Valid Dates: JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057 T   (for TODAY),  T+1 (for TOMORROW),  T+2,  T+7,  etc. T-1 (for YESTERDAY),  T-3W (for 3 WEEKS AGO), etc. If the year is omitted, the computer uses the CURRENT YEAR. This field places a time limit on the 'Do Not Mail', 'Local - Regular Mail' and 'Local - Certified Mail' conditions in the 'MAIL' field. If a date is placed in this field and the software detects that the date the Rx is processed is greater than the date in the field (past the expired date) a default value of 'Regular Mail' will be assumed for the 'MAIL' field. NOTE: The actual value of the 'MAIL' field will not be changed by the software, but can only be modified by a user editing the 'MAIL' field. MAIL STATUS EXPIRATION DATE: T (FEB 24, 1997) NARRATIVE: <RET> PATIENT STATUS: SC// ^
```

## PSXCMOPMGR

Management personnel use this menu to control operations of the Consolidated Mail Outpatient Pharmacy.

Transmission Review Interface Menu ... Operations Management ... Display System Status Reports Menu ... Rx Inquiry Manual/Barcode Release Prescription Unhold Transmission View Transmission Enter/Edit Transmission Comments CMOP Drug/Item Management ... Facility Cost Management ... Archive CMOP Data ...

## PSXCMOPMGR

With this option the user can display the status of current transmissions. The user can print a summary of all statuses or a summary for each status. The following is an explanation of the statuses:

S = Summary

Q = Queued

P = Processed

C = Closed

H = Hold

L = Labels Printed

## Example: Transmission Review

<!-- image -->

```
A         Ascending Order D         Descending Order Enter response: Ascending// A scending Order Enter Begin Date for Report:  TODAY// T-30 (FEB 22, 1997) Enter End Date for Report:  TODAY// T (MAR 24, 1997) DEVICE: [Select Print Device]
```

## ................................................................. report follows on the next page..............................................................

<!-- image -->

## Monitor CMOP Interface

## PSXCMOPMGR

This option is used to display the CMOP Interface Log. The log contains the date and time and message. (See Appendix A for a complete listing of the Interface Log messages.)

## Start CMOP Interface

## PSXCMOPMGR

With this option the user activates the communication link with the vendor system and enables the transfer of data from the VistA CMOP system to the vendor for dispensing. When the CMOP Manager selects the Start CMOP Interface option the following four selections are displayed:

## All Transmissions Queued

This selection will start the interface and download all transmissions in FIFO order. Once the queue is empty a query request will be initiated. The interface remains running and future transmissions will be downloaded as soon as they are queued. If no transmissions are in the queue, query requests will be initiated as per the 'Query Request Interval' site parameter.

## Single Transmission

The CMOP Manager has the option to download a single transmission to the vendor if the queue priority parameter is set to prioritize. Only one transmission number can be entered. This transmission will download to the vendor, all other transmissions will remain in the queue. Once the transmission has been downloaded to the vendor, the interface will be stopped.

## Prioritize Queue

If Prioritize Queue is selected a report of the current queue will be displayed. This report will list all transmissions waiting to be downloaded to the vendor and will be in first-in first-out (FIFO) order. Each transmission will be assigned a sequence number in the report. At the end of the report, the prompt, 'Prioritize Queue NO//' will be displayed. If the default of NO is selected the transmissions will be downloaded in FIFO order. If YES is selected, the prompt 'Enter Queue Order:' will be displayed. The user will enter the sequence to download the transmissions. The transmissions will be resequenced in this order. If the report displays 10 transmissions, and the user wants to put sequence number 6 at the head of the queue and let the other transmissions download in FIFO order, they only need to enter 6 at the Enter Queue Order prompt. If the user doesn't enter a sequence, the default will be to download the transmissions in FIFO order. Only those transmissions that are in the queue when this report is printed will be affected by the prioritization process. The interface will continue to run downloading transmissions as they are queued or initiating queries.

## Query Request

This selection allows the CMOP Manager to initiate a query without downloading transmissions. Once the query is completed the interface will be stopped. If the Query Request Interval has not expired and this option is selected, a message similar to the following will be displayed.

'Another query cannot be initiated for 52 minutes.'

## Example: Start the CMOP Interface

<!-- image -->

[The following screen will be displayed anytime one of the options have been selected. The screen will refresh every 30 seconds unless the user enters an ^.]

```
*** Interface STARTED *** CMOP SYSTEM STATUS Interface             : RUNNING Transmissions Queued  : 1.................Orders/Rx's: 1/1 Last Order Processed  : 521-748-26........PHARMACY...............Feb 19@09:52 Last Query Completed  : #551..............1 Rx's.................Feb 19@09:52 *****Release Data Acknowledgements > 24 hours OUTSTANDING***** Background Process                        Last Ran               Scheduled For Release Data Filed in Master Database.....Feb 26@14:47...........Feb 26@15:02 Database Purge............................Feb 25@16:13...........Feb 26@16:13 Release File Purge........................Feb 25@23:01...........Feb 26@23:01 Release Acknowledgement File Purge........Feb 25@23:30...........Feb 26@23:30 Enter "^" to quit ^
```

<!-- image -->

```
*** Interface STARTED *** Select Interface Menu Option: <RET>
```

## Example 2: Query Request

```
Select Interface Menu Option: START CMOP Interface Select one of the following: A         All Transmissions Queued S         Single Transmission P         Prioritize Queue Q         Query Request Enter response: A// Q uery Request Another query cannot be initiated for 52 minutes. Select Interface Menu Option: <RET>
```

## Stop CMOP Interface

## PSXCMOPMGR

This option stops the CMOP interface data transmission.

## Start/Stop Background Filer

This option enables the user to schedule or unschedule the background filer that files the released data in the CMOP MASTER DATABASE file (#552.4). When the user enters a starting date and time, the message 'Job Started' is displayed. If the background filer is stopped the message 'Job Stopped' is displayed.

## Nightly Purge of CMOP Database

This option schedules or unschedules the nightly job to purge the CMOP DATABASE file (#552.2). To start the nightly purge of the CMOP database, enter the date and time.

## Nightly Purge of Release Data

This option is used to schedule or unschedule the nightly background job to purge release data. To start the purge of release data, enter the date and time. All data already filed in the CMOP MASTER DATABASE file (#552.4) will be deleted.

## Purge of Release Messages

With this option you are able to start or stop the background job that purges the stored data pertaining to the release data mail messages that are returned to the medical centers. You are asked to enter the number of days of data you want to keep. This number also determines the amount of data that will appear on the Report of Release Data Returned and the Resend Release Data reports. For example, if you enter 10 days, then each of the reports will provide information for that number of days. Any data older than 10 days will be purged.

## Resend Release Data to VAMCs

This option provides you with a report by medical center of any release data mail messages that have not been acknowledged within 24 hours. A release data mail message is one that has been returned by the medical center and completely filed at the CMOP facility. At the end of the report you will receive the prompt, 'Resend Messages'. You can enter a list of numbers separated by commas. The specified messages will be returned to the medical center as one new mail message. If there aren't any unacknowledged messages for the medical center selected, the you will get the message, 'No data for the report'. This report can be sent to the screen or it can be sent to a printer.

## Example: Resend Release Data

<!-- image -->

## System Parameter Enter/Edit

This option displays the current site parameter settings and allows editing of those that can be changed.

| Query Request Interval         | This parameter controls the time interval between query requests. The time is entered as hours or fractions of an hour.    |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Query Limit Request            | This parameter controls the number of Rx's that the VistA system will accept during a query.                               |
| Days to Retain Release Summary | This parameter controls the number of days release acknowledgement summaries will be retained in the CMOP OPERATIONS file. |
| CMOPDrug Cost Missing Report   | This parameter controls whether a CMOP DRUG Cost Missing error report is generated.                                        |

## Example: System Parameter Enter/Edit

```
Select Operations Management Option: S ystem Parameter Enter/Edit Query Request Interval:  1 hr // < ENT >  ( 1 hr ) Query Limit Request:  10000 // < ENT > Days to Retain Release Summary:  10 // < ENT > CMOP DRUG Cost Missing reports: YES// ? Do you want the 'CMOP DRUG Cost Missing' error report generated? (Y/N) Choose from: Y YES N NO CMOP DRUG Cost Missing reports: YES// < ENT > Select Operations Management Option: < ENT >
```

## Example: Display System Status

```
Select CMOP System Management Menu Option: D isplay System Status CMOP SYSTEM STATUS Interface             : STOPPED Transmissions Queued  : Nothing in the Queue Last Order Processed  : 521-3-12..........BIRMINGHAM (C).........Feb 26@10:16 Last Query Completed  : #3................7 Rx's.................Feb 26@10:16 *****Release Data Acknowledgments > 24 hours OUTSTANDING*****
```

```
*****Rejected Orders OUTSTANDING***** Background Process                       Last Ran               Scheduled For Release Data Filed in Master Database....Feb 26@12:17...........Feb 26@12:32 Database Purge.......................................Not Scheduled Release File Purge.......................Feb 25@23:00...........Feb 26@23:00 Release Acknowledgement File Purge.......Feb 25@23:30...........Feb 26@23:30
```

## Transmission Report Summary

This option is used to print a report of prescription data for the selected data transmission. The user can only select transmissions which are waiting to download to the automated system.

The report contains the data transmission number, facility, division, the date the transmission was received, total number of orders and prescriptions, and the name of the patient, SSN, Rx number, barcode, and drug name.

## Rejected Messages Report

This option prints information for any rejected messages of a data transmission for review by the CMOP manager. The date range selected by the user is based on the processed date and time.

## Example: Rejected Messages Report

```
Select CMOP System Management Menu Option: RE ports Menu Select Reports Option: REJ ected Messages Report ENTER BEGINNING DATE :  NOW// < ENT > ENTER ENDING DATE :  NOW// < ENT > DEVICE: [Select print device.]
```

## Example: Rejected Messages Report (continued)

```
CMOP Rejected Messages for Transmission # 521-367 Printed : NOV 10,1997@10:27:13 Facility : BIRMINGHAM, AL.              Division:  BIRMINGHAM (C) Received on  Nov 02, 1997 3:44          Total Orders:  4    Total Rx's:  14
```

|   ORDER | NAME                               | RX NUMBER                                       | BAR CODE                                          | DRUG NAME                                                                                                  |
|---------|------------------------------------|-------------------------------------------------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------|
|       7 | REJECTED REASON: CMOPPATIENT3,ONE  | DATA ERROR 11636A 10971E 10345K 11757B DATA     | 521-52066 521-52067 521-52069 521-52070           | ALBUTEROL SULFATE 4MG TAB HALOPERIDOL 20MG TAB IBUPROFEN 600MG TAB ISONIAZID 100MG TAB                     |
|       8 | REJECTED REASON: CMOPPATIENT4,ONE  | ERROR 11597E 11433E 11247F 11325H               | 521-52071 521-52072 521-52073 521-52074           | ALBUTEROL 90MCG 200D ORAL ALUMINUM CL HEXAHYDRATE 2 AMINOPHYLLINE 100MG TAB AMITRIPTYLINE HCL 10MG TA      |
|       9 | REJECTED REASON: CMOPPATIENT5,ONE  | DATA ERROR 15167                                | 521-52057                                         | NAPROXEN 375MG TAB                                                                                         |
|      10 | REJECTED REASON: CMOPPATIENT18,ONE | DATA ERROR 11376D 11417E 200012B 11706E 200011D | 521-52059 521-52060 521-52062 521-52063 521-52064 | AMILORIDE HCL 5MG TAB AMPICILLIN 250MG/5ML SUSP FOLIC ACID 1MG TAB IBUPROFEN 600MG TAB ISONIAZID 100MG TAB |

## Unreleased Rx's Report

With this option the user can print a summary of all prescription data in the CMOP Master Database that have not been released. The summary contains the facility, pharmacy division, date transmitted and received, the Rx number, drug ID, and the number of fills. The report will sort by the order number within the batches displayed.  This report can be printed for a selection of date ranges, facilities, and type of transmissions (Controlled Substances and Non-Controlled Substances).

## Duplicate Release Data Report

This report may be accessed in one of two ways.

- 1) When the system automatically detects duplicate Rx's, an alert is generated. Processing this alert will cause the report to print. Answering yes to the 'Delete these Rx's' release data purge prompt found at the end of the report will mark these Rx's for deletion by the background filer.
- 2) The report can also be generated by using the option 'PSX DUPLICATE RX PURGE'. This option performs the same function as #1 except it gives the user the chance to access the list of duplicates when necessary and not just when an alert is generated.

## Example: Duplicate Release Data Report

<!-- image -->

<!-- image -->

<!-- image -->

## Facility Activity Report

This option prints a report, by facility, for a selected date and time range. The report lists each transmission and the current count of Rx's that are completed, cancelled, and unreleased at the time of the report.

## Turnaround Time Report

This option queues the CMOP Rx Turnaround Time report for the selected date range. The report is based on the time difference between the transmission date and time and the date and time the pharmacist at the CMOP marked the prescription as completed and released. Information includes the average, minimum, and maximum turnaround times, and the total number of Rx's released. Due to the time required to compile the data for this report, it can only be sent to a printer.

## Report of Release Data Returned

This option provides a report by medical center of all release data that has been returned to the medical center. Totals for the number of Rx's returned, Rx's acknowledged, and Rx's not acknowledged are provided for each medical center. A grand total is provided at the end of the report. At the end of the report, if there are messages that have not been acknowledged within a 24 hour period, you will receive the prompt, 'Resend Messages'. If the you respond yes, the process will automatically go to the Resend Release Data option. If there are no unacknowledged messages, the user will not be prompted to resend messages. This report can be sent to the screen or to a printer.

## Print Rejected Orders

This option allows the user to print all rejected orders for a selected transmission. Labels cannot be printed while the CMOP interface is running.

## Print Transmission Labels

## PSXCMOPMGR

This option allows printing of labels for prescription data received by the CMOP. The user selects a transmission Facility Batch number to be printed. All labels 'Queued to send' for this transmission are printed.

## Label Restart Utility

## PSXCMOPMGR

This option enables the user to print a range of CMOP transmission labels that have jammed during normal or reprint label print operations.

## Example: Label Restart Utility

```
Select CMOP System Management Menu Option: RE ports Select Reports Option: L abel Restart Utility CMOP LABEL RESTART UTILITY To run the Label Restart Utility you will need the Rx number of the last USEABLE Rx that printed, as well as the CMOP Order # where the error occurred. Did the error occur during Reprint? NO// <RET>
```

```
Enter Beginning CMOP Order #: 521-310-1 Enter Ending CMOP Order #: 521-310-4 Enter the last USABLE Rx number printed or 'RETURN' to start at the first Rx in order: ?? You selected CMOP order # 521-310-1 If this is correct, please choose the last USABLE Rx that printed from the following list: CMOPPATIENT31,ONE 15112          ASPIRIN 325MG TAB 15114          CIMETIDINE 200MG TAB Enter the last USABLE Rx number printed or 'RETURN' to start at the first Rx in order: 15112 Select Label Printer: [Select print device.] OK TO ASSUME LABEL ALIGNMENT IS CORRECT ?:  (Y/N): YES// <RET> Requested Start Time: NOW// <RET> (FEB 20, 1997@10:21:21) LABELS Queued to Print!! Select Reports Menu Option: <RET>
```

## Reprint Transmission Labels

<!-- image -->

This option enables users at the host CMOP facilities to reprint transmission labels. To reprint the transmission labels, enter the facility-batch number.

## Example 1: Rx Inquiry Received, but not Released

```
Select CMOP System Management Menu Option: RX Inquiry Select Facility Batch Reference # : 521-473 TRANSMITTED :JAN 15,1997@11:58:15     RECEIVED   : JAN 15,1997@11:58:15 TO VENDOR  : RX # : 11698C ORIGINAL        DRUG ID : I0005       QTY : 120      COST : RX STATUS : RECEIVED Select Facility Batch Reference # : <RET> Select CMOP System Management Menu Option: <RET>
```

## Example 2: Rx Inquiry Received and Released

```
Select CMOP System Management Menu Option: RX Inquiry Select Facility Batch Reference # : 521-336 TRANSMITTED :OCT 27,1996@15:29:13     RECEIVED   : OCT 27,1996@15:29:13
```

```
TO VENDOR  : NOV 17,1996@16:55:40 RX # : 11780B REC'D FROM VENDOR  : NOV 17,1996@16:55:39 ORIGINAL        DRUG ID : V0006       QTY : 50       COST : 0.067 RX STATUS : PROCESSED       COMPLETED NOV 17,1996@16:55   AUTOMATED NDC : 1234TEST5678          BY EMPLOYEE : CMOPPHARMACIST28,THREE PROCESSED DT/TM : NOV 17,1996@17:03:46          QUERY ID # 311 LOT # : 1234TST     EXP DATE : JUL 7,1997 Select Facility Batch Reference # : <RET> Select CMOP System Management Menu Option: <RET>
```

## PSXCMOPMGR

This option allows the user at the host facility to release a prescription for a label printed by the VistA system. In order to manually release an Rx, the user must hold the PSXCMOPMGR key. This option is not used to release prescriptions dispensed by the automated non-VistA vendor system.

If an Rx is rejected by the vendor system it will remain on the CMOP system until it is printed and released. In some infrequent cases there is an Rx that should be cancelled instead of printed and released. This option has been created to handle the entry of the cancellation in the CMOP RELEASE file to allow the information to be returned to the VAMC and update the PRESCRIPTION file (#52).

## Example: Manual/Barcode Release Prescription

```
Select CMOP System Management Menu Option: M anual/Barcode Release Prescription This option will only release/complete Rx's which have labels printed manually Select one of the following: R         RELEASE C         NOT DISPENSED Enter response: C NOT DISPENSED Enter Cancel Reason: QUANTITY OR DISPENSE PROBLEM. Enter PHARMACIST: CMOPPHARMACIST30 ,THREE        CT Enter/Wand PRESCRIPTION number: 521-53319 RX# 521-53319 not dispensed.
```

## Example: Unhold a Transmission

```
Select CMOP System Management Menu Option: Unhold Transmission Select CMOP REFERENCE FACILITY BATCH REFERENCE: 521-409 The original transmission, 521-408 has already been sent to the automated vendor system. Transmission, 521-409 is a retransmission of 521-408 and can not be queued. Select CMOP System Management Menu Option: <RET>
```

## Example: View Transmission

```
Select CMOP System Management Menu Option: View Transmission Select CMOP REFERENCE FACILITY BATCH REFERENCE: 597-8881 VIEW TRANSMISSION Transmission     : 597-8881            Transmitted  : Sep 14, 1996 10:13:08 am Status           : Processed           Received     : Sep 14, 1996 10:28 am Division         : LINCOLN             Processed    : Sep 14, 1996 10:46:01 am Sender           : CMOPPHARMACIST30,THREE Beginning order #: 1                   Total orders : 126 Ending order #   : 126                 Total Rx's   : 283 Select CMOP System Management Menu Option: <RET>
```

## Example: Enter/Edit Transmission Comments

```
Select CMOP System Management Menu Option: E nter/Edit transmission comments Select CMOP REFERENCE FACILITY BATCH REFERENCE: 521-409 Transmission     : 521-409             Transmitted  : Nov 29, 1996 2:33:25 pm Status           : Hold                Received     : Nov 29, 1996 2:33:57 pm Division         : BIRMINGHAM (C) Sender           : CMOPPHARMACIST30,THREE Beginning order #: 1                   Total orders : 2 Ending order #   : 2                   Total Rx's   : 6 Retransmission of 521-408 COMMENTS: 1>THIS IS A RETRANSMISSION OF 521-408 BECAUSE FIRST TRANSMISSION FAILED. 2><RET> EDIT Option: <RET> Select CMOP System Management Menu Option: <RET>
```

## Loop CMOP Match to Local Drug File

## PSNMGR

This option allows users to select entries in the local DRUG file (#50), review NDF matches, and mark entries to transmit to the CMOP.

## Example: Loop CMOP Match to Local Drug File

```
Select CMOP Site Manager Menu Option: CMOP D rug/Item Management Select CMOP Drug/Item Management Option: L oop CMOP Match to Local Drug File This option allows you to choose entries from your drug file and helps you review your NDF matches and mark individual entries to send to CMOP. If you mark the entry to transmit to CMOP, it will replace your Dispense Unit with the VA Dispense Unit. In addition, you may overwrite the local drug name with the VA Print Name and the entry will remain uneditable. Do you wish to loop through the whole file? (If you answer "NO", you will loop through ONLY the ones previously marked as "Do not transmit to CMOP"). Enter Yes or No: N O I have to build a table before you can begin "looping" so let me put you on "hold" for a moment. ............................................................... VA Print Name: GUAIFENESIN 100MG/5ML SYRUP         VA Dispense Unit: ML Local Drug Generic Name: GUAIFENESIN 100MG/5ML LIQUID VA Drug Class: RE302 ORDER UNIT: 120ML DISPENSE UNITS/ORDER UNITS: 120 DISPENSE UNIT: MG/ML PRICE PER DISPENSE UNIT: 0.01 ** This entry has been previously marked NOT to transmit to CMOP ** Do you wish to mark this drug to transmit to CMOP? Enter Yes or No: Y ES Your old Dispense Unit  MG/ML  does not match the new one  ML. You may wish to edit the Price Per Order Unit and/or the Dispense Units Per Order Unit. PRICE PER ORDER UNIT: 0.01// <RET> DISPENSE UNITS PER ORDER: 120// <RET> Do you wish to overwrite your local name? Enter Yes or No: Y ES VA Print Name: GUAIFENESIN 100MG/5ML SYRUP Local Drug Name                            CMOP?    VA D.U.        O.W.? ------------------------------------------------------------------------------1. GUAIFENESIN 100MG/5ML SYRUP                YES      ML             YES Price Per Order Unit = 0.01
```

<!-- image -->

<!-- image -->

- +

```
Dispense Units Per Order Unit = 120 If you answer "Yes" you will go to the next VA Print Name. If you answer "No" you will go back through this particular VA Print Name group. Are you sure everything is correct? Enter Yes or No: Y ES You've completed marking everything that is possible.
```

## CMOP Mark/Unmark (Single drug)

## PSNMGR

With this option the user can mark or unmark a single drug for transmission to the CMOP.

If a drug marked for CMOP in the DRUG file (#50) needs to be edited, the entry must be unmarked for CMOP using the CMOP Mark/Unmark (Single drug) option. Once editing is completed, the drug must be re-marked for CMOP using the CMOP Mark/Unmark (Single drug) option.

## ***IMPORTANT***

When using the option CMOP Mark/Unmark (Single drug) to mark a drug for CMOP the user must update the cost information in the DRUG file (#50) to ensure the cost data for the refill will be correct.

## Example 1:  Marking a CMOP Drug (Single drug)

```
Select CMOP Site Manager Menu Option: CMOP D rug/Item Management Select CMOP Drug/Item Management Option: CMOP M ARK/Unmark (Single drug) This option allows you to choose entries from your drug file and helps you review your NDF matches and mark individual entries to send to CMOP. If you mark the entry to transmit to CMOP, it will replace your Dispense Unit with the VA Dispense Unit. In addition, you may overwrite the local drug name with the VA Print Name and the entry will remain uneditable. Select DRUG GENERIC NAME: GUAIFENESIN 100MG/5ML LIQUID RE302 Local Drug Generic Name: GUAIFENESIN 100MG/5ML LIQUID ORDER UNIT: 120ML DISPENSE UNITS/ORDER UNITS: 120 DISPENSE UNIT: EA PRICE PER DISPENSE UNIT: 0.01 VA Print Name: GUAIFENESIN 100MG/5ML SYRUP       VA Dispense Unit: ML VA Drug Class: CN103 Do you wish to mark this drug to transmit to CMOP? Enter Yes or No: Y ES QUANTITY DISPENSE MESSAGE: ENTER IN MULTIPLES OF 120. Your old Dispense Unit  EA  does not match the new one  ML. You may wish to edit the Price Per Order Unit and/or The Dispense Units Per Order Unit. PRICE PER ORDER UNIT: 3.70// 1.20 DISPENSE UNITS PER ORDER UNIT: 1// 120 Do you wish to overwrite your local name? Enter Yes or No: Y ES Select DRUG GENERIC NAME: <RET>
```

## Example 2:  Unmarking a CMOP Drug (Single drug)

```
Select CMOP Site Manager Menu Option: CMOP D rug/Item Management Select CMOP Drug/Item Management Option: CMOP M ark/Unmark (Single drug) This option allows you to choose entries from your drug file and helps you review your NDF matches and mark individual entries to send to CMOP. If you mark the entry to transmit to CMOP, it will replace your Dispense Unit with the VA Dispense Unit. In addition, you may overwrite the local drug name with the VA Print Name and the entry will remain uneditable. Select DRUG GENERIC NAME: GUAIFENESIN 100MG/5ML SYRUP RE302 Local Drug Generic Name: GUAIFENESIN 100MG/5ML SYRUP ORDER UNIT: 120ML DISPENSE UNITS/ORDER UNITS: 120 DISPENSE UNIT: ML PRICE PER DISPENSE UNIT: 0.01 VA Print Name: GUAIFENESIN 100MG/5ML SYRUP            VA Dispense Unit: ML VA Drug Class: CN103 Do you wish to UNmark this drug to transmit to CMOP? Enter Yes or No: Y ES Select DRUG GENERIC NAME: <RET>
```

## CMOP Data from Your Local Drug File

This option is used to print a report of data in your local DRUG file (#50) marked to transmit to the CMOP. This report must be sent to a printer.

## Example: CMOP Data from Your Local Drug File

```
Select CMOP System Management Menu Option: CMOP D rug/Item Management Select CMOP Drug/Item Management Option: CMOP D ata from Your Local Drug File This option will produce a report to help you review your NDF matches. The report will group drugs together that are matched to the same VA Print Name along with the VA Dispense Unit. These will be used for CMOP purposes. You may queue the report to print, if you wish. DEVICE: [Select print device.] [This report must be sent to a printer.]
```

.............................................................................. report follows ...........................................................................

| LOCAL DRUGS MATCHED TO THE SAME VA PRINT NAME             | LOCAL DRUGS MATCHED TO THE SAME VA PRINT NAME   | LOCAL DRUGS MATCHED TO THE SAME VA PRINT NAME   |
|-----------------------------------------------------------|-------------------------------------------------|-------------------------------------------------|
| VA PRINT NAME Local GENERIC NAME                          | VA DISPENSE UNIT Local DISPENSE UNIT            |                                                 |
| ACETAMINOPHEN 650MG RTL SUPP ACETAMINOPHEN 650MG RTL SUPP | EA EA                                           |                                                 |
| ACETAZOLAMIDE 125MG TAB ACETAZOLAMIDE 125MG TAB           | TAB TAB                                         |                                                 |
| ACETAZOLAMIDE 250MG TAB ACETAZOLAMIDE 250MG TAB           | TAB TAB                                         |                                                 |
| ACETAZOLAMIDE 500MG SA CAP ACETAZOLAMIDE 500MG SA CAP     | CAP CAP                                         |                                                 |
| ACETIC ACID 0.25% IRRG SOLN ACETIC ACID 0.25% IRRG SOLN   | ML ML                                           |                                                 |

```
ACETIC ACID 2% OTIC SOLN                               ML ACETIC ACID 2% OTIC SOLN                              ML ACETIC ACID 2/ALUM ACET 10.79% OTIC SOLN               ML ACETIC ACID 2/ALUM ACET 10.79% OTIC SOLN              ML
```

[This report has been abbreviated to save space.]

## Drug Enter/Edit

<!-- image -->

With this option the user can add new drugs to the file, edit existing drugs, and inactivate drugs.

## CMOP Functionality for Drug Enter/Edit

When an entry in DRUG file (#50) has been marked for CMOP, the GENERIC NAME, and DISPENSE UNIT fields cannot be edited. If editing of these fields is necessary, the entry must be unmarked for CMOP using the CMOP Mark/Unmark (Single drug) option. Once editing is completed, the drug must be re-marked for CMOP using the CMOP Mark/Unmark (Single drug) option.

## Example: Drug Enter/Edit

```
Select CMOP System Management Menu Option: CMOP D rug/Item Management Select CMOP Drug/Item Management Option: DRUG E nter/Edit Select DRUG GENERIC NAME: AMOXA 1   AMOXAPIN 100 MG TAB 2   AMOXAPINE 100MG TAB             CN601     N/F 3   AMOXAPINE 150MG TAB                  N/F     12-10-84 CHOOSE 1-3: 2 DO YOU WANT TO MARK THIS DRUG AS AN Outpatient Pharmacy ITEM? YES// N (NO) GENERIC NAME: AMOXAPINE 100MG TAB// AMOXAPIN 100MG CMOP drug names may not be edited.?? Answer must be 1-40 characters in length GENERIC NAME: AMOXAPINE 100MG TAB// <RET> MESSAGE: <RET> QUANTITY DISPENSE MESSAGE: 5ml 10 ml only // ? Answer must be 1-68 characters in length.  Do not enter special characters such as quotes, semicolons, colons. QUANTITY DISPENSE MESSAGE: 5ml 10 ml only // <RET> [Do not enter special characters, e.g., semi-colon (;), caret (^), grave (`), forward slash (/), or colon (:).] VA CLASSIFICATION: CN601// <RET> DEA, SPECIAL HDLG: 6// <RET> MAXIMUM DOSE PER DAY: <RET> STANDARD SIG: <RET> FSN: <RET> NDC: 0005-5391-23// <RET> WARNING LABEL: <RET> Select SYNONYM: ASENDIN 100MG TAB// <RET> SYNONYM: ASENDIN 100MG TAB// <RET> INTENDED USE: <RET> NDC CODE: <RET> Select SYNONYM: <RET> REORDER LEVEL: <RET> ORDER UNIT: BT// <RET> PRICE PER ORDER UNIT: 27.23// <RET> NORMAL AMOUNT TO ORDER: <RET> DISPENSE UNIT: TAB// CAP Dispense unit of CMOP drug cannot be edited!?? Answer must be 1-10 characters in length. DISPENSE UNIT: TAB// <RET> DISPENSE UNITS PER ORDER UNIT: 100// <RET> PRICE PER DISPENSE UNIT is 0.272
```

```
SOURCE OF SUPPLY: <RET> NON-FORMULARY: N/F// <RET> INACTIVE DATE: <RET> CURRENT INVENTORY: 89970// <RET> Select DRUG GENERIC NAME: <RET>
```

## Drugs not Flagged for CMOP Transmission

This report lists items in the local DRUG file (#50) which are available at the CMOP, but have not been marked for transmission.

## Example: Drugs not Flagged for CMOP Transmission

```
Select CMOP System Management Menu Option: CMOP D rug/Item Management Select CMOP Drug/Item Management Option: DR U G S   N O T F l a g g e d   f o r   C M O P   T r a n s m i s s i o n This report will print all drugs marked for Outpatient use which are noncontrolled substances and are not marked to transmit to CMOP. This report requires 132 columns. You may queue the report to print, if you wish. DEVICE: [Select print device.] [This report must be sent to a printer.]
```

.............................................................................. report follows ...........................................................................

[This report has been abbreviated to save space.]

<!-- image -->

| FEB 15,1997                                                                                        | OUTPATIENT DRUGS   | NOT MARKED TO SEND TO CMOP Date printed: Page: 1   |
|----------------------------------------------------------------------------------------------------|--------------------|----------------------------------------------------|
| LOCAL DRUG NAME ---------------------------------------------------------------------------------- | STATUS             | VA PRINT NAME                                      |
| ----------- ALDOCLOR-150 TAB 150/METHYLDOPA 250MG TAB                                              | NOT MARKED         | CHLOROTHIAZIDE                                     |
| ALDOCLOR-250 TAB 250/METHYLDOPA 250MG TAB                                                          | NOT MARKED         | CHLOROTHIAZIDE                                     |
| ANAMINE SYRUP 30MG/5ML LIQUID                                                                      | NOT MARKED         | CTM 2/PSEUDOEPHEDRINE                              |
| ANTHRA-DERM OINT 0.25% 1.5OZ                                                                       | NOT MARKED         | ANTHRALIN 0.25% OINT                               |
| ANTHRALIN 1.0% CR 50GM                                                                             | NOT MARKED         | ANTHRALIN 1% CREAM                                 |
| APRESAZIDE 100/50 CAP CAP                                                                          | NOT MARKED         | HYDRALAZINE 100/HCTZ 50MG                          |
| APRESAZIDE 50/50 CAP                                                                               | NOT MARKED         | HYDRALAZINE 50/HCTZ 50MG CAP                       |
| APRESOLINE-ESIDRIX TAB                                                                             | NOT MARKED         | HYDRALAZINE 25/HCTZ 15MG TAB                       |
| ARISTO-PAK 4MG TAB                                                                                 | DO NOT SEND        | TRIAMCINOLONE 4MG TAB                              |
| ARISTOCORT A 0.1% OINT 60GM OINT                                                                   | NOT MARKED         | TRIAMCINOLONE ACETONIDE 0.1%                       |

## Date Range Compile/Recompile Cost Data

## PSXCOST

This option compiles or recompiles cost data for a date range specified by the user. Before the data for the specified date range is compiled, the data for the date range is deleted from the CMOP COST STATS file (#552.5).

If a background job is queued to run or is running that compiles or purges cost data for the same date range you have selected or for dates that overlap your date range, you cannot queue your compile/recompile job. (See Example 2.)

The average number of prescriptions filled in a day is 10,000 per site. To recompile an average month takes several hours.

+ The cost data for the specified date range is compiled using the data in the CMOP MASTER DATBASE file (#552.4) not by totaling the daily entries in the CMOP COST STATS file (#552.5).

## Example 1:  Date Range Compile/Recompile Cost Data

```
Select CMOP System Management Menu Option: F acility Cost Management Select Facility Cost Management Option: DA te Range Compile/Recompile Cost Data Beginning date: T-180 (SEP 01, 1996) Ending date: T-1 (FEB 27, 1997) Are you sure? N// Y YES Monthly data compilation queued from Sep 01, 1996 to Nov 1996. Requested Start Time: NOW// <RET> (FEB 28, 1997@12:21:41) Task Queued! Daily data compilation queued from Dec 01, 1996 to Feb 27, 1997. Requested Start Time: NOW// <RET> (FEB 28, 1997@12:21:46) Task Queued! Select Facility Cost Management Option: <RET>
```

## Example 2:  Date Range Compile/Recompile Cost Data

```
Select CMOP System Management Menu Option: F acility Cost Management Select Facility Cost Management Option: DA te Range Compile/Recompile Cost Data Beginning date: T-30 (JAN 29, 1997) Ending date: T (FEB 28, 1997)
```

```
Are you sure? N// Y ES Your task cannot be queued. The following active task(s) is for the same date range you have selected or for dates that overlap your date range. Status   Activity  Data Date Range   Task#  Task Started ------------------------------------------------------------------------------Running   Compile 12/01/96-02/27/97 69870  02/28/97@1221 Queued by: CMOPPHARMACIST30,THREE Queued    Compile 02/28/97-02/28/97 69828  02/28/97@0100 Queued by: CMOPPHARMACIST2,THREE Queued    Compile 02/28/97-02/28/97 69827  02/28/97@0100 Queued by: CMOPPHARMACIST27,THREE Beginning date: <RET> Select Facility Cost Management Option: <RET>
```

## Drug Cost by Drug Report

This option prints a report of drug cost by drug. The report lists the drug name, number of original fills, number of refills, total fills, total cost, average cost per dispense unit, and average cost per fill. The report can be printed for a specific facility or all facilities, and a specific division or all divisions. If the facility has more than one division and all divisions are selected, a summary sheet prints. The summary report contains a total for each division and a grand total for the facility.

## Example: Drug Cost by Drug Report

```
Select CMOP System Management Menu Option: F acility Cost Management Select Facility Cost Management Option: DR 1    Drug Cost by Drug Report 2    Drug Cost by Drug Report for One Month 3    Drug Cost by Facility Report CHOOSE 1-3: 1 Drug Cost by Drug Report Do you want to look at data concerning a specific drug? Y// N O Beginning Date: T-60 (DEC 25, 1996) Ending Date: T (FEB 23, 1997) Print data for a specific facility? Y// N O DEVICE: [Select print device.] [This report must be sent to a 132-column printer.] PRINTED: FEB 23,1997@11:23:59 PAGE 1 DRUG COST BY DRUG FOR BIRMINGHAM, AL. DEC 25,1996 TO FEB 23,1997 DIVISION: BIRMINGHAM ORIGN                    TOTAL TOTAL    AVG COST   AVG COST per DRUG                               FILLS       REFILLS      FILLS COST    per FILL   DISPENSE UNIT ================================================================================== ============================= ACETAMINOPHEN 325MG TAB                4             4          8 1.94        0.24        0.003 ACETAMINOPHEN 500MG CAP                1             2          3 0.00        0.00        0.000 ACETAZOLAMIDE 500MG SA CAP             1             0          1 5.73        5.73        0.229 ACETIC ACID 0.25% IRRG SOLN            2             0          2 284.35      142.18        2.585
```

| ACYCLOVIR                                                                      |   1 |   1 |
|--------------------------------------------------------------------------------|-----|-----|
| 200MG CAP 47.80 47.80 0.478 ALBUTEROL 90MCG 200D ORAL INHL 429.25 214.63 4.250 |   0 |   2 |
| ALBUTEROL SULFATE 2MG TAB 0.08 0.08 0.090                                      |   0 |   1 |
| ALBUTEROL SULFATE 4MG TAB 5.16 5.16 0.172                                      |   0 |   1 |
| ALLOPURINOL 100MG TAB 3.84 1.28 0.024                                          |   1 |   3 |
| ALUMINUM CL HEXAHYDRATE 20% TOP SOLN 636.25 636.25 5.090                       |   1 |   1 |
| AMANTADINE HCL 100MG CAP 91.16 22.79 0.214                                     |   1 |   4 |
| AMIKACIN SULFATE 250MG/ML INJ 5190.00 1730.00 17.300                           |   2 |   3 |
| AMILORIDE HCL 5/HCTZ 50MG TAB 32.70 16.35 0.218                                |   2 |   2 |

[Portions of this report have been abbreviated to save space.]

<!-- image -->

| PRINTED: FEB PAGE 2   |
|-----------------------|

<!-- image -->

| AL. DIVISION: PHARMACY TOTAL                                                                                                                                                                                                                                                                          | DRUG COST BY DRUG DEC 25,1996 TO ORIGN   | FOR BIRMINGHAM, FEB 23,1997                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|--------------------------------------------------------------------------------------|
| DRUG FILLS FILLS COST per FILL DISPENSE UNIT ================================================================================== ============================= AMIKACIN SULFATE 250MG/ML INJ 1730.00 1730.00 17.300 AMIODARONE HCL 200MG TAB 37.38 37.38 1.246 AMITRIPTYLINE 50/PERPHENAZINE 4MG TAB 1 | REFILLS 1 0 1 0 0                        | 1 1 1                                                                                |
| DIVISION TOTAL 1822.03 364.41                                                                                                                                                                                                                                                                         | 5 0                                      | ---------------------------------------------------------------------------------- 5 |
| -----------------------------                                                                                                                                                                                                                                                                         |                                          |                                                                                      |
| 4.795                                                                                                                                                                                                                                                                                                 |                                          |                                                                                      |
| PRINTED: FEB 23,1997@11:23:59 PAGE 5                                                                                                                                                                                                                                                                  |                                          | BIRMINGHAM,                                                                          |
| DRUG AL. DIVISION: ALL DIVISIONS                                                                                                                                                                                                                                                                      | COST BY DRUG DEC 25,1996 TO              | FOR FEB 23,1997                                                                      |
| TOTAL AVG COST AVG COST per DIVISION                                                                                                                                                                                                                                                                  | FILLS REFILLS                            | FILLS                                                                                |
| COST per FILL DISPENSE UNIT ================================================================================== =============================                                                                                                                                                          | 99 96                                    | 195                                                                                  |
| BIRMINGHAM 15643.26 80.22 0.877 BIRMINGHAM (C) 2 16.20 8.10 0.081 PHARMACY                                                                                                                                                                                                                            | 0 2                                      |                                                                                      |
| 1822.03 364.41 4.795                                                                                                                                                                                                                                                                                  |                                          |                                                                                      |
| ----------------------------------------------------------------------------------                                                                                                                                                                                                                    | 5 0                                      | 5                                                                                    |
| ----------------------------- FACILITY TOTAL 17481.49 86.54 0.949                                                                                                                                                                                                                                     | 104 98                                   |                                                                                      |
|                                                                                                                                                                                                                                                                                                       |                                          | 202                                                                                  |

## Drug Cost by Drug Report for One Month

This option prints a monthly drug cost report for a month specified by the user. The report lists the total fills, total quantity, total cost, average cost per dispense unit, and formulary/nonformulary. It can be printed for a specified drug or all drugs, a specified facility or all facilities, and a specific division or all divisions. A total for all divisions is included at the end of the report. The minimum total number of refills and minimum total cost are assigned by the user to further refine this report.

## Example: Drug Cost by Drug Report for One Month

```
Select CMOP System Management Menu Option: F acility Cost Management Select Facility Cost Management Option: DR 1    Drug Cost by Drug Report 2    Drug Cost by Drug Report for One Month 3    Drug Cost by Facility Report CHOOSE 1-3: 2 Drug Cost by Drug Report for One Month Enter Month/Year: 11/97 (NOV 1996) Do you want to look at data concerning a specific drug? Y// N O Print data for a specific facility? Y// <RET> ES Select FACILITY: BIRM INGHAM, AL.                                   521
```

<!-- image -->

| Print data for a specific division? Y// <RET> ES                                                                                                                                | Print data for a specific division? Y// <RET> ES                                                                                                                                | Print data for a specific division? Y// <RET> ES                                                                                                                                | Print data for a specific division? Y// <RET> ES                                                                                                                                |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Select Minimum Total number of Refills: : (0-50): 0// <RET>                                                                                                                     | Select Minimum Total number of Refills: : (0-50): 0// <RET>                                                                                                                     | Select Minimum Total number of Refills: : (0-50): 0// <RET>                                                                                                                     | Select Minimum Total number of Refills: : (0-50): 0// <RET>                                                                                                                     |
| Select Minimum Total Cost: : (0-9999): 0// <RET> DEVICE: [Select print device.] [This report must be sent to a 132-column printer.]                                             | Select Minimum Total Cost: : (0-9999): 0// <RET> DEVICE: [Select print device.] [This report must be sent to a 132-column printer.]                                             | Select Minimum Total Cost: : (0-9999): 0// <RET> DEVICE: [Select print device.] [This report must be sent to a 132-column printer.]                                             | Select Minimum Total Cost: : (0-9999): 0// <RET> DEVICE: [Select print device.] [This report must be sent to a 132-column printer.]                                             |
| PRINTED: DEC 23,1996@12:17:57                                                                                                                                                   | PRINTED: DEC 23,1996@12:17:57                                                                                                                                                   | PRINTED: DEC 23,1996@12:17:57                                                                                                                                                   | PRINTED: DEC 23,1996@12:17:57                                                                                                                                                   |
| BIRMINGHAM, AL. NOV 1996 MINIMUM REFILLS OF 0 AT A MINIMUM COST                                                                                                                 | BIRMINGHAM, AL. NOV 1996 MINIMUM REFILLS OF 0 AT A MINIMUM COST                                                                                                                 | BIRMINGHAM, AL. NOV 1996 MINIMUM REFILLS OF 0 AT A MINIMUM COST                                                                                                                 | BIRMINGHAM, AL. NOV 1996 MINIMUM REFILLS OF 0 AT A MINIMUM COST                                                                                                                 |
| OF $0                                                                                                                                                                           | OF $0                                                                                                                                                                           | OF $0                                                                                                                                                                           | OF $0                                                                                                                                                                           |
| DIVISION: BIRMINGHAM (C)                                                                                                                                                        | DIVISION: BIRMINGHAM (C)                                                                                                                                                        | DIVISION: BIRMINGHAM (C)                                                                                                                                                        | DIVISION: BIRMINGHAM (C)                                                                                                                                                        |
| TOTAL TOTAL                                                                                                                                                                     | TOTAL TOTAL                                                                                                                                                                     | TOTAL TOTAL                                                                                                                                                                     | TOTAL TOTAL                                                                                                                                                                     |
| TOTAL AVG COST per                                                                                                                                                              | TOTAL AVG COST per                                                                                                                                                              | TOTAL AVG COST per                                                                                                                                                              | TOTAL AVG COST per                                                                                                                                                              |
| DRUG FILLED QUANTITY COST DISPENSE UNIT N/F ================================================================================== ================================================ | DRUG FILLED QUANTITY COST DISPENSE UNIT N/F ================================================================================== ================================================ | DRUG FILLED QUANTITY COST DISPENSE UNIT N/F ================================================================================== ================================================ | DRUG FILLED QUANTITY COST DISPENSE UNIT N/F ================================================================================== ================================================ |
| ACETAMINOPHEN 325MG TAB 2 400                                                                                                                                                   | ACETAMINOPHEN 325MG TAB 2 400                                                                                                                                                   | ACETAMINOPHEN 325MG TAB 2 400                                                                                                                                                   | ACETAMINOPHEN 325MG TAB 2 400                                                                                                                                                   |
| 1.20 0.003 ACETAMINOPHEN 500MG CAP 2 120                                                                                                                                        | 1.20 0.003 ACETAMINOPHEN 500MG CAP 2 120                                                                                                                                        | 1.20 0.003 ACETAMINOPHEN 500MG CAP 2 120                                                                                                                                        | 1.20 0.003 ACETAMINOPHEN 500MG CAP 2 120                                                                                                                                        |
| 1.08 0.009 *** N/F ***                                                                                                                                                          | 1.08 0.009 *** N/F ***                                                                                                                                                          | 1.08 0.009 *** N/F ***                                                                                                                                                          | 1.08 0.009 *** N/F ***                                                                                                                                                          |
| ACETAZOLAMIDE 500MG SA CAP 2 200 45.80 0.229 *** N/F ***                                                                                                                        | ACETAZOLAMIDE 500MG SA CAP 2 200 45.80 0.229 *** N/F ***                                                                                                                        | ACETAZOLAMIDE 500MG SA CAP 2 200 45.80 0.229 *** N/F ***                                                                                                                        | ACETAZOLAMIDE 500MG SA CAP 2 200 45.80 0.229 *** N/F ***                                                                                                                        |
| ACETIC ACID 0.25% IRRG SOLN 1 30 77.55 2.585                                                                                                                                    | ACETIC ACID 0.25% IRRG SOLN 1 30 77.55 2.585                                                                                                                                    | ACETIC ACID 0.25% IRRG SOLN 1 30 77.55 2.585                                                                                                                                    | ACETIC ACID 0.25% IRRG SOLN 1 30 77.55 2.585                                                                                                                                    |
| ACETOHEXAMIDE 500MG TAB 3 145                                                                                                                                                   | ACETOHEXAMIDE 500MG TAB 3 145                                                                                                                                                   | ACETOHEXAMIDE 500MG TAB 3 145                                                                                                                                                   | ACETOHEXAMIDE 500MG TAB 3 145                                                                                                                                                   |
| ACETOPHENAZINE MALEATE 20MG TAB 1 100 21.20 0.212 *** N/F ***                                                                                                                   | ACETOPHENAZINE MALEATE 20MG TAB 1 100 21.20 0.212 *** N/F ***                                                                                                                   | ACETOPHENAZINE MALEATE 20MG TAB 1 100 21.20 0.212 *** N/F ***                                                                                                                   | ACETOPHENAZINE MALEATE 20MG TAB 1 100 21.20 0.212 *** N/F ***                                                                                                                   |
| ACETYLCYSTEINE 10% INH SOLN 30ML 1 3 103.05 34.350 *** N/F ***                                                                                                                  | ACETYLCYSTEINE 10% INH SOLN 30ML 1 3 103.05 34.350 *** N/F ***                                                                                                                  | ACETYLCYSTEINE 10% INH SOLN 30ML 1 3 103.05 34.350 *** N/F ***                                                                                                                  | ACETYLCYSTEINE 10% INH SOLN 30ML 1 3 103.05 34.350 *** N/F ***                                                                                                                  |
| ACYCLOVIR 200MG CAP 1 50 23.90 0.478                                                                                                                                            | ACYCLOVIR 200MG CAP 1 50 23.90 0.478                                                                                                                                            | ACYCLOVIR 200MG CAP 1 50 23.90 0.478                                                                                                                                            | ACYCLOVIR 200MG CAP 1 50 23.90 0.478                                                                                                                                            |
| ACYCLOVIR NA 500MG/VI INJ 2 100                                                                                                                                                 | ACYCLOVIR NA 500MG/VI INJ 2 100                                                                                                                                                 | ACYCLOVIR NA 500MG/VI INJ 2 100                                                                                                                                                 | ACYCLOVIR NA 500MG/VI INJ 2 100                                                                                                                                                 |
| 1546.50 15.465 ALBUTEROL 90MCG 200D ORAL INHL 6 15                                                                                                                              | 1546.50 15.465 ALBUTEROL 90MCG 200D ORAL INHL 6 15                                                                                                                              | 1546.50 15.465 ALBUTEROL 90MCG 200D ORAL INHL 6 15                                                                                                                              | 1546.50 15.465 ALBUTEROL 90MCG 200D ORAL INHL 6 15                                                                                                                              |
| 34.85 2.293 ALBUTEROL SULFATE 4MG TAB 5 110                                                                                                                                     | 34.85 2.293 ALBUTEROL SULFATE 4MG TAB 5 110                                                                                                                                     | 34.85 2.293 ALBUTEROL SULFATE 4MG TAB 5 110                                                                                                                                     | 34.85 2.293 ALBUTEROL SULFATE 4MG TAB 5 110                                                                                                                                     |
| 13.76 0.125                                                                                                                                                                     | 13.76 0.125                                                                                                                                                                     | 13.76 0.125                                                                                                                                                                     | 13.76 0.125                                                                                                                                                                     |
| ALLOPURINOL 100MG TAB 2 130                                                                                                                                                     | ALLOPURINOL 100MG TAB 2 130                                                                                                                                                     | ALLOPURINOL 100MG TAB 2 130                                                                                                                                                     | ALLOPURINOL 100MG TAB 2 130                                                                                                                                                     |
| 2.40 0.018 ALUMINUM CL HEXAHYDRATE 20% TOP SOLN 3 135 661.70 4.901 *** N/F ***                                                                                                  | 2.40 0.018 ALUMINUM CL HEXAHYDRATE 20% TOP SOLN 3 135 661.70 4.901 *** N/F ***                                                                                                  | 2.40 0.018 ALUMINUM CL HEXAHYDRATE 20% TOP SOLN 3 135 661.70 4.901 *** N/F ***                                                                                                  | 2.40 0.018 ALUMINUM CL HEXAHYDRATE 20% TOP SOLN 3 135 661.70 4.901 *** N/F ***                                                                                                  |
| AMANTADINE HCL 100MG CAP 4 275                                                                                                                                                  | AMANTADINE HCL 100MG CAP 4 275                                                                                                                                                  | AMANTADINE HCL 100MG CAP 4 275                                                                                                                                                  | AMANTADINE HCL 100MG CAP 4 275                                                                                                                                                  |
| 10.70 0.039                                                                                                                                                                     | 10.70 0.039                                                                                                                                                                     | 10.70 0.039                                                                                                                                                                     | 10.70 0.039                                                                                                                                                                     |
| AMCINONIDE 0.1% OINT 1 3 14.85 4.950 *** N/F ***                                                                                                                                | AMCINONIDE 0.1% OINT 1 3 14.85 4.950 *** N/F ***                                                                                                                                | AMCINONIDE 0.1% OINT 1 3 14.85 4.950 *** N/F ***                                                                                                                                | AMCINONIDE 0.1% OINT 1 3 14.85 4.950 *** N/F ***                                                                                                                                |
| AMIKACIN SULFATE 250MG/ML INJ 2 7 121.10 17.300 AMILORIDE HCL 5MG TAB 3 300                                                                                                     | AMIKACIN SULFATE 250MG/ML INJ 2 7 121.10 17.300 AMILORIDE HCL 5MG TAB 3 300                                                                                                     | AMIKACIN SULFATE 250MG/ML INJ 2 7 121.10 17.300 AMILORIDE HCL 5MG TAB 3 300                                                                                                     | AMIKACIN SULFATE 250MG/ML INJ 2 7 121.10 17.300 AMILORIDE HCL 5MG TAB 3 300                                                                                                     |
| 33.00 0.110                                                                                                                                                                     | 33.00 0.110                                                                                                                                                                     | 33.00 0.110                                                                                                                                                                     | 33.00 0.110                                                                                                                                                                     |
| AMINOPHYLLINE 100MG TAB 2 200                                                                                                                                                   | AMINOPHYLLINE 100MG TAB 2 200                                                                                                                                                   | AMINOPHYLLINE 100MG TAB 2 200                                                                                                                                                   | AMINOPHYLLINE 100MG TAB 2 200                                                                                                                                                   |
| 0.50 0.003 *** N/F ***                                                                                                                                                          | 0.50 0.003 *** N/F ***                                                                                                                                                          | 0.50 0.003 *** N/F ***                                                                                                                                                          | 0.50 0.003 *** N/F ***                                                                                                                                                          |
| AMINOPHYLLINE 500MG RTL                                                                                                                                                         |                                                                                                                                                                                 | 3                                                                                                                                                                               | 300                                                                                                                                                                             |
| 312.00 3.120 AMITRIPTYLINE 10/PERPHENAZINE                                                                                                                                      | *** N/F ***                                                                                                                                                                     |                                                                                                                                                                                 |                                                                                                                                                                                 |
| 43.50 0.145 AMITRIPTYLINE HCL 10MG TAB                                                                                                                                          |                                                                                                                                                                                 | 1                                                                                                                                                                               | 60 10                                                                                                                                                                           |
| 1.10 0.006                                                                                                                                                                      | *** N/F ***                                                                                                                                                                     |                                                                                                                                                                                 |                                                                                                                                                                                 |
| AMOXAPINE 100MG TAB 16.32 0.272                                                                                                                                                 | N/F ***                                                                                                                                                                         |                                                                                                                                                                                 |                                                                                                                                                                                 |
| AMOXAPINE 25MG TAB 0.00 0.000                                                                                                                                                   |                                                                                                                                                                                 | 1                                                                                                                                                                               |                                                                                                                                                                                 |
| *** AMOXAPINE 50MG TAB 100                                                                                                                                                      | *** AMOXAPINE 50MG TAB 100                                                                                                                                                      | *** AMOXAPINE 50MG TAB 100                                                                                                                                                      | *** AMOXAPINE 50MG TAB 100                                                                                                                                                      |
| 1                                                                                                                                                                               | 1                                                                                                                                                                               | 1                                                                                                                                                                               | 1                                                                                                                                                                               |
| SUPP 1 100 *** N/F *** 2MG TAB 2 200                                                                                                                                            | SUPP 1 100 *** N/F *** 2MG TAB 2 200                                                                                                                                            | SUPP 1 100 *** N/F *** 2MG TAB 2 200                                                                                                                                            | SUPP 1 100 *** N/F *** 2MG TAB 2 200                                                                                                                                            |
| 0.00 0.000                                                                                                                                                                      | 0.00 0.000                                                                                                                                                                      | 0.00 0.000                                                                                                                                                                      | 0.00 0.000                                                                                                                                                                      |
| AMPICILLIN 250MG/5ML SUSP 2 0                                                                                                                                                   | AMPICILLIN 250MG/5ML SUSP 2 0                                                                                                                                                   | AMPICILLIN 250MG/5ML SUSP 2 0                                                                                                                                                   | AMPICILLIN 250MG/5ML SUSP 2 0                                                                                                                                                   |
| 0.03 1.545 *** N/F ***                                                                                                                                                          | 0.03 1.545 *** N/F ***                                                                                                                                                          | 0.03 1.545 *** N/F ***                                                                                                                                                          | 0.03 1.545 *** N/F ***                                                                                                                                                          |
| ASCORBIC ACID 250MG TAB 2 200                                                                                                                                                   | ASCORBIC ACID 250MG TAB 2 200                                                                                                                                                   | ASCORBIC ACID 250MG TAB 2 200                                                                                                                                                   | ASCORBIC ACID 250MG TAB 2 200                                                                                                                                                   |
| 0.50 0.003 *** N/F ***                                                                                                                                                          | 0.50 0.003 *** N/F ***                                                                                                                                                          | 0.50 0.003 *** N/F ***                                                                                                                                                          | 0.50 0.003 *** N/F ***                                                                                                                                                          |

PRINTED: DEC 23,1996@12:17:57

PRINTED: DEC 23,1996@12:17:57

| ASPIRIN 325MG TAB                                                                                                                                                                                                                                                                                 |             | 2                                      | 200                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|----------------------------------------|---------------------|
| 0.50 0.003 BETAXOLOL 0.5% OPHT SOLN 5ML 46.50 7.750                                                                                                                                                                                                                                               |             | 2                                      | 6                   |
| CAPTOPRIL 100MG TAB 60.38 0.805                                                                                                                                                                                                                                                                   | *** N/F *** | 1                                      | 75                  |
| CIMETIDINE 200MG TAB 25.30 0.127                                                                                                                                                                                                                                                                  |             | 2                                      | 200                 |
| DIAZOXIDE 50MG CAP 23.99 0.390                                                                                                                                                                                                                                                                    |             | 2                                      | 62                  |
| FOLIC ACID 1MG TAB 2.94 0.004                                                                                                                                                                                                                                                                     | *** N/F *** | 13                                     | 680                 |
| FUROSEMIDE 40MG TAB 0.60 0.006                                                                                                                                                                                                                                                                    |             | 2                                      | 100                 |
| HALOPERIDOL 20MG TAB 6235.28 1.411                                                                                                                                                                                                                                                                |             | 22                                     | 4420                |
| IBUPROFEN 600MG TAB 61.71 0.026                                                                                                                                                                                                                                                                   | *** N/F *** | 22                                     | 2360                |
| ISOCARBOXAZID 10MG TAB 0.00 0.000                                                                                                                                                                                                                                                                 |             | 2                                      | 60                  |
| ISONIAZID 100MG TAB 54.60 0.039                                                                                                                                                                                                                                                                   | *** N/F *** | 13                                     | 1390                |
| LEVODOPA 250MG TAB                                                                                                                                                                                                                                                                                |             | 2                                      | 100                 |
| 8.40 0.084 NADOLOL 40MG TAB 36.60                                                                                                                                                                                                                                                                 | *** N/F *** | 3                                      | 120                 |
| 0.305 NAPROXEN 375MG TAB                                                                                                                                                                                                                                                                          | *** N/F *** | 2                                      |                     |
| 33.20 0.166 SULFATE 500MG                                                                                                                                                                                                                                                                         | *** N/F *** |                                        | 200                 |
| NEOMYCIN TAB 12.61 0.097                                                                                                                                                                                                                                                                          |             | 2                                      | 130                 |
| NIACIN 500MG TAB 0.265                                                                                                                                                                                                                                                                            | *** N/F *** | 4                                      | 370                 |
| 98.05 QUINIDINE SULFATE 200MG TAB 3.72 0.031                                                                                                                                                                                                                                                      |             | 1                                      | 120                 |
| PRINTED: DEC 23,1996@12:17:57 PAGE: 2                                                                                                                                                                                                                                                             |             | MONTHLY DRUG                           | COST REPORT FOR     |
| COST                                                                                                                                                                                                                                                                                              |             | REFILLS                                | OF 0 AT A MINIMUM   |
|                                                                                                                                                                                                                                                                                                   | MINIMUM     |                                        |                     |
| DRUG COST DISPENSE UNIT ================================================================================== ================================================ RANITIDINE HCL 150MG TAB 236.82 0.592 UNKNOWN 57.94 19.313 VERAPAMIL HCL 120MG TAB 12.73 0.067 ZINC SULFATE 220MG CAP 2.16 0.012 COST | N/F         | FILLED 4 2 4 3 ---------- MONTHLY DRUG | QUANTITY 400 ------ |
| TOTAL DIVISION                                                                                                                                                                                                                                                                                    |             | REFILLS                                | 3 190 180           |
| COST DIVISION: ALL                                                                                                                                                                                                                                                                                | N/F         |                                        | REPORT NOV 1996 OF  |
| PRINTED: DEC 23,1996@12:17:57 PAGE: 3                                                                                                                                                                                                                                                             |             |                                        | ----------          |
| ---- DIVISION TOTAL 10123.38                                                                                                                                                                                                                                                                      |             | 166                                    | 14658               |
| BIRMINGHAM, AL.                                                                                                                                                                                                                                                                                   | MINIMUM     |                                        | COST FOR            |
| OF $0                                                                                                                                                                                                                                                                                             |             |                                        | 0 AT A MINIMUM      |
|                                                                                                                                                                                                                                                                                                   |             | TOTAL                                  | TOTAL               |
|                                                                                                                                                                                                                                                                                                   |             | FILLED                                 |                     |
| ==================================================================================                                                                                                                                                                                                                |             |                                        |                     |
|                                                                                                                                                                                                                                                                                                   |             |                                        | QUANTITY            |
| ================================================                                                                                                                                                                                                                                                  |             |                                        |                     |

| BIRMINGHAM (C) 10123.38   |   166 | 14658      |
|---------------------------|-------|------------|
| ---                       |       | ---------- |
| FACILITY TOTAL            |   166 | 14658      |

## Drug Cost by Facility Report

This option prints a summary report of drug cost by facility and division. The report lists the division, total original fills, total refills, total fills, total cost, and average cost per fill. It prints all drug for all facilities or a specific facility, all divisions, or a specific division.

## Example: Drug Cost by Facility Report

```
Select CMOP System Management Menu Option: F acility Cost Management Select Facility Cost Management Option: DR 1    Drug Cost by Drug Report 2    Drug Cost by Drug Report for One Month 3    Drug Cost by Facility Report CHOOSE 1-3: 3 Drug Cost by Facility Report Beginning Date: T-60 (JAN 07, 1997) Ending Date: T (MAR 06, 1997) Print data for a specific facility? Y// N O DEVICE: [Select print device.] [This report must be sent to a 132-column printer.]
```

.............................................................................. report follows ...........................................................................

| PRINTED: MAR PAGE 1                                                                             | 6,1997@15:21:18   |                            |                    |                                                                                    |
|-------------------------------------------------------------------------------------------------|-------------------|----------------------------|--------------------|------------------------------------------------------------------------------------|
|                                                                                                 | DRUG COSTS BY JAN | FACILITY FOR 7,1997 TO MAR | BIRMINGHAM, 6,1997 | AL.                                                                                |
|                                                                                                 | ORIGN             |                            | TOTAL              | TOTAL                                                                              |
| AVG COST DIVISION per FILL                                                                      | FILLS             | REFILLS                    | FILLS              | COST                                                                               |
| ================================================================================== ======       |                   |                            |                    |                                                                                    |
| BIRMINGHAM (C) 4.68                                                                             | 1                 | 1                          | 2                  | 9.36                                                                               |
|                                                                                                 | DRUG COSTS BY JAN | FACILITY FOR 7,1997 TO MAR | LOUISVILLE, 6,1997 | KY.                                                                                |
|                                                                                                 | ORIGN             |                            | TOTAL              | TOTAL                                                                              |
| AVG COST DIVISION                                                                               | FILLS             | REFILLS                    | FILLS              | COST                                                                               |
| per FILL                                                                                        |                   |                            |                    | ================================================================================== |
| ====== LOUISVILLE                                                                               | 1                 | 0                          | 1                  | 20.00                                                                              |
| 20.00 LOUISVILLE OUTPATIENT 15.00                                                               | 0                 | 1                          | 1                  | 15.00                                                                              |
| ---------------------------------------------------------------------------------- ------ TOTAL | 1                 | 1                          | 2                  |                                                                                    |
| 17.50                                                                                           |                   |                            |                    | 35.00                                                                              |

<!-- image -->

## High Cost Rx Report

This option prints the High Cost Rx report for a specific facility or all facilities. The report contains the prescription number, drug name, quantity dispensed, drug cost, and total drug cost for each prescription. The CMOP MASTER DATABASE file (#552.4) is searched for prescriptions with the total cost greater than or equal to an amount specified by the user.

## Example: High Cost Rx Report

```
Select CMOP System Management Menu Option: F acility Cost Management Select Facility Cost Management Option: H igh Cost Rx Report Beginning Date: T-1 (MAR 12, 1997) Ending Date: T (MAR 13, 1997) Print data for a specific facility? Y// <RET> ES Select FACILITY: BIRM INGHAM, AL.                                   521 Dollar Limit (Minimum Total Cost):  (0-9999): 30// <RET> DEVICE: [Select print device.]
```

.............................................................................. report follows ...........................................................................

| PRINTED:   | MAR 13,                              | 1997@07:38:08                             |                                      |                                      |                                      | PAGE 1                                                                                    |
|------------|--------------------------------------|-------------------------------------------|--------------------------------------|--------------------------------------|--------------------------------------|-------------------------------------------------------------------------------------------|
|            | HIGH COST REPORT FOR BIRMINGHAM, AL. | HIGH COST REPORT FOR BIRMINGHAM, AL.      | HIGH COST REPORT FOR BIRMINGHAM, AL. | HIGH COST REPORT FOR BIRMINGHAM, AL. | HIGH COST REPORT FOR BIRMINGHAM, AL. | HIGH COST REPORT FOR BIRMINGHAM, AL.                                                      |
|            | FILLS                                | THAT COST AT LEAST $30                    | 12,1997                              | TO                                   | MAR                                  | -- FROM MAR 13,1997                                                                       |
| RX         | #                                    | DRUG                                      | QTY                                  |                                      | COST                                 | TOTAL COST ------------------------------------------------------------------------------ |
|            | 200012                               | FOLIC ACID 1MG TAB                        | 30                                   | x                                    | 4.250                                | = 127.50                                                                                  |
|            | 11601B                               | RANITIDINE HCL 150MG TAB                  | 100.01x                              |                                      | 0.592                                | = 59.21                                                                                   |
|            | 10981B                               | NITROGLYCERIN 0.15MG SL TAB               | 100                                  | x                                    | 1.820                                | = 182.00                                                                                  |
|            | 11760                                | ACETIC ACID 0.25% IRRG SOLN               | 30                                   | x                                    | 2.585                                | = 77.55                                                                                   |
| *          | 11728                                | AMCINONIDE 0.1% CREAM                     | 100                                  | x                                    | 4.950                                | = 495.00                                                                                  |
|            | 11554A                               | AMIKACIN SULFATE 250MG/ML INJ             | 5                                    | x                                    | 17.300                               | = 86.50                                                                                   |
|            | 11553A                               | HALOPERIDOL 20MG TAB                      | 100                                  | x                                    | 1.901                                | = 190.10                                                                                  |
|            | 11427B                               | ACETYLCYSTEINE 10% INH SOLN 30ML          | 3                                    | x                                    | 34.350                               | = 103.05                                                                                  |
| *          | 11193C                               | ZIDOVUDINE 100MG CAP CAPTOPRIL 100MG      | 40                                   | x                                    | 1.970                                | = 78.80                                                                                   |
| *          | 11561B                               | TAB                                       | 75                                   | x                                    | 0.805                                | = 60.38                                                                                   |
|            | 10581D                               | XEROFORM PETROLATUM DRESSING 5X9IN TAB    | 5                                    | x                                    | 6.100                                | = 30.50                                                                                   |
| *          | 11355A                               | RANITIDINE HCL 150MG ZIDOVUDINE 100MG CAP | 100                                  | x                                    | 0.592                                | = 59.20                                                                                   |
| *          | 11595A                               | TAB                                       | 100                                  | x                                    | 1.970                                | = 197.00                                                                                  |
|            | 11513D                               | HALOPERIDOL 20MG                          | 300                                  | x                                    | 1.901                                | = 570.30                                                                                  |
|            | 11769                                | HALOPERIDOL 20MG TAB                      | 50                                   | x                                    | 1.901                                | = 95.05                                                                                   |

## Initialize the Nightly Compile Job

## PSXCOST

This option queues a nightly job that compiles yesterday's cost data and adds the data to the CMOP COST STATS file (#552.5). The user can specify the time the job is tasked to run or accept the default of one o'clock in the morning. The nightly job also queues the next nightly job. It is recommended this job be tasked to run at night at a time convenient to the site.

Two months of daily data are retained in the CMOP COST STATS file (#552.5). On the first of each month, the daily cost data is purged for the third month back and replaced with one entry for the month.

<!-- image -->

Example: Today is 12/1/96. Daily cost data entries for 10/96 through 11/96 are retained in the CMOP COST STATS file (#552.5). The daily entries for 9/96 are replaced with a monthly entry.

+ The entry for the month is compiled using the data in the CMOP MASTER DATABASE file (#552.4), not by totaling the daily entries in the CMOP COST STATS file (#552.5).

If the entries are not the 30 most recent entries, the nightly compile job will delete cost job tasking entries in the CMOP OPERATIONS file (#554).

## Example: Initialize the Nightly Compile Job

```
Select CMOP System Management Menu Option: F acility Cost Management Select Facility Cost Management Option: I nitialize the Nightly Compile Job A job will be tasked every night which compiles yesterday's cost statistics. This job should be run during off hours. The suggested time is 1 o'clock in the morning. ** CAUTION: Check with IRM to make sure the job has not already been queued. Continue? N// Y ES Enter date/time: MAR 7,1997@01:00// <RET> (MAR 07, 1997@01:00) Task Queued ! Select Facility Cost Management Option: <RET>
```

## One Day Compile/Recompile Cost Data

## PSXCOST

This option compiles or recompiles cost data for a day specified by the user.

If a background job is queued to run or is running that compiles or purges cost data for the same date range you have selected or for dates that overlap your date range, you cannot queue your compile/recompile job.

## Example: One Day Compile/Recompile Cost Data

```
Select CMOP System Management Menu Option: F acility Cost Management Select Facility Cost Management Option: O ne Day Compile/Recompile Cost Data Date: T-1 (FEB 15, 1997) Are you sure? N// Y ES One Day data compilation queued from Feb 15,1997 to Feb 15, 1997. Requested Start Time: NOW// <RET> (FEB 15, 1997@08:20:39) Task Queued ! Select Facility Cost Management Option: <RET>
```

<!-- image -->

<!-- image -->

## Purge Cost Data

## PSXCOST

This option deletes data from the CMOP COST STATS file (#552.5). The data for the oldest date is deleted through a date specified by the user.

If a background job is queued to run or is running that compiles or purges cost data for the same date range you have selected or for dates that overlap your date range, you cannot queue your purge job until the background job has completed.

+ Data for three complete months will remain in the file.

## Example 1:  Purge Cost Data

```
Select CMOP System Management Menu Option: F acility Cost Management Select Facility Cost Management Option: P urge Cost Data Data for three complete months must remain in the cost file. JAN 1996 through JUN 1996 can be purged. Purge data from JAN 1996 through: 6 96 (JUN 1996) Purge from JAN 1996 to JUN 1996 Are you sure? N// Y ES Requested Start Time: NOW// <RET> (OCT 12, 1996@14:26:53) Task Queued ! Select Facility Cost Management Option: <RET>
```

## Example 2:  Purge Cost Data

```
Select CMOP System Management Menu Option: F acility Cost Management Select Facility Cost Management Option: P urge Cost Data The cost file contains data beginning with JUL 1996. Data for three complete months must remain in the cost file. No data can be purged. Select Facility Cost Management Option: <RET>
```

## Update Rx COST in Master Database

## PSXCOST

This option is a background job and is used to update the drug costs in the CMOP MASTER DATABASE file (#552.4).

## Example: Update Rx COST in Master Database

```
Select Facility Cost Management Option: U pdate Rx COST in Master Database Enter Begin Date : T-10 (FEB 27, 1997) Enter End Date : T (MAR 08, 1996)
```

```
Requested Start Time: NOW// <RET> (MAR 08, 1997@10:33:30) Job Queued Select Facility Cost Management Option: <RET>
```

## Archive Monthly CMOP Data

- Be sure to record the tape number on the tape label. The tape index number consists of two parts:

·

- 1)  29705 - The year/month being archived in FileMan format.
- 2)  1 - The sequence number of the tape being used. If more than one tape is required for a month then 297051 is incremented to 297052.
- Start and end times are provided so that you can compute how much time it will take to complete subsequent archives.
- When the data is archived, the original files are marked 'uneditable', so be sure you want to archive the data you have selected before you commit. You can archive the same data twice, though. In this instance the tape number will be the same except for the last digit which will be incremented by one.

## Example: Archive Monthly CMOP Data

```
Select Archive CMOP Data Option: A rchive Monthly CMOP Data ENTER MONTH/YEAR TO ARCHIVE :  02/97// <RET> CMOP MASTER DATABASE ARCHIVE Do you want to continue? :  (Y/N): NO// Y ES Select Tape Drive: [Select Tape Drive] //   REWIND? NO// Y (YES) CMOP MASTER DATABASE ARCHIVE       MAR 20,1997@08:45:56 Recording data on tape # 297021. Write this number on the tape label!! TRANSMISSION #      TOT ORDERS      TOT Rx's 521-1                        1             2 521-2                        7            15 521-3                        4             7
```

```
Total # of Transmissions Archived: 3 Total # of Rx's Archived         : 24 Total Bytes Archived             : 6054 Completed: MAR 20,1997@08:46   Closing Tape Device... Select Archive CMOP Data Option: <RET>
```

## Purge Archived CMOP Data

This option is used to purge data that has already been archived from the CMOP MASTER DATABASE file and the CMOP REFERENCE file.

## Example: Purge Archived CMOP Data

```
Select Archive CMOP Data Option: P urge Archived CMOP Data ENTER MONTH/YEAR TO PURGE :  11/97// <RET> CMOP MASTER DATABASE PURGE Total transmissions to be purged  : 2 Total orders to be purged         : 3 Total Rx's to be purged           : 6 Do you want to continue? :  (Y/N): NO// Y ES Transmission# 521-306 has been purged. Transmission# 521-307 has not been archived yet and may not be purged. Select Archive CMOP Data Option: <RET>
```

## Retrieve Archived CMOP Data

This option enables you to retrieve archived Rx's from tape.

## Example: Retrieve Archived CMOP Data

```
Select Archive CMOP Data Option: R etrieve Archived CMOP Data Enter Archived CMOP Transmission Number: 521-662 Enter Rx # to report or return for all: ALL// <RET> Select Printer:   [Select Print Device] Please mount tape #: 296031 Press Return when ready... <RET> Select Tape Drive: [Select Tape Drive] //   REWIND? NO// Y (YES) CMOP MASTER DATABASE ARCHIVE       MAR 21,1997@09:38:02 ARCHIVE REPORT FOR TRANSMISSION # 521-662 by CMOPPHARMACIST30,THREE  on MAR 21,1997 Status: CLOSED                       Trans D/T: MAR 22, 1996@09:18:49 Received D/T: MAR 22, 1996@09:19:11       Closed D/T: MAR 25, 1996@12:28:41 Processed D/T: MAR 25, 1996@11:21:54      Start Seq #: 7 End Seq #: 9                         Total Orders: 3 Total Rx's: 12                        Purge Status: PURGE COMPLETE Retrans:                           Orig Trans #: Division: BIRMINGHAM                   Site Name: BIRMINGHAM, AL. Sender: CMOPPHARMACIST30,THREE LABEL LOG: DATE PRINTED                  PRINTED BY -------------------------------------------------
```

<!-- image -->

## Interface Log Messages

```
+ XXX-XXX = Transmission # XXX-XXX-XXX = Order # xx = Query #
```

## ACK

```
ACK1 ACK message never received for order #XXX-XXX-XXX ACK2 EOT received with no terminator while waiting for ACK message ACK3 EOT received while waiting for ACK message ACK4 ENQ received with no terminator while waiting for ACK message ACK5 Unexpected character received: _$S(X>31:$C(X),1:)_ (_X_) while waiting for ACK message ACK6 Timeout Timer D reading ACK message ACK7 ACK message longer than 240 characters ACK8 ACK message did not end with ETX ACK9 ACK was null ACK10 Timeout reading ACK checksum ACK11 ACK checksum contained an invalid hex digit (_X_) ACK12 ACK checksum does not match ACK13 Order #XXX-XXX-XXX was rejected by CMOP ACK14 ENQ received with no terminator ACK15 MSA order # did not match XXX-XXX-XXX # expected
```

## Send Messages

```
Transmission # XXX-XXX finished downloading. Downloading Transmission # XXX-XXX Batch Header Rejected by Vendor for Transmission XXX-XXX Batch Header for transmission XXX-XXX rejected max times. DHCP Stopping interface. SND1 Timer A timeout after sending a line of text. SND2 ACK Received with bad block number after sending line of text, ASCII (_$G(X)_)  _X Expected ASCII (_$G(PSXBLK)_). SND3 NAK Received with no terminator after sending a line of text. SND4 NAK Received after sending a line of text. SND5 EOT Received with no terminator after sending a line of text. SND6 Garbage received after sending a line of text. (_X_) SND7 EOT Received, aborting send. SND8 Aborting Send.  Error processing order # XXX-XXX-XXX.  Text: _PSXTXT
```

```
SND9 ACK,_$G(PSXBLK)_ received with no terminator after sending a line of text. STP Stopping the interface now
```

## Master Messages

```
MST1 ENQ received with no terminator while Bidding for Master status. MST2 NAK received with no terminator while Bidding for Master status. MST3 ACK without 0 received while Bidding for Master status. MST4 Garbage received while Bidding for Master status. MST5 NAK received while Bidding for Master status. MST6 No response from CMOP while Bidding for Master Status MST7 Simultaneous bid for Master status by CMOP and DHCP. MST8 ACK received with no terminator while Bidding for Master status. MST9 CMOP won't respond, waiting 45 seconds to try again
```

## Query Messages

```
QUERY # XX initiated._$G(PSXQRYA) QUERY # XX completed._$G(PSXQRYA) QRY1 QRY message never received for Query # XX QRY2 EOT received with no terminator while waiting for QRY message QRY3 EOT received while waiting for QRY message QRY5 Unexpected character received: _$S(X>31: $C(X),1:)_ (_X_) while waiting for RY message QRY5 Unexpected character received: _X_ QRY6 Timeout Timer D reading RY message QRY7 QRY message longer than 240 characters QRY8 QRY message did not end with ETX QRY9 QRY was null QRY10 Timeout reading QRY checksum QRY11 QRY checksum contained an invalid hex digit (_X_) QRY12 QRY checksum does not match QRY13 Message # XX was rejected by OM CS QRY14 ENQ received with no terminator QRY15 MSA message ID did not match PSXQRYID #  expected QRY16 Block count greater than 7. QRY17 Wrong Block count received. QRY18 Maximum retries reached for receiving  message. QRY19 Maximum Rxs received, Query terminated. QRY20 No activity on line continuing to  monitor.
```

## Example of a CMoP Rx Label (Part 1)

(Bottle Label)

(Patient Copy)

(Pharmacist Copy)

VAMCANWWHEREAL35208-1234 500(205) 2911111(540/) 15096 SEPS.1994 Fa1o112 CMOPPATIENT25, ONE 45-6789 ASDIRECTO

YAMCANWVHEREAL35208-1234 500(205) 2911111(540/) 15096 SEP 5.1994 Fi1of12 CMOPPATIENT25,ONE 45-6789 ASDIRECTED

S00(540/) SEP 12,1994@14:57 10596 SEP 5.1994 Fa1of12 CMOPPATIENT25, ONE 45-6789 ASDIRECTED

CMOPPROVIDER, ONE Qty.10TAB IBUPROFEN 600 TAB

CMOPPROVIDER, ONE Cty.10 TAB 1BUPRCMOPPATIENT25,ONE 11Rfsremainprior to MARS,1995 COPAY Days Suppty.1

CMOPPROVIDER, ONE Gty.10TAB IBUPROFEN 600MG TAB Hig-----Lots Tech----RPh

600BEACON PHWY BRMINGHAM,AL 35208-1234

521-51272

886125

201EVERYWHEREDRIVE WELLINGTON,AL 35555

"CRITICALMEDICALSHIPMENT

Routing MAL Days supply.1 Cap:SAFETY Isd SEP 5,1994 Exp:MAR S,1995 LaFaN/A Pat.Stat.SC CInic1WEST

CMOPPATIENT25, ONE 201 EVERYWHERE DRIVE WELLINGTON,AL 3555S

dcteaddss change cnbackofthis om

[]Permanert

[]TempororyurtlL------

> **WARNING:** 1,3

""onoueis

521-51272

886425

Figure 2: Example of a CMOP Rx Label (Part 2)

## Example of a CMOP Rx Label (Part 2)

(Multi Rx Documents)

<!-- image -->

## Example of a CMoP Rx Label (Part 3)

(Patient Instructions)

CMOPPATIENT25,ONE 000-45-6789 K4724348904205

For Re filb le Presoiptions:

- 1 . You il receive a ccmp uter copy of each reflla ble presoription.
- 2 . Mail the com puter copy to the pharmaoy. using the bb el provided, as soon as p ossibke to receve: more medication.

## For No n-Refilbble Prescription:

- 1 . Acomp uter copy uil be se nt to yeu wit h a p hce for yo ur doetor t o sig n if he w ant s youto continue on the same medication.
- 2.Ple ase take the oomputer copyto your doctor for his signature OR he may write 2 new prescription on his own form.

## Example of a CMoP Rx Label (Part 4)

## Appendix C: Marking CMOP Drugs When a New Dispense Unit Is Required

The following method is used by several facilities to ease the process of marking CMOP drugs when a new dispense unit is required. There are several ways to complete this process and this is an example of just one method several sites have found helpful.

Table 1: Marking CMOP Drugs - Actions

| Action to be Taken                                                                                                                                                                             | Example                                                                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Select the CMOP Drug/Item Management option.                                                                                                                                                | Select CMOP Site Manager Menu Option: CMOP D rug/Item Management                                                                                                                                                                                                                    |
| 2. Next select the Drug Enter/Edit option.                                                                                                                                                     | Select CMOP Drug/Item Management Option: DRUG E nter/Edit                                                                                                                                                                                                                           |
| 3. Enter the old generic drug name. [The dispense unit is one box.]                                                                                                                            | Select DRUG GENERIC NAME: H3616 HOLLISTER #3616 5'S XA402 DRAINABLE POUCH/CONVEX BARRIER 1 1/2"                                                                                                                                                                                     |
| 4. Mark the drug as an outpatient pharmacy item.                                                                                                                                               | DO YOU WANT TO MARK THIS DRUG AS AN Outpatient Pharmacy ITEM? YES// Y (YES)                                                                                                                                                                                                         |
| 5. Edit the old drug name. [At this point, replace the first letter of the drug name with a lower case z plus the first letter of the drug name so it will not appear again unless requested.] | GENERIC NAME: HOLLISTER #3616 5'S// Replace H With zH Replace zHOLLISTER#3616 5'S                                                                                                                                                                                                   |
| 6. Exit the option by entering an up-arrow (^) at the 'MESSAGE' prompt. This will return you to the 'Select DRUG GENERIC NAME' prompt.                                                         | MESSAGE: DRAINABLE POUCH/CONVEX BARRIER 1 1/2" Replace ^                                                                                                                                                                                                                            |
| 7. Enter the new drug name. [Since this name will be overwritten with the VA Print name it can be named anything you prefer.]                                                                  | Select DRUG GENERIC NAME: HOL3616 ARE YOU ADDING 'HOL3616' AS A NEW DRUG (THE NTH)? Y (YES) DRUG NUMBER: 6528// <RET> DRUG VA CLASSIFICATION: <RET> DRUG FSN: <RET> DRUG NATIONAL DRUG CLASS: <RET> DRUG NON-FORMULARY: <RET> DRUG INACTIVE: <RET> DRUG MESSAGE: AVAILABLE AT CMOP. |
| 8. Again mark the new drug as an outpatient pharmacy item.                                                                                                                                     | DO YOU WANT TO MARK THIS DRUG AS AN Outpatient Pharmacy ITEM? NO// Y (YES)                                                                                                                                                                                                          |
| 9. Enter an up-arrow (^) to exit the option.                                                                                                                                                   | GENERIC NAME: HOL3616// ^ Select DRUG GENERIC NAME: ^                                                                                                                                                                                                                               |
| NEXT. . .                                                                                                                                                                                      |                                                                                                                                                                                                                                                                                     |

| Action to be Taken                                                                                                                                                                                                                                                                                      | Example                                                                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10. Enter VA FileMan. [If you do not have access to VA FileMan, give a list to your IRM contact displaying the name of the drug data is to be transferred from and the name of the drug you wish the data to be transferred to.]                                                                        | Select CMOP Drug/Item Management Option: ^^FM VA FileMan VA FileMan Version 20.0                                                                                           |
| 11. Select the Transfer Entries option.                                                                                                                                                                                                                                                                 | Select VA FileMan Option: TRANSFER ENTRIES                                                                                                                                 |
| 12. Then select the Transfer File Entries option.                                                                                                                                                                                                                                                       | Select TRANSFER OPTION: TRANSFER FILE ENTRIES                                                                                                                              |
| 13. Enter DRUG into the 'INPUT TO WHATFILE ' prompt.                                                                                                                                                                                                                                                    | INPUT TO WHAT FILE: DRUG (4046) TRANSFER FROM FILE: DRUG// <RET>                                                                                                           |
| 14. Enter the new drug in the 'TRANSFER DATA INTO WHICH DRUG' prompt.                                                                                                                                                                                                                                   | TRANSFER DATA INTO WHICH DRUG: HOL3616 [This is the new drug.]                                                                                                             |
| 15. Enter the name of the old drug at the 'TRANSFER FROM DRUG' prompt.                                                                                                                                                                                                                                  | TRANSFER FROM DRUG: zHOLLISTER#3616 [This is the old drug.]                                                                                                                |
| 16. Do not delete the old entry.                                                                                                                                                                                                                                                                        | WANT TO DELETE THIS ENTRY AFTER IT'S TRANSFERRED? NO// <RET> ...EXCUSE ME, THIS MAY TAKE A FEW MOMENTS...                                                                  |
| 17. **IMPORTANT** Do not update the pointers. [This will edit all the prescriptions on file to the new dru g , but will not edit the quantity.]                                                                                                                                                         | SINCE THE TRANSFERRED ENTRY MAY HAVE BEEN 'POINTED TO' BY ENTRIES IN THE 'DRUG' FILE,ETC., DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? NO// <RET> |
| NEXT. . .                                                                                                                                                                                                                                                                                               |                                                                                                                                                                            |
| 18. Again select the CMOP Drug/Item Management option.                                                                                                                                                                                                                                                  | Select CMOP Site Manager Menu Option: CMOP D rug/Item Management                                                                                                           |
| 19. Next select the Drug Enter/Edit option.                                                                                                                                                                                                                                                             | Select CMOP Drug/Item Management Option: DRUG E nter/Edit                                                                                                                  |
| 20. Enter the old drug name at the 'Select DRUG GENERIC NAME' prompt.                                                                                                                                                                                                                                   | Select DRUG GENERIC NAME: zHOLLISTER#3616 5'S                                                                                                                              |
| 21. Mark the drug as an outpatient pharmacy item.                                                                                                                                                                                                                                                       | DO YOU WANT TO MARK THIS DRUG AS AN Outpatient Pharmacy ITEM? NO// Y (YES)                                                                                                 |
| 22. Press return ( <RET> ) at the 'GENERIC NAME' prompt.                                                                                                                                                                                                                                                | GENERIC NAME: zHOLLISTER#3616 5'S Replace <RET>                                                                                                                            |
| 23. Enter a message. [This step is optional, but several medical centers have found it to be helpful for their Automated Data Processing Applications Coordinator (ADPAC.) When a drug is selected and this message appears, it should indicate to the user that the incorrect drug has been selected.] | MESSAGE:**INACTIVE**                                                                                                                                                       |

|   Action to be Taken | Action to be Taken                                                                                                                                                                                                                                                                                                   | Example                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                   24 | Enter ^SYNONYM to jump to the SYNONYM field.                                                                                                                                                                                                                                                                         | VA CLASSIFICATION: XA402// <RET> DEA,SPECIAL HDLG: S// ^SYNONYM                                                                                                                                                                                                                                                                                                                                                                                   |
|                   25 | Enter the @sign to delete all the synonyms from the old drug. [This is necessary to prevent calling up the old drug instead of the new one.]                                                                                                                                                                         | Select SYNONYM: H3616// @ SURE YOU WANT TO DELETE THE ENTIRE 'H3616'SYNONYM? Y (YES) SELECT SYNONYM: <RET> [This option has been abbreviated to save space.]                                                                                                                                                                                                                                                                                      |
|                   26 | At the 'INACTIVATE DATE' prompt, enter today's date to inactivate the old drug.                                                                                                                                                                                                                                      | INACTIVATE DATE: T (OCT 26, 1996)                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                   27 | Enter an up-arrow (^) at the 'REORDER LEVEL' prompt to take you back to the 'Select DRUG GENERIC NAME' prompt.                                                                                                                                                                                                       | REORDER LEVEL: ^                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                   28 | Select the new drug.                                                                                                                                                                                                                                                                                                 | Select DRUG GENERIC NAME: HOL3616 XA402 Available at CMOP                                                                                                                                                                                                                                                                                                                                                                                         |
|                   29 | Accept the default of YES at the 'DO YOU WANTTO MARKTHE DRUG AS AN Outpatient Pharmacy ITEM' prompt.                                                                                                                                                                                                                 | DO YOU WANT TO MARK THIS DRUG AS AN Outpatient Pharmacy ITEM? YES// <RET>                                                                                                                                                                                                                                                                                                                                                                         |
|                   30 | Continue to press return ( <RET> ) through the option.                                                                                                                                                                                                                                                               | GENERIC NAME: HOL3616// <RET> [This option has been abbreviated to save space.]                                                                                                                                                                                                                                                                                                                                                                   |
|                   31 | Edit the DISPENSE UNIT and the DISPENSE UNITS PER ORDER UNIT to reflect the requirements of the VA Print Name                                                                                                                                                                                                        | DISPENSE UNIT: BOX// EA DISPENSE UNITS PER ORDER UNIT: 1// 5                                                                                                                                                                                                                                                                                                                                                                                      |
|                   32 | Continue to press return ( <RET> ) to exit the option.                                                                                                                                                                                                                                                               | [This option has been abbreviated to save space.]                                                                                                                                                                                                                                                                                                                                                                                                 |
|                   33 | Select the CMOP Mark/Unmark (Single drug) option from the CMOP Drug/Item Management menu. The drug can now be marked for CMOP. It does not have to be matched to the NATIONAL DRUG file (#50.6) (NDF) if the old drug was matched. If it was not matched, you will have to match, verify, and merge the drug in NDF. | Select CMOP Drug/Item Management Option: CMOP M ark/Unmark (Single drug) This option allows you to choose entries from your drug file and helps you review your NDF matches and mark individual entries to send to CMOP. If you mark the entry to transmit to CMOP, it will replace your Dispense Unit with the VA Dispense Unit. In addition, you may overwrite the local drug name with the VA Print Name and the entry will remain uneditable. |
|                   34 | Enter the name of the new drug.                                                                                                                                                                                                                                                                                      | Select DRUG GENERIC NAME: HOL3616 XA402 Available at CMOP                                                                                                                                                                                                                                                                                                                                                                                         |

| Action to be Taken                                                                               | Example                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 35. Information will display for the new drug.                                                   | Local Drug Generic Name: HOL3616 ORDER UNIT: BX DISPENSE UNITS/ORDER UNITS: 5 DISPENSE UNIT: EA VA Print Name: POUCH,DRAINABLE,FIRST CHOICE H#3616 VA Dispense Unit: EA VA Drug Class: XA402 |
| 36. Enter YES to mark the drug to transmit to the CMOP.                                          | Do you wish to mark this drug to transmit to CMOP? Enter Yes or No: Y ES                                                                                                                     |
| 37. Enter a quantity dispense message to assist the user inputting the prescription information. | QUANTITY DISPENSE MESSAGE: 5EA = 1 BOX = 30 DAY SUPPLY                                                                                                                                       |
| 38. Enter YES to overwrite your local name.                                                      | Do you wish to overwrite your local name? Enter Yes or No: Y ES                                                                                                                              |
| 39. Press return ( <RET> ) to exit the CMOP Mark/Unmark (Single drug) option                     | Select DRUG GENERIC NAME: <RET>                                                                                                                                                              |
| NEXT. . .                                                                                        |                                                                                                                                                                                              |
| 40. Select the CMOP Drug/Item Management option.                                                 | Select CMOP Site Manager Menu Option: CMOP D rug/Item Management                                                                                                                             |
| 41. Select the Drug Enter/Edit option.                                                           | Select CMOP Drug/Item Management Option: DRUG E nter/Edit                                                                                                                                    |
| 42. Select the new drug generic name.                                                            | Select DRUG GENERIC NAME: HOL3616 POUCH,DRAINABLE,FIRSTCHOICE H#3616                                                                                                                         |
| 43. Mark the drug as an outpatient pharmacy item.                                                | DO YOU WANT TO MARK THIS DRUG AS AN Outpatient Pharmacy ITEM? NO// Y (YES)                                                                                                                   |
| 44. Press return ( <RET> ) at the 'GENERIC NAME' and 'MESSAGE' prompts.                          | GENERIC NAME: POUCH,DRAINABLE,FIRSTCHOICE H#3616 Replace <RET> MESSAGE: Available at CMOP// <RET>                                                                                            |
| 45. Enter a quantity dispense message to assist the user inputting the prescription information. | QUANTITY DISPENSE MESSAGE: 5EA = 1 BOX = 30 DAY SUPPLY                                                                                                                                       |
| 46. Exit the Drug Enter/Edit option.                                                             | VA CLASSIFICATION:XA402// <RET> DEA, SPECIAL HDLG:S// ^                                                                                                                                      |

## Appendix D: Flowchart for Processing a CMOP Prescription

A single line border indicates that the action is a MEDICAL CENTER ACTIVITY.

A double line border indicates that the action is a HOST CMOP ACTIVITY.

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

## Mail Messages Seen At Remote Medical Centers

1. The CMOP Activation Request message is generated when the Outpatient Pharmacy personnel submit a request to activate the medical center facility to do CMOP processing. This message only indicates that a user has selected to activate the site using the CMOP Site Manager option Activate/Inactivate CMOP Processing . Activation does not take place until a response is received from the CMOP host.
2. The CMOP Activation Approved message is returned from the CMOP facility when the CMOP Manager has approved the activation request. At the time of this message, an alert is also generated to all CMOP Manager key holders indicating the approval. At this time, the site becomes active for CMOP processing. Pharmacy users should sign off the system completely. The users should sign back onto the system after receiving the approval message to set up the appropriate CMOP/Outpatient site parameters. All prescriptions  processed after the site parameters are set up for CMOP will be screened and suspended for CMOP if transmission criteria is met.

```
Subj: CMOP Activation Request  [#38898] 11 Dec 96 10:03  5 Lines From: POSTMASTER (Sender: OPPHARMACIST2,THREE)  in 'IN' basket.   Page 1  **NEW** ------------------------------------------------------------------------------Request to activate. CMOP            :  LEAVENWORTH Requester       :  OPPHARMACIST2,THREE Action Date/Time:  DEC 11,1996@10:03
```

............................................An example of this message is shown on the following page ........................................

```
Subj: CMOP Activation Approved  [#33619] 09 Feb 97 11:50  6 Lines From: POSTMASTER                          in 'IN' basket.   Page 1  **NEW** ------------------------------------------------------------------------------Request to activate CMOP processing. CMOP             :  LEAVENWORTH Approving Offical:  CMOPPHARMACIST30,THREE Action Date/Time :  FEB 9,1997@11:50 Action           :  Approved
```

3. The CMOP Transmission Confirmation message is created when medical center CMOP transmission data has been handed to MailMan for delivery to the CMOP host facility. The subject line of the message will include the transmission number. Each successful transmission will generate a transmission confirmation message. If a user initiates a transmission and does not receive a transmission confirmation message, the medical center IRM Service should be contacted for assistance.

```
Subj: CMOP 521-737 Transmitted  [#38862] 09 Feb 97 08:15  8 Lines From: POSTMASTER (Sender: CMOPPHARMACIST30,THREE)  in 'IN' basket.   Page 1 **NEW** ------------------------------------------------------------------------------CMOP TRANSMISSION CONFIRMATION: Pharmacy Division    :  BIRMINGHAM Batch Number         :  521-737 Transmitted by       :  CMOPPHARMACIST30,THREE Date/Time            :  FEB 4,1997@08:15:48 Total orders/Rx's    :  1/5 Beginning order #    :  12 Ending order #       :  12
```

4. The CMOP Transmission Acknowledgment message is created by the host CMOP software when the data transmission is received, data is validated, and loaded into safe storage in the CMOP database. This message serves two purposes. Initially the message is delivered to the remote medical center to the PSXMAIL key holders to indicate that the CMOP has successfully received the data transmitted. The message is also delivered to the medical center CMOP server software and is used to file the date and time the data was received at the CMOP in the transmission entry in the CMOP TRANSMISSION file (#550.2). Receipt of both the Transmission Confirmation and the Transmission Acknowledgment messages for a single transmission confirm that the data transmitted and downloaded to the CMOP facility successfully.
5. The CMOP Error Encountered message is created when medical center CMOP transmission data has been handed to MailMan for delivery to the CMOP host facility. This message is a direct result of the CMOP software screening prescriptions suspended for CMOP during data transmission. If a problem is detected with a prescription selected for transmission, the prescription is not transmitted to the CMOP, but is noted in this message to the user to provide information to correct the problem . If the data is corrected as noted in this message, the prescription will be included in the next transmission. If the data problem is not corrected, the prescription will continue to be listed in this message each time a transmission is initiated. If the data is not corrected the prescription will never be transmitted. The CMOP Error Encountered message may be sent in varying formats depending on the data problems to be reported. Two examples are shown on the following page..

```
Subj: CMOP 521-524 Acknowledged.  [#34712] 04 Apr 95 17:17  8 Lines From: POSTMASTER                            in 'IN' basket.   Page 1  **NEW** ------------------------------------------------------------------------------CMOP TRANSMISSION ACKNOWLEDGEMENT: Pharmacy Division    :  BIRMINGHAM Batch Number         :  521-737 Transmitted by       :  CMOPPHARMACIST30,THREE Date/Time            :  FEB 4,1997@09:16:43 Total orders/Rx's    :  1/5 Beginning order #    :  12 Ending order #       :  12
```

## Example 1

```
Subj: CMOP Error Encountered  [#34392] 11 Dec 96 08:43  16 Lines From: POSTMASTER (Sender: CMOPPHARMACIST30,THREE)  in 'IN' basket.   Page 1 **NEW** ------------------------------------------------------------------------------An error has been encountered while processing prescription data for the Consolidated Mail Outpatient Pharmacy system. Date/Time    :  DEC 11,1996@08:43 Process      :  Data Validation Error Type   :  Invalid or missing data Description  :
```

```
RX #     Fill            Data Field 155465A    Original      Duplicate Rx Action Taken:  Rx's not sent to CMOP but still suspended for transmission. Recommended action:  Correct invalid data.
```

## Example 2

```
Subj: CMOP Error Encountered  [#38880] 05 Dec 96 14:14  21 Lines From: POSTMASTER (Sender: OPPHARMACIST2,THREE)  in 'IN' basket.   Page 1  **NEW** ------------------------------------------------------------------------------An error has been encountered while processing prescription data for the Consolidated Mail Outpatient Pharmacy system. Date/Time :  DEC 5,1996@14:14 Process  :  Transmission of Batch Data Error Type :  Invalid or missing data Description  : The following data is missing in the OUTPATIENT SITE file. State Street Address City Zip Code Area Code Phone Number Action Taken:  No data transmission will occur without this information. Recommended action:  Correct invalid data.
```

6. The CMOP Inactivation Notice message is generated when the Outpatient Pharmacy personnel selects to inactivate the medical center using the CMOP Site Manager menu option Activate/Inactivate CMOP Processing. Inactivation of CMOP processing is immediately effective . Users who do not sign off and then sign back onto the system when inactivation takes place will continue to do CMOP processing.
7. The CMOP Auto-Transmission Schedule message is generated when the Outpatient Pharmacy personnel use the Setup Auto-transmission option from the CMOP Site Manager menu to set up an automated transmission schedule to the CMOP host facility. The message notifies key holders that manual transmissions are not necessary to transmit data . Transmissions will begin automatically on the date and time indicated and continue for the selected frequency until the transmissions are unscheduled or modified.

```
Subj: CMOP Inactivation Notice  [#38894] 05 Dec 96 10:57  05 Lines From: POSTMASTER (Sender: OPPHARMACIST2,THREE)  in 'IN' basket.   Page 1  **NEW** ------------------------------------------------------------------------------Inactivation notice sent CMOP            :  LEAVENWORTH Requester       :  OPPHARMACIST2,THREE Action Date/Time:  DEC 5,1996@10:57
```

```
Subj: CMOP Auto-Transmission Schedule  [#38875] 11 Dec 96 09:32  7 Lines From: POSTMASTER (Sender: CMOPPHARMACIST30,THREE)  in 'IN' basket.   Page 1 **NEW** ------------------------------------------------------------------------------Auto-transmission Schedule. Auto-transmission Schedule.
```

```
Facility                       :  BIRMINGHAM, AL. Date Initiated                 :  Dec 11, 1996@09:32 Begin Automatic Transmissions  :  Dec 11, 1996@09:32 Number of days to transmit thru:  1 Scheduling Frequency (hours)   :  6 Initiating Official            :  CMOPPHARMACIST30,THREE
```

8. The CMOP Not Dispensed Rx List message is generated when release information indicates a prescription has been cancelled ( not dispensed ) by the vendor automated system. The prescription at the remote medical center is marked not dispensed in the PRESCRIPTION file (#52). The prescription is not marked with a status of Cancelled. The prescriptions may be filled locally, edited and re-suspended, or resubmitted for CMOP processing. Cancellation reasons are listed with the Rx number and other transmission information to assist the user in correcting the cause of the cancellation and re-submitting the prescription for filling by the CMOP. A separate message is created for each pharmacy division.

The CMOP Not Dispensed RX List message includes the standard symbols denoting additional information used by the Outpatient Pharmacy.

- Prescription numbers with a corresponding ePharmacy claim is marked with 'e'.
- Prescription numbers with a first party copay are marked with '$'.
9. The CMOP Acknowledgement not Received message is sent when a Transmission Acknowledgement message has not been received for a previous transmission after 24 hours. The CMOP software checks each transmission entry in the CMOP TRANSMISSION file (#550.2) 24 hours after the data is transmitted to ensure that the data was received at the CMOP host facility. If an acknowledgement date/time has not been filed for the transmission, this message reminds the key holders that the Transmission Acknowledgement message has not yet been received. The user should first contact the medical center IRM Service and request that the MailMan queue be checked to see if the transmission was sent. If it has been sent, the CMOP Manager at the host facility should be contacted to determine if there is another reason for the delay.

```
Subj: GENERIC CITY CMOP Not Dispensed Rx List, [#78218200] 07/15/14@23:01 15 lines From: POSTMASTER - POSTMASTER In 'IN' basket. Page 1 -------------------------------------------------------------------------------Not Dispensed Rx Report for the GENERIC CITY Division. The following prescriptions were not dispensed by the vendor: Patient: PSXPATIENT,ONE SSN: ###-##-#### Rx #: ########$e (REF5) Qty: 2 Trans #: 55403 Drug: CATHETER SILASTIC 22FR 30CC Transmitted under CMOP ID: XX923 Reason: NOT STOCKED CONTACT CMOP WITH USAGE Instructions: Prescriptions cannot be processed at CMOP for the reason listed above. Please review the prescription and take the appropriate action(s). If you have any questions, contact your CMOP contact person.
```

```
Subj: CMOP Acknowledgement not Received  [#38915] 20 FEB 97 15:56  3 Lines From: POSTMASTER                           in 'IN' basket.   Page 1 ------------------------------------------------------------------------------An acknowledgement message for transmission # 739 has not been received within the specified time.  Please contact the CMOP facility to see if there is a problem.
```

10. The CMOP Recovery Message is sent whenever a failed CMOP transmission is detected. This message is simply a notification message that the last transmission did not complete. CMOP recovery procedures were initiated to reset the data so that it will be transmitted in the next transmission for that division.
11. The e-Pharmacy CMOP Not Transmitted Rx List Message lists all e-billable prescriptions for which no response has been received from the third party payer. The  prescriptions listed have not been transmitted to CMOP, and remain in the CMOP queue.

```
Subj: CMOP Recovery Message BIRMINGHAM, AL.  [#3288] 21 Feb 97 10:29 CST 11 Lines From: <POSTMASTER@BAB.ISC-BIRM.XX.XXX>  in 'IN' basket.   Page 1  **NEW** ------------------------------------------------------------------------------The last CMOP transmission did not complete properly. The data for this transmission will be sent to the CMOP during the next transmission for that division. If you have scheduled auto transmissions for CMOP, please check to see that they are still scheduled for the correct time. This message is just a notification that problems were detected with the last transmission and that the data was sent to the CMOP facility for processing. If you are getting this message frequently, please contact your IRM staff. Otherwise there is not anything that you need to do.
```

The prescriptions remain in the CMOP queue and transmit when the response from the third party payer is received, or the non-billable issue is resolved. Examples of non-billable issues are prescriptions for sensitive medications that need Release of Information and prescriptions for nonbillable drugs (e.g. Over the Counter (OTC) products for CHAMPVA and TRICARE patients.)

The CMOP Not Transmitted Rx List Message displays the first date of the attempted submission, the number of times the prescription submission has been attempted and the date of the first unsuccessful transmit. The CMOP Not Transmitted Rx List message also displays the site name in the subject line.

```
Subj: ePHARMACY - CMOP Not TRANSMITTED RX List for site GENERIC CITY [#233739] 05/16/13@09:22 From: CMOP Package In 'IN' basket. Page 1 -------------------------------------------------------------------------------The prescriptions listed in this message did not transmit to CMOP for one of the reasons below: A response from the third party payer was not received OR The prescriptions are non-billable in VistA The prescriptions will remain in the CMOP queue and will transmit when the response from the third party payer is received, or the non-billable issue is resolved. Division: GENERIC CITY -------------------------------------------------------------------------------NOT TRANSMITTED RX#/Fill PATIENT(LAST4) DRUG 1ST DT #DAYS --------------------------------------------------------------------------------##########A/1  PSXPATIENT,ONE(####)   METOPROLOL TARTRATE 50M 07/19/14 3 ##########A/1  PSXPATIENT,ONE(####)   ALBUTEROL 100/IPRATRO 2 07/19/14 3 ##########A/1  PSXPATIENT,ONE(####)   FLUOCINONIDE 0.05% OINT 07/19/14 3 ##########A/10 PSXPATIENT,TWO(####) AMITRIPTYLINE 100MG TAB 07/19/14 3 Total GENERIC CITY: 2 Patients and 4 Prescriptions.
```

12. The Message for Discontinued CMOP Prescription lists discontinued prescriptions with a status of Transmitted or Retransmitted

## Example 1 Discontinued by a Background Process

When a CMOP prescription with a status of Transmitted or Retransmitted is discontinued by a background process to the Outpatient Pharmacy options, e.g. CPRS or Registration V. 5.3 packages, then an email will be sent to the PSX EXTERNAL DISPENSE ALERTS mail group (if no recipients are defined in the new mail group, the message will be sent to PSXCMOPMGR key holders) notifying that a prescription was just discontinued for that prescription and that the CMOP status for the prescription just discontinued was either Transmitted or Retransmitted.

```
Subj: TROY - DC Alert on CMOP Rx 123456789 TRANSMITTED  [#90494] 03/03/09@17:37 8 lines From: POSTMASTER  In 'IN' basket.   Page 1  *New* ------------------------------------------------------------------------Rx #: 123456789   Fill: 0 Patient: OUTPATIENT,DCONE (6660) Drug: TAMOXIFEN CITRATE 10MG TABS Rx Status: DISCONTINUED BY PROVIDER Processing Status: TRANSMITTED to CMOP on 02/27/09 Provider: OPPROVIDER, PROV ********    Please contact CMOP or take appropriate action    ******** Enter message action (in IN basket): Ignore// ------------------------------------------------------------------------
```

Example 2 Discontinued by a Foreground Pharmacy Process

When a CMOP prescription with a status of Transmitted or Retransmitted is discontinued by a foreground Pharmacy process due to a duplicate drug scenario that would trigger the duplicate to be discontinued, then the Processing Status field of the duplicate drug message is highlighted to alert the user.

<!-- image -->

In the above example, the line 'Processing Status: Transmitted to CMOP on 11/27/09' is bold. Mail Messages Seen At CMOP Facilities

1. The CMOP Activation Request message is generated when the Outpatient Pharmacy personnel submit a request to activate the medical center facility to do CMOP processing. This message is received at the host CMOP facility and notifies the CMOP Manager that a medical center is requesting to activate CMOP processing. An alert is also generated at the time of this message which requires a response from the CMOP Manager before the medical center can begin CMOP processing. This message is also used to update the CMOP NATIONAL SITE file (#552).

```
Subj: CMOP Activation Request  [#38899] 05 Dec 96 10:58  5 Lines From: POSTMASTER      in 'IN' basket.   Page 1  **NEW** ------------------------------------------------------------------------------Request to activate CMOP processing. Facility         :  BIRMINGHAM, AL. Requester        :  OPPHARMACIST2,THREE Request date/time:  DEC 5,1996@10:58
```

2. The CMOP Activation Approval message is sent to all holders of the key (PSXMAIL) at the host facility. This message notifies the manager that a medical center has now been activated to transmit data to the CMOP.
3. The CMOP Inactivation Notice is received by the CMOP host facility when the medical center inactivates CMOP processing. This message triggers an inactivation flag in the CMOP NATIONAL SITE file (#552). This flag indicates the medical center is inactive and data cannot be received from that medical center until a request to activate CMOP processing is received by the host and approved by the CMOP manager.
4. The CMOP (Batch Number) from (Site) Received message is created when data is downloaded successfully into the CMOP database files at the host facility. This message informs the CMOP personnel that a transmission has arrived and is ready to transfer to the automated vendor system. If the CMOP interface is running when this data is received, it is automatically scheduled and downloaded to the vendor system without delay.
5. The CMOP Review # (Batch Number) message is created on successful receipt of data from the medical center. This message provides a hard copy summary report of all prescriptions included in the transmission.

```
Subj: CMOP Activation Approval  [#38908] 11 Dec 96 10:28  6 Lines From: POSTMASTER (Sender: CMOPPHARMACIST30,THREE)  in 'IN' basket.   Page 1 **NEW** ------------------------------------------------------------------------------Request to activate CMOP processing. Facility         :  BIRMINGHAM, AL. Requester        :  CMOPPHARMACIST30,THREE Request date/time:  DEC 11,1996@10:28 Action taken     :  Approved
```

```
Subj: CMOP Inactivation Notice,BIRMINGHAM,AL. [#38895] 09 Feb 96 11:50 5 Lines From: POSTMASTER     in 'IN' basket.   Page 1  **NEW** ------------------------------------------------------------------------------Notice to Inactivate CMOP Processing. Facility               :  BIRMINGHAM, AL. Notifying Official     :  CMOPPHARMACIST30,THREE Notification date/time :  FEB 9,1996@11:50
```

```
Subj: CMOP 521-737 from BIRMINGHAM Received.  [#34543] 04 Feb 95 15:52 8 Lines From: POSTMASTER (Sender: CMOPPHARMACIST30,THREE)  in 'IN' basket.   Page 1 ------------------------------------------------------------------------------CMOP TRANSMISSION RECEIVED: Pharmacy Division    :  BIRMINGHAM Batch Number         :  521-737 Transmitted by       :  CMOPPHARMACIST30,THREE Date/Time            :  Feb 04, 1997@08:43:44 Total orders/Rx's    :  1/5 Beginning order #    :  12 Ending order #       :  12
```

```
Subj: CMOP Review # 521-737, BIRMINGHAM  [#34227] 11 Dec 97 08:43  9 Lines From: POSTMASTER                       in 'IN' basket.   Page 1  **NEW** ------------------------------------------------------------------------------BIRMINGHAM, AL.     521-737     TRANSMITTED: DEC 11,1996@08:43:29 ORD#     PATIENT          RX#          FILL          DRUG NAME ------------------------------------------------------------------------------12   CMOPPATIENT3,ONE   15525B         ORIG  ACETAMINOPHEN 325MG TAB 15634A         ORIG  AMINOPHYLLINE 500MG RTL SUPP 15631A         ORIG  AMITRIPTYLINE HCL 75MG TAB 15625A         ORIG  AMOXICILLIN 500MG CAP 11642K         ORIG  ISONIAZID 100MG TAB
```

6. The CMOP Auto-Transmission Schedule message is generated when the Outpatient Pharmacy personnel use the Setup Auto-transmission option on the Transmission Menu to set up an automated transmission schedule to the CMOP host facility. The message notifies the host CMOP personnel that the medical center has set up a schedule for automatic transmissions. Transmissions will begin automatically on the date and time indicated and continue for the selected frequency until the transmissions are unscheduled or modified. This information is recorded in the CMOP NATIONAL SITE file (#552).

```
Subj: CMOP Auto-Transmission Schedule, BIRMINGHAM, AL.  [#38881] 11 Dec 96 09:33  7 Lines From: POSTMASTER (Sender: CMOPPHARMACIST30,THREE)  in 'IN' basket.   Page 1 **NEW** ------------------------------------------------------------------------------Auto-Transmission Schedule. Facility                       :  BIRMINGHAM, AL. Initiating Official            :  CMOPPHARMACIST30,THREE Begin Automatic Transmissions  :  Dec 11, 1996@09:32 Scheduling Frequency (hours)   :  6 Number of days to transmit thru:  1
```
