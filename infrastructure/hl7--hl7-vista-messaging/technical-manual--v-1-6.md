---
title: HL7 V. 1.6 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: HL7
app_name: HL7 (VistA Messaging)
section: INF
app_status: active
pkg_ns: 
patch_ver: 1.6
patch_id: 
group_key: "HL7::1.6"
file_numbers: []
security_keys: []
menu_options: 8
description: 
audience: 
keywords: 
  - message
  - table
  - dhcp
  - contents
  - package
  - class
  - cont
  - application
  - protocol
  - routines
page_count: 0
word_count: 8520
section_count: 1
table_count: 16
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: October 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=8"
---

Decentralized Hospital Computer Program

DHCPhealth level seven(HL7)technical manual

October 1995

IRM Field Office

Albany, New York

Preface

The DHCP Health Level Seven (HL7) software package provides an interface that allows DHCP applications to exchange healthcare data with other applications using the HL7 protocol. This manual provides technical information for use by IRM Service personnel to operate and maintain the DHCP HL7 software.

Table of Contents

Introduction 1

> Overview 1

> The DHCP HL7 Package 2

> Lower Level Protocols 3

> The DHCP Interface to the HL7 Protocol 4

> Related Manuals 5

> Organization of this Manual 6

Resource Requirements 7

> Minimum Versions Required 7

> Resource Consumption 7

Implementation and Maintenance 9

> Implementation 9

> Maintenance 9

> Troubleshooting Tip 9

Routines 11

> Routine List with Descriptions 11

> Callable Routines 15

Files 19

> File List with Descriptions 19

> File Flow Chart 22

> Globals 24

> Global Growth 24

> Cross-reference Descriptions 24

Exported Options 35

> Menu Diagram 35

Archiving and Purging 41

> Archiving 41

> Purging 41

External Relations 43

> Minimum Versions Required 43

> Database Integration Agreements (DBIAs) 43

Internal Relations 47

> SACC Exemptions 47

  
Variables 49

> Package-wide Variables 49

> Basic Variables 49

> Arrays 54

How to Generate Online Documentation 55

> %Index 55

> Inquire Option 56

> Print Option File 56

> List File Attributes 57

Glossary 59

Appendix A. Sample HL7 Interface Specification 61

Appendix B. Supported HL7 Message Types 67

Index 69

Introduction

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
- [The DHCP HL7 Package](#the-dhcp-hl7-package)
- [Lower Level Protocols](#lower-level-protocols)
- [The DHCP Interface to the HL7 Protocol](#the-dhcp-interface-to-the-hl7-protocol)
- [Related Manuals](#related-manuals)
- [Organization of this Manual](#organization-of-this-manual)
- [Minimum Versions Required](#minimum-versions-required)
- [Resource Consumption](#resource-consumption)
- [Implementation](#implementation)
- [Maintenance](#maintenance)
- [Troubleshooting Tip](#troubleshooting-tip)
- [Routine List with Descriptions](#routine-list-with-descriptions)
- [Routine List with Descriptions, cont.](#routine-list-with-descriptions-cont)
- [Routine List with Descriptions, cont.](#routine-list-with-descriptions-cont-1)
- [Routine List with Descriptions, cont.](#routine-list-with-descriptions-cont-2)
- [Callable Routines](#callable-routines)
- [File List with Descriptions](#file-list-with-descriptions)
- [File Flow Chart](#file-flow-chart)
- [# Globals](#globals)
- [Global Growth](#global-growth)
- [Cross-reference Descriptions](#cross-reference-descriptions)
- [Menu Diagram](#menu-diagram)
- [Menu Diagram, cont.](#menu-diagram-cont)
- [Menu Diagram, cont.](#menu-diagram-cont-1)
- [Menu Diagram, cont.](#menu-diagram-cont-2)
- [Menu Diagram, cont.](#menu-diagram-cont-3)
- [Archiving](#archiving)
- [Purging](#purging)
- [Minimum Versions Required](#minimum-versions-required-1)
- [Database Integration Agreements (DBIAs)](#database-integration-agreements-dbias)
- [Database Integration Agreements (DBIAs), cont.](#database-integration-agreements-dbias-cont)
- [Database Integration Agreements (DBIAs), cont.](#database-integration-agreements-dbias-cont-1)
- [SACC Exemptions](#sacc-exemptions)
- [Package-wide Variables](#package-wide-variables)
- [Basic Variables](#basic-variables)
- [# # # Arrays](#arrays)
- [%Index](#index)
- [%Index, cont.](#index-cont)
- [Inquire Option](#inquire-option)
- [Print Option File](#print-option-file)
- [List File Attributes](#list-file-attributes)
The first step in understanding the DHCP Health Level Seven (HL7) package is a basic understanding of HL7 itself. HL7 is a standard protocol which specifies the implementation of interfaces between two computer applications (sender and receiver) for electronic data exchange in healthcare environments. HL7 allows healthcare institutions to exchange key sets of data from different application systems. Specifically, it defines the following:
- The data to be exchanged
- The timing of the interchange
- The communication of errors to the sending/receiving application
The formats are generic in nature, and must be configured to meet the needs of the two applications involved. An HL7 interface specification should be written detailing what formats (events, messages, segments, and fields) will be used, and the lower level protocol that will be implemented in order for the two applications to interface with one another. Appendix A of this manual is an example of an HL7 interface specification.
The HL7 protocol defines the content and format of abstract messages and transactions for interface capabilities for the following areas:
- Admission, discharge, and transfer (ADT)
- Order entry
- Query
- Financial applications such as charge, payment adjustments, and insurance
- Ancillary data reporting for Laboratory, Radiology, Pharmacy, etc.
In HL7, information is exchanged using HL7 messages when an event occurs in an application. Each HL7 message consists of one or more HL7 segments. A segment can be thought of as a record in a file. Each segment consists of one or more fields separated by a special character called the *field separator*. The field separator character is defined in the Message Header (MSH) segment of an HL7 message. The MSH segment is always the first segment in every HL7 message. Each field is assigned an HL7 data type (e.g., numeric, text, etc.).
Overview, cont.
In addition to the field separator character, there are four other special characters called *encoding characters*. Encoding characters are also defined in the MSH segment. They operate on a single field in an HL7 segment. Each encoding character must be unique, and serves a specific purpose. None of the encoding characters can be the same as the field separator character.
- The first encoding character is the *component separator*. Some data fields can be divided into multiple components. The component separator is used to separate adjacent components within a data field.
- The second encoding character is the *repetition separator*. Some data fields can be repeated multiple times in a segment. The repetition separator character is used to separate multiple occurrences of a field.
- The third encoding character is the *escape character*. Data fields defined as text or formatted text can include escape sequences. The escape character is used to separate escape sequences from the actual text.
- The fourth encoding character is the *sub-component separator*. Some data fields can be divided into components, and each component can be further divided into sub-components. The sub-component separator is used to separate adjacent sub-components within a component of a field.

# The DHCP HL7 Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the DHCP HL7 package is to assist DHCP applications in exchanging healthcare information with other applications using the HL7 protocol. The DHCP HL7 package consists of a set of utility routines and files that provide a generic interface to the HL7 protocol for all DHCP applications. The DHCP HL7 package can be divided into two parts:

- Lower level protocol support between sending and receiving applications
- DHCP interface to the HL7 protocol

# Lower Level Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The term lower level refers to a portion of the Open Systems Interconnect (OSI) model. The OSI model is divided into seven layers or levels. The lower levels (Layers 1 through 4) support the actual movement of data between systems. This includes the actual physical connection between the systems and the communications protocol used.

The DHCP HL7 package supports the following lower level interfaces:

- HL7 Hybrid Lower Layer Protocol over an RS-232 connection
- DHCP MailMan messages
- X3.28

Using these lower level interfaces, the DHCP HL7 package can support Layers 1 through 4 of the OSI model and eliminate the need for DHCP applications to write lower level interfaces each time they want to exchange data with another application.

These lower level interfaces provide the following functions:

- Receive and send HL7 messages.
- Validate the HL7 Message Header (MSH) information.
- Invoke the appropriate DHCP application routine to process the data in the message.
- Send HL7 accept acknowledgment (ACK) messages back to the sending application.

# The DHCP Interface to the HL7 Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the release of V. 1.6, DHCP HL7 supports several methods for interfacing to the HL7 protocol. The method established by V. 1.5 is still supported (for backwards compatibility), and a new method is introduced, as well as new routines, file structures, templates, menus, and options. There are some significant differences between the V. 1.5 and V. 1.6 interface methods, as shown in the following table.

|                                                     |                                                                                                                                  |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| V. 1.5 Interface Method                         | V. 1.6 Interface Method                                                                                                      |
| One sender and one receiver per message.            | One sender, one or more receivers.                                                                                               |
| Sender and receiver must be on different systems.   | Sender and receiver can be on the same or different systems.                                                                     |
| Messages must go through a communications protocol. | Messages sent to applications on the same system do not have to go through a communications protocol.                            |
| All messages are processed in the background.       | Messages are processed in either the foreground or background, based on the priority assigned by sending/receiving applications. |
| No support for event points.                        | Event points are supported.                                                                                                      |

The DHCP HL7 package assists DHCP applications in interfacing to the HL7 protocol. In addition to the lower levels mentioned previously, all applications must perform the following upper level functions in order to exchange data with another application:

- Event analysis
- Data extraction
- Data filing
- Data formatting
- Message administration

Currently, the functions of event analysis, data extraction, and data filing must be performed by each application package. The DHCP HL7 package provides the following utilities to assist the application package with data formatting:

- Creation of HL7 Message Header (MSH) segments
- Utility calls to convert HL7 data to VA FileMan formats and vice versa
- Validation of Message Header information for all HL7 messages received
- A set of pre-defined variables for use in building HL7 messages/segments

The DHCP Interface to the HL7 Protocol, cont.

The DHCP HL7 package provides the following functions to assist the application package with message administration:

- Support for tracking transmissions and providing a status for each
- Generation of reports on pending transmissions and transmissions with errors
- A queue for incoming and outgoing transmissions
- A real-time monitor to monitor active transmission links and their statuses

The DHCP HL7 package has been designed to be modular, table-driven, and extensible. It appears that with minor modifications, the package could support other protocols (e.g., EDI/X12) in addition to HL7. Current development efforts are concentrated on adding table-driven support for the functions of event analysis, data extraction, data filing, and data formatting. Once these three areas are automated, it will be possible for an application to implement a new HL7 interface to exchange data without writing M routines.

# Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For applications using the V. 1.6 interface method, you might also want to refer to the following manuals:

- DHCP HL7 V. 1.6 Developer Manual
- DHCP HL7 V. 1.6 Installation Guide
- DHCP HL7 V. 1.6 Package Security Guide
- DHCP HL7 V. 1.6 Release Notes
- DHCP HL7 V. 1.6 User Manual

For applications using the V. 1.5 interface method, you might also want to refer to the following manuals:

- DHCP HL7 V. 1.5 Developer Manual
- DHCP HL7 V. 1.5 Installation Guide
- DHCP HL7 V. 1.5 Package Security Guide
- DHCP HL7 V. 1.5 Release Notes
- DHCP HL7 V. 1.5 Technical Manual
- DHCP HL7 V. 1.5 User Manual

# Organization of this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information in this manual is divided into the following sections:

- *Preface* - States the purpose of the software and the intended audience for this manual.
- *Table of Contents* - Lists the topics in the order in which they appear in this manual.
- *Introduction* - Provides an overview of the software and its purpose, refers you to related manuals, and explains the organization of this manual.
- *Resource Requirements* - Discusses the software and hardware requirements for this version of DHCP HL7.
- *Implementation and Maintenance* - Points you to the instructions for implementing the software and its various tools; provides maintenance and troubleshooting tips.
- *Routines* - Provides a complete list of package routines with their descriptions and the supported entry points for this version with their descriptions and parameters.
- *Files* - Provides a complete list of package files and their descriptions; a flow chart to illustrate the pointer relationships between the various files; discussion about globals and global growth; and a complete list of package cross-references with their descriptions.
- *Exported Options* - Contains a menu diagram of all options exported with the package.
- *Archiving and Purging* - Discusses the archiving and purging capabilities of the package.
- *External Relations* - Provides a list of minimum versions of other packages that must be installed prior to installing this version of DHCP HL7, and contains a list of custodial Database Integration Agreements (DBIAs).
- *Internal Relations* - Discusses option dependencies and SACC exemptions.
- *Variables* - Provides a list of package variables and arrays with their descriptions.
- *How to Generate Online Documentation* - Provides tips for accessing technical online information.
- *Glossary* - Provides a list of terms used in this manual with their definitions.
- *Appendices* - Contain supplemental information.
- *Index* - Provides an alphabetical listing of the topics presented in this manual.

Resource Requirements

# Minimum Versions Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum package versions are required in order to install this version of DHCP HL7:

- Kernel V. 7.1
- VA FileMan V. 21.0
- VA FileMan V. 7.1
- OE/RR V. 2.5

# Resource Consumption

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The ^HL global will consume approximately 17K of disk space for static file entries, and about 1K of disk space for every 10 entries in the HL7 message text file (#772).
- The ^HLCS global will consume approximately 50K of disk space for every 100 messages (500 byte average length) in the HL LOGICAL LINK file (#870).
- The ^HLMA global will consume approximately 400 bytes for every 10 entries in the HL7 MESSAGE ADMINISTRATION file (#773).
- CPU usage is insignificant for a few links, but will increase linearly as more links are added.

Implementation and Maintenance

# Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DHCP HL7 V. 1.6 Installation Guide provides detailed step-by-step instructions for package implementation. To implement application interfaces, logical links, and client/server protocols, use the Interface Workbench \[HL INTERFACE WORKBENCH\] option in the V. 1.6 OPTIONS Menu \[HLMENU 1.6\].

# Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You should queue the Purge Message Text Entries \[HL PURGE TRANSMISSIONS\] option on the HL7 Main Menu (HL MAIN MENU) to run as a daily background task. This purges outgoing transmissions in the HL7 MESSAGE TEXT file (#772) that meet the following criteria:

- They have been successfully transmitted.
- They are at least seven days old.

You can also run the Purge Message Text Entries \[HL PURGE TRANSMISSIONS\] option from the menu to purge messages with a status of ERROR IN TRANSMISSION. *You should review error messages before using this option.*

# Troubleshooting Tip

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While the HL7 protocol requires no actual maintenance, you might want to refer to the Callable Routines in the Routines Section of this manual for guidance in troubleshooting, debugging, etc.

Routines

# Routine List with Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list of routines in V. 1.6 of the DHCP HL7 package is grouped into the following categories:

- Routines that support the V. 1.5 interface method
- Routines that support the V. 1.6 interface method
- Routines that support both the V. 1.5 and V. 1.6 interface methods

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 31%" />
<col style="width: 14%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Routine Name</strong></td>
<td><strong>Description</strong></td>
<td><strong>Version Supported</strong></td>
</tr>
<tr class="even">
<td>HLCHK</td>
<td>Validates data in the HL7 Message Header (MSH) segments of all incoming messages, and creates and sends “AR” error type acknowledgment messages.</td>
<td>V. 1.5</td>
</tr>
<tr class="odd">
<td>HLCS</td>
<td>Communications Server Module routine.</td>
<td>V. 1.6</td>
</tr>
<tr class="even">
<td>HLCS1</td>
<td>Manage incoming and outgoing filers menu [HL MANAGE FILERS] options.</td>
<td>V. 1.6</td>
</tr>
<tr class="odd">
<td>HLCSDL, HLCSDL1, HLCSDL2</td>
<td>X3.28 Lower Layer Protocol (LLP) routines.</td>
<td>V. 1.6</td>
</tr>
<tr class="even">
<td>HLCSDR, HLCSDR1, HLCSDR2</td>
<td>HL7 V. 2.2 Hybrid Lower Layer Protocol (HLLP) routines.</td>
<td>V. 1.6</td>
</tr>
<tr class="odd">
<td>HLCSFMN, HLCSFMN0, HLCSFMN1</td>
<td>Filer Monitor routines.</td>
<td>V. 1.6</td>
</tr>
<tr class="even">
<td>HLCSHDR</td>
<td>Creates an HL7 message header from an IEN in the MESSAGE TEST file (#772).</td>
<td>V. 1.6</td>
</tr>
<tr class="odd">
<td>HLCSIN</td>
<td>Incoming background filer.</td>
<td>V. 1.6</td>
</tr>
<tr class="even">
<td>HLCSLNCH</td>
<td><p>Start LLP [HL START] and Stop LLP [HL STOP] options on the Communications Server [HL COMMUNI-</p>
<p>CATIONS SERVER] menu.</p></td>
<td>V. 1.6</td>
</tr>
<tr class="odd">
<td>HLCSMM, HLCSMM1</td>
<td>MailMan LLP routines.</td>
<td>V. 1.6</td>
</tr>
<tr class="even">
<td>HLCSMON, HLCSMON1, HLCSTERM</td>
<td>Systems Link Monitor routines.</td>
<td>V. 1.6</td>
</tr>
<tr class="odd">
<td>HLCSORA1, HLCSORA2, HLCSORAT</td>
<td>Custom report routine.</td>
<td>V. 1.6</td>
</tr>
<tr class="even">
<td>HLCSOUT</td>
<td>Outgoing background filer.</td>
<td>V. 1.6</td>
</tr>
<tr class="odd">
<td>HLCSQUE, HLCSQUE1, HLCSQUED</td>
<td>Logical Link Queue Management utility routines.</td>
<td>V. 1.6</td>
</tr>
<tr class="even">
<td>HLCSRE1, HLCSREP, HLCSREQ, HLCSRES, HLCSRQ</td>
<td>Message Requeuer routines.</td>
<td>V. 1.6</td>
</tr>
</tbody>
</table>

# Routine List with Descriptions, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 31%" />
<col style="width: 14%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Routine Name</strong></td>
<td><strong>Description</strong></td>
<td><strong>Version Supported</strong></td>
</tr>
<tr class="even">
<td>HLCSRV</td>
<td>Server routine for HL7 messages received through MailMan.</td>
<td>V. 1.6</td>
</tr>
<tr class="odd">
<td>HLCSUTL, HLCSUTL1, HLCSUTL2</td>
<td>Communications Server utility routines.</td>
<td>V. 1.6</td>
</tr>
<tr class="even">
<td>HLDTIW01, HLDTIW02, HLDTIW01, HLDTIW03, HLDTIW04, HLDTIW05, HLDTIW2A, HLDTIW2B, HLDTIW2C, HLDTIWP0, HLDTIWP1, HLDTIWP2, HLDTIWP3, HLDTIWP4, HLDTIWP5, HLDTIWP6, HLDTIWU0, HLDTIWU1, HLDTIWU2, HLDTIWU3, HLDTIWU4, HLDTIWU5, HLLM, HLLM1</td>
<td>Interface Workbench Module routines.</td>
<td>V. 1.6</td>
</tr>
<tr class="odd">
<td>HLFNC, HLFNC1, HLFNC2, HLFNC3</td>
<td><p>Perform various functions, such as</p>
<ul>
<li><p>Format names, dates, and times in HL7 or VA FileMan format.</p></li>
<li><p>Convert lower case letters to uppercase.</p></li>
<li><p>Convert DHCP phone number and address to HL7 format.</p></li>
<li><p>Calculate M10 and M11 checksums, etc.</p></li>
</ul></td>
<td><p>Both: HLFNC, HLFNC1</p>
<p>V. 1.6: HLFNC2, HLFNC3</p></td>
</tr>
</tbody>
</table>

# Routine List with Descriptions, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                      |                       |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| Routine Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                      | Version Supported |
| HLINI001, HLINI002, HLINI003, HLINI004, HLINI005, HLINI006, HLINI007, HLINI008, HLINI009, HLINI00A, HLINI00B, HLINI00C, HLINI00D, HLINI00E, HLINI00F. HLINI00G, HLINI00H, HLINI00I, HLINI00J, HLINI00K, HLINI00L, HLINI00M, HLINI00N, HLINI00O, HLINI00P, HLINI00Q, HLINI00R, HLINI00S, HLINI00T, HLINI00U, HLINI00V, HLINI00W, HLINI00X, HLINI00Y, HLINI00Z, HLINI010, HLINI011, HLINI012, HLINI013, HLINI014, HLINI015, HLINI016, HLINI017, HLINI018, HLINI019, HLINI01A, HLINI01B, HLINI01C, HLINI01D, HLINI01E, HLINI01F, HLINI01G, HLINI01H, HLINI01I, HLINI01J, HLINI01K, HLINI01L, HLINI01M, HLINI01N, HLINI01O, HLINI01P, HLINI01Q, HLINI01R, HLINI01S, HLINI01T, HLINI01U, HLINI01V, HLINI01W, HLINI01X, HLINI01Y, HLINI01Z, HLINI020, HLINI021, HLINI022, HLINI023, HLINI024, HLINI025, HLINI026 HLINI027, HLINI028, HLINI029, HLINI02A, HLINI02B, HLINI02C, HLINI02D, HLINI02E, HLINI02F, HLINI02G, HLINI02H, HLINI02I, HLINI02J, HLINI02K, HLINI02L, HLINI02M, HLINI02N, HLINI02O, HLINI02P, HLINI02Q, HLINI02R, HLINI02S, HLINI02T, HLINI02U, HLINI02V, HLINI02W, HLINI02X, HLINI02Y, HLINI02Z, HLINI030, HLINI031, HLINIS, HLINIT, HLINIT1, HLINIT2, HLINIT3, HLINIT4, HLINIT5 | Init routines for DHCP HL7.                                                                                                                                                                                                                                                                                                                                                          | V. 1.6                |
| HLLP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Implements the HL7 Hybrid Lower Layer Protocol. It is used as a communication protocol between a DHCP and non-DHCP application when the two applications are linked together through a port-to-port connection. It receives messages that originate from non-DHCP applications and sends replies. It also sends messages that originate from DHCP applications and receives replies. | V. 1.5                |
| HLMA, HLMA0, HLMA1, HLMA2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Message Administration Module routines.                                                                                                                                                                                                                                                                                                                                              | V. 1.6                |

# Routine List with Descriptions, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 31%" />
<col style="width: 14%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Routine Name</strong></td>
<td><strong>Description</strong></td>
<td><strong>Version Supported</strong></td>
</tr>
<tr class="even">
<td>HLNTEG, HLNTEG0</td>
<td>Integrity routines for the DHCP HL7 package. They provide checksums for the DHCP HL7 routines.</td>
<td>V. 1.6</td>
</tr>
<tr class="odd">
<td>HLONI001, HLONI002, HLONI003, HLONI004, HLONI005, HLONI006, HLONI007, HLONI008, HLONI009, HLONI010, HLONI011, HLONIT, HLONIT1, HLONIT2, HLONIT3</td>
<td>Omit routines for DHCP HL7.</td>
<td>V. 1.6</td>
</tr>
<tr class="even">
<td>HLOPT, HLOPT1</td>
<td>Driver for all edit, print, and purge options in the DHCP HL7 package.</td>
<td>V. 1.5</td>
</tr>
<tr class="odd">
<td>HLPOST, HLPOST16, HLPOSTQ</td>
<td>Post-init routines for DHCP HL7.</td>
<td>V. 1.6</td>
</tr>
<tr class="even">
<td>HLPRE16</td>
<td>Pre-init routine for DHCP HL7.</td>
<td>V. 1.6</td>
</tr>
<tr class="odd">
<td>HLSERV</td>
<td>Receives incoming HL7 messages from non-DHCP applications through DHCP MailMan and sends back acknowledgment messages.</td>
<td>V. 1.5</td>
</tr>
<tr class="even">
<td>HLTASK</td>
<td>Called to create a background task to start the HL7 Hybrid Lower Layer Protocol routine HLLP for a non-DHCP application ad purge HL7 transmissions.</td>
<td>Both</td>
</tr>
<tr class="odd">
<td>HLTF, HLTF0, HLTF1</td>
<td>Called by the HLLP, HLSERV, HLTRANS, and HLCHK routines to record various information in the HL7 MESSAGE TEXT file (#772) for incoming and outgoing HL7 messages.</td>
<td><p>Both: HLTF</p>
<p>V. 1.6: HLTF0, HLTF1</p></td>
</tr>
<tr class="even">
<td>HLTP, HLTP0, HLTP01, HLTP1, HLTP2, HLTPCK1, HLTPCK1A</td>
<td>Transaction Processor Module routines.</td>
<td>V. 1.6</td>
</tr>
<tr class="odd">
<td>HLTRANS</td>
<td>Called by DHCP applications to create messages to send to non-DHCP applications. It interfaces with DHCP MailMan and the HLLP routine to transmit HL7 messages that it creates. It also interfaces with the HLTF routine to record information in the HL7 MESSAGE TEXT file (#772).</td>
<td>V. 1.5</td>
</tr>
<tr class="even">
<td>HLUOPT, HLUOPT1, HLUTIL1, HLUTIL2, HLUTIL3</td>
<td>HL7 utility routines.</td>
<td>V. 1.6</td>
</tr>
</tbody>
</table>

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of supported entry points into routines belonging to the DHCP HL7 package. These entry points should be used by individual DHCP packages using the V. 1.6 interface method. For each entry point listed, the following information is provided:

- Entry point name and description
- Required/optional input parameters
- Output parameters, if applicable

CREATE^HLTF(HLMID,MTIEN,HLDT,HLDT1)

If a batch of HL7 messages (more than one) is to be created, the application processing routine should invoke this entry point to obtain a message ID for the message being sent, and to create an entry in the MESSAGE TEXT file (#772).

Required Input Parameters: HLDT, HLDT1, HLMID, MTIEN

(These parameters must be passed by reference.)

Output Parameters: All of the above input variables are returned as output variables.

GENACK^HLMA1(HLEID,HLMTIENS,HLEIDS,HLARYTYP,HLFORMAT,

HLRESLTA,HLMTIENA,HLP)

After the MSH segment is created, the application processing routine should invoke this entry point to send the acknowledgment message, then quit to pass control back to the DHCP HL7 package

Required Input Parameters: HLEID, HLMTIENS, HLEIDS, HLARYTYP, HLFORMAT, HLRESLTA, HLMTIENA, HLP

(HLRESLTA must be passed by reference.)

Optional Input Parameters: HLMTIENA, HLP("PRIORITY"), HLP("SECURITY")

Output Parameters: HLRESLTA

Several formats may be returned in this 

    variable/parameter. Any string that contains a

    value in a second caret piece indicates that the

    generation of an acknowledgement message was NOT

   successful. 

Successful calls are indicated by the

   possible return values:

-NULL

-MESSAGE ID

   Values indicating no acknowledgement was generated

    include:

-MESSAGE ID^ERROR (IN SEVERAL DIFFERENT

  FORMATS)

-0^IEN 771.7^ACTUAL ERROR MESSAGE

-IEN 771.7^ACUTUAL ERROR MESSAGE

-^ACTUAL ERROR MESSAGE

Because of the format variations possible in the

return string, it is recommended that calling

applications not try to interpret or rely on the

specific values returned in the string and only

use the existence or absence of a second piece

to determine whether the call was successful.

GENERATE^HLMA(HLEID,HLARYTYP,HLFORMAT,HLRESLT,HLMTIEN,HLP)

When this entry point is invoked, it loads the data in the HLA(“HLS”) local array or the ^TMP(“HLS”) global array into the message text file (#772), and the entry in the message text file (#772) is completed. The message is then delivered to the subscribers to the event driver protocol specified in the protocol file (#101). If the call to GENERATE^HLMA is successful, the HLreslt parameter will be returned equal to the message id assigned to the message that was created. If the call was not successful, the HLreslt parameter will be returned with the following three prices of data: message id (or 0 if no message id was assigned)^error code^error message.

Required Input Parameters: HLEID, HLARAYTYP, HLFORMAT, HLRESLT

(HLreslt must be passed by reference.)

Optional Input Parameters: HLMTIEN, HLP("PRIORITY"), HLP("SECURITY"), HLP("CONTPTR")

Output Parameters: HLreslt

Callable Routines, cont.

INIT^HLFNC2(EID,HL,INT)

To transmit HL7 messages, the DHCP application must develop a m routine (or, optionally, an entry point in a routine) for each type of HL7 message it will be sending. (Please refer to Appendix B for a list of supported HL7 message types.) The m routine should invoke this subroutine entry point to initialize variables needed to build an HL7 message for transmission to the receiving application.

Input Parameters: EID, HL

(HL must be passed by reference.)

Optional Input Parameters INT

Output Parameters: HL("ACAT"), HL("APAT"), HL("cc"), HL("ECH"), HL("ETN"), HL("FS"), HL("MTN")HL("PID"), HL("q"), HL("SAN"), HL("SAF"), HL("ver")

MSH^HLFNC2(HL,MID,RESULT,SECURITY

This is a function call used to build MSH segments if a batch of HL7 messages (more than one) is being created. The message ID for each MSH segment should be created by concatenating together:

1.  The message ID returned by the call to CREATE^HLTF
2.  A hyphen
3.  A sequential, whole number starting with 1 (e.g., 12345-1).

*NOTE: If only one HL7 message is being created, the routine should not make the call to CREATE^HLTF or create the MSH segment. The DHCP HL7 package will create the MSH segment for you.*

Required Input Parameters: HL, MID, RESULT

Optional Input Parameters: SECURITY

Output Parameter: RESULT

Files

# File List with Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of files associated with DHCP HL7 V. 1.6 and their descriptions. Per VHA Directive 10-93-142 regarding security of software, some of the DHCP HL7 Data Dictionaries are not to be modified. The file descriptions of these files are so noted.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 30%" />
<col style="width: 57%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>File #</strong></td>
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>101</td>
<td>Protocol</td>
<td><p>A number of fields have been added to the Protocol file (#101) to support messaging protocols for event drivers and event subscribers. The following two values were added to the Type field (#4) of the Protocol file (#101):</p>
<p>E for Event Driver</p>
<p>S for Subscriber</p></td>
</tr>
<tr class="odd">
<td>770</td>
<td>HL7 NON-DHCP APPLICATION PARAMETER</td>
<td>This is the main file that sites must edit before they can begin receiving HL7 transmissions from another system using the V. 1.5 interface. It contains parameters associated with non-DHCP applications from which the DHCP system can accept HL7 transmissions. Use the Non-DHCP Application Parameter Enter/Edit [HL EDIT SITE PARAM] option on the V. 1.5 OPTIONS [HL MENU 1.5] menu to create/edit entries in this file. (Please refer to the DHCP HL7 V. 1.6 User Manual.)</td>
</tr>
<tr class="even">
<td>771</td>
<td><p>HL7 APPLICATION PARAMETER</p>
<p>(Former name: HL7 DHCP APPLICATION PARAMETER in V. 1.5)</p></td>
<td><p>This file contains a list of DHCP applications that are capable of sending/receiving HL7 transmissions for the V. 1.6 interface. It also contains application-specific parameters related to HL7 segments and messages used by each application. Before a site can receive HL7 transmissions, the application to which the HL7 transmissions are to be sent must be defined in this file by using the Interface Workbench [HL INTERFACE WORKBENCH] option on the V. 1.6 OPTIONS [HL MENU 1.6] menu. (Please refer to the DHCP HL7 V. 1.6 User Manual.) The application can be activated in either of the following ways:</p>
<ul>
<li><p>Use the Activate/Inactivate action on the Currently Defined Applications screen of the Interface Workbench [HL INTERFACE WORKBENCH] option on the V. 1.6 OPTIONS [HL MENU 1.6] menu.</p></li>
<li><p>Use the Activate/Inactivate [HL EDIT APPL PARAM] option on the HL7 Main Menu (HL MAIN MENU).</p></li>
</ul></td>
</tr>
</tbody>
</table>

File List with Descriptions, cont.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 30%" />
<col style="width: 57%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>File #</strong></td>
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>771.1*</td>
<td>HL7 FIELD</td>
<td>This file contains the definition of each standard field used by the system. The definitions in this file can be compiled into routines which can perform the basic checks of data received from, or sent to, another system.</td>
</tr>
<tr class="odd">
<td>771.2*</td>
<td>HL7 MESSAGE TYPE</td>
<td>This file contains a list of HL7 messages supported by the DHCP site.</td>
</tr>
<tr class="even">
<td>771.3*</td>
<td><p>HL7 SEGMENT TYPE</p>
<p>(Former name: HL7 SEGMENT NAME in</p>
<p>V. 1.5)</p></td>
<td>This file contains a list of HL7 segments supported by the DHCP site.</td>
</tr>
<tr class="odd">
<td>771.4*</td>
<td>HL7 DATA TYPE</td>
<td>This file contains a list of HL7 data types and their corresponding processing rules.</td>
</tr>
<tr class="even">
<td>771.5*</td>
<td><p>HL7 VERSION</p>
<p>(Former name: HL7 VERSION SUPPORTED in V. 1.5)</p></td>
<td>This file contains a list of HL7 versions supported by the DHCP site.</td>
</tr>
<tr class="odd">
<td>771.6*</td>
<td>HL7 MESSAGE STATUS</td>
<td>This file is a table of statuses that are assigned to entries in the Message Text file (#772) by the Messaging System.</td>
</tr>
<tr class="even">
<td>771.7*</td>
<td>HL7 ERROR MESSAGE</td>
<td>This file is a table of error codes and messages that can be assigned to entries in the Message Text file (#772) by the Messaging System.</td>
</tr>
<tr class="odd">
<td>771.8*</td>
<td>HL7 STANDARD</td>
<td>This file is a table of standard protocols supported by the Messaging System. <em>This file should not be modified locally.</em></td>
</tr>
<tr class="even">
<td>772</td>
<td><p>HL7 MESSAGE TEXT</p>
<p>(Former name: HL7 TRANSMISSION in V. 1.5)</p></td>
<td>This file contains information related to the processing of all incoming and outgoing HL7 messages.</td>
</tr>
<tr class="odd">
<td>773</td>
<td>HL7 MESSAGE ADMINISTRATION</td>
<td>This file is used to create and maintain unique message IDs. It also contains a date/time when each ID was created.</td>
</tr>
<tr class="even">
<td>779.001*</td>
<td>HL7 EVENT TYPE CODE</td>
<td>This file is a table of event codes that are used by the Messaging System. <em>This file should not be modified locally.</em></td>
</tr>
<tr class="odd">
<td>779.002*</td>
<td><p>HL7 ACKNOWLEDGE-</p>
<p>MENT CODE</p></td>
<td>This file is a table of codes used by the Messaging System when processing acknowledgment messages. <em>This file should not be modified locally.</em></td>
</tr>
<tr class="even">
<td>779.003*</td>
<td>HL7 ACCEPT/APPLICATION ACK CONDITION</td>
<td>This file is a table of codes used by the Messaging System when processing acknowledgment messages. <em>This file should not be modified locally.</em></td>
</tr>
<tr class="odd">
<td>779.004*</td>
<td>COUNTRY CODE</td>
<td>This file is a table of country codes that are used by the Messaging System when building message header segments. <em>This file should not be modified locally.</em></td>
</tr>
<tr class="even">
<td>869.1</td>
<td>HL LOWER LEVEL PROTOCOL TYPE</td>
<td>This file contains the valid lower layer protocols for use with the HL7 package.</td>
</tr>
</tbody>
</table>

\* File comes with data which will overwrite existing data.

File List with Descriptions, cont.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 30%" />
<col style="width: 57%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>File #</strong></td>
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>869.2</td>
<td>HL LOWER LEVEL PROTOCOL PARAMETER</td>
<td>This file contains the lower layer protocol parameters used by the HL7 package.</td>
</tr>
<tr class="odd">
<td>869.3</td>
<td>HL COMMUNICATION SERVER PARAMETERS</td>
<td>This is the parameter file used by the HL7 Communications Server.</td>
</tr>
<tr class="even">
<td>870*</td>
<td>HL LOGICAL LINK</td>
<td><p>This file serves two purposes:</p>
<p>1. It is a FileMan-compatible transmission log.</p>
<p>2. The Lower Layer Protocols write and read directly from this file. (See routines HLCSDR1 and HLCSDR2.)</p>
<p>This file stores parameters that govern the behavior of the Lower Layer Protocols. It also stores information that drives the Systems Link Monitor [HL MESSAGE MONITOR] display option on the Communications Server [HL COMMUNICATIONS SERVER] submenu of the V. 1.6 OPTIONS menu [HL MENU 1.6].</p></td>
</tr>
</tbody>
</table>

\* File comes with data which will overwrite existing data.

# File Flow Chart

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>file \# and name</u> <u>points to</u> <u>pointed to by</u>

770 3.8 MAIL GROUP

HL7 NON-DHCP 771 HL7 APPLICATION

APPLICATION PARAMETER

PARAMETER 771.5 HL7 VERSION

771 3.8 MAIL GROUP 101 PROTOCOL

HL7 APPLICATION 771.2 HL7 MESSAGE TYPE 770 HL7 NON-DHCP

PARAMETER 771.3 HL7 SEGMENT TYPE APPLICATION

779.004 COUNTRY CODE PARAMETER

771.1 HL7 FIELD

772 HL7 MESSAGE TEXT

771.1 1 FILE

HL7 FIELD 771 HL7 APPLICATION 771.1 HL7 FIELD

PARAMETER

771.1 HL7 FIELD

771.3 HL7 SEGMENT TYPE

771.4 HL7 DATA TYPE

771.5 HL7 VERSION

771.2 771.5 HL7 VERSION 101 PROTOCOL

HL7 MESSAGE TYPE 771 HL7 APPLICATION

PARAMETER

771.3 771.5 HL7 VERSION 301.5 IVM PATIENT

HL7 SEGMENT NAME 771 HL7 APPLICATION

PARAMETER

771.1 HL7 FIELD

771.4 771.5 HL7 VERSION 771.1 HL7 FIELD

HL7 DATA TYPE771.5 771.8 HL7 STANDARD 101 PROTOCOL

HL7 VERSION 770 HL7 NON-DHCP

APPLICATION

PARAMETER

771.1 HL7 FIELD

771.2 HL7 MESSAGE TYPE

771.3 HL7 SEGMENT TYPE

771.4 HL7 DATA TYPE

779.001 HL7 EVENT TYPE

CODE

779.002 HL7 ACKNOWLEDGE-

MENT CODE

779.003 HL7 ACCEPT/

APPLICATION ACK

CONDITION

779.004 COUNTRY CODE

  
File Flow Chart, cont.

<u>file \# and name</u> <u>points to</u> <u>pointed to by</u>

771.6 772 HL7 MESSAGE TEXT

HL7 MESSAGE STATUS771.7 870 HL LOGICAL LINK

HL7 ERROR MESSAGE771.8 771.5 HL7 VERSION

HL7 STANDARD772 101 PROTOCOL 772 HL7 MESSAGE TEXT

HL7 MESSAGE TEXT 771 HL7 APPLICATION

PARAMETER

771.6 HL7 MESSAGE STATUS

772 HL7 MESSAGE TEXT

773 HL7 MESSAGE

ADMINISTRATION

870 HL LOGICAL LINK

773 772 hl7 message text

HL7 MESSAGEADMINISTRATION779.001 771.5 HL7 VERSION 101 PROTOCOL

HL7 EVENT TYPE CODE779.002 771.5 HL7 VERSION

HL7 ACKNOWLEDGE-MENT CODE779.003 771.5 HL7 VERSION 101 PROTOCOL

HL7 ACCEPT/APPLICATION ACKCONDITION779.004 771.5 HL7 VERSION 771 HL7 APPLICATION

country code parameter

869.1 869.2 HL LOWER LEVEL HL LOWER LEVEL PROTOCOL

PROTOCOL TYPE PARAMETER

869.2 3.5 DEVICE 870 HL LOGICAL LINK

HL LOWER LEVEL 3.8 MAIL GROUP

PROTOCOL PARAMETER 869.1 HL LOWER LEVEL

PROTOCOL TYPE

870 771.7 HL7 ERROR MESSAGE 101 PROTOCOL

HL LOGICAL LINK 869.2 HL LOWER LEVEL 772 HL7 MESSAGE TEXT

PROTOCOL PARAMETER

# # Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The globals ^HL, ^HLCS, and ^HLMA are the globals for DHCP HL7 V. 1.6. It is recommended that only ^HL and ^HLMA be journaled.

# Global Growth

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The ^HL global will consume approximately 17K of disk space for static file entries, and about 1K of disk space for every 10 entries in the HL7 TRANSMISSION file (#772).
- The ^HLCS global will consume approximately 50K of disk space for every 100 messages (500 byte average length) in the HL LOGICAL LINK (#870) file.
- The ^HLMA global will consume approximately 400 bytes for every 10 entries in the HL7 MESSAGE ADMINISTRATION file (#773).

# Cross-reference Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

770 HL7 NON-DHCP APPLICATION PARAMETER

> .01 NAME

> 770^B

> Regular “B” cross-reference.

> 770^AC^MUMPS

> This cross-reference is used in conjunction with the “AF” cross-reference on the FACILITY NAME field (#3) of the HL7 NON-DHCP APPLICATION PARAMETER file (#770) to validate the non-DHCP application name and non-DHCP facility name that are contained in the message header of each HL7 message that is received. This is a multi-key cross-reference which contains the name of the non-DHCP application in the first piece and the name of the non-DHCP facility in the second piece.

> 770^AD^MUMPS

> This cross-reference is used in conjunction with the “AE” cross-reference on the DHCP STATION NUMBER field (#2) of the HL7 NON-DHCP APPLICATION PARAMETER file (#770) to validate the receiving DHCP facility for an HL7 message. This information is contained in the message header that is received with every HL7 message. This is a multi-key cross-reference that contains the name of the non-DHCP application in the first piece and the DHCP station number in the second piece.

Cross-reference Descriptions, cont.

770 HL7 NON-DHCP APPLICATION PARAMETER, cont.

> 2 DHCP STATION NUMBER

> 770^AE^MUMPS

> This is the corresponding cross-reference to the “AD” cross-reference on the \#.01 Field. See the description on the ”AD” cross-reference for further information.

> 770^AF^MUMPS

> This is the corresponding cross-reference to the “AC” cross-reference on the \#.01 Field. See the description for the “AC” cross-reference for further information.

> 6 HL7 DEVICE

> 770^AL^MUMPS

> This cross-reference is used in conjunction with the “ALOG” cross-reference on the Start/Stop Transmission Log field (#50) of the HL7 Non-DHCP Application Parameter file (#770). When the value of Field \#50 is set to Start Transmission Log and the HL7 Device field (#6) in the HL7 Non-DHCP Application Parameter file (#770) is defined, the “ALOG” cross-reference is set. The “ALOG” cross-reference is used as a flag by the HL7 lower level protocol routine (HLLP) to determine when to start and stop logging information related to HL7 transmissions. The log can be turned on during initial testing of the HL7 link and anytime additional debugging is needed. The information captured by the log is stored in nodes descendant from the ^TMP("HL",ION) node, where ION is the name of the DHCP device that is specified as the HL7 device in Field \#6 of the HL7 Non-DHCP Application Parameter file (#770).

> 8 DHCP APPLICATION

> 770^AG

> Regular cross-reference for relating DHCP applications to non-DHCP applications.

> 50 START/STOP TRANSMISSION LOG

> 770^ALOG^MUMPS

This cross-reference is used in conjunction with the “AL” cross-reference on the HL7 Device field (#6) of the HL7 Non-DHCP Application Parameter file (#770) to set/delete a flag for starting/stopping the logging of HL7 transmission information. See the description of the “AL” cross-reference for further information.

Cross-reference Descriptions, cont.

771 HL7 APPLICATION PARAMETER

> .01 NAME

> 771^B

> Regular “B” cross-reference.

> 771^AC^MUMPS

> This cross-reference is used in conjunction with the “AF” cross-reference on the Active/Inactive field (#2) to determine whether a specific application is active.

> 2 ACTIVE/INACTIVE

> 771^AF^MUMPS

> This cross-reference is used in conjunction with the “AC” cross-reference on the Name field (#.01) to determine whether a specific DHCP application is active.

> .05, .01 HL7 SEGMENT

> 771.05^B

> Regular “B” cross-reference.

> .06, .01 HL7 MESSAGE

> 771.06^B

> Regular “B” cross-reference.

771.1 HL7 FIELD

> .01 NAME

> 771.1^B

> Regular “B” cross-reference.

> 2 SEGMENT

> 771.1^C

> Regular cross-reference to look up entries by HL7 segment name.

Cross-reference Descriptions, cont.

771.1 HL7 FIELD, cont.

> .13, .01 APPLICATION

> 771.113^B

> Regular “B” cross-reference.

> 2, .01 VERSION

> 771.12^B

> Regular “B” cross-reference.

771.2 HL7 MESSAGE TYPE

> .01 ABBREVIATED NAME

> 771.2^B

> Regular “B” cross-reference.

> 3, .01 VERSION

> 771.23^B

> Regular “B” cross-reference.

771.3 HL7 SEGMENT TYPE

> .01 ABBREVIATED NAME

> 771.3^B

> Regular “B” cross-reference.

> 3, .01 VERSION

> 771.33^B

> Regular “B” cross-reference.

Cross-reference Descriptions, cont.

771.4 HL7 DATA TYPE

> .01 NAME

> 771.4^B

> Regular “B” cross-reference.

> 3, .01 VERSION

> 771.43^B

> Regular “B” cross-reference.

771.5 HL7 VERSION

> .01 VERSION

> 771.5^B

> Regular “B” cross-reference.

771.6 HL7 MESSAGE STATUS

> .01 NAME

> 771.6^B

> Regular “B” cross-reference.

771.7 HL7 ERROR MESSAGE

> .01 SHORT TEXT

> 771.7^B

> Regular “B” cross-reference.

771.8 HL7 STANDARD

> .01 NAME

> 771.8^B

> Regular “B” cross-reference.

Cross-reference Descriptions, cont.

772 HL7 MESSAGE TEXT

> .01 DATE/TIME ENTERED

> 772^B

> Regular “B” cross-reference.

> 3 CLIENT APPLICATION

> 772^AE^MUMPS

> This cross-reference is used in conjunction with the “AC” cross-reference on the Transmission Type field (#4) and the “AD” cross-reference on the Date/Time Processed field (#21) to determine outgoing transmissions for a specific application that need to be transmitted.

> 772^AG^MUMPS

> This cross-reference is used in conjunction with the “AH” cross-reference on the Message ID field (#6) to look up and link initial HL7 messages with reply/acknowledgment messages.

> 772^AI^MUMPS

> This cross-reference is used in conjunction with the “AJ” cross-reference on the Original Message Text field (#8) to look up a subscriber entry based on the server entry to which it is linked.

> 4 TRANSMISSION TYPE

> 772^AC^MUMPS

> This cross-reference is used in conjunction with the “AE” cross-reference on the Client Application field (#3) and the “AD” cross-reference on the Date/Time Processed field (#21) to determine outgoing transmissions for a specific application that need to be transmitted.

> 6 MESSAGE ID

> 772^C

> This cross-reference is used in conjunction with the “AG” cross-reference on the Non-DHCP Application field (#3) to look up and link initial HL7 messages with reply/acknowledgment messages.

> 772^AH^MUMPS

> This cross-reference is used in conjunction with the “AG” cross-reference on the Non-DHCP Application field (#3) to look up and link initial HL7 messages with reply/acknowledgment messages.

Cross-reference Descriptions, cont.

772 HL7 MESSAGE TEXT, cont.

> 8 PARENT MESSAGE

> 772^AJ^MUMPS

> This cross-reference is used in conjunction with the “AI” cross-reference on the Client Application field (#3) to look up a subscriber entry based on the server entry to which it is linked.

> 11 LOGICAL LINK

> 772^STATUS2^MUMPS

> M-type cross-reference used by background job to dequeue messages for external systems.

> 20 STATUS

> 772^AF

> This cross-reference is used to produce the Awaiting/Pending HL7 Transmissions and Failed HL7 Transmissions reports.

> 772^STATUS1^MUMPS

> M-type cross-reference that background job \$Os through to dequeue messages for external systems.

> 21 DATE/TIME PROCESSED

> 772^AD^MUMPS

> This cross-reference is used in conjunction with the “AE” cross-reference on the Client Application field (#3) and the “AC” cross-reference on the Transmission Type field (#4) to determine outgoing transmissions for a specific application that need to be transmitted.

773 HL7 MESSAGE ADMINISTRATION

> .01 DATE/TIME ENTERED

> 773^B

> Regular “B” cross-reference.

Cross-reference Descriptions, cont.

779.001 HL7 EVENT TYPE CODE

> .01 CODE

> 779.001^B

> Regular “B” cross-reference.

> 01, .01 VERSION

> 779.0101^B

> Regular “B” cross-reference.

779.002 HL7 ACKNOWLEDGEMENT CODE

> .01 CODE

> 779.002^B

> Regular “B” cross-reference.

> 01, .01 VERSION

> 779.00201^B

> Regular “B” cross-reference.

779.003 HL7 ACCEPT/APPLICATION ACK CONDITION

> .01 CODE

> 779.003^B

> Regular “B” cross-reference.

> 01, .01 VERSION

> 779.00301^B

> Regular “B” cross-reference.

Cross-reference Descriptions, cont.

779.004 COUNTRY CODE

> .01 CODE

> 779.004^B

> Regular “B” cross-reference.

> 01, .01 VERSION

> 779.00401^B

> Regular “B” cross-reference.

869.1 HL LOWER LEVEL PROTOCOL TYPE

> .01 NAME

> 869.1^B

> Regular “B” cross-reference.

869.2 HL LOWER LEVEL PROTOCOL PARAMETER

> .01 NAME

> 869.2^B

> Regular “B” cross-reference.

869.3 HL COMMUNICATION SERVER PARAMETERS

> .01 ONE

> 869.3^B

> Regular “B” cross-reference.

> 32, .01 INCOMING FILER TASK NUMBER

> 869.32^B

> Regular “B” cross-reference.

Cross-reference Descriptions, cont.

869.3 HL COMMUNICATION SERVER PARAMETERS, cont.

> 33, .01 OUTGOING FILER TASK NUMBER

> 869.33^B

> Regular “B” cross-reference.

870 HL LOGICAL LINK

> .01 NODE

> 870^B

> Regular “B” cross-reference.

> 2 LLP PARAMETERS

> 870^ALLP

> This cross-reference is used to link the HL LOWER LEVEL PROTOCOL PARAMETER file (#869.2) with the HL LOGICAL LINK file (#870). Using this cross-reference, you can locate the parameter associated with this link.

> 019, .01 MESSAGE NUMBER

> 870.019^B

> Regular “B” cross-reference.

> .01, .01 MESSAGE NUMBER

> 870.01^B

> Regular “B” cross-reference.

Exported Options

# Menu Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following menu should be distributed to the appropriate IRM personnel. There are no locks or restrictions.

HL7 Main Menu (HL MAIN MENU)

\|

\|

----1 V1.5 -----------------------------------------------------1 Non-DHCP

OPTIONS Application

\[HL MENU Parameter

1.5\] Enter/Edit

\| \[HL EDIT

\| SITE PARAM

\|

\|-----------------------------------------------------2 Initiate

\| Background

\| Task \[HL

\| TASK\]

\|

\|-----------------------------------------------------3 Start/Stop

Log of HL7

Transmissions

\[HL TRANSMISSION

LOG\]

----2 V1.6 -------------1 Communications------------------------1 Edit

OPTIONS Server Communication

\[HL MENU \[HL COMMUNICATIONS Server

1.6\] SERVER\] parameters

\| \[HL EDIT COMM

\| \| SERVER

\| \| PARAMETERS\]

\| \|

\| \|-------------2 Manage -----------1 Start

\| \| incoming & default

\| \| outgoing number of

\| \| filers \[HL incoming &

\| \| MANAGE outgoing

\| \| FILERS\] filers \[HL

\| \| \| START

\| \| \| DEFAULT

\| \| \| FILERS\]

\| \| \|

\| \| \|-------------2 Start an

\| \| \| incoming

\| \| \| filer \[HL

\| \| \| START ONE

\| \| \| INCOMING

\| \| \| FILER\]

\| \| \|

# Menu Diagram, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\| \| \|-------------3 Start an

\| \| \| outgoing

\| \| \| filer \[HL

\| \| \| START ONE

\| \| \| OUTGOING

\| \| \| FILER\]

\| \| \|

\| \| \|-------------4 Stop all

\| \| \| incoming

\| \| \| filers \[HL

\| \| \| STOP ALL

\| \| \| INCOMING

\| \| \| FILERS\]

\| \| \|

\| \| \|-------------5 Stop all

\| \| \| outgoing

\| \| \| filers \[HL

\| \| \| STOP ALL

\| \| \| OUTGOING

\| \| \| FILERS\]

\| \| \|

\| \| \|-------------6 Stop an

\| \| \| incoming

\| \| \| filer \[HL

\| \| \| STOP ONE

\| \| \| INCOMING

\| \| \| FILER\]

\| \| \|

\| \| \|-------------7 Stop an

\| \| outgoing

\| \| filer \[HL

\| \| STOP ONE

\| \| OUTGOING

\| \| FILER\]

\| \|

\| \|

\| \|---------------------------------3 Monitor

\| \| incoming &

\| \| outgoing

\| \| filers \[HL

\| \| FILER

\| \| MONITOR\]

\| \|

\| \|---------------------------------4 Start LLP

\| \| \[HL START\]

\| \|

\| \|---------------------------------5 Stop LLP

\| \| \[HL STOP\]

\| \|

\| \|---------------------------------6 Systems

\| \| Link

\| \| Monitor

\| \| \[HL

\| \| MESSAGE

\| \| MONITOR\]

\| \|

# Menu Diagram, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\| \|-------------7 Logical ----------1 Show

\| \| Link Queue Communications

\| \| Management Error

\| \| \[HL QUEUE \[HL SHOW

\| \| MANAGEMENT\] COMMUNICATIONS

\| \| \| ERROR\]

\| \| \|

\| \| \|-------------2 Clear

\| \| \| Communications

\| \| \| Error

\| \| \| \[HL CLEAR

\| \| \| COMMUNICATIONS

\| \| \| ERROR\]

\| \| \|

\| \| \|-------------3 Create/Edit

\| \| \| a Queue

\| \| \| Test Entry

\| \| \| \[HL CRE/ED

\| \| \| QUEUE TEST

\| \| \| ENTRY\]

\| \| \|

\| \| \|-------------4 Copy a

\| \| \| Queue

\| \| \| Entry \[HL

\| \| \| COPY QUEUE

\| \| \| ENTRY\]

\| \| \|

\| \| \|-------------5 Clear a

\| \| Queue of

\| \| all

\| \| Entries

\| \| \[HL CLEAR

\| \| QUEUE\]

\| \|

\| \|

\| \|---------------------------------8 Report \[HL

\| CUSTOM

\| REPORT\]

\|

\|

\|-----------------------------------------------------2 Interface

\| Workbench

\| \[HL

\| INTERFACE

\| WORKBENCH\]

\|

\|-----------------------------------------------------3 Message

Requeuer

\[HL

MESSAGE

REQUEUER\]

# Menu Diagram, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

----------------------------------------------------------------3 Activate/

Inactivate

Application

\[HL EDIT

APPL PARAM\]

----4 Print/Display---------------------------------------------1 Application

Menu \[HL Parameters

PRINT MENU\] Print/Display

MENU\] \[HL PRINT

\| APPL PARAM\]

\|

\|-----------------------------------------------------2 Non-DHCP

\| Application

\| Parameters

\| Print/Display

\| \[HL PRINT

\| SITE PARAM\]

\|

\|-----------------------------------------------------3 Awaiting/

\| Pending HL7

\| Transmissions

\| Print/Display

\| \[HL PRINT

\| PENDING TRANS\]

\|

\|-----------------------------------------------------4 Failed HL7

\| Transmissions

\| Print/Display

\| \[HL PRINT

\| FAILED TRANS\]

\|

\|-----------------------------------------------------5 Version

\| Print/Display

\| \[HL PRINT

\| VERSION\]

\|

\|-----------------------------------------------------6 Message

\| Type

\| Print/Display

\| \[HL PRINT

\| MSG TYPE\]

\|

\|-----------------------------------------------------7 Segment

\| Name

\| Print/Display

\| \[HL PRINT

\| SEGMENT\]

\|

\|-----------------------------------------------------8 Data Type

\| Print/Display

\| \[HL PRINT

\| DATA TYPE\]

\|

# Menu Diagram, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\|-----------------------------------------------------9 Fields

Print/Display

\[HL PRINT

FIELDS\]

----------------------------------------------------------------5 Purge

Message

Text File

Entries

\[HL PURGE

TRANSMISSIONS\]

Archiving and Purging

# Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no archiving in the HL7 software package.

# Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For purging, use the Purge HL7 MESSAGE TEXT File Entries \[HL PURGE TRANSMISSIONS\] option in the HL7 Main Menu (HL MAIN MENU), which purges entries from the HL7 MESSAGE TEXT file (#772). The purge will only delete entries that are at least seven days old.

The HL7 MESSAGE TEXT file (#772) contains a record of all outgoing HL7 transmissions and their statuses. The purge \[HL PURGE TRANSMISSIONS\] option purges all entries in the file that have been successfully transmitted and, optionally, those entries with a status of error in transmission.

To purge entries with an error status, run the \[HL PURGE TRANSMISSIONS\] option directly from the menu, and answer Yes at the "Purge entries that were not successfully transmitted?" prompt. *Entries with an error status should be reviewed before purging.It is recommended that this option be queued to run once a day as a background task in order to automatically purge entries that were successfully transmitted.*Example

Enter cutoff date for purge of HL7 MESSAGE TEXT file: T-13 (JAN 31, 1995)

Purge entries that were not successfully transmitted? NO// ??

Enter 'Yes' to purge entries whose status is 'error in transmission'. If you have reviewed/resolved the cause of the problem of those entries with an 'error' status answer 'Yes'. Otherwise answer 'No'.

Purge entries that were not successfully transmitted? NO// Y YES

Purge queued to run in background.

External Relations

# Minimum Versions Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum package versions are required in order to install this version of DHCP HL7:

- Kernel V. 7.1
- VA FileMan V. 21.0
- VA FileMan V. 7.1
- OE/RR V. 2.5

# Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DHCP HL7 V. 1.6 is the custodial package for the following integration agreements. To obtain more detailed information about these agreements, use the Integration Agreements Menu options in the DBA Menu on FORUM.

940 NAME: DBIA940

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE: INCOME VERIFICATION Albany

USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

FILE: 772 ROOT: HL(772,

DESCRIPTION: TYPE: File

941 NAME: DBIA941

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE: INCOME VERIFICATION Albany

USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

FILE: 771.3 ROOT: HL(771.3,

DESCRIPTION: TYPE: File

942 NAME: DBIA942

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE: INCOME VERIFICATION Albany

USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

FILE: ROOT:

DESCRIPTION: TYPE: Other

# Database Integration Agreements (DBIAs), cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1169 NAME: DBIA1169-A

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE: MINIMAL PATIENT DA Albany

USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

FILE: 771.5 ROOT: HL(771.5,

DESCRIPTION: TYPE: File

1170 NAME: DBIA1169-B

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE: MINIMAL PATIENT DA Albany

USAGE: Private APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

FILE: 771.2 ROOT: HL(771.2,

DESCRIPTION: TYPE: File

10106 NAME: HLFNC

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE:

USAGE: Supported APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: VERSION:

FILE: ROOT:

10107 NAME: HLFNC1

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE:

USAGE: Supported APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: VERSION:

FILE: ROOT:

DESCRIPTION: TYPE: Routine

10108 NAME: HLTF

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE:

USAGE: Supported APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: VERSION:

FILE: ROOT:

DESCRIPTION: TYPE: Routine

# Database Integration Agreements (DBIAs), cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

10109 NAME: HLTRANS

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE:

USAGE: Supported APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: VERSION:

FILE: ROOT:

DESCRIPTION: TYPE: Routine

10110 NAME: HL7 NON-DHCP APPLICATION PARAMETER

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE:

USAGE: Supported APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: VERSION:

FILE: 770 ROOT: HL(770,'B',

DESCRIPTION: TYPE: File

10136 NAME: HL7 DHCP APPLICATION PARAMETER

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE:

USAGE: Supported APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION:

VERSION:

FILE: 771 ROOT: HL(771,

DESCRIPTION: TYPE: File

10137 NAME: HL7 SEGMENT NAME FILE

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE:

USAGE: Supported APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: VERSION:

FILE: 771.3 ROOT: HL(771.3,

DESCRIPTION: TYPE: File

10138 NAME: HL7 TRANSMISSION FILE

CUSTODIAL PACKAGE: HEALTH LEVEL SEVEN Albany

SUBSCRIBING PACKAGE:

USAGE: Supported APPROVED: APPROVED

STATUS: Active EXPIRES:

DURATION: VERSION:

FILE: 772 ROOT: HL(772,

DESCRIPTION: TYPE: File

Internal Relations

All options of the HL7 Main Menu function independently provided the user has the appropriate VA FileMan access.

# SACC Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1 DATE GRANTED: DEC 7,1994

Permanent exemption to use the following 1994 M standard language

features:

Set \$Extract

Merge

Two Argument \$Order (reverse \$o)

Variables

# Package-wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables associated with the DHCP HL7 software package.

# Basic Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table provides a list of the basic variables, with their descriptions, that are used by the DHCP HL7 package for the V. 1.6 interface method. The variables are grouped into the following three categories:

- Variables created when an HL7 message is *received*
- Variables created when an HL7 message is being *sent*
- Variables created when HL7 messages are both *sent and received*

|               |                                                                                                                                                                                                                                                                                                                                             |                   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Variable Name | Description                                                                                                                                                                                                                                                                                                                                 | When Created      |
| EID           | The IEN of the event driver protocol in the Protocol file (#101) for the application that is sending this message.                                                                                                                                                                                                                          | Sent              |
| HL            | The array in which the output parameters will be returned. *This parameter must be passed by reference.*                                                                                                                                                                                                                                    | Sent and Received |
| HL("ACAT")    | The accept acknowledgment type from the Protocol file (#101). (Optional)                                                                                                                                                                                                                                                                    | Sent              |
| HL("APAT")    | The application acknowledgment condition of the sending application from the Protocol file (#101). It is in the message header of the message received. This variable will be used by the receiving application to determine the type of acknowledgment, if any, that must be returned to the application that sent the message. (Optional) | Sent and Received |
| HL("CC")      | The country code of the sending application from the HL7 APPLICATION PARAMETER file (#771). It is in the message header of the message received. (Optional)                                                                                                                                                                                 | Sent and Received |
| HL("DTM")     | The date/time from the message header of the message received in HL7 format. (Optional)                                                                                                                                                                                                                                                     | Received          |

Basic Variables, cont.

|                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                   |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Variable Name | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | When Created  |
| HL("DUZ")         | If a valid DHCP access code is contained in the first component of the Security field (#8) of the MSH segment, HLDUZ will equal the DUZ associated with this access code from the New Person file (#200) on DHCP. (Optional)                                                                                                                                                                                                                                                                                                                                    | Received          |
| HL("ECH")         | The HL7 encoding characters (1 to 4 characters) to be used in extracting data from HL7 segments and fields. Each character must be unique and cannot match the HL7 field separator character. (See the variable HLFS for a definition of the field separator character.) The four encoding characters are the component separator, repetition separator, escape character, and sub-component separator, in that order. The default characters used by the DHCP HL7 package (when an application package does not define its own encoding characters) are ~\|\\. | Sent and Received |
| HL("EID")         | The IEN of the event driver protocol from the Protocol file (#101) that generated the message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Received          |
| HL("EIDS")        | The IEN of the subscriber protocol from the Protocol file (#101) that is receiving the message.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Received          |
| HL("ESIG")        | This variable might not always exist. If a valid DHCP electronic signature code is contained in the third component of the Security field (#8) of the MSH segment, HLESIG will equal the signature block printed name associated with this electronic signature code from the New Person file (#200) on DHCP.                                                                                                                                                                                                                                                   | Received          |
| HL("ETN")         | The 3 character event type name from the Protocol file (#101) (e.g., A01 \[Admit a Patient\], O01 \[Order Message\], etc.).                                                                                                                                                                                                                                                                                                                                                                                                                                     | Sent and Received |
| HL("FS")          | The HL7 field separator character to be used in extracting fields of data from HL7 messages received, or building HL7 segments in messages sent. The field separator is only one character (e.g., ^).                                                                                                                                                                                                                                                                                                                                                           | Sent and Received |
| HL("MID")         | The HL7 message control ID for the message received. A number that uniquely identifies the message.                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Received          |
| HL("MTN")         | The three character message type name from the Protocol file (#101) (e.g., ADT, QRY \[Query\], ORU \[Observation Result Unsolicited\], etc.).                                                                                                                                                                                                                                                                                                                                                                                                                   | Sent and Received |

Basic Variables, cont.

|                   |                                                                                                                                                                                                                                                                                                                                                                  |                   |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Variable Name | Description                                                                                                                                                                                                                                                                                                                                                  | When Created  |
| HL("PID")         | The HL7 processing ID for the message received. (Normally, P for production, T for Training, D for Debug.)                                                                                                                                                                                                                                                       | Sent and Received |
| HL("Q")           | Two quotation marks (""). This variable can be used to insert a null value in an HL7 field when building HL7 segments.                                                                                                                                                                                                                                           | Sent and Received |
| HL("RAN")         | The name of the receiving application from the HL7 APPLICATION PARAMETER file (#771) (e.g., Radiology).                                                                                                                                                                                                                                                          | Received          |
| HL("SAF")         | The name of the sending facility from the HL7 APPLICATION PARAMETER file (#771).                                                                                                                                                                                                                                                                                 | Sent              |
| HL("SAN")         | The name of the sending application (e.g., Radiology) from the HL7 APPLICATION PARAMETER file (#771) for the message received.                                                                                                                                                                                                                                   | Sent and Received |
| HL("VER")         | The version number of the HL7 protocol that was used to build the message being sent/received.                                                                                                                                                                                                                                                                   | Sent and Received |
| HLA("HLA",I)      | A local array consisting of HL7 segments that form an HL7 message where the variable I is a sequential, whole number starting with the number 1. This array is built by the DHCP application in order to send an HL7 message that is small enough to be built in the local partition space. Otherwise, the ^TMP("HLA") global array should be set.               | Received          |
| HLA("HLS",I)      | A local array consisting of HL7 segments that form an HL7 message where the variable I is a sequential, whole number starting with the number 1. This array is built by the DHCP application in order to send an HL7 message that is small enough to be built in the local partition space. Otherwise, the ^TMP("HLS") global array defined below should be set. | Sent              |
| HLARYTYP          | This parameter specifies where the acknowledgment array is stored and whether it is a single message or batch acknowledgment. It must equal LM for Local/Single Message, LB for Local/Batch Message, GM for Global/Single Message or GB for Global/Batch Message.                                                                                                | Sent and Received |
| HLDT              | The parameter in which the message date/time in internal VA FileMan format will be returned. *This parameter must be passed by reference.*                                                                                                                                                                                                                       | Sent and Received |
| HLDT1             | The parameter in which the message date/time in HL7 format will be returned. *This parameter must be passed by reference.*                                                                                                                                                                                                                                       | Sent and Received |

BasicVariables, cont.

|                   |                                                                                                                                                                               |                   |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Variable Name | Description                                                                                                                                                               | When Created  |
| HLEID             | The IEN of the event driver protocol in the Protocol file (#101). It is passed to the processing routine in the variable HL("EID").                                           | Sent and Received |
| HLEIDS            | The IEN of the subscriber protocol in the Protocol file (#101). It is passed to the processing routine in the variable HL("EIDS").                                            | Received          |
| HLFORMAT          | This parameter specifies whether the HLA array is pre-formatted in HL7 format. At this time, it should always equal 1.                                                        | Sent and Received |
| HLMID             | The parameter in which the message ID will be returned. *This parameter must be passed by reference.*                                                                         | Sent and Received |
| HLMTIEN           | The parameter in which the IEN of the entry in the Message Text file (#772) created by the call to the entry point CREATE^HLTF.                                               | Sent              |
| HLMTIENA          | The IEN of the entry in the Message Text file (#772) created by the call to the entry point CREATE^HLTF and returned in the MTIEN parameter.                                  | Received          |
| HLMTIENS          | The IEN of the entry in the Message Text file (#772) for the subscriber application.                                                                                          | Received          |
| HLNEXT            | M code that is executed by the application to \$O through the nodes of the Message Text global.                                                                               | Received          |
| HLNODE            | A node from the Message Text global.                                                                                                                                          | Received          |
| HLP("CONTPTR")    | The value that should go in the continuation pointer field of the Message Header segment for the message being sent.                                                          | Sent              |
| HLP("ERRTEXT")    | If an error occurred during the processing of the incoming message, an error message (1 to 80 characters) should be passed in this parameter. (Optional)                      | Received          |
| HLP("PRIORITY")   | The default priority is delayed. Set this parameter equal to I for Immediate if this message should be delivered in the foreground (immediate).                               | Sent and Received |
| HLP("SECURITY")   | Security information (1 - 40 characters) that the DHCP application wants included in the Security field (#8) of the HL7 MSH or BHS segment when sending a message. (Optional) | Sent and Received |
| HLQUIT            | A variable that indicates when there are no more nodes to process. If HLQUIT is not greater than zero, all message text has been processed.                                   | Received          |

BasicVariables, cont.

<table style="width:100%;">
<colgroup>
<col style="width: 31%" />
<col style="width: 49%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Variable Name</strong></td>
<td><strong>Description</strong></td>
<td><strong>When Created</strong></td>
</tr>
<tr class="even">
<td>HLRESLT</td>
<td>The message ID assigned to this message and/or an error message will be returned in this parameter. This parameter must be passed by reference. If the call to GENERATE^HLMA is successful, this parameter will be returned equal to the message ID assigned to the message that was created. If the call was not successful, this parameter will be returned with the following three pieces of data: message ID (or 0 if no message ID was assigned)^error code^error message.</td>
<td>Sent</td>
</tr>
<tr class="odd">
<td>HLRESLTA</td>
<td>The message ID assigned to this message and/or an error will be returned in this parameter. This parameter must be passed by reference. If the call to GENACK is successful, this parameter will be returned equal to the message ID assigned to the message that was created. If the call was not successful, this parameter will be returned with the following three pieces of data: message ID (or 0 if no message ID was assigned)^error code^error message.</td>
<td>Received</td>
</tr>
<tr class="even">
<td>INT</td>
<td>Indicates that only array values for an internal DHCP-to-DHCP message exchange should be utilized.</td>
<td>Sent</td>
</tr>
<tr class="odd">
<td>MID</td>
<td>The parameter in which the message ID will be returned.</td>
<td><p>Sent and</p>
<p>Received</p></td>
</tr>
<tr class="even">
<td>MTIEN</td>
<td>The parameter in which the IEN of the entry in the Message Text file (#772) (created by the call to the entry point CREATE^HLTF) will be returned. <em>This parameter must be passed by reference.</em></td>
<td>Sent and Received</td>
</tr>
<tr class="odd">
<td>MTIENA</td>
<td>The IEN of the entry in the Message Text file (#772) created by the call to the entry point CREATE^HLTF and returned in the MTIEN parameter.</td>
<td>Received</td>
</tr>
<tr class="even">
<td>PRIORITY</td>
<td>The default priority is delayed. Set this parameter equal to I for Immediate if this message should be delivered in the foreground (immediately). (Optional)</td>
<td>Sent and Received</td>
</tr>
</tbody>
</table>

BasicVariables, cont.

|                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                   |
|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| Variable Name | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | When Created  |
| RESULT            | The message ID assigned to this message and/or an error message will be returned in this parameter. T*his parameter must be passed by reference.* If the call to MSH^HLFNC2 is successful, this parameter will be returned equal to the message ID assigned to the message that was created. If the call was not successful, this parameter will be returned with the following three pieces of data: message ID (or 0 if no message ID was assigned)^error code^error message. | Sent and Received |
| SECURITY          | Security information (1 to 40 characters) that the DHCP application wants included in the Security field (#8) of the HL7 MSH or BHS segment when sending a message. (Optional)                                                                                                                                                                                                                                                                                                  | Sent and Received |
| ^TMP("HLA",\$J,I) | A global array containing all segments of the HL7 message that the receiving DHCP application wishes to send as a response. The variable I is a sequential, whole number starting with the number 1.                                                                                                                                                                                                                                                                            | Received          |
| ^TMP("HLS",\$J,I) | A global array containing all segments of the HL7 message that the receiving DHCP application wishes to send as a response. The variable I is a sequential, whole number starting with the number 1.                                                                                                                                                                                                                                                                            | Sent              |

# # # # Arrays

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table contains a list of arrays, with their descriptions, which are used by the DHCP HL7 V. 1.6 interface method.

|                         |                                                                                                                                                                                                                                                                     |                  |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
| Array Name          | Description                                                                                                                                                                                                                                                     | When Created |
| ^HL(772,HLDA,"IN",I,0)  | A global array containing all segments of the HL7 message received. This is the data that the receiving DHCP application must process. HLDA is the variable as defined earlier in this section. The variable I is a sequential number starting with the number one. | Received         |
| ^TMP("HLS",\$J,HLSDT,I) | A global array containing all segments of the HL7 message that the receiving DHCP application wishes to send. The HLSDT variable is as defined above. The variable I is a sequential number starting with the number one.                                           | Sent             |

How to Generate Online Documentation

This section describes some of the various methods by which users can secure HL7 technical documentation. Online technical documentation pertaining to the HL7 software, in addition to that which is located in the help prompts and on the help screens which are found throughout the HL7 package, can be generated through the use of several Kernel options. These include, but are not limited to, the following:

- %Index
- Menu Management
- Inquire option
- Print Option File
- VA FileMan
- Data Dictionary Utilities
- List File Attributes

Entering question marks at the "Select ... Option:" prompt can also provide users with valuable technical information. For example, a single question mark (?) lists all options which can be accessed from the current option. Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock for each. Three question marks (???) displays a brief description for each option in a menu while an option name preceded by a question mark (?OPTION) shows extended help, if available, for that option.

For a more exhaustive option listing, and further information about other utilities which supply online technical information, please consult the DHCP Kernel Reference Manual.

# %Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to DHCP Programming Standards. The %Index output might include the following components:

- Compiled list of errors and warnings
- Routine listing
- Local variables
- Global variables
- Naked globals
- Label references
- External references

# %Index, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By running %Index for a specified set of routines, you are afforded the opportunity to discover any deviations from DHCP Programming Standards which exist in the selected routine(s), and to see how routines interact with one another (i.e., which routines call or are called by other routines).

To run %Index for the HL7 package, specify the HL namespace at the "routine(s) ?\>" prompt.

*NOTE: HL7 initialization routines which reside in the UCI in which %Index is being run, compiled template routines, and local routines found within the HL namespace should be omitted at the "routine(s) ?\>" prompt. To omit routines from selection, preface the namespace with a minus sign (-).*

# Inquire Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Menu Management option provides the following information about a specified option:

- Option name
- Menu text
- Option description
- Type of option
- Lock (if any)

In addition, all items on the menu are listed for each menu option. To secure information about HL7 options, you must specify the HL namespace.

# Print Option File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This utility generates a listing of options from the OPTION file (#19). You can choose to print all of the entries in this file, or you can elect to specify a single option or range of options. For a list of HL7 options, please refer to the Exported Options section of this manual.

# List File Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This VA FileMan option allows you to generate documentation pertaining to files and file structure. Using the "Standard" format of this option yields the following data dictionary information for a specified file(s):

- File name and description
- Identifiers
- Cross-references
- Files pointed to by the file specified
- Files which point to the file specified
- Input, print, and sort templates

In addition, the following applicable data is supplied for each field in the file:

- Field name, number, title, and description
- Global location
- Help prompt
- Cross-reference(s)
- Input transform
- Date last edited
- Notes

Using the "Global Map" format of this option generates an output which lists the following information:

- All cross-references for the file selected
- Global location of each field in the file
- Input, print, and sort templates.

For a comprehensive listing of HL7 files, please refer to the Files section of this manual.

Glossary

ACK HL7 acknowledgment. This is a message trans-

> mitted back to the VAMC upon receipt of data at the EDR repository.

DHCP Application A software package developed by the VA to support

clinical or administrative functions at VA medical

centers nationwide. It is written in M and, via

Kernel, will run on all major M implementations,

regardless of vendor.

HL7 Component A field can contain multiple components separated by

> the HL7 component separator.

HL7 Field A field is a specific unit of data. Each field is defined

> by the following set of characteristics:

- Position in the Segment
- Name
- ID Number
- Maximum Length
- Optionality
- Repetition
- Table Assignment (optional)
- Type

HL7 Hybrid Lower Layer A communication protocol that supports Layers 1

Protocol through 4 of the OSI protocol.

HL7 Interface The exchange of information between a DHCP

application and the DHCP HL7 package.

HL7 Message A message is the atomic unit for transferring data

> between systems. It is comprised of a group of HL7 segments in a defined sequence. Each message has a message type that defines its purpose. Each message is identified by a unique 3 character code.

HL7 Protocol Health Level Seven. An application communications

> standard for text-type patient-specific data. Permits data exchange between diverse computer configurations with a variety of communications protocols. Communications take place by exchange of HL7 messages.

HL7 Segment A segment is a logical grouping of one or more data

> fields separated by the HL7 field separator. Segments of a message might be optional or required. They might occur only once or might repeat multiple times. Each segment is identified by a unique 3 character code.

Lower Level Interface Refers to Layers 1 through 4 of the Open Systems

> Interconnect (OSI) protocol for exchanging data between computer systems. Layers 1 through 4 ensure physical connectivity and error-free delivery of data between computer systems and are normally handled by a communication protocol independent of the HL7 protocol. In the DHCP HL7 package, the lower level interface is handled by either the DHCP MailMan package or the HL7 Hybrid Lower Layer Protocol.

Non-DHCP Application A term used to refer to and distinguish between the

two applications (the other is called the DHCP

application) that will be exchanging data using the

HL7 protocol.

Appendix A. Sample HL7 Interface Specification

HEALTH LEVEL 7

INTERFACE SPECIFICATIONS

ALBANY INFORMATION SYSTEMS CENTER

DECENTRALIZED HOSPITAL COMPUTER PROGRAM

EXCHANGE OF RADIOLOGY HEALTHCARE INFORMATION

MARCH 1993

1\. PURPOSE

This document specifies an interface to the DHCP Radiology package based upon the HL7 protocol. It is intended that this interface form the basis for the exchange of healthcare information between the DHCP Radiology package and all non-DHCP systems, especially those non-DHCP systems that generate radiology results information.

2\. OVERVIEW

> 2.1 Statement of Intent

> The Albany IRM Field Office (IRMFO) is developing and plans to implement a generic interface to the HL7 protocol for use by the DHCP Radiology package in communicating with non-DHCP systems for the purpose of exchanging healthcare information. This interface might eventually be used by all DHCP clinical packages to exchange healthcare information with non-DHCP systems. The interface will strictly adhere to the HL7 protocol and will avoid using "Z" type extensions to the protocol wherever possible.

> 2.2 Scope

> This document describes messages that are exchanged between the DHCP Radiology package and a non-DHCP system for the purpose of exchanging information concerning radiology results, specifically reports and impressions.

> 3\. GENERAL SPECIFICATIONS

> 3.1 Communication Protocol

> The HL7 protocol defines only the seventh level of the Open System Inter-

> connect (OSI) protocol. This is the application level. Levels one through six involve primarily communication protocols. The HL7 protocol provides some guidance in this area. The communication protocols that will be used for interfacing with the DHCP Radiology package will be based on the HL7 Hybrid Lower Level Protocol which is described in the HL7 Interface Standards document.

> 3.2 Application Processing Rules

> The HL7 protocol itself describes the basic rules for application processing by the sending and receiving systems. Information contained in the protocol will not be repeated here, therefore anyone wishing to interface with the DHCP Radiology package should become familiar with the HL7 protocol version 2.1.

> 3.3 Messages

> The following HL7 messages will be used to support the exchange of Radiology data:

> ACK General Acknowledgment

> ORF Observational Report Response

> ORM Order

> ORR Order Response Message

> ORU Observational Results Unsolicited

> QRY Query Message

> 3.4 Segments

> The following HL7 segments will be used to support the exchange of Radiology data:

> MSA Message Acknowledgment

> MSH Message Header

> OBR Observational Request

> OBX Result

> ORC Common Order

> PID Patient Identification

> QRD Query Definition

> 3.5 Fields

> The following HL7 fields will be used to support the exchange of Radiology data for each of the segments listed in paragraph 3.4:

> FIELD FIELD

> SEGMENT SEQUENCE NUMBER ELEMENT NAME

> -----------------------------------------------------------------------------------------------------------------------------------

> MSA 1 Acknowledgment Code

> 2 Message Control ID

> 3 Text Message

> MSH 1 Field Separator

> 2 Encoding Characters

> 3 Sending Application

> 4 Sending Facility

> 5 Receiving Application

> 6 Receiving Facility

> 7 Date/Time of Message

> 8 Security

> 9 Message Type

> 10 Message Control ID

> 11 Processing ID

> 12 Version ID

> OBR 4 Universal Service Ident.

> 7 Observation Date/Time

> 8 Observation End Date/Time

> 9 Collection Volume

> 14 Specimen Received Date/Time

> 16 Ordering Provider

> 18 Placers Field \#1 (Ward/Clinic)

> 20 Fillers Field \#1 (Ward/Clinic)

> 22 Results Rpt/Status Chng-Date/Time

> OBX 2 Value Type

> 3 Observation Identifier

> 5 Observation Results

> ORC 1 Order Control

> 9 Date/Time of Transaction

> 14 Call Back Phone Number

> PID 3 Patient ID (Internal ID)

> 5 Patient Name

> 7 Date of Birth

> 8 Sex

> 19 SSN Number - Patient  
> 3.5 Fields

> FIELD FIELD

> SEGMENT SEQUENCE NUMBER ELEMENT NAME

> -----------------------------------------------------------------------------------------------------------------------------------

> QRD 1 Query Date/Time

> 2 Query Format Code

> 3 Query Priority

> 4 Query ID

> 7 Quantity Limited Request

> 8 Who Subject Filter

> 9 What Subject Filter

> 10 What Department Data Code

4\. TRANSACTION SPECIFICATIONS

> 4.1 General

> The flow of transactions between the DHCP Radiology package and the non-DHCP system can occur in one of two ways.

> A. DHCP will notify the non-DHCP system that an exam has been done and the non-DHCP system will notify the DHCP system of the results of the exam once the report has been entered.

> B. The non-DHCP system will query the DHCP system for an exam list for a patient or for a specific exam and the DHCP system will respond with the appropriate exam information. The non-DHCP system will then send the results of the exam(s) to the DHCP system once the report has been entered.

> 4.2 Specific Transactions

> A. Complete Exam Sent to Non-DHCP System

> When an exam is completed on the DHCP system, an Order (ORM) message is sent to the non-DHCP system. The ORM message would consist of the following segments:

> ORM ORDER MESSAGE

> -----------------------------------------

> MSH Message Header

> PID Patient Identification

> ORC Common Order

> OBR Observational Request

> OBX Result  
> 4.2 Specific Transactions

> EXAMPLE:

> ----------------

> MSH^~\|\\^RADIOLOGY^608^RADIOLOGY^NON-DHCP^199104301000^^ORM^12345^P^2.1

> PID^^^55555~5~M11^^HL7Patient~One~X^^19300101^M^^^^^^^^^^^123456789

> ORC^NW^^^^^^^^199104301000

> OBR^^^^7089898.8453-1~040391-66~L^^^199104301200^""^""^^^^^""^^3232~

> HL7Doctor~One^^MEDICINE^^^^199104301000

> OBX^^CE^P~PROCEDURE~L^^100~CHEST PA & LAT~L

> OBX^^TX^M~MODIFIERS~L^^RIGHT, PORTABLE

> OBX^^TX^H~HISTORY~L^^None

> OBX^^TX^A~ALLERGIES~L^^BEE STINGS

> The non-DHCP system then sends a General Acknowledgment (ACK) message back to the DHCP system.

> EXAMPLE:

> ----------------

> MSH^~\|\\^RADIOLOGY^NON-DHCP^RADIOLOGY^608^199104301001^^ORR^54322^P^2.1

> MSA^AA^12345

> B. Results of Exam sent to DHCP System

> When the exam results corresponding to the order that was sent by the ORM message in paragraph A are ready, an Observational Results Unsolicited (ORU) message is sent to the DHCP system. The ORU would consist of the following segments:

> ORU OBSERVATIONAL RESULTS UNSOLICITED

> -------------------------------------------------------------------------------

> MSH Message Header

> PID Patient Identification

> OBR Observational Request

> OBX Result

> EXAMPLE:

> ----------------

> MSH^~\|\\^RADIOLOGY^NON-DHCP^RADIOLOGY^608^199104301010^ACCESS CODE\~~

> SIGNATURE CODE^ORU^12346^P^2.1

> PID^^^55555~5~M11^^HL7Patient~One~X^^19300101^M^^^^^^^^^^^123456789

> OBR^^^^7089898.8543-1~043091-66~L^^^199104301200^""^""^^^^^""^^3232~

> HL7Doctor~One^^^^MEDICINE^^199104301010

> OBX^^TX^I~IMPRESSION~L^^HEART NORMAL SIZE

> OBX^^ST^D~DIAGNOSTIC CODE~L^^NORMAL

> OBX^^TX^R~REPORT~L^^Heart appears to be of normal size.

> OBX^^TX^R~REPORT~L^^No infiltrate or abnormal mass noted.

> 4.2 Specific Transactions

> The DHCP system would then send back a General Acknowledgment (ACK) message.

> EXAMPLE:

> ----------------

> MSH^~\|\\^RADIOLOGY^608^RADIOLOGY^NON-DHCP^199104301011^^ACK^54320^P^2.1

> MSA^AA^12346

> C. Query for a List of Exams for a Patient

> An alternate method for a non-DHCP system to determine which exams have been completed for a patient is to send a Query Message (QRY) to the DHCP system. The QRY would consist of the following segments:

> QRY QUERY MESSAGE

> -----------------------------------------

> MSH^~\|\\^RADIOLOGY^NON-DHCP SITE^RADIOLOGY^608^199104301100^ACCESS

> CODE\~~SIGNATURE CODE^QRY^12347^P^2.1

> QRD^199104301100^R^I^Q1^^^5~RD^55555^OTH^PATIENT

> The DHCP system would respond to the query with a list of up to five exams for patient 55555 in record-oriented format. In the following example, only one complete exam existed for the patient.

> EXAMPLE:

> ----------------

> MSH^~\|\\^RADIOLOGY^608^RADIOLOGY^NON-DHCP^199104301101^^ORF^54321^P^2.1

> MSA^AA^12347

> QRD^199104301101^R^I^Q1^^^1~RD^55555^OTH^PATIENT

> PID^^^55555~5~M11^^HL7Patient~One~X^^19300101^M^^^^^^^^^^^123456789

> OBR^^^^7089898.8453-1~043091-66~L^^^199104301200^""^""^^^^^""^^3232~

> HL7Doctor~One^^^^MEDICINE^^199104301200

> OBX^^CE^P~PROCEDURE~L^^110~CHEST 1 VIEW~L

> OBX^^TX^M~MODIFIERS~L^^RIGHT, PORTABLE

> OBX^^TX^H~HISTORY~L^^A history is not available for this patient.

> OBX^^TX^A~ALLERGIES~L^^BEE STINGS

> This query can be used to request a list of exams or just the most recent exam. To request the most recent exam, Field \#7 of the QRD segment would specify one record as the quantity (1~RD) in Field \#7. To receive a list of exams, more than one record would be specified as in the example above. For either of these queries, the full SSN of the patient or the first letter of the last name and the last four digits of the SSN can be passed as the Who Subject Filter. Likewise, this query can be used to request a specific exam. To do so, Field \#7 would specify one record (1~RD), Field \#8 would specify the exam number (e.g., 042891-666) or case number (e.g., 666), and Field \#10 would specify the word EXAM.

Appendix B. Supported HL7 Message Types

ABBREVIATED NAME: ACK FULL NAME: General Acknowledgment

ABBREVIATED NAME: ADT FULL NAME: ADT Message

ABBREVIATED NAME: ARD FULL NAME: Ancillary Report (Display)

ABBREVIATED NAME: BAR FULL NAME: Add/Change Billing Account

ABBREVIATED NAME: DFT FULL NAME: Detail Financial Transaction

ABBREVIATED NAME: DSR FULL NAME: Display Response

ABBREVIATED NAME: MCF FULL NAME: Delayed Acknowledgment

ABBREVIATED NAME: OCF FULL NAME: Order Confirmation

ABBREVIATED NAME: ORF FULL NAME: Observational Result/Record Response

ABBREVIATED NAME: ORM FULL NAME: Order

ABBREVIATED NAME: ORR FULL NAME: Order Response Message

ABBREVIATED NAME: ORU FULL NAME: Observational Results Unsolicited

ABBREVIATED NAME: OSQ FULL NAME: Order Status Query

ABBREVIATED NAME: QRY FULL NAME: Query

ABBREVIATED NAME: UDM FULL NAME: Unsolicited Display

Index

Appendix A. Sample HL7 Interface Specification 61

Appendix B. Supported HL7 Message Types 67

Archiving 41

Archiving and Purging 41

Arrays 54

Basic Variables 49

Callable Routines 15

Cross-reference Descriptions 24

Database Integration Agreements (DBIAs) 43

Exported Options 35

External Relations 43

File List with Descriptions 19

File Flow Chart 22

Files 19

Global Growth 24

Globals 24

Glossary 59

How to Generate Online Documentation 55

Implementation 9

Implementation and Maintenance 9

Inquire Option 56

Internal Relations 47

Introduction 1

List File Attributes 57

Lower Level Protocols 3

Maintenance 9

Menu Diagram 35

Minimum Versions Required 7, 43

Organization of this Manual 6

Overview 1

Package-wide Variables 49

Print Option File 56

Purging 41

Related Manuals 5

Resource Consumption 7

Resource Requirements 7

Routine List with Descriptions 11

Routines 11

SACC Exemptions 47

The DHCP HL7 Package 2

The DHCP Interface to the HL7 Protocol 4

Troubleshooting Tip 9