---
title: DGBT*1*20 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: DGBT
app_name: Beneficiary Travel
section: CLI
app_status: active
pkg_ns: DGBT
patch_ver: 1
patch_id: DGBT*1*20
group_key: DGBT:DGBT:1
file_numbers: []
security_keys: []
menu_options: 0
description: '- Introduction - Inactivating Accounts for Mileage Claims - Claim Submission - Automatic Eligibility Determination - [Special Mode Trip Tracking and...'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 2578
section_count: 23
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: February 2013
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Beneficiary_Travel/dgbt1_0_20_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Beneficiary_Travel/dgbt1_0_20_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=123
audit_applied: '2026-05-31'
master_source: DGBT*1*20 Release Notes
master_pub_date: February 2013
consolidated_from: 2 versions
prior_versions:
- DGBT*1*32 Release Notes
consolidated_title: release notes
---

![](dgbt-1-20-release-notes/001.png)

Beneficiary Travel

Release Notes

DGBT\*1.0\*20

February 2013

Office of Information and Technology (OIT)

Product Development

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Inactivating Accounts for Mileage Claims](#inactivating-accounts-for-mileage-claims)
- [Claim Submission](#claim-submission)
  - [Automatic Eligibility Determination](#automatic-eligibility-determination)
  - [Special Mode Trip Tracking and Accounting](#special-mode-trip-tracking-and-accounting)
  - [Automatic Deductible Zero](#automatic-deductible-zero)
  - [Previous Income Information Retrieval](#previous-income-information-retrieval)
  - [Denial of Benefits](#denial-of-benefits)
  - [Denial of Benefits Letters](#denial-of-benefits-letters)
  - [Common Carrier Mode of Transportation](#common-carrier-mode-of-transportation)
  - [Message on Service Connected Appointment Only](#message-on-service-connected-appointment-only)
- [Data Added to Claim Information Display](#data-added-to-claim-information-display)
  - [Last Address Change Date](#last-address-change-date)
  - [Current Year Income Test from Annual Means Test](#current-year-income-test-from-annual-means-test)
  - [Net Income and Status from Means Test](#net-income-and-status-from-means-test)
  - [Message on Service Connected Appointment Only](#message-on-service-connected-appointment-only-1)
  - [Public Transportation](#public-transportation)
- [Deductible Waivers and Alternate Income](#deductible-waivers-and-alternate-income)
  - [Capture of Deductible Waiver Data](#capture-of-deductible-waiver-data)
  - [Automatic Retrieval of Manual Waiver](#automatic-retrieval-of-manual-waiver)
  - [Standardized Expiration of Authorized BT Waivers](#standardized-expiration-of-authorized-bt-waivers)
  - [Alternate POW Processing](#alternate-pow-processing)
  - [Current Hardship Processing](#current-hardship-processing)
- [New Electronic Voucher Features](#new-electronic-voucher-features)
  - [Cash Reimbursement Form Changes](#cash-reimbursement-form-changes)
- [Trips and Deductible Waivers Tracking Features](#trips-and-deductible-waivers-tracking-features)
  - [National Tracking of BT Deductible in a Calendar Month](#national-tracking-of-bt-deductible-in-a-calendar-month)
  - [## Entering Two Different Types of Waivers](#entering-two-different-types-of-waivers)
- [New BT ReportsMain Menu: RPTS Beneficiary Travel Reports](#new-bt-reportsmain-menu-rpts-beneficiary-travel-reports)
    - [Summary Report](#summary-report)
    - [Audit Report](#audit-report)
    - [Clerk Report](#clerk-report)
    - [Fiscal Report](#fiscal-report)
    - [Travel Pattern Report](#travel-pattern-report)
    - [Special Mode Report](#special-mode-report)
As part of the strategy to provide high quality healthcare to Veterans, VA facilities are authorized to pay for eligible travel expenses related to their healthcare. The Beneficiary Travel (BT) application system is a module within the Veterans Health Information Systems and Technology Architecture (VistA). This module provides automated features to issue beneficiary travel pay. Travel reimbursement is provided by designated categories for eligible Veterans, and to non-employee attendants who are eligible for reimbursement. \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
Bene Travel Account entries must be reviewed and modified prior to use
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Inactivating Accounts for Mileage Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: BENE Travel Account File Enter/Edit

New rules must be followed for entries in the Bene Travel Account file. BT supervisors or ADPAC's must complete the following steps before the BT Enhancement patch is installed:

- Inactivate all accounts for mileage claims that are not of Type 4 (all other) or Type 5 (C&P), or, if a site prefers to keep an account that is not Type 4 or 5 active, they can change that account type to 4 or 5. A site can have more than one account of each type 4 and type 5 but the default will be the first active entry detected by the system.
- A site can have only one active special mode account type (Type 3). It must contain the exact characters "Special Mode – Non-Emergen" in the text for the account type (a 3-digit account code can be before or after the required text). All other type 3 account entries must be inactivated.

New features and changes introduced by BT Enhancement patch DGBT\*1.0\*20:

# *Claim Submission*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Automatic Eligibility Determination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

The BT system will automatically determine if a Veteran is eligible for BT reimbursement based on VistA eligibility, enrollment, and C&P data.

## Special Mode Trip Tracking and Accounting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

Prior to enhancement patch DGBT\*1\*20, VA *Special Mode* payments were handled outside the standard BT software. Modifications to the BT application provide features to fully capture and track Special Mode Transportation Authorization and Special Mode Transportation Vendor Billing. Special Mode Transportation includes air, ambulance, stretcher, wheelchair van, etc.

## Automatic Deductible Zero 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

The BT system will now determine if the deductible should be waived for Veterans who report *Income* below the appropriate threshold on valid Means Tests or though new BT features for capturing low income, Veterans with VA pensions, and Veterans who use Common Carriers.

## Previous Income Information Retrieval 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

There will be times when changes in a Veteran's administrative eligibility for BT or changes in BT rules or regulations grant a Veteran reimbursement of travel for claims that were previously denied to the Veteran.  To correctly process such claims, the BT system will locate and use Veteran income information when a claim is entered for a previous year. This income will be displayed on the Beneficiary Travel Claim Information screen.

## Denial of Benefits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

The BT system will provide new features to deny a claim, document the reason and, print and reprint a Denial of Benefits Letter that includes the Veteran's Appellate Rights if a Veteran has been denied BT Benefits.

## Denial of Benefits Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit, EDL Edit Denial Letters Template, and RDL Reprint Denials of Benefits Letter

The BT system now allows the user to generate Denial of Benefits letters when it has been determined that the Veteran is not eligible for BT reimbursement and his claim has been denied.  BT supervisors and ADPAC's can modify the content of the letters by editing the Denial Letters Template.

## Common Carrier Mode of Transportation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

The BT system captures and displays additional information when a Veteran uses a Common Carrier, such as bus, taxi, etc., as the means of transportation for a trip.

## Message on Service Connected Appointment Only 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

If the Veteran is less than 30% SC and only eligible for *SC Conditions*, and does not pass the *Low-Income Eligibility* test, then the system will display "*BT Alert: ELIGIBLE FOR SC APPOINTMENTS ONLY*" on the Beneficiary Travel Claim Information screen. The alert will be displayed just above the Veteran's *Income.*

# *Data Added to Claim Information Display*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Last Address Change Date 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

The BT system will display the current address of the patient from the Patient file, and the *Date* of the last change to the Veteran's *Address*.

## Current Year Income Test from Annual Means Test 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

The BT system displays a Current-Year Income Test when calculating BT Travel Benefits and when entering a Claim for a previous year. The information is automatically retrieved from the Annual Means Test file.

## Net Income and Status from Means Test 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

The BT system displays *Income* and *Status* information on the Beneficiary Travel Claim Information screen if available from non-expired Rx Co-pay or MT's. If the test is expired then the *Income* will be Ineligible and *Status* will be Expired. The Veteran's *Net Income* instead of Gross Income will be displayed if a valid, completed MT or Co-Pay test exists.

## Message on Service Connected Appointment Only 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

The BT system displays a message to the user if the Veteran is only eligible for reimbursement for *SC Conditions* if the Veteran is less than 30% SC, and does not pass the *Low-Income Eligibility* test.

## Public Transportation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

The BT system displays a new data item on the BT Claim Information Screen to account for Public Transportation (bus pass, etc.)

# *Deductible Waivers and Alternate Income* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Capture of Deductible Waiver Data 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: MAN Manual Deductible Waiver

The BT system allows a user to manually enter a deductible waiver for the remainder of a calendar year for a Veteran through a new option on the Beneficiary Travel menu. A manual waiver can only be edited by the site that created the original "Manual" waiver.

## Automatic Retrieval of Manual Waiver

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

The BT system automatically retrieves manual waivers, transparently to the user, from the local database and from any other site creating or editing a claim.

## Standardized Expiration of Authorized BT Waivers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

If the Veteran has an authorized waiver of the deductible in effect a message will display to alert the user to when the waiver expires. The waivers expire as follows:

- If the Veteran receives any type of Pension the message "PENSION" will display.
- If the Veteran qualifies because the income is below the Low Income Threshold, based on the Means Test or Rx Co-pay test, the message will display the date the Means Test or Rx Co-pay test expires.
- All others will expire at the end of the current calendar year.

## Alternate POW Processing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: ALT BT Alternate Income Enter/Edit

The VistA system does not currently allow former POWs to complete MT or Rx co-pay tests and therefore does not have income information for such Veterans. However, former POWs will be eligible for BT benefits based upon their current income, so BT has been modified to allow manual entry of income information for former POWs.

## Current Hardship Processing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: ALT BT Alternate Income Enter/Edit

It is possible for a Veteran to have MT or Rx co-pay income information in VistA that is not representative of the Veteran's actual income. To account for this the BT system allows the user to manually enter income information for Veterans who are currently experiencing a hardship condition.

# *New Electronic Voucher Features*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Cash Reimbursement Form Changes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Reprint of 70-3542d form and final step in Main Menu: Claim Enter/Edit

The 70-3542d (Cash Reimbursement of BT Expenses) form generated by the BT system has been modified with a change to the static text regarding the amount payable. It also now includes the total monthly deductible and the number of one-way and round trips taken in the current calendar month.

# *Trips and Deductible Waivers Tracking Features*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## National Tracking of BT Deductible in a Calendar Month 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

BT deductions in each calendar month are tracked nationally. The system will count the number of trips and amount of deductible paid during the current month at all sites the patient has visited during the current month. The BT system was also modified to credit the trips to the deductible cap for the current month. The BT system has been modified to track and display:

- the total number of one-way and round trips the Veteran has made to any VAMC under account 829 or 827 in the current calendar month
- the total dollar amount deducted during the current calendar month for all such trips

The BT system was also modified to determine if the Veteran has qualified to have the deductible waived for a mileage claim and display this information on the Beneficiary Travel Claim Information screen. If the Veteran qualifies to have the deductible waived for a mileage claim (account 829) the BT system also sets the deductible amount to \$0 in the claim.

The BT system now displays the following information about claims from other sites:

- Number of trips in the past month
- Deductible amount
- Waiver information

This information is displayed for all facilities visited in the last month.

## ## Entering Two Different Types of Waivers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Main Menu: Claim Enter/Edit

The BT system now allows users to enter two different types of waivers of a patient's deductible amount:

- Alternate Income Waiver - this is entered through the BT Alternate Income Enter/Edit option, and covers two status types, Hardship and POW. A patient would be given a Hardship waiver if there is a current Means Test or Rx Co-Pay test in VistA and their income or other situation has created a temporary financial hardship determined by the BT clerk. Alternate income for a hardship case will expire at the end of the current year. Normally the Registration/Enrollment system does not allow Means tests or Rx Co-pay tests to be entered for POW's as they are automatically waived by the system for any visit deductible or co-pays. But POW's are not automatically eligible for travel reimbursement. If a BT clerk determines a POW is below the low income threshold this can now be entered through the BT Alternate Income Enter/Edit option, and the deductible will be waived. Alternate Income for a POW will expire 365 days from date of entry.
- "Manual" Waiver - entered through the new Manual Deductible Waiver option as a catch all determined by the BT clerk. A patient can be entered into the Manual Deductible Waiver option if the clerk first determines they are considered below the low income threshold, but this information is not stored elsewhere in the Registration/Enrollment package. This waiver will expire at the end of the current year.

# *New BT Reports*Main Menu: RPTS Beneficiary Travel Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The reporting functionality was inadequate for users to quickly and easily generate reports at the National, VISN and Facility levels. The reporting capabilities provided by the BT system were enhanced to allow users to do the following:

- Run any report manually on demand, optionally queuing to run later
- Specify the timeframe for the data to be included in the report
- Export results from any report into Microsoft Excel
- Print any report to a facility printer

### Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Summary Report provides statistical totals for analysis of facility BT funds expended, claims processed, claim denials, alternate transportation usage, and Veteran eligibility demographics during a specified timeframe.

### Audit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Audit Report provides information to audit claims for accuracy.  

### Clerk Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Clerk Report retrieves information about claims entered by a specific BT clerk.

### Fiscal Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Fiscal Report print a sub-set of the fields on the 70-3542d Voucher form for a specified date range. This report can also be exported as a text file for import into other software.

### Travel Pattern Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Travel Pattern Report will be used to analyze distance/location to Veteran claims for unique travel patterns.

### Special Mode Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Special Mode Report will be used to analyze information on Special Mode claims.

Reports can either be printed or exported to an Excel file.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: DGBT*1*32 Release Notes

## Install the CA SiteMinder WebAgent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This part will need to be done at each Web Server (which means that this will probably be done once per Region).

As a part of the Identity Access Management (IAM) teams [VistA Integrated Web Applications](http://vaww.oed.portal.va.gov/sites/vrm/IAM/playbooks/Pages/PIV%20Compliance/VistA/VistA%20Integrated%20Web%20Applications.aspx) integration pattern, the [CA SiteMinder WebAgent](http://vaww.oed.portal.va.gov/sites/vrm/IAM/playbooks/Pages/SSOi/CA%20SiteMinder%20WebAgent.aspx) must be installed on the Beneficiary Travel Dashboard web server. Upon verifications that the required IP addresses and ports are open on the web server, the IAM team will provide a separate CA SiteMinder WebAgent Installation Guide as well as configuration instructions.

Export the Web Server Certificate

You will need to export the web server certificate and private key, used to encrypt your Beneficiary Travel Dashboard URLs, to a .pfx file.

## Export the Web Server Certificate to .pfx File in IIS 7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions from: <https://www.digicert.com/ssl-support/pfx-import-export-iis-7.htm>

1.  On the Web Sever in the Start menu click Run and then type *mmc*.
2.  Click File \> Add/Remove Snap-in.
3.  Click Certificates \> Add.
4.  Select Computer Account and then click Next. Select Local Computer and then click Finish. Then close the add standalone snap-in window and the add/remove snap-in window.
5.  Click the + to expand the certificates (local computer) console tree and look for the personal directory/folder. Expand the certificates folder.
6.  Right-click on the certificate you want to backup and select ALL TASKS \> Export.
7.  Choose Yes, export the private key and include all certificates in certificate path if possible.  
    Warning: Do not select the delete private key option.
8.  Leave the default settings and then enter your password if required.
9.  Choose to save the file and then click Finish. You should receive an "export successful" message. The .pfx file is now saved to the location you selected.

Once you have the .pfx file, you will need to send it to the IAM team.

## Separate the Private Key and SSL Certificate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You will need to separate your web server Private Key and SSL Server Certificate from the .pfx file created in the previous step. You can use the OpenSSL commands below to create the two files.

openssl pkcs12 -in certificate.pfx -nocerts -out private_key.pem -nodes

openssl pkcs12 -in certificate.pfx -nokeys -out certificate.cer

The newly generated .pem and .cer files will be used in the next step.

(Note: If you do not have access to OpenSSL, please open a CA ticket with the NTL.APP.VistA.Bene Travel 1_0 Dashboard group and ask for your ticket to be escalated to Tier 3.)

## Cache SSL/TLS Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Cache System Management Portal click 'SSL/TLS Configuration':

![](dgbt-1-32-release-notes/002.png)

Click 'Create New Configuration':

![](dgbt-1-32-release-notes/003.png)

Enter the fields as shown below:

- Ensure that your configuration name is 'dashboardssoi'.
- Under 'This client's credentials'
  - The 'File containing this configuration's X.509 certificate' is the SSL certificate from the web server (.cer).
  - The 'File containing associated private key' is the private key file created earlier in this guide (.pem).

![](dgbt-1-32-release-notes/004.png)

Click 'Save'.

## Import the XML file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use Caché Studio to import the source code XML.

> **NOTE:** Caché Studio should be connected to your VistA server in your station's namespace.

1.  Click the Tools menu and select Import Local.

![](dgbt-1-32-release-notes/005.png)

Caché\>Studio\>Tools\>Import Local

![](dgbt-1-32-release-notes/006.png)

Beneficiary Travel – Studio Open window

2.  Browse to the DGBT_1_32.xml file retrieved from download.vista.med.va.gov.
3.  Click the Open button.

![](dgbt-1-32-release-notes/007.png)

Beneficiary Travel – Studio Import window

4.  Ensure the Add Imported Items to Project checkbox is not selected and that Compile Imported Items is selected.
5.  Click the OK button to import the Beneficiary Travel Dashboard .csp and .cls project files.

The End.
