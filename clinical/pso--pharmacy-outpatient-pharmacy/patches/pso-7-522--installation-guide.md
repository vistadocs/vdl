---
title: PSO*7*522 Health Connect/Outpatient Pharmacy Automated Interface (OPAI) 1.0 Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Health Connect/Outpatient Pharmacy Automated Interface (OPAI) 1.0 Install Guide
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*522
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 1
description: The purpose of this Installation Guide is to provide an explanation of the installation and implementation process for the Outpatient Pharmacy V. 7.0 Automation Interface project. This project enhances and upgrades the current Outpatient Pharmacy Health Level 7 (HL7) interface to ensure that the int
audience: 
keywords: 
  - interface
  - table
  - contents
  - link
  - outpatient
  - install
  - dispensing
  - dispense
  - site
  - installation
page_count: 0
word_count: 7173
section_count: 31
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_p522_opai_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_p522_opai_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

> ![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-1-0-instal/001.png)

Outpatient PharmacyAutomation Interface

# INSTALLATION GUIDE


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [INSTALLATION GUIDE](#installation-guide)
- [Table of Contents](#table-of-contents)
- [Purpose](#purpose)
- [Scope](#scope)
- [Before You Begin](#before-you-begin)
- [Section 1: Installing the Software](#section-1-installing-the-software)
- [Pre-Installation](#pre-installation)
  - [System Requirements](#system-requirements)
  - [Understanding the Installation Process](#understanding-the-installation-process)
    - [Input Template](#input-template)
- [Installation of Patch](#installation-of-patch)
  - [Installing PSO\7\156](#installing-pso7156)
- [## Installing PSS\1\82](#installing-pss182)
  - [Installing PSN\4\84](#installing-psn484)
- [Post-Installation](#post-installation)
  - [Setting up the Mail Group for HL7 Alerts](#setting-up-the-mail-group-for-hl7-alerts)
  - [# Section 2: Implementing the New Interface](#section-2-implementing-the-new-interface)
- [Pre-Implementation](#pre-implementation)
  - [Completing the Implementation Worksheet](#completing-the-implementation-worksheet)
  - [Validating the Dispense DNS Name](#validating-the-dispense-dns-name)
  - [List of Pharmacist Names](#list-of-pharmacist-names)
  - [Purging Existing Entries in the PHARMACY EXTERNAL INTERFACE File (#52.51)](#purging-existing-entries-in-the-pharmacy-external-interface-file-5251)
- [Performing the Implementation](#performing-the-implementation)
  - [Step 1: Stopping the Dispensing System Logical Link](#step-1-stopping-the-dispensing-system-logical-link)
  - [Step 2: Selecting the Outpatient Site](#step-2-selecting-the-outpatient-site)
  - [Step 3: Turning on the External Interface](#step-3-turning-on-the-external-interface)
  - [Step 4: Setting up a Dispensing System Printer](#step-4-setting-up-a-dispensing-system-printer)
  - [Step 5: Enabling the Automated Dispense Parameter](#step-5-enabling-the-automated-dispense-parameter)
  - [Step 6: Setting the File Release Date/Time Parameter](#step-6-setting-the-file-release-datetime-parameter)
  - [Step 7: Enabling Master File Updates for the DRUG File (#50)](#step-7-enabling-master-file-updates-for-the-drug-file-50)
  - [Step 8: Setting the Dispense DNS Name](#step-8-setting-the-dispense-dns-name)
  - [Step 9: Setting the Dispense DNS Port](#step-9-setting-the-dispense-dns-port)
  - [Step 10: Setting the Outpatient Pharmacy Logical Link](#step-10-setting-the-outpatient-pharmacy-logical-link)
  - [Step 11: Setting up the Logical Link in HL7](#step-11-setting-up-the-logical-link-in-hl7)
  - [## The following is an example of the HL Logical Link Node:](#the-following-is-an-example-of-the-hl-logical-link-node)
  - [Step 12: Starting the Dispensing System Logical Link](#step-12-starting-the-dispensing-system-logical-link)
- [Troubleshooting](#troubleshooting)
  - [## Turning off the HL7 V. 2.4 Interface](#turning-off-the-hl7-v-24-interface)
  - [Resetting the Dispense DNS Name](#resetting-the-dispense-dns-name)
  - [Resetting the Dispensing System Logical Link](#resetting-the-dispensing-system-logical-link)
- [# Appendix A: Implementation Worksheet](#appendix-a-implementation-worksheet)
  - [Setting up the Interface](#setting-up-the-interface)
  - [Several new parameters have been created to support this project, and a modification was made to one of the existing site parameters. Determine the information needed to set your site’s parameters for each OUTPATIENT SITE entry before you install.](#several-new-parameters-have-been-created-to-support-this-project-and-a-modification-was-made-to-one-of-the-existing-site-parameters-determine-the-information-needed-to-set-your-sites-parameters-for-each-outpatient-site-entry-before-you-install)
  - [> 12: HL7 Logical Link On](#12-hl7-logical-link-on)
  - [## Implementation Worksheet — Steps Completed](#implementation-worksheet-steps-completed)
PSO\*7\*156
PSS\*1\*82
PSN\*4\*84
October 2004
(revised March 2019)
V*IST*A Health Systems Design & Development

# Table of Contents

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Installation Guide is to provide an explanation of the installation and implementation process for the Outpatient Pharmacy V. 7.0 Automation Interface project. This project enhances and upgrades the current Outpatient Pharmacy Health Level 7 (HL7) interface to ensure that the interface is compatible with all current Outpatient Pharmacy automated dispensing systems used by the Department of Veterans Affairs Medical Centers (VAMCs). The current V*IST*A HL7 interface is written to the HL7 V. 2.2 standard, and newer automated dispensing systems use an interface written to the newer HL7 V. 2.3.1 standard. The Outpatient Pharmacy Automation Interface project will use the HL7 V. 2.4 standard to create a generic interface compatible with most dispensing systems.

The intended audience for this document is the medical center staff responsible for installation of the patches and setup of the new Outpatient Pharmacy site parameters. These site parameters are described in the section “Understanding the Installation Process.”

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of this project includes enhancements to Outpatient Pharmacy software interfaces. It does not include interfaces to automated dispensing systems used for inpatient medications. The project provides the following enhancements.

- Updates the current Outpatient Pharmacy V.7.0 package HL7 interface to the current ANSI-approved HL7 V.2.4 standard.
- Transmits Outpatient Pharmacy data to multiple vendor systems utilized by VAMCs and receives dispensed prescription data from the vendor systems.
- Provides the ability to send updates to vendor systems through HL7 messaging when changes occur to the national drug file and DRUG file (#50).
- Supports bi-directional HL7 messaging.
- Adds new fields, and changes current field names.
- Uses InterSystems Health Connect to pass data from V*IST*A to the dispensing systems, and back.
*  
(This page included for two-sided copying.)*

# Before You Begin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is organized into two major sections: “Installing the Software” and “Implementing the New Interface.”

It is expected that most sites will install the software and not immediately implement the new interface. This approach is recommended.

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-1-0-instal/002.png)

When the decision is made to implement, it is very important that you complete the Implementation Worksheet (located in Appendix A) and have a copy of this information available for troubleshooting.Having the proper setup of parameters and settings is critical to the success of the implementation.

*(This page included for two-sided copying.)*

# Section 1: Installing the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides information needed to install the patches associated with the project, and is organized in the following sections:

- Pre-Installation
- Installing the Patches
- Post Installation

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides information that helps you determine patch and system requirements before installing the patches that are included in this project. It also helps you understand the updates that the installation process makes. Additionally, descriptions are provided regarding the specific parameters that you must set up to implement the interface.

The Outpatient Pharmacy Automation Interface project is comprised of these patches:

- PSO\*7\*156
- PSS\*1\*82
- PSN\*4\*84

All of the patches must be installed to work properly. There are several steps following installation that will turn on the interface; thus, the patches may be installed, but are not implemented until all of the steps are completed that will turn on the HL7 V. 2.4 standard interface.

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient Pharmacy Automation Interface project operates on standard hardware platforms used by the Veterans Health Administration (VHA) facilities and requires the following Department of Veterans Affairs (VA) software packages to support the enhancements in this project.

|                                  |                        |
|----------------------------------|------------------------|
| Package                          | Minimum Version Needed |
| VA FileMan                       | 22.0                   |
| Kernel                           | 8.0                    |
| MailMan                          | 8.0                    |
| Outpatient Pharmacy              | 7.0                    |
| Scheduling                       | 5.3                    |
| Health Level 7                   | 1.6                    |
| Text Integration Utilities       | 1.0                    |
| Decision Support System          | 3.0                    |
| Integrated Billing               | 2.0                    |
| Pharmacy Benefits Management     | 3.0                    |
| Order Entry/Results Reporting    | 3.0                    |
| Automated Info Collection System | 3.0                    |
| Health Summary                   | 2.7                    |

The above software is not included in this patch and must be installed for this patch to be completely functional.

## Understanding the Installation Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installing the patches in the project does not automatically implement the new HL7 V. 2.4 standard interface. Thus, you can install the patch now, and turn on the new interface at a later date.

During installation, the following installations/processes should occur automatically:

- New site parameters are installed.
- HL7 protocols are installed.
- HL7 Application Parameter Names are installed.
- An HL7 Logical Link is installed.

############################### New Site Parameters

There are several new site parameters added to the OUTPATIENT SITE file installed with PSO\*7\*156, and one modified site parameter that should be set up to turn on the new interface. These parameters include:

- DISPENSING SYSTEM PRINTER
- AUTOMATED DISPENSE
- FILE RELEASE DATE/TIME
- ENABLE MASTER FILE UPDATE
- DISPENSE DNS NAME
- DISPENSE DNS PORT

For a detailed description of each of these parameters, see the Implementation Worksheet in Appendix A of this guide.

###############################  New HL7 Protocols 

The following HL7 Protocols are installed during the installation process:

- *Outpatient Pharmacy Dispense Server* \[PSO EXT SERVER\] protocol
- *Outpatient Pharmacy Dispense Client* \[PSO EXT CLIENT\] protocol
- *Outpatient Pharmacy Completion Server* \[PSO DISP SERVER\] protocol
- *Outpatient Pharmacy Completion Client* \[PSO DISP CLIENT\] protocol
- *PDM Master File Update* \[PSS EXT MFU SERVER\] protocol
- *PDM Master File Update Client* \[PSS EXT MFU CLIENT\] protocol

The *Outpatient Pharmacy Dispense Server* \[PSO EXT SERVER\] protocol has been added as a new event driver protocol, and is necessary for transmission of prescription fills to the automated dispensing system using HL7 V. 2.4 messages. The *Outpatient Pharmacy Dispense Client* \[PSO EXT CLIENT\] protocol has been added as a subscriber to the new event driver, and is used when the automated dispensing machines sends dispense request information back to V*IST*A.

The *Outpatient Pharmacy Completion Server* \[PSO DISP SERVER\] protocol is necessary for the transmission of dispensed prescription information to V*IST*A using HL7 V. 2.4 messages. The *Outpatient Pharmacy Completion Client* \[PSO DISP CLIENT\] protocol is a subscriber to this new event driver, and is used when the automated dispensing machines sends dispense completion information to V*IST*A.

The *PDM Master File Update* \[PSS EXT MFU SERVER\] protocol is necessary to send event notification and data when new drugs are added to the DRUG file (#50) and when certain fields are updated in the same file. This information will be sent to the automated dispensing machine through HL7 V.2.4 formatted messages. The *PDM Master File Update Client* \[PSS EXT MFU CLIENT\] protocol is used as the acknowledgement (ACK) from the external interface for a MFN_M01 message.

The Outpatient Pharmacy (PSO) protocols are only exported in the Patch PSO\*7\*156; the Pharmacy Data Management (PSS) protocols are only exported in the Patch PSS\*1\*82.

The protocol attributes are not displayed during the installation process; however, an example of the protocol attributes is shown on the following page.

  
Example: Protocol Attributes

NUMBER: 5128 NAME: PSO DISP CLIENT

ITEM TEXT: OUTPATIENT PHARMACY COMPLETION CLIENT

TYPE: subscriber CREATOR: OPIRMS23,SIX

TIMESTAMP: 59602,34742 RECEIVING APPLICATION: PSO VISTA

EVENT TYPE: O14 LOGICAL LINK: PSO DISP

RESPONSE MESSAGE TYPE: ACK PROCESSING ROUTINE: D ACK^PSOHLDS

SENDING FACILITY REQUIRED?: YES RECEIVING FACILITY REQUIRED?: YES

NUMBER: 5127 NAME: PSO DISP SERVER

ITEM TEXT: OUTPATIENT PHARMACY COMPLETION SERVER

TYPE: event driver CREATOR: OPIRMS23,SIX

DESCRIPTION: This protocol is used when a dispensing system external

interface sends back a dispensing message to VistA.

TIMESTAMP: 59602,34760 SENDING APPLICATION: PSO DISPENSE

TRANSACTION MESSAGE TYPE: RRD EVENT TYPE: O14

ACCEPT ACK CODE: AL APPLICATION ACK TYPE: NE

VERSION ID: 2.4 RESPONSE PROCESSING ROUTINE: Q

SUBSCRIBERS: PSO DISP CLIENT

NUMBER: 5087 NAME: PSO EXT CLIENT

ITEM TEXT: OUTPATIENT PHARMACY DISPENSE CLIENT

TYPE: subscriber CREATOR: OPIRMS23,SIX

DESCRIPTION: This protocol is used as the ACK from the external interface

for an RDS_O13 message.

TIMESTAMP: 59602,34690 RECEIVING APPLICATION: PSO DISPENSE

EVENT TYPE: O13 LOGICAL LINK: PSO DISP

RESPONSE MESSAGE TYPE: ACK SENDING FACILITY REQUIRED?: YES

RECEIVING FACILITY REQUIRED?: YES

NUMBER: 5086 NAME: PSO EXT SERVER

ITEM TEXT: OUTPATIENT PHARMACY DISPENSE SERVER

TYPE: event driver CREATOR: OPIRMS23,SIX

DESCRIPTION: This protocol is necessary for transmission of prescription

fills to the automatic dispensing machine using HL7 V.2.4 formatted messages.

TIMESTAMP: 59602,34669 SENDING APPLICATION: PSO VISTA

TRANSACTION MESSAGE TYPE: RDS EVENT TYPE: O13

ACCEPT ACK CODE: AL APPLICATION ACK TYPE: AL

VERSION ID: 2.4

RESPONSE PROCESSING ROUTINE: D ACK^PSOHLDS

SUBSCRIBERS: PSO EXT CLIENT

NUMBER: 5131 NAME: PSS EXT MFU CLIENT

ITEM TEXT: PDM MASTER FILE UPDATE CLIENT

TYPE: subscriber CREATOR: OPIRMS23,SIX

DESCRIPTION: This protocol will be used as the ACK from the external

interface for a MFN_M01 message.

TIMESTAMP: 59627,48470 RECEIVING APPLICATION: PSS DISPENSE

EVENT TYPE: M01 LOGICAL LINK: PSO DISP

RESPONSE MESSAGE TYPE: ACK SENDING FACILITY REQUIRED?: YES

RECEIVING FACILITY REQUIRED?: YES

NUMBER: 5130 NAME: PSS EXT MFU SERVER

ITEM TEXT: PDM MASTER FILE UPDATE TYPE: event driver

CREATOR: OPIRMS23,SIX

DESCRIPTION: This protocol will be used to send event notification and data

when new drugs are added to the DRUG file (#50) and when certain fields are

updated in the same file. This information will be sent to the automated

dispensing machines through HL7 V.2.4 formatted messages.

TIMESTAMP: 59627,48318 SENDING APPLICATION: PSS VISTA

TRANSACTION MESSAGE TYPE: MFN EVENT TYPE: M01

ACCEPT ACK CODE: NE APPLICATION ACK TYPE: AL

VERSION ID: 2.4

SUBSCRIBERS: PSS EXT MFU CLIENT

###############################  New HL7 Application Parameters

Four new application parameters have been created to support building the HL7 message. These parameters are:

- PSO VISTA
- PSO DISPENSE
- PSS VISTA
- PSS DISPENSE.

PSO VISTA has been added to the HL7 APPLICATION PARAMETER file (#771) and is exported as the Receiving Application of the *Outpatient Pharmacy Dispense Server* \[PSO EXT SERVER\] protocol. PSO DISPENSE has been added to the HL7 APPLICATION PARAMETER file (#771) and is exported as the Sending Application of the *Outpatient Pharmacy Completion Server* \[PSO DISP SERVER\] protocol.

PSS VISTA has been added to the HL7 APPLICATION PARAMETER file (#771) and is exported as the Sending Application of the *PDM Master File Update* \[PSS EXT MFU SERVER\] protocol. PSS DISPENSE has been added to the HL7 APPLICATION PARAMETER file (#771) and is exported as the Receiving Application of the *PDM Master File Update Client* \[PSS EXT MFU CLIENT\] protocol.

The parameter attributes are not displayed during the installation process; however, here is an example of the parameter attributes:

Example: Parameter Attributes

NUMBER: 118 NAME: PSS DISPENSE

ACTIVE/INACTIVE: ACTIVE COUNTRY CODE: US

HL7 ENCODING CHARACTERS: ~^\\ HL7 FIELD SEPARATOR: \|

NUMBER: 117 NAME: PSS VISTA

ACTIVE/INACTIVE: ACTIVE COUNTRY CODE: US

HL7 ENCODING CHARACTERS: ~^\\ HL7 FIELD SEPARATOR: \|

###############################  Data Dictionary Updates

This patch contains updates to the data dictionaries of the OUTPATIENT SITE file (#59) and PRESCRIPTION file (#52), including input templates.

OUTPATIENT SITE File (#59)

The following new fields are added to the OUTPATIENT SITE file (#59):

- AUTOMATED DISPENSE field (#105)
- FILE RELEASE DATE/TIME field (#105.1)
- ENABLE MASTER FILE UPDATE field (#105.2)
- DISPENSE DNS NAME field (#2006)
- DISPENSE DNS PORT field (#2007)
- DISPENSING SYSTEM PRINTER field (#2008)

The following field in the OUTPATIENT SITE file (#59) has been modified:

- The EXTERNAL INTERFACE field (#5) now includes a new selection: SEND ALL ORDERS AND PRINT LABELS.

PRESCRIPTION File (#52)

The following new fields are added to the PRESCRIPTION file (#52):

- FILLING PERSON field (#38.1)
- CHECKING PHARMACIST field (#38.2)

The following field name has changed:

- The MAN EXPIRATION DATE field (#29) has changed to the DRUG EXPIRATION DATE field (#29).

PRESCRIPTION file (#52) – REFILL sub-file (#52.1)

The following new fields are added to the REFILL sub-file (#52.1) of the PRESCRIPTION file (#52):

- FILLING PERSON field (#19)
- CHECKING PHARMACIST field (#20)

The following field name has changed:

- The EXPIRATION DATE field (#13) has changed to the DRUG EXPIRATION DATE field (#29).

  
PRESCRIPTION file (#52) – PARTIAL sub-file (#52.2)

The following new fields are added to the PARTIAL sub-file (#52.2) of the PRESCRIPTION file (#52):

- FILLING PERSON field (#10)
- CHECKING PHARMACIST field (#11)
- DRUG EXPIRATION DATE field (#12)

PRESCRIPTION file (#52) – ACTIVITY LOG sub-file (#52.3)

The following change has been made to the ACTIVITY LOG sub-file (#52.3) of the PRESCRIPTION file (#52):

- The REASON field (#.02) will now include a new reason code, N:DISPENSE COMPLETION, which indicates the dispensing was completed by an external interface.

### Input Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following existing input template is updated:

- PSO SITE

# Installation of Patch 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This installation is comprised of the patches PSO\*7\*156, PSS\*1\*82, and PSN\*4\*84, and they should be installed in this order. Please read the following installation instructions carefully before beginning the installation.

> **NOTE:** There are several tasks you must complete following installation should you choose to turn on the interface; thus, the patches may be installed, but are not implemented until all of the steps are completed that will turn on the HL7 V. 2.4 standard interface.

If you are currently running an HL7 interface with Outpatient Pharmacy, there is no need to turn off the current interface during installation of PSO\*7\*156. Do not set up the new parameters until you are ready to implement the new interface.

## Installing PSO\*7\*156

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The suggested time to install is during non-peak Pharmacy hours. There should be no Outpatient Pharmacy users on the system, and Outpatient Pharmacy orders should not be acted upon through CPRS.

Installation will take less than 5 minutes.

To install PSO\*7\*156:

1.  Use the *INSTALL/CHECK MESSAGE* option on the *PackMan* menu.
2.  Review your mapped set. If the routines are mapped, they should be removed from the mapped set at this time.
3.  From the *Kernel Installation & Distribution System* menu, select the *Installation* menu.
4.  From this menu, the installer may select to use the following options:  
    (when prompted for INSTALL NAME, enter PSO\*7.0\*156)
    1.  *Backup a Transport Global* - This option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.
    2.  *Compare Transport Global to Current System -* This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
    3.  *Verify Checksums in Transport Global* - This option will ensure the integrity of the routines that are in the transport global.
5.  Use the *Install Package(s)* option and select the package PSO\*7.0\*156.
6.  When prompted "Want KIDS to INHIBIT LOGONs during the install? YES//" respond NO.
7.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//" respond NO.
8.  If Routines were unmapped as part of step 2, they should be returned to the mapped set once the installation has run to completion.

Example of PSO\*7\*156 Installation

Select Installation Option: INstall Package(s)

Select INSTALL NAME: PSO\*7.0\*156 Loaded from Distribution 2/23/04@14:36:

28

=\> PSO\*7\*156

This Distribution was loaded on Feb 23, 2004@14:36:28 with header of

PSO\*7\*156

It consisted of the following Install(s):

PSO\*7.0\*156

Checking Install for Package PSO\*7.0\*156

Install Questions for PSO\*7.0\*156

Incoming Files:

52 PRESCRIPTION (Partial Definition)

> **NOTE:** You already have the 'PRESCRIPTION' File.

59 OUTPATIENT SITE (Partial Definition)

> **NOTE:** You already have the 'OUTPATIENT SITE' File.

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\>

Install Started for PSO\*7.0\*156 :

Feb 23, 2004@14:37:20

Build Distribution Date: Feb 23, 2004

Installing Routines:

Feb 23, 2004@14:37:20

Installing Data Dictionaries: .

Feb 23, 2004@14:37:21

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing HL LOGICAL LINK

Installing HL7 APPLICATION PARAMETER

Installing PROTOCOL

Feb 23, 2004@14:37:21

Updating Routine file...

PSO\*7.0\*156

────────────────────────────────────────────────────────────────────────────────

The following Routines were created during this install:

PSOXZA

PSOXZA1

PSOXZA2

Example of PSO\*7\*156 Installation (continued)

PSOXZA3

PSOXZA4

PSOXZA5

PSOXZA6

PSOXZA7

PSOXZA8

Updating KIDS files...

PSO\*7.0\*156 Installed.

Feb 23, 2004@14:37:21

Install Message sent \#1475

Install Completed

# ## Installing PSS\*1\*82

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can be on the system at the time of installation. The only recommendation for installing this is patch is that none of the following options are being used at the time of installation:

- *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option
- *Synonym Enter/Edit* \[PSS SYNONYM EDIT\] option

Installation will take less than 5 minutes.

To install PSS\*1\*82:

1.  Use the *INSTALL/CHECK MESSAGE* option on the *PackMan* menu.
2.  Review your mapped set. If the routines are mapped, they should be removed from the mapped set at this time.
3.  From the *Kernel Installation & Distribution System* menu, select the *Installation* menu.
4.  From this menu, the installer may select to use the following options:  
    (when prompted for INSTALL NAME, enter PSS\*1.0\*82)
    1.  *Backup a Transport Global* - This option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.
    2.  *Compare Transport Global to Current System -* This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
    3.  *Verify Checksums in Transport Global* - This option will ensure the integrity of the routines that are in the transport global.
5.  Use the *Install Package(s)* option and select the package PSS\*1.0\*82.
6.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//" respond NO.
7.  When prompted "Want KIDS to INHIBIT LOGONs during the install? YES//" respond NO.
8.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//" respond NO.
9.  If Routines were unmapped as part of step 2, they should be returned to the mapped set once the installation has run to completion.

Example of PSS\*1\*82 Installation

Select Installation Option: INstall Package(s)

Select INSTALL NAME: PSS\*1.0\*82 Loaded from Distribution 5/26/04@16:20:27

=\> PSS\*1\*82

This Distribution was loaded on May 26, 2004@16:20:27 with header of

PSS\*1\*82

It consisted of the following Install(s):

PSS\*1.0\*82

Checking Install for Package PSS\*1.0\*82

Install Questions for PSS\*1.0\*82

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\>

Install Started for PSS\*1.0\*82 :

May 26, 2004@16:20:46

Build Distribution Date: May 26, 2004

Installing Routines:

May 26, 2004@16:20:46

PSS\*1.0\*82

────────────────────────────────────────────────────────────────────────────────

Installing PACKAGE COMPONENTS:

Installing HL7 APPLICATION PARAMETER

Installing PROTOCOL

Installing OPTION

May 26, 2004@16:20:47

Updating Routine file...

Updating KIDS files...

PSS\*1.0\*82 Installed.

May 26, 2004@16:20:47

Install Message sent \#1621

───────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

## Installing PSN\*4\*84

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch can be installed when users are not using the National Drug File package. There are no scheduling restrictions or recommendations for this patch.

Installation will take less than 5 minutes.

To install PSN\*4\*84:

1.  Use the *INSTALL/CHECK MESSAGE* option on the *PackMan* menu.
2.  Review your mapped set. If the routines are mapped, they should be removed from the mapped set at this time.
3.  From the *Kernel Installation & Distribution System* menu, select the *Installation* menu.
4.  From this menu, the installer may select to use the following options:  
    (when prompted for INSTALL NAME, enter PSN\*4.0\*84)
    1.  *Backup a Transport Global* - This option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.
    2.  *Compare Transport Global to Current System -* This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
    3.  *Verify Checksums in Transport Global* - This option will ensure the integrity of the routines that are in the transport global.
5.  Use the *Install Package(s)* option and select the package PSN\*4.0\*84.
6.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//" respond NO.
7.  When prompted "Want KIDS to INHIBIT LOGONs during the install? YES//" respond NO.
8.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//" respond NO.
9.  If Routines were unmapped as part of step 2, they should be returned to the mapped set once the installation has run to completion.

Example of PSN\*4.0\*84 Installation

Select Installation Option: INstall Package(s)

Select INSTALL NAME: PSN\*4.0\*84 Loaded from Distribution 4/16/04@20:23:3

6

=\> PSN\*4\*84

This Distribution was loaded on Apr 16, 2004@20:23:36 with header of

PSN\*4\*84

It consisted of the following Install(s):

PSN\*4.0\*84

Checking Install for Package PSN\*4.0\*84

Install Questions for PSN\*4.0\*84

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\>

Install Started for PSN\*4.0\*84 :

Apr 16, 2004@20:23:53

PSN\*4.0\*84

───────────────────────────────────────────────────────────────────────────────

Build Distribution Date: Apr 16, 2004

Installing Routines:

Apr 16, 2004@20:23:53

Installing PACKAGE COMPONENTS:

Installing OPTION

Apr 16, 2004@20:23:53

Updating Routine file...

Updating KIDS files...

PSN\*4.0\*84 Installed.

Apr 16, 2004@20:23:53

Install Message sent \#1596

───────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Informational Patch PSO\*7\*522 was implemented in March 2019 to remove the reference of VIE to Health Connect for HL7 messaging.

## Setting up the Mail Group for HL7 Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the mail group for HL7 alerts does not already exist, the facility will need to set up the V*IST*A Mail Group to receive the HL7 alerts if there is a problem with an HL7 message. This can be done in the *HL7 Main Menu* \[HL MAIN MENU\] option, *Site Parameter Edit* \[HL EDIT COMM SERVER PARAMETERS\] option and adding a mail group to the "Mail Group for Alerts: " prompt.

Example: Setting up a Mail Group

Select OPTION NAME: HL7 MAIN MENU HL7 Main Menu

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

Select HL7 Main Menu Option: Site Parameter Edit

Edit HL7 Site Parameters Page 1 of 2

------------------------------------------------------------------------------

Current Domain: VISTA.MED.VA.GOV

Current Institution: BIRMINGHAM, AL.

Is this a Production or Test Account? PRODUCTION

Mail Group for Alerts: MAILGROUPNAME

System Link Monitor VIEWS

-------------------------

\[Goto next page to edit Background Process Parameters\]

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Save Press \<PF1\>H for help Insert

## # Section 2: Implementing the New Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation of the patch, there are several steps that you must complete before the interface is fully implemented. This section describes those steps, and provides all of the information that you need to get the new interface operational.

The steps are divided into these groups:

- Pre-implementation
- Performing the implementation

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-1-0-instal/003.png)

To implement the new interface, the software contained on the dispensing system will also need to be updated by the vendor. Implementation must be coordinated with the company’s representative that supports your dispensing system.

*(This page included for two-sided copying.)*

# Pre-Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you turn on the new interface, you should do the following:

- Complete the Implementation Worksheet
- Validate the DNS name for the dispensing system.
- Provide a list of Pharmacists and corresponding Internal File Numbers to populate the vendor system.
- Purge existing entries, if any, in the PHARMACY EXTERNAL INTERFACE file (#52.51).

## Completing the Implementation Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Implementation Worksheet, located in Appendix A of this guide, must be completed for each outpatient site that is attached to a dispensing system. Please keep a copy of this worksheet for your records. It may help solve problems that occur after the new interface is operational.

## Validating the Dispense DNS Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a site’s dispensing system DNS Name is not registered, or valid, HL7 messages will not pass through the Interface Engine to the dispensing system. You should first validate the dispensing system DNS name before proceeding with the implementation tasks.

To validate a site’s Dispense DNS Name for a dispensing system:

1.  Assign an IP address and domain name to the automated dispensing system (for example, birmoptifill.med.va.gov).
2.  Add the name to an active Domain Name Server (DNS) directory.
3.  Log on to the V*IST*A server at the operating system level.
4.  Attempt to ping the dispensing system using the new name (for example, ping birmoptifill.med.va.gov).

If pinging the dispensing system does not work, then the name is not properly entered on the DNS and therefore, the Interface Engine will not be able to locate the dispensing system.

If the dispensing system cannot be pinged, you can either log a Remedy ticket to get networking assistance or contact the National Help Desk.

## List of Pharmacist Names

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to implementation, the vendor system will need to be populated with the list of pharmacist names and the Internal Entry Number (IEN) in the NEW PERSON file (200). This information is used when the Dispensing System returns the Checking Pharmacist and Filling Person for each prescription. To get a list of names, you can generate a FileMan report. Once this list is available, you’ll need to work with your vendor to update their system accordingly

Example: List of Pharmacist Names and IENs (sorted by security key)

VA FileMan 22.0

Select OPTION: PRINT FILE ENTRIES

OUTPUT FROM WHAT FILE: NEW PERSON// \<Enter\>

SORT BY: NAME// KEYS

1 KEYS (multiple)

2 KEYSTROKES FROM LM WP

CHOOSE 1-2: 1 KEYS (multiple)

KEYS SUB-FIELD: .01 KEY

START WITH KEY: FIRST// PSORPH

GO TO KEY: LAST// PSORPH

WITHIN KEY, SORT BY:

FIRST PRINT FIELD: .01 NAME

THEN PRINT FIELD: W ?40,D0

THEN PRINT FIELD:

Heading (S/C): NEW PERSON LIST// \<Enter\>

STORE PRINT LOGIC IN TEMPLATE: \<Enter\>

START AT PAGE: 1// \<Enter\>

DEVICE: \<Select Device\>

NEW PERSON LIST SEP 3,2004 10:37 PAGE 1

NAME W ?40,D0

--------------------------------------------------------------------------------

KEY: PSORPH

OPPHARMACIST16,THREE 5

OPPHARMACIST31,THREE 17

OPPHARMACIST22,THREE 121

OPPHARMACIST20,THREE 541

OPPHARMACIST11,THREE 576

OPPHARMACIST25,THREE 622

OPPHARMACIST21,THREE 755

Select OPTION:

Example: List of Pharmacist Names and IENs (sorted by title)

VA FileMan 22.0

Select OPTION: PRINT FILE ENTRIES

OUTPUT FROM WHAT FILE: NEW PERSON// \<Enter\>

SORT BY: NAME// TITLE

START WITH TITLE: FIRST// PHAR

GO TO TITLE: LAST// PHARZ

WITHIN TITLE, SORT BY:

FIRST PRINT FIELD: .01 NAME

THEN PRINT FIELD: W ?30,D0

THEN PRINT FIELD: \<Enter\>

Heading (S/C): NEW PERSON LIST// \<Enter\>

STORE PRINT LOGIC IN TEMPLATE: \<Enter\>

START AT PAGE: 1// \<Enter\>

DEVICE: \<Select Device\>

...EXCUSE ME, HOLD ON...

NEW PERSON LIST SEP 3,2004 11:39 PAGE 1

NAME W ?30,D0

-------------------------------------------------------------------------------

TITLE: PHARMACIST

OPPHARMACIST1,THREE 923

OPPHARMACIST6,THREE 11290

OPPHARMACIST31,THREE 10556

TITLE: PHARMACY TECHNICIAN

OPPHARMTECH23,FIVE 11655

OPPHARMTECH32,FIVE 12123

Select OPTION:

## Purging Existing Entries in the PHARMACY EXTERNAL INTERFACE File (#52.51)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site has been using the previous version of the Outpatient Pharmacy External Interface, you should purge all entries in the PHARMACY EXTERNAL INTERFACE file (#52.51) before implementing the new interface. This can be done by using the *Purge External Batches* option within the *External Interface Menu*. This menu and option are locked with the PSOINTERFACE security key. The purge can be run with Pharmacy Users on the system.

You will want to run this option again 7-10 days after implementing, and subsequently on a regular basis to remove old information.

Example: Purging External Interface file

Select External Interface Menu Option: Purge External Batches

Enter cutoff date for purge: SEP 23,2004// (SEP 23, 2004)

Purge entries that were not successfully processed? NO// YES

Requested Start Time: NOW// (SEP 30, 2004@15:41:49)

# Performing the Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several steps that you must complete before the new interface is operational; these steps correspond directly to the items in the Implementation Worksheet, located in Appendix A. This section provides examples for each step and a place to track the completion status.

The following steps show how to set up parameters for a sample outpatient site, BHAM CLINIC.

If you do not have a copy of the completed Implementation Worksheet, stop!

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-1-0-instal/004.png)

Steps 1 – 12 must be completed for each outpatient site that is attached to a dispensing system.

For steps 2 through 9, you use the *Site Parameter Enter/Edit* \[PSO SITE PARAMETERS\] option on the *Maintenance (Outpatient Pharmacy)* \[PSO MAINTENANCE\] menu to set up the parameters for the selected Outpatient Site.

## Step 1: Stopping the Dispensing System Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are currently utilizing an HL7 interface, you are running the LLP1 Logical Link. This must first be turned off before the new link can be started. Use the *HL7 Main Menu* \[HL MAIN MENU\] option, and then select the *Filer and Link Management Options* \[HL MENU FILER LINK MGT\] menu. Selecting the *Start/Stop Links* \[HL START\] option lets you stop the currently running Logical Link.

Example: Stopping the Logical Link

Select OPTION NAME: HL7 MAIN MENU HL MAIN MENU HL7 Main Menu

Select HL7 Main Menu Option: FILER and Link Management Options

Select Filer and Link Management Options Option: SL Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: PSO LLP1

The LLP was last started on JUN 02, 2001 09:52:02.

Okay to shut down this job? YES

The job for the LLP1 Lower Level Protocol will be shut down.

Step 1 Completed: Yes No

## Step 2: Selecting the Outpatient Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select a site to which you want to apply the parameters. You must do this for each outpatient site that will send to an automated dispensing system.

Example: Selecting the Outpatient Site

Select Outpatient Pharmacy Manager Option: MAINTenance (Outpatient Pharmacy)

Select Maintenance (Outpatient Pharmacy) Option: SITE Parameter Enter/Edit

Select SITE NAME: BHAM CLINIC 500

Would you like to see all site parameters for this division? Y// NO

NAME: BHAM CLINIC//

Step 2 Completed: Yes No

## Step 3: Turning on the External Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Choose selection 1 through 4 to ensure that the orders are sent through the external interface, and choose the selection that best fits your site’s needs.

Example: Turning on the External Interface

*------------------Some options have been skipped to save room for the example--------------------*

EXTERNAL INTERFACE: ??

This field allows sites to alter the characteristics of the external

interface. The Set of Codes field has the following values:

0 - the external interface is off

1 - send all drugs to the external interface; print labels locally

2 - send all drugs to the external interface; don't print labels locally

3 - send only marked drugs to the external interface; don't print labels

locally

4 - send only marked drugs to external interface and print labels through

VistA.

Choose from:

0 INTERFACE TURNED OFF

1 SEND ALL ORDERS AND PRINT LABEL

2 SEND ALL ORDERS AND DON'T PRINT LABEL

3 SEND MARKED ORDERS AND DON'T PRINT

4 SEND MARKED ORDERS AND PRINT LABEL

EXTERNAL INTERFACE: 2 SEND ALL ORDERS AND DON'T PRINT LABEL

Step 3 Completed: Yes No

## Step 4: Setting up a Dispensing System Printer 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is an optional parameter. If defined, only prescriptions that have labels printed on the printer(s) defined will be sent to the dispensing system.

Example: Setting up a Dispensing System Printer

Select Outpatient Pharmacy Manager Option: MAINTenance (Outpatient Pharmacy)

*------------------Some options have been skipped to save room for the example--------------------*

Select DISPENSING SYSTEM PRINTER:?

Answer with DISPENSING SYSTEM PRINTER:

You may enter a new DISPENSING SYSTEM PRINTER, if you wish

This field identifies the name of the printer(s) that, when selected,

and the interface is in use, an HL7 message is generated to the dispensi

ng system.

Only printers are selectable.

Answer with DEVICE NAME, or LOCAL SYNONYM, or \$I, or VOLUME SET(CPU), or

SIGN-ON/SYSTEM DEVICE, or FORM CURRENTLY MOUNTED

Do you want the entire DEVICE List? N (No)

Select DISPENSING SYSTEM PRINTER: Printer 1Step 4 Completed: Yes No

## Step 5: Enabling the Automated Dispense Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To send HL7 messages using HL7 V. 2.4, set this parameter to 2.4.

Example: Setting the Automated Dispense Parameter

*------------------Some options have been skipped to save room for the example--------------------*

AUTOMATED DISPENSE: ??

This field will determine what version of the automated dispense machine

this site is running. If the machine is older than HL7 V.2.4, enter

letter O. If HL7 V.2.4 has been installed, enter 2.4.

Choose from:

0 Less than V2.4

2.4 HL7 V.2.4

AUTOMATED DISPENSE: 2.4

AUTOMATED DISPENSE: HL7 V.2.4

Step 5 Completed: Yes No

## Step 6: Setting the File Release Date/Time Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Set this parameter to 1 (YES) if you want the prescription to be released in V*IST*A once the release information is received from the dispensing system. Otherwise, set this parameter to 0 (NO).

Example: Setting the File Release Date/Time Parameter

*------------------Some options have been skipped to save room for the example--------------------*

FILE RELEASE DATE/TIME: ??

This field is used to indicate if the release date/time is to be filed for

the prescription dispensed by an external interface.

Choose from:

1 YES

FILE RELEASE DATE/TIME: 1 YES

Step 6 Completed: Yes No

## Step 7: Enabling Master File Updates for the DRUG File (#50)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Check with your vendor to determine if they can receive Master File Updates before you use this parameter.

Example: Enabling Master DRUG file (#50) Updates

*------------------Some options have been skipped to save room for the example--------------------*

ENABLE MASTER FILE UPDATE: ??

This field will determine if the automated dispense machines are ready to

receive HL7 V.2.4 messages.

Choose from:

N NO

Y YES

ENABLE MASTER FILE UPDATE: NOStep 7 Completed: Yes No

## Step 8: Setting the Dispense DNS Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must set this parameter to the Domain Name Server (DNS) name (or IP address) of the automated dispensing machine that is used for each outpatient site division. DO NOT use the name supplied in the example.

Example: Setting the Dispense DNS Name

*------------------Some options have been skipped to save room for the example--------------------*

DISPENSE DNS NAME: ??

THIS IS THE DNS NAME OF THE AUTOMATED DISPENSING MACHINE THAT IS USED FOR

THIS OUTPATIENT SITE DIVISION.

DISPENSE DNS NAME: dispensemachine1.vha.med.va.govStep 8 Completed: Yes No

## Step 9: Setting the Dispense DNS Port

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter identifies the port number associated with the automated dispensing machine, which is identified by the DISPENSE DNS NAME. This is a free-text field and is different for each site.

Example: Setting the Dispense DNS Port

*------------------Some options have been skipped to save room for the example--------------------*

DISPENSE DNS PORT: ??

ENTER THE DNS PORT NUMBER ASSOCIATED WITH THE AUTOMATED DISPENSE MACHINE

FOR THIS OUTPATIENT PHARMACY SITE DIVISION.

DISPENSE DNS PORT: 1234Step 9 Completed: Yes No

## Step 10: Setting the Outpatient Pharmacy Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This must be set to PSO DISP. It is the Logical Link field (#2005) of the HL LOGICAL LINK file (#870).

Example: Setting the Outpatient Pharmacy Logical Link

*------------------Some options have been skipped to save room for the example--------------------*

LOGICAL LINK: ?

Top level link that will be used to exchange messages with an external

application. Answer with HL LOGICAL LINK NODE, or INSTITUTION, or DOMAIN, or

TCP/IP SERVICE TYPE

Do you want the entire 197-Entry HL LOGICAL LINK List? NO (No)

LOGICAL LINK: PSO DISPStep 10 Completed: Yes No

## Step 11: Setting up the Logical Link in HL7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To set up the logical link, facilities will need to access the new HL7 Logical Link, PSO DISP, from the *HL7 Main Menu* \[HL MAIN MENU\] option, *Interface Developer Options* \[HL MENU INTERFACE TK\] menu, *Link Edit* \[HL EDIT LOGICAL LINKS\] option. Then, you enter the IP address and port number (9300) of the Interface Engine located at the facility. The port number 9300 has been designated for the Interface Engine at all sites. Your IRM department should have this information, or use this link to determine the appropriate IP address for your facility:

<span class="mark">REDACTED</span>

To access this link, you must have access and be on the VA network.

Example: Setting up the Logical Link

Select OPTION NAME: HL7 Main Menu

Select HL7 Main Menu Option: Interface Developer Options

Select Interface Developer Options Option: EL Link Edit

Select HL LOGICAL LINK NODE: PSO DISP

HL7 LOGICAL LINK

--------------------------------------------------------------------------------

NODE: PSO DISP

INSTITUTION:

DOMAIN:

AUTOSTART: Enabled

QUEUE SIZE: 10

LLP TYPE: TCP \<Enter\>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

HL7 LOGICAL LINK

--------------------------------------------------------------------------------

┌──────────────────────TCP LOWER LEVEL PARAMETERS─────────────────────────┐

│ PSO DISP │

│ │

│ TCP/IP SERVICE TYPE: CLIENT (SENDER) │

│ TCP/IP ADDRESS: xx.x.xxx.xx │

│ TCP/IP PORT: 9300 │

│ │

│ │

│ ACK TIMEOUT: RE-TRANSMISION ATTEMPTS: 5 │

│ READ TIMEOUT: EXCEED RE-TRANSMIT ACTION: │

│ BLOCK SIZE: SAY HELO: │

│ │

│STARTUP NODE: PERSISTENT: │

│ RETENTION: UNI-DIRECTIONAL WAIT: │

└─────────────────────────────────────────────────────────────────────────┘

## ## The following is an example of the HL Logical Link Node:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: HL LOGICAL LINK NODE

NUMBER: 193 NODE: PSO DISP

LLP TYPE: TCP STATE: Enabled

AUTOSTART: Enabled TIME STARTED: FEB 05, 2004@08:25:27

SHUTDOWN LLP ?: NO QUEUE SIZE: 10

RE-TRANSMISSION ATTEMPTS: 5 TCP/IP ADDRESS: xx.x.xxx.xx

TCP/IP PORT: 9300 TCP/IP SERVICE TYPE: CLIENT (SENDER)

Step 11 Completed: Yes No

## Step 12: Starting the Dispensing System Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before messages can be sent through the new HL7 V. 2.4 external interface, the Logical Link you have set up must be started. Use the *HL7 Main Menu* \[HL MAIN MENU\] option, and then select the *Filer and Link Management Options* \[HL MENU FILER LINK MGT\] menu. Selecting the *Start/Stop Links* \[HL START\] option lets you start the Logical Link.

Example: Starting the Logical Link

Select OPTION NAME: HL7 MAIN MENU HL MAIN MENU HL7 Main Menu

Select HL7 Main Menu Option: FILER and Link Management Options

Select Filer and Link Management Options Option: SL Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: PSO DISP

The LLP is started.

Step 12 Completed: Yes No

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## Turning off the HL7 V. 2.4 Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In case of problems during the initial setup, you can back out the patch by turning off the new interface. You can switch from the HL7 V. 2.4 standard interface back to the previous HL7 interface. To do this, change the site parameter AUTOMATED DISPENSE to 0 (zero), and change the Logical Link back to the one used previously.

Example: Switching to the Previous HL7 Interface

AUTOMATED DISPENSE: 2.4//0

AUTOMATED DISPENSE: 0

*------------------Some options have been skipped to save room for the example--------------------*

LOGICAL LINK: PSO DISP// PSO LLP1

If you were running an older version of the HL7 Interface to a dispensing system, the vendor will need to restore their old software prior, if you find a need to revert due to implementation problems.

## Resetting the Dispense DNS Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 8 in the previous section instructs you in how to set up the Dispense DNS Name for the automated dispensing system at your site. You can use either the name or the IP address for the system. If the name does not work, change the Dispense DNS Name to the dispensing system’s IP address.

## Resetting the Dispensing System Logical Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installing and implementing, if you notice that orders are not being filled by the dispensing system, you may need to restart the Logical Link. Use the *HL7 Main Menu* \[HL MAIN MENU\] option, and then select the *Filer and Link Management Options* \[HL MENU FILER LINK MGT\] menu. First, stop the link. Then, use the same option to restart the PSO DISP link.

*(This page included for two-sided copying.)*

# # Appendix A: Implementation Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following worksheet should be completed in its entirety before implementing the new interface.NOTE: If you have multiple dispensing systems, this worksheet will need to be completed for each OUTPATIENT SITE file (#59) entry that is interfaced to a dispensing system.

## Setting up the Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Several new parameters have been created to support this project, and a modification was made to one of the existing site parameters. Determine the information needed to set your site’s parameters for each OUTPATIENT SITE entry before you install.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete all of the following for each outpatient site.

> 1: LOGICAL LINK RUNNING

> Are you currently using a prior HL7 interface to the dispensing system?

> YES \_\_\_\_\_ NO\_\_\_\_\_

> 2: OUTPATIENT SITE NAME:

> For each outpatient site that will send information to a dispensing system, you must set up all of the settings.

> Enter the name of the outpatient site: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 3:EXTERNAL INTERFACE

> This site parameter determines whether the OUTPATIENT SITE entry is interfaced to a dispensing system and how the interface will send drug information. It also determines how the information is sent and if it is printed or not. The EXTERNAL INTERFACE field (#5) in the OUTPATIENT SITE file (#59) includes five possible selections:

> 0 INTERFACE TURNED OFF

> 1 SEND ALL ORDERS AND PRINT LABEL

> 2 SEND ALL ORDERS AND DON'T PRINT LABEL

> 3 SEND MARKED ORDERS AND DON'T PRINT

> 4 SEND MARKED ORDERS AND PRINT LABEL

> Enter the setting you want to use for this parameter: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 4: DISPENSING SYSTEM PRINTER

> This is an optional parameter.

> If it is not defined, information for all prescriptions within the OUTPATIENT SITE entry will be sent to the interface based on the setting of the EXTERNAL INTERFACE field (#5) in the OUTPATIENT SITE file (#59).

> If one or more printers are entered in this new parameter, the release of information to the dispensing system is further restricted and will only send information when the printer(s) defined here are selected to print the label.

> Select from a list of available printers (for example, Printer 1).

> Enter the setting you want to use for this parameter: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 5: AUTOMATED DISPENSE

> This new site parameter determines what version of HL7 is used for the message formats sent to and from the dispensing system. This field must be set to 2.4 to implement the new interface.

> If the new interface has not been implemented yet, this field should be left blank. Selections include:

> 0 = older versions of HL7

> 2.4 – HL7 V. 2.4

> Enter the setting you want to use for this parameter: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 6: FILE RELEASE DATE/TIME

> This new site parameter determines whether or not the site wants to file the release date/time of the prescription when the dispensing systems send back release information. V*IST*A will file the release date and time, and release the prescription automatically. The available selections are:

> 0= NO

> 1=YES

> If it is set to 0 (NO), you must manually release prescriptions automatically. If it is set to 1 (YES), V*IST*A will automatically release the prescriptions.

> Enter the setting you want to use for this parameter: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 7: ENABLE MASTER FILE UPDATE

> This site parameter allows the dispensing system to receive master file updates for the DRUG file (#50). The new ENABLE MASTER FILE UPDATE field (#105.2) in the OUTPATIENT SITE file (#59) provides these selections:

> N= NO

> Y=YES

> Note: At the time of release of the Outpatient Pharmacy Automation Interface enhancement, none of the dispensing systems were using the Master File Updates. Sites should not turn on this parameter unless they ensure that the commercial dispensing system is ready to receive and acknowledge updates to the DRUG file (#50).

> Enter the setting you want to use for this parameter: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 8: DISPENSE DNS NAME

> This new site parameter identifies the Domain Name Server (DNS) name (or the IP address) used by the automated dispensing system for each outpatient site division. The new DISPENSE DNS NAME field (#2006) in the OUTPATIENT SITE file (#59) is a free-text field. You will need to enter the DNS name of the automated dispensing machine in this format:

> name.domain

> Enter the setting you want to use for this parameter \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 9: DISPENSE DNS PORT

> This new site parameter identifies the port number associated with the automated dispensing machine, which is identified by the DISPENSE DNS NAME. The new DISPENSE PORT NUMBER field (#2007) in the OUTPATIENT SITE file (#59) is a free-text field, and lets you enter the port number of the automated dispensing machine associated with the OUTPATIENT SITE entry.

> Enter the setting you want to use for this parameter: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 10: Outpatient Pharmacy LOGICAL LINK

> This site parameter lets you set the top-level link that is used to exchange messages with an external interface. This is the Logical Link field (#2005) of the HL LOGICAL LINK file (#870). If you are currently running an HL7 interface, the Outpatient Pharmacy Logical Link is PSO LLP1. The new Outpatient Pharmacy Logical Link for the HL7 V. 2.4 standard interface is PSO DISP.

> The new Outpatient Pharmacy Logical Link for the HL7 V. 2.4 standard interface is PSO DISP.

> Enter the setting you want to use for this parameter: \_\_\_\_\_\_<u>PSO DISP</u>

> 11: HL7 LOGICAL LINK

> This parameter provides the link from V*IST*A to the site’s Health Connect. This is done through the *HL7 Main Menu* \[HL MAIN MENU\] option.

> You must have access to and be on the VA network to access this document.

> Use the IP address that corresponds to your facility.

> The DNS Port number for the Health Connect is 9300.

> Enter the setting you want to use for this parameter: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## > 12: HL7 Logical Link On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The new logical link can be turned on after all changes have been made to the settings.

> Are you ready to turn the external interface YES \_\_\_\_\_ NO\_\_\_\_\_

## ## Implementation Worksheet — Steps Completed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You have completed the Implementation Worksheet, and can now provide the information to the person responsible for implementing the external interface for the Outpatient Pharmacy Automation Interface project.

Complete this worksheet for all Outpatient Site entries that will use the interface.

*(This page included for two-sided copying.)*