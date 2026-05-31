---
title: FB*3.5*154 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: FB
app_name: Fee Basis
section: FIN
app_status: active
pkg_ns: FB
patch_ver: 3.5
patch_id: FB*3.5*154
group_key: FB:FB:3.5
file_numbers:
- '161'
- '162'
- '162.2'
- '162.4'
- '162.7'
security_keys:
- FBAA LEVEL 2
- INSTEAD OF
- LEVEL 1 AUTH
- LEVEL 1 PMT
menu_options: 0
description: The purpose of this Release Notes document, is to familiarize users with the important features and security controls exported with Fee Basis Patch FB\3.5\154. FB\3.5\154 is one of the Fee Basis patches for the VistA Fee Separation of Duties project. Patches FB\3.5\151, FB\3.5\165, and FB\3.5\172 ar
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 4559
section_count: 27
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: October 2016
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/fee3_5_p154_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/fee3_5_p154_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=40
audit_applied: '2026-05-31'
master_source: FB*3.5*154 Release Notes
master_pub_date: October 2016
consolidated_from: 11 versions
prior_versions:
- FB*3.5*108 Release Notes
- FB*3.5*123 Release Notes
- FB*3.5*124 Release Notes
- FB*3.5*131 Release Notes
- FB*3.5*132 Release Notes
- FB*3.5*135 Release Notes
- FB*3.5*139 Release Notes
- FB*3.5*146 Release Notes
- FB*3.5*158 Release Notes
- FB*3.5*163 Release Notes
consolidated_title: release notes
---

![](fb-3-5-154-release-notes/001.png)

October 2016

Office of Information and Technology (OI&T)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Table of Tables](#table-of-tables)
- [Acknowledgments](#acknowledgments)
  - [Thank You to our Test Sites](#thank-you-to-our-test-sites)
- [# Introduction](#introduction)
  - [Purpose](#purpose)
  - [Software Overview](#software-overview)
  - [Software Dependencies](#software-dependencies)
  - [Pre/Post Installation Overview](#prepost-installation-overview)
    - [Pre-Installation Instructions](#pre-installation-instructions)
    - [Post-Installation Instructions](#post-installation-instructions)
  - [Coordination](#coordination)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [VistA Fee Separation of Duties Security Keys, Patch FB\3.5\154 Release Notes](#vista-fee-separation-of-duties-security-keys-patch-fb35154-release-notes)
  - [Four Security Keys Enhance Separation of Duties Controls](#four-security-keys-enhance-separation-of-duties-controls)
    - [New Security Key: FBAA LEVEL 1 AUTH](#new-security-key-fbaa-level-1-auth)
    - [New Security Key: FBAA LEVEL 1 PMT](#new-security-key-fbaa-level-1-pmt)
    - [New Security Key: FBAA LEVEL 2](#new-security-key-fbaa-level-2)
    - [Modified Existing Security Key: FBAASUPERVISOR](#modified-existing-security-key-fbaasupervisor)
  - [New and Revised Locks on Menu Options](#new-and-revised-locks-on-menu-options)
  - [Existing Menu Options Attached to Other Fee Basis Menus](#existing-menu-options-attached-to-other-fee-basis-menus)
    - [Delete reject flag \[FBAA VOUCHER DELETE REJECT\]](#delete-reject-flag-fbaa-voucher-delete-reject)
    - [Finalize a Batch \[FBAA FINALIZE BATCH\]](#finalize-a-batch-fbaa-finalize-batch)
    - [List Batches Pending Release \[FBAA LIST CLOSED BATCHES\]](#list-batches-pending-release-fbaa-list-closed-batches)
  - [Revised Locks to Prevent Selection of Payment or Batch Entered by Another User](#revised-locks-to-prevent-selection-of-payment-or-batch-entered-by-another-user)
  - [Revised Locks During Selection Of Civil Hospital Notifications](#revised-locks-during-selection-of-civil-hospital-notifications)
  - [Removed Lock on Entry of Amount Paid that Exceeds the Amount Claimed](#removed-lock-on-entry-of-amount-paid-that-exceeds-the-amount-claimed)
  - [Lock to Update of CNH Contract or Rate Data](#lock-to-update-of-cnh-contract-or-rate-data)
  - [Lock to Run Interactive FPPS Transmit Data](#lock-to-run-interactive-fpps-transmit-data)
  - [List of Pending 7078s Modified to Consider Different Security Key](#list-of-pending-7078s-modified-to-consider-different-security-key)
  - [New User Access Report](#new-user-access-report)
  - [Disable Site Parameter EDIT AUTH. DURING PAYMENT](#disable-site-parameter-edit-auth-during-payment)
  - [Prevent Entry of Payment or Pricing if User Entered Authorization](#prevent-entry-of-payment-or-pricing-if-user-entered-authorization)
  - [Nursing Home Daily Rate Cannot be Entered During Payment](#nursing-home-daily-rate-cannot-be-entered-during-payment)
  - [New and Modified Reports Display Users that Entered or Edited Records](#new-and-modified-reports-display-users-that-entered-or-edited-records)
    - [Existing Report: Clerk Look-Up for an Authorization \[FBAA CLERK LOOK-UP\]](#existing-report-clerk-look-up-for-an-authorization-fbaa-clerk-look-up)
    - [New Report: Clerk Lookup for 7078 Authorization \[FBCH CLERK LOOKUP\]](#new-report-clerk-lookup-for-7078-authorization-fbch-clerk-lookup)
    - [New Report: Clerk Lookup for Notification/Request \[FBCH REQUEST CLERK LOOKUP\]](#new-report-clerk-lookup-for-notificationrequest-fbch-request-clerk-lookup)
    - [New Report: Clerk Lookup for Unauthorized Claim \[FBUC CLERK LOOKUP\]](#new-report-clerk-lookup-for-unauthorized-claim-fbuc-clerk-lookup)
- [New Service Requests (NSRs)](#new-service-requests-nsrs)
  - [NSR \#20090309: EMERGENCY PATCH VISTA FEE - SEPARATION OF DUTIES - ASSIGNMENT OF KEYS](#nsr-20090309-emergency-patch-vista-fee-separation-of-duties-assignment-of-keys)
- [REMEDY Tickets and Overview](#remedy-tickets-and-overview)
  - [REMEDY Ticket \#833468 Resolution](#remedy-ticket-833468-resolution)
  - [REMEDY Ticket \#985307 Resolution](#remedy-ticket-985307-resolution)
- [Documentation Retrieval Instructions](#documentation-retrieval-instructions)
  - [Office of Information and Technology (OI&T) Document Retrieval Instructions](#office-of-information-and-technology-oit-document-retrieval-instructions)
  - [VA Software Document Library (VDL)](#va-software-document-library-vdl)
> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.
<table style="width:100%;">
<caption><p><span id="_Toc462748878" class="anchor"></span>Table . Revision History</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 50%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Document Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Oct 2016</td>
<td>1</td>
<td><p>VistA Fee Separation of Duties, Patch FB*3.5*154:</p>
<ul>
<li><blockquote>
<p>Three new security keys are implemented.</p>
</blockquote></li>
<li><blockquote>
<p>Locks on existing functionality and menu options are revised and software is modified to enforce separation of duties.</p>
</blockquote></li>
<li><blockquote>
<p>An existing problem with the identification of the associated authorization for outpatient payments and inpatient ancillary payments is resolved.</p>
</blockquote></li>
<li><blockquote>
<p>The software is modified to prevent an undefined error when a prescription is deleted.</p>
</blockquote></li>
<li><blockquote>
<p>The software is modified to prevent an undefined error when rejected payments are re-initiated.</p>
</blockquote></li>
</ul></td>
<td>VistA Fee Separation of Duties Project Team</td>
</tr>
</tbody>
</table>
<span id="_Toc462748878" class="anchor"></span>Table . Revision History
Table of Contents

# Table of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Acknowledgments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is dedicated to the memory of REDACTED. He was the VHA National Fee Program Manager from 2005-2009. REDACTED always went the extra mile for Veterans and was a major force in developing and managing the Fee programs that serve our Veterans and their families.

The VistA Fee Separation of Duties team gratefully acknowledges the following Department of Veterans Affairs (VA) offices and services for their invaluable contributions and tireless dedication to excellence in contributing subject matter expertise to the development, testing, training, and the coordination of deployment for this software. Listed as follows, they are:

- VHA Community Care Operations Program Office
- VHA Office of Community Care
- VHA Office of Community Care, Revenue Operations
- VHA Office of Informatics & Analytics, Health Informatics
- VHA Office of Informatics & Analytics, Strategic Investment Management
- VHA Office of Quality, Safety and Value, Office of Compliance & Business Integrity
- VA Office of Information & Technology (OI&T) Architecture, Strategy, & Design
- VA OI&T Office of Information Security
- VA OI&T Service Delivery & Engineering
- VA OI&T/Enterprise Program Management Office Application Management/Software Testing and 508
- VA OI&T/Enterprise Program Management Office Intake and Analysis of Alternatives
- VA OI&T/Enterprise Program Management Office, Health Product Support

## Thank You to our Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Fee Separation of Duties team also wants to convey sincere thanks our test sites:

- REDACTED

# # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Release Notes document, is to familiarize users with the important features and security controls exported with Fee Basis Patch FB\*3.5\*154. FB\*3.5\*154 is one of the Fee Basis patches for the VistA Fee Separation of Duties project. Patches FB\*3.5\*151, FB\*3.5\*165, and FB\*3.5\*172 are other Fee Basis patches generated by the project.

## Software Overview 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*154 is one of the Fee Basis patches for the VistA Fee Separation of Duties project. Patches FB\*3.5\*151, FB\*3.5\*165, and FB\*3.5\*172 are other Fee Basis patches generated by the project.

Patch FB\*3.5\*154 revises the locks on existing functionality and menu options to enhance the separation of duty controls. This patch also modifies the software to enforce separation of duty business rules.

This patch resolves an existing problem with the identification of the associated authorization for outpatient payments and inpatient ancillary payments.

This patch modifies the software to prevent an undefined error when a prescription is deleted.

This patch modifies the software to prevent an undefined error when rejected payments are re-initiated.

## Software Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches *<u>must</u>* be installed *<u>prior</u>* to Patch FB\*3.5\*154:

- FB\*3.5\*7
- FB\*3.5\*17
- FB\*3.5\*49
- FB\*3.5\*59
- FB\*3.5\*69
- FB\*3.5\*91
- FB\*3.5\*123
- FB\*3.5\*127
- FB\*3.5\*153
- FB\*3.5\*157

The following patch *<u>must</u>* be installed *<u>immediately after</u>* Patch FB\*3.5\*154:

- DSIF\*3.2\*38

|                                                                                                                    |                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](fb-3-5-154-release-notes/002.png) | ALERT: If your site is using the Fee Basis Claims System (FBCS), you *<u>must</u>* install Patch DSIF\*3.2\*38 *<u>immediately after</u>* installing Patch FB\*3.5\*154 to avoid application/processing errors. If your site is not using FBCS, there is no need to install the FBCS patch. |

<span id="_Ref418201954" class="anchor"></span>Table . Tier Support Contact Information

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                    |                                                                                                                                                                  |
|--------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](fb-3-5-154-release-notes/003.png) | ALERT: Before installing the patch, the FBAA LEVEL 1 AUTH, FBAA LEVEL 1 PMT, and FBAA LEVEL 2 security keys *<u>must</u>* be allocated to appropriate users. |

<span id="_Ref418191596" class="anchor"></span>Table . New and Revised Locks on Existing Menu Options

### Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*172 previously exported the FBAA LEVEL 1 AUTH, FBAA LEVEL 1 PMT, and FBAA LEVEL 2 security keys. These keys *<u>must</u>* be allocated to appropriate users prior to the patch FB\*3.5\*154 installation to minimize work disruption.

Patch FB\*3.5\*154 modifies the software to use these new security keys.

The FBAASUPERVISOR security key *<u>must</u>* be de-allocated from user accounts that no longer require that key once patch FB\*3.5\*154 is installed. Before installing the patch, sites may want to make a list of user accounts that no longer need the FBAASUPERVISOR security key once the patch is installed.

The following five globals may increase in size during the install of the patch. Global size increases at four test sites varied greatly. The difference is believed to be due to the storage efficiency of the global. Globals that have been compressed are expected to experience a higher increase in size when the patch is installed.

> Global Minimum % Maximum % Average %

> Increase Increase Increase

> ------ --------- --------- ---------

> FB583 0 40.00 17.50

> FB7078 0 20.81 9.16

> FBAA 0 13.83 5.84

> FBAAA 0.04 12.30 9.43

> FBAAC 0.01 6.78 3.76

*For more information on the new and revised security keys exported with Patch FB\*3.5\*154, see "Section 2.1. Four Security Keys Enhance Separation of Duties Controls."*

### Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch contains a post install routine that automatically populates new fields for existing records.

The post install routine creates entries in the new USER AUDIT multiple of the following files based on existing data:

- FEE BASIS PATIENT (#161)
- FEE NOTIFICATION/REQUEST (#162.2)
- VA FORM 10-7078 (#162.4)
- FEE BASIS UNAUTHORIZED CLAIM (#162.7)

The post install populates the new AUTHORIZATION POINTER field in the SERVICE PROVIDED multiple of the FEE BASIS PAYMENT file (#162) based on existing data. The post install writes information to the ^XTMP global concerning the population of the AUTHORIZATION POINTER field. The information in ^XTMP is retained for 120 days after the install. After the patch has been installed routine FBXIP154 can optionally be deleted. However, sites may want to retain the routine until the ^XTMP global is purged since it contains a label that can be called from programmer mode to display relevant information from the ^XTMP global.

After the patch is installed the FBAASUPERVISOR security key must be de-allocated from user accounts that no longer require that key.

## Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site is using the Fee Basis Claims System (FBCS), you *<u>must</u>* install Patch DSIF\*3.2\*38 *<u>immediately after</u>* installing Patch FB\*3.5\*154 to avoid application/processing errors. If your site is not using FBCS, there is no need to install the FBCS patch.

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The three tiers of support documented herein are intended to restore normal service operation as quickly as possible and minimize the adverse impact on business operations, ensuring that the best possible levels of service quality and availability are maintained.

Table 2 lists organizational contacts needed by site users for troubleshooting purposes. Support contacts are listed by name of service responsible to fix the problem, description of the incident escalation, associated tier level, and contact information (email and phone number).

| Name                                  | Role                   | Org | Contact Info |
|-------------------------------------------|----------------------------|---------|------------------|
| OI&T National Service Desk                | Tier 1 Support             | OI&T    | REDACTED         |
| Health Product Support                    | Tier 2 Support             | OI&T    | REDACTED         |
| OI&T System Admin/Field Operation Support | Tier 2 & 3 support         | OI&T    | REDACTED         |
| VistA Patch Maintenance                   | Tier 3 Application Support | OI&T    | REDACTED         |

Table used for formatting purposes, only.Tier Support Contact Information

# VistA Fee Separation of Duties Security Keys, Patch FB\*3.5\*154 Release Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Four Security Keys Enhance Separation of Duties Controls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds three new security keys, if they don't already exist, and modifies the description of the existing FBAASUPERVISOR security key. The new keys give sites more control of user's access to the package functions. Additionally, this patch modifies the software to lock many functions with the FBAA LEVEL 2 key instead of the FBAASUPERVISOR key. This is expected to reduce the number of individuals who need to hold the FBAASUPERVISOR key. Lead clerks and supervisors may be assigned more than one of these keys. The four keys exported by the patch are listed below.

### New Security Key: FBAA LEVEL 1 AUTH

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Permits the holder to enter and edit 7079 authorizations, 7078 authorizations, civil hospital notifications, nursing home movements, and unauthorized claims.

### New Security Key: FBAA LEVEL 1 PMT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Permits the holder to enter and edit invoices and payments.

### New Security Key: FBAA LEVEL 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Permits the holder to certify a batch for payment, queue data for transmission to Central FEE, void payments, and update contract and rate data for nursing home vendors. The holder of this key can also bypass some user and status restrictions during selection of a payment or batch. This key is normally assigned to a lead clerk or supervisor.

### Modified Existing Security Key: FBAASUPERVISOR 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to Fee Basis menus and functionality associated with this security key has been modified. This key *now* permits the holder to edit site parameters, maintain the VA fee schedule, edit the contract file, reprocess an overdue batch, resend a completed batch, re-transmit MRAs, and purge MRAs. This key is normally assigned to a supervisor.

## New and Revised Locks on Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Menu options can be locked by a security key. A locked option can *only* be accessed by users who hold the applicable security key. Patch FB\*3.5\*154 modifies locks on the menu options. Menu options used to modify authorizations are generally locked by the new FBAA LEVEL 1 AUTH security key. Menu options used to process payments are generally locked by the new FBAA LEVEL 1 PMT security key. Menu options normally restricted to a lead clerk or supervisor are locked by the new FBAA LEVEL 2 security key. Menu options normally restricted to a supervisor are locked by the FBAASUPERVISOR security key.

Table 3 lists existing menus and associated options, which have new or revised locks with the installation of Patch FB\*3.5\*154. Legend as follows:

1.  The first column lists the menu and associated option affected.
2.  The second column lists the new or revised security key for the associated option.
3.  The third column lists the old security key (if any), which was in place for that option prior to the installation of the Patch FB\*3.5\*154.

| Civil Hospital Main Menu                                   | New Lock      | Old Lock              |
|----------------------------------------------------------------|-------------------|---------------------------|
| Queue Data for Transmission                                    | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Notification/Request Menu                                  | New Lock      | Old Lock              |
| Legal Entitlement                                              | FBAA LEVEL 1 AUTH | None                      |
| Medical Entitlement                                            | FBAA LEVEL 1 AUTH | None                      |
| Delete Notification/Request                                    | FBAA LEVEL 1 AUTH | None                      |
| Reconsider a Denied Request                                    | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Disposition Menu                                           | New Lock      | Old Lock              |
| Complete 7078/Authorization                                    | FBAA LEVEL 1 AUTH | None                      |
| Edit Completed 7078                                            | FBAA LEVEL 1 AUTH | None                      |
| Cancel 7078 Entered in Error                                   | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Print List of Cancelled 7078                                   | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Set-up a 7078                                                  | FBAA LEVEL 1 AUTH | None                      |
| Payment Process Menu                                       | New Lock      | Old Lock              |
| Ancillary Contract Hosp/CNH Payment                            | FBAA LEVEL 1 PMT  | None                      |
| Complete a Payment                                             | FBAA LEVEL 1 PMT  | None                      |
| Delete Inpatient Invoice                                       | FBAA LEVEL 1 PMT  | None                      |
| Edit Ancillary Payment                                         | FBAA LEVEL 1 PMT  | None                      |
| Enter Invoice/Payment                                          | FBAA LEVEL 1 PMT  | None                      |
| Invoice Edit                                                   | FBAA LEVEL 1 PMT  | None                      |
| Multiple Ancillary Payments                                    | FBAA LEVEL 1 PMT  | None                      |
| Patient Reimbursement for Ancillary Services                   | FBAA LEVEL 1 PMT  | None                      |
| Reimbursement for Inpatient Hospital Invoice                   | FBAA LEVEL 1 PMT  | None                      |
| Batch Main Menu – CH                                       | New Lock      | Old Lock              |
| Open a Batch                                                   | FBAA LEVEL 1 PMT  | None                      |
| Edit Batch data                                                | FBAA LEVEL 1 PMT  | None                      |
| Close-out Batch                                                | FBAA LEVEL 1 PMT  | None                      |
| Re-open Batch                                                  | FBAA LEVEL 1 PMT  | None                      |
| Pricer Batch Release                                           | FBAA LEVEL 1 PMT  | None                      |
| Re-initiate Pricer Rejected Items                              | FBAA LEVEL 1 PMT  | None                      |
| Release a Batch                                                | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Re-initiate Rejected Payment Items                             | FBAA LEVEL 1 PMT  | None                      |
| Batch Delete                                                   | FBAA LEVEL 1 PMT  | None                      |
| Open Ancillary Payment Batch                                   | FBAA LEVEL 1 PMT  | None                      |
| Community Nursing Home Main Menu                           | New Lock      | Old Lock              |
| Queue Data for Transmission                                    | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Update Vendor Contract/Rates – CNH                             | FBAA LEVEL 2      | None                      |
| Authorization Main Menu – CNH                              | New Lock      | Old Lock              |
| Enter CNH Authorization                                        | FBAA LEVEL 1 AUTH | None                      |
| Edit CNH Authorization                                         | FBAA LEVEL 1 AUTH | None                      |
| Cancel Authorization Entered in Error                          | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Change Existing Contract Rate for a Patient                    | FBAA LEVEL 1 AUTH | None                      |
| Delete CNH Rate                                                | FBAA LEVEL 2      | None                      |
| Enter Veteran Rates under new Vendor Contract                  | FBAA LEVEL 1 AUTH | None                      |
| Print List of Cancelled 7078                                   | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Batch Main Menu – CNH                                      | New Lock      | Old Lock              |
| Batch Delete                                                   | FBAA LEVEL 1 PMT  | None                      |
| Close-out Batch                                                | FBAA LEVEL 1 PMT  | None                      |
| Edit Batch data                                                | FBAA LEVEL 1 PMT  | None                      |
| Open CNH Batch                                                 | FBAA LEVEL 1 PMT  | None                      |
| Re-initiate Rejected Payment Items                             | FBAA LEVEL 1 PMT  | None                      |
| Re-open Batch                                                  | FBAA LEVEL 1 PMT  | None                      |
| Release a Batch                                                | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Fee Fund Control Main Menu – CNH                           | New Lock      | Old Lock              |
| Estimate Funds for Obligation                                  | FBAA LEVEL 1 AUTH |                           |
| Post Commitments for Obligation                                | FBAA LEVEL 1 AUTH |                           |
| Movement Main Menu – CNH                                   | New Lock      | Old Lock              |
| Admit To CNH                                                   | FBAA LEVEL 1 AUTH | None                      |
| Delete Movement Menu                                           | FBAA LEVEL 1 AUTH | None                      |
| Discharge From CNH                                             | FBAA LEVEL 1 AUTH | None                      |
| Edit Movement Menu                                             | FBAA LEVEL 1 AUTH | None                      |
| Transfer Movement                                              | FBAA LEVEL 1 AUTH | None                      |
| Delete Movement Menu                                       | New Lock      | Old Lock              |
| Admission Delete                                               | FBAA LEVEL 1 AUTH | None                      |
| Discharge Delete                                               | FBAA LEVEL 1 AUTH | None                      |
| Transfer Delete                                                | FBAA LEVEL 1 AUTH | None                      |
| Edit Movement Menu                                         | New Lock      | Old Lock              |
| Admission Edit                                                 | FBAA LEVEL 1 AUTH | None                      |
| Discharge Edit                                                 | FBAA LEVEL 1 AUTH | None                      |
| Transfer Edit                                                  | FBAA LEVEL 1 AUTH | None                      |
| Payment Main Menu – CNH                                    | New Lock      | Old Lock              |
| Delete Inpatient Invoice                                       | FBAA LEVEL 1 PMT  | None                      |
| Edit CNH Payment                                               | FBAA LEVEL 1 PMT  | None                      |
| Enter CNH Payment                                              | FBAA LEVEL 1 PMT  | None                      |
| Medical Fee Main Menu                                      | New Lock      | Old Lock              |
| Enter Authorization                                            | FBAA LEVEL 1 AUTH | None                      |
| Supervisor Main Menu                                           | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Terminate ID Card                                              | FBAA LEVEL 1 AUTH | None                      |
| Batch Main Menu                                            | New Lock      | Old Lock              |
| Batch Delete                                                   | FBAA LEVEL 1 PMT  | None                      |
| Close-out Batch                                                | FBAA LEVEL 1 PMT  | None                      |
| Edit Batch data                                                | FBAA LEVEL 1 PMT  | None                      |
| Open a Batch                                                   | FBAA LEVEL 1 PMT  | None                      |
| Re-open Batch                                                  | FBAA LEVEL 1 PMT  | None                      |
| Release a Batch                                                | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Outputs Main Menu                                          | New Lock      | Old Lock              |
| Group 7079 Print                                               | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Payment menu                                               | New Lock      | Old Lock              |
| Delete Payment Entry                                           | FBAA LEVEL 1 PMT  | None                      |
| Edit Payment                                                   | FBAA LEVEL 1 PMT  | None                      |
| Enter Payment                                                  | FBAA LEVEL 1 PMT  | None                      |
| Multiple Payment Entry                                         | FBAA LEVEL 1 PMT  | None                      |
| Re-initiate Rejected Payment Items                             | FBAA LEVEL 1 PMT  | None                      |
| Reimbursement Payment Entry                                    | FBAA LEVEL 1 PMT  | None                      |
| Travel Payment Only                                            | FBAA LEVEL 1 PMT  | None                      |
| Supervisor Main Menu                                       | New Lock      | Old Lock              |
| Clerk Look-Up For An Authorization                             | FBAASUPERVISOR    | FBAASUPERVISOR by FBAACLU |
| Enter/Edit Suspension Letters                                  | FBAASUPERVISOR    | None                      |
| Edit Pharmacy Invoice Status                                   | FBAA LEVEL 2      | None                      |
| Fee Basis 1358 Segregation of Duty Report                      | FBAASUPERVSIOR    | None                      |
| Pricer Batch Release                                           | FBAA LEVEL 1 PMT  | None                      |
| Queue Data for Transmission                                    | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Re-initiate Rejected Payment Items                             | FBAA LEVEL 1 PMT  | None                      |
| Release a Batch                                                | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Void Payment Main Menu                                         | FBAA LEVEL 2      | None                      |
| Fee Schedule Main Menu (under Supervisor Main Menu)        | New Lock      | Old Lock              |
| Add/Edit Fee Schedule                                          | FBAASUPERVISOR    | None                      |
| Compile Fee Schedule                                           | FBAASUPERVISOR    | None                      |
| FPPS Update & Transmit Menu (under Supervisor Main Menu)   | New Lock      | Old Lock              |
| Outpatient/Ancillary Invoice Edit                              | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Pharmacy Invoice Edit                                          | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Inpatient Invoice Edit                                         | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Purge Message Text                                             | FBAA LEVEL 2      | FBAASUPERVISOR            |
| MRA Main Menu (under Supervisor Main Menu)                 | New Lock      | Old Lock              |
| Vendor MRA Main Menu                                           | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Veteran MRA Main Menu                                          | FBAA LEVEL 2      | None                      |
| Vendor MRA Main Menu (under MRA Main Menu)                 | New Lock      | Old Lock              |
| Update FMS Vendor File in Austin                               | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Delete Vendor MRA                                              | FBAA LEVEL 2      | FBAASUPERVISOR            |
| Reinstate Vendor MRA                                           | FBAA LEVEL 2      | None                      |
| MRA'S Awaiting Austin Approval                                 | FBAA LEVEL 2      | None                      |
| Veteran MRA Main Menu (under MRA Main Menu)                | New Lock      | Old Lock              |
| Add type Veteran MRA                                           | FBAA LEVEL 2      | None                      |
| Change type Veteran MRA                                        | FBAA LEVEL 2      | None                      |
| Delete type Veteran MRA                                        | FBAA LEVEL 2      | None                      |
| Reinstate type Veteran MRA                                     | FBAA LEVEL 2      | None                      |
| Unauthorized Claims File Menu (under Supervisor Main Menu) | New Lock      | Old Lock              |
| Add New Person for Unauthorized Claim                          | FBAA LEVEL 1 AUTH | None                      |
| Disapproval Reasons File Enter/Edit                            | FBAASUPERVISOR    | None                      |
| Dispositions File Edit                                         | FBAASUPERVISOR    | None                      |
| Request Info File Enter/Edit                                   | FBAASUPERVISOR    | None                      |
| Void Payment Main Menu (under Supervisor Main Menu)        | New Lock      | Old Lock              |
| CH Delete Void Payment                                         | FBAA LEVEL 2      | FBAASUPERVISOR by FBCHVP  |
| CH Void Payment                                                | FBAA LEVEL 2      | FBAASUPERVISOR by FBCHVP  |
| CNH Delete Void Payment                                        | FBAA LEVEL 2      | FBAASUPERVISOR by FBCHVP  |
| CNH Void Payment                                               | FBAA LEVEL 2      | FBAASUPERVISOR by FBCHVP  |
| Medical Delete Void Payment                                    | FBAA LEVEL 2      | FBAASUPERVISOR by FBAAVP  |
| Medical Void Payment                                           | FBAA LEVEL 2      | FBAASUPERVISOR by FBAAVP  |
| Pharmacy Delete Void Payment                                   | FBAA LEVEL 2      | FBAASUPERVISOR by FBAAPHV |
| Pharmacy Void Payment                                          | FBAA LEVEL 2      | FBAASUPERVISOR by FBAAPHV |
| Pharmacy Fee Main Menu                                     | New Lock      | Old Lock              |
| Closeout Pharmacy Invoice                                      | FBAA LEVEL 1 PMT  | None                      |
| Complete Pharmacy Invoice                                      | FBAA LEVEL 1 PMT  | None                      |
| Edit Pharmacy Invoice                                          | FBAA LEVEL 1 PMT  | None                      |
| Enter Pharmacy Invoice                                         | FBAA LEVEL 1 PMT  | None                      |
| Patient Re-imbursement                                         | FBAA LEVEL 1 PMT  | None                      |
| Batch Menu – Pharmacy                                      | New Lock      | Old Lock              |
| Batch Delete                                                   | FBAA LEVEL 1 PMT  | None                      |
| Close-out Batch                                                | FBAA LEVEL 1 PMT  | None                      |
| Edit Batch data                                                | FBAA LEVEL 1 PMT  | None                      |
| Open a Pharmacy Batch                                          | FBAA LEVEL 1 PMT  | None                      |
| Re-open Batch                                                  | FBAA LEVEL 1 PMT  | None                      |
| Release a Batch                                                | FBAA LEVEL 2      | FBAASUPERVISOR            |
| State Home Main Menu                                       | New Lock      | Old Lock              |
| Enter New State Home Authorization                             | FBAA LEVEL 1 AUTH | None                      |
| Change a State Home Authorization                              | FBAA LEVEL 1 AUTH | None                      |
| Delete a State Home Authorization                              | FBAA LEVEL 1 AUTH | None                      |
| Reinstate State Home Authorization                             | FBAA LEVEL 1 AUTH | None                      |
| Unauthorized Claim Main Menu                               | New Lock      | Old Lock              |
| Request Information on Unauthorized Claim                      | FBAA LEVEL 1 AUTH | None                      |
| Receive Requested Information                                  | FBAA LEVEL 1 AUTH | None                      |
| Letters for Unauthorized Claim                                 | FBAA LEVEL 1 AUTH | None                      |
| Payments for Unauthorized Claims                               | FBAA LEVEL 1 PMT  | None                      |
| Enter/Edit Unauthorized Claim Menu                         | New Lock      | Old Lock              |
| Enter Unauthorized Claim                                       | FBAA LEVEL 1 AUTH | None                      |
| Modify Unauthorized Claim                                      | FBAA LEVEL 1 AUTH | None                      |
| Disposition Unauthorized Claim                                 | FBAA LEVEL 1 AUTH | None                      |
| Re-open Unauthorized Claim                                     | FBAA LEVEL 1 AUTH | None                      |
| Initiate Appeal for Unauthorized Claim                         | FBAA LEVEL 1 AUTH | None                      |
| Appeal Edit for Unauthorized Claim                             | FBAA LEVEL 2      | None                      |
| COVA Appeal Enter/Edit                                         | FBAA LEVEL 2      | None                      |
| Letters for Unauthorized Claim                             | New Lock      | Old Lock              |
| Update Date Letter Sent                                        | FBAA LEVEL 1 AUTH | None                      |
| Batch Print Letters                                            | FBAA LEVEL 1 AUTH | None                      |
| Reprint Letter(s)                                              | FBAA LEVEL 1 AUTH | None                      |
| Utilities for Unauthorized Claims                          | New Lock      | Old Lock              |
| Add New Person for Unauthorized Claim                          | FBAA LEVEL 1 AUTH | None                      |
| Associate an Unauthorized Claim to a Primary                   | FBAA LEVEL 1 AUTH | None                      |
| Disassociate an Unauthorized Claim                             | FBAA LEVEL 1 AUTH | None                      |
| Return Address Display/Edit                                    | FBAA LEVEL 2      | None                      |

Table used for formatting purposes, only.Table used for formatting purposes, only.

## Existing Menu Options Attached to Other Fee Basis Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several menu options attached to the Supervisor Main Menu are *now* also attached to other Fee Basis menus so they can be utilized by users who should not have supervisor access. These options and their placement are listed as follows.

### Delete reject flag \[FBAA VOUCHER DELETE REJECT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added to Batch Main Menu (under Medical Fee Main Menu)
- Added to Batch Menu - Pharmacy (under Pharmacy Fee Main Menu)

### Finalize a Batch \[FBAA FINALIZE BATCH\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added to Batch Main Menu (under Medical Fee Main Menu)
- Added to Batch Menu - Pharmacy (under Pharmacy Fee Main Menu)

### List Batches Pending Release \[FBAA LIST CLOSED BATCHES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Added to Batch Main Menu (under Medical Fee Main Menu)
- Added to Batch Menu - Pharmacy (under Pharmacy Fee Main Menu)
- Added to Batch Main Menu - CH (under Civil Hospital Main Menu)

## Revised Locks to Prevent Selection of Payment or Batch Entered by Another User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many options used to enter or edit payments and payment batches prevent selection of a payment or batch that was entered by another user. This restriction is not imposed on a user who holds the FBAASUPERVISOR security key.

Many options used to enter or edit payments and payment batches prevent selection of a payment or batch when the batch has certain status values such as supervisor closed. Fewer batch status values are restricted for a user who holds the FBAASUPERVISOR security key.

The following menu options are modified by this patch to check for the new FBAA LEVEL 2 security key INSTEAD OF the existing FBAASUPERVISOR security key when imposing restrictions on the selection of a payment or payment batch.

- Edit Batch data \[FBAA BATCH EDIT\]
- Close-out Batch \[FBAA CLOSE BATCH\]
- Re-open Batch \[FBAA REOPEN BATCH\]
- Batch Delete \[FBAA BATCH DELETE\]
- Enter Payment \[FBAA ENTER PAYMENT\]
- Multiple Payment Entry \[FBAA MULTIPLE PAYMENT ENTRY\]
- Reimbursement Payment Entry \[FBAA MEDICAL REIMBURSEMENT\]
- Ancillary Contract Hosp/CNH Payment \[FBCH ANCILLARY PAYMENT\]
- Multiple Ancillary Payments \[FBCH MULTIPLE PAYMENTS\]
- Patient Reimbursement for Ancillary Services \[FBCH ANCILLARY REIMBURSEMENT\]
- Payments for Unauthorized Claims \[FBUC PAYMENTS\]
- Delete Payment Entry \[FBAA DELETE PAYMENT\]
- Complete a Payment \[FBCH COMPLETE PAYMENT\]
- Re-initiate Pricer Rejected Items \[FBCH REINITIATE PRICER REJECTS\]
- Delete Inpatient Invoice \[FBCH DELETE INVOICE\]
- Invoice Edit \[FBCH EDIT PAYMENT\]
- Edit CNH Payment \[FBCNH EDIT PAYMENT\]
- Delete Inpatient Invoice \[FBCH DELETE INVOICE\]
- Edit Payment \[FBAA EDIT PAYMENT\]
- Edit Ancillary Payment \[FBCH EDIT ANCILLARY PAYMENT\]
- Edit Pharmacy Invoice \[FBAA EDIT PHARMACY INVOICE\]

## Revised Locks During Selection Of Civil Hospital Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option Delete Notification/Request \[FBCH DELETE REQUEST\] currently restricts the selection of a notification/request to the USER ENTERING NOTIFICATION unless the FBAASUPERVISOR key is held. This option is modified by this patch to instead check if the user holds the FBAA LEVEL 2 security key.

## Removed Lock on Entry of Amount Paid that Exceeds the Amount Claimed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Menu options used to enter or edit outpatient and ancillary inpatient payments do not allow the user to enter an amount paid that exceeds the amount claimed or exceeds the calculated fee schedule amount unless the user holds the FBAASUPERVISOR key. This patch modifies the software by removing the requirement that a user hold the FBAASUPERVISOR security key to enter an amount paid that exceeds the amount claimed or fee schedule amount. The following options are modified:

- Enter Payment \[FBAA ENTER PAYMENT\]
- Multiple Payment Entry \[FBAA MULTIPLE PAYMENT ENTRY\]
- Reimbursement Payment Entry \[FBAA MEDICAL REIMBURSEMENT\]
- Ancillary Contract Hosp/CNH Payment \[FBCH ANCILLARY PAYMENT\]
- Multiple Ancillary Payments \[FBCH MULTIPLE PAYMENTS\]
- Patient Reimbursement for Ancillary Services \[FBCH ANCILLARY REIMBURSEMENT\]
- Payments for Unauthorized Claims \[FBUC PAYMENTS\]
- Edit Payment \[FBAA EDIT PAYMENT\]
- Edit Ancillary Payment \[FBCH EDIT ANCILLARY PAYMENT\]

## Lock to Update of CNH Contract or Rate Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of Patch FB\*3.5\*154, the FBAA LEVEL 2 security key locks the ability to update contract and rate data for a community nursing home vendor. The following options are modified to check if user holds this security key before allowing the contract and rate data to be updated:

- Vendor Enter/Edit \[FBCNH VENDOR ENTER/EDIT\]
- Display,Enter,Edit Demographics \[FBAA VENDOR DEMOGRAPHICS\]

## Lock to Run Interactive FPPS Transmit Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*154 modified the Transmit Invoices to FPPS \[FB FPPS TRANSMIT\] option to require the user to hold the FBAA LEVEL 2 security key when the option is run interactively from the menu. The patch does not make any changes to the option when it is run as a scheduled task (non-interactively).

## List of Pending 7078s Modified to Consider Different Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*154 modified option Civil Hospital Main Menu \[FBCH MAIN MENU\] to check if the user holds the FBAA LEVEL 2 security key, rather than the FBAASUPERVISOR security key, to determine if all pending 7078s should be displayed, rather than only those entered by the current user.

## New User Access Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*154 creates a new option called Security Key Report for Fee Basis \[FB SEC KEY RPT\]. This option is attached to the Supervisor Main Menu \[FBAA SUPERVISOR OPTIONS\] and it is locked by the FBAASUPERVISOR security key. This new option generates a report of users that hold Fee Basis security keys. An example is shown below:

> Select Supervisor Main Menu Option: Security Key Report for Fee Basis

> Should report include terminated users with keys? NO//

> Sort by Security Key or User: (S/U): SECURITY KEY

> Select Fee Basis Security Key: ALL//

> DEVICE: HOME//

> Security Key Report for Fee Basis OCT 17, 2014@11:01:28 page 1

> by Security Key for all FB keys

> Name SSN Title

> ----------------------------------- ---- -----------------------------

> Key: FB ARCH

> FEEUSER,FIRST 2709 COMPUTER SYSTEMS ANALYST

> Division(s): 500, 688

> FEEUSER,SECOND 8420

> Division(s): 500

> Key: FBAA LEVEL 1 AUTH

> FEEUSER,FIRST 2709 COMPUTER SYSTEMS ANALYST

> Division(s): 500, 688

> FEEUSER,THIRD 1234 COMPUTER SYSTEMS ANALYST

> Division(s): 500, 688

## Disable Site Parameter EDIT AUTH. DURING PAYMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The site parameter EDIT AUTH. DURING PAYMENT allows selected authorization fields to be edited when some types of payments are entered. Patch FB\*3.5\*154 disabled this site parameter. The user will no longer be prompted to respond to this site parameter when configuring the software. This site parameter will no longer have *any* effect on the Fee Basis software's behavior.

## Prevent Entry of Payment or Pricing if User Entered Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*154 modifies the software to prevent a user from entering payment or pricing for a service if that user previously entered or edited the associated authorization for the service. Entry or editing a civil hospital notification, community nursing home contract rate for a patient, community nursing home movement, or unauthorized claim is considered as a change to the associated authorization.

The options used to enter or edit *authorizations* are modified to keep track of users. The options used to process payments are modified to prevent the user who entered or edited the *authorization* associated with the payment from proceeding.

## Nursing Home Daily Rate Cannot be Entered During Payment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*154 modifies the Enter CNH Payment \[FBCNH ENTER PAYMENT\] option to no longer allow entry of missing daily rates. An update to the daily rate is considered an edit of the authorization and the person who processes the payment cannot edit the authorization per separation of duties business rules.

## New and Modified Reports Display Users that Entered or Edited Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*154 modifies one existing report and adds three new reports to display the list of users who have entered or edited an authorization or associated records. These options, listed as follows, are all locked by the FBAASUPERVISOR security key.

### Existing Report: Clerk Look-Up for an Authorization \[FBAA CLERK LOOK-UP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This existing report option lists users who have entered or edited a specified authorization in the FEE BASIS PATIENT file. When applicable, the output also show users who have entered or edited the civil hospital notification or unauthorized claims associated with the authorization.

### New Report: Clerk Lookup for 7078 Authorization \[FBCH CLERK LOOKUP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new report option lists users who have entered or edited a specified 7078 authorization. Entry or editing of nursing home rate and movements are included in this output. When applicable, the output also shows users who have entered or edited the civil hospital notification associated with the authorization.

This report is located on two menu options:

- Output Menu under the Civil Hospital Main Menu
- Output Main Menu – CNH under the Community Nursing Home Main Menu

### New Report: Clerk Lookup for Notification/Request \[FBCH REQUEST CLERK LOOKUP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new report option lists users who have entered or edited a specified notification/request. It is located on the Notification/Request Menu under the Civil Hospital Main Menu.

### New Report: Clerk Lookup for Unauthorized Claim \[FBUC CLERK LOOKUP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new report option lists users who have entered or edited a specified unauthorized claim. It is located on the Outputs for Unauthorized Claims menu under the Unauthorized Claim Main Menu.

# New Service Requests (NSRs) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## NSR \#20090309: EMERGENCY PATCH VISTA FEE - SEPARATION OF DUTIES - ASSIGNMENT OF KEYS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Recent IG/MQAS VistA Fee Audits have identified issues not in compliance with directives requiring separation of processing and authorization of payment for non-VA claims duties, with clerical staff being assigned supervisory menu options. Due to this discovery recommendations were made to remove assignment of the FBAASUPERVISOR key for clerical staff.

Removal of these keys has created a problem for clerical staff, preventing them from appropriately pricing invoice line items in compliance with regulatory requirements for correct pricing of claims. Productivity of processing claims has been drastically reduced.

Requirements Development & Management New Service Request Database (NSRD) Link: <span id="_Toc462748871" class="anchor"></span>

REDACTED

NSR \#20120609: PROBLEM WITH FEE BASIS PAYMENT FILE/POV ISSUE

There can be a problem with the association of an outpatient or inpatient ancillary payment to the appropriate authorization. The problem occurs when there are payments that should be associated with different authorizations, but those payments have the exact same patient, vendor, and date of service. This situation is common with home health services where there are separate authorizations for nursing and non-nursing services for a single patient and those services are provided to the patient by the same vendor on the same date.

This problem can result in various errors including sending the wrong purpose of visit code when a payment batch is sent to Central FEE.

The problem was originally reported on Remedy Ticket \#726099. A fix for this issue was requested by New Service Request \#20120609.

Patch FB\*3.5\*154 modifies the software to prevent the problem from occurring for new payments. Additionally, when the patch is installed a one-time job examines existing payments and corrects many or all of the existing inappropriate associations.

NSRD Link: REDACTED

# REMEDY Tickets and Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## REMEDY Ticket \#833468 Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Problem: An undefined error occurs when a prescription is deleted from an existing pharmacy invoice using the Edit Pharmacy Invoice \[Edit Pharmacy Invoice\] option.
- Resolution: This patch modifies routine FBAAEPI to prevent the undefined error from occurring.

## REMEDY Ticket \#985307 Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Problem: The Re-initiate Rejected Payment Items \[FBAA REINITIATE REJECTS\] option contains a fault when it is used to re-initiate all items in an outpatient or ancillary inpatient (type B3) payment batch. The problem does not occur when the line items are individually re-initiated.

> The software attempts to track all payment lines (sorted by invoice) that are re-initiated into the new batch. If all the lines on an invoice are not moved into the new batch the re-initiated lines are assigned a different invoice number so an invoice is not spilt between two different payment batches.

> The problem is that the software does not determine the invoice number when a line is re-initiated. If the batch was previously displayed the invoice of the last displayed line item is inappropriately treated as the invoice of all the re-initiated line items. If the batch was not displayed the option a bends with an undefined error for variable FBIN.

- Resolution: The problem is corrected by modifying routine FBAARR1 within line tag REJM so the invoice number of a line item is appropriately determined before it is referenced later in that section of code.

# Documentation Retrieval Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated user documentation describing the new functionality introduced by this patch is available.

## Office of Information and Technology (OI&T) Document Retrieval Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this patch is available.

The preferred method is to retrieve files from REDACTED This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

- Albany: REDACTED
- Hines: REDACTED
- Salt Lake City: REDACTED

## VA Software Document Library (VDL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation can also be found on the VA Software Document Library (VDL) at:

<http://www.va.gov/vdl/application.asp?appid=40>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: FB*3.5*108 Release Notes

## Hardware Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special hardware considerations.

## System Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special system considerations.

## Pre-Installation Considerations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to the installation of FB\*3.5\*108 all open Fee Basis batches must be closed. And all closed batches must be transmitted to Central Fee at the Austin Information Technology Center (AITC).

With the installation of FB\*3.5\*108 batch message size will be limited to 32k bytes maximum. For an inpatient batch this will be 85 lines of data. If the message exceeds 32k Central Fee will reject the batch.

This patch reduces the maximum size of a payment batch from 100 to 85 lines. This limit applies to the B3 (outpatient and ancillary) and B5 (pharmacy) payment batches. This patch introduces a maximum 42 line limit for the contract hospital batch and a maximum 61 line limit for the community nursing home batch.

If larger batches are not transmitted to AITC before this patch is installed, the batches will have to be divided into smaller batches and resubmitted.

Associated patches that must be installed BEFORE FB\*3.5\*108

> FB\*3.5\*107 FB\*3.5\*25 FB\*3.5\*67 FB\*3.5\*68

> FB\*3.5\*79 FB\*3.5\*82 FB\*3.5\*98 FB\*3.5\*103

> FB\*3.5\*116 FB\*3.5\*122 FB\*3.5\*133

## ## Installation Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If installed during the normal workday, it is recommended that the following

selection(s) in the OPTION (#19) file, and all of their descendants be disabled

to prevent possible conflicts while running the KIDS Install. Other VISTA users

will not be affected.

> Civil Hospital Main Menu \[FBCH MAIN MENU\]

Community Nursing Home Main Menu \[FBCNH MAIN MENU\]

Medical Fee Main Menu \[FBAA MEDICAL MAIN MENU\]

Pharmacy Fee Main Menu \[FBAA PHARMACY MAIN MENU\]

Telephone Inquiry Menu \[FB PHONE MENU\]

Unauthorized Claim Main Menu \[FBUC MAIN\]

Install Time - less than 5 minutes

1\. Choose the PackMan message containing this patch.

2\. Choose the INSTALL/CHECK MESSAGE PackMan option.

3\. From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following option. When prompted for the INSTALL, enter the patch \# (FB\*3.5\*108):

1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

4\. From the Installation Menu, select the Install Package(s) option and choose the patch to install.

5\. When prompted 'Want KIDS to Rebuild Manu Trees Upon Completion of Install NO//

Answer YES

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' Accept the default of NO

7\. When prompted 'Enter options you wish to mark as 'Out Of Order':'

Enter the following options:

Civil Hospital Main Menu \[FBCH MAIN MENU\]

Community Nursing Home Main Menu \[FBCNH MAIN MENU\]

Medical Fee Main Menu \[FBAA MEDICAL MAIN MENU\]

Pharmacy Fee Main Menu \[FBAA PHARMACY MAIN MENU\]

Telephone Inquiry Menu \[FB PHONE MENU\]

Unauthorized Claim Main Menu \[FBUC MAIN\]

8\. If prompted "Delay Install (Minutes): (0-60): 0// respond 0

Post Installation Instructions

> The post installation routine will automatically set up two contracts in the FEE BASIS CONTRACT (# 161.43) that currently have national contracts.

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites may retrieve documentation in one of the following ways:

1.  The preferred method is to FTP the files from REDACTED, which will transmit the files from the first available FTP server.
2.  Sites may also elect to retrieve documentation directly from a specific server as follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

 

3.  Documentation can also be retrieved from the VistA Documentation Library (VDL) on the Internet at the following address:

<http://www.va.gov/vdl>.

The documentation distribution includes:

<u>TITLE</u> <u>FILE NAME</u>

Fee Basis User Manual FB_3_5_UM_R0512.PDF

Fee Basis Release Notes/Installation Guide (FB\*3.5\*108) FB_3_5_P108_RN.PDF

Fee Basis Technical Manual/Security Guide FB_3_5_TM_R0512.PDF

> **NOTE:** Use ASCII mode when transferring the .KID file.

> Use Binary mode when transferring the .PDF file.  The .PDF files can be read on a PC using the Adobe Acrobat Reader program. The VistA Documentation Library \[VDL\] contains all end-user manuals.

## CONTRACTED SERVICES AND CONTRACTS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch allows contracts to be entered for Medical Fee and Civil Hospital authorizations and payments. Payment transactions sent from to Central Fee is modified to include the contract number. The contract number is used to identify payments for pilot project HERO. Contracts not associated with project HERO can also be entered and tracked using the new functionality. The new contract functionality does not replace or modify the existing use of contracts in the Community Nursing Home module. This patch also modifies VistA Fee Basis to prevent payments for unauthorized claims from being considered as contracted services.

### New Contract File 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds a new FEE BASIS CONTRACT (#161.43) file. This file contains a list of contracts for the local site. Each contract can have one or more associated vendors.

A new option allows users to enter or edit contracts in this file. The option is named Contract File Enter/Edit \[FBAA CONTRACT FILE\]. The option is locked with the FBAASUPERVISOR security key. It is attached to the Supervisor Main Menu \[FBAA SUPERVISOR OPTIONS\].

Four existing options are moved from the supervisor menu to a new sub-menu to make room for the new contract option. The new sub-menu is the Unauthorized Claims File Menu \[FBCU FILE MENU\]. The options moved to this menu are:

> Add New Person for Unauthorized Claim \[FBUC ADD NEW PERSON\]

> Disapproval Reasons File Enter/Edit \[FBUC DISAPPROVAL REASONS FILE\]

> Dispositions File Edit \[FBUC DISPOSITIONS FILE\]

> Request Info File Enter/Edit \[FBUC REQUEST INFO FILE\]

### Project HERO Contracts 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch automatically enters the following two contracts into the FEE BASIS CONTRACT file for sites that are in VISN 8, 16, 20, or 23.

> CONTRACT NUMBER ASSOCIATED VENDOR ID

> VA101(049A3)-P-0269 942761537 (Delta)

> VA101049A3-P-0270 208418853 (HVHS)

These two contracts are for pilot project HERO. Sites in these VISNs must ensure that a project HERO contract is specified on all appropriate authorizations and payments. These contract numbers are be used by the Austin database to track services provided under project HERO.

### Identify Contract on Authorization 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch modifies the software so users can select a contract when entering or editing authorizations under the Medical Fee and Civil Hospital modules. Only contracts with an active status can be selected. Only contracts associated with the authorized vendor can be selected. Therefore, contracts cannot be entered on a Medical Fee authorization that does not have a specified vendor.

> **NOTE:** Sites that wish to enter contracts on Medical Fee authorizations must ensure the site parameter "ASK VENDOR DURING AUTH." is set to "Y" so vendors can be entered on the authorization.

### Payments for Unauthorized Claims not for a Contracted Service 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch modifies the software to stop asking the user if a line item is for a contracted service when a payment for an unauthorized claim is entered or edited. The system automatically considers these payments as not being for contracted services. This modification prevents an interest penalty from being applied to payments for unauthorized claims. This modification applies to payments for all claims entered via the unauthorized claims module including those considered under the provisions of 38 U.S.C. 1725 and 38 U.S.C. 1728. It is not be possible to specify a contract on payments for unauthorized claims.

### Identify Contract on Invoice/Payment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch modifies the software so a contract can be specified when Medical Fee and Civil Hospital invoices/payments are entered or edited. The following rules apply:

- If a contract is specified on the associated authorization and the vendor being paid matches the vendor on the authorization, the software automatically identifies the payment as a contracted service under the same contract as on the authorization.
- If the contract is not automatically selected due to the authorization (see above) and the user indicates that the line item is for a contracted service, the user is prompted for a contract. This is an optional field. Only contracts with an active status can be selected. Only contracts associated with the vendor being paid can be selected.

## ADDITIONAL DATA AND LARGER \$ AMOUNTS FOR CIVIL HOSPITAL INVOICE 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch modifies civil hospital authorizations and invoices and the Generic Pricer option. The maximum dollar amount is increased from \$999,999.99 to \$9,999,999.99. The maximum number of diagnosis codes and maximum number of procedure codes is increased from 5 to 25. Additional data elements must be entered on the invoice and generic Pricer. A present on admission indicator (POA) must be entered for each diagnosis code. An admitting diagnosis code must be entered. These new data elements are included in the message sent to the NVH Pricer system and in the B9 payment transaction sent to Central Fee.

### Present on Admission Indicator 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch modifies the software to require entry of a POA (present on admission indicator) for each diagnosis code on a civil hospital invoice and generic Pricer. An example follows:

> POA1: ?

> Enter the present on admission indicator for the ICD1 diagnosis.

> Answer with PRESENT ON ADMISSION CODE

> Choose from:

> 1 Unreported/Not used. Exempt from POA reporting.

> N Diagnosis was not present at time of inpatient admission.

> U Documentation insufficient to determine.

> W Provider unable to clinically determine.

> Y Diagnosis was present at time of inpatient admission.

### Admitting Diagnosis 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch modifies the software to require entry of an Admitting on a civil hospital invoice and a generic Pricer.

An example follows:

> ADMITTING DIAGNOSIS: ?

> Enter the admitting diagnosis for this claim.

> Answer with ICD DIAGNOSIS CODE NUMBER, or DESCRIPTION

> Do you want the entire 14954-Entry ICD DIAGNOSIS List?

## SEND EDI CLAIM IDENTIFIER TO CENTRAL FEE 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch modifies VistA Fee Basis to include an EDI identifier in the B3 (outpatient and ancillary), B5 (pharmacy), and B9 (civil hospital and community nursing home) payment transactions that are sent to Central Fee. No additional data entry is required since EDI claims are identified using the existing FPPS CLAIM ID field.

## SEND PATIENT ACCOUNT NUMBER TO CENTRAL FEE 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch modifies VistA Fee Basis to include the value of the existing PATIENT ACCOUNT NUMBER field in the B3 (outpatient and ancillary) payment transaction that is sent to Central Fee.

This patch modifies VistA Fee Basis to include the value of the existing PATIENT CONTROL NUMBER field in the B9 (civil hospital and community nursing home) payment transaction that is sent to Central Fee.

## REDUCE RISK OF INTERFACE ERRORS 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch contains new line limits for payment batches. It also examines several data fields that are sent in a batch message to ensure the space allotted for that field is not exceeded.

### Batch Line Limits 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Central Fee can only accept 32K characters in a single payment batch. Since this patch includes additional data in payment batches, the maximum number of lines in a batch must be reduced to avoid a reject of the entire batch by Central Fee.

This patch reduces the maximum size of a payment batch from 100 to 85 lines. This limit applies to the B3 (outpatient and ancillary) and B5 (pharmacy) payment batches. This patch introduces a maximum 42 line limit for the contract hospital batch and a maximum 61 line limit for the community nursing home batch.

The following site parameters control these limits.

- MAX \# PAYMENT LINE ITEMS: 85// ??

> The maximum number of payment line items that will be allowed in a batch. Any number between 1 and 85 is acceptable. This value is checked during the enter payment options and will warn the clerks when they are within 20 of the maximum. It prevents the clerks from exceeding this number.

- MAX \# CH PAYMENT LINES: 42// ??

> The maximum number of payment line items that will be allowed in a contract hospital batch. This value is checked during the enter payment options and will warn the clerks when they are within 5 of the maximum. It prevents the clerks from exceeding this number.

- MAX \# CNH PAYMENT LINES: 61// ??

> The maximum number of payment line items that will be allowed in a community nursing home batch. This value is checked during the enter payment options and will warn the clerks when they are within 5 of the maximum. It prevents the clerks from exceeding this number.

### Length of Stay on Pricer Transaction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NVH Pricer system in Austin does not support a length of stay greater than 999 days. The message sent from VistA to the NVH Pricer only allocates 3 digits for the computed length of stay value. Austin has reported instances where the message sent from VistA has included more than 3 digits for the length of stay resulting in a formatting error.

This patch modifies the Generic Pricer option to prevent entry of a discharge date that is more than 999 days after the admission date. This patch also modifies the Pricer batch message to send "\*\*\*" as the length of stay if the computed value exceeds 3 digits. This will result in a reject of the line by the NVH Pricer, but the remaining lines in the batch will no longer be adversely impacted.

### State Abbreviation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The message sent to the NVH Pricer and the B3, B5, and B9 payment batch sent to Central Fee contain a two character state abbreviation. In some cases, the 'state' CANADA was selected. This 'state' has a character abbreviation in the STATE file and the entire value was being placed in the message resulting in a format error.

This patch modifies these messages to send "\*\*" as the state abbreviation if the state abbreviation exceeds 2 characters. This will result in a reject of the line, but the remaining lines in the batch will no longer be adversely impacted.

### From: FB*3.5*132 Release Notes

## Background/Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In 2009, VA facilities reported to Central Fee and VistA that duplicate payments were being paid to the same vendor for the same instance of Veteran's care and only one of the payments could be located in the VistA Fee files. Further investigation validated that there were many instances of these erroneous payments.

Full implementation of the two-phased release of VistA Fee and IFCAP Automation Enhancement will prevent duplicate payments to Service Providers.

## New Service Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Fee and IFCAP Automation Enhancement—[20110212](http://vista.med.va.gov/nsrd/Tab_GeneralInfoView.asp?RequestID=20110212)

The following descriptive text is from the New Service Request Database (NSRD) for Request ID: [20110212](http://vista.med.va.gov/nsrd/Tab_GeneralInfoView.asp?RequestID=20110212).

New Capabilities

*"Automation of the finalization process to interface with the creation of an automated 994 code sheet in IFCAP."*Desired Change

*"This request was submitted by the Chief Business Office (CBO), Purchased Care Program Office. They are requesting enhancements to the VistA Fee Basis application in support of preventing duplicate payments which is occurring because there is currently no interface between the VistA Fee Application Batch Software, Central Fee and Integrated Funds Control, Accounting, and Procurement (IFCAP)/Financial Management System (FMS). The proposed enhancement seeks modifications to various modules of VA's VistA software application to include Fee Basis and IFCAP. Affected functions include Fee Batch, IFCAP, claims processing, and payments. Nothing has changed in the business environment per se, this has always been a manual process, but this needs to be automated in order to mitigate risks and to reduce the number of duplicate payments."*

Enhancements to the Fee Basis software exported with Patch FB\*3.5\*132 are documented as follows.

### From: FB*3.5*139 Release Notes

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service or dates of discharge for inpatients that occur on or after the ICD-10 Activation Date.

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

ICD-9-CM and ICD-10-CM Comparison

| ICD-9-CM                                 | ICD-10-CM                                                                     |
|------------------------------------------|-------------------------------------------------------------------------------|
| 13,000 codes (approximately)             | 68,000 codes (approximately)                                                  |
| 3-5 characters                           | 3-7 characters (not including the decimal)                                    |
| Character 1 is numeric or alpha (E or V) | Character 1 is alpha; character 2 is numeric;                                 |
| Characters 2 - 5 are numeric             | Characters 3–7 are alpha or numeric (alpha characters are not case sensitive) |
| Decimal after first 3 characters         | Same                                                                          |

ICD-9-CM and ICD-10-PCS Comparison

| ICD-9-CM Procedure Codes         | ICD-10-PCS                                                                                                                             |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 3-4 characters                   | 7 alphanumeric characters                                                                                                              |
| All characters are numeric       | Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1.                   |
| All characters are numeric       | Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character. |
| Decimal after first 2 characters | Does not contain decimals                                                                                                              |

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

Patch FB\*3.5\*139 makes the following changes to the FB application for the ICD-10 Diagnosis and Procedure Code Set implementation:

- Search Functionality for ICD-10-CM Diagnosis Code and ICD-10-PCS Procedure Code
- Add/Edit/Store and Display ICD-10-CM Diagnosis and ICD-10-PCS Procedure Code
- Print Information for ICD-10-CM Diagnosis and ICD-10-PCS Procedure Code
- Transmissions to the Central Fee and Non-VA-Hospital System (NVHS) Pricer systems to contain ICD-10-CM Diagnosis and ICD-10-PCS Procedure Code

The Product Development 508 Compliance Office Director, Patrick Sheehan, has determined that Fee Basis is a MUMPS roll-and-scroll application developed before 2004. A Section 508 CVS Application Form is in the process of being submitted to the VA for additional assessment.

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FB manuals are posted on the VistA Documentation Library (VDL) [Fee Basis](http://www.va.gov/vdl/application.asp?appid=40) page.

- The following FB manuals are updated with changes for FB\*3.5\*139.
  - FB V. 3.5 Technical Manual
  - FB V. 3.5 User Manual
- The following manuals do not contain changes relating to FB\*3.5\*139.
- FB V. 2.0 Package Security Guide
- FB V. 2.0 Installation Guide

## ICD-10-CM Diagnosis Code Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fee Basis ICD-10 diagnosis code search functionality allows the end user to select a single, valid ICD-10 diagnosis code and display its description. The Fee Basis user interface prompts the user for input, invokes the Lexicon utility to get data, and then presents that data to the end user.

This search method provides a "decision tree" type search that uses the hierarchical structure existing within the ICD-10-CM code set, as defined in the ICD-10-CM Tabular List of Diseases and Injuries, comprising categories, sub-categories, and valid ICD-10-CM codes.

ICD-10-CM diagnosis code search highlights include:

- Text-based search using one or more words as search terms, finding matches based on full descriptions, synonyms, key words, and shortcuts associated with ICD-10-CM diagnosis codes, which are inherently built into the Lexicon coding system.
- The more refined the search criteria used (i.e., the more descriptive the search terms), the more streamlined the process of selecting the correct valid ICD-10 diagnosis code will be.
- The user is presented with a manageable list of matching codes with descriptions, consisting of any combination of categories, sub-categories, and valid codes. The length of the list of items that is presented is set to a default of 20,000. If the list is longer, the user is prompted to refine the search.
- The user can "drill down" through the categories and sub-categories to identify the single, valid ICD-10-CM code that best matches the patient diagnosis.
- Short descriptions for the valid ICD-10-CM codes display.
- Partial code searches are also possible, as is full ICD-10-CM code entry, for situations where all or part of the code is known.

Example of ICD-10 Diagnosis Code Search

ICD1: S62

7 matches found

    1.  S62.0-     Fracture of navicular \[scaphoid\] bone of wrist

                   (147)
    2.  S62.1-     Fracture of other and unspecified carpal bone(s)

                   (357)
    3.  S62.2-     Fracture of first metacarpal bone (231)
    4.  S62.3-     Fracture of other and unspecified metacarpal

                   bone (560)
    5.  S62.5-     Fracture of thumb (105)
    6.  S62.6-     Fracture of other and unspecified finger(s)

                   (490)
    7.  S62.9-     Unspecified fracture of wrist and hand (21)

Select 1-7: 1

4 matches found

    1.  S62.00-    Unspecified fracture of navicular \[scaphoid\]

                   bone of wrist (21)
    2.  S62.01-    Fracture of distal pole of navicular \[scaphoid\]

                   bone of wrist (42)
    3.  S62.02-    Fracture of middle third of navicular \[scaphoid\]

                   bone of wrist (42)
    4.  S62.03-    Fracture of proximal third of navicular

                   \[scaphoid\] bone of wrist (42)

Select 1-4: 4

42 matches found

    1.  S62.031A   Displaced Fracture of Proximal third of

                   Navicular \[Scaphoid\] Bone of right Wrist, Initial Encounter

                   for closed Fracture
    2.  S62.031B   Displaced Fracture of Proximal third of

                   Navicular \[Scaphoid\] Bone of right Wrist, Initial Encounter

                   for open Fracture
    3.  S62.031D   Displaced Fracture of Proximal third of

                   Navicular \[Scaphoid\] Bone of right Wrist, Subsequent

                   Encounter for Fracture with Routine Healing
    4.  S62.031G   Displaced Fracture of Proximal third of

                   Navicular \[Scaphoid\] Bone of right Wrist, Subsequent

                   Encounter for Fracture with Delayed Healing
    5.  S62.031K   Displaced Fracture of Proximal third of

                   Navicular \[Scaphoid\] Bone of right Wrist, Subsequent

                   Encounter for Fracture with Nonunion
    6.  S62.031P   Displaced Fracture of Proximal third of

                   Navicular \[Scaphoid\] Bone of right Wrist, Subsequent

                   Encounter for Fracture with Malunion
    7.  S62.031S   Displaced Fracture of Proximal third of

                   Navicular \[Scaphoid\] Bone of right Wrist, Sequela
    8.  S62.032A   Displaced Fracture of Proximal third of

                   Navicular \[Scaphoid\] Bone of left Wrist, Initial Encounter

                   for closed Fracture

Press \<RETURN\> for more, "^" to exit, or Select 1-8: 1

## ICD-10-PCS Procedure Code Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*139 allows the user to continue to search for ICD-10 diagnosis and procedure codes in the same manner as with current ICD-9 diagnosis codes.

> **NOTE:** Existing ICD-9 search functionality has not changed.

## Inactive Code Searches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For both diagnosis and procedure code searches, if the characters entered match an inactive, valid ICD-10 code, the application displays the matching ICD-10 code and short description (up to 60 characters), along with an indication of the inactive status, providing the ability for user to confirm their selection. When the user confirms their selection, a message displays stating the code is inactive for the date of service (i.e. "Date of Interest"), along with the actual date of service. The code is not associated with the patient record, and the system prompts the user to enter a code.

## Add, Edit, Store ICD-10 Codes 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Please refer to the FB User Manual for information on ICD-9.

Patch FB\*3.5\*139 adds, edits and stores ICD-10 diagnosis and procedure codes within the following FB menu options:

- Unauthorized Claim Main Menu
  - Enter/Edit Unauthorized Claim Menu
  - Modify Unauthorized Claims
  - Re-open Unauthorized Claims
  - Payments for Unauthorized Claims
- Civil Hospital Main Menu
  - Payment Process Menu
  - Batch Main Menu
  - Generic Pricer Interface
- Community Nursing Home Main Menu
  - Enter/Edit CNH Authorization
- Medical Fee Main Menu
  - Enter Authorization
  - Payment Menu

## Display ICD-10-CM Diagnosis Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*139 displays ICD-10 diagnosis codes up to 8 characters with a decimal after the third character within the following FB menu options:

- Unauthorized Claim Main Menu
  - Payments for Unauthorized Claims
  - Display Unauthorized Claim
- Civil Hospital Main Menu
  - Payment Process Menu
  - Batch Main Menu
  - Output Menu
- Community Nursing Home Main Menu
  - Authorization Main Menu
  - Movement Main Menu
  - Output Main Menu
  - Payment Main Menu
- Medical Fee Main Menu
  - Outputs Main Menu
  - Payment Menu
  - Registration Menu
  - Supervisor Main Menu
- Pharmacy Fee Main Menu
  - Enter Pharmacy Invoice
  - Patient Re-imbursement
  - Review Fee Prescription
- Telephone Inquiry Menu

## Display ICD-10-PCS Procedure Code 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*139 displays ICD-10 procedure codes up to 7 characters without a decimal within the following FB menu options:

- Unauthorized Claim Main Menu
  - Payments for Unauthorized Claims
- Civil Hospital Main Menu
  - Payment Process Menu
  - Batch Main Menu
  - Output Menu
- Community Nursing Home Main Menu
  - Output Main Menu
- Telephone Inquiry Menu

## ICD-10-CM Diagnosis Code Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*139 prints ICD-10 diagnosis codes up to 8 characters with a decimal after the third character including short descriptions, and designates whether the diagnosis is ICD-9 or ICD-10 within the following FB menu options:

- Unauthorized Claim Main Menu
  - Add Vendor Payments Output
  - Add Veteran Payments Output
- Civil Hospital Main Menu
  - Output Menu
- Community Nursing Home Main Menu
  - Output Main Menu
- Medical Fee Main Menu
  - Outputs Main Menu
  - Print Rejected Payment Items
- Pharmacy Fee Main Menu
- Telephone Inquiry Menu

## ICD-10-PCS Procedure Code Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*139 prints ICD-10 procedure codes up to 7 characters without a decimal including short descriptions, and designates whether the diagnosis is ICD-9 or ICD-10 within the following FB menu options:

- Unauthorized Claim Main Menu
  - Payments for Unauthorized Claims
- Civil Hospital Main Menu
  - Output Menu
- Community Nursing Home Main Menu
  - Output Main Menu
- Medical Fee Main Menu
  - Outputs Main Menu
- Pharmacy Fee Main Menu
- Telephone Inquiry Menu

## ICD-10-CM Diagnosis Code Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*139 transmits ICD-10 diagnosis codes up to 8 characters with a decimal after the third character to the Central Fee and the Non-VA Hospital System (NVHS) Pricer systems in Austin, Texas.

> **NOTE:** Existing ICD-9 transmission capability has not changed.

## ICD-10-PCS Procedure Code Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*139 transmits ICD-10 procedure codes consisting of 7 alphanumeric characters without a decimal to the Central Fee and the Non-VA Hospital System (NVHS) Pricer systems in Austin, Texas.

> **NOTE:** Existing ICD-9 transmission capability has not changed.

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some FB routines were modified to replace direct global reads and old Application Program Interfaces (APIs) with new Standards and Terminology Services (STS) APIs and Lexicon APIs wherever possible.

The following new routines are added to FB:

| Routine Name | Function                                                                                                                                                     |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FBASF        | Advanced Search Functionality, asks for full or partial ICD-10 Diagnosis code and calls the Lexicon ICD-10 diagnosis search function to display the results. |
| FBASFL       | Advanced Search Functionality – displays a listing of ICD-10 diagnosis codes based on search entry.                                                          |
| FBASFU       | Advanced Search Functionality utilities.                                                                                                                     |
| FBICD9       | ICD-9 Diagnosis Code Utilities                                                                                                                               |
| FBICDP       | ICD-9 & 10 Procedure Code Utilities                                                                                                                          |

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new fields are added to FB:

| Field Name                  | Modifications                                                                                                                                                                       |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ICD Diagnosis field (#.087) | Add the ICD DIAGNOSIS field (#.087), a pointer field to the ICD DIAGNOSIS file (#80), to the AUTHORIZATION multiple field (#161.1) of the FEE BASIS PATIENT file (#161) for ICD-10. |
| ICD Diagnosis field (#5.1)  | Add the ICD DIAGNOSIS field (#5.1), a pointer field to the ICD DIAGNOSIS file (#80), to the FEE BASIS UNAUTHORIZED CLAIMS file (#162.7) for ICD-10.                                 |

*(This page intentionally left blank)*

### From: FB*3.5*124 Release Notes

## Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview

------------------------------

Standard Pre-Installation procedures for installing a patch from PackMan are all that is needed to install this patch.

No Post-Installation procedures are necessary to install this patch.

Installation Instructions

-------------------------

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install. Queuing the installation of this patch is not recommended.

1\. Choose the PackMan message containing this patch.

2\. Choose the INSTALL/CHECK MESSAGE PackMan option.

3\. From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL enter the patch number (FB\*3.5\*124):

> a\. Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.

> b\. Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).

> c\. Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

4\. From the Installation Menu, select the Install Package(s) option and choose the patch to install.

5\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' Accept the default of NO

6\. When prompted 'Enter options you wish to mark as 'Out Of

Order':' Enter the following options:

\[FBAA ENTER PAYMENT\]

\[FBAA MEDICAL REIMBURSEMENT\]

\[FBAA C&P ENTER PAYMENT\]

\[FBAA EDIT PHARMACY INVOICE\]

\[FBAA ENTER PHARMACY INVOICE\]

\[FBAA REIMBURSEMENT PHARMACY\]

\[FBAA MULTIPLE PAYMENT ENTRY\]

\[FBAA EDIT PAYMENT\]

\[FBCH ANCILLARY PAYMENT\]

\[FBCH ANCILLARY REIMBURSEMENT\]

\[FBCH ENTER PAYMENT\]

\[FBCH REIMBURSEMENT INVOICE\]

\[FBCH EDIT PAYMENT\]

\[FBCH MULTIPLE PAYMENTS\]

\[FBCH EDIT ANCILLARY PAYMENT\]

\[FBCNH EDIT PAYMENT\]

\[FBUC PAYMENTS\]

7\. If prompted "Delay Install (Minutes): (0-60): 0// respond 0

Post-Installation Instructions

------------------------------

There are no Post-Installation steps necessary for installing this patch.

## Technical Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Database Repository

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The existing VistA database shall be used for this enhancement. No new fields or files will be added.

### System Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The system features include the following:

This patch contains the modified components (Routines and Input Templates) which implement the VistA Financials Annual Enhancement called VistA Fee Invoice Acceptance Date Controls (NSR# 20080613). The intent of this patch is to prevent a Fee Basis Invoice from being approved for payment, if the Invoice was received at the VA prior to the date(s) of service for the services being billed on the Invoice.

The new checks are implemented at the field level as needed, wherever either the Invoice Received Date or the Date(s) of Service for an Invoice are entered. In cases where the Invoice Received Date is entered first, the user will not be allowed to enter a Date of Service which is later than the Invoice Received Date. If the Date(s) of Service are entered first, the user will not be allowed to enter an Invoice Received Date which is prior to the Date(s) of Service. If a user is editing a previously-entered Invoice, where both types of dates have already been entered, they will not be allowed to edit either the Date of Service, or the Invoice Received Date, if they try to enter a new value which results in the Invoice Received Date being prior to the Date(s) of Service. The changes made by this patch are described below:

1\. The system will perform a validity check that cannot be made until both dates are entered. Either date may be entered first.

2\. The date-check code will determine whether the Claim Received Date and the Date of Service have both been entered. If the second date has not yet been entered, the program will take no further action in the current date field.

3\. If both dates have been entered, and if the Claim Received Date is PRIOR TO the Date of Service, the date entered in the current date field will not be accepted.

4\. Software cannot determine whether an invalid pair of dates is the result of a user entry error, or of a claim being submitted with invalid dates. The system will notify the user when an error has been detected and reject the date just entered. The user will then determine what action to take (i.e. re-enter the current date, go back and modify the first date entered, or exit the claim.)

The application will not allow the entry of both a Claim Received Date and a Date of Service, where the Claim Received Date is prior to the Date of Service. Since both dates are required before a claim can be accepted and sent to Central Fee at the Austin Information Technology Center (AITC), this will prevent a claim from being submitted for payment with a Claim Received Date that is prior to the Date of Service.

### Issue Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no New Service Requests (NSRs) or Remedy Tickets associated with this patch

### From: FB*3.5*146 Release Notes

## New Features and Fixed Previous Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement encompasses modifications to Fee Basis, Registration, and Integrated Billing to facilitate the registration and authorization of newborns. Table 1 lists all of the New Features added by this enhancement.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th>Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">FB*3.5*146</td>
</tr>
<tr class="even">
<td>1</td>
<td>Removes restrictions preventing the entry of a patient less than one year of age.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Internal checks use the date of birth instead of age</td>
</tr>
<tr class="even">
<td>3</td>
<td>Adds reject code C166 to deny claims exceeding the 7 day authorization</td>
</tr>
<tr class="odd">
<td>4</td>
<td><p>"NON-VA FOR FEMALE VET+NEWBORN 17.38" was added to the</p>
<p>VA ADMITTING REGULATION file (#43.4). This new Admitting Regulation is available when editing the 7078.</p></td>
</tr>
<tr class="even">
<td>5</td>
<td>Fee Authorization dates associated with Newborns have checks in place to not allow Authorization dates that fall outside the accepted range of Newborn Authorization. The range is DOB to DOB+7; the system will warn the user and not accept an Authorization date that falls outside the appropriate range for a Newborn.</td>
</tr>
<tr class="odd">
<td colspan="2">DG*5.3*867</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>A new Patient Type of NEWBORN OF VET has been added to the</p>
<p>TYPE OF PATIENT file (#391). This new selection will be available on Registration screen &lt;7&gt;.</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>A sponsor is required for all Newborns determined by having the DOB less than one (1) year from the present date. An inconsistency check has been added to check the presence of a sponsor. If an inconsistency is found, the inconsistency check will prompt the user to return to Screen &lt;15&gt; in registration to enter a Sponsor.</td>
</tr>
<tr class="even">
<td>8</td>
<td><p>All Sponsors for Newborns must be listed as eligible for care. An inconsistency check will check the status of the Sponsors Eligibility. The check will trigger if the Sponsor has no Eligibility status. The inconsistency check will return error <strong>313 Newborn Requires Sponsor</strong> (if you try to enter a newborn without a sponsor, you will get a 313 check message at the end of the registration) or error <strong>314 Newborn Needs Eligible Sponsor</strong> (adds ability to issue a standard authorization for pre-authorized medical care for newborn coverage through midnight of the 7th day past date of birth).</p>
<p>All other statuses (i.e. Pending Verification, Verified, and Pending Re-verification) are acceptable.</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td><p>The following default values were added when entering a Newborn:</p>
<p>PATIENT DATA, SCREEN &lt;2&gt; – "Marital" field is defaulted to "NEVER MARRIED."</p>
<p>APPLICANT/SPOUSE EMPLOYMENT DATA, SCREEN &lt;4&gt; - "Status" field is defaulted to "NOT EMPLOYED."</p>
<p>FAMILY DEMOGRAPHIC DATA, SCREEN &lt;8&gt; - "Married Last Year" field is defaulted to "NO."</p></td>
</tr>
<tr class="even">
<td>10</td>
<td>When a Veteran Mother of a Sponsored Newborn is reviewed in the Registration screens, Screen &lt;15&gt; will display the Newborn(s), with the additional header of "Sponsored Newborn".</td>
</tr>
<tr class="odd">
<td colspan="2">IB*2.0*499</td>
</tr>
<tr class="even">
<td>11</td>
<td>The FAMILY PREFIX "NB Newborn of Vet" has been added to the Help text in the Family Prefix field (#.03) in the SPONSOR RELATIONSHIP file (#355.81).</td>
</tr>
</tbody>
</table>

## Operation Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although sites are required to use FBCS to process claims, Newborn claim can ONLY be processed by VistA at this time. FBCS can NOT be used to process Newborn claims. Refer to the instructions in the Care for Newborn of Women Veterans located at <http://nonvacare.hac.med.va.gov/policy-programs/procedure-guides.asp> for processing Newborn claims.

## Security Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement involves no new security changes.

## Database Impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch bundle required the following modifications to Central Fee's system:

- 29 defined as the new Purpose of Visit (POV) Code for Inpatient Newborn Care
- 66 defined as the new POV Code for Outpatient Newborn Care
- Acceptance of short term authorization for Newborn patients with POV codes 29 and 66
- The inclusion of the new POV codes for Newborn Care on the following Central Fee reports:
  - Report 60002 -- Fee Basis Payment Analysis
  - Report 70001 -- Cost Analysis of Fee Basis Vouchers by Veterans and by Average Monthly Cost Range
  - Report 70007 -- Fee Veterans -- Costs By Facility, State, County, and POV
  - Report 70008 -- Fee Veterans -- Costs By VISN, Nation, and POV

## Infrastructure Impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhancement involves no new hardware or the interfacing of any hardware.

## Other Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no other dependencies for this enhancement.

## Documentation Updated/Created

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch bundle updated the Fee Basis User Manual (fb3_5_um) and PIMS ADT Registration User Manual (dg_5_3_reg_um). Additionally, the document Care for Newborn of Woman Veterans, located at <http://nonvacare.hac.med.va.gov/policy-programs/procedure-guides.asp>, has been created.

## Existing Issues and Workarounds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA MUST BE USED for this process. DO NOT use FBCS. Until FBCS can process Newborn claims, follow your local facility's VistA procedures. Refer to the instructions in the Care for Newborn Women of Veterans located at <http://nonvacare.hac.med.va.gov/policy-programs/procedure-guides.asp> for processing Newborn claims.

### From: FB*3.5*131 Release Notes

## Description of Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch FB\*3.5\*131 is the first of a two-phased release of the VistA Fee and IFCAP Automation Enhancement (aka Duplicate Payments) project.

This patch does not provide any new user functionality. Patch FB\*3.5\*131 sets the foundation for the rollout of the second phase of the Duplicate Payments project by enabling Central Fee to start sending new message types to VistA. It provides an address for Central Fee messages. Central Fee can use this address to send new messages to all VA facilities.

These new message types are ignored by VistA until the release of the second phase of the Duplicate Payments project. Patch FB\*3.5\*131 (increment one) must be released and installed at all VistA sites prior to Central Fee making their production changes for this project.

> **NOTE:** Central Fee is a system at the Austin Information Technology Center (AITC) that processes the payments transmitted by VistA Fee Basis.

### VistA Fee and IFCAP Automation Enhancement—[20110212](http://vista.med.va.gov/nsrd/Tab_GeneralInfoView.asp?RequestID=20110212)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following descriptive text is from the New Service Request Database (NSRD) for Request ID: [20110212](http://vista.med.va.gov/nsrd/Tab_GeneralInfoView.asp?RequestID=20110212).

New Capabilities

*"Automation of the finalization process to interface with the creation of an automated 994 code sheet in IFCAP."*Desired Change

*"This request was submitted by the Chief Business Office (CBO), Purchased Care Program Office. They are requesting enhancements to the VistA Fee Basis application in support of preventing duplicate payments which is occurring because there is currently no interface between the VistA Fee Application Batch Software, Central Fee and Integrated Funds Control, Accounting, and Procurement (IFCAP)/Financial Management System (FMS). The proposed enhancement seeks modifications to various modules of VA's VistA software application to include Fee Basis and IFCAP. Affected functions include Fee Batch, IFCAP, claims processing, and payments. Nothing has changed in the business environment per se, this has always been a manual process, but this needs to be automated in order to mitigate risks and to reduce the number of duplicate payments."*

## Process Incoming Payment Messages from Central Fee 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The server option FBAA BATCH SERVER processes incoming Payment Batch Result messages from Central Fee.  The Payment Batch Result message is a response to a Payment Batch message.  The result message provides a count of accepted line items and identifies any line items that were rejected by Central Fee edit checks.

## Process Incoming Post Voucher Reject Messages from Central Fee

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The server option FBAA REJECT SERVER processes incoming Post Voucher Reject messages from Central Fee.  The Post Voucher Reject message identifies payment line items that have been dropped from Central Fee after receipt of the Voucher Batch message for that line item.

## Process Incoming Voucher Batch Acknowledgement Messages from Central Fee

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The server option FBAA VOUCHER SERVER processes incoming Voucher Batch Acknowledgement messages from Central Fee.  The Voucher Batch Acknowledgement message contains the Central Fee application acknowledgement for a Voucher Batch message.

## Process Payment Batch Result Messages from Central Fee

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routine FBSVBR is called by the exported FBAA BATCH SERVER option to process Payment Batch Result messages from Central Fee.

## Process Post Voucher Reject Messages from Central Fee

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routine FBSVPR is called by the exported FBAA REJECT SERVER option to process Post Voucher Reject messages from Central Fee.

## Process Voucher Batch Acknowledgement Messages from Central Fee

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The routine FBSVVA is called by the exported FBAA VOUCHER SERVER option to process Voucher Batch Acknowledgement messages from Central Fee.

### From: FB*3.5*158 Release Notes

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the new features and functions added to Fee Basis with the FB\*3.5\*158 release.

- Create authorization number and service line number fields in the VistA Fee database.

## Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the enhancements and modifications to Fee Basis with the FB\*3.5\*158 release.

- Expand batch number from 5 to 7 digits.
- Turn off Vitria feed of HL7 files.
- Screens modified to display and handle selection of CARCs/RARCs in accordance with CORE rule 360.
- Processing modified to add fields to the B3, B5 and B9 flat files.
- Processing modified to allow a maximum of five CARC/RARC combinations per claim line.
- Processing modified to restrict RARC selection by CARC where such restrictions exist.
- Processing modified to limit to two the number of RARCs per CARC for each claim line.
- Processing modified to restrict CARC selection to the same business scenario at the claim or line level.
- Processing modified to restrict CAGC selection when a CARC is selected.
- Processing modified to allow RARCs to be selected when no CARC is entered.
- Processing modified to require that CARCs and RARCs be active based on date of adjudication.
- Purge process modified to delete batch number data that is more than 7 years old and to send a MailMan notification when the purge process is run.

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc491353142" class="anchor"></span>Before installation of this patch all batches need to be finalized and closed out, so coordination within the sites and your OIT/ESL teams may be required. This will be needed to avoid having batches being rejected from Central Fee after the patch installation. 

After installation of this patch the Vitria transmissions will need to be shut off. The Vitria transmissions can be shut off by deleting the option, FB FPPS TRANSMIT, from Taskman.

### From: FB*3.5*135 Release Notes

## Civil Hospital and Medical claims Invoice Display option outputs were modified.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Routines FBAAPIN and FBCHVH have been modified to display the Line Item Rendering Provider, Line Item NPI and Line Item Taxonomy codes when available.

## Potential Cost Recovery report has been modified to allow users to exclude setected insurance types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> FBPCR has been modified to include an optional prompt so that users may exclude selected Insurance types (Type of Plan) from the Potential Cost Recovery report \[FB PCR\] option. FBPCR4 was modified to exclude patients that have only the selected insurance type(s) and no other third party insurance. The paid claims for these patients will not display or print on the report.

## A new Unique Claim Identifier (UCID) will be generated for all Civil Hospital and Medical claims manually entered in VistA Fee Basis.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The UCID will be used by the Purchased Care business office in systems downstream from VistA (Central Fee, VHA Support Service Center, etc) to enable the VA to recreate claims as they were submitted by a vendor. The UCID will be comprised of the following:

> 5 digit Station#, left justified, zero filled

> 1 digit Source (1=FB, 2=FBCS, 3=VAPM)

> 1 digit Initiation Type (S=scanned, E=EDI, M=Manual)

> 1 digit Claim Type (I=Institutional, P=Professional, D=Dental, N=Non Standard) 4 digit Calendar year

> '-' to separate the year and sequence# 15 digit Sequence number

> Note: the "4 digit year-Seq#" will be known as the Claim Number. For "E" (EDI) Claims, VistA Fee Basis forces the Sequence number portion of the Claim Number to be the FPPS Claim ID.

> Two APIs have been created for Fee and COTS applications to set the UCID value when filing data to Fee Basis Payment (#162) or Fee Basis Invoice (#162.5) files. These APIs are:

> \$\$PAYUCID^FBUTL135(VET,VEN,TDIEN,SVCIEN,STN,SRCE,INITTYP,CLTYP,CLNUM)

> Inputs: (all inputs are required) VET = veteran DFN VEN = Vendor IEN

> TDIEN = Treatment Date IEN SVCIEN = Service Provided IEN STN = Station

> SRCE = Source (1=FB, 2=FBCS, 3=VAPM)

> INITTYP = Initiation Type (S=scanned, E=EDI, M=Manual)

> CLTYP = Claim Type (P=Professional, D=Dental, N=Non Standard) CLNUM = Claim Number - in format YYYY-nnnn

> Output: "-1^" with an error message or

> Populates the Unique Claim ID field (#81) in file FEE BASIS PAYMENT (#162) (Outpatient) and, Returns the Unique Claim ID

> 2 Fee Basis FB\*3.5\*135 Release Notes December 2012

> \$\$INVUCID^FBUTL135(INVIEN,STN,SRCE,INITTYP,CLNUM)

> Inputs: (all inputs are required) INVIEN = Invoice IEN STN = Station

> SRCE = Source (1=FB, 2=FBCS, 3=VAPM)

> INITTYP = Initiation Type (S=scanned, E=EDI, M=Manual) CLNUM = Claim Number - in YYYY-nnnn format

> Output: "-1^" with an error message or

> Populates the Unique Claim ID field (#85) in file FEE BASIS INVOICE (#162.5) (Inpatient)

and Returns the Unique Claim ID

> In order to create the UCID, the following Fee components were created or modified: Five new APIs were created:

> \$\$ENTINPAT^FBUTL136(FBSTA,FBSRC,FBINT,FBCLT,FBCLAIMS,FBVEND)

> This API is used by Input Template "FBCH ENTER PAYMENT" Inputs: FBSTA = Station

> FBSRC = Source FBINT = Initiation Type FBCLT = Claim Type

> FBCLAIMS = Claim Number FBVEND = Vendor IEN

> Output: Returns a Unique Claim ID that is used by Fileman to populate the Unique Claim ID field (#85) in file

> FEE BASIS INVOICE (#162.5) (Inpatient)

> EDINPAT^FBUTL136(FBXSTR,FBI)

> This API is used by Input Template "FBCH EDIT PAYMENT" Inputs: FBXSTR = FPPS value entered by user for FPPS

> FBI = IEN of Invoice record

> Output: UCID is saved in file 162.5 via Fileman

> \$\$ENTROUTP^FBUTL136(DFN,FBV,FBAAVID,FBCLAIMS)

> This API is used by routine FBAACO Inputs: DFN = Patient ID

> FBV = Vendor IEN

> FBAAVID = Vendor Invoice Date FBCLAIMS = FPPS claim id

Output: UCID that is save in file 162

> EDITOUTP^FBUTL136(FBXSTR,FBDA)

> This API is used by routine FBUTL5.

> Inputs: FBXSTR = FPPS CLAIM ID entered by user

> FBDA = DA variable containing SERVICE PROVIDED, INITIAL TREATMENT DATE, VENDOR, PATIENT

> Output: UCID that is saved in file 162

> December 2012 Fee Basis FB\*3.5\*135 Release Notes 3

> \$\$UCLAIMNO^FBUTIL135(FBSTA,FBSRC,FBINT,FBCLT,FBCLAIMS)

> This API is used by all the other API's Inputs: All inputs are optional.

> FBSTA = Station - Default is the station ID returned by routine STATION^FBAAUTL FBSRC = Source - Default is "1" - FB

> FBINT = Initiation Type - Default is "M" - Manual FBCLT = Claim Type - Default is "N" - Non Standard FBCLAIMS = Claim Number - in YYYY-nnnn format

> Default is \<Current Year\>-\<Next Sequential Number from file FEE BASIS SITE PARAMETERS (#161.4), field UNIQUE CLAIM IDENTIFIER SEQ (#39)

> Output: Returns a Unique Claim ID

> Created field for Unique Claim Identifier Sequence in the FEE BASIS SITE PARAMETERS (#161.4) file.

> For Civil Hospital claims: added field for Unique Claim Identifier to the FEE BASIS INVOICE (#162.5), modified routine FBCHEP and input template \[FBCH ENTER PAYMENT\] (file 162.5) to call new API: ENTINPAT^FBUTL136, and \[FBCH EDIT PAYMENT\] (file 162.5) to call new API: EDINPAT^FBUTL136 prompt for the Claim Number.

> For Medical claims: added field for Unique Claim Identifier to the FEE BASIS PAYMENT (#162) file, modified routine FBAACO to prompt for CLAIM NUMBER and a claim type by calling new API: ENTROUTP^FBUTL136, modified routine FBAACO2 and FBUTL5 to prompt for Claim Number and a claim type by calling new API: EDITOUTP^FBUTL136.

> Three options were added to verify Unique Claim Identifier (UCID) entries for testing. Unique Claim Identifier Utility Menu \[FB UCID UTILITY MENU\] has been created to display information about the Unique Claim Identifier field for entries in files FEE BASIS INVOICE (#162.5),FEE BASIS PAYMENT (#162). This menu option is not available on any existing FB menus, but could be added to a secondary menu. The new menu contains the Fee Basis Unique Claim Identifier Display \[FB UCID DISPLAY\] option and the FB OUTPATIENT UCID REPORT \[FB UCID PAYMENT RPT\]

> option.

## An automated process to copy valid Fee Basis Vendor and 5010 Providers within a paid claim to the IB NON/OTHER VA PROVIDER (#355.93) file was added (For Future Use).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following changes represent partial automation of Fee vendors and 5010 providers from FB to IB. These enhancements were tested at the test sites and will be rolled out nationally, but not "turned on" (no post install). Future patches will build upon the baseline functionality established for this item in the patch.

> Paid inpatient and outpatient claims that are potentially cost recoverable from Integrated Billing (IB) will now have an automated process (For Future Use) available to copy valid Fee Basis Vendor and 5010 Providers within a paid claim to the IB NON/OTHER VA PROVIDER (#355.93) file. Routine FBPAID was modified and new routines FBPAID3 and FBPAID3A were created to capture the paid

> 4 Fee Basis FB\*3.5\*135 Release Notes December 2012

> claims into the new file FEE BASIS PAID TO IB (#161.9) during the nightly mailman processing of the PAID message from Central Fee.

> A new field ALLOW FB PAID TO IB (#40) was created in the FEE BASIS SITE PARAMETERS (#161.4) file (For Future Use), and included in the Input Template \[FBAA SITE PARAMETERS\] Fee Basis Supervisor to allow/disallow the automated process. The interface will not run unless this field is set to YES (allow).

> A new queued option (For Future Use) Fee Basis Payment to IB \[FB PAID TO IB\] calling new routine FBPAID3 will read through the paid entries saved to the FEE BASIS PAID TO IB (#161.9) file and determine claims that are potential cost recovery claims using the same business rules as the existing Potential Cost Recovery Report. Vendor and 5010 providers for entries that pass the potential cost recovery rules will be sent to the new IB API \$\$EPFBAPI^IBCEP8C1, introduced in IB\*2.0\*476, for additional IB checks and to save to file 355.93. Data will be captured for reporting on entries filed to IB and those that failed to file for a variety of reasons (invalid provider name format, etc). ICR 5806: FB PROVIDER TO IB AUTOMATION was approved for this call.

> A new option Provider to IB Report \[FB PROVIDER TO IB\] was created (For Future Use) which calls the new routine FBPAID3B to display data from file 161.9 for entries that were filed to IB and those that failed to file. The data in file 161.9 will be retained for six months after which it will be purged by the nightly process Fee Basis Payment to IB \[FB PAID TO IB\].

> December 2012 Fee Basis FB\*3.5\*135 Release Notes 5

### From: FB*3.5*163 Release Notes

## Features and Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch will improve and automate the transfer of data from VistA Fee Basis to Integrated Billing. The patch makes the following changes and enhancements:

1.  System to automatically populate information entered in VistA Fee Basis authorizations into VistA IB software to accelerate claims for Non-VA health care services.
2.  Assist the VAMCs in obtaining timely precertification from third party payers before care is rendered.
1.  Enhancements to the Potential Cost Recovery Report removed Service Connected decision and added additional display fields.

## Upgrades

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No upgrade information applies.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents (located at the VA Software Document Library at: <http://www.va.gov/vdl/> apply to this release:

- Installation Guide for FB\*3.5\*163
- Fee Basis 3.5 Technical Manual
- CPAC/FB User Guide
