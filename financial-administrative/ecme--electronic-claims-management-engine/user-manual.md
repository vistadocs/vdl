---
title: ECME User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: ECME
app_name: Electronic Claims Management Engine
section: FIN
app_status: archive
pkg_ns: ECME
patch_ver: 1.0
patch_id: ECME*1.0
group_key: "ECME:ECME:1.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - ecme
  - claim
  - claims
  - report
  - pharmacy
  - date
  - patient
  - view
  - status
  - example
page_count: 0
word_count: 42166
section_count: 33
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)_Archive/bps_1_0_p28_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)_Archive/bps_1_0_p28_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=252"
---

---
title: |
  Electronic Claims Management Engine (ECME)

  Version 1.0

  User Manual
---

![](ecme-user-manual/001.png)

May 2021

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc72333925" class="anchor"></span>Table 1: List of Users with Suggested ECME Menus and Security Keys</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 39%" />
<col style="width: 23%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description (Patch # if applicable)</th>
<th>Project Manager</th>
<th>Technical Writer</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>05/2021</td>
<td><p>Updated for BPS*1*28</p>
<p>Updated Title Page date and footers</p>
<p>Added Section 6.3.3 SC Prescriptions for Active Duty Prescriptions</p>
<p>Added Section 8.1.11 Duplicate Claims Report</p></td>
<td>MCCF EDI TAS ePharmacy Development Team</td>
<td>MCCF EDI TAS ePharmacy Development Team</td>
</tr>
<tr class="even">
<td>12/2020</td>
<td><p>Updated for BPS*1*27</p>
<p>Updated Potential Secondary Rx Claims Report Screen Display</p>
<p>Updated Title Page date and footers</p></td>
<td>MCCF EDI TAS ePharmacy Development Team</td>
<td>MCCF EDI TAS ePharmacy Development Team</td>
</tr>
<tr class="odd">
<td>04/2020</td>
<td><p>Updated for BPS*1*26</p>
<p>Updated section 5.6 Add/View Comments</p>
<p>Updated Title Page date and footers</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>1/2019</td>
<td><p>Updated for BPS*1*24</p>
<p>Change label on Claim Log, Modify Change View (CV), Enhance Claim Reports</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/2018</td>
<td><p>Updated for BPS*1*23</p>
<p>Update Title page date, footer date</p>
<p>Modification filter questions CV Change View action, Rx Activity Log to add Date of Service to ECME Log, Resubmit with Edits action, Process Secondary/TRICARE Rx to ECME option, Payable Claims Report, Rejected Claims Report, Reversal Claims Report, Claims Submitted Not Yet Released Report, Recent Transactions Report, Closed Claims Report, View ePharmacy Rx Report Option</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>11/2017</td>
<td><p>Updated for BPS*1*22</p>
<p>Update Title page date, modification to Change View action; change auto-reverse parameter and auto-reversal bulletin; add Facility ID Qualifier and Reconciliation ID to Claim Log and Claim Response Inquiry; add new action PR Print Reports to VER View ePharmacy Rx.</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>05/2017</td>
<td>Updated for BPS*1*21</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>08/2016</td>
<td>Updated for BPS*1*20</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>06/2016</td>
<td><p>Updated Title Page to current OI&amp;T standards.</p>
<p>Updated for BPS*1*19 to reflect customer requested revisions throughout screenshots including numerous changes throughout to update for inclusion of the Close Claim functionality and the new Non-Billable Status Report (NBS)</p></td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/2015</td>
<td>Updated for BPS*1*18</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>11/2013</td>
<td>Updated for BPS*1*15 (made numerous minor changes throughout; fixed defective page breaks)</td>
<td>REDACTED</td>
<td>FirstView Team</td>
</tr>
<tr class="even">
<td>02/2012</td>
<td>Updated for BPS*1*11</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>10/2011</td>
<td>Updated for BPS*1*10</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>06/2011</td>
<td>Updated for BPS*1*10 and consistency</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>12/2010</td>
<td>Reviewed and updated revisions; inserted TRICARE disclaimer</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/2010</td>
<td>Updated for accuracy changes per CBO</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/2010</td>
<td>Updated for BPS*1*8 and Addendum</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>10/2009</td>
<td>Updated for patch BPS*1.0*8 ePharmacy COB Support</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>04/2009</td>
<td>Updated for patch BPS*1.0*7</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/2007</td>
<td>Updated for patch BPS*1.0*2</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>08/2006</td>
<td>Updated for interim patch BPS*1.0*3</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>04/2006</td>
<td>Initial release of the ECME User Manual.</td>
<td>REDACTED</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

<span id="_Toc72333925" class="anchor"></span>Table 1: List of Users with Suggested ECME Menus and Security Keys

Table of Contents

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Orientation](#orientation)
  - [Working with the ECME User Manual](#working-with-the-ecme-user-manual)
  - [Obtaining Online Help](#obtaining-online-help)
  - [Finding Related Manuals](#finding-related-manuals)
- [ECME Menu Structures](#ecme-menu-structures)
  - [The Complete ECME Menu Structure](#the-complete-ecme-menu-structure)
  - [ECME User Screen](#ecme-user-screen)
  - [ECME Pharmacy COB Menu Structure](#ecme-pharmacy-cob-menu-structure)
  - [Pharmacy ECME Manager Menu Structure](#pharmacy-ecme-manager-menu-structure)
  - [Pharmacy Electronic Claims Reports Menu Structure](#pharmacy-electronic-claims-reports-menu-structure)
- [Accessing the ECME Main Menu](#accessing-the-ecme-main-menu)
- [Accessing the ECME User Screen](#accessing-the-ecme-user-screen)
  - [Change View](#change-view)
  - [Sort List](#sort-list)
  - [Reverse Payable Claim](#reverse-payable-claim)
  - [Resubmit Claim](#resubmit-claim)
  - [Close Claim](#close-claim)
    - [Variations to the Close Claim Process](#variations-to-the-close-claim-process)
    - [Special Notes Regarding Secondary Claims](#special-notes-regarding-secondary-claims)
  - [Add / View Comments](#add-view-comments)
  - [Further Research Screen](#further-research-screen)
    - [Insurance Details](#insurance-details)
    - [View Eligibility](#view-eligibility)
    - [View Prescription](#view-prescription)
    - [Add / View Comments](#add-view-comments-1)
    - [Claims Tracking](#claims-tracking)
    - [Third Party Inquiry](#third-party-inquiry)
    - [On Hold Copay Listing](#on-hold-copay-listing)
    - [Release Copay](#release-copay)
    - [IB (Integrated Billing) Events Report](#ib-integrated-billing-events-report)
    - [Group Plan Menu](#group-plan-menu)
    - [Eligibility Inquiry Option](#eligibility-inquiry-option)
  - [Print Claim Log (Hidden Action)](#print-claim-log-hidden-action)
  - [Send to Worklist](#send-to-worklist)
  - [Reopen Closed Claims (Hidden Action)](#reopen-closed-claims-hidden-action)
  - [Resubmit with Edits (Hidden Action)](#resubmit-with-edits-hidden-action)
  - [OPECC Reject Information (Hidden Action)](#opecc-reject-information-hidden-action)
  - [Resubmit Claim Without Reversal (Hidden Action)](#resubmit-claim-without-reversal-hidden-action)
  - [Open / Close Non-Billable Entry (Hidden Action)](#open-close-non-billable-entry-hidden-action)
  - [Display Update (Hidden Action)](#display-update-hidden-action)
  - [Exit (From ECME User Screen)](#exit-from-ecme-user-screen)
- [Accessing the ECME Pharmacy COB Menu](#accessing-the-ecme-pharmacy-cob-menu)
  - [Potential Secondary Rx Claims Report](#potential-secondary-rx-claims-report)
  - [Potential Claims Report for Dual Eligible](#potential-claims-report-for-dual-eligible)
  - [Process Secondary / TRICARE Rx to ECME](#process-secondary-tricare-rx-to-ecme)
    - [Submitting Secondary Claims](#submitting-secondary-claims)
    - [Submitting Primary Claims for TRICARE and Dual Eligibility Patients](#submitting-primary-claims-for-tricare-and-dual-eligibility-patients)
    - [SC Prescriptions for Active Duty Patients](#sc-prescriptions-for-active-duty-patients)
- [Accessing the Pharmacy ECME Manager Menu](#accessing-the-pharmacy-ecme-manager-menu)
  - [ECME Transaction Maintenance Options](#ecme-transaction-maintenance-options)
    - [View / Unstrand Submissions Not Completed](#view-unstrand-submissions-not-completed)
    - [REOPEN a CLOSED ECME Claim](#reopen-a-closed-ecme-claim)
  - [Pharmacy ECME Setup Menu](#pharmacy-ecme-setup-menu)
    - [Edit Basic ECME Parameters](#edit-basic-ecme-parameters)
    - [Edit ECME Pharmacy Data](#edit-ecme-pharmacy-data)
    - [Register Pharmacy with Austin Information Technology Center](#register-pharmacy-with-austin-information-technology-center)
  - [Statistics Screen](#statistics-screen)
    - [Update Continuously](#update-continuously)
    - [Display Update](#display-update)
    - [Zero (Clear) Statistics](#zero-clear-statistics)
    - [Exiting the Statistics Screen](#exiting-the-statistics-screen)
- [Accessing the Pharmacy Electronic Claims Reports](#accessing-the-pharmacy-electronic-claims-reports)
  - [Claim Results and Status](#claim-results-and-status)
    - [Payable Claims Report](#payable-claims-report)
    - [Rejected Claims Report](#rejected-claims-report)
    - [CMOP / ECME Activity Report](#cmop-ecme-activity-report)
    - [Reversal Claims Report](#reversal-claims-report)
    - [Claims Submitted, Not Yet Released](#claims-submitted-not-yet-released)
    - [Recent Transactions](#recent-transactions)
    - [Totals by Date](#totals-by-date)
    - [Closed Claims Report](#closed-claims-report)
    - [Non-Billable Status Report](#non-billable-status-report)
    - [Spending Account Report](#spending-account-report)
    - [Duplicate Claims Report](#duplicate-claims-report)
  - [Other Reports](#other-reports)
    - [ECME Claims-Response Inquiry Option](#ecme-claims-response-inquiry-option)
    - [Payer Sheet Detail Report Option](#payer-sheet-detail-report-option)
    - [ECME Setup – Pharmacies Report](#ecme-setup-pharmacies-report)
    - [Turn-around time statistics](#turn-around-time-statistics)
    - [View ePharmacy Rx](#view-epharmacy-rx)
    - [OPECC Productivity Report](#opecc-productivity-report)
- [BPS Nightly Background Job](#bps-nightly-background-job)
- [Glossary](#glossary)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
The Electronic Claims Management Engine (ECME) generates electronic claims in National Council for Prescription Drug Programs (NCPDP) V. D.0 formats, based on the Outpatient Pharmacy V. 7.0 workflow.
ECME:
- Allows pharmacy claims processing staff to submit, resubmit, and reverse electronic claims.
- Provides reports for end users and management on claims status, transaction history, and system configuration standings.
- Allows Automated Data Processing Application Coordinator (ADPAC) and Information Resources Management Service (IRMS) staff to configure ECME to pharmacy site specifications.
- Allows Eligibility Inquiry and Verification transactions for verification of valid patient pharmacy insurance.
ECME claims processing begins when events within Outpatient Pharmacy V. 7.0 meet specific criteria, based on Integrated Billing (IB) V. 2.0 determination, that indicate the system should generate an electronic claim. To build a claim through ECME, several conditions must be met. First, the patient must be registered and have pharmacy prescription insurance coverage. Second, the patient must be a non-service-connected patient or if service connected; the prescription must not be for the service-connected condition. The patient must not have an environmental indicators condition unless the patient is Active Duty. (If the patient is Active Duty, all prescriptions are billable). Finally, the drug must be billable. Logic embedded within ECME manages the creation of the electronic claim, which requires integration with IB V. 2.0, Pharmacy Data Management, and National Drug File (NDF) V.4.0. ECME also generates claims during Consolidated Mail Outpatient Pharmacy (CMOP) V. 2.0 processing for prescriptions that meet billing requirements.
The Veterans Health Administration (VHA) developed ECME software in order to comply with the Health Insurance Portability and Accountability Act (HIPAA) of 1996 and updated it to comply with the HIPAA rule of 2009, which requires health care providers to transmit outpatient pharmacy prescription claims to payers electronically in the NCPDP format and to receive responses on a real-time basis. ECME is derived from the Point of Sale (POS) Application developed by the Indian Health Service (IHS) and is assigned to the BPS namespace.
The ECME User Manual helps users submit electronic claims, aids ADPAC and IRMS staff in configuring ECME to pharmacy site specifications and is a reference manual for all screens and options within ECME. While the ECME User Manual does explain how to use the Electronic Management Claims Engine, it is not intended to show how ECME interacts with Outpatient Pharmacy V. 7.0, IB V. 2.0, the Austin Information Technology Center, and other software packages to build, submit, receive, and process an electronic claim.
The ECME User Manual assumes that the user is familiar with the VistA computing environment, including the Outpatient Pharmacy V. 7.0 workflow and the Department of Veterans Affairs (DVA) FileMan data structures and terminology.
The ECME User Manual consists of the following sections.
- ECME Introduction: Outlines the history, use, and intent of the ECME software.
- ECME Orientation: Shows how to use the menus and options to generate an electronic claim, obtain online help, and find related manuals.
- ECME Menu Structures: Lists the complete ECME menu structure. It also lists the ECME User, Manager, and Reports menus.
- Accessing the ECME Menu: Describes how to gain access to the ECME main Menu.
- Accessing the ECME User Screen: Describes the elements of submitting pharmacy claims to insurers through the ECME system.
- Accessing the ECME PHARMACY COB menu: Describes the elements of submitting pharmacy claims to secondary insurers and submitting TRICARE claims.
- Accessing the Pharmacy ECME Manager Menu: Describes electronic claims management features that require management level decisions.
- Accessing the Pharmacy Electronic Claims Reports: Describes the reports generated by ECME.
- ECME Background Jobs: Describes the tasks performed by the Nightly Background Job.
- Glossary: Defines common ECME-related terms.
- Acronyms: Lists ECME-related acronyms.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Working with the ECME User Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Electronic Claims Management Engine (ECME) User Manual is a menu- and option-oriented manual. In most cases, the manual describes a menu or option, shows how to access it, and uses tables and screen shots to describe its fields.

The ECME User Manual uses the following methods to enhance readability:

- Menu options and screen actions are italicized.

Example: The *Add Pharmacy / OPECC Comment* action triggers the system to display the Pharmacy / OPECC Comment on the ECME User Screen.

- Screen prompts are denoted with quotation marks around them.

Example: The “Select Action:” prompt will display next.

- Variable names, formal name of options, field and file names, and security keys are completely uppercase.

Example: The BPS USER key.

- Screen captures / dialogues are shaded and shown in a non-proportional font.
1.  User responses to online prompts are in boldface type.

> Example: Select Pharmacy ECME User Menu Option: RPT.

2.  \<Enter\> indicates the user must press the Enter key (or Return key) on the keyboard to proceed to the next prompt. Other keys are represented within \< \> angle brackets.

> Example:

> Select Pharmacy ECME Manager Menu Option: ?\<Enter\>

- The following symbols alerts the user to special information.
- IMPORTANT cautions the user to notice critical information. Example:

  IMPORTANT: Cautions the user to notice critical information.
- NOTE indicates important or helpful information. Example:
1.  Important or helpful information.
- Key options are locked with a particular security key. The user must hold the particular security key to be able to perform the menu option. Example:

  Key The user must hold the BPS MANAGER and BPS MENU keys to access the Pharmacy ECME Manager Menu options.

## Obtaining Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECME software provides online help and commonly used system default prompts. The user can enter question marks at any response prompt. At the end of the help display, VistA (Veterans Health Information Systems and Technology Architecture) immediately returns the user to the starting point.

To retrieve Online Help in any VistA character-based product:

- Enter a single question mark (?) at a field / prompt to obtain a brief description:
1.  If a field is a pointer, entering one question mark (?) displays the HELP PROMPT field contents and a list of choices if the list is short.
3.  If the list is long, the system will ask if the entire list should be displayed. A Y(ES) response will invoke the display. By prefacing the starting point with an up-arrow (^) as a response, the user can give the display a starting point. For example, ^M starts an alphabetic listing at the letter M instead of the letter A while ^127 starts any listing at the 127th entry.
- Enter two question marks (??) at a field / prompt for a more detailed description. If a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks (???) at a field / prompt to invoke any additional Help text stored in Help Frames.

## Finding Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To learn more about the ECME V. 1.0 software, please consult the following:

- Electronic Claims Management Engine (ECME) V. 1.0 Technical Manual / Security Guide

All ECME V. 1.0 documentation can be found at the VistA Documentation Library.

VHA-oriented HIPAA (Health Insurance Portability and Accountability Act) information can be found at REDACTED.

# ECME Menu Structures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a map of the Electronic Claims Management Engine (ECME) menu structure including a list of all options. ECME is a menu-driven system that allows access based on the security keys that the user holds.

Currently, ECME has the following security keys: BPSMENU, BPS USER, BPS MANAGER, BPS MASTER, BPS SUPERVISOR, and BPS REPORTS. All users must have the BPSMENU key in addition to the specific keys listed below.

The following table lists the type of users who would need access to a specific menu and the ECME Security Keys the user must hold to access a particular ECME menu. For example, the OPECC (Outpatient Pharmacy Electronic Claims Coordinator) would need access to all ECME menus, while a Pharmacy Technician might only need access to the Main Menu, ECME User Screen, and Reports menus.

<table>
<caption><p><span id="_Toc72333926" class="anchor"></span>Table 2: Four Areas of the ECME User Screen</p></caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 37%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Type of User</th>
<th>*ECME Menu</th>
<th>ECME Security Keys</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OPECC</td>
<td><p>All ECME Menus:</p>
<blockquote>
<p>ECME Main Menu</p>
<p>ECME User Screen</p>
<p>ECME Pharmacy COB</p>
<p>Pharmacy ECME Manager Menu</p>
<p>Pharmacy Electronic Claims Reports</p>
</blockquote></td>
<td><p>BPSMENU</p>
<p>BPS USER</p>
<p>BPS MANAGER</p>
<p>BPS REPORTS</p></td>
</tr>
<tr class="even">
<td>Pharmacist, Pharmacy Technician</td>
<td><p>ECME Main Menu</p>
<p>ECME User Screen</p>
<p>Pharmacy Electronic Claims Reports</p></td>
<td><p>BPSMENU</p>
<p>BPS USER</p>
<p>BPS REPORTS</p></td>
</tr>
<tr class="odd">
<td>ePharmacy Site Manager and Back-up</td>
<td><p>ECME Main Menu</p>
<p>ECME User Screen</p>
<p>Pharmacy ECME Manager Menu</p>
<p>Pharmacy Electronic Claims Reports</p></td>
<td><p>BPSMENU</p>
<p>BPS USER</p>
<p>BPS MANAGER</p>
<p>BPS MASTER</p>
<p>BPS REPORTS</p></td>
</tr>
<tr class="even">
<td><p>ADPAC</p>
<p>(Automated Data Processing Application Coordinator)</p></td>
<td><p>ECME Main Menu</p>
<p>ECME Pharmacy COB</p>
<p>Pharmacy ECME Manager Menu</p>
<p>Pharmacy Electronic Claims Reports</p></td>
<td><p>BPSMENU</p>
<p>BPS MANAGER</p>
<p>(BPS MASTER is also</p>
<p>required to access certain</p>
<p>MGR menu options)</p>
<p>BPS REPORTS</p></td>
</tr>
<tr class="odd">
<td><p>IRMS</p>
<p>(Information Resources Management Service)</p></td>
<td><p>ECME Main Menu</p>
<p>Pharmacy ECME Manager Menu</p>
<p>Pharmacy Electronic Claims Reports</p></td>
<td><p>BPSMENU</p>
<p>BPS MANAGER (BPS MASTER is also required to access certain MGR menu options)</p>
<p>BPS REPORTS</p></td>
</tr>
<tr class="even">
<td>OPECC Supervisor</td>
<td>Pharmacy Electronic Claims Reports</td>
<td><p>BPS SUPERVISOR</p>
<p>BPS REPORTS</p></td>
</tr>
</tbody>
</table>

<span id="_Toc72333926" class="anchor"></span>Table 2: Four Areas of the ECME User Screen

## The Complete ECME Menu Structure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The complete list of ECME menu options is shown below. The OPECC needs to access all ECME options.

Key The user must hold the BPSMENU and BPS MANAGER keys to view the Pharmacy ECME Manager Menu option. The BPS MASTER key is also required to view the Edit ECME Pharmacy Data (PHAR), Pharmacy ECME Setup Menu (SET), Edit Basic ECME Parameters (BAS), and Register Pharmacy with Austin Information Technology Center (REG) options.

U ECME User Screen…

COB ECME Pharmacy COB…

> SEC Potential Secondary Rx Claims Report

> TRI Potential Claims Report for Dual Eligible

> PRO Process Secondary / TRICARE Rx to ECME

MGR Pharmacy ECME Manager Menu…

> MNT ECME transaction maintenance options…

> UNS View / Unstrand Submissions Not Completed

> ROC Re Open CLOSED Claim

> SET Pharmacy ECME Setup Menu…

> BAS Edit Basic ECME Parameters

> PHAR Edit ECME Pharmacy Data

> REG Register Pharmacy with Austin Information Technology Center

> STAT Statistics Screen

RPT Pharmacy Electronic Claims Reports…

> CLA Claim Results and Status…

> PAY Payable Claims Report

> REJ Rejected Claims Report

> ECMP CMOP / ECME Activity Report

> REV Reversal Claims Report

> NYR Claims Submitted, Not Yet Released

> REC Recent Transactions

> DAY Totals by Date

> CLO Closed Claims Report

> NBS Non-Billable Status Report

> SPA Spending Account Report

> OTH Other Reports…

> CRI ECME Claims-Response Inquiry

> PAY Payer Sheet Detail Report

> PHAR ECME Setup - Pharmacies Report

> TAT Turn-around time statistics

> VER View ePharmacy Rx

> OPR OPECC Productivity Report

## ECME User Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ECME User Screen structure is listed below. The ECME User Screen is a List Manager screen that has multiple actions contained within the option. OPECCs must have access to this option. It may be helpful for Pharmacists and the ePharmacy Site Manager to have access also.

Key The user must hold the BPS MENU and BPS USER keys to view the ECME User Screen option.

U ECME User Screen

## ECME Pharmacy COB Menu Structure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *ECME Pharmacy COB Menu* option structure is listed below. OPECCs must be able to access this menu.

Key The user must hold the BPSMENU keys to view the ECME Pharmacy COB option.

COB ECME Pharmacy COB…

> SEC Potential Secondary Rx Claims Report

> TRI Potential Claims Report for Dual Eligible

> PRO Process Secondary / TRICARE Rx to ECME

## Pharmacy ECME Manager Menu Structure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Pharmacy ECME Manager Menu* option structure is listed below. ADPAC, IRMS (Information Resources Management Service) and OPECC staff must be able to use this menu.

Key The user must hold the BPSMENU and BPS MANAGER keys to view the Pharmacy ECME Manager Menu option.

MGR Pharmacy ECME Manager Menu…

> MNT ECME transaction maintenance options…

> UNS View / Unstrand Submissions Not Completed

> ROC Re Open CLOSED Claim

> SET Pharmacy ECME Setup Menu…

> BAS Edit Basic ECME Parameters

> PHAR Edit ECME Pharmacy Data

> REG Register Pharmacy with Austin Automation Center

> STAT Statistics Screen

## Pharmacy Electronic Claims Reports Menu Structure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Pharmacy Electronic Claims Reports* menu option structure is listed below. OPECCs and Pharmacy staff involved with the ePharmacy process must be able to access this menu.

Key The user must hold the BPSMENU and BPS REPORT keys to view the Pharmacy Electronic Claims Reports option. The OPECC Productivity Report will only display if the user holds the BPS SUPERVISOR KEY.

RPT Pharmacy Electronic Claims Reports…

> CLA Claim Results and Status…

> PAY Payable Claims Report

> REJ Rejected Claims Report

> ECMP CMOP / ECME Activity Report

> REV Reversal Clams Report

> NYR Claims Submitted, Not Yet Released

> REC Recent Transactions

> DAY Totals by Date

> CLO Closed Claims Report

> NBS Non-Billable Status Report

> SPA Spending Account Report

> OTH Other Reports…

> CRI ECME Claims-Response Inquiry

> PAY Payer Sheet Detail Report

> PHAR ECME Setup - Pharmacies Report

> TAT Turn-around time statistics

> VER View ePharmacy Rx

> OPR OPECC Productivity Report

# Accessing the ECME Main Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Electronic Claims Management Engine Main Menu option is usually accessed through the Core Applications Menu.

Key The user must hold the BPSMENU key to view the Electronic Claims Management Engine (ECME) Main Menu.

Example 4-1: Accessing the Electronic Claims Management Engine Main Menu

Select Core Applications Option: ?

Laboratory ...

PIMS MAS MANAGER ...

Mental Health ...

Military Retirees ...

Patient Data Log

Information Management Systems (SWIMS) ...

Voluntary Services' Menu ...

AR Finance AR Manager Menu ...

BPS ECME ...

EN Engineering Main Menu ...

FEE Fee Basis Main Menu ...

HL7 HL7 Main Menu ...

IB Integrated Billing Master Menu ...

NS Nursing System Manager's Menu ...

PSO Outpatient Pharmacy Manager ...

VOL Voluntary Service Master Menu ...

Select Core Applications Option: BPS ECME

# Accessing the ECME User Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *ECME User Screen* provides access to pharmacy claims that have been submitted electronically to third party payers / Pharmacy Benefit Managers (PBM). This option allows the user to review, close, reverse, or resubmit electronic claims.

From the ECME User Screen the user can access additional actions needed to process electronic pharmacy claims, including the Further Research action, which allows the user to research insurance, eligibility, and prescription information.

Key The user must hold the BPSMENU AND BPS USER key to view the ECME User Screen option.

This screen is accessed by selecting the U (ECME User Screen) option on the ECME Main Menu screen.

2.  The screen will display nothing the first time this menu option is entered. Select the Change View option, CV, as in section 5.1, and specify preferences to be displayed on the screen. The system will then default to these settings and display current information about active patients and prescriptions for the timeframe requested.

Example 5-1: Accessing the ECME User Screen Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Main Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

U ECME User Screen

COB ECME Pharmacy COB ...

MGR Pharmacy ECME Manager Menu ...

RPT Pharmacy Electronic Claims Reports ...

Select ECME Option: U ECME User Screen

Please wait...

Example 5-2: Displaying the ECME User Screen Option

PHARMACY ECME Jul 03, 2010@14:55:01 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,FIVE (XXXX) IBINSUR1/ VET Pb:0 Rj:1 AcRv:3 RjRv:0

1.1 COLCHICINE 0.6MG 00074-3781-01 06/24 101297\$ 1/000000001653 M RT DS/N

10/19/10 - Clarification Code 8 submitted.

(OPPUSER,TWO)

p-Reversal accepted

Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen//

This section diagrams and describes the different elements of the ECME User Screen.

Diagram 5-1: ECME User Screen Areas

PHARMACY ECME Jul 03, 2010@14:55:01 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/FILL/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,FIVE (XXXX) IBINSUR1/ Vet Pb:0 Rj:1 AcRv:3 RjRv:0

1.1 COLCHICINE 0.6MG 00074-3781-01 06/24 101297\$ 1/000000001653 M RT DS/N

10/19/10 - Clarification Code 8 submitted.

(OPPUSER,TWO)

p-Reversal accepted

Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen//

The table below describes the four areas of the ECME User Screen.

<table>
<caption><p><span id="_Toc72333927" class="anchor"></span>Table 3: Reject Codes</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3">Screen Area</th>
<th colspan="2">Description</th>
</tr>
<tr class="odd">
<th>#</th>
<th>Line Number. Sequential line number for each patient and associated prescription line(s).</th>
</tr>
<tr class="header">
<th><em>Patient Lines</em></th>
<th><p># PATIENT (Patient ID) INSURANCE/ EligIndicator SummaryStatus</p>
<p>ECMEPatient,FIVE (XXXX) IBINSUR1/ VET Pb:0 Rj:1 AcRv:3 RjRv:0</p>
<p>The first line is the Patient Summary Information line, which displays the patient’s name, (patient ID), insurance company and phone; eligibility indicator for the patient and insurance: VET = Veterans, TRI = TRICARE; CVA = CHAMPVA; claim progress status and a summary status of all claims submitted for this patient within the time frame requested in the ECME User Screen parameters. The codes for the summary status are as follows:</p>
<blockquote>
<p>Pb = Payable</p>
<p>Rj = Rejected</p>
<p>AcRv = Reversal Accepted</p>
<p>RjRv = Reversal Rejected</p>
<p>Example: VET Pb:17 Rj:4 AcRv:0 RjRv:0.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th></th>
<th><em>Claim/ Prescription Information Line</em></th>
<th><p>The Prescription line(s) follow the patient information lines sequentially. For each fill, an ECME claim is sent to the payer and each of these claims is displayed as a separate line on the User Screen (ECME User Screen).</p>
<p>Drug Name NDC DOS RX# Copay Refill/ECME# COLCHICINE 0.6MG 00074-3781-01 06/24 101297 $ 1 /000000001653</p>
<p>LOC /BillTYPE /RXStatus /Release Status</p>
<p>M/ RT/ DS /N</p>
<p>These show for each claim:</p>
<ul>
<li><p>Drug Name</p></li>
<li><p>NDC (National Drug Code)</p></li>
<li><p>Date of Service</p></li>
<li><p>Rx#</p></li>
<li><p>$ Patient Copay (if applicable)</p></li>
<li><p>Refill#</p></li>
<li><p>ECME#</p></li>
<li><p>Fill Location</p></li>
</ul>
<blockquote>
<p>C = Consolidated Mail Outpatient Pharmacy (CMOP)</p>
<p>M = LOCAL MAIL</p>
<p>W = WINDOW FILL</p>
</blockquote>
<ul>
<li><p>Bill Type</p></li>
</ul>
<blockquote>
<p>BB = Backbill</p>
<p>P2 = PRO option</p>
<p>RS = Resubmission</p>
<p>RT = Real Time Fill</p>
</blockquote>
<ul>
<li><p>RX Status</p></li>
</ul>
<blockquote>
<p>AC = Active</p>
<p>NV = Non-verified</p>
<p>HL = Hold</p>
<p>SU = Suspend</p>
<p>EX = Expired</p>
<p>DS = Discontinued</p>
<p>DL = Deleted</p>
<p>?? = Unknown</p>
</blockquote>
<ul>
<li><p>Release Status</p></li>
</ul>
<blockquote>
<p>N = Rx NOT Released</p>
<p>R = Rx Released</p>
</blockquote>
<ul>
<li><p>Coordination of Benefits Indicator</p></li>
</ul>
<blockquote>
<p>p- primary claim</p>
<p>s- secondary claim</p>
<p>s-Payable (p-Payable)</p>
</blockquote>
<p>The status is displayed only for those fill lines (claims) that represent the most recent fill. If there is more than one fill for the same prescription within the time frame requested in the ECME User Screen parameters, the previous fill/claim is indicated with "*" instead of Rx status, and the most current fill will display the RX status. If a fill has been created and put on suspense, the screen displays "*".</p></th>
</tr>
<tr class="header">
<th></th>
<th><em>User-Input Comments</em></th>
<th>The system allows the ECME user to enter comments for any claim displayed on the ECME User Screen. The most recent comment is displayed under the Prescription Information line. If a claim has been resubmitted since the most recent comment, a message displays in place of the most recent comment: “Prior comments suppressed – use CMT action for all comments”.</th>
</tr>
<tr class="odd">
<th></th>
<th><em>Payer Returned Responses</em></th>
<th><p>The Payer Returned Response information is displayed beneath the user-input comments or beneath the patient information line, if no comments were entered. Each response will begin on a separate line.</p>
<p>Valid payer-returned responses include Rejected (with a National Council for Prescription Drug Programs (NCPDP) rejection code described in the ePharmacy Rejects &amp; Resolutions Guide on the <a href="http://vaww.vistau.med.va.gov/vistau/e-bp/e-Pharm/default.htm">e-Pharmacy Training Home Page</a>, with additional lines of descriptive error messages), Payable, Reversal Accepted, Reversal Rejected, Stranded, Stranded reversal, Captured, Duplicate, Other, Cancelled, Corrupt, Unknown status and In Progress. If a claim is closed, “Closed” is added to the status, e.g., “Reversal accepted/Closed”.</p></th>
</tr>
<tr class="header">
<th>Message Window</th>
<th colspan="2">This section displays a plus (+) sign, minus (-) sign or informational text (i.e., Enter ?? for more actions). The plus and minus signs, entered at the action prompt, are used to jump forward or back a screen.</th>
</tr>
<tr class="odd">
<th>Action Area</th>
<th colspan="2">A list of <em>Claims Data Entry</em> options is available to you as described in Section 5 of this manual. A double question mark (<strong>??</strong>) may be entered at the "Select Action" prompt for a list of all List Manager options available.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Header Area</td>
<td colspan="2">Displays the date/time the screen was built, page status, selected division(s), user, and activity date range.</td>
</tr>
<tr class="even">
<td>Patient / Rx Area</td>
<td colspan="2">Displays information about the patient and prescription:</td>
</tr>
</tbody>
</table>

<span id="_Toc72333927" class="anchor"></span>Table 3: Reject Codes

3.  An option chosen at the patient information level is performed on all claim items for that patient.

The ECME User Screen also displays non-billable entries in addition to billable claims. TRICARE and CHAMPVA prescriptions with pseudo-rejection codes of eT and eC display with a few differences. The display for non-billable entries does not include date of service or an ECME number. Also, an open / closed indicator displays for each pseudo-rejection entry and the open / closed status is only for display purposes. The user can filter based on the status by using the Change View action.

The ECME User Screen has several actions to help navigate, as shown below. Actions are entered at the "Select Action" prompt by typing the synonym for the action (e.g., CV for Change View), the first unique letter(s) of the action name (e.g., CL for Close) or the full name of the action (e.g., Sort List for Sort List).

Example 5-2: List of all ECME User Screen Actions

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

List Manager provides generic actions applicable to List Manager Screens. A double question mark (??) may be entered at the "Select Action" prompt for a list of other actions available. Entering the synonym is the quickest way to select an action.

Example 5-3: Displaying List Manager Actions by Entering “??”

Select Action: Next Screen// ??

The following actions are also available:

\+ Next Screen

\- Previous Screen

UP Up a Line

DN Down a Line

\> Shift View to Right

\< Shift View to Left

FS First Screen

LS Last Screen

GO Go to Page

RD Re Display Screen

PS Print Screen

PL Print List

SL Search List

ADPL Auto Display(On/Off)

Q Quit

Press RETURN to continue or '^' to exit:

ROC Reopen Closed Claims

OCN Open/Close Non Billable Entry

DV Print Developer Claim Log

REJ OPECC Reject Information

RER Resubmit Claim w/o Reversal

EX Exit

LOG Print Claim Log

RED Resubmit Claim w/EDITS

UD Display Update

Enter RETURN to continue or '^' to exit:

The following actions are not available for non-billable entries:

REV Reverse Payable Claim

CLO Close Claim

LOG Print Claim Log

WRK Send to Worklist

ROC Reopen Closed Claims

RED Resubmit Claim w/EDITS

RER Resubmit Claim w/o Reversal

RH Release Copay (On FR Further Research)

After selecting an action, a prompt may display for the user to select an item from the ECME User screen.

- If the action requires the user to select a patient line, the system will default a value of 1 for the item prompt if there is only one patient displayed.
- If the action requires the user to select a claim line, the system will default a value of 1.1 for the prompt if there is only one claim displayed.

## Change View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Change View action allows the user to customize information displayed on the ECME User Screen.

The action is accessed by entering CV at the “Select Action:” prompt on the ECME User Screen. The system gives the user the option to “SAVE” these selections as a “preferred view.”

Example 5.1-1: Accessing the Change View Action

PHARMACY ECME Apr 26, 2006@11:44:45 Page: 1 of 2

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Patient Name

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

6 ECMEpatient,Two (XXXX) WEBMD TE/ VET Pb:1 Rj:0 AcRv:0 RjRv:1

6.1 FUROSEMIDE 10MG/M 00641-2312-25 04/18 100004065\$ 0/000000504691 W RT AC/R

p-Payable

6.2 CHOLESTYRAMINE 4G 00087-0580-01 04/19 100004066\$ 0/000000504692 W RT AC/R

p-Reversal rejected

NN:Transaction Rejected At Switch Or Intermediary

NC16-The clearinghouse did not reply in time.

7 ECMEpatient,One (XXXX) WEBMD TE/ VET ALL payable

7.1 ALBUTEROL INHALER 55555-4444-22 04/26 100003744\$ 0/000000504304 W RT AC/R

p-Payable

7.2 ACETYLCYSTEINE 20 00087-0570-09 04/21 100004054\$ 0/000000504677 W RT AC/N

p-Payable

8 ECMEpatient,Three (XXXX) WEBMD TE/ VET ALL payable

\+ Enter ?? for more actions

The screen has been updated on APR 26,2006@14:50:47. Press "Q" to quit.

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen//CV Change View

1.  View data by division(s) or all divisions.

Example 5.1-2: Selecting Views by Division

Select one of the following:

D DIVISION

A ALL

Select Certain Pharmacy (D)ivisions or (A)LL: A// DIVISION

Selected:

Select ECME Pharmacy Division(s): ANYTOWN

ANYTOWN

4.  View data by Eligibility Type of the claim.

Example 5.1-3: Selecting Views by Eligibility Type

Select one of the following:

V VETERAN

T TRICARE

C CHAMPVA

A ALL

Select One or Many Eligibility Types or (A)ll: A// ?

Enter a single response or multiple responses separated by commas.

Example:

T

T,C

5.  View data for one ECME user, many ECME users or all users. The ECME user is defined as the person who last processed / finished / resubmitted, etc., the prescription fill.

Example 5.1-4: Selecting Views from Entries by One User

Select one of the following:

U USER

A ALL

Display One or Many ECME (U)sers or (A)LL: A// USER

Enter a user to select.

Once all users are selected, hit enter without making a selection.

Select User: USER

1 ECMEuser,One UO PHARMACIST

2 ECMEuser,Two UTW PHARMACIST

3 ECMEuser,Three UTH PHARMACIST

CHOOSE 1-3: 1 ECMEuser,One UO PHARMACIST

Selected:

ECMEuser,One

Select User:

6.  View data from one patient, many patients, or all patients.

Example 5.1-5: Selecting Views from Entries for One Patient

Select one of the following:

P PATIENT

A ALL

Display One or Many (P)atients or (A)LL: A// PATIENT

Enter a patient to select.

Once all patients are selected, hit enter without making a selection.

Select Patient: ECMEpatient,ONE// ECME

1 ECMEpatient,One 1-1-65 666443333 NO NSC VETERAN

2 ECMEpatient,Two 1-1-65 666443444 NO NSC VETERAN

3 ECMEpatient,Three 1-1-68 666773333 YES SC VETERAN

ENTER '^' TO STOP, OR

CHOOSE 1-3: 2 ECMEpatient,Two 1-1-65 666443444 NO NSC VETERAN

Enrollment Priority: GROUP 8g Category: NOT ENROLLED End Date: 08/01/2005

Selected:

ECMEpatient,Two

Select Patient:

4.  If selecting one or many patients, data may be viewed for up to 366 days. If selecting all patients, data may be viewed for up to 180 days.
7.  View data about one prescription, many prescriptions, or all prescriptions.

Example 5.1-6: Selecting Views from Entries for One Prescription

Select one of the following:

R RX

A ALL

Display One or Many (R)x or (A)LL: A// RRX

Enter a prescription to select.

Once all prescriptions are selected, hit enter without making a selection.

Select RX: 123456

Selected:

123456

Select RX:

8.  Choose data for a date range or timeframe of days or hours.

Example 5.1-7: Selecting Views by Timeframe of the Default of Days

Select one of the following:

D Date Range

T Timeframe

Display Activity (D)ate Range or (T)imeframe: T// ?

Date Range will allow a user to specify an activity beginning and ending date.

Timeframe will allow a user to specify the activity by days or hours.

Select one of the following:

D Date Range

T Timeframe

Display Activity (D)ate Range or (T)imeframe: Date Range

5.  If selecting one or many patients, data may be viewed for up to 366 days. If selecting all patients, data may be viewed for up to 180 days.
9.  (IF BY DATE RANGE) Choose a beginning and ending date.

Example 5.1-8: Selecting Views by Date Range

Display Activity (D)ate Range or (T)imeframe: T// d Date Range

Activity Beginning Date: T (JAN 11,2008)

Activity Ending Date: ?

Enter a date which is no more than 180 days after the Beginning Date.

Activity Ending Date:

10. (IF BY TIMEFRAME) Choose data for a period of days or hours.

Example 5.1-9: Selecting Views by Timeframe of the Default of Days

Select one of the following:

D DAYS

H HOURS

Activity Timeframe (H)ours or (D)ays: D// \<Enter\> AYS

11. (IF BY TIMEFRAME) Enter a number for the timeframe value for the number of days, or number of hours, to view.

Example 5.1-10: Selecting Views by Timeframe Number of Days or Hours

Activity Timeframe Value: (1-180): 40// 10

12. Choose which types of claims will display on the User Screen.

Example 5.1-11: Selecting Types of Claims

Select one of the following:

O OPEN CLAIMS

C CLOSED CLAIMS

A ALL

Select Open/Closed or All Claims: A// \<Enter\> LL

13. Choose which types of non-billable entries will display on the User Screen.

Example 5.1-12: Selecting Types of Entries

Select one of the following:

O Open Non-Billable Entries

C Closed Non-Billable Entries

A ALL

Please note this question only applies to

TRICARE or CHAMPVA Non-Billable Entries.

Display (O)pen or (C)losed or (A)ll Non-Billable Entries: A//

14. Choose which types of payer requests will display on the User Screen.

Example 5.1-13: Selecting Types of Requests

Select one of the following:

B BILLING REQUESTS

R REVERSALS

A ALL

Select Submission Type: A// \<Enter\> LL

15. View rejected claims, payable claims, or all claims.

Example 5.1-14: Selecting Views of Claim Status

Select one of the following:

R REJECTS

P PAYABLES

U UNSTRANDED

A ALL

Display (R)ejects or (P)ayables or (U)nstranded or (A)LL: A//?

Enter a single response or multiple responses separated by commas.

Example:

P

P,R

16. View released claims, non-released claims, or all claims.

Example 5.1-15: Selecting Views of Released Claims

Select one of the following:

R RELEASED

N NON-RELEASED

A ALL

Display (R)eleased Rxs or (N)on-Released Rxs or (A)LL: A// RELEASED

17. View CMOP, Mail, Window, or all claims.

Example 5.1-16: Selecting Views of CMOP Claims

Select one of the following:

C CMOP

M MAIL

W WINDOW

A ALL

Display (C)MOP or (M)ail or (W)indow or (A)LL: A// ?

Enter a single response or multiple responses separated by commas.

Example:

C

C,M

18. View real time, back bills, bills processed with the PRO option, resubmissions (please see [Section 6.3](#process-secondary-tricare-rx-to-ecme)), or all claims.

Example 5.1-17: Selecting Views of Bill Types

Select one of the following:

R REALTIME

B BACKBILLS

P PRO OPTION

S RESUBMISSION

A ALL

Display (R)ealTime, (B)ackbills, (P)RO Option, Re(S)ubmission or (A)ll: A// ?

Enter a single response or multiple responses separated by commas.

Example:

B

B,P

19. View one reject code, multiple reject codes or all reject codes if the option “REJECTS” was chosen for types of claims to view in (G) Rejected Claims, above. When selecting reject Code, the prompt continues to repeat until the user presses ‘Enter’ without a response.

Example 5.1-18: Selecting Views of One Reject Code

Select one of the following:

R REJECT CODE

A ALL

Display Specific (R)eject Code or (A)LL: A// REJECT CODE

Select Reject Code: 29 M/I Number Refills Authorized

Selected:

29 M/I Number Refills Authorized

Select Reject Code:

20. View data for a specific insurance company or all insurance companies.

Example 5.1-19: Selecting Views by a Specific Insurance Company

Select one of the following:

I SPECIFIC INSURANCE(S)

A ALL

Select Certain (I)NSURANCE or (A)LL): I// \<Enter\> SPECIFIC INSURANCE(S)

Selected: OPINSUR2

Select INSURANCE: DEVELOPMENT INS 123 HERE STREET ANYTOWN

CALIFORNIA Y

Selected: DEVELOPMENT INS

OPINSUR2

Select INSURANCE: OPINSUR2 25 INS WAY ANYTOWN ST Y

Select one of the following:

Y YES

N NO

Delete OPINSUR2 from your list?: NO// y YES

Selected: DEVELOPMENT INS

Select INSURANCE:

21. Answer Y or N to keep the *Change View* action selections as the preferred view. If Y is entered, the preferred view is stored in ECME for use when the user enters the ECME User Screen. If N is entered, the display will only show the selected views until the user quits the ECME User Screen or uses the *Change View* action again.

Example 5.1-20: Entering “Y” to Save Selections as User’s Preferred View

DO YOU WANT TO SAVE THIS VIEW AS YOUR PREFERRED VIEW (Y/N)?: YES

Updating screen...

22. If a user accesses *Change View* and they are not currently viewing the saved preferred view, the user is asked if they want to Restore the Preferred View. The user must answer Y or N when asked to restore the preferred view.
1.  A response of Y will automatically restore the view of the ECME User Screen to the previously saved view without the user answering all the Change View filters.
2.  A response of N will prompt the user with all the Change View filters.

Example 5.1-21: Entering “Y” to Restore User’s Preferred View

Restore your Preferred View and exit Change View (Y/N)? Y//

Updating screen...

## Sort List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Sort List* screen action allows the user to customize the sort order of data displayed on the ECME User Screen.

Sort Order (Defaults):

T – Transaction Date / Time (descending)

D – Division (ascending)

I – Insurance Company (ascending)

C – Reject Code (ascending)

P – Patient Name (ascending)

N – Drug Name (ascending)

B – Bill Type \[BB / P2 / RT\] (ascending)

L – Fill Location (ascending)

R – Released / Non-Release (ascending)

A – Active / Discontinued Rx (ascending)

6.  Transaction Date / Time (descending) is the secondary sort for ALL primary sort selections. Sorting is by PATIENTS (not claims), based on the date / time of their most recent transaction

Access this action by entering SO at the “Select Action:” prompt on the ECME User Screen. The system will give the option to “SAVE” these selections as the User’s “Preferred View.”

Example 5.2-1: Accessing the Sort List Option

PHARMACY ECME Apr 30, 2005@09:10:18 Page:1 of 2

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Patient Name

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

6 ECMEpatient,Two (XXXX) WEBMD / \*89%\* Pb:5 Rj:0 AcRv:0 RjRv:0

6.1 FUROSEMIDE 10MG/M 00641-2312-25 04/21 100004065\$ 0/000000504691 W RT AC/R

p-Payable

6.2 CHOLESTYRAMINE 4G 00087-0580-01 04/21 100004066\$ 0/000000504692 W RT AC/R

p-Reversal rejected

NN:Transaction Rejected At Switch Or Intermediary

NC16-The clearinghouse did not reply in time.

7 ECMEpatient,One (XXXX) WEBMD TE/ VET ALL payable

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen//SO Sort List

Example 5.2-2: Choosing Patient as the User’s Sort Preference

Select one of the following:

T TRANSACTION DATE

D DIVISION

I INSURANCE

C REJECT CODE

P PATIENT NAME

N DRUG NAME

B BILL TYPE (BB/P2/RT)

L FILL LOCATION

R RELEASED/NON-RELEASED

A ACTIVE/DISCONTINUED

ENTER SORT TYPE: P// PATIENT NAME

Example 5.2-3: Choosing User’s Sort Preference as the Preferred View

Select one of the following:

Y YES

N NO

DO YOU WANT TO SAVE THIS VIEW AS YOUR PREFERRED VIEW (Y/N)?: YES

Updating screen...

## Reverse Payable Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Reverse Payable Claim* action allows a user to submit a claim reversal request to the insurer for a claim that was returned as “Payable” or “Reversal Rejected.” A primary claim cannot be reversed if there is a payable secondary claim. The secondary claim must be reversed before the primary claim can be reversed.

Claims that have been closed will be displayed with “/Closed” after the status. Closed claims cannot be reversed until they are first reopened. If the user attempts to reverse a claim that is closed, a message is displayed that the claim “is Closed and cannot be Reversed. Reopen the claim and try again.”

Access the action by entering REV at the “Select Action:” prompt on the ECME User Screen.

Example 5.3-1: Accessing and Executing the Reverse Payable Claim Action

PHARMACY ECME Aug 10, 2005@10:31:22 Page: 18 of 42

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Patient Name

+# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

7 ECMEpatient,One (XXXX) WEBMD TE/ VET ALL payable

7.1 ALBUTEROL INHALER 55555-4444-22 08/08 100003744\$ 0/000000504304 W RT AC/R

p-Payable

7.2 ACETYLCYSTEINE 20 00087-0570-09 08/01 100004054\$ 0/000000504677 W RT AC/N

p-Payable

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen// REV Reverse Payable Claim

1.  The user will see the following message if there is an attempt to reverse a primary claim when there is a payable secondary claim.

Example 5.3-2: Entering the Line Item for a Claim with a Payable Secondary Claim

1.12 FLURAZEPAM 15MG C 00140-0065-14 03/04 102322\$ 2/000000113596 W RT AC/R

cannot be Reversed if the secondary claim is payable.

Please reverse the secondary claim first.

2.  The user is prompted for the line item of the payable claim to be reversed. Remember, if the user enters the patient line number, a claim reverse request will be created for all the payable claims for that patient.

Example 5.3-3: Entering the Line Item for the Claim Reversal Request

Enter the line numbers for the Payable claim(s) to be Reversed.

Select: 7.1

3.  The selected line item is redisplayed, and the user is required to enter text to explain the reversal reason.

Example 5.3-4: Typing Text for Required Reversal Reason

You've chosen to REVERSE the following prescription for ECMEpatient,Six

7.1 ALBUTEROL INHALER 55555-4444-22 02/28 100003744\$ 0/000000504304 W RT AC/R

Enter REQUIRED REVERSAL REASON: RX IS FOR SC CONDITION

This response must have at least 0 characters and no more

than 60 characters and must not contain embedded uparrow

2.  The system asks if you are sure you want to continue with the transaction. The user can answer Y or N. If the user types in Y, the claim reversal request is submitted.

Example 5.3-5: Entering “Y” to Continue Claim Reversal Request

Enter REQUIRED REVERSAL REASON: Drug is only billable through CMOP

Are you sure?(Y/N)? YES

4.  The system asks if want to mark the claim as non-billable in Claims Tracking, and therefore release the patient copay (if any). Enter Y or N. If the user enters Y, it will prompt for a Claims Tracking Non-Billable Reason and a Comment. If the reversal is accepted by the payer, the ECME claim will be closed and a close event will then be sent to IB with the non-billable reason and comment provided by the user. IB should mark the episode as non-billable and release the first-party copay.

Example 5.3-6: Entering “Y” to Mark the Claim as Non-billable

Do you want to mark the claim as non-billable in Claims Tracking and release the Patient Copay (if any) (Yes/No)? No//Yes

Select CLAIMS TRACKING NON-BILLABLE REASONS NAME: ??

Choose from:

1 NOT INSURED

2 SC TREATMENT

3 AGENT ORANGE

4 IONIZING RADIATION

5 SOUTHWEST ASIA

7 COVERAGE CANCELED

10 INVALID PRESCRIPTION ENTRY

12 PRESCRIPTION DELETED

13 PRESCRIPTION NOT RELEASED

14 DRUG NOT BILLABLE

21 MILITARY SEXUAL TRAUMA

29 HEAD/NECK CANCER

30 COMBAT VETERAN

33 90 DAY RX FILL NOT COVERED

34 NOT A CONTRACTED PROVIDER

35 INVALID MULTIPLES PER DAY SUPP

36 REFILL TOO SOON

37 INVALID NDC FROM CMOP

38 PROJECT 112/SHAD

39 NON COVERED DRUG PER PLAN

40 FILING TIMEFRAME NOT MET

61 NO PHARMACY COVERAGE

85 NPI/TAXONOMY ISSUES

86 RX DUR REJECT

87 RX PRIOR AUTH NOT OBTAINED

88 RX MEDICARE PART D

89 RX DISCOUNT CARD

91 DATE OF BIRTH MISMATCH

999 OTHER

Select CLAIMS TRACKING NON-BILLABLE REASONS NAME: 2 SC TREATMENT

Comment : RX IS FOR SC CONDITION

Are you sure (Y/N)? YES

If the reversal is approved by the third-party payer, the claim will be marked as non-billable.

5.  The system submits a claim reversal request to the payer for each selected claim.

Example 5.3-7: Claim Reversal Request is Submitted

Processing Primary claim...

Claim Status:

Reversing...

IN PROGRESS-Building the transaction

IN PROGRESS-Transmitting

IN PROGRESS-Parsing response

E REVERSAL ACCEPTED

Reversal Accepted

1 claim reversal submitted.

Enter RETURN to continue or '^' to exit:

6.  The payer will either “Accept” or “Reject” the claim reversal request. The payer return status is displayed on the Payer Returned Response line.

Example 5.3-8: Accepted Payable Claim Reversal Request

PHARMACY ECME Aug 10, 2005@10:31:22 Page: 18 of 42

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past XX day(s)

Sorted by: Patient Name

+# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

7 ECMEPatient,Six (XXXX) WEBMD TE/ VET ALL payable

7.1 ALBUTEROL INHALER 55555-4444-22 02/28 100003744\$ 0/000000504304 W RT DS/R

p-Reversal Accepted

## Resubmit Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Resubmit Claim action sends a claim reversal request to the insurer, followed by a new claim for the same *prescription*, with the new or updated data for these conditions:

- If the claim was initially returned as “Payable,” the system sends a claim reversal request.
- If the payer “Accepts” the reversal request, the claim resubmission is sent.
- If the payer “Rejects” the reversal request, the claim is NOT resubmitted.
- If the claim was initially returned as “Rejected” or non-billable, the system immediately sends the claim submission to the payer and the reversal request is NOT sent.

The Resubmit action is accessed by entering RES at the “Select Action:” prompt on the ECME User Screen.

Example 5.6-1: Accessing and Executing the Resubmit Claim Action

PHARMACY ECME Jul 22, 2008@14:41:55 Page: 1 of 29

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction Date

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# LOC/TYP RXINF

1 ECMEpatient,One (XXXX) OPINSUR1/ VET Pb:2 Rj:4 AcRv:4 RjRv:0

1.1 RESERPINE 0.1MG S 00083-0035-40 07/19 100598\$ 1/000000000520 W RT AC/N

p-In progress- Waiting to start

1.2 LIDOCAINE 0.5% W/ 00186-0140-01 07/19 100704\$ 1/000000000623 W RT AC/N

p-In progress- Transmitting

1.3 IMIPRAMINE 25MG T 00779-0588-30 07/19 100820\$ 1/000000000740 W RT \*\*/N

p-Rejected

07:M/I Cardholder ID

1.4 FLURAZEPAM 15MG C 00781-2806-05 07/18 100948\$ 0/000000000870 W RT \*\*/N

p-Rejected

07:M/I Cardholder ID

1.5 DACARBAZINE 100MG 00026-8151-10 07/21 100958\$ 2/000000000880 W RT \*\*/N

p-Reversal accepted

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen// res Resubmit Claim

1.  The user is prompted for the line item(s) of the claim to be resubmitted.
7.  The user can also submit multiple line items separated by commas (e.g., “1.1,1.2”), or a range of line items separated by a hyphen (e.g., “1.1-1.3”).

Example 5.4-2: Entering the Line Item for the Claim Resubmission Request

Enter the line numbers for the claim(s) to be resubmitted.

Select item(s): 1.5

Claims that have been closed will be displayed with “/Closed” after the status. [Closed claims cannot be resubmitted until they are reopened.](#reopen-closed-claims-hidden-action) If the user attempts to resubmit a claim that is closed, a message will display that the user cannot resubmit.

Example 5.4-3: Resubmitting a Closed Claim

You've chosen to RESUBMIT the following prescription

1.2 AMITRIPTYLINE HCL 00603-2212-32 10/11 2056098 0/000001616051 M RT DS/N

Are you sure?(Y/N)? y YES

\>\> Cannot Resubmit

1.2 AMITRIPTYLINE HCL 00603-2212-32 10/11 2056098 0/000001616051 M RT DS/N

because the claim is Closed. Reopen the claim and try again.

0 claims have been resubmitted.

The primary claim cannot be resubmitted if there is a payable secondary claim. In these cases, the user must reverse the secondary claim.

If the user attempts to resubmit a primary claim when there is a payable secondary claim, a message will display, which will discontinue the claims resubmission process.

Example 5.4-4: Entering the Line Item for a Claim that has a Payable Secondary Claim

The claim:

1.12 FLURAZEPAM 15MG C 00140-0065-14 03/04 102322\$ 2/000000113596 W RT AC/R

cannot be Resubmitted if the secondary claim is payable.

Please reverse the secondary claim first.

2.  Otherwise, the system redisplays the line item for resubmission, then asks if are sure you want to continue with the transaction. Enter Y or N. If Y, the claim resubmission process continues.

Example 5.4-5: Entering “Y” to Continue Claim Resubmission Request

You've chosen to RESUBMIT the following prescription for ECMEpatient,One

100MG 00026-8151-10 06/26 100958\$ 2/000000000880 W RT \*\*/N

Are you sure?(Y/N)? y YES

23. ECME will allow multiple submissions of the same prescription and fill to be placed on the request queue at the same time. The ECME engine will process all requests in the order that they are received.
8.  Even though a request may be placed on the queue, whether it is processed will depend on the outcome of the previous request.

For instance, if there are two entries on the queue and the second is requesting a reversal, it may not be processed if the previous request comes back with an E REVERSAL ACCEPTED status. If there is already a submission in the queue for this prescription and fill, a message is displayed and asks to proceed.

Example 5.4-6: Entering “Y” to Place Multiple Submissions in the Queue

The claim is in progress. The request will be scheduled and processed after the previous request(s) are completed. Please be aware that the result of the resubmit depends on the payer's response to the prior incomplete requests.

Do you want to proceed?(Y/N)? y YES

24. The claim resubmission request is submitted, and the progress is displayed.

Example 5.4-7: Displaying a Successfully Resubmitted Claim

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Building the claim

IN PROGRESS-Transmitting

E PAYABLE

Veteran Prescription 100958 successfully submitted to ECME for claim generation.

1 claim has been resubmitted.

Enter RETURN to continue or '^' to exit: \<ENTER\>

Updating screen for resubmitted claims...

25. The line item will display the status of a claim that was resubmitted and the Bill Type indicator of “RS.” The “RS” indicates a resubmitted claim. The resubmit indicator will also display for a non-billable prescription that has been resubmitted, even if there is no claim because the prescription remained non-billable.

Example 5.4-8: Displaying the Claim Status after a Resubmission

PHARMACY ECME Jul 12, 2008@14:42:46 Page: 1 of 29

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction Date

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# LOC/TYP RXINF

1 ECMEpatient,One (XXXX) OPINSUR1/ VET Pb:2 Rj:4 AcRv:4 RjRv:0

1.1 RESERPINE 0.1MG S 00083-0035-40 07/09 100598\$ 1/000000000520 W RT AC/N

p-In progress- Waiting to start

1.2 LIDOCAINE 0.5% W/ 00186-0140-01 07/09 100704\$ 1/000000000623 W RT AC/N

p-In progress- Waiting to start

1.3 IMIPRAMINE 25MG T 00779-0588-30 07/09 100820\$ 1/000000000740 W RT \*\*/N

p-Rejected

07:M/I Cardholder ID

1.4 FLURAZEPAM 15MG C 00781-2806-05 07/08 100948\$ 0/000000000870 W RT \*\*/N

p-Rejected

07:M/I Cardholder ID

1.5 DACARBAZINE 100MG 00026-8151-10 07/06 100958\$ 2/000000000880 W RS \*\*/N

p-Payable

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen//

## Close Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action allows the user to close claims that were initially returned as “Rejected”, and reversals that were “Released and Accepted.”

Claims that have already been closed are displayed with “/Closed” after the status. If the user attempts to close a claim that is already closed, the following message is displayed, “This claim is already closed.”

The Close Claim action will prevent a claim from being closed if it is currently open on the Pharmacy Worklist. If the user attempts to close a claim that is open in the Pharmacy Worklist, a message will be displayed that the claim cannot be closed because it is open in the Pharmacy Worklist.

PHARMACY ECME Jul 15, 2014@18:43:02 Page: 1 of 1

SELECTED DIVISION(S): GENERIC CITY

Transmitted by Transmitter, Person Activity Date Range: within the past 365 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1

1.1 ABACAVIR SULFATE 00173066101 07/15 \#######0/00000###7412 M RT SU/N

07/15/14 - IGNORED - test of cmop

p-Rejected

NN:Transaction Rejected At Switch Or Intermediary

NC16-The clearinghouse did not reply in time.

Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Quit//CLO

Enter the line numbers for the claim(s) to be closed.

Select item(s): 1.1

You've chosen to close the following prescription(s) for

Oppatient,ONE :

1.1 ABACAVIR SULFATE 00173066101 07/15 \#######0/00000###7412 M RT SU/N

NN:Transaction Rejected At Switch Or Intermediary

NC16-The clearinghouse did not reply in time.

ALL Selected Rxs will be CLOSED using the same information gathered in the

following prompts.

Are you sure?(Y/N)? y YES

The Prescription is currently open in the pharmacist’s Third Party Payer Reject Worklist. The claim cannot be closed until action is taken by the pharmacist.

PHARMACY ECME Jul 15, 2014@18:43:02 Page: 1 of 1

SELECTED DIVISION(S): GENERIC CITY

Transmitted by Transmitter, Person Activity Date Range: within the past 365 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1

1.1 ABACAVIR SULFATE 00173066101 07/15 \#######0/00000###7412 M RT SU/N

07/15/14 - IGNORED - test of cmop

p-Rejected

NN:Transaction Rejected At Switch Or Intermediary

NC16-The clearinghouse did not reply in time.

Enter ?? for more actions

CU Continuous Update REV Reverse Payable Claim FR Further Research

UD Display Update RES Resubmit Claim LOG Print Claim Log

CV Change View CLO Close Claim WRK Send to Worklist

SO Sort List CMT Add/View Comments EX Exit

Select Action: Quit//

The CLOSE action cannot be applied to the secondary claim if the primary claim has already been closed. The secondary claim is considered closed when the primary claim is closed.

1.  This action is accessed by entering CLO at the “Select Action:” prompt on the ECME User Screen. The system prompts the user for the line number(s) for the claim(s) being closed.

Example 5.5-1: Entering a Prescription Line Item to Close One Rejected Claim

PHARMACY ECME Aug 02, 2005@12:19 Page: 1 of 70

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Patient Name

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

7 ECMEpatient,Two (XXXX) WEBMD / VET Pb:3 Rj:1 AcRv:0 RjRv:0

7.1 DESIPRAMINE 25MG T 00068-0011-10 08/02 100003962\$ 0/000000504559 W RT \*\*/N

p-Rejected

07:M/I Cardholder ID Number

22:M/I Dispense As Written(DAW)/Product Selection Code

34:M/I Submission Clarification Code

7.2 CODEINE SULFATE 30 00002-1010-02 08/02 10082\$ 0/000000504561 W RT EX/N

p-Rejected

07:M/I Cardholder ID Number

23:M/I Ingredient Cost Submitted

8 ECMEpatient,Two (XXXX) WEBMD / VET ALL payable

8.1 TESTOSTERONE ENTH. 00003-0328-40 07/30 909238\$ 0/000001105472 M RT AC/N

p-Payable

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Line Item(s): Next Screen// CLO Close Claim

Enter the line numbers for the claim(s) to be closed.

Select Line Item(s): 7.1

26. The system redisplays the selected line item(s), then notes that all prescription line items for patient line items will be closed using the same information entered into the non-billable reasons name prompt. The user is asked to continue.

Example 5.5-2: Entering “Y” to Continue Close Claim Request

You've chosen to close the following prescription(s) for

ECMEpatient,Two:

7.1 DESIPRAMINE 25MG T 00068-0011-10 03/20 100003962\$ 0/000000504559 W RT \*\*/N

07:M/I Cardholder ID Number

22:M/I Dispense As Written(DAW)/Product Selection Code

34:M/I Submission Clarification Code

ALL Selected Rxs will be CLOSED using the same information gathered in the following prompts.

Are you sure?(Y/N)? YES

27. The user is prompted for a non-billable reason code.

Example 5.5-3: Listing Non-Billable Reason Codes

PHARMACY ECME Aug 12, 2005@12:19 Page: 1 of 70

Select CLAIMS TRACKING NON-BILLABLE REASONS NAME: ??

Choose from:

1 NOT INSURED

2 SC TREATMENT

3 AGENT ORANGE

4 IONIZING RADIATION

5 SOUTHWEST ASIA

7 COVERAGE CANCELED

10 INVALID PRESCRIPTION ENTRY

12 PRESCRIPTION DELETED

13 PRESCRIPTION NOT RELEASED

14 DRUG NOT BILLABLE

21 MILITARY SEXUAL TRAUMA

29 HEAD/NECK CANCER

30 COMBAT VETERAN

33 90 DAY RX FILL NOT COVERED

34 NOT A CONTRACTED PROVIDER

35 INVALID MULTIPLES PER DAY SUPP

36 REFILL TOO SOON

37 INVALID NDC FROM CMOP

38 PROJECT 112/SHAD

39 NON COVERED DRUG PER PLAN

40 FILING TIMEFRAME NOT MET

61 NO PHARMACY COVERAGE

85 NPI/TAXONOMY ISSUES

86 RX DUR REJECT

87 RX PRIOR AUTH NOT OBTAINED

88 RX MEDICARE PART D

89 RX DISCOUNT CARD

91 DATE OF BIRTH MISMATCH

999 OTHER

Select CLAIMS TRACKING NON-BILLABLE REASONS NAME: 61 NO PHARMACY COVERAGE

28. The user is prompted for a comment (explanation), and again whether you want to continue.

Example 5.5-4: Entering a Comment and Answering, ‘Are You Sure?’ Question

Comment : ECME Reject: Insurance does not cover Rxs

Are you sure?(Y/N)? YES

Closing Claim VA2006=1712884=000010=0006693...OK

1 claim has been closed.

Enter RETURN to continue or '^' to exit: \<Enter\>

Updating screen for closed claims...

### Variations to the Close Claim Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the Non-Billable Reason selected is “OTHER,” the system will prompt with two choices: ”NON-BILLABLE” or “DROP TO PAPER.”

- If the user selects (N)ON-BILLABLE EPISODE, the Claims Tracking entry displays the Billable Episode flag = “N” with the Non-Billable Reason selected.
9.  The Billable Episode flag will be changed back to "Y" if a secondary claim is later generated and is returned as payable.
- If the user selects (D)ROP TO PAPER, the system stores the selected Non-Billable Reason in the Close Claim Comments, updates the Claims Tracking entry to display the Billable Episode flag = “Y”, creates the next bill date as T+1 and stores Claims Tracking comments including the initial Non-billable Reason. The next scheduled billing run will pick up this bill if the prescription has been released.

Example 5.5.1-1: Closing a Prescription

You've chosen to close the following prescription(s) for

ECMEPatient,FIVE :

4.1 COLCHICINE 0.6MG 00074378101 06/24 101297\$ 1/000000001653 M RT DS/N

ALL Selected Rxs will be CLOSED using the same information gathered in the

following prompts.

Are you sure?(Y/N)? YES

Select CLAIMS TRACKING NON-BILLABLE REASONS NAME: OTHER

Select one of the following:

N NON-BILLABLE

D DROP TO PAPER

Treat as (N)on-Billable Episode or (D)rop Bill to Paper?: NON-BILLABLE

Comment : Insurance does not cover Rxs

Release Patient CoPay(Y/N)? YES

Are you sure?(Y/N)? NO

Example 5.5.1-2: Entering Non-Billable Episode for Reason Code 31

Select CLAIMS TRACKING NON-BILLABLE REASONS NAME: 31 90 DAY RX FILL NOT COVERED

Select one of the following:

N NON-BILLABLE

D DROP TO PAPER

Treat as (N)on-Billable Episode or (D)rop Bill to Paper?: Select: N Non-billable

1.  The application will prompt the user for a comment. The text can be up to 40 characters and must not contain any embedded up-arrows (^).

Example 5.5.1-3: Entering a Comment

Comment : ECME Reject: Plan does not cover 90-day fills

29. The user can enter Y or N to choose to continue the close claim request or not.

Example 5.5.1-4: Entering “Y” to Continue Close Claim Request

Are you sure?(Y/N)? Y YES

30. If the Rx# display is followed by a “\$”, the ECME user is given the following prompt to answer whether the patient copay can be released also or not. If Y is selected, the patient copay bill will be automatically removed from hold status for ALL selected claims.

Example 5.5.1-5: Releasing Patient Copay

Release Patient CoPay(Y/N)? Y YES

31. When the claim is successfully closed, the display shows that the transaction went through “OK” and states that the claim was closed.

Example 5.5.1-6: Displaying System Closing the Claim

Closing Claim VA2005-1111111-123456-0000501...OK

1 claim has been closed.

Enter RETURN to continue or '^' to exit:/ \<Enter\>

Updating screen for closed claims...

32. The closed claim transaction may no longer be displayed with the patient’s other prescription line items depending on the filters set in Change View. The system will notify Integrated Billing of the closed claim so that Claims Tracking can be updated.

Example 5.5.1-7: Closed Item is No Longer Displayed

PHARMACY ECME Aug 12, 2005@13:13:15 Page: 1 of 69

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Patient Name

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

7 ECMEpatient,Two (XXXX) WEBMD / VET Pb:3 Rj:1 AcRv:0 RjRv:0

7.1 CODEINE SULFATE 30 00002-1010-02 08/03 10082\$ 0/000000504561 W RT EX/N

p-Rejected

07:M/I Cardholder ID Number

23:M/I Ingredient Cost Submitted

8 ECMEpatient, Three (XXXX) WEBMD / VET ALL payable

8.1 TESTOSTERONE ENTH. 00003-0328-40 08/03 909238\$ 0/000001105472 M RT AC/N

p-Payable

9 ECMEpatient,22 (XXXX) WEBMD / VET ALL payable

9.1 HYDROCODONE 5/ACET 55778-8998-88 08/12 909254\$ 1/000001105496 C RT AC/N

\+ Enter ?? for more actions

### Special Notes Regarding Secondary Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a primary claim is successfully closed and there is secondary insurance for that claim, a secondary insurance notification is displayed so that the user will know to bill the secondary payer.

Example 5.5.2-1: Secondary Insurance Notification

This patient has ADDITIONAL insurance with Rx Coverage that may be used to bill this claim. The system will change the CT entry to a NON-BILLABLE Episode. If appropriate, please go to the ECME Pharmacy COB menu and use the PRO - Process Secondary/TRICARE Rx to ECME option to create an ePharmacy secondary claim.

Patient: ECMEpatient,One

Date of service: JUN 29, 2010

Insurance: ECMEInsurance,One

Group number: 10001

BISOPROLOL 2.5MG/ 51285-0047-02 06/29 2055810\$ 0/000001615758 W RT AC/R

Do you want to print the information (above) concerning additional insurance?

(Y/N)? n NO

## Add / View Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system allows the ECME user to enter comments for any claim displayed on the ECME User Screen. There are two types of comments that can be added: OPECC Comments and Pharmacy / OPECC Comments. More details are in paragraph B. below. The most recent comment will be displayed under the Prescription Information line. If a claim has been resubmitted, a message displays in place of the most recent comment: “Prior comments suppressed – use CMT action for all comments.” The message indicating the prior comments were suppressed is not captured in CMT Add / View Comments.

1.  Access this action by entering CMT at the “Select Action:” prompt on the ECME User Screen. The system prompts the user for a line selection to identify the line item(s) to contain a comment. The user can select more than one claim to add the same comment to or can select the patient summary line to add the same comment to all claims that are listed under this patient.

Example 5.6-1: Entering a Prescription Line Item to Add a Comment

PHARMACY ECME Jul 02, 2005@22:19 Page: 1 of 70

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Patient Name

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

1 ECMEpatient,Two (XXXX) WEBMD / VET Pb:3 Rj:1 AcRv:0 RjRv:0

1.1 TAMOXIFEN CITRATE 00093-0784-86 07/01 909392\$ 0/000001105634 W \*\* DS/R

p-Rejected

NN:Transaction Rejected At Switch Or Intermediary

NC40-Request from an unknown site. Registration is required

1.2 DESIPRAMINE HCL 25 00068-0011-10 07/01 909393\$ 0/000001105635 W \*\* AC/R

p-Payable

1.3 DIAZEPAM 5MG/ML IN 00140-1933-06 07/01 909394\$ 0/000001105636 W \*\* AC/N

p-Payable

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen// CMT Add/View Comments

Enter the line number for which you wish to Add/View comments.

Select: 1.2

33. The Add / View Comments list manager screen displays with multiple actions. Both comment actions allow the user to enter a comment for display on the ECME User Screen; however, the action to Add Pharmacy / OPECC Comment also displays the comment on the Outpatient Pharmacy Third Party Payer Rejects Worklist. After selecting a comment action, the system displays the selected line item and prompts the user to enter a comment.

Example 5.6-2: Displaying the Prescription Line Item to Add a Comment or Quit

O Add OPECC Comment EX Exit

P Add Pharmacy/OPECC Comment

Select action: Next Screen// O Add OPECC Comment

Enter the line number for which you wish to Add comments.

Select item: 12.1//

34. The system prompts for the comment and allows up to 70 characters of freeform text. The system will track the user who entered the comment.

Example 5.6-3: Adding a comment to a Prescription Line Item

Enter Comment: This shows a test comment line for a prescription line item.

35. The comment that has been added is displayed with the date of the entry, and a Pharmacy / OPECC Comment is indicated by “(Pharm).” The system then prompts the user for a comment action, to Quit (the default) or Exit.

Example 5.6-4: Displaying the Added Comment and Prompting for Another

ADD/VIEW COMMENTS Jul 02, 2005@22:19 Page: 1 of 1

PHARMACY ECME

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

1.1 DESIPRAMINE HCL 25 00068-0011-10 07/01 909393\$ 0/000001105635 W \*\* AC/R

08/15/05 - This shows a test comment line for a prescription line item.

(LAST,FIRST NAME)

p-Payable

07/11/15 (Pharm) - TEST COMMENT FOR PHARMACY/OPECC COMMENT

(LAST,FIRST NAME)

p-Payable

Enter ?? for more actions

O Add OPECC Comment EX Exit

P Add Pharmacy/OPECC Comment

Select action: Next Screen//

36. Comments can also be generated automatically by the system.
    - For Veterans, there are two types of user-defined rejections that are automatically sent to the Pharmacy Worklist:
1.  Transfer Rejects.
1.  Reject Resolution Required Rejects. The Transfer Reject comment is “Auto Send to Pharmacy Worklist due to Transfer Reject Code” and the Reject Resolution Required Reject comment is “Auto Send to Pharmacy Worklist due to Reject Resolution Required.”
    - TRICARE and CHAMPVA prescriptions are sent to the Pharmacy Worklist if the claim is rejected for any reason. The TRICARE and CHAMPVA comment are “Auto Send to Pharmacy Worklist & OPECC – CVA/TRI.”
    - Auto-resolved rejects will display the comment “Not Transferred to Pharmacy – Unable to Resolve Backbill/Resubmission (POSTMASTER).”
    - There are two comments displayed when the pharmacist attempts to resolve a reject, but the claim cannot transmit:
1.  OPECC to Cancel Existing Bill in IB & Resubmit Claim.
2.  Reason Not Billable (RNB) must be removed from Claims Tracking prior to resubmitting.

## Further Research Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Further Research* Screen allows the user to access different sets of data within VistA for quick problem resolution. The *Further Research* Screen allows the user to access (or jump to) options in other VistA applications.

1.  Enter FR at the “Select Action:” prompt on the ECME User Screen.

Example 5.7-1: Accessing the Further Research Action

PHARMACY ECME July 26, 2005@11:31:22 Page: 18 of 42

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Patient Name

+# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

16 ECMEpatient,One (XXXX) WEBMD / VET ALL payable

16.1 ETANERCEPT 25MG/VI 58406-0425-34 07/22 909504\$ 0/000001105747 M RT AC/N

p-Payable

16.2 ETANERCEPT 25MG/VI 58406-0425-34 07/22 909504\$ 1/000001105747 M RT AC/N

p-Payable

16.3 DIVALPROEX 125MG T 00074-6212-13 07/22 909505\$ 0/000001105748 M RT AC/N

p-Payable

16.4 COLLAGENASE OINT 50484-0527-30 07/22 909506\$ 0/000001105749 M RT AC/N

p-Payable

16.5 NAFCILLIN 1 GM. IN 00209-6950-22 07/22 909507\$ 0/000001105750 M RT AC/N

p-Payable

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen// FR Further Research

37. The system re-displays the ECME User Screen with multiple new “Research” options.

Example 5.7-2: Displaying Multiple Further Research Menu Options

FURTHER RESEARCH SCREEN Nov 03, 2010@15:27:54 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/06 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/26 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/27 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/27 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

INS Insurance details CT Claims Tracking EVNT IB Events Report

VE View Eligibility TPJI Third Party Inquiry GRPL Group Plan Menu

VP View Prescription OH On Hold Copay List EX Exit

CMT Add/View Comments RH Release Copay

Select action:Next Screen//

### Insurance Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action allows the user to view insurance details for a single patient line item. The *Insurance Details* action allows the user to access the Patient Insurance Info View / Edit option, located on the Patient Insurance Menu in the Integrated Billing software.

1.  Enter INS at the “Select Action” prompt, and a single line item to view the *Insurance Details* information for a patient.

Example 5.7.1-1: Accessing Insurance Details Option

FURTHER RESEARCH SCREEN Nov 03, 2010@15:27:54 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/06 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/26 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/27 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/27 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

INS Insurance details CT Claims Tracking EVNT IB Events Report

VE View Eligibility TPJI Third Party Inquiry GRPL Group Plan Menu

VP View Prescription OH On Hold Copay List EX Exit

CMT Add/View Comments RH Release Copay

Select action:Next Screen// INS Insurance details

Please select a SINGLE Patient Line item for viewing Insurance

Select item: 1.4

38. While in Patient Insurance Info View / Edit, the user will have access to all the actions at the bottom of the Insurance Screen. When the user enters QUIT, the system will return to the *Further Research* Screen.

Example 5.7.1-2: Displaying Insurance Details Actions

Patient Insurance Information Aug 09, 2006@12:56:49 Page: 1 of 1

Insurance Management for Patient: ECMEpatient,One 0000

Insurance Co. Type of Policy Group Holder Effect. Expires

1 WEBMD PRESCRIPTION 10000 SELF 01/01/00

Enter ?? for more actions \>\>\>

VP View Policy Info BU Benefits Used EX Exit

AB Annual Benefits INS View Insurance Co.

Select Action:Quit// QUIT

### View Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *View Eligibility* action allows the user to view the Patient Eligibility Screen.

Key The full set of menu options is available only for users with IB INSURANCE SUPERVISOR and IB INSURANCE COMPANY ADD security keys.

1.  Enter VE to view eligibility information for a single patient.

Example 5.7.2-1: Accessing View Eligibility Option

FURTHER RESEARCH SCREEN Nov 03, 2010@15:27:54 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/06 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/26 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/27 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/27 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

INS Insurance details CT Claims Tracking EVNT IB Events Report

VE View Eligibility TPJI Third Party Inquiry GRPL Group Plan Menu

VP View Prescription OH On Hold Copay List EX Exit

CMT Add/View Comments RH Release Copay

Select action:Next Screen// VE View Eligibility

Please select a SINGLE Patient Line item for viewing Eligibility

Select item: 1.4

39. While in the View Eligibility action, the user will have access to only the EXIT / QUIT action at the bottom of the Patient Eligibility Screen. When the user enters QUIT, the system will return to the *Further Research* Screen.

Example 5.7.2-2: Displaying View Eligibility Options.

Patient Eligibility Aug 15, 2005@11:14:12 Page: 1 of 1

ECMEPatient,Six 5959 DOB: 01/02/66

Means Test: YES Insured: Yes

Date of Test: 07/29/05 A/O Exposure:

Co-pay Exemption Test: Rad. Exposure:

Date of Test:

Patient has agreed to pay deductible

Primary Elig. Code: NSC

Service Connected: No

Rated Disabilities: None

Enter ?? for more actions

EX Exit

Select Action: Quit//

### View Prescription

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action allows the user to view details for a single prescription. It accesses the *View Prescription* option, located on the Rx Prescriptions Menu in the Outpatient Pharmacy Manager software.

1.  When VP is entered at the “Select Action:” field, the user will be prompted for the line item of the prescription to display.

Example 5.7.3-1: Accessing View Prescription Action

FURTHER RESEARCH SCREEN Nov 03, 2010@15:27:54 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/06 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/26 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/27 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/27 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

INS Insurance details CT Claims Tracking EVNT IB Events Report

VE View Eligibility TPJI Third Party Inquiry GRPL Group Plan Menu

VP View Prescription OH On Hold Copay List EX Exit

CMT Add/View Comments RH Release Copay

Select action:Next Screen// VP View Prescription

Please select a SINGLE Rx Line item for viewing a Prescription

Select item: 1.4

40. Once a single prescription line item is entered, the system displays the following screens for the selected prescription. When QUIT is entered, the system will return the user to the *Further Research* Screen.

Example 5.7.3-2: Displaying View Prescription Options

Rx Activity Log Nov 03, 20XX@15:27:54 Page: 1 of 5

ECMEPatient,Six

PID: XXXX Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAY X,XXXX (XX) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

Rx \#: XXXXXX\$

Orderable Item: TRIAMTERENE 50MG

CMOP Drug: TRIAMTERENE 50MG TAB

\*Dosage: 50MG

Verb: TAKE

Dispense Units: 1

Noun: TABLET

\*Route: ORAL

\*Schedule: 2X

Patient Instructions

SIG: TAKE ONE TABLET BY MOUTH 2X

Patient Status: OPT NSC

Issue Date: 10/07/XX Fill Date: 10/07/XX

Last Fill Date: 10/07/XX (Window)

Last Release Date: Lot \#:

Expires: 10/08/XX MFG:

Days Supply: 90 QTY (TAB): 11

\# of Refills: 3 Remaining: 3

Provider: OPINSUR2

Routing: Window

Copies: 1

Method of Pickup:

Clinic: Not on File

Division: XXXXXXXXXX

Pharmacist:

Patient Counseling: NO

Remarks:

Finished By: PSOuser,Two

Entry By: PSOuser,Two Entry Date: 10/6/XX 11:45:57

Original Fill Released: Routing: Window

Refill Log:

\# Log Date Refill Date Qty Routing Lot \# Pharmacist

=======================================================================

There are NO Refills For this Prescription

Partial Fills:

\# Log Date Date Qty Routing Lot \# Pharmacist

=======================================================================

There are NO Partials for this Prescription

Activity Log:

\# Date Reason Rx Ref Initiator Of Activity

=======================================================================

1 08/03/XX EDIT ORIGINAL PSOuser,Two

Comments: FILL DATE (3050801),

Copay Activity Log:

\# Date Reason Rx Ref Initiator Of Activity

=======================================================================

There's NO Copay activity to report

Label Log:

\# Date Rx Ref Printed By

=======================================================================

1 08/01/XX ORIGINAL PSOuser,Three

Comments: From RX number XXXXXX

2 08/03/05 ORIGINAL PSOuser,Three

Comments: From RX number XXXXXX (Reprint)

Rx Activity Log Nov 03, 2010@15:27:54 Page: 5 of 5

ECMEPatient,Six

PID: XXXX Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN X, XXXX (XX) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)+

ECME Log:

\# Date Rx Ref Initiator Of Activity

=======================================================================

1 5/22/06@19:00:24 ORIGINAL PSOuser,Three

Comments: Submitted to ECME:CMOP TRANSMISSION(NDC:00049-3980-60)

2 7/6/06@19:01:04 REFILL 1 PSOuser,Three

Comments: Submitted to ECME:CMOP TRANSMISSION(NDC:00049-3980-60)

3 7/7/06@14:39:19 REFILL 1 PSOuser,Three

Comments: Submitted to ECME:REJECT WORKLIST-DUR OVERRIDE CODES(DD/M0/1B)-E

PAYABLE-pMEDCO

4 7/8/06@12:48:02 REFILL 1 PSOuser,Three

Comments: CHAMPVA-ECME RED Resubmit Claim w/Edits: Date of Service

(7/6/2006)-pMEDCO

ECME REJECT Log:

\# Date/Time Rcvd Rx Ref Reject Type STATUS Date/Time Resolved

=======================================================================

1 7/6/06@19:02:08 REFILL 1 DUR RESOLVED 7/7/06@14:39:19

Comments: AUTOMATICALLY CLOSED (CLAIM RE-SUBMITTED)

Enter ?? for more actions

Select Action:Quit//

### Add / View Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When CMT is entered at the “Select Action:” field, the user will access the *Add/View Comments* as described in Section 5.8. The only difference is that when QUIT is selected, the user will be returned to the *Further Research* Screen.

### Claims Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action accesses the Claims Tracking Edit Screen of the Claims Tracking Edit for Billing option in the Integrated Billing software.

1.  Enter the CT action and then enter a single prescription line item to track a claim.

Example 5.7.5-1: Accessing Claims Tracking Option

FURTHER RESEARCH SCREEN Nov 03, 2010@15:27:54 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 11 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/06 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/06 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/07 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/07 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

INS Insurance details CT Claims Tracking EVNT IB Events Report

VE View Eligibility TPJI Third Party Inquiry GRPL Group Plan Menu

VP View Prescription OH On Hold Copay List EX Exit

CMT Add/View Comments RH Release Copay

Select action:Next Screen// CT Claims Tracking

Please select a SINGLE Rx Line item when accessing Claims Tracking.

Select item: 1.1.......

41. While in the *Claims Tracking* action, the user will have menu access to all Claims options at the bottom. Entering EXIT or QUIT will end the *Claims Tracking* and return the user to the *Further Research* screen.

Example 5.7.5-2: Displaying Claims Tracking Options

CLAIMS TRACKING EDIT Nov 03, 2010@15:27:54 Page: 1 of 3

Expanded Claims Tracking Info for: ECMEPatient, Two ROI:

For: PRESCRIPTION REFILL on 11/04/05

\+

Visit Type: PRESCRIPTION REFILL Authorization \#:

Prescription \#: XXXXXXX No. Days Approved: 0

Fill Date: Nov 04, 2005 Second Opinion Required:

Drug: ALLOPURINOL 300MG, 30'S Second Opinion Obtained:

Quantity: 1

Days Supply: 1 Review Information

2 NDC#: 51079-0206-20 Insurance Claim: YES

Physician: ECMEProvider,Two Follow-up Type:

Random Sample:

Special Condition:

Local Addition:

Ins. Reviewer:

Hospital Reviewer:

Billing Information

\+ Enter ?? for more actions

BI Billing Info Edit TA Treatment Auth. EX Exit

RI Review Info SE Submit Claim to ECME

Select Action:Next Screen// \<Enter\>

CLAIMS TRACKING EDIT Nov 03, 2010@15:27:54 Page: 2 of 3

Expanded Claims Tracking Info for: ECMEpatient,Two ROI:

For: PRESCRIPTION REFILL on 11/04/05

\+

Episode Billable: NO Total Charges: \$ 0

Non-Billable Reason: PRESCRIPTION NOT REL Estimated Recv (Pri): \$

Next Bill Date: Estimated Recv (Sec): \$

Work. Comp/OWCP/Tort: Estimated Recv (ter): \$

Initial Bill: Means Test Charges: \$

Bill Status: Amount Paid: \$ 0

Hospital Reviews Entered

Insurance Reviews Entered

Service Connected Conditions:

Service Connected: NO

\+ Enter ?? for more actions

BI Billing Info Edit TA Treatment Auth. EX Exit

RI Review Info SE Submit Claim to ECME

Select Action:Next Screen//\<Enter\>

CLAIMS TRACKING EDIT Nov 03, 2010@15:27:54 Page: 3 of 3

Expanded Claims Tracking Info for: ECMEpatient,Two ROI:

For: PRESCRIPTION REFILL on 11/04/05

\+

NONE STATED

Enter ?? for more actions

BI Billing Info Edit TA Treatment Auth. EX Exit

RI Review Info SE Submit Claim to ECME

Select Action:Quit//

### Third Party Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “TPJI” action allows the user to access the Third Party Joint Inquiry option in the Integrated Billing software.

1.  Enter the TPJI action and then enter a single prescription line item to access the *Third Party (Joint) Inquiry* claim information.

Example 5.7.6-1: Accessing Third Party (Joint) Inquiry Option

FURTHER RESEARCH SCREEN Nov 03, 2010@15:27:54 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/06 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/26 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/27 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/27 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

INS Insurance details CT Claims Tracking EVNT IB Events Report

VE View Eligibility TPJI Third Party Inquiry GRPL Group Plan Menu

VP View Prescription OH On Hold Copay List EX Exit

CMT Add/View Comments RH Release Copay

Select action:Next Screen// TPJI Third Party Inquiry

Please select a SINGLE Patient Line item when accessing TPJI

Select item:

42. While in *Third Party (Joint) Inquiry*, the user has access to all actions displayed at the bottom of the screen. Enter QUIT to return to the main *Further Research* Screen.

Example 5.7.6-2: Displaying Third Party (Joint) Inquiry Options.

Third Party Active Bills Nov 03, 2010@15:27:54 Page: 1 of 1

ECMEPatient,SIX (XXXX)NSC

Bill \# From To MT? Type Stat Rate Insurer Orig Amt Curr Amt

1 K400K9Ce 06/15/05 06/15/05 YES OP A REIM IN WEBMD 45.00 45.00

2 K400K9De 06/15/05 06/15/05 YES OP A REIM IN WEBMD 45.00 45.00

\|r Referred \|\* MT on Hold \|+ Multi Carriers \|

CI Claim Information IL Inactive Bills PI Patient Insurance

CP Change Patient HS Health Summary EL Patient Eligibility

Select Action: Quit//

### On Hold Copay Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option lists On Hold copay information for a single patient. The OH action allows the user to access the *List Current/Past Held Charges by Pt* option, located on the On Hold Menu (that is located on the Automated Means Test Billing Menu) in Integrated Billing software.

10. The On Hold Copay Listing requires that a device with 132 column width be used. It will not display correctly using 80 column width devices.
1.  Enter the OH action and then enter a single patient line item to access the *On Hold CopayListing* option*.*

Example 5.7.7-1: Accessing On Hold Copay Listing Option

FURTHER RESEARCH SCREEN Nov 03, 2010@15:27:54 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/26 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/26 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/27 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/27 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

INS Insurance details CT Claims Tracking EVNT IB Events Report

VE View Eligibility TPJI Third Party Inquiry GRPL Group Plan Menu

VP View Prescription OH On Hold Copay List EX Exit

CMT Add/View Comments RH Release Copay

Select action:Next Screen// OH On Hold Copay Listing

Please select a SINGLE Patient Line item when accessing On Hold Copay Listing

Select item: 1

43. The user is prompted for a start and end date for the report.

Example 5.7.7-2: Entering On Hold Copay Report Start and End Dates

Start with DATE: T-3 (AUG 14, 2005)

Go to DATE: T (AUG 17, 2005)

44. The user is are prompted to choose whether to include Pharmacy Co-pay charges or not.

Example 5.7.7-3: Entering “Y” to Include Pharmacy Co-pay Charges on Report

Include Pharmacy Co-pay charges on this report? NO// YES

\*\*\* Margin width of this output is 132 \*\*\*

\*\*\* This output should be queued \*\*\*

DEVICE: HOME// 132PRINTER

45. Print the report at 132 characters.

Example 5.9.7-4: Printed On Hold Copay Listing Report

List of all HELD bills for ECMEPatient,SIX (XXXX) AUG 8,2006 PAGE 1

PATIENT CHARGES CORRESPONDING THIRD PARTY BILLS

=============================================================================\|\|========================================

From/ Date AR IB \|\| AR

Action ID Type Bill# Fill Dt to AR Charge Status Status\|\| Bill# Classf(\$Typ) ST Charge % Paid

=============================================================================\|\|========================================

'\*' = outpt visit on same day as Rx fill date \|\|

=============================================================================\|\|========================================

5002877 NSC RX Rx \#: 100003994 ECME \# 000001234579\|\|

12/30/05 8.00 ON HOLD\|\|

Enter RETURN to continue or '^' to exit:

### Release Copay

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This action accesses the *Release Charges 'On Hold'* option, located on the On Hold Menu (that is located on the Automated Means Test Billing Menu) in the Integrated Billing software. If The user selects a single Rx Line item, the system defaults the to the REF# of the selected Rx.

1.  Enter RH to access the *Release Copay* option. The user may select a single Patient line item or a single Rx line item.

Example 5.7.8-1: Accessing Release Copay Option

FURTHER RESEARCH SCREEN Nov 03, 2010@15:27:54 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/06 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/26 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/27 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/27 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

INS Insurance details CT Claims Tracking EVNT IB Events Report

VE View Eligibility TPJI Third Party Inquiry GRPL Group Plan Menu

VP View Prescription OH On Hold Copay List EX Exit

CMT Add/View Comments RH Release Copay

Select action:Next Screen// RH Release Copay

Please select a SINGLE Patient Line item or a SINGLE Rx Line item when accessing

Release Copay from Hold.

Select item: 9

46. All copay charges on hold for the selected patient or prescription are listed. Select the line number (reference number) of the item for the release of that copay, then answer Y to okay the charge to Accounts Receivable. The selection is redisplayed and you are advised that the listed charge has been passed to Accounts Receivable.

Example 5.7.8-2: Listing On Hold Copay Charges for Release Copay Option

ECMEPatient,,SIX Pt ID: 000-00-0000

-----------------------------------------------------------------------

The following IB Actions for this patient are ON HOLD:

=======================================================================

REF Action ID Bill Type Bill \# Fr/Fl Dt To/Rls Dt Charge

=======================================================================

1 000596570 Rx \#: 909708 08/01/05 08/01/05 21.00

ECME \#: 000000000000

2 000596574 Rx \#: 909693 08/01/05 08/01/05 21.00

ECME \#: 000000000000

3 000596575 Rx \#: 909694 08/01/05 08/01/05 21.00

ECME \#: 000000000000

4 000596580 Rx \#: 909728 08/01/05 08/01/05 21.00

ECME \#: 000000000000

5 000596581 Rx \#: 909703 08/01/05 08/01/05 21.00

ECME \#: 000000000000

6 000596601 Rx \#: 909698 08/01/05 08/03/05 21.00

ECME \#: 000000000000

Select IB Actions (REF \#) to release (or '^' to exit): 2

OK to pass this charge to Accounts Receivable? YES

Passing charges to Accounts Receivable...

=======================================================================

REF Action ID Bill Type Bill \# Fr/Fl Dt To/Rls Dt Charge

=======================================================================

2 000596574 Rx \#: 909693 K400KDC 08/01/05 08/01/05 21.00

ECME \#: 000000000000

The charge listed above has been passed to Accounts Receivable.

Enter RETURN to continue or '^' to exit:

### IB (Integrated Billing) Events Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “EVNT” action allows the user to access the *IB e-Pharmacy Menu* Option, ECME Billing Events Report.

1.  Enter EVNT to access the *IB Events Report* option. The user may select a single Patient line item or a single Rx line item.

Example 5.7.9-1: Accessing IB Events Report Option

FURTHER RESEARCH SCREEN Nov 03, 2010@15:27:54 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/06 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/26 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/27 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/27 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

INS Insurance details CT Claims Tracking EVNT IB Events Report

VE View Eligibility TPJI Third Party Inquiry GRPL Group Plan Menu

VP View Prescription OH On Hold Copay List EX Exit

CMT Add/View Comments RH Release Copay

Select action:Next Screen// EVNT IB Events Report

Please select a SINGLE Patient Line item or a SINGLE Rx Line item when accessing

The IB Events Report.

Select item: 2

47. The user is prompted for a start and end date for this report.

Example 5.7.9-2: Entering Dates to Include in IB Events Report Listing

START WITH DATE: TODAY//T-60 (JUN 23, 2005)

GO TO DATE: TODAY//T (AUG 22, 2005)

48. The user is prompted to select M (Mail), W (window), C (CMOP) or A (All) events for the selected line item report.

Example 5.7.9-3: Choosing Default ‘All’ for Types of Events for IB Events Report

Select one of the following:

M MAIL

W WINDOW

C CMOP

A ALL

(M)AIL, (W)INDOW, (C)CMOP, (A)LL: ALL// \<Enter\> ALL

49. The user is prompted to select S (SUMMARY REPORT) or D (DETAILED REPORT) and a print device.

Example 5.7.9-4: Selecting Summary Type for IB Events Report

S SUMMARY REPORT

D DETAILED REPORT

(S)UMMARY REPORT, (D)ETAILED REPORT: SUMMARY REPORT// \<Enter\> SUMMARY REPORT

DEVICE: HOME//

PAGE 1

BILLING ECME EVENTS ON 06/23/05 TO 08/22/05 (SUMMARY)

RX# FILL DATE PATIENT NAME DRUG

=======================================================================

1 909693 0 08/01/05 ECMEPatient,SIX EPOETIN ALFA,RECOMB 20,000UNT/

FINISH 08/01/05 11:32a Status:ECME Billable

SUBMIT 08/01/05 11:34a Status:OK

REVERSAL 08/01/05 3:19p Status:ECME Claim reversed, no Bill to cancel

FINISH 08/01/05 3:20p Status:ECME Billable

SUBMIT 08/01/05 3:20p Status:OK

RELEASE 08/01/05 3:20p Status:OK

-----------------------------------------------------------------------

2 909694 0 08/01/05 ECMEPatient,Seven CYCLOPHOSPHAMIDE 1000MG INJ

FINISH 08/01/05 11:44a Status:ECME Billable

SUBMIT 08/01/05 11:45a Status:OK

REVERSAL 08/01/05 3:37p Status:ECME Claim reversed, no Bill to cancel

FINISH 08/01/05 3:38p Status:ECME Billable

SUBMIT 08/01/05 3:38p Status:OK

RELEASE 08/01/05 3:38p Status:OK

BILLING 08/01/05 3:38p Status:Bill# K400KBC created

REVERSAL 08/05/05 3:09p Status:Bill# K400KBC cancelled

Press RETURN to continue, '^' to exit:

Example 5.7.9-5: Selecting a Detailed Type for IB Events Report

S SUMMARY REPORT

D DETAILED REPORT

(S)UMMARY REPORT, (D)ETAILED REPORT: SUMMARY REPORT// DETAILED REPORT

DEVICE: HOME//

PAGE 1

BILLING ECME EVENTS ON 07/06/11 TO 09/04/11 (DETAILED) for XXXXXX VAMC DIVISIO

RX# FILL DATE PATIENT NAME DRUG

=======================================================================

1 2054789 0 06/08/11 ECMEPATIENT,SIX CLONAZEPAM 1MG TAB

FINISH 08/10/11 6:35p Status:ECME Billable

ELIGIBILITY:

DRUG:CLONAZEPAM 1MG TAB

NDC:57664-0274-08, BILLED QTY:30, COST:.024, DEA:4CPR

PLAN: INSURANCE: WEBMD COB: S

BIN:123456, PCN:1123456789, PAYER SHEET B1:WBTESTB1

PAYER SHEET B2:WBTESTB2, PAYER SHEET B3:WBTESTB1

DISPENSING FEE:11.40, BASIS OF COST DETERM:COST CALCULATIONS

COST:12.12, GROSS AMT DUE:12.12, ADMIN FEE:0.00

USER:ECMEuser,Two

SUBMIT 08/10/11 6:35p Status:OK

ECME#:000001614656, FILL DATE:06/08/11, RELEASE DATE:06/08/11

PAYER RESPONSE: PAYABLE

PLAN:, INSURANCE: WEBMD

USER:ECMEuser,Three

BILLING 08/10/11 6:35p Status:Bill K10004V created with ERRORs

Press RETURN to continue, '^' to exit:

PAGE 2

BILLING ECME EVENTS ON 07/06/11 TO 09/04/11 (DETAILED) for XXXXXX VAMC DIVISIO

RX# FILL DATE PATIENT NAME DRUG

=======================================================================

ERROR DESCRIPTION: Cannot establish receivable in AR (secondary ins).

ECME#:000001614656, FILL DATE:06/08/11, RELEASE DATE:06/08/11

DRUG:CLONAZEPAM 1MG TAB

NDC:57664-0274-08, BILLED QTY:30, DAYS SUPPLY:30

BILLED:12.12, PAID:68.32

PLAN:, INSURANCE: WEBMD

USER:ECMEuser,One

REVERSAL 08/11/11 1:18p Status:

ECME#:000001614656, FILL DATE:06/08/11, RELEASE DATE:06/08/11

PAYER RESPONSE: ACCEPTED

PLAN:, INSURANCE: WEBMD

USER:ECMEuser,Two

REVERSAL REASON:TST

FINISH 08/11/11 1:20p Status:ECME Billable

ELIGIBILITY:

DRUG:CLONAZEPAM 1MG TAB

NDC:57664-0274-08, BILLED QTY:30, COST:.024, DEA:4CPR

Press RETURN to continue, '^' to exit:

PAGE 3

BILLING ECME EVENTS ON 07/06/11 TO 09/04/11 (DETAILED) for CHEYENNE VAMC DIVISIO

RX# FILL DATE PATIENT NAME DRUG

=======================================================================

PLAN: INSURANCE: WEBMD COB: S

BIN:123456, PCN:1123456789, PAYER SHEET B1:WBTESTB1

PAYER SHEET B2:WBTESTB2, PAYER SHEET B3:WBTESTB1

DISPENSING FEE:11.40, BASIS OF COST DETERM:COST CALCULATIONS

COST:12.12, GROSS AMT DUE:12.12, ADMIN FEE:0.00

USER:ECMEuser,Two

SUBMIT 08/11/11 1:20p Status:OK

ECME#:000001614656, FILL DATE:06/08/11, RELEASE DATE:06/08/11

PAYER RESPONSE: REJECTED

PLAN:, INSURANCE: WEBMD

USER:ECMEuser,One

-----------------------------------------------------------------------

2 2054803 0 05/06/11 ECMEPATIENT,SIX LIDOCAINE 0.5% (5MG/ML) 50ML M

FINISH 08/10/11 6:07p Status:ECME Billable

ELIGIBILITY:

DRUG:LIDOCAINE 0.5% (5MG/ML) 50ML MDV

NDC:00409-4278-01, BILLED QTY:30, COST:1.486, DEA:6P

Press RETURN to continue, '^' to exit:

### Group Plan Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “GRPL” action allows the user to access the *Group Plan Menu*. This menu includes three selections - Edit PLAN APPLICATION Sub-file (EPLA), Match Group Plan to a Pharmacy Plan (MGP), and Match Multiple Group Plans to a Pharmacy Plan (MMGP).

1.  Enter GRPL to access the *Group Plan Menu* option.

Example 5.7.10-1: Accessing Group Plan Menu

FURTHER RESEARCH SCREEN Nov 03, 2010@15:27:54 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/26 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/26 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/27 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/27 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

INS Insurance details CT Claims Tracking EVNT IB Events Report

VE View Eligibility TPJI Third Party Inquiry GRPL Group Plan Menu

VP View Prescription OH On Hold Copay List EX Exit

CMT Add/View Comments RH Release Copay

Select action:Next Screen// GRPL Group Plan Menu

--- Group Plan Menu ---

EPLA Edit PLAN APPLICATION Sub file

MGP Match Group Plan to a Pharmacy Plan

MMGP Match Multiple Group Plans to a Pharmacy Plan

Select Item(s):

### Eligibility Inquiry Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The hidden “ELIG” Option accesses the *Eligibility Inquiry Option* that allows the sites to verify pharmacy insurance for patients by sending an eligibility verification submission to the third party payer.

1.  When ELIG is entered at the “Select Action:” field, the user will be prompted for the line item of the prescription to display.
50. The user can edit the Relationship Code, Person Code, and Insurance Effective Date.

Example 5.7.11-1: Accessing Eligibility Inquiry Option

FURTHER RESEARCH SCREEN Nov 03, 2010@15:27:54 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/06 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/26 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/27 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/27 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

INS Insurance details CT Claims Tracking EVNT IB Events Report

VE View Eligibility TPJI Third Party Inquiry GRPL Group Plan Menu

VP View Prescription OH On Hold Copay List EX Exit

CMT Add/View Comments RH Release Copay

Select action:Next Screen// ELIG ELIG

Enter the line number for the claim to be submitted for Eligibility Verification

Select item: 1.1

You've chosen to VERIFY Eligibility of the following prescription for ECMEPATIENT,

SIX

1.1 SIMETHICONE 40MG 02587542934 10/26 1100335\$ 0/000000003119 W RT AC/R

Are you sure?(Y/N)? YES

Relationship Code: 1// CARDHOLDER

Person Code: 01//

Effective Date: 10/06/2010// 11/3/2010

Are you sure?(Y/N)? YES

Not submittable: Eligibility Payer Sheet Not Found.

Enter RETURN to continue or '^' to exit:

51. When the user enters QUIT, the system will return to the *Further Research* Screen.
52. When EX is entered at the “Select Action:” prompt from the Further Research Screen, the system will return to the ECME User Screen.

Example 5.7.11-2: Entering the EXIT Action from Further Research Screen

FURTHER RESEARCH SCREEN Nov 03, 2010@15:27:54 Page: 1 of 30

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1 ECMEPatient,,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/06 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/26 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/27 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/27 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

INS Insurance details CT Claims Tracking EVNT IB Events Report

VE View Eligibility TPJI Third Party Inquiry GRPL Group Plan Menu

VP View Prescription OH On Hold Copay List EX Exit

CMT Add/View Comments RH Release Copay

Select action:Next Screen// EX Exit

## Print Claim Log (Hidden Action)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Print Claim Log* option allows the user to print a detailed history in reverse chronological order of the third party claims and responses.

1.  Enter the LOG action and a single prescription line item to view the claim log information for a prescription.

Example 5.10-1: Accessing the Print Claim Log Option

PHARMACY ECME Aug 12, 2005@02:40:34 Page: 1 of 81

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 30 day(s)

Sorted by: Patient Name

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

1 ECMEPatient,,SIX (XXXX) OPINSUR2/2055557898 VET Pb:10 Rj:2 AcRv:0 RjRv:1

1.1 SIMETHICONE 40MG 02587542934 10/06 1100335\$ 0/000000003119 W RT AC/R

p-Rejected

85:Claim Not Processed

NN:Transaction Rejected At Switch Or Intermediary

02:M/I Version/Release Number

EV117-D0 IS INVALID VERSION NUMBER

1.2 TRIAMTERENE 50MG, 00484359030 10/06 1100336\$ 0/000000003120 W RT DS/R

p-Reversal Other

1.3 AMYL NITRITE 0.3M 00223700212 10/07 1100337\$ 0/000000003122 W RT DS/R

p-Reversal Other

1.4 TRIAMTERENE 50MG, 00484359030 10/07 1100339\$ 0/000000003124 W RT AC/R

p-Payable

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen// LOG Print Claim Log

Enter the line number for which you wish to print claim logs.

Select item: 5.1

53. As the data pages print on the screen, there are options to print the information to a device (type PRINT and the device name) or exit (type EXIT) or continue to display information, which is the default (press \<Enter\>).

Example 5.8-2: Displaying Claim Log Data for a Selected Prescription Line Item

PHARMACY ECME Aug 22, 2005@13:58:50 Page: 1 of 7

Claim Log information

Pharmacy ECME Log

Rx \#: 909393/0 ECME#: 000001105635

Drug: AMOXICILLIN 250MG CAP

Patient: ECMEpatient,One (0000) Sex: M DOB: JAN 1, 1954 (57)

Submitted: JUN 15,2005@15:19:11

By: ECMEuser,One

VA Claim \#: VA2005=1234567893=123456=0000502

\+ Enter ?? for more actions

PR Print Data EX Exit

Select action:Next Screen// \<Enter\>

PHARMACY ECME Sep 11, 2005@11:36:14 Page: 2 of 7

Claim Log information

\+

Transaction Information (#661)-------------------------------------------------

Created on: JUN 15,2005@16:25:48

Submitted By: ECMEUSER,FOUR

Transaction Type: REQUEST

Date of Service: 06/15/2005

NDC Code: 00068-0011-10

Quantity Submitted on Claim: 60 ( )

Days Supply: 30

Division : REDACTED

NPI#: 4000000016

ECME Pharmacy: XXXXXXXXX

Rx Qty: 90 (EA) Unit Cost: .752 Gross Amt Due: 79.08

Ingredient Cost: 67.68 Dispensing Fee: 11.40

U&C Charge: 79.08 Admin Fee: 0.00

Insurance Name: WEBMD

Rx Coordination of Benefits: PRIMARY

BIN: 123456

PCN: 1123456789

Group ID: WEBMDTEST

Cardholder ID:

Patient Relationship Code: CARDHOLDER

Cardholder First Name: One

Cardholder Last Name: ECMEpatient

Facility ID Qualifier:

\+ Enter ?? for more actions

PR Print Data EX Exit

Select action:Next Screen// \<Enter\>

PHARMACY ECME Sep 11, 2005@11:39:07 Page: 3 of 7

Claim Log information

\+

Plan ID: 8729

Payer Sheet IEN: WBTESTB1

B2 Payer Sheet IEN: WBTESTB2

B3 Rebill Payer Sheet: WBTESTB1

Certify Mode:

Cert IEN:

\+ Enter ?? for more actions

PR Print Data EX Exit

Select action:Next Screen// \<Enter\>

PHARMACY ECME Sep 11, 2005@11:39:51 Page: 4 of 7

Claim Log information

\+

Response Information (#661)----------------------------------------------------

Response Received: JUN 15,2005@16:25:49

Date of Service: 06/15/2005

Transaction Response Status: Paid

Total Amount Paid: \$40.00

Ingredient Cost Paid: \$48.00 Dispensing Fee Paid: \$1.00

Patient Resp (INS): (\$9.00)

Reconciliation ID:

Reject code(s):

Payer Message:

Payer Additional Message:

Reason for Service Code: AD

DUR Text: AMOXICILLIN 250MG CAP

DUR Additional Text: The text would display here

\+ Enter ?? for more actions

PR Print Data EX Exit

Select action:Next Screen// \<Enter\>

PHARMACY ECME Sep 11, 2005@11:39:51 Page: 5 of 7

Claim Log information

\+

Transaction Information (#659)-------------------------------------------------

Created on: JUN 15,2005@15:07:34

Transaction Type: REQUEST

Date of Service: 06/15/2005

NDC Code: 00068-0011-10

Quantity Submitted on Claim: 60 ( )

Days Supply: 30

Division : REDACTED

NPI#: 4000000016

ECME Pharmacy: BAY PINES

Rx Qty: 90 (EA) Unit Cost: .752 Gross Amt Due: 79.08

Ingredient Cost: 67.68 Dispensing Fee: 11.40

U&C Charge: 79.08 Admin Fee: 0.00

Insurance Name: WEBMD

Rx Coordination of Benefits: PRIMARY

BIN: 123456

PCN: 1123456789

Group ID: WEBMDTEST

Cardholder ID:

Patient Relationship Code: CARDHOLDER

Cardholder First Name: One

Cardholder Last Name: ECMEpatient

Facility ID Qualifier:

\+ Enter ?? for more actions

PR Print Data EX Exit

Select action:Next Screen// \<Enter\>

PHARMACY ECME Sep 11, 2005@11:42:41 Page: 6 of 7

Claim Log information

\+

Plan ID: 8729

Payer Sheet IEN: WBTESTB1

B2 Payer Sheet IEN: WBTESTB2

B3 Rebill Payer Sheet: WBTESTB1

Certify Mode:

Cert IEN:

\+ Enter ?? for more actions

PR Print Data EX Exit

Select action:Next Screen// \<Enter\>

54. After the last data page has displayed on the screen, pressing \<Enter\> will default to “QUIT” and the system returns to the ECME User Screen.

PHARMACY ECME Sep 11, 2005@11:43:01 Page: 7 of 7

Claim Log information

\+

Response Information (#659)----------------------------------------------------

Response Received: JUN 15,2005@15:18:30

Date of Service: 06/15/2005

Transaction Response Status: Rejected

Total Amount Paid: \$0

Ingredient Cost Paid: Dispensing Fee Paid:

Patient Resp (INS):

Reconciliation ID:

Reject code(s):

NN:Transaction Rejected At Switch Or Intermediary

Payer Message: NC40-Request from an unknown site. Registration is required

Payer Additional Message:

Reason for Service Code: AD

DUR Text: AMOXICILLIN 250MG CAP

DUR Additional Text: The text would display here

Enter ?? for more actions

PR Print Data EX Exit

Select action:Quit// \<Enter\> QUIT

## Send to Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Send to Worklist* action allows the user to send rejected claims to the Pharmacy Worklist. Depending on Pharmacy settings, all or only claims with certain reject codes may be sent to the Pharmacy Worklist from the ECME User Screen.

Claims that have been closed will be displayed with “/Closed” after the status. Closed claims cannot be sent to the Pharmacy Work List. If the user attempts to resubmit a claim that is closed, a message is displayed indicating the claim “is closed and cannot be sent to the Pharmacy Work List.”

1.  Enter WRK at the Select Action prompt, and a single line item for the claim to send.

Example 5.09-1: Accessing the Send to Worklist Option, and Entering a Line Item

PHARMACY ECME Jul 03, 2008@12:04:02 Page: 1 of 41

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# LOC/TYP RXINF

1 ECMEpatient,One (XXXX) NON TRIC/ VET Pb:0 Rj:6 AcRv:3 RjRv:2

1.1 ALBUTEROL 0.5% IN 50383-0741-20 07/03 2054905\$ 1/000001614782 W RT \*\*/R

p-Rejected

07:M/I Cardholder ID

1.2 JAPANESE ENCEPHAL 49281-0680-30 06/27 2055040\$ 0/000001614918 W RT \*\*/N

p-In progress- Parsing response

1.3 JAPANESE ENCEPHAL 49281-0680-30 07/03 2055040\$ 1/000001614918 W RT DIS/N

p-In progress- Parsing response

1.4 OLANZAPINE 10MG T 00002-4117-30 06/29 2055048\$ 0/000001614926 W RT DIS/N

p-In progress- Parsing response

1.5 OLANZAPINE 10MG T 00002-4117-30 06/29 2055049\$ 0/000001614927 W RT \*\*/N

p-Reversal accepted/Closed

1.6 OLANZAPINE 10MG T 00002-4117-30 07/03 2055049\$ 1/000001614927 W RT AC/N

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen// wrk Send to Worklist

Enter the line numbers for the claim(s) to send to the Pharmacy Worklist.

Select item(s): 1.1

You've chosen to send to Pharmacy Work List the following:

1.1 ALBUTEROL 0.5% IN 50383-0741-20 06/03 2054905\$ 1/000001614782 W RT \*\*/R

Comment for Pharmacy : Needs to be resolved in Pharmacy.

Eligible claim(s) will be sent to the Pharmacy Worklist...

Are you sure?(Y/N)? y YES

1.1 ALBUTEROL 0.5% IN 50383-0741-20 07/03 2054905\$ 1/000001614782 W RT \*\*/R

has been sent to the Pharmacy Work List.

Enter RETURN to continue or '^' to exit:

Updating screen...

55. The system updates the ECME User Screen with the date, the status, any comments entered, and the name of the user who completed the action.

Example 5.09-2: The Updated User Screen

PHARMACY ECME Jul 03, 2008@12:04:48 Page: 1 of 41

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# LOC/TYP RXINF

1 ECMEpatient,One (XXXX) NON TRIC/ VET Pb:0 Rj:6 AcRv:3 RjRv:2

1.1 ALBUTEROL 0.5% IN 50383-0741-20 06/03 2054905\$ 1/000001614782 W RT \*\*/R

07/23/08 - Sent to Pharmacy: Needs to be resolved in Pharmacy.

(ECMEUSER,FOUR)

p-Rejected

07:M/I Cardholder ID

1.2 JAPANESE ENCEPHAL 49281-0680-30 06/27 2055040\$ 0/000001614918 W RT \*\*/N

p-In progress- Parsing response

1.3 JAPANESE ENCEPHAL 49281-0680-30 07/03 2055040\$ 1/000001614918 W RT DS/N

p-In progress- Parsing response

1.4 OLANZAPINE 10MG T 00002-4117-30 06/29 2055048\$ 0/000001614926 W RT DS/N

p-In progress- Parsing response

1.5 OLANZAPINE 10MG T 00002-4117-30 06/29 2055049\$ 0/000001614927 W RT \*\*/N

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen//

56. If an invalid claim is selected, other messages may appear.

Example 5.09-3: Selected Claim Already on the Pharmacy Worklist

1.15 TAZAROTENE 0.1% T 00023-0042-03 07/15 2055208\$ 0/000001615107 W RT AC/N

07/15/08 - Sent to Pharmacy:testing

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen// wrk Send to Worklist

Enter the line numbers for the claim(s) to send to the Pharmacy Worklist.

Select item(s): 1.15

You've chosen to send to Pharmacy Work List the following:

1.15 TAZAROTENE 0.1% T 00023-0042-03 07/15 2055208\$ 0/000001615107 W RT AC/N

was ALREADY sent to the Pharmacy Work List.

Enter the line numbers for the claim(s) to send to the Pharmacy Worklist.

Select item(s):

Example 5.09-4: Selected Claim Doesn’t Have an Eligible Reject Code

Enter the line numbers for the claim(s) to send to the Pharmacy Worklist.

Select item(s):

You've chosen to send to Pharmacy Work List the following:

1.11 ALLOPURINOL 100MG 00364-0632-02 02/18 788538\$ 0/000001459640 W RT AC/N

doesn't have eligible reject code to be sent to the Pharmacy Work List.

Example 5.09-5: Selected Claim Has Not Been Rejected

Enter the line numbers for the claim(s) to send to the Pharmacy Worklist.

Select item(s):

You've chosen to send to Pharmacy Work List the following:

1.11 ACARBOSE 25MG TAB 00026-2863-51 03/03 788628\$ 0/000001459751 W RT DS/N

was not rejected and cannot be sent to the Pharmacy Work List.

Example 5.09-6: Selected Claim is Closed

1.22 ERYTHRITYL TETRAN 00223-0916-01 04/03 102028\$ 3/000000002403 W RT DL/N

04/06/09 - RX DELETED

(ECMEemployee, One)

p-Rejected/Closed

88:DUR Reject Error

1.23 METHANTHELINE 50M 00014-1501-31 03/13 102029\$ 0/000000002404 W RT AC/N

p-Rejected

79:Refill Too Soon

+---------Enter ?? for more actions-----------------------------------

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen// WRK Send to Worklist

Enter the line numbers for the claim(s) to send to the Pharmacy Worklist.

Select item(s): 1.22

You've chosen to send to Pharmacy Work List the following:

1.22 ERYTHRITYL TETRAN 00223-0916-01 04/03 102028\$ 3/000000002403 W RT DE/N

is closed and cannot be sent to the Pharmacy Work List.

Enter the line numbers for the claim(s) to send to the Pharmacy Worklist.

Select item(s):

## Reopen Closed Claims (Hidden Action)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Reopen Closed Claims* hidden action allows the user to reopen closed claims directly from the User Screen instead of having to access this functionality from the *ECME Transaction Maintenance Options* menu. The BPS MANAGER security key is required to use this option.

1.  Enter ROC at the “Select Action:” prompt to access the option and select a line item.

Example 5.10-1: Accessing the Reopen Closed Claims Option

PHARMACY ECME Mar 27, 2009@16:26:50 Page: 1 of 41

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

-#--PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# LOC/TYP RXINF

1 ECMEpatient,One (XXXX) OPINSUR2/2055557898 VET ALL payable

1.1 DOXEPIN 25MG CAP 00839-7221-06 03/27 102105\$ 0/000000002484 W BB AC/R

p-Payable

1.2 METHAZOLAMIDE 50M 00005-5470-23 03/27 102106\$ 0/000000002485 W BB AC/R

p-Payable

2 ECMEpatient,Two (XXXX) OPINSUR1/ VET Pb:53 Rj:28 AcRv:21 RjRv:6

2.1 MEDROXYPROGESTRON 00009-0050-02 06/20 101171\$ 0/000000001521 W RT DS/N

06/20/08 - Clarification Code 99 submitted.

(ECMEuser,One)

p-Reversal accepted

2.2 RESERPINE 0.1MG S 98521-4587-02 03/26 101237A\$ 0/000000001695 C RT DS/R

p- Rejected/Closed

2.3 FUROSEMIDE 10MG/M 51079-0935-20 03/21 101646\$ 0/000000002014 W RT DS/N

+---------Enter ?? for more actions----------------------------------

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen// ROC ROC

Enter the line number for the claim you want to reopen.

Select item(s): 2.2

You've chosen to reopen the following prescriptions(s) for

ECMEpatient,One:

2.2 RESERPINE 0.1MG S 98521-4587-02 03/26 101237A\$ 0/000000001695 C RT DS/R

All Selected Rxs will be reopened using the same information gathered in the

following prompts.

Are you sure?(Y/N)? YES

57. The user is prompted to enter Reopen Comments, after claim information is displayed. Once a comment is entered, the user is asked to reopen this claim.

Example 5.10-2: Entering Text Comment for Reopened Closed Claim

REOPEN COMMENTS: Claim reopened for new refill

ARE YOU SURE YOU WANT TO RE-OPEN THIS CLAIM? (Y/N)? No// YES

ReOpening Claim: VA2009=4000000016=105220=0005843 ... OK

1 claim has been reopened.

Enter RETURN to continue or '^' to exit: \<Enter\>

58. Once the claim has been successfully reopened, the screen is updated and re-displayed.

Example 5.10-3: The User Screen is Updated and Re-Displayed

Updating screen for reopened claims...

PHARMACY ECME Mar 27, 2009@16:28:32 Page: 1 of 41

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Transaction date by default

-#--PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# LOC/TYP RXINF

1 ECMEpatient,One (XXXX) OPINSUR2/2055557898 VET ALL payable

1.1 DOXEPIN 25MG CAP 00839-7221-06 03/27 102105\$ 0/000000002484 W BB AC/R

p-Payable

1.2 METHAZOLAMIDE 50M 00005-5470-23 03/27 102106\$ 0/000000002485 W BB AC/R

p-Payable

2 ECMEpatient,Two (XXXX) OPINSUR1/ VET Pb:53 Rj:28 AcRv:21 RjRv:6

2.1 MEDROXYPROGESTRON 00009-0050-02 03/20 101171\$ 0/000000001521 W RT DS/N

06/20/08 - Clarification Code 99 submitted.

(ECMEuser,One)

p-Reversal accepted

2.2 RESERPINE 0.1MG S 98521-4587-02 03/26 101237A\$ 0/000000001695 C RT DS/R

p-Rejected

2.3 FUROSEMIDE 10MG/M 51079-0935-20 03/21 101646\$ 0/000000002014 W RT DS/N

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen//

## Resubmit with Edits (Hidden Action)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Resubmit with Edits* hidden action allows the user to edit previously rejected electronic pharmacy claims and to resubmit them with the edited information. The data fields that can be edited to enable resubmission are the Pharmacy Relationship Code, Pharmacy Person Code, Prior Authorization Number, Prior Authorization Type Code, up to three Submission Clarification Codes (if the conditions explained below do not exist), Date of Service, Patient Residence Code, Pharmacy Service Type Code, Delay Reason Code, and / or NCPDP Field Name or Number. (The Date of Service prompt is only asked if the prescription has been released.) If the claim selected is for secondary insurance, the Coordination of Benefits information can also be edited.

The relationship code describes the relationship this patient has to the holder of this insurance policy. The standard NCPDP Patient Relationship Code list follows. However, it is important to note that some payers use their own set of codes for this field, so the field should be populated based upon the payer's expectations.

0 Not Specified

1 Cardholder

2 Spouse

3 Child

4 Other

The Person Code is the specific person code assigned to the patient by the payer. The Prior Authorization number is the number submitted by the provider to identify the prior authorization. For more information on the Coordination of Benefits fields, see the [Process Secondary / TRICARE Rx to ECME section](#process-secondary-tricare-rx-to-ecme) of this document.

The Submission Clarification Code cannot be edited if either of these conditions exists:

- An unresolved reject is on the pharmacists’ worklist
- A resolved reject of RTS (79-Refill Too Soon) or DUR (88-Drug Utilization Review) is from the last claim response.

If neither condition exists, the Submission Clarification Code is editable. If either condition exists, the Submission Clarification Code prompt is bypassed, and a message is displayed on the screen indicating the field cannot be edited.

You've chosen to RESUBMIT the following prescription for ECMEpatient,four

1.2 ALBUTEROL 0.5% IN 24208034720 02/22 0000000 0/000000000003 W RT DS/N

Are you sure?(Y/N)? YES

Pharmacy Relationship Code: 1// CARDHOLDER

Pharmacy Person Code: 125//

Prior Authorization Number: 00000000000//

Prior Authorization Type Code: 0// NOT SPECIFIED

Submission Clarification Code 1: 1 NO OVERRIDE

\*\*OPECC cannot edit Sub. Clar. Code field for this reject - refer to Pharmacist

Patient Residence Code: 1//

By answering YES to Submit NCPDP Field Not on Payer Sheet, it becomes possible to submit a NCPDP field that is not on the payer sheet. When prompted for the field name or number, enter “??” for a list of possible choices. Fields already on the payer sheet are excluded from the list of possible choices. Also excluded are any fields that do not have logic to pull data from VistA (i.e. fields that will always be \<blank\>).

Submit NCPDP Field Not on Payer Sheet (Y/N)? N// YES

Enter a valid NCPDP Field name or number. Enter '??' for

a list of possible choices. Fields already on the payer sheet

are excluded from the list of possible choices. Also excluded

are any fields that do not have logic to pull data from VistA

(i.e. fields that will always be \<blank\>).

NCPDP Field Name or Number: ??

Choose from:

498.12 PRESCRIBER TELEPHONE NUMBER

678 TIME OF SERVICE

B08 PATIENT STREET ADDRESS LINE 1

B09 PATIENT STREET ADDRESS LINE 2

B27 PRESCRIBER STREET ADDR LINE 1

B28 PRESCRIBER STREET ADDR LINE 2

B38 PATIENT ID ASSOC COUNTRY CODE

B41 PRES ID ASSOC COUNTRY CODE

B42 PRESCRIBER COUNTRY CODE

B98 RECONCILIATION ID

NCPDP Field Name or Number: 678 TIME OF SERVICE

Value to transmit: 085354

Transmit with claim (Y/N)? Y//

Claims that have been closed will be displayed with “/Closed” after the status. Closed claims cannot be resubmitted with edits. If the user attempts to resubmit a claim that is closed, a message is displayed that the claim is “Closed and cannot be Resubmitted w/Edits.”

1.  Enter RED at the “Select Action:” prompt to choose the prescription line to resubmit.

Example 5.11-1: Accessing the Resubmit with Edits Option

PHARMACY ECME Aug 12, 2011@02:40:34 Page: 1 of 81

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Patient Name

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

5 ECMEpatient,Two (XXXX) WEBMD / VET ALL payable

5.1 LEUCOVORIN 5MG/ML 00703-5140-01 08/12 10958860\$ 0/000009378798 W RT AC/N

p-Reversal rejected

6 ECMEpatient,One (XXXX) WEBMD / VET Pb:3 Rj:1 AcRv:1 RjRv:0

6.1 GRANULEX SPRAY 4O 00514-0001-01 08/12 10958847 0/000009378705 W RT AC/R

p-Payable

6.2 ACARBOSE 100MG TA 00026-2862-51 08/12 52536284 1/000009378782 W RT DS/N

03/20/06 - RX DISCONTINUED

p-Rejected

08:M/I Person Code

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Quit// RED RED

59. Enter the line number for the claim to be submitted.

Example 5.11-2: Entering the Line Item for the Claim Resubmission Request

Enter the line number for the claim to be resubmitted:

Select item: 6.2

60. If the user attempts to resubmit a primary claim when there is a payable secondary claim, the following message displays that will discontinue the claims resubmission process.

Example 5.11-3: Entering the Line Item for a Claim that has a Payable Secondary Claim

The claim:

1.12 FLURAZEPAM 15MG C 00140-0065-14 03/04 102322\$ 2/000000113596 W RT AC/R

cannot be Resubmitted if the secondary claim is payable.

Please reverse the secondary claim first.

61. The user can enter Y or N to the “ARE YOU SURE?” prompt. If Y, the claim resubmission process will continue.

Example 5.11-4: Entering Yes to “Are You Sure” Prompt

You've chosen to RESUBMIT the following prescription for ECMEpatient, One

1.2 LIDOCAINE 0.5% W/ 00186-0140-01 07/09 100704\$ 1/000000000623 W RT AC/N

ARE YOU SURE? (Y/N)? No// YES

62. The user can edit the Pharmacy Relationship Code, Pharmacy Person Code, Prior Authorization Number, Prior Authorization Type Code, up to three Submission Clarification Codes (if the conditions explained above are not met), Date of Service, Patient Residence Code, Pharmacy Service Type Code and/or Delay Reason Code.

Example 5.11-5: Editing Prompts

Pharmacy Relationship Code: \<Enter\>

Pharmacy Person Code: 23

Prior Authorization Number: 00000000000//

Prior Authorization Type Code: 0// NOT SPECIFIED

Submission Clarification Code 1: 5// THERAPY CHANGE

Submission Clarification Code 2:

Select one of the following:

1\. 01/19/2010 Current Date of Service

2\. 01/19/2010 Fill Date

3\. 01/20/2010 Release Date

Date of Service: 1//2 01/19/2010 Fill Date

Patient Residence Code: 1// HOME

Pharmacy Service Type Code: 1// RETAIL

Delay Reason Code:

The Resubmit with Edits (RED) option will display the information that will be used to populate the Coordination of Benefit fields in the secondary claim. If any of the information is missing, the user will be required to edit the secondary claim information. If all the information is present, the user is given the option to edit the data that will be sent on the secondary claim. The user will also be able to enter the rate type for the secondary claim.

Example 5.11-6: Entering the secondary claim information with payment information

Data for Secondary Claim

------------------------

Insurance: ECME INSURANCE2 COB: SECONDARY

Rate Type: REIMBURSABLE INS.

Other Coverage Code: 02 (OTHER COVERAGE EXISTS - PAYMENT COLLECTED)

Other Payer Coverage Type: 01 (PRIMARY)

Other Payer ID Qualifier: 03 (BANK INFORMATION NUMBER (BIN))

Other Payer ID: 123456

Other Payer Date: Jun 28, 2010

Other Payer Paid Qualifier: 08 (SUM OF ALL REIMBURSEMENT)

Other Payer Amount Paid: 40.00

Do you want to edit this Secondary Claim Information (Y/N)? N// y YES

Insurance COB Subscriber ID Group Holder Effective Expires

============= ==== ============= ========== ======== ========== ==========

1 ECME INSURAN PRI 12340987 T-GROUP1 PATIENT 10/20/2006 06/00/2011

2 ECME INSURAN SEC D-GROUP1 PATIENT 07/09/2006 06/00/2011

SECONDARY INSURANCE POLICY: 2// ECME INSURANCE1 (SECONDARY) - D-GROUP1

SELECT RATE TYPE: REIMBURSABLE INS.// Who's Responsible: INSURER

OTHER COVERAGE CODE: 02// OTHER COVERAGE EXISTS - PAYMENT COLLECTED

OTHER PAYER ID: 123456//

OTHER PAYER DATE: Jun 28, 2010//

Edit Paid Amounts or Reject Codes (PAID AMOUNTS/REJECT CODES): PAID AMOUNTS//

OTHER PAYER AMOUNT PAID QUALIFIER: 08// SUM OF ALL REIMBURSEMENT

OTHER PAYER AMOUNT PAID: (0-999999): 40.00// 40.00

OTHER PAYER PATIENT RESPONSIBILITY AMOUNT QUALIFIER: 06 (AMT REPORTED BY PRIOR PAYER)

OTHER PAYER PATIENT RESPONSIBILITY AMOUNT: 12.38

Example 5.11-7: Entering the Secondary Claim Information with Reject Information

Data for Secondary Claim

------------------------

Insurance: DAVE INSURANCE COB: SECONDARY

Rate Type: REIMBURSABLE INS.

Other Coverage Code: 03 (OTHER COVERAGE EXISTS - THIS CLAIM NOT COVERED)

Other Payer Coverage Type: 01 (PRIMARY)

Other Payer ID Qualifier: 03 (BANK INFORMATION NUMBER (BIN))

Other Payer ID: 610459

Other Payer Date: Aug 16, 2010

Other Payer Reject Code: 34:M/I Submission Clarification Code

Other Payer Reject Code: 07:M/I Cardholder ID

Other Payer Reject Code: JE:M/I Percentage Sales Tax Basis Submitted

Do you want to edit this Secondary Claim Information (Y/N)? N// y YES

Insurance COB Subscriber ID Group Holder Effective Expires

============= ==== ============= ========== ======== ========== =========

1 DAVE INSURANC SEC SI32432 D-GROUP1 PATIENT 05/09/2007

SECONDARY INSURANCE POLICY: 1// DAVE INSURANCE (SECONDARY) - D-GROUP1

SELECT RATE TYPE: REIMBURSABLE INS.// Who's Responsible: INSURER

OTHER COVERAGE CODE: 03// OTHER COVERAGE EXISTS - THIS CLAIM NOT COVERED

OTHER PAYER ID: 610459//

OTHER PAYER DATE: Aug 16, 2010//

Edit Paid Amounts or Reject Codes (PAID AMOUNTS/REJECT CODES): REJECT CODES//

OTHER PAYER REJECT CODE: 34// M/I Submission Clarification Code

OTHER PAYER REJECT CODE: 07// M/I Cardholder ID

OTHER PAYER REJECT CODE: JE// M/I Percentage Sales Tax Basis Submitted

OTHER PAYER REJECT CODE:

The Resubmit with Edits (RED) option will prompt if the claim is correct and if the claim should be submitted to the third party insurance. If the user answers 'Yes' to both prompts, the claim will be submitted. If the user chooses “No”, the action will be cancelled.

Example 5.11-8: Answering “Is the Claim Correct?” Prompt

IS THIS CLAIM CORRECT?(Y/N)? Y// ES

SUBMIT CLAIM TO ECME INSURANCE1 ?(Y/N)? Y// ES

Veteran Prescription 103689 successfully submitted to ECME for claim generation.

Example 5.11-9: Answering “Are You Sure?” Prompt

Are you sure?(Y/N)? YES

Veteran Prescription 100003433A successfully submitted to ECME for claim generation.

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Waiting for packet build

IN PROGRESS-Packet being built

IN PROGRESS-Transmitting

E PAYABLE

Veteran Prescription 100003433A successfully submitted to ECME for claim generation.

1 claim has been resubmitted.

Enter RETURN to continue or '^' to exit: \<Enter\>

Updating screen for resubmitted claim...

## OPECC Reject Information (Hidden Action)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *OPECC Reject Information* hidden action allows the user to view details associated with a rejected claim. This action is only available for claims with open rejections and non-billable prescriptions with pseudo-rejections of eC or eT.

Access the action by entering REJ at the “Select Action:” prompt on the ECME User Screen.

Example 5.12-1: Accessing and Executing the OPECC Reject Information Action

PHARMACY ECME Aug 10, 2005@10:31:22 Page: 18 of 42

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Patient Name

+# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

7 ECMEpatient,One (XXXX) WEBMD TE/ VET ALL payable

7.1 PREDNISONE 1MG TA 00242074475 09/16 100803 0/000000111872 W RS AC/N

09/10/15 – The comment goes here.

(USER, ONE)

p-Rejected

79:Refill Too Soon

\+ Enter ?? for more actions

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen// REJ REJ OPECC Reject Information

1.  The user will see the following message, when attempting to select a claim with no rejection.

Example 5.12-2: Entering the Line Item for a Claim with No Rejection

This claim is not a valid selection for the OPECC Reject Information screen.

This screen is for either rejected claims or non-billable claims.

Enter RETURN to continue or '^' to exit:

63. The user is prompted for the line item of the rejected claim or non-billable prescription entry.

Example 5.12-3: Entering the Line Item for the OPECC Reject Information Action

Select Action: Next Screen// REJ REJ OPECC Reject Information

Select item: 7.1

64. The OPECC Reject Information Screen displays.

Example 5.12-4: OPECC Reject Information Screen Display

OPECC Reject Information Oct 28, 2015@14:45:42 Page: 1 of 3

Division : XXXXXX NPI: 1110099999 NCPDP: 5310000XX TAX ID: XX-XXXXXXX

Patient : PATIENT,ONE(XXXP) Sex: M DOB: JUL XX,19XX(XX)

Rx# : 100XXX/0 ECME#: 000000111872 Date of Service: Sep 16, 2015

Drug : PREDNISONE 1MG TAB NDC Code: 00242-0744-75

REJECT Information (Veteran) RESUBMISSION

Current ECME Status: E REJECTED

Rejects received from Payer on 09/16/2015 5:26:39 pm.

Code Description

79 - Refill Too Soon

Next Avail Fill: 10/31/2015

Payer Message : EMD 1000: CLAIM PAID

Payer Addl Msg : EMD 1000: CLAIM PAID RX:00000010XXXFILL:2015-09-16

BIN:610144 PCN:TEST

OPECC COMMENTS

\- 09/10/15 5:17 pm – First comment for OPECC screen (USER,ONE)

PHARMACIST COMMENTS

\- 05/12/15 8:23 am – Second comment for Pharmacist (USER,TWO)

INSURANCE Information

Insurance : VET CNF

Contact : 333-444-5555

BIN : 610144

PCN : TEST

Group Number : 246

Cardholder ID : 1234567890

Effective Date : 01/25/2015

65. There are four actions available from the OPECC Reject Information screen: VW View Rx, VER View ECME Rx, MP Med Profile, and PI Pat Info.

Example 5.12-5: Actions Available from the OPECC Reject Information Screen

\+ Enter ?? for more actions

VW View Rx VER View ECME Rx MP Med Profile PI Pat Info

Select: Next Screen//

## Resubmit Claim Without Reversal (Hidden Action)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Resubmit Claim w/o Reversal* action resubmits a claim to the insurer without submitting a reversal first, regardless of the VistA claim status. This action should be used in instances where the payer shows the claim was reversed and VistA shows a payable claim. This action is not available if any non-cancelled bill exists.

The action is accessed by entering RER at the “Select Action:” prompt on the ECME User Screen.

Example 5.13-1: Accessing and Executing the Resubmit Claim W/O Reversal Action

Select Action: Next Screen// RER RER Resubmit Claim w/o Reversal

1.  The user is prompted for the line item(s) of the claim to be resubmitted.
11. The user may also submit multiple line items separated by commas (e.g. “1.1,1.2”), or a range of line items separated by a hyphen (e.g. “1.1-1.3”).

Example 5.13-2: Entering the Line Item for the Claim Resubmission Request

> **NOTE:** This action will resubmit claims without performing a reversal.

This action should be used in instances where the payer shows the

claim was reversed and VistA shows a payable claim. This action will

NOT submit a reversal regardless of the current VistA claim status.

Enter the line numbers for the claim(s) to be resubmitted w/o reversal.

Select item(s):

66. The system redisplays the line item for resubmission, then asks are sure you want to continue with the transaction. Enter Y or N. If Y, the claim resubmission process continues.

Example 5.13-5: Entering “Y” to Continue Claim Resubmission Request

You've chosen to RESUBMIT W/O REVERSAL the following Rx for PATIENT,TWO

1.4 PREDNISONE 1MG TA 00242074475 10/28 100XXX 0/000000112XXX W RT AC/N

Are you sure?(Y/N)? YES

67. ECME will allow multiple submissions of the same prescription and fill to be placed on the request queue at the same time. The ECME engine will process all requests in the order that they are received. If there is already a submission in the queue for this prescription and fill, a message is displayed and asks if you want to proceed.

Example 5.13-6: Entering “Y” to Place Multiple Submissions in the Queue

The claim is in progress. The request will be scheduled and processed after the previous request(s) are completed. Please be aware that the result of the resubmit depends on the payer's response to the prior incomplete requests.

Do you want to proceed?(Y/N)? y YES

68. The claim resubmission request is submitted, and the progress is displayed.

Example 5.13-7: Displaying a Successfully Resubmitted Claim

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Building the claim

IN PROGRESS-Transmitting

E PAYABLE

Veteran Prescription 100958 successfully submitted to ECME for claim generation.

1 claim has been resubmitted.

Enter RETURN to continue or '^' to exit: \<ENTER\>

Updating screen for resubmitted claims...

69. The line item will display the status of a claim that was resubmitted and the Bill Type indicator of “RS.” The “RS” indicates a resubmitted claim. The resubmit indicator will also display for a non-billable prescription that has been resubmitted, even if there is no claim because the prescription remained non-billable.

Example 5.13-8: Displaying the Claim Status after a Resubmission

PHARMACY ECME Oct 28, 2015@16:29:32 Page: 2 of 52

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 999 day(s)

Sorted by: Transaction date by default

+# PATIENT/DRUG/COMMENTS INSURANCE/NDC/DOS/RX#/ECME# STATUS/LOC/TYP/RXINF

1.4 PREDNISONE 1MG TA 00242074475 10/28 100XXX 0/000000112XXX W RS AC/N

p-Payable

## Open / Close Non-Billable Entry (Hidden Action)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Open / Close Non-Billable Entry action marks a non-billable entry as open or closed. The action only applies to non-billable entries, not claims that have been submitted to a third party payer.

The action behaves like a toggle. If the entry is currently Open and the action is selected, the user will Close the entry. If the entry is currently Closed and the action is selected, the user will Open the entry.

The action is accessed by entering OCN at the “Select Action:” prompt on the ECME User Screen.

Example 5.14-1: Accessing and Executing the Open / Close Non-Billable Entry Action

Select Action: Next Screen// OCN OCN Open/Close Non-Billable Entry

1.  The user is prompted for the line item(s) of the claim to be opened or closed.

Example 5.14-2: Entering the Line Item for the Open / Close Non-Billable Entry

Enter the line number for the entry to be opened or closed.

Select item:

70. The system redisplays the line item for resubmission, then prompts for a comment. Next the system asks if the user is sure. Enter Y or N. If Y, the entry is marked as Open or Closed.

Example 5.14-5: Answer Prompts for Open / Close Non-Billable Entry

You've chosen to CLOSE the following entry for

PATIENT,ONE :

3.1 MILK OF MAGNESIA 00349821742 100SSS 0/ W RS EX/N

p-Non-Billable/Open

eT:TRICARE-RX NOT BILLABLE (DRUG NOT BILLABLE)

The Selected Entry will be CLOSED.

Comment : Enter a comment now

Are you sure? (Y/N)? YES

Closing Entry

Enter RETURN to continue or '^' to exit:

## Display Update (Hidden Action)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Display Update* action revises the ECME User Screen with the latest information about the status of patients’ prescriptions using the current filter settings. This action updates the ECME User Screen only once.

This hidden action is accessed by entering UD at the “Select Action:” prompt on the ECME User Screen.

Example 5.15-1: Accessing the Display Update Action

PHARMACY ECME Apr 26, 2006@11:44:45 Page: 1 of 2

SELECTED DIVISION(S): ALL

Transmitted by ALL users Activity Date Range: within the past 10 day(s)

Sorted by: Patient Name

\# PATIENT/DRUG/COMMENTS INSURANCE/NDC/RX#/ECME# LOC/TYP RXINF

6 ECMEpatient,Two (XXXX) WEBMD TE/ VET Pb:1 Rj:0 AcRv:0 RjRv:1

6.1 FUROSEMIDE 10MG/M 00641-2312-25 04/22 100004065\$ 0/000000504691 W RT AC/R

p-Payable

6.2 CHOLESTYRAMINE 4G 00087-0580-01 04/22 100004066\$ 0/000000504692 W RT AC/R

p-Reversal rejected

NN:Transaction Rejected At Switch Or Intermediary

NC16-The clearinghouse did not reply in time.

7 ECMEpatient,One (XXXX) WEBMD TE/ VET ALL payable

7.1 ALBUTEROL INHALER 55555-4444-22 04/26 100003744\$ 0/000000504304 W RT AC/R

p-Payable

7.2 ACETYLCYSTEINE 20 00087-0570-09 04/21 100004054\$ 0/000000504677 W RT AC/N

s-Payable (p-Payable)

8 ECMEpatient,Three (XXXX) WEBMD TE/ VET ALL payable

\+ Enter ?? for more actions

The screen has been updated on APR 26,2006@14:50:47. Press "Q" to quit.

CV Change View REV Reverse Payable Claim FR Further Research

SO Sort List RES Resubmit Claim VER View ePharmacy Rx

CMT Add/View Comments CLO Close Claim WRK Send to Worklist

Select Action: Next Screen// UD Display Update

Updating screen.

## Exit (From ECME User Screen)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When EXIT or QUIT is entered at the “Select Action:” prompt, the system will return the user to the *ECME Main Menu*.

# Accessing the ECME Pharmacy COB Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *ECME Pharmacy COB Menu* option allows users to manually send claims to secondary insurance companies; generate primary claims for patients with dual eligibility; and view reports that support secondary billing and primary billing for TRICARE patients.

Example 6-1: Accessing the ECME Pharmacy COB Menu

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXXX VAMC \*

\* Main Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

U ECME User Screen

COB ECME Pharmacy COB ...

MGR Pharmacy ECME Manager Menu ...

RPT Pharmacy Electronic Claims Reports ...

Select ECME Option: MGR Pharmacy ECME Manager Menu

Example 6-2: Displaying the ECME Pharmacy COB Menu

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXXXX VAMC \*

\* Pharmacy ECME Manager Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

SEC Potential Secondary Rx Claims Report

TRI Potential Claims Report for Dual Eligible

PRO Process Secondary/TRICARE Rx to ECME

Select ECME Pharmacy COB Option:

## Potential Secondary Rx Claims Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Potential Secondary Rx Claims Report* is designed to help the OPECC (Outpatient Pharmacy Electronic Claims Coordinator) to identify potential Rx claims for a secondary insurance payer with pharmacy coverage, including both electronic and paper. This report will include prescription claims where the primary claim is payable, or the primary claims has been rejected and closed. Below are some scenarios where a claim will not appear on the report:

- A prescription where the secondary claim is closed in ECME.
- A prescription where the secondary claim is payable in ECME.
- A prescription where the primary payer paid the full amount as there is no more revenue to collect from any other payers.

If a claim is determined to be electronically billable, the OPECC accomplishes this through the *Process Secondary / TRICARE Rx to ECME option.* If the claim must be billed in paper format, the OPECC follows the current procedures for initiating a secondary bill with the billing staff.

1.  Access the Potential Secondary Rx Claims Report by entering SEC at the “ECME Pharmacy COB Option:” prompt on the ECME Pharmacy COB Menu.

Example 6.1-1: Accessing the Potential Secondary Rx Claims Report

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXXX VAMC \*

\* Pharmacy Electronic Claims Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

SEC Potential Secondary Rx Claims Report

TRI Potential Claims Report for Dual Eligible

PRO Process Secondary/TRICARE Rx to ECME

Select ECME Pharmacy COB Option: SEC Potential Secondary Rx Claims Report

71. After the user has selected one, many, or all divisions and a date range, choose the primary (required) and secondary (optional) sort criteria.

Example 6.1-2: Generating the Potential Secondary Rx Claims Report

SELECTION CRITERIA

Select one of the following:

D DIVISION

A ALL

Select Certain Pharmacy (D)ivisions or (A)LL: ALL

EARLIEST DATE: t (APR 14, 2009)

LATEST DATE: T// \<ENTER\> (APR 14, 2009)

SORT CRITERIA

Primary Sort: (N/P/S/D): Division// ??

Enter a code from the list to indicate the Primary sort order.

Select one of the following:

N Patient Name

P Payer

S Date Of Service

D Division

Primary Sort: (N/P/S/D): Division// \<ENTER\>

Secondary Sort: (N/P/S): \<ENTER\>

Tertiary Sort: (N/P/S): \<ENTER\>

Do you want to capture report data for an Excel document? NO// YES

Before continuing, please set up your terminal to capture the

detail report data and save the detail report data in a text file

to a local drive. This report may take a while to run.

> **NOTE:** To avoid undesired wrapping of the data saved to the file,

please enter '0;256;99999' at the 'DEVICE:' prompt.

DEVICE: HOME// 0;256;99999

Collecting Potential Secondary data.

Enter RETURN to continue or '^' to exit: \<ENTER\>

=======================================================================

Potential Secondary Rx Claims Report 4/14/09 - 4/14/09 Page: 1

Selected Divisions: ALL

Sorted By: Division;

Bill# RX# Fill Patient PatID COB Date Payers

-------------------------------------------------------------------------------

Division: XXXXXX

K9000LG 102179 4 ECMEpatient,One 0000 p 4/14/09 ECME INSURANCE1

t ECME INSURANCE2

K0000QD 2055862 0 ECMEpatient,One 0000 p 7/13/10 ECME INSURANCE1

s ECME INSURANCE2

\- ECME INSURANCE3

\(P\) Rej 2055865 0 ECMEpatient,One 0000 p 7/13/10 ECME INSURANCE1

s ECME INSURANCE2

t ECME INSURANCE3

\(P\) Rej 2055866 0 ECMEpatient,Two 4444 p 7/14/10 ECME INSURANCE1

s ECME INSURANCE2

Bill# "(P) Rej" indicates a rejected/closed primary ECME claim

COB "-" indicates a blank COB field in the pt. ins. policy

## Potential Claims Report for Dual Eligible

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Potential Claims Report for Dual Eligible* attempts to identify potential pharmacy claims for TRICARE and CHAMPVA payers. This report includes prescriptions that have been released but have not yet been billed for any patient with dual eligibility (e.g. Veteran, CHAMPVA and TRICARE) who has an active insurance plan with pharmacy coverage and a Type of Plan of TRICARE or CHAMPVA. If the Claims Tracking entry for the specific prescription / fill is identified as being non-billable, then it will not appear on this report.

If a claim is determined to be electronically billable, the OPECC can submit the prescription through the [Process Secondary / TRICARE Rx to ECME option](#process-secondary-tricare-rx-to-ecme).

1.  Access the *Potential Claims Report* for Dual Eligible by entering TRI at the “ECME Pharmacy COB Option:” prompt on the ECME Pharmacy COB Menu.

Example 6.2-1: Accessing the Potential Claims Report for Dual Eligible

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Pharmacy Electronic Claims Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

SEC Potential Secondary Rx Claims Report

TRI Potential Claims Report for Dual Eligible

PRO Process Secondary/TRICARE Rx to ECME

Select ECME Pharmacy COB Option: TRI Potential Claims Report for Dual Eligible

72. After the user has selected one, many, or all divisions, the patient eligibility criteria (TRICARE, CHAMPVA or all) and a date range, choose the primary (required) and secondary (optional) sort criteria.

Example 6.2-2: Generating the Potential TRICARE Claims Report

Select one of the following:

D DIVISION

A ALL

Select Certain Pharmacy (D)ivisions or (A)LL: ALL

Select one of the following:

T TRICARE

C CHAMPVA

A ALL

Display (T)RICARE or (C)HAMPVA or (A)LL Entries: A// LL

EARLIEST DATE: t-10 (APR 06, 2009)

LATEST DATE: T// (APR 16, 2009)

SORT CRITERIA

Primary Sort: (N/P/S/D/E): Division//

Secondary Sort: (N/P/S/E):

Tertiary Sort: (N/P/S/E):

DEVICE: HOME// ;;9999 TELNET TERMINAL

Collecting TRICARE data.

Enter RETURN to continue or '^' to exit:

=======================================================================

Potential TRICARE Rx Claims Report 8/1/80 - 7/28/14 Page: 1

Selected Divisions: ALL

Selected Patient Eligibility: ALL

Sorted By: Division;

'\*' indicates the HPID/OEID failed validation checks

RX# Fill Date Patient PatID COB Elig Payers HPID/OEID

-----------------------------------------------------------------------

Division: XXXXX VAMC

100407 2 9/9/10 OPTRICARE,ONE 160P p TRIC TRICARE-23 TEST 6999999999\*

100408 1 9/9/10 OPTRICARE,ONE 160P p TRIC TRICARE-23 TEST 6999999999\*

## Process Secondary / TRICARE Rx to ECME

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Process Secondary / TRICARE Rx to ECME option allows the OPECC to submit claims for prescriptions / refills that were entered for Secondary claims, TRICARE patients or patients with dual eligibility (e.g. Veteran and TRICARE). These claims are identified using the Potential Secondary Rx Claims Report and Potential Claims Report for Dual Eligible.

This option submits the claim to the third party payer. Any further processing on the claim must then be done through the actions available on the ECME User Screen.

When processing a claim for TRICARE, CHAMPVA and dual eligibility patients, users will be asked for the patient’s name, the fill / refill number from the list provided, and an appropriate billing Rate Type. If the user selects a CHAMPVA Rate Type (CHAMPVA or CHAMPVA REIMB. INS.), the claim will be processed as a CHAMPVA claim. If the user selects a TRICARE Rate Type (TRICARE or TRICARE REIMB. INS.), the claim will be processed as a TRICARE claim. If the user selects a Reimbursable Insurance type, it will be processed as a regular non-TRICARE and non-CHAMPVA claim. The Date of Service is determined based on the date of service algorithm used in Outpatient Pharmacy.

Claims can also be resubmitted using the Process Secondary / TRICARE RX to ECME option. Secondary Claims that are rejected by insurance companies because of missing or incorrect data received, or Primary Claims that have been rejected or reversed, may be resubmitted. This option is not intended to use for Payable claims. Payable claims must be reversed using the Reverse Payable Claim Action on the ECME User Screen before they can be resubmitted via this option. Information previously entered for the claim will appear as the defaults.

Key The user must hold the BPSUSER key to use the Process Secondary / TRICARE Rx to ECME option.

1.  Access the Process Secondary / TRICARE Rx to ECME option by entering PRO at the “ECME Pharmacy COB Option:” prompt on the ECME Pharmacy COB Menu.

Example 6.3-1: Accessing the Process Secondary / TRICARE Rx to ECME Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXXX VAMC \*

\* Pharmacy Electronic Claims Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

SEC Potential Secondary Rx Claims Report

TRI Potential Claims Report for Dual Eligible

PRO Process Secondary/TRICARE Rx to ECME

Select ECME Pharmacy COB Option: PRO Process Secondary/TRICARE Rx to ECME

### Submitting Secondary Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The Process Secondary / TRICARE Rx to ECME (PRO) option will prompt for a Rx#.
2.  The Process Secondary / TRICARE Rx to ECME (PRO) option will display the Rx information to allow the user to ensure the correct Rx# was entered and prompt the user to confirm they wish to continue.
3.  The Process Secondary / TRICARE Rx to ECME (PRO) option will ask the user to select a fill / refill from the list provided by the software.
4.  The Process Secondary / TRICARE Rx to ECME (PRO) option will ask the user to select the Payer Sequence to bill (primary or secondary).
5.  The Process Secondary / TRICARE Rx to ECME (PRO) option will ask the user if they wish to edit the insurance company data. If the user enters YES to this prompt, they will be able to edit the user's insurance via the Patient Insurance Information Screen.

Example 6.3.1-1: Initial Prompts for the Process Secondary / TRICARE Rx to ECME Option

Select PRESCRIPTION RX \#: 10030 LIDOCAINE 0.5% W/EPI INJ MDV

Patient RX# Drug Name RX Status

ECMEPatient, Two 10030 LIDOCAINE 0.5% W/EPI INJ ACTIVE

DO YOU WANT TO CONTINUE?(Y/N)? Y// ES

RX \#10030 has the following fills:

Fill Date

==== ==========

0 07/02/2010

1 10/12/2010

SELECT A FILL TO BILL: 07/02/2010

Select payer sequence for billing:

1 PRIMARY

2 SECONDARY

SELECT PAYER SEQUENCE: 2 SECONDARY

Drug name NDC Date RX# REF# TYPE STATUS

=======================================================================

LIDOCAINE 0. 00186014001 09/10 10030\$ 0/0003098 W RT \*\*/R REJECTED

There is an existing rejected/reversed secondary e-claim(s) for the RX/refill.

Do you want to submit a new secondary claim(Y/N)? N// YES

DO YOU WISH TO ADD/EDIT INSURANCE COMPANY DATA FOR THIS PATIENT?(Y/N)? N// O

Data for Secondary Claim

------------------------

Insurance: INSURANCE3 COB: SECONDARY

Rate Type: REIMBURSABLE INS.

Other Coverage Code: 02 (OTHER COVERAGE EXISTS - PAYMENT COLLECTED)

Other Payer Coverage Type: 01 (PRIMARY)

Other Payer ID Qualifier: 03 (BANK INFORMATION NUMBER (BIN))

Other Payer ID: 123456

Other Payer Date: Oct 15, 2010

Other Payer Paid Qualifier: 07 (DRUG BENEFIT)

Other Payer Amount Paid: 40.00

Other Payer Patient Responsibility Amount Qualifier: 06 (AMT REPORTED BY PRIOR PAYER)

Other Payer Patient Responsibility Amount: \$12.38

Do you want to edit this Secondary Claim Information (Y/N)? N// YES

Insurance COB Subscriber ID Group Holder Effective Expires

============= ==== ============= ========== ======== ========== =========

1 INSURANC2 PRI AAA INS. PATIENT 03/10/2010

2 INSURAN3 SEC 54873579430 GR PATIENT 03/26/2010

SECONDARY INSURANCE POLICY: 2// INSURANCE3 (SECONDARY) - BRIAN'S GRP

SELECT RATE TYPE: REIMBURSABLE INS.// Who's Responsible: INSURER

OTHER COVERAGE CODE: 02// OTHER COVERAGE EXISTS - PAYMENT COLLECTED

OTHER PAYER ID: 123456//

OTHER PAYER DATE: Oct 15, 2010//

Edit Paid Amounts or Reject Codes (PAID AMOUNTS/REJECT CODES): PAID AMOUNTS//

OTHER PAYER AMOUNT PAID QUALIFIER: 07// DRUG BENEFIT

OTHER PAYER AMOUNT PAID: (0-999999): 40.00//

OTHER PAYER AMOUNT PAID QUALIFIER:

SUBMIT CLAIM TO INSURANCE3 ?(Y/N)? Y// ES

Veteran Prescription 10030 successfully submitted to ECME for claim generation.

Processing Secondary claim...

Claim Status:

IN PROGRESS-Building the claim

IN PROGRESS-Building the HL7 packet

IN PROGRESS-Transmitting

E PAYABLE

### Submitting Primary Claims for TRICARE and Dual Eligibility Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section shows an example of how the option can be used to submit claims for prescriptions / refills entered for TRICARE patients or patients with dual eligibility (e.g. Veteran and TRICARE) and that were identified by the Potential Claims Report for Dual Eligible.

When processing a claim for TRICARE and dual eligibility patients, users are asked for patient’s name and the fill / refill from the list provided by the software.

Example 6.3.2-1: Prompt for the Process Secondary / TRICARE Rx to ECME Option

Select ECME Pharmacy COB Option: PRO Process Secondary/ TRICARE Rx to ECME

Select PRESCRIPTION RX \#: 103027 BETHANECHOL 10MG TAB

Patient RX# Drug Name RX Status

ECMEpatient,One 103027 BETHANECHOL 10MG TAB ACTIVE

DO YOU WANT TO CONTINUE?(Y/N)? Y// ES

RX \#103027 has the following fills:

Fill Date

==== ==========

0 10/27/2009

SELECT A FILL TO BILL: 0 10/27/2009

Select payer sequence for billing:

1 PRIMARY

2 SECONDARY

SELECT PAYER SEQUENCE: 1 PRIMARY

SELECT RATE TYPE: 40 TRICARE PHARMACY Who's Responsible: INSURER

DO YOU WISH TO ADD/EDIT INSURANCE COMPANY DATA FOR THIS PATIENT?(Y/N)? N// NO

Insurance COB Subscriber ID Group Holder Effective Expires

============== ==== ============= ========== ========= ========== ==========

EXPRESS SCRIP PRI XXXXXX DODA PATIENT 12/27/2008

PRIMARY INSURANCE POLICY: SH TRICARE (PRIMARY) - TRICARE PLAN

SUBMIT CLAIM TO SH TRICARE ?(Y/N)? Y// y YES

TRICARE Prescription 2055242 submitted to ECME for claim generation.

### SC Prescriptions for Active Duty Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section shows an example of how the option can be used to submit claims for prescriptions / refills entered for patients with TRICARE dual eligibility (e.g. Veteran and TRICARE) with SC prescriptions.

The prescription must be marked as related to an Environmental Indicator / Special Authority and must be one of the following:

SC TREATMENT

AGENT ORANGE

IONIZING RADIATION

SOUTHWEST ASIA

MILITARY SEXUAL TRAUMA

COMBAT VETERAN

When processing a claim for TRICARE dual eligibility patients that have one of the above Environmental Indicator / Special Authority codes, users are asked to verify that the patient was active duty on the date of service and to enter an Electronic Signature code.

Example 6.3.3-1: Prompt for the Process Secondary / TRICARE Rx to ECME Option

Select ECME Pharmacy COB Option: PRO Process Secondary/ TRICARE Rx to ECME

Select PRESCRIPTION RX \#: 9999999 BETHANECHOL 10MG TAB

Patient RX# Drug Name RX Status

ECMEpatient,One 9999999 BETHANECHOL 10MG TAB ACTIVE

DO YOU WANT TO CONTINUE?(Y/N)? Y// ES

RX \#103027 has the following fills:

Fill Date

==== ==========

0 10/27/2020

SELECT A FILL TO BILL: 0 10/27/2020

Select payer sequence for billing:

1 PRIMARY

2 SECONDARY

SELECT PAYER SEQUENCE: 1 PRIMARY

SELECT RATE TYPE: 40 TRICARE PHARMACY Who’s Responsible: INSURER

DO YOU WISH TO ADD/EDIT INSURANCE COMPANY DATA FOR THIS PATIENT?(Y/N)? N// NO

Insurance COB Subscriber ID Group Holder Effective Expires

============== ==== ============= ========== ========= ========== ==========

EXPRESS SCRIP PRI XXXXXX DODA PATIENT 12/27/2018

PRIMARY INSURANCE POLICY: SH TRICARE (PRIMARY) - TRICARE PLAN

SUBMIT CLAIM TO SH TRICARE ?(Y/N)? Y// y YES

Was the patient Active Duty on 10/27/2020? No// YES

Enter your Current Signature Code: SIGNATURE VERIFIED

Veteran Prescription 9999999 successfully submitted to ECME for claim generation.

# Accessing the Pharmacy ECME Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Pharmacy ECME Manager Menu* option allows Automated Data Processing Application Coordinators (ADPAC) and Information Resources Management Service (IRMS) to configure the Electronic Claims Management Engine (ECME) system with pharmacy site-specific options. It is accessed by entering MGR at the “Select ECME Option:” prompt on the ECME Main Menu option.

Key The user must hold the BPS MANAGER key to view the Pharmacy ECME Manager Menu option.

Example 7-1: Accessing the Pharmacy ECME Manager Menu Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXXX VAMC \*

\* Main Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

U ECME User Screen

COB ECME Pharmacy COB ...

MGR Pharmacy ECME Manager Menu ...

RPT Pharmacy Electronic Claims Reports ...

Select ECME Option: MGR Pharmacy ECME Manager Menu

Example 7-2: Displaying Pharmacy ECME Manager Menu Options

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXXXX VAMC \*

\* Pharmacy ECME Manager Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

MNT ECME transaction maintenance options ...

SET Pharmacy ECME Setup Menu ...

STAT Statistics Screen

Select Pharmacy ECME Manager Menu Option:

## ECME Transaction Maintenance Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides functionality that provides unique programmatic solutions to address ECME processing requirements. The only option identified so far is the functionality to unstrand claims.

Example 7.1-1: Accessing the ECME Transaction Maintenance Options

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Pharmacy ECME Manager Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

MNT ECME transaction maintenance options ...

SET Pharmacy ECME Setup Menu ...

STAT Statistics Screen

Key The user must hold the BPSMENU and BPS MANAGER keys to view the Statistics Screen (STAT) and ECME transaction maintenance options (MNT) options. Also, hold the BPS MASTER key to view the Edit Basic ECME Parameters (BAS), the Edit ECME Pharmacy Data (PHAR), the Register Pharmacy with Austin Information Technology Center (REG), and the Pharmacy ECME Setup Menu (SET) options.

Select Pharmacy ECME Manager Menu Option: MNT ECME transaction maintenance options

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* Electronic Claims Management Engine (ECME) v1.0 \*

\* XXXXX VAMC \*

\* BPS MENU MAINTENANCE \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

UNS View/Unstrand Submissions Not Completed

ROC Re Open CLOSED Claim

Select ECME transaction maintenance options Option:

### View / Unstrand Submissions Not Completed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides the user with options to override any current transmission status of claims that have not reached the point of completion to a status of “Done.”

When a claim is unstranded via this option, the status of the claim is changed to ‘E UNSTRANDED’ for billing requests and ‘E REVERSAL UNSTRANDED’ for reversals. This status message is displayed on the ECME User Screen, the Further Research menu, the Developer Log action of the ECME user screen, and the Recent Transaction report.

12. Even though the user performs the View / Unstrand Submissions Not Completed option, the final adjudicating payer claim status of either 'Payable' or 'Rejected' will not be known unless further action is taken on the claim. This will require manual intervention for the claim to be resubmitted to the adjudicating payer after this option is run.
1.  Enter UNS at the “Select ECME transaction maintenance options Option:” to access the unstrand options.

Example 7.1.1-1: Accessing the View / Unstrand Submissions Not Completed Option

UNS View/Unstrand Submissions Not Completed

ROC Re Open CLOSED Claim

Select ECME transaction maintenance options Option: UNS View/Unstrand Submissions Not Completed

Please be aware that if there are submissions appearing on the ECME User Screen

with a status of 'In progress - Transmitting', then there may be a problem

with HL7 or with system connectivity with the Austin Automation Center (AAC).

Please contact your IRM to verify that connectivity to the AAC is working

and the HL7 link BPS NCPDP is processing messages before using this option

to unstrand submissions with a status of 'In progress - Transmitting'.

Do you want to continue? NO//

73. The user will be prompted for a date range to display all stranded claims. The system will accept a date range with or without a time attached to it.
    - First Transaction Date: If a date only is entered for a start date, the system will assume the start date is the date entered and the time will be the beginning of the 24 hour clock (.0001) otherwise the system will accept the entered time parameter.
    - Last Transaction Date: If a date only is entered for the ending date range, the system will assume the ending of a 24-hour clock (.2359), except the current date is entered. If the user enters today’s date as the ending date of the date range, the system will automatically assign the ending time to be 30 minutes prior to the current time to ensure a transmissions that may be currently processing is not interrupted.

Example 7.1.1-2: Entering Date Range for View / Unstrand Submissions Not Completed Option

FIRST TRANSACTION DATE: // T-120

LAST TRANSACTION DATE: T// T

Please wait...

Example 7.1.1-3: Displaying the View / Unstrand Submissions Not Completed Actions

ECME UNSTRAND SUBMISSIONS Oct 08, 2010@15:12:08 Page: 1 of 1

Submissions Stranded from 09/28/2010 through 10/08/2010

Sorted by Transaction Date

\## Trans DT Patient Name ID RX/Fill DOS Ins Co

\*\*\* CLAIMS \*\*\*

1 10/07/2010 ECMEpatient,One 2637 101297/1 06/24/2009 AETNA

In Progress - Done

2 10/07/2010 ECMEpatient,One 2637 101320/1 04/27/2009 AETNA

In Progress - Done

3 10/07/2010 2637 1100349/0 10/07/2010 AETNA

In Progress - Processing request

\*\*\* REVERSALS \*\*\*

4 10/07/2010 ECMEpatient,One 2637 101298/1 06/25/2009 AETNA

In Progress - Done

\*\*\* ELIGIBILITY INQUIRIES \*\*\*

5 10/08/2010 ECMEpatient,One 2637 10/08/2010 AETNA

In Progress - Parsing response

Enter ?? for more actions \>\>\>

ALL Unstrand Current Submissions PRT Print Current Submissions

SEL Select Submissions to Unstrand EX Exit

### REOPEN a CLOSED ECME Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Reopen a Closed Claim* option allows the user to reopen an electronic claim after it has been Closed. The prescription can be Released or Not Released. The user is prompted to enter a patient name and date range to select closed claims by date of service. Once a claim is Reopened, the user may resubmit the claim to the payer for payment.

1.  Enter ROC at the “Select ECME transaction maintenance options Option:” to access the Re Open CLOSED Claim option.

Example 7.1.2-1: Accessing the Re Open CLOSED Claim Option

UNS View/Unstrand Submissions Not Completed

ROC Re Open CLOSED Claim

Select ECME transaction maintenance options Option: ROC Re Open CLOSED Claim

74. The user will be prompted for a patient name.

Example 7.1.2-2: Entering Patient Name to Display Closed Claims for this Option

Select PATIENT NAME: ECMEpatient,One 6-1-60 666006666

NSC VETERAN

75. The user will be prompted for a date range for the dates of service of closed claims.

Example 7.1.2-3: Entering Dates of Service for Closed Claims Listing

START WITH DATE:TODAY//6/13/06 (Jun 13, 2006)

GO TO DATE:TODAY//T (JUL 05, 2006)

76. Enter Reopen and choose the line item of the closed claim that will be reopened.

Example 7.1.2-4: Choosing to Reopen a Closed Claim and Selecting a Line Item

REOPEN CLOSED CLAIM Jul 05, 2006@15:29:21 Page: 1 of 1

PATIENT: ECMEpatient,One (XXXX) Closed claims from 07/05/06 to 07/05/06

\# DRUG NDC DOS RX# REF/ECME# LOC RX INFO

1 RESERPINE 0.25MG 00083-0036-45 07/05 100004093\$ 0/000000504727 W RT AC/R

Enter ?? for more actions

RE Reopen Claim EX Exit

Select action: Quit// R Reopen Claim

Select item: 1

77. The user is prompted to enter a text comment, Reopen Comments, after claim information is displayed.

Example 7.1.2-5: Entering Text Comment for Reopened Closed Claim

PATIENT NAME: ECMEpatient,One RX#: 100000000\$ 0 DRUG: RESERPINE 0.25MG

CLOSED JUL 5,2006@15:13:42

ECME#: 00000504727, DOS: JUL 5,2006, RELEASE DATE: JUL 5,2006@15:12:11

PLAN: HIPPA05 INSURANCE: MEDCO

CLOSE REASON: REFILL TOO SOON

DROP TO PAPER: NO

CLOSE USER: ECMEuser,One

You have selected the CLOSED electronic claim listed above.

REOPEN COMMENTS: Claim reopened for new refill

Example 7.1.2-6: Entering Yes to “Are You Sure” Prompt

ARE YOU SURE YOU WANT TO RE-OPEN THIS CLAIM? (Y/N)? No// YES

ReOpening Claim: VA2006=1712884=000014=0006687 ... OK

1 claim has been reopened.

Enter RETURN to continue or '^' to exit:

## Pharmacy ECME Setup Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Pharmacy ECME Setup* Menu option allows the ADPAC or IRMS to configure ECME to VAMC specifications.

Key The user must hold the BPSMENU, BPS MANAGER, and BPS MASTER keys to view the Pharmacy ECME Setup Menu (SET) option.

Access the menu by entering “SET” at the “Select Pharmacy ECME Setup Menu Option:” prompt in the Pharmacy ECME Manager Menu option.

Example 7.2-1: Accessing the Pharmacy ECME Manager Menu Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXX VAMC \*

\* Pharmacy ECME Manager Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

MNT ECME transaction maintenance options ...

SET Pharmacy ECME Setup Menu ...

STAT Statistics Screen

Select Pharmacy ECME Manager Menu Option: SET Pharmacy ECME Setup Menu

Key The user must hold the BPS MASTER key to view the Edit Basic ECME Parameters (BAS), Edit ECME Pharmacy Data (PHAR), and Register Pharmacy with Austin Automation Center (REG) options.

Example 7.2-2: Pharmacy ECME Setup Menu Options

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXXXX VAMC \*

\* Pharmacy ECME Setup Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

BAS Edit Basic ECME Parameters

PHAR Edit ECME Pharmacy Data

REG Register Pharmacy with Austin Information Technology Center

Select Pharmacy ECME Setup Menu Option:

### Edit Basic ECME Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Edit Basic ECME Parameters* option allows the ADPAC or IRMS to determine how data will be input to ECME.

13. This option should not be used after the initial setup unless any of the information changes for the pharmacy.

Access the menu by entering BAS at the “Select Pharmacy ECME Setup Menu Option:” prompt in the Pharmacy ECME Setup Menu option.

Example 7.2.1-1: Accessing the Edit Basic ECME Parameters Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXXX VAMC \*

\* Pharmacy ECME Setup Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

BAS Edit Basic ECME Parameters

PHAR Edit ECME Pharmacy Data

REG Register Pharmacy with Austin Information Technology Center

Select Pharmacy ECME Setup Menu Option: BAS Edit Basic ECME Parameters

The Edit Basic ECME Parameters option allows the user to enter / edit the number of seconds that the Outpatient Pharmacy application waits for a response to come back from the third party payer. As delivered, the system will have a default timeout of 10 seconds, but it is up to each site to determine how long their pharmacists wait for a response from the payer. The ECME timeout can be populated once the system is installed. After this amount of time has passed, claims processing will continue but not display messages indicating process.

This option will prompt for the Default Eligibility Pharmacy. Once entered, this Pharmacy will be placed on the NCPDP Eligibility Verification request when it is initiated by the new option in IB.

14. One important reason for this is DUR (Drug Utilization Review) /79 rejects. If the payer indicates that there is a problem with the drug (e.g., overdose), the pharmacists will have to act on that response.

This option also allows the user to set the “Insurer Asleep” interval time and number of retries. The Insurer Asleep Interval parameter allows an input between 0 and 29 minutes with a default of 20. The Insurer Asleep Retries parameter allows an input between 0 and 99 retries with a default of 10. If either the Insurer Asleep Interval or the Insurer Asleep Retries parameter is set to 0, the functionality will be disabled. If the user does disable this functionality, any claims that are in an Insurer Asleep state will automatically be resubmitted to the payer.

Occasionally, Emdeon or the third-party payer will return a reject code indicating that the destination system is not available. As one example, the third-party payer may be down for regular system maintenance and any claims submitted during this time will be rejected. When this situation does occur, Emdeon or the third-party payer will generally return one or more of the NCPDP system processing reject codes shown in the table below. These reject codes are automatically resubmitted by ECME at the intervals specified in the “insurer asleep” parameter.

| Reject Code | Explanation                           |
|-------------|---------------------------------------|
| 90          | Host Hung Up                          |
| 91          | Host Response Error                   |
| 92          | System Unavailable / Host Unavailable |
| 95          | Time Out                              |
| 96          | Scheduled Downtime                    |
| 97          | Payer Unavailable                     |
| 98          | Connection to Payer Is Down           |

<span id="_Toc72333928" class="anchor"></span>Table 4: Description of Edit ECME Pharmacy Data Option Fields

Example 7.2.1-2: Entering Edit Basic ECME Parameters

Select Pharmacy ECME Setup Menu Option: BAS Edit Basic ECME Parameters

Edit Pharmacy ECME configuration

ECME timeout? (0 to 30 seconds): 30//

Insurer Asleep Interval (0 to 29 minutes): 5//

Insurer Asleep Retries (0 to 99): 3//

Default Eligibility Pharmacy: PHARMACY-1//

### Edit ECME Pharmacy Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Edit ECME Pharmacy Data* option enables pharmacy users to edit specific parameters that affect the electronic submission of third party prescription claims. The pharmacy site will use this option to control whether the transmission of prescriptions to the CMOP dispensing site will automatically submit electronic third party prescription claims to the insurance payers. This option is also where the pharmacy site will set the parameter of how many days will pass before a reversal is automatically processed for a non-released prescription.

Key The user must hold the BPS MASTER key to view the Edit Basic ECME Parameters (BAS), Edit ECME Pharmacy Data (PHAR), and Register Pharmacy with Austin Automation Center (REG) options.

Access the option by entering PHAR at the “Select Pharmacy ECME Manager Menu Option:” prompt in the *Pharmacy ECME Manager Menu* option.

Example 7.2.2-1: Accessing the Edit ECME Pharmacy Data Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXXX VAMC \*

\* Pharmacy ECME Setup Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

BAS Edit Basic ECME Parameters

PHAR Edit ECME Pharmacy Data

REG Register Pharmacy with Austin Information Technology Center

Select Pharmacy ECME Manager Menu Option: PHAR Edit Pharmacy ECME Pharmacy Data

Example 7.2.2-2: Entering Edit ECME Pharmacy Data Options

Select BPS PHARMACIES NAME: XXXXXX VAMC PHARMACY

NAME: XXXXXX VAMC PHARMACY

STATUS: ACTIVE

NCPDP \#: 1111111

NPI: 1234567893

Select OUTPATIENT SITE: XXXXXX VAMC PHARMACY // \<ENTER\>

OUTPATIENT SITE: XXXXXX VAMC PHARMACY // \<ENTER\>

Select OUTPATIENT SITE: \<ENTER\>

CMOP SWITCH: CMOP ON// \<ENTER\>

AUTO-REVERSE PARAMETER: 5// 5

DEFAULT DEA \#: AG12345

The following table describes the Edit ECME Pharmacy Data option fields:

| Entry                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BPS PHARMACIES NAME    | Pharmacy in a specific VAMC (Department of Veterans Affairs Medical Center) database. The pharmacy user may enter a new BPS pharmacy, which must be 3-30 alphabetical characters.                                                                                                                                                                                                                                                                                                                                                  |
| NAME                   | Display-only field that displays the full pharmacy name entered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| NCPDP \#               | A 7-digit number assigned to the specified pharmacy by the National Council for Prescription Drug Programs (NCPDP). It is also known as NABP.                                                                                                                                                                                                                                                                                                                                                                                      |
| NPI                    | National Provider Identifier. A 10-digit number required by the Health Insurance Portability and Accountability Act of 1996 (HIPAA) to identify individual and organizational providers, such as outpatient sites. The NPI has a usage requirement date beginning May 23, 2008.                                                                                                                                                                                                                                                    |
| STATUS                 | The status of the BPS Pharmacy is either ACTIVE or INACTIVE. The STATUS of the pharmacy may be revised through the Register Pharmacy with Austin Information Technology Center option.                                                                                                                                                                                                                                                                                                                                             |
| OUTPATIENT SITES       | One or more Outpatient Sites (from File 59) may be linked with a single BPS Pharmacy entry. However, an Outpatient Site can only be linked with a single BPS Pharmacy. All the sites linked with a BPS Pharmacy should have the same NCPDP number. When an Outpatient Site is linked to an active BPS Pharmacy entry, the ECME switch for that site is considered ENABLED. If an Outpatient Site is linked to an incorrect BPS Pharmacy, it must be removed from the incorrect entry before it can be linked to the correct entry. |
| CMOP                   | ON if the transmission of prescriptions to the CMOP (Consolidated Mail Outpatient Pharmacy) dispensing site will automatically submit electronic third party prescription claims to the insurance payers. See note below for explanation of claims generated before and after switch is turned on or off.                                                                                                                                                                                                                          |
| AUTO-REVERSE PARAMETER | Enter numbers from 3 to 10 for the number of days to wait before ECME reverses non-released prescription claims with a PAYABLE payer-returned response. Each site’s business practice will dictate what this value should be.                                                                                                                                                                                                                                                                                                      |
| DEFAULT DEA \#         | The pharmacy’s Drug Enforcement Administration (DEA) number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

<span id="_Toc72333929" class="anchor"></span>Table 5: Description of Statistics Screen Option

15. An Outpatient Site is considered ECME active if the Outpatient Site is linked to a BPS Pharmacy, and if that BPS Pharmacy is ACTIVE. Once an Outpatient Site is ECME active, claims for the Outpatient Site can be transmitted to the third-party payer.

    If an Outpatient Site is activated after a claim is already sent to ECME, ECME will NOT generate an electronic claim.

    If an Outpatient Site is inactivated (by unlinking it from a BPS Pharmacy or by changing the STATUS field), reversals for that site will be processed but new submissions will not.

### Register Pharmacy with Austin Information Technology Center

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Register Pharmacy with Austin Information Technology Center option allows the ADPAC to register a pharmacy with the Austin Information Technology Center and update the contact information. This registration should only be performed on initialization of the pharmacy with ECME. Once the pharmacy has been set up to use ECME, the Edit ECME Pharmacy Data option should be used to make any changes.

The automated registration process will send an email to the Primary Site Contact if the registration has any errors or warnings to report. The Alternate Site Contact will be used when the email address for the Primary Site contact is missing. If the alternate site contact does not have an email address, the message will be sent to the BPS OPECC mail group. In addition, if either the primary or alternate site contact is missing their email address, it will be reported as a warning during manual registration. Following is a sample email.

Example 7.2.3-1: ECME Pharmacy Registration Problem Message

Subj: ECME Registration Problem. \[#141587\] 06/09/08@15:36 4 lines

From: ECME PACKAGE In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

Source Process: ECME Pharmacy Registration

ECME Pharmacy Registration HL7 Message not created.

PHARMACY NAME: TEST PHARMACY 2

\*\* NPI NUMBER - Missing/Invalid

Enter message action (in IN basket): Delete//

16. This option should not be used after the initial setup unless any of the information changes for the pharmacy.

    Key The user must hold the BPS MASTER key to view the Edit Basic ECME Parameters (BAS), Edit ECME Pharmacy Data (PHAR), and Register Pharmacy with Austin Automation Center (REG) options.

Access the menu by entering REG at the “Select Pharmacy ECME Setup Menu Option:” prompt in the *Pharmacy ECME Setup Menu* option. The system will validate the data and then send an ePharmacy message to the Austin Information Technology Center, which notifies them that the prospective site is ready to transmit electronic pharmacy claims.

Example 7.2.3-2: Accessing the Register Pharmacy with Austin Information Technology Center Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Pharmacy ECME Setup Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

BAS Edit Basic ECME Parameters

PHAR Edit ECME Pharmacy Data

REG Register Pharmacy with Austin Information Technology Center

Select Pharmacy ECME Setup Menu Option: REG Register Pharmacy with Austin Information Technology Center

Example 7.2.3-3: Register Pharmacy with Austin Information Technology Center with Austin Information Technology Center Option

\*\* ECME Site Registration \*\*

-- PRIMARY SITE CONTACT DATA –

SITE CONTACT: ECMEUSER,ONE// \<ENTER\>

OFFICE PHONE: XXX-XXX-XXXX// \<ENTER\>

EMAIL ADDRESS: ECMEUSER.ONE@FORUM.VA.GOV// \<ENTER\>

-- ALTERNATE SITE CONTACT DATA --

ALTERNATE SITE CONTACT: ECMEUSER,TWO// \<ENTER\>

OFFICE PHONE: XXX-XXX-XXXX// \<ENTER\>

EMAIL ADDRESS: two.ecmeuser@va.gov//

Replace \<ENTER\>

-- Application Registration Validation Results:

DOMAIN NAME - Required - VALID: XXXXXXXX.XXXXXX-XXX-XXXX.XXX.XX.XXX

TCP/IP ADDRESS FOR "EPHARM OUT" - Required - VALID: XX.XXX.XXX.XXX

"EPHARM OUT" PORT NUMBER - Required - VALID: XXXX

SITE NUMBER - Required - VALID: XXX

INTERFACE VERSION - Required - VALID: 3

CONTACT NAME - VALID: ECMEUSER,ONE

CONTACT MEANS - VALID: NET INTERNET ECMEUSER.ONE@FORUM.VA.GOV

ALTERNATE CONTACT NAME - VALID: ECMEUSER,TWO

ALTERNATE CONTACT MEANS - VALID: NET INTERNET two.ecmeuser@va.gov

\*\* Application Registration Data VALID \*\*

Enter RETURN to continue or '^' to exit: \<ENTER\>

Enter/verify Pharmacy Registration Data

Select BPS PHARMACIES NAME: TEST PHARMACY 3

--SITE DATA

STATUS: INACTIVE// \<ENTER\>

NCPDP \#: XXXXXXX// \<ENTER\>

DEFAULT DEA \#: XXXXXXXX// \<ENTER\>

SITE ADDRESS NAME: 111 MAIN STR// \<ENTER\>

SITE ADDRESS 1: 111 MAIN STREET// \<ENTER\>

SITE ADDRESS 2: \<ENTER\>

SITE CITY: ANYTOWN// \<ENTER\>

SITE STATE: NEW YORK// \<ENTER\>

SITE ZIP CODE: 11223// \<ENTER\>

REMITTANCE ADDRESS NAME: 1111 TEST STR// \<ENTER\>

REMIT ADDRESS 1: 111 TEST STREET// \<ENTER\>

REMIT ADDRESS 2: \<ENTER\>

REMIT CITY: ANYTOWN// \<ENTER\>

REMIT STATE: KANSAS// \<ENTER\>

REMIT ZIP: 66606// \<ENTER\>

--PRIMARY CONTACT DATA

VA CONTACT: ECMEUSER,ONE// \<ENTER\>

OFFICE PHONE: XXX-XXX-XXXX// \<ENTER\>

EMAIL ADDRESS: ECMEUSER.ONE@FORUM.VA.GOV

Replace \<ENTER\>

TITLE: OI&T STAFF// \<ENTER\>

--ALTERNATE CONTACT DATA

VA ALTERNATE CONTACT: ECMEUSER,THREE L// \<ENTER\>

OFFICE PHONE: XXX-XXX-XXXX// \<ENTER\>

EMAIL ADDRESS: three.ecmeuser@med.va.gov Replace \<ENTER\>

TITLE: OI&T STAFF// \<ENTER\>

--PHARMACIST DATA

VA LEAD PHARMACIST: ECMEUSER,FOUR// \<ENTER\>

OFFICE PHONE: XXX-XXX-XXXX // \<ENTER\>

EMAIL ADDRESS: \<ENTER\>

TITLE: OI&T STAFF// \<ENTER\>

VA LEAD PHARMACIST LICENSE \#: XXXXXXX// \<ENTER\>

-- Pharmacy Registration Validation Results –

PHARMACY NAME: TEST PHARMACY 3

-- Pharmacy Registration Data VALID. –

Enter/verify Pharmacy Registration Data

Select BPS PHARMACIES NAME: \<ENTER\>

Application Registration Data is VALID

Pharmacy Registration Data is:

VALID for TEST PHARMACY 1 and will be transmitted.

\*INVALID for TEST PHARMACY 2 and will NOT be transmitted.

VALID for TEST PHARMACY 3 and will be transmitted.

Send Application Registration: Y/N ? n NO

Press RETURN to continue...

## Statistics Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Statistics Screen* option allows ADPACS and IRMS to view statistics and transmission progress for all ECME claims.

Key The user must hold the BPSMENU and BPS MANAGER keys to view the Statistics Screen option.

17. Statistics collection begins the moment of ECME installation and continues until either the user uses the Z (clear) action or ECME is uninstalled. It depends on each site's business practice as far as how often or if the stats are cleared.

Access the menu by entering STAT at the “Select Pharmacy ECME Manager Menu Option:” prompt in the Pharmacy ECME Manager Menu option.

Example 7.3-1: Accessing the Statistics Screen Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXXX VAMC \*

\* Pharmacy ECME Manager Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

MNT ECME transaction maintenance options ...

SET Pharmacy ECME Setup Menu ...

STAT Statistics Screen

Select Pharmacy ECME Manager Menu Option: STAT Statistics Screen

Example 7.3-2: Statistics Screen

ECME STATISTICS Nov 03, 2010@16:50:30 Page:1 of 1

Communications statistics last cleared on AUG 18,2003@16:36:28

\* CLAIM STATUS \* \* CLAIM RESULTS \*

Waiting to start 0 Paid claims 2,934

Building the transaction 0 Rejected claims 2,171

Building the claim 0 Dropped to Paper 15

Building the HL7 packet 1 Duplicate claims 0

Preparing for transmit 0 Captured claims 0

Transmitting 0 Accepted Reversals 2,067

Parsing response 0 Rejected Reversals 166

Processing response 0 Accepted Eligibility 7

Rejected Eligibility 44

Errors 14

Enter ?? for more actions

UC Update continuously Z Zero (clear) stats

U1 Display update EX Exit

Select Action:U1//

This section diagrams and describes the different elements of the Statistics Screen.

Diagram 7.3-1: Statistics Option Areas

ECME STATISTICS Nov 03, 2010@16:50:30 Page: 1 of 1

Communications statistics last cleared on AUG 18,2003@16:36:28

\* CLAIM STATUS \* \* CLAIM RESULTS \*

Waiting to start 0 Paid claims 2,934

Building the transaction 0 Rejected claims 2,171

Building the claim 0 Dropped to Paper 15

Building the HL7 packet 1 Duplicate claims 0

Preparing for transmit 0 Captured claims 0

Transmitting 0 Accepted Reversals 2,067

Parsing response 0 Rejected Reversals 166

Processing response 0 Accepted Eligibility 7

Rejected Eligibility 44

Errors 14

Enter ?? for more actions

UC Update continuously Z Zero (clear) stats

U1 Display update EX Exit

Select Action:U1//

The table below describes the Statistics Screen option areas:

| Screen Areas   | Description                                                                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Message Window | This section displays informational text (i.e., Enter ?? for more actions).                                                                                                      |
| Action Area    | Available options. A double question mark (??) may be entered at the "Select Action:" prompt for a list of all List Manager options available.                                   |
| Header Area    | Displays the date for which the user requested the *Statistics Screen* option.                                                                                                   |
| Stats Area     | Displays statistics for all ECME claims. *Claim Status* reports statistics of ECME transactions in progress. *Claim Results* gives statistics about completed ECME transactions. |

<span id="_Toc72333930" class="anchor"></span>Table 6: Glossary

### Update Continuously

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system can update the claims statistics every 3 seconds.

1.  Enter UC to display statistics that will be updated every 3 seconds.

Example 7.3.1-1: Accessing Update Continuously Option

ECME STATISTICS Nov 03, 2010@16:50:30 Page: 1 of 1

Communications statistics last cleared on AUG 18,2003@16:36:28

\* CLAIM STATUS \* \* CLAIM RESULTS \*

Waiting to start 0 Paid claims 2,934

Building the transaction 0 Rejected claims 2,171

Building the claim 0 Dropped to Paper 15

Building the HL7 packet 1 Duplicate claims 0

Preparing for transmit 0 Captured claims 0

Transmitting 0 Accepted Reversals 2,067

Parsing response 0 Rejected Reversals 166

Processing response 0 Accepted Eligibility 7

Rejected Eligibility 44

Errors 14

Enter ?? for more actions

UC Update continuously Z Zero (clear) stats

U1 Display update EX Exit

Select Action:U1//UC Update continuously

78. Press ^ or Q to stop the updating. The system will go back to the Statistics Screen*.*

Example 7.3.1-2: Displaying Claims Status and Results in Update Continuously Mode

ECME STATISTICS Nov 03, 2010@16:50:30 Page: 1 of 1

Communications statistics last cleared on AUG 18,2003@16:36:28

\* CLAIM STATUS \* \* CLAIM RESULTS \*

Waiting to start 0 Paid claims 2,934

Building the transaction 0 Rejected claims 2,171

Building the claim 0 Dropped to Paper 15

Building the HL7 packet 1 Duplicate claims 0

Preparing for transmit 0 Captured claims 0

Transmitting 0 Accepted Reversals 2,067

Parsing response 0 Rejected Reversals 166

Processing response 0 Accepted Eligibility 7

Rejected Eligibility 44

Errors 14

In continuous update mode: press Q to Quit

Q Quit

### Display Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user can update the statistics once every time the option U1 is entered.

Example 7.3.2-1: Accessing Display Update Option

ECME STATISTICS Nov 03, 2010@16:50:30 Page: 1 of 1

Communications statistics last cleared on AUG 18,2003@16:36:28

\* CLAIM STATUS \* \* CLAIM RESULTS \*

Waiting to start 0 Paid claims 2,934

Building the transaction 0 Rejected claims 2,171

Building the claim 0 Dropped to Paper 15

Building the HL7 packet 1 Duplicate claims 0

Preparing for transmit 0 Captured claims 0

Transmitting 0 Accepted Reversals 2,067

Parsing response 0 Rejected Reversals 166

Processing response 0 Accepted Eligibility 7

Rejected Eligibility 44

Errors 14

Enter ?? for more actions

UC Update continuously Z Zero (clear) stats

U1 Display update EX Exit

Select Action:U1//U1 Display update

### Zero (Clear) Statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system can reset the displayed claims statistics to zero. This is useful for looking at short-term averages, such as during a time of heavy activity.

1.  Enter Z to access the *Zero (clear) stats* option.

Example 7.3.3-1: Accessing Zero (clear) stats Option

ECME STATISTICS Nov 03, 2010@16:50:30 Page: 1 of 1

Communications statistics last cleared on AUG 18,2003@16:36:28

\* CLAIM STATUS \* \* CLAIM RESULTS \*

Waiting to start 0 Paid claims 2,934

Building the transaction 0 Rejected claims 2,171

Building the claim 0 Dropped to Paper 15

Building the HL7 packet 1 Duplicate claims 0

Preparing for transmit 0 Captured claims 0

Transmitting 0 Accepted Reversals 2,067

Parsing response 0 Rejected Reversals 166

Processing response 0 Accepted Eligibility 7

Rejected Eligibility 44

Errors 14

Enter ?? for more actions

UC Update continuously Z Zero (clear) stats

U1 Display update EX Exit

Select Action:U1//Z Z (clear) stats

79. The user may choose to either zero out (refresh) the displayed copy of the statistics by entering L (Local) or to zero out the permanent copy by entering P.

    IMPORTANT: Choosing Permanent Copy will permanently zero out the statistics in the database. The user needs to realize that if this selection is chosen, there will no longer be activity history.

Example 7.3.3-2: Entering Zero (clear) stats Option to Delete Local Claim Results Statistics

Select one of the following:

L Local Copy

P Permanent Copy

Delete (L)ocal Copy or (P)ermanent Copy of the statistics: Local Copy// L Local Copy

80. When the system asks if the user is sure, enter Y to continue or N to stop the deletion.

Example 7.3.3-3: Entering Yes to “Are You Sure” Prompt

Are you sure? N// YES

81. Enter Z to access the *Zero (clear) stats* option.

Example 7.3.3-4: Displaying Zeroed Claims Statistics

ECME STATISTICS Nov 03, 2010@16:50:30 Page: 1 of 1

Communications statistics last cleared on AUG 18,2003@16:36:28

\* CLAIM STATUS \* \* CLAIM RESULTS \*

Waiting to start 0 Paid claims 2,934

Building the transaction 0 Rejected claims 2,171

Building the claim 0 Dropped to Paper 15

Building the HL7 packet 1 Duplicate claims 0

Preparing for transmit 0 Captured claims 0

Transmitting 0 Accepted Reversals 2,067

Parsing response 0 Rejected Reversals 166

Processing response 0 Accepted Eligibility 7

Rejected Eligibility 44

Errors 14

Enter ?? for more actions

UC Update continuously Z Zero (clear) stats

U1 Display update EX Exit

Select Action:U1// Z Zero (clear) stats

Delete (L)ocal Copy or (P)ermanent Copy of the statistics: Local Copy// Local Copy

Are you sure? N// YES

### Exiting the Statistics Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enter EX or Q to exit out of the Statistics Screen and return to the Pharmacy ECME Manager Menu.

Example 7.3.4-1: Accessing Exit Option

ECME STATISTICS Nov 03, 2010@16:50:30 Page: 1 of 1

Communications statistics last cleared on AUG 18,2003@16:36:28

\* CLAIM STATUS \* \* CLAIM RESULTS \*

Waiting to start 0 Paid claims 2,934

Building the transaction 0 Rejected claims 2,171

Building the claim 0 Dropped to Paper 15

Building the HL7 packet 1 Duplicate claims 0

Preparing for transmit 0 Captured claims 0

Transmitting 0 Accepted Reversals 2,067

Parsing response 0 Rejected Reversals 166

Processing response 0 Accepted Eligibility 7

Rejected Eligibility 44

Errors 14

Enter ?? for more actions

UC Update continuously Z Zero (clear) stats

U1 Display update EX Exit

Select Action:U1// EX Exit

# Accessing the Pharmacy Electronic Claims Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Pharmacy Electronic Claims* Reports option is a menu that allows the user to obtain detailed information about claims, transactions, Electronic Claims Management Engine (ECME) activities, and system configurations.

Key The user must hold the BPSMENU and BPS REPORTS keys to view the Pharmacy Electronic Claims Reports option.

Access it by entering RPT at the “Select ECME Option:” prompt on the ECME Main Menu option screen.

Example 8-1: Accessing the Pharmacy Electronic Claims Reports Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Main Menu \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

U ECME User Screen

COB ECME Pharmacy COB ...

MGR Pharmacy ECME Manager Menu ...

RPT Pharmacy Electronic Claims Reports ...

Select ECME Option: RPT Pharmacy Electronic Claims Reports

Example 8-2: Displaying Pharmacy Electronic Claims Reports Options

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Pharmacy Electronic Claims Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

CLA Claim Results and Status ...

OTH Other Reports ...

Select Pharmacy Electronic Claims Reports Option:

## Claim Results and Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Claim Results and Status* option is a menu that allows the user to obtain reports about the statuses of claims.

1.  Access Claim Results and Status by entering CLA at the “Select Pharmacy Electronic Claims Reports Option:” prompt on the Pharmacy Electronic Claims Reports option screen.

Example 8.1-1: Accessing the Claim Results and Status Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Pharmacy Electronic Claims Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

CLA Claim Results and Status ...

OTH Other Reports ...

Select Pharmacy Electronic Claims Reports Option: CLA Claim Results and Status

82. The user has a selection of Claims Results and Status Reports to choose from.

Example 8.1-2: Displaying All Claims Results and Status Options

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXXX VAMC \*

\* Claim Results and Status \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PAY Payable Claims Report

REJ Rejected Claims Report

ECMP CMOP/ECME Activity Report

REV Reversal Claims Report

NYR Claims Submitted, Not Yet Released

REC Recent Transactions

DAY Totals by Date

CLO Closed Claims Report

NBS Non-Billable Status Report

SPA Spending Account Report

Select Claim Results and Status Option:

83. Items / filters that pertain to ALL ECME Claims Results and Status REPORTS will be displayed for every option chosen. The user can select these options using the same method as in other VistA applications and as described in the [Change View](#change-view) section.
18. Most of the Claim Results and Status reports require that a device with 256 column width be used. They will not display correctly using 80 column width devices.

Example 8.1-3: Displaying ECME Report Item / Filter Options for ALL REPORTS

Select one of the following:

D DIVISION

A ALL

Select Certain Pharmacy (D)ivisions or (A)LL: \<Enter\> ALL

Select one of the following:

S Summary

D Detail

Display (S)ummary or (D)etail Format: Detail// Summary

Select one of the following:

I SPECIFIC INSURANCE(S)

A ALL

Select Certain (I)NSURANCE or (A)LL): A// I SPECIFIC INSURANCES(S)

Select INSURANCE: IBINSUR1 123 ANYWHERE ST ANYTOWN VIRGINIA

Y

Selected:

IBINSUR1

Select INSURANCE: DEVELOPMENT INS 123 HERE STREET ANYTOWN

CALIFORNIA Y

Selected:

DEVELOPMENT INS

IBINSUR1

Select INSURANCE: \<Enter\>

Select one of the following:

C CMOP

M Mail

W Window

A ALL

Display (C)MOP or (M)ail or (W)indow or (A)LL: ALL// \<Enter\> ALL

Select one of the following:

R Real Time Fills

B Backbill

P PRO Option

S Resubmission

A ALL

Display (R)ealTime, (B)ackbills, (P)RO Option, Re(S)ubmission or (A)LL: A// \<Enter\> ALL

Select one of the following:

D Drug

C Drug Class

A ALL

Display Specific (D)rug or Drug (C)lass or (A)LL: ALL// \<Enter\> ALL

84. In addition to the “ALL REPORTS” prompts, all the Claims Results and Status REPORTS except the ECMP report display another prompt that will allow the user to capture the report data in Excel spreadsheet format. If the answer is Y, additional directions are supplied.

Example 8.1-4: Requesting Report Data in Excel Spreadsheet Format

Do you want to capture report data for an Excel document? NO// YES

Before continuing, please set up your terminal to capture the

detail report data and save the detail report data in a text file

to a local drive. This report may take a while to run.

> **NOTE:** To avoid undesired wrapping of the data saved to the file,

please enter '0;256;99999' at the 'DEVICE:' prompt.

### Payable Claims Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Payable Claims Report* option produces a report that lists PAYABLE electronic claims that have been successfully transmitted to the payer and have not been reversed.

Key The user must hold the BPSMENU and BPS REPORTS keys to view the Payable Claims Report option.

19. The Payable Claims Report option has the most accessible information on payable claims from the BPS Claims File. A FileMan inquiry into the BPS Claims File will find that the information is in NCPDP (National Council for Prescription Drug Programs) V. D.0 formats.
1.  Access the report by entering PAY at the “Select Claim Results and Status Option:” prompt on the Claim Results and Status option screen.

Example 8.1.1-1: Accessing the Payable Claims Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Claim Results and Status \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PAY Payable Claims Report

REJ Rejected Claims Report

ECMP CMOP/ECME Activity Report

REV Reversal Claims Report

NYR Claims Submitted, Not Yet Released

REC Recent Transactions

DAY Totals by Date

CLO Closed Claims Report

NBS Non-Billable Status Report

SPA Spending Account Report

Select Claim Results and Status Option: PAY Payable Claims Report

85. After a selection has been made from the “ALL REPORTS” prompt, the user will be prompted to select a report date range; Released, Not Released or All claims; Certain Eligibility Type or All; Selected Patients or All; Selected Range for Billed Amount or All; and Excel display format and device selection.

Example 8.1.1-2: Additional prompts asked by the Payable Claims Report Option

START WITH TRANSACTION DATE: T-1// T-99

GO TO TRANSACTION DATE: T// \<Enter\>

Select one of the following:

R RELEASED

N NOT RELEASED

A ALL

Include Rxs - (R)ELEASED or (N)OT RELEASED or (A)LL: RELEASED// ALL

Select one of the following:

V VETERAN

T TRICARE

C CHAMPVA

A ALL

Display (V)ETERAN or (T)RICARE or (C)HAMPVA or (A)LL: A// ALL

Select one of the following:

P Patient

A ALL

Display Selected (P)atients or (A)LL: ALL//

Select one of the following:

R Range

A ALL

Select (R)ange for Billed Amount or (A)LL: ALL//

Data fields VA Ingredient Cost, VA Dispensing Fee, Ingredient Cost Paid,

Dispensing Fee Paid and Patient Responsibility (INS) will only be included

when the report is captured for an Excel document. All additional data fields

may not be present for all reports.

Do you want to capture report data for an Excel document? NO// \<Enter\>

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// \<Enter\> IP network

Please wait...

Example 8.1.1-3: Payable Claims Report

ECME PAYABLE CLAIMS DETAIL REPORT Print Date: MAY 21, 2008@11:41:54 Page: 1

DIVISION(S): ALL Fill Locations: C,M,W Fill type: RT,BB,RS

Insurance: SELECTED Drugs/Classes: ALL

Eligibility: CVA,TRI,VET Patient: ALL

ALL PRESCRIPTIONS BY TRANSACTION DATE: From 02/12/08 through 05/21/08

===================================================================================================================

PATIENT NAME Pt.ID ELIG RX# REF/ECME# DATE \$BILLED \$INS RESPONSE \$COLLECT

DRUG NDC RELEASED ON RX INFO BILL# COB

===================================================================================================================

DIVISION: PHARMACY-1

-------------------------------------------------------------------------------------------------------------------

DEVELOPMENT INS

-------------------------------------------------------------------------------------------------------------------

ECMEpatient,One (XXXX) TRI 100222\$ 2/000000111264 04/15/08 51.00 40.00

AMITRIPTYLINE 10MG TAB 00182-1018-10 04/15/08 W RT AC/R K8000K9 p

ECMEpatient, Three (XXXX) VET 222\$ 0/000000000492 03/10/08 51.00 68.32

METHADONE 10MG TAB W RT EX/N

---------- ----------

SUBTOTALS for INS:DEVELOPMENT INS 102.00 108.32 0.00

COUNT 2 2 2

MEAN 51.00 54.16 0.00

-------------------------------------------------------------------------------------------------------------------

IBINSUR1

-------------------------------------------------------------------------------------------------------------------

ECMEpatient, Two (XXXX) VET 100574\$ 0/000000000484 03/05/08 51.00 40.00

NEODECADRON OPHTMALIC SOL. 00006-7639-03 03/05/08 W RT AC/R K8000H6 p

ECMEpatient, Two (XXXX) VET 100575\$ 0/000000000485 03/05/08 51.00 40.00

PENTAERYTHRITOL 10MG TAB 00725-2064-10 03/05/08 W RT AC/R K8000H7 p

SUBTOTALS for INS:IBINSUR1 2142.00 1652.28 5.00

COUNT 42 42 42

MEAN 51.00 39.34 0.12

---------- --------- ----------

SUBTOTALS for DIV:PHARMACY-1 2244.00 1760.60 5.00

COUNT 44 44 44

MEAN 51.00 40.01 0.11

---------- --------- ----------

GRAND TOTALS 2244.00 1760.60 5.00

COUNT 44 44 44

MEAN 51.00 40.01 0.11

Press RETURN to continue:

### Rejected Claims Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Rejected Claims Report* option produces a report that lists electronic claims that have been successfully transmitted to the payer and have been rejected.

Key The user must hold the BPSMENU and BPS REPORTS keys to view the Rejected Claims Report option.

20. The Rejected Claims Report option has the most accessible information on rejected claims from the BPS Claims File. A FileMan inquiry into the BPS Claims File will find that the information is in NCPDP V. D.0 formats.
1.  Access the report by entering REJ at the “Select Claim Results and Status Option:” prompt on the Claim Results and Status option screen.

Example 8.1.2-1: Accessing the Rejected Claims Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Claim Results and Status \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PAY Payable Claims Report

REJ Rejected Claims Report

ECMP CMOP/ECME Activity Report

REV Reversal Claims Report

NYR Claims Submitted, Not Yet Released

REC Recent Transactions

DAY Totals by Date

CLO Closed Claims Report

NBS Non-Billable Status Report

SPA Spending Account Report

Select Claim Results and Status Option: REJ Rejected Claims Report

86. After the user has made selections from the “ALL REPORTS” prompt, the user will be given the following prompts for date range, Released / Not Released / All claims, All / Specific Reject Codes, VETERAN / TRICARE / CHAMPVA / All Eligibility, Selected Patients or All, Selected Range for Billed Amount or All, Excel display format and device selection.

Example 8.1.2-2: Additional prompts asked by the Rejected Claims Report Option

START WITH TRANSACTION DATE: T-1// T-30

GO TO TRANSACTION DATE: T// \<Enter\>

Select one of the following:

R RELEASED

N NOT RELEASED

A ALL

Include Rxs - (R)ELEASED or (N)OT RELEASED or (A)LL: RELEASED// ALL

Select one of the following:

S Specific Reject Code

A ALL

Include (S)pecific Reject Code or (A)LL: ALL// \<Enter\>

Select one of the following:

O OPEN

C CLOSED

A ALL

Include (O)pen, (C)losed, or (A)ll Claims: O// ALL

Select one of the following:

V VETERAN

T TRICARE

C CHAMPVA

A ALL

Include Certain Eligibility Type or (A)ll: V// ALL

Select one of the following:

O OPEN

C CLOSED

A ALL

Include (O)pen, (C)losed, or (A)ll Claims: O// PEN

Select one of the following:

S SPECIFIC PRESCRIBER(S)

A ALL PRESCRIBERS

Select Specific Prescriber(s) or include ALL Prescribers: A// LL PRESCRIBERS

Select one of the following:

P Patient

A ALL

Display Selected (P)atients or (A)LL: ALL//

Select one of the following:

R Range

A ALL

Select (R)ange for Billed Amount or (A)LL: ALL//

Data fields VA Ingredient Cost, VA Dispensing Fee, Ingredient Cost Paid,

Dispensing Fee Paid and Patient Responsibility (INS) will only be included

when the report is captured for an Excel document. All additional data fields

may not be present for all reports.

Do you want to capture report data for an Excel document? NO// \<Enter\>

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// \<Enter\> IP network

Please wait...

Example 8.1.2-3: Rejected Claims Report

ECME REJECTED CLAIMS DETAIL REPORT Print Date: MAY 21, 2008@17:20:35 Page: 1

DIVISION(S): ALL Fill Locations: C,M,W Fill type: RT,BB,RS

Insurance: SELECTED Drugs/Classes: ALL

Reject Code: ALL Eligibility: ALL Open/Closed: ALL

Prescriber: ALL Patient: ALL

ALL PRESCRIPTIONS BY TRANSACTION DATE: From 05/01/08 through 05/21/08

=======================================================================================================================

PATIENT NAME Pt.ID ELIG RX# REF/ECME# DATE RELEASED ON RX INFO COB OPEN/CLOSED

CARDHOLD.ID GROUP ID \$BILLED QTY NDC# PRESCRIBER ID NAME

=======================================================================================================================

DIVISION: PHARMACY-1

-----------------------------------------------------------------------------------------------------------------------

IBINSUR1 - 123456

-----------------------------------------------------------------------------------------------------------------------

ECMEPATIENT,ONE (XXXX) VET 100888\$ 0/000000000808 05/04/08 05/04/08 W RT DS/R s Open

123456 555 51.00 90 00777-0877-03 9998887777 ECMEPRESCRIBER,ONE

FENOPROFEN 300MG CAP

07:M/I Cardholder ID Number

ECMEPATIENT,ONE (XXXX) VET 100892\$ 0/000000000812 05/04/08 05/04/08 W RT DS/R s Closed

123456 555 51.00 90 00777-0877-03 9998887777 ECMEPRESCRIBER,ONE

FENOPROFEN 300MG CAP

07:M/I Cardholder ID Number

ECMEPATIENT,ONE (XXXX) VET 100893\$ 0/000000000813 05/04/08 05/04/08 W RT DS/R p Closed

123456 555 51.00 90 00777-0877-03 9998887777 ECMEPRESCRIBER,ONE

FENOPROFEN 300MG CAP

07:M/I Cardholder ID Number

----------

SUBTOTALS for INS:IBINSUR1 153.00

COUNT 3

MEAN 51.00

-----------------------------------------------------------------------------------------------------------------------

OPINSUR1 - 654321

-----------------------------------------------------------------------------------------------------------------------

ECMEPATIENT,TWO (XXXX) VET 100896\$ 0/000000000816 05/06/08 W RT DS/N p Open

111 51.00 180 00003-0626-50 9995552277 ECMEPRESCRIBER,FIVE

CHLORAL HYDRATE 500MG CAP

12:M/I Patient Location

ECMEPATIENT,TWO (XXXX) VET 100899\$ 0/000000000819 05/06/08 W RT DS/N p Open

111 51.00 180 00149-0030-66 9995552277 ECMEPRESCRIBER,FIVE

DANTROLENE 25MG CAP

75:Prior Authorization Required

ECMEPATIENT,TWO (XXXX) VET 100901\$ 0/000000000821 05/06/08 W RT DS/N p Open

111 51.00 90 00591-5521-04 9995552277 ECMEPRESCRIBER,FIVE

PHENYLBUTAZONE 100MG TAB

05/06/08 - Prior Authorization Code (8/32432242) submitted.

75:Prior Authorization Required

ECMEPATIENT,TWO (XXXX) VET 100902\$ 0/000000000822 05/06/08 W RT DS/N p Open

111 51.00 180 00023-4534-67 9995552277 ECMEPRESCRIBER,FIVE

BACLOFEN 10MG TABS

05/06/08 - Clarification Code 4,3 submitted.

79:Refill Too Soon

ECMEPATIENT,TWO (XXXX) VET 100903\$ 0/000000000823 05/06/08 W RT DS/N s Open

111 51.00 180 00023-4534-67 9995552277 ECMEPRESCRIBER,FIVE

BACLOFEN 10MG TABS

05/06/08 - Clarification Code 4,3 submitted.

79:Refill Too Soon

ECMEPATIENT,TWO (XXXX) VET 100906\$ 0/000000000826 05/06/08 M RT DS/N p Open

111 51.00 180 00839-7221-06 9995552277 ECMEPRESCRIBER,FIVE

DOXEPIN 25MG CAP

05/06/08 - Clarification Code 4,3 submitted.

79:Refill Too Soon

ECMEPATIENT,TWO (XXXX) VET 100907\$ 0/000000000827 05/06/08 M RT AC/N p Open

111 51.00 180 00081-0635-35 9995552277 ECMEPRESCRIBER,FIVE

CHLORAMBUCIL 2MG TAB

79:Refill Too Soon

ECMEPATIENT,TWO (XXXX) VET 100915\$ 0/000000000835 05/07/08 W RT DS/N p Open

111 51.00 180 00023-4534-67 9995552277 ECMEPRESCRIBER,FIVE

BACLOFEN 10MG TABS

05/07/08 - DAFASFDAFDASFDASFAS

75:Prior Authorization Required

ECMEPATIENT,TWO (XXXX) VET 100938\$ 0/000000000858 05/08/08 W RT AC/N p Open

111 51.00 30 00024-2253-04 9995552277 ECMEPRESCRIBER,FIVE

STANOZOLOL 2MG

75:Prior Authorization Required

ECMEPATIENT,TWO (XXXX) VET 100939\$ 0/000000000859 05/08/08 W RT DS/N p Open

111 51.00 180 00078-0005-10 9995552277 ECMEPRESCRIBER,FIVE

THIORIDAZINE 100MG TAB

05/08/08 - FDDSFADFA

75:Prior Authorization Required

ECMEPATIENT,TWO (XXXX) VET 100942\$ 0/000000000862 05/08/08 W RT AC/N p Open

111 51.00 180 00028-0105-10 9995552277 ECMEPRESCRIBER,FIVE

TERBUTALINE 5MG TABS

75:Prior Authorization Required

79:Refill Too Soon

ECMEPATIENT,TWO (XXXX) VET 100945\$ 0/000000000865 05/08/08 W RT DS/N p Open

111 51.00 180 00045-0412-60 9995552277 ECMEPRESCRIBER,FIVE

TOLMETIN 200MG TABS

75:Prior Authorization Required

79:Refill Too Soon

ECMEPATIENT,TWO (XXXX) VET 101002\$ 0/000000000926 05/14/08 W RT DS/N p Open

111 51.00 180 00023-4534-67 9995552277 ECMEPRESCRIBER,FIVE

BACLOFEN 10MG TABS

64:Claim Submitted Does Not Match Prior Authorization

ECMEPATIENT,TWO (XXXX) VET 101011\$ 0/000000000935 05/14/08 W RT DS/N p Open

111 51.00 180 00781-1367-10 9995552277 ECMEPRESCRIBER,FIVE

BENZTROPINE 2MG TAB

12:M/I Patient Location

Press RETURN to continue, '^' to exit:

### CMOP / ECME Activity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *CMOP / ECME Activity Report* option produces a report used for monitoring Consolidated Mail Outpatient Pharmacy (CMOP) activity during both the Controlled Substances and General CMOP Transmissions. The report contains reference information from multiple VistA sources. The user will not be prompted for selections from the “ALL REPORTS” section, but will need to select a report date range, a division or all divisions and a printer device. This report is not a 132-column report and the user can choose to display it on the screen

Key The user must hold the BPSMENU and BPS REPORTS keys to view the CMOP / ECME Activity Report option.

Access the report by entering ECMP at the “Select Claim Results and Status Option:” prompt on the Claim Results and Status option screen.

Example 8.1.3-1: Accessing the CMOP / ECME Activity Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Claim Results and Status \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PAY Payable Claims Report

REJ Rejected Claims Report

ECMP CMOP/ECME Activity Report

REV Reversal Claims Report

NYR Claims Submitted, Not Yet Released

REC Recent Transactions

DAY Totals by Date

CLO Closed Claims Report

NBS Non-Billable Status Report

SPA Spending Account Report

Select Claim Results and Status Option: ECMP CMOP/ECME Activity Report

ENTER BEGINNING TRANSMISSION DATE: 8/31

ENTER ENDING TRANSMISSION DATE: 9/1

SELECTION OF DIVISION(S)

Select one of the following:

A ALL DIVISIONS

S SELECT DIVISIONS

Enter response: SELECT DIVISIONS

1 XXXXXXXXXX

2 YYYYYYYYYY

3 ZZZZZZZZZZ

Select Division(s) : (1-4): 1

You have selected:

1 XXXXXXXXXX

Is this correct? YES// \<Enter\>

Do you want to capture report data for an Excel document? NO// \<Enter\>

Select Printer: HOME;132;999 IP network

Example 8.1.3-2: CMOP / ECME Activity Report

CMOP/ECME ACTIVITY REPORT for XXXXXXXXXX

For AUG 31,2005 thru SEP 1,2005 Printed: NOV 23,2005@10:25:49

=========================================================================================

TRANSMISSION: 2671

STATUS: TRANSMITTED

DIVISION: XXXXXXXXXX

CMOP SYSTEM: LEAVENWORTH

TRANSMISSION DATE/TIME: AUG 31, 2005@16:17:14

TOTAL PATIENTS: 3

TOTAL RXS: 3

NAME ECME#/RX#/FL# NDC SENT NDC RECVD CMOP-STAT

DRUG INSURANCE PAY-STAT BILL# REL-DATE

=========================================================================================

ECMEpatient,One (XXXX) 000001106254/909911\$e/0 00000-0158-23 TRANSMI

ATORVASTATIN CALCI WEBMD E PAYAB

### Reversal Claims Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Reversal Claims Report* option lists claims that have been successfully transmitted to the payer to REVERSE a previously PAYABLE claim and have not been RESUBMITTED.

Key The user must hold the BPSMENU and BPS REPORTS keys to view the Reversal Claims Report option.

1.  Access the report by entering REV at the “Select Claim Results and Status Option:” prompt on the Claim Results and Status option screen.

Example 8.1.4-1: Accessing the Reversal Claims Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Claim Results and Status \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PAY Payable Claims Report

REJ Rejected Claims Report

ECMP CMOP/ECME Activity Report

REV Reversal Claims Report

NYR Claims Submitted, Not Yet Released

REC Recent Transactions

DAY Totals by Date

CLO Closed Claims Report

NBS Non-Billable Status Report

SPA Spending Account Report

Select Claim Results and Status Option: REV Reversal Claims Report

87. After the user has made selections from the “ALL REPORTS” prompt, the user will be given the following prompts for date range, Released / Not Released / All Claims, Auto-Reversed / All Claims, Accepted / Rejected / All Claims, Veteran / TRICARE / CHAMPVA / All Eligibility, Selected Patients or All, Selected Range for Billed Amount or All, Excel display format and device selection.

Example 8.1.4-2: Additional Prompts for the Reversal Claims Report Option

START WITH TRANSACTION DATE: T-1// T-30

GO TO TRANSACTION DATE: T// \<Enter\>

Select one of the following:

R RELEASED

N NOT RELEASED

A ALL

Include Rxs - (R)ELEASED or (N)OT RELEASED or (A)LL: RELEASED// ALL

Select one of the following:

R AutoReversed

A ALL

Include Auto(R)eversed or (A)LL: ALL// \<Enter\>

Select one of the following:

C Accepted

R Rejected

A ALL

Include A(C)cepted or (R)ejected or (A)LL: Rejected// ALL

Select one of the following:

V VETERAN

T TRICARE

C CHAMPVA

A ALL

Display (V)ETERAN or (T)RICARE or (C)HAMPVA or (A)LL: A// ALL

Select one of the following:

P Patient

A ALL

Display Selected (P)atients or (A)LL: ALL// \<Enter\>

Select one of the following:

R Range

A ALL

Select (R)ange for Billed Amount or (A)LL: ALL// \<Enter\>

Data fields VA Ingredient Cost, VA Dispensing Fee, Ingredient Cost Paid, Dispensing Fee Paid and Patient Responsibility (INS) will only be included when the report is captured for an Excel document. All additional data fields may not be present for all reports.

Do you want to capture report data for an Excel document? NO// \<Enter\>

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// \<Enter\> IP network

Please wait...

Example 8.1.4-3: Reversal Claims Report

ECME REVERSED CLAIMS DETAIL REPORT Print Date: APR 17, 2009@14:17:15 Page: 1

DIVISION(S): ALL Fill Locations: C,M,W Fill type: RT,BB,RS

Insurance: ALL ALL Reversals ALL Returned Status Drugs/Classes: ALL

Eligibility: ALL Patient: ALL

ALL PRESCRIPTIONS BY TRANSACTION DATE: From 03/18/09 through 04/17/09

=======================================================================================================================

PATIENT NAME Pt.ID ELIG RX# REF/ECME# DATE \$BILLED \$INS RESPONSE \$COLLECT

DRUG NDC RX INFO COB

RELEASED ON REVERSAL METHOD/RETURN STATUS/REASON

=======================================================================================================================

DIVISION: YYYYYYYY

-----------------------------------------------------------------------------------------------------------------------

COB INSURANCE

-----------------------------------------------------------------------------------------------------------------------

ECMEPATIENT,ONE (XXXX) TRI 102445\$ 0/00000113725 03/20/09 21.88 40.00 0.00

OXYTOCIN 10 UNIT INJ 00071-4160-03 W RT AC/R s

03/18/09 REGULAR/ACCEPTED/2

---------- ---------- ----------

SUBTOTALS for INS:COB INSURANCE 21.88 40.00 0.00

COUNT 1 1 1

MEAN 21.88 40.00 0.00

-----------------------------------------------------------------------------------------------------------------------

ECME INSURANCE

-----------------------------------------------------------------------------------------------------------------------

ECMEPATIENT,TWO (XXXX) VET 102446\$ 0/00000113727 03/20/09 11.00 40.00 0.00

DACARBAZINE 100MG INJ 00026-8151-10 W RT DS/R s

03/20/09 REGULAR/ACCEPTED/REVERSING PRIMARY CLAIM

---------- ---------- ----------

SUBTOTALS for INS:ECME INSURANCE 11.00 40.00 0.00

COUNT 1 1 1

MEAN 11.00 40.00 0.00

-----------------------------------------------------------------------------------------------------------------------

ECME1 INSURANCE

-----------------------------------------------------------------------------------------------------------------------

ECMEPATIENT,TWO (XXXX) VET 102422\$ 1/00000113698 03/20/09 0.00 68.32 0.00

GENTAMICIN OPHTHALMIC OINT. 00719-7058-61 W RT DS/N p

REGULAR/ACCEPTED/RX DISCONTINUED

ECMEPATIENT,ONE (XXXX) TRI 102435\$ 0/00000113713 04/06/09 0.00 40.00 0.00

METHOXAMINE 10MG/CC INJ 00081-0957-10 W RT AC/N p

REGULAR/ACCEPTED/ RX DISCONTINUED

---------- ---------- ----------

SUBTOTALS for INS:ECME1 INSURANCE 0.00 108.32 0.00

COUNT 2 2 2

MEAN 0.00 54.16 0.00

---------- ---------- ----------

SUBTOTALS for DIV:YYYYYYYY 32.88 188.32 0.00

COUNT 4 4 4

MEAN 8.22 47.08 0.00

---------- ---------- ----------

GRAND TOTALS 32.88 188.32 0.00

COUNT 4 4 4

MEAN 8.22 47.08 0.00

### Claims Submitted, Not Yet Released

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Claims Submitted, Not Yet Released* option lists all prescription claims that have been successfully submitted to the payer, have been returned PAYABLE but the prescriptions have not been released.

Key The user must hold the BPSMENU and BPS REPORTS keys to view the Claims Submitted, Not Yet Released Report option.

1.  Access the report by entering NYR at the “Select Claim Results and Status Option:” prompt on the Claim Results and Status option screen.

Example 8.1.5-1: Accessing Claims Submitted, Not Yet Released Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Claim Results and Status \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PAY Payable Claims Report

REJ Rejected Claims Report

ECMP CMOP/ECME Activity Report

REV Reversal Claims Report

NYR Claims Submitted, Not Yet Released

REC Recent Transactions

DAY Totals by Date

CLO Closed Claims Report

NBS Non-Billable Status Report

SPA Spending Account Report

Select Claim Results and Status Option: NYR Claims Submitted, Not Yet Released

88. After the user has made selections from the “ALL REPORTS” prompt, the user will be given the following prompts for date range, Selected Patients or All, Selected Range for Billed Amount or All, Excel display format and device selection.

Example 8.1.5-2: Additional prompts to Claims Submitted, Not Yet Released Option

START WITH TRANSACTION DATE: T-1// T

GO TO TRANSACTION DATE: T// T

Select one or more of the following:

V VETERAN

T TRICARE

C CHAMPVA

A ALL

Display (V)ETERAN or (T)RICARE or (C)HAMPVA or (A)LL: A//

Select one of the following:

P Patient

A ALL

Display Selected (P)atients or (A)LL: ALL//

Select one of the following:

R Range

A ALL

Select (R)ange for Billed Amount or (A)LL: ALL//

Data fields VA Ingredient Cost, VA Dispensing Fee, Ingredient Cost Paid, Dispensing Fee Paid and Patient Responsibility (INS) will only be included when the report is captured for an Excel document. All additional data fields may not be present for all reports.

Do you want to capture report data for an Excel document? NO// \<Enter\>

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// \<Enter\> IP network

Example 8.1.5-3: Claims Submitted, Not Yet Released Report

ECME SUBMIT,NOT RELEASED CLAIMS DETAIL REPORT Print Date: SEP 23, 2005@15:01:21 Page: 1

DIVISION(S): ALL Fill Locations: C,M,W Fill type: RT,BB,RS

Insurance: ALL Drugs/Classes: ALL

Eligibility: CVA,TRI,VET Patient: ALL

PRESCRIPTIONS (NOT RELEASED) BY TRANSACTION DATE: From 09/23/05 through 09/23/05

========================================================================================

PATIENT NAME Pt.ID RX# REF/ECME# DATE \$BILLED \$INS RESPONSE

DRUG NDC RX INFO COB ELIG

========================================================================================

DIVISION: ZZZZZZZ

----------------------------------------------------------------------------------------

WEBMD

----------------------------------------------------------------------------------------

ECMEpatient,One (XXXX) 909716\$ 0/000001105959 09/23/05 45.00 40.00

PROTAMINE SULFATE 5ML INJ 00000-0000-00 W RT AC/N p VET ---------- ----------

SUBTOTALS for INS:WEBMD 45.00 40.00

COUNT 1 1

MEAN 45.00 40.00

---------- ----------

SUBTOTALS for DIV:ZZZZZZZ 45.00 40.00

COUNT 1 1

MEAN 45.00 40.00

GRAND TOTALS 45.00 40.00

COUNT 1 1

MEAN 45.00 40.00

### Recent Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Recent Transactions* option lists claims that have been successfully transmitted to the payer. These claims include submissions, reversals, and resubmissions. Closed Claims will NOT show up on this report since this report displays activity between ECME and the payer only.

Key The user must hold the BPSMENU and BPS REPORTS keys to view the Recent Transactions Report option.

1.  Access the report by entering REC at the “Select Claim Results and Status Option:” prompt on the Claim Results and Status option screen.

Example 8.1.6-1: Recent Transactions Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Claim Results and Status \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PAY Payable Claims Report

REJ Rejected Claims Report

ECMP CMOP/ECME Activity Report

REV Reversal Claims Report

NYR Claims Submitted, Not Yet Released

REC Recent Transactions

DAY Totals by Date

CLO Closed Claims Report

NBS Non-Billable Status Report

SPA Spending Account Report

Select Claim Results and Status Option: REC Recent Transactions

89. After the user has made selections from the “ALL REPORTS” prompt, the user will be given the following prompts for date range, Released / Not Released / All Claims, Excel display format and device selection.

Example 8.1.6-2: Additional prompts asked by the Recent Transactions Option

START WITH TRANSACTION DATE: T-1// T

GO TO TRANSACTION DATE: T// T

Select one of the following:

R RELEASED

N NOT RELEASED

A ALL

Include Rxs - (R)ELEASED or (N)OT RELEASED or (A)LL: RELEASED// ALL

Do you want to capture report data for an Excel document? NO// \<Enter\>

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// \<Enter\> IP network

Please wait...

Example 8.1.6-3: Recent Transactions Report

ECME RECENT TRANSACTIONS DETAIL REPORT Print Date: NOV 03, 2010@17:10:39 Page: 1

DIVISION(S): ALL Fill Locations: C,M,W Fill type: RT,BB,RS

Insurance: ALL Drugs/Classes: ALL

PRESCRIPTIONS BY TRANSACTION DATE: From 10/04/10 through 11/03/10

====================================================================================================================================

PATIENT NAME Pt.ID RX# REF/ECME# COMPLETED TRANS TYPE PAYER RESPONSE COB

DRUG NDC RX INFO INSURANCE ELAP TIME IN SECONDS

====================================================================================================================================

DIVISION: XXXXXXXX

------------------------------------------------------------------------------------------------------------------------------------

ECMEPATIENT,THREE (XXXX) 102128\$ 1/000000002509 10/04/10 02:52PM SUBMIT E REJECTED p

DIAZEPAM 10MG S.T. 00555-0164-04 M RT EX/N REJ OPINSUR1 9

ECMEPATIENT,THREE (XXXX) 1100249\$ 1/ 10/06/10 11:29AM SUBMIT E UNSTRANDED p

GENTAMICIN OPHTHALMIC O 00719-7058-61 W RT AC/N OPINSUR1 502339

ECMEPATIENT,SIX (XXXX) 1100341\$ 0/000000003126 10/07/10 12:06AM SUBMIT E REJECTED p

DOXEPIN 25MG CAP 00839-7221-06 W RT AC/R REJ OPINSUR2 7

ECMEPATIENT,SIX (XXXX) 1100342\$ 0/000000003127 10/07/10 01:59PM SUBMIT E PAYABLE p

CORTICOTROPIN 40UNIT HP 00053-1330-01 W RT AC/R OPINSUR2 4

ECMEPATIENT,SIX (XXXX) 1100336\$ 0/000000003120 10/07/10 03:05PM REVERSAL E REVERSAL OTHER p

TRIAMTERENE 50MG, HCTZ 00484-3590-30 W RT DS/R OPINSUR2 3

ECMEPATIENT,ONE (XXXX) 100952\$ 0/000000000874 10/07/10 05:29PM SUBMIT E UNSTRANDED p

MEDROXYPROGESTRONE 10MG 00009-0050-02 W RT DS/N OPINSUR1 76220585

ECMEPATIENT,ONE (XXXX) 100933\$ 0/000000000853 10/07/10 07:45PM SUBMIT E REJECTED p

DOXEPIN 25MG CAP 00839-7221-06 M RT DS/N REJ OPINSUR1 7

ECMEPATIENT,ONE (XXXX) 101814\$ 0/000000002181 10/08/10 04:11PM REVERSAL E REVERSAL UNSTRANDED p

IMIPRAMINE 25MG TAB 00779-0588-30 W RT DS/N OPINSUR1 57199104

ECMEPATIENT,ONE (XXXX) 100954\$ 0/000000000876 10/08/10 04:16PM SUBMIT E UNSTRANDED p

DOXEPIN 25MG CAP 00839-7221-06 M RT DS/N OPINSUR1 76194694

ECMEPATIENT,ONE (XXXX) 100991\$ 0/000000000915 10/08/10 04:16PM SUBMIT E UNSTRANDED p

BACLOFEN 10MG TABS 00023-4534-67 W RT DS/N OPINSUR1 75772098

ECMEPATIENT,ONE (XXXX) 101860\$ 0/000000002228 10/08/10 04:16PM SUBMIT E UNSTRANDED p

IMIPRAMINE 25MG TAB 00779-0588-30 W RT EX/N OPINSUR1 57199347

ECMEPATIENT,ONE (XXXX) 101861\$ 0/000000002229 10/08/10 04:16PM SUBMIT E UNSTRANDED p

CHLORAL HYDRATE 500MG C 00003-0626-51 W RT DS/N OPINSUR1 57199249

ECMEPATIENT,ONE (XXXX) 101959\$ 0/000000002331 10/08/10 04:16PM SUBMIT E UNSTRANDED p

LIDOCAINE 2% 50ML INJ M 00186-0240-02 W RT DS/N OPINSUR1 51602609

ECMEPATIENT,THREE (XXXX) 102225\$ 0/000000002607 10/08/10 04:16PM SUBMIT E UNSTRANDED p

BIPERIDEN 2MG TAB 00044-0120-04 M RT DS/N OPINSUR1 46160110

### Totals by Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Totals by Date* option totals the daily ECME activity claims that have been successfully transmitted to the payer, have been returned PAYABLE or REJECTED but have not been REVERSED.

Key The user must hold the BPSMENU and BPS REPORTS keys to view the Totals by Day Report option.

1.  Access the report by entering DAY at the “Select Claim Results and Status Option:” prompt on the Claim Results and Status option screen.

Example 8.1.7-1: Totals by Date Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Claim Results and Status \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PAY Payable Claims Report

REJ Rejected Claims Report

ECMP CMOP/ECME Activity Report

REV Reversal Claims Report

NYR Claims Submitted, Not Yet Released

REC Recent Transactions

DAY Totals by Date

CLO Closed Claims Report

NBS Non-Billable Status Report

SPA Spending Account Report

Select Claim Results and Status Option: DAY Totals by Date

90. After the user has made selections from the “ALL REPORTS” prompt, the user will be given the following prompts for date range, Released / Not Released / All Claims, Excel display format and device selection.

Example 8.1.7-2: Additional prompts asked by the Totals by Day Option

START WITH TRANSACTION DATE: T-1// T-30

GO TO TRANSACTION DATE: T// \<Enter\>

Select one of the following:

R RELEASED

N NOT RELEASED

A ALL

Include Rxs - (R)ELEASED or (N)OT RELEASED or (A)LL: RELEASED// ALL

Do you want to capture report data for an Excel document? NO// \<Enter\>

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// \<Enter\> IP network

Please wait...

Example 8.1.7-3: Totals by Date Report (Compacted to fit into document)

ECME TOTALS DETAIL REPORT Print Date: SEP 23, 2005@15:18:52 Page: 1

DIVISION(S): ALL Fill Locations: C,M,W Fill type: RT,BB,RS

Insurance: DEVELOPMENT INS, OPINSUR1 Drugs/Classes: ALL

ALL PRESCRIPTIONS BY TRANSACTION DATE: From 09/23/05 through 09/23/05

======================================================================================

AMOUNT RETURNED RETURNED AMOUNT

DATE \#CLAIMS SUBMITTED REJECTED PAYABLE TO RECEIVE DIFFERENCE

======================================================================================

DIVISION: ZZZZZZZ

-----------------------------------------------------------------------

09/23/05 2 90.00 45.00 45.00 40.00 5.00

-----------------------------------------------------------------------

TOTALS 2 90.00 45.00 45.00 40.00 5.00

-----------------------------------------------------------------------

GRAND TOTALS 2 90.00 45.00 45.00 40.00 5.00

Press RETURN to continue:

### Closed Claims Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Closed Claims Report* option lists claims that have been successfully transmitted to the payer, have been returned REJECTED and have been CLOSED using the Close Claim action within the ECME User Screen. The Excel display format of the report displays the Amount Billed and the Amount Billed is only on the Excel display format.

Key The user must hold the BPSMENU and BPS REPORTS keys to view the Closed Claims Report option.

1.  Access the report by entering CLO at the “Select Claim Results and Status Option:” prompt on the Claim Results and Status option screen.

Example 8.1.8-1: Accessing the Closed Claims Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Claim Results and Status \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PAY Payable Claims Report

REJ Rejected Claims Report

ECMP CMOP/ECME Activity Report

REV Reversal Claims Report

NYR Claims Submitted, Not Yet Released

REC Recent Transactions

DAY Totals by Date

CLO Closed Claims Report

NBS Non-Billable Status Report

SPA Spending Account Report

Select Claim Results and Status Option: CLO Closed Claims Report

91. After the user has made selections from the “ALL REPORTS” prompts, the user will be given the following prompts for date range, Released / Not Released / All claims, All / Specific Close Claim Reason, Veteran / TRICARE / CHAMPVA / All Eligibility, Selected Patients or All, Excel display format and device selection.

Example 8.1.8-2: Selecting Specific Close Claim Reason Option

START WITH CLOSE DATE: T-1// T-50

GO TO CLOSE DATE: T// \<Enter\>

Select one of the following:

R RELEASED

N NOT RELEASED

A ALL

Include Rxs - (R)ELEASED or (N)OT RELEASED or (A)LL: RELEASED// ALL

Select one of the following:

S Specific Close Claim Reason

A ALL

Include (S)pecific Close Claim Reason or (A)LL: ALL// \<Enter\>

Select one of the following:

V VETERAN

T TRICARE

C CHAMPVA

A ALL

Display (V)ETERAN or (T)RICARE or (C)HAMPVA or (A)LL: A// ALL

Select one of the following:

P Patient

A ALL

Display Selected (P)atients or (A)LL: ALL// ALL

Data field for billed amount will only be included when the report is captured

for an Excel document. All additional data fields may not be present for all

reports.

Do you want to capture report data for an Excel document? NO// \<Enter\>

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// \<Enter\> IP network

Please wait...

Example 8.1.8-2: Closed Claims Report

ECME CLOSED CLAIMS DETAIL REPORT Print Date: APR 17, 2009@14:21:22 Page: 1

DIVISION(S): ALL Fill Locations: C,M,W Fill type: RT,BB,RS

Insurance: ALL Close Reason: ALL Drugs/Classes: ALL

Eligibility: ALL Patient: ALL

RELEASED PRESCRIPTIONS BY CLOSE DATE: From 03/18/09 through 04/17/09

======================================================================================================

PATIENT NAME Pt.ID ELIG RX# REF/ECME# RX INFO DRUG NDC

CARDHOLD.ID GROUP ID CLOSE DATE/TIME CLOSED BY CLOSE REASON

COB

======================================================================================================

DIVISION: YYYYYYYY

------------------------------------------------------------------------------------------------------

ECME1 INSURANCE

------------------------------------------------------------------------------------------------------

ECMEPATIENT,TWO (XXXX) TRI 102446\$ 0/0000000113727 W RT DS/R DACARBAZINE 100MG INJ 00026-8151-10

12340987 10001 03/20/09 03:55PM ECMEUSER,ONE INVALID NDC FROM CMOP

p

Claim ID: VA2009=5000000021=000010=0005494

54:Non-Matched Product/Service ID Number

SUBTOTALS for INS: ECMEUSER,ONE

ECMEPAT,ONE 1

-----

CLOSED CLAIMS SUBTOTAL 1

SUBTOTALS for DIV:YYYYYYYY

ECMEUSER,ONE 1

-----

CLOSED CLAIMS SUBTOTAL 1

GRAND TOTALS (ALL DIVISIONS) BY BILLER

ECMEUSER,ONE 1

-----

CLOSED CLAIMS GRAND TOTAL 1

### Non-Billable Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *ECME Reports* menu includes a Non-Billable Status Report for ECME Rxs. This report provides users with a tool to easily identify prescriptions that the ePharmacy software determines are not being billed (e.g., OTC products, no insurance on file or not active). The report ensures that prescriptions are billed for TRICARE and / or CHAMPVA patients in a timely manner.

Key The user must hold the BPSMENU and BPS REPORTS keys to view the Non-Billable Status Report option.

1.  Access the report by entering NBS at the “Select Claim Results and Status Option:” prompt on the Claim Results and Status option screen.

Example 8.1.9-1: Accessing the Non-Billable Status Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Claim Results and Status \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PAY Payable Claims Report

REJ Rejected Claims Report

ECMP CMOP/ECME Activity Report

REV Reversal Claims Report

NYR Claims Submitted, Not Yet Released

REC Recent Transactions

DAY Totals by Date

CLO Closed Claims Report

NBS Non-Billable Status Report

SPA Spending Account Report

Select Claim Results and Status Option: NBS Non-Billable Status Report

92. After the user has made selections from the “ALL REPORTS” prompt, the user will be given a series of prompts as shown below:

Example 8.1.9-2: Selecting Non-Billable Status Report option

START WITH TRANSACTION DATE: T-1// T-10 (MAY 29, 2015)

GO TO TRANSACTION DATE: T// T (JUN 08, 2015)

Select one of the following:

R RELEASED

N NOT RELEASED

A ALL

Include Rxs - (R)ELEASED or (N)OT RELEASED or (A)LL: ALL//

R Most Recent

A ALL

Select Most (R)ecent or (A)ll: MOST RECENT//

Select one or more of the following:

V VETERAN

T TRICARE

C CHAMPVA

A ALL

Display (V)ETERAN or (T)RICARE or (C)HAMPVA or (A)LL: ALL//

Select one of the following:

P Patient

A ALL

Display Selected (P)atients or (A)LL: ALL//

Select one of the following:

R Range

A ALL

Select (R)ange for Billed Amount or (A)LL: ALL//

Select one of the following:

S NON-BILLABLE STATUS

A ALL

Select Certain Non-Billable (S)tatus or (A)ll: ALL//

Do you want to capture report data for an Excel document? NO//

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME// HOME (CRT) Right Margin: 80//132

Please wait...

Example 8.1.9-3: Non-Billable Status Report

ECME RXs WITH Non-Billable STATUS REPORT Print Date: Sept 26, 2014@11:41:54 Page: 1

DIVISION(S): GENERIC Fill Locations: C,M,W

Insurance: ALL Drugs/Classes: ALL

Eligibilities: ALL Patient Name: ALL

NON-BILLABLE STATUS: ALL

ALL PRESCRIPTIONS BY TRANSACTION DATE: From 2/22/09 through 09/23/14

=================================================================================================

PATIENT NAME Pt.ID ELIG RX# REF DATE \$DRUG COST

DRUG NDC RELEASED ON RX INFO NON-BILLABLE STATUS

=================================================================================================

DIVISION: GENERIC DIVISION

-------------------------------------------------------------------------------------------------

GENERIC INS

-------------------------------------------------------------------------------------------------

ECMEpatient,One (XXXX) TRI \######\$ 2 04/15/09 51.00

AMITRIPTYLINE 10MG TAB 00182-1018-10 04/15/09 W AC/R Plan not active, local

ECMEpatient, Three (XXXX) VET \######\$ 0 03/10/09 51.00

METHADONE 10MG TAB 000054-8554-2 03/10/09 W EX/N Plan not linked to Payer

----------

SUBTOTALS for INS:GENERIC INS 102.00

COUNT 2

MEAN 51.00

Press RETURN to continue

-------------------------------------------------------------------------------------------------

GENERIC INSURANCE 2

-------------------------------------------------------------------------------------------------

ECMEpatient, Two (XXXX) VET 100574\$ 0 03/05/09 51.00

NEODECADRON OPHTMALIC SOL. 00006-7639-03 03/05/08 W AC/R Plan not found

ECMEpatient, Two (XXXX) VET 100575\$ 0 03/05/09 51.00

PENTAERYTHRITOL 10MG TAB 00725-2064-10 03/05/08 W AC/R Plan Deactivated

SUBTOTALS for INS:GENERIC INSURANCE 2 2142.00

COUNT 42

MEAN 51.00

----------

SUBTOTALS for DIV:GENERIC DIVISION 2244.00

COUNT 44

MEAN 51.00

----------

GRAND TOTALS 2244.00

COUNT 44

MEAN 51.00

Press RETURN to continue:

### Spending Account Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Spending Account Report* option lists the balance from the patient’s spending account after the specific transaction was applied, the amount from the health plan-funded assistance account that was applied to the Patient Pay Amount and the various amounts still to be collected from the patient.

- Access the report by entering SPA at the “Select Claim Results and Status Option:” prompt on the Claim Results and Status option screen.

Example 8.1.10-1: Accessing the Spending Account Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Claim Results and Status \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PAY Payable Claims Report

REJ Rejected Claims Report

ECMP CMOP/ECME Activity Report

REV Reversal Claims Report

NYR Claims Submitted, Not Yet Released

REC Recent Transactions

DAY Totals by Date

CLO Closed Claims Report

NBS Non-Billable Status Report

SPA Spending Account Report

Select Claim Results and Status Option: SPA Spending Account Report

Example 8.1.10-2: Selecting Spending Account Report Option

Select one of the following:

D DIVISION

A ALL

Select Certain Pharmacy (D)ivisions or (A)LL: DIVISION

Select ECME Pharmacy Division(s): XXXXXXX

Selected:

XXXXXXXX

Select ECME Pharmacy Division(s): YYYYYYY CBOC XXX

Selected:

XXXXXXXX

XXXXX

Select ECME Pharmacy Division(s):

Select one of the following:

S Summary

D Detail

Display (S)ummary or (D)etail Format: Detail//

Select one of the following:

I SPECIFIC INSURANCE(S)

A ALL

Select Certain (I)NSURANCE or (A)LL): A// ALL

Select one of the following:

C CMOP

M Mail

W Window

A ALL

Display (C)MOP or (M)ail or (W)indow or (A)LL: ALL//

Select one of the following:

R Real Time Fills

B Backbill

S ReSubmission

A ALL

Display (R)ealTime, (B)ackbills, (P)RO Option, Re(S)ubmission or (A)LL: A//

Select one of the following:

D Drug

C Drug Class

A ALL

Display Specific (D)rug or Drug (C)lass or (A)LL: ALL//

START WITH TRANSACTION DATE: T-1//

GO TO TRANSACTION DATE: T//

Select one of the following:

R RELEASED

N NOT RELEASED

A ALL

Include Rxs - (R)ELEASED or (N)OT RELEASED or (A)LL: RELEASED//

Select one of the following:

S Specific Reject Code

A ALL

Include (S)pecific Reject Code or (A)LL: ALL//

Do you want to capture report data for an Excel document? NO//

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME//

Please wait...

Example 8.1.10-3: Spending Account Report – Summary

ECME SPENDING ACCOUNT REPORT SUMMARY REPORT Print Date: DEC 02, 2011@16:51:34 Page: 1

DIVISION(S): ALL Fill Locations: C,M,W Fill type: RT,BB,P2,RS

Insurance: ALL Drugs/Classes: ALL

ALL PRESCRIPTIONS BY TRANSACTION DATE: From 06/05/11 through 12/02/11

====================================================================================================================================

PATIENT NAME Pt.ID RX# REF/ECME# DATE \$BILLED \$INS RESPONSE \$COLLECT

DRUG RX INFO INS GROUP# INS GROUP NAME BILL#

\$PROVIDER NETWORK \$BRAND DRUG \$NON-PREF FORM \$BRAND NON-PREF FORM \$COVERAGE GAP \$HEALTH ASST \$SPEND ACCT REMAINING

====================================================================================================================================

DIVISION: XXXXXX

------------------------------------------------------------------------------------------------------------------------------------

---------- ---------- ----------

SUBTOTALS for INS:EPHARM INSURANCE 12.00 999999.99 0.00

0.00 0.00 0.00 0.00 0.00 0.00 12.30

COUNT 1 1 1

1 1 1 1 1 1 1

MEAN 12.00 999999.99 0.00

0.00 0.00 0.00 0.00 0.00 0.00 12.30

---------- ---------- ----------

SUBTOTALS for INS:EXPRESS SCRIPTS 999999.99 999999.99 0.00

0.00 0.00 0.00 0.00 0.00 0.00 15.41

COUNT 1 1 1

1 1 1 1 1 1 1

MEAN 999999.99 999999.99 0.00

0.00 0.00 0.00 0.00 0.00 0.00 15.41

---------- ---------- ----------

SUBTOTALS for DIV:XXXXXX 1000011.99 1999999.98 0.00

0.00 0.00 0.00 0.00 0.00 0.00 27.71

COUNT 2 2 2

2 2 2 2 2 2 2

MEAN 500006.00 999999.99 0.00

0.00 0.00 0.00 0.00 0.00 0.00 13.86

---------- ---------- ----------

GRAND TOTALS 1000011.99 1999999.98 0.00

0.00 0.00 0.00 0.00 0.00 0.00 27.71

COUNT 2 2 2

2 2 2 2 2 2 2

MEAN 500006.00 999999.99 0.00

0.00 0.00 0.00 0.00 0.00 0.00 13.86

Press RETURN to continue:

Example 8.1.10-4: Spending Account Report – Detail

ECME SPENDING ACCOUNT REPORT DETAIL REPORT Print Date: DEC 02, 2011@17:16:36 Page: 1

DIVISION(S): ALL Fill Locations: C,M,W Fill type: RT,BB,P2,RS

Insurance: ALL Drugs/Classes: ALL

ALL PRESCRIPTIONS BY TRANSACTION DATE: From 06/05/11 through 12/02/11

====================================================================================================================================

PATIENT NAME Pt.ID RX# REF/ECME# DATE \$BILLED \$INS RESPONSE \$COLLECT

DRUG RX INFO INS GROUP# INS GROUP NAME BILL#

\$PROVIDER NETWORK \$BRAND DRUG \$NON-PREF FORM \$BRAND NON-PREF FORM \$COVERAGE GAP \$HEALTH ASST \$SPEND ACCT REMAINING

====================================================================================================================================

DIVISION: XXXXXX

------------------------------------------------------------------------------------------------------------------------------------

EPHARM INSURANCE

------------------------------------------------------------------------------------------------------------------------------------

OPCOB,ONECNF (166P) 2719307 0/4316136 08/24/11 12.00 999999.99 0.00

ATENOLOL 25MG TAB W P2 EX/R T00010 EPHARM INSURANCE K1000F7

0.00 0.00 0.00 0.00 0.00 0.00 12.30

Claim ID: VA2011=4050000015=000010=0001047

---------- ---------- ----------

SUBTOTALS for INS:EPHARM INSURANCE 12.00 999999.99 0.00

0.00 0.00 0.00 0.00 0.00 0.00 12.30

COUNT 1 1 1

1 1 1 1 1 1 1

MEAN 12.00 999999.99 0.00

0.00 0.00 0.00 0.00 0.00 0.00 12.30

EXPRESS SCRIPTS

------------------------------------------------------------------------------------------------------------------------------------

OPCOB,ONECNF (166P) 2719307 0/4316136 08/24/11 999999.99 999999.99 0.00

ATENOLOL 25MG TAB W P2 EX/R T100000 EXPRESS SCRIPTS K1000F6

0.00 0.00 0.00 0.00 0.00 0.00 15.41

Claim ID: VA2011=4050000015=000010=0001046

---------- ---------- ----------

SUBTOTALS for INS:EXPRESS SCRIPTS 999999.99 999999.99 0.00

0.00 0.00 0.00 0.00 0.00 0.00 15.41

COUNT 1 1 1

1 1 1 1 1 1 1

MEAN 999999.99 999999.99 0.00

0.00 0.00 0.00 0.00 0.00 0.00 15.41

---------- ---------- ----------

SUBTOTALS for DIV:XXXXXX 1000011.99 1999999.98 0.00

0.00 0.00 0.00 0.00 0.00 0.00 27.71

COUNT 2 2 2

2 2 2 2 2 2 2

MEAN 500006.00 999999.99 0.00

0.00 0.00 0.00 0.00 0.00 0.00 13.86

---------- ---------- ----------

GRAND TOTALS 1000011.99 1999999.98 0.00

0.00 0.00 0.00 0.00 0.00 0.00 27.71

COUNT 2 2 2

2 2 2 2 2 2 2

MEAN 500006.00 999999.99 0.00

0.00 0.00 0.00 0.00 0.00 0.00 13.86

Press RETURN to continue:

### Duplicate Claims Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The *Duplicate Claims Report* option lists claims with status of Duplicate of Approved, Duplicate of Paid, and Duplicate of Capture.
- Access the report by entering DUP at the “Select Claim Results and Status Option:” prompt on the Claim Results and Status option screen.

Example 8.1.11-1: Accessing the Duplicate Claims Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Claim Results and Status \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

PAY Payable Claims Report

REJ Rejected Claims Report

ECMP CMOP/ECME Activity Report

REV Reversal Claims Report

NYR Claims Submitted, Not Yet Released

REC Recent Transactions

DAY Totals by Date

CLO Closed Claims Report

NBS Non-Billable Status Report

SPA Spending Account Report

DUP Duplicate Claims Report

Select Claim Results and Status Option: DUP Duplicate Claims Report

Example 8.1.11-2: Selecting Duplicate Claims Report Option

Select one of the following:

D DIVISION

A ALL

Select Certain Pharmacy (D)ivisions or (A)LL: DIVISION

Select ECME Pharmacy Division(s): XXXXXXX

Selected:

XXXXXXXX

Select ECME Pharmacy Division(s): YYYYYYY CBOC XXX

Selected:

XXXXXXXX

XXXXX

Select ECME Pharmacy Division(s):

Select one of the following:

S Summary

D Detail

Display (S)ummary or (D)etail Format: Detail//

Select one of the following:

I SPECIFIC INSURANCE(S)

A ALL

Select Certain (I)NSURANCE or (A)LL): A// ALL

START WITH TRANSACTION DATE: T-1//

GO TO TRANSACTION DATE: T//

Select one of the following:

R RELEASED

N NOT RELEASED

A ALL

Include Rxs - (R)ELEASED or (N)OT RELEASED or (A)LL: RELEASED//

Select one or more of the following:

V VETERAN

T TRICARE

C CHAMPVA

A ALL

Display (V)ETERAN or (T)RICARE or (C)HAMPVA or (A)LL: A//

Select one or more of the following:

S DUPLICATE OF APPROVED

D DUPLICATE OF PAID

Q DUPLICATE OF CAPTURED

A ALL

Display (S)Dup of Approved or (D)Dup of Paid or (Q)Dup of Capture or (A)LL: A//

Select one of the following:

P Patient

A ALL

Display Selected (P)atients or (A)LL: ALL//

Select one of the following:

R Range

A ALL

Select (R)ange for Billed Amount or (A)LL: ALL//

Data fields VA Ingredient Cost, VA Dispensing Fee, Ingredient Cost Paid

and Dispensing Fee Paid will only be included when the report is captured

for an Excel document. All additional data fields may not be present for all

reports.

Do you want to capture report data for an Excel document? NO//

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME//

Please wait...

Example 8.1.11-3: Duplicate Claims Report – Summary

ECME DUPLICATE CLAIMS SUMMARY REPORT Print Date: NOV 12, 2020@11:44:51 Page: 1

DIVISION(S): ALL Fill Locations: ALL Fill Type: ALL

Insurance: ALL Drugs/Classes: ALL

Eligibility: CVA,TRI,VET Patient: ALL

Status: ALL

ALL PRESCRIPTIONS BY TRANSACTION DATE: From 01/01/15 through 10/01/20

Status Codes: S= Duplicate of Approved, D= Duplicate of Paid, Q= Duplicate of Capture

====================================================================================================================================

PATIENT NAME Pt.ID ELIG REF/ECME# DATE \$BILLED \$INS RESPONSE \$COLLECT Pt.RESP(INS)

DRUG NDC RELEASED ON RX INFO BILL# COB STATUS

====================================================================================================================================

DIVISION: XXXXXXXX XXXX

------------------------------------------------------------------------------------------------------------------------------------

---------- ---------- ---------- ----------

SUBTOTALS for INS:CAREMARK (610029) 99.99 9.99 9.99 9.99

COUNT 1 1 1 1

MEAN 99.99 9.99 9.99 9.99

---------- ---------- ---------- ----------

SUBTOTALS for INS:CAREMARK FEP (610239) 99.99 9.99 9.99 9.99

COUNT 1 1 1 1

MEAN 99.99 9.99 9.99 9.99

---------- ---------- ---------- ----------

SUBTOTALS for INS:MEDIMPACT 99.99 9.99 9.99 9.99

COUNT 1 1 1 1

MEAN 99.99 9.99 9.99 99.99

---------- ---------- ---------- ----------

SUBTOTALS for DIV:XXXXXXXX XXXX 99.99 99.99 99.99 99.99

COUNT 3 3 3 3

MEAN 99.99 9.99 9.99 9.99

---------- ---------- ---------- ----------

GRAND TOTALS 999999.99 999999.9 999999.99 999999.99

COUNT 3 3 3 3

MEAN 99.99 9.99 9.99 9.99

Press RETURN to continue:

Example 8.1.11-4: Duplicate Claims Report – Detail

ECME DUPLICATE CLAIMS DETAIL REPORT Print Date: NOV 12, 2020@12:45:40 Page: 1

DIVISION(S): ALL Fill Locations: ALL Fill Type: ALL

Insurance: ALL Drugs/Classes: ALL

Eligibility: CVA,TRI,VET Patient: ALL

Status: ALL

ALL PRESCRIPTIONS BY TRANSACTION DATE: From 01/01/15 through 10/01/20

Status Codes: S= Duplicate of Approved, D= Duplicate of Paid, Q= Duplicate of Capture

====================================================================================================================================

PATIENT NAME Pt.ID ELIG REF/ECME# DATE \$BILLED \$INS RESPONSE \$COLLECT Pt.RESP(INS)

DRUG NDC RELEASED ON RX INFO BILL# COB STATUS

====================================================================================================================================

DIVISION: XXXXXXXX XXXX

------------------------------------------------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------------------------------------------------

CAREMARK (610029)

------------------------------------------------------------------------------------------------------------------------------------

XXXXX,XXXXXX (9999) VET 0/000009999999 03/09/15 99.99 0.99 0.99 9.99

PREDNISONE 20MG TAB 00099-0099-99 03/09/15 W RT EX/R XXXXXXX p D

---------- ---------- ---------- ----------

SUBTOTALS for INS:CAREMARK (610029) 99.99 0.99 0.99 9.99

COUNT 1 1 1 1

MEAN 99.99 0.99 0.99 9.99

------------------------------------------------------------------------------------------------------------------------------------

CAREMARK FEP (610239)

------------------------------------------------------------------------------------------------------------------------------------

XXXXXXXX,XXXXX (9999) VET 1/0000099999999 06/22/15 99.99 9.99 9.99 9.99

PRECISION XTRA (GLUCOSE) TE 99999-9999-99 06/18/15 C RS AC/R XXXXXXX p D

---------- ---------- ---------- ----------

SUBTOTALS for INS:CAREMARK FEP (610239) 99.99 9.99 9.99 9.99

COUNT 1 1 1 1

MEAN 99.99 9.99 9.99 9.99

Press RETURN to continue, '^' to exit:

ECME DUPLICATE CLAIMS DETAIL REPORT Print Date: NOV 12, 2020@12:45:40 Page: 2

DIVISION(S): ALL Fill Locations: ALL Fill Type: ALL

Insurance: ALL Drugs/Classes: ALL

Eligibility: CVA,TRI,VET Patient: ALL

Status: ALL

ALL PRESCRIPTIONS BY TRANSACTION DATE: From 01/01/15 through 10/01/20

Status Codes: S= Duplicate of Approved, D= Duplicate of Paid, Q= Duplicate of Capture

====================================================================================================================================

PATIENT NAME Pt.ID ELIG REF/ECME# DATE \$BILLED \$INS RESPONSE \$COLLECT Pt.RESP(INS)

DRUG NDC RELEASED ON RX INFO BILL# COB STATUS

====================================================================================================================================

DIVISION: XXXXXXXX XXXX

------------------------------------------------------------------------------------------------------------------------------------

MEDIMPACT

------------------------------------------------------------------------------------------------------------------------------------

XXXXXX,XXX XXXXXX (9999) VET 1/000009999999 01/10/15 99.99 9.99 9.99 99.99

BUPROPION HCL 150MG 12HR SA 99999-9999-99 01/12/15 C RT \*\*/R XXXXXXX p D

---------- ---------- ---------- ----------

SUBTOTALS for INS:MEDIMPACT 99.99 9.99 9.99 99.99

COUNT 1 1 1 1

MEAN 99.99 9.99 9.99 99.99

---------- ---------- ---------- ----------

SUBTOTALS for DIV:XXXXXXXX XXXX 99.99 99.99 99.99 99.99

COUNT 3 3 3 3

MEAN 99.99 9.99 9.99 9.99

---------- ---------- ---------- ----------

GRAND TOTALS 999999.99 999999.99 999999.99 999999.99

COUNT 3 3 3 3

MEAN 99.99 9.99 9.99 9.99

Press RETURN to continue:

## Other Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Other Reports* option allows the user to access lists of electronic claims formats and NCPDP V. D0 fields.

Access the Other Reports option by entering OTH at the “Select Pharmacy Electronic Claims Reports Option:” prompt on the Pharmacy Electronic Claims Reports option screen.

Example 8.2-1: Accessing the Other Reports Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX \*

\* Pharmacy Electronic Claims Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

CLA Claim Results and Status ...

OTH Other Reports ...

Select Pharmacy Electronic Claims Reports Option: OTH Other Reports

Example 8.2-2: Displaying Other Reports Options

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX \*

\* Other Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

CRI ECME Claims-Response Inquiry

PAY Payer Sheet Detail Report

PHAR ECME Setup - Pharmacies Report

TAT Turn-around time statistics

VER View ePharmacy Rx

OPR OPECC Productivity Report

Select Other Reports Option:

### ECME Claims-Response Inquiry Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *ECME Claims-Response Inquiry* option allows the user to enter a VA Claim ID and see the transaction data, the claim data sent to the third-party payer and the response data that was returned. This option may assist the sites and / or the VistA Maintenance Project (VMP) team in determining the cause of a reject that is received from a payer.

Access the *ECME Claims-Response Inquiry* option by entering CRI at the “Select Other Reports Option:” prompt on the Pharmacy Electronic Claims Reports, Other Reports option screen.

Example 8.2.1-1: Accessing the ECME Claims-Response Inquiry Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX \*

\* Other Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

CRI ECME Claims-Response Inquiry

PAY Payer Sheet Detail Report

PHAR ECME Setup - Pharmacies Report

TAT Turn-around time statistics

VER View ePharmacy Rx

OPR OPECC Productivity Report

Select Other Reports Option: CRI ECME Claims-Response Inquiry

Example 8.2.1-2: ECME Claims-Response Inquiry Option

Select VA Claim ID: VA2009=5000000021=105220=0005524 VA2009=5000000021=105220=0

005524

> **NOTE:** This report contains three separate sections - transaction data, claims

data, and response data. There will be a page break/form feed after

each section regardless of the page length specified in the device input.

DEVICE: HOME// \<Enter\> UCX/TELNET Right Margin: 80// \<Enter\>

ECME Claims-Response Inquiry Report Print Date: 04/17/09

VA CLAIM ID: VA2009=5000000021=105220=0005524

BPS TRANSACTION/BPS LOG OF TRANSACTION DATA:

ENTRY#: 113414.00042 STATUS: 99

PHARMACY: PHARM1 PRESCRIPTION \#: 102179

RXI-INTERNAL (c): 113414

PLAN NAME: COB INSURANCE PHARMACY PLAN ID: VA105220

CLAIM IEN (c): 5524 RESPONSE IEN (c): 5369

Press RETURN to continue, '^' to exit:

BPS CLAIMS FILE DATA:

CLAIM ID: VA2009=5000000021=105220=0005524

ELECTRONIC PAYER: MNMEDB1 TRANSMIT FLAG: YES (POINT OF SALE)

TRANSMITTED ON: APR 17,2009@14:54:27 CREATED ON: APR 17,2009@14:54:27

TRANSACTION: 113414.00042 PATIENT NAME: ECMEpatient,One

GROUP INSURANCE PLAN: COB INSURANCE BIN NUMBER: 610459

VERSION RELEASE NUMBER: D0 TRANSACTION CODE: B1

PROCESSOR CONTROL NUMBER: MHCP TRANSACTION COUNT: 1

SOFTWARE VENDER CERT ID: SERVICE PROVIDER ID: 5000000021

SERVICE PROVIDER ID QUAL: 01 GROUP ID: C19977

CARDHOLDER ID: C2XXXXXX PERSON CODE: C301

DATE OF BIRTH: C4XXXXXXXX PATIENT GENDER CODE: MALE

PATIENT RELATIONSHIP CODE: CARDHOLDER

PLACE OF SERVICE: C700 ELIGIBILITY CLARIFICATION CODE: C90

PATIENT FIRST NAME: CAONE PATIENT LAST NAME: CBECMEPATIENT

CARDHOLDER FIRST NAME: CCONE

CARDHOLDER LAST NAME: CDECMEPATIENT

HOME PLAN: CE36

PATIENT STREET ADDRESS: CM13 DFG

PATIENT CITY ADDRESS: CNXXXXXXXX

PATIENT STATE PROV ADDRESS: COXX PATIENT ZIP POSTAL ZONE: CPXXXXX

PATIENT PHONE NUMBER: CQXXXXXXXXX PATIENT ID QUALIFIER: CX01

PATIENT ID: CYXXXXXXXX EMPLOYER ID: CZ

SMOKER INDICATOR: 1C PREGNANCY INDICATOR: 2C

FACILITY ID: 8C

MEDICATION ORDER: 1 MEDICATION NAME: BETAZOLE 50MG/ML INJ

PRESCRIPTION NUMBER: 102179 OTHER COVERAGE CODE: C800

ALTERNATE ID: CW00000000000000000000

COB OTHER PAYMENT COUNTER: 4C1 OTHER PAYER COVERAGE TYPE: 5C01

OTHER PAYER ID QUALIFIER: 6C03 OTHER PAYER ID: 7C123456

OTHER PAYER DATE: APR 14,2009 OTHER PAYER AMOUNT PAID COUNT: HB1

OTHER PAYER REJECT COUNT: 5E00

OTHER PAYER AMT PAID QUALIFIER: HC08 OTHER PAYER AMOUNT PAID: DV00400{

DATE OF SERVICE: APR 14,2009 PRESCRIPTION REFERENCE NUMBER: D20113414

FILL NUMBER: D304 DAYS SUPPLY: D5001

COMPOUND CODE: D61

PRODUCT SERVICE ID: D700002143916

DISPENSE AS WRITTEN: D80 INGREDIENT COST SUBMITTED: D90000510{

PRESCRIBER ID: DBXXXXXXXXX DISPENSING FEE SUBMITTED: DC00000000

DATE PRESCRIPTION WRITTEN: DE20090112

NUMBER OF REFILLS AUTHORIZED: DF05 LEVEL OF SERVICE: DI00

PRESCRIPTION ORIGIN CODE: DJ1 SUBMISSION CLARIFICATION CODE: DK00

BASIS OF COST DETERMINATION: DN07 USUAL AND CUSTOMARY CHARGE: DQ0000510{

SPECIAL PACKAGING INDICATOR: DT0 GROSS AMOUNT DUE: DU0000510{

PRESCRIBER LAST NAME: ECMEPRESCRIBER

OTHER PAYER AMOUNT: DV00400{

PATIENT PAID AMOUNT SUBMITTED: DX0000000{

PRODUCT SERVICE ID QUALIFIER: E103 QUANTITY DISPENSED: E70000001000

ORIGINALLY PRESCRIBED QUANTITY: EB0000001000

SCHEDULED RX ID NUMBER: EK000000000000

PRESCRIPTION SERVICE REFERENCE: EM1 QUANTITY PRESCRIBED: ET0000001000

PRIOR AUTHORIZATION TYPE CODE: EU00

PRIOR AUTHORIZATION SUBMITTED: EV00000000000

INTERMEDIARY AUTH TYPE ID: EW00

INTERMEDIARY AUTHORIZATION ID: EX

PRESCRIBER ID QUALIFIER: EZ01 PRESCRIBER LOCATION CODE: 1E

PC PROVIDER LOCATION CODE: H5036 PC PROVIDER LAST NAME: 4EECMEPROVIDER

PROFESSIONAL FEE SUBMITTED: BE00000000

FLAT SALES TAX SUBMITTED: HA00000000

PERCENTAGE SALES TAX SUBMITTED: GE0000000{

PERCENTAGE SALES TAX RATE: HE0000000 PERCENTAGE SALES TAX BASIS: JE

PRESCRIBER PHONE NUMBER: PMXXXXXXXXXX

DATE OF SERVICE: 20090414 PLAN ID: FOECME INS

RAW DATA SENT:

61045951B1MHCP 1015000000021 20090414

AM01CX01CYXXXXXXXXX C419600101C51CAONECBECMEPATIENT CM13

DFG CNXXXXXXXX COXXCPXXXXX CQXXXXXXXXXXC700

CZ 1C 2C

AM04C2234234CCONECDECMEPATIENT CE36 FOECME INSC908C C19977

C301 C61

AM07EM1D20113414E103D700002143916 E70000001000D304D5001D61D80DE20090112D

F05DJ1DK00ET0000001000C800DT0EB0000001000CW00000000000000000000EK000000000000DI0

0EU00EV00000000000EW00EX

AM02

AM03EZ01DBXXXXXXXXXX 1E ECMEPRESCRIBER H50364EECMEPROVIDER

AM054C15C016C037C123456 E820090414HB1DV00400{

AM11D90000510{DC00000000BE00000000DX0000000{HA00000000GE0000000{HE0000000JE DQ

0000510{DU0000510{DN07

Press RETURN to continue, '^' to exit:

BPS RESPONSE FILE DATA:

BPS CLAIM: VA2009=5000000021=105220=0005524

DATE RESPONSE RECEIVED: APR 17, 2009@14:54:30

VERSION RELEASE NUMBER: D0 TRANSACTION CODE: B1

TRANSACTION COUNT: 1 SERVICE PROVIDER ID: XXXXXXXXXX

SERVICE PROVIDER ID QUALIFIER: 01 DATE OF SERVICE: APR 14,2009

RESPONSE STATUS: REJECTED

MESSAGE: EV161-MANDATORY FIELD HC MISSING IN SEG 05

MEDICATION ORDER: 1 TRANSACTION RESPONSE STATUS: REJECTED

PRESCRIPTION RESPONSE STATUS: REJECTED CLAIM

REJECT COUNT: 04

REJECT CODE: 85 (Claim Not Processed)

REJECT CODE: NN (Transaction Rejected At Switch Or Intermediary

REJECT CODE: R8 (Syntax Error)

REJECT CODE: HC (M/I Other Payer Amount Paid Qualifier)

REJECT CODE: 79 (REFILL TOO SOON)

NEXT AVAIL FILL DATE: APR 20,2009

RAW DATA RECEIVED:

VA2009=XXXXXXXXXX=105220=000xxxxxxB11R01XXXXXXXXXX

20090414\X1E\\X1C\AM20\X1C\F4EV161-MANDATORY FIELD HC MISSING IN SEG

05\X1D\\X1E\\X1C\AM21\X1C\ANR\X1C\FA04\X1C\FB85\X1C\FBNN\X1C\FBR8\X1C\FBHC

Press RETURN to continue:

### Payer Sheet Detail Report Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Payer Sheet Detail Report* option allows the user to list the information on payer sheets used for electronic claims. Payer sheets are templates defined by each payer used to create NCPDP transmissions. The sheets indicate which fields to send in the transmissions, as well as the acceptable values that may appear in the fields. The user may also express conditions for when values are to be used.

Access the Payer Sheet Detail Report option by entering PAY at the “Select Other Reports Option:” prompt on the Pharmacy Electronic Claims Reports, Other Reports option screen.

Example 8.2.2-1: Accessing the Payer Sheet Detail Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Other Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

CRI ECME Claims-Response Inquiry

PAY Payer Sheet Detail Report

PHAR ECME Setup - Pharmacies Report

TAT Turn-around time statistics

VER View ePharmacy Rx

OPR OPECC Productivity Report

Select Other Reports Option: PAY Payer Sheet Detail Report

Example 8.2.2-2: Payer Sheet Detail Report Option

Select Payer Sheet: ABCTEST1

DEVICE: HOME// IP network

Payer Sheet Detail Report Print Date: 09/09/05 Page: 1

Payer Sheet Name: ABCTEST1 Version Number: 7

Status: PRODUCTION NCPDP Version: Version D.0

Seq Field Field Name Proc Mode

--- ----- ---------- ---------

\*\*\* Transaction Header Segment \*\*\*

1 101-A1 BIN NUMBER S

2 102-A2 VERSION/RELEASE NUMBER S

3 103-A3 TRANSACTION CODE S

5 104-A4 PROCESSOR CONTROL NUMBER S

17 202-B2 SERV PROVIDER ID QUALIFIER S

19 201-B1 SERVICE PROVIDER ID S

21 401-D1 DATE FILLED S

Press RETURN to continue, '^' to exit: \<Enter\>

Payer Sheet Detail Report Print Date: 09/09/05 Page: 2

Payer Sheet Name: ABCTEST1 Version Number: 7

Seq Field Field Name Proc Mode

--- ----- ---------- ---------

\*\*\* Transaction Header Segment \*\*\*

22 110-AK SOFTWARE VENDOR/CERT ID S

\*\*\* Patient Segment \*\*\*

31 111-AM SEGMENT IDENTIFICATION S

33 331-CX PATIENT ID QUALIFIER S

35 332-CY PATIENT ID S

36 304-C4 DATE OF BIRTH S

37 305-C5 SEX CODE S

39 307-C7 CUSTOMER LOCATION S

40 335-2C PREGNANCY INDICATOR S

\*\*\* Insurance Segment \*\*\*

49 111-AM SEGMENT IDENTIFICATION S

51 302-C2 CARDHOLDER ID NUMBER S

53 301-C1 GROUP NUMBER S

Press RETURN to continue, '^' to exit: \<Enter\>

Payer Sheet Detail Report Print Date: 09/09/05 Page: 3

Payer Sheet Name: ABCTEST1 Version Number: 7

Seq Field Field Name Proc Mode

--- ----- ---------- ---------

\*\*\* Insurance Segment \*\*\*

54 306-C6 RELATIONSHIP CODE S

\*\*\* Claim Segment \*\*\*

64 111-AM SEGMENT IDENTIFICATION S

66 455-EM RX/SERVICE REF NUMBER QUAL S

69 402-D2 PRESCRIPTION NUMBER S

71 436-E1 PRODUCT/SERV ID QUAL S

73 407-D7 PRODUCT/SERVICE ID S

75 442-E7 QUANTITY DISPENSED S

77 403-D3 NEW/REFILL CODE S

78 405-D5 DAYS SUPPLY S

79 406-D6 COMPOUND CODE S

80 408-D8 OTHER COVERAGE CODE S

82 414-DE DATE PRESCRIPTION WRITTEN S

85 308-C8 OTHER COVERAGE CODE S

Press RETURN to continue, '^' to exit: \<Enter\>

Payer Sheet Detail Report Print Date: 09/09/05 Page: 4

Payer Sheet Name: ABCTEST1 Version Number: 7

Seq Field Field Name Proc Mode

--- ----- ---------- ---------

\*\*\* Claim Segment \*\*\*

87 429-DT UNIT DOSE INDICATOR S

89 453-EJ ORIG PRESCR PROD/SERV ID QUAL S

92 445-EA ORIG PRESCRIBED PROD/SERV CODE S

95 446-EB ORIGINALLY PRESCRIBED QTY S

97 418-DI LEVEL OF SERVICE S

99 461-EU PRIOR AUTHORIZATION TYPE CODE S

102 462-EV PRIOR AUTHORIZATION NUM SUB S

106 463-EW INTERMED AUTH TYPE ID S

109 464-EX INTERMEDIARY AUTHORIZATION ID S

112 343-HD DISPENSING STATUS S

114 344-HF QTY INTENDED TO BE DISPENSED S

117 345-HG DAYS SUPPLY INTEND TO BE DISP S

\*\*\* Pharmacy Provider Segment \*\*\*

127 111-AM SEGMENT IDENTIFICATION S

Press RETURN to continue, '^' to exit: \<Enter\>

Payer Sheet Detail Report Print Date: 09/09/05 Page: 5

Payer Sheet Name: ABCTEST1 Version Number: 7

Seq Field Field Name Proc Mode

--- ----- ---------- ---------

\*\*\* Pharmacy Provider Segment \*\*\*

129 465-EY PROVIDER ID QUALIFIER S

131 444-E9 PROVIDER ID S

\*\*\* Prescriber Segment \*\*\*

140 111-AM SEGMENT IDENTIFICATION S

142 466-EZ PRESCRIBER ID QUALIFIER S

144 411-DB PRESCRIBER ID S

146 427-DR PRESCRIBER LAST NAME S

148 498-PM PRESCRIBER TELEPHONE NUMBER S

150 468-2E PRIMARY CARE PROV ID QUAL S

153 421-DL PRIMARY PRESCRIBER S

155 469-H5 PRIM CARE PROV LOCATION CODE S

158 470-4E PRIM CARE PROVIDER LAST NAME S

Press RETURN to continue, '^' to exit: \<Enter\>

Payer Sheet Detail Report Print Date: 09/09/05 Page: 6

Payer Sheet Name: ABCTEST1 Version Number: 7

Seq Field Field Name Proc Mode

--- ----- ---------- ---------

\*\*\* COB/Other Payments Segment \*\*\*

168 111-AM SEGMENT IDENTIFICATION S

170 337-4C COB/OTHER PAYMENTS COUNTER S

172 338-5C OTHER PAYER COVERAGE TYPE S

174 339-6C OTHER PAYER ID QUALIFIER S

177 340-7C OTHER PAYER ID S

180 443-E8 Other Payer Date S

182 341-HB OTHER PAYER AMOUNT PAID COUNT S

185 342-HC OTH PYR AMOUNT PAID QUAL. S

188 431-DV OTHER PAYOR AMOUNT S

190 471-5E OTHER PAYER REJECT COUNT S

192 472-6E OTHER PAYER REJECT CODE S

\*\*\* Workers' Compensation Segment \*\*\*

202 111-AM SEGMENT IDENTIFICATION S

205 434-DY DATE OF INJURY S

Press RETURN to continue, '^' to exit: \<Enter\>

Payer Sheet Detail Report Print Date: 09/09/05 Page: 7

Payer Sheet Name: ABCTEST1 Version Number: 7

Seq Field Field Name Proc Mode

--- ----- ---------- ---------

\*\*\* Workers' Compensation Segment \*\*\*

\*\*\* DUR/PPS Segment \*\*\*

213 111-AM SEGMENT IDENTIFICATION S

215 473-7E DUR/PPS CODE COUNTER S

218 439-E4 DUR CONFLICT CODE S

220 440-E5 DUR INTERVENTION CODE S

222 441-E6 DUR OUTCOME CODE S

224 474-8E DUR/PPS LEVEL OF EFFORT S

227 475-J9 DUR CO-AGENT ID QUALIFIER S

230 476-H6 DUR CO-AGENT ID S

\*\*\* Pricing Segment \*\*\*

240 111-AM SEGMENT IDENTIFICATION S

242 409-D9 INGREDIENT COST S

244 412-DC DISPENSING FEE SUBMITTED S

Press RETURN to continue, '^' to exit: \<Enter\>

Payer Sheet Detail Report Print Date: 09/09/05 Page: 8

Payer Sheet Name: ABCTEST1 Version Number: 7

Seq Field Field Name Proc Mode

--- ----- ---------- ---------

\*\*\* Pricing Segment \*\*\*

246 477-BE PROFESSIONAL SERV FEE SUBMIT S

249 433-DX PATIENT PAID AMOUNT S

252 481-HA FLAT SALES TAX AMOUNT SUBMIT S

255 482-GE PERCENTAGE SALES TAX AMT SUB S

258 484-JE PERCENT SALES TAX BASIS SUB S

261 426-DQ USUAL & CUSTOMARY CHARGE S

264 430-DU GROSS AMOUNT DUE S

266 423-DN BASIS OF COST DETERMINATION S

\*\*\* Coupon Segment \*\*\*

275 111-AM SEGMENT IDENTIFICATION S

277 485-KE COUPON TYPE S

278 486-ME COUPON NUMBER S

279 487-NE COUPON VALUE AMOUNT S

Press RETURN to continue, '^' to exit: \<Enter\>

Payer Sheet Detail Report Print Date: 09/09/05 Page: 9

Payer Sheet Name: ABCTEST1 Version Number: 7

Seq Field Field Name Proc Mode

--- ----- ---------- ---------

\*\*\* Compound Segment \*\*\*

288 111-AM SEGMENT IDENTIFICATION S

290 450-EF Compound Dose Form Desc Code S

293 451-EG Compound Dispense Unt Form Ind S

295 452-EH Compound Route of Admin S

297 447-EC Compound Ingred Comp Count S

299 488-RE Compound Product ID Qualifier S

301 489-TE Compound Product ID S

302 448-ED Compound Ingredient Quantity S

304 449-EE Compound Ingredient Drug Cost S

307 490-UE Comp Ingred Basis Cost Determ S

Press RETURN to continue:

### ECME Setup – Pharmacies Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will produce a report that displays setup information for each pharmacy configured for a facility.

Access the report by entering PHAR at the “Select Other Reports Option:” prompt on the Pharmacy Electronic Claims Reports, Other Reports option screen.

Example 8.2.3-1: Accessing ECME Setup – Pharmacies Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Other Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

CRI ECME Claims-Response Inquiry

PAY Payer Sheet Detail Report

PHAR ECME Setup - Pharmacies Report

TAT Turn-around time statistics

VER View ePharmacy Rx

OPR OPECC Productivity Report

Select Setup (Configuration) Reports Option: PHAR ECME Setup - Pharmacies Report

DEVICE: IP network

Example 8.2.3-2: ECME Setup - Pharmacies Report Option

BPS PHARMACIES LIST SEP 9,2005 07:17 PAGE 1

-------------------------------------------------------------------------------

NUMBER: 2

NAME: XXXXXXXXX NCPDP \#: XXXXXXX

DEFAULT DEA \#: AGXXXXX CMOP SWITCH: CMOP ON

AUTO-REVERSE PARAMETER: 0 STATUS: ACTIVE

SITE ADDRESS 1: 101 MAIN STREET

SITE CITY: XXXXXXXXX SITE STATE: XXXXX

SITE ZIP CODE: XXXXX SITE ADDRESS NAME: 101 MAIN STREET

HOURS OF OPERATION: 24 START DAY RANGE: MON

END DAY RANGE: MON START HOUR RANGE: 0800

END HOUR RANGE: 1600~TUE NPI: XXXXXXXXXX

DATE/TIME OF LAST NPI CHANGE: OCT 10, 2006@15:05:05

OUTPATIENT SITE: XXXXXXXXXXXX

REMITTANCE ADDRESS NAME: MAIN REMIT ADDRESS 1: 101 MAIN STREET

REMIT CITY: XXXXXXXXX REMIT STATE: XXXXXX

REMIT ZIP: XXXXX VA CONTACT: CONTACT,ONE

VA ALTERNATE CONTACT: CONTACT,ONE VA LEAD PHARMACIST: CONTACT,ONE

VA LEAD PHARMACIST LICENSE \#: XXXXXXXX

Monday Close Time: 1600 Tuesday Close Time: 1600

Wednesday Close Time: 1600 Thursday Close Time: 1600

Friday Close Time: 1600 Saturday Close Time: 1600

Monday Open Time: 0800 Tuesday Open Time: 0800

BPS PHARMACIES LIST SEP 09, 2005@17:17 PAGE 2

-------------------------------------------------------------------------------

Wednesday Open Time: 0800 Thursday Open Time: 0800

Friday Open Time: 0800 Saturday Open Time: 0800

NUMBER: 3

NAME: XXXXXXXXXXX NCPDP \#: XXXXXXX

DEFAULT DEA \#: AGXXXXX CMOP SWITCH: CMOP ON

AUTO-REVERSE PARAMETER: 2 STATUS: ACTIVE

SITE ADDRESS 1: 101 MAIN AVE

SITE CITY: XXXXXXXXXXX SITE STATE: XXXXXX

SITE ZIP CODE: XXXXX SITE ADDRESS NAME: 101 MAIN AVE

HOURS OF OPERATION: 24 START DAY RANGE: MON

END DAY RANGE: MON START HOUR RANGE: 0800

END HOUR RANGE: 1600~TUE NPI: 0000000006

DATE/TIME OF LAST NPI CHANGE: OCT 10, 2006@15:05:05

OUTPATIENT SITE: XXXXXXXXXX VA

OUTPATIENT SITE: XXXXXXXXX CBOC

OUTPATIENT SITE: XXXXX VA CBOC

REMITTANCE ADDRESS NAME: XXXXXXXXXX XXXXXX

REMIT ADDRESS 1: 101 XXXXXXXXXXXXXXXX

REMIT CITY: XXXXXXXXXXX REMIT STATE: XXXXXXXX

REMIT ZIP: XXXXX VA CONTACT: CONTACT,ONE

VA ALTERNATE CONTACT: CONTACT,TWO

VA LEAD PHARMACIST: PHARMACIST,ONE Monday Close Time: 1600

Tuesday Close Time: 1600 Wednesday Close Time: 1600

Thursday Close Time: 1600 Friday Close Time: 1600

BPS PHARMACIES LIST SEP 09, 2005@17:17 PAGE 3

-------------------------------------------------------------------------------

Saturday Close Time: 1600 Monday Open Time: 0800

Tuesday Open Time: 0800 Wednesday Open Time: 0800

Thursday Open Time: 0800 Friday Open Time: 0800

Saturday Open Time: 0800

Press ENTER to continue

### Turn-around time statistics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Turn-around time statistics* option shows the length of time for claims to complete, including breakouts for various steps of claims creation. The end of the report has the average time for the claims displayed.

Access the *Turn-around time statistics* option by entering TAT at the “Select Other Reports Option:” prompt on the Pharmacy Electronic Claims Reports, Other Reports option screen.

Example 8.2.4-1: Accessing the Turn-around time statistics Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXX VAMC \*

\* Other Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

CRI ECME Claims-Response Inquiry

PAY Payer Sheet Detail Report

PHAR ECME Setup - Pharmacies Report

TAT Turn-around time statistics

VER View ePharmacy Rx

OPR OPECC Productivity Report

Select Other Reports Option: TAT Turn-around time statistics

Example 8.2.4-2: Displaying the Turn-around time statistics Report

START WITH DATE: T-1// \<Enter\> (SEP 08, 2005)

GO TO DATE: T// \<Enter\> (SEP 09, 2005)

For Prescription: 1106378.00001 (Rx#: 382992)

Begin 08:19:48

Gathering information 08:19:52

Claim ID created 08:19:55

Claim Sent 08:19:56

Response stored 08:20:04

Completed at: 08:20:04

Turn-around time 16

For Prescription: 1106380.00001 (Rx#: 382994)

Begin 08:19:48

Gathering information 08:19:52

Claim ID created 08:19:55

Claim Sent 08:20:16

Response stored 08:20:18

Completed at: 08:20:18

Turn-around time 30

For Prescription: 1106379.00001 (Rx#: 382993)

Begin 08:19:48

Gathering information 08:19:52

Claim ID created 08:19:55

Claim Sent 08:20:06

Response stored 08:20:08

Completed at: 08:20:08

Turn-around time 20

For Prescription: 1106384.00001 (Rx#: 909952)

Begin 11:27:13

Gathering information 11:27:15

Claim ID created 11:27:16

Claim Sent 11:27:17

Response stored 11:27:23

Completed at: 11:27:23

Turn-around time 10

For Prescription: 1106386.00001 (Rx#: 909954)

Begin 11:27:13

Gathering information 11:27:15

Claim ID created 11:27:17

Claim Sent 11:27:37

Response stored 11:27:39

Completed at: 11:27:39

Turn-around time 26

Average Turn-around time: 13

### View ePharmacy Rx

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *View ePharmacy Rx* option allows the user to view information for one prescription, combining information from Outpatient Pharmacy, Integrated Billing and ECME.

Access the *View ePharmacy Rx* option by entering VER at the “Select Other Reports Option:” prompt on the Pharmacy Electronic Claims Reports, Other Reports option screen.

Example 8.2.5-1: Accessing the View ePharmacy Rx Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* XXXXXX VAHSRO \*

\* Other Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

CRI ECME Claims-Response Inquiry

PAY Payer Sheet Detail Report

PHAR ECME Setup - Pharmacies Report

TAT Turn-around time statistics

VER View ePharmacy Rx

OPR OPECC Productivity Report

Select Other Reports Option: VER View ePharmacy Rx

Example 8.2.5-2: Displaying the View ePharmacy Rx Report

Select Prescription: 2055346

ATENOLOL 25MG TAB

Patient Rx# Drug Name Rx Status

ECMEPATIENT,ONE 2055346 TAMOXIFEN CITRATE 10MG TA DISCONTINUED

OK to continue? Yes// YES

Rx# 2055346 has the following fills:

Fill# Fill Date Release Date

----- ---------- ------------

0 01/29/2009 01/29/2009

1 02/26/2009 02/25/2009

Select Fill Number: 1 02/26/2009 02/26/2009

Select one of the following:

M Most recent transaction for each payer

A All transactions

There are 2 ECME transactions for this Rx/fill.

1 for the primary payer, 1 for the secondary payer.

Select Most recent transaction for each payer or All transactions: M// All trans

actions

Compiling data for View Prescriptions ...

Compiling data for the ECME Claim Log ...

Compiling data for the ECME Billing Events Report ...

Compiling data for the ECME Claims-Response Inquiry (CRI) Report ...

Compiling data for View Insurance Policies ... ...................

Compiling the list of TPJI bills ...

Compiling data for TPJI Claim Information ...

Compiling data for TPJI AR Account Profile ...

Compiling data for TPJI AR Comment History ...

Compiling data for TPJI ECME Rx Response ...

Compiling data for View Registration Eligibility Status ...

Compiling data for View Registration Eligibility Verification ...

View Prescription

Rx View (Discontinued) Feb 08, 2011@13:59:27 Page: 1 of 1

ECMEPATIENT,ONE

PID: 666-87-4529 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: OCT 18,1963 (47) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

+-------------------------------------------------------------------------------

Rx \#: 2055346\$e (ECME#: 000001615253)

Orderable Item: TAMOXIFEN CITRATE TAB

CMOP Drug: TAMOXIFEN CITRATE 10MG TAB

NDC: 00378-0144-93

\*Dosage: 10MG

Verb: TAKE

Dispense Units: 1

Noun: TABLET

\*Route: ORAL (BY MOUTH)

\*Schedule: BID

Patient Instructions:

SIG: TAKE ONE TABLET BY MOUTH TWICE A DAY

Patient Status: OUTPT NON-SC

Issue Date: 01/29/09 Fill Date: 01/29/09

Last Fill Date: 02/26/09 (Mail, Transmitted)

Last Release Date: 02/25/09 Lot \#:

Expires: 01/30/10 MFG:

Days Supply: 3 QTY (TAB): 60

\# of Refills: 11 Remaining: 9

Provider: ECMEPROVIDER,ONE

Routing: Window

Copies: 1

Method of Pickup:

Clinic: Not on File

Division: CHEYENNE VAM&ROC (442)

Pharmacist: ECMEPROVIDER,ONE

Patient Counseling: NO

Remarks: New Order Created by copying Rx \# 2055345.

Finished By: ECMEPROVIDER,ONE

Entry By: ECMEPROVIDER,ONE Entry Date: 01/29/09 12:59:38

Original Fill Released: 02/25/09 Routing: Window

Refill Log:

\# Log Date Refill Date Qty Routing Lot \# Pharmacist

===============================================================================

1 02/25/09 02/25/09 60 Mail

Division: 442 Dispensed: 02/25/09 Released: 2/25/09 NDC: 00378-0144-91

2 02/25/09 02/26/09 60 Mail

Division: 442 Dispensed: 02/26/09 Released:

Partial Fills:

\# Log Date Date Qty Routing Lot \# Pharmacist

===============================================================================

There are NO Partials for this Prescription

Activity Log:

\# Date Reason Rx Ref Initiator Of Activity

===============================================================================

1 02/25/09 SUSPENSE REFILL 1 ECMEPROVIDER,ONE

Comments: RX Placed on Suspense for CMOP until 02-25-09

2 02/25/09 PROCESSED REFILL 1 ECMEPROVIDER,ONE

Comments: Transmitted to DALLAS CMOP

3 02/25/09 SUSPENSE REFILL 2 ECMEPROVIDER,ONE

Comments: RX Placed on Suspense for CMOP until 02-26-09

4 02/25/09 SUSPENSE REFILL 2 ECMEPROVIDER,ONE

Comments: 3/4 of Days Supply SUSPENSE HOLD until 2/28/09.

5 03/01/09 PROCESSED REFILL 2 ECMEPROVIDER,ONE

Comments: Transmitted to DALLAS CMOP

6 06/11/09 DISCONTINUED REFILL 2 ECMEPROVIDER,TWO

Comments: Discontinued During New Prescription Entry - Duplicate Drug

Copay Activity Log:

\# Date Reason Rx Ref Initiator Of Activity

===============================================================================

There's NO Copay activity to report

Label Log:

\# Date Rx Ref Printed By

===============================================================================

1 02/25/09 ORIGINAL ECMEPROVIDER,ONE

Comments: From RX number 2055346

ECME Log:

\# Date/Time Rx Ref Initiator Of Activity

===============================================================================

1 1/29/09@12:59:55 ORIGINAL ECMEPROVIDER,ONE

Comments: Submitted to ECME:WINDOW FILL(NDC:00378-0144-93)-E REJECTED

2 2/25/09@16:49:16 ORIGINAL ECMEPROVIDER,ONE

Comments: Submitted to ECME:REJECT WORKLIST-E PAYABLE

3 2/25/09@16:51:03 REFILL 1 ECMEPROVIDER,ONE

Comments: Submitted to ECME:CMOP TRANSMISSION(NDC:00378-0144-91)

4 3/1/09@14:00:05 REFILL 2 ECMEPROVIDER,ONE

Comments: Submitted to ECME:CMOP TRANSMISSION(NDC:00378-0144-91)

ECME REJECT Log:

\# Date/Time Rcvd Rx Ref Reject Type STATUS Date/Time Resolved

===============================================================================

1 1/29/09@12:59:54 ORIGINAL REFILL TOO SOON RESOLVED 2/25/09@16:49:04

Comments: AUTOMATICALLY CLOSED (CLAIM RE-SUBMITTED)

CMOP Event Log:

Date/Time Rx Ref TRN-Order Stat Comments

===============================================================================

02/25/09@1656 Ref 1 16346-1 DISP NDC: 00378014491

Carrier: USPS Pkg ID: PGKID999

03/01/09@1403 Ref 2 16360-1 TRAN

CMOP Lot#/Expiration Date Log:

Rx Ref Lot \# Expiration Date

===============================================================================

Ref 1 A87904 03/22/07

ECME Claim Log

PHARMACY ECME Feb 08, 2011@14:06:41 Page: 1 of 1

Claim Log information

--------------------------------------------------------------------------------

Pharmacy ECME Log

VA Rx \#: 2055346\$ Fill \#: 1 ECME \#: 1615253

Patient Name: ECMEPATIENT,ONE (4529)

Transaction Number: 1615253.00011

Last Submitted: FEB 25,2009@16:51:03

Last Submitted By: ECMEPROVIDER,ONE

Last VA Claim \#: VA2009=1164471991=000010=0001235

Transmission Information (CLAIM REQUEST)(#1236)--------------------------------

Created on: FEB 25,2009@16:51:04

VA Claim ID: VA2009=1164471991=000010=0001235

Submitted By: ECMEPROVIDER,ONE

Transaction Type: REQUEST

Date of Service: 02/25/2009

NDC: 00378-0144-91

ECME Pharmacy: CHEY9-BOTH NPI & NCPDP

Days Supply: 3

Qty: 60 Unit Cost: .928 Total Price: 68.20

Insurance Name: BLUE MOON INSURANCE

Group Name: T-GROUP1

Rx Coordination of Benefits: PRIMARY

BIN: 123456

PCN: 1123456789

NCPDP Version: D.0

Group ID: 10001

Cardholder ID:

Patient Relationship Code: CARDHOLDER

Cardholder First Name: ONE

Cardholder Last Name: OPPATIENT

Facility ID Qualifier:

Billing Request Payer Sheet: WBTESTB1

Reversal Payer Sheet: WBTESTB2

Response Information (CLAIM REQUEST)(#1213)-----------------------------------

Response Received: FEB 25,2009@16:51:10

Date of Service: 02/25/2009

Transaction Response Status: Paid

Total Amount Paid: \$58.20

Reconciliation ID:

Reject code(s):

Message:

Additional Message:

DUR Response Info:

DUR Additional Text:

ECME CRI REPORT DATA

ECME Claims-Response Inquiry Report Print Date: 02/08/11

VA CLAIM ID: VA2009=1164471991=000010=0001235

BPS TRANSACTION/BPS LOG OF TRANSACTION DATA:

ENTRY#: 1615253.00011 STATUS: 99

PHARMACY: CHEY9-BOTH NPI & NCPDP PRESCRIPTION \#: 2055346

RXI-INTERNAL (c): 1615253

PLAN NAME: BLUE MOON INSURANCE PHARMACY PLAN ID: T00010

CLAIM IEN (c): 1236 RESPONSE IEN (c): 1213

BPS CLAIMS FILE DATA:

CLAIM ID: VA2009=1164471991=000010=0001235

ELECTRONIC PAYER: WBTESTB1 TRANSMIT FLAG: YES (POINT OF SALE)

TRANSMITTED ON: FEB 25,2009@16:51:04 CREATED ON: FEB 25,2009@16:51:04

PATIENT NAME: ECMEPATIENT,ONE

GROUP INSURANCE PLAN: BLUE MOON INSURANCE

BIN NUMBER: 123456 VERSION RELEASE NUMBER: D.0

TRANSACTION CODE: B1 PROCESSOR CONTROL NUMBER: 1123456789

TRANSACTION COUNT: 1 SOFTWARE VENDER CERT ID: TATP

SERVICE PROVIDER ID: 1164471991 SERVICE PROVIDER ID QUAL: 01

GROUP ID: C110001 CARDHOLDER ID: C2

DATE OF BIRTH: C419631018 PATIENT GENDER CODE: MALE

PATIENT FIRST NAME: CAONE PATIENT LAST NAME: CBOPPATIENT

PATIENT STREET ADDRESS: CM32 OAK STREET

PATIENT CITY ADDRESS: CNBIRMINGHAM

PATIENT STATE PROV ADDRESS: COAL PATIENT ZIP POSTAL ZONE: CP35209

PATIENT PHONE NUMBER: CQ2055559874 PATIENT ID QUALIFIER: CX01

PATIENT ID: CY666874529

TRANSACTION ORDER: 1

MEDICATION NAME: TAMOXIFEN CITRATE 10MG TAB

PRESCRIPTION NUMBER: 2055346 OTHER COVERAGE CODE: C800

SUBM CLARIFICATION CODE COUNT: 1

SUBMISSION CLRFCTN CODE CNTR: 1 SUBMISSION CLARIFICATION CODE: DK02

DATE OF SERVICE: FEB 25,2009 PRESCRIPTION/SERVICE REF NO: D21615253

FILL NUMBER: D301 DAYS SUPPLY: D5003

COMPOUND CODE: D61

PRODUCT SERVICE ID: D700378014491

DISPENSE AS WRITTEN: D80 INGREDIENT COST SUBMITTED: D90000510{

PRESCRIBER ID: DB DISPENSING FEE SUBMITTED: DC00000000

DATE PRESCRIPTION WRITTEN: DE20090129

NUMBER OF REFILLS AUTHORIZED: DF11 PRESCRIPTION ORIGIN CODE: DJ1

\*SUBMISSION CLARIFICATION CODE: DK02 BASIS OF COST DETERMINATION: DN07

USUAL AND CUSTOMARY CHARGE: DQ0000510{

GROSS AMOUNT DUE: DU0000510{ PRESCRIBER LAST NAME: DROPPROVIDER

PATIENT PAID AMOUNT SUBMITTED: DX0000000{

PRODUCT SERVICE ID QUALIFIER: E103 QUANTITY DISPENSED: E70000060000

PRESCRIPTION SERVICE REFERENCE: EM1 QUANTITY PRESCRIBED: ET0000060000

PRESCRIBER ID QUALIFIER: EZ01 PRESCRIBER LOCATION CODE: 1E

PC PROVIDER LOCATION CODE: H5001 PC PROVIDER LAST NAME: 4EOPPROVIDER

PRESCRIBER PHONE NUMBER: PM0001234567

DATE OF SERVICE: 20090225

RAW DATA SENT:

12345651B111234567891011164471991 20090225TATP

AM01CX01CY666874529 C419631018C51CAONE CBOPPATIENT CM32

OAK STREET CNBIRMINGHAM COALCP35209 CQ2055559874

AM04C2C110001

AM07EM1D21615253E103D700378014491 E70000060000D301D5003D61D80DE20090129D

F11DJ1DK02ET0000060000C800

AM02

AM03EZ01DB 1E DROPPROVIDER H50014EOPPROVIDER

AM11D90000510{DC00000000DX0000000{DQ0000510{DU0000510{DN07

BPS RESPONSE FILE DATA:

BPS CLAIM: VA2009=1164471991=000010=0001235

DATE RESPONSE RECEIVED: FEB 25, 2009@16:51:10

VERSION RELEASE NUMBER: D.0 TRANSACTION CODE: B1

TRANSACTION COUNT: 1 SERVICE PROVIDER ID: 1164471991

SERVICE PROVIDER ID QUALIFIER: 01 DATE OF SERVICE: FEB 25,2009

RESPONSE STATUS: ACCEPTED

TRANSACTION ORDER: 1 TRANSACTION RESPONSE STATUS: PAID

PRESCRIPTION REFERENCE NUMBER: 1615253

RX REFERENCE NUMBER QUALIFIER: RX BILLING

HEADER RESPONSE STATUS: CLAIM PAYABLE

AUTHORIZATION NUMBER: WEBMD: PAID PATIENT PAY AMOUNT: \$ 10.00

INGREDIENT COST PAID: \$ 55.70 DISPENSING FEE PAID: \$ 12.50

TOTAL AMOUNT PAID: \$ 58.20 INCENTIVE AMOUNT PAID: \$ 1.25

BASIS OF REIMB DETERMINATION: 08 TAX EXEMPT INDICATOR: NOT TAX EXEMPT

FLAT SALES TAX PAID: \$ 1.00 PROFESSIONAL SERVICE FEE PAID: \$ 4.54

OTHER AMOUNT PAID COUNT: 1 OTHER PAYER AMOUNT RECOGNIZED: \$ 0.00

RAW DATA RECEIVED:

VA2009=1164471991=000010=000123551B11A011164471991

20090225\X1D\\X1E\\X1C\AM21\X1C\ANP\X1C\F3WEBMD:

PAID\X1E\\X1C\AM22\X1C\EM1\X1C\D21615253\X1E\\X1C\AM23\X1C\F50000100{\X1C\F6000

0557{\X1C\F70000125{\X1C\AV2\X1C\AW0000010{\X1C\FL0000012E\X1C\J10000045D\X1C\J2

1\X1C\J301\X1C\J40000033C\X1C\J50000000{\X1C\F90000683B\X1C\FM08

ECME BILLING EVENTS REPORT

PAGE 1

BILLING ECME EVENTS (DETAILED) for ALL DIVISIONS

SINGLE PRESCRIPTION – 2055346 FILL# 1

RX# FILL DATE PATIENT NAME DRUG

================================================================================

1 2055346 1 02/25/09 ECMEPATIENT,ONE TAMOXIFEN CITRATE 10MG TAB

FINISH 02/25/09 4:51p Status:ECME Billable

ELIGIBILITY: CV:No

DRUG:TAMOXIFEN CITRATE 10MG TAB

NDC:00378-0144-91, BILLED QTY:60, COST:.928, DEA:6PR

PLAN:T-GROUP1 INSURANCE: BLUE MOON INSURANCE

BIN:123456, PCN:1123456789, PAYER SHEET B1:WBTESTB1

PAYER SHEET B2:WBTESTB2, PAYER SHEET B3:WBTESTB1

DISPENSING FEE:0, BASIS OF COST DETERM:USUAL & CUSTOMARY

COST:68.20, GROSS AMT DUE:68.20, ADMIN FEE:12.50

USER:POSTMASTER

SUBMIT 02/25/09 4:51p Status:OK

ECME#:000001615253, FILL DATE:02/25/09

PAYER RESPONSE: PAYABLE

PLAN:T-GROUP1, INSURANCE: BLUE MOON INSURANCE

USER:POSTMASTER

RELEASE 02/25/09 4:56p Status:OK

ECME#:000001615253, FILL DATE:02/25/09

USER:POSTMASTER

BILLING 02/25/09 4:56p Status:Bill# K90007W created

ECME#:000001615253, FILL DATE:02/25/09,RELEASE DATE:02/25/09

DRUG:TAMOXIFEN CITRATE 10MG TAB

NDC:00378-0144-91, BILLED QTY:60, DAYS SUPPLY:3

BILLED:68.20, PAID:58.20

PLAN:T-GROUP1, INSURANCE: BLUE MOON INSURANCE

USER:POSTMASTER

List of all bills for this Rx (all fills)

BILL RX DATE INSURANCE COB PATIENT

---------------------------------------------------------------------------

1 K90007U 2055346-0 01/29/09 BLUE MOON INSURANC P ECMEPATIENT,ONE

2 K90007W 2055346-1 02/25/09 BLUE MOON INSURANC P ECMEPATIENT,ONE

Medication Profile

ISSUE LAST REF DAY

\# Rx# DRUG \[^\] QTY ST DATE FILL REM SUP

--------------------------------------------------------------------------------

REFILL TOO SOON/DUR REJECTS (Third Party) (2 orders)

1 2999999e AMOXAPINE 25MG TAB 90 A 11-30-17 11-30-17 3 90

2 2888888e AMOXICILLIN 250/CLAV K 62.5 1 A 12-01-17 12-01-17 3 90

View Patient Insurance

Patient Policy Information Feb 23, 2011@13:24:18 Page: 1 of 1

Expanded Policy Information for: ECMEPATIENT,ONE 666-20-4589

OPINSUR1 Insurance Company \*\* Plan Currently Active \*\*

Plan Information Insurance Company

Is Group Plan: YES Company: OPINSUR1

Group Name: DRUG INS Street: 32 CATASTROPHE WAY

Group Number: 111 City/State: ANYTOWN, AL 35209

BIN: Billing Ph:

PCN: Precert Ph:

Type of Plan: PRESCRIPTION

Electronic Type: COMMERCIAL

Plan Filing TF:

ePharmacy Plan ID: VA105220

ePharmacy Plan Name: MINNESOTA MEDICAID

ePharmacy Natl Status: ACTIVE

ePharmacy Local Status: ACTIVE

Utilization Review Info Effective Dates & Source

Require UR: NO Effective Date: 10/12/07

Require Amb Cert: Expiration Date:

Require Pre-Cert: NO Source of Info: INTERVIEW

Exclude Pre-Cond: NO Policy Not Billable: NO

Benefits Assignable: YES

Subscriber Information Subscriber's Employer Information

Whose Insurance: VETERAN Emp Sponsored Plan: No

Subscriber Name: ECMEPATIENT,ONE Employer:

Relationship: SELF Employment Status:

Primary ID: 543252 Retirement Date:

Coord. Benefits: PRIMARY Claims to Employer: No, Send to Insurance Company

Primary Provider: Street:

Prim Prov Phone: City/State:

Phone:

Insured Person's Information (use Subscriber Update Action)

Insured's DOB: 10/18/1963 Str 1: 1225 OAK LANE

Insured's Sex: MALE Str 2:

Insured's Branch: ARMY City: ANYTOWN

Insured's Rank: St/Zip: AL 35209

Phone: 2055555555

Insurance Company ID Numbers (use Subscriber Update Action)

Subscriber Primary ID: 543252

Plan Coverage Limitations

Coverage Effective Date Covered? Limit Comments

-------- -------------- -------- --------------

INPATIENT 08/04/2008 YES

07/11/2008 YES

06/26/2008 YES

02/26/2008 YES

01/28/2008 YES

10/12/2007 YES

06/19/2007 YES

04/13/2007 YES

01/08/2007 YES

06/17/2006 YES

OUTPATIENT 08/04/2008 YES

07/11/2008 YES

06/26/2008 YES

02/26/2008 YES

01/28/2008 YES

10/12/2007 YES

08/02/2007 YES

06/19/2007 YES

04/13/2007 YES

01/08/2007 YES

06/17/2006 YES

PHARMACY 03/17/2009 YES

08/06/2008 YES

08/04/2008 YES

07/11/2008 YES

06/26/2008 YES

DENTAL 08/04/2008 YES

07/11/2008 YES

06/26/2008 YES

02/26/2008 YES

01/28/2008 YES

10/12/2007 YES

08/02/2007 YES

06/19/2007 YES

04/13/2007 YES

01/08/2007 YES

06/17/2006 YES

MENTAL HEALTH 08/04/2008 YES

07/11/2008 YES

06/26/2008 YES

02/26/2008 YES

01/28/2008 YES

10/12/2007 YES

08/02/2007 YES

06/19/2007 YES

04/13/2007 YES

01/08/2007 YES

06/17/2006 YES

LONG TERM CARE BY DEFAULT

User Information Insurance Contact (last)

Entered By: EXAMPLE, EMPLOYEEPerson Contacted:

Entered On: 10/12/07 Method of Contact: PHONE

Last Verified By: EXAMPLE, EMPLOYEE Contact's Phone:

Last Verified On: 02/07/08 Call Ref. No.:

Last Updated By: EXAMPLE, EMPLOYEE Contact Date: APR 15, 2009

Last Updated On: 04/15/09

Comment -- Patient Policy

None

Comment -- Group Plan

Personal Riders

TPJI – Claim Information

Claim Information Feb 08, 2011@14:36:24 Page: 1 of 1

K90007We ECMEPATIENT,ONE O4529 DOB: 10/18/63 Subsc ID:

TPJI – Claim Information

Claim Information Feb 08, 2011@14:36:24 Page: 1 of 1

K90007We ECMEPATIENT,ONE O4529 DOB: 10/18/63 Subsc ID:

--------------------------------------------------------------------------------

Insurance Demographics Subscriber Demographics

Bill Payer: BLUE MOON INSURANCE Group Number: 10001

Claim Address: 321 MOON DRIVE Group Name: T-GROUP1

ANYTOWN, AL 35209 Subscriber ID:

Claim Phone: Employer: USA ARMY CONSULTANTS

Insured's Name: ECMEPATIENT,ONE

Relationship: PATIENT

Claim Information

Bill Type: OUTPATIENT Charge Type:

Time Frame: ADMIT THRU DISCHARGE Service Dates: 02/25/09 - 02/25/09

Rate Type: REIMBURSABLE INS. Orig Claim: 68.20

AR Status: ACTIVE Balance Due: 10.00

Sequence: PRIMARY

Purch Svc: NO

ECME No: 1615253

ECME Ap No: WEBMD: PAID

NPI: 1164471991

Providers: NONE

Entered: 02/25/09 by POSTMASTER

Authorized: 02/25/09 by POSTMASTER

First Printed: 02/25/09 by POSTMASTER

Related Prescription Copay Information

\<none found\>

TPJI – AR Account Profile

AR Account Profile Feb 08, 2011@14:46:24 Page: 1 of 1

K90007We ECMEPATIENT,ONE O4529 DOB: 10/18/63 Subsc ID:

AR Status: ACTIVE Orig Amt: 68.20 Balance Due: 10.00

--------------------------------------------------------------------------------

02/25/09 IB Status: PRINTED (First) 68.20 10.00

Total Collected: 58.20

TPJI – AR Comment History

Comment History Feb 08, 2011@14:47:10 Page: 1 of 1

K90007We ECMEPATIENT,ONE O4529 DOB: 10/18/63 Subsc ID:

AR Status: ACTIVE Orig Amt: 68.20 Balance Due: 10.00

No Comment Transactions Exist For This Account.

TPJI – ECME Claim Information

ECME Claim Information Feb 08, 2011@14:48:16 Page: 1 of 1

K90007We ECMEPATIENT,ONE O4529 DOB: 10/18/63 Subsc ID:

--------------------------------------------------------------------------------

ECME No: 1615253 Pharmacy NPI: 1164471991

ECME Ap No: WEBMD: PAID Provider NPI: No NPI on file

Rx No: 2055346 / 1 Fill Date: 02/25/09

Drug Name: TAMOXIFEN CITRATE 10MG TAB NDC \#: 00378-0144-91

Billed Amt: 68.20 COB: Primary

IB Status: CANCELLED (02/25/09) Reason: ECME PRESCRIPTION REVERSED

Payment Information

Expected Payment Amount: 58.20

Ingredient Cost Reim Amt: 0.00 Dispensing Fee Reim Amt: 0.00

Patient Responsibility Amounts

Deductible: 0.00 Coinsurance: 0.00 Amount of Copay: 0.00

Coverage Gap: 0.00 Processor Fee: 0.00 Exceed Benefit Max: 0.00

Health Plan-funded Assistance Amount: 0.00

Product Selection Amounts

Prod Sel Amt: 0.00 Prod Sel /Non-Pref Formulary: 0.00

Prod Sel/Brand Drug: 0.00 Prod Sel/Brand Non-Pref Formulary: 0.00

Provider Network Adj: 0.00

No COB/Other Payer Data on file in the ECME Response.

ELIGIBILITY STATUS DATA, SCREEN \<7\>

ECMEPATIENT,ONE; 666-20-4589 ACTIVE DUTY

===============================================================================

\<1\> Patient Type: ACTIVE DUTY Veteran: YES

Svc Connected: YES SC Percent: 20%

SC Award Date: OCT 12,2007 Unemployable: NO

P&T: NO

Rated Incomp.: NO

Claim Number: 43243222

Folder Loc.: ALBUQUERQUE

\<2\> Aid & Attendance: NO Housebound: NO

VA Pension: NO VA Disability: NO

Total Check Amount: NOT APPLICABLE

GI Insurance: NO Amount: UNANSWERED

\<3\> Primary Elig Code: SC LESS THAN 50%

Other Elig Code(s): NO ADDITIONAL ELIGIBILITIES IDENTIFIED

Period of Service: PERSIAN GULF WAR

\<3.1\> Combat Vet Elig.: EXPIRED End Date: OCT 11, 2009

\<4\> Service Connected Conditions as stated by applicant

---------------------------------------------------

NONE STATED

ELIGIBILITY VERIFICATION DATA

ELIGIBILITY VERIFICATION DATA, SCREEN \<11\>

ECMEPATIENT,ONE; 666-20-4589 ACTIVE DUTY

===============================================================================

\<1\> Eligibility Status: NOT VERIFIED Status Date: NOT APPLICABLE

Status Entered By: NOT APPLICABLE

Interim Response: UNANSWERED (NOT REQUIRED)

Verif. Method: NOT APPLICABLE

Verif. Source: NOT AVAILABLE

\<2\> Money Verified: NOT VERIFIED

\<3\> Service Verified: NOT VERIFIED

\<4\> Rated Disabilities: SC%: 20 EFF. DATE OF COMBINED SC%:

Orig Curr

Rated Disability Extr Eff Dt Eff Dt

NONE STATED

Enter ?? for more actions \>\>\>

VW View Rx CR CRI Report CI TPJI Claim Info ER TPJI ECME Rx

CL Claim Log IN Insurance AP TPJI Acct Pro ES Elig Status

BE Billing Events LB List of Bills CM TPJI AR Comm EV Elig Verif

MP Med Profile PR Print Report(s)

Select Action: Quit//

There are thirteen actions at the bottom of the screen. Twelve of these actions allow the user to jump to any one of the twelve sections comprising the *View ePharmacy Rx* report. The thirteenth action, PR Print Report(s), allows the user to print one or more sections of the report.

### OPECC Productivity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *OPECC Productivity Report* option allows the user to track the claims for users by transaction date, with the option of a summary view, detail view or Excel download format. If the claim has been submitted multiple times in the report date range, it will appear on the report only once with the appropriate count of transactions displayed under the header: \# of Transactions. The status displayed on the report reflects the status of the most recent transaction. A transaction is anything that results in a claim submission from the ECME User Screen or any back-billing claim submission from Claims Tracking or the PRO Process Secondary / TRICARE Rx to ECME option. An OPECC action of open / close claim is not considered a transaction for the OPECC productivity report.

Key The user must hold the BPS SUPERVISOR key to view the OPECC Productivity Report option.

Access the OPECC Productivity Report option by entering OPR at the “Select Other Reports Option:” prompt on the Pharmacy Electronic Claims Reports, Other Reports option screen.

Example 8.2.6-1: Accessing the OPECC Productivity Report Option

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*Electronic Claims Management Engine (ECME) V1.0\*

\* ALASKA VAHSRO \*

\* Other Reports \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

CRI ECME Claims-Response Inquiry

PAY Payer Sheet Detail Report

PHAR ECME Setup - Pharmacies Report

TAT Turn-around time statistics

VER View ePharmacy Rx

OPR OPECC Productivity Report

Select Other Reports Option: VER View ePharmacy Rx

Example 8.2.6-2: Prompts for the OPECC Productivity Report

Select Other Reports \<TEST ACCOUNT\> Option: OPR OPECC Productivity Report

Select one of the following:

D DIVISION

A ALL

Select Certain Pharmacy (D)ivisions or (A)LL: A// LL

Select one of the following:

V VETERAN

T TRICARE

C CHAMPVA

A ALL

Include Certain Eligibility Type or (A)ll: A// LL

Select one of the following:

U USER

A ALL

Display ECME (U)ser or (A)LL: A// LL

START WITH TRANSACTION DATE: T-1// (OCT 28, 2015)

GO TO TRANSACTION DATE: T// (OCT 29, 2015)

Select one of the following:

S Summary

D Detail

Display (S)ummary or (D)etail Format: Detail//

Enter a code from the list to indicate the sort order.

Select one of the following:

D Division

U User Name

Sort: (D/U): User Name// Division

Do you want to capture report data for an Excel document? NO//

WARNING - THIS REPORT REQUIRES THAT A DEVICE WITH 132 COLUMN WIDTH BE USED.

IT WILL NOT DISPLAY CORRECTLY USING 80 COLUMN WIDTH DEVICES

DEVICE: HOME//0;132

Example 8.2.6-3: Display of the Detailed OPECC Productivity Report

OPECC PRODUCTIVITY DETAIL REPORT Print Date: Oct 29, 2015@10:15:57 Page: 1

DIVISION(S): ALL

ELIGIBILITY: ALL

USERS: ALL

ALL PRESCRIPTIONS BY TRANSACTION DATE: From 9/29/15 through 10/29/15

=================================================================================================================================

\# TRANSACTIONS

USER STATUS DT RANGE TOTAL ELIG RX# REF/ECME# DOS TRANS DATE PAID AMT

=================================================================================================================================

DIVISION: DIVISION ONE

---------------------------------------------------------------------------------------------------------------------------------

USER,EIGHT REJECTED 1 1 CVA 100888 0/000000112004 09/29/15 09/29/15 6.62

USER,EIGHT REJECTED 1 1 CVA 100889 0/000000112005 09/29/15 09/29/15 10.00

USER,NINE PAYABLE 1 1 VET 100840G 0/000000111960 09/30/15 09/30/15 10.00

USER,NINE REVERSAL REJECTED 1 1 VET 100845 0/000000111942 08/25/15 10/01/15 10.00

USER,NINE REJECTED 1 1 CVA 100895 0/000000112012 10/01/15 10/01/15 7.43

USER,NINE REJECTED 1 1 CVA 100895A 0/000000112013 10/01/15 10/01/15 7.43

USER,NINE REJECTED 1 1 CVA 100895D 0/000000112017 10/01/15 10/01/15 7.43

USER,NINE REJECTED 1 1 CVA 100896 0/000000112018 10/01/15 10/01/15 10.00

USER,NINE REJECTED 1 1 CVA 100895F 0/000000112020 10/01/15 10/01/15 7.43

USER,NINE REVERSAL REJECTED 1 1 VET 100840H 0/000000112025 10/01/15 10/01/15 10.00

USER,EIGHT REVERSAL ACCEPTED 1 1 VET 100904 0/000000112032 10/06/15 10/06/15 10.00

USER,EIGHT REJECTED 1 1 VET 100905 0/000000112033 10/06/15 10/06/15 10.00

USER,TWO REVERSAL ACCEPTED 1 1 TRI 100872 0/000000111986 09/23/15 10/08/15 10.00

USER,NINE REVERSAL ACCEPTED 1 1 CVA 100896A 0/000000112024 10/08/15 10/08/15 10.00

USER,NINE REVERSAL ACCEPTED 1 1 TRI 100917 0/000000112046 10/14/15 10/14/15 10.00

USER,NINE REJECTED 1 1 TRI 100917A 0/000000112049 10/14/15 10/14/15 10.00

USER,NINE REJECTED 1 1 TRI 100917B 0/000000112050 10/14/15 10/14/15 10.00

USER,NINE PAYABLE 1 1 CVA 100881 0/000000111997 10/15/15 10/15/15 5.23

USER,FOUR REJECTED 1 1 TRI 100923 0/000000112055 10/15/15 10/15/15

USER,NINE REVERSAL REJECTED 1 1 TRI 100922 0/000000112054 10/15/15 10/16/15 10.00

USER,FOUR REJECTED 1 1 TRI 100927 0/000000112059 10/16/15 10/16/15

USER,FOUR REJECTED 1 1 TRI 100929 0/000000112061 10/16/15 10/16/15

USER,FOUR REJECTED 1 1 TRI 100933 0/000000112065 10/17/15 10/18/15

USER,FOUR REJECTED 1 1 TRI 100936 0/000000112068 10/18/15 10/18/15

USER,FOUR REJECTED 1 1 TRI 100832 0/000000111902 09/25/15 10/20/15

USER,THREE 1 1 TRI 100938 0/000000112070 10/28/15 10/28/15 10.00

SUBTOTALS FOR DIVISION ONE PHARMACY

REJECTED AND NOT REJECTED AND PAYABLE

USER RESOLVED TO PAYABLE (POSSIBLE BACK-BILL) TRANS IN DT RANGE AMOUNT PAID

USER,EIGHT 0 0 4 36.62

USER,THREE 0 0 1 10.00

USER,TWO 0 0 1 10.00

USER,FOUR 0 0 6 0.00

USER,NINE 2 0 14 124.95

GRAND TOTAL

REJECTED AND NOT REJECTED AND PAYABLE

USER RESOLVED TO PAYABLE (POSSIBLE BACK-BILL) TRANS IN DT RANGE AMOUNT PAID

USER,EIGHT 0 0 4 36.62

USER,THREE 0 0 1 10.00

USER,TWO 0 0 1 10.00

USER,FOUR 0 0 6 0.00

USER,NINE 2 0 14 124.95

Example 8.2.6-4: Display of the Summary OPECC Productivity Report

OPECC PRODUCTIVITY SUMMARY REPORT Print Date: Oct 29, 2015@10:32:13 Page: 1

DIVISION(S): ALL

ELIGIBILITY: ALL

USERS: ALL

ALL PRESCRIPTIONS BY TRANSACTION DATE: From 9/29/15 through 10/29/15

=================================================================================================================================

\# TRANSACTIONS

USER STATUS DT RANGE TOTAL ELIG RX# REF/ECME# DOS TRANS DATE PAID AMT

=================================================================================================================================

DIVISION: DIVISION ONE

---------------------------------------------------------------------------------------------------------------------------------

SUBTOTALS FOR DIVISION ONE PHARMACY

REJECTED AND NOT REJECTED AND PAYABLE

USER RESOLVED TO PAYABLE (POSSIBLE BACK-BILL) TRANS IN DT RANGE AMOUNT PAID

USER,ONE 0 0 4 36.62

USER,TWO 0 0 1 10.00

USER,THREE 0 0 1 10.00

USER,FOUR 0 0 6 0.00

USER,FIVE 2 0 14 124.95

GRAND TOTAL

REJECTED AND NOT REJECTED AND PAYABLE

USER RESOLVED TO PAYABLE (POSSIBLE BACK-BILL) TRANS IN DT RANGE AMOUNT PAID

USER,ONE 0 0 4 36.62

USER,TWO 0 0 1 10.00

USER,THREE 0 0 1 10.00

USER,FOUR 0 0 6 0.00

USER,FIVE 2 0 14 124.95

# BPS Nightly Background Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *BPS Nightly Background Job* is scheduled to run daily at the sites during off-hours at intervals defined by the site staff. One of the functions of this job is to identify claims to be reversed and then to automatically submit the Reversal Request to the payer.

For inpatient claims reversals, the program will go through all WINDOW fills for the date 5 days prior to the current date (T-5) and check to see if the patient is a current inpatient. If so, the reversal would be given the reason CURRENT INPATIENT to differentiate between non-released prescriptions and inpatient reversals.

The auto-reversal process for outpatient claims is dependent on whether the site sets the Auto-Reversal parameter to anything but 0 (see Auto-Reversal parameter in the Edit ECME Pharmacy Data option on the ECME Setup menu). All non-released outpatient prescriptions that were initially returned as PAYABLE and are not currently REVERSED and have a date older than the number of days set in the Auto-Reversal parameter would be reversed.

After the *BPS Nightly Background Job* identifies claims to auto-reverse and processes the Reversal Request, the system sends a bulletin to the members of the “BPS OPECC” mail group listing both reversals from the parameter setting and the inpatient claims. This mail group needs to be created at the site and should include all OPECC resources.

Example 9.1-1 Displaying the Auto-Reversal Bulletin

Subj: ECME AUTO-REVERSAL PROCESS \[#2473\] 03/05/05@01:00 29 lines

From: BPS PACKAGE In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

The ECME Nightly Process completed auto-reversing e-Pharmacy claims for prescriptions not released within the specified timeframe.

TOTAL AUTO-REVERSED CLAIMS: 3

Claims Auto-Reversed on 03/06/05:

\# RX/FILL STATUS DATE ELIG PATIENT BPS PHARM DRUG NAME

------------------------------------------------------------------------------

1 908955/1 W/NR 03/01/06 V ECMEpatient,One ANC DRUG NAME ONE

2 909225/1 W/NR 03/04/06 V ECMEpatient,Two ANC DRUG NAME TWO

3 41581/0 W/NR 03/04/06 V ECMEpatient,Three ANC DRUG NAME THREE

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term                                                                                         | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Accredited Standards Committee (ASC)                                                         | An organization that has been accredited by American National Standards Institute (ANSI) for the development of American National Standards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Administrative Code Sets                                                                     | Code sets that characterize a general business situation rather than a medical condition or service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Administrative Simplification (A/S)                                                          | Title II, Subtitle F, of HIPAA, which gives the Department Of Health And Human Services (DHHS) the authority to mandate the use of standards for the electronic exchange of health care data; to specify what medical and administrative code sets should be used within those standards; to require the use of national identification systems for health care patients, providers, payers (or plans), and employers (or sponsors); and to specify the types of measures required to protect the security and privacy of personally identifiable health care information.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| American Medical Association (AMA)                                                           | A professional association that represents the voice of the American medical profession and constitutes the partnership of physicians and their professional associations dedicated to promoting the art and science of medicine and the betterment of public health. Standards developed and approved by organizations accredited by ANSI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| American National Standards (ANS)                                                            | Standards developed and approved by organizations accredited by ANSI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| American National Standards Institute (ANSI)                                                 | An organization that accredits various standards-setting committees and monitors their compliance with the open rule-making process that they must follow to qualify for ANSI accreditation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| American Society for Testing and Materials (ASTM)                                            | A standards group that has published general guidelines for the development of standards, including those for health care identifiers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Back Door                                                                                    | System access via the roll and scroll, character and Mumps based VistA application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Blue Cross and Blue Shield Association (BCBSA)                                               | An association that represents the common interest of Blue Cross and Blue Shield health plans. The BCBSA maintains the Claim Adjustment Reason Codes code set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Business Model                                                                               | A model of a business organization or process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| CHAMPVA Patient                                                                              | A CHAMPVA patient is a patient that is receiving services due to being eligible for the CHAMPVA health benefits program. Their CHAMPVA health benefit program will be billed for the prescription.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Clean Claim                                                                                  | An insurance claim that has no defect, impropriety (including any lack of any substantial documentation) or circumstance requiring special treatment that prevents timely payment from being made.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Clearinghouse (or Health Care Clearinghouse)                                                 | For health care, an organization that translates health care data to or from a standard format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Centers for Medicare & Medicaid Services (CMS)                                               | Centers for Medicare & Medicaid Services, formerly Health Care Financing Administration (HCFA). The administration within the Department of Health and Human Services (HHS) that is responsible for the national administration of the Medicaid and Medicare programs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| CMS-1450                                                                                     | CMS’s name for the institutional uniform claim form, or UB-92.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| CMS-1500                                                                                     | CMS’s name for the professional uniform claim form. Also known as the UCF-1500.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Coordination of Benefits (COB)                                                               | A provision that is intended to avoid claims payment delays and duplication of benefits when a person is covered by two or more plans providing benefits or services for medical, dental, or other care or treatment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Code Set                                                                                     | Under HIPAA "codes used to encode data elements, tables of terms, medical concepts, diagnostic codes, or medical procedures. A code set includes the codes and descriptors of the codes." \[45 CFR 162.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Covered Entity                                                                               | Under HIPAA, a health plan, healthcare clearinghouse or health care provider who transmits information in electronic form in connection with a transaction covered by this subchapter 160.103 of 45 CFR.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Current Procedural Terminology                                                               | A procedure code set maintained and copyrighted by the AMA and that has been selected for use under HIPAA for non-institutional and non-dental professional transactions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Data Dictionary (DD)                                                                         | A document or system that characterizes the data content of a system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Data Element                                                                                 | Under HIPAA, this is "…the smallest named unit of information in a transaction." \[45 CFR 162.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Data Mapping                                                                                 | The process of matching one set of data elements or individual code values to their closest equivalents in another set of them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Data Model                                                                                   | A conceptual model of the information needed to support a business function or process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Data Set                                                                                     | Under HIPAA, this is "…a semantically meaningful unit of information exchanged between two parties to a transaction." \[45 CFR 162.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Designated Code Set                                                                          | A medical or administrative code set, which DHHS has designated for use in one or more of the HIPAA standards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Designated Data Content Committee or Designated DCC                                          | An organization, which DHHS has designated for oversight of the business data content of one or more of the HIPAA-mandated transaction standards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Designated Standard                                                                          | A standard that DHHS has designated for use under the authority provided by HIPAA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Department of Health and Human Services (DHHS) or (HHS)                                      | Department of Health and Human Services                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Electronic Commerce (EComm)                                                                  | The exchange of business information by electronic means.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Electronic Data Interchange (EDI)                                                            | The transfer of data between different companies using networks, such as the Internet. As more and more companies are connected to the Internet, EDI is becoming increasingly important as an industry standard for companies to buy, sell, and trade information. ANSI has approved a set of EDI standards known as the X12 standards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Finish                                                                                       | Term used for completing orders from Order Entry / Results Reporting V. 3.0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ‘Finish’ a Prescription                                                                      | This process within VistA Outpatient Pharmacy V. 7.0 where a pharmacy prescription order has been reviewed by either a pharmacy technician or pharmacist and is the first step in processing a prescription in Pharmacy. If performed by a pharmacist with the appropriate security key, the prescription can be ‘Verified’ as well. See ‘Verify a Prescription’ for more information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Flat File                                                                                    | This term usually refers to a file that consists of a series of fixed-length records that include some sort of record type code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Front Door                                                                                   | System access via the Delphi, Graphical User Interface (GUI) based VistA application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Graphical User Interface (GUI)                                                               | A graphical method of controlling how a user interacts with a computer to perform various tasks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| HCFA Common Procedural Coding System (HCPCS)                                                 | A medical code set that identifies health care procedures, equipment, and supplies for claim submission purposes. It is maintained by Health Care Financing Administration (HCFA), and has been selected for use in the HIPAA transactions. HCPCS Level I contain numeric CPT-4 codes, which are maintained by the AMA. HCPCS Level II contains alphanumeric codes used to identify various items and services that are not included in the CPT-4 code set. These are maintained by HCFA, BCBSA, and Health Insurance Association of America (HIAA). HCPCS Level III contains alphanumeric codes that are assigned by Medicaid State agencies to identify additional items and services not included in levels I and II. These are usually called "local codes”, and must have "W", "X", "Y", or "Z" in the first position. They are not named as HIPAA standard codes. HCPCS Procedure Modifier Codes can be used with all three levels, with the WA-ZY range used for locally assigned procedure modifiers. |
| Health Care Clearinghouse                                                                    | Under HIPAA, this is "… a public or private entity that does either of the following: (1) processes or facilitates the processing of information received from another entity in a nonstandard format or containing nonstandard data content into standard data elements or a standard transaction, or (2) receives a standard transaction from another entity and processes or facilitates the processing of \[that\] information into nonstandard format or nonstandard data content for a receiving entity." \[45 CFR 160.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Health Care Financing Administration (HCFA)                                                  | The DHHS agency responsible for Medicare and parts of Medicaid. HCFA has historically maintained the UB-92 institutional Electronic Media Claims (EMC) format specifications, the professional EMC National Standard Format (NSF) specifications, as well as specifications for various certifications and authorizations used by the Medicare and Medicaid programs. HCFA also maintains the HCPCS medical code set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Health Care Provider                                                                         | Under HIPAA, this is "…a provider of services as defined in the section 1861(u) of the \[Social Security\] Act, 42 USC 1395x(u), a provider of medical or other health services as defined in section 1861(s) of the Act, 42 USC 1395(s), and any other person or organization who furnishes, bills, or is paid for health care in the normal course of business." \[45 CFR 160.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Health Information                                                                           | Under HIPAA this is "… any information, whether oral or recorded in any form or medium that (a) is created or received by a health care provider, health plan, public health authority, employer, life insurer, school or university, or health care clearinghouse; and (b) related to the past, present or future physical or mental health or condition of an individual, the provision of health care to an individual, or the past, present or future payment for the provision of health care to an individual." \[45 CFR 160.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Health Insurance Association of America (HIAA)                                               | An industry association that represents the interests of commercial health care insurers. The HIAA participates in the maintenance of some code sets, including HCPCS Level II codes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Health Insurance Portability and Accountability Act of 1996 (HIPAA)                          | A Federal law that makes several changes that have the goal of allowing persons to qualify immediately for comparable health insurance coverage when they change their employment relationships. Title II, Subtitle F, of HIPAA gives HHS the authority to mandate the use of standards for the electronic exchange of health care data; to specify what medical and administrative code sets should be used within those standards; to require the use of national identification systems for health care patients, providers, payers (or plans), and employers (or sponsors); and to specify the types of measures required to protect the security and privacy of personally identifiable health care information. Also known as the Kennedy-Kassebaum Bill, the Kassebaum-Kennedy Bill, K2, or Public Law 104-191.                                                                                                                                                                                        |
| Health Plan                                                                                  | Under HIPAA this is "…an individual or group plan that provides, or pay the cost of, medical care.” \[45 CFR 160.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Healthcare Financial Management Association (HFMA)                                           | An organization for the improvement of the financial management of healthcare-related organizations. The HFMA sponsors some HIPAA educational seminars.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Health Level Seven (HL7)                                                                     | An ANSI-accredited group that defines standards for the cross-platform exchange of information within a health care organization. HL7 is responsible for specifying the Level Seven Open System Interconnection (OSI) standards for the health industry. Some HL7 standards will be encapsulated in the X12 standards used for transmitting claim attachments.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| HIPAA Data Dictionary or HIPAA DD                                                            | A data dictionary that defines and cross-references the contents of all X12 transactions included in the HIPAA mandate. It is maintained by X12N/TG3.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Implementation Guide (IG)                                                                    | A document explaining the proper use of a standard for a specific business purpose. The X12N HIPAA IGs are the primary reference documents used by those implementing the associated transactions and are incorporated into the HIPAA regulations by reference.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Implementation Specification                                                                 | Under HIPAA, this is "… the specific instructions for implementing a standard \[45 CFR 160.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Information Model                                                                            | A conceptual model of the information needed to support a business function or process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| International Classification of Diseases (ICD)                                               | A medical code set maintained by the World Health Organization (WHO). The primary purpose of this code set is to classify causes of death. A United States (US) extension of this coding system, maintained by the National Center for Health Statistics (NCHS) within the Centers for Disease Control (CDC), is used to identify morbidity factors, or diagnoses. The ICD-9-CM (Revision 9 Clinical Modification) codes have been selected for use in the HIPAA transactions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| International Standards Organization (ISO) or International Organization for Standardization | An organization that coordinates the development and adoption of numerous international standards.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Joint Commission on Accreditation of Healthcare Organizations (JCAHO)                        | In the future, the JCAHO may play a role in certifying these organizations compliance with the HIPAA A/S requirements.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| J-Codes                                                                                      | Previously HCPCS Level II has contained a set of codes with a high-order value of "J" to identify some drugs and some other items. The final HIPAA transactions and code set rule states that any J-codes identifying drugs will be dropped from the HCPCS and NDC codes will be used to identify all drug products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Maintain or Maintenance                                                                      | Under HIPAA, this is "…activities necessary to support the use of a standard adopted by the Secretary, including technical corrections to an implementation specification, and enhancements or expansion of a code set. This term excludes the activities related to the adoption of a new standard or implementation specification, or modification to an adopted standard or implementation specification." \[45 CFR 162.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Maximum Defined Data Set                                                                     | Under HIPAA, this is "… all of the required data elements for a particular standard based on a specific implementation specification." \[45 CFR 162.103\]. A framework under HIPAA whereby an entity creating a transaction is free to include whatever data any receiver might want or need. The recipient of a maximum data set is free to ignore any portion of the data not needed to conduct their part of the associated business transaction, unless the nonessential data is needed for coordination of benefits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Medical Code Sets                                                                            | Codes that characterize a medical condition or treatment. The code sets are usually maintained by professional societies and public health organizations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Memorandum of Understanding (MOU)                                                            | A document providing a general description of the kinds of responsibilities that are to be assumed by two or more parties in their pursuit of some goal(s). More specific information may be provided in an associated Statement of Work (SOW).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Modify or Modification                                                                       | Under HIPAA, refers to "a change adopted by the Secretary, through regulation, to a standard or an implementation specification." \[45 CFR 160.102\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| National Center for Health Statistics (NCHS)                                                 | An administration of HHS and CDC that oversees ICD coding.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| National Council for Prescription Drug Programs (NCPDP)                                      | An ANSI-accredited group that maintains several standard formats for use by the retail pharmacy industry, some of which are included in the HIPAA mandates.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| National Drug Code (NDC)                                                                     | A medical code set that has been selected for use in the HIPAA transactions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| National Employer ID                                                                         | A system for uniquely identifying all sponsors of health care benefits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| National Patient ID                                                                          | A system for uniquely identifying all recipients of health care services.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| National Payer ID                                                                            | A system for uniquely identifying all organizations that pays for health care services. Also known as Health Plan ID or Plan ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| National Provider File (NPF)                                                                 | The database envisioned for use in maintaining a national provider registry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| National Provider ID                                                                         | A system for uniquely identifying all providers of health care services, supplies, and equipment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| National Provider Registry                                                                   | The organization envisioned for assigning the National Provider IDs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| National Provider System (NPS)                                                               | The administrative system envisioned for supporting a national provider registry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| National Standard Format (NSF)                                                               | Generically, this applies to any national standard format, but it is often used in a more limited way to designate the Professional EMC NSF, a 320-byte flat file record format used to submit professional claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| National Uniform Billing Committee (NUBC)                                                    | The committee established by the American Hospital Association (AHA) to develop a single billing form and standard data set that could be used nationwide by institutional providers and payers for handling health care claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| NCPDP Batch Standard                                                                         | An NCPDP standard designed for use by low-volume dispensers of pharmaceuticals, such as nursing homes. Version 1.0 of this standard has been mandated under HIPAA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| NCPDP Telecommunication Standards                                                            | An NCPDP standard designed for use by high-volume dispensers of pharmaceuticals, such as retail pharmacies. Version D0 is the transaction standard under HIPAA.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Non-Formulary Drugs                                                                          | The medications that are defined as commercially available drug products not included in the VA National Formulary.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Notice of Intent (NOI)                                                                       | A document that describes a subject area for which the Federal Government is considering developing regulations. It may describe what the government considers to be the relevant considerations and invite comments from interested parties. These comments can then be used in developing a Notice of Proposed Rulemaking (NPRM) or a final regulation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Notice of Proposed Rulemaking (NPRM)                                                         | A document that describes and explains regulations that the Federal Government proposes to adopt at some future date, and invites interested parties to submit comments related to them. These comments can then be used in developing the final rules.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Office of Management & Budget (OMB)                                                          | A Federal Government agency that has a major role in reviewing proposed Federal regulations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Open System Interconnection (OSI)                                                            | A multi-layer ISO data communications standard. Level Seven of this standard is industry-specific, and HL7 is responsible for specifying the level seven OSI standards for the health industry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Outpatient Pharmacy Electronic Claims Coordinator (OPECC)                                    | This is a designated individual at each site who will be responsible for monitoring NCPDP claims using the ECME module. The OPECC will resolve claim rejection issues with the appropriate parties, make data corrections, and resubmit claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Orderable Item                                                                               | An Orderable Item name and dosage form that has no strength attached to it (e.g., Acetaminophen). The name with a strength attached is the Dispense Drug name (e.g., Acetaminophen 325mg).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Payer                                                                                        | In health care, an entity that assumes the risk of paying for medical treatments. This can be an uninsured patient, a self-insured employer, or a health care plan or Health Maintenance Organization (HMO).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PAYERID                                                                                      | HCFA’s term for their National Payer ID initiative.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PBM                                                                                          | A Pharmacy Benefit Manager (PBM) is a third party administrator of [prescription drug](http://en.wikipedia.org/wiki/Prescription_drug) programs. They are primarily responsible for processing and paying prescription drug claims.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Placeholders                                                                                 | Physical and / or logical data elements that are referenced and placed within a data structure that have a data definition but may or may not currently exist within the system. The value of these data elements is not currently maintained by the software but are established for future iterations of system development related to Billing Aware.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Potentially Billable Event                                                                   | A service that has all required data elements associated with it. These data elements are collected in the VistA Clinical Application.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Professional Component                                                                       | Charges for physician services. Examples include physician who reads the Electrocardiogram (EKG) and an Emergency Room physician who provides treatment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Provider Taxonomy Codes                                                                      | A code set for identifying the provider type and area of specialization for all health care providers. A given provider can have several Provider Taxonomy Codes. The BCBSA maintains this code set.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Secretary                                                                                    | Under HIPAA, this refers to the Secretary of the US Department of Health and Human Services or their designated representatives. \[45 CFR 160.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Segment                                                                                      | Under HIPAA, this is "…a group of related data elements in a transaction.” \[45 CFR 162.103\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Service                                                                                      | Medical care and items such as medical diagnosis and treatment, drugs and biologicals, supplies, appliances, and equipment, medical social services, and use of hospital Regional Primary Care Hospital (RPCH) or Skilled Nursing Facility (SNF) facilities.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Standard                                                                                     | Under HIPAA, this is "… a prescribed set of rules, conditions, or requirements describing the following information for products, systems, services, or practices (1) Classification of components, (2) Specification of Materials, performance, or operations, (3) Delineation of procedures. \[45 CFR 160.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Standard Setting Organization (SSO)                                                          | Under HIPAA, this is "…an organization accredited by ANSI that develops and maintains standards for information transactions or data elements, or any other standard that is necessary for, or will facilitate the implementation of this part." \[45 CFR 160.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Standard Transaction                                                                         | Under HIPAA, this is "… a transaction that complies with the applicable standard adopted under this part." \[45 CFR 162.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Statement of Work (SOW)                                                                      | A document describing the specific tasks and methodologies that will be followed to satisfy the requirements of an associated contract or MOU.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Third Party Administrator (TPA)                                                              | An entity that processes health care claims and performs related business functions for a health plan.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Third (3rd) Party Claims Transaction                                                         | Health care insurance claims submitted to an entity for reimbursement of health care bills. Under HIPAA, this is "…the exchange of information between two parties to carry out financial or administrative activities related to health care." \[45 CFR 160.103\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| TRICARE Patient                                                                              | A TRICARE patient is a patient that is receiving services due to being covered by TRICARE. Their TRICARE insurance will be billed for the prescription.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| UB-92                                                                                        | A uniform institutional claim form developed by the National Uniform Billing Committee (NUBC) that has been in use since 1993.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Unstructured Data                                                                            | This term usually refers to data that is represented as free-form text, as an image, etc., where it is not practical to predict exactly what data will appear where.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ‘Verify’ a Prescription                                                                      | After a prescription order has been ‘Finished’ the prescription must be ‘Verified’ by an authorized VistA user, through the administration of the system security key SOP. This is a critical step in the process of generating an electronic claim.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Veterans Health Information Systems and Technology Architecture (VistA)                      | Acronym for Veterans Health Information Systems and Technology Architecture, the new name for Decentralized Hospital Computer Program (DHCP).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Workgroup for Electronic Data Interchange (WEDI)                                             | A health care industry group that lobbied for HIPAA A/S, and that has a formal consultative role under the HIPAA legislation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
<span id="_Toc72333931" class="anchor"></span>Table 7: Acronyms and Abbreviations

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table provides definitions and explanations for terms and acronyms relevant to the content presented within this document. For additional terms and acronyms, include references to other VA acronym and glossary repositories (e.g., VA Acronym Lookup and OIT Master Glossary).

| Acronym or Term | Definition / Explanation                                                                  |
|-----------------|-------------------------------------------------------------------------------------------|
| AITC            | Austin Information Technology Center                                                      |
| ADPAC           | Automated Data Processing Application Coordinator                                         |
| AMA             | American Medical Association                                                              |
| ANS             | American National Standards                                                               |
| ANSI            | American National Standards Institute                                                     |
| A/S             | Administrative Simplification                                                             |
| ASC             | Accredited Standards Committee                                                            |
| ASTM            | American Society for Testing and Materials                                                |
| BCBSA           | Blue Cross and Blue Shield Association                                                    |
| CDES            | ECME User Screen                                                                          |
| CMOP            | Consolidated Mail Outpatient Pharmacy                                                     |
| CMS             | Centers for Medicare & Medicaid                                                           |
| COB             | Coordination of Benefits                                                                  |
| DD              | Data Dictionary                                                                           |
| DEA             | Drug Enforcement Administration                                                           |
| DHHS            | Department of Health and Human Services                                                   |
| DUR             | Drug Utilization Review                                                                   |
| ECME            | Electronic Claims Management Engine                                                       |
| EComm           | Electronic Commerce                                                                       |
| EDI             | Electronic Data Interchange                                                               |
| FILEMAN         | VistA FileMan                                                                             |
| GUI             | Graphical User Interface                                                                  |
| HCFA            | Health Care Financing Administration                                                      |
| HCPCS           | HCFA Common Procedural Coding System                                                      |
| HFMA            | Healthcare Financial Management Association                                               |
| HHS             | Department of Health and Human Services                                                   |
| HIAA            | Health Insurance Association of America                                                   |
| HIPAA           | Health Insurance Portability and Accountability Act                                       |
| HL7             | Health Level Seven                                                                        |
| IB              | Integrated Billing                                                                        |
| ICD             | International Classification of Disease                                                   |
| ICD-9-CM        | International Classification of Disease, 9<sup>th</sup> revision, Clinical Modification   |
| ICD-9-PCS       | International Classification of Disease, 9<sup>th</sup> revision, Procedure Coding System |
| IG              | Implementation Guide                                                                      |
| IRMS            | Information Resources Management Service                                                  |
| ISO             | International Standards Organization                                                      |
| JCAHO           | Joint Commission on Accreditation of Healthcare Organizations                             |
| MOU             | Memorandum of Understanding                                                               |
| NCHS            | National Center for Health Statistics                                                     |
| NCPDP           | National Council for Prescription Drug Programs                                           |
| NDC             | National Drug Code                                                                        |
| NDF             | National Drug File                                                                        |
| NOI             | Notice of Intent                                                                          |
| NPF             | National Provider File                                                                    |
| NPI             | National Provider Identifier                                                              |
| NPRM            | Notice of Proposed Rulemaking                                                             |
| NPS             | National Provider System                                                                  |
| NSF             | National Standard Format                                                                  |
| NUBC            | National Uniform Billing Committee                                                        |
| OMB             | Office of Management and Budget                                                           |
| OPECC           | Outpatient Pharmacy Electronic Claims Coordinator                                         |
| OSI             | Open System Interconnection                                                               |
| OTC             | Over the Counter                                                                          |
| POS             | Point of Sale                                                                             |
| SOW             | Statement of Work                                                                         |
| SSO             | Standard Setting Organization                                                             |
| TPA             | Third Party Administration                                                                |
| VA              | Department of Veterans Affairs                                                            |
| VAMC            | Department of Veterans Affairs Medical Center                                             |
| VHA             | Veterans Health Administration                                                            |
| VistA           | Veterans Health Information Systems and Technology Architecture                           |
| WEDI            | Workgroup for Electronic Data Interchange                                                 |