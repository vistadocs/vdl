---
title: "HL7 V. 1.6*19 User Manual: TCP/IP Supplement"
doc_type: UM
doc_label: User Manual
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
file_numbers: 
  - 773
security_keys: []
menu_options: 0
description: 2.1. Client and Server Roles in HL7 over TCP/IP [2-1](#client-and-server-roles-in-hl7-over-tcpip)
audience: 
keywords: 
  - table
  - message
  - contents
  - logical
  - listener
  - link
  - threaded
  - strong
  - messages
  - setup
page_count: 0
word_count: 7342
section_count: 26
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 1999
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6p19.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6p19.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=8"
---

![](hl7-v-1-6-19-user-manual-tcp-ip-supplement/001.png)

DHCPHEALTH LEVEL SEVEN(HL7)USER MANUAL: TCP/IP SUPPLEMENT

Version 1.6\*19

January 1999

V*IST*A Software Development

Table of Contents

1\. Patch HL\*1.6\*19 Release Notes [1-1](#patch-hl1.619-release-notes)

1.1. TCP/IP Transport Layer [1-1](#tcpip-transport-layer)

1.2. View Transmission Log Option [1-2](#view-transmission-log-option)

1.3. Performance Improvements [1-2](#performance-improvements)

1.4. V*IST*A HL7 Documentation Updates [1-3](#vista-hl7-documentation-updates)

1.5. Technical Information [1-3](#technical-information)

1.5.1. New Routines [1-3](#new-routines)

1.5.2. Data Dictionary Modifications [1-3](#data-dictionary-modifications)

2\. How to Set Up TCP/IP Interfaces [2-1](#how-to-set-up-tcpip-interfaces)

2.1. Client and Server Roles in HL7 over TCP/IP [2-1](#client-and-server-roles-in-hl7-over-tcpip)

2.2. Requirements for Sending System [2-1](#requirements-for-sending-system)

2.3. Requirements for Receiving System [2-2](#requirements-for-receiving-system)

2.4. TCP/IP Listener Types [2-2](#tcpip-listener-types)

2.4.1. Single-Threaded Listener [2-2](#single-threaded-listener)

2.4.2. Multi-Threaded Listener [2-3](#multi-threaded-listener)

2.5. How to Set Up TCP/IP Logical Links [2-3](#how-to-set-up-tcpip-logical-links)

2.5.1. How to Set Up TCP/IP Logical Links [2-4](#how-to-set-up-tcpip-logical-links-1)

2.5.2. New Logical Link Fields [2-5](#new-logical-link-fields)

2.6. Acknowledgements Over TCP/IP [2-6](#acknowledgements-over-tcpip)

2.6.1. Original Mode Acknowledgements [2-6](#original-mode-acknowledgements)

2.6.2. Enhanced Mode, Full Two-Phase Commit [2-7](#enhanced-mode-full-two-phase-commit)

2.6.3. Addressing Deferred Acknowledgements [2-8](#addressing-deferred-acknowledgements)

2.7. Exporting TCP/IP Logical Links [2-9](#exporting-tcpip-logical-links)

3\. TCP/IP Listener Setup [3-1](#tcpip-listener-setup)

3.1. How to Set Up Single-Threaded Listeners [3-1](#how-to-set-up-single-threaded-listeners)

3.1.1. Logical Link Setup [3-1](#logical-link-setup)

3.1.2. How to Start and Stop the Listener [3-1](#how-to-start-and-stop-the-listener)

3.2. Multi-Threaded Listener Setup: Caché on NT [3-2](#multi-threaded-listener-setup-caché-on-nt)

3.2.1. Logical Link Setup [3-2](#logical-link-setup-1)

3.2.2. How to Start and Stop the Listener [3-2](#how-to-start-and-stop-the-listener-1)

3.3. Multi-Threaded Listener Setup: DSM for OpenVMS [3-3](#multi-threaded-listener-setup-dsm-for-openvms)

3.3.1. Logical Link Setup [3-3](#logical-link-setup-2)

3.3.2. OpenVMS Account Setup for HL7 Handler [3-4](#openvms-account-setup-for-hl7-handler)

3.3.3. Home Directory Setup for HL7 Handler Account [3-6](#home-directory-setup-for-hl7-handler-account)

3.3.4. DCL Login Command Procedure for HL7 Handler [3-6](#dcl-login-command-procedure-for-hl7-handler)

3.3.5. UCX Service [3-7](#ucx-service)

3.3.6. Access Control List (ACL) Issues [3-8](#access-control-list-acl-issues)

3.3.7. Controlling the Number of Log Files Created by UCX [3-9](#controlling-the-number-of-log-files-created-by-ucx)

3.3.8. How to Start and Stop the Listener [3-9](#how-to-start-and-stop-the-listener-2)

4\. Tracking HL7 Message Transmissions [4-1](#tracking-hl7-message-transmissions)

4.1. For TCP/IP Messages Only [4-1](#for-tcpip-messages-only)

4.2. Choosing What Messages to View [4-1](#choosing-what-messages-to-view)

4.3. Viewing Message Summaries [4-2](#viewing-message-summaries)

4.4. Viewing Message Text [4-3](#viewing-message-text)

5\. Exception Processing API [5-1](#exception-processing-api)

5.1. Why Support Only TCP/IP Interfaces? [5-1](#why-support-only-tcpip-interfaces)

5.2. How to Handle Exceptions [5-1](#how-to-handle-exceptions)

5.3. \$\$DONTPURG^HLUTIL [5-2](#dontpurghlutil)

5.4. \$\$TOPURG^HLUTIL [5-2](#topurghlutil)

5.5. \$\$SETPURG^HLUTIL [5-3](#setpurghlutil)

5.6. \$\$REPROC^HLUTIL [5-3](#reprochlutil)

6\. TCP/IP LLP Implementation Details [6-1](#tcpip-llp-implementation-details)

# Patch HL\*1.6\*19 Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Patch HL\1.6\19 Release Notes](#patch-hl1619-release-notes)
  - [TCP/IP Transport Layer](#tcpip-transport-layer)
  - [View Transmission Log Option](#view-transmission-log-option)
  - [Performance Improvements](#performance-improvements)
  - [VISTA HL7 Documentation Updates](#vista-hl7-documentation-updates)
  - [Technical Information](#technical-information)
    - [New Routines](#new-routines)
    - [Data Dictionary Modifications](#data-dictionary-modifications)
- [How to Set Up TCP/IP Interfaces](#how-to-set-up-tcpip-interfaces)
  - [Client and Server Roles in HL7 over TCP/IP](#client-and-server-roles-in-hl7-over-tcpip)
  - [Requirements for Sending System](#requirements-for-sending-system)
  - [Requirements for Receiving System](#requirements-for-receiving-system)
  - [TCP/IP Listener Types](#tcpip-listener-types)
    - [Single-Threaded Listener](#single-threaded-listener)
    - [Multi-Threaded Listener](#multi-threaded-listener)
  - [How to Set Up TCP/IP Logical Links](#how-to-set-up-tcpip-logical-links)
    - [How to Set Up TCP/IP Logical Links](#how-to-set-up-tcpip-logical-links-1)
    - [New Logical Link Fields](#new-logical-link-fields)
  - [Acknowledgements Over TCP/IP](#acknowledgements-over-tcpip)
    - [Original Mode Acknowledgements](#original-mode-acknowledgements)
    - [Enhanced Mode, Full Two-Phase Commit](#enhanced-mode-full-two-phase-commit)
    - [Addressing Deferred Acknowledgements](#addressing-deferred-acknowledgements)
  - [Exporting TCP/IP Logical Links](#exporting-tcpip-logical-links)
- [TCP/IP Listener Setup](#tcpip-listener-setup)
  - [How to Set Up Single-Threaded Listeners](#how-to-set-up-single-threaded-listeners)
    - [Logical Link Setup](#logical-link-setup)
    - [How to Start and Stop the Listener](#how-to-start-and-stop-the-listener)
  - [Multi-Threaded Listener Setup: Caché on NT](#multi-threaded-listener-setup-caché-on-nt)
    - [Logical Link Setup](#logical-link-setup-1)
    - [How to Start and Stop the Listener](#how-to-start-and-stop-the-listener-1)
  - [Multi-Threaded Listener Setup: DSM for OpenVMS](#multi-threaded-listener-setup-dsm-for-openvms)
    - [Logical Link Setup](#logical-link-setup-2)
    - [OpenVMS Account Setup for HL7 Handler](#openvms-account-setup-for-hl7-handler)
    - [Home Directory Setup for HL7 Handler Account](#home-directory-setup-for-hl7-handler-account)
    - [DCL Login Command Procedure for HL7 Handler](#dcl-login-command-procedure-for-hl7-handler)
    - [UCX Service](#ucx-service)
    - [Access Control List (ACL) Issues](#access-control-list-acl-issues)
    - [Controlling the Number of Log Files Created by UCX](#controlling-the-number-of-log-files-created-by-ucx)
    - [How to Start and Stop the Listener](#how-to-start-and-stop-the-listener-2)
- [Tracking HL7 Message Transmissions](#tracking-hl7-message-transmissions)
  - [For TCP/IP Messages Only](#for-tcpip-messages-only)
  - [Choosing What Messages to View](#choosing-what-messages-to-view)
  - [Viewing Message Summaries](#viewing-message-summaries)
  - [Viewing Message Text](#viewing-message-text)
- [Exception Processing API](#exception-processing-api)
  - [Why Support Only TCP/IP Interfaces?](#why-support-only-tcpip-interfaces)
  - [How to Handle Exceptions](#how-to-handle-exceptions)
  - [\$\$DONTPURG^HLUTIL](#dontpurghlutil)
  - [\$\$TOPURG^HLUTIL](#topurghlutil)
  - [\$\$SETPURG^HLUTIL](#setpurghlutil)
  - [\$\$REPROC^HLUTIL](#reprochlutil)
- [TCP/IP LLP Implementation Details](#tcpip-llp-implementation-details)

## TCP/IP Transport Layer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As originally released, DHCP HL7 V. 1.6 supports transmission of HL7 messages between systems using the following transport mechanisms:

- Serial communications lines
- MailMan messages

Patch HL\*1.6\*19 adds an additional transport mechanism:

- Transmission Control Protocol/Internet Protocol (TCP/IP)

V*IST*A systems can now exchange HL7 messages over a TCP/IP network with both V*IST*A and non-V*IST*A systems.

Patch HL\*1.6\*19 supports *bi-directional* transmission of HL7 messages over TCP/IP, using the Minimal Lower Layer Protocol (MLLP) protocol, described later in the *TCP/IP LLP Implementation* chapter. Patch HL\*1.6\*19 implements bi-directional transmission as follows:

- The initiator of a transaction is the sending system.
- After the initial message is sent, the sending system waits for the expected response from the receiving system, which should be returned over the same open channel.
- Upon receipt of the response, the transaction is considered complete.
- If the sending system has another transaction in the queue to send, it is sent.
- At the completion of the last transaction, the connection is closed.
- The receiving system cannot initiate a new transaction of its own over the same open channel (it must open a new connection to do this.)

A number of V*IST*A's HL7 transactions currently use VA MailMan as their transport layer; moving these transactions to TCP/IP logical links may be desirable to take advantage of TCP/IP transport layer features such as immediate commit acknowledgements.

## View Transmission Log Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch HL\*1.6\*19 introduces a new option, View Transmission Log. Using a VA FileMan Browser interface, you can query the transmission log to see pending or transmitted messages. You can filter the message view by date entered, message type and event type.

This new option replaces the former method of scanning globals directly to analyze message transmissions.

## Performance Improvements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By restructuring the use of files, patch HL\*1.6\*19 reduces by at least 50% the disk hits incurred by the creation and transmission of HL7 messages.

Before patch HL\*1.6\*19, to create and transmit a message, the HL7 package incurred 5 major disk writes:

1.  Store outgoing message text in File \# 772 (HL7 Message Text).
2.  Store a message ID and date/time in File \# 773 (HL7 Message Administration).
3.  When attaching a recipient, create a new stub entry in File \# 772.
4.  When attaching a recipient, create a new stub entry in File \# 773.
5.  When transmitting, create a new entry in File \# 870 (HL Logical Link), combine text and recipient information from File \# 772 and 773, attach a message header, and then transmit completely formed message.

Patch HL\*1.6\*19 consolidates the storage of non-TCP/IP message components in File \#772 (HL7 Message Text) and expands the use of File \# 773 (HL7 Message Administration) file for TCP/IP messages.

After patch HL\*1.6\*19, for all messages except those transmitted over TCP/IP, the HL7 package now incurs only 3 major disk writes:

1.  Store outgoing message text, message ID and date/time in File \# 772.
2.  Store recipient information in File \#772.
3.  When transmitting, create a new entry in File \# 870 (HL Logical Link), combines text and recipient information from File \# 772, attach a message header, and then transmit completely formed message.

After patch HL\*1.6\*19, for all messages transmitted over TCP/IP, to create and transmit a message, the HL7 package now incurs only 2 major disk writes:

1.  Store outgoing message text in File \# 772.
2.  Store recipient information in File \#773.
3.  When transmitting, transmit directly from information in File \#772 and File \#773.

A future patch to the HL7 package will result in all message transmissions (not just TCP/IP transmission) being performed directly out of file \#772 and file \#773, minimizing the number of disk hits and maximizing package performance.

## V*IST*A HL7 Documentation Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A HL7 application is being updated through enhancement patches. Two supplemental manuals to the original documentation are provided (this manual for patch HL\*1.6\*19, and the *DHCP HL7 Developer Manual: Dynamic Addressing Supplement* for patch HL\*1.6\*14). Eventually, a single, consolidated, revised HL7 User Manual will be provided, combining all current and future revisions for both original HL7 User (site manager) and Developer manuals. Release will coincide with the release of future Messaging functionality, slated for FY99Q4.

## Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HLCSHDR1, HLCSRPT, HLCSRPT1, HLCSTCP, HLCSTCP1, HLCSTCP2, HLPAT19, HLTP3, HLTP4 , HLTPCK2, HLTPCK2A

### Data Dictionary Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File \# 869.1 HL LOWER LEVEL PROTOCOL TYPE

> New Data:

- One record, TCP, has been added and will be merged into your current data.

File \# 869.2 HL LOWER LEVEL PROTOCOL PARAMETER

> New Fields:

- TCP/IP ADDRESS (F) \[400;1\]
- TCP/IP PORT (NJ5,0) \[400;2\]
- TCP/IP SERVICE TYPE (S) \[400;3\]
- PERSISTENT (S) \[400;4\]
- STARTUP NODE (P14.7) \[400;6\]

File \# 771.6 HL7 MESSAGE STATUS

> New Data:

- Several new statuses have been added and will overwrite your current data.

File \# 771.7 HL7 ERROR MESSAGE

> New Data:

- Several new errors messages have been added and will overwrite your current data.

File \# 772 HL7 MESSAGE TEXT

> Changed Field Definition:

- The .01 field, DATE/TIME ENTERED, has been changed from a pointer to a date/time field.

File \#773 HL7 MESSAGE ADMINISTRATION

> Changed Field Definition:

- The .01 field, DATE/TIME ENTERED, has been changed from a date/time to a pointer to file 772.

> New Fields:

- TRANSMISSION TYPE (RSI), \[0;3\]
- PRIORITY (S), \[0;4\]
- HEADER TYPE (S), \[0;5\]
- ACKNOWLEDGEMENT TO (P773'), \[0;6\]
- LOGICAL LINK (P870'), \[0;7\]
- SUBSCRIBER PROTOCOL (P101'), \[0;8\]
- SECURITY (F), \[0;9\]
- DON'T PURGE (S), \[2;1\]
- CONTINUATION POINTER (F), \[1;1\]
- SENDING APPLICATION (P771'), \[0;11\]
- RECEIVING APPLICATION (P771'), \[0;12\]
- MESSAGE TYPE (P771.2'), \[0;13\]
- EVENT TYPE (P779.001'), \[0;14\]
- STATUS (RP771.6'), \[P;1\]
- STATUS UPDATE DATE/TIME (D), \[P;2\]
- ERROR MESSAGE (F), \[P;3\]
- ERROR TYPE (P771.7'), \[P;4\]
- DATE/TIME PROCESSED (D), \[S;1\]
- MSH (Multiple-773.01), \[MSH;0\]
- .01 MSH (WL), \[0;1\]

# How to Set Up TCP/IP Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Client and Server Roles in HL7 over TCP/IP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two separate sets of M code define the roles of client and server over TCP/IP channels:

- TCP Client = Sender = HL7 Server Protocol (Event Driver)
- TCP Server = Receiver = HL7 Client Protocol (Subscriber)

## Requirements for Sending System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the sending system is a V*IST*A system, the sending application (as defined in the Interface Workbench on the sending V*IST*A system) must have:

- A server (event driver) protocol set up for each message transaction type.
- A client (subscriber) protocol set up for each destination for each message transaction type.
- HL LOGICAL LINK entries set up for each destination system, with all appropriate information including IP address and port.

All messages generated through the server (event driver) protocol will be directed to all appropriate client (subscriber) protocols, including receivers whose HL LOGICAL LINK identifies them as connected through TCP/IP.

## Requirements for Receiving System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the receiving system is not a V*IST*A system, it must support bi-directional TCP/IP transmission, with a TCP/IP listener process that responds to connection requests.

If the receiving system is a V*IST*A system, the receiving application (as defined in the Interface Workbench on the receiving V*IST*A system) must have:

- A server (event driver) protocol set up for each transaction type.
- A client (subscriber) protocol set up for each transaction type.
- A running TCP/IP listener. The TCP/IP listener is a process that listens for TCP/IP connection requests on a particular IP address and port. The listener process must be set up by the receiving site to be actively listening.

## TCP/IP Listener Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two types of TCP/IP listeners are supported by the HL7 package:

- Single-Threaded
- Multi-Threaded

### Single-Threaded Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Single-threaded listeners are best suited for connecting to a specific device over TCP/IP, such as a single Commercial Off-The-Shelf (COTS) system. The HL7 package's single-threaded listener is implemented as an M process running on the server. It waits for connection requests and handles all processing for each connection directly without spawning another job.

The drawback to single-threaded listeners is that if the listener is busy processing an incoming HL7 message during an active connection, other connection requests fail.

For instructions on how to set up single-threaded TCP/IP listeners, please see the "TCP/IP Listener Setup" chapter.

### Multi-Threaded Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multi-threaded listeners are useful when multiple connection requests come to a single port from many devices or systems. An example of this scenario is the use of HL7 messaging by the Clinical Information Resource Network (CIRN). Because multi-threaded listeners spawn off separate handlers for each client connection request, they enable multiple concurrent connections.

For instructions on how to set up multi-threaded TCP/IP listeners, please see the "TCP/IP Listener Setup" chapter.

## How to Set Up TCP/IP Logical Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each client (subscriber) protocol must point to a particular HL LOGICAL LINK entry, identifying the destination system to send the message to. Use the HL7 package's Interface Workbench to set up logical links.

For client (subscriber) protocols that need to connect to destination systems over TCP/IP, you need to set up a logical link for each destination system, with LLP Type set to TCP. Other fields in the logical link describe other characteristics of the destination system, including its TCP/IP address and listener port.

You must also define logical links for each TCP/IP listener on the current system. At a site, this is typically the responsibility of IRM. For more information see the "TCP/IP Listener Setup" chapter.

> **NOTE:** HL LOGICAL LINK entries are not tied to any one protocol, and so can be reused by other protocols.

### How to Set Up TCP/IP Logical Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Interface Workbench to create Logical Link entries for systems other than the current system. This link stores the path to a target system. The following field settings are appropriate for TCP/IP destination logical links:

> LLP Type: TCP

> TCP/IP address: Address of target system

> TCP/IP Port: Port the target system is listening on

> TCP/IP Service Type: CLIENT

> Persistent: Null if link is transient, YES if link should remain open always

> HL-7 Interface Workbench Sep 03, 1998 13:16:55 Page: 15 of 27

> Currently Defined

> Logical Links

> =================================================================================

> \(21\) VAWPX

> LLP Parameter: VAWPX TCP TCP/IP Address: 152.131.120.201

> LLP Type: TCP (T) TCP/IP Port: 5000

> Queue Size: \<DEFAULT\> TCP/IP Service Type: CLIENT

> Institution: \<NONE\> Persistent: \<DEFAULT\>

> Domain: \<NONE\> Startup Node: \<NONE\>

> Autostart: \<DEFAULT\>

#### Starting TCP/IP Logical Links

Starting up a Logical Link (with the START LLP option) is all you need to do to enable exchange of messages over the link. This starts up a process specific to the logical link that runs until you shut down the logical link.

No outbound filers are used for TCP/IP logical links. Instead, the role of the logical link process is expanded. Besides transmitting messages, the logical link process itself also detects whether there are messages to send for the logical link.

A consequence of this shift is that, for the time being, if you have 150 TCP/IP logical links for 150 destinations, 150 logical link processes will run concurrently. A future patch will address this issue, ideally before any system has near that many TCP/IP logical links. The future patch will introduce a queue manager that will start TCP/IP logical link processes only when they are needed to transmit outgoing messages.

### New Logical Link Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch HL\*1.6\*19 introduces new fields to the HL LOWER LEVEL PROTOCOL PARAMETER file (#869.2) for TCP/IP logical links:

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 25%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Field#</strong></td>
<td><strong>Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>400.01</td>
<td>TCP/IP ADDRESS</td>
<td>TCP/IP address of the target system. Leave blank if describing a listener on the current system.</td>
</tr>
<tr class="odd">
<td>400.02</td>
<td>TCP/IP PORT</td>
<td>TCP/IP port to connect to (target system) or listen on (current system).</td>
</tr>
<tr class="even">
<td>400.03</td>
<td>TCP/IP SERVICE TYPE</td>
<td><ul>
<li><p>'CLIENT (SENDER)': Indicates that this Logical Link connects to a target system, with the current system acting as the sender.</p></li>
<li><p>'SINGLE LISTENER': Designates that the current system is a server (listener), using a single threaded listener.</p></li>
<li><p>'MULTI LISTENER': Designates that the current system is a server (listener), using a multiple threaded listener.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>400.04</td>
<td>PERSISTENT</td>
<td>For TCP/IP SERVICE TYPE of Client only. Enter 'YES' if this connection needs to remain open even if there are no messages to send. A setting of 'YES' is appropriate for sending high volumes of messages to a COTS device. The connection remains open until either side disconnects it. On the <strong>V</strong><em>IST</em><strong>A</strong> side, disconnection is by shutting-down the logical link.</td>
</tr>
<tr class="even">
<td>400.06</td>
<td>STARTUP NODE</td>
<td>Applies only if the current system is a listener, and is running dual TaskMan in a DCL context (OpenVMS systems only). If one or more clients can only connect to a single IP address (i.e., a particular node) you can use this field to force links (started by TaskMan) to start up on that particular node.</td>
</tr>
</tbody>
</table>

## Acknowledgements Over TCP/IP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In HL7 versions 2.2 and above, Enhanced Mode differentiates between *commit accept acks* and *application acks*. The acknowledgement scheme is defined in the message header. The following protocol settings define the acknowledgement scheme in the message headers for V*IST*A HL7:

- ACCEPT ACKNOWLEDGEMENT
- APPLICATION ACKNOWLEDGEMENT

Acknowledgements are performed as follows, based on these two settings:

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 58%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Accept Ack<br />
[MSH-15]</strong></td>
<td><strong>Application<br />
Ack<br />
[MSH-16]</strong></td>
<td><strong><br />
<br />
Ack Mode</strong></td>
<td><strong><br />
<br />
Behavior</strong></td>
</tr>
<tr class="even">
<td>null</td>
<td>null</td>
<td>Original</td>
<td>Application ack</td>
</tr>
<tr class="odd">
<td>NE</td>
<td>AL</td>
<td>Original</td>
<td>Application ack</td>
</tr>
<tr class="even">
<td>AL</td>
<td>AL</td>
<td>Enhanced</td>
<td>Commit ack, application ack<br />
(i.e., enhanced mode full two-phase commit)</td>
</tr>
<tr class="odd">
<td>AL</td>
<td>NE</td>
<td>Enhanced</td>
<td>Commit ack, no application ack</td>
</tr>
<tr class="even">
<td>NE</td>
<td>NE</td>
<td>Enhanced</td>
<td>No commit ack, no application ack</td>
</tr>
</tbody>
</table>

### Original Mode Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Original mode, the receiving application is always expected to return a response (i.e., an application acknowledgement). This response may or may not contain data, but always contains an ack. For example, a query response will contain both data and an ack message.

Expected Behavior, Original Mode Acknowledgements over TCP/IP

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sending System</strong></td>
<td><strong>Receiving System</strong></td>
</tr>
<tr class="even">
<td><p>1. Open Connection.</p>
<p>2. Send Message.</p></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><p>3. Process Message.</p>
<p>4. Send Query Response or General Ack (AA, AE, AR).</p></td>
</tr>
<tr class="even">
<td><p>5. Process Response. If not a positive ack, retransmit (go to step 2.)</p>
<p>6. Drop Connection.</p></td>
<td></td>
</tr>
</tbody>
</table>

### Enhanced Mode, Full Two-Phase Commit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Enhanced mode acknowledgements with full two-phase commit, over TCP/IP, the COMMIT ACK should always be immediate and over the current connection. The application acknowledgement should always be deferred, and performed as a separate transaction. This means that the application ack is always deferred and the final "commit" is optional.

Expected Behavior, Enhanced Mode Two-Phase Commit over TCP/IP

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Sending System</strong></td>
<td><strong>Receiving System</strong></td>
</tr>
<tr class="even">
<td colspan="2">Phase I</td>
</tr>
<tr class="odd">
<td><p>1. Open Connection.</p>
<p>2. Transmit Message.</p></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><p>3. Receive Message.</p>
<p>4. Validate Header.</p>
<p>5. Store on local system.</p>
<p>6. Transmit "Commit Accept Ack" (MSA contains 'CA').</p></td>
</tr>
<tr class="odd">
<td><p>7. Receive Commit Ack.</p>
<p>8. Process/validate Commit Ack. If not a positive commit ack, retransmit (go to step 2.)</p>
<p>9. Drop Connection.</p></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2">Phase II</td>
</tr>
<tr class="odd">
<td></td>
<td><p>1. Open Connection.</p>
<p>2. Transmit Application Response. Acknowledgment mode in header must be AL/NE or NE/NE.</p>
<p>3. If Ack mode of application response is NE/NE, drop connection.</p></td>
</tr>
<tr class="even">
<td><p>4. Receive Application Response.</p>
<p>5. Validate Header.</p>
<p>6. Store on local system.</p>
<p>7. If MSH-15='AL', transmit "Commit Accept Ack" (MSA contains 'CA').</p></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><p>8. Receive Commit Accept Ack (if any).</p>
<p>8. Process/Validate Commit Accept Ack. If not a positive commit ack, retransmit (go to step 2.)</p>
<p>10. Drop Connection.</p></td>
</tr>
</tbody>
</table>

### Addressing Deferred Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you process a message, the way to send an application acknowledgement is calling GENACK^HLMA1. Among other things, GENACK^HLMA1 handles the details of where to address the response *to*, as follows:

1\. During application processing of a message, the event driver and subscriber protocols involved in the transaction are available in HL("EID") and HL("EIDS").

2\. The application calls GENACK^HLMA1 to send an application acknowledgement. It should pass HL("EIDS") as the parameter for the transaction's subscriber protocol.

3\. GENACK^HLMA1 uses the subscriber protocol's logical link as the destination to return the response to.

This method works fine for traditional, point-to-point interfaces where the relationship between sender and receiver is defined in advance. However, with the introduction of *dynamic addressing*, transactions occur where the sender and receiver are *not* defined in advance. This poses a problem in certain situations.

For dynamically addressed messages over TCP/IP where original mode is used, returning application acknowledgements is *not* a problem, because the response is returned over the open TCP/IP channel.

However, for *enhanced mode, two-phased commit transactions* over TCP/IP, where the response is deferred, the method used by the GENACK^HLMA1 to address responses doesn't work. While GENACK^HLMA1 still sends the application acknowledgement back over the single logical link attached to the transaction's subscriber protocol, that logical link may have no correspondence with the actual originating system.

A future patch will support HL7 V. 2.3-style message headers, where all the information needed to address a response to a message is contained in that message's header (rather than in the advance interface setup). This more *flexible* arrangement will allow GENACK^HLMA1 to properly address deferred application acknowledgements for interfaces that are not point-to-point. Until this issue is resolved, however, there are two workarounds:

- Use original mode, which skips the commit acknowledgement and instead returns the application acknowledgement over the open TCP/IP channel.
- If the sender is a V*IST*A facility, and if that facility's institution number is in the original message's facility field, use the dynamic addressing features released in patch HL\*1.6\*14 to resolve the proper logical link and dynamically address the response.

## Exporting TCP/IP Logical Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel Installation and Distribution System (KIDS) allows you to export HL LOGICAL LINK and HL LOWER LEVEL PROTOCOL PARAMETER entries. You will, however, need to instruct sites to modify certain site-specific fields in any HL LOWER LEVEL PROTOCOL PARAMETER entries you export.

1.  Export all HL LOWER LEVEL PROTOCOL PARAMETER entries with TCP/IP SERVICE TYPE set to CLIENT (SENDER), and TCP/IP ADDRESS defined. This exports all logical links as client connections to target systems.
2.  Instruct sites to change their own logical link from client to server. To do this, they should change the HL LOWER LEVEL PROTOCOL PARAMETER settings for their own site as follows:
- Delete the TCP/IP ADDRESS for their own site.
- Change the TCP/IP SERVICE TYPE setting for their own site to SINGLE LISTENER or MULTI LISTENER (depending on what type of listener the site will use).

# TCP/IP Listener Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How to Set Up Single-Threaded Listeners

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Single-threaded listener mode for TCP/IP messaging is available for all currently supported M operating systems:

- Caché on NT
- DSM for OpenVMS

To set up single-threaded listeners, simply define an entry in the HL LOGICAL LINK file for each single-threaded listener. No additional setup is required.

### Logical Link Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Interface Workbench, create a Logical Link entry for the single threaded listener. The following field settings are appropriate for single-threaded listeners:

> LLP Type: TCP

> TCP/IP address: DSM for OpenVMS: null; Caché for NT: IP address of listener system

> TCP/IP Port: Port to listen on.

> TCP/IP Service Type: SINGLE LISTENER

> Persistent: Null

> Startup Node: (set only for OpenVMS systems running dual TaskMan.)

> HL-7 Interface Workbench Sep 03, 1998 13:16:55 Page: 15 of 27

> Currently Defined

> Logical Links

> =================================================================================

> \(22\) A6A LISTENER

> LLP Parameter: A6A5000 TCP/IP Address: \<NONE\>

> LLP Type: TCP (T) TCP/IP Port: 5000

> Queue Size: \<DEFAULT\> TCP/IP Service Type: SINGLE LISTENER

> Institution: \<NONE\> Persistent: \<DEFAULT\>

> Domain: \<NONE\> Startup Node: \<NONE\>

> Autostart: \<DEFAULT\>

### How to Start and Stop the Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start single-threaded listeners, use the Start LLP option. Choose the Logical Link entry you defined for the listener. Typically you would run the link in the background. To stop the listener, use the Stop LLP option.

## Multi-Threaded Listener Setup: Caché on NT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel patch XU\*8\*78 provides a multi-threaded listener for TCP/IP messaging for Caché on NT systems.

### Logical Link Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Interface Workbench, create a Logical Link entry for the multi-threaded listener. The following field settings are appropriate for multi-threaded listeners for Caché on NT:

> LLP Type: TCP

> TCP/IP address: IP address of listener system

> TCP/IP Port: (the port to listen on)

> TCP/IP Service Type: MULTI LISTENER

> Persistent: null

> Startup Node: (set only for OpenVMS systems running dual TaskMan.)

> HL-7 Interface Workbench Sep 03, 1998 13:16:55 Page: 15 of 27

> Currently Defined

> Logical Links

> =================================================================================

> \(23\) A6A UCX LISTENER

> LLP Parameter: A6A5000 TCP/IP Address: \<NONE\>

> LLP Type: TCP (T) TCP/IP Port: 5000

> Queue Size: \<DEFAULT\> TCP/IP Service Type: MULTI LISTENER

> Institution: \<NONE\> Persistent: \<DEFAULT\>

> Domain: \<NONE\> Startup Node: \<NONE\>

> Autostart: \<DEFAULT\>

### How to Start and Stop the Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start the multi-threaded listener for Caché on NT systems, use the Start LLP option. Choose the Logical Link entry you defined for this listener. Typically you would run the link in the background. To stop the listener, use the Stop LLP option.

## Multi-Threaded Listener Setup: DSM for OpenVMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For DSM for OpenVMS, multi-threaded listeners are implemented externally, using DSM for OpenVMS's UCX (also known as Digital TCP/IP Services for OpenVMS). UCX permits multiple TCP/IP clients to connect and run as concurrent processes, up to the limits established by the system. UCX listens on a particular port, and launches a specified HL7 handler process for each client connection.

For the UCX HL7 handler process, you need to create:

- an OpenVMS account
- a home directory
- a DCL (Digital Command Language) login command procedure

For the sake of the example in this chapter, the HL7 handler account name is HLSEVEN, the home directory is \[HLSEVEN\] and the DCL login command procedure is named HLSEVEN.COM.

### Logical Link Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using the Interface Workbench, create a Logical Link entry for the multi-threaded listener. The following field settings are appropriate for multi-threaded listeners implemented through UCX:

> LLP Type: TCP

> TCP/IP address: null

> TCP/IP Port: (the port to listen on)

> TCP/IP Service Type: MULTI LISTENER

> Persistent: null

> Startup Node: (set only for OpenVMS systems running dual TaskMan.)

> **NOTE:** If you are *converting an existing logical link* to become a logical link for the UCX TCP/IP listener, rather than creating a new one, follow this procedure:

> 1\. First, stop the logical link.

> 2\. Next, use the "Clear a Queue of all Entries" option on the logical link. This resets all message counters and flags, ensuring the queue is initialized correctly.

> 3\. Now use the Interface Workbench to change the logical link to TCP/IP.

> HL-7 Interface Workbench Sep 03, 1998 13:16:55 Page: 15 of 27

> Currently Defined

> Logical Links

> =================================================================================

> \(23\) A6A UCX LISTENER

> LLP Parameter: A6A5000 TCP/IP Address: \<NONE\>

> LLP Type: TCP (T) TCP/IP Port: 5000

> Queue Size: \<DEFAULT\> TCP/IP Service Type: MULTI LISTENER

> Institution: \<NONE\> Persistent: \<DEFAULT\>

> Domain: \<NONE\> Startup Node: \<NONE\>

> Autostart: \<DEFAULT\>

### OpenVMS Account Setup for HL7 Handler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The easiest way to configure an OpenVMS account to be an HL7 handler is to copy most of the parameters from VA MailMan TCP account. To do this:

1.  Determine an unused User Identification Code (UIC), typically in the same group as other DSM for OpenVMS accounts.
2.  Using the OpenVMS Authorize utility, copy the XMINET account to a new HLSEVEN account with the unused UIC. You must have SYSPRV to do this.
3.  Make sure that the account settings for the new HLSEVEN account are the same as in the example below, or, if they are different, that the impact of the different settings is acceptable for your system. In particular, make sure that the DisCtlY, Restricted and Captive flags are set for security reasons.

#### Account Setup Example (Contains Recommended Settings)

> \$SET DEF SYS\$SYSTEM

> \$MC AUTHORIZE

> UAF\> SHOW XMINET

> Username: XMINET Owner: DSM

> Account: UIC: \[50,44\] (\[XMINET\])

> CLI: DCL Tables: DCLTABLES

> Default: SYS\$SYSDEVICE:\[XMINET\]

> LGICMD: NL:

> Flags: DisCtlY Restricted Captive

> Primary days: Mon Tue Wed Thu Fri

> Secondary days: Sat Sun

> Primary 000000000011111111112222 Secondary 000000000011111111112222

> Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

> Network: \##### Full access \###### \##### Full access \######

> Batch: ----- No access ------ ----- No access ------

> Local: ----- No access ------ ----- No access ------

> Dialup: ----- No access ------ ----- No access ------

> Remote: ----- No access ------ ----- No access ------

> Expiration: (none) Pwdminimum: 6 Login Fails: 0

> Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

> Last Login: (none) (interactive), 10-FEB-1998 15:30 (non-interactive)

> Maxjobs: 0 Fillm: 500 Bytlm: 100000

> Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

> Maxdetach: 0 BIOlm: 150 JTquota: 4096

> Prclm: 8 DIOlm: 18 WSdef: 1344

> Prio: 4 ASTlm: 176 WSquo: 2688

> Queprio: 4 TQElm: 10 WSextent: 65536

> CPU: (none) Enqlm: 3000 Pgflquo: 100000

> Authorized Privileges:

> NETMBX OPER SHARE TMPMBX

> Default Privileges:

> NETMBX OPER SHARE TMPMBX

> UAF\> COPY XMINET HLSEVEN/UIC=\[51,45\]

> %UAF-I-COPMSG, user record copied

> %UAF-W-DEFPWD, copied or renamed records must receive new password

> %UAF-I-RDBADDMSGU, identifier HLSEVEN value \[000051,000045\] added to rights database

> UAF\> SHOW HLSEVEN

> Username: HLSEVEN Owner: DSM

> Account: UIC: \[51,45\] (\[HLSEVEN\])

> CLI: DCL Tables: DCLTABLES

> Default: SYS\$SYSDEVICE:\[XMINET\]

> LGICMD: NL:

> Flags: DisCtlY Restricted Captive

> Primary days: Mon Tue Wed Thu Fri

> Secondary days: Sat Sun

> Primary 000000000011111111112222 Secondary 000000000011111111112222

> Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

> Network: \##### Full access \###### \##### Full access \######

> Batch: ----- No access ------ ----- No access ------

> Local: ----- No access ------ ----- No access ------

> Dialup: ----- No access ------ ----- No access ------

> Remote: ----- No access ------ ----- No access ------

> Expiration: (none) Pwdminimum: 6 Login Fails: 0

> Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

> Last Login: (none) (interactive), (none) (non-interactive)

> Maxjobs: 0 Fillm: 500 Bytlm: 100000

> Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

> Maxdetach: 0 BIOlm: 150 JTquota: 4096

> Prclm: 8 DIOlm: 18 WSdef: 1344

> Prio: 4 ASTlm: 176 WSquo: 2688

> Queprio: 4 TQElm: 10 WSextent: 65536

> CPU: (none) Enqlm: 3000 Pgflquo: 100000

> Authorized Privileges:

> NETMBX OPER SHARE TMPMBX

> Default Privileges:

> NETMBX OPER SHARE TMPMBX

> UAF\> MOD HLSEVEN/DIR=\[HLSEVEN\]

> %UAF-I-MDFYMSG, user record(s) updated

> UAF\> EXIT

> %UAF-I-DONEMSG, system authorization file modified

> %UAF-I-RDBDONEMSG, rights database modified

### Home Directory Setup for HL7 Handler Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to create a home directory for the HL7 handler account. This directory will house the DCL command procedure that is executed whenever a client connects, as well as log files. Make sure that the owner of the directory is the HLSEVEN account.

For example, to create a home directory named \[HLSEVEN\] with ownership of HLSEVEN:

> \$CREATE/DIR \[HLSEVEN\]/OWNER=HLSEVEN

### DCL Login Command Procedure for HL7 Handler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a DCL command procedure like the following, in the home directory for the handler account. Make sure the command procedure file is owned by the HL7 handler account.

1.  Adjust the DSM command line (environment, UCI and volume set) so that it is correct for your system.
2.  If access control is enabled, ensure that the HLSEVEN account has access to this UCI, volume set and routine.
3.  Replace 999 with the internal entry number of the logical link you created (in the HL LOGICAL LINK file) to be invoked by the listener-spawned process.

> \$!HLSEVEN.COM - for incoming connect requests

> \$!------------------------------------------------------------------

> \$ set noon !Don't stop

> \$ set verify

> \$ purge/keep=2 sys\$login:\*.\*

> \$ set proc/priv=(share) !Required to use the MBX device

> \$ x=f\$trnlnm("sys\$net") !This is our MBX device

> \$ write sys\$output x !This can be viewed in the log file

> \$ set nover !Turn off verify

> \$!------------------------------------------------------------------

> \$! \*\*Be sure this command line is correct for your system

> \$! \*\*and if access control is enabled that this account has

> \$! \*\*access to this uci,vol & routine. The number 999 should be replaced

> \$! \*\*with the internal entry number in file 870 for this Logical Link

> \$! /

> \$ dsm/environ=MGRISC/uci=VAH/vol=ROU/data="''x'^999" EN^HLCSTCP

> \$!------------------------------------------------------------------

> \$ logout/brief

### UCX Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you've created the HL7 handler, you can create the UCX service that will listen for connections and launch the HL7 handler. Choose the port it should listen on, and the user and command file to invoke when a connection is received.

For a test account, you can set up a UCX service for testing, and it can use the same OpenVMS account and directory as the production UCX service. Just create a different DCL command file with the UCI and volume set of the test account.

> *(Note: Since UCX is node specific, make sure you are on the correct node.)*

> \$UCX

> UCX\> SET SERVICE HLSEVEN/USER=HLSEVEN/PROC=HLSEVEN /PORT=5000-

> \_UCX\> /PROTOCOL=TCP/REJECT=MESSAGE="All channels busy" -

> \_UCX\> /LIMIT=50/FILE=SYS\$SYSDEVICE:\[HLSEVEN\]HLSEVEN.COM

> UCX\> SHO SERVICE HLSEVEN/FULL

> Service: HLSEVEN

> State: Disabled

> Port: 5000 Protocol: TCP Address: 0.0.0.0

> User_name: not defined Process: HLSEVEN

> UCX\> ENABLE SERVICE HLSEVEN

> UCX\> SET CONFIG ENABLE SERVICE HLSEVEN

> UCX\> SHO SERVICE/FULL HLSEVEN

> Service: HLSEVEN

> State: Enabled

> Port: 5000 Protocol: TCP Address: 0.0.0.0

> Inactivity: 5 User_name: HLSEVEN Process: HLSEVEN

> Limit: 50 Active: 0 Peak: 0

> File: SYS\$SYSDEVICE:\[HLSEVEN\]HLSEVEN.COM

> Flags: Listen

> Socket Opts: Rcheck Scheck

> Receive: 0 Send: 0

> Log Opts: None

> File: not defined

> Security

> Reject msg: All channels busy

> Accept host: 0.0.0.0

> Accept netw: 0.0.0.0

> UCX\> SHO CONFIG ENABLE SERVICE

> Enable service

> FTP, FTP_CLIENT, HLSEVEN, MPI, TELNET, XMINETMM

> UCX\> EXIT

### Access Control List (ACL) Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some sites use DSM's ACL feature, which gives explicit access to each OpenVMS account that needs to enter that DSM environment. If your site is using ACL, you should set up the HLSEVEN account with APPLICATION access, and then specify the Volume, UCI and routine that the HLSEVEN user has authorization to access.

An example of setting this level of access for an HLSEVEN account is provided below:

> \$ DSM /MAN ^ACL

> Environment Access Utilities

> 1\. ADD/MODIFY USER (ADD^ACL)

> 2\. DELETE USER (DELETE^ACL)

> 3\. MODIFY ACTIVE AUTHORIZATIONS (^ACLSET)

> 4\. PRINT AUTHORIZED USERS (PRINT^ACL)

> Select Option \> 1 ADD/MODIFY USER

> OpenVMS User Name: \> HLSEVEN

> ACCESS MODE VOL UCI ROUTINE

> ----------- --- --- -------

> No access rights for this user.

> Access Mode (\[M\]ANAGER, \[P\]ROGRAMMER, or \[A\]PPLICATION): \> A

> Volume set name: \> VAH

> UCI: \> ROU

> Routine: \> HLCSTCP

> Routine: \> \<RET\>

> UCI: \> \<RET\>

> Volume set name: \> \<RET\>

> Access Mode (\[M\]ANAGER, \[P\]ROGRAMMER, or \[A\]PPLICATION): \> \<RET\>

> USER ACCESS MODE VOL UCI ROUTINE

> ---- ----------- --- --- -------

> HLSEVEN APPLICATION VAH ROU HLCSTCP

> OK to file? \<Y\> \<RET\>

> OpenVMS User Name: \> \<RET\>

> OK to activate changes now? \<Y\> \<RET\>

> Creating access authorization file: SYS\$SYSDEVICE:\[DSMMGR\]DSM\$ACCESS.DAT.

### Controlling the Number of Log Files Created by UCX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new HLSEVEN service will automatically create log files (UCX does this and it cannot be prevented) in the HLSEVEN directory named HLSEVEN.LOG;xxx where 'xxx' is a file version number. New versions of this file will be created until that file version number reaches the maximum number of 32767. In order to minimize the number of log files created, you may want to initially rename this log file to the highest version number with the command:

\$ RENAME disk\$:\[HLSEVEN\]HLSEVEN.LOG; disk\$:\[HLSEVEN\]HLSEVEN.LOG;32767

Alternatively, you can set a limit on the number of versions of the log file that can concurrently exist in the HLSEVEN directory:

\$ SET FILE /VERSION_LIMIT=10 disk\$:\[HLSEVEN\]HLSEVEN.LOG;

Note that you would not want to limit the number of versions of the log file until you know that your HLSEVEN service is working correctly; you can use the log file to help diagnose problems with the service/account.

### How to Start and Stop the Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although the multi-threaded listener for OpenVMS systems requires the setup of a logical link, you never actually start or stop this logical link with HL7 package options. Instead, because the listener is implemented as a UCX service, start it up and shut it down by using the generic tools UCX provides to start up and shut down any UCX service.

# Tracking HL7 Message Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new View Transmission Log option makes it easier to look at which HL7 messages have been transmitted (incoming and outgoing) or are pending for transmission. This new option replaces the more tedious former process of looking through globals.

## For TCP/IP Messages Only

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Transmission Log option tracks messages transmitted over TCP/IP logical links only, at this time. The option takes advantage of new, simplified file structures in the HL7 package, currently used only for TCP/IP message transmission. Eventually, messages transmitted over non-TCP/IP logical links will be converted to use the new file structure, and will then be viewable in the View Transmission Log option.

## Choosing What Messages to View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Choose the ‘View Transmission Log’ option from the HL7 Communications Server Menu.

> Search Transmission Log

> Select one of the following:

> A All Completed Transmissions

> E Event Type Search (Completed)

> L Logical Link Search (Completed)

> P Pending Transmissions

> Q Quit (also uparrow, or \<RETURN\>)

> Selection:

Choose whether to look at all transmissions, transmissions for a particular event type, transmissions over a particular logical link, or all pending transmissions.

For each choice, you are able to further filter the list of messages that are displayed:

|                                 |                                      |
|---------------------------------|--------------------------------------|
| Option                      | Filter By                        |
| All Completed Transactions      | Date Range                           |
| Event Type Search (Completed)   | Date Range, Event Type, Message Type |
| Logical Link Search (Completed) | Date Range, Logical Link             |
| Pending Transmissions           | (all)                                |

## Viewing Message Summaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View Transmission Log option displays summaries of all matching messages in VA FileMan's Browser. Messages are sorted by DATE/TIME PROCESSED value in HL7 Message Administration file (#773). For outgoing messages, this is the date/time that the message was transmitted; for incoming messages, this is the date/time that the receiving application processed the message.

> MESSAGE ID \# Dte/TimeEntr'd Log Link Msg:Evn IO Sndg Apl Rcvr Apl HDR

> 1 071698.075746 INDY-TCP ADT:A01 IN MPI-STAR RG CIRN MSH^

> 3 071698.075746 INDY-TCP ACK:A01 OT RG CIRN MPI-STAR MSH^

> 4 072998.132139 INDY-TCP ADT:A01 IN MPI-STAR RG CIRN MSH^

> 6 072998.132139 INDY-TCP ACK:A01 OT RG CIRN MPI-STAR MSH^

> Col\> 1 \|\<PF1\>H=Help \<PF1\>E=Exit\| Line\> 4 of 4 Screen\> 1 of 1

The following information is displayed for each message:

> MESSAGE ID# Unique Message ID number assigned by the HL7 package to the message.

> Dte/TimeEntr'd Exact time and date the message was first handed to HL7.

> Log Link Logical Link on which the message is to be, or was transmitted.

> Msg:Evn Message Type, Event Type pair indicating the nature of the message.

> IO Indicates whether the message is incoming, ‘IN’, or Outgoing, ‘OT”.

> Sndg Apl Application that is sending the message.

> Rcvr Apl Application to which the message is directed.

> HDR Message header. Use the right arrow key to view continuation of header.

You can use the right arrow key to view the continuation of the header (the full header is available if you scroll right):

> MESSAGE ID \# Dte/TimeEntr'd Log Link Msg:Evn IO Sndg Apl Rcvr Apl HDR

> R RG CIRN MSH^~&\\1600^MPI-STARTUP^NXT^RG CIRN^19980716075643^^ADT~A01^4^P^2.2^

> MPI-STAR MSH^~&\\NXT^RG CIRN^1600^MPI STARTUP^19980716075750^^ACK~A01^4^P^2.2^

> R RG CIRN MSH^~&\\1600^MPI-STARTUP^NXT^RG CIRN^19980716075643^^ADT~A01^4^P^2.2^

> MPI-STAR MSH^~&\\NXT^RG CIRN^1600^MPI STARTUP^19980716075750^^ACK~A01^4^P^2.2^

> Col\> 66 \|\<PF1\>H=Help \<PF1\>E=Exit\| Line\> 4 of 4 Screen\> 1 of 1

You can use all of the standard features of the VA FileMan Browser to search through the list. Some particular features of use are:

|                           |                                                |
|---------------------------|------------------------------------------------|
| Keystroke             | Description                                |
| Left and Right Arrow Keys | View text that is beyond either screen margin. |
| \<PF1\> Arrow Down        | Page Down                                      |
| \<PF1\> Arrow Up          | Page Up                                        |
| \<PF1\>F                  | Find Text                                      |
| \<PF1\>N                  | Find Next                                      |

Documentation on the Browser is provided in the VA FileMan User Manual, and in the Browser's online help (in the Browser, press \<PF1\>H).

## Viewing Message Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While in the View Transmission Log option's main screen, you may want to view the full message text for a particular message.

To view message text:

1.  Press \<PF1\>Z while viewing the transmission log.
2.  At the "Enter Message ID Number:" prompt, enter the Message ID \#. Note: Message IDs are unique for TCP/IP messages.
3.  The Browser displays the requested message. To view characters beyond the right or left margins, use the arrow keys.
4.  To return to the View Transmission Log main screen, enter R (for return).

For example, while viewing the transmission log, to view the message text for Message ID \# 20 in the HL7 Message Text file, press \<PF1\>Z and enter the following:

> Enter Message ID \#: 20 \<ret\>

You would then see the text for that message in the new Browser window:

> HL7 MESSAGE TEXT:\[JUL 16,1998@07:57:46\] (wp): MESSAGE TEXT

> MSA^AA^1

> Col\> 1 \|\<PF1\>H=Help \<PF1\>E=Exit\| Line\> 2 of 2 Screen\> 1 of 1

To return to the View Transmission Log main screen, enter R (for return).

# Exception Processing API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The V*IST*A HL7 package does not currently provide an HL7 exception log, although eventually it will. In the meantime, for packages maintaining their own exception logs, the HL7 package provides an API to enable reprocessing messages that you've logged as exceptions.

## Why Support Only TCP/IP Interfaces?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As originally released in patch HL\*1.6\*36, the Exception Processing API worked for HL7 messages sent over existing transport layers (VA MailMan, DHCP-to-DHCP and serial). As modified by patch HL\*1.6\*19, however, these entry points, for the time being, only work with messages sent over TCP/IP logical links.

The reason for this is that the HL7 package is in the midst of a file conversion. Because enhancements are being released through patches, for the time being only messages sent over TCP/IP use the new file structures. In the future, another patch will convert all remaining messages to use the new file structure. At that point (as with the View Transmission Log option) all messages will be supported by the Exception Processing API entry points.

## How to Handle Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An example of an exception is when an incoming message references an entry in a table that is missing. The message must either be rejected or stored as an exception for later processing.

To deal with exceptions, your message processing routine should:

1\. Store the IEN of the message with a problem in your local exception log. You can get the IEN from the variable HLMTIENS, which is always defined during message processing.

2\. Call \$\$DONTPURG^HLUTIL or \$\$SETPURG^HLUTIL(1) (they're equivalent calls) to prevent the HL PURGE TRANSMISSIONS option from purging the message.

3\. Fix the error condition that is causing the exception.

4\. Call \$\$REPROC^HLUTIL to reprocess the message.

5\. If the reprocessing is successful, call \$\$TOPURG^HLUTIL or \$\$SETPURG^HLUTIL(0) (they're equivalent calls) to once again allow purging of the message by the HL7 package.

## \$\$DONTPURG^HLUTIL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This entry point sets a message's DON'T PURGE flag (#773.10) to prevent a message from being purged by the HL PURGE TRANSMISSIONS option. As of patch HL\*1.6\*19, use only for messages sent over TCP/IP links (you must know this in advance).

\$\$DONTPURG^HLUTIL, \$\$TOPURG^HLUTIL and \$\$SETPURG^HLUTIL should be called only by message processing routines invoked by the HL7 package:

- The PROCESS ROUTINE of an interface
- The PROCESS ACKNOWLEDGEMENT ROUTINE of an interface
- The routine passed as a parameter to \$\$REPROC^HLUTIL(IEN,routine)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>format</strong></td>
<td colspan="2">$$DONTPURG^HLUTIL()</td>
</tr>
<tr class="even">
<td><strong>input</strong></td>
<td>HLMTIENS</td>
<td>IEN of message in File #773. This variable should already be defined if in a message processing context.</td>
</tr>
<tr class="odd">
<td><strong>output<br />
</strong></td>
<td>return value</td>
<td><p>1: The message's purge flag has been set.</p>
<p>-1: The call has failed; nothing has been changed.</p></td>
</tr>
</tbody>
</table>

## \$\$TOPURG^HLUTIL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$\$TOPURG^HLUTIL clears a message's DON'T PURGE flag (#773.10), allowing the message to be purged by the HL PURGE TRANSMISSIONS option. As of patch HL\*1.6\*19, use only for messages sent over TCP/IP links (you must know this in advance).

\$\$DONTPURG^HLUTIL, \$\$TOPURG^HLUTIL and \$\$SETPURG^HLUTIL should be called only by message processing routines invoked by the HL7 package:

- The PROCESS ROUTINE of an interface
- The PROCESS ACKNOWLEDGEMENT ROUTINE of an interface
- The routine passed as a parameter to \$\$REPROC^HLUTIL(IEN,routine)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>format</strong></td>
<td colspan="2">$$TOPURG^HLUTIL()</td>
</tr>
<tr class="even">
<td><strong>input</strong></td>
<td>HLMTIENS</td>
<td>IEN of message in File #773. This variable should already be defined if in a message processing context.</td>
</tr>
<tr class="odd">
<td><strong>output</strong></td>
<td>return value</td>
<td><p>0: The message's purge flag has been cleared.</p>
<p>-1: The call has failed; nothing has been changed.</p></td>
</tr>
</tbody>
</table>

## \$\$SETPURG^HLUTIL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$\$SETPURG^HLUTIL is an alternate entry point that duplicates the functionality of both \$\$TOPURG^HLUTIL and \$\$DONTPURG^HLUTIL.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 72%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>format</strong></td>
<td colspan="2">$$SETPURG^HLUTIL(status)</td>
</tr>
<tr class="even">
<td rowspan="2"><strong>input</strong></td>
<td>status</td>
<td><p>1: Sets the message's purge flag such that the message won't be purged (equivalent to $$DONTPURG^HLUTIL).</p>
<p>0: Sets the message's purge flag such that the message will be purged (equivalent to $$TOPURG^HLUTIL).</p></td>
</tr>
<tr class="odd">
<td>HLMTIENS</td>
<td>IEN of message in File #773. This variable should already be defined if in a message processing context.</td>
</tr>
<tr class="even">
<td><strong>output</strong></td>
<td>return value</td>
<td><p>0: The message's purge flag has been set or cleared.</p>
<p>-1: The call has failed; nothing has been changed.</p></td>
</tr>
</tbody>
</table>

## \$\$REPROC^HLUTIL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This entry point lets you *reprocess* a message. Pass the routine to reprocess the message as a parameter to the API. Reprocessing is essentially the same as when, in an interface, the HL7 package calls an application’s PROCESS ROUTINE (for incoming messages) or PROCESS ACKNOWLEDGEMENT routine (for incoming acknowledgements). As of patch HL\*1.6\*19, use only for messages sent over TCP/IP links (you must know this in advance).

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 74%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>format</strong></td>
<td colspan="2">$$REPROC^HLUTIL(IEN,routine)</td>
</tr>
<tr class="even">
<td rowspan="2"><strong>input</strong></td>
<td>IEN</td>
<td>IEN of the message in file #773 to reprocess.</td>
</tr>
<tr class="odd">
<td>routine</td>
<td>The routine to Xecute to reprocess the message.</td>
</tr>
<tr class="even">
<td><strong>output</strong></td>
<td>return value</td>
<td>0 means call has been successfully completed.<br />
-1 means call has failed; nothing has been changed.</td>
</tr>
</tbody>
</table>

# TCP/IP LLP Implementation Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information in this chapter is useful if you are interfacing a device or system with V*IST*A over TCP/IP and need to know the message format expected by V*IST*A.

The TCP/IP implementation in patch HL7\*1.6\*19 encapsulates HL7 messages using Minimal Lower Layer Protocol (MLLP), rather than Hybrid Lower Layer Protocol (HLLP). MLLP is a very simple protocol, and can be used because the TCP/IP channel itself provides most services needed for error-free transmission of messages, including:

- Connection Handshaking
- Full Duplex Data Transfer
- Error Detection and Retransmission
- Flow Control
- Congestion Control
- Connection Release

Using a particular lower layer protocol is not required by the HL7 Standard but is highly recommended.

MLLP Message Format

The MLLP message format expected by V*IST*A is as follows:

- Start Block = \$C(11)
- End Block = \$C(28)
- Carriage Return = \$C(13)

Start Data End

Block Block Block

\| \| \|

\| \| \|

\|--\|\|----------------------------\|\|------\|

\| \|\| \|\| \|

\<11\>DATA 1\<13\>DATA 2\<13\>DATA 3\<13\>\<28\>\<13\>

^ ^ ^ ^

\| \| \| \|

\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\|

\|

\|

(Carriage Returns)