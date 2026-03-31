---
title: Clinical Procedures Outbound Admissions, Discharges, Transfers (ADT) Feed Guide
doc_type: INT
doc_label: Interface Feed Guide
doc_layer: plain
doc_subject: 
app_code: MD
app_name: Clinical Procedures
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - strong
  - class
  - even
  - clinical
  - flowsheets
  - table
  - contents
  - link
  - service
  - feed
page_count: 0
word_count: 10388
section_count: 17
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/cp_flows.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/ClinProc/cp_flows.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=139"
---

![](clinical-procedures-outbound-admissions-discharges-transfers-adt-feed-guide/001.png)

CLINICAL PROCEDURES (CP) V1.0MD\*1.0\*12FLOWSHEETS MODULEOUTBOUND ADMISSIONS, DISCHARGES, TRANSFERS (ADT) FEED GUIDE

November 2011

Office of Information & Technology (OI&T)

Product Development (PD)

Revision History

|                                       |          |                                    |
|---------------------------------------|----------|------------------------------------|
| Description                       | Date | Author                         |
| Updates to sections 2, 3 and 4        | 11-08-11 | <span class="mark">REDACTED</span> |
| Updates to Introduction and section 2 | 11-08-11 | <span class="mark">REDACTED</span> |
|                                       |          |                                    |
|                                       |          |                                    |

*This page intentionally left blank for double-sided printing.*

Table of Contents

*This page intentionally left blank for double-sided printing.*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
    - [The CP Gateway Service ADT System](#the-cp-gateway-service-adt-system)
    - [CP Console/ADT Feed Configuration](#cp-consoleadt-feed-configuration)
  - [Using This Document](#using-this-document)
  - [How Much or What Do I Need to Install?](#how-much-or-what-do-i-need-to-install)
- [Preinstallation](#preinstallation)
  - [Installation Prerequisites](#installation-prerequisites)
  - [General MD\1.0\16 Installation Flow](#general-md1016-installation-flow)
  - [Obtaining the Clinical Flowsheets Installation Files](#obtaining-the-clinical-flowsheets-installation-files)
  - [System Requirements](#system-requirements)
  - [Other Considerations](#other-considerations)
- [Installing the KIDS Build](#installing-the-kids-build)
- [Post-KIDS Configuration](#post-kids-configuration)
  - [Configuring User Roles by Assigning Menu Options and Keys](#configuring-user-roles-by-assigning-menu-options-and-keys)
  - [Creating a Service Account for CP Gateway Service](#creating-a-service-account-for-cp-gateway-service)
  - [Configuring the Inbound HL7 Feed](#configuring-the-inbound-hl7-feed)
  - [Configuring the PROTOCOL File for Outbound ADT Feed](#configuring-the-protocol-file-for-outbound-adt-feed)
  - [Step 4: Configuring the outbound ADT Feed](#step-4-configuring-the-outbound-adt-feed)
- [Installing the CP Console Client](#installing-the-cp-console-client)
  - [CP Console](#cp-console)
  - [Backout Plan](#backout-plan)
- [CP Gateway Service](#cp-gateway-service)
  - [Step 5: Configuring ADT Feed Subscriptions in the CP Console application.](#step-5-configuring-adt-feed-subscriptions-in-the-cp-console-application)
- [FAQ](#faq)
- [Glossary](#glossary)
This guide is derived from the *Clinical Procedures (CP) V1.0 Flowsheets Module Installation Guide* for Patch 16, a formerly released patch. The focus and intent is to assist the user with installation and configuration of the ADT Feed for Patch 12. References to Patch 16 are not applicable and can be ignored.
This *Clinical Procedures (CP) Flowsheets Module Outbound Admissions, Discharge, Transfer (ADT) Feed Guide* provides information for Information Resource Management (IRM) personnel to install and configure the components necessary for the implementation of the Clinical Flowsheets Admissions/Discharges/Transfers (ADT) Feed.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Flowsheets patch of the CP package provides an electronic representation of the traditional paper flowsheet maintained during each inpatient stay. Vitals, Intake/Output, Wound Documentation, etc., are examples of data types that can be recorded via Clinical Flowsheets into the Veterans Health Information System and Technology Architecture (VistA) system. Clinical Flowsheets provides a departure from its predecessor applications by storing collected information as discrete data. Other Clinical Flowsheets functionality includes its use of HL7 messaging and the CP Gateway service to notify the medical device of a patient’s ADT transaction. This aspect of the Clinical Flowsheets ADT functionality is the focus of this documentation.

### The CP Gateway Service ADT System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Gateway Service consists of two “parts”, VistA Server software and Graphical User Interface (GUI) software. The CP Gateway Service ADT software distributed within patch MD\*1.0\*16 allows Clinical Procedures to notify other systems when a patient movement occurs. This notification occurs via HL7 messaging and allows other devices to maintain patient databases with up to date inpatient data.

As part of patch MD\*1.0\*16, CP is distributing a subscriber protocol (MD DGPM PATIENT MOVEMENT). This protocol is registered as a subscriber to the Patient Information Management System (PIMS) event publisher protocol DGPM MOVEMENT EVENTS. When notified of a patient movement, MD DGPM PATIENT MOVEMENT stores information relevant to the patient movement in the CP_MOVEMENT_AUDIT file (#704.005).

After this information is stored in the CP_MOVEMENT_AUDIT file it is used to generate an appropriate ADT message. This message is then submitted to the HL7 system, which uses dynamic routing to determine to which logical link(s) the ADT message should be sent.

The following three items require configuration for the ADT feed (event handling system) to work.

- CP Console/ADT Feed
- PROTOCOL file (#101)
- HL7

### CP Console/ADT Feed Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Console provides the tools to build the flowsheet views and layouts that are used in inpatient settings for patient care, for recording vital statistics as necessary. It also provides a means for configuring the CP Gateway, configuring the CP ADT Feed, assigning permissions to CP Flowsheets users, and system administration.

For more information about CP Console, refer to the *CP Flowsheets Module Implementation Guide*.

## Using This Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document guides the reader through a very specific order for installing and configuring the Clinical Flowsheets’ Outbound ADT Feed (i.e. the CP Flowsheets ADT Feed). This section of the guide will explain the reasoning for that order.

It is recommended that you follow this order because steps described in the later chapters are dependent upon certain previous steps.

Chapter 2. Preinstallation: This chapter lists installation prerequisites. Please install the specified patches and/or packages before attempting to install Clinical Flowsheets.

Chapter 2 also describes where you can download the files needed to install Clinical Flowsheets.

Chapter 3. Installing the KIDS Build: This chapter provides a screen capture of the KIDS build installation process.

Chapter 4. Post-KIDS Configuration: This chapter contains instructions for system and user configuration that occurs in VistA.

Chapter 5. Installing the CP Console Client: The chapter describes how to install the CP Console application.

Chapter 6. Testing the CP ADT Feed: This chapter contains some testing procedures which may be implemented to verify the CP ADT Feed is working as designed.

Chapter 7. FAQ: This chapter contains answers to frequently asked questions concerning the CP ADT Feed.

Chapter 8. Glossary

## How Much or What Do I Need to Install?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Depending on your purposes for installing MD\*1.0\*16, you may not need to install all of the components described in this Installation Guide. Please follow these guidelines for determining which components you should install:

- If the site is not currently running Clinical Procedures, only the KIDS build needs to be installed. All other installation instructions and post-installs can be ignored.
- If the site is running Clinical Procedures and does not plan on implementing Clinical Flowsheets at this time, only the KIDS and CP Console (replacement for the current CP Manager) needs to be installed. Sites with the KIDS and CP Console installed will be able to implement the CP Outbound ADT Feed.
- If the site is running Clinical Procedures and wishes to begin the implementation of Clinical Flowsheets, then all four components need to be installed: KIDS, CP Console, CP Flowsheets and the new CP Gateway Service. Sites with the KIDS, CP Console, CP Flowsheets and the new CP Gateway Service installed will be able to implement the CP ADT Feed.
- Note: the CP Manager application is no longer supported after the installation of MD\*1.0\*16. Use CP Console to perform the functions previously provided by CP Manager.

*This page intentionally left blank for double-sided printing.*

# Preinstallation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **IMPORTANT:** Installation of MD\*1.0\*16 is a prerequisite for MD\*1.0\*12. Content in this document is based on the assumption that you already have MD\*1.0\*16 installed. In addition, installation of MD\*1.0\*12 is mandatory for all sites that are implementing CP Flowsheets.

## Installation Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Clinical Flowsheets Outbound ADT Feed cannot be installed as a stand-alone application without Clinical Procedures (CP). If this is a first-time installation, you must first install the CP package and released CP patches. For more information on installing CP, refer to the *CP Flowsheets Module Installation Guide*.
- Although packaged separately, Clinical Flowsheets is part of the Clinical Procedures patch, MD\*1.0\*16. Thus, Clinical Flowsheet functionality, including the Outbound ADT Feed, cannot be installed without the Clinical Procedures application. If you do not have the Clinical Procedures (CP) package and all released CP patches prior to MD\*1.0\*16 are not installed, you must install them.
- Vitals Patch GMRV\*5.0\*22, GMRV\*5.0\*23 and CP patches MD\*1.0\*21 and MD\*1\*16 must be installed prior to the installation of patch MD\*1.0\*12.
- Coordinate the installation with the Nursing Automated Data Processing Application Coordinator (ADPAC), Medicine ADPAC, Information Resource Management Service (IRMS) and if applicable at your site, the Clinical Application Coordinator (CAC).

## General MD\*1.0\*16 Installation Flow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following flow diagram illustrates an overview of the basic flow of the MD\*1.0\*16 Installation which is the prerequisite for installing MD\*1\*12.

> **NOTE:** The CP Flowsheets GUI does not have to be installed if Flowsheets are not going to be used. The CP Console GUI must be installed to use the ADT Feed.

![](clinical-procedures-outbound-admissions-discharges-transfers-adt-feed-guide/002.png)

Figure 2‑1, Installation Flow

## Obtaining the Clinical Flowsheets Installation Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three distribution files that are used to install the three Clinical Flowsheets components (CP Gateway Service, CP Console, and CP Flowsheets). There is also a configuration file containing the default views. The distribution files are available for download from the Anonymous directories.

File Transfer Protocol (FTP) Instructions:

The file listed in section 5.1 may be obtained via FTP. The preferred method is to FTP the files from:

download.vista.med.va.gov

This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

CIO FIELD OFFICE FTP ADDRESS DIRECTORY

---------------- ------------------------- --------------------

<span class="mark">REDACTED</span>

<u>IT IS ASSUMED THAT ALL OF THE FILES AND DOCUMENTS FOR MD\*1\*16 WERE PREVIOUSLY INSTALLED OR READ PRIOR TO INSTALLING MD\*1\*12. MD\*1\*16 WAS RELEASED NATIONALLY IN JULY, 2011.</u>

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Storage requirements for Clinical Flowsheets client installation:

| Type of Data | Size |
|------------------|----------|
| Applications     | \< 5MB   |
| Help Files       | \< 1MB   |

Sites should reserve 1KB of storage space per observation for data that will accumulate. The vast majority of growth will occur in the OBS file (#704.117).

The following describes the installation environment for Clinical Flowsheets on the VistA client workstation:

- Workstations must be running under Windows XP Professional. Refer to <http://vaww.vairm.vaco.va.gov/vadesktop> for additional information on VA standard desktop configurations.
- Remote Procedure Call (RPC) Broker Workstation must be installed.
- The Clinical Context Object Workgroup (CCOW) runtime from Sentillion must be installed if CCOW functionality is desired. Please see your Information Resource Management (IRM) representative for the installation of CCOW.
- The workstation must be connected to the local area network.
- Administrator privileges are needed on any machine on which CP Gateway Service is installed

> Setting up the Global Placement

Create, place, and set the journaling option for the global ^MDC on the volume set. This is a new global released with the Clinical Flowsheets patch, so this step should be coordinated with the VistA systems manager to avoid default locations and settings being applied to this global.

## Other Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Sites are recommended to install the software in test accounts prior to installing it in production accounts.
- Refer to the MD\*1\*16 Patch for information on verifying the KIDS build checksum before installing Clinical Flowsheets.
- MD\*1\*16 was released under a regular mandate. However, there is no mandatory date to implement it. A site can implement Clinical Procedures Flowsheets at will.
- This patch can be loaded with users on the system. Installing MD\*1\*16 will not affect any users on the system, including those using the pre-patch 16 Clinical Procedures system.
- Installation time is less than five minutes.

> Note: the time required to complete the post-install and to receive the MailMan message will vary depending on your system load.

- Installation of this patch should NOT BE QUEUED.
- Suggested time to install: non-peak requirement hours.
- The CP Console and CP Flowsheets components may be installed locally on individual workstations or remotely on a server that is operating 24/7.
- The CP Manager application is no longer supported after the installation of MD\*1\*16. Use CP Console to perform the functions previously provided by CP Manager.

# Installing the KIDS Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is assumed that the Kids Build for MD\*1\*16 has been installed due to the release in July, 2011. For instructions on Installing MD\*1\*12, please refer to the MD_1_12_Description.rtf document or MD_1_12_RN.docx (release notes).

> **NOTE:** If your site does not plan to implement Clinical Flowsheets and is installing MD\*1.0\*16 only because it is mandated to do so, you are not required to do anything beyond installing the KIDS build.

*This page intentionally left blank for double-sided printing.*

# Post-KIDS Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you begin using Clinical Flowsheets:

1.  Create a Service Account for the CP Gateway Service.
2.  Configure the user roles by assigning menu options and keys.

> **NOTE:** Items 3 – 6 are required only for sites using the CP Gateway Service for interfacing with devices for device inbound data. Sites that will use the Clinical Flowsheets package only for manual entry should only be concerned with items 1 and 2.

3.  Configure the inbound HL7 feed.

> **NOTE:** If you are not going to be implementing Flowsheets, ignore step 4. If you have implemented CP Legacy and you are not implementing Flowsheets, continue with steps 5-7.

4.  Configure the PROTOCOLs.

> **NOTE:** This step may be by-passed if no inbound devices are used.

5.  Configure the outbound Admission Discharge and Transfer (ADT) link and PROTOCOLs.
6.  Configure the outbound ADT subscriptions.

## Configuring User Roles by Assigning Menu Options and Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In VistA, assign each Clinical Flowsheets user (including the service account CP Gateway user, created above) the CliO Service Options \[MD CLIO\] option as a secondary menu option. See section 4.2, step 1 for details about configuring the CP Gateway.
1.  In VistA, give Clinical Flowsheets managers the MD MANAGER and MD ADMINISTRATOR keys. The following are other available CP Flowsheets user keys, along with a description:

    MD ADMINISTRATOR: This key gives the user complete access to all functions in CP Console and CP Flowsheets. Without this key, the user relies on permissions assigned to in CP Console. This user is typically an IRM or a Super CAC.

    MD MANAGER: This key gives the user rights to edit, audit, and rescind observations entered by other users. This key also gives rights to import views into CP Console. This user is typically a Nurse Manager or CAC.

    MD HL7 MANAGER: CP Flowsheets requires the VistA MD HL7 MANAGER role or the MD ADMINISTRATOR role to access the HL7 Monitor. Assign this role to a user who will assist with the HL7 messaging component of CP Flowsheets. Users having this key will be able to update the CP ADT Feed Configuration via CP Flowsheets’ CP Console application.

    MD READ-ONLY: Assign this role to a user to prevent them from entering data in Flowsheets. DO NOT assign MD READ-ONLY to a user concurrently with any role other than MD HL7 MANAGER. Doing so will lead to unpredictable results. A user with the MD READ-ONLY key may NOT log on to CP Console and will have limited functionality in CP Flowsheets.

    MD TRAINEE: Data entered into CP Flowsheets by a user with the MD TRAINEE key does not display on the flowsheet until it has been verified (on the Log Files tab) by any user who was not assigned the MD TRAINEE key.

> **NOTE:** If your site is going to ONLY use CP Flowsheets and not the CP Gateway Service, you can stop after section 4.1; section 4.2 is not required. Also, if the site is going to ONLY use the ADT Feed and not CP Flowsheets, you can stop after section 4.1; section 4.2 is not required.

## Creating a Service Account for CP Gateway Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You will need to create a generic account for the CP Gateway Service to use for connections to VistA.

The CP Gateway Service uses the RPC Broker to communicate with the VistA server and therefore, requires an access code/verify code pair to connect.

1.  Assign this new service account RPC Broker Context for CP Gateway \[MDCP Gateway Context\] option as a secondary menu option ONLY and do not assign any primary menu so that interactive access will not be allowed for this account.
2.  Create a service account in the NEW PERSON file (#200) with access and verify codes. The first name should be USER and the last name CPGATEWAY. Ensure that the VERIFY CODE NEVER EXPIRES flag is SET for this user.

> **NOTE:** Use FileMan or the ADD a New User option.

- NAME: CPGATEWAY, USER
- INITIAL: UC
- ACCESS CODE: *Determined locally by IRM*
- VERIFY CODE: *Determined locally by IRM*
- XUS Active User: YES
- SERVICE/SECTION: *Determined locally by IRM.*
- SECONDARY MENU OPTION: MDCP GATEWAY CONTEXT

> The following screen capture details this procedure:

NAME: CPGATEWAY,USER INITIAL: UC

ACCESS CODE: \<Hidden\>

DATE VERIFY CODE LAST CHANGED: SEP 11,2007

VERIFY CODE: \<Hidden\> SEX: MALE

PREFERRED EDITOR: SCREEN EDITOR - VA FILEMAN

DATE ENTERED: APR 24, 2007 CREATOR: FLOWSHEETSCREATOR,ONE

SSN: 000000000

LAST SIGN-ON DATE/TIME: SEP 17, 2007@09:54:08

XUS Logon Attempt Count: 0 XUS Active User: Yes

Entry Last Edit Date: APR 24, 2007 TERMINAL TYPE LAST USED: C-VT100

NAME COMPONENTS: 200 SERVICE/SECTION: IRM FIELD OFFICE

SIGNATURE BLOCK PRINTED NAME: USER CPGATEWAY

SECONDARY MENU OPTION: MDCP GATEWAY CONTEXT

## Configuring the Inbound HL7 Feed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ICU devices forward observation data to VistA inside HL7 (ORU^R01) inbound messages.

1.  Review the settings for the MDHL IN logical link for correctness and compatibility with the local environment.
2.  Edit the MDHL logical link.

Select OPTION NAME: HL MAIN MENU HL7 Main Menu

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

HLO HL7 (Optimized) MAIN MENU ...

Select HL7 Main Menu Option: INterface Developer Options

EA Application Edit

EP Protocol Edit

EL Link Edit

VI Validate Interfaces

Reports ...

Select Interface Developer Options Option: EL Link Edit

Select HL LOGICAL LINK NODE: MDHL IN

HL7 LOGICAL LINK

-----------------------------------------------------------------------

NODE: MDHL IN

INSTITUTION:

MAILMAN DOMAIN:

AUTOSTART: Enabled

QUEUE SIZE: 100

LLP TYPE: TCP

DNS DOMAIN:

3.  Scroll down to the Lower Level Protocol (LLP) TYPE settings and press \<Enter\>. The TCP settings for this logical link display (Figure 4‑2).

![](clinical-procedures-outbound-admissions-discharges-transfers-adt-feed-guide/003.png)

Figure 4‑2, TCP/IP Service Type

4.  Set the Transmission Control Protocol/Internet Protocol (TCP/IP) SERVICE TYPE to SINGLE LISTENER.
5.  Set the TCP/IP PORT to the port number of the HL7 target used by the 3<sup>rd</sup> party devices.
6.  Set the TaskMan STARTUP NODE according to local requirements.
7.  Start the logical link (in the background).

Select HL7 Main Menu Option: FILER and Link Management Options

Select Filer and Link Management Options Option: START/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: MDHL IN

Job was queued as 924846.

## Configuring the PROTOCOL File for Outbound ADT Feed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** You only need to continue with the following steps if you are using ADT Outbound Messaging.

Patch MD\*1.0\*16 exports to the VistA server a subscriber protocol, MD DGPM PATIENT MOVEMENT, that must be added to the ITEM multiple of the DGPM MOVEMENT EVENTS entry in the PROTOCOL file (#101). This allows the CP ADT feed to receive notification that a patient was admitted, discharged, or transferred.

> **NOTE:** Ensure that logical links are started in the background, or it could take a long time to complete.

The following capture shows how to add MD DGPM PATIENT MOVEMENT to the ITEM multiple:

Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: PROTOCOL//

EDIT WHICH FIELD: ALL// ITEM

1 ITEM (multiple)

2 ITEM TEXT

CHOOSE 1-2: 1 ITEM (multiple)

EDIT WHICH ITEM SUB-FIELD: ALL//

THEN EDIT FIELD:

Select PROTOCOL NAME: DGPM MOVEMENT EVENTS MOVEMENT EVENTS v 5.0

Select ITEM: MD DGPM PATIENT MOVEMENT CliO DGPM patient movement interface

MD DGPM PATIENT MOVEMENT

MNEMONIC:

SEQUENCE:

MODIFYING ACTION:

FORMAT CODE:

DISPLAY NAME:

PROMPT:

DEFAULT:

HELP:

MODE:

Select ITEM:

Select PROTOCOL NAME:

## Step 4: Configuring the outbound ADT Feed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CP Flowsheets uses the VistA HL7 system to deliver ADT messages to vendor devices/servers. Therefore, you need to generate a subscriber PROTOCOL and logical link for each device to which Clinical Flowsheets sends an ADT message. Each developed subscriber PROTOCOL should use MDC ADT OUTBOUND XXX as the application and uses the IP address and port number of the vendor device/server in the logical link. ( note: XXX is the 3 letter vendor code – explained in detail later)

1.  Add a logical link.

Select OPTION NAME: HL MAIN MENU HL7 Main Menu

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

HLO HL7 (Optimized) MAIN MENU ...

Select HL7 Main Menu Option: Interface Developer Options

EA Application Edit

EP Protocol Edit

EL Link Edit

VI Validate Interfaces

Reports ...

Select Interface Developer Options Option: EL Link Edit

Select HL LOGICAL LINK NODE: MDSPL001 (Note: This is an example based on a Spacelabs device. The actual link node name may differ based on the site’s device type.)

Are you adding 'MDSPL001' as a new HL LOGICAL LINK (the 85TH)? No// Y (Yes)

HL7 LOGICAL LINK

-----------------------------------------------------------------------

NODE: MDSPL001

INSTITUTION:

MAILMAN DOMAIN:

AUTOSTART:

QUEUE SIZE: 10

LLP TYPE: TCP

DNS DOMAIN:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

HL7 LOGICAL LINK

-----------------------------------------------------------------------

┌──────────────────────TCP LOWER LEVEL PARAMETERS-──────────────────┐

│ MDSPL001 \|

│ \|

│ TCP/IP SERVICE TYPE: CLIENT (SENDER) │

│ TCP/IP ADDRESS: 127.0.0.1 (See note below.) │

│ TCP/IP PORT: 11223 (See note below.) │

│ TCP/IP PORT (OPTIMIZED): │

│ │

│ ACK TIMEOUT: RE-TRANSMISION ATTEMPTS: │

│ READ TIMEOUT: EXCEED RE-TRANSMIT ACTION: │

│ BLOCK SIZE: SAY HELO: │

│ │

│STARTUP NODE: PERSISTENT: │

│ RETENTION: UNI-DIRECTIONAL WAIT: \|

> **NOTE:** The TCP/IP address and port shown above should be replaced with those of *your site’s* medical device or the aggregating server of the medical device.

The following figure shows additional suggested values for the logical link:

![](clinical-procedures-outbound-admissions-discharges-transfers-adt-feed-guide/004.png)

Figure 4‑3, Logical Link Values

8.  Add a subscriber PROTOCOL using the HL EDIT INTERFACE Option Name.

> Each subscriber PROTOCOL requires a unique name. In order to ensure this uniqueness, rules are used when generating a new PROTOCOL name. As new vendors are added, likewise PROTOCOL vendor abbreviations will be added.

- The first two letters of the name of the PROTOCOL are MD.
- Two or three characters of the name are based on the vendor name.
- The last three characters are a serial number starting with 001.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Vendor Name</strong></th>
<th><strong>PROTOCOL Vendor Abbreviation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>General Electric.</td>
<td>GE</td>
</tr>
<tr class="even">
<td>Spacelabs</td>
<td>SPL</td>
</tr>
<tr class="odd">
<td>Philips</td>
<td>PHL</td>
</tr>
<tr class="even">
<td>Picis</td>
<td>PIC</td>
</tr>
<tr class="odd">
<td><p>Clinicomp</p>
<p>Nihon-khoden</p></td>
<td><p>CLI</p>
<p>NK</p></td>
</tr>
</tbody>
</table>

> Note: The above vendor abbreviations are specified for outbound ADT messages only—not inbound observation messages from third-party vendors. Not all vendors listed are necessarily interfaced with Clinical Flowsheets already.

> Example

> The PROTOCOL used with a Spacelabs device at a specific hospital is MDSPL001:

Select OPTION NAME: HL MAIN MENU HL7 Main Menu

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

HLO HL7 (Optimized) MAIN MENU ...

Select HL7 Main Menu Option: Interface Developer Options

EA Application Edit

EP Protocol Edit

EL Link Edit

VI Validate Interfaces

Reports ...

Select Interface Developer Options Option: EP Protocol Edit

Select PROTOCOL NAME: MDSPL001

Located in the MD (CLINICAL PROCEDURES) namespace.

Are you adding 'MDSPL001' as a new PROTOCOL? No// Y (Yes)

PROTOCOL ITEM TEXT: SPACELABS SERVER 1

PROTOCOL IDENTIFIER:

HL7 INTERFACE SETUP PAGE 1 OF 2

-----------------------------------------------------------------------

NAME: MDSPL001

DESCRIPTION (wp): (empty)

ENTRY ACTION:

EXIT ACTION:

TYPE: subscriber

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Enter a code from the list.

Choose from:

E event driver

S subscriber \<Edit the TYPE to be SUBSCRIBER

Press \<PF1\>H for help Insert

9.  Press \<Enter\>. Control is sent to the HL7 Subscriber edit screen.

HL7 SUBSCRIBER PAGE 2 OF 2

MDSPL001

-----------------------------------------------------------------------

RECEIVING APPLICATION: MDC ADT OUTBOUND xxx (See note below.)

RESPONSE MESSAGE TYPE: ACK EVENT TYPE:

SENDING FACILITY REQUIRED?: NO RECEIVING FACILITY REQUIRED?: NO

SECURITY REQUIRED?:

LOGICAL LINK: MDSPL001

PROCESSING RTN:

ROUTING LOGIC:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_Exit Save Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: E Press \<PF1\>H for help Insert

> **NOTE:** Once you enter the RECEIVING APPLICATION information (“MDC ADT OUTBOUND”), you will see the full list of vendors noted in Step 2 . The xxx in the above field screenshot indicates the vendor, which could be for example, “PHL” for Phillips.

10. Activate the logical link.

> **NOTE:** Both Link Manager and Task Manager must be running

Select OPTION NAME: HL MAIN MENU HL7 Main Menu

Event monitoring menu ...

Systems Link Monitor

Filer and Link Management Options ...

Message Management Options ...

Interface Developer Options ...

Site Parameter Edit

HLO HL7 (Optimized) MAIN MENU ...

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

Select Filer and Link Management Options Option: Start/Stop Links

This option is used to launch the lower level protocol for the

appropriate device. Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: MDSPL001

The LLP was last shutdown on DEC 12, 2007 15:02:01.

Select one of the following:

F FOREGROUND

B BACKGROUND

Q QUIT

Method for running the receiver: B// ACKGROUND

Job was queued as 3092973.

# Installing the CP Console Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## CP Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Console client application is released as part of Patch MD\*1.0\*16. The distribution file is available for download from the Anonymous directories. The patch distribution file name is MD1_0P16_EXES_AND_DOC.zip.

> **NOTE:** To configure the CP Gateway Service, you must install CP Console on the same server, before running CP Console to configure the CP Gateway Service.  However, if you are not using the CP Gateway Service to receive (inbound) data from a third party device, you do not have to install or configure the CP Gateway Service.

> **NOTE:** The CP Console Client will be used for outbound ADT configuration.

To install the CP Console client, complete the following steps:

1.  Extract the compressed ZIP file MD1_0P16_EXES_AND_DOC.zip. It includes the following files:
- CPConsole.exe
- CliO_Terminology.doc
- MD_1_P16_UM.doc
- MD_1_P16_IG.doc
- MD_1_P16_IMPG.pdf
- MD_1_P16_RN.pdf
- CLINPROC1_TM.pdf
- CPConsole.hlp
- CPConsole.cnt
- RoboEx32.dll
11. Distribute the CPConsole.exe file. If you are installing the application onto individual workstations, usually the CPConsole executable file is placed in the following directory: C:\Program Files\VistA\Clinical Procedures.

    If a remote installation is chosen (by storing the application executables on a network rather than locally), you must create a link that reflect the target path. This link can then be distributed (copied) to workstations.
12. The online Help files (files ending in .HLP and .CNT) and the .DLL file should go in a subdirectory of the folder where the executables are placed. Name this directory Help, for example C:\Program Files\VistA\Clinical Procedures\Help.
13. The CliO_Terminology.doc should go in a subdirectory of the folder where the executables are placed. Name this directory Documents, for example C:\Program Files\VistA\Clinical Procedures\Documents.

## Backout Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the complexity of the task step by step procedures for backing out the MD\*1.0\*16 and MD\*1\*12 patches are not provided here. To backout the installation, please create a Remedy Ticket or contact the Remedy Help Desk at <span class="mark">REDACTED</span>

*This page intentionally left blank for double-sided printing.*

.

# CP Gateway Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Gateway Service is released as part of Patch MD\*1.0\*16. The patch distribution file is available for download from the Anonymous directories. The patch distribution includes the setup file MD1_0P16CPGatewayServiceSetup.exe.

Notes:

- Per CP Outbound ADT Feed ONLY functionality, the CP Gateway Service is not applicable.
- A copy of the CP Console application MUST be installed on the same server as the CP Gateway Service in order to administer the CP Gateway Service. This is because the CP Gateway Service depends on information that is stored in the local system registry by the CP Console application.
- You can only have one copy of the CP Gateway Service installed on a server because the server manages the connection properties in the system registry. If you want to run a CP Gateway Service in TEST and PRODUCTION, you will need two servers.

To install the CP Gateway Service, complete the steps per section 6 of the CP Flowsheets Installation Guide (MD_1_P16_IG.doc).

## Step 5: Configuring ADT Feed Subscriptions in the CP Console application.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The dynamic routing system (ADT feed) must be configured, so that HL7 knows to which system to deliver the ADT messages.

1.  Log in to CP Console, using your access code/verify code pair.
14. Expand the CP Console tree view and click Parameters.
15. Select CP ADT Feed Configuration. The CP ADT Feed Configuration detail displays with a list of current ADT targets.

![](clinical-procedures-outbound-admissions-discharges-transfers-adt-feed-guide/005.png)

Figure 6‑1, CP ADT Feed Configuration

16. To add a new ADT target, click New. The Add ADT Target window displays.

![](clinical-procedures-outbound-admissions-discharges-transfers-adt-feed-guide/006.png)

Figure 6‑2, Add ATD Target

17. From the PROTOCOL list, select a subscriber PROTOCOL name (such as MDGE001 or MDSPL001)

    Note: Do not select any PROTOCOL names that start with MDC_ADT.
18. From the Division list, select either an entire division or a ward within a division. (This allows Clinical Flowsheets to filter outbound messages by patient location.)

    Note: If no device is configured to receive messages that are triggered by Registration-ADT events at a particular location, no outbound ADT is generated by CP Flowsheets.
19. In the PROTOCOL Link Name box, enter a name. We suggest following a naming convention that includes the PROTOCOL, the division, and the ADT event type (for example MDGE_SICU_A01)
20. From the HL7 Event Type drop-down, select an ADT outbound message type.
21. Click OK.  
      
    Repeat steps 4-9 for each HL7 event type you need to link. Contact [VA](mailto:VAOITOEDClinProcImplementationSupport@va.gov) OIT OED ClinProc Implementation Support if you need a list of which ADT events can be accepted.
- A01 Admit/visit notification
- A02 Patient transfer
- A03 Discharge/end visit
- A08 Update patient info
- A11 Cancel admission
- A12 Cancel transfer
- A13 Cancel discharge/end visit

  *This page intentionally left blank for double-sided printing.*

# FAQ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Question</strong></th>
<th><strong>How do I stop the CP Gateway Service?</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Response</strong></td>
<td><ol type="1">
<li><p>In Windows, click <strong>Start</strong> | <strong>Control Panel</strong> | <strong>Administrative Tools</strong> | <strong>Services</strong>. The Services window displays.</p></li>
</ol>
<ol start="22" type="1">
<li><p>Click the Clinical Procedures Gateway row. A link, <u>Stop</u> the service, displays.</p></li>
<li><p>Click <strong>Stop</strong>. A progress window displays as the service stops.</p></li>
<li><p>When the progress window closes, the Services window redisplays. The status column in the Clinical Procedures Gateway row displays <strong>Stopped</strong>.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>Question</strong></td>
<td><strong>How can I change the time interval for CP Console and CP Flowsheets at which they time out?</strong></td>
</tr>
<tr class="odd">
<td><strong>Answer</strong></td>
<td>The time interval is set using the TIMED READ value in the NEW PERSON file (#200).</td>
</tr>
<tr class="even">
<td><strong>Question</strong></td>
<td><strong>If our site is going to use the Outbound ADT Feed only, which components need to be installed?</strong></td>
</tr>
<tr class="odd">
<td><strong>Response</strong></td>
<td>If the site is not going to process inbound data from third party device, but will use outbound ADT messaging, the site will need to install the VistA patch MD*1*16 and the CP Console “exe”.</td>
</tr>
</tbody>
</table>

*This page intentionally left blank for double-sided printing.*

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This glossary is used for the Clinical Flowsheets project and may include terms and definitions not used in this specific document.
<table>
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
<td><strong>&lt;RET&gt;</strong></td>
<td>Carriage return.</td>
</tr>
<tr class="even">
<td><strong>Access Code</strong></td>
<td>A unique sequence of characters known by and assigned only to the user, the system manager and/or designated alternate(s). The access code (in conjunction with the verify code) is used by the computer to identify authorized users.</td>
</tr>
<tr class="odd">
<td><strong>Action</strong></td>
<td>A functional process that a clinician or clerk uses in the TIU computer program. For example, “Edit” and “Search” are actions. Protocol is another name for Action.</td>
</tr>
<tr class="even">
<td><strong>ADP</strong></td>
<td>Automated Data Processing</td>
</tr>
<tr class="odd">
<td><strong>ADP Coordinator/­ADPAC/­Application Coordinator</strong></td>
<td>Automated Data Processing Application Coordinator. The person responsible for implementing a set of computer programs (application package) developed to support a specific functional area such as clinical procedures, PIMS, etc.</td>
</tr>
<tr class="even">
<td><strong>ADT</strong></td>
<td>Advanced Data Type (InterSystems Cache). Also Admissions, Discharges, Transfers.</td>
</tr>
<tr class="odd">
<td><strong>AP</strong></td>
<td>Arterial pressure</td>
</tr>
<tr class="even">
<td><strong>API</strong></td>
<td>Application Programming Interface. An interface that a computer system, library, or application provides in order to accept requests for services from other programs, and/or to allow data to be exchanged between them.</td>
</tr>
<tr class="odd">
<td><strong>Application</strong></td>
<td>A system of computer programs and files that have been specifically developed to meet the requirements of a user or group of users.</td>
</tr>
<tr class="even">
<td><strong>Archive</strong></td>
<td>The process of moving data to some other storage medium, usually a magnetic tape, and deleting the information from active storage in order to free-up disk space on the system.</td>
</tr>
<tr class="odd">
<td><strong>Assessment</strong></td>
<td><p>Assessment is the documentation of a clinician’s observations and interpretation of a patient’s clinical state based on a particular set of observations. The documentation is in the form of name-value pairs with values selected from a predetermined set, of name-value pairs in which the value is a number or set of numbers, or of free text.</p>
<p>Examples of assessments from paper ICU flowsheets are coma scale, patient opens eyes, pupil size, reaction to light, and so on.</p></td>
</tr>
<tr class="even">
<td><strong>ASU</strong></td>
<td>Authorization/Subscription Utility. An application that allows sites to associate users with user classes, allowing them to specify the level of authorization needed to sign or order specific document types and orderables. ASU is distributed with TIU in this version; eventually it will probably become independent, to be used by many VistA packages.</td>
</tr>
<tr class="odd">
<td><strong>Attachments</strong></td>
<td><p>Attachments are files or images stored on a network share that can be linked to the CP study. CP is able to accept data/final result report files from automated instruments. The file types that can be used as attachments are the following:<br />
.txt - Text files<br />
.rtf - Rich text files<br />
.jpg - JPEG Images<br />
.jpeg - JPEG Images<br />
.bmp - Bitmap Images<br />
.tiff - TIFF Graphics (group 3 and group 4 compressed and uncompressed types)<br />
.pdf - Portable Document Format<br />
.html - Hypertext Markup Language</p>
<p>.DOC (Microsoft Word) files are not supported. Be sure to convert .doc files to .rtf or to .pdf format.</p></td>
</tr>
<tr class="even">
<td><strong>Background Processing</strong></td>
<td>Simultaneous running of a "job" on a computer while working on another job. Examples would be printing of a document while working on another, or the software might do automatic saves while you are working on something else.</td>
</tr>
<tr class="odd">
<td><strong>Background Task</strong></td>
<td>A job running on a computer while simultaneously working on a second job.</td>
</tr>
<tr class="even">
<td><strong>Backup Procedures</strong></td>
<td>The provisions made for the recovery of data files and program libraries and for restart or replacement of ADP equipment after the occurrence of a system failure.</td>
</tr>
<tr class="odd">
<td><strong>Boilerplate Text</strong></td>
<td>A pre-defined TIU template that can be filled in for Titles, Speeding up the entry process. TIU exports several Titles with boilerplate text which can be modified to meet specific needs; sites can also create their own.</td>
</tr>
<tr class="even">
<td><strong>BP</strong></td>
<td>Blood Pressure.</td>
</tr>
<tr class="odd">
<td><strong>Broker</strong></td>
<td>Software which mediates between two objects, such as a client and a server or a repository and a requestor.</td>
</tr>
<tr class="even">
<td><strong>Browse</strong></td>
<td>Lookup the file folder for a file that you would like to select and attach to the study. (e.g., clicking the “...” button to start a lookup).</td>
</tr>
<tr class="odd">
<td><strong>Bulletin</strong></td>
<td>A canned message that is automatically sent by MailMan to a user when something happens to the database.</td>
</tr>
<tr class="even">
<td><strong>Business Rule</strong></td>
<td>Part of ASU, Business Rules authorize specific users or groups of users to perform specified actions on documents in particular statuses (e.g., an unsigned CP note may be edited by a provider who is also the expected signer of the note).</td>
</tr>
<tr class="odd">
<td><strong>CAC</strong></td>
<td>Clinical Application Coordinator.</td>
</tr>
<tr class="even">
<td><strong>Care Action</strong></td>
<td>Care action is an intervention scheduled on a patient that may or may not be ordered.</td>
</tr>
<tr class="odd">
<td><strong>CCB</strong></td>
<td>Change Control Board.</td>
</tr>
<tr class="even">
<td><strong>CCDSS</strong></td>
<td>Clinical Care Delivery Support System.</td>
</tr>
<tr class="odd">
<td><strong>CCOW</strong></td>
<td>Clinical Context Object Workgroup. An HL7 standard protocol through which applications can synchronize in real-time, enabling Single Sign On and Context Management.</td>
</tr>
<tr class="even">
<td><strong>CDR</strong></td>
<td>Clinical Data Repository.</td>
</tr>
<tr class="odd">
<td><strong>CIS</strong></td>
<td>Clinical Information System. An ICU Clinical Information System is any hardware/software system that works in concert to collect, store, display, and/or enable manipulation of potential, clinically relevant information. A CIS also acts as an HL7 Gateway. Vendors of monitors and other instruments used in an ICU provide the CIS. The primary distinguishing feature of this CIS is its ability to manually select a subset of all available data and send it to the EMR.</td>
</tr>
<tr class="even">
<td><strong>Class</strong></td>
<td>Part of Document Definitions, Classes group documents. For example, “CLINICAL PROCEDURES” is a class with many kinds of Clinical Procedures notes under it. Classes may be subdivided into other Classes or Document Classes. Besides grouping documents, Classes also store behavior which is then inherited by lower level entries.</td>
</tr>
<tr class="odd">
<td><strong>Clinical Flowsheets</strong></td>
<td>A module of the Clinical Procedures package that allows the collection of discrete data from medical devices or a Clinical Information System. It is a complete HL7 standardized instrument interface developed and owned by the Department of Veterans Affairs. This module is comprised of three components: the CP Flowsheets application, the CP Console application, and the CliO Generic Interface.</td>
</tr>
<tr class="even">
<td><strong>Clinical Reminders</strong></td>
<td>A system which allows caregivers to track and improve preventive healthcare and disease treatment for patients and to ensure timely clinical interventions.</td>
</tr>
<tr class="odd">
<td><strong>CliO</strong></td>
<td>Clinical Observations database.</td>
</tr>
<tr class="even">
<td><strong>CM</strong></td>
<td>Configuration Management.</td>
</tr>
<tr class="odd">
<td><strong>Consult</strong></td>
<td>Referral of a patient by the primary care physician to another hospital service/ specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion.</td>
</tr>
<tr class="even">
<td><strong>Contingency Plan</strong></td>
<td>A plan that assigns responsibility and defines procedures for use of the backup/restart/recovery and emergency preparedness procedures selected for the computer system based on risk analysis for that system.</td>
</tr>
<tr class="odd">
<td><strong>CP</strong></td>
<td>Clinical Procedures.</td>
</tr>
<tr class="even">
<td><strong>CP Console</strong></td>
<td>An application used by Administrators to configure the CP Flowsheets application and its interface settings.</td>
</tr>
<tr class="odd">
<td><strong>CP Definition</strong></td>
<td>CP Definitions are procedures within Clinical Procedures.</td>
</tr>
<tr class="even">
<td><strong>CP Flowsheets</strong></td>
<td>A GUI component of the Clinical Flowsheets package. Its primary functions are to provide a means to display data collected from a medical device and to allow manual entry of data. Additional functionality is provided to display and print reports, verify incoming observational data, add comments, correct erroneous information, and submit TIU Notes to CPRS.</td>
</tr>
<tr class="odd">
<td><strong>CP Gateway</strong></td>
<td>The service application that prepares the data contents of HL7 messages for use in CP Hemodialysis. It requires no direct user interaction.</td>
</tr>
<tr class="even">
<td><strong>CP Manager</strong></td>
<td>The CP Manager application is no longer supported after the installation of MD*1.0*16; it has been superseded by. CP Console.</td>
</tr>
<tr class="odd">
<td><strong>CP Study</strong></td>
<td>A CP study is a process created to link the procedure result from the medical device or/and to link the attachments browsed from a network share to the procedure order.</td>
</tr>
<tr class="even">
<td><strong>CPRS</strong></td>
<td>Computerized Patient Record System. A comprehensive VistA program, which allows clinicians and others to enter and view orders, Progress Notes and Discharge Summaries (through a link with TIU), Problem List, view results, reports (including health summaries), etc.</td>
</tr>
<tr class="odd">
<td><strong>Data Dictionary</strong></td>
<td>A description of file structure and data elements within a file.</td>
</tr>
<tr class="even">
<td><strong>DBIA</strong></td>
<td>Database Integration Agreement.</td>
</tr>
<tr class="odd">
<td><strong>Delphi</strong></td>
<td>A programming language, also known as Object Pascal.</td>
</tr>
<tr class="even">
<td><strong>Device</strong></td>
<td>A hardware input/output component of a computer system (e.g., CRT, printer).</td>
</tr>
<tr class="odd">
<td><strong>Display Interval</strong></td>
<td>The amount of time that displays in each column of a flowsheet view. Display interval is configurable from 1 minute to 24 hours. Shorter interval settings can improve readability when a large amount of data is received over a short period of time. Longer interval settings allow you to view longer periods of time while reducing the amount of horizontal scrolling necessary to view all columns.</td>
</tr>
<tr class="even">
<td><strong>DLL</strong></td>
<td>Dynamically Linked Library. These files provide the benefit of shared libraries.</td>
</tr>
<tr class="odd">
<td><strong>DOB</strong></td>
<td>Date of Birth.</td>
</tr>
<tr class="even">
<td><strong>Document Class</strong></td>
<td>Document Classes are categories that group documents (Titles) with similar characteristics together. For example, Cardiology notes might be a Document Class, with Echo notes, ECG notes, etc. as Titles under it. Or maybe the Document Class would be Endoscopy Notes, with Colonoscopy notes, etc. under that Document Class.</td>
</tr>
<tr class="odd">
<td><strong>Document Definition</strong></td>
<td>Document Definition is a subset of TIU that provides the building blocks for TIU, by organizing the elements of documents into a hierarchy structure. This structure allows documents (Titles) to inherit characteristics (such as signature requirements and print characteristics) of the higher levels, Class and Document Class. It also allows the creation and use of boilerplate text and embedded objects.</td>
</tr>
<tr class="even">
<td><strong>DUZ</strong></td>
<td>Designated user. This is the internal FileMan number for a particular user.</td>
</tr>
<tr class="odd">
<td><strong>Edit</strong></td>
<td>Used to change/modify data typically stored in a file.</td>
</tr>
<tr class="even">
<td><strong>EMR</strong></td>
<td>Electronic Medical Record. Health<em>e</em>Vet, is the permanent medical record for a patient in VistA</td>
</tr>
<tr class="odd">
<td><strong>Field</strong></td>
<td>A data element in a file.</td>
</tr>
<tr class="even">
<td><strong>File</strong></td>
<td>The M construct in which data is stored for retrieval later. A computer record of related information.</td>
</tr>
<tr class="odd">
<td><strong>File Manager or FileMan</strong></td>
<td>Within this manual, FileManager or FileMan is a reference to VA FileMan. FileMan is a set of M routines used to enter, edit, print, and sort/search related data in a file, a database.</td>
</tr>
<tr class="even">
<td><strong>File Server</strong></td>
<td>A machine where shared software is stored.</td>
</tr>
<tr class="odd">
<td><strong>Flowsheet</strong></td>
<td>A flowsheet is a table, chart, spreadsheet, or other method of displaying data on two axes. One axis represents time intervals and the other axis represents the readings from an ICU monitor documented at the various time intervals.</td>
</tr>
<tr class="even">
<td><strong>Flowsheet view</strong></td>
<td>A customizable subsection (or page) of a flowsheet. Flowsheet views are created by adding and arranging terms and choosing their default qualifiers. Flowsheet views can be set up to display observations, provide a way to manually enter observations, and display reports.</td>
</tr>
<tr class="odd">
<td><strong>Fluid off</strong></td>
<td>Cumulative volume of fluid removed from patient.</td>
</tr>
<tr class="even">
<td><strong>Gateway</strong></td>
<td>The software that performs background processing for Clinical Procedures.</td>
</tr>
<tr class="odd">
<td><strong>Global</strong></td>
<td>An M term used when referring to a file stored on a storage medium, usually a magnetic disk.</td>
</tr>
<tr class="even">
<td><strong>GUI</strong></td>
<td>Graphical User Interface. A Windows-like screen that uses pull-down menus, icons, pointer devices, and other metaphor-type elements that can make a computer program more understandable, easier to use, allow multi-processing (more than one window or process available at once), etc.</td>
</tr>
<tr class="odd">
<td><strong>HDR</strong></td>
<td>Health Data Repository.</td>
</tr>
<tr class="even">
<td><strong>HEP (CUM)</strong></td>
<td>Cumulative heparin infusion</td>
</tr>
<tr class="odd">
<td><strong>HFS</strong></td>
<td>Host File System.</td>
</tr>
<tr class="even">
<td><strong>HIPAA</strong></td>
<td>Health Insurance Portability and Accountability Act.</td>
</tr>
<tr class="odd">
<td><strong>HL7</strong></td>
<td>Health Level 7. A language which various healthcare systems use to interface with one another.</td>
</tr>
<tr class="even">
<td><strong>HL7 Gateway</strong></td>
<td>Hardware or software provided by a vendor that is able to receive information in a vendor’s proprietary format from one or more ICU monitors and other instruments, to translate the data into standardized HL7 message format, and to pass the messages to other systems.</td>
</tr>
<tr class="odd">
<td><strong>HR</strong></td>
<td>Heart Rate.</td>
</tr>
<tr class="even">
<td><strong>HSD&amp;D</strong></td>
<td>Office of Information (OI), Health Systems Design &amp; Development.</td>
</tr>
<tr class="odd">
<td><strong>HSITES</strong></td>
<td>Health Systems Implementation, Training, Education, and Support.</td>
</tr>
<tr class="even">
<td><strong>ICU</strong></td>
<td>Intensive Care Unit.</td>
</tr>
<tr class="odd">
<td><strong>IEN</strong></td>
<td>Internal Entry Number.</td>
</tr>
<tr class="even">
<td><strong>IJ</strong></td>
<td>Internal Jugular.</td>
</tr>
<tr class="odd">
<td><strong>Instrument</strong></td>
<td>An instrument is a device used to perform a medical function on a patient. In Clinical Flowsheets instrument refers to ICU monitors, which are electronic devices that collect and/or display information concerning the physical state of a patient. Usually, the monitor attaches to a patient and takes readings over time without requiring intervention for each reading.</td>
</tr>
<tr class="even">
<td><strong>Interpreter</strong></td>
<td>Interpreter is a user role exported with USR*1*19 to support the Clinical Procedures Class. The role of the Interpreter is to interpret the results of a clinical procedure. Users who are authorized to interpret the results of a clinical procedure are sent a notification when an instrument report and/or images for a CP request are available for interpretation. Business rules are used to determine what actions an interpreter can perform on a document of a specified class, but the interpreter themselves are defined by the Consults application. These individuals are ‘clinical update users’ for a given consult service.</td>
</tr>
<tr class="odd">
<td><strong>IRM</strong></td>
<td>Information Resource Management.</td>
</tr>
<tr class="even">
<td><strong>IRMS</strong></td>
<td>Information Resource Management Service.</td>
</tr>
<tr class="odd">
<td><strong>JCAHO</strong></td>
<td>Joint Commission on Accreditation of Healthcare Organizations.</td>
</tr>
<tr class="even">
<td><strong>Kernel</strong></td>
<td>A set of software utilities. These utilities provide data processing support for the application packages developed within the VA. They are also tools used in configuring the local computer site to meet the particular needs of the hospital. The components of this operating system include MenuMan, TaskMan, Device Handler, Log-on/Security, and other specialized routines.</td>
</tr>
<tr class="odd">
<td><strong>Key</strong></td>
<td>A level of access assigned to a Flowsheets user that determines which Flowsheets functions the user may perform. Refer to “User Role” in this Glossary.</td>
</tr>
<tr class="even">
<td><strong>LAYGO</strong></td>
<td>An acronym for Learn As You Go. A technique used by VA FileMan to acquire new information as it goes about its normal procedure. It permits a user to add new data to a file.</td>
</tr>
<tr class="odd">
<td><strong>LPES/CPS</strong></td>
<td>Legacy Product Enterprise Support/Clinical Product Support. Enterprise Product Support (formerly Enterprise VistA Support).</td>
</tr>
<tr class="even">
<td><strong>log</strong></td>
<td>A list that provides the time and description of events as they occur.</td>
</tr>
<tr class="odd">
<td><strong>M</strong></td>
<td>Formerly known as MUMPS or the Massachusetts (General Hospital) Utility Multi-Programming System. This is the programming language used to write all VistA applications.</td>
</tr>
<tr class="even">
<td><strong>MailMan</strong></td>
<td>An electronic mail, teleconferencing, and networking system.</td>
</tr>
<tr class="odd">
<td><strong>MAP</strong></td>
<td>Mean Arterial Pressure.</td>
</tr>
<tr class="even">
<td><strong>Menu</strong></td>
<td>A set of options or functions available to users for editing, formatting, generating reports, etc.</td>
</tr>
<tr class="odd">
<td><strong>Module</strong></td>
<td>A component of a software application that covers a single topic or a small section of a broad topic.</td>
</tr>
<tr class="even">
<td><strong>MUMPS</strong></td>
<td>Massachusetts General Hospital Utility Multi-Programming System. Obsolete; now known as "M" programming language.</td>
</tr>
<tr class="odd">
<td><strong>Namespace</strong></td>
<td>A naming convention followed in the VA to identify various applications and to avoid duplication. It is used as a prefix for all routines and globals used by the application.</td>
</tr>
<tr class="even">
<td><strong>Network Server Share</strong></td>
<td>A machine that is located on the network where shared files are stored.</td>
</tr>
<tr class="odd">
<td><strong>Notebook</strong></td>
<td>This term refers to a GUI screen containing several tabs or pages.</td>
</tr>
<tr class="even">
<td><strong>NTE</strong></td>
<td>Not To Exceed.</td>
</tr>
<tr class="odd">
<td><strong>OI</strong></td>
<td>Office of Information. Formerly known as Chief Information Office Field Office, Information Resource Management Field Office, and Information Systems Center.</td>
</tr>
<tr class="even">
<td><strong>option</strong></td>
<td>A functionality that is invoked by the user. The information defined in the option is used to drive the menu system. Options are created, associated with others on menus, or given entry/exit actions.</td>
</tr>
<tr class="odd">
<td><strong>optional page</strong></td>
<td>One of two special types of flowsheet views which provides a way to track a specific condition (e.g., a pacemaker) on its own flowsheet view. An Optional Page can display only once in a given flowsheet. If an optional page is closed and then redisplayed, any data previously entered still displays.</td>
</tr>
<tr class="even">
<td><strong>Package</strong></td>
<td>Otherwise known as an application. A set of M routines, files, documentation and installation procedures that support a specific function within VistA.</td>
</tr>
<tr class="odd">
<td><strong>page</strong></td>
<td>This term refers to a tab on a GUI screen or notebook.</td>
</tr>
<tr class="even">
<td><strong>Password</strong></td>
<td>A protected word or string of characters that identifies or authenticates a user, a specific resource, or an access type (synonymous with Verify Code).</td>
</tr>
<tr class="odd">
<td><strong>PCE</strong></td>
<td>Patient Care Encounter.</td>
</tr>
<tr class="even">
<td><strong>Permission</strong></td>
<td>Setting that can be used to allow access to particular views, flowsheets, etc. to one or more specific users and to control the type of access each user has.</td>
</tr>
<tr class="odd">
<td><strong>PIMS</strong></td>
<td>Patient Information Management System.</td>
</tr>
<tr class="even">
<td><strong>Pivot</strong></td>
<td>Swap the axes of a table or chart. This causes the values that were displayed along the vertical axis to be displayed along the horizontal axis and the values that were displayed along the horizontal axis to be displayed along the vertical axis.</td>
</tr>
<tr class="odd">
<td><strong>PM</strong></td>
<td>Project Manager.</td>
</tr>
<tr class="even">
<td><strong>Pointer</strong></td>
<td>A special data type of VA FileMan that takes its value from another file. This is a method of joining files together and avoiding duplication of information.</td>
</tr>
<tr class="odd">
<td><strong>PRN</strong></td>
<td>As needed.</td>
</tr>
<tr class="even">
<td><strong>Procedure Request</strong></td>
<td>Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/specialty without first requiring formal consultation.</td>
</tr>
<tr class="odd">
<td><strong>Program</strong></td>
<td>A set of M commands and arguments, created, stored, and retrieved as a single unit in M.</td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>A set of rules governing communication within and between computing endpoints.</td>
</tr>
<tr class="odd">
<td><strong>PS</strong></td>
<td>Provider Systems.</td>
</tr>
<tr class="even">
<td><strong>PV</strong></td>
<td>Pulmonary Vascular.</td>
</tr>
<tr class="odd">
<td><strong>QG</strong></td>
<td>Quality Gate.</td>
</tr>
<tr class="even">
<td><strong>Qualifiers</strong></td>
<td>A word or phrase that provides specific information about an observation. For example, an observation could have qualifiers such as Unit (f=degrees Fahrenheit, c=degrees Celsius, bpm=beats per minute, rpm=respirations per minute, etc.), Method (Cu=cuff BP, Dop=Doppler BP, etc.), Position (Ly=lying, Si=sitting, St=standing, etc.), Location (La=left arm, LL=left leg, RA=right arm, RL=right leg, etc.), Quality (A=accurate, E=Estimated), etc.</td>
</tr>
<tr class="odd">
<td><strong>Queuing</strong></td>
<td>The scheduling of a process/task to occur later. Queuing is normally done if a task is a heavy user of computer resources.</td>
</tr>
<tr class="even">
<td><strong>RAID</strong></td>
<td>Redundant Array of Inexpensive Disks. A data storage scheme using multiple hard drives to share or replicate data among the drives.</td>
</tr>
<tr class="odd">
<td><strong>Result</strong></td>
<td>A consequence of an order. Refers to evaluation or status results. When you use the Complete Request (CT) action on a consult or request, you are transferred to TIU to enter the results.</td>
</tr>
<tr class="even">
<td><strong>Routine</strong></td>
<td>A set of M commands and arguments, created, stored, and retrieved as a single unit in M.</td>
</tr>
<tr class="odd">
<td><strong>RPC</strong></td>
<td>Remote Procedure Call. A protocol that allows a computer program running on one host to cause code to be executed on another host.</td>
</tr>
<tr class="even">
<td><strong>Rx</strong></td>
<td>Prescription.</td>
</tr>
<tr class="odd">
<td><strong>SAC</strong></td>
<td>Standards And Conventions.</td>
</tr>
<tr class="even">
<td><strong>Security Key</strong></td>
<td>A function which unlocks specific options and makes them accessible to an authorized user.</td>
</tr>
<tr class="odd">
<td><strong>Sensitive Information</strong></td>
<td>Any information which requires a degree of protection and which should be made available only to authorized users.</td>
</tr>
<tr class="even">
<td><strong>Service</strong></td>
<td>A long-running executable designed to perform specific functions without user intervention. Windows services can be configured to restart automatically when the operating system is rebooted.</td>
</tr>
<tr class="odd">
<td><strong>SGML</strong></td>
<td>Standard Generalized Markup Language.</td>
</tr>
<tr class="even">
<td><strong>Shift</strong></td>
<td>A period of time that can be defined in CP Flowsheets. This often corresponds to the time an individual an individual works.</td>
</tr>
<tr class="odd">
<td><strong>Site Configurable</strong></td>
<td>A term used to refer to features in the system that can be modified to meet the needs of each site</td>
</tr>
<tr class="even">
<td><strong>Software</strong></td>
<td>A generic term for a related set of computer programs, such as an operating system that enables user programs to run.</td>
</tr>
<tr class="odd">
<td><strong>SQA</strong></td>
<td>Software Quality Assurance.</td>
</tr>
<tr class="even">
<td><strong>SRS</strong></td>
<td>Software Requirements Specification.</td>
</tr>
<tr class="odd">
<td><strong>SSN</strong></td>
<td>Social Security Number.</td>
</tr>
<tr class="even">
<td><strong>Status Symbols</strong></td>
<td>Codes used in order entry and Consults displays to designate the status of the order.</td>
</tr>
<tr class="odd">
<td><strong>STS</strong></td>
<td>Standards and Terminology Services. An initiative to create and maintain standardized terminology throughout the VA by assigning a code to every term.</td>
</tr>
<tr class="even">
<td><strong>Supplemental page</strong></td>
<td>One of two special types of flowsheet views which provides a way to track a specific condition (e.g., a pressure wound) on its own flowsheet view. Multiple supplemental pages can be added to a single flowsheet in order to track numerous specific conditions. If a supplemental page is closed and then a new supplemental page is added, the new supplemental page is blank.</td>
</tr>
<tr class="odd">
<td><strong>Tab</strong></td>
<td>One of the five primary GUI screens of the CP Flowsheets application: Flowsheet, Alarms, Reports, Log Files, and HL7 Monitor.</td>
</tr>
<tr class="even">
<td><strong>Task Manager or TaskMan</strong></td>
<td>A part of Kernel which allows programs or functions to begin at specified times or when devices become available. See Queuing.</td>
</tr>
<tr class="odd">
<td><strong>Term</strong></td>
<td>As used in Flowsheets, a term is any piece of relevant data. A term, like “Blood Pressure” will typically have one or more associated measures, modifiers, or qualifiers.</td>
</tr>
<tr class="even">
<td><strong>Terminology</strong></td>
<td>Standardization of words and terms used in Flowsheets.</td>
</tr>
<tr class="odd">
<td><strong>Title</strong></td>
<td>Titles are definitions for documents. They store the behavior of the documents which use them.</td>
</tr>
<tr class="even">
<td><strong>TIU</strong></td>
<td>Text Integration Utilities.</td>
</tr>
<tr class="odd">
<td><strong>TMP</strong></td>
<td>Trans Membrane Pressure.</td>
</tr>
<tr class="even">
<td><strong>UFR</strong></td>
<td>Ultrafiltration Rate.</td>
</tr>
<tr class="odd">
<td><strong>UI</strong></td>
<td>User Interface.</td>
</tr>
<tr class="even">
<td><strong>UNC</strong></td>
<td>Universal Naming Convention.</td>
</tr>
<tr class="odd">
<td><strong>Untrusted device</strong></td>
<td>A medical instrument which has not been mapped for use with the Clinical Flowsheets package. Data sent from an untrusted device will not display in a flowsheet view until someone reviews it (on the CP Flowsheets Log Files tab) and marks it as verified.</td>
</tr>
<tr class="even">
<td><strong>URL</strong></td>
<td>Uniform Resource Locator. A means of finding a resource (such as a web page or a device) on the Internet.</td>
</tr>
<tr class="odd">
<td><strong>URR</strong></td>
<td>Urea Reduction Ratio. The reduction in urea as a result of dialysis.</td>
</tr>
<tr class="even">
<td><strong>User</strong></td>
<td>A person who enters and/or retrieves data in a system, usually utilizing a CRT.</td>
</tr>
<tr class="odd">
<td><strong>User Class</strong></td>
<td>User Classes are the basic components of the User Class hierarchy of ASU (Authorization/Subscription Utility) which allows sites to designate who is authorized to do what to documents or other clinical entities.</td>
</tr>
<tr class="even">
<td><strong>User Role</strong></td>
<td>User Role (in a documentation context). The role of the user with respect to the document in question (e.g., Author/Dictator, Expected Signer, Expected Cosigner, Attending Physician, etc.).</td>
</tr>
<tr class="odd">
<td><strong>User Role</strong></td>
<td><p>User Role (in a Flowsheets setup context). The role of a Flowsheets user with respect to which Flowsheets functions the user will have permission to perform. Flowsheets User Role include the following.</p>
<blockquote>
<p>• MD ADMINISTRATOR</p>
<p>• MD MANAGER</p>
<p>• MD HL7 MANAGER</p>
<p>• MD READ-ONLY</p>
<p>• MD TRAINEE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>Utility</strong></td>
<td>An M program that assists in the development and/or maintenance of a computer system.</td>
</tr>
<tr class="odd">
<td><strong>UUEncoded format</strong></td>
<td>A form of binary to text encoding whose name derives from "Unix-to-Unix encoding”.</td>
</tr>
<tr class="even">
<td><strong>VA</strong></td>
<td>Department of Veterans Affairs. Formerly the Veterans Administration.</td>
</tr>
<tr class="odd">
<td><strong>VAMC</strong></td>
<td>Department of Veterans Affairs Medical Center.</td>
</tr>
<tr class="even">
<td><strong>VDEF</strong></td>
<td>VistA Data Extraction Framework.</td>
</tr>
<tr class="odd">
<td><strong>Verify Code</strong></td>
<td>A unique security code which serves as a second level of security access. Use of this code is site specific. This term is sometimes used interchangeably the term password.</td>
</tr>
<tr class="even">
<td><strong>VHA</strong></td>
<td>Veteran Health Administration.</td>
</tr>
<tr class="odd">
<td><strong>VistA</strong></td>
<td>Veterans Health Information Systems and Technology Architecture.</td>
</tr>
<tr class="even">
<td><strong>VP</strong></td>
<td>Venous Pressure.</td>
</tr>
<tr class="odd">
<td><strong>VUID</strong></td>
<td>Veterans Health Administration (VHA) Unique Identifier. A unique identifier that specifies individual data elements or observations. In Clinical Flowsheets, each term is assigned a VUID.</td>
</tr>
<tr class="even">
<td><strong>Workstation</strong></td>
<td>A personal computer running the Windows 9x or NT operating system.</td>
</tr>
<tr class="odd">
<td><strong>XML</strong></td>
<td>Extensible Markup Language. A simplified subset of Standard Generalized Markup Language (SGML). Its primary purpose is to facilitate the sharing of data across different information systems.</td>
</tr>
<tr class="even">
<td><strong>XMS</strong></td>
<td>Extended Memory Specification. The specification describing the use of extended memory in real mode for storing data.</td>
</tr>
</tbody>
</table>
