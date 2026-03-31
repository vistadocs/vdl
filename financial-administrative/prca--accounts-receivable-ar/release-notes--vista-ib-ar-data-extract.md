---
title: VistA IB/AR Data Extract Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: plain
doc_subject: VistA IB/AR Data Extract
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: 
  - 354
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - prca
  - patch
  - blockquote
  - table
  - contents
  - test
  - extract
  - date
  - accounts
  - class
page_count: 0
word_count: 1774
section_count: 5
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/VistA_IB_AR_Data_Extract_Release_Notes.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/VistA_IB_AR_Data_Extract_Release_Notes.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

![](vista-ib-ar-data-extract-release-notes/001.png)

VISTA IB/AR DATA EXTRACTPHASE II

####### RELEASE NOTES

IB\*2.0\*301

IB\*2.0\*305

PRCA\*4.5\*228

PRCA\*4.5\*232

PRCA\*4.5\*234

PRCA\*4.5\*240

PRCA\*4.5\*243

August 2006

VistA  
Health Systems Design & Development

*  
(This page included for two-sided printing.)*Table of Contents

*  
(This page included for two-sided printing.)*

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
- [Integrated Billing Patch IB\2.0\301](#integrated-billing-patch-ib20301)
- [Accounts Receivable Patch PRCA\4.5\228/234/240](#accounts-receivable-patch-prca45228234240)
- [Integrated Billing Patch IB\2\305](#integrated-billing-patch-ib2305)
- [Accounts Receivable Patch PRCA\4.5\232/243](#accounts-receivable-patch-prca45232243)
  - [New Extracts](#new-extracts)
  - [Changes to Existing Extracts](#changes-to-existing-extracts)
  - [New Bill Status](#new-bill-status)
  - [Test Accounts](#test-accounts)
In September of 2004, patches PRCA\*4.5\*201 and IB\*2.0\*233 implemented the design requirements for a software development project where the Veterans Health Administration (VHA) established a new set of revenue metrics for use in monitoring the performance of the VHA revenue cycle at all VHA facilities.
The desired metrics are industry-standard measures that are commonly used in other public and private health care institutions. An existing VHA centralized data warehouse, Allocation Resource Center (ARC), is used to calculate these metrics and provides results via a web-based performance metric site. The ARC is updated on a monthly basis.
VHA's Chief Business Office (CBO) has identified the daily collection of this data as a high priority to support the metrics development process. CBO needs the daily collection of data to populate the centralized data warehouse with billing and collections transactions from each VHA facility. The calculated metrics will be viewable to field and headquarters staff through an existing website. An automated daily VistA extract provides more timely and accurate data to this centralized data warehouse.
In August of 2005, VistA IB/AR Data Extract Phase II, Part 1 software, patches IB\*2.0\*301 and PRCA\*4.5\*228 was released, expanding the data collected.
Now, VistA IB/AR Data Extract Phase II, Part 2 software, patches PRCA\*4.5\*232, PRCA\*4.5\*243, and IB\*2.0\*305, is being released. This software will transmit additional fields on an existing daily extract and 3 new monthly extracts.
*  
(This page included for two-sided printing.)*

# Integrated Billing Patch IB\*2.0\*301

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2.0\*301 has been released in conjunction with Accounts Receivable (AR) patch PRCA\*4.5\*228 to support the updated functionality for the VistA IB/AR Data Extract, which is sent to the Allocation Resource Center (ARC). This patch corrects a problem with the VistA IB/AR (Integrated Billing/Accounts Receivable) Data Extract for CBO. Only bills that have been previously authorized should be included with the extract. However, during the internal testing of PRCA\*4.5\*228, VistA IB/AR Data Extract Phase II, Part 1, it was discovered that bills which were cancelled but not authorized were also being included. This will no longer happen after this fix.

# Accounts Receivable Patch PRCA\*4.5\*228/234/240

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PRCA\*4.5\*228 added additional fields to the existing transmission to CBO and was a portion of

Part 1 of Phase 2 of the implementation. The following is a list of the fields added to the extract with this patch:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>New Extract</strong></th>
<th><strong>Fields/Data Elements Being Extracted</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Bill/Claims File (#399)</td>
<td><ul>
<li><p>MRA REQUESTED DATE (#7)</p></li>
<li><p>LAST ELECTRONIC EXTRACT DATE (#21)</p></li>
<li><p>PRINTED VIA EDI? (#26)</p></li>
<li><p>FORCE CLAIM TO PRINT (#27)</p></li>
<li><p>CLAIM MRA STATUS (#24)</p></li>
<li><p>MRA RECORDED DATE (#22)</p></li>
<li><p>DATE BILL CANCELLED (#17)</p></li>
<li><p>FORM TYPE (#.19)</p></li>
<li><p>GROUP NUMBER (from file 355.3-GROUP INSURANCE PLAN,#.04)</p></li>
<li><p>PAYER (from file 365.12-PAYER, #.01)</p></li>
<li><p>NATIONAL VA ID NUMBER (from file 365.12-PAYER, #.02)</p></li>
<li><p>DRG (computed from PTF field in 399 (.08) and DRG file (#45),field #9)</p></li>
<li><p>MRA REJECTIONS (YES/NO)</p></li>
<li><p>ECME Number (#460 -Numerical portion of data only)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Bill/Claims Prosthetics File (#362.5) Line</td>
<td><ul>
<li><p>BILL NUMBER (#.02)</p></li>
<li><p>ITEM (#.03)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Integrated Billing Action File (#350) Line</td>
<td><ul>
<li><p>DATE OF TREATMENT (#.17)</p></li>
<li><p>ACTUAL REFILL DATE OF PRESCRIPTION</p></li>
<li><p>DIVISION WHERE CARE WAS RENDERED</p></li>
</ul></td>
</tr>
<tr class="even">
<td>AR Transactions (#433) Line</td>
<td><ul>
<li><p>MEDICARE CONT. ADJUSTMENT (#131)</p></li>
<li><p>MEDICARE UNREIMBURSABLE (#132)</p></li>
<li><p>REFUNDED AMOUNT (#79.18)</p></li>
<li><p>REFUNDED DATE (#79.19)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>New Person (#200)</td>
<td><ul>
<li><p>SPECIALITY (#747.111)</p></li>
<li><p>SERVICE/SECTION (#29)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>AR Batch Payment (#344) Line</td>
<td><ul>
<li><p>FACILITY NUMBER (Calculated by AR function $$SITE^RCMSITE() )</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Patient (#2)</td>
<td><ul>
<li><p>DATE OF DEATH (#.351)</p></li>
<li><p>MARITAL STATUS (#.05)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Annual Means Test (#408.31)</td>
<td><ul>
<li><p>CURRENT MEANS TEST</p></li>
</ul>
<ul>
<li><p>DATE (#.01)</p></li>
<li><p>STATUS (#.03)</p></li>
<li><p>CURRENT INCOME (#.04)</p></li>
</ul>
<blockquote>
<p>Note: The field numbers for CURRENT COPAY TEST, LTC CO-PAY TEST, and LTC</p>
<p>CO-PAY EXEMPTION TEST are the same as for CURRENT MEANS TEST above)</p>
<p>o CURRENT COPAY TEST</p>
<p>DATE</p>
<p>STATUS</p>
<p>CURRENT INCOME</p>
<p>o LTC CO-PAY TEST</p>
<p>DATE</p>
<p>STATUS</p>
<p>CURRENT INCOME</p>
<p>o LTC CO-PAY EXEMPTION TEST</p>
<p>DATE</p>
<p>STATUS</p>
<p>CURRENT INCOME</p>
</blockquote></td>
</tr>
</tbody>
</table>

Other Changes Included in Patch PRCA\*4.5\*228, PRCA\*4.5\*234 and PRCA\*4.5\*240

- Functionality has been added to screen out test patients from the information being transmitted in the data extracts.
- The header of the AR Batch Payment (#344) line has been modified to display the number of rows transmitted.
- This patch adds a new batch type to the BATCH TYPE field (#.04) of the AR DATA QUEUE file (# 348.4). The CBO FISCAL YR 2005 transmissions were sent with a batch type of "E".
- This patch also corrects problems with the first release of this software (PRCA\*4.5\*201). These issues include Remedy Ticket \#HD85294, a flaw which stopped some of the CPT codes from being transmitted, the transmission of internal numbers rather than external values for procedures in line 399.0402, flaws in the original patch that prevented all the transactions from 433 (AR Transaction file) from transmitting, and the use of direct global references.
- Patch PRCA\*4.5\*234 changed the transmission created by PRCA\*4.5\*228 regarding the historicals to send only 1 month of data at a time instead of 3 months.
- Patch PRCA\*4.5\*240 provided 2 fixes related to issues arising out of Phase I of VistA IB/AR Data Extract project. One related to having the software check to see if the batch was closed prior to adding any bills or transactions. The other fix corrected an issue with the refill date for pharmacy prescriptions to have the software access the correct subfield, RELEASE DATE/TIME (#17) in the REFILL subfile (#52) of the PRESCIPTION file (#52).

# Integrated Billing Patch IB\*2\*305

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch IB\*2\*305 is being released in conjunction with Accounts Receivable (AR) patch PRCA\*4.5\*232 to support the updated functionality for the VistA IB/AR Data Extract, which is sent to the Allocation Resource Center (ARC). It provides new entry points which return data to the AR system from IB. In addition, new entry points have been added to collect data returned from AR.

# Accounts Receivable Patch PRCA\*4.5\*232/243

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches PRCA\*4.5\*232 and PRCA\*4.5\*243 are being released in conjunction with patch IB\*2\*305. This patch adds three new extracts. In addition, several additional fields have been added to the existing extract. These new extracts are sent once a month on the first of the month, and include data from the preceding month.

## New Extracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>New Extract</strong></th>
<th><strong>Fields/Data Elements Being Extracted</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IB Patient CoPay Account from File #354.7</td>
<td><ul>
<li><blockquote>
<p>SOCIAL SECURITY NUMBER (SSN)</p>
</blockquote></li>
<li><blockquote>
<p>MONTH/YEAR</p>
</blockquote></li>
<li><blockquote>
<p>TOTAL AMOUNT BILLED</p>
</blockquote></li>
<li><blockquote>
<p>CAP REACHED</p>
</blockquote></li>
<li><blockquote>
<p>TOTAL AMOUNT NON-BILLABLE</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>Pre-Registration Information from the Percentage of Patients Pre-Registered Report</td>
<td><ul>
<li><blockquote>
<p>NUMBER OF UNIQUE PATIENTS TREATED</p>
</blockquote></li>
<li><blockquote>
<p>NUMBER OF UNIQUE PATIENTS PRE-REGISTERED WITHIN</p>
</blockquote></li>
<li><blockquote>
<p>PRE-REGISTRATION TIME FRAME</p>
</blockquote></li>
<li><blockquote>
<p>PERCENT PRE-REGISTERED</p>
</blockquote></li>
<li><blockquote>
<p>NUMBER OF UNIQUE OUTPATIENTS PRE-REGISTERED PAST</p>
</blockquote></li>
<li><blockquote>
<p>PRE-REGISTRATION TIME FRAME</p>
</blockquote></li>
<li><blockquote>
<p>NUMBER OF UNIQUE OUTPATIENTS NEVER PRE-REGISTERED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>Buffer File Information from the IB Insurance Buffer Activity Report</td>
<td><ul>
<li><blockquote>
<p>AVERAGE NUMBER OF DAYS IT TAKES TO PROCESS A POLICY IN THE BUFFER FILE</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

## Changes to Existing Extracts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Extract     | Change                                                                                                                               |
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------|
| e-MRA Reporting | The Total Days Site Not Responsible Due to e-MRA Processing will be added, and included on the 399 line of the extract.                  |
| Offset Amount   | This data is pulled from the BILL/CLAIMS file (#399), OFFSET AMOUNT field (#202); and will be added to the 399 line of the transmission. |

## New Bill Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, bills with a status of Open, Active, or Suspended are transmitted. With this patch, bills with a current status of NEW BILL will also be transmitted.

## Test Accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As with patch PRCA\*4.5\*228, if patch PRCA\*4.5\*232 is installed in a test account, data will begin to be accumulated and the extracts will be setup to run in the test account's TaskMan and sent to the ARC. The ability to turn this functionality off in test accounts ONLY is provided with patch PRCA\*4.5\*232. The function can be turned off and on, as needed, for testing purposes. Turning this functionality OFF, prevents the capture of data into the AR DATA QUEUE file (#348.4) and the transmission of batches. Batches created from a test account are transmitted via FTP (File Transfer Protocol) to a separate account at the ARC.