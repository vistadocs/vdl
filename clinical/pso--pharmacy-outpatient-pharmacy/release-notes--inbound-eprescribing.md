---
consolidated_title: "inbound eprescribing release notes"
app_code: PSO
doc_type: RN
master_source: "PSO*7*617 Inbound ePrescribing Release Notes"
master_pub_date: revision_count: 0
consolidated_from: 2 versions
prior_versions:
  - "PSO*7*635 Inbound ePrescribing Release Notes"
---

Outpatient Pharmacy

Inbound ePrescribing (IEP)CS Electronic Prescriptions (eRx) 5.0VistA Patch \# PSO\*7.0\*617

Release Notes

![](pso-7-617-inbound-eprescribing-release-notes/001.png)

November 2021Version 1.0

Office of Information and Technology (OI&T)

*(This page included for two-sided copying.)*Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Related Patches](#related-patches)
  - [Summary of Changes](#summary-of-changes)
- [Product Documentation](#product-documentation)
The Inbound Electronic Prescribing (eRx) v5.0 enhancements include updates to the current eRx functionality to allow the VA to receive and dispense electronic prescriptions for controlled substance medications. Up until now the eRx Holding Queue restricted the selection of a controlled substance VA dispense drug for any incoming electronic prescription due to the fact that the functionality was not 100% compliant with the DEA requirements (21 CFR Part 1311 Subpart C) for receiving, processing and dispensing controlled substance electronic prescriptions. This project addresses all the DEA requirements and enables the eRx Holding Queue to process incoming electronic prescriptions for controlled substance medications.

## Related Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches are being released to support this project:

APPLICATION/VERSION PATCH

----------------------------------------------------------

OUTPATIENT PHARMACY (PSO) V. 7.0 PSO\*7\*617

CONTROLLED SUBSTANCE (PSD) V. 3.0 PSD\*3\*89

## Summary of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a list of the changes made to the existing Outpatient Pharmacy eRx functionality. Please, refer to the patch description for more detailed information.

1.  New HOLD, REJECT and REMOVE have ben added
2.  The CMOP Controlled Substance Rx Dispense Report \[PSO CMOP CS RX DISPENSE REPORT\] was modified to identify prescriptions that came through eRx
3.  The Released and Unreleased Prescription Report \[PSO RELEASE REPORT\] was modified to identify prescriptions that came through eRx
4.  The Complete Orders from eRx \[PSO ERX FINISH\] option was modified to allow the processing of CS eRx prescriptions:
    1.  A new filter was added to allow the selection of CS, non-CS or Both types of records to display on the eRx Holding Queue.
    2.  When CS or Both is selected a new filter was added to allow the user to select the CS Schedule of the records to display on the eRx Holding Queue.
    3.  CS eRx records will be identified in the eRx Holding Queue by a closing square bracked (\]) displayed right after the sequence \# of the eRx record. Also, once the user selects a CS eRx record it will display “EPCS DEA VALIDATED” in the header.
    4.  The SORT ENTRIES action was modified to allow the user to group CS and non-CS prescriptions after the sort field is selected.
    5.  DO NOT FIILL records will be clearly identified in the header section of the eRx Holding Queue.
    6.  The prescriber DEA# will be displayed along with the other prescriber information.
    7.  For CS eRx records the DEA Schedule will be displayed right after the eRx and VistA Drug names.
    8.  A patient must have at least the ZIP CODE in order to have a CS eRx prescription processed in the eRx Holding Queue.
    9.  The VistA Prescriber selected for a CS eRx record must have a valid DEA# on file and be authorized to write a prescription for the CS Schedule of the VistA Drug selected. Furthermore, the DEA# must match the incoming DEA# otherwise the prescriber cannot be selected for the eRx record.
    10. If the VistA drug selected for the eRx record is marked as a DETOX drug the VistA prescriber must have a valid DETOX# on file.
    11. A new Audit Log was introduced in the eRx Holding Queue to display all changes made to the any eRx records (CS or non-CS) for the following fields: PATIENT, PROVIDER, DRUG, QTY, DAYS SUPPLY, \# OF REFILLS, SIG, PROVIDER COMMENTS and PATIENT INSTRUCTIONS.
    12. When the user select the eRx Change Request (EC) action for a CS eRx record it will limit the to select P (Prior Authorization Required) or U (Prescriber Authorization) for the RX change message request code.
5.  The Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] and Complete Orders from OERR \[PSO LMOE FINISH\] options were modified to allow the processing of CS eRx prescriptions:
    1.  A new hidden action called ‘Un Accept eRx’ (UA) was added for Pending Orders to allow the user to removed it from the Pending Queue and place the eRx back in the eRx Holding Queue to be re-processed.
    2.  When viewing a digitally signed eRx pending order the first line of the scrollable area will display the text "Processing Digitally Signed eRx Order" in reverse video.
    3.  For digitally signed eRx pending orders at the end of the scrollable area there will be a foot note that says: This prescription meets the requirements of the Drug Enforcement Administration (DEA) electronic prescribing for controlled substances rules (21 CFR Parts 1300,1304, 1306, & 1311).
    4.  A new hidden action called Jump to eRx (JE) to allow the user to jump to the corresponding eRx record in the eRx Holding Queue.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation describing the new functionality introduced by this patch is available. The preferred method is to retrieve files from download.vista.med.va.gov. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites Software and Documentation Retrieval Instructions:

Upon National Release the documentation will be in the form of Adobe Acrobat files. Documentation will be found on the VA Software Documentation Library at:

https://www.va.gov/vdl/

<table>
<caption>Table of PSO*7*467 Release DocumentationTable includes file description, file name, and FTP mode</caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 44%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Title</strong></th>
<th><strong>FTP Mode</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PSO_7_0_P617_ig.pdf</td>
<td>Installation Guide - Inbound ePrescribing (PSO*7*0*p617)</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>PSO_7_0_P617_img.pdf</td>
<td>Implementation Guide - Inbound ePrescribing (PSO*7*0*p617)</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>PSO_7_0_P617_rn.pdf</td>
<td>Release Notes - Inbound ePrescribing (PSO*7*0*p617)</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>PSO_7_0_tm.pdf</td>
<td>Technical Manual/Security Guide - Outpatient Pharmacy V.7.0</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td><p>PSO_7_0_P617_um_1_2.pdf</p>
<p>PSO_7_0_P617_um_31.pdf</p>
<p>PSO_7_0_P617_um_32.pdf</p>
<p>PSO_7_0_P617_um_41.pdf</p>
<p>PSO_7_0_P617_um_42.pdf</p>
<p>PSO_7_0_P617_um_51.pdf</p>
<p>PSO_7_0_P617_um_52.pdf</p>
<p>PSO_7_0_P617_um_6.pdf</p></td>
<td>User Manual - Inbound ePrescribing (PSO*7*0*p617)</td>
<td>Binary</td>
</tr>
</tbody>
</table>

Table of PSO\*7\*467 Release DocumentationTable includes file description, file name, and FTP mode

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSO*7*635 Inbound ePrescribing Release Notes

## Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> *(This page included for two-sided copying.)*

1.  [Introduction 1](#introduction)
    1.  [PRE IEP Clearing House Transaction Services Warranty Period 2](#1.1_PRE_IEP_Clearing_House_Transaction_S)
2.  [PRE IEP Clearing House Transaction Services Defect Remediation 3](#pre-iep-clearing-house-transaction-services-defect-remediation)
    1.  [PRE IEP Clearing House Transaction Services eRx VistA PSO\*7.0\*635 4](#pre-iep-clearing-house-transaction-services-erx-vista-pso7.0635)
    2.  [PRE IEP Clearing House Transaction Services eRx v4.1 HUB 4](#2.2_PRE_IEP_Clearing_House_Transaction_S)
3.  [PRE IEP Clearing House Transaction Services ERX v4.1/PSO\*7.0\*635 Known Defects](#pre-iep-clearing-house-transaction-services-erx-v4.1pso7.0635-known-defects) [5](#pre-iep-clearing-house-transaction-services-erx-v4.1pso7.0635-known-defects)
4.  [Product Documentation 6](#product-documentation)

> *(This page included for two-sided copying.)*

## PRE IEP Clearing House Transaction Services eRx VistA PSO\*7.0\*635

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PRE IEP Clearing House Transaction Services eRx VistA PSO\*7.0\*635 defect remediation in this Warranty period release includes:

> EPRESCRIB-3407 Update Data Dictionary - File \#52.45

> EPRESCRIB-3408 NewRx coming with ObservationDateTime failure at hub generating RxRenewal Request

> EPRESCRIB-3410 RxRenewal Request failing at hub because “IndicationForUse” segment is not sending in “Sig” segment

> EPRESCRIB-3413 Quantity Unit of Measure fix for RxRenwal Request Medication Dispensed segment for 2017071 Messages

> EPRESCRIB-3415 ACR codes in file 52.45 has extra space

> EPRESCRIB-3419 The sig is coming from doctor, getting a hard error when generating a RxRnewal Request

> EPRESCRIB-3439 When NewRx message is coming with the multiple

> “OtherMedicationDate” Inbound job broke at hub, messages are not delivering to VistA

> EPRESCRIB-3441 eRx Sig gets truncated in HQ summary details screen, PSO ERX DRUG VALIDATION summary details Screen and OP header section when the eRx is coming with the Sig without spaces

> EPRESCRIB-3447 Vista refills not displaying correct refills for Replace RxRenewal Response message

> EPRESCRIB-3484 RxRenewal Response messages Vista Refills decrementing every time editing the refills.

1.  <span id="2.2_PRE_IEP_Clearing_House_Transaction_S" class="anchor"></span>PRE IEP Clearing House Transaction Services eRx v4.1 HUB The PRE IEP Clearing House Transaction Services eRx v4.1 HUB defect remediation in this Warranty period release includes:

> EPRESCRIB-3392 ERROR: Element 'Extension': \[facet 'pattern'\] The value '' is not accepted by the pattern '\[0-9\]+(\\\[0-9\]+)?'. ERROR: Element 'Extension': '' is not a valid value of the atomic type 'n1..8'

> EPRESCRIB-3393 ERROR: Element 'Name': Missing child element(s). Expected is ( FirstName )

> EPRESCRIB-3394 ERROR: Element 'CountryCode': This element is not expected. Expected is

> ( AddressLine1 )

> EPRESCRIB-3395 ERROR: Element 'ElectronicMail': \[facet 'pattern'\] The value '' is not accepted by the pattern '(\[!-~\]\|\[ \])\*\[!-~\](\[!-~\]\|\[ \])\*'. ERROR: Element 'ElectronicMail': '' is not a valid value of the atomic type 'MailAddressType'

> EPRESCRIB-3396 ERROR: Element 'Number': \[facet 'pattern'\] The value 'NONE' is not accepted by the pattern '\[0-9\]+(\\\[0-9\]+)?'

> EPRESCRIB-3397 ERROR: Element 'Number': \[facet 'pattern'\] The value 'otprovided' is not accepted by the pattern '\[0-9\]+(\\\[0-9\]+)?'

> EPRESCRIB-3398 ERROR: Element 'Value': \[facet 'pattern'\] The value '180.' is not accepted by the pattern '\[0-9\]+(\\\[0-9\]+)?'.

> EPRESCRIB-3406 \#Accepted by Pharmacy counts for Summary Report NewRx Only does not match OB Data in SQL

> EPRESCRIB-3412 A backlog of messages is queueing up and waiting for outbound delivery to CH during peak hours

> EPRESCRIB-3414 Quantity Unit of Measure fix for RxRenwal Request Medication Dispensed segment for 10.6 messages

> EPRESCRIB-3421 Extend the logic from 365 days to 1 and half year for messages relation to display at hub (Track/Audit page).

> EPRESCRIB-3428 Information, structure, and relationships conveyed through presentation cannot be understood.

> EPRESCRIB-3429 Text or images of text have a contrast ratio less than 4.5:1. EPRESCRIB-3430 Functionality of content is not operable through a keyboard interface EPRESCRIB-3431 Pages do not have a title that describes its topic or purpose

> EPRESCRIB-3432 Focusable components in the content do not receive focus in an order that preserves meaning and operability

> EPRESCRIB-3433 Changing the setting of user interface components automatically causes a

> change of context without advising the user of this behavior EPRESCRIB-3434 When errors are automatically detected, an error message is not

> described to the user in text

> EPRESCRIB-3435 An error message was provided, but it does not describe how to correct the error

> EPRESCRIB-3436 Content is not properly encoded and causes assistive technology to

> convey incorrect information

> EPRESCRIB-3437 The name, role, state or value of user interface elements in the product cannot be understood (programmatically determined)

> EPRESCRIB-3438 Software disrupts platform features that are defined in the platform documentation as accessibility features

> EPRESCRIB-3443 The SIG field in the PRESCRIPTION section is not wrapping text correctly for all message types (1,000 characters, no spaces).

> EPRESCRIB-3457 Two issues with the Reports Page - Columns are missing in the last three reports, NewRx counts not showing for Summary New Rx Only

> EPRESCRIB-3471 The Report totals at the bottom of the tables do not align with the correct column

> EPRESCRIB-3474 Reports Number of Records not being displayed at the bottom of all reports and column width for Message Type in Track/Audit not wide enough.
