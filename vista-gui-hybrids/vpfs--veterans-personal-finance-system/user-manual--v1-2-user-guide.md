---
title: VPFS Version 1.2 User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: 
app_code: VPFS
app_name: Veterans Personal Finance System
section: GUI
app_status: active
pkg_ns: VPFS
patch_ver: 1.2
patch_id: VPFS*1.2
group_key: "VPFS:VPFS:1.2"
file_numbers: []
security_keys: []
menu_options: 0
description: > The purpose of this manual is to provide a step-by-step guide to using the VPFS application to manage patient funds.
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - blockquote
  - table
  - contents
  - strong
  - patient
  - class
  - vpfs
  - version
  - guide
  - style
page_count: 0
word_count: 12236
section_count: 112
table_count: 0
figure_count: 0
appendix_count: 6
has_toc: False
is_stub: False
pub_date: July 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VPFS/vpfs_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/VPFS/vpfs_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=170"
---

---
title: |
  Veterans Personal Finance System (VPFS)

  User Guide
---

> Version 1.2.0

![](vpfs-version-1-2-user-guide/001.png)

> July 2020

> U.S. Department of Veterans Affairs Health Systems Design & Development

### Document Approval Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 44%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Title: Project Manager</p>
</blockquote></th>
<th><blockquote>
<p>Signed: [signature on file] Typed: <mark>REDACTED</mark></p>
</blockquote></th>
<th><blockquote>
<p>Date:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Title: SQA Manager</p>
</blockquote></td>
<td><blockquote>
<p>Signed: [signature on file] Typed: <mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p>Date:</p>
</blockquote></td>
</tr>
</tbody>
</table>

> History of Revisions

> The following table contains a history of revisions for the User’s Manual.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 36%" />
<col style="width: 15%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Section Changed</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description of Change</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Effective Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Contacts</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Initial release of VPFS User Guide</p>
</blockquote></td>
<td><blockquote>
<p>10/20/06</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Figures 6.4 and</p>
<p>7.3</p>
<p>Sections 8.2.8,</p>
<p>8.2.11 and other</p>
</blockquote></td>
<td><blockquote>
<p>Updates screen captures. Deleted list item: access privileges for Patient Fund Supervisor.</p>
<p>Other updates as listed in CQ 712</p>
</blockquote></td>
<td><blockquote>
<p>01/18/07</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Updated Figure</p>
</blockquote></td>
<td></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>7.4</p>
</blockquote></td>
<td></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1.1.1</p>
</blockquote></td>
<td><blockquote>
<p>Figure 2-5,</p>
<p>page 18</p>
</blockquote></td>
<td><blockquote>
<p>Updated figures:</p>
<p>“Change Institution” and “Cancel” buttons are now located under the institution list.</p>
</blockquote></td>
<td><blockquote>
<p>06/05/2008</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Figure F-8, Appendix F, page 104</p>
</blockquote></td>
<td><blockquote>
<p>New field “Transaction Date” added to the fiscal transaction summary report.</p>
</blockquote></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Appendix B Glossary</p>
</blockquote></td>
<td><blockquote>
<p>VPFS is defined as Veterans Personal Finance System instead of Veterans Personal Funds System.</p>
</blockquote></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1.1.2</p>
</blockquote></td>
<td><blockquote>
<p>Section 2.1</p>
</blockquote></td>
<td><blockquote>
<p>Modified EVS to EPS.</p>
<p>New VPFS KAAJEE login screen Added a note about Access/Verify code.</p>
<p>These changes are associated with the VPFS patch release 1.1.2</p>
</blockquote></td>
<td><blockquote>
<p>06/23/2009</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 17%" />
<col style="width: 36%" />
<col style="width: 15%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1.1.3</p>
</blockquote></th>
<th><blockquote>
<p>Page 38 ,</p>
<p>Page 42</p>
<p>Page 17</p>
</blockquote></th>
<th><blockquote>
<p>Updated transaction date field information.</p>
<p>Updated „About Screen‟ page Footer version changed to 1.1.3</p>
<p>These changes are associated with the VPFS patch release 1.1.3</p>
</blockquote></th>
<th><blockquote>
<p>06/28/2010</p>
<p>12/20/2010</p>
</blockquote></th>
<th><mark>REDACTED</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.2.0</p>
</blockquote></td>
<td><blockquote>
<p>Page 18-19</p>
</blockquote></td>
<td><blockquote>
<p>Updated with 2FA Single Sign on with PIV Credentials</p>
</blockquote></td>
<td><blockquote>
<p>12/1/2018 –</p>
<p>02/05/2020</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> This page is left blank intentionally.
### List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure 1-1. Select Patient Page (graphic version) Figure 1-2. Select Patient Page (text version) Figure 2-1. VPFS Login Page
> Figure 2-2. VPFS Welcome Page
> Figure 2-3. Elements of VPFS Screen (graphic version) Figure 2-4. About Window
> Figure 2-5. Change Institution page Figure 2-6. Sample Banner
> Figure 2-7. Tabs
> Figure 2-8. Sample Work Area (Account Page)
> Figure 2-9. Example of Required Field Figure 2-10. Sample Selection Table Figure 2-11. Sample Calendar Control
> Figure 2-12. Elements of VPFS Screen (text version)
> Figure 3-1. Select Patient Page
> Figure 3-2. Balance Verification Window Figure 3-3. Patient Funds Patient Account Card
> Figure 4-1. Register Patient Page with Partially Displayed Patient Lookup Window Figure 4-2. Register Patient Page with Patient Lookup Window
> Figure 4-3. Patient Lookup with Available List Figure 4-4. Patient Lookup with Selected Filter Figure 6-1. Patient List Confirmation Window
> Figure 6-2. Post Multiple Transactions – Common Information Page Figure 6-3. Post Multiple Transactions: Select Patients Page
> Figure 6-4. Post Multiple Transactions – Individual Information Page
> Figure 6-5. Post Multiple Transactions - Individual Information Confirmation Page Figure 7-1. Account Tab
> Figure 7-2. Account Page
> Figure 7-3. Post Transaction Page
> Figure 7-4. Post Transaction Confirmation Page Figure 7-5. Balance Verification Window Figure 7-6. Patient Page
> Figure 7-7. Select Provider Page
> Figure 7-8. Select Provider Page with Providers Figure 7-9. Patient Detail Window
> Figure 7-10. Patient Funds Information Display Window Figure 7-11. Patient Funds Patient Account Card
> Figure 7-12. Guardians Page Figure 7-13. Transactions Page
> Figure 7-14. Patient Funds Master Transaction Display Figure 7-15. Suspense Page
> Figure 7-16. Log Page
> Figure 8-1. Administration Menu Figure 8-2. Sample Administration Page Figure 8-3. Maintain Form Types page
> Figure 8-4. Maintain Payee Types Page Figure 8-5. Maintain Remarks Page
> Figure 8-6. Maintain Income Source Types Page Figure 8-7. Maintain Reference Types Page Figure 8-8. Maintain Institutions Page
> Figure 8-9. Maintain Patient Types Page Figure 8-10. Maintain Award Frequencies Page Figure 8-11. Maintain Patient Statuses
> Figure 8-12. Maintain Help Text Page Figure 8-13. Maintain Payment Types Page
> Figure 8-14. Maintain System Parameters Page Figure 8-15. Maintain User Account Page Figure 9-1. Run Reports Page
> Figure 9-2. File Download Window Figure 10-1. Select Suspense Page Figure F-1. Account Balances
> Figure F-2 Activity Audit Listing Report Figure F-3. Date Variance Report
> Figure F-4. Deceased Patient with a Balance
> Figure F-5. Discharged Patient with a Balance Figure F-6. Dormant Account Listing
> Figure F-7. Fiscal Audit Report
> Figure F-8. Fiscal Transaction Summary Report Figure F-9. Inactive Withdrawal Listing
> Figure F-10. Indigent Patient Listing Figure F-11. Min and Max Restrictions Figure F-12. Negative Balance Report Figure F-13. Overdue Restriction Search Figure F-14. Patient Listing
> Figure F-15. Patient Summary Report Figure F-16. Productivity Report Figure F -17 Station Balances Report Figure F-18. Transaction Listing

# About This Document


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Document Approval Signatures](#document-approval-signatures)
    - [List of Figures](#list-of-figures)
- [About This Document](#about-this-document)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [Conventions Used in this Document](#conventions-used-in-this-document)
  - [Business Process Notes](#business-process-notes)
- [Overview of VPFS](#overview-of-vpfs)
  - [What is VPFS?](#what-is-vpfs)
  - [System Requirements](#system-requirements)
  - [User Roles and Access to Functions](#user-roles-and-access-to-functions)
  - [User Roles and Access to Reports](#user-roles-and-access-to-reports)
  - [Electronic Signature (E-signature)](#electronic-signature-e-signature)
  - [Automatic Timeout](#automatic-timeout)
  - [Section 508 Accessibility](#section-508-accessibility)
- [Getting Started](#getting-started)
  - [Accessing VPFS](#accessing-vpfs)
  - [Graphic Version Screen Components](#graphic-version-screen-components)
  - [Popup Windows](#popup-windows)
  - [Left Panel](#left-panel)
  - [![](vpfs-version-1-2-user-guide/023.png)Top Menu Bar](#vpfs-version-1-2-user-guide023pngtop-menu-bar)
  - [![](vpfs-version-1-2-user-guide/029.png)Banner](#vpfs-version-1-2-user-guide029pngbanner)
  - [Tabs](#tabs)
  - [Work Area](#work-area)
  - [Bottom Button Bar](#bottom-button-bar)
  - [Fields](#fields)
  - [![](vpfs-version-1-2-user-guide/050.png)Selection Table](#vpfs-version-1-2-user-guide050pngselection-table)
  - [Calendar Control](#calendar-control)
  - [Shortcut Keys](#shortcut-keys)
  - [Menu Options](#menu-options)
  - [Selection Tables](#selection-tables)
- [Selecting Patients](#selecting-patients)
  - [![](vpfs-version-1-2-user-guide/071.png)![](vpfs-version-1-2-user-guide/072.png)![](vpfs-version-1-2-user-guide/073.png)![](vpfs-version-1-2-user-guide/074.png)Top Menu Bar Options](#vpfs-version-1-2-user-guide071pngvpfs-version-1-2-user-guide072pngvpfs-version-1-2-user-guide073pngvpfs-version-1-2-user-guide074pngtop-menu-bar-options)
  - [Searching For a Patient](#searching-for-a-patient)
  - [Filtering the List of Patients](#filtering-the-list-of-patients)
  - [Verify Balances](#verify-balances)
  - [Viewing / Printing Patient Cards for Multiple Patients](#viewing-printing-patient-cards-for-multiple-patients)
- [Registering a Patient](#registering-a-patient)
- [Transferring a Patient](#transferring-a-patient)
  - [Requesting a Transfer](#requesting-a-transfer)
  - [To Make a Transfer Request](#to-make-a-transfer-request)
  - [To Cancel a Transfer Request:](#to-cancel-a-transfer-request)
  - [Authorizing a Transfer](#authorizing-a-transfer)
  - [To Authorize a Transfer:](#to-authorize-a-transfer)
  - [To Deny a Transfer:](#to-deny-a-transfer)
- [Posting Multiple Transactions](#posting-multiple-transactions)
- [Working with the Patient Account](#working-with-the-patient-account)
  - [Account Tab](#account-tab)
  - [Post a Transaction](#post-a-transaction)
  - [Verify Balances](#verify-balances-1)
  - [Transfer Patient](#transfer-patient)
  - [Overriding Limits](#overriding-limits)
  - [Patient Tab](#patient-tab)
  - [![](vpfs-version-1-2-user-guide/120.png)View / Edit Patient Information](#vpfs-version-1-2-user-guide120pngview-edit-patient-information)
  - [Show Patient Detail](#show-patient-detail)
  - [Show Information Display](#show-information-display)
  - [Show Patient Card](#show-patient-card)
  - [Guardians Tab](#guardians-tab)
  - [Transactions Tab](#transactions-tab)
  - [Editing a Deferral Date](#editing-a-deferral-date)
  - [Showing the Transaction Display](#showing-the-transaction-display)
  - [Exporting Transactions](#exporting-transactions)
  - [Showing the Master Transaction Display](#showing-the-master-transaction-display)
  - [Suspense Tab](#suspense-tab)
  - [Filter the List of Suspense Items](#filter-the-list-of-suspense-items)
  - [Edit a Suspense Item](#edit-a-suspense-item)
  - [Add a Single Suspense Item](#add-a-single-suspense-item)
  - [Add a Recurring Suspense Item](#add-a-recurring-suspense-item)
  - [Cancel a Suspense Item](#cancel-a-suspense-item)
  - [Cancel a Recurring Suspense Item](#cancel-a-recurring-suspense-item)
  - [Cancel all Transactions on a Specified Date](#cancel-all-transactions-on-a-specified-date)
  - [Log Tab](#log-tab)
- [Editing Dropdown Lists (Administration)](#editing-dropdown-lists-administration)
  - [Administration Menu](#administration-menu)
  - [Working with Administration Pages](#working-with-administration-pages)
  - [Editing the List of Form Types](#editing-the-list-of-form-types)
  - [Editing the List of Payee Types](#editing-the-list-of-payee-types)
  - [Editing the List of Remarks](#editing-the-list-of-remarks)
  - [Editing the List of Income Source Types](#editing-the-list-of-income-source-types)
  - [Editing the List of Reference Types](#editing-the-list-of-reference-types)
  - [Editing the List of Institutions](#editing-the-list-of-institutions)
  - [Editing the List of Patient Types](#editing-the-list-of-patient-types)
  - [Editing the List of Award Frequencies](#editing-the-list-of-award-frequencies)
  - [Editing the List of Patient Statuses](#editing-the-list-of-patient-statuses)
  - [Editing the List of Help Text](#editing-the-list-of-help-text)
  - [Editing the List of Payment Types](#editing-the-list-of-payment-types)
  - [Editing System Parameters](#editing-system-parameters)
  - [Editing User Account](#editing-user-account)
- [Viewing / Printing Reports](#viewing-printing-reports)
  - [Run a Report](#run-a-report)
  - [Print a Report](#print-a-report)
  - [Export a Report](#export-a-report)
- [Selecting Suspense Items](#selecting-suspense-items)
  - [Appendix A. 508 Standards](#appendix-a-508-standards)
  - [Standards](#standards)
    - [Paragraph (a)](#paragraph-a)
    - [Paragraph (d)](#paragraph-d)
    - [Paragraph (l)](#paragraph-l)
    - [Paragraph (o)](#paragraph-o)
    - [Paragraph (p)](#paragraph-p)
  - [Appendix B. Glossary](#appendix-b-glossary)
  - [Appendix C. Acronyms and Abbreviations](#appendix-c-acronyms-and-abbreviations)
  - [Appendix D. Frequently Asked Questions](#appendix-d-frequently-asked-questions)
  - [Appendix E. VPFS User Roles and Functions](#appendix-e-vpfs-user-roles-and-functions)
  - [Basic Official User](#basic-official-user)
  - [Basic Patient Funds Clerk](#basic-patient-funds-clerk)
  - [Lead Patient Funds Clerk](#lead-patient-funds-clerk)
  - [Patient Funds Clerk Supervisor](#patient-funds-clerk-supervisor)
  - [Fiscal Management](#fiscal-management)
  - [VPFS System Administrator](#vpfs-system-administrator)
  - [VPFS Security Administrator](#vpfs-security-administrator)
  - [Appendix F. Report Samples Account Balances](#appendix-f-report-samples-account-balances)
  - [Activity Audit Listing](#activity-audit-listing)
  - [Date Variance Report](#date-variance-report)
  - [Deceased Patient with a Balance](#deceased-patient-with-a-balance)
  - [![](vpfs-version-1-2-user-guide/287.png)Discharged Patient with a Balance](#vpfs-version-1-2-user-guide287pngdischarged-patient-with-a-balance)
  - [Dormant Account Listing](#dormant-account-listing)
  - [Fiscal Audit Report](#fiscal-audit-report)
  - [Fiscal Transaction Summary Report](#fiscal-transaction-summary-report)
  - [Inactive Withdrawal Listing](#inactive-withdrawal-listing)
  - [Indigent Patient Listing](#indigent-patient-listing)
  - [Min and Max Restrictions](#min-and-max-restrictions)
  - [Negative Balance Report](#negative-balance-report)
  - [Overdue Restriction Search](#overdue-restriction-search)
  - [Patient Listing](#patient-listing)
  - [Patient Summary](#patient-summary)
  - [Productivity Report](#productivity-report)
  - [Station Balances](#station-balances)
  - [Transaction Listing](#transaction-listing)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this manual is to provide a step-by-step guide to using the VPFS application to manage patient funds.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The audience for this document consists of staff members at the VistA site who use VPFS to manage patient accounts, including all of the following:

> ![](vpfs-version-1-2-user-guide/002.png)Basic Official Users Patient Funds Clerk (PFC) Lead PFC

> PFC Supervisor Fiscal Management

> VPFS System Administrator VPFS Security Administrator

## Conventions Used in this Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Format</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Indicates…</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>bold</strong></p>
</blockquote></td>
<td><blockquote>
<p>A control that you click, such as a button, icon, or link, or a field label.</p>
<p>Example: Click <strong>Search</strong>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Shortcut key combinations</p>
</blockquote></td>
<td><blockquote>
<p>A key combination that you press to perform a specific action or to move the cursor to a specific location on the page. Press and hold the first key then press the second key.</p>
<p>Example: Alt + S to save.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Additional Resources

> Additional VPFS documentation is available in the Health*<u>e</u>*Vet section of the VistA Documentation Library (VDL) website: [<u>http://www.va.gov/vdl/default.asp</u>](http://www.va.gov/vdl/default.asp)

## Business Process Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A copy of the Business Process Notes table is provided at the end of each chapter. Use this page to jot down notes about the changes to business processes that will be required due to the differences between PFOP and VPFS.

# Overview of VPFS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## What is VPFS?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Veterans Personal Finance System (VPFS) is the mini-banking system used by the Veterans Health Administration (VHA) to manage the accounts of VHA patients in the VHA hospital system. VPFS replaces the Personal Funds of Patients (PFOP) system that was used previously. VPFS looks different from PFOP because it is a web-based application; however, its design and functionality are modeled after PFOP. You can perform all the functions in VPFS that were available in PFOP, with the exception of a few functions that are no longer needed because of the newly built-in security controls.

> One of the major changes is that VPFS is a centralized system. With PFOP, each site used a stand-alone copy of the software and there were differences between local versions, such as data structures, business rules, etc. With VPFS, all sites access the same centralized application using a web browser over the VHA secure Intranet. VPFS stores all data for all sites in one centralized database. Access to the data in the database is controlled by security software that limits access according to your VistA site and user role.

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To use the VFPS application:

- JavaScript must be enabled on the PC
- You must have access to the VHA Intranet via one of the following browsers:
  - Microsoft Internet Explorer version 6.0 or higher with SP2, or
  - Netscape 7.1 or higher
- Standard 28-bit encrypted security (SSL) must be implemented. You must have an authorizing user account including:
  - Defined user role
  - Security-approved Access and Verify code pair

> This page is left blank intentionally.

## User Roles and Access to Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As in Personal Funds of Patients (PFOP), the level of access to data and functions in VPFS varies depending on job function. However, VPFS user roles are more strictly defined. Your administrator will work with you to determine the most appropriate level of access for your job function. Table 1-1 lists typical access assignments based on user role.

> Table 1-1. User Roles and Access to Functions

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>User Role Read-Only</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Data Entry</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Basic Official Users</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>View selected patient and account information No reporting privileges</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Basic PFC</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td><blockquote>
<p>Search for patients Register patients Request patient transfer Edit patient information Post transactions</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Lead PFC</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td><blockquote>
<p>Search for patients Register patients Request patient transfer Authorize patient transfer Edit patient information Post transactions</p>
<p>Override account restrictions Override deferral date restrictions</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PFC Supervisor</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td><blockquote>
<p>Search for patients Register patients Request patient transfer Authorize patient transfer Edit patient information Post transactions</p>
<p>Override account restrictions Override deferral date restrictions</p>
<p>Request application changes through Administration area</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Fiscal Management Users</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>View selected patient and account information No reporting privileges</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VPFS System Administrator</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td><blockquote>
<p>Implement authorized changes to common reference data</p>
<p>No patient record access</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VPFS Security Administrator</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>X</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>View selected patient and account information for purposes of data security</p>
</blockquote></td>
</tr>
</tbody>
</table>

## User Roles and Access to Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Table 1-2 lists the reports that are available through VPFS and indicates which users can produce each type of report.

> Table 1-2. User Roles and Access to Reports

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Report</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Basic PFC Lead PFC</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PFC Super</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Fiscal Management</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Enterprise User</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="6"><blockquote>
<p><strong>Patient Card Output Options</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Print Selected Cards</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td rowspan="5"></td>
<td rowspan="5"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Print All Cards</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Transaction Display</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Information Display</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Master Transaction Review</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="6"><blockquote>
<p><strong>Standard Reports</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Activity Audit Listing</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Dormant Account Listing</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Deceased Patient with a Balance</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Discharged Patient with a Balance</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Inactive Withdrawal Listing</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Indigent Patient Listing</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Overdue Restriction Search</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Patient Summary Report</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Min and Max Restrictions</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Patient Listing</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Account Balances</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Transaction Listing</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Fiscal Audit Report</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Fiscal Transaction Summary Report</strong></p>
</blockquote></th>
<th><blockquote>
<p>X</p>
</blockquote></th>
<th>X</th>
<th>X</th>
<th>X</th>
<th><blockquote>
<p>X</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Date Variance Report</strong></p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Negative Balance Report</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td>X</td>
<td>X</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Productivity Report</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Electronic Signature (E-signature)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To ensure security and provide audit information, all VPFS users with authority to post transactions, such as PFCs, lead PFCs, and PFC supervisors, must have an electronic signature code, or e-signature. Your

> e-signature is a secondary level of authentication and carries the same legal responsibilities as your written signature. It works in addition to your password to identify you. You must enter your e-signature when you confirm the transactions that you enter.

> Once you create your e-signature, do not share it with anyone. For your protection, your e-signature will be encrypted and will be unknown to anyone else, including computer programmers maintaining VPFS. If you forget your e-signature, it must be reset by a system administrator.

## Automatic Timeout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If your session is inactive for a predetermined length of time (typically 15 to 25 minutes) the system logs you out automatically and entries that you have not saved will be lost. A warning message appears 5

> ![](vpfs-version-1-2-user-guide/003.png)minutes before the timeout occurs. To continue working after the warning message appears: Enter and/or save entries on the current page. Navigate to a different page.

> If an automatic timeout occurs, you can log back in. The page where you were when the timeout occurred is redisplayed.

> Note: This security feature is equivalent to Automatic Interactive-session Time-out in PFOP.

## Section 508 Accessibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Section 508 is a federal law that requires software developers to provide equivalent web page access to users with visual impairment. The text version of VPFS provides this access with all of the functionality of the graphic version. The text version of VPFS is also helpful for users accessing VPFS via hand-held devices.

> Following is a brief list of features of the text version of VPFS:

> ![](vpfs-version-1-2-user-guide/004.png)Graphics that convey meaning in the graphic version are substituted with text. Navigation is via keyboard instead of mouse.

> Common assistive devices, such as screen readers, text enlargement, and alternate input devices are supported.

> For details about how VPFS meets specific requirements of Section 508, see <u>Appendix A</u>.

> Figure 1-1 and Figure 1-2 show samples of the graphic and text versions of the Select Patient page in VPFS.

> ![](vpfs-version-1-2-user-guide/005.png)

> Figure1-1. Select Patient Page(graphicversion)

![](vpfs-version-1-2-user-guide/006.png)

> Figure 1-2. Select Patient Page (text version)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Business Process Notes:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Accessing VPFS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Your VPFS log in grants you access based on the following:

> ![](vpfs-version-1-2-user-guide/007.png)Your affiliation with a VHA institution, or site, which determines the patient records that you can access.

> ![](vpfs-version-1-2-user-guide/008.png)Your role at the VHA site, which determines the VPFS functions that you can perform.

> To access VPFS:

1.  Contact Enterprise Product Support (EPS) for a current URL to the VPFS application.
2.  Open a web browser and enter the URL from EPS.

> The VPFS Single Sign-on page opens, click on Sign in with VA PIV Card.

![](vpfs-version-1-2-user-guide/009.png)

> Figure 2-1-1. VPFS Single Sign-on Page

3.  The PIV Authentication Page loads, choose your proper PIV credentials.

![](vpfs-version-1-2-user-guide/010.png)

> Figure 2-1-2. VPFS Single Sign-on Authentication Page

#### Enter your proper PIV pin.

![](vpfs-version-1-2-user-guide/011.png)

> Figure 2-1-3. VPFS Single Sign-on Authentication Pin Page

4.  The VPFS Login Page loads. Select your site from the dropdown list of institutions. Note: Current limitation of the IAM provisioning process has warranted an automatic inclusion of all the child stations of the parent stations that the user is provisioned for in the drop-down list. This was done to support the child station login functionality in the 2FA environment.

> .

5.  Click the Proceed button.

![](vpfs-version-1-2-user-guide/012.png)

> Figure 2-1-4. Login VPFS Proceed Page

> The VPFS Welcome page opens.

![](vpfs-version-1-2-user-guide/013.png)

> Figure 2-2. VPFS Welcome Page

6.  ![](vpfs-version-1-2-user-guide/014.png)Click any of the links on the VPFS Welcome page. To start the VPFS graphic version, click Start VPFS.

> ![](vpfs-version-1-2-user-guide/015.png)To start the VPFS text version, click Start VPFS (text-only). For more information about this section 508 compliant version of VPFS, see <u>Appendix A</u>.

> To open the Department of Veterans Affairs home page, click VHA Links. To open the User’s Guide for VPFS, click Users Guide.

> To open the Getting Started in VPFS document, click Getting Started. To open the PFOP Supervisor User Manual, click VHA Docs.

## Graphic Version Screen Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Start VPFS on the VPFS Welcome page, the graphic version of the VPFS application opens in a new window. The first menu item, Select Patient, is displayed.

> ![](vpfs-version-1-2-user-guide/016.png)

> Figure 2-3. Elements of VPFS Screen (graphic version)

## Popup Windows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VPFS uses popup windows for certain actions, such as displaying information and previewing and exporting reports. If you have popup blocker software running on your computer, these popup windows will not display when you click the action button.

> To temporarily override a popup blocker:

> Press and hold Ctrl while you click the button for the VPFS action you want to take.

## Left Panel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The left panel provides user information and a menu of links to the different areas of VPFS:

> About: To view system/user information, click About button.

![](vpfs-version-1-2-user-guide/017.png)

> Figure 2-4. About Window

- Software Versions: Software version numbers for the VPFS application, the database, the browser, and JavaScript. o Screen Resolution: Your current screen resolution setting.

> Note: If your resolution is less than 800/600 you will not be able to see the entire VPFS Web page.

- User information: The name of the user who is currently logged in and the roles associated with the user.

> Note: The sample window shows all possible roles.

> ![](vpfs-version-1-2-user-guide/018.png)User: Displays the name and station number of the current VPFS user. If you are authorized to access multiple sites, the change institution button appears to the right of your username and station ID.

> ![](vpfs-version-1-2-user-guide/019.png)

1.  ![](vpfs-version-1-2-user-guide/020.png)Click the change .

> The Change Institution page opens.

> institution button

> ![](vpfs-version-1-2-user-guide/021.png)

> Figure 2-5. Change Institution page

2.  Click the down arrow and select the institution from the dropdown list.
3.  Click Change Institution.

> The Select Patient page opens with the list of patients for the institution you selected. The station ID displayed in the left panel changes.

> ![](vpfs-version-1-2-user-guide/022.png)Menu: Provides links to the different areas of VPFS and the link to log out of VPFS.

- Select Patient: Access this area to locate the patient you want to work with. From Select Patient you can also register patients and post multiple transactions.
- Administration: Access this area to edit the values that appear in dropdown lists. Options on this menu require certain user roles. Only the options for which you have access appear in the menu. PFC supervisors can make certain local changes. System administrators make global changes that affect all sites. If you do not have access to

> these menu options, request changes through your PFC supervisor or system administrator.

- Reports: Access this area to view, print, and export reports.
- Suspense: Access this area to view, access, and cancel suspense records. o Logout:

> Click to log out of VPFS.

> Caution: Clicking the “X” close box on the window will *not* log you out! Be sure to click the Logout menu option to securely exit the application.

> Help: Displays help text related to the current page or field.

## ![](vpfs-version-1-2-user-guide/023.png)Top Menu Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](vpfs-version-1-2-user-guide/024.png)Menu Options: Menu options for tasks that are available from the page appear across the top menu bar.

> ![](vpfs-version-1-2-user-guide/025.png)Buttons: Buttons appear in the right-hand corner of the top menu bar for tasks that are available from the page. The following buttons are available on numerous pages:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 18%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Button</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Print Preview</p>
<p>![](vpfs-version-1-2-user-guide/026.png)</p>
</blockquote></td>
<td><blockquote>
<p>Click this button to view the current page in your browser window. Once displayed, you can print the page using the browser’s print function.</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>![](vpfs-version-1-2-user-guide/027.png) Previous</p>
</blockquote></td>
<td><blockquote>
<p>Move to the previous item in the list.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Select</p>
</blockquote></td>
<td><blockquote>
<p>Select the current item.</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>![](vpfs-version-1-2-user-guide/028.png) Next</p>
</blockquote></td>
<td><blockquote>
<p>Move to the next item in the list.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## ![](vpfs-version-1-2-user-guide/029.png)Banner

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a patient is selected, the banner displays information about the current account.

> ![](vpfs-version-1-2-user-guide/030.png)

> Figure 2-6. Sample Banner

- Name: Patient's last name, first name, middle initial
- DOB: Patient's date of birth. If the patient is deceased, the patient's date of death (DOD) is shown also.
- SSN: Patient's Social Security Number
- Claim ID: Medical claim number
- Available Balance: Amount that is currently available for withdrawal
- Patient Type: U=unrestricted; R=restricted; L=limited unrestricted; U=unrestricted; X=unknown
- Ward: Ward where the patient is registered
- Station: Station where the patient is registered
- Total Balance: Total balance in the patient's account
- Deferred Balance: Deferred balance in the patient's account
- Private Source: Amount of balance from private source
- Gratuitous: Amount of balance from gratuitous source

> Getting started

## Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a patient account is selected, the following tabs appear across the top of the work area. Click a tab to access information and tasks related to the current patient account.

![](vpfs-version-1-2-user-guide/031.png)

> Figure 2-7. Tabs

> ![](vpfs-version-1-2-user-guide/032.png)Account: View account information for the current patient. From here you can click Post Transaction to post a transaction or click Verify Balance to verify the patient’s balances.

> ![](vpfs-version-1-2-user-guide/033.png)Patient: View and edit patient income information and add or remove income sources.

> ![](vpfs-version-1-2-user-guide/034.png)Guardians: View guardian information. You can designate the VA guardian as director payee and enter the name and / or title of the VA guardian.

> ![](vpfs-version-1-2-user-guide/035.png)Transactions: View transaction history for the selected patient. Use the fields at the top of the page to filter the list of transactions.

> ![](vpfs-version-1-2-user-guide/036.png)Suspense: View descriptions of suspense items in the patient’s records.

> ![](vpfs-version-1-2-user-guide/037.png)Log: View descriptions of specific activities on the patient account.

## Work Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The work area is the main part of the VPFS web page. This part of the page changes when you move from one menu item or tab to another or when the system responds to a request. The following example is of the work area for the Account tab.

> ![](vpfs-version-1-2-user-guide/038.png)

> Figure 2-8. Sample Work Area (Account Page)

## Bottom Button Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Buttons appear in the right-hand side of the bottom button bar to allow you perform actions, such as saving or canceling your entries or moving to the next page in a process:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 26%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Button</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](vpfs-version-1-2-user-guide/039.png)</p>
</blockquote></td>
<td><blockquote>
<p>Save</p>
</blockquote></td>
<td><blockquote>
<p>Save your entries.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vpfs-version-1-2-user-guide/040.png)</p>
</blockquote></td>
<td><blockquote>
<p>Cancel</p>
</blockquote></td>
<td><blockquote>
<p>Clear any unsaved entries.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vpfs-version-1-2-user-guide/041.png)</p>
</blockquote></td>
<td><blockquote>
<p>Next</p>
</blockquote></td>
<td><blockquote>
<p>Move to the next page in the process.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Confirm Transaction</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Move to the page where you confirm the transaction.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](vpfs-version-1-2-user-guide/042.png)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vpfs-version-1-2-user-guide/043.png)</p>
</blockquote></td>
<td><blockquote>
<p>Cancel Transaction</p>
</blockquote></td>
<td><blockquote>
<p>Cancel the transaction.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Different types of fields are used for entering data in different ways as listed in the following table.

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 29%" />
<col style="width: 6%" />
<col style="width: 25%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p><strong>Type of Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>How to Use</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>![](vpfs-version-1-2-user-guide/044.png)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Text Field</p>
</blockquote></td>
<td><blockquote>
<p>Type data in the field.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>![](vpfs-version-1-2-user-guide/045.png)</td>
<td></td>
<td><blockquote>
<p>Dropdown List</p>
</blockquote></td>
<td><blockquote>
<p>1. Click the down arrow on the right to open a dropdown list of valid</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="3"><blockquote>
<p>entries.</p>
<p>2. Select an entry from the list.</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>![](vpfs-version-1-2-user-guide/046.png)</td>
<td></td>
<td><blockquote>
<p>Combo Box</p>
</blockquote></td>
<td><blockquote>
<p>Provides both text field and dropdown list options:</p>
<p>Click the right arrow on the right to open a list of valid entries and select your entry from the list,</p>
<p>OR</p>
<p>type data in the field.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ![](vpfs-version-1-2-user-guide/047.png)![](vpfs-version-1-2-user-guide/048.png)Required Fields

> Required fields are marked with an asterisk (\*). If you leave a required field blank and attempt to save your entries or to continue to the next page in a process, an error window will display the name of the field that requires data.

> ![](vpfs-version-1-2-user-guide/049.png)

> Figure 2-9. Example of Required Field

## ![](vpfs-version-1-2-user-guide/050.png)Selection Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure 2-10. Sample Selection Table

> The results of search and filter entries are displayed in a selection table.

#### Sorting the Records in the List

> You can sort the list of records by clicking on any column heading. The sort order toggles between ascending and descending order.

> ![](vpfs-version-1-2-user-guide/051.png)Ascending Order: The first time you click on the column heading, all of the records in the selection table are sorted in ascending order by that column. The up arrow symbol ▲ appears to the right of the column heading to indicate that the current sort is in ascending order by that column.

> ![](vpfs-version-1-2-user-guide/052.png)Descending Order: The next time you click on the column heading, all of the records in the selection table are sorted in descending order by that column. The down arrow symbol ▼ appears to the right of the column heading to indicate that the current sort is in descending order by that column.

#### Suspense Column

> The header for the 5<sup>th</sup> column is the suspense icon ![](vpfs-version-1-2-user-guide/053.png). If a suspense item (reminder) is associated with the patient account, a suspense icon appears in the row for the patient. To view all suspense items for the patient, click the patient name to open the patient account tabs and then click the Suspense tab.

#### Moving Through the List of Records

> Up to 100 records can be displayed on a page in the selection table. Use the following features to move through the list of records.

> ![](vpfs-version-1-2-user-guide/054.png)![](vpfs-version-1-2-user-guide/055.png)![](vpfs-version-1-2-user-guide/056.png)Scroll Bar: Use the scroll bar on the right to scroll through the current page of records. Page arrows: If more than one page of records exists, use the arrows and page numbers to move through the pages.

> ![](vpfs-version-1-2-user-guide/057.png)Go to the first page of records.

> ![](vpfs-version-1-2-user-guide/058.png)Go to the previous page of records.

> ![](vpfs-version-1-2-user-guide/059.png)Go to the specific page for the number you click.

> ![](vpfs-version-1-2-user-guide/060.png)![](vpfs-version-1-2-user-guide/061.png)Go to the next page of records. Go to the last page of records.

## Calendar Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the calendar control to select the date for a field from a calendar. To use the calendar control:

1.  Click the calendar icon ![](vpfs-version-1-2-user-guide/062.png) to the right of the date field.

> The calendar control opens to today's date, or to the last date you selected.

> ![](vpfs-version-1-2-user-guide/063.png)

> Figure 2-11. Sample Calendar Control

2.  ![](vpfs-version-1-2-user-guide/064.png)![](vpfs-version-1-2-user-guide/065.png)Navigate to the month and year that you want using the dropdown lists or by clicking the previous month ( ) and next month ( ) arrows.
3.  Click the date that you want to enter in the current field. The calendar closes. The date is inserted in the field.

## Shortcut Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following shortcut keys are designed for use with both the graphic and the text versions of VPFS. Press and hold the Alt key, then press the associated key. This places the cursor on the control, such as an icon or button. Once the control is selected, press Enter to activate it.

## Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 83%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Patient</p>
</blockquote></th>
<th><blockquote>
<p>Alt+E</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Administration</p>
</blockquote></td>
<td><blockquote>
<p>Alt+D</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Reports</p>
</blockquote></td>
<td><blockquote>
<p>Alt+O</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Suspense</p>
</blockquote></td>
<td><blockquote>
<p>Alt+U</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Logout</p>
</blockquote></td>
<td><blockquote>
<p>Alt+G</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Top menu bar options. Cycle through: Register, Post Multiple Transaction Show Patient Card, View Selected Patient.</p>
</blockquote></td>
<td><blockquote>
<p>Alt+M</p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  Buttons and Tabs

<table>
<colgroup>
<col style="width: 83%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>S</u>ave</p>
</blockquote></th>
<th><blockquote>
<p>Alt+S</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><u>C</u>ancel</p>
</blockquote></td>
<td><blockquote>
<p>Alt+C</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><u>A</u>dd</p>
</blockquote></td>
<td><blockquote>
<p>Alt+A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><u>R</u>emove</p>
</blockquote></td>
<td><blockquote>
<p>Alt+R</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><u>N</u>ext</p>
</blockquote></td>
<td><blockquote>
<p>Alt+N</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>(<u>B</u>ack)</p>
</blockquote></td>
<td><blockquote>
<p>Alt+B</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><u>P</u>rint page</p>
</blockquote></td>
<td><blockquote>
<p>Alt+P</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Search and Filter buttons.</p>
<p>Cycle through: Search, Clear, Filter, Reset</p>
</blockquote></td>
<td><blockquote>
<p>Alt+F</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cycle through Tabs when tabs are present.</p>
</blockquote></td>
<td><blockquote>
<p>Alt+T</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Selection Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 76%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Column headings</strong>: Place the cursor on a heading in the selection table. Each time you press Alt+H the cursor moves to the next heading. Cycles through headings from left to right.</p>
</blockquote></th>
<th><blockquote>
<p>Alt+H</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Last Selection</strong>: Return the cursor to the most recently selected row in the selection table.</p>
</blockquote></td>
<td><blockquote>
<p>Alt+L</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Next Row</strong>: Place the cursor on the next row in the selection table.</p>
</blockquote></td>
<td>&gt;</td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Previous Row</strong>: Place the cursor on the previous row in the selection table</p>
</blockquote></td>
<td>&lt;</td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Page Number</strong>: Place the cursor on the page number in the page navigation at the top of the selection table.</p>
</blockquote></td>
<td><blockquote>
<p>Alt + (1-5)</p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  Text Version Components

> When you click Start VPFS (text-only) on the VPFS Welcome page, the text version of the VPFS applications opens in a new window. The first menu item, Select Patient, is displayed.

> ![](vpfs-version-1-2-user-guide/066.png)

> Figure 2-12. Elements of VPFS Screen (text version)

> The same components that are present in the graphic version are available in the text version, but are arranged differently:

> ![](vpfs-version-1-2-user-guide/067.png)Actions: Any buttons that appear in the top menu bar or bottom button bar of the graphic version are listed under the heading Actions in the text version in the lower left corner of the page.

> ![](vpfs-version-1-2-user-guide/068.png)Menu: Left panel menu items are listed under the heading Menu in the lower left corner of the page.

> ![](vpfs-version-1-2-user-guide/069.png)User: User identification information is listed under the heading User in the lower left corner of the page.

> ![](vpfs-version-1-2-user-guide/070.png)Help Text: Help text for the current page or field is displayed automatically in the left panel.

3\. Selecting Patients

# Selecting Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ![](vpfs-version-1-2-user-guide/071.png)![](vpfs-version-1-2-user-guide/072.png)![](vpfs-version-1-2-user-guide/073.png)![](vpfs-version-1-2-user-guide/074.png)Top Menu Bar Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To select patients:

1.  Click Select Patient from the menu in the left panel.

> The Select Patient page opens. All patients registered in VPFS at your site are listed in the selection table in alphabetical order by patient last name.

![](vpfs-version-1-2-user-guide/075.png)

> Figure 3-1. Select Patient Page

> Several features are available to make it easier for you to zero in on the patient or group of patients that you want to select. You can search through the list, filter the list, or search and filter the list by entering a combination of search and filter criteria. Once you display the list that you want, you can move through the list using the scroll bar, page numbers, and arrows.

> 3 Selecting Patients

## Searching For a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To search for a patient who is already registered in VPFS:

2.  Search Type: Select the type of data to search on, Patient Code, Last Name, or SSN.
3.  Search Range: Select the range for the search type you entered, Begins with, Contains, Ends with, or Equals.
4.  Search Text: Enter the text to search for in the search type and range you entered.

> For example: To find a patient whose last name begins with Cla, enter Search Type: Last Name, Search Range: Begins with, and Search text: Cla.

5.  Click Search.

> The list of patients that matches the search criteria you entered is displayed. To clear your entries and return to the complete list of patients, click Clear.

## Filtering the List of Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can use any of the filter fields alone or in combination with other filter fields. You can also use filter fields in combination with search fields. To clear your filter entries and start over, click Reset.

> To filter the list to include a specific group of patients:

6.  Enter criteria in any of the filter fields. Leave the default of All for any filter fields that you do not want to use:
    1.  Patient Type: Select the type of patient to include in the list, R-Restricted, L-Limited Unrestricted, U-Unrestricted, X-Unknown, Unknown\>30 days, or leave All.
    2.  In/Out Patient: Select In-patient, Out-patient, or leave All.
    3.  Guardian: Select Both, VA, Civil, None, or leave All.
    4.  Ward: Select a ward from the list or leave All.
    5.  Special: Select Deceased, Director Payee, Discharged, or leave All.
    6.  Balance: This filter field works in combination with the Amount filter field. Select the symbol that expresses the relationship with the balance amount. Select All, equals (=), greater than (\>), greater than or equal to (\>=), less than (\<), less than or equal to (\<=), or leave All.
    7.  Amount: This filter field works in combination with the symbol you entered in the Balance filter field. Enter the balance amount to be compared to the symbol you selected.
    8.  Account Status: Select the account status: Active, Inactive, or leave All.
    9.  Patient Status: Select the patient status: A-Adjudged Incompetent, R-Rated Incompetent, C-Competent, N-Not Rated, X-Unknown, O-Other, or leave All.

> For example: To include all in-patients for a specific ward, select In-patient from the In/Outpatient list and select the ward number from the Ward list, leaving all other filter fields set to All.

7.  Click Filter.

> The list of patient accounts that match the filter criteria, and search criteria if entered, is displayed.

8.  Selecting Patients

## Verify Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This function displays a message that indicates whether the total balance for all the patients in the current list is correct. It does not correct the balance. To verify the account balance for the current list of patients:

3.  Search and / or filter the list to include the patients whose accounts you want to include in the balance check.
4.  Click Verify Balances.

> A window displays a message indicating whether the balances are correct.

![](vpfs-version-1-2-user-guide/076.png)

> Figure 3-2. Balance Verification Window

5.  Read the message and click OK.

> If the message indicates a discrepancy, be sure to notify the appropriate fiscal authority. Unlike the legacy system PFOP, a discrepancy in VPFS indicates an error that needs to be corrected.

## Viewing / Printing Patient Cards for Multiple Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To view / print patient cards for multiple patients:

1.  Complete the steps in Section <u>3.2</u> and <u>3.3</u> to display the list of patients whose Patient Cards you want to view and/or print.
2.  Click the Show Patient Card option in the top menu bar. The Patient Funds Patient Account Card window opens.
3.  Selecting Patients

> ![](vpfs-version-1-2-user-guide/077.png)

> Figure 3-3. Patient Funds Patient Account Card

> The Patient Funds Patient Account Card displays account transaction information for all the selected patients. You can print this file using your browser's Print function.

4.  Registering a Patient

# Registering a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can register any patient in VPFS as long as the patient record already exists in the VistA Patient File. The record would be in the Patient File if:

> ![](vpfs-version-1-2-user-guide/078.png)The patient was previously registered in PFOP.

> The patient is registered at the hospital or institution (site).

> Notes: In PFOP, patients may have multiple accounts at different institutions. In VPFS, patients can only have a single patient account. This account can be transferred to another site if the patient moves. If the patient you are attempting to register has already been registered in VPFS at another institution, you will not be able to register them, however you will be able to request a transfer of that patient to your site. See Transferring a Patient for more information.

> Sensitive Records: The Patient Service Lookup facility (PSL) limits access to sensitive patient information based on the nature of the information and on the authorization level of the user. Before you are granted access to a sensitive patient record an alert will be displayed. If you choose to access the sensitive record, a bulletin will be sent to the Information Security Officer for the facility and an entry created in the Security Log file.

> To register a patient:

1.  Click Select Patient in the left panel. The Select Patient page opens.
2.  Click the Register option in the top menu bar of the Select Patient page.

> The Register Patient page opens with the Patient Lookup fields. This page provides an interface to PSL and allows you to search for patients in the Patient File.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Note:</strong></p>
</blockquote></th>
<th><blockquote>
<p>The PSL window may not be fully visible when it is initially displayed. You may need to scroll right or expand the VPFS window to see the <strong>Search</strong> button on the right side of the page. See Figure 4-1. Register Patient Page with Partially Displayed Patient Lookup Window.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Note</strong>:</p>
</blockquote></td>
<td><blockquote>
<p>For complete information about using PSL, click <strong>Help</strong> in the upper right-hand corner of the Patient Lookup window.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 4 Registering a Patient

> ![](vpfs-version-1-2-user-guide/079.png)

> Figure 4-1. Register Patient Page with Partially Displayed Patient Lookup Window

![](vpfs-version-1-2-user-guide/080.png)

> Figure 4-2. Register Patient Page with Patient Lookup Window

3.  If you want to limit the list, select one of the filters in the Limit Patient Selection By: section. The list for the filter that you selected appears in the Available box.

> 4 Registering a Patient

> ![](vpfs-version-1-2-user-guide/081.png)

> Figure 4-3. Patient Lookup with Available List

4.  Select one or more items from the list in the Available box. (Hold down the Ctrl key to select multiple items.)
5.  Click \> to move the selected items to the Selected list.

![](vpfs-version-1-2-user-guide/082.png)

> Figure 4-4. Patient Lookup with Selected Filter

6.  Enter any of the following search criteria in the Select Patient field.

> Note: An asterisk (\*) can be used as a wildcard to search for all patients if you selected a filter in Limit Patient Selection By. An asterisk is not a valid entry in the Select Patient field otherwise.

> ![](vpfs-version-1-2-user-guide/083.png)Last name: Enter all or the first few characters of the patient’s last name. Must be at least 4 characters with no asterisk. For example: smit to search for all patients with the last name Smith.

> ![](vpfs-version-1-2-user-guide/084.png)Last name,first name: Enter all or part of the patient's last and first name, separated by a comma. For example: smit,j or sm,jo to search for Joe Smith. Must be at least 4 characters with no asterisk.

> ![](vpfs-version-1-2-user-guide/085.png)SSN: Enter the complete Social Security Number (do not include dashes „-‟ or spaces).

> ![](vpfs-version-1-2-user-guide/086.png)Patient Code: Enter the first letter of the patient’s last name followed by the last four digits in their SSN. For example, for a patient with the name of Joe Patient, SSN: 000-000001, you would type P0001 in the Select Patient field.

4.  Registering a Patient
    1.  Click Search.

> The list of patients that match the search criteria you entered is displayed. To clear your entries and return to the complete list of patients, click Clear Search. If more than one page of matches was found, use the Next link at the bottom of the page to go to the next page of results.

2.  Select the patient from the list.

> Any alerts associated with the patient record are displayed, one at a time. Refer to the PSL User Manual, Appendix B for more information about individual alerts.

3.  Read and click Continue to accept each alert.

> ![](vpfs-version-1-2-user-guide/087.png)If the patient is not already registered in VPFS, the Register Patient Confirmation page displays the demographic information for the patient. Continue with the next step.

> ![](vpfs-version-1-2-user-guide/088.png)If the patient is already registered in VPFS at a different site, the Transfer Patient page displays information about the patient you are attempting to register and the patient already registered. You can request a transfer of the patient to your site. See Transferring a Patient and Requesting a Transfer for more information.

> ![](vpfs-version-1-2-user-guide/089.png)If the patient is already registered in VPFS at the current site, an error message appears, click Cancel to cancel the registration and return to the Register Patient page.

4.  Review the demographic information to verify that this is the patient you want to register.
5.  Click Register Patient.

> The Select Patient page opens.

5.  Transferring a Patient

# Transferring a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Transferring a patient occurs in two stages:

1.  A patient transfer is requested by the site wanting the patient account transferred to them.
2.  The transfer is authorized (or denied) by the site that currently owns the patient account.

## Requesting a Transfer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you attempt to register a patient that has already been registered at another site, you will be given the option to request the transfer of that patient's account to your site. After you request a transfer of a patient, you need to contact the Patient Funds department at the current site to have them authorize the transfer (see section - Authorizing a Transfer.) Once they have authorized the transfer, the patient account will be transferred to your site and they will no longer be able to access that account.

> You can select View Patient to go directly to that patient account or go back to the Select Patient page and search for the patient there. If the patient account has not been transferred yet, you will get a message stating that you are not authorized to view the patient.

> To cancel a transfer requested by your site, click Cancel Request from the Request Transfer page.

## To Make a Transfer Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the Register Patient function to try to register the patient in VPFS (go through the normal Register Patient process.) If the patient has already been registered at another site, the Request Transfer page will be displayed. Click Request Transfer to submit a request to transfer the patient to your site.

> Note: You will be notified if the patient has a pending transfer request. There can be only one pending transfer request for a given patient account at a time. If another site has requested the transfer of the patient, you will need to wait until that request has been completed before you can request another transfer.

> Once you have requested a transfer of the patient, you need to contact the current site to have them authorize the transfer. In order to transfer a patient account, all available funds must be withdrawn (the available balance must be \$.00 (zero)) from that account at the current site and transferred to your site via TDA to be re-deposited. If the patient has outstanding deferred transactions, additional TDAs may be required to transfer those funds once they clear. Suspense items will be created for any outstanding deferred transactions to remind you to check their status with the current site.

## To Cancel a Transfer Request:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the Request Transfer page is still displayed, you cancel a pending transfer request by simply clicking the Cancel Request button. You will then return to the Register Patient page.

> If the Request Transfer page is no longer displayed, try to register the patient again using the Register Patient function. This will display the Request Transfer page, where you can click the Cancel Request button.

5.  Transferring a Patient

## Authorizing a Transfer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you select a patient that has a pending transfer request, the Transfer Patient button will be displayed on the Account page. Only Lead PFCs and PFC Supervisors have the ability to authorize or deny a patient transfer request.

> Clicking the Transfer Patient button displays the Transfer Patient page. This page displays information about the patient, as well as the name and station of the requestor. (Only one transfer request can be pending for a patient at a time.) Before a patient can be transferred, their available balance must be \$.00 (zero), so you may need to post a withdrawal transaction prior to authorizing a transfer. These funds would then be sent to the requesting station via TDA to be re-deposited in the account once the transfer has been completed. If there are any outstanding deferred transactions for the account, those amounts would need to be sent to the requesting station once they clear.

## To Authorize a Transfer:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Transfer Patient page, click on Authorize Transfer. The patient will be transferred immediately, and you will no longer have access to that patient account. The Select Patient page will be displayed.

## To Deny a Transfer:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Transfer Patient page, click on Deny Transfer. The transfer request will be cancelled and you will retain control of that patient account. The Account page will be displayed.

> Note: If you plan to deny a transfer for any reason, you should contact the person who requested the transfer and explain why the request will be denied. VPFS does not notify the requestor that a transfer request has been authorized or denied.

6\. Posting Multiple Transactions

# Posting Multiple Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you are processing single transactions for different accounts, you will often find yourself repeatedly entering the same preliminary information (e.g., Form, Reference, Remarks, etc.). To save time and avoid duplicated effort, VPFS (like PFOP) allows you to process a series of transactions in one session, using the Post Multiple Transactions option.

> To post multiple transactions:

1.  Click Select Patient in the left panel. The Select Patient page opens.
2.  Use the search and filter features to search and select the list of patients to whom you want to post transactions. (See Chapter 3 Selecting Patients for assistance.)
3.  Click the Post Multiple Transaction option in the top menu bar.

> A window opens asking if the current list of patients is the one you want.

![](vpfs-version-1-2-user-guide/090.png)

> Figure 6-1. Patient List Confirmation Window

4.  Verify that the list of patients is correct and click OK.

> The Post Multiple Transactions – Common Information page opens.

> ![](vpfs-version-1-2-user-guide/091.png)

> Figure 6-2. Post Multiple Transactions – Common Information Page

6.  Posting Multiple Transactions
    1.  Enter common transaction information. Be sure to enter data in all required fields (marked with \*).
        1.  Transaction Type: Select the Deposit or Withdrawal radio button.
        2.  Reference: Select or type reference text associated with this transaction.
        3.  Form: Select the VA form to use for the transaction.
        4.  Transaction Date: Enter the date for the transaction.
        5.  Source: Select the income source.
        6.  Payment Type: Select the payment type.
        7.  Remarks and Comments: Select a remark from the list, if applicable. Type a comment related to the remark you selected, if applicable. Click Add to add the remark and comment to the Remarks list. You can add additional remarks and comments by repeating this process.
    2.  Click Next to continue with the next post multiple transactions page. The Post Multiple Transactions: Select Patients page opens.

![](vpfs-version-1-2-user-guide/092.png)

> Figure 6-3. Post Multiple Transactions: Select Patients Page

3.  Select the checkbox for each patient to include in this set of transactions. To select all patients in the list, click the checkbox at the top of the Select column.
4.  Click Next to continue with the next post multiple transactions page. The Post Multiple Transactions – Individual Information page opens.

6\. Posting Multiple Transactions

> ![](vpfs-version-1-2-user-guide/093.png)

> Figure 6-4. Post Multiple Transactions – Individual Information Page

> Note: The entry fields that appear on this page are based on your entries on the first Post Multiple Transactions page.

5.  Enter transaction information for the current patient:

> ![](vpfs-version-1-2-user-guide/094.png)Amount: Enter the amount for the transaction.

> ![](vpfs-version-1-2-user-guide/095.png)Count in Restricted Balance: (Appears only if you are posting a withdrawal and withdrawals are restricted for this patient.) Select the checkbox if the transaction amount is to apply to the patient's restricted balance.

> ![](vpfs-version-1-2-user-guide/096.png)Deferral Date: (Appears only if you are posting a deposit made by check.) Enter a deferral date to allow time for the check to clear.

6.  Click Confirm Transaction.

> The Post Multiple Transactions – Individual Information confirmation page opens.

> 6 Posting Multiple Transactions

> ![](vpfs-version-1-2-user-guide/097.png)

> Figure 6-5. Post Multiple Transactions - Individual Information Confirmation Page

7.  ![](vpfs-version-1-2-user-guide/098.png)Review the transaction information to make sure it is correct. If correct, continue with the next step.

> ![](vpfs-version-1-2-user-guide/099.png)If not correct, click Edit Transaction to return to the previous page and edit the information.

8.  Enter your electronic signature code.
9.  Click OK.

> The system verifies your electronic signature and posts the transaction. One of the following occurs:

> ![](vpfs-version-1-2-user-guide/100.png)If additional patient accounts remain for this multiple transaction, the Post Multiple Transactions: Enter transaction page opens for the next patient in the list. Repeat steps 9 through 13 to enter the transaction information for the current patient.

> ![](vpfs-version-1-2-user-guide/101.png)If all transactions have been posted for this multiple transaction, the Select Patient page opens.

# Working with the Patient Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To work with an individual patient account:

1.  Search for the patient, as described in Chapter 3 Selecting Patients.
2.  To access the patient record:

> ![](vpfs-version-1-2-user-guide/102.png)Double-click on the patient's name (or anywhere on the row for the patient), OR

> ![](vpfs-version-1-2-user-guide/103.png)Click View Selected Patient in the top menu bar.

> The patient record tabs open. The sample below shows all possible tabs. The tabs that appear depend on the user roles assigned to the Access / Verify code pair that you used to log in to VPFS. To access a specific type of information in the patient record, click a tab.

![](vpfs-version-1-2-user-guide/104.png)

> Figure 7-1. Account Tab

## Account Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click the Account tab, or when you first access the patient record tabs, account information for the current patient is displayed on the Account page.

![](vpfs-version-1-2-user-guide/105.png)

> Figure 7-2. Account Page From

> the Account page you can:

> ![](vpfs-version-1-2-user-guide/106.png)View the account balance and related information, including monthly and weekly authorized withdrawal amounts (for restricted patients), total balance, deferred balance, and amount available for withdrawal.

> ![](vpfs-version-1-2-user-guide/107.png)Post a transaction.

> Verify the patient's balances.

> Transfer a patient to another institution.

## Post a Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To post a transaction for the current patient:

1.  Select Post Transaction.

> The Post Transaction page opens. Transaction information from the Account page appears at the top of the page.

![](vpfs-version-1-2-user-guide/108.png)

> Figure 7-3. Post Transaction Page

2.  Enter transaction detail:
    1.  Transaction Type: Select the Deposit or Withdrawal radio button.
    2.  Reference: Enter reference text associated with this transaction.
    3.  Amount: Enter the amount for the transaction.
    4.  Form: Select the VA form.
    5.  Transaction Date: Enter the date for the transaction.
    6.  Source: Select the income source.
    7.  Type: Select the payment type.
    8.  Count in Restricted Balance: (Appears only if you are posting a withdrawal and withdrawals are restricted for this patient.) Select the checkbox if the transaction amount is to apply to the patient's restricted balance.
    9.  Deferral Date: (Appears only if you are posting a deposit and you selected Source: Private Source and Type: Check.) Enter a deferral date to allow time for the check to clear. The deferral date cannot be more than 30 days past the transaction date.
    10. Remarks and Comments: Select a remark from the list, if applicable. Type a comment related to the remark you selected, if applicable. Click Add to add the remark and comment to the Remarks list. You can add additional remarks and comments by repeating this process.
3.  Click Confirm Transaction.

> Note: Override warnings may be displayed at this point. Your options will vary depending on your authorizations. See Section 7.1.4, below, for more information.

> Override Gratuitous Balance: If you select Gratuitous as the source of funds and attempt to withdraw an amount that exceeds the available balance in the Gratuitous category, the system will display a warning message. If you continue with the transaction, the transaction will first use all available gratuitous funds and take the remainder from the Private Source funds.

> The Post Transaction confirmation page opens.

![](vpfs-version-1-2-user-guide/109.png)

> Figure 7-4. Post Transaction Confirmation Page

4.  Review the transaction information to make sure it is correct.

> ![](vpfs-version-1-2-user-guide/110.png)If correct, continue with the next step.

> ![](vpfs-version-1-2-user-guide/111.png)If not correct, click Edit Transaction to return to the previous page and edit the information.

5.  Enter your electronic signature code.
6.  Click OK.

> The system verifies your electronic signature, posts the transaction, and reopens the Account tab for the current patient.

## Verify Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This function displays a message that indicates whether the total balance for the current patient is correct. It does not correct the balance.

> To verify the account balance for the current patient:

1.  Select Verify Balance.

> A window displays a message indicating whether the balances are correct.

![](vpfs-version-1-2-user-guide/112.png)

> Figure 7-5. Balance Verification Window

2.  Read the message and click OK.

> If the message indicates a discrepancy, be sure to notify the appropriate fiscal authority. Unlike the legacy system PFOP, a discrepancy in VPFS indicates an error that needs to be corrected.

## Transfer Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Transfer Patient button will appear for any patient with a pending transfer request for users with the Lead PFC or PFC Supervisor roles. When the user clicks this button, the Transfer Patient page displays the user and institution requesting the transfer, and instructions on how to authorize or deny the transfer. See Transferring a Patient for more information.

## Overriding Limits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The transaction you are posting may exceed the total balance, the available balance (the actual balance of funds available, not counting deferred amounts), or it may exceed the weekly or monthly limit placed on a restricted account.

> If you do not have authorization to override these conditions, the system will inform you of this. If you do have access to override available balances or limits placed on restricted accounts, the system will warn you that the transaction exceeds a limit and will ask you to verify that you want to proceed. If you do, the system will process the transaction, and will send an automatic email message to the appropriate group that tracks events overriding limits in VPFS. The system will also log it into the Patient Event Log, where you can view the entry by selecting the Log Tab.

> The generated email message includes the transaction ID and station number for the transaction that caused the override. It also contains a link that will display a report with detailed information about the specified transaction in your browser window. If you are not currently logged into VPFS, you will be prompted to log in before the system will display the report. Be sure to log in using the station specified in the email message.

> Note: The following are not menu items or options to be selected; rather, they are conditions that may be automatically generated during the course of a transaction and require an action from the user, such as a validation or a confirmation, to continue. You must be explicitly authorized to override these limits by holding the appropriate security keys.

> ![](vpfs-version-1-2-user-guide/113.png)Overdraw Account: If you attempt to withdraw an amount that exceeds the total balance in the patient account, the system will display a warning message and you will be required to take personal responsibility for the transaction.

> ![](vpfs-version-1-2-user-guide/114.png)Override Deferral: If you attempt to withdraw an amount that exceeds the balance available for withdrawal (i.e., the total balance minus the amount in deferred items), the system will display a warning message and you will be required to take personal responsibility for the transaction.

> ![](vpfs-version-1-2-user-guide/115.png)Override Weekly/Monthly Restriction: If you attempt to override a weekly or monthly restriction placed on an account, the system will display a warning message.

## Patient Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click the Patient tab, patient information for the current patient is displayed on the Patient page.

![](vpfs-version-1-2-user-guide/116.png)

> Figure 7-6. Patient Page From

> the Patient page you can:

![](vpfs-version-1-2-user-guide/117.png)

> View / edit patient information.

> ![](vpfs-version-1-2-user-guide/118.png)![](vpfs-version-1-2-user-guide/119.png)Note: Information that is shown in gray text comes from Patient Services Demographics and cannot be edited via VPFS.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Show Patient Detail.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Show Information Display.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Show Patient Card.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## ![](vpfs-version-1-2-user-guide/120.png)View / Edit Patient Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For certain fields, such as currency amounts, the system checks the validity of your entry. You will be required to correct any errors before saving the data or proceeding onto the next transaction.

> Note: Your user role determines whether you can view and edit General and Special Remarks.

1.  Patient Status: Select the patient status.
2.  Patient Type: Select the patient type.
3.  Special Remarks: Enter special remarks, if applicable. Maximum of 2000 characters. These remarks can be viewed only by individuals with user roles Basic PFC, Lead PFC, and PFC supervisor.
4.  General Remarks: Enter general remarks, if applicable. Maximum of 2000 characters. These remarks can be viewed by individuals with any user role.
5.  Indigent: Select the checkbox if the patient is indigent.
6.  Minimum Balance: Enter the minimum balance.
7.  Maximum Balance: Enter the maximum balance.
8.  Outpatient / In patient: Select the appropriate radio button.
9.  Weekly Amount: Enter the weekly amount (Sunday to Saturday) that can be withdrawn.
10. Monthly Amount: Enter the monthly amount that can be withdrawn.
11. Date Restricted: If you selected Patient Type R – Restricted or L – Limited Restricted, you must enter the date when the account was restricted. Otherwise, leave this field blank.
12. Physician: If you selected Patient Type R – Restricted, or L – Limited Restricted, you must select the physician, or other healthcare provider, who placed the restriction on the account. To search for the provider, click Select Provider. The Select Provider page opens.

> Note: When you select a provider, your changes to the patient are saved.

> The following four fields work together. The information that you enter will be concatenated and inserted in the unlabeled text box when you click Add. This set of fields is optional; however, the Income Source, Payee, and Amount fields are required before you can click Add.

13. Income Source: Click the arrow to select the income source from the list or type the income source.
14. Payee: Click the arrow to select the payee from the list or type the payee.
15. Amount: Enter the amount.
16. Frequency: Select the frequency. Optional.
17. Station: Both Lead PFCs and PFC Supervisors can transfer a patient to another station. This list will only show stations that are included in the user’s allowed divisions list (the DIVISION multiple) in VistA. This is to allow PFCs to move patients between stations within their division that they have access to.

> Note: To transfer the patient's account to another station you must first post a withdrawal to zero out the patient's account at the current station, then assign the patient to a different station and deposit the funds at the new station. The station number cannot be changed if the patient has a pending transfer request. Additionally, text will be displayed on the screen that the patient has a transfer request pending.

18. Click Add to concatenate and insert the data in the set of fields into the unlabeled text box. To insert additional sets of data, repeat steps 13-17.
19. Click Save.

> Your entries are saved and the page is refreshed.

> Working with the Patient Account

#### Select Provider

> To search for and select the name of the physician or other healthcare provider who set the restriction on the patient account:

1.  Click the Select Provider button.

> The Select Provider lookup window opens.

![](vpfs-version-1-2-user-guide/121.png)

> Figure 7-7. Select Provider Page

2.  Search for the provider by entering complete or partial information in the Last Name and / or First Name fields.
3.  Click Search.

> The list of provider names that match the search criteria you entered is displayed.

> ![](vpfs-version-1-2-user-guide/122.png)

> Figure 7-8. Select Provider Page with Providers

4.  Select the provider from the list.

> The Patient tab for the current patient reopens. The provider's name appears in the Physician field.

## Show Patient Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To view detail for the current patient, click Show Patient Detail on the top menu bar. Patient detail information is stored in the VistA system and is refreshed each time you select the patient in VPFS.

> ![](vpfs-version-1-2-user-guide/123.png)

> Figure 7-9. Patient Detail Window

## Show Information Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To view the Patient Funds Information Display for the current patient, click Show Information Display

> on the top menu bar. The Show Information Display window opens.

> ![](vpfs-version-1-2-user-guide/124.png)

> Figure 7-10. Patient Funds Information Display Window

> The Patient Funds Information Display provides patient account and demographic information. You can print this display using your browser's Print function.

## Show Patient Card

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To view the Patient Funds Patient Account Card for the current patient, click Show Patient Card on the top menu bar. The Patient Funds Patient Account Card window opens.

> ![](vpfs-version-1-2-user-guide/125.png)

> Figure 7-11. Patient Funds Patient Account Card

> The Patient Funds Patient Account Card displays account transaction information for the current patient. You can print this card using your browser's Print function.

## Guardians Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click the Guardians tab, guardian information for the current patient is displayed on the Guardians page.

> ![](vpfs-version-1-2-user-guide/126.png)

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Figure 7-12</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>. Guardians Page</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Guardian information comes from Patient Services Demographics (PSD) and cannot be edited through VPFS. View only data is shown in gray text. Following are the only items that you can change in VPFS:

> ![](vpfs-version-1-2-user-guide/127.png)Director Payee: Select the checkbox if the VA guardian is the director payee.

> Title Name: Enter the title and / or name of the VA guardian.

## Transactions Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click the Transactions tab, transaction history for the current patient is displayed on the Transactions page.

> ![](vpfs-version-1-2-user-guide/128.png)

> Figure 7-13. Transactions Page

> Transactions are sorted by date, in descending order by default. If additional information about the transaction is available, click the ![](vpfs-version-1-2-user-guide/129.png) info icon to view the information.

> From the Transactions page you can perform the following tasks:

> ![](vpfs-version-1-2-user-guide/130.png)Edit Deferral Date: Edit the deferral date.

> ![](vpfs-version-1-2-user-guide/131.png)Transaction Display: Display the Transaction Display.

> ![](vpfs-version-1-2-user-guide/132.png)Export Transactions: Export transaction detail to an Excel spreadsheet.

> ![](vpfs-version-1-2-user-guide/133.png)Master Transaction: Display the Master Transaction Display report.

## Editing a Deferral Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Edit the deferral date if the deferral date that was entered originally is incorrect or if management determines that the deferral date is inappropriate. This function is available only to Lead PFCs or PFC Supervisors. The deferral date cannot be more than 30 days past the transaction date.

Working with the Patient Account

## Showing the Transaction Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To view the Patient Funds Transaction Display for the selected transaction, click Transaction Display on the top menu bar. The Patient Funds Transaction Display window opens. To print this display, use the Print function on your browser.

> ![](vpfs-version-1-2-user-guide/134.png)

## Exporting Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To export the list of transactions to an Excel spreadsheet on your computer:

1.  Click Export.

> The list is displayed in a Microsoft Excel file.

2.  Save the Excel file to your computer.

## Showing the Master Transaction Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To view the Patient Funds Master Transaction Display of all transactions for the current patient, click Master Transaction Display on the top menu bar. The Patient Funds Master Transaction Display window opens. To print this display, use the Print function on your browser.

> ![](vpfs-version-1-2-user-guide/135.png)

> Figure 7-14. Patient Funds Master Transaction Display

## Suspense Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click the Suspense tab, information about suspense items for the current patient is displayed on the Suspense page. A suspense item is a reminder of a deferred action, such as to make sure a patient's monthly check has cleared the bank before allowing a withdrawal, a reminder to pay a patient's monthly rent and utilities, or any other patient account issue to be resolved at a future date.

> ![](vpfs-version-1-2-user-guide/136.png)

> Figure 7-15. Suspense Page

> ![](vpfs-version-1-2-user-guide/137.png)![](vpfs-version-1-2-user-guide/138.png)From the Suspense tab you can perform the following tasks: Filter the list of suspense items to a specific range of dates. Edit an existing suspense item.

> ![](vpfs-version-1-2-user-guide/139.png)Add Suspense: Enter a new suspense item.

> ![](vpfs-version-1-2-user-guide/140.png)Cancel This Item: Cancel an existing suspense item.

> ![](vpfs-version-1-2-user-guide/141.png)Cancel Recurring Items: Cancel all occurrences of a recurring suspense item.

> ![](vpfs-version-1-2-user-guide/142.png)Cancel This Date: Cancel all suspense items on the current account for a specified date.

## Filter the List of Suspense Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can filter the list of suspense items by date:

> To filter the list of suspense items:

1.  From: Enter the first date to include in the date range (MM/DD/YYYY).
2.  To: Enter the last date to include in the date range (MM/DD/YYYY).
3.  Click Filter.

> Only the suspense items within the specified date range appear in the list.

## Edit a Suspense Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To edit an existing suspense item:

1.  Select the suspense item from the selection table.

> The Edit Suspense fields open in the bottom section of the page.

2.  Edit information in the Edit Suspense fields, as needed. See sections 7.5.3 and 7.5.4 for field descriptions.
3.  Click Save.

> Your entries are saved.

## Add a Single Suspense Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To add a suspense item to trigger a single reminder:

1.  Click Add Suspense in the top menu bar.

> The Add Suspense fields open in the bottom section of the page.

2.  Enter information in the Add Suspense fields.
    1.  Item ID: Enter a unique name for the suspense item.
    2.  Assigned To: Enter the name of the person responsible for the suspense item.
    3.  Recurring Item: Leave the checkbox empty.
    4.  Suspense Date: Enter the date for the suspense item. This date can be up to one year in the future.
3.  Click Save.

> Your entries are saved.

## Add a Recurring Suspense Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can schedule recurring suspense items for a specified number of weeks or months. For example: You could schedule a recurring reminder to pay for a patient's haircut once every 6 weeks, or a recurring reminder to pay the patient's rent once every month.

> To schedule a recurring suspense item to trigger multiple reminders:

1.  Click Add Suspense in the top menu bar.

> The Add Suspense fields open in the bottom section of the page.

2.  Enter information in the Add Suspense fields.
    1.  Recurring Item: Select the checkbox. The Recurring Item fields open.
    2.  Description: Enter the description for the recurring suspense item.
    3.  Complete the Recurring Item fields.
        1.  Recurring every: Enter the number for the frequency and select either months or weeks.
        2.  Starting on: Enter the date for the first occurrence.
        3.  Number of Occurrences or Ending by: Enter the number of occurrences or the ending date.

> Note: Suspense items will not be created for recurrences beyond one year in the future.

## Cancel a Suspense Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To cancel a suspense item:

1.  Select the suspense item from the list.
2.  Click Cancel This Item.

> A confirmation window opens.

3.  Click OK to confirm that you want to cancel. The item is removed from the list.

## Cancel a Recurring Suspense Item

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To cancel all occurrences of a recurring suspense item:

1.  Select any occurrence of the item.
2.  Click Cancel Recurring Items. A confirmation window opens.
3.  Click OK to confirm that you want to cancel.

> All occurrences of the item are removed from the list.

## Cancel all Transactions on a Specified Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To cancel a suspense item:

1.  Select the suspense item from the list.
2.  Click Cancel This Date.

> A confirmation window opens.

3.  Click OK to confirm that you want to cancel.

> All items occurring on this date are removed from the list.

## Log Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click the Log tab, the Log tab displays descriptions of significant events in the patient's account.

> ![](vpfs-version-1-2-user-guide/143.png)

> ![](vpfs-version-1-2-user-guide/144.png)![](vpfs-version-1-2-user-guide/145.png)![](vpfs-version-1-2-user-guide/146.png)![](vpfs-version-1-2-user-guide/147.png)Register patient Deactivate patient Activate patient Override deferral

> Figure 7-16. Log Page

> Following are all of the possible events that may appear on the Log tab.

> ![](vpfs-version-1-2-user-guide/148.png)![](vpfs-version-1-2-user-guide/149.png)Override weekly / monthly restrictions Override availability / total balance

> ![](vpfs-version-1-2-user-guide/150.png)![](vpfs-version-1-2-user-guide/151.png)Change patient status (competent / incompetent) Change patient type (restricted, etc.)

> Editing Dropdown Lists (Administration)

# Editing Dropdown Lists (Administration)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Many of the fields on VPFS pages provide dropdown lists of valid values for the user to select their entry. Except for the list of Institutions, which cannot be edited through VPFS, system administrators maintain these lists at the national level. Local Patient Funds Clerk Supervisors can make limited changes to the lists that appear at their site, such as changing the order in which items are listed or adding items that are used by their site only.

## Administration Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Administration in the menu in the left panel, the Administration menu opens.

> ![](vpfs-version-1-2-user-guide/152.png)

> Figure 8-1. Administration Menu

> This sample shows all possible Administration Menu items. The items that appear are based on the user roles assigned to the Access / Verify code pair that you used to log in to VPFS.

## Working with Administration Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Maintain Form Types page is typical of the administration pages that you access from the Administration menu.

> ![](vpfs-version-1-2-user-guide/153.png)

> Figure 8-2. Sample Administration Page

> The following components are present on Administration pages:

> ![](vpfs-version-1-2-user-guide/154.png)Selection Table: Use the selection table to select the item to edit.

- If a checkmark appears in the Not Editable column, changes are not allowed for the item.

> ![](vpfs-version-1-2-user-guide/155.png)Edit Area: Use the fields in the edit area to make the change. Any value that appears in gray text, is a value that cannot be changed.

- Order Number: Select the number for the sequence for the item to appear in dropdown lists.

> ![](vpfs-version-1-2-user-guide/156.png)Buttons: Use the buttons at the bottom of the page to complete your change request.

- Add: Click to open the edit fields to enter values for a new item that you want added to a dropdown list.
- Remove: Click to remove the selected item from a dropdown list.
- Return to Administration Menu: Click to exit the page and return to the Administration menu.
- Save: Click to save your changes. o Cancel: Click to cancel your changes.

> Editing Dropdown Lists (Administration)

## Editing the List of Form Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Maintain Form Types on the Administration menu, the Maintain Form Types page displays the list of values for the dropdown list of forms.

> Roles with access to this function are:

> ![](vpfs-version-1-2-user-guide/157.png)Patient Funds Clerk Supervisors: Make local changes that apply to their own sites only.

> ![](vpfs-version-1-2-user-guide/158.png)System Administrators: Make national changes that apply to all sites.

![](vpfs-version-1-2-user-guide/159.png)

> Figure 8-3. Maintain Form Types page

> These fields are not editable. You can, however, change the sequence in which the item will appear in dropdown lists by changing the Order Number.

## Editing the List of Payee Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Maintain Payee Types on the Administration menu, the Maintain Payee Types page displays the list of values for the dropdown list of payee types.

> Roles with access to this function are:

> ![](vpfs-version-1-2-user-guide/160.png)Patient Funds Clerk Supervisors: Add local forms to the list. Edit or remove any forms that you add. Set the order in which forms appear in lists at your site.

> ![](vpfs-version-1-2-user-guide/161.png)System Administrators: Add, edit, and remove forms at the national level.

![](vpfs-version-1-2-user-guide/162.png)

> Figure 8-4. Maintain Payee Types Page

> Editing Dropdown Lists (Administration)

## Editing the List of Remarks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Maintain Remarks on the Administration menu, the Maintain Remarks page displays the list of values for the dropdown list of remarks.

> Roles with access to this function are:

- Patient Funds Clerk Supervisors: Add local remarks to the list. Edit or remove any remarks that you add. Set the order in which remarks appear in lists at your site.
- System Administrators: Add, edit, and remove remarks at the national level.

![](vpfs-version-1-2-user-guide/163.png)

> Figure 8-5. Maintain Remarks Page

> These fields are not editable. You can, however, change the sequence in which the item will appear in dropdown lists by changing the Order Number.

## Editing the List of Income Source Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Maintain Income Source Types on the Administration menu, the Maintain Income Source Types page displays the list of values for the dropdown list of income source types.

> Role with access to this function:

> ![](vpfs-version-1-2-user-guide/164.png)Patient Funds Clerk Supervisors: Add local income source types to the list. Edit or remove any income source types that you add. Set the order in which income source types appear in lists at your site.

> ![](vpfs-version-1-2-user-guide/165.png)System Administrators: Add, edit, and remove income source types at the national level.

![](vpfs-version-1-2-user-guide/166.png)

> Figure 8-6. Maintain Income Source Types Page

> Editing Dropdown Lists (Administration)

## Editing the List of Reference Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Maintain Reference Types on the Administration menu, the Maintain Reference Types page displays the list of values for the dropdown list of references used for posting transactions.

> Roles with access to this function are:

> ![](vpfs-version-1-2-user-guide/167.png)![](vpfs-version-1-2-user-guide/168.png)![](vpfs-version-1-2-user-guide/169.png)Patient Funds Clerk Supervisors: Add local reference types to the list. Edit or remove any reference types that you add. Set the order in which reference types appear in lists at your site.

> Figure 8-7. Maintain Reference Types Page

> These fields are not editable. You can, however, change the sequence in which the item will appear in dropdown lists by changing the Order Number.

## Editing the List of Institutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Maintain Institutions on the Administration menu, the Maintain Institutions page displays the list of values for the dropdown list of institutions. The list of institutions is supplied by the Department of Veteran Affairs (VA) and cannot be changed through VPFS. The only fields on this page that can be changed are e-mail fields.

> Roles with access to this function are:

> ![](vpfs-version-1-2-user-guide/170.png)Patient Funds Clerk Supervisors: Select your institution and edit the list of recipients and the text for email notifications of overrides, deferral date changes, and overdraws at your site. Use SMTP format for email addresses.

> Note: Multiple email addresses can be entered in the Email Lists fields by separating each address with a comma (“,”). Be sure to validate each address as VPFS cannot notify you in the case where a message is undeliverable.

![](vpfs-version-1-2-user-guide/171.png)

> Figure 8-8. Maintain Institutions Page

## Editing the List of Patient Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Maintain Patient Types on the Administration menu, the Maintain Patient Types page displays the list of values for the dropdown list of patient types.

> Role with access to this function:

> ![](vpfs-version-1-2-user-guide/172.png)System Administrators: Add, edit, and remove patient types.

![](vpfs-version-1-2-user-guide/173.png)

> Figure 8-9. Maintain Patient Types Page

## Editing the List of Award Frequencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Maintain Award Frequencies on the Administration menu, the Maintain Award Frequencies page displays the list of values for the dropdown list of award frequency.

> Role with access to this function:

> ![](vpfs-version-1-2-user-guide/174.png)System Administrators: Add, edit, and remove award frequencies at the national level.

> ![](vpfs-version-1-2-user-guide/175.png)

> Figure 8-10. Maintain Award Frequencies Page

## Editing the List of Patient Statuses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Maintain Patient Statuses on the Administration menu, the Maintain Patient Statuses page displays the list of values for the dropdown list of patient status types.

> Role with access to this function:

> ![](vpfs-version-1-2-user-guide/176.png)System Administrators: Make national changes that apply to all sites.

![](vpfs-version-1-2-user-guide/177.png)

> Figure 8-11. Maintain Patient Statuses

## Editing the List of Help Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Maintain Help Text on the Administration menu, the Maintain Help Text page displays the help text that appears in the left panel of each page.

> Role with access to this function:

> ![](vpfs-version-1-2-user-guide/178.png)System Administrators: Add, edit, and remove the page level and field level help text that is displayed in the left margin. Click the arrow to the left of a page name to open the list of fields on the page and edit field level help text.

> The blue editing area is approximately the same size as the area where the help text will be displayed in the left panel. The help text areas are not scrollable, so be aware how much text you

> enter or some of it may not be visible. The help text for each page or field can be a maximum of 500 characters.

> Tip: To open the list of fields on a page and edit field level help text, click the arrow to the left of the page name.

![](vpfs-version-1-2-user-guide/179.png)

> Figure 8-12. Maintain Help Text Page

## Editing the List of Payment Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Maintain Payment Types on the Administration menu, the Maintain Payment Types page displays the list of values for the dropdown list of payment types.

> Role with access to this function:

> ![](vpfs-version-1-2-user-guide/180.png)System Administrators: Add, edit, and remove payment types at the national level.

![](vpfs-version-1-2-user-guide/181.png)

> Figure 8-13. Maintain Payment Types Page

## Editing System Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click Maintain System Parameters on the Administration menu, the Maintain System Parameters page displays the list of system parameters.

> Important: Changing system parameter values could have a negative impact on VPFS functionality. Make sure that you understand the potential results before you make any changes.

> Role with access to this function:

> ![](vpfs-version-1-2-user-guide/182.png)System Administrators: Add, edit, and remove system parameters at the national level.

![](vpfs-version-1-2-user-guide/183.png)

> Figure 8-14. Maintain System Parameters Page

## Editing User Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Roles with access to this function:

> ![](vpfs-version-1-2-user-guide/184.png)All PFC users (Basic, Lead, Super): Change their personal e-signature code.

> To access the Maintain User Account page to edit your user account:

> ![](vpfs-version-1-2-user-guide/185.png)If you are a Basic or Lead PFC, click Administration in the left panel.

> If you are a PFC Super, click Administration in the left panel, then click Maintain User Account from the Administration menu.

![](vpfs-version-1-2-user-guide/186.png)

> Figure 8-15. Maintain User Account Page

> 9 Viewing / Printing Reports

# Viewing / Printing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To access VPFS reports, click Reports in the left panel. The Run Reports page opens. For samples of the reports available from this page, see <u>Appendix F</u>.

![](vpfs-version-1-2-user-guide/187.png)

> Figure 9-1. Run Reports Page

> ![](vpfs-version-1-2-user-guide/188.png)From this page, you can perform the following tasks:

> Run a report. Print a report.

> Export a report to an Excel spreadsheet.

## Run a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To run a report:

1.  Select the report type from the Select Report dropdown list.

> Filter fields that are available for the report you selected appear. A notation appears indicating the orientation to set in your browser, portrait or landscape, if you decide to print the report.

2.  ![](vpfs-version-1-2-user-guide/189.png)Use the filter fields to customize the report. Following are descriptions of all possible filter fields. Only certain filter fields appear for each report type.

> Select Institutions(s): Select the institution to include in the report or leave All.

> Exclude zero balance accounts: Select the checkbox to exclude accounts with a balance of zero.

> ![](vpfs-version-1-2-user-guide/190.png)Begin Date / End Date: Enter the start and end dates for the data range of the data to include in the report.

> Days Inactive: Enter the maximum number of days that accounts can be inactive and be included in the report or leave the default of 180 days.

9\. Viewing / Printing Reports

3.  Click OK.

> The requested report appears in a separate window. If no data is available, the statement No Data Available appears.

> Note: If popup windows are blocked on your computer, press and hold Ctrl while you click OK.

## Print a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To print the displayed report:

1.  Use your browser's Print function to set the orientation to portrait or landscape, based on the notation on the Run Reports page for the report you are printing.
2.  Once you have set the appropriate orientation for the report, use your browser's print function to print it. The example below lists the procedure you would use with Internet Explorer and most HP printers.

> Your procedure may differ depending on the browser and printer you are using.

> Example:

## Export a Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To export the selected report to an Excel spreadsheet on your computer:

1.  Click Export.

> The File download window opens

> Note: If popup windows are blocked on your computer, press and hold Ctrl while you click

#### Export.

> ![](vpfs-version-1-2-user-guide/191.png)

> Figure 9-2. File Download Window

2.  Save the report as an Excel file to your computer.

> 9 Viewing / Printing Reports

10\. Selecting Suspense Items

# Selecting Suspense Items

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Suspense menu option in the left panel allows you to select suspense items for all patient accounts at your site (or at multiple sites for multi-site institutions. A suspense item is a reminder of a deferred action, such as to make sure a patient's monthly check has cleared the bank before allowing a withdrawal, a reminder to pay a patient's monthly rent and utilities, or any other patient account issue to be resolved at in the future.

> For more information about working with suspense items, see section 7.5.

> To select suspense items for patients at the site or sites to which you have access:

1.  Click Suspense in the left panel.

> The Select Suspense page displays the list of suspense items on patient records at your site(s).

![](vpfs-version-1-2-user-guide/192.png)

> Figure 10-1. Select Suspense Page

> From the Select Suspense page you can perform the following tasks:

> ![](vpfs-version-1-2-user-guide/193.png)

## Appendix A. 508 Standards

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This appendix describes the approach used by the VPFS team to ensure that the VPFS application complies with 508 requirements to provide individuals with visual impairment equivalent access to the application web pages. The paragraphs that are quoted in this appendix come from *Electronic and Information Technology Accessibility Standards Final Rule (Federal Register 21* December 2000, 36 CFR Part 1194).

## Standards

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Paragraph (a)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>“<em>A text equivalent for every non-text</em></p>
<p><em>element shall be provided (e.g., via “alt” “longdesc” or in element content).</em>”</p>
</blockquote></th>
<th><blockquote>
<p>This requirement is met in VPFS mostly through the design of the framework used by individual pages. Alternate text was added to all graphical buttons, identifying the object, its state (e.g., whether disabled or not), and what it does, in a clear and concise manner.</p>
<p>Images that serve as graphic elements or placeholders that do not convey any meaning, do not need to be given alternate text. However, testing programs (such as Bobby) that look for section 508 compliance may flag such images as problems when they are not problems. To avoid this, we</p>
<p>added blank alternate tags to these images.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Paragraph (b)</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>“<em>Equivalent alternative for any multimedia presentation shall be synchronized with the presentation.</em>”</p>
</blockquote></td>
<td><blockquote>
<p>No multimedia presentations will be used.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Paragraph (c)</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> “*Web pages shall be designed so that all information conveyed with color is also available without color, for example form context or markup.*”

> The tabs at the top of each page and the buttons on each page convey information by their color. For instance, the current tab may be highlighted in blue and a button that is disabled may appear gray.

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Paragraph (e)</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>“<em>Redundant text links shall be provided for each active region of a server side image map.</em>”</p>
</blockquote></td>
<td><blockquote>
<p>Server side image maps will not be used.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Paragraph (f)</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>“<em>Client-side image maps shall be provided instead of server-side image maps except where the regions cannot be defined with an available geometric shap</em>e.”</p>
</blockquote></td>
<td><blockquote>
<p>Client side image maps will not be used.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Paragraph (g)</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>“<em>Row and column headers shall be identified for data tables.</em>”</p>
</blockquote></td>
<td><blockquote>
<p>The application uses tables for both page formatting and data presentation. For the tables that present data, row and column headers are clearly identified for screen reader accessibility.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Paragraph (h)</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>“<em>Markup shall be used to associate data cells and header cells for data tables that have two or more logical levels of row or column headers.</em>”</p>
</blockquote></td>
<td><blockquote>
<p>Text is provided to distinguish between data and header cell contents, and to associate content with the appropriate headers.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Paragraph (i)</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>“<em>Frames shall be titled with text that facilitates frame identification and navigation.</em>”</p>
</blockquote></th>
<th><blockquote>
<p>Frames technology will not be used.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> In order to be compliant with this paragraph, text was added to explain the state of a button. In the case of a tab, the alternate text for the tab would say, “Currently in the X section” or alternate text for a button might identify its state.

### Paragraph (d)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> “Documents shall be organized so they are readable without requiring an associated style sheet.” Style sheets are used to display the text in a particular style, color and font size. This can present a problem if the style sheet does not allow the user to increase or decrease the font size. A separate style sheet is provided for the text only version of the application, which specifies the font sizes in relative

> measurements. Using relative measurements allows the fonts to change based on the user’s preferences.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>“<em>Pages shall be designed to avoid causing the screen to flicker with frequency greater than 2 Hz and lower than 55 Hz.</em>”</p>
</blockquote></th>
<th><blockquote>
<p>Screen flicker is kept to a minimum and falls within the accepted range.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Paragraph (k)</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> “*A text-only page, with equivalent information or functionality, shall be provided to make a Web site comply with the provisions of this part, when compliance cannot be accomplished in any other way. The content of the textonly page shall be updated whenever the primary page changes.*”

> After exploring the options to ensure that VPFS is in compliance with 508 the emerging consensus was to create an alternative text only view of the site, as part of the same application. The rationale for this step is as follows:

> ![](vpfs-version-1-2-user-guide/194.png)A text only view allows us to change the order in which information is displayed. For users using assistive technologies this would make the content and navigation much clearer and easier

> ![](vpfs-version-1-2-user-guide/195.png)to understand. Many critical elements of the site may not be

> easily modified to create a “one site fits all” solution. The help text and index most notably are significant barriers to assistive technology.

> ![](vpfs-version-1-2-user-guide/196.png)Creating a text only view gives all visitors the option of using a simplified version of the site. This is advantageous for users who have a slow Internet connection or are using other devices to access the Web, such as palmtop computers.

> ![](vpfs-version-1-2-user-guide/197.png)The implementation of this text only view can be added to the existing application without resorting to creating a completely separate independent application.

> Designing key framework elements appropriately can result in the complete conversion of the output as it is rendered. This method has many advantages.

- The maintenance of two different sites is not necessary. Most site elements can be reused.
- Users of the text only and graphical views of the application will always have the same content. This eliminates the chance that the text only view would not be updated as frequently as the graphical site. Changes to one also take place in the other.

> Appendix A. 508 Standards

### Paragraph (l)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> “*When pages utilize scripting languages to display content, or to create interface elements the information provided by the script shall be identified with functional text that can be read by assistive technology.*”

> The site uses scripting extensively for form validation and navigation. Most of

> this scripting does not write content to the browser and does not affect content. However, several issues remain:

> ![](vpfs-version-1-2-user-guide/198.png)The margin text that runs in the left panel of the page uses a script to update the content of that area

> “*When electronic forms are designed to be completed on-line, the form shall allow people using assistive technology to access the information, field elements, and functionality required for completion and submission of the form, including all direction and cues.*”

### Paragraph (o)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> depending on what field the user’s cursor is currently in. This updated information is not available to a user of an assistive technology. To address this problem, VPFS displays the margin text for the user in a dialog box if the user presses a keyboard shortcut.

> ![](vpfs-version-1-2-user-guide/199.png)Another issue associated with scripting and accessibility concerns the way buttons work. The user

> takes an action by clicking on a button, which in turn triggers a script to run and execute a particular action. If the user cannot use the mouse to click on the button, the action cannot take place. To address this problem, buttons are programmed to trigger actions if the user hits a key on the keyboard while focus is on a button.

> All form fields identify their content to the screen reader. In addition, the forms are designed in such a way as to maximize usability in terms of direct access to information, field elements, and functionality (equivalent to that of the graphical view), including directions, context-sensitive help, etc.

> “*A method shall be provided that permits* VPFS navigational links may appear in the left margin as *users to skip repetitive navigation links*.” well as across the page top and bottom.

> To address this issue, links were added to the top of the page taking the user to the main areas within the page. One link goes to the main content. Another links to the navigational elements.

> In addition to the accessibility links, the text only view of the site reorganizes the content of the page. Repetitive links and content fall to the bottom of the screen, while the main content of the page remains near the top. Also, keyboard shortcuts were added to make jumping between sections of the page easier.

### Paragraph (p)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>“<em>When a timed response is required, the user shall be alerted and given sufficient time to indicate more time is required</em>.”</p>
</blockquote></th>
<th><blockquote>
<p>The site does not have a timed response per prompt. However, in compliance with security requirements, the site has a timeout so that if the user does not take an appropriate action in the form within a given amount of time the session is terminated. The site gives warnings that this is going to take place, which gives a user ample opportunity to take the appropriate action to keep the session from timing out. The users cannot change the time set for the timeout, as this is determined by VHA security policy. However, by acting on the timeout warnings, the user can extend/reset the 20minute timeout period.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Assistive Technology

> There are many products available to assist persons with disabilities, such as speech or refreshable Braille screen readers, programs that can enlarge portions of the screen, or hardware alternatives to keyboards and mice. It is beyond the scope of this document to reference all the different assistive technologies that are available and how VPFS would work with each. Below are the major categories of assistive devices and what will be done in VPFS to support each.

> ![](vpfs-version-1-2-user-guide/200.png)Screen readers: Alternate text will be given to all visual information, including graphical buttons and form controls. A text only view of VPFS that is optimized for use with a screen reader will be available for anyone to use.

> ![](vpfs-version-1-2-user-guide/201.png)Screen magnification and text enlargement: The text only view will allow the text to be increased to any size that is comfortable to the user. The graphical view will also be resizable to accommodate different screen sizes and resolutions.

> ![](vpfs-version-1-2-user-guide/202.png)Alternative input devices: All elements will be designed to allow manipulation without the need for a pointing device. In addition, keyboard shortcuts will be provided to make navigation inside a page easier.

> Assuming the assistive technologies are following industry standards, VPFS will work with assistive technologies.

Appendix B. Glossary

## Appendix B. Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The terms and definitions in this glossary are taken from the *Patient Funds (Integrated System) Technical Manual for Site Manager*, Version 3.0, February 1989, with some additions.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Fiduciary</strong></th>
<th><blockquote>
<p>A legal entity or individual who is appointed by a court of competent jurisdiction or by the administrator and who receives VA benefits reserved for the eligible person’s use and advantage.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Gratuitous Funds</strong></td>
<td><blockquote>
<p>With the exception of insurance, all funds that are derived from VA benefits and that are deposited in the account of a VA patient rated as Incompetent. Although the VA cannot purchase U.S. savings bonds with gratuitous funds, the patient or the patient’s representative can. When these bonds are redeemed, the proceeds (principal) are considered gratuitous funds</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Guardian</strong></td>
<td><blockquote>
<p>A person or corporation who, following the decree of a court of competent jurisdiction, protects the person or property, or both, of a minor or mentally incompetent VA beneficiary.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Incompetent</strong></td>
<td><blockquote>
<p>VA or court decreed classification assigned to patients who, because of mental or physical incapacity, are unable to manage their own affairs.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Institutional Award</strong></td>
<td><blockquote>
<p>An award of disability compensation, pension, or emergency officers‟ retirement pay to the Director of a VA healthcare facility, or to another Federal, State, or private contract facility, on behalf of a veteran rated incompetent by the VA, or adjudged incompetent by court decree, or rated incompetent by both.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Nongratuitous Funds</strong></td>
<td><blockquote>
<p>All funds in patients‟ accounts except those described as gratuitous. Interest on U.S. savings bonds purchased from gratuitous funds is also considered nongratutious.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Patients</strong></td>
<td><blockquote>
<p>Individuals receiving hospitalization, nursing home care, and domiciliary care under VA auspices. Also, individuals whose funds are managed by the VA following their release from authorized medical care.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>PFOP</strong></td>
<td><blockquote>
<p>Personal Funds of Patients: The integrated computer system used by Veterans Health Administration to manage the patient funds at VA healthcare facilities. This integrated system is being</p>
<p>reengineered to the centralized system VPFS.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Appendix B Glossary

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Restricted Accounts</strong></p>
</blockquote></th>
<th><blockquote>
<p>Patient accounts managed by the facility Director, who serves as trustee. Deposited in this type of account are personal funds that</p>
<p>belong to the following types of patients:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- All patients adjudged incompetent by a court.
- All patients whom the VA rates as Incompetent or whom the Director considers incapable of administering their funds.
- For purposes of administration, psychiatric patients whose funds should be controlled because of their ward assignment or because an in-competency rating is pending. For temporary periods, Directors may designate certain “restricted” accounts as “unrestricted” and may authorize the patient concerned to use the account, within prudent limits, as an unrestricted account if such use will aid the patient’s therapeutic progress or will help to determine whether the patient has the ability to handle the funds.

> Review Panel Three-member board that determines patient’s competency and reviews appeals about patient competency. Panel includes:

- The Director (except where the Director appoints a team to determine the patient’s competency) or Assistant Director
- The Chief of Staff

> A mental health professional

- Members of the treatment team for the patient being evaluated are prohibited from serving on the review panel.

> Status Account Status: active, inactive

> Patient Status: incompetent, indigent, deceased

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Unrestricted Accounts</strong></th>
<th><blockquote>
<p>Accounts of patients capable of handling personal funds that are deposited for safekeeping: such accounts are not subject to the trusteeship of the Director; the funds in such accounts are</p>
<p>available for return to the patients on demand.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>VPFS</strong></td>
<td><blockquote>
<p>Veterans Personal Finance System: The Health<em><u>e</u></em>Vet Vista centralized version of the mini-banking system used by the Veterans Health Administration (VHA) to manage the accounts</p>
<p>of patients in the VHA hospital system. Replace PFOP.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Appendix C. Acronyms and Abbreviations

## Appendix C. Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>TERM</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DEFINITION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CFR</p>
</blockquote></td>
<td><blockquote>
<p>Code of Federal Regulations</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 79%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CI</p>
</blockquote></th>
<th><blockquote>
<p>Configuration Item</p>
</blockquote></th>
<th rowspan="27"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>E-signature</p>
</blockquote></th>
<th><blockquote>
<p>Electronic Signature</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>IE</p>
</blockquote></th>
<th><blockquote>
<p>Internet Explorer</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>IIG</p>
</blockquote></th>
<th><blockquote>
<p>Impact Innovations Group</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>IPF</p>
</blockquote></th>
<th><blockquote>
<p>Integrated Patient Funds</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>LLC</p>
</blockquote></th>
<th><blockquote>
<p>Limited Liability Corporation</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>KAAJEE</p>
</blockquote></th>
<th><blockquote>
<p>Kernel Authentication and Authorization for J2EE</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>M, MUMPS</p>
</blockquote></th>
<th><blockquote>
<p>Massachusetts Universal Multi Programming System</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>OI</p>
</blockquote></th>
<th><blockquote>
<p>Office of Information</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>OID</p>
</blockquote></th>
<th><blockquote>
<p>Oracle Internet Directory</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>PDF</p>
</blockquote></th>
<th><blockquote>
<p>Adobe file (*.pdf format)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>PFC</p>
</blockquote></th>
<th><blockquote>
<p>Patient Funds Clerk</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>PFOP</p>
</blockquote></th>
<th><blockquote>
<p>Personal Funds of Patients</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>PSD</p>
</blockquote></th>
<th><blockquote>
<p>Patient Service Demographics</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>PSL</p>
</blockquote></th>
<th><blockquote>
<p>Patient Service Lookup</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>QA</p>
</blockquote></th>
<th><blockquote>
<p>Quality Assurance</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>QCI</p>
</blockquote></th>
<th><blockquote>
<p>Quality Control Inspector</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>SD&amp;D</p>
</blockquote></th>
<th><blockquote>
<p>System Design &amp; Development</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>SDD</p>
</blockquote></th>
<th><blockquote>
<p>System Design Document</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>SSL</p>
</blockquote></th>
<th><blockquote>
<p>Secure Socket Layer</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>SOW</p>
</blockquote></th>
<th><blockquote>
<p>Statement of Work</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>SQA</p>
</blockquote></th>
<th><blockquote>
<p>Software Quality Assurance</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>SSN</p>
</blockquote></th>
<th><blockquote>
<p>Social Security Number</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>TBD</p>
</blockquote></th>
<th><blockquote>
<p>To Be Determined</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>VA</p>
</blockquote></th>
<th><blockquote>
<p>Department of Veterans Affairs</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>VHA</p>
</blockquote></th>
<th><blockquote>
<p>Veterans Health Administration</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>VistA</p>
</blockquote></th>
<th><blockquote>
<p>Veterans Information Systems Technology Architecture</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VPFS</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Personal Finance System</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Appendix D Frequently Asked Questions

## Appendix D. Frequently Asked Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>QUESTION</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ANSWER</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>What is the purpose of VPFS?</p>
</blockquote></td>
<td><blockquote>
<p>VPFS is the current mini-banking system used by the VHA to manage the accounts of VHA patients in the VHA hospital system.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>What is the history of VPFS?</p>
</blockquote></td>
<td><blockquote>
<p>VPFS is the reengineered version of PFOP. VPFS looks different from PFOP because it is a web-based Windows application; however, its design and functionality are modeled after PFOP.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Who will be using VPFS?</p>
</blockquote></td>
<td><blockquote>
<p>Official users, patient funds clerks, systems and security administrators, and Fiscal management.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>How does VPFS work?</p>
</blockquote></td>
<td><blockquote>
<p>You will be able to perform all of the functions in VPFS that you are used to in PFOP, with the exception of a few functions that are no longer needed due to new built-in security controls.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>How can I access VPFS</p>
</blockquote></td>
<td><blockquote>
<p>In order to use the VFPS application, you will need access to the VHA Intranet via Internet Explorer (IE) versions 6 SP1, 6, or</p>
<p>5.5 SP2; or via Netscape version 7.1, 7.02 or 7.01.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>How is information kept secure?</p>
</blockquote></td>
<td><blockquote>
<p>In addition to the standard 128-bit encrypted security (SSL) available through IE and Netscape, all authorized users are required to maintain a password and e-signature code. Without the proper authorization, password, and e-signature, no one can access VPFS.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Will my e-signature be the same as the password?</p>
</blockquote></td>
<td><blockquote>
<p>No. Because the e-signature is a secondary level of security, it is important that it be different than your password.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>What if I don’t know how to use Windows?</p>
</blockquote></th>
<th><blockquote>
<p>There are many Windows tutorials available, commercially and free on the Internet, to introduce you to the operating system.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Appendix D. Frequently Asked Questions

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>QUESTION</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ANSWER</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>What if I’m disabled and can’t read the screen?</p>
</blockquote></td>
<td><blockquote>
<p>You can use the “text-only” option (on the Intro page), which will display all of the page contents in text form, and you can use an assistive screen reader with this version.</p>
<p>In general, the requirement of 508 compliance is that the disabled user (visually disabled or otherwise) should have an experience with the application that is functionally equivalent to that of the non-disabled user. This means that, for each element of the graphics-based presentation, there is a textbased equivalent that can be read by the user or by an assistive device. Further, it is important to make the text-based pages as usable as those of the graphics-based pages, e.g., by providing ways for the user to navigate directly to desired locations. The VPFS approach to 508 compliance is based on a design whereby the user specifies a preference for the text or the graphics version; for each page, the application then determines which version is to be rendered to the browser. This way there is only one Website, and an equivalent experience is</p>
<p>ensured.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Can I bookmark the system pages?</p>
</blockquote></td>
<td><blockquote>
<p>You can bookmark the introduction page, but you must go through the logon process each time you access the system.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix E. VPFS User Roles and Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following breakout itemizes all the functions in the VPFS System.

> o Forms (site-specific list) o

#### Select Patient

> ![](vpfs-version-1-2-user-guide/203.png)Search and Filter

> ![](vpfs-version-1-2-user-guide/204.png)View All Patients (per Institution) Select Patient, go to Account page for patient record

> Register Patient Verify Balances

> Post Multiple Transactions

#### Account

> ![](vpfs-version-1-2-user-guide/205.png)![](vpfs-version-1-2-user-guide/206.png)View Account Balance Post Transaction o Override Restriction o Override Deferral Date Verify Balance Transfer Patient

#### Patient

> ![](vpfs-version-1-2-user-guide/207.png)![](vpfs-version-1-2-user-guide/208.png)Edit Patient Information o Edit Special Remarks View Patient Information

> o View Special Remarks

#### Guardian

> ![](vpfs-version-1-2-user-guide/209.png)Add/Edit Guardian Information View Guardian Information

#### Transactions

> ![](vpfs-version-1-2-user-guide/210.png)Search and Filter

> View Transaction History Edit Deferral Date

#### Suspense

> ![](vpfs-version-1-2-user-guide/211.png)Add Item Cancel Item

> Cancel Items for Date

> Review Suspense Items per Patient (Select Suspense)

#### Log

> ![](vpfs-version-1-2-user-guide/212.png)View Patient Log

#### Administration

> ![](vpfs-version-1-2-user-guide/213.png)Perform Maintenance o Award Frequency o Forms (national list)

> Patient Status o Patient Type o

> Payment Type

- Payee Type (national list) o Payee Type (site-specific list) o Income Source Type (national list)
- Income Source Type (site- specific list)
- Remarks (national list)
- Remarks (site-specific list) o Margin/Page Help o Reference Type (national list) o Reference Type (site-specific list) o Institution (Note: PFC Super can only view/edit their own institutions)
- Maintain System Parameters o

> Maintain User Account

#### Reports

> ![](vpfs-version-1-2-user-guide/214.png)Patient Card Output Options o Print Selected Cards o Print All Cards o Transaction Display o Information Display o Master Transaction Review

> ![](vpfs-version-1-2-user-guide/215.png)Standard Reports o Activity Audit Listing o Dormant Account Listing

- Deceased Patient with a Balance
- Discharged Patient with a Balance
- Inactive Withdrawal Listing o Indigent Patient Listing o Overdue Restriction Search o Patient Summary Report o Min and Max Restrictions o Patient Listing o Account Balances o Transaction Listing o Fiscal Audit Report o Fiscal Transaction Summary Report
- Date Variance Report o Negative Balance Report o Productivity Report

VPFS User Roles and Functions

#### Select Suspense

> ![](vpfs-version-1-2-user-guide/216.png)Search and Filter

> View Suspense Records across Patients Select Suspense Item, go to

> ![](vpfs-version-1-2-user-guide/217.png)Suspense page for patient record Cancel Suspense Item

> Logout

## Basic Official User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Basic Official User is a user who requires access to patient records but does not need privileges to post transactions. Most similar to the existing PFOP Ward Clerk, this user only needs to review patient data.

> Basic Official Users have read-only access to the following selected pages of VPFS.

#### Select Patient

> ![](vpfs-version-1-2-user-guide/218.png)Search and Filter

> View All Patients (per Institution)

> Select Patient, go to Account page for patient record

#### Account

> ![](vpfs-version-1-2-user-guide/219.png)View Account Balance

#### Patient

> ![](vpfs-version-1-2-user-guide/220.png)View Patient Information

#### Guardian

> ![](vpfs-version-1-2-user-guide/221.png)View Guardian Information

#### Logout

> VPFS User Roles and Functions

## Basic Patient Funds Clerk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Basic Patient Funds Clerk (PFC) requires access to patient records to post transactions and print reports. Basic PFCs have the ability to view all of the following pages in the Patient Account module, and

> to edit most information (as in PFOP).

#### Select Patient

> ![](vpfs-version-1-2-user-guide/222.png)Search and Filter View All Patients (per Institution)

> ![](vpfs-version-1-2-user-guide/223.png)Select Patient, go to Account page for patient record

> Register Patient

> Post Multiple Transactions

#### Account

> ![](vpfs-version-1-2-user-guide/224.png)View Account Balance Post Transaction

#### Patient

> ![](vpfs-version-1-2-user-guide/225.png)Edit Patient Information

> o Edit Special Remarks

> View Patient Information

> ![](vpfs-version-1-2-user-guide/226.png)o View Special Remarks

#### Guardian

> ![](vpfs-version-1-2-user-guide/227.png)Add/Edit Guardian Information View Guardian Information

#### Transactions

> ![](vpfs-version-1-2-user-guide/228.png)Search and Filter

> View Transaction History

#### Suspense

> ![](vpfs-version-1-2-user-guide/229.png)Add Item Cancel Item

> Cancel Items for Date Review Suspense Items per

> Patient

> (Select Suspense)

#### Log

> ![](vpfs-version-1-2-user-guide/230.png)View Patient Log

#### Administration

> ![](vpfs-version-1-2-user-guide/231.png)Maintain User Account

#### Reports

> ![](vpfs-version-1-2-user-guide/232.png)Patient Card Output Options o Print Selected Cards o Print All Cards o Transaction Display o Information Display o Master Transaction Review

> ![](vpfs-version-1-2-user-guide/233.png)Standard Reports o Activity Audit Listing o Dormant Account Listing o Deceased Patient with a Balance o Discharged Patient with a

> Balance o Inactive Withdrawal Listing o Indigent Patient Listing o Overdue Restriction Search o Patient Summary Report o Min and Max Restrictions o Patient Listing o Account Balances o Transaction Listing o Fiscal Audit Report o Fiscal Transaction Summary Report o Date Variance

> ![](vpfs-version-1-2-user-guide/234.png)Report

> Select Suspense Search and Filter

> View Suspense Records across Patients

> ![](vpfs-version-1-2-user-guide/235.png)![](vpfs-version-1-2-user-guide/236.png)Select Suspense Item, go to Suspense page for patient record

> Cancel Suspense Item Logout

## Lead Patient Funds Clerk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Lead PFCs have the ability to view all pages and perform all functions in the Patient Account Module, as

> follows.

#### Select Patient

> ![](vpfs-version-1-2-user-guide/237.png)Search and Filter View All Patients (per Institution)

> ![](vpfs-version-1-2-user-guide/238.png)Select Patient, go to Account page for patient record

> Register Patient Verify Balances

> Post Multiple Transactions

#### Account

> ![](vpfs-version-1-2-user-guide/239.png)View Account Balance Post Transaction Verify Balance Transfer Patient

#### Patient

> ![](vpfs-version-1-2-user-guide/240.png)Edit Patient Information Edit Special Remarks View Patient Information View Special Remarks

#### Guardian

> ![](vpfs-version-1-2-user-guide/241.png)Add/Edit Guardian Information View Guardian Information

#### Transactions

> ![](vpfs-version-1-2-user-guide/242.png)Search and Filter

> View Transaction History Edit Deferral Date

#### Suspense

> ![](vpfs-version-1-2-user-guide/243.png)Add Item Cancel Item

> Cancel Items for Date Review Suspense Items per

> Patient

> (Select Suspense)

> Log

> ![](vpfs-version-1-2-user-guide/244.png)View Patient Log

#### Administration

> ![](vpfs-version-1-2-user-guide/245.png)Maintain User Account

#### Reports

> ![](vpfs-version-1-2-user-guide/246.png)Patient Card Output Options o Print Selected Cards o Print All Cards o Transaction Display o Information Display o Master Transaction Review

> ![](vpfs-version-1-2-user-guide/247.png)Standard Reports o Activity Audit Listing o Dormant Account Listing

- Deceased Patient with a Balance
- Discharged Patient with a Balance o Inactive

> Withdrawal Listing o Indigent Patient Listing o Overdue Restriction Search o Patient Summary Report o Min and Max Restrictions o Patient Listing o Account Balances o Transaction Listing o Fiscal Audit Report o Fiscal Transaction Summary

> Report o Date Variance Report

#### Select Suspense

> ![](vpfs-version-1-2-user-guide/248.png)Search and Filter

> View Suspense Records across Patients

> ![](vpfs-version-1-2-user-guide/249.png)Select Suspense Item, go to Suspense

> ![](vpfs-version-1-2-user-guide/250.png)page for patient record Cancel Suspense Item

#### Logout

> 96 VPFS User Guide v1.2.0 July 2020

## Patient Funds Clerk Supervisor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PFC Supervisor has the ability to view all pages and perform all functions in the Patient Account

> Module, as follows:

#### Select Patient

> ![](vpfs-version-1-2-user-guide/251.png)Search and Filter

> ![](vpfs-version-1-2-user-guide/252.png)View All Patients (per Institution) Select Patient, go to Account page for patient record

> Register Patient Verify Balances

> Post Multiple Transactions

#### Account

> ![](vpfs-version-1-2-user-guide/253.png)View Account Balance Post Transaction Verify Balance Transfer Patient

#### Patient

> ![](vpfs-version-1-2-user-guide/254.png)Edit Patient Information Edit Special Remarks View Patient Information View Special Remarks

#### Guardian

> ![](vpfs-version-1-2-user-guide/255.png)Add/Edit Guardian Information View Guardian Information

#### Transactions

> ![](vpfs-version-1-2-user-guide/256.png)Search and Filter

> View Transaction History Edit Deferral Date

#### Suspense

> ![](vpfs-version-1-2-user-guide/257.png)Add Item Cancel Item

> Cancel Items for Date

> Review Suspense Items per Patient (Select Suspense)

- Income Source Type (site-specific list)
- Remarks (site-specific list) o

> Reference Type (site-specific list)

> o Institution (Note: PFC Super can only view/edit their own institutions)

- Maintain User Account

#### Reports

> ![](vpfs-version-1-2-user-guide/258.png)Patient Card Output Options o Print Selected Cards o Print All Cards o Transaction Display o Information Display o Master Transaction Review

> ![](vpfs-version-1-2-user-guide/259.png)Standard Reports o Activity Audit Listing o Dormant Account Listing

- Deceased Patient with a Balance
- Discharged Patient with a Balance
- Inactive Withdrawal Listing o Indigent Patient Listing o Overdue Restriction Search o Patient Summary Report o Min and Max Restrictions o Patient Listing o Account Balances o Transaction Listing o Fiscal Audit Report o Fiscal Transaction Summary Report
- Date Variance Report o Negative Balance Report o Productivity Report

#### Select Suspense

> ![](vpfs-version-1-2-user-guide/260.png)Search and Filter

> View Suspense Records across Patients Select Suspense Item, go to

> ![](vpfs-version-1-2-user-guide/261.png)Suspense page for patient record Cancel Suspense Item

#### Log

> ![](vpfs-version-1-2-user-guide/262.png)View Patient Log

#### Administration

> ![](vpfs-version-1-2-user-guide/263.png)Perform Maintenance o

> Forms (site-specific list)

> o Payee Type (site-specific list)

#### Logout

> Appendix E. VPFS User Roles and Functions

> Suspense

## Fiscal Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The function of Fiscal Management is to perform audits to verify that patient accounts are being properly maintained and reconciled. To this end, Fiscal Management users access VPFS on a read-only basis.

> They cannot create, modify, or delete patient or account information.

> ![](vpfs-version-1-2-user-guide/264.png)Review Suspense Items per Patient

#### Select Patient

> ![](vpfs-version-1-2-user-guide/265.png)Search and Filter

#### Reports

> (Select Suspense)

> View All Patients (per Institution)

> Select Patient, go to Account

> ![](vpfs-version-1-2-user-guide/266.png)page for patient record Verify Balances

#### Account

> ![](vpfs-version-1-2-user-guide/267.png)View Account Balance Verify Balance

#### Patient

> ![](vpfs-version-1-2-user-guide/268.png)View Patient Information

#### Guardian

> ![](vpfs-version-1-2-user-guide/269.png)View Guardian Information

#### Transactions

> ![](vpfs-version-1-2-user-guide/270.png)Search and Filter

> View Transaction History

> Standard Reports o Activity Audit Listing o Dormant Account Listing o Indigent Patient Listing o Overdue Restriction Search o Patient Summary Report o Min and Max Restrictions o Patient Listing o Account Balances o Transaction Listing o Fiscal Audit Report o Fiscal Transaction Summary Report o Date Variance Report o Negative Balance Report

#### ![](vpfs-version-1-2-user-guide/271.png)Select Suspense

> ![](vpfs-version-1-2-user-guide/272.png)Search and Filter

> View Suspense Records across

> Patients Select Suspense Item, go to Suspense page for patient record

> Logout

## VPFS System Administrator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VPFS System Administrator implements authorized changes to the common reference data of VPFS, as follows:

#### Administration

> ![](vpfs-version-1-2-user-guide/273.png)Perform Maintenance o Award Frequency o Forms (national list) o Patient Status o Patient Type

- Payment Type
  - Payee Type (national list) o Income Source Type (national list) o Remarks (national list) o

> Margin/Page Help o Reference Type (national list) o Institution

- Maintain System Parameters

> Logout

## VPFS Security Administrator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VPFS Security Administrator is responsible for ensuring that data access is properly enforced in VPFS (i.e., that users see and operate on only the data and functions for which they have security access privileges). The VPFS Security Administrator has read-only privileges to the following areas of VPFS:

#### Select Patient

> ![](vpfs-version-1-2-user-guide/274.png)Search and Filter

> View All Patients (per Institution)

> Select Patient, go to Account page for patient record

#### ![](vpfs-version-1-2-user-guide/275.png)Account

View Account Balance Patient

View Patient Information

#### Guardian

> ![](vpfs-version-1-2-user-guide/276.png)View Guardian Information

#### Transactions

> ![](vpfs-version-1-2-user-guide/277.png)Search and Filter

> View Transaction History

#### Log

> ![](vpfs-version-1-2-user-guide/278.png)View Patient Log

## Appendix F. Report Samples Account Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option provides a report that shows the grand total of the balances in the Patient Funds system. This

> report is used by Fiscal to reconcile the general ledger.

> Portrait: Select portrait page orientation when printing this report.

> ![](vpfs-version-1-2-user-guide/279.png)

## Activity Audit Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report provides a printout of all Patient Funds transactions for a selected date range. The information is sorted in the following order:

> ![](vpfs-version-1-2-user-guide/280.png)Transaction date:

> ![](vpfs-version-1-2-user-guide/281.png)![](vpfs-version-1-2-user-guide/282.png)![](vpfs-version-1-2-user-guide/283.png)Type of transaction (deposit or withdrawal) Type of currency (cash, check, or “other”) Type of VA form

> Subtotals are calculated for each transaction type, type of currency, and VA form.

> Landscape: Select landscape page orientation when printing this report.

> ![](vpfs-version-1-2-user-guide/284.png)

> Figure F-2 Activity Audit Listing Report

## Date Variance Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Portrait: Select portrait page orientation when printing this report.

![](vpfs-version-1-2-user-guide/285.png)

> Figure F-3. Date Variance Report

## Deceased Patient with a Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Portrait: Select portrait page orientation when printing this report.

> ![](vpfs-version-1-2-user-guide/286.png)

> Figure F-4. Deceased Patient with a Balance

## ![](vpfs-version-1-2-user-guide/287.png)Discharged Patient with a Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Portrait: Select portrait page orientation when printing this report.

> Figure F-5. Discharged Patient with a Balance

## Dormant Account Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option searches the accounts and prints a list of all accounts that have had no activity for the period of time you specify at the prompt.

> Portrait: Select portrait page orientation when printing this report.

> ![](vpfs-version-1-2-user-guide/288.png)

## Fiscal Audit Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure F-6. Dormant Account Listing

> This report provides a printout of all Patient Funds transactions for a selected date range. The information is sorted in the following order:

1.  Transaction date
2.  Type of transaction (deposit or withdrawal)
3.  Type of currency (cash, check, or “other”)
4.  Type of VA form

> Subtotals are calculated for each transaction type, type of currency, and VA form.

> Landscape: Select landscape page orientation when printing this report.

> ![](vpfs-version-1-2-user-guide/289.png)

> Figure F-7. Fiscal Audit Report

## Fiscal Transaction Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Fiscal Transaction Summary Report lists all of the transactions entered into the system for a date or range of dates specified by the user. It differs from the transaction summary used by the Patient Fund Clerks in that it sorts by the date of the transaction, rather than the date the transaction was entered. This allows for predating entries for the previous month on the first day of the following month.

> Landscape: Select landscape page orientation when printing this report.

![](vpfs-version-1-2-user-guide/290.png)

> Figure F-8. Fiscal Transaction Summary Report

## Inactive Withdrawal Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Portrait: Select portrait page orientation when printing this report.

![](vpfs-version-1-2-user-guide/291.png)

> Figure F-9. Inactive Withdrawal Listing

## Indigent Patient Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report displays all patients that have been marked as “Indigent” in the Patient Status field.

> Portrait: Select portrait page orientation when printing this report.

![](vpfs-version-1-2-user-guide/292.png)

> Figure F-10. Indigent Patient Listing

## Min and Max Restrictions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option generates a report of all accounts on which the balance is outside of the range(s) specified in the minimum and maximum balance fields in the Patient Info tab.

> Landscape: Select landscape page orientation when printing this report.

> Appendix F

![](vpfs-version-1-2-user-guide/293.png)

> Figure F-11. Min and Max Restrictions

## Negative Balance Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option prints a list of all accounts with a negative balance in the stored balance, monthly restriction balance, or weekly restriction balance.

> Landscape: Select landscape page orientation when printing this report.

![](vpfs-version-1-2-user-guide/294.png)

> Figure F-12. Negative Balance Report

## Overdue Restriction Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option shows a list all Patient Funds accounts that are identified as “restricted” and have dates of restriction older than 180 days. Select this report by choosing the Overdue Restriction Search menu option. In the displayed or printed report of all accounts that have overdue restrictions, you will see each patient’s name, SSN, and current restriction date.

> Landscape: Select landscape page orientation when printing this report.

![](vpfs-version-1-2-user-guide/295.png)

## Patient Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure F-13. Overdue Restriction Search

> This option prints a list of all Patient Funds patients. Information includes the station, patient’s name, Social Security Number, claim number, ward, account status, patient type (restricted or unrestricted), date of current restriction (if any), date of birth, date of last transaction, and the stored balance for the account.

> Landscape: Select landscape page orientation when printing this report.

> Appendix F

> ![](vpfs-version-1-2-user-guide/296.png)

## Patient Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure F-14. Patient Listing

> The Patient Summary Report is used to produce a list of all your active Patient Funds accounts.

> Landscape: Select landscape page orientation when printing this report.

> ![](vpfs-version-1-2-user-guide/297.png)

## Productivity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure F-15. Patient Summary Report

> This report indicates the number of transactions that each system user posted for a range of dates. The total number of transactions posted appears at the end of the report. Unlike the other VPFS reports, which are patient oriented, the Productivity Report provides information about the workload. Only PFC supervisors have access to this report.

> Portrait: Select portrait page orientation when printing this report.

![](vpfs-version-1-2-user-guide/298.png)

## Station Balances

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure F-16. Productivity Report

> This option provides a report that shows the grand total of all the balances in the Patient Funds system for the Division you have logged in against. In addition, this report has subtotaling for any Child institutions the user is authorized to access. This report is used to reconcile the general ledger.

> The user has the option to run the report for a single institution or all institutions that a user is authorized to access.

> Portrait: Select portrait page orientation when printing this report.

> Appendix F

> ![](vpfs-version-1-2-user-guide/299.png)

> Figure F -17 Station Balances Report

## Transaction Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option produces a report of all the Patient Funds transactions entered into your system for a selected date range. Transactions are grouped by the date the transaction was entered. The report includes the station name, transaction ID, patient name, the reference code, transaction date and dollar amount, the type of transaction (deposit or withdrawal), and the User ID of the Patient Funds Clerk who processed the transaction.

> Landscape: Select landscape page orientation when printing this report.

> ![](vpfs-version-1-2-user-guide/300.png)