---
title: PFOP Version 3 Technical Manual for Site Manager
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: for Site Manager
app_code: PRPF
app_name: Integrated Patient Funds
section: FIN
app_status: active
pkg_ns: PRPF
patch_ver: 3
patch_id: PRPF*3
group_key: "PRPF:PRPF:3"
file_numbers: []
security_keys: []
menu_options: 4
description: The PFOP system is a computerized program that manages the private finances of Veterans Administration patients. The material to be stored in this system is the same information you’ve probably recorded on VA Form 10-1083, the Patient Account Card. Once installed, the PFOP system will accept informa
audience: 
keywords: 
  - patient
  - prpf
  - funds
  - pfop
  - table
  - contents
  - account
  - filed
  - accounts
  - balance
page_count: 0
word_count: 7031
section_count: 7
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Patient_Funds/pfop_tech.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Patient_Funds/pfop_tech.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=46"
---

![](pfop-version-3-technical-manual-for-site-manager/001.png)

Patient Funds (INTEGRATED) SystemTechnical Manual  
FORSITE MANAGERVersion 3.0February 1989  

Preface

The Personal Funds of Patients (PFOP) System automates a number of patient funds tasks - from enrolling new patient accounts, for example, to processing account transactions and printing reports about account transactions. What the system does, essentially, is electronically manage the private finances of VA hospital patients. If you are a Site Manager in a facility that uses IFCAP, you’ll soon find yourself responding to requests from Application Coordinators charged with demonstrating new patient funds work methods and technology. With your assistance and guidance, these VA medical center staff members will be able to chart a smooth transition from the manual patient funds system to the new automated system. Because your role is crucial to the successful operation of the new applications software, this technical manual introduces you to PFOP’s system design and its unique features. Within the pages of this manual, you’ll find information that will help you install and maintain the PFOP package. This manual will also help you identify, predict, and resolve any difficulties that may occur either during startup or during actual system operation.

Table of Contents

Revision History

Initiated on 12/22/04

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 34%" />
<col style="width: 26%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Description (Patch # if applic.)</td>
<td>Project Manager</td>
<td>Technical Writer</td>
</tr>
<tr class="even">
<td>12/22/04</td>
<td>Updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/22/04</td>
<td>Pdf file checked for accessibility to readers with disabilities.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>09/01/05</td>
<td>Added section: Additional File Access</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>09/22/05</td>
<td>Corrected date on title page and footers.</td>
<td></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>03/06/06</td>
<td><p>Added Note to Security Keys section.</p>
<p>Patch: PRPF*3*22</p></td>
<td>REDACTED</td>
<td>REDACTER</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Functional Description


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Functional Description](#functional-description)
- [Introduction](#introduction)
  - [OPERATING SPECIFICS](#operating-specifics)
    - [Sizing Information](#sizing-information)
    - [Translation Tables](#translation-tables)
    - [Mapped Routines](#mapped-routines)
    - [### Routine Descriptions](#routine-descriptions)
    - [Callable Routines](#callable-routines)
    - [Journaling](#journaling)
    - [Purging Data and Archiving](#purging-data-and-archiving)
    - [Internal and External Issues](#internal-and-external-issues)
    - [Site Configuration Issues](#site-configuration-issues)
  - [SECURITY ISSUES](#security-issues)
    - [DHCP Software Restrictions](#dhcp-software-restrictions)
    - [Additional File Access](#additional-file-access)
    - [Electronic Signature](#electronic-signature)
    - [Security Keys](#security-keys)
  - [ON-LINE DOCUMENTATION](#on-line-documentation)
    - [Data Dictionaries](#data-dictionaries)
    - [Input Templates](#input-templates)
  - [FILE DEFINITIONS AND KEY VARIABLES](#file-definitions-and-key-variables)
    - [Pointer Diagram](#pointer-diagram)
    - [![](pfop-version-3-technical-manual-for-site-manager/002.png) File Descriptions](#pfop-version-3-technical-manual-for-site-manager002png-file-descriptions)
    - [Package-wide Variables](#package-wide-variables)
    - [PFOP Menus](#pfop-menus)
    - [Option Descriptions](#option-descriptions)
  - [INSTALLATION GUIDE FOR VERSION 3.0](#installation-guide-for-version-30)
    - [Conversion from Manual System](#conversion-from-manual-system)
    - [Conversion from Class 3 Versions of PFOP - PF\ or PFAS\](#conversion-from-class-3-versions-of-pfop-pf-or-pfas)
  - [PFOP PACKAGE TERMS AND DEFINITIONS](#pfop-package-terms-and-definitions)
The PFOP system electronically manages money held for patients hospitalized at VA facilities. The system’s foundation is the Patient Funds account. Essentially, the Patient Funds account operates much like a checking account; however, the money in a Patient Funds account does not accrue interest and, in some cases, restrictions limit the amount of cash patients may withdraw in a given time period. While using the PFOP system, you’ll perform tasks that closely resemble the banking activities required to maintain checking accounts. Along with your supervisory duties, you’ll be called upon to perform the three basic PFOP system functions that follow.
Establish Patient Funds Account
A Patient Funds account can be opened for any individual listed in both the Patient file (# 2) and the Patient Funds file (# 470). Your facility’s Patient file stores the patient name, social security number, pertinent addresses used by the PFOP system, and any additional medical information about a patient. Your facility’s Patient Funds file stores data associated with the PFOP system (e.g., account balance, restrictions, etc.).
Post Transactions
You may electronically post deposits to Patient Funds accounts and post withdrawals from Patient Funds accounts. You will also have on-line access to the current balances of all Patient Funds accounts and to all of the transactions involving those accounts.
Reconcile Accounts and Reports
Several reports are provided that can be used to help reconcile accounts with Fiscal Service. When generating these reports, you’ll be able to select any one of several formats designed to meet the needs of a variety of users.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PFOP system is a computerized program that manages the private finances of Veterans Administration patients. The material to be stored in this system is the same information you’ve probably recorded on VA Form 10-1083, the Patient Account Card. Once installed, the PFOP system will accept information that you enter into your computer terminal, eliminating the need to record information on the form.

Using a computerized system to manage Patient Funds offers several advantages. First, the program improves efficiency and productivity by reducing unnecessary effort. You no longer have to record the same categories of information over and over again with each new transaction for the same patient. Your program also provides rigorous fiscal and accountability controls that protect Patient Funds (these controls satisfy guidelines described in MP-4, Part I; and in M-1, Part I, Chapter 8).

This package includes options used to enroll patients in the system; options used to process system transactions; and options used to print reports about system transactions. The PFOP system accepts information about only those patients who are REGISTERED WITH YOUR HOSPITAL.

Since it’s part of the Decentralized Hospital Computer Program (DHCP), the PFOP System not only operates on the same computers that manage your medical center’s Patient file, it also shares information stored in that file. Only after Medical Administration Services REGISTERS a patient -- in other words, ADMITS a patient to your hospital and ENTERS the patient into the Patient file -- will you be able to enroll the individual in the PFOP System. Now, let’s take a look at all of your system options and discover the ways in which they help simplify patient funds management.

## OPERATING SPECIFICS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Sizing Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Disk Space. An analysis of the Personal Funds of Patients (PFOP) System database at several test sites yielded information about PFOP disk requirements. The figures that follow represent an estimate of the disk space necessary for one PFOP dynamic file. Contact MAS or Fiscal to get a figure that represents the number of accounts for your facility and a figure that represents the average number of transactions for each account.

> ^PRPF(470, 2 blocks per account + 0.1 block per transaction

> (10 transactions per block)

> ^PRPF(470.1 0.2 blocks per transaction (5 transactions per block)

Equipment. Each Patient Funds Clerk should have a work station terminal. Although not required, a terminal at the Patient Funds Clerk’s window can significantly increase the productivity of PFOP personnel. One printer is adequate for the patient funds office; for ease of filing, however, the printer should be loaded with 8-1/2 inch paper and should be set to print on 16/17 pitch in compressed mode, a setting that provides a 132-column print format.

Device Qty

|                                              |     |
|----------------------------------------------|-----|
| CRT for each Patient Funds Clerk’s work area | 1   |
| CRT at the window for inquiry and posting    | 1   |
| dot matrix printer                           | 1   |

### Translation Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PFOP maintains the following two globals, which are accessed by all users:

^PRPF Global contains all Permanent data. It should be translated to all CPUs accessing patient funds data.

^PR P FT This global is used as a reader and MUST NOT be translated. It is created as needed by the system.

### Mapped Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The list that follows includes the names of PFOP routines and indicates whether the routines should be mapped when using a DSM-11 operating system.

|             |           |                                |                             |                             |
|-------------|-----------|--------------------------------|-----------------------------|-----------------------------|
| Routine | Bytes | Mapping Highly Recommended | Mapping is Not Critical | Mapping Not Recommended |
| PRPFBAL     | 3150      | \*                             |                             |                             |
| PRPFCD      | 3234      | \*                             |                             |                             |
| PRPFCDI     | 3306      | \*                             |                             |                             |
| PRPFCV\*    | 7008      |                                |                             | \*                          |
| PRPFDEF     | 1256      | \*                             |                             |                             |
| PRPF OS,    | 3206      | \*                             |                             |                             |
| PRPFDSI1    | 1972      | \*                             |                             |                             |
| PRPFDST     | 2268      | \*                             |                             |                             |
| PRPFED      | 3934      | \*                             |                             |                             |
| PRPFED1     | 1884      | \*                             |                             |                             |
| PRPFI’      | 129738    |                                |                             | \*                          |
| PRPFMIN     | 1114      |                                | \*                          |                             |
| PRPFMUL     | 3296      | \*                             |                             |                             |
| PRPFNQ      | 2768      | \*                             |                             |                             |
| PRPFOB R    | 2708      |                                | \*                          |                             |
| PRPFPNT     | 1380      |                                | \*                          |                             |
| PRPFPOST    | 4084      | \*                             |                             |                             |
| PRPFQ       | 3412      | \*                             |                             |                             |
| PRPFRES     | 1640      | \*                             |                             |                             |
| PRPFRPT     | 1400      |                                | \*                          |                             |
| PRPFS       | 1458      | \*                             |                             |                             |
| PRPFSIG     | 1456      | \*                             |                             |                             |
| PRPFSITE    | 982       | \*                             |                             |                             |
| PRPFTAT     | 1872      | \*                             |                             |                             |
| PRPFTRCK    | 2304      | \*                             |                             |                             |
| PRPFU       | 3828      | \*                             |                             |                             |
| PRPFU1      | 1218      | \*                             |                             |                             |
| PRPFYN      | 1042      | \*                             |                             |                             |

### ### Routine Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the list that follows you’ll find the names of the PFOP routines along with descriptions of each

routine’s function.

PRPFBAL This routine displays the Patient Balance Screen on a terminal. It is called by both the Check Balance and Post Transaction options.

PRPFCD This routine prints the Patient Funds Card.

PRPFCD1 Contains subroutines used by PRPFCD for printing the card.

PRPFCVT\* These routines convert the Class Ill PFOP software, versions 2.291 and higher, to this version of PFOP.

PRPFDEF This utility routine manages the deferral dates on patient funds accounts.

PRPFDMT This routine displays a single Master Transaction.

PRPFDSI This routine displays PFOP information, excluding transactions.

PRPFDSI1 This routine is a continuation routine of PRPFDSI.

PRPFDST This routine displays a range of transactions for an Individual patient.

PRPFED This routine contains the entry points for the following options:

> Long Registration

> Short Registration

> Edit Selected Patient Data

> Address Edit

> Guardian Edit

> Change Account Status

> Post Transaction

> Deferral Date Edit

> Clear Account Lock

> Add/Edit Suspense Item

> Add/Edit Patient Funds Forms File

PRPFED1 This routine contains the code for the Post Balance Carried Forward from Manual System option.

PRPFMIN This routine supports the Search for Mm/Max Restrictions option.

PRPFMUL This routine allows the user to enter Multiple Transaction Posting option.

PRPFNQ This routine supports the following options:

> Selected Card(s) -- Print

> All Cards - Print

> Overdue Restriction Search

PRPFOBR Recalculates the balances on a single account or on all accounts to verify the Integrity of the data.

PRPFPNT Contains the code to support the following print options:

> Productivity Report

> Fiscal Transaction Summary

> Daily Activity Listing

> Transaction Listing

> Balance In Accounts

> Listing of Patients

> Patient Summary Report

PRPFPOST This routine transfers the data entered into the Temporary Transaction file (Reader) into Files 470 and 470.1.

PRPFQ This is a utility routine that manages device selection and other miscellaneous utility subroutines.

PRPFRES This routine manages the restriction balances for accounts, including posting transactions that are posted in advance.

PRPFRPT This routine contains the code for the Dormant Account Listing.

PRPFS This routine contains the code to support the Suspense file.

PRPFSIG This routine allows the user to edit his or her electronic signature code. This routine is identical to the IFCAP signature code edit program.

PRPFSITE This option creates the reader file when necessary and extracts the variables from the Person (16) file to support the electronic signature code.

PRPFTAT This routine reviews and updates when necessary the account status on an Individual account or all accounts.

PRPFTRCK This routine is the input transform for the amount field of the Temporary Transaction file.

PRPFU This routine contains miscellaneous utility subroutines used throughout the program.

PRPFU1 Continuation of PRPFU.

PRPFYN This program manages all questions requiring a Y/N response similar to YN^0ICN, but with increased functionality. Program also contains an expanded wait message generator.

### Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PFOP contains no callable routines.

### Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your facility runs journaling, the ^PRPF global should be journaled. However, ^PRPFT SHOULD NOT be journaled. If you are NOT doing a daily backup, you should journal to meet the daily backup requirements of MP4, Part 1, Paragraph 3.06.h.1 -- which states:

> Those facilities using a computer system for the maintenance of Personal Funds of Patients accounts must run a daily backup disk, to be stored in a separate, secured location from the computer itself. The backup disk could be made on floppy disks, hard disks, or tape driven depending on the computer system used. This is extremely important to prevent the loss of patient funds data in case of a fire or other disaster in the location where the computer is housed. The foregoing would apply whether a facility used a microcomputer located in the patient funds office or used a terminal connected to a main computer system elsewhere in the facility.

### Purging Data and Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not supported in this release.

### Internal and External Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your system must be running KERNEL Version 5.01 and VA File Manager 17.32 in order for you to load PFOP Version 3.0. In addition, the A5A conversion routine, used to link the User file and the Person file, must have been run.

### Site Configuration Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no IFCAP site parameters to be set with PFOP.

## SECURITY ISSUES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section of your technical manual discusses PFOP package security issues, focusing on the extreme concern about potential mishandling of patient funds account transaction data. In this section you’ll find information about the use of the Electronic Signature on PFOP documents and the use of Security Keys with options.

### DHCP Software Restrictions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The same code modification prohibitions that apply to IFCAP apply as well to the Personal Funds of Patients System. Please review the security information in the notice that follows.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*NOTICE\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The PFOP package manages activities and data related to the Personal Funds of Patients. The obvious need for security is addressed throughout PFOP; this software package makes every effort to restrict the mishandling of PFOP functionality. A significant amount of testing, as well as VA Central Office review, has been conducted on the PFOP package.

The Office of Budget and Finance has requested that each facility using PFOP appreciate the sensitivity of the security issue. Moreover, each facility should adhere to the restrictions that follow.

Local modification of the program is expressly prohibited.

Modification of Class I DHCP software Data Dictionaries is restricted to adding new data elements and to creating input/output templates necessary to meet the specific needs of the local facility.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

### Additional File Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If Kernel File Access Security is activated at a site where this patch is to be loaded, all users of the Personal Funds Package must be given READ access to the following files:

File \#4 (INSTITUTION)

File \#470 (PATIENT FUNDS)

File \#470.1 (PATIENT FUNDS MASTER TRANSACTION)

File \#470.2 (PATIENT FUNDS FORMS)

File \#470.3 (PATIENT FUNDS TRANSACTION COUNTER)

File \#470.5 (PATIENT FUNDS TEMPORARY TRANSACTION)

File \#470.6 (PATIENT FUNDS REMARKS CODE)

### Electronic Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The same Electronic Signature Code used within IFCAP is used for PFOP. Electronic Signature Codes are used within PRPF to permit the posting of transactions to the account of a patient. The Electronic Signature Code is encrypted so that it is unreadable even when viewed in the User file by those with the highest level of access. A menu option exists for all users so that they can change their Electronic Signature Codes at any time.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your PFOP package requires the following security keys:

PRPF CLERK - This key should be assigned to all Patient Funds Clerks and those other personnel authorized to view the SPECIAL REMARKS fields within the patient funds account.

PRPF OVERDRAW - This key will allow the holder to overdraw the balance in a patient funds account, when necessary. This key should NOT be routinely given to all Patient Funds Clerks. System informs users that they are personally liable for any loss of funds resulting from decision to overdraw the account balance.

PRPF RECALCULATE - This key is required to recalculate and correct the 0 balances in an individual patient funds account. Assign this key to any individual authorized by the Chief of MAS to correct the balance in an account. DO NOT give this key to Patient Funds Clerks.

PRPF SUPERVISOR - This key should be allocated to PRPF users who need access to the PRPF Supervisor options.

PRPF DEFERRAL OVERRIDE - This key is used to authorize an individual to override a deferral date on an account and to disperse funds. This key DOES NOT allow an individual to overdraw the account. To ensure backward compatibility, all clerks may override a deferral if this key has NOT been assigned to anyone. If, however, even ONE person has been assigned this key, ALL persons needing to perform a deferral override will require this key. This key should be assigned to a supervisor, assistant chief, chief, or lead clerk.

> **NOTE:** The following list of security keys are used when the legacy Patient Funds application has been migrated to the new VPFS replacement package. These security keys are not required by the legacy Patient Funds package.

PRPF_ACCOUNT_OVERDRAW

This key is required by any user that will need to have the ability to overdraw an account.

PRPF_BASIC_OFFICIAL_USER

The Basic Official User is a user who requires access to patient records, but does not need privileges to post transactions.  Most similar to the existing PFOP Ward Clerk, this user only needs to review patient data.

PRPF_BASIC_PFC

The Basic Patient Funds Clerk (PFC) requires access to patient records to post transactions and print reports.  Basic PFCs have the ability to view all of the following pages in the Patient Account module, and to edit most information (as in PFOP).

PRPF_DEFERRAL_OVERRIDE

This key is required by any user that will need to have the ability to override a deferral date.

PRPF_FISCAL_MANAGEMENT

The function of Fiscal Management is to perform audits to verify that patient accounts are being properly maintained and reconciled. To this end, Fiscal Management users access VPFS on a read-only basis. They cannot create, modify, or delete patient or account information. 

PRPF_LEAD_PFC

Lead PFCs have the ability to view all pages and perform all functions in the Patient Account Module.

PRPF_PFC_SUPER

The PFC Supervisor has the ability to view all pages and perform all functions in the Patient Account Module.

PRPF_RESTRICTION_OVERRIDE

This key is required by any user that will need to have the ability to override a restricted account.

PRPF_VPFS_SECURITY_ADMIN

The VPFS Security Administrator is responsible for ensuring that data access is properly enforced in VPFS (i.e., that users see and operate on only the data and functions for which they have security access privileges). The VPFS Security Administrator has read-only privileges.

PRPF_VPFS_SYSTEM_ADMIN

The VPFS System Administrator implements authorized changes to the common reference data of VPFS.

PRPF_DATA_MIGRATION_USERS

This key is assigned to a user that will perform the migration process.

## ON-LINE DOCUMENTATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may find it wise to print the PFOP Data Dictionaries immediately after you load the PFOP software. To perform this task, use VA File Manger option number 8, List File Attributes. The PFOP files begin at number 470 and end at number 470.6. Depending on your needs, select either a Standard Dictionary or a Brief Data Dictionary.

### Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On this page and several pages that follow appear the lists of the Input, Sort, and Print Templates included with the PFOP package. Please use the FileManager print option to print out the fields being used in these templates. Using on-line documentation is the best way to obtain the most current information available.

> <u>List of PFOP System INPUT Templates</u>

> <u>Name</u> <u>File</u>

> PRPF DEFERRAL EDIT 470

> PRPF FORMS EDIT 470.2

> PRPF INACTIVE/ACTIVE 470

> PRPF LONG REGISTRATION 470

> PRPF MULTIPLE AMT 470.5

> PRPF POST TRANSACTION 470.1

> PRPF SELECTED DATA EDIT 470

> PRPF SHORT REGISTRATION 470

> PRPF SUSPENSE ENTER EDIT 470

> PRPF TEMP BCF AMTS 470.5

> PRPF TEMP MULTIPLE 470.5

> PRPF TEMP TRANS POST 470.5

> <u>List of PFOP System SORT Templates</u>

> <u>Name</u> <u>File</u>

> PRPF BALANCE IN ACCOUNTS 470

> PRPF BY PATIENT 470

> PRPF BY STATUS CHANGED 470

> PRPF CARD BY LIST/NAME 470

> PRPF DAILY ACTIVITY 470.1

> PRPF DAILY TRANSACTION SUMMARY 470.1

> PRPF DORMANT ACCOUNT UST 470

> PRPF FISCAL ACTI VITY REPORT 470.1

> PRPF FISCAL TRANS SUMMARY 470.1

> PRPF INACTIVE ACCOUNTS 470

> PRPF INDIGENT LIST 470

> PRPF LIST 470

> PRPF MIN/MAX1 470

> PRPF MIN/MAX2 470

> PRPF OUT OF BALANCE 470

> PRPF OVERDUE SORT 470

> PRPF PATIENT SUMMARY 470

> PRPF SUSPENSE DISPLAY 470

> PRPF SUSPENSE LIST 470

> <u>List of PFOP System PRINT Templates</u>

> <u>Name</u> <u>File</u>

> PRPF BALANCE IN ACCOUNTS 470

> PRPF CARD PRINT 470

> PRPF CLERK STAT HDR 470.1

> PRPF DAILY ACTIVITY 470.1

> PRPF DAILY TRANSAC11ON SUMMARY 470.1

> PRPF DORMANT ACCOUNT LIST 470

> PRPF FISCAL ACTIVITY REPORT 470.1

> PRPF FISCAL TRANS SUMMARY 470.1

> PRPF INACTIVE ACCOUNTS 470

> PRPF INDIGENT LIST 470

> PRPF MIN/MAX1 470

> PRPF MIN/MAX2 470

> PRPF NEW ACCOUNT STATUS 470

> PRPF OUT OF BALANCE 470

> PRPF OVERDUE PRINT 470

> PRPF PATIENT LIST 470

> PRPF PATIENT SUMMARY 470

> PRPF SUSPENSE DISPLAY 470

> PRPF SUSPENSE LIST 470

> PRPF TRANSACTION DISPLAY 470

## FILE DEFINITIONS AND KEY VARIABLES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pointer Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a depiction of the relationship between the Patient Funds file and its seven interacting files, see the diagram that follows.

Pointer Diagram of PFOP System Files

### ![](pfop-version-3-technical-manual-for-site-manager/002.png) File Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the list that follows, you’ll find descriptions of the Personal Funds of Patients System files and file numbers.

|                                           |                                                                                                                                                                      |
|-------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 470 PATIENT FUNDS                         | Primary file used to store patient specific information from the patient funds package.                                                                              |
| 470.1 PATIENT FUNDS MASTER TRANSACTION    | This file contains ALL transactions entered for ALL patients. The transaction field of each patient account points to this file.                                     |
| 470.2 PATIENT FUNDS FORMS                 | This file contains the list of forms used by the patient funds system.                                                                                               |
| 470.3 PATIENT FUNDS TRANSACTION COUNTER   | This file keeps track of the master transaction numbers.                                                                                                             |
| 470.5 PATIENT FUNDS TEMPORARY TRANSACTION | This READER file temporarily stores data that will later be filed in the Master Transaction file and the Patient Funds file. This file is empty in Its normal state. |
| 470.6 PATIENT FUNDS REMARKS CODE          | This file contains the list of symbols and expanded descriptions to be used to identify remarks on a card.                                                           |

### Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None in this package.

### PFOP Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Illustrations on the pages that follow are diagrams of the exported PFQP menus. The first menu is assigned to the Patient Funds Clerk. The second is assigned to the Patient Funds Supervisor. Both menus were devised to duplicate the actual positions at a facility. Please note that these are only suggested menus. Your facility has the ability to create individualized menus based on specific needs, using Menu Management. It is important that you work with the PFOP Application Coordinators when assigning the menus.

PFOP System Menu for Patient Funds Clerk

![](pfop-version-3-technical-manual-for-site-manager/003.png)

PFOP System Menu for Patient Funds Supervisor

![](pfop-version-3-technical-manual-for-site-manager/004.png)

### Option Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PFOP package employs 48 options. The option names and task descriptions appear in the list that follows.

PRPF ACTIVITY UST

*Activity (AUDIT) Listing*

This option prints a list of all transactions for a range of dates sorted by several parameters. This report allows the user to balance with the Agent Cashier if necessary by CASHICHECK and FORM TYPE.

PRPF ADDRESS EDIT

*Address Edit*

This option allows the user to edit the Patient Address fields located in File 2.

PRPF ALL CARDS

*All Cards - Print*

This option allows the user to print an account card for all accounts.

PRPF BALANCE CHECK

*Balance Check*

This option allows the user to see the balance in a patient’s account. Posting transactions to the accounts is not permitted through this option.

PRPF BALANCE IN ACCOUNTS

*Balance in Accounts*

This option prints the grand total of the accounts within the PFOP System. NO DETAIL IS PRINTED.

PRPF CARD

*Selected Card(s) - Print*

This option allows the user to print a Patient Account Card from a list of accounts selected by the user.

PRPF CHANGE ACCOUNT STATUS

*Change Account Status (ACTIVE/INACTIVE)*

This option allows the user to change the account status of an account from ACTIVE to INACTIVE or INACTIVE to ACTIVE. It will not allow the user to inactivate an account 0 when the balance of funds in the account IS NOT EQUAL to zero.

PRPF CLEAR LOCK

*Clear Account Lock*

This option allows a supervisor to clear a lock on an account. Locks are installed at the time a clerk begins to edit an account. If the option terminates abnormally -- e.g., because of power failure, line drop - the lock may not be cleared automatically and will need to be cleared using this option.

PRPF DEFERRAL DATE EDIT

*Deferral Date Edit*

This option allows a supervisor to change the deferral date on a transaction when the date is entered in error, or when the supervisor deems it appropriate to change the date. System Informs users they are personally liable for any financial loss that occurs as result of changing the deferral date.

PRPF DISPLAY/PRINT

*Card Display/Print Menu*

This menu contains the options that allow the user to print all or selected cards and that permit display of selected information or transactions for a specific patient.

PRPF DORMANT

*Dormant Account Listing*

This option searches the accounts and prints a list of all accounts that have had no activity for a period of time specified by the user. The user has the option of excluding those accounts with \$0 (ZERO) balances.

PRPF FISCAL REPORTS

*Fiscal Reports*

This menu option contains reports that Fiscal uses when balancing the accounting records with the PFOP records. CNQI~: Fiscal reports sort by the DATE OF THE

TRANSACTION rather than the DATE THE TRANSACTION was entered, as is the case with other reports.)

PRPF FISCAL ACTIVITY

*Audit Report (Fiscal - by Transaction Date)*

This option prints a report that Fiscal will use to balance with the general ledger accounts at the end of an accounting period.

PRPF FISCAL TRANS SUMMARY

*Transaction Summary (Fiscal -by Transaction Date)*

This report lists all of the transactions entered into the system for a date or a range of dates in the sequence in which the transactions occurred.

PRPF FORMS EDIT

*Add/Edit Patient Funds Forms*

This option allows the user to add or edit a form from File 470.2.

PRPF GUARDIAN EDIT

*Guardian Edit*

Within this option, the user is permitted to enter or edit Guardian Information contained in File 2.

PRPF INDIGENT PATIENT LIST

*Indigent Patient Listing*

This option prints a list of all accounts marked as INDIGENT.

PRPF INFORMATION DISPLAY

*Information Display*

This option allows the user to display all demographic information related to patient funds accounts. This data is stored in both the Patient Funds file (No. 470) and the facility’s Patient file (No. 2).

PRPF LIST OF PATIENTS

*Listing of Patients*

This option prints a list of all patients in the system.

PRPF LONG REGISTRATION

*Long Form Registration*

This option is the primary option to be used when initially registering a patient in the PFOP System.

PRPF MASTER

*Patient Funds (INTEGRATED) System*

This option is the highest level option in the PFOP System. It contains ALL the options of the system EXCEPT those options designed for queuing only.

PRPF MULTIPLE POST

*Multiple Transaction Posting*

This option allows the user to enter transactions into the PFOP System where most of the information is duplicated from transaction to transaction. The option ~reads the duplicate information into a temporary file. Individual data for each patient is entered and, when verified, is matched with the duplicate data and posted to the master file.

PRPF OUT OF BALANCE REPORT

*Out of Balance Report*

This option reviews each account and compares the computed balances for each transaction with the stored balance for the account. When a discrepancy is found, the patient account name is printed on the report for later evaluation.

PRPF OUTPUT (REPORTS)

*Output (Reports) Menu*

This option contains many of the reports generated by the system.

PRPF OVERDUE RESTRICTION

*Overdue Restriction Search*

This option generates a list of all accounts that are restricted and that indicate the date of restriction is older than 180 days.

PRPF PATIENT SUMMARY

*Patient Summary Report*

This option prints a report of all accounts listed as ACTIVE. The report contains enough information to make manual disbursements in the event of a computer failure. THIS OPTION SHOULD BE RUN AT THE END OF EACH DAY.

PRPF POST

*Post Patient Funds Transaction*

This option allows the user to enter a single transaction into a patient funds account.

PRPF POST BAL CAR FWD

*Post Balance Carried Forward from Manual System*

This option allows the user to enter the Balance Carried Forward data from a manual system. It allows entry of both Private Source and Gratuitous funds on the same transaction and verifies that the dollar amounts entered for “private” and "gratuitous” sources equal the total balance before posting.

PRPF PRODUCTIVITY REPORT

*Productivity Report*

This option allows the supervisor to print a report outlining the number of transactions posted by clerk, for a specified period.

PRPF REGISTRATION

*Add/Edit Patient Account*

This option allows the user to enter a new patient funds account or edit existing demographic information.

PRPF REMARKS CODE EDIT

*Enter/Edit Remarks Codes*

This option allows the user to enter or edit the remarks codes found in File 470.6. These codes are used as a shorthand method of entering standard phrases into the remarks field.

PRPF SEARCH FOR MINIMAX

*Search for Mm/Max Restrictions*

This option generates a report of all accounts in which the stored balance is outside of the range or ranges specified for the account.

PRPF SELECTED DATA EDIT

*Edit Selected Patient Data*

This option allows the user to edit frequently changed data in the Patient Funds file.

PRPF SHORT REGISTRATION

*Short Form Registration*

This option allows the Patient Funds Clerk to enter the minimum information necessary to register a patient.

PRPF SIGNATURE CODE EDIT

*Signature Code Edit*

This option allows a user to enter or change his or her signature code. Encryption algorithm is the same as the one used in IFCAP.

PRPF SUPERVISOR

*Supervisor Menu*

This menu contains the suggested options to be used by the supervisor of the Patient Funds Clerks.

PRPF SUSPENSE ADD

*Add/Edit Suspense Item*

This option allows the user to enter, edit, or delete a Suspense Item for a patient.

PRPF SUSPENSE DATE DELETE

*Kill Complete Suspense Date for Individual Patient*

This option allows the user to kill (delete) ALL Suspense Items for ONE patient for a date specified by the user.

PRPF SUSPENSE ITEM DELETE

*Delete Individual Suspense Item*

This option allows the Patient Funds Clerk to delete an INDIVIDUAL Suspense Item for a specific day.

PRPF SUSPENSE MASTER

*Tickler (SUSPENSE) File Menu*

This option contains all the Suspense file maintenance options for the PFOP System.

PRPF SUSPENSE REPORT

*Print Suspense Report*

This option generates a report of ALL items for ALL patients for a range of dates selected by the user.

PRPF SUSPENSE REVIEW

*Review Suspense Items for Individual Patient*

This option displays or optionally prints complete list of ALL outstanding Suspense Items for an individual patient account for a specified range of dates.

PRPF TASKMAN OUT OF BALANCE

*Out of Balance Report (TASKMAN)*

This option is designed to be a scheduled option run by TASKMAN on a weekly basis. IT

SHOULD NOT BE ASSIGNED TO A MENU. This option produces the same report as the

PRPF 01ST OF BALANCE option.

PRPF TASKMAN UPDATE STATUS

*Update Patient Status for ALL Accounts (TASKMAN)*

This option is designed to be a scheduled option run by TASKMAN on a weekly basis.

It produces the same report as the PRPF UPDATE PATIENT STATUS option of the

Supervisor Menu.

PRPF TRANSACTION DISPLAY

*Transaction Display*

This option allows the user to display transactions for a specific account. User is asked for a range of dates.

PRPF TRANSACTION LIST

*Transaction Listing*

This option prints a list of all transactions for a range of dates specified by

the user.

PRPF TRANSACTION REVIEW

*Master Transaction Review*

This option allows the user to display all Information contained within a single Master Transaction Record. Includes the amount of a transaction charged to Private Source end Gratuitous.

PRPF UPDATE STATUS (ALL)

*Update Patient Status for ALL Accounts*

This option surveys ALL accounts within the PFOP System and updates the account status (ACTIVE/INACTIVE) when necessary.

PRPF VERIFY & CORRECT

*Update Patient Status for ALL Accounts*

This option allows the supervisor to review and, when appropriate, correct the stored balances within the system. This option should not be used until a complete audit of the account is accomplished.

## INSTALLATION GUIDE FOR VERSION 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information that follows represents the procedure for installing PFOP on an integrated database computer system and is appropriate for either a test or production UCI. To install PFOP on your system, you must be running KERNEL, Version 5.01; MAILMAN, Version 3.09; and VA FILEMAN, Version 17.32 or later. In addition, you must have run the A5A conversion routine to ensure the User File (No. 3) and Person File (No. 16) are linked.

### Conversion from Manual System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you’ve been using the manual system and are about to employ the computerized system for the first time, please study the guidelines that follow and then perform the tasks described under “Site Manager Tasks” and “PFOP Personnel Tasks” on the following pages of this manual.

1\. After the Site Manager Installs package and assigns menus and keys, enter the demographic Information, using the “Long Form Registration” option. If necessary. perform this task over a period of weeks, while the manual system continues to operate.

2\. After entering all demographic Information, suspend all operations and balance the cards. If possible, perform these tasks over a weekend during overtime.

3\. Using the option entitled “Post Balance Carried Forward from Manual System”, enter the card balances onto the terminal.

4\. Run “Patient Summary Report.” Next, ensure total amount on cards equals total amount on the summary. Finally, compare each card to each individual entry on the summary.

#### Site Manager Tasks

If you are the Site Manager, you’ll need to perform four major steps to convert from a manual to a computerized system. First, please install the PRPF routines in the production UCI/Directory and then D APRPFINIT Version No.3, which was created on August 3, 1988 at Altoona, PA, by FileMan Version 17.32.

D^PRPFINIT

I AM GOING TO SET UP FOR YOU THE FOLLOWING FILES:

16 Person (Note: You already have Person file)

470 Patient Funds

470.1 Patient Funds Master Transaction

470.2 Patient Funds Forms (including data)

470.3 Patient Funds Transaction Counter

470.4 Patient Funds Future Restrictions

470.5 Patient Funds Temporary Transaction

470.6 Patient Funds Remarks Code (including data)

SHALL I WRITE OVER EXISTING DATA DEFINITIONS? NO// Y (YES)

SHALL I WRITE OVER FILE SECURITY CODES? NO// Y (YES)

> **NOTE:** THIS PACKAGE ALSO CONTAINS SORT TEMPLATES:

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF

THE SAME NAME? NO// Y (YES)

> **NOTE:** THIS PACKAGE ALSO CONTAINS INPUT TEMPLATES:

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF

THE SAME NAME? NO// Y (YES)

> **NOTE:** THIS PACKAGE ALSO CONTAINS PRINT TEMPLATES:

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF

THE SAME NAME? NO// Y (YES)

> **NOTE:** THIS PACKAGE ALSO CONTAINS SECURITY KEYS:

SHALL I WRITE OVER EXISTING SECURITY KEYS OF

THE SAME NAME? NO// Y (YES)

NOTE THIS PACKAGE ALSO CONTAINS OPTIONS:

SHALL I WRITE OVER EXISTING OPTIONS OF

THE SAME NAME? NO// Y (YES)

ARE YOU SURE EVERYTHING’S OK? Y (YES)

HMMMM, I’M WORKING AS FAST AS I CAN

PRPF ACTIVITY LIST Menu Option Filed

PRPF ADDRESS EDIT Menu Option Filed

PRPF ALL CARDS Menu Option Filed

PRPF BALANCE CHECK Menu Option Filed

PRPF BALANCE IN ACCOUNTS Menu Option Filed

PRPF CARD Menu Option Filed

PRPF CHANGE ACCOUNT STATUS Menu Option Filed

PRPF CLEAR LOCK Menu Option Filed

PRPF DEFERRAL DATE EDIT Menu Option Filed

PRPF DISPLAY/PRINT Menu Option Filed

PRPF DORMANT Menu Option Filed

PRPF FISCAL ACTIVITY Menu Option Filed

PRPF FISCAL REPORTS Menu Option Filed

PRPF FISCAL TRANS SUMMARY Menu Option Filed

PRPF FORMS EDIT Menu Option Filed

PRPF GUARDIAN EDIT Menu Option Filed

PRPF INDIGENT DISPLAY Menu Option Filed

PRPF INFORMATION DISPLAY Menu Option Filed

PRPF LIST OF PATIENTS Menu Option Filed

PRPF LONG REGISTRATION Menu Option Filed

PRPF MASTER Menu Option Filed

PRPF MULTIPLE POST Menu Option Filed

PRPF 0UT OF BALANCE REPORT Menu Option Filed

PRPF OUTPUT (REPORTS) Menu Option Filed

PRPF OVERDUE RESTRICTION Menu Option Filed

PRPF PATIENT SUMMARY Menu Option Filed

PRPF POST Menu Option Filed

PRPF POST BAL CAR FWD Menu Option Filed

PRPF PRODUCTIVITY REPORT Menu Option Filed

PRPF REGISTRATION Menu Option Filed

PRPF REMARKS CODE EDIT Menu Option Filed

PRPF SEARCH FOR MIN/MAX Menu Option Filed

PRPF SELECTED DATA EDIT Menu Option Filed

PRPF SHORT REGISTRATION Menu Option Filed

PRPF SIGNATURE CODE EDIT Menu Option Filed

PRPF SUPERVISOR Menu Option Filed

PRPF SUSPENSE ADD Menu Option Filed

PRPF SUSPENSE DATE DELETE Menu Option Filed

PRPF SUSPENSE ITEM DELETE Menu Option Filed

PRPF SUSPENSE MASTER Menu Option Filed

PRPF SUSPENSE REPORT Menu Option Filed

PRPF SUSPENSE REVIEW Menu Option Filed

PRPF TASKMAN OUT OF BALANCE Menu Option Filed

PRPF TASKMAN UPDATE STATUS Menu Option Filed

PRPF TRANSACTION DISPLAY Menu Option Filed

PRPF TRANSACTION LIST Menu Option Filed

PRPF TRANSACTION REVIEW Menu Option Filed

PRPF UPDATE STATUS (ALL) Menu Option Filed

PRPF VERIFY & CORRECT Menu Option Filed

After you’ve installed the PRPF routines and completed the D ^PRPFINIT, please assign the PRPF keys to the appropriate staff members. Next, assign the PRPF MASTER (Patient Funds System) menu to PFOP staff members. And, finally, assign the PRPF BALANCE CHECK (Balance Check) and the PRPF INFORMATION DISPLAY (Information Display) options to all of the appropriate hospital staff members.

#### PFOP Personnel Tasks

When your facility is ready to convert from a manual to a computerized system, you’ll have to perform three basic steps. To begin, log into the PFOP System and enter your Electronic Signature code. Next, using the LONG REGISTRATION option, register all patients into the PFOP System. If you have a card for a patient but the system will not let you add the patient name that's documented on the card, more than likely that particular patient has NEVER been registered in the hospital’s Patient file. MAS personnel in the admissions area will have to enter the patient into the Patient file before you can register the patient in the PFOP System. DO NOT ENTER BALANCES YET!! During the period of time it takes to register all the patients, continue using the manual system and continue posting transactions to the cards.

Finally, AFTER ALL PATIENTS HAVE BEEN REGISTERED, pick a day on which you will enter ALL the balances from the manual system into the PFOP System. Run a balance on the manual system. DO NOT PROCESS ANY TRANSACTIONS WHILE YOU ARE ENTERING THE BALANCES. Using the BALANCE CARRIED FORWARD option of the Registration menu, enter the Private Source, Gratuitous amount, and Total balance for EVERY account. When finished, print the PATIENT SUMMARY REPORT, using the Output (Reports) Menu. Compare the total from the summary report with the total from the manual system. Even If the totals from the two systems are equal, it would be beneficial to conduct a patient-by-patient comparison with manual system cards to ensure balancing transcription errors did not occur. Once you are satisfied that the balance in the new system is correct, you are ready to begin using the electronic system.

### Conversion from Class 3 Versions of PFOP - PF\* or PFAS\*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Version 3 of PFOP provides conversion programs to update the data in the Class 3 versions of PFOP. However, these programs only support conversion of the old software if the installed version number is 2.291 or higher. If you are not sure of the version that is running, you can verify the version number by logging into your system and D ^PF or D ^PFAS. Whichever program you have, it will immediately indicate the version number. If the version number is less than 2.291, you have two options: manually convert; or upgrade to 2.29 1 and then run the conversions that will be discussed below. If you need and wish to do the Intermediate conversion to 2.291, contact Charles Becker at FTS 727-7030 for the documentation and routines.

If you are running 2.291, it will be necessary to ensure that the Patient File Pointer field in File 503910 is in place for ALL accounts. During the process of entering this information that establishes a link to the Patient File, you may find that certain patients are registered in PFOP but are not In File 2. All missing patients MUST be registered by MAS. Options are available in 2.291 under the registration menu to assist in this process. If the old patient funds version is running in a separate UCI/DIRECTORY, you MUST move the old version into the production UCI/DIRECTORY before entering the Patient File Pointer information. When this process is completed, you will have upgraded the database sufficiently to run the PRPFCVT conversion routine.

If you are currently running Version 2.3 or higher, all you need to do is install the PRPF\* routines, D ^PRPFINIT, and then D ^PRPFCVT to convert the data. This data conversion is completely non-invasive. It DOES NOT affect the data in the PFAS global in any way. The conversion process updates the PRPF global with all the appropriate demographic Information contained in the old system and transfers the BALANCES. The conversion DOES NOT transfer the individual transactions. To ensure an appropriate audit trail exists, PLEASE PRINT OUT ALL THE CARDS FROM THE OLD SYSTEM so that they can be microfilmed and stored. Make sure you print the cards on 8-1/2 inch paper, using 16/17 pitch: the regional offices are unable to microfilm 14 inch paper. In addition, since there is no conflict between the old and the new systems, you may leave the routines and PFAS global on the system. Although the PF\* options should be deactivated from all menus to ensure that new data are not posted to the old system, access to the old system can be gained through the ^PFAS routine. Finally, you may find it advisable to put the PFAS\* routines and ^PFAS global on a tape for archiving purposes.

## PFOP PACKAGE TERMS AND DEFINITIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When responding to calls from Application Coordinators and other PFOP users, you’ll probably encounter many package-related terms that are unfamiliar. In the list below you’ll find all of the frequently mentioned terms that appear in the Glossary of the Patient Funds Clerk User manual and the Glossary of the Patient Funds Supervisor User manual. The definitions for these terms should prove helpful.

Fiduciary A legal entity or individual who is appointed by a court of competent jurisdiction or by the administrator and who receives VA benefits reserved for the eligible person’s use and advantage.

Gratuitous Funds With the exception of insurance, all funds that are derived from VA benefits and that are deposited in the account of a VA patient rated as Incompetent. Although the VA cannot purchase U.S. savings bonds with gratuitous funds, the patient or the patient’s representative can. When these bonds are redeemed, the proceeds (principal) are considered gratuitous funds.

Guardian A person or corporation who, following the decree of a court of competent jurisdiction, protects the person or property, or both, of a minor or mentally incompetent VA beneficiary.

Incompetent VA or court decreed classification assigned to patients who, because of mental or physical incapacity, are unable to manage their own affairs.

Institutional Award An award of disability compensation, pension, or emergency officers’ retirement pay to the Director of a VA health care facility, or to another Federal, State, or private contract facility, on behalf of a veteran rated incompetent by the VA, or adjudged incompetent by court decree, or rated incompetent by both.

Nongratuitous Funds All funds in patients’ accounts except those described as gratuitous. Interest on U.S. savings bonds purchased from gratuitous funds is also considered nongratutious.

Patients Individuals receiving hospitalization, nursing home care, and domiciliary care under VA auspices. Also individuals whose funds are managed by the VA following their release from authorized medical care.

PFOP Funds that patients or their representatives deposit in non-interest bearing accounts for safekeeping at VA health care facilities.

Restricted Accounts Patient accounts managed by the facility Director, who serves as trustee. Deposited in this type of account are personal funds that belong to the following types of patients:

> 1\. All patients adjudged incompetent by a court.

> 2\. All patients whom the VA rates as Incompetent or whom the Director considers incapable of administering their funds.

> 3\. For purposes of administration, psychiatric patients whose funds should be controlled because of their ward assignment or because an incompetency rating is pending.

> For temporary periods, Directors may designate certain “restricted” accounts as “unrestricted” and may authorize the patient concerned to use the account, within prudent limits, as an unrestricted account if such use will aid the patient’s therapeutic progress or will help to determine whether the patient has the ability to handle the funds.

Review Panel Three-member board that determines patient’s competency and reviews appeals about patient competency. Panel includes (1) the Director (except where the Director appoints a team to determine the patient’s competency) or Assistant Director; (2) the Chief of Staff; and (3) a mental health professional. Members of the treatment team for the patient being evaluated are prohibited from serving on the review panel.

Unrestricted Accounts Accounts of patients capable of handling personal funds that are deposited for safekeeping: such accounts are not subject to the trusteeship of the Director; the funds in such accounts are available for return to the patients on demand.