---
title: PSO*7*156 Automation Interface Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Automation Interface
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*156
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: The Outpatient Pharmacy Automation Interface project provides an enhancement to the VISTA Outpatient Pharmacy package interface used to send data to non-VISTA pharmacy automation systems. Currently, the VISTA Health Level 7 (HL7) interface used in the Outpatient Pharmacy V. 7.0 package is written to
audience: 
keywords: 
  - pharmacy
  - outpatient
  - table
  - contents
  - parameters
  - protocol
  - interface
  - application
  - server
  - client
page_count: 0
word_count: 1435
section_count: 5
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p156_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p156_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

> ![](pso-7-156-automation-interface-release-notes/001.png)

OUTPATIENT PHARMACYAUTOMATION INTERFACE

####### RELEASE NOTES 

PSO\*7\*156

PSS\*1\*82

PSN\*4\*84

October 2004

V*IST*A Health Systems Design & Development

Table of Contents

# *(This page included for two-sided copying.)*


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying)
- [Introduction](#introduction)
  - [Project Enhancements](#project-enhancements)
- [Outpatient Pharmacy and Pharmacy Data Management Enhancements](#outpatient-pharmacy-and-pharmacy-data-management-enhancements)
  - [Field Updates](#field-updates)
  - [New and Revised Parameters and Options](#new-and-revised-parameters-and-options)
    - [- The Outpatient Pharmacy Site Parameter (Enter/Edit) \[PSO SITE PARAMETERS\] option has been modified to include the following new parameters:](#the-outpatient-pharmacy-site-parameter-enteredit-pso-site-parameters-option-has-been-modified-to-include-the-following-new-parameters)
- [HL7-Related Enhancements](#hl7-related-enhancements)
  - [Data Transmitted between VISTA and the Dispensing System](#data-transmitted-between-vista-and-the-dispensing-system)
    - [New Protocols](#new-protocols)
    - [New Application Parameters](#new-application-parameters)
    - [New Logical Link](#new-logical-link)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient Pharmacy Automation Interface project provides an enhancement to the V*IST*A Outpatient Pharmacy package interface used to send data to non-V*IST*A pharmacy automation systems. Currently, the V*IST*A Health Level 7 (HL7) interface used in the Outpatient Pharmacy V. 7.0 package is written to the American National Standards Institute (ANSI) approved healthcare Version 2.2. However, newer automation systems, such as the McKesson Pharmacy 2000, use an interface written to the newer HL7 standard, Version 2.4. Several medical centers use Class III programming to interface to these newer systems and have experienced repeated difficulties adapting the programming as changes in V*IST*A-related software are released. As a solution to this problem, the current interface is enhanced and upgraded to the current HL7 standards. This project will ensure that the interface is compatible with all current pharmacy automation systems used throughout the Veterans Health Administration (VHA).

This project includes enhancements to Outpatient Pharmacy software interfaces. It does not include interfaces to automated dispensing systems used for inpatient medications.

## Project Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software will provide the following enhancements:

- Updates the current Outpatient Pharmacy V.7.0 package HL7 interface to the current ANSI-approved HL7 V.2.4 standard.
- Transmits Outpatient Pharmacy data to multiple vendor systems utilized by VAMCs and receives dispensed prescription data from the vendor systems.
- Provides the ability to send updates to vendor systems through HL7 messaging when changes occur to the national drug file and DRUG file (#50).
- Supports bi-directional HL7 messaging.
- Adds new fields, and changes current field names.
- Uses the Businessware Interface Engine to pass data from V*IST*A to the dispensing systems, and back.

*(This page included for two-sided copying.)*

# Outpatient Pharmacy and Pharmacy Data Management Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The enhancements to Outpatient Pharmacy consist mostly of back-end updates; however, there have been some field name changes and new fields created, as well as new fields being sent in the HL7 messages. Also, the Outpatient Pharmacy site parameters have been modified, and new parameters have been created. For Pharmacy Data Management, one new option has been added.

When viewing a prescription, the View Prescription screen now displays the Lot \# and Manufacturer for a drug.

## Field Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are field names that have changed for this project.

|                                                    |                                   |                                  |
|----------------------------------------------------|-----------------------------------|----------------------------------|
| File Name and Number                               | Current Field Name and Number | New Field Name and Number    |
| PRESCRIPTION file (#52)                            | MAN EXPIRATION DATE field (#29)   | DRUG EXPIRATION DATE field (#29) |
| REFILL file (#52.1) of the PRESCRIPTION file (#52) | EXPIRATION DATE field (#13)       | DRUG EXPIRATION DATE field (#13) |

The following are new fields created to support this project.

|                                                     |                                          |
|-----------------------------------------------------|------------------------------------------|
| File Name and Number                            | New Field Name and Number            |
| OUTPATIENT SITE file (#59)                          | AUTOMATED DISPENSE field (#105)          |
| OUTPATIENT SITE file (#59)                          | FILE RELEASE DATE/TIME field (#105.1)    |
| OUTPATIENT SITE file (#59)                          | DISPENSE DNS NAME field (#2006)          |
| OUTPATIENT SITE file (#59)                          | DISPENSE DNS PORT NUMBER field (#2007)   |
| OUTPATIENT SITE file (#59)                          | ENABLE MASTER FILE UPDATE field (#105.2) |
| OUTPATIENT SITE file (#59)                          | DISPENSING SYSTEM PRINTER field (#2008)  |
| PRESCRIPTION file (#52)                             | FILLING PERSON field (#38.1)             |
| REFILL file (#52.1) of the PRESCRIPTION file (#52)  | CHECKING PHARMACIST field (#38.2)        |
| REFILL file (#52.1) of the PRESCRIPTION file (#52)  | FILLING PERSON field (#19)               |
| PARTIAL file (#52.2) of the PRESCRIPTION file (#52) | CHECKING PHARMACIST field (#20)          |
| PARTIAL file (#52.2) of the PRESCRIPTION file (#52) | FILLING PERSON field (#10)               |
| PARTIAL file (#52.2) of the PRESCRIPTION file (#52) | CHECKING PHARMACIST field (#11)          |
| PARTIAL file (#52.2) of the PRESCRIPTION file (#52) | DRUG EXPIRATION DATE field (#12)         |

## New and Revised Parameters and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This project creates new parameters and options, and also changes existing parameters and options.

### - The Outpatient Pharmacy *Site Parameter (Enter/Edit)* \[PSO SITE PARAMETERS\] option has been modified to include the following new parameters:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

  - AUTOMATED DISPENSE
  - FILE RELEASE DATE/TIME
  - DISPENSE DNS NAME
  - DISPENSE DNS PORT
  - ENABLE MASTER FILE UPDATE
  - DISPENSING SYSTEM PRINTER

> **NOTE:** Sites using McKesson dispensing systems should not turn on the ENABLE MASTER FILE UPDATE parameter. These sites can leave the field blank, or enter N for NO. At the time of national release, McKesson was not supporting the update of the DRUG file (#50) through the ENABLE MASTER FILE UPDATE parameter; however, they may this decision in the future. Check with your McKesson representative to determine if they are supporting the master file update functionality.

- The EXTERNAL INTERFACE parameter in the Outpatient Pharmacy *Site Parameter (Enter/Edit)* \[PSO SITE PARAMETERS\] option has been modified to include the new selection: SEND MARKED ORDERS AND PRINT LABEL.

The following are new or modified options:

- The *Send Entire Drug File to External Interface* \[PSS MASTER FILE ALL\] option lets the user send the Master File Update information for every entry in the DRUG file (#50) to all specified dispensing systems, regardless of Application Package Use specified. This option is available in the Pharmacy Data Management package.
- The *Reprint an Outpatient Rx Label* \[PSO RXRPT\] option and reprints done using the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option, now prompt the user with the following question:

> 'Do you want to send to External Interface Device? No//'

> If the External Interface is set only to send marked drugs, and the prescription selected does not have a marked drug, the new prompt does not display.

> This gives the user the flexibility to make a decision about reprinting, and prevents duplication of medication dispensed.

# HL7-Related Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient Pharmacy V. 7.0 HL7 interface has been updated to the HL7 V. 2.4 standard. The following sections highlight the changes that were made.

## Data Transmitted between V*IST*A and the Dispensing System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a new prescription is entered into the PRESCRIPTION file (#52), or a renewal, refill, or partial to any existing prescriptions are made, Outpatient Pharmacy V. 7.0 will create and send an HL7 message to the automated dispensing system. Additionally, when a dispensing system receives a request, and then dispenses medication, an HL7 message is sent to Outpatient Pharmacy V. 7.0. The activity log of the PRESCRIPTION file (#52) will be updated.

See the Outpatient Pharmacy Technical Manual/Security Guide for detailed information regarding HL7 message structure.

### New Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New protocols have been added to the Outpatient Pharmacy and the Pharmacy Data Management packages.

Outpatient Pharmacy

Four new protocols have been created to support building the HL7 message. These protocols are:

- *Outpatient Pharmacy Dispense Server* \[PSO EXT SERVER\] protocol
- *Outpatient Pharmacy Dispense Client* \[PSO EXT CLIENT\] protocol
- *Outpatient Pharmacy Completion Server* \[PSO DISP SERVER\] protocol
- *Outpatient Pharmacy Completion Client* \[PSO DISP CLIENT\] protocol

The *Outpatient Pharmacy Dispense Server* \[PSO EXT SERVER\] protocol has been added as a new event driver protocol for requesting prescriptions, and the *Outpatient Pharmacy Dispense Client* \[PSO EXT CLIENT\] protocol has been added as a subscriber to the new event driver. The *Outpatient Pharmacy Completion Server* \[PSO DISP SERVER\] protocol has been added as a new event driver protocol for completing prescriptions, and the *Outpatient Pharmacy Completion Client* \[PSO DISP CLIENT\] protocol has been added as a subscriber to the new event driver. These protocols are exported in the Patch PSO\*7\*156.

Pharmacy Data Management

Two new protocols have been created to send updates from the DRUG file (#50). These protocols are:

- *PDM Master File Update* \[PSS EXT MFU SERVER\] protocol
- *PDM Master File Update Client* \[PSS EXT MFU CLIENT\] protocol

The *PDM Master File Update* \[PSS EXT MFU SERVER\] protocol has been added as a new event driver protocol for sending updates from the DRUG file (#50), and the *PDM Master File Update Client* \[PSS EXT MFU CLIENT\] protocol has been added as a subscriber to the new event driver. These protocols are exported in the Patch PSS\*1\*82.

### New Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New application parameters have been added to the Outpatient Pharmacy and the Pharmacy Data Management packages.

Outpatient Pharmacy

Two new application parameters have been created to support building the HL7 message. These parameters are:

- PSO VISTA
- PSO DISPENSE

PSO VISTA has been added to the HL7 APPLICATION PARAMETER file (#771) and is exported as the Receiving Application of the *Outpatient Pharmacy Dispense Server* \[PSO EXT SERVER\] protocol. PSO DISPENSE has been added to the HL7 APPLICATION PARAMETER file (#771) and is exported as the Sending Application of the *Outpatient Pharmacy Completion Server* \[PSO DISP SERVER\] protocol.

Pharmacy Data Management

Two new application parameters have been created to send updates from the DRUG file (#50). These parameters are:

- PSS VISTA
- PSS DISPENSE.

PSS VISTA has been added to the HL7 APPLICATION PARAMETER file (#771) and is exported as the Sending Application of the *PDM Master File Update* \[PSS EXT MFU SERVER\] protocol. PSS DISPENSE has been added to the HL7 APPLICATION PARAMETER file (#771) and is exported as the Receiving Application of the *PDM Master File Update Client* \[PSS EXT MFU CLIENT\] protocol.

### New Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new HL7 logical link, PSO DISP from the HL LOGICAL LINK file (#870), is being exported as the Logical Link of the PSO DISP protocol. This link information will need to be edited to match the communication method of the interface if this interface is activated. For example, each site will need to set up the IP address and the port number of the Interface Engine located at the facility.