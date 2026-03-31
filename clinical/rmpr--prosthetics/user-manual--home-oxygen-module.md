---
title: Home Oxygen Module User Manual (Updated RMPR*3*168)
doc_type: UM
doc_label: User Manual
doc_layer: plain
doc_subject: Home Oxygen Module  (Updated RMPR*3*168)
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - patient
  - billing
  - oxygen
  - home
  - table
  - contents
  - site
  - concentrator
  - date
  - prescription
page_count: 0
word_count: 9058
section_count: 22
table_count: 18
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr3_o2um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr3_o2um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

PROSTHETICSADMINISTRATIVE HOME OXYGEN MODULEUser Manual

![](home-oxygen-module-user-manual-updated-rmpr-3-168/001.png)

Version 3.0September 1999(Revised August 2014)Department of Veterans AffairsOffice of Information and TechnologyProduct DevelopmentRevision History

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 43%" />
<col style="width: 26%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Project Manager</strong></th>
<th><strong>Technical Writer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/2014</td>
<td><p>Updated document for RMPR*3.0*168:</p>
<p><a href="#_top">Updated title page</a></p>
<p>Added Revision History table</p>
<p>New ICD-10 screen captures (pp. <a href="#ICD10screen1">3-5</a>, <a href="#add-an-item">4-8</a>)</p>
<p>Added ICD-10 code reference (pp. <a href="#ICD10codeupdate1">3-4</a>, <a href="#ICD10codeupdate2">6-2</a>)</p>
<p>Added note for Home Oxygen Patient Warning Message (p. <a href="#ICD10homeoxypatientwarning"><u>3-1</u></a>)</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table of Contents

1\. Introduction [1-1](#introduction)

Overview [1-1](#overview)

New Administrative Home Oxygen Options [1-1](#new-administrative-home-oxygen-options)

List Manager Functions [1-3](#list-manager-functions)

2\. Setting Up the Site Parameters [2-1](#setting-up-the-site-parameters)

Information Needed for the Site Parameters [2-1](#information-needed-for-the-site-parameters)

Correspondence [2-1](#correspondence)

Home Oxygen Vendors [2-2](#home-oxygen-vendors)

Fund Control Points [2-2](#fund-control-points)

Sequence Numbering of Prescriptions [2-2](#sequence-numbering-of-prescriptions)

Site Parameters Enter/Edit Option [2-3](#site-parameters-enteredit-option)

3\. Entering Patient and Prescription Information [3-1](#entering-patient-and-prescription-information)

Add/Edit Home Oxygen Patient [3-2](#section-1)

Add a New Patient [3-2](#add-a-new-patient)

Edit the Patient's Eligibility [3-3](#edit-the-patients-eligibility)

Activate the Patient [3-3](#activate-the-patient)

Add a New Prescription [3-3](#add-a-new-prescription)

Add or Edit a Billing Item [3-4](#add-or-edit-a-billing-item)

Inactivate/Activate Oxygen Patient [3-7](#inactivateactivate-oxygen-patient)

Inactivate a Home Oxygen Patient [3-7](#inactivate-a-home-oxygen-patient)

Activate a Home Oxygen Patient [3-7](#activate-a-home-oxygen-patient)

Generate Letters [3-9](#generate-letters)

4\. Billing [4-1](#billing)

Pre-Billing Discrepancy Report [4-2](#pre-billing-discrepancy-report)

Find Discrepancies that Affect Accurate Billing [4-2](#find-discrepancies-that-affect-accurate-billing)

Correct Discrepancies that Affect Accurate Billing [4-2](#correct-discrepancies-that-affect-accurate-billing)

Billing Transactions [4-4](#billing-transactions)

Create the Billing List [4-4](#create-the-billing-list)

Correct Data on a Patient Record [4-5](#correct-data-on-a-patient-record)

Correct Billing Data and/or Suspend Dollar Amts [4-7](#correct-billing-data-andor-suspend-dollar-amts)

Zero Out an Item [4-7](#zero-out-an-item)

Edit an Item [4-8](#edit-an-item)

Add an Item [4-8](#add-an-item)

Delete an Item [4-9](#delete-an-item)

Add a Patient to the Billing List [4-11](#add-a-patient-to-the-billing-list)

Delete a Patient from the Billing List [4-11](#delete-a-patient-from-the-billing-list)

Change the Quantity of an Item [4-12](#change-the-quantity-of-an-item)

Accept the Billing [4-13](#accept-the-billing)

View Only Accepted or Unaccepted Records [4-13](#view-only-accepted-or-unaccepted-records)

Unaccept the Billing [4-13](#unaccept-the-billing)

Post the Billing [4-14](#post-the-billing)

Sign Off on the Purchase Card [4-16](#sign-off-on-the-purchase-card)

View the 2319 [4-17](#view-the-2319)

Purchase Card Sign Off [4-19](#purchase-card-sign-off)

Verify Posted Billing Transactions [4-20](#verify-posted-billing-transactions)

5\. Reports [5-1](#reports)

Alphabetical List Home Oxygen Patients (by site) [5-2](#alphabetical-list-home-oxygen-patients-by-site)

Active Home Oxygen Patients (Alpha by Zip Code) [5-3](#active-home-oxygen-patients-alpha-by-zip-code)

Prescription Expiration Dates [5-4](#prescription-expiration-dates)

Inactive Home Oxygen Patients (by Inactive date) [5-5](#inactive-home-oxygen-patients-by-inactive-date)

Primary Item Report [5-6](#primary-item-report)

Monthly Home Oxygen Billing [5-7](#monthly-home-oxygen-billing)

New Patients [5-8](#new-patients)

Prescription Report [5-9](#prescription-report)

Pre-Billing Discrepancy Report [5-10](#pre-billing-discrepancy-report-1)

6\. Glossary [6-1](#glossary)

7\. Index [7-1](#index)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [New Administrative Home Oxygen Options](#new-administrative-home-oxygen-options)
  - [List Manager Functions](#list-manager-functions)
- [Setting Up the Site Parameters](#setting-up-the-site-parameters)
  - [Information Needed for the Site Parameters](#information-needed-for-the-site-parameters)
    - [Correspondence](#correspondence)
    - [Home Oxygen Vendors](#home-oxygen-vendors)
    - [Fund Control Points](#fund-control-points)
    - [Sequence Numbering of Prescriptions](#sequence-numbering-of-prescriptions)
  - [Site Parameters Enter/Edit Option](#site-parameters-enteredit-option)
- [# Entering Patient and Prescription Information](#entering-patient-and-prescription-information)
  - [## ## ## Add/Edit Home Oxygen Patient](#addedit-home-oxygen-patient)
    - [Add a New Patient](#add-a-new-patient)
    - [Edit the Patient's Eligibility](#edit-the-patients-eligibility)
    - [Activate the Patient](#activate-the-patient)
    - [Add a New Prescription](#add-a-new-prescription)
    - [Add or Edit a Billing Item](#add-or-edit-a-billing-item)
  - [Inactivate/Activate Oxygen Patient](#inactivateactivate-oxygen-patient)
    - [Inactivate a Home Oxygen Patient](#inactivate-a-home-oxygen-patient)
    - [Activate a Home Oxygen Patient](#activate-a-home-oxygen-patient)
  - [Generate Letters](#generate-letters)
- [# Billing](#billing)
  - [Pre-Billing Discrepancy Report](#pre-billing-discrepancy-report)
    - [Find Discrepancies that Affect Accurate Billing](#find-discrepancies-that-affect-accurate-billing)
    - [Correct Discrepancies that Affect Accurate Billing](#correct-discrepancies-that-affect-accurate-billing)
  - [Billing Transactions](#billing-transactions)
    - [Create the Billing List](#create-the-billing-list)
    - [Correct Data on a Patient Record](#correct-data-on-a-patient-record)
    - [Correct Billing Data and/or Suspend Dollar Amts](#correct-billing-data-andor-suspend-dollar-amts)
    - [Add a Patient to the Billing List](#add-a-patient-to-the-billing-list)
    - [Delete a Patient from the Billing List](#delete-a-patient-from-the-billing-list)
    - [Change the Quantity of an Item](#change-the-quantity-of-an-item)
    - [Accept the Billing](#accept-the-billing)
    - [View Only Accepted or Unaccepted Records](#view-only-accepted-or-unaccepted-records)
    - [Unaccept the Billing](#unaccept-the-billing)
    - [Post the Billing](#post-the-billing)
    - [Sign Off on the Purchase Card](#sign-off-on-the-purchase-card)
    - [View the 2319](#view-the-2319)
  - [Purchase Card Sign Off](#purchase-card-sign-off)
  - [Verify Posted Billing Transactions](#verify-posted-billing-transactions)
- [Reports](#reports)
  - [Alphabetical List Home Oxygen Patients (by site)](#alphabetical-list-home-oxygen-patients-by-site)
  - [Active Home Oxygen Patients (Alpha by Zip Code)](#active-home-oxygen-patients-alpha-by-zip-code)
  - [Prescription Expiration Dates](#prescription-expiration-dates)
  - [Inactive Home Oxygen Patients (by Inactive date)](#inactive-home-oxygen-patients-by-inactive-date)
  - [Primary Item Report](#primary-item-report)
  - [Monthly Home Oxygen Billing](#monthly-home-oxygen-billing)
  - [New Patients](#new-patients)
  - [Prescription Report](#prescription-report)
  - [Pre-Billing Discrepancy Report](#pre-billing-discrepancy-report-1)
- [Glossary](#glossary)
- [Index](#index)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Administrative Home Oxygen Module is exclusively an administrative system. It provides for the recording of patient information for reporting and invoice billing which can be used as a check against bills received from the contractor for each patient. The module facilitates the coordination of services when contractors change at the end of a contract cycle. It also provides correspondence support to remind patients when they need to renew their Home Oxygen prescriptions. 

The Administrative Home Oxygen module is mainly used to manage billing from the vendor, providing several benefits, including saving money by suspending erroneous charges and time by eliminating a manual review of the records. The module also provides information about the current prescription of the patient, and flags patients with special problems quickly.

Correspondence may be required by local VAMC Home Oxygen program policy. With this release, letters may be sent to patients when prescriptions are due to expire or when service is discontinued.

## New Administrative Home Oxygen Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add/Edit Home Oxygen Patient: This option allows you to add patients to the Prosthetics Patient file and document home oxygen prescription data and the equipment that is to be used by the patient.

Inactivate/Activate Oxygen Patient: If the patient is no longer receiving home oxygen or treatment has been interrupted for an extended length of time, inactivate the patient using this option. The option allows you to record a date of inactivation and a coded reason for the inactivation. This option is also used to re-activate a patient. Reactivating the patient changes the Home Oxygen Activation Date for the patient.

Generate Letters: This option generates a list of patients that meet the criteria (number of days prior to prescription expiry) for receiving a letter.

Billing Transactions: This option allows you to edit bills for a specific month, accept those transactions, post and sign-off on them.

Reports:

> Alphabetical List Home Oxygen Patients (by site): This is a listing of active home oxygen patients for a selected site. The report also shows the date the current prescription expires.

> Active Home Oxygen Patients (Alpha by Zip Code): This is a listing of active patients with their address information.

> Prescription Expiration Dates: This is a listing of active patients sorted by the expiration dates for their current prescriptions.

> Inactive Home Oxygen Patients (by Inactive date): This is a listing of inactive patients and the reason they were inactivated.

> Primary Item Report: This is a report of active patients listing the primary item, quantity of the item, and cost.

> Monthly Home Oxygen Billing: This report lists billings for all active home oxygen patients.

> New Patients: This is a report of all new patients for a selected date range.

> Prescription Report: This report includes HCPCS/items, quantity, cost, extended cost, and the fund control point.

> Pre-Billing Discrepancy Report: This report should be run and any discrepancies corrected prior to creating a billing list for a month. If there are any discrepancies for a patient, then that patient will not appear on the billing list.

Site Parameters Enter/Edit: This option is used to enter site specific information regarding default days to expiration for prescription, letters, vendors, and Fund Control Points.

Verify Posted Billing Transactions: This option posts all Home Oxygen billing transactions for a selected month for bills posted in IFCAP that were not also posted in Patient 2319 records. It will loop through all the records for the month and vendor entered.

Purchase Card Sign Off: Once a billing is accepted and posted, this option can be used to sign off on the billing.

## List Manager Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

List Manager is used in the Billing Transactions and Generate Letters options. Its functions provide the ability to move around between screens, search for selected pieces of information, and print the information on the screen(s). A list of the functions for each option can be obtained at the "Select ACTION" prompt by entering two question marks (??). The List Manager functions are shown in bold below.

<u>Billing Transactions Mar 04, 1999 14:19:56 Page: 1 of 29</u>

Billing Transactions for PROSVENDOR,ONE

for FEB 1999

<u>NAME SSN EL PRIMARY ITEM 910 OTHER SUSP TOTAL</u>

1\. PATIENT,ONE 0001 4 O2 TANK H SYSTEM 40.00 0.00 0.00 40.00

2\. PATIENT,TWO 0002 1 O2 CONCENTRATOR 325.00 300.00 0.00 625.00

3\. PATIENT,THREE 0003 4 O2 NEBULIZER/BUNN SYS 150.00 0.00 0.00 150.00

4\. PATIENT,FOUR 0004 4 O2 CONCENTRATOR 182.50 0.00 0.00 182.50

5\. PATIENT,FIVE 0005 4 O2 CONCENTRATOR 162.50 45.00 0.00 207.50

6\. PATIENT,SIX 0006 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

7\. PATIENT,SEVEM 0007 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

8\. PATIENT,EIGHT 0008 4 O2 CONCENTRATOR 182.50 330.00 0.00 512.50

9\. PATIENT,NINE 0009 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

10\. PATIENT,TEN 0010 4 O2 CONCENTRATOR 182.50 228.00 0.00 410.50

|                           |
|---------------------------|
| Enter ?? for more actions |

Select ACTION:Next Screen// ??

ET Edit Patient AP Add Billing Patient UB Unaccept Billing

EB Edit Billing CV Change View XB Post Billing

AB Accept Billing QE Quick Edit

23 Display 2319 SO Sign Off Purchase Card

The following actions are also available:

+ Next Screen FS First Screen SL Search List- Previous Screen LS Last Screen ADPL Auto Display(On/Off)UP Up a Line GO Go to Page QU QuitDN Down a Line RD Re Display Screen\> Shift View to Right PS Print Screen\< Shift View to Left PL Print ListNext Screen: Enter + to move to the next screen.

Previous Screen: Enter - to go back to the previous screen.

Up a Line: (Not used in this version)

Down a Line: (Not used in this version)

Shift View to Right: (Not used in this version)

Shift View to Left: (Not used in this version)

First Screen: Enter FS to return to the first screen.

Last Screen: Enter LS to go forward to the final screen.

Go to Page: Enter GO to select the screen number you want to see.

Re Display Screen: Enter RD to re-display the screen.

Print Screen: Enter PS to get a device to print what you see on the screen.

Print List: Enter PL to get a device to print the data on the screen.

Search List: Enter SL to find a specific piece of information:

> Select ACTION:Quit// sl SL

> Search for: OXYGEN

> Billing Transactions Jul 12, 1999 11:02:32 Page: 1 of 1

> Billing Transactions for PROSVENDOR,TWO

> for JUN 1999

> NAME SSN EL PRIMARY ITEM 910 OTHER SUSP TOTAL

> 1\. PATIENT1,ONE 0001 4 PROSVENDOR, FOUR 1755.00 0.00 0.00 1755.00

> 2\. PATIENT1,two 0002 4 OXYGEN HOSE UNION 518.75 0.00 0.00 518.75

> 3\. PATIENT1,THREE 0003 4 PROSVENDOR, FOUR 320.00 0.00 0.00 320.00

> 4\. PATIENT1,FOUR 0004 4 OXYGEN 0.00 1000.00 0.00 1000.00

> 5\. PATIENT1,FIVE 0005 1 OXYGEN 90.00 0.00 0.00 90.00

> 6\. PATIENT1,SIX 0006 1 OXYGEN HOSE UNION 80.00 0.00 0.00 80.00

> Your search criteria is highlighted on the screen.

Auto Display (On/Off): Enter ADPL to either display or hide the Letter or Billing actions you can take.

<u>Billing Transactions Mar 04, 1999 14:19:56 Page: 1 of 29</u>

Billing Transactions for PROSVENDOR,ONE

for FEB 1999

<u>NAME SSN EL PRIMARY ITEM 910 OTHER SUSP TOTAL</u>

1\. PATIENT,ONE 0001 4 O2 TANK H SYSTEM 40.00 0.00 0.00 40.00

2\. PATIENT,TWO 0002 1 O2 CONCENTRATOR 325.00 300.00 0.00 625.00

3\. PATIENT,THREE 0003 4 O2 NEBULIZER/BUNN SYS 150.00 0.00 0.00 150.00

4\. PATIENT,FOUR 0004 4 O2 CONCENTRATOR 182.50 0.00 0.00 182.50

5\. PATIENT,FIVE 0005 4 O2 CONCENTRATOR 162.50 45.00 0.00 207.50

6\. PATIENT,SIX 0006 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

7\. PATIENT,SEVEN 0007 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

8\. PATIENT,EIGHT 0008 4 O2 CONCENTRATOR 182.50 330.00 0.00 512.50

9\. PATIENT,NINE 0009 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

10\. PATIENT,TEN 0010 4 O2 CONCENTRATOR 182.50 228.00 0.00 410.50

|                           |
|---------------------------|
| Enter ?? for more actions |

> Select ACTION:Next Screen// ADPL ADPL

> Do you wish to turn auto-display 'ON' for this menu? NO// YES

<u>Billing Transactions Mar 04, 1999 14:19:56 Page: 1 of 29</u>

Billing Transactions for PROSVENDOR,ONE

for FEB 1999

<u>NAME SSN EL PRIMARY ITEM 910 OTHER SUSP TOTAL</u>

1\. PATIENT,ONE 0001 4 O2 TANK H SYSTEM 40.00 0.00 0.00 40.00

2\. PATIENT,TWO 0002 1 O2 CONCENTRATOR 325.00 300.00 0.00 625.00

3\. PATIENT,THREE 0003 4 O2 NEBULIZER/BUNN SYS 150.00 0.00 0.00 150.00

4\. PATIENT,FOUR 0004 4 O2 CONCENTRATOR 182.50 0.00 0.00 182.50

5\. PATIENT,FIVE 0005 4 O2 CONCENTRATOR 162.50 45.00 0.00 207.50

6\. PATIENT,SIX 0006 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

7\. PATIENT,SEVEN 0007 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

8\. PATIENT,EIGHT 0008 4 O2 CONCENTRATOR 182.50 330.00 0.00 512.50

9\. PATIENT,NINE 0009 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

10\. PATIENT,TEN 0010 4 O2 CONCENTRATOR 182.50 228.00 0.00 410.50

|                           |
|---------------------------|
| Enter ?? for more actions |

> ET Edit Patient AP Add Billing Patient UB Unaccept Billing

> EB Edit Billing CV Change View XB Post Billing

> AB Accept Billing QE Quick Edit

> 23 Display 2319 SO Sign Off Purchase Card

> Select ACTION:Quit//

Quit: Enter QU to return to exit the option.

# Setting Up the Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before setting up the site parameters, you need to make decisions concerning correspondence and sequence numbering of prescriptions. You also need to gather information on Fund Control Points and vendors.

## Information Needed for the Site Parameters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Correspondence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Your medical center policy may require that letters be sent under certain circumstances to patients receiving home oxygen and/or to the contractor: e.g., when a patient is added to the program, when a prescription is about to expire, and/or when the service is discontinued. If you want to automate this process, the Home Oxygen Module provides the means. Add the letters to the Prosthetic software using the option Add/Edit Correspondence Skeleton Letter found under the Correspondence menu of the Prosthetic Official's Menu. This should be done prior to editing the site parameters in the option Site Parameters Enter/Edit under the Home Oxygen Main Menu. Here's an example of how use the Add/Edit Correspondence Skeleton Letter option:

> Select Correspondence Option: Add/Edit Correspondence Skeleton Letter

> Select PROS LETTER NAME: PRESCRIPTION EXPIRATION

> Are you adding 'PRESCRIPTION EXPIRATION' as a new PROS LETTER (the 7TH)? No// Y (Yes)

> NAME: PRESCRIPTION EXPIRATION// \<RET\>

> LETTER TEXT:

> No existing text

> Edit? NO// YES

> ==\[ WRAP \]==\[ INSERT \]===========\< LETTER TEXT \>=========\[ \<PF1\>H=Help \]====

> Enter the content of the body of your letter here.

> \<=====T=======T=======T=======T=======T=======T=======T=======T=======T=\>=====T

> Is this a Denial type of letter? No// \<RET\> (No)

> Once you have created your letters, determine the following about each letter for the Home Oxygen Site Parameters:

1.  Give the letter one of the following letter codes:

A LETTER 1

B LETTER 2

C LETTER 3

2.  Determine the number of days prior to the expiration (Days to Expiry) of the prescription that the letter should be created. Examples: A letter to remind a patient to renew a prescription might be sent 30 days prior to the expiration of the prescription. In the case of a welcome letter, enter 0 days to create the letter on the day the prescription is entered.
3.  Should the letter be auto-generated or would you rather manage the creation of letters? Auto-generating means that whenever you run the Generate Letters option, a list of patients is created who meet the criteria for the number of days prior the prescription expiration. Letters can be automatically generated from that list.
4.  Do you want a header printed on the letter? If you use pre-printed paper that has a letterhead, then you would answer No to this question. If you want a header to print along with the letter content, then you would answer Yes to this question.

> Worksheet for defining letter management

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 11%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Long Name</strong></td>
<td><strong>Letter Code</strong></td>
<td><p><strong>Days to</strong></p>
<p><strong>Expiry</strong></p></td>
<td><p><strong>Auto-</strong></p>
<p><strong>Gen</strong></p>
<p><strong>Y/N</strong></p></td>
<td><p><strong>Print</strong></p>
<p><strong>Header</strong></p>
<p><strong>Y/N</strong></p></td>
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
<td></td>
</tr>
</tbody>
</table>

### Home Oxygen Vendors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Create a list of the vendors your site uses for providing home oxygen equipment.

### Fund Control Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Create a list of the Fund Control Points (FCP) used for Home Oxygen. There should be at leastone FCP for 910. Many sites will also have a local number for the liquid gas.

> To obtain the FCPs, you can use the Prosthetics package option, Create a No-Form Daily Record, under the Enter New Request menu in Purchasing. At the "Select CONTROL POINT" prompt, enter two question marks to obtain a list of the FCPs used by the Prosthetics and Sensory Aids Service at your site.

### Sequence Numbering of Prescriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Those sites with local policy that defines the length of time the first, second, third, etc. prescriptions are good, may want to take advantage of a default prescription expiry date. Sequence numbering starts with 1 and increases by one for each new prescription. If the first prescription (sequence number 1) at your site cannot exceed 3 months, then its Default Days to Expiration would be 90 (days). If the second and all further prescriptions cannot exceed 6 months, then sequence number 2 and all the following sequence numbers would be given 180 for Default Days to Expiration. If you choose to use this functionality, adding 5-6 sequence numbers should be sufficient. If you choose not to use default dates, the prescription's "Expiration Date" field can be entered by hand.

## Site Parameters Enter/Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have all the above defined for each site, use the Site Parameters Enter/Edit option and enter the information. The following shows the order of the prompts and a brief description of what you should enter:

> Site: Select the site for the parameters you are defining.

> Prescription Sequence Number: Start with 1 and increment by 1 for each sequence number you enter. The first prescription when a patient is activated is sequence number 1, the second sequence number 2, etc. You are not required to use this functionality and may bypass the prompt by pressing the \<ret\> key.

> Default Days to Expiration: If you enter a Sequence number, then you will be asked to enter the Default Days to Expiration. The program will look at the date entered for a prescription, check the sequence number of the prescription, add the Default Days to Expiration to the prescription date, and come up with a default response to the Expiration Date prompt for the prescription. This default response may be accepted or changed.

> Fund Control Point: Enter each Fund Control Point used by your home oxygen program. These Fund Control Points will be displayed on reports that show statistics by Fund Control Point.

> PSAS?: Is this Fund Control Point a Prosthetics Sensory and Aids Service FCP? Enter Yes if the FCP is 910.

> Enter No for all local FCPs.

> Home Oxygen Vendors: Enter each vendor that provides home oxygen services for your patients.

> Home Oxygen Letter: Enter the name of each letter you created using the Add/Edit Correspondence Skeleton Letter option.

> Letter Code: Select one of the following codes:

> A LETTER 1

> B LETTER 2

> C LETTER 3

> Days to Prescription Expiry: Enter the number of days prior to the expiration of the prescription that you want to print the letter to send to the patient. Examples: A letter to remind a patient to renew a prescription might be sent 30 days prior to the expiration of the prescription. In the case of a welcome letter, enter 0 days to create the letter on the day the first prescription is entered.

> Autogenerate Letter: If you want to be able to obtain a list of patients who meet the criteria for receiving this letter you just defined, enter YES at this prompt.

> Print Letter Header: For those sites that print letters on paper already containing a letterhead, enter No at this prompt. For those sites that want to use the on-line letterhead, enter Yes at this prompt.

# # Entering Patient and Prescription Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to bill patients, the program must have information concerning the patient, the patient's prescriptions, and the items being billed to the patient. It needs to know when a patient starts on the program and when the patient is no longer active.

This chapter shows you how to do the following:

- Add patients to the program (Add/Edit Home Oxygen Patient option)
- Enter or change prescription information (Add/Edit Home Oxygen Patient option)
- Create or change the billing equipment list for a patient (Add/Edit Home Oxygen Patient option)
- Inactivate patients from the program (Inactivate/Activate Oxygen Patient option)
- Generate letters (Generate Letters option)

<span id="ICD10homeoxypatientwarning" class="anchor"></span>Note: Upon the ICD-10 activation date, on the *Add/Edit Home Oxygen Patient* option, if you select an existing Item and that Item contains an ICD code that is inactive based on the Start Date of the currently selected prescription, the software then issues a warning and prompts you how you should proceed.

You have three options:

1.  Select a different item with no ICD code or with an active ICD code.
2.  Enter a new item.
3.  Proceed with this item. If the user proceeds with this item, the existing ICD Diagnosis code will be DELETED. The user may then enter an active ICD Diagnosis code or they may leave the ICD Diagnosis field blank.

Example: Warning for *Add/Edit Home Oxygen Patient* Option

The following items are already in the patient's template:

Item Description Vendor ICD CS+

\* 1 HEAD GEAR-CPAP-SOFT PROSVENDOR ONE 784.0 9

2 NECK COOLER, STEELE PROSVENDOR ONE 847.0 9

3 NECKLOOP POWERED AMPLIFIED PROSVENDOR ONE

\* = Primary Item

CS = Code Set for ICD Diagnosis code

\+ = Item with active ICD code on start date of prescription

Select ACTION: (A/D/E): Edit

Select an ITEM: (1-3): 1 \* 1 HEAD GEAR-CPAP-SOFT

This item contains the ICD Diagnosis Code: 784.0 which was inactive based

on the start date of the currently selected prescription.

You may 1)select a different item with no ICD code or with an active ICD code,

2)enter a new item or

3)proceed with this item. If you proceed with this item, the existing

ICD Diagnosis code 784.0 will be DELETED.

You may then enter an active ICD-10 Diagnosis code or you may leave

the ICD Diagnosis field blank.

Do you wish to continue?

## ## ## ## Add/Edit Home Oxygen Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to:

> Add a new patient

> Edit the patient's eligibility

> Activate the patient

> Add a new prescription

> Add or edit a billing item

There are three basic sets of data covered in this option.

> The first set is demographic in nature and includes the prosthetics site, the date the patient was activated/reactivated to the Home Oxygen program, and the patient's eligibility.

> A second set of data is for each prescription and includes the first and subsequent prescription dates, a description what was ordered for the patient, and the prescription expiration date.

> The third set of data is called a "billing equipment list". The billing equipment list is used to record the items that are provided on a monthly basis to the patient. Information that will allow costs to flow through to the correct obligation such as the fund control point (FCP) number will be included as well.

The following shows the order of the prompts and a brief description of what you should enter:

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Enter a site.

Prosthetics Patient Name: Enter the patient name in the usual manner: LAST,FIRST or first initial last name plus last 4 digits of the SSN, etc.

> **NOTE:** This prompt also accepts an item name. If you enter a single letter or the item name, the program searches through a list of items that have been given to patients.

### Add a New Patient 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home Oxygen Module will first search the Prosthetics Patient file for the patient. If the patient isn't there, it will search the VISTA Patient file and ask if you want to add the patient as a new Prosthetics Patient. Enter Yes to add the patient as a new Prosthetics Patient.

Prosthetics Patient Station: If this patient is a new Prosthetics Patient, you must also enter a site for the patient.

### Edit the Patient's Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Home Oxygen Eligibility: Enter the patient's eligibility for home oxygen services. Note: When selecting NSC/OP you may see additional prompts.

1 SC/OP

2 SC/IP

3 NSC/IP

4 NSC/OP

Home Oxygen Contract Location: Enter the site that will be administering the contract for the home oxygen.

### Activate the Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Home Oxygen Activation Date: Enter the latest date the patient was activated as a home oxygen patient. This may be the first date on the program or the most recent activation date following an extended time off the program. An exact date is not required. You may enter a month, day and year or just a month and year. (E.g., 2/2/99, 2/99) Each Activation Date begins a sequence of prescriptions. If you are using this functionality, the earliest prescription date is sequence number 1.

### Add a New Prescription

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Home Oxygen Prescription Date: Enter the prescription date here.

> **NOTE:** It is strongly suggested that you do not delete prescription dates.

If this is a new prescription, you will be asked if you are adding a new one. Answer Yes.

Expiration Date: Enter the expiration date of the prescription. If in the site parameters for the Home Oxygen Module, prescription sequence numbers and default days to expiration were defined, then you may see a default answer here. You may accept the default date or edit it.

Description: Enter a description of how often to use, flow rate, how administered, etc. according to the prescription.

Example: 2 LPM O2 by N/C 24hr/d w/conc 6E, 2D, H

> **NOTE:** If no equipment has been entered for this patient, you will receive a message stating:

No items found, please enter PRIMARY ITEM

> Otherwise, a list of the patient's oxygen equipment appears next with the primary equipment item starred (\*). You have a choice of adding a new item, deleting an item or editing an item.

> The following items are already in this patient's template:

> \* 1 PROSVENDOR, FOUR PROSVENDOR, THREE

> 2 OXYGEN PROSVENDOR, THREE

> \* = Primary Item

> Select ACTION: (A/D/E):

### Add or Edit a Billing Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pros Item Master Name: Select an item from the Prosthetics Master Item list. If this is the first item added, it should be the Primary item (primary component or system) that the patient will be receiving. The primary item is sometimes used on reports in lieu of listing all items.

Primary Item: For each additional item entered, you will be asked if it is the primary item. If you have already entered a primary item, then answer NO at this prompt.

HCPCS Code: Enter the HCPCS code for the item selected.

Vendor: Enter the vendor that will be supplying the equipment and services.

Quantity: Enter the number authorized to be issued to the patient during the month. Example: For liquid oxygen, enter the number of pounds of liquid.

Unit Cost: Enter the cost for each unit issued. Type a dollar amount with 2 decimal digits.

> Note: The program will use the Quantity and Unit Cost to calculate the total amount for billing.

Unit of Issue: Select a unit of issue.

ICD9 or ICD10 Code: <span id="ICD10codeupdate1" class="anchor"></span>Enter the diagnosis that is most closely related to the reason this patient is receiving oxygen.

Remarks: Enter any further information about this patient, up to 30 characters. This information is displayed on the patient's 2319 record on screen 8.

Example: Equip used in conj with CPAP

Item Type: Is this an initial issue ( I ), replacement ( R ), or repair ( X )? If this is a 910 issue, enter X. If this is out of a local FCP, enter either I or R.

Fund Control Point: Through which FCP will this purchase be handled? Enter the FCP here.

At this point you may edit the data you entered, add a new item for this prescription, or delete an item.

Example:<span id="ICD10screen1" class="anchor"></span>

Select Home Oxygen Main Menu Option: Add/Edit Home Oxygen Patient

Select PROSTHETICS PATIENT NAME: PROSPATIENT,ONE 5001AC 1-12-42 0001

12233 YES SC VETERAN

HOME OXYGEN ELIGIBILITY: SC/OP//

HOME OXYGEN CONTRACT LOCATION: ALBANY//

HOME OXYGEN ACTIVATION DATE: MAR 1,2000//

Select HOME OXYGEN PRESCRIPTION DATE: Jan 01, 2014// 3/1/2000 MAR 01, 2000

DATE: MAR 1,2000//

EXPIRATION DATE: MAR 1,2000//

DESCRIPTION:

Adding new ICD9 code.

Edit? NO//

The following items are already in this patient's template:

\* 1 ACETAMINOPHEN W/CODEINE 30MG TAB PROSVENDOR ONE

2 WHEELCHAIR LIGHTWEIGHT PROSVENDOR TWO

3 COLOSTOMY BAGS PROSVENDOR ONE

4 ACETAMINOPHEN W/CODEINE 30MG TAB PROSVENDOR ONE

5 NECK BRACE PROSVENDOR TWO

\* = Primary Item

Select ACTION: (A/D/E): Edit

Select an ITEM: (1-5): 2 2 WHEELCHAIR LIGHTWEIGHT

PRIMARY ITEM: NO//

ITEM: COOKIE//

HCPCS CODE: A4365//

VENDOR: VENDOR TWO //

QUANTITY: 1//

UNIT COST: 1.25//

UNIT OF ISSUE: EA//

ICD10 Diagnosis code: F14.19// 100.0

No data found

ICD10 Diagnosis code: F14.19// F14

20 matches found

1\. F14.10 Cocaine Abuse, Uncomplicated

2\. F14.12- Cocaine abuse with intoxication

3\. F14.14 Cocaine Abuse with Cocaine-Induced Mood Disorder

4\. F14.15- Cocaine abuse with cocaine-induced psychotic

disorder

5\. F14.18- Cocaine abuse with other cocaine-induced disorder

6\. F14.19 Cocaine Abuse with unspecified Cocaine-Induced

Disorder

7\. F14.20 Cocaine Dependence, Uncomplicated

8\. F14.21 Cocaine Dependence, in Remission

Press \<RETURN\> for more, "^" to exit, or Select 1-8: 2

4 matches found

1\. F14.120 Cocaine Abuse with Intoxication, Uncomplicated

(ICD-10-CM F14.120)

2\. F14.121 Cocaine Abuse with Intoxication with Delirium

(ICD-10-CM F14.121)

3\. F14.122 Cocaine Abuse with Intoxication with Perceptual

Disturbance (ICD-10-CM F14.122)

4\. F14.129 Cocaine Abuse with Intoxication, unspecified

(ICD-10-CM F14.129)

Select 1-4: 2

ICD10 Diagnosis code: F14.121

ICD10 Diagnosis description: Cocaine Abuse with Intoxication with Delirium

(ICD-10-CM F14.121)

REMARKS: ICD10 Edit & change//

ITEM TYPE: Initial Issue//

Select FUND CONTROL POINT: ^

## Inactivate/Activate Oxygen Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to:

### Inactivate a Home Oxygen Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Activate a Home Oxygen Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inactivate patients for any of the following reasons:

Discontinued by Patient

Rx Expired

MD Discontinued

Patient Deceased

Inpatient Status

Entered in Error

Note on Inpatient Status: For those patients who are often admitted as an inpatient to manage their condition but whose stay is generally not lengthy, they do not need to be inactivated. Use the Inpatient Status only when it is apparent that their stay will be lengthy and that they may not return to the Home Oxygen Program.

When an Inactivation Date and Inactivation Reason are recorded for a patient, the patient is inactivated causing the last prescription in the patient's file to be canceled. <span class="mark"></span>

When a patient is reactivated, the Inactivation date is deleted. When the inactivation date is deleted, the reason for inactivation is automatically deleted by the system. The prescription will remain unchanged unless it is directly edited in the Add/Edit Home Oxygen Patient option.

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Enter a site.

Prosthetics Patient Name: Enter the patient name in the usual manner: LAST,FIRST or first initial last name plus last 4 digits of the SSN, etc. Note: If you enter a single letter, the program searches through a list of items given to patients.

Home Oxygen Inactivation (or Activation) Date: Enter the date the patient is either inactivated or activated.

Home Oxygen Inactivat. Reason: If the patient is being inactivated, this prompt will appear. Select the reason the patient is being inactivated.

D Discontinued by Patient

R Rx Expired

M MD Discontinued

P Patient Deceased

I Inpatient Status

E Entered in Error

Example:

SITE: HINES ISC VAMC// \<ret\> 499

Select PROSTHETICS PATIENT NAME: PATIENT1,SEVEN SUPPORT ISC 01-05-32

000000017 NO EMPLOYEE

Are you sure you want to inactivate PROSPATIENT1,ONE ?? NO// y YES

HOME OXYGEN INACTIVATION DATE: TODAY// \<ret\> (JUL 01, 1999)

HOME OXYGEN INACTIVAT. REASON: ??

Enter a code (P, R, M, D, I, or E) for the reason for discontinuance of home

oxygen therapy.

Choose from:

D DISCONTINUED BY PATIENT

R Rx EXPIRED

M MD DISCONTINUED

P PATIENT DECEASED

I INPATIENT STATUS

E ENTERED IN ERROR

HOME OXYGEN INACTIVAT. REASON: p PATIENT DECEASED

Select PROSTHETICS PATIENT NAME: \<ret\>

## Generate Letters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you set up your site parameters to auto-generate your letters, this option will build of list of patients who meet the criteria for receiving each type of letter (e.g., recently activated, within so many days of the expiration of their prescription, about to be discontinued from the home oxygen program).

> **NOTE:** Once you print a letter for a patient, the patient will no longer appear on the list for that type of letter. So if you print a welcome letter for a patient, that patient will no longer appear as needing a welcome letter. Use the option Print/Display Patient Correspondence Letter under the Correspondence menu within the Prosthetic Official's Menu if you need to reprint the letter.

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Enter a site.

If your current list is not so current, then generate a new list as shown here. This will place any patients on the list that have met the criteria since the last list was generated:

> Do you wish to manage the current list? No// \<ret\> (No)

> Do you wish to generate a new list which will discard any edits? No// Y (Yes)

<u>RMPO LETTER TYPE Mar 09, 1999 08:57:06 Page: 1 of 1</u>

HINES ISC VAMC

HOME OXYGEN PATIENT LETTER TYPE LIST

<u>Description Number of Patients on List</u>

1 LETTER 1 3

2 LETTER 2 5

3 LETTER 3 1

|                           |
|---------------------------|
| Enter ?? for more actions |

ML Manage Letter List LT Print Letters

Select Action: Quit// LT Print Letters

Select letter type line \#: (1-3): 1

> ML Manage Letter List: This functionality generates a new list, adding any patients that meet the criteria.

> Select Action: Quit// ml Generate Letter List

> Select letter type line \#: (1-3): 2

> Generating a new list... .

> DONE GENERATING A NEW LIST...

> LT Print Letters: This functionality lets you add patients, print the letters for all or selected patients, and delete entries.

> Select Action: Quit// LT Print Letters

> Select letter type line \#: (1-3): 1

> Processing....

<u>RMPO LETTER Mar 09, 1999 08:57:24 Page: 1 of 1</u>

WELCOME TO HOME OXYGEN

HOME OXYGEN PATIENT LETTER LIST

<u>Patient SSN Primary Item Activation Date Rx Expiry</u>

1 PATIENT1,EIGHT 000-00-0008 O2 CONCENTRATOR MAR 06, 1999 JUN 04, 1999

2 PATIENT1,NINE 000-00-0009 O2 CONCENTRATOR MAR 08, 1999 JUN 06, 1999

3 PATIENT1,TEN 000-00-0110 O2 CONCENTRATOR MAR 08, 1999 JUN 06, 1999

|                           |
|---------------------------|
| Enter ?? for more actions |

AP Add Patient to the list PP Print a letter for one patient

DE Delete List Entry X Exit to Letter

AL Print all letters

> AP Add Patient to the list: Use this action if you want to add a patient to the list to receive a letter.

> Select Action: Quit// ap Add Patient to the list

> Select PROSTHETICS PATIENT NAME: NAME,PATIENT

> DE Delete List Entry: This allows you to delete selected entries.

> Select Action: Quit// DE Delete List Entry

> Enter lines to delete: (1-2): 1

> AL Print All Letters: This sends all the letters in the list to a selected Device.

> Select Action: Quit// AL Print all letters

> DEVICE: HOME//

> PP Print a letter for one patient: You may send a letter for one or more selected patients to a selected Device. Enter your selections singly or in a range (e.g., 3,6,7,8 or 3,6-8, etc.)

> Select Action: Quit// PP Print a letter for one patient

> Enter a list or range of numbers (1-2): 1

> DEVICE: HOME//

Device: Enter a printer name. This will not allow you to print to the screen or to a slave printer.

In the following example letter, the header VAMC address information is taken from the Prosthetics Site Parameters file.

HINES ISC VAMC

BUILDING \#37

HINES, IL 60141

MAR 11,1999

PROSPATIENT2,ONE In Reply Refer To: HINES ISC VAMC/121

SSN: 000-00-0021

BELLWOOD, ILLINOIS 60611

4946

Current Home Oxygen Rx#: 1

Rx Expiration Date: JUN 6,1999

Dear Mr. PROSPATIENT2,ONE

Welcome to the Home Oxygen Program

This is the welcome letter containing routine information for any patient

entering the program. The contents of this letter are specific to your

site. It is created prior to editing the letter information in the site

parameters (Site Parameters Enter/Edit) for Home Oxygen.

Prosthetics Service

To help you move around through your letter list on any of the Generate Letters screens, there are a number of options available to you. Enter two question marks at the "Select Action" prompt to see them. This functionality is discussed in the Introduction under List Manager Functions.

# # Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a number of activities associated with billing. This chapter explains how to do the following:

- Find discrepancies that will affect accurate billing (Pre-Billing Discrepancy Report option)
- Correct the discrepancies that affect accurate billing (See Pre-Billing Discrepancy Report)
- Create a billing list (Billing Transactions option)
- Add patients to the billing list (Billing Transactions option)
- Edit patient data after the billing list is created (Billing Transactions option)
- Suspend dollar amounts for an item (Billing Transactions option)
- Complete/accept the billing (Billing Transactions option)
- Sign off the purchase card (Billing Transactions or Purchase Card Sign Off options)
- Verify that everything went okay with the posted billing (Verify Posted Billing Transactions option)

## Pre-Billing Discrepancy Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Always run this report and correct any discrepancies found prior to using the option Billing Transactions. If discrepancies remain unfixed, the patient will not be added to the billing list which can only be created once a month for each vendor.

### Find Discrepancies that Affect Accurate Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Entering "?" will bring up a list of sites. Select a site.

Billing Month: Enter the month and year you want shown in the report. Examples: February 1999, Feb 99, 2/99, 0299, 2-99.

Device: Hit the \<ret\> key to bring the report to your screen or enter the name of a printer to obtain a hard copy report.

HOME OXYGEN PRE-BILLING REPORT MAR 3,1999 10:20 PAGE 1

Name SSN Reason

--------------------------------------------------------------------------------

PROSPATIENT2,TWO 0022 No RX on file

### Correct Discrepancies that Affect Accurate Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following describes the discrepancy and tells you how to correct it.

Different Home Oxygen Contract Location: The Site you enter at the first prompt in this option, is not the same as the Contract Location for the patient shown in the report. If the contract location should be the same, change the location using the Add/Edit Home Oxygen Patient option.

No Home Oxygen Information: There is no eligibility entered for the patient. Enter the patient's eligibility and any other missing home oxygen information using the Add/Edit Home Oxygen Patient option.

Deactivated: The patient was inactivated prior to the billing period. If the patient needs to be reactivated, use the Inactivate/Activate Oxygen Patient option.

No RX on file: The patient has no prescription on file. Enter prescription information using the Add/Edit Home Oxygen Patient option. If the patient is not participating in the program, you may want to inactivate the patient using the Inactivate/Activate Oxygen Patient option.

RX expires prior to billing period: The prescription expired before the selected billing period. If the patient has a new prescription for the period, use the Add/Edit Home Oxygen Patient option to enter the prescription. If not, you may want to inactivate the patient using the Inactivate/Activate Oxygen Patient option.

No items on file: The patient's record shows no items to be billed. Use the Add/Edit Home Oxygen Patient option to add items for the patient.

No items for vendor: There is a vendor attached to the patient record but no item. Use the Add/Edit Home Oxygen Patient option to edit the item for the patient.

## Billing Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Run the Pre-Billing Discrepancy Report under the Reports menu to find any records that lack complete or up-to-date information. Correct those discrepancies prior to using this Billing Transactions option. Any incomplete records will not appear on the billing list. The billing list can only be generated once a month for each vendor.

The main purpose of the Home Oxygen Module is to help you manage the billing. This option produces a list of patients that received oxygen therapy over a selected month from a specified vendor. You can use this option to do a number of things, including edit the patient or billing record, accept or unaccept the billing, display the 2319, post the billing, and sign off using a purchase card or 1358.

### Create the Billing List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Enter a site.

Billing Month: Enter the month you want the bill to cover, e.g., 2-1999, 2-99, Feb 99 for February 1999.

Vendor: Select the vendor for which you want the list generated.

A screen similar to the following will appear:

<u>Billing Transactions Mar 04, 1999 14:19:56 Page: 1 of 29</u>

Billing Transactions for PROSVENDOR, THREE

for FEB 1999

<u>NAME SSN EL PRIMARY ITEM 910 OTHER SUSP TOTAL</u>

1\. PATIENT,ONE 0001 4 O2 TANK H SYSTEM 40.00 0.00 0.00 40.00

2\. PATIENT,TWO 0002 1 O2 CONCENTRATOR 325.00 300.00 0.00 625.00

3\. PATIENT,THREE 0003 4 O2 NEBULIZER/BUNN SYS 150.00 0.00 0.00 150.00

4\. PATIENT,FOUR 0004 4 O2 CONCENTRATOR 182.50 0.00 0.00 182.50

5\. PATIENT,FIVE 0005 4 O2 CONCENTRATOR 162.50 45.00 0.00 207.50

6\. PATIENT,SIX 0006 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

7\. PATIENT,SEVEN 0007 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

8\. PATIENT,EIGHT 0008 4 O2 CONCENTRATOR 182.50 330.00 0.00 512.50

9\. PATIENT,NINE 0009 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

10\. PATIENT,TEN 0010 4 O2 CONCENTRATOR 182.50 228.00 0.00 410.50

|                           |
|---------------------------|
| Enter ?? for more actions |

Select ACTION:Next Screen// ??Note: Entering ?? displays the other options available including the List Manager options for moving about and printing the screens. For information about the List Manager options (+, -, UP, DN, etc.), see List Manager Functions in the Introduction.

  
Billing Actions

There are a number of actions that you can take while in billing. The following information describes each of the actions.

ET Edit Patient AP Add Billing Patient DP Delete Patient Billing

EB Edit Billing CV Change View UB Unaccept Billing

AB Accept Billing QE Quick Edit XB Post Billing

23 Display 2319 SO Sign Off Purchase Card

### Correct Data on a Patient Record

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ET Edit Patient: If you create the billing list and then discover that some items are not covered in the bill for a patient, you can use this function to edit the information in the patient's record. This option only lets you correct information for patients already on the billing list.

> Note: If the patient does not appear on the billing list, run the Pre-Billing Discrepancy report to find out what is missing and correct the record. Then use the Add Billing Patient action described below to add the patient to the list.

> Example: In the following list, the user notices that the amount for an item is not showing due to the vendor not being defined for that item. This was determined by using the Pre-Billing Discrepancy report. We can use Edit Patient to add the vendor and correct any other information that is not complete.

<u>Billing Transactions Jul 04, 1999 14:19:56 Page: 1 of 29</u>

Billing Transactions for PROSVENDOR, THREE

for JUN 1999

<u>NAME SSN EL PRIMARY ITEM 910 OTHER SUSP TOTAL</u>

1\. PATIENT,ONE 0001 4 O2 TANK H SYSTEM 40.00 0.00 0.00 40.00

2\. PATIENT,TWO 0002 1 O2 CONCENTRATOR 325.00 300.00 0.00 625.00

3\. PATIENT,THREE 0003 4 O2 NEBULIZER/BUNN SYS 150.00 0.00 0.00 150.00

4\. PATIENT,FOUR 0004 4 O2 CONCENTRATOR 182.50 0.00 0.00 182.50

5\. PATIENT,FIVE 0005 4 O2 CONCENTRATOR 162.50 45.00 0.00 207.50

6\. PATIENT,SIX 0006 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

7\. PATIENT,SEVEN 0007 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

8\. PATIENT,EIGHT 0008 4 O2 CONCENTRATOR 182.50 330.00 0.00 512.50

9\. PATIENT,NINE 0009 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

10\. PATIENT,TEN 0010 4 O2 CONCENTRATOR 182.50 228.00 0.00 410.50

|                           |
|---------------------------|
| Enter ?? for more actions |

Select ACTION:Next Screen// E

> 1 Edit Billing

> 2 Edit Patient

> CHOOSE 1-2: 2 Edit Patient

> Enter a list or range of numbers (1-6): 4

> EDITING PROSPATIENT2,THREE...

> HOME OXYGEN ELIGIBILITY: NSC/OP// \<ret\>

> HOME OXYGEN CONTRACT LOCATION: HINES ISC VAMC// \<ret\>

> HOME OXYGEN ACTIVATION DATE: JAN 29,1999// \<ret\>

> Select HOME OXYGEN PRESCRIPTION DATE: 5-1-1999// \<ret\>

> DATE: MAY 1,1999// \<ret\>

> EXPIRATION DATE: OCT 28,1999// \<ret\>

> DESCRIPTION:

> No existing text

> Edit? NO// \<ret\>

> The following items are already in this patient's template:

> \* 1 O2 CONCENTRATOR PROSVENDOR, THREE

> 2 OXYGEN CONTENTS LIQ PER/UNIT *\<\< VENDOR NOT DEFINED \>\>*

> \* = Primary Item

> Select ACTION: (A/D/E): e Edit

> Select an ITEM: (1-2): 2 OXYGEN CONTENTS LIQ PER/UNIT

> PRIMARY ITEM: NO// \<ret\>

> ITEM: OXYGEN CONTENTS LIQ PER/UNIT // \<ret\>

> HCPCS CODE: E0442 OXYGEN CONTENTS LIQ PER/UNIT

> VENDOR: PROSVENDOR, THREE PH:555-555-5555 NO: 71608

> ORD ADD:200 VENDOR DRIVE FMS:

> VENDOR, IL 60048 CODE: FAX:

> ...OK? Yes// \<ret\> (Yes)

> QUANTITY: (nn)

> UNIT COST: (\$\$)

> UNIT OF ISSUE: LB POUND

> <span class="mark">ICD9 CODE: 416.8 CHR PULMON HEART DIS NEC</span>

> REMARKS: \<ret\>

> ITEM TYPE: X Repair

> Select FUND CONTROL POINT: 913 PROSTHETIC SUPPLIES

> The following items are already in this patient's template:

> 1 CONCENTRATOR PROSVENDOR, THREE

> \* 2 OXYGEN CONTENTS, GASEOUS, PE PROSVENDOR, THREE

> \* = Primary Item

> Select ACTION: (A/D/E): \<ret\>

<u>Billing Transactions Jul 04, 1999 14:19:56 Page: 1 of 29</u>

Billing Transactions for PROSVENDOR, THREE

for JUN 1999

<u>NAME SSN EL PRIMARY ITEM 910 OTHER SUSP TOTAL</u>

1\. PATIENT,ONE 0001 4 O2 TANK H SYSTEM 40.00 0.00 0.00 40.00

2\. PATIENT,TWO 0002 1 O2 CONCENTRATOR 325.00 300.00 0.00 625.00

3\. PATIENT,THREE 0003 4 O2 NEBULIZER/BUNN SYS 150.00 0.00 0.00 150.00

4\. PATIENT,FOUR 0004 4 O2 CONCENTRATOR 182.50 360.00 0.00 542.50

5\. PATIENT,FIVE 0005 4 O2 CONCENTRATOR 162.50 45.00 0.00 207.50

6\. PATIENT,SIX 0006 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

7\. PATIENT,SEVEN 0007 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

8\. PATIENT,EIGHT 0008 4 O2 CONCENTRATOR 182.50 330.00 0.00 512.50

9\. PATIENT,NINE 0009 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

10\. PATIENT,TEN 0010 4 O2 CONCENTRATOR 182.50 228.00 0.00 410.50

|                           |
|---------------------------|
| Enter ?? for more actions |

> Select ACTION:Next Screen//

> The action corrected the billing list as shown in bold above.

### Correct Billing Data and/or Suspend Dollar Amts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> EB Edit Billing: You can edit the billing information for a patient using this action. It allows you to add, delete, edit, or zero out an item. This option can also be used to suspend dollar amounts for an item. The patient must be on the billing list.

> Example:

<u>Billing Transactions Jul 04, 1999 14:19:56 Page: 1 of 29</u>

Billing Transactions for PROSVENDOR, THREE

for JUN 1999

<u>NAME SSN EL PRIMARY ITEM 910 OTHER SUSP TOTAL</u>

1\. PATIENT,ONE 0001 4 O2 TANK H SYSTEM 40.00 0.00 0.00 40.00

2\. PATIENT,TWO 0002 1 O2 CONCENTRATOR 325.00 300.00 0.00 625.00

3\. PATIENT,THREE 0003 4 O2 NEBULIZER/BUNN SYS 150.00 0.00 0.00 150.00

4\. PATIENT,FOUR 0004 4 O2 CONCENTRATOR 182.50 360.00 0.00 542.50

5\. PATIENT,FIVE 0005 4 O2 CONCENTRATOR 162.50 45.00 0.00 207.50

6\. PATIENT,SIX 0006 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

7\. PATIENT,SEVEN 0007 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

8\. PATIENT,EIGHT 0008 4 O2 CONCENTRATOR 182.50 330.00 0.00 512.50

9\. PATIENT,NINE 0009 4 O2 CONCENTRATOR 162.50 90.00 0.00 252.50

10\. PATIENT,TEN 0010 4 O2 CONCENTRATOR 182.50 228.00 0.00 410.50

|                           |
|---------------------------|
| Enter ?? for more actions |

> Select ACTION:Next Screen// eb Edit Billing

> Enter a list or range of numbers (1-6): 1

> PROSPATIENT2,FOUR 000-00-0024

> Current Prescription (#1)

> Active Date: FEB 28,1999 Expiration Date: JUL 1,1999

> 2 liters per minute by nasal cannula, as needed with an "H" tank.

> HCPCS Description FCP Qty Cost Susp. Total

> 1\. Ennnn TANKS H 910 1 40.00 0.00 40.00

> TOTAL COST 40.00

> Total 910 Charges: 40.00

> Total Station FCP Charges: 0.00

> Select ACTION: (A/D/E/Z): ??

> Enter a code from the list.

> Select one of the following:

> A Add

> D Delete

> E Edit

> Z Zero (This will zero out the cost of the item without going through

> edit.)

#### Zero Out an Item 

> Select ACTION: (A/D/E/Z): z Zero

> PROSPATIENT2,FOUR 000-00-0024

> Current Prescription (#1)

> Current Prescription (#1)

> Active Date: FEB 28,1999 Expiration Date: JUL 1,1999

> 2 liters per minute by nasal cannula, as needed with an "H" tank.

> HCPCS Description FCP Qty Cost Susp. Total

> 1\. Ennnn TANKS H 910 1 0.00 0.00 0.00

> TOTAL COST 0.00

> Total 910 Charges: 0.00

> Total Station FCP Charges: 0.00

#### Edit an Item 

> Select ACTION: (A/D/E/Z): e Edit

> PRIMARY ITEM: YES// \<ret\>

> QUANTITY: 1// \<ret\>

> UNIT COST: 0// 60

> REMARKS: \<ret\>

> SUSPENDED AMOUNT: 0// \<ret\>

> Select FUND CONTROL POINT: 910 PROSTHETIC SERVICES// \<ret\>

> ITEM TYPE: x Repair

> UNIT OF ISSUE: EA// \<ret\>

> PROSPATIENT2,FOUR 000-00-0024

> Current Prescription (#1)

> Current Prescription (#1)

> Active Date: FEB 28,1999 Expiration Date: JUL 1,1999

> 2 liters per minute by nasal cannula, as needed with an "H" tank.

> HCPCS Description FCP Qty Cost Susp. Total

> 1\. Ennnn TANKS H 910 1 60.00 0.00 60.00

> TOTAL COST 60.00

> Total 910 Charges: 60.00

> Total Station FCP Charges: 0.00

#### Add an Item

Select ACTION: (A/D/E): Add

Select PROS ITEM MASTER NAME: ??

Choose from:

4 COLOSTOMY BAGS

26 ACETAMINOPHEN W/CODEINE 30MG TAB

47 PARAFFIN

Select PROS ITEM MASTER NAME: 47PARAFFIN

...OK? Yes// (Yes)

PRIMARY ITEM: N NO

ITEM: COOKIE//

HCPCS CODE: ??

Enter the HCPCS code for this item. This number is taken from the CPT

file (81) and consists of 1 letter and 4 numbers. The HCPCS shares

the CPT file 81.

Choose from:

\#SHIP SHIPPING CHARGES \*\* inactive HCPCS \*\*

\#SHIP SHIPPING CHARGES \*\* inactive HCPCS \*\*

A4254 BATTERY FOR GLUCOSE MONITOR

A4255 GLUCOSE MONITOR PLATFORMS

A4258 LANCET DEVICE

A4259 LANCETS PER BOX

A4265 PARAFFIN

A4280 ADHESIVE SKIN SUPPORT

A4300 IMPLANTABLE ACCESS CATHETER

A4301 IMPLANTABLE ACCESS TOTAL SYSTE

A4324 MALE EXTERNAL CATHETER

A4325 MALE EXTERNAL CATHETER STRIP

A4331 EXTENSION DRAINAGE TUBING

A4332 LUBRICANT, INDIVIDUAL PACKET

A4333 URINARY CATHETER ANCHORING

A4334 URINARY CATHETER ANCHOR LEG

A4348 MALE EXTERNAL CATHETER

A4360 ADULT INCONTINENCE GARMENT \*\* inactive HCPCS \*\*

A4361 OSTOMY FACE PLATE

^

HCPCS CODE: A4265 PARAFFIN

VENDOR: VENDOR ONE PH: NO: 1

ORD ADD: FMS:

CODE: FAX:

\*\*\* BUSINESS TYPE UNDEFINED \*\*\*

...OK? Yes// (Yes)

QUANTITY: 1

UNIT COST: 1.50

UNIT OF ISSUE: EA EACH

ICD10 Diagnosis code: F14

20 matches found

1\. F14.10 Cocaine Abuse, Uncomplicated

2\. F14.12- Cocaine abuse with intoxication

3\. F14.14 Cocaine Abuse with Cocaine-Induced Mood Disorder

4\. F14.15- Cocaine abuse with cocaine-induced psychotic

disorder

5\. F14.18- Cocaine abuse with other cocaine-induced disorder

6\. F14.19 Cocaine Abuse with unspecified Cocaine-Induced

Disorder

7\. F14.20 Cocaine Dependence, Uncomplicated

8\. F14.21 Cocaine Dependence, in Remission

Press \<RETURN\> for more, "^" to exit, or Select 1-8: 2

4 matches found

1\. F14.120 Cocaine Abuse with Intoxication, Uncomplicated

(ICD-10-CM F14.120)

2\. F14.121 Cocaine Abuse with Intoxication with Delirium

(ICD-10-CM F14.121)

3\. F14.122 Cocaine Abuse with Intoxication with Perceptual

Disturbance (ICD-10-CM F14.122)

4\. F14.129 Cocaine Abuse with Intoxication, unspecified

(ICD-10-CM F14.129)

Select 1-4: 2

ICD10 Diagnosis code: F14.121

ICD10 Diagnosis description: Cocaine Abuse with Intoxication with Delirium

(ICD-10-CM F14.121)

REMARKS: TEST \#2

ITEM TYPE: I Initial Issue

> Select FUND CONTROL POINT: ^

#### Delete an Item

> Select ACTION: (A/D/E/Z): Delete

> Select an ITEM: (1-2): 2

> Are you SURE you want to delete this item? NO// YES ...deleted!

> PROSPATIENT2,FOUR 000-00-0024

> Current Prescription (#1)

> Current Prescription (#1)

> Active Date: FEB 28,1999 Expiration Date: JUL 1,1999

> 2 liters per minute by nasal cannula, as needed with an "H" tank.

> HCPCS Description FCP Qty Cost Susp. Total

> 1\. Ennnn TANKS H 910 1 60.00 0.00 60.00

> TOTAL COST 60.00

> Total 910 Charges: 60.00

> Total Station FCP Charges: 0.00

### Add a Patient to the Billing List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> AP Add Billing Patient: If a patient does not appear on the billing list, use the Pre-Billing Discrepancy Report to find out what is missing or incorrect in the patients record. Correct the discrepancy and then use this function to add the patient to the list.

> Example:

> Select ACTION:Quit// ADD Add Billing Patient

> Select PROSTHETICS PATIENT NAME: PROSPATIENT2,FIVE HINES, IL 03-03-6

> 6 0000000025 NO NSC VETERAN

> Item 19 was added to Billing Transaction....

### Delete a Patient from the Billing List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DP Delete Patient Billing: This action removes a patient from the selected month's billing list.

### Change the Quantity of an Item 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> QE Quick Edit: Use this action to quickly edit the quantity of an item.

> Select ACTION:Quit// qe Quick Edit

> Enter a list or range of numbers (1-5): 1

> PROSPATIENT, ONE 000-19-7641

> Current Prescription (#1)

> Active Date: FEB 24,1999 Expiration Date: JUL 1,1999

> HCPCS Description FCP Qty Cost Susp. Total

> 1\. E0430 OXYGEN 910 1 500.00 0.00 500.00

> 2\. A4616 OXYGEN HOSE UNION 910 25 0.75 0.00 18.75

> TOTAL COST 518.75

> Total 910 Charges: 518.75

> Total Station FCP Charges: 0.00

> 1\. E0430 OXYGEN 910 1 500.00 0.00 500.00

> QUANTITY: 1// \<ret\>

> 2\. A4616 OXYGEN HOSE UNION 910 25 0.75 0.00 18.75

> QUANTITY: 25// \<ret\>

> HCPCS Description FCP Qty Cost Susp. Total

> 1\. E0430 OXYGEN 910 1 500.00 0.00 500.00

> 2\. A4616 OXYGEN HOSE UNION 910 25 0.75 0.00 18.75

> TOTAL COST 518.75

> Total 910 Charges: 518.75

> Total Station FCP Charges: 0.00

> Enter RETURN to continue or '^' to exit:

### Accept the Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> AB Accept Billing: Once you are sure the bill is correct, use this action to Accept the billing. You may accept selected records or a range of records. This places a small "a" before those records that have been accepted.

> Select ACTION:Quit// AB Accept Billing

> Enter a list or range of numbers (1-6): 1

### View Only Accepted or Unaccepted Records 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CV Change View: Use this action when you want to limit your list to just those records that are Accepted or Unaccepted. The default view is Both.

> Select ACTION:Quit// cv Change View

> Select one of the following:

> A Accepted

> U Unaccepted

> B Both

> Which Transactions would you like displayed?: Both// u Unaccepted

### Unaccept the Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> UB Unaccept Billing: If you accepted a billing record in error, you can unaccept it using this action. It removes the small "a".

> Select ACTION:Quit// ub Unaccept Billing

> Enter a list or range of numbers (1-6): 1

### Post the Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> XB Post Billing: After accepting a billing, you can post it using this action.

> Also, anytime you have records that are Accepted, when you exit, you will be asked if you would like to post the bills.

> Note: If a purchase card is being used, accepting can be done by multiple people, but posting should only be done by one person. When using a purchase card payment type, <u>do not</u> Post Billing within List Manager. Select Quit and you will see the example below for Purchase Card.

> A small "p" next to the patient name and a "\*" next to an amount indicates that the record is only partially posted.

> Hint: If you have not loaded all your home oxygen patients into the program, you can still post those not in the program using the Create a No-Form Daily Record option under Purchasing.

> **WARNING:** The purchase card holder must have a monthly purchase limit greater than the total purchase order amount.

> Example: (1358 Payment Type)

> Select ACTION:Quit// ?

> ET Edit Patient AP Add Billing Patient UB Unaccept Billing

> EB Edit Billing CV Change View XB Post Billing

> AB Accept Billing QE Quick Edit

> 23 Display 2319 SO Sign Off Purchase Card

> Select ACTION:Quit// xb Post Billing

> Enter a list or range of numbers (1-10): 1-10

> Are you Sure you Want to Post Transactions? NO// y YES

> Fund Control Point: 910 PROSTHETIC SERVICES

> Select Fund Control Point: 910 PROSTHETIC SERVICES 499-C35010 8509.75

> PAYMENT TYPE: ?

> Enter 1 for 1358 or P for Purchase Card.

> Choose from:

> 1 1358

> P PURCHASE CARD

PAYMENT TYPE: 1358

> Select Obligation Number: C35010 499-C35010 09-08-93 1358 Obligated - 1358

> FCP: 910 \$ 10000.00

> Are you sure? NO// YES

> 910 PROSTHETIC SERVICES ...Posted

> Fund Control Point: 913 PROSTHETIC SUPPLIES

> Select Fund Control Point: 913 PROSTHETIC SUPPLIES 499-C35009 7900.00

> PAYMENT TYPE: 1358

> Select Obligation Number: C35010 499-C35010 09-08-93 1358 Obligated - 1358

> FCP: 913 \$ 10000.00

> Are you sure? NO// YES

> 913 PROSTHETIC SUPPLIES ...Posted

> All Fund Control Points posted successfully

> Press any Key to Continue: \<ret\>

> Example: (Purchase Card Type)

> Select ACTION:Quit// ?

> ET Edit Patient AP Add Billing Patient UB Unaccept Billing

> EB Edit Billing CV Change View XB Post Billing

> AB Accept Billing QE Quick Edit

> 23 Display 2319 SO Sign Off Purchase Card

> Select ACTION:Quit// \<ret\> QUIT

> There are patients whose billing transactions have been accepted

> and not yet posted

> Would you like to post them now? NO// YES

> Are you Sure you Want to Post Transactions? NO// YES

> Fund Control Point: 910 PROSTHETIC SERVICES

> Select Fund Control Point: \<ret\>

> PAYMENT TYPE: ?

> Enter 1 for 1358 or P for Purchase Card.

> Choose from:

> 1 1358

> P PURCHASE CARD

> PAYMENT TYPE: PURCHASE CARD

> ENTER A NEW PURCHASE ORDER NUMBER OR A COMMON NUMBERING SERIES

> PURCHASE ORDER: 499-P7 PC AUTHORIZED BUYER

> Are you adding '499-P70151' as a new Purchase Order number ? Y (YES)

> PURCHASE CARD NAME: VISA VISA-CARD

> COST CENTER: 827300// PROSVENDOR,FIVE

> Are you sure? NO// YES

> 910 PROSTHETIC SERVICES ...Posted

> Fund Control Point: 913 PROSTHETIC SUPPLIES

> Select Fund Control Point: \<ret\>

> PAYMENT TYPE: PURCHASE CARD

> ENTER A NEW PURCHASE ORDER NUMBER OR A COMMON NUMBERING SERIES

> PURCHASE ORDER: 499-P7 PC AUTHORIZED BUYER

> Are you adding '499-P70152' as a new Purchase Order number ? Y (YES)

> PURCHASE CARD NAME: VISA VISA-CARD

> COST CENTER: 827300// PROSVENDOR,FIVE

> Are you sure? NO// YES

> 913 PROSTHETIC SUPPLIES ...Posted

> All Fund Control Points posted successfully

> Press any Key to Continue: \<ret\>

### Sign Off on the Purchase Card

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> SO Sign Off Purchase Card: Use this action to sign off on purchase card transactions. If you have posted more than one

> Select ACTION:Quit// SO Sign Off Purchase Card

> PAYMENT TYPE: PURCHASE CARD

> Select FUND CONTROL POINT: 910 PROSTHETIC SERVICES P70148

> Verifying all items posted for FCP. Please be patient.

> Sure you want to Continue? YES

> Enter ELECTRONIC SIGNATURE CODE: (Enter your electronic signature code) Thank you.

> Cost of this request: \$\$\$.00

> Current Control Point Balance: \$\$\$\$.00

### View the 2319

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 23 Display 2319: Use this action to view the 2319. Screen \#8 of the 2319 contains the home oxygen information.

> Select ACTION:Quit// 23 Display 2319

> Enter a number (1-5): 2

> \*Comments on file

> Current Disability Codes are:

> COS/B SC VIETNAM S/C

> AMP/LSD SC VIETNAM S/C Deleted...

> AMP/LPH OTHERS ELIG NSC PL-96-151

> Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue: 8 HOME OXYGEN ITEMS

> PROSPATIENT2,SIX 000-00-0026

> Current Prescription (#1)

> Active Date: FEB 28,1999 Expiration Date: JUL 1,1999

> 2 liters per minute by nasal cannula, 24 hours a day, with an oxygen

> concentrator, 6 "E" tanks, 2 "D" tanks, and an "H" tank as the emergency

> back up system.

> Enter RETURN to continue or '^' to exit: \<ret\>

> PROSPATIENT2,SIX SSN: 000-00-0026 DOB: JAN 1,1918 CLAIM#

> Date Qty Item Type Vendor Sta Serial Delivery Date Tot Cost

> 1\. 05/12/99 1 TANKS E PO VENDOR 499 05/26/99 50.00

> 2\. 05/12/99 1 TANKS E PO VENDOR 499 05/26/99 50.00

> End of Home Oxygen records for this veteran!

> +=Turned-In \*=Historical Data I=Initial X=Repair S=Spare R=Replacement

> Enter 1-2 to show full entry, '^' to exit or \`return\` to continue. 1

> PROSPATIENT2,SIX SSN: 000-00-0026 SUPPORT ISC DOB: 01-01-1918

> APPLIANCE/REPAIR LINE ITEM DETAIL \<4-1\>

> TYPE OF FORM: OTHER INITIATOR: PROSPROVIDER,ONE DATE: MAY 12, 1999@08:48:34

> DELIVER TO:

> TYPE TRANS: QTY: 1 SOURCE: COMMERCIAL

> VENDOR: PROSVENDOR, THREE

> VENDOR PHONE: 555-555-5555

> 200 VENDOR DRIVE

> LIBERTYVILLE, ILLINOIS 60048

> DELIVERY DATE: MAY 26, 1999@06:12:05

> TOTAL COST: \$50.00 OBL: 499-C35010-0070

> REMARKS:

> DISABILITY SERVED: NSC/OP

> APPLIANCE: TANKS E PORTABLES

> PSAS HCPCS: E0420 OXYGEN CYLINDER, DEMURRAGE O

> DESCRIPTION:

> EXTENDED DESCRIPTION:

> Enter RETURN to continue or '^' to exit:

> 1\. 05/12/99 1 TANKS E PO HOLLISTER 499 05/26/99 50.00

> 2\. 05/12/99 1 TANKS E PO HOLLISTER 499 05/26/99 50.00

> End of Home Oxygen records for this veteran!

> +=Turned-In \*=Historical Data I=Initial X=Repair S=Spare R=Replacement

> Enter 1-2 to show full entry, '^' to exit or \`return\` to continue.

> \*Comments on file

> Current Disability Codes are:

> COS/B SC VIETNAM S/C

> AMP/LSD SC VIETNAM S/C Deleted...

> AMP/LPH OTHERS ELIG NSC PL-96-151

> Select one of the following:

> 1 PATIENT DEMOGRAPHICS

> 2 CLINIC ENROLLMENTS/CORRESPONDENCE

> 3 ENTITLEMENT INFORMATION

> 4 APPLIANCE TRANSACTIONS

> 5 AUTO ADAPTIVE INFORMATION

> 6 CRITICAL COMMENTS

> 7 ADD/EDIT DISABILITY CODE

> 8 HOME OXYGEN ITEMS

> Enter 10-2319 screen to VIEW (1-8),'^' to EXIT, or 'return' to continue :

## Purchase Card Sign Off

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this action to sign off on a purchase card transaction. This action can also be taken using the option Billing Transactions.

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Entering "?" will bring up a list of sites. Select a site.

Billing Month: Enter the month you want to review, e.g., 2/99, 0299, Feb 99 for February 1999.

Payment Type: Enter the method of payment for the fund control point. Payments for home oxygen are done by purchase cards or 1358 service orders. Select one of the following:

> 1 1358

> P PURCHASE CARD

Fund Control Point: Through which FCP will this purchase be handled? Enter the FCP here.

Example:

SITE: HINES ISC VAMC// \<ret\> 499

Select BILLING MONTH: 2-1998

PAYMENT TYPE: ??

Enter 1 for 1358 or P for Purchase Card.

Choose from:

1 1358

P PURCHASE CARD

PAYMENT TYPE: P PURCHASE CARD

Select FUND CONTROL POINT: 910 PROSTHETIC SERVICES P70134

Verifying all items posted for FCP. Please be patient.

Sure you want to Continue? Y YES

Enter ELECTRONIC SIGNATURE CODE: (Enter your signature code) Thank you.

Cost of this request: \$\$\$\$.50

Current Control Point Balance: \$\$\$\$.50

## Verify Posted Billing Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After posting billing transactions, a bill might be posted in IFCAP but fail to be posted to the patient's 2319. Use this option as often as needed to make sure that all records get posted to the 2319.

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Enter a site.

Billing Month: Enter the month you want to review, e.g., 2-1999, 2-99, Feb 99 for February 1999. This field only accepts months that have been posted.

Vendor: Select the vendor.

If nothing fails, you get the following notification.

> Processing...

> Everything posted okay!!

# Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a number of reports to help you manage your home oxygen program.

> Alphabetical List Home Oxygen Patients (by site): This is a listing of active home oxygen patients for a selected site. The report also shows the date the current prescription expires.

> Active Home Oxygen Patients (Alpha by Zip Code): This is a listing of active patients with their address information.

> Prescription Expiration Dates: This is a listing of active patients sorted by the expiration dates for their current prescriptions.

> Inactive Home Oxygen Patients (by Inactive date): This is a listing of inactive patients and the reason they were inactivated.

> Primary Item Report: This is a report of active patients listing the primary item, quantity of the item, and cost.

> Monthly Home Oxygen Billing: This report lists billings for all active home oxygen patients.

> New Patients: This is a report of all new patients for a selected date range.

> Prescription Report: This report includes HCPCS/items, quantity, cost, extended cost, and the fund control point.

> Pre-Billing Discrepancy Report: This report should be run and any discrepancies corrected prior to creating a billing list for a month. If there are any discrepancies for a patient, then that patient will not appear on the billing list.

  
Reports ...

## Alphabetical List Home Oxygen Patients (by site)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is an alphabetical listing of active home oxygen patients for a selected site. The report also displays the primary item, the date the patient was last activated, and the date the current prescription expires.

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Entering "?" will bring up a list of sites. Select a site.

Device: Hit the \<ret\> key to bring the report to your screen or enter the name of a printer to obtain a hard copy report.

MAR 3,1999 08:09 HINES ISC VAMC Page: 1

Home Oxygen Patients

Date Current

Prescription

Patient SSN Primary Item Active Expires

======================= ==== ============================== ======== ==========

PROSPATIENT2,SEVEN 0001 CONCENTRATOR 02/22/99 05/23/1999

PROSPATIENT2,EIGHT 0002 CONCENTRATOR 02/24/99 05/25/1999

PROSPATIENT2,NINE 0003 CONCENTRATOR 02/19/99 05/20/1999

...

Total Patients: 8

Reports ...

## Active Home Oxygen Patients (Alpha by Zip Code)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a list of addresses, sorted by the zip code, for active home oxygen patients.

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Entering "?" will bring up a list of sites. Select a site.

Device: Hit the \<ret\> key to bring the report to your screen or enter the name of a printer to obtain a hard copy report.

MAR 3,1999 08:25 HINES ISC VAMC Page: 1

Active Home Oxygen Patients by Zip Code

Zip Code Name/Phone Number SSN Address

========== ===================== ==== ===================================

60067 PROSPATIENT2,TEN 0009 123 Any RD

Anytown ,IL

60141 PROSPATIENT3,ONE 0008 3455 WEST Any ST.

555-555-5555 Anyville ,IL

60148 PROSPATIENT3,TW0 0007 123 E Amystreet

Anywhere ,IL

...

Total Patients: 9

Reports ...

## Prescription Expiration Dates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This list is sorted by the prescription expiration date and displays the patient, SSN, primary item, and the date the patient was last activated.

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Entering "?" will bring up a list of sites. Select a site.

Device: Hit the \<ret\> key to bring the report to your screen or enter the name of a printer to obtain a hard copy report.

MAR 3, 1999 09:13 HINES ISC VAMC Page: 1

Prescription Expiration Date

Date Current

Prescription

Expires Name SSN Primary Item Active

========== ======================= ==== ============================== ========

02/23/1999 PROSPATIENT3,THREE 0033 CONCENTRATOR 02/19/99

05/02/1999 PROSPATIENT3,FOUR 0034 CONCENTRATOR 01/01/99

05/20/1999 PROSPATIENT2,TEN 0210 CONCENTRATOR 02/19/99

...

Total Patients: 8

Reports ...

## Inactive Home Oxygen Patients (by Inactive date)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a list of inactive patients sorted by the dates the patients were inactivated.

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Entering "?" will bring up a list of sites. Select a site.

Start at INACTIVATION DATE: This is the beginning date of the date range for the report.

Ending INACTIVATION DATE: This is the ending date of the date range for the report.

Device: Hit the \<ret\> key to bring the report to your screen or enter the name of a printer to obtain a hard copy report.

MAR 3,1999 09:19 HINES ISC VAMC Page: 1

Inactive Home Oxygen Patients

Date Range: SEP 04, 1998 to MAR 03, 1999

Patient SSN Active Inactive Inactive Reason

=================== ==== ========== ========== ========================

PROSPATIENT3,SIX 0036 02/24/1999 02/24/1999 INPATIENT STATUS

PROSPATIENT3,SEVEN 0037 02/17/1999 03/02/1999 Rx EXPIRED

TOTAL PATIENTS: 2

Reports ...

## Primary Item Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report is sorted by the primary item and displays the patient name, SSN, primary item, quantity of the item, unit cost and total cost.

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Entering "?" will bring up a list of sites. Select a site.

Device: Hit the \<ret\> key to bring the report to your screen or enter the name of a printer to obtain a hard copy report.

MAR 3,1999 09:39 HINES ISC VAMC Page: 1

Primary Item Report

Unit Total

Patient SSN Primary Item Qty Cost Cost

================= ==== ============================== === ====== ======

Primary Item: CONCENTRATOR

PROSPATIENT2,SEVEN 0027 CONCENTRATOR 1 450.00 450.00

PROSPATIENT1,TWO 0012 CONCENTRATOR 1 500.00 500.00

PROSPATIENT3,EIGHT 0196 CONCENTRATOR 1 450.00 450.00

PROSPATIENT3,NINE 0039 CONCENTRATOR 1 500.00 500.00

PROSPATIENT3,TWO 0032 CONCENTRATOR 1 500.00 500.00

Primary Item: TANKS E PORTABLES

PROSPATIENT3,TEN 0310 PROSVENDOR, FOUR 1 50.00 50.00

PROSPATIENT2,TWO 0022 PROSVENDOR, FOUR 1 50.00 50.00

PROSPATIENT1,FIVE 0015 PROSVENDOR, FOUR 1 50.00 50.00

Total Patients: 8

Reports ...

## Monthly Home Oxygen Billing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This prints a list of active patients with their home oxygen costs displayed by FCP and any suspended dollars .

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Entering "?" will bring up a list of sites. Select a site.

Billing Month: Enter the month and year you want shown in the report. Examples: February 1999, Feb 99, 2/99, 0299, 2-99.

Device: Hit the \<ret\> key to bring the report to your screen or enter the name of a printer to obtain a hard copy report.

MAR 3,1999 09:46 HINES ISC VAMC Page: 1

FEB 1999 Monthly Home Oxygen Billing

Station

Fund Control

ACC Name SSN Vendor 910 Point Other Susp Total

----------------- ------- ---------------------------------------------------

PROSPATIENT3,SEVEN 0037 PROSVENDOR, THREE 200.75 - 200.75

PROSPATIENT3,TEN 0310 PROSVENDOR, THREE 518.75 - 518.75

PROSPATIENT4,ONE 0041 PROSVENDOR, THREE 50.00 - 50.00

a# PROSPATIENT4,TWO 0042 PROSVENDOR, THREE 272.00 - 272.00

PROSPATIENT4,THREE 0043 PROSVENDOR, THREE 80.00 - 80.00

Totals: 920.75 200.75 - - 1121.50

Total Patients: 5

> **NOTE:** a = accepted.

\# = posted completely

p = partially posted (one FCP, but not both)

Reports ...

## New Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a list of new patients, not necessarily new to the program but their last activation date falls within the date range selected for the report.

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Entering "?" will bring up a list of sites. Select a site.

Start date: The default start date is the first day of the month you are in. This date may be changed to another. It is assumed the end date is "today".

Device: Hit the \<ret\> key to bring the report to your screen or enter the name of a printer to obtain a hard copy report.

MAR 3,1999 09:55 HINES ISC VAMC Page: 1

New Patient Report

Patient SSN Primary Item Activation Date

===================== ==== ================================ ===============

PROSPATIENT3,EIGHT 0038 CONCENTRATOR MAR 2,1999

PROSPATIENT1,FIVE 0015 CONCENTRATOR MAR 3,1999

PROSPATIENT3,TWO 0032 CONCENTRATOR MAR 2,1999

TOTAL PATIENTS: 3

Reports ...

## Prescription Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report includes HCPCS/items, quantity, cost, extended cost, and the fund control point for a selected patient or all patients.

Site: This prompt only appears if your Prosthetics Service covers multiple stations. Entering "?" will bring up a list of sites. Select a site.

Select All Patients? You may select all patients (YES) or a single patient (NO).

> Prosthetics Patient: If you choose to select a single patient, enter the patient name at this prompt. Enter the patient's name as LAST,FIRST or first initial last name plus last 4 digits of the SSN.

Device: Hit the \<ret\> key to bring the report to your screen or enter the name of a printer to obtain a hard copy report.

MAR 9,1999 12:39 HINES ISC VAMC Page: 1

Prescription Report

Date Current

Name SSN Activation Date Prescription Expires

================= ==== =============== =====================

PROSPATIENT4,FOUR 0044 MAR 8,1999 JUN 6,1999

This is a full description of how much, how often and how the oxygen

should be delivered to the patient according to the prescription.

VENDOR, INC.

Fund

Extended Control

HCPCS Item Qty Unit Cost Cost Point

----- ---- --- --------- ---- -----

E1401 OXYGEN 1 140.00 140.00 910

E0424 PROSVENDOR, FOUR 1 22.50 22.50 910

E0443 PROSVENDOR, FOUR 3 15.00 45.00 910

Total Cost 207.50

Inactivation Date:

Inactivation Reason:

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Total Patients: 1

Reports ...

## Pre-Billing Discrepancy Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Pre-Billing Discrepancy Report under Billing.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td>1358</td>
<td>The computerized record of obligations during a set time frame. This form allows a financial obligation to be set up in the system.</td>
</tr>
<tr class="even">
<td>2319</td>
<td>The computerized form on which a patient's Prosthetics data is accepted.</td>
</tr>
<tr class="odd">
<td>Accept</td>
<td>The act of marking a patient’s monthly home oxygen bill as having been checked and correct.</td>
</tr>
<tr class="even">
<td>Activation Date</td>
<td>Date the patient began home oxygen treatment. If patient becomes inactivated (see Inactivation Reason) this may also be the date the patient is reactivated.</td>
</tr>
<tr class="odd">
<td>AMA</td>
<td>American Medical Association.</td>
</tr>
<tr class="even">
<td>Concentrator</td>
<td>A device that extracts the nitrogen from the air we breathe and outputs 88 to 93% pure oxygen for patients to breathe.</td>
</tr>
<tr class="odd">
<td>Contract Location</td>
<td>The site that administers the contract.</td>
</tr>
<tr class="even">
<td>Cost</td>
<td>Charge per unit in dollars and cents.</td>
</tr>
<tr class="odd">
<td>CPT</td>
<td>Current Procedural Terminology codes published by the AMA.</td>
</tr>
<tr class="even">
<td>Default Days to Expiration</td>
<td>The expiration date of the prescription will default to the contents of this field by adding this number of days to the Prescription Date when the user initially enters a new prescription.</td>
</tr>
<tr class="odd">
<td>Eligibility</td>
<td><p>Home Oxygen eligibility is one of the following:</p>
<p>1 = SC/OP</p>
<p>2 = SC/IP</p>
<p>3 = NSC/IP</p>
<p>4 = NSC/OP</p></td>
</tr>
<tr class="even">
<td>Eligibility, Special Category</td>
<td><p>A subcategories of the NSC/OP:</p>
<p>1 = Special Legislation</p>
<p>2 = A &amp; A</p>
<p>3 = PHC</p>
<p>4 = Eligibility Reform</p></td>
</tr>
<tr class="odd">
<td>FCP</td>
<td>Fund Control Point.</td>
</tr>
<tr class="even">
<td>HCPCS</td>
<td>Healthcare Financing Administration Common Procedure Code System. A code that represents and item or service. Can also be PSAS HCPCS code created by the Data Validation Committee.</td>
</tr>
<tr class="odd">
<td>H.O.</td>
<td>Home Oxygen (From Section 3.1.3).</td>
</tr>
<tr class="even">
<td>ICD9 and ICD10 Code<span id="ICD10codeupdate2" class="anchor"></span></td>
<td>International Classification of Diseases code. A code that represents the primary diagnosis for which oxygen treatment is prescribed for the patient.</td>
</tr>
<tr class="odd">
<td>IEN</td>
<td>Internal Entry Number (From Section 3.5.2.1 – Purchase Order field).</td>
</tr>
<tr class="even">
<td>IFCAP</td>
<td>The financial system in VISTA that records information about obligations, purchase cards, etc.</td>
</tr>
<tr class="odd">
<td>Inactivation Date</td>
<td>The date the patient's home oxygen treatment is discontinued.</td>
</tr>
<tr class="even">
<td>Inactivation Reason</td>
<td><p>Why the treatment is cancelled or not started:</p>
<p>D = Discontinued by Patient</p>
<p>R = Rx Expired</p>
<p>M = MD Discontinued</p>
<p>P = Patient Deceased</p>
<p>I = Inpatient Status</p>
<p>E = Entered in Error</p></td>
</tr>
<tr class="odd">
<td>Item</td>
<td>Something that can be issued to a patient. Multiple items may be associated with one HCPCS.</td>
</tr>
<tr class="even">
<td>Item, Primary</td>
<td>The item that is most important to the patient's care; denotes what kind of treatment the patient is getting. The main component of the equipment.</td>
</tr>
<tr class="odd">
<td>Item Type</td>
<td><p>A first time issue of the item, replacement of the item, or repair of the item:</p>
<p>I = Initial issue</p>
<p>R = Replace</p>
<p>X = Repair</p></td>
</tr>
<tr class="even">
<td>JCAHO</td>
<td>Joint Committee on the Accreditation of Healthcare Organizations</td>
</tr>
<tr class="odd">
<td>Liquid system</td>
<td>A tank of oxygen gas in liquid form.</td>
</tr>
<tr class="even">
<td>PCO</td>
<td>Purchase Card Order.</td>
</tr>
<tr class="odd">
<td>PHC</td>
<td>Sub-category of NSC/OP Eligibility.</td>
</tr>
<tr class="even">
<td>PO</td>
<td>Purchase Order.</td>
</tr>
<tr class="odd">
<td>Post</td>
<td>This process creates and updates a 2319. It also sends home oxygen patient billing transactions to the IFCAP system so that they will be officially recorded and paid, reducing the obligated amount available to be spent.</td>
</tr>
<tr class="even">
<td>Prescription</td>
<td>A physician order for treatment/service/medication for the patient.</td>
</tr>
<tr class="odd">
<td>Prescription Date</td>
<td>Date that the prescription is written.</td>
</tr>
<tr class="even">
<td>Prescription Expiration Date</td>
<td>Date that the prescription is no longer valid.</td>
</tr>
<tr class="odd">
<td>Prescription Sequence Number</td>
<td>This is the internal identification number of a prescription. Each prescription in sequence will have a different life-time. The 1<sup>st</sup> prescription may expire in 6 months, the 2<sup>nd</sup> in another 6 months, the 3<sup>rd</sup> in 12 months, the 4<sup>th</sup> in 24 months. As users enter prescriptions for patients, the system will try to calculate the correct expiration date for it based on the "Default Days to Expiration" field value.</td>
</tr>
<tr class="even">
<td>Prosthesis</td>
<td>A man-made device that replaces functionality that was originally a natural capability of the body.</td>
</tr>
<tr class="odd">
<td>Quantity</td>
<td>The number of units issued.</td>
</tr>
<tr class="even">
<td>SRS</td>
<td>Software Requirements Specification.</td>
</tr>
<tr class="odd">
<td>Suspensed</td>
<td>When a Home Oxygen provider bills the VAMC for services or supplies and the VAMC does not recognize the charges as liquidated and does not pay them, such charges are said to be suspensed.</td>
</tr>
<tr class="even">
<td>Unit of Issue</td>
<td>How the item is issued, e.g., box, each, bottle, liter, etc.</td>
</tr>
<tr class="odd">
<td>VA</td>
<td>Department of Veterans Affairs.</td>
</tr>
<tr class="even">
<td>VAMC</td>
<td>VA Medical Center.</td>
</tr>
<tr class="odd">
<td>Vendor</td>
<td>The company from which the item is purchased.</td>
</tr>
<tr class="even">
<td>VISN</td>
<td>Veterans Integrated Services Network.</td>
</tr>
<tr class="odd">
<td>V<em><span class="smallcaps">ist</span></em>A</td>
<td>Veterans Integrated Services Technical Architecture</td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Accept Billing, 4-12
Active Home Oxygen Patients (Alpha by Zip Code), 1-2, 5-3
Add/Edit Correspondence Skeleton Letter, 2-1
Add/Edit Home Oxygen Patient, 1-1, 3-2
activating the patient, 3-3
adding a new prescription, 3-3
adding or editing a billing item, 3-4
adding patients to module, 3-2
editing the patient's eligibility, 3-3
Alphabetical List Home Oxygen Patients (by site), 1-1, 5-2
Auto-generating letters, 2-2
Billing, 4-1
Billing List
add an item, 4-8
add patient, 4-10
change quantity of an item, 4-11
correct billing data and suspend dollar amts, 4-7
creating, 4-4
delete a patient, 4-10
delete an item, 4-8
edit an item, 4-8
edit patient information, 4-5
view accepted/unaccepted records, 4-12
zero out an item, 4-7
Billing Transactions, 1-1, 4-2, 4-4
actions available, 4-5
Pre-Billing Discrepancy Report, 4-4
Contract Location, 3-3
Correcting discrepancies that affect accurate billing, 4-2
Correspondence, 2-1
Correspondence menu, 2-1
Correspondence/Letters
setup/implementation, 2-1
Default Days to Expiration, 2-2
site parameters, 2-3
Discrepancies that affect accurate billing, 4-2
Display 2319, 4-16
Edit Billing, 4-7
Edit Patient information, 4-5
Eligibility, 3-3
Failure to post to 2319, 4-19
Finding discrepancies that affect accurate billing, 4-2
Fund control point
site parameters, 2-3
Fund control points, 2-2
Generate Letters, 1-1, 2-2, 3-8
Home Oxygen Activation Date, 3-3
Home Oxygen Letter
site parameters, 2-3
Home Oxygen Main Menu, 2-1
Home Oxygen Vendors, 2-2
site parameters, 2-3
Inactivate/Activate Oxygen Patient, 1-1, 3-6
Inactivation, 3-6
reasons to inactivate, 3-6
Inactive Home Oxygen Patients (by Inactive date), 1-2, 5-5
Letters
auto-generating, 2-2
effect of printing, 3-8
setup, 2-1
worksheet for setup, 2-2
List Manager
displaying functions, 1-4
how it works, 1-3
searching for information, 1-4
use in billing transactions/generating letters, 1-3
Manage Letter List, 3-8
Monthly Home Oxygen Billing, 1-2, 5-7
New Patients, 1-2, 5-8
Package Implementation
setting up the site parameters, 2-1
Post Billing, 4-13
Pre-billing discrepancies
correcting, 4-2
finding, 4-2
Pre-Billing Discrepancy Report, 1-2, 4-2, 5-10
Prescription Expiration Dates, 1-2, 5-4
Prescription Report, 1-2, 5-9
Prescription Sequence Number
site parameters, 2-3
Prescriptions
sequence numbering, 2-2
Primary Item Report, 1-2, 5-6
Print Letter Header
site parameters, 2-4
Print Letters, 3-9
adding patient to the list, 3-9
deleting list entry, 3-9
Print/Display Patient Correspondence Letter, 3-8
Prosthetics Patient file, 1-1
PSAS
fund control point setup, 2-3
Purchase Card Sign Off, 1-2, 4-18
Sequence numbering
prescriptions, 2-2
Sign Off Purchase Card, 4-15
Site Parameters Enter/Edit, 1-2, 2-1, 2-3
Station, 3-2
Unaccept Billing, 4-12
Verify Posted Billing Transactions, 1-2, 4-19
