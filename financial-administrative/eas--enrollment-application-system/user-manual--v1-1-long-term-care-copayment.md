---
title: EAS Version 1.1 Long Term Care Copayment User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Long Term Care Copayment
app_code: EAS
app_name: Enrollment Application System
section: FIN
app_status: archive
pkg_ns: EAS
patch_ver: 1.1
patch_id: EAS*1.1
group_key: "EAS:EAS:1.1"
file_numbers: []
security_keys: []
menu_options: 1
description: "<table> <colgroup> <col style=\\"width: 31%\\" /> <col style=\\"width: 68%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th>Option Name</th> <th>Brief Description</th> </tr> </thead> <tbody> <tr class=\\"odd\\"> <td>LTC Copayments Menu</td> <td>This is the menu that contains the options for the LTC Copayments "
audience: 
keywords: 
  - test
  - copayment
  - veteran
  - copay
  - care
  - patient
  - exemption
  - date
  - table
  - income
page_count: 0
word_count: 7231
section_count: 1
table_count: 11
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: December 2019
revision_count: 27
revision_newest: 12/5/2019
revision_oldest: 4/23/02
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)_Archive/eas_1_ltc_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)_Archive/eas_1_ltc_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=254"
---

![](eas-version-1-1-long-term-care-copayment-user-manual/001.png)

veterans millennium health care and benefits act

Long Term Care (LTC) Copayment

USER Manual

December 2019

V*IST*A Health Systems Design & Development

# # Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Revision History](#revision-history)
- [# Introduction](#introduction)
    - [Public Law 106-117](#public-law-106-117)
    - [VA Regulations](#va-regulations)
- [# Using the Software](#using-the-software)
    - [Overview](#overview)
    - [Add a New LTC Copayment Test](#add-a-new-ltc-copayment-test)
    - [Edit an Existing LTC Copayment Test](#edit-an-existing-ltc-copayment-test)
    - [View a LTC Copayment Test](#view-a-ltc-copayment-test)
    - [Print Application for Extended Care (1010-EC)](#print-application-for-extended-care-1010-ec)
    - [Calculated LTC Copayments Print](#calculated-ltc-copayments-print)
    - [Delete a LTC Copayment Test (10-10EC)](#delete-a-ltc-copayment-test-10-10ec)
    - [Expiring or Expired LTC Copayment Tests](#expiring-or-expired-ltc-copayment-tests)
    - [Overview](#overview-1)
    - [Delete a LTC Copay Exemption Test](#delete-a-ltc-copay-exemption-test)
    - [Edit an Existing LTC Copay Exemption Test](#edit-an-existing-ltc-copay-exemption-test)
    - [LTC Copay Exemption Test View](#ltc-copay-exemption-test-view)
    - [View LTC Copay Exemption Test Editing](#view-ltc-copay-exemption-test-editing)
- [# Glossary](#glossary)
- [# Appendix A – LTC Copayment Data Screen Examples](#appendix-a-ltc-copayment-data-screen-examples)
- [Appendix B – LTC Copayment Calculation Scenarios](#appendix-b-ltc-copayment-calculation-scenarios)
- [Appendix C – Calculated LTC Copayments Print Option Sample Outputs](#appendix-c-calculated-ltc-copayments-print-option-sample-outputs)
- [Appendix D – Expiring or Expired LTC Copayment Tests Option Sample Outputs](#appendix-d-expiring-or-expired-ltc-copayment-tests-option-sample-outputs)
- [# Index](#index)
|            |                                                                                                                                                                                                                    |                    |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| Date   | Description                                                                                                                                                                                                    | Author         |
| 7/10/03    | Initial Phase 2 Draft Version                                                                                                                                                                                      | REDACTED           |
| 4/23/02    | Revised based on team feedback (Phase 2)                                                                                                                                                                           | REDACTED           |
| 5/30/02    | Minor revisions to finalize for release (Phase 2)                                                                                                                                                                  | REDACTED           |
| 07/10/03   | Added Delete a LTC Copay Test option (Phase 3/EAS\*1\*34)                                                                                                                                                          | REDACTED           |
| 7/22/03    | Revised to include Phase 3 software enhancements (EAS\*1\*34, DG\*5.3\*518)                                                                                                                                        | REDACTED           |
| 10/20/03   | Revised data fields in Screen 4, Appendix A (Phase 4/EAS\*1\*40)                                                                                                                                                   | REDACTED           |
| 10/20/03   | Revised data fields in Screen 5, Appendix A (Phase 4/EAS\*1\*40)                                                                                                                                                   | REDACTED           |
| 10/21/03   | Added new menu option, Expiring or Expired LTC Copayment Tests, to Using the Software section (Phase 4/EAS\*1\*40)                                                                                                 | REDACTED           |
| 10/27/03   | Updated Introduction section (Phase 4/EAS\*1\*40)                                                                                                                                                                  | REDACTED           |
| 10/28/03   | Updated references to Screen 2 from Eligibility Status Data to Insurance Data (Phase 4/EAS\*1\*40)                                                                                                                 | REDACTED           |
| 10/29/03   | Updated Screen 2 sample in Appendix A (Phase 4/EAS\*1\*40)                                                                                                                                                         | REDACTED           |
| 10/30/03   | Updated Using the Software section (Phase 4/EAS\*1\*40)                                                                                                                                                            | REDACTED           |
| 10/30/03   | Updated Using the Software section (Phase 4/EAS\*1\*40)                                                                                                                                                            | REDACTED           |
| 10/31/03   | Updated Using the Software section (Phase 4/EAS\*1\*40)                                                                                                                                                            | REDACTED           |
| 10/31/03   | Updated Using the Software section (Phase 4/EAS\*1\*40)                                                                                                                                                            | REDACTED           |
| 11/03/03   | Updated Using the Software section (Phase 4/EAS\*1\*40)                                                                                                                                                            | REDACTED           |
| 11/04/03   | Updated data screens in Appendix A                                                                                                                                                                                 | REDACTED           |
| 11/10/03   | Added Appendices C & D                                                                                                                                                                                             | REDACTED           |
| 11/10/03   | Continued with Phase 4 updates (EAS\*1\*40)                                                                                                                                                                        | REDACTED           |
| 11/12/03   | Updates based on review/feedback                                                                                                                                                                                   | REDACTED, REDACTED |
| 11/13/03   | Updates based on review/feedback                                                                                                                                                                                   | REDACTED REDACTED  |
| 9/23/04    | Updated patient-specific data in all screen examples to display fictitious data                                                                                                                                    | REDACTED           |
| 11/30/2004 | Updated to comply with standards set forth in SOP 192-352, Displaying Sensitive Data                                                                                                                               | REDACTED           |
| 2/15/2005  | 10-10EZ 3.0 Enhancements (Patch EAS\*1\*57)                                                                                                                                                                        | REDACTED           |
| 5/27/2005  | Updated Step 5 of the Edit an Existing LTC Copay Exemption Test on page 24 based on Beta testing feedback from the field (EAS\*1\*57, 1010EZ P3).                                                                  | REDACTED           |
| 12/3/2013  | Added description of screen disclaimer and revised descriptions of report disclaimers to description of Calculated LTC Copayments Print option. Added header to Calculated LTC Copayments samples. (EAS\*1.0\*105) | REDACTED           |
| 12/5/2019  | Added veteran awarded Medal of Honor to list of Veterans exempt from LTC Copayments, p. 7 (EAS\*1\*174)                                                                                                            | REDACTED           |
Table of Contents

# # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

##################### Overview

The Veterans Millennium Health Care and Benefits Act, Public Law 106-117, Sec. 101, mandates the application of copayments for veterans receiving Long Term Care (LTC) services. The LTC Copayment software is designed to work in conjunction with software currently in place for determining veteran medical and pharmacy copayment obligations and benefit eligibility based on military history, service-connected disabilities, and financial input.

Phase 1 introduced the following LTC Copayment functionality.

- Allows users to enter, edit, store and print financial information given by the veteran on VA Form 10-10EC, Application for Extended Care Services. You can download a sample form from the Long-term Care Copayments web page on the VistaU Enrollment Training Initiatives web site at REDACTED
- Allows users to designate a veteran who is exempt from the LTC copayments and the reason for the exemption
- Using the financial information entered from the VA Form 10-10EC, Application for Extended Care Services, automatically calculates and displays or prints an estimate of the LTC copayments that the veteran will be obligated to pay for the next twelve months
- Provides Integrated Billing with a veteran's copayment amount via an API

Phase 2 added the following functionality.

- Automates eligibility exemptions
- Adds the LTC Copayment Exemption Test submenu and associated user options
- Provides spend-down calculations

Phase 3 added the following new functionality.

- Allows users who have the appropriate security key to delete a LTC Copayment Test (10-10EC)

Phase 3 added the following enhancements to previously existing functionality.

- Allows users who have the appropriate security key to edit the date of a LTC Copayment Test
- Allows users to add a new LTC Copayment Test for the veteran at any time, including multiple tests within the same year
- Allows users to enter burial and funeral expenses for single veterans
- Allows users to enter expenses greater than total income on the input screen for the LTC Copayment Test (10-10EC)
- Displays the veteran’s LTC copayment status and last test date when using the following Registration user options: Load/Edit, Patient Inquiry, and Register a Patient
- If the veteran did not agree to pay the copayments display a message that indicates that the veteran is ineligible for LTC services
- Prevents the entry of a LTC Copayment Test for a patient who is not a veteran
- Corrects the display of the DECLINES TO PROVIDE FINANCIAL INFORMATION field to include both the “YES” and “NO” responses when the LTC Copayment Test is displayed
- Modifies the Calculated LTC Copayments report to correctly display the maximum copayment amounts for veterans who refuse to pay the copayment
- Corrects the determination of the LTC Copayment status when a veteran’s income is \$0. The LTC Copayment status will be EXEMPT. This change addresses NOIS MAC-1102-61792.

Phase 4 adds the following new functionality.

- Adds a new menu option, Expiring or Expired LTC Copayment Tests, to the LTC Copayments menu. It allows users to print a report listing veterans whose LTC Copayment Tests have already expired or are about to expire

Phase 4 adds the following enhancements to previously existing functionality.

- Modifies VA Form 10-10EC, Application for Extended Care
  - Adds Item 9 (Current Marital Status) to Page 1, Section III
  - Modifies Page 2, Section IV, Fixed Assets, and Section V, Liquid Assets, to provide separate columns for veteran and spouse
  - Modifies Page 2, Section V, Liquid Assets to have 2 categories of assets instead of 3
  - Modifies Page 2, Section VI, Current Gross Income of Veteran and Spouse, to have 3 categories of income instead of 14
  - Modifies Page 2 to include all financial items
  - Reserves Page 3 for signatures (consent for assignment of benefits, consent and agreement to make copayments)
- Modifies the financial data screens to reflect the format changes made to the VA Form 10-10EC, Application for Extended Care paper form
- Replaces the ELIGIBILITY STATUS DATA, SCREEN \<2\> with the INSURANCE DATA, SCREEN \<5\> from the Registration options
- Modifies the *Add a New LTC Copayment Test and Edit an Existing LTC Copayment Test* options to enable the user to indicate that the veteran is exempt from LTC copayments (for a reason other than low income) and complete the LTC Copayment Test without having to go through all of the financial screens
- Supports the display and printing of the LTC Copayment Tests in either the old or new 10-10EC format, depending on which one is used to complete the test
- Modifies the MARITAL STATUS/DEPENDENTS, SCREEN \<3\> to allow users to indicate if a veteran is legally separated; if so, the copayments will be calculated using the rules for an unmarried veteran
- Modifies the FIXED AND LIQUID ASSETS, SCREEN \<4\> to provide separate columns for veteran and spouse, combine fields in Field 4 (Cash, Stocks, Mutual Funds), and provide modified help text for Field 5 (Other Liquid Assets)
- Modifies the CURRENT CALENDAR YEAR GROSS INCOME, SCREEN \<5\> by reducing the number of data groups from fourteen (14) to three (3) and provides modified help text for the three new fields
- Modifies the format of the Calculated LTC Copayments report
  - Separates out Institutional and Non-institutional
  - Modifies Institutional to prompt for a LTC admission date
  - Prints 12 months of copayments starting with a user-specified month and year
  - Allows entry of a future date as the start date to see the spend down of assets

##################### Training

Due to the complex nature of the business processes associated with the placement of veterans in LTC programs, and the sensitive nature of using financial resources to determining copayment obligations, training of VAMC staff is a paramount issue. For information about LTC Copayment training, refer to the Long-term Care Copayments web page on the VistaU Enrollment Training Initiatives web site at REDACTED

##################### Purpose

The purpose of this user manual is to provide instructions for using the LTC Copayment menu and associated menu options, including the LTC Copayment Exemption Test submenu.

##################### References

### Public Law 106-117

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Millennium Health Care and Benefits Act provides VA with the authority and mandate to implement changes within the Veterans Health Care system. Section 101 directs the Secretary to provide LTC services, and dictates, among other things, the application of copayments as related to LTC.

### VA Regulations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

38 CFR §17.111, “Copayments for Extended Care Services”, set forth requirements regarding copayments for extended care services provided to veterans by VA (or paid for by VA) in order to meet provisions of the Veterans Millennium Health Care and Benefits Act.

#####################  Related Manuals

The following related manuals are also being released with the LTC Copayment Phase 4 software. You can download these manuals from the V*IST*A Documentation Library (VDL) web site at [http://www.va.gov/vdl/Financial_Admin.asp?Appid=121](http://www.va.gov/vdl/Financial_Admin.asp?appID=121).

|                  |                                          |                                                                                                                                     |
|------------------|------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| File Name    | Manual Name                          | Description                                                                                                                     |
| EAS_1_P40_IG.PDF | LTC Copayment Phase 4 Installation Guide | Provides detailed instructions for installing the LTC Phase 4 Copayment software.                                                   |
| EAS_1_P40_RN.PDF | LTC Copayment Phase 4 Release Notes      | Provides a high-level overview of new functionality and enhancements to previously released functionality                           |
| EAS_1_P40_TM.PDF | LTC Copayment Technical Manual           | Provides technical information for technical staff that are responsible for implementing and maintaining the LTC Copayment software |

# # Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

##################### Menu Diagram

LTC Copayments Menu (EASEC LTC COPAY MENU)

\|

\|

--------------------------------------------- Add a New LTC Copayment Test

\[EASEC LTC COPAY TEST ADD\]

--------------------------------------------- Edit an Existing LTC Copayment

Test \[EASEC LTC COPAY TEST

EDIT\]

--------------------------------------------- View a LTC Copayment Test

\[EASEC LTC COPAY TEST VIEW\]

--------------------------------------------- Print Application for Extended

Care (10-10EC) \[EASEC LTC

COPAY TEST PRINT\]

--------------------------------------------- Calculated LTC Copayments

Print \[EASEC LTC COPAY PRINT\]

--------------------------------------------- Delete a LTC Copayment Test

(10-10EC) \[EASEC LTC COPAY

TEST DELETE\]

--------------------------------------------- Expiring or Expired LTC

Copayment Tests \[EASEC LTC

COPAY TEST EXPIRE\]

----- LTC Copay Exemption Test Menu --------- Delete a LTC Copay Exemption

\[EASEC LTC EXEMPTION TEST Test \[EASEC LTC EXEMPTION TST

MENU\] DELETE\]

\|

\|---------------------------------- Edit an Existing LTC Copay

\| Exemption Test \[EASEC LTC

\| EXEMPTION TEST EDIT\]

\|

\|---------------------------------- LTC Copay Exemption Test View

\| \[EASEC LTC EXEMPTION TEST

\| VIEW\]

\|

\|---------------------------------- View LTC Copay Exemption Test

Editing \[EASEC LTC EXEMPT TST

VIEW EDIT\]

##################### Assignment of User Options

The LTC Copayment options will need to be assigned to the users who will be entering LTC data at your facility. Contact your IRM Service for assistance.

#####################  LTC Copayments Menu

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Brief Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LTC Copayments Menu</td>
<td>This is the menu that contains the options for the LTC Copayments application.</td>
</tr>
<tr class="even">
<td>Add a New LTC Copayment Test</td>
<td>This option enables you to add a new LTC Copayment Test for a patient. The information entered will be from Form 10-10EC, Application for Extended Care. If all of the required information is entered, the test can be completed, and the 10-10EC form can be printed.</td>
</tr>
<tr class="odd">
<td>Edit an Existing LTC Copayment Test</td>
<td>This option enables you to make changes to data in an existing LTC Copayment Test. If all of the required information is entered, the test can be completed, and the 10-10EC form can be printed.</td>
</tr>
<tr class="even">
<td>View a LTC Copayment Test</td>
<td>This option displays all of the screens containing the information for a selected LTC Copayment Test. It does not allow editing.</td>
</tr>
<tr class="odd">
<td>Print Application for Extended Care (1010-EC)</td>
<td>This menu option allows the selection and printing of an LTC Copayment test.</td>
</tr>
<tr class="even">
<td>Calculated LTC Copayments Print</td>
<td>This option enables you to display or print the calculated LTC copayments for a selected veteran.</td>
</tr>
<tr class="odd">
<td>LTC Copay Exemption Test Menu ...</td>
<td><p>This is a submenu of the LTC Copayments application. It contains the options pertaining to the LTC Copayment Exemption Test.</p>
<ul>
<li><p>Delete a LTC Copay Exemption Test</p></li>
<li><p>Edit an Existing LTC Copay Exemption Test</p></li>
<li><p>LTC Copay Exemption Test View</p></li>
<li><p>View LTC Copay Exemption Test Editing</p></li>
</ul>
<p>Note: There is no Add option on this menu. The LTC Copayment Exemption Test is automatically created based on the veteran’s means test.</p></td>
</tr>
<tr class="even">
<td>Delete a LTC Copayment Test (10-10EC)</td>
<td><p>This option is used to delete a Long Term Care Copayment Test (10-10EC) that may have been entered in error. You must have the DG MTDELETE security key to access to this option.</p>
<p>WARNING: Deleting a LTC Copayment Test using this option deletes the test and all associated changes from the database; no copy of the test is stored for historical purposes.</p></td>
</tr>
<tr class="odd">
<td>Expiring or Expired LTC Copayment Tests</td>
<td>This option enables you to print a list of veterans whose LTC Copayment Tests have expired since a user-specified start date, or are about to expire within a user-specified number of days.</td>
</tr>
</tbody>
</table>

### Add a New LTC Copayment Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you start, please note:*

> ![](eas-version-1-1-long-term-care-copayment-user-manual/002.png) The patient must exist in the PATIENT file before you use this option.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/003.png) The patient must be a veteran; the software prevents the creation of LTC Copayment tests for non-veterans.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/004.png) All LTC Copayment Test financial information is for the CURRENT income year.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/005.png) Current year marital status and spouse residing in community must be answered for accurate calculation of the LTC copayment amounts.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/006.png) Screen 6 (DEDUCTIBLE EXPENSES) allows entry of funeral and burial expenses for a veteran without spouse or dependents. It also allows entry of expenses greater than the income entered in Screen 5 (CURRENT CALENDAR YEAR GROSS INCOME).

> ![](eas-version-1-1-long-term-care-copayment-user-manual/007.png) The prompts in this option were designed to follow the flow of VA Form 10-10EC, Application for Extended Care Services. The LTC software supports the display and printing of the LTC Copayment Tests in either the old or new (December, 2002) VAF 10-10EC format, depending on which one is used to complete the test. You can download a sample form from the Long-term Care Copayments web page on the VistaU Enrollment Training Initiatives web site at [REDACTED](http://vaww.vistau.med.va.gov/Enrollment/LTC_copayments.htm)

> ![](eas-version-1-1-long-term-care-copayment-user-manual/008.png) The following veterans are exempt from LTC Copayments; therefore, they will NOT BE REQUIRED to complete VA Form 10-10EC or pay Extended Care Copayments.

- A veteran with a compensable service-connected disability
- A veteran whose annual income is less than the Single Veteran Pension Rate in effect under 38 U.S.C. 1521(b)
- A veteran receiving care for a service-connected disability as determined by a VA health care provider and documented in the medical records
- A veteran receiving extended care services that began on or before November 30,1999
- A veteran receiving extended care services related to Vietnam-era herbicide-exposure, radiation exposure, Persian Gulf War, and post-Persian Gulf War combat-exposure
- A veteran receiving extended care services related to treatment for military sexual trauma as authorized under 38 U.S.C. 1720D
- A veteran receiving extended care services related to certain care or services for cancer of the head or neck as authorized under 38 U.S.C. 1720E
- A veteran receiving Hospice Care as a part of extended care services
- An eligible combat veteran receiving extended care services related to treatment authorized under 38 U.S.C. 1710(e)(1)(D)
- A veteran awarded Medal of Honor

> ![](eas-version-1-1-long-term-care-copayment-user-manual/009.png) Refer to Appendix A of this manual for sample LTC Copayment data screens.

*Use this option to*

- Add and complete a new LTC Copayment Test for a patient. You can add a new LTC Copayment Test for a veteran at any time, including multiple tests within the same year.
- Print a completed VA Form 10-10EC for the selected patient.

Add a New LTC Copayment Test, continued

*How to use this option*

1.  Select the patient for whom you are adding a LTC Copayment Test. The software displays the patient’s name, date of birth, SSN, and enrollment information. If the means test information for the selected patient is greater than 365 days old, the software displays the following notification.

> \*\*\* Patient Requires a Means Test \*\*\*

> Primary Means Test Required from \[Date\]

> Enter \<RETURN\> to continue.

> MEANS TEST REQUIRED

2.  Enter the date of the test (the default is the current date). If a test already exists for the selected veteran, the software displays the test date and asks if you want to continue.

> An LTC Copay Test already exists on JUL 17,2003.

> Are you sure you want to add a new test? NO//

> “No” response returns you to Step 1. “Yes” response takes you to Step 3.

> The software checks if the patient is exempt from LTC copayments based on his/her eligibility (in this example, compensable service-connected disability).

> ... checking if veteran is exempt from LTC copayments ...

> If the software determines that the patient is exempt from LTC copayments based on eligibility, the reason for exemption will also be displayed, and you return to Step 1.

> ===============================================================================

> Veteran is EXEMPT from Long Term Care copayments.

> Reason for Exemption: COMPENSABLE SC DISABILITY

> ===============================================================================

> If the software does not determine that the patient is exempt from LTC copayments based on eligibility, the following prompt appears.

> Is veteran EXEMPT from LTC copayments? NO// Y YES

Add a New LTC Copayment Test, continued

> *Step 2, continued*

> You would respond YES if the veteran is exempt for a reason other than low income.

> If you respond YES, you must enter a reason for exemption (in this example, hospice care).

> Reason for Exemption: ??

> Choose from:

> 3 LTC FOR SC DISABILITY

> 4 LTC BEGAN PRIOR TO 11/30/1999

> 5 LTC FOR EXPOSURE TO ENVIRONMENTAL CONTAMINANTS (GULF WAR)

> 6 LTC FOR AGENT ORANGE EXPOSURE

> 7 LTC FOR RADIATION EXPOSURE

> 8 LTC FOR TREATMENT RELATED TO MST

> 9 LTC RELATED TO CANCER OF THE HEAD AND NECK

> 11 LTC RELATED TO HOSPICE CARE

> 13 LTC IS SERVICE RELATED - COMBAT VET ELIGIBLE

> Reason for Exemption: LTC RELATED TO HOSPICE CARE

> The following message displays, and you return to Step 1.

> ===============================================================================

> Veteran is EXEMPT from Long Term Care copayments.

> Reason for Exemption: LTC RELATED TO HOSPICE CARE

> ===============================================================================

If the patient is *not exempt* from LTC Copayments, the following displays on your screen, and you go to Step 4.

===============================================================================

> Veteran is NOT EXEMPT from Long Term Care copayments and

> must complete a 10-10EC form.

> ===============================================================================

> If there is no prior year income information on file for the selected patient, the software displays the following notification.

> The previous year's financial information is not on file for this veteran.

> A Means Test is required.

> Do you wish to complete the Means Test at this time? NO//

> “No” response returns you to Step 1. “Yes” response takes you to the Add a New Means Test? Complete a Required Means Test? option in the Means Test User Menu. Refer to the means test user menu section of the Registration Menu User Manual at <http://www.va.gov/vdl/Clinical.asp?appID=55> for information about using this option.

Add a New LTC Copayment Test, continued

> *Step 2, continued*

3.  If the veteran declines to give income information, go to Step 4. If the veteran agrees to give income information, go to Step 5.
4.  The “Does the veteran agree to pay copayments? YES//” prompt appears only if the veteran declines to give income information. “Yes” response takes you to Step 12. You can optionally enter comments and/or print VA Form 10-10EC. A “No” response also takes you to Step 12. Please note that a “No” response will indicate that the veteran is ineligible to receive LTC services.
5.  Screens 1 (MILITARY SERVICE DATA) and 2 (INSURANCE DATA) will display. (Refer to Appendix A of this manual to see samples of these screens.) You cannot edit the data on these screens via the LTC Copayment Menu options. To edit this data, use the Load/Edit Patient Data option in the Registration Menu of the Admission, Discharge, and Transfer (ADT) software.
6.  Use the List Manager actions at the bottom of Screen 3 (MARITAL STATUS/DEPENDENTS), to enter the appropriate marital status and dependents information.

| Action Short Name | Action Long Name        | Description                                                                                                                                                                                                                                                                              |
|-----------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DA                    | Spouse/Dependent Add        | Allows you to add a new dependent. The dependent can either be a spouse or other dependents. The software will prompt for the LTC copayment test information questions if the dependent is added when using the Add a New LTC Copayment Test or Edit an Existing LTC Copayment Test options. |
| AD                    | Add to LTC Copay Test       | Allows you to add selected dependents to the LTC Copayment Test from the above list. The dependent does not have to currently be an active dependent. This will only be allowed if you are adding or editing a LTC Copayment Test.                                                           |
| ES                    | Edit Spouse Demographics    | Allows you to edit the demographics related to the spouse (e.g., Name, DOB, SSN, etc.)                                                                                                                                                                                                       |
| RE                    | Remove from LTC Copay Test  | Allows you to select dependent(s) to be removed from the LTC Copayment Test. This will only be allowed if you are adding or editing a LTC Copayment Test.                                                                                                                                    |
| DD                    | Edit Dependent Demographics | Allows you to edit the demographics related to dependents.                                                                                                                                                                                                                                   |
| XD                    | Expand Dependent            | Allows you to select a specific dependent and view more information about that dependent. You can also select an action to edit the effective dates for that dependent.                                                                                                                      |
| MT                    | Marital/Dependent Info      | Allows you to edit the veteran's marital status and spouse or dependent information specific to the LTC Copayment Test, such as Residing in the Community or Living with Spouse.                                                                                                             |

Add a New LTC Copayment Test, continued

> *Step 6, continued*

> When entering marital status, if you respond YES to the “IS YOUR MARITAL STATUS EITHER MARRIED OR SEPARATED:” prompt, the software prompts you to indicate if the veteran is legally separated. Responding YES to the “ARE YOU LEGALLY SEPARATED:” prompt automatically populates Item 9 (Current Marital Status) in Section III of VAF 10-10EC, and the veteran’s copayments are calculated using the rules for an unmarried veteran.

> The actions in the following table, although not displayed, are also available.

|     |                     |     |                    |      |                      |
|-----|---------------------|-----|--------------------|------|----------------------|
| \+  | Next Screen         | \<  | Shift View to Left | PS   | Print Screen         |
| \-  | Previous Screen     | FS  | First Screen       | PL   | Print List           |
| UP  | Up a Line           | LS  | Last Screen        | SL   | Search List          |
| DN  | Down a Line         | GO  | Go to Page         | ADPL | Auto Display(On/Off) |
| \>  | Shift View to Right | RD  | Re Display Screen  | Q    | Quit                 |

7.  Use the actions at the bottom of Screen 4 (FIXED AND LIQUID ASSETS) to enter dollar amounts for fixed and liquid assets for the current income year.
8.  Use the actions at the bottom of Screen 5 (CURRENT CALENDAR YEAR GROSS INCOME) to enter gross income data for the current income year. You can enter a monthly amount by entering the amount followed by an asterisk (\*), and the software will convert it to an annual amount. For example, if you enter 500\*, the software will multiply the amount (500) times 12 (the number of months in a year) and convert it to an annual amount of 6,000. Fields that do not have to be completed for the veteran you selected will have an entry of N/A; these fields cannot be edited on this screen.
9.  Use the actions at the bottom of Screen 6 (DEDUCTIBLE EXPENSES) to enter deductible expenses for the current income year. You can enter a monthly amount by entering the amount followed by an asterisk (\*), and the software will convert it to an annual amount. For example, if you enter 500\*, the software will multiply the amount (500) times 12 (the number of months in a year) and convert it to an annual amount of 6,000. Fields that do not have to be completed for the veteran you selected will have an entry of N/A; these fields cannot be edited on this screen.
10. The software prompts you to complete the LTC Copay test. “No” response returns you to Step 1; “Yes” response takes you to Step 11. (If the test cannot be completed because of missing or incomplete data, the software prompts you to edit the LTC Copayment Test. “Yes” response takes you to Screen 1 of the Edit a LTC Copayment Test option; “No” response returns you to the menu.)

Add a New LTC Copayment Test, continued

11. Enter the date and time the test was completed (default is today’s date and current time).
12. The software prompts you to enter COMMENTS. This is a word processing field.
13. The software prompts you to print the 10-10EC. “Yes” response takes you to Step 15; “No” response returns you to Step 1.
14. At the “PRINT 10-10EC? YES//” prompt, “Yes” prompt takes you to Step 15.
15. The software will ask if you want to queue the output. “No” response returns you to Step 1; “Yes” response takes you to Step 16.
16. Enter date and time to print the output.

### Edit an Existing LTC Copayment Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you start, please note:*

> ![](eas-version-1-1-long-term-care-copayment-user-manual/010.png) The patient must have an existing LTC Copayment test in order to use this option.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/011.png) The patient must be a veteran; the software prevents the creation of LTC Copayment tests for non-veterans.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/012.png) After you select the patient name and test date, this option works the same as the “Add a New LTC Copayment Test” option.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/013.png) You can edit the date of a LTC Copayment Test if you have the appropriate security key.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/014.png) All LTC Copayment Test financial information is for the CURRENT income year.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/015.png) Current year marital status and spouse residing in community must be answered for accurate calculation of the LTC copayment amounts.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/016.png) Screen 6 (DEDUCTIBLE EXPENSES) allows entry of funeral and burial expenses for a veteran without spouse or dependents. It also allows entry of expenses greater than the income entered in Screen 5 (CURRENT CALENDAR YEAR GROSS INCOME).

> ![](eas-version-1-1-long-term-care-copayment-user-manual/017.png) The prompts in this option were designed to follow the flow of VA Form 10-10EC, Application for Extended Care Services. The LTC software supports the display and printing of the LTC Copayment Tests in either the old or new (December, 2002) VAF 10-10EC format, depending on which one is used to complete the test. You can download a sample form from the Long-term Care Copayments web page on the VistaU Enrollment Training Initiatives web site at [REDACTED](http://vaww.vistau.med.va.gov/Enrollment/LTC_copayments.htm)

> ![](eas-version-1-1-long-term-care-copayment-user-manual/018.png) Refer to Appendix A of this manual for sample LTC Copayment data screens.

*Use this option to*

- Edit an existing LTC copayment test for a patient
- Complete an existing LTC copayment test
- Print completed VA Form 10-10EC for the selected patient

*How to use this option*

1.  Select the patient for whom you are adding a LTC Copayment Test. The software displays the patient’s name, date of birth, SSN, and enrollment information. If the means test information for the selected patient is greater than 365 days old, the software displays the following notification.

> \*\*\* Patient Requires a Means Test \*\*\*

> Primary Means Test Required from \[Date\]

> Enter \<RETURN\> to continue.

> MEANS TEST REQUIRED

Edit an Existing LTC Copayment Test, continued

2.  Select the date of the test that you want to edit (the default is the current date). You can edit the date of the test at the “DATE OF TEST: “ prompt if you have the appropriate security key.

> The software displays the LTC Copayment information and the veteran’s LTC Copayment status. At the “LTC Copay Test Status:” prompt, you can edit the test status. If you edit the status to EXEMPT, you must enter a reason for exemption (in this example, hospice care). The following message displays, and you return to Step 1.

> ===============================================================================

> Veteran is EXEMPT from Long Term Care copayments.

> Reason for Exemption: LTC RELATED TO HOSPICE CARE

> ===============================================================================

> If you edit the test status to NON-EXEMPT, the software takes you to Step 3.

3.  If the veteran declines to give income information, go to Step 4. If the veteran agrees to give income information, go to Step 5.
4.  The “Does the veteran agree to pay copayments? YES//” prompt appears only if the veteran declines to give income information. “Yes” response takes you to Step 12. You can optionally enter comments and/or print VA Form 10-10EC. A “No” response also takes you to Step 12. Please note that a “No” response will indicate that the veteran is ineligible to receive LTC services.
5.  Screens 1 (MILITARY SERVICE DATA) and 2 (INSURANCE DATA) will display. (Refer to Appendix A of this manual to see samples of these screens.) You cannot edit the data on these screens via the LTC Copayment Menu options. To edit this data, use the Load/Edit Patient Data option in the Registration Menu of the Admission, Discharge, and Transfer (ADT) software.

Edit an Existing LTC Copayment Test, continued

6.  Use the List Manager actions at the bottom of Screen 3 (MARITAL STATUS/DEPENDENTS), to enter the appropriate marital status and dependents information.

| Action Short Name | Action Long Name        | Description                                                                                                                                                                                                                                                                              |
|-----------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DA                    | Spouse/Dependent Add        | Allows you to add a new dependent. The dependent can either be a spouse or other dependents. The software will prompt for the LTC copayment test information questions if the dependent is added when using the Add a New LTC Copayment Test or Edit an Existing LTC Copayment Test options. |
| AD                    | Add to LTC Copay Test       | Allows you to add selected dependents to the LTC Copayment Test from the above list. The dependent does not have to currently be an active dependent. This will only be allowed if you are adding or editing a LTC Copayment Test.                                                           |
| ES                    | Edit Spouse Demographics    | Allows you to edit the demographics related to the spouse (e.g., Name, DOB, SSN, etc.)                                                                                                                                                                                                       |
| RE                    | Remove from LTC Copay Test  | Allows you to select dependent(s) to be removed from the LTC Copayment Test. This will only be allowed if you are adding or editing a LTC Copayment Test.                                                                                                                                    |
| DD                    | Edit Dependent Demographics | Allows you to edit the demographics related to dependents.                                                                                                                                                                                                                                   |
| XD                    | Expand Dependent            | Allows you to select a specific dependent and view more information about that dependent. You can also select an action to edit the effective dates for that dependent.                                                                                                                      |
| MT                    | Marital/Dependent Info      | Allows you to edit the veteran's marital status and spouse or dependent information specific to the LTC Copayment Test, such as Residing in the Community or Living with Spouse.                                                                                                             |

> When entering marital status, if you respond YES to the “IS YOUR MARITAL STATUS EITHER MARRIED OR SEPARATED:” prompt, the software prompts you to indicate if the veteran is legally separated. Responding YES to the “ARE YOU LEGALLY SEPARATED:” prompt automatically populates Item 9 (Current Marital Status) in Section III of VAF 10-10EC, and the veteran’s copayments will be calculated using the rules for an unmarried veteran.

> The actions in the following table, although not displayed, are also available.

|     |                     |     |                    |      |                      |
|-----|---------------------|-----|--------------------|------|----------------------|
| \+  | Next Screen         | \<  | Shift View to Left | PS   | Print Screen         |
| \-  | Previous Screen     | FS  | First Screen       | PL   | Print List           |
| UP  | Up a Line           | LS  | Last Screen        | SL   | Search List          |
| DN  | Down a Line         | GO  | Go to Page         | ADPL | Auto Display(On/Off) |
| \>  | Shift View to Right | RD  | Re Display Screen  | Q    | Quit                 |

7.  Use the actions at the bottom of Screen 4 (FIXED AND LIQUID ASSETS) to enter dollar amounts for fixed and liquid assets for the current income year.

Edit an Existing LTC Copayment Test, continued

8.  Use the actions at the bottom of Screen 5 (CURRENT CALENDAR YEAR GROSS INCOME) to enter gross income data for the current income year. You can enter a monthly amount by entering the amount followed by an asterisk (\*), and the software will convert it to an annual amount. For example, if you enter 500\*, the software will multiply the amount (500) times 12 (the number of months in a year) and convert it to an annual amount of 6,000. Fields that do not have to be completed for the veteran you selected will have an entry of N/A; these fields cannot be edited on this screen.
9.  Use the actions at the bottom of Screen 6 (DEDUCTIBLE EXPENSES) to enter deductible expenses for the current income year. You can enter a monthly amount by entering the amount followed by an asterisk (\*), and the software will convert it to an annual amount. For example, if you enter 500\*, the software will multiply the amount (500) times 12 (the number of months in a year) and convert it to an annual amount of 6,000. Fields that do not have to be completed for the veteran you selected will have an entry of N/A; these fields cannot be edited on this screen.
10. The software prompts you to complete the LTC Copay test. “No” response returns you to Step 1; “Yes” response takes you to Step 12. (If the test cannot be completed because of missing or incomplete data, the software prompts you to edit the LTC Copayment Test. “Yes” response takes you to Screen 1 of the Edit a LTC Copayment Test option; “No” response returns you to the menu. )
11. Enter the date and time the test was completed (default is today’s date and current time).
12. The software prompts you to enter COMMENTS. This is a word processing field.
13. The software prompts you to print the 10-10EC. “Yes” response takes you to Step 15; “No” response returns you to Step 1.
14. At the “PRINT 10-10EC? YES//” prompt, “Yes” prompt takes you to Step 15.
15. The software will ask if you want to queue the output. “No” response returns you to Step 1; “Yes” response takes you to Step 16.
16. Enter date and time to print the output.

### View a LTC Copayment Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you start, please note:*

> ![](eas-version-1-1-long-term-care-copayment-user-manual/019.png) The patient must have an existing LTC Copayment test in order to use this option.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/020.png) This option allows you to view data only; it does not allow editing. Use the Edit an Existing LTC Copayment Test option if you want to edit the test.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/021.png) The LTC software supports the display and printing of the LTC Copayment Tests in either the old or new (December, 2002) VAF 10-10EC format, depending on which one is used to complete the test. You can download a sample form from the Long-term Care Copayments web page on the VistaU Enrollment Training Initiatives web site at REDACTED

> ![](eas-version-1-1-long-term-care-copayment-user-manual/022.png) Refer to Appendix A of this manual for sample data screens.

*Use this option to*

View a LTC Copayment test for a specified patient. You can view the following data screens while using this option.

- MILITARY SERVICE DATA, SCREEN \<1\>
- INSURANCE DATA, SCREEN \<2\>
- MARITAL STATUS/DEPENDENTS, SCREEN \<3\>
- FIXED AND LIQUID ASSETS, SCREEN \<4\>
- CURRENT CALENDAR YEAR GROSS INCOME, SCREEN \<5\>
- DEDUCTIBLE EXPENSES, SCREEN \<6\>

*How to use this option*

1.  Select the patient whose LTC Copayment test you want to view. The software displays the patient’s name, date of birth, SSN, and enrollment information.
2.  Enter the date of the test you want to view (default is original test date). The software displays the patient’s LTC Copayment Test information.
3.  Navigate through the data screens that were populated using the Add a New LTC Copayment Test option and/or Edit an Existing LTC Copayment options.

### Print Application for Extended Care (1010-EC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you start, please note:*

> ![](eas-version-1-1-long-term-care-copayment-user-manual/023.png) The patient must have an existing LTC Copayment test in order to use this option.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/024.png) You must specify a 132-column printer at the “DEVICE: HOME//” prompt; screen print of the form will be unreadable.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/025.png) The LTC software supports the display and printing of the LTC Copayment Tests in either the old or new (December, 2002) VAF 10-10EC format, depending on which one is used to complete the test. You can download a sample form from the Long-term Care Copayments web page on the VistaU Enrollment Training Initiatives web site at REDACTED

*Use this option to*

Print a completed VA Form 10-10EC, Application for Extended Care Services, for a selected patient.

*How to use this option*

1.  Select the patient whose LTC Copayment test you want to print. The software displays the patient’s name, date of birth, SSN, and enrollment information.
2.  Enter the date of the test you want to print (default is original test date). The software displays the test type and test status.
3.  Select the name of the printer.
4.  Specify whether to queue the print job. If yes, specify the date and time you want the form to print.

### Calculated LTC Copayments Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you start, please note:*

> ![](eas-version-1-1-long-term-care-copayment-user-manual/026.png) The patient must have an existing LTC Copayment test in order to use this option.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/027.png) Copayments will only be calculated and printed for patients with a LTC Copayment Test status of NON-EXEMPT. Patients with a status of EXEMPT are not required to pay for LTC services.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/028.png) This option provides *estimated* LTC copayment amounts only. When you select this option, a disclaimer appears on the screen. When you send the report to a printer, disclaimers print at the top and bottom of each page. When you display the LTC copayment amounts on your screen, one disclaimer appears in the header on each screen, another disclaimer appears only at the end of the output.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/029.png) This report might take a long time to generate. You should queue the output to print to a device other than your screen and specify a date and time to print.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/030.png) Refer to Appendix B of this manual for LTC Copayment calculation scenarios.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/031.png) Refer to Appendix C of this manual for sample outputs.

*Use this option to*

Display or print the calculated LTC copayments for a selected veteran. The output includes the following information.

- The date on which the report is generated, page number, and report title
- The selected patient’s name, SSN, date of birth, marital status, and LTC Copayment Test date
- The LTC Admission Date (only on the copayment report for institutional extended care services)
- Formula(s) used for calculating copayments for both institutional and non-institutional extended care services for a 6-month period and for a period greater than 6 months
- Monthly totals for total income, total expenses, and total allowances
- Monthly totals for the veteran’s estimated copayment amount (displayed as CALC COPAY)
- Monthly totals for the maximum copayment that could potentially be billed (displayed as MAX COPAY), which this is the cap amount
- Monthly totals for the estimated maximum copayment that the veteran would be responsible for paying (displayed as VET COPAY), which is the lesser of *either* the CALC COPAY or MAX COPAY
- An explanation of the asset spend down calculation (only on the copayment report for institutional extended care services)

Calculated LTC Copayments Print, continued

*How to use this option*

1.  Select the desired format: Institutional (Inpatient) or Non-Institutional (Outpatient). Either response takes you to Step 2.
2.  Select the patient whose estimated LTC copayments you want to display or print. The software displays the patient’s name, date of birth, SSN, enrollment information, and LTC Copayment test information. If your response at Step 1 was “Institutional”, go to Step 3. If your response at Step 1 was “Non-Institutional”, go to Step 4.
3.  Enter the admission date for the current institutional Long Term Care episode.
4.  Enter the starting date for the report in the format month/year (e.g. 9/03). The report will print 12 months of copayments starting with the month and year entered. You can enter a date in the future if you want the report to reflect the spend-down of the patient’s assets.
5.  Select a printer.
6.  Specify whether to queue the print job. If yes, specify a device other than your screen and the date and time you want the report to print.

### Delete a LTC Copayment Test (10-10EC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you start, please note:*

> ![](eas-version-1-1-long-term-care-copayment-user-manual/032.png) The patient must have an existing LTC Copayment test in order to use this option.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/033.png) Use extreme caution when using this option. Deleting a LTC Copayment Test removes the test from the database; no copy is stored for historical purposes. It also deletes all changes associated with the selected test.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/034.png) You must have the DG MTDELETE security key allocated to you in order to access this option.

*Use this option to*

Delete a Long Term Care Copayment Test (10-10EC) that may have been entered in error, and all changes associated with the selected test.

*How to use this option*

1.  Select the patient who’s LTC Copayment Test you want to delete.
2.  The patient’s eligibility, enrollment, Means Test, and LTC Copayment Test data will be displayed.
3.  If multiple tests exist for the selected patient, the software prompts you to choose one.
4.  The software asks if you want to display the selected test. If your response is “No”, go to Step 5. If your response is “Yes”, go to Step 6.
5.  The software prompts you to verify that you want to delete the LTC Copayment Test. If your response is “No”, go to Step 6. If your response is “Yes”, go to Step 7.
6.  Return to the LTC Copayment Test Menu.
7.  The LTC Copayment Test and all associated changes are permanently deleted from the database.

### Expiring or Expired LTC Copayment Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you start, please note:*

> ![](eas-version-1-1-long-term-care-copayment-user-manual/035.png) The patient must have an existing LTC Copayment test in order to use this option.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/036.png) This option allows you to view data only; it does not allow editing. Use the Edit an Existing LTC Copayment Test option if you want to edit the test.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/037.png) The reports generated when using this option will not include deceased veterans, veterans who were exempt from LTC copayments due to a compensable service-connected disability, or veterans whose LTC episode began *before* 11/30/99.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/038.png) This report might take a long time to generate. You should queue the output to print to a device other than your screen and specify a date and time to print.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/039.png) Refer to Appendix A of this manual for sample data screens.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/040.png) Refer to Appendix D of this manual for sample outputs.

*Use this option to*

- Print a list of veterans whose LTC Copayment Test is pending expiration (i.e., the anniversary date of the test is approaching) within a user-specified number of days
- Print a list of veterans whose LTC Copayment Test has already expired (i.e., the anniversary date of the test has passed) since a user-specified date.

*How to use this option*

1.  Select the report (Pending Expiration or Expired) that you want to print. If you selected Pending Expiration, go to Step 2. If you selected Expired, go to Step 3.
2.  Select the number of days in which LTC Copayment Tests are about to expire to include in the report. Go to Step 4.
3.  Enter a start date for LTC Copayment Tests that have already expired.
4.  Select a sort method (Name or Date).
5.  Select a device to print the report. If you enter an up-caret (^) at the “DEVICE: HOME//” prompt, the software cancels the report and displays “Report Cancelled!” on your screen.

#####################  LTC Copay Exemption Test Menu

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Option Name</td>
<td>Brief Description</td>
</tr>
<tr class="even">
<td>Delete a LTC Copay Exemption Test</td>
<td>This option is used to delete a LTC Copayment Exemption Test which may have been inadvertently entered.</td>
</tr>
<tr class="odd">
<td>Edit an Existing LTC Copay Exemption Test</td>
<td>Edit existing LTC Copayment Exemption Test information.</td>
</tr>
<tr class="even">
<td>LTC Copay Exemption Test View</td>
<td>This option allows a user to view a LTC Copay Exemption Test.</td>
</tr>
<tr class="odd">
<td>View LTC Copay Exemption Test Editing</td>
<td><p>This option allows the user to view all changes made to a particular LTC Copayment Exemption Test for a patient. Some of the displayed information includes date of change, user who made the change, and the type of change. If a change involves a change to the test status, both the current and previous values are displayed.</p>
<p>If a LTC Exemption Test is deleted, any associated changes are also deleted.</p></td>
</tr>
</tbody>
</table>

> **NOTE:** There is no Add option on this menu, because the LTC Copayment Exemption Test is created automatically based on the veteran’s means test.

### Delete a LTC Copay Exemption Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you start, please note:*

> ![](eas-version-1-1-long-term-care-copayment-user-manual/041.png) Deleting a LTC Copayment Exemption Test also deletes all changes associated with that test.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/042.png) You cannot delete a LTC Copayment Exemption Test that was uploaded from the HEC.

*Use this option to*

Delete financial test data which may have been entered in error. For veterans, only individual dates of test may be deleted using this option. For non-veterans, all financial tests found may be deleted.

*How to use this option*

1.  Select the patient whose LTC Copayment Exemption Test you want to delete.
2.  The patient’s eligibility, enrollment, Means Test, and LTC Copayment Exemption Test data will be displayed.
3.  The software prompts you to verify that you want to delete the LTC Copayment Exemption Test. “No” response returns you to the menu; “Yes” response deletes the test and associated changes.

### Edit an Existing LTC Copay Exemption Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Before you start, please note:*

![](eas-version-1-1-long-term-care-copayment-user-manual/043.png) A LTC Copayment Exemption Test must exist for the specified veteran before you can use this option.

![](eas-version-1-1-long-term-care-copayment-user-manual/044.png) Refer to Appendix B of this manual for sample data screens.

*Use this option to*

Edit an existing LTC Copayment Exemption Test and to complete the revised test.

*How to use this option*

1.  Select the patient whose test that you want to edit. The patient’s LTC Copayment Exemption Test data will be displayed.
2.  Select the date of the test that you want to edit (the default is the original test date).
3.  Use the actions available at the bottom of the data screen(s) to edit the patient’s financial information.
4.  Enter the date and time that the test was completed (the default is the date of the original test).
5.  Indicate whether you want to print VA Form 10-10EZR. YES response takes you to Step 6; NO response, system prompts “Print 10-10EZ?”. NO response returns user to Step 1.
6.  Select a printer. The output requires 132 columns.

### LTC Copay Exemption Test View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](eas-version-1-1-long-term-care-copayment-user-manual/045.png) The patient must have an existing LTC Copayment test in order to use this option.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/046.png) This option allows you to view data only; it does not allow editing. Use the Edit an Existing LTC Copayment Exemption Test option if you want to edit the test.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/047.png) Refer to Appendix B of this manual for sample data screens.

*Use this option to*

View a LTC Copayment Exemption Test for a specified patient. You can view the following data screens while using this option.

- MARITAL STATUS/DEPENDENTS, SCREEN \<1\>
- PREVIOUS CALENDAR YEAR GROSS INCOME, SCREEN \<2\>
- DEDUCTIBLE EXPENSES, SCREEN \<3\>

*How to use this option*

1.  Select the patient whose LTC Copayment Exemption Test you want to view. The patient’s enrollment information will be displayed.
2.  Enter the date of the test you want to view (the default is the original test date). The patient’s LTC Copayment Exemption Test information will be displayed.
3.  Navigate through the data screens that were populated when the new LTC Copayment Test was created or edited.

### View LTC Copay Exemption Test Editing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](eas-version-1-1-long-term-care-copayment-user-manual/048.png) The patient must have an existing LTC Copayment test in order to use this option.

> ![](eas-version-1-1-long-term-care-copayment-user-manual/049.png) This option allows you to view data only; it does not allow editing. Use the Edit an Existing LTC Copayment Exemption Test option if you want to edit the test.

*Use this option to*

View all changes made to a LTC Copayment Exemption Test for a specified patient. If the test status was changed, both the current and previous statuses will be displayed. The output includes:

- Date and time of change
- Type of change
- User who made the change

*How to use this option*

1.  Select the patient whose LTC Copayment Exemption Test you want to view.

*Sample Output*

PATIENT: EASPATIENT,ONE LTC EXEMPTION TEST DATE: 02/26/2002

VAMC LTC EXEMPTION TEST

CHANGES

Date Type of Change User

=============================================================================

02/26/2002@16:13:49 ADD NEW COPAY EXEMPTION TEST EASUSER,ONE

OLD STATUS VALUE: \<Nothing\>

NEW STATUS VALUE: NON-EXEMPT

OLD SOURCE OF TEST: \<Nothing\>

NEW SOURCE OF TEST: VAMC

# # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym         | Long Name                                               |
|-----------------|---------------------------------------------------------|
| 10-10EC         | VA Form 10-10EC, Application for Extended Care Services |
| 10-10EZ         | VA Form 10-10EZ, Application for Health Benefits        |
| API             | Application Programmer Interface                        |
| LTC             | Long Term Care                                          |
| VA              | Veterans Administration                                 |
| V*IST*A | VHA Information Systems and Technology Architecture     |

# # Appendix A – LTC Copayment Data Screen Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides examples of the data screens you will see when using the options associated with the LTC Copayments and LTC Copay Exemption Test Menus. The following table provides an overview of the data screens associated with each menu option.

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">LTC Copayments Menu</td>
</tr>
<tr class="even">
<td><p>Add a New LTC Copayment Test</p>
<p>Edit an Existing LTC Copayment Test</p>
<p>View a LTC Copayment Test</p></td>
<td><ul>
<li><p>MILITARY SERVICE DATA, SCREEN &lt;1&gt;</p></li>
<li><p>INSURANCE DATA, SCREEN &lt;2&gt;</p></li>
<li><p>MARITAL STATUS/DEPENDENTS, SCREEN &lt;3&gt;</p></li>
<li><p>FIXED AND LIQUID ASSETS, SCREEN &lt;4&gt;</p></li>
<li><p>CURRENT CALENDAR YEAR GROSS INCOME, SCREEN &lt;5&gt;</p></li>
<li><p>DEDUCTIBLE EXPENSES, SCREEN &lt;6&gt;</p></li>
</ul></td>
</tr>
<tr class="odd">
<td colspan="2">LTC Copay Exemption Test Menu</td>
</tr>
<tr class="even">
<td><p>Edit an Existing LTC Copay Exemption Test</p>
<p>LTC Copay Exemption Test View</p></td>
<td><ul>
<li><p>MARITAL STATUS/DEPENDENTS, SCREEN &lt;1&gt;</p></li>
<li><p>PREVIOUS CALENDAR YEAR GROSS INCOME, SCREEN &lt;2&gt;</p></li>
<li><p>DEDUCTIBLE EXPENSES, SCREEN &lt;3&gt;</p></li>
</ul></td>
</tr>
</tbody>
</table>

MILITARY SERVICE DATA, SCREEN \<1\>

EASPATIENT,ONE 999-99-0000 LTC COPAY TEST FOR 2002

==============================================================================

Service Branch Service \# Entered Separated Discharge

-------------- --------- ------- --------- ---------

ARMY 00099999 UNKNOWN UNKNOWN UNKNOWN

POW: From: To: War:

Combat: From: To: Loc:

Vietnam: From: To:

A/O Exp.: Reg: Exam: A/O#:

ION Rad.: Reg: Method:

Lebanon: From: To:

Grenada: From: To:

Panama: From: To:

Gulf War: From: To:

Somalia: From: To:

Env Contam: Reg: Exam:

Mil Disab: UNANSWERED

Dent Inj: Teeth Extracted:

Yugoslavia: From: To:

Purple Heart:

N/T Radium:

INSURANCE DATA, SCREEN \<2\>

EASPATIENT,ONE 000-90-0000 LTC COPAY TEST FOR 2002

==============================================================================

Covered by Health Insurance: UNKNOWN

Insurance COB Subscriber ID Group Holder Effective Expires

===========================================================================

No Insurance Information

Eligible for MEDICAID: YES \[last updated AUG 5,2003@13:37\]

Medicaid Number: 000900000

Enter RETURN to continue or '^' to exit:

Spouse/Dependents Module Mar 12, 2002@16:21:29 Page: 1 of 1

MARITAL STATUS/DEPENDENTS, SCREEN \<3\>

Patient: EASPATIENT,ONE (000-90-0000) Outpatient

LTC Patient/Dependent Relationship Active Address

1 \* TEST,PATIENT SELF \* \*

Married This Year: Yes

Legally Separated: Yes

Enter ?? for more actions

DA Spouse/Dependent Add AD Add to LTC Co pay Test

ES Edit Spouse Demographics RE Remove from LTC Co pay Test

DD Edit Dependent Demographics XD Expand Dependent

MT Marital/Dependent Info

Select Action:Quit//

FIXED AND LIQUID ASSETS, SCREEN \<4\>

EASPATIENT,ONE 000-90-0000 LTC COPAY TEST FOR 2002

==============================================================================

Veteran and Spouse Total

------------------------------------------

\[1\] Residence \$85000.00 \$85000.00

\[2\] Other Residences/Land/Farm - -

\[3\] Vehicle(s) \$12000.00 \$12000.00

\[4\] Cash, Stocks, Bonds, Mutual Fund \$6000.00 \$6000.00

\[5\] Other Liquid Assets - -

Total --\> \$103000.00

THIS SCREEN NOW HAS A SEPARATE COLUMN FOR SPOUSE ASSETS

\<RET\> to CONTINUE, 1-6 or 'ALL' to EDIT, ^N for screen N, or '^' to EXIT:

CURRENT CALENDAR YEAR GROSS INCOME, SCREEN \<5\>

EASPATIENT,ONE 000-90-0000 LTC COPAY TEST FOR 2002

==============================================================================

Veteran Spouse Total

------------------------------------------

\<1\> Gross Annual Employment Income \$30000.00 -

\<2\> Net Income Farm/Ranch/Property

\<3\> Other Income

Total --\> \$30000.00

\<RET\> to CONTINUE, 1-14 or 'ALL' to EDIT, ^N for screen N, or '^' to EXIT:

DEDUCTIBLE EXPENSES, SCREEN \<6\>

EASPATIENT,ONE 000-90-0000 LTC COPAY TEST FOR 2002

==============================================================================

Veteran and Spouse Total

------------------------------------------

\[1\] Education - -

\[2\] Funeral and Burial - -

\[3\] Rent/Mortgage - -

\[4\] Utilities \$2760.00 \$2760.00

\[5\] Car Payment Only - -

\[6\] Food \$4200.00 \$4200.00

\[7\] Non-reimbursed Medical Exp \$800.00 \$800.00

\[8\] Court-ordered Payments - -

\[9\] Insurance - -

\[10\] Taxes \$1000.00 \$1000.00

Total --\> \$8760.00

\<RET\> to CONTINUE, 1-10 or 'ALL' to EDIT, ^N for screen N, or '^' to EXIT:

# Appendix B – LTC Copayment Calculation Scenarios

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

##################### Institutional Extended Care Services

#### Scenario \#1

Patient is receiving institutional extended care. The spouse is residing in the community (in primary residence). Patient has been in extended care for less than 180 days.

*Copayment Calculation*

Veteran and Spouse Income *minus* Allowance (spouse and veteran) *minus* Expenses

#### Scenario \#2

Patient is receiving institutional extended care. The spouse is residing in the community (in primary residence). Patient has been in extended care for 181 days or more.

*Copayment Calculation*

Fixed assets (minus primary residence and one vehicle) *plus* Liquid Assets *plus* Veteran and Spouse Income *minus* Allowance (spouse and veteran) *minus* Expenses

#### Scenario \#3

Patient receiving institutional extended care. Spouse institutionalized. Patient has been in extended care for 180 days or less.

*Copayment Calculation*

Income (veteran and spouse) *minus* Allowance (veteran only) *minus* Expenses

#### Scenario \#4

Patient receiving institutional extended care. Spouse institutionalized. Patient has been in extended care for 181 days.

*Copayment Calculation*

Fixed assets (*minus* primary residence and one vehicle) *plus* Liquid Assets *plus* Income (veteran and spouse) *minus* Allowance (veteran only)

#### Scenario \#5

Patient is receiving institutional extended care. The patient and spouse reside in separate residences. Patient has been in extended care for less than 180 days.

*Copayment Calculation*

Veteran and Spouse Income *minus* Allowance (spouse and veteran) *minus* Expenses

#### Scenario \#6

Patient is receiving institutional extended care. The patient and spouse reside in separate residences. Patient has been in extended care for 181 days or more.

*Copayment Calculation*

Fixed assets (*minus* both primary residence and vehicles of veteran and spouse) *plus* Liquid Assets *plus* Veteran and Spouse Income *minus* Allowance (spouse and veteran) *minus* Expenses

Scenario \#7

Patient is receiving institutional extended care. Patient has no spouse or dependent residing in the community (single veteran). Patient has been in extended care less than 180 days.

Copayment Calculation =

Income *minus* Allowance (veteran) *minus* Expenses

Scenario \#8

Patient is receiving institutional extended care. Patient has no spouse or dependent residing in the community (single veteran). Patient has been in extended care for 181 days or more.

Copayment Calculation =

Fixed assets (including primary residence and vehicle) *plus* Liquid Assets *plus* Income – Allowance (veteran)

##################### Non Institutional Extended Care Services

Scenario \#1

Patient is receiving non-institutional extended care services. There is no spouse in the community (single veteran).

Copayment Calculation =

Income (veteran) *minus* Allowance (veteran) *minus* Expenses

Scenario \#2

Patient is receiving non-institutional extended care services. A spouse or dependent resides in the community (single veteran).

Copayment Calculation =

Income (veteran and spouse) *minus* Allowance (veteran and spouse) *minus* Expenses

# Appendix C – Calculated LTC Copayments Print Option Sample Outputs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

##################### Sample 1 – Single Veteran, Non-institutional (Outpatient) Care

LONG TERM CARE ESTIMATED COPAYMENTS FOR NON-INSTITUTIONAL SERVICES

\*\*This report contains projected estimates based on existing data\*\*

EASPATIENT,ONE 000-70-0000 DOB: Sep 08, 1927

SINGLE

LTC COPAY TEST DATE: Nov 04, 2003

LTC COPAYMENT CALCULATION:

TOTAL INCOME - TOTAL EXPENSES - TOTAL ALLOWANCE

NOV'03 DEC'03 JAN'04 FEB'04 MAR'04 APR'04

TOT INCOME 3416 3416 3416 3416 3416 3416

TOT EXPENSES 0 0 0 0 0 0

TOT ALLOWANCE 600 620 620 580 620 600

CALC COPAY 2816 2796 2796 2836 2796 2816

MAX COPAY 450 465 465 435 465 450

--------------------------------------------------------------------------------

VET COPAY 450 465 465 435 465 450

--------------------------------------------------------------------------------

MAY'04 JUN'04 JUL'04 AUG'04 SEP'04 OCT'04

TOT INCOME 3416 3416 3416 3416 3416 3416

TOT EXPENSES 0 0 0 0 0 0

TOT ALLOWANCE 620 600 620 620 600 620

CALC COPAY 2796 2816 2796 2796 2816 2796

MAX COPAY 465 450 465 465 450 465

--------------------------------------------------------------------------------

VET COPAY 465 450 465 465 450 465

--------------------------------------------------------------------------------

Nov 10, 2003 Page: 2

LONG TERM CARE ESTIMATED COPAYMENTS FOR NON-INSTITUTIONAL SERVICES

\*\*This report contains projected estimates based on existing data\*\*

EASPATIENT,ONE 000-70-0000 DOB: Sep 08, 1927

IMPORTANT NOTICE: The copayment amounts shown in this report are estimates

based on calculations of the copayment amount for an entire month. The

copayment amounts will be adjusted to reflect the actual start date of LTC

services and the copayment exemption for the first 21 days of service. The VET

COPAY amount is based on the assumption that the veteran will be responsible

to pay the lesser of EITHER the calculated copayment (CALC COPAY) OR the

maximum copayment (MAX COPAY). In the event that the calculated copayment

(CALC COPAY) is a negative figure, the veteran copayment (VET COPAY)

will be adjusted to zero (0). If the veteran declined to provide income

information, the veteran will be obligated to pay the maximum copayment.

##################### Sample 2 – Single Veteran, Institutional (Inpatient) Care

Nov 07, 2003 Page: 1

LONG TERM CARE ESTIMATED COPAYMENTS FOR INSTITUTIONAL SERVICES

\*\*This report contains projected estimates based on existing data\*\*

EASPATIENT,ONE 000-70-0000 DOB: Sep 08, 1927

SINGLE

LTC COPAY TEST DATE: Nov 04, 2003 LTC ADMISSION DATE: Nov 07, 2003

LTC COPAYMENT CALCULATIONS:

FOR DAYS 1-180 TOTAL INCOME - TOTAL EXPENSES - TOTAL ALLOWANCE

FOR DAYS 181+ (TOTAL ASSETS + TOTAL INCOME) - TOTAL ALLOWANCE

NOV'03 DEC'03 JAN'04 FEB'04 MAR'04 APR'04

TOT ASSETS - - - - - -

TOT INCOME 3416 3416 3416 3416 3416 3416

TOT EXPENSES 0 0 0 0 0 0

TOT ALLOWANCE 600 620 620 580 620 600

CALC COPAY 2816 2796 2796 2836 2796 2816

MAX COPAY 2910 3007 3007 2813 3007 2910

--------------------------------------------------------------------------------

VET COPAY 2816 2796 2796 2813 2796 2816

--------------------------------------------------------------------------------

MAY'04 JUN'04 JUL'04 AUG'04 SEP'04 OCT'04

TOT ASSETS 14000 13789 13696 13486 13275 13182

TOT INCOME 3416 3416 3416 3416 3416 3416

TOT ALLOWANCE 620 600 620 620 600 620

CALC COPAY 16796 16606 16493 16282 16092 15979

MAX COPAY 3007 2910 3007 3007 2910 3007

--------------------------------------------------------------------------------

VET COPAY 3007 2910 3007 3007 2910 3007

--------------------------------------------------------------------------------

Nov 10, 2003 Page: 2

LONG TERM CARE ESTIMATED COPAYMENTS FOR NON-INSTITUTIONAL SERVICES

\*\*This report contains projected estimates based on existing data\*\*

EASPATIENT,ONE 000-70-0000 DOB: Sep 08, 1927

IMPORTANT NOTICE: The copayment amounts shown in this report are estimates

based on calculations of the copayment amount for an entire month. The

copayment amounts will be adjusted to reflect the actual start date of LTC

services and the copayment exemption for the first 21 days of service. The VET

COPAY amount is based on the assumption that the veteran will be responsible

to pay the lesser of EITHER the calculated copayment (CALC COPAY) OR the

maximum copayment (MAX COPAY). In the event that the calculated copayment

(CALC COPAY) is a negative figure, the veteran copayment (VET COPAY)

will be adjusted to zero (0). If the veteran declined to provide income

information, the veteran will be obligated to pay the maximum copayment.

# Appendix D – Expiring or Expired LTC Copayment Tests Option Sample Outputs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

##################### Sample 1 - Pending Expiration

REPORT DATE: Nov 10, 2003 PAGE: 1

VETERANS WITH LONG TERM CARE COPAYMENT TESTS THAT

ARE PENDING EXPIRATION IN 60 DAYS

SORTED BY NAME

LTC Test LTC Test

SSN Veteran's Name Anniversary Date Status

=============================================================================

000-40-0000 EASPATIENT,ONE 11/14/03 NON-EXEMPT

000-70-0000 EASPATIENT,ONE 12/24/03 NON-EXEMPT

000-10-0000 EASPATIENT,ONE 12/24/03 NON-EXEMPT

000-04-0000 EASPATIENT,ONE 01/07/04 NON-EXEMPT

000-20-0000 EASPATIENT,ONE 12/24/03 NON-EXEMPT

Enter RETURN to continue or '^' to exit:

##################### Sample 2 - Expired

REPORT DATE: Nov 10, 2003 PAGE: 1

VETERANS WITH LONG TERM CARE COPAYMENT TESTS THAT

HAVE EXPIRED SINCE 9/10/03

SORTED BY DATE

LTC Test LTC Test

SSN Veteran's Name Anniversary Date Status

=============================================================================

000-06-0606 EASPATIENT,ONE 09/18/03 EXEMPT

Reason: INCOME (LAST YEAR) BELOW LTC THRESHOLD

000-03-0364 EASPATIENT,ONE 09/20/03 EXEMPT

Reason: INCOME (CURRENT YEAR) BELOW LTC THRESHOLD

000-10-4000 EASPATIENT,ONE 10/04/03 NON-EXEMPT

000-10-1000 EASPATIENT,ONE 10/22/03 NON-EXEMPT

000-10-4000 EASPATIENT,ONE 10/22/03 NON-EXEMPT

000-11-0000 EASPATIENT,ONE 10/24/03 NON-EXEMPT

000-10-0000 EASPATIENT,ONE 10/24/03 NON-EXEMPT

000-01-0000 EASPATIENT,ONE 10/31/03 NON-EXEMPT

000-09-0000 EASPATIENT,ONE 10/31/03 NON-EXEMPT

000-02-0000 EASPATIENT,ONE 10/31/03 NON-EXEMPT

000-70-0000 EASPATIENT,ONE 11/01/03 NON-EXEMPT

Enter RETURN to continue or '^' to exit:

# # Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A

Add a New LTC Copayment Test 7

Appendix A - LTC Copayment Data Screen Examples 28

Appendix B – LTC Copayment Calculation Scenarios 32

Appendix C – Calculated LTC Copayments Print Option Sample Outputs 34

Appendix D – Expiring or Expired LTC Copayment Tests Option Sample Outputs 36

Assignment of User Options 5

C

Calculated LTC Copayments Print 19

D

Delete a LTC Copay Exemption Test 23

Delete a LTC Copayment Test (10-10EC) 21

E

Edit an Existing LTC Copay Exemption Test 24

Edit an Existing LTC Copayment Test 13

Expiring or Expired LTC Copayment Tests 22

G

Glossary 27

I

Introduction 1

L

LTC Copay Exemption Test Menu 23

LTC Copay Exemption Test View 25

LTC Copayments Menu 6

M

Menu Diagram 5

O

Overview 1

P

Print Application for Extended Care (1010-EC) 18

Purpose 3

R

Related Manuals 4

T

Training 3

U

Using the Software 5

V

View a LTC Copayment Test 17

View LTC Copay Exemption Test Editing 26