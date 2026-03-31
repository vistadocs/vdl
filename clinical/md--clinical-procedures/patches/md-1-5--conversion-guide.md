---
title: MD*1*5 Conversion Guide
doc_type: CVG
doc_label: Conversion Guide
doc_layer: patch
doc_subject: 
app_code: MD
app_name: Clinical Procedures
section: CLI
app_status: active
pkg_ns: MD
patch_ver: 1
patch_id: MD*1*5
group_key: "MD:MD:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - conversion
  - procedure
  - medicine
  - report
  - edit
  - reports
  - status
  - table
  - historical
  - procedures
page_count: 0
word_count: 11816
section_count: 8
table_count: 60
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/md_1_p5_cvt.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/md_1_p5_cvt.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=139"
---

![](md-1-5-conversion-guide/001.png)

CLINICAL PROCEDURESCONVERSION GUIDEforMD\*1.0\*5

August 2006

Health Systems Design and Development

Provider Systems

#### Revision History

|          |              |                       |                                    |
|----------|--------------|-----------------------|------------------------------------|
| Date | Revision | Description       | Author                         |
| 08/2006  | 1.0          | CP Patch 5.0 released | <span class="mark">REDACTED</span> |
|          |              |                       |                                    |
|          |              |                       |                                    |
|          |              |                       |                                    |

#### Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview of the Conversion Process](#overview-of-the-conversion-process)
  - [## Intended Audience](#intended-audience)
  - [Related Manuals](#related-manuals)
- [# Installation and Conversion Instructions](#installation-and-conversion-instructions)
  - [Install PackMan Message](#install-packman-message)
  - [Prepare for Conversion](#prepare-for-conversion)
    - [Set up a Host File Server (HFS) Device and Terminal Type](#set-up-a-host-file-server-hfs-device-and-terminal-type)
    - [Verify Procedure/Subspecialty File](#verify-proceduresubspecialty-file)
    - [Print Status Report](#print-status-report)
    - [Release and Verify Procedure Results.](#release-and-verify-procedure-results)
    - [Select Medicine Reports](#select-medicine-reports)
  - [Run Conversion in Test Mode](#run-conversion-in-test-mode)
    - [Set Up the Conversion Parameters](#set-up-the-conversion-parameters)
    - [Enter Hospital Location in CP Manager](#enter-hospital-location-in-cp-manager)
    - [View List of TIU Titles Needed](#view-list-of-tiu-titles-needed)
    - [View Conversion Summary Breakdown](#view-conversion-summary-breakdown)
    - [Build the Conversion List](#build-the-conversion-list)
    - [Run the Conversion in Test Mode](#run-the-conversion-in-test-mode)
    - [Review the Summary of Conversion Process Report](#review-the-summary-of-conversion-process-report)
    - [Fix Medicine Reports](#fix-medicine-reports)
    - [Repeat Process](#repeat-process)
    - [Run Disk Space Requirements Option](#run-disk-space-requirements-option)
  - [Run the Conversion in Real Mode](#run-the-conversion-in-real-mode)
    - [Switch to Real Mode](#switch-to-real-mode)
    - [Run the Conversion in Real Mode](#run-the-conversion-in-real-mode-1)
    - [Verify the Reports](#verify-the-reports)
    - [Lockout Medicine Options](#lockout-medicine-options)
- [Glossary](#glossary)
- [Index](#index)
With the Clinical Procedures (CP) Patch 5, MD\*1.0\*5, you can convert existing Medicine report text into TIU documents and display these documents on the Computerized Patient Record System (CPRS) Reports tab.
As sites implement CP, more medical devices are being interfaced with CP to bring over the final result of the procedures. As sites migrate from using the medical device and Medicine to using the medical device with CP, we see a need to consolidate the historical medicine reports in the Medicine package with the CP reports. The conversion of medicine reports into TIU documents is the next step in the plan for CP to replace Medicine. CP Patch 5 will take the text of the medicine report in its current state and move it to a non-editable form in a TIU document. These converted TIU documents will provide a true view of the interpretation at the time of conversion.
Topics discussed in this chapter are:
- [Overview of the Conversion Process](#_Overview_of_the_Conversion Process)
- [Intended Audience](#intended-audience)
- [Related Manuals](#related-manuals)

## Overview of the Conversion Process 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch provides the tools to consolidate historical Medicine reports into CP reports. Installing patch MD\*1\*5 will load a conversion menu option into your account. This menu option provides a list of options that your site will need to set up the Medicine File parameters for the conversion, build the conversion list, run the conversion, and disable the Medicine options. It also provides a list of options which your site can use as a tool to calculate disk space needed for the TIU document, display the error log, and display the summary of the conversion.

The conversion can be run in two modes:

- TEST Mode: The conversion process will generate the medicine report into a host server file and calculate the number of lines and bytes needed for the report. The actual conversion does not take place.
- REAL Mode: The conversion process will generate the medicine report into a host server file, calculate the number of lines and bytes of the report. A CP study will be created and a TIU document with a historical procedure title and the report text will be created. If the medicine record was associated with a consult procedure, the consult procedure will be disassociated from the medicine report and re-associated with the TIU document created. If there are images associated with the medicine record, the images will be disassociated from the medicine record and re-associated with the TIU document. All the links between the Consult, TIU, and Imaging will be tied to a CP study. The actual conversion will take a printed medicine report text and move it to a TIU document, move the linkages from Consult and Imaging and re-link them to the TIU document.

This benefit of the conversion is to provide Clinical Procedures (CP) end users with the ability to access Medicine data in a CP report format.

Only Medicine reports with the following statuses will be converted:

- Released On-Line Verified
- Released Off-Line Verified
- Released On-Line Verified of Superseded
- Released Off-Line Verified of Superseded
- Released Not Verified
- Reports without any status can be converted if the “Convert if no status” flag is set to “Yes” for the procedure.

Important Notes:

- You will want to lock down a dedicated terminal when you run the conversion, as it may take several hours to run depending on how many records are to be converted.
- It is strongly suggested that you run the conversion in test mode first in a mirrored test account, make sure all records converted in test mode successfully, then run the conversion in real mode in the test account. Records are not actually converted in test mode.

The Medicine options can be disabled and locked out after the conversion is run in Real mode by using the Conversion Lockout menu option.

IT IS VERY IMPORTANT TO READ AND UNDERSTAND ALL OF THE INSTRUCTIONS IN THIS MANUAL BEFORE RUNNING THE CONVERSION. AFTER THE MEDICINE OPTIONS HAVE BEEN LOCKED OUT, YOU WILL NO LONGER BE ABLE TO USE THEM.

## ## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Conversion Guide is intended for use by Clinical Application Coordinators (CAC), Technical Support Office (TSO), Information Resource Management (IRM), Implementation Managers, and Enterprise VistA Support (EVS).

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Here is a list of related manuals that you may find helpful:

> Clinical Procedures Installation Guide

> Clinical Procedures Technical Manual and Package Security Guide

> Clinical Procedures Implementation Guide

> CPRS User Manual

> Consult/Request Tracking User Manual

> Consult/Request Tracking Technical Manual

> Text Integration Utilities (TIU) Implementation Guide

> Text Integration Utilities (TIU) User Manual

> VistA Imaging System (Clinical) User Manual

You can locate these manuals in the [VistA Documentation Library (VDL)](http://www.va.gov/vdl/). Select Clinical from the VDL web page, select the package you want, and then select the manuals. For example, you can select CPRS on the left side of the page. The list of CPRS manuals is displayed.

# # Installation and Conversion Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is important to perform each of the following tasks, which will help you prepare for the final conversion. Keep in mind that after the conversion is complete, you will not be able to enter data manually, so it is critical that you perform these tasks in an organized manner.

Here is a list of required tasks to follow for a successful conversion:

- [Install PackMan Message](#_Install_PackMan_Message)
- [Prepare for Conversion](#prepare-for-conversion)
- [Test the Conversion](#_Run_Conversion_in_Test Mode)
- [Finalize the Conversion](#_Run_the_Conversion_in Real Mode)

## Install PackMan Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you install this patch, your site must have Clinical Procedures V.1.0 and Medicine V.2.3 installed including the following patches:

- Patch 182 of Text Integration Utilities V. 1.0 (TIU\*1.0\*182).

> Make sure to run the option TIU182 DDEFS, MED CONVERSION after patch TIU\*1.0\*182 is installed. This option will populate the CLINICAL PROCEDURES CLASS of documents with a Document Class called HISTORICAL PROCEDURES and a list of standardized historical procedure titles to support patch MD\*1.0\*5 conversion.

- Patch 47 of VistA Imaging V. 3.0 (MAG\*3.0\*47).
- Patch 37 of Consults V. 3.0 (GMRC\*3.0\*37).

You can request patch MD\*1.0\*5 from Enterprise VistA Support (EVS), and then install the build on the M server. Be sure to coordinate the installation with the Clinical Application Coordinator (CAC). Installation should take less than 3 minutes.

After you receive the patch software:

1.  Use the INSTALL/CHECK MESSAGE option on the PackMan menu.
2.  From the Kernel Installation and Distribution System Menu, select the Installation menu.
3.  From this menu, you may elect to use the following options (when prompted for INSTALL NAME, enter MD\*1.0\*5):
1.  Backup a Transport Global
2.  Compare Transport Global to Current System
3.  Verify Checksums in Transport Global
4.  Use the Install Package(s) option and select the patch MD\*1.0\*5.
5.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//," respond NO.
6.  When prompted "Want KIDS to INHIBIT LOGONs during the install? YES//," respond NO.
7.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//," respond NO.
8.  When prompted “DEVICE: HOME //,” respond with \<RET\> or a device name.

## Prepare for Conversion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is important to carefully prepare for the conversion. All steps in this section must be completed in the following order.

1.  [Set up an HFS Device and Terminal Type](#_1._Set_up_an HFS Device and Termina)
2.  [Verify Procedure/Subspecialty File](#verify-proceduresubspecialty-file)
3.  [Print Status Report](#print-status-report)
4.  [Release and Verify Procedure Results](#_4._Release_and_Verify Procedure Res)
5.  [Select Medicine Reports](#select-medicine-reports)

### Set up a Host File Server (HFS) Device and Terminal Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to make an appointment with IRM to help you set up a test for the device on your system that you will use to print the reports. The following device and terminal type settings must be entered exactly as shown. The P-MDHFS terminal type must be set up before the MDHFS device. IRM can assist you with this step. When properly set up, this device will point to a text file and retrieve the data that will be converted into a TIU document.

> TERMINAL TYPE SETTINGS:

> NAME: P-MDHFS SELECTABLE AT SIGN-ON: NO

> RIGHT MARGIN: 80 FORM FEED: \#

PAGE LENGTH: 88 BACK SPACE: \$C(8)

> DEVICE FILE SETTINGS:

> NAME: MDHFS \$I: MDCVT.TXT

> ASK DEVICE: NO ASK PARAMETERS: NO

> SIGN-ON/SYSTEM DEVICE: NO QUEUING: NOT ALLOWED

> LOCATION OF TERMINAL: \*\*\* ASK HOST FILE: NO

> ASK HFS I/O OPERATION: NO SUPPRESS FORM FEED AT CLOSE: YES

> OPEN PARAMETERS: "NWS" SUBTYPE: P-MDHFS

> TYPE: HOST FILE SERVER

### Verify Procedure/Subspecialty File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must verify that you are using a valid routine to generate the Medicine reports. Table 1 displays the data from the Procedure/Subspecialty file (#697.2). These are the procedures that are exported with Medicine V2.3.

To view this information, use FileMan to print the following fields of the Data Dictionary from file 697.2:

- Name
- Global Location
- Entry Point of Print Routine
- Print Routine
- Print Line

  Look for the procedure name, such as ECHO, in the first column and check that the data in the Global Location field matches the entry in the 697.2 file. In addition, check that there are valid entries in the Entry Point of Print Routine, Print Routine, and Print Line fields. If the Entry Point of Print Routine, Print Routine, or Print Line field is blank for an entry, use the appropriate entry from this table (Table 1) to fill in the blank field. The Print Routine and Entry Point must exist for the entry to be valid.

  Note: If the Print Line defaults as blank, that’s okay.

Table 1 – Procedure/Subspecialty File (697.2)

| Name (Procedure) | Global Location | Entry Point of Print Routine | Print Routine | Print Line |
|----------------------|---------------------|----------------------------------|-------------------|----------------|
| ECHO                 | MCAR(691            | ECHO                             | MCARP             | ECHO1          |
| CATH                 | MCAR(691.1          | CATH                             | MCARP             | CATH1          |
| ECG                  | MCAR(691.5          | ECG                              | MCARP             | ECG1           |
| HOLTER               | MCAR(691.6          | HOLTER                           | MCARP             | HOLTER1        |
| ETT                  | MCAR(691.7          | ETT                              | MCARP             | ETT1           |
| EP                   | MCAR(691.8          | EP                               | MCARP             | EP1            |
| HEM\*                | MCAR(694            | LOOK                             | MCARHP            |                |
| GEN IMPL             | MCAR(698            | GEN                              | MCARPAC           | GENIMP         |
| V-LEAD IMP           | MCAR(698.1          | VLEAD                            | MCARPAC           | VLEAD          |
| A-LEAD IMP           | MCAR(698.2          | ALEAD                            | MCARPAC           | ALEAD          |
| PACE SURV            | MCAR(698.3          | SURV                             | MCARPAC           | SURV           |
| GI\*                 | MCAR(699            | ENDO                             | MCARGP            | GI             |
| CONSULT\*            | MCAR(699.5          | EN1                              | MCARGP            | CONSULT        |
| PFT                  | MCAR(700            | DIC                              | MCPFTP            |                |
| RHEUM                | MCAR(701            | RHFULL                           | MCARP             | RHFULL1        |

\* The three procedures marked with an asterisk can be broken down further into individual procedures. As long as they are valid entry points, they will be converted.

Cardiac Surgery Risk Assessment does not have an entry in the Procedure/Subspecialty file (#697.2). It does not use the file to generate the report so you do not need to check for the entry in the file.

### Print Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Print a Status Report to view the status of the Medicine procedure results for each procedure module that you want to convert. You must have your Release Control Electronic Signature turned on to see the result statuses. If you do not have the Release Control Electronic Signature turned on, the result statuses will not show on this report. Use the Turn On Release Control/Elec. Signature option to turn on the Release Control Electronic Signature.

The following are the procedure modules that have the Turn On Release Control/Elec. Signature option:

| Procedures Module | Medicine Procedure Name          | Option Name |
|-----------------------|--------------------------------------|-----------------|
| CATH                  | Cardiac Catheterization              | MCESTONCATH     |
| ECG                   | Electrocardiogram (EKG)              | MCESTONECG      |
| ECHO                  | Echocardiogram                       | MCESTONECHO     |
| EP                    | Electrophysiology                    | MCESTONEP       |
| ETT                   | Exercise Tolerance Test              | MCESTONETT      |
| GI                    | Endoscopy/Consult                    | MCESTONGIENDO   |
| Hematology            | Hematology                           | MCESTONHEM      |
| Holter                | Holter                               | MCESTONHOLTER   |
| PFT                   | Pulmonary Function Tests             | MCESTONPFT      |
| PULM                  | Included in Endoscopy/Consult module | MCESTONPULM     |
|                       | (Also known as Pulmonary Endoscopy)  |                 |

Use the Print Status report to select which results need to be released and verified in the next step. You will need to release and verify any result that is in Draft status. You will need the following keys to view the status reports for each procedure module. If you don’t have the appropriate key for the procedure module, you will not be able to view the report. Contact IRM for key assignment.

Procedure Module User Key

Cardiology MCKEYCARD

GI MCKEYGI

PULM MCKEYPULM

PFT MCKEYPFT

Hematology MCKEYHEM

You need to decide which Medicine subspecialty types (procedure modules) you want to convert.

You can use the following options to print a status report:

Option Name Procedure Module Medicine Procedure Name

MCESSTATUSCATH CATH Cardiac Catheterization

MCESSTATUSECG ECG Electrocardiogram (EKG)

MCESSTATUSECHO ECHO Echocardiogram

MCESSTATUSEP EP Electrophysiology

MCESSTATUSETT ETT Exercise Tolerance Test

MCESSTATUSGI GI Endoscopy/Consult

MCESSTATUSHEM HEM Hematology

MCESSTATUSHOLTER Holter Holter

MCESSTATUSPFT PFT Pulmonary Function Tests

MCESSTATUSPULM PULM Included in Endoscopy/Consult module

(Also known as Pulmonary Endoscopy)

The following modules have no status and therefore do not have a Status Report option:

- Generator Implant
- A-Lead Implant
- V-Lead Implant
- Generalized Procedure/Consults
- Rheumatology
- Surgical Risk Analysis

  The GI module consists of Endoscopic, Pulmonary Endoscopic, and Non-Endoscopic procedures. The Non-Endoscopic procedures are not included in the Endoscopic Status Report. They do not have a status report.

  The procedures without a Status Report have to be converted by setting the Convert if no status field to Yes. (See Example 4 in the section “Set Up the Conversion Parameters” under the main heading *Run Conversion Test Mode*.)

  Once the results in each of the procedure modules you want to convert have been released and verified, you can print this Status Report again and use it to fill out Table 2 and select which Medicine reports you want to check on after the conversion. See 5. Select Medicine Reports for more information.

  You need to print all modules you will convert.

  For an example, here are the steps to print the Echo status report. (To print one of the other modules, choose the appropriate option from the MCMEDICINE SITE MGR MENU.)

  ================

  BEGIN EXAMPLE 1

  ================

  Select OPTION NAME: MCMEDICINE SITE MGR MENU Medicine Menu

  1 Cardiology Menu ...

  2 GI Menu ...

  3 Pulmonary Menu ...

  4 Hematology Menu ...

  5 Pacemaker Menu ...

  6 Rheumatology Menu ...

  7 Generalized Procedure Menu ...

  8 Summary of Patient Procedures

  9 Enable/Disable OE/RR

  10 Workload Reporting Management ...

  Select Medicine Menu Option: 1 Cardiology Menu

  1 Cath Lab Menu ...

  2 ECG Menu ...

  3 Echo Lab Menu ...

  4 EP Lab Menu ...

  5 Holter Lab Menu ...

  6 Exercise Tolerance Test (ETT) Menu ...

  7 Surgical Risk Analysis Menu ...

  8 Summary of Patient Procedures

  9 Problem Oriented Consult Menu ...

  10 Cardiology Management Menu ...

  Select Cardiology Menu Option: 3 Echo Lab Menu

  1 Enter/Edit Echo (Screen)

  2 Echo Test Results

  3 Line Entry/Edit of ECHO test

  4 Image Capture

  5 Brief Line Echo Entry/Edit

  6 Brief Enter/Edit Echo (Screen)

  7 Brief Echo Report

  8 Release Control Options (ECHO) ...

  Select Echo Lab Menu Option: 8 Release Control Options (ECHO)

  Release Control Options

  for Echo Lab

  1 Turn On Release Control/Elec. Signature

  2 Convert Old Records to Released Not Verified

  3 Print Superseded Reports

  4 Allow Printing of Superseded Reports

  5 Print Reports that are Marked for Deletion

  6 Status Report

  Select Release Control Options (ECHO) Option: 6 Status Report

  Select one of the following:

  1 Release

  2 Draft

  3 Both

  Which type of listing do you want see?: Both// \<RET\>

  START WITH DATE/TIME: FIRST// Select an appropriate date range.

  DEVICE: Enter an appropriate device.

  Status Report OCT 4,2004 07:51 PAGE 1

  Date/Time Patient Status

  Status

  ------------------------------------------------------------------------

  SEP 1,1989 CPPATIENT,ONE

  RELEASED OFF-LINE VERIFIED

  OCT 4,1995 10:37 CPPATIENT,TWO

  DRAFT

  NOV 6,1995 12:46 CPPATIENT,THREE

  RELEASED OFF-LINE VERIFIED

  APR 2,1996 09:30 CPPATIENT,FOUR

  DRAFT

  MAY 28,1996 12:55 CPPATIENT,FIVE

  DRAFT

  JUL 5,1996 08:30 CPPATIENT,SIX

  DRAFT

  JUL 5,1996 10:00 CPPATIENT,SEVEN

  DRAFT

  FEB 13,1997 10:30 CPPATIENT,EIGHT

  DRAFT

  AUG 14,1997 07:00 CPPATIENT,NINE

  RELEASED OFF-LINE VERIFIED

  AUG 15,1997 07:30 CPPATIENT,TEN

  DRAFT

  AUG 4,1998 14:28 CPPATIENT,ELEVEN

  RELEASED ON-LINE VERIFIED

  JAN 21,2000 11:21 CPPATIENT,TWELVE

  RELEASED OFF-LINE VERIFIED

  FEB 14,2000 11:42 CPPATIENT,THIRTEEN

  DRAFT

  MAR 31,2000 14:57 CPPATIENT,FOURTEEN

  DRAFT

  JUN 30,2000 08:30 CPPATIENT,FIFTEEN

  RELEASED OFF-LINE VERIFIED

  DEC 24,2000 15:15 CPPATIENT,SIXTEEN

  MAY 13,2001 11:08 CPPATIENT,SEVENTEEN

  DRAFT

  JUN 23,2001 15:15 CPPATIENT,SIXTEEN

  JUN 26,2001 15:15 CPPATIENT,SIXTEEN

  JUN 28,2001 10:15 CPPATIENT,SIXTEEN

  JUN 28,2001 15:15 CPPATIENT,SIXTEEN

  JUL 9,2001 10:15 CPPATIENT,SIXTEEN

  DEC 11,2001 13:06 CPPATIENT,SIXTEEN

  JUN 5,2002 17:23

  JUN 10,2002 16:42 CPPATIENT,EIGHTTEEN

  RELEASED ON-LINE VERIFIED

  SEP 27,2002 10:05 CPPATIENT,NINETEEN

  RELEASED ON-LINE VERIFIED

  APR 23,2004 14:49 CPPATIENT,TWENTY

  RELEASED ON-LINE VERIFIED

  SEP 21,2004 12:08 CPPATIENT,TWENTY-ONE

  RELEASED OFF-LINE VERIFIED

  SEP 22,2004 12:38 CPPATIENT,TWENTY-TWO

  RELEASED OFF-LINE VERIFIED

  Enter RETURN to continue or '^' to exit: \<RET\>

  Status Report statistics OCT 04, 2004 07:51:13

  ------------------------------------------------------------------------

  DRAFT: 10

  PROBLEM DRAFT: 0

  RELEASED ON-LINE VERIFIED: 4

  RELEASED OFF-LINE VERIFIED: 7

  RELEASED NOT VERIFIED: 0

  RELEASED ON-LINE VERIFIED OF SUPERSEDED: 0

  RELEASED OFF-LINE VERIFIED OF SUPERSEDED: 0

  NO STATUS/DRAFT: 8

  ----------

  29

  ================

  END EXAMPLE 1

  ================

### Release and Verify Procedure Results.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Application Coordinator (CAC) should “release and verify” all Draft results for each Medicine procedure that you plan to convert. You can use the MCMedicine Site Mgr Menu to release and verify procedure results.

If you have many records without a status, you can use the Convert Old Records to Released Not Verified option (for each procedure) in the Medicine package to convert the status of the records to Released Not Verified.

Results having the following statuses will be converted:

- Released On-Line Verified
- Released Off-Line Verified
- Released On-Line Verified of Superseded
- Released Off-Line Verified of Superseded
- Released Not Verified
- Other records with “Convert if no status” field set to Yes.

Results having the status of Draft,Problem Draft, and Superseded will be skipped during the conversion process.

================

BEGIN EXAMPLE 2

================

Select OPTION NAME: MCMEDICINE SITE MGR MENU Medicine Menu

1 Cardiology Menu ...

2 GI Menu ...

3 Pulmonary Menu ...

4 Hematology Menu ...

5 Pacemaker Menu ...

6 Rheumatology Menu ...

7 Generalized Procedure Menu ...

8 Summary of Patient Procedures

9 Enable/Disable OE/RR

10 Workload Reporting Management ...

Select Medicine Menu Option: 1 Cardiology Menu

1 Cath Lab Menu ...

2 ECG Menu ...

3 Echo Lab Menu ...

4 EP Lab Menu ...

5 Holter Lab Menu ...

6 Exercise Tolerance Test (ETT) Menu ...

7 Surgical Risk Analysis Menu ...

8 Summary of Patient Procedures

9 Problem Oriented Consult Menu ...

10 Cardiology Management Menu ...

Select Cardiology Menu Option: 3 Echo Lab Menu

1 Enter/Edit Echo (Screen)

2 Echo Test Results

3 Line Entry/Edit of ECHO test

4 Image Capture

5 Brief Line Echo Entry/Edit

6 Brief Enter/Edit Echo (Screen)

7 Brief Echo Report

8 Release Control Options (ECHO) ...

Select Echo Lab Menu Option: 1 Enter/Edit Echo (Screen)

ECHO PROCEDURES

TO ENTER A NEW PROCEDURE:

Enter the date and time when the procedure was performed.

TO EDIT AN EXISTING PROCEDURE:

Enter the patient's name, last name first, or 1st initial of the

last name and the last 4 digits of the social security number.

A partial name may be entered or a release status.

This will bring up all entries matching that part of the name.

Or you may enter the date and time when the procedure was

performed. This must be an exact match.

Or enter a ? to choose from a list of procedures.

Release Control is available. You can release the reports.

You currently have the 'MCKEYCARD' Key.

Select ECHO DATE/TIME: CPPATIENT,EIGHTEEN CPPATIENT,EIGHTEEN \*SENSITIVE\* \*SENSITIVE\* NO EMPLOYEE 9-27-2002@10:05:00 CPPATIENT,EIGHTEEN DRAFT

ECHO LABORATORY (SCREEN 1 of 4) 10/09/03

1 DATE/TIME: SEP 27,2002@10:05

2 CARDIOLOGY PATIENT: CPPATIENT,EIGHTEEN

3 ID: .......... 4 WARD/CLINIC: ..................

5 WT LBS: .... 6 HT IN: ....

7 BODY SURFACE AREA(R): .....

8 RESTING SYSTOLIC BP: .... 9 RESTING DIASTOLIC BP: ....

10 RESTING HEART RATE: ....

11 RHYTHM: .....

12 STUDY QUALITY: ....

13 SYMPTOMS(M): ..............................

14 RISK FACTORS(M): ..............................

15 MEDICATION(M): ..............................

16 STUDY TYPE(M): ....................

COMMANDS: (C)omputed, (M)ultiple, (W)ord processing, (R)ead only

^T or PF1 -- Toggle to Keypad mode ?//?? -- Field help

^C -- Display Commands (current mode) \<RET\> -- Next field

^R -- Repaint the screen \< -- Previous field

^D -- Next screen ^nn -- Go to the 'nn' field

^U -- Previous screen @ -- Delete data

^O -- Turn on/off automatic help ^ -- Quit

Enter “^” to exit this screen.

\* \* \* Release Control \* \* \*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Created on: SEP 27, 2002@10:05

DATE: SEP 27, 2002@10:05

CPPATIENT,EIGHTEEN

Current Status: DRAFT as of SEP 27, 2002@10:06

by: CPPROVIDER,THIRTY

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Do you want to change the release status? N// y YES

\* \* \* Release Control \* \* \*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Created on: SEP 27, 2002@10:05

DATE: SEP 27, 2002@10:05

CPPATIENT,EIGHTEEN

Current Status: DRAFT as of SEP 27, 2002@10:06

by: CPPROVIDER,THIRTY

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Select one of the following:

1 Draft

2 Problem Draft

3 Released On-Line Verified

4 Released Off-line Verified

5 Released not Verified

Please Select a New Status: 1// 3 Released On-Line Verified

\* \* \* Release Control \* \* \*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Created on: SEP 27, 2002@10:05

DATE: SEP 27, 2002@10:05

CPPATIENT,EIGHTEEN

Current Status: DRAFT as of SEP 27, 2002@10:06

by: CPPROVIDER,THIRTY

New status: Released On-Line Verified

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

In order to release and verify procedure results

you must type in your electronic signature code.

Enter your Current Signature Code: SIGNATURE VERIFIED

Record has been updated with new release information

================

END EXAMPLE 2

================

### Select Medicine Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to select a list of Medicine reports from the Medicine package for the procedure module that will be converted. Select one to three reports (per module) with most of the fields filled out with data. Be sure to select reports that have images and consults associated, such as ECHO reports, and reports that do not have images and consults. Print out copies of these reports and save them. After the conversion, you can compare these original copies of the Medicine reports to the new reports that will be available in CPRS.

You can use Table 2 to help you keep track of the reports that you want to convert. When the conversion is complete, you can print the new reports, compare them to these Medicine reports, and verify that the new ones are accurate.

1.  Before you run the conversion, enter the patient name, procedure, and the date/time of the procedure.
2.  After the conversion, verify that each report converted as expected.

<span id="table2" class="anchor"></span>Table 2 - List of Medicine Reports

|              |           |                     |          |
|--------------|-----------|---------------------|----------|
| Patient Name | Procedure | Procedure Date/Time | Verified |
| John Doe     | ECHO      | 10/15/2003          |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |
|              |           |                     |          |

## Run Conversion in Test Mode

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now you are ready to run the conversion in Test mode. No data will be converted while you are in Test mode. Here is a list of steps to follow. These steps must be followed in order. Step 3 is optional.

> 1\. [Set Up the Conversion Parameters](#_1._Setup_the_Conversion Parameters)

> 2\. [Enter a Hospital Location in CP Manager](#_2._Enter_Hospital_Location in CP Ma)

> 3\. [View List of TIU Titles Needed](#_3._View_List_of TIU Titles Needed)

> 4\. [View Conversion Summary Breakdown](#_3._View_Conversion_Summary Breakdow)

> 5\. [Build the Conversion List](#_4._Build_the_Conversion List)

> 6\. [Run the Conversion in Test Mode](#_2._Run_the_Conversion in Test Mode)

> 7\. [Review the Summary of Conversion Process Report](#_2._Review_the_Summary Conversion Re)

> 8\. [Fix Medicine Reports](#fix-medicine-reports)

> 9\. Repeat steps 1 through 7 until you are satisfied with the results and are ready to move to real mode.

> 10\. [Run Disk Space Requirements Option](#_5._Run_Disk_Space Requirements opti)

### Set Up the Conversion Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can convert some procedure modules now, and then go through this process again at a later time to convert other procedure modules. You must set the conversion parameter of at least one procedure module to Yes before you can run the conversion. Do so using the Conversion Setup option. (See Example 3.)

> **NOTE:** It is strongly suggested that you run the conversion in test mode first, and then run the conversion in real mode. Records are not actually converted in test mode.

Running the conversion in test mode will calculate the size of each record so you can determine how large your TIU global has to be. See [Disk Space Requirements](#_9._Run_Disk_Space Requirements Opti) option for more information.

Running the conversion in Real mode will create the TIU documents and attach them to the appropriate CP study. The converted reports will show on the CP/Medicine tree view within the Clinical Reports of the Reports tab in CPRS.

Here are the steps to follow:

a\. Go to the Medicine to CP Conversion Manager (MDCVT MANAGER) menu, and select Conversion Setup. The following prompts will appear at the top of the edit screen:

1\. Conversion Mode: Make sure Test is selected for the Conversion Mode (Test is the default). The conversion should always be run in Test mode before running the conversion in Real mode. Running the conversion in test mode doesn’t actually convert the Medicine records. (See Overview of the Conversion Process on page 1-1.)

2\. Scratch HFS Directory: Enter the Scratch HFS Directory name. Clinical Procedures uses the Host File Server (HFS) functionality in the VA Kernel to create reports. VistA broker processes require full read, write, and delete access to this directory. (Check with IRM about this directory.) If this directory is not filled in, CP tries to use the broker environment directory.

3\. Administrative Closure User: Enter the name of a person who has administrative closure permissions in the Administrative Closure User field. You need to assign someone to be the Administrative Closure person, such as the IRM chief or Chief of Staff. (This person will appear as the Administrative Closure person for each report that is converted.)

b\. Next, for each of the procedure modules listed on the Conversion Setup screen, select either Yes or No to indicate which procedure modules you want to convert. The default for each procedure module is “No.” Be sure that each procedure module that you want to convert has Convert (Yes) selected. Pulmonary reports for Pulmonary Endoscopy and Non-Endoscopic reports are under Endoscopy/Consults. If you set Endoscopy/Consult to “Yes”, the conversion will include Pulmonary Endoscopy and Non-Endoscopic reports with Endoscopy reports.

> **NOTE:** The first time the Conversion Setup is run, default values are set for the fields in the Conversion Setup option.

Upon launching the Conversion Setup option \[MDCVT SETUP\] the first time, the following historical TIU titles will be mapped to the Medicine File parameter:

> <u>Medicine Package Procedures</u> <u>Historical TIU Titles</u>

> ECHO HISTORICAL ECHOCARDIOGRAM PROCEDURE

> CARDIAC CATHETERIZATION HISTORICAL CARDIAC CATHETERIZATION PROCEDURE

> ELECTROCARDIOGRAM (EKG) HISTORICAL ELECTROCARDIOGRAM PROCEDURE

> HOLTER HISTORICAL HOLTER PROCEDURE

> EXERCISE TOLERANCE TEST HISTORICAL EXERCISE TOLERANCE TEST PROCEDURE

> ELECTROPHYSIOLOGY (EP) HISTORICAL ELECTROPHYSIOLOGY PROCEDURE

> \* HEMATOLOGY

> CARDIAC SURGERY RISK ASSESSMENT HISTORICAL PRE/POST SURGERY RISK NOTE

> GENERATOR IMPLANT HISTORICAL PACEMAKER IMPLANTATION PROCEDURE

> V LEAD IMPLANT HISTORICAL PACEMAKER IMPLANTATION PROCEDURE

> A LEAD IMPLANT HISTORICAL PACEMAKER IMPLANTATION PROCEDURE

> PACEMAKER SURVEILLANCE HISTORICAL PACEMAKER IMPLANTATION PROCEDURE

> \* ENDOSCOPY/CONSULT

> \* GENERALIZED PROCEDURE/CONSULT

> PULMONARY FUNCTION TESTS HISTORICAL PULMONARY FUNCTION TEST PROCEDURE

> RHEUMATOLOGY HISTORICAL RHEUMATOLOGY PROCEDURE

> \* Denotes procedures that can be broken down further into individual procedures. They will not be mapped but left blank.

> In addition to the TIU titles being mapped, a CP Definition will be created for each procedure module except the three denoted by a ‘\*’. The CP Definition created will have the name of the Medicine procedure print name and the word “ – HIST” appended after to indicate historical procedure.

CP Procedures and TIU Note Titles needed are created except for those needed for Generalized Procedures, Endoscopy, and Hematology. The Conversion Mode will have a default of “TEST”. You will have to create TIU Note titles for procedures falling under these categories. If there is no match for the CP Procedure, leave it blank and an appropriate CP Procedure will be associated with the Medicine procedure during the conversion.

You can print out a list of titles that needs to be created for Generalized, Endoscopy, or Hematology by first setting the parameter Convert to “Yes.” Run the option List of TIU Titles Needed to print a list of titles that you need to have created in order to convert those procedures. If you do not create the titles for a procedure, that procedure will not be converted. Give the print out of the list of titles to your site’s TIU CAC and ask them to create the titles. If you do not have a TIU CAC, you can use the option Create Document Definitions under the Document Definitions (Manager) menu to create the titles. Refer to the TIU User Manual for assistance.

The following is what the Conversion Setup option looks like:

================

BEGIN EXAMPLE 3

================

> 1 Conversion Setup

> 2 Build Conversion List

> 3 Run the Conversion Process

> 4 Summary of Conversion Process

> 5 Disk Space Requirements

> 6 List of TIU Titles Needed

> 7 Conversion Totals By Status

> 8 Error Log

> 9 Conversion Lockout

> Select Medicine to CP Conversion Manager Option: 1 Conversion Setup

> Conversion Mode: TEST

> Scratch HFS Directory: SYS\$USER:\[PETI.MDCONVERSION\]

> Administrative Closure User: DEMO,CP

> Files to be converted Convert

> Medicine Package Procedure (Y/N)

> ECHO Yes

> CARDIAC CATHETERIZATION Yes

> ELECTROCARDIOGRAM (EKG) Yes

> HOLTER No

> EXERCISE TOLERANCE TEST No

> ELECTROPHYSIOLOGY (EP) Yes

> HEMATOLOGY Yes

> +CARDIAC SURGERY RISK ASSESSMENT No

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> Enter a command or '^' followed by a caption to jump to a specific field.

> COMMAND:

================

END EXAMPLE 3

================

c\. When you select Yes to convert a procedure module, a popup box is displayed. The Medicine Procedure, CP Procedure, and Use TIU Note Title fields will already be filled in.

The appropriate CP Procedure will be automatically filled in for the CP Procedure field except for the Generalized Procedures, Endoscopy, and Hematology procedure modules. For these procedure modules, leave the CP Procedure field blank and an appropriate CP Procedure will be associated with the Medicine procedure in the conversion.

================

BEGIN EXAMPLE 4

================

> ┌ Medicine Procedure Conversion Settings ────────────────────────┐

> │ │

> │ Medicine Procedure: ECHO │

> │ │

> │ CP Procedure: ECHO - HIST │

> │ Convert if no status: Yes │

> │ Use TIU Note Title: HISTORICAL ECHOCARDIOGRAM PROCEDURE │

> │ │

> └────────────────────────────────────────────────────────────────┘

================

END EXAMPLE 4

================

> The CP Procedure and UseTIU Note Title fields are both prepopulated and should not be changed.

If you want to convert a record for a procedure that does not have a status, enter Yes in the Convert if no status field (for each desired module).

> Select Close to close the popup box.

> At the Command prompt select Save, then Exit.

The appropriate TIU Note title will be automatically filled in for the Use TIU Note Title field except for the Generalized Procedures, Endoscopy, and Hematology procedure modules. You will have to create these TIU Note titles. For the rest of the procedure modules, the standardized historical TIU Note titles are exported with patch TIU\*1\*182.

If you are working with a Generalized Procedure, Endoscopy, or Hematology procedure, you must add a TIU Note Title for this procedure. This can be done by going into TIU and adding a title. The title must match the print name of the procedure in the Procedure/Subspecialty file (697.2), and have “HISTORICAL” before the procedure name and “PROCEDURE” after the procedure name. For example, “COLONOSCOPY” would become “Historical COLONOSCOPY Procedure.” You can also use the List of TIU Titles Needed option to print a list of titles you will need to create. See [View List of TIU Titles Needed](#_3._View_List_of TIU Titles Needed) option for more information. The creation of a TIU document title will be discussed in more detail under List of TIU Titles Needed.

Table 3 shows the CP procedure names and TIU note titles that will be created for the CP Procedures and TIU Note fields when the Conversion Setup option is launched for the initial time. You can use this table to mark down which procedure you have set to “Yes” to convert.

Table 3

|                                 |                      |                                |                                              |
|---------------------------------|----------------------|--------------------------------|----------------------------------------------|
| Medicine Procedure Name     | Convert (Yes/No) | CP Procedure               | TIU Note Title                           |
| ECHO                            |                      | ECHO - HIST                    | HISTORICAL ECHOCARDIOGRAM PROCEDURE          |
| CARDIAC CATHETERIZATION         |                      | CATHETERIZATION - HIST         | HISTORICAL CARDIAC CATHETERIZATION PROCEDURE |
| ELECTROCARDIOGRAM (EKG)         |                      | ELECTROCARDIOGRAM - HIST       | HISTORICAL ELECTROCARDIOGRAM PROCEDURE       |
| HOLTER                          |                      | HOLTER - HIST                  | HISTORICAL HOLTER PROCEDURE                  |
| EXERCISE TOLERANCE TEST         |                      | EXERCISE TOLERANCE TEST - HIST | HISTORICAL EXERCISE TOLERANCE TEST PROCEDURE |
| ELECTROPHYSIOLOGY (EP)          |                      | ELECTROPHYSIOLOGY - HIST       | HISTORICAL ELECTROPHYSIOLOGY PROCEDURE       |
| HEMATOLOGY                      |                      |                                |                                              |
| CARDIAC SURGERY RISK ASSESSMENT |                      | CARDIAC SURGERY RISK ASSESSMEN | HISTORICAL PRE/POST SURGERY RISK NOTE        |
| GENERATOR IMPLANT               |                      | GENERATOR IMPLANT - HIST       | HISTORICAL PACEMAKER IMPLANTATION PROCEDURE  |
| V LEAD IMPLANT                  |                      | VENTRICAL LEAD IMPLANT - HIST  | HISTORICAL PACEMAKER IMPLANTATION PROCEDURE  |
| A LEAD IMPLANT                  |                      | ATRIAL LEAD IMPLANT - HIST     | HISTORICAL PACEMAKER IMPLANTATION PROCEDURE  |
| PACEMAKER SURVEILLANCE          |                      | PACEMAKER SURVEILLANCE - HIST  | HISTORICAL PACEMAKER IMPLANTATION PROCEDURE  |
| ENDOSCOPY/CONSULT               |                      |                                |                                              |
| GENERALIZED PROCEDURE/CONSULT   |                      |                                |                                              |
| PULMONARY FUNCTION TESTS        |                      | PULMONARY FUNCTION TEST - HIST | HISTORICAL PULMONARY FUNCTION TEST PROCEDURE |
| RHEUMATOLOGY                    |                      | RHEUMATOLOGY - HIST            | HISTORICAL RHEUMATOLOGY PROCEDURE            |

### Enter Hospital Location in CP Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must enter a hospital location for the CP Procedures that was created within the Setup Conversion option. You can use just one location for all the historical CP procedures. This hospital location should be a historical location for the conversion only. It will not be used for workload reporting. Due to the fact that some of the Medicine reports may not have a CLINIC associated with them, a hospital location will be needed to create the note during the conversion. If a clinic is associated with the report, CP will use it. If no clinic is associated, CP will use the Hospital Location field under that procedure. If you do not have that field entered, you will get a “Couldn’t create the TIU document” error for the record when you run the Error Log option after you have run the conversion in Real mode. Contact your MAS CAC to assist in creating a historical hospital location. The following is an example screen capture of adding a clinic:

(Use Stop Code 674 ADMIN PAT ACTIVITIES for this clinic. If the field is not a required field, you can step past to the next field. If the field is required, enter minimum data. If the field has a default, accept the default.

Select OPTION NAME: SDBUILD Set up a Clinic

Set up a Clinic

Select CLINIC NAME: HISTORIC CLINIC

Are you adding 'HISTORIC CLINIC' as

a new HOSPITAL LOCATION? No// Y (Yes)

NAME: HISTORIC CLINIC//

ABBREVIATION: CLIN-H

CLINIC MEETS AT THIS FACILITY?: Y// YES

SERVICE: M MEDICINE

NON-COUNT CLINIC? (Y OR N): Y YES

INCLUDE ON FILE ROOM LISTS?: N NO

DIVISION: CIOFO HINES DEV// 14100

STOP CODE NUMBER: 674 ADMIN PAT ACTIVTIES (MASNONCT) 674

DEFAULT APPOINTMENT TYPE: REGULAR//

ADMINISTER INPATIENT MEDS?:

TELEPHONE:

REQUIRE X-RAY FILMS?:

REQUIRE ACTION PROFILES?: YES// YES

NO SHOW LETTER:

PRE-APPOINTMENT LETTER:

CLINIC CANCELLATION LETTER:

APPT. CANCELLATION LETTER:

ASK FOR CHECK IN/OUT TIME:

Select PROVIDER:

DEFAULT TO PC PRACTITIONER?:

Select DIAGNOSIS:

WORKLOAD VALIDATION AT CHK OUT:

ALLOWABLE CONSECUTIVE NO-SHOWS: ??

TYPE A WHOLE NUMBER BETWEEN 0 AND 999

ALLOWABLE CONSECUTIVE NO-SHOWS: 0

MAX \# DAYS FOR FUTURE BOOKING: ??

TYPE A WHOLE NUMBER BETWEEN 11 AND 999

MAX \# DAYS FOR FUTURE BOOKING: 11

HOUR CLINIC DISPLAY BEGINS:

START TIME FOR AUTO REBOOK:

MAX \# DAYS FOR AUTO-REBOOK: ??

TYPE A WHOLE NUMBER BETWEEN 1 AND 365

MAX \# DAYS FOR AUTO-REBOOK: 1

SCHEDULE ON HOLIDAYS?:

CREDIT STOP CODE:

PROHIBIT ACCESS TO CLINIC?:

PHYSICAL LOCATION:

PRINCIPAL CLINIC:

OVERBOOKS/DAY MAXIMUM: ??

ENTER THE NUMBER OF ALLOWABLE OVERBOOKS PER DAY. IF OVERBOOKS ARE NOT

ALLOWED, ENTER ZERO.

OVERBOOKS/DAY MAXIMUM: 0

Select SPECIAL INSTRUCTIONS:

LENGTH OF APP'T: ??

TYPE A WHOLE NUMBER BETWEEN 10 AND 240 -- MUST BE A MULTIPLE OF 10 OR 15

LENGTH OF APP'T: 10

VARIABLE APP'NTMENT LENGTH:

DISPLAY INCREMENTS PER HOUR: 4// 15-MIN

INCREMENTS PER HOUR INCONSISTENT WITH 10-MINUTE APPOINTMENT LENGTH??

THIS FIELD \*\*\*SHOULD NOT BE EDITED\*\*\* ONCE AVAILABILITY HAS BEEN CREATED!!

Choose from:

1 60-MIN

2 30-MIN

4 15-MIN

3 20-MIN

6 10-MIN

DISPLAY INCREMENTS PER HOUR: 4// 6 10-MIN

AVAILABILITY DATE:

Select CLINIC NAME:

Once you have a historic clinic created, you need to associate the location to CP Procedures. The following is the list of CP Procedures that were created and will need the hospital location field defined:

- ECHO – HIST
- CATHETERIZATION - HIST
- ELECTROCARDIOGRAM - HIST
- HOLTER - HIST
- EXERCISE TOLERANCE TEST – HIST
- ELECTROPHYSIOLOGY – HIST
- CARDIAC SURGERY RISK ASSESSMEN
- GENERATOR IMPLANT – HIST
- VENTRICAL LEAD IMPLANT - HIST
- ATRIAL LEAD IMPLANT - HIST
- PACEMAKER SURVEILLANCE – HIST
- PULMONARY FUNCTION TEST - HIST
- RHEUMATOLOGY - HIST

Use CP Manager to define the hospital location for the CP Procedures. The CP Procedures should be under the “Unassigned” folder of the Procedure treeview listing.

![](md-1-5-conversion-guide/002.png)

Open the “Unassigned” folder and locate a CP procedure and fill in the Hospital Location field with the historic clinic that was created. Save the record and proceed to the next CP Procedure until you have finish defining them.

![](md-1-5-conversion-guide/003.png)

### View List of TIU Titles Needed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to view the list of TIU Titles that you will need to create for Generalized Procedures, Endoscopy and Hematology procedure modules. There can be several procedures that fall into these categories so there is no way to automatically fill in the TIU Note title into the Use TIU Note Title field for these procedure modules in the Conversion Setup option.

This list is created when a procedure module is marked “Yes” to convert, and the Use TIU Note Title field is left blank. When you create the TIU Note titles listed in this report, be sure to leave them as Inactive. These TIU Note titles are only used for this conversion so there is no need to make them active for other people to use. These new historical titles must begin with “HISTORICAL” and end in “PROCEDURE” to follow the standardized historical naming convention. The titles must be created exactly as it is printed in the List of TIU Titles Needed list. The conversion program needs the name to match exactly for a match to occur between the medicine procedure and the title so the conversion can use the title for the report.

================

BEGIN EXAMPLE 5

================

1 Conversion Setup

2 Build Conversion List

3 Run the Conversion Process

4 Summary of Conversion Process

5 Disk Space Requirements

6 List of TIU Titles Needed

7 Conversion Totals By Status

8 Error Log

9 Conversion Lockout

Select Medicine to CP Conversion Manager Option: 6 List of TIU Titles Needed

Select Device: HOME// Enter appropriate device name.

19-Oct-04 7:47am L I S T O F T I U T I T L E S N E E D E D Page 1

------------------------------------------------------------------------------

PROCEDURES Titles Needed to be Created

---------- ---------------------------

COLONOSCOPY HISTORICAL COLONOSCOPY PROCEDURE

ERCP HISTORICAL ERCP PROCEDURE

LAPARASCOPY HISTORICAL LAPARASCOPY PROCEDURE

FLEX/SIG HISTORICAL FLEX/SIG PROCEDURE

NON-ENDOSCOPIC GI PROCEDURE HISTORICAL NON-ENDOSCOPIC GI

PROCEDURE

LARYNGOSCOPY HISTORICAL LARYNGOSCOPY PROCEDURE

LAVAGE HISTORICAL LAVAGE PROCEDURE

NON-ENDOSCOPIC GI PROCEDURE HISTORICAL NON-ENDOSCOPIC GI

PROCEDURE

PULMONARY ENDOSCOPY HISTORICAL PULMONARY ENDOSCOPY

PROCEDURE

GI ENDOSCOPIC HISTORICAL GI ENDOSCOPIC PROCEDURE

ENDOSCOPIC PROCEDURE HISTORICAL ENDOSCOPIC PROCEDURE

ENDOSCOPY HISTORICAL ENDOSCOPY PROCEDURE

SIG HISTORICAL SIG PROCEDURE

GI HISTORICAL GI PROCEDURE

CONSULT HISTORICAL CONSULT PROCEDURE

BRONCHOSCOPY HISTORICAL BRONCHOSCOPY PROCEDURE

EMERGENCY MEDICINE HISTORICAL EMERGENCY MEDICINE

PROCEDURE

OPHTHAMOLOGY HISTORICAL OPHTHAMOLOGY PROCEDURE

DERMATOLOGY HISTORICAL DERMATOLOGY PROCEDURE

ONCOLOGY HISTORICAL ONCOLOGY PROCEDURE

ORTHOPEDICS HISTORICAL ORTHOPEDICS PROCEDURE

AUDIOLOGY HISTORICAL AUDIOLOGY PROCEDURE

ENDOCRINOLOGY HISTORICAL ENDOCRINOLOGY PROCEDURE

NEUROLOGY HISTORICAL NEUROLOGY PROCEDURE

PSYCHIATRY HISTORICAL PSYCHIATRY PROCEDURE

EARS,NOSE, AND THROAT HISTORICAL EARS,NOSE, AND THROAT

PROCEDURE

PODIATRY HISTORICAL PODIATRY PROCEDURE

RENAL HISTORICAL RENAL PROCEDURE

UROLOGY HISTORICAL UROLOGY PROCEDURE

PHYSICAL THERAPY HISTORICAL PHYSICAL THERAPY PROCEDURE

OCCUPATIONAL THERAPY HISTORICAL OCCUPATIONAL THERAPY

PROCEDURE

RESPIRATORY THERAPY HISTORICAL RESPIRATORY THERAPY

PROCEDURE

HYDROTHERAPY HISTORICAL HYDROTHERAPY PROCEDURE

SPEECH THERAPY HISTORICAL SPEECH THERAPY PROCEDURE

OTHER MEDICAL SERVICES HISTORICAL OTHER MEDICAL SERVICES

PROCEDURE

DENTAL HISTORICAL DENTAL PROCEDURE

GENERAL MEDICINE HISTORICAL GENERAL MEDICINE PROCEDURE

================

END EXAMPLE 5

================

There can be several titles that need to be created. Review the list and mark the ones that your site uses and create the ones that your site needs. Contact your CPRS (TIU) Clinical Application Coordinator (CAC) to create the list of titles that needs to be created. If you do not have a CAC, you can follow EXAMPLE 5a to create the titles.

================

BEGIN EXAMPLE 5a

================

1\. Go into the TIU IRM Maintenance menu.

> 2\. Select Document Definitions Manager \> Create Document Definitions. A screen similar to the following is displayed. (An example of the hierarchy is shown here. On your screen, the levels under Clinical Procedures will not show):

Create Document Definitions May 22, 2006@12:46:32 Page: 1 of 1

BASICS

Name Type

1 CLINICAL DOCUMENTS CL

2 PROGRESS NOTES CL

3 ADDENDUM DC

4 DISCHARGE SUMMARY CL

5 TIU KONNECTION DC

6 CLINICAL PROCEDURES CL

7 SURGICAL REPORTS CL

New Users, Please Enter '?NEW' for Help \>\>\>

Class/DocumentClass Next Level Detailed Display/Edit

(Title) Restart Status...

(Component) Boilerplate Text Delete

Select Action: Next Screen//

Expand the Clinical Procedures Class list.

Select Action: Next Level// Next Level

Select CLINICAL DOCUMENTS Item (Line 2-7): 6

You will see the list of Document Class under Clinical Procedures.

Create Document Definitions May 22, 2006@12:48:24 Page: 1 of 2

BASICS

Name Type

1 CLINICAL DOCUMENTS CL

2 CLINICAL PROCEDURES CL

3 CP CARDIOLOGY DC

4 CP MUSE EKG DC

5 CP OLYMPUS DC

6 CP PROCEDURES CL

7 GASTROENTEROLOGY DC

8 CP HEMODIALYSIS CL

9 HISTORICAL PROCEDURES DC

\+ ?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\>

Class/DocumentClass Next Level Detailed Display/Edit

(Title) Restart Status...

(Component) Boilerplate Text Delete

Select Action: Next Screen//

Expand to the next level of the HISTORICAL PROCEDURES Document Class.

Select Action: Next Screen// next level Next Level

Select CLINICAL PROCEDURES Item (Line 3-9): 9

You will find the historical procedure titles that were exported by patch TIU\*1\*182 here.

Create Document Definitions May 22, 2006@12:52:29 Page: 1 of 2

BASICS

\+ Name Type

2 CLINICAL PROCEDURES CL

3 HISTORICAL PROCEDURES DC

4 HISTORICAL CARDIAC CATHETERIZATION PROCEDURE TL

5 HISTORICAL ECHOCARDIOGRAM PROCEDURE TL

6 HISTORICAL ELECTROCARDIOGRAM PROCEDURE TL

7 HISTORICAL ELECTROPHYSIOLOGY PROCEDURE TL

8 HISTORICAL ENDOSCOPIC PROCEDURE TL

9 HISTORICAL EXERCISE TOLERANCE TEST PROCEDURE TL

10 HISTORICAL HEMATOLOGY PROCEDURE TL

11 HISTORICAL HOLTER PROCEDURE TL

12 HISTORICAL PACEMAKER IMPLANTATION PROCEDURE TL

13 HISTORICAL PRE/POST SURGERY RISK NOTE TL

14 HISTORICAL PULMONARY FUNCTION TEST PROCEDURE TL

\+ ?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\>

(Class/DocumentClass) Next Level Detailed Display/Edit

Title Restart Status...

(Component) Boilerplate Text Delete

Select Action: Next Screen//

Create the TIU titles within the HISTORICAL PROCEDURES Document Class.

Select Action: Next Screen// title Title

Enter the Name of a new HISTORICAL PROCEDURES: HISTORICAL LAPARASCOPY PROCEDURE

CLASS OWNER: CLINICAL COORDINATOR Replace

STATUS: (A/I/T): INACTIVE//

SEQUENCE:

MENU TEXT: Historical Laparasco Replace

Entry Created

If you wish, you may enter another HISTORICAL PROCEDURES:

You can continue to enter each title as needed. Take the default of CLINICAL COORDINATOR for the CLASS OWNER field and leave the STATUS field as INACTIVE.

==================

END OF EXAMPLE 5a

==================

The CP Procedures within Endoscopy, Generalized Procedure, and Hematology will be created during the running of the conversion process in REAL mode. The reports that have a clinic associated with them will be converted to a CP report document. The reports that do not have a clinic associated with them will display a “Couldn’t create the TIU document” error message when you run the Error Log option. Use the List of TIU Titles Needed as a guide to locate CP procedures names. The procedure names will be followed by “ - HIST”. Refer to Section 2 – [Enter Hospital Location in CPManager](#_2._Enter_Hospital_Location in CP Ma_1) to associate the hospital location field.

### View Conversion Summary Breakdown

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are 2 additional reports which are not a necessary part of the conversion process, but which may be useful in aiding you in performing the conversion process: Conversion Totals by Status and Error Log.

  
Conversion Totals by Status

This option displays the conversion totals by status. The Conversion Totals list is a cumulative list, meaning the current total is added to the existing total from a previous execution of the conversion. If reports were previously converted in Real mode, then they will display on this list even though you may have just run the conversion in Test mode.

Conversion Totals

-----------------------------------

Converted REAL Mode: 0

Converted TEST Mode: 154

Skipped: 204

Error: 82

Error Log

This option displays all records that were not converted. These records now have a status of Error. Records will not convert if they have not been released and verified, if there was a problem in creating the TIU document, or if the records had no status and the “Convert if no status” flag is not set to Yes. The site can fix any reports that are in Draft/Problem Draft status. The Draft report will need to be electronically signed in the Medicine package for it to convert. Problem Draft reports will not be able to be converted. If you received a “Couldn’t create the TIU document” error, you need to check whether there is a title created for this procedure or whether there is a hospital location associated with the CP Definition. During the conversion, the program uses the WARD CLINIC associated with the Medicine report. If no WARD CLINIC exists, you must associate a “HISTORICAL” Hospital Location for the CP Definition.

CP CONVERSION ERROR LISTING OCT 21,2004 08:44 PAGE 1

CONVERSION ID ERROR MSG

-----------------------------------------------------------------------------

STATUS: Error

18;MCAR(699.5, Report in Draft/Problem Draft status

16;MCAR(699.5, Report in Draft/Problem Draft status

14;MCAR(699.5, Report in Draft/Problem Draft status

20;MCAR(699.5, Report in Draft/Problem Draft status

52;MCAR(699.5, Report in Draft/Problem Draft status

15;MCAR(699.5, Report in Draft/Problem Draft status

13;MCAR(699.5, Report in Draft/Problem Draft status

4;MCAR(699.5, Report in Draft/Problem Draft status

42;MCAR(699.5, Report in Draft/Problem Draft status

22;MCAR(699.5, Couldn't create the TIU document

### Build the Conversion List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

a\. Run the Build Conversion List option to build the list of reports that you want to convert. Go to the Medicine to CP Conversion Manager, and select Build Conversion List.

b\. You will be asked if you want to build the list of reports to convert. Answer “Yes” if you want to build the list. Based on the procedure module(s) set to “Yes” to convert, this option will go through the Medical Patient file (#690) and built the conversion list with the procedures. When the list is built, the conversion list is stored in the CP Conversion file (#703.9). The status of each report is “Ready to Convert.” After the conversion list is built and the reports are in “Ready to Convert” status, use the Run the Conversion option to run the conversion. When the list is completely built an email message containing the following message will be sent to the person who started the option telling them the list has been built.

Subj: Conversion List \[#104593\] 10/20/04@10:34 2 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

------------------------------------------------------------------------------

The Queued Conversion List is finished.

You can run the Medicine report conversion process.

Enter message action (in IN basket): Ignore//

You can rebuild the list to check for new Medicine Reports that may have been added since the last time you ran the Build Conversion List. The initial run of the option will pick up the procedures in the Medical Patient file at the time of run. Any subsequent run of the option will only pick up any additional procedures added after the previous build. During the subsequent run, the status of the report for the new entries will be “Ready to Convert” and any existing reports from previous build will retain their existing status.Note: This option will ONLY build the entries in the Medicine procedure files that are flagged “Yes” to convert. If your site added any additional data into the Medicine package, you can re-run this option to add to the conversion list. When you are ready to convert a different procedure module, make sure you run this option before you run the conversion.

================

BEGIN EXAMPLE 6

================

> 1 Conversion Setup

> 2 Build Conversion List

> 3 Run the Conversion Process

> 4 Summary of Conversion Process

> 5 Disk Space Requirements

> 6 List of TIU Titles Needed

> 7 Conversion Totals By Status

> 8 Error Log

> 9 Conversion Lockout

Select Medicine to CP Conversion Manager Option: 2 Build Conversion List

You can rebuild the list to check for new Medicine Reports that

may have been added since the last time you ran the Build Conversion List.

Build the list of reports to convert? NO// y YES

Queue the conversion list build? YES// \<RET\>

Requested Start Time: NOW// \<RET\> (OCT 04, 2004@09:32:56)Task Queued

================

END EXAMPLE 6

================

> **NOTE:** The Build Conversion List option automatically checks for new medicine reports, so you don’t have to do anything.

### Run the Conversion in Test Mode

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Go to the Medicine to CP Conversion Manager menu, and select Run the Conversion Process. Since the conversion process can take a long time, it is recommended that you set the build to run during off hours. For example, you can start the build in the evening and let it run overnight. After this option has run, the procedure modules will be in Converted Test status.

> **NOTE:** If you get the message “No Conversion List. Run Build Conversion List option,” you need to go back and run the Build Conversion List option to build the conversion list.

================

BEGIN EXAMPLE 7

================

1 Conversion Setup

2 Build Conversion List

3 Run the Conversion Process

4 Summary of Conversion Process

5 Disk Space Requirements

6 List of TIU Titles Needed

7 Conversion Totals By Status

8 Error Log

9 Conversion Lockout

Select Medicine to CP Conversion Manager Option: 3 Run the Conversion Process

Medicine to Clinical Procedure Conversion

Running conversion in TEST mode.

Ok to continue? NO// y YES

Ready to test the conversion of the Medicine Files? NO// y YES

Conversion in progress…

\[.\] Indicates converted record

\[\*\] Indicates error in record

...........\*...\*.........\*\*...\*.\*\*...\*\*........\*.\*\*.....\*\*\*....\*\*.\*\*.\*\*..\*...\*..\*.\*\*\*\*\*..\*.\*\*.\*.\*....\*.........\*.................\*\*\*\*\*\*\*\*\*...\*\*\*\*.....\*\*\*....\*\*..\*.\*\*\*.\*\*\*\*\*\*\*\*.\*.\*\*..\*.\*\*\*\*..\*..\*................\*...\*....\*.........\*...\*\*.

Conversion Totals

-----------------------------------

Converted REAL Mode: 0

Converted TEST Mode: 154

Skipped: 204

Error: 82

================

END EXAMPLE 7

================

> **NOTE:** The conversion totals in this option only list totals by status for the current run of the conversion.

### Review the Summary of Conversion Process Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the conversion process is complete, go to the Medicine to CP Conversion Manager option and select Summary of Conversion process. The purpose of this step is to determine which reports converted and which did not.

Reports display in one of the four following status types:

- Error (includes the reason, such as Unable to Determine Status or Report in Draft/Problem Status). These reports need to be fixed if you want them to be converted. A record will have a status of Error if there was a problem creating the TIU note, or if there was a problem mapping either a procedure and/or image to the TIU note.
- Skipped – These reports were skipped and will not be converted because they were not selected to be converted in the Conversion Setup option. If you decide you want any of these reports to convert, you must go back into the Conversion Setup option and select YES next to each procedure module you want converted. Superseded records are always skipped.
- Converted Test when reports are successfully converted when running in Test Mode.
- Converted Real when reports are successfully converted when running in Real Mode.

The Summary of Conversion Report lists the Medicine record internal entry number, Medicine procedure file, the status of the conversion, and the total number of lines and bytes needed for the conversion or the error message. Here is an example of this report:

9;MCAR(691.5, Converted Test 67 lines, 2229 bytes

36;MCAR(691.5, Converted Test 65 lines, 2145 bytes

35;MCAR(691.5, Converted Test 65 lines, 2131 bytes

19;MCAR(691.5, Converted Test 65 lines, 2178 bytes

18;MCAR(691.5, Converted Test 66 lines, 2253 bytes

19;MCAR(699, Converted Test 66 lines, 2289 bytes

13;MCAR(691.5, Converted Test 71 lines, 2571 bytes

8;MCAR(691.5, Converted Test 65 lines, 2199 bytes

5;MCAR(691.5, Error Report in Draft/Problem Draft status

3;MCAR(691.5, Skipped Report type not marked for conversion

10;MCAR(699, Skipped Report type not marked for conversion

50;MCAR(691.5, Skipped Report type not marked for conversion

> **NOTE:** The summary provides a history of all modules that have been previously converted, including those that were not processed during the most recent conversion. 

### Fix Medicine Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Medicine reports that display an Error or Skipped status will not convert. If you want to fix the reports in Error status, you need to fix them in the Medicine package. Each facility must decide which reports need to be fixed and which can be ignored. To fix the Medicine reports that display an Error status do the following based on which error displays:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error</strong></th>
<th><strong>How to fix</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Report in Draft/Problem Draft status.</td>
<td>Release and verify the report.</td>
</tr>
<tr class="even">
<td>Couldn’t create the TIU document.</td>
<td><ol type="1">
<li><blockquote>
<p>Make sure the TIU title for the procedure has been created.</p>
</blockquote></li>
<li><blockquote>
<p>You may need to create a historical hospital location if the Medicine record for the procedure module does not have a Ward Location indicated. You can associate it with the CP Definition for the procedure indicated in the Conversion parameter for that procedure.</p>
</blockquote></li>
</ol></td>
</tr>
<tr class="odd">
<td>Unable to determine status.</td>
<td>Go into the Conversion Setup option and set the <strong>Convert if no status</strong> field to <strong>Yes</strong> to convert the procedure.</td>
</tr>
</tbody>
</table>

If the Medicine report displays a status of “Skipped” and you want to convert this report, select “Yes” to convert this procedure module in the Conversion Setup option.

### Repeat Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you have finished fixing the reports, you can run the conversion process again. The reports in error and skipped status will be reset automatically during the conversion. As the conversion cycle is run a subsequent time, it will attempt to convert any report that was not converted successfully the first time.

Repeat steps 1 through 7 until all the reports that you want to convert display the Converted Test status. You can continue cycling through the process until you are satisfied with the results. Then you are ready to lock out the Medicine package.

### Run Disk Space Requirements Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now you need to determine the space requirements needed for the TIU global. Run this option and give the results to your IRM so they can determine if the size of the TIU global needs to be expanded. IRM will expand the size of the TIU global if needed..Note: If you get the following message, you need to go back and run the Build Conversion List option to build the conversion list, then run the conversion in Test mode.

You must build the conversion list and run the conversion in Test mode before this option can be run

================

BEGIN EXAMPLE 8

================

No report was converted. You MUST run the Conversion in TEST or REAL mode first to be able to display the disk space requirements.

1 Conversion Setup

2 Build Conversion List

3 Run the Conversion Process

4 Summary of Conversion Process

5 Disk Space Requirements

6 List of TIU Titles Needed

7 Conversion Totals By Status

8 Error Log

9 Conversion Lockout

Select Medicine to CP Conversion Manager Option: 5 Disk Space Requirements

Summarizing...

FILE COUNT LINES BYTES

------------------------------------------------------------------------------

ECHO 4 281 10104

CARDIAC CATHETERIZATION 15 1684 47728

ELECTROCARDIOGRAM (EKG) 34 1584 57762

ENDOSCOPY/CONSULT 64 3302 103316

GENERALIZED PROCEDURE/CONSULT 47 1788 41665

PULMONARY FUNCTION TESTS 51 3295 137088

=====================================

215 11934 397663

================

END EXAMPLE 8

================

## Run the Conversion in Real Mode

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To finalize the conversion and view the reports on the CPRS tab, here is the final list of tasks:

1.  [Switch to Real Mode](#_1._Switch_to_real mode)
2.  [Run the Conversion in Real Mode](#_2._Run_the_conversion in real mode)
3.  [Verify the Reports](#verify-the-reports)
4.  [Lockout Medicine Options](#lockout-medicine-options)

> **NOTE:** After the conversion is run and before the Medicine options are locked out, you can still enter data through the Medicine package. This newly entered data will be converted the next time the conversion is run. The data previously converted will not be converted again.

### Switch to Real Mode

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Go to the Medicine to CP Conversion Manager menu, and select Conversion Setup. Select Real at the Conversion Mode field. Leave all other fields as they are. Do not make any changes to the procedure modules being converted. You do not need to build the conversion list again because you are not making changes to the procedure modules being converted.

### Run the Conversion in Real Mode

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Go to the Medicine to CP Conversion Manager menu, and select Run the Conversion Process.

================

BEGIN EXAMPLE 9

================

Select Medicine to CP Conversion Manager Option: 3 Run the conversion process

Medicine to Clinical Procedure Conversion

Running conversion in REAL mode.

Ok to continue? NO// y YES

Ready to convert the Medicine Files? NO// y YES

Conversion in progress…

\[.\] Indicates converted record

\[\*\] Indicates error in record

...........\*...\*.........\*\*...\*.\*\*...\*\*........\*.\*\*.....\*\*\*....\*\*.\*\*.\*\*..\*...\*..\*.\*\*\*\*\*..\*.\*\*.\*.\*....\*.........\*.................\*\*\*\*\*\*\*\*\*...\*\*\*\*.....\*\*\*....\*\*..\*.\*\*\*.\*\*\*\*\*\*\*\*.\*.\*\*..\*.\*\*\*\*..\*..\*................\*...\*....\*.........\*...\*\*.

Conversion Totals

-----------------------------------

Converted REAL Mode: 162

Converted TEST Mode: 0

Skipped: 204

Error: 82

================

END EXAMPLE 9

================

> **NOTE:** The conversion totals in this option only list totals by status for the current run of the conversion.

### Verify the Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Now that the conversion has been completed, you can check to make sure all your Medicine reports converted correctly. Also make sure all images associated with each of the Medicine reports are now associated with the correct TIU documents.

View the reports on the CPRS Reports tab

> a\. Logon to CPRS and verify that the new Reports tab displays appropriate reports. Most sites view their reports by selecting Procedures (local only) in the Medicine/CP folder.

> b\. To verify reports on the CPRS Reports tab locate each Medicine report on the new CPRS Reports tab and compare it with the reports you have printed out prior to the conversion, (Fig. 2-1). Use [Table 2](#table2) to make sure all reports converted successfully.

> c\. The converted reports will also be included in the following report components:

- Abnormal (if applicable)
- Brief Report
- Full Captioned
- Full Report
- Procedures

> Note: The message “CONVERTED ARCHIVED REPORT” displays in the header and footer of each report that did not have an associated status and Released Not Verified status in the Medicine package.

![Fig. 2-1

View the reports on the CPRS Consults tab](md-1-5-conversion-guide/004.png)

*Fig. 2-1

View the reports on the CPRS Consults tab*

If there is a procedure linked with the converted Medicine report, you can view the report through the Consults tab.

From the Consults tab select Action \> Consult Tracking \> Display Results. The converted TIU document is displayed (Fig. 2-2), or you can click on the TIU document under Related Documents.

![Fig. 2-2

View associated images in Imaging](md-1-5-conversion-guide/005.png)

*Fig. 2-2

View associated images in Imaging*

If there are images associated with the TIU note, view the images through Imaging Display.

a\. Launch VistA Imaging Display from the CPRS Tools pull-down menu.

b\. Click the Clinical All tab of the Imaging List screen, (Fig. 2-3).

![Fig. 2-3

c\. Double-click the historical procedure to view images associated with that procedure, (Fig. 2-4).](md-1-5-conversion-guide/006.png)

*Fig. 2-3

c\. Double-click the historical procedure to view images associated with that procedure, (Fig. 2-4).*

![Fig. 2-4

d\. Double click the abstract image in Fig. 2-5 to view the image.](md-1-5-conversion-guide/007.png)

*Fig. 2-4

d\. Double click the abstract image in Fig. 2-5 to view the image.*

![Fig. 2-5

e\. Click the Report button ![](md-1-5-conversion-guide/009.png) in Fig. 2-5 to view the TIU note associated with the procedure, (Fig. 2-6).](md-1-5-conversion-guide/008.png)

*Fig. 2-5

e\. Click the Report button ![](md-1-5-conversion-guide/009.png) in Fig. 2-5 to view the TIU note associated with the procedure, (Fig. 2-6).*

![Fig. 2-6

An alternate way to view the associated image and the TIU note through Imaging Display is through the Imaging Display Main window.](md-1-5-conversion-guide/010.png)

*Fig. 2-6

An alternate way to view the associated image and the TIU note through Imaging Display is through the Imaging Display Main window.*

a.. Select View \> Clinical Procedures to view all CP related images, (Fig. 2-7).

![Fig. 2-7

b\. Once you have selected Clinical Procedures, you will get a listing of the TIU titles in (Fig 2-8).](md-1-5-conversion-guide/011.png)

*Fig. 2-7

b\. Once you have selected Clinical Procedures, you will get a listing of the TIU titles in (Fig 2-8).*

![Fig. 2-8

c\. Double click the TIU document title, the associated abstract images will be displayed as in Fig 2-4 will be displayed.](md-1-5-conversion-guide/012.png)

*Fig. 2-8

c\. Double click the TIU document title, the associated abstract images will be displayed as in Fig 2-4 will be displayed.*

### Lockout Medicine Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you have reviewed the error log and are satisfied with the Medicine report conversion results, go to the Medicine to CP Conversion Manager menu, and select CONVERSION LOCKOUT, which locks out the MC Namespace options in Medicine. Only lockout the Medicine options for the procedure modules that you have already converted. You may also need to lock out local options that can access Medicine. At this point, you cannot use Medicine for those subspecialties that are locked out.

The following prompt displays: Are All Medicine Reports Converted? NO//

The parameter MD MEDICINE CONVERTED will be set to Yes if you respond Yes to the above prompt, or if you select All to convert all procedure modules.

================

BEGIN EXAMPLE 10

================

Select Medicine to CP Conversion Manager Option: 8 Conversion Lockout

Place the Medicine options OUT OF ORDER? NO// YES

Select one of the following:

1 CATH

2 ECG

3 ECHO

4 EP

5 HOLTER

6 ETT

7 SURGICAL RISK

8 CONSULT

9 GI

10 PULMONARY-GI

11 PFT

12 HEMATOLOGY

13 PACEMAKER

14 RHEUMATOLOGY

15 ALL

Enter response: ALL

Placing the following Medicine options OUT OF ORDER:

Enter/Edit Cath (Screen) \[MCFSCATH\]

Cath Test Results \[MCFPCATH\]

Line Entry/Edit of Cath Record \[MCFLCATH\]

Brief Line Entry/Edit of Cath Record \[MCBLCATH\]

Brief Enter/Edit Cath (Screen) \[MCBSCATH\]

Brief Cath Report \[MCBPCATH\]

Image Capture \[MCARCATHIMAGE\]

Enter/Edit ECG (Screen) \[MCFSECG\]

ECG Test Results \[MCFPECG\]

Line ECG Entry/Edit \[MCFLECG\]

Summary of Automated Records Transferred \[MCARECGAUTOSUM\]

Brief Line ECG Entry/Edit \[MCBLECG\]

Brief Enter/Edit ECG (Screen) \[MCBSECG\]

Brief ECG Report \[MCBPECG\]

Enter/Edit Echo (Screen) \[MCFSECHO\]

Echo Test Results \[MCFPECHO\]

Line Entry/Edit of ECHO test \[MCFLECHO\]

Image Capture \[MCARECHOIMAGE\]

Brief Line Echo Entry/Edit \[MCBLECHO\]

Brief Enter/Edit Echo (Screen) \[MCBSECHO\]

Brief Echo Report \[MCBPECHO\]

Enter/Edit Ep (Screen) \[MCFSEP\]

Results of EP Tests \[MCFPEP\]

EP Line Entry/Edit \[MCFLEP\]

Brief EP Line Entry/Edit \[MCBLEP\]

Brief Enter/Edit EP (Screen) \[MCBSEP\]

Brief EP Report \[MCBPEP\]

Enter/Edit Holter (Screen) \[MCFSHOLTER\]

Holter Test Results \[MCFPHOLTER\]

Line Entry/Edit of Holter \[MCFLHOLTER\]

Brief Line Entry/Edit of Holter \[MCBLHOLTER\]

Brief Enter/Edit Holter (Screen) \[MCBSHOLTER\]

Brief Holter Report \[MCBPHOLTER\]

Enter/Edit ETT (Screen) \[MCFSETT\]

ETT Results \[MCFPETT\]

Line Entry/Edit of ETT Test \[MCFLETT\]

Brief Line Entry/Edit of ETT \[MCBLETT\]

Brief Enter/Edit ETT (Screen) \[MCBSETT\]

Brief ETT Report \[MCBPETT\]

Pre-Surgery Risk Analysis Enter/Edit \[MCARCATHSRAPRE\]

Post-Surgery Risk Analysis Enter/Edit \[MCARCATHSRAPOST\]

Pre-Surgery Risk Analysis Enter/Edit(Screen) \[MCARSRAPRE\]

Post-Surgery Risk Analysis Enter/Edit(Screen) \[MCARSRAPOST\]

Surgical Risk Analysis Report \[MCARCATHSRAPRINT\]

Problem Oriented Consult Enter/Edit \[MCARGICONSULTEDIT\]

Problem Oriented Consult Enter/Edit (Screen) \[MCCONSULTSCREEN\]

Problem Oriented Consult Report \[MCARGICONSULTPRINT\]

Brief Enter/Edit of a Problem Oriented Consult \[MCARGICONSULTBRIEF\]

Brief Consult Enter/Edit (Screen) \[MCCONSULTBRSCR\]

Brief Consult Report \[MCCONSULTBRREPORT\]

Enter/Edit GI Procedure (Line) \[MCFLGI\]

Procedure Enter/Edit (Screen) \[MCFSGI\]

Endoscopic Report \[MCFPGI\]

Diagnosis Review/Revision \[MCARGIDIAG\]

Recall List \[MCARGIRECALLIST\]

Image Capture \[MCARGIMAGE\]

Brief Enter/Edit GI Procedure \[MCBLGI\]

Brief Procedure Enter/Edit (Screen) \[MCBSGI\]

Brief Endoscopic Report \[MCBPGI\]

Enter/Edit Non-Endoscopic Exams (Line) \[MCFLNONENDO\]

Enter/Edit Non-Endoscopic Exams (Screen) \[MCFSNONENDO\]

Non-Endoscopic Report \[MCFPNONENDO\]

Brief Enter/Edit of Non-Endo GI Procedure \[MCBLNONENDO\]

Brief Non-Endo Enter/Edit (Screen) \[MCBSNONENDO\]

Brief Non-Endoscopic Report \[MCBPNONENDO\]

Endoscopy Enter/Edit \[MCFLPULM\]

Endoscopy Enter/Edit (Screen) \[MCFSPULM\]

Endoscopic Report \[MCFPPULM\]

Diagnosis Review/Revision \[MCARPULMDIAG\]

Recall List \[MCARPULMRECALLIST\]

Image Capture \[MCARPULMIMAGE\]

Brief Endoscopy Enter/Edit \[MCBLPULM\]

Brief Endoscopy Enter/Edit (Screen) \[MCBSPULM\]

Brief Endoscopy Report \[MCBPPULM\]

Enter/Edit PFT \[MCFLPFT\]

Interpretation Enter/Edit \[MCFLPFTI\]

PFT Report \[MCFPPFT\]

Enter/Edit PFT (Screen) \[MCFSPFT\]

Brief PFT Enter/Edit \[MCBLPFT\]

Brief PFT Enter/Edit (Screen) \[MCBSPFT\]

Brief PFT Report \[MCBPPFT\]

Enter/Edit Hematology Procedures \[MCFLHEM\]

Enter/Edit Hematology Procedures (Screen) \[MCFSHEM\]

Hematology Report \[MCFPHEM\]

Image Capture \[MCARHEMIMAGE\]

Brief Enter/Edit of Hematology Procedures \[MCBLHEM\]

Brief Hematology Enter/Edit (Screen) \[MCBSHEM\]

Brief Hematology Report \[MCBPHEM\]

Combined Implant/Leads Enter/Edit \[MCARPACEMULTEDIT\]

Generator Implant/Explant Enter/Edit \[MCARPACEGENIMP\]

A-Lead Implant/Explant Enter/Edit \[MCFLALEAD\]

V-Lead Implant/Explant Enter/Edit \[MCFLVLEAD\]

Surveillance Enter/Edit \[MCFLSURV\]

Demographic Data Enter/Edit \[MCARPACEDIT\]

Brief Generator Implant/Explant Enter/Edit \[MCBLGENE\]

Brief A-Lead Implant/Explant Entry/Edit \[MCBLALEAD\]

Brief V-Lead Implant/Explant Enter/Edit \[MCBLVLEAD\]

Brief Surveillance Enter/Edit \[MCBLSURV\]

Combined Implant/Leads Enter/Edit \[MCFSMULTI\]

A-Lead Implant/Explant Enter/Edit \[MCFSALEAD\]

V-Lead Implant/Explant Enter/Edit \[MCFSVLEAD\]

Surveillance Enter/Edit \[MCARPACESCREENSURV\]

Demographic Data Enter/Edit \[MCARPACESCREENDEMO\]

Brief Generator Enter/Edit (Screen) \[MCBSGENI\]

Brief A-Lead Imp/Exp Enter/Edit (Screen) \[MCBSALEAD\]

Brief V-Lead Imp/Exp Enter/Edit (Screen) \[MCBSVLEAD\]

Brief Surveillance Enter/Edit (Screen) \[MCPACSURVBRSCR\]

Generator Report \[MCARPACEGENPRINT\]

A-Lead Report \[MCFPALEAD\]

V-Lead Report \[MCFPVLEAD\]

Surveillance Report \[MCARPACESURVPRINT\]

Active Patient Report \[MCARPACEPATIENT\]

Brief Generator Report \[MCBPGEN.IMPLANT\]

Brief A-Lead Report \[MCBPALEAD\]

Brief V-Lead Report \[MCBPVLEAD\]

Brief Surveillance Report \[MCPACSURVBRREPORT\]

Diagnosis Edit \[MCRHDIAGF\]

Add NEW visit/display Patient Background Info. \[MCRHBACKF\]

History Narrative Edit \[MCRHNARRF\]

Display Serial Laboratory Info. \[MCRHLABF\]

Health Assessment (HAQ) Edit \[MCRHHAQF\]

Health/Physical History Edit \[MCRHPATHISTF\]

Physical Examination Edit \[MCRHPHYSF\]

Death Admin Edit \[MCRHDEATHF\]

Diagnosis Print \[MCRHDIAGP\]

Background Information Print \[MCRHBACKP\]

History Narrative Print \[MCRHNARRP\]

Serial Laboratory Info. Print \[MCRHLABP\]

Health Assessment (HAQ) Print \[MCRHHAQP\]

Health/Physical History Print \[MCRHPATHISTP\]

Physical Examination Print \[MCRHPHYSP\]

Death Admin Print \[MCRHDEATHP\]

Print All Report \[MCRHALLP\]

Brief Rheumatology Report \[MCBPRHEUM\]

Image Capture \[MCRHIMAGE\]

Diagnosis Line Edit \[MCRHDIAGL\]

History Narrative Line Edit \[MCRHNARRL\]

Health Assessment (HAQ) Line Edit \[MCRHHAQL\]

Health/Physical History Line Edit \[MCRHPATHISTL\]

Physical Examination Line Edit \[MCRHPHYSL\]

Death Admin Line Edit \[MCRHDEATHL\]

Brief Diagnosis Line Edit \[MCRHBRIEF\]

Generalized Procedure Enter/Edit \[MCFLGEN\]

Generalized Procedure Enter/Edit (Screen) \[MCFSGEN\]

Image Capture \[MCGENERICIMAGE\]

Brief Generalized Procedure Enter/Edit \[MCBLGEN\]

Brief Generalized Procedure Enter/Edit (Screen) \[MCBSGEN\]

Summary of Patient Procedures \[MCARSUMMARY\]

================

END EXAMPLE 10

================

After being locked out the Medicine options will look similar to the following:

1 Enter/Edit Cath (Screen)

\*\*\> Out of order: Medicine Reports Converted to Clinical Procedures - OPTION OUT OF SERVICE

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access Code A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.
Action A functional process that a clinician or clerk uses in the TIU computer program. For example, “Edit” and “Search” are actions. Protocol is another name for Action.
ADP Coordinator/ADPAC/Application Coordinator Automated Data Processing Application Coordinator. The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as clinical procedures, PIMS, etc.
Application A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users.
Archive The process of moving data to some other storage medium, usually a magnetic tape, and deleting the information from active storage in order to free-up disk space on the system.
ASU Authorization/Subscription Utility, an application that allows sites to associate users with user classes, allowing them to specify the level of authorization needed to sign or order specific document types and orderables. ASU is distributed with TIU in this version; eventually it will probably become independent, to be used by many VistA packages.
Attachments Attachments are files or images stored on a network share that can be linked to the CP study. CP is able to accept data/final result report files from automated instruments. The file types that can be used as attachments are the following:
> .TXT Text files
> .RTF Rich text files
> .JPG JPEG Images
> .JPEG JPEG Images
> .BMP Bitmap Images
> .TIFF TIFF Graphics (group 3 and group 4 compressed and uncompressed types)
> .PDF Portable Document Format
> .HTML Hypertext Markup Language
> Note: .DOC (Microsoft Word files) are not supported. Be sure to convert .DOC files to .RTF or to .PDF format.
Background Processing Simultaneous running of a "job" on a computer while working on another job. Examples would be printing of a document while working on another, or the software might do automatic saves while you are working on something else.
Backup Procedures The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.
Boilerplate Text A pre-defined TIU template that can be filled in for Titles, Speeding up the entry process. TIU exports several Titles with boilerplate text which can be modified to meet specific needs; sites can also create their own.
Browse Lookup the file folder for a file that you would like to select and attach to the study. (e.g., clicking the “...” button to start a lookup).
Bulletin A canned message that is automatically sent by MailMan to a user when something happens to the database.
Business Rule Part of ASU, Business Rules authorize specific users or groups of users to perform specified actions on documents in particular statuses (e.g., an unsigned TIU note may be edited by a provider who is also the expected signer of the note).
Class Part of Document Definitions, Classes group documents. For example, “CLINICAL PROCEDURES” is a class with many kinds of Clinical Procedures notes under it. Classes may be subdivided into other Classes or Document Classes. Besides grouping documents, Classes also store behavior which is then inherited by lower level entries.
Consult Referral of a patient by the primary care physician to another hospital service/ specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion.
Contingency Plan A plan that assigns responsibility and defines procedures for use of the backup/restart/recovery and emergency preparedness procedures selected for the computer system based on risk analysis for that system.
CP Clinical Procedures.
CP Definition CP Definitions are procedures within Clinical Procedures.
CP Study A CP study is a process created to link the procedure result from the medical device or/and to link the attachments browsed from a network share to the procedure order.
CPRS Computerized Patient Record System. A comprehensive VistA program, which allows clinicians and others to enter and view orders, Progress Notes and Discharge Summaries (through a link with TIU), Problem List, view results, reports (including health summaries), etc.
Data Dictionary A description of file structure and data elements within a file.
Device A hardware input/output component of a computer system (e.g., CRT, printer).
Document Class Document Classes are categories that group documents (Titles) with similar characteristics together. For example, Cardiology notes might be a Document Class, with Echo notes, ECG notes, etc. as Titles under it. Or maybe the Document Class would be Endoscopy Notes, with Colonoscopy notes, etc. under that Document Class.
Document Definition Document Definition is a subset of TIU that provides the building blocks for TIU, by organizing the elements of documents into a hierarchy structure. This structure allows documents (Titles) to inherit characteristics (such as signature requirements and print characteristics) of the higher levels, Class and Document Class. It also allows the creation and use of boilerplate text and embedded objects.
Edit Used to change/modify data typically stored in a file.
Field A data element in a file.
File The M construct in which data is stored for retrieval at a later time. A computer record of related information.
File Manager or FileMan Within this manual, FileManager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/search related data in a file, a database.
File Server A machine where shared software is stored.
Gateway The software that performs background processing for Clinical Procedures.
Global An M term used when referring to a file stored on a storage medium, usually a magnetic disk.
GUI Graphical User Interface - a Windows-like screen that uses pull-down menus, icons, pointer devices, and other metaphor-type elements that can make a computer program more understandable, easier to use, allow multi-processing (more than one window or process available at once), etc.
Interpreter Interpreter is a user role exported with USR\*1\*19 to support the Clinical Procedures Class. The role of the Interpreter is to interpret the results of a clinical procedure. Users who are authorized to interpret the results of a clinical procedure are sent a notification when an instrument report and/or images for a CP request are available for interpretation. Business rules are used to determine what actions an interpreter can perform on a document of a specified class, but the interpreter themselves are defined by the Consults application. These individuals are ‘clinical update users’ for a given consult service.
IRMS Information Resource Management Service.
Kernel A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include: MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.
LAYGO An acronym for Learn As You Go. A technique used by VA FileMan to acquire new information as it goes about its normal procedure. It permits a user to add new data to a file.
M Formerly known as MUMPS or the Massachusetts (General Hospital) Utility Multi-Programming System. This is the programming language used to write all VistA applications.
MailMan An electronic mail, teleconferencing, and networking system.
Menu A set of options or functions available to users for editing, formatting, generating reports, etc.
Module A component of a software application that covers a single topic or a small section of a broad topic.
Namespace A naming convention followed in the VA to identify various applications and to avoid duplication. It is used as a prefix for all routines and globals used by the application.
Network Server Share A machine that is located on the network where shared files are stored.
Notebook This term refers to a GUI screen containing several tabs or pages.
OI Office of Information, formerly known as Chief Information Office Field Office, Information Resource Management Field Office, and Information Systems Center.
Option A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions.
Package Otherwise known as an application. A set of M routines, files, documentation and installation procedures that support a specific function within VistA.
Page This term refers to a tab on a GUI screen or notebook.
Password A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).
Pointer A special data type of VA FileMan that takes its value from another file. This is a method of joining files together and avoiding duplication of information.
Procedure Module Any procedure/subspecialty located in the Procedure/Subspecialty file (697.2).
Procedure Request Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/specialty without first requiring formal consultation.
Program A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
Queuing The scheduling of a process/task to occur at a later time. Queuing is normally done if a task uses up a lot of computer resources.
RAID Redundant Array of Inexpensive Drives. Imaging uses this to store images.
Real Mode Running the conversion in real mode converts a Medicine report to a text document which is then stored in a TIU document. Converted Medicine reports can be viewed though the CPRS Reports tab.
Result A consequence of an order. Refers to evaluation or status results. When you use the Complete Request (CT) action on a consult or request, you are transferred to TIU to enter the results.
\<RET\> Carriage return.
Routine A set of M commands and arguments, created, stored, and retrieved as a single unit in M.
Security Key A function which unlocks specific options and makes them accessible to an authorized user.
Sensitive Information Any information which requires a degree of protection and which should be made available only to authorized users.
Site Configurable A term used to refer to features in the system that can be modified to meet the needs of each site.
Software A generic term referring to a related set of computer programs. Generally, this refers to an operating system that enables user programs to run.
Status Symbols Codes used in order entry and Consults displays to designate the status of the order.
Task Manager or TaskMan A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.
Test Mode Running the conversion in test mode does not convert any Medicine reports. It calculates the number of lines and bytes needed for each report.
Title Titles are definitions for documents. They store the behavior of the documents which use them.
TIU Text Integration Utilities.
User A person who enters and/or retrieves data in a system, usually utilizing a CRT.
User Class User Classes are the basic components of the User Class hierarchy of ASU (Authorization/Subscription Utility) which allows sites to designate who is authorized to do what to documents or other clinical entities.
User Role User Role identifies the role of the user with respect to the document in question (e.g., Author/Dictator, Expected Signer, Expected Cosigner, Attending Physician, etc.).
Utility An M program that assists in the development and/or maintenance of a computer system.
Verify Code A unique security code which serves as a second level of security access. Use of this code is site specific; sometimes used interchangeably with a password.
VistA Veterans Health Information Systems and Technology Architecture.
Workstation A personal computer running the Windows 9x or NT operating system.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Disk Space Requirements, 2-27
Finalize the Conversion, 2-28
Fix Medicine Reports, 2-26
Glossary, 3-1
Install PackMan Message, 2-1
Lockout Medicine, 2-35
Overview of the Conversion Process, 1-1
Prepare for Conversion, 2-3
Print Status Report, 2-5
Related Manuals, 1-3
Release and Verify Procedure Results, 2-9
Review the Summary Conversion Report, 2-25
Run Conversion Setup, 2-14
Run Disk Space Requirements option, 2-27
Run the Conversion, 2-24
Run the conversion in real mode, 2-29
Select Medicine Reports, 2-13
Set up an HFS Device and Terminal Type, 2-3
Summary of Conversion Process, 2-25
Switch to real mode, 2-28
Verify Procedure/Subspecialty File, 2-4
Verify the Reports, 2-30
View Conversion Totals by Status, 2-21
View Error Log, 2-22
View List of TIU Titles Needed, 2-20
