---
title: HL7 V. 1.6 Release Notes
doc_type: RN
doc_label: Release Notes
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
menu_options: 0
description: - [Fields Added to the Top Level of the Protocol file (#101) 8](#fields-added-to-the-top-level-of-the-protocol-file-101-8) - [V. 1.6 Related Manuals](#v-16-related-manuals) - [V. 1.5 Related Manuals](#v-15-related-manuals) - [New Modules](#new-modules) - [New Modules, cont.](#new-modules-cont) - [Ne
audience: 
keywords: 
  - hlini
  - table
  - message
  - contents
  - dhcp
  - options
  - cont
  - protocol
  - files
  - incoming
page_count: 0
word_count: 2455
section_count: 1
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=8"
---

Decentralized Hospital Computer Program

DHCpHealth Level Seven(HL7)RELEASE NOTES

October 1995

IRM Field Office

Albany NY

Table of Contents

Overview 1

> V. 1.6 Related Manuals 1

> V. 1.5 Related Manuals 2

Routines 3

> New Modules 3

> New Routines 4

Data Dictionaries 5

> New Files 5

> Modified Files 7

# Fields Added to the Top Level of the Protocol file (#101) 8


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Fields Added to the Top Level of the Protocol file (#101) 8](#fields-added-to-the-top-level-of-the-protocol-file-101-8)
- [V. 1.6 Related Manuals](#v-16-related-manuals)
- [V. 1.5 Related Manuals](#v-15-related-manuals)
- [New Modules](#new-modules)
- [New Modules, cont.](#new-modules-cont)
- [New Routines](#new-routines)
- [New Files](#new-files)
- [New Files, cont.](#new-files-cont)
- [New Files, cont.](#new-files-cont-1)
- [Modified Files](#modified-files)
- [Modified Files, cont.](#modified-files-cont)
- [Fields Added to the Top Level of the Protocol file (#101)](#fields-added-to-the-top-level-of-the-protocol-file-101)
- [Fields Added to the Top Level of the Protocol file (#101), cont.](#fields-added-to-the-top-level-of-the-protocol-file-101-cont)
- [New Input Templates](#new-input-templates)
- [New Options](#new-options)
- [New Options, cont.](#new-options-cont)
- [New Options, cont.](#new-options-cont-1)
- [Menu Structure](#menu-structure)
> New Input Templates 10
Options 11
> New Options 11
> Menu Structure 13
Overview
With the release of V. 1.6, DHCP HL7 supports several methods for interfacing to the HL7 protocol. The method established by V. 1.5 is still supported (for backwards compatibility), and a new method is introduced, as well as new routines, file structures, templates, menus, and options. There are some significant differences between the V. 1.5 and V. 1.6 interface methods, as shown in the following table:
|                                                     |                                                                                                                                  |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| V. 1.5 Interface Method                         | V. 1.6 Interface Method                                                                                                      |
| One sender and one receiver per message.            | One sender, one or more receivers.                                                                                               |
| Sender and receiver must be on different systems.   | Sender and receiver can be on the same or different systems.                                                                     |
| Messages must go through a communications protocol. | Messages sent to applications on the same system do not have to go through a communications protocol.                            |
| All messages are processed in the background.       | Messages are processed in either the foreground or background, based on the priority assigned by sending/receiving applications. |
| No support for event points.                        | Event points are supported.                                                                                                      |

# V. 1.6 Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For applications using the V. 1.6 interface method, please refer to the following manuals:

- DHCP HL7 V. 1.6 Developer Manual
- DHCP HL7 V. 1.6 Installation Guide
- DHCP HL7 V. 1.6 Package Security Guide
- DHCP HL7 V. 1.6 Technical Manual
- DHCP HL7 V. 1.6 User Manual

# V. 1.5 Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For applications using the V. 1.5 interface method, you might also want to refer to the following manuals:

- DHCP HL7 V. 1.5 Developer Manual
- DHCP HL7 V. 1.5 Installation Guide
- DHCP HL7 V. 1.5 Package Security Guide
- DHCP HL7 V. 1.5 Release Notes
- DHCP HL7 V. 1.5 Technical Manual
- DHCP HL7 V. 1.5 User Manual

Routines

V. 1.5 routines have not been modified significantly in V. 1.6; however, all new routines introduced in V. 1.6 have been namespaced according to the module of the DHCP HL7 package to which they belong.

# New Modules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLCS

Communications Server

The Communications Server module receives all incoming messages and transmits all outgoing messages. It includes options for IRM staff to monitor incoming and outgoing messages and to start/stop lower level protocols.

HLDTIW

Interface Workbench

The Interface Workbench Module defines the application(s) that will send/receive HL7 messages. It uses List Manager screens which contain various tools and actions with which you create, edit, and delete applications and their associated logical links, server protocols, and subscriber (client) protocols.

HLFNC

Functions

Routines in this namespace provide callable subroutines or extrinsic functions that can be used by the DHCP HL7 package itself or by other DHCP applications.

HLMA

Message Administration

The Message Administration module is the single point of control for all messages. All messages must pass through the Message Administration module, where they are assigned a unique message ID in the HL7 Message Administration file (#773). The Message Administration module also creates one or more entries in the HL7 Message Text file (#772) for each message.

HLTP

Transaction Processor

The Transaction Processor module performs all actions relating to generating outgoing messages and processing incoming messages. It performs such functions as validating message headers, filing message text, invoking application processing routines, etc.

# New Modules, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLUTIL

Utilities

Routines in this namespace provide callable subroutines and extrinsic functions that are reserved for use by the DHCP HL7 package.

# New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLCS HLCS1 HLCSDL HLCSDL1 HLCSDL2 HLCSDR HLCSDR1 HLCSDR2

HLCSFMN HLCSFMN0 HLCSFMN1 HLCSHDR HLCSIN HLCSLNCH HLCSMM HLCSMM1

HLCSMON HLCSMON1 HLCSORA1 HLCSORA2 HLCSORAT HLCSOUT HLCSQUE HLCSQUE1

HLCSQUED HLCSRE1 HLCSREP HLCSREQ HLCSRES HLCSRQ HLCSRV HLCSTERM

HLCSUTL HLCSUTL1 HLCSUTL2 HLDTIW01 HLDTIW02 HLDTIW03 HLDTIW04 HLDTIW05

HLDTIW2A HLDTIW2B HLDTIW2C HLDTIWP0 HLDTIWP1 HLDTIWP2 HLDTIWP3 HLDTIWP4

HLDTIWP5 HLDTIWP6 HLDTIWU0 HLDTIWU1 HLDTIWU2 HLDTIWU3 HLDTIWU4 HLDTIWU5

HLFNC2 HLFNC3 HLINI00A HLINI00B HLINI00C HLINI00D HLINI00E HLINI00F

HLINI00G HLINI00H HLINI00I HLINI00J HLINI00K HLINI00L HLINI00M HLINI00N

HLINI00O HLINI00P HLINI00Q HLINI00R HLINI00S HLINI00T HLINI00U HLINI00V

HLINI00W HLINI00X HLINI00Y HLINI00Z HLINI01A HLINI01B HLINI01C HLINI01D

HLINI01E HLINI01F HLINI01G HLINI01H HLINI01I HLINI01J HLINI01K HLINI01L

HLINI01M HLINI01N HLINI01O HLINI01P HLINI01Q HLINI01R HLINI01S HLINI01T

HLINI01U HLINI01V HLINI01W HLINI01X HLINI01Y HLINI01Z HLINI027 HLINI028

HLINI029 HLINI02A HLINI02B HLINI02C HLINI02D HLINI02E HLINI02F HLINI02G

HLINI02H HLINI02I HLINI02J HLINI02K HLINI02L HLINI02M HLINI02N HLINI02O

HLINI02P HLINI02Q HLINI02R HLINI02S HLINI02T HLINI02U HLINI02V HLINI02W

HLINI02X HLINI02Y HLINI02Z HLINI030 HLINI031 HLINIS HLINIT5 HLLM

HLLM1 HLMA HLMA0 HLMA1 HLMA2 HLNTEG0 HLONI001 HLONI002

HLONI003 HLONI004 HLONI005 HLONI006 HLONI007 HLONI008 HLONI009 HLONI010

HLONI011 HLONIT HLONIT1 HLONIT2 HLONIT3 HLOPT1 HLPOST HLPOST16

HLPOSTQ HLPRE16 HLTF0 HLTF1 HLTP HLTP0 HLTP01 HLTP1

HLTP2 HLTPCK1 HLTPCK1A HLUOPT HLUOPT1 HLUTIL1 HLUTIL2 HLUTIL3

Data Dictionaries

All files in DHCP HL7 V. 1.6 support V. 2.2 of the HL7 protocol.

# New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

101

Protocol

A number of fields have been added to the Protocol file (#101) to support messaging protocols for event drivers and event subscribers. The following two values were added to the Type field (#4) of the Protocol file (#101):

- E for Event Driver
- S for Subscriber

771.6

HL7 Message Status

This file is a table of statuses that are assigned to entries in the HL7 Message Text file (#772).

771.7

HL7 Error Message

This file is a table of error codes and messages that are assigned to entries in the HL7 Message Text file (#772).

771.8

HL7 Standard

This file is a table of standard protocols supported by the DHCP HL7 package.

773

HL7 MESSAGE ADMINISTRATION

This file is used to create and maintain unique message IDs. It also contains the date/time when each ID was created.

# New Files, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*779.001

HL7 Event TYPE Code

This file is a table of HL7 event codes.

\*779.002

HL7 AcknowledgEment Code

This is a file of codes that are used by the system when processing acknowledgment messages to determine whether the message was successfully received and processed.

\*779.003

HL7 Accept/Application ACK Condition

This is a file of codes that are used by the system when processing acknowledgment messages to determine how to respond to a message.

\*779.004

Country Code

This is a table of codes used by the system when building message header segments.

869.1

HL LOWER LEVEL PROTOCOL TYPE

This file contains the valid Lower Layer Protocols (LLPs) available for use with the HL7 package.

869.2

HL LOWER LEVEL PROTOCOL PARAMETER

This file contains the LLP parameters used by the HL7 package. Each protocol uses a separate node to hold the parameters associated with the LLP used by the logical link. There should be an entry in this file for each logical link defined in File \#870. The currently defined nodes are:

- 100 - MailMan
- 200 - HLLP
- 300 - X3.28

\*Data tables to support each standard (#779.001 to \#779.999). Files \#779.005 through \#779.999 are reserved for distribution with future releases. *These files should not be modified locally, because each subsequent version will overwrite prior versions to support the HL7 Standard.*

# New Files, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

869.3

HL COMMUNICATION SERVER PARAMETERS

This file contains the parameters used by the HL7 Communications Server.

870

HL LOGICAL LINK

This file contains information about how to transmit information between applications that are on different computer systems. It also temporarily stores messages prior to their transmission.

# Modified Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

771

New name in V. 1.6: HL7 Application Parameter

(Former name in V. 1.5: HL7 DHCP APPLICATION PARAMETER)

In V. 1.6, this file includes information about *all* applications (DHCP and non-DHCP) that exchange messages.

771.1

HL7 Field

This file is used for documentation purposes only in V. 1.6, but entries have been added for all HL7 protocol fields, and some minor structural changes have been made.

771.2

HL7 Message Type

Entries have been added for all HL7 message types and a new VERSION field (#3) has been created.

771.3

New name in V. 1.6: HL7 Segment Type

(Former name in V. 1.5: HL7 SEGMENT NAME)

Entries have been added for all HL7 segment types and a new VERSION field (#3) has been created.

771.4

HL7 Data Type

Entries have been added for new HL7 data types and a new VERSION field (#3) has been created.

# Modified Files, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

771.5

New name in V. 1.6: HL7 Version

(Former name in V. 1.5: HL7 VERSION SUPPORTED)

A new STANDARD field (#2) has been added to link each version number with a standard.

772

New name in V. 1.6: HL7 Message Text

(Former name in V. 1.5: HL7 TRANSMISSION)

- Several fields have been added or changed to link messages with new files, such as HL7 Message Status (#771.6), HL7 Error Message (#771.7), and HL Logical Link (#870).
- The labels of several fields have been changed to make them more pertinent.
- Field \# .01 has been changed from a date/time to a pointer to the HL7 Message Administration file (#773).

# Fields Added to the Top Level of the Protocol file (#101)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

770.1

Server Application

Pointer to the HL7 Application Parameter file (#771).

770.2

Client (Subscriber)

Pointer to the HL7 Application Parameter file (#771).

770.3

Message Type

Pointer to the HL7 Message Type file (#771.2).

770.4

Event Type

Pointer to the HL7 Event Type CODE file (#779.001).

770.5

Priority

Set of codes: I for Immediate; D for Deferred.

770.6

Processing ID

Set of codes: D for Debug; T for Training; P for Production.

# Fields Added to the Top Level of the Protocol file (#101), cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

770.7

Logical Link

Pointer to the HL Logical Link file (#870).

770.8

Accept ACK Code

Pointer to the HL7 Accept/Application ACK Condition file (#779.003).

770.9

Application ACK Type

Pointer to the HL7 Accept/Application ACK Condition file (#779.003).

770.95

Version ID

Pointer to the HL7 Version file (#771.5).

771

Generate/Process Routine

M code which calls the message generation or message processing routine for an initial message.

772

Generate/Process ACK Routine

M code which calls the message generation/processing routine for a query response or regular acknowledgment.

773.1

Sending Facility Required?

Set of codes: 1 for Yes; 0 for No.

773.2

Receiving Facility Required?

Set of codes: 1 for Yes; 0 for No.

773.3

Security Required?

Set of codes: 1 for Yes; 0 for No.

773.4

Date/Time of Message Required?

Set of codes: 1 for Yes; 0 for No.

# New Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL 1.6 APPLICATION PARAM EDIT (File \#771)

HL MESSAGING PROTOCOL EDIT (File \#101)

Options

# New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new options support V. 1.6 only:

HL CLEAR COMMUNICATIONS ERROR

Clears the LLP error for a user-specified logical link.

HL CLEAR QUEUE

Reinitializes a queue to zero entries.

HL COMMUNICATIONS SERVER

Menu containing the Communications Server options.

HL COPY QUEUE ENTRY

Copies a message into a queue multiple times. (This option can be used to "test" interfaces by allowing a message to be retransmitted multiple times.)

HL CRE/ED QUEUE TEST ENTRY

Creates a "test" message in a queue and sends it to a non-DHCP system or a DHCP application. (This allows testing of an interface with "test" messages that have been entered into a word-processing field.)

HL CUSTOM REPORT

Prints customized reports about entries in the HL LOGICAL LINK file (#870).

HL EDIT COMM SERVER PARAMETERS

Edits the HL COMMUNICATION SERVER PARAMETER file (#869.3).

HL FILER MONITOR

Used to monitor incoming and outgoing filers.

HL INTERFACE WORKBENCH

Used to define the application (e.g., RADIOLOGY) that will send/receive HL7 messages through the use of various List Manager screens and tools.

HL MANAGE FILERS

Menu containing the options to manage the incoming and outgoing filers.

HL MENU 1.6

Main menu containing all V. 1.6 options.

# New Options, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL MESSAGE MONITOR

Monitor that displays real-time information about serial links.

HL MESSAGE REQUEUER

Activates the HL7 Message Requeuer, which allows users to requeue for transmission selected HL7 messages.

HL QUEUE MANAGEMENT

Menu containing the options to manage the logical link queues and to setup test entries in those queues.

HL SHOW COMMUNICATIONS ERROR

Displays the most recent LLP error for a user-specified logical link.

HL START

Starts a user-specified LLP.

HL START DEFAULT FILERS

Starts the user-specified default number of incoming filers.

HL START ONE INCOMING FILER

Starts the first sequential incoming filer that is not running.

HL START ONE OUTGOING FILER

Starts the first sequential outgoing filer that is not running.

HL STOP

Stops a user-specified LLP.

HL STOP ALL INCOMING FILERS

Stops all incoming filers that are currently running.

HL STOP ALL OUTGOING FILERS

Stops all outgoing filers that are currently running.

HL STOP ONE INCOMING FILER

The first sequential filer in the list of incoming gets flagged to stop.

HL STOP ONE OUTGOING FILER

The first sequential filer in the list of outgoing gets flagged to stop.

# New Options, cont.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following new option supports V. 1.5 only:

HL MENU 1.5

Main menu containing all V. 1.5 options.

# Menu Structure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With this release of DHCP HL7, the menu structure has been modified to distinguish options that support V. 1.5, V. 1.6, or both versions.

HL7 Main Menu

1 V1.5 OPTIONS ...

1 Non-DHCP Application Parameter Enter/Edit

2 Initiate Background Task

3 Start/Stop Log of HL7 Transmissions

2 V1.6 OPTIONS ...

1 Communications Server ...

1 Edit Communication Server parameters

2 Manage incoming & outgoing filers ...

1 Start default number of incoming & outgoing filers

2 Start an incoming filer

3 Start an outgoing filer

4 Stop all incoming filers

5 Stop all outgoing filers

6 Stop an incoming filer

7 Stop an outgoing filer

3 Monitor incoming & outgoing filers

4 Start LLP

5 Stop LLP

6 Systems Link Monitor

7 Logical Link Queue Management ...

1 Show Communications Error

2 Clear Communications Error

3 Create/Edit a Queue Test Entry

4 Copy a Queue Entry

5 Clear a Queue of all Entries

8 Report

2 Interface Workbench

3 Message Requeuer

3 Activate/Inactivate Application

4 Print/Display Menu ...

1 Application Parameters Print/Display

2 Non-DHCP Application Parameters Print/Display

3 Awaiting/Pending Transmissions Print/Display

4 Failed HL7 Transmissions Print/Display

5 Version Print/Display

6 Message Type Print/Display

7 Segment Name Print/Display

8 Data Type Print/Display

9 Fields Print/Display

5 Purge Message Text File Entries