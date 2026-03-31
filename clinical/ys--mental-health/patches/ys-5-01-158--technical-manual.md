---
title: YS*5.01*158 Mental Health - Suicide Prevention Package Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Mental Health - Suicide Prevention Package
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01*158
group_key: "YS:YS:5.01"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - application
  - software
  - requirements
  - security
  - patient
  - vista
  - assignment
  - health
page_count: 0
word_count: 1972
section_count: 19
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/clin_0004av_tm_ys_501_158.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/clin_0004av_tm_ys_501_158.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

Mental Health – Suicide Prevention

Suicide Prevention Package

![](ys-5-01-158-mental-health-suicide-prevention-package-technical-manual/001.png)

May 2021

Technical Manual

YS\*5.01\*158

Submitted as CLIN 0004AV

Contract VA118-16-D-1007, Task Order VA11817F10070006

*Submitted by:*

Booz Allen Hamilton Inc.

141 W. Front Street, Suite 200

Red Bank, NJ 07701

Phone: 732-936-3500

Fax: 732-936-3535

![](ys-5-01-158-mental-health-suicide-prevention-package-technical-manual/002.png)

Revision History

<table>
<caption>Table used for formatting, only.Revision History, including date of changes, version number, description of change, and author of change.</caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 45%" />
<col style="width: 24%" />
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
<td>02/28/2021</td>
<td>1.2</td>
<td><p>Update – Build 14</p>
<ul>
<li><p>Update application name from MHA PaSE to MHA Web</p></li>
</ul></td>
<td>Booz Allen</td>
</tr>
<tr class="even">
<td>12/11/2020</td>
<td>1.1</td>
<td>Update – Build 13</td>
<td>Booz Allen</td>
</tr>
<tr class="odd">
<td>09/11/2020</td>
<td>1.0</td>
<td>Initial Document</td>
<td>Booz Allen</td>
</tr>
</tbody>
</table>

Table used for formatting, only.Revision History, including date of changes, version number, description of change, and author of change.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [System Overview](#system-overview)
  - [Document Orientation](#document-orientation)
    - [Software Disclaimer](#software-disclaimer)
    - [References](#references)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [System Requirements](#system-requirements)
    - [Hardware Requirements](#hardware-requirements)
    - [Software Requirements](#software-requirements)
    - [Database Requirements](#database-requirements)
  - [System Setup and Configuration](#system-setup-and-configuration)
- [Files](#files)
- [Routines](#routines)
- [Exported Options](#exported-options)
- [Mail Groups, Alerts, and Bulletins](#mail-groups-alerts-and-bulletins)
- [Public Interfaces](#public-interfaces)
  - [Integration Control Registrations](#integration-control-registrations)
  - [Application Programming Interfaces](#application-programming-interfaces)
  - [Remote Procedure Calls](#remote-procedure-calls)
  - [HL7 Messaging](#hl7-messaging)
  - [Web Services](#web-services)
- [Standards and Conventions Exemptions](#standards-and-conventions-exemptions)
  - [Internal Relationships](#internal-relationships)
  - [Software-wide Variables](#software-wide-variables)
- [Security](#security)
  - [Menus and Options](#menus-and-options)
  - [Security Keys and Roles](#security-keys-and-roles)
  - [File Security](#file-security)
  - [Electronic Signatures](#electronic-signatures)
  - [Secure Data Transmission](#secure-data-transmission)
- [Archiving](#archiving)
- [Non-Standard Cross-References](#non-standard-cross-references)
  - [Enterprise Service Desk and Organizational Contacts](#enterprise-service-desk-and-organizational-contacts)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
This document gives a brief technical overview of the Mental Health Assistant (MHA) Web-Patient Entry (MHA Web-PE) Application architecture and describes the developer environments.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes the technical details for MHA Web.

The project scope can be found in the Suicide_Prevention_Requirements.xlsx located in GitHub.

## System Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MHA Web application will give providers ability to assign and schedule current and future patient self-administrations that can be completed on a kiosk or iPad, comprehensively manage assessments, securely implement mobile instrument administrations and migrate data to VistA. The new enhancements which allow clinicians to assign instruments for patient self-administration require navigation from existing MHA and Computerized Patient Record System (CPRS) screens. This ensures efficient processes and that the facilitation of management of access to care for at risk Veterans.

The full capabilities of this application will be delivered in multiple iterations. The first iteration provides the ability for a clinician to create a patient Assignment in the MHA Delphi interface and allows the patient to self-administer the instrument Assignment on a kiosk or iPad at a VA clinic (MHA Web–PE). The second interation allows the clinician to create and edit a patient assignment in the web based interface and allows the clinician to administer the instrument. This is known as Planning and Staff Entry (MHA Web).

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Disclaimer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software was developed at the Department of Veterans Affairs (VA) by employees and contractors of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

### References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Web is implemented in Spring Boot with a React front-end and Java backend. The React code is bundled using webpack and deployed onto the Spring Boot server running embedded Tomcat.

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MHA Web application requires:

1)  Microsoft Azure cloud-based server environment
2)  Red Hat Linux (Redhat: enterprise_linux:7.6:GA:server)
3)  Java JRE ( Java Open JDK 1.8.0_191 )
4)  Docker (18.09.1, build 4c52b90)
5)  MHA Web-PE JAR file

### Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no hardware modifications with this Mental Health Assistant release; however, previous packages have been run on the standard hardware platforms used by the Department of Veterans Affairs Health Care System facilities. These systems consist of standard or upgraded Alpha AXP clusters, standard intel hardware Windows operating system, or Microsoft Azure instances and run either Cache-VMS, Cache-NT, Cache- OpenVMS, or Cache- Windows Server 2008 or higher.

Deployment at the VistA sites require a workstation, kiosk, or VA iPad for patients to access MHA Web-PE. A VA standard workstation is required to access MHA Web.

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                      |                            |
|----------------------|----------------------------|
| Application Name | Minimum Version Needed |
| CPRS                 | 31 A                       |
| Clinical Reminders   | 2.0                        |
| Kernel               | 8.0                        |
| RPC Broker           | 1.1                        |
| PIMS                 | 5.3                        |
| VA FileMan           | 22.0                       |
| Mailman              | 8.0                        |

The following patches are required:

YS\*5.01\*141 – MHA GUI and Web Updates

YS\*5.01\*150 – Suicide Prevention Instruments

YS\*5.01\*173 – Inactivate I9 Instruments, Update PROMIS29

The following patch is strongly recommended:

DG\*5.3\*1026 – Master Veteran Indexa VistA Enhancement – TFL API Update

### Database Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Web requires a compatible MySQL Database hosted in the Azure environment. This database serves as connection and session management and does not contain any Protected Health Information (PHI) or Personally Identifiable Information (PII).

## System Setup and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Web runs in an Azure cloud environment as a JAR file in a Dockerized instance. The application instance properties and connection parameters are contained in a configuration files.

- application.properties
- application.yml

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two files are required for the MHA Web application. The first is the executable JAR file and the second is the configuration file which contains the properties and connection parameters for the application instance.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two components to the routines, one which is the web-based UI and the other manages the VistA Remote Procedure Calls (RPC).

- staffentry.jar – Executable file which runs in the Azure Docker container.
- YS_501_158.KID – VistA KIDS package of routines which handle RPC requests.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Web adds YTQREST MHA to the OPTION file as the context for the RPC call.

# Mail Groups, Alerts, and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no mail groups, alerts or bulletins.

# Public Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is an intranet clinician facing web site that hosts the MHA Web application. The web site is accessed by the browser on a workstation within the VA.

## Integration Control Registrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view the details of a Database Integration Agreements (DBIA) use the VA Forum option “Inquire to an Integration Control Registration” to display the DBIAS where the Mental Health package is the custodial or the subscribing package.

## Application Programming Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Web utilizes two APIs.

The Azure docker React/Java application leverages the existing VistaLink APIs. Further documentation regarding the available APIs are available on the VA Software Document Library.

The VistA interface exposes application functionality through the RPC, YTQREST QADMIN. The functional calls are listed in the table below.

| RPC URL                                        | Description                                                                                                         |
|----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| GET /api/mha/getconn                               | Response to an RPC connection test request                                                                              |
| GET /api/mha/patient/:dfn/identifiers              | Get patient demographic information for the patient specified by the :dfn parameter                                     |
| GET /api/mha/persons/:match                        | Get a list of users from the NEW PERSON file that starts with the :match parameter                                      |
| GET /api/mha/users/Lmatch                          | Get a list of users from the NEW PERSON file that starts with the :match parameter                                      |
| GET /api/mha/instruments/active                    | Get a list of active instruments                                                                                        |
| GET /api/mha/instrument/:instrumentName            | Get the instrument definition specified by the :instrumentName parameter                                                |
| GET /api/mha/checks/:instrumentName                | Get validation requirements for the instrument specified by the :instrumentName parameter                               |
| GET /api/mha/assignment/:assignmentId              | Get information regarding the patient instrument assignment specified by the :assignmentId parameter                    |
| GET /api/mha/assignment/:assignmentId/:division    | Get information regarding the patient instrument assignment specified by the :assignmentId parameter                    |
| GET /api/mha/assignment/graph/:dfn/:instrument     | Get the graph data for a patient specified by :dfn and instrument administrations specified by :instrument.             |
| GET /api/mha/instrument/admin/:adminId             | Get the current state and details of an instrument administration in progress specified by the :adminId parameter.      |
| GET /api/mha/instrument/report/:adminId            | Get the report text for the instrument administration specified by :adminId                                             |
| GET /api/mha/instrument/note/:adminId              | Get the note text for the instrument administration specified by :adminId                                               |
| GET /api/mha/permission/cosign/:adminId/:userId    | Get the cosigining permission for the instrument administration specified by :adminId and the user specified by :userId |
| GET /api/mha/instrument/list/:dfn                  | Get a list of instrument administrations for a patient specified by :dfn                                                |
| GET /api/mha/location/list/:duz                    | Get a list of Hospital Locations available for a user specified by :duz                                                 |
| GET /api/mha/category/list                         | Get a list of instruments available sorted by instrument type Category                                                  |
| GET /api/mha/assignment/list/:dfn                  | Get a list of Assignments for a patient specified by :dfn                                                               |
| GET /api.mha/consult/list/:dfn                     | Get a list of Consults for a patient specified by :dfn                                                                  |
| GET /api/mha/assignment/staff/:assignmentId        | Get a Staff only assignment specified by :assignmentId                                                                  |
| POST /api/mha/assignment                           | Save a new Assignment                                                                                                   |
| POST /api/mha/assignment/edit/:assignmentId        | Save the edited Assignment specified by :assignmentId                                                                   |
| POST /api/mha/instrument/admin                     | Save the status and details of an instrument administration in progress.                                                |
| POST /api/mha/instrument/note                      | Save the unsigned Note text for an instrument administration                                                            |
| DELETE /api/mha/assignment/:assignmentID           | Delete the Assignment specified by :assignmentId                                                                        |
| DELETE /api/mha/assignment/:assignmentID/:division | Delete the Assignment specified by :assignmentId                                                                        |

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Web uses one RPC, YTQREST QADMIN.

NAME: YTQREST QADMIN TAG: QADMIN

ROUTINE: YTQREST RETURN VALUE TYPE: ARRAY

AVAILABILITY: RESTRICTED WORD WRAP ON: FALSE

VERSION: 1 APP PROXY ALLOWED: No

DESCRIPTION:

Front controller for questionnaire administrator.

## HL7 Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No HL7 interfaces are used.

## Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No web service calls are used.

# Standards and Conventions Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No exemptions are used.

## Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No internal relationships.

## Software-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No software-wide variables are used.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinicians use CPRS and MHA to create Assignments for patients and administer instruments. No changes will be needed to the security and privacy requirements already approved for VistA and the GUI applications.

MHA Web functionality adheres to all VA and VHA security requirements and allows the clinician to create Assignments for patients, administer instruments, and review results.

## Menus and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One new OPTION is created to provide the Context for the RPC, YTQREST MHA.

The OPTION YS BROKER1 is updated to include the RPC YTQREST QADMIN. This allows users who already have YS BROKER1 to access the application without any additional configuration.

## Security Keys and Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new Security Keys or roles are defined.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Web does not store any PHI/PII. The application transmits PHI/PII to and from Vista via https and VistaLink but sensitive data is only hosted on Vista systems.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No changes to Electronic Signatures are implemented.

## Secure Data Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Web-PE only transmits data inside the VA network via https and VistaLink.

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No archiving is needed.

# Non-Standard Cross-References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA Web-PE utilizes the standard format of the ^XTMP global to store Assignment information. Assignments are only stored in ^XTMP until they are completed. In order to increase application efficiency MHA Web-PE makes use of two cross-references in ^XTMP.

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>XTMP Cross-Reference</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^XTMP(“YTQASMT-INDEX”,”AC”,ssn,lastname,date/time)<br />
=assignment#</td>
<td>Assignment cross-reference by last four SSN, patient last name, and inverse date/time.</td>
</tr>
<tr class="even">
<td>^XTMP(“YTQASMT-INDEX”,”AD”,dfn,duz,assignment#)<br />
=date</td>
<td>Assignment cross-reference by patient DFN, user DUZ, and assignment#. Date is in FileMan format.</td>
</tr>
</tbody>
</table>

## Enterprise Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Contact the Enterprise Service Desk if assistance is needed.

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term   | Meaning                                                         |
|------------|---------------------------------------------------------------------|
| CPRS       | Computerized Patient Record System                                  |
| DSM-5      | Diagnostic and Statistical Manual of Mental Disorders – 5th Edition |
| https      | Hypertext Transfer Protocol Secure                                  |
| MHA        | Mental Health Assistant                                             |
| MUMPS      | Massachusetts General Hospital Utility Multi-Programming System     |
| PSPO       | Patient Safety Program Office                                       |
| PTSD       | Posttraumatic Stress Disorder                                       |
| RPC Broker | Remote Procedure Call Broker                                        |
| RSD        | Requirements Specification Document                                 |
| RTM        | Requirements Traceability Matrix                                    |
| SAC        | Standards and Conventions                                           |
| SDD        | System Design Document                                              |
| SSO        | Single Sign-On                                                      |
| SPP        | Suicide Prevention Project                                          |
| SQA        | Software Quality Assurance                                          |
| TRM        | Technical Reference Model                                           |
| VA         | Veterans Administration                                             |
| VDD        | Version Description Document                                        |
| VistA      | Veterans Health Information Systems and Technology Architecture     |