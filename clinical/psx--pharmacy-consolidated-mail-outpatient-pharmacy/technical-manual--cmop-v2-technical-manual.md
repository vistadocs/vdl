---
title: CMOP Version 2 Technical Manual (Updated PSX*2*91)
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: (Updated PSX*2*91)
app_code: PSX
app_name: "Pharmacy: Consolidated Mail Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSX
patch_ver: 2
patch_id: PSX*2
group_key: "PSX:PSX:2"
file_numbers: []
security_keys: []
menu_options: 0
description: The Consolidated Mail Outpatient Pharmacy (CMOP) software package establishes an interface for the electronic transfer of information between Veterans Affairs Medical Centers (VAMCs) and the Consolidated Mail Outpatient Pharmacy host system for an integrated and highly automated outpatient pharmacy
audience: 
keywords: 
  - table
  - cmop
  - segment
  - contents
  - message
  - span
  - transmission
  - class
  - number
  - example
page_count: 0
word_count: 21251
section_count: 56
table_count: 88
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: April 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/psx_2_0_p91_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/psx_2_0_p91_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=85"
---

---
title: |
  Consolidated Mail Outpatient Pharmacy (CMOP)

  Version 2.0

  Technical Manual
---

![](cmop-version-2-technical-manual-updated-psx-2-91/001.png)

April 1997  
(Revised September 2021)

Revision History

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<caption><p><span id="_Toc84256329" class="anchor"></span>Table 1: Special Notations</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th>Revision Date</th>
<th>Revised Pages</th>
<th>Patch Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>09/2021</td>
<td>18</td>
<td>PSX*2*91</td>
<td>Removed language concerning Release of Information from CMOP Not Transmitted Rx List Message.</td>
</tr>
<tr class="even">
<td>11/2015</td>
<td>18</td>
<td>PSX*2*77</td>
<td>Updated the subject line of the "CMOP Not Transmitted Rxs - &lt;Site Name&gt;" bulletin screenshot on page 18.</td>
</tr>
<tr class="odd">
<td>06/2015</td>
<td>14,15,18</td>
<td>PSX*2*77</td>
<td>Update CMOP Not Dispensed Rx List and CMOP Not Transmitted Rx List Message mail messages</td>
</tr>
<tr class="even">
<td>12/2010</td>
<td>i, 71</td>
<td>PSX*2*71</td>
<td><p>Change to allow more than five warnings per prescription to be transmitted to CMOP, and also allow warning text that is greater than 220 characters per warning. Created a continuation segment in NTE|11A| to contain the warning text that is greater than the initial 220 characters, up to an additional 220 characters. The continuation segment immediately follows the NTE|11| segment of the warning.</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>07/2009</td>
<td>i, 33</td>
<td>PSX*2*65</td>
<td>Added PSXRPPL2 and PSXBPSR1 to the routine List. (REDACTED, PM; REDACTED, Tech Writer)</td>
</tr>
<tr class="even">
<td>01/2007</td>
<td>33, 65, 68-69, 71, 75, 75a-b, 77</td>
<td>PSX*2*54</td>
<td><p>Added PSXBLD1 to the Routine List. Updated affected HL7 segments to reference the new warning label source.</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>09/2006</td>
<td>All</td>
<td>PSX*2*61</td>
<td><p>Encapsulation II Follow-up Patches. Added PSX550 to the Routine List. (Clean-up - fixed both Table of Contents, added blank pages, deleted headers, re-numbered pages, etc.) This is a re-issue of the full manual.</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>04/1997</td>
<td></td>
<td></td>
<td>Original Released Technical Manual.</td>
</tr>
</tbody>
</table>

<span id="_Toc84256329" class="anchor"></span>Table 1: Special Notations

Table of Contents

List of Tables

Preface

Version 2.0 of Consolidated Mail Outpatient Pharmacy (CMOP) software processes and automatically transmits prescription data from a Veterans Affairs Medical Center (VAMC) to a CMOP host facility, where prescriptions are mailed from an integrated and highly automated outpatient prescription dispensing system. The CMOP software package is intended for pharmacists and pharmacy technicians who are familiar with the functionality of Outpatient Pharmacy Version 7.0.

This technical manual provides additional information for package coordinators and supervisors. Users who are not familiar with Veterans Health Information Systems and Technology Architecture (VistA) software may also wish to refer to documentation for VA Kernel.

# CMOP Version 2.0 Technical Manual


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [CMOP Version 2.0 Technical Manual](#cmop-version-20-technical-manual)
- [Introduction](#introduction)
- [Orientation](#orientation)
  - [Special Notations](#special-notations)
  - [Change Pages](#change-pages)
  - [Package Management](#package-management)
  - [Flowchart for Processing a CMOP Prescription](#flowchart-for-processing-a-cmop-prescription)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Installation](#installation)
  - [Resource Requirements](#resource-requirements)
  - [Hardware Requirements](#hardware-requirements)
  - [Specific System Requirements](#specific-system-requirements)
  - [MailMan Issues Related to CMOP Operations](#mailman-issues-related-to-cmop-operations)
  - [Mail Messages Seen at Remote Medical Centers](#mail-messages-seen-at-remote-medical-centers)
  - [Mail Messages Seen at CMOP Facilities](#mail-messages-seen-at-cmop-facilities)
  - [MailMan Server Option Set Up](#mailman-server-option-set-up)
  - [Kernel Site Parameter Setup](#kernel-site-parameter-setup)
  - [Mail Group](#mail-group)
  - [Package Security](#package-security)
    - [Security Keys Used by CMOP Remote Medical Centers](#security-keys-used-by-cmop-remote-medical-centers)
    - [Security Keys Used by CMOP Host Facilities](#security-keys-used-by-cmop-host-facilities)
  - [CMOP Host Facility Install for Printer](#cmop-host-facility-install-for-printer)
  - [Barcodes](#barcodes)
- [Files](#files)
  - [Outpatient Pharmacy Files](#outpatient-pharmacy-files)
- [Routine List](#routine-list)
- [# Exported Options](#exported-options)
  - [Menus](#menus)
- [Archiving and Purging](#archiving-and-purging)
  - [Host CMOP Facility](#host-cmop-facility)
  - [Remote Medical Center](#remote-medical-center)
- [Callable Routines](#callable-routines)
- [Routine Mapping](#routine-mapping)
- [External Relations](#external-relations)
  - [MailMan Issues Related to CMOP Operations](#mailman-issues-related-to-cmop-operations-1)
  - [Agreements](#agreements)
- [Internal Relations](#internal-relations)
- [Package-Wide Variables](#package-wide-variables)
- [On-Line Documentation](#on-line-documentation)
  - [Journaling Globals](#journaling-globals)
  - [Templates](#templates)
- [Glossary](#glossary)
- [Appendix A—Consolidated Mail Outpatient Pharmacy Communications Protocol](#appendix-aconsolidated-mail-outpatient-pharmacy-communications-protocol)
  - [Overview](#overview)
    - [Introduction](#introduction-1)
    - [Requirements & Assumptions](#requirements-assumptions)
    - [Environment Model](#environment-model)
  - [Communication Control Characters](#communication-control-characters)
    - [Control Sequences](#control-sequences)
    - [Block Number (BLK)](#block-number-blk)
    - [Text Length (TL)](#text-length-tl)
    - [Block Checking Characters (BCC)](#block-checking-characters-bcc)
  - [Establishment of Master / Slave Relationship](#establishment-of-master-slave-relationship)
  - [Message Transfer](#message-transfer)
    - [Transmission Blocks](#transmission-blocks)
    - [Replies](#replies)
  - [Interrupts](#interrupts)
  - [Timers and Recovery Procedures](#timers-and-recovery-procedures)
    - [Timers](#timers)
    - [Recovery Procedures](#recovery-procedures)
- [Appendix B—Consolidated Mail Outpatient Pharmacy Application Message Definition Statement](#appendix-bconsolidated-mail-outpatient-pharmacy-application-message-definition-statement)
  - [Overview of Message Encoding and Construction Rules](#overview-of-message-encoding-and-construction-rules)
    - [Messages](#messages)
    - [Segments](#segments)
  - [Message Header Segment—MSH](#message-header-segmentmsh)
  - [Patient Identification Segment—PID](#patient-identification-segmentpid)
  - [Common Order Segment—ORC](#common-order-segmentorc)
  - [Pharmacy Order Segments—RX1, ZX1](#pharmacy-order-segmentsrx1-zx1)
  - [NTE Notes and Comments Segment](#nte-notes-and-comments-segment)
    - [NTE Segment—Facility Specific Information Definition Table Set ID=1](#nte-segmentfacility-specific-information-definition-table-set-id1)
    - [RF Patient Instruction NTE Segment Definition Table Set ID=2](#rf-patient-instruction-nte-segment-definition-table-set-id2)
    - [NRF Patient Instruction NTE Segment Definition Table Set ID=3](#nrf-patient-instruction-nte-segment-definition-table-set-id3)
    - [Copayment NTE Segment Definition Table Set ID=4](#copayment-nte-segment-definition-table-set-id4)
    - [MRX Document NTE Segment Definition Table Set ID=5](#mrx-document-nte-segment-definition-table-set-id5)
    - [Suspense Notification NTE Segment Set ID=6](#suspense-notification-nte-segment-set-id6)
    - [SIG (Instructions) NTE Segment Definition Table Set ID=7](#sig-instructions-nte-segment-definition-table-set-id7)
    - [Patient Additional Street Address Segment Definition Table Set ID=8](#patient-additional-street-address-segment-definition-table-set-id8)
    - [Patient Warning Label Text Segment Definition Table Set ID=11](#patient-warning-label-text-segment-definition-table-set-id11)
  - [General Acknowledgment Message](#general-acknowledgment-message)
  - [Transaction Specifications](#transaction-specifications)
  - [Batch Transmissions](#batch-transmissions)
  - [VistA Query for Data from non-VistA System](#vista-query-for-data-from-non-vista-system)
  - [Non-VistA System Response to VistA Data Query](#non-vista-system-response-to-vista-data-query)
    - [NTE Segment—Vendor (non-VistA) Response Definition Table Set ID=99](#nte-segmentvendor-non-vista-response-definition-table-set-id99)
    - [NTE Segment—Vendor Ancillary Data Definition Table Set ID=100](#nte-segmentvendor-ancillary-data-definition-table-set-id100)
- [Appendix C—Consolidated Mail Outpatient Pharmacy Electronic Data / HL7 Interface Guidelines](#appendix-cconsolidated-mail-outpatient-pharmacy-electronic-data-hl7-interface-guidelines)
- [CMOP HL7 Interface Specification](#cmop-hl7-interface-specification)
- [Introduction](#introduction-2)
- [Key Terms](#key-terms)
  - [File Extensions](#file-extensions)
- [Message Rules](#message-rules)
- [Segment Rules](#segment-rules)
- [Field Rules](#field-rules)
- [Message Construction Rules](#message-construction-rules)
- [Communication Protocol](#communication-protocol)
  - [Concept of Operation](#concept-of-operation)
    - [Overview](#overview-1)
    - [Activation/Inactivation](#activationinactivation)
    - [Transmission Schedule](#transmission-schedule)
    - [Prescription Order Transmissions](#prescription-order-transmissions)
- [HL7 Segments Used in CMOP Transactions](#hl7-segments-used-in-cmop-transactions)
  - [Activate/Inactivate (.SIT)](#activateinactivate-sit)
  - [Activation Acknowledgement Message (.SAC)](#activation-acknowledgement-message-sac)
  - [Inactivation Acknowledgement Message (.SAC)](#inactivation-acknowledgement-message-sac)
  - [Transmission Scheduling (.SCH)](#transmission-scheduling-sch)
    - [Request Event Reason](#request-event-reason)
  - [Schedule Acknowledgement (.HAC)](#schedule-acknowledgement-hac)
  - [Batch Transmission Segments (.TRN)](#batch-transmission-segments-trn)
  - [Batch Transmission Acknowledgement/Non-Acknowledgement (.TAC)](#batch-transmission-acknowledgementnon-acknowledgement-tac)
  - [Prescription Fulfillment (.QRY)](#prescription-fulfillment-qry)
  - [Batch Prescription Fulfillment Acknowledgement (.QAC)](#batch-prescription-fulfillment-acknowledgement-qac)
  - [National Drug file Update (.NDF)](#national-drug-file-update-ndf)
  - [NDF Update Acknowledgement (.NAC)](#ndf-update-acknowledgement-nac)
- [Appendix A: Drug Warnings](#appendix-a-drug-warnings)
- [Appendix B: CMOP Host Site Directory](#appendix-b-cmop-host-site-directory)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Consolidated Mail Outpatient Pharmacy (CMOP) software package establishes an interface for the electronic transfer of information between Veterans Affairs Medical Centers (VAMCs) and the Consolidated Mail Outpatient Pharmacy host system for an integrated and highly automated outpatient pharmacy prescription dispensing system.

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Special Notations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following notations are used in this manual:

| Description                              | Notation                                                                                                                                     |
|------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Return or Enter Key                      | \<RET\> if in text, <u>\<RET\></u> if in screen example.                                                                                 |
| User Response on Computer Screen Example | Underlined and bold (they will not appear this way on the screen). After a user response on a screen example, <u>\<RET\></u> is implied. |
| Editor’s Note Description                | Inside square brackets: \[ \]                                                                                                                |
| Explanation Interrupting Computer        | Inside square brackets: \[ \] and screen example bold.                                                                                       |

<span id="_Toc84256330" class="anchor"></span>Table 2: Remote Medical Center

## Change Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Future modifications to the software may require changes to the documentation. Change pages will reflect the new version number and date in the footer. Vertical lines in the margin may also be used to further highlight changes on a page.

## Package Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package does not impose any additional legal requirements on the user, nor does it relieve the user of any legal requirements. Names and social security numbers used in the examples are fictitious.

## Flowchart for Processing a CMOP Prescription

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A single line border indicates that the action is a MEDICAL CENTER ACTIVITY.

> A double line border indicates that the action is a HOST CMOP ACTIVITY.

> Rx Entered at Medical Center  
> Rx Screened for CMOP Criteria  
> Drug Marked for CMOP in DRUG file (#50)  
> Mail-No CMOP  
> No Tradename  
> Rx Meets CMOP Criteria  
> Suspended for CMOP Transmission in RX SUSPENSE file (#52.5)  
> CMOP INDICATOR field in RX SUSPENSE file (#52.5) = Queued for Transmission  
> Activity Log in file \#52=Suspended for CMOP Transmission

> User Selects Initiate A Transmission TRANSMIT DATA THRU TODAY// \<RET\>  
> ARE YOU SURE YOU WISH TO CONTINUE ? NO//YES

> Transmission Job is Queued  

> Xmit Status in CMOP SYSTEM file (#550) = Transmitting Data  
> Select All Rx’s Queued for Transmission from Rx Suspense  
> Send/Transmit selected Rx’s to ECME for electronic billing  

> Wait to receive response from payer  
> (15 seconds for each e-billable Rx; 2 hours max.)  
> (e.g., 300 e-billable Rx’s = 4500 seconds/3600 = 1.25 hrs)  

> From the selected Rx’s, filter Rx’s that have unresolved DUR/REFILL TOO SOON rejects  

> From the remaining list, filter Rx’s for which the 3rd party payer has not responded  

> A MailMan message is generated and sent to PSXMAIL keyholders  

> Mark Selected Rx’s CMOP Indicator = Loading for Transmission  

> Rescreens Data for CMOP Transmission  

> Builds Transmission Data in CMOP RX QUEUE file (#550.1)  

> CMOP Error Encountered Message Created for Rx’s which were Selected, but not Transmitted  

> Creates Transmission Number in CMOP TRANSMISSION file (#550.2)  

> Creates MailMan Message for Transmission Data and Sends to the Host CMOP Server  

> Transmission Confirmation Message Generated  

> Creates Transmission Entry in the CMOP EVENT MULTIPLE Subfile of PRESCRIPTION file (#52) Marking the Entry as Transmitted  

> An Entry Is Made in the ACTIVITY LOG Subfile in PRESCRIPTION file (#52) as Transmitted to CMOP  

> CMOP Indicator in File \#52.5 for All Transmitted Rx’s = Transmission Completed  

> Xmit Status in CMOP SYSTEM file (#550) = No Current Transmission  

> Data Has Transmitted/Job Is Complete

> Transmission Message Is Received at CMOP Facility by the CMOP Server

> Tasked Job Performs the Following:  
> Data Is Downloaded Into CMOP DATABASE file (#552.2) for Transmission to the Vendor  
> Data Is Entered in the CMOP MASTER DATABASE file (#552.4)

> CMOP Review Message Containing a List of All Rx’s for This Transmission Is Sent

> Transmission Acknowledgement Message Is Created and Sent to the Medical Center

> Acknowledgement Message Received by the CMOP Server at Medical Center

> Tasked Job Completes the Following:  
> Acknowledgement Date/Time Is Filed in the CMOP TRANSMISSION file (#550.2)

> The Transmission Phase of the Rx Is Completed

> The Rx Is Downloaded to the Vendor Automated Dispensing System for Filling

> Download Acknowledgement Message is Created and Sent to the Medical Center

> Download Acknowledgement message is received by CMOP Server at the Medical Center

> Downloaded Data is purged from the CMOP RX QUEUE file (#550.1)

> Rx Release Data Is Received by CMOP VistA from the Vendor System

> Rx Data Stored Temporarily in the CMOP RELEASE file (#552.3)

> The CMOP Background Filer Files Data Listed Ready to File from CMOP RELEASE file (#552.3), Files It in the CMOP MASTER DATABASE file (#552.4), and Marks the Rx Status = Released

> The Background Filer Selects All Data Marked Released In the CMOP MASTER DATABASE file (#552.4), Builds a CMOP Release MailMan Message for Each Facility Having Released Data and Marks the Rx Status = Returned

> The Mail Message Is Sent to the Medical Centers to the CMOP Server  
> \*\*\*USERS DO NOT RECEIVE THESE MESSAGES\*\*\*

> Release Data Message Is Received by the CMOP Server

> Job Is Tasked to File Release Information from the Release  
> Data Message into the PRESCRIPTION file (#52). This Action Will Release the Rx and Generate Any Prescription Copayment Necessary

> A Return Release Acknowledgement Message Is Built on Completion of Filing the Rx’s. This Message Is Sent to the Host Facility

> CMOP Server at the CMOP Host Facility to Update the CMOP MASTER DATABASE file (#552.4).

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For installation of the Consolidated Mail Outpatient Pharmacy Version 2.0 software package, please refer to the Installation Guide.

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version (2.0) of Consolidated Mail Outpatient Pharmacy requires, at least, the following VA software applications.

| Software Application     | Minimum Version Required |
|--------------------------|--------------------------|
| Kernel                   | 8.0                      |
| MailMan                  | 7.1                      |
| VA FileMan               | 21.0                     |
| National Drug File (NDF) | 3.16                     |
| Outpatient Pharmacy (OP) | 7.0                      |

<span id="_Toc84256331" class="anchor"></span>Table 3: Host Facility

| Software Application     | Minimum Version Required |
|--------------------------|--------------------------|
| Kernel                   | 8.0                      |
| MailMan                  | 7.1                      |
| VA FileMan               | 21.0                     |
| National Drug File (NDF) | 3.16                     |

<span id="_Toc84256332" class="anchor"></span>Table 4: CMOP Remote Medical Center Security Keys

## Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no additional hardware requirements for the medical centers.

The host facility must support a port to port connection between the VistA CMOP PC system and the vendor PC system. Label printers should be available for the VistA CMOP system for use in the event of a system failure on the automated dispensing system.

## Specific System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ENQLM – ALPHA/VMS Sites Only

Please refer to REDACTED.

Subj: AXP\*105 Recommended Parameter and Quota Changes \[#30955206\] 03 Mar 00 19:24 for system settings.

## MailMan Issues Related to CMOP Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful operation of the CMOP software is highly dependent on MailMan processing of the communications between the software and the user. The developer recommends that the medical centers and CMOP host facilities use TCP/IP for the best results.

Mail messages are used extensively to relate the status of jobs, deliver reports, and advise users of data or transmission problems. The transmission mechanism for prescription data is the MailMan server option S.PSXX CMOP SERVER. MailMan delivers data to this option, which queues numerous background jobs to handle processing and releasing of prescriptions. Information Resources Management (IRM) should note that problems with MailMan may directly impact on the performance of the CMOP software. The following examples describe the various types of mail messages produced by the CMOP software.

Example: CMOP MailMan Messages

The Consolidated Mail Outpatient Pharmacy software generates numerous MailMan messages to notify pharmacy personnel regarding the status of background procedures. Messages received by the host CMOP and the medical centers are included here with a description of the content. All messages are sent to users who hold the PSXMAIL security key.

## Mail Messages Seen at Remote Medical Centers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The CMOP Activation Request message is generated when the Outpatient Pharmacy personnel submit a request to activate the medical center facility to do CMOP processing. This message only indicates that a user has selected to activate the site using the CMOP Site Manager option Activate/Inactivate CMOP Processing. Activation does not take place until a response is received from the CMOP host.

Subj: CMOP Activation Request \[#38898\] 11 Dec 96 10:03 5 Lines

From: POSTMASTER (Sender: OPPHARMACIST15,ONE) in 'IN' basket. Page 1

-----------------------------------------------------------------------------------------

\*\*NEW\*\*

Request to activate.

CMOP REDACTED

Requester : OPPHARMACIST15,ONE

Action Date/Time: DEC 11,1996@10:03

2.  The CMOP Activation Approved message is returned from the CMOP facility when the CMOP Manager has approved the activation request. At the time of this message, an alert is also generated to all CMOP Manager key holders indicating the approval. At this time, the site becomes active for CMOP processing. Pharmacy users should sign off the system completely. The users should sign back onto the system after receiving the approval message to set up the appropriate CMOP/Outpatient site parameters. All prescriptions processed after the site parameters are set up for CMOP will be screened and suspended for CMOP if transmission criteria are met.

Subj: CMOP Activation Approved \[#33619\] 09 Feb 97 6 Lines

From: POSTMASTER in 'IN' 11:50 basket. Page 1 \*\*NEW\*\*

-----------------------------------------------------------------------------------------

Request to activate CMOP processing.

CMOP: REDACTED

Approving Official: CMOPPHARMACIST24,ONE

Action Date/Time: FEB 9,1997@11:50

Action : Approved

3.  The CMOP Transmission Confirmation message is created when medical center CMOP transmission data has been handed to MailMan for delivery to the CMOP host facility. The subject line of the message will include the transmission number. A typical CMOP transmission would look like the example below. Controlled substance transmissions will be indicated on the subject line (i.e. CMOP CS 521-737 Transmitted \[#34652\] 10 Jan 97 06:22 8 Lines). Each successful transmission will generate a transmission confirmation message. If a user initiates a transmission and does not receive a transmission confirmation message, the medical center IRM Service should be contacted for assistance.

Subj: XXXXXXXXXXX CMOP 521-737 Transmitted \[#38862\] 09 Feb 97 08:158 Lines

From: POSTMASTER (Sender: CMOPPHARMACIST24,ONE) in 'IN' basket. Page 1

\*\*NEW\*\*

-----------------------------------------------------------------------------------------

CMOP TRANSMISSION CONFIRMATION:

Pharmacy Division : XXXXXXXXXXX

Batch Number : 521-737

Transmitted by : CMOPPHARMACIST24,ONE

Date/Time : FEB 4,1997@08:15:48

Total orders/Rx's : 1/5

Beginning order \# : 12

Ending order \# : 12

4.  The CMOP Transmission Acknowledgment message is created by the host CMOP software when the data transmission is received, data is validated, and loaded into safe storage in the CMOP database. A typical CMOP transmission would like the example below. Controlled substance transmissions will be indicated on the subject line (i.e. CMOP CS 521-524 Acknowledged. \[#32614\] 06 Jan 95 15:18 8 Lines). This message serves two purposes. Initially the message is delivered to the remote medical center to the PSXMAIL key holders to indicate that the CMOP has successfully received the data transmitted. The message is also delivered to the medical center CMOP server software and is used to file the date and time the data was received at the CMOP in the transmission entry in the CMOP TRANSMISSION file (#550.2). Receipt of both the Transmission Confirmation and the Transmission Acknowledgment messages for a single transmission confirm that the data transmitted and downloaded to the CMOP facility successfully.

Subj: CMOP 521-524 Acknowledged. \[#34712\] 04 Apr 95 17:17 8 Lines

From: POSTMASTER in 'IN' basket. Page 1 \*\*NEW\*\*

-----------------------------------------------------------------------------------------

CMOP TRANSMISSION ACKNOWLEDGEMENT:

Pharmacy Division : XXXXXXXXXXX

Batch Number : 521-737

Transmitted by : CMOPPHARMACIST1,ONE

Date/Time : FEB 4,1997@09:16:43

Total orders/Rx's : 1/5

Beginning order \# : 12

Ending order \# : 12

5.  The CMOP Error Encountered message is created when medical center CMOP transmission data has been handed to MailMan for delivery to the CMOP host facility. This message is a direct result of the CMOP software screening prescriptions suspended for CMOP during data transmission. If a problem is detected with a prescription selected for transmission, the prescription is not transmitted to the CMOP, but is noted in this message to the user to provide information to correct the problem. If the data is corrected as noted in this message, the prescription will be included in the next transmission. If the data problem is not corrected, the prescription will continue to be listed in this message each time a transmission is initiated. If the data is not corrected the prescription will never be transmitted. The CMOP Error Encountered message may be sent in varying formats depending on the data problems to be reported. Two examples are shown on the following page.

Example 1

Subj: 521 CMOP Error Encountered \[#34392\] 11 Dec 96 08:43 16 Lines From: POSTMASTER (Sender: CMOPPHARMACIST2,ONE) in 'IN' basket. Page 1

\*\*NEW\*\*

-----------------------------------------------------------------------------------------

An error has been encountered while processing prescription data for the Consolidated Mail Outpatient Pharmacy system.

Date/Time: DEC 11,1996@08:43

Process: Data Validation

Error Type: Invalid or missing data

Description:

RX \# Fill Data Field SSN NAME

300410 Original Patient Adress 000-23-4567 CMOPPATIENT2,ONE

Action Taken: Rx's not sent to CMOP but still suspended for transmission.

Recommended action: Correct invalid data.

Example 2

Subj: 521 CMOP Error Encountered \[#38880\] 05 Dec 96 14:14 21 Lines From: POSTMASTER (Sender: CMOPPHARMACIST2,ONE) in 'IN' basket. Page 1

\*\*NEW\*\*

-----------------------------------------------------------------------------------------

An error has been encountered while processing prescription data for the Consolidated Mail Outpatient Pharmacy system.

Date/Time: DEC 5,1996@14:14

Process : Transmission of Batch Data

Error Type: Invalid or missing data

Description :

The following data is missing in the OUTPATIENT SITE file.

State

Street Address

City

Zip Code

Area Code

Phone Number

Action Taken: No data transmission will occur without this information. Recommended action: Correct invalid data.

6.  The CMOP Inactivation Notice message is generated when the Outpatient Pharmacy personnel selects to inactivate the medical center using the CMOP Site Manager menu option Activate/Inactivate CMOP Processing. Inactivation of CMOP processing is immediately effective. Users who do not sign off and then sign back onto the system when inactivation takes place will continue to do CMOP processing.

Subj: CMOP Inactivation Notice \[#38894\] 05 Dec 96 10:57 05 Lines From: POSTMASTER (Sender: OPPHARMACIST2,ONE) in 'IN' basket. Page 1

\*\*NEW\*\*

-----------------------------------------------------------------------------------------

Inactivation notice sent

CMOP: REDACTED

Requester: OPPHARMACIST2,ONE

Action Date/Time: DEC 5,1996@10:57

7.  The CMOP Auto-Transmission Schedule message is generated when the Outpatient Pharmacy personnel uses the Setup Auto-transmission option from the CMOP Site Manager menu to set up an automated transmission schedule to the CMOP host facility. A typical CMOP transmission will look like the example below. Controlled substance transmissions will be indicated on the subject line (i.e. CMOP CS Auto-Transmission Schedule \[#36452\] 11 Jan 96 07:24 7 Lines). The message notifies key holders that manual transmissions are not necessary to transmit data. Transmissions will begin automatically on the date and times indicated and continue for the selected frequency until the transmissions are unscheduled or modified.

Subj: CMOP Auto-Transmission Schedule \[#38875\] 11 Dec 96 09:32 7 Lines

From: POSTMASTER (Sender: OPPHARMACIST2,ONE) in 'IN' basket. Page 1

\*\*NEW\*\*

-----------------------------------------------------------------------------------------

Auto-transmission Schedule.

Facility : XXXXXXXXXXX, AL.

Date Initiated : Dec 11, 1996@09:32

Begin Automatic Transmissions : Dec 11, 1996@09:32

Number of days to transmit thru: 1

Scheduling Frequency (hours) : 6

Initiating Official : OPPHARMACIST2,ONE

8.  The CMOP Not Dispensed Rx List message is generated when release information indicates a prescription has been cancelled (not dispensed) by the vendor-automated system. The prescription at the remote medical center is marked not dispensed in the PRESCRIPTION file (#52). The prescription is not marked with a status of Cancelled. The prescriptions may be filled locally, edited and re-suspended, or resubmitted for CMOP processing. Cancellation reasons are listed with the Rx number and other transmission information to assist the user in correcting the cause of the cancellation and re-submitting the prescription for filling by the CMOP. A separate message is created for each pharmacy division. The prescription numbers include the standard symbols denoting additional information used by Outpatient Pharmacy. Prescription numbers for ePharmacy claims shall be marked with ‘e’. Prescription numbers with a first party copay shall be marked with ‘\$’.

Subj: CMOP Not Dispensed Rx List \[#38912\] 11 Dec 96 11:05 24 Lines

From: POSTMASTER in 'IN' basket. Page 1 \*\*NEW\*\*

-----------------------------------------------------------------------------------------

Not Dispensed Rx Report for the REDACTED Division.

The following prescriptions were not dispensed by the vendor:

Patient: CMOPPATIENT16,ONE SSN: 000-00-0001

Rx \#: 11642K\$e (ORG) Qty: 60 Trans \#: 737

Drug: ISONIAZID 100MG TAB CMOP Drug ID: I0067

Reason: QUANTITY OR DISP PROBLEM

Rx \#: 15634A\$ (ORG) Qty: 120 Trans \#: 737

Drug: AMINOPHYLLINE 500MG RTL SUPP CMOP Drug ID: A0214

Reason: QUANTITY OR DISP PROBLEM

Patient: CMOPPATIENT3,ONE SSN: 000-00-0001

Rx \#: 15558A (ORG) Qty: 120 Trans \#: 738

Drug: ACETAMINOPHEN 325MG TAB CMOP Drug ID: A0022

Reason: QUANTITY OR DISP PROBLEM

9.  The CMOP Acknowledgement not Received message is sent when a Transmission Acknowledgement message has not been received for a previous transmission after 24 hours. The CMOP software checks each transmission entry in the CMOP TRANSMISSION file (#550.2) 24 hours after the data is transmitted to ensure that the data was received at the CMOP host facility. If an acknowledgement date/time has not been filed for the transmission, this message reminds the key holders that the Transmission Acknowledgement message has not yet been received. The user should first contact the medical center IRM Service and request that the MailMan queue be checked to see if the transmission was sent. If it has been sent, the CMOP Manager at the host facility should be contacted to determine if there is another reason for the delay.

Subj: 521 CMOP Acknowledgement not Received \[#38915\] 20 Feb 97 15:56 3 Lines

From: POSTMASTER in 'IN' basket. Page 1

-----------------------------------------------------------------------------------------

An acknowledgement message for transmission \# 739 has not been

received within the specified time. Please contact the CMOP facility

to see if there is a problem.

10. The CMOP Recovery Message is sent whenever a failed CMOP transmission is detected. This message is simply a notification message that the last transmission did not complete. CMOP recovery procedures were initiated to reset the data so that it will be transmitted in the next transmission for that division.

Subj: CMOP Recovery Message REDACTED, AL. \[#3288\] 11/25/02@11:55 11 Lines From: \<POSTMASTER@BAB.ISC-xxxx.VA.GOV\> in 'IN' basket. Page 1 \*\*NEW\*\*

-----------------------------------------------------------------------------------------

The last CMOP transmission did not complete properly. The data for this transmission will be sent to the CMOP during the next transmission for that division.

If you have scheduled auto transmissions for CMOP, please check to see that they are still scheduled for the correct time.

This message is just a notification that problems were detected with the last transmission and that the data was sent to the CMOP facility for processing. If you are getting this message frequently, please contact your IRM staff.

Otherwise there is not anything that you need to do.

Transmission: 20081730

Division: REDACTED

CMOP Host: REDACTED

Type: NON-Controlled Subs

Date/Time: NOV 25, 2002@11:55:25

The prescriptions have been reset into CMOP suspense and this transmission has been closed

11. The CMOP Error Message is sent when the software encounters an error that interrupts the transmission. CMOP will then reset the prescriptions for the division's transmission that was interrupted and proceed to process the other divisions.

Subj: CMOP Error TROY 4003 \[#138163\] 12/18/02@10:19 5 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------------------

NON-CS CMOP Transmission encountered the following error. Please investigate \\

Division: XXXX

Type/Batch NON-CS / 4003

Error: LOCK+16^PSXRTR:1, %DSM-E-NUMBER, Attempt to perform division

by zero, -DSM-I-ECODE, MUMPS error code: M9

The prescriptions have been reset and other divisions' transmissions are continuing.

12. The CS or NON-CS Scheduled Transmission Re-Queued Message is sent if an auto- scheduled transmission starts up and finds another transmission is still in process. After the message is sent, the auto-scheduled CS or NON-CS transmission is re-queued to start again with a thirty-minute delay.

Subj: NON-CS Scheduled Transmission RE-Queued \[#138176\] 12/18/02@15:06

6 lines

From: CMOPPHARMACIST27,ONE In 'IN' basket. Page 1

-----------------------------------------------------------------------------------------

The NON-CS Scheduled Transmission for DEC 18,2002@15:06:01 was re-queued with task \# 2026 to run again in 30 minutes. It could not obtain a lock on the RX QUEUE file \#550.1.

That indicates that a transmission was in progress.

If you are getting this message frequently, please contact your IRM Group.

13. The CMOP Retransmission Report Message has been enhanced to include the list of prescriptions that are either sent or will not be sent because they have been released.

Subj: CMOP Retransmission Report for 7781 \[#32168468\] 12/12/02@15:55

109 lines

From: POSTMASTER - UNKNOWN

(Sender: CMOPPHARMACIST26,ONE - ADP SITE MANAGER, IRM SERVICE (IRM - phone: x85261)

In 'IN' basket. Page 1

-----------------------------------------------------------------------------------------

CMOP Re-Transmission Report

Retransmission \# 7782.

The Original Transmission \# 7781 contained:

Beginning Message Number: 1

Ending Message Number : 80

Total Orders : 80

Total Rx's : 90

Retransmission \# 7782 contained:

Beginning Message Number: 1

Ending Message Number : 80

Total Orders : 80

Total Rx's : 90

\*\* Prescriptions that have been released are not sent. \*\* Following is the list of prescriptions

and their 'Sent' or 'Released Date' status.

CMOPPATIENT1,ONE 335-xxxxx 1192147G-2 SENT

CMOPPATIENT2,ONE 321-xxxxx 1380689-2 12/10/02

CMOPPATIENT3,ONE 344-16-xxxxx 1401097-2 SENT

CMOPPATIENT4,ONE 353-12-xxxxx 1395540A-0 SENT

CMOPPATIENT5,ONE 348-30-xxxxx 1277158D-3 SENT

14. The ePharmacy CMOP Not Transmitted Rx List Message lists all e-billable prescriptions for which no response has been received from the third-party payer. The prescriptions listed have not been transmitted to CMOP and remain in the CMOP queue. The message includes the first attempted transmission to CMOP and the number of failed attempts.

Subj: ePharmacy CMOP Not TRANSMITTED Rxs - CBOC PHARMACY \[#2442829\]

11/10/15@10:46 24 lines

From: POSTMASTER In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------------------

The prescriptions listed in this message did not transmit to CMOP for one of the reasons below:

A response from the third party payer was not received

OR

The prescriptions are non-billable in VistA

The prescriptions will remain in the CMOP queue and will transmit when the response from the third party payer is received, or the non-billable issue is resolved.

Division: CBOC PHARMACY

-----------------------------------------------------------------------------------------

NOT

TRANSMITTED

RX#/Fill \#DAYS PATIENT(LAST4) DRUG 1<sup>ST</sup>

DT \#DAYS

-----------------------------------------------------------------------------------------

70000007/0 ECMEPATIENT,DAVE(2365) BENZTROPINE 2MG

TAB 11/10/15 1

Total CBOC PHARMACY: 1 Patients and 1 Prescriptions.

## Mail Messages Seen at CMOP Facilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The CMOP Activation Request message is generated when the Outpatient Pharmacy personnel submit a request to activate the medical center facility to do CMOP processing. This message is received at the host CMOP facility and notifies the CMOP Manager that a medical center is requesting to activate CMOP processing. An alert is also generated at the time of this message which requires a response from the CMOP Manager before the medical center can begin CMOP processing. This message is also used to update the CMOP NATIONAL SITE file (#552).

Subj: CMOP Activation Request \[#38899\] 05 Dec 96 10:58 5 Lines

From: POSTMASTER in 'IN' basket. Page 1 \*\*NEW\*\*

-----------------------------------------------------------------------------------------

Request to activate CMOP processing.

Facility: XXXXXXXXXXX, AL.

Requester: OPPHARMACIST10,ONE

Request date/time: DEC 5,1996@10:58

2.  The CMOP Activation Approval message is sent to all holders of the key (PSXMAIL) at the host facility. This message notifies the manager that a medical center has now been activated to transmit data to the CMOP.

Subj: CMOP Activation Approval \[#38908\] 11 Dec 96 10:28 6 Lines

From: POSTMASTER (Sender: CMOPPHARMACIST28,ONE) in 'IN' basket. Page 1

\*\*NEW\*\*

-----------------------------------------------------------------------------------------

Request to activate CMOP processing.

Facility : XXXXXXXXXXX, AL.

Requester : CMOPPHARMACIST28,ONE

Request date/time:DEC 11,1996@10:28

Action taken :Approved

3.  The CMOP Inactivation Notice is received by the CMOP host facility when the medical center inactivates CMOP processing. This message triggers an inactivation flag in the CMOP NATIONAL SITE file (#552). This flag indicates the medical center is inactive and data cannot be received from that medical center until a request to activate CMOP processing is received by the host and approved by the CMOP manager.

Subj: CMOP Inactivation Notice,XXXXXXXXXXX,AL. 09 Feb 96 11:50 5

\[#38895\] Lines

From: POSTMASTER in 'IN' basket. Page 1 \*\*NEW\*\*

-----------------------------------------------------------------------------------------

Notice to Inactivate CMOP Processing.

Processing.

Facility: XXXXXXXXXXX, AL.

Notifying Official: CMOPPHARMACIST28,ONE

Notification date/time: FEB 9,1996@11:50

4.  The CMOP (Batch Number) from (Site) Received message is created when data is downloaded successfully into the CMOP database files at the host facility. This message informs the CMOP personnel that a transmission has arrived and is ready to transfer to the automated vendor system. A typical CMOP transmission will look like the example below. Controlled substance transmissions will be indicated on the subject line (i.e. CMOP CS 541-737 from XXXXXXXXXXX Received. \[#35641\] 10 Aug 95 14:45 8 Lines). If the CMOP interface is running when this data is received, it is automatically scheduled and downloaded to the vendor system without delay.

Subj: CMOP 521-737 from XXXXXXXXXXX Received. \[#34543\] 04 Feb 95 15:52 8

Lines

From: POSTMASTER (Sender: CMOPPHARMACIST28,ONE) in 'IN' basket. Page 1

-----------------------------------------------------------------------------------------

CMOP TRANSMISSION RECEIVED:

Pharmacy Division: XXXXXXXXXXX

Batch Number : 521-737

Transmitted by : CMOPPHARMACIST28,ONE

Date/Time : Feb 04, 1997@08:43:44

Total orders/Rx's: 1/5

Beginning order \#: 12

Ending order \# : 12

5.  The CMOP Review \# (Batch Number) message is created on successful receipt of data from the medical center. This message provides a hard copy summary report of all prescriptions included in the transmission.

Subj: CMOP Review \# 521-737, XXXXXXXXXXX \[#34227\] 11 Dec 97 08:43 9 Lines

From: POSTMASTER in 'IN' basket. Page 1 \*\*NEW\*\*

-----------------------------------------------------------------------------------------

XXXXXXXXXXX, AL. 521-737 TRANSMITTED: DEC 11,1996@08:43:29

ORD# PATIENT RX# FILL DRUG NAME

-----------------------------------------------------------------------------------------

12 CMOPPATIENT31,ONE 15525B ORIG ACETAMINOPHEN 325MG TAB

15634A ORIG AMINOPHYLLINE 500MG RTL SUPP

15631A ORIG AMITRIPTYLINE HCL 75MG TAB

15625A ORIG AMOXICILLIN 500MG CAP

11642K ORIG ISONIAZID 100MG TAB

6.  The CMOP Auto-Transmission Schedule message is generated when the Outpatient Pharmacy personnel uses the Setup Auto-transmission option on the Transmission Menu to set up an automated transmission schedule to the CMOP host facility. The message notifies the host CMOP personnel that the medical center has set up a schedule for automatic transmissions. Transmissions will begin automatically on the date and time indicated and will continue for the selected frequency until the transmissions are unscheduled or modified. This information is recorded in the CMOP NATIONAL SITE file (#552). A typical CMOP transmission will look like the example below. Controlled substance transmissions will be indicated on the subject line (i.e. CMOP CS Auto-Transmission Schedule, XXXXXXXXXXX, AL. \[#36874\] 22 Mar 96 10:42 7 Lines).

Subj: CMOP Auto-Transmission Schedule, XXXXXXXXXXX, AL. \[#38881\]

11 Dec 96 09:33 7 Lines

From: POSTMASTER (Sender: CMOPPHARMACIST30,ONE) in 'IN' basket. Page 1

\*\*NEW\*\*

-----------------------------------------------------------------------------------------

Auto-Transmission Schedule.

Facility : XXXXXXXXXXX, AL.

Initiating Official : CMOPPHARMACIST30,ONE

Begin Automatic Transmissions : Dec 11, 1996@09:32

Scheduling Frequency (hours) : 6

Number of days to transmit thru: 1

Initiating Official : CMOPPHARMACIST22,ONE

## MailMan Server Option Set Up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software is designed to transmit data via MailMan between the remote medical center facilities and the host facility. MailMan servers are used to accomplish this data transmission.

For a server to function it must be associated with an entry in the BULLETIN file (#3.6). The selected bulletin entry must point to a mail group with at least one active user.

A mail group must be set up with the name, CMOP MANAGERS. The mail group must have at least one active user as a member for the CMOP software to operate. It is recommended that the Outpatient Pharmacy package coordinator and other pharmacy staff responsible for CMOP functions be members of this mail group.

The installation process will set up the following OPTION (#19) and BULLETIN file (#3.6) entries. The entries may be viewed using the VA FileMan Inquire to File Entries option and will contain the information listed below:

VA FileMan Version 21.0

Select OPTION: Inquire to File Entries

OUTPUT FROM WHAT FILE: OPTION // \<RET\> (5464 entries)

Select OPTION NAME: PSXX CMOP SERVER Consolidated Mail Outpatient

Pharmacy Server

ANOTHER ONE: \<RET\>

STANDARD CAPTIONED OUTPUT? YES// \<RET\> (YES)

DISPLAY COMPUTED FIELDS? NO// \<RET\> (NO)

DISPLAY AUDIT TRAIL? NO// \<RET\> (NO)

NAME: PSXX CMOP SERVER

MENU TEXT: Consolidated Mail Outpatient Pharmacy Server

TYPE: server CREATOR: POSTMASTER

LOCK: PSXCMOPMGR PACKAGE: CMOP

DESCRIPTION: This server acts as the receiver for data transmissions and other communications for the Consolidated Mail Outpatient Pharmacy system.

ROUTINE: PSXSERV SERVER BULLETIN: PSX CMOP

SERVER ACTION: RUN IMMEDIATELY SERVER MAIL GROUP: CMOP MANAGERS SUPRESS BULLETIN: YES, SUPRESS IT

UPPERCASE MENU TEXT: CONSOLIDATED MAIL OUTPATIENT P

Select OPTION NAME: \<RET\>

1.  The site must enter CMOP Managers in the MAIL GROUP field of the PSX CMOP entry in the BULLETIN file (#3.6).

## Kernel Site Parameter Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MailMan patch XM\*7.1\*36 should be installed. When patch is in place, set the fields NETWORK - MAX LINES @ SEND TO and NETWORK - MAX LINES RECEIVED to null as in the following example. This will allow larger CMOP transmissions to build without bumping into the preset Kernel site parameter limitations.

Example:

MSM\>D ^XUP

Setting up programmer environment

terminal type set to : C-VT100

Select OPTION NAME: XMKSP

Kernel Site Parameters for MailMan

Select KERNEL SITE PARAMETERS DOMAIN NAME: \[Enter Your Site’s Domain Name\]

TIME ZONE: CST// ^NETWORK - MAX LINES @ SEND TO

NETWORK - MAX LINES @ SEND TO: 15000// @

SURE YOU WANT TO DELETE? Y (Yes)

NETWORK - MAX LINES RECEIVED: 15000// @

SURE YOU WANT TO DELETE? Y (Yes)

Select KERNEL SITE PARAMETERS DOMAIN NAME: \<RET\>

## Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A public mail group must be set up with the name, CMOP MANAGERS. The CMOP MANAGERS mail group should exist at all sending sites. The mail group must have at least one active user as a member for the CMOP software to operate.

## Package Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Security Keys Used by CMOP Remote Medical Centers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The security keys listed below control the access necessary to operate the CMOP software. These keys should be assigned by the Chief of Pharmacy or a designee.

| Security Key | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSXCMOPMGR   | This security key locks the CMOP Site Manager Menu.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PSX XMIT     | Only holders of this security key and the PSXCMOPMGR key may transmit data to the CMOP using suspense options. This key also locks the Transmission Menu on the CMOP Site Manager Menu.                                                                                                                                                                                                                                                                                              |
| PSXRTRAN     | This key allows the holder to access the Re-transmit CMOP Data option which re-sends previously transmitted data to the CMOP.                                                                                                                                                                                                                                                                                                                                                        |
| PSXAUTOX     | This security key allows users access to the Setup Auto-transmission option. This key in combination with the PSXCMOPMGR and PSX XMIT are required to set up the auto-transmission schedule.                                                                                                                                                                                                                                                                                         |
| PSNMGR       | This security key is used to lock the CMOP Mark/Unmark (Single drug) and the Loop CMOP Match to Local Drug File options which use the NATIONAL DRUG file (#50.6) to mark and match items for CMOP dispense. This key is not exported with CMOP.                                                                                                                                                                                                                                      |
| PSXMAIL      | This security key enables a site manager to specify who receives the various mail messages and alerts generated by the CMOP process. The user(s) assigned this key must be active in the system. When the mail messages are generated, the software will look for users with the PSXMAIL key who are active. If there are no users with this key or there are users with this key who are inactive, then the software will send the messages to all holders with the PSXCMOPMGR key. |
| PSXRESUB     | This security key is used to lock the Resubmit CMOP Rx option and enables a designated user to resubmit Rx’s to the CMOP.                                                                                                                                                                                                                                                                                                                                                            |

<span id="_Toc84256333" class="anchor"></span>Table 5: CMOP Remote Host Facility Security Keys

### Security Keys Used by CMOP Host Facilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The security keys listed below control the access necessary to operate the CMOP software. At the host CMOP, these keys should be assigned by the CMOP Director or a designee.

| Security Key | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PSXCMOPMGR   | This security key locks the CMOP System Management Menu.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PSXCOST      | This key allows the holder to access the compile/recompile, initialize, update, and purge options of the Facility Cost Management menu.                                                                                                                                                                                                                                                                                                                                              |
| PSXRPH       | This key should only be assigned to the pharmacists who will be responsible for the release of prescriptions at the CMOP. The user must have this key to manually release Rx’s at the CMOP host facility.                                                                                                                                                                                                                                                                            |
| PSNMGR       | This security key is used to lock the CMOP Mark/Unmark (Single drug) and the Loop CMOP Match to Local Drug File options which use the NATIONAL DRUG file (#50.6) to mark and match items for CMOP dispense. This key is not exported with CMOP.                                                                                                                                                                                                                                      |
| PSXMAIL      | This security key enables a site manager to specify who receives the various mail messages and alerts generated by the CMOP process. The user(s) assigned this key must be active in the system. When the mail messages are generated, the software will look for users with the PSXMAIL key who are active. If there are no users with this key or there are users with this key who are inactive, then the software will send the messages to all holders with the PSXCMOPMGR key. |

<span id="_Toc84256334" class="anchor"></span>Table 6: Outpatient Pharmacy Files

## CMOP Host Facility Install for Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

2.  Each CMOP host facility should have a label printer(s) set up with new label stock forms for printing CMOP labels should the automated dispensing equipment fail. This will allow the CMOP to print labels for filling prescriptions manually and should only be used in an emergency situation.

The following barcode information may be helpful in setting up barcode labels.

## Barcodes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of Consolidated Mail Outpatient Pharmacy includes the ability to print barcodes on the refill request form and on the multi-RX request form. The Kernel group responsible for the TERMINAL TYPE file (#3.2) has defined two new fields. To use the barcode capability, you should define new terminal types, for example, P-DS220 BARCODER and P-MT290 BARCODER. All parameters for these new types should be the same as those for the corresponding terminal type without the barcode capability. The two new fields (BAR CODE ON and BAR CODE OFF) should be entered.

<u>For the Data South 220</u>:

BAR CODE ON =

\*27,"\$70s",\*97,"H",\$S('\$D(X):"04",X="M":"04",X="S":"02",X="L":"10",1:"04"),\*94, "BDB"

3.  The letter following the \$70 is a lower-cases. BAR CODE OFF =\*94,"G",\*27,"\$70c".

BAR CODE OFF =\*94,"G",\*27,"\$70c"

4.  The letter following the \$70 is a lower-case c.

<u>For the Data South XL300 DD</u>:

BAR CODE ON =

\*27,"\[lw",\*27,\$s70",\*94,"H",\$S('\$D(X):"04",X="M":"04",X="S":"02",X="L":"10",1: "04"),\*94,"BDB"

BAR CODE OFF=\*94,"G",\*27,"\$c70",\*27,"\[2w",!

<u>For the MT-290</u>:

BAR CODE ON =

\*26,"F0",\$S('\$D(X):2,X="M":2,X="S":1,X="L":6,1:2),";000",\*25,\*20,"\*"

BAR CODE OFF = "\*",\*20,!,?\$S(\$D(X1):X1,1:0),\$S(\$D(X2):X2,1:"")

<u>For the OTC-560</u>:

BAR CODE ON =\*27,"\[;",\$S('\$D(X):3,X="M":6,X="L":12,1:3),"}",\*27,"\[3t"

BAR CODE OFF = \*27,"\[0t"

<u>For the GENICOM 4440</u>:

BAR CODE ON =\*27,"\[;",\$S('\$D(X):3,X="M":6,X="L":12,1:3),"}",\*27,"\[3t" BAR CODE OFF = \*27,"\[0t"

In the DEVICE file (#3.5), each pharmacy label printer should have the appropriate entries in both the SUBTYPE and DEFAULT SUBTYPE fields.

On the printers, the form length must be set to 24 lines. This is feature 2 on the DS-220 and part of the main menu for the MT-290. Additionally, feature 46 on the DS-220, ESCAPE SEQUENCE DISABLE, must be set to 0 and the MT-290 must have the required barcode cartridge installed.

Barcodes can only be printed on the four-inch labels. If you are still using the older three-inch labels, you cannot print barcodes.

While this section describes printing of barcodes on only the OTC-560, GENICOM- 4440, DS-220, and MT-290 printers, the function is device independent and can be used with any printer which can print barcodes and which can be set for a form length of either four inches or 24 lines. The following information is intended as a guide for setting up the barcode fields for other printers.

<u>For the DATASOUTH-200</u>:

BAR CODE ON=

\*27,"\[1w",\*27,"\$70s",\*94,"H",\$S('\$D(X):"04",X="M":"04",X="S":"02",X="L":" 10",1:"04"),\*94,"BDB"

BAR CODE OFF=\*94,"G",\*27,"\$70c",\*27,"\[2w",!

<u>For the MT-661</u>:

BAR CODE ON=

\*27,"\[\<4h",\*94,\$S(\$X\<60:"T450",1:"T850"),\*94,"W9;5;1",\*94,"B1;35;1;3",\*13

BAR CODE OFF=\*13,\*10,\*27,"\[\<4l",\*27,"\[5w"

5.  The character after the \[4 in the BAR CODE OFF above is a lower-case L.

<u>For the DATASOUTH A600</u>:

BAR CODE OFF=\$C(94),"\*",\$C(94),"PN"

BAR CODE ON=\$C(94),"PY",\$C(94),"M",\$C(94),"H03",\$C(94),\$S(\$X\<80:"T0450"

,1:"T0850"),\$C(94),"BYB"

<u>For the DATASOUTH XL400</u>:

BAR CODE OFF=\*94,"G",\*27,"\$70c"

BAR CODE ON=\*27,"\$70s",\*94,"H",\$S('\$D(X):"04",X="M":"04",X="S":"02",X="L":"1 0",1:"04"),\*94,"BDB"

<u>For the DATASOUTH PERFORMAX AS-600</u>:

BAR CODE OFF=\$C(94),"\*",\$C(94),"PN"

BAR CODE ON=\$C(94),"PY",\$C(94),"M",\$C(94),"H03",\$C(94),\$S(\$X\<80:"T0450"

Each of the two fields is the argument of a MUMPS Write command.

Three parameters are used.

X is the barcode height. Values can be S, M, or L. If X is undefined or not equal to one of these, the default value of S is used. S is 2/10 inch for the DS-220 and 1/6 inch for the MT-290. M is 4/10 inch for the DS-200 and 1/3 inch for the MT-290. L is one inch for both.

X1 is the value of \$X at the left edge of the barcode. If X1 is undefined, the default value of 0 is used.

X2 is the data to be bar-coded. Remember that the code 39-character set which is being used by the VA is a limited subset of the ASCII character set containing only the numbers, upper case letters and eight punctuation characters. In most cases, any other characters are not printed. For example, the barcode for the string “123abc” will be the same as that for the string “123.”

On most printers, printing a barcode is a graphics operation which causes the value of \$Y to be something other than the line count from the top of the page. Forms with barcodes on them must use a form feed to go to the top of the next form rather than a counted number of line feeds. This is the reason that printers being used to print barcodes on outpatient pharmacy labels must be set for a form length of 24 lines or four inches.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package requires the 21 files listed below. Information about the files can be obtained by using the VA FileMan to generate a list of file attributes.

The Data Dictionaries (DDs) are considered part of the online documentation for this software application. Use VA FileMan option List File Attributes \[DILIST\], under Data Dictionary Utilities \[DI DDU\], to print the DDs.

The following are the files for which you should print DDs.

## Outpatient Pharmacy Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File  | Name                  | Up Date Dd | Send Sec. Code | Data Comes W/File | Site Data | Rslv Pts | User Over Ride |
|-------|-----------------------|------------|----------------|-------------------|-----------|----------|----------------|
| 550   | CMOP SYSTEM           | YES        | YES            | NO                |           |          |                |
| 550.1 | CMOP RX QUEUE         | YES        | YES            | NO                |           |          |                |
| 550.2 | CMOP TRANSMISSION     | YES        | YES            | NO                |           |          |                |
| 552   | CMOP NATIONAL SITE    | YES        | YES            | NO                |           |          |                |
| 552.1 | CMOP REFERENCE        | YES        | YES            | NO                |           |          |                |
| 552.2 | CMOP DATABASE         | YES        | YES            | NO                |           |          |                |
| 552.3 | CMOP RELEASE          | YES        | YES            | NO                |           |          |                |
| 552.4 | CMOP MASTER DATABASE  | YES        | YES            | NO                |           |          |                |
| 552.5 | CMOP COST STATS       | YES        | YES            | NO                |           |          |                |
| 553   | CMOP INTERFACE        | YES        | YES            | NO                |           |          |                |
| 553.1 | CMOP LOG              | YES        | YES            | NO                |           |          |                |
| 554   | CMOP OPERATIONS       | YES        | YES            | NO                |           |          |                |
| 555   | CMOP DATABASE ARCHIVE | YES        | YES            | NO                |           |          |                |
| 50    | DRUG                  | YES        | YES            | NO                |           |          |                |
| 50.6  | NATIONAL DRUG         | YES        | YES            | YES               |           |          |                |
| 51.5  | ORDER UNIT            | YES        | YES            | YES               |           |          |                |
| 52    | PRESCRIPTION          | YES        | YES            | NO                |           |          |                |
| 52.5  | RX SUSPENSE           | YES        | YES            | NO                |           |          |                |
| 54    | RX CONSULT            | YES        | YES            | YES               |           |          |                |

<span id="_Toc84256335" class="anchor"></span>Table 7: Package Export Menus

The namespace for the Consolidated Mail Outpatient Pharmacy package is PSX.

# Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of routines you will see for Consolidated Mail Outpatient Pharmacy (including those patched through PSX\*2\*48) when you load the new routine set. The first line of each routine contains a brief description of the general function of the routine. Use the First Line Routine Print \[XU FIRST LINE PRINT\] option found within the Kernel Routine Tools \[XUPR-ROUTINE-TOOLS\] menu to print the first line description of each PSX\* routine.

PSX41NDX

PSX41PRE

PSX41PST

PSX550

PSXACK

PSXACT

PSXARC

PSXARC1

PSXARC2

PSXARPT

PSXATREJ

PSXAUTO

PSXAUTOC

PSXBKD

PSXBKG

PSXBLD

PSXBLD1

PSXBPSMS

PSXBPSR1

PSXBPSRP

PSXBPSUT

PSXCH

PSXCHENV

PSXCMOP

PSXCMOP0

PSXCMOP1

PSXCOSTU

PSXCRENV

PSXCSCMN

PSXCSDA

PSXCSDC

PSXCSDC1

PSXCSDC2

PSXCSHI

PSXCSHI1

PSXCSLG1

PSXCSLOG

PSXCSMN1

PSXCSMON

PSXCSSUM

PSXCST

PSXCST1

PSXCSTPG

PSXCSUTL

PSXDB

PSXDENT

PSXDODAC

PSXDODAK

PSXDODAT

PSXDODB

PSXDODB1

PSXDODFX

PSXDODH

PSXDODH1

PSXDODNT

PSXDODQY

PSXDQUE

PSXDQUEC

PSXDRPT

PSXDUAL

PSXEDIT

PSXEDRG

PSXEDUTL

PSXERR

PSXERR1

PSXHENV

PSXHL7

PSXHL71

PSXHSYS

PSXHSYS1

PSXJOB

PSXLBL

PSXLBL1

PSXLBL2

PSXLBLNR

PSXLBLPT

PSXLBLT

PSXLBLU

PSXLIST

PSXLKUP

PSXLM1

PSXLTST

PSXMISC

PSXMISC1

PSXMSGS

PSXMST

PSXNEW

PSXNOCMP

PSXNOTE

PSXOCMOP

PSXOPUTL

PSXPLOG

PSXPOST

PSXPOST1

PSXPST32

PSXPURG

PSXPURG1

PSXQRY

PSXQUE

PSXRACT

PSXRCVRY

PSXRECV

PSXRECV1

PSXREF

PSXREJ

PSXREL

PSXRENV

PSXRESUB

PSXRHLP

PSXRPPL

PSXRPPL1

PSXRPPL2

PSXRPT

PSXRSTAT

PSXRSUS

PSXRSUS1

PSXRSYU

PSXRTN

PSXRTN1

PSXRTR

PSXRTRA1

PSXRTRAN

PSXRTRAO

PSXRXQU

PSXRXU

PSXSERV

PSXSITE

PSXSMRY

PSXSND

PSXSRP

PSXSRST

PSXSTAT

PSXSTP

PSXSTRT

PSXSUDCN

PSXSYS

PSXTL

PSXTNRPT

PSXUNHLD

PSXUNREL

PSXUTL

PSXVCK

PSXVCK1

PSXVEND

PSXVIEW

PSXVND

PSXVPN

# # Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package exports the following menus. These menus should be assigned at the discretion of the CMOP Manager at the host CMOP and the Chief of Pharmacy at the remote medical centers.

<table>
<caption><p><span id="_Toc84256336" class="anchor"></span>Table 8: Remote Medical Center</p></caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Package Exports</th>
<th>Menus</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Remote Medical Centers</td>
<td><ul>
<li><blockquote>
<p>CMOP Site Manager Menu</p>
</blockquote></li>
<li><blockquote>
<p>CMOP Drug/Item Management</p>
</blockquote></li>
<li><blockquote>
<p>Reports Menu</p>
</blockquote></li>
<li><blockquote>
<p>Transmission Menu</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>CMOP Host Facilities</td>
<td><ul>
<li><blockquote>
<p>CMOP System Management Menu</p>
</blockquote></li>
<li><blockquote>
<p>Interface Menu</p>
</blockquote></li>
<li><blockquote>
<p>Operations Menu</p>
</blockquote></li>
<li><blockquote>
<p>Reports</p>
</blockquote></li>
<li><blockquote>
<p>CMOP Drug/Item Management</p>
</blockquote></li>
<li><blockquote>
<p>Facility Cost Management</p>
</blockquote></li>
<li><blockquote>
<p>Archive CMOP Data</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc84256336" class="anchor"></span>Table 8: Remote Medical Center

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Host CMOP Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the host CMOP facility a background job will purge the CMOP DATABASE file (#552.2), the CMOP REFERENCE file (#552.1), the CMOP RELEASE file (#552.3),

and the Release Data Acknowledgement from the CMOP OPERATIONS file (#554) on a scheduled basis.

Both the CMOP REFERENCE file (#552.1) and the CMOP DATABASE file (#552.2) are purged by the same job. This job is scheduled by using the Nightly Purge of CMOP Database, \[PSX PURGE CMOP DATABASE\] under the Operations Management menu option on the CMOP System Management Menu. This job should be scheduled to run during non-peak hours to lessen the impact on system operations. Once scheduled, this job will reschedule to run again every 24 hours. This job will purge the data from the SITE TEXT field (#14) in the CMOP REFERENCE file (#552.1), and related data from the CMOP DATABASE file (#552.2) for those transmissions marked as Closed in the STATUS field (#1) of the CMOP REFERENCE file (#552.1).

The purge of the CMOP RELEASE file (#552.3) is scheduled through the Nightly Purge of Release Data, \[PSX PURGE RELEASE\] option under the Operations Management menu on the CMOP System Management Menu. This job should be scheduled to run during non-peak hours to lessen the impact on system operations. Once scheduled, this job will reschedule to run every 24 hours. It will purge all data from the CMOP RELEASE file (#552.3) that is marked as Ready to Purge in the PURGE field (#1).

The purge of the Release Data Acknowledgements from the CMOP OPERATIONS file (#554) is scheduled through the Nightly Purge of Release Data \[PSX PURGE RELEASE\] option under the Operations Management menu on the CMOP System Management Menu. This job should be scheduled to run during non-peak hours to lessen the impact on the system’s performance. When scheduling this job, the user is required to enter the number of days of acknowledgements to keep in the file. Once scheduled, this job will reschedule to run every 24 hours.

These three jobs should be scheduled upon installation of the CMOP software. Only one schedule can be set up at a time for these jobs. If the system has to be shut down, these three jobs should be unscheduled first. They can be unscheduled using the same options used to set up the schedule. Once the system is brought back up, these jobs should be rescheduled again. If the system goes down, these jobs should be rescheduled once the system is restored.

## Remote Medical Center

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the remote medical center’s transmission data is stored in the CMOP RX QUEUE file (#550.1). The data is maintained until it is successfully downloaded to the vendor system. This file is purged automatically when the remote medical center receives an acknowledgement from the CMOP indicating that the data has been received by the vendor system.

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None of the CMOP routines have been designed to be called outside of the package.

# Routine Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No recommendations are made for routine mapping.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version (2.0) of Consolidated Mail Outpatient Pharmacy requires, at least, the following VA software applications.

| Software Application     | Minimum Version Required |
|--------------------------|--------------------------|
| Kernel                   | 8.0                      |
| MailMan                  | 7.1                      |
| VA FileMan               | 21.0                     |
| National Drug File (NDF) | 3.16                     |
| Outpatient Pharmacy (OP) | 7.0                      |

<span id="_Toc84256337" class="anchor"></span>Table 9: Host Facility

| Software Application     | Minimum Version Required |
|--------------------------|--------------------------|
| Kernel                   | 8.0                      |
| MailMan                  | 7.1                      |
| VA FileMan               | 21.0                     |
| National Drug File (NDF) | 3.16                     |

<span id="_Toc84256338" class="anchor"></span>Table 10: Remote Medical Center

## MailMan Issues Related to CMOP Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful operation of the CMOP software is highly dependent on MailMan processing of the communications between the software and the user. The developer recommends that the medical centers and CMOP host facilities use TCP/IP for the best results.

Mail messages are used extensively to relate the status of jobs, deliver reports, and advise users of data or transmission problems. The transmission mechanism for prescription data is the MailMan server option S.PSXX CMOP SERVER. MailMan delivers data to this option, which queues numerous background jobs to handle processing and releasing of prescriptions. Information Resources Management (IRM) should note that problems with MailMan may directly impact on the performance of the CMOP software.

## Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Consolidated Mail Outpatient Pharmacy (CMOP) V. 2.0 has Integration Agreements with Outpatient Pharmacy, National Drug File, Pharmacy Data Management, and VA FileMan. For complete information regarding the Integration Agreements for CMOP V. 2.0, please refer to the DBA menu option on FORUM and then the Integration Agreement menu.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package does not require a SACC agreement.

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This package does not contain any package-wide variables.

# On-Line Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout the entire Consolidated Mail Outpatient Pharmacy package, you may obtain on-line help. You may enter a question mark (?) at any prompt to assist you in your choice of actions.

The Data Dictionaries (DDs) are considered part of the on-line documentation for this software application. Use VA FileMan option List File Attributes, under Data Dictionary Utilities, to print the DDs.

The following are the files for which you should print DDs:

| File Numbers | File Names        |
|--------------|-------------------|
| 550          | CMOP SYSTEM       |
| 550.1        | CMOP RX QUEUE     |
| 550.2        | CMOP TRANSMISSION |
| 50           | DRUG              |
| 50.6         | NATIONAL DRUG     |
| 51.5         | ORDER UNIT        |
| 52           | PRESCRIPTION      |
| 52.5         | RX SUSPENSE       |
| 54           | RX CONSULT        |

<span id="_Toc84256339" class="anchor"></span>Table 11: Host Facility

| File Numbers | File Names                   |
|--------------|------------------------------|
| 552          | CMOP NATIONAL SITE           |
| 552.1        | CMOP REFERENCE               |
| 552.2        | CMOP DATABASE                |
| 552.3        | CMOP RELEASE                 |
| 552.4        | CMOP MASTER DATABASE         |
| 552.5        | CMOP COST STATS              |
| 553          | CMOP INTERFACE               |
| 553.1        | CMOP QUERY                   |
| 554          | CMOP OPERATIONS              |
| 555          | CMOP MASTER DATABASE ARCHIVE |
| 50           | DRUG                         |
| 50.6         | NATIONAL DRUG                |
| 51.5         | ORDER UNIT                   |
| 54           | RX CONSULT                   |

<span id="_Toc84256340" class="anchor"></span>Table 12: Control Sequences

The namespace for the Consolidated Mail Outpatient Pharmacy package is PSX.

## Journaling Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Journaling of the PSX global is recommended.

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Input</u>

PSX DRUG - This input template is used by CMOP to enter/edit data in DRUG file (#50).

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym                  | Meaning                                                                                                                                                                                                                                                                                                          |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Activity Log             | A log, by date, of changes made to or actions taken on a prescription. An entry is made in this log each time the prescription is edited, cancelled, reinstated after being cancelled, or renewed. An entry will be made into this log when the Rx is suspended for CMOP and when the Rx is transmitted to CMOP. |
| CMOP                     | Acronym for Consolidated Mail Outpatient Pharmacy.                                                                                                                                                                                                                                                               |
| CMOP Indicator           | The CMOP indicator is the status of the CMOP Rx in suspense.                                                                                                                                                                                                                                                     |
| Expiration               | The date on which a prescription is no longer active.                                                                                                                                                                                                                                                            |
| Host                     | A host is a CMOP facility that receives prescription data and fills and mails the prescriptions to the veteran.                                                                                                                                                                                                  |
| Issue Date               | The date on which the prescription was written. This date is usually, but not always, the same as the first fill date. This date cannot be later than the first fill date.                                                                                                                                       |
| Prescription Index Field | The PRESCRIPTION INDEX field of the RX1 segment is the unique key used to identify an individual prescription. It contains the Facility ID, Rx Number, and the Fill Number of a previously received prescription.                                                                                                |
| Remote Medical Center    | A remote medical center is a VAMC outpatient pharmacy that transmits prescription data to the host CMOP for filling and mailing.                                                                                                                                                                                 |
| Sig                      | The instructions printed on the label.                                                                                                                                                                                                                                                                           |
| Suspense                 | A prescription may not be able to be filled on the day it was requested. When the prescription is entered, a label is not printed. Rather, the prescription is put in the RX SUSPENSE file (#52.5) to be printed at a later date.                                                                                |
| VistA                    | Acronym for Veterans Health Information Systems and Technology Architecture.                                                                                                                                                                                                                                     |
<span id="_Toc84256341" class="anchor"></span>Table 13: Message Header

# Appendix A—Consolidated Mail Outpatient Pharmacy Communications Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document defines the communications protocol required to form the basis for the exchange of information between the VistA Consolidated Mail Outpatient Pharmacy (CMOP) system interface and the vendor PC system. The communication protocol used for interfacing with the VistA CMOP package will be based on the ANSI X3.28 Data Link Protocol as described in Appendix B of the Health Industry Level 7 (HL7) Interface Standard Document Version 2.1. All further references to HL7 in this document refer to the Health Industry Level 7 Interface Standard (version 2.1) publication unless otherwise indicated.

The ANSI X3.28-1976 Data Link Protocol is available from

American National Standards, Inc.  
1430 Broadway  
REDACTED, NY 10018 (212) 642-4900

The following X3.28 options are used

Establishment and termination Subcategory 2.3: Two way Alternating, Nonswitched Point-to-Point.

Message Transfer Subcategory B1: Message-Associated Blocking, with Longitudinal Checking and Single Acknowledgments.

Termination Interrupt (3.4.3).

An additional feature not covered in the X3.28 standard, but used in this protocol:

A line check (timer E) provides early warning of communications link problems.

### Requirements & Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  This protocol must support a point-to-point connection with guaranteed delivery (does not guarantee processing).
2.  Only one physical line is required to accommodate the request and (application level) reply for a given remote operation.
3.  The data link protocol must allow different types of remote operations to be sent over a single physical line. (Data link acknowledgment of a message cannot wait for the application level reply. This would hang the link and prevent all types of messages from being delivered.) Positive Acknowledgments (ACKs) must be sent independently of any application reply.
4.  Block transmissions and responses must be synchronous.
5.  Either side can detect when the communications link is non-operational.
6.  Before ACKing a message received by a system, the message is either:
1.  Placed in reliable storage.
2.  Delivered to an application process, where the message will be processed before it is acknowledged.

### Environment Model

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following model and guidelines are used with this protocol to support the stated requirements and assumptions.

The job of the communication modules which implement this protocol is to take a message from a single source and deliver it intact to a single destination.

The communications protocol is a delivery mechanism and does not process the data content of the messages it transfers. The application processing of the data is performed at a higher level and should not be confused with the communications protocol described here.

## Communication Control Characters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table defines the communication control sequences. A brief description of each sequence follows the table. References to these control sequences are used in describing the protocol throughout this document.

### Control Sequences

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Abbreviation | Characters | Actual Bytes (hex) | Decimal     |
|--------------|------------|--------------------|-------------|
| TERM         | CR         | 0D                 | 13          |
| STX          | STX        | 02                 | 2           |
| ETB          | ETB        | 17                 | 23          |
| ETX          | ETX        | 03                 | 3           |
| EOT          | EOT        | 04                 | 4\*     |
| ENQ          | ENQ        | 05                 | 5\*     |
| NAK          | NAK        | 15                 | 21\*    |
| ACK0         | DLE 0      | 10 30              | 16,48\* |
| ACK1         | DLE 1      | 10 31              | 16,49\* |
| ACK2         | DLE 2      | 10 32              | 16,50\* |
| ACK3         | DLE 3      | 10 33              | 16,51\* |
| ACK4         | DLE 4      | 10 34              | 16,52\* |
| ACK5         | DLE 5      | 10 35              | 16,53\* |
| ACK6         | DLE 6      | 10 36              | 16,54\* |
| ACK7         | DLE 7      | 10 37              | 16,55\* |

<span id="_Toc84256342" class="anchor"></span>Table 14: PID

6.  This control sequence is always followed by a carriage return character, 0D.

STX (Start of Text)

STX precedes a sequence of characters that are to be treated as an entity and entirely transmitted through to the ultimate destination. Such a sequence is referred to as a “text.” If the text is subdivided into transmission blocks, STX delimits the start of each block that continues transmission of the text.

ETX (End of Text)

ETX delimits the end of a message text. In multi-block messages, ETX indicates the last block of the message.

ETB (End of Block)

ETB delimits the end of a block which is not the last block of a message.

EOT (End of Transmission)

EOT indicates the conclusion of a transmission that contained one or more message texts.

EOT cancels any previous master/slave relationship.

EOT is sent by a master station after the completion of the message transfer phase to cause a normal termination of the current master/slave relationship.

EOT is sent by a slave station in place of ACK/NAK in order to effect a termination interrupt function. It serves to Negative Acknowledgment (NAK) the current block and causes the current master/slave relationship to be ended.

ENQ (Enquiry)

ENQ is used by either station to request master status.

ENQ is used during the message transfer phase by the master station to indicate that the last response reviewed from the slave station was not understood and should send the last ACK or NAK.

NAK (Negative Acknowledgment)

NAK is transmitted as a negative response to received messages.

During the master/slave establishment phase, NAK is used to indicate that the station is not ready to receive.

During message transfer, NAK indicates that the last received message block was not accepted, but the station is ready to receive, and the master should retransmit.

ACK (Positive Acknowledgment)

During the master/slave establishment phase, ACK is used to indicate that the station is ready to receive.

During message transfer, ACK is transmitted by a slave station as an affirmative reply to a transmission block.

### Block Number (BLK)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The number used to sequence message blocks. It immediately follows the start-of-block (STX) delimiter. The BLK character is a single ASCII numeric character (0, 1, 2, 3, 4, 5, 6, 7). The first transmission block is assigned the numeric character one (hex 31).

### Text Length (TL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A decimal number in ASCII characters which represents the number of bytes of message text present in the block. It is always five characters long, right justified, and zero filled.

### Block Checking Characters (BCC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two block check characters (BCC) are added at the end of each transmission block to facilitate error detection. The BCC is generated as follows:

Take the Exclusive-Or of all the characters in the block, starting with the character following STX, and ending with (and including) the character just prior to the BCC characters. Convert the resulting binary value to a two-character hexadecimal ASCII representation.

For example, to send the message text “HL7 is great!,” the general message format of:

STX BLK TL \<Text of Message\> ETX BCC CR

would be encoded as the hexadecimal byte values:

STX 02

BLK1 31 (“1”) (BCC starts here, inclusive)

0 30

0 30

0 30

1 31

3 33

H 48

L 4C

7 37

20

i 69

s 73

20

g 67

r 72

e 65

a 61

t 74

! 21

ETX 03 (BCC ends here, inclusive)

6 36

D 44

CR 0D

where the BCC is calculated as the Exclusive-Or of the check summed bytes: 31, 30, 30, 30, 31, 33, 48, 4C, 37, 20, 69, 73, 20, 67, 72, 65, 61, 74, 21, 03=6D.

The ASCII characters 6D are used as the BCC above.

## Establishment of Master / Slave Relationship

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before the establishment of a master / slave relationship, neither station is able to send. Either station may request control of the line to become the master (sender). It is the responsibility of the master stations to give up its master status when it no longer has data to send.

When the line is idle and a station desires to transmit a message, that station requests control of the line (master status) by sending a ENQ sequence to the remote station. It is possible for both stations to bid for master status at the same time, indicated by receipt of a ENQ in response to sending a ENQ. In this case, both stations enter a timeout period.

The station designated as Primary will timeout before the other station (which would be designated as the Secondary station) and send its ENQ again.

When one of the stations bids for the line, the following events occur:

One of the stations ENQ.

The other station grants the line to the sending station by responding with an ACK.

The sending station waits for receipt of ACK. If ACK is received before expiration of Timer A, the sending station has been granted master status and begins transmitting the ENQ sequence.

A station that has not sent ENQ, but has received ENQ takes the following action:

Inhibits the sending of ENQ to bid for master status.

If ready to receive, assumes slave status and sends ACK.

If not ready to receive, sends NAK.

Upon receipt of an affirmative reply, the bidding station assumes master status and proceeds with message transfer.

Upon receipt of NAK, the bidding station reinitiates a bid for master status. The station reinitiates its bid M times and then exits to a recovery procedure.

In the case of an invalid or no reply to ENQ, the bidding station reinitiates its bid for master status. The station reinitiates its bid N times. After N unsuccessful bids, the station exits to a recovery procedure.

An exit to the recovery procedures indicates that the remote station is not operational – i.e., busy or down. The recovery procedure will consist of a delay, after which line bidding is resumed.

## Message Transfer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Messages may be subdivided into blocks. A transmission block may be a complete message or a portion of message. The master station sends each transmission block to the slave station and waits for a reply before sending the next block.

If the reply indicates that the block was accepted, the master station may send another block, or it may terminate its master status. If the reply is negative, the master station immediately retransmits the block that was not accepted.

### Transmission Blocks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The transmission of blocks is initiated by the master after a master/slave relationship has been established. The master station begins the first transmission block and all subsequent blocks with STX.

A block that ends at an intermediate point within the message is ended with ETB. A block that ends at the end of a message is ended with ETX. The ETB and ETX characters are immediately followed by the Block Check Characters (BCC). After the ETB or ETX and BCC are sent, the master station waits for a reply.

### Replies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The slave station, upon detecting the ETB or ETX followed by the BCC, determines whether it will send ACK or NAK. It verifies that a block was received correctly by checking that:

1.  The message terminated with TERM.
2.  The calculated BCC matches the BCC in the message.
3.  The number of bytes in the message text matches the Text Length (TL) in the message.
4.  The message text is followed by either an ETB or ETX.

The receiver checks the block sequence number (BLK) to detect duplicate or missing blocks.

ACK If the transmission block was accepted and the slave station is ready to receive another block, it sends ACK. Upon detecting the ACK, the master station may either transmit the next block, or initiate termination of master status if the last block ended in ETX BCC.

NAK If the transmission block was not accepted and the slave station is ready to receive another block, it sends a NAK. Upon detecting a NAK, the master station initiates retransmission of the last transmitted block. L transmissions may be made, after which the master station exits to a recovery procedure.

> A message block is acknowledged as soon as the receiving buffer is available to receive the next block. Flow control (XON, XOFF) is not needed since a synchronous block acknowledgment scheme is used and a receiver’s buffer is guaranteed to hold a block of maximum block size.

## Interrupts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At times during data exchange, the receiving station may wish to cause the sending station to quit sending. This procedure is called an interrupt. The interrupt is accomplished by the receiving station transmitting EOT in lieu of one of its normal responses. This response indicates a negative acknowledgment of the last block and the termination of the current master/slave relationship.

## Timers and Recovery Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Timers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Timers are used to ensure that a station can recognize the non-occurrence on an event, such as an incomplete message or no response to a transmitted block. Note that the timers specified in this section are fundamental only and do not necessarily imply a specific implementation.

Logging and/or operator notification of timeouts should be done to aid in the maintenance and troubleshooting of the interface.

#### Timer A (Response Timer)

Timer A is used by the sending station to protect against an invalid response or no response. Timer A is started after the transmission of the last character of a block or after sending ENQ. Timer A is stopped upon receipt of a valid reply (ACK, NAK, or EOT).

The value for Timer A includes the response time of the receiver plus the time to transmit the acknowledgment sequence. It should be slightly longer than Timer B.

If timeout occurs while sending a block, the sending station either:

Retransmits the block (up to N times) or

follows the Sending Station Abort procedures by transmitting EOT ENQ.

#### Timer B (Receive Timer)

A slave station uses Timer B to protect against failure to recognize the end of a block (ETB or ETX). Timer B is started upon receipt of STX. Timer B is stopped upon receipt of a valid terminating character or sequence, ETB or ETX and BCC.

If timeout occurs, the receiving station will:

Discard the incomplete block and

respond with EOT and

prepare to receive another line bid.

#### Timer D (Inter-Block Timer)

Timer D serves to prevent a station from hanging in slave mode. Timer D is started when entering slave mode and restarted after replying to each block. Timer D is stopped upon receipt or transmission of EOT.

If timeout occurs, the receiving station will:

Initiate termination interrupt, and

return to control mode.

#### Timer E (Line Check Timer)

Timer E triggers a check of the communications link when neither station has requested to be master for some time. Timer E is reset whenever a transmission is sent or received.

If timeout occurs, the station transmits a EOT ENQ line bid. The line then may be released with (EOT) as soon as master/slave is established.

If no response is received when bidding for the line, the normal mechanism using Timer A will report a problem with the communications link.

### Recovery Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a timeout, invalid, or NAK response to a transmitted block is received, the master station transmits the block again. This may occur up to L times. The recovery procedure after L unsuccessful retransmissions is

Notify the operator or the application program, or both, and

transmit EOT to end the master/slave relationship.

When a timeout, invalid, or NAK response to a line bid (ENQ) is received, the sender transmits ENQ again. This may occur up to L times. The recovery procedures after M unsuccessful retransmission is

Notify the operator or the application program, or both, and

the sender may continue to request the line by sending ENQ with an appropriate delay between requests.

# Appendix B—Consolidated Mail Outpatient Pharmacy Application Message Definition Statement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document defines the application-level messages required to form the basis for the exchange of information between the VistA Consolidated Mail Outpatient Pharmacy (CMOP) system interface and the vendor PC system. The communication protocol used for interfacing with the VistA CMOP package will be based on the ANSI X3.28 Data Link Protocol as described in Appendix B of the Health Industry Level 7 (HL7) Interface Standard Document Version 2.1. All further references to HL7 in this document refer to the Health Industry Level 7 Interface Standard (version 2.1) publication unless otherwise indicated.

The HL7 protocol describes the exchange of messages in terms of two entities, the initiating and responding systems. Each is both a sender and receiver of messages. The initiating system, VistA, sends first and then receives, while the responding system receives first, then sends. The exchange proceeds as follows:

Initiator, VistA, receives messages from the sending application (CMOP) software and sends it to the responding system.

Responder receives the messages

1.  validates it syntactically against the encoding rules, and if it fails, a reject message is constructed by the protocol software and returned to the initiator.
2.  passes it to the application, which
1)  creates a response message, or
2)  creates an error message, or
3)  creates a reject message
3.  sends the response, error, or reject message to the initiator.

The initiating application process creates a message with data values as defined by HL7. The message is encoded and sent to the lower level protocols, which deliver it to the responding application. The responding application accepts the message, validates it, and if it fails the protocol software rejects the message. That is, it creates an ACK message with “AR” in the Acknowledgment Code. If the message processes successfully, the functional response message (MSA) contains an “AA” in the Acknowledgment Code. If the error is detected in one of the segments the MSA segment should contain an “AE” in the Acknowledgment Code. However, if the responding application fails to process (rejects) the message for reasons unrelated to its content or format (system, down, internal error, etc.) the MSA segment should contain an “AR” in Acknowledgment Code. The protocol software then passes the response message to the initiating system. (Refer to HL7, II-11 for a description of the values and construction of the MSA segment).

A message is the unit of data transferred between systems. It is comprised of a “group of segments” in a defined sequence. Each message (or segment) has a message type that defines its purpose. All message (or segment) types beginning with Z are reserved for locally defined messages or segments, and as such, are not defined in HL7. Segments are logical groupings of data fields; segments of a message may be required or optional. They may occur only once in a message or they may be allowed to repeat. Each segment is given a name and is identified by a unique three-character code known as the Segment ID.

## Overview of Message Encoding and Construction Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In constructing a message certain special characters are used. They are the segment terminator, the field separator, the component separator, subcomponent separator, and the repetition separator. The segment terminator is the last character of every segment. It is always the ASCII CR character (hex ØD). The characters recommended by HL7 and used in this application are

Field separator character “\|”

Component separator character “^”

SubComponent separator character “&”

Repetition separator character “~”

Escape character “\\

The field separator character is always the “fourth” character of the MSH segment. The component separator is the “first” character in the Encoding character data field of the MSH segment. The repetition separator is the “second” character in the Encoding Characters field, the escape character is “third”, and the subcomponent separator is the fourth in the Encoding Characters data field of the MSH segment. The Control Section, Chapter II of the HL7 Standard describes fully the encoding and construction rules for the HL7 messages.

The following pages define the segments, data fields, and sequences used to construct the HL7 messages for the CMOP application.

### Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following HL7 messages will be used to support the exchange of CMOP Information.

ACK General Acknowledgment

ORM Order

QRY Query

ORF Observation Result/Record Response

### Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following HL7 segments will be used to support the exchange of CMOP information.

BHS Batch Header

BTS Batch Trailer

MSA Message Acknowledgment

MSH Message Header

NTE Notes and Comments

PID Patient Identification

ORC Common Order

RX1 Pharmacy Order

ZX1 Pharmacy Order (Application defined)

QRD Query Definition

The segment definition tables list and describe the data fields in the segments and characteristics of their usage. The following information is specified about each data field:

Sequence \# (SEQ): the ordinal position of the data field within the segment.

Length (LEN): the maximum number of characters that one occurrence of the data field may occupy in any message.

Data Type (DT): restrictions on the contents of the data field as defined in the HL7 standard.

Optionality (R/O): whether the field in the segment is required or optional. The designations are:

R: required

0 (or null): optional

Repetition (RP/#): whether the field in the segment may repeat. The designations are:

N (null): no repetition allowed.

The field may repeat an indefinite or site determined number of times (integer). The field may repeat up to the number of times specified in the integer.

Element Name: identifies the contents of the data field.

The following pages define the segments, data fields, and sequences used to construct the HL7 messages for the CMOP application.

## Message Header Segment—MSH

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Message Header Segment defines the intent, source, destination, and some specifics of the syntax of a message.

| Segment | SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME          |
|---------|------|-----|-----|-----|-----|-----------------------|
| MSH     | 1    | 1   | ST  | R   |     | Field Separator       |
|         | 2    | 4   | ST  | R   |     | Encoding Characters   |
|         | 3    | 15  | ST  |     |     | Sending Application   |
|         | 5    | 15  | ST  |     |     | Receiving Application |
|         | 7    | 19  | TS  |     |     | Date/Time of Message  |
|         | 9    | 7   | ID  | R   |     | Message Type          |
|         | 10   | 20  | ST  | R   |     | Message Control ID    |
|         | 11   | 1   | ID  | R   |     | Processing ID         |
|         | 12   | 8   | NM  | R   |     | Version ID            |

<span id="_Toc84256343" class="anchor"></span>Table 15: Segment Definitions

The contents of the message header segment follow:

Segment ID: identifies the type of segment (MSH)

Field separator: defines the character to be used as a field separator for the rest of the message (\|).

Encoding Characters: four characters, the component separator, the repetition separator and the escape character, and the sub-component separator. (^~\\).

Sending Application: name of application transmitting to CMOP (VistA).

Receiving Application: name of receiving application (i.e., Vendor).

Message Type: identifies the segment as an order message (ORM).

Message Control ID: number of other identifiers that “uniquely” identifies the message. This identifier is echoed back by the receiving system in the Message Acknowledgment. The Message Control ID contains the facility identification number, the transmission number from the CMOP TRANSMISSION file (#550.2), and the sequence number from the CMOP RX QUEUE file (#550.1) in the form: VAMC Station \# - Transmission \# - Sequence \#.

Processing ID: define the type of processing according to the selected communication protocol. (P=Production).

Version ID: Identifies the version of the communication protocol to be matched to the receiving system’s own version to ensure the message will be interpreted correctly.

<u>Example MSH segment</u>:

MSH\|^~\\\|DHCP\|\|VENDOR\|\|199209150415\|\|ORM\|106-247-2567\|P\|2.1\|

## Patient Identification Segment—PID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Identification Segment is used as the primary means of communicating patient identification information, which for the most part is not likely to change.

| Segment | SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME               |
|---------|------|-----|-----|-----|-----|----------------------------|
| PID     | 3    | 16  | CK  | R   |     | Patient ID (Internal ID)   |
|         | 5    | 48  | PN  | R   |     | Patient Name               |
|         | 11   | 106 | AD  | R   |     | Patient Address            |
|         | 13   | 18  | PH  | O   |     | Phone Number               |
|         | 14   | 1   | NM  | O   |     | Other Language PMI Flag    |
|         | 17   | 17  | ST  | O   |     | Integration Control Number |

<span id="_Toc84256344" class="anchor"></span>Table 16: RX1 Segment Definition

Contents of the patient identification segment are:

Segment ID: identifies type of segment (PID).

Patient ID: social security number (see HL7 encoding rules).

Patient Name: identifies the patient (see HL7 encoding rules). Patient Address—mailing location for patient order.

Phone Number: home phone number.

Other Language PMI Flag: denotes in which language to print the PMI; numeric unless the CMOP WARNING LABEL SOURCE is set to “New”, and then is either ENG for English or SPA for Spanish.

Integration Control Number : sent if it is a nationally assigned number.

<u>Example of PID segment</u>:

PID\|\|\|000579013^1^M11\|\|CMOPPATIENT3^ONE\|\|\|\|\|\|123 OAK ST.^REDACTED^TX^75024\|\|(555)555-5555\|1

When the CMOP WARNING LABEL SOURCE is "New", the PMI preference will be sent as “ENG” for English or “SPA” for Spanish instead of the current numeric values.

<u>Example of PID segment (when CMOP WARNING LABEL SOURCE = NEW):</u>

PID\|\|\|000579013^1^M11\|\|CMOPPATIENT3^ONE\|\|\|\|\|\|123 OAK ST.^REDACTED^TX^75024\|\|(555)555-5555\|ENG\|\|\|1000000001V012345

## Common Order Segment—ORC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The common order segment may consist of data common to all orders for the patient. The order control data field defines the function of the order segment. For this application this segment serves to mark the beginning of a new prescription/item order for the patient. It consists of only the segment ID and the order control data field indicating a new order.

All order segments must be preceded by an ORC segment.

| Segment | SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME  |
|---------|------|-----|-----|-----|-----|---------------|
| ORC     | 1    | 2   | ST  | R   |     | Order Control |

<span id="_Toc84256345" class="anchor"></span>Table 17: ZX1 Segment Definition

<u>Example ORC segment</u>:

ORC\|NW\|

## Pharmacy Order Segments—RX1, ZX1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two segments are used by this application to complete a pharmacy order. These are the RX1 pharmacy segment, defined by HL7, and the ZX1 application defined segment.

These segments occur only once for each pharmacy order and always follow an ORC segment. Multiple orders (ORC, RX1, ZX1 combination) may be present for each patient order message.

| Segment | SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME              |
|---------|------|-----|-----|-----|-----|---------------------------|
| RX1     | 1    | 20  | TX  | R   |     | Prescription Index        |
|         | 12   | 11  | CQ  | R   |     | Quantity Dispensed        |
|         | 14   | 48  | CE  | R   |     | Drug ID (locally defined) |
|         | 19   | 3   | NM  |     |     | Number of Refills         |
|         | 20   | 8   | DT  | R   |     | Issue Date                |
|         | 21   | 3   | NM  |     |     | Refills Remaining         |
|         | 24   | 8   | DT  | R   |     | Expiration Date           |
|         | 25   | 8   | DT  |     |     | Last Refill Date          |
|         | 26   | 20  | ST  | R   |     | Rx Number                 |
|         | 30   | 80  | TX  | R   |     | Instructions (SIG)        |

<span id="_Toc84256346" class="anchor"></span>Table 18: General NTE Segment Definition

For purposes of this application, the field length of the data element, Quantity Dispensed has been expanded to 11 to allow for a maximum quantity of 8 significant digits and two decimal digits (nnnnnnnn.nn).

The SIG data element for the RX1 data segment will have the maximum field length of 80 characters. If necessary, immediately following the RX1 will be an NTE (Notes and Comments) segment, which will contain up to the next 100 characters of the SIG data element. If the SIG length exceeds this 80-character limit the NTE segment will repeat as necessary until all of the SIG is transmitted. See the section of this document referring to NTE segments for further description of these segments. The SIG data may also contain instructions in another language.

<u>Example RX1 segment</u>:

RX1\|521-10170-1\|\|\|\|\|\|\|\|\|\|\|30\|\|218A^ RANITIDINE 100mg ^L\|\|\|\|\|5\|19921225\|3\|\|\| 19930630\|19921230\|10170\|\|\|\|TAKE ONE TABLET THREE TIMES A DAY AFTER MEALS

The standard HL7 definitions apply to all data elements except the Drug ID and the Prescription Index. The Drug ID element is locally defined for the CMOP application. The coded element consists of three components: the identifier, the VA Print name, and the coding system name, “L”, indicating this is a locally defined code. The Prescription Index data element is used by the vendor system to determine the existence of a duplicate prescription date at the time the patient order is received. This data element is formatted as follows: facility ID–prescription number–fill number of the prescription.

For the purposes of this application, the data elements, Issue Date (Sequence \#20) and Expiration Date, are present in data fields currently unused by HL7 (V. 2.1). The Issue Date is the date the physician wrote the order, and the Expiration Date is the date the prescription expires.

| Segment | SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME               |
|---------|------|-----|-----|-----|-----|----------------------------|
| ZX1     | 1    | 20  | ST  | R   |     | RX Number                  |
|         | 2    | 48  | CE  | R   |     | Pharmacy Site ID           |
|         | 3    | 1   | ST  | R   |     | Mail Processing ID         |
|         | 4    | 3   | NM  | R   |     | RX count                   |
|         | 5    | 8   | ST  |     |     | Refill text                |
|         | 6    | 30  | ST  | R   |     | Provider/Physician         |
|         | 7    | 1   | NM  |     |     | Registered Mail            |
|         | 8    | 12  | ST  | R   |     | Clerk/Verifying Pharmacist |
|         | 9    | 8   | TS  | R   |     | Fill date (YYYYMMDD)       |
|         | 10   | 1   | NM  |     |     | Copayment ID               |
|         | 11   | 1   | NM  |     |     | Renewable                  |
|         | 12   | 1   | NM  |     |     | Safety Cap                 |
|         | 13   | 3   | NM  | R   |     | Days Supply                |
|         | 14   | 1   | NM  |     |     | Controlled Subs Indicator  |
|         | 15   | 20  | ST  |     |     | Barcode Data               |
|         | 16   | 11  | ST  |     | Y/5 | Warning Message Flag\*     |
|         | 17   | 20  | ST  | R   |     | Patient Status             |
|         | 18   | 20  | ST  |     |     | Clinic                     |

<span id="_Toc84256347" class="anchor"></span>Table 19: NTE Segments Application Definition

7.  When the CMOP WARNING LABEL SOURCE is “New”, the warning label numbers will not be sent in the ZX1 segment, but instead, will be sent along with the warning label text in the new NTE\|11\|segments.

<u>Example ZX1 segment</u>:

ZX1\|10170\|521^XXXXXXXXXXX\|M\|1\|(1 of 2)\|OPPROVIDER3,TWO\|1\|(674/1874)\|19920125\| 1\|1\|1\|30\|1\|521-107396\|3~7\|SC50\|CARDIOLOGY

Application specific data elements included in the ZX1 segment are described as follows:

Rx Number: the prescription number of the medication/item requested.

Pharmacy Site ID: SITE NUMBER field and PHARMACY DIVISION NAME field from the OUTPATIENT SITE file (#59) of the sending medical center. Example: 521^Xxxxxxxxxxx

Mail Processing ID: Currently the only designation permitted is “M”—mail.

Rx Count: Total number of Rx’s including this Rx which are remaining in the patient order (number of orders to be processed).

Provider/Physician: The name of the provider/physician responsible for this order.

Registered Mail: Designations are 1-Yes and otherwise No. This data element may be reviewed for further description in the future but will remain a single numeric digit code.

Clerk/Verifying Pharmacist: A unique number identifying the verifying pharmacist, and another identifying the clerk who entered the order.

Fill date: Fill date of the drug/item (CCYYMMDD).

Copayment ID: Designation is 1-patient is eligible for prescription copayment, otherwise patient is ineligible.

Renewable: Indicates whether or not the prescription is renewable. Designation is 1- Renewable.

Safety Cap: Indicates if the medication requires a non-safety cap. Designations are 1- Yes, otherwise No. If 1 (Yes), print NON-Safety on the Pharmacist Copy.

Days Supply: The number of days supply for the prescription/item. This information is printed on the Copayment document and the Pharmacist copy.

Controlled Substances Indicator: This data element will contain a 1 if the Rx is a controlled substance; otherwise, the field will be null.

Barcode Data-Institution ID: Internal entry number from prescription file.

Warning Message Flag: This data element contains codes for warning text to be printed with the drug. This field may be repeated five times.

Patient Status: Pharmacy patient status.

Clinic: Clinic location at time of order.

## NTE Notes and Comments Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Notes and Comments segments are utilized by this application to transfer data which cannot be included in current HL7 defined segments.

NTE segments may repeat as necessary, and all NTE segments using the same set ID will follow consecutively in the message.

Batch related NTE segments containing facility specific parameters, patient instructions and prescription copayment narrative will appear immediately following the BHS segment.

Patient related NTE segments containing multi-Rx and suspense notification, and address (third line) information will follow the PID segment.

Order related NTE segments containing information related to the SIG (instructions) will follow the RX1 segment and may repeat as necessary.

| Segment | SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME |
|---------|------|-----|-----|-----|-----|--------------|
| NTE     | 1    | 4   | SI  |     |     | Set ID       |
|         | 3    | 120 | TX  | R   | Y   | Comment      |

<span id="_Toc84256348" class="anchor"></span>Table 20: NTE Segment: Set ID=1

When a field of type TX is being encoded, the escape character may be used to signal certain special characteristics of portions of the text field. The escape character is whatever display ASCII character is specified in the Escape Character Field in the MSH segment. For purposes of this application, the character “\\ will be used to represent the character so designated in a message. An escape sequence consists of the escape character followed by an escape code id of one character followed by 0 or more data characters followed by another occurrence of the escape character. The following escape sequences are defined and currently being used in this application.

\F\\ - field separator

\S\\ - component separator

\T\\ - subcomponent separator

\R\\ - repetition separator

Application definition for numbering of NTE segments:

| Set ID | Notes and Comments field                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \*1    | Facility Information separated by the escape sequences defined by field separator and component separator. (Required Segment)(max character=186).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 2      | Patient Instructions for refillable Rx. Text information separated by the repetition separator escape sequence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 3      | Patient Instructions for non-refillable Rx. Text information separated by the repetition separator escape sequence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 4      | Copayment narrative text information separated by the repetition separator escape sequence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \*5    | Multi-Rx turnaround information containing data fields separated by the field separator escape sequence. (max character=125).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| \*6    | Suspense notification information containing data fields separated by the field separator escape sequence. (max character=124).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 7      | SIG (Instructions) information when the SIG length exceeds the 80 characters allowed in the RX1 segment. This segment may repeat as many times as needed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| \*8    | If the patient street address information exceeds two lines (HL7 standard for PID segment), additional lines, beginning with “line 3” will be held in NTE\|8\| segments. These segments will always follow the Patient Identification (PID) segment. This segment will also contain temporary address information (max character=124).                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 11     | Warning Label Text - \*When the CMOP WARNING LABEL SOURCE is “New”, the warning label numbers, and corresponding warning label text will be sent in this new segment. If the patient has a PMI preference of Spanish, warning labels will be sent in both English and Spanish. If the DEA, SPECIAL HDLG field (#3) in the DRUG file (#50) begins with numbers 1,2,3,4, or 5, then the NO TRANSFER warning text from the RX CONSULT file (#54) entry number 20 will be sent as one of the warnings. There is no limit on the number of warnings that can be sent. The text in this segment, however, will be restricted to 220 characters. If the warning text is greater than 220 characters in length, then it will be continued in the continuation segment NTE\|11A\|. |
| 11A    | Warning Label Text Continuation – \*This segment will immediately follow the NTE\|11\| (Notes and Comments) segment, but only when the NTE\|11\| text exceeds 220 characters. This segment will contain the additional characters beyond the first 220 characters of the warning, but only up to an additional 220 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 99     | Information regarding dispensing of the prescription ordered. This data is returned from the vendor system when a query message is received from the VistA system. (Required for each prescription returned).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 100    | Information on this segment consists of the cancellation reason for a non-dispensed prescription, the date the prescription was shipped to the patient, the carrier handling the shipment, and the package identification code of the shipment. This data, if present, is returned by the vendor system when a query message is received from the VistA system.                                                                                                                                                                                                                                                                                                                                                                                                           |

<span id="_Toc84256349" class="anchor"></span>Table 21: NTE Segment: Set ID=2

8.  \*The requirements of the data elements for this segment exceed the 120-character length definition but will not exceed the maximum characters listed. The maximum length of any segment (including control characters) is 245 characters.

### NTE Segment—Facility Specific Information Definition Table Set ID=1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NOTES AND COMMENTS field contains information related to the institution or facility which originated the message. The TX (Text field) Data type uses the escape sequence, \F\\ as a field separator, and the escape sequence, \S\\ as a component separator.

The information in the table below describes the components encoded in the NOTES AND COMMENTS text field of the Facility NTE segment: Set ID=1.

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME IN NOTES AND COMMENTS |
|------|-----|-----|-----|-----|------------------------------------|
| 1    | 40  | ST  | R   |     | Pharmacy Division Data             |
| 2    | 106 | AD  | R   |     | Address                            |
| 3    | 40  | TN  |     |     | Phone number                       |

<span id="_Toc84256350" class="anchor"></span>Table 22: NTE Segment: Set ID=3

<u>Example</u>:

NTE\|1\|\|Site#\S\Division Name\S\Institution\F\Street Address\S\Other Street\S\City\S\State Abbrev.\S\ZIP code (99999 or 99999-9999)\F\Phone (999) 999-9999

This required segment, NTE\|1\|, is a single occurrence for each Batch of data and will always follow the Batch Header Segment (BHS\|)

Description of Components of the data elements:

Pharmacy Division Data: Components of this field are the site number, the pharmacy division, and the institution (station number).

Address: The 1-2 line street address, city, state, and ZIP Code for the pharmacy division.

Phone: The telephone number of the pharmacy division.

### RF Patient Instruction NTE Segment Definition Table Set ID=2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME IN NOTES AND COMMENTS |
|------|-----|-----|-----|-----|------------------------------------|
| 1    | 4   | SI  |     |     | Set ID                             |
| 3    | 100 | ST  | R   |     | Instruction (refillable)           |

<span id="_Toc84256351" class="anchor"></span>Table 23: NTE Segment: Set ID=4

<u>Example</u>:

NTE\|2\|\|The instructions present in this field refer to refillable prescriptions only. This information may b

NTE\|2\|\|e found in the outpatient site file number 59.

This segment, NTE \|2\|, may repeat as necessary to include all RF patient instructions and, if present, will always follow the NTE\|1\| segment.

This is not a required segment and will only be present if data is available.

### NRF Patient Instruction NTE Segment Definition Table Set ID=3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME IN NOTES AND COMMENTS |
|------|-----|-----|-----|-----|------------------------------------|
| 1    | 4   | SI  |     |     | Set ID                             |
| 3    | 100 | ST  | R   |     | Instruction (refillable)           |

<span id="_Toc84256352" class="anchor"></span>Table 24: NTE Segment: Set ID=5

<u>Example</u>:

NTE\|3\|\|The instructions present in this field refer to non-refillable prescriptions only and may be found i

NTE\|3\|\|n the outpatient site file number 59.

This segment, NTE\|3\|, may repeat as necessary to include all NRF patient instructions and, if present, will always follow the last NTE\|2\| segment.

This is not a required segment and will only be present if data is available.

### Copayment NTE Segment Definition Table Set ID=4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME IN NOTES AND COMMENTS |
|------|-----|-----|-----|-----|------------------------------------|
| 1    | 4   | SI  |     |     | Set ID                             |
| 3    | 100 | ST  | R   |     | Instruction (refillable)           |

<span id="_Toc84256353" class="anchor"></span>Table 25: Multi Rx Information Data Fields

<u>Example</u>:

NTE\|4\|\|This is an example of the prescription copayment narrative information entered in the outpatient sit

NTE\|4\|\|e file. This information will advise patients of telephone contact numbers available for inquires.

This segment, NTE\|4\|, may repeat as necessary to include all prescription copayment narrative text and if present, will follow the last NTE\|3\| segment. This is not a required segment and will only be present if data is available.

### MRX Document NTE Segment Definition Table Set ID=5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME IN NOTES AND COMMENTS |
|------|-----|-----|-----|-----|------------------------------------|
| 1    | 4   | SI  |     |     | Set ID                             |
| 3    | 120 | ST  | R   |     | Max Rx Information                 |

<span id="_Toc84256354" class="anchor"></span>Table 26: NTE Segment: Set ID=6

The NOTES AND COMMENTS field contains information related to the institution or facility which originated the message. The TX (Text field) Data type uses the escape sequence, \F\\ as a field separator, and the escape sequence, \S\\ as a component separator.

The information in the table below describes the components encoded in the NOTES AND COMMENTS text field of the MRX Document NTE segment: Set ID=5.

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME IN NOTES AND COMMENTS |
|------|-----|-----|-----|-----|------------------------------------|
| 1    | 20  | ST  | R   |     | Prescription Number                |
| 2    | 40  | ST  | R   |     | Generic Drug Name                  |
| 3    | 2   | NM  | R   |     | Refills Remaining                  |
| 4    | 8   | DT  | R   |     | Expiration Date                    |
| 5    | 20  | ST  | R   |     | Barcode Data                       |

<span id="_Toc84256355" class="anchor"></span>Table 27: NTE Segment: Set ID=7

<u>Example</u>:

NTE\|5\|\|104728\F\ACETAMINOPHEN 325mg\F\3\F\19930731\F\521-4219 NTE\|5\|\|947\F\NIACIN 25mg\F\1\F\19930228\F\521-4297

The MRX NTE segment will occur once for each prescription to be listed on the multi- Rx turnaround document. These segments (if present) will always follow the PID segment of the message.

### Suspense Notification NTE Segment Set ID=6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME IN NOTES AND COMMENTS |
|------|-----|-----|-----|-----|------------------------------------|
| 1    | 4   | ST  |     |     | Set ID                             |
| 3    | 120 | ST  | R   |     | Suspense Notice Information        |

<span id="_Toc84256356" class="anchor"></span>Table 28: NTE Segment: Set ID=8

<u>Example</u>:

NTE\|6\|\|1267218A\F\VERAPAMIL 120mg TAB NTE\|6\|\|8473C\F\PREDNISONE 20mg TAB

The Suspense Notification NTE segment will occur once for each prescription to be printed on the Suspense Notification Document. These segments (if present) will always follow the related PID segment of the message.

Suspense Notice Information Data Fields:

Prescription Number

Generic Drug Name

Suspense Date (designated for future use, not presently required)

### SIG (Instructions) NTE Segment Definition Table Set ID=7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the CMOP WARNING LABEL SOURCE is “New”, additional fields are added to this segment for the SIG.

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME IN NOTES AND COMMENTS |
|------|-----|-----|-----|-----|------------------------------------|
| 1    | 4   | ST  | R   |     | Set ID                             |
| 2    | 100 | ST  | R   |     | RX Number                          |
| 3    | 3   | ST  | R   |     | Language Code                      |
| 4    | 2   | NM  | R   |     | Record Number                      |
| 5    | 80  | ST  | R   |     | Text                               |

<span id="_Toc84256357" class="anchor"></span>Table 29: Additional Address Information Data Fields

<u>Example</u>:

RX1\|500-300997-1\|\|\|\|\|\|\|\|\|\|\|21\|\|T0034^THIORIDAZINE HCL 10MG

TAB^L\|\|\|\|\|11\|2006112

8\|11\|\|\|20071129\|20061208\|300997\|\|\|\|TAKE ONE TABLET BY MOUTH TWICE A DAY FOR 7 DAYS, THEN TAKE ONE TABLET AT

NTE\|7\|300997\|ENG\|1\|BEDTIME FOR 7 DAYS

NTE\|7\|300997\|SPA\|1\|TAKE UNO TABLET BY MOUTH TWICE A DAY PARA 7 DIAS, THEN TAKE UNO TABLET AT

NTE\|7\|300997\|SPA\|2\|BEDTIME PARA 7 DIAS OTHER LANGUAGE PATIENT INSTRUCTIONS WOULD HAVE BEEN

NTE\|7\|300997\|SPA\|3\|ENTERED HERE

This segment, NTE\|7\|, may repeat as necessary to include all the SIG (instructions) and, if present, will always follow the related RX1 segment.

### Patient Additional Street Address Segment Definition Table Set ID=8

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME IN NOTES AND COMMENTS |
|------|-----|-----|-----|-----|------------------------------------|
| 1    | 4   | ST  |     |     | Set ID                             |
| 3    | 120 | ST  | R   |     | Additional Address Information     |

<span id="_Toc84256358" class="anchor"></span>Table 30: NTE Segment: Set ID=11

<u>Example of Patient Data with Temporary Address Information</u>:

PID\|\|\|000579013^1^M11\|\|CMOPPATIENT3^ONE\|\|\|\|\|\|123 OAK ST.^REDACTED^TX^75024 (or 75025-9999)

NTE\|8\|\|1\F\19930115\F\Street Address line 3\R\Street Address line 4\R\Street Address line 5

<u>Example of Patient Data with NO Temporary Address Information</u>:

PID\|\|\|000579013^1^M11\|\|CMOPPATIENT3^ONE\|\|\|\|\|\|123 OAK ST.^REDACTED^TX^75024

NTE\|8\|\|\F\\F\Street Address line 3\R\Street Address line 4\R\Street Address line 5

This segment, NTE\|8\|, lists additional address information for the patient and, if present, will follow the related PID segment.

Additional Address Information Data Fields:

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME IN NOTES AND COMMENTS                                      |
|------|-----|-----|-----|-----|-------------------------------------------------------------------------|
| 1    | 1   | NM  | R   |     | Temporary Address (1=yes)                                               |
| 2    | 8   | DT  | R   |     | Temporary Until (Date YYYYMMDD)                                         |
| 3    | 35  | ST  | R   | Y/2 | Additional Street Address \[This field may repeat twice if necessary\]. |

<span id="_Toc84256359" class="anchor"></span>Table 31: MSA Acknowledgment Segment Definition

### Patient Warning Label Text Segment Definition Table Set ID=11

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME IN NOTES AND COMMENTS |
|------|-----|-----|-----|-----|------------------------------------|
| 1    | 4   | ST  | R   |     | Set ID                             |
| 2    | 100 | ST  | R   |     | RX Number                          |
| 3    | 3   | ST  | R   |     | Language Code                      |
| 4    | 2   | NM  | R   |     | Record Number                      |
| 5    | 265 | ST  | R   |     | Warning Label Text                 |

<span id="_Toc84256360" class="anchor"></span>Table 32: MSA Batch Transmission Definition

<u>Example of Warning Label Text</u>:

NTE\|11\|300997\|ENG\|1N\|May cause drowsiness. Alcohol may intensify this effect.

Use care when operating a car or dangerous machines. NTE\|11\|300997\|ENG\|77N\|Warning: Do not use while you are breastfeeding. Consult your doctor or pharmacist.

Enter RETURN to continue or '^' to exit:

Subj: CMOP Transmission from REDACTED, NY \[#168989\] Page 4 NTE\|11\|300997\|ENG\|13N\|It is very important that you take or use this exactly as

directed. Do not skip doses or discontinue unless directed by your doctor.

NTE\|11\|300997\|ENG\|14N\|Obtain medical advice before taking non-prescription drug s as some may affect the action of this medication.

NTE\|11\|300997\|ENG\|20\|CAUTION: Federal law prohibits the transfer of this drug to any person other than the patient for whom it was prescribed.

NTE\|11\|300997\|SPA\|1N\|Puede causar somnolencia. El alcohol puede intensificar es te efecto. Tenga cuidado cuando conduzca veh¡culos automotores u opere maquinar ia peligrosa.

NTE\|11\|300997\|SPA\|77N\|Advertencia: No lo use mientras amamante. Cons£ltelo a su mdico o farmacutico.

NTE\|11\|300997\|SPA\|13N\|Es muy importante que lo tome o lo use exactamente seg£n las indicaciones. No omita ninguna dosis ni lo deje de usar a menos que lo mand e el mdico.

NTE\|11\|300997\|SPA\|14N\|Consulte a un profesional de la salud antes de tomar medi camentos sin receta mdica ya que algunos pueden afectar la acci¢n de este medi camento.

NTE\|11\|300997\|SPA\|20\|PRECAUCION: La ley federal prohibe la transferencia de est e medicamento a otro paciente para el que no fue recetado.

## General Acknowledgment Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The protocol software of the responding system sends a General Acknowledgment message to the sender upon receiving a complete patient order. The General Acknowledgment message consists of a message header (MSH) segment and a message acknowledgment (MSA) segment.

| Segment | SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME        |
|---------|------|-----|-----|-----|-----|---------------------|
| MSA     | 1    | 2   | ST  | R   |     | Acknowledgment Code |
|         | 2    | 20  | ST  | R   |     | Message Control ID  |
|         | 3    | 80  | ST  |     |     | Text Message        |

<span id="_Toc84256361" class="anchor"></span>Table 33: QRD Segment Definition

Data elements included in the MSA segment are

Acknowledgment code—Indicates the status of the patient order. Designations are:

AA-accepted

AE-error (not currently used by this application)

AR-rejected

Message Control ID—the ID of the message sent by the sending system which allows the sending system to associate this response with the message for which it is intended.

Text Message—Text information that further describes an error condition.

<u>Example of General Acknowledgment Message (Accepted)</u>:

MSH\|^~\\\|VENDOR\|\|DHCP\|\|199211091600\|\|ACK\|Z96748\|P\|2.1\| MSA\|AA\|106-247-2567\|

The “AA” code in the MSA segment indicates the message was accepted by the application. The segment acknowledges the message that VistA sent as 106-247-2567.

<u>Example of General Acknowledgment Message (Error Condition)</u>:

MSH\|^~\\\|VENDOR\|\|DHCP\|\|199211091600\|\|ACK\|Z96748\|P\|2.1\| MSA\|AR\|106-247-2567\|FORMAT ERROR

The AR code in the MSA segment indicates an error condition was detected by the application during data validation of the message, and the message was rejected, not accepted, by the receiver.

## Transaction Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The message header segment (MSH) and the patient identification (PID) segment are present once for each patient order message. The common order (ORC) segment and the pharmacy order segments (RX1, ZX1) are present for each prescription/item contained in the patient order. The NTE segments containing the multi-Rx information, suspense notification information, and additional street address, if present, will follow the PID segment and precede the first occurrence of the ORC segment. The minimum segments required for a patient order message are MSH, PID, ORC, RX1, and ZX1.

The following is a description of the data transmitted to the non-VistA system from the VistA CMOP application. When a patient order transaction, is complete and ready for transmission to the non-VistA system, the ORM message will consist of the following segments.

ORM - ORDER MESSAGE

MSH - Message Header

PID - Patient Identification

NTE - Notes and Comments

ORC - Common Order

RX1 - Pharmacy Order

ZX1 - VA Specific Pharmacy Information

<u>Example</u>:

MSH\|^~\\\|DHCP\|\|VENDOR\|\|199209150415\|\|ORM\|106-247-2567\|P\|2.1\| PID\|\|\|000579013^1^M11\|\|CMOPPATIENT3^ONE\|\|\|\|\|\|123 OAK ST.^REDACTED^TX^75024 NTE\|5\|\|104728\F\ACETAMINOPHEN 325mg\F\3\F\19930731\F\521-17843 NTE\|5\|\|947\F\NIACIN 25mg\F\1\F\19930228\F\521-209678 NTE\|6\|\|1267218A\F\VERAPAMIL 120mg TAB

NTE\|6\|\|8473C\F\PREDNISONE 20mg TAB

NTE\|8\|\|Street Address line 3\R\Street Address line 4\R\Street Address line 5 ORC\|NW\|

RX1\|521-10170-1\|\|\|\|\|\|\|\|\|\|\|30\|\|218A^ RANITIDINE 100mg ^L\|\|\|\|\|5\|19921225\|3\|\|\| 19930630\|

19921230\|10170\|\|\|\| TAKE 2 TABLET(S) BY MOUTH EVERY DAY FOR 7 DAYS, THEN TAKE 3 TABLET(S) EVERY DAY

NTE\|7\|10170\|ENG\|1\|THEN TAKE 1 TABLET TWICE A DAY FOR 3 DAYS, THEN TAKE 2 TABLET(S) FOR PAIN

NTE\|11\|300551A\|ENG\|13N\|It is very important that you take or use this exactly as directed. Do not skip doses or discontinue unless directed by your doctor. ZX1\|10170\|521^XXXXXXXXXXX\|M\|1\|(1 of 2)\|OPPROVIDER31,TWO\|1\|(674/1874)\| 199201251301\|1\|1\|1\|30\|19920630\|521-107396\|\|SC50\|CARDIOLOGY

NTE segments with set ID’s 5, 6, and 8 will be present, if and only if, data is available.

NTE segment set ID 11 is only present if the CMOP WARNING LABEL SOURCE is set to “New”.

The non-VistA system then sends a General Acknowledgment message (MSA segment) back to the CMOP system.

## Batch Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Segment | SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME              |
|---------|------|-----|-----|-----|-----|---------------------------|
| BHS     | 1    | 1   | ST  | R   |     | Batch Field Separator     |
|         | 2    | 3   | ST  | R   |     | Batch Encoding Characters |
|         | 3    | 15  | ST  |     |     | Sending Application       |
|         | 5    | 15  | ST  |     |     | Receiving Application     |
|         | 7    | 19  | TS  |     |     | Date/Time Message         |
|         | 9    | 7   | ID  | R   |     | Message Type              |
|         | 10   | 20  | ST  | R   |     | Batch Reference ID\*  |
|         | 11   | 1   | ID  | R   |     | Processing ID             |
|         | 12   | 8   | NM  | R   |     | Version ID                |

<span id="_Toc84256362" class="anchor"></span>Table 34: Vendor Response NTE Segment=99

9.  \*Batch Reference ID – The facility ID number followed by a hyphen and the transmission number for the medical center. This ID uniquely identifies the transmission.

BTS: This segment defines the end of a batch.

The HL7 Batch Transmission protocol will be used to transmit a group of patient orders from the same facility. The following is an example of a batch transmission.

<u>Example</u>:

BHS\|^~\\\|DHCP\|\|VENDOR\|\|199209160415\|\|ORM\|106-247\|P\|2.\|

NTE\|1\|\|Site#\S\Division Name\S\Institution\F\Street Address\S\Other Street\S\City\S\State Code\S\ZIPcode (99999 or 99999-9999)\F\Phone(999)999- 9999

NTE\|2\|\|The instructions present in this field refer to refillable prescriptions only. This information may b

NTE\|2\|\|e found in the outpatient site file number 59.

NTE\|3\|\|The instructions present in this field refer to non-refillable prescriptions only and may be found i

NTE\|3\|\|n the outpatient site file number 59.

NTE\|4\|\|This is an example of the prescription copayment narrative information entered in the outpatient sit

NTE\|4\|\|e file. This information will advise patients of telephone contact numbers available for inquires.

MSH\|^~\\\|DHCP\|\|VENDOR\|\|199209150415\|\|ORM\|106-247-2567\|P\|2.1\| PID\|\|\|000579013^1^M11\|\|CMOPPATIENT3^ONE\|\|\|\|\|\|123 OAK ST.^REDACTED^TX^75024 NTE\|5\|\|104728\F\ACETAMINOPHEN 325mg\F\3\F\19930731\F\521-4219 NTE\|5\|\|947\F\NIACIN 25mg\F\1\F\19930228\F\521-67438 NTE\|6\|\|1267218A\F\VERAPAMIL 120mg TAB

NTE\|6\|\|8473C\F\PREDNISONE 20mg TAB ORC\|NW\|

RX1\|521-10170-1\|\|\|\|\|\|\|\|\|\|\|30\|\|218A^ RANITIDINE 100mg ^L\|\|\|\|\|5\|19921225\|3\|\|\| 19930630\|

19921230\|10170\|\|\|\|TAKE ONE TABLET THREE TIMES A DAY AFTER MEALS ZX1\|10170\|521^XXXXXXXXXXX^7\|M\|1\|(1 of 2)\|OPPROVIDER,TWO\|1\|(674/1874)\|19920125\| 1\|1\|1\|30\|\|521-107396\|WARN\|SC50\|CARDIOLOGY

MSH\|. . . (multiple patient orders will follow)

BTS\|

NTE segments with set IDs 2,3, and 4 will be present, if and only if, data is available.

## VistA Query for Data from non-VistA System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The generalized Query Message (QRY) will be used to support queries from the VistA CMOP system to the non- VistA system. The queries will request an immediate response and require “record oriented” data containing dispensing information from the responding system.

The VistA CMOP Query requests prescription data released since the last query was issued. The non- VistA system will respond with “all available data” up to the maximum number of responses allowed by the Quantity Limited Request data element in the Query Definition segment (QRD). Usually, each data response is for a single prescription. The automated system has the option of returning multiple prescriptions for a single unique patient order (MSH, PID). The responses may be for prescriptions of the same or different patients.

The following HL7 segments will be used to support the VistA Query:

QRY - Query Message

MSH - Message Header

| QRD | SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME                    |
|-----|------|-----|-----|-----|-----|---------------------------------|
|     | 1    | 19  | TS  | R   |     | Query Date/Time                 |
|     | 2    | 1   | ID  | R   |     | Query Format Code (R)           |
|     | 3    | 1   | ID  | R   |     | Query Priority (I)              |
|     | 4    | 10  | ST  | R   |     | Query ID                        |
|     | 7    | 5   | CQ  | R   |     | Quantity Limited Request (ZO)   |
|     | 8    | 20  | ST  | R   | Y   | Who Subject Filter (OP)         |
|     | 9    | 3   | ID  | R   | Y   | What Subject Filter (OTH)       |
|     | 10   | 20  | ST  | R   | Y   | What Department Data Code (ALL) |

<span id="_Toc84256363" class="anchor"></span>Table 35: Vendor Ancillary Data NTE Segment=100

10. \*For purposes of this application, the Quantity Limited Request data element is locally defined to be the maximum number of prescription responses allowed to be returned for the current data query.

<u>Example of Data Query from VistA to non-VistA System</u>:

MSH\|^~\\\|DHCP\|\|VENDOR\|\|199211102304\|\|QRY\|29745\|P\|2.1\| QRD\|199211102304\|R\|I\|29745\|\|\|2000^ZO\|OP\|OTH\|ALL

## Non-VistA System Response to VistA Data Query

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Observation Result/Record Response (ORF) message will be used to return dispensing information to the VistA system. The data elements required for each prescription/item ordered will be contained in an NTE segment with the Set ID=99. One NTE\|99\| segment will be returned for each prescription/item of each patient order. The QRD segment will be echoed from the QRY message and the PID and MSH segments are echoed from the original patient orders.

The following HL7 segments will be used to support the Query response information and the Query Acknowledgment from the non-VistA system:

ORF Observation Result/Record Response Message

MSA General Acknowledgment

QRD Query Definition

MSH Message Header

PID Patient Identification

NTE Notes and Comments

<u>Example of General Acknowledgment Message of VistA Query by Non-VistA System</u>:

MSH\|^~\\\|VENDOR\|\|DHCP\|\|199211112339\|\|ORF\|VENDOR MSG ID\|P\|2.1\| MSA\|AA\|29745\| QRD\|199211102304\|R\|I\|29745\|\|\|2000^ZO\|OP\|OTH\|ALL

### NTE Segment—Vendor (non-VistA) Response Definition Table Set ID=99

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NOTES AND COMMENTS field contains dispensing information for a prescription. The TX (Text field) data type used the escape sequence, \F\\ as a field separator, and the escape sequence, \S\\ as a component separator. The information in the table below describes the components encoded in the NOTES AND COMMENTS text field of the Vendor Response NTE segment.

The following table describes data elements present in the Notes and Comments field of the Vendor Response NTE segment:

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME                                |
|------|-----|-----|-----|-----|---------------------------------------------|
| 1    | 15  | ST  | R   |     | Rx Number                                   |
| 2    | 2   | ST  | R   |     | Status - (completed/cancelled/out of stock) |
| 3    | 12  | TS  | R   |     | Completed dt/tm                             |
| 4    | 12  | ST  |     |     | NDC                                         |
| 5    | 6   | NM  | R   |     | Released by Employee                        |
| 6    | 20  | ST  | R   |     | Message Control ID                          |
| 7    | 27  | CE  |     |     | Lot \# - Expiration Date                    |

<span id="_Toc84256364" class="anchor"></span>Table 36: Key Terms

This segment, NTE\|99\|, is a single occurrence required for each prescription released by the non- VistA system and will always follow the related PID segment or another NTE\|99 or NTE\|100 segment from the same order.

Description of Components of the Data Elements:

RX Number: The external value of the prescription number being released. Status—Status, assigned by the vendor, of the released prescription.

CO-Completed: CMOP filled the prescription and sent it to the patient.

CA-Cancelled: CMOP did not dispense the drug/item.

OS-Out of Stock: CMOP is temporarily out of stock for the requested drug/item. The automated system will complete the prescription when the drug/item becomes available. If the drug/item is not stocked within a reasonable time period, the prescription will be cancelled.

Completed Date/Time: The date/time the prescription data was released by the pharmacist.

NDC: National Drug Code.

Released by Employee: The code which uniquely identifies the pharmacist who released the dispense information.

Message Control ID: The original message control ID used by the VistA system to uniquely identify the patient order for the prescription release data being returned by the non-VistA system. This message control ID originates from the MSH segment transmitted with the original patient order.

Lot# - Expiration Date: The field has two components. The first component is the lot# of the prescription dispensed (12 characters). The second component is the expiration date of the lot# (15 characters).

<u>Example of Prescription Release Data from Non-VistA System</u>:

MSH\|^~\\\|DHCP\|\|VENDOR\|\|199209150415\|\|ORF\|4073682\|P\|2.1\| PID\|\|\|000579013^1^M11\|\|CMOPPATIENT3^ONE\|\|\|\|\|\|123 OAK ST.^REDACTED^TX^75024

NTE\|99\|\|RX#1\F\Status\F\Completed DT-Time\F\NDC\F\Released by Emp\F\106-247- 2567\F\Lot#\S\Expdt\R\Lot#\S\Expdt

NTE\|99\|\|RX#2\F\Status\F\Completed DT-Time\F\NDC\F\Released by Emp\F\106-247- 2567\F\Lot#\S\Expdt\R\Lot#\S\Expdt

### NTE Segment—Vendor Ancillary Data Definition Table Set ID=100

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ# | LEN | DT  | R/O | RP  | ELEMENT NAME                                |
|------|-----|-----|-----|-----|---------------------------------------------|
| 1    | 15  | ST  | R   |     | Rx Number                                   |
| 2    | 2   | ST  | R   |     | Status - (completed/cancelled/out of stock) |
| 3    | 12  | TS  | R   |     | Completed dt/tm                             |
| 4    | 12  | ST  |     |     | NDC                                         |
| 5    | 6   | NM  | R   |     | Released by Employee                        |
| 6    | 20  | ST  | R   |     | Message Control ID                          |
| 7    | 27  | CE  |     |     | Lot \# - Expiration Date                    |

<span id="_Toc84256365" class="anchor"></span>Table 37: MSH – Message Header Segment – Required Segment

<u>Example</u>:

NTE\|100\|\|Cancellation Reason\F\Date Shipped\F\Carrier\F\Package ID\F\Rx Number

This data is returned by the vendor system when a query message is received from the VistA system. This NTE\|100\| segment is a single occurrence for each prescription manifested by the non-VistA system and, if present, will always follow the related NTE\|99\| segment for the same prescription.

Description of Components of the Data Elements:

Cancellation Reason: The reason the prescription was cancelled by the pharmacist. This data element is required for all prescriptions returned with a status of cancelled.

Date Shipped: The date/time the prescription was shipped to the patient. Carrier, the carrier responsible for shipping the prescription to the patient.

Package ID: A unique identification code assigned by the non-VistA system for tracking the prescription shipment.

RX Number: The external value of the prescription number being released.

# Appendix C—Consolidated Mail Outpatient Pharmacy Electronic Data / HL7 Interface Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following EDI document is attached as a separate, complete document. Its original formatting, including page numbering and Table of Contents, are retained.

Consolidated Mail Outpatient Pharmacy (CMOP)

Electronic Data Interface (EDI) Guidelines

Version 1

![](cmop-version-2-technical-manual-updated-psx-2-91/002.png)

September 2021

# CMOP HL7 Interface Specification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General HL7 Information

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to define a standard electronic data interface (EDI) between outside agencies and the Consolidate Mail Outpatient Pharmacy (CMOP) system. This specification is based upon the Health Level 7 Standard (HL7) Version 2.3.1. The term “Level 7” refers to the highest level of the Open System Interconnection (OSI) model of the International Standards Organization (ISO). The OSI model is divided into seven levels or layers. The HL7 Standard is primarily focused on what happens within the seventh or application layer. The definitions of the data to be exchanged, the timing of the exchanges, and the communication of certain application specific errors occur at this layer.

# Key Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc84256366" class="anchor"></span>Table 38: MFE – Master File Entry Segment – Required segment</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Outside Agency</td>
<td>Outside agencies are defined as any non-VA entity.</td>
</tr>
<tr class="even">
<td>Originating Agency (OA)</td>
<td>The agency that ‘owns’ the prescription (Rx). The originating agency may be an entity sending data to a VA CMOP facility. The originating agency may also be a VA CMOP facility sending the Rx data to an outside agency to fill under the ‘home delivery’ contract.</td>
</tr>
<tr class="odd">
<td>Dispensing Agency (DA)</td>
<td>The agency that fulfills the prescription order.</td>
</tr>
<tr class="even">
<td>Prescription Order Data</td>
<td>This the data needed by the filling agency to dispense and mail the Rx to the patient.</td>
</tr>
<tr class="odd">
<td>Prescription Fulfillment Data</td>
<td>This is the data that is returned by the dispensing agency to the originating agency to show that the Rx was either dispensed and mailed or returned as not- dispensed.</td>
</tr>
<tr class="even">
<td>Station Number</td>
<td>A unique number assigned to the originating facility. This number is from three to five numbers in length. VA Medical Centers will use the Station ID numbers. DoD MTFs will use the DMIS ID numbers. The data type is integer.</td>
</tr>
<tr class="odd">
<td>Batch Number</td>
<td><p>This is a unique number assigned to each batch of dispensing data to be transferred. The Batch Number is made up of two data elements. The first element is the unique Station Number of the originating agency. The second element is a unique number generated by the originating agency for the batch. This number is formatted as a two-digit year, the Julian Date, two-digit hour, two digit minute (YYDDDHHMM). If two batches are created simultaneously at the originating site this number must be incremented to make the batches unique. These two data elements are joined together with the underscore character.</p>
<p><u>Example</u>: the originating agency Station Number is 766, batch number is 013240530. The unique Batch Number would be 766_013240530.</p></td>
</tr>
<tr class="even">
<td>Rx Index</td>
<td><p>This is a number that uniquely identifies the prescription from all other prescriptions. The Rx Index is made up of the Station Number dash Rx Number dash Fill Number. Fill numbers start at 1 for the original and increment sequentially for each new fill of the same prescription.</p>
<p><u>Examples</u>: Station Number = 10101, Rx Number = 123456T, Fill Number = 1 for the original. The Rx Index would be 10101-123456T-1. Station Number 10101, Rx Number = 12222A, Fill Number = 2 for the first refill of this prescription, the Rx Index would be 10101-12222A-2.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc84256366" class="anchor"></span>Table 38: MFE – Master File Entry Segment – Required segment

## File Extensions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following file extensions will be used for the transaction specified.

.TRN - transmission of dispense request from OA to DA.

> 766_013240530.trn

.TAC - acknowledgement of dispense requests DA to OA.

> 766_013240530.ack

.QRY – prescription fulfillment data from DA to OA.

> 0111141230.qry

.QAC – acknowledgement of receipt of fulfillment data from OA to DA.

> 0111141230.qac

.SIT - activation/deactivation request from OA to DA.

> Filename Format - OA station number_DateTime stamp (yymmddhhmm).sit 766_0111151300.sit

.SAC – acknowledgement of activation/deactivation 766_0111151300.sac

.SCH – auto transmission schedule/unschedule message 766_0111151300.sch

.HAC – acknowledgement of auto transmission schedule/unschedule message.

> 766_0111151300.hac

.NDF – National Drug File data update

> ndf update pxxx.ndf where xxx is the NDF patch number.

.NAC – National Drug File data update acknowledgement ndf update pxxx.nac

11. The ‘.TAC’, ‘.QAC’, ‘.SAC’, and ‘HAC’ acknowledgement files content will indicate the acceptance or rejection (nak) of the corresponding message. The message body will indicate which response is accurate.

# Message Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 Standard describes the basic rules for the exchange of information between two computer systems. The unit of data transferred is referred to as the message. It is comprised of a group of segments in a defined sequence. Each message has a three-character code called a message type that defines its purpose. The real-world event that initiates an exchange of messages is called a trigger event. There is a one-to-many relationship between message types and trigger event codes. The same trigger event code may not be associated with more than one message type; however a message type may be associated with more than one trigger event. All message type and trigger event codes beginning with Z are reserved for locally defined messages. No such codes will be defined within the HL7 Standard.

Some special characters are used to construct messages. They are the segment terminator, field separator, component separator, sub-component separator, repetition separator, and escape character. The segment terminator is always a carriage return (CR in ASCII or hex OD). The other characters recommended by HL7 are used in this application (See HL7 Standard V. 2.3.1, Chapter 2 for details).

# Segment Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A segment is a logical grouping of data fields. Segments of a message may be required or optional. They may occur only once in a message or they may be allowed to repeat. Each segment is given a name and is identified by a unique three-character code. All segments beginning with Z are reserved for locally defined messages. No such code will be defined within the HL7 Standard. Segment length will not exceed 245 characters.

# Field Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A field is a string of characters. HL7 does not care how systems actually store data within an application. Except where noted, HL7 data fields may take on the null value. Sending the null value, which is transmitted as two double quotation marks (“”), is different from omitting an optional data field. The difference appears when the contents of a message will be used to update a record in a database rather than create a new one. If no value is sent (i.e., it is omitted) the old value should remain unchanged. If the null value is sent, the old value should be changed to null. In defining a segment, the following information is specified about each field:

1.  Position - position of the data field within the segment.
2.  Name - unique descriptive name for the field.
3.  ID number - integer that uniquely identifies the data field throughout the Standard.
4.  Maximum length - maximum number of characters that one occurrence of the data field may occupy.
5.  Optional - whether the data field is required (R), optional (O), or conditional (C) in a segment.
6.  Repetition - whether the field may repeat (N=no; Y=yes; (integer)= no. of repeats).
7.  Table - a table of values for a field (See HL7 Standard V. 2.3.1, Section 2.4.3.7 for source of tables).
8.  Data type - restrictions on the contents of the data field (See HL7 Standard V. 2.3.1, Section 2.4.5).

# Message Construction Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

12. These message construction rules define the standard HL7 encoding rules, creating variable length delimited messages. Although only one set of encoding rules is defined as a standard in HL7 Version 2.3, other encoding rules are possible (but since they are non-standard, they may only be used by a site-specific agreement).

Step 1: Construct the segments in the order defined for the message. Each message is constructed as follows:

1.  The first three characters are the segment ID code.
2.  Each data field in sequence is inserted in the segment in the following manner:
1.  A field separator is placed in the segment.
2.  If the value is not present, no further characters are required.
3.  If the value is present, but null, the characters “” (two consecutive double quotation marks) are placed in the field.
4.  Otherwise, the characters of the value are placed in the segment. The maximum number of characters that can be included is defined for each data field. It is not necessary and is undesirable to pad fields to fixed lengths. Padding to fixed lengths is permitted. The individual data fields are encoded as shown in HL7 Standard V. 2.3.1, Chapter 2, Section 2.8, “DATA TYPES.”
5.  If the field definition calls for a field to be broken into components, the following rules are used:
1.  If more than one component is included they are separated by the component separator.
2.  Components that are present but null are represented by the characters “”.
3.  Components that are not present are treated by including no characters in the component.
4.  Components that are not present at the end of a field need not be represented by component separators. For example, the two data fields are equivalent:

> \|ABC^DEF^^\| and \|ABC^DEF\|.

6.  If the component definition calls for a component to be broken into subcomponents, the following rules are used:
1.  If more than one subcomponent is included they are separated by the subcomponent separator.
2.  Subcomponents that are present, but null are represented by the characters “”.
3.  Subcomponents that are not present are treated by including no characters in the subcomponent.
4.  Subcomponents that are not present at the end of a component need not be represented by sub-component separators. For example, the two data components are equivalent:

> ^XXX&YYY&&^ and ^XXX&YYY^.

7.  If the field definition permits repetition of a field, the following rules are used, the repetition separator is used only if more than one occurrence is transmitted and is placed between occurrences. (If three occurrences are transmitted, two repetition separators are used.) In the example below, two occurrences of telephone number are being sent:

> \|234-7120~599-1288B1234\|

3.  Repeat step 1) b) while there are any fields present to be sent. If all the data fields remaining in the segment definition are not present there is no requirement to include any more delimiters.
4.  End each segment with an ASCII carriage return character,

Step 2: Repeat Step 1 until all segments have been generated.

The following rules apply to receiving HL7 messages and converting their contents to data values:

1.  Ignore segments, fields, components, subcomponents, and extra repetitions of a field that are present but were not expected.
2.  Treat segments that were expected but are not present as consisting entirely of fields that are not present.
3.  Treat fields and components that are expected but were not included in a segment as not present.

# Communication Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Connectivity will be established using methods compatible with both the current VHA standards and the capabilities of the systems involved. The method the CMOP program is using to communicate with outside agencies at the time of printing follows. Due to the variability of network communication techniques and policy, the actual hardware currently in use has not been included in this document.

Purpose: This document describes the data transfer method used to exchange information between the VA CMOP system and outside agencies.

## Concept of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The method of data transfer described herein is commonly referred to as the “fetch” method. A storage device such as a hard drive located on a network server is shared between the OA and the DA. All data and administrative communications consist of HL7 formatted flat ASCII files.

These files are transferred to and from subdirectories or folders named INBOX and OUTBOX located on the shared drive. The OA will put all files it creates in the INBOX. The DA will put all files it creates in the OUTBOX. The OA will ‘batch’ together all data required to fill the prescriptions into one file.

The data is gathered and batched based on an agreed upon time interval and frequency between the DA and the OA. There can be from one-to-many patients in the batch. Each patient can have from one-to-many prescriptions. Data is organized by patient order in the file.

### Activation/Inactivation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To request approval to send the DA prescription data, the OA places an activation request in the INBOX. File extension “. sit.”
2.  The DA fetches the data from the INBOX and places an approval/disapproval in the OUTBOX. File extension “. sac.”

### Transmission Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If approved for activation, the OA places a transmission schedule in the INBOX. This transmission schedule would have previously been coordinated with the DA. File extension “. sch”.
2.  The DA fetches the transmission schedule and places a message acknowledgement file in the OUTBOX. File extension “.hac.”

### Prescription Order Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The OA batches the prescriptions and places the prescription order batch file in the INBOX. File extension “.trn.”
2.  The DA fetches the prescription order batch file and begins processing. The DA places an acknowledgement file in the OUTBOX. File extension “. tac.” If the file contains errors the DA places a negative acknowledgement in the OUTBOX. Where possible, as many of the problems detected will be identified. The entire batch will be rejected if ANY bad data within that batch is detected.
3.  After fulfilling the prescription orders, DA places the prescription fulfillment data in a folder in the OUTBOX. File extension “.qry.”
4.  The OA fetches the fulfillment data from the OUTBOX and places an acknowledgement that it has received the data in the INBOX. File extension “.qac.”
5.  The DA places a final acknowledgement in the OUTBOX upon receipt of the fulfillment acknowledgement from the OA in the inbox. File extension “.qac.” This completes the cycle for a prescription order.

# HL7 Segments Used in CMOP Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains the definitions of the segments used in CMOP transactions. It is divided into parts according to functionality, i.e., activation/inactivation, etc. Following each section heading is a list of the segments used for that transaction. Segment notation follows standard HL7 encoding rules.

Each message is defined in special notation that lists the segment IDs in the order they would appear in the message. Message segments without the braces or brackets indicate the segment is required within the message.

Braces, { . . . }, indicate one or more repetitions of the enclosed group of segments. (Of course, the group may contain only a single segment.)

Brackets, \[ . . . \], show that the enclosed group of segments is optional. If a group of segments is optional and may repeat it should be enclosed in brackets and braces, { \[ . . . \]

}.

13. \[{...}\] and {\[...\]} are equivalent.

## Activate/Inactivate (.SIT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH

MFE

ZLF

| Field Name                 | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                                                                                                                |
|----------------------------|------|-----|-----|-----|-----|-----|------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Field Separator            | 1    | 1   | ST  | R   | N   |     |      | HL7 recommended field separator.                                                                                                                           |
| Encoding Characters        | 2    | 4   | ST  | R   | N   |     |      | HL7 recommended encoding characters.                                                                                                                       |
| Sending Application        | 3    | 15  | ST  | R   | N   |     |      | The name of the application creating the batch.                                                                                                            |
| Receiving Application      | 5    | 30  | ST  | R   | N   |     |      | This is the application receiving the data.                                                                                                                |
| Message Creation Date/Time | 7    | 26  | TS  | R   | N   |     |      | Date and time the message was created on the sending station's system.                                                                                     |
| Message Type               | 9    | 7   | C   | R   | N   |     | 0076 | The type of message being sent. This will always be MFN^M01.                                                                                               |
| Message Control ID         | 10   | 20  | ST  | R   | N   |     |      | This is a number that uniquely identifies this message from all other messages. The format of the message number is station number transmission date/time. |
| Processing ID              | 11   | 1   | ID  | R   | N   |     | 0103 | This will always be a P.                                                                                                                                   |
| Version ID                 | 12   | 8   | ID  | R   | N\` |     | 0104 | This will always be 2.3.1                                                                                                                                  |
| Accept Ack Type            | 15   | 2   | ID  | R   | N   |     | 0155 | This will always be AL for this MSH segment.                                                                                                               |
| Application Ack Type       | 16   | 2   | ID  | R   | N   |     | 0155 | This will always be AL for this MSH segment.                                                                                                               |

<span id="_Toc84256367" class="anchor"></span>Table 39: ZLF – Master File Update Segment – Required Segment

<u>Example</u>:

MSH\|^~\\\|CHCS\|\|VistA\|\|20020412163500\|\|MFN^M01\|0617-021021635\|P\|2.3.1\|\|\|AL\|AL

| Field Name              | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                           |
|-------------------------|------|-----|-----|-----|-----|-----|------|-----------------------------------------------------------------------|
| Record-Level Event Code | 1    | 3   | ID  | R   |     |     | 0180 | Record-Level Event Code. This will always be MUP.                     |
| MFN Control ID          | 2    | 20  | ST  | C   |     |     |      | This field will be the station number and the transmission date/time. |
| Effective Date/Time     | 3    | 26  | TS  | O   |     |     |      | Date/Time of Request.                                                 |
| Primary Key Value – MFE | 4    | 200 | NM  | R   | Y   |     |      | Medical Center Station Number.                                        |
| Primary Key Value Type  | 5    | 3   | ID  | R   | Y   |     | 0355 | The field will be CE for all segments.                                |

<span id="_Toc84256368" class="anchor"></span>Table 40: MSH – Message Header Segment – Required Segment

<u>Example</u>:

MFE\|MUP\|766-011214\|200110021345\|766\|CE

| Field Name                      | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                                                            |
|---------------------------------|------|-----|-----|-----|-----|-----|-----|--------------------------------------------------------------------------------------------------------|
| Request Type                    | 1    | 3   | NM  | R   |     |     |     | See Request Type table below.                                                                          |
| Requesting / Approving Official | 2    | 45  | ST  | R   |     |     |     | Name of person requesting or approving the action. Format^LAST NAME^FIRST NAME^MI^SUFFIX.              |
| Agency                          | 3    | 4   | ST  | R   |     |     |     | Agency Type. See Agency Table below. This table can be added to as necessary.                          |
| Reject Reason                   | 4    | 80  | ST  |     |     |     |     | This is a free text rejection reason. This will only be present if the request was denied or rejected. |

<span id="_Toc84256369" class="anchor"></span>Table 41: MFE – Master File Entry Segment – Required Segment

<u>Example</u>:

ZLF\|1\|CMOPPHARMACIST3,THREE\|2\|

ZLF Request Type

1.  Request to Activate Non-Controlled Substance Transmissions.
2.  Request to Activate Controlled Substance Transmissions.
3.  Activation Approval.
4.  Activation Disapproval.
5.  Inactivation for Non-Control Substances Transmissions.
6.  Inactivation for Control Substances Transmissions.

ZLF Agency Table.

1.  VA Medical Center
2.  US Army
3.  US Air Force
4.  US Navy
5.  US Marine Corp
6.  US Coast Guard
7.  Indian Health Service
8.  Public Health Service
9.  CHAMPVA
10. CHAMPUS
11. OTHER/Not Applicable

## Activation Acknowledgement Message (.SAC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH

MFE

ZLF

| Field Name                 | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                                                                                                                |
|----------------------------|------|-----|-----|-----|-----|-----|------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Field Separator            | 1    | 1   | ST  | R   | N   |     |      | HL7 recommended field separator.                                                                                                                           |
| Encoding Characters        | 2    | 4   | ST  | R   | N   |     |      | HL7 recommended encoding characters.                                                                                                                       |
| Sending Application        | 3    | 15  | ST  | R   | N   |     |      | The name of the application creating the batch.                                                                                                            |
| Receiving Application      | 5    | 30  | ST  | R   | N   |     |      | This is the application receiving the data.                                                                                                                |
| Message Creation Date/Time | 7    | 26  | TS  | R   | N   |     |      | Date and time the message was created on the sending station's system.                                                                                     |
| Message Type               | 9    | 7   | C   | R   | N   |     | 0076 | The type of message being sent. This will always be MFR^M02.                                                                                               |
| Message Control ID         | 10   | 20  | ST  | R   | N   |     |      | This is a number that uniquely identifies this message from all other messages. The format of the message number is station number-transmission date/time. |
| Processing ID              | 11   | 1   | ID  | R   | N   |     | 0103 | This will always be a P.                                                                                                                                   |
| Version ID                 | 12   | 8   | ID  | R   | N   |     | 0104 | This will always be 2.3.1.                                                                                                                                 |
| Accept Ack Type            | 15   | 2   | ID  | R   | N   |     | 0155 | This will always be NE for this MSH segment.                                                                                                               |
| Application Ack Type       | 16   | 2   | ID  | R   | N   |     | 0155 | This will always be NE for this MSH segment.                                                                                                               |

<span id="_Toc84256370" class="anchor"></span>Table 42: ZLF – Master File Update Segment – Required Segment

<u>Example</u>:

MSH\|^~\\\|VistA\|\|CHCS\|\|20010925202704\|\|MFR^M02\|766-011214\|P\|2.3.1\|NE\|NE

| Field Name              | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                           |
|-------------------------|------|-----|-----|-----|-----|-----|------|-----------------------------------------------------------------------|
| Record-Level Event Code | 1    | 3   | ID  | R   |     |     | 0180 | Record-Level Event Code. This will always be MUP.                     |
| MFN Control ID          | 2    | 20  | ST  | C   |     |     |      | This field will be the station number and the transmission date/time. |
| Effective Date/Time     | 3    | 26  | TS  | O   |     |     |      | Date/Time of Request                                                  |
| Primary Key Value – MFE | 4    | 200 | NM  | R   | Y   |     |      | Medical Center Station Number.                                        |
| Primary Key Value Type  | 5    | 3   | ID  | R   | Y   |     | 0355 | The field will be CE for all segments.                                |

<span id="_Toc84256371" class="anchor"></span>Table 43: MSA – Message Acknowledgment Segment – Required Segment

<u>Example</u>:

MFE\|MUP\|766-011214\|200110021345\|766\|CE

| Field Name                      | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                                                            |
|---------------------------------|------|-----|-----|-----|-----|-----|-----|--------------------------------------------------------------------------------------------------------|
| Request Type                    | 1    | 3   | NM  | R   |     |     |     | See Request Type table below.                                                                          |
| Requesting / Approving Official | 2    | 45  | ST  | R   |     |     |     | Name of person requesting or approving the action. Format^LAST NAME^FIRST NAME^MI^SUFFIX.              |
| Reject Reason                   | 4    | 80  | ST  |     |     |     |     | This is a free text rejection reason. This will only be present if the request was denied or rejected. |

<span id="_Toc84256372" class="anchor"></span>Table 44: MSH – Message Header Segment – Required Segment

<u>Example</u>:

ZLF\|2\| CMOPPHARMACIST3,THREE

ZLF Request Type

1.  Request to Activate Non Controlled Substance Transmissions.
2.  Request to Activate Controlled Substance Transmissions.
3.  Activation Approval.
4.  Activation Disapproval.
5.  Deactivation for Non Control Substances Transmissions.
6.  Deactivation for Control Substances Transmissions.

## Inactivation Acknowledgement Message (.SAC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH MSA

MSH – Message Header Segment – Required segment

| Field Name                 | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                                                                                                                 |
|----------------------------|------|-----|-----|-----|-----|-----|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Field Separator            | 1    | 1   | ST  | R   | N   |     |      | HL7 recommended field separator.                                                                                                                            |
| Encoding Characters        | 2    | 4   | ST  | R   | N   |     |      | HL7 recommended encoding characters.                                                                                                                        |
| Sending Application        | 3    | 15  | ST  | R   | N   |     |      | The name of the application creating the batch.                                                                                                             |
| Receiving Application      | 5    | 30  | ST  | R   | N   |     |      | This is the application receiving the data.                                                                                                                 |
| Message Creation Date/Time | 7    | 26  | TS  | R   | N   |     |      | Date and time the message was created on the sending station's system.                                                                                      |
| Message Type               | 9    | 7   | C   | R   | N   |     | 0076 | The type of message being sent. This will always be MFR^M02.                                                                                                |
| Message Control ID         | 10   | 20  | ST  | R   | N   |     |      | This is a number that uniquely identifies this message from all other messages. The format of the message number is station number- transmission date/time. |
| Processing ID              | 11   | 1   | ID  | R   | N   |     | 0103 | This will always be a P.                                                                                                                                    |
| Version ID                 | 12   | 8   | ID  | R   | N   |     | 0104 | This will always be 2.3.1.                                                                                                                                  |
| Accept Ack Type            | 15   | 2   | ID  | R   | N   |     | 0155 | This will always be NE for this MSH segment.                                                                                                                |
| Application Ack Type       | 16   | 2   | ID  | R   | N   |     | 0155 | This will always be NE for this MSH segment.                                                                                                                |

<span id="_Toc84256373" class="anchor"></span>Table 45: ARQ – Appointment Request Segment – Required Segment

<u>Example</u>:

MSH\|^~\\\|VistA\|\|CHCS\|\|20010925202704\|\|MFR^M02\|0111-011214\|P\|2.3.1\|NE\|NE

| Field Name           | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | ITEM# | Description                                                            |
|----------------------|------|-----|-----|-----|-----|-----|------|-------|------------------------------------------------------------------------|
| Acknowledgement Code | 1    | 2   | ID  | R   |     |     | 0008 | 00018 | Acknowledgement Code This will be CA.                                  |
| Message Control ID   | 2    | 20  | ST  | R   |     |     |      |       | Message Control ID. This will be same as on the preceding MSH segment. |
| Text Message         | 3    | 80  | ST  | O   |     |     |      |       | This will be null.                                                     |

<span id="_Toc84256374" class="anchor"></span>Table 46: MSH – Message Header Segment – Required Segment

<u>Example</u>:

MSA\|CA\|0111-011214\|

## Transmission Scheduling (.SCH)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH

ARQ

| Field Name                 | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                                                                                                                 |
|----------------------------|------|-----|-----|-----|-----|-----|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Field Separator            | 1    | 1   | ST  | R   | N   |     |      | HL7 recommended field separator.                                                                                                                            |
| Encoding Characters        | 2    | 4   | ST  | R   | N   |     |      | HL7 recommended encoding characters.                                                                                                                        |
| Sending Application        | 3    | 15  | ST  | R   | N   |     |      | The name of the application creating the batch. In the VA this will always be VistA.                                                                        |
| Receiving Application      | 5    | 30  | ST  | R   | N   |     |      | This is the application receiving the data.                                                                                                                 |
| Message Creation Date/Time | 7    | 26  | TS  | R   | N   |     |      | Date and time the message was created on the sending station’s system.                                                                                      |
| Message Type               | 9    | 7   | C   | R   | N   |     | 0076 | The type of message being sent. This will always be ‘SIU^SO7.’ Cancel SIU^S20.                                                                              |
| Message Control ID         | 10   | 20  | ST  | R   | N   |     |      | This is a number that uniquely identifies this message from all other messages. The format of the message number is station number- transmission date/time. |
| Processing ID              | 11   | 1   | ID  | R   | N   |     | 0103 | This will always be a P.                                                                                                                                    |
| Version ID                 | 12   | 8   | ID  | R   | N   |     | 0104 | This will always be 2.3.1.                                                                                                                                  |
| Accept Ack Type            | 15   | 2   | ID  | R   | N   |     | 0155 | This will always be AL for this MSH segment.                                                                                                                |
| Application Ack Type       | 16   | 2   | ID  | R   | N   |     | 0155 | This will always be AL for this MSH segment.                                                                                                                |

<span id="_Toc84256375" class="anchor"></span>Table 47: MSA – Message Acknowledgment Segment – Required Segment

<u>Example</u>:

MSH\|^~\\\|CHCS\|\|VistA\|\|2001121401000\|\|SIU^SO7\|0111-011214\|P\|2.3.1\|AL\|AL

| Field Name                      | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                                                   |
|---------------------------------|------|-----|-----|-----|-----|-----|-----|-----------------------------------------------------------------------------------------------|
| Placer Appointment ID           | 1    | 75  | EI  | R   |     |     |     | This is the Station ID.                                                                       |
| Request Event Reason            | 6    | 200 | CE  | O   |     |     |     | This is the code for the type of scheduling event. See table below.                           |
| Requested Start Date/Time Range | 11   | 53  | DR  | O   | Y   |     |     | This is the Date/Time the transmission schedule will begin.                                   |
| Repeating Interval              | 13   | 100 | RI  | O   |     |     |     | Repeating Interval. See Chapter 4, Section 4.4.2.                                             |
| Placer Contact Person           | 15   | 48  | XCN | R   | Y   |     |     | Name of the Point of Contact from the Medical Center. Format ^LAST NAME^FIRST NAME^MI^SUFFIX. |
| Placer Contact Phone Number     | 16   | 40  | XTN | O   | Y   |     |     | Phone Number of the point of contact in sequence 15.                                          |
| Entered By Person               | 19   | 48  | XCN | R   | Y   |     |     | The person who initiated the request. Format ^LAST NAME^FIRST NAME^MI^SUFFIX.                 |
| Entered By Phone Number         | 20   | 40  | XTN | O   | Y   |     |     | The phone number of the person initiating the request.                                        |

<span id="_Toc84256376" class="anchor"></span>Table 48: FHS – File Header Segment – Required Segment

### Request Event Reason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Non-Controlled Substance Transmission Auto Schedule.
2.  Controlled Substance Transmission Auto Schedule.
3.  Non-Controlled Substance Transmission Cancel Auto Schedule.
4.  Controlled Substance Transmission Cancel Auto Schedule.

<u>Example</u>:

ARQ\|10111\|\|\|\|\|1\|\|\|\|\|200112141000\|\|Q24H\|\|CMOPPHARMACIST3,THREE \|(000) 555-1212\|\|\| CMOPPHARMACIST3,THREE \|(000) 555-1212

## Schedule Acknowledgement (.HAC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH

MSA

| Field Name                 | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                                                                                                                 |
|----------------------------|------|-----|-----|-----|-----|-----|------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Field Separator            | 1    | 1   | ST  | R   | N   |     |      | HL7 recommended field separator.                                                                                                                            |
| Encoding Characters        | 2    | 4   | ST  | R   | N   |     |      | HL7 recommended encoding characters.                                                                                                                        |
| Sending Application        | 3    | 15  | ST  | R   | N   |     |      | The name of the application creating the batch. In the VA this will always be VistA.                                                                        |
| Receiving Application      | 5    | 30  | ST  | R   | N   |     |      | This is the application receiving the data.                                                                                                                 |
| Message Creation Date/Time | 7    | 26  | TS  | R   | N   |     |      | Date and time the message was created on the sending station’s system.                                                                                      |
| Message Type               | 9    | 7   | C   | R   | N   |     | 0076 | The type of message being sent. This will always be ‘SRR^SO7’ for the schedule, SRR^S20 for a schedule cancellation.                                        |
| Message Control ID         | 10   | 20  | ST  | R   | N   |     |      | This is a number that uniquely identifies this message from all other messages. The format of the message number is station number- transmission date/time. |
| Processing ID              | 11   | 1   | ID  | R   | N   |     | 0103 | This will always be a P.                                                                                                                                    |
| Version ID                 | 12   | 8   | ID  | R   | N   |     | 0104 | This will always be 2.3.1.                                                                                                                                  |
| Accept Ack Type            | 15   | 2   | ID  | R   | N   |     | 0155 | This will be NE for this segment.                                                                                                                           |
| Application Ack Type       | 16   | 2   | ID  | R   | N   |     | 0155 | This will be NE for this segment.                                                                                                                           |

<span id="_Toc84256377" class="anchor"></span>Table 49: BHS – Batch Header Segment – Required segment

<u>Example</u>:

MSH\|^~\\\|VistA\|\|CHCS\|\|2001121401100\|\|SRR^SO7\|0111-011214\|P\|2.3.1\|NE\|NE

| Field Name           | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | ITEM# | Description                                                            |
|----------------------|------|-----|-----|-----|-----|-----|------|-------|------------------------------------------------------------------------|
| Acknowledgement Code | 1    | 2   | ID  | R   |     |     | 0008 | 00018 | Acknowledgement Code This will be CA.                                  |
| Message Control ID   | 2    | 20  | ST  | R   |     |     |      |       | Message Control ID. This will be same as on the preceding MSH segment. |
| Text Message         | 3    | 80  | ST  | O   |     |     |      |       | This will be null.                                                     |

<span id="_Toc84256378" class="anchor"></span>Table 50: ORC – Common Order Segment – Required Segment

<u>Example</u>:

MSA\|CA\|10111-011214\|

## Batch Transmission Segments (.TRN)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FHS

BHS

ORC

{NTE\|2}

{NTE\|3}

{NTE\|4}

MSH

PID

\[NTE\|8\]

{\[ZML\]}

{\[ZSL\]}

ORC

RXE

{\[NTE\|7\]}

ZR1}

14. This group of segments can be repeated between the first ORC and BTS segments.

BTS

FTS

| Field Name               | SEQ# | LEN | DT  | R/O | REP | TBL | Description                                                                                               |
|--------------------------|------|-----|-----|-----|-----|-----|-----------------------------------------------------------------------------------------------------------|
| File Field Separator     | 1    | 1   | ST  | R   | N   |     | HL7 recommended field separator.                                                                          |
| File Encoding Characters | 2    | 4   | ST  | R   | N   |     | HL7 recommended encoding characters.                                                                      |
| File Sending Application | 3    | 15  | ST  | R   | N   |     | The name of the application creating the batch. In the VA this will always be VistA.                      |
| File Sending Facility    | 4    | 20  | ST  | R   | N   |     | The name of the sending medical center.                                                                   |
| File Receiving Facility  | 6    | 20  | ST  | R   | N   |     | The name of the receiving station.                                                                        |
| File Creation Date/Time  | 7    | 26  | ST  | R   | N   |     | The date and time the batch was created on the sending station system.                                    |
| File Control ID          | 11   | 20  | ST  | R   | N   |     | This field will be the file name. The file name is the batch number concatenated with the file extension. |

<span id="_Toc84256379" class="anchor"></span>Table 51: NTE\|2 – Refill Instructions Text – Required Segment

<u>Example</u>:

FHS\|^~\\\|CHCS\|MEDICAL CENTER NAME\|\|CMOP REDACTED\|20010928120135\|\|\|\|573- 013240530.TRN

| Field Name                  | SEQ# | LEN | DT  | R/O | REP | TBL | Description                                                                          |
|-----------------------------|------|-----|-----|-----|-----|-----|--------------------------------------------------------------------------------------|
| Batch Field Separator       | 1    | 1   | ST  | R   | N   |     | HL7 recommended field separator.                                                     |
| Batch Encoding Characters   | 2    | 3   | ST  | R   | N   |     | HL7 recommended encoding characters.                                                 |
| Batch Sending Application   | 3    | 15  | ST  | R   | N   |     | The name of the application creating the batch. In the VA this will always be VistA. |
| Batch Receiving Application | 5    | 15  | ST  | R   | N   |     | The name of the sending medical center.                                              |
| Batch Creation Date/Time    | 7    | 26  | TS  | R   | N   |     | The date and time the batch was created on the sending station system.               |
| Batch Name/ID/Type          | 9    | 20  | ST  | O   | N   |     | RAR^RAR                                                                              |
| Batch Control ID            | 11   | 20  | ST  | R   | N   |     | This is the transmission number.                                                     |

<span id="_Toc84256380" class="anchor"></span>Table 52: NTE\|3 – Non-Refill Instructions Text Segment– Required Segment

<u>Example</u>:

BHS\|^~\\\|Outside Agency Application Name\|\|VistA\|\|20011109144013\|\|RAR^RAR\|\|573- 013240530

| Field Name                     | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                                             |
|--------------------------------|------|-----|-----|-----|-----|-----|------|-----------------------------------------------------------------------------------------|
| Order Control                  | 1    | 2   | ID  | R   | N   |     | 0119 | This will always be a new order, NW.                                                    |
| Order Facility Name            | 21   | 60  | XON | O   | Y   |     |      | This field will contain the pharmacy division name and unique pharmacy division number. |
| Ordering Facility Address      | 22   | 106 | XAD | O   | Y   |     |      | This field contains the return mailing address for the sending pharmacy division.       |
| Ordering Facility Phone Number | 23   | 48  | XTN | O   | Y   |     |      | This is the phone number for the sending pharmacy division.                             |

<span id="_Toc84256381" class="anchor"></span>Table 53: NTE\|4 – Copay Instructions Text Segment – Required Segment

<u>Example</u>:

ORC\|NW\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|\|^^^^^^^573PHARMACY DIVISION&123\|PO BOX 123456^^REDACTED^FL^55555-5555\|(000) 555-5557

| Field Name               | SEQ# | LEN | DT  | R/O | REP | TBL | Description                                                                                                                                                                                                                                                               |
|--------------------------|------|-----|-----|-----|-----|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set ID = 2               | 1    | 1   | ST  | R   | N   |     | Set id for the segment.                                                                                                                                                                                                                                                   |
| Refill Instructions Text | 2    | 100 | FT  | R   |     |     | This is the standard free text refill instructions that will print for all refillable prescriptions in the patch. For backwards compatibility, this segment will always be present. If no data for the segment, the segment will be formatted with at least three spaces. |

<span id="_Toc84256382" class="anchor"></span>Table 54: MSH – Message Header Segment – Required Segment

\[NTE\] The Set ID field will identify the NTE segment (2=Refill Instructions; 3=Non-refill Instructions Narrative; 4=Copayment Narrative). The Comment field will contain the respective information.

<u>Example</u>:

NTE\|2\|Prescriptions (Rx’s) are NOT automatically

NTE\|2\|refilled. To request refills:

NTE\|2\|

NTE\|2\|(1) Call our TOLL FREE \# -\> 1-000-555-5550

NTE\|2\| Have your Social Security & Rx \#’s ready

NTE\|2\| OR

NTE\|2\|(2) Sign and mail your refill request(s)

NTE\|2\| Use the return address label provided

NTE\|2\|

NTE\|2\|Order your refills as soon as possible, AT

NTE\|2\|LEAST 14 DAYS before you run out

NTE\|2\|

NTE\|2\|ALL refills are MAILED. Please do NOT come

NTE\|2\|to the clinic for Rx refills

| Field Name               | SEQ# | LEN | DT  | R/O | REP | TBL | Description                                                                                                                                                                                                                                                                          |
|--------------------------|------|-----|-----|-----|-----|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set ID = 3               | 1    | 1   | ST  | R   | N   |     | Set id for the segment.                                                                                                                                                                                                                                                              |
| Refill Instructions Text | 2    | 100 | FT  | R   |     |     | This is the standard free text non-refillable instructions that will print for all non-refillable prescriptions in the batch For backwards compatibility, this segment will always be present. If no data for the segment, the segment will be formatted with at least three spaces. |

<span id="_Toc84256383" class="anchor"></span>Table 55: PID – Patient Identification Segment – Required segment

<u>Example</u>:

NTE\|3\| \*\* If NO REFILLS remain OR your Rx has

NTE\|3\| EXPIRED (too old) \*\* discuss this with

NTE\|3\| your VA PROVIDER at your next appt.

NTE\|3\|

NTE\|3\| If you will run out of medicine BEFORE

NTE\|3\| your next appt, call (555) 555-5555 to

NTE\|3\| make or change an appt.

| Field Name               | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                                                                                                                                                                                                                                            |
|--------------------------|------|-----|-----|-----|-----|-----|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Set ID = 4               | 1    | 1   | ST  | R   | N   |     |     | Set id for the segment.                                                                                                                                                                                                                                                                |
| Refill Instructions Text | 2    | 100 | FT  | R   |     |     |     | This is the standard free text copay instructions that will print for all prescriptions in the batch that have a copay charge. For backwards compatibility, this segment will always be present. If no data for the segment, the segment will be formatted with at least three spaces. |

<span id="_Toc84256384" class="anchor"></span>Table 56: NTE\|8 – Additional Patient Street Address Information Segment – Optional Segment

<u>Example</u>:

NTE\|4\| Questions about your bill? Please call

NTE\|4\| 1-888-555-5555 Ext. 5005 (TOLL FREE)

| Field Name                 | SEQ# | LEN | DT  | R/O | REP | TBL  | Description                                                                                                                                                          |
|----------------------------|------|-----|-----|-----|-----|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Field Separator            | 1    | 1   | ST  | R   | N   |      | HL7 recommended field separator.                                                                                                                                     |
| Encoding Characters        | 2    | 4   | ST  | R   | N   |      | HL7 recommended encoding characters.                                                                                                                                 |
| Sending Application        | 3    | 15  |     |     |     |      | The name of the application creating the batch. In the VA this will always be ‘VistA.’                                                                               |
| Receiving Application      | 5    | 30  | ST  | R   | N   |      | This is the application receiving the data. Where VA is the Dispensing Agency it will be ‘VistA.’                                                                    |
| Message Creation Date/Time | 7    | 26  | TS  | R   | N   |      | Date and time the message was created on the sending Station system.                                                                                                 |
| Message Type               | 9    | 7   | C   | R   | N   | 0076 | The type of message being sent. This will always be ‘ORM^O01.’                                                                                                       |
| Message Control ID         | 10   | 20  | ST  | R   | N   |      | This is a number that uniquely identifies this message from all other messages. The format of the message number is station number-transmission number-order number. |
| Processing ID              | 11   | 1   | ID  | R   | N   | 0103 | This will always be a P.                                                                                                                                             |
| Version ID                 | 12   | 8   | ID  | R   | N   | 0104 | This will always be 2.3.1.                                                                                                                                           |
| Accept Ack Type            | 15   | 2   | ID  | R   | N   | 0155 | This will always be NE.                                                                                                                                              |
| Application Ack Type       | 16   | 2   | ID  | R   | N   | 0155 | This will always be NE.                                                                                                                                              |

<span id="_Toc84256385" class="anchor"></span>Table 57: ZML – Multi-Rx Label Segment – Optional Segment

\[MSH-5\] Receiving Application is the name of the dispensing application.

\[MSH-10\] Message Control ID is the number that uniquely identifies the message. It is returned in MSA-2.

<u>Example</u>:

MSH\|^~\\\|SENDING AGENCY NAME\|\|VistA\|\|20010925202704\|\|ORM^O01\|573-013240530- 1794\|P\|2.3.1\|\|\|AL\|AL

| Field Name           | SEQ# | LEN | DT  | R/O | REP | QTY | Description                                                                                                                                                  |
|----------------------|------|-----|-----|-----|-----|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Patient ID           | 3    | 20  | C   | R   | N   |     | Patient SSN^Check Digit^Check Digit Scheme. Check digit scheme will be M11. HL7 P 2-15.                                                                      |
| Patient Name         | 5    | 48  | PN  | R   | N   |     | The name of the patient. Format will be ^LAST NAME^FIRST NAME^MIDDLE INITIAL^SUFFIX.                                                                         |
| Patient Address      | 11   | 106 | AD  | R   | Y   | 3   | The patient’s mailing address. See HL7 specification, 3.3.2.11 for format.                                                                                   |
| Patient Phone Number | 13   | 40  | TN  | O   | N   |     | The patient’s contact phone number.                                                                                                                          |
| Primary Language     | 15   | 60  | CE  | O   | N   |     | Patient’s primary language field is used to determine the language used to print the patient PMIS. “ENG” is sent for English, and “SPA” is sent for Spanish. |

<span id="_Toc84256386" class="anchor"></span>Table 58: ZSL – Suspense Label Segment – Optional Segment

\[PID-3\] This is the patient’s SSN, check digit and check digit scheme. Refer to HL7 Version

2.3.1 page 2-15.

\[PID-15\] Patient’s primary language field is used to determine the language used to print the patient PMIS. “ENG” is sent for English, and “SPA” is sent for Spanish.

<u>Example</u>:

PID\|\|\|000579013^1^M11\|\|CMOPPATIENT3,TWO\|\|\|\|\|\|123 OAK ST.^REDACTED^TX^75024\|\|(555) 555-4124\|ENG

| Field Name                | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description |
|---------------------------|------|-----|-----|-----|-----|-----|-----|-------------|
| Set Id = 8                | 1    | 4   | ST  | R   | N   |     |     |             |
| Additional Street Address | 2    | 200 | FT  | R   | N   |     |     |             |

<span id="_Toc84256387" class="anchor"></span>Table 59: ORC – Common Order Segment – Required Segment (HL7 2.3.1)

This segment is included for backwards compatibility.

<u>Example</u>:

NTE\|8\|\|\F\\F\SLIP 44

| Field Name        | SEQ# | LEN | DT  | R/O | REP | TBL | Description                                                                                                                                                      |
|-------------------|------|-----|-----|-----|-----|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Drug Name         | 1    | 40  | ST  | R   | N   |     | The free text drug name. (VA PRINT NAME).                                                                                                                        |
| Number of Refills | 2    | 3   | NM  | R   | N   |     | Total number of remaining refills.                                                                                                                               |
| Expiration Date   | 3    | 26  | TS  | R   | N   |     | Prescription expiration date.                                                                                                                                    |
| Rx Number         | 4    | 20  | ST  | R   | N   |     | This is the prescription number as assigned by the originating pharmacy.                                                                                         |
| Barcode           | 5    | 20  | ST  | R   | N   |     | This field is used by the VA pharmacy system to produce a barcode value that is recognized on the medical system. This barcode is used to enter the next refill. |

<span id="_Toc84256388" class="anchor"></span>Table 60: RXE – Pharmacy/Treatment Encoded Order Segment – Required Segment

\[ZML\] This segment is repetitive. It repeats for all the drugs for the patient

<u>Example</u>:

ZML\|FELODIPINE 10MG SA TAB\|1\|20011209\|200002833\|573-7291313 ZML\|LEVOTHYROXINE NA (SYNTHROID) 0.1MG TAB\|1\|20011209\|200012872\|573- 8048381

| Field Name    | SEQ# | LEN | DT  | R/O | REP | TBL | Description                                                              |
|---------------|------|-----|-----|-----|-----|-----|--------------------------------------------------------------------------|
| Drug Name     | 1    | 40  | ST  | R   | N   |     | The free text drug name. (VA PRINT NAME).                                |
| Suspense Date | 2    | 26  | TS  | R   | N   |     | The date the fill is suspended for processing.                           |
| Rx Number     | 3    | 20  | ST  | R   | N   |     | This is the prescription number as assigned by the originating pharmacy. |

<span id="_Toc84256389" class="anchor"></span>Table 61: NTE\|7 – Additional Medication Instructions Segment – Optional Segment

\[ZSL\] This segment is repetitive. It repeats for all suspended Rx’s for the patient.

<u>Example</u>:

ZSL\|FELODIPINE 10MG SA TAB\|20011209\|200002833

<table>
<caption><p><span id="_Toc84256390" class="anchor"></span>Table 62: ZR1 – Rx Order Additional Information Segment – Required Segment</p></caption>
<colgroup>
<col style="width: 21%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Name</th>
<th>SEQ#</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>REP</th>
<th>TBL</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Order Control</td>
<td>1</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td>N</td>
<td>0119</td>
<td>This will always be a new order. NW</td>
</tr>
<tr class="even">
<td>Placer Order Number</td>
<td>2</td>
<td>75</td>
<td>CM</td>
<td>R</td>
<td>N</td>
<td></td>
<td>This is the Rx Index. See Key Terms for the definition of the Rx Index.</td>
</tr>
<tr class="odd">
<td>Placer Group Number</td>
<td>4</td>
<td>22</td>
<td>EI</td>
<td>R</td>
<td>N</td>
<td></td>
<td><p>This field is two parts. The first part is the number of Rx’s in the patient order, the second number is the Sequence number of this Rx in the patient order.</p>
<p>Example: this patient order has five Rx's in it, this Rx is the second Rx in the order so this field will be 5^2.</p></td>
</tr>
<tr class="even">
<td>Quantity Timing</td>
<td>7</td>
<td>200</td>
<td>TQ</td>
<td>R</td>
<td>N</td>
<td></td>
<td>This field contains duration of the fill. Start date of the fill End date of the fill = Start date + days supply.</td>
</tr>
<tr class="odd">
<td>Entered By</td>
<td>10</td>
<td>80</td>
<td>CN</td>
<td>R</td>
<td>N</td>
<td></td>
<td>The entering clerk’s id number.</td>
</tr>
<tr class="even">
<td>Ordering Provider</td>
<td>12</td>
<td>80</td>
<td>CN</td>
<td>R</td>
<td>N</td>
<td></td>
<td>The name of the ordering provider.</td>
</tr>
<tr class="odd">
<td>Order Effective Date</td>
<td>15</td>
<td>26</td>
<td>TS</td>
<td>R</td>
<td>N</td>
<td></td>
<td>The effective date of the order.</td>
</tr>
</tbody>
</table>

<span id="_Toc84256390" class="anchor"></span>Table 62: ZR1 – Rx Order Additional Information Segment – Required Segment

<u>Example</u>:

ORC\|NW\|573-200002833F-4\|\|5^2\|\|\|^^^20010925^20011224\|\|\|10111\|\|^CMOPPHARMACIST29^ THREE^\|\|\|20001227

| Field Name                             | SEQ# | LEN | DT  | R/O | REP | TBL | Description                                                                                                                                               |
|----------------------------------------|------|-----|-----|-----|-----|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Quantity/Timing                        | 1    | 200 | TQ  | R   | N   |     | Quantity Requested.                                                                                                                                       |
| Give Code                              | 2    | 100 | CE  | R   | N   |     | This is a composite field that contains the unique VA product ID^VA Print Name^L.                                                                         |
| Give Amount – Minimum                  | 3    | 20  | NM  | R   | N   |     | Quantity Requested.                                                                                                                                       |
| Give Units                             | 5    | 60  | CE  | R   | N   |     | This field contains the units for the Give Amount as encoded by the pharmacy or treatment application. Example: TAB, CAP, GM, OZ etc.                     |
| Provider's Administration Instructions | 7    | 200 | CE  | R   | N   |     | This field will contain the first 80 characters of the provider's instructions (SIG).                                                                     |
| Number of Refills                      | 12   | 60  | NM  | R   | N   |     | This field contains the total original number of refills.                                                                                                 |
| Pharmacist Verifier ID                 | 14   | 20  | ST  | R   | N   |     | This is the pharmacist's id number on the sending station system. For the VA it will be the pharmacist's Local ID (DUZ) number.                           |
| Prescription Number                    | 15   | 20  | ST  | R   | N   |     | This is the Rx Index number as assigned by the originating pharmacy. This number has to match the Placer Order Number field on the preceding ORC Segment. |
| Number of Refills Remaining            | 16   | 20  | NM  | R   | N   |     | Number of refills remaining for this prescription.                                                                                                        |
| D/T of Most Recent Refill              | 18   | 26  | TS  | R   | N   |     | Date of the most recent fill dispensed.                                                                                                                   |

<span id="_Toc84256391" class="anchor"></span>Table 63: BTS – Batch Trailer Segment – Required Segment

<u>Example</u>:

RXE\|45\|L0139^LEVOTHYROXINE NA (SYNTHROID) 0.1MG TAB^L\|45\|\|TAB\|\|^TAKE 1 TABLET(S) BY MOUTH EVERY MORNING \|\|\|\|\|0\|\|10111\|200012872\|0\|\|20010925

<u>ADDITIONAL FIELD NOTES</u>:

\[RXE-1\] Quantity Requested

\[RXE-2\] Give Code identifies the substance ordered as encoded by the Pharmacy. The components, in order, are the VA Product ID, VA Product Name.

\[RXE-3\] Give Amount - Minimum is a required field but it will not be used in OP Version 2.0. It will always be a null value (“”).

\[RXE-5\] Give Units identifies the units for the give amount as encoded by the VA National Drug File.

\[RXE-7\] Providers Administration Instructions (SIG). This field is limited to 80 characters. Only the second component of this field is used.

Components: \<identifier (ST)\> ^ \<text (ST)\> ^ \<name of coding system (ST)\> ^ \<alternate identifier (ST)\> ^ \<alternate text (ST)\> ^ \<name of alternate coding system (ST)\>

Definition: This field contains the ordering provider’s instructions to the patient or the provider administering he drug or treatment. If coded, a user-defined table must be used; if free text (describing a custom V, mixture, or salve, for example), place the text in the second component, e.g., \|^this is a free text administration instruction\|.

\[RXE-12\] Number of Refills - Definition: This field contains the total original number of refills. Outpatient only.

\[RXE-14\] Pharmacist Verifier ID identifies the pharmacist who verified the order. The first component is the DFN pointer in the NEW PERSON file (#200) of VistA and the second component is the name.

\[RXE-15\] Prescription Number is the external Outpatient prescription number.

\[RXE-16\] Number of Refills Remaining - Definition: Number of refills remaining. This field is conditional because it is required when a prescription is dispensed to an outpatient. It is not relevant to inpatient treatment orders.

\[RXE-18\] D/T of Last Refill identifies the last date the patient received this particular drug (i.e., Last Dispense Date).

| Field Name                      | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                 |
|---------------------------------|------|-----|-----|-----|-----|-----|-----|---------------------------------------------|
| Set ID = 7                      | 1    | 4   | ST  | R   | N   |     |     |                                             |
| Patient Medication Instructions | 2    | 100 | FT  | R   | N   |     |     | This is field is limited to 100 characters. |

<span id="_Toc84256392" class="anchor"></span>Table 64: FTS – File Trailer Segment – Required Segment

The NTE\|7 segment carries SIG information when the RXE-7 field exceeds 80 characters. The NTE\|7 segment may repeat as many times as necessary to complete the SIG.

<u>Example</u>:

NTE\|7\|Take one tablet every four hours.

| Field Name         | SEQ# | LEN | DT  | R/O | REP | QTY | TBL   | Description                                                                                                                                                                                                                                                                         |
|--------------------|------|-----|-----|-----|-----|-----|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rx Number          | 1    | 20  | ST  | R   | N   |     |       | This is the Rx Index number as assigned by the originating pharmacy. This number has to match the Prescription Number field on the preceding RXE segment.                                                                                                                           |
| Rx Patient Status  | 2    | 20  | CE  | R   | N   |     |       | The patient's status.                                                                                                                                                                                                                                                               |
| Renewable          | 3    | 1   | ST  | O   | N   |     |       | A flag indicating whether this prescription is renewable. A 1 in this field indicates that the prescription is renewable. Null means the prescription is not renewable.                                                                                                             |
| Copayment          | 4    | 1   | ST  | O   | N   |     |       | A flag indicating whether this patient will be charged a copay for this prescription. A 1 means a copay charge is due. Null means no copay charge is due.                                                                                                                           |
| Safety Cap         | 5    | 1   | ST  | O   | N   |     |       | A flag to indicate the patient's preference for a safety cap. A 1 will indicate safety cap, null will be no safety cap.                                                                                                                                                             |
| Refill Text        | 6    | 8   | ST  | R   | N   |     |       | This is the free text. It will be formatted as refill number of maximum refills. Example: (1of10).                                                                                                                                                                                  |
| Clinic             | 7    | 40  | ST  | R   | N   |     |       | The free text name of the clinic where the prescription originated. (DoD Group Pharmacy).                                                                                                                                                                                           |
| Days Supply        | 8    | 3   | NM  | R   | N   |     |       | The days supply for the prescription.                                                                                                                                                                                                                                               |
| Rx Barcode Value   | 9    | 20  | ST  | R   | N   |     |       | This field is used by the VA pharmacy system to produce a barcode value that is recognized on the medical system. This barcode is used to enter the next refill. Barcode Data—Institution ID—Internal entry number from prescription file. (DoD – Letters RX then number “RX12345”. |
| Drug Warning       | 10   | 35  | ST  | O   | R   | 5   | APP B | This field contains the record number of the corresponding drug warning from the Drug Warning table.                                                                                                                                                                                |
| Mail Flag          | 11   | 2   | ST  | O   | N   |     |       | This field is reserved for future use.                                                                                                                                                                                                                                              |
| Rx Expiration Date | 12   | 26  | TS  | R   | N   |     |       | The date the prescription expires.                                                                                                                                                                                                                                                  |
| PMIS Data          | 13   | 10  | ST  | O   | N   |     |       | This is the record number for the PMIS sheet that will print with the prescription. This field is included for future enhancements.                                                                                                                                                 |

<span id="_Toc84256393" class="anchor"></span>Table 65: MSH – Message Header Segment – Required Segment

<u>Example</u>:

ZR1\|200012872\|ONSC\|1\|1\|0\|(1of1)\|INVERNESS/PC,LAB\|45\|573-8048381\|1~2~3\|\|20020101\|

| Field Name          | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                |
|---------------------|------|-----|-----|-----|-----|-----|-----|------------------------------------------------------------|
| Batch Message Count | 1    | 10  | ST  | R   | N   |     |     | This is the number of patient order messages in the batch. |
| Batch Comment       | 2    | 80  | ST  | O   | N   |     |     | This field is not used now.                                |
| Batch Totals        | 3    | 20  | ST  | R   | N   |     |     | This field will contain the number of Rx's in the batch.   |

<span id="_Toc84256394" class="anchor"></span>Table 66: MSA – Message Acknowledgement Segment – Required Segment

<u>Example</u>:

BTS\|50\|\|77

| Field Name            | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                                                                                               |
|-----------------------|------|-----|-----|-----|-----|-----|-----|-------------------------------------------------------------------------------------------------------------------------------------------|
| File Batch Count      | 1    | 10  | NM  | R   | N   |     |     | This is the number of batches in the file. A file can contain from one-to-many batches.                                                   |
| File Trailer Comments | 2    | 80  | ST  | O   | N   |     |     | This field will contain the free text reason the file was rejected by the receiving station. The sending station will not use this field. |

<span id="_Toc84256395" class="anchor"></span>Table 67: Batch Reject Reason Code Table

<u>Example</u>:

FTS\|1

## Batch Transmission Acknowledgement/Non-Acknowledgement (.TAC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH

MSA

| Field Name                 | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                                                                                                                                          |
|----------------------------|------|-----|-----|-----|-----|-----|------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Field Separator            | 1    | 1   | ST  | R   | N   |     |      | HL7 recommended field separator.                                                                                                                                                     |
| Encoding Characters        | 2    | 4   | ST  | R   | N   |     |      | HL7 recommended encoding characters.                                                                                                                                                 |
| Sending Application        | 3    | 15  | ST  | R   | N   |     |      | The name of the application creating the batch. Within the VA this will always be VistA. Outside Agencies will use the medical center name of origin.                                |
| Receiving Application      | 5    | 30  | ST  | R   | N   |     |      | This is the application receiving the data.                                                                                                                                          |
| Message Creation Date/Time | 7    | 26  | TS  | R   | N   |     |      | Date and time the message was created on the sending station's system.                                                                                                               |
| Message Type               | 9    | 7   | C   | R   | N   |     | 0076 | The type of message being sent. This will always be ORR^O02.                                                                                                                         |
| Message Control ID         | 10   | 20  | ST  | R   | N   |     |      | This is a number that uniquely identifies this message from all other messages. The format of the message number is station number-transmission date/time. Same value as \[BHS-11\]. |
| Processing ID              | 11   | 1   | ID  | R   | N   |     | 0103 | This will always be P.                                                                                                                                                               |
| Version ID                 | 12   | 8   | ID  | R   | N   |     | 0104 | This will be 2.3.1,                                                                                                                                                                  |
| Accept Ack Type            | 15   | 2   | ID  | R   | N   |     | 0155 | This will always be NE for this MSH segment.                                                                                                                                         |
| Application Ack Type       | 16   | 2   | ID  | R   | N   |     | 0155 | This will always be NE for this MSH segment.                                                                                                                                         |

<span id="_Toc84256396" class="anchor"></span>Table 68: FHS – File Header Segment – Required Segment

<u>Example</u>:

MSH\|^~\\\|VistA\|\|CHCS\|\|20010925202704\|\|ORM^O02\|573-013240530\|P\|2.3.1\|\|\|NE\|NE

| Field Name           | SEQ# | LEN | DT  | R/O | QTY | TBL  | ITEM# | Description                                                                                                                                                                                                       |
|----------------------|------|-----|-----|-----|-----|------|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Acknowledgement Code | 1    | 2   | ID  | R   |     | 0008 | 00018 | Acknowledgement Code.                                                                                                                                                                                             |
| Message Control ID   | 2    | 20  | ST  | R   |     |      |       | This is the Station Number and transmission date/time.                                                                                                                                                            |
| Text Message         | 3    | 80  | ST  | O   |     |      |       | This field will contain the reject reason code, the order sequence number, and Rx sequence number for any errors detected. Format will be Reason Code~Order Sequence Number~Rx Sequence Number. Field may repeat. |

<span id="_Toc84256397" class="anchor"></span>Table 69: BHS – Batch Header Segment – Required Segment

| REASON CODE | REASON TEXT                            | SEGMENT SEQUENCE |
|-------------|----------------------------------------|------------------|
| 1           | File Field Separator                   | FHS-1            |
| 2           | File Encoding Characters               | FHS-2            |
| 3           | File Sending Application               | FHS-3            |
| 4           | File Sending Facility                  | FHS-4            |
| 5           | File Receiving Facility                | FHS-6            |
| 6           | File Creation Date/Time                | FHS-7            |
| 7           | File Control ID                        | FHS-11           |
| 8           | Batch Field Separator                  | BHS-1            |
| 9           | Batch Encoding Characters              | BHS-2            |
| 10          | Batch Sending Application              | BHS-3            |
| 11          | Batch Receiving Application            | BHS-5            |
| 12          | Batch Creation Date/Time               | BHS-7            |
| 13          | Batch Name/ID/Type                     | BHS-9            |
| 14          | Batch Control ID                       | BHS-11           |
| 15          | Order Control                          | ORC-2            |
| 16          | Order Facility Name                    | ORC-21           |
| 17          | Ordering Facility Address              | ORC-22           |
| 18          | Ordering Facility Phone Number         | ORC-23           |
| 19          | REFILL INSTRUCTIONS                    | NTE\|2           |
| 20          | NON REFILL INSTRUCTIONS                | NTE\|3           |
| 21          | COPAY INSTRUCTIONS                     | NTE\|4           |
| 22          | Message Control ID MSH for each order  | MSH-10           |
| 23          | Patient ID                             | PID-3            |
| 24          | Patient Name                           | PID-5            |
| 25          | Patient Address                        | PID-11           |
| 26          | Patient Phone Number                   | PID-13           |
| 27          | Order Control                          | ORC-1            |
| 28          | Placer Order Number                    | ORC-2            |
| 29          | Placer Group Number                    | ORC-4            |
| 30          | Quantity Timing                        | ORC-7            |
| 31          | Entered By                             | ORC-10           |
| 32          | Ordering Provider                      | ORC-12           |
| 33          | Order Effective Date                   | ORC-15           |
| 34          | Quantity/Timing                        | RXE-1            |
| 35          | Give Code                              | RXE-2            |
| 36          | Give Amount – Minimum                  | RXE-3            |
| 37          | Give Units                             | RXE-5            |
| 38          | Provider's Administration Instructions | RXE-7            |
| 39          | Number of Refills                      | RXE-12           |
| 40          | Pharmacist Verifier ID                 | RXE-14           |
| 41          | Prescription Number                    | RXE-15           |
| 42          | Number of Refills Remaining            | RXE-16           |
| 43          | D/T of Most Recent Refill              | RXE-18           |
| 44          | Rx Number                              | ZR1-1            |
| 45          | Rx Patient Status                      | ZR1-2            |
| 46          | Renewable                              | ZR1-3            |
| 47          | Copayment                              | ZR1-4            |
| 48          | Safety Cap                             | ZR1-5            |
| 49          | Refill Text                            | ZR1-6            |
| 50          | Clinic                                 | ZR1-7            |
| 51          | Days Supply                            | ZR1-8            |
| 52          | Rx Barcode Value                       | ZR1-9            |
| 53          | Drug Warning                           | ZR1-10           |
| 54          | Mail Flag                              | ZR1-11           |
| 55          | Rx Expiration Date                     | ZR1-12           |
| 56          | Batch Message Count                    | BTS-1            |
| 57          | Batch Comment                          | BTS-2            |
| 58          | Batch Totals                           | BTS-3            |
| 59          | File Batch Count                       | FTS-1            |
| 60          | File Trailer Comments                  | FTS-2            |

<span id="_Toc84256398" class="anchor"></span>Table 70: MSH – Message Header Segment – Required Segment

<u>Examples</u>:

Transmission Acceptance: MSA\|CA\|573-013240530

Transmission Reject:

MSA\|CR\|573-013240530\|51~1~3^54~3~1

## Prescription Fulfillment (.QRY)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FHS

BHS

{MSH

PID

ORC

RXD

ZR2}

BTS

FTS

| Field Name               | SEQ# | LEN | DT  | R/O | REP | TBL | Description                                                                                                                                           |
|--------------------------|------|-----|-----|-----|-----|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| File Field Separator     | 1    | 1   | ST  | R   | N   |     | HL7 recommended field separator.                                                                                                                      |
| File Encoding Characters | 2    | 4   | ST  | R   | N   |     | HL7 recommended encoding characters.                                                                                                                  |
| File Sending Application | 3    | 15  | ST  | R   | N   |     | The name of the application creating the batch. Within the VA this will always be VistA. Outside Agencies will use the medical center name of origin. |
| File Sending Facility    | 4    | 20  | ST  | R   | N   |     | The name of the sending agency.                                                                                                                       |
| File Receiving Facility  | 6    | 20  | ST  | R   | N   |     | The name of the receiving agency.                                                                                                                     |
| File Creation Date/Time  | 7    | 26  | TS  | R   | N   |     | The date and time the batch was created on the sending station system.                                                                                |
| File Control ID          | 11   | 20  | ST  | R   | N   |     | This field will be the file name. The file name is the batch number concatenated with the file extension.                                             |

<span id="_Toc84256399" class="anchor"></span>Table 71: PID – Patient Identification Segment – Required Segment

<u>Example</u>:

FHS\|^~\\\|CHCS\|DoD\|\|VISTA \|20010928120135\|\|\|\|573_013240530.QRY

| Field Name                  | SEQ# | LEN | DT  | R/O | REP | TBL | Description                                                                          |
|-----------------------------|------|-----|-----|-----|-----|-----|--------------------------------------------------------------------------------------|
| Batch Field Separator       | 1    | 1   | ST  | R   | N   |     | HL7 recommended field separator.                                                     |
| Batch Encoding Characters   | 2    | 3   | ST  | R   | N   |     | HL7 recommended encoding characters.                                                 |
| Batch Sending Application   | 3    | 15  | ST  | R   | N   |     | The name of the application creating the batch. In the VA this will always be VistA. |
| Batch Receiving Application | 5    | 15  | ST  | R   | N   |     | The name of the receiving agency.                                                    |
| Batch Creation Date/Time    | 7    | 26  | TS  | R   | N   |     | The date and time the batch was created on the sending station system.               |
| Batch Control ID            | 11   | 20  | ST  | R   | N   |     | This is a unique number that identifies this batch of fulfillment data.              |

<span id="_Toc84256400" class="anchor"></span>Table 72: ORC – Common Order Segment – Required Segment

<u>Example</u>:

BHS\|^~\\\|Sending Agency\|\|Receiving Agency\|\|20011109144013\|\|\|\|013240530

| Field Name                 | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                                          |
|----------------------------|------|-----|-----|-----|-----|-----|------|--------------------------------------------------------------------------------------|
| Field Separator            | 1    | 1   | ST  | R   | N   |     |      | HL7 recommended field separator.                                                     |
| Encoding Characters        | 2    | 4   | ST  | R   | N   |     |      | HL7 recommended encoding characters.                                                 |
| Sending Application        | 3    | 15  | ST  | R   | N   |     |      | The name of the application creating the batch. In the VA this will always be VistA. |
| Receiving Application      | 5    | 30  | ST  | R   | N   |     |      | This is the application receiving the data.                                          |
| Message Creation Date/Time | 7    | 26  | TS  | R   | N   |     |      | Date and time the message was created on the sending station's system.               |
| Message Type               | 9    | 7   | C   | R   | N   |     | 0076 | The type of message being sent. This will always be 'RDS^R06.'                       |
| Message Control ID         | 10   | 20  | ST  | R   | N   |     |      | This the Rx Index.                                                                   |
| Processing ID              | 11   | 1   | ID  | R   | N   |     | 0103 | This will always be a P.                                                             |
| Version ID                 | 12   | 8   | ID  | R   | N   |     | 0104 | This will always be 2.3.1.                                                           |
| Accept Ack Type            | 15   | 2   | ID  | R   | N   |     | 0155 | This will always be AL for this MSH segment.                                         |
| Application Ack Type       | 16   | 2   | ID  | R   | N   |     | 0155 | This will always be AL for this MSH segment.                                         |

<span id="_Toc84256401" class="anchor"></span>Table 73: RXD – Pharmacy/Treatment Dispense Segment – Required Segment

<u>Example</u>:

MSH\|^~\\\|VistA\|\|CHCS\|\|20010925202704\|\|RDS^R06\|573-013240530\|P\|2.3.1\|\|\|AL\|AL

| Field Name           | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                                             |
|----------------------|------|-----|-----|-----|-----|-----|-----|-----------------------------------------------------------------------------------------|
| Patient ID           | 3    | 20  | C   | R   | N   |     |     | Patient SSN^Check Digit^Check Digit Scheme. Check digit scheme will be M11. HL7 P 2-15. |
| Patient Name         | 5    | 48  | PN  | R   | N   |     |     | The name of the patient. Format will be ^LAST NAME^FIRST NAME^MIDDLE INTITIAL^SUFFIX.   |
| Patient Address      | 11   | 106 | AD  | R   | Y   | 3   |     | The patient's mailing address. See HL7 specification, 3.3.2.11 for format.              |
| Patient Phone Number | 13   | 40  | TN  | O   | N   |     |     | The patient's phone number.                                                             |

<span id="_Toc84256402" class="anchor"></span>Table 74: ZR2 – Release Data Additional Information Segment – Required Segment

<u>Example</u>:

PID\|\|\|000579013^6^M11\|\|^CMOPPATIENT3^ONE^^\|\|\|\|\|\|123 OAK ST.^^REDACTED^TX^75024\|\|(555) 555-5541

| Field Name          | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                   |
|---------------------|------|-----|-----|-----|-----|-----|------|---------------------------------------------------------------|
| Order Control       | 1    | 2   | ID  | R   | N   |     | 0119 | This will always be OK for order complete or CA for Canceled. |
| Placer Order Number | 2    | 75  | CM  | C   | N   |     |      | This is the Rx Index. See definitions.                        |

<span id="_Toc84256403" class="anchor"></span>Table 75: BTS – Batch Trailer Segment – Required Segment

<u>Example</u>:

ORC\|OK\|573-200009492-2

| Field Name                | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                                                                                                                                                                                                                                                                                                     |
|---------------------------|------|-----|-----|-----|-----|-----|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Dispense Sub-ID Counter   | 1    | 4   | NM  | R   | N   |     |     | Refill Number. Number between 1 and 12.                                                                                                                                                                                                                                                                                                         |
| Dispense/Give Code        | 2    | 100 | CE  | R   | N   | 292 |     | This is a composite field that contains the unique VA product ID and VA PRINT NAME.                                                                                                                                                                                                                                                             |
| Date/Time Dispensed       | 3    | 26  | TS  | R   | N   |     |     | This is the date and time the prescription was packed.                                                                                                                                                                                                                                                                                          |
| Actual Dispense Amount    | 4    | 20  | NM  | R   | N   |     |     | This is the true dispense quantity.                                                                                                                                                                                                                                                                                                             |
| Prescription Number       | 7    | 20  | ST  | R   | N   |     |     | The unique Rx number generated by the sending station.                                                                                                                                                                                                                                                                                          |
| Dispense Notes            | 9    | 200 | ST  | O   | N   |     |     | This field will contain the reason the prescription could not be dispensed by the CMOP. If the prescription was dispensed this field will be null. This field is only used when the CMOP production system is returning the data to the CMOP VistA system. While the field allows 200 characters, this will contain a maximum of 40 characters. |
| Dispensing Provider       | 10   | 200 | XCN | O   | N   |     |     | This field contains the id number of the dispensing pharmacist. This data is only returned from the CMOP Production system to the CMOP VistA system. The data is not forwarded back to the medical center.                                                                                                                                      |
| Substance Lot Number      | 18   | 20  | ST  | O   | Y   | 5   |     | This is the lot number of the medication dispensed, it can be repeated up to five times.                                                                                                                                                                                                                                                        |
| Substance Expiration Date | 19   | 26  | TS  | O   | Y   | 5   |     | This is the expiration date for the lot number's dispensed.                                                                                                                                                                                                                                                                                     |

<span id="_Toc84256404" class="anchor"></span>Table 76: FTS – File Trailer Segment – Required Segment

<u>Example</u>:

Rx that is filled and sent to the patient: RXD\|1\|S0022^SIMVASTATIN 40MG TAB^L\|20010822081001\|45\|\|\|10014891\|\|\|\|\|\|\|\|\|\|\|0108064\|20020801

Rx that is not filled:

RXD\|1\|S0022^SIMVASTATIN 40MG TAB^L\|20010822081001\|0\|\|\|10014891\|\|INCORRECT

QTY – CORRECT AND RESEND\|\|\|\|\|\|\|\|\|\|

| Field Name              | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                                                                                                                                                |
|-------------------------|------|-----|-----|-----|-----|-----|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Carrier                 | 1    | 12  | ST  | R   | N   |     |     | This is the free text name of the mail carrier.                                                                                                                                            |
| Package Tracking Number | 2    | 60  | ST  | R   | N   |     |     | This is the tracking number used to track the package with the mail carrier.                                                                                                               |
| Prescription Number     | 3    | 20  | ST  | R   | N   |     |     | This unique Rx number generated by the sending station. This number has to match the prescription number field on the preceding RXD segment.                                               |
| Rx Drug Cost            | 4    | 20  | MO  | O   | N   |     |     | This is the drug cost at dispense time. Currently this field is not in used to return cost to the medical center. It is used to return drug costs to the VA CMOP by ‘Outsourcing’ vendors. |
| Dispensing Fee          | 5    | 20  | MO  | O   | Y   |     |     | This field contains any extra dispensing fee associated with filling the prescription.                                                                                                     |
| Mailing Cost            | 6    | 20  | MO  | O   | N   |     |     | This field contains mailing cost. This field is not in use but is defined for future use.                                                                                                  |

<span id="_Toc84256405" class="anchor"></span>Table 77: FHS – File Header Segment – Required Segment

<u>Example</u>:

Rx that is filled and sent to the patient:

ZR2\|CTC-USPS\|5161145008952133980\|10014891\|

Rx that is not filled:

ZR2\|CA

| Field Name          | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                |
|---------------------|------|-----|-----|-----|-----|-----|-----|------------------------------------------------------------|
| Batch Message Count | 1    | 10  | ST  | R   | N   |     |     | This is the number of patient order messages in the batch. |
| Batch Comment       | 2    | 80  | ST  | O   | N   |     |     | This field is not used now.                                |
| Batch Totals        | 3    | 20  | ST  | R   | N   |     |     | This field will contain the number of Rx's in the batch.   |

<span id="_Toc84256406" class="anchor"></span>Table 78: BHS – Batch Header Segment – Required Segment

<u>Example</u>:

BTS\|50\|\|77

| Field Name            | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                                                                                               |
|-----------------------|------|-----|-----|-----|-----|-----|-----|-------------------------------------------------------------------------------------------------------------------------------------------|
| File Batch Count      | 1    | 10  | NM  | R   | N   |     |     | This is the number of batches in the file. A file can contain from one-to-many batches.                                                   |
| File Trailer Comments | 2    | 80  | ST  | O   | N   |     |     | This field will contain the free text reason the file was rejected by the receiving station. The sending station will not use this field. |

<span id="_Toc84256407" class="anchor"></span>Table 79: MSH – Message Header Segment – Required Segment

<u>Example</u>:

FTS\|1

## Batch Prescription Fulfillment Acknowledgement (.QAC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FSH

BHS

{MSH

MSA}

BTS

FTS

| Field Name               | SEQ# | LEN | DT  | R/O | REP | TBL | Description                                                                          |
|--------------------------|------|-----|-----|-----|-----|-----|--------------------------------------------------------------------------------------|
| File Field Separator     | 1    | 1   | ST  | R   | N   |     | HL7 recommended field separator.                                                     |
| File Encoding Characters | 2    | 4   | ST  | R   | N   |     | HL7 recommended encoding characters.                                                 |
| File Sending Application | 3    | 15  | ST  | R   | N   |     | The name of the application creating the batch. In the VA this will always be VistA. |
| File Sending Facility    | 4    | 20  | ST  | R   | N   |     | The name of the sending medical center.                                              |
| File Receiving Facility  | 6    | 20  | ST  | R   | N   |     | The name of the receiving station.                                                   |
| File Creation Date/Time  | 7    | 26  | TS  | R   | N   |     | The date and time the batch was created on the sending station system.               |
| File Control ID          | 11   | 20  | ST  | R   | N   |     | This field will be the file name.                                                    |

<span id="_Toc84256408" class="anchor"></span>Table 80: BTS – Batch Trailer Segment – Required Segment

<u>Example</u>:

FHS\|^~\\\|MEDICAL CENTER NAME\|\|CMOP REDACTED\|\|20010928120135\|\|\|\|573- 013240530.QAC

| Field Name                  | SEQ# | LEN | DT  | R/O | REP | TBL | Description                                                                                                                                           |
|-----------------------------|------|-----|-----|-----|-----|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| Batch Field Separator       | 1    | 1   | ST  | R   | N   |     | HL7 recommended field separator.                                                                                                                      |
| Batch Encoding Characters   | 2    | 3   | ST  | R   | N   |     | HL7 recommended encoding characters.                                                                                                                  |
| Batch Sending Application   | 3    | 15  | ST  | R   | N   |     | The name of the application creating the batch. In the VA this will always be VistA.                                                                  |
| Batch Receiving Application | 5    | 15  | ST  | R   | N   |     | The name of the receiving medical center.                                                                                                             |
| Batch Creation Date/Time    | 7    | 26  | TS  | R   | N   |     | The date and time the batch was created on the sending station system.                                                                                |
| Batch Control ID            | 11   | 20  | ST  | R   | N   |     | This is a unique number that identifies this batch of fulfillment data acknowledgements. It will be the same number as the batch it is acknowledging. |

<span id="_Toc84256409" class="anchor"></span>Table 81: FTS – File Trailer Segment – Required Segment

<u>Example</u>:

BHS\|^~\\\|Outside Agency\|\|VistA\|\|20011109144013\|\|\|\|013240530

| Field Name                 | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                                                                                                                |
|----------------------------|------|-----|-----|-----|-----|-----|------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Field Separator            | 1    | 1   | ST  | R   | N   |     |      | HL7 recommended field separator.                                                                                                                           |
| Encoding Characters        | 2    | 4   | ST  | R   | N   |     |      | HL7 recommended encoding characters.                                                                                                                       |
| Sending Application        | 3    | 15  | ST  | R   | N   |     |      | The name of the application creating the batch. In the VA this will always be VistA.                                                                       |
| Receiving Application      | 5    | 30  | ST  | R   | N   |     |      | This is the application receiving the data.                                                                                                                |
| Message Creation Date/Time | 7    | 26  | TS  | R   | N   |     |      | Date and time the message was created on the sending station's system.                                                                                     |
| Message Type               | 9    | 7   | C   | R   | N   |     | 0076 | The type of message being sent. This will always be RRD^R04.’                                                                                              |
| Message Control ID         | 10   | 20  | ST  | R   | N   |     |      | This is a number that uniquely identifies this message from all other messages. The format of the message number is station number-transmission date/time. |
| Processing ID              | 11   | 1   | ID  | R   | N   |     | 0103 | Represented as P.                                                                                                                                          |
| Version ID                 | 12   | 8   | ID  | R   | N   |     | 0104 | Always 2.3.1.                                                                                                                                              |
| Accept Ack Type            | 15   | 2   | ID  | R   | N   |     | 0155 | This will always be NE for this MSH segment.                                                                                                               |
| Application Ack Type       | 16   | 2   | ID  | R   | N   |     | 0155 | This will always be NE for this MSH segment.                                                                                                               |

<span id="_Toc84256410" class="anchor"></span>Table 82: MSH – Message Header Segment – Required Segment

<u>Example</u>:

MSH\|^~\\\|CHCS\|\|VistA\|\|20010925202704\|\|RRD^R04\|573-013240530\|P\|2.3.1\|\|\|NE\|NE

MSA – Message Acknowledgement Segment – Required segment

| Field Name           | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | ITEM# | Description                                                                                                                                            |
|----------------------|------|-----|-----|-----|-----|-----|------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Acknowledgement Code | 1    | 2   | ID  | R   |     |     | 0008 | 00018 | Acknowledgement Code.                                                                                                                                  |
| Message Control ID   | 2    | 20  | ST  | R   |     |     |      |       | This is the Rx Index. See definition section.                                                                                                          |
| Text Message         | 3    | 80  | ST  | O   |     |     |      |       | Text Message - This field will contain the reject reason code and the free text rejection reason. If the message was accepted this field will be null. |

<span id="_Toc84256411" class="anchor"></span>Table 83: MFE – Master File Entry Segment – Required Segment

<u>Example</u>:

Rx that is successfully filed at the medical center: MSA\|CA\|516-11450-8954

Rx that can’t be filed at the medical center: MSA\|CR\|516-11450-8954\|2-RX ENTRY MISSING

REMOTE ERROR CONDITION

1.  Release date already exists
2.  Rx entry missing
3.  Fill mismatch
4.  Transmission number mismatch
5.  No CMOP event multiple
6.  Fill does not exist
7.  Other

| Field Name          | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                |
|---------------------|------|-----|-----|-----|-----|-----|-----|------------------------------------------------------------|
| Batch Message Count | 1    | 10  | ST  | R   | N   |     |     | This is the number of patient order messages in the batch. |
| Batch Comment       | 2    | 80  | ST  | O   | N   |     |     | This field is not used now.                                |
| Batch Totals        | 3    | 20  | ST  | R   | N   |     |     | This field will contain the number of Rx's in the batch.   |

<span id="_Toc84256412" class="anchor"></span>Table 84: ZND – NDF Data Segment - Required Segment

<u>Example</u>:

BTS\|50\|\|77

| Field Name            | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                                                                                               |
|-----------------------|------|-----|-----|-----|-----|-----|-----|-------------------------------------------------------------------------------------------------------------------------------------------|
| File Batch Count      | 1    | 10  | NM  | R   | N   |     |     | This is the number of batches in the file. A file can contain from one-to-many batches.                                                   |
| File Trailer Comments | 2    | 80  | ST  | O   | N   |     |     | This field will contain the free text reason the file was rejected by the receiving station. The sending station will not use this field. |

<span id="_Toc84256413" class="anchor"></span>Table 85: MSH – Message Header Segment - Required Segment

<u>Example</u>:

FTS\|1

## National Drug file Update (.NDF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH

MFE

ZND

| Field Name                 | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                                          |
|----------------------------|------|-----|-----|-----|-----|-----|------|--------------------------------------------------------------------------------------|
| Field Separator            | 1    | 1   | ST  | R   | N   |     |      | HL7 recommended field separator.                                                     |
| Encoding Characters        | 2    | 4   | ST  | R   | N   |     |      | HL7 recommended encoding characters.                                                 |
| Sending Application        | 3    | 15  | ST  | R   | N   |     |      | The name of the application creating the batch. In the VA this will always be VistA. |
| Receiving Application      | 5    | 30  | ST  | R   | N   |     |      | This is the application receiving the data.                                          |
| Message Creation Date/Time | 7    | 26  | TS  | R   | N   |     |      | Date and time the message was created on the sending station's system.               |
| Message Type               | 9    | 7   | C   | R   | N   |     | 0076 | The type of message being sent. This will always be 'MFN^M08.                        |
| Message Control ID         | 10   | 20  | ST  | R   | N   |     |      | This will be ‘NDF-UPDATE-Pxxx’ where xxx indicates the patch number.                 |
| Processing ID              | 11   | 1   | ID  | R   | N   |     | 0103 | This will always be a P.                                                             |
| Version ID                 | 12   | 8   | ID  | R   | N   |     | 0104 | This will always be 2.3.1.                                                           |
| Accept Ack Type            | 15   | 2   | ID  | R   | N   |     | 0155 | This will be AL.                                                                     |
| Application Ack Type       | 16   | 2   | ID  | R   | N   |     | 0155 | This will be AL.                                                                     |

<span id="_Toc84256414" class="anchor"></span>Table 86: MSA – Message Acknowledgement Segment – Required Segment

<u>Example</u>:

MSH\|^~\\\|VistA\|\|CHCS\|\|20010925202704\|\|MFN^M08\|20011215\|P\|2.3.1\|\|\|AL\|AL

| Field Name              | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                                                                                                                                                              |
|-------------------------|------|-----|-----|-----|-----|-----|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Record-Level Event Code | 1    | 3   | ID  | R   |     |     | 0180 | Record-Level Event Code this will be MUP.                                                                                                                                                                |
| MFN Control ID          | 2    | 20  | ST  | C   |     |     |      | This is a set of codes that indicates which field has been edited. Multiple codes can be listed. Multiple codes will be separated by the ^ character. This field can be null. See table below for codes. |
| Primary Key Value - MFE | 4    | 200 | ST  | R   |     |     |      | This field will be the 12 Digit NDC from the VA National Drug file system.                                                                                                                               |
| Primary Key Value Type  | 5    | 3   | ID  | R   |     |     | 0355 | The field will be CE for all segments.                                                                                                                                                                   |

<span id="_Toc84256415" class="anchor"></span>Table 87: Drug Warning Codes

Codes for MFN Control ID Table:

A New Entry in the VA Product File C Transmit to CMOP Flag Change

N New NDC entry in the VA NDC/UPN file V VA Print Name change

P VA Product ID

<u>Example</u>:

MFE\|MUP\|A^C^N^V\|\|051672400503\|CE

| Field Name                      | SEQ# | LEN | DT  | R/O | REP | QTY | TBL | Description                                                                                                                                                               |
|---------------------------------|------|-----|-----|-----|-----|-----|-----|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NDC                             | 1    | 12  | EI  | R   |     |     |     | This is the 12-digit NDC. Padded with a leading zero.                                                                                                                     |
| VA Trade Name                   | 2    | 50  | ST  | O   |     |     |     | This is the VA trade name for the drug.                                                                                                                                   |
| OTX Flag                        | 3    | 1   | ST  | O   |     |     |     | Flag that indicates that this is an over-the- counter drug. O – Over the counter; R – Prescription.                                                                       |
| Activation/Change Date          | 4    | 48  | ST  | O   |     |     |     | This field can have multiple dates. The dates correspond to the codes in MFE-2. Dates will be separated by the ^ character. This field can be null. Date format YYYYMMDD. |
| VA Product Name                 | 5    | 64  | ST  | O   |     |     |     | VA Product Name for the drug.                                                                                                                                             |
| VA Print Name                   | 6    | 40  | ST  | C   |     |     |     | VA Print Name. This field will be required if the drug can be dispensed by the CMOP facilities. This is the name that will print on the patient Rx label.                 |
| VA Product Identifier           | 7    | 5   | ST  | O   |     |     |     | VA code to uniquely identify the drug for CMOP processing.                                                                                                                |
| CMOP Flag                       | 8    | 1   | NM  | R   |     |     |     | Flag to indicate if this drug can be dispensed by a CMOP facility. 1 = Can be processed by CMOP facilities.                                                               |
| Control Substance Schedule Code | 9    | 1   | NM  | O   |     |     |     | Flag for the Federal Schedule for Controlled Substances. See Federal Schedule for Controlled Substances Table below.                                                      |
| Dosage Form                     | 10   | 30  | ST  | O   |     |     |     | VA Dosage Form.                                                                                                                                                           |
| Dispense Unit                   | 11   | 10  | ST  | O   |     |     |     | VA Dispense Unit.                                                                                                                                                         |
| VA Generic Name                 | 12   | 30  | ST  | O   |     |     |     | VA Generic Name for the drug.                                                                                                                                             |

<span id="_Toc84256416" class="anchor"></span>Table 88: CMOP Host Site Directory

Federal Schedule for Controlled Substances Table

0 Unscheduled

1 Schedule I

2 Schedule II

3 Schedule III

4 Schedule IV

5 Schedule V

<u>Example</u>:

ZND\|051672400503\|CARBAMAZEPINE 200MG TAB\|R\|19990217^19990217^20011031^20011031\|CARBAMAZEPINE 200MG TAB\|CARBAMAZEPINE 200MG TAB\|C1010\|1\|\|TAB\|\|CARBAMAZEPINE

## NDF Update Acknowledgement (.NAC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MSH

MSA

| Field Name                 | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | Description                                                                          |
|----------------------------|------|-----|-----|-----|-----|-----|------|--------------------------------------------------------------------------------------|
| Field Separator            | 1    | 1   | ST  | R   | N   |     |      | HL7 recommended field separator.                                                     |
| Encoding Characters        | 2    | 4   | ST  | R   | N   |     |      | HL7 recommended encoding characters.                                                 |
| Sending Application        | 3    | 15  | ST  | R   | N   |     |      | The name of the application creating the batch. In the VA this will always be VistA. |
| Receiving Application      | 5    | 30  | ST  | R   | N   |     |      | This is the application receiving the data.                                          |
| Message Creation Date/Time | 7    | 26  | TS  | R   | N   |     |      | Date and time the message was created on the sending station's system.               |
| Message Type               | 9    | 7   | C   | R   | N   |     | 0076 | The type of message being sent. This will always be 'MFR^M08.'                       |
| Message Control ID         | 10   | 20  | ST  | R   | N   |     |      | This will be ‘NDF-UPDATE-Pxxx’ where xxx indicates the patch number.                 |
| Processing ID              | 11   | 1   | ID  | R   | N   |     | 0103 | This will always be a P.                                                             |
| Version ID                 | 12   | 8   | ID  | R   | N   |     | 0104 | This will always be 2.3.1.                                                           |
| Accept Ack Type            | 15   | 2   | ID  | R   | N   |     | 0155 | This will be NE.                                                                     |
| Application Ack Type       | 16   | 2   | ID  | R   | N   |     | 0155 | This will be NE.                                                                     |

<u>Example</u>:

MSH\|^~\\\|CHCS\|\|VistA\|\|20010925202704\|\|MFR^M08\|20011215\|P\|2.3.1\|\|\|NE\|NE

| Field Name           | SEQ# | LEN | DT  | R/O | REP | QTY | TBL  | ITEM# | Description                                                                                                                                            |
|----------------------|------|-----|-----|-----|-----|-----|------|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Acknowledgement Code | 1    | 2   | ID  | R   |     |     | 0008 | 00018 | Acknowledgement Code: CA – Commit Accept or CR – Commit Reject.                                                                                        |
| Message Control ID   | 2    | 20  | ST  | R   |     |     |      |       | This is same as the MSH-10 field.                                                                                                                      |
| Text Message         | 3    | 80  | ST  | O   |     |     |      |       | Text Message - This field will contain the reject reason code and the free text rejection reason. If the message was accepted this field will be null. |

<u>Example</u>:

MSA\|CA\|20011215

# Appendix A: Drug Warnings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the drug warning codes associated with the DRUG WARNING field (#10) on the RXE segment. No more than five warning codes may be included for each prescription.

| No. | Drug Warning      | Warning Code                                                                                                              |
|-----|-------------------|---------------------------------------------------------------------------------------------------------------------------|
| 1   | DROWSINESS        | MAY CAUSE DROWSINESS- Alcohol may intensify this effect. USE CARE when driving or when operating dangerous machinery.     |
| 2   | FINISH            | IMPORTANT: Finish all this medication unless otherwise directed by prescriber.                                            |
| 3   | EMPTY STOMACH     | Take medication on an EMPTY STOMACH 1 hour before or 2-3 hours after a meal unless otherwise directed by your doctor.     |
| 4   | NO DAIRY PRODUCTS | Do not take antacids or iron preparations or eat dairy products within 1 hour of taking this medication.                  |
| 5   | WATER             | Take with plenty of WATER.                                                                                                |
| 6   | DISCOLORATION     | May cause discolored urine or feces.                                                                                      |
| 7   | DIURETIC K        | It may be advisable to drink a full glass of orange juice or eat a banana daily while on this medication.                 |
| 8   | NO ALCOHOL        | DO NOT DRINK ALCOHOLIC BEVERAGES when taking this medication.                                                             |
| 9   | ADVICE            | DO NOT TAKE non-prescription drugs without MEDICAL advice.                                                                |
| 10  | WITH FOOD         | TAKE WITH FOOD OR MILK.                                                                                                   |
| 11  | SUNLIGHT          | Avoid prolonged exposure to SUNLIGHT and finish all this medication unless otherwise directed by prescriber.              |
| 12  | SHAKE WELL        | SHAKE WELL.                                                                                                               |
| 13  | EXTERNAL          | For external use ONLY.                                                                                                    |
| 14  | STRENGTH          | NOTE DOSAGE STRENGTH.                                                                                                     |
| 15  | REFRIGERATE       | REFRIGERATE -DO NOT FREEZE.                                                                                               |
| 16  | DUPLICATE         | This prescription CANNOT be refilled without a written duplicate from your physician.                                     |
| 17  | EXPIRATION DATE   | Do not use after specified date.                                                                                          |
| 18  | NO REFILL         | THIS PRESCRIPTION CANNOT BE REFILLED.                                                                                     |
| 19  | SAME DRUG         | This is the same medication you have been getting. Color, size, or shape may appear different.                            |
| 20  | NO TRANSFER       | CAUTION: Federal law prohibits the transfer of this drug to any person other than the patient for whom it was prescribed. |

# Appendix B: CMOP Host Site Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| LOCATION     | DESIGNATION | NOTES           |
|--------------|-------------|-----------------|
| REDACTED, MA | CMOP-BED    |                 |
| REDACTED, SC | CMOP-CHAR   |                 |
| REDACTED, TX | CMOP-DAL    |                 |
| REDACTED, IL | CMOP-HINE   | AKA Great Lakes |
| REDACTED, KS | CMOP-LEAV   |                 |
| REDACTED, TN | CMOP-MURF   |                 |
| REDACTED, CA | CMOP-WLA    |                 |