---
title: IB*2 EDI User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: IB*2 EDI
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: archive
pkg_ns: IB
patch_ver: 2.0
patch_id: IB*2.0
group_key: "IB:IB:2.0"
file_numbers: 
  - 200
  - 355
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - provider
  - blockquote
  - insurance
  - claim
  - claims
  - billing
  - secondary
  - payer
  - prompt
  - table
page_count: 0
word_count: 60629
section_count: 46
table_count: 8
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: August 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)_Archive/ib_2_0_edi_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)_Archive/ib_2_0_edi_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=266"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>EDI Integrated Billing  
  Version 2.0

  User Guide
---

![](ib-2-edi-user-guide/001.png)

August 2005  
Revised: March 2022

Office of Information and Technology (OIT)

Revision History

1.  The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

<table>
<caption><p><span id="_Toc100304280" class="anchor"></span>Table : Patient Billing Revenue Process</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 12%" />
<col style="width: 48%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>March 2022</td>
<td>3.5</td>
<td><p>Patch IB*2*665.</p>
<p>Added section/subsections: 6.2.8, 6.2.8.1, 6.2.8.2, 6.2.8.3</p>
<p>Added section 6.3.9</p>
<p>Added <em>Note</em> to section 6.7, steps 3 and 4.</p>
<p>Added <em>Note</em> to section 6.8, step 3</p>
<p>Updated instructions in section 6.15, steps 3, 7, 10 and 16.</p>
<p>Added <em>Note</em> to section 6.15, steps 7, 10, and 15.</p>
<p>Updated screens in section 6.15, under steps, 14 and 16.</p>
<p>Added <em>Note</em> to section 10.3.17 and inserted a reference to section 3.3.</p></td>
<td>MCCF EDI TAS eBilling</td>
</tr>
<tr class="even">
<td>December 2021</td>
<td>3.5</td>
<td><p>Patch IB*2*687</p>
<p>Revised Sections 9.1 &amp; 9.2</p></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="odd">
<td>August 2021</td>
<td>3.4</td>
<td><p>Patch IB*2*650.</p>
<p>Added <em>Note:</em> to sections 6.9, #4 and 10.2.1</p>
<p>Added new acronyms/terms to APPENDIX B – ACRONYMS AND ABBREVIATIONS</p>
<ul>
<li><p>277RFAI</p></li>
<li><p>277STAT</p></li>
</ul>
<p>Fixed multiple punctuation/grammatical MS WORD errors within the document.</p></td>
<td>MCCF EDI TAS eBilling</td>
</tr>
<tr class="even">
<td>April 2021</td>
<td>3.3</td>
<td><p>Patch IB*2*668</p>
<p>Revised Sections 9.1 &amp; 9.2 – Redactions and dropped “Service Type Code” from two screen shots.</p></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="odd">
<td>November 2020</td>
<td>3.2</td>
<td><p>Patch IB*2*641.</p>
<p>Added sections: 6.2.7, 6.3.7, 6.3.8, 9.7, and 10.3.21 (For this patch, when Section 9.7 was added, Section 9.7 for Patch IB*2*608 became Section 9.8)</p>
<p>Revised sections/subsections: 6.7, 6.8, 10.1, and 10.2.1.</p>
<p>Updated section 10.2.4.</p></td>
<td>MCCF EDI TAS eBilling</td>
</tr>
<tr class="even">
<td>January 2020</td>
<td>3.1</td>
<td><p>Patch IB*2*623.</p>
<p>Revised sections/subsections: 3.3, 6.7, 6.8, 6.9. 10.1, 10.2.1, and 10.3.20.</p>
<p>Updates requested by the eBiz Team.</p>
<p>Sections 6.7 &amp; 6.8.</p>
<p>Section 10.2.1.</p></td>
<td>MCCF EDI TAS eBilling</td>
</tr>
<tr class="odd">
<td>December 2019</td>
<td>3.0</td>
<td>Patch IB*2*652 Revised screen shots of Insurance Plan List in section 2.1.1.2 and 2.1.2 by adding the new action NP New Plan.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>April 2019</td>
<td>2.9</td>
<td>Patch IB*2*608 Added section 9.7. Revised sections/subsections: 2.1.2, 2.1.3. 3, 3.1, 3.2, 3.3, 6.2.3.1, 6.3.6, 6.4, 6.15, 6.8, 9.1, and 10.3.17.</td>
<td>MCCF EDI TAS eBilling</td>
</tr>
<tr class="odd">
<td>October 2018</td>
<td>2.8</td>
<td>Patch IB*2*592 Added sections 6.3.5, 6.9 and 9.6. Modified sections/sub-sections 2.1.1.1, 2.1.1.2, 2.1.2, 2.1.3, 4.0, 4.1, 4.3.2, 4.5, 6.1, 6.4, 6.6.1, 6.15, 7.2, 10.3.16, 10.3.18, 10.3.20, 11, and 12.</td>
<td>MCCF EDI TAS eBilling</td>
</tr>
<tr class="even">
<td>October 2017</td>
<td>2.7</td>
<td>Patch IB*2*577 Added sub-section 10.3.20, Modified sub-section 6.2.3.2 and 6.7 and 6.8.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>July 2017</td>
<td>2.6</td>
<td>Patch IB*2*576 Added sub-sections 6.2.5 and 6.3.4.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>August 2016</td>
<td>2.5</td>
<td><p>Patch IB*2*549.</p>
<p>Revised Sections: 2.1.1.2, 2.1.2, 5.1.1.</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>August 2016</td>
<td>2.4</td>
<td><p>Patch IB*2*547.</p>
<p>Revised Sections: 2.1.1.1, 2.1.2, 6.2.4, and all sub-sections, 6.3.3, 6.7, 6.9, 6.10, 6.14, 7.2, 8., 9.3, 9.4, 9.5, 10.2.1, 10.3.16, 10.3.17, 10.3.19, Appendix B.</p></td>
<td>MCCF EDI TAS eInsurance</td>
</tr>
<tr class="even">
<td>April 2015</td>
<td>2.3</td>
<td><p>IOC Exit Review Patch IB*2*516.</p>
<p>Revised Sections: 6.11, 6.2.3.1, 6.2.3.2, 6.3.2, 9.2.3.</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>April 2015</td>
<td>2.2</td>
<td><p>Patch IB*2*516 .</p>
<p>Revised Sections: 2.1.1.1, 2.1.1.2, 2.1.2, 3, 3.1, 4.4.1, 6.2.3, 6.2.3.1, 6.2.3.2, 6.3.2, 5.7, 6.7, 6.8, 6.9, 6.10, 6.11, 6.12, 72, 7.2.1, 9.3.14, 9.3.16, 9.3.17.</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>January 2015</td>
<td>2.1</td>
<td><p>Patch IB*2*521.</p>
<p>Revised EDI Parameter Report Section 9.3.14, Appendix B.</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>August 2014</td>
<td>2.0</td>
<td><p>Patch IB*2*488 (Build 1).</p>
<p>Revised Sections: 2.1.1.1. (Steps 1 &amp; 2), 2.2.1, 4.4.1 (Steps 5 &amp; 9), 6.2.2, 6.6.1, 6.7 (note after Step 5), 6.8 (note after Step 5), 6.9 (notes after Steps 6 &amp; 7), 6.10, 9.3.16, Appendix A &amp; B.</p>
<p>General grammar, spelling and format changes applied.</p></td>
<td><p>REDACTED</p>
<p>FirstView</p></td>
</tr>
<tr class="even">
<td>March 2014</td>
<td>1.12</td>
<td><p>Patch IB*2.0*476.</p>
<p>Revised Sections: 4.4.1, 4.5.3.</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>March 2012</td>
<td>1.11</td>
<td><p>Patch IB*2*447 and PRCA*4.5*275.</p>
<p>Revised Sections: 6 &amp; 7.</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>September 2011</td>
<td>1.10</td>
<td><p>Patch IB*2*432.</p>
<p>Revised Sections: 1, 2, 4, 6.</p>
<p>Added Sections: 7 and 8.</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>May 2011</td>
<td>1.9</td>
<td>Patch IB*2*433 – Section 6.7.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>January 2011</td>
<td>1.8</td>
<td>Edits by Training Department and removed reference to patch IB*2*433.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>November 2010</td>
<td>1.7</td>
<td><p>Patch IB*2*436 – Section 4 and</p>
<p>Section 4.5.3.1.</p>
<p>Also replaced references to Emdeon and Express Bill with “clearinghouse.”</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>February 2009</td>
<td>1.6</td>
<td>Patch IB*2*400.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>May 2008</td>
<td>1.5</td>
<td>Patch IB*2*377</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>November 2007</td>
<td>1.4</td>
<td>Patch IB*2*368 and 371.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>July 2007</td>
<td>1.3</td>
<td>Patch IB*2*374.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>February 2007</td>
<td>1.2</td>
<td>Patches IB*2*343, 348, and 349.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>July 2006</td>
<td>1.1</td>
<td>Patch IB*2*320.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>August 2005</td>
<td>1</td>
<td>Patch IB*2*296.</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

<span id="_Toc100304280" class="anchor"></span>Table : Patient Billing Revenue Process

Artifact Rationale

Per the Veteran-focused Integrated Process (VIP) Guide, the User’s Guide is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A User Guide is a technical communication document intended to give assistance to people using a particular system, such as Veterans Health Information System and Technology Architecture (VistA) end users. It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most user guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The User Guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required if applicable to your product.

Table of Contents

List of Tables

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Revenue Process](#revenue-process)
  - [Critical EDI Process Terms](#critical-edi-process-terms)
  - [EDI Process Flow](#edi-process-flow)
- [Insurance Company Set-up](#insurance-company-set-up)
  - [Insurance Company Setup](#insurance-company-setup)
    - [Activate New Payer to Transmit eClaims](#activate-new-payer-to-transmit-eclaims)
    - [Activate Existing Commercial Payer to Transmit eClaims](#activate-existing-commercial-payer-to-transmit-eclaims)
    - [Activate Existing Payer to Test Primary Blue Cross / Blue Shield eClaims](#activate-existing-payer-to-test-primary-blue-cross-blue-shield-eclaims)
- [Pay-to Provider(s) Set-up](#pay-to-providers-set-up)
  - [Define Default Pay-to Provider](#define-default-pay-to-provider)
  - [Associate Divisions with Non-Default Pay-to Provider](#associate-divisions-with-non-default-pay-to-provider)
  - [Rate Types for Non-MCCF Pay-to Provider](#rate-types-for-non-mccf-pay-to-provider)
- [Provider ID Set-up](#provider-id-set-up)
  - [Table of IDs](#table-of-ids)
  - [Pay-to Provider IDs](#pay-to-provider-ids)
    - [Define the Pay-to Provider Primary ID / NPI](#define-the-pay-to-provider-primary-id-npi)
    - [Define the Pay-to Provider Secondary IDs](#define-the-pay-to-provider-secondary-ids)
  - [Billing Provider IDs](#billing-provider-ids)
    - [Define the Billing Provider Primary ID / NPI](#define-the-billing-provider-primary-id-npi)
    - [Define the Billing Provider Secondary IDs](#define-the-billing-provider-secondary-ids)
  - [Service Facility IDs (Laboratory or Facility IDs)](#service-facility-ids-laboratory-or-facility-ids)
    - [Define Non-VA Laboratory or Facility Primary IDs / NPI](#define-non-va-laboratory-or-facility-primary-ids-npi)
    - [Define Non-VA Laboratory or Facility Secondary IDs](#define-non-va-laboratory-or-facility-secondary-ids)
    - [Define VA Laboratory or Facility Primary IDs / NPI](#define-va-laboratory-or-facility-primary-ids-npi)
    - [Define VA Laboratory or Facility Secondary IDs](#define-va-laboratory-or-facility-secondary-ids)
  - [Attending, Operating, and Other Physicians and Rendering, Referring, and Supervising Providers](#attending-operating-and-other-physicians-and-rendering-referring-and-supervising-providers)
    - [Define a VA Physician / Provider’s Primary ID / NPI](#define-a-va-physician-providers-primary-id-npi)
    - [Define a VA Physician / Provider’s Secondary IDs](#define-a-va-physician-providers-secondary-ids)
    - [Define a non-VA Physician / Provider’s Secondary IDs](#define-a-non-va-physician-providers-secondary-ids)
    - [Define Insurance Company IDs](#define-insurance-company-ids)
    - [Define either a Default or Individual Physician / Provider Secondary ID](#define-either-a-default-or-individual-physician-provider-secondary-id)
  - [Care Units](#care-units)
    - [Define Care Units for Physician / Provider Secondary IDs](#define-care-units-for-physician-provider-secondary-ids)
    - [Define Care Units for Billing Provider Secondary IDs](#define-care-units-for-billing-provider-secondary-ids)
  - [ID Parameters by Insurance Company](#id-parameters-by-insurance-company)
    - [Define Attending/Rendering Provider Secondary ID Parameters](#define-attendingrendering-provider-secondary-id-parameters)
    - [Define Referring Provider Secondary ID Parameters](#define-referring-provider-secondary-id-parameters)
    - [Define Billing Provider Secondary ID Parameters](#define-billing-provider-secondary-id-parameters)
    - [Define No Billing Provider Secondary IDs by Plan Type](#define-no-billing-provider-secondary-ids-by-plan-type)
    - [View Associated Insurance Companies, Provider IDs, and ID Parameters](#view-associated-insurance-companies-provider-ids-and-id-parameters)
  - [Associated Insurance Companies and Copying Physician / Provider Secondary IDs and Additional Billing Provider Secondary IDs](#associated-insurance-companies-and-copying-physician-provider-secondary-ids-and-additional-billing-provider-secondary-ids)
    - [Designate a Parent Insurance Company](#designate-a-parent-insurance-company)
    - [Designate a Child Insurance Company](#designate-a-child-insurance-company)
    - [Copy Physician / Provider Secondary IDs](#copy-physician-provider-secondary-ids)
    - [Copy Additional Billing Provider Secondary IDs](#copy-additional-billing-provider-secondary-ids)
    - [Synchronizing Associated Insurance Company IDs](#synchronizing-associated-insurance-company-ids)
- [Subscriber and Patient ID Set-Up](#subscriber-and-patient-id-set-up)
  - [Subscriber and Patient Insurance Provided IDs](#subscriber-and-patient-insurance-provided-ids)
    - [Define Subscriber Primary ID](#define-subscriber-primary-id)
    - [Define Subscriber and Patient Primary IDs](#define-subscriber-and-patient-primary-ids)
    - [Define Subscriber and Patient Secondary IDs](#define-subscriber-and-patient-secondary-ids)
- [Entering Electronic Claims](#entering-electronic-claims)
  - [Summary of Enter / Edit Billing Information to Support ASC X12N/5010](#summary-of-enter-edit-billing-information-to-support-asc-x12n5010)
  - [Changes Made by Specific Patches](#changes-made-by-specific-patches)
    - [Patch IB\2\447](#patch-ib2447)
    - [Patch IB\2\488](#patch-ib2488)
    - [Patch IB\2\516](#patch-ib2516)
    - [Patch IB\2\547](#patch-ib2547)
    - [Patch IB.2.576](#patch-ib2576)
    - [Patch IB\2\577](#patch-ib2577)
    - [Patch IB\2\641](#patch-ib2641)
    - [Patch IB\2\665](#patch-ib2665)
  - [Handling Error Messages and Warnings](#handling-error-messages-and-warnings)
    - [Patch IB\2\488](#patch-ib2488-1)
    - [Patch IB\2\516](#patch-ib2516-1)
    - [Patch IB\2\547](#patch-ib2547-1)
    - [Patch IB\2\576](#patch-ib2576-1)
    - [Patch IB\2\592](#patch-ib2592)
    - [Patch IB\2\608](#patch-ib2608)
    - [Patch IB\2\623](#patch-ib2623)
    - [Patch IB\2\641](#patch-ib2641-1)
    - [Patch IB\2\665](#patch-ib2665-1)
  - [Claim versus Line Level Data](#claim-versus-line-level-data)
  - [Screen 3 – Payer Information](#screen-3-payer-information)
    - [EDI Fields](#edi-fields)
    - [Using Care Units for Billing Provider Secondary IDs](#using-care-units-for-billing-provider-secondary-ids)
  - [Screen 10 – Physician / Provider and Print Information](#screen-10-physician-provider-and-print-information)
    - [EDI Fields UB-04 / CMS-1500 / J430D](#edi-fields-ub-04-cms-1500-j430d)
  - [UB-04 Claims](#ub-04-claims)
  - [CMS-1500 Claims](#cms-1500-claims)
  - [J430D Claims](#j430d-claims)
  - [Lab Claims](#lab-claims)
  - [Pharmacy Claims](#pharmacy-claims)
  - [Correct Rejected or Denied Claims](#correct-rejected-or-denied-claims)
  - [Viewed Cancelled Claims](#viewed-cancelled-claims)
  - [Printed Claims](#printed-claims)
  - [View/Resubmit Claims – Live or Test – Synonym: RCB](#viewresubmit-claims-live-or-test-synonym-rcb)
- [Processing of Secondary / Tertiary Claims](#processing-of-secondary-tertiary-claims)
  - [Criteria for the Automatic Processing of Secondary or Tertiary Claims](#criteria-for-the-automatic-processing-of-secondary-or-tertiary-claims)
  - [COB Management Worklist](#cob-management-worklist)
    - [Data Displayed for Claims on the COB Management Worklist](#data-displayed-for-claims-on-the-cob-management-worklist)
    - [Available COB Management Worklist Actions](#available-cob-management-worklist-actions)
- [Requests for Additional Data to Support Claims](#requests-for-additional-data-to-support-claims)
- [IB Site Parameters](#ib-site-parameters)
  - [Define Printers for Automatically Processed Secondary / Tertiary Claims](#define-printers-for-automatically-processed-secondary-tertiary-claims)
  - [Enable Automatic Processing of Secondary / Tertiary Claims](#enable-automatic-processing-of-secondary-tertiary-claims)
  - [Printed Claims Rev Code Excl: 17 Activated Codes Defined](#printed-claims-rev-code-excl-17-activated-codes-defined)
  - [Alternate Primary Payer ID Types](#alternate-primary-payer-id-types)
  - [ASC X12N Health Care Claim Request for Additional Information (277RFAI)](#asc-x12n-health-care-claim-request-for-additional-information-277rfai)
  - [New EDI Parameter for Dental Processing](#new-edi-parameter-for-dental-processing)
  - [New EDI Parameter for 837 FHIR Transaction Processing](#new-edi-parameter-for-837-fhir-transaction-processing)
  - [CMN CPT Code Inclusion: CMN CPT Codes Included](#cmn-cpt-code-inclusion-cmn-cpt-codes-included)
- [Reports](#reports)
  - [EDI Reports – Overview](#edi-reports-overview)
  - [Most Frequently Used Menus / Reports](#most-frequently-used-menus-reports)
    - [Claims Status Awaiting Resolution – Synonym CSA](#claims-status-awaiting-resolution-synonym-csa)
    - [Multiple CSA Message Management – Synonym: MCS](#multiple-csa-message-management-synonym-mcs)
    - [Electronic Report Disposition](#electronic-report-disposition)
    - [EDI Claim Status Report- Synonym: ECS](#edi-claim-status-report-synonym-ecs)
  - [Additional Reports and Options](#additional-reports-and-options)
    - [Ready for Extract Status Report – Synonym: REX](#ready-for-extract-status-report-synonym-rex)
    - [Transmit EDI Bills – Manual – Synonym: SEND](#transmit-edi-bills-manual-synonym-send)
    - [EDI Return Message Management Menu – Synonym: MM](#edi-return-message-management-menu-synonym-mm)
    - [EDI Message Text to Screen Maintenance](#edi-message-text-to-screen-maintenance)
    - [EDI Messages Not Reviewed Report](#edi-messages-not-reviewed-report)
    - [Electronic Error Report](#electronic-error-report)
    - [Return Messages Filing Exceptions](#return-messages-filing-exceptions)
    - [Status Message Management](#status-message-management)
    - [Bills Awaiting Resubmission – Synonym: BAR](#bills-awaiting-resubmission-synonym-bar)
    - [EDI Messages Not Yet Filed –Synonym: MP](#edi-messages-not-yet-filed-synonym-mp)
    - [Pending Batch Transmission Status Report – Synonym: PBT](#pending-batch-transmission-status-report-synonym-pbt)
    - [EDI Batches Pending Receipt– Synonym: PND](#edi-batches-pending-receipt-synonym-pnd)
    - [View / Print EDI Bill Extract Data – Synonym: VPE](#view-print-edi-bill-extract-data-synonym-vpe)
    - [Insurance Company EDI Parameter Report – Synonym: EPR](#insurance-company-edi-parameter-report-synonym-epr)
    - [Test Claim EDI Transmission Report – Synonym: TCS](#test-claim-edi-transmission-report-synonym-tcs)
    - [Third Party Joint Inquiry – Synonym: TPJI](#third-party-joint-inquiry-synonym-tpji)
    - [Re-generate Unbilled Amounts Report](#re-generate-unbilled-amounts-report)
    - [Patient Billing Inquiry – Synonym: INQU](#patient-billing-inquiry-synonym-inqu)
    - [Printed Claims Report](#printed-claims-report)
    - [HCCH Payer ID Report](#hcch-payer-id-report)
    - [Resubmission / Printing Claims No Changes CSA Report Synonym: RPN](#resubmission-printing-claims-no-changes-csa-report-synonym-rpn)
- [APPENDIX A – Batch Processing Setup](#appendix-a-batch-processing-setup)
  - [Batch Processing Setup](#batch-processing-setup)
- [APPENDIX B - Acronyms and Abbreviations](#appendix-b-acronyms-and-abbreviations)
In 1996, Congress passed into law the Health Insurance Portability and Accountability Act (HIPAA). This Act directs the federal government to adopt national electronic standards for automated transfer of certain healthcare data between healthcare payers, plans, and providers. Now that these standards are in place, the Veterans Health Administration (VHA) will submit claims containing the required standard data content to all payers accepting Electronic Data Interchange (EDI).

## Revenue Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The overall patient billing revenue process for the VHA is summarized in the table below:

<table>
<caption><p><span id="_Toc100304281" class="anchor"></span>Table : VistA Record</p></caption>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 21%" />
<col style="width: 22%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Intake</td>
<td>Utilization Review</td>
<td>Billing</td>
<td>Collection</td>
<td>Utilization Review</td>
</tr>
<tr class="even">
<td><p>Patient Registration</p>
<p>Insurance Identification</p>
<p>Insurance Verification</p></td>
<td><p>Pre-certification &amp; Certification</p>
<p>Continued Stay</p></td>
<td><p>Documentation</p>
<p>EDI Bill Generation</p>
<p>Medicare Remittance Advice (MRA)</p>
<p>Claim status messages</p></td>
<td><p>Establish Receivables</p>
<p>A/R Follow-up</p>
<p>Lockbox</p>
<p>Collection Correspondence</p></td>
<td>Appeals</td>
</tr>
</tbody>
</table>

<span id="_Toc100304281" class="anchor"></span>Table : VistA Record

During the Intake phase, the patient is registered. Insurance information is identified and / or verified.

In the Utilization Review phase, the patient is pre-certified and certified, and continued stay reviews are performed.

In the Billing phase, the patient encounter is documented and coded. An electronic data interchange (EDI) bill and / or Medicare Remittance Advice (MRA) request is generated and sent to the payer. Claim status messages include information that appears on the Claims Status Awaiting Resolution (CSA) report.

During the Collections phase, establishment of receivables, accounts receivables follow-up, lockbox, and any collection correspondence take place.

Another Utilization Review can take place if there are any appeals.

EDI Billing provides the VHA with the capability to submit Institutional and Professional claims electronically as 837 Health Care Claim transmissions, rather than printing and mailing claims from each facility.

## Critical EDI Process Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Also see APPENDIX B - Acronyms and Abbreviations.

- 835 Health Care Claim Payment/Advice – The HIPAA adopted standard for Electronic Remittance Advice (ERA) to report the processing of all claim types (including retail pharmacy). The term “835” represents the data set that is sent from health plans to healthcare providers and contains detailed information about the processing of the claim. This includes payment information and reduction or rejection reasons. All health plans are required to use the same explanation of benefit codes (adjustment reason codes) and adhere to very specific reporting requirements. The term “835” is used interchangeably with Electronic Remittance Advice (ERA) and Medicare Remittance Advice (MRA).
- 837 Health Care Claim – The HIPAA adopted standard for electronic submission of hospital, outpatient, and dental claims. The term “837” represents the data set that is sent from healthcare providers to insurance companies (payers). The 837 standard includes the data required for coordination of benefits and is used for primary and secondary payer claims submission. The term “837” is used interchangeably with electronic claim.
- 277 Claim Status Messages – Electronic messages returned to the Veterans Affairs Medical Centers (VAMC) providing status information on a claim from the Financial Service Center (FSC) in Austin, Texas. These messages can originate at FSC, at the payer or at the clearinghouse.
- Clearinghouse – A company that provides batch and real-time transaction processing services and connectivity to payers or providers. Transactions include insurance eligibility verification, claims submission processing, electronic remittance processing and payment posting for electronic claims.
- eClaim – A claim that is transmitted electronically to FSC from the VHA.
- EDI – Electronic Data Interchange (EDI) is the process of transacting business by exchanging data electronically and includes submitting claims electronically (paperless claims processing), as well as electronic funds transfer (EFT) and electronic inquiry for claim status and patient eligibility.
- EOB – An Explanation of Benefits (EOB) reports the disposition of an individual claim. Many EOBs may be contained within a single 835 ERA file.
- ePayer – Payer that accepts electronic claims from the clearinghouse.
- Fiscal Intermediary – A fiscal intermediary performs services on behalf of health-care payers. These services include claim adjudication, reimbursement, and collections. Trailblazer Health Enterprises is an example of a fiscal intermediary that acts on behalf of Medicare. Trailblazer receives claims from the VA in the form of an 837 file and then adjudicates the claims to create an MRA 835 file.
- FSC – The FSC receives 837 Health Care Claim transmissions from VistA and transmits this data to the clearinghouse. FSC also receives error/informational messages and 835 Health Care Claim Payment/Advice transmissions from the clearinghouse and transmits this data to VistA.
- HIPAA – In 1996, Congress passed into law the Health Insurance Portability and Accountability Act (HIPAA). This Act is comprised of two major legislative actions: Health Insurance Reform and Administrative Simplification. The Administrative Simplification provisions of HIPAA direct the federal government to adopt national electronic standards for automated transfer of certain healthcare data between health-care payers, plans, and providers. This enables the entire healthcare industry to communicate electronic data using a single set of standards, thus eliminating all non-standard formats currently in use. Once these standards are in place, a healthcare provider will be able to submit a standard transaction for eligibility, authorization, referrals, claims, or attachments containing the same standard data content to any health plan. This will "simplify" many clinical, billing, and other financial applications, and reduces costs.
- ASC X12 (also known as ANSI ASC X12) – This is the official designation of the U.S. national [standards body](http://en.wikipedia.org/wiki/Standards_organization) for the development and maintenance of [Electronic Data Interchange](http://en.wikipedia.org/wiki/Electronic_Data_Interchange) (EDI) standards. The HIPAA transactions are based upon these standards.

## EDI Process Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc100304293" class="anchor"></span>Figure : EDI Process Flow

![](ib-2-edi-user-guide/002.png)

The above flowchart (EDI Process Flow) represents the path that electronic claims follow. The objective of electronic billing is to submit completely correct claims. Claims sent electronically reach the payer faster, are processed faster, and are paid faster than claims submitted to the payer on paper via the mail.

From the user’s desktop, the claim goes to the FSC as a VistA Mailman message. The FSC translates the claim into the HIPAA 837 Health Care Claim format and forwards the claim to the clearinghouse.

From the clearinghouse, the arrow pointing upwards represents the path claims travel if the claim can be submitted electronically to the payer. If the clearinghouse does not have an electronic connection with a payer, or if specific claims must be submitted on paper, the claim is printed at Express Bill and mailed to the payers.

Electronic claims status messages from ePayers return to the VAMCs along the same path. Payers receiving printed claims do not return electronic messages. However, the clearinghouse returns a message indicating that the claim was printed and mailed.

Different electronic edits are in place at each transmission point that may initiate the sending of a claims status message. Claim status messages returned by the clearinghouse and / or payer will provide information on a specific claim. There is no standard content for messages. The information contained within a claim status message varies from payer to payer.

# Insurance Company Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The most common cause of claims rejection is the improper setup of the insurance company and / or provider IDs within VistA. With EDI Billing, there are fields in an 837 claim transmission that are auto-populated with the data defined in VistA. This information must be accurate to generate a clean electronic claim.

## Insurance Company Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Activate New Payer to Transmit eClaims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The typical business process for setting up new payers is:

1.  The Insurance Verification Office initially enters a new payer into VistA.
2.  Lists of new payers are printed and provided to the medical center’s billing office on a regular basis (daily/weekly). Some individuals become members of the IB New Insurance mail group to receive e-mail bulletins whenever a new insurance policy is added to VistA.
3.  Billing staff uses the Insurance Company Editor to define Provider IDs: Type of Coverage; Electronic Insurance Type and Electronic Transmit? by Insurance Company. The Profession/Institutional Payer Primary and Secondary IDs are also defined using the Insurance Company Editor.
4.  Billing staff use The Insurance Company Editor to specify the correct Electronic Plan Type for each Insurance Plan.
2.  Selecting the correct electronic plan type is important. This field may determine which provider IDs are transmitted and / or printed. Choosing the wrong electronic plan type for an Insurance Plan could result in claims being rejected by the clearinghouse or by the payer.

    When Patch IB\*2\*477 is installed and a claim is authorized with more than one payer, a warning is displayed unless all the Payer IDs are on the claim.

    When Patch IB\*2\*576 is installed and a claim is sent without a Payer ID and the clearing house returns a Payer ID in the 277Stat messages that deliver clearing house claims reports, the system will update the Payer ID in the Insurance Company file if the field is BLANK. Refer to the new HCCH Payer ID Report for further detail.

#### Define EDI Settings for a Blue Cross / Blue Shield (BC/BS) Insurance Company

The steps listed below define the EDI settings for BC/BS Insurance:

1.  At the Billing Parameters screen in the Insurance Company Editor, enter BP – Billing/EDI Param.

Insurance Company Editor Oct 01, 2007@10:15:14 Page: 1 of 9

Insurance Company Information for: BLUE CROSS

Type of Company: HEALTH INSURANCE Currently Active

Billing Parameters

Signature Required?: NO Filing Time Frame:

Reimburse?: WILL REIMBURSE Type Of Coverage: HEALTH INSURAN

Mult. Bedsections: Billing Phone: XXX/XXX-XXXX

Diff. Rev. Codes: Verification Phone: XXX/XXX-XXXX

One Opt. Visit: NO Precert Comp. Name:

Amb. Sur. Rev. Code: Precert Phone: XXX/XXX-XXXX

Rx Refill Rev. Code:

EDI Parameters

Transmit?: YES-LIVE Insurance Type:

\+ Enter ?? for more actions \>\>\>

BP Billing/EDI Param RE Remarks DC Delete Company

AD Billing Addresses SY Synonyms VP View Plans

AC Associate Companies EA Edit All EX Exit

ID Prov IDs/ID Param AI (In)Activate Company

PA Payer CC Change Insurance Co.

Select Action: Next Screen//*BP Billing/EDI Param*

3.  When Patch IB\*2\*488 is installed and users create a new Insurance Company, the system will set the value of the EDI – Transmit? field in the Insurance Company Entry/Edit option, equal to YES-LIVE.

    When Patch IB\*2\*592 is installed, there will be a new Dental Payer Primary ID field. This will make it possible to route Dental claims to a different entity for processing dental claims than Institutional or Professional claims.

    When Patch IB\*2\*592 is installed, the initial Insurance Company screen will no longer have Actions for modifying each Insurance Company address. Instead, the addresses have been moved to their own Listman screen and there will be a new Action for defining an address, telephone number and FAX number for Dental claims.

The following prompts will display.

SIGNATURE REQUIRED ON BILL?: NO//

REIMBURSE?: WILL REIMBURSE//

ALLOW MULTIPLE BEDSECTIONS:

DIFFERENT REVENUE CODES TO USE:

ONE OPT. VISIT ON BILL ONLY:

AMBULATORY SURG. REV. CODE:

PRESCRIPTION REFILL REV. CODE:

FILING TIME FRAME:

TYPE OF COVERAGE: HEALTH INSURANCE//

BILLING PHONE NUMBER: XXX/XXX-XXXX//

VERIFICATION PHONE NUMBER: XXX/XXX-XXXX//

Are Precerts Processed by Another Insurance Co.?:

PRECERTIFICATION PHONE NUMBER: XXX/XXX-XXXX//

EDI - Transmit?:YES-LIVE// *YES-LIVE*

EDI - Inst Payer Primary ID: *12B30*

EDI - Alt Inst Payer Primary ID Type:

EDI - 1ST Inst Payer Sec. ID Qualifier:

EDI - Prof Payer Primary ID: *SB960*

EDI - Alt Prof Payer Primary ID Type:

EDI - 1ST Prof Payer Sec. ID Qualifier:

EDI - Dental Payer Primary ID:

EDI - Insurance Type: *GROUP POLICY* //

EDI – Print Sec/Tert Auto Claims?:

EDI – Print Medicare Sec Claims w/o MRA?:YES//

EDI - Bin Number:

4.  Patch IB\*2.0\*320 added a new security key, IB EDI INSURANCE EDIT. A user must hold this key to edit the EDI-Transmit, EDI Prof Payer ID; EDI Inst Payer ID and EDI-Insurance Type fields.
5.  At the EDI - Inst Payer Primary ID: prompt, enter the Payer Primary ID provided by the clearinghouse.
5.  Patch IB\*2.0\*488 will make changes that prevent a user from entering any value containing PRNT / prnt as a Primary Payer ID.

    When editing the Payer Primary ID fields for a commercial payer, (not BC/BS) these fields may be left blank. The clearinghouse will try to match the VistA payer name and address to an entry in its Payer Lookup Table and auto-populate these fields. Payer ID numbers are available from the PayerLists site.
6.  At the EDI - 1ST Inst Payer Sec. ID Qualifier: prompt, press the \<Enter\> key to leave field blank.
6.  Patch IB\*2\*371 added the ability to define Payer Secondary IDs. These are unusual and should only be populated if the clearinghouse or eBusiness Solutions Office provides the user with a secondary ID number.
7.  At the EDI - Prof Payer Primary ID: prompt, enter the Payer Primary ID provided by the clearinghouse.
8.  At the EDI - 1ST Prof Payer Sec. ID Qualifier: prompt, press the \<Enter\> key to leave field blank.
9.  At the EDI - Insurance Type: prompt, enter ?? to see the choices available. For this example, select Group Policy. This will result in a checkmark in the GROUP insurance box of the CMS-1500/BOX 1.
10. Press the \<Enter\> key until the Billing Parameters screen reappears.
7.  When Patch IB\*2\*371 is loaded, the patch will automatically define a Professional Payer Secondary for Medicare WNR that will have a Qualifier = Payer ID Number and an ID = VA plus the site’s ID.

EDI - Transmit?: YES-LIVE//

EDI - Inst Payer Primary ID: 12M61//

EDI - Alt Inst Payer Primary ID Type:

EDI - 1ST Inst Payer Sec. ID Qualifier:

EDI - Prof Payer Primary ID: SMTX1//

EDI - Alt Prof Payer Primary ID Type:

EDI - 1ST Prof Payer Sec. ID Qualifier: *PAYER ID X*//

EDI - 1ST Prof Payer Sec. ID: *VA999*//

8.  Patch IB\*2\*432 added the ability to define whether or not the payer will accept MRA secondary claims electronically when the primary claim was never sent to Medicare and no MRA was ever received. When the patch is loaded, this field will be set to ‘0’ which means that the claims will be transmitted electronically unless this field is changed by the site.

    This only pertains to claims that cannot be submitted thru MRA due to the service being on the Payer Excluded Service list.

    Patch IB\*2\*432 added the ability to define whether or not the payer will accept MRA secondary claims electronically when the primary claim was never sent to Medicare and no MRA was ever received. When the patch is loaded, this field will be set to ‘0’ which means that the claims will be transmitted electronically unless this field is changed by the site.

    Once Patch IB\*2\*516 is installed, a new field, Health Plan Identifier (HPID)/Other Entity Identifier (OEID), will display in the EDI Parameters section. The field will not be editable. The HPID or OEID number will come from the National Insurance File.

EDI - Dental Payer Primary ID:

EDI - Insurance Type: GROUP POLICY //

EDI - Bin Number:

EDI - UMO (278) ID:

EDI - Print Sec/Tert Auto Claims?:

EDI - Print Medicare Sec Claims w/o MRA?:

#### Define EDI Settings for a Blue Cross / Blue Shield Group Insurance Plan

The steps listed below define the EDI settings for BC/BS Group Insurance Plan:

1.  At the Billing Parameters Screen in the Insurance Company Editor, enter VP -View Plans and press the \<Enter\> key.

Insurance Company Editor Oct 01, 2007@10:15:14 Page: 1 of 9

Insurance Company Information for: BLUE CROSS

Type of Company: HEALTH INSURANCE Currently Active

Billing Parameters

Signature Required?: NO Filing Time Frame:

Reimburse?: WILL REIMBURSE Type Of Coverage: HEALTH INSURAN

Mult. Bedsections: Billing Phone: XXX/XXX-XXXX

Diff. Rev. Codes: Verification Phone: XXX/XXX-XXXX

One Opt. Visit: NO Precert Comp. Name:

Amb. Sur. Rev. Code: Precert Phone: XXX/XXX-XXXX

Rx Refill Rev. Code:

EDI Parameters

Transmit?: YES-LIVE Insurance Type: GROUP POLICY

\+ Enter ?? for more actions \>\>\>

BP Billing/EDI Param RE Remarks DC Delete Company

AD Billing Addresses SY Synonyms VP View Plans

AC Associate Companies EA Edit All EX Exit

ID Prov IDs/ID Param AI (In)Activate Company

PA Payer CC Change Insurance Co.

Select Action: Next Screen//*VP View Plans*

11. The Insurance Plan List appears. Select the appropriate plan from the list. In this example, Plan 1 is selected by typing VP=1 and pressing the Enter key.

Insurance Plan List Mar 31, 2004@16:12:52 Page: 1 of 1

All Plans for: BLUE CROSS BLUE SHIELD DEMO Insurance Company

X + =\> Indiv. Plan \* =\> Inactive Plan Pre- Pre- Ben

Group Name Group Number Type of Plan UR? Ct? ExC? As?

1 DEMO FOR TRAINING 87654 COMPREHENSIVE NO YES YES YES

Enter ?? for more actions

*VP View/Edit Plan* IP (In)Activate Plan NP New Plan

AB Annual Benefits EX Exit

Select Action: Quit// *VP=1*

12. The View/Edit Plan screen displays. To edit plan information, type PI and press the \<Enter\> key.
9.  The IB GROUP PLAN EDIT security key is required to use PI.

View/Edit Plan Mar 31, 2004@16:19:51 Page: 1 of 3

Plan Information for: BLUE CROSS Insurance Company

\*\* Plan Currently Active \*\*

Plan Information Utilization Review Info

Is Group Plan: YES Require UR: NO

Group Name: DEMO FOR TRAINING Require Amb Cert: YES

Group Number: 87654 Require Pre-Cert: YES

Type of Plan: COMPREHENSIVE MAJOR MED Exclude Pre-Cond: YES

Plan Filing TF: Benefits Assignable: YES

Plan Coverage Limitations

Coverage Effective Date Covered? Limit Comments

-------- -------------- -------- --------------

INPATIENT 02/10/04 YES

OUTPATIENT 02/10/04 YES

PHARMACY 02/10/04 NO

\+ Enter ?? for more actions

*PI Change Plan Info* IP (In)Activate Plan

UI UR Info AB Annual Benefits

CV Add/Edit Coverage CP Change Plan

PC Plan Comments EX Exit

Select Action: Next Screen// *PI* Change Plan Info

13. For this scenario, NO is typed in for the Do you wish to change this plan to an Individual Plan? field.
14. Continue to press the \<Enter\> key until Electronic Plan Type field is displayed.
15. Type in the appropriate code and press the \<Enter\> key. The chosen plan will be displayed. In this example BL has been selected.

<u>WARNING</u>: Selecting the correct electronic plan type is critical. The electronic plan type for BC/BS payers should usually be set to BL - not commercial. Choosing the wrong electronic plan type for a Group Insurance Plan could result in claims being rejected by the clearinghouse or by the payer.

10. Patch IB\*2\*432 added the ability to define two additional types of Electronic Plan Type: 17 – Dental and FI – Federal Employee Plan.

    Patch IB\*2\*436 added the ability to define an additional plan type for MediGap F and G plans. MEDIGAP (SUPPL - COINS, DED, PART B EXC).

This plan is currently defined as a Group Plan.

*Do you wish to change this plan to an Individual Plan? NO*

No change was made.

GROUP PLAN NAME: DEMO GROUP//

GROUP PLAN NUMBER: 7878787878//

TYPE OF PLAN: COMPREHENSIVE MAJOR MED

*ELECTRONIC PLAN TYPE: ?*

Enter the appropriate type of plan to be used for electronic billing.

Choose from:

16 HMO MEDICARE

MX MEDICARE A or B

TV TITLE V

MC MEDICAID

*BL BC/BS*

CH TRICARE

15 INDEMNITY

CI COMMERCIAL

HM HMO

DS DISABILITY

12 PPO

13 POS

ZZ OTHER

FI FEP – Do not use for BC/BS

17 DENTAL

ELECTRONIC PLAN TYPE: *BL BCBS*

The following screen will display.

View/Edit Plan Mar 31, 2004@16:19:51 Page: 1 of 3

Plan Information for: BLUE CROSS Insurance Company

\*\* Plan Currently Active \*\*

Plan Information Utilization Review Info

Is Group Plan: YES Require UR: NO

Group Name: DEMO FOR TRAINING Require Amb Cert: YES

Group Number: 87654 Require Pre-Cert: YES

Type of Plan: COMPREHENSIVE MAJOR MED Exclude Pre-Cond: YES

*Electronic Type: BC/BS* Benefits Assignable: YES

\+ Enter ?? for more actions

Select Action: Next Screen//

### Activate Existing Commercial Payer to Transmit eClaims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To activate an existing payer to receive electronic claims, use the Billing Parameters screen in the Insurance Company Editor. The EDI - Transmit? field on this screen must be set to YES-LIVE. In the Live mode, bills are automatically sent electronically and cannot be printed until the confirmation of a receipt message has been received from the FSC.

Follow these steps to change the EDI - Transmit? Field:

1.  On the Billing Parameters screen in the Insurance Company Editor, type BP and press the \<Enter\> key.

Insurance Company Editor Oct 01, 2007@10:40:16 Page: 1 of 8

Insurance Company Information for: AETNA

Type of Company: HEALTH INSURANCE Currently Inactive

Billing Parameters

Signature Required?: NO Filing Time Frame: 12 MOS

Reimburse?: WILL REIMBURSE Type Of Coverage: HEALTH INSURAN

Mult. Bedsections: Billing Phone:

Diff. Rev. Codes: Verification Phone:

One Opt. Visit: NO Precert Comp. Name:

Amb. Sur. Rev. Code: Precert Phone:

Rx Refill Rev. Code:

EDI Parameters

Transmit?: NO Insurance Type:

\+ Enter ?? for more actions \>\>\>

*BP Billing/EDI Param RE Remarks DC Delete CompanyAD Billing Addresses SY Synonyms VP View PlansAC Associate Companies EA Edit All EX ExitID Prov IDs/ID Param AI (In)Activate CompanyPA Payer CC Change Insurance Co.*

Select Action: Next Screen//*BP Billing/EDI Param*

11. Patch IB\*2.0\*320 added a new security key, IB EDI INSURANCE EDIT. A user must hold this key to edit the EDI-Transmit, EDI Prof Payer ID; EDI Inst Payer ID and EDI-Insurance Type fields.
16. At the EDI -Transmit? field, make sure the field is defined as YES-LIVE.
17. At the EDI - Insurance Type field, enter the correct response for the Insurance Company being edited. For this example, the correct Electronic Insurance Type is Group.
12. Except for the testing of Primary BC / BS and some secondary end to end claims, it is no longer necessary to change the EDI -Transmit? field to YES-TEST. Instead, use the new option, RCB – View/Resubmit Claims-Live or Test. Refer to Section 4.

    Once Patch IB\*2\*516 is installed, a new field, HPID / OEID, will display in the EDI Parameters section. The field will not be editable. The HPID or OEID number will come from the National Insurance File.

    Patch IB\*2\*547 will add a field, UMO (278)ID, to the EDI Parameters section which will allow users to define a primary payer identification number which will be transmitted in ASC X12N 5010 Health Care Services Review – Request for Review and Response (278) transactions.

    Patch IB\*2\*547 will add the fields, EDI - Alt Inst Payer Primary ID Type, EDI - Alt Inst Payer Primary ID, EDI - Alt Prof Payer Primary ID Type and EDI - Alt Prof Payer Primary ID, to the EDI Parameters section which will allow users to define one or more primary payer identification numbers which will be transmitted in ASC X12N 5010 Health Care Claims (837) transactions which need to be routed to contractors who adjudicate specific claim types such as claims for durable medical equipment (DME).

    Patch IB\*2\*592 will add the ability to define an EDI - Dental Payer Primary ID. The ID will then be used on Dental Claims to be routed to a different entity than institutional or professional claims when needed.

    Patch IB\*2\*608 will no longer provide the ability to select 0 - NO for EDI – Transmit.

SIGNATURE REQUIRED ON BILL?: NO//

REIMBURSE?: WILL REIMBURSE//

ALLOW MULTIPLE BEDSECTIONS: YES//

DIFFERENT REVENUE CODES TO USE:

ONE OPT. VISIT ON BILL ONLY: NO//

AMBULATORY SURG. REV. CODE:

PRESCRIPTION REFILL REV. CODE: 253//

FILING TIME FRAME: ONE YEAR//

TYPE OF COVERAGE: HEALTH INSURANCE//

BILLING PHONE NUMBER: XXX-XXX-XXXX//

VERIFICATION PHONE NUMBER: XXX-XXX-XXXX//

Are Precerts Processed by Another Insurance Co.?: NO

//

PRECERTIFICATION PHONE NUMBER: XXX-XXX-XXXX//

*EDI - Transmit?: ??*

This is the flag that says whether or not an insurance company is ready

to be billed electronically via 837/EDI functions.

Choose from:

1 YES-LIVE

2 YES-TEST

*EDI - Transmit?: 1 YES-LIVE*

EDI - Inst Payer Primary ID:

*EDI - Inst Payer Primary ID: Available from Clearinghouse*

EDI - Alt Inst Payer Primary ID Type: LTC//

EDI - Alt Inst Payer Primary ID Type: LTC//

EDI - Alt Inst Payer Primary ID: LTC1234//

Select EDI - Alt Inst Payer Primary ID Type:

*EDI - 1ST Inst Payer Sec. ID Qualifier:EDI - Prof Payer Primary ID:EDI - Prof Payer Primary ID: Available from Clearinghouse*

EDI - Alt Prof Payer Primary ID Type: LTC//

EDI - Alt Prof Payer Primary ID Type: LTC//

EDI - Alt Prof Payer Primary ID: LTC1234P//

Select EDI - Alt Prof Payer Primary ID Type:

*EDI - 1ST Prof Payer Sec. ID Qualifier:EDI - Dental Payer Primary ID:EDI – Insurance Type: ??*

Choose from:

1 HMO

2 COMMERCIAL

3 MEDICARE

4 MEDICAID

*5 GROUP POLICY*

9 OTHER

*EDI – Insurance Type: 5 GROUP POLICY*

EDI - Bin Number:

EDI - UMO (278) ID:

EDI - Print Sec/Tert Auto Claims?:

EDI - Print Medicare Sec Claims w/o MRA?:

The following steps show the user how to enter the Electronic Plan Type for a CommercialGroup Insurance Plan:

1.  At the Billing Parameters Screen in the Insurance Company Editor type in VP (View Plans) and press the \<Enter\> key.

Insurance Company Editor Oct 01, 2007@10:40:16 Page: 1 of 8

Insurance Company Information for: AETNA

Type of Company: HEALTH INSURANCE Currently Inactive

Billing Parameters

Signature Required?: NO Filing Time Frame: 12 MOS

Reimburse?: WILL REIMBURSE Type Of Coverage: HEALTH INSURAN

Mult. Bedsections: Billing Phone:

Diff. Rev. Codes: Verification Phone:

One Opt. Visit: NO Precert Comp. Name:

Amb. Sur. Rev. Code: Precert Phone:

Rx Refill Rev. Code:

EDI Parameters

Transmit?: YES-LIVE Insurance Type: GROUP POLICY

\+ Enter ?? for more actions \>\>\>

BP Billing/EDI Param RE Remarks DC Delete Company

AD Billing Addresses SY Synonyms VP View Plans

AC Associate Companies EA Edit All EX Exit

ID Prov IDs/ID Param AI (In)Activate Company

PA Payer CC Change Insurance Co.

Select Action: Next Screen//*VP View Plans*

18. The Insurance Plan List appears. In this example, Plan 1 is selected by typing VP=1 and pressing the \<Enter\> key.

Insurance Plan List Apr 14, 2004@09:21:12 Page: 1 of 1

All Plans for: AETNA Insurance Company

X + =\> Indiv. Plan \* =\> Inactive Plan Pre- Pre- Ben

Group Name Group Number Type of Plan UR? Ct? ExC? As?

1 MANAGED CHOICE 55555-111-00001 COMPREHENSIVE YES YES UNK YES

Enter ?? for more actions

*VP View/Edit Plan* IP (In)Activate Plan NP New Plan

AB Annual Benefits EX Exit

Select Action: Quit// *VP=1*

19. The View/Edit Plan screen appears. To edit plan information, type PI and press the \<Enter\> key.
13. The IB GROUP PLAN EDIT security key is required to use PI.

View/Edit Plan Apr 14, <2004@09:22:11> Page: 1 of 3

Plan Information for: AETNA Insurance Company

\*\* Plan Currently Active \*\*

Plan Information Utilization Review Info

Is Group Plan: YES Require UR: YES

Group Name: MANAGED CHOICE Require Amb Cert:

Group Number: XXXXX-XXX- Require Pre-Cert: YES

Type of Plan: COMPREHENSIVE MAJOR MED Exclude Pre-Cond:

Plan Filing TF: Benefits Assignable: YES

Plan Coverage Limitations

Coverage Effective Date Covered? Limit Comments

-------- -------------- -------- --------------

INPATIENT 02/01/04 YES

OUTPATIENT 02/01/04 YES

PHARMACY 02/01/04 NO

\+ Enter ?? for more actions

*PI Change Plan Info* IP (In)Activate Plan

UI UR Info AB Annual Benefits

CV Add/Edit Coverage CP Change Plan

PC Plan Comments EX Exit

Select Action: Next Screen// *PI Change Plan Info*

20. For this scenario, NO is entered for the Do you wish to change this plan to an Individual Plan? field.
21. Continue to press the \<Enter\> key until Electronic Plan Type field is activated.
22. Type in the appropriate code and press the \<Enter\> key. The chosen plan will be displayed. In this example CI has been selected.

<u>WARNING</u>: Selecting the correct electronic plan type is important. Choosing the wrong electronic plan type for a Group Insurance Plan could result in claims being rejected by the clearinghouse or by the payer.

This plan is currently defined as a Group Plan.

*Do you wish to change this plan to an Individual Plan? NO*

No change was made.

GROUP PLAN NAME: MANAGED CHOICE//

GROUP PLAN NUMBER: XXXXX-XXX-XXXXX//

TYPE OF PLAN: COMPREHENSIVE MAJOR MEDICAL//

*ELECTRONIC PLAN TYPE: ?*

Enter the appropriate type of plan to be used for electronic billing.

Choose from:

16 HMO MEDICARE

MX MEDICARE A or B

TV TITLE V

MC MEDICAID

BL BC/BS

CH TRICARE

15 INDEMNITY

*CI COMMERCIAL*

HM HMO

DS DISABILITY

12 PPO

13 POS

ZZ OTHER

17 Dental

FI FEP – Do not use for BC/BS

ELECTRONIC PLAN TYPE: *CI COMMERCIAL*

PLAN FILING TIME FRAME: .....

The following screen will display.

View/Edit Plan Apr 14, 2004@09:24:02 Page: 1 of 3

Plan Information for: AETNA DEMO INSURANCE Insurance Company

\*\* Plan Currently Active \*\*

Plan Information Utilization Review Info

Is Group Plan: YES Require UR: YES

Group Name: MANAGED CHOICE Require Amb Cert:

Group Number: XXXXX-XXX-XXXXX Require Pre-Cert: YES

Type of Plan: COMPREHENSIVE MAJOR MED Exclude Pre-Cond:

*Electronic Type: COMMERCIAL* Benefits Assignable: YES

\+ Enter ?? for more actions

Select Action: Next Screen//

### Activate Existing Payer to Test Primary Blue Cross / Blue Shield eClaims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Blue Cross and Blue Shield payers require the submission of test claims before accepting live claims. A member of the eBilling Team contacts someone at the facility to coordinate this testing.

14. When testing the electronic submission of secondary claims using the RCB – View/Resubmit Claims-Live or Test, it is not necessary to change Electronic Transmit? to YES-TEST nor is it necessary to print and mail claims sent using RCB.

If an eBilling Team member, request claims submitted electronically as a Live test enables the BC/BS payer to receive primary claims electronically but in a testing mode, use the Billing Parameters screen in the Insurance Company Editor. The EDI -Transmit? field on this screen must be set to YES-TEST. In testing mode, bills are automatically sent electronically and cannot be printed until the confirmation of receipt message has been received from the FSC.

The following steps show the user how to change the Electronic Transmit? field:

1.  On the Billing Parameters screen in the Insurance Company Editor, type BP and press the \<Enter\> key.

Insurance Company Editor Oct 01, 2007@10:15:14 Page: 1 of 9

Insurance Company Information for: BLUE CROSS

Type of Company: HEALTH INSURANCE Currently Active

Billing Parameters

Signature Required?: NO Filing Time Frame:

Reimburse?: WILL REIMBURSE Type Of Coverage: HEALTH INSURAN

Mult. Bedsections: Billing Phone: XXX/XXX-XXXX

Diff. Rev. Codes: Verification Phone: XXX/XXX-XXXX

One Opt. Visit: NO Precert Comp. Name:

Amb. Sur. Rev. Code: Precert Phone: XXX/XXX-XXXX

Rx Refill Rev. Code:

EDI Parameters

Transmit?: NO Insurance Type:

\+ Enter ?? for more actions \>\>\>

*BP Billing/EDI Param RE Remarks DC Delete CompanyAD Billing Addresses SY Synonyms VP View PlansAC Associate Companies EA Edit All EX ExitID Prov IDs/ID Param AI (In)Activate CompanyPA Payer CC Change Insurance Co.*

Select Action: Next Screen//*BP Billing/EDI Param*

23. At the EDI - Transmit? field, type 2 to change the field to YES-TEST. Continue to press the \<Enter\> key until the Billing Parameters screen reappears.

<u>WARNING</u>: When using the TEST mode setting for BC / BS claims for which payment is expected, it is important to note the carrier will not process bills sent in test mode. These bills mustbe printed locally and mailed in order to receive payment.

SIGNATURE REQUIRED ON BILL?: NO//

REIMBURSE?: WILL REIMBURSE//

ALLOW MULTIPLE BEDSECTIONS: YES//

DIFFERENT REVENUE CODES TO USE:

ONE OPT. VISIT ON BILL ONLY: NO//

AMBULATORY SURG. REV. CODE: 490//

PRESCRIPTION REFILL REV. CODE: 250//

FILING TIME FRAME: ONE YEAR FROM DATE OF SERVICE

TYPE OF COVERAGE: HEALTH INSURANCE//

BILLING PHONE NUMBER: XXX-XXX-XXXX//

VERIFICATION PHONE NUMBER: ITS: XXX-XXX-XXXX//

Are Precerts Processed by Another Insurance Co.?: NO

//

PRECERTIFICATION PHONE NUMBER: XXX-XXX-XXXX//

EDI - Transmit?: NO// ??

This is the flag that says whether or not an insurance company is

ready to be billed electronically via 837/EDI functions.

Choose from:

1 YES-LIVE

*2 YES-TEST*

EDI - Transmit?: 1 YES-LIVE

EDI - Inst Payer Primary ID: Available from Clearinghouse

Select EDI - Alt Inst Payer Primary ID Type:

EDI - 1ST Inst Payer Sec. ID Qualifier:

EDI - Prof Payer Primary ID: Available from Clearinghouse

Select EDI - Alt Prof Payer Primary ID Type:

EDI - 1ST Prof Payer Sec. ID Qualifier:

EDI - Dental Payer Primary ID:

EDI – Insurance Type: 5 GROUP POLICY

EDI - Bin Number:

EDI - UMO (278) ID:

EDI - Print Sec/Tert Auto Claims?:

EDI - Print Medicare Sec Claims w/o MRA?:

# Pay-to Provider(s) Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each VA database can have one or more Pay-to Providers. Each VA database must have at least one Pay-to Provider. A Pay-to Provider is the entity which is seeking payment for a claim (who will receive the payment). The Pay-to Provider can have a street address or a Post Office Box number if a physical location is not available.

With Patch IB\*2\*516, sites will gain the ability to define a second set of Pay-to Providers to be used on claims with the Rate Type of TRICARE REIMB. or TRICARE. To define the Non-Medical Care Collections Fund (MCCF) Pay-to Providers, the steps are the same as the following steps for regular Pay-to Providers. A new section has been added to the IB Site Parameters.

With Patch IB\*2\*608, sites will gain the ability to define the Rate Type to be used for Non-MCCF Pay-To Providers (formerly the TRICARE Pay-To Providers) address. The system will use the Non-MCCF Pay-To address data on claims with specified Rate Types only when the Non-MCCF Pay-To Providers address is not the same as the billing Pay-To Providers address.

IB Site Parameters Jun 16, 2014@11:34:09 Page: 3 of 5

Only authorized persons may edit this data.

\+

\[11\]Pay-To Providers : 1 defined, default - ANYTOWN VAMC

*\[12\]Non-MCCF Pay-To Providers: 0 defined*

\[13\]Inpt Health Summary: INPATIENT HEALTH SUMMARY

Opt Health Summary : OUTPATIENT HEALTH SUMMARY

\[14\]HIPPA NCPDP Active Flag : Active

\[15\]Inpatient TP Active : YES

Outpatient TP Active: YES

Pharmacy TP Active : YES

Prosthetic TP Active: YES

\[16\] EDI/MRA Activated : BOTH EDI AND MRA

EDI Contact Phone : (XXX) XXX-XXXX

\+ Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Next Screen//

## Define Default Pay-to Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

15. With Patch IB\*2\*516, two new Security Keys have been added: IB EDIT PAY-TO and IB EDIT PAY-TO TC. Users must be assigned these keys before adding or editing a Pay-to Provider.
1.  Access the option SITEMCCRSite Parameter Display/Edit.
24. From the MCCR Site Parameters screen, enter the action: IB Site Parameters.
25. Press the \<Enter\> key for Next Screen until Page 2 is displayed.
26. From the IB Site Parameters screen, enter the action: EP Edit Set.
27. Enter the number 11.
28. From the Pay-to Providers screen, enter the action: AP Add Provider.
29. From the Enter Pay-to Provider: prompt, enter ANYTOWN VAMC for this example.
16. A Pay-to Provider should be a VAMC level facility with a valid National Provider Identifier (NPI). The Pay-to Provider can be an institution outside your own database. For Example: VAMC A could process payments for services provided by VAMC B.
30. At the Are you adding 'ANYTOWN VAMC' as a new PAY-TO PROVIDERS (the 1ST for this IB SITE PARAMETERS)? No// prompt, enter YES for this example.
31. At the Pay-to Provider Name prompt, press the \<Enter\> key to accept the default name from the Institution file.
32. At the Pay-to Provider Address Line 1 prompt; press the \<Enter\> key to accept the default address from the Institution file.
33. At the Pay-to Provider Address Line 2 prompt; press the \<Enter\> key to accept the default address from the Institution file.
34. At the Pay-to Provider City prompt; press the \<Enter\> key to accept the default City from the Institution file.
35. At the Pay-to Provider State prompt; press the \<Enter\> key to accept the default State from the Institution file.
36. At the Pay-to Provider Zip Code prompt; press the \<Enter\> key to accept the default ZIP from the Institution file.
37. At the Pay-to Provider Phone Number prompt; enter the Phone Number that a payer should use to contact the site.
38. At the Pay-to Provider Federal Tax ID Number prompt; press the \<Enter\> key to accept the default Tax ID.
17. There will be a default Tax ID only when the institution selected as the Pay-to Provider is the same as the main division in the site’s database. This is taken from the IB Site Parameters.

<u>WARNING</u>*:* Do not add your site’s Tax ID if the Pay-to Provider is another VAMC. Make sure to obtain and enter the other site’s Tax ID.

18. A Pay-to Provider does not have to have an actual street address. Enter a P.O. Box as an address.

Pay-To Providers Dec 22, 2008@13:58:13 Page: 1 of 1

No Pay-To Providers defined.

\* = Default Pay-to provider

AP Add Provider DP Delete Provider RT Rate Types

EP Edit Provider AS Associate Divisions

Select Item(s): Quit// *AP Add Provider*

Enter Pay-to Provider: ANYTOWN VAMC WY M&ROC 999

Are you adding 'ANYTOWN VAMC' as a new PAY-TO PROVIDERS (the 1ST for this IB

SITE PARAMETERS)? No// *y (Yes)*

Pay-to Provider Name: ANYTOWN VAMC//

Pay-to Provider Address Line 1: REDACTED

Replace

Pay-to Provider Address Line 2: *Mail Stop 10234*

Pay-to Provider City: ANYTOWN //

Pay-to Provider State: WYOMING//

Pay-to Provider Zip Code: XXXXX-XXXX//

Pay-to Provider Phone Number: *XXX-XXX-XXXX*

Pay-to Provider Federal Tax ID Number: XX-XXXXXXX//

The following screen will display.

Pay-To Providers Dec 22, 2008@14:38:21 Page: 1 of 1

1\. *\Name : ANYTOWN VAMC State : WY

Address 1: REDACTED Zip Code: XXXXX-XXXX

Address 2: Phone :

City : ANYTOWN Tax ID : XX-XXXXXXX

*\* = Default Pay-to provider*

AP Add Provider DP Delete Provider RT Rate Types

EP Edit Provider AS Associate Divisions

Select Item(s): Quit//

When the first Pay-to Provider is entered, it becomes the default Pay-to Provider and all the divisions in the database are assigned automatically to the default provider.

39. From the Pay-to Providers screen, enter the action AS Associate Divisions.

The following screen will display.

Pay-To Provider Associations Dec 22, 2008@14:42:27 Page: 1 of 1

ANYTOWN VAMC (Default)

1 999GA ANYTOWN

2 999GC ANYTOWN

3 999GD ANYTOWN

4 999 ANYTOWN VAMROC

5 999GB ANYTOWN

6 999GE TEST MORC

Enter ?? for more actions

AS Associate Division EX Exit

Select Item(s): Quit//

## Associate Divisions with Non-Default Pay-to Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When adding a second Pay-to Provider, users will be prompted to make it the default Pay-to Provider, Is this the default Pay-To Provider? NO//. If users make the new Pay-to Provider the default provider, all divisions will be associated with the new default. If users do not make the new provider the default, then the user will have to associate select divisions with the new Pay-to Provider.

19. When there is more than one Pay-to Provider, users must associate divisions with the non-default Pay-to Provider(s).
1.  From the Pay-to Providers screen, enter the action AS Associate Divisions.

Pay-To Providers Dec 22, 2008@14:55:32 Page: 1 of 1

1\. \*Name : ANYTOWN VAMC State : WY

Address 1: REDACTED Zip Code: XXXXX-XXXX

Address 2: Phone :

City : ANYTOWN Tax ID : 99-9999999

2\. Name : ANYTOWN HEALTH CARE SYSTEM - FT. H State : MT

Address 1: VA Medical Center Zip Code: XXXXX

Address 2: Phone : XXX-XXX-XXXX

City : ANYTOWN Tax ID : XX-XXXXXXX

\* = Default Pay-to provider

AP Add Provider DP Delete Provider RT Rate Types

EP Edit Provider AS Associate Divisions

Select Item(s): Quit// *AS Associate Divisions*

The following screen will display.

Pay-To Provider Associations Dec 22, 2008@15:32:45 Page: 1 of 1

ANYTOWN VAMC (Default)

1 999GA ANYTOWN

2 999GC ANYTOWN

3 999GD ANYTOWN

4 999 ANYTOWN VAMROC

5 999GB ANYTOWN

6 999GE TEST MORC

ANYTOWN HEALTH CARE SYSTEM - ANYTOWN DIVISION

*No Divisions found.*

Enter ?? for more actions

AS Associate Division EX Exit

Select Item(s): Quit// AS Associate Division

Select Division (1-6): 5

Select Pay-To Provider: ANYTOWN

40. At the Select Item(s): prompt, enter the action AS Associate Divisions.
41. At the Division (1-6): prompt, enter 5 for this example.
42. At the Pay-to Provider: prompt, enter ANYTOWN for this example.
20. Users cannot associate a division that is defined as a Pay-to Provider to another Pay-to Provider. Users will get the following error if tried: A division used as a Pay-to Provider cannot be associated with another Pay-to Provider.
43. Repeat steps 2 - 4 if necessary.
21. Once a division has been explicitly associated with a particular Pay-to Provider, changing the default Pay-to Provider will not automatically change the division’s associated Pay-to Provider.

The following screen will display.

Pay-To Provider Associations Dec 22, 2008@15:34:39 Page: 1 of 1

ANYTOWN VAMC (Default)

1 999GA ANYTOWN

2 999GC ANYTOWN

3 999GD ANYTOWN

4 999 ANYTOWN VAMROC

5 999GE TEST MORC

ANYTOWN HEALTH CARE SYSTEM - ANYTOWN DIVISION

*6 999GB SIDNEY*

Enter ?? for more actions

AS Associate Division EX Exit

Select Item(s): Quit//

## Rate Types for Non-MCCF Pay-to Provider

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

22. Users with access to IB Site Parameters and IB EDIT PAY-TO TC security key will be able to add and delete a Rate Type.

When Patch IB\*2\*623 is installed at the site, the Non-MCCF Rate Types will be populated with the following rate types:

- CHAMPVA REIMB. INS.
- CHAMPVA
- TRICARE REIMB. INS.
- TRICARE
- TRICARE DES
- TRICARE SCI
- TRICARE TBI
- TRICARE BLIND REHABILITATION
- TRICARE DENTAL
- TRICARE PHARMACY
- INTERAGENCY
- INELIGIBLE
- INELIGIBLE REIMB. INS.
- SHARING AGREEMENT

Listed below are the steps to enter Rate Types for Non-MCCF Pay-to Provider:

1.  From the Non-MCCF Pay-to Providers screen, enter the action RT Rate Types.
44. At the Select Item(s): prompt, enter the action AR Add Rate Type.
45. At the Select a Rate Type to be added prompt, enter INELIGIBLE for this example.
46. Repeat step 3 if necessary.

Non-MCCF Pay-To Providers Dec 22, 2008@14:55:32 Page: 1 of 1

1\. \*Name : ANYTOWN VAMC

Address 1: REDACTED

Address 2:

City : ANYTOWN

State : WY

Zip Code: XXXXX-XXXX

Phone :

Tax ID : XX-XXXXXXX

2\. Name : ANYTOWN HEALTH CARE SYSTEM - FT. H

Address 1: VA Medical Center

Address 2:

City : ANYTOWN

State : MT

Zip Code: XXXXX

Phone : XXX-XXX-XXXX

Tax ID : XX-XXXXXXX

\* = Default Pay-to provider

AP Add Provider DP Delete Provider RT Rate Types

EP Edit Provider AS Associate Divisions

Select Item(s): Quit// *RT Rate types*

The following screen will display.

Non-MCCF Rate Types Dec 10, 2019@13:32:37 Page: 1 of 1

X RTY DESCRIPTION

1\. 4 INTERAGENCY

2\. 9 SHARING AGREEMENT

3\. 12 CHAMPVA REIMB. INS.

4\. 13 CHAMPVA

5\. 14 TRICARE REIMB. INS.

6\. 15 TRICARE

7\. 18 INELIGIBLE

8\. 21 INELIGIBLE REIMB. INS.

9\. 36 DOD DISABILITY EVALUATION

10\. 37 DOD SPINAL CORD INJURY

11\. 38 DOD TRAUMATIC BRAIN INJURY

12\. 39 DOD BLIND REHABILITATION

13\. 40 TRICARE DENTAL

14\. 41 TRICARE PHARMACY

Enter ?? for more actions

AR Add Rate Type RR Remove Rate Type

Select Item(s): Quit//

# Provider ID Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Payers require the use of a variety of provider identifiers on claims submitted for adjudication. Printed claim forms have boxes where these IDs can be printed.

The general term, Provider ID, can refer to an ID that belongs to a human being such as an Attending physician or it can refer to an ID that belongs to an organization that provides healthcare services to a veteran such as a VAMC or an outside laboratory. Both VA and non-VA people and organizations have IDs.

IDs have qualifiers that identify what type of ID is being transmitted. For example, a Blue Cross ID is transmitted with a qualifier (1A) which indicates that this number is a Blue Cross number. Appendix C has a list of qualifiers and which ones can be transmitted in which 837 records.

The NPI (National Provider Identifier) is a HIPAA requirement with a usage requirement date beginning May 23, 2007. The NPI is transmitted on 837 records along with treating specialty taxonomies from the National Uniform Claims Committee (NUCC) published code list.

Patch IB\*2.0\*343 added the ability to define the NPI and Taxonomy Codes for the VAMC, Non-VA facilities, and both VA and Non-VA human providers.

Patches IB\*2.0\*348 and 349 added the ability to print the NPI on the new UB-04 and CMS-1500 claim forms.

After Patch IB\*2\*436, old claims can be reprinted locally for legal purposes and sent to Regional Counsel even though the original claim was created prior to the requirement for providers to have an assigned NPI. A legal claim is defined as having a Billing Rate Type of “NO FAULT INS”, “WORKERS’ COMP”, or “TORT FEASOR.”

When Patch IB\*2.0\*432 is loaded, the Social Security Number (SSN) will no longer be transmitted in the 837 records as a human providers Primary ID. The NPI will be transmitted in the 837 Health Care Claim transmission as the Primary ID for both human providers and organizational providers such as the Billing Provider.

The HIPAA 837 transaction set includes a number of segments in which to transmit multiple IDs and qualifiers for a single claim. The list below indicates the VistA record name, the type of information being transmitted, the maximum number of IDs that can go in that record for one claim and if the IDs will print on a paper claim (P), transmit electronically (T), or do both (B).

<table>
<caption><p><span id="_Toc100304282" class="anchor"></span>Table : ID Definition VistA</p></caption>
<colgroup>
<col style="width: 21%" />
<col style="width: 42%" />
<col style="width: 19%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>Segment</th>
<th>Type of ID</th>
<th>Max # of IDs</th>
<th>(P)rint<br />
(T)ransmit<br />
(B)oth</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRV:9</td>
<td>Billing Provider Primary ID</td>
<td>1</td>
<td>B</td>
</tr>
<tr class="even">
<td>PRV1:6</td>
<td>Pay-to Provider Primary ID</td>
<td>1</td>
<td>T</td>
</tr>
<tr class="odd">
<td>CI1A:2-17</td>
<td>Billing Provider Secondary IDs</td>
<td>8</td>
<td>B</td>
</tr>
<tr class="even">
<td>OPR1</td>
<td>Attending, Other Operating or Operating Physician Primary ID</td>
<td>1/Physician</td>
<td>B</td>
</tr>
<tr class="odd">
<td>OPR1</td>
<td>Referring Provider Primary ID</td>
<td>1/Provider</td>
<td>B</td>
</tr>
<tr class="even">
<td>OPR7</td>
<td>Supervising Provider Primary ID</td>
<td>1/Provider</td>
<td>B</td>
</tr>
<tr class="odd">
<td>OPR9</td>
<td>Rendering Provider Primary ID</td>
<td>1</td>
<td>B</td>
</tr>
<tr class="even">
<td>OPRB</td>
<td>Assistant Surgeon Primary ID</td>
<td>1</td>
<td>B</td>
</tr>
<tr class="odd">
<td>OPR2</td>
<td>Attending Physician Secondary IDs</td>
<td>5</td>
<td>B</td>
</tr>
<tr class="even">
<td>OPRA</td>
<td>Rendering Provider Secondary ID</td>
<td>4</td>
<td>B</td>
</tr>
<tr class="odd">
<td>OPR3</td>
<td>Operating Physician Secondary IDs</td>
<td>5</td>
<td>B</td>
</tr>
<tr class="even">
<td>OPR4</td>
<td>Other Physician Secondary IDs</td>
<td>5</td>
<td>B</td>
</tr>
<tr class="odd">
<td>OPR5</td>
<td>Referring Provider Secondary IDs</td>
<td>5</td>
<td>B</td>
</tr>
<tr class="even">
<td>OPR8</td>
<td>Supervising Provider Secondary IDs</td>
<td>5</td>
<td>B</td>
</tr>
<tr class="odd">
<td>SUB2</td>
<td>Laboratory or Facility Primary ID</td>
<td>1</td>
<td>B</td>
</tr>
<tr class="even">
<td>SUB2</td>
<td>Laboratory or Facility Secondary IDs</td>
<td>5</td>
<td>T</td>
</tr>
</tbody>
</table>

<span id="_Toc100304282" class="anchor"></span>Table : ID Definition VistA

## Table of IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table displays:

- Where IDs are defined in VistA
- Where IDs are stored in VistA
- Where IDs appear on billing forms
- Where IDs appear in the VistA option View / Print EDI Bill Extract Data (VPE)
- The EDI 837 transaction record location.

<table>
<caption><p><span id="_Toc100304283" class="anchor"></span>Table : Claim Type - Dental</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 29%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th>Defined</th>
<th>Stored</th>
<th>Displayed</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Pay-to Provider NPI</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>The Institution file is not available to Billing personnel</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Institution (#4)</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>PRV1, Piece 6</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>Pay-to Provider Primary ID (Federal Tax Number of the VAMC - Legacy</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>MCCR Site Parameter Display/Edit</p>
</blockquote></li>
<li><blockquote>
<p>IB SITE PARAMETERS (#350.9)</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>Billing Provider NPI</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>The Institution file is not available to Billing personnel</p>
</blockquote></li>
<li><blockquote>
<p>Institution (#4)</p>
</blockquote></li>
<li><blockquote>
<p>FL 56</p>
</blockquote></li>
<li><blockquote>
<p>Box 33a</p>
</blockquote></li>
<li><blockquote>
<p>PRV, Piece 9</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>Billing Provider Taxonomy Code</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>The Institution file is not available to Billing personnel</p>
</blockquote></li>
<li><blockquote>
<p>Institution (#4)</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>PRV, Piece 14</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>Billing Provider Secondary ID (Federal Tax Number of the VAMC)</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>MCCR Site Parameter Display/Edit</p>
</blockquote></li>
<li><blockquote>
<p>IB SITE PARAMETERS (#350.9)</p>
</blockquote></li>
<li><blockquote>
<p>FL 5</p>
</blockquote></li>
<li><blockquote>
<p>Box 25</p>
</blockquote></li>
<li><blockquote>
<p>CI1A, Piece 5</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>Billing Provider Secondary IDs - Legacy</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Insurance Company Entry/Edit ID Prov IDs/ID Param</p>
</blockquote></li>
<li><blockquote>
<p>FACILITY BILLING ID (#355.92)</p>
</blockquote></li>
<li><blockquote>
<p>FL 57</p>
</blockquote></li>
<li><blockquote>
<p>Box 33b</p>
</blockquote></li>
<li><blockquote>
<p>CI1A, Pieces 6-17</p>
</blockquote></li>
</ul>
<ol start="23">
<li><p>If none are defined, the default is the Federal Tax ID.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>VA - Attending, Other Operating or Operating Physician NPI</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider Self Entry (Not available to Billing personnel)</p>
</blockquote></li>
<li><blockquote>
<p>NEW PERSON (#200)</p>
</blockquote></li>
<li><blockquote>
<p>FL 76-79</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>OPR1, Piece 3, 6, or 9</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>VA – Attending Provider Taxonomy Code</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Add a New User to the System (Not available to Billing personnel); Edit an Existing User; Person Class Edit</p>
</blockquote></li>
<li><blockquote>
<p>PERSON CLASS (#8932.1)</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>OPR, Piece 17</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>VA - Referring Provider NPI</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider Self Entry (Not available to Billing personnel); Add/Edit NPI values for Providers</p>
</blockquote></li>
<li><blockquote>
<p>NEW PERSON (#200)</p>
</blockquote></li>
<li><blockquote>
<p>FL 78 or 79</p>
</blockquote></li>
<li><blockquote>
<p>Box 17b</p>
</blockquote></li>
<li><blockquote>
<p>OPR1, Piece 12</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>VA – Rendering Provider NPI</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider Self Entry (Not available to Billing personnel); Add/Edit NPI values for Providers</p>
</blockquote></li>
<li><blockquote>
<p>NEW PERSON (#200)</p>
</blockquote></li>
<li><blockquote>
<p>FL 78 or 79</p>
</blockquote></li>
<li><blockquote>
<p>24J (Rendering)</p>
</blockquote></li>
<li><blockquote>
<p>OPR9, Piece 9</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>VA - Rendering Taxonomy Code</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Add a New User to the System (Not available to Billing personnel); Edit an Existing User Person Class Edit</p>
</blockquote></li>
<li><blockquote>
<p>PERSON CLASS (#8932.1)</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>OPR9, Piece 11</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>VA - Supervising Provider NPI</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider Self Entry (Not available to Billing personnel); Add/Edit NPI values for Providers</p>
</blockquote></li>
<li><blockquote>
<p>NEW PERSON file #200</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>OPR7, Piece 7</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>VA – Assistant Surgeon NPI</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider Self Entry (Not available to Billing personnel); Add/Edit NPI values for Providers</p>
</blockquote></li>
<li><blockquote>
<p>NEW PERSON file #200</p>
</blockquote></li>
<li><blockquote>
<p>OPRB, Piece 9</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>VA – Assistant Surgeon Taxonomy Code</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Add a New User to the System (Not available to Billing personnel); Edit an Existing User Person Class Edit</p>
</blockquote></li>
<li><blockquote>
<p>PERSON CLASS (#8932.1)</p>
</blockquote></li>
<li><blockquote>
<p>OPRB, Piece 11</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>Non-VA - Attending, Other Operating or Operating Physician NPI</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Non/Other VA Provider Individual</p>
</blockquote></li>
<li><blockquote>
<p>IB NON VA/OTHER BILLING PROVIDER (#355.93)</p>
</blockquote></li>
<li><blockquote>
<p>FL 76-79</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>OPR1, Piece 3,6, or 9</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>Non-VA – Attending Provider Taxonomy Code</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Non/Other VA Provider Individual</p>
</blockquote></li>
<li><blockquote>
<p>IB NON VA/OTHER BILLING PROVIDER (#355.93)</p>
</blockquote></li>
<li><blockquote>
<p>FL 76-79</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>OPR, Piece 17</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>Non-VA – Rendering Provider NPI</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA Files</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Non/Other VA ProviderIndividual</p>
</blockquote></li>
<li><blockquote>
<p>IB NON VA/OTHER BILLING PROVIDER (#355.93)</p>
</blockquote></li>
<li><blockquote>
<p>FL 78-79</p>
</blockquote></li>
<li><blockquote>
<p>24J</p>
</blockquote></li>
<li><blockquote>
<p>OPR9, Piece 9</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>Non-VA – Referring Provider NPI</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA Files</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Non/Other VA Provider Individual</p>
</blockquote></li>
<li><blockquote>
<p>IB NON VA/OTHER BILLING PROVIDER (#355.93)</p>
</blockquote></li>
<li><blockquote>
<p>FL 78-79</p>
</blockquote></li>
<li><blockquote>
<p>17b</p>
</blockquote></li>
<li><blockquote>
<p>OPR1, Piece 12</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>Non-VA – Rendering Provider Taxonomy Code</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA Files</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Non/Other VA Provider Individual</p>
</blockquote></li>
<li><blockquote>
<p>IB NON/OTHER VA BILLING PROVIDER (#355.93)</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>OPR9, Piece 11</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>Non-VA – Supervising Provider NPI</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA Files</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Non/Other VA Provider Individual</p>
</blockquote></li>
<li><blockquote>
<p>IB NON VA/OTHER BILLING PROVIDER (#355.93)</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>OPR7, Piece 7</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>VA - Attending, Other Operating or Operating Physician Secondary IDs - Legacy</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA Files</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Provider Specific IDs Provider’s Own IDs Provider IDs Furnished by Insurance Co</p>
</blockquote></li>
<li><blockquote>
<p>IB Billing Practitioner ID (#355.9)</p>
</blockquote></li>
<li><blockquote>
<p>FL 76-79</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>OPR2, OPR3, OPR4 Pieces 3, 5, 7, 9 or 11</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>VA – Rendering Provider Secondary IDs - Legacy</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA Files</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Provider Specific IDs Provider’s Own IDs Provider IDs Furnished by Insurance Co</p>
</blockquote></li>
<li><blockquote>
<p>IB Billing Practitioner ID (#355.9)</p>
</blockquote></li>
<li><blockquote>
<p>FL 78-79</p>
</blockquote></li>
<li><blockquote>
<p>Box 24J</p>
</blockquote></li>
<li><blockquote>
<p>OPRA, Pieces 2-9</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>VA – Referring Provider Secondary IDs - Legacy</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA Files</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Provider Specific IDs Provider’s Own IDs Provider IDs Furnished by Insurance Co</p>
</blockquote></li>
<li><blockquote>
<p>IB Billing Practitioner ID (#355.9)</p>
</blockquote></li>
<li><blockquote>
<p>FL 78-79</p>
</blockquote></li>
<li><blockquote>
<p>Box 17a</p>
</blockquote></li>
<li><blockquote>
<p>OPR5, Pieces 2-10</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>VA – Supervising Provider Secondary IDs - Legacy</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA Files</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Provider Specific IDs Provider’s Own IDs Provider IDs Furnished by Insurance Co</p>
</blockquote></li>
<li><blockquote>
<p>IB Billing Practitioner ID (#355.9)</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>OPR8, Pieces 2-11</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>VA – Assistant Surgeon Secondary IDs - Legacy - N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Non - VA - Attending, Other Operating or Operating Physician Secondary IDs - Legacy</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA Files</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Non/Other VA Provider ID Information Provider ID Maintenance Provider Specific IDs Provider’s Own IDs Provider IDs Furnished by Insurance Co</p>
</blockquote></li>
<li><blockquote>
<p>IB Billing Practitioner ID (#355.9)</p>
</blockquote></li>
<li><blockquote>
<p>FL 76-79</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>OPR2, OPR3, OPR4 Pieces 2-11</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>Non - VA – Rendering Provider Secondary IDs - Legacy</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA Files</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Non/Other VA Provider ID Information Provider ID Maintenance Provider Specific IDs Provider’s Own IDs Provider IDs Furnished by Insurance Co</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>IB Billing Practitioner ID (#355.9)</p>
</blockquote></li>
<li><blockquote>
<p>FL 78-79</p>
</blockquote></li>
<li><blockquote>
<p>Box 24J</p>
</blockquote></li>
<li><blockquote>
<p>OPRA, Pieces 2-9</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>Non-VA - Referring Provider Secondary IDs - Legacy</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA Files</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Provider Specific IDs Provider’s Own IDs Provider IDs Furnished by Insurance Co</p>
</blockquote></li>
<li><blockquote>
<p>IB Billing Practitioner ID (#355.9)</p>
</blockquote></li>
<li><blockquote>
<p>FL 78-79</p>
</blockquote></li>
<li><blockquote>
<p>Box 17a</p>
</blockquote></li>
<li><blockquote>
<p>OPR5, Pieces 2-10</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>Non - VA – Supervising Provider Secondary IDs - Legacy</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA Files</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Non/Other VA Provider ID Information Provider ID Maintenance Provider Specific IDs Provider’s Own IDs Provider IDs Furnished by Insurance Co</p>
</blockquote></li>
<li><blockquote>
<p>IB Billing Practitioner ID (#355.9)</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>OPR8, Pieces 2-11</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>VA - Service Facility – Laboratory or Facility NPI</td>
<td>After Patch IB*2*400, only VA facility types that do not have NPIs (e.g., Mobile Outreach Clinic [MORC]) are used as VA Service Facilities. Most often the Service Facility is blank.</td>
<td></td>
</tr>
<tr class="odd">
<td>VA - Service Facility – Laboratory or Facility Federal Tax ID</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>MCCR Site Parameter Display/Edit; Insurance Company Entry/Edit</p>
</blockquote></li>
<li><blockquote>
<p>IB SITE PARAMETERS (#350.9)</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>SUB, Piece 9</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>VA - Service Facility – Laboratory or Facility Secondary IDs - Legacy</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Insurance Company Entry/Edit ID Prov IDs/ID Param VA-Lab/Facility IDs</p>
</blockquote></li>
<li><blockquote>
<p>FACILITY BILLING ID (#355.92)</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>Box 32b</p>
</blockquote></li>
<li><blockquote>
<p>SUB2, Pieces 7-16</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>Non-VA - Service Facility – Laboratory or Facility NPI</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Non/Other VA Provider ID Information Facility Facility Info</p>
</blockquote></li>
<li><blockquote>
<p>IB NON VA/OTHER BILLING PROVIDER file #355.93</p>
</blockquote></li>
<li><blockquote>
<p>N/A</p>
</blockquote></li>
<li><blockquote>
<p>Box 32a</p>
</blockquote></li>
<li><blockquote>
<p>SUB2, Piece 6</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>Non-VA - Service Facility – Laboratory or Facility Secondary IDs - Legacy</td>
<td><ul>
<li><blockquote>
<p>VistA Option</p>
</blockquote></li>
<li><blockquote>
<p>VistA File</p>
</blockquote></li>
<li><blockquote>
<p>UB-04</p>
</blockquote></li>
<li><blockquote>
<p>CMS-1500</p>
</blockquote></li>
<li><blockquote>
<p>VPE (837 Record)</p>
</blockquote></li>
</ul></td>
<td><ul>
<li><blockquote>
<p>Provider ID Maintenance Non/Other VA Provider ID Information FacilitySecondary ID Maint</p>
</blockquote></li>
<li><blockquote>
<p>IB BILLING PRACTITIONER ID (#355.9)</p>
</blockquote></li>
<li><blockquote>
<p>Not Printed</p>
</blockquote></li>
<li><blockquote>
<p>32b</p>
</blockquote></li>
<li><blockquote>
<p>SUB2, Pieces 7-16</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc100304283" class="anchor"></span>Table : Claim Type - Dental

## Pay-to Provider IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Define the Pay-to Provider Primary ID / NPI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pay-to Provider NPI is not entered or maintained by Billing personnel. The Pay-to Provider NPI is retrieved from the Institution file (#4).

Beginning with Patch IB\*2\*432, the Pay-to Provider Primary ID is the NPI number of the site defined as the Pay-to Provider. The Federal Tax Number is defined when the Pay-to Provider is defined but will no longer be used as the Primary ID. Refer to Section 3.1.

### Define the Pay-to Provider Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With Patch IB\*2\*400, the CI1B segment was added to the outbound 837 claim transmission map to transmit Pay-to Provider Secondary IDs if the need should arise in the future. The CI1B segment was removed with Patch IB\*2\*432.

## Billing Provider IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Billing Provider Primary ID and the Billing Provider Secondary IDs are IDs that identify the facility at which the patient service was provided. This is a facility with a physical location (street address). The Billing Provider on a claim must be one of the following Facility Types that have been assigned NPI numbers:

- CBOC – Community Based Outpatient Clinic
- HCS – Health Care System
- M&ROC – Medical and Regional Office Center
- OC – Outpatient Clinic (Independent)
- OPC – Out Patient Clinic
- PHARM – Pharmacy
- VAMC – VA Medical Center
- RO-OC – Regional Office – Outpatient Clinic

When care is provided at any other facility type (i.e., a mobile unit), the Billing Provider becomes the Parent facility as defined in the Institution file (#4) and the mobile unit becomes the Service Facility.

With Patch IB\*2\*432, the name for the Billing Provider on a claim is extracted from the new Billing Facility Name field (#200) of the Institution file (#4). If this field is not populated, the IB software continues to extract the name from the .01 field of the Institution file.

### Define the Billing Provider Primary ID / NPI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all claims generated by the VA, the Billing Provider Secondary ID is the Federal Tax Number of the site. Once defined, the IB software will automatically assign this ID to a claim.

The Billing Provider NPI is the Billing Provider Primary ID. The Billing Provider NPI is defined in the Institution file. Once defined, the IB software automatically assigns this ID to a claim.

The VA Billing Provider NPI and Taxonomy Code will not be entered or maintained by Billing personnel. Users may change the default Billing Provider taxonomy code for a claim but users cannot change the Billing Provider NPI.

1.  Access the option SITEMCCR Site Parameter Display/Edit.
47. From the MCCR Site Parameters screen, enter the action: IB Site Parameters.
48. Press the \<Enter\> key for Next Screen until Page 2 is displayed.
49. From the IB Site Parameters screen, enter the action: EP Edit Set.
50. Enter the number 9.
51. At the Federal Tax Number prompt, enter the site’s Federal Tax Number.

IB Site Parameters Oct 20, 2005@16:23:16 Page: 2 of 6

Only authorized persons may edit this data.

\[5\] Medical Center : ANYTOWN VAMC Default Division : REDACTED

MAS Service : PATIENT ELIGIBILITY Billing Supervisor : REDACTED

\[6\] Initiator Authorize: YES Xfer Proc to Sched : NO

Ask HINQ in MCCR : YES Use Non-PTF Codes : YES

Multiple Form Types: YES Use OP CPT screen : YES

\[7\] UB-04 Print IDs : YES UB-04 Address Col :

CMS-1500 Print IDs : YES CMS-1500 Addr Col : 28

\[8\] Default RX DX Cd : 780.99 Default ASC Rev Cd : 490

Default RX CPT Cd : Default RX Rev Cd : 251

\[9\] Bill Signer Name : \<No longer used\> Federal Tax X :

Bill Signer Title : \<No longer used\>

Remark on Each Bill: BILL X MUST BE ON ALL REMITTANCE

\+ Enter ?? for more actions

EP Edit Set EX Exit Action

Select Action: Next Screen// *ep Edit Set*

Select Parameter Set(s): (5-9): 9

NAME OF CLAIM FORM SIGNER: BUSINESS OFFICE//

TITLE OF CLAIM FORM SIGNER:

FEDERAL TAX NUMBER: *XXX123456*

### Define the Billing Provider Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Billing Provider Secondary IDs are IDs and Qualifiers that are provided to a site by the insurance company. There can be a total of eight Billing Provider Secondary IDs per claim.

1.  The first ID is calculated by the system and used by the clearinghouse to sort claims.
52. The second ID is always the site’s Federal Tax ID, and the remaining six IDs must be defined by the IB staff if required.

Users can define one Billing Provider Secondary ID for a CMS-1500, and another for a UB-04 for the main division. If no other Billing Provider Secondary IDs are defined, these two IDs become the default IDs for all claims. At this time, there will not be any Billing Provider secondary IDs for Dental claims.

Billing Provider Secondary IDs can be defined by Division, Form Type, and Care Unit.

#### Define Default Billing Provider Secondary IDs by Form Type

1.  Access the option MCCR SYSTEM DEFINITION MENUInsurance Company Entry/Edit.
53. At the Select Insurance Company Name: prompt, enter Blue Cross of California for this example.
54. From the Insurance Company Editor screen, enter the action: ID Prov IDs/ID Param.
55. From the Billing Provider IDs screen, enter the action Add an ID.
56. At the Define Billing Provider Secondary IDs by Care Units? No// prompt, press the \<Enter\> key to accept the default of No.
57. At the Division prompt, accept the default for the main Division.
58. At the ID Qualifier: Electronic Plan Type// prompt, enter Blue Shield to override the default value for this example.
24. The default value for the Billing Provider Secondary ID Qualifier is still based upon the Electronic Plan Type of the patient’s insurance plan. Users now have the ability to override this default.
59. At the Form Type prompt, enter CMS-1500 for this example.
60. At the Billing Provider Secondary ID prompt, enter the ID XXXXXXXX1B for this example.
61. Repeat these steps for the Form Type = UB-04, Qualifier = Blue Cross and ID = XXXXXX1A.
25. Beginning with Patch IB\*2\*432, if no Billing Provider Secondary IDs are defined, the Federal Tax ID will no longer be used as a default value.

Billing Provider IDs (Parent) May 27, 2005@12:48:29 Page: 1 of 1

Insurance Co: BLUE CROSS OF CALIFORNIA Billing Provider Secondary IDs

ID Qualifier ID X Form Type

No Billing Provider IDs found

Enter ?? for more actions

Add an ID Additional IDs Exit

Edit an ID ID Parameters

Delete an ID VA-Lab/Facility IDs

Select Action: Quit// *a Add ID*

Define Billing Provider Secondary IDs by Care Units? No//??

Enter No to define a Billing Provider Secondary ID

for the Division.

Enter Yes to define a Billing Provider Secondary ID

for a specific Care Unit.

If no Care Unit is entered on Billing Screen 3, the

Billing Provider Secondary ID defined for the Division will

be transmitted in the claim.

0 No

1 Yes

Define Billing Provider Secondary IDs by Care Units? No//*No*

Division: Main Division// *Main Division*

ID Qualifier: Electronic Plan Type//*Blue Shield*

Enter Form Type for ID: *CMS-1500*

Billing Provider Secondary ID: *XXXXXX1B*

The following screen will display. These two IDs will be the default IDs for all claims and will appear on Billing Screen 3.

Billing Provider IDs (Parent) May 27, 2005@12:48:29 Page: 1 of 1

Insurance Co: BLUE CROSS OF CALIFORNIA Billing Provider Secondary IDs

ID Qualifier ID X Form Type

Division: Name of Main Division/Default for All Divisions

*1 Blue Cross XXXXXX1A UB042 Blue Shield XXXXXX1B 1500*

Enter ?? for more actions

Add an ID Additional IDs Exit

Edit an ID ID Parameters

Delete an ID VA-Lab/Facility IDs

Select Action: Quit//

#### Define Billing Provider Secondary IDs by Division and Form Type

If an insurance company requires different Billing Provider Secondary IDs for each division, then users must define more than just the default IDs.

1.  Access the option MCCR SYSTEM DEFINITION MENUInsurance Company Entry/Edit.
62. At the Select Insurance Company Name: prompt, enter Blue Crossof California for this example.
63. From the Insurance Company Editor screen, enter the action ID Prov IDs/ID Param.
64. From the Billing Provider IDs screen, enter the action Add an ID.
65. At the Define Billing Provider Secondary IDs by Care Units? No// prompt, press the \<Enter\> key to accept the default of No.
66. At the Division prompt, override the default for the main division by entering the name of another division, Remote Clinic for this example.
67. At the ID Qualifier: Electronic Plan Type// prompt, enter Blue Shield to override the default value for this example.
68. At the Form Type prompt, enter CMS-1500 for this example.
69. At the Billing Provider Secondary ID prompt, enter the ID 1XXXXX1B for this example.
70. Repeat these steps for the Form Type = UB-04, Qualifier = Blue Cross and ID = 1XXXXX1A.
26. Users may repeat these steps to define different Billing Provider Secondary IDs for each division if required by the insurance company.

Billing Provider IDs (Parent) May 27, 2005@12:48:29 Page: 1 of 1

Insurance Co: BLUE CROSS OF CALIFORNIA Billing Provider Secondary IDs

ID Qualifier ID X Form Type

Division: Name of Main Division/Default for All Divisions

1 Blue Cross XXXXXX1A UB04

2 Blue Shield XXXXXX1B 1500

Enter ?? for more actions

Add an ID Additional IDs Exit

Edit an ID ID Parameters

Delete an ID VA-Lab/Facility IDs

Select Action: Quit// *a Add ID*

Define Billing Provider Secondary IDs by Care Units? No//*No*

Division: Main Division// *Remote Clinic*

ID Qualifier: Electronic Plan Type//*Blue Shield*

Enter Form Type for ID: *CMS-1500*

Billing Provider Secondary ID: *1XXXXX1B*

The following screen will display:

27. The two IDs for the Remote Clinic division are available to the clerk on Billing Screen 3 for claims for services provided by this division.

Billing Provider IDs May 27, 2005@12:48:29 Page: 1 of 1

Insurance Co: BLUE CROSS OF CALIFORNIA Billing Provider Secondary IDs

ID Qualifier ID X Form Type

Division: Name of Main Division/Default for All Divisions

1 Blue Cross XXXXXX1A UB04

2 Blue Shield XXXXXX1B 1500

Division: Remote Clinic

*3 Blue Cross 1XXXXX1A UB044 Blue Shield 1XXXXX1B 1500*

Enter ?? for more actions

Add an ID Additional IDs Exit

Edit an ID ID Parameters

Delete an ID VA-Lab/Facility IDs

Select Action: Quit//

#### Define Billing Provider Secondary IDs by Division, Form Type and Care Unit

If an insurance company requires different Billing Provider Secondary IDs for services provided by particular Care Units, users can define the IDs by Division, Form Type, and Care Unit.

1.  Access the option MCCR SYSTEM DEFINITION MENUInsurance Company Entry/Edit.
71. At the Select Insurance Company Name: prompt, enter Blue Cross of California for this example.
72. From the Insurance Company Editor screen, enter the action ID Prov IDs/ID Parameters.
73. From the Billing Provider IDs screen, enter the action Add an ID.
74. At the Define Billing Provider Secondary IDs by Care Units? No// prompt, enter YES to override the default.
75. At the Division prompt, press the \<Enter\> key to accept the default for the Main Division.
76. At the Care Unit: prompt, enter ?? to see a pick list of available Care Units.
28. Refer to Section 3.4.2 to learn how to create this list of available Care Units.
77. At the Care Unit: prompt, enter Anesthesia for this example.
78. At the ID Qualifier: Electronic Plan Type// prompt, enter Blue Shield to override the default value for this example.
79. At the Form Type prompt, enter CMS-1500 for this example.
80. At the Billing Provider Secondary ID prompt, enter the ID 11XXXX1B for this example.
81. Repeat these steps for the Form Type = UB-04, Qualifier = Blue Cross and ID = 11XXXX1A.
82. Repeat these steps for Care Units Reference Lab and Home Health.

Billing Provider IDs May 27, 2005@12:48:29 Page: 1 of 1

Insurance Co: BLUE CROSS OF CALIFORNIA Billing Provider Secondary IDs

ID Qualifier ID X Form Type

Division: Name of Main Division/Default for All Divisions

1 Blue Cross XXXXXX1A UB04

2 Blue Shield XXXXXX1B 1500

Division: Remote Clinic

3 Blue Cross 1XXXXX1A UB04

4 Blue Shield 1XXXXX1B 1500

Enter ?? for more actions

Add an ID Additional IDs Exit

Edit an ID ID Parameters

Delete an ID VA-Lab/Facility IDs

Select Action: Quit// a Add ID

Define Billing Provider Secondary IDs by Care Units? No//*??*

Enter No to define a Billing Provider Secondary ID

for the Division.

Enter Yes to define a Billing Provider Secondary ID

for a specific Care Unit.

If no Care Unit is entered on Billing Screen 3, the

Billing Provider Secondary ID defined for the Division will

be transmitted in the claim.

0 No

1 Yes

Define Billing Provider Secondary IDs by Care Units? No//*1 Yes*

Division: Main Division// Main Division

Care Unit:*??*

Select a Care Unit from the list:

1 Anesthesia

2 Reference Lab

3 Home Health

Care Unit: *1 Anesthesia*

ID Qualifier: Electronic Plan Type//*Blue Shield*

Enter Form Type for ID: *CMS-1500*

Billing Provider Secondary ID: *XXXXXX1B*

The following screen will display.

Billing Provider IDs May 27, 2005@12:48:29 Page: 1 of 1

Insurance Co: BLUE CROSS OF CALIFORNIA Billing Provider Secondary IDs

ID Qualifier ID X Form Type

Division: Name of Main Division/Default for All Divisions

1 Blue Cross XXXXXX1A UB04

2 Blue Shield XXXXXX1B 1500

*Care Unit: Anesthesia3 Blue Cross 11XXXX1A UB044 Blue Shield 11XXXX1B 1500Care Unit: Reference Lab5 Blue Cross 12XXXX1A UB046 Blue Shield 12XXXX1B 1500Care Unit: Home Health7 Blue Cross 13XXXX1A UB048 Blue Shield 13XXXX1B 1500*

\+

Enter ?? for more actions

Add an ID Additional IDs Exit

Edit an ID ID Parameters

Delete an ID VA-Lab/Facility IDs

Select Action: Quit//

29. If users want a default Billing Provider Secondary ID to populate Billing Screen 3, define a default ID for the division and define IDs for the division and specific care units. Users can then accept the default ID or override the ID with one of the Care Unit IDs during the creation of a claim.

#### Define Additional Billing Provider Secondary IDs by Division and Form Type

In addition to the Billing Provider Secondary ID that appears on Billing Screen 3 for each insurance company on the bill, there can be five additional Billing Provider Secondary IDs that will be transmitted with claims for an insurance company.

Prior to Patch IB\*2.0\*320, the IDs defined in IB Site Parameters, Section 14 and Provider ID Maintenance, Number 3, were transmitted with all claims to all payers. These options for defining IDs were removed with Patch IB\*2.0\*320.

If an insurance company requires additional Billing Provider Secondary IDs, users can define the IDs in Insurance Company Entry/Edit.

1.  Access the option MCCR SYSTEM DEFINITION MENUInsurance Company Entry/Edit.
83. At the Select Insurance Company Name: prompt, enter Blue Cross of California for this example.
84. From the Insurance Company Editor screen, enter the action: ID Prov IDs/ID Param.
85. From the Billing Provider IDs screen, enter the action Additional IDs.
86. From the Billing Provider IDs – Additional Billing Provider Sec. IDs screen, enter the action Add an ID.
87. At the ID Qualifier: prompt, enter Medicare for this example.
30. There cannot be two Billing Provider Secondary IDs on a claim with the same Qualifier. If the user enters an ID with the same Qualifier here as one defined under Billing Provider Secondary IDs for the Division on a claim, the Additional Billing Provider Secondary ID with the same Qualifier will not be transmitted on the claim.
88. At the Form Type prompt, enter CMS-1500 for this example.
89. At the Billing Provider Secondary ID prompt, enter the ID 14XXXX1C for this example.
90. Repeat these steps for the Form Type = UB-04, Qualifier = Medicare, ID = 14XXXX1C.
31. Users can repeat these steps to define multiple additional Billing Provider Secondary IDs if required by the insurance company.

Billing Provider IDs (Parent) May 27, 2005@12:48:29 Page: 1 of 1

Insurance Co: BLUE CROSS OF CALIFORNIA Additional Billing Provider Sec. IDs

ID Qualifier ID X Form Type

No Additional Billing Provider IDs found

Enter ?? for more actions

Add an ID Delete an ID Exit

Edit an ID Copy IDs

Select Action: Quit// *Add an ID*

Type of ID: *Medicare*

Form Type: *1500*

Billing Provider Secondary ID: *14XXXX1C*

The following screen will display.

Billing Provider IDs (Parent) May 27, 2005@12:48:29 Page: 1 of 1

Insurance Co: BLUE CROSS OF CALIFORNIA Additional Billing Provider Sec. IDs

ID Qualifier ID X Form Type

Division: Name of Main Division/Default for All Divisions

*1 Medicare 14XXXX1C UB042 Medicare 14XXXX1C 1500*

Enter ?? for more actions

Add an ID Delete an ID Exit

Edit an ID Copy IDs

Select Action: Quit// Add an ID

Type of ID: Medicare

Form Type: UB-04

Billing Provider Secondary ID: XXXXXXX11

## Service Facility IDs (Laboratory or Facility IDs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The 837 claims transmission records contain Service Facility data like the name and address of a facility and primary and secondary IDs for that facility. Often this is an outside, non-VA facility. These IDs are called the Laboratory or Facility Primary ID and the Laboratory or Facility Secondary IDs.

If there is a non-VA facility on a claim because a veteran received care at an outside laboratory or a private hospital or clinic, an insurance company can require the claim to contain primary and secondary Laboratory or Facility IDs for the organization that provided the care.

If there is not an outside facility on a claim, but the care was provided by the VA at a facility such as a Mobile clinic, an insurance company can require the claim to contain primary and secondary Laboratory or Facility IDs for the clinic.

Patch IB\*2.0\*320 provided enhancements to allow users to more easily define Laboratory or Facility IDs for the VA or non-VA.

Beginning with Patches IB\*2.0\*348 and 349, the Service Facility NPI will be printed on locally printed CMS-1500 claims.

Beginning with Patch IB\*2.0\*400, the Service Facility loop will not be populated if the care was provided at a VA location that has an NPI such as a CBOC, VAMC, or Pharmacy.

The non-VA Service Facility NPI and Taxonomy Code will be entered and maintained by Billing personnel.

### Define Non-VA Laboratory or Facility Primary IDs / NPI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For outside, non-VA facilities such as an independent laboratory, the Laboratory or Facility Primary ID should be the entity’s NPI.

In addition to the Federal Tax ID, an NPI and one or more Taxonomy Codes can be defined for outside, non-VA facilities.

1.  Access the option MCCR SYSTEM DEFINITION MENUProvider ID Maintenance.
91. At the Select Provider ID Maintenance Option: prompt, enter NF for Non-VA Facility.
92. At the Select a NON/Other VA Provider: prompt, enter IB Outside Facility for this example.
93. From the Non-VA Lab or Facility Info screen, enter the action FI for Lab/Facility Info.
94. At the Street Address: prompt, enter 123 Westbend Street for this example.
32. Effective with Patch IB\*2\*488, only a physical street address may be entered (no post office box). Any entry that begins with “P.O.” or “PO” or “Box” is prohibited.
95. At the Street Address Line 2: prompt, press the \<Enter\> key to leave blank.
96. At the City prompt, enter Long Beach for this example.
97. At the State: prompt, enter California for this example.
98. At the Zip Code prompt, enter 999999999 for this example.
33. Effective with Patch IB\*2\*488, only a 9- or 10-digit ZIP code may be entered: 999999999/99999-9999.

    With 5010, claims must be submitted with a street address and a full nine-digit zip code when reporting a non-VA service facility location.
99. At the Contact Name: prompt, enter IB,CONTACT O for this example.
100. At the Contact Phone Number: prompt, enter \###-###-#### for this example.
101. At the Contact Phone Extension: prompt, enter 123478.
102. At the ID Qualifier: prompt, press the \<Enter\> key to accept the default.
103. At the Lab or Facility Primary ID: prompt, enter 111111112.
104. At the X12 Type of Facility: prompt, enter FA - Facility for this example.
34. With Patch IB\*2\*371, FA will be sent as the Type of Facility on all institutional claims regardless of what is defined. HIPAA only allows FA on institutional claims.
105. At the Mammography Certification Number: prompt, press the \<Enter\> key to leave blank. If the user knows the Mammography number, then it can be entered here.
106. At the NPI: prompt, enter XXXXXXXXXX for this example.
35. With Patch IB\*2\*516, users will have the ability to define a Non-VA Facility as a sole-proprietorship and link the Non-VA Facility to a human provider. If a facility is linked to a human provider, then the human’s NPI may be used for both the human and the facility. The individual provider must be defined in VistA before he/she can be linked to the facility.
107. At the Select Taxonomy Code: prompt, enter 954 for this example.
108. At the OK? Prompt, press the \<Enter\> key to accept the default.
109. At the Are you adding 'General Acute Care Hospital' as a new TAXONOMY CODE (the 1ST for this IB NON/OTHER VA BILLING PROVIDER)? No// prompt, enter Yes.
110. At the Primary Code: prompt, enter Yes for this example.
111. At the Status: prompt, enter Active.
112. At the Select Taxonomy Code: prompt, press the \<Enter\> key.
36. With Patch IB\*2\*432, the ability to define the name of a contact person at the outside facility and the telephone number for that person will be available to users.
113. At the Allow future updates by FEE BASIS automatic interface? YES// prompt, press the \<Enter\> key to accept the default.
37. This question does not impact current functionality as this is part of Future Development.

STREET ADDRESS: *123 Test Street*

STREET ADDRESS LINE 2:

CITY: CHEYENNE// *Long Beach*

STATE: *CALIFORNIA*

ZIP CODE: 999999999//

CONTACT NAME: IB,CONTACT O//

CONTACT PHONE NUMBER: XXX-XXX-XXXX//

CONTACT PHONE EXTENSION: 123478//

ID Qualifier: 24 - EMPLOYER'S IDENTIFICATION X

Lab or Facility Primary ID: *111111112*//

X12 TYPE OF FACILITY: *FACILITY*//

MAMMOGRAPHY CERTIFICATION X:

SOLE PROPRIETORSHIP?: NO

NPI: XXXXXXXXXX

Select TAXONOMY CODE: *954* General Acute Care Hospital 282N000

00X

...OK? *Yes*// (Yes)

Are you adding 'General Acute Care Hospital' as

a new TAXONOMY CODE (the 1ST for this IB NON/OTHER VA BILLING PROVIDER)? No/

/ y (Yes)

PRIMARY CODE: *y YES*

STATUS: *a ACTIVE*

Select TAXONOMY CODE:

The following screen will display.

Non-VA Lab or Facility Info Jul 05, 20126@16:04:07 Page: 1 of 1

Name: IB OUTSIDE FACILITY

Address: 123 Test Street

ANYTOWN, CALIFORNIA XXXXx

Contact Name: IB,CONTACT O

Contact Phone: XXX-XXX-XXXX XXXXXXX

Type of Facility: FACILITY

Primary ID: *XXXXXXXXX*

ID Qualifier: 24 - EMPLOYER'S IDENTIFICATION X

Mammography Certification X:

NPI: *XXXXXXXXXX*

Taxonomy Code: *XXXXXXXXX(Primary)*

Allow future updates by FEE BASIS automatic interface? : YES

Enter ?? for more actions

FI Lab/Facility Info LI Lab/Facility Ins ID

LO Lab/Facility Own ID EX Exit

Select Action: Quit//

### Define Non-VA Laboratory or Facility Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For outside, non-VA facilities, users can define multiple Laboratory or Facility Secondary IDs. These IDs can be either the facility’s own IDs, such as a Clinical Laboratory Improvement Amendment (CLIA) number, or IDs assigned to the facility by an insurance company.

#### Define a non-VA Facility’s Own Laboratory or Facility Secondary IDs

1.  Access the option MCCR System Definition MenuProvider ID Maintenance.
114. At the Select Provider ID Maintenance Option: prompt, enter NF for Non-VA Facility.
115. From the Non-VA Lab or Facility Info screen, enter the action LO for Lab/Facility Own ID.
116. From the Secondary Provider ID screen, enter the action AI for Add an ID.
117. At the Enter Provider ID Qualifier prompt, enter X5 CLIA Number for this example.
118. At the Form Type Applied to: prompt, enter CMS-1500 FORMS ONLY for this example.
119. At the Care Type: prompt, enter OUTPATIENT ONLY for this example.
120. At the Enter Lab or Facility Secondary ID prompt, enter DXXXXX for this example.
38. Users may repeat these steps to define more Laboratory or Facility Secondary IDs.

Secondary Provider ID May 11, 2005@11:17:20 Page: 1 of 1

\*\* Lab or Facility’s Own IDs (No Specific Insurance Co) \*\*

Provider: IB Outside Facility (Non-VA Lab or Facility)

ID Qualifier Form Care Type IDX

No ID's found for provider

Enter ?? for more actions

AI Add an ID DI Delete an ID

EI Edit an ID EX Exit

Select Action: Quit// *AI Add an ID*

Select Provider ID Qualifier: *X5 CLIA Number*

FORM TYPE APPLIED TO: *CMS-1500 FORMS ONLY*

BILL CARE TYPE: *OUTPATIENT ONLY*

THE FOLLOWING WAS CHOSEN:

INSURANCE: ALL INSURANCE

PROV TYPE: CLIA X

FORM TYPE: CMS-1500 FORM ONLY

CARE TYPE: OUTPATIENT ONLY

Provider ID: *DXXXXX*

The following screen will display.

Secondary Provider ID May 11, 2005@11:17:20 Page: 1 of 1

\*\* Lab or Facility’s Own IDs (No Specific Insurance Co) \*\*

Provider: IB Outside Facility (Non-VA Lab or Facility)

ID Qualifier Form Care Type IDX

*1 CLIA X 1500 OUTPT DXXXXX*

Enter ?? for more actions

AI Add an ID DI Delete an ID

EI Edit an ID EX Exit

Select Action: Quit//

#### Define a non-VA Facility’s Laboratory or Facility Secondary IDs Assigned by an Insurance Company

1.  Access the option MCCR SYSTEM DEFINITION MENUProvider ID Maintenance.
121. At the Select Provider ID Maintenance Option: prompt, enter NF for Non-VA Facility.
122. From the Non-VA Lab or Facility Info screen, enter the action LI for Lab/Facility Ins ID.
123. From the Secondary Provider ID screen, enter the action AI for Add an ID.
124. At the Enter Provider ID Qualifier prompt, enter Blue Shield for this example.
125. At the Form Type Applied to: prompt, enter CMS-1500 FORMS ONLY for this example.
126. At the Care Type: prompt, enter BOTH for this example.
127. At the Enter Lab or Facility Secondary ID prompt, enter 111XXX1B for this example.
39. Users may repeat these steps to define more Laboratory or Facility Secondary IDs. A maximum of five Laboratory or Facility Secondary IDs can be defined per insurance company. A maximum of five Laboratory or Facility Secondary IDs can be transmitted in a claim.

Secondary Provider ID May 11, 2005@11:17:20 Page: 1 of 1

\*\* Lab or Facility Secondary IDs from Insurance Co \*\*

Provider: IB Outside Facility (Non-VA Lab or Facility)

Insurance Co: BLUE CROSS OF CALIFORNIA

ID Qualifier Form Care Type IDX

No ID's found for provider and selected insurance co

Enter ?? for more actions

AI Add an ID DI Delete an ID

EI Edit an ID EX Exit

Select Action: Quit// *AI Add an ID*

Select Provider ID Qualifier: *BLUE SHIELD ID*

FORM TYPE APPLIED TO: *1500 FORMS ONLY*

BILL CARE TYPE: b *BOTH INPATIENT AND OUTPATIENT*

THE FOLLOWING WAS CHOSEN:

INSURANCE: BLUE CROSS OF CALIFORNIA

PROV TYPE: BLUE SHIELD ID

FORM TYPE: 1500 FORM ONLY

CARE TYPE: BOTH INPATIENT AND OUTPATIENT

Provider ID: *111XXX1B*

The following screen will display.

Secondary Provider ID May 11, 2005@11:17:20 Page: 1 of 1

\*\* Lab or Facility Secondary IDs from Insurance Co \*\*

Provider: IB Outside Facility (Non-VA Lab or Facility)

Insurance Co: BLUE CROSS OF CALIFORNIA

ID Qualifier Form Care Type IDX

*1 BLUE SHIELD ID 1500 INPT/OUTPT 111XXX1B*

Enter ?? for more actions

AI Add an ID DI Delete an ID

EI Edit an ID EX Exit

Select Action: Quit//

### Define VA Laboratory or Facility Primary IDs / NPI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA Service Facility NPI and Taxonomy Code will not be entered or maintained by Billing personnel. Beginning with Patch IB\*2.0\*400, only those VA locations for which no NPI numbers were obtained (i.e., Mobile Outreach Clinic \[MORC\], Centralized Mail Out Pharmacy \[CMOP\]) will populate the Service Facility. Because of this, there will usually be no VA Laboratory or Facility NPI in the 837 claim transmission.

### Define VA Laboratory or Facility Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each insurance company, users can define multiple Laboratory or Facility Secondary IDs for the VA by division and form type.

1.  Access the option Patient Insurance MenuInsurance Company Entry/Edit.
128. At the Select Insurance Company Name: prompt, enter Blue Cross of California for this example.
129. From the Insurance Company Editor screen, enter the action ID Prov IDs/ID Parameters.
130. From the Billing Provider IDs screen, enter the action VA-Lab/Facility IDs.
131. From the VA-Lab/Facility IDs screen, enter the action Add an ID.
132. At the Division prompt, accept the default for the main Division.
133. At the ID Qualifier: prompt, enter Blue Shield for this example.
134. At the Form Type prompt, enter CMS-1500 for this example.
135. At the VA Lab or Facility Secondary ID prompt, enter the ID 1212XX1B for this example.
136. Repeat these steps for the Form Type = UB-04, Qualifier = Blue Cross and ID = 1212XX1A.
137. Repeat these steps for the Form Type = UB-04, Qualifier = Commercial and ID = 1313XXG2.
40. Users may repeat these steps to define more Laboratory or Facility Secondary IDs. A maximum of five Laboratory or Facility Secondary IDs can be defined per division, form, and insurance company.

VA-Lab/Facility IDs May 27, 2005@12:48:29 Page: 1 of 1

Insurance Co.: BLUE CROSS OF CALIFORNIA

VA-Lab/Facility Primary ID: XXXXXXXX

VA-Lab/Facility Secondary IDs

ID Qualifier ID X Form Type

No Laboratory or Facility IDs found

Enter ?? for more actions

Add an ID Delete an ID

Edit an ID Exit

Select Action: *Add an ID*

The following screen will display.

VA-Lab/Facility IDs May 27, 2005@12:48:29 Page: 1 of 1

Insurance Co.: BLUE CROSS OF CALIFORNIA

VA-Lab/Facility Primary ID: Federal Tax ID

VA-Lab/Facility Secondary IDs

ID Qualifier IDX Form Type

Division: Name of Main Division/Default for All Divisions

*1 Blue Cross 1212XX1A UB042 Blue Shield 1212XX1B 1500*

Division: CBOC

*3 Commercial 1313XXG2 UB04*

Enter ?? for more actions

Add an ID Delete an ID

Edit an ID Exit

Select Action: Edit//

## Attending, Operating, and Other Physicians and Rendering, Referring, and Supervising Providers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A physician can appear on a UB-04 claim form as an Attending, Operating or Other Operating Physician. Beginning with Patch IB\*2\*432, Rendering and Referring Providers can also be added to an Institutional claim. A healthcare provider (physician, nurse, physical therapist, etc.) can appear on a 1500 claim form as a Rendering, Referring or Supervising Provider. Beginning with Patch IB\*2\*592 and the introduction of the Dental claim, an Assistant Surgeon can be added to a claim for dental services. Dental claims are a type of professional claim and can have a Rendering or Assistant Surgeon and / or a Referring and Supervising Provider.

All of these healthcare providers have a primary ID. The provider’s primary ID is the provider’s NPI. These physicians / providers can also have multiple secondary IDs that are either their own IDs, or IDs provided by an insurance company.

The VA Physician’s or Provider’s NPI is stored in the New Person file. This file is not maintained by Billing personnel. The Non-VA Physician’s or Provider’s NPI is defined in Provider ID Maintenance.

A human provider’s NPI is transmitted in the 837 Health Care Claim transmission and is printed on locally printed claim forms since Patches IB\*2.0\*348 and 349.

All of these types of healthcare providers can be either VA or non-VA employees.

### Define a VA Physician / Provider’s Primary ID / NPI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA Physician’s or Provider’s SSN and NPI are stored in the New Person file (#200). These IDs should be entered when the user is originally added to the system. The provider’s Taxonomy code is entered along with the Person Class.

<u>WARNING</u>: Beginning with Patch IB\*2\*432, SSNs will continue to be defined in the New Person file for VA Providers and users may continue to define SSNs as secondary IDs for non-VA providers but VistA will no longer transmit SSNs as human providers’ Primary IDs. There will no longer be an edit check in Enter / Edit Billing Information to ensure that a provider’s SSN is available.

### Define a VA Physician / Provider’s Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Physicians and Providers can have both their own ID, such as a state medical license, and an ID provided by an insurance company.

#### Define a VA Physician / Provider’s Own Secondary IDs

Physicians and other healthcare providers are assigned IDs that identify the IDs. These IDs include an NPI that serves as their primary ID. In addition to their NPI, the Physician / Provider may also have one or more of the following types of secondary IDs:

- OB – State License Number
- EI – EIN
- SY – SSN (VA SSNs are defined in the New Person file)
- X5 – State Industrial Accident Provider Number
- 1G – Unique Provider Identification Number (UPIN)

The steps listed below define are the steps to define a VA Physician / Provider’s own secondary ID.

1.  Access the option MCCR SYSTEM DEFINITION MENUProvider ID Maintenance.
138. At the Select Provider ID Maintenance Option: prompt, enter PO for Provider Own IDs.
139. At the (V)A or (N)on-VA provider: V//: prompt, press the \<Enter\> key to accept the default.
140. At the Select V.A. PROVIDER NAME: prompt, enter IB,DOCTOR 1.
41. This screen can be accessed through the MCCR System Definition Menu. Users must hold the IB PROVIDER EDIT security key to access this option.

    With Patch IB\*2\*447, IB will prevent the user from authorizing a claim in which a human provider has an EIN or SSN consisting of anything other than nine digits.

Provider ID Maintenance Main Menu

Enter a code from the list.

Provider IDs

PO Provider Own IDs

PI Provider Insurance IDs

Insurance IDs

BI Batch ID Entry

II Insurance Co IDs

Care Units

CP Care Units for Providers

CB Care Units for Billing Provider

Non-VA Items

NP Non-VA Provider

NF Non-VA Facility

Select Provider ID Maintenance Option: *PO Provider Own IDs*

(V)A or (N)on-VA provider: *V// A PROVIDER*

Select V.A. PROVIDER NAME:*IB,DOCTOR 1*

141. At the Select Action: prompt, enter AI for Add an ID.
142. At the Select ID Qualifier: prompt, enter State License for this example.
143. At the Select LICENSING STATE: prompt, enter California for this example.
144. When asked if the user is entering California as the 1<sup>st</sup> state for this provider, enter Yes.
145. At the LICENSING STATE: prompt, press the \<Enter\> key to accept the default.
146. At the LICENSING NUMBER: prompt, enter XXXXSTATE for this example.

Physician / Provider ID Nov 02, 2005@10:24:46 Page: 1 of 1

\*\* Physician / Provider's Own IDs (No Specific Insurance Co) \*\*

Provider : IB,DOCTORB (VA PROVIDER)

ID Qualifier Form Care Type Care Unit IDX

No ID's found for provider

Enter ?? for more actions

AI Add an ID DI Delete an ID

EI Edit an ID EX Exit

Select Action: Quit// *AI Add an ID*

Select ID Qualifier: *??*

Choose from:

EIN EI

SOCIAL SECURITY NUMBER SY

STATE INDUSTRIAL ACCIDENT PROV X5

STATE LICENSE 0B

UPIN 1G

Enter the Qualifier that identifies the type of ID.

Select Provider ID Type: *0B State License*

Select LICENSING STATE: *CALIFORNIA*

Are you adding 'CALIFORNIA' as a new LICENSING STATE (the 1ST for this NEW PER

SON)? No// *y (Yes)*

LICENSING STATE: *CALIFORNIA*//

LICENSE NUMBER: *XXXXSTATE*

The following screen will display.

Physician / Provider ID Nov 02, 2005@10:24:46 Page: 1 of 1

\*\* Physician / Provider's Own IDs (No Specific Insurance Co) \*\*

Provider : IB,DOCTORB (VA PROVIDER)

ID Qualifier Form Care Type Care Unit IDX

*1 CA STATE LICENSE X XXXXSTATE*

Enter ?? for more actions

AI Add an ID DI Delete an ID

EI Edit an ID EX Exit

Select Action: Quit//

#### Define a VA Physician / Provider’s Insurance Company Secondary IDs

Physicians and other healthcare providers can be assigned secondary IDs by insurance companies. Some insurance companies assign one ID to be used by every Physician / Provider at a site. Other insurance companies assign each Physician / Provider his or her own ID. In addition to their NPI, the Physician / Provider may also have one or more of the following types of secondary IDs:

- 1A - Blue Cross
- 1B - Blue Shield
- 1C - Medicare
- 1H - CHAMPUS
- G2 - Commercial
- LU - Location \#
- N5 - Provider Plan Network
- 1G - UPIN

Listed below are the steps to define a VA Physician / Provider’s Insurance Company secondary ID.

1.  Access the option MCCR SYSTEM DEFINITION MENUProvider ID Maintenance.
147. At the Select Provider ID Maintenance Option: prompt, enter PI for Provider Insurance IDs.
148. At the (V)A or (N)on-VA provider: V//: prompt, press the \<Enter\> key to accept the default.
149. At the Select V.A. PROVIDER NAME: prompt, enter IB,DOCTOR 1.
150. At the Select Insurance Co.: prompt, enter Blue Cross of California for this example.

Provider ID Maintenance Main Menu

Enter a code from the list.

Provider IDs

PO Provider Own IDs

PI Provider Insurance IDs

Insurance IDs

BI Batch ID Entry

II Insurance Co IDs

Care Units

CP Care Units for Providers

CB Care Units for Billing Provider

Non-VA Items

NP Non-VA Provider

NF Non-VA Facility

Select Provider ID Maintenance Option: *PI Provider Insurance IDs*

(V)A or (N)on-VA provider: *V// A PROVIDER*

Select V.A. PROVIDER NAME:*IB,DOCTOR 1*

Select INSURANCE CO: *BLUE CROSS OF CALIFORNIA*

151. At the Select Action: prompt, enter AI for Add an ID.
152. At the Select ID Qualifier: prompt, enter 1B – Blue Shield for this example.
153. At the FORM TYPE APPLIED TO: prompt, enter CMS-1500 Only for this example.
154. At the BILL CARE TYPE: prompt, enter 0 for this example.
155. At the CARE UNIT: prompt, enter Surgery for this example.
156. At the PROVIDER ID: prompt, enter XXXXBSHIELD for this example.
42. Defining an insurance company provided ID for a particular Care Unit is only necessary when the insurance company assigns Physician / Provider IDs by care unit.

    Users can repeat these steps for this Physician / Provider adding more IDs from this insurance company or change insurance company or change Physician / Provider. Refer to Section 3.7 to learn about copying IDs to multiple insurance companies.

    If the user does not define a Network ID for TRICARE claims, the system will automatically include the provider’s SSN as the Network ID.

Physician / Provider ID Nov 02, 2005@10:24:46 Page: 1 of 1

\*\* Physician / Provider's IDs from Insurance Co \*\*

Provider : IB,DOCTORB (VA PROVIDER)

INSURANCE CO: BLUE CROSS OF CALIFORNIA (Parent)

ID Qualifier Form Care Type Care Unit IDX

No ID's found for provider

Enter ?? for more actions

AI Add an ID DI Delete an ID

EI Edit an ID EX Exit

Select Action: Quit// *AI Add an ID*

Select ID Qualifier: *??*

Choose from:

BLUE CROSS 1A

BLUE SHIELD 1B

CHAMPUS 1H

COMMERCIAL G2

LOCATION NUMBER LU

MEDICARE PART A 1C

MEDICARE PART B 1C

PROVIDER PLAN NETWORK N5

UPIN 1G

Enter the Qualifier that identifies the type of ID.

Select Provider ID Type: *Blue Shield*

FORM TYPE APPLIED TO: *CMS-1500 FORMS ONLY*

BILL CARE TYPE: 0 *BOTH INPATIENT AND OUTPATIENT*

Select IB PROVIDER ID CARE UNIT: *Surgery*

THE FOLLOWING WAS CHOSEN:

INSURANCE: BLUE CROSS OF CALIFORNIA

PROV TYPE: BLUE SHIELD ID

FORM TYPE: CMS-1500 FORM ONLY

CARE TYPE: BOTH INPATIENT AND OUTPATIENT

CARE UNIT: Surgery

PROVIDER ID: *XXXXBSHIELD*

The following screen will display.

Physician / Provider ID Nov 02, 2005@10:24:46 Page: 1 of 1

\*\* Physician / Provider's IDs from Insurance Co \*\*

Provider : IB,DOCTORB (VA PROVIDER)

INSURANCE CO: BLUE CROSS OF CALIFORNIA (Parent)

ID Qualifier Form Care Type Care Unit IDX

*1 BLUE SHIELD ID 1500 INPT/OUTPT XXXXBSHIELD*

Enter ?? for more actions

AI Add an ID DI Delete an ID

EI Edit an ID EX Exit

Select Action: Quit//

#### Define non-VA Physician and Provider Primary IDs / NPI

Non-VA physicians and other healthcare providers are not VistA users, so the Physicians / Providers are not normally in the New Person file unless the Physicians / Providers are also current / previous VA employees. Even if a Physician / Provider functions in both a VA and non-VA role, the SSN, NPI and Taxonomy Code of a non-VA Physician / Provider must be entered by Billing personnel using Provider ID Maintenance. Non-VA Physician / Provider primary and secondary legacy IDs are both defined the same way and the system uses the SSN as the primary ID. Refer to Section 3.4.4.1.

43. Non-VA Physician / Provider IDs can be defined through Provider ID Maintenance through PO \> Provider Own IDS or through NP \> Non- VA PROVIDER.

#### Define a non-VA Physician / Provider’s NPI

The NPI and Taxonomy Code for a non-VA Physician or Provider can be entered by Billing personnel using Provider ID Maintenance.

1.  Access the option MCCR SYSTEM DEFINITION MENUProvider ID Maintenance.
157. At the Select Provider ID Maintenance Option: prompt, enter NP for Non-VA Provider.
158. At the Select a Non-VA Provider: prompt, enter IB,OUTSIDEPROV for this example.
44. When accessing an existing entry, press ENTER to continue or, if necessary, the spelling of the provider’s name can be corrected at the NAME prompt. Names should be entered in the following format: LAST NAME,FIRST NAME MIDDLE INITIAL.

    Beginning with Patch IB\*2\*436, it will be possible to enter a provider into the VA New Person file as a VA provider and then enter that same provider in Provider Maintenance as a non-VA provider using the same name and will no longer be necessary to manipulate the name by adding a middle initial (for example).

    Users must hold the IB PROVIDER EDIT security key to access this option.

Provider ID Maintenance Main Menu

Enter a code from the list.

Provider IDs

PO Provider Own IDs

PI Provider Insurance IDs

Insurance IDs

BI Batch ID Entry

II Insurance Co IDs

Care Units

CP Care Units for Providers

CB Care Units for Billing Provider

Non-VA Items

NP Non-VA Provider

NF Non-VA Facility

Select Provider ID Maintenance Option: *NP Non-VA Provider*

Select a NON-VA PROVIDER: *IB,OUTSIDEPROV INDIVIDUAL*

For individual type entries: The name should be entered in

LAST,FIRST MIDDLE format.

Select a NON-VA PROVIDER: IB,OUTSIDEPROV INDIVIDUAL

NAME: IB,OUTSIDEPROV //:

The following screen will display.

NON-VA PROVIDER INFORMATION Dec 07, 2006@12:40:51 Page: 1 of 1

Name: IB,OUTSIDEPROV

Type: INDIVIDUAL PROVIDER

Credentials: MD

Specialty: 30

NPI:

Taxonomy Code:

Enter ?? for more actions

ED Edit Demographics PI Provider Ins ID

PO Provider Own ID EX Exit

Select Action: Quit//

159. At the Select Action: prompt, enter ED for Edit Demographics.
160. At the Credentials: prompt, press the \<Enter\> key to accept the default.
161. At the Specialty: prompt, press the \<Enter\> key to accept the default.
162. At the NPI: prompt, enter 0000000006 for this example.
163. At the Taxonomy: prompt, enter 15 Allopathic and Osteopathic Physicians – Internal Medicine Cardiovascular Disease 207RC0000X for this example.
164. At the Are you adding 'Allopathic and Osteopathic Physicians' as a new TAXONOMY CODE (the 1ST for this IB NON/OTHER VA BILLING PROVIDER)? No// prompt, enter Yes for this example.
165. At the Primary Code: prompt, enter Yes for this example.
166. At the Status: prompt, enter Active for this example.
45. A provider may have more than one Taxonomy Code.
167. At the Allow future updates by FEE BASIS automatic interface? YES// prompt, press the \<Enter\> key to accept the default.

NAME: IB,OUTSIDEPROV//

CREDENTIALS: MD//

SPECIALTY: 30//

NPI: *XXXXXXXXXX*

Select TAXONOMY CODE: *15 Allopathic and Osteopathic Physicians 207RC0000XInternal MedicineCardiovascular Disease*

Are you adding 'Allopathic and Osteopathic Physicians' as

a new TAXONOMY CODE (the 1ST for this IB NON/OTHER VA BILLING PROVIDER)? No/

/ y (Yes)

PRIMARY CODE: *y YES*

STATUS: *a ACTIVE*

Select TAXONOMY CODE:

The following screen will display.

NON-VA PROVIDER INFORMATION Jul 05, 20126@14:49:53 Page: 1 of 1

Name: IB,OUTSIDEPROV

Type: INDIVIDUAL PROVIDER

Credentials: MD

Specialty: 30

NPI: *0000000006*

Taxonomy Code: *207RC0000X (Primary)*

Allow future updates by FEE BASIS automatic interface? : YES

Enter ?? for more actions

ED Edit Demographics PI Provider Ins ID

PO Provider Own ID EX Exit

Select Action: Quit//

### Define a non-VA Physician / Provider’s Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Define a non-VA Physician / Provider’s Own IDs

Non-VA Physicians and other healthcare providers are assigned IDs that identify the IDs. After Patch IB\*2\*432, it is not necessary to define the outside provider’s SSN. The SSN will no longer serve as the Primary ID. The Primary ID will be the provider’s NPI. In addition to their provider’s SSN, the provider may also have one or more of the following types of secondary IDs:

- OB – State License Number
- EI – EIN
- TJ – Federal Taxpayer’s Number
- X5 – State Industrial Accident Provider Number
- 1G – UPIN
- SY – SSN

Listed below are the steps to define a non-VA Physician / Provider’s Own IDs.

1.  Access the option MCCR SYSTEM DEFINITION MENUProvider ID Maintenance.
168. At the Select Provider ID Maintenance Option: prompt, enter PO for Provider Own IDs.
169. At the (V)A or (N)on-VA provider: V//: prompt, enter N for Non-VA provider.
170. At the Select Non V.A. PROVIDER NAME: prompt, enter IB,OUTSIDEDOC for this example.

Provider ID Maintenance Main Menu

Enter a code from the list.

Provider IDs

PO Provider Own IDs

PI Provider Insurance IDs

Insurance IDs

BI Batch ID Entry

II Insurance Co IDs

Care Units

CP Care Units for Providers

CB Care Units for Billing Provider

Non-VA Items

NP Non-VA Provider

NF Non-VA Facility

Select Provider ID Maintenance Option: *PO Provider Own IDs*

(V)A or (N)on-VA provider: V// *n NON-VA PROVIDER*

Select Non V.A. PROVIDER NAME:*IB,OUTSIDEDOC*

171. At the Select Action: prompt, enter AI for Add an ID.
172. At the Enter Provider ID Qualifier: prompt, enter Social Security Number for this example.
173. At the FORM TYPE APPLIED TO: prompt, enter 0 for this example.
174. At the BILL CARE TYPE: prompt, enter 0 for this example.
175. At the PROVIDER ID: prompt, enter XXXXX1212 for this example.
46. Users may repeat the above steps to enter additional IDs for a Physician / Provider.

Performing Provider ID Nov 02, 2005@10:24:46 Page: 1 of 1

\*\* Performing Provider's Own IDs (No Specific Insurance Co) \*\*

Provider : IB,OUTSIDEDOC (NON-VA PROVIDER)

ID Qualifier Form Care Type Care Unit IDX

No ID's found for provider

Enter ?? for more actions

AI Add an ID DI Delete an ID

EI Edit an ID EX Exit

Select Action: Quit// *AI Add an ID*

Select ID Qualifier: *??*

Choose from:

EIN EI

SOCIAL SECURITY NUMBER SY

STATE INDUSTRIAL ACCIDENT PROV X5

STATE LICENSE 0B

UPIN 1G

Enter the Qualifier that identifies the type of ID.

Select ID Qualifier: *SY Social Security Number*

FORM TYPE APPLIED TO: *0 BOTH UB-04 AND CMS-1500 FORMS*

BILL CARE TYPE: *0 BOTH INPATIENT AND OUTPATIENT*

THE FOLLOWING WAS CHOSEN:

INSURANCE: ALL INSURANCE

PROV TYPE: SOCIAL SECURITY NUMBER

FORM TYPE: BOTH UB-04 & CMS-1500 FORMS

CARE TYPE: BOTH INPATIENT AND OUTPATIENT

PROVIDER ID: *XXXXXXXXX*

The following screen will display.

Performing Provider ID Nov 02, 2005@10:24:46 Page: 1 of 1

\*\* Performing Provider's Own IDs (No Specific Insurance Co) \*\*

Provider : IB,OUTSIDEDOC (NON-VA PROVIDER)

ID Qualifier Form Care Type Care Unit IDX

*1 SOCIAL SECURITY NUMB BOTH INPT/OUTPT XXXXXXXXX*

Enter ?? for more actions

AI Add an ID DI Delete an ID

EI Edit an ID EX Exit

Select Action: Quit//

#### Define a non-VA Physician / Provider’s Insurance Company Secondary IDs

Physicians and other healthcare providers are assigned secondary IDs by insurance companies. In addition to their provider’s own IDs, the Physicians / Providers may also have one or more of the following types of secondary IDs:

- 1A – Blue Cross
- 1B – Blue Shield
- 1C – Medicare
- 1G – UPIN
- 1H – CHAMPUS
- G2 – Commercial
- LU – Location \#
- N5 – Provider Plan Network

Listed below are the steps to define a non-VA Physician / Provider’s Own IDs.

1.  Access the option MCCR SYSTEM DEFINITION MENUProvider ID Maintenance.
176. At the Select Provider ID Maintenance Option: prompt, enter NP for Non-VA Provider.
177. At the Select a NON-VA PROVIDER: prompt, enter IB,OUTSIDEDOC.

Provider ID Maintenance Main Menu

Enter a code from the list.

Provider IDs

PO Provider Own IDs

PI Provider Insurance IDs

Insurance IDs

BI Batch ID Entry

II Insurance Co IDs

Care Units

CP Care Units for Providers

CB Care Units for Billing Provider

Non-VA Items

NP Non-VA Provider

NF Non-VA Facility

Select Provider ID Maintenance Option: *NP Non-VA Provider*

(V)A or (N)on-VA provider: *V// N Non-VA PROVIDER*

Select a NON-VA PROVIDER: *IB,OUTSIDEDOC*

Select INSURANCE CO: BLUE CROSS OF CALIFORNIA

178. At the Select Action: prompt, enter PI for Provider Ins ID.
179. At the Select INSURANCE CO: prompt, enter Blue Cross of California for this example.
180. At the Select Action: prompt, enter AI for Add an ID.
181. At the Select ID Qualifier: prompt, enter 1B – Blue Shield for this example.
182. At the FORM TYPE APPLIED TO: prompt, enter CMS-1500 Only for this example.
183. At the BILL CARE TYPE: prompt, enter 0 for this example.
184. At the PROVIDER ID: prompt, enter XXBSHIELD for this example.
47. Users can repeat these steps for this Physician / Provider adding more IDs from this insurance company or change insurance company or change Physician / Provider.

Performing Provider ID Nov 02, 2005@10:24:46 Page: 1 of 1

\*\* Performing Provider's IDs from Insurance Co \*\*

Provider : IB,OUTSIDEDOC (Non-VA PROVIDER)

INSURANCE CO: BLUE CROSS OF CALIFORNIA (Parent)

ID Qualifier Form Care Type Care Unit IDX

No ID's found for this insurance co.

Enter ?? for more actions

AI Add an ID DI Delete an ID

EI Edit an ID EX Exit

Select Action: Quit// *AI Add an ID*

Select ID Qualifier: *??*

Choose from:

BLUE CROSS 1A

BLUE SHIELD 1B

CHAMPUS 1H

COMMERCIAL G2

LOCATION NUMBER LU

MEDICARE PART A 1C

MEDICARE PART B 1C

PROVIDER PLAN NETWORK N5

UPIN 1G

Enter the Qualifier that identifies the type of ID.

Select Provider ID Type: *Blue Shield*

FORM TYPE APPLIED TO: *CMS-1500 FORMS ONLY*

BILL CARE TYPE: *0 BOTH INPATIENT AND OUTPATIENT*

THE FOLLOWING WAS CHOSEN:

INSURANCE: BLUE CROSS OF CALIFORNIA

PROV TYPE: BLUE SHIELD ID

FORM TYPE: CMS-1500 FORM ONLY

CARE TYPE: BOTH INPATIENT AND OUTPATIENT

PROVIDER ID: *XXBSHIELD*

The following screen will display.

Performing Provider ID Nov 02, 2005@10:24:46 Page: 1 of 1

\*\* Performing Provider's IDs from Insurance Co \*\*

Provider : IB,OUTSIDEDOC (Non-VA PROVIDER)

INSURANCE CO: BLUE CROSS OF CALIFORNIA (Parent)

ID Qualifier Form Care Type Care Unit IDX

*1 BLUE SHIELD ID 1500 INPT/OUTPT XXXXBSHIELD*

Enter ?? for more actions

AI Add an ID DI Delete an ID

EI Edit an ID EX Exit

Select Action: Quit//

### Define Insurance Company IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Both individual Physician / Provider secondary IDs and insurance company default Physician / Provider secondary IDs provided by an insurance company can be entered and copied from within Insurance Company IDs.

There are three options:

- I – Individual IDs
- A – Individual and Default IDs
- D – Default IDs

Option A is the basically the same as I and D combined, so users can add Physician / Provider secondary IDs and / or default secondary IDs.

#### Define Default Physician / Provider Insurance Company Secondary IDs

Users can use the Provider ID Maintenance option, Insurance Company IDs, to enter numbers that are assigned by an insurance company to be used as default Attending, Operating, Other, Rendering, Referring and Supervising Secondary IDs for all physicians and healthcare providers. These IDs with be automatically sent with all 837 claims to the insurance company for which the default IDs are defined.

1.  Access the option MCCR SYSTEM DEFINITION MENUProvider ID Maintenance.
185. At the Select Provider ID Maintenance Option: prompt, enter II for Insurance Co IDs.
186. At the Select Insurance Company Name: prompt, enter Blue Cross ofCalifornia for this example.
187. At the Select Display Content: prompt, enter D.

Provider ID Maintenance Main Menu

Enter a code from the list.

Provider IDs

PO Provider Own IDs

PI Provider Insurance IDs

Insurance IDs

BI Batch ID Entry

II Insurance Co IDs

Care Units

CP Care Units for Providers

CB Care Units for Billing Provider

Non-VA Items

NP Non-VA Provider

NF Non-VA Facility

Select Provider ID Maintenance Option: *II Insurance Co IDs*

Select INSURANCE COMPANY NAME: *BLUE CROSS OF CALIFORNIA PO BOX 99999*

ANYTOWN *CALIFORNIA Y*

SELECT DISPLAY CONTENT: A//*D INSURANCE CO DEFAULT IDS*

188. At the Select Action: prompt, enter AI for Add an ID.

INSURANCE CO PROVIDER ID Dec 19, 2005@12:24:41 Page: 1 of 2

Insurance Co: BLUE CROSS OF CALIFORNIA (Parent)

PROVIDER NAME FORM CARE TYPE CARE UNIT IDX

Provider ID Type: BLUE SHIELD

1 \<\<INS CO DEFAULT\>\> BOTH INPT/OUTPT BSDEFAULT

Provider ID Type: COMMERCIAL

2 \<\<INS CO DEFAULT\>\> BOTH INPT/OUTPT COMDEFAULT

Provider ID Type: PROVIDER PLAN NETWORK

3 \<\<INS CO DEFAULT\>\> BOTH INPT/OUTPT NETDEFAULT

Provider ID Type: UPIN

4 \<\<INS CO DEFAULT\>\> BOTH INPT/OUTPT UPINDEFAULT

\+ Enter ?? for more actions

AI Add an ID DP Display Ins Params VI View IDs by Type

DI Delete an ID CI Change Ins Co CU Care Unit Maint

EI Edit an ID CD Change Display EX Exit

Select Action: Next Screen//*AI Add an ID*

189. At the Select Provider (optional): prompt, press the \<Enter\> key to leave the prompt blank.
190. At the YOU ARE ADDING A PROVIDER ID THAT WILL BE THE INSURANCE CO DEFAULT IS THIS OK?: prompt, enter YES.
191. At the Select Provider ID Type: prompt, enter Blue Cross for this example.
192. At the FORM TYPE APPLIED TO: prompt, enter UB-04 Forms Only for this example.
193. At the BILL CARE TYPE: prompt, enter 0 for BOTH INPATIENT AND OUTPATIENT for this example.
194. At the PROVIDER ID: prompt, enter BCDEFAULT for this example.

YOU ARE ADDING A PROVIDER ID THAT WILL BE THE INSURANCE CO DEFAULT

Select Provider ID Type: *BLUE CROSS 1A*

FORM TYPE APPLIED TO: UB-04// *UB-04 FORMS ONLY*

BILL CARE TYPE: *0 BOTH INPATIENT AND OUTPATIENT*

THE FOLLOWING WAS CHOSEN:

INSURANCE: BLUE CROSS OF CALIFORNIA

PROV TYPE: BLUE CROSS

FORM TYPE: UB-04 FORM ONLY

CARE TYPE: BOTH INPATIENT AND OUTPATIENT

PROVIDER ID: *BCDEFAULT*

The following screen will display.

INSURANCE CO PROVIDER ID Dec 19, 2005@12:34:01 Page: 1 of 2

Insurance Co: BLUE CROSS OF CALIFORNIA (Parent)

PROVIDER NAME FORM CARE TYPE CARE UNIT IDX

Provider ID Type: BLUE CROSS

*1 \<\<INS CO DEFAULT\>\> UB-04 INPT/OUTPT BCDEFAULT*

Provider ID Type: BLUE SHIELD

2 \<\<INS CO DEFAULT\>\> BOTH INPT/OUTPT DEFALLProv

Provider ID Type: COMMERCIAL

3 \<\<INS CO DEFAULT\>\> BOTH INPT/OUTPT COMDEFAULT

Provider ID Type: PROVIDER PLAN NETWORK

4 \<\<INS CO DEFAULT\>\> BOTH INPT/OUTPT NETDEFAULT

\+ Enter ?? for more actions

AI Add an ID DP Display Ins Params VI View IDs by Type

DI Delete an ID CI Change Ins Co CU Care Unit Maint

EI Edit an ID CD Change Display EX Exit

Select Action: Next Screen//

48. This default ID will be transmitted on all claims where Blue Cross of California is the payer as a Physician / Provider secondary ID.

#### Define Individual Physician / Provider Insurance Company Secondary IDs

Users can use the Provider ID Maintenance option, Insurance Company IDs, to enter numbers that are assigned by an insurance company as individual Attending, Operating, Other, Rendering, Referring, and Supervising Secondary IDs.

1.  Access the option MCCR SYSTEM DEFINITION MENUProvider ID Maintenance.
195. At the Select Provider ID Maintenance Option: prompt, enter II for Insurance Co IDs.
196. At the Select Insurance Company Name: prompt, enter Blue Cross ofCalifornia for this example.

Provider ID Maintenance Main Menu

Enter a code from the list.

Provider IDs

PO Provider Own IDs

PI Provider Insurance IDs

Insurance IDs

BI Batch ID Entry

II Insurance Co IDs

Care Units

CP Care Units for Providers

CB Care Units for Billing Provider

Non-VA Items

NP Non-VA Provider

NF Non-VA Facility

Select Provider ID Maintenance Option: ii Insurance Co IDs

Select INSURANCE COMPANY NAME: *BLUE CROSS OF CALIFORNIA PO BOX XXXXX*

ANYTOWN *CALIFORNIA Y*

197. At the Select Display Content: prompt, enter I for this example.
198. At the Do you want to display IDs for a Specific Provider: prompt, enter No for this example.

SELECT DISPLAY CONTENT: A// ??

\(D\) DISPLAY CONTAINS ONLY THOSE IDS ASSIGNED AS DEFAULTS TO THE FACILITY BY

THE INSURANCE COMPANY

\(I\) DISPLAY CONTAINS ONLY THOSE IDS ASSIGNED TO INDIVIDUAL PROVIDERS BY THE

INSURANCE COMPANY

\(A\) DISPLAY CONTAINS ALL IDS ASSIGNED BY THE INSURANCE COMPANY FOR ONE OR ALL PROVIDER ID TYPES

Select one of the following:

D INSURANCE CO DEFAULT IDS

I INDIVIDUAL PROVIDER IDS FURNISHED BY THE INS CO

A ALL IDS FURNISHED BY THE INS CO BY PROVIDER TYPE

SELECT DISPLAY CONTENT: A// *I INDIVIDUAL PROVIDER IDS FURNISHED BY THE INS CO*

DO YOU WANT TO DISPLAY IDS FOR A SPECIFIC PROVIDER?: *NO*//

199. At the Select Action: prompt, enter AI for Add an ID.

INSURANCE CO PROVIDER ID Dec 15, 2005@15:36:31 Page: 1 of 89

Insurance Co: BLUE CROSS OF CALIFORNIA (Parent)

PERFORMING PROV ID MAY REQUIRE CARE UNIT

PROVIDER ID TYPE FORM CARE TYPE CARE UNIT IDX

Provider: IB,DOCTOR3

1 PROVIDER PLAN NETWOR BOTH INPT/OUTPT MDXXXXXA

Provider: IB,DOCTOR9

2 PROVIDER PLAN NETWOR BOTH INPT/OUTPT GXXXXXA

Provider: IB,DOCTOR10

3 PROVIDER PLAN NETWOR BOTH INPT/OUTPT GXXXXXX

Provider: IB,DOCTOR76

4 PROVIDER PLAN NETWOR BOTH INPT/OUTPT GXXXXXX

\+ Enter ?? for more actions

AI Add an ID DP Display Ins Params VI View IDs by Type

DI Delete an ID CI Change Ins Co CU Care Unit Maint

EI Edit an ID CD Change Display EX Exit

Select Action: Next Screen// *AI Add an ID*

200. At the Select ID Qualifier: prompt, enter 1B – Blue Shield for this example.
201. At the FORM TYPE APPLIED TO: prompt, enter CMS-1500 Only for this example.
202. At the BILL CARE TYPE: prompt, enter 0 for this example.
203. At the CARE UNIT: prompt, enter Surgery for this example.
204. At the PROVIDER ID: prompt, enter BSXXXXX for this example.

Select PROVIDER: *IB,DOCTOR7*

Select Provider ID Type: *BLUE SHIELD 1B*

FORM TYPE APPLIED TO: *CMS-1500 FORMS ONLY*

BILL CARE TYPE: *0 BOTH INPATIENT AND OUTPATIENT*

Select IB PROVIDER ID CARE UNIT: *Surgery*

THE FOLLOWING WAS CHOSEN:

INSURANCE: BLUE CROSS OF CALIFORNIA

PROV TYPE: BLUE SHIELD

FORM TYPE: CMS-1500 FORM ONLY

CARE TYPE: BOTH INPATIENT AND OUTPATIENT

CARE UNIT: Surgery

PROVIDER ID: *BSXXXXX*

The following screen will display.

INSURANCE CO PROVIDER ID Dec 15, 2005@16:11:31 Page: 49 of 89

Insurance Co: BLUE CROSS OF CALIFORNIA (Parent)

PERFORMING PROV ID MAY REQUIRE CARE UNIT

PROVIDER ID TYPE FORM CARE TYPE CARE UNIT IDX

\+

Provider: IB,DOCTOR15

194 PROVIDER PLAN NETWOR BOTH INPT/OUTPT GXXXXX

Provider: IB,DOCTOR54

195 PROVIDER PLAN NETWOR BOTH INPT/OUTPT G4XXXXX

Provider: IB,DOCTOR7

196 BLUE CROSS UB-04 INPT/OUTPT BCXXXXXXX

*197 BLUE SHIELD 1500 INPT/OUTPT Surgery BSXXXXX*

Provider: IB,DOCTOR6

\+ Enter ?? for more actions

AI Add an ID DP Display Ins Params VI View IDs by Type

DI Delete an ID CI Change Ins Co CU Care Unit Maint

EI Edit an ID CD Change Display EX Exit

Select Action: Next Screen//

### Define either a Default or Individual Physician / Provider Secondary ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Access the option MCCR SYSTEM DEFINITION MENUProvider ID Maintenance.
205. At the Select Provider ID Maintenance Option: prompt, enter II for Insurance Co IDs.
206. At the Select Insurance Company Name: prompt, enter Blue Cross of California for this example (the Parent company).
207. At the Select Display Content: prompt, enter A for this example.
208. At the DO YOU WANT TO DISPLAY IDS FOR A SPECIFIC PROVIDER ID TYPE?: NO// prompt, accept the default.

Provider ID Maintenance Main Menu

Enter a code from the list.

Provider IDs

PO Provider Own IDs

PI Provider Insurance IDs

Insurance IDs

BI Batch ID Entry

II Insurance Co IDs

Care Units

CP Care Units for Providers

CB Care Units for Billing Provider

Non-VA Items

NP Non-VA Provider

NF Non-VA Facility

Select Provider ID Maintenance Option: *II Insurance Co IDs*

Select INSURANCE COMPANY NAME: *BLUE CROSS OF CALIFORNIA PO BOX 99999LOS ANGELES CALIFORNIA Y*

SELECT DISPLAY CONTENT: *A// LL IDS FURNISHED BY THE INS CO BY PROVIDER TYPE*

DO YOU WANT TO DISPLAY IDS FOR A SPECIFIC PROVIDER ID TYPE?: *NO*//

209. At the Select Action: prompt, enter AI for Add an ID.

INSURANCE CO PROVIDER ID Dec 15, 2005@16:18:07 Page: 1 of 31

Insurance Co: BLUE CROSS OF CALIFORNIA (Parent)

PERFORMING PROV ID MAY REQUIRE CARE UNIT

PROVIDER NAME FORM CARE TYPE CARE UNIT IDX

Provider ID Type: BLUE CROSS

1 IB,DOCTOR7 UB-04 INPT/OUTPT BCXXXXX

Provider ID Type: BLUE SHIELD

2 \<\<INS CO DEFAULT\>\> BOTH INPT/OUTPT DEFALLProv

3 IB Outside Facility BOTH INPT/OUTPT BSFACXXXX

4 IB,DOCTOR8 BOTH INPT/OUTPT BSINDOUT

5 IB,DOCTOR33 BOTH INPT/OUTPT BSLIM

6 IB,DOCTOR7 1500 INPT/OUTPT BSXXXXX

Provider ID Type: PROVIDER PLAN NETWORK

7 IB,DOCTOR64 BOTH INPT/OUTPT MDXXXXXA

\+ Enter ?? for more actions

AI Add an ID DP Display Ins Params VI View IDs by Type

DI Delete an ID CI Change Ins Co CU Care Unit Maint

EI Edit an ID CD Change Display EX Exit

Select Action: Next Screen//*AI Add an ID*

49. At the Select Provider (optional) prompt, enter a Provider’s Name to enter an individual ID or leave blank to enter a default ID and then continue to define the ID as before.

*Select PROVIDER (optional):* IB,DOCTOR7

Searching for a VA PROVIDER

IB,DOCTOR7 1XXXX LZZ 114 RESIDENT PHYSICIAN

...OK? Yes// (Yes)

Select Provider ID Type: *COMMERCIAL G2*

FORM TYPE APPLIED TO: *0 BOTH UB-04 AND CMS-1500 FORMS*

BILL CARE TYPE: *0 BOTH INPATIENT AND OUTPATIENT*

THE FOLLOWING WAS CHOSEN:

INSURANCE: BLUE CROSS OF CALIFORNIA

PROV TYPE: COMMERCIAL

FORM TYPE: BOTH UB-04 & CMS-1500 FORMS

CARE TYPE: BOTH INPATIENT AND OUTPATIENT

PROVIDER ID: *CMXXXXXX*

## Care Units

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some insurance companies assign the same IDs to multiple Physician / Providers, based upon Care Units, to be used as *Physician / Provider Secondary IDs* on claims. This allows more than one person to have the same ID without everyone having the same ID.

Example: Insurance Company A assigns the number XXXXXX1 to a care unit called Care Unit A and assigns this number and care unit to Dr. A, Dr. B, Dr. C and Dr. E. as their Physician / Provider Secondary ID. The same insurance company assigns the number XXXXXX2 to a care unit called Care Unit B and assigns this number and care unit to Dr. F, Dr. G, Dr. H and Dr. I. as their Physician / Provider Secondary IDs.

Some insurance companies assign IDs to be used as *Billing Provider Secondary IDs* on claims for services performed for specific types of care.

Example: Insurance Company A assigns the number XXXXHH to be used as the Billing Provider Secondary ID (Billing Screen 3) when Home Health services are provided. The same insurance company assigns the number XXXXER as the Billing Provider Secondary ID (Billing Screen 3) when Emergency services are provided.

The names of the “care unit” used by insurance companies are specified by the insurance companies and do not relate directly to the medical services or departments of the medical center. For this reason, users must define these Care Units in Provider ID Maintenance.

### Define Care Units for Physician / Provider Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Access the option MCCR SYSTEM DEFINITION MENUProvider ID Maintenance.
210. At the Select Provider ID Maintenance Option: prompt, enter CP for Care Units for Providers.
211. At the Select INSURANCE CO: prompt, enter Blue Cross of California for this example.

Provider ID Maintenance Main Menu

Enter a code from the list.

Provider IDs

PO Provider Own IDs

PI Provider Insurance IDs

Insurance IDs

BI Batch ID Entry

II Insurance Co IDs

Care Units

CP Care Units for Providers

CB Care Units for Billing Provider

Non-VA Items

NP Non-VA Provider

NF Non-VA Facility

Select Provider ID Maintenance Option: *CP Care Units for Providers*

Select INSURANCE CO: *Blue Cross of California*

212. At the Select Action: prompt, enter AU for Add a Unit.
213. At the SELECT CARE UNIT FOR THE INSURANCE CO: prompt, enter Surgery for this example. Confirm Surgery.
214. At the IB PROVIDER ID CARE UNIT DESCRIPTION: prompt, enter a free-text description of the Care Unit.
215. At the ID Qualifier: prompt, enter Blue Shield for this example.
216. At the FORM TYPE APPLIED TO: prompt, enter 0 for BOTH UB-04 & CMS-1500 FORMS.
217. At the BILL CARE TYPE: prompt, enter 0 for BOTH INPATIENT AND OUTPATIENT.
50. Remember, ‘Blue Cross’ ID can only be used on Institutional claims.

PROVIDER ID CARE UNITS Nov 03, 2005@11:56:45 Page: 1 of 1

Insurance Co: BLUE CROSS OF CALIFORNIA

CARE UNIT NAME DESCRIPTION

No CARE UNITs Found for Insurance Co

Enter ?? for more actions

AU Add a Unit DU Delete a Unit

EU Edit a Unit EX Exit

Select Action: Quit// *AU Add a Unit*

SELECT CARE UNIT FOR THE INSURANCE CO: *Surgery*

Are you adding 'Surgery' as a new IB PROVIDER ID CARE UNIT? No// *y (Yes)*

IB PROVIDER ID CARE UNIT DESCRIPTION: Ambulatory Surgery

ID TYPE: *BLUE SHIELD*

FORM TYPE APPLIED TO: *0 BOTH UB-04 & CMS-1500 FORMS*

BILL CARE TYPE: *0 BOTH INPATIENT AND OUTPATIENT*

CARE UNIT: *Surgery*

\>\> CARE UNIT COMBINATION FILED FOR THE INSURANCE CO

PRESS ENTER TO CONTINUE

The following screen will display.

PROVIDER ID CARE UNITS Nov 03, 2005@11:56:45 Page: 1 of 1

Insurance Co: BLUE CROSS OF CALIFORNIA

CARE UNIT NAME DESCRIPTION

*1 Surgery Ambulatory Surgeryo BLUE SHIELD ID Both form types Inpt/Outpt*

Enter ?? for more actions

AU Add a Unit DU Delete a Unit

EU Edit a Unit EX Exit

Select Action: Quit//

51. Once the user has defined a Care Unit when the user goes to define Physician / Provider’s IDs furnished by an insurance company, the user will be prompted to enter the name of the Care Unit if the user enters the same ID Qualifier, Form Type, and Bill Care Type as those for which the user previously defined a Care Unit.

PROVIDER ID Nov 21, 2005@09:52:39 Page: 1 of 1

\*\* Provider IDs Furnished by Insurance Co \*\*

PROVIDER : IB,DOCTOR7 (VA PROVIDER)

INSURANCE CO: BLUE CROSS OF CALIFORNIA

PROVIDER ID TYPE FORM CARE TYPE CARE UNIT ID X

No ID's found for provider and selected insurance co

Enter ?? for more actions

AU Add a Unit DU Delete a Unit

EU Edit a Unit EX Exit

Select Action: Quit// *AU Add a Unit*

CHOOSE 1-2: 2 BLUE SHIELD ID

FORM TYPE APPLIED TO: 0 BOTH UB-04 AND CMS-1500 FORMS

BILL CARE TYPE: 0 BOTH INPATIENT AND OUTPATIENT

Select IB PROVIDER ID CARE UNIT: *Surgery Ambulatory Surgery BLUE CROSSOF CALIFORNIA*

THE FOLLOWING WAS CHOSEN:

INSURANCE: BLUE CROSS OF CALIFORNIA

PROV TYPE: BLUE SHIELD ID

FORM TYPE: BOTH UB-04 & CMS-1500 FORMS

CARE TYPE: BOTH INPATIENT AND OUTPATIENT

CARE UNIT: Surgery

PROVIDER ID: XXXXBS

52. When creating a bill for a patient with this payer, if IB,Doctor7 is entered on Screen 8, this ID for the Care Unit, Surgery, will be one of the Physician / Provider’s Secondary IDs available.

\*\*\*\* SECONDARY PERFORMING PROVIDER IDs \*\*\*\*

PRIMARY INSURANCE CO: BLUE CROSS OF CALIFORNIA

PROVIDER: IB,DOCTOR7 (RENDERING)

SELECT A SECONDARY ID OR ACTION FROM THE LIST BELOW:

1 - NO SECONDARY ID NEEDED

2 - ADD AN ID FOR THIS CLAIM ONLY

*3 - XXXXBS BLUE SHIELD ID Surgery*

Selection: 1//

### Define Care Units for Billing Provider Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Access the option MCCR SYSTEM DEFINITION MENUProvider ID Maintenance.
218. At the Select Provider ID Maintenance Option: prompt, enter CB for Care Units for Billing Provider.
219. At the Select INSURANCE CO: prompt, enter Blue Cross of California for this example.

Provider ID Maintenance Main Menu

Enter a code from the list.

Provider IDs

PO Provider Own IDs

PI Provider Insurance IDs

Insurance IDs

BI Batch ID Entry

II Insurance Co IDs

Care Units

CP Care Units for Providers

CB Care Units for Billing Provider

Non-VA Items

NP Non-VA Provider

NF Non-VA Facility

Select Provider ID Maintenance Option: *CB Care Units for Billing Provider*

Select INSURANCE CO: *Blue Cross of California*

220. At the Select Action: prompt, enter AU for Add a Unit.
221. At the Enter the Division for this Care Unit: prompt, press the \<Enter\> key to accept the default.
222. At the Enter Care Unit Name: prompt, enter Anesthesia for this example.
223. At the Enter a Care Unit Description: prompt, enter a free text description.
53. Users may repeat these steps to create multiple Care Units for multiple divisions. Refer to Section 3.1.2.3 to learn how to assign Billing Provider Secondary IDs to Care Units.

Care Units – Billing Provider May 27, 2005@11:17:46 Page: 1 of 0

Insurance Co: BLUE CROSS OF CALIFORNIA

Care Unit Name Division Description

No Care Units defined for this Insurance Co.

Enter ?? for more actions

AU Add a Unit DU Delete a Unit

EU Edit a Unit EX Exit

Select Action: Quit// *AU Add a Unit*

Enter the Division for this Care Unit: *Main Division*//

Enter Care Unit name: *Anesthesia*

Are you adding 'Anesthesia' as

a new Care Unit for Main Division? No// *y (Yes)*

Enter a Care Unit Description: *Free Text Description*

Care Unit combination filed for this Insurance Co.

The following screen will display.

Care Units – Billing Provider May 27, 2005@11:17:46 Page: 1 of 0

Insurance Co: BLUE CROSS/BLUE SHIELD

Care Unit Name Description

-------------------------------------------------------------------------------

*Division: Main DivisionAnesthesia Free Text DescriptionReference Lab Free Text DescriptionHome Health Free Text DescriptionDivision: Remote ClinicReference Lab Free Text Description*

Enter ?? for more actions

AU Add a Unit DU Delete a Unit

EU Edit a Unit EX Exit

Select Action: Quit// QUIT

## ID Parameters by Insurance Company

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to defining Care Units and Physician / Provider IDs in Provider ID Maintenance, there are also ID parameters that can be set for an insurance company that effect which IDs get sent on 837 claims transmissions to an insurance company.

Users need to be aware of these parameters so the parameters can be set *if needed*. The users do not need to be set unless there is a specific need for a particular insurance company.

1.  Access the option Insurance Company Entry/Edit.
224. At the Select INSURANCE COMPANY NAME: prompt, enter BLUE CROSSOF CALIFORNIA for this example.
225. From the Insurance Company Editor, enter the Prov IDs/ID Param action.

Insurance Company Editor Oct 01, 2007@14:27:13 Page: 1 of 9

Insurance Company Information for: BLUE CROSS OF CALIFORNIA

Type of Company: HEALTH INSURANCE Currently Active

Billing Parameters

Signature Required?: NO Filing Time Frame:

Reimburse?: WILL REIMBURSE Type Of Coverage: HEALTH INSURAN

Mult. Bedsections: Billing Phone: XXX/XXX-XXXX

Diff. Rev. Codes: Verification Phone: XXX/XXX-XXXX

One Opt. Visit: NO Precert Comp. Name:

Amb. Sur. Rev. Code: Precert Phone: XXX/XXX-XXXX

Rx Refill Rev. Code:

EDI Parameters

Transmit?: YES-LIVE Insurance Type: HMO

\+ Enter ?? for more actions \>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Action: Next Screen// ID Prov IDs/ID Param

226. From the Billing Provider IDs screen, enter the ID Parameters action.

Billing Provider IDs (Parent) May 27, 2005@12:48:29 Page: 1 of 1

Insurance Co: BLUE CROSS OF CALIFORNIA Billing Provider Secondary IDs

ID Qualifier ID X Form Type

Division: Name of Main Division/Default for All Divisions

1 Electronic Plan Type XXXXXXXXX UB-04

2 Electronic Plan Type XXXXXXXX1X 1500

Enter ?? for more actions

Add an ID Additional IDs Exit

Edit an ID *ID Parameters*

Delete an ID VA-Lab/Facility IDs

Select Action: Edit// *ID Parameters*

54. The ID Parameter Maint. Screen displays the current parameter values.
227. At the Select Action: prompt, enter the Edit Params action.

Transmit no Billing Provider Sec ID for the following Electronic Plan Types:

Billing Provider/Service Facility

\+ Enter ?? for more actions

Edit Params Edit Billing Prov Params Exit

Select Action: Next Screen// Edit Params

The following will display.

Attending/Rendering Provider Secondary ID

Default ID (1500): BLUE SHIELD//

Default ID (UB): BLUE CROSS//

Require ID on Claim: BOTH UB-04 AND CMS-1500 REQUIRED

//

Referring Provider Secondary ID

Default ID (1500): BLUE SHIELD//

Require ID on Claim: CMS-1500//

Billing Provider Secondary IDs

Use Att/Rend ID as Billing Provider Sec. ID (1500)?: NO

//

Use Att/Rend ID as Billing Provider Sec. ID (UB)?: NO

//

Billing Provider/Service Facility

Always use main VAMC as Billing Provider (1500)?: NO

//

Always use main VAMC as Billing Provider (UB-04)?: NO

//

### Define Attending/Rendering Provider Secondary ID Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can define the type of ID that will be the default secondary ID for the Rendering Provider or Attending Physician during the creation of a claim.

A type of default secondary ID can be defined for a CMS-1500 claim and / or a UB-04 claim.

Users can also set a parameter that will make these IDs required on a claim. If the users are required, and the Physician / Provider on the claim does not have a secondary ID of the type required, the claim cannot be authorized.

Attending/Rendering Provider Secondary ID

Default ID (1500): BLUE SHIELD ID

Default ID (UB04): BLUE CROSS ID

Require ID on Claim: BOTH

### Define Referring Provider Secondary ID Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can define the type of ID that will be the default secondary ID for the Referring Provider during the creation of a CMS-1500 claim.

A type of default secondary ID can be defined for a CMS-1500 claim.

Users can also set a parameter that will make this ID required on a claim. If the ID is required and the referring provider on the claim does not have a secondary ID of the type required, the claim cannot be authorized.

The default type of ID for a Referring Provider is a Unique Provider Identification Number (UPIN); users can, however, override this default.

Referring Provider Secondary ID

Default ID (1500): *UPIN*// BLUE SHIELD ID

Require ID on Claim: CMS-1500 REQUIRED

### Define Billing Provider Secondary ID Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If an insurance company wants the Billing Provider Secondary ID (Billing Screen 3) to be the same as the Attending Physician’s or the Rendering Provider’s ID, users can set the Send Attending / Rendering ID as Billing Provider Sec. ID?: parameter to Yes. The default value is No.

Billing Provider Secondary IDs

Use Att/Rend ID as Billing Provider Sec. ID (1500)?: YES

Use Att/Rend ID as Billing Provider Sec. ID (UB-04)?: NO

55. If the payer requires the Attending / Rendering Physician / Provider’s Secondary ID as the Billing Provider Secondary ID, this parameter can be set and a default Attending / Rendering ID type can be set and then users can just accept the default ID on Billing Screen 8 and will be transmitted as the Physician / Provider’s Secondary ID and the Billing Provider Secondary ID.

### Define No Billing Provider Secondary IDs by Plan Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some insurance companies do not want any Billing Provider Secondary IDs to be transmitted in the 837 claim transmission for claims to specific plan types.

To define which plan types require no Billing Provider Secondary IDs, users must enter the plan types.

1.  From the ID Parameter Maint. screen, enter the Edit Billing Prov Params action.
56. The first Billing Provider Secondary ID will still be sent with the claim regardless of this parameter. The first ID is a calculated value used by the clearinghouse for sorting purposes.
228. At the Select Action: prompt, enter Add Plan.
229. At the Enter Electronic Plan Type: prompt, enter PPO for this example.

Billing Provider Parameters May 27, 2005@12:48:29 Page: 1 of 1

Insurance Co.: BLUE CROSS OF CALIFORNIA

Transmit No Billing Provider Sec ID for the following Electronic Plan Types:

1 HMO

Enter ?? for more actions

Add Plan Delete Plan Exit

Select Action: *Add Plan*

Enter Electronic Plan Type: *PPO*

### View Associated Insurance Companies, Provider IDs, and ID Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When in the Insurance Company Editor, users can scroll through the information that has been defined for a particular insurance company.

57. Patch IB\*2.0\*320 added sections to display: Associated Insurance Companies; Provider IDs and ID Parameters.

Insurance Company Editor Nov 22, 2005@10:26:11 Page: 5 of 7

Insurance Company Information for: BLUE CROSS OF CALIFORNIA

Type of Company: BLUE CROSS Currently Active

\+

*Associated Insurance Companies*

This insurance company is defined as a Parent Insurance Company.

There are 4 Child Insurance Companies associated with it.

Select the "AC Associate Companies" action to enter/edit the children.

*Provider IDs*

Billing Provider Secondary ID

Main Division and Default for All Divisions/1500:

Main Division and Default for All Divisions/UB-04:

Main Division Care Units:

Anesthesia/1500:

Reference Lab/1500:

Reference Lab/UB-04:

Home Health/UB-04:

2<sup>nd</sup> Division Name/1500:

2<sup>nd</sup> Division Name/UB-04:

Additional Billing Provider Secondary IDs

Main Division and Default for All Divisions/1500:

1<sup>st</sup> ID

2<sup>nd</sup> ID

3<sup>rd</sup> ID

Maximum of 6 additional IDs

Main Division and Default for All Divisions/UB-04:

1<sup>st</sup> ID

2<sup>nd</sup> ID

3<sup>rd</sup> ID

Maximum of 6 additional IDs

VA-Laboratory or Facility Secondary IDs

Main Division and Default for All Divisions/1500:

1<sup>st</sup> ID

2<sup>nd</sup> ID

3<sup>rd</sup> ID

Maximum of 5 additional IDs

*ID Parameters*

Attending/Rendering Provider Secondary ID Qualifier (1500):

Attending/Rendering Provider Secondary ID Qualifier (UB-04):

Attending/Rendering Secondary ID Requirement: NONE REQUIRED

Referring Provider Secondary ID Qualifier (1500):

Referring Provider Secondary ID Requirement:

Use Attending/Rendering ID as Billing Provider Sec. ID: No

Transmit no Billing Provider Sec. ID for the Electronic Plan Types:

HMO

PPO

Send VA Lab/Facility IDs or Facility Data: No

## Associated Insurance Companies and Copying Physician / Provider Secondary IDs and Additional Billing Provider Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*320 provided the ability for users to associate multiple Insurance Company entries with each other.

Example: If there are 45 Blue Cross / Blue Shield entries in the Insurance Company file, users can make one of these entries the Parent company and make 1 to 44 of the other entries a Child company.

Making these associations will cause the software to automatically make the Physician / Provider Secondary IDs and the Additional Billing Provider Secondary IDs the same for all associated companies.

Once these associations are made and the IDs synchronized for all the associated companies, users can Add, Edit, and / or Delete IDs for the associated companies from the Parent company. Changes to the IDs from a Child company, however, are prohibited.

If a situation changes and becomes necessary for a Child company to have IDs that differ from those of the Parent company, users may disassociate the Child company from the Parent company.

### Designate a Parent Insurance Company

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The steps listed below designate a Parent Insurance Company:

1.  Access the Insurance Company Editor.
230. At the Select INSURANCE COMPANY NAME: prompt, enter Blue Cross ofCalifornia for this example.
231. At the Define Insurance Company as Parent or Child: prompt, enter Parent.

Insurance Company Editor Oct 01, 2007@14:27:13 Page: 1 of 9

Insurance Company Information for: BLUE CROSS OF CALIFORNIA

Type of Company: HEALTH INSURANCE Currently Active

Billing Parameters

Signature Required?: NO Filing Time Frame:

Reimburse?: WILL REIMBURSE Type Of Coverage: HEALTH INSURAN

Mult. Bedsections: Billing Phone: XXX/XXX-XXXX

Diff. Rev. Codes: Verification Phone: XXX/XXX-XXXX

One Opt. Visit: NO Precert Comp. Name:

Amb. Sur. Rev. Code: Precert Phone: XXX/XXX-XXXX

Rx Refill Rev. Code:

EDI Parameters

Transmit?: YES-LIVE Insurance Type: GROUP

\+ Enter ?? for more actions \>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address *AC Associate Companies* AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen//*AC Associate Companies*

Define Insurance Company as Parent or Child: *P PARENT*

232. At the Select Action: prompt, enter Associate Companies for this example.
233. At the Select INSURANCE COMPANY NAME: prompt, enter BLUE CROSS / BLUE SHIELD 801 PINE ST. CHATTANOOGA,TN for this example.
58. Steps 2 - 4 can be repeated to associate additional Insurance Companies with Blue Cross of California.

    A Parent – Child association can be removed using the Disassociate Companies action.

    To stop an insurance company from being a Parent, all associations with any Child entries must be removed. After disassociating all the Child entries, users may delete the Parent using the ‘@’ sign at the Define Insurance Company as Parent or Child: PARENT// prompt.

Associated Insurance Co's Nov 21, 2005@11:13:53 Page: 1 of 1

Parent Insurance Company:

BLUE CROSS OF CALIFORNIA PO BOX XXXXX LOS ANGELES,CA

Ins Company Name Address City

No Children Insurance Companies Found

Enter ?? for more actions

Associate Companies Exit

Disassociate Companies

Select Action: Quit// *as Associate Companies*

Select Insurance Company: *BLUE CROSS/BLUE SHIELD801 PINE ST.* ANYTOWN*,TN*

The following screen will display.

Associated Insurance Co's Nov 21, 2005@11:30:25 Page: 1 of 1

Parent Insurance Company:

BLUE CROSS OF CALIFORNIA PO BOX XXXXX LOS ANGELES,CA

Ins Company Name Address City

1 BLUE CROSS FEP PO BOX *XXXXX* ANYTOWN,CA

2 BLUE CROSS / BLUE SHIELD REDACTED ANYTOWN,KY

3 BLUE CROSS / BLUE SHIELD REDACTED ANYTOWN,TN

Enter ?? for more actions

Associate Companies Exit

Disassociate Companies

Select Action: Quit//

### Designate a Child Insurance Company

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An insurance company can be designated as a Child, from the Parent insurance company as demonstrated in Section 4.8.1.

If users want to quickly define a single insurance company as a Child, the users can do this from the Insurance Company Editor.

1.  Access the Insurance Company Editor.
234. At the Select INSURANCE COMPANY NAME: prompt, enter Aetna for this example.
235. At the Define Insurance Company as Parent or Child: prompt, enter Child for this example.
236. At the Associate with which Parent Insurance Company: prompt, enter the name of the insurance company that will be the Parent.
59. ‘??’ will provide a list of available Parent insurance companies.

Insurance Company Editor Oct 01, 2007@14:33:41 Page: 1 of 8

Insurance Company Information for: AETNA

Type of Company: HEALTH INSURANCE Currently Inactive

Billing Parameters

Signature Required?: NO Filing Time Frame: 12 MOS

Reimburse?: WILL REIMBURSE Type Of Coverage: HEALTH INSURAN

Mult. Bedsections: Billing Phone:

Diff. Rev. Codes: Verification Phone:

One Opt. Visit: NO Precert Comp. Name:

Amb. Sur. Rev. Code: Precert Phone:

Rx Refill Rev. Code:

EDI Parameters

Transmit?: YES-LIVE Insurance Type: GROUP POLICY

\+ Enter ?? for more actions \>\>\>

BP Billing/EDI Param IO Inquiry Office EA Edit All

MM Main Mailing Address AC Associate Companies AI (In)Activate Company

IC Inpt Claims Office ID Prov IDs/ID Param CC Change Insurance Co.

OC Opt Claims Office PA Payer DC Delete Company

PC Prescr Claims Of RE Remarks VP View Plans

AO Appeals Office SY Synonyms EX Exit

Select Action: Next Screen// ac Associate Companies

Define Insurance Company as Parent or Child: *Child CHILD*

Associate with which Parent Insurance Company: *AetNA LIFE INSURANCE* REDACTED ANYTOWN PENNSYLVANIA Y.

### Copy Physician / Provider Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Individual Physician / Provider Secondary IDs can be entered, edited, or deleted one time from the Parent insurance company and these changes will be copied to all associated insurance companies (Child).

This can be done using the following Provider ID Maintenance options:

- Provider ID Maint PI Provider Insurance IDs
- Provider ID Maint II Insurance Co IDs
- Provider ID Maint BI Batch ID Entry

### Copy Additional Billing Provider Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When users are done adding, editing, or deleting Additional IDs from the Parent insurance company, the changes will be copied to all associated insurance companies.

### Synchronizing Associated Insurance Company IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is an IRM option for synchronizing the IDs of a Parent insurance company with all of the associated Child companies. This option is intended as a back-up option if the IDs of a Parent have become out of synch with the Child companies due to a system problem.

# Subscriber and Patient ID Set-Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Insurance Companies issue identification numbers to the people that they insure. The person who pays for the insurance policy or whose employer pays for the insurance policy or who receives Medicare is referred to as the subscriber. A veteran can be the subscriber, or a veteran can be insured through an insurance policy that belongs to some other subscriber such as the veteran’s spouse or parent.

## Subscriber and Patient Insurance Provided IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some insurance companies issue identification numbers only to the subscriber. Some others issue unique identification numbers to each person covered by the subscriber’s policy.

Insurance companies can issue both Subscriber Primary and Secondary ID numbers and Patient Primary and Secondary ID numbers.

These ID numbers can be entered when a policy is initially added in VistA through Add a policy. Sometimes the primary IDs will be added during the initial Patient Registration process and placed in the insurance company buffer.

Both Patient and Subscriber, Primary and Secondary IDs can be added or edited at any time using the option Patient Insurance Info View/Edit.

### Define Subscriber Primary ID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the patient is the subscriber, users will be prompted for the Subscriber’s Primary ID.

1.  Access the option Patient Insurance Info View/Edit.
237. At the Select Patient Name: prompt, enter IB,PATIENT TWO.
238. At the Select Items: prompt, enter Policy Edit/View.
239. At the Select Policy(s): prompt, enter 1 for this example.

Patient Insurance Management Sep 24, 2007@10:18:49 Page: 1 of 1

Insurance Management for Patient: IB,PATIENT TWO IXXXX XX/XX/XXXX

Insurance Co. Type of Policy Group Holder Effect. Expires

1 AETNA US HEALTH COMPREHENSIVE M XXXXXX-XX- SELF 03/06/07

2 BLUE CROSS CA ( PREFERRED PROVI XXXXXX SPOUSE 05/15/07

3 IB INSURANCE CO COMPREHENSIVE M XXXPLANNUM OTHER 05/16/07

4 NEW YORK LIFE MEDIGAP (SUPPLE F OTHER 09/29/06

Enter ?? for more actions \>\>\>

AP Add Policy EA Fast Edit All CP Change Patient

VP Policy Edit/View BU Benefits Used WP Worksheet Print

DP Delete Policy VC Verify Coverage PC Print Insurance Cov.

AB Annual Benefits RI Personal Riders EB Expand Benefits

RX RX COB Determination EX Exit

Select Item(s): Quit// *VP Policy Edit/View*

Select Policy(s): (1-4): *1*...................

The following screen will display.

Patient Policy Information Sep 24, 2007@11:20:54 Page: 1 of 6

For: IB,PATIENT TWO XXX-XX-XXXX XX/XX/XXXX DOD: XX/XX/XXXX

AETNA US HEALTHCARE Insurance Company \*\* Plan Currently Active \*\*

Insurance Company

Company: AETNA US HEALTHCARE

Street: PO BOX XXXXX

City/State: ANYTOWN, IN XXXXX

Billing Ph: XXX/XXX-XXXX

Precert Ph:

Plan Information

Is Group Plan: YES

Group Name: FT JAMES CORP

Group Number: XXXXXX-XX-XXX

BIN:

PCN:

Type of Plan: COMPREHENSIVE MAJOR MED

Electronic Type: COMMERCIAL

Plan Filing TF: 2 YRS

Utilization Review Info Effective Dates & Source

Require UR: Effective Date: 03/06/07

\+ Enter ?? for more actions

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

*SU Subscriber Update* PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// *SU Subscriber Update*

240. At the Select Action: prompt, enter Subscriber Update.
241. At the Pt. Relationship to Subscriber: prompt, enter Patient.
60. With Patch IB\*2\*371, the Whose Insurance? prompt was removed.

    With Patch IB\*2\*371, users will have the ability to update the patient’s name for any patient and any insurance company. This will allow users to make the patient’s name match what is on file at the payer even when the patient’s name is different from what is in the VistA patient file.
242. At the Name of Subscriber: prompt, press the \<Enter\> key to accept the default of IB,Patient Two.
61. Once Patch IB\*2\*547 is installed, a patient and / or a subscriber with only a last name will be acceptable in Enter / Edit Billing Information.

    With Patch IB\*2\*371, users will have the ability to update the patient’s name for any patient and any insurance company. This will allow users to make the patient’s name match what is on file at the payer even when the patient’s name is different from what is in the VistA patient file.
243. At the Effective Date of Policy: prompt, press the \<Enter\> key to accept the default of MAR 6, 2007.
244. At the Coordination of Benefits: prompt, enter Primary for this example.
245. At the Source of Information: prompt, press the \<Enter\> key to accept the default of Interview.
246. At the Subscriber Primary ID: prompt, enter IDXXXXX for this example.
247. At the Do you want to enter/update Subscriber Secondary IDs? Prompt, press the \<Enter\> key to accept the default of No.
248. At the Subscriber's DOB: prompt, press the \<Enter\> key to accept the default.
249. At the Subscriber’s Sex: prompt, press the \<Enter\> key to accept the default.
62. With Patch IB\*2\*361, the Insured’s Sex prompt was added. This is required by HIPAA as is the Insured’s DOB.

    The Insured’s address is not required by HIPAA but HIPAA will not accept a partial address. When the insured is the patient, the patient’s address will be defaulted from the patient file.

Select Action: Next Screen// *Subscriber Update*

PT. RELATIONSHIP TO SUBSCRIBER: *PATIENT*

NAME OF SUBSCRIBER: *IB,PATIENT TWO*//

EFFECTIVE DATE OF POLICY: *MAR 6,2007*

INSURANCE EXPIRATION DATE:

PRIMARY CARE PROVIDER:

PRIMARY PROVIDER PHONE:

COORDINATION OF BENEFITS: *PRIMARY*

SOURCE OF INFORMATION: *INTERVIE*W//

SUBSCRIBER PRIMARY ID: IDXXXXX

Do you want to enter/update Subscriber Secondary IDs? *No*// NO

SUBSCRIBER'S DOB: *XXX XX,XXXX*//

SUBSCRIBER'S SEX: *MALE*//

SUBSCRIBER'S BRANCH: *NAVY*//

SUBSCRIBER'S RANK:

SUBSCRIBER'S STREET 1: *REDACTED*//

SUBSCRIBER'S STREET 2:

SUBSCRIBER'S CITY: *ANYTOWN*//

SUBSCRIBER'S STATE: *WYOMING*//

SUBSCRIBER'S ZIP: XXXXX//

63. Patch IB\*2\*377 will provide the ability for the Name of the Subscriber and the Subscriber’s primary ID (HIC#) to be automatically updated in the Patient’s Medicare (WNR) Insurance when an MRA is received in VistA that contains a corrected name and / or ID. The PATIENT file will not be changed.

### Define Subscriber and Patient Primary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the patient is not the subscriber, users will be prompted for the Patient’s Primary ID as well as the Subscriber’s Primary ID.

1.  Access the option Patient Insurance Info View/Edit.
250. At the Select Patient Name: prompt, enter IB,PATIENT TWO.
251. At the Select Items: prompt, enter Policy Edit/View.
252. At the Select Policy(s): prompt, enter 3 for this example.

Patient Insurance Management Sep 24, 2007@10:18:49 Page: 1 of 1

Insurance Management for Patient: IB,PATIENT TWO I4444 XX/XX/XXXX

Insurance Co. Type of Policy Group Holder Effect. Expires

1 AETNA US HEALTH COMPREHENSIVE M XXXXXX-XX- SELF 03/06/07

2 BLUE CROSS CA ( PREFERRED PROVI XXXXXX SPOUSE 05/15/07

3 IB INSURANCE CO COMPREHENSIVE M XXXPLANNUM SPOUSE 05/16/07

4 NEW YORK LIFE MEDIGAP (SUPPLE F OTHER 09/29/06

Enter ?? for more actions \>\>\>

AP Add Policy EA Fast Edit All CP Change Patient

VP Policy Edit/View BU Benefits Used WP Worksheet Print

DP Delete Policy VC Verify Coverage PC Print Insurance Cov.

AB Annual Benefits RI Personal Riders EX Exit

Select Item(s): Quit// *VP Policy Edit/View*

Select Policy(s): (1-4): 3.

The following screen will display.

Patient Policy Information Sep 24, 2007@10:33:49 Page: 2 of 6

For: IB,PATIENT TWO XXX-XX-XXXX XX/XX/XXXX DOD: XX/XX/XXXX

IB INSURANCE CO Insurance Company \*\* Plan Currently Active \*\*

Subscriber Information Subscriber's Employer Information

Whose Insurance: SPOUSE Emp Sponsored Plan: No

Subscriber Name: Employer:

Relationship: Employment Status:

Primary ID: Retirement Date:

Coord. Benefits: Claims to Employer: No, Send to Insurance

Primary Provider: Street:

Prim Prov Phone: City/State:

Phone:

Insured Person's Information (use Subscriber Update Action)

Insured's DOB: XX/XX/XXXX Str 1: 123 E.TEST BLVD

\+ Enter ?? for more actions

PI Change Plan Info GC Group Plan Comments CP Change Policy Plan

UI UR Info EM Employer Info VC Verify Coverage

ED Effective Dates CV Add/Edit Coverage AB Annual Benefits

*SU Subscriber Update* PT Pt Policy Comments BU Benefits Used

IP Inactivate Plan EA Fast Edit All EB Expand Benefits

EX Exit

Select Action: Next Screen// *SU Subscriber Update*

253. At the Select Action: prompt, enter Subscriber Update.
254. At the PT. RELATIONSHIP TO SUBSCRIBER: prompt, enter SPOUSE for this example.
64. With Patch IB\*2\*377, an expanded list of HIPAA compliant codes for Pt. Relationship to Insured, was added.

    With Patch IB\*2\*371, the Whose Insurance? prompt was removed.
255. At the Name of Subscriber: prompt, enter IB,Spouse Two for this example.
256. At the Effective Date of Policy: prompt, press the \<Enter\> key to accept the default of May 15, 2007.
257. At the Coordination of Benefits: prompt, enter Secondary for this example.
258. At the Source of Information: prompt, press the \<Enter\> key to accept the default of Interview.
259. At the Subscriber Primary ID: prompt, enter XXXXXID for this example.
260. At the Do you want to enter/update Subscriber Secondary IDs? Prompt, press the \<Enter\> key to accept the default of No.
261. At the Patient Primary ID: prompt, enter XXXXXID2 for this example.
262. At the Do you want to enter/update Patient Secondary IDs? Prompt, press the \<Enter\> key to accept the default of No.
263. At the Subscriber’s DOB: prompt, enter XXX XX,XXXX for this example.
264. At the Subscriber’s Sex: prompt, enter Female for this example.
65. With Patch IB\*2\*361, the Insured’s Sex prompt was added. This is required by HIPAA as is the Insured’s DOB.

    If the Patient’s Relationship to the Insured is spouse, then the patient’s address will be the default address of the Insured. Users may enter different values if the spouse’s address is different from the patient’s.

    The Insured’s address is not required by HIPAA but HIPAA will not accept a partial address.

Select Action: Next Screen// *SU Subscriber Update*

PT. RELATIONSHIP TO SUBSCRIBER: *SPOUSE*//

NAME OF SUBSCRIBER: *IB,SPOUSE TWO*

EFFECTIVE DATE OF POLICY: *MAY 15,2007*

INSURANCE EXPIRATION DATE:

PRIMARY CARE PROVIDER:

PRIMARY PROVIDER PHONE:

COORDINATION OF BENEFITS: *SECONDARY*

SOURCE OF INFORMATION: *INTERVIEW*//

SUBSCRIBER PRIMARY ID: *XXXXXID*

Do you want to enter/update Subscriber Secondary IDs? *No*// NO

PATIENT PRIMARY ID: *XXXXXID2*

Do you want to enter/update Patient Secondary IDs? *No*// NO

SUBSCRIBER'S DOB: *XXX XX,XXXX*

SUBSCRIBER'S SEX: *FEMALE*

SUBSCRIBER'S BRANCH:

SUBSCRIBER'S RANK:

SUBSCRIBER'S STREET 1: *123 E.TEST BLVD*//

SUBSCRIBER'S STREET 2:

SUBSCRIBER'S CITY: *ANYTOWN*//

SUBSCRIBER'S STATE: *WYOMING*//

SUBSCRIBER'S ZIP: *XXXXX*//

### Define Subscriber and Patient Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to Subscriber and Patient Primary IDs, it is possible for insurance companies to issue secondary IDs, although this is unusual. A subscriber or a patient may also have one or more secondary IDs of the following types:

- 23 Client Number
- IG Insurance Policy Number
- SY Social Security Number

SUBSCRIBER PRIMARY ID: XXXXXID//

Do you want to enter/update Subscriber Secondary IDs? No// *y YES*

SUBSCRIBER'S SEC QUALIFIER(1):??

Enter a Qualifier to identify the type of ID number.

Choose from:

23 Client Number

IG Insurance Policy Number

SY Social Security Number

SUBSCRIBER'S SEC QUALIFIER(1): *IG Insurance Policy Number*

SUBSCRIBER'S SEC ID(1): *XXXXID2*

SUBSCRIBER'S SEC QUALIFIER(2):

PATIENT PRIMARY ID: *IDXXXXX*//

Do you want to enter/update Patient Secondary IDs? No// *y YES*

PATIENT'S SEC QUALIFIER(1): *IG Insurance Policy Number*

PATIENT'S SECONDARY ID(1): *ID2XXXX*

PATIENT'S SEC QUALIFIER(2):

1.  Access Subscriber Update again.
265. At the Do you want to enter/update Subscriber Secondary IDs? No//: prompt, enter Yes.
266. At the Subscriber’s Sec Qualifier (1): prompt, enter IG for this example.
66. 23 Client Number is used for claims to the Indian Health Service/Contract Health Services (HIS/CHS).

    VistA will not allow users to enter SY for SNN if the payer is Medicare. Medicare will not accept the SSN as a subscriber’s secondary ID.
267. At the Subscriber’s Sec ID (1): prompt, enter XXXXID2 for this example.
268. At the Subscriber’s Sec Qualifier (2): prompt, press the \<Enter\> key if the user does not want to add another ID.
269. At the Patient Primary ID (1): prompt, press the \<Enter\> key to accept the default.
270. At the Do you want to enter/update Patient Secondary IDs? No//: prompt, enter Yes.
271. At the Patient’s Sec Qualifier (1): prompt, enter IG for this example.
272. At the Patient’s Sec ID (1): prompt, enter ID2XXXX for this example.
273. At the Patient’s Sec Qualifier (2): prompt, press the \<Enter\> key if the user does not want to add another ID.

# Entering Electronic Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section briefly identifies the screens used in the billing process that contain fields critical to EDI billing. It is important that all the data transmitted in an electronic claim be accurate and appropriate. This section is just meant to highlight some specific fields that pertain to electronic processing.

## Summary of Enter / Edit Billing Information to Support ASC X12N/5010

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There have been numerous changes with Patch IB\*2\*447 to the Enter / Edit Billing Information option to support changes in the Health Care Claim (837) Technical Reports (ASC X12N/ 5010) for both Institutional and Professional claims.

Patch IB\*2\*592 introduces the additional claim type of Dental. The Dental claims are also transmitted in the ASC X12N/5010 Health Care Claim (837) transaction.

| Screen | Section | Change                                                                    |
|--------|---------|---------------------------------------------------------------------------|
| 5      | 3       | Addition of Priority (Type) of Admission.                                 |
| 5      | 3       | Addition of Default Priority (Type) of Admission.                         |
| 8      |         | Screen 9 contains all information previously found on Screen 8 section 3. |
| 9      |         | Added Ambulance Transport Information (Claim Level).                      |
| 9      |         | Added Ambulance Certification Data (Claim Level).                         |
| 11     |         | Local screen 9 information was moved to screen 11.                        |

<span id="_Toc100304284" class="anchor"></span>Table : Payer Information

67. After Patch IB\*2\*432 is installed, users will no longer receive Warnings when there is more than one division or non-matching providers on a claim. It will be possible to have multi-divisional claims with line-level and claim-level providers, of the same type, who do not match

    After Patch IB\*2\*432 is installed, users will no longer receive an Error when a human provider does not have an SSN or EIN defined.

## Changes Made by Specific Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Patch IB\*2\*447

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following changes are in Patch IB\*2\*447 not covered elsewhere in this document.

#### Enter / Edit Billing Information

- The procedure in the first line-level position (first entered or set to 1 by user) on a claim, will no longer be designated a claim level Principal procedure (Qualifier BR) on an outpatient, institutional claim.
- The additional procedures in the line items of an outpatient, institutional will no longer be designated a claim level Other procedures (Qualifier BQ).
- IB will calculate the amount due from the MediGap secondary payer based upon the beginning Date of Service on a claim and the effective date of the MediGap Plans.

#### MEDIGAP Calculations

68. This option is currently not available and can be turned on at a future time.
- The amount due from the Medicare secondary Medigap payer will be based upon the Type of Plan of the Insurance Plan:
- MEDIGAP A (COINS, NO DED, NO B EXC)
- MEDIGAP B (COINS, A DED, NO B DED, NO B EXC)
- MEDIGAP C (COINS, A/B DED,NO B EXC)
- MEDIGAP D (COINS, A DED, NO B DED, NO B EXC)
- MEDIGAP F (COINS, DED, NO B EXC)
- MEDIGAP G (COINS, A DED, NO B DED, NO B EXC)
- MEDIGAP K (A COINS, 50% B COINS, 50% A DED, NO B DED, NO B EXC)
- MEDIGAP L (A COINS, 75% B COINS, 75% A DED, NO B DED, NO B EXC)
- MEDIGAP M (COINS, 50% A DED, NO B DED, NO B EXC)
- MEDIGAP N (COINS, A DED, NO B DED, NO B EXC)
- The amount due from the Medicare Secondary payer will be based upon the Type of Plan defined for the Insurance Plan:
- Medicare Secondary (COINS, DED, No B EXC)
- Medicare Secondary (COINS, DED, B EXC)
- The amount due from the Medicare Secondary Supplemental payer will be based upon the Type of Plan defined for the Insurance Plan. Medicare (Supplemental) (COINS, DED, No B EXC).
- The amount due from the Medicare Secondary Employer Group Health Plan (EGHP) payer will be based upon the Type of Plan defined for the Insurance Plan:
- CARVE-OUT (COINS, DED, B EXC)
- COMPREHENSIVE (COINS, DED, B EXC)
- MEDICAL EXPENSE (OPT/PROF) (COINS, DED, B EXC)
- MENTAL HEALTH (COINS, DED, B EXC)
- POINT OF SERVICE (COINS, DED, B EXC)
- PREFERRED PROVIDER ORGANIZATION (PPO) (COINS, DED, B EXC)
- RETIREE (COINS, DED, B EXC)
- SURGICAL EXPENSE INSURANCE (COINS, DED, B EXC)
- The monetary value entered by users in Section 5 of Screen 7, Rev. Code, for outpatient and inpatient Professional claims will be retained unless users:
- Remove the procedure that generated the Revenue Code and monetary value;
- Execute the Rate Schedule recalculation of charges function;
- Change the division associated with the procedure;
- Change the Charge Type;
- Change the division associated with the claim.
- It will be possible to transmit Revenue/Procedure codes which generate zero charge amounts in an 837 Health Care Claim Transmissions (PRF, Piece 5 and INS, Piece 9).
- Users will be able to enter and transmit a Priority (Type) of Visit (Admission Type Code) code field in an outpatient, institutional 837 Health Care Claim Transmission (CL1, Piece 23). There will no longer be a hard-coded value, 9, transmitted or printed.
- Users will be able to enter and transmit the following Ambulance Transport Data in a professional 837 Health Care Claim Transmission:
- Patient’s Weight Qualifier = LB
- Patient’s Weight
- Transport Reason Code
- Transport Distance Qualifier = DH
- Transport Distance
- Round Trip Purpose Description (Free Text)
- Stretcher Purpose Description (Free Text)
- Users will be able to enter and transmit the following Ambulance Certification Data in a professional 837 Health Care Claim Transmission:
- Code Category – 07
- Certification Condition Indicator – YES
- Condition Codes (1-5 codes)

### Patch IB\*2\*488

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*488 includes the following changes not covered elsewhere in this document.

#### Enter/Edit Billing Information

The system no longer provides the ability for users to force institutional or professional claims to be printed at the Health Care Clearing House (HCCH)

#### MRA Management Worklist (MRW)

Patch IB\*2\*488 modified the way message storage errors (created when an Electronic Explanation of Benefits (EEOB) or MRA is received and all the line items cannot be matched correctly) are displayed in TPJI. Internal code will no longer be displayed to the users. In addition to the changes in TPJI, similar changes exist in MRW for Medicare claims.

The Following types of errors will be displayed:

- Procedure Code mismatch
- Procedure Modifier mismatch
- Revenue Code mismatch
- Charge Amount mismatch
- Number of Units mismatch

The type of mismatch error and the values that were in the outbound 837 transaction will be displayed along with the values that were received in the inbound 835 transaction.

View an EOB Apr 14, 2014@18:25:55 Page: 4 of 6

BILL X:XXX-KXXXXXX

CURRENT INSURANCE COMPANY (PRIMARY): MEDICARE (WNR)

\+

VistA could not match all of the Line Level data received in the EEOB

(835 Record 40) to the claim in VistA.

Mismatched Procedure Code:

Payer reported the following was billed via the Claim (837):

Proc:71010 Mods:59 Rev Cd:324 Chg:227.40 Units:1

Payer reported adjudication via the EOB (835) as follows:

Proc:71015 Mods:59 Rev Cd:324 Chg:227.40 Units:1

Amt:100.00

---------------------------------------------------------------------

Service line adjustment (EEOB Record 41) has no matching service line

\+ Enter ?? for more actions

General Info Claim Level Adj Review Info

Payer Info Medicare Info Exit

Claim Level Pay Line Level Adj

Select Action: Next Screen//

Users can now identify those Medicare claims with associated MSEs as an exclamation point will appear to the left of the claim number.

MRA Management WorkList Nov 25, 2013@14:06:58 Page: 1 of 35

Bill X Svc Date Patient Name SSN Pt Resp Bill Amt Type

BILLER: IB,CLERK F

1 !999-KXXXXXX\* 06/02/10 IB,PATIENT 234 XXXX 0.00 1710.76 O/I

Insurers: MEDICARE (WNR), NAT'L ASSOC OF LETTER CARRIERS

MRA Status: DENIED, Jul 12, 2010

2 999-KXXXXXX 06/02/10 IB,PATIENT 33 XXXX 0.00 380.22 O/P

Insurers: MEDICARE (WNR), NAT'L ASSOC OF LETTER CARRIERS

MRA Status: DENIED, Jul 07, 2010

3 999-KXXXXXX 05/14/10 IB,PATIENT 12 XXXX 0.00 132.20 O/P

Insurers: MEDICARE (WNR), UNITEDHEALTHCARE

MRA Status: DENIED, Aug 16, 2010

4 999-KXXXXXX 06/11/10 IB,PATIENT 12 XXXX 0.00 132.20 O/P

Insurers: MEDICARE (WNR), UNITEDHEALTHCARE

MRA Status: DENIED, Aug 16, 2010

5 999-KXXXXXX 06/14/10 IB,PATIENT 103 XXXX 0.00 81.22 I/P

\+ !=835 Data Mismatch Enter ?? for more actions

PC Process COB VC View Comments PM Print MRA

VE View an EOB CB Cancel Bill TP Third Party Joint Inq.

SU Summary MRA Info CR Correct Bill Q Exit

EC Enter Comments CC Cancel/Clone A Bill

RS Review Status VB View Bill

Select Action: Next Screen//

If users attempt to access any of the following Actions, the system will display a warning message.

- PC - Process COB
- VE - View an EOB
- SU – Summary MRA Info
- PM - Print MRA

Warning : The MRA for this claim caused a Data Mismatch/Message Storage Error. If you continue, the secondary claim may not contain the correct data.

Do you wish to continue?: No//

#### Enhanced CMS-1500 Printed Claim Form

The CMS-1500 Printed Claim Form has been updated to comply with the new National Uniform Claim Committee (NUCC) standards.

### Patch IB\*2\*516

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*516 includes the following changes not covered elsewhere in this document.

#### TRICARE/TRICARE REIMB. Pay-to Providers

If the Rate Type of a claim is either TRICARE or TRICARE REIMB., the new Non-MCCF Pay-to Provider will be printed or transmitted in the same manner as the regular Pay-to Provider information is for other Rate Types.

- The Non-MCCF Pay-to Provider’s address will print on the CMS – 1500 form in Box 32.
- The Non-MCCF Pay-to Provider’s data will print on the UB04 in FL2 only when the information is not exactly the same as the Billing Provider information.
- The Non-MCCF Pay-to Provider data will be transmitted in the 837 claim transaction in Record PRV1/Loop 2010A/B.

#### NDC Numbers for Non-RX Claims

If an NDC number and the units administered to the patient are entered on either a professional or institutional claim, the information will print in the following locations if the claim is printed locally:

- CMS – 1500 – Box 24: Shaded area – Format: N4NDC#\<space\>Unit Qualifier#of Units – if transmitted, the NDC number is transmitted in Record PRF/Loop 2410.
- UB04 – FL43 - Format: N4NDC#\<space\>Unit Qualifier#of Units – if transmitted the NDC number is transmitted in Record INS/Loop 2410.
69. The ability to select a Unit Qualifier was added in patch IB\*2\*577.

### Patch IB\*2\*547

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*547 includes the following changes not covered elsewhere in this document.

#### Service Lines with No Print Order

Identical CPT/HCPCS procedures that have the exact same data elements and no print order will be assigned to the same Revenue code with a combined number of units and monetary value.

#### Last Names Only

Claims can now be submitted for both patients and / or subscribers who have only one name (last name). A patient and / or subscriber with only a last name will no longer trigger a fatal error when trying to authorize a claim.

#### Blank Present on Admission

Inpatient institutional claims no longer require a Present on Admission (POA) value for all diagnosis codes. If a POA indicator is needed, the allowable values are now the following:

- Y – Yes
- N – No
- U – No Information in the Record
- W – Clinically Undetermined

#### Printed CMS 1500 Forms

Printed secondary/tertiary claims on CMS 1500 forms will display the dollar amount of previous primary and secondary payer payments in Box 29 - Amount Paid.

#### Printed UB04 Forms

The admission date and time will print on the UB04 form in FL 12 and 13 on claims for inpatient admissions only.

#### Insurance Company Entry / Edit / View Insurance Company

Though IB will continue to use only complete addresses in 837 transactions, the address fields in the insurance company editor will display whatever address data is stored in VistA for the following fields even when the address data is incomplete:

- Main Mailing Address
- Inpt Claims Office
- Opt Claims Office
- Prescr Claims Office
- Appeals Office
- Inquiry Office
70. View Insurance Company, which is just a view only option of what is in the Insurance Company Entry/Edit option, will display the same address information.

#### EDI Menu for Electronic Bills - Print EOB

Print EOB will display the complete and current textual description associated with the Claims Adjustment Reason Codes / Remittance Advice Remark Codes (CARC/RARC) received in an electronic EOB.

#### Copy and Cancel (CLON)

The existing CLON option logic for the inclusion of Coordination of Benefits (COB) data was enhanced to incorporate the following rules:

- Copy primary claim with EOB to a new primary claim – Do not copy COB data.
- Copy secondary claim to new secondary claim – Copy primary COB data.
- Copy tertiary claim to new tertiary claim – Copy primary and secondary COB data.

#### ASC X12N 5010 Health Care Claim (837) Transactions

The following changes were made to 837 transactions:

- An inpatient institutional 837 transaction no longer requires a POA for each diagnosis.
- An inpatient admission date can no longer be transmitted on outpatient claims.
- All Rate Types for which the responsible party is equal to insurer can now be transmitted electronically when appropriate.
- Institutional 837 transactions can now transmit up to twenty-five procedure codes.
- Institutional 837 transactions can now transmit up to 12 External Cause of Injury codes.

### Patch IB.2.576

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*576 includes the following changes not covered elsewhere in this document.

#### Enhanced CMS-1500 Printed Claim Form

The CMS-1500 Printed Claim Form has been updated to comply with the National Uniform Claim Committee (NUCC) standards:

- The Event Date will no longer be used as a default value for Box 14. If there is no Occurrence Code 10 – Last Menstrual Period Date or Occurrence Code 11 – Onset of Illness Date on the claim, no date or date qualifier will print in Box 14.
- The Timeframe of Bill value of either 7 – REPLACEMENT CLAIM or 8 - VOID/CANCEL PRIOR CLAIM will print in Box 22 (left-hand side) and the Internal Control Number (ICN) from the payer will print in Box 22 (right-hand side) for replacement claims 7 or 8.

#### MRA Management Worklist (MRW)

The legend on the MRW screen has been enhanced to include the explanation for an asterisk displaying next to a claim number.

MRA Management WorkList Nov 25, 2013@14:06:58 Page: 1 of 35

Bill X Svc Date Patient Name SSN Pt Resp Bill Amt Type

BILLER: IB,CLERK F

1 !999-KXXXXXX\* 06/02/10 IB,PATIENT 234 XXXX 0.00 1710.76 O/I

Insurers: MEDICARE (WNR), NAT'L ASSOC OF LETTER CARRIERS

MRA Status: DENIED, Jul 12, 2010

2 999-KXXXXXX 06/02/10 IB,PATIENT 33 XXXX 0.00 380.22 O/P

Insurers: MEDICARE (WNR), NAT'L ASSOC OF LETTER CARRIERS

MRA Status: DENIED, Jul 07, 2010

3 999-KXXXXXX 05/14/10 IB,PATIENT 12 XXXX 0.00 132.20 O/P

Insurers: MEDICARE (WNR), UNITEDHEALTHCARE

MRA Status: DENIED, Aug 16, 2010

4 999-KXXXXXX 06/11/10 IB,PATIENT 12 XXXX 0.00 132.20 O/P

Insurers: MEDICARE (WNR), UNITEDHEALTHCARE

MRA Status: DENIED, Aug 16, 2010

5 999-KXXXXXX 06/14/10 IB,PATIENT 103 XXXX 0.00 81.22 I/P

\+ !=835 Data Mismatch \*=Review in Process

PC Process COB VC View Comments PM Print MRA

VE View an EOB CB Cancel Bill TP Third Party Joint Inq.

SU Summary MRA Info CR Correct Bill Q Exit

EC Enter Comments CC Cancel/Clone A Bill

RS Review Status VB View Bill

Select Action: Next Screen//

#### Insurance Company Entry / Edit

The Insurance Company Editor has been modified to prevent the creation of new 5 character ZIP codes or 9 digit codes which include invalid final four digits (0000 or 9999). This change will affect the following addresses:

- Main Mailing Address
- Inpatient Claims Office Address
- Appeals Office Address
- Inquiry Office Address
- Outpatient Claims Office Address
- Prescription Claims Office Address

This change will not affect existing ZIP code values or usage unless someone attempts to update the current value.

All new ZIP codes should be 9 valid digits. If a user does not enter the correctly formatted data, the user will not be able to proceed. The following will be displayed:

Answer must be nine (999999999) or ten characters (99999-9999) in length. The last 4 cannot be '0000' or '9999'.

### Patch IB\*2\*577

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*577 includes the following changes not covered elsewhere in this document.

#### CLON

In addition to the changes made to CLON in patch IB\*2\*547, CLON has been enhanced to recalculate the monetary amount being billed to the destination payer when a claim is Canceled and Copied and the payer sequence is changed.

Example: A secondary claim is Clon’d to make a new claim and then the payer sequence is changed to Primary, to be resubmitted as an adjustment claim. Because the claim is going to the primary payer, the amount billed will be equal to the original amount billed to the primary payer.

### Patch IB\*2\*641

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*641 includes the following changes not covered elsewhere in this document.

#### Zero Dollar Total Claims Fatal Error Message

A new fatal error message will prevent the authorization of claims with total billed charges of zero.

The following error message will be displayed:

Total Charges for Bill missing or equals zero.

#### EDI Claim Status Report

This report can now be run by either detail or summary, patch 641 added the option to run in a summary format.

### Patch IB\*2\*665

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*665 includes the following changes not covered elsewhere in this document:

#### Inbound 277STAT

The current, proprietary 277STAT transactions which are received in VistA Mailman format from the Financial Services Center (FSC), have been replaced with HL7 FHIR (Fast Healthcare Interoperability Resources) messages.

#### Tertiary Claims will not Overwrite Secondary Claim Payer ID

VistA will submit tertiary claims/bills with a correct Secondary Payer ID for claims with Medicare as the primary, when the secondary commercial insurance is paid and there is a commercial tertiary insurance. VistA will no longer overwrite the secondary claim Payer ID at the line level with IPRNT for institutional claims or PPRNT for professional claims.

#### Principal Procedure Code must be Blank on the Second and Subsequent Printed Pages for UB-04 Claims 

VistA will place the Principal Procedure code in Principal form locator 74 on the first page and subsequent pages will have blank principal procedure codes.

## Handling Error Messages and Warnings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

71. Warnings will not prevent users from authorizing a claim, Errors will. If one or more errors exist, the user will be prompted to correct the errors. If a user answers Yes, the system will display the billing screens to allow the user to make changes.

IB Edit Checks are done before claim authorization.

... Executing national IB edits

ERROR/WARNING OUTPUT DEVICE: HOME// TELNET TERMINAL

\*\*Warnings\*\*:

Prov secondary id type for the PRIMARY RENDERING is invalid/won't transmit

BLUE CROSS CA (WY) requires Amb Care Certification

\*\*Errors\*\*:

A CPT procedure is missing an associated diagnosis.

Place of Service not entered for at least one procedure.

Type of Service not entered for at least one procedure.

Claims with multiple payers require all Payer IDs.

A claim cannot have a Primary Payer ID value of HPRNT/SPRNT.

Do you wish to edit the inconsistencies now? NO// y YES

### Patch IB\*2\*488

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*488 added several new error messages to Enter/Edit Billing Information:

- Error - when a professional claim contains no procedures codes.
- Error - when an outpatient, institutional claim contains no procedures codes.
- Error - when a Primary Payer ID is a PRNT/prnt value.

### Patch IB\*2\*516

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*516 made several changes to existing error and warnings messages:

- Error - when a claim contains a procedure code outside the 100-999 range – Removed.
- Error - when a human provider has no NPI – Added.
- Error - when a non-VA facility has no NPI – Added.
- Warning - when a non-VA Facility has no Taxonomy code – Removed.
72. The system will try to automatically remove non-billable providers from a claim as the auto biller creates a claim. The new error is for those cases where the provider has not been removed.

### Patch IB\*2\*547

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*547 made several changes to the existing logic for these error messages. The following error messages will no longer be triggered if the patient or subscriber only has a last name defined in VistA:

- Error - Patient's first and last name must begin with an alpha character.
- Error - Primary insurance subscriber's name is missing or invalid.
- Error - Secondary insurance subscriber's name is missing or invalid.
- Error - Tertiary insurance subscriber's name is missing or invalid.

### Patch IB\*2\*576

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*576 made changes to the existing logic for this error message.

The following error message will only display when there are both Occurrence Codes 10 – Last Menstrual Period and 11 – Onset of Illness on a claim:

- Error - Occ. Codes Onset of Illness (11) and LMP (10) not allowed on same bill.

### Patch IB\*2\*592

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Error - Rendering Provider or Assistant Surgeon required on Dental Claims.
- Error - Assistant Surgeon's NPI is required.
- Error - Assistant Surgeon taxonomy missing.
- Error - Claim Level Assistant Surgeon differs from all Line Level Assistant Surgeons.
- Error - Medicare (WNR) does not accept Dental claims.
- Error - Insurance Company does not have Dental Coverage.
- Error - Claim Level Rendering and Asst Surgeon NOT allowed on same Dental Claim.

### Patch IB\*2\*608

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Error - CMN form-specific data missing for the Form Type chosen.
- Error - Procedure A Calories missing.
- Error - Date of last "ABG PO2" and / or "O2 Saturation" Test(s) missing.
- Error - Procedure B Calories" missing.
- Error - Date of Latest 4 LPM Test(s) missing.
- Error - The following CMN field(s) missing or in error for at least 1 procedure.
- Error - Claim has no Rendering Providers present.

### Patch IB\*2\*623

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Warning - Only 4 diagnosis codes are allowed on a dental transaction.

### Patch IB\*2\*641

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*641 Added new logic to display the following error messages:

- If the staff attempts to authorize electronic resubmissions or print claims that rejected without changes made to any claim fields in VistA:
- Warning - You are about to Resubmit by Print, Retransmit, or Print a bill that has an error or was rejected without making any changes to the claim. Please check before continuing.
- If the staff attempts to authorize a claim with zero dollar total charges:
- Error - Total Charges for Bill missing or equals zero.
- If the staff attempts to authorize a Professional Claim for a procedure code without a Place of Service:
- Error - Place of Service not entered for at least one procedure.

### Patch IB\*2\*665

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*665 made several changes to the existing logic for error messages.

The following error messages will be triggered if the Biller enters too many codes in these fields in VistA for submitted claims:

- Error - Claim cannot contain more than 25 Procedure Codes for EDI submission.

  If claim needs more than 25 Procedure Codes, then select 'Force to Print'.
- Error - Claim cannot contain more than 24 Occurrence Codes for EDI submission.

  If claim needs more than 24 Occurrence Codes, then select 'Force to Print'.
- Error - Claim cannot contain more than 24 Occurrence Span Codes for EDI submission.

  If claim needs more than 24 Occurrence Span Codes, select 'Force to Print'.
- Error - Claim cannot contain more than 23 Value Codes for EDI submission.

  If more than 23 Value Codes need to be entered, select 'Force to Print'.
- Error - Claim cannot contain more than 24 Condition Codes for EDI submission.

  If more than 24 Condition Codes are needed, select 'Force to Print'.
- Error - 24 Other diagnosis codes are allowed on an electronic institutional claim.
- Error - 17 Other Diagnosis Codes allowed on a printed UB-04
- Error - 3 e-diagnosis codes are allowed on a printed UB04.
- Error - 12 e-diagnosis codes are allowed on an electronic institutional claim.
- Error - 12 diagnosis codes are allowed on a professional claim.
- Error - 4 diagnosis codes are allowed on a dental claim.
- Error - Institutional claim cannot contain more than 999 Revenue Codes.

## Claim versus Line Level Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the introduction of additional Line Level data (including Line Level Providers) in Patch IB\*2\*447, it is important to understand the concept of Claim Level data applying to all the line items on a claim. Claim Level data applies to all the line items on a claim, while Line Level data should be used to provide *exceptions* to the Claim Level data.

Example: If all the procedures on a claim were performed by the same Rendering provider, the claim should only have a Claim Level Rendering provider. If all but one procedure is done by the same Rendering provider and one procedure is done by a second Rendering provider, the claim should have a Claim Level Rendering provider and one different Line Level Rendering provider. Line Level providers will be transmitted in 837 Health Care Claim transmissions.

In addition, Institutional claims can have both line-level and / or claim-level Rendering, Referring, and Other Operating Providers. The Attending Provider is still the only provider required on an institutional claim and there is no longer a generic Other Provider.

Professional claims continue to allow Rendering, Referring, and Supervising Providers on a claim. The Rendering Provider is still the only provider required on a professional claim.

73. After Patch IB\*2\*592 is installed, users will be able to add a new type of provider, Assistant Surgeon, to a new form type J430D (Dental).

    After Patch IB\*2\*608 is installed, users will be able to submit a professional claim without a Rendering provider. Users will receive a non-fatal warning message when a professional claim does not contain a Rendering provider.

## Screen 3 – Payer Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EDI Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Section   | Field                                 | Description                                                                                                                                                                                                                                                                                                            |
|-----------|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Section 1 | Transmit                              | When a payer has been set up to transmit claims electronically, this field will say “Yes”. If the field says “No” the claim will be printed locally.                                                                                                                                                                   |
| Section 2 | Primary, Secondary and Tertiary Payer | These fields display the Billing Provider Secondary IDs for the payers on the bill. These IDs are defined in the Insurance Company Editor. Note: If users set the ID Parameter: Send Attending / Rendering ID as Billing Provider Sec. ID? to Yes for a payer on the claim, the Attending / Rendering ID will be sent. |
| Section 3 | Mailing Address                       | This field should contain a valid mailing address for the current payer. In order to avoid EDI errors, there should be no periods or dashes such as P.O. Box, Winston-Salem, St. Paul, etc. Exception: Medicare does not have a valid address.                                                                         |
| Section 3 | Electronic ID                         | This field contains the Inst Payer Primary ID or Prof Payer Primary ID defined in the Insurance Company Editor. Payer Primary IDs are provided by the clearinghouse and can be found at the Emdeon site.                                                                                                               |

<span id="_Toc100304285" class="anchor"></span>Table : EDI Fields

74. The 3-line mailing address displayed here is used also used by the clearinghouse to look up the Electronic ID for the payer when a claim is sent without a defined Electronic Bill ID.

IB,PATIENT 1 XX-XX-XXXX BILLX: KXXXXXX - Outpat/1500 SCREEN \<3\>

===============================================================================

PAYER INFORMATION

\[1\] Rate Type : REIMBURSABLE INS. Form Type: CMS-1500

Responsible: INSURER Payer Sequence: Primary

Bill Payer : CIGNA *Transmit: Yes*

Ins 1: CIGNA Policy X: XXXXXXXXX

Grp X: GRP NUM XXXX Whose: VETERAN Rel to Insd: PATIENT

Grp Nm: TEST GROUP Insd Sex: MALE Insured: IB,PATIENT IN

Ins 2: BLUE CROSS CA (W Policy X: XXXXXXXXX

Grp X: UNSPECIFIED Whose: SPOUSE Rel to Insd: SPOUSE

Grp Nm: TEST BCBS Insd Sex: FEMALE Insured: ib,wife in

\*\*\* Patient has Insurance Buffer entries \*\*\*

\[2\] Billing Provider Secondary IDs:

Primary Payer:

Secondary Payer: *XXXXXXX* Tertiary Payer:

\[3\] Mailing Address : Electronic ID: *XXXID*

CIGNA

PO BOX *99999*

ANYTOWN, TX *99999*

\<RET\> to CONTINUE, 1-3 to EDIT, '^N' for screen N, or '^' to QUIT:

75. Patch IB\*2\*432 made changes so that the Federal Tax ID Number will no longer be used as a default value when no other Billing Provider Secondary ID is defined for a payer – Section 2.

### Using Care Units for Billing Provider Secondary IDs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Section 2 of Billing Screen 3 contains fields for the Billing Provider Secondary IDs for the primary, secondary, and tertiary payers on a claim. Normally the default values for the site or the defined values for the division on the claim populate these fields. If any insurance company on the claim requires different Billing Provider Secondary IDs based upon Care Units, users can change the default values to the value defined for the Care Unit where the services were provided.

1.  At the \<RET\> to CONTINUE, 1-3 to EDIT, '^N' for screen N, or '^' to QUIT: prompt, enter 2.
274. At the Current Bill Payer Sequence: prompt, press the \<Enter\> key to accept the default.
275. At the Define Primary Payer ID by Care Unit?: prompt, press the \<Enter\> key to accept the default.
276. At the Primary Payer ID: prompt, press the \<Enter\> key to accept the default.
277. At the Define Secondary Payer ID by Care Unit?: prompt, enter Yes for this example.
278. At the Division: prompt, press the \<Enter\> key to accept the default for this example.
279. At the Care Unit: prompt, enter Anesthesia for this example.
280. At the Secondary Payer ID: prompt, press the \<Enter\> key to accept the default.
76. The Care Units must be defined in Provider ID Maintenance and the ID numbers must be defined in the Insurance Company Editor.

IB,PATIENT 1 XX-XX-XXXX BILLX: KXXXXXX - Outpat/1500 SCREEN \<3\>

===============================================================================

PAYER INFORMATION

\[1\] Rate Type : REIMBURSABLE INS. Form Type: CMS-1500

Responsible: INSURER Payer Sequence: Primary

Bill Payer : MRA NEEDED FROM MEDICARE Transmit: Yes

Ins 1: MEDICARE (WNR) WILL NOT REIMBURSE Policy X: XXXXXXXXA

Grp X: PART A Whose: VETERAN Rel to Insd: PATIENT

Grp Nm: PART A Insd Sex: MALE Insured: IB,PATIENT 1

Ins 2: BLUE CROSS OF CA Policy X: XXXXXXX

Grp X: PLAN 2 Whose: VETERAN Rel to Insd: PATIENT

Grp Nm: PROTECTION PLUS Insd Sex: MALE Insured: IB,PATIENT 1

\[2\] Billing Provider Secondary IDs:

Primary Payer: XXXXXX

Secondary Payer: *XXXXXX1X* Tertiary Payer:

\[3\] Mailing Address : Electronic ID: XXXXID

NO MAILING ADDRESS HAS BEEN SPECIFIED! (Patient has Medicare)

Send Bill to PAYER listed above.

\<RET\> to CONTINUE, 1-3 to EDIT, '^N' for screen N, or '^' to QUIT: *2*

Current Bill Payer Sequence: *PRIMARY INSURANCE*//

Define Primary Payer ID by Care Unit? *No*//

Primary Payer ID: *670899*//

Define Secondary Payer ID by Care Unit? No//*Yes*

Division: *Main Division*//

Care Unit: ??

1 Anesthesia

2 Reference Lab

3 Home Health

Care Unit: *1 Anesthesia*

Secondary Payer ID: *XXXXXXX*//

## Screen 10 – Physician / Provider and Print Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EDI Fields UB-04 / CMS-1500 / J430D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc100304286" class="anchor"></span>Table : Valid Secondary ID Types for Current Payer</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Section</th>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Section 3/3</td>
<td>Providers</td>
<td><p>When a Physician / Provider is entered here, the system finds the appropriate IDs and Taxonomy Codes for him/her.</p>
<p>The Primary IDs are the providers’ NPIs and their secondary IDs are those IDs that users have defined as the provider’s own or as those provided by an insurance company.</p>
<p>Claim Level providers may not be required if each Line Item has a provider associated with it.</p></td>
</tr>
<tr class="even">
<td>Section 4</td>
<td>Other Facility, CLIA#, Mammography Certification Number</td>
<td><p>These are the sections through which outside facilities are entered. The primary and secondary Laboratory or Facility IDs and Taxonomy Codes are then transmitted with the claim.</p>
<p>The CLIA# and Mammography Certification Number can also be sent with a professional laboratory claim or mammography claim. Dental does not currently allow for billing for care provided at a non-VA facility.</p></td>
</tr>
<tr class="odd">
<td>Section 5 / 7</td>
<td>Billing Provider</td>
<td>These sections display the calculated Billing Provider and the Billing Provider’s Taxonomy Code. Only the taxonomy code can be edited.</td>
</tr>
<tr class="even">
<td>Section 6 / 8</td>
<td>Force to Print</td>
<td><p>Users can set this field to force a claim to print locally.</p>
<p>Patch IB*2*488 removed the former option to force a Professional or Institutional claim to print at the clearinghouse. Dental does not currently allow for the local printing of J430D forms.</p></td>
</tr>
<tr class="odd">
<td>Section 7 / 9</td>
<td>Provider ID Maint</td>
<td>This is a link to the Provider ID Maintenance function.</td>
</tr>
</tbody>
</table>

<span id="_Toc100304286" class="anchor"></span>Table : Valid Secondary ID Types for Current Payer

Below is the Provider and Print Information sections:

IB,PATIENT2 XX-XX-XXXX BILLX: KXXXXX - Outpat/UB-04 SCREEN \<10\>

============================================================================

BILLING - SPECIFIC INFORMATION

\[1\] Bill Remarks

\- FL-80 : UNSPECIFIED \[NOT REQUIRED\]

ICN/DCN(s) : UNSPECIFIED \[NOT REQUIRED\]

Auth/Referral : UNSPECIFIED \[NOT REQUIRED\]

Admission Source : UNSPECIFIED

\[2\] Pt Reason f/Visit : UNSPECIFIED

*\[3\] Providers :- ATTENDING : UNSPECIFIED\[4\] Other Facility (VA/non): UNSPECIFIED \[NOT REQUIRED\]*

\[5\] Billing Provider : ANYTOWN VAMC

Taxonomy Code : 282N00000X

*\[6\] Force To Print? : NO FORCED PRINT\[7\] Provider ID Maint : (Edit Provider ID information)*

\<RET\> to CONTINUE, 1-7 to EDIT, '^N' for screen N, or '^' to QUIT:

77. With Patch IB\*2\*488, the former option to force a claim to print at the clearinghouse has been removed.

IB,PATIENT 3 XX-XX-XXXX BILLX: KXXXXX - Outpat/1500 SCREEN \<10\>

===============================================================================

BILLING - SPECIFIC INFORMATION

\[1\] Unable To Work From: UNSPECIFIED \[NOT REQUIRED\]

Unable To Work To : UNSPECIFIED \[NOT REQUIRED\]

\[2\] ICN/DCN(s) : UNSPECIFIED \[NOT REQUIRED\]

Auth/Referral : UNSPECIFIED \[NOT REQUIRED\]

*\[3\] Providers :- RENDERING (MD) : IB,DOCTOR 1 Taxonomy: UNSPECIFIED\[4\] Other Facility (VA/non): UNSPECIFIED \[NOT REQUIRED\]Lab CLIA X : UNSPECIFIED \[NOT REQUIRED\]Mammography Cert X : UNSPECIFIED \[NOT REQUIRED\]*

\[5\] Chiropractic Data : UNSPECIFIED \[NOT REQUIRED\]

\[6\] Form Locator 19 : UNSPECIFIED \[NOT REQUIRED\]

*\[7\] Billing Provider : ANYTOWN VAMCTaxonomy Code : XXXXXXXXXX\[8\] Force To Print? : NO FORCED PRINT\[9\] Provider ID Maint : (Edit Provider ID information)*

\<RET\> to CONTINUE, 1-9 to EDIT, '^N' for screen N, or '^' to QUIT: 8

FORCE CLAIM TO PRINT: NO FORCED PRINT// ??

If this field is set to 1, the claim will be printed locally.

If field is set to 0, the claim will be transmitted

electronically to the payer.

Choose from:

0 NO FORCED PRINT

1 FORCE LOCAL PRINT

FORCE CLAIM TO PRINT: NO FORCED PRINT//

## UB-04 Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following screens provide a simplified example of a UB-04 claim:

1.  When processing a UB-04 claim, information on Screens 1 and 2 should be reviewed for correctness. Press the \<Enter\> key to move from one screen to the next.
281. On Screen 3, the payer information is reviewed for correctness. The patient may have more than one insurance policy. If the correct information is not displayed, select a section (1, 2, or 3) and edit the necessary fields. Press the \<Enter\> key to continue to Screen 5.
78. With Patch IB\*2\*516, users will have the ability to add a one-time HPID, per payer, to a claim if the HPID in the Insurance Company file is not the correct one. The HPID will not be stored in the Insurance Company file. The HPID will only apply to the claim.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/UB-04 SCREEN \<3\>

============================================================================

PAYER INFORMATION

*\[1\]* Rate Type : REIMBURSABLE INS. Form Type: UB-04

Responsible: INSURER Payer Sequence: Primary

Bill Payer : Blue Cross Fep Transmit: Yes

Ins 1: Blue Cross Fep Policy X: RXXXXXXXXX

Grp X: 100 Whose: VETERAN Rel to Insd: PATIENT

Grp Nm: STANDARD FAMILY Insd Sex: MALE Insured: IB,PATIENT3

*\[2\]* Billing Provider Secondary IDs:

Primary Payer: XXXXXXXX

Secondary Payer: Tertiary Payer:

*\[3\]* Mailing Address : Electronic ID: XXXXX

Blue Cross Fep

REDACTED

Anytown, AL XXXXXXXXX

\<RET\> to CONTINUE, 1-3 to EDIT, '^N' for screen N, or '^' to QUIT:

282. On Screen 5, enter sections 1-7 to type in the diagnosis information, the services/procedures provided and the date of service. Include the Admission Type Code, Occurrence, and Condition Code when required. Press the \<Enter\> key to move to Screen 7.
79. With Patch IB\*2\*516, users will be able to look up Occurrence Codes, Condition Codes, and Value Codes by the external NUBC code numbers.

    After Patch IB\*2\*477 is installed users can enter a Priority (Type) of Visit to an outpatient, institutional claim. The value will no longer be hard-coded with 9 – Information not available. The default value will be elective. This is a required field.

    A new fatal error message will prevent the authorization of a claim when the Total Charge dollar amount does not equal the sum of the dollar amounts for the line items on the claim.

    With Patch IB\*2\*665, a new fatal error message will prevent the authorization of a UB-04 Medicare claim with secondary insurance when too many codes are entered as follows:

    Error - Claim cannot contain more than 25 Procedure Codes for EDI submission.

    Error - Claim cannot contain more than 24 Occurrence Codes for EDI submission.

    Error - Claim cannot contain more than 24 Occurrence Span Codes for EDI submission.

    Error - Claim cannot contain more than 23 Value Codes for EDI submission.

    Error - Claim cannot contain more than 24 Condition Codes for EDI submission.

    Error - 24 Other diagnosis codes are allowed on an electronic institutional claim.

    Error - 17 Other Diagnosis Codes allowed on a printed UB-04

    Error - 3 e-diagnosis codes are allowed on a printed UB04.

    Error - 12 e-diagnosis codes are allowed on an electronic institutional claim.

    Error – Institutional claims cannot contain more than 999 Revenue Codes.

    A new fatal error message will prevent the authorization of a UB-04 Commercial Insurance only claim when too many codes are entered as follows:

    Error - Claim cannot contain more than 25 Procedure Codes for EDI submission.  
    If claim needs more than 25 Procedure Codes, then select 'Force to Print'.

    Error - Claim cannot contain more than 24 Occurrence Codes for EDI submission.  
    If claim needs more than 24 Occurrence Codes, then select 'Force to Print'.

    Error - Claim cannot contain more than 24 Occurrence Span Codes for EDI submission.  
    If claim needs more than 24 Occurrence Span Codes, select 'Force to Print'.

    Error - Claim cannot contain more than 23 Value Codes for EDI submission.  
    If more than 23 Value Codes need to be entered, select 'Force to Print'.

    Error - Claim cannot contain more than 24 Condition Codes for EDI submission.  
    If more than 24 Condition Codes are needed, select 'Force to Print'

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/UB-04 SCREEN \<5\>

============================================================================

EVENT - OUTPATIENT INFORMATION

\[1\] Event Date : XXX XX, XXXX

\[2\] Prin. Diag.: ABDOM PAIN, L L QUADR - 789.04

Other Diag.: BENIGN NEOPLASM LG BOWEL - 211.3

Other Diag.: DIVERTICULOSIS OF COLON - 562.10

\[3\] OP Visits : XXX XX, XXXX

Type :

\[4\] Cod. Method: HCPCS

CPT Code : LESION REMOVE COLONOSCOPY 45384 XXX XX, XXXX

CPT Code : OFFICE/OUTPATIENT VISIT, NEW 99201 XXX XX, XXXX

CPT Code : CHEST X-RAY 71010-ET XXX XX, XXXX

\[5\] Rx. Refills: UNSPECIFIED \[NOT REQUIRED\]

\[6\] Pros. Items: UNSPECIFIED \[NOT REQUIRED\]

\[7\] Occ. Code : ONSET OF SYMPTOMS/ILLNESS XXX XX, XXXX

\[8\] Cond. Code : UNSPECIFIED \[NOT REQUIRED\]

\[9\] Value Code : UNSPECIFIED \[NOT REQUIRED\]

\<RET\> to CONTINUE, 1-9 to EDIT, '^N' for screen N, or '^' to QUIT:

283. If all information has been entered correctly, Screen 7 will be auto-populated (as shown below) with the necessary information to send the claim electronically. *Make sure that the Disch Stat field in Section 1 is populated*. Press the \<Enter\> key to move to Screen 8.
80. Allowable dollar amounts have been increased to 9999999.99 before users will be forced to split lines.

    With Patch IB\*2\*516, new prompts have been added to Screens 4 and 5 to allow users to enter NDCs and Units to non-RX procedures for medications administered in an outpatient setting. With Patch IB\*2\*577, users will gain the ability to define the type of Units and will no longer default to Units. The new choices are: International Unit; Gram; Milligram; Milliliter or Unit.

    With Patch IB\*2\*516, new prompts have been added to Screens 4 and 5 to allow users to enter 80 character descriptions to CPT / HCPCS procedure codes for services Not Otherwise Classified.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX – Outpat/UB-04 SCREEN \<7\>

BILLING – GENERAL INFORMATION

\[1\] Bill Type : 131 Loc. Of Care: HOSPITAL – INPT OR OPT (INCLU

Charge Type : INSTITUTIONAL Disch Stat: DISCHARGED TO HOME OR SELF CAR

Form Type : UB-04 Timeframe: ADMIT THRU DISCHARGE

Bill Classif: OUTPATIENT Division: CHEYENNE VAMROC

\[2\] Sensitive? : UNSPECIFIED Assignment: YES

\[3\] Bill From : XXX XX, XXXX Bill To: XXX XX, XXXX

\[4\] OP Visits : XXX XX, XXXX

\[5\] Rev. Code : 750-GASTR-INST SVS 45384 \$X,XXX.XX OUTPATIENT VISIT

Rev. Code : 324-DX X-RAY/CHEST 71010 \$XXX.XX OUTPATIENT VISIT

Rev. Code : 510-CLINIC 99201 \$XXX.XX OUTPATIENT VISIT

OFFSET : \$0.00 \[NO OFFSET RECORDED\]

BILL TOTAL : \$X,XXX.XX

\[6\] Rate Sched : (re-calculate charges)

\[7\] Prior Claims: UNSPECIFIED

\<RET\> to CONTINUE, 1-7 to EDIT, ‘^N’ for screen N, or ‘^’ to QUIT:

81. After Patch IB\*2\*432, it will no longer be possible to authorize a Sensitive claim unless users indicated that a Release of Information has been completed.

    After Patch IB\*2\*665 , a new fatal error message will prevent the authorization of a UB-04 claim when too many Revenue codes are entered:

    Error - Institutional claims cannot contain more than 999 Revenue Codes.
284. On Screens 8 and 9, enter any necessary Claim level data to the claim.
82. IB\*2\*447 moved Screen 8, Section 3 Ambulance Information to a new Screen 9.

    After Patch IB\*2\*623, the user no longer need to indicate a Release of Information has been completed when authorizing a Sensitive claim with the date of service on or after 01/28/2019.

    After Patch IB\*2\*641, a new fatal error will prevent the authorization of claims with total billed charges of zero.

IB,PATIENT MRA XX-XX-XXXX BILLX: KXXXXXX - Inpat/UB04 SCREEN \<8\>

=============================================================================

BILLING - CLAIM INFORMATION

\[1\] COB Non-Covered Charge Amt:

\[2\] Property Casualty Information

Claim Number: Contact Name:

Date of 1st Contact: Contact Phone:

\[3\] Surgical Codes for Anesthesia Claims

Primary Code: Secondary Code:

\[4\] Paperwork Attachment Information

Report Type: NN Transmission Method: XX

Attachment Control X: XXXXXXXXXX

\[5\] Disability Start Date: Disability End Date:

\[6\] Assumed Care Date: Relinquished Care Date:

\<RET\> to CONTINUE '^N' for screen N, or '^' to QUIT:

83. For Worker’s Compensation Claims Only (Rate Type = Worker’s Comp.): The Paperwork Attachment Information will now AUTOMATICALLY print in CMS-1500 Box 19, in the following format: PWKNNFX1234890701.

IB,PATIENT F BILLX: KXXXXXX - Outpat/1500 SCREEN \<9\>

================================================================================

AMBULANCE INFORMATION

\[1\] Ambulance Transport Data

D/O Location:

P/U Address1: D/O Address1:

P/U Address2: D/O Address2:

P/U City: D/O City:

P/U State/Zip: D/O State/Zip:

Patient Weight: 195 Transport Distance: 200

Transport Reason: Patient was transported to nearest facility for care

of symptoms, complaints or both.

R/T Purpose: Patient fell and sustained possible injuries to neck

Stretcher Purpose: Patient unable to walk due to possible injuries to

neck

\[2\] Ambulance Certification Data

Condition Indicator: 01 - Admitted to hospital

04 - Moved by stretcher

06 - Transported in emergency situation

08 - Visible hemorrhaging

09 - Medically necessary service

\<RET\> to CONTINUE '^N' for screen N, or '^' to QUIT:

285. On Screen 10, enter 3 to enter the name of the Attending Physician. The claim level attending is still required. An outpatient UB-04 claim can also contain a line-level or claim level Referring, Operating and / or Other Operating Physician(s).
84. Remember: Patch IB\*2\*432 will make it possible to enter and transmit Line Level providers. Line Level and Claim Level providers should not be the same. Claim Level providers apply to the entire claim. Line Level providers are exceptions.

    With Patch IB\*2\*432, users cannot authorize a claim which has an Other Operating Physician unless there is an Operating Physician on the claim.

    Patch IB\*2\*432 will make it possible to enter a Referral Number for each payer on the claim.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/UB-04 SCREEN \<10\>

============================================================================

BILLING - SPECIFIC INFORMATION

\[1\] Bill Remarks

\- FL-80 : UNSPECIFIED \[NOT REQUIRED\]

ICN/DCN(s) : UNSPECIFIED \[NOT REQUIRED\]

Auth/Referral : UNSPECIFIED \[NOT REQUIRED\]

Admission Source : UNSPECIFIED

\[2\] Pt Reason f/Visit : UNSPECIFIED

\[3\] Providers :

\- ATTENDING : UNSPECIFIED

\[4\] Other Facility (VA/non): UNSPECIFIED \[NOT REQUIRED\]

\[5\] Billing Provider : ANYTOWN VAMC

Taxonomy Code : XXXXXXXXXX

\[6\] Alt Prim Payer ID : P: XXXXXXXXXXXXXXX

\[7\] Force To Print? : NO FORCED PRINT

\[8\] Provider ID Maint : (Edit Provider ID information)

\<RET\> to CONTINUE, 1-8 to EDIT, '^N' for screen N, or '^' to QUIT:

85. The Primary ID (NPI) for the Attending, Operating or Other Operating Physician is always transmitted with a claim.

    The Secondary IDs for the Attending, Operating or Other Operating Physician are determined from what the user enters and from entries in Provider ID Maintenance.

    A fatal error message will prevent users from authorizing an adjustment claim, Type of Bill Frequency Code of 7 or 8, in which the destination payer (primary/secondary/tertiary) individual control number (ICN/DCN) is not present

    Patch IB\*2\*547added a field to Screen 10 for alternative payer primary IDs which are used to direct claims to administrative contractors who process specialized claims such as Durable Medical Equipment (DME) claims. Unless an alternative ID is added to the claim by the billing clerk, the regular EDI – Primary Payer ID will be sent with a claim.

When a provider is first added to Screen 10, the user will be shown a screen that contains a list of all the provider’s IDs, the ID type and, optionally, the care unit on file for the provider's IDs. This will include the provider's own IDs, the provider's IDs assigned by the insurance company, the insurance company defaults, if any, and all IDs assigned to the provider by care unit.

The first two entries in this list will always be:

1.  NO SECONDARY ID NEEDED.
286. ADD AN ID FOR THIS CLAIM ONLY.

<u>WARNING</u>: Any ID entered on Screen 10 will automatically override any default provider secondary ID that exists for the same ID Qualifier for this claim ONLY.

\*\*\*\* SECONDARY PERFORMING PROVIDER IDs \*\*\*\*

PRIMARY INSURANCE CO: BLUE CROSS CA (WY)

PROVIDER: IB,PHYSICIAN4 (ATTENDING)

INS. COMPANY'S DEFAULT SECONDARY ID TYPE IS: BLUE CROSS ID

SELECT A SECONDARY ID OR ACTION FROM THE LIST BELOW:

1 - NO SECONDARY ID NEEDED

2 - ADD AN ID FOR THIS CLAIM ONLY

3 - \<DEFAULT\> XXXXBCROSS BLUE CROSS ID

4 - WYXXXX ST LIC (WY)

Selection: 3//

If there is a default secondary ID found, based on the insurance company parameters and the Provider ID is defined in the Provider ID Maintenance, this will be the 3rd entry in the list and will be preceded with the text \<DEFAULT\>. If this ID exists, the default for the Selection prompt will be 3.

If no default ID exists, the default for the selection prompt will be 1 – No Secondary ID needed.

Any care units assigned to an ID using Provider ID Maintenance are displayed at the far right of the ID line. The user no longer has to enter a care unit on the bill.

The user can make a selection from the list by choosing the number preceding the ID the user wants to assign to the provider for the bill. This will add both the ID Qualifier and the ID number to the claim.

86. If the Provider has multiple IDs defined, the one the user select or the new one time only ID that the user enters, will appear on Screen 10 and will be the first ID sent but the system will still transmit the remaining IDs. The one the user selects will just be the first one transmitted. The maximum number that will be transmitted is five.

    With Patch IB\*2\*432, IDs for Line Level providers are determined in the same manner as Claim Level Providers.

If none of the IDs are valid for the provider for the claim, the user can add a new ID *for this claim only*.

1.  At the Selection prompt, type 2 to add an ID for this claim only.
287. At the PRIM INS PERF PROV SECONDARY ID TYPE: prompt, enter the ID Qualifier that the primary payer requires as a secondary ID type. Type two question marks (??) to see the list of possible choices. (For this example, type Location Number as the secondary ID Qualifier).
288. At the PRIM INS PERF PROV SECONDARY ID: prompt, enter the ID number provided by the payer. In this example, type XXXXA.

Selection: 3// 2

PRIM INS PERF PROV SECONDARY ID TYPE: ??

Choose from:

BLUE CROSS ID

BLUE SHIELD ID

COMMERCIAL ID

LOCATION NUMBER

MEDICARE PART A

MEDICARE PART B

PRIM INS PERF PROV SECONDARY ID TYPE: LOCATION NUMBER

PRIM INS PERF PROV SECONDARY ID: XXXXA

After an ID and ID Qualifier are added to the claim for a provider, the provider’s name and the selected ID are displayed on Screen 10. These fields can be edited / deleted.

If a Physician / Provider is deleted, the next time the provider entry is accessed, the list of valid IDs will be displayed again.

| Secondary ID Types                                          | Current Payer                                                                                                                                                   |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attending / Referring / Operating / Other Operating (UB-04) | State License; Blue Cross; Blue Shield; Medicare Part A; UPIN; TRICARE; Commercial ID; Location Number; Network ID; SSN; State Industrial and Accident Provider |
| Rendering/Referring/Supervising (1500)                      | State License; Blue Shield; Medicare Part B; UPIN; TRICARE; Commercial ID; Location Number; Network ID; SSN; State Industrial and Accident Provider             |

<span id="_Toc100304287" class="anchor"></span>Table : Valid Secondary ID Types for Other Payer (Not Current)

| Secondary ID Types                    | Current Payer                                                                       |
|---------------------------------------|-------------------------------------------------------------------------------------|
| Attending / Operating / Other (UB-04) | Blue Cross; Blue Shield; Medicare; Commercial ID; Location Number                   |
| Rendering (1500)                      | Blue Shield; Medicare Part A and Part B; Commercial ID; Location Number; Network ID |
| Referring (1500)                      | Blue Shield; Medicare Part A and Part B; Commercial ID; Location Number; Network ID |
| Supervising (1500)                    | Blue Shield; Medicare Part A and Part B; Commercial ID; Network ID                  |

<span id="_Toc100304288" class="anchor"></span>Table : Valid Secondary ID Types for Current Payer

289. At the \<RET\> to Continue: prompt (any screen), enter ?PRV to see summary information about a particular provider.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/UB-04 SCREEN \<10\>

==================================================================================

BILLING - SPECIFIC INFORMATION

\[1\] Bill Remarks

\- FL-80 : UNSPECIFIED \[NOT REQUIRED\]

ICN/DCN(s) : UNSPECIFIED \[NOT REQUIRED\]

Auth/Referral : UNSPECIFIED \[NOT REQUIRED\]

Admission Source : PHYSICIAN REFERRAL

\[2\] Pt Reason f/Visit : COUGH - 786.2

*\[3\] Providers :- ATTENDING (MD) : IB,DOCTOR4 Taxonomy: XXXXXXXXXX (XX)*

\[4\] Other Facility (VA/non): UNSPECIFIED \[NOT REQUIRED\]

\[5\] Billing Provider : ANYTOWN VAMC

Taxonomy Code : XXXXXXXXXX

\[6\] Force To Print? : NO FORCED PRINT

\[7\] Provider ID Maint : (Edit Provider ID information)

\<RET\> to CONTINUE, 1-7 to EDIT, '^N' for screen N, or '^' to QUIT: *?PRV*

(V)A or (N)on-VA Provider: *V*// A PROVIDER

This is a display of provider specific information.

This bill is UB-04/Outpatient

This is a display of provider specific information.

This bill is UB-04/Outpatient

The valid provider functions for this bill are:

1 REFERRING SITUATIONAL - ALREADY ON BILL

2 OPERATING SITUATIONAL - NOT ON BILL

3 RENDERING SITUATIONAL - ALREADY ON BILL

4 ATTENDING REQUIRED - ALREADY ON BILL

9 OTHER OPERATING OPTIONAL - NOT ON BILL

Select PROVIDER NAME: *IB,Doctor RAD* PI

--------------------------------------------------------------------------------

Signature Name: DOCTOR RAD IB

Signature Title:

Degree: MD

NPI: XXXXXXXXXX

License(s): WY: XXXXXXX

Person Class: XXXXXXX

PROVIDER TYPE: Allopathic and Osteopathic Physicians

CLASSIFICATION: Radiology

SPECIALIZATION: Body Imaging

TAXONOMY: XXXXXXXXXX (XXX)

EFFECTIVE: 6/7/10

RC Provider Group: None

--------------------------------------------------------------------------------

Select PROVIDER NAME:

290. At the \<RET\> to Continue: prompt (any screen), enter ?ID to see what IDs will be transmitted with the claim.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/UB-04 SCREEN \<10\>

==================================================================================

BILLING - SPECIFIC INFORMATION

\[1\] Bill Remarks

\- FL-80 : UNSPECIFIED \[NOT REQUIRED\]

ICN/DCN(s) : UNSPECIFIED \[NOT REQUIRED\]

Auth/Referral : UNSPECIFIED \[NOT REQUIRED\]

Admission Source : PHYSICIAN REFERRAL

\[2\] Pt Reason f/Visit : COUGH - 786.2

\[3\] Providers :

\- REFERRING (MD) : IB,DOCTOR GP Taxonomy: XXXXXXXXXX (XX)

\[P\]VAD000 \[S\]999999999

\- RENDERING (MD) : IB,DOCTOR CARD Taxonomy: XXXXXXXXXX (XX)

\[P\]VAD000 \[S\]999999999

\- ATTENDING (MD) : IB,DOCTOR4 Taxonomy: XXXXXXXXXX (XX)

\[P\]VAD000 \[S\]999999999

\[4\] Other Facility (VA/non): UNSPECIFIED \[NOT REQUIRED\]

\[5\] Billing Provider : ANYTOWN VAMC

Taxonomy Code : XXXXXXXXXX

\[6\] Force To Print? : NO FORCED PRINT

\[7\] Provider ID Maint : (Edit Provider ID information)

\<RET\> to CONTINUE, 1-7 to EDIT, '^N' for screen N, or '^' to QUIT: *?ID*

If this bill is transmitted electronically, the following IDs will be sent:

Primary Ins Co: BLUE CROSS CA (WY) \<\<\<Current Ins

Secondary Ins Co: AETNA US HEALTHCARE

Provider IDs: (VistA Records OP1,OP2,OP4,OP8,OP9,OPR2,OPR3,OPR4,OPR5,OPR8):

ATTENDING: IB,DOCTOR4

NPI: XXXXXXXXXX

Secondary IDs

\(P\) BLUE CROSS XXXXXX

REFERRING: IB,DOCTOR GP

NPI: XXXXXXXXXX

\(P\) BLUE CROSS XXXXXX

RENDERING: IB,DOCTOR CARD

NPI: XXXXXXXXXX

\(P\) BLUE CROSS XXXXXX

Billing Provider Name and ID Information

Billing Provider: ANYTOWN VAMC

Billing Provider NPI: XXXXXXXXXX

Billing Provider Tax ID (VistA Record PRV): 999999999

Billing Provider Secondary IDs (VistA Record CI1A):

\(P\) PROVIDER SITE NUMBER 0000 \<\<\<System Generated ID

\(P\) BLUE CROSS XXXXXX

Service Line Providers

Service Line: 3

RENDERING: IB,DOCTOR RAD

NPI: XXXXXXXXXX

\(P\) BLUE CROSS XXXXXX

\(P\) EIN XXXXXXXXX

\(P\) STATE LICENSE XXXXXXX

Press ENTER to continue

291. Press the \<Enter\> key to move through the fields. At the Want To Authorize Bill At This Time?: and Authorize Bill Generation?: prompts, enter Yes. The claim is now complete and will be transmitted to the FSC in Austin at the next regularly scheduled transmission time.

WANT TO EDIT SCREENS? NO// \<ENTER\>

WANT TO AUTHORIZE BILL AT THIS TIME? No// *YES*

AUTHORIZE BILL GENERATION?: *YES*

Adding bill to BILL TRANSMISSION File.

*Bill will be submitted electronically*

Passing completed Bill to Accounts Receivable. Bill is no longer editable.

Completed Bill Successfully sent to Accounts Receivable.

This Bill Can Not Be Printed Until Transmit Confirmed

This Outpatient INSTITUTIONAL bill may have corresponding PROFESSIONAL

charges.

## CMS-1500 Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following screens provide a simplified example of a CMS-1500 claim.

1.  When processing a CMS-1500 claim, information on Screens 1 and 2 should be reviewed for correctness. Press the \<Enter\> key to move from one screen to the next.
292. On Screen 3, the payer information is reviewed for correctness. The patient may have more than one insurance policy. If the correct information is not displayed, select a section (1, 2, or 3 ) and edit the necessary fields. Press the \<Enter\> key to continue to Screen 4.
87. With Patch IB\*2\*516, users will have the ability to add a one-time HPID, per payer, to a claim if the HPID in the Insurance Company file is not the correct one. The HPID will not be stored in the Insurance Company file. The HPID will only apply to the claim.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Inpat/1500 SCREEN \<3\>

============================================================================

PAYER INFORMATION

*\[1\]* Rate Type : REIMBURSABLE INS. Form Type: CMS 1500

Responsible: INSURER Payer Sequence: Primary

Bill Payer : Blue Cross Fep Transmit: Yes

Ins 1: Blue Cross Fep Policy X: RXXXXXXXXX

Grp X: XXX Whose: VETERAN Rel to Insd: PATIENT

Grp Nm: STANDARD FAMILY Insd Sex: MALE Insured: IB,PATIENT3

*\[2\]* Billing Provider Secondary IDs:

Primary : XXXXXX

Secondary: Tertiary :

*\[3\]* Mailing Address : Electronic ID: XXXXX

Blue Cross Fep

REDACTED

, AL XXXXXXXXX

\<RET\> to CONTINUE, 1-3 to EDIT, '^N' for screen N, or '^' to QUIT:

293. Specify the correct diagnosis and procedure code(s) that must be on this claim. Press the \<Enter\> key to move to Screen 6.
88. With Patch IB\*2\*516, users will have the ability to re-sequence diagnosis codes that have been linked to a specific procedure without breaking the link.

    With Patch IB\*2\*516, new prompts have been added to Screens 4 and 5 to allow users to enter NDCs and Units to non-RX procedures for medications administered in an outpatient setting. With Patch IB\*2\*577, users can also select the type of units.

    With Patch IB\*2\*516, new prompts have been added to Screens 4 and 5to allow users to enter 80 character descriptions to CPT/HCPCS procedure codes for services Not Otherwise Classified.

    Patch IB\*2\*608 will provide the ability to enter the data for Certificate of Medical Necessity-CMS-484-Oxygen and DME Information Form (DIF)-CMS-10126-Enteral and Parenteral Nutrition. When a CMN CPT code that has been defined in the IB Site Parameters is entered, the “CMN Required? will be prompted.

    With Patch IB\*2\*665, a new fatal error message will prevent the authorization of a CMS 1500 claim when too many condition or diagnosis codes are entered as follows:

    Error - Claim cannot contain more than 24 Condition Codes for EDI submission.

    Error - 12 diagnosis codes are allowed on a professional claim.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/1500 SCREEN \<5\>

============================================================================

EVENT - OUTPATIENT INFORMATION

\<1\> Event Date : OCT 12, 2010

\[2\] Prin. Diag.: ACUTE BRONCHITIS - 466.0

Other Diag.: DMI WO CMP NT ST UNCNTRL - 250.01

\[3\] OP Visits : OCT 12,2010,

\[4\] Cod. Method: HCPCS

CPT Code : CHEST X-RAY 71010-26 466.0 OCT 12, 2010

\[5\] Rx. Refills: UNSPECIFIED \[NOT REQUIRED\]

\[6\] Pros. Items: UNSPECIFIED \[NOT REQUIRED\]

\[7\] Occ. Code : UNSPECIFIED \[NOT REQUIRED\]

\[8\] Cond. Code : UNSPECIFIED \[NOT REQUIRED\]

\<9\> Value Code : UNSPECIFIED \[NOT REQUIRED\]

\<RET\> to CONTINUE, 1-9 to EDIT, '^N' for screen N, or '^' to QUIT:

294. Verify that the Form Type is CMS-1500 and that the date of billing is entered. Make sure the Disch Stat field is populated. If all the data have been entered correctly, section 5 should display the correct revenue codes and costs. Press the \<Enter\> key to move to Screen 8.
89. There is a new non-fatal Warning message when a claim contains a Revenue code(s) which generates a zero dollar amount charge.

    After Patch IB\*2\*432, it will no longer be possible to authorize a Sensitive claim unless users indicated that a Release of Information has been completed.

    After Patch IB\*2\*432, Section 1 of screens 6/7 will no longer have fields for Covered, non-Covered or Co-insurance Days. This information will need to be added to a claim using Condition Codes.

    Allowable dollar amounts have been increased to 9999999.99 before users will be forced to split lines.

    After Patch IB\*2\*432, it will be possible to add line-level Additional OB Minutes to an anesthesia claim for an Obstetric procedure that requires more than the normal amount of minutes.

    After Patch IB\*2\*623, the user no longer needs to indicate a Release of Information has been completed when authorizing a Sensitive claim with the date of service on or after 01/28/2019.

    After Patch IB\*2\*641, a new fatal error will prevent the authorization of claims with total billed charges of zero.

    After Patch IB\*2\*641, a new fatal error will prevent professional claims from being authorized when a procedure is missing the place of service.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX – Outpat/1500 SCREEN \<7\>

BILLING – GENERAL INFORMATION

\[1\] Bill Type : 131 Loc. Of Care: HOSPITAL – INPT OR OPT (INCLU

Charge Type : PROFESSIONAL Disch Stat: DISCHARGED TO HOME OR SELF CAR

Form Type : CMS-1500 Timeframe: ADMIT THRU DISCHARGE

Bill Classif: OUTPATIENT Division: CHEYENNE VAMROC

\[2\] Sensitive? : NO Assignment: YES

\[3\] Bill From : OCT 12, 2010 Bill To: OCT 13, 2010

\[4\] OP Visits : OCT 12,2010,

\[5\] Rev. Code : 324-DX X-RAY/CHEST 71010 \$45.30 OUTPATIENT VISIT

OFFSET : \$0.00 \[NO OFFSET RECORDED\]

BILL TOTAL : \$45.30

\[6\] Rate Sched : (re-calculate charges)

\[7\] Prior Claims: UNSPECIFIED

\<RET\> to CONTINUE, 1-7 to EDIT, ‘^N’ for screen N, or ‘^’ to QUIT:

295. On Screens 8 and 9, enter any necessary Claim level data to the claim.
90. IB\*2\*447 moved Screen 8, Section 3 Ambulance Information to a new Screen 9.

    IB\*2\*448 moved Screen 10.

IB,PATIENT MRA XX-XX-XXXX BILLX: KXXXXXD - Outpat/1500 SCREEN \<8\>

=============================================================================

BILLING - CLAIM INFORMATION

\[1\] COB Non-Covered Charge Amt:

\[2\] Property Casualty Information

Claim Number: Contact Name:

Date of 1st Contact: Contact Phone:

\[3\] Surgical Codes for Anesthesia Claims

Primary Code: Secondary Code:

\[4\] Paperwork Attachment Information

Report Type: Transmission Method:

Attachment Control X:

\[5\] Disability Start Date: Disability End Date:

\[6\] Assumed Care Date: Relinquished Care Date:

\[7\] Special Program:??

This is the Special Program with which a claim is associated. Refer to

MEDICARE regulations to decide when to use this field.

Choose from:

01 EPSDT/CHAP

02 Phys Handicapped Children Program

03 Special Fed Funding

05 Disability

07 Induced Abortion - Danger to Life

08 Induced Abortion - Rape or Incest

09 2nd Opinion/Surgery

Special Program:

\[8\] Homebound: ??

This is to indicate that the patient is homebound or

institutionalized. Refer to MEDICARE regulations on when to

use this field.

Choose from:

0 NO

1 YES

Homebound:

\[9\] Date Last Seen:??

This is the date a patient was last seen. Refer to MEDICARE

regulations on when to use this field.

Date Last Seen:

\<RET\> to CONTINUE '^N' for screen N, or '^' to QUIT:

91. IB\*2\*488 moved the following Screen 10 fields to Screen 8: Special Program; Date Last Seen; Homebound. These fields no longer print in Box 19.
92. The prompts on Screen 8 are smart prompts, available for the correct form type.

IB,PATIENT MRA XX-XX-XXXX BILLX: KXXXXXE - Outpat/1500 SCREEN \<9\>

================================================================================

AMBULANCE INFORMATION\[1\] Ambulance Transport Data

D/O Location:

P/U Address1: D/O Address1:

P/U Address2: D/O Address2:

P/U City: D/O City:

P/U State/Zip: D/O State/Zip:

Patient Weight: Transport Distance:

Transport Reason:

R/T Purpose:

Stretcher Purpose:

\[2\] Ambulance Certification Data

Condition Indicator: 12 - Confined to a bed or chair

01 - Admitted to hospital

\<RET\> to CONTINUE, 1-2 to EDIT, '^N' for screen N, or '^' to QUIT: 1

P/U Address1:

P/U Address 2:

P/U City:

P/U State:

P/U Zip:

D/O Location:

D/O Address1:

D/O Address2:

D/O City:

D/O State:

D/O Zip:

Patient Weight:

Transport Distance:

Transport Reason:

R/T Purpose:

Stretcher Purpose:

\<RET\> to CONTINUE, 1-2 to EDIT, '^N' for screen N, or '^' to QUIT: 2

Select Ambulance Condition Indicator: 01// ?

Answer with AMBULANCE CONDITION INDICATOR

Choose from:

12

01

You may enter a new AMBULANCE CONDITION INDICATOR, if you wish

Select an Ambulance Condition Indicator. Answer must be 1-2

characters in length.

This limits the entry to five condition indicators.

Answer with AMBULANCE CONDITION INDICATORS CODE

Choose from:

12 Confined to a bed or chair

01 Admitted to hospital

04 Moved by stretcher

05 Unconscious or in Shock

06 Transported in emergency situation

07 Had to be physically restrained

08 Visible hemorrhaging

09 Medically necessary service

Select Ambulance Condition Indicator: 01//

296. From Screen 10, select section 3 to enter the name of the Rendering Provider if necessary. Enter a Referring Provider and / or Supervising Provider if required by the payer for the procedure codes on the claim.
93. Remember: Patch IB\*2\*432 will make it possible to enter and transmit Line Level providers. Line Level and Claim Level providers should not be the same. Claim Level providers apply to the entire claim. Line Level providers are exceptions.

    After Patch IB\*2\*432, it will no longer be possible to authorize a Sensitive claim unless users indicate that a Release of Information has been completed.

    After Patch IB\*2\*623, the user no longer needs to indicate a Release of Information has been completed when authorizing a Sensitive claim with the date of service on or after 01/28/2019.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/1500 SCREEN \<10\>

============================================================================

BILLING - SPECIFIC INFORMATION

\[1\] Unable To Work From: UNSPECIFIED \[NOT REQUIRED\]

Unable To Work To : UNSPECIFIED \[NOT REQUIRED\]

\[2\] ICN/DCN(s) : UNSPECIFIED \[NOT REQUIRED\]

Tx Auth. Code(s) : UNSPECIFIED \[NOT REQUIRED\]

\[3\] Providers :

\- RENDERING (MD) : IB,DOCTOR4 Taxonomy: 000000000X

\[P\]XXXXBCROSS

\[4\] Other Facility (VA/non): UNSPECIFIED \[NOT REQUIRED\]

Lab CLIA X : UNSPECIFIED \[NOT REQUIRED\]

Mammography Cert X : UNSPECIFIED \[NOT REQUIRED\]

\[5\] Chiropractic Data : UNSPECIFIED \[NOT REQUIRED\]

\[6\] Form Locator 19 : UNSPECIFIED \[NOT REQUIRED\]

\[7\] Billing Provider : ANYTOWN VAMC

Taxonomy Code : 282N00000X

\[8\] Force To Print? : NO FORCED PRINT

\[9\] Provider ID Maint : (Edit Provider ID information)

\<RET\> to CONTINUE, 1-6 to EDIT, '^N' for screen N, or '^' to QUIT:

94. The Primary ID (NPI) for the Attending, Operating or Other Physician is always transmitted with a claim.

    The Secondary IDs for the Attending, Operating or Other Physician are determined from what the user enters and from entries in Provider ID Maintenance.

    If users have set a default ID type and made it required for the current or other payer, the claim cannot be authorized if the physician does not have an ID of that type defined.

When a provider is first added to Screen 10, the user will be shown a screen that contains a list of all the provider’s IDs, the ID type and, optionally, the care unit on file for the provider's IDs. This will include the provider's own IDs, the provider's IDs assigned by the insurance company, the insurance company defaults, if any, and all IDs assigned to the provider by care unit.

The first 2 entries in this list will always be:

1.  NO SECONDARY ID NEEDED
2.  ADD AN ID FOR THIS CLAIM ONLY

<u>WARNING</u>: Any ID entered on Screen 10 will automatically override any default provider secondary ID that exists for the same ID Qualifier for this claim ONLY.

\*\*\*\* SECONDARY PERFORMING PROVIDER IDs \*\*\*\*

PRIMARY INSURANCE CO: BLUE CROSS CA (WY)

PROVIDER: IB,PHYSICIAN4 (ATTENDING)

INS. COMPANY'S DEFAULT SECONDARY ID TYPE IS: BLUE SHIELD ID

SELECT A SECONDARY ID OR ACTION FROM THE LIST BELOW:

1 - NO SECONDARY ID NEEDED

2 - ADD AN ID FOR THIS CLAIM ONLY

3 - \<DEFAULT\> XXXXBSHIELD BLUE SHIELD ID

4 - WYXXXX ST LIC (WY)

Selection: 3//

If there is a default secondary ID found, based on the insurance company parameters and the Provider ID is defined in the Provider ID Maintenance, this will be the 3rd entry in the list and will be preceded with the text \<DEFAULT\>. If this ID exists, the default for the Selection prompt will be 3.

If no default ID exists, the default for the selection prompt will be 1 – No Secondary ID needed.

Any care units assigned to an ID using Provider ID Maintenance are displayed at the far right of the ID line. The user no longer has to enter a care unit on the bill.

The user can make a selection from the list by choosing the number preceding the ID the user wants to assign to the provider for the bill. This will add both the ID Qualifier and the ID number to the claim.

95. If the Provider has multiple IDs defined, the one the user selects or the new one time only ID that the user enters, will appear on Screen 10 and will be the first ID sent but the system will still transmit the remaining IDs. The one the user selects will just be the first one transmitted. The maximum number that will be transmitted is five.

If none of the IDs are valid for the provider for the claim, the user can add a new ID *for this claim only*.

1.  At the Selection prompt, type 2 to add an ID for this claim only.
297. At the PRIM INS PERF PROV SECONDARY ID TYPE: prompt, enter the ID Qualifier that the primary payer requires as a secondary ID type. Type two question marks (??) to see the list of possible choices. (For this example, type Location Number as the secondary ID Qualifier).
298. At the PRIM INS PERF PROV SECONDARY ID: prompt, enter the ID number provided by the payer. In this example, type XXXXA.

Selection: 3// *2*

PRIM INS PERF PROV SECONDARY ID TYPE: *??*

Choose from:

BLUE CROSS ID

BLUE SHIELD ID

COMMERCIAL ID

*LOCATION NUMBER*

MEDICARE PART A

MEDICARE PART B

PRIM INS PERF PROV SECONDARY ID TYPE: *LOCATION NUMBER*

PRIM INS PERF PROV SECONDARY ID: *XXXXA*

After an ID and ID Qualifier are added to the claim for a provider, the provider’s name and the selected ID are displayed on Screen 8. These fields can be edited/deleted.

If a Physician / Provider is deleted, the next time the provider entry is accessed, the list of valid IDs will be displayed again.

| Secondary ID Types                         | Current Payer                                                                                                                                                   |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Attending / Operating / Other (UB-04)      | State License; Blue Cross; Blue Shield; Medicare Part A; UPIN; TRICARE; Commercial ID; Location Number; Network ID; SSN; State Industrial and Accident Provider |
| Rendering / Referring / Supervising (1500) | State License; Blue Shield; Medicare Part B; UPIN; TRICARE; Commercial ID; Location Number; Network ID; SSN; State Industrial and Accident Provider             |

<span id="_Toc100304289" class="anchor"></span>Table : Valid Secondary ID Types for Other Payer (Not Current)

| Secondary ID Types                    | Current Payer                                                                                      |
|---------------------------------------|----------------------------------------------------------------------------------------------------|
| Attending / Operating / Other (UB-04) | Blue Cross; Blue Shield; Medicare Part A and Part B; UPIN; TRICARE; Commercial ID; Location Number |
| Rendering (1500)                      | Blue Shield; Medicare Part A and Part B; Commercial ID; Location Number; Network ID                |
| Referring (1500)                      | Blue Shield; Medicare Part A and Part B; Commercial ID; Location Number; Network ID                |
| Supervising (1500)                    | Blue Shield; Medicare Part A and Part B; Commercial ID; Network ID                                 |

<span id="_Toc100304290" class="anchor"></span>Table : Valid Secondary ID Types for Current Payer

299. At the \<RET\> to Continue: prompt (any screen), enter ?PRV to see summary information about a particular provider.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/UB04 SCREEN \<10\>

==================================================================================

BILLING - SPECIFIC INFORMATION

\[1\] Bill Remarks

\- FL-80 : UNSPECIFIED \[NOT REQUIRED\]

ICN/DCN(s) : UNSPECIFIED \[NOT REQUIRED\]

Auth/Referral : UNSPECIFIED \[NOT REQUIRED\]

Admission Source : PHYSICIAN REFERRAL

\[3\] Providers :

\- RENDERING (MD) : IB,DOCTOR4 Taxonomy: XXXXXXXXXX

\[P\]XXXXBCROSS

\[4\] Other Facility (VA/non): UNSPECIFIED \[NOT REQUIRED\]

Lab CLIA X : UNSPECIFIED \[NOT REQUIRED\]

Mammography Cert X : UNSPECIFIED \[NOT REQUIRED\]

\[5\] Chiropractic Data : UNSPECIFIED \[NOT REQUIRED\]

\[6\] Form Locator 19 : UNSPECIFIED \[NOT REQUIRED\]

\[7\] Billing Provider : ANYTOWN VAMC

Taxonomy Code : XXXXXXXXXX

\[8\] Force To Print? : NO FORCED PRINT

\[9\] Provider ID Maint : (Edit Provider ID information)

\<RET\> to CONTINUE, 1-7 to EDIT, '^N' for screen N, or '^' to QUIT:*?PRV*

(V)A or (N)on-VA Provider: V// *NON-VA PROVIDER*

Select NON-VA PROVIDER NAME: *IB,OUTSIDEDOC* OI

--------------------------------------------------------------------------------

Signature Name: OUTSIDEDOC IB

NPI: XXXXXXXXXX

License(s): None Active on X/X/XX

Person Class: XXXXXXX

PROVIDER TYPE: Allopathic and Osteopathic Physicians

CLASSIFICATION: Resident, Allopathic (includes Interns, Residents, Fellows)

SPECIALIZATION:

TAXONOMY: XXXXXXXXXX (144)

--------------------------------------------------------------------------------

Select NON-VA PROVIDER NAME:

300. At the \<RET\> to Continue: prompt (any screen), enter ?ID to see what IDs will be transmitted with the claim.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/UB04 SCREEN \<10\>

==================================================================================

BILLING - SPECIFIC INFORMATION

\[1\] Bill Remarks

\- FL-80 : UNSPECIFIED \[NOT REQUIRED\]

ICN/DCN(s) : UNSPECIFIED \[NOT REQUIRED\]

Auth/Referral : UNSPECIFIED \[NOT REQUIRED\]

Admission Source : PHYSICIAN REFERRAL

\[3\] Providers :

\- RENDERING (MD) : IB,DOCTOR4 Taxonomy: XXXXXXXXXX

\[P\]XXXXBCROSS

\[4\] Other Facility (VA/non): UNSPECIFIED \[NOT REQUIRED\]

Lab CLIA X : UNSPECIFIED \[NOT REQUIRED\]

Mammography Cert X : UNSPECIFIED \[NOT REQUIRED\]

\[5\] Chiropractic Data : UNSPECIFIED \[NOT REQUIRED\]

\[6\] Form Locator 19 : UNSPECIFIED \[NOT REQUIRED\]

\[7\] Billing Provider : ANYTOWN VAMC

Taxonomy Code : XXXXXXXXXX

\[8\] Force To Print? : NO FORCED PRINT

\[9\] Provider ID Maint : (Edit Provider ID information)

\<RET\> to CONTINUE, 1-7 to EDIT, '^N' for screen N, or '^' to QUIT: *?ID*

IF THIS BILL IS TRANSMITTED ELECTRONICALLY, THE FOLLOWING IDS WILL BE SENT:

PRIMARY INS CO: BLUE CROSS CA (WY) \<\<\<Current Ins

SECONDARY INS CO: TPM TRUST

PROVIDER IDs: (VISTA RECORDS OP1,OP2,OP4,OP8,OP9,OPR2,OPR3,OPR4,OPR5,OPR8):

ATTENDING/RENDERING: IB,DOCTOR 4

NPI: XXXXXXXXXX

SSN: XXXXXXXXX

SECONDARY IDs

\(P\) LOCATION NUMBER XXXXA

\(P\) BLUE CROSS ID XXXXBCROSS

\(P\) ST LIC (WY) WYXXXX

301. Press the \<Enter\> key to move through the fields. At the Want To Authorize Bill At This Time?: and Authorize Bill Generation?: prompts, enter Yes. The claim is now complete and will be transmitted to the FSC at the next regularly scheduled transmission time.

Executing A/R edits

No A/R errors found

WANT TO EDIT SCREENS? NO//

THIS BILL WILL BE TRANSMITTED ELECTRONICALLY

WANT TO AUTHORIZE BILL AT THIS TIME? No// *YES*

AUTHORIZE BILL GENERATION?: *YES*

Adding bill to BILL TRANSMISSION File.

*Bill will be submitted electronically*

Passing completed Bill to Accounts Receivable. Bill is no longer editable.

Completed Bill Successfully sent to Accounts Receivable.

This Bill Can Not Be Printed Until Transmit Confirmed

## J430D Claims 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following screens provide a simplified example of a J430D claim.

1.  When processing a J430D claim, information on Screens 1 and 2 should be reviewed for correctness. Press the \<Enter\> key to move from one screen to the next.
302. On Screen 3, the payer information is reviewed for correctness. The patient may have more than one insurance policy. If the correct information is not displayed, select a section (1, 2, or 3 ) and edit the necessary fields. Press the \<Enter\> key to continue to Screen 5.
96. Medicare does NOT accept Dental claims. If the user attempts to bill Medicare, the user will get a Fatal Error message.

    \*\*Errors\*\*:

    Medicare (WNR) does not accept Dental claims.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpt/J430D SCREEN \<3\>

============================================================================

PAYER INFORMATION

*\[1\]* Rate Type : REIMBURSABLE INS. Form Type: J430D

Responsible: INSURER Payer Sequence: Primary

Bill Payer : Delta Dental Transmit: Yes

Ins 1: Dental Delta Policy X: RXXXXXXXX

Grp X: XXXX Whose: VETERAN Rel to Insd: PATIENT

Grp Nm: STANDARD FAMILY Insd Sex: MALE Insured: IB,PATIENT3

*\[2\]* Billing Provider Secondary IDs:

Primary :

Secondary: Tertiary :

*\[3\]* Mailing Address : Electronic ID: XXXXX

Delta Dental

REDACTED

ANYTOWN, FL XXXXXXXXX

\<RET\> to CONTINUE, 1-3 to EDIT, '^N' for screen N, or '^' to QUIT:

303. Specify the correct diagnosis and procedure code(s) that must be on this claim. Press the \<Enter\> key to move to Screen 7.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/J430D SCREEN \<5\>

============================================================================

EVENT - OUTPATIENT INFORMATION

\<1\> Event Date : OCT 12, 2017

\[2\] Prin. Diag.: Arrested dental caries - K02.3

\[3\] OP Visits : OCT 12,2017,

\[4\] Cod. Method: HCPCS

CPT Code : DENTAL SEALANT PER TOOTH D1351 K02.3 OCT 12, 2017

\<5\> Rx. Refills: UNSPECIFIED \[NOT REQUIRED\]

\<6\> Pros. Items: UNSPECIFIED \[NOT REQUIRED\]

\[7\] Occ. Code : UNSPECIFIED \[NOT REQUIRED\]

\<RET\> to CONTINUE, 1-9 to EDIT, '^N' for screen N, or '^' to QUIT:

304. Verify that the Form Type is J430D and that the date of billing is entered. Make sure the Disch Stat field is populated. If all the data have been entered correctly, section 5 should display the correct revenue codes and costs. Press the \<Enter\> key to move to Screen 8.
97. The Occurrence Code field can be used to add Accident Information to a Dental claim if necessary. The Occurrence codes will not be transmitted as Occurrence codes but the Accident information will be transmitted. An accident date is required on Dental claims that contain a Property and Casualty number.

    There are new Line Level data fields specific to Dental claims:

    Oral Cavity Designation (1):

    Prosthesis/Crown/Inlay Code:

    Prior Placement Date Qualifier:

    Prior Placement Date:

    Tooth Code:

    Tooth Surface:

    Orthodontic Banding Date:

    Orthodontic Banding Replacement Date:

    Treatment Start Date:

    Treatment Completion Date
98. Type of Service is not available for Dental Claims.

    With Patch IB\*2\*650, a Dental claim will not transmit without a Prior Placement Date and a Prior Placement Date Qualifier.

    With Patch IB\*2\*665, a new fatal error message will prevent the authorization of a Dental claim when too many diagnosis codes are entered as follows:

    Error – 4 diagnosis codes are allowed on a dental claim.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/J430D SCREEN \<7\>

============================================================================

BILLING - GENERAL INFORMATION

\[1\] Bill Type : 131 Loc. of Care: HOSPITAL - INPT OR OPT (INCLU

Charge Type : PROFESSIONAL Disch Stat: DISCHARGED TO HOME OR SELF CAR

Form Type : J430D Timeframe: ADMIT THRU DISCHARGE

Bill Classif: OUTPATIENT Division: CHEYENNE VAMROC

\[2\] Sensitive? : NO Assignment: YES

\[3\] Bill From : OCT 12, 2017 Bill To: OCT 12, 2017

\[4\] OP Visits : OCT 12,2017,

\[5\] Rev. Code : 512-DENTAL CLINIC D1351 \$64.29 OUTPATIENT VISIT

OFFSET : \$0.00 \[NO OFFSET RECORDED\]

BILL TOTAL : \$64.29

\[6\] Rate Sched : (re-calculate charges)

\[7\] Prior Claims: UNSPECIFIED

\<RET\> to CONTINUE, 1-7 to EDIT, '^N' for screen N, or '^' to QUIT:

305. On Screens 8, enter any necessary Claim level data to the claim.
99. The claim data is specific to Dental Claims. The Dental Paperwork functions as it does for other claims except the list of available attachments is different and more specific to dental.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpt/J430D SCREEN \<8\>

=============================================================================

DENTAL - CLAIM INFORMATION

\[1\] Tooth Status

\[2\] Orthodontic Information

Banding Date:

Treatment Months Count:

Treatment Months Remaining Count:

Treatment Indicator:

\[3\] Dental Paperwork Attachment

Report Type: Trans Method:

Attachment Control X:

\[4\] Property Casualty Information

Claim Number:

\<RET\> to CONTINUE, 1-4 to EDIT, '^N' for screen N, or '^' to QUIT:

306. From Screen 10, select section 3 to enter the name of the Rendering Provider or Assistant Surgeon if necessary. Enter a Referring Provider and / or Supervising Provider if required by the payer for the procedure codes on the claim.
100. Both a Rendering Provider and an Assistant Surgeon are not allowed on the same Dental claim.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/J430D SCREEN \<10\>

============================================================================

BILLING - SPECIFIC INFORMATION

\<1\> Unable To Work From: UNSPECIFIED \[NOT REQUIRED\]

Unable To Work To : UNSPECIFIED \[NOT REQUIRED\]

\[2\] ICN/DCN(s) : UNSPECIFIED \[NOT REQUIRED\]

Auth/Referral : UNSPECIFIED \[NOT REQUIRED\]

\[3\] Providers : UNSPECIFIED

\<4\> Other Facility (VA/non): UNSPECIFIED \[NOT REQUIRED\]

Lab CLIA X : UNSPECIFIED \[NOT REQUIRED\]

Mammography Cert X : UNSPECIFIED \[NOT REQUIRED\]

\<5\> Chiropractic Data : UNSPECIFIED \[NOT REQUIRED\]

\[6\] Dental Claim Note : UNSPECIFIED \[NOT REQUIRED\]

\[7\] Billing Provider : ANYTOWN VAMC

Taxonomy Code : XXXXXXXXXX

\[8\] Alt Prim Payer ID : UNSPECIFIED \[NOT REQUIRED\]

\<9\> Force To Print? : NO FORCED PRINT

\[10\] Provider ID Maint : (Edit Provider ID information)

\<RET\> to CONTINUE, 1-10 to EDIT, '^N' for screen N, or '^' to QUIT:

101. Section 4 is disabled. Users cannot create claims for non-VA Dental services.

     Section 6 allows users to enter a free text, up to 80 character, dental specific comment

     Section 9 is disabled. Users cannot print Dental claims.

     Though allowed, VistA will not provide the ability to define secondary IDs for Dental Claims.

     With Patch IB\*2\*623, users will have the ability to view the following data at the end of the claim or do a ?J430D on any billing screens:

     Claim provider(s) from screen 10

     Dental Claim Note (35)

     Diagnosis Codes (Display diagnosis codes 1 through 4 only)

     Date of Service (24)

     Place of Service (38)

     Oral Cavity Designation (25)

     Tooth Code (27)

     Tooth Surface (28)

     Procedure Code (29)

     Modifier (29)

     Associated Diagnosis (29a)

     Quantity (29b)

     Charge (31)

Example of dx, procedures, teeth info, and charges entered on the Dental claim

--------------------------------------------------------------------------------

Claim Provider:

Rendering/XXXXXXXXXX Referring/XXXXXXXXX Supervising/XXXXXXXXX

34a. Diagnosis:

1.XX1 2.XX2 3.XX3 4.XX4

35\. Dental Claim Note:

THIS IS A TEST FOR THIS CLAIM.

24 25 27 28 29 29a 29b 31 38

--------------------------------------------------------------------------------

03 26 18 03 26 18 01 02 10 20 30 11 BDFIL DXXXX ABCD 1 183722 22

03 26 18 03 26 18 2 MO DYYYY AC 1 100000 22

--------------------------------------------------------------------------------

| Secondary ID Types              | Current Payer                                       |
|---------------------------------|-----------------------------------------------------|
| Rendering / Supervising (J430D) | State License; UPIN; Commercial ID; Location Number |
| Assistant Surgeon (J430D        | State License; UPIN; Commercial ID; Location Number |
| Referring (J430D)               | State License; UPIN; Commercial ID                  |

<span id="_Toc100304291" class="anchor"></span>Table : Valid Secondary ID Types for Other Payer (Not Current)

| Secondary ID Types        | Current Payer                                       |
|---------------------------|-----------------------------------------------------|
| Rendering (J430D)         | State License; UPIN; Commercial ID; Location Number |
| Referring (J430D)         | State License; UPIN; Commercial ID                  |
| Supervising (J430D)       | State License; UPIN; Commercial ID; Location Number |
| Assistant Surgeon (J430D) | State License; UPIN; Commercial ID; Location Number |

<span id="_Toc30513948" class="anchor"></span>Table : Acronyms and Abbreviations

307. Press the \<Enter\> key to move through the fields. At the Want To Authorize Bill At This Time?: and Authorize Bill Generation?: prompts, enter Yes. The claim is now complete and will be transmitted to the FSC at the next regularly scheduled transmission time.

Executing A/R edits

No A/R errors found

WANT TO EDIT SCREENS? NO//

THIS BILL WILL BE TRANSMITTED ELECTRONICALLY

WANT TO AUTHORIZE BILL AT THIS TIME? No// *YES*

AUTHORIZE BILL GENERATION?: *YES*

Adding bill to BILL TRANSMISSION File.

*Bill will be submitted electronically*

Passing completed Bill to Accounts Receivable. Bill is no longer editable.

Completed Bill Successfully sent to Accounts Receivable.

## Lab Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EDI Enhanced HIPAA format allows users to enter a CLIA# when billing for certain laboratory procedures. The VA’s CLIA \# must be entered on Screen 8 when billing a Medicare secondary payer for laboratory and pathology procedures that are not reimbursed in full by Medicare.

The following screens provide a simplified example of a lab claim:

1.  When processing a Laboratory claim, information on Screens 1 and 2 should be reviewed for correctness. Press the \<Enter\> key to move from one screen to the next.
308. On Screen 3, the payer information is reviewed for correctness. The patient may have more than one insurance policy. If the correct information is not displayed, select a section (1, 2, or 3 ) and edit the necessary fields. Press the \<Enter\> key to continue to Screen 5.
102. With Patch IB\*2\*516, users will have the ability to add a one-time HPID, per payer, to a claim if the HPID in the Insurance Company file is not the correct one. The HPID will not be stored in the Insurance Company file. The HPID will only apply to the claim.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/1500 SCREEN \<3\>

============================================================================

PAYER INFORMATION

*\[1\]* Rate Type : REIMBURSABLE INS. Form Type: CMS 1500

Responsible: INSURER Payer Sequence: Primary

Bill Payer : Blue Cross Fep Transmit: Yes

Ins 1: Blue Cross Fep Policy X: RXXXXXXXX

Grp X: XXX Whose: VETERAN Rel to Insd: PATIENT

Grp Nm: STANDARD FAMILY Insd Sex: MALE Insured: IB,PATIENT3

*\[2\]* Billing Provider Secondary IDs:

Primary : XXXXXX

Secondary: Tertiary :

*\[3\]* Mailing Address : Electronic ID: XXXXX

Blue Cross Fep

REDACTED

Anytown, AL XXXXXXXXX

\<RET\> to CONTINUE, 1-3 to EDIT, '^N' for screen N, or '^' to QUIT:

309. Specify the correct diagnosis and procedure code(s) that must be on this claim. Press the \<Enter\> key to move to Screen 7.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/1500 SCREEN \<5\>

============================================================================

EVENT - OUTPATIENT INFORMATION

\[1\] Event Date : XX XX,XXXX

\[2\] Prin. Diag.: URINARY FREQUENCY - 788.41

\[3\] OP Visits : XXX XX,XXXX

\[4\] Cod. Method: HCPCS

CPT Code : URINALYSIS, AUTO W/SCOPE 81001 XXX XX,XXXX

CPT Code : URINE BACTERIA CULTURE 87088 XXX XX,XXXX

\[5\] Rx. Refills: UNSPECIFIED \[NOT REQUIRED\]

\[6\] Pros. Items: UNSPECIFIED \[NOT REQUIRED\]

\[7\] Occ. Code : UNSPECIFIED \[NOT REQUIRED\]

\[8\] Cond. Code : UNSPECIFIED \[NOT REQUIRED\]

\[9\] Value Code : UNSPECIFIED \[NOT REQUIRED\]

\<RET\> to CONTINUE, 1-9 to EDIT, '^N' for screen N, or '^' to QUIT:

310. Verify that the Form Type is CMS-1500 and that the date of billing is entered. Make sure the Disch Stat field is populated. If all the data have been entered correctly, section 5 should display the correct revenue codes and costs. Press the \<Enter\> key to move to Screen 8.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXX - Outpat/1500 SCREEN \<7\>

============================================================================

BILLING - GENERAL INFORMATION

\[1\] Bill Type : 131 Loc. of Care: HOSPITAL - INPT OR OPT (INCLU

Charge Type : PROFESSIONAL Disch Stat: DISCHARGED TO HOME OR SELF CAR

Form Type : CMS-1500 Timeframe: ADMIT THRU DISCHARGE

Bill Classif: OUTPATIENT Division: ANYTOWN VAMROCY VAMC

\[2\] Sensitive? : UNSPECIFIED Assignment: YES

\[3\] Bill From : *XXX XX,XXXX* Bill To: *XXX XX,XXXX*

\[4\] OP Visits : *XXX XX,XXXX\[5\] Rev. Code : 306-LAB/BACT-MICRO 87088 \$33.20 OUTPATIENT VISITRev. Code : 307-GASTR-INST SVS 81001 \$12.77 OUTPATIENT VISIT*

OFFSET : \$0.00 \[NO OFFSET RECORDED\]

*BILL TOTAL : \$45.97*

\[6\] Rate Sched : (re-calculate charges)

\[7\] Prior Claims: UNSPECIFIED

\<RET\> to CONTINUE, 1-7 to EDIT, '^N' for screen N, or '^' to QUIT:

311. On Screens 8 and 9, enter any necessary Claim level data to the claim and press the ENTER key to move to Screen 10.
103. IB\*2\*447 moved Screen 8, Section 3 Ambulance Information to a new Screen 9.

IB,PATIENT MRA XX-XX-XXXX BILLX: KXXXXXD - Outpat/1500 SCREEN \<8\>

=============================================================================

BILLING - CLAIM INFORMATION

\[1\] COB Non-Covered Charge Amt:

\[2\] Property Casualty Information

Claim Number: Contact Name:

Date of 1st Contact: Contact Phone:

\[3\] Surgical Codes for Anesthesia Claims

Primary Code: Secondary Code:

\[4\] Paperwork Attachment Information

Report Type: Transmission Method:

Attachment Control X:

\[5\] Disability Start Date: Disability End Date:

\[6\] Assumed Care Date: Relinquished Care Date:

\[7\] Special Program:

\[8\] Homebound:

\[9\] Date Last Seen:

\<RET\> to CONTINUE '^N' for screen N, or '^' to QUIT:

104. IB\*2\*488 moved the following Screen 10 fields to Screen 8: Special Program; Date Last Seen; Homebound. These fields no longer print in Box 19.

IB,PATIENT MRA XX-XX-XXXX BILLX: KXXXXXE - Outpat/1500 SCREEN \<9\>

=============================================================================

AMBULANCE INFORMATION\[1\] Ambulance Transport Data

D/O Location:

P/U Address1: D/O Address1:

P/U Address2: D/O Address2:

P/U City: D/O City:

P/U State/Zip: D/O State/Zip:

Patient Weight: Transport Distance:

Transport Reason:

R/T Purpose:

Stretcher Purpose:

\[2\] Ambulance Certification Data

Condition Indicator: 12 - Confined to a bed or chair

01 - Admitted to hospital

\<RET\> to CONTINUE, 1-2 to EDIT, '^N' for screen N, or '^' to QUIT: 1

P/U Address1:

P/U Address 2:

P/U City:

P/U State:

P/U Zip:

D/O Location:

D/O Address1:

D/O Address2:

D/O City:

D/O State:

D/O Zip:

Patient Weight:

Transport Distance:

Transport Reason:

R/T Purpose:

Stretcher Purpose:

\<RET\> to CONTINUE, 1-2 to EDIT, '^N' for screen N, or '^' to QUIT: 2

Select Ambulance Condition Indicator: 01// ?

Answer with AMBULANCE CONDITION INDICATOR

Choose from:

12

01

You may enter a new AMBULANCE CONDITION INDICATOR, if you wish

Select an Ambulance Condition Indicator. Answer must be 1-2

characters in length.

This limits the entry to five condition indicators.

Answer with AMBULANCE CONDITION INDICATORS CODE

Choose from:

12 Confined to a bed or chair

01 Admitted to hospital

04 Moved by stretcher

05 Unconscious or in Shock

06 Transported in emergency situation

07 Had to be physically restrained

08 Visible hemorrhaging

09 Medically necessary service

Select Ambulance Condition Indicator: 01//

312. From Screen 10, enter 3 to add a Rendering and Referring and Supervising provider, if necessary.
313. To edit, select Section 5 and enter the CLIA \# if required by the payer.
105. After Patch IB\*2.0\*320, the billing software will automatically populate the CLIA# for the division on the claim when the claim is for the Service Type = 5 (Diagnostic Laboratory) if the CLIA# exists in the VistA Institution file. Users may override this value for the current claim only.

     For outside laboratory services, the billing software will automatically populate the CLIA# if there is a Laboratory or Facility secondary ID defined for the outside facility with an ID Qualifier of X4 (CLIA \#).

     There will be an Error Message for laboratory claims to Medicare when there is no CLIA# on the claim and a Warning Message for laboratory claims to other payers when there is no CLIA# on the claim.

IB,PATIENT3 XX-XX-XXXX BILLX: KXXXXXX - Outpat/1500 SCREEN \<10\>

============================================================================

BILLING - SPECIFIC INFORMATION

\[\[1\] Bill Remarks

\- FL-80 : UNSPECIFIED \[NOT REQUIRED\]

ICN/DCN(s) : UNSPECIFIED \[NOT REQUIRED\]

Auth/Referral : UNSPECIFIED \[NOT REQUIRED\]

Admission Source : PHYSICIAN REFERRAL

\[3\] Providers :

*- REFERRING (MD) : IB,DOCTOR5 Taxonomy: XXXXXXXXXX (XX)\[P\]XX0000- RENDERING (MD) : IB,DOCTOR4 Taxonomy: XXXXXXXXXX (XX)\[P\]XXX123*

\[4\] Other Facility (VA/non): UNSPECIFIED \[NOT REQUIRED\]

*Lab CLIA X : DXXXXXXX*

Mammography Cert X : UNSPECIFIED \[NOT REQUIRED\]

\[5\] Chiropractic Data : UNSPECIFIED \[NOT REQUIRED\]

\[6\] CMS-1500 Box 19 : UNSPECIFIED \[NOT REQUIRED\]

\[7\] Billing Provider : ANYTOWN VAMC

Taxonomy Code : XXXXXXXXX

\[8\] Alt Prim Payer ID : UNSPECIFIED \[NOT REQUIRED\]

\[9\] Force To Print? : NO FORCED PRINT

\[10\] Provider ID Maint : (Edit Provider ID information)

\<RET\> to CONTINUE, 1-10 to EDIT, '^N' for screen N, or '^' to QUIT: 6

CMS-1500 Box 19: ??

This is an 71 character free-text field that will print in Box 19

of the CMS-1500. Use this field to enter additional Payer required

IDs in the format of Qualifier\<no space\>ID number\<3 spaces\>

Qualifier\<no space\>ID number.

CMS-1500 Box 19: ??

DISPLAY THE FULL CMS-1500 BOX 19?: NO//

106. Patch IB\*2\*488 changed the prompt Form Locator 19 to CMS-1500 Box 19 and updated the Help text.

     There is a new field in Section 4 for the Mammography Certification Number where users can enter a certification number on claims for mammography exams. The known Mammography Certification Numbers will be stored in the Institution file, one per site.

     Patch IB\*2\*547 added a field to Screen 10 for alternative payer primary IDs which are used to direct claims to administrative contractors who process specialized claims such as Durable Medical Equipment (DME) claims.

## Pharmacy Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1500 pharmacy claims can be submitted electronically to the clearinghouse where the claims will be printed and mailed. If a pharmacy claim is entered on a UB04, the claim must be printed locally.

The following screens give a simplified example of a pharmacy claim.

1.  When processing a Pharmacy claim, information on Screens 1 and 2 should be reviewed for correctness. Press the \<Enter\> key to move from one screen to the next.
314. On Screen 3, the payer information should be reviewed for correctness. The patient may have more than one insurance policy. If the correct information is not displayed, select a section (1, 2, or 3) and edit the necessary fields. Press the \<Enter\> key to continue to Screen 5.
107. For Pharmacy claims, change the form type to a CMS-1500.

     With Patch IB\*2\*516, users will have the ability to add a one-time HPID, per payer, to a claim if the HPID in the Insurance Company file is not the correct one. The HPID will not be stored in the Insurance Company file. The HPID will only apply to the claim.

IB,PATIENT5 XX-XX-XXXX BILLX: KXXXXXX - Outpat/1500 SCREEN \<3\>

===============================================================================

PAYER INFORMATION

*\[1\]* Rate Type : REIMBURSABLE INS. Form Type: CMS-1500

Responsible: INSURER Payer Sequence: Primary

Bill Payer : CIGNA Transmit: Yes

Ins 1: CIGNA Policy X: XXXXXXXXX

Grp X: GRP NUM XXXX Whose: VETERAN Rel to Insd: PATIENT

Grp Nm: CHALKER Insd Sex: MALE Insured: IB,PATIENT5

Ins 2: BLUE CROSS CA (W Policy X: RXXXXXXXX

Grp X: GRP NUM XXXXX Whose: SPOUSE Rel to Insd: SPOUSE

Grp Nm: HARTLY Insd Sex: FEMALE Insured: IB,WIFE5

*\[2\]* Billing Provider Secondary IDs: UNSPECIFIED \[NOT REQUIRED\]

*\[3\]* Mailing Address :

NO MAILING ADDRESS HAS BEEN SPECIFIED! (Patient has Medicare)

Send Bill to PAYER listed above.

\<RET\> to CONTINUE, *1-3 to EDIT*, '^N' for screen N, or '^' to QUIT:

315. The highlighted fields are auto-populated. Remember that this is a professional bill that is being transmitting as a CMS-1500, so each HCPCS code will have to be associated with a diagnosis code. To begin this process, type 4 to edit the Cod. Method field and press the \<Enter\> key.
108. With Patch IB\*2\*432, when adding a refill to a claim, users will be able to view the date a prescription was order along with the other data.

ADD/EDIT RX FILL 2054788 FOR Oct 26, 2010 CORRECT? YES//

Date RX Ordered: Oct 26, 2010

RX X: XXXXXXX//

DATE: OCT 26,2010//

DRUG: HYDROCHLOROTHIAZIDE 25MG TAB//

DAYS SUPPLY: 30//

QTY: 15//

NDC X: XXXXX-XXXX-XX//

FORMAT OF NDCX: 5-4-2 FORMAT//

The following screen will display:

IB,PATIENT5 XX-XX-XXXX BILLX: KXXXXXX - Outpat/1500 SCREEN \<5\>

===============================================================================

EVENT - OUTPATIENT INFORMATION

\<1\> Event Date : XXX XX,XXXX

*\[2\] Prin. Diag.: ISSUE REPEAT PRESCRIPT - V68.1*

\[3\] OP Visits : UNSPECIFIED

*\[4\] Cod. Method: HCPCS*

CPT Code : Oral prescrip drug non chemo J8499 V68.1 XXX XX,XXXX

*\[5\] Rx. Refills: HYDROCHLOROTHIAZIDE 25MG TAB* XXX XX,XXXX

\[6\] Pros. Items: UNSPECIFIED \[NOT REQUIRED\]

\[7\] Occ. Code : UNSPECIFIED \[NOT REQUIRED\]

\[8\] Cond. Code : UNSPECIFIED \[NOT REQUIRED\]

\<9\> Value Code : UNSPECIFIED \[NOT REQUIRED\]

\<RET\> to CONTINUE, 1-9 to EDIT, '^N' for screen N, or '^' to QUIT:

316. At the Select Procedure Date field, re-type the date.
317. At the Select Procedure field, type the appropriate code. Once the code auto-populates the data, type YES to confirm.
318. At the Provider field, type the name of the physician. Information related to that provider will auto-populate.
319. Type the appropriate data related to the Place of Service and the Type of Service.
320. Press the \<Enter\> key until Screen 5 appears.

\<\<CURRENT PROCEDURAL TERMINOLOGY CODES\>\>

LISTING FROM VISIT DATES WITH ASSOCIATED CPT CODES

IN OUTPT ENCOUNTERS FILE

===============================================================================

NO. CODE SHORT NAME CLINIC DATE

===============================================================================

NO CPT CODES ON FILE FOR THE VISIT DATES ON THIS BILL

PROCEDURE CODING METHOD: HCPCS (1500 COMMON PROCEDURE CODING SYSTEM)

//

Select PROCEDURE DATE (X/XX/XX-XX/XX/XX): XX-XX-XX

\* Patient has no Visits for this date...

Select PROCEDURE: J

Searching for a CPT,(pointed-to by PROCEDURES)

J8499 Oral prescrip drug non chemo

...OK? Yes// Yes Oral prescrip drug non chem Rx: 0000000D

PROCEDURES: J8499//

Select CPT MODIFIER SEQUENCE:

PROVIDER: IB,DOCTOR6//

ASSOCIATED CLINIC: CARDIAC CONSULT

DIVISION: ANY VAMC// XXX

PLACE OF SERVICE: XX OUTPATIENT HOSPITAL

TYPE OF SERVICE: 1 MEDICAL CARE

EMERGENCY PROCEDURE?: NO// NO

PRINT ORDER:

321. Notice the association has been made between the diagnosis code and the required procedure code. Press the \<Enter\> key to move to Screen 7.

IB,PATIENT5 XX-XX-XXXX BILLX: KXXXXX - Outpat/1500 SCREEN \<5\>

===============================================================================

EVENT - OUTPATIENT INFORMATION

\<1\> Event Date : XXX XX,XXXX

\[2\] Prin. Diag.: ISSUE REPEAT PRESCRIPT - V68.1

\[3\] OP Visits : XXX XX,XXXX

\[4\] Cod. Method: HCPCS

CPT Code : Oral prescrip drug non chemo *J8499 VXX.X* XXX XX,XXXX

\[5\] Rx. Refills: RANITIDINE HCL 150MG (ZANTAC) TAB XXX XX,XXXX

\[6\] Pros. Items: UNSPECIFIED \[NOT REQUIRED\]

\[7\] Occ. Code : UNSPECIFIED \[NOT REQUIRED\]

\[8\] Cond. Code : UNSPECIFIED \[NOT REQUIRED\]

\<9\> Value Code : UNSPECIFIED \[NOT REQUIRED\]

\<RET\> to CONTINUE, 1-9 to EDIT, '^N' for screen N, or '^' to QUIT:

322. If all the data have been entered correctly, section 5 should display the correct revenue code and charges.. Press the \<Enter\> key to move to Screen 8.

IB,PATIENT5 XX-XX-XXXX BILLX: KXXXXX - Outpat/1500 SCREEN \<7\>

===============================================================================

BILLING - GENERAL INFORMATION

\[1\] Bill Type : 131 Loc. of Care: HOSPITAL - INPT OR OPT (INCLU

Covered Days: UNSPECIFIED Bill Classif: OUTPATIENT

Non-Cov Days: UNSPECIFIED Timeframe: ADMIT THRU DISCHARGE

Charge Type : UNSPECIFIED Disch Stat:

Form Type : CMS-1500 Division: ANYTOWN VAMC

\[2\] Sensitive? : UNSPECIFIED Assignment: YES

\[3\] Bill From : XXX XX,XXXX Bill To: XXX XX,XXXX

\[4\] OP Visits : UNSPECIFIED

\[5\] Rev. Code : 253-WARFARIN SODIUM 5 J8499 1 \$36.00 PRESCRIPTION

OFFSET: \$0.00 \[NO OFFSET RECORDED\]

BILL TOTAL : \$36.00

\[6\] Rate Sched : (re-calculate charges)

\[7\] Prior Claims: UNSPECIFIED

323. On Screens 8 and 9, enter any necessary claim-level data to the claim and press the \<Enter\> key to move to Screen 10.
109. IB\*2\*447 moved Screen 8, Section 3 Ambulance Information to a new Screen 9.

IB,PATIENT MRA XX-XX-XXXX BILLX: KXXXXXD - Outpat/1500 SCREEN \<8\>

================================================================================

BILLING - CLAIM INFORMATION

\<1\> COB Non-Covered Charge Amt:

\<2\> Property Casualty Information

Claim Number: Contact Name:

Date of 1st Contact: Contact Phone:

\<3\> Surgical Codes for Anesthesia Claims

Primary Code: Secondary Code:

\<4\> Paperwork Attachment Information

Report Type: Transmission Method:

Attachment Control X:

\<5\> Disability Start Date: Disability End Date:

\<6\> Assumed Care Date: Relinquished Care Date:

\[7\] Special Program:

\[8\] Homebound:

\[9\] Date Last Seen:

\<RET\> to CONTINUE '^N' for screen N, or '^' to QUIT:

The following screen will display:

IB,PATIENTM M XXX-XX-XXXX BILLX: KXXXXXX - Outpat/UB04 SCREEN \<9\>

================================================================================

AMBULANCE INFORMATION

\<1\> Ambulance Transport Data

D/O Location:

P/U Address1: D/O Address1:

P/U Address2: D/O Address2:

P/U City: D/O City:

P/U State/Zip: D/O State/Zip:

Patient Weight: Transport Distance:

Transport Reason:

R/T Purpose:

Stretcher Purpose:

\<2\> Ambulance Certification Data

Condition Indicator:

\<RET\> to CONTINUE, 1-2 to EDIT, '^N' for screen N, or '^' to QUIT:

324. From Screen 10, enter 3 to add a Rendering provider.

     Patch IB\*2\*547 added a field to Screen 10 for alternative payer primary IDs which are used to direct claims to administrative contractors who process specialized claims such as Durable Medical Equipment (DME) claims.

IB,PATIENT5 XX-XX-XXXX BILLX: KXXXXXX - Outpat/1500 SCREEN \<10\>

================================================================================

BILLING - SPECIFIC INFORMATION

\[1\] Unable To Work From: UNSPECIFIED \[NOT REQUIRED\]

Unable To Work To : UNSPECIFIED \[NOT REQUIRED\]

\[2\] ICN/DCN(s) : UNSPECIFIED \[NOT REQUIRED\]

Auth/Referral : UNSPECIFIED \[NOT REQUIRED\]

\[3\] Providers :

\- RENDERING : UNSPECIFIED

\[4\] Other Facility (VA/non): UNSPECIFIED \[NOT REQUIRED\]

Lab CLIA X : UNSPECIFIED \[NOT REQUIRED\]

Mammography Cert X : UNSPECIFIED \[NOT REQUIRED\]

\[5\] Chiropractic Data : UNSPECIFIED \[NOT REQUIRED\]

\[6\] CMS-1500 Box 19 : UNSPECIFIED \[NOT REQUIRED\]

\[7\] Billing Provider : ANYTOWN VAMC

Taxonomy Code : 282N00000X

\[8\] Alt Prim Payer ID : UNSPECIFED \[NOT REQUIRED\]

\[9\] Force To Print? : NO FORCED PRINT

\[10\] Provider ID Maint : (Edit Provider ID information)

\<RET\> to CONTINUE, 1-10 to EDIT, '^N' for screen N, or '^' to QUIT:

This claim is now ready for authorization.

## Correct Rejected or Denied Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A claim can be rejected at some stage during either the electronic or manual process. A claim can be denied by the payer during the adjudication process. When a claim is either rejected or denied, the claim may be for a reason that can be corrected. Once the claim is corrected, the claim can be retransmitted or resent through the mail to the payer.

With Patch IB\*2\*433, a new option has been added to the IB Module that allows users to correct a claim while maintaining the original claim number on the resubmitted claim.

With Patch IB\*2\*447, users are able to correct all types of claims including a claim that processes to a non-accruing funds. It is now possible to correct a claim with one of the following rate types:

- INTERAGENCY
- SHARING AGREEMENT
- TRICARE
- WORKMAN’S COMP

Follow the steps below to correct a rejected or denied claim.

1.  Access the option Third Party Billing Menu.
325. At the Select Third Party Billing Menu Option: prompt, enter CRD for Correct Rejected/Denied Bill.
326. At the Enter BILL NUMBER or Patient NAME: prompt, enter the claim number of the claim that requires correction.
327. At the ARE YOU SURE YOU WANT TO CANCEL THIS BILL? No// prompt, enter Yes to override the default.
328. At the CANCEL BILL?: prompt, enter YES.
329. At the REASON CANCELLED: prompt, enter a free-text comment.
110. This new option was designed to replace the existing option CLON Copy and Cancel under the majority of circumstances. The existing CLON Copy and Cancel option will now be locked with a new Security Key named IB CLON.

     The existing CLON Copy and Cancel option should only be used to correct denied claims against which a payment has been posted or to correct a claim with one of the Bill Rate Types that are excluded from the new processes..

     The existing CLON Copy and Cancel option should be used to correct denied claims against which a payment has been posted, a secondary/tertiary claim or a claim in MRA Request status.

     The IB CLON security key which restricted the use of the CLON option , was removed with Patch IB\*2\*516.

The following screen will display.

IB,PATIENT4 (XX-XX-XXXX) DOB: XXX XX,XXXX

================================================================================

Rate Type : REIMBURSABLE INS.

Event Date : XXX XX XXXX

Sensitive : NO

Responsible : INSURANCE CARRIER (Specify CARRIER on SCREEN 3)

Loc of Care : HOSPITAL (INCLUDES CLINIC) - INPT. OR OPT.

Event Source : Outpatient

Timeframe : ADMIT THRU DISCHARGE

(Specify actual bill type fields on SCREENs 6/7)

Bill From : XXX XX,XXXX

Bill To : XXX XX,XXXX

Initial BillX : KXXXXXX-01

Copied BillX : KXXXXXX-01

Please verify the above information for the bill you just entered. Once this

information is accepted it will no longer be editable and you will be required

to CANCEL THE BILL if changes to this information are necessary.

IS THE ABOVE INFORMATION CORRECT AS SHOWN? Yes//

330. Return through the claim screens correcting whatever data requires correction.
331. Complete and authorize the claim.
111. The number of the original claim has been incremented and now displays with a -01 after the claim number. The original claim number has been assigned to the new claim. Each time a claim is corrected, the previous cancelled version will be incremented -01, -02, -03, etc..

When a user attempts to use the CRD Correct Rejected/Denied Bill option to correct a claim against which a payment has been posted, the user will be warned that the user must use the existing CLON Copy and Cancel option.

Select Third Party Billing Menu Option: CRD Correct Rejected/Denied Bill

Enter BILL NUMBER or Patient NAME: KXXXXXX IB,PATIENT1 XX-XX-XX

Outpatient REIMBURSABLE INS. PRNT/TX

Please note a PAYMENT of \*\*\$45\*\* has been POSTED to this bill. Copy and cancel

(CLON) must be used to correct this bill.

When a user attempts to use the CRD Correct Rejected/Denied Bill option to correct a denied claim which has received only one of its associated split Explanation of Benefits (EOB), the user will be warned that the user must wait for the arrival of the second EOB before the user can use this new option.

Select Third Party Billing Menu Option: CRD Correct Rejected/Denied Bill

Enter BILL NUMBER or Patient NAME: KXXXXXX IB,PATIENT1 XX-XX-XX

Outpatient REIMBURSABLE INS. PRNT/TX

There is a split EOB associated with this claim. You cannot use this option to Correct this claim until the second EOB has been received.

When a user attempts to use the CRD Correct Rejected/Denied Bill option to correct a rejected or denied claim which has an excluded Billing Rate Type, the user will be warned that the user must use the existing CLON Copy and Cancel option.

Select Third Party Billing Menu Option: CRD Correct Rejected/Denied Bill

Enter BILL NUMBER or Patient NAME: KXXXXXX IB,PATIENT1 XX-XX-XX

Outpatient REIMBURSABLE INS. PRNT/TX

This option cannot be used to correct some Billing Rate Types (Example: TRICARE).

Use Copy and Cancel (CLON) to correct this bill.

When a user attempts to use the CRD Correct Rejected/Denied Bill option to correct a rejected or denied secondary or tertiary claim, the user will be notified that the user must use the existing CLON Copy and Cancel option.

Please note that COB data exists for this bill.

Copy and cancel (CLON) must be used to correct this bill.

When a user attempts to use the CRD Correct Rejected/Denied Bill option to correct a claim with a status of MRA Request, the user will receive the following message.

This bill is in a status of REQUEST MRA.

No MRAs have been received and there are no rejection messages on file

for the most recent transmission of this MRA request bill.

112. The new CRD Correct Rejected/Denied Bill option has been added to the CSA Claims Status Awaiting Resolution option and the MRW MRA Worklist option as Correct Bill.

The history of corrected claims will be available from the following locations:

- BILL - Enter/Edit Billing Information
- INQ – Patient Billing Inquiry

## Viewed Cancelled Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a claim has been cancelled, users can view the data stored in the Bill / Claims file (#399) for the cancelled claim.

The View Cancelled Bill option is on the Third Party Billing Menu.

ADPR Print Bill Addendum Sheet

AUTH Authorize Bill Generation

BILL Enter/Edit Billing Information

CANC Cancel Bill

CLA Multiple CLAIMSMANAGER Claim Send

CLON Copy and Cancel

CRD Correct Rejected/Denied Bill

DLST Delete Auto Biller Results

GEN Print Bill

INQU Patient Billing Inquiry

LIST Print Auto Biller Results

PRNT Print Authorized Bills

RETN Return Bill Menu ...

VCB View Cancelled Bill

VIEW View Bills Pending Transmission

VIST Outpatient Visit Date Inquiry

Select Third Party Billing Menu \<TEST ACCOUNT\> Option:

## Printed Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some claims should not be transmitted electronically and should be printed locally.

These include:

- Claims requiring clinical attachments such as progress notes.
- Professional claims containing more than the maximum number of 8 diagnosis codes.
- Professional claims containing more than the maximum number of diagnosis pointers (4).
- Institutional claims containing more than the maximum number of procedure codes (999).
- Professional claims containing more than the maximum number of procedure codes/line items (50).
- Institutional pharmacy claims.
- Secondary claims to Medicare WNR (When Medicare WNR is NOT the primary insurance).

## View/Resubmit Claims – Live or Test – Synonym: RCB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new option, View/Resubmit Claims – Live or Test, has been added to the EDI menu. This option replaces: Resubmit a Bill; Resubmit a Batch of Bills and View/Resubmit Claims as Test. This option provides the ability to resubmit claims as test claims for testing or production claims for payment.

Patch IB\*2\*547 will add the ability to run the RCB option to find previously printed claims and to resubmit them to the test queue *only*. The claims cannot be retransmitted to the production queue. The patch will also provide the ability to look-up claims to specific payers using the EDI - Inst Payer Primary ID or EDI - Prof Payer Primary ID.

Patch IB\*2\*608 will only include the Coordination of Benefit (COB) data for the previous payer sequence to be resubmitted in the current payer sequence claim to the test queue. The patch will also filter out the claim(s) with associated COB data when those claims have been selected to be retransmitted to the production queue. These non-transmitted claims will be listed on the screen as skipped.

1.  At the Select EDI Menu For Electronic Bills Option, type RCB and press the Return key.
332. At the Run report for (P)rinted or (T)ransmitted claims?: Transmitted// prompt, press the Enter key to accept the default.
333. At the SELECT BY: (C)LAIM OR SEE A (L)IST TO PICK FROM: prompt, press the Enter key to accept the default of List.
334. At the Run for(A)ll payers or (S)elected Payers? prompt, type S for Selected Payers.
113. If the user chooses Selected payers after the user enters Blue Cross of CA, for example, the user will be prompted to include all insurance companies with the same Electronic Billing ID. This will prevent the user from having to enter every BC/BS company defined in your Insurance file.
335. At the Select Insurance Company: prompt, enter an EDI Payer Primary ID.
336. At the Select Insurance Company prompt, press the Enter key when done selecting payers.
337. At the Run for (U)B-04, (C)MS-1500, (J)430D or All: prompt, press the Enter key to accept the default of Both.
114. The Date Range for the search for claims has been restricted to a maximum of90 days to minimize the impact of the search on the system.

     With Patch IB\*2\*665, user can select a Start with Date Last Transmitted using a Date@Time military time parameter to select a range of claims beginning at a specific time period. (e.g., T@0800, 01-01-21@1200, 01-JAN-2021@1600, etc.)

     User can select a Go to Date Last Transmitted using a Date@Time military time parameter to select a range of claims ending at a specific time period. (e.g., T@0700, 01-01-21@1200, 01-JAN-2021@1400, etc.)
338. At the Start with Date Last Transmitted: prompt, type T-200 for this example.
339. At the Go toDate Last Transmitted: prompt, press the Enter key to accept the default of 12/1/04. This will return results for 90 days.
340. At the Select Additional Limiting Criteria (optional): prompt, press the Enter key without selecting anything additional.
115. With Patch IB\*2\*665, there is a new ‘5-A0 Received in Austin only’ option in the Additional Selection Criteria

Select EDI Menu For Electronic Bills Option: RCB View/Resubmit Claims-Live or Test

\*\*\* NOTE: 2 '^' ARE NEEDED TO ABORT THE OPTION (^^)

1 '^' BRINGS YOU BACK TO THE PREVIOUS SELECTION PROMPT(^)

Run report for (P)rinted or (T)ransmitted claims?: Transmitted//Transmitted

Select By: (C)laim or see a (L)ist to pick from?: List//

PAYER SELECTION:

Run for (A)ll Payers or (S)elected Payers?: Selected Payers//Selected Payers

Include all payers with the same electronic Payer ID? Yes// YES

Select Insurance Company: XXXXX

1 XXXXX AETNA HEALTH PLANSREDACTED ANYTOWN,IL XXXXX/XXXXX

2 XXXXX AETNA HEALTH PLANSREDACTED ANYTOWN,NY XXXXX/XXXXX

3 XXXXX AETNA HEALTH PLANSREDACTEDANYTOWN,OH XXXXX/XXXXX

4 XXXXX AETNA HEALTH PLANSREDACTED ANYTOWN,PA XXXXX/XXXXX

4

5 60054 AETNA HEALTH PLANSPO BOX *99999* ANYTOWN,OR 99999/99999

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 AETNA HEALTH PLANS4501 N STERLING PEORIA,IL 99999/99999

Select Another Insurance Company:

BILL FORM TYPE SELECTION:

Run for (U)B-04, (C)MS-1500, (J)430D or (A)ll: All//ALL

LAST BATCH TRANSMIT DATE RANGE SELECTION:

Start with Date Last Transmitted: T-200 (XXX XX, XXXX)

Go to Date Last Transmitted:(T-200 – T-110): T-110// (XXX XX, XXXX)

ADDITIONAL SELECTION CRITERIA:

1 - MRA Secondary Only

2 - Primary Claims Only

3 - Secondary Claims Only

4 - Claims Sent to Print at Clearinghouse Only

5 – A0 Received in Austin only

341. At the Would you like to include cancelled claims? No//: prompt, enter No.
342. At the Would you like to include claims Forced to Print at the Clearinghouse? No// prompt, enter No.
343. At the Sort By prompt, enter B to override the default of Current Payer.
116. Sort by Batch if the user wants to resubmit batches of claims or Current Payer if the user wants to resubmit a variety of individual claims.
344. At the DO YOU WANT A (R)EPORT OR A (S)CREEN LIST FORMAT?: prompt, press the \<Enter\> key to accept the default of Screen List.

Would you like to include cancelled claims? No// NO

Would you like to include claims Forced to Print at the Clearinghouse? No// NO

Sort By: Current Payer// ??

Enter a code from the list.

Select one of the following:

1 Batch By Last Transmitted Date (Claims within a Batch)

2 Current Payer (Insurance Company)

Sort By: Current Payer// Batch By Last Transmitted Date (Claims within a Batch)Do you want a (R)eport or a (S)creen List format?: Screen List//

The following screen is displayed:

PREVIOUSLY TRANSMITTED CLAIMS Mar 21, 2005@15:52:10 Page: 1 of 1215

\*\* A claim may appear multiple times if transmitted more than once. \*\*

\*\* T = Test Claim \*\* R = Batch Rejected

\>\>\>X of Claims Selected: 0 (marked with \*)

Claim X Form Type Seq Status Current Payer

Batch:XXXXXXXXXX Date Last Transmitted: Nov 30, 2004

1 KXXXXXX T UB-04 OUTPT P PRNT/TX AETNA US HEALTHCARE

Batch:XXXXXXXXXX Date Last Transmitted: Nov 30, 2004

2 KXXXXXX UB-04 OUTPT P PRNT/TX AETNA US HEALTHCARE

Batch:XXXXXXXXXX Date Last Transmitted: Nov 30, 2004

3 KXXXXXX T J430D OUTPT P PRNT/TX DELTA DENTAL

Batch:XXXXXXXXXX Date Last Transmitted: Nov 30, 2004

4 KXXXXXX T 1500 OUTPT S PRNT/TX AETNA

Batch:XXXXXXXXXX Date Last Transmitted: Nov 30, 2004

5 KXXXXXX UB-04 OUTPT P PRNT/TX AETNA US HEALTHCARE

Batch:XXXXXXXXXX Date Last Transmitted: Nov 30, 2004

6 KXXXXXX 1500 OUTPT P PRNT/TX AETNA US HEALTHCARE

\+ Enter ?? for more actions \>\>\>

Claim(s) Select/De select View Claims Selected

Select/De select All Claims Print Report

Resubmit Claims Exit

Action: Next Screen//

345. At the Action prompt, type B to select batches of claims to resubmit as test or ‘C’ to select claims.
346. At the Select EDI Transmission Batch Number: prompt, enter the number of the desired batch.
117. The user may repeat the above, entering as many batch numbers as the user want.

     With Patch IB\*2\*665, the user can use the new ‘Select / De select All Claims’ option in the command bar to select/de select a range of claims in the list.

PREVIOUSLY TRANSMITTED CLAIMS Mar 21, 2005@16:07:38 Page: 1 of 1215

\*\* A claim may appear multiple times if transmitted more than once. \*\*

\>\>\>X of Claims Selected: 1 (marked with \*)

Claim X Form Type Seq Status Current Payer

Batch:xxXXXXXXXXXXDate Last Transmitted: Nov 30, 2004

1 \*KXXXXXX UB-04 OUTPT P PRNT/TX UNITED HEALTHCARE

Batch: XXXXXXXXXX Date Last Transmitted: Nov 30, 2004

2 KXXXXXX UB-04 OUTPT P REQUEST MRA MEDICARE (WNR)

Batch: XXXXXXXXXX Date Last Transmitted: Nov 30, 2004

3 KXXXXXX 1500 OUTPT P PRNT/TX UNITED HEALTHCARE

Batch: XXXXXXXXXX Date Last Transmitted: Nov 30, 2004

4 KXXXXXX J430D OUTPT S PRNT/TX Delta Dental

Batch: XXXXXXXXXX Date Last Transmitted: Nov 30, 2004

5 KXXXXXX UB-04 OUTPT P PRNT/TX AETNA US HEALTHCARE

Batch: XXXXXXXXXX Date Last Transmitted: Nov 30, 2004

6 KXXXXXX 1500 OUTPT P PRNT/TX AETNA US HEALTHCARE

\+ Enter ?? for more actions \>\>\>

Claim(s) Select/De select View Claims Selected

Select/De select All Claims Print Report

Resubmit Claims as TEST Exit

Action: Next Screen// b Batch Select/De select

Select EDI TRANSMISSION BATCH NUMBER: XXXXXXXXXX

347. When the user has entered all of the batches the user wants, at the ACTION prompt, type ‘R’ for Resubmit Claims.
348. At the Resubmit Claims: prompt, press the \<Enter\> key to resubmit the claims for payment.
118. The system will inform the user of the number of claims that will be resubmitted and whether or not the users are being submitted for payment or testing.
349. At the Are You Sure You Want To Continue?: prompt, type YES to override the default.

You are about to resubmit 2 claims as Production claims.

Are you sure you want to continue?: NO// *y YES*

Resubmission in process

# Processing of Secondary / Tertiary Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With Patch IB\*2\*432 installed, the procedures for the processing of secondary and tertiary non-MRA claims have changed.

When electronic Explanation of Benefits (EOBs) are received for claims that are NOT Medicare (WNR) claims and the payments are processed in AR, the EOBs will be evaluated and if the data in the EOBs meets certain criteria, the secondary or tertiary claims will either be processed automatically or sent to the new COB Management Worklist for manual processing.

When a claim is processed in AR and its status becomes Collected / Closed, no MailMan message will be generated. Either the subsequent claim will be automatically processed or the claim will appear on the new worklist.

Patch IB\*2\*447 removed the option, Copy for Secondary / Tertiary Bill \[IB COPY SECOND/THIRD\]. This option became obsolete with the install of IB\*2.0\*432 and the introduction of the new CBW (COB Management Work list).

A new, non-human user, IB,AUTHORIZER REG, will be the clerk responsible for the automatic processing of non-MRA secondary and tertiary claims.

In order to be able to either create a subsequent claim, or to send a claim to the new COB Management Worklist for manual processing, the following conditions must be met:

- All Explanation of Benefit (EOBs), 835 Health Care Claim Payment Advice, have been received.
- Payment from the previous payer has been posted by AR.
- The bill status for the previous payer is Collected/Closed.
- Electronic Secondary and Tertiary claim will contain the Coordination of Benefits data from the EOBs in the 837 Health Care Claim transmission to FSC.
119. Secondary and Tertiary claims will be created with a new claim number.

     Remember: Whether or not a Secondary or Tertiary claim to an electronic payer is transmitted or printed, is determined by the new parameter in the Insurance Company Editor. Refer to Section 2.1.1.1.

## Criteria for the Automatic Processing of Secondary or Tertiary Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a non-MRA claim has received all associated EOBs and meets the following criteria, the subsequent claim will be automatically created and either transmitted electronically to the next payer, or printed (along with the associated MRAs / EOBs) and mailed to the next payer:

- EOB contains only Adjustment Group Codes = Contractual Obligation (CO) associated with one of the following Reason Codes: A2; B6; 45; 102; 104; 118; 131; 23; 232; 44; 59; 94; 97; or 10.
- EOB contains only Adjustment Group Codes = Patient Responsibility (PR) associated with one of the following Reason Codes; 1; 2; or 66.
- The sum of the deductible, coinsurance and co-payment amounts is greater than \$0.00.
- The EOB status is Processed (The Claim Status Code is either 1, 2, or 3).

## COB Management Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any non-MRA claim that does not meet the criteria for the automatic creation of a Secondary or Tertiary claim will be placed on the COB Management Worklist.

1.  Access the EDI Menu For Electronic Bills menu.
350. At the Select EDI Menu For Electronic Bills Option: prompt, enter CBW for COB Management Worklist.
120. Patch IB\*2\*516 provided the ability for users to run the worklist by one or more divisions.
351. At the Select Division: ALL// prompt; press the \<Enter\> key to accept the default.
352. At the Select BILLER: ALL// prompt, press the \<Enter\> key to accept the default.
353. At the Sort By: BILLER// prompt, press the \<Enter\> key to accept the default.
354. At the Do you want to include Denied EOBs for Duplicate Claim/Service? No// prompt, press the \<Enter\> key to accept the default.
121. A non-MRA claim which receives a DENIED EOB and which is Collected / Closed by AR and which has a subsequent payer, will also be placed on the CBW. This includes claims that have potential patient responsibility such as TRICARE and CHAMPVA.

     Patch IB\*2\*547 provides additional search and sort criteria for this worklist. Users can create a list of just primary claims or just secondary claims or both, and the users can now sort by primary or secondary insurance company.

     Complete CARC / RARC textual descriptions will display from Print or View an EOB from within the COB Management Worklist.

The following screen will display.

COB Management WorkList JAN 01, 2011@13:41:16 Page: 1 of 20

Bill X Svc Date Patient Name SSN Pt Resp Bill Amt Type

BILLER: IB,CLERK 1

1 XXX-KXXXXXX\* 12/07/10 IB,PATIENT 27345 XXXX 0.00 87.58 O/P

Insurers: AETNA US HEALTHCARE

EOB Status: DENIED, Feb 25, 2004

2 XXX-KXXXXXX\* 12/07/10 IB,PATIENT 4 XXXX 86.40 72.00 O/D

Insurers: DELTA DENTAL

EOB Status: DENIED, Jun 09, 2004

3 XXX-KXXXXXX 12/08/10 IB,PATIENT 33 XXXX 0.00 2243.16 I/I

Insurers: AETNA US HEALTHCARE

EOB Status: DENIED, Jul 28, 2004

4 XXX-KXXXXXX 12/08/10 IB,PATIENT 102 XXXX 0.00 45.61 O/P

Insurers: AETNA US HEALTHCARE

EOB Status: DENIED, Jun 09, 2004

5 XXX-KXXXXXX 12/14/10 IB,PATIENT 10 XXXX 0.00 30.74 O/P

Insurers: AETNA US HEALTHCARE

\+ Enter ?? for more actions

PC Process COB CB Cancel Bill RM Remove from Worklist

VE View an EOB CR Correct Bill PE Print EOB/MRA

EC Enter/View Comments CC Cancel/Clone A Bill TP Third Party Joint Inq.

RS Review Status VB View Bill EX Exit

Select Action: Next Screen//

### Data Displayed for Claims on the COB Management Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following data is displayed on the COB Management Worklist:

- List Number
- Claim Number
- Asterisk – when claim is under review
- Claim Date
- Patient Name
- Last 4 Numbers of Patient’s SSN
- Patient Responsibility Monetary Amount
- Monetary Amount on the Claim
- Patient Status, Inpatient/Outpatient
- Claim Form Type
- Status of EOB
- Insurance Company(s)
- Clerk Name – Depends on Sort Criteria
- Division(s)
- Days since Last Transmission – Depends on Sort Criteria
- Date of EOB - Depends on Sort Criteria

### Available COB Management Worklist Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following actions are available to help the users manage those claims which failed to meet the automatic processing criteria:

- PC: Process COB – Process a claim on the list to the next payer on the bill
- VE: View an EOB – View the EOB(s) associated with a claim on the list
- EC: Enter / View Comments – Enter new comments for a claim on the list or view previously entered comments
- RS: Review Status – Change the review status for a claim on the list
- CB: Cancel Bill – Cancel a bill that does not need to be resubmitted
- CR: Correct Bill – Correct a bill that needs to be resubmitted
- CC: Cancel / Clone A Bill – Clone a bill that needs to be resubmitted (locked with IB CLON)
- VB: View Bill – View the billing screens
- RM: Remove from Worklist – Remove claim from worklist if no need to resubmit
- PE: Print EOB / MRA – Print associated MRAs or EOB
- TP: Third Party Joint Inq. – Select a claim and go directly to the claim in TPJI
- EX: Exit – Exit the worklist and return to the EDI Menu
122. Remove from Worklist was added so that claims that have been Collected / Closed and placed on the worklist can be removed if there is no reason to process it to the next payer (i.e., no Patient Responsibility). These claims should not be cancelled as the claims have been Collected / Closed in AR.

     Remember: It is possible that a tertiary claim on the COB Management Worklist began as an MRA claim. The Print EOB / MRA action will provide users with the option to print both EOBs and MRAs.

# Requests for Additional Data to Support Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*547 added a new worklist and a new inbound transaction, the ASC X12N 5010 Health Care Claim Request for Additional Information (277RFAI) to VistA. The 277RFAI transaction is initiated by the payer in response to a claim for health care services when the payor needs additional information in order to adjudicate the claim correctly.

A 277RFAI might, for example, request an image, a test result, or a Certificate of Medical Necessity. At the time that Patch IB\*2\*547 is installed, the methods for providing this additional data will be manual. In the future, it will be possible to respond to a 277RFAI with an ASC X12N 5010 Additional Information to Support a Health Care Claim or Encounter (275) transaction.

The RFAI Management Worklist was added to provide a method for displaying and managing these requests for additional documentation to support the adjudication of a claim.

1.  Access the EDI Menu For Electronic Bills menu.
355. At the Select EDI Menu For Electronic Bills Option: prompt, enter RFI for RFAI Management Worklist.
356. At the Select Authorizing Biller: ALL// prompt, press the Enter key to accept the default.
357. At the Select Primary Sort: LOINC Code// prompt, press the Enter key to accept the default of LOINC.

The following screen is displayed:

RFAI Management Worklist Apr 28, 2015@14:25:12 Page: 1 of 16

Bill X Payer Name Patient Name SSN Svc Date Curr Bal

1 KXXXXXX MEDICARE (WNR) IB,PATIENT 333 XXXX 06/29/09 \$43851.78

55115-0 - Requested imaging studies information Document

2 KXXXXXX MEDICARE (WNR) IB,PATIENT 22 XXXX 11/05/10 \$1226.18

64286-8 — Deprecated Diagnostic imaging order

3 KXXXXXX UNITEDHEALTHCARE IB,PATIENT 765 XXXX 11/05/10 \$9.65

55115-0 — Requested imaging studies information Document

4 KXXXXXX MEDICARE (WNR) IB,PATIENT 22 XXXX 11/05/10 \$1226.18

22034-3 — Path report.total Cancer

<span class="mark">+ \* Indicates RFAI review in progress</span>

Select Message Exit

ReSort Messages

Select Action: Next Screen//Select Message

Select RFAI Message: (1-4):1

358. At the Select RFAI Message: (1-4) : prompt, enter 1 to select a message to expand.

The following screen is displayed:

RFAI Message Apr 28, 2015@14:43:44 Page: 1 of 2

Bill X Payer Name Patient Name SSN Svc Date Curr Bal

KXXXXXX IB INSURANCE CO IB,PATIENT 33 XXXX 06/29/09 \$43851.78

<span class="mark">Information Source</span>

Payer Name: IB INSURANCE COMPANY

Payer Contact 1: FAX Number There can be up to 3 contact methods

Payer Contact X: XXX XXX-XXXX

Payer Contact 2: Telephone

Payer Contact X: XXX XXX-XXXX EXT: XXXXXXX

Payer Response Contact 1: There can be up to 3 contact methods

Payer Response Contact X: XXX XXX-XXXX

Payer Response Contact 2: Telephone

Payer Response Contact X: XXX XXX-XXXX EXT: XXXXXXX

Payer Address: REDACTEDAnytown, New York XXXXX

Payer Claim Control Number: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

<span class="mark">Claim Level Status Information</span>

Patient Control X: XXXXXXX Claim Number

Date of Service: XX/XX/XX

Medical Records Number: XXXXXXXX

Member Identification Number: XXXXXXXXXX

Type of Service: XXX Institutional Only Type of Bill

Health Care Claim Status Category: These 3 can repeat

Additional Information Request Modifier: Show LOINC Code Text not just code

Status Information Effective Date: XX/XX/XX

Response Due Date: XX/XX/XX

<span class="mark">Service Line Information/ Service Line Status Information</span>

Line Item Control Number: XXXXXX

Service Line Date:

Revenue Code:

Coding Method: HCPCS

Procedure Code:XXXXXXX

Procedure Modifier: There can be up to 4

Procedure Modifier:

Line Item Charge Amount: XXXXXXXXXXXXXXXXXX

Health Care Claim Status Category: These 3 can repeat

Additional Information Request Modifier: Show LOINC Code Text not just code

Status Information Effective Date: XX/XX/XX

Response Due Date: XX/XX/XX

<span class="mark">+ Enter ?? for more</span>

EC Enter Comments TJ Third Party Joint Inq.

RS Review Status EX Exit

RE Remove Entry

Select Action: Next Screen// Remove Entry

From the RFAI message Screen, users can take the following actions:

- Enter comments – user name and date/time will be automatically captured.
- Change the Review Status – the entry with be marked by an asterisk.
- Remove an entry from the list once it has been addressed – user name and date/time will be captured along with free text removal comment.
- Jump to the claim in TPJI – comments from the RFAI Management Worklist will be viewable from within TPJI.

# IB Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Define Printers for Automatically Processed Secondary / Tertiary Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New fields were added to the MCCR Site Parameter Display / Edit option so that users can define printers to which to print automatically processed secondary or tertiary claims and associated EOB / MRAs to payers which cannot support electronic claim transmissions.

1.  Access the MCCR System Definition Menu.
359. At the Select MCCR System Definition Menu Option: prompt, enter Site for MCCR Site Parameter Display/Edit.
360. At the Select Action: prompt, Enter IB to access the IB Site Parameters.

MCCR Site Parameters Feb 01, 2011@15:04:47 Page: 1 of 1

Display/Edit MCCR Site Parameters.

Only authorized persons may edit this data.

IB Site Parameters Claims Tracking ParametersFacility Definition General ParametersMail Groups Tracking ParametersPatient Billing Random SamplingThird Party Billing HCSR ParametersProvider IdEDI TransmissionThird Party Auto Billing Parameters Insurance VerificationGeneral Parameters General ParametersInpatient Admission eIV ParametersOutpatient Visit eIV Batch ExtractsPrescription Refill IIU Parameters

Enter ?? for more actions

IB Site Parameter AB Automated Billing EX Exit

CT Claims Tracking IV Ins. Verification

Select Action: Quit// IB Site Parameters

The following screen will display.

IB Site Parameters Feb 01, 2011@16:22:02 Page: 1 of 5

Only authorized persons may edit this data.

\[1\] Copay Background Error Mg: IB ERROR

Copay Exemption Mailgroup: IB ERROR

Use Alerts for Exemption : NO

\[2\] Hold MT Bills w/Ins : YES X of Days Charges Held: 90

Suppress MT Ins Bulletin : NO

Means Test Mailgroup : IB MEANS TEST

Per Diem Start Date : 11/05/90

\[3\] Disapproval Mailgroup : MCCR - BUSINESS OFFICE

Cancellation Mailgroup : UB-82 CANCELL

Cancellation Remark : BILL CANCELLED IN BUSINESS OFFICE

\[4\] New Insurance Mailgroup : IB NEW INSURANCE

Unbilled Mailgroup : IB UNBILLED AMOUNTS

Auto Print Unbilled List : NO

\+ Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Next Screen//

361. At the Select Action: prompt, press the \<Enter\> key to accept the default of Next Screen until Section 7 is displayed.

IB Site Parameters Feb 01, 2011@16:25:43 Page: 2 of 5

Only authorized persons may edit this data.

\+

\[5\] Medical Center : ANYTOWN VAMC Default Division : ANYTOWN VAMR

MAS Service : BUSINESS OFFICE Billing Supervisor : REDACTED

\[6\] Initiator Authorize: YES Xfer Proc to Sched : YES

Ask HINQ in MCCR : YES Use Non-PTF Codes : YES

Multiple Form Types: YES Use OP CPT screen : YES

\[7\] UB-04 Print IDs : YES UB-04 Address Col :

CMS-1500 Print IDs : YES CMS-1500 Addr Col : 40

CMS-1500 Auto Prter: RM340 UB-04 Auto Prter : RM340

EOB Auto Prter : RM340 MRA Auto Prter : RM340

\[8\] Printed Claims Rev Code Excl: 16 Activated Codes Defined

\[9\] Default RX DX Cd : V68.1 Default ASC Rev Cd : 490

Default RX CPT Cd : J8499 Default RX Rev Cd : 250

\[10\] Bill Signer Name : \<No longer used\> Federal Tax X : XX-XXXXXXX

Bill Signer Title : \<No longer used\>

\+ Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Next Screen//

362. At the Select Action: prompt, enter EP=7.
363. At the CMS-1500 Auto Printer: prompt, enter the name of the printer to which CMS secondary or tertiary claims will print.
364. At the UB04 Auto Printer: prompt, enter the name of the printer to which CMS secondary or tertiary claims will print.
365. At the EOB Auto Printer: prompt, enter the name of the printer to which CMS secondary or tertiary claims will print.
366. At the MRA Auto Printer: prompt, enter the name of the printer to which CMS secondary or tertiary claims will print.
123. The same printer can be used to print more than one thing if your printers are setup to handle more than one form type.

     Remember: The MRA is a 132 column printout.

UB-04 PRINT LEGACY ID: YES//

CMS-1500 PRINT LEGACY ID: YES//

UB-04 ADDRESS COLUMN:

CMS-1500 ADDRESS COLUMN: 40//

CMS-1500 Auto Printer:

UB-04 Auto Printer:

EOB Auto Printer:

MRA Auto Printer:

## Enable Automatic Processing of Secondary / Tertiary Claims

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new field was added to the MCCR Site Parameter Display/Edit option so that users can enable / disable the automatic processing of secondary / tertiary non-MRA claims.

1.  Access the MCCR System Definition Menu.
367. At the Select MCCR System Definition Menu Option: prompt, enter Site for MCCR Site Parameter Display/Edit.
368. At the Select Action: prompt, Enter IB to access the IB Site Parameters.

MCCR Site Parameters Feb 01, 2011@15:04:47 Page: 1 of 1

Display/Edit MCCR Site Parameters.

Only authorized persons may edit this data.

IB Site Parameters Claims Tracking ParametersFacility Definition General ParametersMail Groups Tracking ParametersPatient Billing Random SamplingThird Party Billing HCSR ParametersProvider IdEDI TransmissionThird Party Auto Billing Parameters Insurance VerificationGeneral Parameters General ParametersInpatient Admission eIV ParametersOutpatient Visit eIV Batch ExtractsPrescription Refill IIU Parameters

Enter ?? for more actions

IB Site Parameter AB Automated Billing EX Exit

CT Claims Tracking IV Ins. Verification

Select Action: Quit// IB Site Parameters

The following screen will display.

IB Site Parameters Feb 01, 2011@16:22:02 Page: 1 of 5

Only authorized persons may edit this data.

\[1\] Copay Background Error Mg: IB ERROR

Copay Exemption Mailgroup: IB ERROR

Use Alerts for Exemption : NO

\[2\] Hold MT Bills w/Ins : YES X of Days Charges Held: 90

Suppress MT Ins Bulletin : NO

Means Test Mailgroup : IB MEANS TEST

Per Diem Start Date : 11/05/90

\[3\] Disapproval Mailgroup : MCCR - BUSINESS OFFICE

Cancellation Mailgroup : UB-82 CANCELL

Cancellation Remark : BILL CANCELLED IN BUSINESS OFFICE

\[4\] New Insurance Mailgroup : IB NEW INSURANCE

Unbilled Mailgroup : IB UNBILLED AMOUNTS

Auto Print Unbilled List : NO

\+ Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Next Screen//

369. At the Select Action: prompt, press the \<Enter\> key to accept the default of Next Screen until Section 14 is displayed.

IB Site Parameters Sep 16, 2011@14:32:21 Page: 3 of 5

Only authorized persons may edit this data.

\+

\[11\]Pay-To Providers : 1 defined, default - ANYTOWN TEST1 VAMC

\[12\] Non-MCCF Pay-To Providers: 2 defined, default – ANYTOWN CBOC

\[13\]Inpt Health Summary: INPATIENT HEALTH SUMMARY

Opt Health Summary : OUTPATIENT HEALTH SUMMARY

\[14\]HIPPA NCPDP Active Flag : Not Active

Drug Non Covered Recheck Period : 0 days(s)

Non Covered Reject Codes

: 70 Product/Service Not Covered

\[15\]Inpatient TP Active : YES

Outpatient TP Active: YES

Pharmacy TP Active : YES

Prosthetic TP Active: YES

\[16\] EDI/MRA Activated : BOTH EDI AND MRA

\+ Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Next Screen//

370. At the Select Action: prompt, enter EP=16.
371. The Enable Auto Reg EOB Processing?: prompt will be set to YES.

<u>WARNING</u>: This parameter should not be changed unless there is a compelling reason to stop the automatic processing of secondary/tertiary claims.

Select Action: Next Screen// ep=14 Edit Set

SITE CONTACT PHONE NUMBER: XXX-XXX-XXXX//

LIVE TRANSMIT 837 QUEUE: MCT//

TEST TRANSMIT 837 QUEUE: MCT//

AUTO TRANSMIT BILL FREQUENCY: 1//

HOURS TO TRANSMIT BILLS: 1130;1500;1700//

MAX X BILLS IN A BATCH: 10//

ONLY 1 INS CO PER CLAIM BATCH: YES//

DAYS TO WAIT TO PURGE MSGS: 15//

Allow MRA Processing?: YES//

Enable Automatic MRA Processing?: YES//

Enable Auto Reg EOB Processing?: YES//

## Printed Claims Rev Code Excl: 17 Activated Codes Defined

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*547 added Section 8, Printed Claims Rev Code Excl:, to the IB Site Parameters. When the Patch is installed, the following revenue codes, if active, will be pre-populated:

- 270-279
- 290-299

Users will be able to add and / or delete additional revenue codes. Revenue codes that are defined here will be used to screen out claims from the Printed Claims report.

IB Site Parameters Nov 03, 2015@10:43:20 Page: 2 of 5

Only authorized persons may edit this data.

\+

\[5\] Medical Center : ANYTOWN VAMC Default Division : ANYTOWN VAMR

MAS Service : BUSINESS OFFICE Billing Supervisor : REDACTED

\[6\] Initiator Authorize: YES Xfer Proc to Sched : YES

Ask HINQ in MCCR : YES Use Non-PTF Codes : YES

Multiple Form Types: YES Use OP CPT screen : YES

\[7\] UB-04 Print IDs : YES UB-04 Address Col :

CMS-1500 Print IDs : YES CMS-1500 Addr Col : 40

CMS-1500 Auto Prter: UB-04 Auto Prter :

EOB Auto Prter : MRA Auto Prter :

\[8\] Printed Claims Rev Code Excl: 17 Activated Codes Defined

\[9\] Default RX DX Cd : Z76.0 (ICD-10) Default ASC Rev Cd : 490

Default RX CPT Cd : J8499 Default RX Rev Cd : 250

\+ Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Next Screen//

The following prompts will display.

Excluded Revenue Codes Nov 03, 2015@11:05:06 Page: 1 of 1

X RCD DESCRIPTION

1\. 270 MED-SUR SUPPLIES

2\. 271 NON-STER SUPPLY

3\. 272 STERILE SUPPLY

4\. 273 TAKEHOME SUPPLY

5\. 274 PROSTH/ORTH DEV

6\. 275 PACE MAKER

7\. 276 INTRA OC LENS

8\. 277 O2/TAKEHOME

9\. 278 SUPPLY/IMPLANTS

10\. 279 SUPPLY/OTHER

11\. 290 MED EQUIP/DURAB

12\. 291 MED EQUIP/RENT

13\. 292 MED EQUIP/NEW

14\. 293 MED EQUIP/USED

15\. 294 MED EQUIP/SUPPLIES/DRUGS

16\. 299 MED EQUIP/OTHER

Enter ?? for more actions

AC Add Revenue Code DC Delete Revenue Code EX Exit

Select Item(s): Quit// ac Add Revenue Code

Revenue Code: 118 REHAB/PVT REHABILITATION

Revenue Code:

1.  Access the MCCR System Definition Menu.
372. At the Select MCCR System Definition Menu Option: prompt, enter Site for MCCR Site Parameter Display / Edit.
373. At the Select Action: prompt, Enter IB to access the IB Site Parameters.
374. At the Select Action: Next Screen// prompt, enter EP=8 to access Excluded Revenue Codes.
375. At the Select Item(s): Quit// prompt, enter AC for Add Revenue Code.
376. At the Revenue Code: prompt, enter a Revenue Code number.
377. At the Revenue Code: prompt, press the Enter key when done adding codes.

## Alternate Primary Payer ID Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*547 added Sections 17 and 18, Alt Prim Payer ID Typ-Medicare and Alt Prim Payer ID Typ-Commercial. Users can define qualifiers to be used to define alternative professional and / or institutional primary payer IDs by type in Insurance Company Entry / Edit. These ID types provide the ability to direct 837 transactions to different processing entities depending on the type of claim.

IB Site Parameters Nov 03, 2015@11:21:32 Page: 4 of 5

Only authorized persons may edit this data.

\+

\[16\] EDI/MRA Activated : BOTH EDI AND MRA

EDI Contact Phone : (XXX) XXX-XXXX

EDI 837 Live Transmit Queue : MCT

EDI 837 Test Transmit Queue : MCT

Auto-Txmt Bill Frequency : Every Day

Hours To Auto-Transmit : 1130;1500;1700

Max X Bills Per Batch : 10

Only Allow 1 Ins Co/Claim Batch?: NO

Last Auto-Txmt Run Date : 03/08/11

Days To Wait To Purge Msgs : 15

Allow MRA Processing? : YES

Enable Automatic MRA Processing?: YES

Enable Auto Reg EOB Processing? : YES

\[17\]Alt Prim Payer ID Typ-Medicare: 2 defined

\[18\]Alt Prim Payer ID Typ-Commercial: 2 defined

\+ Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Next Screen//

1.  Access the MCCR System Definition Menu.
2.  At the Select MCCR System Definition Menu Option: prompt, enter Site for MCCR Site Parameter Display/Edit.
3.  At the Select Action: prompt, Enter IB to access the IB Site Parameters.
4.  At the Select Action: Next Screen// prompt, enter EP=17 to access Alt Prim Payer Typ-Medicare.
5.  At the Select Item(s): Quit// prompt, enter AT for Add ID Type.
6.  At the Enter a Primary ID Type: prompt, enter a Free Text ID Type.
7.  At the Are you adding 'HOSPICE' as a new IB ALTERNATE PRIMARY ID TYPES (the 2nd)? No// prompt, enter YES.
8.  At the Enter a Primary ID Type: prompt, press the Enter key when done adding types.

Alt Primary Payer ID Types Nov 03, 2015@11:32:18 Page: 1 of 1

1 DME

Enter ?? for more actions

AT Add ID Type DT Delete ID Type EX Exit

Select Action: Quit//AT Add ID Type

Enter a Primary ID Type: HOSPICE

Are you adding 'HOSPICE' as

a new IB ALTERNATE PRIMARY ID TYPES (the 4TH)? No// y

## ASC X12N Health Care Claim Request for Additional Information (277RFAI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*547 added Section 20 to the IB Site Parameters. When the Patch is installed, the following 277RFAI parameters will be pre-populated:

- Days to store 277RFAI Transactions.
- Days to wait to purge entry on RFAI Management Worklist.

IB Site Parameters Nov 03, 2015@12:33:34 Page: 5 of 5

Only authorized persons may edit this data.

\+

\[19\]Are we using ClaimsManager? : NO

Is ClaimsManager working OK? : NO

ClaimsManager TCP/IP Address : XX.XXX.XX.XXX

ClaimsManager TCP/IP Ports : XXXXX

XXXXX

XXXXX

XXXXX

XXXXX

General Error MailGroup : IBCI GENERAL ERROR

Communication Error MailGroup: IBCI COMMUNICATION ERROR

MailMan Messages : PRIORITY

\[20\]Days to store 277RFAI Transactions: No Purge

Days to wait to purge entry on RFAI Management Worklist: 20

Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Quit// ep=20 Edit Set

PURGE DAYS 277 RFAI: ??

Enter the number of days (between 365 and 3000) to

retain 277 RFAI transactions in VistA.

A null entry (the default) indicates the transactions

will be stored forever.

PURGE DAYS 277 RFAI:

WORKLIST PURGE DAYS 277 RFAI: 20//

1.  Access the MCCR System Definition Menu.
378. At the Select MCCR System Definition Menu Option: prompt, enter Site for MCCR Site Parameter Display/Edit.
379. At the Select Action: prompt, Enter IB to access the IB Site Parameters.
380. At the Select Action: Quit// prompt, enter EP=20 to access the 277RFAI parameters.
381. At the PURGE DAYS 277 RFAI: prompt, press the Enter key to accept the default.
382. At the WORKLIST PURGE DAYS 277 RFAI: prompt, enter a Number that represents the number of days a 277 RFAI entry will remain on the RFAI Worklist before being automatically removed.

## New EDI Parameter for Dental Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*592 added a new parameter to the IB Site Parameters. The new Allow Dental Claim Processing field will be set to YES when the patch is installed.

If there is ever a need, this field can be reset to NO and the new Dental form J430D will no longer be available in Enter/Edit Billing Information and the AutoBiller will stop creating Dental claims.

IB Site Parameters Dec 14, 2017@12:02:08 Page: 4 of 5

Only authorized persons may edit this data.

\+

\[16\] EDI/MRA Activated : BOTH EDI AND MRA

EDI Contact Phone : (XXX) XXX-XXXX

EDI 837 Live Transmit Queue : MCT

EDI 837 Test Transmit Queue : MCT

Auto-Txmt Bill Frequency : Every Day

Hours To Auto-Transmit : 0900;1200;1700

Max X Bills Per Batch : 10

Only Allow 1 Ins Co/Claim Batch?: NO

Last Auto-Txmt Run Date : 12/13/17

Days To Wait To Purge Msgs : 15

Allow MRA Processing? : YES

Enable Automatic MRA Processing?: YES

Enable Auto Reg EOB Processing? : YES

Allow Dental Claim Processing? : YES

\[17\]Alt Prim Payer ID Typ-Medicare: 1 defined

\+ Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Next Screen//

## New EDI Parameter for 837 FHIR Transaction Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*641 added a new parameter to the IB Site Parameters. The new Allow 837 FHIR Trans Processing field will be set to NO when the patch is installed. A “Yes” indicates all 837 claims are to be submitted to FSC using the standard HL7 FHIR format. A “No” indicates all 837 claims are to be submitted to FSC using the proprietary Mailman format.

IB Site Parameters Dec 14, 2017@12:02:08 Page: 4 of 5

Only authorized persons may edit this data.

\+

\[16\] EDI/MRA Activated : BOTH EDI AND MRA

EDI Contact Phone : (XXX) XXX-XXXX

EDI 837 Live Transmit Queue : MCT

EDI 837 Test Transmit Queue : MCT

Auto-Txmt Bill Frequency : Every Day

Hours To Auto-Transmit : 0900;1200;1700

Max X Bills Per Batch : 10

Only Allow 1 Ins Co/Claim Batch?: NO

Last Auto-Txmt Run Date : 12/13/17

Days To Wait To Purge Msgs : 15

Allow MRA Processing? : YES

Enable Automatic MRA Processing?: YES

Enable Auto Reg EOB Processing? : YES

Allow Dental Claim Processing? : YES

Processing?: YES

\[17\]Alt Prim Payer ID Typ-Medicare: 1 defined

\+ Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Next Screen//

## CMN CPT Code Inclusion: CMN CPT Codes Included

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*608 added Section 21, CMN CPT Code Inclusion:, to the IB Site Parameters. When the Patch is installed, many CPT Codes will be pre-populated.

Users will be able to add and / or delete additional CPT codes. CPT codes that are defined here will be used to prompt “CMN Required?” on CMS-1500, screen 5.

IB Site Parameters Nov 03, 2015@12:33:34 Page: 5 of 5

Only authorized persons may edit this data.

\+

\[20\]Days to store 277RFAI Transactions: No Purge

Days to wait to purge entry on RFAI Management Worklist: 20

\[21\]CMN CPT Code Inclusion: 50 CMN CPT Codes Included

Enter ?? for more actions

EP Edit Set EX Exit

Select Action: Quit// ep=21 Edit Set

PURGE DAYS 277 RFAI: ??

Enter the number of days (between 365 and 3000) to

retain 277 RFAI transactions in VistA.

A null entry (the default) indicates the transactions

will be stored forever.

PURGE DAYS 277 RFAI:

WORKLIST PURGE DAYS 277 RFAI: 20//

The following prompts will display.

CMN CPT Inclusions May 03, 2018@11:05:06 Page: 1 of 4

<u>X CPT DESCRIPTION</u>

1\. B4102 EF ADULT FLUIDS AND ELECTRO

2\. B4103 EF PED FLUID AND ELECTROLYTE

3\. B4104 ADDITIVE FOR ENTERAL FORMULA

4\. B4149 EF BLENDERIZED FOODS

5\. B4150 EF COMPLET W/INTACT NUTRIENT

6\. B4152 EF CALORIE DENSE\>/=1.5KCAL

7\. B4153 EF HYDROLYZED/AMINO ACIDS

8\. B4154 EF SPEC METABOLIC NONINHERIT

9\. B4155 EF INCOMPLETE/MODULAR

10\. B4157 EF SPECIAL METABOLIC INHERIT

11\. B4158 EF PED COMPLETE INTACT NUT

12\. B4159 EF PED COMPLETE SOY BASED

13\. B4160 EF PED CALORIC DENSE\>/=0.7KC

14\. B4161 EF PED HYDROLYZED/AMINO ACID

15\. B4162 EF PED SPECMETABOLIC INHERIT

16\. B4164 PARENTERAL 50% DEXTROSE SOLU

Enter ?? for more actions

AC Add CPT Code DC Delete CPT Code

Select Item(s): Next Screen// ac Add CPT Code

CPT Code: B4172 PARENTERAL SOL AMINO ACID 5.

CPT Code:

1.  Access the MCCR System Definition Menu.
383. At the Select MCCR System Definition Menu Option: prompt, enter Site for MCCR Site Parameter Display/Edit.
384. At the Select Action: prompt, Enter IB to access the IB Site Parameters.
385. At the Select Action: Next Screen// prompt, enter EP=21 to access CMN CPT Code Inclusion.
386. At the Select Item(s): Quit// prompt, enter AC for Add CPT Code.
387. At the Revenue Code: prompt, enter a CPT Code number.
388. At the Revenue Code: prompt, press the Enter key when done adding codes.

# Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are a number of reports available to monitor and manage electronic claims. The EDI menu option can be accessed from the Billing Clerk's Menu.

## EDI Reports – Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TR reports provide the end-user with information to monitor and manage EDI claims still within the VA, that is, between the VAMC and the FSC in Austin, TX. The MM reports provide the end-user with information and feedback from parties external to the VA such as the clearinghouse and the various electronic payers.

<span id="_Toc100304294" class="anchor"></span>Figure : TR Report

![](ib-2-edi-user-guide/003.png)

## Most Frequently Used Menus / Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Claims Status Awaiting Resolution – Synonym CSA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this report?

Billing and Accounts Receivable (or Accounts Management) staff use CSA to review the most current status messages and to perform follow-up actions on the bills. Electronic status messages, which include information and rejection messages from the clearinghouse or the payers, are accessed using this option.

When is this option used?

This is an option that must be checked Daily to determine which claims have rejection or warning messages that were returned from the clearinghouse or from payers. The cause for rejections must be resolved. This option should be used in conjunction with supporting reports (e.g., R022, R0SS, R0SC).

The CSA report contains a Primary, Secondary and Tertiary sort capability and can be sorted by:

- A - Authorizing Biller
- B - Bill Number
- C - Current Balance
- S - Date of Service
- D - Division
- E - Error Code Text
- N - Number of Days Pending
- M - Patient Name
- P - Payer
- R - Review in Process
- L - SSN Last 4

Once the CSA screen list is displayed, users can select new sort criteria and re-sort the list without exiting the option.

Reports can be run showing rejections only (R), or both informational and rejection messages (B). Users most often run the CSA report to show rejections only so the users can focus on those claims that require corrective action.

These messages are automatically assigned a status of Not Reviewed and require users to review the messages and make corrections to update this status in IB. Users select a bill from the list to view the details and the entire message text. Messages are marked as reviewed or review in process. Users may document comments.

124. With Patch IB\*2.0\*320, changes were made to suppress the display of 2Q Claim Status Messages and duplicate claim status messages.

     Users can run this report by MCCF, Non-MCCF, or Both. The Non-MCCF report will display all claims with the rate types defined in the Non_MCCF Rate Types listing under section \[12\] Non-MCCF Pay-To Providers in the IB Site Parameters.

     With Patch IB\*2\*641, when users select Resubmit by Print, Retransmit a Bill or Print Bill actions, the following warning message will be displayed for the user:

     The user is about to Resubmit by Print, Retransmit or Print a bill that has an error or was rejected without making any changes to the claim. Please check before continuing.

     With Patch IB\*2.0\*650, the user will be prompted for a First Date Received and a Last Date Received date range when they select the (B)oth informational and rejects? sort criteria when running the report.

As messages are reviewed, the messages can be marked as follows:

- <u>Not Reviewed</u> – No action has been taken on a bill that has been returned from the clearinghouse/payer.
- <u>Review in Process</u> – While a claim is being reworked, the status can be changed to “Review in Process.”
- <u>Review Complete</u> – The error has been resolved and the message from this report will be cleared.

Actions such as Cancel Bill, Copy/Cancel Bill, TPJI and Print Bill are available to the user via this option and the user can make needed corrections and re-submit claims from within this option.

Other options available on the CSA include:

- <u>CSA-EDI History Display</u> – The EDI History display option shows all the status messages under the selected bill / message. This information is similar to information that can be viewed under the TPJI menu options.
- <u>CSA-Enter / Edit Comments</u> – The enter / edit comments option gives the user the ability to add a comment onto a bill (status message) in order to inform AR and billing why the issue hasn't been resolved or why the claim was printed to paper.
- <u>CSA-Resubmit by Print</u> – The Resubmit by Print action is used when the user reviews the status message or bill and determines the only way to correct the problem is to submit the claim on hard copy as it cannot pass the electronic edits. The user may “resubmit by print” to the payer instead of retransmitting electronically. If printed from this option, users will be asked to “review complete” the status message, which will automatically clear it from the report.
- <u>CSA-Retransmit a Bill</u> – Similar to the Resubmit by Print action, the Retransmit Bill is used when the user reviews the status message or bill and determines the reason for the rejection has been corrected elsewhere in the system and the claim just needs to be resent. The user may then retransmit to the payer.
- <u>CSA-Review Status</u> – A bill will continue to show up on the report until the bill is canceled / cloned, canceled, or the status is changed to Review Complete.

Users also have access to the option Multiple CSA Message Management from within the CSA list if the user holds the IB Message Management security key.

125. After Patch IB\*2\*547 is installed, the source of a claim status message will include the name of the clearinghouse when the clearinghouse is the source.

     With Patch IB\*2\*641, when users select Resubmit by Print, Retransmit a Bill, or Print Bill actions, the following warning message will be displayed for the user:

     The user is about to Resubmit by Print, Retransmit, or Print a bill that has an error or was rejected without making any changes to the claim. Please check before continuing.

### Multiple CSA Message Management – Synonym: MCS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

This option is designed to allow users to take action on CSA messages when a problem arises during the processing of electronic claims that causes a large volume of erroneous status messages to be sent to the site. This option performs tasks similar to the CSA option.

126. This option is locked by the IB Message Management security key.

When is this option used?

This option is used when there are pages of erroneous messages in CSA that were caused by a processing problem. Use this option to take a similar action (such as retransmission of the associated claims) on multiple claims at the same time.

The initial search for claims and claims status messages is done automatically when the option is selected. The initial search results in the display of all claims that are Not Cancelled and for which the review status is Not Reviewed or Review in Process.

127. If someone else is working on a claim in CSA, the claim will not display in MCS. Only one user can be in MCS at a time. The following message will be displayed: Sorry, another user is currently using the MCS option. Please try again later.

Once the initial list has been built, users may further refine their search or work from the default list.

128. The purpose of MCS is to select multiple claims and then apply the same action to all the selected claims. For example, users can enter a comment once and then apply the comment to 1-n claims.

Other actions available on the MCS include:

- <u>Message Search</u> – Allows the user to change the criteria upon which the list of claims will be built.
- <u>Change Review Status</u> – Same as CSA.
- <u>Cancel Claims</u> – Same as CSA.
- <u>Enter Comment</u> – Same as CSA.
- <u>Resubmit by Print</u> – Same as CSA.
- <u>Retransmit Bill</u> – Same as CSA.
- <u>Select / Deselect Claims</u> – Allows users to select the claims to apply an action.
129. When using the Resubmit by Print action, the claims selected will not be removed from the list of claims until the claims have actually been printed.

### Electronic Report Disposition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

This option allows the site to determine which clearinghouse generated electronic messages / reports are to be sent to the EDI mail group and which should be ignored.

When is this option used?

The default setting on this report will contain a disposition of “Mail Report to Mail Group”. It is up to the individual site’s supervisory staff to determine what reports should be ignored.

130. Further explanations of these reports are available in documents provided by the clearinghouse that are entitled <u>Claim Submitter Reports – Providers Reference Guide.</u>

The following reports should be reviewed when received. The reports contain information that cannot be translated into claim status messages therefore, this information is not available in CSA.

- R000 NETWORK NEWS

> Provides news on system problems, updates, and other pertinent information.

- RPT-02 FILE STATUS REPORT

> Provides an initial analysis of the file by displaying file status of accepted or rejected and a description of the status. It also indicates the total number of claims and the dollar value if the file contains valid claims.

- RPT-03 FILE SUMMARY REPORT

> Provides summarized information on the quantity of accepted, rejected, and pending claims, as well as the total number of claims received by the clearinghouse for each submitted file.

- RPT-08 PROVIDER MONTHLY SUMMARY

> Displays the number and dollar value of claims accepted and forwarded by the clearinghouse for the month. Monthly and Y-T-D Totals for both accepted and rejected claims are included as well as the provider’s top 25 errors for the month.

The following reports contain information that is also translated into status messages and displayed on CSA.

- RPT-04 FILE DETAIL SUMMARY REPORT

> Contains a detail summary of the file submitted for processing. It provides a file roll-up listing of all accepted, rejected, and pending claims contained in each file submitted to the clearinghouse. It also contains payer name/id and status of claim.

- RPT-04A AMENDED FILE DETAIL SUMMARY REPORT

> Contains a detailed listing of all claims for which the status was amended during the previous processing day. Claims statuses are amended when a pending claim is processed and / or a claim is reprocessed at the clearinghouse.

- RPT-05 BATCH & CLAIM LEVEL REJECTION REPORT

> Contains rejected batches and claims listed with detailed error explanations. In order to prevent “lost” claims, the RPT-05 report must be reviewed and worked after each file transmission.

- RPT-05A AMENDED BATCH & CLAIM LEVEL REJECTION REPORT

> Contains rejected batches and claims listed with detailed error explanations. In order to prevent “lost” claims, the RPT-05A report must be reviewed and worked after each file transmission.

- RPT-10 PROVIDER CLAIM STATUS

> This report contains information provided from payers who are receiving claims for adjudication from the clearinghouse. Not all payers who process claims through the clearinghouse system provide information for this Provider Claim Status Report and the amount/frequency of information produced will vary from payer to payer.

- RPT-11 SPECIAL HANDLING / UNPROCESSED CLAIMS REPORT

> This report contains information provided from payers who are receiving claims for adjudication from the clearinghouse. Not all payers who process claims through the clearinghouse system provide information for this Provider Claim Status Report and the amount / frequency of information produced will vary from payer to payer. The RPT-11 returns Unprocessed, Request for Additional Information, and Rejected statuses only.

### EDI Claim Status Report- Synonym: ECS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this report?

View electronic transmission status to assure claims move through the system in a timely fashion.

When is this option used?

It is recommended that initially this report be viewed daily as it provides transmission status of all claims that were transmitted to FSC. Once a comfort zone is established and everything is flowing correctly, this report may only need to be run weekly.

This report can be run by either claim detail or summary mode.

- Reports can be created based on:
- Specific Claim or Search Criteria
- Division
- Payer
- Transmission Date range
- EDI Status
- Reports can be sorted by:
- Transmission Date
- Payer
- EDI Status
- Current Balance
- Division
- Claim Number
- AR Status
- Age
- Possible EDI claim statuses include:
- Ready for Extract
- Pending Austin Receipt
- Received in Austin
- Accepted by Non-Payer
- Accepted Payer
- Error Condition
- Cancelled
- Corrected/Retransmitted
- Closed

## Additional Reports and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Ready for Extract Status Report – Synonym: REX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this report?

This report provides a list of claims held in a Ready for Extract status. These claims are held in a queue until batch processing occurs.

When is this option used?

Initially this option is used to assure claims are being transmitted at the times set in the MCCR Site Parameters. This option should by reviewed daily until there is a comfort level with the transmission timeframes and then less frequently based on local experience.

Claims that are trapped due to the EDI parameters being turned off can also be viewed. It is rare that EDI is turned off during processing. If this occurs, use EXT Extract Status Management to Cancel or Cancel / Clone/ Auth the trapped claims.

Choices to view are:

1.  All bills in Ready for Extract status.
2.  Bills trapped due to EDI parameter being turned off (If EDI is on, no bills will be trapped in extract).

### Transmit EDI Bills – Manual – Synonym: SEND

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

This option is used to by-pass the normal daily / nightly transmission queues if the need arises to get the claim to the payer quickly.

When is this option used?

There are occasions when there is a need to transmit a claim(s) immediately instead of waiting for the batching frequency as scheduled in the MCCR Site Parameter. This option will allow sending individual claim(s) or all claims in a ready for extract status.

Select one of the following:

- A - Transmit (A)LL bills in READY FOR EXTRACT status.
- S - Transmit only (S)ELECTED bills.

### EDI Return Message Management Menu – Synonym: MM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains the options needed to define the types of electronic reports from the clearinghouse that the site needs to see and defines the text that should / should not allow automatic review and filing for informational status messages. It also contains an option to purge old status messages, reports for maintaining the integrity of the return message subsystem and the option for reviewing electronically returned messages.

### EDI Message Text to Screen Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

This option controls what status and / or error messages users may wish to review using special text words and / or phrases. This will either require the message to be reviewed or will auto-file the message and flag it as not needing a review.

This option allows for the display of a list of words or phrases that, if found in the text of an informational status message, will either always require the message to be reviewed or will auto-file the message and flag it as not needing a review.

When is this option used?

Depending on what types of status messages users wish to review for follow-up on rejected claims and / or monitoring claims status, users may want to add or edit additional text as needed.

The words and phrases for “Requiring Review” and “Not Requiring Review” will initially populate as shown in the screen print below. This option is used to edit or add more words or phrases, as required, to manage and control the status messages.

### EDI Messages Not Reviewed Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this report?

This option allows for the display of all EDI return messages that were filed without needing a review based on the text entries in the message screen text file.

When is this option used?

The report can be run for a user-selected date range, based on the date the message was received at the site, and may be sorted by the message text that caused the message to not need a review or by the bill number. Users may want to use this option for analysis or review of all EDI messages that were not able to view initially.

### Electronic Error Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this report?

This report provides a tool for billing supervisors and staff to identify the “who, what, and where” of errors in the electronic billing process. This is a report that will allow the supervisory staff to review “frequently received” errors. This is an informational management tool requiring no actions on the part of the billing staff.

When is this option used?

This option can be used at any time by a supervisor or other management staff when needed to determine the reason for various errors (i.e., the same error being made by one or more of the billing staff). The report can be sorted by:

- A - AUTHORIZING BILLER
- B - BILLED AMOUNT
- E - EPISODE OF CARE
- P - PATIENT NAME
- S - PATIENT SSN
- Y - PAYER NAME
- C - ERROR CODE

### Return Messages Filing Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

After users have transmitted claims and have been received for EDI processing, a message will be sent to the mail groups shown in the set-up section of this manual.

When is this option used?

When a message is sent, the message is temporarily stored in the “EDI MESSAGES” file. Normally, these messages are in and out of this file in a matter of seconds. If, however, a problem is detected and a message cannot be filed in the appropriate file (s) for its message type, the message will remain in this temporary file.

There are two (2) statuses for messages in this file.

- Pending: The task to force a message to update the IB files has either not yet been created or has been created but has not yet begun to run.
- Updating: The task to force a message to update the IB files has started. It may or may not still be running. If the user tries to file a message with this status, a check is made to see if it is currently running. If it is, the message will not be re-tasked.

Any message may be viewed or printed. This does not affect the message in any way but looking at the message may help to indicate the next course of action needed.

There are two (2) actions available to get these messages out of the file.

- File Message: This action re-executes the tasked job to update the database with the contents of the message.
- Delete Message: This is a drastic action that should only be taken when it has been determined there is no other possible way to process a message. When a message is deleted using this action, a bulletin is sent to the IB EDI Mail Group with the text of the message and the name of the user who deleted the message. Users must hold the IB SUPERVISOR security key to perform this action.

### Status Message Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

This option allows users to print / purge electronically returned status messages that have been in a final review status for a user-selected number of days.

When is this option used?

There will be an accumulation of status messages in a final review status. This option will delete or purge status messages in one of the Final Review statuses prior to a selected date. Auto purging of messages can also be set in the IB Site Parameters.

This report can be sorted by:

- A - ALL STATUS MESSAGES
- S - SELECTED STATUS MESSAGES

Selected status message reports can be run showing:

- A - Auto Filed/No Review Only
- B - Bill Number
- S - Message Severity
- T - Specific Message Text

### Bills Awaiting Resubmission – Synonym: BAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this report?

This report lists all batches that have been resubmitted but which did not include all of the bills from the original batch. These are batches that have at least one bill still not resubmitted or canceled.

When is this option used?

When a batch is identified to have a claim in error, the batch may be re-submitted with the claim in error removed. This option will track and report specific bills in this category. The report can sort data by:

- B - BILL NUMBER
- L - LAST SENT DATE
- A - BILLED AMOUNT
- N - BATCH NUMBER (LAST SENT IN)

The report also indicates the “Bill Transmission Status.”

### EDI Messages Not Yet Filed –Synonym: MP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this report?

This report allows the user to select receipt, rejection, or both message types and a minimum number of days these messages have been in a PENDING or UPDATING status before the messages will be included on the report. The report will then list all messages in the file that meet these criteria.

When is this option used?

This is a status report that allows for review of messages not yet filed.

### Pending Batch Transmission Status Report – Synonym: PBT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this report?

This report shows the current transmission status of a batch's mail message. It also includes the mail message number; the first and last date / time the message was sent. Only batches in a pending transmission status will be on this report.

When is this option used?

This is another option to track the batch(s) of claims after authorizing and transmission to be sure all batches transmitted have been received in Austin. Users can omit both the station number prefix at the front of the batch number and the following zeroes and use only the final digits of the batch number for lookup.

### EDI Batches Pending Receipt– Synonym: PND

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this report?

This report lists all batches by batch number that have been in a PENDING status and have not yet received confirmation of receipt from Austin for more than one (1) day. The report includes individual claims if the users choose to include them.

The report includes:

- Batch Number
- Transmission Date
- Mail Message \#

Claims display the following:

- Claim Number
- Payer Sequence
- Balance Due
- EDI Status
- IB Status
- AR Status

EDI Batches Pending Austin Receipt After 1 Day Page: 2

Run Date: 01/07/2008@14:44:28

Batch X Transmission Date Mail Message X

------------------------------------------------------------------------------

Claim Seq Bal Due EDI Stat IB Status AR Status

KXXXXXX P 198.54 P PRNT/TX NEW BILL

KXXXXXX P 76.36 P PRNT/TX NEW BILL

KXXXXXX P 305.11 P PRNT/TX NEW BILL

KXXXXXX P 76.36 P PRNT/TX NEW BILL

KXXXXXX P 880.71 P PRNT/TX NEW BILL

XXXXXXXXXX 03/29/2006@21:05:33 1321

Claim Seq Bal Due EDI Stat IB Status AR Status

KXXXXXX P 76.36 P REQUEST MRA BILL INCOMPLETE

KXXXXXX P 73.01 P REQUEST MRA BILL INCOMPLETE

KXXXXXX P 4390.06 P REQUEST MRA BILL INCOMPLETE

KXXXXXX P 73.01 P REQUEST MRA BILL INCOMPLETE

Enter ENTER to continue or '^' to exit:

131. Members of the G.IB EDI mail group will receive an email message when there are batches of claims that have not received a confirmation message from Austin after 1 day.

*Subj: EDI BATCHES WAITING AUSTIN RECEIPT FOR OVER 1 DAY* \[X21387\]

06/19/04@19:02 6 lines

From: XXXXXXXXXXX,XXXX X In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

There are 30 EDI batch(es) still pending Austin receipt

for more than 1 day. Please investigate why they have not yet been confirmed

as being received by Austin.

*Since there were more than 10 batches found*, please run the

EDI BATCHES WAITING FOR AUSTIN RECEIPT OVER 1-DAY report to get a list of the

se batches.

Enter message action (in IN basket): Delete//

When is this option used?

Users may use this option to obtain Batch or Messages numbers when a problem arises or to monitor the status of batches recently transmitted. Batches should not be in a “Pending Austin Receipt” status for more than a day.

132. Contact IRM for assistance in finding out why a confirmation message has not been received from Austin.

     Before contacting IRM, note the Message Numbers for the batches that the user needs investigated. These numbers can be found in the PND option.

<u>WARNING</u>: If IRM needs assistance, log a REMEDY ticket or call the National Help Desk .

### View / Print EDI Bill Extract Data – Synonym: VPE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

This option displays the EDI extract data for a bill.

When is this option used?

This option is used only if there is a need to determine what data was transmitted for a specific bill. The detailed extract data will contain all the elements in the flat file that is transmitted to FSC. FSC, in turn, translates the data to a HIPAA-compliant format for transmission to the clearinghouse.

### Insurance Company EDI Parameter Report – Synonym: EPR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

This option will display the EDI Parameters of the Active Insurance Companies defined in Vista.

The contents of the following parameters will be included in this report:

- Insurance Company Name
- Street Address and City of Insurance Company
- Electronic Transmit?
- Institutional Electronic Bill ID
- Professional Electronic Bill ID
- HPID / OEID
- Electronic Type
- Type of Coverage
- Always Use main VAMC as Billing Provider

All Companies Insurance Company EDI Parameter Report Page: 1

Sorted By Ins Company Name Mar 02, 2015@10:30:28

Only Blank or 'PRNT' Bill ID's = NO

'\*' indicates the HPID/OEID failed validation checks

Electron Inst Prof HPID/ Electronic

Insurance Company Name Street Address City Transmit ID ID OEID Type Coverage Type

=================================================================================================INSURANCE COMPANY ONE REDACTEDANYTOWN,OH YES-L 8XXXX 8XXXX XXXXXXXXXX GROUP PLAN HEALTH INS…

INSURANCE COMPANY TWO REDACTED ANYTOWN,UT YES-L XXXXXXXXXX\* OTHER HEALTH INS…

When is this option used?

This option can be used whenever there is a need to confirm that the Insurance Company parameters are correctly defined to support the electronic transmission of claims. This option will be of value when the eClaims Plus patches are loaded and sites gain the ability to transmit secondary claims to the payers (electronic, end-to-end processing). Example: Sites can use this option to make sure the payers’ Electronic Bill IDs are defined.

### Test Claim EDI Transmission Report – Synonym: TCS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

The Claim Status Messages for claim(s) and batch(es) submitted via the RCB option as Test claims will not appear in CSA. No action will be required in response to these messages. For informational purposes, these messages will be available through the Test Claim EDI Transmission Report. This option can be used to investigate the status of test claims to see, for example, whether the transmission was accepted/rejected by FSC or accepted / rejected by the clearinghouse.

133. The messages in this option will be automatically purged after 60 days.

When is this option used?

This option can be used whenever a user needs to investigate the current status of a claim or batch of claims. The messages in this report will be like the messages in TPJI.

Test Claim EDI Transmission Report Page: 1

Selected Batches Mar 22, 2005@12:14:38

================================================================================

BatchX: XXXXXXXXXX

ClaimX: KXXXXXX IB,Patient7 (1500, Prof, Outpat)

--------------------------------------------------------------------------------

Transmission Information

03/17/2005@11:11:25 BchXXXXXX IB,Clerk2 CIGNA HEALTHCARE (S)

### Third Party Joint Inquiry – Synonym: TPJI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

This option provides a convenient location for both claim, AR, Insurance and EDI data related to a claim.

When is this option used?

This option is used by both Integrated Billing and Accounts Receivable personnel who require information about a claim. Both AR and IB users can also add comments to an MRA Request or non-MRA Request claim using this option.

The following actions are available from TPJI:

- BC - Bill Charges
- DX - Bill Diagnosis
- PR - Bill Procedures
- CB - Change Bill
- ED - EDI Status
- AR - Account Profile
- CM - Comment History
- IR - Insurance Reviews
- HS - Health Summary
- AL - Active List
- VI - Insurance Company
- VP - Policy
- AB - Annual Benefits
- EL - Patient Eligibility
134. Patch IB\*2\*377 included changes to allow the addition of and the viewing of MRA Request claim comments using TPJI. Comment History now pertains to MRA Request claims as well as regular claims. MRA Request claim comments are not stored as AR comments though.

     Patch IB\*2\*516 changed the lists of Active and Inactive claims to display the claim type of either Institutional or Professional in addition to Inpatient, Inpatient Humanitarian, Outpatient, or Outpatient Humanitarian. Patch IB\*2\*592 further changed the lists of Active and Inactive claims to display the additional claim type of Dental.

     Patch IB\*2\*516 also added the ability for users to view related claims for which the patient is responsible, when reviewing Claim Information for a selected claim.

     After Patch IB\*2\*547 is installed, the source of a claim status message will include the name of the clearinghouse when the clearinghouse is the source.

     After Patch IB\*2\*547 is installed, users will be able to view the comments that were added to an entry on the new RFAI Management Worklist in the comment section of the TPJI.

     After Patch IB\*2\*547 is installed, users will be able to view the complete and current textual description associated with the Claims Adjustment Reason Codes / Remittance Advice Remark Codes (CARC / RARC) received in an electronic EOB.

Patch IB\*2\*488 modified the way message storage errors (created when an EEOB or MRA is received and all the line items cannot be matched correctly) are displayed in TPJI. Internal MUMPS code will no longer be displayed to the users.

The Following types of errors will be displayed:

- Procedure Code mismatch
- Procedure Modifier mismatch
- Revenue Code mismatch
- Charge Amount mismatch
- Number of Units mismatch

Claim Information Nov 25, 2013@14:56:02 Page: 1 of 2

%K101XXX IB,PATIENT 123 IXXXX DOB: XX/XX/XX Subsc ID: XXXXXXXXX

Insurance Demographics Subscriber Demographics

Bill Payer: IB INSURANCE CO Group Number: GRP PLN XXXXX

Claim Address: REDACTED Group Name: STATE OF WY

ANYTOWN, WY XXXXXXXXX Subscriber ID: XXXXXXXXXX

Claim Phone: XXX/XXX-XXXX Employer: STATE OF WYO

Insured's Name: IB,PATIENT 123

Relationship: PATIENT

Claim Information

Bill Type: OUTPATIENT Charge Type: INSTITUTIONAL

Time Frame: ADMIT THRU DISCHARGE Service Dates: XX/XX/XX – XX/XX/XX

Rate Type: REIMBURSABLE INS. Orig Claim: 145.49

AR Status: ACTIVE Balance Due: 145.49

\+ \|% EEOB \| Enter ?? for more actions\|

BC Bill Charges AR Account Profile VI Insurance Company

DX Bill Diagnosis CM Comment History VP Policy

PR Bill Procedures IR Insurance Reviews AB Annual Benefits

CB Change Bill HS Health Summary EL Patient Eligibility

ED EDI Status AL Go to Active List EB Expand Benefits

RX ECME Information EX Exit

Select Action: Next Screen// BC Bill Charges

DO YOU WANT ALL EEOB DETAILS?: NO// Y

The type of mismatch error and the values that were in the outbound 837 transaction will be displayed along with the values that were received in the inbound 835 transaction.

Bill Charges Apr 14, 2014@16:27:18 Page: 7 of 8

KXXXXX IB,PATIENT MRA I4321 DOB: XX/XX/XX Subsc ID: XXXXXXXXXX

04/10/14 - 04/10/14 ADMIT THRU DISCHARGE Orig Amt: 0.00

\+

--------------------------------------------------------------------------------

VistA could not match all of the Line Level data received in the EEOB

(835 Record 40) to the claim in VistA.

Mismatched Procedure Code:

Payer reported the following was billed via the Claim (837):

Proc:71010 Mods:59 Rev Cd:324 Chg:227.40 Units:1

Payer reported adjudication via the EOB (835) as follows:

Proc:71015 Mods:59 Rev Cd:324 Chg:227.40 Units:1

Amt:100.00

---------------------------------------------------------------------

Service line adjustment (EEOB Record 41) has no matching service line

Allowed Amt: 114.80 Per Diem Amt: 0.00

---------------------------------------------------------------------

Service line adjustment (EEOB Record 45) has no matching service line

\+ \|% EEOB \| Enter ?? for more actions\|

PR Bill Procedures CM Comment History AB Annual Benefitslity

CI Go to Claim Screen IR Insurance Reviews EL Patient Eligibility

HS Health Summary EX Exit

ED EDI Status AL Go to Active List

VI Insurance Company

Select Action: Next Screen//

### Re-generate Unbilled Amounts Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

This option provides some basic information about billable events that have not yet been billed to a payer and dollar amounts associated with billable events in a specified time-frame.

When is this option used?

This option can be used to view the number of inpatient or outpatient care events and / or prescriptions that have not been billed and the dollar amounts attributed to the events.

Subj: UNBILLED AMOUNTS SUMMARY REPORT \[X197848\] 06/23/14@12:41 34 lines

From: INTEGRATED BILLING PACKAGE In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

SUMMARY UNBILLED AMOUNTS FOR ANYTOWN VAMC (999).

PERIOD: FROM 09/01/04 TO 09/30/06

DETAILED REPORT PRINTED TO '/dev/pts/5'

Inpatient Care:

Number of Unbilled Inpatient Admissions : 0

Number of MRA Unbilled Inpt Admissions : 2

Number of Inpt. Institutional Cases : 0

Average Inpt. Institutional Bill Amount : 15321.18

Number of Inpt. Professional Cases : 0

Average Inpt. Professional Bill Amount : 1036.36

Total Unbilled Inpatient Care : 0.00

Total MRA Unbilled Inpatient Care : 0.00

135. Patch IB\*2\*547 provided the ability for users to run this report by division (one or more) or not and to sort the report by division or by patient name in alphabetical order. If users do search by division, the Re-generate Unbilled Amount Summary will display the summary totals before the division data. The display of CPT codes and monetary amounts for outpatient claims has also been restored.

     Patch IB\*2\*608 provided the ability for users to run this report by MCCF, Non-MCCF (Outpatient Only), or Both. The Non-MCCF (Outpatient Only) report will display the type of claims based on the eligibility (CHAMPVA, Tricare, Employee, Ineligible and Sharing Agreement), the appointment type (Employee and Sharing Agreement) or the rate type (CHAMPVA Reimb. Ins., CHAMPVA, Tricare Reimb. Ins., Tricare, Interagency, Ineligible and Sharing Agreement).

     Patch IB\*2\*665 replaced hard-coded rate types added in Patch IB\*2\*608 with a table that can be found in Section 3.3 of this document.

Do you want to store Unbilled Amounts figures? NO//

Search by Division?? NO//Search by (M)CCF, (N)on-MCCF (Outpatient Only), or (B)oth? M// b Both

Start with DATE: 08/23/1966// t-1000 (FEB 07, 2013)

Go to DATE: 11/04/2015// (NOV 04, 2015)

Choose report type(s) to print:

1 - INPATIENT UNBILLED

2 - OUTPATIENT UNBILLED

3 - PRESCRIPTION UNBILLED

4 - ALL OF THE ABOVE

Select: (1-4): 4//

You have selected

4 - ALL OF THE ABOVE

Are you sure? NO// y YES

Print detail report with the Unbilled Amounts summary? NO// y

### Patient Billing Inquiry – Synonym: INQU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

This option provides some basic information about a particular claim. It is a simple inquiry option.

When is this option used?

This option can be used to view the following type of information related to a bill:

- Bill Status
- Rate Type
- Form Type (UB04/CMS-1500 and J430D)
- Visit Date(s)
- Charges
- AR Status
- Statement Dates
- Dates related to actions such as Entered, Cancelled, or Printed
- Bill Number copied from or to
- Patient, Mailing, and Insurance Company address

The data available varies based upon when the inquiry is made and what actions have been carried out regarding the claim

### Printed Claims Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

This option provides information about claims that are printed locally but which had the potential to be transmitted electronically. The report can be generated for either the Consolidated Patient Account Centers (CPACs) or the sites which process TRICARE claims.

When is this option used?

This report is used by billing personnel to monitor the printing of potentially transmittable claims and displays the following information:

- Biller
- Outpatient/Inpatient and Institutional/Professional
- Rate Type
- Plan Type
- Division
- Revenue Codes
- Insurance Company
136. The revenue codes that determine whether or not a printed claim will be included in this report are defined in the IB Site Parameters.

     Claims to the payer – Department of Labor and certain types of rate types and types of plans are not included in this report because these do not have the potential to be transmitted electronically.

### HCCH Payer ID Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

When the VHA sends a claim to the clearinghouse with no defined Primary Payer ID (EDI - Inst Payer Primary ID,EDI - Prof Payer Primary ID and / or EDI-Dental Payer Primary ID) and the clearinghouse has an electronic ID for the payer, the payer ID will be returned to the site. Or when VHA sends a claim to the clearing house with no defined Claim Office ID, VistA automatically takes the ID and populates the field in the Insurance Company file. This option provides information about the updates or attempted updates to the Insurance Company file.

137. If a value already exists in VistA for the Payer ID, no update will be made but the attempt will be reported.

When is this option used?

This report is used by billing personnel to monitor the automated updates or update attempts to the Insurance Company file when the 277STAT reports are received from the clearinghouse. The report provides the following data:

- Insurance Company Name
- Insurance Company Address
- Date
- EDI-Payer ID
- Claim Office ID
- Old Value
- New Value
- Update Made (Yes / No)

<span id="_Toc100304295" class="anchor"></span>Figure : Clearinghouse Payer ID Report

![](ib-2-edi-user-guide/004.png)

### Resubmission / Printing Claims No Changes CSA Report Synonym: RPN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What is the purpose of this option?

This option provides information about claims’ electronic status messages for the payers and which users attempt to use ‘Resubmit by Print”, “Retransmit Bill”, or “Print Bill” action from the CSA worklist.

When is this option used?

This option can be used at any time by a supervisor or other management staff to determine which users attempt to authorize electronic resubmission or print claims on the CSA worklist without making changes to any claim fields.

<span id="_Toc100304296" class="anchor"></span>Figure : Resubmission / Printing Claims No Changes CSA Report

![](ib-2-edi-user-guide/005.png)

# APPENDIX A – Batch Processing Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Batch Processing Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following example shows the user how to define batch processing for a payer:

1.  Under the IB Site Parameters, go to field \[15\] EDI/MRA Activated.
389. Edit fields as necessary (fields are highlighted in yellow for this example).

     Details on each field follow the screen example.

<u>WARNING</u>: When the MRA software was loaded (Patch IB\*2.0\*155), the EDI/MRA Activated field was removed from this screen. Only an IRM is able to access this field via FileMan. The reason for this is to prevent MRA from being activated before the FSC is ready to accept MRA transmissions from a particular site.

IB Site Parameters Aug 13, 2003@10:22:46 Page: 5 of 6

Only authorized persons may edit this data.

+----------------------------------------------------------------------

\[15\] EDI/MRA Activated : *EDI*

EDI Contact Phone :

EDI 837 Live Transmit Queue : *MCH*

EDI 837 Test Transmit Queue : *MCT*

Auto-Txmt Bill Frequency : *Every Day*

Hours To Auto-Transmit : *1300;1600*

Max X Bills Per Batch : *50*

Only Allow 1 Ins Co/Claim Batch?: *NO*

Last Auto-Txmt Run Date : *08/13/03*

Days To Wait To Purge Msgs : *120*EDI/MRA Activated: Controls whether EDI is available for the site.

Choose from:

- 0 - NOT EDI OR MRA
- 1 - EDI ONLY
- 2 - MRA ONLY
- 3 - BOTH EDI AND MRA

<u>WARNING</u>: This prompt is no longer accessible to anyone except an IRM.

IB Site Parameters May 27, 2004@14:14:24 Page: 5 of 6

Only authorized persons may edit this data.

\+

HMO NUMBER :

STATE INDUSTRIAL ACCIDENT PROV:

LOCATION NUMBER :

\[15\] EDI/MRA Activated : BOTH EDI AND MRA

EDI Contact Phone : XXX-XXX-XXXX

EDI 837 Live Transmit Queue : MCH

EDI 837 Test Transmit Queue : MCT

Auto-Txmt Bill Frequency : Every Day

Hours To Auto-Transmit : 1000;1400;2000

Max X Bills Per Batch : 10

Only Allow 1 Ins Co/Claim Batch?: NO

Last Auto-Txmt Run Date : 05/26/04

Days To Wait To Purge Msgs : 45

*Allow MRA Processing? : YESEnable Automatic MRA Processing?: YES*

Allow Dental Claim Processing? : YES

\+ Enter ?? for more actions

EP Edit Set EX Exit Action

- EDI Contact Phone: The phone number of the person at the site contact to whom EDI inquiries will be directed. The Pay-to Provider telephone number that is defined in Section 10 for each Pay-to Provider, will be printed on the UB04 and CMS-1500 form starting with Patch IB\*2.0\*400.
- EDI 837 Live Transmit Queue: The name of the Austin data queue that will receive claims to be processed via a live connection to the clearinghouse. These data are populated at the time of installation and would not normally be edited by the site.
- EDI 837 Test Transmit Queue: The name of the Austin data queue that will receive test claims. These data are populated at the time of installation and would not normally be edited by the site.
- Auto Txmt Bill Frequency: The desired number of days between each execution of the automated bill transmitter. For example, if the automated bill transmitter should run only once a week, this number would be 7. If the automated bill transmitter should run every night, then the number should be 1. If this is left blank or zero then the automated bill transmitter background job will never run.
- Hours To Transmit Bills: Contains the times of the day when EDI transmission of bills should occur. A maximum of 4 daily times daily may be entered and the times must be separated by a semi-colon. Times must be entered in 4-digit military format, without punctuation (HHMM;HHMM;HHMM;HHMM). If no times are entered, EDI transmission will take place as a normal part of the nightly job.
- Max \# Of Bills Per Batch: The maximum number of bills allowed in a single batch. With a new payer, it is suggested that the user begins with fairly small batches (10-20 claims).
- Only Allow 1 Ins Co / Claim Batch: Indicates whether or not the site wishes to limit batches to claims for a single insurance company.
- Last Auto-Txmt Run Date: The last date the auto transmit of bills was run at the site. These data are display only and cannot be edited.
- Days To Wait To Purge Msgs: This is the number of days after an electronic status message has been marked reviewed that the purge message option can delete it from the system.

# APPENDIX B - Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table provides definitions and explanations for terms and acronyms relevant to the content presented within this document. For additional terms and acronyms, the user can include references to other VA acronym and glossary repositories (e.g., VA Acronym Lookup and OIT Master Glossary).

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th>Acronym or Term</th>
<th>Definition / Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>277 Claim Status Messages (277STAT)</td>
<td>Electronic messages returned to the VAMC providing status information on a claim from the Financial Service Center (FSC) in Austin, Texas. These messages can originate at FSC, at the payer or at the clearinghouse.</td>
</tr>
<tr class="even">
<td>277 Request for additional information (277RFAI)</td>
<td><p>HIPAA Standard Electronic Transaction ASC X12 277, Health Care Claim Request for Additional Information</p>
<p>The HIPAA adopted standard for requesting additional information for health care claims submitted. Payers utilize this transaction for requesting additional information or missing information from providers on previously submitted health care claims.</p></td>
</tr>
<tr class="odd">
<td>835 Health Care Claim Payment / Advice (835)</td>
<td><p>The HIPAA adopted standard for electronic remittance advice to report the processing of all claim types (including retail pharmacy). The term “835” represents the data set that is sent from health plans to healthcare providers and contains detailed information about the processing of the claim. This includes payment information and reduction or rejection reasons.</p>
<p>All health plans are required to use the same explanation of benefit codes (adjustment reason codes) and adhere to very specific reporting requirements. The term “835” is used interchangeably with Electronic Remittance Advice (ERA) and Medicare Remittance Advice (MRA).</p></td>
</tr>
<tr class="even">
<td>837 Health Care Claim</td>
<td><p>The HIPAA adopted standard for electronic submission of hospital, outpatient, and dental claims. The term “837” represents the data set that is sent from healthcare providers to insurance companies (payers).</p>
<p>The 837 standard includes the data required for coordination of benefits and is used for primary and secondary payer claims submission. The term “837” is used interchangeably with electronic claim.</p></td>
</tr>
<tr class="odd">
<td>ASC X12</td>
<td>(Also known as ANSI ASC X12) – This is the official designation of the U.S. National <a href="http://en.wikipedia.org/wiki/Standards_organization">Standards Body</a> for the development and maintenance of <a href="http://en.wikipedia.org/wiki/Electronic_Data_Interchange">Electronic Data Interchange</a> (EDI) standards. The HIPAA transactions are based upon these standards.</td>
</tr>
<tr class="even">
<td>BC/BS</td>
<td>Blue Cross / Blue Shield</td>
</tr>
<tr class="odd">
<td>CARC</td>
<td>Claims Adjustment Reason Codes</td>
</tr>
<tr class="even">
<td>CBOC</td>
<td>Community Based Outpatient Clinic</td>
</tr>
<tr class="odd">
<td>CD2</td>
<td>Critical Decision Point #2</td>
</tr>
<tr class="even">
<td>Clearinghouse</td>
<td>A company that provides batch and real-time transaction processing services and connectivity to payers or providers. Transactions include insurance eligibility verification, claims submission processing, electronic remittance processing and payment posting for electronic claims.</td>
</tr>
<tr class="odd">
<td>CLIA</td>
<td>Clinical Laboratory Improvement Amendment</td>
</tr>
<tr class="even">
<td>CLON</td>
<td>Copy and Cancel</td>
</tr>
<tr class="odd">
<td>CMOP</td>
<td>Centralized Mail Out Pharmacy</td>
</tr>
<tr class="even">
<td>COB</td>
<td>Coordination of Benefits</td>
</tr>
<tr class="odd">
<td>CPAC</td>
<td>Consolidated Patient Account Center</td>
</tr>
<tr class="even">
<td>CSA</td>
<td>See Claims Status Awaiting Resolution</td>
</tr>
<tr class="odd">
<td>eClaim</td>
<td>A claim that is submitted electronically from the VA.</td>
</tr>
<tr class="even">
<td>EDI</td>
<td>See Electronic Data Interchange</td>
</tr>
<tr class="odd">
<td>EEOB</td>
<td>Electronic Explanation of Benefits</td>
</tr>
<tr class="even">
<td>eIV</td>
<td>Electronic Insurance Verification. It is also the Insurance buffer entry source name in the Insurance Buffer List to signal entry processing by Electronic Insurance Verification.</td>
</tr>
<tr class="odd">
<td>Electronic Data Interchange (EDI)</td>
<td>EDI is the process of transacting business electronically. It includes submitting claims electronically (paperless claims processing), as well as electronic funds transfer and electronic inquiry for claim status and patient eligibility.</td>
</tr>
<tr class="even">
<td>Electronic Payer</td>
<td>A payer that has an electronic connection with the clearinghouse.</td>
</tr>
<tr class="odd">
<td>EOB</td>
<td>An Explanation of Benefits (EOB) reports the disposition of an individual claim. Many EOBs may be contained within a single 835 ERA file.</td>
</tr>
<tr class="even">
<td>ePayer</td>
<td>Payer that accepts electronic claim from the clearinghouse pays electronically. See Payer.</td>
</tr>
<tr class="odd">
<td>ERA</td>
<td>Electronic Remittance Advice (ERA)</td>
</tr>
<tr class="even">
<td>Facility Fed Tax ID #</td>
<td>This is the number that will be the default for all providers for the ID type at the facility if the payer does not have specific requirements.</td>
</tr>
<tr class="odd">
<td>Fiscal Intermediary</td>
<td><p>A fiscal intermediary performs services on behalf of healthcare payers. These services include claim adjudication, reimbursement, and collections.</p>
<p>Trailblazer is an example of a fiscal intermediary that acts on behalf of Medicare. Trailblazer receives claims from the VA in the form of an 837 file and then adjudicates the claims to create an MRA/EOB 835 file.</p></td>
</tr>
<tr class="even">
<td>Form Types</td>
<td>The UB-04, CMS-1500 or J430D billing form on which services will be billed.</td>
</tr>
<tr class="odd">
<td>FSC</td>
<td><p>The VA Financial Services Center in Austin. The Financial Service Center translates claims into an industry-standard format (HIPAA 837) and forwards claims to the clearinghouse.</p>
<p>The FSC is the single point for the exchange of data between VistA and the clearinghouse.</p></td>
</tr>
<tr class="even">
<td>HCS</td>
<td>Health Care System</td>
</tr>
<tr class="odd">
<td>Healthcare Company</td>
<td>See Payer</td>
</tr>
<tr class="even">
<td>Health Insurance Portability and Accountability Act (HIPAA)</td>
<td><p>In 1996 Congress passed into law the Health Insurance Portability and Accountability Act (HIPAA). This Act is comprised of two major legislative actions: Health Insurance Reform and Administrative Simplification.</p>
<p>The Administrative Simplification provisions of HIPAA direct the federal government to adopt national electronic standards for automated transfer of certain healthcare data between healthcare payers, plans, and providers. This will enable the entire healthcare industry to communicate electronic data using a single set of standards thus eliminating all non-standard formats currently in use.</p>
<p>Once these standards are in place, a healthcare provider will be able to submit a standard transaction for eligibility, authorization, referrals, claims, or attachments containing the same standard data content to any health plan. This will "simplify" many clinical, billing, and other financial applications and reduce costs.</p></td>
</tr>
<tr class="odd">
<td>HPID</td>
<td>Health Plan Identifier</td>
</tr>
<tr class="even">
<td>IIU</td>
<td>Interfacility Insurance Update. This term refers to the automated push of active, verified insurance information in real time from the VistA instance used to verify to the account to other VistA instances where the Veteran has received care.</td>
</tr>
<tr class="odd">
<td>Insurance Company</td>
<td>See Payer</td>
</tr>
<tr class="even">
<td>Legacy IDs</td>
<td>This term refers to those payer-provided or users own IDs (individual and organizational) which will eventually be made obsolete by the use of National Provider Identifiers.</td>
</tr>
<tr class="odd">
<td>M&amp;ROC</td>
<td>Medical and Regional Office Center</td>
</tr>
<tr class="even">
<td>MCCF</td>
<td>Medical Care Collections Fund</td>
</tr>
<tr class="odd">
<td>MORC</td>
<td>Mobile Outreach Clinic</td>
</tr>
<tr class="even">
<td>MRA</td>
<td>Medicare Remittance Advice</td>
</tr>
<tr class="odd">
<td>MRW</td>
<td>Management Worklist</td>
</tr>
<tr class="even">
<td>NPI</td>
<td>National Provider Identifier - A standard, unique health identifier for healthcare providers, both individuals and organizations.</td>
</tr>
<tr class="odd">
<td>Non-VA Facility</td>
<td>Any facility that provides services to a VA patient and subsequently bills the VA for those services.</td>
</tr>
<tr class="even">
<td>Non-VA Provider</td>
<td>Any individual provider who provides services to a VA patient and subsequently bills the VA for these services.</td>
</tr>
<tr class="odd">
<td>NUCC</td>
<td>National Uniform Claims Committee</td>
</tr>
<tr class="even">
<td>OB</td>
<td>State License Number</td>
</tr>
<tr class="odd">
<td>OC</td>
<td>Outpatient Clinic (Independent)</td>
</tr>
<tr class="even">
<td>OEID</td>
<td>Other Entity Identifier</td>
</tr>
<tr class="odd">
<td>OIT</td>
<td>Office of Information and Technology</td>
</tr>
<tr class="even">
<td>OPC</td>
<td>Outpatient Clinic</td>
</tr>
<tr class="odd">
<td>Parent</td>
<td>The top facility in a hierarchical domain.</td>
</tr>
<tr class="even">
<td>Payer</td>
<td>The insured’s insurance company. Other terms that are used to denote Payer include ePayer, insurance company, healthcare company, etc.</td>
</tr>
<tr class="odd">
<td>Payer Code</td>
<td>A code used for enrollment that uniquely identifies the payer.</td>
</tr>
<tr class="even">
<td>Payer List</td>
<td>List of payers that consist of the payer category, claim type, payer code, and payer name.</td>
</tr>
<tr class="odd">
<td>PHARM</td>
<td>Pharmacy</td>
</tr>
<tr class="even">
<td>POA</td>
<td>Present on Admission</td>
</tr>
<tr class="odd">
<td>Provider</td>
<td>Provider of healthcare services</td>
</tr>
<tr class="even">
<td>Provider ID</td>
<td>A provider ID can represent a facility or an individual Physician / Provider.</td>
</tr>
<tr class="odd">
<td>RARC</td>
<td>Remittance Advice Remark Codes</td>
</tr>
<tr class="even">
<td>RO-OC</td>
<td>Regional Office – Outpatient Clinic</td>
</tr>
<tr class="odd">
<td>SSN</td>
<td>Social Security Number</td>
</tr>
<tr class="even">
<td>TAS</td>
<td>Transaction Applications Suite (TAS)</td>
</tr>
<tr class="odd">
<td>Taxonomy Code</td>
<td><p>The Health Care Provider Taxonomy code set is a collection of unique alphanumeric codes, ten characters in length. The code set is structured into three distinct "Levels" including Provider Type, Classification, and Area of Specialization.</p>
<p>The Health Care Provider Taxonomy code set allows a single provider (individual, group, or institution) to identify their specialty category.</p></td>
</tr>
<tr class="even">
<td>UPIN</td>
<td>Unique Provider Identification Number</td>
</tr>
<tr class="odd">
<td>URL</td>
<td>Uniform Resource Locator</td>
</tr>
<tr class="even">
<td>VAMC</td>
<td>Veterans Affairs Medical Center</td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="even">
<td>VIP</td>
<td>Veteran-Focused Integration Process</td>
</tr>
<tr class="odd">
<td>VISN</td>
<td>Veterans Integrated Service Network</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information System and Technology Architecture</td>
</tr>
</tbody>
</table>