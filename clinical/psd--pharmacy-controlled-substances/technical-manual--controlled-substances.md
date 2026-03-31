---
consolidated_title: "controlled substances technical manual"
app_code: PSD
doc_type: TM
master_source: "Controlled Substances Version 3 Technical Manual (Updated PSD*3*84)"
master_pub_date: March 1997
consolidated_from: 2 versions
prior_versions:
  - "Controlled Substances Version 3 Technical Manual (Updated PSD*3*89)"
---

<!-- image -->

# CONTROLLED SUBSTANCES (CS)

TECHNICAL MANUAL


March 1997

(Revised November 2018)

<!-- image -->

Product Development

########### 1 Revision History

The table below lists changes made since the initial release of this manual. Use the Change Pages document to update an existing manual or use the entire updated manual.

| **Date**   | **Revised Pages**    | **Patch Number**   | **Description**                                                                                                                                                                                                                                                                                                                                                                               |
|------------|----------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 11/2018    | 18  ,  40  ,  57     | PSD*3*84           | Updated the PSD DAILY LOG and PSD DAILY LOG TECH option descriptions to add the ^ALL CII DRUGS group name to search for all Schedule II drugs.  Updated the PSD OUTPATIENT option description to include a new prompt requiring pharmacists to enter a narcotic on-hand count that is confirmed against the VistA on-hand count.  Updated the number of routines in the CS package.  REDACTED |
| 06/2018    | 97                   | PSD*3*82           | Added NAOU Usage Report [PSD NAOU USAGE] option to the PSD TECH ADV key.  REDACTED                                                                                                                                                                                                                                                                                                            |
| 05/2013    | i, 18-18b,  45       | PSD*3*73           | Added two new options to Descriptions table.  Added two new reports to Production Reports Menu.  REDACTED                                                                                                                                                                                                                                                                                     |
| 05/2013    | i, 41c, 96-98        | PSD*3*76           | Page 41c is no longer necessary and has been removed.  Updated Glossary with description of patch’s new security key PSDRPH  REDACTED                                                                                                                                                                                                                                                         |
| 04/2011    | i, 15, 41-41c, 97-98 | PSD*3*71           | Clarified description of PSD TECH ADV key. Corrected option name in PSD TRAN entry. Made revision to PSD PHARM TECH option description.  REDACTED                                                                                                                                                                                                                                             |
| 05/2010    | 15, 41-41c, 97-98    | PSD*3*69           | Added description of patch’s new security key PSD TECH ADV, and options from the pharmacist menu added to the  *Technician (CS Pharmacy) Menu*  [PSD PHARM TECH], which allow holders of this new key to perform these additional functions.  REDACTED                                                                                                                                        |
| 08/08      | 24, 37, 39, 40       | PSD*3*64           | New menu options added to the Transfer Green Sheet Menu  REDACTED                                                                                                                                                                                                                                                                                                                             |
| 07/03      | 19-20, 44-45         | PSD*3*40           | Added two new reports associated with the Electronic Order Entry for Schedule II Controlled Substances project to the  *Production Repo*  rts [PSD PRODUCTION REPORTS] menu:  *Digitally Signed CS Orders Report*  [PSD DIGITALLY SIGNED ORDERS] and  *Digitally Signed OP Released Rx Report*  [PSD DIG. SIGNED RELEASED RX].                                                                |
| 04/03      | All                  | PSD*3*41           | Updated the manual to Standards. Added the  *CS Monitoring Menu*  options and routines.                                                                                                                                                                                                                                                                                                       |
| 03/97      |                      |                    | Original Released Technical Manual.                                                                                                                                                                                                                                                                                                                                                           |

&lt;This page is intentionally left blank.&gt;

**Table of Contents**

1.	0BIntroduction	1

1.1.	14BOrientation	1

1.2.	15BPackage Functional Description	2

1.3.	16BPackage Management	3

2.	1BImplementation and Maintenance	5

2.1.	17BInstallation	5

2.2.	18BSite Parameters	5

3.	2BRoutines	7

3.1.	19BDescriptions	7

3.2.	20BChecksum	7

3.3.	21BCallable Routines	8

3.4.	22BRoutine Mapping	8

4.	3BFile List	9

5.	4BArchiving and Purging	11

5.1.	23BArchiving	11

5.2.	24BPurging	11

6.	5BExternal Relationships	13

7.	6BInternal Relationships	15

8.	7BExported Options	15

8.1.	25BStand-Alone Options	15

8.2.	26BDescriptions	15

9.	8BPackage–Wide Variables	55

9.1.	27BPackage–Wide Variables	55

9.2.	28BPackage Variables	55

10.	9BResource Requirements	57

10.1.	29BHardware Requirements	57

10.1.1.	35BPrinting of Bar Codes	58

10.1.2.	36BHP LaserJet Printer	58

10.1.3.	37BOTC Printer	60

10.1.4.	38BKYOCERA Printer	60

10.1.5.	39BPortable Barcode Reader (TRAKKER 9440)	62

10.1.6.	40BInterfacing the TRAKKER 9440 to a VT-320 Auxiliary Port	66

11.	10BHow to Generate On-line Documentation	73

12.	11BAdditional Information	75

12.1.1.	41BFILE #58.2 AOU INVENTORY GROUP	75

13.	12BAppendix A Health Level 7 (HL7)	77

13.1.	30BIntroduction	77

13.1.1.	42BGeneral Description	77

13.1.2.	43BLower Level Protocols	77

13.1.3.	44BAcronyms	78

13.1.4.	45BTerms	78

13.1.5.	46BAssumptions and Dependencies	79

13.1.6.	47BReferences	79

13.2.	31BPurpose	79

13.3.	32BOverview	79

13.3.1.	48BStatement of Intent	79

13.3.2.	49BScope and Audience	79

13.4.	33BGeneral Specifications	80

13.4.1.	50BCommunication Protocol	80

13.4.2.	51BApplication Processing Rules	80

13.4.3.	52BMessage Types	80

13.4.4.	53BMessages	81

13.4.5.	54BFields	82

13.4.6.	55BMessage Segment Definitions:	83

13.5.	34BTransaction Specifications	91

13.5.1.	56BGeneral	91

13.5.2.	57BSpecific Transactions	91

14.	13BGlossary	93

## 0BIntroduction

The Controlled Substances V. 3.0 module provides functionality to monitor and track the receipt, inventory, and dispensing of all controlled substances. This module provides the pharmacy with the capability to define a controlled substance location and a list of controlled substances to maintain a perpetual inventory. The capability for pharmacy personnel to receive a controlled substance order automatically, updating the quantity on hand and receipt history is also provided. Nursing personnel are provided with the capability to request orders for controlled substances via on-demand requests. Pharmacy may dispense controlled substances via the software automating all necessary documents (VA FORMs 10-2321 and 10-2638) to complete an order request. The software provides functionality to address returns to stock, destructions, and transfers between locations; log outpatient prescriptions and order cancellations; report Automated Management Information System (AMIS) and cost data; and maintain perpetual inventory balances.

### 14BOrientation

This manual is divided into sections addressing such items as routines, files, security, options, etc. to provide a method of quick reference for the Site Manager and Information Resources Management (IRM) and Automated Data Processing (ADP) staff. For more detailed information about the package functionality, refer to the Controlled Substances V. 3.0 User Manual.

Within this documentation, several notations need to be outlined.

- Menu options will be italicized.

Example: *Controlled Substance Balances Report* indicates a menu option.

- Screen prompts will be denoted with quotation marks around them.

Example: “Select INPATIENT SITE NAME” indicates a screen prompt.

- Responses in bold face indicate what the user is to type in.

Example: Okay to Continue? No// **Y** ES.

- Text centered between arrows represents a keyboard key that needs to be pressed in order for the system to capture a user response or move the cursor to another field. **&lt;Enter&gt;** indicates that the Enter key (or Return key on some keyboards) must be pressed. **&lt;Tab&gt;** indicates that the Tab key must be pressed.

Example:  Press **&lt;Tab&gt;** to move the cursor to the next field.

Press **&lt;Enter&gt;** to select the default.

<!-- image -->

- **Note** : Indicates especially important or helpful information.

<!-- image -->

- Options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option.
<!-- image -->

Example:  The PSDMGR key is required. Please contact the Pharmacy Supervisor.

- **?** , **??** , **???** One, two, or three question marks can be entered at any of the prompts for on-line help.  One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

- ^ Up Caret (arrow or a circumflex) and pressing **&lt;Enter&gt;** can be used to exit the current option.

### 15BPackage Functional Description

The Controlled Substances V. 3.0 software process usually consists of the following functions:

- Pharmacy set up of narcotic vaults and nursing wards (Narcotic Area Of Use - NAOUs).

- Monitors/tracks the receipt, inventory, and dispensing of controlled substances.

- Allows management inspections to automatically identify discrepancies in stock levels.

- Allows nursing to place orders for controlled substances via on-demand requests.

- Allows pharmacy to dispense controlled substance drugs, update on-hand balances, automate VA FORM 10-2321, and print VA FORM 10-2638.

- Review VA FORM 10-2638 when completed and returned to pharmacy.

- Provides AMIS and cost reporting data.

- Maintains perpetual inventory balances.

- Provides ability to return to stock, transfer between locations, cancel orders, and log outpatient prescriptions.

- Automates current inventory requirements, which allows Department of Veterans Affairs Medical Centers (VAMCs) to detect discrepancies or diversions of controlled substances, thereby improving overall drug accountability.

- Display history of actions taken on controlled substances orders.

### 16BPackage Management

This package does not impose any additional legal requirements on the user, nor does it relieve the user of any legal requirements. Names and social security numbers used in the examples are fictitious.

&lt;This page is intentionally left blank.&gt;

## 1BImplementation and Maintenance

### 17BInstallation

For installation of the Controlled Substances (CS) V. 3.0 software package, please refer to the Installation Guide.

### 18BSite Parameters

The following is the site parameter that is used in defining the CS module for each site.

- **IS SITE SELECTABLE FOR CS**

How should the IS SITE SELECTABLE FOR CS parameter be answered? This parameter was created because Inpatient Medications V. 5.0, Auto Replenishment/Ward Stock V. 2.3, and Controlled Substances V. 3.0 share the INPATIENT Site file (#59.4). Therefore, this parameter will screen out inpatient site names that are not used by the Controlled Substances V. 3.0 module. For every entry in this file, it should be determined if the site name should be shown to the users of the Controlled Substances V. 3.0 package. If the site name should be shown, enter **1** or **YES** for this parameter, otherwise, enter **0** or **NO** .

&lt;This page is intentionally left blank.&gt;

## 2BRoutines

### 19BDescriptions

Use the following option to print routine descriptions:

Example: Print Routine Descriptions

Select Systems Manager Menu Option: **PRO** grammer Options

Select Programmer Options Option: **ROU** tine Tools

Select Routine Tools Option: **FIR** st Line Routine Print

PRINTS FIRST LINES

routine(s) ?   &gt; **PSD***

searching directory ...

routine(s) ?   &gt;

(A)lpha, (D)ate ,(P)atched, OR (S)ize ORDER: A// **&lt;Enter&gt;**

Include line 2? NO// **&lt;Enter&gt;**

DEVICE: HOME// **&lt;Enter&gt;**

### 20BChecksum

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1. Any comment line with a single semi-colon is (presumed) to be followed by comments and only the line tag will be included.

2. Line 2 will be excluded from the count.

3. The total value of the routine is determined by taking, excluding the exception, as noted above, and multiplying the ASCII value of each character by its position on the line being checked.

Example: Checksum Option

&gt;D CHECK^XTSUMBLD

routine(s) ?   &gt; **PSD***

searching directory . **&lt;Enter&gt;** ..

routine(s) ?   &gt; **&lt;Enter&gt;**

**-----------------------------------------** ***example follows*** **-----------------------------------------**

Example: Checksum Option (continued)

PSDNMBA        	value = 7638815

PSDNMKY        	value = 5224255

PSDNMPR        	value = 7345943

PSDNMRP        	value = 7410643

PSDNMSP        	value = 6584930

PSDNMU         	value = 6690662

PSDNMWE        	value = 10976237

### 21BCallable Routines

None of the Controlled Substances V. 3.0 routines are designed for calling outside of the package.

### 22BRoutine Mapping

There are no specific recommendations for routine mapping.

## 3BFile List

The following files are owned by the Controlled Substances V. 3.0 package:

- 58.82. CS ORDER STATUS
- 58.83. CS COMPLETION STATUS
- 58.84. DRUG ACCOUNTABILITY TRANSACTION TYPE
- 58.85. CS WORKSHEET
- 58.86. CS DESTRUCTION
- 58.87. CS CORRECTION LOG
- 58.88. CS IRL PROGRAM
- 58.89. CS ERROR LOG

59.4	INPATIENT SITE

For a complete list of the files and templates exported by the CS module use the *Build File Print* option, which is a Kernel Installation and Distribution System (KIDS) option.

&gt; **D ^XQ1**

Select OPTION NAME: **XPD MAIN** Kernel Installation &amp; Distribution System

Select Kernel Installation &amp; Distribution System Option: **Ut** ilities

Select Utilities Option: **BUI** ld File Print

Select BUILD NAME: **CONTR** OLLED SUBSTANCES 3.0

DEVICE: *[Select Print Device]*

<!-- image -->

## 4BArchiving and Purging

### 23BArchiving

At present, the CS module does not provide for the archiving of its data.

### 24BPurging

**Auto-Purging**

There is a background job, which should be scheduled through TaskMan to run each night at a convenient time. The routine should run nightly; therefore the rescheduling frequency is 1D. The purpose of the option is to purge the CS WORKSHEET file (#58.85). This file is the holding area for CS order requests pending pharmacy processing. The data should remain in the file until the orders have been received in an NAOU or cancelled by pharmacy. Once the order is received on an NAOU or cancelled, the data is purged from the system through this background job.

Using the TaskMan Manager’s *Schedule/Unschedule Options* [XUTM SCHEDULE] option, select the *Purge CS WORKSHEET File* [PSD PURGE] option. At the “QUEUED TO RUN AT WHAT TIME:” prompt, enter **T@** followed by the time the job is to begin. The time should be one that does not conflict with system backup. At the “RESCHEDULING FREQUENCY:” prompt, enter **1D** . The “DEVICE FOR QUEUED JOB OUTPUT” prompt should remain blank since this is a background job.

#### 70BExample:  How to Schedule a TaskMan Task

Select Systems Manager Menu Option: **TASK** Manager

Select Task Manager Option: **SCH** edule/Unschedule Options

Select OPTION to schedule or reschedule: **PSD PURGE**

QUEUED TO RUN AT WHAT TIME: **T@2200**

DEVICE FOR QUEUED JOB OUTPUT: **&lt;Enter&gt;**

RESCHEDULING FREQUENCY: **1D**

QUEUED TO RUN ON VOLUME SET: *[At this prompt, select the Volume Set name that the option should run on.]*

SPECIAL QUEUEING: **&lt;Enter&gt;**

Select OPTION to schedule or reschedule: **&lt;Enter&gt;**

&lt;This page is intentionally left blank.&gt;

## 5BExternal Relationships

The Controlled Substances V. 3.0 module relies on, at least, the following external packages to run effectively:

Package	Minimum version needed

Kernel	8.0

VA FileMan	21.0

MailMan	7.1

Nursing	2.5

*	Outpatient Pharmacy	6.0

Auto Replenishment/Ward Stock	2.2

Inpatient Medications	4.0

Drug Accountability	2.0

Integrated Billing	2.0

Health Level 7 (HL7)	1.6

To run this module, the New Person file (#200), Ward Location file (#42), Drug file (#50), PHARMACY SYSTEM file (#59.7), INPATIENT SITE file (#59.4), and Prescription file (#52) files are needed. The system does not need to be taken down, but the CS and Drug Accountability menus must be made **unavailable** to the users. This is now handled within the KIDS install process.

Patches XU*8*26 and XU*8*44 must be installed to support the witness identification for Nurse dispensing functionality and the HL7 interface.

Please note that patch PSGW* 2.2*2 should be installed to ensure compatibility between AR/WS V. 2.2 and Controlled Substances V. 3.0.

* 	Patch PSO*6*134 should be installed to ensure compatibility between 	Outpatient V. 6.0 and Controlled Substances V. 3.0.

This package is required to support the Health Level 7 (HL7) Interface to Narcotic dispensing Equipment Systems.

&lt;This page is intentionally left blank.&gt;

## 6BInternal Relationships

All of the Controlled Substances V. 3.0 package options have been designed to stand-alone. Each option requires the use of the package-wide variable PSDSITE that is set as users enter the package. Even though **all** options are independently invoked, users will be repeatedly asked to select an Inpatient Site (if there are two or more sites that are flagged as selectable for CS use) if top-level CS menus do not contain the following entry and exit code in the OPTION file (#19):

**ENTRY ACTION:  I '$D(PSDSITE) D ^PSDSET**

**EXIT ACTION :  K PSDSITE**

The entry and exit code should not be included on submenus in order to preserve the variable PSDSITE.

## 7BExported Options

### 25BStand-Alone Options

All of the CS package options have been designed to stand alone. All pharmacy personnel may be assigned the *Controlled Substances Menu* [PSD MENU] as a menu option. Pharmacy managers may be assigned the *CS Monitoring Menu* [PSD NM MENU] option. All nursing personnel, using the CS software, may be assigned the *Controlled Substances Nurses’ (CS) Menu* [PSD NURSE MENU] as a menu option. Controlled Substances inspectors may be assigned the *Controlled Substances Inspector Menu* [PSD INSPECTOR MENU] option and the *CS Monitoring Menu* [PSD NM MENU] option. Each option utilizes the package-wide variable PSDSITE that is set as users enter the package.

Controlled Substances (CS) V. 3.0 package technicians may be assigned the *Technician (CS Pharmacy) Menu* [PSD PHARM TECH] option. They may also be assigned the PSD TECH ADV security key. With the PSD TECH ADV security key, technicians can perform the functions from the pharmacist menu that have been added to the *Technician (CS Pharmacy) Menu* [PSD PHARM TECH]. The CS technician may perform all the *Outpatient Rx’s* menu functions except releasing prescriptions.

### 26BDescriptions

| Option Name                   | Routine   | Menu Text / Description                                                                                                              |
|-------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------|
| PSD AMIS                      | PSDAMIS   | *AMIS Report*  This option provides the pharmacy with AMIS report information by NAOU.                                               |
| PSD BALANCE ADJUSTMENT REVIEW | PSDADJD   | *Balance Adjustment Report*  This report allows the selection of drugs and a date range for which to review all balance adjustments. |

| Option Name                                | Routine    | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD BALANCE ADJUSTMENTS  **Lock:**  PSDMGR | PSDADJ     | *Balance Adjustments*  This option is used to review or enter adjustments needed to correct the balance of a drug.  CS drugs not dispensed with a VA FORM 10-2638 returned to stock, or returned to manufacturer and held for destruction are deducted from the vault on-hand amount using this option.                                                                                                                                                                                                                                                                                                                                                                                                    |
| PSD BALANCE INITIALIZE                     | PSDADJI    | *Initialize Balance at Setup*  This option will be used at package initialization only.  It provides pharmacy a method of entering on-hand balances for CS drugs stocked within their dispensing vaults.  The drugs will be listed alphabetically, displaying narcotic breakdown and package size for each. This option should be used only when the CS package is ready to be "turned on" for production use.                                                                                                                                                                                                                                                                                             |
| PSD COMPLETE GS                            | PSDGSRV    | *Complete Green Sheet*  Pharmacy uses this option to complete a reviewed Green Sheet.  Green Sheets with no discrepancies, math errors, drugs returned to stock, and drugs holding for destruction, associated with this Green Sheet, are processed utilizing this option.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PSD CORRECT EXISTING GS                    | EN2^PSDCOR | *Existing Green Sheets Correction*  This option allows the pharmacy supervisor access to make corrective actions on CS orders.  The CS software allows pharmacy to add existing Green Sheets active orders on an NAOU at package setup.  These orders may be tracked using the CS software. Sometimes one of these existing Green Sheets may be incorrectly entered in the software.  Using this option, the pharmacy supervisor may delete this erroneous existing Green Sheet.  An entry in the CS CORRECTION LOG file (#58.87) will be created to log a history of all corrective actions.                                                                                                              |
| PSD CORRECT GS STATUS                      | EN3^PSDCOR | *Error on Completed Green Sheets*  This option allows the Pharmacy Supervisor to correct the completed status of a Green Sheet from COMPLETED - REVIEWED to COMPLETED - PENDING PROBLEM RESOLUTION.  An entry in the CS CORRECTION LOG file (#58.87) will be created to track this error.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PSD CORRECT STATUS                         | EN1^PSDCOR | *Correct Order Status - GS Ready for Pickup*  This option allows the Pharmacy Supervisor access to correct the order status of certain CS orders.  Sometimes nursing may erroneously flag a Green Sheet ready for pharmacy pickup.  Using this option, the Pharmacy Supervisor may change the Green Sheet order status from COMPLETED - GREEN SHEET READY FOR PICKUP to DELIVERED - ACTIVELY ON NAOU to correct this problem.  An entry in the CS CORRECTION LOG file (#58.87) will be created to log a history of all corrective actions.                                                                                                                                                                 |
| PSD CORRECTION LOG                         |            | *Correction Menu*  This menu option allows the pharmacy supervisor access to make corrective actions on CS orders. An entry in the CS CORRECTION LOG file (#58.87) will be created to log a history of all corrective actions.  **Menu Items:**  PSD CORRECT STATUS  *Correct Order Status - GS Ready for Pickup*  PSD CORRECT EXISTING GS  *Existing Green Sheets Correction*  PSD EDIT/CANC VER ORD  *Edit/Cancel Verified Orders*  PSD CORRECT GS STATUS  *Error on Completed Green Sheets*  PSD ERR/ADJ PENDING REPORT  List Pending Errors/Adjustments Logged by TRAKKER  PSD ERR/ADJ RESOLVED REPORT  *Print Resolved Errors/Adjustments Log*  PSD ERR/ADJ EDIT  *Enter Error/Adjustment Resolution* |

| Option Name                             | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD CORRECTION LOG REPORT               | PSDCORP   | *Correction Log Report*  This report lists all corrective actions logged for a selected date range.  This report may be generated by order status changes or by Green Sheet deletions.                                                                                                                                                                                                                                  |
| PSD COST REPORTS                        | PSDCOST   | *Cost Reports*  This option provides pharmacy cost reporting data for CS drugs, by NAOU, for a specified date range.                                                                                                                                                                                                                                                                                                    |
| PSD CP TRANSACTION REVIEW               | PSDREVC   | *Control Point Transaction Review*  Use this option to review the receipt transactions processed for a selected control point transaction number.                                                                                                                                                                                                                                                                       |
| PSD CS PRESCRIPTIONS REPORT             | PSDDSOR   | *Controlled Substance Prescriptions Report*  This option provides a report of digitally signed orders that have been filled for Schedules I-V controlled substances. The report is for a date range with the option of including discontinued and/or expired orders and various sort criteria. For example, list by patient, by provider, by drug, and by schedule, etc. It is an 80-column report queued to a printer. |
| PSD DAILY LOG                           | PSDACT    | *Daily Activity Log*  (in lieu of VA FORM 10-2320)  The Daily Activity Log lists all transactions for a CS dispensing site (vault).  It includes a forwarding balance on each transaction.  This document may be generated for a single drug, some drugs, all Schedule II drugs (by typing the ^ALL CII DRUGS group name), or ALL drugs within a specified date range.                                                  |
| PSD DAILY LOG TECH  **Lock:**  PSD TECH | PSDACT    | *Daily Activity Log*  (in lieu of VA FORM 10-2320)  The Daily Activity Log lists all transactions for a CS dispensing site (vault).  It includes a forwarding balance on each transaction.  This document may be generated for a single drug, some drugs, all Schedule II drugs (by typing the ^ALL CII DRUGS group name), or ALL drugs with a specified date range.                                                    |

| PSD DEA LIST          | PSDEA    | *DEA Special Handling List*  This report alphabetically lists the drug name, DEA Special Handling, and NDC data for all drugs within the DRUG file (#50) marked for CS package use.  This report will be helpful in researching drugs incorrectly marked for CS package use.                                                                                                                                           |
|-----------------------|----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD DEA SUBOXONE      | PSDSUBOX | *DEA DATA – Waived Practitioner Report*  This report provides a list of patients that were prescribed with Suboxone drugs. Two views are available, one with details, and another with just the counts of Suboxone patients per prescriber.                                                                                                                                                                            |
| PSD DEST DRUGS REPORT | PSDESTP  | *Destroyed Drugs Report*  This report lists, alphabetically by drug; all destroyed controlled substances, within a narcotic dispensing site, for a given period of time. Pharmacy Supervisor certifying the destruction, quantity destroyed, and date destroyed is also included on this report. The report may be generated for a single drug, several drugs, or ALL drugs stocked within a specific dispensing site. |

&lt;This page is intentionally left blank.&gt;

| Option Name                          | Routine     | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Menu Text / Description   |
|--------------------------------------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|
| PSD DEST NON-CS DRUG                 | PSDESTO     | Hold a CS Drug (No Inventory Update)  This option allows Pharmacy Supervisors to place a CS VA drug, from the DRUG file (#50), on hold for destruction. When using this option, the CS inventory balance will not be updated. A CS DESTRUCTION file (#58.86) entry is made and can be tracked through the CS software.                                                                                                                                                                                                                                                                                                 |                           |
| PSD DEST TEXT DRUG                   | PSDESTF     | *Non-VA Drug Placed on Hold for Destruction*  This option allows the Pharmacy Supervisors to place a non-VA drug, not existing in the DRUG file (#50), on hold for destruction.  A CS DESTRUCTION file (#58.86) entry is made and can be tracked through the CS software.                                                                                                                                                                                                                                                                                                                                              |                           |
| PSD DESTROY DEA41                    | PSDEA41     | *DEA Form 41 Destroyed Drugs Report*  This report lists information on destroyed CS that is required in completing the DEA Form 41.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |                           |
| PSD DESTROY DRUGS  **Lock:**  PSDMGR | PSDEST      | *Destroy a Controlled Substances Drug*  This option provides the supervisor ability to enter the destruction information for any CS drug being destroyed.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                           |
| PSD DESTROY MENU                     |             | *Destructions Menu*  This menu allows Pharmacy Supervisors to maintain the necessary records when destroying a CS drug.  **Menu Items:**  PSD DESTROY DRUGS  *Destroy a Controlled Substances Drug*  PSD DEST NON-CS DRUG  Hold a CS Drug (No Inventory Update)  PSD DEST TEXT DRUG  *Non-VA Drug Placed on Hold for Destruction*                                                                                                                                                                                                                                                                                      |                           |
| PSD DESTRUCTION HOLDING              | PSDHRPT     | *Destructions Holding Report*  This report lists all CS drugs being held for destruction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                           |
| PSD DIGITALLY SIGNED ORDERS          | PSDDSOR     | *Digitally Signed CS Orders Report*  Only functional when DEA regulations are revised and PKI functionality can be fully implemented nationally. Sites opting to activate PKI functionality for pharmacy can use this option to retrieve and list all digitally signed orders for controlled substances.                                                                                                                                                                                                                                                                                                               |                           |
| PSD DIG. SIGNED RELEASED RX          | PSDDSOR2    | *Digitally Signed OP Released Rx Report*  Only functional when DEA regulations are revised and PKI functionality can be fully implemented nationally. Sites opting to activate PKI functionality for pharmacy can use this option to retrieve and list all released digitally signed orders for controlled substances.                                                                                                                                                                                                                                                                                                 |                           |
| PSD DISPENSE TO NDES                 | PSDNDES     | *Narcotic Dispensing Equipment Orders*  This option is for dispensing from Pharmacy to narcotic dispensing equipment systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |                           |
| PSD DISPENSE W/O GS                  | PSDDFP      | Pharmacy Dispense without (VA FORM 10-2638)  This option provides pharmacy the ability to dispense CS drugs from a dispensing site without generating the VA FORM 10-2638. Drugs dispensed using this option will not be displayed on the Inspector's Log for controlled substances for the NAOUs.  These drugs will be included on the Pharmacy Dispensing Report and the Daily Activity Log.                                                                                                                                                                                                                         |                           |
| PSD DISPENSING MENU                  |             | *Dispensing Menu*  This menu contains access to all options associated with the dispensing of controlled substances.  **Menu Items:**  PSD WORKSHEET PRINT  *Print CS Dispensing Worksheet*  PSD WORKSHEET DISPENSING  *Fill/Dispense CS Orders from Worksheet*  PSD PRINT 2321  Dispensing/Receiving Report (VA FORM 10-2321)  PSD PRINT 2638  Green Sheet - Print (VA FORM 10-2638)  PSD DISPENSE W/O GS  Pharmacy Dispense without (VA FORM 10-2638)  PSD REPRINT MENU  *Reprint Reports Menu*  PSD LABEL DRUG/NUMBER  Label for Dispensing (Barcode)  PSD DISPENSE TO NDES  *Narcotic Dispensing Equipment Orders* |                           |
| PSD DRUG CHECK                       | PSDMAPU     | *Check Stocked Drugs for CS Use*  This option queues a background job to check all ACTIVE drugs stocked, within an ACTIVE NAOU, for use with the CS package. If a stocked drug has been unmarked for CS use the drug will then be inactivated.  At job completion a MailMan message will be sent listing any drug discrepancies.                                                                                                                                                                                                                                                                                       |                           |
| PSD DRUG FILE DATA                   | PSDCSL      | *Drug File Stats for CS Drugs*  This report lists the drug name, order unit, price per order unit, dispense unit, dispense units per order unit, and price per dispense unit.  These statistics are compiled from the DRUG file (#50) and may be used when loading stock drugs into a NAOU. All drugs marked for CS package use will print on this report.                                                                                                                                                                                                                                                             |                           |
| PSD DRUG LOC EDIT                    | PSDCODE     | *Enter/Edit CS Drug Location Codes*  This option allows editing of the codes used to define the locations of stocked drugs in NAOU or in the pharmacy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                           |
| PSD DRUG LOC PRINT                   | CODE^PSDPRT | *List CS Drug Location Codes*  This report will list the codes used to define the location of drugs stocked in NAOU or in the pharmacy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                           |
| PSD DRUG RECEIPT HISTORY             | PSDREVD     | *Drug Receipt History*  This option is used to review all receipts processed over a selected time range for a selected drug.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |                           |
| PSD EDIT/CANC VER ORD                | PSDEVO      | *Edit/Cancel Verified Orders*  This option allows the Pharmacy Supervisor access to edit or cancel a verified order.  The order must be edited or cancelled prior to being delivered to the NAOU.  A verified order may be edited only once.  It must be cancelled and re-entered if a second edit is required.  Quantity, manufacturer, lot number, and expiration date are the only fields in which edits can be made.                                                                                                                                                                                               |                           |

| Option Name                                                                            | Routine       | *Menu Text / Description*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD EDIT/CANC VER ORD RPT                                                              | PSDEVOR       | *Edited Verified Orders Report*  This report lists all verified orders that have been edited or cancelled within a specified date range.  Data listed includes pharmacy dispensing # (Green Sheet #), date edited, drug, type of action (edited or cancelled), original quantity, new quantity, and name of the pharmacist. The manufacturer, lot #, or expiration date fields will also be listed if edited.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PSD EMERGENCY ORDER REPORT                                                             | PSDEM         | *Unscheduled Order Report*  A report to show by drug or by NAOU a list of unscheduled orders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PSD ENTER/EDIT MENU                                                                    |               | *Enter/Edit Menu*  This menu contains the enter/edit options associated with setting up the files for the CS module.  **Menu Items:**  PSD INVEN TYPE EDIT  *Inventory Types - Enter/Edit*  PSD DRUG LOC EDIT  *Enter/Edit CS Drug Location Codes*  PSD NAOU EDIT  *Create/Edit the Narcotic Area of Use*  PSD STOCK DRUG EDIT  *Stock CS Drugs - Enter/Edit*  PSD MFG/LOT/EXP DATE EDIT  *Manufacturer, Lot #, and Exp. Date - Enter/Edit*  PSD NARC EDIT  Narcotic Breakdown Unit/Package Size - Enter/Edit  PSD NAOU INV GROUP EDIT  *NAOU Inventory Group - Enter/Edit*  PSD MARK  *Mark/Unmark Drugs for controlled substances use*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PSD ERR/ADJ EDIT  **Lock:**  PSD ERROR                                                 | PSDERD        | *Enter Error/Adjustment Resolution*  This option allows designated Pharmacy Supervisors the ability to enter a resolution comment for each error or adjustment created when using the barcode TRAKKER.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PSD ERR/ADJ PENDING REPORT  **Lock:**  PSD ERROR                                       | PSDERP        | List Pending Errors/Adjustments Logged by TRAKKER  This option lists all pending errors/adjustments logged from the barcode TRAKKER for a specific Dispensing Site within a given time frame.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PSD ERR/ADJ RESOLVED REPORT  **Lock:**  PSD ERROR                                      | PSDERCP       | *Print Resolved Errors/Adjustments Log*  This report prints a listing of all resolved errors/adjustments logged by the barcode TRAKKER for a specific Dispensing Site within a given time frame.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PSD EXISTING GS                                                                        | PSDEXGS       | *Add Existing Green Sheets at Setup*  This option provides pharmacy the ability to enter existing Green Sheets and active orders on an NAOU, at package setup.  These orders may be tracked through the CS software.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PSD EXP REPORT                                                                         | PSDEXP        | *Expiration Date Report*  This option will print a Controlled Substances Expiration Date Report for a single NAOU, several NAOUs, or ALL NAOUs.  This report may be sorted by DATE/DRUG/NAOU or by DATE/NAOU/DRUG.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PSD GS DISCREPANCY REPORT                                                              | PSDCRP        | *Completed Green Sheet Discrepancy Report*  This report lists all Green Sheets with a completion status of MATH ERROR, GREEN SHEET NOT SIGNED BY NURSE, or OTHER - REFERRED TO SUPERVISOR.  This report may be printed for a single NAOU, several NAOUs, or ALL NAOUs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PSD GS HISTORY                                                                         | PSDGSH        | *Green Sheet History*  The Green Sheet history provides pharmacy with a detailed account of every transaction affecting this VA FORM 10-2638.  This history may be displayed to the user's screen or directed to a printer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PSD GS LISTING                                                                         | PSDGSL        | *Listing of Green Sheet Log*  This option numerically lists all Green Sheets for a given date range or for a given Green Sheet number range.  The logs list Green Sheet number, date dispensed, and current status.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PSD GS TRANS NOT RECD (NAOU)                                                           | PSDNBT        | Transferred Green Sheets - Pending NAOU Receipt  This report lists all Green Sheets that have been transferred from an NAOU and are pending receipt in another NAOU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PSD GS TRANSFER (NAOU) REPORT                                                          | PSDNTR        | *Green Sheet Transfer Between NAOUs Report*  This report lists all Green Sheets transferred and received between NAOUs for a given date range.  This report may be printed for a single NAOU, several NAOUs, or ALL NAOUs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PSD INACTIVATE NAOU                                                                    | PSDNACT       | *Inactivate NAOU*  This option will allow a user to inactivate an NAOU.  An inactivation date may be entered for a future time.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PSD INACTIVATE NAOU STOCK DRUG                                                         | PSDNSTK       | *Inactivate NAOU Stock Drug*  This option is used to inactivate a drug that is currently on a NAOU stock list.  Drugs should not be deleted, but simply inactivated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PSD INFUSION MENU                                                                      |               | *Infusion Order Processing Menu*  This menu contains the infusion order/entry and transferring a Green Sheet options associated with the IV pharmacist processing a CS infusion order.  **Menu Items:**  PSD INFUSION O/E  *Infusion Order Entry*  PSD NURSE TRANSFER GS  *Transfer Green Sheet and Drug to another NAOU*  *Transfer GS for PCA/Infusion Signed Out to Patient*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PSD INFUSION O/E                                                                       | PSDORV        | *Infusion Order Entry*  The IV pharmacist uses this option to electronically request CS drugs used in IV orders. Only infusion orders requiring the VA FORM 10-2638 should be requested using this option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PSD INSP LOG BY RECD DATE                                                              | PSDRLOG       | *Inspector's Log by Rec'd Date*  This report lists all dispensing transactions for Narcotic Area of Use received within a given date range.  The data includes dispensing number, drug name, date received, quantity received, expiration date (if available), blanks for quantity on hand, and a signature blank for verification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PSD INSP PLACE HOLD                                                                    | PSDCSI        | *Place Green Sheet on Hold*  This option allows the CS Inspector to place a Green Sheet on hold for review.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PSD INSP REMOVE HOLD                                                                   | PSDRSI        | *Remove Green Sheet from Hold*  This option allows the CS Inspector to remove a Green Sheet from hold.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PSD INSPECTOR MENU  **Action:**  I '$D(PSDSITE) D ^PSDSET  **Exit Action:**  K PSDSITE |               | *Controlled Substances Inspector Menu*  This menu contains all options associated with a CS inspection.  **Menu Items:**  PSD INSP PLACE HOLD  *Place Green Sheet on Hold*  PSD INSP REMOVE HOLD  *Remove Green Sheet from Hold*  PSD PRINT INSPECTOR LOG  *Inspector's Log for Controlled Substances*  PSD PRT GS INSP HOLD  *Under Inspector's Review - Green Sheets*  PSD INVEN SHEET PRT  *Inventory Sheet Print*  PSD INSP LOG BY RECD DATE  *Inspector's Log by Rec'd Date*  PSD IRL INSP MENU  *Barcode TRAKKER for CS Inspections*  PSD GS HISTORY  *Green Sheet History*  PSD NAOU BALANCE REPORT  *Narcotic Count - Shift Report*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PSD INVEN SHEET PRT                                                                    | PSDBALI       | *Inventory Sheet Print*  This option prints an Inspector's Sheet, which is used to inventory on-hand amounts within a pharmacy-dispensing site (vault).  This form lists current on-hand amounts and provides a blank space for the inspector to list actual on-hand counts.  A signature line is included on each page. This sheet may be generated for one drug, some drugs, or ALL drugs. The drugs are listed alphabetically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PSD INVEN TYPE EDIT                                                                    | PSDNVT        | *Inventory Types - Enter/Edit*  This option will edit the entries in the AOU INVENTORY TYPE file (#58.16) used to classify NAOU drugs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PSD INVEN TYPE PRINT                                                                   | INVEN^PSDPRT  | *Print Inventory Types*  Use this option to print the entries in the AOU INVENTORY TYPE file (#58.16) used to classify NAOU stocked drugs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PSD IRL INSP DATA                                                                      | UPLOAD^PSDUP3 | Send Inspections Inventory TRAKKER Data to DHCP  This option contains the access to upload or send narcotic vault inspections inventory from the barcode TRAKKER to  **V**  *IST*  **A**  .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PSD IRL INSP MENU                                                                      |               | *Barcode TRAKKER for CS Inspections*  This menu contains the options associated with performing narcotic vault inspections using the barcode TRAKKER device.  **Menu Items:**  PSD IRL INSPECTOR INV  Load Software and Insp. Inventory into TRAKKER  PSD IRL INSP DATA  *Send Inspections Inventory TRAKKER Data to DHCP*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PSD IRL INSPECTOR INV                                                                  | PSDUP3        | Load Software and Insp. Inventory into TRAKKER  This option contains the access to download an IRL program to the TRAKKER and download the narcotic inspections inventory to the TRAKKER. This option is used for the Narcotic Inspectors only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PSD IRL INV DATA                                                                       | UPLOAD^PSDUP2 | *Send Vault TRAKKER Inventory Data to DHCP*  This option contains the access to upload or send vault inventory from the barcode TRAKKER to  **V**  *IST*  **A**  .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PSD IRL INV MENU                                                                       |               | *Barcode TRAKKER for Inventory*  This menu contains the options associated with performing narcotic vault inventories using the barcode TRAKKER device.  **Menu Items:**  PSD IRL VAULT INV  *Load Software and Inventory into TRAKKER*  PSD IRL INV DATA  *Send Vault TRAKKER Inventory Data to DHCP*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PSD IRL VAULT INV                                                                      | PSDUP2        | *Load Software and Inventory into TRAKKER*  This option contains the access to download an IRL program to the TRAKKER and download the vault inventory to the TRAKKER, in one step. This option is used for pharmacy service only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PSD LABEL DRUG/NUMBER                                                                  | PSDLBL        | Label for Dispensing (Barcode)  This option allows pharmacy to print the dispensing number/drug barcode label that is attached to the drug delivered to the NAOUs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PSD LABEL INSP                                                                         | PSDLBLI       | *Inspectors Label Print*  This option allows the inspector or Pharmacy Supervisor to print the CS Inspector's barcode labels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PSD LABEL PHARM  **Lock:**  PSDMGR                                                     | PSDLBL3       | *Print Pharmacist ID Labels*  This option allows Pharmacy Supervisors to print the pharmacists barcoded ID label. This label is scanned when pharmacists inventory CS drugs in the dispensing vault.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PSD LABEL VAULT                                                                        | PSDLBL1       | *Barcode Drug Labels for Vault*  This option allows pharmacy to print the barcode labels for dispensing-site (vault) stocked drugs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PSD MARK                                                                               | PSDAPU        | Mark/Unmark Drugs for Controlled Substances Use  This option provides the ability to mark/unmark entries in the DRUG file (#50) for use with the CS package.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PSD MENU  **Action:**  I '$D(PSDSITE) D ^PSDSET  **Exit Action:**  K PSDSITE           |               | *Controlled Substances Menu*  This menu contains access to all options associated with the CS module of the Pharmacy software.  **Menu Items:**  PSD MGR  *Supervisor (CS) Menu*  PSD TRANSACTION MENU  *Pharmacist Menu*  PSD PRODUCTION REPORTS  *Production Reports*  PSD PHARM TECH  *Technician (CS Pharmacy) Menu*  PSD LABEL VAULT  *Barcode Drug Labels for Vault*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PSD MFG REPORT PRINT                                                                   | PSDPMFG       | *Manufacturer and Narcotic Information Report*  This report prints an alphabetical listing of all ACTIVE drugs within an ACTIVE NAOU that have been defined in the DRUG ACCOUNTABILITY STATS file (#58.8). This report lists NAOU, drug name, manufacturer, lot #, expiration date, narcotic breakdown unit, and narcotic package size.  This report may be sorted alphabetically by NAOU, then drug name or drug name, then NAOU. The user may select one NAOU, several NAOUs, or all NAOUs to print.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PSD MFG/LOT/EXP DATE EDIT                                                              | PSDMFG        | *Manufacturer, Lot #, and Exp. Date - Enter/Edit*  This option allows the user to enter or edit manufacturer, lot #, and expiration dates for stocked drugs in an NAOU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PSD MGR  **Lock:**  PSDMGR                                                             |               | *Supervisor (CS) Menu*  This menu contains the options used for the NAOU set-up and maintenance.  **Menu Items:**  PSD SETUP  *Set Up CS (Build Files) Menu*  PSD MGR REPORTS  *Management Reports*  PSD BALANCE ADJUSTMENTS  *Balance Adjustments*  PSD CORRECTION LOG  *Correction Menu*  PSD EXISTING GS  *Add Existing Green Sheets at Setup*  PSD LABEL PHARM  *Print Pharmacist ID Labels*  PSD DESTROY MENU  *Destructions Menu*  PSD LABEL INSP  *Inspectors Label Print*  PSD EMERGENCY ORDER REPORT  *Unscheduled Order Report*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PSD MGR REPORTS                                                                        |               | *Management Reports*  This option contains all reports or lists associated with drug accountability for narcotics.  **Menu Items:**  PSD NOT DELIVERED  *Orders Filled Not Delivered*  PSD PEND VAULT ORDERS  *Pending CS Orders by Dispensing Site*  PSD DESTRUCTION HOLDING  *Destructions Holding Report*  PSD EDIT/CANC VER ORD RPT  *Edited Verified Orders Report*  PSD GS TRANSFER (NAOU) REPORT  *Green Sheet Transfer Between NAOUs Report*  PSD GS TRANS NOT RECD (NAOU)  Transferred Green Sheets - Pending NAOU Receipt  PSD GS DISCREPANCY REPORT  *Completed Green Sheet Discrepancy Report*  PSD CORRECTION LOG REPORT  *Correction Log Report*  PSD NAOU USAGE  *NAOU Usage Report*  PSD DESTROY DEA41  *DEA Form 41 Destroyed Drugs Report*  PSD DEST DRUGS REPORT  *Destroyed Drugs Report*  PSD AMIS  *AMIS Report*  PSD GS LISTING  *Listing of Green Sheet Log*  PSD COST REPORTS  *Cost Reports*  PSD PRT GS INSP HOLD  *Under Inspector's Review - Green Sheets*  PSD BALANCE ADJUSTMENT REVIEW  *Balance Adjustment Report*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PSD NAOU ADJ                                                                           | PSDADJN       | *Balance Adjustments – NAOU*  This option may be used to adjust the balance of controlled substances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PSD NAOU BAL INITIAL                                                                   | PSDADJIN      | *Initialize NAOU Drug Balance*  This option may be used to establish beginning balances for drugs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PSD NAOU BALANCE REPORT                                                                | PSDBAN        | *Narcotic Count - Shift Report*  This report will show the balance for one or all drugs on a ward.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PSD NAOU EDIT  **Lock:**  PSD PARAM                                                    | PSDEN         | *Create/Edit the Narcotic Area of Use*  This option allows the user to initially define the NAOU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PSD NAOU INV GROUP EDIT                                                                | PSDGEN        | *NAOU Inventory Group - Enter/Edit*  This option allows the user to enter and edit inventory groups.  These groups define a cluster of NAOUs.  For each of these NAOUs, one or more inventory types may be defined.  This lets pharmacy detail a list of standard NAOUs and inventory types that can be easily selected when doing inventory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PSD NAOU INV GROUP PRINT                                                               | PSDGPR        | Inventory Group List (80 column)  This option prints a list of the currently defined NAOU inventory groups with their associated inventory types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PSD NAOU INV GROUP SORT                                                                | PSDGSK        | *Sort NAOUs in Inventory Group*  This option allows the user to change the order in which the NAOUs will sort within an inventory group.  NAOUs should sort in the order that they will be visited.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PSD NAOU PRINT                                                                         | NAOU^PSDPRT   | *Show Narcotic Area of Use*  This option allows the user to print the NAOUs/Location Type/Primary Dispensing Site created in the Create/Edit the Narcotic Area of Use option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PSD NAOU USAGE                                                                         | PSDNU         | *NAOU Usage Report*  This report will print an NAOU drug usage report for a selected date range.  The report may be sorted by drug (one, some, or ALL) or by NAOU (one, some, or ALL).  A detailed list of orders, including the pharmacy dispensing # (Green Sheet #), date filled, quantity, and who ordered the drug will be printed.  Summary totals by order and quantity are also generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PSD NARC EDIT                                                                          | PSDNARC       | Narcotic Breakdown Unit/Package Size - Enter/Edit  This option allows the user to enter or edit narcotic breakdown unit and narcotic package size for stocked drugs in an active NAOU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PSD NM CS ADJ                                                                          | PSDNMBA       | *CS Balance Adjustments Report*  This option lists Drug Accountability Transactions in which the CS vault inventory balance was adjusted manually during the date range entered.  The adjuster and reason will display on the report for the Narcotic Inspectors and Pharmacy Managers to review regularly for appropriateness and authorization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PSD NM MENU                                                                            |               | *CS Monitoring Menu*  This standalone menu contains CS Monitoring reports to help facilitate the monitoring of CS and Schedule II narcotics. The menu should be assigned to the appropriate Narcotic Inspectors and Pharmacy Managers at the site. IA 3882 - Gives permission for Kernel's  *Option Access by User*  [XUOPTWHO] option to be included on this menu.  **Menu Items:**  PSD NM SECURITY KEY  *CS Application Security Key Report*  PSD NM CS ADJ  *CS Balance Adjustments Report*  PSD NM RX SAME PERSON  *CS RXs by Same Person Report*  PSD NM RX REPRINT  *Label Reprint for CS RXs Report*  XUOPTWHO  *Option Access By User*  PSD NM RX PARTIAL  *Partial Request for CS RXs Report*  PSD NM RX WITHOUT VA  *Patients Without VA Visit Report*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PSD NM RX PARTIAL                                                                      | PSDNMPR       | *Partial Request for CS RXs Report*  This option lists CS prescriptions for which a prescription partial fill was requested.  An individual could partially fill the same prescription more than once and be diverting prescription drugs.  Narcotic Inspectors and Pharmacy managers should monitor this activity. This report should be queued to run during non-peak hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PSD NM RX REPRINT                                                                      | PSDNMRP       | *Label Reprint for CS RXs Report*  This option lists CS prescriptions for which a prescription label reprint was requested.  An individual could fill the same prescription more than once and be diverting prescription drugs. Narcotic Inspectors and Pharmacy managers should monitor this activity. This report should be queued to run during non-peak hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PSD NM RX SAME PERSON                                                                  | PSDNMSP       | *CS RXs by Same Person Report*  This option lists CS prescriptions that were entered, finished and released by the same person for the date range entered. Different pharmacists in the prescription filling process normally perform these functions.  Although frequently necessary on off-shifts and weekends, CS Inspectors and Pharmacy Managers should monitor this activity. This report should be queued to run during non-peak hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PSD NM RX WITHOUT VA                                                                   | PSDNMWE       | *Patients Without VA Visit Report*  This option lists patients that receive prescriptions but have not had a VA clinic visit within one year of a RX release date for the date range entered.  Excluding RXs released on the same day as a discharge and within a user defined discharge date range.  Patients in Fee Basis and Aid and Attendance programs may be included on the list and should be reviewed.  This lists represents a potential diversion tactic that could be employed to prevent detection and suspicion. This report should be queued to run during non-peak hours.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PSD NM SECURITY KEY                                                                    | PSDNMKY       | *CS Application Security Key Report*  This option lists holders of the PSJ RPHARM and/or PSDMGR security keys. Holders of these keys have the ability to override discrepancies, make CS vault inventory adjustments and transfer medications between vaults.  The list requires routine monitoring and validation for accuracy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PSD NOT DELIVERED                                                                      | PSDFND        | *Orders Filled Not Delivered*  This option generates a list of all CS orders filled from the pharmacy-dispensing site (vault) but not yet delivered to the NAOUs.  A summary total sorted by drug is also generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PSD NOT DELIVERED NURSE  **Lock:**  PSJ RNURSE                                         | PSDFND        | Orders Filled Not Delivered  This option generates a list of all CS orders filled from the pharmacy-dispensing site (vault) but not yet delivered to the NAOUs.  A summary total sorted by drug is also generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PSD NURSE DEFECTIVE DOSE                                                               | PSDRF4        | *Record Defective Dose*  When a nurse discovers a damaged drug that cannot be dispensed to a patient, this option may be used to record the wasting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PSD NURSE DELAYED DISPENSE                                                             | PSDRFS        | *Delayed Sign Out Dose for Patient*  This option may be used when there is computer down time and it is necessary to sign out doses that were already given to patients.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PSD NURSE DISP MENU  **Action:**  D ^PSDRFD  **Exit Action:**  K NAOU,NAOUN            |               | *Sign Out Menu*  This is a menu to assist nurses in tracking doses signed out for patients.  **Menu Items:**  PSD NURSE DISPENSING  *Sign Out Dose for Patient*  PSD PAT ID LIST  *Patient ID List Print*  PSD NURSE DISP REPORT  *Activity Report*  PSD NURSE WASTE  *Record Delayed Wastage*  PSD NURSE NOT GIVEN  *Not Given, Return to Stock*  PSD NURSE DEFECTIVE DOSE  *Record Defective Dose*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PSD NURSE DISP REPORT                                                                  | PSDPAT        | *Activity Report*  This option provides a detailed and summary listing of activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PSD NURSE DISPENSING                                                                   | PSDRF         | *Sign Out Dose for Patient*  This option is designed for signing out doses via a radio frequency device.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PSD NURSE GS MENU                                                                      |               | *Green Sheet Menu*  This menu contains options for handling green sheets.  **Menu Items:**  PSD REC GS  *Receipt of Controlled Substance from Pharmacy*  PSD READY GS FOR PICKUP  *Complete a Green Sheet - Ready for Pickup*  PSD GS HISTORY  *Green Sheet History*  PSD NURSE TRANS GS MENU  *Transfer Green Sheet Menu*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PSD NURSE HELP                                                                         | PSDHELP       | *Help Online*  Use this option to view or print online help.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PSD NURSE INFUSION                                                                     | PSDORNV       | *Infusion or PCA Syringe Order Entry For Patient*  This option is for ordering an infusion or PCA syringe for a specific patient.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PSD NURSE MENU  **Action:**  I '$D(PSDSITE) D ^PSDSET  **Exit Action:**  K PSDSITE     |               | *Controlled Substances Nurses' (CS) Menu*  This menu provides nurses access to all options associated with requesting and receiving CS drugs from pharmacy.  **Menu Items:**  PSD NURSE SHIFT LOG  *Ward (NAOU) Drug History*  PSD NURSE HELP  *Help Online*  PSD NURSE DISP MENU  *Sign Out Menu*  PSD NURSE ORDER MENU  *Ordering Menu*  PSD NURSE GS MENU  *Green Sheet Menu*  PSD NAOU BALANCE REPORT  *Narcotic Count - Shift Report*  PSD REC GS  *Receipt of Controlled Substance from Pharmacy*  PSD NURSE ONLINE COUNT  *Verify Count*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PSD NURSE NOT GIVEN                                                                    | PSDRFR        | *Not Given, Return to Stock*  This option may be used when a dose is not given to a patient and must be returned to stock.  This option must be used within one hour of the last dispensed dose (by the nurse that dispensed that dose).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PSD NURSE ONLINE COUNT                                                                 | PSDADJC       | *Verify Count*  This option may be used to verify and correct balances.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PSD NURSE ORDER MENU                                                                   |               | *Ordering Menu*  This menu contains options for ordering and checking on orders.  **Menu Items:**  PSD ORDER ENTRY  *CS Order Entry For Ward*  PSD PEND NAOU ORDERS  *Pending CS Orders Report for an NAOU*  PSD NOT DELIVERED NURSE  *Orders Filled Not Delivered*  PSD NURSE PRIORITY ORDER CHECK  *Check on Priority Orders*  PSD NURSE INFUSION  *Infusion or PCA Syringe Order Entry For Patient*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PSD NURSE PRIORITY ORDER CHECK                                                         | PSDEM4        | *Check on Priority Orders*  This option will check the status of Priority Orders that Pharmacy has filled today for a selected NAOU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PSD NURSE REC TRANSFER GS                                                              | PSDNTT        | *Receive Green Sheet &amp; Drug from another NAOU*  This option provides nurses the ability to receive CS drugs and their associated Green Sheet from another NAOU.  The transferring of CS drugs between NAOUs requires two processing steps.  Step 1 - Transfer Green Sheet and Drug to another NAOU  Step 2 - From an NAOU - Receive Green Sheet Transfer &amp; Drug                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PSD GS REC PCA/INF FOR PATIENT                                                         | PSDNTTPC      | *Receive GS for PCA/Infusion Signed Out to Patient*  This option provides nurses the ability to receive Green Sheets for PCA/Infusions from another NAOU.  The transferring of these Green Sheets between NAOUs requires two processing steps.  Step 1 – Transfer GS for PCA/Infusion Signed  Out to Patient  Step 2 – Receive GS for PCA/Infusion Signed  Out to Patient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PSD NURSE REPRINT 2321                                                                 | PSDRPT        | Reprint Transfer Between NAOUs (VA FORM 10-2321)  Nurses may reprint the transfer between NAOUs form (in lieu of VA FORM 10-2321) for any Green Sheet and drug transferred from their NAOU.  The form may be reprinted only if the transferred Green Sheet and drug has not been received into the NAOU receiving the transfer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PSD NURSE SHIFT LOG                                                                    | PSDNSCL       | *Ward (NAOU) Drug History*  Use this report to list all ACTIVE CS orders currently on a specific NAOU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PSD NURSE SUPR MENU                                                                    |               | *Nursing Supervisor Menu*  This is a menu with special options to support the signing out of CS.  **Menu Items:**  PSD NAOU BAL INITIAL  *Initialize NAOU Drug Balance*  PSD NAOU ADJ  *Balance Adjustments - NAOU*  PSD PAT INQUIRY  *Patient/Location Inquiry*  PSD EMERGENCY ORDER REPORT  *Unscheduled Order Report*  PSD EXP REPORT  *Expiration Date Report*  PSD PAT ID LIST  *Patient ID List Print*  PSD NURSE DELAYED DISPENSE  *Delayed Sign Out Dose for Patient*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PSD NURSE TRANS GS MENU                                                                |               | *Transfer Green Sheet Menu*  Use this menu to transfer and receive Green Sheets between NAOUs.  **Menu Items:**  PSD NURSE TRANSFER GS  *Transfer Green Sheet and Drug to another NAOU*  PSD NURSE REC TRANSFER GS  *Receive Green Sheet &amp; Drug from another NAOU*  PSD GS TRANS PCA/INF PATIENT  *Transfer GS for PCA/Infusion Signed Out to Patient*  PSD GS REC PCA/INF FOR PATIENT  *Receive GS for PCA/Infusion Signed Out to Patient*  PSD NURSE REPRINT 2321  Reprint Transfer Between NAOUs (VA FORM 10-2321)  PSD GS TRANS NOT RECD (NAOU)  *Transferred Green Sheets - Pending NAOU Receipt*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PSD NURSE TRANSFER GS                                                                  | PSDNTF        | *Transfer Green Sheet and Drug to another NAOU*  This option provides nurses the ability to transfer CS drugs and their associated Green Sheet to another NAOU.  The transferring of CS drugs between NAOUs requires two processing steps.  Step 1 - Transfer Green Sheet and Drug to another NAOU  Step 2 - From an NAOU - Receive Green Sheet Transfer &amp; Drug                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PSD GS TRANS PCA/INF PATIENT                                                           | PSDNTFPC      | *Transfer GS for PCA/Infusion Signed Out to Patient*  This option provides nurses the ability to transfer Green Sheets for PCA/Infusions to another NAOU.  The transferring of these Green Sheets between NAOUs requires two processing steps.  Step 1 – Transfer GS for PCA/Infusion Signed Out to Patient  Step 2 – Receive GS for PCA/Infusion Signed Out to Patient                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PSD NURSE WASTE                                                                        | PSDRFW        | *Record Delayed Wastage*  This option can be used when a dispensed dose needs to be wasted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PSD ON-HAND                                                                            | PSDBAL        | *List On-Hand Amounts*  This option lists current on-hand amounts for drugs stocked in a pharmacy-dispensing site (vault).  The report is selectable by one drug, some drugs, or ALL drugs. The drugs are listed alphabetically to the user's screen or a selected printer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| PSD ON-HAND TECH  **Lock:**  PSD TECH                                                  | PSDBAL        | *List On-Hand Amounts*  This option lists current on-hand amounts for drugs stocked in a pharmacy-dispensing site (vault).  The report is selectable by one drug, some drugs, or ALL drugs.  The drugs are listed alphabetically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PSD ORDER ENTRY                                                                        | PSDORN        | *CS Order Entry For Ward*  Use this option to electronically request CS drugs from pharmacy requiring the VA FORM 10-2638.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PSD OUTPATIENT                                                                         | PSDOPT        | *Outpatient Rx's*  This option provides pharmacy the ability to log outpatient prescriptions from their CS dispensing vault.  The pharmacist will select an outpatient prescription and the software will display the most recently filled Rx. It will display new, refill, and partial prescriptions. The option includes a failsafe requiring users to enter the correct on-hand narcotic medication count. If the user's entry does not match the count in VistA after three attempts, personnel in the CS BALANCE DISCREPANCY mail group are notified to investigate further. This failsafe can be switched on or off for each dispensing site using the BALANCE DISCREPANCY CHECK field (#37) in the DRUG ACCOUNTABILITY STATS file (#58.8), since it may not be practical for automated dispensing sites that cannot perform an on-hand medication count while dispensing drugs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PSD PAT ID LIST                                                                        | PSDLBLP       | *Patient ID List Print*  This option supports the printing of barcode labels for patient ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PSD PAT INQUIRY                                                                        | PSDPATI       | *Patient/Location Inquiry*  This option may be used to verify the location of a patient.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PSD PEND NAOU ORDERS                                                                   | PSDORSN       | *Pending CS Orders Report for an NAOU*  Use this option to list all pending CS orders.  This report may be generated for a single drug or ALL drugs within the NAOU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PSD PEND VAULT ORDERS                                                                  | PSDORST       | *Pending CS Orders by Dispensing Site*  Pharmacy uses this option to list all pending CS orders for a specific dispensing site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PSD PHARM TECH                                                                         |               | *Technician (CS Pharmacy) Menu*  <!-- image -->  This menu provides the Pharmacy Technicians access to options associated with requesting, receiving, and processing CS orders handled by pharmacy and nursing. This menu is a combination of CS options used by both pharmacy technicians and RPhs.  **Note: Some menu items are accessed by certain keys.**  **Menu Items:**  PSD WORKSHEET PRINT  *Print CS Dispensing Worksheet*  PSD WORKSHEET DISPENSING  *Fill/Dispense CS Orders from Worksheet*  PSD PRINT GS PICKUP  *Green Sheet Ready for Pickup Log*  PSD PICKUP GS  *Pick Up Green Sheet*  PSD ORDER ENTRY  *CS Order Entry For Ward*  PSD REC GS  *Receipt of Controlled Substance from Pharmacy*  PSD COMPLETE GS  *Complete Green Sheet*  PSD GS HISTORY  *Green Sheet History*  PSD ON-HAND TECH  *List On-Hand Amounts*  PSD DAILY LOG TECH  Daily Activity Log (in lieu of VA FORM 10-2320)  PSD PRINT VAULT TRANSFERS TECH  *Transfer Drugs between Dispensing Sites Report*  PSD RECEIPTS MENU  *Receipts Into Pharmacy menu.*  PSD DISPENSING MENU  *Dispensing Menu*  PSD DESTROY MENU  *Destructions Menu*  PSD MFG/LOT/EXP DATE EDIT  *Manufacturer, Lot #, and Exp. Date - Enter/Edit*  Complete Green Sheet [PSD COMPLETE GS]  Destroyed Drugs Report [PSD DEST DRUGS REPORT]  DEA Form 41 Destroyed Drugs Report [PSD DESTROY DEA41]  Destructions Holding Report [PSD DESTRUCTION HOLDING]  Add Existing Green Sheets at Setup [PSD EXISTING GS]  Green Sheet Transfer Between NAOUs Report [PSD GS TRANSFER (NAOU) REPORT]  Transfer Drugs between Dispensing Sites [PSD TRANSFER VAULT DRUGS]  Receipts Into Pharmacy [PSD RECEIPTS MENU] menu.  PSD RECEIVING  *Receiving*  PSD PURCHASE ORDER REVIEW  *Purchase Order Review*  PSD CP TRANSACTION REVIEW  *Control Point Transaction Review*  PSD DRUG RECEIPT HISTORY  *Drug Receipt History*  PSD PV INVOICE REVIEW  *Invoice Review (Prime Vendor)*  Dispensing Menu [PSD DISPENSING MENU]  PSD WORKSHEET PRINT  *Print CS Dispensing Worksheet*  PSD WORKSHEET DISPENSING  *Fill/Dispense CS Orders from Worksheet*  PSD PRINT 2321  *Dispensing/Receiving Report (VA FORM 10-2321)*  PSD PRINT 2638  *Green Sheet - Print (VA FORM 10-2638)*  Reprint Reports Menu [PSD REPRINT MENU]  PSD REPRINT 2321  *Reprint Disp/Receiving Report (VA FORM 10-2321)*  PSD REPRINT 2638  *Green Sheet Reprint (VA FORM 10-2638)*  PSD REPRINT WORKSHEET  *Dispensing Worksheet Reprint*  PSD REPRINT LABEL  *Label Reprint for Dispensing Drug*  PSD NURSE REPRINT 2321  *Reprint Transfer Between NAOUs (VA FORM 10-2321*  PSD DISPENSE W/O GS  *Pharmacy Dispense without (VA FORM 10-2638)*  PSD LABEL DRUG/NUMBER  *Label for Dispensing (Barcode)*  PSD DISPENSE TO NDES  *Narcotic Dispensing Equipment Orders*  Destructions Menu [PSD DESTROY MENU]  PSD DEST NON-CS DRUG  *Hold a CS Drug (No Inventory Update)*  PSD DEST TEXT DRUG  *Non-VA Drug Placed on Hold for Destruction*  PSD MFG/LOT/EXP DATE EDIT  *Manufacturer, Lot #, and Exp. Date - Enter/Edit*  PSD OUTPATIENT  *Outpatient Rx's*  <!-- image -->  **Note: The CS technician may perform all the Outpatient Rx's menu functions except releasing a prescription.** |

| Option Name             | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                  |
|-------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD PICKUP GS           | PSDGSPU   | *Pick Up Green Sheet*  This option provides pharmacy the ability to receive a Green Sheet into pharmacy that has been marked as Ready for Pickup by Nursing.                                                                                                                                                                                                             |
| PSD PRINT 2321          | PSDPDR    | Dispensing/Receiving Report (VA FORM 10-2321)  This report lists all CS orders dispensed to a NAOU.  This report requires the Dispensing Pharmacist signature and the signature of the nurse receiving the CS drugs.  This report will be retained within pharmacy after the controlled substances are delivered to the ward.  This report replaces the VA FORM 10-2321. |
| PSD PRINT 2638          | PSDPGS    | Green Sheet - Print (VA FORM 10-2638)  Pharmacy prints Green Sheets using this option.  All Green Sheets, not previously printed for a specific NAOU, will be generated.  A single Green Sheet print may also be selected.                                                                                                                                               |
| PSD PRINT GS PICKUP     | PSDPUGS   | *Green Sheet Ready for Pickup Log*  This report lists all Green Sheets ready on the wards to be picked up by pharmacy.  This report requires a signature of the pharmacy employee picking up the Green Sheet and a signature of the nurse releasing the Green Sheet.  This document will be retained on the ward for nurse's records.                                    |
| PSD PRINT INSPECTOR LOG | PSDPLOG   | *Inspector's Log for Controlled Substances*  This report lists all active Green Sheets by NAOU.  The data includes Green Sheet number, drug name, date dispensed, quantity dispensed, expiration date (if available), blanks for quantity on hand, and a signature blank for verification.                                                                               |
| PSD PRINT PHARM DISP    | PSDPND    | *Pharmacy Dispensing Report*  This report lists by dispensing site and date range the drug name, pharmacy dispensing number (Green Sheet #), quantity dispensed, date dispensed, and dispensing pharmacist.  Also there's a summary by drug of total number dispensed.  The summary may be generated without the individual dispensing data.                             |

| Option Name               | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD PRINT SETUP LISTS     |           | *Print CS Set Up Lists*  This option contains all reports or lists associated with setting up the files for the CS module.  **Menu Items:**  PSD DRUG LOC PRINT  *List CS Drug Location Codes*  PSD INVEN TYPE PRINT  *Print Inventory Types*  PSD NAOU PRINT  *Show Narcotic Area of Use*  PSD DRUG FILE DATA  *Drug File Stats for CS Drugs*  PSD DEA LIST  *DEA Special Handling List*  PSD STOCK PRINT  Stock Drug Print (Stock Level and Location)  PSD STOCK LIST  Stock Drug List (Inventory Type and Location)  PSD NAOU INV GROUP PRINT  Inventory Group List (80 column)  PSD MFG REPORT PRINT  *Manufacturer and Narcotic Information Report*  PSD STOCK UNIT LIST  *Breakdown/Dispensing Unit Report* |
| PSD PRINT VAULT TRANSFERS | PSDTRVR   | *Transfer Drugs between Dispensing Sites Report*  This report displays all transactions, which transferred CS between dispensing sites, for a given period of time. The transactions list within dispensing site, by drug, the date/time transferred, quantity transferred, and pharmacist transferring the drug.                                                                                                                                                                                                                                                                                                                                                                                                 |

| Option Name                                         | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD PRINT VAULT TRANSFERS TECH  **Lock:**  PSD TECH | PSDTRVR   | *Transfer Drugs between Dispensing Sites Report*  This report displays all transactions, which transferred CS between dispensing sites, for a given period of time. The transactions list within dispensing site, by drug, the date/time transferred, quantity transferred, and pharmacist transferring.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PSD PRODUCTION REPORTS                              |           | *Production Reports*  Pharmacy uses the production reports to maintain CS drug accountability and proper inventory controls. Reports generated in lieu of VA FORM 10-2321 and VA FORM 10-2638 may be generated from this menu.  **Menu Items:**  PSD PRINT INSPECTOR LOG  *Inspector's Log for Controlled Substances*  PSD STOCK PRINT  Stock Drug Print (Stock Level and Location)  PSD PRINT PHARM DISP  *Pharmacy Dispensing Report*  PSD PRINT GS PICKUP  *Green Sheet Ready for Pickup Log*  PSD PEND VAULT ORDERS  *Pending CS Orders by Dispensing Site*  PSD NOT DELIVERED  *Orders Filled Not Delivered*  PSD GS HISTORY  *Green Sheet History*  PSD DAILY LOG  Daily Activity Log (in lieu of VA FORM 10-2320)  PSD INVEN SHEET PRT  *Inventory Sheet Print*  PSD ON-HAND  *List On-Hand Amounts*  PSD EXP REPORT  *Expiration Date Report*  PSD PRINT VAULT TRANSFERS  *Transfer Drugs between Dispensing Sites Report*  PSD PRT GS PICKED UP  *GS Picked Up Awaiting Pharmacy Review*  PSD INSP LOG BY RECD DATE  *Inspector's Log by Rec'd Date*  PSD RX DISPENSING REPORT  *Rx (Prescription) Outpatient Dispensing Report*  PSD DIGITALLY SIGNED ORDERS  *Digitally Signed CS Orders Report*  PSD DIG. SIGNED RELEASED RX  *Digitally Signed OP Released Rx Report*  PSD CS PRESCRIPTIONS REPORT  *Controlled Substance Prescriptions Report*  PSD DEA SUBOXONE  *DEA DATA – Waived Practitioner Report* |
| PSD PRT GS INSP HOLD                                | PSDPSI    | *Under Inspector's Review - Green Sheets*  This report lists all Green Sheets placed on hold for review by a CS Inspector.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PSD PRT GS PICKED UP                                | PSDCPO    | *GS Picked Up Awaiting Pharmacy Review*  This report lists all Green Sheets picked up by pharmacy but still awaiting a pharmacy review.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PSD PURCHASE ORDER REVIEW                           | PSDREV    | *Purchase Order Review*  Use this option to review all receipt transactions for a selected purchase order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PSD PURGE                                           | PSDPRG    | *Purge CS WORKSHEET File*  This option purges the CS WORKSHEET file (#58.85) nightly. The CS WORKSHEET file (#58.85) is the holding area for CS order requests pending pharmacy processing. The data should remain in the file until orders have been received on an NAOU or cancelled. Once the order is received on an NAOU or cancelled, the data is purged from the file using this background job. This routine should run nightly. The time to queue this option to run should not conflict with system backup.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PSD PV INVOICE REVIEW                               | PSDREPV   | Invoice Review (Prime Vendor)  To list all receipts that has been posted for a selected Prime Vendor invoice number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PSD READY GS FOR PICKUP                             | PSDNCGS   | *Complete a Green Sheet - Ready for Pickup*  Use this option to complete a CS Administration Record (VA FORM 10-2638).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PSD REC GS                                          | PSDNRGS   | *Receipt of Controlled Substance from Pharmacy*  Use this option to receive CS orders with a Green Sheet (VA FORM 10-2638).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

| Option Name       | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                     |
|-------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD RECEIPTS MENU |           | *Receipts Into Pharmacy*  Use this option to process receipts for purchase orders, control point transactions, and Prime Vendors.  **Menu Items:**  PSD RECEIVING  *Receiving*  PSD PURCHASE ORDER REVIEW  *Purchase Order Review*  PSD CP TRANSACTION REVIEW  *Control Point Transaction Review*  PSD DRUG RECEIPT HISTORY  *Drug Receipt History*  PSD PV INVOICE REVIEW  *Invoice Review (Prime Vendor)* |
| PSD RECEIVING     | PSDREC    | *Receiving*  Use this option to process receipts from a purchase order, control point transaction, or Prime Vendor, updating the balance, transaction file, and monthly activity.                                                                                                                                                                                                                           |
| PSD REPRINT 2321  | PSDRDR    | Reprint Disp/Receiving Report (VA FORM 10-2321)  The Dispensing/Receiving Report (in lieu of the VA FORM 10-2321) may be reprinted.  This report may be generated for a single Green Sheet or for a single NAOU within a specified date and time frame.                                                                                                                                                     |
| PSD REPRINT 2638  | PSDRPGS   | Green Sheet Reprint (VA FORM 10-2638)  Pharmacy uses this option to reprint a single Green Sheet.                                                                                                                                                                                                                                                                                                           |
| PSD REPRINT LABEL | PSDLBLR   | *Label Reprint for Dispensing Drug*  This option provides pharmacy the tools to reprint CS dispensing drug labels.                                                                                                                                                                                                                                                                                          |

| Option Name              | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|--------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD REPRINT MENU         |           | *Reprint Reports Menu*  This menu allows various narcotic reports and forms to be reprinted. To ensure drug accountability, certain CS documents should only be printed once.  This option allows the reprinting of these controlled records.  **Menu Items:**  PSD REPRINT 2321  Reprint Disp/Receiving Report (VA FORM 10-2321)  PSD REPRINT 2638  Green Sheet Reprint (VA FORM 10-2638)  PSD REPRINT WORKSHEET  *Dispensing Worksheet Reprint*  PSD REPRINT LABEL  *Label Reprint for Dispensing Drug*  PSD NURSE REPRINT 2321  *Reprint Transfer Between NAOUs (VA FORM 10-2321)*                                                                                                                                     |
| PSD REPRINT WORKSHEET    | PSDRWK    | *Dispensing Worksheet Reprint*  Pharmacy personnel use this option to reprint a dispensing worksheet. The previously printed dispensing worksheet, for a given dispensing site, is utilized in reprinting this listing.  The sort selected during the original printing of the worksheet sequences these orders.  The reprinted worksheet lists a worksheet number assigned to this order, drug, quantity ordered, dispense to location, ordered by, comments and blanks for manufacturer, lot #, and expiration date. If this order has been processed by pharmacy since the original printing, the worksheet number will display as asterisk (*).  A new worksheet will not be generated during the reprinting process. |
| PSD RX DISPENSING REPORT | PSDOPTR   | *Rx (Prescription) Outpatient Dispensing Report*  A report sorted by drug, prescription number, or inventory type for a date range of outpatient dispensing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

| Option Name                            | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD SETUP                              |           | *Set Up CS (Build Files) Menu*  Options that support management of files typically created and edited during initial set up of the CS module.  **Menu Items:**  PSD PRINT SETUP LISTS  *Print CS Set Up Lists*  PSD SITE  *Site Parameters*  PSD INACTIVATE NAOU  *Inactivate NAOU*  PSD INACTIVATE NAOU STOCK DRUG  *Inactivate NAOU Stock Drug*  PSD WARD CONVERSION  *Ward (for Drug) Transfer*  PSD WARD ADD/DEL  Add/Delete Ward (for Drug)  PSD NAOU INV GROUP SORT  *Sort NAOUs in Inventory Group*  PSD TRANSFER MENU  *Transfer Stock Entries*  PSD DRUG CHECK  *Check Stocked Drugs for CS Use*  PSD BALANCE INITIALIZE  *Initialize Balance at Setup*  PSD ENTER/EDIT MENU  *Enter/Edit Menu*                                                                                                                                                                                                                                                                                                                                                                                       |
| PSD SITE  **Lock:**  PSD PARAM         | PSDSITE   | *Site Parameters*  Site parameters for the CS module.  This includes selecting an inpatient site for CS use and answering package specific questions concerning this site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| PSD STOCK DRUG EDIT                    | PSDSTK    | *Stock CS Drugs - Enter/Edit*  Provides access to enter or edit drugs stocked in the NAOU. This is how stocked drugs within an NAOU are added or changed. Duplicate entries are not allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PSD STOCK LIST                         | PSDLSTK   | Stock Drug List (Inventory Type and Location)  This report lists all active stocked drugs you have defined in the DRUG ACCOUNTABILITY STATS file (#58.8).  This report can be sorted alphabetically or by inventory type/location/drug.  The data includes NAOU, location, drug name, stock level, and reorder level. The report sorted by inventory type/location/drug will include the type as printed data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| PSD STOCK PRINT                        | PSDPSTK   | Stock Drug Print (Stock Level and Location)  This report prints an alphabetic listing of all active drugs you have defined in the DRUG ACCOUNTABILITY STATS file (#58.8).  This report lists NAOU, drug name, location, stock levels, all ward (for drug) assignments, and all inventory types.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PSD STOCK UNIT LIST                    | PSDPDU    | *Breakdown/Dispensing Unit Report*  This report provides an alphabetic listing of all active drugs you have defined in the DRUG ACCOUNTABILITY STATS file (#58.8).  This listing includes breakdown unit and package size from the DRUG ACCOUNTABILITY STATS file (#58.8) and dispense unit and price per dispense unit from the DRUG file (#50).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PSD TRANSACTION MENU                   |           | *Pharmacist Menu*  This option provides pharmacy the access to process all CS transactions. This includes receipts into pharmacy; all orders dispensed from pharmacy, and outpatient prescriptions. Completing Green Sheets allows pharmacy to complete those Green Sheets with no discrepancies, math errors, drugs returned to stock, and drugs being held for destruction.  Returns to stock and holding for destruction must be drugs associated with the Green Sheet when using this option.  **Menu Items:**  PSD RECEIPTS MENU  *Receipts Into Pharmacy*  PSD DISPENSING MENU  *Dispensing Menu*  PSD COMPLETE GS  *Complete Green Sheet*  PSD OUTPATIENT  *Outpatient Rx's*  PSD TRANSFER VAULT DRUGS  *Transfer Drugs between Dispensing Sites*  PSD INFUSION MENU  *Infusion Order Processing Menu*  PSD DESTROY MENU  *Destructions Menu*  PSD ORDER ENTRY  *CS Order Entry For Ward*  PSD REC GS  *Receipt of Controlled Substance from Pharmacy*  PSD IRL INV MENU  *Barcode TRAKKER for Inventory*  PSD MFG/LOT/EXP DATE EDIT  *Manufacturer, Lot #, and Exp. Date - Enter/Edit* |
| PSD TRANSFER AOU                       | PSDTRA    | *AOU to NAOU Transfer Entries*  This option will "copy" the active stock entries from a selected AR/WS Area of Use into one or more selected CS NAOU.  As many as 10 NAOUs may be chosen for transfer at one time.  The drug name only, or the drug name, stock level, and location code, or drug name, stock level, location code, and inventory types can be transferred.  The "copy" process will not copy inactive drugs. The actual transfer takes place in a background job, which is queued automatically.  When the transfer is complete, the user will be notified by a MailMan message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PSD TRANSFER MENU  **Lock:**  PSD TRAN |           | *Transfer Stock Entries*  This menu option supports two distinct methods of transferring active stock.  The first "copies" active stock from a NAOU into another NAOU.  The second "copies" active stock from an AR/WS Area of Use into a CS NAOU.  **Menu Items:**  PSD TRANSFER NAOU  *NAOU to NAOU Transfer Stock Entries*  PSD TRANSFER AOU  *AOU to NAOU Transfer Entries*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PSD TRANSFER NAOU                      | PSDTRN    | *NAOU to NAOU Transfer Stock Entries*  This option will "copy" the active stock entries from a selected NAOU into one or more selected NAOUs.  As many as 10 NAOUs may be chosen for transfer at one time. The drug name only, or drug name, stock level, and location code, or drug name, stock level, location code, and inventory types can be transferred.  The "copy" process will not copy inactive drugs.  The actual transfer takes place in a background job, which is automatically queued.  When the transfer is complete, the user will be notified by a MailMan message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PSD TRANSFER VAULT DRUGS               | PSDTRV    | *Transfer Drugs between Dispensing Sites*  This option is utilized to transfer controlled substances between dispensing sites.  The inventory balances are updated within each dispensing site. When drugs are being transferred from one dispensing site into another, a MailMan message will be generated to the Pharmacy Supervisor holding the PSDMGR security key, if the receiving dispensing site does not normally stock that particular drug.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PSD WARD ADD/DEL                       | PSDWADD   | Add/Delete Ward (for Drug)  This option will allow a user to add or delete a ward (for drug) assignment for all stock drugs in one or more active NAOUs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

| Option Name              | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD WARD CONVERSION      | PSDWCHG   | *Ward (for Drug) Transfer*  This option will enable a user to change a ward (for drug) designation from the old ward to a new ward for all drugs in all NAOUs or in a single NAOU.  This can be used, for example, when a ward is closed down for construction.  A background job can be queued for a later time to do the conversion and a MailMan message will be sent to the person who queued the job when it has run to completion.                                                                                                                                                                                                                                                               |
| PSD WORKSHEET DISPENSING | PSDDWK    | *Fill/Dispense CS Orders from Worksheet*  Pharmacy personnel use this option to process and verify CS orders.  The Pharmacy Dispensing Worksheet should be printed first using the Print CS Dispensing Worksheet option. CS orders may be dispensed by selecting an individual worksheet number or by sort order on the worksheet.  The pharmacist will be prompted for dispensing pharmacist, dispensing site, quantity dispensed, manufacturer, lot #, and expiration date.  The prompt for pharmacy dispensing number will only appear if your site has elected to enter these control numbers manually.  Otherwise, the software will automatically generate the next available dispensing number. |

| Option Name         | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD WORKSHEET PRINT | PSDPWK    | *Print CS Dispensing Worksheet*  Pharmacy personnel use this option to print a dispensing worksheet. This worksheet MUST be printed prior to pharmacy dispensing CS orders.  Pharmacy may sort this report within a dispensing site, by NAOU (one, some, or ALL), or by inventory group. Next, the orders are sorted by either (1) drug, then all NAOUs, or (2) NAOU, then all drugs.  The worksheet lists a worksheet number assigned to this order, drug, quantity ordered, dispense to location, ordered by, comments, and blanks for manufacturer, lot #, and expiration date.  When using the Fill/Dispense CS Orders from Worksheet option, pharmacy may process orders by individual request number (the assigned worksheet number) or by worksheet.  If the worksheet method of dispensing is selected, the software will display each order to the pharmacist in the sequence the order was printed. Each time this report is run, a new worksheet will be built and all new CS orders will be included.  The printed sequence of CS orders will change with each new worksheet. |

&lt;This page is intentionally left blank.&gt;

## ## 10 8BPackage–Wide Variables

### 27BPackage–Wide Variables

There are no package–wide variables for Controlled Substances V. 3.0.

### 28BPackage Variables

CS module contains only one package variable - PSDSITE. This variable must be defined and is required for the package to run. PSDSITE is set in the routine PSDSET as package users enter the module.

Some stations design their own menus for individual users. If this is the case, then the top level CS menu only must contain the following entry and exit code in the OPTION file (#19):

**ENTRY ACTION:  I '$D(PSDSITE) D ^PSDSET**

**EXIT ACTION:  K PSDSITE**

This entry and exit code should not be included on the submenus in order to preserve the variable PSDSITE. This entry and exit code must be present because the PSDSITE variable is set as users enter the package. If the Kernel’s “^OPTION NAME” feature is used to jump directly into lower levels of the CS package, then the “Inpatient Site Name” prompt must be answered in order to define the PSDSITE variable. All options are independently invoked, however, if the instructions above are not followed, users will be repeatedly asked to select an Inpatient Site if there are two or more sites that are flagged as selectable for CS use.

&lt;This page is intentionally left blank.&gt;

## 9BResource Requirements

There are 298 CS routines that take up approximately 949K of disk space.

The KERNEL response time monitoring hooks, for capacity management studies, have been added to the Nurse Order entry routine PSDORN1 and the Pharmacy dispensing routine PSDDWK3.

### 29BHardware Requirements

The following equipment is recommended to successfully implement V. 3.0:

Intermec TRAKKER 9440 (Barcode Reader)

HP LaserJet III (or any compatible laser printer e.g., 3si, 4si, 5si, and Kyocera)

VT320 (bi-directional only) or any bi-directional flow CRT

The laser single sheet feed printer is required to print the VA FORM 10-2638 and barcode ID labels. It is recommended that the printer be physically located in the narcotic vault for efficiency and security.

The laser printer must be a selectable device via the terminal server. Barcode printing is not available with a slaved printer.

The barcode TRAKKERs and CRTs are required to download/upload data necessary in maintaining a perpetual inventory within the pharmacy vault.

To support barcode label printing and downloading/uploading via the TRAKKER, certain hardware specific parameters for the TERMINAL TYPE file (#3.2) and DEVICE file (#3.5) are necessary. To assist IRM in setting up these devices the routine PSDTER has been included in the routine set. The TERMINAL TYPE file (#3.2) information includes right margin, form feed, page length, backspace, open execute, barcode on, and barcode off. DEVICE file (#3.5) data includes margin width, form feed, page length, backspace and subtype. For the TRAKKER, open printer port and close printer port is included in the terminal type information. See page 73 for examples in setting up the devices using the routine PSDTER.

#### 35BPrinting of Bar Codes

**Introduction**

**Bar Code:** 3 of 9 portrait (most popular and applicable) it is variable-length, bi-directional, self-checking, alphanumeric code. It consists of 36 defined numeric and upper case alphabetic characters, seven special characters, and a stop/start character. Each character is composed of nine elements: five bars and four spaces. Three of nine elements are wide and six are narrow.

**Suggested Typeface:** Letter Gothic has a clean modern appearance and can be read at a glance when used with bar code.

**Printer Models tested:**

HP LaserJet III              Kyocera F800A

HP LaserJet 3si             Output Technology Corporation (OTC) 560 DL.

HP LaserJet 4si

#### 36BHP LaserJet Printer

**External Font Cartridge:** HP 36596A 3037 (custom font 3-9)(3/4si)

HP C2053A #C06 (bar code and more)

HP 92286W1 (bar code 3-9/OCR A)

**Paper:** Good quality label paper

**Terminal Type File:** An OPEN EXECUTE, BAR CODE OFF and BAR CODE ON are needed to set the print commands (escape sequences).

HP LaserJet printer matches font characteristics in the following order:

(symbol set, spacing, pitch, point size, style, stroke weight, typeface)

Example: TERMINAL TYPE File (#3.2)

OPEN EXECUTE:

W *27,(escape sequence)

"E",(reset the printer to default settings)

*27,(escape sequence)

"&amp;l0O",(&amp;l(type of command)0O(portrait orientation)

**use a lower case l and a upper case O **

*27,(escape sequence)

"(8U",(Roman8 symbol set)

*27,(escape sequence)

"s0p(fixed spacing(zero)

16.66h(pitch # characters/inch)

8.5v(point size(height of a character)

0(upright style)

s0b(medium stroke weight)

6T",(Gothic typeface)

*27,(escape sequence)

"="(half line feed)

From the HP manual use the PCL TYPEFACE LIST UNDER CARTRIDGE FONTS to select the print commands (escape sequences) for the BAR CODE ON.

Use the following device and terminal type files to print:

(1) Green sheets on plain paper

(2) Drug labels

**Example: DEVICE File (#3.5)**

NAME: DEMON BARCODE                     $I: &lt;$Ivalue&gt;:

ASK DEVICE: YES                         ASK PARAMETERS: YES

SIGN-ON/SYSTEM DEVICE: NO               LOCATION OF TERMINAL:&lt;location&gt;

*MARGIN WIDTH: 0                        *FORM FEED: #

*PAGE LENGTH: 58                        *BACK SPACE: $C(8)

SUBTYPE: P-HP BARCODER                  TYPE: TERMINAL

LAT SERVER NODE: IS3D2                  LAT SERVER PORT:&lt;port#&gt;

VMS DEVICE TYPE: NOT SPOOLED            LAT PORT SPEED:96

**Example: TERMINAL TYPE File (#3.2)**

NAME: P-HP BARCODER                     SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 0                         FORM FEED: #

PAGE LENGTH: 58                         BACK SPACE: $C(8)

OPEN EXECUTE: W

27)\_"E"\_$C(27)\_"&amp;l0O"\_$C(27)\_"(8U"\_$C(27)\_"(s0p"\_$S($G(PSDC

PI)=10:"10h14",1:"12h12")\_"v0s0b6T"

10 PITCH: $C(27)\_"(s10H"                12 PITCH: $C(27)\_"(s12H"

HIGH INTENSITY (BOLD): $C(27)\_"(s4b"    DEFAULT LINES PER INCH:

$C(27)\_"&amp;l8C"

X LINES PER INCH: $C(27)\_"&amp;l12C"

BAR CODE OFF:

"*"\_$C(27)\_"&amp;l0O"\_$C(27)\_"(8U"\_$C(27)\_"(s0p"\_$S($G(PSDCPI)=10:"1

0h14",1:"12h12")\_"v0s0b6T"

BAR CODE ON:

$S($D(PSDX2):$C(27)\_"*p"\_(PSDX2-1*300+200)\_"y*p"\_(PSDX1-1*810+38)

\_"X",1:"")\_$C(27)\_"(0Y"\_$C(27)\_"(s0p8.1h12v0s0b0T

Use the following device and terminal type files to print:

(1) Patient ID Labels

**Example: DEVICE File (#3.5)**

NAME: CSHPBAR                           $I: 0

ASK DEVICE: YES                       ASK PARAMETERS: YES

SIGN-ON/SYSTEM DEVICE: NO             LOCATION OF TERMINAL: SLAVE FOR

*MARGIN WIDTH: 0                      *FORM FEED: #

*PAGE LENGTH: 58                      *BACK SPACE: $C(8)

SUBTYPE: P-HPCS                       TYPE: TERMINAL

VMS DEVICE TYPE: NOT SPOOLED          LAT PORT SPEED: 96

**Example: TERMINAL TYPE File (#3.2)**

NAME: P-HPCS                           SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 0                       FORM FEED: #

PAGE LENGTH: 58                       BACK SPACE: $C(8)

OPEN EXECUTE: W

*27,"E",*27,"&amp;l0O",*27,"(8U",*27,"(s0p16.66h8.5v0s0b6T",*27,"=

"

BAR CODE OFF:

"*",*27,"&amp;l0O",*27,"(8U",*27,"(s0p16.66h8.5v0s0b6T",*27,"="

BAR CODE ON: *27,"&amp;l0O",*27,"(0Y",*27,"(s0p12.00v4.35h0s"

#### 37BOTC Printer

Use the following device and terminal type file to print:

(1)  Patient ID labels

(2)  Drug labels

**Example: DEVICE File (#3.5)**

NAME: REX                               $I: \_LTA9094:

ASK DEVICE: YES                       ASK PARAMETERS: YES

LOCATION OF TERMINAL: DEVELOPMENT HALLWAY

*MARGIN WIDTH: 132                    *FORM FEED: #

*PAGE LENGTH: 66                      *BACK SPACE: $C(8)

BARCODE AVAIL: YES

MNEMONIC: SCHMEGMO

MNEMONIC: SMEGMA

MNEMONIC: DEV LP

SUBTYPE: P-OTC560                     TYPE: TERMINAL

LAT SERVER NODE: DSV2                 LAT SERVER PORT: LC-4-11

VMS DEVICE TYPE: NOT SPOOLED          LAT PORT SPEED: 96

**Example: TERMINAL TYPE File (#3.2)**

NAME: P-OTC560                        RIGHT MARGIN: 132

FORM FEED: #                          PAGE LENGTH: 66

BACK SPACE: $C(8)                     10 PITCH: $C(27)\_"[w"

12 PITCH: $C(27)\_"[2w"

DESCRIPTION: OTC 560DL with Epson FX100 Emulation

16 PITCH: $C(27)\_"[3w"                BAR CODE OFF: $C(27),"[0t"

BAR CODE ON: $C(27),"[4;4;0;2;4;2;4;2}",$C(27),"[3t"

#### 38BKYOCERA Printer

Prescribe is the native language of the laser printer. It gives the capability to control line and character spacing, adjust margins, change fonts, position text, draw graphics and print multiple copies. It sends commands to the printer to be executed.

**Commands:**

**!R!** causes the printer to switch from normal text printing mode to Prescribe mode.

**EXIT;** returns printer back to normal mode.

There can be an unlimited number of commands between the initial !R! and the final EXIT;.

**EX: !R!** command; command;

**RES;** causes a page break and reset parameters back to the initial settings.

**MRP;** moves the cursor from its current position to a specified relative position, measured in the units designated by the UNITS command.

**BARC 19** , prints specified data in barcode form. The 19 provide code 39 with no check digits.

A command name should be followed by a space.(sem ; )

Each command must end with a semicolon (;).

A comma must follow a parameter and a semicolon must follow the last parameter.

Use the following device and terminal type file to print:

(1) Drug Labels

**Example: DEVICE File (#3.5)**

NAME: KYOCERA BARCODER	$I: &lt;$I value&gt;

ASK DEVICE: YES	ASK PARAMETERS: YES

SIGN-ON/SYSTEM DEVICE: NO	LOCATION OF TERMINAL: &lt;location&gt;

MARGIN WIDTH: 0 	FORM FEED: #

PAGE LENGTH: 66	BACK SPACE: $C(8)

SUBTYPE: P-KYOCERA-BARCODE	TYPE: TERMINAL

**Example: TERMINAL TYPE File (#3.2)**

NAME: P-KYOCERA-BARCODE                 SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 0                                     FORM FEED: #

PAGE LENGTH: 66                                    BACK SPACE: $C(8)

OPEN EXECUTE: W "!R! RES;FONT "\_$S($G(PSDCPI)=10:1,1:6)\_";EXIT;"

10 PITCH: "!R! FONT1; EXIT;"          12 PITCH: "!R! FONT6; EXIT;"

DEFAULT LINES PER INCH: "!R! SLM 2; EXIT;"

X LINES PER INCH: "!R! SLPI 4.1; EXIT;"

BAR CODE OFF: "', 60, 60, 3, 6, 6, 6, 3, 6, 6, 6;"\_$S('$D(PSDX1):"",PSDX1=PSDC

NT:"MRP 0 , 60;",1:"")\_"EXIT;"

BAR CODE ON: "!R! FONT 6; UNIT D; "\_$S('$D(PSDX1):"",PSDX1=1:"MRP 0,-60 ; ",1:"")\_$S('$D(PSDX1):"",1:"MRP "\_(PSDX1&gt;1*810+38)\_" , 0 ;")\_" BARC 19, N, '"

Use the following device and terminal type file to print:

(1) Patient ID labels

**Example: DEVICE File (#3.5)**

NAME: CSKYWARD                          $I: 0

ASK DEVICE: YES                       LOCATION OF TERMINAL: SLAVE FOR

*MARGIN WIDTH: 0                      *FORM FEED: #

*PAGE LENGTH: 66                      *BACK SPACE: $C(8)

BARCODE AVAIL: YES                    SUBTYPE: P-KYOCERA-CSWARD-BARCODE

TYPE: TERMINAL

**Example: TERMINAL TYPE File (#3.2)**

NAME: P-KYOCERA-CSWARD-BARCODE          SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 0                       FORM FEED: #

PAGE LENGTH: 66                       BACK SPACE: $C(8)

OPEN EXECUTE: W "!R!  RES; FONT 7; EXIT;"

CLOSE EXECUTE: W "!R!;RES;EXIT;",*27,"[4i"

DESCRIPTION: CONTROLLED SUBSTANCES PATIENT LABLES ON WARD

BAR CODE OFF: "', 60, 60, 2, 10, 10, 10, 2, 10, 10, 10; MRP 0 , 60;

EXIT;"

BAR CODE ON: "!R!  FONT 7; UNIT D; MRP 0,-30 ; BARC 19,  N, '"

#### 39BPortable Barcode Reader (TRAKKER 9440)

CS V. 3.0 includes options for downloading IRL programs to the TRAKKER. For these options to function, the TRAKKER must be connected to your **V** *IST* **A** computer system. The TRAKKER comes with an RS-232 cable. The end of the cable that connects to your system terminates to a DB-25PIN connector.

The TRAKKER may be connected to the system via the auxiliary port of any CRT that supports complete bi-directional data flow and flow control (XON-XOFF) through the auxiliary port. Whatever strategy works for addressing a slave printer to the CATHODE RAY TUBE (CRT) will also work for the TRAKKER.

The following procedure illustrates stepping through the configuration process to verify whether the TRAKKER is properly prepared to interface with **V** *IST* **A** .

<!-- image -->

**Note** : A brief example of the TRAKKER setup may be displayed by running the routine PSDTRAK from programmer mode.

To enter the configuration mode use the following steps:

1. Turn the TRAKKER on by pressing the &lt; **on-off** &gt; key. The unit should perform a brief self-test and then display a “Ready” prompt.

1. Hold down the &lt; **Ctrl** &gt; key and press **E** . The words “CONFIGURATION MENU:” should appear on the first line of the TRAKKER display screen. This is the configuration mode.

1. Press the &lt; **Enter** &gt; key until prompted to “Select or modify 	operating parameters?”, the word **NO** will appear on the fourth TRAKKER display line.

1. Change **NO** to **YES** by pressing the &lt; **Space** &gt; key.

1. Use the &lt; **Enter** &gt; key to step through the basic operating parameters. Unless otherwise instructed, use the &lt; **Space** &gt; key to make the selections:

a.	BEEP VOLUME: Set this according to the user’s preference. If the work environment is noisy, choose **HIGH** .

b.	DISPLAY MODE: This tells the TRAKKER how to display data that is entered. Choose **BUFFERED** .

c.	CHARACTER SET: This selects an alphabet. Choose **US-ASCII** .

d.	CPU RESP REQD MODE: Tells the TRAKKER whether to wait for an acknowledgment from **V** *IST* **A** after each transmission of uploaded data. Choose **DISABLED** .

e.	PREAMBLE A REQUIRED: Tells the TRAKKER whether to check for one specific preamble on all data entered. Choose **NO** .

f.	LASER SCANNER MODE: Tells the TRAKKER whether to allow continuous scanning of barcode labels without release of the laser trigger in between. Choose **ONE-SHOT TRIGGER** .

g.	APPEND TIME TO DATA: Instructs the TRAKKER to add the correct time to each data record as it is transmitted. Choose **NO** .

h.	TIME IN SECONDS: Tells the TRAKKER whether time displays should include seconds. Choose **YES** .

i.	RESUME IRL PROGRAM: Choose **NO** .

j.	AUTOMATIC SHUT—OFF: A time-out feature such that the TRAKKER will turn itself off after a specified period of inactivity in order to conserve battery power. Enter the selection (in minutes) as a number. The TRAKKER will ignore the &lt; **Space** &gt; key. A **10-minute** time-out period is suggested.

k.	BACKLIGHT TIMEOUT: A time-out feature on backlighting of the TRAKKER display screen. Intended to conserve battery power. Selections are made in seconds. A **60 second** time-out period is suggested.

6. The next configuration heading is “Select or modify comm protocol?” Use the &lt; **Space** &gt; key to select **POINT TO POINT** .

1. Use the &lt; **Enter** &gt; key to step through the comm protocol:

a.	CHECK CTS: Tells the TRAKKER whether or not to look for a CTS (clear to send) signal before transmitting data. Since **V** *IST* **A** uses XON/XOFF, choose **NO** .

b.	XON: When XON/XOFF protocol is used, the XON character must be specified here. Hold down the &lt; **Ctrl** &gt; key and press **Q** . **DC1** should appear on the last TRAKKER display line. Press &lt; **Enter** &gt; to continue.

c.	XOFF: Hold down the &lt; **Ctrl** &gt; key and press **S** . Observe **DC3** and press &lt; **Enter** &gt; to continue.

d.	BAUD RATE: The TRAKKER data transmission speed. **1200 baud** is recommended.

e.	PARITY: Selection is **DISABLED** .

f.	DATA BITS: Select **8** .

g.	STOP BITS: Select **1** .

h.	TIMEOUT DELAY: Tells the TRAKKER how long to wait for the next character of a downloaded IRL program before declaring an error condition. Choose **10 seconds** .

i.	INTERCHAR DELAY: Tells the TRAKKER how long to pause between characters when uploading data to **V** *IST* **A** . Choose **50 milliseconds (ms)** .

j.	TURNAROUND DELAY: Delay time between receipt of a character from **V** *IST* **A** and acknowledgment by the TRAKKER. This parameter is not critical with an XON/XOFF protocol. **Choose 0 ms** .

1. When the TURNAROUND DELAY is set, the “Select or modify barcodes?” prompt will display again. The TRAKKER is now configured for use with **V** *IST* **A** .

To save any changes that have been made, hold down the &lt; **Alt** &gt; key and then press the &lt; **E** &gt; key. Once saved, the changes will remain in a non-volatile section of TRAKKER memory until the TRAKKER is re-configured.

To exit the configuration mode without saving any changes, hold down the &lt; **Crtl** &gt; key and press &lt; **Z** &gt;. Do this instead of the escape sequence (&lt; **Alt** &gt;, &lt; **E** &gt;) described above.

<!-- image -->

**Note** : If the TRAKKER has been configured differently, first it must be RESET . For details on this procedure, refer to the *INTERMEC 944X TRAKKER READERS User’s Manual* . Next, the user must CONFIGURE the TRAKKER, repeating steps 1-8 above.

**Setting the TRAKKER clock:**

<!-- image -->

**Note** : The clock should be set on the TRAKKER before users start performing inventories. It is not necessary to press &lt; **Enter** &gt; after responding **YES** to setting the clock.

After having turned the TRAKKER on, press &lt; **Ctrl** &gt; &lt; **T** &gt;.

The following will be displayed:

#### 71BExample: TRAKKER Clock

<!-- image -->

#### 40BInterfacing the TRAKKER 9440 to a VT-320 Auxiliary Port

The auxiliary port of the VT-320 is a six pin modular jack, so a cable with a six pin modular plug on one end and a male DB-25 connector on the other is needed.

<!-- image -->

The PRINTER SET UP SCREEN of the VT-320 will allow configuration of the CRT for use with a TRAKKER. To get to this screen:

1. Hold the &lt; **Shift** &gt; key and press &lt; **SET UP&gt;** .

1. Use the cursor control keys &lt; **--&gt;** &gt;(right arrow) to move the cursor to the box labeled Printer.

1. Press the &lt; **Enter&gt;** key.

From this point, the user can set the software selectable features of the auxiliary port as follows:

1. Speed: The baud rate of the auxiliary port. This must match the baud rate of the TRAKKER. **1200** is commonly used.

1. Printer to Host Communication: This must be set to **Printer to Host** for the TRAKKER upload/download operations.

1. Print Mode: Determines how the auxiliary port is controlled. Proper setting is **Normal Print Mode** .

1. XOFF: This selects whether or not the auxiliary port will use XON/XOFF 	data flow control. Proper setting is **XOFF** .

1. Bits and Parity: Selects a character format for the auxiliary port. Must match the character format of the TRAKKER.

1. Stop Bit: Selects the number of stop bits. Must match the format of the TRAKKER. **One** stop bit is commonly used.

1. Print Region: Unimportant for downloading or uploading. Commonly set to **Print Full Page** .

1. Printed Data Type: Used primarily with slaved printer but not critical for downloading or uploading. Commonly set to **National Only** .

1. Print Terminator: Selects whether or not the VT-320 should send a form feed at the end of each print operation. Proper setting is **No Terminator** .

Finally, appropriate entries in your TERMINAL TYPE file (#3.2) and DEVICE file (#3.5) are needed. For IRM, the routine PSDTER will allow the user to setup the TERMINAL TYPE file (#3.2) and DEVICE file (#3.5) information. This routine may be run from programmer’s mode. Refer to page 9 in the Installation Guide for an example.

**Example: DEVICE File (#3.5)**

NAME     	: TRAKKERSL

LOCATION     	: SLAVED 9440 FROM VT420 AUXILLARY PORT

MARGIN WIDTH 	: 80

PAGE LENGTH 	: 9999

MNEMONIC  	: TRAKKERSL

FORM FEED 	: #

BACK SPACE 	: $C(8)

SUB-TYPE  	: C-VT420 (9440)

TYPE    	: TERMINAL

$I      	: 0 (zero)

**Example: TERMINAL TYPE File (#3.2)**

NAME 	: C-VT420 (9440)

FORM FEED 	: #

OPEN EXECUTE   	: W $C(0)

DESCRIPTION 	: TRAKKER 9440 TO AUXILLARY PORT OF VT420

OPEN PRINTER PORT	: W $C(27)\_"[5i"

CLOSE PRINTER PORT	: W $C(27)\_"[4i"

RIGHT MARGIN 	: 80

PAGE LENGTH  	: 9999

**Functions on the TRAKKER:**

&lt; **Ctrl** &gt;-&lt; **T** &gt;	This gives access to set the clock.

&lt; **Ctrl** &gt;-&lt; **Enter** &gt;-&lt; **E** &gt;	This gives access to end an IRL session.

Simultaneously press the &lt; **Ctrl** &gt;-&lt; **Enter** &gt;keys,

release them, then press &lt; **E** &gt;.

&lt; **Ctrl** &gt;-&lt; **Enter** &gt;-&lt; **C** &gt;	This gives access to clear the data files.

Simultaneously press the &lt; **Ctrl** &gt;-&lt; **Enter** &gt;keys,

release them, then press &lt; **C** &gt;.

[To clear the data files the user must have already ended the IRL session.]

**Example: Using Routine PSDTER**

**D ^XUP**

Setting up programmer environment

Access code: *[Enter your access code here]*

Terminal Type set to: C-VT100

Select OPTION NAME:

**&gt;D ^PSDTER**

Select one of the following:

1         Load all three barcode Terminal Types

2         Load the P-HP BARCODER Terminal Type

3         Load the P-KYOCERA-BARCODE Terminal Type

4         Load the C-VT420 (9440) Terminal Type

5         Select your own Terminal Type

6         Display

7         Nevermind

Enter response: **?**

If any of the selected Terminal Types already exist, I will ask for your

approval before proceeding.

Select one of the following:

1         Load all three barcode Terminal Types

2         Load the P-HP BARCODER Terminal Type

3         Load the P-KYOCERA-BARCODE Terminal Type

4         Load the C-VT420 (9440) Terminal Type

5         Select your own Terminal Type

6         Display

7         Nevermind

Enter response: **1** Load all three barcode Terminal Types

Current settings: *[If a P-HP BARCODER TERMINAL TYPE already exists, current settings will be displayed]*

Are you sure that you want to stuff the Controlled Substances barcode

set-up into the P-HP BARCODER Terminal Type? No// **Y** ES

Updating P-HP BARCODER.

Update the DEVICE file? No// **?**

Yes, and I will add the P-HP BARCODER Terminal Type and update a few

fields in the device of your selection.

Update the DEVICE file? No// **&lt;Enter&gt;**

Current settings: *[If a P-KYOCERA BARCODE TERMINAL TYPE already exists, current settings will be displayed]*

Are you sure that you want to stuff the Controlled Substances barcode

set-up into the P-KYOCERA-BARCODE Terminal Type? No// **?**

Yes and I'll update OPEN EXECUTE, RIGHT MARGIN, PAGE LENGTH, Etc. fields.

Are you sure that you want to stuff the Controlled Substances barcode

set-up into the P-KYOCERA-BARCODE Terminal Type? No// **Y** ES

Updating P-KYOCERA-BARCODE.

Update the DEVICE file? No// **&lt;Enter&gt;**

Are you sure that you want to stuff the Controlled Substances barcode

set-up into the C-VT420 (9440) Terminal Type? No// **Y** ES

Updating C-VT420 (9440).

Update the DEVICE file? No// **&lt;Enter&gt;**

The HP LaserJet III and the Kyocera laser printer setup used in testing the printing of the VA FORM 10-2638 follows:

**-----------------------------------------** ***example continues*** **---------------------------------------**

**Example: Using Routine PSDTER (continued)**

**LASER    PRINTER    STATUS    PAGE**

Software version  6.45 - 20  ,      released 04/90.
 Units : Inches.               Page : Portrait.
 Current font :      1.        Current country :  0.
 Copies :  1.                  Current emulation :  6.

**Margins                    Spacings**

Top        0.300               Line        0.167
  Bottom    10.300               Character   0.100
  Left       0.000               Pen width   0.010
  Right      8.000

**Memory allocation (Kbytes)** User memory avail.  187.225      In use (System) 108.773
  Prescribe MCRO buff.  4.996      In use            0.000
  PCL MCRO buff         3.500      In use            0.000

Parallel buff. size  10.000
  RS232C buff. size    10.000
  Raster size         128.000

**Miscellaneous status**

Option (Comment)        Value  Option(Comment)       Value
  ----------------------------------------------------------
  CO(Reserved)              0    P1(Default Emulation)   6
  C1(Page orientation)      0    P2(C.R. action)         1
  C2(Dflt font Num-mid.)    0    P3(L.F. action)         1
  C3(Dflt font Num-low)     1    P9(Escape Char.)       82
  C4(PCL MCRO buff.)        0    UO(Line/Inch\_high)      6
  C5(Dflt font Num-High)    0    U1(Line/Inch\_low)       0
  A1(Top margin\_high)       0    U2(Char/Inch\_high)     10
  A2(Top margin\_low)        0    U3(Char/Inch\_low)       0
  A3(Left margin\_high)      0    U5(Status page)         0
  A4(Left margin\_low)       0    U6(Country code)        0
  A5(Page length\_high)     13    U7(Dflt symbol set)     0
  A6(Page length\_low)      61    RO(Reserved)            6
  A7(Page width\_high)       8    R1(Reserved)            0
  A8(Page width\_low)       11    R2(Dflt paper size)     0
  HO(Prescribe macro)       0    R3(Reserved)            0
  H1(RS232C baud rate)     96    R4(Reserved             1
  H2(RS232C data bits)      8    R5(Raster size)         1
  H3(RS232C stop bit)       1    R6(Reserved)            0
  H4(RS232C parity bit)     0    R7(Other paper size)    0
  H5(RS232C protocol)       0    R8(D.W. Data length)    7
  H6(Zoff threshold[%])    90    R9(Reserved)            0
  H7(Xon threshold[%])     70    MO(PAR buffer size)     1
  H8(RS232C buff. size)     1    M1(Reserved)            0
  H9(F.F. time out)         3    M2(Reserved)            0

Service information

/0024/0050/1061/0811/

**-----------------------------------------** ***example continues*** **---------------------------------------**

**Example: Using Routine PSDTER (continued)**

*** SAGG GLOBAL TRENDING DISPLAY FOR ^PSD ***

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Site Name: JACKSON            Complexity Level: 1      Supporting ISC: 7

System Type: VAX-DSM          OS Version: V6.2         Kernel Version: 8.0

SAGG Version: 1.6T6           MUMPS Version: DSM V6.3D-031 for OpenVMS AXP

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ACTUAL GLOBAL TREND             NORMALIZED GLOBAL TREND

-------------------             -----------------------

SESSION   # OF | GB SIZE  GB GROWTH GB   %  | GB SIZE GB GROWTH|Flag

DATES     DAYS | In Blks  In Blks   Eff  CHANGE| In Blks In Blks  |

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

|                               |                  |

JUN 09, 1996   43 |    22,480    1,356 77%   6.0% |    26,436   3,956| *L*

JUN 22, 1996   13 |    22,819      339 77%   1.5% |    24,015   1,196| *L*

OCT 12, 1996   112|    30,197    7,378 76%  24.4% |    40,501  10,304| *H*

NOV 09, 1996   28 |    33,643    3,446 76%  10.2% |    36,219   2,576| *H*

DEC 07, 1996   28 |    39,183    5,540 76%  14.1% |    41,759   2,576| *H*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

STATISTICAL INFORMATION FOR ^PSD

--------------------------------

Beginning Global Size:               22,480 Blks  (23.0 Mb)

Ending Global Size:                  39,183 Blks  (40.1 Mb)

# Sample Sessions:                     5 Samples

Total # of Sample Days:                 181 Days

Avg Daily Normalized Global Growth:      92 Blks

Avg 28 Day Normalized Global Growth:  2,576 Blks

Avg 1 Year Normalized PSD Growth:     33,580 Blks  (34.4 Mb)

Avg 1 Year Projected PSD Size:       72,763 Blks  (74.5 Mb)

Avg 2 Year Projected PSD Size:      106,343 Blks  (108.9 Mb)

Avg 3 Year Projected PSD Size:      139,923 Blks  (143.3 Mb)

> **NOTE:** *H* means that the actual global growth increased 20%

more than the average normalized global growth for

this site.

*L* means that the actual global growth decreased 20%

more than the average normalized global growth for

this site.

&lt;This page is intentionally left blank.&gt;

## 10BHow to Generate On-line Documentation

Throughout the entire CS module, on-line help is obtained by entering a question mark (?) at any prompt to assist in the choice of actions.

The Data Dictionaries (DDs) are considered part of the on-line documentation for this software application. Use the VA FileMan *DATA DICTIONARY UTILITIES* option to print the DDs. For instructions on obtaining a list of files exported by the CS module refer to page 13 of this manual.

The namespace for the CS module is PSD.

&lt;This page is intentionally left blank.&gt;

## 11BAdditional Information

**Templates**

#### 41BFILE #58.2 AOU INVENTORY GROUP

INPUT TEMPLATE(S)

PSD INV GROUP

&lt;This page is intentionally left blank.&gt;

## 12BAppendix A Health Level 7 (HL7)

Appendix A is comprised of the HL7 interface specifications from the Birmingham Information Resources Management Field Office, Department of Veterans Affairs.

### 30BIntroduction

#### 42BGeneral Description

The **V** *IST* **A** Controlled Substances (CS) V. 3.0 package provides an interface between **V** *IST* **A** and a Narcotic Dispensing Equipment System (NDES). The CS package uses the HL7 Version 2.2 protocol. Messages are based on the definitions found in the HL7 Interface Standards [1]. The CS package uses Version 1.6 of the HL7 package to assist in exchanging health care information with any NDES [2]. The HL7 package can be divided into two parts: lower level protocol support between sending and receiving applications and the **V** *IST* **A** interface to the HL7 protocol.

#### 43BLower Level Protocols

The term lower level refers to a portion of the Open Systems Interconnect (OSI) model. The OSI model is divided into seven layers or levels. The lower levels (layers 1 through 4) support the actual physical connection between the systems and the communications protocol used. The CS package will use the HL7 Hybrid Lower Layer Protocol over an RS-232 connection as supported by the HL7 package.

This lower level interface provides the following functions:

- Receive and send HL7 messages

- Validate the HL7 Message Header (MSH) information

- Invoke the appropriate **V** *IST* **A** application routine to process the data in the message

- Send HL7 acknowledgment (ACK) messages back to the sending application

#### 44BAcronyms

**ACK** Acknowledgment messages

**ADT** Admission, Discharge, Transfer

**CS** Controlled Substances

**DHCP** Decentralized Hospital Computer Program

**HL7** Health Level Seven

**MSH** Message Header

**NDES** Narcotic Dispensing Equipment System

**OSI** Open Systems Interconnect

#### 45BTerms

**Dispense**

Removal of medication by an authorized user, from a system cabinet, on behalf of a patient.

**Return**

The return of unused medication by an authorized user, to a system cabinet, that has previously been dispensed for a patient and not used. Medication that is returned can be reused, and is returned to the cabinet to be dispensed for another patient.

**Waste**

The return of partially used medication, by an authorized user, to a system cabinet, that has previously been dispensed for a patient and partially used. Medication that has been wasted is no longer usable.

#### 46BAssumptions and Dependencies

Each session is begun between the **V** *IST* **A** system and the NDES at startup and will remain active as long as the supporting network and systems are functioning. The **V** *IST* **A** system is independent of the NDES. Shut down or startup of the NDES will not adversely affect the **V** *IST* **A** system. Likewise, shut down or startup of the **V** *IST* **A** system should not adversely affect the NDES.

#### 47BReferences

[1]	Health Level Seven Interface Standards Version 2.2

[2]	DHCP Health Level 7 Developer Manual Version 1.5, July 1993

### 31BPurpose

This document specifies an interface to the Veterans Health Information Systems and Technology Architecture ( **V** *IST* **A** ) Controlled Substances V. 3.0 package based upon the Health Level 7 (HL7) protocol. It is intended that this interface form the basis for the exchange of health care information between the **V** *IST* **A** Controlled Substances V. 3.0 package and any Narcotic Dispensing Equipment Systems (NDES).

### 32BOverview

#### 48BStatement of Intent

The Birmingham Information Resources Management Field Office (IRMFO) is developing, and plans to implement, a generic interface to the HL7 protocol for use by the **V** *IST* **A** Controlled Substances V. 3.0 package in communicating with any NDES for the purpose of exchanging health care information. The interface will strictly adhere to the HL7 protocol and will avoid using Z type extensions to the protocol whenever possible.

#### 49BScope and Audience

This document describes messages that are exchanged between the **V** *IST* **A** Controlled Substances V. 3.0 package and any NDES for the purpose of exchanging information concerning controlled substances. It is intended for use by vendors wishing to offer proposals for the

Controlled Substances V. 3.0 system interface, as well as facilitate an understanding on the part of the VA clinicians, IRM personnel, and clinical database developers of the nature and types of data to be made available.

### 33BGeneral Specifications

#### 50BCommunication Protocol

The HL7 protocol defines only the seventh level of the Open System Interconnect (OSI) protocol. This is the application level. Levels one through six involve primarily communication protocols. The HL7 protocol provides some guidance in this area. The communication protocols that will be used for interfacing with the **V** *IST* **A** Controlled Substances V. 3.0 package will be based on the HL7 Hybrid Lower Level Protocol, which is described in the HL7 Implementation Guide.

#### 51BApplication Processing Rules

The HL7 protocol itself describes the basic rules for application processing by the sending and receiving systems. Information contained in the protocol will not be repeated here; therefore, anyone wishing to interface with the **V** *IST* **A** Controlled Substances V. 3.0 package should become familiar with the HL7 protocol Version 2.2.

#### 52BMessage Types

Both systems will send an acknowledgment (ACK) message when the incoming message has been validated for correct syntax and content and committed to storage.

The **V** *IST* **A** system will send admission, discharge, and transfer (ADT) messages to the NDES whenever an admission, discharge, or transfer event occurs.

The NDES will send pharmacy dispense messages (DFT) to **V** *IST* **A** whenever a dispense, return, or waste event occurs*.

#### 53BMessages

#### 58BADT Message Type

The ADT transaction set provides for transmitting new or updated patient demographic and visit information. The ADT message that the **V** *IST* **A** system will transmit to the NDES should contain the following segments:

| SEGMENT   | NAME                   | USER/HL7 DEFINED   |
|-----------|------------------------|--------------------|
| MSH       | Message Header         | HL7                |
| EVN       | Event Type             | HL7 (Table 0003)   |
| PID       | Patient Identification | HL7                |
| PV1       | Patient Visit          | HL7                |

#### 59BDFT Message Type

The DFT message will be transmitted by the NDES for each instance of dispensing drugs to a patient.

| SEGMENT   | NAME                   | USER/HL7 DEFINED   |
|-----------|------------------------|--------------------|
| MSH       | Message Header         | HL7                |
| EVN       | Event Type             | HL7 (Table 0003)   |
| PID       | Patient Identification | HL7                |
| PV1       | Patient Visit          | HL7                |
| FT1       | Financial Transaction  | HL7                |

#### 54BFields

The segment definition tables list and describe the data fields in the segment and characteristics of their usage. The following information is specified about each data field.

**Sequence Number (SEQ):** The ordinal position of the data field within the segment. This number is used to refer to the data field in the text comments that follow the segment definition table.

**Length (LEN):** The maximum number of characters that one occurrence of the data field may occupy.

**Data Type (DT):** Restrictions on the contents of the data field as defined by the HL7 Standard.

**Optionality (R/O/C):** Whether the data field is required, optional, or conditional in a segment. The designations are: R - required; O (null) - optional; and C - conditional on the trigger event.

**Repetition (RP/#):** Whether the field may repeat. The designations are: N (null) - for no repetition allowed; Y - the field may repeat an indefinite or site determined number of times; and (integer) - the field may repeat up to the number of times specified in the integer.

**Table (TBL#):** A table of values which may be defined by HL7 or negotiated between he **V** *IST* **A** application and the vendor system.

**Element Name:** Globally unique descriptive name for the field.

The following HL7 fields will be used to support the exchange of data for each of the segments listed in the segments paragraph. Tables referenced in the segments can be found in the HL7 Interface Standards document. For the standard HL7 segments, definitions of each element are provided for those fields, which are utilized. The field definitions can include specific information (e.g., expected format) for transmission.

#### 55BMessage Segment Definitions:

#### 60BMSA - Message Acknowledgment

The MSA segment contains information sent while acknowledging another message.

|   SEQ |   LEN | DT   | R/O   | RP/#   |   TBL# | ELEMENT NAME        |
|-------|-------|------|-------|--------|--------|---------------------|
|     1 |     2 | ID   | R     |        |      8 | Acknowledgment Code |
|     2 |    20 | ST   | R     |        |        | Message Control ID  |
|     3 |    80 | ST   |       |        |        | Text Message        |

MSA field definitions

(A) Acknowledgment Code (ID)

The ACKNOWLEDGMENT CODE can have the following values:

**HL7 Table 8 - ACKNOWLEDGMENT CODE**

| VALUE   | DESCRIPTION        |
|---------|--------------------|
| AA      | Application Accept |
| AE      | Application Error  |
| AR      | Application Reject |

(B) Message Control ID (ST)

This field identifies the message sent by the sending system. It allows the sending system to associate this response with the message for which it is intended.

(C) Message (ST)

This is an optional text field that further describes an error condition. The text may be printed in error logs or presented to an end user.

#### 61BMSH - Message Header

The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message.

|   SEQ |   LEN | DT   | R/O   | RP/#   |   TBL# | ELEMENT NAME          |
|-------|-------|------|-------|--------|--------|-----------------------|
|     1 |     1 | ST   | R     |        |        | Field Separator       |
|     2 |     4 | ST   | R     |        |        | Encoding Characters   |
|     3 |    15 | ST   |       |        |        | Sending Application   |
|     4 |    20 | ST   |       |        |        | Sending Facility      |
|     5 |    30 | ST   |       |        |        | Receiving Application |
|     6 |    30 | ST   |       |        |        | Receiving Facility    |
|     7 |    26 | TS   |       |        |        | Date/Time Of Message  |
|     8 |    40 | ST   |       |        |        | Security              |
|     9 |     7 | CM   | R     |        |     76 | Message Type          |
|    10 |    20 | ST   | R     |        |        | Message control ID    |
|    11 |     1 | ID   | R     |        |    103 | Processing ID         |
|    12 |     8 | ID   | R     |        |    104 | Version ID            |

MSH field definitions

Separator (ST)

This field is the separator between the segment ID and the first real field, MSH-2-encoding characters. It serves as the separator and defines the character to be used as a separator for the rest of the message. The **V** *IST* **A** system uses: |.

Encoding Characters (ST)

This field is four characters in the following order: the component separator, repetition separator, escape character and sub component separator. The **V** *IST* **A** system uses:^ ~\&amp;.

Sending Application (ST)

This field is used for interface with lower level protocols.

Sending Facility (ST)

This field addresses one of several occurrences of the same application within the sending system. It is entirely site-defined.

Receiving Application (ST)

This field is used for interface with lower level protocols.

Receiving Facility (ST)

This field identifies the receiving application among multiple identical instances of the application running on behalf of different organizations.

Date/Time Of Message (TS)

This field is the date/time that the sending system created the message. If the time zone is specified, it is used throughout the message as the default time zone.

Security (ST)

In some applications of HL7 this field is used to implement security features. Its use is not yet further specified.

Message Type (CM)

MESSAGE TYPE is a composite element made up of: &lt;message type&gt; &lt;trigger event&gt; The first component is the message type, found in table 76 - message type. The second component is the trigger event code found in table 3 - event type code. The receiving system uses this field to know the data segments to recognize, and possibly, the application to which to route this message.

Message Control ID (ST)

This field is a number or other identifier that uniquely identifies the message. The receiving system echoes this ID back to the sending system in the Message Acknowledgment segment (MSA).

Processing ID (ID)

This field is used to decide whether to process the message as defined in the HL7 application processing rules.

**HL7 Table 103 - PROCESSING ID**

| VALUE   | DESCRIPTION   |
|---------|---------------|
| D       | Debugging     |
| P       | Production    |
| T       | Training      |

VERSION ID (ID)

This filed is matched by the receiving system to its own version to be sure the message will be interpreted correctly. Only the following values are expected/accepted.

**HL7 Table 104 - VERSION ID**

|   VALUE | DESCRIPTION               |
|---------|---------------------------|
|     2.1 | Release 2.1 March 1990    |
|     2.2 | Release 2.2 December 1994 |

#### 62BERR - Error

The ERR segment is used to add error comments to acknowledgment messages.

|   SEQ |   LEN | DT   | R/O   | RP/#   |   TBL# | ELEMENT NAME            |
|-------|-------|------|-------|--------|--------|-------------------------|
|     1 |    80 | CM   | R     | Y      |     60 | Error Code and Location |

ERR field definitions

Error code and location (CM)

This field is in standard HL7 format.

#### 63BEVN - Event Type

The EVN segment is used to communicate necessary trigger event information to the NDES.

|   SEQ |   LEN | DT   | R/O   | RP/#   |   TBL# | ELEMENT NAME       |
|-------|-------|------|-------|--------|--------|--------------------|
|     1 |     3 | ID   | R     |        |   0003 | Event Type Code    |
|     2 |    19 | TS   | R     |        |        | Date/Time of Event |

EVN field definitions

Event Type Code (ID)

A01	Admit a patient

A02	Transfer a patient

A03	Discharge a patient

P03	Post detail financial transaction

Date/Time of Event (TS)

The date/time of the admission, transfer, discharge, or financial transaction.

#### 64BPID - Patient Identification

The PID segment is used by both applications as the primary means of communicating patient identification information. This segment contains permanent patient identifying, and demographic information that, for the most part, is not likely to change frequently.

|   SEQ |   LEN | DT   | R/O   | RP/#   | TBL#   | ELEMENT NAME             |
|-------|-------|------|-------|--------|--------|--------------------------|
|     1 |     4 | SI   |       |        |        | Set ID - Patient ID      |
|     2 |    16 | CK   |       |        |        | Patient ID (External ID) |
|     3 |    16 | CK   | R     | Y      |        | Patient ID (Internal ID) |
|     5 |    48 | PN   | R     |        |        | Patient Name             |

PID field definitions

Set ID - patient ID (SI)

This is a sequence number used to identify the segment repetitions.

Patient ID (External ID) (CK)

This is a composite element made up of: &lt;patient ID&gt; &lt;check digit&gt; &lt;check digit scheme&gt; &lt;assigning facility ID&gt; &lt;type&gt;

When the **V** *IST* **A** Controlled Substances V. 3.0 system transmits to the NDES, the first component is the social security number from the Patient file. The second and third components are the check digit and check digit scheme.

Patient ID (internal ID) (CM)

This is a composite element made up of: &lt;patient ID&gt; &lt;check digit&gt; &lt;check digit scheme&gt; &lt;assigning facility ID&gt; &lt;type&gt;

When the **V** *IST* **A** Controlled Substances V. 3.0 system transmits to the NDES, the first component is the unique internal entry number from the Patient file. The second and third components are the check digit and check digit scheme.

Patient name (PN)

This field is in standard HL7 format.

#### 65BPV1 - Patient Visit

The PV1 segment is used by Registration/ADT applications to communicate information on a visit specific basis.

|   SEQ |   LEN | DT   | R/O   | RP/#   | TBL#   | ELEMENT NAME              |
|-------|-------|------|-------|--------|--------|---------------------------|
|     1 |     4 | SI   |       |        |        | Set ID - Patient Visit    |
|     3 |    12 | CM   | R     |        |        | Assigned Patient Location |
|     6 |    12 | CM   |       |        |        | Prior Patient Location    |
|     7 |    60 | CN   | R     |        |        | Attending Doctor          |

PV1 field definitions

Set ID - patient visit (SI)

This is a sequence number used to identify the segment repetitions.

Assigned Patient Location

This is an HL7 ID type field that consists of three components: Nurse Unit (HL7 terminology), Room, and Bed. For the purposes of this interface, Nurse Unit will be considered synonymous with Ward Location.  The value of the Ward Location component of the Assigned field will be a one to three digit code.

Prior Patient Location

This is an HL7 ID type field that consists of three components: Nurse Unit (HL7 terminology), Room, and Bed. For the purposes of this interface, Nurse Unit will be considered synonymous with Ward Location. The value of the Ward Location component of the Prior Patient Locations field will be a one to three digit code.

Attending doctor (CN)

This field is in standard HL7 format.

#### 66BFT1 - Financial Transaction Segment

Housed in the DFT message, the FT1 segment is used for each instance of 	dispensing, returning, or wasting drugs for a patient.

|   SEQ |   LEN | LEN   | DT   | R/O   | R/O   | RP/#   | RP/#   | TBL#   | TBL#                     | ELEMENT NAME             |
|-------|-------|-------|------|-------|-------|--------|--------|--------|--------------------------|--------------------------|
|     2 |    12 | ST    | ST   | ST    |       |        |        |        | Transaction ID           | Transaction ID           |
|     4 |     8 | DT    | DT   | DT    | R     |        |        |        | Transaction Date         | Transaction Date         |
|     5 |     8 | DT    | DT   | DT    |       |        |        |        | Transaction Posting Date | Transaction Posting Date |
|     6 |     8 | ID    | ID   | ID    | R     |        |        |        | Transaction Type         | Transaction Type         |
|     7 |    20 | ID    | ID   | ID    | R     |        |        |        | Transaction Code         | Transaction Code         |
|    10 |     4 | NM    | NM   | NM    | R     |        |        |        | Transaction Quantity     | Transaction Quantity     |
|    20 |    60 | CN    | CN   | CN    | R     |        |        |        | Performed By Code        | Performed By Code        |

~~PV1 field definitions~~

Transaction ID (ST)

Number assigned by the sending system for control purposes. The number can be returned by the receiving system to identify errors.

Transaction Date (DT)

Date of transaction

Transaction Posting Date (DT)

Date the transaction was sent to **V** *IST* **A**

Transaction Type (ID)

D - Dispensed, R - Returned, W - Wasted

Transaction Code (ID)

Code for the purpose of uniquely identifying the transaction

Transaction Quantity (NM)

The quantity of medication dispensed, returned, or wasted.

Performed By Code (CN)

The composite number/name of the person, which performed the transaction, with number being the internal entry number (DUZ) from the **V** *IST* **A** NEW PERSON file (#200)

### 34BTransaction Specifications

#### 56BGeneral

The flow of transactions between the **V** *IST* **A** system and the NDES may occur in two ways.

1. The **V** *IST* **A** system will send ADT event type HL7 messages to the NDES whenever an admission, discharge, or transfer event occurs.

1. The NDES will send pharmacy dispense messages (DFT) to **V** *IST* **A** whenever a dispense, return, or waste event occurs.

#### 57BSpecific Transactions

#### 67BAdmit a Patient (Event Code A01)

When a patient is admitted, an ADT Message (ADT) with event code A01 is sent from the **V** *IST* **A** system to the NDES. These ADT messages would consist of the following segments.

**ADT	ADT MESSAGE**

MSH	Message Header

EVN	Event Type

PID	Patient Identification

PV1	Patient Visit

**Example: Admit a Patient (Event Code A01)**

MSH|^~\&amp;|PSD-CS|500|PSD-CS|NDES|199112202359||ADT^A01|12345-1|P|2.1

EVN|A01|19911220100020

PID|1|000-77-1640^8^M10|1^1^M10||CSPATIENT^ONE||||||||||||||

PV1||I|15^E200^2|||3333^CSPROVIDER^ONE

The NDES would then send a General Acknowledgment (ACK) message back to the **V** *IST* **A** system.

#### 68BTransfer (Event Code A02)

When a patient is transferred and their location or treating specialty changes, an ADT Message with event code A02 is sent from the **V** *IST* **A** system to the NDES. This ADT message would consist of the following segments.

**ADT	ADT MESSAGE**

MSH	Message Header

EVN	Event Type

PID	Patient Identification

PV1	Patient Visit

**Example: Transfer (Event Code A02)**

MSH|^~\&amp;|PSD-CS|500|PSD-CS|NDES|199112202359||ADT^A01|12345-1|P|2.1

EVN|A02|19911220100020

PID|1|000-77-1640^8^M10|1^1^M10||CSPATIENT^ONE||||||||||||||

PV1||I|15^E200^2|||3333^CSPROVIDER^ONE

The NDES would then send a General Acknowledgment (ACK) message back to the **V** *IST* **A** system.

#### 69BDischarge (Event A03)

When a patient is discharged, an ADT Message with event code A03 is sent from the **V** *IST* **A** system to the NDES. This ADT message would consist of the following segments.

**ADT	ADT MESSAGE**

MSH	Message Header

EVN	Event Type

PID	Patient Identification

PV1	Patient Visit

Example: Discharge (Event A03)

MSH|^~\&amp;|PSD-CS|500|PSD-CS|NDES|199112202359||ADT^A01|12345-1|P|2.1

EVN|A03|19911220100020

PID|1|000-77-1640^8^M10|1^1^M10||CSPATIENT^ONE||||||||||||||

PV1||I|15^E200^2|||3333^CSPROVIDER^ONE

The NDES system would then send a General Acknowledgment (ACK) message back to the **V** *IST* **A** system.

## 13BGlossary

**Action Prompt** There are two action prompts that occur during the pharmacy dispensing process. The action codes appear in “( )”. The following codes are valid:

**V** Verify or Dispense the order (Displayed only to the dispensing pharmacist)

**P** Process or Fill the order (Displayed only to the pharmacy technician or pharmacist filling but not dispensing the order)

**DC** Cancel the order

**E** Edit the order

**B** Bypass the order

**S** Show the order

**Completion Status** A review status is attached to each CS Green Sheet returned to pharmacy. 	The following are valid:

**NO DISCREPANCY—** No discrepancy found.

**TURN IN FOR DESTRUCTION** —CS drug turned in to be destroyed.

**RETURNED TO STOCK** —CS Drug returned to stock. The dispensing site inventory balance will be updated.

**MATH ERROR** —CS drug discrepancy found.

**GREEN SHEET NOT SIGNED BY NURSE** —GS missing nurse’s signature.

**OTHER - REFERRED TO PHARMACY SUPERVISOR** —CS drug discrepancy referred to supervisor for resolution.

**Daily Activity Log** The Daily Activity Log lists data, within a selected date range, associated with the VA FORM 10-2320 for a dispensing site.

**Dispensing #** Control number assigned by pharmacy when dispensing a CS drug. This 	number is used to track the Green Sheet and drug. Also referred to as the Disp #, Green Sheet #, or GS # throughout the CS package.

**Dispensing/Receiving** This report can be printed in lieu of VA FORM 10-2321

**Report (in lieu of** and lists all Controlled Substances orders dispensed to an

**VA FORM 10-2321)** NAOU. The signature of the dispensing pharmacist and the nurse receiving the drug are required.

**Dispensing Site** An NAOU set up as a pharmacy vault that dispenses CS drugs.

**Dispensing Worksheet** This worksheet compiles a list of all pending CS request orders for a selected dispensing site. A worksheet number, drug name, quantity ordered, requesting NAOU, ordered by, comments, and blanks for pharmacy dispensing number, manufacturer, lot number, and expiration date are listed on the worksheet.

**Drug Address Code** Text used to clarify the meaning of a drug address code.

**Expansion** For example, the code S would be expanded and printed as shelf. (These codes and expansions are locally created terms.)

**Drug Address Code** A code that represents the location of a drug in the

**(Location Code)** NAOU. For example, if TYLOX is stored in an NAOU on the second set of shelves, third shelf from the top, its drug address code could be expressed as S,2,3. The address code can consist of up to three levels separated by a comma. Each level should further define the exact location. The code is associated with an expansion for clarity.

**Green Sheet #** Control number assigned by pharmacy when dispensing a CS drug. This number is used to track the Green Sheet and drug. It is also referred to as the GS #, Dispensing #, or Disp # throughout the CS package.

**Green Sheet** The CONTROLLED SUBSTANCE 	ADMINISTRATION RECORD (VA FORM 10-2638) is referred to as a Green Sheet or GS throughout the CS package. Pharmacy dispensing number, drug name, expiration date, quantity dispensed, lot number, ordered by, dispensed by, and ward (NAOU) are printed on the form.

**Inpatient Site** Inpatient Site must be defined for each NAOU. The CS software utilizes this data to distinguish multi-divisional sites.

**Inspector’s Log** This report lists all active Green Sheets by NAOU. It includes the following information: Green Sheet #, drug name, date dispensed, quantity dispensed, expiration date (if available), blanks for quantity on hand, and a signature blank for verification.

**Interactive Reader** The Interactive Reader Language (IRL) is a language used

**Language (IRL)** to write programs on barcode readers that allow the reader to interact with the user.

**Master Vault** An NAOU set up as your primary dispensing site.

**NAOU Inventory Group** An NAOU Inventory Group is defined by pharmacy to represent the Narcotic Areas of Use, which are inventoried together as a group. By grouping the commonly inventoried NAOUs under an easy to remember group name, the elements of the inventory are established, and do not have to be redefined every time an inventory is scheduled.

**Narcotic Location** An NAOU set up for the nursing wards, pharmacy IV room, or a pharmacy working stock area.

**NAOU - Narcotic Area of Use** A Narcotic Area of Use (NAOU) is a place where commonly stocked CS drugs are stored for use by pharmacy, wards or treatment areas. There are three types of NAOUs: 1) Master Vault, 2) Satellite Vault and 3) Narcotic Locations.

**Order Status** A processing status is attached to each CS request order. The following are valid:

**ORDERED - NOT PROCESSED** —

Ordered by nursing but not processed by pharmacy.

**PROCESSED - NOT DISPENSED** —Processed (filled) by pharmacy but not yet dispensed.

**FILLED - NOT DELIVERED** —Dispensed and verified by pharmacy but not delivered to the requesting NAOU.

**DELIVERED - ACTIVELY ON NAOU** —Drug stored on the NAOU.

**COMPLETED - GREEN SHEET READY FOR PICKUP** —Nursing has flagged the Green Sheet ready for pharmacy pickup.

**COMPLETED - GREEN SHEET PICKED UP** —Green Sheet returned to pharmacy but not yet reviewed.

**COMPLETED - REVIEWED** —Pharmacy has reviewed the Green Sheet.

**COMPLETED - PENDING PROBLEM RESOLUTION** —Pharmacy has reviewed the Green Sheet and a problem exists.

**CANCELLED—** Order cancelled.

**TRANSFERRED TO ANOTHER NAOU—** Order and drug transferred to another NAOU.

**UNDER REVIEW BY INSPECTOR—** Order and drug pulled from NAOU by CS Inspector for review.

**LOGGED BY TRAKKER—** All drug doses from this order have been logged out to patients using the TRAKKER.

**PSD ERROR** Allocate this key to pharmacy supervisors responsible for maintaining the narcotic vault. This key controls access to reports listing various 	errors and exception conditions generated when entries are filed from the barcode TRAKKER. Also, the holders of this key will receive electronic mail messages created by using the TRAKKER.

**PSD NURSE** Allocate this key to nurses, usually LPNs, who may only receive and administer controlled substances drugs, but cannot place order requests.

**PSD PARAM** Allocate this key to **only** the Inpatient Pharmacy Coordinators. This key controls the printing of the Green Sheets and the range of automated dispensing numbers for a dispensing site.

**PSD TECH** Allocate this key to control substance technicians. This key controls access to the *List On-Hand Amounts* [PSD ON-HAND TECH], *Transfer Drugs between Dispensing Sites Report* [PSD PRINT VAULT TRANSFERS TECH], and the *Daily Activity Log (in lieu of VA FORM 10-2320)* [PSD DAILY LOG TECH] options on the *Technician (CS Pharmacy) Menu* [PSD PHARM TECH].

**PSD TECH ADV** Allocate this key to specific control substance technicians who perform advance functions. This key controls access to the *Receipts Into Pharmacy* [PSD RECEIPTS MENU], *Dispensing Menu* [PSD DISPENSING MENU], *Destructions Menu* [PSD DESTROY MENU], *Manufacturer, Lot #, and Exp. Date - Enter/Edit* [PSD MFG/LOT/EXP], *Outpatient Rx's* [PSD OUTPATIENT], *Complete Green Sheet* [PSD COMPLETE GS], *Destroyed Drugs Report* [PSD DEST DRUGS REPORT], *DEA Form 41 Destroyed Drugs Report* [PSD DESTROY DEA41], *Destructions Holding Report* [PSD DESTRUCTION HOLDING], *Add Existing Green Sheets at Setup* [PSD EXISTING GS], *Green Sheet Transfer Between NAOUs Report* [PSD GS TRANSFER (NAOU) REPORT], *NAOU Usage Report* [PSD NAOU USAGE], *Transfer Drugs between Dispensing Sites* [PSD TRANSFER VAULT DRUGS] options on the *Technician (CS Pharmacy) Menu* [PSD PHARM TECH]. The CS technician may perform all functions of the *Outpatient Rx’s* [PSD OUTPATIENT] option except releasing prescriptions.

**PSD TRAN** Allocate this key only to the Inpatient Pharmacy Coordinator. This key controls the access to the *NAOU to NAOU Transfer Stock Entries* [PSD TRANSFER NAOU] option. Users can copy stock entries from one NAOU into another NAOU or from an Auto Replenishment/Ward Stock (AR/WS) Area Of Use (AOU) into an NAOU.

**PSDMGR** Allocate this key to the Inpatient Pharmacy Coordinators. This key controls the editing of CS files for package set up and it locks the *Supervisor (CS) Menu* option.

**PSDRPH** This key authorizes pharmacists to verify and dispense controlled substance prescription(s). The PSDRPH security key should be given to registered pharmacists working on controlled substances to honor Drug Enforcement Administration (DEA) regulations and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist.

**PSJ PHARM TECH** Allocate this key to pharmacy technicians handling controlled substances orders.

**PSJ RNURSE** Allocate this key to nurses who request and receive controlled substances orders on the wards.

**PSJ RPHARM** Allocate this key to pharmacists who can dispense and receive controlled substances drugs.

**Satellite Vault** An NAOU set up as a secondary dispensing site.

**Stock Drug** A drug (from the drug file (#50)) stored in an 	NAOU.

**Stock Level** The quantity of a drug stocked in a specific NAOU.

**TRAKKER** A barcode collection system utilized by scanning 	barcode labels or pressing the keypad.

**V** ***IST*** **A** Veterans Health Information Systems and Technology Architecture

**Ward (for Drug)** The name of the ward or wards that will use this particular drug. It is important to accurately answer this prompt because this is the link between the Inpatient Medications V. 5.0 package and the Controlled Substances V. 3.0 package. The Inpatient Medications V. 5.0 package looks at this field to know if the drug is a CS stocked drug.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Controlled Substances Version 3 Technical Manual (Updated PSD*3*89)

## CONTROLLED SUBSTANCES (CS)

## TECHNICAL MANUAL

## Version 5.0 March 1997

## Revision History

The table below lists changes made since the initial release of this manual. Use the Change Pages document to update an existing manual or use the entire updated manual.

| Date    | Revised Pages         | Patch Number   | Description                                                                                                                                                                                                                                                                                                                                                                                |
|---------|-----------------------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 11/2021 | 18, 19, 21, 44        | PSD*3*89       | Changed the Option Menu Text for two reports: PSD DIGITALLY SIGNED ORDERS - OP CS Orders Report PSD DIG. SIGNED RELEASED RX - OP Released Rx Report Added filters to three reports to allow choosing the source of reported prescriptions - CPRS, eRx, CPRS+eRx, Written, or All. PSD CS PRESCRIPTIONS REPORT PSD DIGITALLY SIGNED ORDERS PSD DIG. SIGNED RELEASED RX                      |
| 11/2018 | 18, 43, 65            | PSD*3*84       | Updated the PSD DAILY LOG and PSD DAILY LOG TECH option descriptions to add the ^ALL CII DRUGS group name to search for all Schedule II drugs. Updated the PSD OUTPATIENT option description to include a new prompt requiring pharmacists to enter a narcotic on-hand count that is confirmed against the VistA on-hand count. Updated the number of routines in the CS package. REDACTED |
| 06/2018 | 109                   | PSD*3*82       | Added NAOU Usage Report [PSD NAOU USAGE] option to the PSD TECH ADV key. REDACTED                                                                                                                                                                                                                                                                                                          |
| 05/2013 | i, 18-18b, 45         | PSD*3*73       | Added two new options to Descriptions table. Added two new reports to Production Reports Menu. REDACTED                                                                                                                                                                                                                                                                                    |
| 05/2013 | i, 41c, 96-98         | PSD*3*76       | Page 41c is no longer necessary and has been removed. Updated Glossary with description of patch's new security key PSDRPH REDACTED                                                                                                                                                                                                                                                        |
| 04/2011 | i, 15, 41- 41c, 97-98 | PSD*3*71       | Clarified description of PSD TECH ADV key. Corrected option name in PSD TRAN entry. Made revision to PSD PHARM TECH option description. REDACTED                                                                                                                                                                                                                                           |
| 05/2010 | 15, 41-41c, 97-98     | PSD*3*69       | Added description of patch's new security key PSD TECH ADV, and options from the pharmacist menu added to the Technician (CS Pharmacy) Menu [PSD PHARM TECH], which allow holders of this new key to perform these additional functions. REDACTED                                                                                                                                          |
| 08/08   | 24, 37, 39, 40        | PSD*3*64       | New menu options added to the Transfer Green Sheet Menu REDACTED                                                                                                                                                                                                                                                                                                                           |

| 07/03   | 19-20, 44-45   | PSD*3*40   | Added two new reports associated with the Electronic Order Entry for Schedule II Controlled Substances project to the Production Repo rts [PSD PRODUCTION REPORTS] menu: Digitally Signed CS Orders Report [PSD DIGITALLY SIGNED ORDERS] and Digitally Signed OP Released Rx Report [PSD DIG. SIGNED RELEASED RX].   |
|---------|----------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 04/03   | All            | PSD*3*41   | Updated the manual to Standards. Added the CS Monitoring Menu options and routines.                                                                                                                                                                                                                                  |
| 03/97   |                |            | Original Released Technical Manual.                                                                                                                                                                                                                                                                                  |

&lt;This page is intentionally left blank.&gt;

## Table of Contents

| 1. 0BIntroduction.................................................................................................................. 1   | 1. 0BIntroduction.................................................................................................................. 1   | 1. 0BIntroduction.................................................................................................................. 1   |   1. 0BIntroduction.................................................................................................................. 1 |
|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                                                         | 1.1.                                                                                                                                    | 14BOrientation............................................................................................................              |                                                                                                                                       1 |
|                                                                                                                                         | 1.2.                                                                                                                                    | 15BPackage Functional Description ...........................................................................                           |                                                                                                                                       3 |
|                                                                                                                                         | 1.3.                                                                                                                                    | 16BPackage Management..........................................................................................                         |                                                                                                                                       3 |
| 2.                                                                                                                                      | 1BImplementation and Maintenance...............................................................................                         | 1BImplementation and Maintenance...............................................................................                         |                                                                                                                                       5 |
|                                                                                                                                         | 2.1.                                                                                                                                    | 17BInstallation............................................................................................................             |                                                                                                                                       5 |
|                                                                                                                                         | 2.2.                                                                                                                                    | 18BSite Parameters....................................................................................................                  |                                                                                                                                       5 |
| 3.                                                                                                                                      | 2BRoutines.......................................................................................................................       | 2BRoutines.......................................................................................................................       |                                                                                                                                       7 |
|                                                                                                                                         | 3.1.                                                                                                                                    | 19BDescriptions .........................................................................................................               |                                                                                                                                       7 |
|                                                                                                                                         | 3.2.                                                                                                                                    | 20BChecksum............................................................................................................                 |                                                                                                                                       7 |
|                                                                                                                                         | 3.3.                                                                                                                                    | 21BCallable Routines .................................................................................................                  |                                                                                                                                       8 |
|                                                                                                                                         | 3.4.                                                                                                                                    | 22BRoutine Mapping..................................................................................................                    |                                                                                                                                       8 |
| 4.                                                                                                                                      | 3BFile List.........................................................................................................................    | 3BFile List.........................................................................................................................    |                                                                                                                                       9 |
| 5.                                                                                                                                      | 4BArchiving and Purging ...............................................................................................11               | 4BArchiving and Purging ...............................................................................................11               |                                                                                                                                         |
|                                                                                                                                         | 5.1.                                                                                                                                    | 23BArchiving .............................................................................................................11            |                                                                                                                                         |
|                                                                                                                                         | 5.2.                                                                                                                                    | 24BPurging................................................................................................................11            |                                                                                                                                         |
| 6.                                                                                                                                      | 5BExternal Relationships ...............................................................................................13              | 5BExternal Relationships ...............................................................................................13              |                                                                                                                                         |
| 7.                                                                                                                                      | 6BInternal Relationships ................................................................................................15             | 6BInternal Relationships ................................................................................................15             |                                                                                                                                         |
| 8.                                                                                                                                      | 7BExported Options........................................................................................................15            | 7BExported Options........................................................................................................15            |                                                                                                                                         |
|                                                                                                                                         | 8.1.                                                                                                                                    | 25BStand-Alone Options ...........................................................................................15                    |                                                                                                                                         |
|                                                                                                                                         | 8.2.                                                                                                                                    | 26BDescriptions ........................................................................................................15              |                                                                                                                                         |
| 9.                                                                                                                                      | 8BPackage-Wide Variables............................................................................................63                  | 8BPackage-Wide Variables............................................................................................63                  |                                                                                                                                         |
| 9.1.                                                                                                                                    | 27BPackage-Wide Variables ....................................................................................63                        | 27BPackage-Wide Variables ....................................................................................63                        |                                                                                                                                         |
| 9.2.                                                                                                                                    | 28BPackage Variables ..............................................................................................63                   | 28BPackage Variables ..............................................................................................63                   |                                                                                                                                         |
| 10.                                                                                                                                     | 9BResource Requirements.........................................................................................65                      | 9BResource Requirements.........................................................................................65                      |                                                                                                                                         |
|                                                                                                                                         | 10.1. 29BHardware Requirements......................................................................................65                  | 10.1. 29BHardware Requirements......................................................................................65                  |                                                                                                                                         |
|                                                                                                                                         | 10.1.1. 35BPrinting of Bar Codes...................................................................................66                   | 10.1.1. 35BPrinting of Bar Codes...................................................................................66                   |                                                                                                                                         |
|                                                                                                                                         | 10.1.2.                                                                                                                                 | 36BHP LaserJet Printer .....................................................................................67                          |                                                                                                                                         |
|                                                                                                                                         | 10.1.3. 37BOTC Printer .................................................................................................69              | 10.1.3. 37BOTC Printer .................................................................................................69              |                                                                                                                                         |
|                                                                                                                                         | 10.1.4. 38BKYOCERA Printer .......................................................................................69                    | 10.1.4. 38BKYOCERA Printer .......................................................................................69                    |                                                                                                                                         |
|                                                                                                                                         | 10.1.5. 39BPortable Barcode Reader (TRAKKER 9440)................................................71                                     | 10.1.5. 39BPortable Barcode Reader (TRAKKER 9440)................................................71                                     |                                                                                                                                         |
| 11.                                                                                                                                     | 10.1.6. 40BInterfacing the TRAKKER 9440 to a VT-320 Auxiliary Port ..........................77                                         | 10.1.6. 40BInterfacing the TRAKKER 9440 to a VT-320 Auxiliary Port ..........................77                                         |                                                                                                                                         |
|                                                                                                                                         | 10BHow to Generate On-line Documentation............................................................84                                  | 10BHow to Generate On-line Documentation............................................................84                                  |                                                                                                                                         |
| 12.                                                                                                                                     | 11BAdditional Information..........................................................................................86                   | 11BAdditional Information..........................................................................................86                   |                                                                                                                                         |

| 13.                                                                                                                              | 12BAppendix A Health Level 7 (HL7) .........................................................................88                   | 12BAppendix A Health Level 7 (HL7) .........................................................................88              |
|----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| 13.1.                                                                                                                            | 30BIntroduction .........................................................................................................88      | 30BIntroduction .........................................................................................................88 |
| 13.1.1.                                                                                                                          | 13.1.1.                                                                                                                          | 42BGeneral Description.....................................................................................88               |
| 13.1.2.                                                                                                                          | 13.1.2.                                                                                                                          | 43BLower Level Protocols .................................................................................88                |
| 13.1.3.                                                                                                                          | 13.1.3.                                                                                                                          | 44BAcronyms ....................................................................................................89          |
| 13.1.4.                                                                                                                          | 13.1.4.                                                                                                                          | 45BTerms..........................................................................................................89        |
| 13.1.5.                                                                                                                          | 13.1.5.                                                                                                                          | 46BAssumptions and Dependencies..................................................................90                         |
| 13.1.6.                                                                                                                          | 13.1.6.                                                                                                                          | 47BReferences..................................................................................................90           |
| 13.2.                                                                                                                            | 31BPurpose...............................................................................................................90      | 31BPurpose...............................................................................................................90 |
| 13.3. 32BOverview.............................................................................................................90 | 13.3. 32BOverview.............................................................................................................90 |                                                                                                                             |
| 13.3.1.                                                                                                                          | 13.3.1.                                                                                                                          | 48BStatement of Intent ......................................................................................90             |
| 13.3.2.                                                                                                                          | 13.3.2.                                                                                                                          | 49BScope and Audience....................................................................................90                 |
| 13.4.                                                                                                                            | 33BGeneral Specifications ........................................................................................91             | 33BGeneral Specifications ........................................................................................91        |
| 13.4.1.                                                                                                                          | 13.4.1.                                                                                                                          | 50BCommunication Protocol..............................................................................91                   |
| 13.4.2.                                                                                                                          | 13.4.2.                                                                                                                          | 51BApplication Processing Rules ......................................................................91                    |
| 13.4.3.                                                                                                                          | 13.4.3.                                                                                                                          | 52BMessage Types ...........................................................................................91              |
| 13.4.4.                                                                                                                          | 13.4.4.                                                                                                                          | 53BMessages....................................................................................................92           |
| 13.4.5.                                                                                                                          | 13.4.5.                                                                                                                          | 54BFields...........................................................................................................93      |
| 13.4.6.                                                                                                                          | 13.4.6.                                                                                                                          | 55BMessage Segment Definitions: ....................................................................94                      |
| 13.5. 34BTransaction Specifications.................................................................................102          | 13.5. 34BTransaction Specifications.................................................................................102          | 13.5. 34BTransaction Specifications.................................................................................102     |
| 13.5.1.                                                                                                                          | 13.5.1.                                                                                                                          | 56BGeneral......................................................................................................102         |
| 13.5.2.                                                                                                                          | 13.5.2.                                                                                                                          | 57BSpecific Transactions.................................................................................102                |

## 0B Introduction

The Controlled Substances V. 3.0 module provides functionality to monitor and track the receipt, inventory, and dispensing of all controlled substances. This module provides the pharmacy with the capability to define a controlled substance location and a list of controlled substances to maintain a perpetual inventory. The capability for pharmacy personnel to receive a controlled substance order automatically, updating the quantity on hand and receipt history is also provided. Nursing personnel are provided with the capability to request orders for controlled substances via on-demand requests. Pharmacy may dispense controlled substances via the software automating all necessary documents (VA FORMs 10-2321 and 10-2638) to complete an order request. The software provides functionality to address returns to stock, destructions, and transfers between locations; log outpatient prescriptions and order cancellations; report Automated Management Information System (AMIS) and cost data; and maintain perpetual inventory balances.

## 14B Orientation

This manual is divided into sections addressing such items as routines, files, security, options, etc. to provide a method of quick reference for the Site Manager and Information Resources Management (IRM) and Automated Data Processing (ADP) staff. For more detailed information about the package functionality, refer to the Controlled Substances V. 3.0 User Manual.

Within this documentation, several notations need to be outlined.

-  Menu options will be italicized. Example: Controlled Substance Balances Report indicates a menu

option.

-  Screen prompts will be denoted with quotation marks around them. Example: 'Select INPATIENT SITE NAME' indicates a screen prompt.
-  Responses in bold face indicate what the user is to type in. Example: Okay to Continue? No// Y ES.
-  Text centered between arrows represents a keyboard key that needs to be pressed in order for the system to capture a user response or move the cursor to another field. &lt;Enter&gt; indicates that the Enter key (or Return key on some keyboards) must be pressed. &lt;Tab&gt; indicates that the Tab key must be pressed.

Example:

Press &lt;Tab&gt; to move the cursor to the next field.

Press &lt;Enter&gt; to select the default.

-  Note : Indicates especially important or helpful

information.

<!-- image -->

-  Options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option. Example: The PSDMGR key is required. Please contact the Pharmacy Supervisor.
-  ? , ?? , ??? One, two, or three question marks can be entered at any of the prompts for on-line help. One question mark elicits a brief statement of what information is appropriate for the

prompt. Two question marks provide more help, plus the hidden actions and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

-  ^ Up Caret (arrow or a circumflex) and pressing &lt;Enter&gt; can be used to exit the current option.

## 15B Package Functional Description

The Controlled Substances V. 3.0 software process usually consists of the following functions:

-  Pharmacy set up of narcotic vaults and nursing wards (Narcotic Area Of Use - NAOUs).
-  Monitors/tracks the receipt, inventory, and dispensing of controlled substances.
-  Allows management inspections to automatically identify discrepancies in stock levels.
-  Allows nursing to place orders for controlled substances via on-demand requests.
-  Allows pharmacy to dispense controlled substance drugs, update on-hand balances, automate VA FORM 10-2321, and print VA FORM 10-2638.
-  Review VA FORM 10-2638 when completed and returned to pharmacy.
-  Provides AMIS and cost reporting data.
-  Maintains perpetual inventory balances.
-  Provides ability to return to stock, transfer between locations, cancel orders, and log outpatient prescriptions.
-  Automates current inventory requirements, which allows Department of Veterans Affairs Medical Centers (VAMCs) to detect discrepancies or diversions of controlled substances, thereby improving overall drug accountability.
-  Display history of actions taken on controlled substances orders.

## 16B Package Management

This package does not impose any additional legal requirements on the user, nor does it relieve the user of any legal requirements. Names and social security numbers used in the examples are fictitious.

## &lt;This page is intentionally left blank.&gt;

## 1B Implementation and Maintenance

## 17B Installation

For installation of the Controlled Substances (CS) V. 3.0 software package, please refer to the Installation Guide.

## 18B Site Parameters

The following is the site parameter that is used in defining the CS module for each site.

##  IS SITE SELECTABLE FOR CS

How should the IS SITE SELECTABLE FOR CS parameter be answered? This parameter was created because Inpatient Medications V. 5.0, Auto Replenishment/Ward Stock V. 2.3, and Controlled Substances V. 3.0 share the INPATIENT SITE file (#59.4). Therefore, this parameter will screen out inpatient site names that are not used by the Controlled Substances V. 3.0 module. For every entry in this file, it should be determined if the site name should be shown to the users of the Controlled Substances V. 3.0 package. If the site name should be shown, enter 1 or YES for this parameter, otherwise, enter 0 or NO .

## &lt;This page is intentionally left blank.&gt;

## 2B Routines

## 19B Descriptions

Use the following option to print routine descriptions:

## Example: Print Routine Descriptions

```
Select Systems Manager Menu Option: PRO grammer Options Select Programmer Options Option: ROU tine Tools Select Routine Tools Option: FIR st Line Routine Print PRINTS FIRST LINES routine(s) ? > PSD* searching directory ... routine(s) ? > (A)lpha, (D)ate ,(P)atched, OR (S)ize ORDER: A// <Enter> Include line 2? NO// <Enter> DEVICE: HOME// <Enter>
```

## 20B Checksum

This option determines the current checksum of selected routine(s).

The Checksum of the routine is determined as follows:

1. Any comment line with a single semi-colon is (presumed) to be followed by comments and only the line tag will be included.
2. Line 2 will be excluded from the count.
3. The total value of the routine is determined by taking, excluding the exception, as noted above, and multiplying the ASCII value of each character by its position on the line being checked.

## Example: Checksum Option

```
>D CHECK^XTSUMBLD routine(s) ? > PSD* searching directory . <Enter> .. routine(s) ? > <Enter> -----------------------------------------example follows -----------------------------------------
```

## Example: Checksum Option (continued)

```
PSDNMBA value = 7638815 PSDNMKY value = 5224255 PSDNMPR value = 7345943 PSDNMRP value = 7410643 PSDNMSP value = 6584930 PSDNMU value = 6690662
```

```
PSDNMWE value = 10976237
```

## 21B Callable Routines

None of the Controlled Substances V. 3.0 routines are designed for calling outside of the package.

## 2 B Routine Mapping

There are no specific recommendations for routine mapping.

## 3B File List

The following files are owned by the Controlled Substances V. 3.0 package:

```
58.82 CS ORDER STATUS 58.83 CS COMPLETION STATUS 58.84 DRUG ACCOUNTABILITY TRANSACTION TYPE 58.85 CS WORKSHEET 58.86 CS DESTRUCTION 58.87 CS CORRECTION LOG 58.88 CS IRL PROGRAM 58.89 CS ERROR LOG 59.4 INPATIENT SITE
```

For a complete list of the files and templates exported by the CS module use the Build File Print option, which is a Kernel Installation and Distribution System (KIDS) option.

```
> D ^XQ1 Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System Select Kernel Installation & Distribution System Option: Ut ilities Select Utilities Option: BUI ld File Print Select BUILD NAME: CONTR OLLED SUBSTANCES 3.0 DEVICE: [Select Print Device]
```

<!-- image -->

## 4B Archiving and Purging

## 23B Archiving

At present, the CS module does not provide for the archiving of its data.

## 24B Purging

## Auto-Purging

There is a background job, which should be scheduled through TaskMan to run each night at a convenient time. The routine should run nightly; therefore the rescheduling frequency is 1D. The purpose of the option is to purge the CS WORKSHEET file (#58.85). This file is the holding area for CS order requests pending pharmacy processing. The data should remain in the file until the orders have been received in an NAOU or cancelled by pharmacy. Once the order is received on an NAOU or cancelled, the data is purged from the system through this background job.

Using the TaskMan Manager's Schedule/Unschedule Options [XUTM SCHEDULE] option, select the Purge CS WORKSHEET File [PSD PURGE] option. At the 'QUEUED TO RUN AT WHAT TIME:' prompt, enter T@ followed by the time the job is to begin. The time should be one that does not conflict with system backup. At the 'RESCHEDULING FREQUENCY:' prompt, enter 1D . The 'DEVICE FOR QUEUED JOB OUTPUT' prompt should remain blank since this is a background job.

## 70B Example: How to Schedule a TaskMan Task

```
Select Systems Manager Menu Option: TASK Manager Select Task Manager Option: SCH edule/Unschedule Options Select OPTION to schedule or reschedule: PSD PURGE QUEUED TO RUN AT WHAT TIME: T@2200 DEVICE FOR QUEUED JOB OUTPUT: <Enter> RESCHEDULING FREQUENCY: 1D QUEUED TO RUN ON VOLUME SET: [At this prompt, select the Volume Set name that the option should run on.] SPECIAL QUEUEING: <Enter> Select OPTION to schedule or reschedule: <Enter>
```

## &lt;This page is intentionally left blank.&gt;

## 5B External Relationships

The Controlled Substances V. 3.0 module relies on, at least, the following external packages to run effectively:

| Package                         |   Minimum version needed |
|---------------------------------|--------------------------|
|  Kernel                        |                      8   |
| VA FileMan                      |                     21   |
| MailMan                         |                      7.1 |
| Nursing                         |                      2.5 |
| * Outpatient Pharmacy           |                      6   |
|  Auto Replenishment/Ward Stock |                      2.2 |
| Inpatient Medications           |                      4   |
| Drug Accountability             |                      2   |
| Integrated Billing              |                      2   |
|  Health Level 7 (HL7)          |                      1.6 |

To run this module, the NEW PERSON file (#200), WARD LOCATION file (#42), DRUG file (#50), PHARMACY SYSTEM file (#59.7), INPATIENT SITE file (#59.4), and PRESCRIPTION file (#52) files are needed. The system does not need to be taken down, but the CS and Drug Accountability menus must be made unavailable to the users. This is now handled within the KIDS install process.

-  Patches XU*8*26 and XU*8*44 must be installed to support the witness identification for Nurse dispensing functionality and the HL7 interface.
-  Please note that patch PSGW* 2.2*2 should be installed to ensure compatibility between AR/WS V. 2.2 and Controlled Substances V. 3.0.
* Patch PSO*6*134 should be installed to ensure compatibility between Outpatient V. 6.0 and Controlled Substances V. 3.0.
-  This package is required to support the Health Level 7 (HL7) Interface to Narcotic dispensing Equipment Systems.

## &lt;This page is intentionally left blank.&gt;

## 6B Internal Relationships

All of the Controlled Substances V. 3.0 package options have been designed to stand-alone. Each option requires the use of the package-wide variable PSDSITE that is set as users enter the package. Even though all options are independently invoked, users will be repeatedly asked to select an Inpatient Site (if there are two or more sites that are flagged as selectable for CS use) if top-level CS menus do not contain the following entry and exit code in the OPTION file (#19):

```
ENTRY ACTION: I '$D(PSDSITE) D ^PSDSET EXIT ACTION : K PSDSITE
```

The entry and exit code should not be included on submenus in order to preserve the variable PSDSITE.

## 7B Exported Options

## 25B Stand-Alone Options

All of the CS package options have been designed to stand alone. All pharmacy personnel may be assigned the Controlled Substances Menu [PSD MENU] as a menu option. Pharmacy managers may be assigned the CS Monitoring Menu [PSD NM MENU] option. All nursing personnel, using the CS software, may be assigned the Controlled Substances Nurses' (CS) Menu [PSD NURSE MENU] as a menu option. Controlled Substances inspectors may be assigned the Controlled Substances Inspector Menu [PSD INSPECTOR MENU] option and the CS Monitoring Menu [PSD NM MENU] option. Each option utilizes the package-wide variable PSDSITE that is set as users enter the package.

Controlled Substances (CS) V. 3.0 package technicians may be assigned the Technician (CS Pharmacy) Menu [PSD PHARM TECH] option. They may also be assigned the PSD TECH ADV security key. With the PSD TECH ADV security key, technicians can perform the functions from the pharmacist menu that have been added to the Technician (CS Pharmacy) Menu [PSD PHARM TECH]. The CS technician may perform all the Outpatient Rx's menu functions except releasing prescriptions.

## 26B Descriptions

| Option Name                   | Routine   | Menu Text / Description                                                                                                           |
|-------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| PSD AMIS                      | PSDAMIS   | AMIS Report This option provides the pharmacy with AMIS report information by NAOU.                                               |
| PSD BALANCE ADJUSTMENT REVIEW | PSDADJD   | Balance Adjustment Report This report allows the selection of drugs and a date range for which to review all balance adjustments. |

| Option Name                          | Routine    | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD BALANCE ADJUSTMENTS Lock: PSDMGR | PSDADJ     | Balance Adjustments This option is used to review or enter adjustments needed to correct the balance of a drug. CS drugs not dispensed with a VA FORM 10-2638 returned to stock or returned to manufacturer and held for destruction are deducted from the vault on-hand amount using this option.                                                                                                                                                                                                                                                                                     |
| PSD BALANCE INITIALIZE               | PSDADJI    | Initialize Balance at Setup This option will be used at package initialization only. It provides pharmacy a method of entering on-hand balances for CS drugs stocked within their dispensing vaults. The drugs will be listed alphabetically, displaying narcotic breakdown and package size for each. This option should be used only when the CS package is ready to be "turned on" for production use.                                                                                                                                                                              |
| PSD COMPLETE GS                      | PSDGSRV    | Complete Green Sheet Pharmacy uses this option to complete a reviewed Green Sheet. Green Sheets with no discrepancies, math errors, drugs returned to stock, and drugs holding for destruction, associated with this Green Sheet, are processed utilizing this option.                                                                                                                                                                                                                                                                                                                 |
| PSD CORRECT EXISTING GS              | EN2^PSDCOR | Existing Green Sheets Correction This option allows the pharmacy supervisor access to make corrective actions on CS orders. The CS software allows pharmacy to add existing Green Sheets active orders on an NAOU at package setup. These orders may be tracked using the CS software. Sometimes one of these existing Green Sheets may be incorrectly entered in the software. Using this option, the pharmacy supervisor may delete this erroneous existing Green Sheet. An entry in the CS CORRECTION LOG file (#58.87) will be created to log a history of all corrective actions. |
| PSD CORRECT GS STATUS                | EN3^PSDCOR | Error on Completed Green Sheets This option allows the Pharmacy Supervisor to correct the completed status of a Green Sheet from COMPLETED - REVIEWED to COMPLETED - PENDING PROBLEM RESOLUTION. An entry in the CS CORRECTION LOG file (#58.87) will be created to track this error.                                                                                                                                                                                                                                                                                                  |

| Option Name        | Routine    | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD CORRECT STATUS | EN1^PSDCOR | Correct Order Status - GS Ready for Pickup This option allows the Pharmacy Supervisor access to correct the order status of certain CS orders. Sometimes nursing may erroneously flag a Green Sheet ready for pharmacy pickup. Using this option, the Pharmacy Supervisor may change the Green Sheet order status from COMPLETED - GREEN SHEET READY FOR PICKUP to DELIVERED - ACTIVELY ON NAOU to correct this problem. An entry in the CS CORRECTION LOG file (#58.87) will be created to log a history of all corrective actions.                                                                                                                                     |
| PSD CORRECTION LOG |            | Correction Menu This menu option allows the pharmacy supervisor access to make corrective actions on CS orders. An entry in the CS CORRECTION LOG file (#58.87) will be created to log a history of all corrective actions. Menu Items: PSD CORRECT STATUS Correct Order Status - GS Ready for Pickup PSD CORRECT EXISTING GS Existing Green Sheets Correction PSD EDIT/CANC VER ORD Edit/Cancel Verified Orders PSD CORRECT GS STATUS Error on Completed Green Sheets PSD ERR/ADJ PENDING REPORT List Pending Errors/Adjustments Logged by TRAKKER PSD ERR/ADJ RESOLVED REPORT Print Resolved Errors/Adjustments Log PSD ERR/ADJ EDIT Enter Error/Adjustment Resolution |

| Option Name                       | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD CORRECTION LOG REPORT         | PSDCORP   | Correction Log Report This report lists all corrective actions logged for a selected date range. This report may be generated by order status changes or by Green Sheet deletions.                                                                                                                                                                                                                                                                                                                    |
| PSD COST REPORTS                  | PSDCOST   | Cost Reports This option provides pharmacy cost reporting data for CS drugs, by NAOU, for a specified date range.                                                                                                                                                                                                                                                                                                                                                                                     |
| PSD CP TRANSACTION REVIEW         | PSDREVC   | Control Point Transaction Review Use this option to review the receipt transactions processed for a selected control point transaction number.                                                                                                                                                                                                                                                                                                                                                        |
| PSD CS PRESCRIPTIONS REPORT       | PSDDSOR   | Controlled Substance Prescriptions Report This option provides a report of digitally signed orders that have been filled for Schedules I-V controlled substances. The report is for a date range with the option of selecting the source of prescription (CPRS, eRx, CPRS+eRx, Written, or All), and including discontinued and/or expired orders and various sort criteria. For example, list by patient, by provider, by drug, and by schedule, etc. It is an 80-column report queued to a printer. |
| PSD DAILY LOG                     | PSDACT    | Daily Activity Log (in lieu of VA FORM 10-2320) The Daily Activity Log lists all transactions for a CS dispensing site (vault). It includes a forwarding balance on each transaction. This document may be generated for a single drug, some drugs, all Schedule II drugs (by typing the ^ALL CII DRUGS group name), or ALL drugs within a specified date range.                                                                                                                                      |
| PSD DAILY LOG TECH Lock: PSD TECH | PSDACT    | Daily Activity Log (in lieu of VA FORM 10-2320) The Daily Activity Log lists all transactions for a CS dispensing site (vault). It includes a forwarding balance on each transaction. This document may be generated for a single drug, some drugs, all Schedule II drugs (by typing the ^ALL CII DRUGS group name), or ALL drugs with a specified date range.                                                                                                                                        |

| Option Name           | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD DEA LIST          | PSDEA     | DEA Special Handling List This report alphabetically lists the drug name, DEA Special Handling, and NDC data for all drugs within the DRUG file (#50) marked for CS package use. This report will be helpful in researching drugs incorrectly marked for CS package use.                                                                                                                                            |
| PSD DEA SUBOXONE      | PSDSUBOX  | DEA DATA - Waived Practitioner Report This report provides a list of patients that were prescribed with Suboxone drugs. Two views are available, one with details, and another with just the counts of Suboxone patients per prescriber.                                                                                                                                                                            |
| PSD DEST DRUGS REPORT | PSDESTP   | Destroyed Drugs Report This report lists, alphabetically by drug; all destroyed controlled substances, within a narcotic dispensing site, for a given period of time. Pharmacy Supervisor certifying the destruction, quantity destroyed, and date destroyed is also included on this report. The report may be generated for a single drug, several drugs, or ALL drugs stocked within a specific dispensing site. |

## &lt;This page is intentionally left blank.&gt;

| Option Name                    | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD DEST NON-CS DRUG           | PSDESTO   | Hold a CS Drug (No Inventory Update) This option allows Pharmacy Supervisors to place a CS VA drug, from the DRUG file (#50), on hold for destruction. When using this option, the CS inventory balance will not be updated. A CS DESTRUCTION file (#58.86) entry is made and can be tracked through the CS software.                                                      |
| PSD DEST TEXT DRUG             | PSDESTF   | Non-VA Drug Placed on Hold for Destruction This option allows the Pharmacy Supervisors to place a non-VA drug, not existing in the DRUG file (#50), on hold for destruction. A CS DESTRUCTION file (#58.86) entry is made and can be tracked through the CS software.                                                                                                      |
| PSD DESTROY DEA41              | PSDEA41   | DEA Form 41 Destroyed Drugs Report This report lists information on destroyed CS that is required in completing the DEA Form 41.                                                                                                                                                                                                                                           |
| PSD DESTROY DRUGS Lock: PSDMGR | PSDEST    | Destroy a Controlled Substances Drug This option provides the supervisor ability to enter the destruction information for any CS drug being destroyed.                                                                                                                                                                                                                     |
| PSD DESTROY MENU               |           | Destructions Menu This menu allows Pharmacy Supervisors to maintain the necessary records when destroying a CS drug. Menu Items: PSD DESTROY DRUGS Destroy a Controlled Substances Drug PSD DEST NON-CS DRUG Hold a CS Drug (No Inventory Update) PSD DEST TEXT DRUG Non-VA Drug Placed on Hold for Destruction Destructions Holding Report                                |
| PSD DESTRUCTION HOLDING        | PSDHRPT   | This report lists all CS drugs being held for destruction.                                                                                                                                                                                                                                                                                                                 |
| PSD DIGITALLY SIGNED ORDERS    | PSDDSOR   | OP CS Orders Report Only functional when DEA regulations are revised and PKI functionality can be fully implemented nationally. Sites opting to activate PKI functionality for pharmacy can use this option to retrieve and list all digitally signed orders for controlled substances. The source of prescription (CPRS, eRx, CPRS+eRx, Written, or All) may be selected. |

| Option Name                 | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD DIG. SIGNED RELEASED RX | PSDDSOR2  | OP Released Rx Report Only functional when DEA regulations are revised and PKI functionality can be fully implemented nationally. Sites opting to activate PKI functionality for pharmacy can use this option to retrieve and list all released digitally signed orders for controlled substances. The source of prescription (CPRS, eRx, CPRS+eRx, Written, or All) may be selected.                                                                                                                                                                                                  |
| PSD DISPENSE TO NDES        | PSDNDES   | Narcotic Dispensing Equipment Orders This option is for dispensing from Pharmacy to narcotic dispensing equipment systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PSD DISPENSE W/O GS         | PSDDFP    | Pharmacy Dispense without (VA FORM 10-2638) This option provides pharmacy the ability to dispense CS drugs from a dispensing site without generating the VA FORM 10-2638. Drugs dispensed using this option will not be displayed on the Inspector's Log for controlled substances for the NAOUs. These drugs will be included on the Pharmacy Dispensing Report and the Daily Activity Log.                                                                                                                                                                                           |
| PSD DISPENSING MENU         |           | Dispensing Menu This menu contains access to all options associated with the dispensing of controlled substances. Menu Items: PSD WORKSHEET PRINT Print CS Dispensing Worksheet PSD WORKSHEET DISPENSING Fill/Dispense CS Orders from Worksheet PSD PRINT 2321 Dispensing/Receiving Report (VA FORM 10- 2321) PSD PRINT 2638 Green Sheet - Print (VA FORM 10-2638) PSD DISPENSE W/O GS Pharmacy Dispense without (VA FORM 10-2638) PSD REPRINTMENU Reprint Reports Menu PSD LABEL DRUG/NUMBER Label for Dispensing (Barcode) PSD DISPENSE TO NDES Narcotic Dispensing Equipment Orders |

| Option Name              | Routine     | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD DRUG CHECK           | PSDMAPU     | Check Stocked Drugs for CS Use This option queues a background job to check all ACTIVE drugs stocked, within an ACTIVE NAOU, for use with the CS package. If a stocked drug has been unmarked for CS use the drug will then be inactivated. At job completion a MailMan message will be sent listing any drug discrepancies.                                                                                       |
| PSD DRUG FILE DATA       | PSDCSL      | Drug File Stats for CS Drugs This report lists the drug name, order unit, price per order unit, dispense unit, dispense units per order unit, and price per dispense unit. These statistics are compiled from the DRUG file (#50) and may be used when loading stock drugs into a NAOU. All drugs marked for CS package use will print on this report.                                                             |
| PSD DRUG LOC EDIT        | PSDCODE     | Enter/Edit CS Drug Location Codes This option allows editing of the codes used to define the locations of stocked drugs in NAOU or in the pharmacy.                                                                                                                                                                                                                                                                |
| PSD DRUG LOC PRINT       | CODE^PSDPRT | List CS Drug Location Codes This report will list the codes used to define the location of drugs stocked in NAOUor in the pharmacy.                                                                                                                                                                                                                                                                                |
| PSD DRUG RECEIPT HISTORY | PSDREVD     | Drug Receipt History This option is used to review all receipts processed over a selected time range for a selected drug.                                                                                                                                                                                                                                                                                          |
| PSD EDIT/CANC VER ORD    | PSDEVO      | Edit/Cancel Verified Orders This option allows the Pharmacy Supervisor access to edit or cancel a verified order. The order must be edited or cancelled prior to being delivered to the NAOU. A verified order may be edited only once. It must be cancelled and re- entered if a second edit is required. Quantity, manufacturer, lot number, and expiration date are the only fields in which edits can be made. |

| Option Name                | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|----------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD EDIT/CANC VER ORD RPT  | PSDEVOR   | Edited Verified Orders Report This report lists all verified orders that have been edited or cancelled within a specified date range. Data listed includes pharmacy dispensing # (Green Sheet #), date edited, drug, type of action (edited or cancelled), original quantity, new quantity, and name of the pharmacist. The manufacturer, lot #, or expiration date fields will also be listed if edited.                                                                                                                                                                                          |
| PSD EMERGENCY ORDER REPORT | PSDEM     | Unscheduled Order Report A report to show by drug or by NAOU a list of unscheduled orders.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| PSD ENTER/EDIT MENU        |           | Enter/Edit Menu This menu contains the enter/edit options associated with setting up the files for the CS module. Menu Items: PSD INVEN TYPE EDIT Inventory Types - Enter/Edit PSD DRUG LOC EDIT Enter/Edit CS Drug Location Codes PSD NAOU EDIT Create/Edit the Narcotic Area of Use PSD STOCK DRUG EDIT Stock CS Drugs - Enter/Edit PSD MFG/LOT/EXP DATE EDIT Manufacturer, Lot #, and Exp. Date - Enter/Edit PSD NARC EDIT Narcotic Breakdown Unit/Package Size - Enter/Edit PSD NAOU INV GROUP EDIT NAOU Inventory Group - Enter/Edit PSD MARK Mark/Unmark Drugs for controlled substances use |

| Option Name                                 | Routine   | Menu Text / Description                                                                                                                                                                                                                                            |
|---------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD ERR/ADJ EDIT Lock: PSD ERROR            | PSDERD    | Enter Error/Adjustment Resolution This option allows designated Pharmacy Supervisors the ability to enter a resolution comment for each error or adjustment created when using the barcode TRAKKER.                                                                |
| PSD ERR/ADJ PENDING REPORT Lock: PSD ERROR  | PSDERP    | List Pending Errors/Adjustments Logged by TRAKKER This option lists all pending errors/adjustments logged from the barcode TRAKKER for a specific Dispensing Site within a given time frame.                                                                       |
| PSD ERR/ADJ RESOLVED REPORT Lock: PSD ERROR | PSDERCP   | Print Resolved Errors/Adjustments Log This report prints a listing of all resolved errors/adjustments logged by the barcode TRAKKER for a specific Dispensing Site within a given time frame.                                                                      |
| PSD EXISTING GS                             | PSDEXGS   | Add Existing Green Sheets at Setup This option provides pharmacy the ability to enter existing Green Sheets and active orders on an NAOU, at package setup. These orders may be tracked through the CS software.                                                   |
| PSD EXP REPORT                              | PSDEXP    | Expiration Date Report This option will print a Controlled Substances Expiration Date Report for a single NAOU, several NAOUs, or ALL NAOUs. This report may be sorted by DATE/DRUG/NAOU or by DATE/NAOU/DRUG.                                                     |
| PSD GS DISCREPANCY REPORT                   | PSDCRP    | Completed Green Sheet Discrepancy Report This report lists all Green Sheets with a completion status of MATH ERROR, GREEN SHEET NOT SIGNED BY NURSE, or OTHER - REFERRED TO SUPERVISOR. This report may be printed for a single NAOU, several NAOUs, or ALL NAOUs. |
| PSD GS HISTORY                              | PSDGSH    | Green Sheet History The Green Sheet history provides pharmacy with a detailed account of every transaction affecting this VAFORM 10-2638. This history may be displayed to the user's screen or directed to a printer.                                             |
| PSD GS LISTING                              | PSDGSL    | Listing of Green Sheet Log This option numerically lists all Green Sheets for a given date range or for a given Green Sheet number range. The logs list Green Sheet number, date dispensed, and current status.                                                    |

| Option Name                    | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD GS TRANS NOT RECD (NAOU)   | PSDNBT    | Transferred Green Sheets - Pending NAOU Receipt This report lists all Green Sheets that have been transferred from an NAOU and are pending receipt in another NAOU.                                                                                                                                                                                                                              |
| PSD GS TRANSFER (NAOU) REPORT  | PSDNTR    | Green Sheet Transfer Between NAOUs Report This report lists all Green Sheets transferred and received between NAOUs for a given date range. This report may be printed for a single NAOU, several NAOUs, or ALL NAOUs.                                                                                                                                                                           |
| PSD INACTIVATE NAOU            | PSDNACT   | Inactivate NAOU This option will allow a user to inactivate an NAOU. An inactivation date may be entered for a future time.                                                                                                                                                                                                                                                                      |
| PSD INACTIVATE NAOU STOCK DRUG | PSDNSTK   | Inactivate NAOU Stock Drug This option is used to inactivate a drug that is currently on a NAOU stock list. Drugs should not                                                                                                                                                                                                                                                                     |
| PSD INFUSION MENU              |           | be deleted, but simply inactivated. Infusion Order Processing Menu This menu contains the infusion order/entry and transferring a Green Sheet options associated with the IV pharmacist processing a CS infusion order. Menu Items: PSD INFUSION O/E Infusion Order Entry PSD NURSE TRANSFER GS Transfer Green Sheet and Drug to another NAOU Transfer GS for PCA/Infusion Signed Out to Patient |
| PSD INFUSION O/E               | PSDORV    | Infusion Order Entry The IV pharmacist uses this option to electronically request CS drugs used in IV orders. Only infusion orders requiring the VA FORM 10- 2638 should be requested using this option.                                                                                                                                                                                         |
| PSD INSP LOG BY RECD DATE      | PSDRLOG   | Inspector's Log by Rec'd Date This report lists all dispensing transactions for Narcotic Area of Use received within a given date range. The data includes dispensing number, drug name, date received, quantity received, expiration date (if available), blanks for quantity on hand, and a signature blank for verification.                                                                  |
| PSD INSP PLACE HOLD            | PSDCSI    | Place Green Sheet on Hold This option allows the CS Inspector to place a Green Sheet on hold for review.                                                                                                                                                                                                                                                                                         |

| Option Name                                                                | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD INSP REMOVE HOLD                                                       | PSDRSI    | Remove Green Sheet from Hold This option allows the CS Inspector to remove a                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PSD INSPECTOR MENU Action: I '$D(PSDSITE) D ^PSDSET Exit Action: K PSDSITE |           | Green Sheet from hold. Controlled Substances Inspector Menu This menu contains all options associated with a CS inspection. Menu Items: PSD INSP PLACE HOLD Place Green Sheet on Hold PSD INSP REMOVE HOLD Remove Green Sheet from Hold PSD PRINT INSPECTOR LOG Inspector's Log for Controlled Substances PSD PRT GS INSP HOLD Under Inspector's Review - Green Sheets PSD INVEN SHEET PRT Inventory Sheet Print PSD INSP LOG BY RECD DATE Inspector's Log by Rec'd Date PSD IRL INSP MENU Barcode TRAKKER for CS Inspections PSD GS HISTORY Green Sheet History PSD NAOU BALANCE REPORT |
| PSD INVEN SHEET PRT                                                        | PSDBALI   | Narcotic Count - Shift Report Inventory Sheet Print This option prints an Inspector's Sheet, which is used to inventory on-hand amounts within a pharmacy-dispensing site (vault). This form lists current on-hand amounts and provides a blank space for the inspector to list actual on-hand counts. A signature line is included on each page. This sheet may be generated for one drug, some drugs, or ALL drugs. The drugs are listed alphabetically.                                                                                                                               |

| Option Name           | Routine       | Menu Text / Description                                                                                                                                                                                                                                                                                      |
|-----------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD INVEN TYPE EDIT   | PSDNVT        | Inventory Types - Enter/Edit This option will edit the entries in the AOU INVENTORY TYPE file (#58.16) used to classify NAOU drugs.                                                                                                                                                                          |
| PSD INVEN TYPE PRINT  | INVEN^PSDPRT  | Print Inventory Types Use this option to print the entries in the AOU INVENTORY TYPE file (#58.16) used to classify NAOU stocked drugs.                                                                                                                                                                      |
| PSD IRL INSP DATA     | UPLOAD^PSDUP3 | Send Inspections Inventory TRAKKER Data to DHCP This option contains the access to upload or send narcotic vault inspections inventory from the barcode TRAKKER to V IST A .                                                                                                                                 |
| PSD IRL INSP MENU     |               | Barcode TRAKKER for CS Inspections This menu contains the options associated with performing narcotic vault inspections using the barcode TRAKKER device. Menu Items: PSD IRL INSPECTOR INV Load Software and Insp. Inventory into TRAKKER PSD IRL INSP DATA Send Inspections Inventory TRAKKER Data to DHCP |
| PSD IRL INSPECTOR INV | PSDUP3        | Load Software and Insp. Inventory into TRAKKER This option contains the access to download an IRL program to the TRAKKER and download the narcotic inspections inventory to the TRAKKER. This option is used for the Narcotic Inspectors only.                                                               |
| PSD IRL INV DATA      | UPLOAD^PSDUP2 | Send Vault TRAKKER Inventory Data to DHCP This option contains the access to upload or send vault inventory from the barcode TRAKKER to V IST A .                                                                                                                                                            |

| Option Name                  | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                |
|------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD IRL INV MENU             |           | Barcode TRAKKER for Inventory This menu contains the options associated with performing narcotic vault inventories using the barcode TRAKKER device. Menu Items: PSD IRL VAULT INV Load Software and Inventory into TRAKKER PSD IRL INV DATA Send Vault TRAKKER Inventory Data to DHCP |
| PSD IRL VAULT INV            | PSDUP2    | Load Software and Inventory into TRAKKER This option contains the access to download an IRL program to the TRAKKER and download the vault inventory to the TRAKKER, in one step. This option is used for pharmacy service only.                                                        |
| PSD LABEL DRUG/NUMBER        | PSDLBL    | Label for Dispensing (Barcode) This option allows pharmacy to print the dispensing number/drug barcode label that is attached to the drug delivered to the NAOUs.                                                                                                                      |
| PSD LABEL INSP               | PSDLBLI   | Inspectors Label Print This option allows the inspector or Pharmacy Supervisor to print the CS Inspector's barcode labels.                                                                                                                                                             |
| PSD LABEL PHARM Lock: PSDMGR | PSDLBL3   | Print Pharmacist ID Labels This option allows Pharmacy Supervisors to print the pharmacists barcoded ID label. This label is scanned when pharmacists inventory CS drugs in the dispensing vault.                                                                                      |
| PSD LABEL VAULT              | PSDLBL1   | Barcode Drug Labels for Vault This option allows pharmacy to print the barcode labels for dispensing-site (vault) stocked drugs.                                                                                                                                                       |
| PSD MARK                     | PSDAPU    | Mark/Unmark Drugs for Controlled Substances Use This option provides the ability to mark/unmark entries in the DRUG file (#50) for use with the CS package.                                                                                                                            |

| Option Name                                                      | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD MENU Action: I '$D(PSDSITE) D ^PSDSET Exit Action: K PSDSITE |           | Controlled Substances Menu This menu contains access to all options associated with the CS module of the Pharmacy software. Menu Items: PSD MGR Supervisor (CS) Menu PSD TRANSACTION MENU Pharmacist Menu PSD PRODUCTION REPORTS Production Reports PSD PHARM TECH Technician (CS Pharmacy) Menu PSD LABEL VAULT                                                                                                                                                                                   |
| PSD MFG REPORT PRINT                                             | PSDPMFG   | Manufacturer and Narcotic Information Report This report prints an alphabetical listing of all ACTIVE drugs within an ACTIVE NAOU that have been defined in the DRUG ACCOUNTABILITY STATS file (#58.8). This report lists NAOU, drug name, manufacturer, lot #, expiration date, narcotic breakdown unit, and narcotic package size. This report may be sorted alphabetically by NAOU, then drug name or drug name, then NAOU. The user may select one NAOU, several NAOUs, or all NAOUs to print. |
| PSD MFG/LOT/EXP DATE EDIT                                        | PSDMFG    | Manufacturer, Lot #, and Exp. Date - Enter/Edit This option allows the user to enter or edit manufacturer, lot #, and expiration dates for stocked drugs in an NAOU.                                                                                                                                                                                                                                                                                                                               |

| Option Name          | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|----------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD MGR Lock: PSDMGR |           | Supervisor (CS) Menu This menu contains the options used for the NAOU set-up and maintenance. Menu Items: PSD SETUP Set Up CS (Build Files) Menu PSD MGR REPORTS Management Reports PSD BALANCE ADJUSTMENTS Balance Adjustments PSD CORRECTION LOG Correction Menu PSD EXISTING GS Add Existing Green Sheets at Setup PSD LABEL PHARM Print Pharmacist ID Labels PSD DESTROY MENU Destructions Menu PSD LABEL INSP Inspectors Label Print PSD EMERGENCY ORDER REPORT Unscheduled Order Report |

| PSD MGR REPORTS   | Management Reports This option contains all reports or lists associated with drug accountability for narcotics. Menu Items: PSD NOT DELIVERED Orders Filled Not Delivered PSD PEND VAULT ORDERS Pending CS Orders by Dispensing Site PSD DESTRUCTION HOLDING Destructions Holding Report PSD EDIT/CANC VER ORD RPT Edited Verified Orders Report PSD GS TRANSFER (NAOU) REPORT Green Sheet Transfer Between NAOUs Report PSD GS TRANS NOT RECD (NAOU) Transferred Green Sheets - Pending NAOU Receipt PSD GS DISCREPANCY REPORT Completed Green Sheet Discrepancy Report PSD CORRECTION LOG REPORT Correction Log Report PSD NAOU USAGE NAOU Usage Report PSD DESTROY DEA41 DEA Form 41 Destroyed Drugs Report PSD DEST DRUGS REPORT Destroyed Drugs Report PSD AMIS AMIS Report PSD GS LISTING Listing of Green Sheet Log PSD COST REPORTS Cost Reports   |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Option Name                   | Routine     | Menu Text / Description                                                                                                                                                                                                                                                                                                                 |
|-------------------------------|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                               |             | PSD PRT GS INSP HOLD Under Inspector's Review - Green Sheets PSD BALANCE ADJUSTMENT REVIEW Balance Adjustment Report                                                                                                                                                                                                                    |
| PSD NAOU ADJ                  | PSDADJN     | Balance Adjustments - NAOU This option may be used to adjust the balance of controlled substances.                                                                                                                                                                                                                                      |
| PSD NAOU BAL INITIAL          | PSDADJIN    | Initialize NAOU Drug Balance This option may be used to establish beginning balances for drugs.                                                                                                                                                                                                                                         |
| PSD NAOU BALANCE REPORT       | PSDBAN      | Narcotic Count - Shift Report This report will show the balance for one or all drugs on a ward.                                                                                                                                                                                                                                         |
| PSD NAOU EDIT Lock: PSD PARAM | PSDEN       | Create/Edit the Narcotic Area of Use This option allows the user to initially define the NAOU.                                                                                                                                                                                                                                          |
| PSD NAOU INV GROUP EDIT       | PSDGEN      | NAOU Inventory Group - Enter/Edit This option allows the user to enter and edit inventory groups. These groups define a cluster of NAOUs. For each of these NAOUs, one or more inventory types may be defined. This lets pharmacy detail a list of standard NAOUs and inventory types that can be easily selected when doing inventory. |
| PSD NAOU INV GROUP PRINT      | PSDGPR      | Inventory Group List (80 column) This option prints a list of the currently defined NAOU inventory groups with their associated inventory types.                                                                                                                                                                                        |
| PSD NAOU INV GROUP SORT       | PSDGSK      | Sort NAOUs in Inventory Group This option allows the user to change the order in which the NAOUs will sort within an inventory group. NAOUs should sort in the order that they will be visited.                                                                                                                                         |
| PSD NAOU PRINT                | NAOU^PSDPRT | Show Narcotic Area of Use This option allows the user to print the NAOUs/Location Type/Primary Dispensing Site created in the Create/Edit the Narcotic Area of Use option.                                                                                                                                                              |

| Option Name    | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                      |
|----------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD NAOU USAGE | PSDNU     | NAOU Usage Report This report will print an NAOU drug usage report for a selected date range. The report may be sorted by drug (one, some, or ALL) or by NAOU (one, some, or ALL). A detailed list of orders, including the pharmacy dispensing # (Green Sheet #), date filled, quantity, and who ordered the drug will be printed. Summary totals by order and quantity are also generated. |
| PSD NARC EDIT  | PSDNARC   | Narcotic Breakdown Unit/Package Size - Enter/Edit This option allows the user to enter or edit narcotic breakdown unit and narcotic package size for stocked drugs in an active NAOU.                                                                                                                                                                                                        |
| PSD NMCS ADJ   | PSDNMBA   | CS Balance Adjustments Report This option lists Drug Accountability Transactions in which the CS vault inventory balance was adjusted manually during the date range entered. The adjuster and reason will display on the report for the Narcotic Inspectors and Pharmacy Managers to review regularly for appropriateness and authorization.                                                |

| Option Name     | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|-----------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSDNMMENU       |           | CS Monitoring Menu This standalone menu contains CS Monitoring reports to help facilitate the monitoring of CS and Schedule II narcotics. The menu should be assigned to the appropriate Narcotic Inspectors and Pharmacy Managers at the site. IA 3882 - Gives permission for Kernel's Option Access by User [XUOPTWHO] option to be included on this menu. Menu Items: PSD NMSECURITY KEY CS Application Security Key Report PSD NMCS ADJ CS Balance Adjustments Report PSD NMRXSAMEPERSON CS RXs by Same Person Report PSD NMRXREPRINT Label Reprint for CS RXs Report XUOPTWHO Option Access By User PSD NMRXPARTIAL Partial Request for CS RXs Report PSD NMRXWITHOUT VA |
| PSDNMRX PARTIAL | PSDNMPR   | Patients Without VA Visit Report Partial Request for CS RXs Report This option lists CS prescriptions for which a prescription partial fill was requested. An individual could partially fill the same prescription more than once and be diverting prescription drugs. Narcotic Inspectors and Pharmacy managers should monitor this activity. This report should be queued to run during non- peak hours.                                                                                                                                                                                                                                                                   |

| Option Name        | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSDNMRX REPRINT    | PSDNMRP   | Label Reprint for CS RXs Report This option lists CS prescriptions for which a prescription label reprint was requested. An individual could fill the same prescription more than once and be diverting prescription drugs. Narcotic Inspectors and Pharmacy managers should monitor this activity. This report should be queued to run during non-peak hours.                                                                                                                                                                                                                      |
| PSDNMRXSAME PERSON | PSDNMSP   | CS RXs by Same Person Report This option lists CS prescriptions that were entered, finished and released by the same person for the date range entered. Different pharmacists in the prescription filling process normally perform these functions. Although frequently necessary on off-shifts and weekends, CS Inspectors and Pharmacy Managers should monitor this activity. This report should be queued to run during non-peak hours.                                                                                                                                          |
| PSDNMRX WITHOUT VA | PSDNMWE   | Patients Without VA Visit Report This option lists patients that receive prescriptions but have not had a VA clinic visit within one year of a RX release date for the date range entered. Excluding RXs released on the same day as a discharge and within a user defined discharge date range. Patients in Fee Basis and Aid and Attendance programs may be included on the list and should be reviewed. This lists represents a potential diversion tactic that could be employed to prevent detection and suspicion. This report should be queued to run during non-peak hours. |
| PSDNM SECURITY KEY | PSDNMKY   | CS Application Security Key Report This option lists holders of the PSJ RPHARM and/or PSDMGR security keys. Holders of these keys have the ability to override discrepancies, make CS vault inventory adjustments and transfer medications between vaults. The list requires routine monitoring and validation for accuracy.                                                                                                                                                                                                                                                        |
| PSD NOT DELIVERED  | PSDFND    | Orders Filled Not Delivered This option generates a list of all CS orders filled from the pharmacy-dispensing site (vault) but not yet delivered to the NAOUs. A summary total sorted by drug is also generated.                                                                                                                                                                                                                                                                                                                                                                    |

| Option Name                                                     | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD NOT DELIVERED NURSE Lock: PSJ RNURSE                        | PSDFND    | Orders Filled Not Delivered This option generates a list of all CS orders filled from the pharmacy-dispensing site (vault) but not yet delivered to the NAOUs. A summary total sorted by drug is also generated.                                                                                                                                                     |
| PSD NURSE DEFECTIVE DOSE                                        | PSDRF4    | Record Defective Dose When a nurse discovers a damaged drug that cannot be dispensed to a patient, this option may be used to record the wasting.                                                                                                                                                                                                                    |
| PSD NURSE DELAYED DISPENSE                                      | PSDRFS    | Delayed Sign Out Dose for Patient This option may be used when there is computer down time and it is necessary to sign out doses that were already given to patients.                                                                                                                                                                                                |
| PSD NURSE DISP MENU Action: D ^PSDRFD Exit Action: K NAOU,NAOUN |           | Sign Out Menu This is a menu to assist nurses in tracking doses signed out for patients. Menu Items: PSD NURSE DISPENSING Sign Out Dose for Patient PSD PAT ID LIST Patient ID List Print PSD NURSE DISP REPORT Activity Report PSD NURSE WASTE Record Delayed Wastage PSD NURSE NOT GIVEN Not Given, Return to Stock PSD NURSE DEFECTIVE DOSE Record Defective Dose |
| PSD NURSE DISP REPORT                                           | PSDPAT    | Activity Report This option provides a detailed and summary listing of activity.                                                                                                                                                                                                                                                                                     |
| PSD NURSE DISPENSING                                            | PSDRF     | Sign Out Dose for Patient This option is designed for signing out doses via a radio frequency device.                                                                                                                                                                                                                                                                |

| Option Name        | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                            |
|--------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD NURSE GS MENU  |           | Green Sheet Menu This menu contains options for handling green sheets. Menu Items: PSD REC GS Receipt of Controlled Substance from Pharmacy PSD READY GS FOR PICKUP Complete a Green Sheet - Ready for Pickup PSD GS HISTORY Green Sheet History PSD NURSE TRANS GS MENU Transfer Green Sheet Menu |
| PSD NURSE HELP     | PSDHELP   | Help Online Use this option to view or print online help.                                                                                                                                                                                                                                          |
| PSD NURSE INFUSION | PSDORNV   | Infusion or PCA Syringe Order Entry For Patient This option is for ordering an infusion or PCA syringe for a specific patient.                                                                                                                                                                     |

| Option Name                                                            | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD NURSE MENU Action: I '$D(PSDSITE) D ^PSDSET Exit Action: K PSDSITE |           | Controlled Substances Nurses' (CS) Menu This menu provides nurses access to all options associated with requesting and receiving CS drugs from pharmacy. Menu Items: PSD NURSE SHIFT LOG Ward (NAOU) Drug History PSD NURSE HELP Help Online PSD NURSE DISP MENU Sign Out Menu PSD NURSE ORDER MENU Ordering Menu PSD NURSE GS MENU Green Sheet Menu PSD NAOU BALANCE REPORT Narcotic Count - Shift Report PSD REC GS Receipt of Controlled Substance from Pharmacy PSD NURSE ONLINE COUNT |
| PSD NURSE NOT GIVEN                                                    | PSDRFR    | Not Given, Return to Stock This option may be used when a dose is not given to a patient and must be returned to stock. This option must be used within one hour of the last dispensed dose (by the nurse that dispensed that dose).                                                                                                                                                                                                                                                       |
| PSD NURSE ONLINE COUNT                                                 | PSDADJC   | Verify Count This option may be used to verify and correct balances.                                                                                                                                                                                                                                                                                                                                                                                                                       |

| Option Name                    | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD NURSE ORDER MENU           |           | Ordering Menu This menu contains options for ordering and checking on orders. Menu Items: PSD ORDER ENTRY CS Order Entry For Ward PSD PEND NAOU ORDERS Pending CS Orders Report for an NAOU PSD NOT DELIVERED NURSE Orders Filled Not Delivered PSD NURSE PRIORITY ORDER CHECK Check on Priority Orders PSD NURSE INFUSION Infusion or PCA Syringe Order Entry For Patient |
| PSD NURSE PRIORITY ORDER CHECK | PSDEM4    | Check on Priority Orders This option will check the status of Priority Orders that Pharmacy has filled today for a selected NAOU.                                                                                                                                                                                                                                          |
| PSD NURSE REC TRANSFER GS      | PSDNTT    | Receive Green Sheet &Drug from another NAOU This option provides nurses the ability to receive CS drugs and their associated Green Sheet from another NAOU. The transferring of CS drugs between NAOUs requires two processing steps. Step 1 - Transfer Green Sheet and Drug to another NAOU Step 2 - From an NAOU - Receive Green Sheet Transfer &Drug                    |
| PSD GS REC PCA/INF FOR PATIENT | PSDNTTPC  | Receive GS for PCA/Infusion Signed Out to Patient This option provides nurses the ability to receive Green Sheets for PCA/Infusions from another NAOU. The transferring of these Green Sheets between NAOUs requires two processing steps. Step 1 - Transfer GS for PCA/Infusion Signed Out to Patient Step 2 - Receive GS for PCA/Infusion Signed Out to Patient          |

| Option Name            | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD NURSE REPRINT 2321 | PSDRPT    | Reprint Transfer Between NAOUs (VA FORM 10- 2321) Nurses may reprint the transfer between NAOUs form (in lieu of VA FORM 10-2321) for any Green Sheet and drug transferred from their NAOU. The form may be reprinted only if the transferred Green Sheet and drug has not been received into the NAOU receiving the transfer.                                                                                                            |
| PSD NURSE SHIFT LOG    | PSDNSCL   | Ward (NAOU) Drug History Use this report to list all ACTIVE CS orders currently on a specific NAOU.                                                                                                                                                                                                                                                                                                                                       |
| PSD NURSE SUPR MENU    |           | Nursing Supervisor Menu This is a menu with special options to support the signing out of CS. Menu Items: PSD NAOU BAL INITIAL Initialize NAOU Drug Balance PSD NAOU ADJ Balance Adjustments - NAOU PSD PAT INQUIRY Patient/Location Inquiry PSD EMERGENCY ORDER REPORT Unscheduled Order Report PSD EXP REPORT Expiration Date Report PSD PAT ID LIST Patient ID List Print PSD NURSE DELAYED DISPENSE Delayed Sign Out Dose for Patient |

| Option Name                  | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD NURSE TRANS GS MENU      |           | Transfer Green Sheet Menu Use this menu to transfer and receive Green Sheets between NAOUs. Menu Items: PSD NURSE TRANSFER GS Transfer Green Sheet and Drug to another NAOU PSD NURSE REC TRANSFER GS Receive Green Sheet &Drug from another NAOU PSD GS TRANS PCA/INF PATIENT Transfer GS for PCA/Infusion Signed Out to Patient PSD GS REC PCA/INF FOR PATIENT Receive GS for PCA/Infusion Signed Out to Patient PSD NURSE REPRINT 2321 Reprint Transfer Between NAOUs (VA FORM 10- 2321) PSD GS TRANS NOT RECD (NAOU) Transferred Green Sheets - Pending NAOU Receipt |
| PSD NURSE TRANSFER GS        | PSDNTF    | Transfer Green Sheet and Drug to another NAOU This option provides nurses the ability to transfer CS drugs and their associated Green Sheet to another NAOU. The transferring of CS drugs between NAOUs requires two processing steps. Step 1 - Transfer Green Sheet and Drug to another NAOU Step 2 - From an NAOU - Receive Green Sheet Transfer &Drug                                                                                                                                                                                                                 |
| PSD GS TRANS PCA/INF PATIENT | PSDNTFPC  | Transfer GS for PCA/Infusion Signed Out to Patient This option provides nurses the ability to transfer Green Sheets for PCA/Infusions to another NAOU. The transferring of these Green Sheets between NAOUs requires two processing steps. Step 1 - Transfer GS for PCA/Infusion Signed Out to Patient Step 2 - Receive GS for PCA/Infusion Signed Out to Patient                                                                                                                                                                                                        |

| Option Name                     | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD NURSE WASTE                 | PSDRFW    | Record Delayed Wastage This option can be used when a dispensed dose needs to be wasted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PSD ON-HAND                     | PSDBAL    | List On-Hand Amounts This option lists current on-hand amounts for drugs stocked in a pharmacy-dispensing site (vault). The report is selectable by one drug, some drugs, or ALL drugs. The drugs are listed alphabetically to the user's screen or a selected printer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PSD ON-HAND TECH Lock: PSD TECH | PSDBAL    | List On-Hand Amounts This option lists current on-hand amounts for drugs stocked in a pharmacy-dispensing site (vault). The report is selectable by one drug, some drugs, or ALL drugs. The drugs are listed alphabetically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PSD ORDER ENTRY                 | PSDORN    | CS Order Entry For Ward Use this option to electronically request CS drugs from pharmacy requiring the VA FORM 10-2638.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PSD OUTPATIENT                  | PSDOPT    | Outpatient Rx's This option provides pharmacy the ability to log outpatient prescriptions from their CS dispensing vault. The pharmacist will select an outpatient prescription and the software will display the most recently filled Rx. It will display new, refill, and partial prescriptions. The option includes a failsafe requiring users to enter the correct on- hand narcotic medication count. If the user's entry does not match the count in VistA after three attempts, personnel in the CS BALANCE DISCREPANCY mail group are notified to investigate further. This failsafe can be switched on or off for each dispensing site using the BALANCE DISCREPANCY CHECK field (#37) in the DRUG ACCOUNTABILITY STATS file (#58.8), since it may not be practical for automated dispensing sites that cannot perform an on-hand medication count while dispensing drugs. |
| PSD PAT ID LIST                 | PSDLBLP   | Patient ID List Print This option supports the printing of barcode labels for patient ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PSD PAT INQUIRY                 | PSDPATI   | Patient/Location Inquiry This option may be used to verify the location of a patient.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

| Option Name           | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-----------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD PEND NAOU ORDERS  | PSDORSN   | Pending CS Orders Report for an NAOU Use this option to list all pending CS orders. This report may be generated for a single drug or ALL drugs within the NAOU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PSD PEND VAULT ORDERS | PSDORST   | Pending CS Orders by Dispensing Site Pharmacy uses this option to list all pending CS orders for a specific dispensing site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PSD PHARM TECH        |           | Technician (CS Pharmacy) Menu This menu provides the Pharmacy Technicians access to options associated with requesting, receiving, and processing CS orders handled by pharmacy and nursing. This menu is a combination of CS options used by both pharmacy technicians and RPhs. Note: Some menu items are accessed by certain keys. Menu Items: PSD WORKSHEET PRINT Print CS Dispensing Worksheet PSD WORKSHEET DISPENSING Fill/Dispense CS Orders from Worksheet PSD PRINT GS PICKUP Green Sheet Ready for Pickup Log PSD PICKUP GS Pick Up Green Sheet PSD ORDER ENTRY CS Order Entry For Ward PSD REC GS Receipt of Controlled Substance from Pharmacy PSD COMPLETE GS Complete Green Sheet PSD GS HISTORY Green Sheet History PSD ON-HAND TECH List On-Hand Amounts PSD DAILY LOG TECH Daily Activity Log (in lieu of VA FORM 10-2320) PSD PRINT VAULT TRANSFERS TECH Transfer Drugs between Dispensing Sites Report PSD RECEIPTS MENU Receipts Into Pharmacy menu. |

| Option Name   | Routine   | Menu Text / Description                                                                                                                         |
|---------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------|
|               |           | PSD DISPENSINGMENU Dispensing Menu PSD DESTROY MENU Destructions Menu PSD MFG/LOT/EXP DATE EDIT Manufacturer, Lot #, and Exp. Date - Enter/Edit |

| Complete Green Sheet [PSD COMPLETE GS] Destroyed Drugs Report [PSD DEST DRUGS REPORT] DEA Form 41 Destroyed Drugs Report [PSD DESTROY DEA41] Destructions Holding Report [PSD DESTRUCTION HOLDING] Add Existing Green Sheets at Setup [PSD EXISTING GS] Green Sheet Transfer Between NAOUs Report [PSD GS TRANSFER (NAOU) REPORT] Transfer Drugs between Dispensing Sites [PSD TRANSFER VAULT DRUGS] Receipts Into Pharmacy [PSD RECEIPTS MENU] menu. PSD RECEIVING Receiving PSD PURCHASE ORDER REVIEW Purchase Order Review PSD CP TRANSACTION REVIEW Control Point Transaction Review PSD DRUG RECEIPT HISTORY Drug Receipt History PSD PV INVOICE REVIEW Invoice Review (Prime Vendor) Dispensing Menu [PSD DISPENSING MENU] PSD WORKSHEET PRINT Print CS Dispensing Worksheet PSD WORKSHEET DISPENSING Fill/Dispense CS Orders from Worksheet PSD PRINT 2321 Dispensing/Receiving Report (VA FORM 10- 2321) PSD PRINT 2638 Green Sheet - Print (VA FORM 10-2638) Reprint Reports Menu [PSD REPRINT MENU] PSD REPRINT 2321 Reprint Disp/Receiving Report (VA FORM 10- 2321)   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<!-- image -->

| Option Name   | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|               |           | PSD REPRINT 2638 Green Sheet Reprint (VA FORM 10-2638) PSD REPRINT WORKSHEET Dispensing Worksheet Reprint PSD REPRINT LABEL Label Reprint for Dispensing Drug PSD NURSE REPRINT 2321 Reprint Transfer Between NAOUs (VA FORM 10- 2321 PSD DISPENSE W/O GS Pharmacy Dispense without (VA FORM 10-2638) PSD LABEL DRUG/NUMBER Label for Dispensing (Barcode) PSD DISPENSE TO NDES Narcotic Dispensing Equipment Orders Destructions Menu [PSD DESTROY MENU] PSD DEST NON-CS DRUG Hold a CS Drug (No Inventory Update) PSD DEST TEXT DRUG Non-VA Drug Placed on Hold for Destruction PSD MFG/LOT/EXP DATE EDIT Manufacturer, Lot #, and Exp. Date - Enter/Edit PSD OUTPATIENT Outpatient Rx's Note: The CS technician may perform all the Outpatient Rx's menu functions except releasing a prescription. |

| Option Name             | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                 |
|-------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD PICKUP GS           | PSDGSPU   | Pick Up Green Sheet This option provides pharmacy the ability to receive a Green Sheet into pharmacy that has been marked as Ready for Pickup by Nursing.                                                                                                                                                                               |
| PSD PRINT 2321          | PSDPDR    | Dispensing/Receiving Report (VA FORM 10- 2321) This report lists all CS orders dispensed to a NAOU. This report requires the Dispensing Pharmacist signature and the signature of the nurse receiving the CS drugs. This report will be retained within pharmacy after the controlled substances are delivered to the ward.             |
| PSD PRINT 2638          | PSDPGS    | Green Sheet - Print (VA FORM 10-2638) Pharmacy prints Green Sheets using this option. All Green Sheets, not previously printed for a specific NAOU, will be generated. A single Green Sheet print may also be selected.                                                                                                                 |
| PSD PRINT GS PICKUP     | PSDPUGS   | Green Sheet Ready for Pickup Log This report lists all Green Sheets ready on the wards to be picked up by pharmacy. This report requires a signature of the pharmacy employee picking up the Green Sheet and a signature of the nurse releasing the Green Sheet. This document will be retained on the ward for nurse's records.        |
| PSD PRINT INSPECTOR LOG | PSDPLOG   | Inspector's Log for Controlled Substances This report lists all active Green Sheets by NAOU. The data includes Green Sheet number, drug name, date dispensed, quantity dispensed, expiration date (if available), blanks for quantity on hand, and a signature blank for verification.                                                  |
| PSD PRINT PHARM DISP    | PSDPND    | Pharmacy Dispensing Report This report lists by dispensing site and date range the drug name, pharmacy dispensing number (Green Sheet #), quantity dispensed, date dispensed, and dispensing pharmacist. Also there's a summary by drug of total number dispensed. The summary may be generated without the individual dispensing data. |

| Option Name               | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD PRINT SETUP LISTS     |           | Print CS Set Up Lists This option contains all reports or lists associated with setting up the files for the CS module. Menu Items: PSD DRUG LOC PRINT List CS Drug Location Codes PSD INVEN TYPE PRINT Print Inventory Types PSD NAOU PRINT Show Narcotic Area of Use PSD DRUG FILE DATA Drug File Stats for CS Drugs PSD DEA LIST DEA Special Handling List PSD STOCK PRINT Stock Drug Print (Stock Level and Location) PSD STOCK LIST Stock Drug List (Inventory Type and Location) PSD NAOU INV GROUP PRINT Inventory Group List (80 column) PSD MFG REPORT PRINT Manufacturer and Narcotic Information Report PSD STOCK UNIT LIST |
| PSD PRINT VAULT TRANSFERS | PSDTRVR   | Transfer Drugs between Dispensing Sites Report This report displays all transactions, which transferred CS between dispensing sites, for a given period of time. The transactions list within dispensing site, by drug, the date/time transferred, quantity transferred, and pharmacist transferring the drug.                                                                                                                                                                                                                                                                                                                         |

| Option Name                                   | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                               |
|-----------------------------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD PRINT VAULT TRANSFERS TECH Lock: PSD TECH | PSDTRVR   | Transfer Drugs between Dispensing Sites Report This report displays all transactions, which transferred CS between dispensing sites, for a given period of time. The transactions list within dispensing site, by drug, the date/time transferred, quantity transferred, and pharmacist transferring. |

| PSD PRODUCTION REPORTS   | Production Reports Pharmacy uses the production reports to maintain CS drug accountability and proper inventory controls. Reports generated in lieu of VA FORM 10-2321 and VA FORM 10-2638 may be generated from this menu. Menu Items: PSD PRINT INSPECTOR LOG Inspector's Log for Controlled Substances PSD STOCK PRINT Stock Drug Print (Stock Level and Location) PSD PRINT PHARM DISP Pharmacy Dispensing Report PSD PRINT GS PICKUP Green Sheet Ready for Pickup Log PSD PEND VAULT ORDERS Pending CS Orders by Dispensing Site PSD NOT DELIVERED Orders Filled Not Delivered PSD GS HISTORY Green Sheet History PSD DAILY LOG Daily Activity Log (in lieu of VA FORM 10-2320) PSD INVEN SHEET PRT Inventory Sheet Print PSD ON-HAND List On-Hand Amounts PSD EXP REPORT Expiration Date Report PSD PRINT VAULT TRANSFERS Transfer Drugs between Dispensing Sites Report PSD PRT GS PICKED UP GS Picked Up Awaiting Pharmacy Review PSD INSP LOG BY RECD DATE Inspector's Log by Rec'd Date PSD RX DISPENSING REPORT   |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Option Name               | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                           |           | Rx (Prescription) Outpatient Dispensing Report PSD DIGITALLY SIGNED ORDERS OP CS Orders Report PSD DIG. SIGNED RELEASED RX OP Released Rx Report PSD CS PRESCRIPTIONS REPORT Controlled Substance Prescriptions Report PSD DEA SUBOXONE DEA DATA - Waived Practitioner Report                                                                                                                                                                                                                                     |
| PSD PRT GS INSP HOLD      | PSDPSI    | Under Inspector's Review - Green Sheets This report lists all Green Sheets placed on hold for review by a CS Inspector.                                                                                                                                                                                                                                                                                                                                                                                           |
| PSD PRT GS PICKED UP      | PSDCPO    | GS Picked Up Awaiting Pharmacy Review This report lists all Green Sheets picked up by pharmacy but still awaiting a pharmacy review.                                                                                                                                                                                                                                                                                                                                                                              |
| PSD PURCHASE ORDER REVIEW | PSDREV    | Purchase Order Review Use this option to review all receipt transactions for a selected purchase order.                                                                                                                                                                                                                                                                                                                                                                                                           |
| PSD PURGE                 | PSDPRG    | Purge CS WORKSHEET File This option purges the CS WORKSHEET file (#58.85) nightly. The CS WORKSHEET file (#58.85) is the holding area for CS order requests pending pharmacy processing. The data should remain in the file until orders have been received on an NAOU or cancelled. Once the order is received on an NAOUor cancelled, the data is purged from the file using this background job. This routine should run nightly. The time to queue this option to run should not conflict with system backup. |
| PSD PV INVOICE REVIEW     | PSDREPV   | Invoice Review (Prime Vendor) To list all receipts that has been posted for a selected Prime Vendor invoice number.                                                                                                                                                                                                                                                                                                                                                                                               |
| PSD READY GS FOR PICKUP   | PSDNCGS   | Complete a Green Sheet - Ready for Pickup Use this option to complete a CS Administration Record (VA FORM 10-2638).                                                                                                                                                                                                                                                                                                                                                                                               |
| PSD REC GS                | PSDNRGS   | Receipt of Controlled Substance from Pharmacy Use this option to receive CS orders with a Green Sheet (VA FORM 10-2638).                                                                                                                                                                                                                                                                                                                                                                                          |

| Option Name       | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                         |
|-------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD RECEIPTS MENU |           | Receipts Into Pharmacy Use this option to process receipts for purchase orders, control point transactions, and Prime Vendors. Menu Items: PSD RECEIVING Receiving PSD PURCHASE ORDER REVIEW Purchase Order Review PSD CP TRANSACTION REVIEW Control Point Transaction Review PSD DRUG RECEIPT HISTORY Drug Receipt History PSD PV INVOICE REVIEW Invoice Review (Prime Vendor) |
| PSD RECEIVING     | PSDREC    | Receiving Use this option to process receipts from a purchase order, control point transaction, or Prime Vendor, updating the balance, transaction file, and monthly activity.                                                                                                                                                                                                  |
| PSD REPRINT 2321  | PSDRDR    | Reprint Disp/Receiving Report (VA FORM 10- 2321) The Dispensing/Receiving Report (in lieu of the VA FORM 10-2321) may be reprinted. This report may be generated for a single Green Sheet or for a single NAOUwithin a specified date and time frame.                                                                                                                           |
| PSD REPRINT 2638  | PSDRPGS   | Green Sheet Reprint (VA FORM 10-2638) Pharmacy uses this option to reprint a single Green Sheet.                                                                                                                                                                                                                                                                                |
| PSD REPRINT LABEL | PSDLBLR   | Label Reprint for Dispensing Drug This option provides pharmacy the tools to reprint CS dispensing drug labels.                                                                                                                                                                                                                                                                 |

| Option Name              | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD REPRINT MENU         |           | Reprint Reports Menu This menu allows various narcotic reports and forms to be reprinted. To ensure drug accountability, certain CS documents should only be printed once. This option allows the reprinting of these controlled records. Menu Items: PSD REPRINT 2321 Reprint Disp/Receiving Report (VA FORM 10- 2321) PSD REPRINT 2638 Green Sheet Reprint (VA FORM 10-2638) PSD REPRINT WORKSHEET Dispensing Worksheet Reprint PSD REPRINT LABEL Label Reprint for Dispensing Drug PSD NURSE REPRINT 2321 Reprint Transfer Between NAOUs (VA FORM 10-                                                                                                                                                            |
| PSD REPRINT WORKSHEET    | PSDRWK    | Dispensing Worksheet Reprint Pharmacy personnel use this option to reprint a dispensing worksheet. The previously printed dispensing worksheet, for a given dispensing site, is utilized in reprinting this listing. The sort selected during the original printing of the worksheet sequences these orders. The reprinted worksheet lists a worksheet number assigned to this order, drug, quantity ordered, dispense to location, ordered by, comments and blanks for manufacturer, lot #, and expiration date. If this order has been processed by pharmacy since the original printing, the worksheet number will display as asterisk (*). A new worksheet will not be generated during the reprinting process. |
| PSD RX DISPENSING REPORT | PSDOPTR   | Rx (Prescription) Outpatient Dispensing Report A report sorted by drug, prescription number, or inventory type for a date range of outpatient dispensing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

| Option Name              | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|--------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD SETUP                |           | Set Up CS (Build Files) Menu Options that support management of files typically created and edited during initial set up of the CS module. Menu Items: PSD PRINT SETUP LISTS Print CS Set Up Lists PSD SITE Site Parameters PSD INACTIVATE NAOU Inactivate NAOU PSD INACTIVATE NAOU STOCK DRUG Inactivate NAOU Stock Drug PSD WARDCONVERSION Ward (for Drug) Transfer PSD WARDADD/DEL Add/Delete Ward (for Drug) PSD NAOU INV GROUP SORT Sort NAOUs in Inventory Group PSD TRANSFER MENU Transfer Stock Entries PSD DRUG CHECK Check Stocked Drugs for CS Use PSD BALANCE INITIALIZE Initialize Balance at Setup PSD ENTER/EDIT MENU |
| PSD SITE Lock: PSD PARAM | PSDSITE   | Site Parameters Site parameters for the CS module. This includes selecting an inpatient site for CS use and answering package specific questions concerning this site.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

| Option Name         | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD STOCK DRUG EDIT | PSDSTK    | Stock CS Drugs - Enter/Edit Provides access to enter or edit drugs stocked in the NAOU. This is how stocked drugs within an NAOU are added or changed. Duplicate entries are not allowed.                                                                                                                                                                                                                   |
| PSD STOCK LIST      | PSDLSTK   | Stock Drug List (Inventory Type and Location) This report lists all active stocked drugs you have defined in the DRUG ACCOUNTABILITY STATS file (#58.8). This report can be sorted alphabetically or by inventory type/location/drug. The data includes NAOU, location, drug name, stock level, and reorder level. The report sorted by inventory type/location/drug will include the type as printed data. |
| PSD STOCK PRINT     | PSDPSTK   | Stock Drug Print (Stock Level and Location) This report prints an alphabetic listing of all active drugs you have defined in the DRUG ACCOUNTABILITY STATS file (#58.8). This report lists NAOU, drug name, location, stock levels, all ward (for drug) assignments, and all inventory types.                                                                                                               |
| PSD STOCK UNIT LIST | PSDPDU    | Breakdown/Dispensing Unit Report This report provides an alphabetic listing of all active drugs you have defined in the DRUG ACCOUNTABILITY STATS file (#58.8). This listing includes breakdown unit and package size from the DRUG ACCOUNTABILITY STATS file (#58.8) and dispense unit and price per dispense unit from the DRUG file (#50).                                                               |

| PSD TRANSACTION MENU   | Pharmacist Menu This option provides pharmacy the access to process all CS transactions. This includes receipts into pharmacy; all orders dispensed from pharmacy, and outpatient prescriptions. Completing Green Sheets allows pharmacy to complete those Green Sheets with no discrepancies, math errors, drugs returned to stock, and drugs being held for destruction. Returns to stock and holding for destruction must be drugs associated with the Green Sheet when using this option. Menu Items: PSD RECEIPTS MENU Receipts Into Pharmacy PSD DISPENSINGMENU Dispensing Menu PSD COMPLETE GS Complete Green Sheet PSD OUTPATIENT Outpatient Rx's PSD TRANSFER VAULT DRUGS Transfer Drugs between Dispensing Sites PSD INFUSION MENU Infusion Order Processing Menu PSD DESTROY MENU Destructions Menu PSD ORDER ENTRY CS Order Entry For Ward PSD REC GS Receipt of Controlled Substance from Pharmacy PSD IRL INV MENU Barcode TRAKKER for Inventory PSD MFG/LOT/EXP DATE EDIT   |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| Option Name                      | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                  |           | Manufacturer, Lot #, and Exp. Date - Enter/Edit                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| PSD TRANSFER AOU                 | PSDTRA    | AOU to NAOU Transfer Entries This option will "copy" the active stock entries from a selected AR/WS Area of Use into one or more selected CS NAOU. As many as 10 NAOUs may be chosen for transfer at one time. The drug name only, or the drug name, stock level, and location code, or drug name, stock level, location code, and inventory types can be transferred. The "copy" process will not copy inactive drugs. The actual transfer takes place in a background job, which is queued automatically. When the transfer is complete, the user will be notified by a MailMan message. |
| PSD TRANSFER MENU Lock: PSD TRAN |           | Transfer Stock Entries This menu option supports two distinct methods of transferring active stock. The first "copies" active stock from a NAOU into another NAOU. The second "copies" active stock from an AR/WS Area of Use into a CS NAOU. Menu Items: PSD TRANSFER NAOU NAOU to NAOU Transfer Stock Entries PSD TRANSFER AOU AOU to NAOU Transfer Entries                                                                                                                                                                                                                              |
| PSD TRANSFER NAOU                | PSDTRN    | NAOU to NAOU Transfer Stock Entries This option will "copy" the active stock entries from a selected NAOU into one or more selected NAOUs. As many as 10 NAOUs may be chosen for transfer at one time. The drug name only, or drug name, stock level, and location code, or drug name, stock level, location code, and inventory types can be transferred. The "copy" process will not copy inactive drugs. The actual transfer takes place in a background job, which is automatically queued. When the transfer is complete, the user will be notified by a MailMan message.             |

| Option Name              | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD TRANSFER VAULT DRUGS | PSDTRV    | Transfer Drugs between Dispensing Sites This option is utilized to transfer controlled substances between dispensing sites. The inventory balances are updated within each dispensing site. When drugs are being transferred from one dispensing site into another, a MailMan message will be generated to the Pharmacy Supervisor holding the PSDMGR security key, if the receiving dispensing site does not normally stock that particular drug. |
| PSD WARD ADD/DEL         | PSDWADD   | Add/Delete Ward (for Drug) This option will allow a user to add or delete a ward (for drug) assignment for all stock drugs in one or more active NAOUs.                                                                                                                                                                                                                                                                                            |

| Option Name              | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD WARD CONVERSION      | PSDWCHG   | Ward (for Drug) Transfer This option will enable a user to change a ward (for drug) designation from the old ward to a new ward for all drugs in all NAOUs or in a single NAOU. This can be used, for example, when a ward is closed down for construction. A background job can be queued for a later time to do the conversion and a MailMan message will be sent to the person who queued the job when it has run to completion.                                                                                                                                                                                                                                                             |
| PSD WORKSHEET DISPENSING | PSDDWK    | Fill/Dispense CS Orders from Worksheet Pharmacy personnel use this option to process and verify CS orders. The Pharmacy Dispensing Worksheet should be printed first using the Print CS Dispensing Worksheet option. CS orders may be dispensed by selecting an individual worksheet number or by sort order on the worksheet. The pharmacist will be prompted for dispensing pharmacist, dispensing site, quantity dispensed, manufacturer, lot #, and expiration date. The prompt for pharmacy dispensing number will only appear if your site has elected to enter these control numbers manually. Otherwise, the software will automatically generate the next available dispensing number. |

| Option Name         | Routine   | Menu Text / Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD WORKSHEET PRINT | PSDPWK    | Print CS Dispensing Worksheet Pharmacy personnel use this option to print a dispensing worksheet. This worksheet MUST be printed prior to pharmacy dispensing CS orders. Pharmacy may sort this report within a dispensing site, by NAOU (one, some, or ALL), or by inventory group. Next, the orders are sorted by either (1) drug, then all NAOUs, or (2) NAOU, then all drugs. The worksheet lists a worksheet number assigned to this order, drug, quantity ordered, dispense to location, ordered by, comments, and blanks for manufacturer, lot #, and expiration date. When using the Fill/Dispense CS Orders from Worksheet option, pharmacy may process orders by individual request number (the assigned worksheet number) or by worksheet. If the worksheet method of dispensing is selected, the software will display each order to the pharmacist in the sequence the order was printed. Each time this report is run, a new worksheet will be built and all new CS orders will be included. The printed sequence of CS orders will change with each new worksheet. |

## &lt;This page is intentionally left blank.&gt;

## 8B Package-Wide Variables

## 27B Package-Wide Variables

There are no package-wide variables for Controlled Substances V. 3.0.

## 28B Package Variables

CS module contains only one package variable - PSDSITE. This variable must be defined and is required for the package to run. PSDSITE is set in the routine PSDSET as package users enter the module.

Some stations design their own menus for individual users. If this is the case, then the top level CS menu only must contain the following entry and exit code in the OPTION file (#19):

```
ENTRY ACTION: I '$D(PSDSITE) D ^PSDSET EXIT ACTION: K PSDSITE
```

This entry and exit code should not be included on the submenus in order to preserve the variable PSDSITE. This entry and exit code must be present because the PSDSITE variable is set as users enter the package. If the Kernel's '^OPTION NAME' feature is used to jump directly into lower levels of the CS package, then the 'Inpatient Site Name' prompt must be answered in order to define the PSDSITE variable. All options are independently invoked, however, if the instructions above are not followed, users will be repeatedly asked to select an Inpatient Site if there are two or more sites that are flagged as selectable for CS use.

## &lt;This page is intentionally left blank.&gt;

## 9B Resource Requirements

There are 298 CS routines that take up approximately 949K of disk space.

The KERNEL response time monitoring hooks, for capacity management studies, have been added to the Nurse Order entry routine PSDORN1 and the Pharmacy dispensing routine PSDDWK3.

## 29B Hardware Requirements

The following equipment is recommended to successfully implement V. 3.0:

Intermec TRAKKER 9440 (Barcode Reader) HP LaserJet III (or any compatible laser printer e.g., 3si, 4si, 5si, and Kyocera) VT320 (bi-directional only) or any bi-directional flow CRT

The laser single sheet feed printer is required to print the VA FORM 10-2638 and barcode ID labels. It is recommended that the printer be physically located in the narcotic vault for efficiency and security.

The laser printer must be a selectable device via the terminal server. Barcode printing is not available with a slaved printer.

The barcode TRAKKERs and CRTs are required to download/upload data necessary in maintaining a perpetual inventory within the pharmacy vault.

To support barcode label printing and downloading/uploading via the TRAKKER, certain hardware specific parameters for the TERMINAL TYPE file (#3.2) and DEVICE file (#3.5) are necessary. To assist IRM in setting up these devices the routine PSDTER has been included in the routine set. The TERMINAL TYPE file (#3.2) information includes right margin, form feed, page length, backspace, open execute, barcode on, and barcode off. DEVICE file (#3.5) data includes margin width, form feed, page length, backspace and subtype. For the TRAKKER, open printer port and close printer port is included in the terminal type information. See page 73 for examples in setting up the devices using the routine PSDTER.

## 35B Printing of Bar Codes

## Introduction

Bar Code: 3 of 9 portrait (most popular and applicable) it is variable-length, bi-directional, selfchecking, alphanumeric code. It consists of 36 defined numeric and upper case alphabetic

characters, seven special characters, and a stop/start character. Each character is composed of nine elements: five bars and four spaces. Three of nine elements are wide and six are narrow.

Suggested Typeface: Letter Gothic has a clean modern appearance and can be read at a glance when used with bar code.

## Printer Models tested:

HP LaserJet III Kyocera F800A HP LaserJet 3si HP LaserJet 4si

Output Technology Corporation (OTC) 560 DL.

## 36B HP LaserJet Printer

External Font Cartridge:

HP 36596A 3037 (custom font 3-9)(3/4si)

HP C2053A #C06 (bar code and more)

HP 92286W1 (bar code 3-9/OCR A)

Paper:

Good quality label paper

Terminal Type File: An OPEN EXECUTE, BAR CODE OFF and BAR CODE ON are needed to set the print commands (escape sequences).

HP LaserJet printer matches font characteristics in the following order: (symbol set, spacing, pitch, point size, style, stroke weight, typeface)

## Example: TERMINAL TYPE File (#3.2)

```
OPEN EXECUTE: W *27,(escape sequence) "E",(reset the printer to default settings) *27,(escape sequence) "&l0O",(&l(type of command)0O(portrait **use a lower case l and a upper case O ** *27,(escape sequence) "(8U",(Roman8 symbol set) *27,(escape sequence) "s0p(fixed spacing(zero) 16.66h(pitch # characters/inch) 8.5v(point size(height of a character) 0(upright style) s0b(medium stroke weight) 6T",(Gothic typeface) *27,(escape sequence)
```

```
orientation) "="(half line feed)
```

From the HP manual use the PCL TYPEFACE LIST UNDER CARTRIDGE FONTS to select the print commands (escape sequences) for the BAR CODE ON.

Use the following device and terminal type files to print:

- (1) Green sheets on plain paper
- (2) Drug labels

Example: DEVICE

File (#3.5)

NAME: DEMON BARCODE

$I: &lt;$Ivalue&gt;:

ASK DEVICE:

YES

ASK PARAMETERS: YES

SIGN-ON/SYSTEM DEVICE: NO

LOCATION OF TERMINAL:&lt;location&gt;

*MARGIN WIDTH: 0

*FORM FEED: #

*PAGE LENGTH:

58

*BACK SPACE: $C(8)

SUBTYPE: P-HP BARCODER

TYPE:

TERMINAL

LAT SERVER NODE:

IS3D2

LAT SERVER PORT:&lt;port#&gt;

VMS DEVICE TYPE:

NOT

SPOOLED

LAT PORT SPEED:96

## Example: TERMINAL TYPE File (#3.2)

```
NAME: P-HP BARCODER SELECTABLE AT SIGN-ON: NO RIGHT MARGIN: 0 FORM FEED: # PAGE LENGTH: 58 BACK SPACE: $C(8) OPEN EXECUTE: W 27)_"E"_$C(27)_"&l0O"_$C(27)_"(8U"_$C(27)_"(s0p"_$S($G(PSDC PI)=10:"10h14",1:"12h12")_"v0s0b6T" 10 PITCH: $C(27)_"(s10H" 12 PITCH: $C(27)_"(s12H" HIGH INTENSITY (BOLD): $C(27)_"(s4b" DEFAULT LINES PER INCH: $C(27)_"&l8C" X LINES PER INCH: $C(27)_"&l12C" BAR CODE OFF: "*"_$C(27)_"&l0O"_$C(27)_"(8U"_$C(27)_"(s0p"_$S($G(PSDCPI)=10:"1 0h14",1:"12h12")_"v0s0b6T" BAR CODE ON: $S($D(PSDX2):$C(27)_"*p"_(PSDX2-1*300+200)_"y*p"_(PSDX1-1*810+38) _"X",1:"")_$C(27)_"(0Y"_$C(27)_"(s0p8.1h12v0s0b0T
```

## Use the following device and terminal type files to print: (1) Patient ID Labels

## Example: DEVICE File (#3.5)

```
NAME: CSHPBAR $I: 0 ASK DEVICE: YES ASK PARAMETERS: YES SIGN-ON/SYSTEM DEVICE: NO LOCATION OF TERMINAL: SLAVE FOR *MARGIN WIDTH: 0 *FORM FEED: # *PAGE LENGTH: 58 *BACK SPACE: $C(8) SUBTYPE: P-HPCS TYPE: TERMINAL VMS DEVICE TYPE: NOT SPOOLED LAT PORT SPEED: 96
```

## Example: TERMINAL TYPE File (#3.2)

```
NAME: P-HPCS SELECTABLE AT SIGN-ON: NO RIGHT MARGIN: 0 FORM FEED: # PAGE LENGTH: 58 BACK SPACE: $C(8) OPEN EXECUTE: W *27,"E",*27,"&l0O",*27,"(8U",*27,"(s0p16.66h8.5v0s0b6T",*27,"= " BAR CODE OFF: "*",*27,"&l0O",*27,"(8U",*27,"(s0p16.66h8.5v0s0b6T",*27,"="
```

```
BAR CODE ON: *27,"&l0O",*27,"(0Y",*27,"(s0p12.00v4.35h0s"
```

## 37B OTC Printer

Use the following device and terminal type file to print:

- (1) Patient ID labels
- (2) Drug labels

## Example: DEVICE File (#3.5)

```
NAME: REX $I: _LTA9094: ASK DEVICE: YES ASK PARAMETERS: YES LOCATION OF TERMINAL: DEVELOPMENT HALLWAY *MARGIN WIDTH: 132 *FORM FEED: # *PAGE LENGTH: 66 *BACK SPACE: $C(8) BARCODE AVAIL: YES MNEMONIC: SCHMEGMO MNEMONIC: SMEGMA MNEMONIC: DEV LP SUBTYPE: P-OTC560 TYPE: TERMINAL LAT SERVER NODE: DSV2 LAT SERVER PORT: VMS DEVICE TYPE: NOT SPOOLED LAT PORT SPEED: 96
```

## Example: TERMINAL TYPE File (#3.2)

```
NAME: P-OTC560 RIGHT MARGIN: 132 FORM FEED: # PAGE LENGTH: 66 BACK SPACE: $C(8) 10 PITCH: $C(27)_"[w" 12 PITCH: $C(27)_"[2w" DESCRIPTION: OTC 560DL with Epson FX100 Emulation 16 PITCH: $C(27)_"[3w" BAR CODE OFF:
```

```
$C(27),"[0t" BAR CODE ON: $C(27),"[4;4;0;2;4;2;4;2}",$C(27),"[3t"
```

## 38B KYOCERA Printer

Prescribe is the native language of the laser printer. It gives the capability to control line and character spacing, adjust margins, change fonts, position text, draw graphics and print multiple copies. It sends commands to the printer to be executed.

## Commands:

!R! causes the printer to switch from normal text printing mode to Prescribe mode.

EXIT; returns printer back to normal mode.

There can be an unlimited number of commands between the initial !R! and the final EXIT;.

EX: !R! command; command;

RES; causes a page break and reset parameters back to the initial settings.

MRP; moves the cursor from its current position to a specified relative position, measured in the units designated by the UNITS command.

```
LC-4-11
```

BARC 19 , prints specified data in barcode form. The 19 provide code 39 with no check digits.

A command name should be followed by a space.(sem ; )

Each command must end with a semicolon (;).

A comma must follow a parameter and a semicolon must follow the last parameter.

Use the following device and terminal type file to print: (1) Drug Labels

## Example: DEVICE File (#3.5)

```
NAME: KYOCERA BARCODER $I: <$I value> ASK DEVICE: YES ASK PARAMETERS: YES SIGN-ON/SYSTEM DEVICE: NO LOCATION OF TERMINAL: <location> MARGIN WIDTH: 0 FORM FEED: # PAGE LENGTH: 66 BACK SPACE: $C(8) SUBTYPE: P-KYOCERA-BARCODE TYPE: TERMINAL
```

## Example: TERMINAL TYPE File (#3.2)

```
NAME: P-KYOCERA-BARCODE SELECTABLE AT SIGN-ON: NO RIGHT MARGIN: 0 FORM FEED: # PAGE LENGTH: 66 BACK SPACE: $C(8) OPEN EXECUTE: W "!R! RES;FONT "_$S($G(PSDCPI)=10:1,1:6)_";EXIT;" 10 PITCH: "!R! FONT1; EXIT;" 12 PITCH: "!R! FONT6; EXIT;" DEFAULT LINES PER INCH: "!R! SLM 2; EXIT;" X LINES PER INCH: "!R! SLPI 4.1; EXIT;" BAR CODE OFF: "', 60, 60, 3, 6, 6, 6, 3, 6, 6, 6;"_$S('$D(PSDX1):"",PSDX1=PSDC NT:"MRP 0 , 60;",1:"")_"EXIT;" BAR CODE ON: "!R! FONT 6; UNIT D; "_$S('$D(PSDX1):"",PSDX1=1:"MRP 0,-60 ; ",1:"")_$S('$D(PSDX1):"",1:"MRP "_(PSDX1>1*810+38)_" , 0 ;")_" BARC 19, N, '"
```

Use the following device and terminal type file to print: (1) Patient ID labels

## Example: DEVICE File (#3.5)

```
NAME: CSKYWARD $I: 0 ASK DEVICE: YES LOCATION OF TERMINAL: SLAVE FOR *MARGIN WIDTH: 0 *FORM FEED: # *PAGE LENGTH: 66 *BACK SPACE: $C(8) BARCODE AVAIL: YES SUBTYPE: P-KYOCERA-CSWARD-BARCODE TYPE: TERMINAL
```

## Example: TERMINAL TYPE File (#3.2)

```
NAME: P-KYOCERA-CSWARD-BARCODE SELECTABLE AT SIGN-ON: NO RIGHT MARGIN: 0 FORM FEED: # PAGE LENGTH: 66 BACK SPACE: $C(8) OPEN EXECUTE: W "!R! RES; FONT 7; EXIT;" CLOSE EXECUTE: W "!R!;RES;EXIT;",*27,"[4i" DESCRIPTION: CONTROLLED SUBSTANCES PATIENT LABLES ON WARD BAR CODE OFF: "', 60, 60, 2, 10, 10, 10, 2, 10, 10, 10; MRP 0 , 60; EXIT;" BAR CODE ON: "!R! FONT 7; UNIT D; MRP 0,-30 ; BARC 19, N, '"
```

## 39B Portable Barcode Reader (TRAKKER 9440)

CS V. 3.0 includes options for downloading IRL programs to the TRAKKER. For these options to function, the TRAKKER must be connected to your V IST A computer system. The TRAKKER comes with an RS-232 cable. The end of the cable that connects to your system terminates to a DB-25PIN connector.

The TRAKKER may be connected to the system via the auxiliary port of any CRT that supports complete bi-directional data flow and flow control (XON-XOFF) through the auxiliary port.

Whatever strategy works for addressing a slave printer to the CATHODE RAY TUBE (CRT) will also work for the TRAKKER.

The following procedure illustrates stepping through the configuration process to verify whether the TRAKKER is properly prepared to interface with V IST A .

<!-- image -->

Note : A brief example of the TRAKKER setup may be displayed by running the routine PSDTRAK from programmer mode.

To enter the configuration mode use the following steps:

1. Turn the TRAKKER on by pressing the &lt; on-off &gt; key. The unit should perform a brief self-test and then display a 'Ready' prompt.
2. Hold down the &lt; Ctrl &gt; key and press E . The words 'CONFIGURATION MENU:' should appear on the first line of the TRAKKER display screen. This is the configuration mode.
3. Press the &lt; Enter &gt; key until prompted to 'Select or modify operating parameters?', the word NO will appear on the fourth TRAKKER display line.
4. Change NO to YES by pressing the &lt; Space &gt; key.
5. Use the &lt; Enter &gt; key to step through the basic operating parameters. Unless otherwise instructed, use the &lt; Space &gt; key to make the selections:
- a. BEEP VOLUME: Set this according to the user's preference. If the work environment is noisy, choose HIGH .
- b. DISPLAY MODE: This tells the TRAKKER how to display data that is entered. Choose BUFFERED .
- c. CHARACTER SET: This selects an alphabet. Choose US-ASCII .
- d. CPU RESP REQD MODE: Tells the TRAKKER whether to wait for an acknowledgment from V IST A after each transmission of uploaded data. Choose DISABLED .
- e. PREAMBLE A REQUIRED: Tells the TRAKKER whether to check for one specific preamble on all data entered. Choose NO .
- f. LASER SCANNER MODE: Tells the TRAKKER whether to allow continuous scanning of barcode labels without release of the laser trigger in between. Choose ONE-SHOT TRIGGER .

- g. APPEND TIME TO DATA: Instructs the TRAKKER to add the correct time to each data record as it is transmitted. Choose NO .
- h. TIME IN SECONDS: Tells the TRAKKER whether time displays should include seconds. Choose YES .
- i. RESUME IRL PROGRAM: Choose NO .
- j. AUTOMATIC SHUT-OFF: A time-out feature such that the TRAKKER will turn itself off after a specified period of inactivity in order to conserve battery

- power. Enter the selection (in minutes) as a number. The TRAKKER will ignore the &lt; Space &gt; key. A 10-minute time-out period is suggested.
- k. BACKLIGHT TIMEOUT: A time-out feature on backlighting of the TRAKKER display screen. Intended to conserve battery power. Selections are made in seconds. A 60 second time-out period is suggested.
6. The next configuration heading is 'Select or modify comm protocol?' Use the &lt; Space &gt; key to select POINT TO POINT .
7. Use the &lt; Enter &gt; key to step through the comm protocol:
- a. CHECK CTS: Tells the TRAKKER whether or not to look for a CTS (clear to send) signal before transmitting data. Since V IST A uses XON/XOFF, choose NO .
- b. XON: When XON/XOFF protocol is used, the XON character must be specified here. Hold down the &lt; Ctrl &gt; key and press Q . DC1 should appear on the last TRAKKER display line. Press &lt; Enter &gt; to continue.
- c. XOFF: Hold down the &lt; Ctrl &gt; key and press S . Observe DC3 and press &lt; Enter &gt; to continue.
- d. BAUD RATE: The TRAKKER data transmission speed. 1200 baud is recommended.
- h. TIMEOUT DELAY: Tells the TRAKKER how long to wait for the next character of a downloaded IRL program before declaring an error condition. Choose 10 seconds .
- i. INTERCHAR DELAY: Tells the TRAKKER how long to pause between characters when uploading data to V IST A . Choose 50 milliseconds (ms) .
- j. TURNAROUND DELAY: Delay time between receipt of a character from V IST A and acknowledgment by the TRAKKER. This parameter is not critical with an XON/XOFF protocol. Choose 0 ms .
8. When the TURNAROUND DELAY is set, the 'Select or modify barcodes?' prompt will display again. The TRAKKER is now configured for use with V IST A .

- e.

- PARITY: Selection is DISABLED .

- f. DATA

- BITS:

Select 8 .

- g. STOP BITS: Select 1 .

To save any changes that have been made, hold down the &lt; Alt &gt; key and then press the &lt; E &gt; key. Once saved, the changes will remain in a non-volatile section of TRAKKER memory until the TRAKKER is re-configured.

To exit the configuration mode without saving any changes, hold down the &lt; Crtl &gt; key and press &lt; Z &gt;. Do this instead of the escape sequence (&lt; Alt &gt;, &lt; E &gt;) described above.

<!-- image -->

Note : If the TRAKKER has been configured differently, first it must be RESET. For details on this procedure, refer to the INTERMEC 944X TRAKKER READERS User's Manual . Next, the user must CONFIGURE the TRAKKER, repeating steps 1-8 above.

## Setting the TRAKKER clock:

<!-- image -->

Note : The clock should be set on the TRAKKER before users start performing inventories. It is not necessary to press &lt; Enter &gt; after responding YES to setting the clock.

After having turned the TRAKKER on, press &lt; Ctrl &gt; &lt; T &gt;.

The following will be displayed:

## 71B Example: TRAKKER Clock

Clock is set t o 93/ 14/ 11:21:06

Set t he clock? Y Y ear : 9 3 Mont h : 1 2 Day : 2 8 Hour : 9 Minut e: 4 5 Clock is set t o 93/ 12/ 28:09:45

## 40B Interfacing the TRAKKER 9440 to a VT-320 Auxiliary Port

The auxiliary port of the VT-320 is a six pin modular jack, so a cable with a six pin modular plug on one end and a male DB-25 connector on the other is needed.

<!-- image -->

The PRINTER SET UP SCREEN of the VT-320 will allow configuration of the CRT for use with a TRAKKER. To get to this screen:

1. Hold the &lt; Shift &gt; key and press &lt; SET UP&gt; .
2. Use the cursor control keys &lt; --&gt; &gt;(right arrow) to move the cursor to the box labeled Printer.
3. Press the &lt; Enter&gt; key.

From this point, the user can set the software selectable features of the auxiliary port as follows:

1. Speed: The baud rate of the auxiliary port. This must match the baud rate of the TRAKKER. 1200 is commonly used.
2. Printer to Host Communication: This must be set to Printer to Host for the TRAKKER upload/download operations.
3. Print Mode: Determines how the auxiliary port is controlled. Proper setting is Normal Print Mode .
4. XOFF: This selects whether or not the auxiliary port will use XON/XOFF data flow control. Proper setting is XOFF .
5. Bits and Parity: Selects a character format for the auxiliary port. Must match the character format of the TRAKKER.
6. Stop Bit: Selects the number of stop bits. Must match the format of the TRAKKER. One stop bit is commonly used.
7. Print Region: Unimportant for downloading or uploading. Commonly set to Print Full Page .
8. Printed Data Type: Used primarily with slaved printer but not critical for downloading or uploading. Commonly set to National Only .
9. Print Terminator: Selects whether or not the VT-320 should send a form feed at the end of each print operation. Proper setting is No Terminator .

Finally, appropriate entries in your TERMINAL TYPE file (#3.2) and DEVICE file (#3.5) are needed. For IRM, the routine PSDTER will allow the user to setup the TERMINAL TYPE file (#3.2) and DEVICE file (#3.5) information. This routine may be run from programmer's mode. Refer to page 9 in the Installation Guide for an example.

## Example: DEVICE File (#3.5)

NAME :

TRAKKERSL

LOCATION

:

SLAVED 9440 FROM VT420 AUXILLARY PORT

MARGIN WIDTH :

80

PAGE LENGTH

:

9999

MNEMONIC

:

TRAKKERSL

FORM FEED :

## Example: TERMINAL TYPE File (#3.2)

NAME :

C-VT420 (9440)

FORM FEED

:

## Functions on the TRAKKER:

&lt; Ctrl &gt;-&lt; T &gt;

This gives access to set the clock.

&lt; Ctrl &gt;-&lt; Enter &gt;-&lt; E &gt;

This gives access to end an IRL session. Simultaneously press the &lt; Ctrl &gt;-&lt; Enter &gt;keys, release them, then press &lt; E &gt;.

&lt; Ctrl &gt;-&lt; Enter &gt;-&lt; C &gt;

This gives access to clear the data files. Simultaneously press the &lt; Ctrl &gt;-&lt; Enter &gt;keys, release them, then press &lt; C &gt;.

[To clear the data files the user must have already ended the IRL session.]

## Example: Using Routine PSDTER

```
D ^XUP Setting up programmer environment Access code: [Enter your access code here] Terminal Type set to: C-VT100 Select OPTION NAME: >D ^PSDTER Select one of the following: 1 Load all three barcode Terminal Types 2 Load the P-HP BARCODER Terminal Type 3 Load the P-KYOCERA-BARCODE Terminal Type 4 Load the C-VT420 (9440) Terminal Type 5 Select your own Terminal Type 6 Display 7 Nevermind Enter response: ? If any of the selected Terminal Types already exist, I will ask for your approval before proceeding. Select one of the following: 1 Load all three barcode Terminal Types 2 Load the P-HP BARCODER Terminal Type 3 Load the P-KYOCERA-BARCODE Terminal Type 4 Load the C-VT420 (9440) Terminal Type 5 Select your own Terminal Type 6 Display 7 Nevermind Enter response: 1 Load all three barcode Terminal Types Current settings: [If a P-HP BARCODER TERMINAL TYPE already exists, current settings will be displayed] Are you sure that you want to stuff the Controlled Substances barcode set-up into the P-HP BARCODER Terminal Type? No// Y ES Updating P-HP BARCODER. Update the DEVICE file? No// ? Yes, and I will add the P-HP BARCODER Terminal Type and update a few fields in the device of your selection. Update the DEVICE file? No// <Enter> Current settings: [If a P-KYOCERA BARCODE TERMINAL TYPE already exists, current settings will be displayed] Are you sure that you want to stuff the Controlled Substances barcode set-up into the P-KYOCERA-BARCODE Terminal Type? No// ? Yes and I'll update OPEN EXECUTE, RIGHT MARGIN, PAGE LENGTH, Etc. fields. Are you sure that you want to stuff the Controlled Substances barcode set-up into the P-KYOCERA-BARCODE Terminal Type? No// Y ES Updating P-KYOCERA-BARCODE. Update the DEVICE file? No// <Enter> Are you sure that you want to stuff the Controlled Substances barcode set-up into the C-VT420 (9440) Terminal Type? No// Y ES Updating C-VT420 (9440). Update the DEVICE file? No// <Enter>
```

The HP LaserJet III and the Kyocera laser printer setup used in testing the printing of the VA FORM 10-2638 follows:

-----------------------------------------

## Example: Using Routine PSDTER (continued)

```
----------------------------------------------------------LASER PRINTER STATUS PAGE Software version 6.45 -20 , released 04/90. Units : Inches. Page : Portrait. Current font : 1. Current country : 0. Copies : 1. Current emulation : 6. Margins Spacings Top 0.300 Line 0.167 Bottom 10.300 Character 0.100 Left 0.000 Pen width 0.010 Right 8.000 Memory allocation (Kbytes) User memory avail. 187.225 In use (System) 108.773 Prescribe MCRO buff. 4.996 In use 0.000 PCL MCRO buff 3.500 In use 0.000 Parallel buff. size 10.000 RS232C buff. size 10.000 Raster size 128.000 Miscellaneous status Option (Comment) Value Option(Comment) Value CO(Reserved) 0 P1(Default Emulation) 6 C1(Page orientation) 0 P2(C.R. action) 1 C2(Dflt font Num-mid.) 0 P3(L.F. action) 1 C3(Dflt font Num-low) 1 P9(Escape Char.) 82 C4(PCL MCRO buff.) 0 UO(Line/Inch_high) 6 C5(Dflt font Num-High) 0 U1(Line/Inch_low) 0 A1(Top margin_high) 0 U2(Char/Inch_high) 10 A2(Top margin_low) 0 U3(Char/Inch_low) 0 A3(Left margin_high) 0 U5(Status page) 0 A4(Left margin_low) 0 U6(Country code) 0 A5(Page length_high) 13 U7(Dflt symbol set) 0 A6(Page length_low) 61 RO(Reserved) 6 A7(Page width_high) 8 R1(Reserved) 0 A8(Page width_low) 11 R2(Dflt paper size) 0 HO(Prescribe macro) 0 R3(Reserved) 0 H1(RS232C baud rate) 96 R4(Reserved 1 H2(RS232C data bits) 8 R5(Raster size) 1 H3(RS232C stop bit) 1 R6(Reserved) 0 H4(RS232C parity bit) 0 R7(Other paper size) 0 H5(RS232C protocol) 0 R8(D.W. Data length) 7 H6(Zoff threshold[%]) 90 R9(Reserved) 0 H7(Xon threshold[%]) 70 MO(PAR buffer size) 1 H8(RS232C buff. size) 1 M1(Reserved) 0 H9(F.F. time out) 3 M2(Reserved) 0 Service information /0024/0050/1061/0811/
```

----------------------------------------- example

continues

--------------------------------------- example

continues

---------------------------------------

## Example: Using Routine PSDTER (continued)

## * SAGG GLOBAL TRENDING DISPLAY FOR ^PSD *

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Site Name:

JACKSON

Complexity Level: 1

Supporting ISC:

7

System Type:

VAX-DSM

OS Version: V6.2

Kernel Version:

8.0

SAGG Version:

1.6T6

MUMPS Version: DSM V6.3D-031 for OpenVMS AXP

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ACTUAL GLOBAL TREND

NORMALIZED GLOBAL TREND

-------------------

-----------------------

SESSION # OF | GB SIZE GB GROWTH GB % | GB SIZE GB GROWTH|Flag DATES DAYS | In Blks In Blks Eff CHANGE| In Blks In Blks

|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

|

|

|

JUN

09,

1996

43

|

22,480

1,356

77%

6.0%

|

26,436

3,956|

*L*

JUN

22,

1996

13

|

22,819

339

77%

1.5%

|

24,015

1,196|

*L*

OCT

12,

1996

112|

30,197

7,378

76%

24.4%

|

40,501

10,304|

*H*

NOV

09,

1996

28

|

33,643

3,446

76%

10.2%

|

36,219

2,576|

*H*

DEC

07,

1996

28

|

39,183

5,540

76%

14.1%

|

41,759

2,576|

*H*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## STATISTICAL INFORMATION FOR ^PSD

--------------------------------

Beginning Global Size:

22,480 Blks

(23.0 Mb)

Ending Global Size:

39,183 Blks

(40.1 Mb)

## &lt;This page is intentionally left blank.&gt;

## 10B How to Generate On-line Documentation

Throughout the entire CS module, on-line help is obtained by entering a question mark (?) at any prompt to assist in the choice of actions.

The Data Dictionaries (DDs) are considered part of the on-line documentation for this software application. Use the VA FileMan DATA DICTIONARY UTILITIES option to print the DDs. For instructions on obtaining a list of files exported by the CS module refer to page 13 of this manual.

The namespace for the CS module is PSD.

## &lt;This page is intentionally left blank.&gt;

## 1 B Additional Information

## Templates

## 41B FILE #58.2 AOU INVENTORY GROUP

INPUT TEMPLATE(S) PSD INV GROUP

## &lt;This page is intentionally left blank.&gt;

## 12B Appendix A Health Level 7 (HL7)

Appendix A is comprised of the HL7 interface specifications from the Birmingham Information Resources Management Field Office, Department of Veterans Affairs.

## 30B Introduction

## 42B General Description

The V IST A Controlled Substances (CS) V. 3.0 package provides an interface between V IST A and a Narcotic Dispensing Equipment System (NDES). The CS package uses the HL7 Version 2.2 protocol. Messages are based on the definitions found in the HL7 Interface Standards [1]. The CS package uses Version 1.6 of the HL7 package to assist in exchanging health care information with any NDES [2]. The HL7 package can be divided into two parts: lower level protocol support between sending and receiving applications and the V IST A interface to the HL7 protocol.

## 43B Lower Level Protocols

The term lower level refers to a portion of the Open Systems Interconnect (OSI) model. The OSI model is divided into seven layers or levels. The lower levels (layers 1 through 4) support the actual physical connection between the systems and the communications protocol used. The CS package will use the HL7 Hybrid Lower Layer Protocol over an RS-232 connection as supported by the HL7 package.

This lower level interface provides the following functions:

-  Receive and send HL7 messages
-  Validate the HL7 Message Header (MSH) information
-  Invoke the appropriate V IST A application routine to process the data in the message
-  Send HL7 acknowledgment (ACK) messages back to the sending application

## 4 B Acronyms

ACK

Acknowledgment messages

ADT

Admission, Discharge, Transfer

CS Controlled Substances

DHCP

Decentralized Hospital Computer Program

HL7

Health Level Seven

MSH

Message Header

NDES

Narcotic Dispensing Equipment System

OSI

Open Systems Interconnect

## 45B Terms

## Dispense

Removal of medication by an authorized user, from a system cabinet, on behalf of a patient.

## Return

The return of unused medication by an authorized user, to a system cabinet, that has previously been dispensed for a patient and not used. Medication that is returned can be reused, and is returned to the cabinet to be dispensed for another patient.

## Waste

The return of partially used medication, by an authorized user, to a system cabinet, that has previously been dispensed for a patient and partially used. Medication that has been wasted is no longer usable.

## 46B Assumptions and Dependencies

Each session is begun between the V IST A system and the NDES at startup and will remain active as long as the supporting network and systems are functioning. The V IST A system is independent of the NDES. Shut down or startup of the NDES will not adversely affect the V IST A system. Likewise, shut down or startup of the V IST A system should not adversely affect the NDES.

## 47B References

- [1] Health Level Seven Interface Standards Version 2.2
- [2] DHCP Health Level 7 Developer Manual Version 1.5, July 1993

## 31B Purpose

This document specifies an interface to the Veterans Health Information Systems and Technology Architecture ( V IST A ) Controlled Substances V. 3.0 package based upon the Health Level 7 (HL7) protocol. It is intended that this interface form the basis for the exchange of health care information between the V IST A Controlled Substances V. 3.0 package and any Narcotic Dispensing Equipment Systems (NDES).

## 32B Overview

## 48B Statement of Intent

The Birmingham Information Resources Management Field Office (IRMFO) is developing, and plans to implement, a generic interface to the HL7 protocol for use by the V IST A Controlled Substances V. 3.0 package in communicating with any NDES for the purpose of exchanging health care information. The interface will strictly adhere to the HL7 protocol and will avoid using Z type extensions to the protocol whenever possible.

## 49B Scope and Audience

This document describes messages that are exchanged between the V IST A Controlled Substances V. 3.0 package and any NDES for the purpose of exchanging information concerning controlled substances. It is intended for use by vendors wishing to offer proposals for the

Controlled Substances V. 3.0 system interface, as well as facilitate an understanding on the part of the VA clinicians, IRM personnel, and clinical database developers of the nature and types of data to be made available.

## 3 B General Specifications

## 50B Communication Protocol

The HL7 protocol defines only the seventh level of the Open System Interconnect (OSI) protocol. This is the application level. Levels one through six involve primarily communication protocols. The HL7 protocol provides some guidance in this area. The communication protocols that will be used for interfacing with the V IST A Controlled Substances V. 3.0 package will be based on the HL7 Hybrid Lower Level Protocol, which is described in the HL7 Implementation Guide.

## 51B Application Processing Rules

The HL7 protocol itself describes the basic rules for application processing by the sending and receiving systems. Information contained in the protocol will not be repeated here; therefore, anyone wishing to interface with the V IST A Controlled Substances V. 3.0 package should become familiar with the HL7 protocol Version 2.2.

## 52B Message Types

Both systems will send an acknowledgment (ACK) message when the incoming message has been validated for correct syntax and content and committed to storage.

The V IST A system will send admission, discharge, and transfer (ADT) messages to the NDES whenever an admission, discharge, or transfer event occurs.

The NDES will send pharmacy dispense messages (DFT) to V IST A whenever a dispense, return, or waste event occurs*.

## 53B Messages

## 58B ADT Message Type

The ADT transaction set provides for transmitting new or updated patient demographic and visit information. The ADT message that the V IST A system will transmit to the NDES should contain the following segments:

| SEGMENT   | NAME                   | USER/HL7 DEFINED   |
|-----------|------------------------|--------------------|
| MSH       | Message Header         | HL7                |
| EVN       | Event Type             | HL7 (Table 0003)   |
| PID       | Patient Identification | HL7                |
| PV1       | Patient Visit          | HL7                |

## 59B DFT Message Type

The DFT message will be transmitted by the NDES for each instance of dispensing drugs to a patient.

| SEGMENT   | NAME                   | USER/HL7 DEFINED   |
|-----------|------------------------|--------------------|
| MSH       | Message Header         | HL7                |
| EVN       | Event Type             | HL7 (Table 0003)   |
| PID       | Patient Identification | HL7                |
| PV1       | Patient Visit          | HL7                |
| FT1       | Financial Transaction  | HL7                |

## 54B Fields

The segment definition tables list and describe the data fields in the segment and characteristics of their usage. The following information is specified about each data field.

| Sequence Number (SEQ):   | The ordinal position of the data field within the segment. This number is used to refer to the data field in the text comments that follow the segment definition table.                                                                                      |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Length (LEN):            | The maximum number of characters that one occurrence of the data field may occupy.                                                                                                                                                                            |
| Data Type (DT):          | Restrictions on the contents of the data field as defined by the HL7 Standard.                                                                                                                                                                                |
| Optionality (R/O/C):     | Whether the data field is required, optional, or conditional in a segment. The designations are: R - required; O (null) - optional; and C - conditional on the trigger event.                                                                                 |
| Repetition (RP/#):       | Whether the field may repeat. The designations are: N (null) - for no repetition allowed; Y - the field may repeat an indefinite or site determined number of times; and (integer) - the field may repeat up to the number of times specified in the integer. |
| Table (TBL#):            | A table of values which may be defined by HL7 or negotiated between he V IST A application and the vendor system.                                                                                                                                             |
| Element Name:            | Globally unique descriptive name for the field.                                                                                                                                                                                                               |

The following HL7 fields will be used to support the exchange of data for each of the segments listed in the segments paragraph. Tables referenced in the segments can be found in the HL7 Interface Standards document. For the standard HL7 segments, definitions of each element are provided for those fields, which are utilized. The field definitions can include specific information (e.g., expected format) for transmission.

## 5 B Message Segment Definitions:

## 60B MSA - Message Acknowledgment

The MSA segment contains information sent while acknowledging another message.

|   SEQ |   LEN | DT   | R/O   | RP/#   |   TBL# | ELEMENTNAME         |
|-------|-------|------|-------|--------|--------|---------------------|
|     1 |     2 | ID   | R     |        |      8 | Acknowledgment Code |
|     2 |    20 | ST   | R     |        |        | Message Control ID  |
|     3 |    80 | ST   |       |        |        | Text Message        |

## MSA field definitions

## (A) Acknowledgment Code (ID)

The ACKNOWLEDGMENT CODE can have the following values:

HL7 Table 8 - ACKNOWLEDGMENT CODE

| VALUE   | DESCRIPTION        |
|---------|--------------------|
| AA      | Application Accept |
| AE      | Application Error  |
| AR      | Application Reject |

## (B) Message Control ID (ST)

This field identifies the message sent by the sending system. It allows the sending system to associate this response with the message for which it is intended.

## (C) Message (ST)

This is an optional text field that further describes an error condition. The text may be printed in error logs or presented to an end user.

## 61B MSH - Message Header

The MSH segment defines the intent, source, destination, and some specifics of the syntax of a message.

|   SEQ |   LEN | DT   | R/O   | RP/#   |   TBL# | ELEMENTNAME           |
|-------|-------|------|-------|--------|--------|-----------------------|
|     1 |     1 | ST   | R     |        |        | Field Separator       |
|     2 |     4 | ST   | R     |        |        | Encoding Characters   |
|     3 |    15 | ST   |       |        |        | Sending Application   |
|     4 |    20 | ST   |       |        |        | Sending Facility      |
|     5 |    30 | ST   |       |        |        | Receiving Application |
|     6 |    30 | ST   |       |        |        | Receiving Facility    |
|     7 |    26 | TS   |       |        |        | Date/Time Of Message  |
|     8 |    40 | ST   |       |        |        | Security              |
|     9 |     7 | CM   | R     |        |     76 | Message Type          |
|    10 |    20 | ST   | R     |        |        | Message control ID    |
|    11 |     1 | ID   | R     |        |    103 | Processing ID         |
|    12 |     8 | ID   | R     |        |    104 | Version ID            |

## MSH field definitions

Separator (ST)

This field is the separator between the segment ID and the first real field, MSH-2ENCODING CHARACTERS. It serves as the separator and defines the character to be used as a separator for the rest of the message. The V IST A system uses: |.

## Encoding Characters (ST)

This field is four characters in the following order: the component separator, repetition separator, escape character and subcomponent separator. The V IST A system uses:^ ~\&amp;.

## Sending Application (ST)

This field is used for interface with lower-level protocols.

## Sending Facility (ST)

This field addresses one of several occurrences of the same application within the sending system. It is entirely site-defined.

## Receiving Application (ST)

This field is used for interface with lower-level protocols.

## Receiving Facility (ST)

This field identifies the receiving application among multiple identical instances of the application running on behalf of different organizations.

## Date/Time Of Message (TS)

This field is the date/time that the sending system created the message. If the time zone is specified, it is used throughout the message as the default time zone.

## Security (ST)

In some applications of HL7 this field is used to implement security features. Its use is not yet further specified.

## Message Type (CM)

MESSAGE TYPE is a composite element made up of: &lt;message type&gt; &lt;trigger event&gt; The first component is the message type, found in table 76 - MESSAGE TYPE. The second component is the trigger event code found in table 3 - EVENT TYPE CODE. The receiving system uses this field to know the data segments to recognize, and possibly, the application to which to route this message.

## Message Control ID (ST)

This field is a number or other identifier that uniquely identifies the message. The receiving system echoes this ID back to the sending system in the Message Acknowledgment segment (MSA).

## Processing ID (ID)

This field is used to decide whether to process the message as defined in the HL7 application processing rules.

HL7 Table 103 - PROCESSING ID

| VALUE   | DESCRIPTION   |
|---------|---------------|
| D       | Debugging     |
| P       | Production    |
| T       | Training      |

## VERSION ID (ID)

This filed is matched by the receiving system to its own version to be sure the message will be interpreted correctly. Only the following values are expected/accepted.

HL7 Table 104 - VERSION ID

|   VALUE | DESCRIPTION               |
|---------|---------------------------|
|     2.1 | Release 2.1 March 1990    |
|     2.2 | Release 2.2 December 1994 |

## 62B ERR - Error

The ERR segment is used to add error comments to acknowledgment messages.

|   SEQ |   LEN | DT   | R/O   | RP/#   |   TBL# | ELEMENTNAME             |
|-------|-------|------|-------|--------|--------|-------------------------|
|     1 |    80 | CM   | R     | Y      |     60 | Error Code and Location |

## ERR field definitions

Error code and location (CM)

This field is in standard HL7 format.

## 63B EVN - Event Type

The EVN segment is used to communicate necessary trigger event information to the NDES.

|   SEQ |   LEN | DT   | R/O   | RP/#   |   TBL# | ELEMENTNAME        |
|-------|-------|------|-------|--------|--------|--------------------|
|     1 |     3 | ID   | R     |        |   0003 | Event Type Code    |
|     2 |    19 | TS   | R     |        |        | Date/Time of Event |

## EVN field definitions

Event Type Code (ID)

A01

Admit a patient

A02

Transfer a patient

A03

Discharge a patient

P03

Post detail financial transaction

Date/Time of Event (TS)

The date/time of the admission, transfer, discharge, or financial transaction.

## 64B PID - Patient Identification

The PID segment is used by both applications as the primary means of communicating patient identification information. This segment contains permanent patient identifying, and demographic information that, for the most part, is not likely to change frequently.

|   SEQ |   LEN | DT   | R/O   | RP/#   | TBL#   | ELEMENTNAME              |
|-------|-------|------|-------|--------|--------|--------------------------|
|     1 |     4 | SI   |       |        |        | Set ID - Patient ID      |
|     2 |    16 | CK   |       |        |        | Patient ID (External ID) |
|     3 |    16 | CK   | R     | Y      |        | Patient ID (Internal ID) |
|     5 |    48 | PN   | R     |        |        | Patient Name             |

## PID field definitions

Set ID - patient ID (SI)

This is a sequence number used to identify the segment repetitions.

## Patient ID (External ID) (CK)

This is a composite element made up of: &lt;patient ID&gt; &lt;check digit&gt; &lt;check digit scheme&gt; &lt;assigning facility ID&gt; &lt;type&gt;

When the V IST A Controlled Substances V. 3.0 system transmits to the NDES, the first component is the social security number from the Patient file. The second and third components are the check digit and check digit scheme.

## Patient ID (internal ID) (CM)

This is a composite element made up of: &lt;patient ID&gt; &lt;check digit&gt; &lt;check digit scheme&gt; &lt;assigning facility ID&gt; &lt;type&gt;

When the V IST A Controlled Substances V. 3.0 system transmits to the NDES, the first component is the unique internal entry number from the Patient file. The second and third components are the check digit and check digit scheme.

## Patient name (PN)

This field is in standard HL7 format.

## 65B PV1 - Patient Visit

The PV1 segment is used by Registration/ADT applications to communicate information on a visit specific basis.

|   SEQ |   LEN | DT   | R/O   | RP/#   | TBL#   | ELEMENTNAME               |
|-------|-------|------|-------|--------|--------|---------------------------|
|     1 |     4 | SI   |       |        |        | Set ID - Patient Visit    |
|     3 |    12 | CM   | R     |        |        | Assigned Patient Location |
|     6 |    12 | CM   |       |        |        | Prior Patient Location    |
|     7 |    60 | CN   | R     |        |        | Attending Doctor          |

## PV1 field definitions

## Set ID - patient visit (SI)

This is a sequence number used to identify the segment repetitions.

## Assigned Patient Location

This is an HL7 ID type field that consists of three components: Nurse Unit (HL7 terminology), Room, and Bed. For the purposes of this interface, Nurse Unit will be considered synonymous with Ward Location. The value of the Ward Location component of the Assigned field will be a one to three digit code.

## Prior Patient Location

This is an HL7 ID type field that consists of three components: Nurse Unit (HL7 terminology), Room, and Bed. For the purposes of this interface, Nurse Unit will be considered synonymous with Ward Location. The value of the Ward Location component of the Prior Patient Locations field will be a one to three digit code.

## Attending doctor (CN)

This field is in standard HL7 format.

## B FT1 - Financial Transaction Segment

Housed in the DFT message, the FT1 segment is used for each instance of dispensing, returning, or wasting drugs for a patient.

|   SEQ |   LEN | DT   | R/O   | RP/#   | TBL#   | ELEMENTNAME              |
|-------|-------|------|-------|--------|--------|--------------------------|
|     2 |    12 | ST   |       |        |        | Transaction ID           |
|     4 |     8 | DT   | R     |        |        | Transaction Date         |
|     5 |     8 | DT   |       |        |        | Transaction Posting Date |
|     6 |     8 | ID   | R     |        |        | Transaction Type         |
|     7 |    20 | ID   | R     |        |        | Transaction Code         |
|    10 |     4 | NM   | R     |        |        | Transaction Quantity     |
|    20 |    60 | CN   | R     |        |        | Performed By Code        |

PV1 field definitions

Transaction ID (ST)

Number assigned by the sending system for control purposes. The number can be returned by the receiving system to identify errors.

Transaction Date (DT)

Date of transaction

Transaction Posting Date (DT)

Date the transaction was sent to V IST A

Transaction Type (ID)

D - Dispensed, R - Returned, W - Wasted

Transaction Code (ID)

Code for the purpose of uniquely identifying the transaction

Transaction Quantity (NM)

The quantity of medication dispensed, returned, or wasted.

Performed By Code (CN)

The composite number/name of the person, which performed the transaction, with number being the internal entry number (DUZ) from the V IST A NEW PERSON file (#200)

## 34B Transaction Specifications

## 56B General

The flow of transactions between the V IST A system and the NDES may occur in two ways.

1. The V IST A system will send ADT event type HL7 messages to the NDES whenever an admission, discharge, or transfer event occurs.
2. The NDES will send pharmacy dispense messages (DFT) to V IST A whenever a dispense, return, or waste event occurs.

## 57B Specific Transactions

## 67B Admit a Patient (Event Code A01)

When a patient is admitted, an ADT Message (ADT) with event code A01 is sent from the V IST A system to the NDES. These ADT messages would consist of the following segments.

## ADT ADT MESSAGE

| MSH   | Message Header         |
|-------|------------------------|
| EVN   | Event Type             |
| PID   | Patient Identification |
| PV1   | Patient Visit          |

## Example: Admit a Patient (Event Code A01)

```
MSH|^~\&|PSD-CS|500|PSD-CS|NDES|199112202359||ADT^A01|12345-1|P|2.1 EVN|A01|19911220100020 PID|1|000-77-1640^8^M10|1^1^M10||CSPATIENT^ONE|||||||||||||| PV1||I|15^E200^2|||3333^CSPROVIDER^ONE
```

The NDES would then send a General Acknowledgment (ACK) message back to the V IST A system.

## 68B Transfer (Event Code A02)

When a patient is transferred and their location or treating specialty changes, an ADT Message with event code A02 is sent from the V IST A system to the NDES. This ADT message would consist of the following segments.

## ADT ADT MESSAGE

MSH

Message Header

EVN

Event Type

PID

Patient Identification

PV1

Patient Visit

## Example: Transfer (Event Code A02)

```
MSH|^~\&|PSD-CS|500|PSD-CS|NDES|199112202359||ADT^A01|12345-1|P|2.1 EVN|A02|19911220100020 PID|1|000-77-1640^8^M10|1^1^M10||CSPATIENT^ONE|||||||||||||| PV1||I|15^E200^2|||3333^CSPROVIDER^ONE
```

The NDES would then send a General Acknowledgment (ACK) message back to the V IST A system.

## 69B Discharge (Event A03)

When a patient is discharged, an ADT Message with event code A03 is sent from the V IST A system to the NDES. This ADT message would consist of the following segments.

## ADT ADT MESSAGE

MSH

Message Header

EVN

Event Type

PID

Patient Identification

PV1

Patient Visit

## Example: Discharge (Event A03)

```
MSH|^~\&|PSD-CS|500|PSD-CS|NDES|199112202359||ADT^A01|12345-1|P|2.1 EVN|A03|19911220100020 PID|1|000-77-1640^8^M10|1^1^M10||CSPATIENT^ONE|||||||||||||| PV1||I|15^E200^2|||3333^CSPROVIDER^ONE
```

The NDES system would then send a General Acknowledgment (ACK) message back to the V IST A system.

## 13B Glossary

| Action Prompt      | There are two action prompts that occur during the pharmacy dispensing process. The action codes appear in '( )'. The following codes are valid: V Verify or Dispense the order (Displayed only to the dispensing pharmacist) P Process or Fill the order (Displayed only to the pharmacy technician or pharmacist filling but not dispensing the order) DC Cancel the order E Edit the order B Bypass the order S Show the order   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Completion Status  | A review status is attached to each CS Green Sheet returned to pharmacy. The following are valid:                                                                                                                                                                                                                                                                                                                                   |
| Daily Activity Log | The Daily Activity Log lists data, within a selected date range, associated with the VA FORM 10-2320 for a dispensing site.                                                                                                                                                                                                                                                                                                         |

| Dispensing #                                            | Control number assigned by pharmacy when dispensing a CS drug. This number is used to track the Green Sheet and drug. Also referred to as the Disp #, Green Sheet #, or GS # throughout the CS package.                                                                                                                                                                                              |
|---------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dispensing/Receiving Report (in lieu of VA FORM10-2321) | This report can be printed in lieu of VAFORM 10-2321 and lists all Controlled Substances orders dispensed to an NAOU. The signature of the dispensing pharmacist and the nurse receiving the drug are required.                                                                                                                                                                                      |
| Dispensing Site                                         | An NAOU set up as a pharmacy vault that dispenses CS drugs.                                                                                                                                                                                                                                                                                                                                          |
| Dispensing Worksheet                                    | This worksheet compiles a list of all pending CS request orders for a selected dispensing site. A worksheet number, drug name, quantity ordered, requesting NAOU, ordered by, comments, and blanks for pharmacy dispensing number, manufacturer, lot number, and expiration date are listed on the worksheet.                                                                                        |
| Drug Address Code Expansion                             | Text used to clarify the meaning of a drug address code. For example, the code S would be expanded and printed as shelf. (These codes and expansions are locally created terms.)                                                                                                                                                                                                                     |
| Drug Address Code (Location Code)                       | A code that represents the location of a drug in the NAOU. For example, if TYLOX is stored in an NAOU on the second set of shelves, third shelf from the top, its drug address code could be expressed as S,2,3. The address code can consist of up to three levels separated by a comma. Each level should further define the exact location. The code is associated with an expansion for clarity. |
| Green Sheet #                                           | Control number assigned by pharmacy when dispensing a CS drug. This number is used to track the Green Sheet and drug. It is also referred to as the GS #, Dispensing #, or Disp # throughout the CS package.                                                                                                                                                                                         |
| Green Sheet                                             | The CONTROLLED SUBSTANCE ADMINISTRATION RECORD (VA FORM 10-2638) is referred to as a Green Sheet or GS throughout the CS package. Pharmacy dispensing number, drug name, expiration date, quantity                                                                                                                                                                                                   |

| Inpatient Site                    | dispensed, lot number, ordered by, dispensed by, and ward (NAOU) are printed on the form. Inpatient Site must be defined for each NAOU. The CS software utilizes this data to distinguish multi-divisional                                                                                                                              |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inspector's Log                   | This report lists all active Green Sheets by NAOU. It includes the following information: Green Sheet #, drug name, date dispensed, quantity dispensed, expiration date (if available), blanks for quantity on hand, and a signature blank for verification.                                                                            |
| Interactive Reader Language (IRL) | The Interactive Reader Language (IRL) is a language used to write programs on barcode readers that allow the reader to interact with the user.                                                                                                                                                                                          |
| Master Vault                      | An NAOUset up as your primary dispensing site.                                                                                                                                                                                                                                                                                          |
| NAOU Inventory Group              | An NAOU Inventory Group is defined by pharmacy to represent the Narcotic Areas of Use, which are inventoried together as a group. By grouping the commonly inventoried NAOUs under an easy to remember group name, the elements of the inventory are established, and do not have to be redefined every time an inventory is scheduled. |
| Narcotic Location                 | An NAOU set up for the nursing wards, pharmacy IV room, or a pharmacy working stock area.                                                                                                                                                                                                                                               |
| NAOU - Narcotic Area of Use       | A Narcotic Area of Use (NAOU) is a place where commonly stocked CS drugs are stored for use by pharmacy, wards or treatment areas. There are three types                                                                                                                                                                                |

## Order Status

## PSD ERROR

of NAOUs: 1) Master Vault, 2) Satellite Vault and 3) Narcotic Locations.

A processing status is attached to each CS request order. The following are valid:

## ORDERED - NOT PROCESSED -

Ordered by nursing but not processed by pharmacy.

PROCESSED - NOT DISPENSED -Processed (filled) by pharmacy but not yet dispensed.

FILLED - NOT DELIVERED -Dispensed and verified by pharmacy but not delivered to the requesting NAOU.

DELIVERED - ACTIVELY ON NAOU -Drug stored on the NAOU.

## COMPLETED - GREEN SHEET READY FOR

PICKUP -Nursing has flagged the Green Sheet ready for pharmacy pickup.

COMPLETED - GREEN SHEET PICKED UP -Green Sheet returned to pharmacy but not yet reviewed.

COMPLETED - REVIEWED -Pharmacy has reviewed the Green Sheet.

## COMPLETED - PENDING PROBLEM

RESOLUTION -Pharmacy has reviewed the Green Sheet and a problem exists.

CANCELLEDOrder cancelled.

TRANSFERRED TO ANOTHER NAOUOrder and drug transferred to another NAOU.

UNDER REVIEW BY INSPECTOROrder and drug pulled from NAOU by CS Inspector for review.

LOGGED BY TRAKKERAll drug doses from this order have been logged out to patients using the TRAKKER.

Allocate this key to pharmacy supervisors responsible for maintaining the narcotic vault. This key controls access to reports listing various errors and exception conditions generated when entries are filed from the barcode

| PSD NURSE   | TRAKKER. Also, the holders of this key will receive electronic mail messages created by using the TRAKKER. Allocate this key to nurses, usually LPNs, who may only receive and administer controlled substances drugs, but cannot place order requests.   |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD PARAM   | Allocate this key to only the Inpatient Pharmacy Coordinators. This key controls the printing of the Green Sheets and the range of automated dispensing numbers for a dispensing site.                                                                    |

| PSD TECH     | Allocate this key to control substance technicians. This key controls access to the List On-Hand Amounts [PSD ON- HAND TECH], Transfer Drugs between Dispensing Sites Report [PSD PRINT VAULT TRANSFERS TECH], and the Daily Activity Log (in lieu of VA FORM 10-2320) [PSD DAILY LOG TECH] options on the Technician (CS Pharmacy) Menu [PSD PHARM TECH].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSD TECH ADV | Allocate this key to specific control substance technicians who perform advance functions. This key controls access to the Receipts Into Pharmacy [PSD RECEIPTS MENU], Dispensing Menu [PSD DISPENSING MENU], Destructions Menu [PSD DESTROY MENU], Manufacturer, Lot #, and Exp. Date - Enter/Edit [PSD MFG/LOT/EXP], Outpatient Rx's [PSD OUTPATIENT], Complete Green Sheet [PSD COMPLETE GS], Destroyed Drugs Report [PSD DEST DRUGS REPORT], DEA Form 41 Destroyed Drugs Report [PSD DESTROY DEA41], Destructions Holding Report [PSD DESTRUCTION HOLDING], Add Existing Green Sheets at Setup [PSD EXISTING GS], Green Sheet Transfer Between NAOUs Report [PSD GS TRANSFER (NAOU) REPORT], NAOU Usage Report [PSD NAOUUSAGE], Transfer Drugs between Dispensing Sites [PSD TRANSFER VAULT DRUGS] options on the Technician (CS Pharmacy) Menu [PSD PHARM TECH]. The CS technician may perform all functions of the Outpatient Rx's [PSD OUTPATIENT] |
| PSD TRAN     | Allocate this key only to the Inpatient Pharmacy Coordinator. This key controls the access to the NAOU to NAOU Transfer Stock Entries [PSD TRANSFER NAOU] option. Users can copy stock entries from one NAOU into another NAOU or from an Auto Replenishment/Ward Stock (AR/WS) Area Of Use (AOU) into an NAOU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PSDMGR       | Allocate this key to the Inpatient Pharmacy Coordinators. This key controls the editing of CS files for package set up and it locks the Supervisor (CS) Menu option.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PSDRPH       | This key authorizes pharmacists to verify and dispense controlled substance prescription(s). The PSDRPH security key should be given to registered pharmacists working on controlled substances to honor Drug Enforcement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

Administration (DEA) regulations and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist.

| PSJPHARMTECH    | Allocate this key to pharmacy technicians handling controlled substances orders.                                                                                                                                                                                                                                                                  |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSJ RNURSE      | Allocate this key to nurses who request and receive controlled substances orders on the wards.                                                                                                                                                                                                                                                    |
| PSJ RPHARM      | Allocate this key to pharmacists who can dispense and receive controlled substances drugs.                                                                                                                                                                                                                                                        |
| Satellite Vault | An NAOU set up as a secondary dispensing site.                                                                                                                                                                                                                                                                                                    |
| Stock Drug      | A drug (from the DRUG file (#50)) stored in an NAOU.                                                                                                                                                                                                                                                                                              |
| Stock Level     | The quantity of a drug stocked in a specific NAOU.                                                                                                                                                                                                                                                                                                |
| TRAKKER         | A barcode collection system utilized by scanning barcode labels or pressing the keypad.                                                                                                                                                                                                                                                           |
| V IST A         | Veterans Health Information Systems and Technology Architecture                                                                                                                                                                                                                                                                                   |
| Ward (for Drug) | The name of the ward or wards that will use this particular drug. It is important to accurately answer this prompt because this is the link between the Inpatient Medications V. 5.0 package and the Controlled Substances V. 3.0 package. The Inpatient Medications V. 5.0 package looks at this field to know if the drug is a CS stocked drug. |
