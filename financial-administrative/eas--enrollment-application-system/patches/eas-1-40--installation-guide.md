---
title: EAS*1*40 Long Term Care Copayment Phase 4 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Long Term Care Copayment Phase 4
app_code: EAS
app_name: Enrollment Application System
section: FIN
app_status: active
pkg_ns: EAS
patch_ver: 1
patch_id: EAS*1*40
group_key: "EAS:EAS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - copayment
  - veteran
  - installation
  - copayments
  - test
  - modifies
  - care
  - patch
  - table
  - contents
page_count: 0
word_count: 1535
section_count: 1
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_p40_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/eas_1_p40_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=121"
---

![](eas-1-40-long-term-care-copayment-phase-4-installation-guide/001.png)

veterans millennium health care and benefits act

Long Term Care (LTC) Copayment Phase 4

installation guide

Patch EAS\*1\*40

November 2003

V*IST*A System Design & Development

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Preinstallation Considerations](#preinstallation-considerations)
- [Installation Instructions](#installation-instructions)
- [Sample Installation](#sample-installation)

##################### Overview

The Veterans Millennium Health Care and Benefits Act, Public Law 106-117, Sec. 101, mandates the application of copayments for veterans receiving Long Term Care (LTC) services. The LTC Copayment software is designed to work in conjunction with software currently in place for determining veteran medical and pharmacy copayment obligations and benefit eligibility based on military history, service-connected disabilities, and financial input.
Phase 1 introduced the following LTC Copayment functionality:
- Allows users to enter, edit, store and print financial information given by the veteran on VA Form 10-10EC, Application for Extended Care Services. You can download a sample form from the Long-term Care Copayments web page on the VistaU Enrollment Training Initiatives web site at REDACTED
- Allows users to designate a veteran who is exempt from the LTC copayments and the reason for the exemption
- Using the financial information entered from the VA Form 10-10EC, Application for Extended Care Services, automatically calculates and displays or prints an estimate of the LTC copayments that the veteran will be obligated to pay for the next twelve months
- Provides Integrated Billing with a veteran's copayment amount via an API
Phase 2 added the following functionality:
- Automates eligibility exemptions
- Adds the LTC Copayment Exemption Test submenu and associated user options
- Provides spend-down calculations
Phase 3 added the following new functionality
- Allows users who have the appropriate security key to delete a LTC Copayment Test (10-10EC)
Phase 3 added the following enhancements to previously existing functionality:
- Allows users who have the appropriate security key to edit the date of a LTC Copayment Test
- Allows users to add a new LTC Copayment Test for the veteran at any time, including multiple tests within the same year
- Allows users to enter burial and funeral expenses for single veterans
- Allows users to enter expenses greater than total income on the input screen for the LTC Copayment Test (10-10EC)
- Displays the veteran’s LTC copayment status and last test date when using the following Registration user options: Load/Edit Patient Data, Patient Inquiry, and Register a Patient
- If the veteran did not agree to pay the copayments display a message that indicates that the veteran is ineligible for LTC services
- Prevents the entry of a LTC Copayment Test for a patient who is not a veteran
- Corrects the display of the DECLINES TO PROVIDE FINANCIAL INFORMATION field to include both the “YES” and “NO” responses when the LTC Copayment Test is displayed
- Modifies the Calculated LTC Copayments report to correctly display the maximum copayment amounts for veterans who refuse to pay the copayment
- Corrects the determination of the LTC Copayment status when a veteran’s income is \$0. The LTC Copayment status will be EXEMPT. This change addresses NOIS MAC-1102-61792.
Phase 4 adds the following new functionality:
- Adds a new menu option, Expiring or Expired LTC Copayment Tests, to the LTC Copayments menu. It allows users to print a report listing veterans whose LTC Copayment Tests have already expired or are about to expire
Phase 4 adds the following enhancements to previously existing functionality:
- Modifies VA Form 10-10EC, Application for Extended Care
  - Adds Item 9 (Current Marital Status) to Page 1, Section III
  - Modifies Page 2, Section IV, Fixed Assets, and Section V, Liquid Assets, to provide separate columns for veteran and spouse
  - Modifies Page 2, Section V, Liquid Assets, to reduce the number of asset categories from 3 to 2
  - Modifies Page 2, Section VI, Current Gross Income of Veteran and Spouse, to reduce the number of income categories from 14 to 3
  - Modifies Page 2 to include all financial items
  - Reserves Page 3 for signatures (consent for assignment of benefits, consent and agreement to make copayments)
- Modifies the financial data screens to reflect the format changes made to the VA Form 10-10EC, Application for Extended Care paper form
- Replaces the ELIGIBILITY STATUS DATA, SCREEN \<2\> with the INSURANCE DATA, SCREEN \<5\> from the Registration options
- Modifies the Add a New LTC Copayment Test and Edit an Existing LTC Copayment Test options to enable the user to indicate that the veteran is exempt from LTC copayments (for a reason other than low income) and complete the LTC Copayment Test without having to go through all of the financial screens
- Supports the display and printing of the LTC Copayment Tests in either the old or new 10-10EC format, depending on which one is used to complete the test
- Modifies the MARITAL STATUS/DEPENDENTS, SCREEN \<3\> to allow users to indicate if a veteran is legally separated; if so, the copayments will be calculated using the rules for an unmarried veteran
- Modifies the FIXED AND LIQUID ASSETS, SCREEN \<4\> to provide separate columns for veteran and spouse, combine fields (Cash, Stocks, Mutual Funds) in Data Group 4 and provide modified help text for Data Group 5
- Modifies the CURRENT CALENDAR YEAR GROSS INCOME, SCREEN \<5\> by reducing the number of data groups from 14 to 3
- Modifies the format of the Calculated LTC Copayments report
  - Separates out Institutional and Non-institutional
  - Modifies Institutional to prompt for a LTC admission date
  - Prints 12 months of copayments starting with a user-specified month and year
  - Allows entry of a future date as the start date to see the spend down of assets

##################### Training 

Due to the complex nature of the business processes associated with the placement of veterans in LTC programs, and the sensitive nature of using financial resources to determining copayment obligations, training of VAMC staff is a paramount issue. For information about LTC Copayment training, refer to the Long-term Care Copayments web page on the VistaU Enrollment Training Initiatives web site at REDACTED

##################### Purpose

The purpose of this installation guide is to provide instructions for use by technical staff members who will be installing the LTC Copayment software.

##################### Related Manuals

The following related manuals are also being released with the LTC Copayment Phase 4 software:
|                  |                                        |                                                                                                                                     |
|------------------|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| File Name    | Manual Name                        | Description                                                                                                                     |
| EAS_1_P40_RN.PDF | LTC Copayment Phase 4 Release Notes    | Provides a high-level overview of new functionality and enhancements to previously released functionality                           |
| EAS_1_P40_UM.PDF | Updated LTC Copayment User Manual      | Provides instructions for using the LTC Copayment user menus and options                                                            |
| EAS_1_P40_TM.PDF | Updated LTC Copayment Technical Manual | Provides technical information for technical staff that are responsible for implementing and maintaining the LTC Copayment Software |

# Preinstallation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

##################### Other Software Versions Required

The following V*<span class="smallcaps">ist</span>*A package versions or higher must be installed prior to installing the LTC Copayment software:

|                                              |                              |
|----------------------------------------------|------------------------------|
| Package Name                             | Minimum Version Required |
| Income Verification Match (IVM)              | 2.0                          |
| Integrated Billing (IB)                      | 2.0                          |
| Kernel                                       | 8.0                          |
| VA FileMan                                   | 22.0                         |
| V*IST*A HL7                          | 1.6                          |
| Patient Information Management System (PIMS) | 5.3                          |

##################### Routine List

The following is a list of the routine(s) included in Patch EAS\*1\*40. The second line of each of these routine(s) will look like:

\<tab\>;;1.0;ENROLLMENT APPLICATION SYSTEM;\*\*\[patch list\]\*\*;Mar 15, 2001

|                  |                  |                 |                 |
|------------------|------------------|-----------------|-----------------|
| Routine Name | Before Patch | After Patch | Patch List  |
| EASEC100         | 13958032         | 14813325        | 5,7,16,40       |
| EASEC101         | 7982246          | 8588407         | 5,40            |
| EASEC103         | 11923179         | 12427624        | 5,7,40          |
| EASEC10E         | 4502587          | 4965438         | 5,40            |
| EASEC10R         | N/A              | 34216114        | 40              |
| EASECA           | 5819485          | 7389299         | 5,7,34,40       |
| EASECCAL         | 3948225          | 3328449         | 5,7,19,34,39,40 |
| EASECDD          | 13990181         | 16741946        | 5,7,34,40       |
| EASECDP3         | 4064247          | 4876909         | 5,40            |
| EASECE           | 6347897          | 6789390         | 5,7,34,40       |
| EASECEXP         | N/A              | 9514860         | 40              |
| EASECPC          | 13307404         | 4743840         | 5,7,19,24,34,40 |
| EASECPC1         | 2459140          | 12637945        | 7,24,40         |
| EASECSC2         | 10264733         | 4487312         | 5,40            |
| EASECSC4         | 3978580          | 4654832         | 5,40            |
| EASECSC5         | 5212071          | 5944536         | 5,7,40          |
| EASECSCC         | 10828685         | 11038388        | 5,7,34,40       |
| EASECSCR         | 7408977          | 7733616         | 5,40            |
| EASECSCU         | 3837036          | 3891887         | 5,7,40          |
| EASECSU3         | 2956713          | 3189826         | 5,7,40          |
| EASECU           | 3227925          | 3280276         | 5,7,34,40       |

##################### Assignment of User Options

The LTC Copayment options will need to be assigned to the users who will be entering LTC data at your facility.

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended this patch be installed outside of normal business hours to avoid any complications resulting from users on the system. Installation will take less than 5 minutes.

1.  Review your mapped set. If any of the routines listed in the ROUTINE SUMMARY section of patch EAS\*1\*40 is mapped, it should be removed from the mapped set at this time.
2.  Choose the PackMan message containing this patch and select the INSTALL/CHECK MESSAGE option on the PackMan menu.
3.  From the 'Kernel Installation & Distribution System' menu \[XPD MAIN\], select the Installation menu.
4.  From the INSTALLATION MENU, you may elect to use the following options. (When prompted for INSTALL NAME, enter EAS\*1.0\*40).
    1.  Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
    4.  Print Transport Global - This option will allow you to view the components of the KIDS build.
5.  Use the INSTALL PACKAGE(S) OPTION and select EAS\*1.0\*40.
6.  The install will ask if you wish to rebuild menu trees. It is recommended that you answer NO to this prompt. The trees will be rebuilt the next time the system does this task.
7.  When prompted “Want KIDS to INHIBIT Logon's during the install? YES//”, it is recommended you answer NO.
8.  When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//”, respond YES. When prompted to select the options you would like to place out of order, enter the following:

> EASEC LTC COPAY MENU LTC Copayments Menu

> EASEC LTC COPAY PRINT Calculated LTC Copayments Print

> EASEC LTC COPAY TEST ADD Add a New LTC Copayment Test

> EASEC LTC COPAY TEST EDIT Edit an Existing LTC Copayment Test

> EASEC LTC COPAY TEST PRINT Print Application for Extended Care (10-

> 10EC)

> EASEC LTC COPAY TEST VIEW View a LTC Copayment Test

9.  If routines were unmapped as part of Step 1, they should be returned to the mapped set once the installation has run to completion.

# Sample Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a copy of the entry in the INSTALL file after Patch EAS\*1\*40 was installed in a test account.

Install Started for EAS\*1.0\*40 :

Nov 17, 2003@13:03:39

Build Distribution Date: Oct 23, 2003

Installing Routines:

Nov 17, 2003@13:03:40

Installing Data Dictionaries:

Nov 17, 2003@13:03:41

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing OPTION

Nov 17, 2003@13:03:42

Updating Routine file...

EAS\*1.0\*40

────────────────────────────────────────────────────────────────

The following Routines were created during this install:

DGMTXX1

DGMTXX11

DGMTXX12

DGMTXX2

DGMTXX21

DGMTXX22

DGMTXX3

DGMTXX31

DGMTXX32

Updating KIDS files...

EAS\*1.0\*40 Installed.

Nov 17, 2003@13:03:43

Install Message sent \#99353

Install Completed