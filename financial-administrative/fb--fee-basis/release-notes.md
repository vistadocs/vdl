---
title: Fee Basis Version 3.5 Release Notes (1995)
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: (1995)
app_code: FB
app_name: Fee Basis
section: FIN
app_status: active
pkg_ns: FB
patch_ver: 3.5
patch_id: FB*3.5
group_key: "FB:FB:3.5"
file_numbers: []
security_keys: []
menu_options: 1
description: - [# Section 1 - Options](#section-1-options) - [# Section 2 - Routines](#section-2-routines) - [New Routines](#new-routines) - [Obsolete Routines](#obsolete-routines) - [Routines for Mapping (DSM)](#routines-for-mapping-dsm) - [# Section 3 - Package Changes](#section-3-package-changes) - [Payment P
audience: 
keywords: 
  - table
  - contents
  - payment
  - basis
  - payments
  - vendor
  - letters
  - suspension
  - print
  - sites
page_count: 0
word_count: 3724
section_count: 17
table_count: 0
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: January 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/fb3_5rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/fb3_5rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=40"
---

Decentralized Hospital Computer Program

Fee BasisRELEASE NOTES

January 1995

Information Systems Center

Albany, New York

Table of Contents

Section 1. Options 1

> New Options 1

> Obsolete Options 2

Section 2. Routines 3

> New Routines 3

> Obsolete Routines 3

> Routines for Mapping (DSM) 3

Section 3. Package Changes 5

> Payment Process 5

> CPT Modifiers/Fee Schedule 6

> CNH Movements and the AMIS 349 6

> Fee Basis Medical and Pharmacy Denials 6

> Purpose of Visit Code 6

> Telephone Inquiry Menu 7

> Nursing Home 10-0168 Report 8

> Suspension Letters 9

> Multiple Ancillary Payments 9

> Nursing Home Payments through the CNH Module 9

Section 4. File (DD) Changes 11

> New Files with Descriptions 11

> Obsolete Files 11

> File Changes 11

Section 5. Security Keys, Mail Groups, Bulletins 15

Section 6. Appendices 17

> Appendix A. PAID Server 17

> Appendix B. List Manager Actions 18

Index 19

# # Section 1 - Options


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Section 1 - Options](#section-1-options)
- [# Section 2 - Routines](#section-2-routines)
  - [New Routines](#new-routines)
  - [Obsolete Routines](#obsolete-routines)
  - [Routines for Mapping (DSM)](#routines-for-mapping-dsm)
- [# Section 3 - Package Changes](#section-3-package-changes)
  - [Payment Process](#payment-process)
  - [CPT Modifiers/Fee Schedule](#cpt-modifiersfee-schedule)
  - [CNH Movements and the AMIS 349](#cnh-movements-and-the-amis-349)
  - [Fee Basis Medical and Pharmacy Denials](#fee-basis-medical-and-pharmacy-denials)
  - [Purpose of Visit Code](#purpose-of-visit-code)
  - [Telephone Inquiry Menu](#telephone-inquiry-menu)
  - [Nursing Home 10-0168 Report](#nursing-home-10-0168-report)
  - [Suspension Letters](#suspension-letters)
- [# The Suspension Letter Print option now prompts the user to print denials only. If the user answers YES, only the denial letters for the programs selected print. Answering NO to this prompt prints all letters for the programs selected (as in the past). This prompt was added to allow the site the flexibility of generating only denial letters. This flexibility was requested by the sites in order to avoid vendor confusion when the vendor receives both the DHCP suspension letters and the Explanation of Benefits letter from the Austin Automation Center. Since the Explanation of Benefits letter contains a listing of payments covered by the check, as well as the suspension reasons for any partial payments, many sites felt it only necessary to generate denial letters to vendors from DHCP. This change provides sites with that functionality.](#the-suspension-letter-print-option-now-prompts-the-user-to-print-denials-only-if-the-user-answers-yes-only-the-denial-letters-for-the-programs-selected-print-answering-no-to-this-prompt-prints-all-letters-for-the-programs-selected-as-in-the-past-this-prompt-was-added-to-allow-the-site-the-flexibility-of-generating-only-denial-letters-this-flexibility-was-requested-by-the-sites-in-order-to-avoid-vendor-confusion-when-the-vendor-receives-both-the-dhcp-suspension-letters-and-the-explanation-of-benefits-letter-from-the-austin-automation-center-since-the-explanation-of-benefits-letter-contains-a-listing-of-payments-covered-by-the-check-as-well-as-the-suspension-reasons-for-any-partial-payments-many-sites-felt-it-only-necessary-to-generate-denial-letters-to-vendors-from-dhcp-this-change-provides-sites-with-that-functionality)
- [# A second suspension letter option was added to the Outputs Main menu under the Medical Fee program. This Individual Suspension Letter Print option was added to allow sites the flexibility to print letters for one patient and/or vendor.](#a-second-suspension-letter-option-was-added-to-the-outputs-main-menu-under-the-medical-fee-program-this-individual-suspension-letter-print-option-was-added-to-allow-sites-the-flexibility-to-print-letters-for-one-patient-andor-vendor)
- [## Multiple Ancillary Payments](#multiple-ancillary-payments)
- [# The Multiple Ancillary Payments option was added to allow sites the ability to add many ancillary payments that are identical (with the exception of date of service) as quickly and easily as possible. This option is similar to the Multiple Payment Entry option in the Medical program. The user is asked all similar payment information up front and is then allowed to enter multiple dates of service.](#the-multiple-ancillary-payments-option-was-added-to-allow-sites-the-ability-to-add-many-ancillary-payments-that-are-identical-with-the-exception-of-date-of-service-as-quickly-and-easily-as-possible-this-option-is-similar-to-the-multiple-payment-entry-option-in-the-medical-program-the-user-is-asked-all-similar-payment-information-up-front-and-is-then-allowed-to-enter-multiple-dates-of-service)
- [It is imperative that all sites use the Post Commitments for Obligation option PRIOR to processing any payments against that obligation each month. When version 3.5 is installed, there must be an estimate on the 1358 for each payment you are processing in order to release the payment.](#it-is-imperative-that-all-sites-use-the-post-commitments-for-obligation-option-prior-to-processing-any-payments-against-that-obligation-each-month-when-version-35-is-installed-there-must-be-an-estimate-on-the-1358-for-each-payment-you-are-processing-in-order-to-release-the-payment)
- [# In version 3.0, if you did not post your commitments, the software did it for you when you released the batch. However, as new authorizations were set up during the month, these were posted by patient. This was due to backward compatability with two versions of IFCAP. Now that all sites have been on IFCAP 4 for at least a year, Fee expects to find an entry on the 1358 for each of the CNH patients.](#in-version-30-if-you-did-not-post-your-commitments-the-software-did-it-for-you-when-you-released-the-batch-however-as-new-authorizations-were-set-up-during-the-month-these-were-posted-by-patient-this-was-due-to-backward-compatability-with-two-versions-of-ifcap-now-that-all-sites-have-been-on-ifcap-4-for-at-least-a-year-fee-expects-to-find-an-entry-on-the-1358-for-each-of-the-cnh-patients)
- [# # Section 4 - File (DD) Changes](#section-4-file-dd-changes)
  - [New Files with Descriptions](#new-files-with-descriptions)
  - [Obsolete Files](#obsolete-files)
  - [FEE CH REPORT OF CONTACT](#fee-ch-report-of-contact)
- [# Section 5 - Security Keys, Mail Groups, Bulletins](#section-5-security-keys-mail-groups-bulletins)
- [# Section 6. Appendices](#section-6-appendices)
  - [Appendix A - Paid Server](#appendix-a-paid-server)
  - [Appendix B - List Manager Actions](#appendix-b-list-manager-actions)
New Options
<u>FB CHECK DISPLAY</u>
Menu Text: Check Display
This option displays all payments included on a check that was issued after the payment conversion from CALM to the Financial Management System (FMS).
<u>FB PHONE MENU</u>
Menu Text: Telephone Inquiry Menu
This menu contains all options that are used to answer telephone inquiries from vendors and/or veterans regarding payments or checks.
<u>FB VENDOR/VETERAN PAYMENTS</u>
Menu Text: Payment Listing for Vendor/Veteran
This option prompts you to select the vendor who is calling and the veteran about whom information is being requested. It then calls VA List Manager to display a listing of payments for all Fee Basis programs in reverse chronological order by Service Date (with the most recent displaying first).
<u>FBAA AUTHORIZATION DISPLAY</u>
Menu Text: Authorization Display
This option displays an authorization on screen for a user-specified authorization number. The authorization number appears on the printed 7079.
<u>FBAA PAID SERVER</u>
Menu Text: Fee Basis Payment Message Server
This server processes incoming payment information sent from FMS.
<u>FBAA SUSPENSION LETTER INDIV</u>
Menu Text: Individual Suspension Letter Print
This option prints the suspension letters for an individual patient and/or vendor.
<u>FBCH MULTIPLE PAYMENTS</u>
Menu Text: Multiple Ancillary Payments
This option is used to enter identical ancillary services incurred while in a non-VA hospital for a specific patient and vendor. Only the date of service may differ.
<u>FBCNH RCS 10-0168 REPORT</u>
Menu Text: Nursing Home 10-0168 Report
This option generates the data for the Community Nursing Home Code Sheet 10-0168 (formerly the RCS 18-3 Report).
Obsolete Options
The following options may be deleted.
FBAA VENDOR CLEANUP
FBAA MRA VENDOR ADD FO

# # Section 2 - Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FBAACCB2 FBAACO5 FBAAUTL4 FBAAUTL5 FBAUTHP FBCKDIS

FBCKDIS1 FBNHAMI1 FBNHPC1 FBNHRAT1 FBNHRCS FBNHRCS1

FBNHRCS2 FBNHRCS3 FBNHRCS4 FBP35D FBPAID FBPAID1

FBPAID2 FBPAY21 FBPHON FBPHON1 FBPHON2 FBPRE35

FBPST35 FBPST35A FBPST35B FBPST35C FBUCUTL8

## Obsolete Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FBAACP0 FBAADEV FBAAMP2 FBAAPRE3 FBAASL2 FBAASL3

FBAASL4 FBCHUCEP FBPOST3 FBPST3 FBPST3A FBPST3B

FBPST3C FBPST3D FBUPLD FBUPLD1

## Routines for Mapping (DSM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FBAAAUT FBAACCB\* FBAACIE FBAACO\* FBAADEM\* FBAAEP\*

FBAAMP\* FBAAOB FBAAPI FBAAPIE\* FBAASCB\* FBAAUTL\*

FBAAVD\* FBCH78\* FBCHREQ\* FBCHSCB FBMRA\* FBNHEA\*

FBNHED\* FBNHEP\* FBNHPC FBNHRAT FBNHRC FBUC\*

# # Section 3 - Package Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Payment Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Version 3.5 of Fee Basis involves changes to the Austin Payment process. In prior versions, Fee Basis payments were processed using the following systems.

DHCP Fee—Users enter payment data and submit batches of payment line items to Central Fee.

Central Fee—A batch system that resides at the Austin Automation Center (AAC).

CALM—Central Fee creates CALM code sheets for payment release.

Previously, the interface among the three systems only operated in one direction, and no payment information was sent back to DHCP Fee other than processing reports.

The Financial Management System (FMS) software replaces the former CALM payment system. Central Fee has been modified to send payment documents to FMS and return payment documents confirmed by the treasury to DHCP.

In order to facilitate the changes to the payment process, DHCP now asks an additional prompt in the Enter Payment options for Outpatient, Civil Hospital, and Ancillary payments. The prompt allows you to select which line items are for contracted services. Prompts do not appear in the Community Nursing Home or Pharmacy modules, as these values are defaulted to "always a contract service" and "never a contract service" respectively.

DHCP now receives check information back from FMS upon confirmation by the treasury. A new DHCP output is available to display check information for a selected check number. Additionally, each payment history, batch listing, invoice display, or other output which displays line item information has now been modified to include check information, date paid, and/or check cancellation information. Line items that had previously been cancelled will be annotated with a plus sign (+) preceding the display.

## CPT Modifiers/Fee Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the release of the CPT V. 5.0 software package, Fee Basis now has the ability to break down services provided to the modifier level. The software now prompts you to select a modifier after the selection of the CPT code in all Outpatient Payment options. Input of the field is optional and can be bypassed if the information is not available or applicable. All DHCP outputs that display a CPT Code now display the CPT-Modifier combination.

With the inclusion of CPT Modifiers, Fee Basis V. 3.5 now provides the functionality of calculating the Fee Schedule at the modifier level.

## CNH Movements and the AMIS 349

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to version 3.5, users were required to exercise caution in selecting the appro-

priate patient movement types. If a wrong movement was entered, a movement was missed, or movements were incomplete, the Bed Occupants Remaining and Patient Days of Care totals were inaccurate on the AMIS 349 Print.

Version 3.5 of Fee Basis checks transfer and discharge types against the patient's previous movement. Screens have been placed on the Discharge or Transfer Types that are selectable based on the Last Movement Type.

## Fee Basis Medical and Pharmacy Denials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fee Basis Medical Denials file (#163) and the Fee Basis Pharmacy Denials file (#163.1) are being eliminated with this version of Fee Basis. A con-

version allows merging of the medical denials data into the Fee Basis Payment file (#162). All future denials will be stored in the respective payment files. Suspension letters will still print in the same fashion.

## Purpose of Visit Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A change to the state abbreviation for Alaska has been made to Purpose Of Visit (POV) Code 35. The description now reads: NON-VA HOSP. CARE FOR NSC COND. (AK, VI AND HI ONLY).

## Telephone Inquiry Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A telephone inquiry menu has been added to the Fee Basis Main Menu. This phone menu has been designed to assist users in retrieving payment and related informa-

tion from DHCP quickly and easily when contacted by a vendor or veteran. The menu currently contains four options, the first of which is a check display. Choosing this option allows you to enter the check number provided by the vendor. The option displays all payments included on a check that was issued after the payment conver-

sion from CALM to FMS and includes all line items paid for with that check number for all Fee Basis programs.

<u>New Option: Payment Listing for Vendor/Veteran</u>

The option Payment Listing for Vendor/Veteran is a new option that prompts you for a vendor and a veteran. The option places you in the VA List Manager utility, where data is returned in List Manager screen format. You can view, move through, and print information through the use of various List Manager actions. (Please refer to Appendix B for more information about List Manager's generic actions.) The first screen displays a listing of all payments, regardless of Fee Basis program, for the vendor and veteran selected in reverse chronological order by Service Date (listing the most recent first). Possible actions appear on the bottom of the screen, similar to the following screen example. Please refer to the Fee Basis V. 3.5 User Manual for more detail about this option.

![](fee-basis-version-3-5-release-notes-1995/001.png)

BS BATCH STATUS EV EXPAND VIEW DV DISPLAY VENDOR

LB LIST BATCH CP CHANGE PATIENT DC DISPLAY CHECK

ID INVOICE DISPLAY CV CHANGE VENDOR

LC LOOKUP CPT/MODIFIER DA DISPLAY AUTH/7078/583

Select Action:Quit//

The option is designed to handle all inquiries from one screen, thus eliminating the necessity of jumping to different menus to obtain information from varying programs.

<u>Yes/No Prompts</u>

Most Yes/No prompts throughout the Fee Basis software now also accept numeric entries of "0" (zero) for a NO response or "1" (one) for a YES response.

## Nursing Home 10-0168 Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option has been added to the Output Main Menu for the Community Nursing Home Program. The format of the report has changed. Version 3.5 of Fee Basis, when used with Version 2.0 of the Generic Code Sheet software, also allows you to create code sheets with a status of MARKED FOR BATCHING. The following table describes the fields included in the new 10-0168 (former RCS 18-3) Report.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 51%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>FIELD</strong></td>
<td><strong>VALUE</strong></td>
<td><strong>POSITION</strong></td>
</tr>
<tr class="even">
<td>Header Field</td>
<td>CNH</td>
<td>1–3</td>
</tr>
<tr class="odd">
<td>Station Number</td>
<td>Station Number</td>
<td>4–6</td>
</tr>
<tr class="even">
<td>Name of CNH</td>
<td>Free Text</td>
<td>7–29</td>
</tr>
<tr class="odd">
<td>City of CNH</td>
<td>Free Text</td>
<td>30–44</td>
</tr>
<tr class="even">
<td>State Code of CNH</td>
<td>Two Numbers</td>
<td>45–46</td>
</tr>
<tr class="odd">
<td>County Code of CNH</td>
<td>Three Numbers</td>
<td>47–49</td>
</tr>
<tr class="even">
<td>Number of Beds</td>
<td>Three Numbers</td>
<td>50–52</td>
</tr>
<tr class="odd">
<td>CNH Inspected/Accredited</td>
<td><p>I = Inspected</p>
<p>A = Accredited</p>
<p>B = Both</p></td>
<td>53</td>
</tr>
<tr class="even">
<td>Per Diem Rate (HIGH)</td>
<td>Three Numbers</td>
<td>54–56</td>
</tr>
<tr class="odd">
<td>Per Diem Rate (LOW)</td>
<td>Three Numbers</td>
<td>57–59</td>
</tr>
<tr class="even">
<td>Certified Medicare/Medicaid</td>
<td><p>1 = Not certified for either</p>
<p>2 = Certified for Medicare only</p>
<p>3 = Certified for Medicaid only</p>
<p>4 = Certified for both Medicare and Medicaid</p></td>
<td>60</td>
</tr>
<tr class="odd">
<td>Number of Veterans in CNH</td>
<td>Three Numbers</td>
<td>61–63</td>
</tr>
<tr class="even">
<td>Date of Last Assessment</td>
<td>MMYY</td>
<td>64–67</td>
</tr>
<tr class="odd">
<td>Text Terminator</td>
<td>$</td>
<td>68</td>
</tr>
</tbody>
</table>

## Suspension Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # The Suspension Letter Print option now prompts the user to print denials only. If the user answers YES, only the denial letters for the programs selected print. Answering NO to this prompt prints all letters for the programs selected (as in the past). This prompt was added to allow the site the flexibility of generating only denial letters. This flexibility was requested by the sites in order to avoid vendor confusion when the vendor receives both the DHCP suspension letters and the Explanation of Benefits letter from the Austin Automation Center. Since the Explanation of Benefits letter contains a listing of payments covered by the check, as well as the suspension reasons for any partial payments, many sites felt it only necessary to generate denial letters to vendors from DHCP. This change provides sites with that functionality.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # A second suspension letter option was added to the Outputs Main menu under the Medical Fee program. This Individual Suspension Letter Print option was added to allow sites the flexibility to print letters for one patient and/or vendor.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ## Multiple Ancillary Payments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # The Multiple Ancillary Payments option was added to allow sites the ability to add many ancillary payments that are identical (with the exception of date of service) as quickly and easily as possible. This option is similar to the Multiple Payment Entry option in the Medical program. The user is asked all similar payment information up front and is then allowed to enter multiple dates of service.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Nursing Home Payments through the CNH Module

# It is imperative that all sites use the Post Commitments for Obligation option PRIOR to processing any payments against that obligation each month. When version 3.5 is installed, there must be an estimate on the 1358 for each payment you are processing in order to release the payment.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # In version 3.0, if you did not post your commitments, the software did it for you when you released the batch. However, as new authorizations were set up during the month, these were posted by patient. This was due to backward compatability with two versions of IFCAP. Now that all sites have been on IFCAP 4 for at least a year, Fee expects to find an entry on the 1358 for each of the CNH patients.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # Section 4 - File (DD) Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Files with Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

162.95 Fee Basis Check Cancellation Reason

This file stores the check cancellation reasons and codes used by the Financial Management System (FMS). These reasons will be returned to the site from FMS when a check is cancelled. This file is pointed to by all payment files. \*\*\*Per VHA Directive 10-93-142, this file definition should not be modified. \*\*\*

## Obsolete Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

163 Fee Basis Medical Denials

163.1 Fee Basis Pharmacy Denials

File Changes161 FEE BASIS PATIENT

> <u>Fields Deleted</u>

> 4 CNH LEVEL OF CARE

> 102 AUSTIN DELETED

> 103 DATE OF AUSTIN DELETE

> 104 DATE TRANSMITTED TO AUSTIN

> <u>Field Type Changes</u>

> .096 ACCIDENT RELATED (Y/N) Free Text

> .097 POTENTIAL COST RECOVERY CASE Free Text

> 102 AUSTIN DELETE FLAG Free Text

161.2 FEE BASIS VENDOR

> <u>Fields Deleted</u>

> 16 NUMBER OF SKILLED BEDS

> 17 NUMBER OF INTERMEDIATE BEDS

> 21 LEVELS OF CARE PROVIDED

> <u>Field Type Changes</u>

> 30.03 1099 VENDOR Free Text

161.4 FEE BASIS SITE PARAMETERS

> <u>Fields Marked for Deletion</u>

> 21 ASK PROGRAM SPECIFIC AUTH.

> <u>Fields Deleted</u>

> 36 LAST UC UPDATED

> 37 DATE UC CONVERSION COMPLETED

> <u>Field Type Changes</u>

> 12 MEDICAL PAYMENT VENDOR DISPLAY Free Text

> 13 PHARMACY PAYMENT VENDOR DISPLAY Free Text

> 19 EDIT AUTH. DURING PAYMENT Free Text

## FEE CH REPORT OF CONTACT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Field Type Changes</u>

> 16.5 VETERAN HAVE OTHER INSURANCE Free Text

162 FEE BASIS PAYMENT

> <u>New Cross-References</u>

> CHECK NUMBER (ACK)

> CHECK NUMBER (ACKT)

> CPT MODIFIER (AE1)

> <u>New Fields</u>

> 162.03 - SERVICE PROVIDED

> 33 VENDOR INVOICE DATE

> 34 PROMPT PAY TYPE

> 35 CHECK NUMBER

> 36 CANCELLATION DATE

> 37 REASON CODE

> 38 CANCELLATION ACTIVITY

> 39 CPT MODIFIER

> 40 DISBURSED AMOUNT

> 41 INTEREST AMOUNT

> 162.04 - TRAVEL PAYMENT DATE

> 8 DATE PAID

> 9 CHECK NUMBER

> 10 CANCELLATION DATE

> 11 REASON CODE

> 12 CANCELLATION ACTIVITY

> 13 DISBURSED AMOUNT

> 14 INTEREST AMOUNT

> <u>Field Type Changes</u>

> 32 SERVICE CONNECTED CONDITION? Free Text

162 FEE BASIS PAYMENT, cont.

> <u>Fields Marked for Deletion</u>

> 1.5 FEE PROGRAM

> <u>Obsolete Cross-References</u>

> REJECT STATUS (AF)

162.1 FEE BASIS PHARMACY INVOICE

> <u>New Cross-References</u>

> CHECK NUMBER (ACK)

> <u>New Fields</u>

> 162.12 - SUSPENSION DESCRIPTION

> 28 DATE PAID

> 29 PROMPT PAY TYPE

> 30 CHECK NUMBER

> 31 CANCELLATION DATE

> 32 REASON CODE

> 33 CANCELLATION ACTIVITY

> 34 DISBURSED AMOUNT

> 35 INTEREST AMOUNT

162.2 FEE NOTIFICATION/REQUEST

> <u>Field Type Changes</u>

> 8 LEGAL ENTITLEMENT Free Text

> 11 MEDICAL ENTITLEMENT Free Text

162.5 FEE BASIS INVOICE

> <u>New Cross-References</u>

> CHECK NUMBER (ACK)

> <u>New Fields</u>

> 45 DATE PAID

> 46 VENDOR INVOICE DATE

> 47 PROMPT PAY TYPE

> 48 CHECK NUMBER

> 49 CANCELLATION DATE

> 50 REASON CODE

> 51 CANCELLATION ACTIVITY

> 52 DISBURSED AMOUNT

> 53 INTEREST AMOUNT

162.7 FEE BASIS UNAUTHORIZED CLAIMS

> <u>Fields Marked for Deletion</u>

> 16 DISPOSITION DESCRIPTION

> 17 REASON FOR PENDING

163.99 FEE BASIS FEE SCHEDULE

> <u>Field Type Changes</u>

> .01 CPT-MODIFIER Free Text

# # Section 5 - Security Keys, Mail Groups, Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new security keys, mail groups, or bulletins issued with this version of Fee Basis. There are also no obsolete bulletins with this version.

# # Section 6. Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Appendix A - Paid Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a sample PAID Server mail message.

Subj: Server Request Notice \[#183837\] 27 May 94 11:15 20 Lines

From: POSTMASTER Page 1

------------------------------------------------------------------------------

May 26, 1994 2:50 PM

A request for execution of a server option has been received.

Sender: REDACTED

Option name: FBAA PAID SERVER

Subject: FPA/ \#941461343846831

Message \#: 183818

Comments: No errors detected by the Menu System.

This is the server bulletin XQSERVER

The 'AMOUNT PAID' has been altered on the Fee Payment Voucher Document

in FMS for the following payments:

Check Number: 102 to SEAL POINT MEDICAL CNH for FEEpatient, One - 0000

From Date: 9/1/93 To Date: 9/5/93 Invoice Number: 1481

\>\>\> For detailed payment information use the appropriate payment output. \<\<\<

Select MESSAGE Action: IGNORE (in IN basket)//

## Appendix B - List Manager Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of generic List Manager actions with a brief description of each. The mnemonic for each action is shown in brackets \[ \] following the action name. Entering the mnemonic is the quickest way to select an action.

ActionDescription

Next Screen \[+\] Move to the next screen.

Previous Screen \[-\] Move to the previous screen.

Up a Line \[UP\] Move up one line.

Down a Line \[DN\] Move down one line.

Shift View to Right \[\>\] Move the screen to the right if the screen width is more than 80 characters.

Shift View to Left \[\<\] Move the screen to the left if the screen width is more then 80 characters.

First Screen \[FS\] Move to the first screen.

Last Screen \[LS\] Move to the last screen.

Go to Page \[GO\] Move to any selected page in the list.

Refresh Screen \[RE\] Redisplay the current screen.

Print Screen \[PS\] Prints the header and the portion of the list currently displayed.

Print List \[PL\] Prints the list of entries currently displayed.

Search List \[SL\] Finds selected text in list of entries.

Auto Display(On/Off) \[ADPL\] Toggles the menu of actions to be displayed/not displayed automatically.

Quit \[QU\] Exits the screen.

Index

Appendices 17

Bulletins 15

CNH Movements and the AMIS 349 6

CPT Modifiers/Fee Schedule 6

Fee Basis Medical and Pharmacy Denials 6

File Changes 11

File (DD) Changes 11

Files with Descriptions 11

List Manager Actions 18

Mail Groups 15

Multiple Ancillary Payments 9

Nursing Home 10-0168 Report 8

Nursing Home Payments through the CNH Module 9

Options 1

Package Changes 5

PAID Server 17

Payment Process 5

Purpose of Visit Code 6

Routines 3

Routines for Mapping (DSM) 3

Section 1. (see Options)

Section 2. (see Routines)

Section 3. (see Package Changes)

Section 4. (see File (DD) Changes)

Section 5. (see Security Keys, Mail Groups, Bulletins)

Section 6. (see Appendices)

Security Keys 15

Suspension Letters 9

Telephone Inquiry Menu 7