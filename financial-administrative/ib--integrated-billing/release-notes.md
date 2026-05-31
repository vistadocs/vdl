---
title: IB*2*516 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*516
group_key: IB:IB:2
file_numbers:
- '1.01'
- '1.02'
- '1.03'
- '1.04'
- '1.05'
- '2'
- '2.312'
- '2.3226'
- '4.07'
- '4.11'
- '4.12'
- '4.13'
- '11.04'
- '19'
- '20'
- '21'
- '36'
- '51'
- '53'
- '54'
- '81'
- '261'
- '350.9'
- '350.929'
- '355.3'
- '355.33'
- '355.93'
- '364.5'
- '364.6'
- '364.7'
- '365'
- '365.03'
- '365.26'
- '371'
- '372'
- '373'
- '399'
- '399.0304'
- '399.040'
- '399.041'
- '399.047'
- '471'
- '472'
- '473'
security_keys:
- PROVIDER
menu_options: 0
description: Electronic Data Interchange (EDI)New Standards and Operating Rules –VHA Provider-side Technical Compliance
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 11169
section_count: 19
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: null
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_0_p516_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_0_p516_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=45
audit_applied: '2026-05-31'
master_source: IB*2*516 Release Notes
master_pub_date: 'null'
consolidated_from: 20 versions
prior_versions:
- IB*2*452 Release Notes
- IB*2*458 Release Notes
- IB*2*476 Release Notes
- IB*2*488 Release Notes
- IB*2*494 Release Notes
- IB*2*499 Release Notes
- IB*2*511 Release Notes
- IB*2*519 Release Notes
- IB*2*521 Release Notes
- IB*2*525 Release Notes
- IB*2*528 Release Notes
- IB*2*534 Release Notes
- IB*2*550 Release Notes
- IB*2*614 Release Notes
- IB*2*653 Release Notes
- IB*2*685 Release Notes
- IB*2*688 Release Notes
- IB*2*697 Release Notes
- IB*2*701 Release Notes
consolidated_title: release notes
---

![](ib-2-516-release-notes/001.png)

Electronic Data Interchange (EDI)New Standards and Operating Rules –VHA Provider-side Technical Compliance RequirementsVA118-1001-1018

####### eBilling Build 3

####### Integrated Billing (IB)

####### RELEASE NOTES/ Installation Guide/ Rollback Plan

IB\*2\*516April 2015Table of Contents

*(This page included for two-sided copying.)*<span id="_Toc354988659" class="anchor"></span>

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Documentation and Distribution](#documentation-and-distribution)
- [Patch Description and Installation Instructions](#patch-description-and-installation-instructions)
  - [Patch Description](#patch-description)
  - [Pre/Post Installation Overview](#prepost-installation-overview)
  - [Installation Instructions](#installation-instructions)
- [Backout and Rollback Procedures](#backout-and-rollback-procedures)
  - [Overview of Backout and Rollback Procedures](#overview-of-backout-and-rollback-procedures)
  - [Backout Procedure](#backout-procedure)
  - [Rollback Procedure](#rollback-procedure)
- [Enhancements](#enhancements)
  - [System Feature: Enter/Edit Billing Information](#system-feature-enteredit-billing-information)
    - [Enter/Edit Billing Information- Revenue Codes \<100](#enteredit-billing-information-revenue-codes-100)
    - [Enter/Edit Billing Information - Line Level NDC Codes to Non-Prescription Claims - Professional](#enteredit-billing-information-line-level-ndc-codes-to-non-prescription-claims-professional)
    - [The IB System provides the ability for users to add a line level 5-4-2 format National Drug Code to a non-prescription procedure when creating a professional claim.](#the-ib-system-provides-the-ability-for-users-to-add-a-line-level-5-4-2-format-national-drug-code-to-a-non-prescription-procedure-when-creating-a-professional-claim)
    - [Enter/Edit Billing Information- Line Level NDC Codes to Non-Prescription Claims – Institutional](#enteredit-billing-information-line-level-ndc-codes-to-non-prescription-claims-institutional)
    - [Enter/Edit Billing Information- Line Level Description – 99 Procedure Codes – Professional](#enteredit-billing-information-line-level-description-99-procedure-codes-professional)
    - [Enter/Edit Billing Information - Line Level Description - 99 Procedure Codes – Institutional](#enteredit-billing-information-line-level-description-99-procedure-codes-institutional)
    - [Enter/Edit Billing Information - Line Level Description - NOC Procedure Codes – Professional](#enteredit-billing-information-line-level-description-noc-procedure-codes-professional)
    - [Enter/Edit Billing Information - Line Level Description - NOC Procedure Codes – Institutional](#enteredit-billing-information-line-level-description-noc-procedure-codes-institutional)
    - [Enter/Edit Billing Information - Fatal Error - Non-billable Providers – Professional](#enteredit-billing-information-fatal-error-non-billable-providers-professional)
    - [Enter/Edit Billing Information - Fatal Error - Non-billable Providers – Institutional](#enteredit-billing-information-fatal-error-non-billable-providers-institutional)
    - [Enter/Edit Billing Information - Screen – Non-billable Provider – Institutional](#enteredit-billing-information-screen-non-billable-provider-institutional)
    - [Enter/Edit Billing Information - Screen – Non-billable Provider – Professional](#enteredit-billing-information-screen-non-billable-provider-professional)
    - [Enter/Edit Billing Information - Fatal Error – Missing non-VA Lab or Facility NPI – Professional](#enteredit-billing-information-fatal-error-missing-non-va-lab-or-facility-npi-professional)
    - [Enter/Edit Billing Information - Fatal Error – Missing non-VA Lab or Facility NPI – Institutional](#enteredit-billing-information-fatal-error-missing-non-va-lab-or-facility-npi-institutional)
    - [Enter/Edit Billing Information - Warning – Missing Lab or Facility Taxonomy Code – Institutional](#enteredit-billing-information-warning-missing-lab-or-facility-taxonomy-code-institutional)
    - [Enter/Edit Billing Information - Warning – Missing Lab or Facility Taxonomy Code – Professional](#enteredit-billing-information-warning-missing-lab-or-facility-taxonomy-code-professional)
    - [Enter/Edit Billing Information - Print – TRICARE-specific Pay-to Provider – UB04 – TRICARE REIMB.](#enteredit-billing-information-print-tricare-specific-pay-to-provider-ub04-tricare-reimb)
    - [Enter/Edit Billing Information - Print – TRICARE-specific Pay-to Provider – UB04 – UB04 – TRICARE](#enteredit-billing-information-print-tricare-specific-pay-to-provider-ub04-ub04-tricare)
    - [Enter/Edit Billing Information - Print – TRICARE-specific Pay-to Provider – CMS 1500 – TRICARE REIMB.](#enteredit-billing-information-print-tricare-specific-pay-to-provider-cms-1500-tricare-reimb)
    - [Enter/Edit Billing Information - Print – TRICARE-specific Pay-to Provider – CMS 1500 – TRICARE](#enteredit-billing-information-print-tricare-specific-pay-to-provider-cms-1500-tricare)
    - [Enter/Edit Billing Information - Re-sequence Diagnoses/Maintain Pointers](#enteredit-billing-information-re-sequence-diagnosesmaintain-pointers)
    - [Enter/Edit Billing Information - Value Code Help](#enteredit-billing-information-value-code-help)
    - [Enter/Edit Billing Information - Value Code – External Code Lookup](#enteredit-billing-information-value-code-external-code-lookup)
    - [Enter/Edit Billing Information - Occurrence Code Help](#enteredit-billing-information-occurrence-code-help)
    - [Enter/Edit Billing Information - Occurrence Code – External Code Lookup](#enteredit-billing-information-occurrence-code-external-code-lookup)
    - [Enter/Edit Billing Information - Condition Code Help](#enteredit-billing-information-condition-code-help)
    - [Enter/Edit Billing Information - Condition Code – External Code Lookup](#enteredit-billing-information-condition-code-external-code-lookup)
    - [Enter/Edit Billing Information - One-Time HPID – Professional](#enteredit-billing-information-one-time-hpid-professional)
    - [Enter/Edit Billing Information - One-Time HPID – Institutional](#enteredit-billing-information-one-time-hpid-institutional)
    - [Enter/Edit Billing Information - Line Level NDC Code Units to Non-Prescription Claims – Professional](#enteredit-billing-information-line-level-ndc-code-units-to-non-prescription-claims-professional)
    - [Enter/Edit Billing Information - Line Level NDC Code Units to Non-Prescription Claims – Institutional](#enteredit-billing-information-line-level-ndc-code-units-to-non-prescription-claims-institutional)
  - [System Feature: Insurance Company Editor](#system-feature-insurance-company-editor)
    - [Insurance Company Editor - Federal Employee Plan – Help Description](#insurance-company-editor-federal-employee-plan-help-description)
  - [System Feature: Billing Reports](#system-feature-billing-reports)
    - [Billing Reports - Sort - Re-generate Unbilled Amounts Report – Division](#billing-reports-sort-re-generate-unbilled-amounts-report-division)
    - [Billing Reports - Display - Re-generate Unbilled Amounts Report – Division](#billing-reports-display-re-generate-unbilled-amounts-report-division)
    - [Billing Reports - Print - Re-generate Unbilled Amounts Report – Division](#billing-reports-print-re-generate-unbilled-amounts-report-division)
    - [Billing Reports - Display new HIPAA Compliant Fields on IB Reports](#billing-reports-display-new-hipaa-compliant-fields-on-ib-reports)
  - [System Feature: Third Party Joint Inquiry](#system-feature-third-party-joint-inquiry)
    - [Third Party Joint Inquiry - TPJI Visual Indicator – Institutional](#third-party-joint-inquiry-tpji-visual-indicator-institutional)
    - [Third Party Joint Inquiry - TPJI Visual Indicator – Professional](#third-party-joint-inquiry-tpji-visual-indicator-professional)
    - [Third Party Joint Inquiry - Co-Payment Amount – TPJI](#third-party-joint-inquiry-co-payment-amount-tpji)
  - [System Feature: COB Management Worklist](#system-feature-cob-management-worklist)
    - [COB Management Worklist - Sort – COB Management Worklist – Division](#cob-management-worklist-sort-cob-management-worklist-division)
    - [COB Management Worklist - Display – COB Management Worklist – Division](#cob-management-worklist-display-cob-management-worklist-division)
    - [COB Management Worklist - Print – COB Management Worklist – Division](#cob-management-worklist-print-cob-management-worklist-division)
  - [System Feature: Health Care Claim Transactions (837)](#system-feature-health-care-claim-transactions-837)
    - [Health Care Claim Transactions (837) - Transmit HPID – Destination Payer – Institutional](#health-care-claim-transactions-837-transmit-hpid-destination-payer-institutional)
    - [Health Care Claim Transactions (837) - Transmit HPID – Destination Payer – Professional](#health-care-claim-transactions-837-transmit-hpid-destination-payer-professional)
    - [Health Care Claim Transactions (837) - Transmit HPID – Other Payer(s) – Institutional](#health-care-claim-transactions-837-transmit-hpid-other-payers-institutional)
    - [Health Care Claim Transactions (837) - Transmit HPID – Other Payer(s) – Professional](#health-care-claim-transactions-837-transmit-hpid-other-payers-professional)
    - [Health Care Claim Transactions (837) - Transmit Sole-Proprietorship NPI – Institutional](#health-care-claim-transactions-837-transmit-sole-proprietorship-npi-institutional)
    - [Health Care Claim Transactions (837) - Transmit Sole-Proprietorship NPI – Professional](#health-care-claim-transactions-837-transmit-sole-proprietorship-npi-professional)
    - [Health Care Claim Transactions (837) - Transmit TRICARE-specific Pay-to Provider – Institutional – TRICARE REIMB.](#health-care-claim-transactions-837-transmit-tricare-specific-pay-to-provider-institutional-tricare-reimb)
    - [Health Care Claim Transactions (837) - Transmit TRICARE-specific Pay-to Provider – Institutional – TRICARE](#health-care-claim-transactions-837-transmit-tricare-specific-pay-to-provider-institutional-tricare)
    - [Health Care Claim Transactions (837) - Transmit TRICARE-specific Pay-to Provider – Professional – TRICARE REIMB.](#health-care-claim-transactions-837-transmit-tricare-specific-pay-to-provider-professional-tricare-reimb)
    - [Health Care Claim Transactions (837) - Transmit TRICARE-specific Pay-to Provider – Professional – TRICARE](#health-care-claim-transactions-837-transmit-tricare-specific-pay-to-provider-professional-tricare)
    - [Health Care Claim Transactions (837) - Transmit NDC Code – non-RX – Institutional](#health-care-claim-transactions-837-transmit-ndc-code-non-rx-institutional)
    - [Health Care Claim Transactions (837) - Transmit NDC Code – non-RX – Professional](#health-care-claim-transactions-837-transmit-ndc-code-non-rx-professional)
    - [Health Care Claim Transactions (837) - Transmit NOC Procedures - Free Text Description – Institutional](#health-care-claim-transactions-837-transmit-noc-procedures-free-text-description-institutional)
    - [Health Care Claim Transactions (837) - Transmit NOC Procedures – Free Text Description – Professional](#health-care-claim-transactions-837-transmit-noc-procedures-free-text-description-professional)
    - [Health Care Claim Transactions (837) - Transmit NDC Code Units– non-RX – Institutional](#health-care-claim-transactions-837-transmit-ndc-code-units-non-rx-institutional)
    - [Health Care Claim Transactions (837) - Transmit NDC Code Units – non-RX – Professional](#health-care-claim-transactions-837-transmit-ndc-code-units-non-rx-professional)
    - [Health Care Claim Transactions (837) - Transmit Maximum 12 Procedures – Inpatient/Institutional](#health-care-claim-transactions-837-transmit-maximum-12-procedures-inpatientinstitutional)
  - [System Feature: Copy and Cancel a Bill (CLON)/Correct Rejected/Denied Bill (CRD)](#system-feature-copy-and-cancel-a-bill-cloncorrect-rejecteddenied-bill-crd)
    - [Copy and Cancel a Bill (CLON)/Correct Rejected/Denied Bill (CRD) - CRD - Prevent Correction of Secondary Claim](#copy-and-cancel-a-bill-cloncorrect-rejecteddenied-bill-crd-crd-prevent-correction-of-secondary-claim)
    - [Copy and Cancel a Bill (CLON)/Correct Rejected/Denied Bill (CRD) - CRD - Prevent Correction of Tertiary Claim](#copy-and-cancel-a-bill-cloncorrect-rejecteddenied-bill-crd-crd-prevent-correction-of-tertiary-claim)
    - [Copy and Cancel a Bill (CLON)/Correct Rejected/Denied Bill (CRD) - CLON – Copy Secondary/Tertiary Claim Data to New Secondary/Tertiary Claim](#copy-and-cancel-a-bill-cloncorrect-rejecteddenied-bill-crd-clon-copy-secondarytertiary-claim-data-to-new-secondarytertiary-claim)
    - [Copy and Cancel a Bill (CLON)/Correct Rejected/Denied Bill (CRD) - CRD – Copy Primary Claim Data to New Primary Claim](#copy-and-cancel-a-bill-cloncorrect-rejecteddenied-bill-crd-crd-copy-primary-claim-data-to-new-primary-claim)
    - [Copy and Cancel a Bill (CLON)/Correct Rejected/Denied Bill (CRD) - CRD – Prevent Correction of Claim in MRA Request Status](#copy-and-cancel-a-bill-cloncorrect-rejecteddenied-bill-crd-crd-prevent-correction-of-claim-in-mra-request-status)
  - [System Feature: Provider ID Maintenance](#system-feature-provider-id-maintenance)
    - [Provider ID Maintenance - Sole-Proprietorship Designation - non-VA Facility](#provider-id-maintenance-sole-proprietorship-designation-non-va-facility)
    - [Provider ID Maintenance - Link non-VA Facility to Sole-Proprietor](#provider-id-maintenance-link-non-va-facility-to-sole-proprietor)
    - [Provider ID Maintenance - Sole-Proprietorship non-VA Facility – NPI](#provider-id-maintenance-sole-proprietorship-non-va-facility-npi)
  - [System Feature: MCCR Site Parameter Display/Edit](#system-feature-mccr-site-parameter-displayedit)
    - [MCCR Site Parameter Display/Edit - Default TRICARE Pay-to Provider](#mccr-site-parameter-displayedit-default-tricare-pay-to-provider)
    - [MCCR Site Parameter Display/Edit - Default TRICARE Pay-to Provider Associations](#mccr-site-parameter-displayedit-default-tricare-pay-to-provider-associations)
    - [MCCR Site Parameter Display/Edit - Additional TRICARE Pay-to Providers](#mccr-site-parameter-displayedit-additional-tricare-pay-to-providers)
    - [MCCR Site Parameter Display/Edit - Associate Division(s) with TRICARE Pay-to Provider](#mccr-site-parameter-displayedit-associate-divisions-with-tricare-pay-to-provider)
    - [MCCR Site Parameter Display/Edit - Edit a TRICARE Pay-to Provider](#mccr-site-parameter-displayedit-edit-a-tricare-pay-to-provider)
    - [MCCR Site Parameter Display/Edit - Delete a TRICARE Pay-to Provider](#mccr-site-parameter-displayedit-delete-a-tricare-pay-to-provider)
    - [MCCR Site Parameter Display/Edit - Re-associate Divisions - Delete TRICARE Pay-to Provider](#mccr-site-parameter-displayedit-re-associate-divisions-delete-tricare-pay-to-provider)
    - [MCCR Site Parameter Display/Edit - Re-associate Divisions - TRICARE Pay-to Provider Security Key](#mccr-site-parameter-displayedit-re-associate-divisions-tricare-pay-to-provider-security-key)
    - [MCCR Site Parameter Display/Edit - Re-associate Divisions - Pay-to Provider Security Key](#mccr-site-parameter-displayedit-re-associate-divisions-pay-to-provider-security-key)
  - [System Feature: View Cancelled Claim](#system-feature-view-cancelled-claim)
    - [View Cancelled Claim - View Cancelled Claim](#view-cancelled-claim-view-cancelled-claim)
  - [System Feature: Miscellaneous Existing Requirements](#system-feature-miscellaneous-existing-requirements)
    - [Miscellaneous Existing Requirements - Correct - FEAT604 Transmit Property and Casualty Claim Number](#miscellaneous-existing-requirements-correct-feat604-transmit-property-and-casualty-claim-number)
    - [Miscellaneous Existing Requirements - Delete – FEAT435 VAMC as Billing Provider](#miscellaneous-existing-requirements-delete-feat435-vamc-as-billing-provider)
    - [Miscellaneous Existing Requirements - Change – FEAT102 EDI Parameter Report](#miscellaneous-existing-requirements-change-feat102-edi-parameter-report)
    - [Miscellaneous Existing Requirements - Delete – FEAT443 Schedule Mailman Message/Payer Settings for Billing Provider/Service Facility](#miscellaneous-existing-requirements-delete-feat443-schedule-mailman-messagepayer-settings-for-billing-providerservice-facility)
    - [Miscellaneous Existing Requirements - Delete – FEAT444 Default Schedule Mailman Message/Payer Settings for Billing Provider/Service Facility](#miscellaneous-existing-requirements-delete-feat444-default-schedule-mailman-messagepayer-settings-for-billing-providerservice-facility)
    - [Miscellaneous Existing Requirements - Delete – FEAT445 Mailman Message with Payer Settings/Billing Provider/Service Facility](#miscellaneous-existing-requirements-delete-feat445-mailman-message-with-payer-settingsbilling-providerservice-facility)
    - [Miscellaneous Existing Requirements - Delete – FEAT446 Mailman Message with Payer Settings/Billing Provider/Service Facility](#miscellaneous-existing-requirements-delete-feat446-mailman-message-with-payer-settingsbilling-providerservice-facility)
    - [Miscellaneous Existing Requirements - Delete – FEAT573 Security Key for CopyCancel a Claim](#miscellaneous-existing-requirements-delete-feat573-security-key-for-copycancel-a-claim)
This Integrated Billing (IB) patch is comprised of numerous enhancements and correction of existing issues in the Integrated Billing application. These enhancements are designed to improve revenue through the creation of HIPAA compliant claims. This patch will also remove some of the features that were introduce to support the transition from ASC X12N 4010 to ASC X12N 5010 as they are no longer needed. This patch will provide the ability to transmit the new national payer identification numbers (HPID/OEID) in claim transactions and view the Health Plan Identifier/Other Entity Identifier (HPID/OEID) in the Insurance Company Editor and on The EDI Parameter report.
Some of the more significant things this patch will provide are the ability for billing personnel to do the following:
- Add National Drug Codes and Units to a claim
- Add Procedure Code descriptions to Not Otherwise Classified procedures on a claim
- Define a Pay-to Provider to be used on TRICARE claims
- View linked first-party claim information via TPJI
- Sort the COB Management Worklist and Re-generate Unbilled Amounts Report by Division
- Define non-VA facilities as sole-proprietorships
- View the data associated with cancelled claims
APPLICATION/VERSION PATCH
---------------------------------------------------------------
INTEGRATED BILLING (IB) V. 2.0 IB\*2\*516
This patch (IB\*2\*516) is being released in the Kernel Installation and Distribution System (KIDS) distribution.

## Documentation and Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to FTP the files from

REDACTED

This transmits the files from the first available FTP server. Sites may

also elect to retrieve software directly from a specific server as

follows:

Albany REDACTED REDACTED

Hines REDACTED REDACTED

Salt Lake City REDACTED REDACTED

Documentation can also be found on the VA Software Documentation Library

at: http://www.va.gov/vdl/

File Description File Name FTP Mode

-------------------------------------------------------------------------

IB Release Notes/Installation Guide ib_2_0_p516_rn.pdf Binary

EDI User Guide edi_user_guide_r0415.pdf Binary

Integrated Billing (IB) V. 2.0

Technical Manual ib_2_0_tm_r0415.pdf Binary

*(This page included for two-sided copying.)*

# Patch Description and Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

=============================================================================

Run Date: APR 23, 2015 Designation: IB\*2\*516

Package : INTEGRATED BILLING Priority : MANDATORY

Version : 2 Status : RELEASED

=============================================================================

Associated patches: (v)IB\*2\*66 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*68 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*93 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*139 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*370 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*404 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*431 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*437 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*448 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*451 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*458 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*476 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*488 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*494 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*497 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*506 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*515 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*519 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*521 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*526 \<\<= must be installed BEFORE \`IB\*2\*516'

(v)IB\*2\*533 \<\<= must be installed BEFORE \`IB\*2\*516'

Subject: EBILLING - CLAIMS COMPLIANCE

Category: ROUTINE

OTHER

DATA DICTIONARY

INPUT TEMPLATE

Description:

===========

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Important Note: There is one \*\*MANDATORY\*\* pre-installation activity associated with this install.

The IB Staff MUST empty the 837 extract/transmission queue PRIOR to the installation of this patch.

Please reference instructions from the Pre/Post Installation Overview for further details.

Additionally, the patch installation instructions include a menu rebuild to remove a deleted option. It is \*\*STRONGLY SUGGESTED\*\* that the rebuild of primary menu trees occurs during non-peak hours. The patch should either be installed during non-peak hours, or you may enter NO to the Rebuild Menus prompt if your system does this in a nightly TaskMan process.

Important Note: After Initial Operating Capabilities (IOC) was completed, the ICD10 development team discovered a Severity Level 3 defect:

The attending provider's name is not being automatically added to Billing screen 10, Section 3 when a bill is created by the AutoBiller and the provider has a valid National Provider Identifier (NPI). Note that the attending provider's name transmits when the biller manually adds it to the bill.

This has been logged as Remedy ticket INC000001243424 and will be addressed in a future release.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

This Integrated Billing (IB) patch introduces changes to VistA's Electronic Claims processing in order to meet the Committee on Operating Rules for Information Exchange (CORE) Operating Rules.

Complete List of patch items:

1.  Enter/Edit Billing Information \[IB EDIT BILLING INFO\]
1)  Provide the ability for users to authorize a claim for Skilled Nursing Facility (SNF) with a revenue code(s) less than 100 (remove existing fatal error for codes outside the 100-999 range).
2)  Provide the ability for users to add National Drug Codes to non-prescription claims.
3)  Provide the ability for users to add a description to a claim with a procedure code that ends in 99 or contains the following in the code description:

Not Otherwise Classified

Not Otherwise

Unlisted

Not listed

Unspecified

Unclassified

Not otherwise specified

Non-specified

Not elsewhere specified

Not elsewhere

Nos (Note: Include "nos ", "nos;", "nos,")

Noc (Note: Include "noc ", "noc;", "noc,")

4)  Prevent the ability to authorize claims with non-billable providers \[provider has no National Provider Identification Number (NPI)\] on the claim.
5)  Prevent the ability to authorize a Fee Basis claim with a non-VA Lab or Facility that has no NPI.
6)  Provide the ability to authorize a claim with Service Facility data that does not have a Lab or Facility Taxonomy Code without displaying a Warning (remove existing warning).
7)  Provide the ability to print a TRICARE claim with a TRICARE-specific Pay-to Provider.
8)  Provide the ability for users to re-sequence Diagnoses Codes (DX) after Procedures have been associated with the DX (Pointers) without breaking the association.
9)  Provide the ability for users to view a list of the following Code sets by Code number when they enter ?? for Help on Billing Screen 4 and 5:

Occurrence Codes

Condition Codes

Value Codes

10) Provide the ability for users to lookup a Code from one of the following Code sets using the code number:

Occurrence Codes

Condition Codes

Value Codes

2.  Insurance Company Editor
1)  Remove functionality that provides the ability for a site to set a parameter that forces all claims to a particular payer, to use the VAMC as the Billing Provider instead of the lowest enumerated Billing Provider.
2)  Change the Plan Type description for the Plan Type = FI- FEP (Federal Employee Plan) to Do Not Use for BC/BS when users enter ?? for Help at a Plan Type field.
3.  Reports
1)  Add the display of the new Health Plan Identifier (HPID) and the Other Entity Identifier (OEID) to the Insurance Company EDI Parameter Report \[IBCN INSURANCE EDI REPORT\].
2)  Remove the display of the Billing Provider override parameter from the Insurance Company EDI Parameter Report \[IBCN INSURANCE EDI REPORT\].
3)  Provide the ability to display partial or complete new HIPAA compliant electronic 270/271 Health Care Eligibility Benefit Inquiry and Response fields on IB reports.
4)  Provide the ability for users to sort and display the Re-Generate Unbilled Amounts Report \[IBT RE-GEN UNBILLED REPORT\] by Division.
5)  Deleted Insurance Company Billing Provider Flag Rpt/Msg \[IBCN INS BILL PROV FLAG RPT\] which is no longer needed.
4.  Third Party Joint Inquiry (TPJI) \[IBJ THIRD PARTY JOINT INQUIRY\]
1)  Provide the ability for users to see that a claim in TPJI, Active and Inactive claim lists, is an Institutional or a Professional claim.
2)  Provide the ability for users to view the Co-payment amount associated with a claim in TPJI
5.  COB Management Worklist (CBW) \[IBCE COB MANAGEMENT\]
1)  Provide the ability for users to sort and display the CBW by Division Transactions.
6.  Transactions
1)  Provide the ability to transmit the HPID in the Institutional/ Professional 837 claim transaction (Loops 2010BB and 2330B) - continue to transmit legacy primary and secondary IDs in the Institutional/Professional 837 claim transaction.
2)  Provide the ability to transmit the same NPI (organizational) for a Service Facility and a Rendering Provider (individual) on an Institutional/Professional 837 claim transaction.
3)  Remove monthly Mailman messages that notify CBO of how sites have the EDI Parameter for Billing Provider set.
4)  Prevent an Institutional/Professional 837 claim transaction with a Y4 Property and Casualty Number Qualifier with no corresponding Property and Casualty Number.
5)  Provide the ability to transmit the TRICARE Pay-to Provider on all claims with Rate Type equal to TRICARE and TRICARE REIMB. INS (Loop 2010AB).
6)  Provide the ability to transmit a NDC code and units on a non-prescription 837 claim transaction.
7.  Correct Rejected/Denied Bill (CRD) \[IB CORRECT REJECTED/DENIED\] and Copy and Cancel (CLON) \[IB COPY AND CANCEL\]
1)  Remove the Security Key, IB CLON, from the OPTION (#19) File that locked the CLON option.
2)  Remove the ability for users to CRD secondary/tertiary claims.
3)  Provide the ability for as many fields as possible to be copied from an original claim to a copy.
8.  View Cancelled Claim \[IB VIEW CANCEL BILL\]
1)  A new option to provide the ability to see all the data that was in a cancelled claim.
9.  Provider ID Maintenance \[IBCE PROVIDER MAINT\]
1)  Provide the ability for users to define an Outside Facility that is a sole-proprietorship with an NPI number that is also used by the provider who is the sole-proprietor.
10. MCCR Site Parameter Display/Edit \[IBJ MCCR SITE PARAMETERS\]
1)  Provide the ability for users to define a Pay-to Provider to be used only on claims with a Rate Type equal to TRICARE or TRICARE REIMB. INS.
2)  Lock the new Tricare Pay-to Provider functionality Printed CMS - 1500 and UB - 04 Forms with new security key, IB EDIT PAY-TO TC.
3)  Lock the existing Pay-to Provider functionality Printed CMS - 1500 and UB - 04 Forms with new security key, IB EDIT PAY-TO.
11. Printed CMS - 1500 and UB-04 Forms
1)  Provide the ability to print an NDC code on a non-prescription claim.

Patch Components

================

The following is a list of field modifications included in this patch:

Files & Fields Associated:

File Name (#) New/Modified/

Sub-file Name (#) Field Name (Number) Deleted

------------------- --------------------------------- -------------

PATIENT (#2)

INSURANCE TYPE sub-file (#2.312)

NEW GROUP NAME (#20) Modified

NEW GROUP NUMBER (#21) Modified

INSURANCE COMPANY (#36) Modified

SEND LAB OR FAC IDS FOR VAMC Modified

(#4.07)

USE VAMC AS BILL PROV ON 1500 Modified

(#4.11)

USE VAMC AS BILL PROV ON UB04 Modified

(#4.12)

USE BILL PROV VAMC ADDRESS Modified

(#4.13)

IB SITE PARAMETERS (#350.9) Modified

DEFAULT TRICARE PAY-TO PROV New

(#11.04)

TRICARE PAY-TO PROVIDERS sub-file (#350.929) New

TC FACILITY (#.01) New

TC NAME (#.02) New

TC FEDERAL TAX NUMBER (#.03) New

TC TELEPHONE NUMBER (#.04) New

TC PARENT PAY-TO PROVIDER (#.05) New

TC STREET ADDRESS 1 (#1.01) New

TC STREET ADDRESS 2 (#1.02) New

TC CITY (#1.03) New

TC STATE (#1.04) New

TC ZIP (#1.05) New

GROUP INSURANCE PLAN (#355.3) Modified

ELECTRONIC PLAN TYPE (#.15) Modified

IB NON/OTHER VA BILLING PROVIDER (#355.93) Modified

SOLE PROPRIETORSHIP (#.17) New

NON-VA PROVIDER (#.18) New

IB DATA ELEMENT DEFINITION (#364.5) Modified

Screen: I \$\$INCLUDE^IBY516PR(5,Y)

IB FORM SKELETON DEFINITION (#364.6) Modified

Screen: I \$\$INCLUDE^IBY516PR(6,Y)

IB FORM FIELD CONTENT (#364.7) Modified

Screen: I \$\$INCLUDE^IBY516PR(7,Y)

BILL/CLAIMS (#399) Modified

PRIMARY NODE 7 (#371) New

SECONDARY NODE 7 (#372) New

TERTIARY NODE 7 (#373) New

PRIMARY INSURANCE HPID (#471) New

SECONDARY INSURANCE HPID (#472) New

TERTIARY INSURANCE HPID (#473) New

PROPERTY/CASUALTY CLAIM NUMBER Modified

(#261)

CONDITION CODE sub-file (#399.040)

CONDITION CODE (#.01) Modified

OCCURRENCE CODE sub-file (#399.041)

OCCURRENCE CODE (#.01) Modified

VALUE CODE sub-file (#399.047)

VALUE CODE (#.01) Modified

PROCEDURES sub-file (#399.0304) Modified

PROCEDURE DESCRIPTION (#51) New

NDC (#53) New

UNITS (#54) New

Bulletins Associated:

New/Modified/

Bulletin Name Deleted

------------- -------------

N/A

Dialogs Associated:

New/Modified/

Dialog Name Deleted

----------- -------------

N/A

Forms Associated:

New/Modified/

Form Name File Name (Number) Deleted

--------- ------------------ -------------

N/A

Functions Associated:

New/Modified/

Function Name Deleted

------------- -------------

N/A

Help Frames Associated:

New/Modified/

Help Frame Name Deleted

--------------- -------------

N/A

Mail Groups Associated:

New/Modified/

Mail Group Name Deleted

--------------- -------------

N/A

Options Associated:

New/Modified/

Option Name Type Deleted

----------- ---- -------------

IB COPY AND CANCEL run routine Modified

IB VIEW CANCEL BILL run routine New

IBCN INS BILL PROV FLAG run routine Delete

RPT

Parameter Definitions:

New/Modified/

Parameter Name Deleted

-------------- -------------

N/A

Parameter Template:

New/Modified/

Template Name Deleted

------------- -------------

N/A

Protocols Associated:

New/Modified/

Protocol Name Deleted

------------- -------------

IBCEM CSA CANCEL/CLONE BILL New

IBCEM CSA MSG MENU Modified

IBJP IB PAY-TO DIVISION ADD Modified

IBJP IB PAY-TO PROVIDER ADD Modified

IBJP IB PAY-TO PROVIDER DEL Modified

IBJP IB PAY-TO PROVIDER EDIT Modified

IBJP IB PAY-TO PROVIDERS MENU Modified

IBJP IB TRICARE PAY-TO ASSOCIATIONS MENU New

IBJP IB TRICARE PAY-TO DIVISION ADD New

IBJP IB TRICARE PAY-TO PROVIDER ADD New

IBJP IB TRICARE PAY-TO PROVIDER DEL New

IBJP IB TRICARE PAY-TO PROVIDER DIVISIONS New

IBJP IB TRICARE PAY-TO PROVIDER EDIT New

IBJP IB TRICARE PAY-TO PROVIDERS MENU New

Security Keys Associated:

New/Modified/

Security Key Name Deleted

----------------- -------------

IB EDIT PAY-TO New

IB EDIT PAY-TO TC New

Templates, Input Associated:

New/Modified/

Template Name Type File Name (Number) Deleted

------------- ---- ------------------ -------------

IB SCREEN3 Input BILL/CLAIMS (#399) Modified

IBEDIT INS CO1 Input INSURANCE COMPANY (#36) Modified

Templates, List Associated:

New/Modified/

Template Name Type Deleted

------------- ---- -------------

IBJP IB PAY-TO List Modified

ASSOCIATIONS

IBJP IB PAY-TO List Modified

PROVIDERS

IBJP IB TRICARE List New

PAY-TO ASSOCS

IBJP IB TRICARE List New

PAY-TO PROVS

Templates, Print Associated:

New/Modified/

Template Name Type File Name (Number) Deleted

------------- ---- ------------------ -------------

IBNOTVER Print PATIENT (#2) Modified

Templates, Sort Associated:

New/Modified/

Template Name Type File Name (Number) Deleted

------------- ---- ------------------ -------------

N/A

Additional Information:

N/A

New Service Requests (NSRs)

----------------------------

\#20110503 Electronic Data Interchange (EDI) New Standards and Operating

Rules (Veterans Health Administration) VHA Provider-Side TCRs.

Patient Safety Issues (PSIs)

-----------------------------

N/A

Remedy Ticket(s) & Overview

---------------------------

N/A

Test Sites:

----------

REDACTED

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview

------------------------------

\*\*\*\*Important Note: There is one \*\*MANDATORY\*\* pre-installation

activity associated with this install.

The IB Staff MUST empty the 837 extract/transmission queue PRIOR to the installation of this patch. \*\*\*

The site Information Resource Management (IRM) would coordinate with the Billing Department to insure that the 837 extract/transmission queue is empty. The Billing Department should be aware of the set of instructions to be executed. If not billing supervisor can be contacted. Once the Billing Department has completed the instruction, the Billing department is to inform IRM that the patch installation could proceed.

The instructions to empty the queue are as follows:

Select the option: TRANSMIT EDI BILLS - MANUAL \[IBCE 837 MANUAL

TRANSMIT\]

What is the purpose of this option?

This option is used to by-pass the normal daily/nightly transmission

queues if the need arises to get the claim to the payer quickly.

When is this option used?

There are occasions when there is a need to transmit a claim(s)

immediately instead of waiting for the batching frequency as scheduled

in the MCCR Site Parameter. This option will allow sending individual

claim(s) or all claims in a ready for extract status.

Upon selecting this option you will be prompted with the following:

Select one of the following:

A Transmit (A)LL bills in READY FOR EXTRACT status

S Transmit only (S)ELECTED bills

You should select 'A' for ALL

Once the Billing Department has completed the instruction, the Billing department is to inform IRM that the patch installation could proceed.

There are no other mandatory pre-installation activities associated with this package.

\*\*\*\*Important Note: After IOC was completed, the ICD10 development team

discovered a Severity Level 3 defect:

The attending provider's name is not being automatically added to Billing

screen 10, Section 3 when a bill is created by the AutoBiller and the provider has a valid NPI. Note that the attending provider's name transmits when the biller manually adds it to the bill.

This has been logged as Remedy ticket INC000001243424 and will be addressed in a future release.

The pre-installation routine will delete unused Output Formatter entries.

The pre and post installation routines will recompile the Input Templates

for the Billing Screens.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

-------------------------

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\* You should install this patch during non-peak hours, when no \*

\* Integrated Billing or Accounts Receivable users are on the \*

\* system. \*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*There are no options to disable.

Install Time: Less than 10 minutes.

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following option. When prompted for the INSTALL enter the patch \#IB\*2.0\*516.
1)  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2)  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3)  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4)  Print Transport Global - This option will allow you to view the components of the KIDS build.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//' You may answer NO if your system does this in a nightly TaskMan process.
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' Answer NO
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// Answer NO
8.  If prompted "Delay Install (Minutes): (0 - 60): 0// respond 0.

Post-Installation Instructions

------------------------------

Routines IBY516PO and IBY516PR can be manually deleted by IT/IRM upon completion of the installation.

New Security Keys IB EDIT PAY-TO and IB EDIT PAY-TO TC should be assigned

to the Billing Supervisor.

Routine Information:

====================

The second line of each of these routines now looks like:

;;2.0;INTEGRATED BILLING;\*\*\[Patch List\]\*\*;21-MAR-94;Build 123

The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

Routine Name: IBATLM3A

Before: B22313695 After: B24217228 \*\*115,516\*\*

Routine Name: IBBFAPI

Before: B43623282 After: B43892084 \*\*267,297,249,317,361,384,404,516\*\*

Routine Name: IBCAPP2

Before: B43298709 After: B49339546 \*\*432,447,516\*\*

Routine Name: IBCBB11

Before: B97720533 After: B95727608 \*\*51,343,363,371,395,392,401,

384,400,436,432,516\*\*

Routine Name: IBCBB7

Before: B28157499 After: B28514446 \*\*51,137,240,447,488,516\*\*

Routine Name: IBCC

Before: B57603103 After: B65165308 \*\*2,19,77,80,51,142,137,161,

199,241,155,276,320,358,433,

432,447,516\*\*

Routine Name: IBCCC

Before: B20967189 After: B22970985 \*\*80,109,106,51,320,433,432,447,516\*\*

Routine Name: IBCCC2

Before:B108841715 After:B113680571 \*\*80,106,124,138,51,151,137,

161,182,211,245,155,296,320,

348,349,371,400,433,432,447,

516\*\*

Routine Name: IBCD3

Before: B31598371 After: B32514703 \*\*14,55,52,91,106,125,51,148,

160,137,210,245,260,405,384,

516\*\*

Routine Name: IBCECOB

Before: B17969465 After: B27628888 \*\*137,155,288,432,488,516\*\*

Routine Name: IBCECOB1

Before:B112283735 After:B141608790 \*\*137,155,288,348,377,417,432,

447,488,516\*\*

Routine Name: IBCECOB2

Before:B183092638 After:B183699434 \*\*137,155,433,432,447,488,516\*\*

Routine Name: IBCECSA4

Before: B60720503 After: B61845851 \*\*137,155,320,371,433,516\*\*

Routine Name: IBCEF

Before: B58449164 After: B64641917 \*\*52,80,51,137,288,296,361,371,

447,516\*\*

Routine Name: IBCEF11

Before: B67207596 After: B80990662 \*\*51,137,155,309,335,348,349,

371,432,447,473,516\*\*

Routine Name: IBCEF21

Before: B23776552 After: B23973664 \*\*51,296,371,389,448,516\*\*

Routine Name: IBCEF22

Before: B79219296 After: B90984490 \*\*51,137,135,155,309,349,389,

432,488,516\*\*

Routine Name: IBCEF3

Before: B47162871 After: B47786755 \*\*52,84,121,51,152,210,155,348,

349,389,488,516\*\*

Routine Name: IBCEF31

Before: B11345418 After: B14588723 \*\*155,296,349,400,432,488,516\*\*

Routine Name: IBCEF72

Before: B54190068 After: B57296289 \*\*232,320,349,432,516\*\*

Routine Name: IBCEF73A

Before: B55865498 After: B43076924 \*\*343,374,395,391,400,432,516\*\*

Routine Name: IBCEF74A

Before: B39969650 After: B39038241 \*\*320,343,349,395,400,432,516\*\*

Routine Name: IBCEF76

Before: B45722940 After: B48153213 \*\*320,349,400,432,516\*\*

Routine Name: IBCEF77

Before: B24927059 After: B27920356 \*\*232,280,155,290,291,320,348,

349,516\*\*

Routine Name: IBCEF78

Before: B4445010 After: B7140538 \*\*371,516\*\*

Routine Name: IBCEF79

Before:B170462166 After:B118916763 \*\*400,419,432,516\*\*

Routine Name: IBCEFP

Before:B115077680 After:B115631357 \*\*432,447,473,516\*\*

Routine Name: IBCEOB0

Before: B90917821 After: B91995821 \*\*135,280,155,431,488,516\*\*

Routine Name: IBCEOB01

Before: B24417822 After: B25712240 \*\*377,516\*\*

Routine Name: IBCEP8

Before:B129710257 After:B134052747 \*\*51,137,232,288,320,343,374,

377,391,400,436,432,476,516\*\*

Routine Name: IBCEP81

Before: B65647537 After: B67515820 \*\*343,391,400,476,516\*\*

Routine Name: IBCEP82

Before: B73798180 After: B72564022 \*\*343,374,377,391,516\*\*

Routine Name: IBCEP8B

Before: B34200270 After: B35610752 \*\*391,432,476,488,516\*\*

Routine Name: IBCEPB

Before: B10650639 After: B7598816 \*\*320,348,349,400,516\*\*

Routine Name: IBCEQ1A

Before: B62926268 After: B67430449 \*\*232,348,349,516\*\*

Routine Name: IBCF21

Before: B15664460 After: B16291620 \*\*8,80,51,488,516\*\*

Routine Name: IBCF23A

Before: B19444201 After: B20324273 \*\*51,432,516\*\*

Routine Name: IBCF31

Before: B19588940 After: B19880263 \*\*17,52,80,51,516\*\*

Routine Name: IBCNBLE

Before:B108261556 After:B108261560 \*\*82,231,184,251,371,416,435,

452,497,519,516\*\*

Routine Name: IBCNBLE1

Before: B32174406 After: B32419797 \*\*184,271,416,435,467,516\*\*

Routine Name: IBCNBLP

Before: B25507553 After: B28291070 \*\*82,497,516\*\*

Routine Name: IBCNBLP1

Before: B31255881 After: B34470080 \*\*82,133,516\*\*

Routine Name: IBCNEHLQ

Before: B46752354 After: B49920378 \*\*184,271,300,361,416,438,467,

497,533,516\*\*

Routine Name: IBCNRP

Before: B21440357 After: B23991821 \*\*251,516\*\*

Routine Name: IBCNRP5

Before: B56002389 After: B56117515 \*\*276,516\*\*

Routine Name: IBCNRPM1

Before: B6996620 After: B7640127 \*\*251,516\*\*

Routine Name: IBCNRPMT

Before: B4118434 After: B4159618 \*\*251,516\*\*

Routine Name: IBCNRPS2

Before: B22515799 After: B24644732 \*\*276,516\*\*

Routine Name: IBCNRRP3

Before: B55033574 After: B58110020 \*\*251,276,516\*\*

Routine Name: IBCNS

Before: B27665348 After: B28265165 \*\*28,43,80,82,133,399,516\*\*

Routine Name: IBCNS1

Before: B35071030 After: B42707809 \*\*28,60,52,85,107,51,137,240,

371,516\*\*

Routine Name: IBCNS2

Before: B24154529 After: B29335309 \*\*28,43,80,51,137,155,488,516\*\*

Routine Name: IBCNS3

Before: B62573337 After: B60729122 \*\*287,399,416,516\*\*

Routine Name: IBCNSBL1

Before: B33740946 After: B37090504 \*\*6,28,82,249,276,516\*\*

Routine Name: IBCNSC1

Before: B90495985 After: B80307925 \*\*62,137,232,291,320,348,349,

371,400,519,516\*\*

Routine Name: IBCNSC3

Before: B18009103 After: B18386728 \*\*28,46,68,516\*\*

Routine Name: IBCNSC4

Before: B18086570 After: B18719019 \*\*43,85,103,251,416,497,516\*\*

Routine Name: IBCNSGE

Before:B103633903 After: B98010090 \*\*296,400,521,516\*\*

Routine Name: IBCNSGM

Before: B42642306 After: B42739860 \*\*400,516\*\*

Routine Name: IBCNSJ14

Before: B9289898 After: B9400113 \*\*28,516\*\*

Routine Name: IBCNSJ2

Before: B21486680 After: B22855491 \*\*28,516\*\*

Routine Name: IBCNSJ4

Before: B28671454 After: B30114071 \*\*28,62,516\*\*

Routine Name: IBCNSJ5

Before: B19164548 After: B19961411 \*\*43,516\*\*

Routine Name: IBCNSM2

Before: B21029266 After: B21200856 \*\*28,103,139,516\*\*

Routine Name: IBCNSM3

Before: B14271242 After: B15749953 \*\*6,28,85,211,251,399,506,516\*\*

Routine Name: IBCNSM31

Before: B21224087 After: B21467883 \*\*6,28,68,413,497,516\*\*

Routine Name: IBCNSM5

Before: B21379064 After: B22650774 \*\*28,497,516\*\*

Routine Name: IBCNSMM

Before: B20650555 After: B21594622 \*\*103,133,184,516\*\*

Routine Name: IBCNSP

Before: B48468493 After: B49297563 \*\*6,28,43,52,85,251,363,371,

416,497,516\*\*

Routine Name: IBCNSP0

Before: B37737467 After: B38008161 \*\*28,43,52,85,93,103,137,229,

251,363,371,399,438,458,497,

516\*\*

Routine Name: IBCNSP11

Before: B11695386 After: B11721673 \*\*28,43,85,103,137,251,399,516\*\*

Routine Name: IBCNSUR

Before: B24160231 After: B24287477 \*\*103,276,506,516\*\*

Routine Name: IBCNSUR1

Before: B56652391 After: B57694333 \*\*103,225,276,516\*\*

Routine Name: IBCNSUX

Before: B16195424 After: B16407219 \*\*103,516\*\*

Routine Name: IBCNSUX1

Before: B20036863 After: B20451867 \*\*103,133,516\*\*

Routine Name: IBCOMA1

Before: B29547296 After: B34536686 \*\*103,516\*\*

Routine Name: IBCOMC2

Before: B12700505 After: B12669229 \*\*103,153,516\*\*

Routine Name: IBCONS1

Before: B75219188 After: B79511698 \*\*66,80,137,516\*\*

Routine Name: IBCOPP2

Before: B19008544 After: B20749250 \*\*28,62,93,516\*\*

Routine Name: IBCOPP3

Before: B9597460 After: B10453963 \*\*28,516\*\*

Routine Name: IBCRBC

Before: B11588633 After: B13081185 \*\*52,80,106,51,137,245,370,516\*\*

Routine Name: IBCSC3

Before: B37249647 After: B37464352 \*\*8,43,52,80,82,51,137,232,320,

377,516\*\*

Routine Name: IBCSC4D

Before: B61931126 After: B75384760 \*\*55,62,91,106,124,51,210,403,

400,461,516\*\*

Routine Name: IBCSCE1

Before: B7420897 After: B7430380 \*\*516\*\*

Routine Name: IBCU7

Before: B77808645 After:B111564056 \*\*62,52,106,125,51,137,210,245,

228,260,348,371,432,447,488,

461,516\*\*

Routine Name: IBCU74

Before: B35879024 After: B36449231 \*\*228,260,339,432,516\*\*

Routine Name: IBCVA0

Before: B10445232 After: B10440495 \*\*52,361,371,516\*\*

Routine Name: IBJDF51

Before: B57886181 After: B58912743 \*\*123,185,240,356,452,516\*\*

Routine Name: IBJPS

Before: B3981041 After: B4384435 \*\*39,52,70,115,143,51,137,161,

155,320,348,349,377,384,400,

432,494,461,516\*\*

Routine Name: IBJPS2

Before: B41765087 After: B45274108 \*\*39,52,115,143,51,137,161,155,

320,348,349,377,384,400,432,

494,461,516\*\*

Routine Name: IBJPS3

Before: B89166752 After:B111722417 \*\*400,432,516\*\*

Routine Name: IBJPS4

Before: B28407182 After: B36439628 \*\*400,516\*\*

Routine Name: IBJTCA1

Before: B54215341 After: B59453492 \*\*39,80,106,137,223,276,363,

384,432,452,473,497,521,516\*\*

Routine Name: IBJTCA2

Before: B23068552 After: B40902439 \*\*39,80,155,320,516\*\*

Routine Name: IBJTLA1

Before: B10714466 After: B11361045 \*\*39,80,61,51,153,137,183,276,

451,516\*\*

Routine Name: IBJTLB1

Before: B11067077 After: B11794378 \*\*39,80,61,137,276,451,516\*\*

Routine Name: IBJTU1

Before: B7894877 After: B7959085 \*\*39,80,276,451,516\*\*

Routine Name: IBJTU31

Before: B7603119 After: B8926798 \*\*39,61,516\*\*

Routine Name: IBNCPDP3

Before: B84831779 After: B84489638 \*\*223,276,342,363,383,384,411,

435,452,516\*\*

Routine Name: IBNCPDP5

Before: B80347970 After: B80792303 \*\*411,452,526,516\*\*

Routine Name: IBNCPDS1

Before: B10933965 After: B11865744 \*\*411,452,516\*\*

Routine Name: IBNCPEV

Before: B97561964 After:B102192248 \*\*342,363,383,384,411,435,452,

521,516\*\*

Routine Name: IBNCPEV1

Before: B65821785 After: B67774383 \*\*342,339,363,411,435,452,516\*\*

Routine Name: IBOTR3

Before: B29774240 After: B31663645 \*\*42,80,100,118,128,133,447,516\*\*

Routine Name: IBRBUL

Before: B36492961 After: B39836566 \*\*70,95,121,153,195,347,452,516\*\*

Routine Name: IBRFN3

Before: B29612898 After: B30451954 \*\*61,133,210,309,389,516\*\*

Routine Name: IBRFN4

Before: B25630558 After: B27444633 \*\*301,305,389,516\*\*

Routine Name: IBTOBI1

Before: B18898112 After: B19861632 \*\*276,377,516\*\*

Routine Name: IBTRCD0

Before: B16113018 After: B16868309 \*\*458,516\*\*

Routine Name: IBTUBO

Before: B25696439 After: B35610159 \*\*19,31,32,91,123,159,192,235,

248,155,516\*\*

Routine Name: IBTUBO1

Before: B47180115 After: B62446159 \*\*19,31,32,91,123,159,247,155,

277,339,399,516\*\*

Routine Name: IBTUBO2

Before: B33667876 After: B49823798 \*\*19,31,32,91,123,159,192,155,

309,347,437,516\*\*

Routine Name: IBTUBO3

Before: B23289291 After: B28228475 \*\*123,159,192,155,277,516\*\*

Routine Name: IBTUBOA

Before: B30890238 After: B37900623 \*\*19,31,32,91,123,159,192,155,

276,516\*\*

Routine Name: IBTUBUL

Before: B21781134 After: B72452562 \*\*19,123,159,217,155,356,516\*\*

Routine Name: IBVCB

Before: n/a After:B123320263 \*\*516\*\*

Routine Name: IBVCB1

Before: n/a After:B135425175 \*\*516\*\*

Routine Name: IBVCB2

Before: n/a After:B110047132 \*\*516\*\*

Routine Name: IBY516PO

Before: n/a After: B4162987 \*\*516\*\*

Routine Name: IBY516PR

Before: n/a After: B10110091 \*\*516\*\*

Routine list of preceding patches: 139, 370, 404, 437, 448, 451, 461, 506

519, 521, 526, 533

*(This page included for two-sided copying.)*

# Backout and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview of Backout and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback plan for VistA applications is complex and not able to be a "one size fits all." The general strategy for VistA rollback is to repair the code with a follow-on patch. The development team recommends that sites log a Remedy ticket if it is a nationally released patch; otherwise, the site should contact the Product Support team directly for specific solutions to their unique problems.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the VistA Installation Procedure of the KIDS build, the installer hopefully backed up the modified routines by the use of the 'Backup a Transport Global' action.  The installer can restore the routines using the MailMan message that were saved prior to installing the patch.  The backout procedure for global, data dictionary and other VistA components is more complex and will require issuance of a follow-on patch to ensure all components are properly removed. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with restoration of the data.  This backout may need to include a database cleanup process.

Please contact the Product Support team for assistance if the installed patch that needs to be backed out contains anything at all besides routines before trying to backout the patch.  If the installed patch that needs to be backed out includes a pre or post install routine please contact the product support team before attempting the backout.

From the Kernel Installation and Distribution System Menu, select

the Installation Menu.  From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch \#.

    a. Backup a Transport Global - This option will create a backup

       message of any routines exported with this patch. It will not

       backup any other changes such as DD's or templates.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedure for VistA patches is complicated and may require a follow-on patch to fully roll back to the pre-patch state. This is due to the possibility of Data Dictionary updates, Data updates, cross references, and transmissions from VistA to offsite data stores.

Please contact the Product Support team for assistance if needed.

*(This page included for two-sided copying.)*

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following features in VistA, Integrated Billing are affected by this effort:

## System Feature: Enter/Edit Billing Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Enter/Edit Billing Information- Revenue Codes \<100

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to authorize a claim with one or more revenue codes outside the 100-999 range.

### Enter/Edit Billing Information - Line Level NDC Codes to Non-Prescription Claims - Professional 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The IB System provides the ability for users to add a line level 5-4-2 format National Drug Code to a non-prescription procedure when creating a professional claim.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Enter/Edit Billing Information- Line Level NDC Codes to Non-Prescription Claims – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to add a line level 5-4-2 format National Drug Code to a non-prescription procedure when creating an institutional claim.

### Enter/Edit Billing Information- Line Level Description – 99 Procedure Codes – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to add a line level, 1-80 character free text description to a procedure code that ends in 99 on a professional claim.

### Enter/Edit Billing Information - Line Level Description - 99 Procedure Codes – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to add a line level, 1-80 character free text description to a procedure code that ends in 99 on an institutional claim.

### Enter/Edit Billing Information - Line Level Description - NOC Procedure Codes – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to add a line level, 1-80 character free text description to a procedure code (CPT/HCPCS) on a professional claim that contains the following text in the procedure's description (file 81, field 81.01,01):

- Not Otherwise Classified
- Not Otherwise
- Unlisted
- Not listed
- Unspecified
- Unclassified
- Not otherwise specified
- Non-specified
- Not elsewhere specified
- Not elsewhere
- Nos (Note: Include "nos ", "nos;", "nos,")
- Noc (Note: Include "noc ", "noc;", "noc,")

### Enter/Edit Billing Information - Line Level Description - NOC Procedure Codes – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to add a line level, 1-80 character free text description to a procedure code (CPT/HCPCS) on an institutional claim that contains the following text in the procedure's description (file 81, field 81.01,01):

- Not Otherwise Classified
- Not Otherwise
- Unlisted
- Not listed
- Unspecified
- Unclassified
- Not otherwise specified
- Non-specified
- Not elsewhere specified
- Not elsewhere
- Nos (Note: Include "nos ", "nos;", "nos,")
- Noc (Note: Include "noc ", "noc;", "noc,")

### Enter/Edit Billing Information - Fatal Error - Non-billable Providers – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from authorizing a professional claim that contains an individual provider who has no NPI number:

- Rendering
- Supervising
- Referring

### Enter/Edit Billing Information - Fatal Error - Non-billable Providers – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from authorizing an institutional claim that contains an individual provider who has no NPI number:

- Attending
- Operating
- Other Operating

### Enter/Edit Billing Information - Screen – Non-billable Provider – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System automatically removes all individual providers who have no NPI number from an institutional claim.

### Enter/Edit Billing Information - Screen – Non-billable Provider – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System automatically removes all individual providers who have no NPI number from a professional claim.

### Enter/Edit Billing Information - Fatal Error – Missing non-VA Lab or Facility NPI – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from authorizing a professional Fee Basis claim with a non-VA Facility that does not have an NPI.

### Enter/Edit Billing Information - Fatal Error – Missing non-VA Lab or Facility NPI – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from authorizing an institutional Fee Basis claim with a non-VA Facility that does not have an NPI.

### Enter/Edit Billing Information - Warning – Missing Lab or Facility Taxonomy Code – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System no longer provides a non-fatal warning message to users when an institutional claim contains a Lab or Facility which has no active taxonomy code.

### Enter/Edit Billing Information - Warning – Missing Lab or Facility Taxonomy Code – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System no longer provides a non-fatal warning message to users when a professional claim contains a Lab or Facility which has no active taxonomy code.

### Enter/Edit Billing Information - Print – TRICARE-specific Pay-to Provider – UB04 – TRICARE REIMB.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to print the TRICARE-specific Pay-to Provider data on a UB04 when the rate type of the claim is TRICARE REIMB.

### Enter/Edit Billing Information - Print – TRICARE-specific Pay-to Provider – UB04 – UB04 – TRICARE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to print the TRICARE-specific Pay-to Provider data on a UB04 when the rate type of the claim is TRICARE.

### Enter/Edit Billing Information - Print – TRICARE-specific Pay-to Provider – CMS 1500 – TRICARE REIMB.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to print the TRICARE-specific Pay-to Provider data on a CMS - 1500 when the rate type of the claim is TRICARE REIMB.

### Enter/Edit Billing Information - Print – TRICARE-specific Pay-to Provider – CMS 1500 – TRICARE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to print the TRICARE-specific Pay-to Provider data on a CMS - 1500 when the rate type of the claim is TRICARE.

### Enter/Edit Billing Information - Re-sequence Diagnoses/Maintain Pointers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to re-sequence a diagnosis code which has been associated with a procedure code(s) while maintaining the association (diagnoses pointers).

### Enter/Edit Billing Information - Value Code Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to view the list of available Value Codes by NUBC code number when users enter ?? for Help.

### Enter/Edit Billing Information - Value Code – External Code Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to lookup a Value Code by NUBC code number.

### Enter/Edit Billing Information - Occurrence Code Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to view the list of available Occurrence Codes by NUBC code number when users enter ?? for Help.

### Enter/Edit Billing Information - Occurrence Code – External Code Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to lookup a Occurrence Code by NUBC code number.

### Enter/Edit Billing Information - Condition Code Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to view the list of available Condition Codes by NUBC code number when users enter ?? for Help.

### Enter/Edit Billing Information - Condition Code – External Code Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to lookup a Condition Code by NUBC code number.

### Enter/Edit Billing Information - One-Time HPID – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to enter a one-time (the ID will not be stored in the Insurance Company file) Health Plan Identifier for the following payers when present on a professional claim:

- Primary
- Secondary
- Tertiary

### Enter/Edit Billing Information - One-Time HPID – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to enter a one-time (the ID will not be stored in the Insurance Company file) Health Plan Identifier for the following payer(s) when present on an institutional claim:

- Primary
- Secondary
- Tertiary

### Enter/Edit Billing Information - Line Level NDC Code Units to Non-Prescription Claims – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to add a line level number of units for each National Drug Code on a non-prescription procedure when creating a professional claim.

### Enter/Edit Billing Information - Line Level NDC Code Units to Non-Prescription Claims – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to add a line level number of units for each National Drug Code on a non-prescription procedure when creating an institutional claim.

## System Feature: Insurance Company Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Insurance Company Editor - Federal Employee Plan – Help Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System displays the following description for the Plan Type of FEP when users enter ?? for Help at the Electronic Plan Type field in Change Plan Info under View/Edit Plan:

- Do Not Use for BC/BS

## System Feature: Billing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Billing Reports - Sort - Re-generate Unbilled Amounts Report – Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to sort the Re-generate Unbilled Amounts Report by Division.

### Billing Reports - Display - Re-generate Unbilled Amounts Report – Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to display the Re-generate Unbilled Amounts Report by Division.

### Billing Reports - Print - Re-generate Unbilled Amounts Report – Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to print the Re-generate Unbilled Amounts Report by Division.

### Billing Reports - Display new HIPAA Compliant Fields on IB Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System retrieves the data for existing report fields on existing reports from the following new HIPAA length compliant fields:

- Sub-file 2.312
  - SUBSCRIBER ID – Maximum 80 A/N – 2.312, 7.02
  - NAME OF INSURED – Maximum 130 A/N – 2.312, 7.01
- Sub-file 2.3226
  - COMMUNICATION NUMBER – Maximum 245 A/N – 2.3226, 1
- Sub-file 355.3
  - GROUP NAME – Maximum 80 A/N – 355.3, 2.01
  - GROUP NUMBER – Maximum 55 A/N – 355, 2.02
- Sub-file 355.33
  - GROUP NAME – Maximum 80 A/N – 355.33, 90.01
  - GROUP NUMBER – Maximum 55 A/N – 355.33, 90.02
  - SUBSCRIBER ID – Maximum 80 A/N – 355.33, 90.03
  - NAME OF INSURED – Maximum 130 A/N – 355.33, 91.01
- Sub-file 365
  - NAME OF INSURED – Maximum 130 A/N – 365, 13.01
  - SUBSCRIBER ID – Maximum 80 A/N – 365, 13.02
  - GROUP NAME – Maximum 80 A/N – 365, 14.01
  - GROUP NUMBER – Maximum 55 A/N – 365, 14.02
- Sub-file 365.03
  - COMMUNICATION NUMBER 1 – Maximum 245 A/N – 365.03, 1
  - COMMUNICATION NUMBER 2 – Maximum 245 A/N – 365.03, 2
  - COMMUNICATION NUMBER 3 – Maximum 245 A/N – 365.03, 3
- Sub-file 365.26
  - COMMUNICATION NUMBER – Maximum 245 A/N – 365.26, 1.01

## System Feature: Third Party Joint Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Third Party Joint Inquiry - TPJI Visual Indicator – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System displays a visual indicator for each institutional claim on a claim list identifying the claim as institutional, when users access one of the following list in TPJI:

- Inactive Bills
- Third Party Active Bills

> **NOTE:** Maintains the current Inpatient/Outpatient indicator

### Third Party Joint Inquiry - TPJI Visual Indicator – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System displays a visual indicator for each professional claim on a claim list identifying the claim as professional, when users access one of the following lists in TPJI:

- Inactive Bills
- Third Party Active Bills

> **NOTE:** Maintains the current Inpatient/Outpatient indicator

### Third Party Joint Inquiry - Co-Payment Amount – TPJI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to view the co-payment amount when one is associated with a claim in TPJI.

## System Feature: COB Management Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### COB Management Worklist - Sort – COB Management Worklist – Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to sort the COB Management Worklist by Division.

### COB Management Worklist - Display – COB Management Worklist – Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to display the COB Management Worklist by Division.

### COB Management Worklist - Print – COB Management Worklist – Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to print the COB Management Worklist by Division.

## System Feature: Health Care Claim Transactions (837)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Health Care Claim Transactions (837) - Transmit HPID – Destination Payer – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the Health Plan Identifier for the destination payer in an institutional X12N 5010 Health Care Claim (837) transaction to FSC..

### Health Care Claim Transactions (837) - Transmit HPID – Destination Payer – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the Health Plan Identifier for the destination payer in a professional X12N 5010 Health Care Claim (837) transaction to FSC.

### Health Care Claim Transactions (837) - Transmit HPID – Other Payer(s) – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the Health Plan Identifier for the other payer(s) in an institutional X12N 5010 Health Care Claim (837) transaction to FSC.

### Health Care Claim Transactions (837) - Transmit HPID – Other Payer(s) – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the Health Plan Identifier for the other payer(s) in a professional X12N 5010 Health Care Claim (837) transaction to FSC.

### Health Care Claim Transactions (837) - Transmit Sole-Proprietorship NPI – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the same NPI for an individual provider and a non-VA lab or Facility in an institutional X12N 5010 Health Care Claim (837) transaction to FSC.

### Health Care Claim Transactions (837) - Transmit Sole-Proprietorship NPI – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the same NPI for an individual provider and a non-VA lab or Facility in a professional X12N 5010 Health Care Claim (837) transaction to FSC.

### Health Care Claim Transactions (837) - Transmit TRICARE-specific Pay-to Provider – Institutional – TRICARE REIMB.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the following TRICARE-specific Pay-to-Provider data in an institutional X12N 5010 Health Care Claim (837) transaction to FSC when the claim has a rate type of TRICARE REIMB.:

- NM101 – 87 - Required
- NM102 – Non-Person Entity - Required
- N301 – Pay-To Address Line - Required
- N302 – Pay-To Address Line - Situational
- N401 – Pay-To Address City – Required
- N402 – Pay-To Address State Code – Required in USA
- N403 – Pay-To Address Postal Zone or ZIP Code – Required in USA

### Health Care Claim Transactions (837) - Transmit TRICARE-specific Pay-to Provider – Institutional – TRICARE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the following TRICARE-specific Pay-to-Provider data for an institutional X12N 5010 Health Care Claim (837) transaction to FSC when the claim has a rate type of TRICARE:

- NM101 – 87 - Required
- NM102 – Non-Person Entity - Required
- N301 – Pay-To Address Line - Required
- N302 – Pay-To Address Line - Situational
- N401 – Pay-To Address City – Required
- N402 – Pay-To Address State Code – Required in USA
- N403 – Pay-To Address Postal Zone or ZIP Code – Required in USA

### Health Care Claim Transactions (837) - Transmit TRICARE-specific Pay-to Provider – Professional – TRICARE REIMB.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the following TRICARE-specific Pay-to-Provider data in a professional X12N 5010 Health Care Claim (837) transaction to FSC when the claim has a rate type of TRICARE REIMB.:

- NM101 – 87 - Required
- NM102 – Non-Person Entity - Required
- N301 – Pay-To Address Line - Required
- N302 – Pay-To Address Line - Situational
- N401 – Pay-To Address City – Required
- N402 – Pay-To Address State Code – Required in USA
- N403 – Pay-To Address Postal Zone or ZIP Code – Required in USA

### Health Care Claim Transactions (837) - Transmit TRICARE-specific Pay-to Provider – Professional – TRICARE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the following TRICARE-specific Pay-to-Provider data in a professional X12N 5010 Health Care Claim (837) transaction to FSC when the claim has a rate type of TRICARE:

- NM101 – 87 - Required
- NM102 – Non-Person Entity - Required
- N301 – Pay-To Address Line - Required
- N302 – Pay-To Address Line - Situational
- N401 – Pay-To Address City – Required
- N402 – Pay-To Address State Code – Required in USA
- N403 – Pay-To Address Postal Zone or ZIP Code – Required in USA

### Health Care Claim Transactions (837) - Transmit NDC Code – non-RX – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the following line level 5-4-2 format NDC in an institutional X12N 5010 Health Care Claim (837) transaction to FSC (Loop 2410):

- LIN02 – N4 – Required
- LIN03 – National Drug Code – Required

### Health Care Claim Transactions (837) - Transmit NDC Code – non-RX – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the following line level 5-4-2 format NDC in a professional X12N 5010 Health Care Claim (837) transaction to FSC (Loop 2410):

- LIN02 – N4 – Required
- LIN03 – National Drug Code – Required

### Health Care Claim Transactions (837) - Transmit NOC Procedures - Free Text Description – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit a line level 1-80 A/N procedure description in an institutional X12N 5010 Health Care Claim (837) transaction to FSC (Loop 2400):

- SV202-7 – Description - Situational

### Health Care Claim Transactions (837) - Transmit NOC Procedures – Free Text Description – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit a line level 1-80 A/N procedure description in a professional X12N 5010 Health Care Claim (837) transaction to FSC (Loop 2400):

- SV101-7 – Description – Situational

### Health Care Claim Transactions (837) - Transmit NDC Code Units– non-RX – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the following line level NDC unit count in an institutional X12N 5010 Health Care Claim (837) transaction to FSC (Loop 2410):

- CTP04 – National Drug Unit Count – Required
- CTP05 - 1 - Code Qualifier – UN (Units) – Required

### Health Care Claim Transactions (837) - Transmit NDC Code Units – non-RX – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit the following line level NDC unit count in a professional X12N 5010 Health Care Claim (837) transaction to FSC (Loop 2410):

- CTP04 – National Drug Unit Count – Required
- CTP05 - 1 - Code Qualifier – UN (Units) – Required

### Health Care Claim Transactions (837) - Transmit Maximum 12 Procedures – Inpatient/Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit a maximum of 12 procedure codes in an inpatient, institutional X12N 5010 Health Care Claim (837) transaction to FSC (Loop 2300 – HI01-2).

## System Feature: Copy and Cancel a Bill (CLON)/Correct Rejected/Denied Bill (CRD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Copy and Cancel a Bill (CLON)/Correct Rejected/Denied Bill (CRD) - CRD - Prevent Correction of Secondary Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from copying rejected/denied secondary claims using the Correct Rejected/Denied Bill option (CRD).

### Copy and Cancel a Bill (CLON)/Correct Rejected/Denied Bill (CRD) - CRD - Prevent Correction of Tertiary Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from copying rejected/denied tertiary claims using the Correct Rejected/Denied Bill option (CRD).

### Copy and Cancel a Bill (CLON)/Correct Rejected/Denied Bill (CRD) - CLON – Copy Secondary/Tertiary Claim Data to New Secondary/Tertiary Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to copy data from an original secondary/tertiary claim, including COB data from the electronic EOB(s) to a new claim using the Copy and Cancel a Bill (CLON) option.

### Copy and Cancel a Bill (CLON)/Correct Rejected/Denied Bill (CRD) - CRD – Copy Primary Claim Data to New Primary Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to copy data from an original primary claim to a new claim using the Correct Rejected/Denied Bill (CRD) option.

### Copy and Cancel a Bill (CLON)/Correct Rejected/Denied Bill (CRD) - CRD – Prevent Correction of Claim in MRA Request Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from copying an MRA claim in an MRA Request status using the Correct Rejected/Denied Bill option (CRD).

## System Feature: Provider ID Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Provider ID Maintenance - Sole-Proprietorship Designation - non-VA Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to designate a non-VA Facility as a sole-proprietorship.

### Provider ID Maintenance - Link non-VA Facility to Sole-Proprietor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to link a non-VA Facility that is a sole-proprietorship to an individual provider.

### Provider ID Maintenance - Sole-Proprietorship non-VA Facility – NPI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to enter an NPI number for a non-VA Facility that is defined as a sole-proprietorship that has previously been entered for an individual provider.

## System Feature: MCCR Site Parameter Display/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MCCR Site Parameter Display/Edit - Default TRICARE Pay-to Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to define a default Pay-to Provider for TRICARE claims with the following data:

- Pay-to Provider from the Institution file
- Pay-to Provider Name – default from Institution file
- Pay-to Provider Address Line 1 – default from Institution file
- Pay-to Provider Address Line 2 – default from Institution file
- Pay-to Provider City – default from Institution file
- Pay-to Provider State – default from Institution file
- Pay-to Provider Zip Code – default from Institution file
- Pay-to Provider Phone Number:
- Pay-to Provider Federal Tax ID Number
- Default Flag

### MCCR Site Parameter Display/Edit - Default TRICARE Pay-to Provider Associations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System automatically associates all divisions of the VAMC with the default TRICARE Pay-to Provider.

### MCCR Site Parameter Display/Edit - Additional TRICARE Pay-to Providers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to define additional non-default Pay-to Providers for TRICARE claims with the following data:

- Pay-to Provider from the Institution file
- Pay-to Provider Name – default from Institution file
- Pay-to Provider Address Line 1 – default from Institution file
- Pay-to Provider Address Line 2 – default from Institution file
- Pay-to Provider City – default from Institution file
- Pay-to Provider State – default from Institution file
- Pay-to Provider Zip Code – default from Institution file
- Pay-to Provider Phone Number:
- Pay-to Provider Federal Tax ID Number
- Default Flag

### MCCR Site Parameter Display/Edit - Associate Division(s) with TRICARE Pay-to Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to re-associate one or more divisions of the medical center with additional non-default Pay-to Providers for TRICARE claims.

### MCCR Site Parameter Display/Edit - Edit a TRICARE Pay-to Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to edit a TRICARE Pay-to Provider.

### MCCR Site Parameter Display/Edit - Delete a TRICARE Pay-to Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to delete a TRICARE Pay-to Provider.

### MCCR Site Parameter Display/Edit - Re-associate Divisions - Delete TRICARE Pay-to Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System automatically re-associates all divisions associated with a deleted TRICARE Pay-to Provider with the default provider.

### MCCR Site Parameter Display/Edit - Re-associate Divisions - TRICARE Pay-to Provider Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides a Security Key to allow users to access the capability to define TRICARE Pay-to Provider(s).

### MCCR Site Parameter Display/Edit - Re-associate Divisions - Pay-to Provider Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides a Security Key to allow users to access the capability to define Pay-to Provider(s).

## System Feature: View Cancelled Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### View Cancelled Claim - View Cancelled Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to view the non-computed data stored in the Bill/Claim file (file 399) for a Cancelled claim.

## System Feature: Miscellaneous Existing Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Miscellaneous Existing Requirements - *Correct* - FEAT604 Transmit Property and Casualty Claim Number 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB system transmits the following data with a Professional 837 claim transmission only when a Property/Casualty Claim Number is present on a claim (2010CA REF01, REF02):

- Y4 - Agency Claim Number Qualifier
- Property Casualty Claim Number

### Miscellaneous Existing Requirements - *Delete* – FEAT435 VAMC as Billing Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA IB system provides the ability for authorized users to designate by insurance company and form type, that the Billing Provider will always be the main facility (VAMC) on claims to the payer.

### Miscellaneous Existing Requirements - *Change* – FEAT102 EDI Parameter Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vista system provides the ability for users to view a report which includes the contents of the following fields in the Insurance Company file for all active entries:

- Insurance Company Name; and
- Insurance Company Address (Line 1, City and State); and
- Electronic Type; and
- Type of Coverage; and
- Electronic Transmit?; and
- Inst Electronic Bill ID; and
- Prof Electronic Bill ID; and
- Inst Use VAMC as Billing Provider - Delete
- Prof Use VAMC as Billing Provider – Delete
- HPID(s) - Add
- OEID(s) – Add

### Miscellaneous Existing Requirements - *Delete* – FEAT443 Schedule Mailman Message/Payer Settings for Billing Provider/Service Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vista system provides the ability for users to schedule the task to generate the mailman message that reports a site's settings in the Insurance Company Editor for the Billing Provider/Service Facility parameters.

### Miscellaneous Existing Requirements - *Delete* – FEAT444 Default Schedule Mailman Message/Payer Settings for Billing Provider/Service Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vista system automatically sets the default frequency for the task to generate the mailman message that reports a site's settings in the Insurance Company Editor for the Billing Provider/Service Facility parameters, upon installation of the patch, to one time per month.

### Miscellaneous Existing Requirements - *Delete* – FEAT445 Mailman Message with Payer Settings/Billing Provider/Service Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vista IB system generates a mailman message that reports a site's settings in the Insurance Company Editor for the Billing Provider/Service Facility parameters, when at least one of the Always use main VAMC as Billing Provider parameters is set to 'Yes', which includes the following data:

- Insurance Company Name; and
- Insurance Company Address; and
- Date of Report; and
- Station ID; and
- Electronic Transmit; and
- Inst Electronic Bill ID; and
- Prof Electronic Bill ID; and
- Inst Use VAMC as Billing Provider; and
- Prof Use VAMC as Billing Provider.

### Miscellaneous Existing Requirements - *Delete* – FEAT446 Mailman Message with Payer Settings/Billing Provider/Service Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vista IB system generates an mailman message that reports a site's settings in the Insurance Company Editor for the Billing Provider/Service Facility parameters, when both of the Always use main VAMC as Billing Provider parameters is set to 'No', which includes the following data:

- Date of Report; and
- Station ID

### Miscellaneous Existing Requirements - *Delete* – FEAT573 Security Key for Copy_Cancel a Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB system provides the ability for authorized users to assign a security key to a user which will allow them to use the existing Clon – Copy/Cancel a Claim option \[IB COPY AND CANCEL\].

### ### ### ### ### ### ##
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: IB*2*528 Release Notes

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software being released as a host file and/or documentation describing the new functionality introduced by this patch are available.

The preferred method is to retrieve files from download.vista.med.va.gov. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server. Sites may retrieve the software and/or documentation directly using Secure Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

Albany <span class="mark">REDACTED</span>

Hines <span class="mark">REDACTED</span>

Salt Lake City <span class="mark">REDACTED</span>

Documentation can also be found on the VA Software Documentation Library at: http://www4.va.gov/vdl/

The documentation will be in the form of Adobe Acrobat files.

File Description File Name FTP Mode

-------------------------------------------------------------------------------------------------------------------------

Integrated Billing User Manual IB_2_0_UM.PDF (binary)

Integrated Billing Technical Manual/ IB_2_0_TM.PDF (binary)

Security Guide

Integrated Billing Release Notes IB_2_0_P528_RN.PDF (binary)

Electronic Insurance Verification (eIV) IB_2_0_EIV_TM.PDF (binary)

Technical Manual/Security Guide

Electronic Insurance Verification (eIV) User Manual IB_2_0_EIV_UG.PDF (binary)

## Technical Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### SSVI - Data Source/Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The updated insurance information will reside in the site's existing VistA database where the patient has been seen and optionally transferred to those subscribing VA sites via Remote Query. Those subscribing sites will receive then store the updated information within their VA VistA database until processed.

Three files have been created. IB INSURANCE CONSISTENCY ELEMENTS (#366.2) contains the fields or categories to be checked for inconsistencies following an editing session of the insurance edit option information. IB INSURANCE INCONSISTENT DATA (#366.1) is a storage area for all the fields or categories that have been recently found to be inconsistent. IB SSVI PIN/HL7 PIVOT (#366) is a storage area for all the remote query transaction information.

The project will allow the processing/sending of updated patient insurance information via Remote Query messaging. The user will set a flag to have the option of transmitting any updated patient insurance information.

\*\*\*Note:

The newly added software application System Sharing Verified Insurance (SSVI) Parameter in the eIV Site Parameters is set to OFF during the install. DO NOT TURN SSVI ON. This patch will install all necessary source code, data dictionaries, options, templates etc. for the SSVI application, however, this feature should be set to OFF so as to not initiate the SSVI feature. This feature will be modified in future IB projects with instructions on how to use this newly added feature.

\*\*\*Note:

The newly added software application Consistency Checker source code that uses the options Patient Insurance Info View/Edit (PI)--\> Verify Coverage (VC) is now disabled ('commented out') so as to not use the "Consistency Checker" source code to verify coverage. This feature will be modified within future IB projects with instructions on how to use this newly added Consistency Checker feature in conjunction with the SSVI feature. DO NOT ENABLE THE SSVI UTILITY.

### Eligibility Benefits and Claims Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Eligibility Benefits and Claims Status Data Content and Infrastructure (Phase 2, Iteration 2) project task will create enhancements to the VA VistA system utilizing the IB Version 2.0 software application.

Enhancements will include the creation/modifications of existing Insurance screens/menus/options/templates/files.

1.  A newly created Subscriber screen will display a side-by-side comparison of the Insurance Verification Processor buffer information against the patient's Subscriber information found in sub-file (#2.312) Insurance Type File of the Patient File (#2).
2.  A newly created Annual Benefits screen will allow the user to View/Edit/Save the patient annual benefits found within file (#355.4) Annual Benefits File.
3.  A newly created Coverage Limitations screen will allow the user to View/Edit/Save the patient coverage limitations data found within file (#355.32) Plan Coverage Limitations File.
4.  Standardization of certain insurance subscriber display field names from "Insured (Person)" or "Patient" to "Subscriber".

### Security Key Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updates will be made to IB Insurance security keys.

1.  The post-install routine for this patch will rename the IBCNE IIV AUTOMATCH security key to IBCNE EIV MAINTENANCE and assign it as appropriate.
2.  The renamed IBCNE EIV MAINTENANCE key will be assigned to the IBCNE PAYER MAINTENANCE MENU and its options IBCNE PAYER EDIT and IBCNE PAYER LINK, replacing the IB INSURANCE SUPERVISOR lock on these options.
3.  The renamed IBCNE EIV MAINTENANCE key will be assigned to the IBCNSC INS CO PAYER protocol, i.e., the Payer Action (PA) on the IBCN INSURANCE CO EDIT option.

### Eligibility Benefits and Claims Patient Policy Information Screen – Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enhancements made to the patient policy comments displayed in the Patient Policy Screens.

Option: Patient Insurance Info/Edit (PI)

Software modifications made to the VP View Policy action located on the

Patient Policy Information screen include:

1.  Retrieval of comment data from the new COMMENT - SUBSCRIBER POLICY multiple (2.312, 1.18).
2.  Display of comments in Comment -- Patient Policy region.

Affected Options:

Patient Insurance Info/Edit \[IBCN PATIENT INSURANCE\]

Third Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]

View Patient Insurance \[IBCN VIEW PATIENT INSURANCE\]

Claims Tracking Edit \[IBT EDIT BI TRACKING ENTRY\]

Software modifications made to the AC Add Comment action on the Patient Policy Information screen include:

1.  Provides the capability for the user to enter up to 250 characters of comments
2.  Provides the capability for the user to edit previously entered comments entered on the same day
3.  The user-entered comments, the date/time that the comment was entered/edited, and the user ID (DUZ) gets stored in the respective fields of the COMMENT - SUBSCRIBER POLICY multiple (2.312, 1.18):

> COMMENT DATE/TIME (2.342,.01)

> LAST EDITED BY (2.342,.02)

> COMMENT (2.342,.03)

4.  Due to the authorized usage of the existing COMMENT PATIENT POLICY field (2.312, 1.08) by other applications (ICRs), the old comment field and the new comment multiple are to be populated until the IA subscribers have made the necessary changes to their applications to reference the new fields at the 2.312, 1.18 multiple. To that end the following DD definitions were made:
1.  Trigger cross-reference was defined to the COMMENT field (2.342, .03) that will populate the COMMENT PATIENT POLICY field (2.312, 1.08) when data is entered/edited at the COMMENT field (2.342, .03).
2.  Mumps cross-reference was defined to the COMMENT PATIENT POLICY field (2.312, 1.08) that will populate the fields at the COMMENT SUBCRIBER POLICY multiple only when both the old and the new comment field is different.

Affected Options:

Patient Insurance Info/Edit \[IBCN PATIENT INSURANCE\]

Third Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]

View Patient Insurance \[IBCN VIEW PATIENT INSURANCE\]

Claims Tracking Edit \[IBT EDIT BI TRACKING ENTRY\]

### Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several new reports will be added to the IB menus and existing reports will be updated.

1.  A new report will be created to capture Group Plans without annual benefits for a requested year.
2.  An audit report will be created to monitor changes to four IB insurance-related files.
3.  A new report will be created to capture outgoing and incoming HL7 messages between VistA and the Financial Services Center (FSC).
4.  Two new fields, "FSC Trusted?" and "Number of Active Groups", will be added to the eIV Payer Link Report. (The "HPID/OEID" field was added in IB\*2.0\*521.)
5.  A new submenu will be created to display all insurance-related reports under one menu.
6.  IB reports will be enhanced to enable output to Excel spreadsheets.

## Issue Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is associated with the following NSRs:

- 180833
- 20110215
- 20120118

### Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no Remedy Tickets associated with this patch.

### From: IB*2*488 Release Notes

### Enter/Edit Billing Information - Remove Force Print at HCCH – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System no longer provides the ability for users to add the value equal to Force Clearing House Print to an institutional electronic claim that forces the claim to be printed at the HCCH.

### Enter/Edit Billing Information - Remove Force Print at HCCH – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System no longer provides the ability for users to add the value equal to Force Clearing House Print to a professional electronic claim that forces the claim to be printed at the HCCH.

### Enter/Edit Billing Information - Fatal Error for PRNT Values – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from Authorizing an Institutional claim with a Primary Payer ID equal to one of the following:

- HPRNT
- SPRNT
- IPRNT
- PPRNT

### Enter/Edit Billing Information - Fatal Error for PRNT Values – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from Authorizing a professional claim with a Primary Payer ID equal to one of the following:

- SPRNT
- HPRNT
- IPRNT
- PPRNT

### Enter/Edit Billing Information - Fatal Error for No Procedures – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from Authorizing a professional claim that contains no Procedure Codes.

### Enter/Edit Billing Information - Fatal Error for No Procedures – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from Authorizing an outpatient, institutional claim that contains no Procedure Codes.

## System Feature: Provider Maintenance 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Provider Maintenance - Outside Facility ZIP Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to enter ONLY a 9 - 10 character value for the ZIP Code in Non-VA FacilityLab/Facility InfoZip Code (999999999/99999-9999).

### Provider Maintenance - Outside Facility Address Line 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability for users to enter ONLY a physical street address value (no Post Office Box) for the first line of the street address in Non-VA FacilityLab/Facility InfoStreet Address.

## System Feature: Insurance Company Entry/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Insurance Company Entry/Edit - Payer Primary ID – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from defining the Inst Payer Primary ID as one of the following:

- HPRNT
- SPRNT
- IPRNT
- PPRNT

### Insurance Company Entry/Edit - Payer Primary ID – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prevents users from defining the Prof Payer Primary ID as one of the following:

- SPRNT
- HPRNT
- IPRNT
- PPRNT

### Insurance Company Entry/Edit - Value for EDI – Transmit? – New Ins. Co.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System sets the value for the Transmit Electronically field (File 36, field 3.01) equal to YES – LIVE when users create a new Insurance Company in File 36.

## System Feature: MRA Management Worklist (MRW)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MRA Management Worklist (MRW) - Display Message Storage Errors in MRW

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System displays Medicare-equivalent Remittance Advice (MRA) message storage errors for Medicare claims in the MRA Management Worklist in a human readable format.

### Third Party Joint Inquiry (TPJI) - Display Message Storage Errors in TPJI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System displays X12N 5010 Health Care Claim Payment/Advice (835) message storage errors for non-Medicare and Medicare claims in TPJI in a human readable format.

## System Feature: CMS – 1500 Printed Claim Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CMS – 1500 Printed Claim Form - Obsolete CMS – 1500 Data Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System no longer prints the following information on a locally printed CMS – 1500 claim form:

- Box 8

> o Patient Marital Status

> o Patient Employment

> o Patient Student Status

- Box 9

> o 9b – Other Insured's DOB

> o 9b – Other Insured's Gender

> o 9c – Employer's Name

> o 9c – School Name

- Box 11

> o 11b – Employer's Name

> o 11b – School Name

- Box 19

> o EPSDT Flag

> o Attending Not Hospice Employee

> o Homebound Indicator

> o Special Program Indicator

> o Date Last Seen

- Box 30 – Balance Due

### CMS – 1500 Printed Claim Form - New/Changed CMS – 1500 Data Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System prints the following data on a locally printed CMS – 1500 claim form when available on a professional claim:

- Box 10
  - 10d – NUCC designated Claim Condition Codes
- Box 11
  - 11b – Other Claim ID = Qualifier Y4 and Property and Casualty Number
- Box 14 – Date Qualifier
  - 484 Last Menstrual Period (LMP), or
  - 431 Onset of Current Symptoms or Illness if no date for LMP
- Box 15 – Date Qualifier
  - 439 Accident (Occurrence Codes)
  - 455 Last X-ray (Chiropractic Claim)
  - 453 Acute Manifestation of Chronic Condition (Chiropractic Claims)
  - 471 Prescription (RX Claims)
  - Initial Treatment (Occurrence Code – PT/OT/Speech/Home IV/Cardiac Rehab)
  - Latest Visit or Consultation
- Box 17 – Provider Qualifier
  - DN – Referring Provider
  - DQ – Supervising Provider
- Box 19 – Rate Type = Worker's Comp.:
  - PWK
  - Report Type Code
  - Transmission Type Code
  - Attachment Control Number
- Box 19 – Rate Type not equal to Worker's Comp.
  - Free Text – Maximum 71 characters
- Box 21
  - 21A-L – Up to 12 Diagnoses Codes
  - ICD Version Indicator
- Box 24E
  - Diagnoses Pointers will be A-L values

### Health Care Claim Transactions (837) - 12 Diagnoses (DXs) – Professional Claim

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit 1-12 diagnostic codes (DC1 – DC12) on a professional X12N 5010 Health Care Claim (837) transaction to FSC.

### Health Care Claim Transactions (837) - Service Line Charge Amount

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit a Service Line Charge Amt (INS, Piece 9) with a maximum length equal to 18 numeric in an institutional X12N 5010 Health Care Claim (837) transaction to FSC.

### Health Care Claim Transactions (837) - Service Line Non-Covered Charge Amount

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit a Service Line Non-Covered Charge Amt (INS, Piece 12) with a maximum length equal to 18 numeric in an institutional X12N 5010 Health Care Claim (837) transaction to FSC.

### Health Care Claim Transactions (837) - Transmit Workman's Compensation Claims – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit an institutional claim with a Rate Type equal to Worker's Comp. to FSC in an X12N 5010 Health Care Claim (837) transaction.

### Health Care Claim Transactions (837) - Transmit Workman's Compensation Claims – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit a professional claim with a Rate Type equal to Worker's Comp. to FSC in an X12N 5010 Health Care Claim (837) transaction.

### Health Care Claim Transactions (837) - Assignment Code – Institutional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System transmits an Assignment Code with the value of A in all institutional X12N 5010 Health Care Claim (837) transactions to FSC.

### Health Care Claim Transactions (837) - Assignment Code – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System transmits an Assignment Code with the value of A in all professional X12N 5010 Health Care Claim (837) transactions to FSC.

### Health Care Claim Transactions (837) - Diagnoses Pointers – Professional

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System provides the ability to transmit 2 A/N diagnoses pointers with diagnoses on a professional claim to FSC in an X12N 5010 Health Care Claim (837) transaction.

## System Features: Miscellaneous Existing Requirements 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Miscellaneous Existing Requirements – *Correct -* FEAT765 Functional Requirement: Transmit Revenue/Procedure Codes with Zero Charge Amount

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB System transmits Revenue/Procedure codes which generate zero charge amounts in 837 Health Care Claim Transmissions (PRF, Piece 5 and INS, Piece 9).

### Miscellaneous Existing Requirements – *Delete* – FEAT 602 Functional Requirement: Transmit Service Facility Contact Data 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB system transmits the following data with a Professional 837 claim transmission when an Service Facility Communication Number is present on a claim (2310C PER01, PER03):

- Contact Function Code: IC Information Contact
- Communication Number Qualifier: TE Telephone
- Communication Number: Telephone
- Communication Number Qualifier: EX Telephone Extension
- Communication Number: Extension Number

\*\*\*NOTE\*\*\* We will continue to transmit the Property and Casualty data entered on Billing Screen 8. The above fields will be relabeled as Property and Casualty data but will not be transmitted in the Service Facility loop.

###

### From: IB*2*519 Release Notes

## System Feature: HL7 Messages Inbound

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HL7 Messages Inbound – Maintain the Insurance Company Name in the Insurance Company file (#36) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The insurance company name in the Insurance Company File (#36) is NOT updated using the data from the NIF.

### HL7 Messages Inbound – The HPID/OEID Field to Be Viewable Only in the Insurance Company file (#36)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HPID/OEID field is viewable but non-editable in VistA in the Insurance Company file (#36). Any changes to HPID/OEID are made in the NIF so that they may be distributed to all VAMCs.

### HL7 Messages Inbound – Store the HPID in the Insurance Company file (#36)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system stores the HPID in the Insurance Company file (#36). The HPID is a 10-digit, all-numeric identifier which follows the ISO (International Organization for Standardization) Standard 7812 format with a Luhn check-digit as the tenth digit. The start digit of the HPID signals whether the identifier has been provided to a health plan or to an "other entity". If the start digit is a seven (7) then it identifies a health plan, a six (6) indicates an "other entity".

### HL7 Messages Inbound – Store the Other Entity Identifier (OEID) in the Insurance Company file (#36)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system stores the Other Entity Identifier (OEID) in the Insurance Company file (#36). The OEID serves as the identifier for entities that are not health plans, healthcare providers, or individuals (persons) who are not eligible for the HPID or National Provider Identifier (NPI), yet they need to be identified in standard transactions and for other lawful purposes. The Other Entity Identifier begins with a six (6).

### HL7 Messages Inbound – Distinguish Between HPID and OEID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system maintains a field to distinguish between an HPID identifier and an OEID identifier. <u>Note</u>: HPID is used for patient specific health plan product or benefit plan; OEID is used for organizations that perform the health plan function or other entity that performs certain administrative or contracting functions on behalf of the health plan.

### HL7 Messages Inbound – Ability to Define the HPID as Either a Controlling Health Plan (CHP) or Subhealth Plan (SHP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system defines the VistA Insurance Company file (#36) entry as either the Controlling Health Plan (CHP) or Subhealth Plan (SHP).

<u>Note:</u> CHP is a health plan that controls its own business activities, actions, or policies. Can have 0 to many subhealth plans associated to it. SHP is a health plan whose business activities, actions, or policies are directed by a CHP.

### HL7 Messages Inbound – Associate the Legacy Identifiers to the New HPID/ OEID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system associates the new HPID/OEID data element with the legacy identifiers representing a given health plan so there will be a linkage between old and new.

<u>Note</u>: A HPID/OEID may be linked to more than one legacy ID and there may be multiple HPID/OEID entries linked to a single legacy ID.

### HL7 Messages Inbound – Retain Patient Policy Functionality with Respect to the Patient File (#2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system retains the functionality to associate patients to their policies, and maintain the necessary information on electronic transmissions so that FSC retains the ability to route files to the correct payer system.

### HL7 Messages Inbound – Maintain the Existing EDI Professional and EDI Institutional Legacy 20-Byte Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system provides the ability for VistA to maintain the existing (legacy) 20 byte data field, for the EDI Professional and the EDI Institutional.

<u>Note:</u> Fields are as follows: File \#36, field \#3.02 EDI ID NUMBER-PROF and File \#36 field \#3.04 EDI ID NUMBER-INST.

### HL7 Messages Inbound – Continue to Store the Legacy Electronic Payer ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system provides the ability for VistA to continue to store the legacy electronic Payer ID.

### HL7 Messages Inbound – Load the HPID/OEID into the local Insurance Company File (#36) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system loads the HPID into the local Insurance Company file (#36) based on the INSID from the original seeding of the NIF from VistA.

<u>Note:</u> INSID is a unique insurance company ID from VistA. It is a combination of the site's number and the internal record number in file \#36.

### HL7 Messages Inbound – Receive and Process a HPID/OEID from FSC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system provides the ability for VistA to receive and process HPID/OEID into file \#36 upon receipt of an update from FSC based on changes to the NIF. An INSID consisting of a site ID and IEN is used so that updates are only stored at sites with systems already containing a given payer.

### HL7 Messages Inbound – Modify the Insurance Company View Screen to Include the HPID/OEID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Insurance Company View Screen includes the HPID/OEID. This field is view only.

## System Feature: HL7 Messages Outbound

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HL7 Messages Outbound - Allow Messages to be Exchanged between VistA and the NIF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system provides the ability for VistA to use an interface to send and receive messages to/from the NIF, regardless of who initiates the message.

<u>Note:</u> VistA receives and stores a NIFID (National Insurance File ID).

### HL7 Messages Outbound - Send Updates to the NIF for New Group/Plans Entered in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system provides the ability for VistA to use an interface to send a message containing insurance company information to the NIF, when a new Group/Plan is entered into VistA, and it is a new Insurance Company.

<u>Note:</u> VistA receives and stores a NIFID.

### HL7 Messages Outbound - Send Updates to the NIF for Insurance Companies Modified in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system provides the ability for VistA to use an interface to send a message containing insurance company information to the NIF, when a VistA/NIF exchanged field associated with an insurance company is modified in VistA.

## System Feature: Data Extract

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Data Extract - Create Data Extract Files from Each VAMC to FSC for Initial Seeding of NIF

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data extracts are created from each VAMC's VistA system using data from the Insurance Company (#36) file and sent to the FSC for initial seeding of the NIF. VistA only sends active insurance companies.

### From: IB*2*458 Release Notes

## CLAIMS TRACKING DENIAL REASONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Insurance Review that results in a Denial is assigned a reason for that denial from a standard set of reasons. New entries are being added to this standard set of Insurance Review Denial Reasons.

| New CLAIMS TRACKING DENIAL REASONS (#356.21): |          |
|-----------------------------------------------|----------|
| DELAY IN TREATMENT/SERVICE                    | DELAY TX |
| OBSERVATION IS MORE APPROPRIATE               | OBS      |
| ALTERNATE LEVEL OF CARE IS MORE APPROPRIATE   | ALT LOC  |

## CLAIMS TRACKING REVIEW TYPES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each Insurance Review is assigned a Type identifying both the type of care and the type of review. New entries are being added to the standard set of Insurance Review Types.

| New CLAIMS TRACKING REVIEW TYPE (#356.11): |     |            |
|--------------------------------------------|-----|------------|
| SNF/NHCU REVIEW                            | 25  | SNF/NHCU   |
| INPT RETROSPECTIVE REVIEW                  | 35  | RETRO INPT |
| OPT RETROSPECTIVE REVIEW                   | 55  | RETRO OPT  |

<u>Display and Edit with New Review Types:</u>

The Insurance Review Types are used as controls when processing the fields of an Insurance Review to determine the data related to that review. For example the fields displayed and editable for a URGENT/EMERGENT ADMIT REVIEW are different than the fields displayed and editable for an OUTPATIENT TREATMENT review. The new Review Types will manage review data in the same way as existing similar Review Types:

SNF/NHCU REVIEW processed same as a URGENT/EMERGENT ADMIT REVIEW

INPT RETROSPECTIVE REVIEW processed same as a URGENT/EMERGENT ADMIT REVIEW

OPT RETROSPECTIVE REVIEW processed same as a OUTPATIENT TREATMENT Review

## CLAIMS TRACKING REASONS NOT BILLABLE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each event in Claims Tracking may be assigned a Reason Not Billable to indicate the event is not billable and why. The standard list of Reasons Not Billable is being updated, one entry is changed and several added.

<u>Update CLAIMS TRACKING NON-BILLABLE REASONS (#356.8):</u>

The name of one Reason Not Billable is being changed.

NPI/TAXONOMY ISSUES changed to NPI/TAXONOMY/PPN ISSUES

<u>New CLAIMS TRACKING NON-BILLABLE REASONS (#356.8):</u>

| New CLAIMS TRACKING NON-BILLABLE REASONS (#356.8): |      |           |                 |
|----------------------------------------------------|------|-----------|-----------------|
| NAME                                               | CODE | ECME FLAG | ECME PAPER FLAG |
| APPT CANCELLED/PT NOT SEEN                         | MC20 |           |                 |
| SEEN BY PROVIDER ON SAME DAY                       | MC21 |           |                 |
| NON-BILLABLE DME/PROSTHETIC                        | MC22 |           |                 |
| NON-BILLABLE PROCEDURE                             | MC23 |           |                 |
| EMPLOYEE HEALTH                                    | MC24 | Yes       | No              |
| ENCOUNTER DURING INPT STAY                         | MC25 |           |                 |
| NO PROSTHETIC COVERAGE                             | CV22 |           |                 |
| NON-COVERED DIAGNOSIS                              | CV23 |           |                 |
| NON-COVERED ROUTINE CARE                           | CV24 |           |                 |
| HDHP PLAN NOT BILLED                               | CV25 | Yes       | No              |
| NOT RELATED TO WC/TORT/NF                          | CV26 |           |                 |
| TRICARE PT SEEN AS VETERAN                         | CV27 | Yes       | No              |
| COMBINED CHARGES                                   | BL08 |           |                 |
| UNBUNDLED SERVICE                                  | BL09 |           |                 |

## CLAIMS TRACKING INSURANCE REVIEW CALL REFERENCE AND AUTHORIZATION NUMBER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The INSURANCE REVIEW file CALL REFERENCE NUMBER (#356.2, .09) and AUTHORIZATION NUMBER (#356.2, .28) fields are both being expanded to 35 characters.

<u>Fields Moved:</u>

Due to the additional length required these fields have been moved in the INSURANCE REVIEW file (#356.2). Two new fields are being added as replacements and the two existing fields inactivated:

INSURANCE REVIEW (#356.2) file:

- \#.09 CALL REFERENCE NUMBER (15chr) moved to \#2.01 CALL REFERENCE NUMBER (35chr)
- \#.28 AUTHORIZATION NUMBER (18chr) moved to \#2.02 AUTHORIZATION NUMBER (35chr)

<u>Data Copied:</u>

The data in the inactivated fields will be moved to the new fields so there should be no change from the user perspective except the expanded number of characters available.

<u>Data Display:</u>

These two fields are displayed on several Claims Tracking screens and reports. If the number of characters available is too short to display the full extended length then the data will be truncated. A '\*' will be appended to the end of the data to indicate the full data is not displayed. See Example Screens Section.

<u>Call Reference Number as Default:</u>

When a new Insurance Review is created and a Call Reference Number is entered then it is used as the default value for the Authorization Number. This default has been removed. Now when the Authorization Number is presented the Authorization Number of a previous Insurance Review for the event will be used as the default. If there was no previous Insurance Review Authorization Number then no default will be presented.

## CLAIMS TRACKING RELEASE OF INFORMATION SPECIAL CONSENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Release of Information (ROI) function within Claims Tracking has been enhanced to include records of the ROI consents received and the sensitive condition they cover.

Currently each event in Claims Tracking may be assigned a Special Consent ROI: Not Required, Obtained, Required, and Refused. This indicates if that specific event may be related to a sensitive condition requiring a Release of Information consent form from the patient. The new option will now allow entry of a record indicating a consent form has been received for a specific sensitive condition.

<u>New CLAIMS TRACKING ROI CONSENT (#356.26) file:</u>

A new file has been created for records of Release of Information obtained from a patient with the following. Note that each sensitive condition will have its own record.

- PATIENT the consent was received from.
- SENSITIVE CONDITION the consent for release covers. Includes the four standard sensitive conditions requiring ROI:
  - DRUG ABUSE
  - ALCOHOLISM/ALCOHOL ABUSE
  - TESTING FOR OR INFECTION WITH HIV
  - SICKLE CELL ANEMIA
- The EFFECTIVE DATE when the consent for release begins.
- The EXPIRATION DATE when the consent for release ends.
- A REVOKED flag indicating the patient revoked the consent. In this case the Expiration date is updated to the date the revocation becomes effective. A consent may be revoked but will be active for the date range assigned.
- COMMENTS associated with ROI, this is intended primarily for entry of the Insurance the release consent covers.

<u>View Patient ROI Special Consent Records:</u>

A new screen has been added to display and manage the ROI consent records. This screen has been added as an action on the main Claims Tracking Editor screen: ROI Consent (RO). See Example Screens Section.

The ROI Special Consent screen will display all ROI consents entered for the Patient. The display order is currently active ROIs first then in reverse effective date order. Most recent active ROIs will be at the top. The Patient, effective date, expiration date and sensitive condition are all displayed. In addition, a flag will indicate which consents are currently active, inactive or inactive/revoked. The comments are displayed; however due to space limitations these are truncated. Use the '\>' to shift the view to the right to see the entire comment field, '\<' shift the view back to the left.

Option: Claims Tracking Edit \[IBT EDIT TRACKING ENTRY\], ROI Consent (RO)

<u>Add/Edit ROI Special Consent Records for a Patient:</u>

Actions associated with the new Claims Tracking Editor screen for ROI Special Consent:

- Add ROI Consent (AR) will allow new entries to be added.
- Edit ROI (ER) will allow edit of existing entries.
- Revoke ROI (RV) will allow an ROI consent to be flagged as revoked by the patient. The Expiration date must be updated to the date the revocation takes effect.
- Delete ROI (DR) will allow a ROI record to be deleted. This should only be used if the record was entered in error. Old records that expired should remain.

Users must be assigned the new IB ROI EDIT Security Key to perform any of these actions or to modify the ROI records.

Security Key: IB ROI EDIT (new)

<u>Updates to Claims Tracking Displays for ROI:</u>

Several Claims Tracking screens and reports have been updated to show indicators of the patients active ROI consent, if any.

The main Claims Tracking Editor screen is the list of a patient's events within a timeframe. This screen has been modified in two ways:

- Header of this screen will show indicators of the patient's sensitive conditions that have currently active consents, if any: ROI: AHS
- Each event in the list displays the Special Consent ROI field associated with that event (Not Required, Obtained, Required, Refused). If the Special Consent ROI is Obtained then indicators of the sensitive conditions that have active consents on the date of the event will be appended to the field: OBTAIN(AS)

Several other screens will have the following change to the header depending on the type of screen display:

- Headers of screens that display lists of a patient's events will show indicators of the patient's sensitive conditions that have currently active consents, if any: ROI: AHS.
- Headers of screens that display the extended data of a particular event and have Special Consent ROI set to Obtained will have indicators of the sensitive conditions that have consents active on the date of the event appended: ROI: OBTAINED (AS).

<u>ROI Expired Consent Report:</u>

A new report will list the ROI Special Consents that will expire within a user specified date range. This report has been added to the Management Reports (Billing) Menu.

Option: ROI Expired Consent \[IB OUTPUT ROI EXPIRED\] (new)

Menu: Management Reports (Billing) Menu \[IB OUTPUT MANAGEMENT REPORTS\]

## DAYS DENIED REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Days Denied report lists Inpatient stays that have a Denial Insurance Review. Significant updates have been made to the Days Denied Report:

- The charges displayed as the Amount Denied has been update to the current active charges, Reasonable Charges.
- Social Security Number has been removed and replaced with the last 4.
- The Inpatient Admission's Service is added to each denied stay in the detail section. This is the Service the patient was in at either the admission, if that date is included in the report, or the Service the patient was in on the begin date of the report. This Service is used to provide the summary.
- The Amount Denied has been added to each denied stay in the detail section. This amount is either:
  - if entire admission was denied and the entire stay is within the date range of the report then the Amount Denied is the full charge of the Admission
  - if only a partial denial then the Amount Denied is an average charge based on the full charge and the number of denied days on the report
- Inpatient stays of one day will now be included on the report.
- Events in Claims Tracking not linked to an actual clinical event will now be included on the report. Entries are sometimes manually created so Insurance Reviews can be completed before the event is automatically entered into Claims Tracking. The data on these types of entries will be limited as there is no source clinical event, for example there will be no service or amount displayed.
- Detail and Summary sections are added for other types of care than Inpatient. Any Outpatient, Prescriptions or Prosthetics assigned a denial will be included on the report.

Option: Days Denied Report \[IBT OUTPUT DENIED DAYS REPORT\]

## REASONS NOT BILLABLE REPORT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An estimated charge for an Inpatient admission is included on the Reasons Not Billable report. Errors were identified in the Reasonable Charges Inpatient Facility charge calculation and have been corrected:

- Every Inpatient stay was assumed to have been a DRG charge. This is updated so Nursing Home Care Treating Specialties will be properly charged the Skilled Nursing per diem.
- Observation care will not be identified with and charged a DRG charge.
- The Inpatient DRG calculation did not recognize the difference between ICU and Non-ICU care and added both DRG charges to the final amount. This is updated so each type will be identified and charged only the corresponding DRG amount.

Option: Reasons Not Billable Report \[IBJD REASONS NOT BILLABLE\]

## BILL/CLAIMS ENTRY OF REASON NOT BILLABLE (?RNB)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are cases where an event may only be partially billed and therefore will require both a bill and a Reason Not Billable. To assist processing these types of events a new Help action has been added to Enter/Edit a Bill option. The '?RNB' action will present the Claims Tracking entries related to the bill and allow a Reason Not Billable to be entered. The Reason Not Billable should only be entered if the event is not fully billed.

Option: Enter/Edit Billing Information \[IB EDIT BILLING INFO\]

## UPDATE FIELD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The INSURANCE REVIEW (#356.2) FINAL OUTCOME OF APPEAL (#.29) field contained a misspelling. This has been corrected (PARITIAL corrected to PARTIAL) and Help Text was added to the field.

## CHARGE MASTER UPLOAD EXPAND DIVISION CHARACTERS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A list of sites is included with each version of Reasonable Charges released. This site number was limited to 5 characters. Actual division numbers are allowed 7 characters. Therefore the Charge Master Upload has been modified to allow 7 character site numbers.

Option: Load Host File into Charge Master \[IBCR HOST FILE LOAD\]

## CHARGE MASTER REASONABLE CHARGES FACILITY TYPE DESIGNATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each VA division is identified as a particular Facility Type for Reasonable Charges, either Provider Based or Non-Provider Based. This designation determines the charges loaded and available for use for that division.

Non-Provider Based Freestanding Charges include Professional charges only.

Provider Base Charges include Institutional and Professional charges for Inpatient, SNF and Outpatient care.

There is the potential that a particular division's Facility Type may change which would require a complete new set of Reasonable Charges to be loaded for the new type. Previously this was only possible when a new version was released.

A new option is added to allow a site's Facility Type to be changed at any time so it is no longer dependent on a version release. The current versions Reasonable Charges are inactivated and a new set loaded for the new Facility Type effective on a specified date.

\>\>\> CBO must approve any Facility Type change.

Option: RC Change Facility Type \[IBCR RC FACILITY TYPE\] (new)

Menu: Charge Master IRM Menu \[IBCR CHARGE MASTER IRM MENU\] (link)

### From: IB*2*494 Release Notes

## Documentation Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to FTP the files from REDACTED

This transmits the files from the first available FTP server. Sites may

also elect to retrieve software directly from a specific server as follows:

Albany REDACTED REDACTED

Hines REDACTED REDACTED

Salt Lake City REDACTED REDACTED

The documentation will be in the form of Adobe Acrobat files.

Documentation can also be found on the VA Software Documentation Library at:

http://www.va.gov/vdl/

Title File Name FTP Mode

--------------------------------------------------------------------

IB Release Notes/ IB_2_0_P494_RN.PDF Binary

Installation Guide (IB\*2.0\*494)

*(This page included for two-sided copying.)*

## Functional Specifications for Integrated Billing (IB)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Nightly Report for FSC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Remove Nightly TaskMan Job

The system no longer produced a download to send to FSC via option ePharmacy Shared Matches Report – TaskMan.

The job was removed from the Task Manager schedule. The feature components, including code, were removed from the system.

The original components were contained in patch IB\*2\*322 which was available in Attachment A of the Requirements Specification Document.

This requirement pertains to decommissioned functionality.

### View Insurance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Remove "e-Pharmacy" from Insurance Company Enter/Edit

The "EI Insurance Company Entry/Edit" option no longer displayed "e-Pharmacy" on the Payer Information line.

The comma following e-IV was removed.

This requirement pertains to decommissioned functionality.

Payer Information: e-IV, e-Pharmacy

Payer Name:

VA National ID: CMS National ID:

#### Remove the E-PHARM Payer Application Section

The "EI Insurance Company Entry/Edit" option no longer displayed a Payer Application section of E-PHARM.

This requirement pertains to decommissioned functionality.

Before the enhancement:

Payer Information: e-IV, e-Pharmacy

Payer Name: EPHARM INSURANCE

VA National ID: XX999 CMS National ID:

Payer Application: E-PHARM FSC Auto-Update: NO

National Active: YES Deactivated: NO

Local Active: YES

Payer Application: eIV FSC Auto-Update: NO

National Active: YES Deactivated: NO

Local Active: YES

After the enhancement:

Payer Information: e-IV

Payer Name: EPHARM INSURANCE

VA National ID: XX999 CMS National ID:

Payer Application: eIV FSC Auto-Update: NO

National Active: YES Deactivated: NO

Local Active: YES

### TPJI ECME Claim Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Display Cancelled Bill Information

The ECME Claim Information Screen displayed information for cancelled bills.

From option IBJ Third Party Joint Inquiry, action RX ECME Information displayed an additional line with information on cancelled bills above Payment Information. The reason was displayed next to the status. If a claim reversal did not exist, the screen did not display the additional line. In the header of the screen, an additional line that shows the AR status, original amount, and balance due was displayed.

ECME Claim Information        Jan 28, 2013@10:06:53          Page:   1 of    2

K300004e   OPTRICARE,ONE  O4789          DOB: 10/18/63   Subsc ID: SI9844532  

AR Status: CANCELLATION             Orig Amt: 13.77      Balance Due: 0.00    

IB Status: CANCELLED (01/18/13)  Reason: ECME PRESCRIPTION REVERSED Payment Information

Ingredient Cost Paid: 55.70

Dispensing Fee Paid: 12.50

Patient Resp (Ins): (10.00)

Expected Payment Amount: 68.32

### Miscellaneous Decommissioned Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Remove Options from IBCNR E-PHARMACY Menu

The IBCNR E-PHARMACY Menu no longer contained options for the following:

> EHNF Edit HIPAA NCPDP FLAG

> ENP Edit NCPDP PROCESSOR APPLICATION Subfile

> EPAY Edit PAYER APPLICATION Subfile

> EPBM Edit PBM APPLICATION Subfile

> NON Drugs Non-Covered Report

The data remained on the system for all options except "NON Drugs Non-Covered Report". The data for the Drugs Non-Covered Report is addressed in subsequent requirements.

This requirement pertains to decommissioned functionality.

#### Remove Drugs Non-Covered Report

The system no longer contained the IB Drugs Non-Covered Report.

The option was removed from the system.

This requirement pertains to decommissioned functionality.

#### Remove Drugs Non-Covered Recheck Period from Display

Section 12 of the IB Site Parameters option did not contain a field for "Drug Non-Covered Recheck Period."

This requirement pertains to decommissioned functionality.

#### Remove Non-Covered Reject Codes from display

Section 12 of the IB Site Parameters option did not contain a field for "Non-Covered Reject Codes".

This requirement pertains to decommissioned functionality.

#### Remove DRUG NON-COVERED RECHECK PERIOD field

File IB SITE PARAMETERS FILE (350.9) no longer contained field DRUG NON-COVERED RECHECK PERIOD (11.02).

The data was removed and the field was deleted.

This requirement pertains to decommissioned functionality.

#### Remove NON-COVERED REJECT CODES field

File IB SITE PARAMETERS FILE (350.9) no longer contained field NON-COVERED REJECT CODES (11) in subfile 350.912.

The data was removed and the field was deleted and subfile.

This requirement pertains to decommissioned functionality.

#### Remove file IB NDC NON-COVERED BY PLAN

File IB NDC NON-COVERED BY PLAN (366.16) was removed from VistA.

Remove the data and delete the data dictionary and all associated fields. This requirement pertains to decommissioned functionality.

#### Remove reference to IB NDC NON-COVERED BY PLAN

The VistA system no longer referenced file IB NDC NON-COVERED BY PLAN (366.16).

IB Billing Determination was modified so that there was no check to see if the drug/plan was stored in file 366.16. (Note: the call to \$\$CHCK^IBNCDNC was removed.)

This requirement pertains to decommissioned functionality.

#### Modify DBIA# 5185

The ECME system no longer referenced DBIA# 5185 to allow access to Integrated Billing data for file IB NDC NON-COVERED BY PLAN (366.16).

The routine that referenced the DBIA (IBNCDNC) was removed.

This requirement pertains to decommissioned functionality.

#### Remove Decommissioned Routines

The VistA system no longer contained routines for the Drugs Non-Covered functionality.

The functionality was decommissioned and corresponding data were removed. Routines IBNCDNC and IBNCDNC1 were removed.

This requirement pertains to decommissioned functionality.

### Old TRICARE Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Remove Old TRICARE Process

The system no longer contained the components distributed for the old TRICARE Process.

Prior to the ePharmacy project for electronically billable TRICARE claims, there were TRICARE processes in place to handle billing. The ePharmacy TRICARE project did not follow the same design as the original TRICARE process, and that original software was retired. The associated data remained on the system. The original components were contained in patch IB\*2\*52, which is available for reference in Attachment B of the Requirements Specification Document.

This requirement pertains to decommissioned functionality.

### From: IB*2*452 Release Notes

### IB Billing Determination API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Add IB support for CHAMPVA ePharmacy insurance and CHAMPVA patient eligibility, and process CHAMPVA ePharmacy prescriptions using the CHAMPVA rate type.

### New Reason Not Billable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

2.  Add a new Claims Tracking Reason Not Billable (RNB) for CHAMPVA, inpatient prescriptions.

### Changes to ECME Billing Events Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3.  Enhance the ECME Billing Events Report option \[IB ECME BILLING EVENTS\] as follows:
- Add patient eligibility (VETERAN, TRICARE, CHAMPVA)
- Display the NCPDP quantity and units when available and also the Billed quantity and units
- Display a breakout of all fees and costs associated with each prescription
- Display a breakout of the payer-reported amounts paid in the ECME response for each prescription

### Bill Creation for Duplicate ECME Response

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

4.  Create a bill in IB and AR when a DUPLICATE ECME response is received and only when a non-cancelled bill with the same Rx#, fill#, and payer sequence doesn't already exist.

### Inclusion of ECME# in Existing Displays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

5.  Add the display of the ECME# to several existing reports, screens, and MailMan messages that currently only show the Rx#.

### New Fields and Prompts in Existing Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

6.  Add fields and prompts for the Pharmacy Relationship Code and for the Pharmacy Person Code in both the Process Insurance Buffer \[IBCN INSURANCE BUFFER PROCESS\] option and in the Patient Insurance Info View/Edit \[IBCN PATIENT INSURANCE\] option.

### New Claims Tracking Reason Not Billable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

7.  Add a new Claims Tracking Reason Not Billable (RNB) for Auto-Reversals for Inpatient Prescriptions. Previous to this patch, the RNB for this situation was being filed by the system as OTHER.

### New Service Requests (NSR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch addresses the following New Service Request (NSR):

> -------------------------------------------------

> Request Name: ePharmacy Claims Phase 6 (FY10)

> Request ID: 20090215

### Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no Remedy Tickets associated with this patch.

### From: IB*2*525 Release Notes

### Tracking HPID Field Edits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*525 (HPID Build 3) contains the changes made to the BILL/CLAIMS File (#399) to track changes to the claim-level HPID Fields \#471, \#472, and \#473.

### Manually Added HPIDs to Billing Claim Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*525 (HPID Build 3) implements a menu option that runs an ad-hoc report listing Authorized claims that have had claim-level HPIDs added within a selected date range.

### From: IB*2*550 Release Notes

## System Feature: ROI Expiration Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Release of Information \[IBCNR RELEASE OF INFORMATION\] action allows the user to enter any date for the expiration date. However, the expiration date cannot be earlier than the effective date. There is also a new ROI Expiration Report \[IBCNR ROI EXPIRATION REPORT\] available to users and is sorted by expiration date in reverse chronological order.

## System Feature: TRICARE Copay

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system does not create a TRICARE copay for a prescription if a TRICARE copay already exists.

## System Feature: Display VA Plan ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several options display the VA Plan ID instead of the Pharmacy Plan: Group Plan Worksheet Report \[IBCNR GROUP PLAN WORKSHEET\], Match Multiple Group Plans \[IBCNR GROUP PLAN MATCH\], and Match Group Plan to a Pharmacy \[IBCNR PLAN MATCH\].

## System Feature: Billing Determination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IB Billing Determination uses the ePharmacy Billable fields to assess billable status and the Sensitive Diagnosis Drug field to assess sensitive diagnosis instead of using the DEA, Special HDLG field.

## System Feature: Date of Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back billing processes uses the same date of service algorithm used in outpatient pharmacy.

## System Feature: Billing Event Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IB Billing Event Log contains new drug file fields in the finish event for billing events that do not generate a claim because of non-billable determination.

### From: IB*2*521 Release Notes

## System Feature: EDI Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EDI Transactions – Validate the HPID/OEID and Health Plan Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software provides the ability to validate the HPID/OEID and health plan name against the NIF.

### EDI Transactions – Ensure the Legacy ID and HPID/OEID are Shared with Interfacing Systems 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The legacy ID and HPID/OEID are shared with systems that interface with VistA. The systems to be interfaced include but are not limited to: FSC (Financial Services Center) preprocessors, EEOB and Payment Healthcare Resolution Application (EPHRA), Health Care Clearinghouses and Medicare Administrative Contractors[^1].

## System Feature: Reports/Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Reports/Screens - Modify the following eBilling Reports to Include the HPID/OEID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modifications are made to the current Insurance Company EDI Parameter Report (EPR report) to display both the Payer ID and the HPID/OEID ID on this report.

### Reports/Screens - Modify the following eInsurance Reports to Include the HPID/OEID 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following eInsurance reports include the HPID/OEID ID:

- Insurance Company EDI Parameter Report \[IBCN INSURANCE EDI REPORT\]
- eIV Payer Link Report \[IBCNE IIV PAYER LINK REPORT\]

[^1]: The legacy Payer IDs for the 837 is the EDI Professional ID and the EDI Institutional ID. The legacy Payer ID for the 835 (Electronic Remittance Advice/Electronic Funds Transfer) is the TIN (Tax ID).

### From: IB*2*499 Release Notes

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

Although sites are required to use FBCS to process claims, Newborn claim can ONLY be processed by VistA at this time. FBCS can NOT be used to process Newborn claims. Refer to the instructions in the Care for Newborn of Women Veterans located at REDACTED for processing Newborn claims.

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

This patch bundle updated the Fee Basis User Manual (fb3_5_um) and PIMS ADT Registration User Manual (dg_5_3_reg_um). Additionally, the document Care for Newborn of Woman Veterans, located REDACTED has been created.

## Existing Issues and Workarounds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA MUST BE USED for this process. DO NOT use FBCS. Until FBCS can process Newborn claims, follow your local facility's VistA procedures. Refer to the instructions in the Care for Newborn Women of Veterans located at REDACTED for processing Newborn claims.

### From: IB*2*534 Release Notes

## Routine Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The second line of each of these routines now looks like:

> ;;2.0;INTEGRATED BILLING;\*\*\[Patch List\]\*\*;21-MAR-94;Build 18

> The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

> Routine Name: IB534PST

> Before: n/a After: B14543577 \*\*534\*\* Routine Name: IBNCPDP1

> Before:B191529259 After:B164054794 \*\*223,276,339,363,383,405,384,

> 411,434,437,435,455,452,473,

> 494,534\*\*

> Routine Name: IBNCPDPU

> Before:B122718985 After:B125879968 \*\*223,276,347,383,405,384,437,

> 435,452,511,534\*\*

> Routine Name: IBNCPEV3

> Before: n/a After: B30560136 \*\*534\*\* Routine Name: IBNCPLOG

> Before: B76075004 After: B83304395 \*\*342,339,363,383,411,435,452,534\*\*

> Routine list of preceding patches: 494, 511

### Background Logic Change to Billing Rules for Inpatient Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### In order to allow all discharge medications to be billed, the billing rules for inpatient prescriptions were modified so that all inpatient prescriptions will be billed to the third party payer. Note that the inpatient auto reversal process of the BPS Nightly Background Job will continue to reverse inpatient claims if the patients are still in an inpatient status five days after the prescription fill date.

### Background Logic Change to Billing Rules Exception Processing for TRICARE/CHAMPVA Patients with Environmental Indicators

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The billing rules for processing claims with Environmental Indicators were changed:

#### TRICARE/CHAMPVA claims with Environmental Indicators are filled but not billed to the third party insurance.

#### Active Duty prescriptions are flagged for Environmental Indicators for patients whose Eligibility is TRICARE are filled and billed to TRICARE.

### IB Routines and Databases Modified to Support the New ECME Non- Billable Status Report Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integrated Billing routines and databases were modified to support the new ECME Non-Billable Status Report \[BPS RPT NON-BILLABLE REPORT\] option. Please see the BPS\*1.0\*19 patch description for more information on this new report.

### From: IB*2*688 Release Notes

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to implement reports that would help billing users to identify patients that were treated under OTH authority and PP. This is to provide details about eligibility changes and VA care provided to these patients.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets billing users and administrators that review Former Service Member's and and PP episodes of care and released prescription details to determine if potential back-billing is necessary.

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the features and functions added by IB\*2.0\*688:

- Added new Presumptive Psychosis Reconciliation Report \[DG PRESUMP. PSYCH. RECON RPT\] menu option to Consolidated Patient Account Center (CPAC) Facility Revenue Billing Menu \[KPA FACILITY REVENUE BILLING\].

> \* BEGIN SCREEN CAPTURE \*

Select OPTION NAME: KPA FACILITY REVENUE BILLING CPAC Facility

Revenue Billing Menu

PPR Presumptive Psychosis Reconciliation Report

Automated Means Test Billing Menu ...

> Claims Status Awaiting Resolution

> \* END SCREEN CAPTURE \*

- Added new API "EN^IBEFSMUT" to the Integrated Billing application.

Listed below are the details on accessing this entry point and the data that should be returned.

ROUTINE: IBEFSMUT

COMPONENT: EN(DFN,BEGDT,ENDDT,LIST)

VARIABLES: Both DFN

Internal entry number from the PATIENT file (#2)

\[required\]

VARIABLES: Input BEGDT

EVENT DATE Beginning Date \[required\]

VARIABLES: Input ENDDT

EVENT DATE Ending Date \[required\]

VARIABLES: Both LIST

Subscript name used in the ^TMP global \[required\]

EN^IBEFSMUT(DFN,BEGDT,ENDDT,LIST)

Input:

DFN

BEGDT

ENDDT

LIST

FILE \#350 OUTPUT:

^TMP(\$J,LIST,FILENO,DFN,0)=Total entries or -1^NO

DATA FOUND

^TMP(\$J,LIST,FILENO,DATE,DFN,RECCNT)=ACTION

TYPE^BILLING GROUP^IEN^BILL NUMBER^RESULTING

FROM^TOTAL CHARGE^STATUS^INSTITUTION^CLINIC

STOP^USER LAST UPDATING

Where:

LIST = Subscript name used in the ^TMP global

FILENO = File \#350, this is to distinguish where

records coming from

DATE = Event Date (I:350,.17)

DFN = IEN from the PATIENT File(#2)

RECCNT = Record counter

1^2^3^4^5^6^7^8^9^10, where:

1 = ACTION TYPE (E;350,.03)

2 = BILLING GROUP (I;350.1,.11)

> **NOTE:** NULL is returned if there is no BILLING

GROUP

3 = IEN from INTEGRATED BILLING file (#350)

4 = AR BILL NUMBER (E;350,.11)

> **NOTE:** NULL is returned if there is no AR BILL

NUMBER

5 = RESULTING FROM (I;350,.04)

> **NOTE:** If RESULTING FROM 2ND ^ piece ":"=350,

the format will be:

RESULTING FROM;DATE BILLED FROM(I;350,.14):

COPAYMENT TIER (I;350,.22)

6 = TOTAL CHARGE (E;350,.07)

7 = STATUS (E;350,.05)

8 = INSTITUTION (IE;350,.13)

9 = CLINIC STOP(IE;350,.2)

> **NOTE:** NULL is returned if there is no CLINIC

STOP

10 = USER LAST UPDATING (E;350,13)

FILE \#399 OUTPUT:

^TMP(\$J,LIST,FILENO,DFN,0)=Total entries or -1^NO

DATA FOUND

^TMP(\$J,LIST,FILENO,DATE,DFN,RECCNT)=RATE

TYPE^IEN^RATE TYPE NAME^IEN^BILL NUMBER^RESULTING

FROM^CHARGES^STATUS

Where:

LIST = Subscript name used in the ^TMP global

FILENO = File \#399, this is to distinguish where

the records coming from

DATE = Event Date (399,.03)

DFN = IEN from the PATIENT File (#2)

RECCNT = Record Counter

1^2^3^4^5^6^7^8^9^10, where

1 = BILL CLASSIFICATION (I;399,.05)

2 = RATE TYPE NAME (E;399,.07)

3 = IEN from BILL/CLAIMS file (#399)

4 = BILL NUMBER (E;399,.01)

5 = RESULTING FROM, will be in the format of:

If inpatient bill, the format will be:

BILL TYPE:BILL CLASSIFICATION(E;399,.05)

> **NOTE:** BILL TYPE=1 if inpatient bill

BILL TYPE=0 if outpatient bill

BILL TYPE=3 if Rx bill

If outpatient bill, the format will be:

TYPE (I;399.042,.1):BILL

CLASSIFICATION(E;399,.05):BILL TYPE

If Rx bill, the format will be:

BILL TYPE:BEDSECTION(E;399.042,.05):RXIEN

(I;362.4,.05):

RXNUMBER (E;362.4,.01):RXFILL

NUMBER(I;362.4,.1):RXSTATUS(52,100)

6 = CHARGES

> **NOTE:** If inpatient bill, CHARGES will be extracted

in 399,201

If outpatient/Rx bill, CHARGES will be

extracted in 399.042,.04

7 = STATUS (E;399,.13)

8 = DIVISION(I;399,.22)

9 = ENTERED/EDITED BY (E;399,2)

10 = PTFIEN (I;399,.08)

> **NOTE:** If inpatient bill, this ^piece contain

the PTF ENTRY NUMBER

If outpatient bill, this ^piece contain

the outpatient

encounter IEN

Otherwise, NULL is returned.

## Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None at this time.

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None at this time.

## Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents are located at the VA Software Document Library and apply to this release:

- Deployment, Installation, Back-out, and Rollback Guide
- Integrated Billing V. 2.0 User Manual

### From: IB*2*476 Release Notes

### IB\*2.0\*476

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### December 2012

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Version 1.3 Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Office of Information and Technology (OIT) Product Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 11%" />
<col style="width: 44%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>July 2012</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Initial document creation</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>November 2012</p>
</blockquote></td>
<td><blockquote>
<p>1.1&amp;1.2</p>
</blockquote></td>
<td><blockquote>
<p>Updated overview</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>December 2012</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>Updated from patch return</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
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
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> ii Integrated Billing IB\*2.0\*476 Release Notes December 2012

## Modified input transform routines.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The input transforms on two fields in the IB NON/OTHER VA BILLING PROVIDER FILE (#355.93) file were modified to allow the Fee Basis Payment to IB \[FB PAID TO IB\] background job make updates to the fields:

> PRVFMT^IBCEP8 was modified for the NAME (#.01) field NPIUSED^IBCEP81 was modified for the NPI (#41.01) field

## A new API was created to be used by Fee Basis for automating IB provider edits.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A new routine IBCEP8C contains the API EPFBAPI that is called by the Fee Basis Payment to IB \[FB PAID TO IB\] background job to add/edit IB providers. Supporting functions include a lookup of existing records in the IB NON/OTHER VA BILLING PROVIDER FILE (#355.93) file using the NPI provided by Fee Basis records. Other functions include the ability to compare and update a matched record when required, and functions to create a new entry. The new field (#50) DATE/TIME LAST FB UPDATE is edited during the automated process to allow tracking and reporting of IB providers edited by Fee Basis.

## Allow IB users to turn off automated edits to specific IB Non-VA Providers.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Routines IBCEP8 and IBCEP8B have been modified to display and update a new multiple valued field, DATE/TIME ALLOW FB UPDATE (#51) in the IB NON/OTHER VA BILLING

> PROVIDER FILE (#355.93) file. A new routine, IBCEP8C1 provides supporting code for this functionality. The new field allows an IB user to 'allow' or 'disallow' automated updates from Fee Basis. The modified routines are accessed by the IB Non-VA Provider ID Maintenance screens in IB.

## Provide tracking and audit reports for the Fee Basis to IB Provider automation.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A new menu option, IB Provider From FB Reports Menu \[IB PROVIDER FROM FB RPTS MENU\] has been created that contain two new reporting options that provide tools to locate and display information about records modified or created by the FB PAID TO IB interface for a date range. This menu is not available on any existing IB menus, but could be added to a menu or secondary menu for an IB user or supervisor. The report options available on this menu are:

> Non-VA Provider From FB Summary Report \[IB PROVIDER FROM FB SUMMARY\] Non-VA Provider From FB Detail Report \[IB PROVIDER FROM FB DETAIL\]

> 2 Integrated Billing IB\*2.0\*476 Release Notes December 2012
