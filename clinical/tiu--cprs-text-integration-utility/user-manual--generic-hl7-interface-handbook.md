---
title: TIU Generic HL7 Interface Handbook
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: 
app_code: TIU
app_name: "CPRS: Text Integration Utility"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: 
  - 2
  - 200
  - 8925
  - 900010
  - 9000010
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - message
  - document
  - class
  - table
  - vista
  - patient
  - application
  - strong
  - contents
  - vendor
page_count: 0
word_count: 31351
section_count: 30
table_count: 75
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: August 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiuhl7.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiuhl7.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=65"
---

![](tiu-generic-hl7-interface-handbook/001.png)

Text Integration Utilities (TIU)

Generic HL7 Interface

Handbook

August 2019

VistA System Design & Development

Computerized Patient Record System Product Line

<span id="_Toc11371351" class="anchor"></span>Revision History

|                                         |              |                                  |                                    |
|-----------------------------------------|--------------|----------------------------------|------------------------------------|
| Event                                   | Date         | Pages                            | Tech Writer, Project Manager       |
| Initial release                         | October 2006 | All                              | <span class="mark">redacted</span> |
| VIE Migration to HealthConnect– updates | June 2019    | ROES -VIE / HC Migration related | <span class="mark">redacted</span> |
| CCR&A VistA to HSRM TIU Interface       | June 2019    | Patch TIU\*1\*323 related        | <span class="mark">redacted</span> |
| CCR&A VistA to HSRM TIU Interface       | Aug 2019     | Post Patch TIU\*1\*323 related   | <span class="mark">redacted</span> |
# Tables, Illustrations, and Figures


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Tables, Illustrations, and Figures](#tables-illustrations-and-figures)
- [Introduction](#introduction)
  - [Purpose of the HL7 Generic Interface](#purpose-of-the-hl7-generic-interface)
  - [Scope of the Manual](#scope-of-the-manual)
  - [Audience](#audience)
  - [Availability](#availability)
  - [## Messaging Workbench (MWB)](#messaging-workbench-mwb)
  - [Overview VistA Inbound and Outbound TIU HL7 Interfaces](#overview-vista-inbound-and-outbound-tiu-hl7-interfaces)
    - [VistA Inbound TIU HL7 Interfaces](#vista-inbound-tiu-hl7-interfaces)
    - [### VistA Outbound TIU HL7 Interfaces](#vista-outbound-tiu-hl7-interfaces)
- [# Getting Started – Configuring the Interface](#getting-started-configuring-the-interface)
  - [Introduction](#introduction-1)
  - [Physical Link](#physical-link)
  - [The HL7 Logical Link File \#870](#the-hl7-logical-link-file-870)
  - [The HL7 Application Parameter File \#771](#the-hl7-application-parameter-file-771)
  - [The Protocol File \#101](#the-protocol-file-101)
- [Vendor Setup](#vendor-setup)
- [VistA Interface Engine and HealthConnect](#vista-interface-engine-and-healthconnect)
  - [Essentials](#essentials)
- [Database Repository](#database-repository)
- [System Features](#system-features)
  - [Creating a progress note from an HL7 message](#creating-a-progress-note-from-an-hl7-message)
  - [HL7 Fields](#hl7-fields)
    - [### Unique Patient Identifier (one required)](#unique-patient-identifier-one-required)
    - [Patient Visit (optional)](#patient-visit-optional)
    - [### Text (required)](#text-required)
    - [Document Author (required)](#document-author-required)
    - [Activity Date/Time (required)](#activity-datetime-required)
    - [Create New TIU Document](#create-new-tiu-document)
    - [Expected Cosigner (conditionally required)](#expected-cosigner-conditionally-required)
    - [### Visit Number](#visit-number)
    - [Hospital Location](#hospital-location)
    - [Dictation Date/Time](#dictation-datetime)
    - [Episode Begin Date/Time (conditionally required)](#episode-begin-datetime-conditionally-required)
    - [Reference Date/Time](#reference-datetime)
    - [Surgical Case \# or Consult \# (conditionally required)](#surgical-case-or-consult-conditionally-required)
    - [Signature Status (required)](#signature-status-required)
    - [Document Completion Status](#document-completion-status)
    - [Document Availability](#document-availability)
  - [Delimiter values](#delimiter-values)
    - [Information about delimiters and handling of HL7 text](#information-about-delimiters-and-handling-of-hl7-text)
- [# Vendor Guidelines](#vendor-guidelines)
  - [Overview](#overview)
  - [Background of the VistA TIU Application](#background-of-the-vista-tiu-application)
    - [Assumptions](#assumptions)
  - [Generic HL7 Functions](#generic-hl7-functions)
    - [TIU Document: Progress Note](#tiu-document-progress-note)
    - [TIU Document: Consult](#tiu-document-consult)
    - [TIU Document: Discharge Summary](#tiu-document-discharge-summary)
    - [TIU Document: Surgery Report](#tiu-document-surgery-report)
- [Glossary](#glossary)
- [Appendix A: Messaging Workbench](#appendix-a-messaging-workbench)
  - [Overview](#overview-1)
  - [HL7 Message Profile](#hl7-message-profile)
  - [HL7 Message Profile](#hl7-message-profile-1)
  - [## Segments](#segments)
- [# Appendix B: Testing](#appendix-b-testing)
  - [Sample Test Plan](#sample-test-plan)
  - [Introduction](#introduction-2)
    - [1) ROES Standardized Local Titles](#1-roes-standardized-local-titles)
    - [2) The HL7 Logical Link File \#870 – Link for DDC](#2-the-hl7-logical-link-file-870-link-for-ddc)
    - [3) The HL7 Application Parameter File \#771 – TIUHL7 and ROES-PN applications](#3-the-hl7-application-parameter-file-771-tiuhl7-and-roes-pn-applications)
    - [4) & 5) The Protocol File \#101 – ROES Event & Subscriber Protocols](#4-5-the-protocol-file-101-roes-event-subscriber-protocols)
  - [Testing Plans for ROES progress note project](#testing-plans-for-roes-progress-note-project)
    - [6) Alpha Test Phase:](#6-alpha-test-phase)
    - [7) Beta Test Phase:](#7-beta-test-phase)
    - [8) Information Regarding Students](#8-information-regarding-students)
  - [Contact Information](#contact-information)
    - [9) TIU Team Contacts:](#9-tiu-team-contacts)
    - [10) DDC Contacts:](#10-ddc-contacts)
  - [Sample ROES Event and Subscriber Protocol Screen Prints](#sample-roes-event-and-subscriber-protocol-screen-prints)
  - [Appendix C: Setting Up TIU CCRA Interface Components](#appendix-c-setting-up-tiu-ccra-interface-components)
  - [Select HL LOGICAL LINK NODE: TIU1 TIUCCRAHL7 LOGICAL LINK--------------------------------------------------------------------------------NODE: TIUCCRA DESCRIPTION: +INSTITUTION: CHEYENNE VAMROCMAILMAN DOMAIN:AUTOSTART: EnabledQUEUE SIZE: 10LLP TYPE: TCPDNS DOMAIN:\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\HL7 LOGICAL LINK--------------------------------------------------------------------------------+----------------------TCP LOWER LEVEL PARAMETERS-------------------------+¦ TIUCCRA ¦¦ ¦¦ TCP/IP SERVICE TYPE: CLIENT (SENDER) ¦¦ TCP/IP ADDRESS: xx.xxx.xx.xxx ¦¦ TCP/IP PORT: xxxx ¦¦ TCP/IP PORT (OPTIMIZED): ¦¦ ¦¦ ACK TIMEOUT: 5 RE-TRANSMISION ATTEMPTS: 1 ¦¦ READ TIMEOUT: 5 EXCEED RE-TRANSMIT ACTION: restart ¦¦ BLOCK SIZE: SAY HELO: ¦¦ TCP/IP OPENFAIL TIMEOUT: ¦¦STARTUP NODE: PERSISTENT: NO ¦¦ RETENTION: 30 UNI-DIRECTIONAL WAIT: ¦+-------------------------------------------------------------------------+======================================================================================HL7 APPLICATION PARAMETER NAME:1 TIU CCRA SEND ACTIVE2 TIU HSRM RECEIVE ACTIVE=====================================================================================HL7 APPLICATION EDIT--------------------------------------------------------------------------------NAME: TIU CCRA SEND ACTIVE/INACTIVE: ACTIVEFACILITY NAME: 534 COUNTRY CODE: USAHL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ^\\MAIL GROUP: GMRCCCRA NOTIFICATIONS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\HL7 APPLICATION EDIT--------------------------------------------------------------------------------NAME: TIU HSRM RECEIV ACTIVE/INACTIVE: ACTIVEFACILITY NAME: 200 COUNTRY CODE: USAHL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ^\\MAIL GROUP:\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\==================================================================================Select PROTOCOL NAME: TIU1 TIU CCRA-HSRM MDM-T02 CLIENT TIU CCRA-HSRM MDM-T02 CLIENT2 TIU CCRA-HSRM MDM-T02 SERVER TIU CCRA-HSRM MDM-T02 SERVER==================================================================================HL7 INTERFACE SETUP PAGE 1 OF 2--------------------------------------------------------------------------------NAME: TIU CCRA-HSRM MDM-T02 CLIENTDESCRIPTION (wp): + \[Sends HL7 MDM-T02 v2.5.1 messages from VistA CCRA\]ENTRY ACTION:EXIT ACTION:TYPE: subscriber\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Exit Save Refresh QuitHL7 SUBSCRIBER PAGE 2 OF 2TIU CCRA-HSRM MDM-T02 CLIENT--------------------------------------------------------------------------------RECEIVING APPLICATION: TIU HSRM RECEIVRESPONSE MESSAGE TYPE: ACK EVENT TYPE: T02SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YESSECURITY REQUIRED?:LOGICAL LINK: TIUCCRAPROCESSING RTN:ROUTING LOGIC:\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\==================================================================================HL7 INTERFACE SETUP PAGE 1 OF 2--------------------------------------------------------------------------------NAME: TIU CCRA-HSRM MDM-T02 SERVERDESCRIPTION (wp): + \[Sends HL7 MDM-T02 v2.5.1 messages from VistA CC\]ENTRY ACTION:EXIT ACTION:TYPE: event driver\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\HL7 EVENT DRIVER PAGE 2 OF 2TIU CCRA-HSRM MDM-T02 SERVER--------------------------------------------------------------------------------+----------------------Sending Application Edit---------------------------+T¦ ¦¦ NAME: TIU CCRA SEND ACTIVE/INACTIVE: ACTIVE ¦¦ ¦¦ FACILITY NAME: 534 COUNTRY CODE: USA ¦¦ ¦R¦HL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ^\\ ¦¦ ¦¦ ¦¦ MAIL GROUP: GMRCCCRA NOTIFICATIONS ¦¦ ¦+-------------------------------------------------------------------------+HL7 EVENT DRIVER PAGE 2 OF 2+--------------------------HL7 SUBSCRIBER--------------------------------+---¦ TIU CCRA-HSRM MDM-T02 CLIENT ¦---¦------------------------------------------------------------------------¦TR¦ RECEIVING APPLICATION: TIU HSRM RECEIV ¦¦ ¦¦ RESPONSE MESSAGE TYPE: ACK EVENT TYPE: T02 ¦¦ ¦¦SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YES ¦RE¦ ¦¦ SECURITY REQUIRED?: ¦T¦ ¦¦ LOGICAL LINK: TIUCCRA ¦¦ ¦¦ PROCESSING RTN: ¦¦ ROUTING LOGIC: ¦+------------------------------------------------------------------------+HL7 EVENT DRIVER PAGE 2 OF 2TIU CCRA-HSRM MDM-T02 SERVER--------------------------------------------------------------------------------SENDING APPLICATION: TIU CCRA SENDTRANSACTION MESSAGE TYPE: MDM EVENT TYPE: T02MESSAGE STRUCTURE:PROCESSING ID: VERSION ID: 2.5.1ACCEPT ACK CODE: AL APPLICATION ACK TYPE: NERESPONSE PROCESSING RTN:SUBSCRIBERSTIU CCRA-HSRM MDM-T02 CLIENT\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Exit](#select-hl-logical-link-node-tiu1-tiuccrahl7-logical-link-node-tiuccra-description-institution-cheyenne-vamrocmailman-domainautostart-enabledqueue-size-10llp-type-tcpdns-domainhl7-logical-link-tcp-lower-level-parameters-tiuccra-tcpip-service-type-client-sender-tcpip-address-xxxxxxxxxx-tcpip-port-xxxx-tcpip-port-optimized-ack-timeout-5-re-transmision-attempts-1-read-timeout-5-exceed-re-transmit-action-restart-block-size-say-helo-tcpip-openfail-timeout-startup-node-persistent-no-retention-30-uni-directional-wait-hl7-application-parameter-name1-tiu-ccra-send-active2-tiu-hsrm-receive-activehl7-application-edit-name-tiu-ccra-send-activeinactive-activefacility-name-534-country-code-usahl7-field-separator-hl7-encoding-characters-mail-group-gmrcccra-notificationshl7-application-edit-name-tiu-hsrm-receiv-activeinactive-activefacility-name-200-country-code-usahl7-field-separator-hl7-encoding-characters-mail-groupselect-protocol-name-tiu1-tiu-ccra-hsrm-mdm-t02-client-tiu-ccra-hsrm-mdm-t02-client2-tiu-ccra-hsrm-mdm-t02-server-tiu-ccra-hsrm-mdm-t02-serverhl7-interface-setup-page-1-of-2-name-tiu-ccra-hsrm-mdm-t02-clientdescription-wp-sends-hl7-mdm-t02-v251-messages-from-vista-ccraentry-actionexit-actiontype-subscriberexit-save-refresh-quithl7-subscriber-page-2-of-2tiu-ccra-hsrm-mdm-t02-client-receiving-application-tiu-hsrm-receivresponse-message-type-ack-event-type-t02sending-facility-required-yes-receiving-facility-required-yessecurity-requiredlogical-link-tiuccraprocessing-rtnrouting-logichl7-interface-setup-page-1-of-2-name-tiu-ccra-hsrm-mdm-t02-serverdescription-wp-sends-hl7-mdm-t02-v251-messages-from-vista-ccentry-actionexit-actiontype-event-driverhl7-event-driver-page-2-of-2tiu-ccra-hsrm-mdm-t02-server-sending-application-edit-t-name-tiu-ccra-send-activeinactive-active-facility-name-534-country-code-usa-rhl7-field-separator-hl7-encoding-characters-mail-group-gmrcccra-notifications-hl7-event-driver-page-2-of-2-hl7-subscriber-tiu-ccra-hsrm-mdm-t02-client-tr-receiving-application-tiu-hsrm-receiv-response-message-type-ack-event-type-t02-sending-facility-required-yes-receiving-facility-required-yes-re-security-required-t-logical-link-tiuccra-processing-rtn-routing-logic-hl7-event-driver-page-2-of-2tiu-ccra-hsrm-mdm-t02-server-sending-application-tiu-ccra-sendtransaction-message-type-mdm-event-type-t02message-structureprocessing-id-version-id-251accept-ack-code-al-application-ack-type-neresponse-processing-rtnsubscriberstiu-ccra-hsrm-mdm-t02-clientexit)
- [Index](#index)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose of the HL7 Generic Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the project is to create a generic Health Level Seven (HL7) interface to Text Integration Utilities (TIU) that will support the upload of a wide-range of textual documents from Commercial-Off-the-Shelf (COTS) applications in use now and in the future at Veteran Administration (VA) Medical Centers. This project was created in response to multiple TIU interface requests, most notably from the Resident Assessment Instrument/Minimum Data Set (RAI/MDS) application by AccuMed Software. Other projects interested in the interface are the Remote Order Entry System (ROES) software used by the Denver Distribution Center (DDC), the Precision Data Solutions Transcription Service software, and the VA Home Telehealth software.

The project creates a single COTS/application interface specification to allow textual documents to be uploaded and displayed in CPRS. This allows clinicians to view information from the COTS package without leaving the patient’s electronic medical record.

## Scope of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This handbook is meant to contain all information needed to set up and operate the HL7 Generic Interface.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is an interim manual for use during testing of the HL7 Generic Interface. Anyone needing information with respect to this software should be able to find it in this handbook.

## Availability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The current copy of this document is available on the VA intranet at: <http://vista.med.va.gov/tiu/> select Patches & Enhancements then User Docs next to Patch \#200.

Anyone with comments or corrections on the handbook may contact the technical writer directly at <span class="mark">REDACTED</span> or 801-588-5029.

## ## Messaging Workbench (MWB)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MWB is a tool that facilitates the creation of HL7 2.4 message profile definitions. MWB supports exporting of the message metadata into HL7v2 Message Conformance Profile format.

The MWB is a tool for analysts and developers that facilitates the construction, documentation and reporting of message specifications as well as HL7 Conformance profiles. It follows the standards set by the HL7 version 2.4 Conformance Special Interest Group (SIG) and produces profiles that are interoperable with other HL7 compliant messaging tools. In addition to its profile documentation function, this tool includes other features to assist messaging developers, such as reverse engineering, message instance analysis and message instance validation.

The MWB is the first freeware tool available for creating message profiles. The MWB developer works for VHA and is an active member of the HL7 Conformance Special Interest Group (SIG) and the tool has evolved with input from this SIG. The MWB tool is used extensively within VHA for developing and documenting HL7 messages.

MWB HL7 message profiles for TIU HL7 are available to any vendor who wishes to download and use the MWB tool. A Word document generated by the tool is also available to provide the workbench information in a readable/printable format.

The MWB software can be downloaded from the VHA Intranet:

<http://vista.med.va.gov/messaging/> then select VistA HL7 Website, then follow the link to HL7 Messaging Workbench.

The MWB software can also be downloaded from the HL7 website [<u>www.hl7.org</u>](file:///C:\Users\vhaisdsafkol\AppData\Local\Microsoft\Windows\INetCache\Content.Outlook\AppData\Local\Microsoft\Windows\Temporary%20Internet%20Files\Content.IE5\PD7F0DPK\www.hl7.org). From the home page heading “Committees”, select

Special Interest Groups (SIG)

Conformance

Documents and Presentations

There is a good tutorial on HL7 on the VistA HL7 webpage. To access it go to the VistA HL7 website at: <http://vista.med.va.gov/messaging>. Then follow the links to HL7 Documents and Presentations. From this page scroll down until you fine Archived Documents and Presentations then select HL7 1.6 Tutorial.ppt.

## Overview VistA Inbound and Outbound TIU HL7 Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistA Inbound TIU HL7 Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Generic HL7 enhances the TIU application to allow textual documents created by non-Veteran Health Information System and Technology Architecture (VistA) applications to be uploaded and displayed in the Computerized Patient Record System (CPRS). This will meet the identified need to provide document integration between COTS and other non-VistA applications in use at medical centers and CPRS/TIU. The end result will create an improved electronic medical record by bringing into CPRS additional documentation in support of patient care and treatment.

The interface will replace the copy and pasting. It will save clinicians time by alleviating the necessity to log onto a COTS server to retrieve patient information. It will save time for clerical staff who manually will add documents into TIU.

The COTS package connects to the VA computer system and send an HL7 message to the VistA Interface Engine (VIE). VIE sends the message to the Generic HL7 application. The Generic HL7 application stores the message in TIU

Currently all VIE interfaces are being migrated to HC. This Manual has been updated to specifically to reflect the migration of the ROES HL7 interfaces with VistA from VIE to HC, until all TIU COTS interfaces have been migrated from VIE to HC. New COTS TIU implementations are required to be configured with HealthConnect as messaging middleware.

ROES Application has migrated from using VistA Interface Engine (VIE) as messaging middleware to HealthConnect (HC). All HL7 messaging rules and descriptions that describe VIE throughout this document will apply to HC interfaces for ROES, and future COTS TIU HL7 interfaces.

### ### VistA Outbound TIU HL7 Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Community Care Referrals and Authorizations (CCR&A) project has implemented a new TIU interface that is sending the Community Care Consult /Progress Notes, entered in CPRS, from VistA to HealthShare Referral Management (HSRM) system.

This functionality has been released with TIU\*1\*32 VistA patch.

VistA connects to HealthConnect (HC) as messaging middleware, that sends the HL7 v 2.5.1 MDM-T02 message to HSRM.

The generic the HL7 VistA components definitions as described in this document apply also for this VistA Outgoing interface.

The specifics of installing this interface are described in the TIU\*1\*323 Patch Description.

Examples of setting up the HL7 VistA components (Application Parameters, HL7 Protocols and HL7 Logical Link) are provided in Appendix C: Setting Up TIUCCRA Interface Components.

# # Getting Started – Configuring the Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Text Integration Utilities (TIU) Generic HL7 Interface must be configured before HL7 messages may be received and processed to create or update TIU documents. Each step detailed below will provide an explanation regarding the configuration as it relates both to TIU and VistA HL7 messaging for this interface. For further information regarding VistA HL7 messaging, please refer to the HL7 documentation found at the VistA Documentation Library (<http://www.va.gov/vdl/>) under “Infrastructure: HL7” and <http://www.hl7.org>.

For this guide, the TIU Generic HL7 Interface (TIUHL7) consists of the following components:

- Logical Link(s)
- Receiving Application
- Event Driver
- Subscriber
- Sending Application

<span id="_Toc145664620" class="anchor"></span>Generic HL7 Components and Data Flow for using HealthConnect / VIE

![](tiu-generic-hl7-interface-handbook/002.png)

## Physical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The physical link between an external contractor and any VHA entity would be satisfied with a client VPN account. Reference this document:

<https://vaww.admin.vpn.va.gov/one-va-vpn/home/ConnectionOptions.ppt>

Outlines what justifies the different kinds of connections.

The following are general guidelines with respect to information needed to obtain an account:

The Contracting Officer Technical Representative (COTR) for the contract should contact the local ISO. The ISO needs to know:

- The name of the contractor
- The IP address(es) they need to access
- Last 4 of their SSN
- Email address
- Phone Number
- Company Name
- Address

At a minimum, the contractor must have a Background Investigation (BI) on file or in process. This requirement is usually stipulated in the contract and the COTR should be able to provide information on that as well.

The ISO will direct the contractor to on-line VA security awareness training and privacy training. This training is required prior to a VPN account being provided.

The ISO will request a VA windows account from their local IRM for the contractor (used by the VPN for authentication)

The contractor must sign a VA Rules of Behavior and any other documentation required at the local level.

The ISO will provide the contractor with their VA Windows account and VPN media.

## The HL7 Logical Link File \#870

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Logical links describe the complete network path to a given system. The first LOGICAL LINK to configure (*not* included in the TIU\*1\*200 distribution) will be the link over which all incoming HL7 messages will be received. Your site should already have a link ready for this use:

- The TCP/I Port for the link should be set to 5000.
- The LLP type for the links should be set to TCP.
- The device Type for the links should be set to Multi Listener.
- The Autostart for the link should be set to Enabled.

Please contact your IRM staff or site manager to find the name of the link to use.

The next link to configure is the link to the sender’s system. TIU will use this link for the transmission of APPLICATION ACKNOWLEDGMENTS. You will need to know the IP Address and Port \# of the sender’s system.

From the HL7 Main Menu Option, select the Interface Developer Options menu.

To set up or edit link definitions, use the “Link Edit” option, on the Interface Developer Options menu:

Select Interface Developer Options Option: Link Edit

Select HL LOGICAL LINK NODE: TIUHL7 EX

HL7 LOGICAL LINK

-----------------------------------------------------------------------

NODE: TIUHL7 EX

INSTITUTION:

DOMAIN:

AUTOSTART: Enabled

QUEUE SIZE: 10

LLP TYPE: TCP

-----------------------------------------------------------------------

If your site is using a VistA Interface Engine (VIE) or HealthConnect (HC), this link should only need to be configured once. Once setup, it may be used by multiple subscribing protocols. If your site is not using a VIE, a descriptive name is helpful in troubleshooting link problems and errors. Rename the link if desired.

Example Link Name: *TIUHL7 VIE or TIUHL7 HC*

Enter your site information in the Institution and Domain fields; this information is optional and may be left blank.

Tab down to the LLP Type field and press \<Enter\> or \<Return\>. The option then presents a form to edit the fields specific to the LLP Type of the selected Link:

┌──────────────────────TCP LOWER LEVEL PARAMETERS─────────────────────────┐

│ TIUHL7 EX │

│ │

│ TCP/IP SERVICE TYPE: Client (Sender) │

│ TCP/IP ADDRESS: 192.168.1.1 │

│ TCP/IP PORT: 5000 │

│ │

│ │

│ ACK TIMEOUT: RE-TRANSMISION ATTEMPTS: │

│ READ TIMEOUT: EXCEED RE-TRANSMIT ACTION: │

│ BLOCK SIZE: SAY HELO: │

│ │

│STARTUP NODE: PERSISTENT: No │

│ RETENTION: UNI-DIRECTIONAL WAIT: │

└─────────────────────────────────────────────────────────────────────────┘

TCP/IP Service Type must be set as “Client (Sender)”. Enter the sending application’s IP Address and Port \# to be used. Save the changes and return to the HL7 Main Menu Option.

From the HL7 Main Menu Option, select the Filer and Link Management Options menu.

To test the link, select “Ping (TCP Only)” and at the prompt “Select HL LOGICAL LINK NODE:” enter the name of the link entered. The message “PING Worked” should be displayed. If you do not see this message, ensure that the receiving system has been configured and setup properly.

After the PING portion, that the link must be started. Here’s the menu and option:

Select HL7 Main Menu Option: FILER AND Link Management Options

SM Systems Link Monitor

FM Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Select Filer and Link Management Options Option: SL Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE:

## The HL7 Application Parameter File \#771

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entries in this file are used to define the sending and receiving applications for VistA HL7. Each sending and receiving application must be defined separately.

From the HL7 Main Menu Option, select the Interface Developer Options menu. To set up or edit HL7 Applications, use the “Application Edit” option, on the Interface Developer Options menu:

Select Interface Developer Options Option: Application Edit

Select HL7 APPLICATION PARAMETER NAME: TIUHL7 EX RECEIVING APP

HL7 APPLICATION EDIT

-----------------------------------------------------------------------------

NAME: TIUHL7 EX RECEI ACTIVE/INACTIVE: INACTIVE

FACILITY NAME: \<required\> COUNTRY CODE: US

HL7 FIELD SEPARATOR: ^ HL7 ENCODING CHARACTERS: ~\|\\

MAIL GROUP:

-----------------------------------------------------------------------------

Rename the example application TIUHL7. This application will always be the receiving application for the TIU Generic HL7 Interface.

Change the status to ACTIVE.

The Facility Name must be entered for routing information used by the VistA Interface Engine (VIE) or by HealthConnect (HC). This field is optional if your site is not routing messages through a local VIE or to a regional HealthConnect(HC).

The HL7 Field Separator and HL7 Encoding Characters do not need to be changed. Please see the HL7 Site Manager & Developer Manual for more information.

Example Facility Name: 666~TESTLAB.FO-SLC.MED.VA.GOV~DNS

Repeat this step for the Sending Application; rename the TIUHL7 EX SENDING APP to the agreed upon name of the vendor server/application to receive messages from.

Example Sending Application: *HTAPPL*

This name was used for the Sending Application from the Home TeleHealth project.

## The Protocol File \#101

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entries in this file are used to define each transaction/message type. The two entries in this file included in the TIU\*1.0\*200 distribution to be edited are the Event and Subscriber protocols.

From the HL7 Main Menu Option, select the Interface Developer Options menu. To set up or edit HL7 Protocols, use the “Protocol Edit” option, on the Interface Developer Options menu:

Select Interface Developer Options Option: Protocol Edit

Select PROTOCOL NAME: TIUHL7 EXAMPLE MDM SUB

HL7 INTERFACE SETUP PAGE 1 OF 2

-----------------------------------------------------------------------------

NAME: TIUHL7 EXAMPLE MDM SUB

DESCRIPTION (wp): (empty)

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber

-----------------------------------------------------------------------------

The following naming convention is suggested for protocols for the TIUHL7 Interface:

\<RECEIVING APP\> \<SENDING APP\> \<MESSAGE TYPE\> \<PROTOCOL TYPE\>

Examples: TIUHL7 HTAPPL MDM SUBSCRIBER

TIUHL7 HTAPPL MDM EVENT

Example Protocol Name for Subscribers: *TIUHL7 HTAPPL MDM SUB*

This name was used for the subscribing protocol for messages from the Home TeleHealth project.

Tab down to the Type field and press \<Enter\> or \<Return\>. The option then presents a form to edit the fields specific to the Type of the selected protocol:

HL7 SUBSCRIBER PAGE 2 OF 2

TIUHL7 EXAMPLE MDM SUB

-----------------------------------------------------------------------------

RECEIVING APPLICATION: TIUHL7 EX RECEI

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: T02

SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YES

SECURITY REQUIRED?: NO

LOGICAL LINK: TIUHL7 EX

PROCESSING RTN: D PROCMSG^TIUHL7P1

ROUTING LOGIC:

-----------------------------------------------------------------------------

Enter TIUHL7 as the RECEIVING APPLICATION.

If your site is not using a VIE or HC to route HL7 messages, the Sending and Receiving Facilities Required fields may be set to NO.

Replace the LOGICAL LINK and enter the name of the *outgoing* logical link created earlier to send Application Acknowledgments to the sending application.

Save the changes and begin editing the TIUHL7 EXAMPLE MDM EVENT as follows:

Select PROTOCOL NAME: TIUHL7 EXAMPLE MDM EVENT

HL7 INTERFACE SETUP PAGE 1 OF 2

-----------------------------------------------------------------------------

NAME: TIUHL7 EXAMPLE MDM EVENT

DESCRIPTION (wp): (empty)

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver

-----------------------------------------------------------------------------

The following naming convention is suggested for protocols for the TIUHL7 Interface:

TIUHL7 \<sending app\> MDM \<type\>

Example Protocol Name for Subscribers: *TIUHL7 HTAPPL MDM EVENT*

This name was used for the event protocol for messages from the Home TeleHealth project.

Tab down to the Type field and press \<Enter\> or \<Return\>. The option then presents a form to edit the fields specific to the Type of the selected protocol:

HL7 EVENT DRIVER PAGE 2 OF 2

TIUHL7 EXAMPLE MDM EVENT

-----------------------------------------------------------------------------

SENDING APPLICATION: TIUHL7 EX SENDI

TRANSACTION MESSAGE TYPE: MDM EVENT TYPE: T02

MESSAGE STRUCTURE:

PROCESSING ID: VERSION ID: 2.4

ACCEPT ACK CODE: AL APPLICATION ACK TYPE: NE

RESPONSE PROCESSING RTN:

SUBSCRIBERS

TIUHL7 EXAMPLE MDM SUB

-----------------------------------------------------------------------------

Edit the Sending Application and enter the name of the Sending Application created earlier.

The SUBSCRIBERS should reflect the new name created earlier for the subscribing protocol.

# Vendor Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vendors have two responsibilities:

1.  Produce HL7 messages that are compatible with the Generic HL7 interface as described in this Handbook.
2.  Establish a viable LAN connection to the customer sites within the Veterans Health Administration through Enterprise HealthConnect(E-HC).

Vendors should work closely with IRM staff at the customer sites.

Some of the elements that are part of establishing a LAN connection are:

3.  You need the port number of the Regional HC (R-HC) for receiving messages.
4.  You need the HC ACK port number at the vendor site.
5.  You need the site e-mail address for HC errors.
6.  You need contact the VA OIT EHRM HSEP Implementation Team for further connectivity instructions and coordination (<span class="mark">REDACTED</span>)

# VistA Interface Engine and HealthConnect

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With both middleware products used by VA, VistA Interface Engine (VIE) and HealthConnect (HC), communication components work concurrently to model, automate, track, and optimize communication processes within and between data systems, providing a high emphasis on security and reliability. Both products also enable real-time, multi-directional communication among VistA applications, the Health Data Repository, Commercial-Off-The-Shelf (COTS) products, and other systems. In other words, each VIE and HC provide an integrated environment for managing the flow of critical information throughout the VHA's corporate business systems, as well as through external vendors and computer systems.

Currently all VIE interfaces are being migrated to HC. This Manual has been updated to specifically to reflect the migration of the ROES HL7 interfaces with VistA from VIE to HC. New TIU implementations are required to be configured with HealthConnect as messaging middleware.

Information on setup and operation of HC messaging middleware will be provided by the VA OIT EHRM HSEP Implementation Team that can be reached by email at <span class="mark">REDACTED</span>.

## Essentials 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is a requirement that for new implementations you use HealthConnect (HC) with the Generic HL7 Interface.

The following steps are important for the proper functioning of HC with the Generic HL7 Interface:

1.  Configure the vendor application with the local site HC port address (this is usually 8090).
2.  Identify a local site email address to receive HC error messages. You will need to request that the VA OIT EHRM HSEP Implementation Team configure this email address in the Regional HealthConnect (R-HC) instance.
3.  Provide information to the VA OIT EHRM HSEP Implementation Team to update the HC Enterprise Configuration matrix.
4.  Sending application name
5.  Receiving application name
6.  IP & Port where application acknowledgments are to be sent.
7.  Contact VA OIT EHRM HSEP Implementation Team for further instructions and Interface Control Documents.

# Database Repository

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing VistA database will be used to store TIU Documents File \#8925.

# System Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Creating a progress note from an HL7 message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No TIU document and/or PCE visit file entry will be created until generic HL7 verifies all required fields. The progress note will be created only if all the following conditions are met and verified.

## HL7 Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The fields needed to support the Generic HL7 Interface are given in terms of the edits performed on each field. Some fields are only conditionally required. You should read each edit carefully to fully understand what is required of each field.

> **NOTE:** If a piece of data is listed as required, document processing will not occur if that piece of data is missing from the HL7 message. This will not be annotated for each validation section unless otherwise noted.

If an error message is returned, it will contain a clear text reminder explaining the error. This can be viewed using the TIUHL7 Message Manager \[TIUHL7 MSG MGR\] which is exported in the TIU Maintenance Menu.

The following is an example of using the HL7 message Manager to check an error message:

1 TIU Parameters Menu ...

2 Document Definitions (Manager) ...

3 User Class Management ...

4 TIU Template Mgmt Functions ...

5 TIU Alert Tools

6 Active Title Cleanup Report

7 TIUHL7 Message Manager

Select TIU Maintenance Menu Option: 7 TIUHL7 Message Manager

Searching for messages.....

Refresh Message List

<u>TIUHL7 Message Manager Aug 04, 2006@15:47:19 Page: 1 of 1</u>

TIUHL7 Received Messages

Receiving Sending Message

<u>Message ID Date/Time Processed Application Application Status</u>

1 99953044 Jul 31, 2006@11:24:53 TIUHL7 HTAPPL Rejected

2 99953046 Jul 31, 2006@11:27:14 TIUHL7 HTAPPL Rejected

3 99953048 Jul 31, 2006@11:28:44 TIUHL7 HTAPPL Accepted

4 200T40029200608 Aug 02, 2006@11:35:11 TIUHL7 HTAPPL Accepted

5 200T40003200608 Aug 02, 2006@14:28:14 TIUHL7 HTAPPL Accepted

6 99953050 Aug 02, 2006@15:45:41 TIUHL7 HTAPPL Accepted

Enter ?? for more actions

View Message Delete Message(s)

Refresh Message List

Select Action: Quit// 2

<u>TIUHL7 Message Viewer Aug 04, 2006@15:47:22 Page: 1 of 1</u>

MSA^AR^99953046^TIUHL7^HTAPPL

ERR^PV1^44^^0000.00~Could not find a visit for Jul 31, 2006@16:21.

MSH^~\|\\^HTAPPL^00T5~VAWW.VITERION.CC.MED.VA.GOV~DNS^TIUHL7^689~ANONYMOUS.MED.V

A.GOV~DNS^20060731092708-0700^^MDM~T02~MDM_T02^99953046^T^2.4^^^AL^AL^USA

EVN^T02

PID^^^\~\~~USVHA~NI\|\~\~~USSSA~SS\|290\~\~~USVHA~PI\|\|^^TIUPATIENT~FIVE

PV1^^^GI WALK-IN^^^^^^^^^^^^NEW^^^^^^^^^^^^^^^^^^^^^^^^^20040626011903

TXA^^^TEXT^200607311621^^^^^33271~TIUPROVIDER~THREE\~\~\~\~~USVHA^~^^~USVHA^^^^PROGRE

SS NOTE^^^^^^\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~~

OBX^1^TX^SUBJECT~This is the subject ^^NEW TEST TODAY NEW Location NEW TEST

new REF date for GI WALK-IN .

Enter ?? for more actions

Delete Message Reprocess Message

Select Item(s): Quit//

The messages displayed by the Message Manager are from the XTEMP Global, which is set to delete messages after seven (7) days. In other words, VistA discards HL7 messages that are more than seven (7) days old.

### ### Unique Patient Identifier (one required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Locate the patient information in the HL7 message. Details of the patient information, such as the Social Security Number (SSN), or Integration Control Number (ICN), or Data File Number (DFN), will be found in the Patient Identification (PID) segment of the HL7 message. The unique patient information is required to enter any information into a patient’s Electronic Health Record.

This is a repeating field containing the Integration Control Number (ICN), Data File Number (DFN), or Social Security Number (SSN) along with the appropriate ASSIGNING AUTHORITY (USVHA or USSSA) and IDENTIFIER TYPE CODE (NI,PI,SS).

<span id="_Toc145664621" class="anchor"></span>Table 1: Patient Identifier

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 0%" />
<col style="width: 14%" />
<col style="width: 21%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>HL7 Segment</p></li>
</ul></th>
<th colspan="2"><ul>
<li><p>Identifier</p></li>
<li></li>
</ul></th>
<th><ul>
<li><p>Position</p></li>
</ul></th>
<th><ul>
<li><p>Assigning Authority</p></li>
<li></li>
</ul></th>
<th><ul>
<li><p>Identifier type code</p></li>
<li></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>PID</p></li>
</ul></td>
<td colspan="2"><ul>
<li><p>National ICN</p></li>
</ul></td>
<td><ul>
<li><p>3.5</p></li>
</ul></td>
<td><ul>
<li><p>USVHA</p></li>
</ul></td>
<td><ul>
<li><p>NI</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>PID</p></li>
</ul></td>
<td colspan="2"><ul>
<li><p>SSN</p></li>
</ul></td>
<td><ul>
<li><p>3.5</p></li>
</ul></td>
<td><ul>
<li><p>USSSA</p></li>
</ul></td>
<td><ul>
<li><p>SS</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>PID</p></li>
</ul></td>
<td colspan="2"><ul>
<li><p>VistA id</p></li>
<li><p>(DFN)</p></li>
</ul></td>
<td><ul>
<li><p>3.5</p></li>
</ul></td>
<td><ul>
<li><p>USVHA</p></li>
</ul></td>
<td><ul>
<li><p>PI</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>PID</p></li>
</ul></td>
<td><ul>
<li><p>Patient Identifier List</p></li>
</ul></td>
<td colspan="2"><ul>
<li><p>3.1</p></li>
</ul></td>
<td><ul>
<li><p>ICN</p></li>
</ul></td>
<td><ul>
<li><p>Use with patient name to identify unique patient in Patient File #2</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>PID</p></li>
</ul></td>
<td><ul>
<li><p>Patient Identifier List</p></li>
</ul></td>
<td colspan="2"><ul>
<li><p>3.1</p></li>
</ul></td>
<td><ul>
<li><p>SSN</p></li>
</ul></td>
<td><ul>
<li><p>Use with patient name to identify unique patient in Patient File #2</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>PID</p></li>
</ul></td>
<td><ul>
<li><p>Patient Identifier List</p></li>
</ul></td>
<td colspan="2"><ul>
<li><p>3.1</p></li>
</ul></td>
<td><ul>
<li><p>DFN (IEN) for Patient File #2</p></li>
</ul></td>
<td><ul>
<li><p>Use with patient name to identify unique patient in Patient File #2</p></li>
<li><p>Pointer to Patient File #2 will be stored in TIU Document File #8925, field .02 PATIENT</p></li>
</ul></td>
</tr>
</tbody>
</table>

#### TIUHL7 Validation:

The PATIENT IDENTIFIERS are used to perform a patient lookup in the VistA database. If only one numeric identifier is sent, the name comparison will occur between the LAST NAME and FIRST INITIAL.

If two or more numeric identifiers are sent, the name comparison will occur between the LAST NAME only. The name from the lookup is compared with the patient name from the HL7 message. Any discrepancy between the lookup name and the HL7 message name will stop document processing.

If multiple PATIENT IDENTIFIERS are sent, each patient lookup value of the DFN is compared against the other PATIENT IDENTIFIER lookup values of the DFN. Any discrepancy will stop document processing.

If multiple patients are returned using the DFN, ICN, or SSN, Date of Birth, the patient’s last and first name with the full Social Security Number will be required to select a unique patient.

<span id="_Toc145664622" class="anchor"></span>Table 2: Patient Identifier (continued)

| HL7 Segment | HL7 Field                                    | Position | Content     | Use/Comment                                                                      |
|-------------|----------------------------------------------|----------|-------------|----------------------------------------------------------------------------------|
| PID         | Patient Name – Family Name                   | 5.1.1    | Last name   | Use with patient SSN, ICN, or DFN to identify unique patient in Patient File \#2 |
| PID         | Patient Name – Given Name                    | 5.2      | First name  | Use with patient SSN, ICN, or DFN to identify unique patient in Patient File \#2 |
| PID         | Patient Name – Second And Further Given Name | 5.3      | Middle name | Use with patient SSN, ICN, or DFN to identify unique patient in Patient File \#2 |

Name fields from HL7 message are text fields and should be checked for escape sequences. COTS packages should replace all special characters used by HL7 with the appropriate escape sequences in text fields. See [Table 11](#Table_11), Information about Delimiters And Escape Sequences.

TIU may need to format name fields from the HL7 message into the VistA name format. TIU may need to combine the first letter of the last name with the last four characters of the SSN for a patient search. If the search returns multiple patients, full name and SSN should be compared to locate the unique patient. If a unique patient is located, HL7 message processing continues.

If no unique patient matches the information in the PID segment of the message, an application acknowledgement HL7 error message will be returned to the COTS package stating that the patient could not be located. No TIU document will be created. HL7 message processing will stop.

### Patient Visit (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Locate the patient visit in the HL7 message, if the patient Visit IEN is in the HL7 message, use it to locate the patient visit in VistA. If there is no IEN in the HL7 message, use the admission date and time in the message to locate the visit. If no patient visit is located, check the Document.

Availability Status field in the HL7 record to see if the document should be created. If it indicates that a TIU note should be created when an exact visit cannot be found. A patient historical visit will be created from the date and time in the message. HL7 message processing will continue.

If there is an error and a new visit cannot be created, an HL7 application acknowledgement error message returns to the COTS package, stating the visit could not be created. No TIU document will be created. HL7 message processing will stop.

If the document availability status field indicates that a TIU note should not be created when an exact visit cannot be located, an HL7 application acknowledgment error returns to the COTS package stating that an exact patient visit could not be located and no note is created, as indicated by the COTS package. HL7 message processing will stop.

<span id="_Toc145664623" class="anchor"></span>Table 3: Patient Visit

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>HL7 Segment</th>
<th>HL7 Field</th>
<th>Position</th>
<th>Content</th>
<th>Use/Comment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PV1</td>
<td>Visit Number</td>
<td>19.1</td>
<td>IEN for Visit File #9000010</td>
<td><p>If the COTS package has the visit IEN, it can be entered into this field to facilitate location of the appropriate visit.</p>
<p>Pointer to Visit File #9000010 will be stored in TIU Document File #8925, field .03 VISIT</p></td>
</tr>
<tr class="even">
<td>PV1</td>
<td>Admit Date/Time</td>
<td>44.1</td>
<td>Date of the admission or outpatient visit</td>
<td><p>Used to locate unique visit in Visit File #9000010</p>
<p>Or used to create unique visit in Visit File #900010</p>
<p>May be stored in TIU DOUCMENT File #8925, field .07 EPISODE BEGIN DATE/TIME</p></td>
</tr>
<tr class="odd">
<td>TXA</td>
<td>Document Availability Status</td>
<td>19</td>
<td></td>
<td><p>TIU will use this field to determine if the document should be stored if the visit cannot be found.</p>
<p>AV - keep document</p>
<p>If visit cannot be located, a new visit will be created as a historical visit using today's date (NOW). The document will be attached to this new visit.</p>
<p>CA or blank - delete document</p>
<p>If visit cannot be located, delete the document and pass back the appropriate error message.</p></td>
</tr>
</tbody>
</table>

#### ### Unique Document Note Title (required)

Locate the Unique Document Name, the title of the note, in the HL7 message. The TIU Note Title Name must match the exact name in the message. If there is no Note Title, return an HL7 application acknowledgement error message stating that the note title does not match an existing TIU note title. No TIU documents will be created. HL7 message processing will stop.

If a Note Title is found, HL7 message processing continues.

If the note title is under the Consults document class, but the HL7 message does not contain a Consult number, return an HL7 application acknowledgement error message stating that the consult number is missing. No TIU document will be created. HL7 message processing will stop.

If the note title is under the Surgical Reports document class, but the HL7 message does not contain a Surgery case number, the program attempts to access the case number by doing a lookup with the Admission Date/Time from the HL7 message. If it cannot find a Surgery case number, it will return an HL7 application acknowledgement error message stating that the surgery case number is missing. No TIU document will be created. HL7 message processing will stop.

If the note title is under the Discharge Summary document class, but the HL7 message does not contain a Admit Date/Time, return an HL7 application acknowledgement error message stating that the discharge date is missing. No TIU document will be created. HL7 message processing will stop.

<span id="_Toc145664624" class="anchor"></span>Table 4: Document Table

| HL7 Segment | HL7 Field                 | Position | Content            | Use/Comment                                                                                                                          |
|-------------|---------------------------|----------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| TXA     | Unique Document File Name | 16       | TIU document title | This field contains a unique document title which must exist in the TIU Document Definition File \#8925.1 at the receiving location. |

#### This patch is a required patch for the Home Telehealth/Vista Integration program. The titles listed below are the agreed upon titles by the Office of Care Coordination for the Home Telehealth program.

> **NOTE:** In order for the Home Telehealth interface to work, the titles must be an EXACT match.

#### Installing these titles during the HL7 patch installation is optional. If they were installed, any titles that already exist in 8925.1 as an EXACT match will simply be ignored and no changes will be made for that entry; only titles that do not yet exist will be added to 8925.1.  Therefore it is highly suggested that you review the list of titles and the document class that will be added to File 8925.1 with this patch prior to installation.  

The Home Telehealth titles are:

   File \# 8925.1  
   
   TIU DOCUMENT DEFINITION  
   -------------------------  
   Consult Titles:  
    CARE COORDINATION HOME TELEHEALTH SCREENING CONSULT  
   
   Document Class (Progress Notes):  
    CARE COORDINATION HOME TELEHEALTH NOTES  
   
   Progress Note Titles (CARE COORDINATION/HOME TELEHEALTH NOTES):  
    CARE COORDINATION HOME TELEHEALTH DISCHARGE NOTE  
    CARE COORDINATION HOME TELEHEALTH EDUCATION NOTE  
    CARE COORDINATION HOME TELEHEALTH EVALUATION NOTE  
    CARE COORDINATION HOME TELEHEALTH EVALUATION TREATMENT PLAN  
    CARE COORDINATION HOME TELEHEALTH SUBSEQUENT EVAL NOTE  
    CARE COORDINATION HOME TELEHEALTH SUMMARY OF EPISODE NOTE  
    CARE COORDINATION HOME TELEHEALTH TELEPHONE ENCOUNTER NOTE  
    CARE COORDINATION HOME TELEHEALTH VIDEO VISIT NOTE  
 

### ### Text (required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that the HL7 message contains document text. The text of the document is located in the OBX section of the HL7 message. If there is no text in the HL7 message, an application acknowledgement error message will be returned to the COTS package stating that there is no document text. No TIU document will be created. HL7 message processing will stop.

If there is text in the HL7 message, processing will continue.

There are several types of documents that can be uploaded in the HL7 message. Different types of documents have different types of required field:

Surgical Operative report documents require the unique Surgery Case Number. If no Case Number is provided and there is only one surgery case for the day, the document text will be added to an existing TIU Surgical Operative Report stub note for the surgery date if a note does not already exist with text. If a Surgery case number is provided with a date, the document will be created. If there is no Surgery Case Number and there is no date provided for the surgery, an error message will be returned to the COTS package. The surgery case number is located in the Unique Document Number element TXA 12 section of the HL7 message segment.

Discharge Summary documents require a particular admission date in order for a document to be created. If there is no match on the admission date, an application error message will be returned to the COTS package. This discharge date is located in the PV1 44 section of the HL7 message segment.

Consults require the unique ID number of the Consult. If the unique ID number is present, processing continues. If the unique ID number is blank or the ID provided cannot be found, no consult document is created and an application error message is returned. This document type is located in the TXA 12 section of the message segment.

<span id="_Toc145664625" class="anchor"></span>Table 5: Text

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th>HL7 Segment</th>
<th>HL7 Field</th>
<th>Position</th>
<th>Content</th>
<th>Use/Comment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OBX</td>
<td><p>Observation Value</p>
<p>(repeatable element, one for every line in the report)</p></td>
<td>5</td>
<td>Document text</td>
<td><p>Text of TIU document. Only one OBX segment will be included in the message.</p>
<p>This text will be stored in TIU Document File #8925, field 2 REPORT TEXT</p>
<p>The Observation Value element is repeatable and is used to transmit document text. Each Observation Value should contain a single line of the text document. Leading spaces should be included. Trailing spaces should be removed.</p>
<p>The sending package will substitute the appropriate escape sequences for every field separator and encoding character in this and any other text field in the message. The receiving package will change every escape sequence back to the appropriate special character.</p></td>
</tr>
</tbody>
</table>

### Document Author (required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the author of the document located in the TXA section of the HL7 message. Locate Author information in the New Person File \#200 using the Name and SSN located in the HL7 message. Current TIU rules will apply to the Author. Signed by author will use Current APIs.

The NAME is required and if missing will stop document processing. The ID NUMBER is optional but recommended. If the ID NUMBER is not included, an exact match lookup will be performed using the name from the HL7 message. If this lookup fails, document processing will stop.

If the ID NUMBER is included, it will be used to perform the lookup and retrieve the author/dictator name. If a name is found, it is validated against the name from the HL7 message. If this comparison fails, document processing will stop.

The document Originator is the author or dictator and is the expected signer. This project expects the expected signer or expected cosigner will be the only signers.

<span id="_Toc145664626" class="anchor"></span>Table 6: Document Author Table

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 23%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th>HL7 Segment</th>
<th>HL7 Field</th>
<th>Position</th>
<th>Content</th>
<th>Use/Comment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TXA</td>
<td>Originator Code/Name – ID</td>
<td>9.1</td>
<td><p>SSN or</p>
<p>IEN</p></td>
<td><p>Use with clinician name to identify unique clinician in New Person File #200</p>
<p>This is the author/dictator of the document in the TIU Document File #8925, field 1202 AUTHOR/DICTATOR</p></td>
</tr>
<tr class="even">
<td>TXA</td>
<td>Originator Code/Name – Family Name</td>
<td>9.2.1</td>
<td>Last name</td>
<td><p>Use with clinician SSN to identify unique clinician in NEW PERSON File #200</p>
<p>Pointer to this person will be stored in TIU Document File #8925, field 1204 EXPECTED SIGNER</p></td>
</tr>
<tr class="odd">
<td>TXA</td>
<td>Originator Code/Name – Given Name</td>
<td>9.3</td>
<td>First name</td>
<td>Use with clinician SSN to identify unique clinician in NEW PERSON File #200</td>
</tr>
<tr class="even">
<td>TXA</td>
<td>Originator Code/Name – Second And Further Given Name</td>
<td>9.4</td>
<td>Middle name</td>
<td>Use with clinician SSN to identify unique clinician in New Person File #200</td>
</tr>
<tr class="odd">
<td>TXA</td>
<td>Assigning authority/Namespace ID</td>
<td>9.9</td>
<td><p>USSSA or</p>
<p>USVHA</p></td>
<td><p>USSSA means 9.1 is an SSN</p>
<p>USVHA means 9.1 is an IEN</p></td>
</tr>
</tbody>
</table>

### Activity Date/Time (required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the activity date and time of the document, which is located in the TXA segment of the HL7 message. If there is no activity date and time in the HL7 message, an application acknowledgement error message will be returned to the COTS package stating that no activity date/time exists. No TIU document will be created. HL7 message processing will stop.

If the document activity date and time is not blank, HL7 processing will continue.

<span id="_Toc145664627" class="anchor"></span>Table 7: Origination Date/Time

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>HL7 Segment</th>
<th>HL7 Field</th>
<th>Position</th>
<th>Content</th>
<th>Use/Comment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TXA</td>
<td>Activity Date/Time</td>
<td>6.1</td>
<td><p>Reference date/time</p>
<p>Dictation date/time</p></td>
<td><p>Date/time the document was created</p>
<p>(dictated, recorded)</p>
<p>This date will be stored in</p>
<p>TIU Document File #8925, field 1301 REFERENCE DATE</p>
<p>and</p>
<p>TIU Document File #8925, field 1307 DICTATION DATE (if document was dictated)</p></td>
</tr>
</tbody>
</table>

### Create New TIU Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a TIU document note if all the following data elements are verified:

The patient is uniquely matched in VistA

The activity date/time is not blank

The HL7 message contains text

The author is a unique match in VistA and does not require a cosigner (TIU business rules)

The document note title is located in TIU and required fields for that document type are verified (the document type is in the HL7 message):

Progress note: title exists in the TIU PROGRESS NOTES document class

Consult document: title exists in the TIU CONSULTS document class, and unique document number (consult number) must exist in VistA; document will be linked to the consult;

Discharge summary document: title exists in the TIU DISCHARGE SUMMARY document class and admit date/time must be verified; document will reference the date of admission

Surgical Operative Report: title exists in the TIU SURGICAL REPORTS document class and unique document number (surgery case number) must exist in the Surgery package - if no case number, activity date must match the date of an existing surgery case; document text will be stored in existing TIU Surgery stub note.

> An application acknowledgement is returned if the note is created. If there is a problem creating the progress note an application error acknowledgement is returned that states that the note could not be created, no TIU document is created, and HL7 message processing stops.

### Expected Cosigner (conditionally required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the author requires an expected cosigner and one isn’t included in the HL7 message, document in not created and an error message is returned.

The NAME is required and if missing will stop document processing. The ID NUMBER is optional but recommended. If the ID NUMBER is not included, an exact match lookup will be performed using the name from the HL7 message. If this lookup fails, document processing will stop.

If the ID NUMBER is included, it will be used to perform the lookup and retrieve the expected cosigner name. If a name is found, it is validated against the name from the HL7 message. If this comparison fails, document processing will stop.

<span id="_Toc145664628" class="anchor"></span>Table 8: Expected Cosigner

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th>HL7 Segment</th>
<th>HL7 Field</th>
<th>Position</th>
<th>Content</th>
<th>Use/Comment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TXA</td>
<td><p>Assigned Document Authenticator</p>
<p>– ID</p></td>
<td>10.1</td>
<td>SSN</td>
<td><p>Use with clinician name to identify unique clinician in New Person File #200</p>
<p>Identifies expected cosigner for unsigned documents in the TIU Document File #8925, field 1208 EXPECTED COSIGNER.</p></td>
</tr>
<tr class="even">
<td>TXA</td>
<td><p>Assigned Document Authenticator</p>
<p>– Family Name</p></td>
<td>10.2.1</td>
<td>Last name</td>
<td><p>Use with clinician SSN to identify unique clinician in New Person File #200</p>
<p>Identifies expected cosigner for unsigned documents.</p></td>
</tr>
<tr class="odd">
<td>TXA</td>
<td>Assigned Document Authenticator – Given Name</td>
<td>10.3</td>
<td>First name</td>
<td><p>Use with clinician SSN to identify unique clinician in New Person File #200</p>
<p>Identifies expected cosigner for unsigned documents.</p></td>
</tr>
<tr class="even">
<td>TXA</td>
<td>Assigned Document Authenticator – Second And Further Given Name</td>
<td>10.4</td>
<td>Middle name</td>
<td><p>Use with clinician SSN to identify unique clinician in New Person File #200</p>
<p>Identifies expected cosigner for unsigned documents.</p></td>
</tr>
<tr class="odd">
<td>TXA</td>
<td>Identifier type code</td>
<td>10.13</td>
<td>COSIGNER</td>
<td>This code indicates that the person specified in this group of elements is the expected cosigner of this document</td>
</tr>
</tbody>
</table>

#### ### Entered By

Segment:TXAField:TRANSCRIPTIONIST CODE/NAMEExample: 666123456~TRANSCRIBER~ONE TIUHL7\~\~\~\~~USSSA

Required: No

TIU Field: 1302 ENTERED BY

Description: The name of the transcriptionist in HL7 format along with the appropriate ID NUMBER (SSN or IEN) and NAMESPACE ID (USSSA or USVHA).

#### TIUHL7 Validation:

The NAME is required and if missing will stop document processing. The ID NUMBER is optional but recommended. If the ID NUMBER is not included, an exact match lookup will be performed using the name from the HL7 message. If this lookup fails, document processing will stop.

If the ID NUMBER is included, it will be used to perform the lookup and retrieve the transcriptionist. If a name is found, it is validated against the name from the HL7 message. If this comparison fails, document processing will stop.

### ### Visit Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Segment: PV1

Field: VISIT NUMBER

Example: 144701

Required: No

TIU Field: .03 VISIT

Description: This is the IEN of the desired Visit from file \#9000010.

#### TIUHL7 Validation:

The identified patient is compared with the patient indicated from the Visit \# and any discrepancy will stop document processing.

If a Visit \# is not sent, the EPISODE BEGIN DATE/TIME will be used as a lookup value to find a Visit \#. If this lookup fails and DOCUMENT AVAILABILITY not sent as "AV", document processing will stop.

### Hospital Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Visits are required for all TIU documents.

Segment: PV1

Field: ASSIGNED PATIENT LOCATION

Segment: point of care

Example: EXAMPLE LOCATION

Required: Conditionally

TIU Field: Hospital Location

Description: Only the first component, point of care, is supported as the free text name of the HOSPITAL LOCATION (file \# 44). Do not add any component separators.

#### TIUHL7 Validation:

This VISIT validation supersedes all previous versions for all the associated fields: ADMIT DATE/TIME, ACTIVITY DATE/TIME, HOSPITAL LOCATION, VISIT \# & DOCUMENT AVAILABILITY.

#### For DISCHARGE SUMMARIES:

- must have a co-signer and TIUHL7 will also use to set ATTENDING PHYSICIAN
- \- If a VISIT \# is sent: Patient in HL7 message and VISIT must match
- If a VISIT \# is NOT sent:
  - ADMIT DATE/TIME is required for the admission lookup, otherwise message will be rejected.
  - Will use ADMIT DATE/TIME to find an admission. If multiple admissions for that day, HOSPITAL LOCATION will be used to find the most recent admission. If multiple matches for a given HOSPITAL LOCATION, lookup fails and message will be rejected.

For PROGRESS NOTES:

- For NEW VISIT (including new HISTORICAL):
  - VISIT \# must be sent as NEW
  - If DOCUMENT AVAILABILITY is AV, a new HISTORICAL visit will be created, otherwise a NEW VISIT will be created.
  - HOSPITAL LOCATION is required for new, NON-HISTORICAL visits (will reject). A HISTORICAL VISIT may be set as "NO LOCATION" if one is not sent.
  - The ADMIT DATE/TIME will be used as the visit date. If this date is NOT sent, it will use NOW.
  - If the HOSPITAL LOCATION is a ward location, the visit type will be "I" for inpatient. If the visit is a historical visit, the type will be "E" for event. All other visits will be "A" for ambulatory.

For non-historical visits, If the HOSPITAL LOCATION cannot be determined via lookup, message will be rejected.

For EXISTING VISIT:

- VISIT \# must be sent
- Patient in HL7 message and VISIT must match

To lookup EXISTING VISIT:- VISIT \# must NOT be sent or equal to null- VISIT lookup varies based up type of DATE used for lookups.

IF an ADMISSION is to be used, the ADMIT DATE/TIME MUST be sent. Using same matching logic from above, if an ADMISSION cannot be found, message will be rejected.

IF a CLINIC APPOINTMENT is to be used, the ADMIT DATE/TIME must NOT be sent and the ACTIVITY DATE/TIME will be used to find the clinic appointment. If an APPT cannot be found, the message will be rejected UNLESS DOCUMENT AVAILABILITY is set as AV, then a new historical visit using NOW will be used.

### Dictation Date/Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Segment: TXA

Field: TRANSCRIPTION DATE/TIME

Example: 200602281530 (Feb 28, 2006@3:30 pm)

Required: No

TIU Field: 1307 DICTATION DATE

Description: This is the date/time in HL7 format.

#### TIUHL7 Validation:

This value is used for the DICTATION DATE of the TIU document.

### Episode Begin Date/Time (conditionally required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Segment:PV1

Field: ADMIT DATE/TIME

Example: 200601311200 (Jan 1, 2006@12:00 pm)

Required: Conditionally Required\*TIU Field: 07 EPISODE BEGIN DATE/TIME

Description: This is the date/time in HL7 format.

#### TIUHL7 Validation:

Used if a VISIT \# is not included in the HL7 message to find a visit for the patient. If a visit cannot be found (none or multiple visits for the date), document processing will stop if DOCUMENT AVAILABILITY not sent as "AV".

This date is also used to find an OPERATION REPORT or PROCEDURE REPORT if the associated Surgical Case \# is not included in the HL7 message.

Required for DISCHARGE SUMMARY if VISIT \# not sent, otherwise optional.

### Reference Date/Time 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Segment: TXA

Field: ACTIVITY DATE/TIME

Example: 200603061400 (March 6, 2006@2:00 pm)

Required: Yes

TIU Field: 1301 REFERENCE DATE/TIME

Description: This is the date/time in HL7 format.

#### TIUHL7 Validation:

This is the date by which the document will be referenced and sorted. For Progress Notes & Discharge Summaries, this should be the date of the visit. For OPERATION REPORTS, this should be the date of the surgical case. Because this date is used in sorting, no validation is done by TIUHL7.

This date is used to determine the author's cosigner requirements.

### Surgical Case \# or Consult \# (conditionally required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Segment: TXA

Field: UNIQUE DOCUMENT NUMBER

Example: 2112

Required: Conditionally Required\*TIU Field: 1405 REQUESTING PACKAGE REFERENCE

Description: This is the surgical case \# or consult \#.

#### TIUHL7 Validation:

Based on the document title class, TIUHL7 will validate the value from the HL7 message as either a surgical case \# or consult request \#.

For both the consult and surgical case, TIUHL7 will validate the patient against the patient from the consult/surgical case. Any discrepancy will stop document processing.

Required for Consult titles; optional for SURGICAL REPORTS.

### Signature Status (required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check the signature status of the HL7 message. The HL7 element Document Completion Status should contain LA for Legally Authenticated if the document is supposed to be signed and the signature information is included in the HL7 message. The value of PA or blank indicates that the document is not signed. Processing of the HL7 message continues.

<span id="_Toc145664629" class="anchor"></span>  
Table 9: Signature Status

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 16%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>HL7 Segment</th>
<th>HL7 Field</th>
<th>Position</th>
<th>Content</th>
<th>Use/Comment</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TXA</td>
<td>Document Completion Status</td>
<td>17</td>
<td>LA, PA, or NULL</td>
<td><p>Determines whether the document is signed or not. PA/Pre-Authenticated: A completion status for documents indicating that the Document is complete, but has not been signed.</p>
<p>LA/Legally Authenticated: A completion status in which a document or entry has been signed manually or electronically in the COTS package by the individual who is legally responsible for that document or entry.</p></td>
</tr>
</tbody>
</table>

TIUHL7 follows regular TIU business rules when setting the document signature status.  The document signature status is determined by parameters assigned at the title level or inherited from the parent document class or class level.

Some TIU title parameters (Require Verification & Release) are only followed if the capture method is "upload", so all TIUHL7 titles will be set to "upload" upon document creation.

 TIU can apply signatures to uploaded documents if the document status is "unsigned" or "uncosigned".

 TIU cannot apply signatures to uploaded documents if the document requires verification ("unverified" status) and/or release ("unreleased" status).

 If the TIU HL7 message contains signature information and a document availability status is "AV" then the document will be created and TIU will attempt to electronically sign the document; if the signature fails, the document will be kept in an unsigned status.  After the signature(s) have been applied, the document with either be in an "uncosigned" or "completed" status.

 If the TIU HL7 message contains signature information and the document availability status is not "AV", the document will not be saved due to the failure to apply the electronic signature.

### Document Completion Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Segment: TXA

Field: DOCUMENT COMPLETION STATUS

Example: LA

Required: No

TIU Field: N/A

Description: This can be set to Legally Authenticated (LA) or blank.

#### TIUHL7 Validation:

During message processing, if this value is set to LA, at least one electronic signature must be applied to the document. If electronic signature fails and the availability is not set to AV, the document will be deleted.

### Document Availability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Segment: TXA

Field: DOCUMENT AVAILABILITY STATUS

Example: AV

Required: No

TIU Field: N/A

Description: This can be set to either AV or blank.

#### TIUHL7 Validation:

During message processing, this value is used to determine the status of a TIU document.

If a visit cannot be found or the DOCUMENT COMPLETION STATUS is sent as Legally Authenticated (LA) and the signature action fails, and this status is not set to available (AV), then the document will be deleted.

## Delimiter values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="Table_11" class="anchor"></span>Table 11: Information about Delimiters and Escape Sequences.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 14%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Delimiter</p></li>
</ul></th>
<th><ul>
<li><p>Suggested Value</p></li>
</ul></th>
<th><ul>
<li><p>Encoding Character Position</p></li>
</ul></th>
<th><ul>
<li><p>Escape Sequence</p></li>
</ul></th>
<th><ul>
<li><p>Usage</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Segment Terminator</p></li>
</ul></td>
<td><ul>
<li><p>&lt;cr&gt; (hex 0D)</p></li>
</ul></td>
<td><ul>
<li><p>-</p></li>
</ul></td>
<td><ul>
<li></li>
</ul></td>
<td><ul>
<li><p>Terminates a segment record. This value cannot be changed by implementers.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Field Separator</p></li>
</ul></td>
<td><ul>
<li><p>^</p></li>
</ul></td>
<td><ul>
<li><p>-</p></li>
</ul></td>
<td><ul>
<li><p>\F\</p></li>
</ul></td>
<td><ul>
<li><p>Separates two adjacent data fields within a segment. It also separates the segment ID from the first data field in each segment.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Component Separator</p></li>
</ul></td>
<td><ul>
<li><p>~</p></li>
</ul></td>
<td><ul>
<li><p>1</p></li>
</ul></td>
<td><ul>
<li><p>\S\</p></li>
</ul></td>
<td><ul>
<li><p>Separates adjacent components of data fields where allowed.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Subcomponent Separator</p></li>
</ul></td>
<td><ul>
<li><p>&amp;</p></li>
</ul></td>
<td><ul>
<li><p>4</p></li>
</ul></td>
<td><ul>
<li><p>\T\</p></li>
</ul></td>
<td><ul>
<li><p>Separates adjacent subcomponents of data fields where allowed. If there are no subcomponents, this character may be omitted.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Repetition Separator</p></li>
</ul></td>
<td><ul>
<li><p>|</p></li>
</ul></td>
<td><ul>
<li><p>2</p></li>
</ul></td>
<td><ul>
<li><p>\R\</p></li>
</ul></td>
<td><ul>
<li><p>Separates multiple occurrences of a field where allowed.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Escape Character</p></li>
</ul></td>
<td><ul>
<li><p>\</p></li>
</ul></td>
<td><ul>
<li><p>3</p></li>
</ul></td>
<td><ul>
<li><p>\E\</p></li>
</ul></td>
<td><ul>
<li><p>Escape character for use with any field represented by an ST, TX, or FT data type, or for use with the data (fourth) component of the ED data type. If no escape characters are used in a message, this character maybe omitted. However, it must be resent if subcomponents are used in the message.</p></li>
</ul></td>
</tr>
</tbody>
</table>

When a field of type TX, FT, or CF is being encoded, the escape character maybe used to signal certain special characteristics of portions of the text field. The escape character is whatever display ASCII character is specified in the \<escape character\> component of *MSH-2-encoding characters.* For purposes of this section, the character \\ will be used to represent the character so designated in a message. An *escape sequence* consists of the escape character followed by an escape code ID of one character, zero (0) or more data characters, and another occurrence of the escape character.

### Information about delimiters and handling of HL7 text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There may be special character embedded in text that also have meaning within HL7. The sending system will be responsible for changing every one of these special characters into the appropriate escape sequences before they place the text into the HL7 message.

For every field parsed from the HL7 message that is a data type TX (text) or ST (simple string), call a function that will replace all escape sequences with the corresponding field separator or encoding character.

For every text field placed into an HL7 message, call a function that will replace all field separator or encoding characters with the corresponding escape sequence.

Document text in OBX segmented field 5 is delimited by Field Separator “^”. The Observation Value will be repeated once for every line of the document.

For every name parsed from the HL7 message, call a function that will take the fields and format a VistA name.

For every name placed into an HL7 message, call a function that will take the VistA name and split it into HL7 format.

# # Vendor Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes the technical details behind TIUI/HL7 functionality that will allow computer-off-the-shelf (COTS) packages to upload documents into Text Integration Utility (TIU) using Health Level Seven (HL7) messaging. Each COTS package must have authorized access to the VA VistA system located behind a VA firewall at a VA data center that runs VistA TIU software. A critical function of the Home Telehealth systems will be their ability to communicate with existing Veteran Health Administration (VHA) computer systems, including VistA.

HL7 is the VA-adopted standard for the exchange of data that supports clinical patient care, and the management and delivery of healthcare services. HL7 accomplishes data exchange by defining the protocol for exchanging clinical data between healthcare information systems. As a standard, HL7 is widely accepted and used both nationally and internationally. Any vendors that wish to upload documents in HL7 format will be required to incorporate into their systems the ability to accept and send HL7 messages.

TIU is a software package written and maintained by VHA that allows users to create many different types of clinical documents and store them in a patient’s electronic record. Currently, clinical users can type document text directly into TIU. The TIU Upload utility also allows users to create documents outside of VistA and upload them into a TIU document using Kermit. The TIU Upload utility will not change and will still be available to users who need this functionality. Since the VistA systems have evolved and HL7 has become the adopted standard for transmission of health data, the VHA was in need of a new HL7 utility to upload documents into TIU.

This TIU/HL7 utility is designed to accommodate upload of *most* types of TIU documents. TIU Upload can still be used to upload text documents that cannot be handled TIU/HL7.

This document gives an overview of the functions that must be implemented using HL7 messaging. The rest of this document is divided into overview of the data flow, detailed overview of each function, and specifications and references. The section [Background of the VistA TIU Application](#background-of-the-vista-tiu-application) provides the setting for Text Integration Utilities. The [Generic HL7 Functions](#Functions) section provides information about each TIU document type that is supported by this software. Section [Required Fields](#required-fields) and the following sections contain the specifications for the HL7 data fields and the references that form the basis of this document.

Table 12 contains the acronyms and abbreviations used in this document.

<span id="_Ref95101041" class="anchor"></span>Table 12: Acronyms and Abbreviations

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>Acronym</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AAC</td>
<td>Austin Automation Center</td>
</tr>
<tr class="even">
<td>ADT</td>
<td>Admission, discharge and Transfer</td>
</tr>
<tr class="odd">
<td>ACK</td>
<td>Acknowledgement</td>
</tr>
<tr class="even">
<td>CCR&amp;A</td>
<td><p>Community Care Referrals and Authorizations (CCR&amp;A) application is</p>
<p>an enterprise-wide system used by Community Care (CC) staff to</p>
<p>automatically generate referrals and authorizations for all Veterans</p>
<p>receiving care in the community</p></td>
</tr>
<tr class="odd">
<td>CIO</td>
<td>Chief Information Officer</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td>Computerized Patient Records System</td>
</tr>
<tr class="odd">
<td>DDC</td>
<td>Denver Distribution Center</td>
</tr>
<tr class="even">
<td>DFN</td>
<td>Data File Number</td>
</tr>
<tr class="odd">
<td>ESM</td>
<td>Enterprise Systems Manager</td>
</tr>
<tr class="even">
<td>Hines</td>
<td>Hines Data Center</td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>Health Level 7 protocol</td>
</tr>
<tr class="even">
<td>HSRM</td>
<td>HealthShare Referral Management system</td>
</tr>
<tr class="odd">
<td>HT</td>
<td>Home Telehealth</td>
</tr>
<tr class="even">
<td>ICN</td>
<td>Integration Control Number</td>
</tr>
<tr class="odd">
<td>IE</td>
<td>Interface Engine</td>
</tr>
<tr class="even">
<td>IEN</td>
<td>Internal Entry Number</td>
</tr>
<tr class="odd">
<td>M&amp;IS</td>
<td>Messaging &amp; Interfaces Services</td>
</tr>
<tr class="even">
<td>MPI</td>
<td>Master Patient Index</td>
</tr>
<tr class="odd">
<td>OCC</td>
<td>Office of Care Coordination</td>
</tr>
<tr class="even">
<td>OI</td>
<td>Office of Information</td>
</tr>
<tr class="odd">
<td>PD</td>
<td>Patient Demographics</td>
</tr>
<tr class="even">
<td>RDV</td>
<td>Remote Data View</td>
</tr>
<tr class="odd">
<td>ROES</td>
<td>Remote Order/Entry System</td>
</tr>
<tr class="even">
<td>SSN</td>
<td>Social Security Number</td>
</tr>
<tr class="odd">
<td>TCP/IP</td>
<td>Transmission Control Protocol/Internet Protocol</td>
</tr>
<tr class="even">
<td>URL</td>
<td>Universal Record Location</td>
</tr>
<tr class="odd">
<td>VA</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>VACO</td>
<td>Veterans Affairs Central Office</td>
</tr>
<tr class="odd">
<td>VAMC</td>
<td>Department of Veterans Affairs Medical Center</td>
</tr>
<tr class="even">
<td>VIE</td>
<td>VistA Interface Engine</td>
</tr>
<tr class="odd">
<td>VISN</td>
<td>Veterans integrated service unit</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture</td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="even">
<td>WAN</td>
<td>Wide Area Network</td>
</tr>
</tbody>
</table>

## Background of the VistA TIU Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Test Integration Utilities (TIU) application was designed as a repository for a variety of text documents that belong in the patient record. The purpose of TIU) is to simplify the access and use of clinical documents for both clinical and administrative VAMC personnel, by standardizing the way clinical documents are managed. TIU includes a document hierarchy that is made up of Classes, Document Classes and Document titles. Titles a under a Document Class take on the characteristics of that document class and each document class has its own unique requirements

#### Progress Notes

VistA users create Progress Note titles in the TIU PROGRESS NOTES Class. When TIU creates a Progress Note document, TIU must associate this type of document to a visit. HL7 Progress Note messages should contain information to identify an existing visit in VistA. If visit information is missing from a Progress Note HL7 message or if TIU cannot find the visit, TIU will reject the HL7 message unless it contains information that instructs TIU to create a new patient historical visit with the activity date and time in the message.

#### Consult Notes

VistA users create Consult Note titles in the TIU CONSULTS Document Class. Consult notes must be linked to a Consult at the time they are created.

A VistA user creates a consult order. To resolve a consult, the VistA user selects a Consult Note title and selects an open consult from a list of patient. A signed consult note completes the consult, but a user can link any number of additional consult notes to a single consult. HL7 Consult Note messages must contain the DFN of an existing VistA Consult. If the consult information is not included in a Consult Note HL7 message, TIU will reject the HL7 message.

#### Surgery Reports

VistA users create Surgery Report titles in the TIU SURGICAL REPORTS Document Class. The Surgery package assigns a case number to each Surgery case. The Surgery package creates a “stub” surgery note at the time a VistA user completes a Surgery case in the Surgery package. The stub document is just a placeholder and does not contain text. Currently, the VistA user can manually enter text or TIU Upload can add the transcribed text to the stub note if it can locate the stub note using the surgery case number. HL7 Surgery Report messages should contain the surgery case number. If the surgery case number is missing, TIU will look for the Operation date in the element Activity Date/Time. If the Activity Date/Time can be located in the Surgery package and there is only one surgery for that date/time, TIU will add the text to an existing stub surgery note.

#### Discharge Summaries

VistA users create discharge summary Note titles in the TIU DISCHARGE SUMMARY Document Class. Discharge Summary notes must be linked to an admission.

TIU requires a particular admission in order to create a discharge summary document. HL7 discharge summary messages must include an admission date. If there is no match on the admission date, TIU will reject HL7 message.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The vendor has some relationship or contract with the VHA that gives them access to the VA WAN.
2.  The vendor has some information from the VA about a site: location,
3.  The vendor has some information from the VA about a patient: name, national identity (ICN), VistA identity (DFN), US identity (SSN), Date of Birth
4.  The vendor has some information about the author of the note: Name, VistA identity (DFN), US identity (SSN)
5.  The vendor has some information about other VA employees, like cosigner, attending physician: Name, VistA identity (DFN), US identity (SSN)
6.  The vendor knows the exact document title that will be created at each site
7.  The VA sites that receive the HL7 message will create not new document titles if the exact title does not already exist

Each COTS package that uses the TIUHL7 software has some patient data that the vendor and their VHA contact want to upload as document text into the VistA electronic patient record. This information could be:

- Transcription text for a report or a note
- Details of an order placed with a system outside of VistA
- Details of a completed assessment or care plan
- Incident report or periodic status

Each vendor, working with VHA staff, must answer the following questions:

- What information from the COTS package needs to uploaded into a TIU document
- What type of TIU document should be created?
  - Surgery report that will be text for an existing stub surgery note
  - Consult note that will be linked to an existing consult
  - Discharge summary that will be associated with an admission date
  - Progress note that will be associated with a visit date.
- What should be the format of the document text?
  - Simple text must be created, without formatting information
  - TIU will do no formatting, it will just store lines of text
- What type of TIU note should the HL7 message upload?
  - The HL7 message is required to contain some specific information for each TIU document type, but the HL7 message does not control the type of document that TIU will create; TIU controls the document type by following rules for the TIU document class that contains the document title
  - Progress note titles must be created in the TIU PROGRESS NOTES class
  - Discharge summary note titles must be created in the TIU discharge SUMMARY document class
  - Consult note titles must be created in the TIU CONSULTS document class
  - Surgery report titles must be created in the TIU SURGICAL REPORTS document class
  - The title must be included in the HL7 message and must be the exact spelling as the title stored in TIU at the site that receives the HL7 message
- Should the document be stored in TIU as a signed or unsigned document?
  - Signature information may be included in an HL7 message, but the COTS package should have a legal electronic signature on file before they create a signed document in TIU
  - TIU must be able to locate an electronic signature in VistA for any signer designated in the HL7 message TIU/HL7 software will respect existing TIU business rules as it evaluates each document and determines the correct status
  - The TIU/HL7 upload process can result in TIU documents with the following status codes: UNRELEASED, UNVERIFIED, UNSIGNED, UNCOSIGNED, COMPLETED
- What VistA location should receive the HL7 message?
  - The COTS package should have received information from a VistA location and should send documents to that location so they can be stored as part of the patient record

Once the vendor and the VHA staff agree on all of these points, each vendor must modify their software to create an MDM/T02 HL7 message and send it to TIU. The vendor software should contain the following functionality:

- Define a trigger, or multiple triggers, that will generate an MDM/T02 HL7 message
  - Trigger when a document has been completed – create unsigned document
  - Trigger when a document has been signed – create signed document
  - Trigger to create one HL7 message; could be used to retransmit message that failed, once the message has been corrected; could be used to upload individual documents created from information that existed prior to the installation of the TIU/HL7 software
  - Trigger to create a series of HL7 messages for completed or signed documents that have not been uploaded to VistA for a given date range; could be used to upload documents created from information that existed prior to the installation of the TIU/HL7 software
- Modify COTS software to create and send one MDM/T02 HL7 message for each document
  - Each trigger can generate one or many HL7 messages
  - Software may queue a number of individual HL7 messages to be sent at a later time when system performance should not be impacted
  - Each HL7 message should be complete and will be processed separately, as one HL7 message
  - COTS software should not create what is known as an HL7 “batch” with one header and multiple records – TIU will not be able to process the data.
  - Vendor software must be connected to the VA WAN
  - HL7 message can be sent via TCP/IP or HTTP protocol
- Modify COTS software to receive HL7 acknowledgement messages
  - Receive HL7 commit acknowledgement (ACK) message that indicates if the HL7 message was received by HC/VistA TIU
  - Receive an application ACK message if TIU document is successfully stored
  - Receive an application ACK reject message if TIU document is not successfully stored
- Vendor should have process for resolving errors
  - Receive an email from HC if the HL7 message could not be properly forwarded by the HC or if there is an error – must designate an email recipient
  - Errors will need to be resolved on the vendor side; there will be no error buffer on the TIU side where errors can be resolved, as is currently available with TIU Upload.
  - Record successful transmissions in the vendor software to prevent retransmission of the same document
  - Record transmission failures in the vendor software to trigger error resolution or document retransmission (automated or manual)
  - Review the HL7 application ACK reject message to determine if the problem is data related and correct the patient data
  - Review the HL7 application ACK reject message to determine if the problem is software related and correct the software
  - Provide reports of successful uploads, failed uploads, and uploads where no ACK was received.
  - Provide for retransmission of individual messages

TIU will not create any document and/or PCE visit file entry until it has verified all required fields. TIU will only create the document once if all the necessary fields are present and pass verification.

Once the data from the HL7 message is verified, TIU creates the document and assigns a status to the document. TIU will generate signature alerts for the appropriate individuals. The COTS package will send the document text in the OBX segment of an MDM/T02 HL7 message. Chapter 9 of the HL7 2.4 standards manual defines messages to support *Medical Records/Information Management (Document Management)*.

A network of Interface Engines (IE) will move all HL7 messages from the vendor software to the VistA TIU software. Each COTS package must have access to a local VA interface engine using TCP port 8090. The validation and testing document will include the IE domain name and port number that each vendor will use at the VA sites that receives the HL7 message.

## Generic HL7 Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Function section describes the different types of documents a COTS package can upload to the VistA patient record with an HL7 message. Vendors will send all documents using the MDM/T02 HL7 message type.

All messages require a basic set of information that identify the VistA facility, the patient, the author of the document and the document title. Sub heading 3.1 documents this basic information. Subsequent subheadings will refer back to the basics in section 3.1.

The MDM/T02 HL7 message can be sent to upload the following types of documents: progress note, consult note, discharge summary, addendum, or surgery report. Each document type is described under separate document sub headings.

Important! Please note: The choice of document type is *<u>not</u>* under the control of the HL7 message. The TIU software determines document type based on the location of the document title within the TIU document hierarchy:

- A progress note title must be stored in the TIU <u>PROGRESS NOTE</u> Class
- A consult note title must be stored in the TIU <u>CONSULTS</u> Document Class
- A discharge summary title must be stored in the TIU <u>discharge SUMMARY</u> Document Class
- A surgery report title must be stored in the TIU <u>SURGICAL REPORTS</u> Class

The HL7 message has a field for Document type, but this field is not supported because it will not override TIU business rules. To give an example, a single HL7 message could create two different document types.

#### Intent: Create a consult note that is linked to a particular consult 

The consult number is included in the HL7 message and the document title is located under the TIU CONSULTS Document Class; TIU will create a Consult Note.

#### Expected Result: Correct document type created.

A consult number is included in the HL7 message, but the document title is located under the TIU PROGRESS NOTES Document Class; TIU will ignore the consult number and create a Progress Note.

#### Unexpected Result: Incorrect document type created.

This document is not a replacement for the HL7 manuals. For more information about the MDM/T02 HL7 message, refer to Chapter 9 of the HL7 2.4 standard: *Medical Records/Information Management (Document Management)*. Information specific to this software HL7 requirements are documented under each document type below.

### TIU Document: Progress Note 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The vendor has patient information to upload to VistA and they and their VistA contact has decided that it should be stored as a TIU Progress Note. The vendor software formats the information into document text, builds an HL7 message that contains this text, and sends the HL7 message to VistA, where TIU stores the text in the patient record as a TIU Progress Note.

#### Description

The vendor creates an MDM/T02 HL7 message to upload a progress note. The message contains document text, information to identify a patient, the document author, the progress note title, and visit information if they want the progress note linked to an existing visit.

TIU will verify the content of the HL7 message and will not create the progress note until it has finished verifying all the required fields. If there are errors, TIU will send an HL7 Application Reject Acknowledgement message to the vendor software. The message will include text descriptions of all the errors found during data verification. If there are no errors, TIU will store the text in a progress note.

#### Responsibilities

Responsibilities are the required actions necessary for the completion of the function; the following paragraphs list the responsibilities.

#### Vendor Responsibilities

In support of the process of creating a progress note, vendor is responsible for:

- Establishing a relationship with one or more VHA sites so the vendor has access to the VHA WAN and an interface engine server located at a VA site
- Receiving information from the VHA site that will:
  - Uniquely identify a patient
  - Uniquely identify the VistA location that will receive and store the progress note
  - Uniquely identify the VistA user who is the author (signer) of the document.
  - Uniquely identify the progress note title at the receiving VA site into which the document text will be stored
  - Uniquely identify the VistA visit that will be linked to the progress note at the time the document is created:
  - Visit IEN
  - Admission date/time
  - Authorizing TIU to create a new visit or reject the HL7 message if an existing visit cannot be located.
- Working with their VHA contacts to determine the acceptable layout for the document text and the exact TIU progress note title.
- Creating a trigger in the vendor software that will generate an MDM/T02 HL7 message that contains text of the progress note that has been formatted from data stored in the vendor system.
- Sending the MDM/T02 HL7 message to the Interface Engine.
- Receiving HL7 commit acknowledgement message from the Interface Engine indicating that message was received.
- Checking whether the TIU document was successfully created.
  - Recording that TIU successfully created a progress note.
  - Receiving HL7 Application Accept Acknowledgement message indicating that TIU successfully created the progress note.
  - Recording successful document transmission in vendor software so there is a record that the data was successfully uploaded, if appropriate.
  - Recording that TIU rejected the HL7 message and did not create a progress note:
  - Receiving HL7 Application Reject Acknowledgement message indicating that TIU rejected the HL7 message and did not create the progress note
  - Recording that the HL7 message failed in vendor software so there is a record that the data has not been uploaded and store the error message so it can be reviewed
  - Alerting appropriate people of failed document upload.
  - Triggering another MDM/T02 message once the problems have been corrected (may require software change or update of vendor software with VistA information).
  - Recording that no HL7 Application Acknowledgement was received.
  - Recording that an application or commit acknowledgement for the HL7 message was received.
  - Determining what happened if the vendor software does not receive a commit or application acknowledgement.
  - Triggering another MDM/T02 message to be sent once the problems have been corrected (may require vendor software change or update of vendor software with VistA information).
- Providing a way to retransmit the MDM/T02 message.
  - When a message did not upload successfully.
  - When they want to upload data that existed in the vendor system prior to the availability of this TIU HL7 upload software.

#### Interface Engine Responsibilities

The Interface Engine is responsible for:

- Storing vendor information in a table so it will know that it should receive and accept HL7 messages from the vendor software.
- Receiving the HL7 message from the COTS software package.
- Routing the HL7 message from the vendor software to the appropriate facility via the Interface Engine.
- Routing HL7 commit and application Acknowledgement messages to the vendor server
- Sending an email to a designated address when an error occurs

#### #### VistA Responsibilities

TIU is responsible for:

- Receiving and parsing data from the HL7 message
- Locating a unique patient using identifiers SSN, ICN, DFN, name, Date of Birth
- Locating a unique patient visit using visit IEN or admission date/time; or creates a patient historical visit from the date and time in the message, if the message indicates that a TIU note should be created when an exact visit cannot be found
- Locating the document title in TIU
- Verifying that document text was included in the HL7 message
- Locating the author and cosigner using identifiers SSN, name
- Locating an existing visit in VistA that will be associated with the progress note
- Creating a new visit if instructed to do so in the HL7 message

A progress note must be associated with a visit date. If TIU cannot find a visit date that matches the HL7 message data, the HL7 message can instruct TIU to create a new visit and then create the progress note, or to reject the HL7 message and not create a progress note. TIU will take the following steps in its attempt to find a visit to associate with a progress note document. TIU will:

- Look for the visit IEN and uses it to locate an existing visit
- Look for the admission date and time and uses it to locate an existing visit or
- If neither visit IEN or admission date match a visit at the receiving site, TIU will examine the document availability status in the HL7 record
  - AV – Available indicates that the progress note should be created if an existing visit cannot be found; TIU creates a new patient historical visit from the date and time of the message, then creates the progress note
  - CA – Cancel indicates that the progress note should *not be created* if an existing visit cannot be found; TIU does not create a progress note, TIU rejects the HL7 message and returns an Application Acknowledgment reject HL7 message.

If verification proves that it has everything it needs to create a progress note, TIU will create a new progress note and link it to a visit. If verification proves that there is an error, TIU will create an Application Acknowledgement reject HL7 message with an error code and error text that explains all of the fields that failed verification and TIU will not create a progress note document.

If the Progress Note HL7 message contains signature data, TIU will create a signed progress note with a status of “completed”. Otherwise TIU saves the note with a status according to regular TIU business rules. If the document text was transcribed, the status could be set to “unverified”. If the status is “unsigned”, TIU will send an alert to the author (signer) to let them know there is a note to be signed. TIU will send an HL7 Application Accept Acknowledgement message to the vendor software, along with the DFN of the new progress note.

A positive acknowledgement indicates that TIU successfully created the progress note. A reject acknowledgment indicates that TIU did not create the progress note. Reject acknowledgements contain information that indicate why the HL7 message was rejected

#### User Responsibilities

A user is someone who has contact with the vendor, and the vendor software, and has some responsibility for the progress note document. More than one user could handle these responsibilities. A user with VistA access is responsible for:

- Ensuring that the exact document title included in the HL7 message exists in TIU and has been created in the TIU Progress Notes document class
- Verifying the progress note document if it is created with status “unverified”
- Signing the progress note document if it is created with status “unsigned”
- Cosigning the progress note document if it is created with status “uncosigned”
- Reviewing the signed document is in VistA if they were the person who signed the document in the vendor software

#### Required Fields

The MDM/T02 HL7 message for progress notes requires the following fundamental data items:

- Vendor identification
- Patient record VistA facility id
- Patient record VistA facility number
- Patient Name
- Patient identifier (at least one)
  - Patient ICN
  - Patient SSN
  - Patient Date of Birth
  - Patient record number (DFN) created by the VistA facility
- Document title from VistA facility that is from the TIU PROGRESS NOTES document class (title in HL7 message must exactly match title in TIU)
- Author (expected signer) name and ID as identified in VistA
- Document text

In addition to the fields that are required in all MDM/T02 HL7 messages, a Progress note requires visit information.

<span id="_Ref96837714" class="anchor"></span>Table 13: Data Validation Rules

| Data                                                    |       |                                                                                            |
|---------------------------------------------------------|-------|--------------------------------------------------------------------------------------------|
| Home Telehealth vendor server identification            | All   | Placed in MSH and OBX segments to identify the vendor server and vendor server application |
| Patient ICN                                             | Alert | National index for the patient (unique identity within the VA)                             |
| Patient Name                                            | Alert | Legal name of the patient                                                                  |
| Patient SSN                                             | Alert | US index for the patient (unique identity within the US)                                   |
| Patient’s record number in sign up VistA facility (DFN) | Alert | VistA facility index for the patient (unique identity within VistA facility)               |
| Name of document author                                 | All   | Person who will be expected to sign the TIU document in VistA                              |
| Visit IEN                                               |       | VistA facility index for a patient visit (unique identity within the VistA facility)       |

#### #### Data Nomenclature

The VistA facility id and VistA facility number are obtained from the Institution File. Patient data comes from VistA Patient File \#2. Information about the author, cosigner, attending physician comes from VistA New Person File \#200.

The institution file definition and extract can be found on the section labeled *Facility address file* on the web page [<u>http://vaww.va.gov/techsvc/projects/VICReplacement_docs.html</u>](http://vaww.va.gov/techsvc/projects/VICReplacement_docs.html). A recent extract from the address file can be directly retrieved from URL <http://vaww.va.gov/techsvc/projects/VIC/FacilityAddresses_Vendor.txt>.

#### Message Content

The HL7 message content is defined in the HL7 2.4 standard chapter 9 (*Medical Records/Information Management (Document Management*).

#### Message Format 

The message type for the progress note message is MDM~T02. The Medical Document Management (MDM) Message is documented in Chapter 9 of the HL7 2.4 standard. The HL7 event code is T02, which identifies the message as carrying an “original document and content”. The MDM/T02 HL7 message has six data segments that contain the following information:

- Message identification (MSH)
- Document available event (EVN)
- Patient identification (PID)
- Patient visit information (PV1)
- Document notification (TXA)
- Observation/result data (OBX)

### TIU Document: Consult 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The vendor has patient information to upload to VistA and they and their VistA contact has decided that it should be stored as a TIU Consult Note. The vendor software formats the information into document text, builds an HL7 message that contains this text, and sends the HL7 message to VistA, where TIU stores the text in the patient record as a TIU Consult Note.

#### Description

The vendor creates an MDM/T02 HL7 message to upload a consult note. The message contains document text, information to identify a patient, the document author, the consult note title, and the ID number of the consult. Consults are created as orders for some type of service. Consult notes are created under the CONSULTS document class in TIU and are linked to consults so the consult and the note text can be viewed from the Consults Tab in CPRS GUI. A signed consult note completes the consult. Multiple signed consult notes can be created and linked to a single consult.

TIU will verify the content of the HL7 message and will not create the consult note until it has finished verifying all the required fields. If there are errors, TIU will send an HL7 Application Reject Acknowledgement message to the vendor software. The message will include text descriptions of all the errors found during data verification. If there are no errors, TIU will store the text in a progress note.

#### Responsibilities

Responsibilities are the required actions necessary for the completion of the function; the following paragraphs list the responsibilities.

#### Vendor Responsibilities

In support of the process of creating a progress note, vendor is responsible for:

- Establishing a relationship with one or more VHA sites so the vendor has access to the VHA WAN and an interface engine server located at a VA site
- Receiving information from the VHA site that will
  - Uniquely identify a patient
  - Uniquely identify the VistA location that will receive and store the progress note
  - Uniquely identify the VistA user who is the author (signer) of the document.
  - Uniquely identify the progress note title at the receiving VA site into which the document text will be stored
  - Uniquely identify the VistA Consult IEN that will be linked to the consult note at the time the document is created:
- Working with their VHA contacts to determine the acceptable layout for the document text and the exact TIU consult note title.
- Creating a trigger in the vendor software that will generate an MDM/T02 HL7 message that contains text of the consult note that has been formatted from data stored in the vendor system
- Sending the MDM/T02 HL7 message to the Interface Engine
- Receiving HL7 commit acknowledgement message from the Interface Engine indicating that message was received
- Checking whether the TIU document was successfully created
  - Recording that TIU successfully created a consult note
  - Receiving HL7 Application Accept Acknowledgement message indicating that TIU successfully created the consult note
  - Recording successful document transmission in vendor software so there is a record that the data was successfully uploaded, if appropriate
  - Recording that TIU rejected the HL7 message and did not create a consult note
  - Receiving HL7 Application Reject Acknowledgement message indicating that TIU rejected the HL7 message and did not create the consult note
  - Recording that the HL7 message failed in vendor software so there is a record that the data has not been uploaded and store the error message so it can be reviewed
  - Alerting appropriate people of failed document upload
  - Triggering another MDM/T02 message once the problems have been corrected (may require software change or update of vendor software with VistA information)
- Recording that no HL7 Application Acknowledgement was received
  - Recording that an application or commit acknowledgement for the HL7 message was received
  - Determining what happened if the vendor software does not receive a commit or application acknowledgement
  - Triggering another MDM/T02 message to be sent once the problems have been corrected (may require vendor software change or update of vendor software with VistA information)
- Providing a way to retransmit the MDM/T02 message
  - When a message did not upload successfully
  - When they want to upload data that existed in the vendor system prior to the availability of this TIU HL7 upload software

#### Interface Engine Responsibilities

The Interface Engine is responsible for:

- Storing vendor information in a table so it will know that it should receive and accept HL7 messages from the vendor software
- Receiving the HL7 message from the COTS software package
- Routing the HL7 message from the vendor software to the appropriate facility Interface Engine via
- Routing HL7 commit and application Acknowledgement messages to the vendor server
- Sending an email to a designated address when an error occurs

#### #### VistA Responsibilities

TIU is responsible for:

- Receiving and parsing data from the HL7 message
- Locating a unique patient using identifiers SSN, ICN, DFN, name, and Date of Birth
- Locating a unique patient visit using visit IEN or admission date/time; or creates a patient historical visit from the date and time in the message, if the message indicates that a TIU note should be created when an exact visit cannot be found
- Locating the document title in TIU
- Verifying that document text was included in the HL7 message
- Locating the author and cosigner using identifiers SSN, name
- Locating an existing consult in VistA that will be linked to the consult note

A consult note must be linked to an existing consult. If TIU cannot find a consult that matches the HL7 message consult number, TIU will reject the HL7 message and not create a consult note.

> **NOTE:** The HL7 message does not determine the type of TIU document. A VistA user must create the consult note title in the TIU CONSULTS document class in order for it to be a consult note. If the HL7 message contains a consult number and the document title exists in the TIU PROGRESS NOTES document class instead of the TIU CONSULTS document class, TIU will create a progress note instead of a consult note and the document will not be linked to a consult.

If verification proves that it has everything it needs to create a progress note, TIU will create a new consult note and link it to a visit. If verification proves that there is an error, TIU will create an Application Acknowledgement reject HL7 message with an error code and error text that explains all of the fields that failed verification and TIU will not create a consult note document.

If the consult note HL7 message contains signature data, TIU will create a signed consult note with a status of “completed.” Otherwise, TIU saves the note with a status according to regular TIU business rules. If the document text was transcribed, the status could be set to “unverified.” If the status is “unsigned,” TIU will send an alert to the author (signer) to let them know there is a note to be signed. TIU will send an HL7 Application Accept Acknowledgement message to the vendor software, along with the DFN of the new consult note.

A positive acknowledgement indicates that TIU successfully created the consult note. A reject acknowledgment indicates that TIU did not create the consult note. Reject acknowledgements contain information that indicate why the HL7 message was rejected

#### User Responsibilities

A user is someone who has contact with the vendor, and the vendor software, and has some responsibility for the progress note document. More than one user could handle these responsibilities. A user with VistA access is responsible for:

- Ensuring that the exact document title included in the HL7 message exists in TIU and has been created in the TIU Consults document class
- Verifying the consult note document if it is created with status “unverified”
- Signing the consult note document if it is created with status “unsigned”
- Cosigning the consult note document if it is created with status “uncosigned”
- Reviewing the signed document is in VistA if they were the person who signed the document in the vendor software

#### Required Fields

The MDM/T02 HL7 message for consult notes requires the following fundamental data items:

- Vendor identification
- Patient record VistA facility id
- Patient record VistA facility number
- Patient Name
- Patient identifier (at least one)
  - Patient ICN
  - Patient SSN
  - Patient record number (DFN) created by the VistA facility
  - Patient Date of Birth
- Document title from VistA facility that is from the TIU CONSULTS document class (title in HL7 message must exactly match title in TIU)
- Author (expected signer) name and ID as identified in VistA
- Document text

In addition to the fields that are required in all MDM/T02 HL7 messages, a Progress note requires visit information.

- 

<span id="_Toc111258285" class="anchor"></span>Table 14: Data Validation Rules

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 7%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>Home Telehealth vendor server identification</th>
<th>All</th>
<th>Placed in MSH and OBX segments to identify the vendor server and vendor server application</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patient ICN</td>
<td>Alert</td>
<td>National index for the patient (unique identity within the VA)</td>
</tr>
<tr class="even">
<td>Patient Name</td>
<td>Alert</td>
<td>Legal name of the patient</td>
</tr>
<tr class="odd">
<td>Patient SSN</td>
<td>Alert</td>
<td>US index for the patient (unique identity within the US)</td>
</tr>
<tr class="even">
<td>Patient Date of Birth</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Patient’s record number in sign up VistA facility (DFN)</td>
<td>Alert</td>
<td>VistA facility index for the patient (unique identity within VistA facility)</td>
</tr>
<tr class="even">
<td>Name of document author</td>
<td>All</td>
<td>Person who will be expected to sign the TIU document in VistA</td>
</tr>
<tr class="odd">
<td>Consult IEN</td>
<td></td>
<td><p>VistA facility index for a consult</p>
<p>(unique identity within the VistA facility)</p></td>
</tr>
</tbody>
</table>

#### Data Nomenclature

The VistA facility id and VistA facility number are obtained from the Institution File. Patient data comes from VistA Patient File \#2. Information about the author, cosigner, attending physician comes from VistA New Person File \#200.

The institution file definition and extract can be found on the section labeled *Facility address file* on the web page [<u>http://vaww.va.gov/techsvc/projects/VICReplacement_docs.html</u>](http://vaww.va.gov/techsvc/projects/VICReplacement_docs.html). A recent extract from the address file can be directly retrieved from URL <http://vaww.va.gov/techsvc/projects/VIC/FacilityAddresses_Vendor.txt>.

#### Message Content

The HL7 message content is defined in the HL7 2.4 standard chapter 9 (*Medical Records/Information Management (Document Management*).

#### Message Format 

The message type for the progress note message is MDM~T02. The Medical Document Management (MDM) Message is documented in Chapter 9 of the HL7 2.4 standard. The HL7 event code is T02, which identifies the message as carrying an “original document and content”. The MDM/T02 HL7 message has six data segments that contain the following information:

- Message identification (MSH)
- Document available event (EVN)
- Patient identification (PID)
- Patient visit information (PV1)
- Document notification (TXA)
- Observation/result data (OBX)

#### Example

MSH^~\|\\^Home Telehealth 2004^\<facility number\>~XYZ Corp server.MED.VA.gov~DNS ^VistA^\<VA facility dns\>^^20040621104503‑0500^^MDM~T02^500167399^T^2.4^^^AL^AL^US

PID^^^1234567890V23456\~\~~USVHA&&0363~NI\|123456789\~\~~USSSA~SS~VA FACILITY NAME&500&L\|1234567890V23456\~\~~USVHA&&0363~NI~VA FACILITY NAME&500&L^^Patient~Veterans~Administration\~\~\~~L

PV1^^^^^123456789\~\~~USVHA\~~VA facility&facility number&L\~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^200411010622200000‑0400^200411280622200000‑0400^^^^^^^^

TXA^^CN^TEXT^^32885~Doctor~Fine\~\~\~\~\~~USVHA~L\~\~~NI~facility&facility number&L^200411280622200000‑0400^200411280622200000‑0400^^^32885~Doctor~Fine\~\~\~\~\~~USVHA~L\~\~~NI~facility&facility number&L^^^123456789\~\~~USVHA\~~VA facility&facility number&L\~~^^^Care Coordination/Home Telehealth Summary of Episode^PA^U^AV^A

OBX^1^TX^^^Patient, Veterans Aloysius has been supported by the Home Telehealth Program.\|The following information was submitted by the veteran through their Home Telehealth system.\|‑ 28 sessions with the Congestive Heart Failure DIALOG \| ‑28 sessions with the Chronic Pain DIALOG\| ‑ 28 BLOOD GLUCOSE observations \| ‑ 28 BLOOD PRESSURE observations \|‑ 28 PAIN observations \| ‑ 28 PULSE observations \| - 28 PULSE OXIMETRY observations \| - 28 TEMPERATURE observations \| - 28 WEIGHT observations 

<span id="_Ref96945291" class="anchor"></span>Figure 11: 28-Day Consult Note Data

MSH^~\|\\^Home Telehealth 2004^\<facility number\>~XYZ Corp server.MED.VA.gov~DNS ^VistA^\<VistA Facility dns\>^^20040621104503‑0500^^ORU~R01^500167499^T^2.4^^^AL^AL^US

PID^^^1234567890V23456\~\~~USVHA&&0363~NI\|123456789\~\~~USSSA~SS~VA FACILITY NAME&500&L\|1234567890V23456\~\~~USVHA&&0363~NI~VA FACILITY NAME&500&L^^Patient~Veterans~Administration\~\~\~~L

PV1^^^^^123456789\~\~~USVHA\~~VA facility&facility number&L\~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^200412140622200000‑0400^200412140622200000‑0400^^^^^^^^

TXA^^PR^AP^200412141154‑0500^32885~Doctor~Fine\~\~\~\~\~~USVHA~L\~\~~NI~facility&facility number&L^200412140622200000‑0400^200412140622200000‑0400^^^32885~Doctor~Fine\~\~\~\~\~~USVHA~L\~\~~NI~facility&facility number&L^^^123456789\~\~~USVHA\~~VA facility&facility number&L\~~^^^Care Coordination/Home Telehealth Summary of Episode^PA^U^AV^A

OBX^^ST^2~Pulse~99VA120.51^^50^beats/min^^^^^F^^^^^^Device Entered^XYZ Corp~123B~1.2

<span id="_Ref96945298" class="anchor"></span>Figure 12: “Out-of-bounds” Progress Note Data (Pulse)

#### Acknowledge Message Content

The message content is given in the *VA Home Telehealth HL-7 Message formats* document. The VistA system generates an acknowledgment message when it has processed the progress note message.

#### Message Format

The acknowledge function uses the General Acknowledgment (ACK) Message as documented in chapter 2 of the HL7 standard. The Home Telehealth Vendor Server will mandate an acceptance of the progress note itself (an application acknowledgement).

#### Example

The following three examples are of a message acceptance, a request acceptance (application acknowledge) and a request refusal (application negative acknowledgement). The example is from the *Home Telehealth Profile*. The fields of interest are in *italics*, bold and red.

MSH^~\|\\^VistA^\<VistA Facility dns\>^Home Telehealth 2004^\<facility number\>~XYZ Corp server.MED.VA.gov~DNS ^20040621104503‑0500^^ACK^600167123^T^2.4^^^ER^ER^USA

MSA^CA^500167399^^^^

<span id="_Toc111256958" class="anchor"></span>Figure 13: Progress Note Message Acceptance (Message Acknowledge)

MSH^~\|\\^VistA^\<VistA Facility dns\>^Home Telehealth 2004^\<facility number\>~XYZ Corp server.MED.VA.gov~DNS ^20040621104503‑0500^^ACK^600167123^T^2.4^^^ER^ER^USA

MSA^AA^500167399^^^^

<span id="_Toc111256959" class="anchor"></span>Figure 14: Progress Note Acceptance (Application Acknowledge)

MSH^~\|\\^VistA^\<VistA Facility dns\>^Home Telehealth 2004^\<facility number\>~XYZ Corp server.MED.VA.gov~DNS ^20040621104503‑0500^^ACK^600167123^T^2.4^^^ER^ER^USA

MSA^AR^500167399^^^^100~Missing ICN~HL70357

ERR^PID^3^0^100~Missing ICN~HL70357

<span id="_Toc111256960" class="anchor"></span>Figure 15: Progress Note Refusal (Application Acknowledge)

### TIU Document: Discharge Summary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The vendor has patient information to upload to VistA and they and their VistA contact have decided that it should be stored as a TIU discharge summary. The vendor software formats the information into document text, builds an HL7 message that contains this text, and sends the HL7 message to VistA, where TIU stores the text in the patient record as a TIU discharge summary.

#### Description

The vendor creates an MDM/T02 HL7 message to upload a discharge summary. The message contains document text, information to identify a patient, the document author, the discharge summary title, and the VistA admission date that they want associated with this discharge summary.

TIU will verify the content of the HL7 message and will not create the discharge summary until it has finished verifying all the required fields. If there are errors, TIU will send an HL7 Application Reject Acknowledgement message to the vendor software. The message will include text descriptions of all the errors found during data verification. If there are no errors, TIU will store the text in a discharge summary.

#### Responsibilities

Responsibilities are the required actions necessary for the completion of the function; the following paragraphs list the responsibilities.

#### Vendor Responsibilities

In support of the process of creating a discharge summary, vendor is responsible for:

- Establishing a relationship with one or more VHA sites so the vendor has access to the VHA WAN and an interface engine server located at a VA site
- Receiving information from the VHA site that will:
  - Uniquely identify a patient
  - Uniquely identify the VistA location that will receive and store the discharge summary
  - Uniquely identify the VistA user who is the author (signer) of the document.
  - Uniquely identify the discharge summary title at the receiving VA site into which the document text will be stored
  - Uniquely identify the VistA inpatient admission date/time that will be associated with the discharge summary.
- Working with their VHA contact(s) to determine the acceptable layout for the document text and the exact TIU discharge summary title.
- Creating a trigger in the vendor software that will generate an MDM/T02 HL7 message that contains text of the discharge summary
- Sending the MDM/T02 HL7 message to the Interface Engine
- Receiving HL7 commit acknowledgement message from the Interface Engine indicating that message was received
- Checking whether the TIU document was successfully created
  - Recording that TIU successfully created a discharge summary
  - Receiving HL7 Application Accept Acknowledgement message indicating that TIU successfully created the discharge summary
  - Recording successful document transmission in vendor software so there is a record that the data was successfully uploaded, if appropriate
  - Recording that TIU rejected the HL7 message and did not create a discharge summary
  - Receiving HL7 Application Reject Acknowledgement message indicating that TIU rejected the HL7 message and did not create the discharge summary
  - Recording that the HL7 message failed in vendor software so there is a record that the data has not been uploaded and store the error message so it can be reviewed
  - Alerting appropriate people of failed document upload
  - Triggering another MDM/T02 message once the problems have been corrected (may require software change or update of vendor software with VistA information)
  - Recording that no HL7 Application Acknowledgement was received
  - Recording/acknowledging that an application or commit acknowledgement for the HL7 message was received
  - Determining what happened if the vendor software does not receive a commit or application acknowledgement
  - Triggering another MDM/T02 message to be sent once the problems have been corrected (may require vendor software change or update of vendor software with VistA information)
- Providing a way to retransmit the MDM/T02 message
  - When a message did not upload successfully
  - When they want to upload data that existed in the vendor system prior to the availability of this TIU HL7 upload software

#### Interface Engine Responsibilities

The Interface Engine is responsible for:

- Storing vendor information in a table so it will know that it should receive and accept HL7 messages from the vendor software
- Receiving the HL7 message from the COTS software package
- Routing the HL7 message from the vendor software to the appropriate facility Interface Engine via
- Routing HL7 commit and application Acknowledgement messages to the vendor server
- Sending an email to a designated address when an error occurs

#### VistA Responsibilities

TIU is responsible for:

- Receiving and parsing data from the HL7 message
- Locating a unique patient using identifiers SSN, ICN, DFN, name, and Date of Birth
- Locating a unique patient admission using admission date/time
- Locating the document title in TIU
- Verifying that document text was included in the HL7 message
- Locating the author and cosigner using identifiers SSN, name
- Using the admission date in the HL7 message to locate an inpatient visit in VistA that will be associated with the discharge summary.

A discharge summary must be associated with a patient admission. If TIU cannot find a visit with an admission date that matches the HL7 message data, TIU will reject the HL7 message and not create a discharge summary. TIU will find the admission date and time in the HL7 message and use it to locate an existing visit

If verification proves that it has everything it needs to create a discharge summary, TIU will create a new discharge summary and link it to an inpatient admission. If verification proves there is an error, TIU will create an Application Acknowledgement reject HL7 message with an error code and error text that explains all of the fields that failed verification and TIU will not create a discharge summary document.

If the discharge summary HL7 message contains signature data, TIU will create a signed discharge summary with a status of “completed”. Otherwise, TIU saves the note with a status according to regular TIU business rules. If the document text was transcribed, the status could be set to “unverified”. If the status is “unsigned”, TIU will send an alert to the author (signer) to let them know there is a note to be signed. TIU will send an HL7 Application Accept Acknowledgement message to the vendor software, along with the DFN of the new discharge summary.

A positive acknowledgement indicates that TIU successfully created the discharge summary. A reject acknowledgment indicates that TIU did not create the discharge summary. Reject acknowledgements contain information that indicate why the HL7 message was rejected

#### User Responsibilities

A user is someone who has contact with the vendor, and the vendor software, and has some responsibility for the discharge summary document. More than one user could handle these responsibilities. A user with VistA access is responsible for:

- Ensuring that the exact document title included in the HL7 message exists in TIU and has been created in the TIU discharge SUMMARY document class
- Verifying the discharge summary document if it is created with status “unverified”
- Signing the discharge summary document if it is created with status “unsigned”
- Cosigning the discharge summary document if it is created with status “uncosigned”
- Reviewing the signed document is in VistA if they were the person who signed the document in the vendor software

#### Required Fields

The MDM/T02 HL7 message requires the following fundamental data items:

- Vendor identification
- Patient record VistA facility id
- Patient record VistA facility number
- Patient Name
- Patient identifier (at least one)
  - Patient ICN
  - Patient SSN
  - Patient record number (DFN) created by the VistA facility
- Document title from VistA facility that is from the TIU discharge SUMMARY document class (title in HL7 message must exactly match title in TIU)
- Author (expected signer) name and ID as identified in VistA
- Document text

In addition to the fields that are required in all MDM/T02 HL7 messages, a discharge summary requires visit information.

- 

<span id="_Toc111258286" class="anchor"></span>Table 15: Data Validation Rules

| Home Telehealth vendor server identification            | All   | Placed in MSH and OBX segments to identify the vendor server and vendor server application |
|---------------------------------------------------------|-------|--------------------------------------------------------------------------------------------|
| Patient ICN                                             | Alert | National index for the patient (unique identity within the VA)                             |
| Patient Name                                            | Alert | Legal name of the patient                                                                  |
| Patient SSN                                             | Alert | US index for the patient (unique identity within the US)                                   |
| Patient Date of Birth                                   |       |                                                                                            |
| Patient’s record number in sign up VistA facility (DFN) | Alert | VistA facility index for the patient (unique identity within VistA facility)               |
| Name of document author                                 | All   | Person who will be expected to sign the TIU document in VistA                              |
| Admission date/time                                     |       | VistA date/time of an inpatient visit                                                      |

#### Data Nomenclature

The VistA facility id and VistA facility number are obtained from the Institution File. Patient data comes from VistA Patient File \#2. Information about the author, cosigner, attending physician comes from VistA New Person File \#200.

The institution file definition and extract can be found on the section labeled *Facility address file* on the web page [<u>http://vaww.va.gov/techsvc/projects/VICReplacement_docs.html</u>](http://vaww.va.gov/techsvc/projects/VICReplacement_docs.html). A recent extract from the address file can be directly retrieved from URL <http://vaww.va.gov/techsvc/projects/VIC/FacilityAddresses_Vendor.txt>.

#### Message Content

The HL7 message content is defined in the HL7 2.4 standard chapter 9 (*Medical Records/Information Management (Document Management*).

#### Message Format 

The message type for the discharge summary message is MDM~T02. The Medical Document Management (MDM) Message is documented in Chapter 9 of the HL7 2.4 standard. The HL7 event code is T02, which identifies the message as carrying an “original document and content”. The MDM/T02 HL7 message has six data segments that contain the following information:

- Message identification (MSH)
- Document available event (EVN)
- Patient identification (PID)
- Patient visit information (PV1)
- Document notification (TXA)
- Observation/result data (OBX)

### TIU Document: Surgery Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The vendor has patient information to upload to VistA and they and their VistA contact have decided that it should be stored as a TIU surgery operative report. The vendor software formats the information into document text, builds an HL7 message that contains this text, and sends the HL7 message to VistA, where TIU stores the text in the patient record as a TIU surgery operative report.

#### Description

The vendor creates an MDM/T02 HL7 message to upload a surgery operative report. The message contains document text, information to identify a patient, the document author, the surgery operative report title, and the surgery case number into which they want to store this surgery operative report.

The Surgery Operation report is different from other documents. When a user enters Patient Time Out of OR into the Surgery package, the Surgery package creates a “stub” surgery report document that is linked to the surgery case number. The document does not contain text, so the surgeon has to enter the data manually or a service will need to upload the transcribed text into this stub document. TIU will need to use the surgery case number in the HL7 message to locate the correct stub note and store the report text into this document stub.

TIU will verify the content of the HL7 message and will not add the text to a surgery operative report until it has finished verifying all the required fields. If there are errors, TIU will send an HL7 Application Reject Acknowledgement message to the vendor software. The message will include text descriptions of all the errors found during data verification. If there are no errors, TIU will store the text into the surgery operative report.

#### Responsibilities

Responsibilities are the required actions necessary for the completion of the function; the following paragraphs list the responsibilities.

#### Vendor Responsibilities

In support of the process of creating a surgery operative report, vendor is responsible for:

- Establishing a relationship with one or more VHA sites so the vendor has access to the VHA WAN and an interface engine server located at a VA site
- Receiving information from the VHA site that will
  - Uniquely identify a patient
  - Uniquely identify the VistA location that will receive and store the surgery operative report
  - Uniquely identify the VistA user who is the author (signer) of the document.
  - Uniquely identifies the surgery operative report title at the receiving VA site into which the document text will be stored
  - Uniquely identify the VistA Surgery case and the TIU stub document where the text of the surgery operative report will be stored
  - Locate TIU stub note using surgery case number from the HL7 message
  - If the surgery case number is not included, TIU will attempt to locate surgery case number using the operation date stored in activity date/time field of HL7 message. If TIU can locate one surgery for that date, it will locate and update the stub note. If TIU finds more than one surgery case, it will reject the HL7 message.
- Working with their VHA contact(s) to determine the acceptable layout for the document text and the exact surgery document title
- Creating a trigger in the vendor software that will generate an MDM/T02 HL7 message that contains text of the surgery operative report
- Sending the MDM/T02 HL7 message to the Interface Engine
- Receiving HL7 commit acknowledgement message from the Interface Engine indicating that message was received
- Checking whether the TIU document was successfully updated:
  - Recording that TIU successfully updated the surgery operative report
  - Receiving HL7 Application Accept Acknowledgement message indicating that TIU successfully added text to the surgery operative report
  - Recording successful document transmission in vendor software so there is a record that the data was successfully uploaded, if appropriate
  - Recording that TIU rejected the HL7 message and did not create a surgery operative report
  - Receiving HL7 Application Reject Acknowledgement message indicating that TIU rejected the HL7 message and did not update the surgery operative report
  - Recording that the HL7 message failed in vendor software so there is a record that the data has not been uploaded and store the error message so it can be reviewed
  - Alerting appropriate people of failed document upload
  - Triggering another MDM/T02 message once the problems have been corrected (may require software change or update of vendor software with VistA information)
  - Recording that no HL7 Application Acknowledgement was received
  - Recording that an application or commit acknowledgement for the HL7 message was received
  - Determining what happened if the vendor software does not receive a commit or application acknowledgement
  - Triggering another MDM/T02 message to be sent once the problems have been corrected (may require vendor software change or update of vendor software with VistA information)
- Providing a way to retransmit the MDM/T02 message
  - When a message did not upload successfully
  - When they want to upload data that existed in the vendor system prior to the availability of this TIU HL7 upload software

#### Interface Engine Responsibilities

The Interface Engine is responsible for:

- Storing vendor information in a table so it will know that it should receive and accept HL7 messages from the vendor software
- Receiving the HL7 message from the COTS software package
- Routing the HL7 message from the vendor software to the appropriate facility Interface Engine via
- Routing HL7 commit and application Acknowledgement messages to the vendor server
- Sending an email to a designated address when an error occurs

#### VistA Responsibilities

TIU is responsible for:

- Receiving and parsing data from the HL7 message
- Locating a unique patient using identifiers SSN, ICN, DFN, name, and Date of Birth
- Locating a unique patient admission using admission date/time
- Locating the document title in TIU
- Verifying that document text was included in the HL7 message
- Locating the author and cosigner using identifiers SSN, name
- Locating the stub surgery document in TIU VistA that will be associated with the surgery operative report.
  - Surgery case number
  - Activity date/time = Operation date

A surgery operative report must be uploaded into an existing surgery stub document in TIU. If TIU cannot find the stub TIU document that matches that case number using the HL7 message data, TIU will attempt to locate the case number using the activity date/time. If TIU still cannot locate a surgery case for that date or if there are more than surgery cases for that date, TIU will reject the HL7 message. Surgery reports cannot be created outside of the Surgery package, so TIU cannot create a new surgery operative report from text in an HL7 message.

If verification proves that it has everything it needs, TIU will add text to the stub operation report. If verification proves there is an error, TIU will create an Application Acknowledgement reject HL7 message with an error code and error text that explains all of the fields that failed verification and TIU will not create a new surgery operation report or update an existing stub document.

If the surgery operation report HL7 message contains signature data, TIU will create a signed surgery operation report with a status of “completed”. Otherwise TIU saves the note with a status according to regular TIU business rules. If the document text was transcribed, the status could be set to “unverified”. If the status is “unsigned”, TIU will send an alert to the author (signer) to let them know there is a note to be signed. TIU will send an HL7 Application Accept Acknowledgement message to the vendor software, along with the DFN of the new surgery operation report.

A positive acknowledgement indicates that TIU successfully added text to an existing stub surgery report. A reject acknowledgment indicates that TUI did not add text to an existing stub surgery report. Reject acknowledgements contain information that indicate why the HL7 message was rejected

#### User Responsibilities

A user is someone who has contact with the vendor, and the vendor software, and has some responsibility for the surgery operation report. More than one user could handle these responsibilities. A user with VistA access is responsible for:

- Ensuring that the exact document title included in the HL7 message exists in TIU and has been created in the TIU SURGICAL REPORTS document class
- Verifying the surgery operation report document if it is created with status “unverified”
- Signing the surgery operation report document if it is created with status “unsigned”
- Cosigning the surgery operation report document if it is created with status “uncosigned”
- Reviewing the signed document is in VistA if they were the person who signed the document in the vendor software

#### Required Fields

The MDM/T02 HL7 message for surgery operation reports requires the following fundamental data items:

- Vendor identification
- Patient record VistA facility id
- Patient record VistA facility number
- Patient Name
- Patient identifier (at least one)
- Patient ICN
- Patient SSN
- Patient Date of Birth
- Patient record number (DFN) created by the VistA facility
- Document title from VistA facility that is from the TIU surgery operation report document class (title in HL7 message must exactly match title in TIU)
- Author (expected signer) name and ID as identified in VistA
- Document text

In addition to the fields that are required in all MDM/T02 HL7 messages, a discharge summary requires visit information.

- 

<span id="_Toc111258287" class="anchor"></span>Table 16: Data Validation Rules

| Home Telehealth vendor server identification            | All   | Placed in MSH and OBX segments to identify the vendor server and vendor server application |
|---------------------------------------------------------|-------|--------------------------------------------------------------------------------------------|
| Patient ICN                                             | Alert | National index for the patient (unique identity within the VA)                             |
| Patient Name                                            | Alert | Legal name of the patient                                                                  |
| Patient SSN                                             | Alert | US index for the patient (unique identity within the US)                                   |
| Patient Date of Birth                                   |       |                                                                                            |
| Patient’s record number in sign up VistA facility (DFN) | Alert | VistA facility index for the patient (unique identity within VistA facility)               |
| Name of document author                                 | All   | Person who will be expected to sign the TIU document in VistA                              |
| Admission date/time                                     |       | VistA date/time of an operation visit                                                      |

#### Data Nomenclature

The VistA facility id and VistA facility number are obtained from the Institution File. Patient data comes from VistA Patient File \#2. Information about the author, cosigner, attending physician comes from VistA New Person File \#200.

The institution file definition and extract can be found on the section labeled *Facility address file* on the web page [<u>http://vaww.va.gov/techsvc/projects/VICReplacement_docs.html</u>](http://vaww.va.gov/techsvc/projects/VICReplacement_docs.html). A recent extract from the address file can be directly retrieved from URL <http://vaww.va.gov/techsvc/projects/VIC/FacilityAddresses_Vendor.txt>.

#### Message Content

The HL7 message content is defined in the HL7 2.4 standard chapter 9 (*Medical Records/Information Management (Document Management*).

#### Message Format 

The message type for the discharge summary message is MDM~T02. The Medical Document Management (MDM) Message is documented in Chapter 9 of the HL7 2.4 standard. The HL7 event code is T02, which identifies the message as carrying an “original document and content”. The MDM/T02 HL7 message has six data segments that contain the following information:

Message identification (MSH)

Document available event (EVN)

Patient identification (PID)

Patient visit information (PV1)

Document notification (TXA)

Observation/result data (OBX)

References

*Health Level Seven, Version 2.4* standard can be found at URL <http://vista.med.va.gov/messaging/msgadmin/hl7_specifications.asp>.

VHA OI Home Telehealth Web site containing this document and other information can be found at URL <http://vaww.va.gov/techsvc/projects/HomeTelehealthHL7.html>

[*HL7 Vitals Message Profile*](http://vaww.va.gov/techsvc/projects/eHomeCare/HDRVitalsMessageProfile.doc) (<http://vaww.va.gov/techsvc/projects/eHomeCare/HDRVitalsMessageProfile.doc>) defines the HL7 messages used to transfer vitals to HDR.

VA Data Standards group posts the current standards work at URL <http://vaww.infoshare.va.gov/Data_Standardization/Working%20Groups/Vitals_DAT/default.aspx>.

[*HL7 Telehealth Message Profiles*](http://vaww.va.gov/techsvc/projects/HomeTelehealthHL7.html) (<http://vaww.va.gov/techsvc/projects/HomeTelehealthHL7.html>) defines the HL7 messages used to implement the Home Telehealth patient sign up, observation, and acknowledgements.

[*Master Patient Index (MPI)/Patient Demographics (PD) HL7 Interface Specification*](http://vista.med.va.gov/VistA_Lib/Clinical/MPI_Patient_Demographics_(MPI-PD)/MPI_PD_HL7_Interface.pdf) (<http://vista.med.va.gov/VistA_Lib/Clinical/MPI_Patient_Demographics_(MPI-PD)/MPI_PD_HL7_Interface.pdf>) defines the HL7 message ate are used with MPI.

The institution master file is maintained on FORUM.

A current extract from that file can be found at URL <http://vaww.va.gov/techsvc/projects/VIC/FacilityAddresses_Vendor.txt>.

The File Format Specification can be found at URL <http://vaww.va.gov/techsvc/projects/VIC/FacilityAddressFileFormat.doc>.

A complete list of VA IT acronyms can be found at URL <http://vaww1.va.gov/med/acronyms/acronym.cfm>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ACK General Acknowledgment message. The ACK message is used to respond to a message where there has been an error that precludes application processing or where the application does not define a special message type for the response.
Acknowledgment—Application Level The appropriate application on the receiving system receives the transaction and processes it successfully. The receiving system returns an application-dependent response to the initiator.
Acknowledgment—Accept Level The receiving system commits the message to safe storage in a manner that releases the sending system from any obligation to resend the message. A response is returned to the initiator indicating successful receipt and secure storage of the information.
Austin Automation Center (AAC) AAC is a corporate data center for VA. The central repository for National Patient Care Database is maintained at the AAC.
ASU Authorization/Subscription Utility, an application that allows sites to associate users with user classes, allowing them to specify the level of authorization needed to sign or order specific document types and orderables. ASU is distributed with TIU in this version; eventually it will probably become independent, to be used by many V*IST*A packages.
Action A functional process that a clinician or clerk uses in the TIU computer program. For example, “Edit” and “Search” are actions. Protocol is another name for Action.
Boilerplate Text A pre-defined TIU template that can be filled in for Titles, speeding up the entry process. TIU exports several Titles with boilerplate text which can be modified to meet specific needs; sites can also create their own.
Business Rule Part of ASU, Business Rules authorize specific users or groups of users to perform specified actions on documents in particular statuses (e.g., an unsigned progress note may be edited by a provider who is also the expected signer of the note).
Care Coordinators Care Coordinators are licensed health care professionals who help veteran patients self-manage their condition and in doing so guide and support them to ensure they receive the right care, in the right place, at the right time from the right person.
Class Part of Document Definitions, Classes group documents. For example, “Progress Notes” is a class with many kinds of progress notes under it.
Classes may be subdivided into other Classes or Document Classes. Besides grouping documents, Classes also store behavior which is then inherited by lower level entries.
Clinician A doctor or other provider in the medical center who is authorized to provide patient care.
Component Components are “sections” or “pieces” of documents, such as Subjective, Objective, Assessment, and Plan in a SOAP Progress Note. Components may have (sub)Compon-ents as items. They may have Boilerplate Text. Components may be designated as “Shared.”
Consult Referral of a patient by the primary care physician to another hospital service/ specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion.
COTS Commercial Off The Shelf. Describes software or hardware products that are ready-made and available for sale to the general public. COTS include VA applications that are not part of the VistA system.
CPRS Computerized Patient Record System. CPRS provides an integrated patient record system for clinicians, managers, quality assurance staff, and researchers. The primary goal of CPRS is to create a fast and easy-to-use product that gives physicians enough information through clinical reminders, results reporting, and expert system feedback to make better decisions regarding orders and treatment. V*IST*A software integrated with CPRS includes Pharmacy, Lab, Radiology, Allergy Tracking, Consults, Dietetics, Progress Notes, Problem List, Patient Administration, Vitals, PCE, TIU, ASU and Clinical Lexicon.
CWAD Cautions, Warnings, Adverse Reactions, Directives; a type of Progress Note.
DFN Data File Number used in VA FileMan. Sometimes referred to as the Patient’s Internal Entry Number (IEN).
Discharge Summary Discharge summaries are summaries of a patient’s medical care during a single hospitalization, including the pertinent diagnostic and therapeutic tests and procedures as well as the conclusions generated by those tests. They are required for all discharges and transfers from a VA medical center, domiciliary, or nursing home care. The automated Discharge Summary module of TIU provides an efficient and immediate mechanism for clinicians to capture transcribed patient discharge summaries online, where they’re available for review, signing, adding addendum, etc.
Document Class Document Classes are categories that group documents (Titles) with similar characteristics together. For example, Nursing Progress Notes might be a Document Class, with Nursing Dialysis Progress Notes, Nursing psychology Progress Notes, etc. as Titles under it. Or maybe the Document Class would be Psychology Notes, with Psychology Nursing Notes, Psychology Social Worker Notes, Psychology Patient Education Notes, etc. under that Document Class..
Document Definition Document Definition is a subset of TIU that provides the building blocks for TIU, by organizing the elements of documents into a hierarchy structure. This structure allows documents (Titles) to inherit characteristics (such as signature requirements and print characteristics) of the higher levels, Class and Document Class. It also allows the creation and use of boilerplate text and embedded objects.
HC HealthConnect- Component System of HealthShare Platform, InterSystems Product. VA formal communications gateway to VistA applications. Communication components work concurrently to model, automate, track, and optimize communication processes within and between data systems, providing a high emphasis on security and reliability. The product will also enable real-time, multi-directional communication among VistA applications, the HDR, Commercial-Off-The-Shelf (COTS) products, and other systems.
HIMS Hospital Information Management System, common abbreviation/synonym used at VA site facilities; also known as MIS (see below).
HIPAA Health Insurance Portability and Accountability Act. Addresses the security and privacy of health data.
HL7 Health Level 7. An ANSI recognized information exchange protocol used in medicine, and possibly elsewhere. The protocol architecture is hierarchical, moving from high-level groupings and structures to a set of several hundred data fields. Each level of the hierarchy serves a different organizing purpose and is designed to accommodate the flexibility necessary for compatibility of specialized data sets that have facility-specific needs. See the HL7 website: [www.hl7.org](http://www.hl7.org).
ICN Integration Control Number. A unique identifier assigned to patients when they are added to the Master Patient Index. ICNs fall under two categories: national and local. The ICN follows the ASTM E1714-95 standard for a universal health identifier. ICNs link patients to their records across VA systems. The ICN is stored in a message using the HL7 CX format. The ID subfield is the ICN. The type subfield is USVHA.
ID Coded Value data type.
IE Interface Engine. A device or software application that connects disparate system, transforms data, converts data, routes data, ensures the delivery of data and is rules based. The IE provides a consistent HL7 compliant communication environment. That is separate from the specific and individual application needs. Within this environment messages can be routed, transformed, converted and delivery guaranteed as required by the application.
IEN Internal Entry Number. Used by FileMan, it is a unique number assigned to each entry in an M global.
IRT Incomplete Record Tracking, a package TIU can interface with to transmit incomplete progress notes and discharge summaries.
Interdisciplinary Note A new feature of Text Integration Utilities (TIU) for expressing notes from different care givers as a single episode of care. They always start with a single note by the initial contact person (e.g., triage nurse, case manager, attending) and continue with separate notes created and signed by other providers, then attached to the original note.
ISO Information Security Officer. Every medical center within the VA has one.
MIS Common abbreviation/synonym used at VA site facilities for the Medical Information Section of Medical Administration Service. May be called HIMS (Health Information Management Section).
MIS Manager Manager of the Medical Information Section of Medical Administration Service at the site facility who has ultimate responsibility to see that MRTs complete their duties.
MPI Master Patient Index. Creates an index that uniquely identifies each active patient treated by the Veterans Administration and to identify the VHA facilities where a patient is receiving care. This is crucial to the sharing of patient information across sites. Master Patient Index manages the synchronization of patient file information with the Master Patient Index and with the patient's treating facilities to insure that data being shared is stored in the correct patient's record.
MRT Medical Record Technician in the Medical Information Section of Medical Administration Service at the site facility who completes the tasks of assuring that all discharge summaries placed in a patient’s medical record have been verified for accuracy and completion and that a permanent chart copy has been placed in a patient’s medical record for each separate admission to the hospital.
Protocol A set of procedures for establishing and controlling data transmission
Procedure Request Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/specialty without requiring formal consultation first.
RDV Remote Data View. A CPRS application that allows a caregiver to view patient data that is stored at another VHA facility.
Result A consequence of an order. Refers to evaluation or status results. In regards to Consult/Request Tracking, results refer to a TIU document or Medicine procedure result attached to the consult or procedure request.
Requestor This is the health care provider (e.g., the physician/clinician) who requests the order to be done.
ROES Remote Order Entry System.
Screen Context This term refers to the particular selection of orders displayed on the screen (e.g., Medicine consults for the patient Ralph Jones).
Service A clinical or administrative specialty (or department) within a Medical Center.
SSN Social Security Number
Status A result that indicates the processing state of an order; for example, a Cardiology Consult order may be “discontinued (dc)” or “completed (c)”.
Status Symbols Codes used in order entry and Consults displays to designate the status of the order.
Telehealth The use of electronic communications and information technology to provide and support health care when distance separates the participants. It covers health care practitioners interacting with patients and patients interacting with other patients.
Telemedicine The provision of care by a licensed independent health care provider that directs, diagnoses, or otherwise provides clinical treatment delivered using electronic communications and information technology when distance separates the provider and the patient. .
TCP/IP Transaction Control Protocol/Internet Protocol A set of protocols for Layers 3 (Network) and 4 (Transport) of the OSI network model. TCP/IP has been developed over a period of 30 years under the auspices of the Department of Defense. It is a de facto standard, particularly as higher-level layers over Ethernet. TCP/IP predates the OSI model; and thus, TCP/IP is not OSI-compliant.
TIU Text Integration Utilities, a part of VistA that files clinical notes. These are most visible in CPRS on the Notes tab.
USVHA United States Veterans Health Administration
VA Department of Veterans Affairs
VAMC Department of Veterans Affairs Medical Center
VIE VistA Interface Engine. Deprecated – Being migrated to HealthConnect. Formerly called the Vitria Interface Engine.
VistA Veteran Health Information System and Technology Architecture
VistA Web A new web based application to view patient data at a set of VA facilities.

# Appendix A: Messaging Workbench

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is sample printout from the Messaging Work Bench (MWB). The HL7 message format is one used during the testing of Generic HL7.

MWB is a tool that facilitates the creation of HL7 2.4 message profile definitions. MWB supports exporting of the message metadata into HL7v2 Message Conformance Profile format.

The MWB is a tool for analysts and developers that facilitates the construction, documentation and reporting of message specifications as well as HL7 Conformance profiles. It follows the standards set by the HL7 version 2.4 Conformance Special Interest Group (SIG) and produces profiles that are interoperable with other HL7 compliant messaging tools. In addition to its profile documentation function, this tool includes other features to assist messaging developers, such as reverse engineering, message instance analysis and message instance validation.

The MWB is the first freeware tool available for creating message profiles. The MWB developer works for VHA and is an active member of the HL7 Conformance Special Interest Group (SIG) and the tool has evolved with input from this SIG. The MWB tool is used extensively within VHA for developing and documenting HL7 messages.

MWB HL7 message profiles for TIU HL7 are available to any vendor who wishes to download and use the MWB tool. A Word document generated by the tool is also available to provide the workbench information in a readable/printable format.

The MWB software can be downloaded from the VHA Intranet:

[http://vista.med.va.gov/messaging/](http://vista.med.va.gov/messaging/) then select VistA HL7 Website, then follow the link to HL7 Messaging Workbench.

The MWB software can also be downloaded from the HL7 website [<u>www.hl7.org</u>](file:///C:\Users\vhaisdsafkol\AppData\Local\Microsoft\Windows\INetCache\Content.Outlook\AppData\Local\Microsoft\Windows\Temporary%20Internet%20Files\Content.IE5\PD7F0DPK\www.hl7.org). From the home page heading “Committees”, select

Special Interest Groups (SIG)

Conformance

Documents and Presentations

There is a good tutorial on HL7 on the VistA HL7 webpage. To access it go to the VistA HL7 website at: [http://vista.med.va.gov/messaging](http://vista.med.va.gov/messaging). Then follow the links to HL7 Documents and Presentations. From this page scroll down until you fine Archived Documents and Presentations then select HL7 1.6 Tutorial.ppt.

## HL7 Message Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HL7 Message Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Implementation Note:                                                                                                                                                                                                                                                                                                                                                                   |
|   This MWB profile defines the HL7 MDM T02 message COTS applications can use to upload text data into VistA Text Integration Utilities (TIU) documents. The COTS application must have access to the VA WAN and must have a relationship with a VHA site . The COTS package must also have patient specific information that the site wants uploaded into a TIU document.              |
|   The vendor should work closely with their VHA contact as they prepare their HL7 message. The COTS package will establish a trigger event that creates an unsolicited MDM/T02 message and sends it to VistA. The HL7 message will contain document text in a format approved by their VA contact, along with the exact title of a TIU document that exists at the receiving VHA site. |
|   Important: The location of the title in the TIU hierarchy determines the document type, not the content of the HL7 message. The following TIU document types are supported:                                                                                                                                                                                                          |
|   Progress Note TIU PROGRESS NOTES document class must be associated with a visit                                                                                                                                                                                                                                                                                                      |
|   Consult Note TIU CONSULTS document class must be linked to an existing consult                                                                                                                                                                                                                                                                                                       |
|   Discharge Summary TIU DISCHARGE SUMMARY document class must be associated with an admission                                                                                                                                                                                                                                                                                          |
|   Surgery Report TIU SURGICAL REPORTS document class must be an existing TIU stub note                                                                                                                                                                                                                                                                                                 |
|   Other TIU document classes with special processing are not supported by this software:                                                                                                                                                                                                                                                                                               |
|   Not Supported: Patient Record Flags document class                                                                                                                                                                                                                                                                                                                                   |
|   Not Supported: Addendum document class                                                                                                                                                                                                                                                                                                                                               |
|   Not Supported: Clinical Procedures document class                                                                                                                                                                                                                                                                                                                                    |
|   The HL7 message will be processed if, at the receiving VistA location, TIU can: Identify a unique patient; Identify a unique person who is the author or cosigner of the document; Locate the exact document title; Locate other information required for the specific TIU document types. The HL7 message can also include specific user information to create a signed document.   |
|   If the HL7 message passes all TIU validations and TIU is able to create/update a TIU document, an Application Acknowledgement HL7 message will be returned to the COTS package.                                                                                                                                                                                                      |

|                         |                                                                                                     |
|-------------------------|-----------------------------------------------------------------------------------------------------|
| Interface ID        |   HL7 Generic Interface with TIU - rev                                                              |
| Organization        |   HDS                                                                                               |
| HL7 Version         |   2.4                                                                                               |
| Spec Version        |   .0                                                                                                |
| Application Role    |   Sender                                                                                            |
| Conformance Type    |   Strict                                                                                            |
| Encodings           |  ER7                                                                                                |
| Event Description   |   Original document notification and content                                                        |
| Message Type        |   MDM                                                                                               |
| Event Type          |   T02                                                                                               |
| Order Control Code  |                                                                                                     |
| Message Structure   |   MSH,EVN,PID,PV1,TXA,{OBX}                                                                         |
| Structure Type      |   MDM_T02                                                                                           |
| Accept Ack          |   NE                                                                                                |
| Application Ack     |   AL                                                                                                |
| Ack Mode            |   Deferred                                                                                          |
| Static Profile ID   |   {ConfSig(1) HDS(1) 2.4(7) static-profile(1) MDM(23) T02(226) null(0) MDM_T02(51) .0(1) Sender(1)} |
| Dynamic Profile ID  |   {ConfSig(1) HDS(1) 2.4(7) dynamic-profile(2) AccNE_AppAL(2) defer_mode_ack(1)}                    |

## ## Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 46%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Optionality Codes:</p>
<ul>
<li><p>R - required</p></li>
<li><p>RE - required or empty</p></li>
<li><p>C - conditional</p></li>
<li><p>CE - conditional or empty</p></li>
<li><p>O - optional</p></li>
<li><p>NS - not supported</p></li>
<li><p>U - unknown</p></li>
</ul></td>
<td><p>Abbreviations:</p>
<ul>
<li><p>seq - sequence</p></li>
<li><p>DT - datatype</p></li>
<li><p>Len - length</p></li>
<li><p>Opt - optionality</p></li>
<li><p>Rep - repeatable</p></li>
<li><p>Min - quantity min</p></li>
<li><p>Max - quantity max</p></li>
<li><p>Tbl - table</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="segment-msh">Segment: MSH </h3></td>
</tr>
<tr class="even">
<td><strong>Description:</strong> Message Header</td>
</tr>
<tr class="odd">
<td><strong>Optionality:</strong> R</td>
</tr>
<tr class="even">
<td><strong>Repeatable:</strong> False</td>
</tr>
<tr class="odd">
<td><strong>Minimum:</strong> 1</td>
</tr>
<tr class="even">
<td><strong>Maximum:</strong> 1</td>
</tr>
<tr class="odd">
<td><strong>Reference:</strong> </td>
</tr>
</tbody>
</table>

#### Fields

|                                                                              |         |        |         |         |         |         |         |         |               |               |            |               |
|------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|---------------|
| Name                                                                     | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference |
|   Field Separator                                                            |   1     |   ST   |   1     |   R     | False   |   1     |   1     |         |               |               |   ^        |   2.16.9.1    |
|   Encoding Characters                                                        |   2     |   ST   |   4     |   R     | False   |   1     |   1     |         |               |               |   ~\|\\    |   2.16.9.2    |
| Implementation Note:                                                         |         |        |         |         |         |         |         |         |               |               |            |               |
|   Escape sequences to use for the field separator and encoding characters if |         |        |         |         |         |         |         |         |               |               |            |               |
|   they occur in the body of any text field:                                  |         |        |         |         |         |         |         |         |               |               |            |               |
|   \F\\ field separator ^                                                     |         |        |         |         |         |         |         |         |               |               |            |               |
|   \S\\ component separator ~                                                 |         |        |         |         |         |         |         |         |               |               |            |               |
|   \R\\ repetition separator \|                                               |         |        |         |         |         |         |         |         |               |               |            |               |
|   \E\\ escape character \\                                                   |         |        |         |         |         |         |         |         |               |               |            |               |
|   \T\\ subcomponent separator &                                              |         |        |         |         |         |         |         |         |               |               |            |               |
| HL7 Definition:                                                              |         |        |         |         |         |         |         |         |               |               |            |               |
|   Component separator, Repetition separator, Escape character,               |         |        |         |         |         |         |         |         |               |               |            |               |
|  Subcomponent separator                                                      |         |        |         |         |         |         |         |         |               |               |            |               |

|                                                                                                                                                                |         |        |         |         |         |         |         |         |               |               |                                |               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|--------------------------------|---------------|
| Name                                                                                                                                                       | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val                     | Reference |
|   Sending Application                                                                                                                                          |   3     |   HD   |   50    |   R     | False   |   1     |   1     | 0361    |               |               |                                |   2.16.9.3    |
| HL7 Definition:                                                                                                                                                |         |        |         |         |         |         |         |         |               |               |                                |               |
|   Uniquely identifies the sending COTS application among all other applications                                                                                |         |        |         |         |         |         |         |         |               |               |                                |               |
|   that send HL7 messages to TIU. Entirely  site-defined. The network enterprise                                                                                |         |        |         |         |         |         |         |         |               |               |                                |               |
|   consists of all those applications that participate in the exchange of HL7                                                                                   |         |        |         |         |         |         |         |         |               |               |                                |               |
|   messages within the enterprise.                                                                                                                              |         |        |         |         |         |         |         |         |               |               |                                |               |
|    namespace ID                                                                                                                                                |   1     |   IS   |   20    |   R     |         |   1     |   1     |   0363  |               |               |   HTAPPL                       |               |
| Implementation Note:                                                                                                                                           |         |        |         |         |         |         |         |         |               |               |                                |               |
|   User defined table 0363: No need to add COTS application ID to table.                                                                                        |         |        |         |         |         |         |         |         |               |               |                                |               |
| HL7 Definition:                                                                                                                                                |         |        |         |         |         |         |         |         |               |               |                                |               |
|   A character string that uniquely identifies the sending COTS application.                                                                                    |         |        |         |         |         |         |         |         |               |               |                                |               |
|    universal ID                                                                                                                                                |   2     |   ST   |   3     |   NS    |         |   0     |   0     |         |               |               |                                |               |
|    universal ID type                                                                                                                                           |   3     |   ID   |   3     |   NS    |         |   0     |   0     |   0301  |               |               |                                |               |
|   Sending Facility                                                                                                                                             |   4     |   HD   |   110   |   R     | False   |   1     |   1     |  0362   |               |               |                                |   2.16.9.4    |
| HL7 Definition:                                                                                                                                                |         |        |         |         |         |         |         |         |               |               |                                |               |
|   Identifies the sending application among multiple identical instances of the application running on behalf of different organizations.                       |         |        |         |         |         |         |         |         |               |               |                                |               |
|    namespace ID                                                                                                                                                |   1     |   IS   |   10    |   R     |         |   1     |   1     |   0363  |               |               |   200T5                        |               |
| Implementation Note:                                                                                                                                           |         |        |         |         |         |         |         |         |               |               |                                |               |
|   No need to add COTS facility ID to table.                                                                                                                    |         |        |         |         |         |         |         |         |               |               |                                |               |
| HL7 Definition:                                                                                                                                                |         |        |         |         |         |         |         |         |               |               |                                |               |
|   Namespace ID assigned to COTS package. Required by HC. Alpha numeric.                                                                                        |         |        |         |         |         |         |         |         |               |               |                                |               |
|    universal ID                                                                                                                                                |   2     |   ST   |   90    |   R     |         |   1     |   1     |         |               |               |   VAWW.VITERION. CC.MED.VA.GOV |               |
| HL7 Definition:                                                                                                                                                |         |        |         |         |         |         |         |         |               |               |                                |               |
|   Universal ID that identifies sending COTS facility. Domain name is better than a hard coded IP address because it will still work if the IP address changes. |         |        |         |         |         |         |         |         |               |               |                                |               |
|    universal ID type                                                                                                                                           |   3     |   ID   |   3     |   R     |         |   1     |   1     |   0301  |               |               |   DNS                          |               |
| HL7 Definition:                                                                                                                                                |         |        |         |         |         |         |         |         |               |               |                                |               |
|   DNS = Internet dotted name.                                                                                                                                  |         |        |         |         |         |         |         |         |               |               |                                |               |

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 10%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><strong>Seq</strong></td>
<td><strong>DT</strong></td>
<td><strong>Len</strong></td>
<td><strong>Opt</strong></td>
<td><strong>Rep</strong></td>
<td><strong>Min</strong></td>
<td><strong>Max</strong></td>
<td><strong>Tbl</strong></td>
<td><strong>Predicate</strong></td>
<td><strong>Fixed Val</strong></td>
<td><strong>Ex Val</strong></td>
<td><strong>Reference</strong></td>
</tr>
<tr class="even">
<td>  Receiving Application</td>
<td>  5</td>
<td>  HD</td>
<td>  50</td>
<td>  R</td>
<td>False</td>
<td>  1</td>
<td>  1</td>
<td> 0361</td>
<td> </td>
<td>   </td>
<td>   </td>
<td>  2.16.9.5</td>
</tr>
<tr class="odd">
<td colspan="11">HL7 Definition:</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">  Uniquely identifies the receiving application among all other applications within the network enterprise</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>   namespace ID</td>
<td>  1</td>
<td>  IS</td>
<td>  20</td>
<td>  R</td>
<td> </td>
<td>  1</td>
<td>  1</td>
<td>  0363</td>
<td> </td>
<td> </td>
<td>  TIUHL7</td>
<td> </td>
</tr>
<tr class="even">
<td colspan="11">Implementation Note:</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">  No need to add VA application ID to table.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">HL7 Definition:</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">  Namespace ID that identifies TIU/HL7 as the receiving application/process. TIUHL7 is recommended</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>   universal ID</td>
<td>  2</td>
<td>  ST</td>
<td>  3</td>
<td>  NS</td>
<td> </td>
<td>  0</td>
<td>  0</td>
<td> </td>
<td>   </td>
<td>   </td>
<td>   </td>
<td> </td>
</tr>
<tr class="odd">
<td>   universal ID type</td>
<td>  3</td>
<td>  ID</td>
<td>  3</td>
<td>  NS</td>
<td> </td>
<td>  0</td>
<td>  0</td>
<td>  0301</td>
<td>   </td>
<td>   </td>
<td>   </td>
<td> </td>
</tr>
<tr class="even">
<td>  Receiving Facility</td>
<td>  6</td>
<td>  HD</td>
<td>  180</td>
<td>  R</td>
<td>False</td>
<td>  1</td>
<td>  1</td>
<td> 0110</td>
<td> </td>
<td>   </td>
<td>   </td>
<td>  2.16.9.6</td>
</tr>
<tr class="odd">
<td colspan="11">HL7 Definition:</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">  Identifies the receiving application among multiple identical instances of the application running on behalf of different organizations. Site defined. Facility must have TIU HL7 installed and must have the patient record to which this TIU document will be added.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>   namespace ID</td>
<td>  1</td>
<td>  IS</td>
<td>  10</td>
<td>  R</td>
<td> </td>
<td>  1</td>
<td>  1</td>
<td>  0363</td>
<td> </td>
<td> </td>
<td>  552</td>
<td> </td>
</tr>
<tr class="even">
<td colspan="11">Implementation Note:</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">  No need to add ID to table.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">HL7 Definition:</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">  VistA site ID.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>   universal ID</td>
<td>  2</td>
<td>  ST</td>
<td>  90</td>
<td>  R</td>
<td> </td>
<td>  1</td>
<td>  1</td>
<td> </td>
<td> </td>
<td> </td>
<td><p>DAYTLAB.FO-BAYPINES.MED.</p>
<p>VA.GOV</p></td>
<td> </td>
</tr>
<tr class="odd">
<td colspan="11">HL7 Definition:</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">  Universal ID that identifies sending VistA facility. Domain name is better than a hard coded IP address because it will still work if the IP address changes.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>   universal ID type</td>
<td>  3</td>
<td>  ID</td>
<td>  3</td>
<td>  R</td>
<td> </td>
<td>  1</td>
<td>  1</td>
<td>  0301</td>
<td> </td>
<td> </td>
<td>  DNS</td>
<td> </td>
</tr>
<tr class="even">
<td colspan="11">HL7 Definition:</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">  DNS = Internet dotted name.</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 3%" />
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 9%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><strong>Seq</strong></td>
<td><strong>DT</strong></td>
<td><strong>Len</strong></td>
<td><strong>Opt</strong></td>
<td><strong>Rep</strong></td>
<td><strong>Min</strong></td>
<td><strong>Max</strong></td>
<td><strong>Tbl</strong></td>
<td><strong>Predicate</strong></td>
<td><strong>Fixed Val</strong></td>
<td><strong>Ex Val</strong></td>
<td><strong>Reference</strong></td>
</tr>
<tr class="even">
<td>  Date/Time Of Message</td>
<td>  7</td>
<td>  TS</td>
<td>  26</td>
<td>  R</td>
<td>False</td>
<td>  1</td>
<td>  1</td>
<td> </td>
<td> </td>
<td>   </td>
<td>   </td>
<td>  2.16.9.7</td>
</tr>
<tr class="odd">
<td colspan="11">HL7 Definition: Date/time that the COTS package created the message.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>   Date/Time</td>
<td>  1</td>
<td>  NM</td>
<td>  14</td>
<td>  R</td>
<td> </td>
<td>  1</td>
<td>  1</td>
<td> </td>
<td> </td>
<td> </td>
<td>20050629163312</td>
<td>  2.16.9.7</td>
</tr>
<tr class="odd">
<td>   degree of precision</td>
<td>  2</td>
<td>  ST</td>
<td>  1</td>
<td>  NS</td>
<td> </td>
<td>  0</td>
<td>  0</td>
<td> </td>
<td>   </td>
<td>   </td>
<td>   </td>
<td> </td>
</tr>
<tr class="even">
<td>  Security</td>
<td>  8</td>
<td>  ST</td>
<td>  40</td>
<td>  NS</td>
<td>False</td>
<td>  0</td>
<td>  0</td>
<td> </td>
<td>   </td>
<td>   </td>
<td>   </td>
<td>  2.16.9.8</td>
</tr>
<tr class="odd">
<td>  Message Type</td>
<td>  9</td>
<td>CM_MSG</td>
<td>  15</td>
<td>  R</td>
<td>False</td>
<td>  1</td>
<td>  1</td>
<td>0076</td>
<td> </td>
<td>   </td>
<td>   </td>
<td>  2.16.9.9</td>
</tr>
<tr class="even">
<td colspan="11">HL7 Definition:</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">  Unsolicited document creation. The COTS package could have two methods for triggering this message.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">  1. Internal processing triggers the event</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">  2. Event manually triggered by user; could be used to resubmit an HL7 message or to submit an HL7 message for an event that took place prior to installation of this software.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">  Examples: document completed and locked; document signed and locked; order submitted, order updated, order completed; weekly report completed; incident report completed;</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>   message type</td>
<td>  1</td>
<td>  ID</td>
<td>  3</td>
<td>  R</td>
<td> </td>
<td>  1</td>
<td>  1</td>
<td>  0076</td>
<td> </td>
<td> </td>
<td>  MDM</td>
<td> </td>
</tr>
<tr class="even">
<td>   trigger event</td>
<td>  2</td>
<td>  ID</td>
<td>  3</td>
<td>  R</td>
<td> </td>
<td>  1</td>
<td>  1</td>
<td>  0003</td>
<td> </td>
<td> </td>
<td>  T02</td>
<td> </td>
</tr>
<tr class="odd">
<td>   message structure</td>
<td>  3</td>
<td>  ID</td>
<td>  3</td>
<td>  NS</td>
<td> </td>
<td>  0</td>
<td>  0</td>
<td>  0354</td>
<td>   </td>
<td>   </td>
<td>   </td>
<td> </td>
</tr>
<tr class="even">
<td>  Message Control ID</td>
<td>  10</td>
<td>  ST</td>
<td>  30</td>
<td>  R</td>
<td>False</td>
<td>  1</td>
<td>  1</td>
<td> </td>
<td> </td>
<td> </td>
<td><p>20050621153255</p>
<p>MDMT02</p></td>
<td>  2.16.9.10</td>
</tr>
<tr class="odd">
<td colspan="11">HL7 Definition:</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">  Contains a number or other identifier created by the COTS package to uniquely identify the message. It is echoed back to the COTS package in the Message Acknowledgement Segment (MSA)</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Processing ID</td>
<td>  11</td>
<td>  PT</td>
<td>  3</td>
<td>  R</td>
<td>False</td>
<td>  1</td>
<td>  1</td>
<td> </td>
<td> </td>
<td>   </td>
<td>   </td>
<td>  2.16.9.11</td>
</tr>
<tr class="even">
<td colspan="11">Implementation Note:</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">  This field must be set to "P" for production when the software runs</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">  against production VistA.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">HL7 Definition:</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">  This field is used to decide whether to   process the message as defined in HL7</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">  Application. This allows different priorities   to be given to different processing modes.</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

|                                                                                                                                                      |         |        |         |         |         |         |         |         |               |               |            |               |
|------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|---------------|
| Name                                                                                                                                             | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference |
|    processing ID                                                                                                                                     |   1     |   ID   |   3     |   R     |         |   1     |   1     |   0103  |               |               |   T        |               |
| Implementation Note:                                                                                                                                 |         |        |         |         |         |         |         |         |               |               |            |               |
|   HC requires that this field be set to "P" when HL7 message is sent to a VistA production site. They also look for "T" when running at a test site. |         |        |         |         |         |         |         |         |               |               |            |               |
| HL7 Definition:                                                                                                                                      |         |        |         |         |         |         |         |         |               |               |            |               |
|   T=Training, P=Production                                                                                                                           |         |        |         |         |         |         |         |         |               |               |            |               |
|    processing mode                                                                                                                                   |   2     |   ID   |   3     |  NS     |         |   0     |   0     | 0207    |               |               |            |               |
|   Version ID                                                                                                                                         |   12    | VID    |   10    |   R     | False   |   1     |   1     | 0104    |               |               |            | 2.16.9.12     |
| HL7 Definition:                                                                                                                                      |         |        |         |         |         |         |         |         |               |               |            |               |
|   HL7 2.4                                                                                                                                            |         |        |         |         |         |         |         |         |               |               |            |               |
|    version ID                                                                                                                                        |   1     |   ID   |   3     |   R     |         |   1     |   1     | 0104    |               |               |   2.4      |               |
|    internationalization code                                                                                                                         |   2     |   CE   |   0     |  NS     |         |   0     |   0     |         |               |               |            |               |
|    international version ID                                                                                                                          |   3     |   CE   |   0     |  NS     |         |   0     |   0     |         |               |               |            |               |
|   Sequence Number                                                                                                                                    |   13    |  NM    |   15    |  NS     | False   |   0     |   0     |         |               |               |            |   2.16.9.13   |
|   Continuation Pointer                                                                                                                               |   14    |   ST   | 180     |  NS     | False   |   0     |   0     |         |               |               |            |   2.16.9.14   |
|   Accept Acknowledgment Type                                                                                                                         |   15    |   ID   |   2     |   R     | False   |   1     |   1     | 0155    |               |               |   AL       |   2.16.9.15   |
| HL7 Definition:                                                                                                                                      |         |        |         |         |         |         |         |         |               |               |            |               |
|   Identifies the conditions under which commit acknowledgments are required to                                                                       |         |        |         |         |         |         |         |         |               |               |            |               |
|   be returned in response to this message. Should be set to AL="always".                                                                             |         |        |         |         |         |         |         |         |               |               |            |               |
|   Application Acknowledgment Type                                                                                                                    |   16    |   ID   |   2     |   R     | False   |   1     |   1     | 0155    |               |               |   AL       |  2.16.9.16    |
| HL7 Definition:                                                                                                                                      |         |        |         |         |         |         |         |         |               |               |            |               |
|   Identifies the conditions under which application acknowledgments are required                                                                     |         |        |         |         |         |         |         |         |               |               |            |               |
|   to be returned in response to this   message. Should be set to AL = "always"                                                                       |         |        |         |         |         |         |         |         |               |               |            |               |
|   Country Code                                                                                                                                       |   17    |   ID   |   3     | NS      | False   |   0     |   0     | 0399    |               |               |            | 2.16.9.17     |
|   Character Set                                                                                                                                      |   18    |   ID   |   16    | NS      | False   |   0     |   0     | 0211    |               |               |            | 2.16.9.18     |

|                                           |         |        |         |         |         |         |         |         |               |               |            |               |
|-------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|---------------|
| Name                                  | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference |
|   Principal Language Of Message           |   19    |   CE   |   250   |   NS    | False   |   0     |   0     |         |               |               |            |   2.16.9.19   |
|   Alternate Character Set Handling Scheme |   20    |   ID   |   20    |   NS    | False   |   0     |   0     |   0356  |               |               |            |   2.16.9.20   |
|   Conformance Statement ID                |   21    |   ID   |   10    |   NS    | False   |   0     |   0     |   0449  |               |               |            |   2.16.9.21   |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="segment-evn">Segment: EVN </h3></td>
</tr>
<tr class="even">
<td><strong>Description:</strong> Event Type</td>
</tr>
<tr class="odd">
<td><strong>Optionality:</strong> R</td>
</tr>
<tr class="even">
<td><strong>Repeatable:</strong> False</td>
</tr>
<tr class="odd">
<td><strong>Minimum:</strong> 1</td>
</tr>
<tr class="even">
<td><strong>Maximum:</strong> 1</td>
</tr>
<tr class="odd">
<td><strong>Reference:</strong> </td>
</tr>
</tbody>
</table>

Fields

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 1%" />
<col style="width: 3%" />
<col style="width: 9%" />
<col style="width: 27%" />
<col style="width: 6%" />
<col style="width: 9%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><blockquote>
<p><strong>Seq</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Len</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Opt</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Rep</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Min</strong></p>
</blockquote></td>
<td colspan="2"><strong>Max</strong></td>
<td><strong>Tbl</strong></td>
<td><strong>Predicate</strong></td>
<td><strong>Fixed Val</strong></td>
<td><strong>Ex Val</strong></td>
<td><strong>Reference</strong></td>
</tr>
<tr class="even">
<td>  Event Type Code</td>
<td>  1</td>
<td>  ID</td>
<td>  3</td>
<td>  RE</td>
<td>False</td>
<td>  0</td>
<td colspan="2">  1</td>
<td>0003</td>
<td> </td>
<td> </td>
<td> </td>
<td>  3.4.1.1</td>
</tr>
<tr class="odd">
<td colspan="12">HL7 Definition:</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="12">  TIU will not use this field. This field has been retained for backward compatibility only. Use the second component (trigger event) of MSH-9 - Message Type to transmit event type code information.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>  Recorded Date/Time</td>
<td>  2</td>
<td>  TS</td>
<td>  26</td>
<td>NS</td>
<td>False</td>
<td>  0</td>
<td>  0</td>
<td colspan="2"> </td>
<td>   </td>
<td>   </td>
<td>   </td>
<td>  3.4.1.2</td>
</tr>
<tr class="even">
<td>  Date/Time Planned Event</td>
<td>  3</td>
<td>  TS</td>
<td>  26</td>
<td>NS</td>
<td>False</td>
<td>  0</td>
<td>  0</td>
<td colspan="2"> </td>
<td>   </td>
<td>   </td>
<td>   </td>
<td>  3.4.1.3</td>
</tr>
<tr class="odd">
<td>  Event Reason Code</td>
<td>  4</td>
<td>  IS</td>
<td>  0</td>
<td>NS</td>
<td>False</td>
<td>  0</td>
<td>  0</td>
<td colspan="2">0062</td>
<td>   </td>
<td>   </td>
<td>   </td>
<td>  3.4.1.4</td>
</tr>
<tr class="even">
<td>  Operator ID</td>
<td>  5</td>
<td>XCN</td>
<td>  250</td>
<td>NS</td>
<td>False</td>
<td>  0</td>
<td>  0</td>
<td colspan="2">0188</td>
<td>   </td>
<td>   </td>
<td>   </td>
<td>  3.4.1.5</td>
</tr>
<tr class="odd">
<td>  Event Occurred</td>
<td>  6</td>
<td>  TS</td>
<td>  26</td>
<td>NS</td>
<td>False</td>
<td>  0</td>
<td>  0</td>
<td colspan="2"> </td>
<td>   </td>
<td>   </td>
<td>   </td>
<td>  3.4.1.6</td>
</tr>
<tr class="even">
<td>  Event Facility</td>
<td>  7</td>
<td>  HD</td>
<td>180</td>
<td>NS</td>
<td>False</td>
<td>  0</td>
<td>  0</td>
<td colspan="2"> </td>
<td>   </td>
<td>   </td>
<td>   </td>
<td>  3.4.1.7</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="segment-pid">Segment: PID </h3></td>
</tr>
<tr class="even">
<td><strong>Description:</strong> Patient identification</td>
</tr>
<tr class="odd">
<td><strong>Optionality:</strong> R</td>
</tr>
<tr class="even">
<td><strong>Repeatable:</strong> False</td>
</tr>
<tr class="odd">
<td><strong>Minimum:</strong> 1</td>
</tr>
<tr class="even">
<td><strong>Maximum:</strong> 1</td>
</tr>
<tr class="odd">
<td><strong>Reference:</strong> </td>
</tr>
</tbody>
</table>

#### Fields

<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 12%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Name</strong></td>
<td><strong>Seq</strong></td>
<td><strong>DT</strong></td>
<td><strong>Len</strong></td>
<td><strong>Opt</strong></td>
<td><strong>Rep</strong></td>
<td><strong>Min</strong></td>
<td><strong>Max</strong></td>
<td><strong>Tbl</strong></td>
<td><strong>Predicate</strong></td>
<td><strong>Fixed Val</strong></td>
<td><strong>Ex Val</strong></td>
<td><strong>Reference</strong></td>
</tr>
<tr class="even">
<td>  Set ID - PID</td>
<td>  1</td>
<td>  SI</td>
<td>  4</td>
<td>  NS</td>
<td>False</td>
<td>  0</td>
<td>  0</td>
<td> </td>
<td>   </td>
<td>   </td>
<td>   </td>
<td>  3.4.2.1</td>
</tr>
<tr class="odd">
<td>  Patient ID</td>
<td>  2</td>
<td>  CX</td>
<td>  20</td>
<td>  NS</td>
<td>False</td>
<td>  0</td>
<td>  0</td>
<td> </td>
<td>   </td>
<td>   </td>
<td>   </td>
<td>  3.4.2.2</td>
</tr>
<tr class="even">
<td>  Patient Identifier List</td>
<td>  3</td>
<td>  CX</td>
<td>  100</td>
<td>  RE</td>
<td>True</td>
<td>  0</td>
<td>  *</td>
<td> </td>
<td> </td>
<td>   </td>
<td>   </td>
<td>  3.4.2.3</td>
</tr>
<tr class="odd">
<td colspan="11">Implementation Note:</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">  One identifier is the Integration Control Number (ICN). Other possible identifiers present include Vista DFN (IEN), Social Security Number (SSN). VA Claim Number and ICN Alias are not supported.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">HL7 Definition:</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">  ICN - Integration Control Number (ICN) will always be the first number in the list.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>   ID</td>
<td>  1</td>
<td>  ST</td>
<td>  25</td>
<td>  RE</td>
<td> </td>
<td>  0</td>
<td>  1</td>
<td> </td>
<td> </td>
<td> </td>
<td><p>5520020866</p>
<p>V352123</p></td>
<td>  PATIENT file #2, field MPI;1 991.01 INTEGRATION CONTROL NUMBER</td>
</tr>
<tr class="even">
<td colspan="11">Implementation Note:</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">  Cannot be a locally defined MPI number</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="11">HL7 Definition:</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="11">  Master Patient Index INTEGRATION CONTROL (ICN) NUMBER stored in Patient file #2. COTS package should provide the ICN if they have it available.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>   check digit</td>
<td>  2</td>
<td>  ST</td>
<td>  0</td>
<td>  NS</td>
<td> </td>
<td>  0</td>
<td>  0</td>
<td> </td>
<td>   </td>
<td>   </td>
<td>   </td>
<td> </td>
</tr>
<tr class="odd">
<td>   code identifying the check digit scheme employed</td>
<td>  3</td>
<td>  ID</td>
<td>  3</td>
<td>  NS</td>
<td> </td>
<td>  0</td>
<td>  0</td>
<td>  0061</td>
<td>   </td>
<td>   </td>
<td>   </td>
<td> </td>
</tr>
<tr class="even">
<td>   assigning authority</td>
<td>  4</td>
<td>  HD</td>
<td>  30</td>
<td>  RE</td>
<td> </td>
<td>  0</td>
<td>  1</td>
<td>  0363</td>
<td> </td>
<td>   </td>
<td>   </td>
<td> </td>
</tr>
</tbody>
</table>

|                                                                                                                                             |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|-------------|-------------------------------------------------|
| Name                                                                                                                                    | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val  | Reference                                   |
|   ¦nbspnamespace ID                                                                                                                         |   1     |   IS   |   10    | RE      |         |   0     |   1     | 0363    |               |               |   USVHA     |                                                 |
| Implementation Note:                                                                                                                        |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|   User defined table 0363:                                                                                                                  |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|   Patient Identifier Table Value                                                                                                            |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|   -----------------------------------------------------------                                                                               |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|   SSN USSSA                                                                                                                                 |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|   ICN,DFN USVHA - add                                                                                                                       |         |        |         |         |         |         |         |         |               |               |             |                                                 |
| HL7 Definition:                                                                                                                             |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|   USVHA for ICN and DFN                                                                                                                     |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|   ¦nbsp; universal ID                                                                                                                       |   2     |   ST   |   10    |   NS    |         |   0     |   0     |         |               |               |             |                                                 |
|   ¦nbsp; universal ID type (ID)                                                                                                             |   3     |   ID   |   10    |   NS    |         |   0     |   0     |   0301  |               |               |             |                                                 |
|    identifier type code                                                                                                                     |   5     |   ID   |   3     |   RE    |         |   0     |   1     |   0203  |               |               |   NI        |                                                 |
| HL7 Definition:                                                                                                                             |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|   NI = National Unique Individual Identifier for ICN                                                                                        |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|    assigning facility                                                                                                                       |   6     |   HD   |   3     |   NS    |         |   0     |   0     |         |               |               |             |                                                 |
|    effective date                                                                                                                           |   7     |   DT   |   3     |   NS    |         |   0     |   0     |         |               |               |             |                                                 |
|    expiration date                                                                                                                          |   8     |   DT   |   3     |   NS    |         |   0     |   0     |         |               |               |             |                                                 |
|   Patient Identifier List_rep                                                                                                               |   3     |   CX   |   100   |   RE    | False   |   0     |   1     |         |               |               |             |   3.4.2.3                                       |
| HL7 Definition:                                                                                                                             |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|   SSN - Social Security Number. If DFN (IEN to PATIENT file) is not provided, this will be the secondary field used for TIU patient lookup. |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|    ID                                                                                                                                       |   1     |   ST   |   25    |   RE    |         |   0     |   1     |         |               |               |   666242333 |   PATIENT file \#2 - .09 SOCIAL SECURITY NUMBER |
| HL7 Definition:                                                                                                                             |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|   SSN                                                                                                                                       |         |        |         |         |         |         |         |         |               |               |             |                                                 |
|    check digit                                                                                                                              |   2     |   ST   |   0     |   NS    |         |   0     |   0     |         |               |               |             |                                                 |
|    code identifying the check digit scheme employed                                                                                         |   3     |   ID   |   0     |   NS    |         |   0     |   0     |         |               |               |             |                                                 |

|                                                                                                                                                          |         |        |         |         |         |         |         |         |               |               |            |                                    |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|------------------------------------|
| Name                                                                                                                                                 | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference                      |
|    assigning authority                                                                                                                                   |   4     |   HD   |   10    |   RE    |         |   0     |   1     |         |               |               |            |                                    |
|   ¦nbsp; namespace ID                                                                                                                                    |   1     |   IS   |   10    |   RE    |         |   0     |   1     |   0363  |               |               |   USSSA    |                                    |
|   ¦nbsp; universal ID                                                                                                                                    |   2     |   ST   |   0     |   NS    |         |   0     |   0     |         |               |               |            |                                    |
|   ¦nbsp; universal ID type (ID)                                                                                                                          |   3     |   ID   |   0     |   NS    |         |   0     |   0     |         |               |               |            |                                    |
|    identifier type code                                                                                                                                  |   5     |   ID   |   3     |   RE    |         |   0     |   1     |   0203  |               |               |   SS       |                                    |
|    assigning facility                                                                                                                                    |   6     |   HD   |   3     |   NS    |         |   0     |   0     |         |               |               |            |                                    |
|    effective date                                                                                                                                        |   7     |   DT   |   0     |   NS    |         |   0     |   0     |         |               |               |            |                                    |
|    expiration date                                                                                                                                       |   8     |   DT   |   0     |   NS    |         |   0     |   0     |         |               |               |            |                                    |
|   Patient Identifier List_rep                                                                                                                            |   3     |   CX   |   100   |   RE    | False   |   0     |   1     |         |               |               |            |   3.4.2.3                          |
| HL7 Definition:                                                                                                                                          |         |        |         |         |         |         |         |         |               |               |            |                                    |
|   DFN is the Internal Entry Number (IEN) for PATIENT file \#2. Pointer to PATIENT file \#2 will be stored in TIU DOCUMENT file \#8925, field .02 PATIENT |         |        |         |         |         |         |         |         |               |               |            |                                    |
|    ID                                                                                                                                                    |   1     |   ST   |   25    |   RE    |         |   0     |   1     |         |               |               |   129909   |   PATIENT file \#2, field .001 IEN |
| HL7 Definition:                                                                                                                                          |         |        |         |         |         |         |         |         |               |               |            |                                    |
|   DFN - aka IEN, Internal Entry Number                                                                                                                   |         |        |         |         |         |         |         |         |               |               |            |                                    |
|    check digit                                                                                                                                           |   2     |   ST   |   0     |   NS    |         |   0     |   0     |         |               |               |            |                                    |
|    code identifying the check digit scheme employed                                                                                                      |   3     |   ID   |   0     |   NS    |         |   0     |   0     |         |               |               |            |                                    |
|    assigning authority                                                                                                                                   |   4     |   HD   |   10    |   RE    |         |   0     |   1     |         |               |               |            |                                    |
|   ¦nbsp; namespace ID                                                                                                                                    |   1     |   IS   |   10    |   RE    |         |   0     |   1     |   0363  |               |               |   USVHA    |                                    |
| HL7 Definition:                                                                                                                                          |         |        |         |         |         |         |         |         |               |               |            |                                    |
|   VHA is the authority that assigned the IEN to the patient                                                                                              |         |        |         |         |         |         |         |         |               |               |            |                                    |
|   ¦nbsp; universal ID                                                                                                                                    |   2     |   ST   |   0     |   NS    |         |   0     |   0     |         |               |               |            |                                    |

|                                                                                                                                                  |         |        |         |         |         |         |         |         |               |               |            |                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|------------------------------------|
| Name                                                                                                                                         | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference                      |
|   ¦nbsp; universal ID type (ID)                                                                                                                  |   3     |   ID   |   0     | NS      |         |   0     |   0     |         |               |               |            |                                    |
|    identifier type code                                                                                                                          |   5     |   ID   |   10    | RE      |         |   0     |   1     | 0203    |               |               |   PI       |                                    |
| HL7 Definition:                                                                                                                                  |         |        |         |         |         |         |         |         |               |               |            |                                    |
|   Patient Internal Identifier - PI                                                                                                               |         |        |         |         |         |         |         |         |               |               |            |                                    |
|    assigning facility                                                                                                                            |   6     |   HD   |   3     | NS      |         |   0     |   0     |         |               |               |            |                                    |
|    effective date                                                                                                                                |   7     |   DT   |   0     | NS      |         |   0     |   0     |         |               |               |            |                                    |
|    expiration date                                                                                                                               |   8     |   DT   |   0     | NS      |         |   0     |   0     |         |               |               |            |                                    |
|   Patient Identifier List_rep                                                                                                                    |   3     |   CX   |   0     | NS      | False   |   0     |   0     |         |               |               |            |   3.4.2.3                          |
|   Patient Identifier List_rep                                                                                                                    |   3     |   CX   |   0     | NS      | False   |   0     |   0     |         |               |               |            |   3.4.2.3                          |
|   Alternate Patient ID - PID                                                                                                                     |   4     |   CX   |   20    | NS      | False   |   0     |   0     |         |               |               |            |   3.4.2.4                          |
|   Patient Name                                                                                                                                   |   5     | XPN    | 250     |   R     | True    |   1     |   \*    |         |               |               |            |   PATIENT file \#2, field .01 NAME |
| HL7 Definition:                                                                                                                                  |         |        |         |         |         |         |         |         |               |               |            |                                    |
|   Legal \[VHA Standard\] (2; .01) VistA format is LASTNAME, FIRSTNAME MIDDLE; VistA software will format VistA name from HL7 name, if necessary. |         |        |         |         |         |         |         |         |               |               |            |                                    |
|    family name                                                                                                                                   |   1     |   FN   |   35    |   R     |         |   1     |   1     |         |               |               |            |                                    |
|   ¦nbsp; surname                                                                                                                                 |   1     |   ST   |   35    |   R     |         |   1     |   1     |         |               |               | TIUPATIENT |                                    |
|   ¦nbsp; own surname prefix                                                                                                                      |   2     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |            |                                    |
|   ¦nbsp; own surname                                                                                                                             |   3     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |            |                                    |
|   ¦nbsp; surname prefix from partner/spouse                                                                                                      |   4     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |            |                                    |
|   ¦nbsp; surname from partner/spouse                                                                                                             |   5     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |            |                                    |
|    given name                                                                                                                                    |   2     |   ST   |   30    |   R     |         |   1     |   1     |         |               |               |   ONE      |                                    |

|                                                       |         |        |         |         |         |         |         |         |               |               |            |               |
|-------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|---------------|
| Name                                              | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference |
|    second and further given names or initials thereof |   3     |   ST   |   30    | RE      |         |   0     |   1     |         |               |               |   R        |               |
|    suffix                                             |   4     |   ST   |   3     |   NS    |         |   0     |   0     |         |               |               |            |               |
|    prefix                                             |   5     |   ST   |   3     |   NS    |         |   0     |   0     |         |               |               |            |               |
|    degree                                             |   6     |   ST   |   3     |   NS    |         |   0     |   0     |   0360  |               |               |            |               |
|    name type code                                     |   7     |   ID   |   3     |   NS    |         |   0     |   0     |   0200  |               |               |            |               |
|    name representation code                           |   8     |   ID   |   3     |   NS    |         |   0     |   0     |   0465  |               |               |            |               |
|    name context                                       |   9     |   CE   |   0     |   NS    |         |   0     |   0     |         |               |               |            |               |
|    name validity range                                |   10    |   DR   |   3     |   NS    |         |   0     |   0     |         |               |               |            |               |
|    name assembly order                                |   11    |   ID   |   3     |   NS    |         |   0     |   0     |   0444  |               |               |            |               |
|   Patient Name_rep                                    |   5     |   XPN  |   3     |   NS    | False   |   0     |   0     |         |               |               |            |               |
|   Patient Name_rep                                    |   5     |   XPN  |   3     |   NS    | False   |   0     |   0     |         |               |               |            |               |
|   Patient Name_rep                                    |   5     |   XPN  |   3     |   NS    | False   |   0     |   0     |         |               |               |            |               |
|   Mother's Maiden Name                                |   6     |   XPN  |   3     |   NS    | False   |   0     |   0     |         |               |               |            |   6.5.7.40    |
|   Date/Time of Birth                                  |   7     |   TS   |   26    |   NS    | False   |   0     |   0     |         |               |               |            |   15.4.6.6    |
|   Administrative Sex                                  |   8     |   IS   |   1     |   NS    | False   |   0     |   0     |   0001  |               |               |            |   15.4.6.5    |
|   Patient Alias                                       |   9     |   XPN  |   250   |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.9     |
|   Race                                                |   10    |   CE   |   250   |   NS    | False   |   0     |   0     |   0005  |               |               |            |   15.4.6.27   |
|   Patient Address                                     |   11    |   XAD  |   250   |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.11    |
|   Phone Number - Home                                 |   12    |   XTN  |   3     |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.13    |
|   Phone Number - Business                             |   13    |   XTN  |   3     |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.14    |

|                                   |         |        |         |         |         |         |         |         |               |               |            |               |
|-----------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|---------------|
| Name                          | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference |
|   Primary Language                |   14    |   CE   |   250   |   NS    | False   |   0     |   0     |   0296  |               |               |            |   6.5.7.34    |
|   Marital Status                  |   15    |   CE   |   3     |   NS    | False   |   0     |   0     |   0002  |               |               |            |   15.4.6.17   |
|   Religion                        |   16    |   CE   |   3     |   NS    | False   |   0     |   0     |   0006  |               |               |            |   6.5.7.39    |
|   Patient Account Number          |   17    |   CX   |   250   |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.18    |
|   SSN Number - Patient            |   18    |   ST   |   16    |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.19    |
|   Driver's License Number-Patient |   19    |   DLN  |   25    |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.20    |
|   Mother's Identifier             |   20    |   CX   |   250   |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.21    |
|   Ethnic Group                    |   21    |   CE   |   3     |   NS    | False   |   0     |   0     |   0189  |               |               |            |   15.4.6.28   |
|   Birth Place                     |   22    |   ST   |   250   |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.23    |
|   Multiple Birth Indicator        |   23    |   ID   |   250   |   NS    | False   |   0     |   0     |   0136  |               |               |            |   3.4.2.24    |
|   Birth Order                     |   24    |   NM   |   2     |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.25    |
|   Citizenship                     |   25    |   CE   |   250   |   NS    | False   |   0     |   0     |   0172  |               |               |            |   6.5.7.33    |
|   Veterans Military Status        |   26    |   CE   |   250   |   NS    | False   |   0     |   0     |   0172  |               |               |            |   3.4.2.27    |
|   Nationality                     |   27    |   CE   |   250   |   NS    | False   |   0     |   0     |   0212  |               |               |            |   6.5.7.41    |
|   Patient Death Date and Time     |   28    |   TS   |   3     |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.29    |
|   Patient Death Indicator         |   29    |   ID   |   3     |   NS    | False   |   0     |   0     |   0136  |               |               |            |   3.4.2.30    |
|   Identity Unknown Indicator      |   30    |   ID   |   3     |   NS    | False   |   0     |   0     |   0136  |               |               |            |   3.4.2.31    |
|   Identity Reliability Code       |   31    |   IS   |   3     |   NS    | False   |   0     |   0     |   0445  |               |               |            |   3.4.2.32    |
|   Last Update Date/Time           |   32    |   TS   |   3     |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.33    |
|   Last Update Facility            |   33    |   HD   |   3     |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.34    |

|                         |         |        |         |         |         |         |         |         |               |               |            |               |
|-------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|---------------|
| Name                | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference |
|   Species Code          |   34    |   CE   |   3     |   NS    | False   |   0     |   0     |   0446  |               |               |            |   3.4.2.35    |
|   Breed Code            |   35    |   CE   |   3     |   NS    | False   |   0     |   0     |   0447  |               |               |            |   3.4.2.36    |
|   Strain                |   36    |   ST   |   3     |   NS    | False   |   0     |   0     |         |               |               |            |   3.4.2.37    |
|   Production Class Code |   37    |   CE   |   3     |   NS    | False   |   0     |   0     |   0429  |               |               |            |   3.4.2.38    |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="segment-pv1">Segment: PV1 </h3></td>
</tr>
<tr class="even">
<td><strong>Description:</strong> Patient visit</td>
</tr>
<tr class="odd">
<td><strong>Optionality:</strong> R</td>
</tr>
<tr class="even">
<td><strong>Repeatable:</strong> False</td>
</tr>
<tr class="odd">
<td><strong>Minimum:</strong> 1</td>
</tr>
<tr class="even">
<td><strong>Maximum:</strong> 1</td>
</tr>
<tr class="odd">
<td><strong>Reference:</strong> </td>
</tr>
</tbody>
</table>

#### Fields

|                                                                                  |         |        |         |         |         |         |         |         |                                                                                                                                                                                    |               |            |     |     |               |
|----------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|------------|-----|-----|---------------|
| Name                                                                         | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate                                                                                                                                                                      | Fixed Val | Ex Val |     |     | Reference |
|   Set ID - PV1                                                                   |   1     |   SI   |   4     | NS      | False   |   0     |   0     |         |                                                                                                                                                                                    |               |            |     |     |   3.4.3.1     |
|   Patient Class                                                                  |   2     |   IS   |   1     | NS      | False   |   0     |   0     | 0004    |                                                                                                                                                                                    |               |            |     |     |   3.4.3.2     |
|   Assigned Patient Location                                                      |   3     |   PL   |   80    |   C     | False   |   0     |   1     |  B      |   For Progress Notes: a new HISTORICAL visit will be created, otherwise a NEW VISIT will be created. - HOSPITAL LOCATION is required for new, NON- HISTORICAL vists (will reject). |               |            |     |     |   6.5.1.16    |
| Implementation Note:                                                             |         |        |         |         |         |         |         |         |                                                                                                                                                                                    |               |            |     |     |               |
|   For Progress Notes:                                                            |         |        |         |         |         |         |         |         |                                                                                                                                                                                    |               |            |     |     |               |
|   a new HISTORICAL visit will be created, otherwise a NEW VISIT will be created. |         |        |         |         |         |         |         |         |                                                                                                                                                                                    |               |            |     |     |               |
|   - HOSPITAL LOCATION is required for new, NON-HISTORICAL vists (will reject).   |         |        |         |         |         |         |         |         |                                                                                                                                                                                    |               |            |     |     |               |

|                                               |         |        |         |         |         |         |         |         |                                                                                                                                                                                  |               |                  |                           |
|-----------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|------------------|---------------------------|
| Name                                      | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate                                                                                                                                                                    | Fixed Val | Ex Val       | Reference             |
|    point of care                              |   1     |   IS   |   30    |   C     |         |   0     |   1     | 0302    | For Progress Notes: a new HISTORICAL visit will be created, otherwise a NEW VISIT will be created. - HOSPITAL LOCATION is required for new, NON- HISTORICAL vists (will reject). |               | EXAMPLE LOCATION | 44; .01 NAME (0;1) \[RF\] |
| Implementation Note:                          |         |        |         |         |         |         |         |         |                                                                                                                                                                                  |               |                  |                           |
|   Only the first component, point of care, is |         |        |         |         |         |         |         |         |                                                                                                                                                                                  |               |                  |                           |
|   supported as the free text name of the      |         |        |         |         |         |         |         |         |                                                                                                                                                                                  |               |                  |                           |
|   HOSPTIAL LOCATION (file \# 44). Do not      |         |        |         |         |         |         |         |         |                                                                                                                                                                                  |               |                  |                           |
|   add any component separators.               |         |        |         |         |         |         |         |         |                                                                                                                                                                                  |               |                  |                           |
|    room                                       |   2     |   IS   |   3     |   NS    |         |   0     |   0     |   0303  |                                                                                                                                                                                  |               |                  |                           |
|    bed                                        |   3     |   IS   |   3     |   NS    |         |   0     |   0     |   0304  |                                                                                                                                                                                  |               |                  |                           |
|    facility (HD)                              |   4     |   HD   |   3     |   NS    |         |   0     |   0     |         |                                                                                                                                                                                  |               |                  |                           |
|    location status                            |   5     |   IS   |   3     |   NS    |         |   0     |   0     |   0306  |                                                                                                                                                                                  |               |                  |                           |
|    person location type                       |   6     |   IS   |   3     |   NS    |         |   0     |   0     |   0305  |                                                                                                                                                                                  |               |                  |                           |
|    building                                   |   7     |   IS   |   3     |   NS    |         |   0     |   0     |   0307  |                                                                                                                                                                                  |               |                  |                           |
|    floor                                      |   8     |   IS   |   3     |   NS    |         |   0     |   0     |   0308  |                                                                                                                                                                                  |               |                  |                           |
|    Location description                       |   9     |   ST   |   3     |   NS    |         |   0     |   0     |         |                                                                                                                                                                                  |               |                  |                           |

|                                                                                                                                                                                                                                                                                                                                                                                                             |         |      |        |       |         |      |         |      |         |         |     |         |        |         |     |               |     |               |     |            |            |               |     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|------|--------|-------|---------|------|---------|------|---------|---------|-----|---------|--------|---------|-----|---------------|-----|---------------|-----|------------|------------|---------------|-----|
| Name                                                                                                                                                                                                                                                                                                                                                                                                    | Seq |      | DT |       | Len |      | Opt |      | Rep | Min |     | Max |        | Tbl |     | Predicate |     | Fixed Val |     | Ex Val |            | Reference |     |
|  Admission Type                                                                                                                                                                                                                                                                                                                                                                                             |         |   4  |        |   IS  |         |   2  |         | NS   | False   |         |   0 |   0     |   0007 |         |     |               |     |               |     |            |   3.4.3.4  |               |     |
|   Preadmit Number                                                                                                                                                                                                                                                                                                                                                                                           |         |   5  |        |   CX  |         | 250  |         | NS   | False   |         |   0 |   0     |        |         |     |               |     |               |     |            |   3.4.3.5  |               |     |
|   Prior Patient Location                                                                                                                                                                                                                                                                                                                                                                                    |         |   6  |        |   PL  |         |   3  |         | NS   | False   |         |   0 |   0     |        |         |     |               |     |               |     |            |   3.4.3.6  |               |     |
|   Attending Doctor                                                                                                                                                                                                                                                                                                                                                                                          |         |   7  |        |   XCN |         | 250  |         | NS   | False   |         |   0 |   0     | 0010   |         |     |               |     |               |     |            |   3.4.3.7  |               |     |
|   Referring Doctor                                                                                                                                                                                                                                                                                                                                                                                          |         |   8  |        |   XCN |         | 250  |         | NS   | False   |         |   0 |   0     | 0010   |         |     |               |     |               |     |            |   3.4.3.8  |               |     |
|  Consulting Doctor                                                                                                                                                                                                                                                                                                                                                                                          |         |   9  |        |   XCN |         | 250  |         | NS   | False   |         |   0 |   0     | 0010   |         |     |               |     |               |     |            |   3.4.3.9  |               |     |
|   Hospital Service                                                                                                                                                                                                                                                                                                                                                                                          |         | 10   |        |   IS  |         |   10 |         | NS   | False   |         |   0 |   0     |   0069 |         |     |               |     |               |     |            |   3.4.3.10 |               |     |
|   Temporary Location                                                                                                                                                                                                                                                                                                                                                                                        |         | 11   |        |   PL  |         |   80 |         | NS   | False   |         |   0 |   0     |        |         |     |               |     |               |     |            |   3.4.3.11 |               |     |
|   Preadmit Test Indicator                                                                                                                                                                                                                                                                                                                                                                                   |         | 12   |        |   IS  |         |   2  |         | NS   | False   |         |   0 |   0     | 0087   |         |     |               |     |               |     |            |   3.4.3.12 |               |     |
|   Re-admission Indicator                                                                                                                                                                                                                                                                                                                                                                                    |         | 13   |        |   IS  |         |   2  |         | NS   | False   |         |   0 |   0     | 0092   |         |     |               |     |               |     |            |   3.4.3.13 |               |     |
|   Admit Source                                                                                                                                                                                                                                                                                                                                                                                              |         | 14   |        |   IS  |         |   6  |         |   NS | False   |         |   0 |   0     |   0023 |         |     |               |     |               |     |            |   3.4.3.14 |               |     |
| Ambulatory Status                                                                                                                                                                                                                                                                                                                                                                                           |         |   15 |        |   IS  |         |   2  |         | NS   | False   |         |   0 |   0     | 0009   |         |     |               |     |               |     |            |   6.5.7.32 |               |     |
|   VIP Indicator                                                                                                                                                                                                                                                                                                                                                                                             |         |   16 |        |   IS  |         |   2  |         | NS   | False   |         |   0 |   0     | 0099   |         |     |               |     |               |     |            |   3.4.3.16 |               |     |
|   Admitting Doctor                                                                                                                                                                                                                                                                                                                                                                                          |         |   17 |        |   XCN |         | 250  |         | NS   | False   |         |   0 |   0     | 0010   |         |     |               |     |               |     |            |   3.4.3.17 |               |     |
|   Patient Type                                                                                                                                                                                                                                                                                                                                                                                              |         | 18   |        |   IS  |         |   2  |         | NS   | False   |         |   0 |   0     | 0018   |         |     |               |     |               |     |            |   6.5.1.18 |               |     |
|   Visit Number                                                                                                                                                                                                                                                                                                                                                                                              |         | 19   |        |   CX  |         | 250  |         | RE   | False   |         |   0 |   1     |        |         |     |               |     |               |     |            |   3.4.3.19 |               |     |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                                                             |         |      |        |       |         |      |         |      |         |         |     |         |        |         |     |               |     |               |     |            |            |               |     |
|   Progress Note: Used when creating a TIU Progress Note. DFN (IEN) that identifies a unique visit in VistA VISIT file \#9000010. Progress notes must be linked to a visit. If this field is populated, TIU will use it to locate the patient visit in VistA. If this field is blank or TIU cannot find a visit to match the content of this field, TIU will use PV1.44 Admit Date/Time to locate the visit. |         |      |        |       |         |      |         |      |         |         |     |         |        |         |     |               |     |               |     |            |            |               |     |
|   If no patient visit is located, TIU will check TXA.19 Document Availability Status to see if the document should be created: AV=Available, i.e. create a new document using NOW for the visit date and time; CA=Cancel, i.e. reject the HL7 message and do not create the document.                                                                                                                       |         |      |        |       |         |      |         |      |         |         |     |         |        |         |     |               |     |               |     |            |            |               |     |

|                                                                                                                    |         |        |         |         |         |         |         |         |               |               |            |                                      |
|--------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|--------------------------------------|
| Name                                                                                                           | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference                        |
|    ID                                                                                                              |   1     |   ST   |   30    |  RE     |         |   0     |   1     |         |               |               |   1900     | VISIT file \#9000010, field .001 IEN |
| HL7 Definition:                                                                                                    |         |        |         |         |         |         |         |         |               |               |            |                                      |
|   Contains the DFN/IEN to VISIT file \#9000010, which will be stored in TIU DOCUMENT file \#8925, field .03 VISIT. |         |        |         |         |         |         |         |         |               |               |            |                                      |
|    Check digit                                                                                                     |   2     |   ST   |   0     |   NS    |         |   0     |   0     |         |               |               |            |                                      |
|    code identifying the check digit scheme employed                                                                |   3     |   ID   |   3     |   NS    |         |   0     |   0     |   0061  |               |               |            |                                      |
|    assigning authority                                                                                             |   4     |   HD   |   3     |   NS    |         |   0     |   0     |         |               |               |            |                                      |
|    identifier type code (ID)                                                                                       |   5     |   ID   |   3     |   NS    |         |   0     |   0     |   0203  |               |               |            |                                      |
|    assigning facility                                                                                              |   6     |   HD   |   3     |   NS    |         |   0     |   0     |         |               |               |            |                                      |
|    effective date (DT)                                                                                             |   7     |   DT   |   3     |   NS    |         |   0     |   0     |         |               |               |            |                                      |
|    expiration date                                                                                                 |   8     |   DT   |   3     |   NS    |         |   0     |   0     |         |               |               |            |                                      |
|   Financial Class                                                                                                  |   20    |   FC   |   50    |   NS    | False   |   0     |   0     |   0064  |               |               |            |   3.4.3.20                           |
|   Charge Price Indicator                                                                                           |   21    |   IS   |   2     |   NS    | False   |   0     |   0     |   0032  |               |               |            |   3.4.3.21                           |
|   Courtesy Code                                                                                                    |   22    |   IS   |   2     |   NS    | False   |   0     |   0     |   0045  |               |               |            |   3.4.3.22                           |
|   Credit Rating                                                                                                    |   23    |   IS   |   2     |   NS    | False   |   0     |   0     |   0046  |               |               |            |   3.4.3.23                           |
|   Contract Code                                                                                                    |   24    |   IS   |   2     |   NS    | False   |   0     |   0     |   0044  |               |               |            |   3.4.3.24                           |

|                             |         |        |         |         |         |         |         |         |               |               |            |               |
|-----------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|---------------|
| Name                    | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference |
|   Contract Effective Date   | 25      |   DT   |   8     | NS      | False   |   0     |   0     |         |               |               |            |   3.4.3.25    |
|   Contract Amount           | 26      |   NM   |   12    | NS      | False   |   0     |   0     |         |               |               |            |   3.4.3.26    |
|   Contract Period           | 27      |   NM   |   3     | NS      | False   |   0     |   0     |         |               |               |            |   3.4.3.27    |
|   Interest Code             | 28      |   IS   |   2     | NS      | False   |   0     |   0     | 0073    |               |               |            |   3.4.3.28    |
|   Transfer to Bad Debt Code | 29      |   IS   |   1     | NS      | False   |   0     |   0     | 0110    |               |               |            |   3.4.3.29    |
|   Transfer to Bad Debt Date | 30      |   DT   |   8     | NS      | False   |   0     |   0     |         |               |               |            |   3.4.3.30    |
|   Bad Debt Agency Code      | 31      |   IS   |   10    | NS      | False   |   0     |   0     | 0021    |               |               |            |   3.4.3.31    |
|   Bad Debt Transfer Amount  | 32      |   NM   |   12    | NS      | False   |   0     |   0     |         |               |               |            |   3.4.3.32    |
|   Bad Debt Recovery Amount  | 33      |   NM   |   12    | NS      | False   |   0     |   0     |         |               |               |            |   3.4.3.33    |
|   Delete Account Indicator  | 34      |   IS   |   1     | NS      | False   |   0     |   0     | 0111    |               |               |            |   3.4.3.34    |
|   Delete Account Date       | 35      |   DT   |   8     | NS      | False   |   0     |   0     |         |               |               |            |   3.4.3.35    |
|   Discharge Disposition     | 36      |   IS   |   3     | NS      | False   |   0     |   0     | 0112    |               |               |            |   3.4.3.36    |
|   Discharged to Location    | 37      | CM_DLD |   25    | NS      | False   |   0     |   0     |   0113  |               |               |            |   3.4.3.37    |
|   Diet Type                 | 38      |   CE   | 250     | NS      | False   |   0     |   0     | 0114    |               |               |            |   3.4.3.38    |
|   Servicing Facility        | 39      |   IS   |   10    | NS      | False   |   0     |   0     | 0115    |               |               |            |   3.4.3.39    |
|   Bed Status                | 40      |   IS   |   1     | NS      | False   |   0     |   0     | 0116    |               |               |            |   3.4.8.2     |
|   Account Status            |   41    |   IS   |   2     | NS      | False   |   0     |   0     | 0117    |               |               |            |   3.4.3.41    |
|   Pending Location          |   42    |   PL   |   80    | NS      | False   |   0     |   0     |         |               |               |            |   3.4.3.42    |

|                                                                                                                                                                                                                                                                                                         |         |        |         |         |         |         |         |         |               |               |                |                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|----------------|---------------------------------------------------------|
| Name                                                                                                                                                                                                                                                                                                | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val     | Reference                                           |
|   Prior Temporary Location                                                                                                                                                                                                                                                                              | 43      |   PL   | 80      | NS      | False   |   0     |   0     |         |               |               |                |   3.4.3.43                                              |
|   Admit Date/Time                                                                                                                                                                                                                                                                                       | 44      |   TS   | 26      | RE      | False   |   0     |   1     |         |               |               |                |   3.4.3.44                                              |
| HL7 Definition:                                                                                                                                                                                                                                                                                         |         |        |         |         |         |         |         |         |               |               |                |                                                         |
|   Represents an inpatient admission or an outpatient visit.                                                                                                                                                                                                                                             |         |        |         |         |         |         |         |         |               |               |                |                                                         |
|   Discharge Summary: Required when creating a TIU Discharge Summary document; used to identify the admission associated with the discharge.                                                                                                                                                             |         |        |         |         |         |         |         |         |               |               |                |                                                         |
|   Progress note: Used to find an existing visit if TIU cannot find one using PV1.19 Visit Number.                                                                                                                                                                                                       |         |        |         |         |         |         |         |         |               |               |                |                                                         |
|    Date/Time                                                                                                                                                                                                                                                                                            |   1     |   NM   |   14    |   RE    |         |   0     |   1     |         |               |               |   200501200814 |   VISIT file \#9000010, field .01 VISIT/ADMIT DATE&TIME |
| HL7 Definition:                                                                                                                                                                                                                                                                                         |         |        |         |         |         |         |         |         |               |               |                |                                                         |
|   Admission date will be used to locate a visit if the IEN to the VISIT file is not provided. If the visit is located, the date/time will be stored in TIU DOCUMENT file \#8925, field .07 EPISODE BEGIN DATE/TIME. If this field is blank, a new historical visit could be created using today's date. |         |        |         |         |         |         |         |         |               |               |                |                                                         |
|    degree of precision                                                                                                                                                                                                                                                                                  |   2     |   ST   |   0     |   NS    |         |   0     |   0     |         |               |               |                |                                                         |
|   Discharge Date/Time                                                                                                                                                                                                                                                                                   |   45    |   TS   |   26    |   NS    | False   |   0     |   0     |         |               |               |                |   3.4.3.45                                              |
|   Current Patient Balance                                                                                                                                                                                                                                                                               |   46    |   NM   |   12    |   NS    | False   |   0     |   0     |         |               |               |                |   3.4.3.46                                              |
|   Total Charges                                                                                                                                                                                                                                                                                         |   47    |   NM   |   12    |   NS    | False   |   0     |   0     |         |               |               |                |   3.4.3.47                                              |
|   Total Adjustments                                                                                                                                                                                                                                                                                     |   48    |   NM   |   12    |   NS    | False   |   0     |   0     |         |               |               |                |   3.4.3.48                                              |
|   Total Payments                                                                                                                                                                                                                                                                                        |   49    |   NM   |   12    |   NS    | False   |   0     |   0     |         |               |               |                |   3.4.3.49                                              |
|   Alternate Visit ID                                                                                                                                                                                                                                                                                    |   50    |   CX   |   250   |   NS    | False   |   0     |   0     |   0203  |               |               |                |   3.4.3.50                                              |
|   Visit Indicator                                                                                                                                                                                                                                                                                       |   51    |   IS   |   1     |   NS    | False   |   0     |   0     |   0326  |               |               |                |   3.4.3.51                                              |
|   Other Healthcare Provider                                                                                                                                                                                                                                                                             |   52    |   XCN  |   250   |   NS    | False   |   0     |   0     |   0010  |               |               |                |   3.4.3.52                                              |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="segment-txa"><strong>Segment</strong>: TXA </h3></td>
</tr>
<tr class="even">
<td><strong>Description:</strong> Transcription Document Header</td>
</tr>
<tr class="odd">
<td><strong>Optionality:</strong> R</td>
</tr>
<tr class="even">
<td><strong>Repeatable:</strong> False</td>
</tr>
<tr class="odd">
<td><strong>Minimum:</strong> 1</td>
</tr>
<tr class="even">
<td><strong>Maximum:</strong> 1</td>
</tr>
<tr class="odd">
<td><strong>Reference:</strong> 9.6.1</td>
</tr>
</tbody>
</table>

#### Fields

|                                                                                                                                                                                                                                                                                                                                                 |         |        |         |         |         |         |         |         |               |               |                |               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|----------------|---------------|
| Name                                                                                                                                                                                                                                                                                                                                        | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val     | Reference |
|   Set ID- TXA                                                                                                                                                                                                                                                                                                                                   |   1     |   SI   |   4     |   NS    | False   |   0     |   0     |         |               |               |                |   9.6.1.1     |
|   Document Type                                                                                                                                                                                                                                                                                                                                 |   2     |   IS   |   2     |   NS    | False   |   0     |   0     |   0270  |               |               |                |   9.6.1.2     |
|   Document Content Presentation                                                                                                                                                                                                                                                                                                                 |   3     |   ID   |   4     |   R     | False   |   1     |   1     |  0191   |               |               |   TEXT         |   9.6.1.3     |
|   Activity Date/Time                                                                                                                                                                                                                                                                                                                            |   4     |   TS   |   26    |   R     | False   |   1     |   1     |         |               |               |                |   9.6.1.4     |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                 |         |        |         |         |         |         |         |         |               |               |                |               |
|   Required for all documents. Will be used as the Reference date in TIU and will be the date by which the documents will be referenced and sorted. For new documents, this date will be stored in TIU DOCUMENT file \#8925, field 1301 REFERENCE DATE.                                                                                          |         |        |         |         |         |         |         |         |               |               |                |               |
|   Discharge Summary: date of admission. (same date as PV1.44 Admit date/time)                                                                                                                                                                                                                                                                   |         |        |         |         |         |         |         |         |               |               |                |               |
|   Consult Note: date of the consult or the date patient data was added to the vendor system                                                                                                                                                                                                                                                     |         |        |         |         |         |         |         |         |               |               |                |               |
|   Progress Note: date of the visit or date that will be used as Reference data when creating historical visit                                                                                                                                                                                                                                   |         |        |         |         |         |         |         |         |               |               |                |               |
|   Surgery Report: date of the surgery. This date will be used to locate a Surgery document if the surgery case number is not in this HL7 message. If more than one surgery took place on this date, TIU will not be able to tell which case to update, so the HL7 record will be rejected and must be resubmitted with the surgery case number. |         |        |         |         |         |         |         |         |               |               |                |               |
|    Date/Time                                                                                                                                                                                                                                                                                                                                    |   1     |   NM   |   14    |   R     |         |   1     |   1     |         |               |               |   200501281130 |               |
| Implementation Note:                                                                                                                                                                                                                                                                                                                            |         |        |         |         |         |         |         |         |               |               |                |               |
|   YYYYMMDD\[HHHMM\[SS\[.SSSS\]\]\]\[+-ZZZZ\]                                                                                                                                                                                                                                                                                                    |         |        |         |         |         |         |         |         |               |               |                |               |
|    degree of precision                                                                                                                                                                                                                                                                                                                          |   2     |   ST   |   0     |   NS    |         |   0     |   0     |         |               |               |                |               |

|                                                                                                                                                                                                                                                                                                                                                                 |         |        |         |         |         |         |         |         |               |               |                |                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|----------------|------------------------------------------|
| Name                                                                                                                                                                                                                                                                                                                                                        | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val     | Reference                            |
|   Primary Activity Provider Code/Name                                                                                                                                                                                                                                                                                                                           |   5     | XCN    | 250     | NS      | False   |   0     |   0     |         |               |               |                |   9.6.1.5                                |
|   Origination Date/Time                                                                                                                                                                                                                                                                                                                                         |   6     |   TS   |   0     | NS      | False   |   0     |   0     |         |               |               |                |                                          |
|  Transcription Date/Time                                                                                                                                                                                                                                                                                                                                        |   7     |   TS   |   26    | RE      | False   |   0     |   1     |         |               |               |                |   9.6.1.7                                |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                 |         |        |         |         |         |         |         |         |               |               |                |                                          |
|   This field is required if the the document was transcribed. This field will not be stored in TIU.                                                                                                                                                                                                                                                             |         |        |         |         |         |         |         |         |               |               |                |                                          |
|    Date/Time                                                                                                                                                                                                                                                                                                                                                    |   1     |   NM   |   26    | RE      |         |   0     |   1     |         |               |               |   200602281530 |   8925; 1307 DICTATION DATE (13;7) \[D\] |
| Implementation Note:                                                                                                                                                                                                                                                                                                                                            |         |        |         |         |         |         |         |         |               |               |                |                                          |
|   YYYYMMDD\[HHHMM\[SS\[.SSSS\]\]\]\[+-ZZZZ\]                                                                                                                                                                                                                                                                                                                    |         |        |         |         |         |         |         |         |               |               |                |                                          |
|    degree of precision                                                                                                                                                                                                                                                                                                                                          |   2     |   ST   |   0     | NS      |         |   0     |   0     |         |               |               |                |                                          |
|   Edit Date/Time                                                                                                                                                                                                                                                                                                                                                |   8     |   TS   |   0     | NS      | False   |   0     |   0     |         |               |               |                |   9.6.1.8                                |
|   Originator Code/Name                                                                                                                                                                                                                                                                                                                                          |   9     | XCN    | 250     |   R     | False   |   1     |   1     |         |               |               |                |   9.6.1.9                                |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                 |         |        |         |         |         |         |         |         |               |               |                |                                          |
|   Author & expected signer. This field identifies the person who originated (i.e., dictated) the document and is expected to enter the first-line signature for the document. TIU will use this field to populate two fields in TIU DOCUMENT file \#8925: field 1202 AUTHOR/DICTATOR; field 1204 EXPECTED SIGNER                                                |         |        |         |         |         |         |         |         |               |               |                |                                          |
|   If the Document Completion Status is LA/Legally Authenticated, TIU will check for a date in the signer field TXA.22.15.1 Authentication Person, Time Stamp. If the date is there, TIU will use the signature block information for this person to apply an electronic signature to this note for EXPECTED SIGNER. The date of signature in VistA will be NOW. |         |        |         |         |         |         |         |         |               |               |                |                                          |
|    ID number (ST)                                                                                                                                                                                                                                                                                                                                               |   1     |   ST   |   30    |   R     |         |   1     |   1     |         |               |               |   33234        | NEW PERSON file \#200, field .001 IEN    |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                 |         |        |         |         |         |         |         |         |               |               |                |                                          |
|   SSN or DUZ of a person in VistA NEW PERSON file \#200. Must have value in TXA 9.9.1 Originator Code/name namespace to determine which number: USVHA for DUZ; USSSA for SSN                                                                                                                                                                                    |         |        |         |         |         |         |         |         |               |               |                |                                          |
|    family name                                                                                                                                                                                                                                                                                                                                                  |   2     |   FN   |   30    |   R     |         |   1     |   1     |         |               |               |                |                                          |
| HL7 Definition: Test data must conform to confidentiality rules.                                                                                                                                                                                                                                                                                                |         |        |         |         |         |         |         |         |               |               |                |                                          |

|                                                                                                       |         |        |         |         |         |         |         |         |               |               |                 |               |
|-------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|-----------------|---------------|
| Name                                                                                              | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val      | Reference |
|   ¦nbsp; surname                                                                                      |   1     |   ST   |   30    |   R     |         |   1     |   1     |         |               |               |   TIUPROVIDER   |               |
|   ¦nbsp; own surname prefix                                                                           |   2     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |                 |               |
|   ¦nbsp; own surname                                                                                  |   3     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |                 |               |
|   ¦nbsp; surname prefix from partner/spouse                                                           |   4     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |                 |               |
|   ¦nbsp; surname from partner/spouse                                                                  |   5     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |                 |               |
|    given name                                                                                         |   3     |   ST   |   30    |   R     |         |   1     |   1     |         |               |               |   ONEORIGINATOR |               |
|    second and further given names or initials thereof                                                 |   4     |   ST   |   30    | RE      |         |   0     |   1     |         |               |               |   M             |               |
|    suffix (e.g., JR or III)                                                                           |   5     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |                 |               |
|    prefix (e.g., DR)                                                                                  |   6     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |                 |               |
|    degree (e.g., MD)                                                                                  |   7     |   IS   |   3     | NS      |         |   0     |   0     | 0360    |               |               |                 |               |
|    source table                                                                                       |   8     |   IS   |   20    | NS      |         |   0     |   0     | 0297    |               |               |                 |               |
|    assigning authority                                                                                |   9     | HD     |   10    |   R     |         |   1     |   1     |         |               |               |                 |               |
|   ¦nbsp; namespace ID                                                                                 |   1     |   IS   |   10    |   R     |         |   1     |   1     | 0363    |               |               |   USVHA         |               |
| HL7 Definition:                                                                                       |         |        |         |         |         |         |         |         |               |               |                 |               |
|   Required to determine value in TXA.9.1 Originator Code/Name ID number: USVHA for DUZ; USSSA for SSN |         |        |         |         |         |         |         |         |               |               |                 |               |
|   ¦nbsp; universal ID                                                                                 |   2     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |                 |               |
|   ¦nbsp; universal ID type                                                                            |   3     |   ID   |   3     | NS      |         |   0     |   0     | 0301    |               |               |                 |               |
|    name type code                                                                                     |   10    |   ID   |   3     | NS      |         |   0     |   0     | 0200    |               |               |                 |               |
|    identifier check digit                                                                             |   11    |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |                 |               |

|                                                                                                                                                                                                                                                                                                                                                                            |         |       |        |       |         |      |         |      |         |     |         |      |         |        |         |     |               |     |               |               |               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|-------|--------|-------|---------|------|---------|------|---------|-----|---------|------|---------|--------|---------|-----|---------------|-----|---------------|---------------|---------------|
| Name                                                                                                                                                                                                                                                                                                                                                                   | Seq |       | DT |       | Len |      | Opt |      | Rep |     | Min |      | Max |        | Tbl |     | Predicate |     | Fixed Val | Ex Val    | Reference |
|    code identifying the check digit scheme employed                                                                                                                                                                                                                                                                                                                        |   12    |   ID  |        |   3   |         |   NS |         |      |         |   0 |         |   0  |         |   0061 |         |     |               |     |               |               |               |
|    identifier type code (IS)                                                                                                                                                                                                                                                                                                                                               |   13    |   IS  |        |   10  |         |   NS |         |      |         |   0 |         |   0  |         |   0203 |         |     |               |     |               |               |               |
|    assigning facility                                                                                                                                                                                                                                                                                                                                                      |   14    |   HD  |        |   3   |         |   NS |         |      |         |   0 |         |   0  |         |        |         |     |               |     |               |               |               |
|    Name Representation code                                                                                                                                                                                                                                                                                                                                                |   15    |   ID  |        |   3   |         |   NS |         |      |         |   0 |         |   0  |         |   0465 |         |     |               |     |               |               |               |
|    name context                                                                                                                                                                                                                                                                                                                                                            |   16    |   CE  |        |   15  |         |   NS |         |      |         |   0 |         |   0  |         |   0448 |         |     |               |     |               |               |               |
|    name validity range                                                                                                                                                                                                                                                                                                                                                     |   17    |   DR  |        |   3   |         |   NS |         |      |         |   0 |         |   0  |         |        |         |     |               |     |               |               |               |
|    name assembly order                                                                                                                                                                                                                                                                                                                                                     |   18    |   ID  |        |   3   |         |   NS |         |      |         |   0 |         |   0  |         |   0444 |         |     |               |     |               |               |               |
|   Assigned Document Authenticator                                                                                                                                                                                                                                                                                                                                          |   10    |   XCN |        |   250 |         |   RE |         | True |         |   0 |         |   \* |         |        |         |     |               |     |               |               |   9.6.1.10    |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                            |         |       |        |       |         |      |         |      |         |     |         |      |         |        |         |     |               |     |               |               |               |
|   Expected cosigner: Identifies expected co-signer. Will be used to look up user in NEW PERSON file \#200. Pointer to the person will be store in TIU DOCUMENT file \#8925, field 1208 EXPECTED COSIGNER                                                                                                                                                                   |         |       |        |       |         |      |         |      |         |     |         |      |         |        |         |     |               |     |               |               |               |
|   If the Document Completion Status is LA/Legally Authenticated, TIU will check for a date in the cosigner field TXA.22(1).15.1 Authentication Person, Time Stamp_rep. If the date is there, TIU will use the signature block information for this person to apply an electronic signature to this note for EXPECTED COSIGNER. The date of signature in VistA will be NOW. |         |       |        |       |         |      |         |      |         |     |         |      |         |        |         |     |               |     |               |               |               |
|    ID number (ST)                                                                                                                                                                                                                                                                                                                                                          |   1     |   ST  |        |   13  |         |   RE |         |      |         |   0 |         |   1  |         |        |         |     |               |     |               |   666554444   |               |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                            |         |       |        |       |         |      |         |      |         |     |         |      |         |        |         |     |               |     |               |               |               |
|   SSN or DUZ of a person in VistA NEW PERSON file \#200. Must have value in TXA 10.9.1 assigning authority namespace ID to determine what this number represents: USVHA for DUZ, USSSA for SSN.                                                                                                                                                                            |         |       |        |       |         |      |         |      |         |     |         |      |         |        |         |     |               |     |               |               |               |
|    family name                                                                                                                                                                                                                                                                                                                                                             |   2     |   FN  |        |   35  |         |   RE |         |      |         |   0 |         |   1  |         |        |         |     |               |     |               |               |               |
|   ¦nbsp; surname                                                                                                                                                                                                                                                                                                                                                           |   1     |   ST  |        |   30  |         |   R  |         |      |         |   1 |         |   1  |         |        |         |     |               |     |               |   TIUPROVIDER |               |
|   ¦nbsp; own surname prefix                                                                                                                                                                                                                                                                                                                                                |   2     |   ST  |        |   3   |         |   NS |         |      |         |   0 |         |   0  |         |        |         |     |               |     |               |               |               |
|   ¦nbsp; own surname                                                                                                                                                                                                                                                                                                                                                       |   3     |   ST  |        |   3   |         |   NS |         |      |         |   0 |         |   0  |         |        |         |     |               |     |               |               |               |

|                                                                                                                 |         |      |        |      |         |      |         |     |         |     |         |     |         |        |         |     |               |     |               |                  |               |
|-----------------------------------------------------------------------------------------------------------------|---------|------|--------|------|---------|------|---------|-----|---------|-----|---------|-----|---------|--------|---------|-----|---------------|-----|---------------|------------------|---------------|
| Name                                                                                                        | Seq |      | DT |      | Len |      | Opt |     | Rep |     | Min |     | Max |        | Tbl |     | Predicate |     | Fixed Val | Ex Val       | Reference |
|   ¦nbsp; surname prefix from partner/spouse                                                                     |   4     |   ST |        |   3  |         | NS   |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |                  |               |
|   ¦nbsp; surname from partner/spouse                                                                            |   5     |   ST |        |   3  |         | NS   |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |                  |               |
|    given name                                                                                                   |   3     |   ST |        |   30 |         | RE   |         |     |         |   0 |         |   1 |         |        |         |     |               |     |               | ONEAUTHENTICATOR |               |
|    second and further given names or initials thereof                                                           |   4     |   ST |        |   30 |         |   RE |         |     |         |   0 |         |   1 |         |        |         |     |               |     |               |   TWO            |               |
|    suffix (e.g., JR or III)                                                                                     |   5     |   ST |        |   3  |         | NS   |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |                  |               |
|    prefix (e.g., DR)                                                                                            |   6     |   ST |        |   3  |         | NS   |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |                  |               |
|    degree (e.g., MD)                                                                                            |   7     |   IS |        |   3  |         | NS   |         |     |         |   0 |         |   0 |         | 0360   |         |     |               |     |               |                  |               |
|    source table                                                                                                 |   8     |   IS |        |   30 |         | NS   |         |     |         |   0 |         |   0 |         |   0297 |         |     |               |     |               |                  |               |
|    assigning authority                                                                                          |   9     |  HD  |        |   10 |         |   RE |         |     |         |   0 |         |   1 |         |        |         |     |               |     |               |                  |               |
| HL7 Definition:                                                                                                 |         |      |        |      |         |      |         |     |         |     |         |     |         |        |         |     |               |     |               |                  |               |
|   Required if this group is populated, if ID number contains data.                                              |         |      |        |      |         |      |         |     |         |     |         |     |         |        |         |     |               |     |               |                  |               |
|   ¦nbsp; namespace ID                                                                                           |   1     |   IS |        |   10 |         |   RE |         |     |         |   0 |         |   1 |         |   0363 |         |     |               |     |               |   USSSA          |               |
| HL7 Definition:                                                                                                 |         |      |        |      |         |      |         |     |         |     |         |     |         |        |         |     |               |     |               |                  |               |
|   Required to determine source of number in field TXA.10.1 ID number. Should be USVHA for DUZ, or USSSA an SSN. |         |      |        |      |         |      |         |     |         |     |         |     |         |        |         |     |               |     |               |                  |               |
|   ¦nbsp; universal ID                                                                                           |   2     |   ST |        |   3  |         | NS   |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |                  |               |
|   ¦nbsp; universal ID type                                                                                      |   3     |   ID |        |   3  |         | NS   |         |     |         |   0 |         |   0 |         |   0301 |         |     |               |     |               |                  |               |
|    name type code                                                                                               | 10      |   ID |        |   3  |         | NS   |         |     |         |   0 |         |   0 |         |   0200 |         |     |               |     |               |                  |               |
|    identifier check digit                                                                                       | 11      |   ST |        |   3  |         | NS   |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |                  |               |

|                                                     |         |        |         |         |         |         |         |         |               |               |               |                                           |
|-----------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|---------------|-------------------------------------------|
| Name                                            | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val    | Reference                             |
|    code identifying the check digit scheme employed |   12    |   ID   |   3     |   NS    |         |   0     |   0     |   0061  |               |               |               |                                           |
|    identifier type code (IS)                        |   13    |   IS   |   30    |   NS    |         |   0     |   0     |         |               |               |               |                                           |
|    assigning facility                               | 14      |   HD   |   3     | NS      |         |   0     |   0     |         |               |               |               |                                           |
|    Name Representation code                         | 15      |   ID   |   3     | NS      |         |   0     |   0     |   0465  |               |               |               |                                           |
|    name context                                     | 16      |   CE   |   15    | NS      |         |   0     |   0     |   0448  |               |               |               |                                           |
|    name validity range                              | 17      |   DR   |   6     |   NS    |         |   0     |   0     |         |               |               |               |                                           |
|    name assembly order                              | 18      |   ID   |   3     | NS      |         |   0     |   0     | 0444    |               |               |               |                                           |
|   Transcriptionist Code/Name                        |   11    | XCN    | 250     | RE      | False   |   0     |   1     |         |               |               |               |   9.6.1.11                                |
| Implementation Note:                                |         |        |         |         |         |         |         |         |               |               |               |                                           |
|   The name of the transcriptionist in HL7           |         |        |         |         |         |         |         |         |               |               |               |                                           |
|   format along with the appropriate ID              |         |        |         |         |         |         |         |         |               |               |               |                                           |
|   NUMBER (SSN or IEN) and NAMESPACE                 |         |        |         |         |         |         |         |         |               |               |               |                                           |
|   ID (USSSA or USVHA).                              |         |        |         |         |         |         |         |         |               |               |               |                                           |
|    ID number (ST)                                   |   1     |   ST   |   20    | RE      |         |   0     |   1     |         |               |               |   666123456   |   8925; 1302 ENTERED BY (13:2) \[P200'O\] |
| Implementation Note:                                |         |        |         |         |         |         |         |         |               |               |               |                                           |
|   Pointer to \#200 NEW PERSON File                  |         |        |         |         |         |         |         |         |               |               |               |                                           |
|    family name                                      |   2     |   FN   |   50    | RE      |         |   0     |   1     |         |               |               |               |                                           |
|   ¦nbsp; surname                                    |   1     |   ST   |   30    | RE      |         |   0     |   1     |         |               |               |   TRANSCRIBER |   9.6.1.11                                |
|   ¦nbsp; own surname prefix                         |   2     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |               |                                           |
|   ¦nbsp; own surname                                |   3     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |               |                                           |
|   ¦nbsp; surname prefix from partner/spouse         |   4     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |               |                                           |

|                                                       |      |         |      |        |      |         |      |         |     |         |     |         |     |         |        |         |     |               |     |               |            |              |               |
|-------------------------------------------------------|------|---------|------|--------|------|---------|------|---------|-----|---------|-----|---------|-----|---------|--------|---------|-----|---------------|-----|---------------|------------|--------------|---------------|
| Name                                              |      | Seq |      | DT |      | Len |      | Opt |     | Rep |     | Min |     | Max |        | Tbl |     | Predicate |     | Fixed Val | Ex Val |              | Reference |
|   ¦nbsp; surname from partner/spouse                  |   5  |         |   ST |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |            |              |               |
|    given name                                         |   3  |         |   ST |        |   30 |         |   RE |         |     |         |   0 |         |   1 |         |        |         |     |               |     |               |            |   ONE TIUHL7 |   9.6.1.11    |
|    second and further given names or initials thereof |   4  |         |   ST |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |            |              |               |
|    suffix (e.g., JR or III)                           |   5  |         |   ST |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |            |              |               |
|    prefix (e.g., DR)                                  |   6  |         |   ST |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |            |              |               |
|    degree (e.g., MD)                                  |   7  |         |   IS |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |   0360 |         |     |               |     |               |            |              |               |
|    source table                                       |   8  |         |   IS |        |   30 |         |   RE |         |     |         |   0 |         |   1 |         |   0297 |         |     |               |     |               |            |   USSSA      |   HL70297     |
|    assigning authority                                |   9  |         |   HD |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |            |              |               |
|    name type code                                     |   10 |         |   ID |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |   0200 |         |     |               |     |               |            |              |               |
|    identifier check digit                             |   11 |         |   ST |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |            |              |               |
|    code identifying the check digit scheme employed   |   12 |         |   ID |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |   0061 |         |     |               |     |               |            |              |               |
|    identifier type code (IS)                          |   13 |         |   IS |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |            |              |               |
|    assigning facility                                 |   14 |         |   HD |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |            |              |               |
|    Name Representation code                           |   15 |         |   ID |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |   0465 |         |     |               |     |               |            |              |               |
|    name context                                       |   16 |         |   CE |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |   0448 |         |     |               |     |               |            |              |               |
|    name validity range                                |   17 |         |   DR |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |        |         |     |               |     |               |            |              |               |
|    name assembly order                                |   18 |         |   ID |        |   3  |         |   NS |         |     |         |   0 |         |   0 |         |   0444 |         |     |               |     |               |            |              |               |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                   |         |        |         |         |         |         |         |         |               |               |                    |               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|--------------------|---------------|
| Name                                                                                                                                                                                                                                                                                                                                                                                                                                          | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val         | Reference |
|   Unique Document Number                                                                                                                                                                                                                                                                                                                                                                                                                          |   12    |   EI   |   30    | RE      | False   |   0     |   1     |         |               |               |                    |   9.6.1.12    |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                                                                                                   |         |        |         |         |         |         |         |         |               |               |                    |               |
|   Surgery Report: this field should contain the Surgery case number and Unique Document File Name should also contain the title of the operative report. If this field is blank, an attempt will be made to locate a surgery case with a date equal to the Activity date/time. If there is only one surgery for this date and the TIU stub note does not already contain text, TIU will store the text of this document into this surgery report. |         |        |         |         |         |         |         |         |               |               |                    |               |
|   Consult Note: this field should identify the consult to which this note should be linked. This field will contain the DFN/IEN of the record in CONSULTATION file \#90.21.                                                                                                                                                                                                                                                                       |         |        |         |         |         |         |         |         |               |               |                    |               |
|   Note: HL7 Document Type is not used in this HL7 message. TIU identifies document type by the location of the document title in the TIU document hierarchy.                                                                                                                                                                                                                                                                                      |         |        |         |         |         |         |         |         |               |               |                    |               |
|    entity identifier                                                                                                                                                                                                                                                                                                                                                                                                                              |   1     |   ST   |   20    | RE      |         |   0     |   1     |         |               |               |   109              |               |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                                                                                                   |         |        |         |         |         |         |         |         |               |               |                    |               |
|   SURGERY case number                                                                                                                                                                                                                                                                                                                                                                                                                             |         |        |         |         |         |         |         |         |               |               |                    |               |
|   Consult number                                                                                                                                                                                                                                                                                                                                                                                                                                  |         |        |         |         |         |         |         |         |               |               |                    |               |
|    namespace ID                                                                                                                                                                                                                                                                                                                                                                                                                                   |   2     |   IS   |   10    | NS      |         |   0     |   0     |   0363  |               |               |                    |               |
|    universal ID                                                                                                                                                                                                                                                                                                                                                                                                                                   |   3     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |                    |               |
|    universal ID type                                                                                                                                                                                                                                                                                                                                                                                                                              |   4     |   ID   |   3     | NS      |         |   0     |   0     |   0301  |               |               |                    |               |
|   Parent Document Number                                                                                                                                                                                                                                                                                                                                                                                                                          |   13    |   EI   |   30    | NS      | False   |   0     |   0     |         |               |               |                    |   9.6.1.13    |
|   Placer Order Number                                                                                                                                                                                                                                                                                                                                                                                                                             |   14    |   EI   |   22    | NS      | False   |   0     |   0     |         |               |               |                    |   9.6.1.14    |
|   Filler Order Number                                                                                                                                                                                                                                                                                                                                                                                                                             |   15    |   EI   |   22    | NS      | False   |   0     |   0     |         |               |               |                    |   9.6.1.15    |
|   Unique Document File Name                                                                                                                                                                                                                                                                                                                                                                                                                       |   16    |   TX   |   60    |   R     | False   |   1     |   1     |         |               |               | History & Physical |   9.6.1.16    |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                                                                                                   |         |        |         |         |         |         |         |         |               |               |                    |               |
|   Document Title: This field contains a unique document title which must match an existing title in the TIU DOCUMENT DEFINITION file \#8925.1 at the receiving location. If this title does not exactly match the title in TIU, the HL7 record will be rejected. Note that the location of this title within the TIU document class hierarchy determines the type of document that will be created, not the content of the HL7 message.           |         |        |         |         |         |         |         |         |               |               |                    |               |

|                                                                                                                                                                                                                                                                                                                                                                                        |         |        |         |         |         |         |         |         |               |               |            |               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|---------------|
| Name                                                                                                                                                                                                                                                                                                                                                                               | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference |
|   Document Completion Status                                                                                                                                                                                                                                                                                                                                                           | 17      |   ID   |   2     | RE      | False   |   0     |   1     | 0271    |               |               |   LA       |   9.6.1.17    |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                                        |         |        |         |         |         |         |         |         |               |               |            |               |
|   Signed document: This field should be set to LA/Legally Authenticated if it is to be stored as a signed document. The document must be signed manually or electronically in the vendor package by the individual who is legally responsible for that document (TXA.Originator) and who has signature authority in VistA.                                                             |         |        |         |         |         |         |         |         |               |               |            |               |
|   If the author has an electronic signature in VistA, it will be applied to the document. If the VistA user does not have a valid electronic signature, the document can still be created, but it will not be signed. TIU will get the date/time of the signature from TXA Authentication Person, Time Stamp.                                                                          |         |        |         |         |         |         |         |         |               |               |            |               |
|   TIU will ignore this field if it is blank or any other value.                                                                                                                                                                                                                                                                                                                        |         |        |         |         |         |         |         |         |               |               |            |               |
|   Document Confidentiality Status                                                                                                                                                                                                                                                                                                                                                      | 18      |   ID   |   2     | NS      | False   |   0     |   0     | 0272    |               |               |            |   9.6.1.18    |
|   Document Availability Status                                                                                                                                                                                                                                                                                                                                                         | 19      |   ID   |   2     | RE      | False   |   0     |   1     | 0273    |               |               |   AV       |   9.6.1.19    |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                                        |         |        |         |         |         |         |         |         |               |               |            |               |
|   Progress Note: TIU will use this field to determine if a document should be stored when an existing visit cannot be located                                                                                                                                                                                                                                                          |         |        |         |         |         |         |         |         |               |               |            |               |
|   AV - Available: create document. If a visit cannot be located, a new historical visit will be created using today's date (NOW). The document will be attached to this new visit.                                                                                                                                                                                                     |         |        |         |         |         |         |         |         |               |               |            |               |
|   CA - Cancel (or blank): do not create document. If a visit cannot be located, the document will not be created and a reject Application ACK will be returned.                                                                                                                                                                                                                        |         |        |         |         |         |         |         |         |               |               |            |               |
|   Document Storage Status                                                                                                                                                                                                                                                                                                                                                              | 20      |   ID   |   2     | NS      | False   |   0     |   0     |   0275  |               |               |            |   9.6.1.20    |
|   Document Change Reason                                                                                                                                                                                                                                                                                                                                                               | 21      |   ST   | 30      | NS      | False   |   0     |   0     |         |               |               |            |   9.6.1.21    |
|   Authentication Person, Time Stamp                                                                                                                                                                                                                                                                                                                                                    |   22    | PPN    | 250     | RE      | True    |   0     |   \*    |         |               |               |            |   9.6.1.22.1  |
| Implementation Note:                                                                                                                                                                                                                                                                                                                                                                   |         |        |         |         |         |         |         |         |               |               |            |               |
|   must be in order, signer first, cosigner second                                                                                                                                                                                                                                                                                                                                      |         |        |         |         |         |         |         |         |               |               |            |               |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                                        |         |        |         |         |         |         |         |         |               |               |            |               |
|   Signed date/time: Used in conjunction with TXA.9 Originator Code/Name field. Contains date and time document was signed by EXPECTED SIGNER in the vendor package. If TXA.17 Document Completion Status is LA - legally authenticated, TIU will look for TXA.22.15 Date/Time Action Performed and will apply VistA electronic signature information to the TIU field EXPECTED SIGNER. |         |        |         |         |         |         |         |         |               |               |            |               |

|                                                                                                                                                                                                                                                          |         |        |         |         |         |         |         |         |               |               |            |               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|---------------|
| Name                                                                                                                                                                                                                                                 | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference |
|    ID number (ST)                                                                                                                                                                                                                                        |   1     |   ST   |   10    | NS      |         |   0     |   0     |         |               |               |            |               |
|    family name                                                                                                                                                                                                                                           |   2     |   FN   |   3     | NS      |         |   0     |   0     |         |               |               |            |               |
|    given name                                                                                                                                                                                                                                            |   3     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |            |               |
|    second and further given names or initials thereof                                                                                                                                                                                                    |   4     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |            |               |
|    suffix (e.g., JR or III)                                                                                                                                                                                                                              |   5     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |            |               |
|    prefix (e.g., DR)                                                                                                                                                                                                                                     |   6     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |            |               |
|    degree (e.g., MD)                                                                                                                                                                                                                                     |   7     |   IS   |   3     | NS      |         |   0     |   0     | 0360    |               |               |            |               |
|    source table                                                                                                                                                                                                                                          |   8     |   IS   |   3     | NS      |         |   0     |   0     | 0297    |               |               |            |               |
|    assigning authority                                                                                                                                                                                                                                   |   9     |   HD   |   3     | NS      |         |   0     |   0     |         |               |               |            |               |
|    name type code                                                                                                                                                                                                                                        |   10    |   ID   |   3     | NS      |         |   0     |   0     | 0200    |               |               |            |               |
|    identifier check digit                                                                                                                                                                                                                                |   11    |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |            |               |
|    code identifying the check digit scheme employed                                                                                                                                                                                                      |   12    |   ID   |   3     | NS      |         |   0     |   0     | 0061    |               |               |            |               |
|    identifier type code (IS)                                                                                                                                                                                                                             |   13    |   IS   |   10    | RE      |         |   0     |   1     |         |               |               |   SIGNER   |               |
| HL7 Definition:                                                                                                                                                                                                                                          |         |        |         |         |         |         |         |         |               |               |            |               |
|   Could be SIGNER or COSIGNER. This indicates that the Date/Time Action Performed represents signature by the EXPECTED SIGNER (represented by the Originator Code/Name) or by the EXPECTED COSIGNER (represented by the Assigned Document Authenticator) |         |        |         |         |         |         |         |         |               |               |            |               |
|    assigning facility                                                                                                                                                                                                                                    |   14    |   HD   |   3     | NS      |         |   0     |   0     |         |               |               |            |               |
|    Date/Time Action Performed                                                                                                                                                                                                                            |   15    |   TS   |   14    | RE      |         |   0     |   1     |         |               |               |            |               |
| HL7 Definition:                                                                                                                                                                                                                                          |         |        |         |         |         |         |         |         |               |               |            |               |
|   The date/time the document was signed. Will be stored in TIU DOCUMENT file \#8925, field 1501 SIGNATURE DATE/TIME                                                                                                                                      |         |        |         |         |         |         |         |         |               |               |            |               |

|                                                                                                                                                                                                                                                                                                                                                                                                               |         |        |         |         |         |         |         |         |               |                                                                                                |               |     |              |                                        |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|------------------------------------------------------------------------------------------------|---------------|-----|--------------|----------------------------------------|
| Name                                                                                                                                                                                                                                                                                                                                                                                                      | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate |                                                                                                | Fixed Val |     | Ex Val   | Reference                          |
|   ¦nbsp; Date/Time                                                                                                                                                                                                                                                                                                                                                                                            |   1     |   NM   |   14    | RE      |         |   0     |   1     |         |               |                                                                                                |               |     | 200501281230 |   TIU DOCUMENT file \#8925, field 1501 |
| Implementation Note:                                                                                                                                                                                                                                                                                                                                                                                          |         |        |         |         |         |         |         |         |               |                                                                                                |               |     |              |                                        |
|   YYYYMMDD\[HHHMM\[SS\[.SSSS\]\]\]\[+-ZZZZ\]                                                                                                                                                                                                                                                                                                                                                                  |         |        |         |         |         |         |         |         |               |                                                                                                |               |     |              |                                        |
|   ¦nbsp; degree of precision                                                                                                                                                                                                                                                                                                                                                                                  |   2     |   ST   |   0     | NS      |         |   0     |   0     |         |               |                                                                                                |               |     |              |                                        |
|    Name Representation code                                                                                                                                                                                                                                                                                                                                                                                   |   16    |   ID   |   3     | NS      |         |   0     |   0     | 0465    |               |                                                                                                |               |     |              |                                        |
|    name context                                                                                                                                                                                                                                                                                                                                                                                               |   17    |   CE   |   3     | NS      |         |   0     |   0     | 0448    |               |                                                                                                |               |     |              |                                        |
|    name validity range                                                                                                                                                                                                                                                                                                                                                                                        |   18    |   DR   |   3     | NS      |         |   0     |   0     |         |               |                                                                                                |               |     |              |                                        |
|    name assembly order                                                                                                                                                                                                                                                                                                                                                                                        |   19    |   ID   |   3     | NS      |         |   0     |   0     | 0444    |               |                                                                                                |               |     |              |                                        |
|   Authentication Person, Time Stamp_rep                                                                                                                                                                                                                                                                                                                                                                       |   22    | PPN    | 250     |   C     | False   |   0     |   1     |         |               |   Optional when the status of TXA-17 Document Completion Status is LA - Legally Authenticated. |               |     |              |   9.6.1.22.2                           |
| HL7 Definition:                                                                                                                                                                                                                                                                                                                                                                                               |         |        |         |         |         |         |         |         |               |                                                                                                |               |     |              |                                        |
|   Cosigned date/time. Used in conjunction with Cosigner information in TXA.10 Assigned Document Authenticator. Contains date and time document was signed by EXPECTED COSIGNER in the vendor package. If TXA.17 Document Completion Status is LA - legally authenticated, TIU will look for TXA.22(1).15.1 Date/Time Action Performed and will apply electronic signature to the TIU field EXPECTED COSIGNER. |         |        |         |         |         |         |         |         |               |                                                                                                |               |     |              |                                        |
|    ID number (ST)                                                                                                                                                                                                                                                                                                                                                                                             |   1     |   ST   |   10    |   NS    |         |   0     |   0     |         |               |                                                                                                |               |     |              |                                        |
|    family name                                                                                                                                                                                                                                                                                                                                                                                                |   2     |   FN   |   3     |   NS    |         |   0     |   0     |         |               |                                                                                                |               |     |              |                                        |
|    given name                                                                                                                                                                                                                                                                                                                                                                                                 |   3     |   ST   |   3     |   NS    |         |   0     |   0     |         |               |                                                                                                |               |     |              |                                        |
|    second and further given names or initials thereof                                                                                                                                                                                                                                                                                                                                                         |   4     |   ST   |   3     |   NS    |         |   0     |   0     |         |               |                                                                                                |               |     |              |                                        |

|                                                                                                                         |      |         |      |        |         |     |     |         |     |         |     |         |     |         |      |         |               |               |     |                  |            |                                                    |               |
|-------------------------------------------------------------------------------------------------------------------------|------|---------|------|--------|---------|-----|-----|---------|-----|---------|-----|---------|-----|---------|------|---------|---------------|---------------|-----|------------------|------------|----------------------------------------------------|---------------|
| Name                                                                                                                |      | Seq |      | DT | Len |     |     | Opt |     | Rep |     | Min |     | Max |      | Tbl | Predicate | Fixed Val |     |                  | Ex Val |                                                    | Reference |
|    suffix (e.g., JR or III)                                                                                             |   5  |         |   ST |        |         |   3 | NS  |         |     |         |   0 |         |   0 |         |      |         |               |               |     |                  |            |                                                    |               |
|    prefix (e.g., DR)                                                                                                    |   6  |         |   ST |        |         |   3 | NS  |         |     |         |   0 |         |   0 |         |      |         |               |               |     |                  |            |                                                    |               |
|    degree (e.g., MD)                                                                                                    |   7  |         |   IS |        |         |   3 | NS  |         |     |         |   0 |         |   0 |         | 0360 |         |               |               |     |                  |            |                                                    |               |
|    source table                                                                                                         |   8  |         |   IS |        |         |   3 | NS  |         |     |         |   0 |         |   0 |         | 0270 |         |               |               |     |                  |            |                                                    |               |
|    assigning authority                                                                                                  |   9  |         |   HD |        |         |   3 | NS  |         |     |         |   0 |         |   0 |         |      |         |               |               |     |                  |            |                                                    |               |
|    name type code                                                                                                       |   10 |         |   ID |        |         |   3 | NS  |         |     |         |   0 |         |   0 |         | 0200 |         |               |               |     |                  |            |                                                    |               |
|    identifier check digit                                                                                               |   11 |         |   ST |        |         |   3 | NS  |         |     |         |   0 |         |   0 |         |      |         |               |               |     |                  |            |                                                    |               |
|    code identifying the check digit scheme employed                                                                     |   12 |         |   ID |        |         |   3 | NS  |         |     |         |   0 |         |   0 |         | 0061 |         |               |               |     |                  |            |                                                    |               |
|    identifier type code (IS)                                                                                            |   13 |         |   IS |        |         | 10  | RE  |         |     |         |   0 |         |   1 |         |      |         |               |               |     |   COSIGNER       |            |                                                    |               |
|    assigning facility                                                                                                   |   14 |         |   HD |        |         |   3 | NS  |         |     |         |   0 |         |   0 |         |      |         |               |               |     |                  |            |                                                    |               |
|    Date/Time Action Performed                                                                                           |   15 |         |   TS |        |         | 20  | RE  |         |     |         |   0 |         |   1 |         |      |         |               |               |     |                  |            |                                                    |               |
| HL7 Definition:                                                                                                         |      |         |      |        |         |     |     |         |     |         |     |         |     |         |      |         |               |               |     |                  |            |                                                    |               |
|   The date/time the document was cosigned. Will be stored in TIU DOCUMENT file \#8925, field 1507 COSIGNATURE DATE/TIME |      |         |      |        |         |     |     |         |     |         |     |         |     |         |      |         |               |               |     |                  |            |                                                    |               |
|   ¦nbsp; Date/Time                                                                                                      |   1  |         |   NM |        |         | 14  | RE  |         |     |         |   0 |         |   1 |         |      |         |               |               |     |   20050128130005 |            |   TIU DOCUMENT file \#8925, field 1507 COSIGNATURE |               |
| Implementation Note:                                                                                                    |      |         |      |        |         |     |     |         |     |         |     |         |     |         |      |         |               |               |     |                  |            |                                                    |               |
|   YYYYMMDD\[HHHMM\[SS\[.SSSS\]\]\]\[+-ZZZZ\]                                                                            |      |         |      |        |         |     |     |         |     |         |     |         |     |         |      |         |               |               |     |                  |            |                                                    |               |
|   ¦nbsp; degree of precision                                                                                            |   2  |         |   ST |        |         |   0 | NS  |         |     |         |   0 |         |   0 |         |      |         |               |               |     |                  |            |                                                    |               |
|    Name Representation code                                                                                             |   16 |         |   ID |        |         |   3 | NS  |         |     |         |   0 |         |   0 |         | 0465 |         |               |               |     |                  |            |                                                    |               |
|    name context                                                                                                         |   17 |         |   CE |        |         |   3 | NS  |         |     |         |   0 |         |   0 |         | 0448 |         |               |               |     |                  |            |                                                    |               |
|    name validity range                                                                                                  |   18 |         |   DR |        |         |   3 | NS  |         |     |         |   0 |         |   0 |         |      |         |               |               |     |                  |            |                                                    |               |

|                                                    |         |        |         |         |         |         |         |         |               |               |            |               |
|----------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|---------------|
| Name                                           | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference |
|    name assembly order                             |   19    |   ID   |   3     | NS      |         |   0     |   0     | 0444    |               |               |            |               |
|   Distributed Copies (Code and Name of Recipients) |   23    | XCN    |   3     | NS      | False   |   0     |   0     |         |               |               |            |   9.6.1.23    |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="segment-obx">Segment: OBX </h3></td>
</tr>
<tr class="even">
<td><strong>Description:</strong> Observation/Result</td>
</tr>
<tr class="odd">
<td><strong>Optionality:</strong> R</td>
</tr>
<tr class="even">
<td><strong>Repeatable:</strong> True</td>
</tr>
<tr class="odd">
<td><strong>Minimum:</strong> 1</td>
</tr>
<tr class="even">
<td><strong>Maximum:</strong> *</td>
</tr>
<tr class="odd">
<td><strong>Reference:</strong> 7.4.2</td>
</tr>
</tbody>
</table>

#### Fields

|                                                                                                                                                                     |         |        |         |         |         |         |         |         |               |               |                                          |               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------------------------------------|---------------|
| Name                                                                                                                                                            | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val                               | Reference |
|   Set ID - OBX                                                                                                                                                      |   1     |   SI   |   4     |   R     | False   |   1     |   1     |         |               |               |   1                                      |   7.4.2.1     |
| HL7 Definition:                                                                                                                                                     |         |        |         |         |         |         |         |         |               |               |                                          |               |
|   This field contains the sequence number. For compatibility with ASTM.                                                                                             |         |        |         |         |         |         |         |         |               |               |                                          |               |
|   Value Type                                                                                                                                                        |   2     |   ID   |   2     |   R     | False   |   1     |   1     | 0125    |               |               |   TX                                     |   7.4.2.2     |
| HL7 Definition:                                                                                                                                                     |         |        |         |         |         |         |         |         |               |               |                                          |               |
|   TX is the only allowed valued and is used to send large amounts of text. In the TX data type, the repeat delimiter can only be used to identify paragraph breaks. |         |        |         |         |         |         |         |         |               |               |                                          |               |
|   Value Type should be TX - string data meant for user display (on a terminal or printer). Leading spaces should be included. Trailing spaces should be removed.    |         |        |         |         |         |         |         |         |               |               |                                          |               |
|   Observation Identifier                                                                                                                                            |   3     |   CE   |   88    | RE      | False   |   0     |   1     |         |               |               |                                          |   7.4.2.3     |
| HL7 Definition:                                                                                                                                                     |         |        |         |         |         |         |         |         |               |               |                                          |               |
|   Subject: This field will be used to pass an optional subject for the document. Non-standard use. Optional.                                                        |         |        |         |         |         |         |         |         |               |               |                                          |               |
|    identifier                                                                                                                                                       |   1     |   ST   |   8     | RE      |         |   0     |   1     |         |               |               |   Subject                                |               |
|    text                                                                                                                                                             |   2     |   ST   |   80    | RE      |         |   0     |   1     |         |               |               |   My Special Subject for this & Document |               |
|    name of coding system                                                                                                                                            |   3     |   IS   |   3     | NS      |         |   0     |   0     | 0396    |               |               |                                          |               |

|                                                                                                                                                                                                                                                                             |         |        |         |         |         |         |         |         |               |               |                                                                          |               |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|--------------------------------------------------------------------------|---------------|
| Name                                                                                                                                                                                                                                                                    | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val                                                               | Reference |
|    alternate identifier                                                                                                                                                                                                                                                     |   4     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |                                                                          |               |
|    alternate text                                                                                                                                                                                                                                                           |   5     |   ST   |   3     | NS      |         |   0     |   0     |         |               |               |                                                                          |               |
|    name of alternate coding system                                                                                                                                                                                                                                          |   6     |   IS   |   3     | NS      |         |   0     |   0     | 0396    |               |               |                                                                          |               |
|   Observation Sub-Id                                                                                                                                                                                                                                                        |   4     |   ST   |   20    | NS      | False   |   0     |   0     |         |               |               |                                                                          |   7.4.2.4     |
|   Observation Value                                                                                                                                                                                                                                                         |   5     |   TX   |   80    |   R     | True    |   1     |   \*    |         |               |               |   This is the first line of the note\| The patient shows signs of....    |   7.4.2.5     |
| Implementation Note:                                                                                                                                                                                                                                                        |         |        |         |         |         |         |         |         |               |               |                                                                          |               |
|   One Observation Value for each line of text                                                                                                                                                                                                                               |         |        |         |         |         |         |         |         |               |               |                                                                          |               |
| HL7 Definition:                                                                                                                                                                                                                                                             |         |        |         |         |         |         |         |         |               |               |                                                                          |               |
|   Text of TIU document. Only one OBX segment will be included in the message.                                                                                                                                                                                               |         |        |         |         |         |         |         |         |               |               |                                                                          |               |
|   This text will be stored in TIU DOCUMENT file \#8925, field 2 REPORT TEXT                                                                                                                                                                                                 |         |        |         |         |         |         |         |         |               |               |                                                                          |               |
|   The Observation Value element is repeatable and is Used to transmit document text. Each Observation Value should contain a single line of the text document. Leading spaces should be included. Trailing spaces should be removed.                                        |         |        |         |         |         |         |         |         |               |               |                                                                          |               |
|   The sending package will substitute the appropriate escape sequences for every field separator and encoding character in this and any other text field in the message. The receiving package will change every escape sequence back to the appropriate special character. |         |        |         |         |         |         |         |         |               |               |                                                                          |               |
|   Observation Value_rep                                                                                                                                                                                                                                                     |   5     |   TX   |   80    |   R     | False   |   1     |   1     |         |               |               |   Line 2 test special characters: ^ \\ \| ~ &                            |               |
|   Observation Value_rep                                                                                                                                                                                                                                                     |   5     |   TX   |   80    |   R     | False   |   1     |   1     |         |               |               |   This is the third line of the report... the patient has symptoms of... |               |
|   Observation Value_rep                                                                                                                                                                                                                                                     |   5     |   TX   |   80    |   R     | False   |   1     |   1     |         |               |               |                                                                          |               |
| HL7 Definition:                                                                                                                                                                                                                                                             |         |        |         |         |         |         |         |         |               |               |                                                                          |               |
|   This is a blank line for testing                                                                                                                                                                                                                                          |         |        |         |         |         |         |         |         |               |               |                                                                          |               |
|   Observation Value_rep                                                                                                                                                                                                                                                     |   5     |   TX   |   80    |   R     | False   |   1     |   1     |         |               |               |   This is the last line of the report...in conclusion,...                |               |
|   Units                                                                                                                                                                                                                                                                     |   6     |   CE   | 250     | NS      | False   |   0     |   0     |         |               |               |                                                                          |   7.4.2.6     |

|                                      |         |        |         |         |         |         |         |         |               |               |            |               |
|--------------------------------------|---------|--------|---------|---------|---------|---------|---------|---------|---------------|---------------|------------|---------------|
| Name                             | Seq | DT | Len | Opt | Rep | Min | Max | Tbl | Predicate | Fixed Val | Ex Val | Reference |
|   References Range                   |   7     |   ST   |   60    | NS      | False   |   0     |   0     |         |               |               |            |   7.4.2.7     |
|   Abnormal Flags                     |   8     |   IS   |   5     | NS      | False   |   0     |   0     | 0078    |               |               |            |   7.4.2.8     |
|   Probability                        |   9     |   NM   |   5     | NS      | False   |   0     |   0     |         |               |               |            |   7.4.2.9     |
|   Nature of Abnormal Test            |   10    |   ID   |   2     | NS      | False   |   0     |   0     | 0080    |               |               |            |   7.4.2.10    |
|   Observation Result Status          |   11    |   ID   |   1     | NS      | False   |   0     |   0     | 0085    |               |               |            |   7.4.2.11    |
|   Date Last Observation Normal Value |   12    |   TS   |   3     | NS      | False   |   0     |   0     |         |               |               |            |   7.4.2.12    |
|   User Defined Access Checks         |   13    |   ST   |   3     | NS      | False   |   0     |   0     |         |               |               |            |   7.4.2.13    |
|   Date/Time of the Observation       |   14    |   TS   |   26    | NS      | False   |   0     |   0     |         |               |               |            |   7.4.2.14    |
|   Producer's ID                      |   15    |   CE   | 250     | NS      | False   |   0     |   0     |         |               |               |            |   7.4.2.15    |
|   Responsible Observer               |   16    | XCN    | 250     | NS      | False   |   0     |   0     |         |               |               |            |   7.4.2.16    |
|   Observation Method                 |   17    |   CE   |   3     | NS      | False   |   0     |   0     |         |               |               |            |   7.4.2.17    |
|   Equipment Instance Identifier      |   18    |   EI   |   22    | NS      | False   |   0     |   0     |         |               |               |            |   7.4.2.18    |
|   Date/Time of the Analysis          |   19    |   TS   |   26    | NS      | False   |   0     |   0     |         |               |               |            |   7.4.2.19    |

# # Appendix B: Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Sample Test Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A test plan should contain the following elements:

1)  Manual entry of TIU titles. Any HL7 application will contain one or more titles that are unique to it. These titles must be entered into TIU on the VistA system and must match exactly what the HL7 vendor application sends.
2)  Set up and configure the HL7 logical link for the application to be tested.
3)  Set up of application parameters for TIUHL7 and vendor application to be tested.
4)  Set up of protocol event drivers for the application to be tested.
5)  Set up of protocol subscribers for the application to be tested.
6)  Alpha test plan.
7)  Beta test plan.
8)  Information regarding students and expected cosigners.
9)  TIU Team points of contact.
10) Application team points of contact.

Among the information that the following test plan leaves out, but must be present (by implication) is a set of test users. This includes test patients with valid veteran’s IDs, test signers, and test cosigners. You may use providers already in the system for test signers and cosigners, but you must not use actual patients. You must set up test patients with names and IDs that are easily identified with your test application.

A standard for test patients used within VHA is to use the application name as part of the test patient last name, and use a number spelled out as the first name. Example: CPRSPatient, One. This way it is entirely unambiguous who is a test patient. Similarly, the test Social Security Number assigned to test patients should start with either 666 or 000—number sequences not used by the Social Security Administration.

Once established, test patients need to be coordinated with the application vendor.

The following is verbatim from the ROES project testing document:

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This implementation and test plan covers the following areas:

1)  Manual entry of ROES TIU titles
2)  Set up of logical link for Denver Distribution Center
3)  Set up of application parameters for TIUHL7 and ROES-PN applications
4)  Set up of 4 protocol event drivers for ROES progress note project
5)  Set up of 4 protocol subscribers for ROES progress note project
6)  Alpha test plan
7)  Beta test plan
8)  Information regarding students and expected cosigners
9)  TIU Team points of contact
10) DDC points of contact

<u>Supplemental Implementation Steps</u> (to be performed by IRM or CAC working with ASPS):

### 1) ROES Standardized Local Titles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local titles cannot be distributed via VistA patches. The TIU Team is attempting to get the ROES titles approved by data standardization which would bring the status of ‘national title’ to them, permitting them to be distributed electronically. It is unlikely that this will happen prior to testing.

Manual input of 4 ROES standardized local titles is needed to ensure that the HL7 messages and the TIU progress notes contain the correct titles and can be processed correctly. Creation of a new TIU document would occur in the TIU package. Menu tree options are TIU IRM MAINTENANCE MENU\>DOCUMENT DEFINITION MGR\>CREATE DDEFS MGR.

If your site organizes these progress note titles under a specific document class, you will need to identify the appropriate document class name at your site under which Audiology or Audiology & Speech Pathology progress notes would be filed. This document class would be a parent to the ROES titles. If no document class exists at your site for Audiology or ASPS progress notes, the parent could be just the class ‘Progress Notes’ or you could create a new document class for Audiology (ASPS) progress notes if desired.

Creation of these new documents (optional document class and the 4 titles) will need to be performed by an individual at each site with the appropriate privileges and menu access. When installed manually, the titles should be entered by cutting and pasting them from this document to ensure that there are no typographic errors. The following listing documents the recommendations on title names and ancillary information:

Document Type = “DOCUMENT CLASS” (this may already exist at your site OR is an optional entry).

Parent Document Type = “CLASS”.

Parent = “PROGRESS NOTE”.

Name (of document class) = “AUDIOLOGY SERVICE NOTES” (or variant “AUDIOLOGY & SPEECH PATHOLOGY SERVICE NOTES”). Please cut and paste this name from this document if creating manually.

Status = “ACTIVE”.

Menu Text = “ASPS SERVICE NOTES”

The next 4 titles MUST be input to make this implementation of TIU patch 200 work for ROES progress notes.

Document Type = “TITLE”.

Parent Document Type = “DOCUMENT CLASS” (optional) OR “CLASS”.

Parent = “AUDIOLOGY SERVICE NOTES” (variant “AUDIOLOGY & SPEECH PATHOLOGY SERVICE NOTES”) OR “PROGRESS NOTE”.

Name (of document title) = “AUDIOLOGY ROES HEARING AID ORDER NOTE”. Please cut and paste this name from this document if creating manually.

Status = “Active”.

Print Name = “AUDIOLOGY ROES HEARING AID ORDER NOTE”.

Document Type = “TITLE”.

Parent Document Type = “DOCUMENT CLASS” (optional) OR “CLASS”.

Parent = “AUDIOLOGY SERVICE NOTES” (variant “AUDIOLOGY & SPEECH PATHOLOGY SERVICE NOTES”) OR “PROGRESS NOTE”.

Name (of document title) = “AUDIOLOGY ROES HEARING AID ISSUE NOTE”. Please cut and paste this name from this document if creating manually.

Status = “ACTIVE”.

Print Name = “AUDIOLOGY ROES HEARING AID ISSUE NOTE”.

Document Type = “TITLE”.

Parent Document Type = “DOCUMENT CLASS” (optional) OR “CLASS”.

Parent = “AUDIOLOGY SERVICE NOTES” (variant “AUDIOLOGY & SPEECH PATHOLOGY SERVICE NOTES”) OR “PROGRESS NOTE”.

Name (of document title) = “AUDIOLOGY ROES HEARING AID MODEL CHANGE NOTE”. Please cut and paste this name from this document if creating manually.

Status = “ACTIVE”.

Print Name = “AUDIOLOGY ROES HEARING AID MODEL CHANGE NOTE”.

Document Type = “TITLE”.

Parent Document Type = “DOCUMENT CLASS”.

Parent Document Type = “DOCUMENT CLASS” (optional) OR “CLASS”.

Parent = “AUDIOLOGY SERVICE NOTES” (variant “AUDIOLOGY & SPEECH PATHOLOGY SERVICE NOTES”) OR “PROGRESS NOTE”.

Name (of document title) = “AUDIOLOGY ROES HEARING AID SERVICE REQUEST NOTE”. Please cut and paste this name from this document if creating manually.

Status = “ACTIVE”.

Print Name = “AUDIOLOGY ROES HEARING AID SERVICE REQUEST NOTE”.

### 2) The HL7 Logical Link File \#870 – Link for DDC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Logical links describe the complete network path to a given system. The ROES sending application is configured to receive APPLICATION ACKNOWLEDGMENTS (AA) over the same port it is sending HL7 messages, so only one LOGICAL LINK is necessary. Your site should already have a link ready for this use.

- The Logical Link for DDC is VADDC.
- TCP/IP Service Type for the link must be set as “Client (Sender)”.
- The IP address should be set to 10.224.54.3.

If DDC determines that a second link is necessary for APPLICATION ACKNOWLEDGMENTS (AA), the DDC POC will contact you regarding the correct name, IP Address and Port \# to be used. If you had to edit the TCP/IP Service Type or IP address for this link save the changes and return to the HL7 Main Menu Option.

From the HL7 Main Menu option, select the Filer and Link Management Options menu. To test the link, select “Ping (TCP Only)” and at the prompt “Select HL LOGICAL LINK NODE:” enter VADDC. The message “PING Worked” should be displayed. If you do not see this message, ensure that the receiving system has been configured and setup properly. After the PING test, the link must be started. Here’s the menu and option:

Select HL7 Main Menu Option: Filer and Link Management Options

SM Systems Link Monitor

FM Monitor, Start, Stop Filers

LM TCP Link Manager Start/Stop

SA Stop All Messaging Background Processes

RA Restart/Start All Links and Filers

DF Default Filers Startup

SL Start/Stop Links

PI Ping (TCP Only)

ED Link Edit

ER Link Errors ...

Select Filer and Link Management Options Option: SL Start/Stop Links

\[This option is used to launch the lower level protocol for the appropriate device. Please select the node with which you want to communicate, in this case, VADDC.\]

Select HL LOGICAL LINK NODE: VADDC

### 3) The HL7 Application Parameter File \#771 – TIUHL7 and ROES-PN applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entries in this file are used to define the sending and receiving applications for VistA HL7. Each sending and receiving application must be defined separately. You can edit the examples exported in the patch for both the receiving and sending applications: TIUHL7 EX RECEIVING APP and TIUHL7 EX SENDING APP. From the HL7 Main Menu Option, select the Interface Developer Options menu. To set up HL7 Applications or edit the HL7 Example Applications, use the “EA Application Edit” option, on the Interface Developer Options menu:

Select Interface Developer Options Option: EA Application Edit

Select HL7 APPLICATION PARAMETER NAME: TIUHL7 EX RECEIVING APP

HL7 APPLICATION EDIT

---------------------------------------------------------------------------------------------------------------------

NAME: TIUHL7 EX RECEI ACTIVE/INACTIVE: INACTIVE

FACILITY NAME: COUNTRY CODE: USA

HL7 FIELD SEPARATOR: HL7 ENCODING CHARACTERS: ~\|\\

MAIL GROUP:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Rename the receiving example application TIUHL7. This application will always be the receiving application for the TIU Generic HL7 Interface. Change the status to ACTIVE. The Facility Name must be entered for routing information used by the HealthConnect (HC). \[If your site is not routing messages through a local HC this field is optional.\] The HL7 Field Separator and HL7 Encoding Characters do not need to be changed. Please see the HL7 Site Manager & Developer Manual for more information.

> Example Facility Name: 666~TESTLAB.FO-SLC.MED.VA.GOV~DNS.

> Example Facility Name: 621~ MTN-HOME.MED.VA.GOV~DNS.

> Example Facility Name: 554~ DENVER.MED.VA.GOV~DNS.

The receiving application should look like the following when finished editing:

HL7 APPLICATION EDIT

----------------------------------------------------------------------------------

NAME: TIUHL7 ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: \<your facility\> COUNTRY CODE: USA

HL7 FIELD SEPARATOR: HL7 ENCODING CHARACTERS: ~\|\\

MAIL GROUP:

Repeat this step for the Sending Application; rename the TIUHL7 EX SENDING APP to: ROES-PN*.* This name was used for the Sending Application from the ROES Progress Note project. The status should be set to ACTIVE, use the same country code and HL7 encoding characters. The FACILITY NAME should be set to: 791~VISTA.DDC.OAMM.VA.GOV~DNS.

The sending application should look like the following when finished editing:

HL7 APPLICATION EDIT

----------------------------------------------------------------------------------

NAME: ROES-PN ACTIVE/INACTIVE: ACTIVE

FACILITY NAME: 791~VISTA. COUNTRY CODE: USA

DDC.OAMM.VA.GOV~DNS

HL7 FIELD SEPARATOR: HL7 ENCODING CHARACTERS: ~\|\\

MAIL GROUP:

### 4) & 5) The Protocol File \#101 – ROES Event & Subscriber Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Entries in this file are used to define each transaction/message type. For the ROES Progress Note project, there are 4 distinct transaction/message types. There are two entries in this file included in the TIU\*1.0\*200 distribution that need to be edited:

> TIUHL7 EXAMPLE MDM SUB

> TIUHL7 EXAMPLE MDM EVENT

You will need to edit each to create the event and subscriber protocols for the first ROES message type (order):

> TIUHL7 ROES-PN ORDER MDM SUB (subscriber protocol)

> TIUHL7 ROES-PN ORDER MDM Event (event protocol).

Clone the edited protocols to create the other event and subscriber protocols for the other three ROES progress note transactions/message types.

\[Note: if you are already testing this patch with other partners, you may have edited the sample protocols in the patch for your first test partner. In that case, just clone all 4 ROES message type protocols for event and subscriber as described below.\]

From the HL7 Main Menu Option, select the Interface Developer Options menu. To set up or edit HL7 Protocols, use the “Protocol Edit” option, on the Interface Developer Options menu:

Select Interface Developer Options Option: Protocol Edit

Select PROTOCOL NAME: TIUHL7 EXAMPLE MDM SUB

HL7 INTERFACE SETUP PAGE 1 OF 2

----------------------------------------------------------------------------------

NAME: TIUHL7 EXAMPLE MDM SUB

DESCRIPTION (wp): (empty)

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber

The following naming convention is being used for protocols for the TIUHL7 ROES Interface:

TIUHL7 \<sending app\> MDM \<type\>,

where

\<sending app\> specifies the ROES application and ROES application message type

And

\<type\> specifies the type of protocol (either Subscriber or Event).

The first ROES subscriber protocol is: TIUHL7 ROES-PN ORDER MDM SUB*.* Please edit the example name for the first subscribing protocol to

> TIUHL7 ROES-PN ORDER MDM SUB.

\[Later clone the name for the other three subscribing protocols; these will be new entries from this same menu option:

> TIUHL7 ROES-PN ISSUE MDM SUB

> TIUHL7 ROES-PN MODEL CHANGE MDM SUB

> TIUHL7 ROES-PN SERVICE REQUEST MDM SUB.\]

Tab down to the Type field and press \<Enter\> or \<Return\> to accept ‘subscriber’ entry. The option then presents Page 2 to edit the fields specific to the subscriber type of the selected protocol:

HL7 SUBSCRIBER PAGE 2 OF 2

TIUHL7 ROES-PN ORDER MDM SUB

--------------------------------------------------------------------------------------------------------------------

RECEIVING APPLICATION: TIUHL7

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: T02

SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YES

SECURITY REQUIRED?: NO

LOGICAL LINK: VADDC

PROCESSING RTN: D PROCMSG^TIUHL7P1

ROUTING LOGIC:

Enter TIUHL7 as the RECEIVING APPLICATION. \[If your site is not using a HC to route HL7 messages, the Sending and Receiving Facilities Required fields may be set to NO. This is NOT the usual case.\] Replace the LOGICAL LINK and enter the name of the DDC logical link created/edited earlier to send Application Acknowledgments to the sending application. Do not change any of the other fields. Save the changes to the subscriber protocol.

\[When cloning/creating new subscriber protocol entries, you must type in the word ‘subscriber’ in the type field on page 1 and then press \<Enter\> to get into page 2. \]

Begin editing the example event protocol TIUHL7 EXAMPLE MDM EVENT as follows:

Select PROTOCOL NAME: TIUHL7 EXAMPLE MDM EVENT

HL7 INTERFACE SETUP PAGE 1 OF 2

----------------------------------------------------------------------------------

NAME: TIUHL7 EXAMPLE MDM EVENT

DESCRIPTION (wp): (empty)

ENTRY ACTION:

EXIT ACTION:

TYPE: event driver

The following naming convention is suggested for protocols for the TIUHL7 Interface:

TIUHL7 \<sending app\> MDM \<type\>,

Where

\<sending app\> specifies the ROES application and ROES application message type

And

\<type\> specifies the type of protocol (either Subscriber or Event).

The first ROES event protocol is: TIUHL7 ROES-PN ORDER MDM EVENT*.* This name was used for the first event protocol for messages from the ROES Progress Note project.

\[Later clone the name for the other three protocol event drivers; these will be new entries from this same menu option:

> TIUHL7 ROES-PN ISSUE MDM EVENT

> TIUHL7 ROES-PN MODEL CHANGE MDM EVENT

> TIUHL7 ROES-PN SERVICE REQUEST MDM EVENT.\]

Tab down to the Type field and press \<Enter\> or \<Return\> to accept the ‘event’ entry. The option then presents Page 2 to edit the fields specific to the event type of the selected protocol:

HL7 EVENT DRIVER PAGE 2 OF 2

TIUHL7 ROES-PN ORDER MDM EVENT

----------------------------------------------------------------------------------

SENDING APPLICATION: ROES-PN

TRANSACTION MESSAGE TYPE: MDM EVENT TYPE: T02

MESSAGE STRUCTURE:

PROCESSING ID: VERSION ID: 2.4

ACCEPT ACK CODE: AL APPLICATION ACK TYPE: NE

RESPONSE PROCESSING RTN:

SUBSCRIBERS

TIUHL7 ROES-PN ORDER MDM SUB

Edit the Sending Application to ROES-PN. The SUBSCRIBERS should reflect the new name created earlier for the subscribing protocol, TIUHL7 ROES-PN ORDER MDM SUB. Make these same types of entries for the other three protocol event drivers. See sample screen prints for each ROES event driver and subscriber protocol at the end of this document.

\[When cloning/creating new event driver protocol entries, you must type in the word ‘event’ in the type field on page 1 and then press \<Enter\> to get into page 2. \]

At the end of this process you should have:

Two applications:

> TIUHL7

> ROES-PN

Four event protocols:

> TIUHL7 ROES-PN ORDER MDM EVENT

> TIUHL7 ROES-PN ISSUE MDM EVENT

> TIUHL7 ROES-PN MODEL CHANGE MDM EVENT

> TIUHL7 ROES-PN SERVICE REQUEST MDM EVENT

And four subscribing protocols:

> TIUHL7 ROES-PN ORDER MDM SUB

> TIUHL7 ROES-PN ISSUE MDM SUB

> TIUHL7 ROES-PN MODEL CHANGE MDM SUB

> TIUHL7 ROES-PN SERVICE REQUEST MDM SUB.

Subscriptions should be as follows:

- The ROES ORDER subscriber protocol should be subscribing to the ROES ORDER event driver protocol.
- The ROES ISSUE subscriber protocol should be subscribing to the ROES ISSUE event driver protocol.
- The ROES MODEL CHANGE subscriber protocol should be subscribing to the ROES MODEL CHANGE event driver protocol.
- The ROES SERVICE REQUEST subscriber protocol should be subscribing to the ROES SERVICE REQUEST event driver protocol.

## Testing Plans for ROES progress note project

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### 6) Alpha Test Phase:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Ensure each site has installed TIU\*1\*200 in production environment.
2.  Ensure that supplemental implementation steps (above) have been completed.
3.  Audiology & Speech Pathology Service POC will identify 3-6 of each type of ROES transaction: order, issue, model change, and service request. ID by veteran name/SSN, date, type of transaction, audiologist. These transactions need to have been completed recently (2-4 weeks). Some transactions are done in higher volumes. If possible supply larger numbers of these test transactions.
4.  Please transmit this information to \< names & addresses removed for privacy reasons \>. Please transmit this information starting the week of 17-October.
5.  DDC HL7 messaging routines will be run against the appropriate ROES transactions to generate the HL7 messages.
6.  HL7 messages will be transmitted through the HC framework from DDC to testing site for upload.
7.  The local IRM or CAC POC may need to confirm message upload in TIU and/or investigate potential problems with upload at local site – problems would be reported to the TIU Team (contacts listed below) and \< names & addresses removed for privacy reasons \>.
8.  Once upload has been confirmed, the Audiology & Speech Pathology Service POC will be asked to review the notes and supply feedback on content, note layout, etc. to \< names & addresses removed for privacy reasons \>.

### 7) Beta Test Phase:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Ensure that the Alpha Test Phase is complete and that all issues have been resolved prior to starting the Beta Test Phase.
2.  DDC internal triggers for ROES HL7 messages will be turned ON for the 3 beta test sites. This will be done on or about 31-October.
3.  DDC will trigger ROES HL7 messages for all ROES orders, issues, model changes, and service requests for repair done at the three test sites.
4.  DDC will collect identifying information about each message (veteran name/SSN, date, type of transaction, and audiologist).
5.  Each local site will receive a list of ROES transactions for which an HL7 message was generated (by identifiers described above). This will probably be done once every day or two for at least one week, starting the week of 31-October.
6.  The local site will be asked to confirm that the messages did upload and that the content and format are correct (as agreed upon when the alpha test phase was completed).

### 8) Information Regarding Students

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Students cannot legally sign progress notes. If a student enters a ROES transaction that could result in a ROES progress note and the student is recorded as the “Requested By” person for the ROES transaction, the student MUST input an EXPECTED COSIGNER into the ROES system. The ROES custom/digital hearing aid order and ROES service request order screens are being modified to collect this data. In addition, checks are being inserted to ensure that an expected cosigner is input when the “Requested By” person is listed in the ROES system with a title of STUDENT. The student cannot get past the first ROES order page without inputting an expected cosigner.

The only way these checks will work and ensure that expected cosigners are present when required is if all students have been input correctly into the ROES system with a “Title” = “STUDENT.” It is imperative that all ROES supervisors check the “Title” setting for all students in the ROES Station Parameters Enter/Edit page. \[ROES Desktop\>Station Actions\>Station Parameters is the path to this page.\] The “Title” must be set = “STUDENT.”

Taking this action will NOT affect the students privileges in ROES; these are separate settings (on the same page) and each student should be given and/or retain the privileges deemed necessary and permissible by the supervisor.

## Contact Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### 9) TIU Team Contacts:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\< Names & addresses removed for privacy reasons. \>

### 10) DDC Contacts:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\< Names & addresses removed for privacy reasons. \>

## Sample ROES Event and Subscriber Protocol Screen Prints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROES Order Event Protocol:

HL7 INTERFACE SETUP PAGE 1 OF 2----------------------------------------------------------------------------------NAME: TIUHL7 ROES-PN ORDER MDM EVENT

DESCRIPTION (wp): \[Empty.\]ENTRY ACTION:EXIT ACTION:TYPE: event driverHL7 EVENT DRIVER PAGE 2 OF 2TIUHL7 ROES-PN ORDER MDM EVENT---------------------------------------------------------------------------------- SENDING APPLICATION: ROES-PN

TRANSACTION MESSAGE TYPE: MDM EVENT TYPE: T02MESSAGE STRUCTURE:PROCESSING ID: VERSION ID: 2.4ACCEPT ACK CODE: AL APPLICATION ACK TYPE: NERESPONSE PROCESSING RTN:SUBSCRIBERSTIUHL7 ROES-PN ORDER MDM SUB

ROES Order Subscriber Protocol:

HL7 INTERFACE SETUP PAGE 1 OF 2----------------------------------------------------------------------------------NAME: TIUHL7 ROES-PN ORDER MDM SUB

DESCRIPTION (wp): \[Empty\]ENTRY ACTION:EXIT ACTION:TYPE: subscriberHL7 SUBSCRIBER PAGE 2 OF 2TIUHL7 ROES-PN ORDER MDM SUB----------------------------------------------------------------------------------RECEIVING APPLICATION: TIUHL7

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: T02SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YESSECURITY REQUIRED?: NOLOGICAL LINK: VADDC

PROCESSING RTN: D PROCMSG^TIUHL7P1ROUTING LOGIC:

ROES Issue Event Protocol:

HL7 INTERFACE SETUP PAGE 1 OF 2----------------------------------------------------------------------------------NAME: TIUHL7 ROES-PN ISSUE MDM EVENT

DESCRIPTION (wp): \[Empty.\]ENTRY ACTION:EXIT ACTION:TYPE: event driverHL7 EVENT DRIVER PAGE 2 OF 2TIUHL7 ROES-PN ISSUE MDM EVENT----------------------------------------------------------------------------------SENDING APPLICATION: ROES-PN

TRANSACTION MESSAGE TYPE: MDM EVENT TYPE: T02MESSAGE STRUCTURE:PROCESSING ID: VERSION ID: 2.4ACCEPT ACK CODE: AL APPLICATION ACK TYPE: NERESPONSE PROCESSING RTN:SUBSCRIBERS

TIUHL7 ROES-PN ISSUE MDM SUB

ROES Issue Subscriber Protocol:

HL7 INTERFACE SETUP PAGE 1 OF 2----------------------------------------------------------------------------------NAME: TIUHL7 ROES-PN ISSUE MDM SUB

DESCRIPTION (wp): \[Empty\]ENTRY ACTION:EXIT ACTION:TYPE: subscriberHL7 SUBSCRIBER PAGE 2 OF 2TIUHL7 ROES-PN ISSUE MDM SUB----------------------------------------------------------------------------------RECEIVING APPLICATION: TIUHL7

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: T02SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YESSECURITY REQUIRED?: NOLOGICAL LINK: VADDC

PROCESSING RTN: D PROCMSG^TIUHL7P1ROUTING LOGIC:

ROES Model Change Event Protocol:

HL7 INTERFACE SETUP PAGE 1 OF 2----------------------------------------------------------------------------------NAME: TIUHL7 ROES-PN MODEL CHANGE MDM EVENT

DESCRIPTION (wp): \[Empty.\]ENTRY ACTION:EXIT ACTION:TYPE: event driverHL7 EVENT DRIVER PAGE 2 OF 2TIUHL7 ROES-PN MODEL CHANGE MDM EVENT----------------------------------------------------------------------------------SENDING APPLICATION: ROES-PN

TRANSACTION MESSAGE TYPE: MDM EVENT TYPE: T02MESSAGE STRUCTURE:PROCESSING ID: VERSION ID: 2.4ACCEPT ACK CODE: AL APPLICATION ACK TYPE: NERESPONSE PROCESSING RTN:SUBSCRIBERS

TIUHL7 ROES-PN MODEL CHANGE MDM SUB

ROES Model Change Subscriber Protocol:

HL7 INTERFACE SETUP PAGE 1 OF 2----------------------------------------------------------------------------------NAME: TIUHL7 ROES-PN MODEL CHANGE MDM SUB

DESCRIPTION (wp): \[Empty\]ENTRY ACTION:EXIT ACTION:TYPE: subscriberHL7 SUBSCRIBER PAGE 2 OF 2TIUHL7 ROES-PN MODEL CHANGE MDM SUB----------------------------------------------------------------------------------RECEIVING APPLICATION: TIUHL7

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: T02SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YESSECURITY REQUIRED?: NOLOGICAL LINK: VADDC

PROCESSING RTN: D PROCMSG^TIUHL7P1ROUTING LOGIC:

ROES Service Request Event Protocol:

HL7 INTERFACE SETUP PAGE 1 OF 2----------------------------------------------------------------------------------NAME: TIUHL7 ROES-PN SERVICE REQUEST MDM EVENT

DESCRIPTION (wp): \[Empty.\]ENTRY ACTION:EXIT ACTION:TYPE: event driverHL7 EVENT DRIVER PAGE 2 OF 2TIUHL7 ROES-PN SERVICE REQUEST MDM EVENT----------------------------------------------------------------------------------SENDING APPLICATION: ROES-PN

TRANSACTION MESSAGE TYPE: MDM EVENT TYPE: T02MESSAGE STRUCTURE:PROCESSING ID: VERSION ID: 2.4ACCEPT ACK CODE: AL APPLICATION ACK TYPE: NERESPONSE PROCESSING RTN:SUBSCRIBERS

TIUHL7 ROES-PN SERVICE REQUEST MDM SUB

ROES Service Request Subscriber Protocol:

HL7 INTERFACE SETUP PAGE 1 OF 2----------------------------------------------------------------------------------NAME: TIUHL7 ROES-PN SERVICE REQUEST MDM SUB

DESCRIPTION (wp): \[Empty\]ENTRY ACTION:EXIT ACTION:TYPE: subscriberHL7 SUBSCRIBER PAGE 2 OF 2TIUHL7 ROES-PN SERVICE REQUEST MDM SUB----------------------------------------------------------------------------------RECEIVING APPLICATION: TIUHL7

RESPONSE MESSAGE TYPE: ACK EVENT TYPE: T02SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YESSECURITY REQUIRED?: NOLOGICAL LINK: VADDC

PROCESSING RTN: D PROCMSG^TIUHL7P1ROUTING LOGIC:

## Appendix C: Setting Up TIU CCRA Interface Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Select HL LOGICAL LINK NODE: TIU1 TIUCCRAHL7 LOGICAL LINK--------------------------------------------------------------------------------NODE: TIUCCRA DESCRIPTION: +INSTITUTION: CHEYENNE VAMROCMAILMAN DOMAIN:AUTOSTART: EnabledQUEUE SIZE: 10LLP TYPE: TCPDNS DOMAIN:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_HL7 LOGICAL LINK--------------------------------------------------------------------------------+----------------------TCP LOWER LEVEL PARAMETERS-------------------------+¦ TIUCCRA ¦¦ ¦¦ TCP/IP SERVICE TYPE: CLIENT (SENDER) ¦¦ TCP/IP ADDRESS: xx.xxx.xx.xxx ¦¦ TCP/IP PORT: xxxx ¦¦ TCP/IP PORT (OPTIMIZED): ¦¦ ¦¦ ACK TIMEOUT: 5 RE-TRANSMISION ATTEMPTS: 1 ¦¦ READ TIMEOUT: 5 EXCEED RE-TRANSMIT ACTION: restart ¦¦ BLOCK SIZE: SAY HELO: ¦¦ TCP/IP OPENFAIL TIMEOUT: ¦¦STARTUP NODE: PERSISTENT: NO ¦¦ RETENTION: 30 UNI-DIRECTIONAL WAIT: ¦+-------------------------------------------------------------------------+======================================================================================HL7 APPLICATION PARAMETER NAME:1 TIU CCRA SEND ACTIVE2 TIU HSRM RECEIVE ACTIVE=====================================================================================HL7 APPLICATION EDIT--------------------------------------------------------------------------------NAME: TIU CCRA SEND ACTIVE/INACTIVE: ACTIVEFACILITY NAME: 534 COUNTRY CODE: USAHL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ^~\\MAIL GROUP: GMRCCCRA NOTIFICATIONS\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_HL7 APPLICATION EDIT--------------------------------------------------------------------------------NAME: TIU HSRM RECEIV ACTIVE/INACTIVE: ACTIVEFACILITY NAME: 200 COUNTRY CODE: USAHL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ^~\\MAIL GROUP:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_==================================================================================Select PROTOCOL NAME: TIU1 TIU CCRA-HSRM MDM-T02 CLIENT TIU CCRA-HSRM MDM-T02 CLIENT2 TIU CCRA-HSRM MDM-T02 SERVER TIU CCRA-HSRM MDM-T02 SERVER==================================================================================HL7 INTERFACE SETUP PAGE 1 OF 2--------------------------------------------------------------------------------NAME: TIU CCRA-HSRM MDM-T02 CLIENTDESCRIPTION (wp): + \[Sends HL7 MDM-T02 v2.5.1 messages from VistA CCRA\]ENTRY ACTION:EXIT ACTION:TYPE: subscriber\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Exit Save Refresh QuitHL7 SUBSCRIBER PAGE 2 OF 2TIU CCRA-HSRM MDM-T02 CLIENT--------------------------------------------------------------------------------RECEIVING APPLICATION: TIU HSRM RECEIVRESPONSE MESSAGE TYPE: ACK EVENT TYPE: T02SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YESSECURITY REQUIRED?:LOGICAL LINK: TIUCCRAPROCESSING RTN:ROUTING LOGIC:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_==================================================================================HL7 INTERFACE SETUP PAGE 1 OF 2--------------------------------------------------------------------------------NAME: TIU CCRA-HSRM MDM-T02 SERVERDESCRIPTION (wp): + \[Sends HL7 MDM-T02 v2.5.1 messages from VistA CC\]ENTRY ACTION:EXIT ACTION:TYPE: event driver\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_HL7 EVENT DRIVER PAGE 2 OF 2TIU CCRA-HSRM MDM-T02 SERVER--------------------------------------------------------------------------------+----------------------Sending Application Edit---------------------------+T¦ ¦¦ NAME: TIU CCRA SEND ACTIVE/INACTIVE: ACTIVE ¦¦ ¦¦ FACILITY NAME: 534 COUNTRY CODE: USA ¦¦ ¦R¦HL7 FIELD SEPARATOR: \| HL7 ENCODING CHARACTERS: ^~\\ ¦¦ ¦¦ ¦¦ MAIL GROUP: GMRCCCRA NOTIFICATIONS ¦¦ ¦+-------------------------------------------------------------------------+HL7 EVENT DRIVER PAGE 2 OF 2+--------------------------HL7 SUBSCRIBER--------------------------------+---¦ TIU CCRA-HSRM MDM-T02 CLIENT ¦---¦------------------------------------------------------------------------¦TR¦ RECEIVING APPLICATION: TIU HSRM RECEIV ¦¦ ¦¦ RESPONSE MESSAGE TYPE: ACK EVENT TYPE: T02 ¦¦ ¦¦SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YES ¦RE¦ ¦¦ SECURITY REQUIRED?: ¦T¦ ¦¦ LOGICAL LINK: TIUCCRA ¦¦ ¦¦ PROCESSING RTN: ¦¦ ROUTING LOGIC: ¦+------------------------------------------------------------------------+HL7 EVENT DRIVER PAGE 2 OF 2TIU CCRA-HSRM MDM-T02 SERVER--------------------------------------------------------------------------------SENDING APPLICATION: TIU CCRA SENDTRANSACTION MESSAGE TYPE: MDM EVENT TYPE: T02MESSAGE STRUCTURE:PROCESSING ID: VERSION ID: 2.5.1ACCEPT ACK CODE: AL APPLICATION ACK TYPE: NERESPONSE PROCESSING RTN:SUBSCRIBERSTIU CCRA-HSRM MDM-T02 CLIENT\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Exit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Community Care TIU Document POST-SIGNATURE CODE field setup.

==================================================================================Select OPTION: ENTER OR EDIT FILE ENTRIESInput to what File: TIU DOCUMENT// TIU DOCUMENT DEFINITION(1040 entries)EDIT WHICH FIELD: ALL// POST1 POST-SIGNATURE CODE2 POSTING INDICATORCHOOSE 1-2: 1 POST-SIGNATURE CODETHEN EDIT FIELD:Select TIU DOCUMENT DEFINITION NAME: <u>COMMUNITY CARE-PATIENT LETTER</u> TITLEStd Title: NONVA NOTEPOST-SIGNATURE CODE: D EN^TIUCCRHL()Select TIU DOCUMENT DEFINITION NAME: <u>COMMUNITY CARE-ADMINISTRATIVE REQUEST</u>TITLEStd Title: NONVA NOTEPOST-SIGNATURE CODE: D EN^TIUCCRHL()Select TIU DOCUMENT DEFINITION NAME: <u>COMMUNITY CARE-COORDINATION NOTE</u>TITLEStd Title: NONVA NOTEPOST-SIGNATURE CODE: D EN^TIUCCRHL()Select TIU DOCUMENT DEFINITION NAME: <u>COMMUNITY CARE-HOSPITAL NOTIFICATION NOTE</u>TITLEStd Title: NONVA NOTEPOST-SIGNATURE CODE: D EN^TIUCCRHL()Select TIU DOCUMENT DEFINITION NAME: <u>COMMUNITY CARE-EMERGENCY TREATMENT</u>TITLEStd Title: NONVA NOTEPOST-SIGNATURE CODE: D EN^TIUCCRHL()Select TIU DOCUMENT DEFINITION NAME:

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ACK 71
Acknowledgment—Accept Level 71
Acknowledgment—Application Level 71
Acronyms and Abbreviations 38
Action 71
Activity Date/Time 25
Admit Date/Time 19
ANSI 74
Assigned Document Authenticator 27
Assumptions 41
ASTM E1714-95 standard 74
ASU 71, 73
Audience 1
authentication 2
Availability 1
Boilerplate Text 71
business rule 44, 49, 71
business rules 42, 54, 61, 66
Care Coordinators 72
class 39, 41, 44, 72, 73
Clinician 72
Component 72
Component Separator 35
Components 1
Configuring the Interface 1
Consult 72
Consult \# 32
Consult documen 26
Consult Notes 39
Contact information 1
COTR 2
COTS 1, 3, 18, 19, 22, 25, 72
CPRS 1, 72
Create a TIU document 26
CWAD 73
Data File Number 17, 38, 73
Data Flow 1
Data Validation Rules 50
Database Repository 13
delimiters 36
DFN 38, 73
Dictation Date/Time 31
Discharge Summaries 40
discharge summary 40, 44, 59, 61, 63, 67
discharge SUMMARY 62
Discharge summary 26, 41
Discharge Summary 59, 73
Document Availability 34
document class 20, 39, 40, 41, 44, 49, 50, 51, 54, 55, 61, 66, 67, 73
Document Completion Status 33, 34
Document Definition 73
Document Definition File \#8925.1 20
Document File \#8925 17, 19, 23, 24, 25, 27
document titles 39
Entered By 28
Episode Begin Date/Time 31
error acknowledgement 26
error code 15
error message 15
Escape Characte 35
escape sequence 35
expected cosigner 24
Expected Cosigner 27
expected signer 24, 72
EXPECTED SIGNER 24
Field Separator 35
Fields 15
File \#101 6
File \#2 17, 50, 55, 62, 67
File \#200 24, 27, 50, 55, 62, 67
File \#771 5
File \#870 3
File \#8925 13, 17, 19, 23, 24, 25, 27
file \#8925.1 21
File \#8925.1 20
File \#9000010 19
Getting Started 1
Glossary 71
Health Level 7 74
HIMS 75
HL Logical Link File \#870 3
HL7 Application Parameter File \#771 5
HL7 Message Profile 80
HL7 tutorial 2, 79
HL7 version 2.4 2, 79
HL7 website 74
Home Telehealth 21
Home Telehealth titles 21
ICN 17, 18, 38, 41, 48, 50, 53, 55, 61, 62, 65, 67, 74
ID 74
IE 74
IEN 73, 74
Integration Control Number 17, 74
Interdisciplinary Note 74
Interface Engine 3, 38, 43, 46, 47, 52, 53, 59, 60, 64, 65, 74, 77
Internal Entry Number 38, 74
Introduction 1
IRM 2, 3
IRT 74
ISO 2
Maintenance Menu 15
Master Patient Index 74, 75
Message Manager 15
Messaging Workbench 1
MIS 75
MIS Manager 75
MPI 75
MRT 75
MWB 1
National ICN 17
New Person File \#200 24, 27, 50, 55, 62, 67
Observation Value 23
Office of Care Coordination 21
Originator 24
Overview 3
Patient File \#2 17, 18, 50, 55, 62, 67
Patient ICN 50, 55, 62, 67
Patient Name 18
Patient Visit 18
Patient’s Internal Entry Number 73
PCE visit file 15, 43
Physical Link 2
Procedure Request 75
progress note 15
Progress note 26
Progress Notes 39
Protocol 75
Protocol File \#101 6
Purpose 1
RDV 75
Reference Date/Time 31
Remote Data View 75
Repetition Separator 35
Requestor 76
Result 75
Sample Test Plan 115
Scope of the Manual 1
Screen Context 76
Segment Terminato 35
Segment: MSH 82
Service 76
Signature Status 32
SOAP 72
Social Security Number 17
Status Result 76
Status Symbols 76
Subcomponent Separator 35
Surgery Reports 39
Surgical Case \# 32
Surgical Operative Report 26
System Features 15
TCP/IP 76
Telehealth 76
Telemedicine 76
Template 71
test patients 115
test Social Security Number 115
Text 22
TIU Documents File \#8925 13
Transaction Control Protocol/Internet Protocol 76
TRANSCRIPTIONIST 28
tutorial 2, 79
Unique Document Note Title 20
Unique Patient Identifier 17
USVHA 74
Vendor Guidelines 37
VIE 3, 5, 7, 77
Visit File \#9000010 19
Visit Number 19, 28
VistA defined 77
VistA Documentation Library 1
VistA Interface Engine 3, 5, 38, 77
VistA Web 77
Vitria Interface Engine 77
VPN 2
XTEMP Global 16
