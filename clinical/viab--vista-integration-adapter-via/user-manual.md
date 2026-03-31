---
title: VistA Integration Adapter (VIAB) Version 1 VIP User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: VIP
app_code: VIAB
app_name: VistA Integration Adapter (VIA)
section: CLI
app_status: active
pkg_ns: VIAB
patch_ver: 1
patch_id: VIAB*1
group_key: "VIAB:VIAB:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - application
  - document
  - span
  - guide
  - services
  - class
  - service
  - vista
page_count: 0
word_count: 3246
section_count: 15
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2016
revision_count: 1
revision_newest: 06/28/16
revision_oldest: 06/28/16
docx_url: "https://www.va.gov/vdl/documents/Clinical/VistA_Integration_Adapter_(VIA)/via_vip_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/VistA_Integration_Adapter_(VIA)/via_vip_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=221"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>VistA Integration Adapter (VIA)

  1.0

  User Guide
---

![](vista-integration-adapter-viab-version-1-vip-user-guide/001.png)

June 2016

Office of Information and Technology (OI&T)

Revision History

| Date     | Revision | Description         | Author   |
|----------|----------|---------------------|----------|
| 06/28/16 | 1.0      | Initial VIP Version | Engility |

<span id="_Toc454884946" class="anchor"></span>Table : Organization of User Guide

Artifact Rationale

Per the Veteran-focused Integrated Process (VIP) Guide, the User’s Guide is required to be completed prior to Critical Decision Point \#2 (CD2), with the expectation that it will be updated as needed. A User Guide is a technical communication document intended to give assistance to people using a particular system, such as VistA end users. It is usually written by a technical writer, although it can also be written by programmers, product or project managers, or other technical staff. Most user guides contain both a written guide and the associated images. In the case of computer applications, it is usual to include screenshots of the human-machine interfaces, and hardware manuals often include clear, simplified diagrams. The language used is matched to the intended audience, with jargon kept to a minimum or explained thoroughly. The User Guide is a mandatory, build-level document, and should be updated to reflect the contents of the most recently deployed build. The sections documented herein are required, if applicable to your product.

Table of Contents

Tables

Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Document Orientation](#document-orientation)
    - [Organization of the Manual](#organization-of-the-manual)
    - [Assumptions](#assumptions)
    - [Coordination](#coordination)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operation](#continuity-of-operation)
  - [Getting Started](#getting-started)
  - [Logging On](#logging-on)
  - [System Menu](#system-menu)
  - [Changing User ID and Password](#changing-user-id-and-password)
  - [Exit System](#exit-system)
  - [Caveats and Exceptions](#caveats-and-exceptions)
- [Using the Software](#using-the-software)
- [Troubleshooting](#troubleshooting)
  - [Special Instructions for Error Correction](#special-instructions-for-error-correction)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
- [Appendix](#appendix)
- [Index](#index)
Due to increased requests for external access to the Veterans Health Information Systems and Technology Architecture (VistA) system, the Department of Veterans Affairs (VA) has defined a need for a set of web services to facilitate those requests. Two Medical Domain Web Services (MDWS) applications were deployed to meet the need. However, these already-fielded products now require unanticipated corrective maintenance and do not meet current Information Technology (IT) supportability requirements in terms of security, stringent performance, scalability, and maintainability.
Therefore, a plan to replace MDWS is underway with the VistA Integration Adapter (VIA) middleware application. It is a solution that can be leveraged across the enterprise in support of the VA. VIA is designed to correct the aforementioned deficiencies and re-engineer the MDWS applications to a Java Enterprise Edition (JEE) platform, according to the Performance Work Statement (PWS) and Business Requirements Document (BRD).
Additionally, VIA facilitates the convergence of JMeadows and MDWS services into a common service platform, thereby providing the existing functionality of MDWS to client applications. VIA creates a set of common web services that allow consuming applications to securely retrieve data from VistA systems. It is intended to perform as an adapter that abstracts consuming applications from the technical details of the VistA computing environment. VIA utilizes a modularized design approach that separates generic-infrastructure functionality from business-oriented functionality, and thereby allows consuming applications to connect to VistA systems. VIA exposes the business interfaces using the Simple Object Access Protocol (SOAP) standard. This common service platform establishes a shared infrastructure for accessing a diverse set of information across geographic locations and spanning multiple technologies, and ultimately establishes a set of data access services within the VA’s extensive application landscape.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the VIA User Guide is to provide technical information to system administrators, IT support staff, and other authorized users. It will be updated as needed in subsequent releases.

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The document orientation is shown below in Sections 1.2.1 through 1.2.6.

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The major sections of the User Guide are shown in the following table:

| Section | Description                |
|---------|----------------------------|
| 1.0     | Introduction               |
| 2.0     | System Summary             |
| 3.0     | Getting Started            |
| 4.0     | Using the Software         |
| 5.0     | Troubleshooting            |
| 6.0     | Acronyms and Abbreviations |

<span id="_Toc454884947" class="anchor"></span>Table : VIA Sustainment Team

The target audience for this guide includes system administrators, IT support staff, and other authorized users.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the assumption that there will be no direct users because VIA is middleware.

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIA code is released through Austin Information Technology Center (AITC). The production code is identified at AITC as VIA. Coordination is done by the use of AITC standard request practices. A Request for Change (RFC) and a communication to the team is done to get on the AITC release calendar.

The following table shows the current sustainment team supporting VIA:

| Name                                                                                    | Role(s)                     |
|---------------------------------------------------------------------------------------------|---------------------------------|
| [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) | Application Manager             |
| [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) | Build Manager (Release Manager) |
| [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) | Database Administrator          |
| [*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp) | Linux System Administrator      |

<span id="_Toc454884948" class="anchor"></span>Table : Acronyms and Abbreviations

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIA software and documentation disclaimers are shown below in Sections 1.2.4.1 and 1.2.4.2.

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of the Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable.

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are references and resources for the VIA User Guide:

- [VIA System Design Document](http://vaww.oed.portal.va.gov/pm/hppmd/CSSS/VIA/Shared%20Documents/VIA%20(E)%20System%20Design%20Document.docx)
- [VIA Business Requirements Document](http://vaww.oed.portal.va.gov/pm/hppmd/CSSS/VIA/Shared%20Documents/VIA%20(E)%20Business%20Requirements%20Document.docx)
- [VIA Interface Control Document](http://vaww.oed.portal.va.gov/pm/hppmd/CSSS/VIA/Shared%20Documents/VIA%20Interface%20Control%20Document.docx)
- [VIA Requirements Specification Document](http://vaww.oed.portal.va.gov/pm/hppmd/CSSS/VIA/Shared%20Documents/VIA%20(E)%20Requirements%20Specification%20Document.docx)

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp)

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIA system provides a secure, standards-based platform for delivery of Electronic Health Record (EHR) data from VistA and other sources to the requesting systems. VIA accomplishes this by retrieving data from numerous distributed data sources, aggregating the data, and providing it to the calling application. The existing services may be designed initially for a specific client system, but they are also used by other client applications with similar data needs.

This is made possible by establishing multiple, independent, de-coupled web services for the data retrieval capability and for providing core business functionality. The web services are deployed in a standards-based, consistent fashion and are deployed in a JEE container. The JEE container specified in the Task Order response (Oracle WebLogic) is highly scalable, widely used within VHA, and provides high performance suitable for enterprise-class application needs.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The relevant services and the interfaces associated with VIA services are shown in Figure 1 below. These include the VIA environment, service requestor systems, and data source systems from a logical perspective.

![](vista-integration-adapter-viab-version-1-vip-user-guide/002.png)

<span id="_Toc454884981" class="anchor"></span>Figure : VIA High-Level Application Design

The To-Be environment utilizes a local DB (database) for internal application use, (e.g., logging and auditing). The DB must be available at all times for the system to continue operations successfully. If the DB becomes unavailable for any reason, the application services using the DB cannot continue to operate. System availability will be impacted because the existing DB must be taken offline for routine maintenance and system upgrades.

![](vista-integration-adapter-viab-version-1-vip-user-guide/003.png)

<span id="_Toc454884982" class="anchor"></span>Figure : VIA Production Hardware Configuration

There are three primary scenarios that the production configuration must be able to handle:

1.  Failure of a single application server – rules configured in the LTMs will remove the Internet Protocol (IP) address from the pool of available servers. The remaining active application servers will continue processing.
2.  Failure of a single DB server – Since there is a single DB server at each site, and the DB server must be available for processing, then VIA processing for the site cannot continue. Rules configured in the Global Traffic Manager (GTM) will disallow all VIA processing for that site by removing the IP address from the pool of available servers. The remaining active application servers will continue processing
3.  Failure of all application servers at one data center – rules established in the GTM will disallow VIA processing for that site.

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 3, below, illustrates the interface data flow between systems involved in the VIA service interactions. The interfaces can be categorized as 1) Front-End Systems, which act as clients who request data and 2) Back-End systems, which act as data provider systems.

![](vista-integration-adapter-viab-version-1-vip-user-guide/004.png)

<span id="_Toc454884983" class="anchor"></span>Figure : VIA Interface Architecture

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to manipulate DB structure and storage will be restricted to administrative-level users. These users will be the security operations staff and DB administrators, who will either make use of the security information or perform maintenance support of the DB infrastructure.

All application connectivity to the audit logs will be through a single user’s profile that will be configured to read and write data privileges. The DB user will have no permission to update or permanently remove data from the audit logs. This approach aligns with VA Directive 6500 on the access to audit data.

All application connectivity to the exception logs will be through a single user who will have full read, write, update, and delete access to the exception logs. The exception logs are for the sole purpose of monitoring and debugging middleware software behavior, so the requirement to reset the exception logs will occur with fair regularity.

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIA is middleware and will be hosted at AITC. VIA will adopt all of AITC’s contingencies in the event of emergency, disaster, or accident.

## Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To configure and install the supporting software for VIA, please refer to the following:

- [VIA Installation Manual](http://vaww.oed.portal.va.gov/projects/via/Documents/VIA%20Installation%20Manual.doc)
- [VIA Interface Control Document](http://vaww.oed.portal.va.gov/pm/hppmd/CSSS/VIA/Shared%20Documents/VIA%20Interface%20Control%20Document.docx)
- [VIA Interface Control Document Annex A](http://vaww.oed.portal.va.gov/pm/hppmd/CSSS/VIA/Shared%20Documents/VIA%20Interface%20Control%20Document%20Annex%20A.doc)
- [VIA Interface Control Document Annex B](http://vaww.oed.portal.va.gov/pm/hppmd/CSSS/VIA/Shared%20Documents/VIA%20Interface%20Control%20Document%20Annex%20B.doc)
- [VIA Interface Control Document Annex C](http://vaww.oed.portal.va.gov/pm/hppmd/CSSS/VIA/Shared%20Documents/VIA%20Interface%20Control%20Document%20Annex%20C.doc)
- [VIA Interface Control Document Annex D](http://vaww.oed.portal.va.gov/pm/hppmd/CSSS/VIA/Shared%20Documents/VIA%20Interface%20Control%20Document%20Annex%20D.doc)
- [VIA Interface Control Document Annex E](http://vaww.oed.portal.va.gov/pm/hppmd/CSSS/VIA/Shared%20Documents/VIA%20Interface%20Control%20Document%20Annex%20E.doc)
- [VIA Interface Control Document Annex F](http://vaww.oed.portal.va.gov/pm/hppmd/CSSS/VIA/Shared%20Documents/VIA%20Interface%20Control%20Document%20Annex%20F.doc)
- [VIA Interface Control Document Annex G](http://vaww.oed.portal.va.gov/pm/hppmd/CSSS/VIA/Shared%20Documents/VIA%20Interface%20Control%20Document%20Annex%20G.doc)

If your application is currently stateful, then the following documents should be helpful in the conversion from Stateful to Stateless:

[VIA Stateful to Stateless Conversion Guide](http://vaww.oed.portal.va.gov/projects/via/Documents/VIA%20Stateful%20To%20Stateless%20Conversion%20Guide.docx)

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIA is middleware; therefore, the consuming application (i.e., CPRS) is the source for log on.

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable.

## Changing User ID and Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIA is middleware; therefore, the consuming application is the source for log on. Although there is no password needed for VIA specifically, VIA will pass the authorization used to log into the consuming application. Changes to a user id or password will be handled by the consuming application.

## Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the user exits the consuming application, VIA is also exited.

## Caveats and Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must assign to users and Clinical Application Coordinators (CACs) the following secondary menu option. This option provides access to the VIA context created in the patch. If this option is not assigned, a user will not be able to utilize VIA. The VIA project team recommends working with your site’s IT staff to determine which users should receive the menu option.

The VIAB WEB SERVICES OPTION provides access to all RPC calls that VIA uses. Therefore, work with your site’s CACs to gather a list of VIA users and determine which views each user needs. Only assign the views that each user needs.

1.  Log in to VistA.
2.  At the Select OPTION NAME prompt, type EVE and then press the \<Enter\> key.
3.  At the Choose 1-5 prompt, type the number 1 (for EVE Systems Manager Menu) and press the \<Enter\> key.
4.  At the Select Systems Manager Menu Option prompt, type User Management and press the \<Enter\> key.
5.  At the Select User Management Option prompt, type edit (for Edit an Existing User) and press the \<Enter\> key.
6.  At the Select NEW PERSON NAME prompt, type the user’s name using the following format: lastname, firstname. Press the \<Enter\> key.
7.  Press the \<Down Arrow\> key to highlight the Select SECONDARY MENU OPTIONS field. (Type a question mark (?) to see a list of the secondary options that are currently assigned to the user.)
8.  In the SECONDARY MENU OPTIONS field, type VIAB WEB SERVICES OPTION, and then press the \<Enter\> key.
9.  At the Are you adding …as a new SECONDARY MENU OPTIONS (the…for this NEW PERSON)? No// prompt, type Yes and press the \<Enter\> key.
10. Press the \<Enter\> key again to accept this new option.
11. In the SYNONYM field, type a synonym for the option (optional). Press the \<Enter\> key.
12. Press the \<Enter\> key to close the COMMAND field and return to the Select SECONDARY MENU OPTIONS field.
13. Press the \<Down Arrow\> key to move through the Edit Existing User dialog. At the end of each page, type the letter n in the COMMAND field to enter the following page.
14. Stop on page 3.
15. Check the user’s person class, which appears on page 3, to make sure the user’s person class is active.
16. If the user’s person class is not active, select an active person class for the user.
17. When you have entered all applicable secondary menu options and verified that the user has an active person class, type the word Exit in the COMMAND field.
18. At the Save changes before leaving form (Y/N)? prompt, type the letter Y and press the \<Enter\> key.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[*<span class="mark">REDACTED</span>*](http://vaww.telehealth.va.gov/quality/tmp/index.asp).

## Special Instructions for Error Correction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the exception handling policies for VIA services. VIA exposes data from multiple data sources in the form of services provided to external systems (service requestors). These service requestors have their own policies for handling errors.

VIA is responsible for fulfilling the service request as long as the system is operational. The general error handling policies are provided below.

- Web Services (WS) standard SOAP exception handling will be used for communicating exceptions back to the service requestor. This will make use of SOAP faults to provide information regarding the exception.
- Standard Java exception handling will be used within service application code.
- When critical errors occur that place the system in an unrecoverable and unstable state, the application will terminate. These types of errors include code errors and missing resources (e.g., internal DB, configuration file, and runtime dependency). The rationale behind taking the extreme step of terminating the application is that if a critical error is raised and users are allowed to continue, all of the subsequent processing could be compromised. This could result in incorrect processing and corrupted data being stored in the DB.
- An error that occurs because of a data source being unavailable is a special condition. When this happens, the situation should be considered a non-fatal error and processing should continue so that the service request is fulfilled, with any available data successfully retrieved along with information specifying which data sources were unavailable. A use-case scenario for this would be retrieving EHR data for a patient with records at four VHA VistA sites. If one of the four sites was unavailable and the connection was to time out, the service would provide data from the three sites and indicate which site was unavailable.
- Exceptions will be caught and handled at the highest-level controlling entity (typically the Controller classes) in the method call chain. At this top level, exceptions will be logged using the Log4J logging mechanism. Encapsulating the logging functions at the highest level within the code structure is intended to avoid duplicate log entries. No other methods within the call chain should catch the error, unless it could add information relevant to resolving the error.
- Within the service or framework, catch blocks must not “eat” the exception. This refers to code where the exception is caught with an empty block or a block that simply displays information and allows the application to continue. This hides the error and could potentially leave the application in an unreliable state.
- Error information presented to the user must be meaningful to the user and must be information on which the user can act. If the user can take no corrective action, a message will be displayed indicating that the user should contact the Help Desk for Tier 1 support.
- All exceptions will be logged using VIA’s common Log4J logging framework.
- The Fail-Fast principle will be applied in all application code. The Fail-Fast principle states that errors will be identified as close to the source of the problem as possible and a suitable exception will be thrown. The rationale behind this principle is that when an error condition occurs within the code, it should be identified as soon as possible so that: 1) errors are not propagated to other parts of the code, and 2) the cause can be identifies and resolved quickly. If errors are not handled when they occur, the system may continue to process them and they can become more difficult to resolve.

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a table of acronyms and/or abbreviations used in this document and the meaning of each. Additional acronyms and definitions can be found in the [OIT Master Glossary](http://vaww.oed.wss.va.gov/process/OIT%20Master%20Glossary/Home.aspx).

| Term    | Definition                                                  |
|-------------|-----------------------------------------------------------------|
| AITC    | Austin Information Technology Center                            |
| BRD     | Business Requirements Document                                  |
| CPRS    | Computerized Patient Record System                              |
| CAC     | Clinical Application Coordinator                                |
| DB      | database                                                        |
| EHR     | Electronic Health Record                                        |
| GTM     | Global Traffic Manager                                          |
| IAM     | Identity and Access Management                                  |
| ICD     | Interface Control Document                                      |
| IT      | Information Technology                                          |
| JEE     | Java Enterprise Edition                                         |
| MDWS    | Medical Domain Web Services                                     |
| MS      | Milestone                                                       |
| PITC    | Philadelphia Information Technology Center                      |
| PWS     | Performance Work Statement                                      |
| SOAP    | Simple Object Access Protocol                                   |
| RESTful | Representational State Transfer                                 |
| RFC     | Request for Change                                              |
| RPC     | Remote Procedure Call                                           |
| SOAP    | Simple Object Access Protocol                                   |
| TRM     | Technical Reference Manual                                      |
| VHA     | Veterans Health Administration                                  |
| VIA     | VistA Integration Adapter                                       |
| VISTA   | Veterans Health Information Systems and Technology Architecture |

Acronyms and AbbreviationsThis table is a glossary of acronyms and abbreviations used in this document.

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable.
